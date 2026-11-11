# 심리 주제 폴더 (`psychology/`) — 클라우드에서 분석

VERSION: v1.0 — 2026-11-11 — 새로 만듦 (사용자 지시 "가장 최근에 주식 주제에서 했던 것처럼 심리 주제로 분석 코드 돌려서 해당 주제 유튜브 분석에 필요한 자료 받고
페르소나 구성해서 내가 어떤 제목, 썸네일 문구, 보조문구로 영상 만들어야 하는지 하나 알려줘봐" → "계속 진행하고 최근 트렌드도 파악해서 페르소나에 반영해야돼").

- '심리' = 새 채널 분야 탐색 `new/channel_ideas.md` 3순위 **심리·인간관계** (심리학·인간관계·자존감·감정·가족·성격). 주식 투자 심리(`stock/` 심리 테스트 편)와는 따로.
- 주식(`stock/guides/quick_flow.md`)·역사와 같은 길: 탐색 → 승인·분석 → 확인 엑셀 → 페르소나 → 댓글 묶음 → 댓글 니즈 → 콘텐츠 엑셀 → 대본 받을 목록. 이번 회차는 **추천 하나** `source/first_pick.md` 까지 (주제 탐색 20개·요약본·대본은 아직).
- ※ 연구·교육용. 심리 치료·진단이 아니다.

## 클라우드에서 분석 (`tools/cloud_run.py`)

```bash
python3 tools/cloud_run.py psychology status                       # 할당량·탐색 목록·승인 수·남은 것
python3 tools/cloud_run.py psychology explore --weeks 26           # 롱폼 탐색 (검색어 29개 × 4~20분·20분 넘음 = 58번 ≈ 5,000단위 — 첫 회차 실제 5,064)
python3 tools/cloud_run.py psychology explore --shorts --weeks 26  # 쇼츠 탐색 (아직 안 함 — 약 2,900단위)
python3 tools/cloud_run.py psychology list --checked               # 새 추천
python3 tools/cloud_run.py psychology uncheck ID …                 # 주제 밖 추천 풀기 (아래 '첫 회차' 표의 종류)
python3 tools/cloud_run.py psychology approve                      # 추천 승인 → 설명·썸네일·댓글 전부 → 분석 (첫 회차 251개 = 댓글 1,316단위 + 채널 기준선 290단위)
python3 tools/cloud_run.py psychology demand                       # 자동완성 (할당량 0)
python3 tools/cloud_run.py psychology analyze                      # 분석 다시 (할당량 0 — 끝에 personas.md 도 다시)
python3 tools/tag_keywords.py psychology --no-seed-search --write-keywords   # 검색어를 탐색 캐시의 실제 태그로 다시 (할당량 0)
```
- 그다음 (할당량 0): `python3 tools/target_check.py psychology` · `python3 tools/comment_clusters.py psychology` (scikit-learn·kiwipiepy 필요 — `pip install scikit-learn kiwipiepy`) · `python3 tools/comment_title_ideas.py psychology candidates` → Claude 가 `comment_title_picks.tsv` → `match` · `python3 tools/content_analysis.py psychology` (성공 사례 썸네일은 Claude 가 `analysis_thumbs_*.jpg` 를 보고 `thumb_codes.tsv`) · `python3 tools/pc_transcribe.py list psychology`.
- **이 주제는 PC 웹 화면 탭을 켜지 않는다** (CLAUDE.md '분석' — PC 결과가 GitHub `result/outliers/` 를 덮음). 대본은 '대본만 받기'(`run_analyzer.ps1 -Transcribe -Folder psychology`, 목록 `result/outliers/transcript_todo.csv` 251개).
- **네트워크**: 이 클라우드 환경에 `i.ytimg.com`(썸네일)·`suggestqueries.google.com`(자동완성)을 허용함 (2026-11-11 — 첫 승인 때 썸네일 71장이 막혀 다시 받음). 자막(`www.youtube.com`)은 막힘 → 설명으로 대신 (대본 근거로 쓰지 않음).

## 첫 회차 (2026-11-11)

| 단계 | 결과 | 할당량 |
|---|---|---|
| 씨앗 탐색 (심리학·인간관계·심리·자존감 × 26주) | 영상 293 | 812 |
| 태그 고르기 (`--no-seed-search` — 씨앗 365일 검색 800단위 대신 탐색 캐시) | 검색어 28 + 손으로 '나르시시스트' (채널 3곳 · 태그 조회수 합 186만) = **29** | 0 |
| 롱폼 탐색 29개 × 26주 | 영상 2,183 · 추천 434 | 5,064 |
| 추천 훑기 → **푼 것 183** | 음악 플레이리스트·브이로그 18 · 콩트·브이로그·토크 예능 39 · 아이돌·예능·연애 프로 리뷰 25 · TV 상담 예능 클립 20 · 골프·시험·스포츠 멘탈 15 · 종교 법문·간증·타로·음악 15 · 그 밖(책·영화·사회 평론·성인물) 14 · 공부법·뇌과학 일반 14 · 정치·사건·범죄 11 · 육아·아동 6 · 댓글 아주 많은 큰 채널 영상 6 (할당량) | 0 |
| 승인 251 → 분석 | 성공 사례 **174** · 하루 조회수 상위 72 · 비교 집단 1,302 (성공 16%) · 채널 기준선 145곳 · 댓글 51,764 | 1,606 |
| 자동완성 29 · 썸네일 다시 71 | | 0 |
| **합계** | 남은 할당량 2,318 (쇼츠 탐색·③ 기간 없는 검색은 다음 회차) | **7,482** |

- 되풀이되는 주제 밖 낱말은 `keywords.toml` EXCLUDE_KEYWORDS · `analysis_rules.toml` [exclude] OFF_TOPIC 에 더함 (플레이리스트·브이로그·골프·찬송·법문·타로·리센느·하트시그널·나는솔로·환승연애 …).
- 페르소나 감사 (`python3 tools/personas.py psychology audit stage:<키> --n 14` — Claude 가 무작위 댓글을 읽음): 5070 12/14 · 가족 11/13 · 내향인 10/13 · 연애 9/12 · 직장인 9/14 (나이만 맞은 것까지 12/14).
- 한계: 대본 0 (자막 막힘) — 도입·구성·말 속도는 아직 근거 없음 · 댓글 유형 표본(`comment_types.py sample` — 사람이 600개 분류)은 아직 · 쇼츠 분석 없음 · ③ 조회수 상위(기간 없는 검색)는 첫 회차에 끔(`[views_top] TOP_PCT = 0`).

## 파일

| 파일 | 내용 |
|---|---|
| `analyzer_config.toml` | 분석기 설정 v1.0 — 주제 '심리', 한국어 영상만 |
| `keywords.txt` | 탐색 검색어 29개 (태그 28 + 손으로 1) |
| `keywords.toml` | 관련어 v1.0 — 강한·약한 관련어 · 지우는 표현(투자 심리·소비 심리·심리전·범죄 심리 …) · 탐색 목록 빼는 말 |
| `tag_rules.toml` | 태그 → 검색어 규칙 v1.0 (주제 낱말 필수 · 사람·방송 이름·명상·명언·손절(주식 말)·MBTI·마음챙김 뺌) |
| `analysis_rules.toml` | 분석 기준 v1.0 — 주식·역사와 같은 세 묶음 · 형식 5개(수면·낭독 / 인터뷰·강연 / 사연·고민 상담 / 심리 테스트 / 브이로그) · OFF_TOPIC |
| `personas.toml` | 페르소나 설정 v1.0 — 묶음 7 · 처지 12 · 용어 · **TREND_DAYS = 28** (최근 흐름, `tools/personas.py` v1.1) |
| `result/outliers/` | 사례 폴더 `W_*` 251 · `analysis.md` · `weekly.md` · `personas.md`(5명 + 2-1 최근 흐름) · `target_check.xlsx` · `comment_clusters.md`·`.xlsx` · `comment_titles.md`(K01~K29) · `content_analysis.md`·`.xlsx` · `thumb_codes.tsv` · `transcript_todo.csv` |
| [`source/first_pick.md`](source/first_pick.md) | **추천 하나** — 제목·썸네일 주요 문구·보조 문구·그림 + 근거 |
| `cloud_cache/` | 탐색 캐시 묶음 (새 컨테이너에서 저절로 풂) |

## 다음 할 일

1. 사용자: 추천(`source/first_pick.md`) 좋음·나쁨 · 채널 설명(`<주제>/guides/channel.md` — 아직 없음).
2. 할당량이 초기화되면 쇼츠 탐색 → 쇼츠 승인 → 분석 · ③ `[views_top] TOP_PCT = 10` → `explore --alltime-only`.
3. PC '대본만 받기' → 대본이 오면 `analyze` · `content_analysis` 다시 (도입·구성 근거).
4. 주식처럼 주제 탐색 20개 → 요약본 (`stock/topics/README.md` 꼴).
