// 디자인 시스템 — guides/video_guide.md 3번 (모든 영상 공통)
export const FPS = 30;
export const W = 1920;
export const H = 1080;

export const C = {
  cream: "#F2EBDD",      // 기본 배경
  navy: "#14213D",       // 위기·손실 구간 배경
  light: "#FAF6EE",      // 해결·희망 구간 배경
  ink: "#1E1E1E",        // 글자·선
  inkOnNavy: "#F7F3EA",  // 네이비 배경의 글자
  gain: "#E63B2E",       // 수익·상승 (빨강)
  loss: "#2D6CDF",       // 손실·하락 (파랑)
  yellow: "#FFD400",     // 핵심 강조 (한 화면에 한 곳)
  gray: "#9A968E",       // 비교 대상·보조
} as const;

export type Bg = "cream" | "navy" | "light";
export const bgColor = (bg: Bg) => (bg === "navy" ? C.navy : bg === "light" ? C.light : C.cream);
export const fgColor = (bg: Bg) => (bg === "navy" ? C.inkOnNavy : C.ink);

export const SIZE = {
  bigNumber: 190,   // 160–220
  headline: 80,     // 72–88 (Serif 900)
  label: 40,        // 36–44
  caption: 26,      // 출처·개념도 (최소 28px 규칙 → 캡션도 28 이상으로 씀)
  min: 28,
  margin: 96,
  subtitle: 46,
} as const;

// 모션 (프레임)
export const M = {
  enter: 15,       // 등장 12–18
  exit: 9,         // 퇴장 8–10
  stagger: 5,      // 순차 등장 4–6
  highlight: 10,   // 형광펜
  count: 25,       // 숫자 카운트 20–30
  subFade: 4,      // 자막 페이드
} as const;

export const SANS = "NotoSansKR";
export const SERIF = "NotoSerifKR";
