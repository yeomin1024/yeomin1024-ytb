// 문제 분석 파트 S10–S20 (문장 27–58)
import React from "react";
import {useCurrentFrame} from "remotion";
import {C} from "../../../design/tokens";
import {count, enter, prog} from "../../../components/anim";
import {num, won} from "../../../components/fmt";
import {Arrow, Big, Box, Card, Chip, CornerNote, Headline, Hi, Label, Mark, fadeOut, vis} from "../../../components/ui";
import {Bubble, NumberTitle} from "../../../components/cards";
import {Bars, Dot, HRule, Layer, Line, P, PtLabel, YearLine} from "../../../components/charts";
import {F, PRICE} from "../facts";
import {DateTag, DayTile, DotRow, HATCH, LIGHT_GAIN, Target, Waffle, StrikeAt} from "../local";
import {THOUGHT_REBUY} from "./host";
import {SceneC} from "./story";

const STATIC = -60; // 같은 항목의 이어지는 장면: 번호 타이틀이 이미 떠 있음

// 번호 타이틀 문구 (같은 항목은 같은 문구, S31 두 열 요약도 같은 이름)
export const T01 = "크게 오르는 날은 크게 떨어진 날 바로 뒤에";
export const T02 = "한번 팔면 다시 사기 훨씬 어렵다";
export const T03 = "바닥은 지나고 나서야 보인다";
export const T04 = "사고판 시점 때문에 수익이 줄어든다";

// ── S10 문장 27–31: "01" → 사례 카드 2장 (2026년 3월 4일 -12% 넘게 → 하루 뒤 약 +10% / 2020년 코로나 3월 19일 -8% 넘게 → 다음 날 +7% 넘게) ──
const K = 13; // 하루 등락률 1%당 막대 길이(px), 두 카드 같은 비율
type Day = {pct: number; day: string; val: string; at: number; valAt: number};
const DayPairCard: React.FC<{x: number; head: React.ReactNode; at: number; down: Day; up: Day; tag?: {text: string; at: number}}> = ({x, head, at, down, up, tag}) => {
  const f = useCurrentFrame();
  const z = 280; // 0% 선 (카드 안 y)
  const dh = Math.abs(down.pct) * K * prog(f, down.at, 16);
  const uh = up.pct * K * prog(f, up.at, 16);
  const DX = 110;
  const UX = 470;
  const BW = 150;
  const lab: React.CSSProperties = {position: "absolute", width: BW + 160, textAlign: "center"};
  return (
    <Box x={x} y={262}>
      <div style={vis(f, at)}>
        <Card style={{width: 780, height: 530, boxSizing: "border-box", padding: 0, position: "relative"}}>
          <div style={{position: "absolute", left: 40, top: 26, display: "flex", alignItems: "center", gap: 18}}>{head}</div>
          <div style={{position: "absolute", left: 40, right: 40, top: z - 3, height: 6, background: C.ink, opacity: enter(f, down.at)}} />
          {/* 떨어진 날 */}
          <div style={{position: "absolute", left: DX, top: z, width: BW, height: dh, background: C.loss, borderRadius: "0 0 10px 10px"}} />
          <div style={{...lab, left: DX - 80, top: z - 58, opacity: enter(f, down.at)}}>
            <Label size={38}>{down.day}</Label>
          </div>
          <div style={{...lab, left: DX - 80, top: z + Math.abs(down.pct) * K + 10, opacity: enter(f, down.valAt)}}>
            <Label size={50} weight={900} color={C.loss}>
              {down.val}
            </Label>
          </div>
          {/* 다음 날 */}
          <div style={{position: "absolute", left: UX, top: z - uh, width: BW, height: uh, background: C.gain, borderRadius: "10px 10px 0 0"}} />
          <div style={{...lab, left: UX - 80, top: z + 12, opacity: enter(f, up.at)}}>
            <Label size={38}>{up.day}</Label>
          </div>
          <div style={{...lab, left: UX - 80, top: z - up.pct * K - 70, opacity: enter(f, up.valAt)}}>
            <Label size={50} weight={900} color={C.gain}>
              {up.val}
            </Label>
          </div>
          {tag ? (
            <div style={{position: "absolute", left: 290, top: 372, ...vis(f, tag.at)}}>
              <Chip variant="outline" size={32}>
                {tag.text}
              </Chip>
            </div>
          ) : null}
        </Card>
      </div>
    </Box>
  );
};
export const S10: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  return (
    <>
      <NumberTitle
        no="01"
        at={a(27)}
        title={
          <>
            크게 오르는 날은
            <span style={{opacity: enter(f, b(27))}}>
              {" "}
              크게 떨어진 날 <Hi at={b(27, 0.45)}>바로 뒤에</Hi>
            </span>
          </>
        }
      />
      <DayPairCard
        x={140}
        at={a(28)}
        head={
          <>
            <DateTag>{F.crashYear.v}</DateTag>
            <Label size={40}>코스피</Label>
          </>
        }
        down={{pct: PRICE.kDrop0304, day: F.crashDay.v, val: `-${F.kospiDrop.v}% 넘게`, at: a(28, 0.15), valAt: a(28, 0.3)}}
        up={{pct: PRICE.kRise0305, day: "하루 뒤", val: `약 +${F.kospiNext.v}%`, at: a(29, 0.1), valAt: a(29, 0.4)}}
        tag={{text: "역사상 최대 하락률", at: a(28, 0.55)}}
      />
      <DayPairCard
        x={1000}
        at={a(30)}
        head={
          <>
            <DateTag>{F.covidYear.v} 코로나</DateTag>
            <Label size={40}>코스피</Label>
          </>
        }
        down={{pct: PRICE.kDrop2020, day: F.covidDay.v, val: `-${F.covidDrop.v}% 넘게`, at: a(31, 0.05), valAt: a(31, 0.25)}}
        up={{pct: PRICE.kRise2020, day: "다음 날", val: `+${F.covidRise.v}% 넘게`, at: a(31, 0.55), valAt: a(31, 0.7)}}
      />
    </>
  );
};

// ── S11 문장 32–34: JP모건(미국 자산운용사) → S&P 500, 2006년부터 20년 → 계속 투자 8,000만 원 넘게 vs 가장 많이 오른 10일 놓침 3,600만 원 ──
export const S11: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  const out = a(33);
  const hAll = 1;
  const hMiss = PRICE.jpmMiss / PRICE.jpmAll;
  const hStart = 10000 / PRICE.jpmAll; // 1,000만 원 = $10,000 기준 (비율)
  const baseY = 720;
  const maxH = 370;
  const vAll = count(f, a(33, 0.45), F.jpmStart.v, F.jpmAll.v, 26);
  const vMiss = count(f, a(34, 0.4), F.jpmStart.v, F.jpmMiss.v, 26);
  return (
    <>
      <NumberTitle no="01" at={STATIC} title={T01} />
      <div style={{position: "absolute", inset: 0, opacity: fadeOut(f, out)}}>
        <Box x={140} y={330}>
          <div style={vis(f, a(32))}>
            <Card style={{width: 700}}>
              <Label size={40} weight={500} color={C.gray}>
                미국 자산운용사
              </Label>
              <Big size={140} style={{marginTop: 12}}>
                {F.jpm.v}
              </Big>
            </Card>
          </div>
        </Box>
        <Box x={1040} y={300}>
          <div style={vis(f, b(32))}>
            <Chip size={44}>{F.index.v} 지수</Chip>
          </div>
        </Box>
        <YearLine x0={1080} x1={1660} y={600} from={`${F.jpmFrom.v}년`} to={`${F.jpmTo.v}년`} at={b(32, 0.15)} mid={<Big size={110}>{F.jpmYears.v}년</Big>} />
      </div>
      <div style={{position: "absolute", inset: 0, opacity: enter(f, out)}}>
        <Bars
          x={520}
          baseY={baseY}
          maxH={maxH}
          barW={240}
          gap={420}
          items={[
            {
              h: hMiss,
              color: LIGHT_GAIN,
              at: a(34, 0.4),
              label: (
                <>
                  가장 많이 오른 <Hi at={a(34, 0.15)}>10일</Hi> 놓침
                </>
              ),
              top: (
                <Label size={58} weight={900} color={C.gain}>
                  {won(vMiss)}
                </Label>
              ),
            },
            {
              h: hAll,
              color: C.gain,
              at: a(33, 0.45),
              label: "계속 투자",
              top: (
                <Label size={58} weight={900} color={C.gain}>
                  {won(vAll)} 넘게
                </Label>
              ),
            },
          ]}
        />
        <HRule y={baseY - maxH * hStart} x0={460} x1={1500} at={a(33, 0.1)} labelAt="right">
          <Label size={36} weight={500}>
            처음 {won(F.jpmStart.v)}
          </Label>
        </HRule>
        <CornerNote at={out} y={770}>
          출처: {F.jpm.v}
        </CornerNote>
      </div>
    </>
  );
};

// ── S12 문장 35–36: 가장 많이 오른 10일(점 10개) → 6개 강조, 6일 = 가장 크게 떨어진 10일과 2주 안 → 폭락한 날 매도 → 바로 뒤 반등 놓침 ──
export const S12: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const out = a(36);
  const d = 96;
  const gap = 34;
  const x0 = 960 - (10 * d + 9 * gap) / 2;
  const x6 = x0 + 6 * d + 5 * gap;
  const bp = prog(f, a(35, 0.35), 12);
  return (
    <>
      <NumberTitle no="01" at={STATIC} title={T01} />
      <Box x={960} y={262} w={1200} center>
        <div style={vis(f, a(35))}>
          <Label size={44}>가장 많이 오른 {F.bestDays.v}일</Label>
        </div>
      </Box>
      <DotRow x={x0} y={340} d={d} gap={gap} at={a(35)} hiAt={a(35, 0.35)} k={F.nearWorst.v} color={C.gain} />
      {/* 6개 묶음 괄호 */}
      <div style={{position: "absolute", left: x0, top: 456, width: (x6 - x0) * bp, height: 22, borderLeft: `6px solid ${C.ink}`, borderBottom: `6px solid ${C.ink}`, borderRight: bp > 0.95 ? `6px solid ${C.ink}` : undefined, borderRadius: "0 0 8px 8px", opacity: enter(f, a(35, 0.35))}} />
      <div style={{position: "absolute", inset: 0, opacity: fadeOut(f, out)}}>
        <Box x={x0} y={500} w={x6 - x0} center={false}>
          <div style={{width: x6 - x0, textAlign: "center", ...vis(f, a(35, 0.45))}}>
            <Big size={180}>{F.nearWorst.v}일</Big>
          </div>
        </Box>
        <Box x={x6 + 40} y={540}>
          <div style={vis(f, a(35, 0.6))}>
            <Label size={44}>가장 크게 떨어진 10일과</Label>
            <Label size={56} weight={900}>
              <Hi at={a(35, 0.75)} until={out}>
                {F.twoWeeks.v}
              </Hi>
            </Label>
          </div>
        </Box>
      </div>
      {/* 36: 폭락한 날 매도 → 바로 뒤 반등 놓침 */}
      <Box x={420} y={520}>
        <div style={vis(f, out)}>
          <DayTile w={440} h={240} top="폭락한 날" tone="loss" date="매도" />
        </div>
      </Box>
      <Box x={900} y={612}>
        <Arrow dir="right" len={120} at={a(36, 0.3)} />
      </Box>
      <Box x={1060} y={520}>
        <div style={vis(f, a(36, 0.35))}>
          <DayTile w={440} h={240} top="바로 뒤" date={<span style={{color: C.gain}}>반등</span>}>
            <div style={{display: "flex", alignItems: "center", gap: 10, opacity: enter(f, a(36, 0.6))}}>
              <Mark kind="cross" at={a(36, 0.6)} size={46} color={C.ink} />
              <Label size={44} weight={900}>
                <Hi at={a(36, 0.7)}>놓침</Hi>
              </Label>
            </div>
          </DayTile>
        </div>
      </Box>
    </>
  );
};

// ── S13 문장 37–39: "02" → 판 가격(3월 4일) → (뒷줄) 다음 날 다시 살 가격 +11% 넘게 → "내가 틀렸다고 인정해야 하나…" ──
export const S13: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  return (
    <>
      <NumberTitle
        no="02"
        at={a(37)}
        title={
          <>
            한번 팔면 다시 사기 <Hi at={a(37, 0.6)}>훨씬 어렵다</Hi>
          </>
        }
      />
      <Box x={240} y={400}>
        <div style={vis(f, a(38))}>
          <Card style={{width: 520}}>
            <Label size={36} weight={500} color={C.gray}>
              {F.crashDay.v}
            </Label>
            <Label size={64} weight={900}>
              판 가격
            </Label>
          </Card>
        </div>
      </Box>
      <Box x={800} y={472}>
        <Arrow dir="right" len={180} at={b(38)} color={C.gain} />
      </Box>
      <Box x={1020} y={258}>
        <div style={vis(f, b(38, 0.1))}>
          <Card style={{width: 680}}>
            <Label size={36} weight={500} color={C.gray}>
              다음 날
            </Label>
            <Label size={64} weight={900}>
              다시 살 가격
            </Label>
            <Big size={120} color={C.gain} style={{marginTop: 10}}>
              +{F.nextDayRise.v}% 넘게
            </Big>
          </Card>
        </div>
      </Box>
      <Box x={240} y={612}>
        <Bubble at={a(39, 0.05)} size={46}>
          내가 틀렸다고 인정해야 하나…
        </Bubble>
      </Box>
    </>
  );
};

// ── S14 문장 40–41: 미국 MIT 연구진 · 2003년부터 13년 → (뒷줄) 증권 계좌 65만여 개 → 패닉셀 = 한 달 사이 주식 90% 넘게 정리 ──
export const S14: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  const shrink = prog(f, a(41, 0.35), 22);
  const BW = 900;
  return (
    <>
      <NumberTitle no="02" at={STATIC} title={T02} />
      <Box x={140} y={270}>
        <div style={vis(f, a(40))}>
          <Card style={{width: 1640, boxSizing: "border-box", padding: "34px 52px"}}>
            <div style={{display: "flex", alignItems: "center", gap: 26}}>
              <Label size={56} weight={900}>
                미국 {F.mit.v}
              </Label>
              <div style={vis(f, a(40, 0.3))}>
                <Chip size={40}>
                  {F.mitFrom.v}년부터 {F.mitYears.v}년
                </Chip>
              </div>
            </div>
            <div style={{display: "flex", alignItems: "baseline", gap: 30, marginTop: 10, opacity: enter(f, b(40))}}>
              <Label size={56}>증권 계좌</Label>
              <Big size={170}>{F.accounts.v}</Big>
            </div>
          </Card>
        </div>
      </Box>
      <Box x={140} y={688}>
        <div style={vis(f, a(41))}>
          <Label size={56} weight={900}>
            <Hi at={a(41, 0.75)}>패닉셀</Hi>
          </Label>
        </div>
      </Box>
      <Box x={480} y={636}>
        <div style={vis(f, a(41, 0.1))}>
          <Label size={38}>{F.panicMonth.v} 주식</Label>
        </div>
      </Box>
      <div style={{position: "absolute", left: 480, top: 690, width: BW, height: 64, border: `4px solid ${C.ink}`, borderRadius: 12, overflow: "hidden", background: HATCH, boxSizing: "border-box", opacity: enter(f, a(41, 0.1))}}>
        <div style={{position: "absolute", left: 0, top: 0, bottom: 0, width: `${100 - 92 * shrink}%`, background: C.ink}} />
      </div>
      <Box x={BW + 500} y={694}>
        <div style={vis(f, a(41, 0.5))}>
          <Label size={48} weight={900}>
            {F.panicPct.v}% 넘게 정리
          </Label>
        </div>
      </Box>
    </>
  );
};

// ── S15 문장 42–43: 10×10 와플 31칸 → 31% 다시 주식으로 돌아오지 않음 → S07의 말풍선 "잠잠해지면 다시 사면 되지" + ✗ ──
export const S15: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const v = count(f, a(42, 0.2), 0, F.neverBack.v, 24);
  return (
    <>
      <NumberTitle no="02" at={STATIC} title={T02} />
      <Waffle x={170} y={290} n={F.neverBack.v} at={a(42)} fillAt={a(42, 0.2)} />
      <Box x={760} y={280}>
        <div style={vis(f, a(42))}>
          <Label size={44}>패닉셀 중</Label>
        </div>
      </Box>
      <Box x={760} y={340}>
        <div style={{display: "flex", alignItems: "center", gap: 40, opacity: enter(f, a(42, 0.2))}}>
          <Big size={200}>
            <Hi at={a(42, 0.7)}>{num(v)}%</Hi>
          </Big>
          <div style={vis(f, a(42, 0.45))}>
            <Label size={48}>다시 주식으로</Label>
            <Label size={48}>돌아오지 않음</Label>
          </div>
        </div>
      </Box>
      <Box x={760} y={610}>
        <Bubble at={a(43, 0.05)} size={44}>
          {THOUGHT_REBUY}
        </Bubble>
      </Box>
      <Box x={1650} y={606}>
        <Mark kind="cross" at={a(43, 0.45)} size={110} color={C.ink} />
      </Box>
    </>
  );
};

// ── S16 문장 44–47: "03" → 코스피 실제 지수: 3월 4일 판 날(점선) → 3월 31일 5,052 더 낮음 → 한 달도 안 돼 +30% 넘게 ──
const kx = (d: number) => 360 + d * 24; // 3/4부터 지난 날 수 (달력 기준 비율)
const ky = (v: number) => 700 - (v - 5000) * (400 / 1700);
const K0304: P = [kx(0), ky(PRICE.k0304)];
const K0305: P = [kx(1), ky(PRICE.k0305)];
const K0331: P = [kx(27), ky(PRICE.k0331)];
const K0427: P = [kx(54), ky(PRICE.k0427)];
export const S16: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  return (
    <>
      <NumberTitle
        no="03"
        at={a(44)}
        title={
          <>
            바닥은 <Hi at={a(44, 0.5)}>지나고 나서야</Hi> 보인다
          </>
        }
      />
      <Box x={360} y={268}>
        <div style={vis(f, a(45))}>
          <Chip size={38}>코스피</Chip>
        </div>
      </Box>
      <HRule y={K0304[1]} x0={K0304[0]} x1={1720} at={a(45, 0.3)} color={C.gray} />
      <Layer>
        <Line pts={[K0304, K0305]} at={a(46)} dur={8} color={C.gain} width={7} />
        <Line pts={[K0305, K0331]} at={a(46, 0.12)} dur={22} color={C.loss} width={7} />
        <Line pts={[K0331, K0427]} at={a(47, 0.05)} dur={26} color={C.gain} width={7} />
        <Dot p={K0304} at={a(45)} color={C.ink} />
        <Dot p={K0331} at={a(46, 0.5)} color={C.loss} />
        <Dot p={K0427} at={a(47, 0.5)} color={C.gain} />
      </Layer>
      <PtLabel p={K0304} at={a(45)} anchor="left">
        <div style={{textAlign: "right"}}>
          <Label size={38}>{F.crashDay.v}</Label>
          <Label size={38} weight={900}>
            판 날
          </Label>
        </div>
      </PtLabel>
      <PtLabel p={K0331} at={a(46, 0.5)} anchor="bottom" gap={22}>
        <div style={{display: "flex", alignItems: "baseline", gap: 14}}>
          <Label size={40}>{F.kospiLowDay.v}</Label>
          <Label size={56} weight={900} color={C.loss}>
            {num(F.kospiLow.v)}
          </Label>
          <Label size={36} weight={500} color={C.loss}>
            더 낮음
          </Label>
        </div>
      </PtLabel>
      <PtLabel p={K0427} at={a(47, 0.5)} anchor="top">
        <div style={{textAlign: "right"}}>
          <Label size={40}>한 달도 안 돼</Label>
          <Label size={64} weight={900} color={C.gain}>
            +{F.rebound30.v}% 넘게
          </Label>
        </div>
      </PtLabel>
      <CornerNote at={a(45)} y={770}>
        실제 지수 · 일부 날짜만 연결
      </CornerNote>
    </>
  );
};

// ── S17 문장 48–49: 더 싸게 다시 사려면 파는 날 ✓ + 사는 날 ✓ 둘 다 → 겁에 질린 날에는 둘 다 ? ──
const DayTarget: React.FC<{x: number; label: string; at: number; checkAt: number; qAt: number}> = ({x, label, at, checkAt, qAt}) => {
  const f = useCurrentFrame();
  return (
    <Box x={x} y={350}>
      <div style={vis(f, at)}>
        <Card style={{width: 560, height: 390, boxSizing: "border-box", position: "relative", display: "flex", flexDirection: "column", alignItems: "center", gap: 22}}>
          <Label size={56} weight={900}>
            {label}
          </Label>
          <div style={{position: "relative"}}>
            <Target size={190} at={at} />
            <div style={{position: "absolute", right: -130, top: 40, opacity: fadeOut(f, qAt)}}>
              <Mark kind="check" at={checkAt} size={110} color={C.ink} />
            </div>
            <div style={{position: "absolute", right: -130, top: 10, fontFamily: "NotoSerifKR", fontWeight: 900, fontSize: 140, lineHeight: 1, color: C.ink, ...vis(f, qAt)}}>?</div>
          </div>
        </Card>
      </div>
    </Box>
  );
};
export const S17: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const q = a(49, 0.3);
  return (
    <>
      <NumberTitle no="03" at={STATIC} title={T03} />
      <Box x={960} y={262} w={1600} center>
        <div style={{...vis(f, a(48)), opacity: enter(f, a(48)) * fadeOut(f, a(49))}}>
          <Label size={48}>
            더 싸게 다시 사려면 → <Hi at={a(48, 0.7)} until={a(49)}>둘 다</Hi> 맞혀야
          </Label>
        </div>
      </Box>
      <Box x={960} y={262} w={1600} center>
        <div style={vis(f, a(49))}>
          <div style={{display: "inline-block", background: C.loss, color: "#FFFFFF", fontWeight: 700, fontSize: 44, padding: "8px 30px", borderRadius: 12}}>겁에 질린 날</div>
        </div>
      </Box>
      <DayTarget x={300} label="파는 날" at={a(48, 0.2)} checkAt={a(48, 0.35)} qAt={q} />
      <div style={{position: "absolute", left: 900, top: 490, fontFamily: "NotoSansKR", fontWeight: 900, fontSize: 90, ...vis(f, a(48, 0.45))}}>+</div>
      <DayTarget x={1060} label="사는 날" at={a(48, 0.45)} checkAt={a(48, 0.6)} qAt={q + 6} />
    </>
  );
};

// ── S18 문장 50–53: "04" → 모닝스타 · 2024년까지 10년 미국 펀드 → 펀드 자체 연 8.2% vs 투자자 연 7.0% → 1.2%p → 전체 수익의 15% 정도 사라짐 ──
export const S18: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  const baseY = 720;
  const maxH = 240;
  const hF = 1;
  const hI = F.investorRet.v / F.fundRet.v;
  const topF = baseY - maxH * hF;
  const topI = baseY - maxH * hI;
  const bx = 960;
  const bp = prog(f, a(53, 0.1), 12);
  const lost = prog(f, b(53, 0.15), 16);
  const PW = 580;
  return (
    <>
      <NumberTitle
        no="04"
        at={a(50)}
        title={
          <>
            사고판 시점 때문에<span style={{opacity: enter(f, b(50))}}> 수익이 줄어든다</span>
          </>
        }
      />
      <Box x={140} y={258}>
        <div style={vis(f, a(51))}>
          <Card style={{width: 1640, boxSizing: "border-box", padding: "20px 44px", display: "flex", alignItems: "center", gap: 26}}>
            <Label size={56} weight={900}>
              {F.morningstar.v}
            </Label>
            <Label size={36} weight={500} color={C.gray}>
              미국 펀드 평가사
            </Label>
            <Chip size={36}>{F.msTo.v}년까지</Chip>
            <div style={vis(f, b(51))}>
              <Chip variant="outline" size={36}>
                {F.msYears.v}년 · 미국 펀드
              </Chip>
            </div>
          </Card>
        </div>
      </Box>
      <Bars
        x={260}
        baseY={baseY}
        maxH={maxH}
        barW={220}
        gap={200}
        items={[
          {h: hI, color: LIGHT_GAIN, at: b(52), label: "투자자가 번 돈", top: <Label size={54} weight={900} color={C.gain}>연 {F.investorRet.v.toFixed(1)}%</Label>},
          {h: hF, color: C.gain, at: a(52, 0.1), label: "펀드 자체", top: <Label size={54} weight={900} color={C.gain}>연 {F.fundRet.v}%</Label>},
        ]}
      />
      {/* 53: 차이 1.2%p */}
      <div style={{position: "absolute", left: 480, top: topI - 3, width: (bx - 480) * bp, borderTop: `5px dashed ${C.ink}`}} />
      <div style={{position: "absolute", left: 900, top: topF - 3, width: (bx - 900) * bp, borderTop: `5px dashed ${C.ink}`}} />
      <div style={{position: "absolute", left: bx - 3, top: topF, width: 6, height: (topI - topF) * bp, background: C.ink}} />
      <Box x={bx + 24} y={topF - 8}>
        <div style={vis(f, a(53, 0.2))}>
          <Label size={52} weight={900}>
            {F.gapPt.v}%p
          </Label>
        </div>
      </Box>
      {/* (뒷줄) 전체 수익의 15% 정도가 사라짐 */}
      <Box x={1230} y={470}>
        <div style={vis(f, b(53))}>
          <Label size={40}>전체 수익</Label>
          <div style={{position: "relative", marginTop: 14, width: PW, height: 90, border: `4px solid ${C.ink}`, borderRadius: 12, overflow: "hidden", boxSizing: "border-box", background: C.gain}}>
            <div style={{position: "absolute", right: 0, top: 0, bottom: 0, width: PW * 0.15 * lost, background: C.light}}>
              <div style={{position: "absolute", inset: 0, background: HATCH}} />
            </div>
          </div>
          <div style={{marginTop: 18, textAlign: "right", ...vis(f, b(53, 0.35))}}>
            <Label size={56} weight={900}>
              <Hi at={b(53, 0.5)}>{F.gapShare.v}% 정도</Hi>
            </Label>
            <Label size={38}>사고판 시점 때문에 사라짐</Label>
          </div>
        </div>
      </Box>
    </>
  );
};

// ── S19 문장 54–56: 긴 하락장도 있다 → 2008년 금융위기 코스피 1년 만에 절반 넘게 ↓ → 이전 고점까지 3년 넘게 ──
const gx = (yr: number) => 300 + yr * 390; // 2007-10-31부터 지난 해 (실제 시간 비율)
const gy = (v: number) => 720 - (v - 900) * (380 / 1170);
const G0: P = [gx(0), gy(PRICE.k2007peak)];
const G1: P = [gx(0.98), gy(PRICE.k2008low)];
const G2: P = [gx(3.18), gy(PRICE.k2011back)];
export const S19: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const bp = prog(f, a(56, 0.4), 18);
  const by = G0[1] - 46;
  return (
    <>
      <Box x={140} y={124}>
        <div style={vis(f, a(54))}>
          <Headline size={76}>긴 하락장도 있다</Headline>
        </div>
      </Box>
      <Box x={780} y={142}>
        <div style={vis(f, a(55))}>
          <Chip size={40}>{F.gfcYear.v} 금융위기 · 코스피</Chip>
        </div>
      </Box>
      <HRule y={G0[1]} x0={G0[0]} x1={G2[0] + 20} at={a(56)} color={C.gray} labelAt="right">
        <Label size={40} color={C.gray}>
          이전 고점
        </Label>
      </HRule>
      <Layer>
        <Line pts={[G0, G1]} at={a(55, 0.15)} dur={24} color={C.loss} />
        <Line pts={[G1, G2]} at={a(56, 0.1)} dur={30} color={C.gain} />
        <Dot p={G0} at={a(55, 0.15)} color={C.ink} />
        <Dot p={G1} at={a(55, 0.6)} color={C.loss} />
        <Dot p={G2} at={a(56, 0.5)} color={C.gain} />
      </Layer>
      <PtLabel p={G1} at={a(55, 0.6)} anchor="bottom" gap={24}>
        <Label size={44} weight={900} color={C.loss}>
          1년 만에 {F.gfcDrop.v} ↓
        </Label>
      </PtLabel>
      {/* 3년 넘게 괄호 */}
      <div style={{position: "absolute", left: G0[0], top: by, width: (G2[0] - G0[0]) * bp, height: 20, borderTop: `6px solid ${C.ink}`, borderLeft: `6px solid ${C.ink}`, borderRight: bp > 0.95 ? `6px solid ${C.ink}` : undefined, borderRadius: "8px 8px 0 0"}} />
      <Box x={(G0[0] + G2[0]) / 2} y={by - 74} w={600} center>
        <div style={vis(f, a(56, 0.6))}>
          <Label size={56} weight={900}>
            {F.gfcRecover.v}
          </Label>
        </div>
      </Box>
      <CornerNote at={a(55)} y={770}>
        실제 지수 · 일부 날짜만 연결
      </CornerNote>
    </>
  );
};

// ── S20 문장 57–58: 무조건 버티기(취소선) → (뒷줄) 겁이 결정하지 않도록 미리 세운 기준 → "하락장에서는 어떻게?" ──
export const S20: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  const out = a(58);
  return (
    <>
      <div style={{position: "absolute", inset: 0, opacity: fadeOut(f, out)}}>
        <Box x={180} y={330}>
          <div style={vis(f, a(57))}>
            <Card style={{width: 700, height: 300, boxSizing: "border-box", display: "flex", alignItems: "center", justifyContent: "center"}}>
              <Headline size={76} color={C.gray}>
                <StrikeAt at={a(57, 0.45)} color={C.ink}>
                  무조건 버티기
                </StrikeAt>
              </Headline>
            </Card>
          </div>
        </Box>
        <Box x={1040} y={330}>
          <div style={vis(f, b(57))}>
            <Card style={{width: 700, height: 300, boxSizing: "border-box", display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", gap: 16}}>
              <Label size={40} weight={500} color={C.gray}>
                겁이 결정하지 않도록
              </Label>
              <Headline size={76}>
                <Hi at={b(57, 0.45)}>미리 세운 기준</Hi>
              </Headline>
            </Card>
          </div>
        </Box>
      </div>
      <Box x={960} y={380} w={1600} center>
        <div style={vis(f, out)}>
          <Headline size={88}>하락장에서는 어떻게?</Headline>
        </div>
      </Box>
    </>
  );
};
