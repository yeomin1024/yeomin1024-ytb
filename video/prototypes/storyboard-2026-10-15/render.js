// VERSION: v1.1 — 2026-10-15 — 표준 모드(doctype)로 렌더, extra 모드(시각 지정). v1.0 — 스토리보드 HTML(GSAP 타임라인)을 Playwright로 멈춰 찍어 대표 장면(stills)·미리보기 영상(video)·페이지 확인(page)을 만든다
// 사용: npm install (gsap) 뒤 NODE_PATH=$(npm root -g) node render.js stills|video|page|extra  (playwright 는 전역 설치본)
//   CDN(gsap)·구글 폰트 요청은 로컬 파일로 돌려준다 (렌더 환경은 cdnjs 가 막혀 있음)
const { chromium } = require("playwright");
const fs = require("fs");
const path = require("path");
const { spawn } = require("child_process");

const DIR = __dirname;
const MODE = process.argv[2] || "stills";
const W = Number(process.env.W || 1280), H = Math.round(W * 9 / 16);
const FPS = Number(process.env.FPS || 30);
const log = (stage, kv) => console.log(`[${stage}] ${new Date().toISOString().slice(11, 19)} ` + Object.entries(kv).map(([k, v]) => `${k}=${v}`).join(" "));
const CSS = [500, 700, 900].map(w => `@font-face{font-family:"Noto Sans KR";font-weight:${w};src:url(http://localfonts/NotoSansKR-${w}.ttf) format("truetype")}`).join("\n");

async function open(viewport, query) {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport, deviceScaleFactor: 1 });
  await page.route("https://cdnjs.cloudflare.com/**", r => r.fulfill({ path: path.join(DIR, "node_modules/gsap/dist/gsap.min.js"), contentType: "application/javascript" }));
  await page.route("https://fonts.googleapis.com/**", r => r.fulfill({ contentType: "text/css", body: CSS }));
  // 폰트: 이 폴더 fonts/ 가 없으면 저장소 video/public/fonts (video/scripts/get-fonts.mjs 가 받음)
  const FONTS = fs.existsSync(path.join(DIR, "fonts")) ? path.join(DIR, "fonts") : path.join(DIR, "..", "..", "public", "fonts");
  await page.route("http://localfonts/**", r => r.fulfill({ path: path.join(FONTS, path.basename(new URL(r.request().url()).pathname)), contentType: "font/ttf" }));
  await page.route("https://fonts.gstatic.com/**", r => r.abort());
  page.on("pageerror", e => log("PAGEERROR", { msg: JSON.stringify(e.message) }));
  page.on("console", m => { if (m.type() === "error" || m.type() === "warning") log("CONSOLE", { type: m.type(), msg: JSON.stringify(m.text()) }); });
  // 게시할 때처럼 표준 모드로 (doctype 없으면 quirks 모드라 클래스 대소문자가 섞임)
  fs.writeFileSync(path.join(DIR, "_render.html"), "<!doctype html><html><head><meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\"></head><body>" + fs.readFileSync(path.join(DIR, "storyboard.html"), "utf-8") + "</body></html>");
  await page.goto("file://" + path.join(DIR, "_render.html") + query);
  await page.evaluate(async () => { await Promise.all([500, 700, 900].map(w => document.fonts.load(`${w} 100px "Noto Sans KR"`, "가나다0"))); await document.fonts.ready; });
  return { browser, page };
}

(async () => {
  const t0 = Date.now();
  if (MODE === "page") {
    const { browser, page } = await open({ width: 1280, height: 900 }, "");
    await page.waitForTimeout(400);
    await page.screenshot({ path: path.join(DIR, "out", "page.png"), fullPage: true });
    const over = await page.evaluate(() => document.documentElement.scrollWidth > window.innerWidth);
    await page.setViewportSize({ width: 400, height: 800 });
    await page.waitForTimeout(300);
    await page.screenshot({ path: path.join(DIR, "out", "page_phone.png"), fullPage: false });
    const overPhone = await page.evaluate(() => document.documentElement.scrollWidth > window.innerWidth);
    log("PAGE", { horizontal_overflow_desktop: over, horizontal_overflow_phone: overPhone, sec: ((Date.now() - t0) / 1000).toFixed(1) });
    await browser.close();
    return;
  }
  const { browser, page } = await open({ width: W, height: H }, "?render=1");
  const D = await page.evaluate(() => window.SB.D);
  if (MODE === "stills") {
    fs.mkdirSync(path.join(DIR, "frames"), { recursive: true });
    const cuts = await page.evaluate(() => window.SB.cuts);
    for (const [n, , , key, , name] of cuts) {
      await page.evaluate(t => window.SB.seek(t), key);
      const f = path.join(DIR, "frames", `s${String(n).padStart(2, "0")}.jpg`);
      await page.screenshot({ path: f, type: "jpeg", quality: 86 });
      log("STILL", { cut: n, t: key, name: JSON.stringify(name), file: path.basename(f), kb: Math.round(fs.statSync(f).size / 1024) });
    }
  } else if (MODE === "extra") {
    for (const t of (process.env.TIMES || "").split(",").filter(Boolean).map(Number)) {
      await page.evaluate(x => window.SB.seek(x), t);
      await page.screenshot({ path: path.join(DIR, "out", `t_${t}.jpg`), type: "jpeg", quality: 86 });
      log("EXTRA", { t });
    }
  } else if (MODE === "video") {
    fs.mkdirSync(path.join(DIR, "out"), { recursive: true });
    const outFile = path.join(DIR, "out", `storyboard_preview_${H}p.mp4`);
    const ff = spawn("ffmpeg", ["-y", "-v", "error", "-f", "image2pipe", "-framerate", String(FPS), "-i", "-", "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", "-movflags", "+faststart", outFile], { stdio: ["pipe", "inherit", "inherit"] });
    const N = Math.round(D * FPS);
    for (let i = 0; i <= N; i++) {
      await page.evaluate(t => window.SB.seek(t), i / FPS);
      const buf = await page.screenshot({ type: "jpeg", quality: 90 });
      if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once("drain", r));
      if (i % 300 === 0) log("FRAME", { i, of: N, t: (i / FPS).toFixed(1), sec: ((Date.now() - t0) / 1000).toFixed(0) });
    }
    ff.stdin.end();
    await new Promise((res, rej) => ff.on("close", c => c === 0 ? res() : rej(new Error("ffmpeg exit " + c))));
    log("VIDEO", { file: outFile, frames: N + 1, fps: FPS, size: `${W}x${H}`, mb: (fs.statSync(outFile).size / 1e6).toFixed(1), sec: ((Date.now() - t0) / 1000).toFixed(0) });
  }
  await browser.close();
})().catch(e => { log("ERROR", { stage: MODE, msg: JSON.stringify(e.message), next: "PAGEERROR 줄과 storyboard.html 스크립트를 확인" }); process.exit(1); });
