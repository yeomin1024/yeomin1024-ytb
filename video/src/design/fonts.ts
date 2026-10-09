// 폰트: public/fonts/ 의 Noto Sans KR(500·700·900), Noto Serif KR(700·900)을 로드 (scripts/get-fonts.mjs 가 받음)
// @remotion/google-fonts 대신 로컬 파일을 쓰는 이유: 한글은 굵기마다 조각 파일이 120개라 렌더가 느리고 불안정함
import {continueRender, delayRender, staticFile} from "remotion";
import {SANS, SERIF} from "./tokens";

const FILES: [string, string, number][] = [
  [SANS, "NotoSansKR-500.ttf", 500], [SANS, "NotoSansKR-700.ttf", 700], [SANS, "NotoSansKR-900.ttf", 900],
  [SERIF, "NotoSerifKR-700.ttf", 700], [SERIF, "NotoSerifKR-900.ttf", 900],
];

let started = false;
export const loadFonts = () => {
  if (started || typeof document === "undefined") return;
  started = true;
  const handle = delayRender("한글 폰트 로드");
  Promise.all(
    FILES.map(([family, file, weight]) => {
      const face = new FontFace(family, `url(${staticFile(`fonts/${file}`)})`, {weight: String(weight)});
      return face.load().then((f) => document.fonts.add(f));
    }),
  )
    .then(() => continueRender(handle))
    .catch((e) => {
      console.error("[fonts] 로드 실패 → video 폴더에서 npm run fonts 실행", e);
      continueRender(handle);
    });
};
