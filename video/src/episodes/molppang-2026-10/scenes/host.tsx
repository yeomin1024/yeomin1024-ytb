// 진행자 파트 S06–S07 (문장 12–18)
import React from "react";
import {useCurrentFrame} from "remotion";
import {C, SERIF} from "../../../design/tokens";
import {enter} from "../../../components/anim";
import {won} from "../../../components/fmt";
import {Box, Chip, Headline, Hi, Label, fadeOut, vis} from "../../../components/ui";
import {Bubble} from "../../../components/cards";
import {F} from "../facts";
import {MiniAccount, MyAccount} from "../local";
import {SceneC} from "./story";

// S06 문장 12–15: 앞의 사연(S02의 계좌 카드, 작게) → 생각 말풍선 3개 (자막마다 하나씩)
export const S06: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  return (
    <>
      <Box x={100} y={190}>
        <div style={vis(f, a(12))}>
          <Chip variant="outline" size={36}>
            앞의 사연
          </Chip>
        </div>
      </Box>
      {/* 0.83배: 카드 안 가장 작은 글자(34px)도 28px 이상 */}
      <Box x={100} y={280}>
        <div style={{...vis(f, a(12, 0.1)), transformOrigin: "0 0"}}>
          <div style={{transform: "scale(0.83)", transformOrigin: "0 0"}}>
            <MyAccount pnl={F.loss.v} footL={`${F.company.v} ${won(F.all.v)}`} footR="현금 0원" />
          </div>
        </div>
      </Box>
      <Box x={950} y={170}>
        <Bubble at={a(13, 0.05)} size={44}>
          몰빵하면 많이 오르겠지?
        </Bubble>
      </Box>
      <Box x={950} y={380}>
        <Bubble at={a(14, 0.05)} size={44}>
          한 종목에 다 넣어야지!
        </Bubble>
      </Box>
      <Box x={950} y={590}>
        <Bubble at={a(15, 0.05)} size={44}>
          떨어져도 금방 다시 오르겠지
        </Bubble>
      </Box>
    </>
  );
};

// S07 문장 16–18: 좋다고 생각하는 종목 → (뒷줄) 전 재산 몰빵한 계좌 여럿 → (뒷줄) 큰 수익? → "몰빵의 문제" + 01~04
export const S07: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  const out = a(18);
  const n = 12;
  return (
    <>
      <div style={{position: "absolute", inset: 0, opacity: fadeOut(f, out)}}>
        <Box x={960} y={220} w={1600} center>
          <div style={{...vis(f, a(16, 0.1)), opacity: enter(f, a(16, 0.1)) * fadeOut(f, b(17))}}>
            <Chip variant="outline" size={44}>
              내가 좋다고 생각하는 종목
            </Chip>
          </div>
        </Box>
        <Box x={960} y={200} w={1600} center>
          <div style={vis(f, b(17))}>
            <Headline size={110}>
              <span style={{color: C.gain}}>큰 수익</span>?
            </Headline>
          </div>
        </Box>
        <Box x={960 - (n * 120 + (n - 1) * 24) / 2} y={420}>
          <div style={{display: "flex", gap: 24}}>
            {Array.from({length: n}).map((_, i) => (
              <MiniAccount key={i} at={b(16) + i * 3} w={120} />
            ))}
          </div>
        </Box>
        <Box x={960} y={540} w={1400} center>
          <div style={vis(f, b(16, 0.4))}>
            <Label size={52} weight={900}>
              전 재산 <Hi at={a(17, 0.2)}>몰빵</Hi>
            </Label>
          </div>
        </Box>
      </div>
      {/* 18: 문제 알아보기 — 번호 01~04 */}
      <Box x={960} y={260} w={1600} center>
        <div style={vis(f, out)}>
          <Headline size={96}>몰빵의 문제</Headline>
        </div>
      </Box>
      <Box x={960} y={480} w={1000} center>
        <div style={{display: "flex", justifyContent: "center", gap: 36}}>
          {["01", "02", "03", "04"].map((no, i) => (
            <div
              key={no}
              style={{
                ...vis(f, a(18, 0.3) + i * 5),
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
              {no}
            </div>
          ))}
        </div>
      </Box>
    </>
  );
};
