# 주식 주제 폴더 (`stock/`) — 새로 시작 (2026-10-15)

VERSION: v1.0 — 2026-10-15 — 최초 (사용자 지시: "주식 주제로 유튜브 분석기 돌리기위한 세팅 좀 해줘 stock 폴더 만들고 검색어 설정 같은거 말이야 그리고 내가 어떻게 실행해야하는지도 명령 알려줘")

공통 지시사항은 저장소 최상위 `guides/`에 있고, 이 폴더에는 **주식에만 해당하는 것**만 둔다.
※ 연구·교육용이다. 투자 권유가 아니다.

- 예전 `stock/` 폴더(사연형 주식 영상)는 2026-10-13 사용자 지시로 지웠다 — 내용은 커밋 `2a68307`. 이 폴더는 **그것과 따로 새로 시작**한다 (옛 결과·규칙을 빌려 쓰지 않음).
- `economic/`(재테크)와 **검색어가 일부 겹친다** (ETF·ISA·연금저축 등). 주제마다 결과·지시사항은 따로 만든다 — 한 주제 결과를 다른 주제 규칙으로 쓰지 않는다 (`guides/pipeline.md` 1단계 4번).
- 이 주제의 지시사항(`guides/`)·대본 규칙(`research_rules.toml`)은 **이 주제의 성공 사례 분석 결과가 나온 뒤** 만든다.

## 실행 (집 PC — PowerShell)

```powershell
# 처음 한 번 (또는 실행기가 바뀌었을 때) — 실행기 받기
curl.exe -L -o run_analyzer.ps1 https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/main/run_analyzer.ps1

# 주식만 (웹 화면 — 브라우저가 http://127.0.0.1:8765/ 로 열림)
powershell -ExecutionPolicy Bypass -File run_analyzer.ps1 -Folder stock

# 재테크·주식 둘 다 (주제마다 창 하나씩, 할당량은 같은 키에서 함께 셈)
powershell -ExecutionPolicy Bypass -File run_analyzer.ps1 -Folder economic,stock
```

- 실행기가 켤 때마다 최신 코드와 이 폴더의 설정(`analyzer_config.toml`·`keywords.toml`·`keywords.txt`·`tag_rules.toml`·`analysis_rules.toml`)을 받는다. 키는 PC 의 맨 위 `.env` (또는 `stock/.env`) — git 에 올리지 않는다.
- 웹 화면 순서: **[탐색] → 목록(배수 높은 순)에서 체크 → [승인]** → 승인한 영상 자료 + 주별 분석 + `result/outliers/analysis.md` → GitHub. 쇼츠는 4번 칸 [쇼츠].
- 예전 자동 실행(화면 없이): `-Auto -Folder stock` · 작업 스케줄러 등록: `-RegisterTask -Folder stock` · 설정을 GitHub 것으로 덮기: `-UpdateConfig -Folder stock`. 자세히 `guides/pc_analysis.md`.

## 할당량

- 검색어 1개 = 약 300단위 (성공 사례 검색 2번 + 분석기 1번). 지금 32개 → **한 바퀴 약 9,600단위** ≈ 하루 할당량(10,000). 넘으면 태평양 자정 +10분(한국 오후 4~5시)에 **저절로 이어서** 한다.
- 2026-10-15 클라우드에서 검색어를 고르느라 같은 키로 약 810단위를 썼다 (씨앗 검색 4개 × 200 + 영상 정보).
- 할당량을 아끼려면 검색어를 지우면 된다 (`keywords.txt` 줄 삭제) — Google Cloud 프로젝트를 여러 개 만드는 방법은 쓰지 않는다 (YouTube API 정책 위반).

## 파일

| 위치 | 내용 |
|---|---|
| `analyzer_config.toml` | 분석기 설정 v1.0: 주제 이름 **주식**·폴더 `stock`·할당량 `QUOTA_BUDGET = 6000`·**영상 파일 안 받음**(`DOWNLOAD_VIDEOS = false`) — 값은 `economic/` v1.1 과 같음 |
| **`keywords.txt`** | **검색어 목록 32개** — 한 줄에 하나, `#` 줄은 메모. 실제 영상 태그에서 고름(`tools/tag_keywords.py` v1.3). **GitHub 에서 고치면 PC 가 다음 회차에 자동으로 받아 씀** |
| `keywords.toml` | 주제 관련어 45개(주식·코스피·ETF·배당주·공매도·반대매매·연금저축·ISA …) · 약한 관련어 23개(투자·종목·개미·손절·물타기 …) · 제외어(주식회사·(주)·㈜) — 탐색한 영상이 주식 영상인지 가름 |
| `tag_rules.toml` | 태그 → 검색어 규칙 v1.0: 씨앗 검색어(주식·주식 투자·주식 초보·미국주식) · 채널 5곳 이상 · 40개 · **빼는 말**(뉴스·시황·전망·라이브·쇼츠·경제·금리·환율·정치·**종목 이름**·부동산·코인·자기계발·AI·금융·달러) · 묶음 13개 · 묶음 밖은 '기타 주식' |
| [`tag_candidates.md`](tag_candidates.md) | **고른 태그 표**: 태그마다 채널 수·영상 수·묶음·검색어로 썼는지(안 쓴 까닭) — `.csv` 도 |
| `analysis_rules.toml` | 분석 기준 v1.0 — `economic/` v1.4 와 같고 뺄 주제만 **부동산·코인** (`OFF_TOPIC_THEMES`) |
| `.env` | (PC에만, git 제외) 이 주제만 쓰는 키 — 보통 비워 둠 |
| `targets.json` | (PC 웹 화면) 직접 추가한 영상·채널 |
| `result/outliers/` | (분석 뒤) 승인한 영상 자료 `W_<영상ID>/` · `analysis.md`(지시사항 재료 — 숫자·원문만) · `weekly.md` · `approved.md` · `downloads.md` · 쇼츠 `shorts/` |

## 검색어 다시 고르기

```bash
python tools/tag_keywords.py stock --write-keywords                    # 씨앗 검색 4개 × 200단위 + 영상 정보
python tools/tag_keywords.py stock --write-keywords --no-seed-search   # 받아 둔 캐시로만 (0단위)
```

빼고 싶은 말은 `tag_rules.toml` 의 `TAG_EXCLUDE` 에 넣는다 — 그러면 다시 골라도 되살아나지 않는다.
