// VERSION: v1.0 — 2026-10-27 — 배치 점검: 장면 파일의 '배치 표'(window.LAYOUT = {칸 이름: [x, y, w, h]})대로 물건이 놓였는지
//   사용자 지시 2026-10-27 "영상에서 모든 오브젝트별로 배치 위치를 딱 정해서 자꾸 뭔가 어긋나잖아".
//   대표 장면(K.cut)마다(+ --every 초마다) 무대를 그 시각으로 돌려 놓고:
//     ① 칸 없음 — 장면(.sc) 바로 아래 보이는 물건에 data-slot 이 없음 (배치 표 밖에서 자리를 정한 물건)
//     ② 배치 표에 없는 칸 — data-slot 이름이 window.LAYOUT 에 없음
//     ③ 칸 밖 — 물건(글자·그림·카드)의 화면 상자가 자기 칸 상자를 벗어남 (DOM ±tol px · 인형 ±ptol px)
//     ④ 겹침 — 서로 다른 칸의 물건이 겹침 (window.LAYOUT_ALLOW 의 [칸, 칸] 짝은 일부러 겹치는 것 · 인형끼리는 앞뒤 겹이라 뺌)
//     ⑤ 인형 칸 없음 — 종이 인형(puppet.js v1.3 S.boxes)에 slot 이 없음
//   보이는 것만 (불투명도 0.3 이상). 문제가 있으면 끝 코드 1.
//   사용법: node video/scripts/layout-check.mjs <영상ID> [--tol 4] [--ptol 14] [--every 0] [--min-op 0.3] [--min-area 150] [--shots <폴더>]
//   --every N 으로 장면 사이도 볼 때는 --min-op 0.9 (장면이 바뀌며 겹쳐 사라지는 0.35초는 빼고 — 다 보이는 물건만).
//   --shots: 문제가 난 시각의 화면을 칸 상자(초록)·문제 상자(빨강)와 함께 저장. 연구·교육용 영상 도구.
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
if (!ID) { console.error("사용법: node video/scripts/layout-check.mjs <영상ID> [--tol 4] [--ptol 14] [--every 0] [--min-area 150] [--shots <폴더>]"); process.exit(2); }
const PAGE = path.join(ROOT, "video", "episodes", ID, "index.html");
if (!fs.existsSync(PAGE)) { log("FAIL", { stage: "input", page: path.relative(ROOT, PAGE), next: "영상ID 확인" }); process.exit(2); }
const HTML = fs.readFileSync(PAGE, "utf-8");
const [W0, H0] = (m => (m ? [+m[1], +m[2]] : [1920, 1080]))(HTML.match(/<meta name="video-size" content="(\d+)x(\d+)"/));
const TOL = +opt("tol", 4), PTOL = +opt("ptol", 14), EVERY = +opt("every", 0), MIN_AREA = +opt("min-area", 150), MIN_OP = +opt("min-op", 0.3), SHOTS = opt("shots", null);

async function loadPw() {
  try { return (await import("playwright")).default; } catch { /* 전역 설치본 */ }
  const req = createRequire(import.meta.url);
  return req(path.join(execSync("npm root -g", { encoding: "utf-8" }).trim(), "playwright"));
}

const COLLECT = ([TOL, PTOL, MIN_AREA, MIN_OP]) => {
  const LAY = window.LAYOUT || {}, ALLOW = new Set((window.LAYOUT_ALLOW || []).map(p => p.slice().sort().join("|")));
  const st = document.getElementById("stage"), S0 = st.getBoundingClientRect();
  const op = el => { let o = 1; for (let e = el; e && e !== st; e = e.parentElement) { const cs = getComputedStyle(e); o *= +cs.opacity; if (cs.display === "none" || cs.visibility === "hidden") return 0; } return o; };
  const R = el => { const b = el.getBoundingClientRect(); return [b.left - S0.left, b.top - S0.top, b.right - S0.left, b.bottom - S0.top].map(v => Math.round(v)); };
  const items = [], probs = [];
  st.querySelectorAll("[data-slot]").forEach(el => {
    if (op(el) < MIN_OP) return;
    const r = R(el); if (r[2] - r[0] < 1 || r[3] - r[1] < 1) return;
    items.push({ kind: "dom", el, slot: el.dataset.slot, rect: r, label: `${el.dataset.slot}:${(el.textContent || "").trim().replace(/\s+/g, " ").slice(0, 14) || el.tagName}` });
  });
  st.querySelectorAll(".sc").forEach(sc => {
    if (op(sc) < MIN_OP) return;
    for (const n of sc.children) {
      if (n.dataset.slot || op(n) < MIN_OP) continue;
      const r = R(n); if (r[2] - r[0] < 2 || r[3] - r[1] < 2) continue;
      probs.push({ kind: "칸 없음", what: `${n.className && n.className.baseVal != null ? n.className.baseVal : n.className || n.tagName}:${(n.textContent || "").trim().slice(0, 14)}`, rect: r });
    }
  });
  for (const S of (window.Puppet && window.Puppet.stages) || []) {
    if (!S.boxes) continue;
    for (const b of S.boxes(MIN_OP)) {
      if (!b.slot) probs.push({ kind: "인형 칸 없음", what: b.key, rect: b.rect });
      items.push({ kind: "puppet", el: null, slot: b.slot, rect: b.rect, label: `${b.slot || "?"}:${b.key}` });
    }
  }
  for (const it of items) {
    if (!it.slot) continue;
    const box = LAY[it.slot];
    if (!box) { probs.push({ kind: "배치 표에 없는 칸", what: it.label, rect: it.rect }); continue; }
    const [x, y, w, h] = box, t = it.kind === "puppet" ? PTOL : TOL, r = it.rect;
    if (r[0] < x - t || r[1] < y - t || r[2] > x + w + t || r[3] > y + h + t) probs.push({ kind: "칸 밖", what: it.label, rect: r, box: [x, y, x + w, y + h] });
  }
  for (let i = 0; i < items.length; i++) for (let j = i + 1; j < items.length; j++) {
    const a = items[i], b = items[j];
    if (a.kind === "puppet" && b.kind === "puppet") continue;
    if (a.slot && a.slot === b.slot) continue;
    if (a.el && b.el && (a.el.contains(b.el) || b.el.contains(a.el))) continue;
    if (ALLOW.has([a.slot, b.slot].sort().join("|"))) continue;
    const ix = Math.min(a.rect[2], b.rect[2]) - Math.max(a.rect[0], b.rect[0]), iy = Math.min(a.rect[3], b.rect[3]) - Math.max(a.rect[1], b.rect[1]);
    if (ix <= 0 || iy <= 0) continue;
    const area = ix * iy, small = Math.min((a.rect[2] - a.rect[0]) * (a.rect[3] - a.rect[1]), (b.rect[2] - b.rect[0]) * (b.rect[3] - b.rect[1]));
    if (area > Math.max(MIN_AREA, 0.01 * small)) probs.push({ kind: "겹침", what: `${a.label} × ${b.label}`, rect: [Math.max(a.rect[0], b.rect[0]), Math.max(a.rect[1], b.rect[1]), Math.min(a.rect[2], b.rect[2]), Math.min(a.rect[3], b.rect[3])] });
  }
  return { probs, slots: items.map(i => ({ slot: i.slot, rect: i.rect })), n: items.length };
};

const pw = await loadPw();
let browser;
try { browser = await pw.chromium.launch({ args: ["--allow-file-access-from-files"] }); }
catch { browser = await pw.chromium.launch({ args: ["--allow-file-access-from-files"], executablePath: "/opt/pw-browsers/chromium" }); }
const page = await browser.newPage({ viewport: { width: W0, height: H0 }, deviceScaleFactor: 1 });
const NM = path.join(ROOT, "video", "render", "node_modules");
await page.route(/^https?:\/\//, r => {
  const u = r.request().url();
  if (/cdnjs\.cloudflare\.com\/ajax\/libs\/gsap\//.test(u)) return r.fulfill({ path: path.join(NM, "gsap", "dist", "gsap.min.js"), contentType: "application/javascript" });
  if (/three@0\.160\.0\/build\/three\.min\.js/.test(u)) return r.fulfill({ path: path.join(NM, "three", "build", "three.min.js"), contentType: "application/javascript" });
  return r.abort();
});
const errs = [];
page.on("pageerror", e => errs.push(e.message));
await page.goto("file://" + PAGE + "?render=1");
const ok = await page.waitForFunction(() => window.SB && window.SB.ready, null, { timeout: 30000 }).then(() => true, () => false);
if (!ok) { log("FAIL", { stage: "load", errors: JSON.stringify(errs.slice(0, 3)), next: "render.mjs check 로 장면 파일 오류 먼저" }); await browser.close(); process.exit(2); }
await page.evaluate(async () => { await document.fonts.ready; });
const info = await page.evaluate(() => ({ cuts: window.SB.cuts, D: window.SB.D, lay: Object.keys(window.LAYOUT || {}).length }));
log("START", { tool: "layout-check.mjs v1.0", video: ID, size: `${W0}x${H0}`, slots: info.lay, cuts: info.cuts.length, every: EVERY, tol: TOL, ptol: PTOL, min_op: MIN_OP, note: "연구·교육용 영상 도구" });
if (!info.lay) log("WARN", { stage: "layout", msg: "window.LAYOUT 없음 — 모든 물건이 '칸 없음'으로 나옴", next: "장면 파일에 배치 표를 둠" });
const times = info.cuts.map(c => ({ t: c.t, name: c.name }));
if (EVERY > 0) for (let t = EVERY; t < info.D; t += EVERY) times.push({ t: +t.toFixed(2), name: `${EVERY}초마다` });
times.sort((a, b) => a.t - b.t);
const all = [];
if (SHOTS) fs.mkdirSync(SHOTS, { recursive: true });
for (const c of times) {
  await page.evaluate(t => window.SB.seek(t), c.t);
  const res = await page.evaluate(COLLECT, [TOL, PTOL, MIN_AREA, MIN_OP]);
  for (const p of res.probs) { all.push({ ...p, t: c.t, cut: c.name }); log("LAYOUT", { t: c.t, cut: c.name, kind: p.kind, what: p.what, rect: (p.rect || []).join(","), box: (p.box || []).join(",") }); }
  if (SHOTS && res.probs.length) {
    await page.evaluate(([probs, slots]) => {
      const st = document.getElementById("stage"), d = document.createElement("div"); d.id = "__lay"; d.style.cssText = "position:absolute;inset:0;pointer-events:none;z-index:99999";
      const bx = (r, c, w) => { const e = document.createElement("div"); e.style.cssText = `position:absolute;left:${r[0]}px;top:${r[1]}px;width:${r[2] - r[0]}px;height:${r[3] - r[1]}px;border:${w}px solid ${c}`; d.appendChild(e); };
      for (const s of slots) if (s.slot && window.LAYOUT[s.slot]) { const [x, y, w, h] = window.LAYOUT[s.slot]; bx([x, y, x + w, y + h], "rgba(0,255,120,.8)", 2); }
      for (const p of probs) if (p.rect) bx(p.rect, "rgba(255,30,30,.95)", 4);
      st.appendChild(d);
    }, [res.probs, res.slots]);
    await page.screenshot({ path: path.join(SHOTS, `${String(c.t.toFixed(1)).padStart(6, "0")}s.png`) });
    await page.evaluate(() => document.getElementById("__lay").remove());
  }
}
await browser.close();
const byKind = {};
for (const p of all) byKind[p.kind] = (byKind[p.kind] || 0) + 1;
log("DONE", { video: ID, samples: times.length, problems: all.length, by_kind: JSON.stringify(byKind), page_errors: errs.length, next: all.length ? "장면 파일의 배치 표·data-slot 을 고친 뒤 다시" : "배치 표대로 놓임" });
process.exit(all.length || errs.length ? 1 : 0);
