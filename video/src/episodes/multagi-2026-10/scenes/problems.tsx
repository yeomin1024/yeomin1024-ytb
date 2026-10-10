// 문제 분석 파트 S11–S22 (자막 24–58)
import React from "react";
import {interpolate, useCurrentFrame} from "remotion";
import {C, SERIF} from "../../../design/tokens";
import {count, enter, prog} from "../../../components/anim";
import {num, won} from "../../../components/fmt";
import {Big, Box, Caption, Card, Chip, CornerNote, Headline, Hi, Label, Mark, fadeOut, vis} from "../../../components/ui";
import {AccountCard, NumberTitle} from "../../../components/cards";
import {Bars, Dot, HRule, Layer, Line, P, PtLabel} from "../../../components/charts";
import {Balance, Stack, Weight} from "../../../components/objects";
import {F, KAKAO} from "../facts";
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

// S17 문장 40–43: "03" → 연구 카드 (자본시장연구원 · 2020년 · 개인 투자자 약 20만 명) → 산 다음 날 판 비율: 수익 난 종목 41% / 손실 난 종목 22%, 78%는 그대로 보유
const HOLD = "repeating-linear-gradient(135deg, transparent 0 12px, rgba(154,150,142,0.38) 12px 16px)"; // 판 비율 막대의 나머지 = 들고 있음 (빗금)
const SELL_X = 520;
const SELL_W = 1200;
const SellRow: React.FC<{y: number; label: string; pct: number; color: string; at: number; fillAt: number; hold?: React.ReactNode}> = ({y, label, pct, color, at, fillAt, hold}) => {
  const f = useCurrentFrame();
  const w = SELL_W * (pct / 100) * prog(f, fillAt, 18);
  return (
    <>
      <Box x={140} y={y + 24}>
        <div style={vis(f, at)}>
          <Label size={48} weight={900}>
            {label}
          </Label>
        </div>
      </Box>
      <div style={{position: "absolute", left: SELL_X, top: y, width: SELL_W, height: 110, border: `4px solid ${C.ink}`, borderRadius: 14, overflow: "hidden", background: HOLD, boxSizing: "border-box", opacity: enter(f, at)}}>
        <div style={{position: "absolute", left: 0, top: 0, bottom: 0, width: w, background: color, display: "flex", alignItems: "center", justifyContent: "center"}}>
          <Label size={52} weight={900} color="#FFFFFF" style={{whiteSpace: "nowrap", opacity: enter(f, fillAt + 8)}}>
            {pct}% 팖
          </Label>
        </div>
        {hold ? <div style={{position: "absolute", left: SELL_W * (pct / 100), right: 0, top: 0, bottom: 0, display: "flex", alignItems: "center", justifyContent: "center"}}>{hold}</div> : null}
      </div>
    </>
  );
};
export const S17: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const out = a(42);
  return (
    <>
      <NumberTitle
        no="03"
        at={a(40)}
        title={
          <>
            손실 종목을{" "}
            <Hi at={a(40, 0.6)} until={a(43)}>
              너무 오래
            </Hi>{" "}
            붙잡는다
          </>
        }
      />
      <div style={{position: "absolute", inset: 0, opacity: fadeOut(f, out)}}>
        <Box x={140} y={290}>
          <div style={vis(f, a(41))}>
            <Card style={{width: 1640, boxSizing: "border-box", padding: "34px 52px"}}>
              <div style={{display: "flex", alignItems: "center", gap: 26}}>
                <Label size={56} weight={900}>
                  {F.kcmi.v}
                </Label>
                <div style={vis(f, a(41, 0.3))}>
                  <Chip size={40}>{F.kcmiYear.v} 거래</Chip>
                </div>
              </div>
              <div style={{display: "flex", alignItems: "baseline", gap: 30, marginTop: 10, opacity: enter(f, a(41, 0.5))}}>
                <Label size={56}>개인 투자자 약</Label>
                <Big size={170}>{F.kcmiInvestors.v}</Big>
              </div>
            </Card>
          </div>
        </Box>
      </div>
      {/* 42–43: 산 다음 날 판 비율 (막대 = 그날 수익·손실 난 종목 전체, 빗금 = 들고 있음) */}
      <Box x={SELL_X} y={290}>
        <div style={{display: "flex", alignItems: "center", gap: 18, ...vis(f, out)}}>
          <Chip size={40}>{F.dayAfter.v}</Chip>
          <Label size={44}>판 비율</Label>
        </div>
      </Box>
      <SellRow y={410} label="수익 난 종목" pct={F.sellWin.v} color={C.gain} at={out} fillAt={a(42, 0.45)} />
      <SellRow
        y={590}
        label="손실 난 종목"
        pct={F.sellLoss.v}
        color={C.loss}
        at={a(43)}
        fillAt={a(43, 0.12)}
        hold={
          <div style={vis(f, a(43, 0.5))}>
            <Label size={52} weight={900}>
              <Hi at={a(43, 0.65)}>
                {F.holdLoss.v}% 그대로 보유
              </Hi>
            </Label>
          </div>
        }
      />
      <CornerNote at={out}>출처: {F.kcmi.v}</CornerNote>
    </>
  );
};

// S18 문장 44–45: 들고 있던 종목 평균 수익률 — 이 습관이 가장 강한 투자자 (뒷줄) 평균 -9.8% / 손실 종목부터 정리한 투자자 평균 +4.9% (왼쪽 나쁜 쪽)
export const S18: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  const Z = 480; // 0선 y
  const k = 16; // 수익률 1%당 막대 길이(px)
  const XL = 620;
  const XR = 1300;
  const BW = 240;
  const atL = b(44, 0.1);
  const atR = a(45, 0.4);
  const hL = Math.abs(F.dispoAvg.v) * k * prog(f, atL, 20);
  const hR = F.lossFirstAvg.v * k * prog(f, atR, 18);
  const vL = count(f, atL, 0, F.dispoAvg.v, 20);
  const vR = count(f, atR, 0, F.lossFirstAvg.v, 18);
  return (
    <>
      <NumberTitle no="03" at={STATIC} title={T03} />
      <Box x={140} y={262}>
        <div style={vis(f, b(44))}>
          <Label size={44} color={C.gray}>
            들고 있던 종목 평균 수익률
          </Label>
        </div>
      </Box>
      <div style={{position: "absolute", left: XL - BW / 2 - 80, top: Z, width: XR - XL + BW + 160, height: 6, background: C.ink, opacity: enter(f, a(44))}} />
      {/* 왼쪽: 이 습관이 가장 강한 투자자 — 막대가 0선 아래로 */}
      <Box x={XL} y={Z - 124} w={560} center>
        <div style={vis(f, a(44))}>
          <Label size={44} weight={900}>
            이 습관이 가장 강한
          </Label>
          <Label size={44} weight={900}>
            투자자
          </Label>
        </div>
      </Box>
      <div style={{position: "absolute", left: XL - BW / 2, top: Z + 6, width: BW, height: hL, background: C.loss, borderRadius: "0 0 10px 10px"}} />
      <Box x={XL} y={Z + 6 + Math.abs(F.dispoAvg.v) * k + 14} w={560} center>
        <div style={{display: "flex", alignItems: "baseline", justifyContent: "center", gap: 14, opacity: enter(f, atL)}}>
          <Label size={40}>평균</Label>
          <Big size={100} color={C.loss}>
            {num(vL, 1)}%
          </Big>
        </div>
      </Box>
      {/* 오른쪽: 손실 종목부터 정리한 투자자 — 막대가 0선 위로 */}
      <div style={{position: "absolute", left: XR - BW / 2, top: Z - hR, width: BW, height: hR, background: C.gain, borderRadius: "10px 10px 0 0"}} />
      <Box x={XR} y={Z - F.lossFirstAvg.v * k - 114} w={560} center>
        <div style={{display: "flex", alignItems: "baseline", justifyContent: "center", gap: 14, opacity: enter(f, atR)}}>
          <Label size={40}>평균</Label>
          <Big size={100} color={C.gain}>
            +{num(vR, 1)}%
          </Big>
        </div>
      </Box>
      <Box x={XR} y={Z + 30} w={560} center>
        <div style={vis(f, a(45))}>
          <Label size={44} weight={900}>
            손실 종목부터
          </Label>
          <Label size={44} weight={900}>
            정리한 투자자
          </Label>
        </div>
      </Box>
      <CornerNote at={STATIC}>출처: {F.kcmi.v}</CornerNote>
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

// S20·S21 공통 (네이비): 카카오 실제 종가 선 (날짜 간격은 실제와 다름, 숫자는 대본 값만) + 아래 개인 매수 막대 (그 기간 아래에)
const ky = (v: number) => 400 + (KAKAO.peak - v) * (280 / (KAKAO.peak - KAKAO.now));
const K0: P = [300, ky(KAKAO.peak)]; // 2021-06-23 고점
const K1: P = [520, ky(KAKAO.w0)]; // 2021-09-03
const K2: P = [600, ky(KAKAO.w1)]; // 2021-09-10 (일주일 뒤)
const K3: P = [760, ky(KAKAO.y21)]; // 2021-12-30
const K4: P = [1100, ky(KAKAO.y22)]; // 2022-12-29
const K5: P = [1580, ky(KAKAO.now)]; // 2026-10-08
const BUY_BASE = 800;
const BUY_MAX = 80; // 2022년 2조 2,870억 원 = 80px (출처 수치 비율, 숫자 표시 안 함)
const BUY_BG = "rgba(247,243,234,0.6)";
const BuyBar: React.FC<{x0: number; x1: number; eok: number; at: number; labelAt: number; strong?: number; children: React.ReactNode}> = ({x0, x1, eok, at, labelAt, strong = 0, children}) => {
  const f = useCurrentFrame();
  const full = (eok / F.buy2022Eok.v) * BUY_MAX;
  const h = full * prog(f, at, 16);
  return (
    <>
      <div style={{position: "absolute", left: x0, top: BUY_BASE - h, width: x1 - x0, height: h, background: strong > 0 ? `rgba(247,243,234,${0.6 + 0.4 * strong})` : BUY_BG, borderRadius: "8px 8px 0 0"}} />
      <div style={{position: "absolute", left: x0 - 40, top: BUY_BASE, width: x1 - x0 + 80, height: 6, background: C.inkOnNavy, opacity: enter(f, at)}} />
      <Box x={(x0 + x1) / 2} y={BUY_BASE - full - 60} w={560} center>
        <div style={vis(f, labelAt)}>
          <Label size={36}>{children}</Label>
        </div>
      </Box>
    </>
  );
};
/** 고점 (문장 49) — S20·S21 같은 자리 */
const PeakLabel: React.FC<{at: number}> = ({at}) => (
  <PtLabel p={K0} at={at} anchor="top">
    <Label size={36} weight={500}>
      {F.kakao.v} · {F.peakMonth.v}
    </Label>
    <Label size={60} weight={900}>
      {F.peak.v}
    </Label>
  </PtLabel>
);
/** 그해 9월 빅테크 규제, 일주일 만에 -17% 가까이 (문장 50) */
const WeekLabel: React.FC<{at: number; numAt: number; until?: number}> = ({at, numAt, until}) => {
  const f = useCurrentFrame();
  return (
    <Box x={650} y={300}>
      <div style={vis(f, at, until)}>
        <Chip variant="outline" size={36}>
          {F.regMonth.v} · {F.regNews.v}
        </Chip>
      </div>
      <div style={{marginTop: 14, ...vis(f, numAt, until)}}>
        <Label size={52} weight={900} color={C.loss}>
          일주일 만에 -{F.weekDrop.v}% 가까이
        </Label>
      </div>
    </Box>
  );
};

// S20 문장 48–51 (네이비): "04" → 카카오 2021년 6월 16만 9,500원 → 9월 빅테크 규제, 일주일 만에 -17% 가까이 → 그 한 주 개인 1조 원 넘게 매수
export const S20: SceneC = ({t}) => {
  const {a} = t;
  return (
    <>
      <NumberTitle no="04" at={a(48)} title={T04} />
      <Layer>
        <Line pts={[K0, K1, K2]} at={a(50, 0.1)} dur={22} color={C.loss} />
        <Dot p={K0} at={a(49, 0.1)} color={C.inkOnNavy} />
        <Dot p={K2} at={a(50, 0.35)} color={C.loss} />
      </Layer>
      <PeakLabel at={a(49, 0.1)} />
      <WeekLabel at={a(50, 0.15)} numAt={a(50, 0.5)} />
      <BuyBar x0={K1[0]} x1={K2[0]} eok={F.buyWeekEok.v} at={a(51, 0.4)} labelAt={a(51, 0.5)}>
        개인 {F.buyWeek.v} 넘게 매수
      </BuyBar>
      <CornerNote at={a(49)}>실제 주가 흐름 · 날짜 간격은 실제와 다름</CornerNote>
    </>
  );
};

// S21 문장 52–55 (네이비): 2022년 반 토막 · 개인 2조 원 넘게 더 매수 → 소액주주 15만 명 가까이 늘어 206만 명 → 2026년 10월 3만 2천 원대, 고점의 5분의 1도 안 됨 → 더 사들인 만큼 손실도 함께
export const S21: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const grow = prog(f, a(53, 0.45), 16);
  const HW = 240; // 소액주주 막대 최대 폭
  const strong = prog(f, a(55, 0.2), 12);
  return (
    <>
      <NumberTitle no="04" at={STATIC} title={T04} />
      <Layer>
        <Line pts={[K0, K1, K2]} at={STATIC} color={C.loss} />
        <Line pts={[K2, K3, K4]} at={a(52, 0.05)} dur={24} color={C.loss} />
        <Line pts={[K4, K5]} at={a(54, 0.1)} dashed width={6} />
        <Dot p={K0} at={STATIC} color={C.inkOnNavy} />
        <Dot p={K2} at={STATIC} color={C.loss} />
        <Dot p={K4} at={a(52, 0.4)} color={C.loss} />
        <Dot p={K5} at={a(54, 0.3)} color={C.loss} />
      </Layer>
      <PeakLabel at={STATIC} />
      <WeekLabel at={STATIC} numAt={STATIC} until={a(52)} />
      <BuyBar x0={K1[0]} x1={K2[0]} eok={F.buyWeekEok.v} at={STATIC} labelAt={STATIC} strong={strong}>
        개인 {F.buyWeek.v} 넘게 매수
      </BuyBar>
      {/* 52: 2022년 반 토막 + 그해 개인 2조 원 넘게 더 매수 */}
      <PtLabel p={K4} at={a(52, 0.4)} until={a(53)} anchor="right">
        <Label size={48} weight={900} color={C.loss}>
          {F.halfYear.v} 반 토막
        </Label>
      </PtLabel>
      <BuyBar x0={K3[0]} x1={K4[0]} eok={F.buy2022Eok.v} at={a(52, 0.5)} labelAt={a(52, 0.6)} strong={strong}>
        개인 {F.buy2022.v} 넘게 더 매수
      </BuyBar>
      {/* 53: 그해 소액주주 15만 명 가까이 늘어 206만 명 (막대 비율 191.8 : 206.7만 명) */}
      <Box x={1160} y={262}>
        <div style={vis(f, a(53), a(54))}>
          <Card style={{width: 640, boxSizing: "border-box", padding: "26px 36px"}}>
            <Label size={40} weight={900}>
              {F.kakao.v} 소액주주
            </Label>
            {[
              {y: "2021년 말", w: HW * (F.holders21.v / F.holders22.v), v: null},
              {y: `${F.halfYear.v} 말`, w: HW * (F.holders21.v / F.holders22.v) + HW * (1 - F.holders21.v / F.holders22.v) * grow, v: F.holders.v},
            ].map((r) => (
              <div key={r.y} style={{display: "flex", alignItems: "center", gap: 14, marginTop: 14}}>
                <Label size={32} weight={500} color={C.gray} style={{width: 150, flex: "none"}}>
                  {r.y}
                </Label>
                <div style={{width: r.w, height: 40, background: C.ink, borderRadius: 8, flex: "none"}} />
                {r.v ? (
                  <Label size={38} weight={900} style={{opacity: enter(f, a(53, 0.6)), whiteSpace: "nowrap"}}>
                    {r.v}
                  </Label>
                ) : null}
              </div>
            ))}
            <div style={{marginTop: 16, ...vis(f, a(53, 0.3))}}>
              <Label size={48} weight={900}>
                <Hi at={a(53, 0.45)}>+{F.holdersUp.v} 가까이</Hi>
              </Label>
            </div>
          </Card>
        </div>
      </Box>
      {/* 54: 2026년 10월 3만 2천 원대, 고점의 5분의 1도 안 됨 */}
      <PtLabel p={K5} at={a(54, 0.3)} anchor="top">
        <Label size={36} weight={500}>
          {F.now.v}
        </Label>
        <Label size={60} weight={900} color={C.loss}>
          {F.kakaoNow.v}
        </Label>
        <Label size={40} style={{marginTop: 4}}>
          <Hi at={a(54, 0.65)} until={a(55)}>
            고점의 {F.fifth.v}도 안 됨
          </Hi>
        </Label>
      </PtLabel>
      {/* 55: 떨어질수록 더 사들인 만큼 손실도 함께 (매수 막대가 밝아짐) */}
      <Box x={1160} y={290}>
        <div style={vis(f, a(55, 0.1))}>
          <Label size={52} weight={900}>
            떨어질수록 더 사들인 만큼
          </Label>
        </div>
        <div style={{marginTop: 6, ...vis(f, a(55, 0.35))}}>
          <Label size={60} weight={900}>
            <Hi at={a(55, 0.5)}>손실도 함께 ↑</Hi>
          </Label>
        </div>
      </Box>
      <CornerNote at={STATIC}>실제 주가 흐름 · 날짜 간격은 실제와 다름</CornerNote>
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
