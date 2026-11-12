# 심리 주제 폴더 (`psychology/`) — 클라우드에서 분석

VERSION: v1.0 — 2026-11-11 — 새로 만듦 (사용자 지시 2026-11-11 "가장 최근에 주식 주제에서 했던 것처럼 심리 주제로 분석 코드 돌려서 해당 주제 유튜브 분석에 필요한 자료 받고 페르소나 구성해서 내가 어떤 제목, 썸네일 문구, 보조문구로 영상 만들어야 하는지 하나 알려줘봐 그리고 최근 트렌드도 반영해야 돼").

- 새 채널 분야 탐색 `new/niches.toml` 의 **'07. 심리·인간관계'**(new/ 결과 성공 비율 32%)를 그 분야만의 폴더로 분석한다. 방법은 주식·역사와 같다 (`stock/guides/quick_flow.md` 1~8단계 — 주제 이름만 `psychology`).
- 결과 숫자: `result/outliers/analysis.md` (숫자·원문만). 제목·썸네일 추천(판단)은 `source/first_video.md`.
- ※ 연구·교육용 분석 — 의료·심리 상담이 아니다. 정신건강 정보는 대본 전에 연구·공공기관 자료로 확인한다.

## 클라우드에서 분석 (`tools/cloud_run.py`)

```bash
python3 tools/cloud_run.py psychology status                       # 할당량·탐색 목록·승인 수·남은 것
python3 tools/cloud_run.py psychology resume                       # 할당량·하루 검색 횟수 때문에 남은 탐색·댓글·채널 기준선
python3 tools/cloud_run.py psychology explore --weeks 26           # 롱폼 탐색 (검색어 28개 × 4~20분·20분 넘음 = 56번 ≈ 5,600단위)
python3 tools/cloud_run.py psychology explore --shorts --weeks 26  # 쇼츠 탐색 (롱폼 탐색이 끝난 뒤 — 28번 ≈ 2,800단위)
python3 tools/cloud_run.py psychology list --checked               # 새 추천
python3 tools/cloud_run.py psychology uncheck ID …                 # 심리가 아닌 추천 풀기 (투자 심리·타로·노래 등)
python3 tools/cloud_run.py psychology approve                      # 추천 승인 → 설명·자막·썸네일·댓글 → 분석
python3 tools/cloud_run.py psychology analyze                      # 롱폼·쇼츠 분석 다시 (할당량 0)
python3 tools/tag_keywords.py psychology --write-keywords          # 검색어를 실제 영상 태그로 다시 고르기 (씨앗 검색 — 할당량)
```

- **키**: 환경 변수 `YOUTUBE_API_KEY` — `history/`·`new/` 와 같은 키라 같은 날 하루 10,000단위·하루 검색 횟수를 함께 쓴다.
- **캐시**: `psychology/cloud_cache/` (명령 뒤 저절로 묶음 — 새 컨테이너에서도 이어서).
- ⚠️ PC 웹 화면에서 심리 탭을 켜지 않는다 (PC 결과로 GitHub 의 `result/outliers/` 를 덮음). 대본은 '대본만 받기' (`tools/pc_transcribe.py list psychology` → PC `run_analyzer.ps1 -Transcribe -Folder psychology`).
- 예약 작업은 만들지 않음 (2026-10-24 사용자 지시 — 분석은 시킬 때).

## 파일

| 파일 | 내용 |
|---|---|
| `analyzer_config.toml` | 분석기 설정 v1.0 — 주제 이름 '심리', 외국 영상 꺼짐 |
| `keywords.txt` | 탐색 검색어 — `tools/tag_keywords.py` 가 실제 영상 태그에서 고름 |
| `tag_rules.toml` | 태그 → 검색어 규칙 v1.0 — 씨앗 4개(심리학·인간관계·자존감·심리) · 빼는 말(투자 심리·타로·사주·종교 설교·음악) · 주제 낱말 필수 |
| `tag_candidates.md`·`.csv` | 태그 표 (채널 수 순, 왜 뺐는지) |
| `keywords.toml` | 관련어 v1.0 — 강한·약한 관련어 · 지우는 표현('투자 심리'·'매수 심리'·'심리적 지지선'·타로·사주) |
| `analysis_rules.toml` | 분석 기준 v1.0 — 주식·재테크·역사와 같은 세 묶음 · 심리 형식 7개 · 점술 빼기 |
| `personas.toml` | 시청자 페르소나 설정 v1.0 → `result/outliers/personas.md` (분석 끝에 저절로) |
| `result/outliers/` | 승인한 영상 자료(`W_<영상ID>/`) · `analysis.md` · `personas.md` · `comment_titles.md` · `comment_clusters.md` · `content_analysis.md` |
| `source/first_video.md` | **첫 영상 제목·썸네일 문구·보조 문구 추천 (판단)** |
| `cloud_cache/` | 탐색 캐시 묶음 |

## 회차 기록

| 때 | 한 일 | 할당량 | 결과 |
|---|---|---|---|
| 2026-11-11 18:22~22:48 KST (사용자 지시 — 첫 회차) | 설정 · 씨앗 검색 · 태그 검색어 28개 · 롱폼 탐색 26주 · 추천 훑기(193개 풂) · 승인 317 · 분석 · 페르소나 감사·고침(v1.1) · 댓글 묶음 · 댓글 니즈 C01~C26 · 확인·콘텐츠 엑셀 · 대본 받을 목록 | 씨앗 812 + 탐색 7,886 (기간 없는 검색 22번 포함) + 승인 1,914 = 하루 몫 다 씀 | 탐색 2,722 · 성공 사례 **135** · 하루 조회수 상위 77 · 조회수 상위 77 · 비교 집단 757 (성공 32%) · 페르소나 5명 (5060 · 부모·가족 상처 · 배우자·시댁 · 학생·청년 · 우울·불안) · 첫 영상 추천 `source/first_video.md` |

## 다음 할 일
1. 할당량이 초기화되면 (한국 17시) `resume` — 댓글 덜 받은 134개 · 같은 채널 기준선 → `analyze`.
2. 쇼츠 탐색 `explore --shorts --weeks 26` (28번 ≈ 2,800단위) → 추천 훑기 → 승인.
3. 사용자 PC 대본만 받기 (`transcript_todo.md` 317개) → `analyze` 다시.
4. 성공 사례 썸네일 분류 `thumb_codes.tsv` → `content_analysis.py psychology`.

## 한계
- 대본 0개 (자막 서버 막힘 · 음성인식은 PC) — 제목·썸네일·댓글로만.
- 쇼츠는 아직 탐색 전 · 같은 채널 기준선 없음 (할당량).
- 페르소나 감사(v1.0 규칙, Claude 가 무작위 댓글을 읽음): 5060 12/14 · 부모·가족 상처 7/9 · 직장 7/9 · 배우자·시댁 5/9 · 학생·청년 5/9 · 우울·불안 5/9 — 뒤 셋은 대강의 크기로만.
