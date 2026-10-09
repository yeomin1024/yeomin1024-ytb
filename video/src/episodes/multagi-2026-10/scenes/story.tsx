// 사연 파트 S01–S06 (자막 1–14) — 장면 구성표: stock/out/multagi-2026-10/scene_plan.md
import React from "react";
import {useCurrentFrame} from "remotion";
import {C} from "../../../design/tokens";
import {count, enter, prog, shake} from "../../../components/anim";
import {num, won} from "../../../components/fmt";
import {ST} from "../../../components/timeline";
import {Arrow, Big, Box, Card, Chip, CornerNote, Label, Strike, fadeOut, vis} from "../../../components/ui";
import {AccountCard, Bubble, NewsCard, Seg} from "../../../components/cards";
import {Layer, Line, PtLabel} from "../../../components/charts";
import {PushButton} from "../../../components/objects";
import {F} from "../facts";

export type SceneC = React.FC<{t: ST}>;

// 계좌 카드 공통 값 (S02·S03·S05에서 같은 모양으로 재사용)
const ADD = "#5A5751"; // 물타기로 넣은 돈 조각 (처음 산 돈과 구분)
const STOCK = F.company.v;
const CARD_X = 140;
const CARD_Y = 170;
const RIGHT_X = 1250;

// S01 자막 1–3: 뉴스 카드(-22%) → 의료비↑·실적 전망↓ → 생각 말풍선
export const S01: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const d = count(f, a(1, 0.55), 0, -F.drop1.v);
  return (
    <>
      <Box x={150} y={200}>
        <div style={vis(f, a(1))}>
          <NewsCard date={F.storyMonth.v} title={`${F.company.v} 주가`} width={860} sub={<span style={{opacity: enter(f, a(2))}}>{F.biggest.v}</span>}>
            <div style={{display: "flex", alignItems: "baseline", gap: 26, marginTop: 18, opacity: enter(f, a(1, 0.55))}}>
              <Big color={C.loss}>{num(d)}%</Big>
              <Label size={44}>하루 만에</Label>
            </div>
          </NewsCard>
        </div>
      </Box>
      <Box x={1140} y={240} w={640}>
        <div style={{display: "flex", flexDirection: "column", alignItems: "center", gap: 18}}>
          <div style={vis(f, a(2, 0.3), a(3))}>
            <Chip variant="outline" size={52}>
              의료비 ↑
            </Chip>
          </div>
          <div style={{opacity: fadeOut(f, a(3))}}>
            <Arrow dir="down" len={110} at={a(2, 0.45)} />
          </div>
          <div style={vis(f, a(2, 0.6), a(3))}>
            <Chip variant="outline" size={52}>
              실적 전망 <span style={{color: C.loss}}>↓</span>
            </Chip>
          </div>
        </div>
      </Box>
      <Box x={1110} y={330}>
        <Bubble at={a(3, 0.15)} size={50}>
          큰 회사니까
          <br />
          지금이 싸게 살 때
        </Bubble>
      </Box>
    </>
  );
};

// S02 자막 4–5: 계좌 카드 (8,000만 원 중 5,000만 원 매수) → 일주일 만에 -200만 원
export const S02: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const buyAt = a(4, 0.45);
  const stock = count(f, buyAt, 0, F.first.v, 20);
  const pnl = f < buyAt ? null : count(f, a(5, 0.45), F.pnlStart.v, F.pnlWeek.v);
  return (
    <>
      <Box x={CARD_X} y={CARD_Y}>
        <div style={vis(f, a(4))}>
          <AccountCard total={F.saved.v} segs={[{v: stock}]} stockName={STOCK} pnl={pnl} />
        </div>
      </Box>
      <Box x={RIGHT_X} y={330}>
        <div style={vis(f, a(5))}>
          <Chip size={48}>{F.week.v}</Chip>
        </div>
      </Box>
    </>
  );
};

// S03 자막 6–8: 같은 계좌 카드에 물타기 ①② (+1,500만 원씩) → 평단 ↓ + "조금만 반등해도 본전"
export const S03: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const s1 = count(f, a(6, 0.5), 0, F.add1.v, 20);
  const s2 = count(f, a(7, 0.45), 0, F.add2.v, 20);
  const dim = prog(f, a(7), 10);
  const segs: Seg[] = [{v: F.first.v}, {v: s1, color: ADD}, {v: s2, color: ADD}];
  return (
    <>
      <Box x={CARD_X} y={CARD_Y}>
        <AccountCard
          total={F.saved.v}
          segs={segs}
          stockName={STOCK}
          pnl={F.pnlWeek.v}
          pnlDim={dim}
          pnlNote={<span style={{opacity: dim, color: C.loss, fontSize: 80, fontWeight: 900}}>▼</span>}
        />
      </Box>
      <Box x={RIGHT_X} y={250}>
        <div style={{display: "flex", flexDirection: "column", gap: 40}}>
          <div style={vis(f, a(6, 0.5), a(8))}>
            <Chip size={44}>물타기 ① {won(F.add1.v, true)}</Chip>
          </div>
          <div style={vis(f, a(7, 0.45), a(8))}>
            <Chip size={44}>물타기 ② {won(F.add2.v, true)}</Chip>
          </div>
        </div>
      </Box>
      <Box x={RIGHT_X} y={230}>
        <div style={vis(f, a(8))}>
          <Chip variant="outline" size={52}>
            평단 <span style={{color: C.loss}}>↓</span>
          </Chip>
        </div>
      </Box>
      <Box x={RIGHT_X - 30} y={400}>
        <Bubble at={a(8, 0.35)} size={50}>
          조금만 반등해도
          <br />
          본전
        </Bubble>
      </Box>
    </>
  );
};

// S04 자막 9: 개념도 — 기대한 반등(점선)은 오지 않고 선이 계속 내려감
export const S04: SceneC = ({t}) => {
  const {a} = t;
  const fall: [number, number][] = [
    [260, 300],
    [520, 420],
    [700, 385],
    [980, 560],
  ];
  return (
    <>
      <Layer>
        <Line pts={fall} at={a(9)} dur={20} color={C.loss} />
        <Line
          pts={[
            [980, 560],
            [1200, 430],
            [1400, 330],
          ]}
          at={a(9, 0.15)}
          dashed
        />
        <Line
          pts={[
            [980, 560],
            [1220, 640],
            [1300, 615],
            [1560, 730],
          ]}
          at={a(9, 0.45)}
          dur={24}
          color={C.loss}
        />
      </Layer>
      <PtLabel p={[1400, 330]} at={a(9, 0.15)} anchor="right" gap={44}>
        <Label size={52} color={C.gray}>
          <Strike at={a(9, 0.75)} color={C.ink}>
            반등
          </Strike>
        </Label>
      </PtLabel>
      <CornerNote at={a(9)}>개념도</CornerNote>
    </>
  );
};

// S05 자막 10–12 (네이비): 같은 계좌 카드 -200만 → -2,000만 원 + 흔들림, 뉴스 카드(전망 철회·CEO 사임, 약 -18%)
export const S05: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const hit = a(10, 0.6);
  const pnl = count(f, hit, F.pnlWeek.v, F.pnlCrash.v, 24);
  const d = count(f, a(12, 0.35), 0, -F.drop2.v);
  return (
    <>
      <Box x={CARD_X} y={CARD_Y}>
        <AccountCard
          total={F.saved.v}
          segs={[{v: F.first.v}, {v: F.add1.v, color: ADD}, {v: F.add2.v, color: ADD}]}
          stockName={STOCK}
          pnl={pnl}
          pnlDim={1 - prog(f, hit, 8)}
          pnlNote={<span style={{opacity: 1 - prog(f, hit, 8), color: C.loss, fontSize: 80, fontWeight: 900}}>▼</span>}
          shakeX={shake(f, hit + 24)}
        />
      </Box>
      <Box x={1240} y={170}>
        <div style={vis(f, a(10))}>
          <Chip size={44}>{F.crashDay.v}</Chip>
        </div>
      </Box>
      <Box x={1240} y={290}>
        <div style={vis(f, a(11))}>
          <NewsCard
            width={584}
            title={
              <>
                실적 전망 철회
                <br />
                CEO 사임
              </>
            }
          >
            <div style={{display: "flex", alignItems: "baseline", gap: 14, marginTop: 14, opacity: enter(f, a(12, 0.35))}}>
              <Label size={48}>약</Label>
              <Big size={150} color={C.loss}>
                {num(d)}%
              </Big>
            </div>
          </NewsCard>
        </div>
      </Box>
    </>
  );
};

// S06 자막 13–14 (네이비): 물타기 +3,000만 원 → 손실 ↑ / 물타기 버튼이 눌림
export const S06: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const until = a(14);
  return (
    <>
      <Box x={170} y={300}>
        <div style={vis(f, a(13), until)}>
          <Card style={{width: 720}}>
            <Label size={38} weight={500} color={C.gray}>
              평단 ↓ 하려고 넣은 돈
            </Label>
            <Big size={110} style={{marginTop: 10}}>
              {won(F.added.v, true)}
            </Big>
          </Card>
        </div>
      </Box>
      <Box x={920} y={392}>
        <div style={{opacity: fadeOut(f, until)}}>
          <Arrow dir="right" len={150} at={a(13, 0.55)} color={C.inkOnNavy} />
        </div>
      </Box>
      <Box x={1110} y={300}>
        <div style={vis(f, a(13, 0.6), until)}>
          <Card style={{width: 600}}>
            <Label size={38} weight={500} color={C.gray}>
              결과
            </Label>
            <Big size={110} color={C.loss} style={{marginTop: 10}}>
              손실 ↑
            </Big>
          </Card>
        </div>
      </Box>
      <Box x={760} y={300}>
        <div style={{opacity: enter(f, a(14))}}>
          <PushButton label="물타기" at={a(14)} pressAt={a(14, 0.32)} />
        </div>
      </Box>
    </>
  );
};
