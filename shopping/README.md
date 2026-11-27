# 쇼핑 주제 폴더 (`shopping/`) — 쿠팡 파트너스 · 4050 여성 살림·생활 추천 — 클라우드에서 분석

VERSION: v1.1 — 2026-11-27 — 첫 편 대본 `source/nanbang-mulgeon-2026-11-27/` v1.4 (난방 물건 순이득 · 계산 v1.6 · 페르소나 5회차에서 멈춤) · 다음 주제 탐색 `next_topic.toml`
(v1.0 — 2026-11-27 — 새로 만듦 (사용자 지시 2026-11-27 "쿠팡파트너스 상품 홍보 목적 유튜브 채널 만들건데 어떻게 해야 될까?" → "소비가 많은 여성 나이대 타겟으로 할거야 계속 진행해")

- **채널 방향·법·정책 = `guides/channel.md`** (⚠️ v0.1 임시 — 타깃 40~50대 여성 근거 · 돈이 들어오는 길 3가지 · 광고 표시·AI 가상인물·기만 광고·스팸 정책 · 사용자 결정 2개)
- 결과 숫자: `result/outliers/analysis.md` (숫자·원문만). 판단은 `guides/channel.md`.
- 방법은 심리·역사와 같다 (`stock/guides/quick_flow.md` 1~8단계 — 주제 이름만 `shopping`).
- ※ 연구·교육용 분석 — 구매 권유가 아니다. 법·정책 줄은 첫 업로드 전에 공정위·유튜브 원문으로 확인.

## 클라우드에서 분석 (`tools/cloud_run.py`)

```bash
python3 tools/cloud_run.py shopping status                       # 할당량·탐색 목록·승인 수·남은 것
python3 tools/cloud_run.py shopping resume                       # 할당량·하루 검색 횟수 때문에 남은 탐색·댓글·채널 기준선
python3 tools/cloud_run.py shopping explore --weeks 26           # 롱폼 탐색 (검색어 30개 × 4~20분·20분 넘음 = 60번 ≈ 6,000단위)
python3 tools/cloud_run.py shopping explore --shorts --weeks 26  # 쇼츠 탐색 (30번 ≈ 3,000단위)
python3 tools/cloud_run.py shopping list --checked               # 새 추천
python3 tools/cloud_run.py shopping uncheck ID …                 # 주제·타깃 밖 추천 풀기 (남성·20대·아이돌·사연·테크 리뷰어)
python3 tools/cloud_run.py shopping approve                      # 추천 승인 → 설명·썸네일·댓글 → 분석
python3 tools/cloud_run.py shopping analyze                      # 롱폼·쇼츠 분석 다시 (할당량 0)
python3 tools/tag_keywords.py shopping --write-keywords          # 검색어를 실제 영상 태그로 다시 고르기 (씨앗 4개 = 800단위)
```

- **키**: 환경 변수 `YOUTUBE_API_KEY` — 이 세션은 '음악 유튜브 주제 탐색' 환경 키 (음악 분석과 하루 10,000단위를 함께 씀).
- **캐시**: `shopping/cloud_cache/` (명령 뒤 저절로 묶음 — 새 컨테이너에서도 이어서).
- **대본**: 클라우드에서는 자막 서버가 로봇 확인(google.com/sorry)으로 막음 → PC '대본만 받기' (`python3 tools/pc_transcribe.py list shopping` → PC `run_analyzer.ps1 -Transcribe -Folder shopping`).
- ⚠️ PC 웹 화면에서 쇼핑 탭을 켜지 않는다 (PC 결과로 GitHub 의 `result/outliers/` 를 덮음).
- 예약 작업은 만들지 않음 (2026-10-24 사용자 지시 — 분석은 시킬 때).

## 파일

| 파일 | 내용 |
|---|---|
| `guides/channel.md` | 채널 방향 v0.2 (임시) — 타깃 근거 · 수익 길 · 반드시 지킬 것 7가지 · 제작 방식 결정(A 실사 / B 정보 비교) · 첫 탐색 미리 보기 |
| `analyzer_config.toml` | 분석기 설정 v1.0 — 주제 이름 '쿠팡 추천템 (4050 여성)', 외국 영상 꺼짐 |
| `keywords.txt` | 탐색 검색어 30개 — 실제 태그 (넓은 태그 4개는 타깃 태그로 바꿈 — 파일 머리 줄) |
| `tag_rules.toml` | 태그 → 검색어 규칙 v1.0 — 씨앗 4개(쿠팡 추천템·살림템·40대 화장품·4050 패션) · 빼는 말(남성·20대·육아·자취·캠핑·투자·사연) |
| `tag_candidates.md`·`.csv` | 태그 표 (채널 수 순, 왜 뺐는지) |
| `keywords.toml` | 관련어 v1.0 — 강한(추천템·꿀템·살림템·내돈내산·하울·4050 패션…)·약한 관련어 · 지우는 표현(영화 리뷰·종목 추천·시니어사연) |
| `analysis_rules.toml` | 분석 기준 v1.0 — 세 묶음 · **성공 조회수 10만** (관련 롱폼 가운데값 125,310) · 쇼핑 형식 7개 · 타깃 밖 빼기 |
| `personas.toml` | 시청자 페르소나 설정 v1.0 → `result/outliers/personas.md` (분석 끝에 저절로) — 주부·워킹맘·5060·4050 외모 고민·1인 가구(타깃 밖 확인) |
| `result/web/explore.json` | 탐색 목록 (2,060개) |
| `result/outliers/` | 승인한 영상 자료(`W_<영상ID>/`) · `analysis.md` · `personas.md` … |
| `guides/item_select.md` | **쿠팡 물건 고르기 v0.1** — 순서 7단계 · 자동화 되는 것/안 되는 것 · 첫 후보 |
| `source/item_scan.py` | **물건 후보 찾기 v0.1.1** (할당량 0) — 물건 사전 83개 × 최근 하루 조회수·살 마음 댓글 영상 수·성공 사례 → `result/items/item_scan.md`·`.csv` · 시험 `--selftest` |
| `source/winter_tips.py` | **겨울 꿀팁 쇼츠 시장 v1.0.0** — 갈래 20개 × 쇼츠 검색 1번(최근 365일) → `result/next_topic/winter_tips.md` (숫자) · 판단 `result/next_topic/winter_topics.md` (후보 8개) · 시험 `--selftest` |
| `next_topic.toml` | 다음 주제 탐색 네 단계 설정 (`guides/topic_guide.md` 1-0) — 생활 문제 18묶음 · 겹침 후보 3 → `result/next_topic/` |
| `source/nanbang-mulgeon-2026-11-27/` | **첫 편 '난방비 아끼려고 산 물건, 한 달에 얼마 남나'** — 대본 v1.4 · `calc/heating_calc.py` v1.6 · `대본_근거.md` · 페르소나 기록 `persona_loop.json` (5회차 — 사용자 판단 대기) |
| `excluded_videos.md` | 주제 밖이라 뺀 승인 영상 3개 (연예 소식·골프 여행·반찬 레시피) |
| `result/outliers/transcript_todo.md` | PC '대본만 받기' 목록 (316편) |
| `cloud_cache/` | 탐색 캐시 묶음 |
| `CHANGELOG.md` | 바꾼 것 |

## 회차 기록

| 때 | 한 일 | 할당량 | 결과 |
|---|---|---|---|
| 2026-11-27 1회차 | 태그 씨앗 4개 → 검색어 30개 · 롱폼 탐색 26주 · 추천 390 → 주제·타깃 밖 74개 풂(조회수 10만 아래 46 · 남성·아이돌·20대 뷰티·사연·테크·자취 28) → 승인 316 (대본 0 — 클라우드 자막 막힘 · 설명 304) → 주제 밖 3개 더 뺌 | 씨앗 812 + 탐색 7,867 + 승인 1,933 = 하루 9,800 다 씀 (채널 기준선 96곳·댓글 80개·기간 없는 검색 42 는 17:10 KST 뒤 `resume`) | **성공 사례 97** · 비교 집단 501 (27%) · 다이소·가성비 36%·지수 1.7 · 비교 40%·경고형 39% · 페르소나 2명 (5060 46% · 4050 외모 23%) · 밝힌 나이 40대 26%·50대 22%·60대 22% — 판단 `guides/channel.md` v0.2 5번 |
