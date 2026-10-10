// 진행자 파트 S07–S10 (자막 15–23)
import React from "react";
import {useCurrentFrame} from "remotion";
import {C, SERIF} from "../../../design/tokens";
import {count, enter} from "../../../components/anim";
import {num} from "../../../components/fmt";
import {Arrow, Big, Box, Card, Chip, Headline, Hi, Label, vis} from "../../../components/ui";
import {Bubble} from "../../../components/cards";
import {Layer, Line} from "../../../components/charts";
import {F} from "../facts";
import {SceneC} from "./story";

// S07 문장 15–18: 계속 떨어지는 선 → 생각 말풍선 3개 (자막 하나에 하나)
export const S07: SceneC = ({t}) => {
  const {a} = t;
  return (
    <>
      <Layer>
        <Line
          pts={[
            [760, 170],
            [860, 215],
            [920, 200],
            [1040, 270],
            [1090, 255],
            [1180, 320],
          ]}
          at={a(15)}
          dur={24}
          color={C.loss}
        />
      </Layer>
      <Box x={130} y={440}>
        <Bubble at={a(16)} size={46}>
          평단만 낮추면 본전
        </Bubble>
      </Box>
      <Box x={720} y={500}>
        <Bubble at={a(17)} size={46}>
          큰 회사가 설마?
        </Bubble>
      </Box>
      <Box x={1270} y={440}>
        <Bubble at={a(18)} size={46} tail="right">
          팔면 손실 확정
        </Bubble>
      </Box>
    </>
  );
};

// S08 문장 19: 손실 인정 싫음 → 기준 없는 물타기
export const S08: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  return (
    <>
      <Box x={170} y={330}>
        <div style={vis(f, a(19))}>
          <Card style={{width: 600, textAlign: "center", padding: "48px 40px"}}>
            <Headline size={72}>손실 인정 싫음</Headline>
          </Card>
        </div>
      </Box>
      <Box x={840} y={400}>
        <Arrow dir="right" len={220} at={a(19, 0.5)} />
      </Box>
      <Box x={1130} y={330}>
        <div style={vis(f, a(19, 0.6))}>
          <Card style={{width: 640, textAlign: "center", padding: "48px 40px"}}>
            <Headline size={72}>
              <Hi at={a(19, 0.72)}>기준 없는</Hi> 물타기
            </Headline>
          </Card>
        </div>
      </Box>
    </>
  );
};

// S09 문장 20–22: 2025년 5월 서학개미 → (뒷줄) 이 종목 4,800억 원 넘게 순매수 → 그달 1위 → 형광펜
export const S09: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  const v = count(f, b(20, 0.3), 0, F.netBuy.v as number, 28);
  return (
    <>
      <Box x={960} y={170} w={1400} center>
        <div style={vis(f, a(20))}>
          <Chip size={44}>
            {F.netBuyMonth.v} · 서학개미<span style={{opacity: enter(f, b(20, 0.6))}}> 순매수</span>
          </Chip>
        </div>
      </Box>
      <Box x={960} y={290} w={1400} center>
        <div style={vis(f, b(20))}>
          <Label size={56}>{F.company.v}</Label>
        </div>
      </Box>
      <Box x={960} y={380} w={1600} center>
        <div style={{opacity: enter(f, b(20, 0.3)), display: "flex", justifyContent: "center", alignItems: "baseline", gap: 20}}>
          <Big size={200}>
            <Hi at={a(22, 0.1)}>{num(v)}억 원</Hi>
          </Big>
          <Label size={56}>넘게</Label>
        </div>
      </Box>
      <Box x={960} y={640} w={1200} center>
        <div style={vis(f, a(21, 0.55))}>
          <Chip variant="outline" size={52}>
            그달 순매수 {F.rank.v}위
          </Chip>
        </div>
      </Box>
    </>
  );
};

// S10 문장 23: "기준 없는 물타기, 왜 위험할까?" + 하나씩 볼 번호 4개
export const S10: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  return (
    <>
      <Box x={960} y={210} w={1600} center>
        <div style={vis(f, a(23))}>
          <Headline size={88}>기준 없는 물타기</Headline>
        </div>
        <div style={vis(f, a(23, 0.3))}>
          <Headline size={88}>왜 위험할까?</Headline>
        </div>
      </Box>
      <Box x={960} y={520} w={1000} center>
        <div style={{display: "flex", justifyContent: "center", gap: 36}}>
          {["01", "02", "03", "04"].map((n, i) => (
            <div
              key={n}
              style={{
                ...vis(f, a(23, 0.6) + i * 5),
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
