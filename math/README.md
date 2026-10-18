# 수학 퀴즈 폴더 (`math/`) — 수학 문제를 띄워 두고 시청자가 맞춰 보는 채널, 될까?

VERSION: v1.0 — 2026-10-18 — 새로 만듦 (사용자 지시 2026-10-18: "수학문제 띄워놓고 시청자가 맞춰보는 영상이 조회수 잘 나오고 구독자 많이 모을 수 있는지 탐색해볼래?")

- **같은 잣대(한국어 롱폼)로 다른 27개 분야와 견준 것**은 `new/` 의 '28. 수학 퀴즈' ([`new/result/niche/niche_scan.md`](../new/result/niche/niche_scan.md)).
- 이 폴더는 그 밖의 두 가지를 잰다: ① **쇼츠** (퀴즈는 쇼츠가 많은 형식) ② **세계(영어) 시장** (숫자·식에는 언어가 거의 없음 — 외국 영상 켬, `INCLUDE_FOREIGN = true`).
- 결과 숫자: [`result/niche/niche_scan.md`](result/niche/niche_scan.md) (롱폼) · [`result/niche/niche_scan_shorts.md`](result/niche/niche_scan_shorts.md) (쇼츠). **판단·추천**: [`channel_ideas.md`](channel_ideas.md).
- ※ 연구·교육용.

## 실행 (클라우드)

```bash
python3 tools/niche_scan.py math sync                        # niches.toml → keywords.txt(한국어 6) · keywords_foreign.txt(영어 5) · tag_rules.toml
python3 tools/cloud_run.py math explore --weeks 26           # 롱폼 (검색어 11개 × 2번 = 22번 ≈ 2,200단위)
python3 tools/cloud_run.py math explore --shorts --weeks 26  # 쇼츠 (11번 ≈ 1,100단위)
python3 tools/niche_scan.py math report                      # 롱폼 표 (할당량 0)
python3 tools/niche_scan.py math report --shorts             # 쇼츠 표 (할당량 0)
```

- ⚠️ 키(`YOUTUBE_API_KEY`, 지문 `58333e86`)는 `new/`·`history/` 와 같다 — 하루 검색 횟수(429)를 함께 쓴다. 역사 예약 작업이 매일 한국 16:20 에 돌므로 이 폴더는 그 앞(16:10)이나 뒤에.
- 탐색 캐시 `math/cloud_cache/cache.tgz` (cloud_run 이 저절로 묶고 풂).

## 파일

| 파일 | 내용 |
|---|---|
| [`niches.toml`](niches.toml) | **원본** — 갈래 9개 (한국어 4 · 영어 3 · 기준 재테크·stock market) |
| `keywords.txt` · `keywords_foreign.txt` · `tag_rules.toml` | 만든 파일 (`niche_scan sync`) — 손으로 고치지 않음 |
| `analyzer_config.toml` | 주제 '수학 퀴즈' · 외국 영상 켬 |
| `keywords.toml` | 수학 관련어 ('주제 관련 몫' — 검색어가 수학 영상을 실제로 찾았는지) · `수학여행`·`수학능력` 은 먼저 지움 |
| `analysis_rules.toml` | `new/` 와 같은 기준 (롱폼 180일·5만·×3·1만·4분 / 쇼츠 3~180일·5만·×3·5만회) |
| `result/niche/` | 분야 비교 표·csv (롱폼 · `_shorts`) |

## 첫 탐색 기록 (2026-10-18, 이 클라우드 환경 키)

| 시각 (한국) | 단계 | 결과 | 단위 |
|---|---|---|---|
| 15:29 | `new` explore (새 검색어 '수학 퀴즈'·'계산 퀴즈'만, 나머지 44개는 캐시) | 롱폼 '계산 퀴즈' 결과 6 + 2개뿐 | 412 |
| 15:29 | `math` explore 롱폼 | 검색 19/22 — 3번은 **하루 검색 횟수 한도(429)** (전날 할당량 날의 남은 몫 — 역사 예약 작업과 같은 키) | 1,925 |
| 16:10 | `wait-reset --then resume` → 남은 검색 3번 | 롱폼 목록 651 (라이브 315 뺌) | 305 |
| 16:10 | `math explore --shorts` | 쇼츠 검색 11/11 → 쇼츠 508개 | 1,118 |
| 16:10 | `niche_scan math report` · `report --shorts` · `new report` | 표 3개 | 0 |

자동완성(사람들이 찾는 말 — 이번엔 환경 네트워크가 열려 받음): '수학 퀴즈' → 초등·1학년·3학년·게임·맞추기 · '계산 퀴즈' → 1개뿐 · 'math puzzle' → for adults·for grade 4·with answers · 'mental math' → quiz·tricks·for class 1.

### 한눈에 (숫자 — 자세히는 표, 판단은 `channel_ideas.md`)

| 갈래 | 롱폼 성공 비율 | 롱폼 작은 채널 하루 조회수 | 쇼츠 성공 비율 | 쇼츠 작은 채널 하루 조회수 | 외국 영상 몫 |
|---|---|---|---|---|---|
| 수학·계산 퀴즈 (한국어) | 2% | 10 | 11% | 170 | 35% / 8% |
| 암산 | 1% | 8 | 33% (암산 천재 아이·예능 장면) | 1,574 | 2% / 4% |
| IQ·두뇌 퀴즈 | 3% | 25 | 40% (반은 수학 아님 — 강아지·게임) | 3,866 | 29% / 52% |
| 교양 수학 (설명형) | 0% | 3 | 9% | 87 | 8% / 7% |
| **Math puzzle (영어)** | **43%** ('math puzzle' 26% · 'can you solve this' 55% — 수수께끼 모음) | 3,561 | 20% | 40,574 | 98% / 99% |
| **Math olympiad (영어)** | **39%** | 1,366 | 17% ⚠️ | — (5개) | 91% / 100% |
| **Mental math (영어)** | **28%** | 4,268 | 25% | 49,104 (9개 ⚠️) | 96% / 92% |
| (기준) 재테크 | 3% | ⚠️ 2개 | 34% (대부분 재테크 아닌 예능 장면) | 30,239 | 10% / 0% |
| (기준) stock market (영어) | 5% | ⚠️ 3개 | 10% | ⚠️ 4개 | 100% / 98% |

- 같은 잣대(한국어 롱폼)로 `new/` 28개 분야 중 **'28. 수학 퀴즈' 26위** (성공 3%, 상위 영상 하루 조회수 중앙값 14회).

## 한계
- 갈래마다 검색어 1~2개, 검색마다 조회수 상위 50개 — '가장 많이 본 영상들'만. 시청자 니즈(댓글)는 아직 없음 (승인 안 함).
- '암산' 은 'X암산' 산 이름·드라마도 걸림, 'IQ 테스트' 쇼츠의 반은 수학이 아님(강아지·마인크래프트) — `주제 관련 몫` 칸.
- 쇼츠 조회수는 다시 재생도 셈 (2025-03-31~) — 롱폼과 숫자 크기를 바로 견주지 않는다.

## 다음 할 일
1. 사용자가 `channel_ideas.md` 를 보고 정함 (추천: 한국어 수학 퀴즈 채널은 하지 않음 · 하려면 세계(영어) '수학 두뇌 문제' 채널).
2. 정하면: 영어 검색어를 태그로 넓혀(`tools/tag_keywords.py math --foreign` — `tag_rules.toml [foreign]` 규칙을 먼저) 다시 탐색 → 성공 사례 승인(댓글) → `analysis.md` → 첫 영상 후보.

## 변경 이력
| 버전 | 날짜 | 내용 |
|---|---|---|
| v1.0 | 2026-10-18 | 새로 만듦: 갈래 9개 · 롱폼 검색 22 + 쇼츠 11 (3,348단위 — `new/` 412 포함 3,760) · 분야 비교 롱폼·쇼츠 · 추천 `channel_ideas.md` |
