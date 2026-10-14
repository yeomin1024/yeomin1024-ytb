# 재테크 주제 폴더 (`economic/`) — 새로 시작 (2026-10-13)

공통 지시사항은 저장소 최상위 `guides/`에 있고, 이 폴더에는 **경제·재테크에만 해당하는 것**만 둔다.
※ 연구·교육용이다. 투자 권유가 아니다.

2026-10-13 사용자 지시로 다른 주제 폴더(stock·stock_backup·health·lifetips·selfdev·space·story)를 모두 지우고 이 폴더 하나만 만들었다:
"기존 stock, health 등 모든 주제 폴더 전부 삭제하고 경제, 재태크(economic) 폴더만 하나 만들고 코드 분석기에서 사용한 검색어 목록 같은거는 따로 빼놓고
분석기 코드 pc에서 돌릴 수 있도록 수정하고 방법 알려주고 api 할당량이 초기화된 시간이 되면 다시 자동으로 분석결과를 확인 못한 부분부터 새로 추가로 만들도록 수정해"

- 지운 폴더의 내용(옛 분석 결과·주제 규칙·대본·업로드 기록 `youtube.json`)은 git 기록에 있다: 커밋 `2a68307` (예: `git show 2a68307:stock/guides/script_rules.md`).
- 이 주제의 지시사항(`guides/`)은 **이 주제의 성공 사례 분석 결과가 나온 뒤** 만든다 (`guides/pipeline.md` 2단계 — 다른 주제 결과를 빌려 쓰지 않음).

| 위치 | 내용 |
|---|---|
| `analyzer_config.toml` | 분석기 설정 v1.1: 주제 이름 **재테크**(경제는 뺌)·저장 폴더·검색 지역·광고 의심 영상 거르기·할당량 `QUOTA_BUDGET = 6000`·**영상 파일 안 받음**(`DOWNLOAD_VIDEOS = false`) |
| **`keywords.txt`** | **검색어 목록** — 한 줄에 하나, 그룹 없음, `#` 줄은 메모 (사용자 지시 2026-10-13 "꼭 그룹을 지정해야하나 검색어만 넣어도 되잖아"). 지금 36개 = 태그 40개(`tag_candidates.md`)에서 사용자가 부동산·코인을 지운 것. **GitHub 에서 고치면 PC 가 다음 회차에 자동으로 받아 씀** (VERSION 불필요) |
| `keywords.toml` | v3.0: 주제 관련어 45개 · 약한 관련어 · 제외어 (주제 관련 영상 판단). `[KEYWORD_GROUPS]` 는 비움 (`keywords.txt`가 없을 때만 씀) |
| `tag_rules.toml` | 태그 → 검색어 규칙 v1.1 (`tools/tag_keywords.py`가 읽음 — `--write-keywords` 는 `keywords.txt` 를 씀): 씨앗 검색어(재테크·재테크 방법·재테크 초보·돈 모으는 방법) · 채널 5곳 이상 · 40개 · **빼는 말**(경제·뉴스·금리·환율·경기·물가·종목·정치·쇼츠 등, **사용자가 지운 부동산·코인** — 예외 경제적자유·직장인 재테크) · 묶음 10개 |
| [`tag_candidates.md`](tag_candidates.md) | **고른 태그 표** (GitHub 에서 바로 보임): 태그마다 채널 수·영상 수·묶음·검색어로 썼는지(안 쓴 까닭) — `.csv` 도 |
| `.env` | (PC에만, git 제외) 이 주제만 쓰는 키 — 보통 비워 둠(맨 위 `.env` 키). 다른 주제와 동시에 돌리면 같은 키의 하루 할당량을 나눠 씀 (`guides/pc_analysis.md` "여러 주제를 동시에") |
| `result/` | (분석 뒤) 분석기 결과 — PC 실행이 GitHub에 올림. 직접 고치지 않음 |
| `result/outliers/` | (분석 뒤) 작은 채널 성공 사례 20개 + **구독자 수 상관없이 조회수 상위 20개**: `summary.md`(사례마다 첫 1분 발췌·90초마다 흐름·인기 댓글) · `outliers.csv` · `popular.csv` · `candidates.csv` · `status.json`(남은 일) + 사례 폴더 `01_…`·`P01_…` (자막·**댓글 전부**·썸네일 — 저장소가 비공개일 때만 GitHub 에) |
| `targets.json` | (PC 웹 화면) 직접 추가한 영상·채널 — 채널은 올라온 영상 전부를 탐색 |
| `result/outliers/W_<영상ID>/` | (웹 화면) **승인한 영상**의 설명·자막·썸네일·댓글 전부 (저장소가 비공개일 때만 GitHub 에) |
| `result/outliers/weekly.md` | (웹 화면) **주별 분석** — 최근 1주·2주·3주… 한 주씩 넓힌 창 (`weekly.json`·`weekly.csv`) |
| `result/outliers/downloads.md` | **받은 자료 표** (GitHub 에서 바로 보임): 탐색한 검색어(태그)별 결과, 자료로 받은 영상마다 **업로드 날짜**·자막(자막/음성인식/대기)·댓글(받은 수/영상 표시)·썸네일·설명·태그·챕터, 분석기 성공사례 |
| `result/pc_progress.json` | (분석 뒤) PC 실행 진행 상태: 회차·끝났는지·남은 일·다음 회차 시각 |
| `guides/` | (분석 뒤) 주제 규칙 `data_insights.md`·`script_rules.md`·`title_rules.md`·`thumbnail_rules.md`·`upload_rules.md` |
| `source/<영상ID>/` | (주제를 고른 뒤) 영상별 대본·자막·제목·썸네일 프롬프트·업로드 시트·요약 |

## 다음 할 일
1. **분석 (사용자, 집 PC):** [`guides/pc_analysis.md`](../guides/pc_analysis.md) — `run_analyzer.ps1` 한 번 실행. 할당량이 모자라면 다음 날(한국 오후 4~5시 초기화 뒤) 자동으로 이어서 돈다. 자막·썸네일은 PC에서만 받힌다.
2. 분석이 끝나면(GitHub `economic/result/pc_progress.json`의 `complete: true`) Claude에게: "economic 분석 끝났어, 결과로 지시사항이랑 주제 만들어줘" → `guides/pipeline.md` 2단계부터.
