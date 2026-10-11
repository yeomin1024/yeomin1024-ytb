// 문제 분석 파트 S08–S19 (문장 19–55)
import React from "react";
import {interpolate, useCurrentFrame} from "remotion";
import {C, SERIF} from "../../../design/tokens";
import {enter, prog} from "../../../components/anim";
import {won} from "../../../components/fmt";
import {Big, Box, Card, Chip, CornerNote, Headline, Hi, Label, Mark, fadeOut, vis} from "../../../components/ui";
import {NumberTitle} from "../../../components/cards";
import {Dot, HRule, Layer, Line, P, PtLabel} from "../../../components/charts";
import {Balance, Weight} from "../../../components/objects";
import {F} from "../facts";
import {CrossLabel, DateTag, GHOST, MiniAccount, MiniPhone, Moon, MyAccount, Waffle, waffleSize} from "../local";
import {SceneC} from "./story";

const STATIC = -60; // 같은 항목의 이어지는 장면: 번호 타이틀이 이미 떠 있음
const CLAMP = {extrapolateLeft: "clamp", extrapolateRight: "clamp"} as const;

// 번호 타이틀 문구 (같은 항목은 같은 문구, S32 두 열 요약도 같은 이름)
export const T01 = "몰빵 종목이 하락하면 대처할 방법이 없다";
export const T02 = "버티는 것도 답이 아니다";
export const T03 = "큰 수익을 낼 확률 자체가 낮다";
export const T04 = "몰빵은 판단력까지 무너뜨린다";

// ── S08 문장 19–22: "01" → 앞으로 어떻게 움직일지 모름(갈래 ?) → 장기 ↑ 이어도 단기 큰 악재 → 상승세 보고 산 사람·기존 수익 중인 사람도 큰 손해 (개념도) ──
const HIST: P[] = [
  [220, 560],
  [330, 520],
  [420, 560],
  [540, 500],
  [650, 540],
  [760, 490],
  [860, 520],
];
const NOW = HIST[HIST.length - 1];
const BR: P[][] = [
  [NOW, [1060, 420], [1260, 330]],
  [NOW, [1080, 530], [1300, 515]],
  [NOW, [1060, 620], [1260, 720]],
];
const UPPATH: P[] = [
  [220, 700],
  [340, 640],
  [440, 670],
  [560, 590],
  [680, 610],
  [800, 540],
  [920, 560],
  [1040, 480],
  [1160, 500],
  [1280, 420],
];
const TOP = UPPATH[UPPATH.length - 1];
const CRASH: P = [1330, 690];
const OLD = UPPATH[3];
export const S08: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  const out = a(21);
  const bp = prog(f, b(22, 0.15), 14);
  return (
    <>
      <NumberTitle
        no="01"
        at={a(19)}
        title={
          <>
            몰빵 종목이
            <span style={{opacity: enter(f, b(19))}}>
              {" "}
              하락하면 <Hi at={b(19, 0.4)} until={b(20)}>대처할 방법이 없다</Hi>
            </span>
          </>
        }
      />
      {/* 20: 앞으로 어떻게 움직일지 모름 */}
      <div style={{position: "absolute", inset: 0, opacity: fadeOut(f, out)}}>
        <Layer>
          <Line pts={HIST} at={a(20, 0.05)} dur={24} width={7} />
          <Dot p={NOW} at={a(20, 0.4)} />
          {BR.map((p, i) => (
            <Line key={i} pts={p} at={b(20, 0.05) + i * 4} dashed width={6} />
          ))}
        </Layer>
        <PtLabel p={NOW} at={a(20, 0.4)} anchor="bottom">
          <Label size={40}>지금</Label>
        </PtLabel>
        <div style={{position: "absolute", left: 1380, top: 380, fontFamily: SERIF, fontWeight: 900, fontSize: 200, lineHeight: 1, ...vis(f, b(20, 0.3))}}>?</div>
      </div>
      {/* 21–22: 장기 ↑ 이어도 단기 큰 악재 → 상승세 보고 산 사람·기존 수익 중인 사람도 큰 손해 */}
      <div style={{position: "absolute", inset: 0, opacity: enter(f, out)}}>
        <Layer>
          <Line pts={[[220, 720], [1700, 330]]} at={out} dashed width={6} />
          <Line pts={UPPATH} at={out + 6} dur={30} width={7} />
          <Line pts={[TOP, CRASH]} at={b(21, 0.15)} dur={8} color={C.loss} width={12} />
          <Dot p={CRASH} at={b(21, 0.3)} color={C.loss} r={16} />
          <Dot p={TOP} at={a(22, 0.1)} color={C.ink} />
          <Dot p={OLD} at={a(22, 0.5)} color={C.ink} />
        </Layer>
        <Box x={1460} y={262}>
          <div style={vis(f, out + 4)}>
            <Label size={40} color={C.gray}>
              장기적으로 ↗
            </Label>
          </div>
        </Box>
        <PtLabel p={CRASH} at={b(21, 0.3)} anchor="left" gap={30}>
          <div style={{display: "inline-block", background: C.loss, color: "#FFFFFF", fontWeight: 700, fontSize: 40, padding: "8px 26px", borderRadius: 12}}>단기 · 갑자기 큰 악재</div>
        </PtLabel>
        <PtLabel p={TOP} at={a(22, 0.1)} anchor="top">
          <Label size={40}>상승세 보고 매수</Label>
        </PtLabel>
        <PtLabel p={OLD} at={a(22, 0.5)} anchor="top">
          <Label size={40}>기존 수익 중</Label>
        </PtLabel>
        {/* (뒷줄) 큰 손해 괄호 */}
        <div style={{position: "absolute", left: 1400, top: TOP[1], width: 24, height: (CRASH[1] - TOP[1]) * bp, borderTop: `6px solid ${C.loss}`, borderRight: `6px solid ${C.loss}`, borderBottom: bp > 0.95 ? `6px solid ${C.loss}` : undefined, borderRadius: "0 8px 8px 0", opacity: bp > 0 ? 1 : 0}} />
        <Box x={1450} y={(TOP[1] + CRASH[1]) / 2 - 40}>
          <div style={vis(f, b(22, 0.35))}>
            <Label size={64} weight={900} color={C.loss}>
              큰 손해
            </Label>
          </div>
        </Box>
      </div>
      <CornerNote at={a(20)} y={780}>
        개념도
      </CornerNote>
    </>
  );
};

// ── 사례 카드 (빅테크 하루 급락): 이름 · 연도 · 원인 · 0선 아래 파랑 막대 · 값 ──
const KB = 9; // 하락률 1%당 막대 길이(px), 세 카드 같은 비율
export const CASE_W = 540;
export const CaseCard: React.FC<{
  x: number;
  y?: number;
  name: string;
  at: number;
  year: string;
  yearAt: number;
  why: React.ReactNode;
  whyAt: number;
  pct: number;
  unit: string;
  barAt: number;
  extra?: React.ReactNode;
}> = ({x, y = 262, name, at, year, yearAt, why, whyAt, pct, unit, barAt, extra}) => {
  const f = useCurrentFrame();
  const z = 236;
  const h = Math.abs(pct) * KB * prog(f, barAt, 18);
  return (
    <Box x={x} y={y}>
      <div style={vis(f, at)}>
        <Card style={{width: CASE_W, height: 520, boxSizing: "border-box", padding: 0, position: "relative"}}>
          <div style={{position: "absolute", left: 36, top: 22}}>
            <Label size={60} weight={900}>
              {name}
            </Label>
          </div>
          <div style={{position: "absolute", right: 30, top: 34, opacity: enter(f, yearAt)}}>
            <DateTag>{year}</DateTag>
          </div>
          <div style={{position: "absolute", left: 36, top: 112, width: CASE_W - 72}}>{typeof why === "string" ? <WhyText at={whyAt}>{why}</WhyText> : why}</div>
          <div style={{position: "absolute", left: 36, right: 36, top: z - 3, height: 6, background: C.ink, opacity: enter(f, barAt)}} />
          <div style={{position: "absolute", left: 60, top: z + 3, width: 140, height: h, background: C.loss, borderRadius: "0 0 10px 10px"}} />
          <div style={{position: "absolute", left: 232, top: z + 20, opacity: enter(f, barAt + 6)}}>
            <Label size={36} weight={500} color={C.gray}>
              {unit}
            </Label>
            <Big size={110} color={C.loss} style={{marginTop: 4}}>
              {pct}%
            </Big>
          </div>
          {extra ? <div style={{position: "absolute", left: 36, top: 410, width: CASE_W - 72}}>{extra}</div> : null}
        </Card>
      </div>
    </Box>
  );
};
const WhyText: React.FC<{at: number; children: React.ReactNode}> = ({at, children}) => {
  const f = useCurrentFrame();
  return (
    <div style={{opacity: enter(f, at)}}>
      <Label size={36} weight={500} color="#55524C">
        {children}
      </Label>
    </div>
  );
};
const CX = [120, 690, 1260];

// ── S09 문장 23–27: 메타 · 구글 · 엔비디아 사례 카드 → 2022 메타 실적 실망 하루 -26% → 2023 구글 AI 챗봇 광고 속 오답 장중 -9% → 2025 엔비디아 중국 AI 기업 · (뒷줄) 딥시크 등장 하루 -17% → 미국 증시 역사상 하루 최대 시가총액 손실 ──
export const S09: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  return (
    <>
      <NumberTitle no="01" at={STATIC} title={T01} />
      <CaseCard x={CX[0]} name={F.meta.v} at={a(23, 0.25)} year={F.metaYear.v} yearAt={a(24)} why={F.metaWhy.v} whyAt={a(24, 0.3)} pct={F.metaDrop.v} unit="하루" barAt={a(24, 0.55)} />
      <CaseCard x={CX[1]} name={F.google.v} at={a(23, 0.4)} year={F.googleYear.v} yearAt={a(25)} why={F.googleWhy.v} whyAt={a(25, 0.25)} pct={F.googleDrop.v} unit="장중" barAt={a(25, 0.65)} />
      <CaseCard
        x={CX[2]}
        name={F.nvidia.v}
        at={a(23, 0.55)}
        year={F.nvidiaYear.v}
        yearAt={a(26)}
        why={
          <Label size={36} weight={500} color="#55524C">
            <span style={{opacity: enter(f, a(26, 0.35))}}>중국 AI 기업 </span>
            <span style={{opacity: enter(f, b(26))}}>{F.nvidiaWhy.v}</span>
          </Label>
        }
        whyAt={a(26, 0.35)}
        pct={F.nvidiaDrop.v}
        unit="하루"
        barAt={b(26, 0.35)}
        extra={
          <div style={{opacity: enter(f, a(27, 0.1))}}>
            <Label size={34} weight={500}>
              미국 증시 역사상
            </Label>
            <Label size={34} weight={900}>
              <Hi at={a(27, 0.55)}>하루 최대 시가총액 손실</Hi>
            </Label>
          </div>
        }
      />
    </>
  );
};

// ── S10 문장 28–29: S09의 메타 카드 + "전문가도 ?" → 메타 폭락 직전 → (뒷줄) 팔라는 의견 애널리스트 단 2명뿐 ──
export const S10: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  const q = a(29);
  return (
    <>
      <NumberTitle no="01" at={STATIC} title={T01} />
      <CaseCard x={200} name={F.meta.v} at={a(28)} year={F.metaYear.v} yearAt={a(28)} why={F.metaWhy.v} whyAt={a(28)} pct={F.metaDrop.v} unit="하루" barAt={a(28)} />
      <Box x={900} y={300}>
        <div style={{display: "flex", alignItems: "center", gap: 30, ...vis(f, a(28, 0.25)), opacity: enter(f, a(28, 0.25)) * fadeOut(f, q)}}>
          <Label size={64} weight={900}>
            전문가도
          </Label>
          <div style={{fontFamily: SERIF, fontWeight: 900, fontSize: 220, lineHeight: 1}}>?</div>
        </div>
      </Box>
      <Box x={900} y={290}>
        <div style={vis(f, q)}>
          <DateTag style={{fontSize: 40, display: "inline-block"}}>{F.meta.v} 폭락 직전</DateTag>
        </div>
        <div style={{marginTop: 36, ...vis(f, b(29))}}>
          <Label size={48}>팔라는 의견 낸 애널리스트</Label>
        </div>
        <div style={{display: "flex", alignItems: "baseline", gap: 16, marginTop: 10, ...vis(f, b(29, 0.3))}}>
          <Label size={56} weight={900}>
            단
          </Label>
          <Big size={200}>
            <Hi at={b(29, 0.5)}>{F.analysts.v}명</Hi>
          </Big>
          <Label size={56} weight={900} style={{marginLeft: -10}}>
            뿐
          </Label>
        </div>
      </Box>
    </>
  );
};

// ── S11 문장 30–31: 사연 계좌 카드(S02와 같음, -2,000만 원 · 현금 0원) → 선택지 없음 → 물타기 ✗ 현금 0원 / 손절 → 손실 확정 ──
export const S11: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  return (
    <>
      <NumberTitle no="01" at={STATIC} title={T01} />
      <Box x={120} y={262}>
        <div style={vis(f, a(30))}>
          <MyAccount pnl={F.loss.v} footL={`${F.company.v} ${won(F.all.v)}`} footR="현금 0원" />
        </div>
      </Box>
      <Box x={1140} y={268}>
        <div style={vis(f, a(30, 0.55))}>
          <Headline size={76}>
            선택지 <Hi at={a(30, 0.7)}>없음</Hi>
          </Headline>
        </div>
      </Box>
      <Box x={1140} y={400}>
        <div style={vis(f, a(31, 0.02))}>
          <Card style={{width: 680, boxSizing: "border-box", padding: "24px 40px", display: "flex", alignItems: "center", gap: 30}}>
            <Label size={56} weight={900}>
              물타기
            </Label>
            <CrossLabel at={a(31, 0.15)} size={44}>
              현금 0원
            </CrossLabel>
          </Card>
        </div>
      </Box>
      <Box x={1140} y={590}>
        <div style={vis(f, a(31, 0.5))}>
          <Card style={{width: 680, boxSizing: "border-box", padding: "24px 40px", display: "flex", alignItems: "center", gap: 30}}>
            <Label size={56} weight={900}>
              손절
            </Label>
            <Label size={44} weight={900} color={C.loss} style={{opacity: enter(f, a(31, 0.7))}}>
              → 손실 확정
            </Label>
          </Card>
        </div>
      </Box>
    </>
  );
};

// ── S12 문장 32–33: 미리 정해 둔 손절 라인 → 장 시작 전 악재 → 다음 날 시작가가 손절 라인보다 훨씬 아래 (개념도) ──
const DAY1: P[] = [
  [200, 400],
  [300, 380],
  [400, 420],
  [500, 370],
  [600, 400],
  [700, 360],
  [800, 390],
  [900, 380],
];
const OPEN: P = [1110, 700];
const STOP_Y = 540;
const SEP_X = 1000;
export const S12: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const bp = prog(f, a(33, 0.65), 12);
  return (
    <>
      <NumberTitle no="01" at={STATIC} title={T01} />
      <Layer>
        <Line pts={DAY1} at={a(32)} dur={22} width={7} />
        <Line pts={[DAY1[DAY1.length - 1], OPEN]} at={a(33, 0.45)} dashed width={5} />
        <Dot p={OPEN} at={a(33, 0.5)} color={C.loss} r={16} />
      </Layer>
      <HRule y={STOP_Y} x0={200} x1={1700} at={a(32, 0.25)} color={C.ink} labelAt="aboveEnd">
        <div style={{display: "flex", alignItems: "center", gap: 14}}>
          <Label size={40}>미리 정해 둔 손절 라인</Label>
          <div style={{opacity: enter(f, a(33, 0.8))}}>
            <Mark kind="cross" at={a(33, 0.8)} size={56} color={C.loss} />
          </div>
        </div>
      </HRule>
      {/* 장 마감 | 다음 날 장 시작 */}
      <div style={{position: "absolute", left: SEP_X - 3, top: 360, height: 300, borderLeft: `6px dashed ${C.gray}`, opacity: enter(f, a(33))}} />
      <Box x={SEP_X} y={262} w={600} center>
        <div style={vis(f, a(33))}>
          <div style={{display: "inline-block", background: C.loss, color: "#FFFFFF", fontWeight: 700, fontSize: 42, padding: "8px 28px", borderRadius: 12}}>장 시작 전 악재</div>
        </div>
      </Box>
      <PtLabel p={OPEN} at={a(33, 0.5)} anchor="bottom" gap={24}>
        <Label size={40}>다음 날 시작</Label>
      </PtLabel>
      {/* 손절 라인 → 시작가 괄호 */}
      <div style={{position: "absolute", left: 1170, top: STOP_Y, width: 24, height: (OPEN[1] - STOP_Y) * bp, borderTop: `6px solid ${C.loss}`, borderRight: `6px solid ${C.loss}`, borderBottom: bp > 0.95 ? `6px solid ${C.loss}` : undefined, borderRadius: "0 8px 8px 0", opacity: bp > 0 ? 1 : 0}} />
      <Box x={1220} y={(STOP_Y + OPEN[1]) / 2 - 36}>
        <div style={vis(f, a(33, 0.7))}>
          <Label size={56} weight={900} color={C.loss}>
            훨씬 아래
          </Label>
        </div>
      </Box>
      <CornerNote at={a(32)} y={780}>
        개념도
      </CornerNote>
    </>
  );
};

// ── S13 문장 34–38: "02" → 되찾기 훨씬 어렵다 → 7,000만 → 5,000만 원 -29% → (뒷줄) +40% / 반토막 -50% → +100% 두 배 · (뒷줄) -70% → +233% 세 배 넘게 → 몰빵은 계좌 전체로 ──
const RB = 690; // 바닥선
const RH = 300; // 원금 높이
const RW = 200;
type Rec = {x: number; rem: number; drop: string; need: string; sub?: string; bottom: string; at: number; needAt: number};
const RecoveryCol: React.FC<{r: Rec}> = ({r}) => {
  const f = useCurrentFrame();
  const cur = 1 - (1 - r.rem) * prog(f, r.at + 8, 16);
  const red = (1 - r.rem) * prog(f, r.needAt, 20);
  const o = enter(f, r.at);
  return (
    <>
      <div style={{position: "absolute", left: r.x, top: RB - RH * cur, width: RW, height: RH * cur, background: C.ink, borderRadius: cur > 0.99 ? "10px 10px 0 0" : 0, opacity: o}} />
      {cur < 0.999 ? (
        <div style={{position: "absolute", left: r.x, top: RB - RH, width: RW, height: RH * (1 - cur), boxSizing: "border-box", background: GHOST, border: `4px dashed ${C.loss}`, borderRadius: "10px 10px 0 0"}} />
      ) : null}
      {red > 0 ? <div style={{position: "absolute", left: r.x + 10, top: RB - RH * r.rem - RH * red, width: RW - 20, height: RH * red, background: C.gain, borderRadius: "8px 8px 0 0"}} /> : null}
      <div style={{position: "absolute", left: r.x + RW + 16, top: RB - RH + (RH * (1 - r.rem)) / 2 - 30, opacity: enter(f, r.at + 16)}}>
        <Label size={46} weight={900} color={C.loss}>
          {r.drop}
        </Label>
      </div>
      <div style={{position: "absolute", left: r.x - 100, width: RW + 200, top: RB - RH - 14, transform: "translateY(-100%)", textAlign: "center", opacity: enter(f, r.needAt + 8)}}>
        {r.sub ? (
          <Label size={36} weight={700} color={C.gain}>
            {r.sub}
          </Label>
        ) : null}
        <Big size={84} color={C.gain}>
          {r.need}
        </Big>
      </div>
      <div style={{position: "absolute", left: r.x - 100, width: RW + 200, top: RB + 14, textAlign: "center", opacity: o}}>
        <Label size={36}>{r.bottom}</Label>
      </div>
    </>
  );
};
export const S13: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  const last = a(38);
  const cols: Rec[] = [
    {x: 200, rem: F.after.v / F.all.v, drop: `${F.drop29.v}%`, need: `+${F.need40.v}%`, bottom: `${won(F.all.v).replace(" 원", "")} → ${won(F.after.v)}`, at: a(36, 0.05), needAt: b(36, 0.2)},
    {x: 600, rem: 1 + F.half.v / 100, drop: `${F.half.v}%`, need: `+${F.need100.v}%`, sub: "두 배", bottom: "반토막", at: a(37, 0.05), needAt: a(37, 0.3)},
    {x: 1000, rem: 1 + F.drop70.v / 100, drop: `${F.drop70.v}%`, need: `+${F.need233.v}%`, sub: "세 배 넘게", bottom: "70% 하락", at: b(37, 0.05), needAt: b(37, 0.45)},
  ];
  return (
    <>
      <NumberTitle
        no="02"
        at={a(34)}
        title={
          <>
            버티는 것도 <Hi at={a(34, 0.55)} until={a(35, 0.5)}>답이 아니다</Hi>
          </>
        }
      />
      <HRule y={RB - RH} x0={150} x1={1250} at={a(36)} color={C.gray} labelAt="right">
        <Label size={40} color={C.gray}>
          원금
        </Label>
      </HRule>
      <div style={{position: "absolute", left: 150, top: RB, width: 1100, height: 6, background: C.ink, opacity: enter(f, a(36))}} />
      {cols.map((r, i) => (
        <RecoveryCol key={i} r={r} />
      ))}
      {/* 오른쪽: 35 되찾기 훨씬 어렵다 → 38 몰빵은 계좌 전체로 */}
      <Box x={1430} y={330}>
        <div style={{...vis(f, a(35)), opacity: enter(f, a(35)) * fadeOut(f, last)}}>
          <Label size={44}>크게 잃으면</Label>
          <Headline size={64} style={{marginTop: 8}}>
            되찾기
          </Headline>
          <Headline size={64}>
            <Hi at={a(35, 0.6)} until={last}>
              훨씬 어렵다
            </Hi>
          </Headline>
        </div>
      </Box>
      <Box x={1430} y={330}>
        <div style={vis(f, last)}>
          <Label size={44}>몰빵은 이 위험을</Label>
          <Headline size={72} style={{marginTop: 8}}>
            <Hi at={a(38, 0.5)}>계좌 전체로</Hi>
          </Headline>
        </div>
      </Box>
    </>
  );
};

// ── S14 문장 39–42: "03" → 자본시장연구원 · 2023년 말까지 10년 · (뒷줄) 국내 상장사 주식 수익률 → 와플 52% 1년짜리 안전한 채권보다 못 벎 → 시총 상위 30% 대형주 58% 오히려 더 높음 ──
const WC = 30;
const WG = 5;
export const S14: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  const v52 = Math.round(F.under52.v * prog(f, a(41, 0.2), 24));
  const v58 = Math.round(F.under58.v * prog(f, a(42, 0.45), 24));
  const ws = waffleSize(WC, WG);
  return (
    <>
      <NumberTitle
        no="03"
        at={a(39)}
        title={
          <>
            큰 수익을 낼 <Hi at={a(39, 0.6)} until={a(40)}>확률 자체가 낮다</Hi>
          </>
        }
      />
      <Box x={140} y={262}>
        <div style={vis(f, a(40))}>
          <Card style={{width: 1640, boxSizing: "border-box", padding: "18px 40px", display: "flex", alignItems: "center", gap: 26}}>
            <Label size={52} weight={900}>
              {F.kcmi.v}
            </Label>
            <div style={vis(f, a(40, 0.4))}>
              <Chip size={36}>{F.kcmiPeriod.v}</Chip>
            </div>
            <div style={vis(f, b(40, 0.1))}>
              <Chip variant="outline" size={36}>
                {F.kcmiScope.v} 주식 수익률
              </Chip>
            </div>
          </Card>
        </div>
      </Box>
      {/* 41: 국내 상장사 52% */}
      <Waffle x={150} y={410} cell={WC} gap={WG} n={F.under52.v} at={a(41)} fillAt={a(41, 0.2)} color={C.loss} />
      <Box x={150 + ws + 36} y={404}>
        <div style={vis(f, a(41))}>
          <Label size={36} weight={500} color={C.gray}>
            {F.kcmiScope.v}
          </Label>
          <Big size={150} color={C.loss} style={{marginTop: 6}}>
            {v52}%
          </Big>
          <Label size={34} style={{marginTop: 14, opacity: enter(f, a(41, 0.5))}}>
            1년짜리 안전한 채권보다
          </Label>
          <Label size={40} weight={900} style={{opacity: enter(f, a(41, 0.75))}}>
            못 벎
          </Label>
        </div>
      </Box>
      {/* 42: 시총 상위 30% 대형주 58% */}
      <Waffle x={990} y={410} cell={WC} gap={WG} n={F.under58.v} at={a(42)} fillAt={a(42, 0.45)} color={C.loss} />
      <Box x={990 + ws + 36} y={404}>
        <div style={vis(f, a(42))}>
          <Label size={36} weight={500} color={C.gray}>
            시총 상위 30% 대형주
          </Label>
          <Big size={150} color={C.loss} style={{marginTop: 6}}>
            {v58}%
          </Big>
          <Label size={40} weight={900} style={{marginTop: 14, opacity: enter(f, a(42, 0.7))}}>
            <Hi at={a(42, 0.8)}>오히려 더 높음</Hi>
          </Label>
        </div>
      </Box>
      <CornerNote at={a(40)} y={780}>
        출처: {F.kcmi.v}
      </CornerNote>
    </>
  );
};

// ── S15 문장 43–44: 2026년 6월까지 코스피 두 배 넘게 ↑ → (뒷줄) 지수를 이긴 종목 4% 미만 (와플) → 몰빵 = 이 4%를 정확히 골라야 ──
const W2C = 40;
const W2G = 6;
const W2X = 820;
const W2Y = 290;
export const S15: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  const out = a(44);
  const ringW = 4 * W2C + 3 * W2G + 28;
  const ringH = W2C + 28;
  const per = 2 * (ringW + ringH);
  const rp = prog(f, a(44, 0.35), 16);
  return (
    <>
      <NumberTitle no="03" at={STATIC} title={T03} />
      <div style={{position: "absolute", inset: 0, opacity: fadeOut(f, out)}}>
        <Box x={140} y={300}>
          <div style={vis(f, a(43))}>
            <DateTag style={{fontSize: 40, display: "inline-block"}}>
              {F.kospiYear.v} · {F.kospiTo.v}
            </DateTag>
          </div>
          <div style={{marginTop: 34, ...vis(f, a(43, 0.15))}}>
            <Label size={56}>코스피</Label>
          </div>
          <div style={{display: "flex", alignItems: "center", gap: 18, marginTop: 10, ...vis(f, a(43, 0.35))}}>
            <Big size={110} color={C.gain}>
              {F.kospiTwice.v}
            </Big>
            <Label size={90} weight={900} color={C.gain}>
              ↑
            </Label>
          </div>
        </Box>
      </div>
      <Waffle x={W2X} y={W2Y} cell={W2C} gap={W2G} n={F.beatShare.v} at={b(43)} fillAt={b(43, 0.3)} dur={14} color={C.gain} />
      <Box x={1330} y={300}>
        <div style={vis(f, b(43))}>
          <Label size={40}>지수를 이긴 종목</Label>
          <Big size={120} color={C.gain} style={{marginTop: 10}}>
            {F.beat4.v}% 미만
          </Big>
        </div>
      </Box>
      {/* 44: 이 4%를 정확히 골라야 */}
      <svg width={1920} height={1080} style={{position: "absolute", left: 0, top: 0, overflow: "visible"}}>
        <rect x={W2X - 14} y={W2Y - 14} width={ringW} height={ringH} rx={14} fill="none" stroke={C.ink} strokeWidth={6} strokeDasharray={per} strokeDashoffset={per * (1 - rp)} opacity={rp > 0 ? 1 : 0} />
      </svg>
      <Box x={1330} y={540}>
        <div style={vis(f, a(44, 0.2))}>
          <Label size={44}>몰빵 = 이 4%를</Label>
          <Headline size={68} style={{marginTop: 6}}>
            <Hi at={a(44, 0.5)}>정확히</Hi> 골라야
          </Headline>
        </div>
      </Box>
    </>
  );
};

// ── S16 문장 45–47: 엔씨소프트 · LG생활건강 2021년 고점(잉크 막대) → (뒷줄) -70% 넘게 → 5년 넘게 고점 되찾지 못함 → 코스피 2021년 고점의 두 배 수준 ──
const SB = 720; // 바닥선
const SU = 170; // 2021년 고점 = 100%
const SW = 180;
const HighBar: React.FC<{x: number; ratio: number; at: number; moveAt: number; name: string; up?: boolean}> = ({x, ratio, at, moveAt, name, up}) => {
  const f = useCurrentFrame();
  const o = enter(f, at);
  const k = prog(f, moveAt, 20);
  const cur = up ? 1 : 1 - (1 - ratio) * k;
  const extra = up ? (ratio - 1) * k : 0;
  return (
    <>
      <div style={{position: "absolute", left: x, top: SB - SU * cur, width: SW, height: SU * cur, background: C.ink, opacity: o, borderRadius: cur > 0.99 && !extra ? "10px 10px 0 0" : 0}} />
      {!up && cur < 0.999 ? (
        <div style={{position: "absolute", left: x, top: SB - SU, width: SW, height: SU * (1 - cur), boxSizing: "border-box", background: GHOST, border: `4px dashed ${C.loss}`, borderRadius: "10px 10px 0 0"}} />
      ) : null}
      {extra > 0 ? <div style={{position: "absolute", left: x, top: SB - SU - SU * extra, width: SW, height: SU * extra, background: C.gain, borderRadius: "10px 10px 0 0"}} /> : null}
      <div style={{position: "absolute", left: x - 80, width: SW + 160, top: SB + 14, textAlign: "center", opacity: o}}>
        <Label size={38}>{name}</Label>
      </div>
    </>
  );
};
export const S16: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  return (
    <>
      <NumberTitle no="03" at={STATIC} title={T03} />
      <div style={{position: "absolute", left: 180, top: SB, width: 1280, height: 6, background: C.ink, opacity: enter(f, a(45))}} />
      <HighBar x={240} ratio={F.ncRatio.v} at={a(45, 0.2)} moveAt={b(45, 0.1)} name={F.nc.v} />
      <HighBar x={540} ratio={F.lghRatio.v} at={a(45, 0.45)} moveAt={b(45, 0.15)} name={F.lgh.v} />
      <HRule y={SB - SU} x0={180} x1={1460} at={a(45, 0.05)} color={C.gray} labelAt="right">
        <Label size={40} color={C.gray}>
          {F.highYear.v} 고점
        </Label>
      </HRule>
      <Box x={480} y={SB - SU - 82} w={600} center>
        <div style={vis(f, b(45, 0.35))}>
          <Label size={56} weight={900} color={C.loss}>
            -{F.down70.v}% 넘게
          </Label>
        </div>
      </Box>
      {/* 46: 5년 넘게 고점 되찾지 못함 */}
      <Box x={480} y={300} w={760} center>
        <div style={{display: "flex", flexDirection: "column", alignItems: "center", gap: 8, ...vis(f, a(46))}}>
          <Label size={52} weight={900}>
            {F.years5.v}
          </Label>
          <CrossLabel at={a(46, 0.4)} size={44}>
            고점 되찾지 못함
          </CrossLabel>
        </div>
      </Box>
      {/* 47: 코스피는 2021년 고점의 두 배 수준 */}
      <HighBar x={1150} ratio={F.kospiRatio.v} at={a(47, 0.1)} moveAt={a(47, 0.45)} name="코스피" up />
      <Box x={1150 + SW / 2} y={SB - SU * F.kospiRatio.v - 84} w={500} center>
        <div style={vis(f, a(47, 0.6))}>
          <Label size={56} weight={900} color={C.gain}>
            <Hi at={a(47, 0.75)}>{F.kospiDouble.v}</Hi>
          </Label>
        </div>
      </Box>
    </>
  );
};

// ── S17 문장 48: 몰빵 성공담(빨강 계좌 3개)만 들림 → (뒷줄) 크게 잃은 사람들(파랑 계좌 여럿)은 조용히 떠남 ──
export const S17: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  const leave = b(48, 0.35);
  return (
    <>
      <NumberTitle no="03" at={STATIC} title={T03} />
      <Box x={170} y={300}>
        <div style={vis(f, a(48))}>
          <Label size={52} weight={900}>
            몰빵 성공담만 들림
          </Label>
        </div>
        <div style={{display: "flex", gap: 26, marginTop: 30}}>
          {[0, 1, 2].map((i) => (
            <MiniAccount key={i} at={a(48, 0.1) + i * 4} tone="gain" w={160} />
          ))}
        </div>
      </Box>
      <div style={{position: "absolute", left: 830, top: 270, width: 6, height: 500, background: C.gray, opacity: enter(f, b(48)) * 0.6}} />
      <Box x={920} y={300}>
        <div style={vis(f, b(48))}>
          <Label size={52} weight={900}>
            크게 잃은 사람들
          </Label>
        </div>
      </Box>
      <Box x={920} y={392}>
        <div style={{display: "grid", gridTemplateColumns: "repeat(6, 130px)", gap: 22}}>
          {Array.from({length: 12}).map((_, i) => {
            const go = prog(f, leave + i * 2, 16);
            return (
              <div key={i} style={{opacity: 1 - 0.8 * go, transform: `translateX(${go * 50}px)`}}>
                <MiniAccount at={b(48, 0.05) + i * 2} tone="loss" w={130} />
              </div>
            );
          })}
        </div>
      </Box>
      <Box x={920} y={660}>
        <div style={vis(f, b(48, 0.45))}>
          <Label size={52} weight={900}>
            → <Hi at={b(48, 0.6)}>조용히 떠남</Hi>
          </Label>
        </div>
      </Box>
    </>
  );
};

// ── S18 문장 49–51: "04" → 천칭: 잃을 때 / 얻을 때, 잃는 쪽으로 기움 → 고통 블록 1개 → (뒷줄) 기쁨 블록 1개 → 고통 블록 2개 + 두 배 정도 ──
export const S18: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  // 50: 잃는 쪽으로 기움 / 51 앞줄 '잃을 때의 고통' 블록 1개 / (뒷줄) '기쁨' 1개 → '두 배 정도': 고통 블록이 2개가 되며 더 기움
  const dbl = b(51, 0.45);
  const ang = interpolate(f, [a(50, 0.3), a(50, 0.3) + 18, dbl, dbl + 18], [0, 6, 6, 12], CLAMP);
  // 접시 위치 (components/objects Balance와 같은 계산) — 접시 이름 칩은 접시 아래
  const cx = 960;
  const cy = 420;
  const span = 1000;
  const r = (ang * Math.PI) / 180;
  const hx = (span / 2) * Math.cos(r);
  const hy = (span / 2) * Math.sin(r);
  const panL = {x: cx - hx, y: cy + hy + 150};
  const panR = {x: cx + hx, y: cy - hy + 150};
  const W2 = (txt: string, at: number, color: string) => (
    <Weight at={at} color={color} textColor="#FFFFFF" w={170}>
      {txt}
    </Weight>
  );
  return (
    <>
      <NumberTitle
        no="04"
        at={a(49)}
        title={
          <>
            몰빵은 <Hi at={a(49, 0.4)} until={b(51, 0.4)}>판단력까지</Hi> 무너뜨린다
          </>
        }
      />
      <Balance
        cx={cx}
        cy={cy}
        span={span}
        angle={ang}
        at={a(50)}
        left={
          <div style={{display: "flex", gap: 10}}>
            {W2("고통", a(51, 0.12), C.loss)}
            {W2("고통", dbl, C.loss)}
          </div>
        }
        right={W2("기쁨", b(51, 0.15), C.gain)}
      />
      <Box x={panL.x} y={panL.y + 50} w={300} center>
        <div style={vis(f, a(50, 0.1))}>
          <Chip variant="loss" size={38}>
            잃을 때
          </Chip>
        </div>
      </Box>
      <Box x={panR.x} y={panR.y + 50} w={300} center>
        <div style={vis(f, a(50, 0.2))}>
          <Chip variant="gain" size={38}>
            얻을 때
          </Chip>
        </div>
      </Box>
      <Box x={960} y={262} w={600} center>
        <div style={vis(f, b(51, 0.45))}>
          <Label size={60} weight={900}>
            <Hi at={b(51, 0.6)}>두 배 정도</Hi>
          </Label>
        </div>
      </Box>
    </>
  );
};

// ── S19 문장 52–55: 전 재산 → 매일 고통(요일 7칸) → 하루 수십 번 앱 → (뒷줄) 밤 · 미국 장 · 잠 설침 → 팔아야 할 때 못 팖 · 기다려야 할 때 못 기다림 → "어떻게 투자해야 할까?" ──
const DAYS = ["월", "화", "수", "목", "금", "토", "일"];
export const S19: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  const p53 = a(53);
  const p54 = a(54);
  const p55 = a(55);
  const tw = 7 * 190 + 6 * 20;
  return (
    <>
      <div style={{position: "absolute", inset: 0, opacity: fadeOut(f, p55)}}>
        <NumberTitle no="04" at={STATIC} title={T04} />
      </div>
      {/* 52: 전 재산이 걸리면 매일 */}
      <div style={{position: "absolute", inset: 0, opacity: fadeOut(f, p53)}}>
        <Box x={960} y={290} w={1400} center>
          <div style={{display: "flex", justifyContent: "center", alignItems: "center", gap: 24, ...vis(f, a(52))}}>
            <Chip size={44}>전 재산</Chip>
            <Label size={52} weight={900}>
              → 매일
            </Label>
          </div>
        </Box>
        {DAYS.map((d, i) => (
          <Box key={d} x={960 - tw / 2 + i * 210} y={420}>
            <div style={vis(f, a(52, 0.3) + i * 4)}>
              <div style={{width: 190, height: 220, boxSizing: "border-box", border: `4px solid ${C.ink}`, borderRadius: 16, overflow: "hidden", background: C.light}}>
                <div style={{background: C.ink, color: C.light, textAlign: "center", fontWeight: 700, fontSize: 36, padding: "6px 0"}}>{d}</div>
                <div style={{height: 160, display: "flex", alignItems: "center", justifyContent: "center"}}>
                  <Label size={40} weight={900} color={C.loss}>
                    고통
                  </Label>
                </div>
              </div>
            </div>
          </Box>
        ))}
      </div>
      {/* 53: 하루 수십 번 앱 → (뒷줄) 밤에 미국 장, 잠 설침 */}
      <div style={{position: "absolute", inset: 0, opacity: enter(f, p53) * fadeOut(f, p54)}}>
        <Box x={250} y={300}>
          <MiniPhone at={p53} w={220} />
        </Box>
        <Box x={530} y={360}>
          <div style={vis(f, a(53, 0.2))}>
            <Label size={48}>하루</Label>
            <Big size={150} style={{marginTop: 8}}>
              {F.manyTimes.v}
            </Big>
          </div>
        </Box>
        <Box x={1080} y={290}>
          <div style={vis(f, b(53))}>
            <div style={{position: "relative", width: 640, height: 400, borderRadius: 26, background: C.navy, color: C.inkOnNavy, padding: "34px 40px", boxSizing: "border-box"}}>
              <div style={{display: "flex", alignItems: "center", gap: 22}}>
                <Moon size={80} />
                <Label size={52} weight={900} color={C.inkOnNavy}>
                  밤
                </Label>
              </div>
              <div style={{position: "absolute", right: 50, top: 40}}>
                <MiniPhone at={b(53, 0.1)} w={180} dark>
                  <Label size={30} color={C.ink}>
                    {F.usMarket.v}
                  </Label>
                  <div style={{marginTop: 14, height: 30, borderRadius: 8, background: C.ink}} />
                </MiniPhone>
              </div>
              <div style={{position: "absolute", left: 40, bottom: 40}}>
                <CrossLabel at={b(53, 0.55)} size={48} color={C.inkOnNavy}>
                  잠
                </CrossLabel>
              </div>
            </div>
          </div>
        </Box>
      </div>
      {/* 54: 팔아야 할 때 못 팔고, 기다려야 할 때 못 기다림 */}
      <div style={{position: "absolute", inset: 0, opacity: enter(f, p54) * fadeOut(f, p55)}}>
        {[
          {x: 200, head: "팔아야 할 때", no: "못 팖", at: a(54, 0.05)},
          {x: 1000, head: "기다려야 할 때", no: "못 기다림", at: a(54, 0.5)},
        ].map((c) => (
          <Box key={c.head} x={c.x} y={330}>
            <div style={vis(f, c.at)}>
              <Card style={{width: 720, height: 300, boxSizing: "border-box", display: "flex", flexDirection: "column", justifyContent: "center", gap: 24}}>
                <Label size={60} weight={900}>
                  {c.head}
                </Label>
                <CrossLabel at={c.at + 12} size={52}>
                  {c.no}
                </CrossLabel>
              </Card>
            </div>
          </Box>
        ))}
      </div>
      {/* 55: 그렇다면 어떻게? */}
      <Box x={960} y={390} w={1600} center>
        <div style={vis(f, p55)}>
          <Headline size={88}>그렇다면 어떻게?</Headline>
        </div>
      </Box>
    </>
  );
};
