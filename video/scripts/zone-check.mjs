// VERSION: v1.0 — 2026-11-11 — 영역 점검: 장면 파일의 '영역 표'(window.ZONES = {배경: {영역 이름: {poly: [[x,y]…], h: [최소, 최대]}}})대로
//   인물·모션그래픽이 배경의 맞는 자리에 있는지 본다 (layout-check.mjs 의 칸 점검과 따로 — 칸은 화면 상자, 영역은 배경 그림 속 자리).
//   사용자 지시 2026-11-11 "영상 만들 때 캐릭터가 엉뚱한 곳에 있거나 모션 그래픽 요소가 배경이나 이미지들 어울리지 않는 위치에 있거나
//   어긋나는게 꽤 있는데 그런거 영역을 확실하게 정해서 꼼꼼히 확인해".
//   장면 파일 약속 (manspi-jeonmang-2026-11 v3.0 부터):
//     · 장면마다 .world[data-bg="배경"] — 카메라(transform)는 세계에 · 흔들림은 .sc 에
//     · 인물 상자 .act[data-zone="영역"][data-h="화면 키(px, 세계 좌표)"][data-free="a-b,c-d"] — 안에 .ft(발 기준점 1px) · .hd(원화마다 머리 상자) · .bd(원화마다 몸 상자)
//     · 물건 [data-zone="영역"] (data-anchor="bottom" 이면 밑변 가운데 점만 영역 안에 — 장식장·책상 위 소품) · data-owner="인물 id"(그 인물 얼굴은 가려도 됨 — 손에 든 것)
//     · 세계의 층 .lay[data-l="back|act|front|fly|top|light"] — back 층 물건이 인물 몸·머리에 가리면 '가려짐', fly·top 층 물건이 머리를 덮으면 '얼굴 가림'
//   보는 것 (보이는 것만 — 불투명도 --min-op 이상, 그 장면이 다 나타난 때):
//     ① 발 밖 — 인물 발 기준점이 자기 영역 다각형 밖 (data-free 시각 안은 뺌 — 걸어 들어옴·나감)
//     ② 키 — 인물 data-h 가 영역의 h 범위 밖 (원근: 같은 바닥에서 키가 다르면 엉뚱해 보임)
//     ③ 영역 밖 — 물건 상자(또는 밑변 점)가 자기 영역 밖 (± --tol px)
//     ④ 얼굴 가림 — fly·top 층 물건이 보이는 머리 상자의 --face 비율 넘게 덮음 (data-owner 가 그 인물이면 뺌)
//     ⑤ 가려짐 — back 층 정보 물건(data-info)이 앞 인물의 머리·몸 상자에 --hide 비율 넘게 가림
//     ⑥ 얼굴 잘림 — 보이는 머리 상자가 화면 밖으로 --cut px 넘게 나감 (data-free 안은 뺌)
//   사용법: node video/scripts/zone-check.mjs <영상ID> [--every 0.5] [--min-op 0.9] [--face-op 0.3] [--tol 8] [--face 0.12] [--hide 0.2] [--cut 12] [--shots <폴더>]
//   (--face-op: 얼굴 가림은 반투명 물건도 봄 — 흐려지며 얼굴에 겹친 목표 숫자처럼)
//   문제가 있으면 끝 코드 1. 연구·교육용 영상 도구.
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
if (!ID) { console.error("사용법: node video/scripts/zone-check.mjs <영상ID> [--every 0.5] [--min-op 0.9] [--tol 8] [--face 0.12] [--hide 0.2] [--cut 12] [--shots <폴더>]"); process.exit(2); }
const PAGE = path.join(ROOT, "video", "episodes", ID, "index.html");
if (!fs.existsSync(PAGE)) { log("FAIL", { stage: "input", page: path.relative(ROOT, PAGE), next: "영상ID 확인" }); process.exit(2); }
const FACE_OP = +opt("face-op", 0.3), EVERY = +opt("every", 0.5), MIN_OP = +opt("min-op", 0.9), TOL = +opt("tol", 8), FACE = +opt("face", 0.12), HIDE = +opt("hide", 0.2), CUT = +opt("cut", 12), SHOTS = opt("shots", null);

async function loadPw() {
  try { return (await import("playwright")).default; } catch { /* 전역 설치본 */ }
  const req = createRequire(import.meta.url);
  return req(path.join(execSync("npm root -g", { encoding: "utf-8" }).trim(), "playwright"));
}

// 브라우저 안에서: 시각 t 의 문제 목록
const COLLECT = ([MIN_OP, TOL, FACE, HIDE, CUT, FACE_OP]) => {
  const st = document.getElementById("stage"), S0 = st.getBoundingClientRect(), t = window.SB.t;
  const Z = window.ZONES || {};
  const op = el => { let o = 1; for (let e = el; e && e !== st; e = e.parentElement) { const cs = getComputedStyle(e); o *= +cs.opacity; if (cs.display === "none" || cs.visibility === "hidden") return 0; } return o; };
  const R = el => { const b = el.getBoundingClientRect(); return [b.left - S0.left, b.top - S0.top, b.right - S0.left, b.bottom - S0.top]; };
  const area = r => Math.max(0, r[2] - r[0]) * Math.max(0, r[3] - r[1]);
  const inter = (a, b) => area([Math.max(a[0], b[0]), Math.max(a[1], b[1]), Math.min(a[2], b[2]), Math.min(a[3], b[3])]);
  const free = el => (el.dataset.free || "").split(",").filter(Boolean).some(s => { const [a, b] = s.split("-").map(Number); return t >= a && t < b; });
  const inPoly = (p, poly) => { let c = false; for (let i = 0, j = poly.length - 1; i < poly.length; j = i++) { const [xi, yi] = poly[i], [xj, yj] = poly[j]; if ((yi > p[1]) !== (yj > p[1]) && p[0] < (xj - xi) * (p[1] - yi) / (yj - yi) + xi) c = !c; } return c; };
  const distOut = (p, poly) => {       // 다각형 밖이면 가장 가까운 변까지 거리 (안이면 0)
    if (inPoly(p, poly)) return 0;
    let d = 1e9;
    for (let i = 0, j = poly.length - 1; i < poly.length; j = i++) {
      const [x1, y1] = poly[j], [x2, y2] = poly[i], dx = x2 - x1, dy = y2 - y1, L = dx * dx + dy * dy || 1;
      const u = Math.max(0, Math.min(1, ((p[0] - x1) * dx + (p[1] - y1) * dy) / L));
      d = Math.min(d, Math.hypot(p[0] - (x1 + u * dx), p[1] - (y1 + u * dy)));
    }
    return d;
  };
  const probs = [];
  const worlds = [...st.querySelectorAll(".world[data-bg]")].filter(w => op(w) >= MIN_OP);
  for (const w of worlds) {
    const bg = w.dataset.bg, zones = Z[bg] || {};
    // 세계 좌표 → 화면 좌표 (세계 transform · 장면 흔들림 · 무대 위치)
    const mW = new DOMMatrix(getComputedStyle(w).transform === "none" ? undefined : getComputedStyle(w).transform);
    const sc = w.closest(".sc"), mS = new DOMMatrix(getComputedStyle(sc).transform === "none" ? undefined : getComputedStyle(sc).transform);
    const toScr = ([x, y]) => { const p = mS.transformPoint(mW.transformPoint(new DOMPoint(x, y))); return [p.x, p.y]; };
    const zpoly = name => zones[name] && zones[name].poly.map(toScr);
    const heads = [], bodies = [];
    // 인물
    for (const a of w.querySelectorAll(".act[data-zone]")) {
      if (op(a) < MIN_OP) continue;
      const zn = a.dataset.zone, z = zones[zn], id = a.dataset.id || "?";
      if (!z) { probs.push({ kind: "영역 표에 없음", what: `${bg}:${zn} (${id})` }); continue; }
      const h = +a.dataset.h;
      if (z.h && (h < z.h[0] || h > z.h[1])) probs.push({ kind: "키", what: `${id} 키 ${Math.round(h)}px — ${bg}:${zn} 는 ${z.h[0]}~${z.h[1]}` });
      const ft = a.querySelector(".ft");
      if (ft && !free(a)) {
        const r = R(ft), p = [(r[0] + r[2]) / 2, (r[1] + r[3]) / 2], d = distOut(p, zpoly(zn));
        if (d > TOL) probs.push({ kind: "발 밖", what: `${id} 발 (${Math.round(p[0])},${Math.round(p[1])}) — ${bg}:${zn} 밖 ${Math.round(d)}px`, rect: [p[0] - 10, p[1] - 10, p[0] + 10, p[1] + 10] });
      }
      for (const hd of a.querySelectorAll(".hd")) if (op(hd) >= 0.5) {
        const r = R(hd); heads.push({ id, r, el: a });
        if (!free(a) && (r[0] < -CUT || r[1] < -CUT || r[2] > 1920 + CUT || r[3] > 1080 + CUT)) probs.push({ kind: "얼굴 잘림", what: `${id} 머리 ${r.map(Math.round).join(",")}`, rect: r });
      }
      for (const bd of a.querySelectorAll(".bd")) if (op(bd) >= 0.5) bodies.push({ id, r: R(bd), el: a });
    }
    // 물건
    for (const el of w.querySelectorAll("[data-zone]:not(.act)")) {
      const o = op(el);
      if (o < FACE_OP) continue;
      const zn = el.dataset.zone, poly = zpoly(zn), r = R(el);
      if (r[2] - r[0] < 2 || r[3] - r[1] < 2) continue;
      const label = `${zn}:${(el.textContent || "").trim().replace(/\s+/g, " ").slice(0, 14) || (el.getAttribute("src") || el.className || el.tagName).toString().split("/").pop()}`;
      if (!poly) { probs.push({ kind: "영역 표에 없음", what: `${bg}:${label}` }); continue; }
      if (o < MIN_OP) { /* 반투명: 영역 점검은 빼고 얼굴 가림만 */ }
      else if (el.dataset.anchor === "bottom") {
        const p = [(r[0] + r[2]) / 2, r[3]], d = distOut(p, poly);
        if (d > TOL) probs.push({ kind: "영역 밖", what: `${label} 밑변 (${Math.round(p[0])},${Math.round(p[1])}) 밖 ${Math.round(d)}px`, rect: r });
      } else {
        const out = [[r[0], r[1]], [r[2], r[1]], [r[2], r[3]], [r[0], r[3]]].map(p => distOut(p, poly)).reduce((m, v) => Math.max(m, v), 0);
        if (out > TOL) probs.push({ kind: "영역 밖", what: `${label} — ${bg}:${zn} 밖 ${Math.round(out)}px`, rect: r });
      }
      const lay = (el.closest("[data-l]") || {}).dataset || {};
      const own = el.dataset.owner || (el.closest("[data-owner]") || { dataset: {} }).dataset.owner;
      if (lay.l === "fly" || lay.l === "top") {
        for (const h of heads) {
          if (own && (own === "*" || own === h.id)) continue;
          const f = inter(r, h.r) / (area(h.r) || 1);
          if (f > FACE) probs.push({ kind: "얼굴 가림", what: `${label} × ${h.id} 머리 ${Math.round(f * 100)}%`, rect: r });
        }
      }
      if (lay.l === "back" && el.dataset.info && o >= MIN_OP) {
        for (const h of [...heads, ...bodies]) {
          const f = inter(r, h.r) / (area(r) || 1);
          if (f > HIDE) probs.push({ kind: "가려짐", what: `${label} — ${h.id} 뒤에 ${Math.round(f * 100)}%`, rect: r });
        }
      }
    }
  }
  return { probs, worlds: worlds.length };
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
const info = await page.evaluate(() => ({ D: window.SB.D, cuts: window.SB.cuts, zones: Object.keys(window.ZONES || {}).length }));
log("START", { tool: "zone-check.mjs v1.0", video: ID, zones_bg: info.zones, every: EVERY, min_op: MIN_OP, tol: TOL, face: FACE, hide: HIDE, note: "연구·교육용 영상 도구" });
if (!info.zones) log("WARN", { stage: "zones", msg: "window.ZONES 없음", next: "장면 파일에 영역 표를 둠" });
const times = info.cuts.map(c => ({ t: c.t, name: c.name }));
for (let t = EVERY; t < info.D; t += EVERY) times.push({ t: +t.toFixed(2), name: `${EVERY}초마다` });
times.sort((a, b) => a.t - b.t);
if (SHOTS) fs.mkdirSync(SHOTS, { recursive: true });
const all = [], seen = new Map();
for (const c of times) {
  await page.evaluate(t => window.SB.seek(t), c.t);
  const res = await page.evaluate(COLLECT, [MIN_OP, TOL, FACE, HIDE, CUT, FACE_OP]);
  for (const p of res.probs) {
    all.push({ ...p, t: c.t });
    const key = `${p.kind}|${p.what.replace(/\(\d+,\d+\)|\d+px|\d+%/g, "#")}`;
    if (!seen.has(key)) { seen.set(key, { ...p, t0: c.t, t1: c.t, n: 1 }); } else { const s = seen.get(key); s.t1 = c.t; s.n++; }
  }
  if (SHOTS && res.probs.length) {
    await page.evaluate(probs => {
      const st = document.getElementById("stage"), d = document.createElement("div"); d.id = "__z"; d.style.cssText = "position:absolute;inset:0;pointer-events:none;z-index:99999";
      for (const p of probs) if (p.rect) { const e = document.createElement("div"); const r = p.rect; e.style.cssText = `position:absolute;left:${r[0]}px;top:${r[1]}px;width:${r[2] - r[0]}px;height:${r[3] - r[1]}px;border:4px solid rgba(255,30,30,.95)`; d.appendChild(e); }
      st.appendChild(d);
    }, res.probs);
    await page.screenshot({ path: path.join(SHOTS, `${String(c.t.toFixed(1)).padStart(6, "0")}s.png`) });
    await page.evaluate(() => document.getElementById("__z").remove());
  }
}
await browser.close();
for (const s of seen.values()) log("ZONE", { t: `${s.t0}~${s.t1}`, samples: s.n, kind: s.kind, what: s.what });
const byKind = {};
for (const p of seen.values()) byKind[p.kind] = (byKind[p.kind] || 0) + 1;
log("DONE", { video: ID, samples: times.length, problems: seen.size, by_kind: JSON.stringify(byKind), page_errors: errs.length, next: seen.size ? "장면 파일의 SPOT·영역 표·물건 자리를 고친 뒤 다시" : "모두 제 영역 안" });
process.exit(seen.size || errs.length ? 1 : 0);
