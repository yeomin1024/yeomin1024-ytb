// 진행자 파트 S09–S12 (문장 17–27)
import React from "react";
import {interpolate, useCurrentFrame} from "remotion";
import {C, SERIF} from "../../../design/tokens";
import {count, enter} from "../../../components/anim";
import {num} from "../../../components/fmt";
import {Big, Box, Chip, CornerNote, Headline, Hi, Label, fadeOut, vis} from "../../../components/ui";
import {Bubble} from "../../../components/cards";
import {Bars, Layer, Line, P} from "../../../components/charts";
import {Balance, Weight} from "../../../components/objects";
import {F} from "../facts";
import {SceneC} from "./story";

const CLAMP = {extrapolateLeft: "clamp", extrapolateRight: "clamp"} as const;

// S09 문장 17–20: 쭉쭉 오르는 선(개념도) → 생각 말풍선 3개 (자막 하나에 하나)
const RISE: P[] = [
  [300, 360],
  [470, 330],
  [580, 345],
  [760, 280],
  [880, 292],
  [1080, 220],
  [1200, 232],
  [1420, 160],
  [1620, 130],
];
export const S09: SceneC = ({t}) => {
  const {a} = t;
  return (
    <>
      <Layer>
        <Line pts={RISE} at={a(17)} dur={30} color={C.gain} />
      </Layer>
      <Box x={110} y={450}>
        <Bubble at={a(18)} size={46}>
          조금만 빌렸다가
          <br />
          바로 갚으면 되지
        </Bubble>
      </Box>
      <Box x={720} y={500}>
        <Bubble at={a(19)} size={46}>
          내 돈만 넣기엔
          <br />
          아까워
        </Bubble>
      </Box>
      <Box x={1290} y={450}>
        <Bubble at={a(20)} size={46} tail="right">
          설마
          <br />
          반대매매까지?
        </Bubble>
      </Box>
      <CornerNote at={a(17)} y={250}>
        개념도
      </CornerNote>
    </>
  );
};

// 조 단위 표기: 억 → "38조 6천억 원"
const joEok = (eok: number) => {
  const v = Math.round(eok / 1000) * 1000;
  const jo = Math.floor(v / 10000);
  const cheon = Math.round((v % 10000) / 1000);
  return `${jo ? `${jo}조 ` : ""}${cheon ? `${cheon}천억 ` : ""}원`.replace(/^원$/, "0원");
};

// S10 문장 21–23: 천칭 저울(오르는 장이 무겁고 빚은 가볍게) → 6월 24일 신용융자 잔고 38조 6천억 원, 사상 최대 → 개인 투자자가 빌려 산 주식
export const S10: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const out = a(22);
  const angle = interpolate(f, [a(21, 0.25), a(21, 0.55)], [0, -12], CLAMP);
  const v = count(f, a(22, 0.25), 0, 386000, 28);
  return (
    <>
      <div style={{position: "absolute", inset: 0, opacity: fadeOut(f, out)}}>
        <Balance
          cx={960}
          cy={360}
          angle={angle}
          at={a(21)}
          left={
            <Weight at={a(21, 0.1)} color="#C9C4BA" textColor={C.ink} w={260}>
              빚
            </Weight>
          }
          right={
            <Weight at={a(21, 0.2)} color={C.gain} textColor="#FFFFFF" w={340}>
              오르는 장
            </Weight>
          }
        />
      </div>
      <Box x={960} y={180} w={1600} center>
        <div style={vis(f, out)}>
          <Chip size={46}>
            {F.balanceDay.v} · 신용융자 잔고
          </Chip>
        </div>
      </Box>
      <Box x={960} y={300} w={1700} center>
        <div style={{opacity: enter(f, a(22, 0.25))}}>
          <Big size={190}>{joEok(v)}</Big>
        </div>
      </Box>
      <Box x={960} y={520} w={1200} center>
        <div style={vis(f, a(22, 0.6))}>
          <Label size={72} weight={900}>
            <Hi at={a(22, 0.72)}>사상 최대</Hi>
          </Label>
        </div>
      </Box>
      <Box x={960} y={660} w={1600} center>
        <div style={vis(f, a(23))}>
          <Label size={50}>= 개인 투자자가 증권사 돈을 빌려 산 주식</Label>
        </div>
      </Box>
    </>
  );
};

// S11 문장 24–26: 6월 한 달 · 증권사 10곳 신용 반대매매 / (뒷줄) 3,935억 원어치 + 6월 막대 → 1월 막대(1/7) 7배 가까이 → 빚투 ≠ 몇몇 사람만의 이야기
export const S11: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  const v = count(f, b(24) + 2, 0, F.creditSold.v, 26);
  const hJan = F.janBar.v / F.creditSold.v;
  return (
    <>
      <Box x={140} y={210}>
        <div style={vis(f, a(24), a(26))}>
          <Label size={44} weight={500} color={C.gray}>
            6월 한 달 · 증권사 {F.brokers.v}곳
          </Label>
          <Label size={52} style={{marginTop: 6}}>
            신용 반대매매로 팔린 주식
          </Label>
        </div>
      </Box>
      <Box x={140} y={370}>
        <div style={{display: "flex", alignItems: "baseline", gap: 18, ...vis(f, b(24))}}>
          <Big size={170}>{num(v)}억 원</Big>
          <Label size={52}>어치</Label>
        </div>
      </Box>
      <Box x={140} y={600}>
        <div style={vis(f, a(26, 0.1))}>
          <Headline size={60}>빚투 ≠ 몇몇 사람만의 이야기</Headline>
        </div>
      </Box>
      <div style={{position: "absolute", inset: 0, opacity: enter(f, b(24))}}>
      <Bars
        x={1180}
        baseY={710}
        maxH={430}
        barW={190}
        gap={170}
        items={[
          {h: hJan, color: C.gray, label: "1월", at: a(25)},
          {h: 1, color: C.ink, label: "6월", at: b(24)},
        ]}
      />
      </div>
      <Box x={1275} y={500} w={420} center>
        <div style={vis(f, a(25, 0.4))}>
          <Label size={52} weight={900}>
            <Hi at={a(25, 0.55)}>{F.x7.v}배 가까이</Hi>
          </Label>
        </div>
      </Box>
    </>
  );
};

// S12 문장 27: "빚투, 왜 위험할까?" + 하나씩 볼 번호 4개
export const S12: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  return (
    <>
      <Box x={960} y={230} w={1600} center>
        <div style={vis(f, a(27))}>
          <Headline size={88}>빚투, 왜 위험할까?</Headline>
        </div>
      </Box>
      <Box x={960} y={470} w={1000} center>
        <div style={{display: "flex", justifyContent: "center", gap: 36}}>
          {["01", "02", "03", "04"].map((n, i) => (
            <div
              key={n}
              style={{
                ...vis(f, a(27, 0.45) + i * 5),
                width: 150,
                height: 130,
                borderRadius: 18,
                background: C.ink,
                color: C.light,
                fontFamily: SERIF,
                fontWeight: 900,
                fontSize: 64,
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
              }}
            >
              {n}
            </div>
          ))}
        </div>
      </Box>
    </>
  );
};
