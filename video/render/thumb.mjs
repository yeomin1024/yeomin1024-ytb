// VERSION: v1.1 — 2026-10-25 — 말풍선 꼬리 자리 tailPos(0~1, 말풍선 왼쪽 끝부터 비율)·꼬리 길이 tailLen(px) — 그림 속 인물 머리를 정확히 가리키게
//   (글자 없는 썸네일 그림이 와서 말풍선이 얼굴을 덮지 않게 옮기면서).
// (v1.0) — 2026-10-25 — 썸네일 문구를 코드로 넣기 (사용자 지시 2026-10-25 "그 썸네일은 이제 이미지만 만들고 문구는 너가 만들어서
//   넣는식으로 하자" — 시험 채널 test/ 부터). 그림(ChatGPT, 글자 없음)은 픽셀 그대로 옮기기만 하고(자르기·크기), 글자·꼬리표·말풍선은 이 도구가
//   Noto Sans KR 900 으로 그린다 → 그림 속 한글이 틀리는 일이 없고, 제목·숫자가 바뀌면 글만 고쳐 다시 만든다.
//   설정 = 썸네일 옆 JSON (예: test/source/<영상ID>/shorts/thumbnails/thumbnail_1.json) — 아래 '설정' 참고. 결과 JPEG ≤ 700KB.
//   연구·교육용 영상 도구.
//
//   node video/render/thumb.mjs <설정.json> [<설정.json> …]
//
// 설정 (경로는 설정 파일 기준):
//   { "out": "thumbnail_1.jpg", "size": [1080, 1920], "bg": "#000", "shade": [0.55, 0.8],   // shade: 그 높이 비율부터 아래로 어둡게 (글자 읽히게)
//     "images": [ { "src": "../../images/X.jpg", "crop": [x, y, w, h], "box": [x, y, w, h] } ],     // crop 없으면 그림 전체, box 에 꽉 채움(cover)
//     "blocks": [
//       { "kind": "lines", "box": [x, y, w, h], "align": "center|left", "valign": "center|bottom", "lineHeight": 1.12,
//         "rel": [1, 1.15],            // 줄마다 크기 비율 (없으면 모두 같은 크기)
//         "stroke": 0, "shadow": 0,     // 검정 외곽선 굵기(px, 글자 크기 100 기준) · 그림자
//         "lines": [ [["일본 면세 ", "W"], ["바뀌면", "Y"]], … ] },   // 줄 = [글, 색] 조각들 — 상자 안에서 가장 크게
//       { "kind": "tag", "x": 40, "y": 600, "w": 520, "h": 110, "bg": "R", "color": "W", "text": "모르면 …", "radius": 22, "fill": [0.9, 0.68] },  // 상자 안 가장 크게
//       { "kind": "bubble", "x": …, "y": …, "w": …, "h": …, "bg": "Y", "color": "K", "text": "…", "tail": "left|right", "tailPos": 0.2, "tailLen": 60 } ] }   // tailPos·tailLen 은 없어도 됨
//   색 약자: W 흰 #FFFFFF · Y 노랑 #FFD400 · R 빨강 #FF2A2A · K 검정 #111111 · G 청록 #22C7B0 (그 밖은 CSS 색 그대로)
import fs from "node:fs";
import path from "node:path";
import os from "node:os";
import { fileURLToPath, pathToFileURL } from "node:url";
import { createRequire } from "node:module";
import { execSync } from "node:child_process";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const FONT = path.join(ROOT, "video/public/fonts/NotoSansKR-900.ttf");
const COL = { W: "#FFFFFF", Y: "#FFD400", R: "#FF2A2A", K: "#111111", G: "#22C7B0" };
const col = c => COL[c] || c;
const esc = s => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;");
const log = (stage, o) => console.log(`[${stage}] [${new Date().toISOString()}] ` + Object.entries(o).map(([k, v]) => `${k}=${typeof v === "string" && /\s/.test(v) ? JSON.stringify(v) : v}`).join(" "));
const fail = (stage, msg, hint) => { log(stage, { level: "error", error: msg, hint }); process.exit(1); };

function page(spec, dir) {
  const [W, H] = spec.size;
  const imgs = (spec.images || []).map((im, i) => {
    const src = path.resolve(dir, im.src);
    if (!fs.existsSync(src)) fail("THUMB", `그림 없음 ${path.relative(ROOT, src)}`, "ChatGPT 가 올린 그림 경로 확인 (images_chatgpt.md)");
    const [bx, by, bw, bh] = im.box || [0, 0, W, H];
    return `<div class="im" id="im${i}" data-crop='${JSON.stringify(im.crop || null)}' style="left:${bx}px;top:${by}px;width:${bw}px;height:${bh}px"><img src="${pathToFileURL(src)}"></div>`;
  }).join("");
  const blocks = (spec.blocks || []).map((b, i) => {
    if (b.kind === "lines") {
      const [x, y, w, h] = b.box;
      const lines = b.lines.map((ln, k) => `<div class="ln" data-rel="${(b.rel || [])[k] || 1}">${ln.map(([t, c]) => `<span style="color:${col(c)}">${esc(t)}</span>`).join("")}</div>`).join("");
      return `<div class="lines" id="b${i}" data-kind="lines" data-lh="${b.lineHeight || 1.12}" data-stroke="${b.stroke || 0}" data-shadow="${b.shadow || 0}"
        style="left:${x}px;top:${y}px;width:${w}px;height:${h}px;text-align:${b.align || "center"};justify-content:${b.valign === "bottom" ? "flex-end" : b.valign === "top" ? "flex-start" : "center"}">${lines}</div>`;
    }
    if (b.kind === "tag" || b.kind === "bubble") {
      const pos = b.tailPos == null ? "" : `left:${(b.tailPos * 100).toFixed(1)}%;right:auto;`;                 // v1.1 꼬리 자리
      const len = b.tailLen ? `border-top-width:${b.tailLen}px;bottom:-${b.tailLen - 10}px;` : "";
      const tail = b.kind === "bubble" ? `<i class="tail ${b.tail || "left"}" style="${pos}${len}border-top-color:${col(b.bg)}"></i>` : "";
      return `<div class="${b.kind}" id="b${i}" data-kind="box" data-fill='${JSON.stringify(b.fill || [0.9, 0.68])}' style="left:${b.x}px;top:${b.y}px;width:${b.w}px;height:${b.h}px;background:${col(b.bg)};color:${col(b.color)};border-radius:${b.radius == null ? 22 : b.radius}px">
        <span class="bt">${esc(b.text)}</span>${tail}</div>`;
    }
    fail("THUMB", `모르는 블록 ${b.kind}`, "lines · tag · bubble");
  }).join("");
  const shade = spec.shade ? `<div style="position:absolute;left:0;top:${spec.shade[0] * H}px;width:${W}px;height:${(1 - spec.shade[0]) * H}px;background:linear-gradient(180deg,rgba(0,0,0,0),rgba(0,0,0,${spec.shade[1]}))"></div>` : "";
  return `<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{font-family:"NK";font-weight:900;src:url(${pathToFileURL(FONT)}) format("truetype")}
html,body{margin:0;width:${W}px;height:${H}px;overflow:hidden;background:${spec.bg || "#000"}}
body{position:relative;font-family:"NK",sans-serif;font-weight:900}
.im{position:absolute;overflow:hidden}.im img{position:absolute;display:block}
.lines{position:absolute;display:flex;flex-direction:column}
.ln{white-space:nowrap;letter-spacing:-0.01em}
.lines span{paint-order:stroke fill;-webkit-text-stroke-color:#000;stroke-linejoin:round}
.tag,.bubble{position:absolute;display:grid;place-items:center;box-sizing:border-box}
.bt{white-space:nowrap;line-height:1;letter-spacing:-0.01em}
.tail{position:absolute;bottom:-34px;width:0;height:0;border-left:26px solid transparent;border-right:26px solid transparent;border-top:44px solid}
.tail.left{left:18%;transform:skewX(18deg)}.tail.right{right:18%;transform:skewX(-18deg)}
</style></head><body>${imgs}${shade}${blocks}</body></html>`;
}

// 브라우저 안: 그림 자르기·채우기, 글자 크기를 상자에 맞춰 가장 크게
function layout() {
  const res = [];
  for (const box of document.querySelectorAll(".im")) {
    const img = box.querySelector("img"), crop = JSON.parse(box.dataset.crop || "null");
    const [cx, cy, cw, ch] = crop || [0, 0, img.naturalWidth, img.naturalHeight];
    const bw = box.clientWidth, bh = box.clientHeight, s = Math.max(bw / cw, bh / ch);
    img.style.width = img.naturalWidth * s + "px"; img.style.height = img.naturalHeight * s + "px";
    img.style.left = -(cx * s + (cw * s - bw) / 2) + "px"; img.style.top = -(cy * s + (ch * s - bh) / 2) + "px";
    res.push({ img: img.src.split("/").pop(), scale: +s.toFixed(4) });
  }
  for (const b of document.querySelectorAll('[data-kind="lines"]')) {
    const lns = [...b.querySelectorAll(".ln")], lh = +b.dataset.lh, st = +b.dataset.stroke, sh = +b.dataset.shadow;
    const W = b.clientWidth, H = b.clientHeight;
    const apply = f => lns.forEach(l => { const s = f * +l.dataset.rel; l.style.fontSize = s + "px"; l.style.lineHeight = lh; l.querySelectorAll("span").forEach(sp => { sp.style.webkitTextStrokeWidth = (st * s / 100) + "px"; if (sh) sp.style.textShadow = `0 ${sh * s / 100}px ${2 * sh * s / 100}px rgba(0,0,0,.85)`; }); });
    let lo = 10, hi = 600;
    for (let k = 0; k < 30; k++) {                                   // 넓이·높이 모두 상자 안인 가장 큰 크기 (이분 탐색)
      const m = (lo + hi) / 2; apply(m);
      const ok = lns.every(l => l.scrollWidth <= W) && lns.reduce((a, l) => a + l.getBoundingClientRect().height, 0) <= H;
      if (ok) lo = m; else hi = m;
    }
    apply(lo);
    res.push({ block: b.id, size: +lo.toFixed(1), widths: lns.map(l => l.scrollWidth).join("/"), box: `${W}x${H}` });
  }
  for (const b of document.querySelectorAll('[data-kind="box"]')) {
    const [fw, fh] = JSON.parse(b.dataset.fill || "[0.9,0.68]");      // 상자 안 글자가 차지할 넓이·높이 비율
    const t = b.querySelector(".bt"), W = b.clientWidth * fw, H = b.clientHeight * fh;
    let lo = 10, hi = 400;
    for (let k = 0; k < 30; k++) { const m = (lo + hi) / 2; t.style.fontSize = m + "px"; if (t.scrollWidth <= W && t.getBoundingClientRect().height <= H) lo = m; else hi = m; }
    t.style.fontSize = lo + "px";
    res.push({ block: b.id, size: +lo.toFixed(1) });
  }
  return res;
}

const files = process.argv.slice(2);
if (!files.length) fail("THUMB", "설정 파일 없음", "node video/render/thumb.mjs <썸네일 옆 thumbnail_N.json>");
async function pw() {                                             // render.mjs 와 같음: 로컬에 없으면 전역 설치본
  try { return (await import("playwright")).default; } catch { /* 전역 */ }
  return createRequire(import.meta.url)(path.join(execSync("npm root -g", { encoding: "utf-8" }).trim(), "playwright"));
}
const browser = await (await pw()).chromium.launch({ args: ["--allow-file-access-from-files"] });
try {
  for (const f of files) {
    const specPath = path.resolve(f), dir = path.dirname(specPath);
    let spec;
    try { spec = JSON.parse(fs.readFileSync(specPath, "utf-8")); } catch (e) { fail("THUMB", `설정 읽기 실패 ${f}: ${e.message}`, "JSON 형식 확인"); }
    const [W, H] = spec.size;
    const tmp = path.join(os.tmpdir(), `thumb-${process.pid}.html`);
    fs.writeFileSync(tmp, page(spec, dir));
    const pg = await browser.newPage({ viewport: { width: W, height: H } });
    await pg.goto(pathToFileURL(tmp).href);
    await pg.evaluate(() => document.fonts.ready);
    await pg.waitForFunction(() => [...document.images].every(i => i.complete && i.naturalWidth > 0), null, { timeout: 15000 })
      .catch(() => fail("THUMB", "그림을 읽지 못함", "그림 파일이 깨졌는지 확인 (700KB 넘는 파일은 GitHub 앱이 잘라 올림)"));
    const fontOk = await pg.evaluate(() => document.fonts.check('900 50px "NK"'));
    if (!fontOk) fail("THUMB", "글꼴을 읽지 못함", "node video/scripts/get-fonts.mjs");
    const info = await pg.evaluate(layout);
    const out = path.resolve(dir, spec.out);
    let q = 92, bytes;
    for (; q >= 60; q -= 4) { await pg.screenshot({ path: out, type: "jpeg", quality: q }); bytes = fs.statSync(out).size; if (bytes <= 700_000) break; }
    await pg.close(); fs.unlinkSync(tmp);
    info.forEach(x => log("THUMB", { spec: path.relative(ROOT, specPath), ...x }));
    log("THUMB", { out: path.relative(ROOT, out), size: `${W}x${H}`, quality: q, bytes, ok: bytes <= 700_000 });
  }
} finally { await browser.close(); }
