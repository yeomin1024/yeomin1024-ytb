# 공통 지시사항 — 모든 주제에 쓰는 영상 제작 규칙

버전: v1.3 — 2026-10-10 — 사용자 지시: 스토리보드·승인 단계 삭제(오디오가 생기면 바로 영상), 내레이션은 사연자·진행자 목소리 설정 파일(`voices/`)로 대본 전부 한 번에, 사례는 되도록 최신 (v1.2: 내레이션은 Kaggle에서 오픈소스 음성 AI로, v1.1: 전체 진행 순서를 `pipeline.md`로 (분석 → 지시사항·주제 → 제목·썸네일 프롬프트·업로드 시트·대본·스토리보드 → 요약 문서 → 오디오가 생기면 렌더·비공개 업로드))

이 폴더(`guides/`)는 **주제와 상관없이** 쓰는 지시사항이다. 주제마다 다른 내용(시청자, 금액 기준, 고지 문구, 근거 자료, 피드백 사례)은 각 주제 폴더의 `guides/`에 있다.
**주제 규칙이 공통 규칙과 다르면 주제 규칙을 따른다.**

## 파일

| 파일 | 하는 일 | 함께 읽는 주제 파일 (주식 예) |
|---|---|---|
| **`pipeline.md`** | **전체 진행 순서 1~4단계, 사용자가 처음 한 번 할 일(키 설정), Claude에게 하는 말 예시** | — |
| `title_guide.md` | 주제 탐색, 제목 공식, 영상별 제목 3개 | `stock/guides/title_rules.md` |
| `script_guide.md` | 대본(사연→진행자→고지→문제 분석→올바른 방법→마무리), SRT 자막 | `stock/guides/script_rules.md` |
| `thumbnail_guide.md` | 영상별 썸네일 시안 3개의 프롬프트 파일 (이미지는 사용자가 이미지 AI로, 코드로 렌더하지 않음) | `stock/guides/thumbnail_rules.md` |
| `video_guide.md` | Remotion 모션그래픽 영상 (오디오가 생기면: 장면 구성 `plan.ts` → 영상 코드 → still 자체 점검 → 렌더, 승인 없음) | `stock/guides/script_rules.md` (재구성 문구 등) |
| `upload_guide.md` | 업로드 시트: 설명란·챕터·태그·고정 댓글·업로드 설정 | `stock/guides/upload_rules.md` |
| `tts_guide.md` | 내레이션 만들기: Kaggle GPU에서 Qwen3-TTS(오픈소스). 사연자·진행자 목소리 설정(`voices/*.json`), 대본 전부 한 번에(`all`) → zip → `narration.mp3` | — |
| `archive/` | 지금은 쓰지 않는 옛 지시사항 | — |

모든 지시사항이 근거로 쓰는 분석 결과는 `<주제폴더>/guides/data_insights.md`에 있다. 원본 데이터는 `<주제폴더>/result/`(분석기 `youtube_topic_analyzer.py` 결과)다.

## 영상 하나를 만드는 순서 (자세히: `pipeline.md`)

| 단계 | 할 일 | 지시사항·명령 | 결과물 (`<주제폴더>/` 기준) |
|---|---|---|---|
| 1 | 분석 결과가 없으면 분석기 실행 | `bash tools/run_analysis.sh <주제폴더>` | `result/` |
| 2 | 분석 결과로 주제 규칙·`data_insights.md` 만들기·고치기 → 주제 탐색 | `data_insights.md` 9번, `title_guide.md` 0번 | `guides/`, 주제 후보 |
| 3 ① | 대본 TXT·SRT·README — SRT 검사: 문장 / 자막 / SRT–TXT 일치 / 고지 공백. 사례·연구는 되도록 최신(2020년대 먼저) | `script_guide.md` | `source/<영상ID>/` |
| 3 ② | 제목 3개 (1개 채택, 짝 썸네일) | `title_guide.md` 11번 | `source/<영상ID>/titles.md` |
| 3 ③ | 썸네일 **프롬프트** 3개 (이미지는 사용자가 이미지 AI로) | `thumbnail_guide.md` | `source/<영상ID>/thumbnails/thumbnail_1~3.md` |
| 3 ④ | 업로드 시트 (제목·설명란·챕터 명령·태그·고정 댓글) | `upload_guide.md` | `source/<영상ID>/upload.md` |
| 3-5 | 영상별 요약 문서 (스토리보드 없음) | `python tools/make_summary.py <주제폴더> <영상ID>` | `source/<영상ID>/summary.md` |
| 3-6 | 내레이션 (사용자, Kaggle): 대본 전부 → 사연자·진행자 목소리 → zip → GitHub에 올림 | `python tools/tts_narration.py all`, `tts_guide.md` | `source/<영상ID>/narration.mp3` |
| 4 | 오디오가 생기면 → 영상 코드가 없으면 Claude가 만들고 스스로 점검(**승인 없음**) → SRT 맞춤 → 렌더 → 유튜브 **비공개** 업로드 + 1시간 뒤 예약 공개 (최대 3개) | `video_guide.md` 6번, `bash tools/publish.sh`, `upload_guide.md` 9번 | `video/src/episodes/<영상ID>/`, `out/<영상ID>/final_1080p.mp4`, `source/<영상ID>/youtube.json` |
| 그 뒤 | 스튜디오에서 테스트 및 비교(썸네일 3개)·자동 더빙 확인·공개 전환 → 결과 기록 | `upload_guide.md` 7번 | `upload.md`·`titles.md`·`thumbnails/*.md` 결과 칸 |

Claude Code에 시킬 때 예시는 `pipeline.md` 마지막 표에 있다.

## 새 주제 시작하기 (예: 부동산)

1. 분석 설정 파일을 만든다: `python youtube_topic_analyzer.py --topic 부동산 --folder realestate --init-config`
   - 결과: `realestate/analyzer_config.toml`
   - 그 파일의 `KEYWORD_GROUPS`·`RELEVANCE_TERMS`를 채운다.
2. 분석을 실행한다: `python youtube_topic_analyzer.py --config realestate/analyzer_config.toml` (클라우드에서는 `bash tools/run_analysis.sh realestate`)
   - 결과: `realestate/result/`
3. 주식 폴더를 본떠 주제 규칙을 만든다.
   - `realestate/guides/script_rules.md`, `title_rules.md`, `thumbnail_rules.md`, `data_insights.md`
   - `realestate/source/used_content.md`
   - 시청자·금액 기준·고지 문구·마무리 인사·색 의미처럼 주제마다 다른 것만 적는다.
4. 위 "영상 하나를 만드는 순서"대로 진행한다. 영상 프로젝트(`video/`)는 주제끼리 같이 쓴다.

## 변경 이력

| 버전 | 날짜 | 변경 내용 |
|---|---|---|
| v1.3 | 2026-10-10 | 사용자 지시: 3 ⑤(영상 코드·스토리보드 승인) 삭제 → 4단계에서 오디오가 생기면 영상 코드부터 승인 없이, 3-6 내레이션(사연자·진행자 목소리 설정, 대본 전부 `all`), 사례는 최신 |
| v1.2 | 2026-10-10 | 사용자 지시: `tts_guide.md` 추가 (Kaggle에서 오픈소스 음성 AI로 내레이션), 순서 표 4단계에 오디오 만드는 법 |
| v1.1 | 2026-10-10 | 사용자 지시: `pipeline.md` 추가, 순서 표를 1~4단계(분석·주제·제작·요약·자동 업로드)로 바꿈, 썸네일은 프롬프트만 |
| v1.0 | 2026-10-09 | 최초 작성: 공통·주제 규칙 분리, 작업 순서 표 |
