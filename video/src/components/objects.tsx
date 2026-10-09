// 사물형 컴포넌트 — 버튼, 천칭 저울, 스마트폰, 체크리스트, 쌓이는 블록 (guides/video_guide.md 3-5 "심리·감정", "시청자 행동 권유")
import React from "react";
import {interpolate, useCurrentFrame} from "remotion";
import {C, SANS} from "../design/tokens";
import {enter, prog} from "./anim";
import {Label, Mark, useFg} from "./ui";

const CLAMP = {extrapolateLeft: "clamp", extrapolateRight: "clamp"} as const;

/** 누르는 버튼 (손은 그리지 않음 — 인물 금지). pressAt에 눌림. 빨강은 수익 색이라 쓰지 않고 노랑(그 화면의 강조 한 곳)으로 */
export const PushButton: React.FC<{label: string; at: number; pressAt: number; size?: number}> = ({label, at, pressAt, size = 340}) => {
  const f = useCurrentFrame();
  const down = interpolate(f, [pressAt, pressAt + 4, pressAt + 14], [0, 1, 0.7], CLAMP);
  const lift = 30 * (1 - down);
  return (
    <div style={{position: "relative", width: size + 60, height: size * 0.62 + 90, opacity: enter(f, at)}}>
      {/* 받침 */}
      <div style={{position: "absolute", left: 0, bottom: 0, width: size + 60, height: 96, borderRadius: "50%", background: C.ink, border: `4px solid ${C.ink}`}} />
      {/* 버튼 옆면 */}
      <div style={{position: "absolute", left: 30, bottom: 44, width: size, height: lift + 46, background: "#C9A800", borderLeft: `4px solid ${C.ink}`, borderRight: `4px solid ${C.ink}`}} />
      {/* 버튼 윗면 */}
      <div
        style={{
          position: "absolute",
          left: 30,
          bottom: 44 + lift + 46 - size * 0.31,
          width: size,
          height: size * 0.62,
          borderRadius: "50%",
          background: C.yellow,
          border: `4px solid ${C.ink}`,
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          color: C.ink,
          fontFamily: SANS,
          fontWeight: 900,
          fontSize: 60,
        }}
      >
        {label}
      </div>
    </div>
  );
};

/** 천칭 저울: angle(도) > 0 이면 왼쪽이 아래로. 접시 위 내용은 left/right */
export const Balance: React.FC<{cx: number; cy: number; angle: number; left: React.ReactNode; right: React.ReactNode; at: number; span?: number}> = ({cx, cy, angle, left, right, at, span = 900}) => {
  const f = useCurrentFrame();
  const fg = useFg();
  const o = enter(f, at);
  const r = (angle * Math.PI) / 180;
  const hx = (span / 2) * Math.cos(r);
  const hy = (span / 2) * Math.sin(r);
  const L = {x: cx - hx, y: cy + hy};
  const R = {x: cx + hx, y: cy - hy};
  const hang = 150;
  const pan = (p: {x: number; y: number}, content: React.ReactNode) => (
    <>
      <svg width={1920} height={1080} style={{position: "absolute", left: 0, top: 0, overflow: "visible"}}>
        <path d={`M ${p.x} ${p.y} L ${p.x - 150} ${p.y + hang} M ${p.x} ${p.y} L ${p.x + 150} ${p.y + hang}`} stroke={fg} strokeWidth={4} />
        <path d={`M ${p.x - 190} ${p.y + hang} L ${p.x + 190} ${p.y + hang} Q ${p.x} ${p.y + hang + 70} ${p.x - 190} ${p.y + hang} Z`} fill={fg} />
      </svg>
      <div style={{position: "absolute", left: p.x - 230, width: 460, top: p.y + hang - 8, transform: "translateY(-100%)", display: "flex", flexDirection: "column", alignItems: "center", gap: 8}}>{content}</div>
    </>
  );
  return (
    <div style={{position: "absolute", inset: 0, opacity: o}}>
      {/* 기둥 */}
      <div style={{position: "absolute", left: cx - 8, top: cy, width: 16, height: 300, background: fg}} />
      <div style={{position: "absolute", left: cx - 160, top: cy + 296, width: 320, height: 24, borderRadius: 12, background: fg}} />
      {/* 막대 */}
      <div style={{position: "absolute", left: cx - span / 2, top: cy - 8, width: span, height: 16, borderRadius: 8, background: fg, transform: `rotate(${-angle}deg)`, transformOrigin: "50% 50%"}} />
      <div style={{position: "absolute", left: cx - 22, top: cy - 22, width: 44, height: 44, borderRadius: 99, background: fg}} />
      {pan(L, left)}
      {pan(R, right)}
    </div>
  );
};

/** 저울 접시 위 무게 블록 */
export const Weight: React.FC<{children: React.ReactNode; at: number; color?: string; textColor?: string; w?: number}> = ({children, at, color = C.ink, textColor = C.light, w = 340}) => {
  const f = useCurrentFrame();
  const p = enter(f, at);
  return (
    <div style={{width: w, padding: "14px 10px", borderRadius: 12, background: color, color: textColor, fontFamily: SANS, fontWeight: 900, fontSize: 40, textAlign: "center", opacity: p, transform: `translateY(${(1 - p) * -60}px)`}}>
      {children}
    </div>
  );
};

/** 스마트폰 화면 (실제 앱 UI를 따라 그리지 않은 단순 화면) */
export const Phone: React.FC<{at: number; w?: number; h?: number; children: React.ReactNode; style?: React.CSSProperties}> = ({at, w = 430, h = 640, children, style}) => {
  const f = useCurrentFrame();
  const p = enter(f, at);
  return (
    <div style={{width: w, height: h, borderRadius: 56, border: `10px solid ${C.ink}`, background: C.light, color: C.ink, padding: "70px 34px 40px", boxSizing: "border-box", opacity: p, transform: `translateY(${(1 - p) * 40}px)`, position: "relative", ...style}}>
      <div style={{position: "absolute", top: 22, left: "50%", width: 120, height: 18, marginLeft: -60, borderRadius: 9, background: C.ink}} />
      {children}
    </div>
  );
};

/** 켜짐/꺼짐 스위치 (onAt에 켜짐) */
export const Toggle: React.FC<{onAt: number}> = ({onAt}) => {
  const f = useCurrentFrame();
  const p = prog(f, onAt, 8);
  return (
    <div style={{width: 112, height: 60, borderRadius: 30, background: p > 0.5 ? C.ink : "#D6D1C6", position: "relative", flex: "none"}}>
      <div style={{position: "absolute", top: 6, left: 6 + 52 * p, width: 48, height: 48, borderRadius: 24, background: C.light}} />
    </div>
  );
};

/** 체크리스트 한 줄 */
export const CheckRow: React.FC<{at: number; checkAt?: number; children: React.ReactNode; size?: number; color?: string}> = ({at, checkAt, children, size = 46, color}) => {
  const f = useCurrentFrame();
  const bgFg = useFg();
  const fg = color ?? bgFg;
  const p = enter(f, at);
  return (
    <div style={{display: "flex", alignItems: "center", gap: 26, opacity: p, transform: `translateX(${(1 - p) * -30}px)`}}>
      <div style={{width: size + 18, height: size + 18, border: `5px solid ${fg}`, borderRadius: 10, flex: "none", display: "flex", alignItems: "center", justifyContent: "center"}}>
        {checkAt !== undefined ? <Mark kind="check" at={checkAt} size={size} color={fg} /> : null}
      </div>
      <Label size={size} color={fg}>
        {children}
      </Label>
    </div>
  );
};

/** 같은 종목 위에 쌓이는 블록 (아래에서 위로) */
export type Block = {v: number; label: React.ReactNode; at: number; color?: string; textColor?: string};
export const Stack: React.FC<{x: number; baseY: number; w: number; unit: number; blocks: Block[]; base: React.ReactNode}> = ({x, baseY, w, unit, blocks, base}) => {
  const f = useCurrentFrame();
  const fg = useFg();
  let y = baseY;
  return (
    <>
      <div style={{position: "absolute", left: x - 30, top: baseY, width: w + 60, height: 8, background: fg, borderRadius: 4}} />
      <div style={{position: "absolute", left: x - 100, width: w + 200, top: baseY + 22, textAlign: "center"}}>{base}</div>
      {blocks.map((b, i) => {
        const h = b.v * unit;
        y -= h;
        const p = enter(f, b.at);
        return (
          <div
            key={i}
            style={{
              position: "absolute",
              left: x,
              top: y,
              width: w,
              height: h - 6,
              borderRadius: 10,
              background: b.color ?? C.ink,
              color: b.textColor ?? C.light,
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              fontFamily: SANS,
              fontWeight: 900,
              fontSize: 40,
              opacity: p,
              transform: `translateY(${(1 - p) * -90}px)`,
            }}
          >
            {b.label}
          </div>
        );
      })}
    </>
  );
};
