// 사연 파트 S01–S08 (문장 1–16) — 장면 구성표: stock/out/bittu-2026-10/scene_plan.md
import React from "react";
import {useCurrentFrame} from "remotion";
import {C} from "../../../design/tokens";
import {count, enter, prog, shake} from "../../../components/anim";
import {num, won} from "../../../components/fmt";
import {ST} from "../../../components/timeline";
import {Arrow, Big, Box, Card, Chip, CornerNote, Hi, Label, Mark, fadeOut, vis} from "../../../components/ui";
import {Bubble, NewsCard} from "../../../components/cards";
import {Dot, Layer, Line, P, PtLabel} from "../../../components/charts";
import {Phone} from "../../../components/objects";
import {F} from "../facts";
import {DayStrip, LeverageCard, Swatch} from "../local";

export type SceneC = React.FC<{t: ST}>;

// 계좌 카드 자리 (S02·S03·S05·S21에서 같은 자리·같은 모양)
export const CARD_X = 140;
export const CARD_Y = 170;
const RIGHT_X = 1230;
const OWN = F.own.v;
const DEBT = F.debt.v;

// 7월 30일 강제 매도 → 7월 31일 반등 날짜 칸 (S08·S17에서 같은 모양)
export const SaleDays: React.FC<{at: number; upAt: number; y?: number}> = ({at, upAt, y = 300}) => (
  <DayStrip
    x={330}
    y={y}
    boxW={560}
    gap={140}
    h={210}
    size={52}
    days={[
      {date: F.saleDay.v, at, lines: [{text: "강제 매도", at, tone: "loss"}]},
      {date: F.reboundDay.v, at: upAt, lines: [{text: `+${F.rebound.v}% 가까이`, at: upAt, tone: "gain"}]},
    ]}
  />
);

// S01 문장 1: 뉴스 카드 2026년 5월 SK하이닉스 주가 → +80% 넘게 (한 달 만에)
export const S01: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const v = count(f, a(1, 0.35), 0, F.mayUp.v, 28);
  return (
    <Box x={960} y={230} w={1100} center>
      <div style={{...vis(f, a(1)), display: "inline-block", textAlign: "left"}}>
        <NewsCard date={F.storyMonth.v} title={`${F.stock.v} 주가`} width={1000}>
          <div style={{display: "flex", alignItems: "center", gap: 28, marginTop: 20, opacity: enter(f, a(1, 0.35))}}>
            <Big size={210} color={C.gain}>
              +{num(v)}%
            </Big>
            <div>
              <Label size={56}>넘게</Label>
              <Label size={56} style={{whiteSpace: "nowrap"}}>
                한 달 만에
              </Label>
            </div>
          </div>
        </NewsCard>
      </div>
    </Box>
  );
};

// S02 문장 2–4: 계좌 카드 — 내 돈 3,000만 원 (+ 말풍선) → 빌린 돈 3,000만 원 = 6,000만 원어치 → 신용 거래 설명
export const S02: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const own = count(f, a(2, 0.1), 0, OWN, 20);
  const debtAt = a(3, 0.3);
  const debt = count(f, debtAt, 0, DEBT, 22);
  const bought = f >= debtAt;
  return (
    <>
      <Box x={CARD_X} y={CARD_Y}>
        <div style={vis(f, a(2))}>
          <LeverageCard own={own} debt={debt} pnl={F.pnlStart.v} pnlOpen={prog(f, a(3, 0.55), 14)} header={bought ? undefined : ""} />
        </div>
      </Box>
      <Box x={RIGHT_X + 20} y={250}>
        <Bubble at={a(2, 0.3)} until={a(3)} size={48}>
          {won(OWN)}만
          <br />
          넣기엔 아까워
        </Bubble>
      </Box>
      <Box x={RIGHT_X} y={230} w={594}>
        <div style={vis(f, a(4))}>
          <Chip size={52}>{F.credit.v}</Chip>
        </div>
        <div style={{marginTop: 40, ...vis(f, a(4, 0.25))}}>
          <Label size={52} weight={900}>
            산 주식 = 담보
          </Label>
        </div>
        <div style={{marginTop: 18, ...vis(f, a(4, 0.5))}}>
          <Label size={48}>→ 증권사 돈을 빌림</Label>
        </div>
      </Box>
    </>
  );
};

// S03 문장 5–7: 같은 카드 +1,500만 원 (6월 22일 · 290만 원 넘게) → 내 돈만이면 +750만 원, 빚 덕분에 ×2 → 수익 ×2 · 손실도 ×2
export const S03: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const upAt = a(5, 0.4);
  const g = count(f, upAt, 0, F.gain.v, 25);
  const out = a(7);
  return (
    <>
      <Box x={CARD_X} y={CARD_Y}>
        <LeverageCard own={OWN + g} debt={DEBT} pnl={g} />
      </Box>
      <Box x={RIGHT_X} y={180}>
        <div style={vis(f, a(5), out)}>
          <Chip size={40}>
            {F.peakDay.v} · {F.peakPrice.v} 넘게
          </Chip>
        </div>
      </Box>
      <Box x={RIGHT_X} y={300}>
        <div style={vis(f, a(6), out)}>
          <Card style={{width: 594, boxSizing: "border-box", padding: "30px 40px"}}>
            <Label size={40} weight={500} color={C.gray}>
              내 돈만 넣었다면
            </Label>
            <Big size={110} color={C.gray} style={{marginTop: 8}}>
              {won(F.gainOwnOnly.v, true)}
            </Big>
            <div style={{marginTop: 22, ...vis(f, a(6, 0.5))}}>
              <Label size={56} weight={900}>
                빚 덕분에 <Hi at={a(6, 0.62)} until={out}>×{F.times2.v}</Hi>
              </Label>
            </div>
          </Card>
        </div>
      </Box>
      <Box x={RIGHT_X} y={290}>
        <div style={{display: "flex", flexDirection: "column", gap: 44}}>
          <div style={vis(f, a(7, 0.1))}>
            <Chip variant="gain" size={60}>
              수익 ×{F.times2.v}
            </Chip>
          </div>
          <div style={vis(f, a(7, 0.5))}>
            <Chip variant="loss" size={60}>
              손실도 ×{F.times2.v}
            </Chip>
          </div>
        </div>
      </Box>
    </>
  );
};

// S04 문장 8–9 (네이비): 7월 28일 저녁 · 담보 부족 문자 → 추가로 넣을 돈 ✗
export const S04: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  return (
    <>
      <Box x={CARD_X} y={170}>
        <div style={vis(f, a(8))}>
          <Chip size={48}>{F.textDay.v}</Chip>
        </div>
      </Box>
      <Box x={330} y={270}>
        <Phone at={a(8, 0.1)} w={480} h={500}>
          <Label size={34} weight={500} color={C.gray}>
            문자
          </Label>
          <div style={{marginTop: 30, background: "#ECE6D8", borderRadius: 26, padding: "26px 30px", ...vis(f, a(8, 0.35))}}>
            <Label size={36} weight={500} color="#5F5B53">
              증권사
            </Label>
            <div style={{marginTop: 12, display: "inline-block", background: C.loss, color: "#FFFFFF", borderRadius: 12, padding: "8px 22px"}}>
              <Label size={60} weight={900} color="#FFFFFF">
                담보 부족
              </Label>
            </div>
          </div>
        </Phone>
      </Box>
      <Box x={1040} y={350}>
        <div style={vis(f, a(9))}>
          <Card style={{width: 700, boxSizing: "border-box", display: "flex", alignItems: "center", justifyContent: "space-between", padding: "40px 52px"}}>
            <Label size={60} weight={900}>
              추가로 넣을 돈
            </Label>
            <Mark kind="cross" at={a(9, 0.3)} size={110} color={C.loss} />
          </Card>
        </div>
      </Box>
    </>
  );
};

// S05 문장 10–11 (네이비): 이틀 뒤 아침 장 시작 → 같은 카드에 '전부 강제 매도' → 빚 갚고 남은 돈 500만 원, -2,500만 원
export const S05: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const hit = a(11, 0.15);
  const p = prog(f, hit, 28);
  const own = OWN + (F.left.v - OWN) * p;
  const debt = DEBT * (1 - prog(f, hit, 18));
  const pnl = count(f, hit, 0, F.loss.v, 28);
  const after = f >= hit;
  const stamp = (
    <div style={{...vis(f, a(10, 0.35), hit), display: "inline-block", background: C.loss, borderRadius: 14, padding: "14px 34px", transform: `${vis(f, a(10, 0.35), hit).transform} rotate(-3deg)`}}>
      <Label size={84} weight={900} color="#FFFFFF">
        전부 강제 매도
      </Label>
    </div>
  );
  return (
    <>
      <Box x={CARD_X} y={CARD_Y}>
        <LeverageCard
          own={own}
          debt={debt}
          pnl={after ? pnl : null}
          pnlSlot={after ? undefined : stamp}
          header=""
          ownLabel={after ? `남은 돈 ${won(F.left.v)}` : undefined}
          debtLabel={after ? `빌린 돈 ${won(DEBT)} 갚음` : undefined}
          shakeX={shake(f, hit + 28)}
        />
      </Box>
      <Box x={RIGHT_X} y={180}>
        <div style={vis(f, a(10))}>
          <Chip size={40}>{F.saleWhen.v} · 장 시작</Chip>
        </div>
      </Box>
    </>
  );
};

// S06 문장 12–13 (네이비): 7월 28일 하루 만에 코스피 -10% 넘게 / (뒷줄) SK하이닉스 -15% 가까이 → 중국 메모리 반도체 회사 상장 / (뒷줄) + AI 투자 걱정
const DropRow: React.FC<{name: string; pct: number; note: string; at: number}> = ({name, pct, note, at}) => {
  const f = useCurrentFrame();
  const v = count(f, at, 0, -pct, 22);
  return (
    <div style={{display: "flex", alignItems: "baseline", gap: 20, marginTop: 14, ...vis(f, at)}}>
      <Label size={46} style={{width: 260}}>
        {name}
      </Label>
      <Big size={118} color={C.loss}>
        {num(v)}%
      </Big>
      <Label size={40}>{note}</Label>
    </div>
  );
};
export const S06: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  return (
    <>
      <Box x={CARD_X} y={190}>
        <div style={vis(f, a(12))}>
          <NewsCard date={F.crashDay.v} title="하루 만에" width={820}>
            <DropRow name="코스피" pct={F.kospiDrop.v} note="넘게" at={a(12, 0.3)} />
            <DropRow name={F.stock.v} pct={F.skDrop.v} note="가까이" at={b(12)} />
          </NewsCard>
        </div>
      </Box>
      <Box x={1020} y={190}>
        <div style={vis(f, a(13))}>
          <NewsCard
            width={760}
            title={
              <>
                중국 메모리 반도체
                <br />
                회사 상장
              </>
            }
          >
            <div style={{marginTop: 26, ...vis(f, b(13))}}>
              <Label size={56} weight={900} color={C.loss}>
                + {F.cause2.v}
              </Label>
            </div>
          </NewsCard>
        </div>
      </Box>
    </>
  );
};

// S07 문장 14 (네이비): 실제 주가 흐름 — 산 날 → 6월 22일 → 7월 30일 시가(강제로 팔린 날) → 7월 31일 다음 날 +30% 가까이
// 값: README 실제 시세 (facts.pricePath). 날짜 간격은 실제와 다름, 숫자는 표시하지 않음
const yv = (won: number) => 690 - ((won - 1_300_000) / 1_650_000) * 480;
const UP1: P[] = [
  [200, yv(2_333_000)], // 5/29 산 날
  [560, yv(2_919_000)], // 6/22
];
const DOWN: P[] = [
  [560, yv(2_919_000)], // 6/22
  [660, yv(2_555_000)], // 6/23
  [1000, yv(1_816_000)], // 7/27
  [1130, yv(1_550_000)], // 7/28
  [1260, yv(1_401_000)], // 7/29
  [1390, yv(1_361_000)], // 7/30 시가 (강제 매도)
];
const UP2: P[] = [
  [1390, yv(1_361_000)],
  [1560, yv(1_718_000)], // 7/31
];
export const S07: SceneC = ({t}) => {
  const {a} = t;
  const sold = DOWN[DOWN.length - 1];
  const next = UP2[1];
  return (
    <>
      <Layer>
        <Line pts={UP1} at={a(14)} dur={12} color={C.gain} width={9} />
        <Line pts={DOWN} at={a(14) + 12} dur={26} color={C.loss} width={9} />
        <Dot p={sold} at={a(14, 0.22)} color={C.loss} />
        <Line pts={UP2} at={a(14, 0.48)} dur={16} color={C.gain} width={9} />
        <Dot p={next} at={a(14, 0.48) + 16} color={C.gain} />
      </Layer>
      <PtLabel p={sold} at={a(14, 0.22)} anchor="bottom">
        <Chip variant="loss" size={44}>
          강제로 팔린 날
        </Chip>
      </PtLabel>
      <PtLabel p={next} at={a(14, 0.55)} anchor="top">
        <Chip variant="gain" size={48}>
          다음 날 +{F.rebound.v}% 가까이
        </Chip>
      </PtLabel>
      <CornerNote at={a(14)} y={130}>
        실제 주가 흐름 · 날짜 간격은 실제와 다름
      </CornerNote>
    </>
  );
};

// S08 문장 15–16 (네이비): 빌린 돈 3,000만 원(수익 ×2) / (뒷줄) → 내 돈 3,000만 → 500만 원 → 빚만 없었다면, 그 하루 (7월 30일 → 7월 31일)
export const S08: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  const out = a(16);
  const ownV = count(f, b(15, 0.25), OWN, F.left.v, 28);
  return (
    <>
      <div style={{position: "absolute", inset: 0, opacity: fadeOut(f, out)}}>
        <Box x={CARD_X} y={250}>
          <div style={vis(f, a(15))}>
            <Card style={{width: 620, boxSizing: "border-box"}}>
              <Label size={44}>
                <Swatch kind="debt" size={34} />
                빌린 돈
              </Label>
              <Big size={120} style={{marginTop: 10}}>
                {won(DEBT)}
              </Big>
              <div style={{marginTop: 22, ...vis(f, a(15, 0.4))}}>
                <Chip variant="gain" size={46}>
                  수익 ×{F.times2.v}
                </Chip>
              </div>
            </Card>
          </div>
        </Box>
        <Box x={810} y={410}>
          <Arrow dir="right" len={170} at={b(15)} color={C.inkOnNavy} />
        </Box>
        <Box x={1040} y={250}>
          <div style={vis(f, b(15))}>
            <Card style={{width: 740, boxSizing: "border-box"}}>
              <Label size={44}>
                <Swatch kind="own" size={34} />내 돈
              </Label>
              <Big size={140} color={f >= b(15, 0.25) ? C.loss : C.ink} style={{marginTop: 10}}>
                {won(ownV)}
              </Big>
              <Label size={40} weight={500} color={C.gray} style={{marginTop: 14}}>
                처음 {won(OWN)}
              </Label>
            </Card>
          </div>
        </Box>
      </div>
      <Box x={960} y={190} w={1400} center>
        <div style={vis(f, out)}>
          <Label size={56} color={C.inkOnNavy}>
            빚만 없었다면
          </Label>
        </div>
      </Box>
      <SaleDays at={out + 4} upAt={out + 10} y={300} />
      <Box x={960} y={580} w={1400} center>
        <div style={vis(f, a(16, 0.35))}>
          <Label size={60} weight={900} color={C.inkOnNavy}>
            버틸 수 있었던 <Hi at={a(16, 0.5)}>그 하루</Hi>
          </Label>
        </div>
      </Box>
    </>
  );
};
