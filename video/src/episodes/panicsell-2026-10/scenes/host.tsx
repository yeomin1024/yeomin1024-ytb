// 진행자 파트 S07–S09 (문장 17–26)
import React from "react";
import {useCurrentFrame} from "remotion";
import {C, SERIF} from "../../../design/tokens";
import {count, enter, prog} from "../../../components/anim";
import {num} from "../../../components/fmt";
import {Big, Box, Chip, CornerNote, Headline, Hi, Label, fadeOut, vis} from "../../../components/ui";
import {Bubble} from "../../../components/cards";
import {Dot, Layer, Line, P, PtLabel} from "../../../components/charts";
import {F} from "../facts";
import {Gauge, MiniAccount} from "../local";
import {SceneC} from "./story";

/** 문장 19의 생각 말풍선 문구 (S15에서 같은 말풍선으로 다시 씀) */
export const THOUGHT_REBUY = "일단 팔고, 잠잠해지면 다시 사면 되지";

// S07 문장 17–21: 시장 전체가 무너지는 날(파랑 선 여러 개, 개념도) → 생각 말풍선 3개 → 개념도: 가격이 가장 낮을 때 가장 많이 판다
export const S07: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const out = a(21);
  const fall = (dy: number, k: number): P[] => [
    [700, 170 + dy],
    [820, 190 + dy + 10 * k],
    [900, 182 + dy + 22 * k],
    [1010, 222 + dy + 30 * k],
    [1080, 214 + dy + 40 * k],
    [1200, 262 + dy + 46 * k],
  ];
  // 21: 가격 선과 매도량 막대 (개념도)
  const price: P[] = [
    [260, 250],
    [420, 290],
    [580, 330],
    [740, 395],
    [900, 470],
    [1060, 430],
    [1220, 390],
    [1380, 350],
  ];
  const vol = [0.18, 0.28, 0.42, 0.62, 1, 0.5, 0.3, 0.2];
  const baseY = 770;
  const maxH = 180;
  return (
    <>
      <div style={{position: "absolute", inset: 0, opacity: fadeOut(f, out)}}>
        <Layer>
          <Line pts={fall(0, 1)} at={a(17, 0.2)} dur={22} color={C.loss} width={7} />
          <Line pts={fall(28, 0.8)} at={a(17, 0.26)} dur={22} color={C.loss} width={7} />
          <Line pts={fall(56, 1.2)} at={a(17, 0.32)} dur={22} color={C.loss} width={7} />
        </Layer>
        <Box x={1250} y={190}>
          <div style={vis(f, a(17, 0.3))}>
            <Chip size={40}>시장 전체 ↓</Chip>
          </div>
        </Box>
        <Box x={110} y={380}>
          <Bubble at={a(18)} size={46}>
            정말 0원 되는 거 아냐?
          </Bubble>
        </Box>
        <Box x={1240} y={380}>
          <Bubble at={a(20)} size={46} tail="right">
            뉴스마다 더 떨어진대
          </Bubble>
        </Box>
        <Box x={500} y={590}>
          <Bubble at={a(19)} size={44}>
            {THOUGHT_REBUY}
          </Bubble>
        </Box>
        <CornerNote at={a(17, 0.2)} y={130}>
          개념도
        </CornerNote>
      </div>
      {/* 21: 겁 > 판단 → 가격이 가장 낮을 때 가장 많이 판다 */}
      <div style={{position: "absolute", inset: 0, opacity: enter(f, out)}}>
        <Box x={140} y={150}>
          <div style={vis(f, out)}>
            <Chip size={44}>겁 &gt; 판단</Chip>
          </div>
        </Box>
        <Layer>
          <Line pts={price} at={out + 4} dur={26} color={C.ink} width={8} />
          <Dot p={price[4]} at={a(21, 0.45)} color={C.loss} />
        </Layer>
        <PtLabel p={price[4]} at={a(21, 0.45)} anchor="bottom" gap={26}>
          <Label size={40} color={C.loss}>
            가격 가장 낮을 때
          </Label>
        </PtLabel>
        <div style={{position: "absolute", left: 200, top: baseY, width: 1260, height: 6, background: C.ink, opacity: enter(f, out)}} />
        {vol.map((v, i) => {
          const h = maxH * v * prog(f, a(21, 0.5) + i * 2, 18);
          return (
            <div
              key={i}
              style={{position: "absolute", left: price[i][0] - 36, top: baseY - h, width: 72, height: h, background: i === 4 ? C.ink : "#B9B2A4", borderRadius: "8px 8px 0 0"}}
            />
          );
        })}
        <Box x={price[4][0] + 60} y={baseY - maxH - 2}>
          <div style={vis(f, a(21, 0.65))}>
            <Label size={44} weight={900}>
              ← <Hi at={a(21, 0.75)}>가장 많이 팖</Hi>
            </Label>
          </div>
        </Box>
        <Box x={1500} y={baseY - 52}>
          <div style={vis(f, a(21, 0.5))}>
            <Label size={34} weight={500} color={C.gray}>
              파는 양
            </Label>
          </div>
        </Box>
        <CornerNote at={out} y={130}>
          개념도
        </CornerNote>
      </div>
    </>
  );
};

// S08 문장 22–23: 3월 4일 VKOSPI 80 넘어 사상 최고 → 공포 게이지(개념도)
export const S08: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const v = count(f, a(22, 0.4), 0, F.vkospi.v, 26);
  return (
    <>
      <Box x={960} y={140} w={1400} center>
        <div style={{display: "flex", justifyContent: "center", alignItems: "center", gap: 22, ...vis(f, a(22))}}>
          <Chip size={40}>{F.crashDay.v}</Chip>
          <Label size={48}>변동성 지수 VKOSPI</Label>
        </div>
      </Box>
      <Gauge cx={960} cy={640} r={380} at={a(23)} p={0.96} />
      <Box x={960} y={360} w={900} center>
        <div style={{display: "flex", justifyContent: "center", alignItems: "baseline", gap: 18, opacity: enter(f, a(22, 0.4))}}>
          <Big size={210}>{num(v)}</Big>
          <Label size={52}>넘어</Label>
        </div>
      </Box>
      <Box x={960} y={668} w={900} center>
        <div style={vis(f, a(22, 0.65))}>
          <Label size={60} weight={900}>
            <Hi at={a(22, 0.75)}>사상 최고</Hi>
          </Label>
        </div>
      </Box>
      <Box x={1380} y={560}>
        <div style={vis(f, a(23, 0.45))}>
          <Label size={44}>시장의 공포를</Label>
          <Label size={44}>숫자로</Label>
        </div>
      </Box>
      <CornerNote at={a(23)}>개념도</CornerNote>
    </>
  );
};

// S09 문장 24–26: 코스피 하루 거래대금 58조 원 넘어 사상 최대 → 사연자 혼자가 아님(계좌 아이콘 여럿) → "하락장에서 전부 팔기, 왜 위험할까?" + 01~04
export const S09: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const out = a(26);
  const v = count(f, a(24, 0.35), 0, F.tradeValue.v, 26);
  return (
    <>
      <div style={{position: "absolute", inset: 0, opacity: fadeOut(f, out)}}>
        <Box x={960} y={170} w={1400} center>
          <div style={vis(f, a(24))}>
            <Label size={52}>코스피 하루 거래대금</Label>
          </div>
        </Box>
        <Box x={960} y={260} w={1400} center>
          <div style={{display: "flex", justifyContent: "center", alignItems: "baseline", gap: 18, opacity: enter(f, a(24, 0.35))}}>
            <Big size={200}>{num(v)}조 원</Big>
            <Label size={52}>넘게</Label>
          </div>
        </Box>
        <Box x={960} y={490} w={900} center>
          <div style={vis(f, a(24, 0.65))}>
            <Label size={60} weight={900}>
              <Hi at={a(24, 0.75)}>사상 최대</Hi>
            </Label>
          </div>
        </Box>
        <Box x={168} y={612}>
          <div style={{display: "flex", gap: 24}}>
            {Array.from({length: 12}).map((_, i) => (
              <div key={i} style={{display: "flex", flexDirection: "column", alignItems: "center", gap: 8}}>
                <MiniAccount at={i === 0 ? a(25, 0.05) : a(25, 0.3) + i * 3} dark={i === 0} w={110} />
                {i === 0 ? (
                  <div style={{opacity: enter(f, a(25, 0.05))}}>
                    <Label size={32}>사연자</Label>
                  </div>
                ) : null}
              </div>
            ))}
          </div>
        </Box>
      </div>
      <Box x={960} y={200} w={1600} center>
        <div style={vis(f, out)}>
          <Headline size={88}>하락장에서 전부 팔기,</Headline>
        </div>
        <div style={vis(f, a(26, 0.3))}>
          <Headline size={88}>왜 위험할까?</Headline>
        </div>
      </Box>
      <Box x={960} y={520} w={1000} center>
        <div style={{display: "flex", justifyContent: "center", gap: 36}}>
          {["01", "02", "03", "04"].map((n, i) => (
            <div
              key={n}
              style={{
                ...vis(f, a(26, 0.6) + i * 5),
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
