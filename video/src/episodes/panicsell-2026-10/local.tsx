// panicsell-2026-10 전용 시각 요소 — 사연 계좌 카드, 일시정지 표시(서킷브레이커), 공포 게이지, 10×10 와플, 점 한 줄,
// 날짜 칸·달력, 주식|채권 나눔 막대, 과녁, 자물쇠, 작은 계좌 아이콘 (guides/video_guide.md 3-5, 맞는 패턴이 없을 때 단순 도형)
import React from "react";
import {useCurrentFrame} from "remotion";
import {C, SANS, SERIF} from "../../design/tokens";
import {enter, prog} from "../../components/anim";
import {won} from "../../components/fmt";
import {Card, Label, Mark, Strike, useFg} from "../../components/ui";

export const HATCH = "repeating-linear-gradient(135deg, transparent 0 12px, rgba(154,150,142,0.38) 12px 16px)";
export const LIGHT_GAIN = "#F2A59E"; // 비교 대상(작은 수익) 막대
export const LIGHT_LOSS = "#9DB7EA"; // 비교 대상(작은 손실) 막대

// ── 사연 계좌 카드 — 영상 끝까지 같은 모양·같은 색 (S02 처음 등장) ──
// 막대: 잉크 = 삼성전자, 빗금 = 현금. pnl은 만 원 단위
export const ACC_W = 960;
const BAR_W = ACC_W - 96;
export const MyAccount: React.FC<{
  pnl: number | null;
  pnlNote?: React.ReactNode;
  stock?: number; // 0~1, 막대의 삼성전자 비율
  parts?: number; // 막대를 n칸으로 나눈 선 (3 = 3분의 1씩, 4 = 4분의 1씩)
  head?: React.ReactNode; // "내 계좌" 오른쪽 (날짜 칩)
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
        {head}
      </div>
      {compact ? null : (
        <>
          <Label size={34} weight={500} color={C.gray} style={{marginTop: 12}}>
            평가손익
          </Label>
          <div style={{display: "flex", alignItems: "baseline", gap: 20, height: 172, paddingTop: 4}}>
            <div style={{fontFamily: SANS, fontWeight: 900, fontSize: 160, lineHeight: 1, letterSpacing: "-0.035em", color: pnlColor, whiteSpace: "nowrap"}}>
              {pnl === null ? "" : won(pnl, true)}
            </div>
            {pnlNote}
          </div>
        </>
      )}
      <div style={{position: "relative", marginTop: compact ? 26 : 12, width: BAR_W, height: 56, border: `4px solid ${C.ink}`, borderRadius: 12, overflow: "hidden", background: HATCH, boxSizing: "border-box"}}>
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

/** 계좌 카드 머리의 날짜 칩 (잉크 바탕) */
export const DateTag: React.FC<{children: React.ReactNode; style?: React.CSSProperties}> = ({children, style}) => (
  <div style={{background: C.ink, color: C.light, fontFamily: SANS, fontWeight: 700, fontSize: 34, lineHeight: 1.2, padding: "6px 20px", borderRadius: 8, whiteSpace: "nowrap", ...style}}>{children}</div>
);

// ── 일시정지 표시 (서킷브레이커 = 거래 멈춤) ──
export const PauseIcon: React.FC<{size?: number; color?: string}> = ({size = 120, color}) => {
  const fg = useFg();
  const c = color ?? fg;
  return (
    <div style={{width: size, height: size, borderRadius: size, border: `${Math.round(size * 0.07)}px solid ${c}`, display: "flex", alignItems: "center", justifyContent: "center", gap: size * 0.14, boxSizing: "border-box", flex: "none"}}>
      <div style={{width: size * 0.13, height: size * 0.42, background: c, borderRadius: 4}} />
      <div style={{width: size * 0.13, height: size * 0.42, background: c, borderRadius: 4}} />
    </div>
  );
};

// ── 공포 게이지 (반원, 개념도): p = 0~1 바늘 위치 ──
export const Gauge: React.FC<{cx: number; cy: number; r: number; at: number; p: number}> = ({cx, cy, r, at, p}) => {
  const f = useCurrentFrame();
  const fg = useFg();
  const draw = prog(f, at, 20);
  const needle = prog(f, at + 10, 22) * p;
  const L = Math.PI * r;
  const ang = Math.PI * (1 - needle); // 왼쪽(π) → 오른쪽(0)
  const nx = cx + Math.cos(ang) * (r - 60);
  const ny = cy - Math.sin(ang) * (r - 60);
  const fillL = L * needle;
  return (
    <svg width={1920} height={1080} style={{position: "absolute", left: 0, top: 0, overflow: "visible"}}>
      <path d={`M ${cx - r} ${cy} A ${r} ${r} 0 0 1 ${cx + r} ${cy}`} stroke="#D9D2C4" strokeWidth={34} fill="none" strokeLinecap="round" strokeDasharray={L} strokeDashoffset={L * (1 - draw)} />
      <path d={`M ${cx - r} ${cy} A ${r} ${r} 0 0 1 ${cx + r} ${cy}`} stroke={fg} strokeWidth={34} fill="none" strokeLinecap="round" strokeDasharray={`${fillL} ${L}`} opacity={draw > 0.9 ? 1 : 0} />
      <line x1={cx} y1={cy} x2={nx} y2={ny} stroke={fg} strokeWidth={10} strokeLinecap="round" opacity={enter(f, at + 10)} />
      <circle cx={cx} cy={cy} r={18 * enter(f, at + 10)} fill={fg} />
    </svg>
  );
};

// ── 10×10 와플 (100칸 = 전체, n칸 색칠) ──
export const Waffle: React.FC<{x: number; y: number; cell?: number; gap?: number; n: number; at: number; fillAt: number; color?: string}> = ({x, y, cell = 40, gap = 7, n, at, fillAt, color = C.ink}) => {
  const f = useCurrentFrame();
  const o = enter(f, at);
  const shown = Math.round(prog(f, fillAt, 24) * n);
  const cells = [];
  for (let i = 0; i < 100; i++) {
    const r = Math.floor(i / 10);
    const c = i % 10;
    const on = i < shown;
    cells.push(
      <div
        key={i}
        style={{position: "absolute", left: x + c * (cell + gap), top: y + r * (cell + gap), width: cell, height: cell, borderRadius: 6, boxSizing: "border-box", border: `3px solid ${on ? color : "#C9C2B4"}`, background: on ? color : "transparent", opacity: o}}
      />,
    );
  }
  return <>{cells}</>;
};

// ── 점 한 줄 (10일 = 10개, k개 강조) ──
export const DotRow: React.FC<{x: number; y: number; n?: number; d?: number; gap?: number; at: number; hiAt: number; k: number; color: string}> = ({x, y, n = 10, d = 96, gap = 34, at, hiAt, k, color}) => {
  const f = useCurrentFrame();
  const h = prog(f, hiAt, 14);
  return (
    <>
      {Array.from({length: n}).map((_, i) => {
        const o = enter(f, at + i * 3);
        const hot = i < k;
        const bg = hot ? color : h > 0 ? `rgba(154,150,142,${0.35 + 0.65 * (1 - h)})` : color;
        const col = hot ? color : h > 0.5 ? "#C9C2B4" : color;
        return (
          <div
            key={i}
            style={{position: "absolute", left: x + i * (d + gap), top: y, width: d, height: d, borderRadius: d, background: hot ? bg : h > 0.5 ? "transparent" : bg, border: `5px solid ${col}`, boxSizing: "border-box", opacity: o, transform: `scale(${0.7 + 0.3 * o})`}}
          />
        );
      })}
    </>
  );
};

// ── 날짜 칸 (달력 한 칸: 위 띠 + 날짜 + 아래 내용) ──
export const DayTile: React.FC<{w?: number; h?: number; top: React.ReactNode; date: React.ReactNode; tone?: "ink" | "loss"; children?: React.ReactNode; style?: React.CSSProperties}> = ({w = 300, h = 250, top, date, tone = "ink", children, style}) => {
  const band = tone === "loss" ? C.loss : C.ink;
  return (
    <div style={{width: w, height: h, boxSizing: "border-box", background: C.light, color: C.ink, border: `4px solid ${band}`, borderRadius: 18, overflow: "hidden", display: "flex", flexDirection: "column", ...style}}>
      <div style={{background: band, color: "#FFFFFF", fontFamily: SANS, fontWeight: 700, fontSize: 34, textAlign: "center", padding: "6px 0"}}>{top}</div>
      <div style={{flex: 1, display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", gap: 10}}>
        <div style={{fontFamily: SANS, fontWeight: 900, fontSize: 52, lineHeight: 1.1, whiteSpace: "nowrap"}}>{date}</div>
        {children}
      </div>
    </div>
  );
};

// ── 한 달 달력 (일~토). ring = 동그라미 칠 날, mark = 색 칸 ──
const DOW = ["일", "월", "화", "수", "목", "금", "토"];
export const MonthCal: React.FC<{
  x: number;
  y: number;
  title: string;
  firstDow: number; // 1일의 요일 (0 = 일요일)
  days: number;
  cell?: number;
  at: number;
  ring?: {day: number; at: number}[];
  mark?: {day: number; at: number; color: string}[];
}> = ({x, y, title, firstDow, days, cell = 60, at, ring = [], mark = []}) => {
  const f = useCurrentFrame();
  const o = enter(f, at);
  const rowH = cell * 0.8;
  const w = cell * 7;
  const pos = (d: number) => {
    const i = firstDow + d - 1;
    return {cx: (i % 7) * cell + cell / 2, cy: 52 + 40 + Math.floor(i / 7) * rowH + rowH / 2};
  };
  return (
    <div style={{position: "absolute", left: x, top: y, width: w + 36, padding: "18px 18px 14px", boxSizing: "content-box", background: C.light, border: `4px solid ${C.ink}`, borderRadius: 18, color: C.ink, opacity: o, transform: `translateY(${(1 - o) * 20}px)`}}>
      <div style={{position: "relative", width: w, height: 52 + 40 + rowH * Math.ceil((firstDow + days) / 7)}}>
        <div style={{fontFamily: SERIF, fontWeight: 900, fontSize: 44, lineHeight: "52px", textAlign: "center"}}>{title}</div>
        {DOW.map((d, i) => (
          <div key={d} style={{position: "absolute", left: i * cell, top: 52, width: cell, height: 40, textAlign: "center", fontFamily: SANS, fontWeight: 700, fontSize: 28, lineHeight: "40px", color: i === 5 ? C.ink : C.gray}}>
            {d}
          </div>
        ))}
        {mark.map((m) => {
          const p = pos(m.day);
          const k = enter(f, m.at);
          return <div key={`m${m.day}`} style={{position: "absolute", left: p.cx - cell / 2 + 3, top: p.cy - rowH / 2 + 2, width: cell - 6, height: rowH - 4, borderRadius: 10, background: m.color, opacity: k}} />;
        })}
        {Array.from({length: days}).map((_, i) => {
          const d = i + 1;
          const p = pos(d);
          const marked = mark.some((m) => m.day === d && f >= m.at);
          return (
            <div key={d} style={{position: "absolute", left: p.cx - cell / 2, top: p.cy - rowH / 2, width: cell, height: rowH, textAlign: "center", lineHeight: `${rowH}px`, fontFamily: SANS, fontWeight: 700, fontSize: 28, color: marked ? "#FFFFFF" : C.ink}}>
              {d}
            </div>
          );
        })}
        <svg width={w} height={52 + 40 + rowH * 6} style={{position: "absolute", left: 0, top: 0, overflow: "visible"}}>
          {ring.map((r) => {
            const p = pos(r.day);
            const R = rowH * 0.62;
            const L = 2 * Math.PI * R;
            const k = prog(f, r.at, 14);
            return <circle key={`r${r.day}`} cx={p.cx} cy={p.cy} r={R} stroke={C.ink} strokeWidth={5} fill="none" strokeDasharray={L} strokeDashoffset={L * (1 - k)} transform={`rotate(-90 ${p.cx} ${p.cy})`} />;
          })}
        </svg>
      </div>
    </div>
  );
};

// ── 주식 | 채권 나눔 막대 ──
export const SplitBar: React.FC<{w: number; h?: number; share: number; at: number; labels?: boolean}> = ({w, h = 80, share, at, labels = true}) => {
  const f = useCurrentFrame();
  const o = enter(f, at);
  const sw = w * share;
  const txt: React.CSSProperties = {position: "absolute", top: 0, height: h - 8, display: "flex", alignItems: "center", fontFamily: SANS, fontWeight: 700, fontSize: 34, whiteSpace: "nowrap"};
  return (
    <div style={{position: "relative", width: w, height: h, border: `4px solid ${C.ink}`, borderRadius: 12, overflow: "hidden", background: "#D9D2C4", boxSizing: "border-box", opacity: o}}>
      <div style={{position: "absolute", left: 0, top: 0, bottom: 0, width: sw, background: C.ink}} />
      {labels ? (
        <>
          <div style={{...txt, left: 20, color: C.light, opacity: sw > 140 ? 1 : 0}}>주식</div>
          <div style={{...txt, right: 20, color: C.ink, opacity: w - sw > 140 ? 1 : 0}}>채권</div>
        </>
      ) : null}
    </div>
  );
};

// ── 과녁 (맞혀야 하는 날) ──
export const Target: React.FC<{size?: number; at: number}> = ({size = 170, at}) => {
  const f = useCurrentFrame();
  const k = enter(f, at);
  const r = size / 2;
  return (
    <svg width={size} height={size} style={{overflow: "visible", opacity: k, transform: `scale(${0.8 + 0.2 * k})`}}>
      {[1, 0.68, 0.36].map((s, i) => (
        <circle key={i} cx={r} cy={r} r={(r - 4) * s} fill={i === 1 ? C.light : i === 0 ? "#E5DED0" : C.ink} stroke={C.ink} strokeWidth={5} />
      ))}
    </svg>
  );
};

// ── 자물쇠 (돈이 묶임) ──
export const Lock: React.FC<{size?: number; at: number; color?: string}> = ({size = 90, at, color = C.ink}) => {
  const f = useCurrentFrame();
  const k = enter(f, at);
  return (
    <svg width={size} height={size * 1.15} viewBox="0 0 100 115" style={{overflow: "visible", opacity: k, transform: `translateY(${(1 - k) * -16}px)`}}>
      <path d="M 26 52 L 26 34 A 24 24 0 0 1 74 34 L 74 52" stroke={color} strokeWidth={12} fill="none" strokeLinecap="round" />
      <rect x={10} y={50} width={80} height={62} rx={12} fill={color} />
      <circle cx={50} cy={78} r={9} fill={C.light} />
    </svg>
  );
};

// ── 작은 계좌 아이콘 (그날 함께 두려움에 떤 다른 계좌들) ──
export const MiniAccount: React.FC<{at: number; dark?: boolean; w?: number}> = ({at, dark, w = 120}) => {
  const f = useCurrentFrame();
  const k = enter(f, at);
  const ink = dark ? C.ink : C.gray;
  return (
    <div style={{width: w, height: w * 0.74, boxSizing: "border-box", border: `4px solid ${ink}`, borderRadius: 14, background: C.light, padding: "12px 14px", opacity: k, transform: `translateY(${(1 - k) * 16}px)`, display: "flex", flexDirection: "column", gap: 8}}>
      <div style={{width: "55%", height: 8, borderRadius: 4, background: ink}} />
      <div style={{width: "80%", height: 18, borderRadius: 4, background: C.loss, opacity: dark ? 1 : 0.55}} />
      <div style={{width: "100%", height: 12, borderRadius: 4, background: ink, opacity: 0.5}} />
    </div>
  );
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

/** 취소선 — 공통 Strike는 시작 전에도 12px 조각이 보여서, at 전에는 글자만 그린다 */
export const StrikeAt: React.FC<{at: number; color?: string; children: React.ReactNode}> = ({at, color, children}) => {
  const f = useCurrentFrame();
  return f < at ? <span style={{display: "inline-block"}}>{children}</span> : <Strike at={at} color={color}>{children}</Strike>;
};
