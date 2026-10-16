# 역사 (`history/`) — 클라우드에서 매일 이어서 분석

VERSION: v1.0 — 2026-10-16 — 새로 만듦 (사용자 지시 2026-10-16: "이 환경은 이제 저장소에 있는 역사 주제 (history경로 없으면 만들것)를 유튜브 분석 코드 실행해서 분석하는 환경이야 사용량 초기화 될때마다 분석을 계속 이어서하면 돼 캐시를 저장소에 남겨서 분석 이어서 할 수 있게 하고")

- 고른 까닭: [`new/channel_ideas.md`](../new/channel_ideas.md) 1순위 '역사 해설' — 분야 27개 비교에서 성공 비율 41% (작은 채널이 조회수 상위에 끼는 몫, 재테크·주식 2%) · 2년 안 구독자 1만 채널 37% · 성공 영상 길이 19분 ([`new/result/niche/niche_scan.md`](../new/result/niche/niche_scan.md)).
- 이 폴더는 그 분야**만**을 태그 검색어 40개로 다시 재고, 성공 사례의 설명·댓글까지 받아 `result/outliers/analysis.md`(숫자·원문만)를 만든다 (`guides/pipeline.md` 1단계). 지시사항(`history/guides/data_insights.md`)·주제는 그 결과가 나온 뒤.
- `new/` 의 캐시·결과는 빌려 쓰지 않는다 (CLAUDE.md '주제 캐시·설정은 주제마다 따로' — 비교 집단이 다른 분야 영상으로 섞임). 규칙을 다듬을 때 `new/` 자료를 **읽기만** 했다 (아래 '규칙을 정한 근거').
- ※ 연구·교육용 분석.

## 실행 (클라우드 — 이 환경)

```bash
python3 tools/cloud_run.py history status                    # 할당량·탐색 목록·승인 수·남은 것 (할당량 0)
python3 tools/tag_keywords.py history --write-keywords        # 태그 씨앗 검색 8개(≈1,600단위) → 검색어 40개 keywords.txt (처음 한 번 · 검색은 7일 캐시)
python3 tools/cloud_run.py history resume                    # 할당량 때문에 남은 탐색 검색·댓글·채널 기준선
python3 tools/cloud_run.py history explore --weeks 26        # 롱폼 탐색 (검색어 40개 × 4~20분·20분 넘음 = 검색 80번 ≈ 8,000단위)
python3 tools/cloud_run.py history list --checked            # 도구 추천(체크) — 역사가 아닌 것은 uncheck <ID>
python3 tools/cloud_run.py history approve                   # 승인 → 설명·자막·댓글 전부 · 주별 분석 · 성공 사례 분석
python3 tools/cloud_run.py history analyze                   # analysis.md 다시 (할당량 0)
python3 tools/cloud_run.py history explore --shorts --weeks 26   # 쇼츠 (롱폼 탐색이 다 끝난 뒤 — 검색 40번 ≈ 4,000단위)
```

- 웹 화면(`tools/web_ui.py`)의 작업 함수를 그대로 부르므로 분석·추천(체크)·할당량 계산은 PC 와 같다 (`stock/README.md` '클라우드에서 분석').
- **매일 이어서**: 예약 작업 '역사 분석 이어서 (할당량 초기화 뒤 매일)' `trig_01TEbPHqXpzYY3hj6LhyBb7q` — 태평양 자정 +20분(한국 16:20, 서머타임 끝나면 2026-11-01 부터 17:20)에 이 클라우드 세션(`session_01Nd9n754WdtaqPq45t3uPSZ`)을 깨워 위 순서로 돌리고 main 에 올린다 (`guides/status.md` 2-5).
- **캐시**: `history/cloud_cache/cache.tgz` (+ 목록 `cache.json`) = `result/outliers/.cache`(검색·영상 정보·채널 업로드 목록·쇼츠) + `result/web`(탐색 목록·체크·승인 목록). `cloud_run.py` 가 명령 뒤 저절로 묶고, 새 컨테이너에서 저절로 푼다. ⚠️ `tag_keywords.py` 는 혼자 묶지 않으므로 그 뒤 `cloud_run.py history cache-save`.
- ⚠️ **PC 웹 화면에서 역사 탭을 켜지 않는다** — PC 가 자기 `history/result/outliers/` 로 GitHub 것을 통째로 바꿔 클라우드가 받은 사례 폴더(`W_…`)가 지워짐 (`guides/pc_analysis.md` '클라우드에서 돌리기'). 그래서 음성인식(PC 만)은 하지 않는다.
- 키: 환경 변수 `YOUTUBE_API_KEY` (지문 `58333e86…` — `new/` 탐색과 같은 키, 하루 할당량을 함께 씀). 역사만 다른 키를 쓰려면 환경 변수 `YOUTUBE_API_KEY_HISTORY` (`outlier_research.load_api_key` 가 먼저 읽음).

## 이 환경 네트워크 (2026-10-16 확인)

| 받는 것 | 곳 | 이 환경 |
|---|---|---|
| 검색·영상 정보·구독자·댓글 (YouTube Data API) | `www.googleapis.com` | 됨 |
| 자막 | `www.youtube.com` | **막힘** (프록시 403) → 영상 설명으로 대신 (글 출처 '설명' — 대본 근거로 쓰지 않음) |
| 썸네일 이미지 | `i.ytimg.com` | **막힘** → analysis.md '썸네일 한 장'이 비어 있음 |
| 자동완성 (수요) | `suggestqueries.google.com` | **막힘** → '수요와 공급'의 자동완성 말이 없음 |

사용자가 클라우드 환경 설정 → Network access 에 세 곳을 더하면 받는다 (재테크·주식 환경은 2026-10-16 더함).

## 파일

| 파일 | 내용 |
|---|---|
| `analyzer_config.toml` | 분석기 설정 v1.0 — 주제 이름 '역사', 외국 영상 꺼짐(한국어 시장부터) |
| `keywords.txt` | 검색어 — **태그로 고름** (`tag_keywords.py --write-keywords` 가 다시 씀, 손으로 고쳐도 됨) |
| `keywords.toml` | 관련어 v1.0 — 강한 59 · 약한 45 · 지우는 말 13 ('흑역사'·'역사적 신고가'·'조선업'·'고대하던' 등) |
| `tag_rules.toml` | 태그 → 검색어 규칙 v1.0 — 씨앗 8 · 빼는 말 · 역사 낱말 필수(TAG_REQUIRE) · 묶음 12개(TAG_THEMES — 분석의 '주제별 성공 비율'도 이 묶음) |
| `analysis_rules.toml` | 분석 기준 v1.0 — 성공 기준은 CLAUDE.md 그대로(180일·구독자 5만 이하·×3·1만·4분), 형식 5가지(잠잘 때 듣는·몰아보기·강의·야담·애니메이션), 빼는 것 = 도박·시험 강의·게임 |
| `cloud_cache/` | 탐색 캐시 묶음 |
| `result/outliers/` | 결과 — `analysis.md`(숫자·원문만) · `weekly.md` · `approved.md` · `downloads.md` · 사례 폴더 `W_<영상ID>/` |

## 규칙을 정한 근거 (2026-10-16, 할당량 0)

`new/` 탐색 캐시(영상 4,037개)를 스크래치 폴더에 풀어 **읽기만** 해서 시험했다 (이 폴더 캐시에는 넣지 않음):
- 관련어: `new/` 의 '03. 역사' 표본 139개 중 **136개**가 역사 관련으로 잡힘 (놓친 3개는 '오디세이(아)' 원작 이야기 — 신화). 다른 분야 표본 2,388개 중 106개(4%)가 역사 관련으로 잡힘 — 대부분 조선 배경 야담·사극 오디오 드라마(`#조선시대 #사극`).
- 태그: 같은 규칙으로 미리 골라 보니 역사·세계사·역사이야기·한국사·조선시대·역사다큐·조선왕조실록… → '조선야담'(지어낸 이야기 낭독 — `new/channel_ideas.md` 에서 따로 보류한 분야)과 '벌거벗은세계사 …'(방송 프로그램 이름 태그 — 그 방송 클립만 모임)는 빼는 말에 더함, '전쟁' 혼자는 지금 전쟁 소식이 위를 덮어 필수 낱말에서 뺌.
- ⚖️ 판단: 야담은 **검색어로 고르지 않을 뿐** 빼지 않는다 — '조선시대' 같은 검색에 섞여 오면 analysis.md 형식 '야담·설화'로 따로 보인다.

## 기록

### 2026-10-16 (첫날 — 설정만)

| 단계 | 결과 | 단위 |
|---|---|---|
| 설정 파일 5개 · `topics.txt` 에 더함 | 위 '파일' | 0 |
| `tag_keywords.py history` (씨앗 검색) | **못 함** — 이 키가 오늘 Google 의 '하루 검색 횟수' 한도(HTTP 429 `Search Queries per day`)에 이미 걸림 (같은 키로 `new/` 탐색이 18:21~18:27 에 검색 88번). 검색 16번은 초기화 뒤로 | 0 |
| 예약 작업 `trig_01TEbPHqXpzYY3hj6LhyBb7q` | 매일 태평양 00:20 (cron `CRON_TZ=America/Los_Angeles 20 0 * * *`) — 첫 회차 2026-10-17 16:20 한국. 재테크(00:15)·주식(00:15 한 번) 예약과 main 푸시가 겹치지 않게 5분 늦춤 | — |

## 다음 할 일

1. (예약 작업, 10-17 16:20 한국) 씨앗 검색 → `keywords.txt` 40개 → `explore --weeks 26` → 추천 확인(역사가 아닌 것 uncheck) → `approve` → `analyze` → main. 하루 할당량으로 다 못 하면 다음 날 이어서 (검색 96번 — 하루 검색 횟수 한도가 90번 언저리일 수 있음, 주식 2026-10-16 91번째에 429).
2. 롱폼 탐색이 다 끝난 날부터 쇼츠 탐색·승인 (`guides/shorts_guide.md`).
3. 결과가 모이면 `history/guides/data_insights.md` (지시사항 재료 — 0번 '한계'를 먼저: 이 환경은 자막·썸네일·자동완성이 막혀 있어 성공 사례 대부분이 글 출처 '설명').
4. (사용자 선택) 전 세계 대상으로 할지 — 그러면 `cloud_run.py history foreign on` + 영어 씨앗(`tag_rules.toml` `[foreign]`) → `keywords_foreign.txt`.

## 변경 이력
| 버전 | 날짜 | 내용 |
|---|---|---|
| v1.0 | 2026-10-16 | 새로 만듦: 설정 5개 · 규칙 근거(new/ 자료 읽기만) · 첫날 씨앗 검색은 하루 검색 횟수 한도로 못 함 · 매일 예약 작업 |
