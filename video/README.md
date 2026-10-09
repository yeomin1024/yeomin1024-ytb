# video/ — Remotion 모션그래픽 영상 (모든 주제 공통)

지시사항: `guides/video_guide.md` · 변경 이력: `CHANGELOG.md`
※ 투자 교육용 영상 제작 도구입니다. 영상 내용은 투자 권유가 아닙니다.

## PC 준비 (한 번)
1. Node.js 20 이상 설치 (https://nodejs.org — LTS)
2. 이 폴더에서 `npm install` → 패키지 설치 + 한글 폰트 자동 다운로드(`public/fonts/`)
   - 폰트만 다시 받기: `npm run fonts`

## 자주 쓰는 명령 (이 폴더에서)
| 할 일 | 명령 |
|---|---|
| 미리보기 (브라우저) | `npm run studio` |
| 타입 검사 | `npm run typecheck` |
| 장면 구성표 + 스토리보드 | `node scripts/storyboard.mjs multagi-2026-10 ../stock/out/multagi-2026-10` (고친 장면만: `--only S05,S13`) |
| 완성 영상 렌더 | `npx remotion render multagi-2026-10 ../stock/out/multagi-2026-10/final_1080p.mp4 --codec=h264 --crf=18` |

- 자막·고지 카드 데이터는 대본에서 만든다 (저장소 최상위에서): `python tools/srt_tool.py remotion <TXT> <SRT> video/src/episodes/<영상ID>/subtitles.ts`
- 내레이션(`narration.mp3`)을 넣는 기능은 아직 없다. 녹음 파일이 생기면 SRT 타이밍을 맞춘 뒤 `Episode.tsx`에 오디오를 추가한다 (고지 카드 지점에서 오디오를 나눠야 함 — video_guide 2번).
