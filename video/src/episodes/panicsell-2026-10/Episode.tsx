// panicsell-2026-10 — 하락장 패닉셀 (문장 92 / 자막 111 + 고지 카드 1개, 번호는 대본 문장 번호)
// 장면 구성표: stock/out/panicsell-2026-10/scene_plan.md · 데이터 시트: ./facts.ts
// ※ 투자 교육용 영상. 특정 종목의 매수·매도 권유가 아님.
import React from "react";
import {AbsoluteFill, Html5Audio, Sequence, staticFile} from "remotion";
import {Bg, C, FPS} from "../../design/tokens";
import {Src, makeTimeline, sceneTime} from "../../components/timeline";
import {Scene, WIPE} from "../../components/ui";
import {DisclaimerCard, ReconCaption, Subtitles} from "../../components/overlays";
import {SRC} from "./subtitles";
import {RECON} from "./facts";
import {PLAN_ROWS, STORY_LAST} from "./plan";
import {S01, S02, S03, S04, S05, S06, SceneC} from "./scenes/story";
import {S07, S08, S09} from "./scenes/host";
import {S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20} from "./scenes/problems";
import {S21, S22, S23, S24, S25, S26, S27, S28, S29, S30, S31} from "./scenes/methods";

const SOURCE: Src = SRC;
export const tl = makeTimeline(SOURCE, FPS);

// 장면 구성(자막 범위·배경·전환·연출 설명)은 plan.ts, 여기서는 장면 컴포넌트만 연결한다
const SCENES: Record<string, SceneC> = {
  S01, S02, S03, S04, S05, S06, S07, S08, S09, S10, S11, S12, S13, S14, S15, S16,
  S17, S18, S19, S20, S21, S22, S23, S24, S25, S26, S27, S28, S29, S30, S31,
};
const DEFS = PLAN_ROWS.map((r) => {
  const C = SCENES[r.id];
  if (!C) throw new Error(`장면 컴포넌트 없음: ${r.id}`);
  return {...r, C};
});

export const PLAN = DEFS.map((d, i) => ({
  ...d,
  from: tl.s(d.subs[0]),
  to: i === DEFS.length - 1 ? tl.total : tl.e(d.subs[1]),
}));
export const DURATION = tl.total;

const bgAt = (f: number): Bg => PLAN.find((p) => f >= p.from && f < p.to)?.bg ?? "cream";

export const Episode: React.FC = () => (
  <AbsoluteFill style={{background: C.cream}}>
    {PLAN.map((p, i) => {
      const next = PLAN[i + 1];
      const extra = next?.wipe ? WIPE : 0; // 다음 장면이 와이프로 들어오는 동안 아래에 계속 보이게
      return (
        <Sequence key={p.id} name={p.id} from={p.from} durationInFrames={p.to - p.from + extra}>
          <Scene bg={p.bg} dur={p.to - p.from} wipe={p.wipe}>
            <p.C t={sceneTime(tl, p.from, p.to)} />
          </Scene>
        </Sequence>
      );
    })}
    {tl.cards.map((c) => (
      <Sequence key={`card-${c.afterSentence}`} name="고지 카드" from={c.from} durationInFrames={c.to - c.from}>
        <DisclaimerCard card={c} />
      </Sequence>
    ))}
    {SOURCE.audio ? <Html5Audio src={staticFile(SOURCE.audio.file)} /> : null}
    <ReconCaption text={RECON} from={tl.s(1)} to={tl.e(STORY_LAST)} />
    <Subtitles subs={tl.subs} bgAt={bgAt} />
  </AbsoluteFill>
);
