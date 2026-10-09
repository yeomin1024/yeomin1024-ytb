// 영상용 한글 폰트를 Google Fonts에서 받아 public/fonts/ 에 저장 (npm install 때 자동 실행, 이미 있으면 건너뜀)
// Noto Sans KR 500/700/900, Noto Serif KR 700/900 — SIL Open Font License
import fs from "node:fs";
import path from "node:path";

const OUT = path.join(path.dirname(new URL(import.meta.url).pathname.replace(/^\/([A-Za-z]:)/, "$1")), "..", "public", "fonts");
const FONTS = [
  ["Noto Sans KR", "NotoSansKR", [500, 700, 900]],
  ["Noto Serif KR", "NotoSerifKR", [700, 900]],
];
fs.mkdirSync(OUT, {recursive: true});
for (const [family, file, weights] of FONTS) {
  for (const w of weights) {
    const dest = path.join(OUT, `${file}-${w}.ttf`);
    if (fs.existsSync(dest) && fs.statSync(dest).size > 100000) continue;
    const css = await (await fetch(`https://fonts.googleapis.com/css2?family=${encodeURIComponent(family)}:wght@${w}`)).text();
    const url = (css.match(/url\((https:[^)]+\.ttf)\)/) || [])[1];
    if (!url) throw new Error(`[fonts] ${family} ${w}: TTF 주소를 찾지 못함`);
    const buf = Buffer.from(await (await fetch(url)).arrayBuffer());
    fs.writeFileSync(dest, buf);
    console.log(`[fonts] 받음 ${path.basename(dest)} (${(buf.length / 1e6).toFixed(1)}MB)`);
  }
}
console.log(`[fonts] 준비 완료: ${OUT}`);
