// 올바른 방법 파트 S21–S31 (문장 59–92), 밝은 크림 배경
import React from "react";
import {interpolate, useCurrentFrame} from "remotion";
import {C} from "../../../design/tokens";
import {count, enter, prog} from "../../../components/anim";
import {num, won} from "../../../components/fmt";
import {Arrow, Big, Box, Card, Chip, CornerNote, Headline, Hi, Label, Mark, fadeOut, vis} from "../../../components/ui";
import {NumberTitle} from "../../../components/cards";
import {Dot, HRule, Layer, Line, P} from "../../../components/charts";
import {CheckRow, Phone} from "../../../components/objects";
import {F, PRICE} from "../facts";
import {DateTag, DayTile, HATCH, Lock, MonthCal, MyAccount, PauseIcon, SplitBar, StrikeAt} from "../local";
import {SceneC, Tail} from "./story";

const STATIC = -60;
const CR = 864; // 오른쪽에 놓는 계좌 카드 x (S25·S27)

// 번호 타이틀 문구 (S31 두 열 요약도 같은 이름)
export const M1 = "1~2년 안에 쓸 돈은 넣지 않기";
export const M2 = "크게 떨어진 날엔 하루 기다리기";
export const M3 = "꼭 팔아야 한다면, 정해 둔 만큼만";
export const M4 = "다시 살 날짜와 금액도 정해 두기";
export const M5 = "계좌는 정해 둔 날에만 확인";

// ── S21 문장 59–61: "첫째" → 2008년 회복에 몇 년(S19 선과 같은 모양, 작게) → 꺼내 써야 할 돈이 주식에 묶임 → (뒷줄) 바닥에서라도 매도 ──
const mx = (yr: number) => 220 + yr * 190;
const my = (v: number) => 694 - (v - 900) * (290 / 1170);
const MG0: P = [mx(0), my(PRICE.k2007peak)];
const MG1: P = [mx(0.98), my(PRICE.k2008low)];
const MG2: P = [mx(3.18), my(PRICE.k2011back)];
export const S21: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  const bp = prog(f, a(60, 0.4), 16);
  const by = MG0[1] - 40;
  return (
    <>
      <NumberTitle
        no="첫째"
        at={a(59)}
        title={
          <>
            <Hi at={a(59, 0.5)}>1~2년</Hi> 안에 쓸 돈은 넣지 않기
          </>
        }
      />
      <Box x={140} y={262}>
        <div style={vis(f, a(60))}>
          <Card style={{width: 880, height: 528, boxSizing: "border-box", position: "relative", padding: 0}}>
            <div style={{position: "absolute", left: 36, top: 26}}>
              <DateTag>{F.gfcYear.v}</DateTag>
            </div>
          </Card>
        </div>
      </Box>
      <HRule y={MG0[1]} x0={MG0[0]} x1={MG2[0] + 10} at={a(60, 0.3)} color={C.gray} />
      <Layer>
        <Line pts={[MG0, MG1]} at={a(60, 0.1)} dur={16} color={C.loss} />
        <Line pts={[MG1, MG2]} at={a(60, 0.25)} dur={20} color={C.gain} />
        <Dot p={MG1} at={a(60, 0.2)} color={C.loss} />
      </Layer>
      <div style={{position: "absolute", left: MG0[0], top: by, width: (MG2[0] - MG0[0]) * bp, height: 18, borderTop: `6px solid ${C.ink}`, borderLeft: `6px solid ${C.ink}`, borderRight: bp > 0.95 ? `6px solid ${C.ink}` : undefined, borderRadius: "8px 8px 0 0"}} />
      <Box x={(MG0[0] + MG2[0]) / 2 + 60} y={by - 66} w={420} center>
        <div style={vis(f, a(60, 0.5))}>
          <Label size={46} weight={900}>
            회복에 몇 년
          </Label>
        </div>
      </Box>
      <Box x={MG1[0] - 40} y={MG1[1] + 24}>
        <div style={vis(f, b(61))}>
          <div style={{display: "inline-block", background: C.loss, color: "#FFFFFF", fontWeight: 700, fontSize: 36, padding: "6px 22px", borderRadius: 10}}>바닥에서라도 매도</div>
        </div>
      </Box>
      {/* 61: 꺼내 써야 할 돈이 주식에 묶임 */}
      <Box x={1100} y={300}>
        <div style={vis(f, a(61))}>
          <Card style={{width: 700, boxSizing: "border-box", position: "relative"}}>
            <Label size={44}>주식</Label>
            <div style={{marginTop: 22, height: 170, borderRadius: 16, background: C.ink, color: C.light, display: "flex", alignItems: "center", justifyContent: "center"}}>
              <Label size={52} weight={900} color={C.light}>
                꺼내 써야 할 돈
              </Label>
            </div>
            <div style={{position: "absolute", right: 30, top: 18}}>
              <Lock size={80} at={a(61, 0.45)} />
            </div>
          </Card>
        </div>
      </Box>
    </>
  );
};

// ── S22 문장 62–63: 예시 — S02의 계좌 카드(간단형) 4,000만 원 중 1년 안에 쓸 돈 1,000만 원은 빼고 → 주식 3,000만 원 ──
export const S22: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const split = a(62, 0.5);
  const stock = 1 - (F.spend.v / F.invest.v) * prog(f, split, 16);
  const segR = (F.spend.v / F.invest.v) * 864; // 막대 안쪽 폭 864 중 쓸 돈 부분
  return (
    <>
      <NumberTitle no="첫째" at={STATIC} title={M1} />
      <Box x={480} y={262}>
        <div style={vis(f, a(62))}>
          <MyAccount
            compact
            pnl={null}
            stock={stock}
            head={
              <div style={{display: "flex", alignItems: "center", gap: 16}}>
                <Chip variant="outline" size={32}>
                  예시
                </Chip>
                <Label size={40} weight={500} color={C.gray}>
                  {won(F.invest.v)}
                </Label>
              </div>
            }
            footR={<span style={{opacity: enter(f, split)}}>1년 안에 쓸 돈 {won(F.spend.v)}</span>}
          />
        </div>
      </Box>
      <Box x={528} y={590} w={864 - segR} center={false}>
        <div style={{width: 864 - segR, display: "flex", justifyContent: "center", alignItems: "baseline", gap: 20, ...vis(f, a(63, 0.15))}}>
          <Label size={52} style={{whiteSpace: "nowrap", flex: "none"}}>
            주식
          </Label>
          <Big size={170} style={{flex: "none"}}>
            <Hi at={a(63, 0.4)}>{won(F.stockOnly.v)}</Hi>
          </Big>
        </div>
      </Box>
    </>
  );
};

// ── S23 문장 64–67: "둘째" → 서킷브레이커 걸린 날(일시정지) → (뒷줄) 결정을 다음 날로 → 3월 5일에 팔았다면 -460만 원 vs 3월 4일 다 판 -800만 원 넘게, 절반 가까이 ──
export const S23: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  const out = a(66);
  const mv = prog(f, b(65, 0.3), 20);
  const chipX = interpolate(mv, [0, 1], [560, 1360]);
  const chipY = interpolate(mv, [0, 1], [584, 466]); // 왼쪽 칸 아래 → 다음 날 칸 가운데
  const lossR = count(f, b(66, 0.1), 0, F.delayLoss.v);
  const lossL = count(f, a(67, 0.15), 0, F.pnl0304.v);
  const k = 0.8; // 만 원 → px (막대)
  return (
    <>
      <NumberTitle
        no="둘째"
        at={a(64)}
        title={
          <>
            크게 떨어진 날엔{" "}
            <Hi at={a(64, 0.6)} until={out}>
              하루 기다리기
            </Hi>
          </>
        }
      />
      <div style={{position: "absolute", inset: 0, opacity: fadeOut(f, out)}}>
        <Box x={300} y={300}>
          <div style={vis(f, a(65))}>
            <DayTile w={520} h={370} top="서킷브레이커 걸린 날" tone="loss" date={<PauseIcon size={120} color={C.ink} />} />
          </div>
        </Box>
        <Box x={880} y={462}>
          <Arrow dir="right" len={170} at={b(65)} />
        </Box>
        <Box x={1100} y={300}>
          <div style={vis(f, b(65))}>
            <DayTile w={520} h={370} top="다음 날" date="" />
          </div>
        </Box>
        <div style={{position: "absolute", left: chipX, top: chipY, transform: "translateX(-50%)"}}>
          <div style={vis(f, b(65))}>
            <Chip size={46}>결정</Chip>
          </div>
        </div>
      </div>
      {/* 66–67: 화면 분할 — 왼쪽 3월 4일 다 판 실제 / 오른쪽 3월 5일에 팔았다면 */}
      <div style={{position: "absolute", left: 958, top: 290, width: 4, height: 440, background: C.gray, opacity: enter(f, a(67))}} />
      <Box x={1020} y={290}>
        <div style={vis(f, out)}>
          <Chip size={42}>{F.delayDay.v}에 팔았다면</Chip>
        </div>
        <div style={{marginTop: 26, opacity: enter(f, b(66))}}>
          <Big size={150} color={C.loss}>
            {won(lossR)}
          </Big>
          <div style={{marginTop: 26, height: 48, width: Math.abs(lossR) * k, background: C.loss, borderRadius: 8}} />
        </div>
        <div style={{marginTop: 26, ...vis(f, a(67, 0.5))}}>
          <Label size={56} weight={900}>
            <Hi at={a(67, 0.6)}>{F.halfish.v} ↓</Hi>
          </Label>
        </div>
      </Box>
      <Box x={140} y={290}>
        <div style={vis(f, a(67))}>
          <Chip variant="outline" size={42}>
            {F.crashDay.v} 전부 매도
          </Chip>
        </div>
        <div style={{marginTop: 26, opacity: enter(f, a(67, 0.1))}}>
          <div style={{display: "flex", alignItems: "baseline", gap: 14}}>
            <Big size={150} color={C.loss}>
              {won(lossL)}
            </Big>
            <Tail o={enter(f, a(67, 0.3))}>넘게</Tail>
          </div>
          <div style={{marginTop: 26, height: 48, width: Math.abs(lossL) * k * (Math.abs(F.pnl0304Exact.v) / Math.abs(F.pnl0304.v)), background: C.loss, borderRadius: 8}} />
        </div>
      </Box>
    </>
  );
};

// ── S24 문장 68–69: "셋째" → 막대 "전부"(취소선) → 3칸으로 나눔, 한 번에 1/3까지 ──
export const S24: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const X = 260;
  const W = 1400;
  const cut = prog(f, a(69, 0.3), 14);
  return (
    <>
      <NumberTitle no="셋째" at={a(68)} title={M3} />
      <Box x={X} y={318}>
        <div style={vis(f, a(68, 0.35))}>
          <Label size={64} weight={900} color={C.gray}>
            <StrikeAt at={a(68, 0.6)} color={C.ink}>
              전부
            </StrikeAt>
          </Label>
        </div>
      </Box>
      <div style={{position: "absolute", left: X, top: 420, width: W, height: 120, border: `4px solid ${C.ink}`, borderRadius: 14, overflow: "hidden", background: HATCH, boxSizing: "border-box", opacity: enter(f, a(68, 0.3))}}>
        <div style={{position: "absolute", left: 0, top: 0, bottom: 0, width: W - (W / 3) * cut, background: C.ink}} />
        {[1, 2].map((k) => (
          <div key={k} style={{position: "absolute", left: (W * k) / 3 - 3, top: 0, bottom: 0, width: 6, background: C.light, opacity: enter(f, a(69))}} />
        ))}
      </div>
      <Box x={X + (W * 5) / 6} y={566} w={640} center>
        <div style={vis(f, a(69, 0.35))}>
          <Label size={44}>한 번에</Label>
          <Big size={160}>
            <Hi at={a(69, 0.6)}>1/3까지</Hi>
          </Big>
        </div>
      </Box>
    </>
  );
};

// ── S25 문장 70–72: S02 계좌 카드 — 3월 4일 1/3만 매도 → (뒷줄) 4월 23일 -170만 원 정도 / 전부 판 사연자 -800만 원 넘게, 650만 원 가까이 적은 손실 / 틀려도 1/3만 ──
export const S25: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  const back = b(70);
  const pnl = f < back ? F.pnl0304.v : count(f, b(70, 0.15), F.pnl0304.v, F.partialPnl.v);
  const cut = prog(f, a(70, 0.4), 14);
  const wrong = a(72, 0.2);
  return (
    <>
      <NumberTitle no="셋째" at={STATIC} title={M3} />
      <Box x={CR} y={262}>
        <div style={vis(f, a(70))}>
          <MyAccount
            pnl={pnl}
            pnlNote={<Tail>{f < back ? "넘게" : "정도"}</Tail>}
            stock={1 - cut / 3}
            parts={3}
            head={<DateTag>{f < back ? F.crashDay.v : F.checkDay.v}</DateTag>}
            footL={<span style={{opacity: enter(f, a(70, 0.45))}}>삼성전자 2/3</span>}
            footR={
              f < wrong ? (
                <span style={{opacity: enter(f, a(70, 0.5))}}>판 1/3 → 현금</span>
              ) : (
                <span style={{color: C.ink, fontWeight: 900}}>
                  <Hi at={wrong + 4}>틀려도 1/3만</Hi>
                </span>
              )
            }
            barOverlay={
              <div style={{position: "absolute", right: (864 / 3 - 56) / 2, top: -2, opacity: enter(f, wrong)}}>
                <Mark kind="cross" at={wrong} size={52} color={C.ink} />
              </div>
            }
          />
        </div>
      </Box>
      <Box x={120} y={300}>
        <div style={vis(f, a(71))}>
          <Chip variant="outline" size={42}>
            전부 판 사연자
          </Chip>
          <div style={{display: "flex", alignItems: "baseline", gap: 12, marginTop: 26}}>
            <Big size={130} color={C.loss}>
              {won(F.pnl0304.v)}
            </Big>
            <Tail>넘게</Tail>
          </div>
        </div>
      </Box>
      <Box x={120} y={600}>
        <div style={vis(f, a(71, 0.45), wrong)}>
          <Label size={52} weight={900}>
            <Hi at={a(71, 0.6)} until={wrong}>
              손실 {won(F.partialBetter.v)} 가까이 ↓
            </Hi>
          </Label>
        </div>
      </Box>
    </>
  );
};

// ── S26 문장 73–75: "넷째" → 판 돈을 4주 동안 매주 금요일 1/4씩 (3월 6일·13일·20일·27일) → 평균 약 18만 8천 원 ──
const FRIDAYS = ["3월 6일", "3월 13일", "3월 20일", "3월 27일"];
const FRI_X = [270, 630, 990, 1350];
export const S26: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  return (
    <>
      <NumberTitle no="넷째" at={a(73)} title={M4} />
      {FRIDAYS.map((d, i) => (
        <Box key={d} x={FRI_X[i]} y={280}>
          <div style={vis(f, a(74, 0.25 + i * 0.12))}>
            <DayTile w={300} h={240} top="금요일" date={d}>
              <Label size={40} color={C.gray}>
                판 돈 {F.rebuyFrac.v}
              </Label>
            </DayTile>
          </div>
        </Box>
      ))}
      <Box x={960} y={566} w={1200} center>
        <div style={vis(f, a(75, 0.1))}>
          <Label size={44}>평균 다시 산 가격</Label>
        </div>
      </Box>
      <Box x={960} y={622} w={1400} center>
        <div style={vis(f, a(75, 0.3))}>
          <Big size={160}>
            <Hi at={a(75, 0.55)}>약 {F.rebuyAvg.v}</Hi>
          </Big>
        </div>
      </Box>
    </>
  );
};

// ── S27 문장 76–78: S02 계좌 카드 4월 23일 -190만 원 정도 / 다시 사지 않았다면 -800만 원 넘게, 600만 원 넘게 나음 → 금요일 4칸 ✓, 판 가격보다 비싸도 그대로 ──
const ry = (p: number) => 716 - (p - PRICE.sold) * 0.006;
export const S27: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const out = a(78);
  const pnl = count(f, a(76, 0.3), F.pnl0304.v, F.rebuyPnl.v);
  return (
    <>
      <NumberTitle no="넷째" at={STATIC} title={M4} />
      <div style={{position: "absolute", inset: 0, opacity: fadeOut(f, out)}}>
        <Box x={CR} y={262}>
          <div style={vis(f, a(76))}>
            <MyAccount
              pnl={pnl}
              pnlNote={<Tail o={enter(f, a(76, 0.6))}>정도</Tail>}
              stock={1}
              parts={4}
              head={<DateTag>{F.checkDay.v}</DateTag>}
              footL="금요일마다 1/4씩 다시 삼"
            />
          </div>
        </Box>
        <Box x={120} y={300}>
          <div style={vis(f, a(77))}>
            <Chip variant="outline" size={42}>
              다시 사지 않았다면
            </Chip>
            <div style={{display: "flex", alignItems: "baseline", gap: 12, marginTop: 26}}>
              <Big size={130} color={C.loss}>
                {won(F.pnl0304.v)}
              </Big>
              <Tail>넘게</Tail>
            </div>
          </div>
        </Box>
        <Box x={120} y={600}>
          <div style={vis(f, a(77, 0.45))}>
            <Label size={52} weight={900}>
              <Hi at={a(77, 0.6)} until={out}>
                {won(F.rebuyBetter.v)} 넘게 나음
              </Hi>
            </Label>
          </div>
        </Box>
      </div>
      {/* 78: 금요일 4칸 ✓ + 판 가격보다 비싼 실제 값 (점, 비율만) */}
      {FRIDAYS.map((d, i) => (
        <Box key={d} x={FRI_X[i]} y={262}>
          <div style={vis(f, out + i * 4)}>
            <DayTile w={300} h={210} top="금요일" date={d}>
              <Mark kind="check" at={a(78, 0.55) + i * 5} size={58} color={C.ink} />
            </DayTile>
          </div>
        </Box>
      ))}
      <HRule y={ry(PRICE.sold)} x0={240} x1={1640} at={a(78, 0.15)} color={C.gray} labelAt="right">
        <Label size={40} color={C.gray}>
          판 가격
        </Label>
      </HRule>
      {PRICE.rebuy.map((p, i) => {
        const x = FRI_X[i] + 150;
        const y = ry(p);
        const k = prog(f, a(78, 0.25) + i * 3, 12);
        return (
          <React.Fragment key={p}>
            <div style={{position: "absolute", left: x - 3, top: y + (ry(PRICE.sold) - y) * (1 - k), width: 6, height: (ry(PRICE.sold) - y) * k, background: C.gain}} />
            <div style={{position: "absolute", left: x - 15, top: y - 15, width: 30, height: 30, borderRadius: 99, background: C.gain, border: `4px solid ${C.light}`, opacity: k}} />
          </React.Fragment>
        );
      })}
      <Box x={960} y={740} w={1400} center>
        <div style={vis(f, a(78, 0.6))}>
          <Label size={44} weight={900}>
            판 가격보다 비싸도 <Hi at={a(78, 0.7)}>정해 둔 날 그대로</Hi>
          </Label>
        </div>
      </Box>
      <CornerNote at={out} y={130}>
        실제 종가 비율
      </CornerNote>
    </>
  );
};

// ── S28 문장 79–82: "다섯째" → 노벨 경제학상 리처드 탈러 교수 등 · (뒷줄) 1997년 실험 → 대학생, 가상의 주식|채권 나눠 넣기 → 결과를 보여 주는 횟수만 다르게 (매달 / 1년에 한 번) ──
export const S28: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  const share = interpolate(f, [a(81, 0.3), a(81, 0.55), a(81, 0.8), a(82)], [0.5, 0.64, 0.42, 0.55], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  return (
    <>
      <NumberTitle no="다섯째" at={a(79)} title={M5} />
      <Box x={140} y={262}>
        <div style={vis(f, a(80))}>
          <Card style={{width: 1640, boxSizing: "border-box", padding: "20px 44px", display: "flex", alignItems: "center", gap: 24}}>
            <Chip variant="outline" size={36}>
              노벨 경제학상
            </Chip>
            <Label size={56} weight={900}>
              {F.thaler.v}
            </Label>
            <div style={vis(f, b(80))}>
              <Chip size={38}>{F.thalerYear.v}년 실험</Chip>
            </div>
          </Card>
        </div>
      </Box>
      <Box x={140} y={420}>
        <div style={vis(f, a(81))}>
          <Label size={44}>{F.students.v} · 가상의 돈을 나눠 넣기</Label>
        </div>
      </Box>
      <Box x={140} y={488}>
        <SplitBar w={1640} h={90} share={share} at={a(81, 0.15)} />
      </Box>
      <Box x={140} y={640}>
        <div style={{display: "flex", alignItems: "center", gap: 24, ...vis(f, a(82))}}>
          <Label size={44}>결과 보기</Label>
          <Chip size={40}>매달</Chip>
          <div style={{display: "flex", gap: 8}}>
            {Array.from({length: 12}).map((_, i) => (
              <div key={i} style={{width: 30, height: 40, borderRadius: 6, background: C.ink, opacity: enter(f, a(82, 0.15) + i * 2)}} />
            ))}
          </div>
        </div>
      </Box>
      <Box x={1180} y={640}>
        <div style={{display: "flex", alignItems: "center", gap: 24, ...vis(f, a(82, 0.4))}}>
          <Chip variant="outline" size={40}>
            1년에 한 번
          </Chip>
          <div style={{width: 30, height: 40, borderRadius: 6, background: C.ink}} />
        </div>
      </Box>
    </>
  );
};

// ── S29 문장 83–85: 화면 분할 — 매달 본 학생 주식 41% (왼쪽) / 1년에 한 번 본 학생 70% 가까이 (오른쪽) → 자주 볼수록 겁, 가장 적게 벎 ──
export const S29: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const vL = count(f, a(83, 0.4), 0, F.monthlyStock.v);
  const vR = count(f, a(84, 0.35), 0, F.yearlyStock.v);
  return (
    <>
      <NumberTitle no="다섯째" at={STATIC} title={M5} />
      <div style={{position: "absolute", left: 958, top: 280, width: 4, height: 500, background: C.gray, opacity: enter(f, a(84))}} />
      <Box x={140} y={280}>
        <div style={vis(f, a(83))}>
          <Chip size={42}>매달 본 학생</Chip>
        </div>
        <div style={{display: "flex", alignItems: "baseline", gap: 18, marginTop: 14, opacity: enter(f, a(83, 0.4))}}>
          <Label size={48}>주식</Label>
          <Big size={160}>{num(vL)}%</Big>
        </div>
        <div style={{marginTop: 18}}>
          <SplitBar w={720} share={(F.monthlyStock.v / 100) * prog(f, a(83, 0.4), 24)} at={a(83, 0.4)} />
        </div>
        <div style={{marginTop: 26, ...vis(f, a(85))}}>
          <Label size={40} color={C.gray}>
            자주 볼수록 → 손실도 자주 보임 → 겁
          </Label>
        </div>
        <div style={{marginTop: 8, ...vis(f, a(85, 0.6))}}>
          <Label size={56} weight={900}>
            <Hi at={a(85, 0.7)}>가장 적게 벎</Hi>
          </Label>
        </div>
      </Box>
      <Box x={1020} y={280}>
        <div style={vis(f, a(84))}>
          <Chip variant="outline" size={42}>
            1년에 한 번 본 학생
          </Chip>
        </div>
        <div style={{display: "flex", alignItems: "baseline", gap: 18, marginTop: 14, opacity: enter(f, a(84, 0.35))}}>
          <Label size={48}>주식</Label>
          <Big size={160}>{num(vR)}%</Big>
          <Label size={48}>가까이</Label>
        </div>
        <div style={{marginTop: 18}}>
          <SplitBar w={720} share={(F.yearlyStock.v / 100) * prog(f, a(84, 0.35), 24)} at={a(84, 0.35)} />
        </div>
      </Box>
    </>
  );
};

// ── S30 문장 86–88: 3월·4월 달력, 마지막 금요일(3월 27일·4월 24일)에 동그라미 → -670만 원 / (뒷줄) +55만 원 → 3월 4일 칸(파랑)은 계좌 안 봄 ──
export const S30: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  const no = a(88, 0.2);
  return (
    <>
      <NumberTitle no="다섯째" at={STATIC} title={M5} />
      <MonthCal x={140} y={262} title="3월" firstDow={0} days={31} at={a(86)} ring={[{day: 27, at: a(86, 0.45)}]} mark={[{day: 4, at: no, color: C.loss}]} />
      <MonthCal x={650} y={262} title="4월" firstDow={3} days={30} at={a(86, 0.12)} ring={[{day: 24, at: a(86, 0.55)}]} />
      <Box x={650} y={666}>
        <div style={vis(f, a(86, 0.5))}>
          <Label size={40}>○ = 마지막 금요일</Label>
        </div>
      </Box>
      <Box x={140} y={666}>
        <div style={{display: "flex", alignItems: "center", gap: 12, ...vis(f, no)}}>
          <Mark kind="cross" at={no + 4} size={52} color={C.ink} />
          <Label size={42} weight={900}>
            <Hi at={a(88, 0.45)}>{F.crashDay.v} 계좌 안 봄</Hi>
          </Label>
        </div>
      </Box>
      <Box x={1200} y={280}>
        <div style={vis(f, a(87))}>
          <Label size={44}>{F.check1Day.v}</Label>
          <Big size={130} color={C.loss} style={{marginTop: 8}}>
            {won(count(f, a(87, 0.3), 0, F.check1.v))}
          </Big>
        </div>
      </Box>
      <Box x={1200} y={500}>
        <div style={vis(f, b(87))}>
          <Label size={44}>{F.check2Day.v}</Label>
          <Big size={130} color={C.gain} style={{marginTop: 8}}>
            {won(count(f, b(87, 0.2), 0, F.check2.v), true)}
          </Big>
        </div>
      </Box>
    </>
  );
};

// ── S31 문장 89–92: 두 열 요약 (위험한 이유 4 / (뒷줄) 지킬 기준 5) → 휴대폰 확인 (오늘 폭락한 날? / (뒷줄) 곧 써야 할 돈?) → 성공 투자 ──
const RISKS = ["오르는 날은 떨어진 날 바로 뒤에", "한번 팔면 다시 사기 어렵다", "바닥은 지나고 나서야 보인다", "사고판 시점이 수익을 줄인다"];
const RULES = ["1~2년 안에 쓸 돈은 넣지 않기", "크게 떨어진 날엔 하루 기다리기", "팔아도 정해 둔 만큼만", "다시 살 날짜·금액 정해 두기", "계좌는 정해 둔 날에만 확인"];
const KO = ["첫째", "둘째", "셋째", "넷째", "다섯째"];
export const S31: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  const out = a(90);
  const end = t.dur - 20;
  const col = (title: string, items: string[], x: number, at0: number, numbered: (i: number) => string) => (
    <Box x={x} y={170}>
      <div style={vis(f, at0)}>
        <Card style={{width: 820, boxSizing: "border-box", padding: "30px 40px"}}>
          <Headline size={56}>{title}</Headline>
          <div style={{marginTop: 18, display: "flex", flexDirection: "column", gap: 14}}>
            {items.map((s, i) => (
              <div key={s} style={{display: "flex", gap: 18, alignItems: "baseline", ...vis(f, at0 + 6 + i * 5)}}>
                <Label size={34} weight={900} color={C.gray} style={{minWidth: 100}}>
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
  return (
    <>
      <div style={{position: "absolute", inset: 0, opacity: fadeOut(f, out)}}>
        {col("위험한 이유", RISKS, 120, a(89, 0.05), (i) => `0${i + 1}`)}
        {col("지킬 기준", RULES, 980, b(89), (i) => KO[i])}
      </div>
      <div style={{position: "absolute", inset: 0, opacity: fadeOut(f, a(91))}}>
        <Box x={680} y={240}>
          <Phone at={out} w={560} h={430}>
            <Label size={36} weight={500} color={C.gray}>
              다 팔고 싶은 날
            </Label>
            <div style={{marginTop: 40, display: "flex", flexDirection: "column", gap: 40}}>
              <CheckRow at={a(90, 0.3)} checkAt={a(90, 0.75)} size={42} color={C.ink}>
                오늘 폭락한 날?
              </CheckRow>
              <CheckRow at={b(90)} checkAt={b(90, 0.6)} size={42} color={C.ink}>
                곧 써야 할 돈?
              </CheckRow>
            </div>
          </Phone>
        </Box>
      </div>
      <Box x={960} y={400} w={1000} center>
        <div style={{...vis(f, a(91, 0.1)), opacity: enter(f, a(91, 0.1)) * fadeOut(f, end)}}>
          <Headline size={88}>성공 투자</Headline>
        </div>
      </Box>
    </>
  );
};
