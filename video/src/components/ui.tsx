// 공통 UI 기본 요소 — 장면 틀, 글자, 형광펜, 칩, 화살표, ✓/✗ 표시 (guides/video_guide.md 3-2·3-4)
import React, {createContext, useContext} from "react";
import {AbsoluteFill, interpolate, useCurrentFrame} from "remotion";
import {Bg, C, H, M, SANS, SERIF, SIZE, W, bgColor, fgColor} from "../design/tokens";
import {enter, prog} from "./anim";

const CLAMP = {extrapolateLeft: "clamp", extrapolateRight: "clamp"} as const;

// ── 배경 컨텍스트: 글자색·칩 색을 배경에 맞춘다 ──
const BgCtx = createContext<Bg>("cream");
export const useBg = () => useContext(BgCtx);
export const useFg = () => fgColor(useBg());

/** 등장(spring) + 선택적 퇴장(9프레임). until 이후 사라진다. */
export const vis = (f: number, at: number, until?: number, dist = 24): React.CSSProperties => {
  const p = enter(f, at);
  const q = until === undefined ? 1 : 1 - prog(f, until, M.exit);
  return {opacity: p * q, transform: `translateY(${(1 - p) * dist}px)`};
};
/** 살짝 커지며 등장 (말풍선·도장) */
export const popIn = (f: number, at: number, until?: number): React.CSSProperties => {
  const p = enter(f, at);
  const q = until === undefined ? 1 : 1 - prog(f, until, M.exit);
  return {opacity: p * q, transform: `scale(${0.86 + 0.14 * p})`};
};
/** 퇴장만 (0→1 사이 불투명도) */
export const fadeOut = (f: number, until?: number) => (until === undefined ? 1 : 1 - prog(f, until, M.exit));

// ── 찢어진 종이 와이프 (가벼운 polygon clip-path) ──
export const WIPE = 16;
const JAG = [-38, 22, -12, 40, -26, 8, 34, -40, 16, -6, 28, -30, 12, 38, -18, 4, 30, -34, 18];
const tornClip = (p: number) => {
  if (p >= 1) return undefined;
  const edge = interpolate(p, [0, 1], [-80, W + 80]);
  const n = JAG.length - 1;
  const pts = JAG.map((j, i) => `${(edge + j).toFixed(1)}px ${((i * H) / n).toFixed(1)}px`);
  return `polygon(0px 0px, ${pts.join(", ")}, 0px ${H}px)`;
};

/** 장면 틀: 배경색 + 고정 점 질감 + 1.00→1.03 줌인 + (선택) 찢어진 종이 와이프 */
export const Scene: React.FC<{bg: Bg; dur: number; wipe?: boolean; children: React.ReactNode}> = ({bg, dur, wipe, children}) => {
  const f = useCurrentFrame();
  const z = interpolate(f, [0, dur], [1, 1.03], CLAMP);
  const dot = bg === "navy" ? "rgba(255,255,255,0.045)" : "rgba(90,70,40,0.07)";
  return (
    <BgCtx.Provider value={bg}>
      <AbsoluteFill
        style={{
          background: bgColor(bg),
          backgroundImage: `radial-gradient(${dot} 1.2px, transparent 1.7px)`,
          backgroundSize: "7px 7px",
          clipPath: wipe ? tornClip(prog(f, 0, WIPE)) : undefined,
          color: fgColor(bg),
          fontFamily: SANS,
          fontVariantNumeric: "tabular-nums",
        }}
      >
        <AbsoluteFill style={{transform: `scale(${z})`, transformOrigin: "50% 42%"}}>{children}</AbsoluteFill>
      </AbsoluteFill>
    </BgCtx.Provider>
  );
};

/** 절대 위치 상자 (x, y = 왼쪽 위 / center면 x가 가운데) */
export const Box: React.FC<{x: number; y: number; w?: number; center?: boolean; style?: React.CSSProperties; children: React.ReactNode}> = ({x, y, w, center, style, children}) => (
  <div
    style={{
      position: "absolute",
      left: center ? x - (w ?? 0) / 2 : x,
      top: y,
      width: w,
      textAlign: center ? "center" : undefined,
      ...style,
    }}
  >
    {children}
  </div>
);

type TP = {children: React.ReactNode; style?: React.CSSProperties; color?: string; size?: number};
export const Headline: React.FC<TP> = ({children, style, color, size = SIZE.headline}) => (
  <div style={{fontFamily: SERIF, fontWeight: 900, fontSize: size, lineHeight: 1.22, letterSpacing: "-0.01em", color, ...style}}>{children}</div>
);
export const Label: React.FC<TP & {weight?: number}> = ({children, style, color, size = SIZE.label, weight = 700}) => (
  <div style={{fontFamily: SANS, fontWeight: weight, fontSize: size, lineHeight: 1.3, color, ...style}}>{children}</div>
);
export const Big: React.FC<TP> = ({children, style, color, size = SIZE.bigNumber}) => (
  <div style={{fontFamily: SANS, fontWeight: 900, fontSize: size, lineHeight: 1, letterSpacing: "-0.035em", fontVariantNumeric: "tabular-nums", whiteSpace: "nowrap", color, ...style}}>{children}</div>
);
export const Caption: React.FC<TP> = ({children, style, color = C.gray, size = SIZE.min}) => (
  <div style={{fontFamily: SANS, fontWeight: 500, fontSize: size, lineHeight: 1.3, color, ...style}}>{children}</div>
);

/** 노랑 형광펜: 왼쪽→오른쪽 10프레임. 아래 글자 위에 노랑 박스+잉크 글자 사본을 잘라서 드러낸다 (네이비에서도 읽힘) */
export const Hi: React.FC<{at: number; until?: number; children: React.ReactNode}> = ({at, until, children}) => {
  const f = useCurrentFrame();
  const p = prog(f, at, M.highlight) * fadeOut(f, until);
  const pad = "0 0.16em";
  return (
    <span style={{position: "relative", display: "inline-block", padding: pad}}>
      <span>{children}</span>
      <span
        style={{
          position: "absolute",
          inset: 0,
          padding: pad,
          background: C.yellow,
          color: C.ink,
          borderRadius: 8,
          whiteSpace: "nowrap",
          clipPath: `inset(-2px ${((1 - p) * 100).toFixed(2)}% -2px 0)`,
        }}
      >
        {children}
      </span>
    </span>
  );
};

/** 칩: 날짜·태그. solid = 잉크 바탕, outline = 테두리, loss/gain = 파랑/빨강 바탕 흰 글자 */
export const Chip: React.FC<{children: React.ReactNode; variant?: "solid" | "outline" | "loss" | "gain" | "gray"; size?: number; style?: React.CSSProperties}> = ({
  children,
  variant = "solid",
  size = 34,
  style,
}) => {
  const bg = useBg();
  const fg = fgColor(bg);
  const inv = bg === "navy" ? C.navy : C.light;
  const map = {
    solid: {background: fg, color: inv, border: `3px solid ${fg}`},
    outline: {background: "transparent", color: fg, border: `3px solid ${fg}`},
    loss: {background: C.loss, color: "#FFFFFF", border: `3px solid ${C.loss}`},
    gain: {background: C.gain, color: "#FFFFFF", border: `3px solid ${C.gain}`},
    gray: {background: "transparent", color: C.gray, border: `3px solid ${C.gray}`},
  }[variant];
  return (
    <div style={{display: "inline-block", fontFamily: SANS, fontWeight: 700, fontSize: size, lineHeight: 1.2, padding: "10px 26px", borderRadius: 999, whiteSpace: "nowrap", ...map, ...style}}>
      {children}
    </div>
  );
};

/** 화살표 (선이 그려지며 등장). len = 길이(px) */
export const Arrow: React.FC<{dir?: "right" | "down" | "up"; len?: number; at: number; color?: string; stroke?: number; style?: React.CSSProperties}> = ({
  dir = "right",
  len = 120,
  at,
  color,
  stroke = 8,
  style,
}) => {
  const f = useCurrentFrame();
  const fg = useFg();
  const col = color ?? fg;
  const p = prog(f, at, 12);
  const head = 22;
  const horiz = dir === "right";
  const w = horiz ? len : head * 2 + stroke;
  const h = horiz ? head * 2 + stroke : len;
  const line = horiz ? `M 0 ${h / 2} L ${len - 4} ${h / 2}` : dir === "down" ? `M ${w / 2} 0 L ${w / 2} ${len - 4}` : `M ${w / 2} ${len} L ${w / 2} 4`;
  const tip = horiz
    ? `M ${len - head} ${h / 2 - head} L ${len - 3} ${h / 2} L ${len - head} ${h / 2 + head}`
    : dir === "down"
      ? `M ${w / 2 - head} ${len - head} L ${w / 2} ${len - 3} L ${w / 2 + head} ${len - head}`
      : `M ${w / 2 - head} ${head} L ${w / 2} 3 L ${w / 2 + head} ${head}`;
  return (
    <svg width={w} height={h} style={{overflow: "visible", ...style}}>
      <path d={line} stroke={col} strokeWidth={stroke} strokeLinecap="round" fill="none" strokeDasharray={len} strokeDashoffset={len * (1 - p)} />
      <path d={tip} stroke={col} strokeWidth={stroke} strokeLinecap="round" strokeLinejoin="round" fill="none" opacity={p > 0.85 ? 1 : 0} />
    </svg>
  );
};

/** ✓ / ✗ 표시 (SVG, 그려지며 등장) */
export const Mark: React.FC<{kind: "check" | "cross"; at: number; size?: number; color?: string; style?: React.CSSProperties}> = ({kind, at, size = 72, color, style}) => {
  const f = useCurrentFrame();
  const fg = useFg();
  const p = prog(f, at, 10);
  const d = kind === "check" ? "M 12 52 L 40 80 L 90 18" : "M 18 18 L 82 82 M 82 18 L 18 82";
  const L = kind === "check" ? 120 : 182;
  return (
    <svg width={size} height={size} viewBox="0 0 100 100" style={{overflow: "visible", ...style}}>
      <path d={d} stroke={color ?? fg} strokeWidth={13} strokeLinecap="round" strokeLinejoin="round" fill="none" strokeDasharray={L} strokeDashoffset={L * (1 - p)} />
    </svg>
  );
};

/** 취소선 (가로로 그어짐) */
export const Strike: React.FC<{at: number; color?: string; children: React.ReactNode}> = ({at, color, children}) => {
  const f = useCurrentFrame();
  const fg = useFg();
  const p = prog(f, at, 10);
  return (
    <span style={{position: "relative", display: "inline-block"}}>
      {children}
      <span style={{position: "absolute", left: -6, top: "52%", height: 7, width: `calc(${p * 100}% + 12px)`, background: color ?? fg, borderRadius: 4}} />
    </span>
  );
};

/** 밝은 카드 (계좌·뉴스·메모 공통 바탕): 크림/네이비 어디서나 같은 모양 */
export const Card: React.FC<{style?: React.CSSProperties; children: React.ReactNode}> = ({style, children}) => (
  <div style={{background: C.light, color: C.ink, border: `4px solid ${C.ink}`, borderRadius: 22, padding: "34px 44px", boxShadow: "0 8px 0 rgba(20,20,20,0.14)", ...style}}>{children}</div>
);

/** "개념도" 등 구석 캡션 (그래픽 영역 오른쪽 아래) */
export const CornerNote: React.FC<{children: React.ReactNode; at: number; until?: number; x?: number; y?: number}> = ({children, at, until, x = W - SIZE.margin, y = 770}) => {
  const f = useCurrentFrame();
  return (
    <div style={{position: "absolute", right: W - x, top: y, opacity: enter(f, at) * fadeOut(f, until)}}>
      <Caption>{children}</Caption>
    </div>
  );
};
