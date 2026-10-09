// 스토리보드 + 장면 구성표 생성 (guides/video_guide.md 5·6번)
//   node scripts/storyboard.mjs <영상ID> <출력폴더> [--only S05,S13] [--full]
//   예) node scripts/storyboard.mjs multagi-2026-10 ../stock/out/multagi-2026-10
// - src/episodes/<영상ID>/plan.ts 를 읽어 <출력폴더>/scene_plan.md 를 만든다
// - 장면마다 "마지막 자막 끝 10프레임 전" still(+ plan의 shots)을 <출력폴더>/storyboard/ 에 JPG로 렌더하고 index.html 을 만든다
// - 번들은 한 번만 하고 브라우저 하나로 still을 연속 렌더한다 (속도 규칙)
// - 브라우저: 환경변수 REMOTION_BROWSER (없으면 Remotion 기본 브라우저)
import fs from "node:fs";
import path from "node:path";
import {fileURLToPath, pathToFileURL} from "node:url";
import {build} from "esbuild";
import {bundle} from "@remotion/bundler";
import {openBrowser, renderStill, selectComposition} from "@remotion/renderer";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const [id, outArg, ...rest] = process.argv.slice(2);
if (!id || !outArg) {
  console.error("사용법: node scripts/storyboard.mjs <영상ID> <출력폴더> [--only S05,S13] [--full]");
  process.exit(1);
}
const only = (() => {
  const i = rest.indexOf("--only");
  return i >= 0 ? new Set(rest[i + 1].split(",")) : null;
})();
const scale = rest.includes("--full") ? 1 : 0.5;
const outDir = path.resolve(process.cwd(), outArg);
const sbDir = path.join(outDir, "storyboard");
fs.mkdirSync(sbDir, {recursive: true});
const log = (stage, kv) => console.log(`[${stage}] [${new Date().toISOString()}] ${Object.entries(kv).map(([k, v]) => `${k}=${v}`).join(" ")}`);

// ── 1. plan.ts · subtitles.ts · timeline.ts 를 esbuild로 묶어서 읽기 ──
const ep = path.join(root, "src", "episodes", id);
const tmp = path.join(root, ".remotion", `plan-${id}.mjs`);
fs.mkdirSync(path.dirname(tmp), {recursive: true});
await build({
  stdin: {
    contents: `export {PLAN_ROWS} from "./src/episodes/${id}/plan"; export {SRC} from "./src/episodes/${id}/subtitles"; export {makeTimeline} from "./src/components/timeline"; export {FPS} from "./src/design/tokens";`,
    resolveDir: root,
    loader: "ts",
  },
  bundle: true,
  format: "esm",
  platform: "node",
  outfile: tmp,
  logLevel: "warning",
});
const {PLAN_ROWS, SRC, makeTimeline, FPS} = await import(pathToFileURL(tmp).href + `?t=${Date.now()}`);
const tl = makeTimeline(SRC, FPS);
const subText = new Map(tl.subs.map((s) => [s.n, s.lines.join(" ")]));
const tc = (fr) => {
  const s = fr / FPS;
  return `${Math.floor(s / 60)}:${(s % 60).toFixed(1).padStart(4, "0")}`;
};
const rows = PLAN_ROWS.map((r, i) => ({
  ...r,
  from: tl.s(r.subs[0]),
  to: i === PLAN_ROWS.length - 1 ? tl.total : tl.e(r.subs[1]),
}));
log("PLAN", {episode: id, scenes: rows.length, subtitles: tl.subs.length, cards: tl.cards.length, frames: tl.total, length: tc(tl.total)});

// ── 2. scene_plan.md ──
const bgKo = {cream: "크림", navy: "네이비", light: "밝은 크림"};
const esc = (s) => String(s).replace(/\|/g, "\\|");
const subRange = (r) => (r.subs[0] === r.subs[1] ? `${r.subs[0]}` : `${r.subs[0]}–${r.subs[1]}`);
let md = `# ${id} 장면 구성표\n\n`;
md += `자동 생성 — \`video/scripts/storyboard.mjs\` (원본 데이터: \`video/src/episodes/${id}/plan.ts\`, 숫자: \`facts.ts\`). 형식: \`guides/video_guide.md\` 5-2\n\n`;
md += `- 장면 ${rows.length}개, 자막 ${tl.subs.length}개, 고지 카드 ${tl.cards.length}개, 전체 ${tc(tl.total)} (${tl.total}프레임, ${FPS}fps)\n`;
for (const c of tl.cards) md += `- 고지 카드 "${c.title}": 자막 ${c.afterSub} 뒤 ${tc(c.from)}–${tc(c.to)} (${((c.to - c.from) / FPS).toFixed(1)}초)\n`;
md += `- 사연 파트(자막 1–14) 동안 왼쪽 위에 "실제 주가 흐름을 바탕으로 재구성한 사연" 캡션 (1-11)\n`;
md += `- 전환: 배경이 바뀌는 곳과 새 항목 시작은 찢어진 종이 와이프(W), 나머지는 컷\n\n`;
md += `| 장면 | 자막 | 시간 | 배경 | 연출 (자막 번호별) | 화면 텍스트 | 패턴 | 연결 근거 |\n|---|---|---|---|---|---|---|---|\n`;
for (const r of rows) {
  md += `| ${r.id}${r.wipe ? " (W)" : ""} | ${subRange(r)} | ${tc(r.from)}–${tc(r.to)} | ${bgKo[r.bg]} | ${esc(r.does)} | ${esc(r.text)} | ${esc(r.pattern)} | ${esc(r.why)} |\n`;
  const card = tl.cards.find((c) => c.afterSub === r.subs[1]);
  if (card) md += `| 카드 | — | ${tc(card.from)}–${tc(card.to)} | 크림 | 노랑 띠 + 문구 ${card.lines.length}줄이 차례로 | ${esc(card.title)} / ${esc(card.lines.join(" / "))} | 화면 고지 카드 | TXT [장면] 문구 그대로 |\n`;
}
fs.writeFileSync(path.join(outDir, "scene_plan.md"), md);
log("PLAN", {wrote: path.join(outDir, "scene_plan.md")});

// ── 3. still 목록 ──
const shots = [];
for (const r of rows) {
  for (const n of r.shots ?? []) shots.push({scene: r.id, file: `${r.id}-${n}.jpg`, frame: tl.e(n) - 10, subs: [n, n], r});
  shots.push({scene: r.id, file: `${r.id}.jpg`, frame: tl.e(r.subs[1]) - 10, subs: r.subs, r});
  const card = tl.cards.find((c) => c.afterSub === r.subs[1]);
  if (card) shots.push({scene: "카드", file: "card.jpg", frame: card.to - 30, subs: null, r: null, card});
}
const todo = only ? shots.filter((s) => only.has(s.scene)) : shots;

// ── 4. 렌더 ──
const t0 = Date.now();
const browserExecutable = process.env.REMOTION_BROWSER || null;
log("RENDER", {stage: "bundle", entry: "src/index.ts"});
const serveUrl = await bundle({entryPoint: path.join(root, "src", "index.ts"), publicDir: path.join(root, "public")});
const browser = await openBrowser("chrome", {browserExecutable});
const composition = await selectComposition({serveUrl, id, puppeteerInstance: browser, browserExecutable});
for (const s of todo) {
  await renderStill({composition, serveUrl, frame: s.frame, output: path.join(sbDir, s.file), imageFormat: "jpeg", jpegQuality: 82, scale, puppeteerInstance: browser, browserExecutable, overwrite: true});
  log("RENDER", {still: s.file, frame: s.frame, time: tc(s.frame)});
}
await browser.close({silent: true});
log("RENDER", {stills: todo.length, seconds: ((Date.now() - t0) / 1000).toFixed(1)});

// ── 5. index.html ──
const h = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
const cards = shots
  .map((s) => {
    if (s.card) {
      return `<article><img src="${s.file}" loading="lazy"><div class="meta"><b>고지 카드</b> <span>자막 ${s.card.afterSub} 뒤 · ${tc(s.card.from)}–${tc(s.card.to)}</span></div><p class="sub">${h(s.card.title)} — ${h(s.card.lines.join(" / "))}</p></article>`;
    }
    const subs = [];
    for (let n = s.subs[0]; n <= s.subs[1]; n++) subs.push(`<li><b>${n}</b> ${h(subText.get(n))}</li>`);
    return `<article><img src="${s.file}" loading="lazy"><div class="meta"><b>${s.file.replace(".jpg", "")}</b> <span>자막 ${subRange({subs: s.subs})} · ${tc(s.frame)} · ${bgKo[s.r.bg]}${s.r.wipe ? " · 와이프" : ""}</span></div><ul>${subs.join("")}</ul><p class="why"><b>연출</b> ${h(s.r.does)}</p><p class="why"><b>연결 근거</b> ${h(s.r.why)}</p></article>`;
  })
  .join("\n");
const html = `<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${id} 스토리보드</title>
<style>body{margin:0;background:#F2EBDD;color:#1E1E1E;font-family:"Noto Sans KR",system-ui,sans-serif}header{padding:24px 16px;max-width:1400px;margin:0 auto}h1{font-size:28px;margin:0 0 8px}main{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,560px),1fr));gap:20px;padding:0 16px 40px;max-width:1400px;margin:0 auto}article{background:#FAF6EE;border:2px solid #1E1E1E;border-radius:12px;overflow:hidden}img{width:100%;display:block;border-bottom:2px solid #1E1E1E}.meta{padding:10px 14px;display:flex;gap:10px;align-items:baseline;flex-wrap:wrap}.meta span{color:#6b675f;font-size:14px}ul{margin:0;padding:0 14px 6px 32px;font-size:14px;line-height:1.5}.why{margin:6px 14px 10px;font-size:13px;line-height:1.5;color:#3b3833}p.sub{margin:0 14px 12px;font-size:14px}</style></head>
<body><header><h1>${id} 스토리보드</h1><div>장면 ${rows.length}개 · 자막 ${tl.subs.length}개 · 고지 카드 ${tl.cards.length}개 · 전체 ${tc(tl.total)} · still은 각 장면 마지막 자막 끝 10프레임 전 (추가 컷은 장면-자막번호)</div><div>장면 구성표: <code>scene_plan.md</code> · 투자 교육용 영상이며 특정 종목의 매수·매도 권유가 아닙니다.</div></header>
<main>
${cards}
</main></body></html>`;
fs.writeFileSync(path.join(sbDir, "index.html"), html);
log("DONE", {index: path.join(sbDir, "index.html"), stills: shots.length});
