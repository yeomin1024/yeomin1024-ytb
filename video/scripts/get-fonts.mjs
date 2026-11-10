// 영상용 한글 폰트를 Google Fonts에서 받아 public/fonts/ 에 저장 (npm install 때 자동 실행, 이미 있으면 건너뜀)
// Noto Sans KR 500/700/900, Noto Serif KR 700/900 (+ 2026-11-05 Noto Sans · Noto Sans JP · Noto Sans Devanagari 900 — 외국어 썸네일) — SIL Open Font License
import fs from "node:fs";
import path from "node:path";

const OUT = path.join(path.dirname(new URL(import.meta.url).pathname.replace(/^\/([A-Za-z]:)/, "$1")), "..", "public", "fonts");
const FONTS = [
  ["Noto Sans KR", "NotoSansKR", [500, 700, 900]],
  ["Noto Serif KR", "NotoSerifKR", [700, 900]],
  // 2026-11-05 — 외국어 썸네일 (사용자 지시 "외국어 자막, 제목, 썸네일 등 외국어 설정에 필요한 것들 생성하고 지시사항에 반영해"):
  // 라틴(영어·인도네시아어·포르투갈어·스페인어·독일어·베트남어·튀르키예어) · 일본어 · 힌디어(데바나가리) — video/render/thumb.mjs v1.2 spec.lang
  ["Noto Sans", "NotoSans", [900]],
  ["Noto Sans JP", "NotoSansJP", [900]],
  ["Noto Sans Devanagari", "NotoSansDevanagari", [900]],
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
