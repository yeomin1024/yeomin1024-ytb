// 차트 컴포넌트 — 라인(stroke-dashoffset으로 그려짐), 세로 막대 비교, 연도 타임라인 (guides/video_guide.md 3-4·3-5)
import React from "react";
import {useCurrentFrame} from "remotion";
import {C, SANS} from "../design/tokens";
import {enter, prog} from "./anim";
import {Label, useFg} from "./ui";

export type P = [number, number]; // 픽셀 좌표 (1920×1080 화면 기준)

/** 데이터 → 픽셀: xs는 화면 x를 직접 주고, 값(y)만 선형 변환 */
export const yScale = (v0: number, v1: number, y0: number, y1: number) => (v: number) => y0 + ((v - v0) / (v1 - v0)) * (y1 - y0);

const segLen = (pts: P[]) => pts.slice(1).reduce((a, p, i) => a + Math.hypot(p[0] - pts[i][0], p[1] - pts[i][1]), 0);

/** 지금까지 그려진 끝점 (라벨을 선 끝에 붙일 때) */
export const pointAt = (pts: P[], t: number): P => {
  const total = segLen(pts);
  let left = total * Math.max(0, Math.min(1, t));
  for (let i = 1; i < pts.length; i++) {
    const a = pts[i - 1];
    const b = pts[i];
    const l = Math.hypot(b[0] - a[0], b[1] - a[1]);
    if (left <= l || i === pts.length - 1) {
      const k = l === 0 ? 0 : Math.min(1, left / l);
      return [a[0] + (b[0] - a[0]) * k, a[1] + (b[1] - a[1]) * k];
    }
    left -= l;
  }
  return pts[pts.length - 1];
};

/** 전체 화면 SVG 레이어 */
export const Layer: React.FC<{children: React.ReactNode; style?: React.CSSProperties}> = ({children, style}) => (
  <svg width={1920} height={1080} viewBox="0 0 1920 1080" style={{position: "absolute", left: 0, top: 0, overflow: "visible", ...style}}>
    {children}
  </svg>
);

/** 꺾은선: at부터 dur 동안 그려짐. dashed면 그리기 대신 페이드 */
export const Line: React.FC<{pts: P[]; at: number; dur?: number; color?: string; width?: number; dashed?: boolean; opacity?: number}> = ({
  pts,
  at,
  dur = 30,
  color,
  width = 8,
  dashed,
  opacity = 1,
}) => {
  const f = useCurrentFrame();
  const fg = useFg();
  const d = pts.map((p, i) => `${i ? "L" : "M"} ${p[0].toFixed(1)} ${p[1].toFixed(1)}`).join(" ");
  if (dashed) {
    return <path d={d} stroke={color ?? C.gray} strokeWidth={width} fill="none" strokeDasharray="18 16" strokeLinecap="round" opacity={enter(f, at) * opacity} />;
  }
  const L = segLen(pts);
  const p = prog(f, at, dur);
  return <path d={d} stroke={color ?? fg} strokeWidth={width} fill="none" strokeLinecap="round" strokeLinejoin="round" strokeDasharray={L + 1} strokeDashoffset={(L + 1) * (1 - p)} opacity={p > 0 ? opacity : 0} />;
};

export const Dot: React.FC<{p: P; at: number; color?: string; r?: number}> = ({p, at, color, r = 13}) => {
  const f = useCurrentFrame();
  const fg = useFg();
  const k = enter(f, at);
  return <circle cx={p[0]} cy={p[1]} r={r * k} fill={color ?? fg} stroke={C.light} strokeWidth={4} />;
};

/** 점 옆 라벨 (HTML). anchor: 점 기준 위치 */
export const PtLabel: React.FC<{p: P; at: number; until?: number; anchor?: "top" | "bottom" | "left" | "right"; children: React.ReactNode; gap?: number}> = ({
  p,
  at,
  until,
  anchor = "top",
  children,
  gap = 26,
}) => {
  const f = useCurrentFrame();
  const o = enter(f, at) * (until === undefined ? 1 : 1 - prog(f, until, 9));
  const t = {
    top: `translate(-50%, calc(-100% - ${gap}px))`,
    bottom: `translate(-50%, ${gap}px)`,
    left: `translate(calc(-100% - ${gap}px), -50%)`,
    right: `translate(${gap}px, -50%)`,
  }[anchor];
  return <div style={{position: "absolute", left: p[0], top: p[1], transform: t, opacity: o, whiteSpace: "nowrap", textAlign: "center"}}>{children}</div>;
};

/** 가로 기준선 (점선) + 왼쪽 라벨 */
export const HRule: React.FC<{y: number; x0: number; x1: number; at: number; color?: string; labelAt?: "right" | "aboveEnd"; children?: React.ReactNode}> = ({y, x0, x1, at, color = C.gray, labelAt = "right", children}) => {
  const f = useCurrentFrame();
  const o = enter(f, at);
  const w = (x1 - x0) * prog(f, at, 14);
  return (
    <>
      <div style={{position: "absolute", left: x0, top: y - 3, width: w, height: 0, borderTop: `6px dashed ${color}`, opacity: o}} />
      {children ? (
        <div style={{position: "absolute", left: labelAt === "right" ? x1 + 20 : x1, top: labelAt === "right" ? y : y - 14, transform: labelAt === "right" ? "translateY(-50%)" : "translate(-100%, -100%)", opacity: o, whiteSpace: "nowrap"}}>{children}</div>
      ) : null}
    </>
  );
};

/** 세로 막대 비교: 각 막대 높이(0~1), 아래 라벨, 위 값 라벨 */
export type BarItem = {h: number; color: string; label: React.ReactNode; top?: React.ReactNode; at: number};
export const Bars: React.FC<{items: BarItem[]; x: number; baseY: number; maxH: number; barW?: number; gap?: number}> = ({items, x, baseY, maxH, barW = 220, gap = 200}) => {
  const f = useCurrentFrame();
  const fg = useFg();
  return (
    <>
      <div style={{position: "absolute", left: x - 40, top: baseY, width: items.length * barW + (items.length - 1) * gap + 80, height: 6, background: fg}} />
      {items.map((it, i) => {
        const h = maxH * it.h * prog(f, it.at, 22);
        const left = x + i * (barW + gap);
        return (
          <React.Fragment key={i}>
            <div style={{position: "absolute", left, top: baseY - h, width: barW, height: h, background: it.color, borderRadius: "10px 10px 0 0"}} />
            <div style={{position: "absolute", left: left - gap / 2, width: barW + gap, top: baseY + 18, textAlign: "center", opacity: enter(f, it.at)}}>
              <Label size={38}>{it.label}</Label>
            </div>
            {it.top ? (
              <div style={{position: "absolute", left: left - gap / 2, width: barW + gap, top: baseY - h - 16, transform: "translateY(-100%)", textAlign: "center", opacity: enter(f, it.at + 12)}}>
                {it.top}
              </div>
            ) : null}
          </React.Fragment>
        );
      })}
    </>
  );
};

/** 연도 타임라인: 시작·끝 연도만 + 가운데 기간 라벨 */
export const YearLine: React.FC<{x0: number; x1: number; y: number; from: string; to: string; mid: React.ReactNode; at: number}> = ({x0, x1, y, from, to, mid, at}) => {
  const f = useCurrentFrame();
  const fg = useFg();
  const p = prog(f, at, 24);
  const end = x0 + (x1 - x0) * p;
  const o0 = enter(f, at);
  const o1 = enter(f, at + 20);
  const yr: React.CSSProperties = {position: "absolute", top: y + 30, transform: "translateX(-50%)", fontFamily: SANS, fontWeight: 900, fontSize: 56};
  return (
    <>
      <div style={{position: "absolute", left: x0, top: y - 4, width: end - x0, height: 8, background: fg, borderRadius: 4}} />
      <div style={{position: "absolute", left: x0 - 16, top: y - 16, width: 32, height: 32, borderRadius: 99, background: fg, opacity: o0}} />
      <div style={{position: "absolute", left: x1 - 16, top: y - 16, width: 32, height: 32, borderRadius: 99, background: fg, opacity: o1}} />
      <div style={{...yr, left: x0, opacity: o0}}>{from}</div>
      <div style={{...yr, left: x1, opacity: o1}}>{to}</div>
      <div style={{position: "absolute", left: (x0 + x1) / 2, top: y - 40, transform: "translate(-50%, -100%)", opacity: o1}}>{mid}</div>
    </>
  );
};
