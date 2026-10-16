// VERSION: v1.1 — 2026-10-16 — 찍을 시안 파일을 고름 (5번째 인자, 기본 race3d.html — v4 는 race3d_v4.html). node snap.mjs <out.png> [rule] [date] [page]
// v1.0 — 2026-10-16 — race3d.html 한 장 찍기 (시안 확인용).
import { createRequire } from "module";
import path from "path";
import { fileURLToPath, pathToFileURL } from "url";
const HERE = path.dirname(fileURLToPath(import.meta.url));
const require = createRequire(path.join(HERE, "../../render/"));
const pw = require("playwright");
const [out, rule = "dip10", date = "2023-09-29", page = "race3d.html"] = process.argv.slice(2);
let b; try { b = await pw.chromium.launch(); } catch { b = await pw.chromium.launch({ executablePath: "/opt/pw-browsers/chromium" }); }
const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
const errs = []; p.on("pageerror", e => errs.push(String(e))); p.on("console", m => { if (m.type() === "error") errs.push(m.text()); else if (m.text().startsWith("[STILL]")) console.log(m.text()); });
await p.goto(pathToFileURL(path.join(HERE, page)).href + `?rule=${rule}&date=${date}`);
await p.waitForFunction(() => window.READY === true, null, { timeout: 30000 });
await p.evaluate(() => document.fonts.ready);
await p.locator("#stage").screenshot({ path: out });
console.log(`[STILL] ${new Date().toISOString()} file=${out} page=${page} rule=${rule} date=${date} errors=${errs.length}`); errs.forEach(e => console.log("  ", e));
await b.close();
