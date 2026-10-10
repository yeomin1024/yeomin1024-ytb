// 문제 분석 파트 S11–S22 (자막 24–58)
import React from "react";
import {interpolate, useCurrentFrame} from "remotion";
import {C, SERIF} from "../../../design/tokens";
import {count, enter, prog} from "../../../components/anim";
import {eokMan, num, won} from "../../../components/fmt";
import {Big, Box, Caption, Card, Chip, CornerNote, Headline, Hi, Label, Mark, fadeOut, vis} from "../../../components/ui";
import {AccountCard, NewsCard, NumberTitle} from "../../../components/cards";
import {Bars, Dot, HRule, Layer, Line, P, PtLabel, YearLine} from "../../../components/charts";
import {Balance, Stack, Weight} from "../../../components/objects";
import {F} from "../facts";
import {SceneC} from "./story";

const ADD = "#5A5751"; // S03 계좌 카드의 물타기 조각 색과 같음
const STATIC = -60; // 같은 항목의 이어지는 장면: 번호 타이틀이 이미 떠 있음
const LIGHT_LOSS = "#9DB7EA"; // 비교 대상(물타기 안 했을 때)의 손실 막대

// 번호 타이틀 문구 (같은 항목은 같은 문구)
const T01 = "평단은 조금, 걸린 돈은 크게";
const T02 = "떨어진 가격 ≠ 싼 가격";
const T03 = "손실 종목을 너무 오래 붙잡는다";
const T04 = "만회하려는 물타기, 멈추기 어렵다";

// S11 문장 24–25: "01" → 사연 계좌 카드(간단형)에 물타기 3,000만 원이 더해짐
export const S11: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const grow = prog(f, a(25, 0.45), 22);
  return (
    <>
      <NumberTitle
        no="01"
        at={a(24)}
        title={
          <>
            평단은 조금, 걸린 돈은 <Hi at={a(24, 0.75)}>크게</Hi>
          </>
        }
      />
      <Box x={140} y={330}>
        <div style={vis(f, a(25))}>
          <AccountCard
            compact
            total={F.saved.v}
            segs={[{v: F.first.v}, {v: F.add1.v * grow, color: ADD}, {v: F.add2.v * grow, color: ADD}]}
            stockName={F.company.v}
            pnl={null}
          />
        </div>
      </Box>
      <Box x={1250} y={400}>
        <div style={vis(f, a(25, 0.45))}>
          <Chip size={50}>물타기 {won(F.added.v, true)}</Chip>
        </div>
      </Box>
    </>
  );
};

// S12 문장 26–27: 화면 분할 — 평단 428→415달러(약 -3%) vs 걸린 돈 5,000만→8,000만 원(+60%)
export const S12: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const avg = count(f, a(26, 0.45), F.avgFrom.v, F.avgTo.v);
  const inv = count(f, a(27, 0.5), F.first.v, F.investedTo.v);
  const BW = 700;
  return (
    <>
      <NumberTitle no="01" at={STATIC} title={T01} />
      <div style={{position: "absolute", left: 959, top: 290, width: 4, height: 440, background: C.gray, opacity: enter(f, a(27))}} />
      <Box x={140} y={300} w={760}>
        <div style={vis(f, a(26))}>
          <Label size={48}>평단</Label>
          <Big size={130} style={{marginTop: 12}}>
            {num(avg)}달러
          </Big>
          <div style={{marginTop: 30, height: 44, width: (BW * avg) / F.avgFrom.v, background: C.gray, borderRadius: 8}} />
          <div style={{marginTop: 24, opacity: enter(f, a(26, 0.7))}}>
            <Chip variant="gray" size={44}>
              약 -{F.avgDrop.v}%
            </Chip>
          </div>
        </div>
      </Box>
      <Box x={1020} y={300} w={760}>
        <div style={vis(f, a(27))}>
          <Label size={48}>한 종목에 걸린 돈</Label>
          <Big size={130} style={{marginTop: 12}}>
            {won(inv)}
          </Big>
          <div style={{marginTop: 30, height: 44, width: (BW * inv) / F.investedTo.v, background: C.ink, borderRadius: 8}} />
          <div style={{marginTop: 24, opacity: enter(f, a(27, 0.75))}}>
            <Label size={64} weight={900}>
              <Hi at={a(27, 0.85)}>+{F.investedUp.v}%</Hi>
            </Label>
          </div>
        </div>
      </Box>
    </>
  );
};

// S13 문장 28–29: 폭락한 날 손실 막대 (물타기 함 -2,000만 vs 안 함) 차이 600만 원+ → 같은 종목에 쌓이는 돈
export const S13: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  const out = a(29);
  const baseY = 715;
  const maxH = 310;
  const hR = Math.abs(F.noAvgLoss.v) / Math.abs(F.pnlCrash.v); // 1,400 / 2,000 (계산, 숫자는 표시 안 함)
  const topL = baseY - maxH;
  const topR = baseY - maxH * hR;
  const bx = 1390;
  const bp = prog(f, b(28), 12);
  return (
    <>
      <NumberTitle no="01" at={STATIC} title={T01} />
      <div style={{position: "absolute", inset: 0, opacity: fadeOut(f, out)}}>
        <Box x={1120} y={262} w={800}>
          <div style={vis(f, a(28))}>
            <Label size={40} color={C.gray}>
              폭락한 날 손실
            </Label>
          </div>
        </Box>
        <Bars
          x={500}
          baseY={baseY}
          maxH={maxH}
          barW={260}
          gap={320}
          items={[
            {h: 1, color: C.loss, label: "물타기 함", at: a(28, 0.05), top: <Label size={56} weight={900} color={C.loss}>{won(F.pnlCrash.v)}</Label>},
            {h: hR, color: LIGHT_LOSS, label: "물타기 안 함", at: a(28, 0.3)},
          ]}
        />
        <div style={{position: "absolute", left: 760, top: topL - 3, width: (bx - 760) * bp, borderTop: `5px dashed ${C.loss}`}} />
        <div style={{position: "absolute", left: bx - 3, top: topL, width: 6, height: (topR - topL) * bp, background: C.loss}} />
        <Box x={bx + 30} y={(topL + topR) / 2 - 36}>
          <div style={vis(f, b(28, 0.1))}>
            <Label size={48} weight={900}>
              <Hi at={b(28, 0.3)} until={out}>
                {F.extraLoss.v}만 원 넘게 ↑
              </Hi>
            </Label>
          </div>
        </Box>
      </div>
      <div style={{position: "absolute", inset: 0, opacity: enter(f, out)}}>
        <Stack
          x={420}
          baseY={700}
          w={500}
          unit={0.05}
          base={<Label size={40}>같은 종목</Label>}
          blocks={[
            {v: F.first.v, label: `처음 ${won(F.first.v)}`, at: a(29, 0.05)},
            {v: F.add1.v, label: won(F.add1.v, true), at: a(29, 0.3), color: ADD},
            {v: F.add2.v, label: won(F.add2.v, true), at: a(29, 0.42), color: ADD},
          ]}
        />
        <Box x={1060} y={360} w={760}>
          <div style={vis(f, a(29, 0.1))}>
            <Headline size={72}>평단 낮추기</Headline>
          </div>
          <div style={vis(f, a(29, 0.55))}>
            <Headline size={72}>
              = <Hi at={a(29, 0.7)}>돈을 더 거는 일</Hi>
            </Headline>
          </div>
        </Box>
      </div>
    </>
  );
};

// S14 문장 30–31: "02" → 떨어지는 선(개념도)과 "이유?"
export const S14: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const pts: P[] = [
    [260, 330],
    [520, 400],
    [640, 380],
    [900, 560],
    [1060, 540],
    [1400, 700],
  ];
  return (
    <>
      <NumberTitle
        no="02"
        at={a(30)}
        title={
          <>
            떨어진 가격 ≠ <Hi at={a(30, 0.65)}>싼 가격</Hi>
          </>
        }
      />
      <Layer>
        <Line pts={pts} at={a(31)} dur={26} color={C.loss} />
      </Layer>
      <PtLabel p={[1060, 540]} at={a(31, 0.55)} anchor="top" gap={40}>
        <Card style={{padding: "18px 40px"}}>
          <Headline size={72}>이유?</Headline>
        </Card>
      </PtLabel>
      <CornerNote at={a(31)}>개념도</CornerNote>
    </>
  );
};

// 사례 카드 (날짜 · 하락률 · 원인) — 자막 순서대로 채움
const CaseCard: React.FC<{x: number; date: string; pct: number; approx?: boolean; cause: React.ReactNode; at: number; pctAt: number; causeAt: number}> = ({
  x,
  date,
  pct,
  approx,
  cause,
  at,
  pctAt,
  causeAt,
}) => {
  const f = useCurrentFrame();
  const v = count(f, pctAt, 0, -pct);
  return (
    <Box x={x} y={280}>
      <div style={vis(f, at)}>
        <Card style={{width: 520, height: 370, boxSizing: "border-box"}}>
          <div style={{display: "inline-block", background: C.ink, color: C.light, fontWeight: 700, fontSize: 34, padding: "6px 20px", borderRadius: 8}}>{date}</div>
          <div style={{display: "flex", alignItems: "baseline", gap: 12, marginTop: 18, opacity: enter(f, pctAt)}}>
            {approx ? <Label size={44}>약</Label> : null}
            <Big size={120} color={C.loss}>
              {num(v)}%
            </Big>
          </div>
          <div style={{marginTop: 20, opacity: enter(f, causeAt)}}>
            <Label size={40}>{cause}</Label>
          </div>
        </Card>
      </div>
    </Box>
  );
};

// S15 문장 32–36: 사례 카드 3장 — 4월 17일 -22% / 5월 13일 약 -18% / 5월 15일 약 -11% + 메디케어 사기 혐의
export const S15: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  return (
    <>
      <NumberTitle no="02" at={STATIC} title={T02} />
      <CaseCard x={140} date={F.d1.v} pct={F.drop1.v} cause="실적 전망 하향" at={a(32)} causeAt={b(32)} pctAt={b(32, 0.45)} />
      <CaseCard
        x={700}
        date={F.d2.v}
        pct={F.drop2.v}
        approx
        cause={
          <>
            전망 철회
            <br />
            CEO 사임
          </>
        }
        at={a(33)}
        causeAt={a(33, 0.25)}
        pctAt={b(33, 0.1)}
      />
      <CaseCard x={1260} date={F.d3.v} pct={F.drop3.v} approx cause="법무부 수사 보도" at={a(34)} pctAt={a(34, 0.35)} causeAt={a(35)} />
      <div style={{position: "absolute", right: 140, top: 690, ...vis(f, a(36))}}>
        <Chip variant="outline" size={38}>
          메디케어(노인 의료보험) 관련 사기 혐의
        </Chip>
      </div>
    </>
  );
};

// S16 문장 37–39: 실제 주가 흐름 585달러 → 274달러(절반 아래) → 2026년 10월 376달러, 평단 415달러 점선
const yv = (v: number) => 720 - (v - 250) * 1.2;
const CRASH: P[] = [
  [220, yv(585.04)], // 4/16
  [330, yv(454.11)], // 4/17
  [450, yv(427.96)], // 4/23
  [560, yv(411.44)], // 4/30
  [680, yv(380.64)], // 5/9
  [760, yv(378.75)], // 5/12
  [840, yv(311.38)], // 5/13
  [960, yv(274.35)], // 5/15
];
export const S16: SceneC = ({t}) => {
  const {a} = t;
  const end = CRASH[CRASH.length - 1];
  const now: P = [1560, yv(376.32)];
  return (
    <>
      <NumberTitle no="02" at={STATIC} title={T02} />
      <Layer>
        <Line pts={CRASH} at={a(37, 0.1)} dur={40} color={C.loss} />
        <Line pts={[end, now]} at={a(38)} dashed width={6} />
        <Dot p={CRASH[0]} at={a(37, 0.1)} color={C.loss} />
        <Dot p={end} at={a(37, 0.55)} color={C.loss} />
        <Dot p={now} at={a(38, 0.5)} color={C.loss} />
      </Layer>
      <PtLabel p={CRASH[0]} at={a(37, 0.1)} anchor="right">
        <Label size={48} weight={900}>
          {F.p585.v}달러
        </Label>
      </PtLabel>
      <PtLabel p={end} at={a(37, 0.55)} anchor="right">
        <div style={{textAlign: "left"}}>
          <Label size={48} weight={900} color={C.loss}>
            {F.p274.v}달러
          </Label>
          <Label size={40}>
            한 달 만에 <Hi at={a(37, 0.8)} until={a(38)}>절반 아래</Hi>
          </Label>
        </div>
      </PtLabel>
      <PtLabel p={[(end[0] + now[0]) / 2, (end[1] + now[1]) / 2]} at={a(38)} anchor="top" gap={14}>
        <Caption>1년 반</Caption>
      </PtLabel>
      <PtLabel p={now} at={a(38, 0.5)} anchor="bottom">
        <Label size={36} weight={500}>
          {F.now.v}
        </Label>
        <Label size={48} weight={900}>
          <Hi at={a(39, 0.55)}>{F.p376.v}달러</Hi>
        </Label>
      </PtLabel>
      <HRule y={yv(F.avgTo.v as number)} x0={200} x1={1720} at={a(39)} labelAt="aboveEnd">
        <Label size={42}>평단 {F.avgTo.v}달러</Label>
      </HRule>
      <CornerNote at={a(37)}>실제 주가 흐름 · 날짜 간격은 실제와 다름</CornerNote>
    </>
  );
};

// S17 문장 40–42: "03" → 연구 카드 (테런스 오딘 교수 · 계좌 1만 개 · 1987년부터 7년)
export const S17: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  return (
    <>
      <NumberTitle
        no="03"
        at={a(40)}
        title={
          <>
            손실 종목을 <Hi at={a(40, 0.6)}>너무 오래</Hi> 붙잡는다
          </>
        }
      />
      <Box x={360} y={300}>
        <div style={vis(f, a(41))}>
          <Card style={{width: 1200, padding: "40px 56px"}}>
            <Label size={44}>
              {F.odean.v} 교수 · {F.odeanOrg.v}
            </Label>
            <div style={{display: "flex", alignItems: "baseline", gap: 24, marginTop: 18, opacity: enter(f, b(41))}}>
              <Label size={56} weight={700}>
                개인 투자자 계좌
              </Label>
              <Big size={170}>{F.accounts.v}</Big>
            </div>
            <div style={{marginTop: 26, ...vis(f, a(42))}}>
              <Chip size={42}>
                {F.odeanFrom.v}년부터 · {F.odeanYears.v}년 거래 기록
              </Chip>
            </div>
          </Card>
        </div>
      </Box>
    </>
  );
};

// S18 문장 43–45: 파는 비율 (손실 종목 vs 수익 종목 1.5배) → 그 뒤 1년 수익률 차이 3.4%p (개념도)
export const S18: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const sw = a(44);
  const baseY = 690;
  const maxH = 360;
  const hL = 0.45;
  const hR = 0.8;
  const topL = baseY - maxH * hL;
  const topR = baseY - maxH * hR;
  const bx = 1400;
  const bp = prog(f, a(45, 0.5), 12);
  return (
    <>
      <NumberTitle no="03" at={STATIC} title={T03} />
      <div style={{position: "absolute", inset: 0, opacity: fadeOut(f, sw)}}>
        <Box x={960} y={250} w={800} center>
          <Label size={44} color={C.gray}>
            파는 비율
          </Label>
        </Box>
        <Bars
          x={560}
          baseY={baseY}
          maxH={maxH}
          barW={260}
          gap={280}
          items={[
            {h: 0.55, color: C.loss, label: "손실 난 종목", at: a(43, 0.45)},
            {h: 0.55 * F.sellRatio.v, color: C.gain, label: "수익 난 종목", at: a(43, 0.05), top: <Label size={64} weight={900}><Hi at={a(43, 0.8)} until={sw}>{F.sellRatio.v}배</Hi></Label>},
          ]}
        />
      </div>
      <div style={{position: "absolute", inset: 0, opacity: enter(f, sw)}}>
        <Box x={960} y={250} w={800} center>
          <Label size={44} color={C.gray}>
            그 뒤 1년 수익률
          </Label>
        </Box>
        <Bars
          x={560}
          baseY={baseY}
          maxH={maxH}
          barW={260}
          gap={280}
          items={[
            {h: hL, color: C.loss, label: "붙잡은 손실 종목", at: a(45)},
            {h: hR, color: C.gain, label: "판 수익 종목", at: sw + 6},
          ]}
        />
        <div style={{position: "absolute", left: 820, top: topL - 3, width: (bx - 820) * bp, borderTop: `5px dashed ${C.ink}`}} />
        <div style={{position: "absolute", left: bx - 3, top: topR, width: 6, height: (topL - topR) * bp, background: C.ink}} />
        <Box x={bx + 30} y={(topL + topR) / 2 - 36}>
          <div style={vis(f, a(45, 0.55))}>
            <Label size={52} weight={900}>
              <Hi at={a(45, 0.65)}>{F.gap.v}%p 더 높음</Hi>
            </Label>
          </div>
        </Box>
        <CornerNote at={sw}>개념도 · 출처: {F.odean.v} 교수 연구</CornerNote>
      </div>
    </>
  );
};

// S19 문장 46–47: 천칭 저울 — "본전 기다림"이 "수익"보다 무거움 → 물타기 돈이 더 얹혀 더 기울어짐
export const S19: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const angle = interpolate(f, [a(46, 0.2), a(46, 0.5), a(47, 0.5), a(47, 0.75)], [0, 11, 11, 19], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const shrink = prog(f, a(46, 0.7), 15);
  return (
    <>
      <NumberTitle no="03" at={STATIC} title={T03} />
      <Balance
        cx={960}
        cy={400}
        angle={angle}
        at={a(46)}
        left={
          <>
            <Weight at={a(47, 0.45)} color={ADD}>
              + 물타기 돈
            </Weight>
            <Weight at={a(46)}>본전 기다림</Weight>
          </>
        }
        right={
          <Weight at={a(46, 0.3)} color={C.gain} textColor="#FFFFFF" w={340 - 120 * shrink}>
            수익{shrink > 0.5 ? " ↓" : ""}
          </Weight>
        }
      />
    </>
  );
};

// S20 문장 48–51 (네이비): "04" → 1995 베어링스 은행 붕괴 → 1762~1995 233년 → 닉 리슨, 손실 날 때마다 베팅 ↑ (개념도)
const BETS = [70, 120, 190, 270];
const BetBars: React.FC<{at: number[]; extra?: {h: number; at: number}}> = ({at, extra}) => {
  const f = useCurrentFrame();
  const list = [...BETS.map((h, i) => ({h, at: at[i]})), ...(extra ? [extra] : [])];
  return (
    <>
      {list.map((b, i) => {
        const h = b.h * prog(f, b.at, 14);
        return <div key={i} style={{position: "absolute", left: 1120 + i * 135, top: 740 - h, width: 100, height: h, background: i === 4 ? C.inkOnNavy : "rgba(247,243,234,0.6)", borderRadius: "8px 8px 0 0"}} />;
      })}
      <div style={{position: "absolute", left: 1090, top: 740, width: list.length * 135 + 30, height: 6, background: C.inkOnNavy, opacity: enter(f, at[0])}} />
    </>
  );
};
export const S20: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  const bet0 = b(51);
  return (
    <>
      <NumberTitle no="04" at={a(48)} title={T04} />
      <Box x={140} y={290}>
        <div style={vis(f, a(49))}>
          <NewsCard date={`${F.baringsYear.v}년`} title="영국 베어링스 은행 붕괴" width={820} />
        </div>
      </Box>
      <div style={{opacity: fadeOut(f, a(51))}}>
        <YearLine x0={1100} x1={1700} y={430} from={`${F.baringsFounded.v}년`} to={`${F.baringsYear.v}년`} at={a(50)} mid={<Big size={100}>{F.baringsAge.v}년</Big>} />
      </div>
      <Box x={140} y={560}>
        <div style={vis(f, a(51))}>
          <Label size={40} weight={500}>
            싱가포르 지점 · {F.leesonAge.v}살 트레이더
          </Label>
          <Label size={64} weight={900}>
            닉 리슨
          </Label>
        </div>
      </Box>
      <Box x={1120} y={340}>
        <div style={vis(f, bet0)}>
          <Label size={40}>손실 날 때마다 베팅 ↑</Label>
        </div>
      </Box>
      <BetBars at={BETS.map((_, i) => bet0 + i * 8)} />
      <CornerNote at={bet0} y={770}>
        개념도
      </CornerNote>
    </>
  );
};

// S21 문장 52–55 (네이비): 1995년 1월 고베 대지진 → 손절 안 함 → 반등에 더 크게 → -8억 2,700만 파운드, 1파운드에 매각 → 본전 생각
export const S21: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  const out = a(54);
  const loss = count(f, a(54, 0.1), 0, -F.baringsLoss.v, 28);
  return (
    <>
      <NumberTitle no="04" at={STATIC} title={T04} />
      <div style={{position: "absolute", inset: 0, opacity: fadeOut(f, out)}}>
        <Box x={140} y={290}>
          <div style={vis(f, a(52))}>
            <NewsCard date={`${F.baringsYear.v}년 1월`} title="일본 고베 대지진" sub={<span style={{opacity: enter(f, b(52))}}>→ 일본 주가 급락</span>} width={860}>
              <div style={{display: "flex", alignItems: "center", gap: 16, marginTop: 22, opacity: enter(f, b(52, 0.5))}}>
                <Mark kind="cross" at={b(52, 0.5)} size={56} color={C.ink} />
                <Label size={44}>손절 안 함</Label>
              </div>
            </NewsCard>
          </div>
        </Box>
        <Box x={1120} y={250}>
          <div style={vis(f, a(53, 0.3))}>
            <Label size={40}>반등에 더 크게</Label>
          </div>
        </Box>
        <BetBars at={BETS.map(() => STATIC)} extra={{h: 380, at: a(53, 0.3)}} />
      </div>
      <Box x={960} y={290} w={1700} center>
        <div style={{...vis(f, out), display: "inline-block", background: C.loss, color: "#FFFFFF", borderRadius: 18, padding: "18px 44px"}}>
          <Big size={140}>{eokMan(loss)} 파운드</Big>
        </div>
      </Box>
      <Box x={960} y={510} w={1200} center>
        <div style={vis(f, b(54))}>
          <Chip size={46}>은행은 단돈 {F.soldFor.v}에 매각</Chip>
        </div>
      </Box>
      <Box x={960} y={640} w={1500} center>
        <div style={vis(f, a(55, 0.3))}>
          <Headline size={72}>
            <Hi at={a(55, 0.5)}>본전 생각</Hi> 앞에서 못 멈춤
          </Headline>
        </div>
      </Box>
    </>
  );
};

// S22 문장 56–58: 갈림길(개념도) — 통한 경우(위, 빨강) / 결과는 미리 모름(?) → "물타기·손절, 어떤 기준으로?"
export const S22: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const out = a(58);
  const fork: P = [820, 470];
  return (
    <>
      <div style={{position: "absolute", inset: 0, opacity: fadeOut(f, out)}}>
        <Layer>
          <Line pts={[[260, 470], fork]} at={a(56)} dur={16} />
          <Line pts={[fork, [1100, 380], [1400, 250]]} at={a(56, 0.3)} dur={22} color={C.gain} />
          <Line pts={[fork, [1100, 560], [1400, 690]]} at={a(57)} dur={22} color={C.loss} />
        </Layer>
        <PtLabel p={[1400, 250]} at={a(56, 0.55)} anchor="right">
          <div style={{display: "flex", alignItems: "center", gap: 14}}>
            <Mark kind="check" at={a(56, 0.55)} size={60} color={C.gain} />
            <Label size={48}>통한 경우</Label>
          </div>
        </PtLabel>
        <div
          style={{
            position: "absolute",
            left: fork[0] - 70,
            top: fork[1] - 70,
            width: 140,
            height: 140,
            borderRadius: 99,
            background: C.ink,
            color: C.light,
            fontFamily: SERIF,
            fontWeight: 900,
            fontSize: 96,
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            ...vis(f, a(57, 0.35)),
          }}
        >
          ?
        </div>
        <PtLabel p={fork} at={a(57, 0.45)} anchor="bottom" gap={92}>
          <Label size={46}>결과는 미리 모름</Label>
        </PtLabel>
        <CornerNote at={a(56)}>개념도</CornerNote>
      </div>
      <Box x={960} y={300} w={1600} center>
        <div style={vis(f, out)}>
          <Headline size={88}>물타기 · 손절</Headline>
        </div>
        <div style={vis(f, a(58, 0.35))}>
          <Headline size={88}>
            <Hi at={a(58, 0.6)}>어떤 기준</Hi>으로?
          </Headline>
        </div>
      </Box>
    </>
  );
};
