// VERSION: v1.0 — 2026-11-24 — 말풍선·이름표·도장·카드·소품 점검: 잘림 · 화면/자막 띠 밖 · 서로 겹침
//   사용자 지시 2026-11-24 "말풍선이 중간선에 잘리는데 안잘리도록 해 … 말풍선 좀 겹치게, 잘리게 하지말고 좀 보이게 하라고".
//   layout-check.mjs 는 장면(.sc) 바로 아래 칸만 보고 세계(world) 안의 말풍선은 보지 않음 → 이 도구가 따로 본다.
//   --every 초마다(기본 0.2) 무대를 그 시각으로 돌려 놓고, 보이는(누적 불투명도 ≥ --min-op, 기본 0.6) 물건마다:
//     ① 잘림 — 반반 화면(장면 .sc 의 data-vis="x0,x1")에서 보이는 반쪽 밖으로 나감
//     ② 화면 밖 — 화면 가장자리 6px 안쪽을 벗어남
//     ③ 자막 띠 — 자막(#cc)이 보일 때 그 상자와 겹침
//     ④ 겹침 — 말풍선·이름표·도장·카드·소품끼리 겹침 (부모·자식 사이는 뺌)
//   같은 문제가 이어지는 시각은 한 줄로 묶어 보고. 문제가 있으면 끝 코드 1. 연구·교육용 영상 도구.
//   사용법: node video/scripts/bubble-check.mjs <영상ID> [--every 0.2] [--min-op 0.6] [--from 0 --to 9999] [--shots <폴더>]
import fs from "node:fs";
import path from "node:path";
import { execSync } from "node:child_process";
import { createRequire } from "node:module";
import { fileURLToPath } from "node:url";

const HERE = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(HERE, "..", "..");
const argv = process.argv.slice(2);
const opt = (k, d) => { const i = argv.indexOf(`--${k}`); return i >= 0 ? argv[i + 1] : d; };
const ID = argv.find((a, i) => !a.startsWith("--") && !(i > 0 && argv[i - 1].startsWith("--")));
const ts = () => new Date().toISOString().replace(/\.\d+Z$/, "Z");
const log = (stage, kv) => console.log(`[${stage}] [${ts()}] ` + Object.entries(kv).map(([k, v]) => `${k}=${typeof v === "string" && /\s/.test(v) ? JSON.stringify(v) : v}`).join(" "));
if (!ID) { console.error("사용법: node video/scripts/bubble-check.mjs <영상ID> [--every 0.2] [--min-op 0.6] [--from 0 --to 9999] [--shots <폴더>]"); process.exit(2); }
const PAGE = path.join(ROOT, "video", "episodes", ID, "index.html");
if (!fs.existsSync(PAGE)) { log("FAIL", { stage: "input", page: path.relative(ROOT, PAGE), next: "영상ID 확인" }); process.exit(2); }
const EVERY = +opt("every", 0.2), MIN_OP = +opt("min-op", 0.6), FROM = +opt("from", 0), TO = +opt("to", 99999), SHOTS = opt("shots", null);

async function loadPw() {
  try { return (await import("playwright")).default; } catch { /* 전역 설치본 */ }
  const req = createRequire(import.meta.url);
  return req(path.join(execSync("npm root -g", { encoding: "utf-8" }).trim(), "playwright"));
}

const COLLECT = (MIN_OP) => {
  const st = document.getElementById("stage"), S0 = st.getBoundingClientRect();
  const op = el => { let o = 1; for (let e = el; e && e !== st; e = e.parentElement) { const cs = getComputedStyle(e); o *= +cs.opacity; if (cs.display === "none" || cs.visibility === "hidden") return 0; } return o; };
  const R = el => { const b = el.getBoundingClientRect(); return [b.left - S0.left, b.top - S0.top, b.right - S0.left, b.bottom - S0.top].map(v => Math.round(v)); };
  const name = el => `${el.classList.contains("pbub") ? "말풍선" : el.classList.contains("tag") ? "이름표" : el.classList.contains("stamp") ? "도장" : el.classList.contains("ccard") ? "카드" : "소품"}:${(el.textContent || el.getAttribute("src") || "").trim().replace(/\s+/g, " ").replace(/^.*\//, "").slice(0, 16)}`;
  const items = [];
  st.querySelectorAll(".pbub,.tag,.stamp,.ccard,img.spr").forEach(el => {
    if (op(el) < MIN_OP) return;
    const r = R(el); if (r[2] - r[0] < 4 || r[3] - r[1] < 4) return;
    const sc = el.closest("[data-vis]");
    items.push({ el, r, what: name(el), vis: sc ? sc.dataset.vis.split(",").map(Number) : null });
  });
  const probs = [];
  const cc = document.getElementById("cc");
  const ccR = cc && cc.textContent.trim() && op(cc) > 0.3 ? R(cc) : null;
  const ov = (a, b) => { const ix = Math.min(a[2], b[2]) - Math.max(a[0], b[0]), iy = Math.min(a[3], b[3]) - Math.max(a[1], b[1]); return ix > 0 && iy > 0 ? ix * iy : 0; };
  for (const it of items) {
    const [x0, y0, x1, y1] = it.r;
    if (it.vis && (x0 < it.vis[0] + 4 || x1 > it.vis[1] - 4)) probs.push({ kind: "잘림(반쪽 밖)", what: it.what, rect: it.r });
    if (x0 < 6 || y0 < 6 || x1 > 1914 || y1 > 1074) probs.push({ kind: "화면 밖", what: it.what, rect: it.r });
    if (ccR && ov(it.r, ccR) > 200) probs.push({ kind: "자막 띠와 겹침", what: it.what, rect: it.r });
  }
  for (let i = 0; i < items.length; i++) for (let j = i + 1; j < items.length; j++) {
    const a = items[i], b = items[j];
    if (a.el.contains(b.el) || b.el.contains(a.el)) continue;
    const area = ov(a.r, b.r);
    if (area > 300) probs.push({ kind: "겹침", what: `${a.what} × ${b.what}`, rect: [Math.max(a.r[0], b.r[0]), Math.max(a.r[1], b.r[1]), Math.min(a.r[2], b.r[2]), Math.min(a.r[3], b.r[3])] });
  }
  return { probs, n: items.length };
};

const pw = await loadPw();
let browser;
try { browser = await pw.chromium.launch({ args: ["--allow-file-access-from-files"] }); }
catch { browser = await pw.chromium.launch({ args: ["--allow-file-access-from-files"], executablePath: "/opt/pw-browsers/chromium" }); }
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
const NM = path.join(ROOT, "video", "render", "node_modules");
await page.route(/^https?:\/\//, r => {
  const u = r.request().url();
  if (/cdnjs\.cloudflare\.com\/ajax\/libs\/gsap\//.test(u)) return r.fulfill({ path: path.join(NM, "gsap", "dist", "gsap.min.js"), contentType: "application/javascript" });
  return r.abort();
});
const errs = [];
page.on("pageerror", e => errs.push(e.message));
await page.goto("file://" + PAGE + "?render=1");
const ok = await page.waitForFunction(() => window.SB && window.SB.ready, null, { timeout: 30000 }).then(() => true, () => false);
if (!ok) { log("FAIL", { stage: "load", errors: JSON.stringify(errs.slice(0, 3)), next: "render.mjs check 로 장면 파일 오류 먼저" }); await browser.close(); process.exit(2); }
await page.evaluate(async () => { await document.fonts.ready; });
const D = await page.evaluate(() => window.SB.D);
log("START", { tool: "bubble-check.mjs v1.0", video: ID, every: EVERY, min_op: MIN_OP, from: FROM, to: Math.min(TO, D), note: "연구·교육용 영상 도구" });
const runs = new Map();          // 같은 문제(종류+대상)가 이어지는 구간을 묶음
const all = [];
if (SHOTS) fs.mkdirSync(SHOTS, { recursive: true });
let samples = 0;
for (let t = Math.max(0, FROM); t <= Math.min(TO, D); t += EVERY) {
  const tt = +t.toFixed(2);
  await page.evaluate(x => window.SB.seek(x), tt);
  const res = await page.evaluate(COLLECT, MIN_OP);
  samples++;
  const seen = new Set();
  for (const p of res.probs) {
    const key = `${p.kind}|${p.what}`;
    seen.add(key);
    const r = runs.get(key);
    if (r && tt - r.to <= EVERY * 1.5) r.to = tt;
    else { const n = { ...p, from: tt, to: tt }; runs.set(key, n); all.push(n); if (SHOTS) await page.screenshot({ path: path.join(SHOTS, `${String(tt.toFixed(1)).padStart(6, "0")}s.png`) }); }
  }
}
await browser.close();
for (const p of all) log("BUBBLE", { from: p.from, to: p.to, kind: p.kind, what: p.what, rect: (p.rect || []).join(",") });
const byKind = {};
for (const p of all) byKind[p.kind] = (byKind[p.kind] || 0) + 1;
log("DONE", { video: ID, samples, problems: all.length, by_kind: JSON.stringify(byKind), page_errors: errs.length, next: all.length ? "say()·stamp()·card() 자리를 고친 뒤 다시" : "잘림·겹침 없음" });
process.exit(all.length || errs.length ? 1 : 0);
