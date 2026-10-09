// 카드형 컴포넌트 — 계좌 카드, 금액 막대, 뉴스 카드, 생각 말풍선, 번호 타이틀, 메모 카드 (guides/video_guide.md 3-5)
import React from "react";
import {useCurrentFrame} from "remotion";
import {C, SANS, SERIF} from "../design/tokens";
import {won} from "./fmt";
import {Card, Chip, Label, popIn, useBg, vis} from "./ui";

// ── 금액 막대: 한 종목에 들어간 돈(조각들) + 남은 현금 ──
export type Seg = {v: number; color?: string; label?: string};
export const AmountBar: React.FC<{segs: Seg[]; total: number; width: number; height?: number; cashLabel?: boolean}> = ({segs, total, width, height = 56, cashLabel = true}) => {
  let acc = 0;
  return (
    <div style={{position: "relative", width, height, border: `4px solid ${C.ink}`, borderRadius: 12, overflow: "hidden", background: cashLabel ? "repeating-linear-gradient(135deg, transparent 0 12px, rgba(154,150,142,0.25) 12px 16px)" : C.light}}>
      {segs.map((s, i) => {
        const left = (acc / total) * width;
        const w = (Math.max(0, s.v) / total) * width;
        acc += Math.max(0, s.v);
        return <div key={i} style={{position: "absolute", left, top: 0, bottom: 0, width: w, background: s.color ?? C.ink, borderRight: w > 2 ? `3px solid ${C.light}` : undefined}} />;
      })}
    </div>
  );
};

// ── 계좌 카드 (사연 주인공) — 영상 끝까지 같은 모양으로 재사용 ──
export const AccountCard: React.FC<{
  total: number; // 모은 돈 (만 원)
  segs: Seg[]; // 종목에 들어간 돈 조각
  stockName: string;
  pnl: number | null; // 평가손익 (만 원, 애니메이션 값)
  pnlNote?: React.ReactNode; // 평가손익 옆 표시 (예: ▼)
  pnlDim?: number; // 0~1, 1이면 흐리게
  shakeX?: number;
  compact?: boolean; // 평가손익 줄 없이 (돈이 얼마나 걸렸는지만 볼 때)
  style?: React.CSSProperties;
}> = ({total, segs, stockName, pnl, pnlNote, pnlDim = 0, shakeX = 0, compact = false, style}) => {
  const invested = segs.reduce((a, s) => a + s.v, 0);
  const cash = total - invested;
  const pnlColor = pnl === null || Math.round(pnl) === 0 ? C.ink : pnl < 0 ? C.loss : C.gain;
  return (
    <Card style={{width: 1040, padding: "36px 48px 40px", transform: `translateX(${shakeX}px)`, ...style}}>
      <div style={{display: "flex", justifyContent: "space-between", alignItems: "baseline"}}>
        <Label size={40}>내 계좌</Label>
        <Label size={36} weight={500} color={C.gray}>
          모은 돈 {won(total)}
        </Label>
      </div>
      {compact ? null : (
        <>
          <Label size={34} weight={500} color={C.gray} style={{marginTop: 18}}>
            평가손익
          </Label>
          <div style={{display: "flex", alignItems: "center", gap: 28, height: 176}}>
            <div style={{fontFamily: SANS, fontWeight: 900, fontSize: 164, lineHeight: 1, letterSpacing: "-0.035em", color: pnlColor, opacity: 1 - 0.7 * pnlDim, whiteSpace: "nowrap"}}>
              {pnl === null ? "" : won(pnl)}
            </div>
            {pnlNote}
          </div>
        </>
      )}
      <div style={{marginTop: compact ? 28 : 14}}>
        <AmountBar segs={segs} total={total} width={936} />
      </div>
      <div style={{display: "flex", justifyContent: "space-between", marginTop: 14}}>
        <Label size={36}>
          {stockName} {won(invested)}
        </Label>
        <Label size={36} weight={500} color={C.gray}>
          현금 {won(cash)}
        </Label>
      </div>
    </Card>
  );
};

// ── 뉴스·사건 헤드라인 카드 ──
export const NewsCard: React.FC<{date?: string; title: React.ReactNode; sub?: React.ReactNode; width?: number; children?: React.ReactNode; style?: React.CSSProperties}> = ({
  date,
  title,
  sub,
  width = 760,
  children,
  style,
}) => (
  <Card style={{width, ...style}}>
    {date ? (
      <div style={{display: "inline-block", background: C.ink, color: C.light, fontWeight: 700, fontSize: 32, padding: "6px 20px", borderRadius: 8, marginBottom: 18}}>{date}</div>
    ) : null}
    <div style={{fontFamily: SANS, fontWeight: 900, fontSize: 56, lineHeight: 1.22}}>{title}</div>
    {sub ? <div style={{fontFamily: SANS, fontWeight: 500, fontSize: 36, lineHeight: 1.35, color: "#55524C", marginTop: 12}}>{sub}</div> : null}
    {children}
  </Card>
);

// ── 생각 말풍선: 생각 하나에 말풍선 하나 ──
export const Bubble: React.FC<{at: number; until?: number; children: React.ReactNode; size?: number; tail?: "left" | "right"; style?: React.CSSProperties}> = ({
  at,
  until,
  children,
  size = 46,
  tail = "left",
  style,
}) => {
  const f = useCurrentFrame();
  const dots = tail === "left" ? {left: 60} : {right: 60};
  return (
    <div style={{position: "relative", display: "inline-block", ...popIn(f, at, until), transformOrigin: tail === "left" ? "10% 100%" : "90% 100%", ...style}}>
      <div style={{background: C.light, color: C.ink, border: `4px solid ${C.ink}`, borderRadius: 64, padding: "30px 50px", fontFamily: SANS, fontWeight: 700, fontSize: size, lineHeight: 1.3, textAlign: "center"}}>
        {children}
      </div>
      <div style={{position: "absolute", bottom: -34, width: 30, height: 30, borderRadius: 99, background: C.light, border: `4px solid ${C.ink}`, ...dots}} />
      <div style={{position: "absolute", bottom: -62, width: 16, height: 16, borderRadius: 99, background: C.light, border: `4px solid ${C.ink}`, ...(tail === "left" ? {left: 34} : {right: 34})}} />
    </div>
  );
};

// ── 번호 타이틀 ("01", "첫째") — 같은 목록은 같은 디자인, 화면 위쪽 머리글 ──
export const NumberTitle: React.FC<{no: string; title: React.ReactNode; at: number}> = ({no, title, at}) => {
  const f = useCurrentFrame();
  const bg = useBg();
  const boxBg = bg === "navy" ? C.inkOnNavy : C.ink;
  const boxFg = bg === "navy" ? C.navy : C.light;
  return (
    <div style={{position: "absolute", left: 96, top: 120, display: "flex", alignItems: "center", gap: 32, ...vis(f, at)}}>
      <div style={{minWidth: 128, height: 112, padding: "0 22px", borderRadius: 18, background: boxBg, color: boxFg, fontFamily: SERIF, fontWeight: 900, fontSize: 64, display: "flex", alignItems: "center", justifyContent: "center"}}>
        {no}
      </div>
      <div style={{fontFamily: SERIF, fontWeight: 900, fontSize: 72, lineHeight: 1.15, whiteSpace: "nowrap"}}>{title}</div>
    </div>
  );
};

// ── 메모 카드 ("산 이유 한 줄") ──
export const Note: React.FC<{head: string; text: React.ReactNode; textP?: number; width?: number; children?: React.ReactNode; style?: React.CSSProperties}> = ({head, text, textP = 1, width = 760, children, style}) => (
  <Card style={{width, background: "#FFFDF6", ...style}}>
    <Label size={34} weight={500} color={C.gray}>
      {head}
    </Label>
    <div style={{marginTop: 14, borderBottom: `3px dashed ${C.gray}`, paddingBottom: 12, minHeight: 74, fontFamily: SANS, fontWeight: 900, fontSize: 52, lineHeight: 1.3, clipPath: `inset(0 ${(1 - textP) * 100}% 0 0)`}}>{text}</div>
    {children}
  </Card>
);

// 칩 재노출 (장면 파일에서 한 번에 가져다 쓰도록)
export {Chip};
