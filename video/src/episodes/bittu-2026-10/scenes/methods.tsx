// 올바른 방법 파트 S22–S29 (문장 57–84) + 마무리 S30 (문장 85–88), 밝은 크림 배경
import React from "react";
import {interpolate, useCurrentFrame} from "remotion";
import {C} from "../../../design/tokens";
import {count, enter, prog} from "../../../components/anim";
import {num, won} from "../../../components/fmt";
import {Arrow, Big, Box, Card, Chip, Headline, Hi, Label, Mark, fadeOut, vis} from "../../../components/ui";
import {NumberTitle} from "../../../components/cards";
import {HRule} from "../../../components/charts";
import {Balance, CheckRow, Weight} from "../../../components/objects";
import {F} from "../facts";
import {DayStrip, LeverageCard, ValueBar} from "../local";
import {SceneC} from "./story";

const STATIC = -60;
const CLAMP = {extrapolateLeft: "clamp", extrapolateRight: "clamp"} as const;
const T1 = "빌리기 전에, 반대매매 가격부터 계산";
const T2 = "빌리는 돈은 내 돈의 일부만";
const T5 = "미수는 쓰지 않기";

// S22 문장 57–59: "첫째" → 산 가격 선 / 반대매매 가격 = ? → 내 돈만큼 빌렸다면 / (뒷줄) -30% → 담보 140% 아래 → 233만 3천 원 × 70% = 163만 3천 원
export const S22: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  const yTop = 430;
  const yBot = 690;
  const solved = f >= a(59, 0.35);
  return (
    <>
      <NumberTitle no="첫째" at={a(57)} title={T1} />
      <HRule y={yTop} x0={200} x1={1380} at={a(57, 0.3)} color={C.ink} />
      <HRule y={yBot} x0={200} x1={1380} at={a(57, 0.5)} color={C.loss} />
      <Box x={200} y={yTop - 74}>
        <div style={vis(f, a(57, 0.3))}>
          <Label size={48}>
            산 가격<span style={{opacity: enter(f, a(59))}}> · {F.buyPrice.v}</span>
          </Label>
        </div>
      </Box>
      <Box x={200} y={yBot - 190}>
        <div style={vis(f, a(57, 0.5))}>
          <Label size={44} color={C.loss}>
            반대매매 가격
          </Label>
          <div style={{display: "flex", alignItems: "baseline", gap: 26, height: 116}}>
            <Big size={110} color={C.loss}>
              {solved ? F.callPrice.v : "?"}
            </Big>
            <div style={vis(f, a(59, 0.45))}>
              <Label size={52} weight={900}>
                = 산 가격 <Hi at={a(59, 0.6)}>× {F.pct70.v}%</Hi>
              </Label>
            </div>
          </div>
        </div>
      </Box>
      <Box x={1260} y={262}>
        <div style={vis(f, a(58))}>
          <Chip variant="outline" size={42}>
            내 돈만큼 빌렸다면
          </Chip>
        </div>
      </Box>
      <Box x={1420} y={yTop + 8}>
        <Arrow dir="down" len={yBot - yTop - 16} at={b(58)} color={C.loss} stroke={7} />
      </Box>
      <Box x={1500} y={yTop + 50}>
        <div style={vis(f, b(58, 0.2))}>
          <Label size={72} weight={900} color={C.loss}>
            -{F.callPct.v}%
          </Label>
          <Label size={40} style={{marginTop: 6}}>
            담보 {F.keep.v}% 아래
          </Label>
        </div>
      </Box>
    </>
  );
};

// S23 문장 60–61: 6월 23일 SK하이닉스 하루 -12% 넘게 → 거리 막대: 하루 10% 넘게 / (뒷줄) 반대매매 가격까지 -30%, 생각보다 가까운 거리
export const S23: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  const d = count(f, a(60, 0.3), 0, -F.jun23Drop.v, 22);
  const X0 = 200;
  const W = 1300; // = 30%
  const fill = (W * F.jun23Drop.v) / F.callPct.v;
  const track = prog(f, b(61), 16);
  return (
    <>
      <NumberTitle no="첫째" at={STATIC} title={T1} />
      <Box x={X0} y={270}>
        <div style={vis(f, a(60))}>
          <Chip size={42}>
            {F.jun23.v} · {F.stock.v}
          </Chip>
        </div>
        <div style={{display: "flex", alignItems: "baseline", gap: 24, marginTop: 10, opacity: enter(f, a(60, 0.3))}}>
          <Label size={56}>하루</Label>
          <Big size={170} color={C.loss}>
            {num(d)}%
          </Big>
          <Label size={56}>넘게</Label>
        </div>
      </Box>
      <Box x={X0} y={548}>
        <div style={vis(f, a(61))}>
          <Label size={40} weight={900} color={C.loss}>
            하루 {F.daily10.v}% 넘게
          </Label>
        </div>
      </Box>
      <div style={{position: "absolute", right: 1920 - (X0 + W), top: 548, textAlign: "right", ...vis(f, b(61))}}>
        <Label size={40} weight={900}>
          반대매매 가격까지 -{F.callPct.v}%
        </Label>
      </div>
      <div style={{position: "absolute", left: X0, top: 606, width: W * track, height: 84, boxSizing: "border-box", border: `4px dashed ${C.ink}`, borderRadius: 10, opacity: enter(f, b(61))}} />
      <div style={{position: "absolute", left: X0, top: 606, width: fill * prog(f, a(61, 0.1), 16), height: 84, background: C.loss, borderRadius: 10}} />
      <Box x={960} y={712} w={1600} center>
        <div style={vis(f, b(61, 0.3))}>
          <Label size={56} weight={900}>
            {F.callPct.v}%는 <Hi at={b(61, 0.45)}>생각보다 가까운 거리</Hi>
          </Label>
        </div>
      </Box>
    </>
  );
};

// 반대매매 가격까지 떨어져야 하는 폭 — 두 줄 거리 막대 (S24·S25에서 같은 모양)
const DROW_X = 580;
const DROW_W = 900; // = 100%
const DropRows: React.FC<{at1: number; at2: number; hiAt?: number; until?: number; marks?: {line: number; cross: number; check: number}}> = ({at1, at2, hiAt, until, marks}) => {
  const f = useCurrentFrame();
  const rows = [
    {label: "내 돈만큼 빌림", pct: F.callPct.v, color: C.gray, at: at1, y: 340, mark: "cross" as const, text: "강제 매도", tone: C.loss},
    {label: `${won(F.borrow600.v)}만 빌림`, pct: F.call77.v, color: C.ink, at: at2, y: 550, mark: "check" as const, text: "안 팔림", tone: C.ink},
  ];
  const lineX = DROW_X + (DROW_W * F.stockDrop.v) / 100;
  return (
    <div style={{position: "absolute", inset: 0, opacity: fadeOut(f, until)}}>
      <Box x={140} y={262}>
        <div style={vis(f, at1)}>
          <Label size={36} weight={500} color={C.gray}>
            반대매매 가격까지 주가가 떨어져야 하는 폭
          </Label>
        </div>
      </Box>
      {rows.map((r, i) => {
        const v = count(f, r.at + 6, 0, -r.pct, 22);
        return (
          <div key={i} style={{position: "absolute", left: 0, top: r.y, width: 1920, ...vis(f, r.at)}}>
            <div style={{position: "absolute", left: 140, top: 0, width: 420}}>
              <Label size={42} color={i === 0 ? C.gray : C.ink}>
                {r.label}
              </Label>
              <Big size={100} color={i === 0 ? C.gray : C.ink} style={{marginTop: 6}}>
                {i === 1 && hiAt !== undefined ? <Hi at={hiAt} until={until}>{num(v)}%</Hi> : `${num(v)}%`}
              </Big>
            </div>
            <div style={{position: "absolute", left: DROW_X, top: 50, width: DROW_W, height: 70, boxSizing: "border-box", border: `4px solid ${C.ink}`, borderRadius: 10, background: "transparent"}} />
            <div style={{position: "absolute", left: DROW_X, top: 50, width: (DROW_W * r.pct * prog(f, r.at + 6, 22)) / 100, height: 70, background: r.color, borderRadius: 10}} />
            {marks ? (
              <div style={{position: "absolute", left: DROW_X + DROW_W + 40, top: 46, display: "flex", alignItems: "center", gap: 12, ...vis(f, i === 0 ? marks.cross : marks.check)}}>
                <Mark kind={r.mark} at={i === 0 ? marks.cross : marks.check} size={62} color={r.tone} />
                <Label size={44} weight={900} color={r.tone}>
                  {r.text}
                </Label>
              </div>
            ) : null}
          </div>
        );
      })}
      {marks ? (
        <>
          <div style={{position: "absolute", left: lineX - 3, top: 330, height: 360, borderLeft: `6px dashed ${C.loss}`, opacity: enter(f, marks.line)}} />
          <div style={{position: "absolute", left: lineX, top: 702, transform: "translateX(-50%)", whiteSpace: "nowrap", ...vis(f, marks.line)}}>
            <Label size={46} weight={900} color={C.loss}>
              {F.sale30.v} 약 -{F.stockDrop.v}%
            </Label>
          </div>
        </>
      ) : null}
    </div>
  );
};

// S24 문장 62–65: "둘째" → 예시 내 돈의 20%까지(같은 계좌 카드, 간단형) → 3,000만 원에 600만 원 → 거리 막대 -30% vs -77%
export const S24: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const sw = a(65);
  const debt = count(f, a(63, 0.35), 0, F.borrow600.v, 20);
  const nums = f >= a(64, 0.2);
  return (
    <>
      <NumberTitle no="둘째" at={a(62)} title={T2} />
      <div style={{position: "absolute", inset: 0, opacity: fadeOut(f, sw)}}>
        <Box x={140} y={300}>
          <div style={vis(f, a(63, 0.2))}>
            <LeverageCard
              compact
              own={F.own.v}
              debt={debt}
              pnl={null}
              header={nums ? `주식 ${won(F.value3600.v)}어치` : ""}
              ownLabel={nums ? undefined : "내 돈"}
              debtLabel={nums ? `빌린 돈 ${won(F.borrow600.v)}` : "빌린 돈"}
            />
          </div>
        </Box>
        <Box x={1240} y={320}>
          <div style={vis(f, a(63))}>
            <Chip variant="outline" size={40}>
              예시
            </Chip>
          </div>
          <div style={{marginTop: 24, ...vis(f, a(63, 0.2))}}>
            <Label size={60} weight={900}>
              내 돈의 {F.borrowPct.v}%까지
            </Label>
          </div>
        </Box>
      </div>
      <DropRows at1={sw} at2={sw + 10} hiAt={a(65, 0.6)} />
    </>
  );
};

// S25 문장 66–68: S24 거리 막대 + 7월 30일 약 -42% 선 (위 ✗ 강제 매도, 아래 ✓ 안 팔림) → 천칭 저울: 오를 때 수익 ↓ vs 폭락에도 계좌 유지
export const S25: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const sw = a(67);
  const angle = interpolate(f, [a(67, 0.3), a(67, 0.55), a(68, 0.35), a(68, 0.6)], [0, -9, -9, 13], CLAMP);
  return (
    <>
      <NumberTitle no="둘째" at={STATIC} title={T2} />
      <DropRows at1={STATIC} at2={STATIC} until={sw} marks={{line: a(66, 0.1), cross: a(66, 0.4), check: a(66, 0.62)}} />
      <div style={{position: "absolute", inset: 0, opacity: enter(f, sw)}}>
        <Balance
          cx={960}
          cy={400}
          angle={angle}
          at={sw}
          left={
            <Weight at={a(68, 0.2)} w={430}>
              폭락에도 계좌 유지
            </Weight>
          }
          right={
            <Weight at={a(67, 0.2)} color={C.gain} textColor="#FFFFFF" w={360}>
              오를 때 수익 ↓
            </Weight>
          }
        />
      </div>
    </>
  );
};

// S26 문장 69–72: "셋째" → 넣을 현금(따로) → 날짜 칸 7월 28일 문자 → 7월 29일 +600만 원 / (뒷줄) 140% 넘음 → 7월 30일 강제 매도 없음 / (뒷줄) 7월 31일 반등 → 없으면 덜 빌리기
export const S26: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  const sw = a(70);
  return (
    <>
      <NumberTitle no="셋째" at={a(69)} title="넣을 현금을 미리 떼어 두기" />
      <div style={{position: "absolute", inset: 0, opacity: fadeOut(f, sw)}}>
        <Box x={200} y={330}>
          <div style={vis(f, a(69, 0.25))}>
            <Label size={44}>투자</Label>
            <div style={{marginTop: 16}}>
              <ValueBar own={F.own.v} debt={F.debt.v} width={760} max={F.bought.v} height={96} />
            </div>
          </div>
        </Box>
        <Box x={1160} y={330}>
          <div style={vis(f, a(69, 0.45))}>
            <Label size={44} color={C.gray}>
              따로 떼어 둠
            </Label>
            <div style={{marginTop: 16, width: 520, height: 96, boxSizing: "border-box", border: `5px dashed ${C.ink}`, borderRadius: 12, display: "flex", alignItems: "center", justifyContent: "center"}}>
              <Label size={52} weight={900}>
                넣을 현금
              </Label>
            </div>
          </div>
        </Box>
      </div>
      <DayStrip
        x={140}
        y={290}
        boxW={392}
        gap={24}
        h={236}
        size={40}
        days={[
          {date: "7월 28일", at: sw, lines: [{text: "담보 부족 문자", at: sw + 4}]},
          {
            date: F.topUpDay.v,
            at: a(70, 0.3),
            lines: [
              {text: won(F.topUp.v, true), at: a(70, 0.4)},
              {text: `담보 ${F.keep.v}% 넘음`, at: b(70, 0.1), mark: "check"},
            ],
          },
          {date: F.saleDay.v, at: a(71), lines: [{text: "강제 매도 없음", at: a(71, 0.25), mark: "check"}]},
          {
            date: F.reboundDay.v,
            at: b(71),
            lines: [
              {text: "반등", at: b(71, 0.15), tone: "gain"},
              {text: `+${F.rebound.v}% 가까이`, at: b(71, 0.15), tone: "gain"},
            ],
          },
        ]}
      />
      <Box x={960} y={600} w={1600} center>
        <div style={vis(f, a(72))}>
          <Label size={60} weight={900}>
            넣을 현금이 없다면 → <Hi at={a(72, 0.4)}>덜 빌리기</Hi>
          </Label>
        </div>
      </Box>
    </>
  );
};

// S27 문장 73–78: "넷째" → 6월 22일 계좌 카드(+1,500만 원) → 3,000만 원어치 팔아 빚 상환 → 남은 주식 = 전부 내 돈 → 7월 폭락에도 강제 매도 없음 / (뒷줄) 7월 31일 -350만 원 정도 → 실제 사연 -2,500만 원과 비교, 2천만 원 넘게 차이
export const S27: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  const repayAt = a(75, 0.3);
  const debt = F.debt.v * (1 - prog(f, repayAt, 22));
  const repaid = f >= repayAt;
  const fall = count(f, b(77, 0.15), 0, F.remain731.v - F.remain.v, 26); // 4,500 → 2,650
  const own = F.remain.v + fall;
  const pnl = own - F.own.v;
  const cmp = a(78);
  return (
    <>
      <NumberTitle no="넷째" at={a(73)} title="수익이 나면 빚부터 갚기" />
      <div style={{position: "absolute", inset: 0, opacity: fadeOut(f, cmp)}}>
      <Box x={140} y={270}>
        <div style={vis(f, a(74))}>
          <LeverageCard
            own={own}
            debt={debt}
            pnl={pnl}
            pnlNote={
              <span style={{opacity: enter(f, b(77, 0.5))}}>
                <Label size={56}>정도</Label>
              </span>
            }
            header={
              <span style={{opacity: f < repayAt ? 1 : f < a(76) ? 1 - prog(f, repayAt, 8) : enter(f, a(76))}}>
                주식 {won(Math.max(0, own) + (f < a(76) && f >= repayAt ? F.debt.v : debt))}어치
              </span>
            }
            ownLabel={f >= a(76) ? "전부 내 돈" : undefined}
            debtLabel={repaid ? "빌린 돈 갚음" : undefined}
          />
        </div>
      </Box>
      <Box x={1230} y={290}>
        <div style={vis(f, a(74, 0.2), b(77))}>
          <Chip size={46}>{F.peakDay.v}</Chip>
        </div>
      </Box>
      <Box x={1230} y={290}>
        <div style={vis(f, b(77))}>
          <Chip size={46}>{F.reboundDay.v}</Chip>
        </div>
      </Box>
      <Box x={1230} y={420} w={594}>
        <div style={vis(f, a(75), a(76))}>
          <Label size={50} weight={900}>
            {won(F.repay.v)}어치 팔아
            <br />
            빚 상환
          </Label>
        </div>
      </Box>
      <Box x={1230} y={420} w={594}>
        <div style={vis(f, a(76), a(77))}>
          <Label size={50} weight={900}>
            남은 주식 =
            <br />
            <Hi at={a(76, 0.4)} until={a(77)}>
              전부 내 돈
            </Hi>
          </Label>
        </div>
      </Box>
      <Box x={1230} y={420} w={594}>
        <div style={{display: "flex", alignItems: "flex-start", gap: 14, ...vis(f, a(77))}}>
          <Mark kind="check" at={a(77, 0.1)} size={58} color={C.ink} />
          <Label size={50} weight={900}>
            7월 폭락에도
            <br />
            강제 매도 없음
          </Label>
        </div>
      </Box>
      </div>
      {/* 문장 78: 실제 사연 -2,500만 원(왼쪽, 나쁜 쪽) vs 빚부터 갚았다면 -350만 원 정도(오른쪽) — 계좌 카드와 같은 막대 무늬 */}
      <div style={{position: "absolute", left: 958, top: 300, width: 4, height: 370, background: C.gray, opacity: enter(f, cmp)}} />
      <CompareSide x={140} at={cmp} title="실제 사연" value={F.loss.v} own={F.left.v} />
      <CompareSide x={1000} at={cmp + 6} title="빚부터 갚았다면" value={F.loss350.v} own={F.remain731.v} note="정도" />
      <Box x={960} y={706} w={1600} center>
        <div style={vis(f, a(78, 0.5))}>
          <Label size={64} weight={900}>
            <Hi at={a(78, 0.62)}>{F.gap2000.v}</Hi> 차이
          </Label>
        </div>
      </Box>
    </>
  );
};

// S27 문장 78의 한쪽: 제목 · 손실 숫자 · 남은 내 돈 막대 (잉크 = 남은 돈, 파랑 점선 = 잃은 돈)
const CompareSide: React.FC<{x: number; at: number; title: string; value: number; own: number; note?: string}> = ({x, at, title, value, own, note}) => {
  const f = useCurrentFrame();
  return (
    <Box x={x} y={300}>
      <div style={{width: 780, textAlign: "center", ...vis(f, at)}}>
        <Label size={50}>{title}</Label>
        <div style={{display: "flex", justifyContent: "center", alignItems: "baseline", gap: 16, marginTop: 14}}>
          <Big size={140} color={C.loss}>
            {won(value)}
          </Big>
          {note ? <Label size={52}>{note}</Label> : null}
        </div>
        <div style={{display: "flex", justifyContent: "center", marginTop: 30}}>
          <ValueBar own={own} debt={0} width={640} max={F.own.v} height={70} />
        </div>
        <Label size={36} weight={500} color={C.gray} style={{marginTop: 12}}>
          남은 내 돈 {won(own)}
        </Label>
      </div>
    </Box>
  );
};

// S28 문장 79–81: "다섯째" → 날짜 칸: 산 날 → 이틀 뒤 결제일(돈 채워 넣기) / (뒷줄) 산 날 = 외상으로 삼 → 못 채우면 → 그다음 날 아침 반대매매
export const S28: SceneC = ({t}) => {
  const {a, b} = t;
  return (
    <>
      <NumberTitle no="다섯째" at={a(79)} title={T5} />
      <DayStrip
        x={140}
        y={320}
        boxW={520}
        gap={40}
        h={262}
        size={46}
        days={[
          {date: "산 날", at: a(80), lines: [{text: "외상으로 삼", at: b(80, 0.1)}]},
          {
            date: `${F.settle.v} · 결제일`,
            at: a(80, 0.3),
            lines: [
              {text: "돈 채워 넣기", at: a(80, 0.5)},
              {text: "못 채우면", at: a(81), mark: "cross", tone: "loss"},
            ],
          },
          {date: "그다음 날 아침", at: a(81, 0.35), lines: [{text: "반대매매", at: a(81, 0.45), tone: "loss"}]},
        ]}
      />
    </>
  );
};

// S29 문장 82–84: 30칸 달력(30일 동안 현금 100%) → 6월 한 달 증권사 10곳 미수 반대매매 / (뒷줄) 8,459억 원어치 → 며칠짜리 외상 ≠ 오래 들고 갈 주식
export const S29: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  const sw = a(83);
  const v = count(f, b(83) + 2, 0, F.misuSold.v, 26);
  const fillP = prog(f, a(82, 0.15), 36);
  const cells = Array.from({length: F.cashDays.v}, (_, i) => i);
  return (
    <>
      <NumberTitle no="다섯째" at={STATIC} title={T5} />
      <div style={{position: "absolute", inset: 0, opacity: fadeOut(f, sw)}}>
        <Box x={140} y={300}>
          <div style={{display: "grid", gridTemplateColumns: "repeat(10, 84px)", gap: 12, opacity: enter(f, a(82))}}>
            {cells.map((i) => (
              <div key={i} style={{width: 84, height: 70, borderRadius: 8, boxSizing: "border-box", border: `4px solid ${C.ink}`, background: i < fillP * F.cashDays.v ? C.ink : "transparent"}} />
            ))}
          </div>
        </Box>
        <Box x={1240} y={290}>
          <div style={vis(f, a(82, 0.1))}>
            <Big size={150}>{F.cashDays.v}일 동안</Big>
          </div>
          <div style={{marginTop: 22, ...vis(f, a(82, 0.4))}}>
            <Label size={52} weight={900}>
              현금 {F.cash100.v}% 있어야
              <br />
              주식을 살 수 있음
            </Label>
          </div>
        </Box>
      </div>
      <div style={{position: "absolute", inset: 0, opacity: enter(f, sw)}}>
        <Box x={960} y={262} w={1600} center>
          <Label size={44} weight={500} color={C.gray}>
            6월 한 달 · 증권사 {F.brokers.v}곳
          </Label>
          <Label size={52} style={{marginTop: 6}}>
            미수 반대매매로 팔린 주식
          </Label>
        </Box>
        <Box x={960} y={410} w={1600} center>
          <div style={{display: "flex", justifyContent: "center", alignItems: "baseline", gap: 18, ...vis(f, b(83))}}>
            <Big size={180}>{num(v)}억 원</Big>
            <Label size={56}>어치</Label>
          </div>
        </Box>
      </div>
      <Box x={960} y={650} w={1700} center>
        <div style={{display: "inline-flex", alignItems: "center", gap: 30, ...vis(f, a(84))}}>
          <Chip variant="outline" size={46}>
            며칠짜리 외상
          </Chip>
          <Label size={80} weight={900}>
            ≠
          </Label>
          <Chip variant="outline" size={46}>
            오래 들고 갈 주식
          </Chip>
        </div>
      </Box>
    </>
  );
};

// S30 문장 85–88: 두 열 요약 (위험한 이유 4 / 지킬 기준 5) → 카드 '빚을 내기 전에 ✓ 반대매매 가격부터 계산' → 성공 투자
const RISKS = ["손실도 똑같이 커짐", "가장 나쁜 때·가격에 팜", "이자가 매일 쌓임", "하락장에서 더 크게 잃음"];
const RULES = ["반대매매 가격부터 계산", "내 돈의 일부만 빌리기", "넣을 현금 떼어 두기", "수익 나면 빚부터 갚기", "미수는 쓰지 않기"];
export const S30: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const out = a(86);
  const end = t.dur - 20;
  const col = (title: string, items: string[], x: number, at0: number, numbered: (i: number) => string, nw: number) => (
    <Box x={x} y={150}>
      <div style={vis(f, at0)}>
        <Card style={{width: 780, boxSizing: "border-box", padding: "32px 44px"}}>
          <Headline size={56}>{title}</Headline>
          <div style={{marginTop: 18, display: "flex", flexDirection: "column", gap: 14}}>
            {items.map((s, i) => (
              <div key={s} style={{display: "flex", gap: 18, alignItems: "baseline", ...vis(f, at0 + 6 + i * 5)}}>
                <Label size={36} weight={900} color={C.gray} style={{minWidth: nw}}>
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
        {col("빚투가 위험한 이유", RISKS, 140, a(85, 0.05), (i) => `0${i + 1}`, 52)}
        {col("빚을 쓸 때 지킬 기준", RULES, 1000, a(85, 0.45), (i) => KO[i], 100)}
      </div>
      <div style={{position: "absolute", inset: 0, opacity: fadeOut(f, a(87))}}>
        <Box x={960} y={290} w={1000} center>
          <div style={{...vis(f, out), display: "inline-block", textAlign: "left"}}>
            <Card style={{width: 940, boxSizing: "border-box", padding: "40px 56px"}}>
              <Label size={44} weight={500} color={C.gray}>
                빚을 내기 전에
              </Label>
              <div style={{marginTop: 30}}>
                <CheckRow at={out + 6} checkAt={a(86, 0.55)} size={60} color={C.ink}>
                  반대매매 가격부터 계산
                </CheckRow>
              </div>
            </Card>
          </div>
        </Box>
      </div>
      <Box x={960} y={380} w={1000} center>
        <div style={{...vis(f, a(87, 0.1)), opacity: enter(f, a(87, 0.1)) * fadeOut(f, end)}}>
          <Headline size={88}>성공 투자</Headline>
        </div>
      </Box>
    </>
  );
};

