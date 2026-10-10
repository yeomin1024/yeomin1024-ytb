// 사연 파트 S01–S06 (문장 1–16) — 장면 구성표: stock/out/panicsell-2026-10/scene_plan.md
import React from "react";
import {useCurrentFrame} from "remotion";
import {C} from "../../../design/tokens";
import {count, enter, prog, shake} from "../../../components/anim";
import {num, won} from "../../../components/fmt";
import {ST} from "../../../components/timeline";
import {Big, Box, Card, Chip, CornerNote, Headline, Hi, Label, fadeOut, vis} from "../../../components/ui";
import {Bubble, NewsCard} from "../../../components/cards";
import {Dot, HRule, Layer, Line, P, PtLabel} from "../../../components/charts";
import {Phone} from "../../../components/objects";
import {F, PRICE} from "../facts";
import {DateTag, MyAccount, PauseIcon, StrikeAt} from "../local";

export type SceneC = React.FC<{t: ST}>;

// 사연 계좌 카드 위치 (S02·S04 같은 자리, 같은 모양)
export const CARD_X = 120;
export const CARD_Y = 170;
const RX = 1140; // 오른쪽 열

/** "넘게" 같은 꼬리말 (계좌 카드 평가손익 옆) */
export const Tail: React.FC<{children: React.ReactNode; o?: number}> = ({children, o = 1}) => (
  <Label size={44} style={{opacity: o}}>
    {children}
  </Label>
);

// S01 문장 1: 뉴스 카드 — 2026년 3월 4일 코스피 -12% 넘게 (하루 만에)
export const S01: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const d = count(f, a(1, 0.45), 0, -F.kospiDrop.v);
  return (
    <Box x={460} y={210}>
      <div style={vis(f, a(1))}>
        <NewsCard date={`${F.crashYear.v} ${F.crashDay.v}`} title="코스피" width={1000}>
          <div style={{display: "flex", alignItems: "center", gap: 36, marginTop: 6, opacity: enter(f, a(1, 0.45))}}>
            <Big size={210} color={C.loss}>
              {num(d)}%
            </Big>
            <div style={{opacity: enter(f, a(1, 0.6))}}>
              <Label size={52}>넘게</Label>
              <Label size={52}>하루 만에</Label>
            </div>
          </div>
        </NewsCard>
      </div>
    </Box>
  );
};

// S02 문장 2–6: 계좌 카드 (삼성전자 4,000만 원) → 산 이유 뉴스 → 산 다음 날 이란 공격 → 3월 3일 -400만 원 → "금방 회복하겠지"
export const S02: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const buyAt = a(2, 0.35);
  const amt = count(f, buyAt, 0, F.invest.v, 20);
  const hit = a(5, 0.45);
  const pnl = f < buyAt ? null : count(f, hit, 0, F.pnl0303.v);
  return (
    <>
      <Box x={CARD_X} y={CARD_Y}>
        <div style={vis(f, a(2))}>
          <MyAccount
            pnl={pnl}
            stock={prog(f, buyAt, 20)}
            head={<DateTag style={{opacity: enter(f, a(5))}}>{F.firstTradeDay.v}</DateTag>}
            footL={`${F.company.v} ${won(amt)}`}
          />
        </div>
      </Box>
      {/* 2: 닷새 전 */}
      <Box x={RX} y={200}>
        <div style={vis(f, a(2, 0.1), a(3))}>
          <Chip size={50}>{F.fiveDays.v}</Chip>
        </div>
      </Box>
      {/* 3: 산 이유 — 반도체 뉴스, 오래 들고 갈 생각 */}
      <Box x={RX} y={200}>
        <div style={vis(f, a(3), a(4))}>
          <NewsCard date="뉴스" title={F.reason.v} width={660} />
        </div>
        <div style={{marginTop: 30, ...vis(f, a(3, 0.5), a(4))}}>
          <Chip variant="outline" size={46}>
            {F.holdLong.v}
          </Chip>
        </div>
      </Box>
      {/* 4: 산 다음 날, 미국·이스라엘이 이란을 공격 */}
      <Box x={RX} y={200}>
        <div style={vis(f, a(4), a(5))}>
          <Chip size={46}>{F.dayAfterBuy.v}</Chip>
        </div>
        <div style={{marginTop: 24, ...vis(f, a(4, 0.2), a(5))}}>
          <NewsCard
            title={
              <>
                미국·이스라엘,
                <br />
                이란 공격
              </>
            }
            width={660}
          />
        </div>
      </Box>
      {/* 5: 연휴 뒤 첫 거래일 (카드 머리 3월 3일) */}
      <Box x={RX} y={200}>
        <div style={vis(f, a(5))}>
          <Chip size={46}>{F.holiday.v}</Chip>
        </div>
      </Box>
      {/* 6: 금방 회복하겠지 */}
      <Box x={RX + 20} y={360}>
        <Bubble at={a(6, 0.1)} size={50}>
          금방 회복하겠지
        </Bubble>
      </Box>
    </>
  );
};

// S03 문장 7–8 (네이비): 다음 날 3월 4일 → 오전 11시쯤 서킷브레이커, 시장 전체 거래 20분 멈춤
export const BreakerCard: React.FC<{f: number; at: number; timeAt?: number; haltAt: number; width?: number}> = ({f, at, timeAt, haltAt, width = 900}) => (
  <div style={vis(f, at)}>
    <Card style={{width, boxSizing: "border-box"}}>
      {timeAt !== undefined ? (
        <div style={{display: "inline-block", opacity: enter(f, timeAt)}}>
          <DateTag>{F.cbTime.v}</DateTag>
        </div>
      ) : null}
      <Headline size={84} style={{marginTop: timeAt !== undefined ? 14 : 0}}>
        서킷브레이커
      </Headline>
      <div style={{display: "flex", alignItems: "center", gap: 34, marginTop: 18, opacity: enter(f, haltAt), transform: `translateY(${(1 - enter(f, haltAt)) * 16}px)`}}>
        <PauseIcon size={150} color={C.ink} />
        <div>
          <Label size={44}>시장 전체 거래</Label>
          <div style={{display: "flex", alignItems: "baseline", gap: 16}}>
            <Big size={160}>{F.cbMinutes.v}분</Big>
            <Label size={56} weight={900}>
              멈춤
            </Label>
          </div>
        </div>
      </div>
    </Card>
  </div>
);

export const S03: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  return (
    <>
      <Box x={140} y={230}>
        <div style={vis(f, a(7))}>
          <Label size={52}>{F.nextDay.v}</Label>
          <Big size={180} style={{marginTop: 12}}>
            {F.crashDay.v}
          </Big>
        </div>
      </Box>
      <Box x={880} y={190}>
        <BreakerCard f={f} at={a(8)} timeAt={a(8)} haltAt={a(8, 0.55)} />
      </Box>
    </>
  );
};

// S04 문장 9–11 (네이비): 같은 계좌 카드 -400만 → -800만 원 넘게 + 흔들림 → 뉴스(전쟁·유가·환율) → "이러다 전부 잃겠다" → 장 마감 직전 전부 매도
const NEWS = ["전쟁 확대", "유가 ↑", "환율 ↑"];
export const S04: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const hit = a(9, 0.2);
  const pnl = count(f, hit, F.pnl0303.v, F.pnl0304.v, 24);
  const sell = a(11, 0.55);
  return (
    <>
      <Box x={CARD_X} y={CARD_Y}>
        <MyAccount
          pnl={pnl}
          pnlNote={<Tail o={enter(f, hit + 22)}>넘게</Tail>}
          stock={1 - prog(f, sell + 6, 16)}
          head={<DateTag>{F.crashDay.v}</DateTag>}
          footL={
            <StrikeAt at={sell + 10} color={C.ink}>
              {F.company.v} {won(F.invest.v)}
            </StrikeAt>
          }
          footR={<span style={{opacity: enter(f, sell + 16)}}>현금</span>}
          shakeX={shake(f, hit + 24)}
        />
      </Box>
      {/* 10: 뉴스가 쏟아짐 */}
      {NEWS.map((n, i) => (
        <Box key={n} x={RX + (i === 1 ? 50 : 0)} y={180 + i * 160}>
          <div style={vis(f, a(10, 0.12 + i * 0.22), a(11))}>
            <Card style={{width: 600, boxSizing: "border-box", padding: "18px 36px"}}>
              <Label size={30} weight={500} color={C.gray}>
                뉴스
              </Label>
              <Label size={54} weight={900}>
                {n}
              </Label>
            </Card>
          </div>
        </Box>
      ))}
      {/* 11: 이러다 전부 잃겠다 → 장 마감 직전 전부 매도 */}
      <Box x={RX + 10} y={210}>
        <Bubble at={a(11, 0.05)} size={50}>
          이러다 전부 잃겠다
        </Bubble>
      </Box>
      <Box x={RX + 40} y={480}>
        <div style={{...vis(f, sell), transform: `${vis(f, sell).transform} rotate(-4deg)`}}>
          <Label size={40}>{F.sellWhen.v}</Label>
          <div style={{marginTop: 10, display: "inline-block", border: `7px solid ${C.inkOnNavy}`, borderRadius: 16, padding: "8px 34px"}}>
            <Label size={84} weight={900}>
              {F.sellAll.v}
            </Label>
          </div>
        </div>
      </Box>
    </>
  );
};

// S05 문장 12–14 (네이비): 실제 종가 흐름 — 다 판 날 → 다음 날 +11% 넘게 → 7주 뒤 판 가격보다 +30% 넘게 → 처음 산 가격도 넘음
const yv = (p: number) => 700 - (p - 165000) * (460 / 65000);
const PATH: P[] = [
  [220, yv(PRICE.buy)], // 2/27 산 날
  [400, yv(PRICE.d0303)], // 3/3
  [580, yv(PRICE.sold)], // 3/4 판 날
];
const UP1: P = [760, yv(PRICE.d0305)]; // 3/5
const END: P = [1520, yv(PRICE.d0423)]; // 4/23
export const S05: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const sold = PATH[2];
  return (
    <>
      <Box x={220} y={150}>
        <div style={vis(f, a(12))}>
          <Chip size={40}>{F.company.v}</Chip>
        </div>
      </Box>
      <HRule y={sold[1]} x0={sold[0]} x1={1440} at={a(13)} color={C.gray} labelAt="right">
        <Label size={40} color={C.gray}>
          판 가격
        </Label>
      </HRule>
      <HRule y={PATH[0][1]} x0={PATH[0][0]} x1={1440} at={a(14)} color={C.inkOnNavy} labelAt="right">
        <Label size={40}>처음 산 가격</Label>
      </HRule>
      <Layer>
        <Line pts={PATH} at={a(12)} dur={14} color={C.gray} width={7} />
        <Line pts={[sold, UP1]} at={a(12, 0.35)} dur={14} color={C.gain} />
        <Line pts={[UP1, END]} at={a(13, 0.1)} dashed width={6} />
        <Dot p={sold} at={a(12, 0.1)} color={C.inkOnNavy} />
        <Dot p={UP1} at={a(12, 0.5)} color={C.gain} />
        <Dot p={END} at={a(13, 0.35)} color={C.gain} />
      </Layer>
      <PtLabel p={sold} at={a(12, 0.1)} anchor="bottom">
        <Label size={40}>{F.crashDay.v} · 다 판 날</Label>
      </PtLabel>
      <PtLabel p={UP1} at={a(12, 0.5)} anchor="top">
        <Label size={36} weight={500}>
          다음 날
        </Label>
        <Label size={60} weight={900} color={C.gain}>
          +{F.nextDayRise.v}% 넘게
        </Label>
      </PtLabel>
      <PtLabel p={END} at={a(13, 0.4)} anchor="top">
        <Label size={36} weight={500}>
          {F.weeks7.v} · 판 가격보다
        </Label>
        <Label size={64} weight={900} color={C.gain}>
          <Hi at={a(13, 0.6)}>+{F.rise30.v}% 넘게</Hi>
        </Label>
      </PtLabel>
      <CornerNote at={a(12)}>실제 종가 흐름 · 일부 날짜만 연결</CornerNote>
    </>
  );
};

// S06 문장 15–16 (네이비): "시장이 빼앗아 감"(취소선) → 겁에 질려 내던진 800만 원 → 다음 날 빨갛게 오른 주가를 보는 휴대폰
export const S06: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const out = a(16);
  const line: P[] = [
    [20, 150],
    [90, 132],
    [150, 90],
    [220, 70],
    [300, 22],
  ];
  return (
    <>
      <div style={{position: "absolute", inset: 0, opacity: fadeOut(f, out)}}>
        <Box x={150} y={360}>
          <div style={vis(f, a(15))}>
            <Label size={60} weight={900} color={C.gray}>
              <StrikeAt at={a(15, 0.3)} color={C.inkOnNavy}>
                시장이 빼앗아 감
              </StrikeAt>
            </Label>
          </div>
        </Box>
        <Box x={1000} y={250}>
          <div style={vis(f, a(15, 0.45))}>
            <Label size={52}>
              겁에 질려 <Hi at={a(15, 0.65)} until={out}>내던진</Hi>
            </Label>
            <div style={{marginTop: 20, display: "inline-block", background: C.loss, color: "#FFFFFF", borderRadius: 18, padding: "16px 40px"}}>
              <Big size={180}>{won(F.thrown.v)}</Big>
            </div>
          </div>
        </Box>
      </div>
      <Box x={710} y={190}>
        <Phone at={a(16, 0.05)} w={500} h={590}>
          <Label size={36} weight={500} color={C.gray}>
            {F.company.v} · 다음 날
          </Label>
          <Big size={130} color={C.gain} style={{marginTop: 18}}>
            +{F.nextDayRise.v}%
          </Big>
          <svg width={340} height={170} style={{marginTop: 30, overflow: "visible"}}>
            <path
              d={line.map((q, i) => `${i ? "L" : "M"} ${q[0]} ${q[1]}`).join(" ")}
              stroke={C.gain}
              strokeWidth={10}
              fill="none"
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeDasharray={420}
              strokeDashoffset={420 * (1 - prog(f, a(16, 0.2), 24))}
            />
          </svg>
        </Phone>
      </Box>
    </>
  );
};
