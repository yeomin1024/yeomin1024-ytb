// VERSION: v1.1 — 2026-10-10 — 파트 라벨 판정을 srt_tool.is_label과 같게: '-숫자'로 시작하는 줄은 문장 (v1.0: 내레이션 오디오에 SRT 타이밍 맞추기, 오디오는 고치지 않음)
// 사용 (video/ 폴더에서):
//   npm run align-audio -- <주제폴더> <영상ID>                예) npm run align-audio -- stock molppang-2026-10
//   옵션: --audio <파일>  --noise -35  --min-pause 0.12  --dry-run  --srt-out <파일>  --no-export
//
// 입력: ../<주제폴더>/source/<영상ID>/<영상ID>.txt, <영상ID>.srt (지금 SRT — 문장별 앞줄·뒷줄 나눔과 예상 길이에 씀),
//       narration.mp3 / .wav / .m4a (또는 --audio)
// 하는 일:
//   1. ffmpeg silencedetect 로 쉼(무음 구간)을 찾는다.
//   2. 동적 계획법으로 문장 경계 N−1개를 쉼에 하나씩 맞춘다. 문장 길이가 예상(지금 SRT 길이 × 말 속도)과 가까울수록,
//      쉼이 길수록 점수가 좋다. [장면] 고지 카드 자리는 3.5초 이상 쉼에만 맞춘다 (없으면 멈춤 — 오디오는 고치지 않으므로).
//   3. 앞줄·뒷줄로 나뉜 문장은 문장 안의 쉼 중 예상 위치에 가장 가까운 곳에서 나눈다 (없으면 예상 비율 위치).
//   4. 자막은 쉼을 덮어 이어 붙이고(빈 화면 없음), 고지 카드 자리만 공백으로 둔다. SRT = 영상 시간.
//   5. 기존 SRT는 <영상ID>.srt.bak-<시각> 으로 남기고 새 SRT를 쓴 뒤, srt_tool.py check 와 remotion 내보내기를 실행한다.
//      영상 길이 = max(마지막 자막 끝 + 1초, 오디오 길이) — 오디오보다 짧게 자르지 않는다.
// ※ 쉼 찾기 결과는 꼭 귀로 확인한다: 보고에 나오는 "확인 필요" 문장은 스튜디오에서 들어 보고 SRT를 손으로 고친다.
import fs from "node:fs";
import path from "node:path";
import {spawnSync} from "node:child_process";
import {fileURLToPath} from "node:url";

const VIDEO = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const ROOT = path.resolve(VIDEO, "..");
const CARD_GAP_MIN = 3.5;
const LEAD_IN_MAX = 2.0;
const log = (stage, kv) => console.log(`[${stage}] [${new Date().toISOString()}] ${Object.entries(kv).map(([k, v]) => `${k}=${v}`).join(" ")}`);

// ── 인자 ──
const argv = process.argv.slice(2);
const opt = (name, def) => {
  const i = argv.indexOf(`--${name}`);
  return i >= 0 ? argv[i + 1] : def;
};
const flag = (name) => argv.includes(`--${name}`);
const BOOL = new Set(["dry-run", "no-export"]);
const pos = [];
for (let i = 0; i < argv.length; i++) {
  if (argv[i].startsWith("--")) {
    if (!BOOL.has(argv[i].slice(2))) i++; // 값이 있는 옵션은 다음 칸을 건너뜀
  } else pos.push(argv[i]);
}
const [topic, id] = pos;
if (!topic || !id) {
  console.error("사용법: npm run align-audio -- <주제폴더> <영상ID> [--audio 파일] [--noise -35] [--min-pause 0.12] [--dry-run]");
  process.exit(1);
}
const dir = path.join(ROOT, topic, "source", id);
const txtPath = opt("txt", path.join(dir, `${id}.txt`));
const srtPath = opt("srt", path.join(dir, `${id}.srt`));
const audioPath = opt("audio", ["mp3", "wav", "m4a"].map((e) => path.join(dir, `narration.${e}`)).find((p) => fs.existsSync(p)));
const noise = Number(opt("noise", "-35"));
const minPause = Number(opt("min-pause", "0.12"));
for (const [k, p] of [["대본", txtPath], ["SRT", srtPath], ["내레이션", audioPath]]) {
  if (!p || !fs.existsSync(p)) {
    log("INPUT", {error: `${k} 파일 없음`, path: p ?? `${dir}/narration.mp3|wav|m4a`, hint: "경로를 확인하거나 --audio 로 지정"});
    process.exit(1);
  }
}

// ── 대본·SRT 읽기 (tools/srt_tool.py 와 같은 규칙) ──
const lines = fs.readFileSync(txtPath, "utf8").replace(/^﻿/, "").split(/\r?\n/).map((l) => l.trim());
const sents = [];
const cards = [];
let inCard = false;
for (const l of lines) {
  if (!l) continue;
  if (l.startsWith("-") && !/^-\s*[\d.,]/.test(l)) {   // 파트 라벨 ('-2,500만 원…'처럼 '-숫자'면 문장)
    inCard = false;
    continue;
  }
  if (l.startsWith("[장면]")) {
    inCard = true;
    cards.push(sents.length); // 이 문장 번호 뒤에 카드
    continue;
  }
  if (!inCard) sents.push(l);
}
const sec = (ts) => {
  const [h, m, r] = ts.trim().split(":");
  const [s, ms] = r.split(",");
  return +h * 3600 + +m * 60 + +s + +ms / 1000;
};
const subs = fs
  .readFileSync(srtPath, "utf8")
  .replace(/^﻿/, "")
  .trim()
  .split(/\r?\n\s*\r?\n/)
  .map((b) => b.trim().split(/\r?\n/))
  .filter((b) => b.length >= 3)
  .map((b) => {
    const [a, c] = b[1].split("-->");
    return {start: sec(a), end: sec(c), text: b.slice(2).map((x) => x.trim()).join(" ")};
  });
const groups = [];
{
  let i = 0;
  for (let n = 1; n <= sents.length; n++) {
    const parts = [];
    let joined = "";
    while (i < subs.length && joined.length < sents[n - 1].length) {
      parts.push(subs[i++]);
      joined = parts.map((p) => p.text).join(" ");
    }
    if (joined !== sents[n - 1]) {
      log("INPUT", {error: `문장 ${n}: SRT와 대본이 다름`, hint: "먼저 python tools/srt_tool.py check 로 맞추세요"});
      process.exit(1);
    }
    groups.push({n, text: sents[n - 1], parts, exp: parts[parts.length - 1].end - parts[0].start});
  }
}
log("INPUT", {txt: path.relative(ROOT, txtPath), srt: path.relative(ROOT, srtPath), audio: path.relative(ROOT, audioPath), sentences: groups.length, subtitles: subs.length, split: groups.filter((g) => g.parts.length > 1).length, cardAfter: cards.join(",") || "없음"});

// ── ffmpeg 로 쉼 찾기 ──
const runFfmpeg = (args) => {
  const env = process.env.FFMPEG;
  const tries = env ? [[env, args]] : [["ffmpeg", args], [process.platform === "win32" ? "npx.cmd" : "npx", ["remotion", "ffmpeg", ...args]]];
  for (const [cmd, a] of tries) {
    const r = spawnSync(cmd, a, {cwd: VIDEO, encoding: "utf8", maxBuffer: 64 * 1024 * 1024, shell: cmd.endsWith(".cmd")});
    if (!r.error && (r.stderr || "").includes("Duration")) return r.stderr;
  }
  log("AUDIO", {error: "ffmpeg 실행 실패", hint: "ffmpeg를 설치하거나 video/ 에서 npm install (Remotion 내장 ffmpeg 사용)"});
  process.exit(1);
};
const t0 = Date.now();
const err = runFfmpeg(["-hide_banner", "-nostats", "-i", audioPath, "-af", `silencedetect=noise=${noise}dB:d=${minPause}`, "-f", "null", "-"]);
const dm = err.match(/Duration:\s*(\d+):(\d+):([\d.]+)/);
const audioSec = +dm[1] * 3600 + +dm[2] * 60 + +dm[3];
let sil = [];
for (const m of err.matchAll(/silence_(start|end):\s*([\d.]+)/g)) {
  if (m[1] === "start") sil.push({s: +m[2], e: audioSec});
  else if (sil.length) sil[sil.length - 1].e = +m[2];
}
const onset = sil.length && sil[0].s <= 0.05 ? sil[0].e : 0;
const offset = sil.length && sil[sil.length - 1].e >= audioSec - 0.05 ? sil[sil.length - 1].s : audioSec;
sil = sil.filter((x) => x.s > onset + 0.01 && x.e < offset - 0.01).map((x) => ({...x, d: x.e - x.s}));
log("AUDIO", {seconds: audioSec.toFixed(2), speechFrom: onset.toFixed(2), speechTo: offset.toFixed(2), pauses: sil.length, noise: `${noise}dB`, minPause, ms: Date.now() - t0});

// ── 동적 계획법: 문장 경계 N−1개를 쉼에 맞춤 ──
const N = groups.length;
const cardSet = new Set(cards);
const S = sil.length;
if (S < N - 1) {
  log("ALIGN", {error: `쉼 ${S}개 < 필요한 경계 ${N - 1}개`, hint: "--noise 를 -30 으로 올리거나 --min-pause 를 0.08 로 낮추세요"});
  process.exit(1);
}
const align = (rate) => {
  // dp[i][j]: 문장 1..i 를 끝내고 경계 i 를 쉼 j 에 둔 최소 비용
  const INF = 1e18;
  const dp = Array.from({length: N}, () => new Float64Array(S).fill(INF));
  const from = Array.from({length: N}, () => new Int32Array(S).fill(-1));
  const sentCost = (i, a, b) => {
    const dur = b - a;
    const e = groups[i].exp * rate;
    if (dur <= 0.2) return INF;
    const sd = 0.25 * e + 0.35;
    return ((dur - e) / sd) ** 2;
  };
  const pauseBonus = (j) => 2.0 * Math.log(1 + sil[j].d / 0.15);
  for (let j = 0; j < S; j++) {
    if (cardSet.has(1) && sil[j].d < CARD_GAP_MIN) continue;
    dp[0][j] = sentCost(0, onset, sil[j].s) - pauseBonus(j);
  }
  for (let i = 1; i < N - 1; i++) {
    const needCard = cardSet.has(i + 1);
    for (let j = i; j < S; j++) {
      if (needCard && sil[j].d < CARD_GAP_MIN) continue;
      if (!needCard && sil[j].d >= CARD_GAP_MIN && cards.length) continue; // 고지 공백은 카드 자리에만
      let best = INF;
      let arg = -1;
      for (let k = j - 1; k >= i - 1; k--) {
        if (dp[i - 1][k] >= INF) continue;
        const dur = sil[j].s - sil[k].e;
        if (dur > groups[i].exp * rate * 3 + 4) break; // 너무 긴 문장 후보는 건너뜀
        const c = dp[i - 1][k] + sentCost(i, sil[k].e, sil[j].s);
        if (c < best) {
          best = c;
          arg = k;
        }
      }
      if (arg >= 0) {
        dp[i][j] = best - pauseBonus(j);
        from[i][j] = arg;
      }
    }
  }
  let best = Infinity;
  let last = -1;
  for (let k = 0; k < S; k++) {
    if (dp[N - 2][k] >= INF) continue;
    const c = dp[N - 2][k] + sentCost(N - 1, sil[k].e, offset);
    if (c < best) {
      best = c;
      last = k;
    }
  }
  if (last < 0) return null;
  const pick = new Array(N - 1);
  pick[N - 2] = last;
  for (let i = N - 2; i > 0; i--) pick[i - 1] = from[i][pick[i]];
  return {pick, cost: best};
};
const expTotal = groups.reduce((s, g) => s + g.exp, 0);
let rate = (offset - onset - sil.reduce((s, x) => s + (x.d >= CARD_GAP_MIN ? x.d : 0), 0) - (N - 1) * 0.45) / expTotal;
let res = null;
for (let it = 0; it < 3; it++) {
  res = align(rate);
  if (!res) break;
  const speech = groups.reduce((s, _, i) => {
    const a = i === 0 ? onset : sil[res.pick[i - 1]].e;
    const b = i === N - 1 ? offset : sil[res.pick[i]].s;
    return s + (b - a);
  }, 0);
  rate = speech / expTotal; // 실제 말 속도로 다시
}
if (!res) {
  log("ALIGN", {error: "맞출 수 없음 (고지 카드 자리의 3.5초 이상 쉼이 없을 수 있음)", hint: "오디오는 고치지 않습니다 — 녹음에 카드 자리 쉼(3.5초+)이 있는지 확인"});
  process.exit(1);
}

// ── 문장·자막 시간 만들기 ──
const out = [];
const report = [];
for (let i = 0; i < N; i++) {
  const g = groups[i];
  const a = i === 0 ? onset : sil[res.pick[i - 1]].e;
  const speechEnd = i === N - 1 ? offset : sil[res.pick[i]].s;
  const next = i === N - 1 ? Math.min(audioSec, offset + 0.4) : sil[res.pick[i]].e;
  const end = cardSet.has(i + 1) || i === N - 1 ? (i === N - 1 ? next : speechEnd + 0.15) : next; // 카드 자리만 공백
  const dur = speechEnd - a;
  const dev = (dur - g.exp * rate) / (g.exp * rate);
  let splitAt = null;
  let how = "";
  if (g.parts.length > 1) {
    const frac = (g.parts[0].end - g.parts[0].start) / g.exp;
    const want = a + dur * frac;
    const inner = sil.filter((x) => x.s > a + 0.3 && x.e < speechEnd - 0.3);
    const near = inner.map((x) => ({x, dist: Math.abs((x.s + x.e) / 2 - want)})).filter((o) => o.dist < dur * 0.25).sort((p, q) => p.dist - q.dist)[0];
    if (near) {
      splitAt = near.x.e - 0.05;
      how = "쉼";
    } else {
      splitAt = want;
      how = "비율";
    }
  }
  const startT = i === 0 ? Math.max(0, a - 0.1) : a;
  if (splitAt === null) out.push({start: startT, end, text: g.text});
  else {
    out.push({start: startT, end: splitAt, text: g.parts[0].text});
    out.push({start: splitAt, end, text: g.parts[1].text});
  }
  if (Math.abs(dev) > 0.35 || how === "비율") report.push(`문장 ${g.n}: 길이 ${dur.toFixed(2)}초 (예상 ${(g.exp * rate).toFixed(2)}초, ${(dev * 100).toFixed(0)}%)${how === "비율" ? ", 앞줄·뒷줄을 비율로 나눔" : ""}`);
}
const firstSubOf = (n) => groups.slice(0, n - 1).reduce((acc, g) => acc + g.parts.length, 0); // 문장 n 첫 자막의 out 위치
const cardGaps = cards.map((n) => ({n, gap: out[firstSubOf(n + 1)].start - out[firstSubOf(n + 1) - 1].end}));
log("ALIGN", {rate: rate.toFixed(3), cost: res.cost.toFixed(1), subtitles: out.length, cardGap: cardGaps.map((c) => `문장${c.n}뒤 ${c.gap.toFixed(2)}초`).join(",") || "없음", lastEnd: out.at(-1).end.toFixed(2), audio: audioSec.toFixed(2), checkNeeded: report.length});
for (const r of report) console.log(`  ⚠️ 확인 필요 ${r}`);
if (out[0].start > LEAD_IN_MAX) console.log(`  ⚠️ 첫 자막이 ${out[0].start.toFixed(2)}초에 시작 (2초 넘음) — 오디오 앞 여백이 김`);

// ── 쓰기 ──
const ts = (t) => {
  let ms = Math.round(t * 1000);
  const h = Math.floor(ms / 3600000);
  ms -= h * 3600000;
  const m = Math.floor(ms / 60000);
  ms -= m * 60000;
  const s = Math.floor(ms / 1000);
  ms -= s * 1000;
  const p = (v, n = 2) => String(v).padStart(n, "0");
  return `${p(h)}:${p(m)}:${p(s)},${p(ms, 3)}`;
};
const body = out.map((s, i) => `${i + 1}\n${ts(s.start)} --> ${ts(s.end)}\n${s.text}`).join("\n\n") + "\n";
if (flag("dry-run")) {
  log("WRITE", {dryRun: true, note: "SRT를 쓰지 않음"});
  process.exit(0);
}
const target = opt("srt-out", srtPath);
if (target === srtPath) {
  const bak = `${srtPath}.bak-${new Date().toISOString().replace(/[:.]/g, "-")}`;
  fs.copyFileSync(srtPath, bak);
  log("WRITE", {backup: path.relative(ROOT, bak)});
}
fs.writeFileSync(target, body);
log("WRITE", {srt: path.relative(ROOT, target), subtitles: out.length});

// ── 검사·영상용 내보내기 ──
const py = ["python3", "python", "py"].find((p) => !spawnSync(p, ["--version"]).error);
const tool = path.join(ROOT, "tools", "srt_tool.py");
const chk = spawnSync(py, [tool, "check", txtPath, target], {encoding: "utf8"});
process.stdout.write(chk.stdout || "");
if (!flag("no-export")) {
  const ep = path.join(VIDEO, "src", "episodes", id);
  if (fs.existsSync(ep)) {
    const ext = path.extname(audioPath);
    const pub = path.join(VIDEO, "public", "audio", `${id}${ext}`);
    fs.mkdirSync(path.dirname(pub), {recursive: true});
    fs.copyFileSync(audioPath, pub); // 원본 그대로 복사 (오디오는 고치지 않음)
    const r = spawnSync(py, [tool, "remotion", txtPath, target, path.join(ep, "subtitles.ts"), "--audio-seconds", audioSec.toFixed(3), "--audio-file", `audio/${id}${ext}`], {encoding: "utf8"});
    process.stdout.write(r.stdout || r.stderr || "");
  } else {
    log("EXPORT", {skip: `video/src/episodes/${id} 없음 (영상 코드를 만든 뒤 다시 실행)`});
  }
}
process.exit(chk.status ?? 0);
