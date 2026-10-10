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
| 점검용 still (저장소 밖 임시 폴더, 커밋하지 않음 — 스토리보드 문서는 만들지 않음, 사용자 지시 2026-10-10) | `node scripts/storyboard.mjs multagi-2026-10 /tmp/qa-multagi` (고친 장면만: `--only S05,S13`) |
| 내레이션에 SRT 맞추기 | `npm run align-audio -- stock multagi-2026-10` (오디오: `stock/source/<영상ID>/narration.mp3·wav·m4a` 또는 `--audio <파일>`) — 오디오는 고치지 않음 |
| 완성 영상 렌더 | `npx remotion render multagi-2026-10 ../stock/out/multagi-2026-10/final_1080p.mp4 --codec=h264 --crf=18` |

- 자막·고지 카드 데이터는 대본에서 만든다 (저장소 최상위에서): `python tools/srt_tool.py remotion <TXT> <SRT> video/src/episodes/<영상ID>/subtitles.ts`
- 번호는 모두 **대본 문장 번호**다 (SRT 번호 아님). 긴 문장은 앞줄·뒷줄 자막 2개 → 뒷줄 내용 그림은 `t.b(n)`.
- 고지 카드는 SRT 안의 공백(3.5초 이상)에 들어간다. 코드에서 자막·오디오를 밀지 않는다 (SRT = 영상 시간).
- `npm run align-audio`는 오디오를 `public/audio/<영상ID>.<확장자>`로 복사하고(원본 그대로, git 제외) `subtitles.ts`에 넣는다 → 영상 길이 = max(마지막 자막 + 1초, 오디오 길이).
