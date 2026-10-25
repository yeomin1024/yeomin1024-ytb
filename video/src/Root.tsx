// 컴포지션 등록 — 영상마다 하나 (ID = 영상ID). guides/video_guide.md 2번
// 2026-10-25: 주식 옛 Remotion 영상 4편(multagi·bittu·panicsell·molppang)을 지워 등록된 컴포지션이 없다 (되살리기: git checkout 2a0427d0 -- video/src).
import React from "react";
import {loadFonts} from "./design/fonts";

loadFonts();

export const RemotionRoot: React.FC = () => <></>;
