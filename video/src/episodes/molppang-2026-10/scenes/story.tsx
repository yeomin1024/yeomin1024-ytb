// 사연 파트 S01–S05 (문장 1–11) — 장면 구성표: ../plan.ts
import React from "react";
import {useCurrentFrame} from "remotion";
import {C} from "../../../design/tokens";
import {count, enter, prog, shake} from "../../../components/anim";
import {won} from "../../../components/fmt";
import {ST} from "../../../components/timeline";
import {Arrow, Big, Box, Card, CornerNote, Headline, Hi, Label, Mark, fadeOut, vis} from "../../../components/ui";
import {Bubble, NewsCard} from "../../../components/cards";
import {Dot, HRule, Layer, Line, P, PtLabel} from "../../../components/charts";
import {CheckRow} from "../../../components/objects";
import {F, PRICE} from "../facts";
import {CrossLabel, DateTag, MyAccount, SearchBar} from "../local";

export type SceneC = React.FC<{t: ST}>;

// 사연 계좌 카드 위치 (S02·S03·S04·S05·S11·S29·S30 같은 자리, 같은 모양)
export const CARD_X = 120;
export const CARD_Y = 170;
const RX = 1150; // 오른쪽 열

/** 문장 5의 생각 말풍선 문구 (S30에서 같은 말풍선으로 다시 씀 — "사연자처럼") */
export const THOUGHT_UP = "더 오를 것 같아";

/** "정도" 같은 꼬리말 (계좌 카드 평가손익 옆) */
export const Tail: React.FC<{children: React.ReactNode; o?: number}> = ({children, o = 1}) => (
  <Label size={44} style={{opacity: o, whiteSpace: "nowrap"}}>
    {children}
  </Label>
);

// S01 문장 1–2: 검색창 "AI 관련 주식" → (뒷줄) 몽고디비 → 투자 전망 ✓ · 실적 ✓ · 주가 상승세 ✓
export const S01: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  const up: P[] = [
    [0, 44],
    [30, 36],
    [52, 40],
    [84, 18],
    [110, 4],
  ];
  return (
    <>
      <Box x={150} y={230}>
        <div style={vis(f, a(1))}>
          <SearchBar text={F.aiStock.v} textP={prog(f, a(1, 0.12), 28)} w={880} />
        </div>
      </Box>
      <Box x={150} y={400}>
        <div style={vis(f, b(1))}>
          <Card style={{width: 880, boxSizing: "border-box", padding: "30px 48px"}}>
            <Label size={36} weight={500} color={C.gray}>
              종목
            </Label>
            <Big size={130} style={{marginTop: 10}}>
              {F.company.v}
            </Big>
          </Card>
        </div>
      </Box>
      <Box x={RX + 30} y={250}>
        <div style={{display: "flex", flexDirection: "column", gap: 56}}>
          <CheckRow at={a(2, 0.02)} checkAt={a(2, 0.12)} size={50}>
            {F.outlook.v}
          </CheckRow>
          <CheckRow at={a(2, 0.3)} checkAt={a(2, 0.4)} size={50}>
            {F.earnings.v}
          </CheckRow>
          <CheckRow at={a(2, 0.55)} checkAt={a(2, 0.66)} size={50}>
            <span style={{display: "inline-flex", alignItems: "center", gap: 22}}>
              {F.trend.v}
              <svg width={112} height={50} style={{overflow: "visible"}}>
                <path
                  d={up.map((q, i) => `${i ? "L" : "M"} ${q[0]} ${q[1]}`).join(" ")}
                  stroke={C.gain}
                  strokeWidth={8}
                  fill="none"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeDasharray={140}
                  strokeDashoffset={140 * (1 - prog(f, a(2, 0.6), 18))}
                />
              </svg>
            </span>
          </CheckRow>
        </div>
      </Box>
    </>
  );
};

// S02 문장 3: 계좌 카드 — 전 재산 7,000만 원이 몽고디비 한 종목으로 100% → "몰빵"
export const S02: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const buyAt = a(3, 0.45);
  const p = prog(f, buyAt, 22);
  return (
    <>
      <Box x={CARD_X} y={CARD_Y}>
        <div style={vis(f, a(3))}>
          <MyAccount pnl={f < buyAt + 22 ? null : 0} stock={p} footL={`${F.company.v} ${won(F.all.v * p)}`} footR={`현금 ${won(F.all.v * (1 - p))}`} />
        </div>
      </Box>
      <Box x={RX + 30} y={250}>
        <div style={vis(f, buyAt)}>
          <Label size={48}>{F.company.v}</Label>
          <Big size={200} style={{marginTop: 6}}>
            {Math.round(100 * p)}%
          </Big>
        </div>
        <div style={{marginTop: 40, ...vis(f, a(3, 0.7))}}>
          <Headline size={110}>
            <Hi at={a(3, 0.78)}>{F.allIn.v}</Hi>
          </Headline>
        </div>
      </Box>
    </>
  );
};

// S03 문장 4–6: 같은 계좌 카드 +1,000만 원 정도 → 전고점(개념도) + 생각 말풍선 "더 오를 것 같아" → 문장 6 ✗ (꿈)
const PK: P[] = [
  [1170, 300], // 전고점
  [1250, 400],
  [1330, 520],
  [1410, 470],
  [1480, 500],
  [1570, 410], // 지금 (+1,000만 원)
];
const PROJ: P[] = [PK[PK.length - 1], [1760, 312]];
export const S03: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const gainAt = a(4, 0.25);
  const pnl = count(f, gainAt, 0, F.gain.v);
  const dream = a(6, 0.15);
  return (
    <>
      <Box x={CARD_X} y={CARD_Y}>
        <MyAccount pnl={pnl} pnlNote={<Tail o={enter(f, gainAt + 20)}>정도</Tail>} footL={`${F.company.v} ${won(F.all.v)}`} footR="현금 0원" />
      </Box>
      {/* 5: 전고점 (개념도) */}
      <HRule y={PK[0][1]} x0={PK[0][0]} x1={1790} at={a(5)} color={C.gray} />
      <Box x={PK[0][0]} y={PK[0][1] - 66}>
        <div style={vis(f, a(5))}>
          <Label size={40} color={C.gray}>
            {F.prevHigh.v}
          </Label>
        </div>
      </Box>
      <Layer>
        <Line pts={PK} at={a(5, 0.05)} dur={22} width={7} />
        <Line pts={PROJ} at={a(5, 0.45)} dashed width={6} opacity={1 - 0.6 * prog(f, dream, 10)} />
        <Dot p={PK[PK.length - 1]} at={a(5, 0.4)} color={C.gain} />
      </Layer>
      <Box x={1615} y={316}>
        <div style={{opacity: enter(f, dream)}}>
          <Mark kind="cross" at={dream} size={100} />
        </div>
      </Box>
      <Box x={RX + 30} y={560}>
        <div style={{opacity: 1 - 0.55 * prog(f, dream, 10)}}>
          <Bubble at={a(5, 0.5)} size={48}>
            {THOUGHT_UP}
          </Bubble>
        </div>
      </Box>
      <CornerNote at={a(5)} y={780}>
        개념도
      </CornerNote>
    </>
  );
};

// S04 문장 7–9 (네이비): 같은 계좌 카드 +1,000만 → -2,000만 원 + 흔들림 → 뉴스 "CEO, 다른 회사로 이적" → 고점에서 내려오던 주가가 (뒷줄) 최대 -26%
const yv = (v: number) => 300 + (PRICE.mdbHigh - v) * (400 / (PRICE.mdbHigh - PRICE.mdbLow));
const DOWN: P[] = [
  [260, yv(PRICE.mdbHigh)],
  [400, yv(462)],
  [520, yv(468)],
  [660, yv(440)],
  [800, yv(449)],
  [940, yv(424)],
  [1080, yv(PRICE.mdbPrevClose)],
];
const NEWS: P = DOWN[DOWN.length - 1];
const LOW: P = [1200, yv(PRICE.mdbLow)];
export const S04: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  const hit = a(7, 0.5);
  const pnl = count(f, hit, F.gain.v, F.loss.v, 24);
  const out = a(9);
  return (
    <>
      <div style={{position: "absolute", inset: 0, opacity: fadeOut(f, out)}}>
        <Box x={CARD_X} y={CARD_Y}>
          <MyAccount pnl={pnl} head={<DateTag style={{opacity: enter(f, a(7))}}>어느 날</DateTag>} footL={`${F.company.v} ${won(F.all.v)}`} footR="현금 0원" shakeX={shake(f, hit + 24)} />
        </Box>
        <Box x={RX} y={210}>
          <div style={vis(f, a(8, 0.35))}>
            <NewsCard
              date={F.company.v}
              title={
                <>
                  CEO,
                  <br />
                  다른 회사로 이적
                </>
              }
              width={680}
            />
          </div>
        </Box>
      </div>
      {/* 9: 고점에서 내려오던 주가 → (뒷줄) 그 소식에 최대 -26% */}
      <div style={{position: "absolute", inset: 0, opacity: enter(f, out)}}>
        <Box x={140} y={150}>
          <div style={vis(f, out)}>
            <DateTag style={{background: C.inkOnNavy, color: C.navy}}>{F.company.v}</DateTag>
          </div>
        </Box>
        <Layer>
          <Line pts={DOWN} at={out + 2} dur={30} color={C.loss} width={6} />
          <Line pts={[NEWS, LOW]} at={b(9, 0.1)} dur={10} color={C.loss} width={12} />
          <Dot p={DOWN[0]} at={out + 2} color={C.inkOnNavy} />
          <Dot p={NEWS} at={a(9, 0.42)} color={C.inkOnNavy} />
          <Dot p={LOW} at={b(9, 0.25)} color={C.loss} r={16} />
        </Layer>
        <PtLabel p={DOWN[0]} at={out + 2} anchor="top">
          <Label size={44}>고점</Label>
        </PtLabel>
        <PtLabel p={NEWS} at={a(9, 0.42)} anchor="top" gap={30}>
          <div style={{display: "inline-block", border: `4px solid ${C.inkOnNavy}`, borderRadius: 12, padding: "6px 20px"}}>
            <Label size={38}>CEO 이적 소식</Label>
          </div>
        </PtLabel>
        <PtLabel p={LOW} at={b(9, 0.3)} anchor="right" gap={34}>
          <div style={{textAlign: "left"}}>
            <Label size={48}>최대</Label>
            <Big size={190} color={C.loss}>
              {F.maxDrop.v}%
            </Big>
          </div>
        </PtLabel>
        <CornerNote at={out} y={140}>
          개념도
        </CornerNote>
      </div>
    </>
  );
};

// S05 문장 10–11 (네이비): 같은 계좌 카드 현금 0원 → ✗ 물타기 할 돈 → 하필 매수 다음에 (매수 → 이적 소식) → 말풍선 "너무 가혹해…"
export const S05: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const out = a(11);
  return (
    <>
      <Box x={CARD_X} y={CARD_Y}>
        <MyAccount
          pnl={F.loss.v}
          footL={`${F.company.v} ${won(F.all.v)}`}
          footR={
            <span style={{color: C.ink, fontWeight: 900}}>
              <Hi at={a(10, 0.2)}>현금 0원</Hi>
            </span>
          }
        />
      </Box>
      <div style={{position: "absolute", inset: 0, opacity: fadeOut(f, out)}}>
        <Box x={RX + 20} y={230}>
          <CrossLabel at={a(10, 0.1)} size={56}>
            물타기 할 돈
          </CrossLabel>
        </Box>
        <Box x={RX + 20} y={420}>
          <div style={vis(f, a(10, 0.45))}>
            <Label size={40} weight={500}>
              하필
            </Label>
          </div>
          <div style={{display: "flex", alignItems: "center", gap: 18, marginTop: 12}}>
            <div style={vis(f, a(10, 0.5))}>
              <DateTag style={{background: C.inkOnNavy, color: C.navy, fontSize: 40}}>내가 산 다음</DateTag>
            </div>
            <Arrow dir="right" len={90} at={a(10, 0.6)} color={C.inkOnNavy} />
            <div style={vis(f, a(10, 0.66))}>
              <DateTag style={{background: C.loss, color: "#FFFFFF", fontSize: 40}}>CEO 이적</DateTag>
            </div>
          </div>
        </Box>
      </div>
      <Box x={RX + 30} y={330}>
        <Bubble at={a(11, 0.1)} size={56}>
          너무 가혹해…
        </Bubble>
      </Box>
    </>
  );
};
