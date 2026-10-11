// molppang-2026-10 전용 시각 요소 (공통 컴포넌트는 고치지 않음) — guides/video_guide.md 3-5, 맞는 패턴이 없을 때 단순 도형
// - MyAccount: 사연 계좌 카드 (전 재산 7,000만 원, 막대 잉크 = 몽고디비, 빗금 = 현금) — 영상 끝까지 같은 모양·같은 색
// - BoxRow: 10개 종목에 나눈 칸 (칸마다 아래에서 채움, 잃은 부분은 파랑 점선) / WeightBar: 계좌 비중 막대 (계좌 카드 막대와 같은 무늬)
// - Waffle(10×10, 소수 칸 채움), MiniAccount(작은 계좌 아이콘), SearchBar, DotGrid(500곳), Moon(밤), MiniPhone, CrossLabel, StrikeAt
import React from "react";
import {useCurrentFrame} from "remotion";
import {C, SANS} from "../../design/tokens";
import {enter, prog} from "../../components/anim";
import {won} from "../../components/fmt";
import {Card, Label, Mark, Strike} from "../../components/ui";
import {F} from "./facts";

export const HATCH = "repeating-linear-gradient(135deg, transparent 0 12px, rgba(154,150,142,0.38) 12px 16px)";
export const GHOST = "rgba(45,108,223,0.16)"; // 잃은 부분 (파랑 점선 칸)
export const LIGHT_LOSS = "#9DB7EA"; // 비교 대상(작은 손실) 막대

// ── 사연 계좌 카드 — 영상 끝까지 같은 모양·같은 색 (S02 처음 등장) ──
// 막대: 잉크 = 몽고디비(한 종목), 빗금 = 현금. pnl은 만 원 단위
export const ACC_W = 960;
export const BAR_IN = ACC_W - 96; // 막대 바깥 폭 864
export const MyAccount: React.FC<{
  pnl: number | null;
  pnlNote?: React.ReactNode;
  stock?: number; // 0~1, 막대에서 종목이 차지하는 비율
  parts?: number; // 막대를 n칸으로 나눈 선
  head?: React.ReactNode; // "내 계좌" 오른쪽 (기본: 전 재산 7,000만 원)
  footL?: React.ReactNode;
  footR?: React.ReactNode;
  barOverlay?: React.ReactNode; // 막대 위에 겹치는 표시
  shakeX?: number;
  compact?: boolean;
  style?: React.CSSProperties;
}> = ({pnl, pnlNote, stock = 1, parts, head, footL, footR, barOverlay, shakeX = 0, compact, style}) => {
  const pnlColor = pnl === null || Math.round(pnl) === 0 ? C.ink : pnl < 0 ? C.loss : C.gain;
  return (
    <Card style={{width: ACC_W, boxSizing: "border-box", padding: "34px 48px 38px", transform: `translateX(${shakeX}px)`, ...style}}>
      <div style={{display: "flex", justifyContent: "space-between", alignItems: "center", height: 56}}>
        <Label size={40}>내 계좌</Label>
        {head ?? (
          <Label size={36} weight={500} color={C.gray}>
            전 재산 {won(F.all.v)}
          </Label>
        )}
      </div>
      {compact ? null : (
        <>
          <Label size={34} weight={500} color={C.gray} style={{marginTop: 12}}>
            평가손익
          </Label>
          <div style={{display: "flex", alignItems: "baseline", gap: 20, height: 172, paddingTop: 4}}>
            {/* 꼬리말("정도")이 있으면 "+1,000만 원 정도"가 카드 안에 들어가도록 조금 작게 */}
            <div style={{fontFamily: SANS, fontWeight: 900, fontSize: pnlNote ? 136 : 160, lineHeight: 1, letterSpacing: "-0.035em", color: pnlColor, whiteSpace: "nowrap"}}>
              {pnl === null ? "" : won(pnl, true)}
            </div>
            {pnlNote}
          </div>
        </>
      )}
      <div style={{position: "relative", marginTop: compact ? 26 : 12, width: BAR_IN, height: 56, border: `4px solid ${C.ink}`, borderRadius: 12, overflow: "hidden", background: HATCH, boxSizing: "border-box"}}>
        <div style={{position: "absolute", left: 0, top: 0, bottom: 0, width: `${Math.max(0, Math.min(1, stock)) * 100}%`, background: C.ink}} />
        {parts
          ? Array.from({length: parts - 1}).map((_, i) => (
              <div key={i} style={{position: "absolute", left: `${((i + 1) * 100) / parts}%`, top: 0, bottom: 0, width: 4, marginLeft: -2, background: C.light}} />
            ))
          : null}
        {barOverlay}
      </div>
      <div style={{display: "flex", justifyContent: "space-between", alignItems: "center", marginTop: 12, minHeight: 48}}>
        <Label size={36}>{footL}</Label>
        <Label size={36} weight={500} color={C.gray}>
          {footR}
        </Label>
      </div>
    </Card>
  );
};

/** 칩 모양 날짜·태그 (잉크 바탕) */
export const DateTag: React.FC<{children: React.ReactNode; style?: React.CSSProperties}> = ({children, style}) => (
  <div style={{background: C.ink, color: C.light, fontFamily: SANS, fontWeight: 700, fontSize: 34, lineHeight: 1.2, padding: "6px 20px", borderRadius: 8, whiteSpace: "nowrap", ...style}}>{children}</div>
);

/** 취소선 — at 전에는 글자만 그린다 */
export const StrikeAt: React.FC<{at: number; color?: string; children: React.ReactNode}> = ({at, color, children}) => {
  const f = useCurrentFrame();
  return f < at ? <span style={{display: "inline-block"}}>{children}</span> : <Strike at={at} color={color}>{children}</Strike>;
};

/** ✗ 표시 + 글자 한 줄 */
export const CrossLabel: React.FC<{at: number; children: React.ReactNode; size?: number; color?: string}> = ({at, children, size = 44, color}) => {
  const f = useCurrentFrame();
  return (
    <div style={{display: "flex", alignItems: "center", gap: 14, opacity: enter(f, at)}}>
      <Mark kind="cross" at={at} size={size + 8} color={color} />
      <Label size={size} color={color}>
        {children}
      </Label>
    </div>
  );
};

// ── 10×10 와플 (100칸 = 전체, n칸 색칠 — 소수면 마지막 칸을 그 비율만큼 아래에서 채움) ──
export const Waffle: React.FC<{x: number; y: number; cell?: number; gap?: number; n: number; at: number; fillAt: number; color?: string; dur?: number}> = ({
  x,
  y,
  cell = 36,
  gap = 6,
  n,
  at,
  fillAt,
  color = C.ink,
  dur = 24,
}) => {
  const f = useCurrentFrame();
  const o = enter(f, at);
  const shown = prog(f, fillAt, dur) * n;
  const cells = [];
  for (let i = 0; i < 100; i++) {
    const r = Math.floor(i / 10);
    const c = i % 10;
    const k = Math.max(0, Math.min(1, shown - i)); // 이 칸이 채워진 비율
    const on = i < Math.ceil(n - 1e-9);
    cells.push(
      <div
        key={i}
        style={{
          position: "absolute",
          left: x + c * (cell + gap),
          top: y + r * (cell + gap),
          width: cell,
          height: cell,
          borderRadius: 6,
          boxSizing: "border-box",
          border: `3px solid ${on && k > 0 ? color : "#C9C2B4"}`,
          background: k > 0 ? `linear-gradient(to top, ${color} ${k * 100}%, transparent ${k * 100}%)` : "transparent",
          opacity: o,
        }}
      />,
    );
  }
  return <>{cells}</>;
};
export const waffleSize = (cell = 36, gap = 6) => 10 * cell + 9 * gap;

// ── 작은 계좌 아이콘: 막대가 한 종목(잉크)으로 꽉 참 + 손익 표시(빨강/파랑) ──
export const MiniAccount: React.FC<{at: number; tone?: "ink" | "gain" | "loss"; w?: number; toneAt?: number; until?: number; drift?: number}> = ({at, tone = "ink", w = 120, toneAt, until, drift = 0}) => {
  const f = useCurrentFrame();
  const k = enter(f, at);
  const q = until === undefined ? 1 : 1 - prog(f, until, 14);
  const tk = toneAt === undefined ? 1 : prog(f, toneAt, 10);
  const pnl = tone === "gain" ? C.gain : tone === "loss" ? C.loss : C.gray;
  return (
    <div
      style={{
        width: w,
        height: w * 0.74,
        boxSizing: "border-box",
        border: `4px solid ${C.ink}`,
        borderRadius: 14,
        background: C.light,
        padding: "12px 14px",
        opacity: k * q,
        transform: `translate(${(1 - q) * drift}px, ${(1 - k) * 16}px)`,
        display: "flex",
        flexDirection: "column",
        gap: 8,
      }}
    >
      <div style={{width: "55%", height: 8, borderRadius: 4, background: C.ink}} />
      <div style={{width: "80%", height: 16, borderRadius: 4, background: pnl, opacity: tone === "ink" ? 0 : tk}} />
      <div style={{width: "100%", height: 14, borderRadius: 4, background: C.ink}} />
    </div>
  );
};

// ── 검색창 (돋보기는 선으로) ──
export const SearchBar: React.FC<{text: string; textP: number; w?: number}> = ({text, textP, w = 900}) => (
  <div style={{width: w, height: 120, boxSizing: "border-box", border: `5px solid ${C.ink}`, borderRadius: 60, background: C.light, display: "flex", alignItems: "center", gap: 26, padding: "0 44px"}}>
    <svg width={56} height={56} viewBox="0 0 56 56" style={{flex: "none"}}>
      <circle cx={23} cy={23} r={16} stroke={C.ink} strokeWidth={6} fill="none" />
      <path d="M 35 35 L 50 50" stroke={C.ink} strokeWidth={7} strokeLinecap="round" />
    </svg>
    <div style={{fontFamily: SANS, fontWeight: 700, fontSize: 52, color: C.ink, whiteSpace: "nowrap", clipPath: `inset(0 ${(1 - textP) * 100}% 0 0)`}}>{text}</div>
  </div>
);

// ── 종목 칸 한 줄 (10개 종목에 나눈 돈): 칸마다 아래에서 잉크로 채움. ghost[i]까지가 원래 높이 → 잃은 부분은 파랑 점선 ──
export type BoxCell = {fill: number; base?: number; color?: string; label?: React.ReactNode; dim?: number};
export const BoxRow: React.FC<{x: number; y: number; size?: number; gap?: number; cells: BoxCell[]; at: number; stagger?: number}> = ({x, y, size = 136, gap = 14, cells, at, stagger = 2}) => {
  const f = useCurrentFrame();
  return (
    <>
      {cells.map((c, i) => {
        const o = enter(f, at + i * stagger);
        const base = c.base ?? 1;
        const lost = Math.max(0, base - c.fill);
        const left = x + i * (size + gap);
        return (
          <React.Fragment key={i}>
            <div style={{position: "absolute", left, top: y, width: size, height: size, boxSizing: "border-box", border: `4px solid ${C.ink}`, borderRadius: 12, overflow: "hidden", background: C.light, opacity: o * (1 - (c.dim ?? 0) * 0.6)}}>
              <div style={{position: "absolute", left: 0, right: 0, bottom: 0, height: `${Math.max(0, c.fill) * 100}%`, background: c.color ?? C.ink}} />
              {lost > 0.002 ? (
                <div style={{position: "absolute", left: 4, right: 4, bottom: `${Math.max(0, c.fill) * 100}%`, height: `calc(${lost * 100}% - 4px)`, background: GHOST, border: `4px dashed ${C.loss}`, borderRadius: 6, boxSizing: "border-box"}} />
              ) : null}
            </div>
            {c.label ? (
              <div style={{position: "absolute", left: left - 20, width: size + 40, top: y + size + 12, textAlign: "center", opacity: o}}>
                {c.label}
              </div>
            ) : null}
          </React.Fragment>
        );
      })}
    </>
  );
};
export const boxRowW = (n: number, size = 136, gap = 14) => n * size + (n - 1) * gap;

// ── 계좌 비중 막대 (계좌 카드 막대와 같은 무늬, 크게): 조각 폭 = 비중 ──
export type WSeg = {v: number; color?: string; hatch?: boolean; ghost?: boolean};
export const WeightBar: React.FC<{x: number; y: number; w: number; h?: number; segs: WSeg[]; opacity?: number}> = ({x, y, w, h = 96, segs, opacity = 1}) => {
  const total = segs.reduce((a, s) => a + s.v, 0);
  let acc = 0;
  return (
    <div style={{position: "absolute", left: x, top: y, width: w, height: h, boxSizing: "border-box", border: `4px solid ${C.ink}`, borderRadius: 14, overflow: "hidden", background: C.light, opacity}}>
      {segs.map((s, i) => {
        const l = (acc / total) * (w - 8);
        const sw = (s.v / total) * (w - 8);
        acc += s.v;
        return (
          <div
            key={i}
            style={{
              position: "absolute",
              left: l,
              top: 0,
              bottom: 0,
              width: sw,
              background: s.ghost ? GHOST : s.hatch ? HATCH : s.color ?? C.ink,
              borderRight: i < segs.length - 1 ? `4px solid ${C.light}` : undefined,
              boxSizing: "border-box",
            }}
          />
        );
      })}
    </div>
  );
};

// ── 점 격자 (S&P 500 = 500곳): hot 칸은 크게·빨강 ──
export const DotGrid: React.FC<{x: number; y: number; cols: number; rows: number; d?: number; gap?: number; at: number; dur?: number; hot?: number[]; hotAt?: number}> = ({
  x,
  y,
  cols,
  rows,
  d = 14,
  gap = 8,
  at,
  dur = 24,
  hot = [],
  hotAt = 1e9,
}) => {
  const f = useCurrentFrame();
  const n = cols * rows;
  const shown = prog(f, at, dur) * n;
  const hp = prog(f, hotAt, 12);
  const hotSet = new Set(hot);
  const dots = [];
  for (let i = 0; i < n; i++) {
    if (i >= shown) break;
    const r = Math.floor(i / cols);
    const c = i % cols;
    const isHot = hotSet.has(i);
    const s = isHot ? 1 + 0.9 * hp : 1;
    dots.push(
      <div
        key={i}
        style={{
          position: "absolute",
          left: x + c * (d + gap) + (d - d * s) / 2,
          top: y + r * (d + gap) + (d - d * s) / 2,
          width: d * s,
          height: d * s,
          borderRadius: 99,
          background: isHot && hp > 0 ? C.gain : C.ink,
        }}
      />,
    );
  }
  return <>{dots}</>;
};

// ── 달 (밤) ──
export const Moon: React.FC<{size?: number; color?: string}> = ({size = 90, color = C.inkOnNavy}) => (
  <svg width={size} height={size} viewBox="0 0 100 100" style={{overflow: "visible"}}>
    <path d="M 62 8 A 44 44 0 1 0 92 66 A 36 36 0 1 1 62 8 Z" fill={color} />
  </svg>
);

// ── 작은 휴대폰 (계좌를 연 순간 — 화면이 켜지고 "내 계좌"와 계좌 카드와 같은 무늬의 막대) ──
export const MiniPhone: React.FC<{at: number; w?: number; dark?: boolean; children?: React.ReactNode}> = ({at, w = 190, dark, children}) => {
  const f = useCurrentFrame();
  const k = enter(f, at);
  const on = prog(f, at + 6, 8);
  return (
    <div
      style={{
        position: "relative",
        width: w,
        height: w * 1.55,
        boxSizing: "border-box",
        border: `8px solid ${dark ? C.inkOnNavy : C.ink}`,
        borderRadius: 30,
        background: on > 0 ? C.light : "#D9D2C4",
        padding: "40px 16px 0",
        opacity: k,
        transform: `translateY(${(1 - k) * 20}px)`,
      }}
    >
      <div style={{position: "absolute", top: 12, left: "50%", width: 54, height: 10, marginLeft: -27, borderRadius: 5, background: C.ink}} />
      <div style={{opacity: on}}>
        {children ?? (
          <>
            <Label size={30}>내 계좌</Label>
            <div style={{marginTop: 18, height: 34, borderRadius: 8, border: `4px solid ${C.ink}`, background: C.ink, boxSizing: "border-box"}} />
          </>
        )}
      </div>
    </div>
  );
};
