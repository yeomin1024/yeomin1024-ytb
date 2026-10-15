# 공통 지시사항 — 모든 주제에 쓰는 영상 제작 규칙

버전: v1.20 — 2026-10-15 — 사용자 지시 "썸네일 문구는 제목에서 더 줄일 수 있는 부분을 줄이고 … 하나는 정말로 썸네일 클릭율이 높도록 만들고 나머지 2개는 좀 실험적인걸로": `thumbnail_guide.md` v2.0 전면 개정(옛 v1.3.1 → `archive/thumbnail_guide_v1.md`) (v1.19 — 2026-10-14 — 사용자 지시 "주제 탐색, 제목 생성, 대본 생성을 어떻게 했는지와 피드백을 반영해서 각각 지시사항 파일": `topic_guide.md` v1.0 신설, `title_guide.md`·`script_guide.md` v3.0 전면 개정(옛 것은 `archive/`), 도구 `tools/content_research.py`·`tools/law_text.py` (v1.18 — 2026-10-14 — 사용자 지시: 분석 결과는 `result/outliers/analysis.md`(성공 사례·주제·수요와 공급·제목·썸네일·구성·구독자·시청자 니즈 — 지시사항 재료) (v1.17 — 2026-10-14 — 사용자 지시: PC 분석은 웹 화면(`pc_analysis.md` v1.9 "웹 화면") (v1.16 — 2026-10-13 — 사용자 지시: 검색어는 `<주제>/keywords.txt`에 한 줄에 하나 (그룹 없음) (v1.15 — 2026-10-13 — 사용자 지시: 검색어는 실제 영상 태그에서 고름(`tools/tag_keywords.py`·`<주제>/tag_rules.toml`), 새 주제 시작하기 1번 (v1.14 — 2026-10-13 — 실행 명령을 `-File run_analyzer.ps1`(`.\` 없이 — Git Bash 오류) (v1.13 — 2026-10-13 — 사용자 지시: 여러 주제를 동시에 분석 (주제마다 `keywords.toml`·`.env`, `pc_analysis.md` v1.2) (v1.12 — 2026-10-13 — 사용자 지시: 성공 사례·조회수 상위(구독자 무관)의 댓글 전부, 저장소가 비공개면 사례 폴더까지 전부 올림 (`pc_analysis.md` v1.1) (v1.11 — 2026-10-13 — 사용자 지시: 주제 폴더를 모두 지우고 `economic/`(경제·재테크) 하나로, 검색어는 `<주제폴더>/keywords.toml`로 따로, 분석은 집 PC에서(`pc_analysis.md` — 할당량 초기화 뒤 남은 부분부터 자동으로 이어서) (v1.10 — 2026-10-12 — 사용자 지시: 올린 영상 줄이기(스튜디오 컷, `upload_guide.md` 10번·`tools/studio_trim.py`) (v1.9 — 2026-10-12 — 사용자 지시: 성공 사례 분석은 최근·작은 채널·배수 기준과 댓글의 시청자 니즈로, 주제마다 자기 자료만 (v1.8: 사연 20~30초로 짧지만 강렬하게, 내레이션 목소리는 샘플을 듣고 골라 고정; v1.7: 업로드 설정 '변경되거나 합성된 콘텐츠' = 예; v1.6: 썸네일 3개 모두 아래쪽 제목 문구 2줄·thumbnail_3은 검은 배경에 채택 제목 문구 그대로(노랑·빨강 강조), 렌더 뒤 음량 -14 LUFS (v1.5: 진행자는 중저음 남성, 모든 대본에서 같은 목소리 (v1.4: 오디오는 고르지 않고 하나로, 결과 파일은 대본 폴더마다 GitHub에 자동으로 (v1.3: 스토리보드·승인 단계 삭제(오디오가 생기면 바로 영상), 내레이션은 사연자·진행자 목소리 설정 파일(`voices/`)로 대본 전부 한 번에, 사례는 되도록 최신 (v1.2: 내레이션은 Kaggle에서 오픈소스 음성 AI로, v1.1: 전체 진행 순서를 `pipeline.md`로 (분석 → 지시사항·주제 → 제목·썸네일 프롬프트·업로드 시트·대본·스토리보드 → 요약 문서 → 오디오가 생기면 렌더·비공개 업로드))))))))))))

이 폴더(`guides/`)는 **주제와 상관없이** 쓰는 지시사항이다. 주제마다 다른 내용(시청자, 금액 기준, 고지 문구, 근거 자료, 피드백 사례)은 각 주제 폴더의 `guides/`에 있다.
**주제 규칙이 공통 규칙과 다르면 주제 규칙을 따른다.**

> 2026-10-13: 주제 폴더는 `economic/`(경제·재테크) 하나다. 아래 지시사항 곳곳의 `stock/…` 경로는 지운 옛 주식 폴더의 **예시**다 — 내용은 git 커밋 `2a68307`에 있다 (`git show 2a68307:stock/guides/script_rules.md`). 경제·재테크의 주제 규칙(`economic/guides/`)은 분석 결과가 나온 뒤 만든다.

## 파일

| 파일 | 하는 일 | 함께 읽는 주제 파일 (예: 옛 주식 폴더 — 경제·재테크는 `economic/guides/` 같은 이름) |
|---|---|---|
| **`pipeline.md`** | **전체 진행 순서 1~4단계, 사용자가 처음 한 번 할 일(키 설정), Claude에게 하는 말 예시** | — |
| **`pc_analysis.md`** | **집 PC에서 분석 돌리기**: `run_analyzer.ps1` → **웹 화면**(키·검색어·영상/채널 추가·탐색→체크→승인→주별 분석 1·2·3…주). **분석 결과 = `<주제폴더>/result/outliers/analysis.md`** (성공 사례·주제·수요와 공급·제목·썸네일·구성·구독자·시청자 니즈 — 2단계 지시사항 재료). 자동 실행(`-Auto`):  성공 사례 + 조회수 상위(구독자 무관)의 자막·썸네일·**댓글 전부** + 주제 분석 → GitHub(비공개 저장소면 사례 폴더까지), 할당량이 모자라면 초기화(한국 오후 4~5시) 뒤 남은 부분만 자동으로 이어서. 저장소를 비공개로 바꾸는 법 | `<주제폴더>/keywords.txt`(검색어, 한 줄에 하나) · `keywords.toml`(관련어) · `analyzer_config.toml` |
| **`topic_guide.md`** (v1.0) | **주제 탐색**: 시청자층(댓글 나이) → 시청자가 가장 원하는 정보(질문 묶음) = 결론 → 시장(수요·공급·같은 채널) → 후보 표 → 결론·오래가는 원칙·바뀔 수 있는 것 (`tools/content_research.py audience·needs`) | `<주제>/guides/data_insights.md` 1번, `<주제>/research_rules.toml` |
| **`title_guide.md`** (v3.0) | **제목**: 호기심 구절 + 해소 구절, 형식·낱말·맨 앞 말·금액 표현을 비교 집단·좁힌 주제·같은 채널로 확인, 60자 이하, 숫자는 대본이 증명 (`content_research.py titles`) | `data_insights.md` 2번 |
| **`script_guide.md`** (v3.0) | **대본**: 사용자 피드백 18개(0번), 7챕터 구성(도입 50초에 결론·약속·기준 날짜 → 예시 인물 → 원칙 2~3개 → 순서 → 결과 → 이미 하고 있다면 → 정리·감사 인사), 사실은 오늘 시행 중인 법령 원문(`tools/law_text.py`), 숫자는 계산 코드, 측정(`content_research.py measure`), SRT. 사연 파트는 선택 | `data_insights.md` 3·4번, 완성 예 `economic/source/eunte-kkeonaeseugi-2026-10/` |
| `thumbnail_guide.md` v3.0 | 영상별 썸네일 프롬프트 3개 — 본안 1(클릭률 최대) + 실험안 2, 모두 아래쪽 2줄(채택 제목 줄임, 노랑 = 중요·빨강 = 나쁜 상황), 그림은 문구의 장면, 댓글 니즈 낱말은 낱말 그대로 (이미지는 사용자가 이미지 AI로, 코드로 렌더하지 않음) | `<주제>/guides/data_insights.md` '썸네일' |
| `video_guide.md` | Remotion 모션그래픽 영상 (오디오가 생기면: 장면 구성 `plan.ts` → 영상 코드 → still 자체 점검 → 렌더 → 음량 -14 LUFS, 승인 없음) | `stock/guides/script_rules.md` (재구성 문구 등) |
| `upload_guide.md` | 업로드 시트: 설명란·챕터·태그·고정 댓글·업로드 설정 | `stock/guides/upload_rules.md` |
| `tts_guide.md` | 내레이션 만들기: Kaggle GPU에서 Qwen3-TTS(오픈소스). 사연자(Sohee)·진행자(중저음 남성, 기준 목소리 `voices/ref/host.wav`를 모든 대본이 복제) 목소리 설정(`voices/*.json`), 대본 전부 한 번에(`all --push`) → 영상마다 `narration.mp3` 하나를 대본 폴더에 자동으로 올림 | — |
| `archive/` | 지금은 쓰지 않는 옛 지시사항 | — |

모든 지시사항이 근거로 쓰는 분석 결과는 `<주제폴더>/guides/data_insights.md`에 있다. 그 근거는 **그 주제의 최근·작은 채널 성공 사례와 댓글의 시청자 니즈**다 (`tools/outlier_research.py`, `pipeline.md` 1단계 4번·2단계 2번 — 다른 주제 결과를 빌려 쓰지 않음, 사용자 지시 2026-10-12). 원본 데이터는 `<주제폴더>/result/`(분석기 `youtube_topic_analyzer.py` 결과)다.

## 영상 하나를 만드는 순서 (자세히: `pipeline.md`)

| 단계 | 할 일 | 지시사항·명령 | 결과물 (`<주제폴더>/` 기준) |
|---|---|---|---|
| 1 | 분석 결과가 없으면 분석 — **집 PC**(자막·썸네일까지, 남으면 다음 날 자동으로 이어서) 또는 클라우드(분석기만) | `pc_analysis.md` (`run_analyzer.ps1`), 클라우드 `bash tools/run_analysis.sh <주제폴더>` | `result/`, `result/outliers/` |
| 2 | 분석 결과로 `data_insights.md` 만들기·고치기(`content_research.py all`) → 주제 탐색 | `topic_guide.md` | `guides/`, `source/topic_candidates.md` |
| 3 ① | 대본 TXT·SRT·README·확인표·계산 코드 — 7~8분, 결론 먼저, 오늘 시행 중인 법령으로 사실 확인, 숫자는 계산 코드(사연 파트를 넣으면 20~30초). SRT 검사 ✅. 사례·연구는 되도록 최신(2020년대 먼저) | `script_guide.md` v3.0 | `source/<영상ID>/` |
| 3 ② | 제목 3개 (R1 추천, 근거 표, 짝 썸네일) | `title_guide.md` v3.0 | `source/<영상ID>/titles.md` |
| 3 ③ | 썸네일 **프롬프트** 3개 — 본안 1 + 실험안 2, 모두 아래쪽 2줄 (이미지는 사용자가 이미지 AI로) | `thumbnail_guide.md` v3.0 | `source/<영상ID>/thumbnails/thumbnail_1~3.md`·`README.md`·`chatgpt.md`·이미지 |
| 3 ④ | 업로드 시트 (제목·설명란·챕터 명령·태그·고정 댓글) | `upload_guide.md` | `source/<영상ID>/upload.md` |
| 3-5 | 영상별 요약 문서 (스토리보드 없음) | `python tools/make_summary.py <주제폴더> <영상ID>` | `source/<영상ID>/summary.md` |
| 3-6 | 내레이션 (사용자, Kaggle 셀 하나): (처음 한 번) 목소리 후보 샘플 → 사용자가 듣고 고름 → Claude `pick` → 대본 전부 → 고른 사연자·진행자 목소리 → 영상마다 오디오 하나 → 대본 폴더마다 GitHub에 자동으로 | `python tools/tts_narration.py all --push`, `tts_guide.md` | `source/<영상ID>/narration.mp3` |
| 4 | 오디오가 생기면 → 영상 코드가 없으면 Claude가 만들고 스스로 점검(**승인 없음**) → SRT 맞춤 → 렌더 → 음량 맞춤(-14 LUFS) → 유튜브 **비공개** 업로드 + 1시간 뒤 예약 공개 (최대 3개) | `video_guide.md` 6번, `bash tools/publish.sh`, `upload_guide.md` 9번 | `video/src/episodes/<영상ID>/`, `out/<영상ID>/final_1080p.mp4`, `source/<영상ID>/youtube.json` |
| 그 뒤 | 스튜디오에서 테스트 및 비교(썸네일 3개)·자동 더빙 확인·공개 전환 → 결과 기록 | `upload_guide.md` 7번 | `upload.md`·`titles.md`·`thumbnails/*.md` 결과 칸 |

Claude Code에 시킬 때 예시는 `pipeline.md` 마지막 표에 있다.

## 새 주제 시작하기 (예: 부동산)

1. 분석 설정 파일을 만든다: `python youtube_topic_analyzer.py --topic 부동산 --folder realestate --init-config`
   - 결과: `realestate/analyzer_config.toml` + 검색어 파일 `realestate/keywords.toml` (분석기 v2.4.0)
   - `keywords.toml`의 `RELEVANCE_TERMS`(주제 관련어)를 채우고, `<폴더>/tag_rules.toml`(씨앗 검색어·빼는 말·묶음 — 예: `economic/tag_rules.toml`)을 만든 뒤 `python tools/tag_keywords.py <폴더> --write-keywords`로 검색어 목록 `<폴더>/keywords.txt`(한 줄에 하나)를 **실제 영상 태그**로 채운다 (사용자 지시 2026-10-13 — 직접 적어도 됨). 예: `economic/keywords.txt`
2. 분석을 실행한다 (집 PC): `powershell -ExecutionPolicy Bypass -File run_analyzer.ps1 -Folder realestate` — 다른 주제와 동시에: `-Folder economic,realestate` → `pc_analysis.md` "여러 주제를 동시에" (같은 키는 하루 할당량을 나눠 씀)
   - 결과: `realestate/result/`, `realestate/result/outliers/` (클라우드에서는 `bash tools/run_analysis.sh realestate` — 자막·썸네일 없음)
3. 분석 결과로 주제 규칙을 만든다 (형식은 옛 주식 폴더 `git show 2a68307:stock/guides/<파일>`을 본뜸).
   - `realestate/guides/script_rules.md`, `title_rules.md`, `thumbnail_rules.md`, `data_insights.md`
   - `realestate/source/used_content.md`
   - 시청자·금액 기준·고지 문구·마무리 인사·색 의미처럼 주제마다 다른 것만 적는다.
4. 위 "영상 하나를 만드는 순서"대로 진행한다. 영상 프로젝트(`video/`)는 주제끼리 같이 쓴다.

## 변경 이력

| 버전 | 날짜 | 변경 내용 |
|---|---|---|
| v1.20 | 2026-10-15 | 사용자 지시 "썸네일 문구는 제목에서 더 줄일 수 있는 부분을 줄이고 … 나머지 2개는 좀 실험적인걸로": `thumbnail_guide.md` v2.0 (본안 1 + 실험안 2, 하단 2줄 = 채택 제목 줄임, 노랑 = 중요·빨강 = 나쁜 상황, 댓글 니즈 낱말은 낱말 그대로, 검은 배경 thumbnail_3 없앰) |
| v1.19 | 2026-10-14 | 사용자 지시 "주제 탐색, 제목 생성, 대본 생성 … 각각 지시사항 파일": `topic_guide.md` v1.0 신설, `title_guide.md`·`script_guide.md` v3.0(옛 v2.1·v2.4.1 → `archive/`), 재테크 근거 `economic/guides/data_insights.md`, 도구 `tools/content_research.py`·`tools/law_text.py` |
| v1.17 | 2026-10-14 | 사용자 지시 "분석기 웹 ui 형식으로": `pc_analysis.md` v1.9 웹 화면 |
| v1.16 | 2026-10-13 | 사용자 지시 "꼭 그룹을 지정해야하나 검색어만 넣어도 되잖아": 검색어 `keywords.txt` (`pc_analysis.md` v1.8, `pipeline.md` v1.16) |
| v1.15 | 2026-10-13 | 사용자 지시 "그냥 검색어를 재테크 관련 태그로 찾아서 다 그걸로 탐색해봐": 새 주제 시작하기 1번 — 검색어는 `tag_keywords.py`로 태그에서 (`pc_analysis.md` v1.6, `pipeline.md` v1.15) |
| v1.14 | 2026-10-13 | 사용자 PC 오류("-File 매개 변수에 대한 인수 '.run_analyzer.ps1'이(가) 없습니다"): 새 주제 시작하기 2번 명령을 `-File run_analyzer.ps1`로 (`pc_analysis.md` v1.3) |
| v1.13 | 2026-10-13 | 사용자 지시 "동시에 병렬로 다른 주제 분석도 가능하도록 … 검색어 설정 파일, 키설정 파일도 여러개": 새 주제 시작하기 2번(동시에), `pc_analysis.md` v1.2 |
| v1.12 | 2026-10-13 | 사용자 지시 "비공개로 돌릴테니까 전부 다 업로드되게 하고 댓글은 전부 …": `pc_analysis.md` v1.1, `pipeline.md` v1.12, `tts_guide.md` v1.8(비공개 저장소에서 Kaggle 셀) |
| v1.11 | 2026-10-13 | 사용자 지시 "기존 stock, health 등 모든 주제 폴더 전부 삭제하고 경제, 재태크(economic) 폴더만 … 검색어 목록 같은거는 따로 빼놓고 분석기 코드 pc에서 돌릴 수 있도록 … api 할당량이 초기화된 시간이 되면 다시 자동으로 … 확인 못한 부분부터": `pc_analysis.md` v1.0 추가, 1단계 = 집 PC 권장, 새 주제는 `keywords.toml`, 옛 `stock/…` 경로는 커밋 `2a68307`의 예시 |
| v1.10 | 2026-10-12 | 사용자 지시 "패닉셀 … 사연 부분을 줄일려고 하는데 자를 부분좀 알려줘봐": 올린 영상 줄이기 — `upload_guide.md` v1.5 10번(스튜디오 '새 컷', `tools/studio_trim.py` v1.0), `srt_tool.py` v1.6(올린 영상의 사연 길이는 실측 진행자 시작 ≤ 0:30) |
| v1.9 | 2026-10-12 | 사용자 지시: 성공 사례 분석 다시 — `tools/outlier_research.py`(최근 180일·구독자 5만 이하·조회수≥구독자×3·4분 이상), data_insights는 주제 자기 자료·시청자 니즈 중심, 빌린 근거 금지 (`pipeline.md` v1.9) |
| v1.8 | 2026-10-12 | 사용자 지시: 사연 20~30초 (`script_guide.md` v2.4 0-1의 13번·2-1, 주제 `script_rules.md`, `srt_tool.py` v1.5 검사 — 근거 패닉셀 평균 시청 약 50초), 목소리 샘플 고르기 (`tts_guide.md` v1.5 4-0, `tts_narration.py` v1.4 samples·pick) |
| v1.7 | 2026-10-11 | 사용자 지시: 업로드 설정 '변경되거나 합성된 콘텐츠' = 예 (AI 음성 내레이션, `upload_guide.md` v1.4, `youtube_upload.py` v1.3이 자동 등록) |
| v1.6 | 2026-10-11 | 사용자 지시: 썸네일 하단 제목 2줄·thumbnail_3 검은 배경 제목형 (`thumbnail_guide.md` v1.3, 주제 `thumbnail_rules.md`), 4단계 렌더 뒤 음량 맞춤 (`video_guide.md` v3.6, `tools/loudnorm.py`) |
| v1.5 | 2026-10-11 | 사용자 지시: 진행자 중저음 남성·모든 대본 같은 목소리 (`tts_guide.md` 4-1) |
| v1.4 | 2026-10-11 | 사용자 지시: 3-6 오디오 하나·고르지 않음, 결과는 Kaggle이 대본 폴더마다 GitHub에 자동으로 올림 |
| v1.3 | 2026-10-10 | 사용자 지시: 3 ⑤(영상 코드·스토리보드 승인) 삭제 → 4단계에서 오디오가 생기면 영상 코드부터 승인 없이, 3-6 내레이션(사연자·진행자 목소리 설정, 대본 전부 `all`), 사례는 최신 |
| v1.2 | 2026-10-10 | 사용자 지시: `tts_guide.md` 추가 (Kaggle에서 오픈소스 음성 AI로 내레이션), 순서 표 4단계에 오디오 만드는 법 |
| v1.1 | 2026-10-10 | 사용자 지시: `pipeline.md` 추가, 순서 표를 1~4단계(분석·주제·제작·요약·자동 업로드)로 바꿈, 썸네일은 프롬프트만 |
| v1.0 | 2026-10-09 | 최초 작성: 공통·주제 규칙 분리, 작업 순서 표 |
