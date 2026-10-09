// Remotion 설정 — guides/video_guide.md 2번 (1080p 30fps, 무거운 효과 금지)
import {Config} from "@remotion/cli/config";

Config.setVideoImageFormat("jpeg");
Config.setOverwriteOutput(true);
Config.setConcurrency(null);           // CPU 코어 수에 맞춰 자동
// 이미 설치된 크롬을 쓰려면 환경변수 REMOTION_BROWSER 에 실행 파일 경로를 넣는다 (없으면 Remotion이 자동으로 받음)
if (process.env.REMOTION_BROWSER) {
  Config.setBrowserExecutable(process.env.REMOTION_BROWSER);
}
