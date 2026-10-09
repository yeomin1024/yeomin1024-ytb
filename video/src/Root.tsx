// 컴포지션 등록 — 영상마다 하나 (ID = 영상ID). guides/video_guide.md 2번
import React from "react";
import {Composition} from "remotion";
import {loadFonts} from "./design/fonts";
import {FPS, H, W} from "./design/tokens";
import {DURATION as MULTAGI_DURATION, Episode as Multagi} from "./episodes/multagi-2026-10/Episode";

loadFonts();

export const RemotionRoot: React.FC = () => (
  <>
    <Composition id="multagi-2026-10" component={Multagi} durationInFrames={MULTAGI_DURATION} fps={FPS} width={W} height={H} />
  </>
);
