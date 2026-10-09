# 공통 지시사항 — 모든 주제에 쓰는 영상 제작 규칙

이 폴더(`guides/`)는 **주제와 상관없이** 쓰는 지시사항이다. 주제마다 다른 내용(시청자, 금액 기준, 고지 문구, 근거 자료, 피드백 사례)은 각 주제 폴더의 `guides/`에 있다.
**주제 규칙이 공통 규칙과 다르면 주제 규칙을 따른다.**

## 파일

| 파일 | 하는 일 | 함께 읽는 주제 파일 (주식 예) |
|---|---|---|
| `title_guide.md` | 주제 탐색, 제목 공식, 영상별 제목 3개 | `stock/guides/title_rules.md` |
| `script_guide.md` | 대본(사연→진행자→고지→문제 분석→올바른 방법→마무리), SRT 자막 | `stock/guides/script_rules.md` |
| `thumbnail_guide.md` | 영상별 썸네일 시안 3개의 프롬프트 파일, Remotion Still 렌더 | `stock/guides/thumbnail_rules.md` |
| `video_guide.md` | Remotion 모션그래픽 영상 (장면 구성표 → 스토리보드 승인 → 렌더) | `stock/guides/script_rules.md` (재구성 문구 등) |
| `archive/` | 지금은 쓰지 않는 옛 지시사항 | — |

모든 지시사항이 근거로 쓰는 분석 결과는 `<주제폴더>/guides/data_insights.md`에 있다. 원본 데이터는 `<주제폴더>/result/`(분석기 `youtube_topic_analyzer.py` 결과)다.

## 영상 하나를 만드는 순서

| 단계 | 할 일 | 지시사항 | 결과물 (`<주제폴더>/` 기준) |
|---|---|---|---|
| 0 | (선택) 분석 다시 돌리기 → `data_insights.md` 갱신 | 저장소 `README.md`의 분석기 사용법 | `result/`, `guides/data_insights.md` |
| 1 | 주제 고르기 | `title_guide.md` 0번 | (대화) |
| 2 | 제목 후보 → 사용자 선택 | `title_guide.md` 7·10번 | `titles/title_candidates_<날짜>.md` |
| 3 | 대본 TXT·SRT·README | `script_guide.md` | `source/<영상ID>/` |
| 4 | 영상별 제목 3개 | `title_guide.md` 11번 | `source/<영상ID>/titles.md` |
| 5 | 썸네일 프롬프트 3개 | `thumbnail_guide.md` | `source/<영상ID>/thumbnails/thumbnail_1~3.md` |
| 6 | 내레이션 녹음(`narration.mp3`)·배경음악(`bgm.mp3`) 넣기 | `video_guide.md` 0번 | `source/<영상ID>/` |
| 7 | 장면 구성표 → 스토리보드 → **사용자 승인** → 렌더 | `video_guide.md` | `out/<영상ID>/` |
| 8 | 썸네일 3장 렌더 | `thumbnail_guide.md` 5번 | `out/<영상ID>/thumbnails/` |
| 9 | 업로드 후 "테스트 및 비교" 결과 기록 | `title_guide.md` 11번, `thumbnail_guide.md` 8번 | `titles.md`, `thumbnails/*.md` 결과 칸 |

Claude Code에 시킬 때 예시:
> `guides/README.md`와 `stock/guides/`를 읽고, `stock/source/multagi-2026-10/` 대본으로 `guides/video_guide.md` 순서대로 영상을 만들어 줘. 스토리보드에서 멈춰.

## 새 주제 시작하기 (예: 부동산)

1. 분석 설정 파일을 만든다: `python youtube_topic_analyzer.py --topic 부동산 --folder realestate --init-config`
   - 결과: `realestate/analyzer_config.toml`
   - 그 파일의 `KEYWORD_GROUPS`·`RELEVANCE_TERMS`를 채운다.
2. 분석을 실행한다: `python youtube_topic_analyzer.py --config realestate/analyzer_config.toml`
   - 결과: `realestate/result/`
3. 주식 폴더를 본떠 주제 규칙을 만든다.
   - `realestate/guides/script_rules.md`, `title_rules.md`, `thumbnail_rules.md`, `data_insights.md`
   - `realestate/source/used_content.md`
   - 시청자·금액 기준·고지 문구·마무리 인사·색 의미처럼 주제마다 다른 것만 적는다.
4. 위 "영상 하나를 만드는 순서"대로 진행한다. 영상 프로젝트(`video/`)는 주제끼리 같이 쓴다.
