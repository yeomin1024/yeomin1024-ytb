// bittu-2026-10 전용 시각 요소 (공통 컴포넌트는 고치지 않음)
// - ValueBar / LeverageCard: 사연 계좌 카드 = 주식 평가액 막대가 "내 돈(잉크) + 수익(빨강) / 잃은 내 돈(파랑 점선) + 빌린 돈(빗금)"으로 나뉜다
//   → 빚은 주가와 상관없이 그대로이고, 오르내림은 내 돈 칸에서만 일어난다는 것을 한눈에 (같은 사연은 영상 끝까지 같은 카드)
// - DayStrip: 날짜 칸 (담보 부족 문자 → 반대매매 → 다음 날 반등)
// - Gauge: 담보 비율 막대 (주식 가치 vs 빌린 돈, 140% 선) — 개념도
import React from "react";
import {useCurrentFrame} from "remotion";
import {C, SANS} from "../../design/tokens";
import {enter} from "../../components/anim";
import {won} from "../../components/fmt";
import {Card, Label, Mark, useFg, vis} from "../../components/ui";
import {F} from "./facts";

/** 빌린 돈 칸 (빗금 회색) — 계좌 카드·담보 막대·예시 막대에서 같은 무늬 */
export const DEBT_FILL = "repeating-linear-gradient(135deg, #8E887D 0 10px, #C9C4BA 10px 20px)";
/** 잃은 내 돈 (파랑 점선 칸) */
export const GHOST_FILL = "rgba(45,108,223,0.14)";
export const BAR_W = 936;
export const MAX_VALUE = F.peakValue.v; // 7,500만 원 = 막대 전체 길이

export type Tone = "loss" | "gain" | "ink" | "gray";
export const toneColor = (t: Tone = "ink") => (t === "loss" ? C.loss : t === "gain" ? C.gain : t === "gray" ? C.gray : C.ink);

// ── 주식 평가액 막대 ──
export const ValueBar: React.FC<{own: number; debt: number; base?: number; width?: number; max?: number; height?: number; ghost?: boolean}> = ({
  own,
  debt,
  base = F.own.v,
  width = BAR_W,
  max = MAX_VALUE,
  height = 60,
  ghost = true,
}) => {
  const k = width / max;
  const o = Math.max(0, own);
  const parts: {w: number; style: React.CSSProperties}[] = [
    {w: Math.min(o, base) * k, style: {background: C.ink, border: `4px solid ${C.ink}`}},
    {w: Math.max(0, o - base) * k, style: {background: C.gain, border: `4px solid ${C.ink}`}},
    {w: ghost ? Math.max(0, base - o) * k : 0, style: {background: GHOST_FILL, border: `4px dashed ${C.loss}`}},
    {w: Math.max(0, debt) * k, style: {background: DEBT_FILL, border: `4px solid ${C.ink}`}},
  ];
  return (
    <div style={{display: "flex", gap: 4, height}}>
      {parts.map((p, i) => (p.w < 1 ? null : <div key={i} style={{width: p.w, height, boxSizing: "border-box", borderRadius: 8, flex: "none", ...p.style}} />))}
    </div>
  );
};

/** 범례 네모 (내 돈 = 잉크, 빌린 돈 = 빗금) */
export const Swatch: React.FC<{kind: "own" | "debt" | "ghost" | "gain"; size?: number}> = ({kind, size = 28}) => (
  <span
    style={{
      display: "inline-block",
      width: size,
      height: size,
      borderRadius: 6,
      boxSizing: "border-box",
      verticalAlign: "-0.12em",
      marginRight: 12,
      background: kind === "own" ? C.ink : kind === "debt" ? DEBT_FILL : kind === "gain" ? C.gain : GHOST_FILL,
      border: kind === "ghost" ? `3px dashed ${C.loss}` : `3px solid ${C.ink}`,
    }}
  />
);

// ── 사연 계좌 카드 (S02·S03·S05·S21·S24·S27에서 같은 모양) ──
export const LeverageCard: React.FC<{
  own: number; // 지금 내 돈 (만 원, 평가액 - 빌린 돈)
  debt: number; // 빌린 돈 (만 원)
  base?: number; // 처음 넣은 내 돈
  pnl: number | null; // 평가손익 (만 원)
  pnlNote?: React.ReactNode;
  pnlSlot?: React.ReactNode; // 평가손익 숫자 대신 넣을 것 (예: 강제 매도 도장)
  header?: React.ReactNode; // 오른쪽 위 (기본: 주식 ○○만 원어치)
  ownLabel?: React.ReactNode;
  debtLabel?: React.ReactNode;
  compact?: boolean;
  pnlOpen?: number; // 0~1: 평가손익 줄이 열리는 정도 (산 뒤에 열림)
  shakeX?: number;
  style?: React.CSSProperties;
  children?: React.ReactNode;
}> = ({own, debt, base = F.own.v, pnl, pnlNote, pnlSlot, header, ownLabel, debtLabel, compact = false, pnlOpen = 1, shakeX = 0, style, children}) => {
  const pnlColor = pnl === null || Math.round(pnl) === 0 ? C.ink : pnl < 0 ? C.loss : C.gain;
  const value = Math.max(0, own) + debt;
  return (
    <Card style={{width: 1040, boxSizing: "border-box", padding: "32px 48px 36px", position: "relative", transform: `translateX(${shakeX}px)`, ...style}}>
      <div style={{display: "flex", justifyContent: "space-between", alignItems: "baseline"}}>
        <Label size={40}>내 계좌</Label>
        <Label size={36} weight={500} color={C.gray}>
          {header === undefined ? `주식 ${won(value)}어치` : header}
        </Label>
      </div>
      {compact ? null : (
        <div style={{height: 228 * pnlOpen, overflow: "hidden", opacity: pnlOpen}}>
          <Label size={34} weight={500} color={C.gray} style={{marginTop: 12}}>
            평가손익
          </Label>
          <div style={{display: "flex", alignItems: "center", gap: 24, height: 172}}>
            {pnlSlot ?? (
              <div style={{fontFamily: SANS, fontWeight: 900, fontSize: 164, lineHeight: 1, letterSpacing: "-0.035em", color: pnlColor, whiteSpace: "nowrap"}}>
                {pnl === null ? "" : won(pnl, true)}
              </div>
            )}
            {pnlNote}
          </div>
        </div>
      )}
      <div style={{marginTop: compact ? 26 : 26 - 16 * pnlOpen}}>
        <ValueBar own={own} debt={debt} base={base} />
      </div>
      <div style={{display: "flex", justifyContent: "space-between", marginTop: 16}}>
        <Label size={36}>
          <Swatch kind="own" />
          {ownLabel ?? `내 돈 ${won(base)}`}
        </Label>
        <Label size={36} weight={500}>
          {debt > 0.5 || debtLabel ? <Swatch kind="debt" /> : null}
          {debtLabel ?? (debt > 0.5 ? `빌린 돈 ${won(debt)}` : "")}
        </Label>
      </div>
      {children}
    </Card>
  );
};

// ── 날짜 칸 ──
export type DayLine = {text: React.ReactNode; at: number; tone?: Tone; mark?: "check" | "cross"; until?: number};
export type Day = {date: React.ReactNode; at: number; lines?: DayLine[]; until?: number; hi?: boolean};
export const DayStrip: React.FC<{x: number; y: number; days: Day[]; boxW: number; h?: number; gap?: number; size?: number}> = ({x, y, days, boxW, h = 270, gap = 28, size = 42}) => {
  const f = useCurrentFrame();
  return (
    <>
      {days.map((d, i) => (
        <div key={i} style={{position: "absolute", left: x + i * (boxW + gap), top: y, ...vis(f, d.at, d.until)}}>
          <Card style={{width: boxW, height: h, boxSizing: "border-box", padding: "24px 26px"}}>
            <div style={{display: "inline-block", background: C.ink, color: C.light, fontFamily: SANS, fontWeight: 700, fontSize: 34, padding: "6px 18px", borderRadius: 8, whiteSpace: "nowrap"}}>{d.date}</div>
            <div style={{marginTop: 18, display: "flex", flexDirection: "column", gap: 8}}>
              {(d.lines ?? []).map((l, k) => (
                <div key={k} style={{display: "flex", alignItems: "center", gap: 10, ...vis(f, l.at, l.until, 14)}}>
                  {l.mark ? <Mark kind={l.mark} at={l.at} size={42} color={toneColor(l.tone)} /> : null}
                  <Label size={size} weight={900} color={toneColor(l.tone)} style={{whiteSpace: "nowrap"}}>
                    {l.text}
                  </Label>
                </div>
              ))}
            </div>
          </Card>
        </div>
      ))}
    </>
  );
};

// ── 담보 비율 막대 (개념도): 위 = 주식 가치(비율만큼), 아래 = 빌린 돈(100%), 점선 = 140% ──
export const Gauge: React.FC<{x: number; y: number; U: number; ratio: number; at: number; lineAt: number; lineLabel?: React.ReactNode; dim?: number}> = ({
  x,
  y,
  U,
  ratio,
  at,
  lineAt,
  lineLabel,
  dim = 0,
}) => {
  const f = useCurrentFrame();
  const fg = useFg();
  const x0 = x + 250;
  const H = 76;
  const gapY = 118;
  const below = ratio < F.keep.v / 100;
  const o = enter(f, at);
  const lineX = x0 + (U * F.keep.v) / 100;
  return (
    <>
      <div style={{position: "absolute", left: x, top: y + 12, opacity: o}}>
        <Label size={40}>주식 가치</Label>
      </div>
      <div style={{position: "absolute", left: x, top: y + gapY + 12, opacity: o}}>
        <Label size={40}>빌린 돈</Label>
      </div>
      <div style={{position: "absolute", left: x0, top: y, width: Math.max(0, U * ratio * o), height: H, borderRadius: 8, background: below ? C.loss : C.ink, opacity: 1 - 0.5 * dim}} />
      <div style={{position: "absolute", left: x0, top: y + gapY, width: U * o, height: H, borderRadius: 8, boxSizing: "border-box", background: DEBT_FILL, border: `4px solid ${C.ink}`}} />
      <div style={{position: "absolute", left: lineX - 3, top: y - 44, height: gapY + H + 64, borderLeft: `6px dashed ${fg}`, opacity: enter(f, lineAt)}} />
      <div style={{position: "absolute", left: lineX, top: y - 52, transform: "translate(-50%, -100%)", opacity: enter(f, lineAt), whiteSpace: "nowrap"}}>
        {lineLabel ?? (
          <Label size={48} weight={900}>
            {F.keep.v}%
          </Label>
        )}
      </div>
    </>
  );
};
