# 제작 판 — 모든 주제 한 판 (트렌드 → 주제 → 제목 → 썸네일 → 대본·음성 → 영상 → 업로드 → 채널 분석)

VERSION: v1.1 — 2026-11-27 — **단계마다 그 단계에서 기다리는 편만** (통과한 편은 접힌 '이 단계를 통과한 편' — 통과를 풀 때만) · **주제 모두**(심리·위기·재테크·주식·역사·쇼핑·음악·시험 채널·새 분야·수학 — `studio.toml` TOPICS) · **주제 켜기·끄기** (2-1) · 그림은 자료 안 data URI · 옛 편 저장소 기준 단계 보정 (제목 = 업로드 시트·올린 기록·titles.md · 음성·장면·영상·업로드가 있으면 앞 단계도 지남) — 사용자 지시 2026-11-27 "아니 각 단계에 맞는 것만 나오게 해야지 지금은 다 나오잖아 수정하고 주식 이런 주제는 왜 없어? 누락된거 추가하고 주제 비활성화도 할 수 있도록 해 비활성화하면 아티팩트에서 보이지 않고 에이전트가 보지도 않도록 하는거야".
이전 v1.0 — 2026-11-27 — 최초. 사용자 지시 2026-11-27 "지금 아티팩트가 심리, 위기 2개 있는데 하나로 통합하고 아래 내용을 모두 만족하도록 수정해"
(공통: 구글 트렌드 전체 탐색·주제별 검색어·명령 · PC 가 일정 간격으로 받아 올림·결과 보기 · 단계별 통과 체크된 것만 다음 단계 /
주제 탐색: 공통 규칙 수정·주제별 결과 / 제목: 규칙·자주 쓰는 낱말·성공 제목 참고(수정)·피드백 / 썸네일: 규칙·피드백·성공 문구 참고(수정) /
대본: 규칙·줄별 피드백·음성 생성 체크·체크된 것만 생성·줄별 재생성 체크 / 영상: 공통 규칙·대본만 읽고 코드로 먼저 테스트·Claude 스킬 GitHub 링크 /
업로드: 영상별 최종 종합 확인·업로드 기록·재업로드 / 채널 분석: 유튜브 연동 내 채널 자료).

- **판 주소**: https://claude.ai/artifact/Q5u1feF9sGL2jFBa8D1FPN (비공개 · 주제 = `studio/studio.toml` TOPICS 10개 (`game/` 은 유튜브 흐름 밖이라 뺌) · 옛 '심리 분석 판' FsxRtUKNLbUAPHSFYSYL7U · '위기 분석 판' LknhGN84g4NpgbwcjbK56C 를 합침 — 옛 판의 페르소나·내역은 `studio/legacy/` 에 보관, 옛 판은 사용자가 지우라고 할 때만 지움)
- **도구**: `tools/studio_board.py` (build · sync · selftest) · 틀 `studio/board_template.html` · 설정 `studio/studio.toml` (주제 = TOPICS) · 규칙 목록 `studio/rules.json` · 채널 지표 `tools/channel_stats.py` → `studio/channels/channels.json`
- 연구·교육용 — 의료·심리 상담·투자 조언이 아님.

## 1. 판을 다시 만들기 (Claude)

```bash
python3 tools/studio_board.py build          # → studio/build/ (index.html · data/*.json · img/ — git 에 넣지 않음)
```
- Artifact 도구: `file_path` = `studio/build/index.html`, `root` = `studio/build`, `files` = 바뀐 `data/*.json` (+ 새 그림 `img/…`) — **같은 주소** (studio.toml `ARTIFACT`). 다른 세션이면 먼저 `Artifact read` 한 번 뒤 `url` 로 올림.
- 언제: 대본·제목·썸네일·음성·영상·업로드 기록이 저장소에서 바뀐 뒤 · 동기화 뒤 · PC 트렌드 결과가 올라온 뒤 · `channel_stats.py` 뒤.

## 2. 단계와 통과 체크 (모든 세션이 지킴)

| 순서 | 단계 (db `gates` 의 stage) | 판 화면 | 다음 단계로 가는 조건 |
|---|---|---|---|
| 1 | 주제 `topic` | 1 주제 탐색 | 주제 통과 |
| 2 | 제목 `title` | 2 제목 | 제목 통과 |
| 3 | 썸네일 `thumb` | 3 썸네일 | 썸네일 통과 |
| 4 | 대본 `script` | 4 대본·음성 | 대본 통과 (그 뒤에만 음성 체크 가능) |
| 5 | 음성 `voice` | 4 대본·음성 | 음성 통과 |
| 6 | 코드 테스트 `codetest` | 5 영상 ① | 대본 내용만 읽고 코드 화면으로만 만든 테스트 영상 통과 (AI 그림 없이) |
| 7 | 영상 `video` | 5 영상 ② | 최종 영상 통과 |
| 8 | 업로드 `upload` | 6 업로드 | 최종 확인 7칸 + 업로드 승인 |

- **화면마다 그 단계에서 기다리는 편만** (v1.1): 1 주제 = 주제 · 2 = 제목 · 3 = 썸네일 · 4 = 대본·음성 · 5 = 코드 테스트·영상 · 6 = 업로드 (+ 올린 편은 기록·다시 올리기용으로 따로). 지금 단계 = 앞에서부터 아직 통과 안 한 첫 단계. 이미 통과한 편은 접힌 '이 단계를 통과한 편' 안에만 (체크를 풀어 되돌릴 때).
- **판 체크가 늘 이김.** 판에서 체크하지 않은 편은 저장소 기준(이미 만든 것 — 제목·썸네일 파일·페르소나 기록·음성·장면 파일·video.json·youtube.json)이 기본값.
- 앞 단계가 통과가 아니면 뒤 단계 체크는 무효 (판이 막고, `gates.json` 의 `pass` 도 앞 단계까지 모두 통과일 때만 true).
- **Claude 는 `studio/state/gates.json` 에서 그 편의 앞 단계가 `pass: true` 인 것만 다음 단계 작업** (제목 → 썸네일 → 대본 → …). 판 후보(`episodes`)는 주제 통과 뒤 Claude 가 대본 폴더를 만듦 (영상ID = `<이름>-YYYY-MM-DD`).

## 2-1. 주제 켜기·끄기 (v1.1)

- 판 '공통 › 주제 켜기·끄기' 체크를 풀면 → 판에서 바로 사라짐 (주제 단추·흐름 표·트렌드·채널 분석) → Claude 동기화 때 `studio/state/topics.json` `disabled` 에 적힘.
- **꺼 둔 주제는 Claude·하위 에이전트가 읽지도 작업하지도 않음** (CLAUDE.md) · 도구도 건너뜀: `tools/topic_state.py`(공용) · `studio_board.py` build(자료를 안 만듦)·sync(단계·트렌드·음성 줄에서 뺌) · `tts_narration.py` v1.19.1 · `kaggle_tts_panel.py` v1.3 · `upload_preview.py` v1.4 · `upload_web.py` v1.10 · `channel_stats.py` v1.1 · `cloud_run.py` v1.7·`next_topic.py` v1.1 (꺼 둔 주제면 시작하지 않음 — `--force` 없음).
- 다시 켜면 다음 동기화·build 부터 자료가 들어옴. 폴더·파일은 지우지 않음.

## 3. 동기화 — 판 db → 저장소 ("제작 판 동기화해")

판에서 바꾼 것은 바로 판 db 에 저장된다. PC·Kaggle·다른 세션은 저장소를 읽으므로 Claude 가 옮긴다:

1. `ArtifactData list` 를 컬렉션마다 `out_dir` = 스크래치 폴더로: `gates · episodes · rules · refs · feedback · tts · trends · skills · uploads · channels · topics`
2. `python3 tools/studio_board.py sync <그 폴더>` → `studio/state/` 에
   - `topics.json` 꺼 둔 주제 (v1.1 — 모든 세션·도구가 읽음)
   - `gates.json` 단계 통과 (편마다 · 판/저장소 기준 표시)
   - `trends.json` 트렌드 검색어 (PC `-TrendsWatch` 가 GitHub 에서 읽음)
   - `tts_queue.json` 음성 생성 줄 (Kaggle `tts_narration.py all` 이 읽음 — 대본 통과 전 체크는 넣지 않음)
   - `reupload.json` 다시 올리기 허용 (PC 업로드 화면이 표시) · `skills.json` Claude 스킬 링크 · `board_db.json` db 전체 사본
   - 규칙 고침·뺌·더함 → `studio/rules.json` 바로 반영 + 로그 `[RULES]` → **같은 세션에서 근거 문서(src)도 고친다** (CLAUDE.md·guides·<주제>/guides)
3. 로그 `[FEEDBACK]` (status=new) 마다 반영 (제목·썸네일 문구 → package.json·업로드 시트 / 대본 줄 → 대본 TXT — 바꿀 때마다 페르소나 반복 검증 `guides/persona_loop.md`) → 판 db 그 문서 `status: "done"`, `reply` 한 줄 (ArtifactData update, if_version)
4. 고정 채널(`channels` status=new) → 분석에 더한 뒤 `done`·`reply` (위기는 독립 분석이라 `crisis/code/crisis_lab.py` 쪽)
5. `git commit` · `git pull --rebase` · `git push` (main) → `build` → 같은 주소로 발행

## 4. 화면별 — 무엇을 어디서

- **공통**: 편마다 지금 단계 표 · 트렌드 검색어(주제별 + 전체 탐색 분류 번호 · 간격) · PC 결과(시간 흐름 표·작은 선 그래프 · 관련 검색어 급상승/인기) · 명령 · 동기화 안 된 건수.
- **1 주제 탐색**: 주제 후보(저장소 편 + 판에서 더한 후보) · 탐색 결과 문서(studio.toml `EXPLORE`) · 페르소나(옛 판) · 고정 채널 넣기 · 대본 받기 명령(심리).
- **2 제목**: 편 제목·다른 안·근거·페르소나 회차 · 피드백 · 성공 사례 제목(심리 `analysis.json` 94 · 위기 `videos.csv` 성공 73 — 판에서 고치기·빼기·더하기 = db `refs`, 분석 원본은 그대로) · 자주 쓰는 낱말(성공 제목 낱말 수 · 성공 비율 높은/낮은 낱말·꼴 · `result/related/*.md`).
- **3 썸네일**: 주요·보조 문구 · 썸네일 3장(작게) · 피드백 · 성공 사례 문구(심리 `thumb_codes.tsv` — 위기는 분류 없음, 판에서 더함).
- **4 대본·음성**: 편 고르기 → 줄마다 [피드백] · 음성 뒤 바뀐 줄 노란 밑줄 · 줄 '재생성' 체크 · '음성 생성'·'전부 다시' · 상태(체크 없음 / Claude 동기화 전 / Kaggle 대기 줄 / 체크대로 만들어짐) · 이미 올린 편은 음성을 다시 만들지 않음.
- **5 영상**: ① 코드 테스트 ② 최종 영상 체크 · 장면 파일·렌더 기록·업로드 조각 · 명령 · 피드백 · Claude 스킬 GitHub 링크(등록·고치기·지우기 — 영상 세션은 `studio/state/skills.json` 을 먼저 읽음).
- **6 업로드**: 최종 종합 확인(제목·썸네일·설명란·태그·설정·자동 점검 + 사람 확인 7칸) → 업로드 승인 · 업로드 기록(youtube.json · youtube_old_* · youtube_history.json) · 다시 올리기 허용.
- **채널 분석**: 우리 채널 6곳 공개 지표 · 최근 영상 표(조회수·하루 조회수·좋아요·댓글) · 판 편과 연결 — `python3 tools/channel_stats.py` (YOUTUBE_API_KEY 세션, 약 3단위/채널). 시청 지속·클릭률은 PC `tools/youtube_feedback.py` (OAuth).

## 5. 판 밖에서 바뀐 도구

| 도구 | 바뀐 것 |
|---|---|
| `tools/pc_trends.py` v1.3 · `run_analyzer.ps1` v3.8 | `-TrendsWatch` = `pc_trends.py watch` — GitHub `studio/state/trends.json` 을 회차마다 읽어 `<주제>/result/next_topic/board_<기간>/batch_NNN_<지문>.csv·json` (전체 탐색 = `new/…`) · 기본 60분 · 같은 기간 결과가 있으면 건너뜀 · `-Once` 한 번 |
| `tools/tts_narration.py` v1.19 · `tools/kaggle_tts_panel.py` v1.2 | `all` = 판 주제(`tts_queue.json` topics)는 체크한 대본만 · 줄 redo = 그 문장만 · full = 처음부터 · 만든 뒤 메타 `queue_stamp` · 판 밖 주제는 예전처럼 · `--all-pending` = 모두 예전처럼 |
| `tools/upload_web.py` v1.9 | '올린 영상'마다 [다시 올리기] (확인 창) — 옛 youtube.json → `youtube_history.json` 맨 앞 · 판 허용 표시 |
| `tools/channel_stats.py` v1.0 | 새로 — 채널 공개 지표 |

## 변경 이력
| 버전 | 날짜 | 바뀐 것 |
|---|---|---|
| v1.1 | 2026-11-27 | 단계마다 그 단계 편만 · 주제 10개 · 주제 켜기·끄기(topics.json) · data URI 그림 · 옛 편 단계 보정 |
| v1.0 | 2026-11-27 | 최초 |
