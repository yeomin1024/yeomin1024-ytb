// VERSION: v1.6 — 2026-10-16 — three.js(jsdelivr three@0.160.0) 를 로컬 node_modules 로 (gsap 처럼) · 낱말 검사 예외에 SPY (주식 1번 v2 3D 장면).
// v1.5 — 2026-10-16 — 낱말 검사 예외에 HOLD (계좌 칸 'BUY & HOLD' — 사용자 지시 2026-10-16 "1번째 박스에는 맨처음에 매수하고 그냥 냅둔 수익도 표시해").
// v1.4 — 2026-10-16 — 낱말 검사에서 BUY·SELL(사용자 지시 2026-10-16 "buy, sell 문구 붙여서 표시하고")과 지표 이름 RSI·VIX 도 뺌 (stock/guides/README.md 4번).
// v1.3 — 2026-10-16 — 낱말 검사에서 지수 이름 'NASDAQ' 도 뺌 (S&P 와 같은 고유 이름 — 주식 1번 v2 확인 장면 '나스닥 2000·2003 시작', stock/guides/README.md 4번).
// v1.2 — 2026-10-16 — video --estimated-preview: 추정 시각(오디오 전)으로 소리 없는 미리보기만 렌더 (<주제>/out/<영상ID>/preview_estimated_silent.mp4 —
//   final_1080p.mp4·음량 맞춤·Drive 는 하지 않음). 옵션 없이는 예전처럼 거부. 사용자 지시 2026-10-16 "영상도 렌더링 해봐" (오디오 아직 없음).
// v1.1 — 2026-10-15 — sync --estimate (오디오 전 추정 시각 — 장면 배치·still 점검용, video 모드는 거부), 자막 없는 영상(#cc 없음)은
//   검사 아래 한계를 y 1020(유튜브 진행 막대 60px 비움 — stock/guides/README.md 4번), K.init opts.noWords 면 화면 글자에 낱말(한글·가나·한자·영어 2글자 이상, S&P·코드 카드 .code 빼고)이
//   있는지도 검사. 사용자 지시 2026-10-15 "영상에 자막 달지말고".
// v1.0 — 2026-10-15 — 새 스타일 영상 렌더기 (guides/video_guide.md v4.0 6번 '할 일': 시안 render.js 를 옮겨 1080p·오디오 붙이기·자막 굽기)
//   장면 파일 video/episodes/<영상ID>/index.html (GSAP 타임라인, kit.js) 을 Playwright 로 열어 1/30초마다 SB.seek(t) → 찍은 장면을 ffmpeg 로
//   이어 H.264 → narration.mp3 를 붙임 → tools/loudnorm.py (-14 LUFS, 트루 피크 -1.5 dBTP 이하). 오디오는 고치지 않는다.
//   연구·교육용 영상 — 투자·세무 권유 아님.
// 사용 (저장소 최상위에서):
//   node video/render/render.mjs sync   <주제> <영상ID>     # 문장 시각(tts_narration.json)·자막(SRT)·길이를 index.html 데이터 칸에 넣음
//   node video/render/render.mjs sync   <주제> <영상ID> --estimate   # 오디오 전: 대본 음절로 추정한 시각 (EP.estimated — 렌더 안 됨)
//   node video/render/render.mjs check  <주제> <영상ID>     # 대표 장면(K.cut)마다 글자 크기·자막 띠 겹침·화면 밖 검사 (+ 0.5초마다 겹침만)
//   node video/render/render.mjs stills <주제> <영상ID> [--out <폴더>] [--w 1280]   # 대표 장면 still (저장소 밖 — 기본 임시 폴더)
//   node video/render/render.mjs extra  <주제> <영상ID> --times 12.5,40 [--out <폴더>]
//   node video/render/render.mjs video  <주제> <영상ID> [--workers 3] [--from 0 --to 60] [--crf 18]
//        → <주제>/out/<영상ID>/final_1080p.mp4 (--from/--to 면 preview_<from>-<to>.mp4, 음량 맞춤 없음)
//   node video/render/render.mjs video  <주제> <영상ID> --estimated-preview   # 오디오 전 추정 시각 — 소리 없는 미리보기만 (최종본 아님)
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { spawn, spawnSync, execSync } from "node:child_process";
import { createRequire } from "node:module";
import { fileURLToPath } from "node:url";

const HERE = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(HERE, "..", "..");
const VERSION = "v1.6";                        // 로그 [RENDER] tool= 에 찍힘 (v1.4~v1.6 때 올리지 않았던 것을 맞춤)
const log = (stage, kv) => console.log(`[${stage}] [${new Date().toISOString().slice(0, 19)}Z] ` +
  Object.entries(kv).map(([k, v]) => `${k}=${typeof v === "string" && /\s/.test(v) ? JSON.stringify(v) : v}`).join(" "));

const argv = process.argv.slice(2);
const opt = (name, def) => { const i = argv.indexOf(`--${name}`); return i >= 0 ? argv[i + 1] : def; };
const pos = argv.filter((a, i) => !a.startsWith("--") && !(i > 0 && argv[i - 1].startsWith("--")));
const [MODE, TOPIC, ID] = pos;
if (!MODE || !TOPIC || !ID) {
  console.error("사용: node video/render/render.mjs <sync|check|stills|extra|video> <주제> <영상ID> [옵션]");
  process.exit(2);
}
const SRC = path.join(ROOT, TOPIC, "source", ID);
const EPDIR = path.join(ROOT, "video", "episodes", ID);
const PAGE = path.join(EPDIR, "index.html");
const AUDIO = ["mp3", "wav", "m4a"].map(e => path.join(SRC, `narration.${e}`)).find(f => fs.existsSync(f));

function fail(stage, msg, next) {
  log(stage, { level: "error", msg, next: next || "-" });
  process.exit(1);
}

// ---------- sync: 문장 시각·자막·길이 → index.html ----------
function parseSrt(text) {
  const out = [];
  for (const block of text.replace(/\r/g, "").split(/\n\n+/)) {
    const lines = block.trim().split("\n");
    const i = lines.findIndex(l => l.includes("-->"));
    if (i < 0) continue;
    const [a, b] = lines[i].split("-->").map(s => s.trim()).map(s => {
      const m = s.match(/(\d+):(\d+):(\d+)[,.](\d+)/);
      return +m[1] * 3600 + +m[2] * 60 + +m[3] + +m[4] / 1000;
    });
    out.push([+a.toFixed(3), +b.toFixed(3), lines.slice(i + 1).join("\n")]);
  }
  return out;
}
function probeDuration(f) {
  const r = spawnSync("ffprobe", ["-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f], { encoding: "utf-8" });
  return parseFloat(r.stdout);
}
// 추정 시각 모델 (2026-10-15, 진행자 H04 실제 오디오 4개 — 재테크 toejik·isa·eunte·gicho — 문장 길이 최소제곱):
//   문장 길이 ≈ 0.151초 × 읽는 음절(srt_tool.syllables) + 0.25초 × 쉼표 − 0.08초 (평균 오차 0.2초), 쉼 = tts_narration 기본값.
const EST = { perSyl: 0.151, comma: 0.25, base: -0.08, min: 0.8, lead: 0.3, gap: 0.45, part: 1.0, tail: 0.8 };
function estimateSync() {
  const txt = path.join(SRC, `${ID}.txt`);
  if (!fs.existsSync(txt)) fail("SYNC", `대본 없음 ${path.relative(ROOT, txt)}`);
  const py = `import sys, json
sys.path.insert(0, sys.argv[2])
import srt_tool
from pathlib import Path
rows, part, card = [], "", False
for raw in Path(sys.argv[1]).read_text("utf-8-sig").splitlines():
    line = raw.strip()
    if not line:
        continue
    if srt_tool.is_label(line):
        part, card = line.lstrip("-").strip(), False
        continue
    if line.startswith("[장면]"):
        card = True
        continue
    if not card:
        rows.append([line, part, srt_tool.syllables(line)])
assert [r[0] for r in rows] == srt_tool.parse_txt(sys.argv[1]), "문장 판정이 srt_tool 과 다름"
print(json.dumps({"rows": rows, "cards": len(srt_tool.parse_cards(sys.argv[1]))}, ensure_ascii=False))`;
  const r = spawnSync("python3", ["-c", py, txt, path.join(ROOT, "tools")], { encoding: "utf-8" });
  if (r.status !== 0) fail("SYNC", "대본 읽기 실패: " + (r.stderr || "").trim().split("\n").pop(), "python3 tools/srt_tool.py check 로 대본 확인");
  const { rows, cards } = JSON.parse(r.stdout);
  if (cards) log("SYNC", { level: "warn", note: "고지 카드 쉼은 추정에 넣지 않음", cards });
  let t = EST.lead;
  const sent = rows.map(([text, part, syl], i) => {
    const d = Math.max(EST.min, EST.perSyl * syl + EST.comma * (text.match(/,/g) || []).length + EST.base);
    const it = { n: i + 1, part, text, start: +t.toFixed(3), end: +(t + d).toFixed(3) };
    t += d + (i === rows.length - 1 ? EST.tail : rows[i + 1][1] !== part ? EST.part : EST.gap);
    return it;
  });
  const D = +t.toFixed(2);
  const ep = { id: ID, topic: TOPIC, duration: D, audio: null, estimated: true, est_model: EST,
    synced: new Date().toISOString().slice(0, 19) + "Z", sent, subs: [] };
  writeEp(ep);
  log("SYNC", { video: ID, mode: "estimate", sentences: sent.length, syllables: rows.reduce((a, x) => a + x[2], 0), duration_s: D,
    note: "오디오가 생기면 sync 로 다시 (이 시각으로는 video 를 만들지 않음)", file: path.relative(ROOT, PAGE) });
}
function writeEp(ep) {
  if (!fs.existsSync(PAGE)) fail("SYNC", `장면 파일 없음 ${path.relative(ROOT, PAGE)}`, "Claude 가 장면 파일을 먼저 만든다 (video_guide 7번)");
  const html = fs.readFileSync(PAGE, "utf-8");
  const re = /\/\*EP-DATA:BEGIN\*\/[\s\S]*?\/\*EP-DATA:END\*\//;
  if (!re.test(html)) fail("SYNC", "index.html 에 /*EP-DATA:BEGIN*/ … /*EP-DATA:END*/ 칸이 없음");
  fs.writeFileSync(PAGE, html.replace(re, `/*EP-DATA:BEGIN*/window.EP=${JSON.stringify(ep)};/*EP-DATA:END*/`));
}
function sync() {
  if (argv.includes("--estimate")) return estimateSync();
  if (!AUDIO) fail("SYNC", `오디오 없음 (${path.relative(ROOT, SRC)}/narration.*)`, "오디오가 생긴 뒤에만 영상 (video_guide 0번)");
  const meta = JSON.parse(fs.readFileSync(path.join(SRC, "tts_narration.json"), "utf-8"));
  const srt = parseSrt(fs.readFileSync(path.join(SRC, `${ID}.srt`), "utf-8"));
  const aDur = probeDuration(AUDIO);
  const D = +Math.max(aDur, srt.length ? srt[srt.length - 1][1] + 1.0 : 0).toFixed(2);
  const sent = meta.items.map(it => ({ n: it.n, part: it.part, text: it.text, start: it.start, end: it.end }));
  if (Math.abs(meta.seconds - aDur) > 0.5) log("SYNC", { level: "warn", note: "tts_narration.json 길이와 오디오 길이가 다름", meta_s: meta.seconds, audio_s: aDur.toFixed(2) });
  const ep = { id: ID, topic: TOPIC, duration: D, audio: path.relative(EPDIR, AUDIO).split(path.sep).join("/"),
    synced: new Date().toISOString().slice(0, 19) + "Z", tts: meta.created, script_sha1: meta.script_sha1, sent, subs: srt };
  writeEp(ep);
  log("SYNC", { video: ID, sentences: sent.length, subs: srt.length, audio_s: aDur.toFixed(2), duration_s: D, file: path.relative(ROOT, PAGE) });
}

// ---------- 브라우저 ----------
async function loadPlaywright() {
  try { return (await import("playwright")).default; } catch { /* 전역 설치본 */ }
  const req = createRequire(import.meta.url);
  return req(path.join(execSync("npm root -g", { encoding: "utf-8" }).trim(), "playwright"));
}
async function openPage(pw, width) {
  let browser;
  try { browser = await pw.chromium.launch(); }
  catch { browser = await pw.chromium.launch({ executablePath: "/opt/pw-browsers/chromium" }); }
  const page = await browser.newPage({ viewport: { width: width || 1920, height: Math.round((width || 1920) * 9 / 16) }, deviceScaleFactor: 1 });
  const GSAP = path.join(HERE, "node_modules", "gsap", "dist", "gsap.min.js");
  if (!fs.existsSync(GSAP)) fail("RENDER", "gsap 없음", "cd video/render && npm install");
  const THREE_JS = path.join(HERE, "node_modules", "three", "build", "three.min.js");   // v1.6
  await page.route(/^https?:\/\//, r => {                     // gsap·three(CDN)은 로컬 파일로, 그 밖의 인터넷 요청은 막음 (렌더는 로컬 파일만)
    const u = r.request().url();
    if (/cdnjs\.cloudflare\.com\/ajax\/libs\/gsap\//.test(u)) return r.fulfill({ path: GSAP, contentType: "application/javascript" });
    if (/three@0\.160\.0\/build\/three\.min\.js/.test(u)) {
      if (!fs.existsSync(THREE_JS)) fail("RENDER", "three 없음", "cd video/render && npm install");
      return r.fulfill({ path: THREE_JS, contentType: "application/javascript" });
    }
    return r.abort();
  });
  const errs = [];
  page.on("pageerror", e => { errs.push(e.message); log("PAGEERROR", { msg: JSON.stringify(e.message) }); });
  page.on("console", m => { if (m.type() === "error") { errs.push(m.text()); log("CONSOLE", { msg: JSON.stringify(m.text()) }); } });
  await page.goto("file://" + PAGE + "?render=1");
  await page.waitForFunction(() => window.SB && window.SB.ready, null, { timeout: 30000 }).catch(() => fail("RENDER", "장면 파일이 준비되지 않음 (SB.ready)", "브라우저 오류 줄 확인: " + errs.join(" | ")));
  await page.evaluate(async () => { await Promise.all([500, 700, 900].map(w => document.fonts.load(`${w} 100px "Noto Sans KR"`, "가나다0"))); await document.fonts.ready; });
  if (width && width !== 1920) await page.evaluate(w => { document.getElementById("stage").style.transform = `scale(${w / 1920})`; document.getElementById("wrap").style.cssText = `width:${w}px;height:${Math.round(w * 9 / 16)}px`; }, width);
  return { browser, page, errs };
}

// ---------- check: 글자 크기·자막 띠·화면 밖 ----------
const CHECK_FN = () => {
  const st = document.getElementById("stage");
  const out = [];
  const cc0 = document.getElementById("cc");
  const LOW = cc0 ? 884 : 1020;                // 자막 띠 위 · 자막 없는 영상은 맨 아래 60px(진행 막대·자동 자막) 위
  const NOWORDS = !!(window.K && window.K.opt && window.K.opt.noWords);
  const op = el => { let o = 1; for (let e = el; e && e !== st; e = e.parentElement) { const cs = getComputedStyle(e); o *= +cs.opacity; if (cs.display === "none" || cs.visibility === "hidden") return 0; } return o; };
  const walker = document.createTreeWalker(st, NodeFilter.SHOW_TEXT);
  for (let n = walker.nextNode(); n; n = walker.nextNode()) {
    if (!n.textContent.trim()) continue;
    const el = n.parentElement;
    if (el.closest("#cc")) continue;
    const o = op(el);
    if (o < 0.3) continue;
    const r = document.createRange(); r.selectNodeContents(n);
    const b = r.getBoundingClientRect();
    if (!b.width) continue;
    const fs = parseFloat(getComputedStyle(el).fontSize);
    const txt = n.textContent.trim().slice(0, 24);
    if (fs < 36) out.push({ kind: "글자 36px 미만", txt, fs });
    if (NOWORDS && !el.closest(".code") && (/[가-힣ぁ-んァ-ン一-龥]/.test(n.textContent) || /[A-Za-z]{2,}/.test(n.textContent.replace(/S&P|NASDAQ|BUY|SELL|HOLD|RSI|VIX|SPY/g, ""))))
      out.push({ kind: "낱말(언어 없는 화면)", txt });   // K.init opts.noWords — 숫자·기호·A·B·S&P·NASDAQ 만 (stock/guides/README.md 4번)
    if (b.bottom > LOW && !el.closest("#chip")) out.push({ kind: cc0 ? "자막 띠(y 880 아래)와 겹침" : "맨 아래 60px(y 1020 아래)", txt, bottom: Math.round(b.bottom) });
    if (b.left < 40 || b.right > 1880 || b.top < 30) out.push({ kind: "화면 가장자리 밖", txt, left: Math.round(b.left), right: Math.round(b.right), top: Math.round(b.top) });
  }
  // 자막 띠 줄 수
  const cc = document.getElementById("cc");
  if (cc && cc.textContent.trim()) { const lines = Math.round(cc.getBoundingClientRect().height / (52 * 1.3)); if (lines > 2) out.push({ kind: "자막 3줄 이상", txt: cc.textContent.slice(0, 24), lines }); }
  return out;
};
async function check() {
  const pw = await loadPlaywright();
  const { browser, page, errs } = await openPage(pw, 1920);
  const { D, cuts } = await page.evaluate(() => ({ D: window.SB.D, cuts: window.SB.cuts }));
  let bad = 0;
  const seen = new Set();
  const times = [...cuts.map(c => [c.t, c.name]), ...Array.from({ length: Math.floor(D / 0.5) }, (_, i) => [i * 0.5, ""])];
  for (const [t, name] of times) {
    await page.evaluate(x => window.SB.seek(x), t);
    for (const p of await page.evaluate(CHECK_FN)) {
      const key = p.kind + "|" + p.txt;
      if (seen.has(key)) continue;
      seen.add(key);
      bad++;
      log("CHECK", { t: t.toFixed(2), cut: name || "-", ...p });
    }
  }
  log("CHECK", { video: ID, cuts: cuts.length, samples: times.length, problems: bad, page_errors: errs.length });
  await browser.close();
  process.exit(bad || errs.length ? 1 : 0);
}

// ---------- stills / extra ----------
async function stills(times) {
  const pw = await loadPlaywright();
  const W = Number(opt("w", 1280));
  const { browser, page } = await openPage(pw, W);
  const outDir = opt("out", path.join(os.tmpdir(), "video_stills", ID));
  fs.mkdirSync(outDir, { recursive: true });
  const list = times || (await page.evaluate(() => window.SB.cuts)).map(c => [c.t, c.name]);
  for (const [i, [t, name]] of list.entries()) {
    await page.evaluate(x => window.SB.seek(x), t);
    const f = path.join(outDir, `${String(i + 1).padStart(3, "0")}_${t.toFixed(1)}s.jpg`);
    await page.screenshot({ path: f, type: "jpeg", quality: 85 });
    log("STILL", { n: i + 1, t: t.toFixed(2), name: name || "-", file: f });
  }
  await browser.close();
}

// ---------- video ----------
async function renderChunk(pw, from, to, fps, file, crf, tag) {
  const { browser, page } = await openPage(pw, 1920);
  const ff = spawn("ffmpeg", ["-y", "-v", "error", "-f", "image2pipe", "-framerate", String(fps), "-i", "-", "-c:v", "libx264", "-preset", "fast",
    "-crf", String(crf), "-pix_fmt", "yuv420p", "-r", String(fps), file], { stdio: ["pipe", "inherit", "inherit"] });
  const t0 = Date.now();
  for (let i = from; i < to; i++) {
    await page.evaluate(t => window.SB.seek(t), i / fps);
    const buf = await page.screenshot({ type: "jpeg", quality: 92 });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once("drain", r));
    if ((i - from) % 900 === 0) log("FRAME", { worker: tag, i, of: `${from}-${to - 1}`, sec: ((Date.now() - t0) / 1000).toFixed(0) });
  }
  ff.stdin.end();
  await new Promise((res, rej) => ff.on("close", c => (c === 0 ? res() : rej(new Error("ffmpeg exit " + c)))));
  await browser.close();
}
async function video() {
  const t0 = Date.now();
  const fps = Number(opt("fps", 30)), crf = Number(opt("crf", 18));
  const html = fs.readFileSync(PAGE, "utf-8");
  const m = html.match(/window\.EP=(\{[\s\S]*?\});\/\*EP-DATA:END\*\//);
  if (!m) fail("RENDER", "데이터 칸이 비었음", `node video/render/render.mjs sync ${TOPIC} ${ID}`);
  const ep = JSON.parse(m[1]);
  const estPreview = !!ep.estimated && argv.includes("--estimated-preview");
  if (ep.estimated && !estPreview) fail("RENDER", "추정 시각(오디오 전)으로는 영상을 만들지 않음", `오디오가 생기면 node video/render/render.mjs sync ${TOPIC} ${ID} (미리보기만: --estimated-preview)`);
  if (estPreview) log("RENDER", { level: "warn", note: "추정 시각 미리보기 — 소리 없음, 최종본 아님 (오디오가 오면 sync 뒤 다시 렌더)" });
  const from = opt("from") ? Number(opt("from")) : 0, to = opt("to") ? Number(opt("to")) : ep.duration;
  const preview = opt("from") != null || opt("to") != null || estPreview;
  const F0 = Math.round(from * fps), F1 = Math.ceil(to * fps);
  const workers = Math.max(1, Math.min(Number(opt("workers", Math.max(1, os.cpus().length - 1))), 6));
  const outDir = path.join(ROOT, TOPIC, "out", ID);
  fs.mkdirSync(outDir, { recursive: true });
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), `render_${ID}_`));
  log("RENDER", { video: ID, tool: `render.mjs ${VERSION}`, frames: F1 - F0, fps, from, to: to.toFixed(2), workers, crf, tmp });
  const pw = await loadPlaywright();
  const per = Math.ceil((F1 - F0) / workers);
  const chunks = Array.from({ length: workers }, (_, k) => [F0 + k * per, Math.min(F1, F0 + (k + 1) * per), path.join(tmp, `chunk_${k}.mp4`)]).filter(c => c[0] < c[1]);
  await Promise.all(chunks.map(([a, b, f], k) => renderChunk(pw, a, b, fps, f, crf, k)));
  fs.writeFileSync(path.join(tmp, "list.txt"), chunks.map(c => `file '${c[2]}'`).join("\n"));
  const out = path.join(outDir, estPreview ? "preview_estimated_silent.mp4" : preview ? `preview_${from}-${Math.round(to)}.mp4` : "final_1080p.mp4");
  const args = ["-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", path.join(tmp, "list.txt")];
  if (AUDIO && !estPreview) args.push("-ss", String(from), "-t", String(to - from), "-i", AUDIO, "-map", "0:v", "-map", "1:a", "-c:a", "aac", "-b:a", "192k");
  args.push("-c:v", "copy", "-movflags", "+faststart", out);
  const r = spawnSync("ffmpeg", args, { stdio: "inherit" });
  if (r.status !== 0) fail("RENDER", "ffmpeg 이어 붙이기 실패", `조각은 ${tmp} 에 남음`);
  const dur = probeDuration(out);
  const a = spawnSync("ffprobe", ["-v", "error", "-select_streams", "a", "-show_entries", "stream=codec_name", "-of", "csv=p=0", out], { encoding: "utf-8" }).stdout.trim();
  log("RENDER", { file: path.relative(ROOT, out), duration_s: dur.toFixed(2), audio: a || "없음", mb: (fs.statSync(out).size / 1e6).toFixed(1), sec: ((Date.now() - t0) / 1000).toFixed(0) });
  fs.rmSync(tmp, { recursive: true, force: true });
  if (!preview) {
    const ln = spawnSync("python3", [path.join(ROOT, "tools", "loudnorm.py"), out], { stdio: "inherit" });
    if (ln.status !== 0) fail("LOUDNORM", "음량 맞춤 실패 (렌더 파일은 그대로)", `python3 tools/loudnorm.py ${path.relative(ROOT, out)}`);
  }
  log("DONE", { file: path.relative(ROOT, out), sec: ((Date.now() - t0) / 1000).toFixed(0) });
}

if (MODE === "sync") sync();
else if (MODE === "check") await check();
else if (MODE === "stills") await stills();
else if (MODE === "extra") await stills((opt("times") || "").split(",").filter(Boolean).map(Number).map(t => [t, ""]));
else if (MODE === "video") await video();
else fail("START", `모르는 모드 ${MODE}`);
