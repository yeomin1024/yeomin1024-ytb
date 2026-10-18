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

## 첫 탐색 기록 (2026-10-18)

(아래 숫자는 쇼츠 탐색 뒤 채움)

## 변경 이력
| 버전 | 날짜 | 내용 |
|---|---|---|
| v1.0 | 2026-10-18 | 새로 만듦 |
