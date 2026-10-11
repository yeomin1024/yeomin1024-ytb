// 올바른 방법 파트 S20–S32 (문장 56–91), 밝은 크림 배경
import React from "react";
import {useCurrentFrame} from "remotion";
import {C, SERIF} from "../../../design/tokens";
import {count, enter, prog} from "../../../components/anim";
import {won} from "../../../components/fmt";
import {Big, Box, Card, Chip, CornerNote, Headline, Hi, Label, fadeOut, vis} from "../../../components/ui";
import {Bubble, NumberTitle} from "../../../components/cards";
import {Phone} from "../../../components/objects";
import {F} from "../facts";
import {BoxCell, BoxRow, CrossLabel, DateTag, DotGrid, HATCH, MyAccount, StrikeAt, WeightBar, boxRowW} from "../local";
import {T01, T02, T03, T04} from "./problems";
import {SceneC, THOUGHT_UP, Tail} from "./story";

const STATIC = -60;

// 번호 타이틀 문구 (S32 두 열 요약도 같은 이름)
export const M1 = "한 종목 비중의 상한 정하기";
export const M2 = "종목만 말고 업종도 나누기";
export const M3 = "어렵다면 지수 ETF를 기본으로";
export const M4 = "한 번에 다 사지 말고 현금 남기기";
export const M5 = "수익 나면 비중부터 확인";

// ── S20 문장 56–57: "한 번에 큰 수익"(취소선) vs 나눠 담기 → 다섯 가지 (첫째~다섯째) ──
const KO = ["첫째", "둘째", "셋째", "넷째", "다섯째"];
export const S20: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const out = a(57);
  return (
    <>
      <div style={{position: "absolute", inset: 0, opacity: fadeOut(f, out)}}>
        <Box x={200} y={320}>
          <div style={vis(f, a(56, 0.1))}>
            <Card style={{width: 700, height: 320, boxSizing: "border-box", display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", gap: 14}}>
              <Label size={40} weight={500} color={C.gray}>
                욕심
              </Label>
              <Headline size={68} color={C.gray}>
                <StrikeAt at={a(56, 0.45)} color={C.ink}>
                  한 번에 큰 수익
                </StrikeAt>
              </Headline>
            </Card>
          </div>
        </Box>
        <Box x={1020} y={320}>
          <div style={vis(f, a(56, 0.6))}>
            <Card style={{width: 700, height: 320, boxSizing: "border-box", display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", gap: 30}}>
              <Headline size={76}>
                <Hi at={a(56, 0.75)}>나눠 담기</Hi>
              </Headline>
              <div style={{display: "flex", gap: 10}}>
                {Array.from({length: 6}).map((_, i) => (
                  <div key={i} style={{width: 80, height: 56, borderRadius: 10, background: C.ink, opacity: enter(f, a(56, 0.65) + i * 3)}} />
                ))}
              </div>
            </Card>
          </div>
        </Box>
      </div>
      <Box x={960} y={300} w={1200} center>
        <div style={vis(f, out)}>
          <Headline size={80}>{F.five.v}가지</Headline>
        </div>
      </Box>
      <Box x={960} y={450} w={1600} center>
        <div style={{display: "flex", justifyContent: "center", gap: 30}}>
          {KO.map((k, i) => (
            <div
              key={k}
              style={{
                ...vis(f, a(57, 0.3) + i * 5),
                width: 250,
                height: 130,
                borderRadius: 18,
                background: C.ink,
                color: C.light,
                fontFamily: SERIF,
                fontWeight: 900,
                fontSize: 56,
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
              }}
            >
              {k}
            </div>
          ))}
        </div>
      </Box>
    </>
  );
};

// ── S21 문장 58–59: "첫째" → 예시 계좌 7,000만 원(S02의 계좌 카드, 간단형) + 상한 15% 선 → (뒷줄) 한 종목 1,050만 원까지 ──
const S21X = 480;
const S21Y = 300;
const capX = S21X + 48 + 4 + F.cap.v / 100 * (864 - 8);
export const S21: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  const fill = (F.cap.v / 100) * prog(f, b(59, 0.1), 16);
  const barTop = S21Y + 34 + 56 + 26;
  return (
    <>
      <NumberTitle
        no="첫째"
        at={a(58)}
        title={
          <>
            한 종목 비중의 <Hi at={a(58, 0.6)} until={b(59, 0.4)}>상한</Hi> 정하기
          </>
        }
      />
      <Box x={S21X} y={S21Y}>
        <div style={vis(f, a(59))}>
          <MyAccount
            compact
            pnl={null}
            stock={fill}
            head={
              <div style={{display: "flex", alignItems: "center", gap: 16}}>
                <Chip variant="outline" size={32}>
                  예시
                </Chip>
                <Label size={40} weight={500} color={C.gray}>
                  {won(F.all.v)}
                </Label>
              </div>
            }
            footL={<span style={{opacity: enter(f, b(59))}}>한 종목</span>}
          />
        </div>
      </Box>
      <div style={{position: "absolute", left: capX - 3, top: barTop - 8, height: 56 + 16, borderLeft: `6px dashed ${C.ink}`, opacity: enter(f, a(59, 0.15))}} />
      {/* 카드 아래 (카드 바닥 = barTop + 56 + 12 + 48 + 38 + 4) */}
      <Box x={capX} y={barTop + 56 + 116} w={400} center>
        <div style={vis(f, a(59, 0.15))}>
          <Label size={44} weight={900}>
            ↑ 상한 {F.cap.v}%
          </Label>
        </div>
      </Box>
      <Box x={960} y={676} w={1400} center>
        <div style={{display: "flex", justifyContent: "center", alignItems: "baseline", gap: 22, ...vis(f, b(59, 0.3))}}>
          <Label size={52}>최대</Label>
          <Big size={130}>
            <Hi at={b(59, 0.5)}>{won(F.capAmt.v)}</Hi>
          </Big>
          <Label size={52}>까지</Label>
        </div>
      </Box>
    </>
  );
};

// ── S22 문장 60–61: 7,000만 원 → 10개 종목 × 700만 원 (칸 10개) → 같은 폭락: 한 칸만 2/7 잃음 → 몰빵 -2,000만 원 vs 나눴다면 약 -200만 원, 계좌의 3% 정도 ──
const BRX = 960 - boxRowW(10) / 2;
const BRY = 340;
const cells700 = (fill0: number, rest = 1, label = true): BoxCell[] =>
  Array.from({length: 10}).map((_, i) => ({fill: i === 0 ? fill0 : rest, label: label ? <Label size={32}>700만</Label> : undefined}));
export const S22: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const hit = a(61, 0.15);
  const fill0 = 1 - (-F.loss.v / F.all.v) * prog(f, hit, 16);
  const vL = count(f, a(61, 0.3), 0, F.loss.v);
  const vR = count(f, a(61, 0.3), 0, F.splitLoss.v);
  return (
    <>
      <NumberTitle no="첫째" at={STATIC} title={M1} />
      <Box x={960} y={262} w={1400} center>
        <div style={{...vis(f, a(60)), opacity: enter(f, a(60)) * fadeOut(f, a(61))}}>
          <Label size={44}>
            {won(F.all.v)} → {F.n10.v}개 종목에 {won(F.each.v)}씩
          </Label>
        </div>
      </Box>
      <BoxRow x={BRX} y={BRY} cells={cells700(fill0)} at={a(60, 0.3)} />
      <Box x={BRX} y={268}>
        <div style={vis(f, hit)}>
          <div style={{display: "inline-block", background: C.loss, color: "#FFFFFF", fontWeight: 700, fontSize: 36, padding: "6px 22px", borderRadius: 10, whiteSpace: "nowrap"}}>같은 폭락</div>
        </div>
      </Box>
      {/* 화면 분할: 왼쪽 몰빵 / 오른쪽 나눴다면 */}
      <div style={{position: "absolute", left: 958, top: 570, width: 4, height: 210, background: C.gray, opacity: enter(f, a(61, 0.3))}} />
      <Box x={200} y={570}>
        <div style={vis(f, a(61, 0.3))}>
          <Chip variant="outline" size={40}>
            몰빵
          </Chip>
          <Big size={120} color={C.loss} style={{marginTop: 20}}>
            {won(vL)}
          </Big>
        </div>
      </Box>
      <Box x={1010} y={570}>
        <div style={vis(f, a(61, 0.3))}>
          <Chip size={40}>{F.n10.v}개로 나눴다면</Chip>
          <div style={{display: "flex", alignItems: "flex-end", gap: 24, marginTop: 20}}>
            <Big size={120} color={C.loss}>
              약 {won(vR)}
            </Big>
            <div style={vis(f, a(61, 0.6))}>
              <Label size={38}>계좌의</Label>
              <Label size={44} weight={900}>
                <Hi at={a(61, 0.7)}>{F.splitPct.v}% 정도</Hi>
              </Label>
            </div>
          </div>
        </div>
      </Box>
    </>
  );
};

// ── S23 문장 62–63: S22의 칸 10개 — 시장 전체 ↓ (모든 칸이 조금씩) → 한 회사 악재는 한 칸만, 계좌 전체가 무너지는 일은 막음 (개념도) ──
export const S23: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const mk = prog(f, a(62, 0.3), 18) * (1 - prog(f, a(63), 12));
  const one = prog(f, a(63, 0.2), 16);
  const cells: BoxCell[] = Array.from({length: 10}).map((_, i) => ({fill: i === 0 ? 1 - 0.18 * mk - 0.7 * one : 1 - 0.18 * mk, label: <Label size={32}>700만</Label>}));
  return (
    <>
      <NumberTitle no="첫째" at={STATIC} title={M1} />
      <BoxRow x={BRX} y={BRY} cells={cells} at={STATIC} />
      <Box x={960} y={262} w={800} center>
        <div style={{...vis(f, a(62, 0.1)), opacity: enter(f, a(62, 0.1)) * fadeOut(f, a(63))}}>
          <Chip variant="outline" size={40}>
            시장 전체 ↓
          </Chip>
        </div>
      </Box>
      <Box x={BRX} y={268}>
        <div style={vis(f, a(63, 0.1))}>
          <div style={{display: "inline-block", background: C.loss, color: "#FFFFFF", fontWeight: 700, fontSize: 36, padding: "6px 22px", borderRadius: 10, whiteSpace: "nowrap"}}>한 회사 악재</div>
        </div>
      </Box>
      <Box x={960} y={590} w={1400} center>
        <div style={vis(f, a(63, 0.4))}>
          <Label size={48}>계좌 전체가 무너지는 일</Label>
          <Headline size={76} style={{marginTop: 8}}>
            <Hi at={a(63, 0.65)}>막을 수 있음</Hi>
          </Headline>
        </div>
      </Box>
      <CornerNote at={a(62)} y={780}>
        개념도
      </CornerNote>
    </>
  );
};

// ── S24 문장 64–67: "둘째" → AI 반도체 · AI 소프트웨어 · AI 전력주 = 사실상 한 종목 → 딥시크 등장한 날 엔비디아·브로드컴 -17% → 비스트라 -28% ──
const ZY = 520; // 0선
const KS = 7; // 하락률 1%당 px
const COLC = [420, 960, 1500];
const DropBar: React.FC<{cx: number; name: string; pct: number; at: number}> = ({cx, name, pct, at}) => {
  const f = useCurrentFrame();
  const h = Math.abs(pct) * KS * prog(f, at, 16);
  const w = 110;
  return (
    <>
      <div style={{position: "absolute", left: cx - 120, width: 240, top: ZY - 54, textAlign: "center", opacity: enter(f, at)}}>
        <Label size={36}>{name}</Label>
      </div>
      <div style={{position: "absolute", left: cx - w / 2, top: ZY + 3, width: w, height: h, background: C.loss, borderRadius: "0 0 10px 10px"}} />
      <div style={{position: "absolute", left: cx - 120, width: 240, top: ZY + Math.abs(pct) * KS + 12, textAlign: "center", opacity: enter(f, at + 10)}}>
        <Label size={50} weight={900} color={C.loss}>
          {pct}%
        </Label>
      </div>
    </>
  );
};
export const S24: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  const bp = prog(f, a(65, 0.6), 14);
  const day = a(66);
  const chips = [F.aiChip.v, F.aiSoft.v, F.aiPower.v];
  return (
    <>
      <NumberTitle
        no="둘째"
        at={a(64)}
        title={
          <>
            종목만 말고 <Hi at={a(64, 0.55)} until={a(65, 0.7)}>업종도</Hi> 나누기
          </>
        }
      />
      {chips.map((c, i) => (
        <Box key={c} x={COLC[i]} y={270} w={500} center>
          <div style={vis(f, a(65, 0.03 + i * 0.14))}>
            <Chip variant="outline" size={44}>
              {c}
            </Chip>
          </div>
        </Box>
      ))}
      {/* 사실상 한 종목 (괄호) */}
      <div style={{position: "absolute", inset: 0, opacity: fadeOut(f, day)}}>
        <div style={{position: "absolute", left: 230, top: 352, width: 1460 * bp, height: 24, borderLeft: `6px solid ${C.ink}`, borderBottom: `6px solid ${C.ink}`, borderRight: bp > 0.95 ? `6px solid ${C.ink}` : undefined, borderRadius: "0 0 8px 8px", opacity: enter(f, a(65, 0.6))}} />
        <Box x={960} y={400} w={1000} center>
          <div style={vis(f, a(65, 0.7))}>
            <Headline size={72}>
              = <Hi at={a(65, 0.8)}>사실상 한 종목</Hi>
            </Headline>
          </div>
        </Box>
      </div>
      {/* 66–67: 딥시크가 등장한 날 */}
      <Box x={200} y={372}>
        <div style={vis(f, day)}>
          <DateTag style={{fontSize: 40, display: "inline-block"}}>딥시크 등장한 날</DateTag>
        </div>
      </Box>
      <div style={{position: "absolute", left: 200, top: ZY - 3, width: 1520, height: 6, background: C.ink, opacity: enter(f, a(66, 0.3))}} />
      <DropBar cx={COLC[0] - 110} name={F.nvidia.v} pct={F.nvidiaDrop.v} at={a(66, 0.45)} />
      <DropBar cx={COLC[0] + 110} name={F.broadcom.v} pct={F.nvidiaDrop.v} at={a(66, 0.55)} />
      <DropBar cx={COLC[2]} name={F.vistra.v} pct={F.vistraDrop.v} at={a(67, 0.55)} />
    </>
  );
};

// ── S25 문장 68–69: 반도체 · 헬스케어 · 소비재 · 금융 → (뒷줄) 서로 다른 업종 → 악재는 한 업종에만, 함께 무너질 가능성 줄어듦 ──
const SECT = ["반도체", "헬스케어", "소비재", "금융"];
const TW = 380;
const TX0 = 960 - (4 * TW + 3 * 30) / 2;
export const S25: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  const hit = prog(f, a(69, 0.1), 10);
  return (
    <>
      <NumberTitle no="둘째" at={STATIC} title={M2} />
      {SECT.map((s, i) => (
        <Box key={s} x={TX0 + i * (TW + 30)} y={330}>
          <div style={vis(f, a(68, 0.1 + i * 0.12))}>
            <Card style={{width: TW, height: 200, boxSizing: "border-box", display: "flex", alignItems: "center", justifyContent: "center", borderColor: i === 0 && hit > 0.5 ? C.loss : C.ink}}>
              <Label size={58} weight={900} color={i === 0 && hit > 0.5 ? C.loss : C.ink}>
                {s}
                {i === 0 && hit > 0 ? <span style={{opacity: hit}}> ↓</span> : null}
              </Label>
            </Card>
          </div>
        </Box>
      ))}
      <Box x={TX0 + TW / 2} y={266} w={300} center>
        <div style={vis(f, a(69, 0.05))}>
          <div style={{display: "inline-block", background: C.loss, color: "#FFFFFF", fontWeight: 700, fontSize: 34, padding: "4px 22px", borderRadius: 10}}>악재</div>
        </div>
      </Box>
      <Box x={960} y={600} w={1400} center>
        <div style={{...vis(f, b(68)), opacity: enter(f, b(68)) * fadeOut(f, a(69, 0.3))}}>
          <Headline size={76}>
            <Hi at={b(68, 0.3)} until={a(69, 0.3)}>
              서로 다른 업종
            </Hi>
          </Headline>
        </div>
      </Box>
      <Box x={960} y={600} w={1400} center>
        <div style={vis(f, a(69, 0.4))}>
          <Headline size={72}>
            함께 무너질 가능성 <Hi at={a(69, 0.65)}>줄어듦</Hi>
          </Headline>
        </div>
      </Box>
    </>
  );
};

// ── S26 문장 70–72: "셋째" → S&P 500 ETF 하나 → (뒷줄) 미국 대표 기업 500곳 (점 500개) → 시장을 이끄는 대형 승자 기업도 함께 ──
const HOT = [3, 31, 58, 77, 112, 146, 190, 233, 268, 301, 347, 390, 421, 466];
export const S26: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  return (
    <>
      <NumberTitle
        no="셋째"
        at={a(70)}
        title={
          <>
            어렵다면 <Hi at={a(70, 0.6)} until={b(71, 0.5)}>지수 ETF를</Hi> 기본으로
          </>
        }
      />
      <Box x={200} y={270}>
        <div style={vis(f, a(71))}>
          <Card style={{width: 640, height: 520, boxSizing: "border-box", padding: "22px 30px", position: "relative"}}>
            <div style={{display: "flex", justifyContent: "space-between", alignItems: "center"}}>
              <Label size={46} weight={900}>
                {F.sp500.v} ETF
              </Label>
              <Chip variant="outline" size={32}>
                하나
              </Chip>
            </div>
          </Card>
        </div>
      </Box>
      <DotGrid x={200 + (640 - (25 * 12 + 24 * 7)) / 2} y={380} cols={25} rows={20} d={12} gap={7} at={b(71, 0.05)} dur={30} hot={HOT} hotAt={a(72, 0.25)} />
      <Box x={930} y={300}>
        <div style={vis(f, b(71, 0.1))}>
          <Label size={48}>미국 대표 기업</Label>
          <Big size={180} style={{marginTop: 6}}>
            {F.n500.v}곳
          </Big>
        </div>
      </Box>
      <Box x={930} y={560}>
        <div style={{display: "flex", alignItems: "center", gap: 18, ...vis(f, a(72, 0.2))}}>
          <div style={{width: 26, height: 26, borderRadius: 99, background: C.gain, flex: "none"}} />
          <Label size={42}>시장을 이끄는 대형 승자 기업</Label>
        </div>
        <div style={{marginTop: 22, ...vis(f, a(72, 0.5))}}>
          <Label size={52} weight={900}>
            직접 안 골라도 <Hi at={a(72, 0.7)}>함께 담김</Hi>
          </Label>
        </div>
      </Box>
    </>
  );
};

// ── S27 문장 73–74: 워런 버핏 · 아내에게 남길 돈 90% → (뒷줄) S&P 500 지수 펀드 → 예시: 절반 지수 ETF + 나머지 개별 종목 ──
const BX = 200;
const BW = 1520;
export const S27: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  const p = prog(f, a(73, 0.2), 18);
  const p2 = prog(f, a(74, 0.25), 16);
  const indivX = BX + BW / 2;
  return (
    <>
      <NumberTitle no="셋째" at={STATIC} title={M3} />
      <Box x={BX} y={262}>
        <div style={{display: "flex", alignItems: "baseline", gap: 26, ...vis(f, a(73))}}>
          <Label size={56} weight={900}>
            {F.buffett.v}
          </Label>
          <Label size={40} weight={500} color={C.gray}>
            아내에게 남길 돈
          </Label>
        </div>
      </Box>
      <WeightBar x={BX} y={350} w={BW} h={100} segs={[{v: F.buffett90.v * p}, {v: 100 - F.buffett90.v * p, color: C.light}]} opacity={enter(f, a(73, 0.12))} />
      <Box x={BX + (BW * F.buffett90.v) / 200} y={358} w={400} center>
        <div style={{opacity: enter(f, a(73, 0.36))}}>
          <Big size={84} color="#FFFFFF">
            {F.buffett90.v}%
          </Big>
        </div>
      </Box>
      <Box x={BX + (BW * F.buffett90.v) / 200} y={462} w={800} center>
        <div style={vis(f, b(73, 0.15))}>
          <Label size={46} weight={900}>
            {F.sp500.v} 지수 펀드
          </Label>
        </div>
      </Box>
      {/* 74: 예시 — 절반 지수 ETF, 나머지 개별 종목 */}
      <Box x={BX} y={545}>
        <div style={vis(f, a(74))}>
          <Chip variant="outline" size={34}>
            예시
          </Chip>
        </div>
      </Box>
      <WeightBar
        x={BX}
        y={610}
        w={BW}
        h={100}
        segs={[{v: 50}, ...Array.from({length: 5}).map(() => ({v: 10 * p2, color: C.gray})), {v: 50 * (1 - p2), color: C.light}]}
        opacity={enter(f, a(74, 0.1))}
      />
      <Box x={BX + BW / 4} y={628} w={600} center>
        <div style={{opacity: enter(f, a(74, 0.15))}}>
          <Label size={46} weight={900} color="#FFFFFF">
            {F.halfEtf.v} 지수 ETF
          </Label>
        </div>
      </Box>
      <Box x={indivX + BW / 4} y={722} w={700} center>
        <div style={vis(f, a(74, 0.55))}>
          <Label size={44} weight={900}>
            나머지 개별 종목
          </Label>
        </div>
      </Box>
    </>
  );
};

// ── S28 문장 75–77: "넷째" → 한 종목 700만 원을 세 번에 나눠 → 첫 매수 직후 악재 → (뒷줄) 남은 돈으로 더 싸게 살지·기다릴지 고를 수 있음 ──
const QX = [200, 715, 1230];
const QW = 490;
const QY = 370;
export const S28: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  const buy1 = prog(f, a(77, 0.05), 12);
  return (
    <>
      <NumberTitle
        no="넷째"
        at={a(75)}
        title={
          <>
            한 번에 다 사지 말고 <Hi at={a(75, 0.6)} until={a(76)}>현금</Hi> 남기기
          </>
        }
      />
      <Box x={200} y={276}>
        <div style={{display: "flex", alignItems: "center", gap: 30, ...vis(f, a(76))}}>
          <Label size={48} weight={900}>
            한 종목 {won(F.each.v)}
          </Label>
          <div style={{...vis(f, a(76, 0.6)), opacity: enter(f, a(76, 0.6)) * fadeOut(f, b(77))}}>
            <Chip size={38}>세 번에 나눠</Chip>
          </div>
        </div>
      </Box>
      {QX.map((x, i) => (
        <React.Fragment key={x}>
          <div style={{position: "absolute", left: x, top: QY, width: QW, height: 140, boxSizing: "border-box", border: `4px solid ${C.ink}`, borderRadius: 14, overflow: "hidden", background: HATCH, opacity: enter(f, a(76, 0.55) + i * 4)}}>
            {i === 0 ? <div style={{position: "absolute", left: 0, top: 0, bottom: 0, width: `${buy1 * 100}%`, background: C.ink}} /> : null}
          </div>
          <Box x={x + QW / 2} y={QY + 152} w={QW} center>
            <div style={{opacity: enter(f, a(76, 0.6) + i * 4)}}>
              <Label size={40}>{i + 1}번</Label>
            </div>
          </Box>
        </React.Fragment>
      ))}
      <Box x={QX[0] + QW / 2} y={QY + 38} w={QW} center>
        <div style={vis(f, a(77, 0.25))}>
          <div style={{display: "inline-block", background: C.loss, color: "#FFFFFF", fontWeight: 700, fontSize: 40, padding: "6px 26px", borderRadius: 12}}>악재 ↓</div>
        </div>
      </Box>
      {/* (뒷줄) 2·3번 칸 = 남은 돈 (위 괄호) */}
      <div style={{position: "absolute", left: QX[1], top: QY - 30, width: QX[2] + QW - QX[1], height: 18, borderTop: `6px solid ${C.ink}`, borderLeft: `6px solid ${C.ink}`, borderRight: `6px solid ${C.ink}`, borderRadius: "8px 8px 0 0", opacity: enter(f, b(77))}} />
      <Box x={QX[1] + QW + 7} y={QY - 104} w={900} center>
        <div style={vis(f, b(77))}>
          <Label size={52} weight={900}>
            남은 돈
          </Label>
        </div>
      </Box>
      <Box x={QX[1] + QW + 7} y={600} w={1100} center>
        <div style={{display: "flex", justifyContent: "center", gap: 40, ...vis(f, b(77, 0.15))}}>
          <Chip variant="outline" size={44}>
            더 싸게 살지
          </Chip>
          <Chip variant="outline" size={44}>
            기다릴지
          </Chip>
        </div>
      </Box>
      <Box x={QX[1] + QW + 7} y={696} w={1100} center>
        <div style={vis(f, b(77, 0.45))}>
          <Label size={56} weight={900}>
            <Hi at={b(77, 0.6)}>고를 수 있음</Hi>
          </Label>
        </div>
      </Box>
    </>
  );
};

// ── S29 문장 78–79: 사연 계좌 카드(S02와 같음) 현금 0원 · ✗ 물타기 할 돈(S05와 같음) → 현금: 노는 돈(취소선) → 위기 때 꺼내 쓰는 선택지 ──
export const S29: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  return (
    <>
      <NumberTitle no="넷째" at={STATIC} title={M4} />
      <Box x={120} y={262}>
        <div style={vis(f, a(78))}>
          <MyAccount
            pnl={F.loss.v}
            footL={`${F.company.v} ${won(F.all.v)}`}
            footR={
              <span style={{color: C.ink, fontWeight: 900}}>
                <Hi at={a(78, 0.55)} until={a(79)}>
                  현금 0원
                </Hi>
              </span>
            }
          />
        </div>
      </Box>
      <Box x={1150} y={290}>
        <CrossLabel at={a(78, 0.35)} size={52}>
          물타기 할 돈
        </CrossLabel>
      </Box>
      <Box x={1150} y={440}>
        <div style={{display: "flex", alignItems: "center", gap: 22, ...vis(f, a(79))}}>
          <Chip size={44}>현금</Chip>
          <Label size={52} weight={900} color={C.gray}>
            <StrikeAt at={a(79, 0.3)} color={C.ink}>
              노는 돈
            </StrikeAt>
          </Label>
        </div>
        <div style={{marginTop: 34, ...vis(f, a(79, 0.5))}}>
          <Label size={44}>위기 때 꺼내 쓰는</Label>
          <Headline size={84} style={{marginTop: 6}}>
            <Hi at={a(79, 0.75)}>선택지</Hi>
          </Headline>
        </div>
      </Box>
    </>
  );
};

// ── S30 문장 80–81: "다섯째" → 사연 계좌 카드 +1,000만 원 정도(S03과 같음) + S03의 말풍선 "더 오를 것 같아" → 그대로 두기 · 더 사기 ──
export const S30: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a} = t;
  return (
    <>
      <NumberTitle
        no="다섯째"
        at={a(80)}
        title={
          <>
            수익 나면 <Hi at={a(80, 0.6)} until={a(81)}>비중부터</Hi> 확인
          </>
        }
      />
      <Box x={120} y={262}>
        <div style={vis(f, a(81))}>
          <MyAccount pnl={F.gain.v} pnlNote={<Tail>정도</Tail>} footL={`${F.company.v} ${won(F.all.v)}`} footR="현금 0원" />
        </div>
      </Box>
      <Box x={1170} y={300}>
        <Bubble at={a(81, 0.25)} size={50}>
          {THOUGHT_UP}
        </Bubble>
      </Box>
      <Box x={1170} y={560}>
        <div style={{display: "flex", gap: 26}}>
          <div style={vis(f, a(81, 0.5))}>
            <Chip variant="outline" size={44}>
              그대로 두기
            </Chip>
          </div>
          <div style={vis(f, a(81, 0.7))}>
            <Chip variant="outline" size={44}>
              더 사기
            </Chip>
          </div>
        </div>
      </Box>
    </>
  );
};

// ── S31 문장 82–85: 계좌 비중 막대(10칸) — 700만 원 종목이 두 배(빨강) → (뒷줄) 10% → 18% 정도 → 그대로 두면 몰빵에 가까워짐 → 상한 15% 넘은 만큼만 팔아 다른 종목에 → 악재가 터져도 대처할 여유 ──
const WX = 200;
const WW = 1520;
const WY = 340;
const WH = 110;
export const S31: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  const dbl = prog(f, a(82, 0.22), 16);
  const trim = prog(f, a(84, 0.4), 18);
  const capV = (F.cap.v / 100) * (F.all.v - F.each.v + 2 * F.each.v); // 상한 15%까지만 (비율 계산용, 숫자 표시 안 함)
  const v0 = F.each.v + F.each.v * dbl - (2 * F.each.v - capV) * trim;
  const vo = F.each.v + ((2 * F.each.v - capV) / 9) * trim;
  const p83 = a(83);
  const p84 = a(84);
  const p85 = a(85);
  const ext = prog(f, a(83, 0.2), 24) * (1 - prog(f, p84, 10));
  const segs = [{v: v0, color: dbl > 0.05 ? C.gain : C.ink}, ...Array.from({length: 9}).map((_, i) => ({v: vo, color: i === 3 && f >= a(85, 0.2) ? C.loss : C.ink}))];
  const total = v0 + 9 * vo;
  const end0 = WX + 4 + (v0 / total) * (WW - 8);
  const capX = WX + 4 + (F.cap.v / 100) * (WW - 8);
  return (
    <>
      <NumberTitle no="다섯째" at={STATIC} title={M5} />
      <Box x={WX + WW} y={272}>
        <div style={{transform: "translateX(-100%)", whiteSpace: "nowrap"}}>
          <div style={vis(f, a(82))}>
            <Label size={40} color={C.gray}>
              내 계좌 비중
            </Label>
          </div>
        </div>
      </Box>
      <WeightBar x={WX} y={WY} w={WW} h={WH} segs={segs} opacity={enter(f, a(82))} />
      <Box x={WX} y={WY + 18}>
        <div style={{opacity: enter(f, a(82, 0.05)) * fadeOut(f, a(82, 0.2))}}>
          <Label size={36} color="#FFFFFF" style={{paddingLeft: 18}}>
            {won(F.each.v).replace(" 원", "")}
          </Label>
        </div>
      </Box>
      <Box x={(WX + end0) / 2} y={264} w={300} center>
        <div style={{...vis(f, a(82, 0.3)), opacity: enter(f, a(82, 0.3)) * fadeOut(f, p84)}}>
          <Label size={56} weight={900} color={C.gain}>
            ×2
          </Label>
        </div>
      </Box>
      {/* 82 (뒷줄): 10% → 18% 정도 */}
      <Box x={WX} y={500}>
        <div style={{...vis(f, b(82, 0.15)), opacity: enter(f, b(82, 0.15)) * fadeOut(f, p84)}}>
          <div style={{display: "flex", alignItems: "baseline", gap: 26}}>
            <Big size={110} color={C.gray}>
              {F.w10.v}%
            </Big>
            <Label size={70} weight={900}>
              →
            </Label>
            <Big size={130}>
              <Hi at={b(82, 0.45)} until={p83}>
                {F.w18.v}% 정도
              </Hi>
            </Big>
          </div>
        </div>
      </Box>
      {/* 83: 그대로 두면 몰빵에 가까워짐 (개념도) */}
      <div style={{position: "absolute", left: end0, top: WY - 12, width: Math.max(0, (WX + WW * 0.7 - end0) * ext), height: WH + 24, boxSizing: "border-box", border: `5px dashed ${C.gray}`, borderLeft: "none", borderRadius: "0 14px 14px 0", opacity: ext > 0 ? 1 : 0}} />
      <Box x={1100} y={680}>
        <div style={{...vis(f, a(83, 0.3)), opacity: enter(f, a(83, 0.3)) * fadeOut(f, p84)}}>
          <Label size={52} weight={900}>
            → <Hi at={a(83, 0.55)} until={p84}>몰빵에 가까워짐</Hi>
          </Label>
        </div>
      </Box>
      <CornerNote at={p83} until={p84} y={780}>
        개념도
      </CornerNote>
      {/* 84: 상한 15% 선 → 넘은 만큼만 팔아 다른 종목에 */}
      <div style={{position: "absolute", left: capX - 3, top: WY - 30, height: WH + 60, borderLeft: `6px dashed ${C.ink}`, opacity: enter(f, p84)}} />
      <Box x={capX} y={WY + WH + 40} w={400} center>
        <div style={vis(f, p84)}>
          <Label size={44} weight={900}>
            상한 {F.cap.v}%
          </Label>
        </div>
      </Box>
      <Box x={960} y={600} w={1500} center>
        <div style={{...vis(f, a(84, 0.45)), opacity: enter(f, a(84, 0.45)) * fadeOut(f, p85)}}>
          <Label size={56} weight={900}>
            <Hi at={a(84, 0.6)} until={p85}>
              넘은 만큼만
            </Hi>{" "}
            팔아 → 다른 종목에
          </Label>
        </div>
      </Box>
      {/* 85: 한 종목에 악재가 터져도 대처할 여유 */}
      <Box x={960} y={600} w={1500} center>
        <div style={vis(f, a(85, 0.2))}>
          <Label size={56} weight={900}>
            <span style={{color: C.loss}}>한 종목 악재</span>에도 → <Hi at={a(85, 0.5)}>대처할 여유</Hi>
          </Label>
        </div>
      </Box>
    </>
  );
};

// ── S32 문장 86–91: 두 열 요약 (몰빵의 위험 4 / (뒷줄) 나눠 담는 법 5) → 늦지 않았다 → 휴대폰: 가장 비중이 큰 종목 몇 %? → 큰 수익(취소선) · 대처 가능하게 → 성공 투자 ──
const RISKS = [T01.replace("몰빵 종목이 ", ""), T02, T03.replace("큰 수익을 낼 확률 자체가", "큰 수익 낼 확률이"), T04.replace("몰빵은 ", "")];
const RULES = [M1, M2.replace("종목만 말고 ", ""), M3.replace("어렵다면 ", ""), "현금 남기고 나눠 사기", M5];
export const S32: SceneC = ({t}) => {
  const f = useCurrentFrame();
  const {a, b} = t;
  const p87 = a(87);
  const p88 = a(88);
  const p89 = a(89);
  const p90 = a(90);
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
      <div style={{position: "absolute", inset: 0, opacity: fadeOut(f, p87)}}>
        {col("몰빵의 위험", RISKS, 120, a(86, 0.05), (i) => `0${i + 1}`)}
        {col("나눠 담는 법", RULES, 980, b(86), (i) => KO[i])}
      </div>
      {/* 87: 이미 손실을 봤어도 늦지 않았다 */}
      <Box x={960} y={300} w={1600} center>
        <div style={{...vis(f, p87), opacity: enter(f, p87) * fadeOut(f, p88)}}>
          <Label size={52}>이미 손실을 봤어도</Label>
          <Headline size={110} style={{marginTop: 16}}>
            <Hi at={a(87, 0.4)} until={p88}>
              늦지 않았다
            </Hi>
          </Headline>
        </div>
      </Box>
      {/* 88: 지금 내 계좌에서 가장 비중이 큰 종목이 몇 %? */}
      <div style={{position: "absolute", inset: 0, opacity: fadeOut(f, p89)}}>
        <Box x={660} y={230}>
          <Phone at={p88} w={600} h={500}>
            <Label size={44}>내 계좌</Label>
            <Label size={36} weight={500} color={C.gray} style={{marginTop: 30, opacity: enter(f, a(88, 0.3))}}>
              가장 비중이 큰 종목
            </Label>
            <div style={{marginTop: 10, opacity: enter(f, a(88, 0.5))}}>
              <Big size={150}>
                <Hi at={a(88, 0.65)} until={p89}>
                  몇 %?
                </Hi>
              </Big>
            </div>
          </Phone>
        </Box>
      </div>
      {/* 89: 큰 수익보다 대처 가능하게 */}
      <div style={{position: "absolute", inset: 0, opacity: enter(f, p89) * fadeOut(f, p90)}}>
        <Box x={200} y={360}>
          <div style={vis(f, p89)}>
            <Headline size={84} color={C.gray}>
              <StrikeAt at={a(89, 0.3)} color={C.ink}>
                큰 수익
              </StrikeAt>
            </Headline>
          </div>
        </Box>
        <Box x={860} y={360}>
          <div style={vis(f, a(89, 0.4))}>
            <Headline size={84}>
              <Hi at={a(89, 0.6)}>대처 가능하게</Hi> 투자
            </Headline>
          </div>
        </Box>
      </div>
      {/* 90–91: 성공 투자 */}
      <Box x={960} y={400} w={1000} center>
        <div style={{...vis(f, a(90, 0.1)), opacity: enter(f, a(90, 0.1)) * fadeOut(f, end)}}>
          <Headline size={96}>성공 투자</Headline>
        </div>
      </Box>
    </>
  );
};
