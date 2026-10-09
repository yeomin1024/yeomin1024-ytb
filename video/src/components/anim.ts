// 모션 규칙 — guides/video_guide.md 3-4 (spring ease-out, 과한 바운스 금지)
import {interpolate, spring, Easing} from "remotion";
import {FPS, M} from "../design/tokens";

/** at 프레임부터 12–18프레임 동안 등장 (0→1). */
export const enter = (frame: number, at: number, dur = M.enter) =>
  spring({frame: frame - at, fps: FPS, durationInFrames: dur, config: {damping: 200, mass: 0.6}});

/** 등장 스타일: 아래에서 살짝 올라오며 페이드 */
export const rise = (frame: number, at: number, dist = 24): React.CSSProperties => {
  const p = enter(frame, at);
  return {opacity: p, transform: `translateY(${(1 - p) * dist}px)`};
};

/** 0→1 진행 (선형 구간 + ease-out) */
export const prog = (frame: number, at: number, dur: number) =>
  interpolate(frame, [at, at + dur], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.out(Easing.cubic)});

/** 숫자 카운트업/다운 20–30프레임 */
export const count = (frame: number, at: number, from: number, to: number, dur: number = M.count) =>
  from + (to - from) * prog(frame, at, dur);

/** 3프레임 흔들림 (손실 순간) */
export const shake = (frame: number, at: number) => {
  const d = frame - at;
  return d >= 0 && d < 6 ? Math.sin(d * 2.4) * 10 * (1 - d / 6) : 0;
};

/** 한 자막 안에서 k번째 요소 시점 (자막 길이를 n등분) */
export const within = (from: number, to: number, k: number, n: number) => Math.round(from + ((to - from) * k) / n);
