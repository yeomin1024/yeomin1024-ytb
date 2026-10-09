// 올바른 방법 파트 S23–S31 (자막 59–91), 밝은 크림 배경
import React from "react";
import {useCurrentFrame} from "remotion";
import {C} from "../../../design/tokens";
import {count, enter, prog} from "../../../components/anim";
import {num, won} from "../../../components/fmt";
import {Arrow, Big, Box, Card, Chip, CornerNote, Headline, Hi, Label, Mark, Strike, fadeOut, vis} from "../../../components/ui";
import {AmountBar, Note, NumberTitle} from "../../../components/cards";
import {Dot, HRule, Layer, Line, P, PtLabel} from "../../../components/charts";
import {CheckRow, Phone, Toggle} from "../../../components/objects";
import {F} from "../facts";
import {SceneC} from "./story";

const STATIC = -60;
const T4 = "손절 가격을 미리 정하고 지키기";
const T5 = (at?: number) => (
  <>
    {at === undefined ? "세 가지" : <Hi at={at}>세 가지</Hi>}가 맞을 때만, 정한 금액 안에서
  </>
);

// S23 자막 59–63: "첫째" → 메모 카드 2장: 사연자의 이유(✗ 판단 못 함) vs 실적이 좋아질 것(✓ 기준) → 5월 13일 이유 깨짐
export const S23: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  return (
    <>
      <NumberTitle no="첫째" at={a(59)} title="사기 전에, 산 이유를 한 줄로" />
      <Box x={140} y={290}>
        <div style={vis(f, a(59, 0.5))}>
          <Note
            head="사연자의 산 이유"
            width={780}
            textP={prog(f, a(60, 0.15), 22)}
            text="큰 회사라 망하지 않는다"
          >
            <div style={{marginTop: 22, display: "flex", flexDirection: "column", gap: 14}}>
              <div style={{display: "flex", alignItems: "center", gap: 16, ...vis(f, a(61, 0.2))}}>
                <Mark kind="cross" at={a(61, 0.35)} size={50} color={C.loss} />
                <Label size={42}>지금 가격이 싼지</Label>
              </div>
              <div style={{display: "flex", alignItems: "center", gap: 16, ...vis(f, a(61, 0.5))}}>
                <Mark kind="cross" at={a(61, 0.65)} size={50} color={C.loss} />
                <Label size={42}>언제 다시 오를지</Label>
              </div>
            </div>
          </Note>
        </div>
      </Box>
      <Box x={1000} y={290}>
        <div style={vis(f, a(62))}>
          <Note
            head="이렇게 적었다면"
            width={780}
            textP={prog(f, a(62, 0.1), 22)}
            text={<Strike at={a(63, 0.6)}>실적이 다시 좋아질 것</Strike>}
          >
            <div style={{marginTop: 22, display: "flex", alignItems: "center", gap: 16, ...vis(f, a(62, 0.7))}}>
              <Mark kind="check" at={a(62, 0.75)} size={50} color={C.ink} />
              <Label size={42}>기준이 생김</Label>
            </div>
          </Note>
        </div>
      </Box>
      <Box x={1000} y={680}>
        <div style={{display: "flex", alignItems: "center", gap: 20}}>
          <div style={vis(f, a(63, 0.05))}>
            <Chip size={40}>{F.d2.v} 실적 전망 철회</Chip>
          </div>
          <div style={vis(f, a(63, 0.6))}>
            <Label size={46} weight={900}>
              → <Hi at={a(63, 0.7)}>이유가 깨짐</Hi>
            </Label>
          </div>
        </div>
      </Box>
    </>
  );
};

// 작은 선 차트 패널 (S24·S29에서 같은 모양으로 재사용): 패널 안 좌표 680×230
type Series = {pts: P[]; color: string; at: number; dur?: number};
const Panel: React.FC<{x: number; y: number; title: React.ReactNode; at: number; series: Series[]; h?: number; children?: React.ReactNode}> = ({x, y, title, at, series, h = 400, children}) => {
  const f = useCurrentFrame();
  return (
    <Box x={x} y={y}>
      <div style={vis(f, at)}>
        <Card style={{width: 760, height: h, boxSizing: "border-box", position: "relative", padding: "28px 40px"}}>
          <Label size={44}>{title}</Label>
          <svg width={680} height={230} style={{position: "absolute", left: 40, top: 110, overflow: "visible"}}>
            {series.map((s, i) => {
              const L = s.pts.slice(1).reduce((acc, p, k) => acc + Math.hypot(p[0] - s.pts[k][0], p[1] - s.pts[k][1]), 0);
              const p = prog(f, s.at, s.dur ?? 24);
              return (
                <path
                  key={i}
                  d={s.pts.map((q, k) => `${k ? "L" : "M"} ${q[0]} ${q[1]}`).join(" ")}
                  stroke={s.color}
                  strokeWidth={8}
                  fill="none"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeDasharray={L + 1}
                  strokeDashoffset={(L + 1) * (1 - p)}
                  opacity={p > 0 ? 1 : 0}
                />
              );
            })}
          </svg>
          {children}
        </Card>
      </div>
    </Box>
  );
};
const flat = (y: number, wob: number[]): P[] => wob.map((w, i) => [i * (680 / (wob.length - 1)), y + w]);

// S24 자막 64–67: "둘째" → 패널 2개: 그 회사만 떨어짐(왼쪽) vs 시장 전체가 함께(오른쪽) → 4월 17일 → 4월 23일 엿새 뒤 → 물타기 ✗
export const S24: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const rightAt = a(65, 0.05);
  const leftAt = a(65, 0.5);
  const down = (y0: number, k: number): P[] => [
    [0, y0],
    [170, y0 + 30 * k],
    [340, y0 + 70 * k],
    [510, y0 + 100 * k],
    [680, y0 + 150 * k],
  ];
  return (
    <>
      <NumberTitle no="둘째" at={a(64)} title="물타기 전에, 떨어진 이유부터" />
      <Panel
        x={140}
        y={280}
        at={leftAt}
        title="그 회사만"
        series={[
          {pts: flat(40, [0, 8, -6, 4, 0]), color: C.gray, at: leftAt},
          {pts: flat(90, [0, -6, 6, -4, 2]), color: C.gray, at: leftAt},
          {pts: flat(140, [0, 6, -4, 8, 0]), color: C.gray, at: leftAt},
          {pts: down(30, 1.2), color: C.loss, at: leftAt + 6},
        ]}
      >
        <div style={{position: "absolute", right: 30, top: 24, display: "flex", alignItems: "center", gap: 10, ...vis(f, a(67, 0.45))}}>
          <Mark kind="cross" at={a(67, 0.45)} size={56} color={C.loss} />
          <Label size={44} weight={900}>
            물타기 안 함
          </Label>
        </div>
      </Panel>
      <Panel
        x={1020}
        y={280}
        at={rightAt}
        title="시장 전체가 함께"
        series={[
          {pts: down(10, 0.9), color: C.loss, at: rightAt},
          {pts: down(50, 0.9), color: C.loss, at: rightAt + 3},
          {pts: down(90, 0.8), color: C.loss, at: rightAt + 6},
          {pts: down(40, 1.0), color: C.loss, at: rightAt + 9},
        ]}
      />
      <Box x={140} y={710}>
        <div style={{display: "flex", alignItems: "center", gap: 18, ...vis(f, a(66))}}>
          <Chip size={38}>{F.d1.v} 실적 전망 ↓</Chip>
          <Arrow dir="right" len={80} at={a(66, 0.3)} stroke={6} />
          <Chip variant="outline" size={38}>
            {F.firstBuyDay.v} 첫 매수
          </Chip>
          <div style={vis(f, a(66, 0.6))}>
            <Label size={40}>{F.sixDays.v}</Label>
          </div>
        </div>
      </Box>
      <CornerNote at={rightAt}>개념도</CornerNote>
    </>
  );
};

// S25 자막 68–72: "셋째" → 5월 9일 381달러 / 평단 424달러(취소선, 앞날과 무관) / 처음 본다면 1,500만 원 새로? → 산다면 그때만 물타기
export const S25: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  return (
    <>
      <NumberTitle no="셋째" at={a(68)} title="평단은 잊고, 지금 가격으로" />
      <Box x={140} y={280}>
        <div style={vis(f, a(69))}>
          <Chip size={40}>{F.lastAddDay.v} 주가</Chip>
          <Big size={160} style={{marginTop: 14}}>
            {F.p381.v}달러
          </Big>
        </div>
      </Box>
      <Box x={1000} y={300}>
        <div style={vis(f, a(70))}>
          <Label size={64} weight={900} color={C.gray}>
            <Strike at={a(70, 0.45)} color={C.ink}>
              평단 {F.avg424.v}달러
            </Strike>
          </Label>
        </div>
        <div style={{marginTop: 12, ...vis(f, a(70, 0.6))}}>
          <Label size={44}>회사의 앞날과 상관없음</Label>
        </div>
      </Box>
      <Box x={140} y={580}>
        <div style={vis(f, a(71))}>
          <Card style={{width: 1640, padding: "26px 44px", display: "flex", alignItems: "center", justifyContent: "space-between"}}>
            <Label size={46}>
              처음 본다면, {F.p381.v}달러에 {won(F.add2.v)}을 새로 넣을까?
            </Label>
            <div style={{display: "flex", alignItems: "center", gap: 12, ...vis(f, a(72, 0.6))}}>
              <Mark kind="check" at={a(72, 0.65)} size={54} color={C.ink} />
              <Label size={46} weight={900}>
                <Hi at={a(72, 0.75)}>산다 → 그때만</Hi>
              </Label>
            </div>
          </Card>
        </div>
      </Box>
      <Box x={180} y={712}>
        <div style={vis(f, a(72, 0.1))}>
          <Label size={38} weight={500} color={C.gray}>
            실적 전망을 낮춘 회사라는 걸 알고도
          </Label>
        </div>
      </Box>
    </>
  );
};

// S26 자막 73–76: "넷째" → 처음 산 가격 428달러 / -10% 손절 가격 385달러 → 실제 주가가 5월 9일 그 아래로
const yp = (v: number) => 360 + (428 - v) * (240 / 43); // 428 → 360, 385 → 600
export const S26: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const price: P[] = [
    [300, yp(427.96)], // 4/23
    [800, yp(411.44)], // 4/30
    [1300, yp(380.64)], // 5/9
  ];
  return (
    <>
      <NumberTitle no="넷째" at={a(73)} title={T4} />
      <HRule y={yp(428)} x0={200} x1={1500} at={a(74)} color={C.ink} />
      <HRule y={yp(385)} x0={200} x1={1500} at={a(74, 0.55)} color={C.loss} />
      <Box x={200} y={yp(428) - 66}>
        <div style={vis(f, a(74))}>
          <Label size={42}>
            처음 산 가격
            <span style={{opacity: enter(f, a(75, 0.25))}}> · {F.avgFrom.v}달러</span>
          </Label>
        </div>
      </Box>
      <Box x={200} y={yp(385) + 16}>
        <div style={vis(f, a(74, 0.55))}>
          <Label size={42} color={C.loss}>
            -{F.stopPct.v}% → 판다
            <span style={{opacity: enter(f, a(75, 0.6))}}>
              {" "}
              · <Hi at={a(75, 0.75)}>손절 가격 {F.stopPrice.v}달러</Hi>
            </span>
          </Label>
        </div>
      </Box>
      <Box x={1560} y={yp(428) - 20}>
        <Arrow dir="down" len={yp(385) - yp(428) + 10} at={a(74, 0.55)} color={C.loss} stroke={6} />
      </Box>
      <Layer>
        <Line pts={price} at={a(76)} dur={30} color={C.loss} />
        <Dot p={price[2]} at={a(76, 0.6)} color={C.loss} />
      </Layer>
      <PtLabel p={price[2]} at={a(76, 0.6)} anchor="right">
        <Label size={44} weight={900}>
          {F.lastAddDay.v}
        </Label>
      </PtLabel>
      <CornerNote at={a(76)}>실제 주가 흐름 (일부 날짜만 연결)</CornerNote>
    </>
  );
};

// S27 자막 77–80: 기준대로 팔았다면 -500만 원에서 멈춤 → 5월 9일 = 마지막 물타기 날 → 분할(기준 없음 -2,000만 vs 기준 있음 -500만) → 휴대폰 자동 매도
export const S27: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const sp = a(79);
  const ph = a(80);
  const lossL = count(f, a(79, 0.25), 0, F.pnlCrash.v);
  const lossR = count(f, a(79, 0.25), 0, F.stopLoss.v);
  return (
    <>
      <NumberTitle no="넷째" at={STATIC} title={T4} />
      <div style={{position: "absolute", inset: 0, opacity: fadeOut(f, sp)}}>
        <Box x={960} y={280} w={1400} center>
          <div style={vis(f, a(77))}>
            <Label size={46}>물타기 없이 기준대로 팔았다면</Label>
          </div>
          <div style={{display: "flex", justifyContent: "center", alignItems: "baseline", gap: 24, marginTop: 20, ...vis(f, a(77, 0.55))}}>
            <Big size={180} color={C.loss}>
              {won(F.stopLoss.v)}
            </Big>
            <Label size={52}>에서 멈춤</Label>
          </div>
        </Box>
        <Box x={960} y={640} w={1400} center>
          <div style={vis(f, a(78, 0.3))}>
            <Chip size={44}>{F.lastAddDay.v} = 마지막 물타기를 한 그날</Chip>
          </div>
        </Box>
      </div>
      <div style={{position: "absolute", inset: 0, opacity: enter(f, sp) * fadeOut(f, ph)}}>
        <div style={{position: "absolute", left: 958, top: 290, width: 4, height: 420, background: C.gray}} />
        <Box x={140} y={320} w={780} center={false}>
          <div style={{textAlign: "center", width: 780}}>
            <Label size={50}>기준 없음</Label>
            <Big size={150} color={C.loss} style={{marginTop: 20}}>
              {won(lossL)}
            </Big>
          </div>
        </Box>
        <Box x={1000} y={320}>
          <div style={{textAlign: "center", width: 780}}>
            <Label size={50}>
              <Hi at={a(79, 0.7)} until={ph}>
                기준 있음
              </Hi>
            </Label>
            <Big size={150} color={C.loss} style={{marginTop: 20}}>
              {won(lossR)}
            </Big>
          </div>
        </Box>
      </div>
      <Box x={745} y={260}>
        <Phone at={ph} h={540}>
          <Label size={34} weight={500} color={C.gray}>
            주식 앱 설정
          </Label>
          <div style={{marginTop: 40, display: "flex", alignItems: "center", justifyContent: "space-between"}}>
            <Label size={44}>자동 매도</Label>
            <Toggle onAt={a(80, 0.55)} />
          </div>
          <div style={{marginTop: 34, borderTop: `3px solid #D6D1C6`, paddingTop: 30, opacity: enter(f, a(80, 0.6))}}>
            <Label size={34} weight={500} color={C.gray}>
              손절 가격
            </Label>
            <Label size={52} weight={900} color={C.loss}>
              {F.stopPrice.v}달러
            </Label>
          </div>
        </Phone>
      </Box>
    </>
  );
};

// S28 자막 81–82: "다섯째" → 체크리스트 3개 (산 이유 그대로 / 시장 전체가 함께 하락 / 지금 가격에서 새로 사도 됨)
export const S28: SceneC = ({t}) => {
  const {a} = t;
  return (
    <>
      <NumberTitle no="다섯째" at={a(81)} title={T5(a(81, 0.35))} />
      <Box x={330} y={320}>
        <div style={{display: "flex", flexDirection: "column", gap: 54}}>
          <CheckRow at={a(82, 0.02)} checkAt={a(82, 0.2)} size={56}>
            산 이유가 그대로
          </CheckRow>
          <CheckRow at={a(82, 0.3)} checkAt={a(82, 0.55)} size={56}>
            시장 전체가 함께 빠짐
          </CheckRow>
          <CheckRow at={a(82, 0.62)} checkAt={a(82, 0.88)} size={56}>
            지금 가격에서 새로 사도 됨
          </CheckRow>
        </div>
      </Box>
    </>
  );
};

// S29 자막 83–86: S24와 같은 패널 — S&P 500(시장 전체): 2월 고점 → 4월 초 -19% 가까이 → 6월 말 사상 최고치 / 유나이티드헬스(회사 문제): 회복 못 함
export const S29: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const rAt = a(83);
  const spxDown: P[] = [
    [20, 30],
    [150, 60],
    [260, 200],
  ];
  const spxUp: P[] = [
    [260, 200],
    [420, 110],
    [560, 60],
    [680, 20],
  ];
  const unh: P[] = [
    [20, 40],
    [140, 60],
    [200, 140],
    [330, 210],
    [500, 200],
    [680, 205],
  ];
  return (
    <>
      <NumberTitle no="다섯째" at={STATIC} title={T5()} />
      <Panel x={1020} y={280} at={rAt} title={<>S&amp;P 500 · 시장 전체</>} h={440} series={[
        {pts: spxDown, color: C.loss, at: a(84, 0.2)},
        {pts: spxUp, color: C.gain, at: a(85, 0.1), dur: 30},
      ]}>
        <div style={{position: "absolute", left: 200, top: 104, ...vis(f, a(84, 0.25))}}>
          <Caption2>2월 고점</Caption2>
        </div>
        <div style={{position: "absolute", left: 40 + 260 - 20, top: 110 + 200 + 26, ...vis(f, a(84, 0.6))}}>
          <Label size={40} weight={900} color={C.loss}>
            -{F.spxDrop.v}% 가까이
          </Label>
        </div>
        <div style={{position: "absolute", right: 34, top: 280, ...vis(f, a(85, 0.55))}}>
          <Label size={40} weight={900} color={C.gain}>
            {F.spxBack.v} 사상 최고치
          </Label>
        </div>
      </Panel>
      <Box x={1020} y={740}>
        <div style={vis(f, a(83, 0.4))}>
          <Chip size={36}>{F.spxWhen.v} · 관세 충격</Chip>
        </div>
      </Box>
      <Panel x={140} y={280} at={a(86)} title={<>{F.company.v} · 회사 문제</>} h={440} series={[{pts: unh, color: C.loss, at: a(86, 0.15), dur: 30}]}>
        <div style={{position: "absolute", right: 34, top: 110 + 205 + 30, ...vis(f, a(86, 0.65))}}>
          <Label size={40} weight={900}>
            <Hi at={a(86, 0.75)}>회복 못 함</Hi>
          </Label>
        </div>
      </Panel>
      <CornerNote at={rAt} x={900} y={740}>
        개념도
      </CornerNote>
    </>
  );
};
const Caption2: React.FC<{children: React.ReactNode}> = ({children}) => (
  <Label size={36} weight={500} color={C.gray}>
    {children}
  </Label>
);

// S30 자막 87: 예시 금액 — 처음 5,000만 원 + 물타기 1,500만 원 한 번까지 (한도 선)
export const S30: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const total = F.limitFirst.v + F.limitAdd.v;
  const W = 1300;
  const first = count(f, a(87, 0.15), 0, F.limitFirst.v, 22);
  const add = count(f, a(87, 0.6), 0, F.limitAdd.v, 18);
  const limitX = 300 + W;
  return (
    <>
      <NumberTitle no="다섯째" at={STATIC} title={T5()} />
      <Box x={300} y={290}>
        <div style={vis(f, a(87))}>
          <Chip variant="outline" size={38}>
            예시
          </Chip>
        </div>
      </Box>
      <Box x={300} y={400}>
        <div style={{opacity: enter(f, a(87, 0.1))}}>
          <AmountBar segs={[{v: first}, {v: add, color: "#5A5751"}]} total={total} width={W} height={90} cashLabel={false} />
        </div>
      </Box>
      <Box x={300} y={510}>
        <div style={vis(f, a(87, 0.15))}>
          <Label size={44}>처음 {won(F.limitFirst.v)}</Label>
        </div>
      </Box>
      <div style={{position: "absolute", right: 1920 - limitX, top: 510, textAlign: "right", ...vis(f, a(87, 0.6))}}>
        <Label size={44}>물타기 {won(F.limitAdd.v, true)}</Label>
      </div>
      <div style={{position: "absolute", left: limitX + 6, top: 350, height: 260, borderLeft: `6px dashed ${C.ink}`, opacity: enter(f, a(87, 0.75))}} />
      <div style={{position: "absolute", left: limitX - 260, top: 620, width: 520, textAlign: "center", ...vis(f, a(87, 0.8))}}>
        <Label size={50} weight={900}>
          <Hi at={a(87, 0.85)}>한 번까지</Hi>
        </Label>
      </div>
    </>
  );
};

// S31 자막 88–91: 두 열 요약 (위험한 이유 4 / 물타기·손절 기준 5) → 휴대폰 체크 (산 이유, 손절 가격) → 성공 투자
const RISKS = ["평단 조금 ↓, 걸린 돈 크게 ↑", "떨어진 가격 ≠ 싼 가격", "손실 종목을 오래 붙잡음", "만회하려다 못 멈춤"];
const RULES = ["산 이유를 한 줄로", "떨어진 이유부터 확인", "평단 잊고 지금 가격으로", "손절 가격 미리 정하기", "세 가지 + 정한 금액 안에서"];
export const S31: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const out = a(89);
  const end = t.dur - 20;
  const col = (title: string, items: string[], x: number, at0: number, numbered: (i: number) => string) => (
    <Box x={x} y={150}>
      <div style={vis(f, at0)}>
        <Card style={{width: 780, padding: "32px 44px"}}>
          <Headline size={56}>{title}</Headline>
          <div style={{marginTop: 18, display: "flex", flexDirection: "column", gap: 14}}>
            {items.map((s, i) => (
              <div key={s} style={{display: "flex", gap: 18, alignItems: "baseline", ...vis(f, at0 + 6 + i * 5)}}>
                <Label size={36} weight={900} color={C.gray}>
                  {numbered(i)}
                </Label>
                <Label size={40}>{s}</Label>
              </div>
            ))}
          </div>
        </Card>
      </div>
    </Box>
  );
  const KO = ["첫째", "둘째", "셋째", "넷째", "다섯째"];
  return (
    <>
      <div style={{position: "absolute", inset: 0, opacity: fadeOut(f, out)}}>
        {col("위험한 이유", RISKS, 140, a(88, 0.05), (i) => `0${i + 1}`)}
        {col("물타기·손절 기준", RULES, 1000, a(88, 0.5), (i) => KO[i])}
      </div>
      <div style={{position: "absolute", inset: 0, opacity: fadeOut(f, a(90))}}>
        <Box x={745} y={180}>
          <Phone at={out} h={600}>
            <Label size={34} weight={500} color={C.gray}>
              물타기 전에
            </Label>
            <div style={{marginTop: 36, display: "flex", flexDirection: "column", gap: 34}}>
              <CheckRow at={out + 6} checkAt={a(89, 0.45)} size={46} color={C.ink}>
                산 이유
              </CheckRow>
              <CheckRow at={out + 11} checkAt={a(89, 0.75)} size={46} color={C.ink}>
                손절 가격
              </CheckRow>
            </div>
            <div style={{position: "absolute", left: 34, right: 34, bottom: 40, height: 96, borderRadius: 20, background: C.ink, color: C.light, display: "flex", alignItems: "center", justifyContent: "center", fontWeight: 900, fontSize: 46, opacity: 0.35 + 0.65 * prog(f, a(89, 0.8), 10)}}>
              물타기
            </div>
          </Phone>
        </Box>
      </div>
      <Box x={960} y={380} w={1000} center>
        <div style={{...vis(f, a(90, 0.1)), opacity: enter(f, a(90, 0.1)) * fadeOut(f, end)}}>
          <Headline size={88}>성공 투자</Headline>
        </div>
      </Box>
    </>
  );
};

// 사용하지 않는 import 경고 방지용 (num은 다른 장면과 맞춰 둠)
void num;
