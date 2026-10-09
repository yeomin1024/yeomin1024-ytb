// 화면 위에 겹치는 요소 — 자막, 재구성 사연 캡션, 화면 고지 카드 (guides/video_guide.md 1-11, 2 "화면 고지 카드", 3-3)
import React from "react";
import {AbsoluteFill, useCurrentFrame} from "remotion";
import {Bg, C, M, SANS, SERIF, SIZE} from "../design/tokens";
import {enter, prog} from "./anim";
import {Card, Sub} from "./timeline";

/** 자막: 하단 중앙, 아래 72px, 최대 1500px, 46px 700. 자막 사이 빈 화면 없음 → 띠는 유지하고 글자만 4프레임 페이드 */
export const Subtitles: React.FC<{subs: Sub[]; bgAt: (frame: number) => Bg}> = ({subs, bgAt}) => {
  const f = useCurrentFrame();
  const i = subs.findIndex((s) => f >= s.from && f < s.to);
  if (i < 0) return null;
  const s = subs[i];
  const prev = subs[i - 1];
  const next = subs[i + 1];
  const joinedPrev = prev !== undefined && prev.to === s.from;
  const joinedNext = next !== undefined && next.from === s.to;
  const tIn = Math.min(1, (f - s.from + 1) / M.subFade);
  const tOut = Math.min(1, (s.to - f) / M.subFade);
  const textO = Math.min(tIn, tOut);
  const bandO = Math.min(joinedPrev ? 1 : tIn, joinedNext ? 1 : tOut);
  const bg = bgAt(f);
  const band = bg === "navy" ? "rgba(20,33,61,0.85)" : bg === "light" ? "rgba(250,246,238,0.92)" : "rgba(242,235,221,0.92)";
  const color = bg === "navy" ? C.inkOnNavy : C.ink;
  return (
    <AbsoluteFill style={{justifyContent: "flex-end", alignItems: "center", paddingBottom: 72, pointerEvents: "none"}}>
      <div
        style={{
          maxWidth: 1500,
          padding: "14px 40px",
          borderRadius: 12,
          background: band,
          opacity: bandO,
          fontFamily: SANS,
          fontWeight: 700,
          fontSize: SIZE.subtitle,
          lineHeight: 1.4,
          color,
          textAlign: "center",
        }}
      >
        <div style={{opacity: textO}}>
          {s.lines.map((l, k) => (
            <div key={k} style={{whiteSpace: "nowrap"}}>
              {l}
            </div>
          ))}
        </div>
      </div>
    </AbsoluteFill>
  );
};

/** 재구성 사연 캡션: 사연 파트 동안 왼쪽 위, 28px 웜 그레이 */
export const ReconCaption: React.FC<{text: string; from: number; to: number}> = ({text, from, to}) => {
  const f = useCurrentFrame();
  if (f < from || f >= to) return null;
  const o = Math.min(prog(f, from, 8), 1 - prog(f, to - 8, 8));
  return (
    <div style={{position: "absolute", left: SIZE.margin, top: 48, fontFamily: SANS, fontWeight: 500, fontSize: SIZE.min, color: C.gray, opacity: o}}>{text}</div>
  );
};

/** 화면 고지 카드 (노랑 띠): TXT [장면] 문구 그대로, 한 줄씩 순서대로 */
export const DisclaimerCard: React.FC<{card: Card}> = ({card}) => {
  const f = useCurrentFrame(); // Sequence 안: 0부터
  const len = card.to - card.from;
  const step = Math.min(30, Math.floor((len * 0.45) / Math.max(1, card.lines.length)));
  const out = 1 - prog(f, len - 10, 10);
  return (
    <AbsoluteFill style={{background: C.cream, fontFamily: SANS, color: C.ink, opacity: out}}>
      <div style={{position: "absolute", left: 0, right: 0, top: 150, height: 150, background: C.yellow, transform: `scaleX(${prog(f, 0, 14)})`, transformOrigin: "0% 50%"}} />
      <div style={{position: "absolute", left: 0, right: 0, top: 150, height: 150, display: "flex", alignItems: "center", justifyContent: "center", fontFamily: SERIF, fontWeight: 900, fontSize: 80, opacity: enter(f, 8)}}>
        {card.title}
      </div>
      <div style={{position: "absolute", left: 200, right: 200, top: 380, display: "flex", flexDirection: "column", gap: 30}}>
        {card.lines.map((l, i) => {
          const p = enter(f, 16 + i * step);
          return (
            <div key={i} style={{fontWeight: 700, fontSize: 44, lineHeight: 1.4, opacity: p, transform: `translateY(${(1 - p) * 18}px)`}}>
              {l}
            </div>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};
