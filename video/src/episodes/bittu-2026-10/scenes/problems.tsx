// 문제 분석 파트 S13–S21 (문장 28–56)
import React from "react";
import {interpolate, useCurrentFrame} from "remotion";
import {C} from "../../../design/tokens";
import {count, enter, prog, shake} from "../../../components/anim";
import {num, won} from "../../../components/fmt";
import {Big, Box, Card, Chip, CornerNote, Headline, Hi, Label, Mark, fadeOut, vis} from "../../../components/ui";
import {NumberTitle} from "../../../components/cards";
import {Bars, HRule, Layer, Line, P, PtLabel} from "../../../components/charts";
import {F} from "../facts";
import {DEBT_FILL, GHOST_FILL, Gauge, LeverageCard, Swatch, ValueBar} from "../local";
import {CARD_X, CARD_Y, SaleDays, SceneC} from "./story";

const STATIC = -60; // 같은 항목의 이어지는 장면: 번호 타이틀이 이미 떠 있음
const LIGHT_LOSS = "#9DB7EA"; // 비교 대상의 손실 막대 (연한 파랑)
const CLAMP = {extrapolateLeft: "clamp", extrapolateRight: "clamp"} as const;

// 번호 타이틀 문구 (같은 항목은 같은 문구)
const T01 = "빚은 손실도 똑같이 키운다";
const T02 = "가장 나쁜 때, 가장 나쁜 가격에 판다";
const T03 = "이자는 주가와 상관없이 매일 쌓인다";
const T04 = "빚낸 투자자가 더 크게 잃었다";

// 줄어드는 막대 한 줄: 남은 부분(잉크) + 사라진 부분(파랑 점선)
const ShrinkRow: React.FC<{y: number; at: number; drop: number; label: React.ReactNode; sub: React.ReactNode; value: React.ReactNode; valueAt: number}> = ({y, at, drop, label, sub, value, valueAt}) => {
  const f = useCurrentFrame();
  const W = 760;
  const p = prog(f, valueAt, 26);
  const keep = W * (1 - (drop / 100) * p);
  return (
    <div style={{position: "absolute", left: 0, top: y, width: 1920, ...vis(f, at)}}>
      <div style={{position: "absolute", left: 140, top: 0, width: 360}}>
        <Label size={50}>{label}</Label>
        <Label size={34} weight={500} color={C.gray} style={{marginTop: 4}}>
          {sub}
        </Label>
      </div>
      <div style={{position: "absolute", left: 520, top: 20, width: W, height: 84, display: "flex", gap: 4}}>
        <div style={{width: keep, height: 84, background: C.ink, borderRadius: 8, flex: "none"}} />
        {W - keep > 2 ? <div style={{width: W - keep - 4, height: 84, boxSizing: "border-box", background: GHOST_FILL, border: `4px dashed ${C.loss}`, borderRadius: 8, flex: "none"}} /> : null}
      </div>
      <div style={{position: "absolute", left: 1320, top: -14, display: "flex", alignItems: "baseline", gap: 12, opacity: enter(f, valueAt)}}>{value}</div>
    </div>
  );
};

// S13 문장 28–30: "01" → 주가 약 -42% vs 사연자의 돈 3,000만 원 -83%
export const S13: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const d1 = count(f, a(29, 0.35), 0, -F.stockDrop.v, 26);
  const d2 = count(f, a(30, 0.3), 0, -F.ownDrop.v, 26);
  return (
    <>
      <NumberTitle
        no="01"
        at={a(28)}
        title={
          <>
            빚은 <Hi at={a(28, 0.55)}>손실도</Hi> 똑같이 키운다
          </>
        }
      />
      <ShrinkRow
        y={330}
        at={a(29)}
        valueAt={a(29, 0.35)}
        drop={F.stockDrop.v}
        label="주가"
        sub="팔린 날 · 산 가격 대비"
        value={
          <>
            <Label size={52}>약</Label>
            <Big size={140} color={C.loss}>
              {num(d1)}%
            </Big>
          </>
        }
      />
      <ShrinkRow
        y={560}
        at={a(30)}
        valueAt={a(30, 0.3)}
        drop={F.ownDrop.v}
        label="사연자의 돈"
        sub={won(F.own.v)}
        value={
          <Big size={170} color={C.loss}>
            {num(d2)}%
          </Big>
        }
      />
    </>
  );
};

// S14 문장 31–32: 큰 평가액 막대 — 빌린 돈 칸은 그대로, 내 돈 칸만 3,000만 → 500만 원 / 내 돈 = 빌린 돈일 때 (뒷줄) 주가 -50% → 내 돈 0원
export const S14: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  const W = 1400;
  const MAX = F.bought.v;
  const p31 = prog(f, a(31, 0.2), 30);
  const reset = prog(f, a(32, 0.05), 16);
  const p32 = prog(f, b(32, 0.2), 26);
  const own = f < a(32) ? F.own.v + (F.left.v - F.own.v) * p31 : f < b(32) ? F.left.v + (F.own.v - F.left.v) * reset : F.own.v * (1 - p32);
  const zero = count(f, b(32, 0.2), F.own.v, F.halfLeft.v, 26);
  return (
    <>
      <NumberTitle no="01" at={STATIC} title={T01} />
      <Box x={260} y={270}>
        <div style={{display: "flex", alignItems: "center", gap: 20}}>
          <div style={vis(f, a(31), a(32))}>
            <Chip variant="loss" size={42}>
              주가 ↓
            </Chip>
          </div>
        </div>
      </Box>
      <Box x={260} y={270}>
        <div style={{display: "flex", alignItems: "center", gap: 20}}>
          <div style={vis(f, a(32))}>
            <Chip variant="outline" size={42}>
              내 돈 = 빌린 돈
            </Chip>
          </div>
          <div style={vis(f, b(32))}>
            <Chip variant="loss" size={42}>
              주가 -{F.half.v}%
            </Chip>
          </div>
        </div>
      </Box>
      <Box x={260} y={380}>
        <div style={{opacity: enter(f, a(31))}}>
          <ValueBar own={own} debt={F.debt.v} width={W} max={MAX} height={100} />
        </div>
      </Box>
      <Box x={260} y={500} w={W}>
        <div style={{display: "flex", justifyContent: "space-between", opacity: enter(f, a(31))}}>
          <Label size={44}>
            <Swatch kind="own" size={34} />
            {f < b(32) ? `내 돈 ${won(own)}` : "내 돈"}
          </Label>
          <div style={{textAlign: "right"}}>
            <Label size={44}>
              <Swatch kind="debt" size={34} />
              빌린 돈 {won(F.debt.v)}
            </Label>
            <div style={vis(f, a(31, 0.45))}>
              <Label size={52} weight={900} style={{marginTop: 8}}>
                = 그대로 갚아야
              </Label>
            </div>
          </div>
        </div>
      </Box>
      <Box x={260} y={640}>
        <div style={{display: "flex", alignItems: "baseline", gap: 24, ...vis(f, b(32, 0.2))}}>
          <Label size={52}>남은 내 돈</Label>
          <Big size={140} color={C.loss}>
            <Hi at={b(32, 0.7)}>{won(zero)}</Hi>
          </Big>
        </div>
      </Box>
    </>
  );
};

// S15 문장 33–36: "02" → 담보 비율 막대(140% 선) → 선 아래로 → 정해진 날까지 돈 더 넣기 → 못 넣으면 장 시작하자마자 매도 (개념도)
export const S15: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const ratio = interpolate(f, [a(35, 0.1), a(35, 0.1) + 30], [2.0, 1.22], CLAMP);
  const dim = prog(f, a(36, 0.45), 14);
  return (
    <>
      <NumberTitle no="02" at={a(33)} title={T02} />
      <Gauge
        x={140}
        y={370}
        U={560}
        ratio={ratio}
        at={a(34)}
        lineAt={a(34, 0.45)}
        dim={dim}
        lineLabel={
          <Label size={52} weight={900}>
            <Hi at={a(34, 0.6)}>{F.keep.v}% 이상</Hi>
          </Label>
        }
      />
      <Box x={140} y={650}>
        <div style={{display: "flex", alignItems: "center", gap: 26}}>
          <div style={vis(f, a(35, 0.45))}>
            <Chip size={42}>정해진 날까지 돈 더 넣기</Chip>
          </div>
          <div style={vis(f, a(36))}>
            <Chip variant="loss" size={42}>
              못 넣으면 → 장 시작하자마자 매도
            </Chip>
          </div>
        </div>
      </Box>
      <CornerNote at={a(34)} y={130}>
        개념도
      </CornerNote>
    </>
  );
};

// S16 문장 37–40: 전날 종가와 15~30% 낮은 가격(개념도) → 모자란 돈 vs 팔리는 주식 → 금융감독원 사례 201만 원 → 405주 · 3,090만 원어치 전부
export const S16: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const sw = a(38);
  const baseY = 720;
  const maxH = 400;
  const hS = F.short.v / F.soldAmt.v;
  const x1 = 600;
  const x2 = 1240;
  const bw = 260;
  const s = count(f, a(39, 0.45), 0, F.short.v, 20);
  const big = count(f, a(40, 0.15), 0, F.soldAmt.v, 24);
  return (
    <>
      <NumberTitle no="02" at={STATIC} title={T02} />
      <div style={{position: "absolute", inset: 0, opacity: fadeOut(f, sw)}}>
        <HRule y={360} x0={200} x1={1500} at={a(37)} color={C.ink} />
        <Box x={200} y={290}>
          <div style={vis(f, a(37))}>
            <Label size={44}>전날 종가</Label>
          </div>
        </Box>
        <div
          style={{
            position: "absolute",
            left: 200,
            top: 430,
            width: 1300 * prog(f, a(37, 0.3), 16),
            height: 170,
            boxSizing: "border-box",
            background: GHOST_FILL,
            border: `4px dashed ${C.loss}`,
            borderRadius: 10,
          }}
        />
        <Box x={240} y={480}>
          <div style={{display: "flex", alignItems: "baseline", gap: 30, ...vis(f, a(37, 0.45))}}>
            <Label size={60} weight={900} color={C.loss}>
              {F.discount.v} 낮은 가격
            </Label>
            <Label size={46}>→ 팔 수량 기준</Label>
          </div>
        </Box>
        <CornerNote at={a(37)}>개념도</CornerNote>
      </div>
      <div style={{position: "absolute", inset: 0, opacity: enter(f, sw)}}>
        <Bars
          x={x1}
          baseY={baseY}
          maxH={maxH}
          barW={bw}
          gap={x2 - x1 - bw}
          items={[
            {h: hS, color: C.gray, label: "모자란 돈", at: sw},
            {h: 1, color: C.loss, label: "팔리는 주식", at: sw + 8},
          ]}
        />
        <Box x={x1 + bw / 2} y={baseY - maxH * hS - 90} w={400} center>
          <div style={vis(f, a(39, 0.45))}>
            <Label size={60} weight={900}>
              {won(s)}
            </Label>
          </div>
        </Box>
        <Box x={x2 + bw / 2} y={baseY - maxH - 90} w={700} center>
          <div style={vis(f, a(40, 0.1))}>
            <Label size={60} weight={900}>
              {F.soldShares.v}주 · {won(big)}어치
            </Label>
          </div>
        </Box>
        <Box x={x2 + bw + 40} y={470}>
          <div style={vis(f, a(40, 0.5))}>
            <Label size={64} weight={900}>
              <Hi at={a(40, 0.62)}>전부 팔림</Hi>
            </Label>
          </div>
        </Box>
        <Box x={140} y={290}>
          <div style={vis(f, a(39))}>
            <Chip size={42}>{F.fss.v} 사례</Chip>
          </div>
        </Box>
      </div>
    </>
  );
};

// S17 문장 41–42: S08과 같은 날짜 칸(7월 30일 강제 매도 → 7월 31일 +30% 가까이) / (뒷줄) 팔린 주식은 돌아오지 않음 → 빚이 없었다면 스스로 결정
export const S17: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  return (
    <>
      <NumberTitle no="02" at={STATIC} title={T02} />
      <SaleDays at={a(41)} upAt={a(41, 0.3)} y={280} />
      <Box x={960} y={540} w={1600} center>
        <div style={{display: "inline-flex", alignItems: "center", gap: 18, ...vis(f, b(41))}}>
          <Mark kind="cross" at={b(41, 0.1)} size={60} color={C.loss} />
          <Label size={56} weight={900}>
            이미 팔린 주식은 돌아오지 않음
          </Label>
        </div>
      </Box>
      <Box x={960} y={660} w={1700} center>
        <div style={{display: "inline-flex", alignItems: "center", gap: 18, ...vis(f, a(42))}}>
          <Mark kind="check" at={a(42, 0.2)} size={60} color={C.ink} />
          <Label size={52}>
            빚이 없었다면 → 기다릴지 말지 <Hi at={a(42, 0.5)}>스스로 결정</Hi>
          </Label>
        </div>
      </Box>
    </>
  );
};

// S18 문장 43–46: "03" → 개념도(주가와 상관없이 매일 오르는 이자 계단) → 2026년 5월 증권사 10곳 / (뒷줄) 90일 넘게 평균 연 9.38% → 3,000만 원 1년 이자 280만 원 넘게 → 1년 +9% 넘게 못 오르면 손해
const STOCK_WIGGLE: P[] = [
  [260, 430],
  [400, 360],
  [520, 470],
  [660, 380],
  [800, 520],
  [940, 410],
  [1080, 500],
  [1220, 360],
  [1360, 470],
  [1500, 400],
];
const stairs = (): P[] => {
  const pts: P[] = [[260, 720]];
  for (let i = 0; i < 10; i++) {
    const x = 260 + (i + 1) * 124;
    const y0 = 720 - i * 24;
    pts.push([x, y0], [x, y0 - 24]);
  }
  return pts;
};
const STAIRS = stairs();
export const S18: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  const c1 = a(44);
  const c2 = a(45);
  const rate = count(f, b(44, 0.15), 0, F.rate.v, 24);
  const intr = count(f, a(45, 0.3), 0, F.interest.v, 26);
  return (
    <>
      <NumberTitle
        no="03"
        at={a(43)}
        title={
          <>
            이자는 주가와 상관없이 <Hi at={a(43, 0.55)} until={c1}>매일</Hi> 쌓인다
          </>
        }
      />
      <div style={{position: "absolute", inset: 0, opacity: fadeOut(f, c1)}}>
        <Layer>
          <Line pts={STOCK_WIGGLE} at={a(43, 0.15)} dur={26} color={C.gray} width={6} />
          <Line pts={STAIRS} at={a(43, 0.3)} dur={34} color={C.loss} width={8} />
        </Layer>
        <PtLabel p={STOCK_WIGGLE[STOCK_WIGGLE.length - 1]} at={a(43, 0.15)} anchor="right">
          <Label size={44} color={C.gray}>
            주가
          </Label>
        </PtLabel>
        <PtLabel p={STAIRS[STAIRS.length - 1]} at={a(43, 0.5)} anchor="right">
          <Label size={48} weight={900} color={C.loss}>
            이자
          </Label>
        </PtLabel>
        <CornerNote at={a(43, 0.15)}>개념도</CornerNote>
      </div>
      <div style={{position: "absolute", inset: 0, opacity: enter(f, c1) * fadeOut(f, c2)}}>
        <Box x={960} y={290} w={1600} center>
          <div style={vis(f, c1)}>
            <Chip size={44}>
              {F.rateMonth.v} · 증권사 {F.brokers.v}곳 신용 이자
            </Chip>
          </div>
        </Box>
        <Box x={960} y={410} w={1600} center>
          <div style={vis(f, b(44))}>
            <Label size={52}>{F.over90.v}일 넘게 · 평균</Label>
          </div>
          <div style={{opacity: enter(f, b(44, 0.15))}}>
            <Big size={200}>연 {num(rate, 2)}%</Big>
          </div>
        </Box>
      </div>
      <div style={{position: "absolute", inset: 0, opacity: enter(f, c2)}}>
        <Box x={960} y={280} w={1600} center>
          <Label size={48} weight={500} color={C.gray}>
            {won(F.debt.v)} · {F.oneYear.v} · 연 {F.rate.v}%
          </Label>
          <div style={{display: "flex", justifyContent: "center", alignItems: "baseline", gap: 22, marginTop: 14, opacity: enter(f, a(45, 0.3))}}>
            <Label size={60}>이자</Label>
            <Big size={180} color={C.loss}>
              {won(intr)}
            </Big>
            <Label size={60}>넘게</Label>
          </div>
        </Box>
        <Box x={960} y={600} w={1700} center>
          <div style={vis(f, a(46))}>
            <Label size={44} weight={500} color={C.gray}>
              빌린 돈으로 산 부분
            </Label>
          </div>
          <div style={{marginTop: 8, ...vis(f, a(46, 0.3))}}>
            <Label size={60} weight={900}>
              {F.oneYear.v}에 <Hi at={a(46, 0.5)}>+{F.breakeven.v}% 넘게</Hi> 못 오르면 → 손해
            </Label>
          </div>
        </Box>
      </div>
    </>
  );
};

// S19 문장 47–50: "04" → 국내 대형 증권사 2곳 · 개인 계좌 460만 개 → 2026년 3월 1~9일 폭락장 / (뒷줄) 신용 쓴 계좌 -19% → 안 쓴 계좌 -8.2%, 2.3배
export const S19: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  const sw = a(49);
  const acc = count(f, a(48, 0.3), 0, F.accounts.v, 24);
  const l1 = count(f, b(49, 0.2), 0, -F.creditLoss.v, 22);
  const l2 = count(f, a(50, 0.15), 0, -F.noCreditLoss.v, 22);
  const baseY = 730;
  const maxH = 270;
  const x1 = 560;
  const x2 = 1100;
  const bw = 280;
  const h2 = F.noCreditLoss.v / F.creditLoss.v;
  return (
    <>
      <NumberTitle no="04" at={a(47)} title={T04} />
      <Box x={960} y={300} w={1300} center>
        <div style={{...vis(f, a(48), sw), display: "inline-block"}}>
          <Card style={{width: 1100, boxSizing: "border-box", textAlign: "center", padding: "40px 56px"}}>
            <Label size={50}>
              국내 대형 증권사 {F.firms.v}곳 · 개인 계좌
            </Label>
            <div style={{opacity: enter(f, a(48, 0.3))}}>
              <Big size={200} style={{marginTop: 14}}>
                {num(acc)}만 개
              </Big>
            </div>
          </Card>
        </div>
      </Box>
      <Box x={960} y={262} w={1300} center>
        <div style={vis(f, sw)}>
          <Chip size={42}>{F.crashPeriod.v} 폭락장</Chip>
        </div>
      </Box>
      <div style={{position: "absolute", inset: 0, opacity: enter(f, b(49))}}>
        <Bars
          x={x1}
          baseY={baseY}
          maxH={maxH}
          barW={bw}
          gap={x2 - x1 - bw}
          items={[
            {h: 1, color: C.loss, label: "신용 쓴 계좌", at: b(49)},
            {h: h2, color: LIGHT_LOSS, label: "신용 안 쓴 계좌", at: a(50)},
          ]}
        />
      </div>
      <Box x={x1 + bw / 2} y={baseY - maxH - 130} w={500} center>
        <div style={vis(f, b(49, 0.2))}>
          <Big size={110} color={C.loss}>
            {num(l1)}%
          </Big>
        </div>
      </Box>
      <Box x={x2 + bw / 2} y={baseY - maxH * h2 - 130} w={500} center>
        <div style={vis(f, a(50, 0.15))}>
          <Big size={110} color={C.loss}>
            {num(l2, 1)}%
          </Big>
        </div>
      </Box>
      <Box x={x2 + bw + 60} y={520}>
        <div style={vis(f, a(50, 0.55))}>
          <Label size={80} weight={900}>
            <Hi at={a(50, 0.68)}>{F.ratio.v}배</Hi>
          </Label>
        </div>
      </Box>
    </>
  );
};

// S20 문장 51–52: 미국 · 2010년 / (뒷줄) 개인 외환 거래 빚의 한도 ↓ → 빚을 많이 쓰던 투자자의 손실: 줄이기 전 vs 그 뒤 (40% 줄어듦)
export const S20: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  const sw = a(52);
  const cut = prog(f, b(51, 0.35), 24);
  const baseY = 722;
  const maxH = 300;
  const x1 = 560;
  const x2 = 1100;
  const bw = 280;
  const h2 = F.usAfter.v / 100;
  const topL = baseY - maxH;
  const topR = baseY - maxH * h2;
  const lx = x2 + bw + 50;
  const lp = prog(f, a(52, 0.55), 12);
  return (
    <>
      <NumberTitle no="04" at={STATIC} title={T04} />
      <Box x={140} y={265}>
        <div style={vis(f, a(51))}>
          <Chip size={44}>미국 · {F.usYear.v}년</Chip>
        </div>
      </Box>
      <div style={{position: "absolute", inset: 0, opacity: fadeOut(f, sw)}}>
        <Box x={140} y={390}>
          <div style={vis(f, b(51))}>
            <Label size={50}>개인 외환 거래 · 쓸 수 있는 빚의 한도</Label>
          </div>
        </Box>
        <Box x={140} y={480}>
          <div style={{display: "flex", alignItems: "center", gap: 30, opacity: enter(f, b(51))}}>
            <div style={{width: 1300 - 700 * cut, height: 90, boxSizing: "border-box", background: DEBT_FILL, border: `4px solid ${C.ink}`, borderRadius: 10}} />
            <Label size={72} weight={900} style={{opacity: cut}}>
              ↓
            </Label>
          </div>
        </Box>
      </div>
      <div style={{position: "absolute", inset: 0, opacity: enter(f, sw)}}>
        <Box x={(x1 + x2 + bw) / 2} y={350} w={900} center>
          <Label size={44}>빚을 많이 쓰던 투자자의 손실</Label>
        </Box>
        <Bars
          x={x1}
          baseY={baseY}
          maxH={maxH}
          barW={bw}
          gap={x2 - x1 - bw}
          items={[
            {h: 1, color: C.loss, label: "한도 줄이기 전", at: sw},
            {h: h2, color: LIGHT_LOSS, label: "그 뒤", at: a(52, 0.3)},
          ]}
        />
        <div style={{position: "absolute", left: x1 + bw, top: topL - 3, width: (lx - x1 - bw) * lp, borderTop: `5px dashed ${C.loss}`}} />
        <div style={{position: "absolute", left: lx - 3, top: topL, width: 6, height: (topR - topL) * lp, background: C.loss}} />
        <Box x={lx + 30} y={(topL + topR) / 2 - 40}>
          <div style={vis(f, a(52, 0.6))}>
            <Label size={64} weight={900}>
              <Hi at={a(52, 0.7)}>{F.usCut.v}% 줄어듦</Hi>
            </Label>
          </div>
        </Box>
      </div>
    </>
  );
};

// S21 문장 53–56: 빚 덕분에 크게 번 사람도 ✓ → 사연자도 6월까지(S03 카드 +1,500만 원) → 한 번의 폭락: +1,500만 → 0원 / (뒷줄) → -2,500만 원 → 어떤 기준?
export const S21: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  const cardAt = a(54);
  const out = a(56);
  const g = count(f, a(55, 0.3), F.gain.v, 0, 22); // 번 돈 사라짐
  const l = count(f, b(55, 0.2), 0, F.loss.v, 26); // 내 돈까지
  const own = F.own.v + g + l;
  const pnl = g + l;
  return (
    <>
      <Box x={960} y={380} w={1600} center>
        <div style={{display: "inline-flex", alignItems: "center", gap: 22, ...vis(f, a(53), cardAt)}}>
          <Mark kind="check" at={a(53, 0.15)} size={80} color={C.gain} />
          <Headline size={80}>빚 덕분에 크게 번 사람도</Headline>
        </div>
      </Box>
      <div style={{position: "absolute", inset: 0, opacity: fadeOut(f, out)}}>
        <Box x={CARD_X} y={CARD_Y}>
          <div style={vis(f, cardAt)}>
            <LeverageCard own={own} debt={F.debt.v} pnl={pnl} shakeX={shake(f, b(55, 0.2) + 26)} />
          </div>
        </Box>
        <Box x={1230} y={200}>
          <div style={vis(f, a(54, 0.15))}>
            <Chip size={46}>사연자도 6월까지</Chip>
          </div>
          <div style={{marginTop: 40, ...vis(f, a(55))}}>
            <Chip variant="loss" size={46}>
              한 번의 폭락
            </Chip>
          </div>
          <div style={{marginTop: 34, ...vis(f, a(55, 0.3))}}>
            <Label size={46} weight={900}>
              번 돈
              <span style={{opacity: enter(f, b(55))}}> + 내 돈까지</span>
            </Label>
          </div>
        </Box>
      </div>
      <Box x={960} y={300} w={1600} center>
        <div style={vis(f, out)}>
          <Headline size={88}>빚을 낸다면,</Headline>
        </div>
        <div style={vis(f, a(56, 0.3))}>
          <Headline size={88}>
            <Hi at={a(56, 0.55)}>어떤 기준</Hi>을 지킬까?
          </Headline>
        </div>
      </Box>
    </>
  );
};

