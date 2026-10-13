# CHANGELOG — youtube_topic_analyzer

## 2026-10-13 (5) — 오래 걸리던 까닭 고침: 하루 할당량 쓰는 순서 (댓글은 원인이 아님)

### 왜 (사용자 질문: "너무 오래 걸리는데 댓글 전체 받아서 그런거야? 댓글 받아오는 방식이 어떤 거야 좋은 해결 방법 생각해봐")
- 댓글 받는 방식: commentThreads(최상위, 100개씩 1단위, 답글 5개까지 같이) + 답글이 5개 넘는 댓글은 comments.list(100개씩 1단위). 쪽마다 저장해 이어 받음.
- **실측 (2026-10-13, 클라우드 API):** 조회수 355만 영상 댓글 583개 전부(답글 218) ≈ 11단위, 작은 채널 사례 44개 = 3단위 → 40개 영상이면 보통 몇백 단위. 하루 10,000 의 대부분은 **검색**(100단위/번: 성공 사례 40번 + 분석기 50번).
- 실제로 날을 늘리던 것:
  1. 성공 사례 할당량이 고정 4,000인데 검색 40번(4,000) + 검색 여유 150 이 안 들어가 **검색 2번이 늘 다음 날로** → 첫날엔 결과가 '준비됨'이 될 수 없었음
  2. 고정 배분(성공 사례 4,000 / 분석기 6,000) — 분석기가 덜 쓰면 남은 단위를 버림, 몇백 단위 댓글 때문에 하루를 더 기다림
  3. `pc_analysis` 가 분석기 사용량을 잘못된 키(`used`)로 읽음 (실제 `quota_used`)

### 고친 것
| 파일 (버전) | 함수·항목 | 내용 |
|---|---|---|
| `tools/pc_analysis.py` v1.3 | `outlier_need`, `one_round` | 성공 사례 할당량 자동(`--outlier-quota 0` 기본) = 검색 수 × 100 + 여유 (경제·재테크 4,290) → 첫날 검색·인기 댓글까지 끝 |
| 〃 | `Ledger`, `pacific_day`, `one_round` | 오늘(태평양 날짜) 쓴 단위 장부 `.yt_work/quota_<주제>.json` — 도구마다 남은 만큼만 줌(같은 날 다시 돌려도 넘지 않음), 분석기는 `--quota-budget` 으로 오늘 남은 만큼 |
| 〃 | `one_round` (③ 보충 `TOPUP`) | 분석기 다음에 오늘 남은 할당량으로 성공 사례 수집을 한 번 더 (검색은 캐시 → 댓글로) |
| 〃 | `analyzer_summary`, `outlier_summary` | 분석기 사용량 `quota_used` 로 읽기, `ready` 를 진행 상태·로그에 |
| `tools/outlier_research.py` v1.5 | `fetch_all_comments(full=)`, `comments_step`, `run_topic`, `write_status` | 댓글 1단계 = 모든 사례 인기 댓글 100개(관련성 순 1쪽, 영상마다 1단위) 먼저 → `status.json ready`; 2단계 = 사례마다 전부(시간순+답글). 같은 댓글은 id 로 하나로 |
| `guides/pc_analysis.md` v1.4 | 할당량 표·댓글 비용 | 단계 ③ 보충, 실측 숫자, 첫날 ready·다음 날 complete |

### 결과 (로그·검사)
- `pc_analysis.py --self-test` ALL PASS (새: 1회차 OUTLIER→ANALYZER→TOPUP, 보충 할당량 = 9,800 − 3,900 − 5,700 = 200, 같은 날 다시 실행하면 다 쓴 경우 도구를 돌리지 않음, 분석기 `quota_used`, 자동 할당량 계산)
- 성공 사례 오프라인 시험 14개 통과 (새: 할당량이 모자란 1회차에도 사례 8개 모두 인기 댓글 먼저 → `ready=True`)
- 실제 API (임시 폴더, 검색은 막고 `--quota 140`): 성공 사례 댓글 44/44(3단위), 조회수 상위 583/583(답글 218, 약 11단위), 두 영상 2단계 합계 10단위

### 알려 둘 것
- 검색 할당량은 그대로라 주제 하나가 '완전히' 끝나는 데는 보통 이틀째 (분석기 나머지 검색어). 하루 안에 다 끝내려면 검색을 줄여야 함 (예: 성공 사례 `--per-group 1` → 검색 20번, 분석기 검색어 50 → 30) — 사용자가 정할 일.
- 연구·교육용, 투자 권유 아님. 위험 관련 값 변경 없음 (할당량은 하루 10,000 − 200 안에서 나눔).

## 2026-10-13 (4) — 실행 명령을 어느 터미널에서나 되게 (문서만)

### 왜 (사용자 PC 오류: "-File 매개 변수에 대한 인수 '.run_analyzer.ps1'이(가) 없습니다")
- 오류 속 경로에 `\`가 없음 → 명령을 **Git Bash**(또는 WSL·VS Code bash 터미널)에서 실행해 bash 가 `.\run_analyzer.ps1`의 `\`를 지운 것으로 판단. 그 창에서는 받기 줄 `wget … -OutFile`(PowerShell 문법)도 안 돼 파일이 없을 수 있음. 저장소는 아직 공개(raw 주소 200)라 비공개 문제는 아님.

### 고친 것 (코드 동작 변화 없음)
| 파일 (버전) | 내용 |
|---|---|
| `guides/pc_analysis.md` v1.3 · `README.md` · `guides/README.md` v1.14 · `run_analyzer.ps1` v2.2.1(머리 주석만) · `economic/analyzer_config.toml` v1.0.1(주석만) | 실행 `powershell -ExecutionPolicy Bypass -File run_analyzer.ps1` (`.\` 없이 — PowerShell·명령 프롬프트·Git Bash 공통), 받기 `curl.exe -L -o run_analyzer.ps1 …` (Windows 10·11 기본), 문제 해결에 이 오류 |

## 2026-10-13 (3) — 여러 주제를 동시에 (주제마다 검색어·키 파일)

### 왜 (사용자 지시: "economic 분석을 위해 경제, 재태크 관련 검색어 만들어 놓았어? 그리고 동시에 병렬로 다른 주제 분석도 가능하도록 해야해 그럼 검색어 설정 파일, 키설정 파일도 여러개 있어야 겠지")
- 검색어: `economic/keywords.toml` v1.0 이미 있음 (10개 그룹 × 5 = 50개, 관련어 48개) — 바꾸지 않음.
- 같은 PC에서 두 주제를 함께 돌리면 분석기가 같은 git 작업 폴더(`.yt_work/_github_clone`)·임시 폴더를 서로 지우고, 패키지 설치가 겹쳤다.
- 할당량: YouTube 할당량은 Google Cloud 프로젝트마다 하루 10,000. 같은 도구를 프로젝트 여러 개로 나눠 할당량을 더 받는 것('sharding')은 YouTube API 개발자 정책 위반 (할당량 축소·키 회수·계정 정지 위험, https://developers.google.com/youtube/terms/developer-policies-guide) → 기본은 키 하나를 주제끼리 나눠 씀.

### 고친 것
| 파일 (버전) | 함수·항목 | 내용 |
|---|---|---|
| `youtube_topic_analyzer.py` v2.6.0 | `key_sources`, `load_keys`, `reload_github_token`, `folder_tag`, `main` | 주제별 키: `<주제폴더>/.env` → 환경 변수 `<키>_<폴더>` → 맨 위 `.env` → 환경 변수 |
| 〃 | `process_success_case`, `stage8_push_github`, `push_only`, `JsonCache.set` | 주제마다 따로: `.yt_work/_github_clone_<폴더>`·`_outliers_keep_<폴더>`·`tmp/<폴더>/<영상>`·`push_log_<폴더>.txt`, 캐시 임시 파일 이름에 프로세스 번호 |
| 〃 | `parse_args`, `apply_cli` | `--setup-only`(패키지 준비만), `--quota-budget`(⚠️ 비용 관련 — 같은 키를 나눌 때 실행기가 넘김). 자가진단 26/26 |
| `tools/outlier_research.py` v1.4 | `load_api_key`, `_env_file_key`, `main` | 주제별 키(같은 순서), 주제 여러 개를 한 번에 돌리면 키마다 Api(할당량) 따로 — 같은 키끼리만 `--quota` 를 나눠 씀 |
| `tools/pc_analysis.py` v1.2 | `run_parallel`, `child_cmd`, `spawn_prefixed`, `find_secret`, `ensure_topic_env`, `analyzer_budget` | `pc_analysis.py economic health` → 패키지 준비 한 번, 주제마다 자식 프로세스(줄 앞 `[주제]`, 잠금·로그·진행·대기 따로). 같은 키를 쓰는 주제 N개 → 성공 사례·분석기 할당량 모두 ÷N. `<주제>/.env` 빈 틀을 만듦(정책 경고 포함) |
| `run_analyzer.ps1` · `run_analyzer.sh` v2.2 | `-Folder` / `--folder` | 여러 주제 (`economic,health` 또는 여러 번), 주제마다 설정·검색어 파일 받기, 작업 스케줄러·cron 도 여러 주제 |
| **버그 수정** `tools/pc_analysis.py`·`tools/outlier_research.py` | `.env` 읽는 정규식 | `KEY=` 가 비어 있고 다음 줄이 주석이면 `\s*`가 줄을 넘어 `#`를 키로 읽던 것 → `[ \t]*` (v1.0~1.3 에도 있던 문제: 빈 키를 '있음'으로 봄) |
| 문서 | `guides/pc_analysis.md` v1.2 "여러 주제를 동시에" · `guides/README.md` v1.13 · `guides/pipeline.md` v1.13 · `CLAUDE.md` · `README.md` · `economic/README.md` | 주제마다 파일 표, 키 찾는 순서, 할당량 N등분, sharding 경고·할당량 증가 신청, 새 주제 추가 방법 |

### 결과 (로그·검사)
- `pc_analysis.py --self-test` ALL PASS (새: 같은 키 p1·p2 → `--outlier-quota 2000`·`--quota-share 2`, 다른 키 p3 → 4000·1, 설정 없는 주제는 건너뛰고 exit 1, 남은 일이 있으면 exit 3, `QUOTA_BUDGET` 읽기)
- 실제 병렬 dry-run (임시 폴더, economic + `--init-config` 로 만든 health): 줄 앞 `[economic]`·`[health]`, 같은 키면 `outlier_quota=2000 daily_quota=4750`, health/.env 에 다른 키를 넣으면 나누지 않음, 자식 분석기 명령에 `--skip-install`·`--quota-budget 3000`(공유 2)
- `run_analyzer.sh --folder economic --folder health` (로컬 서버): 설정·검색어 4개 받고 `pc_analysis.py economic health` 실행, `--print-cron` 도 두 주제
- 주제별 키 시험 5개 통과(주제 .env 먼저·빈 값이면 맨 위·환경 변수 `_<폴더>`·키가 다르면 Api 따로·같으면 하나), 성공 사례 오프라인 시험 13개 그대로 통과, 분석기 자가진단 26/26
- `run_analyzer.ps1` 은 이 환경에 PowerShell 이 없어 실행 시험 못 함

### 알려 둘 것
- 키 하나를 여러 주제가 나눠 쓰면 주제마다 그만큼 오래 걸림 (남은 부분은 매일 자동으로 이어서). 더 빠르게 하려면 할당량 증가 신청.
- 연구·교육용, 투자 권유 아님. 위험 관련 값: `--quota-budget`(나눌 때만 실행기가 낮춤)은 로그에 '위험/비용 관련 설정이 기본값과 다릅니다'로 남음.

## 2026-10-13 (2) — 댓글 전부 · 조회수 상위 영상(구독자 무관) · 저장소가 비공개면 전부 올림

### 왜 (사용자 지시: "비공개로 돌릴테니까 전부 다 업로드되게 하고 댓글은 전부 받도록 수정해 그리고 구독자 수 상관없이 조회수 많이 나온 영상 댓글은 전부 받아야해")
- 지금까지: 사례마다 인기 댓글 100개(최상위만), 작은 채널 성공 사례만, 공개 저장소라 사례 폴더는 PC에만.
- 확인 (2026-10-13 16:2x KST): 저장소는 아직 **공개** (`api.github.com/repos/…` 토큰 없이 200) → 코드가 올리기 전에 공개 여부를 확인해 비공개일 때만 사례 폴더를 올림.

### 고친 것
| 파일 (버전) | 함수·항목 | 내용 |
|---|---|---|
| `tools/outlier_research.py` v1.3 | `fetch_all_comments`, `write_comments_csv`, `read_comments_jsonl`, `Api.get` | **댓글 전부:** commentThreads(시간순, 100개씩) + 답글이 5개 넘는 댓글은 comments.list. 쪽마다 `comments.jsonl`에 덧붙이고 `comments_state.json`에 다음 쪽 저장 → 할당량이 끝나면 다음 실행이 그 쪽부터. 같은 댓글은 id로 하나로. 댓글 막힌 영상(403)·지워진 답글(404) 처리. `--comments 0`(기본 = 전부), `--no-replies` |
| 〃 | `relevant`, `run_topic`, `case_folder`, `write_summary`, `write_status` | **조회수 상위 `--popular 20`:** 구독자 수 상관없이 주제 관련(분석기 `topic_relevance`와 같은 규칙, keywords.toml `RELEVANCE_*`)·4분 이상·최근 365일 → 조회수 순, 채널당 2개 → 자막·썸네일·댓글 전부 (폴더 `P01_<영상ID>`, `popular.csv`, 성공 사례와 겹치면 그 폴더). summary·status에 두 묶음·댓글 받은 수·받는 중인 영상 |
| 〃 | `_comment_rec` | 댓글 기록: id·답글이면 부모 id·좋아요·글·시각·답글 수·채널 주인 댓글 여부. **작성자 이름은 저장하지 않음** |
| `youtube_topic_analyzer.py` v2.5.0 | `_copy_local_outliers`, `stage8_push_github` | **저장소가 비공개면** PC의 `outliers/`를 사례 폴더까지 통째로(저장소 쪽을 PC와 똑같이, `.cache`·`_old`·95MB 넘는 파일 제외) 올리고 `git add -f`로 .gitignore 를 넘음. 공개면 예전처럼 요약 파일만. 자가진단 1개 추가(25/25) |
| `tools/pc_analysis.py` v1.1 | `one_round`, `analyzer_done_recently`, `round_verdict` | `--popular` 전달, 분석기가 이월 없이 끝나면(7일 안) 다음 회차부터 건너뛰고 하루 할당량 `--daily-quota 9500`을 댓글에, 기본 최대 회차 7 → 10, `--rerun-analyzer` |
| `run_analyzer.ps1` · `run_analyzer.sh` v2.1 | `Get-Secret`/`env_get`, `Get-Remote`/`fetch` | **비공개 저장소에서 코드 받기:** `.env`(또는 환경 변수)의 `GITHUB_TOKEN`으로 GitHub API(Contents)에서 받음. ps1은 JSON base64(1MB 이하), sh는 원본 머리글 — 토큰은 머리글로만(sh는 curl 설정을 표준 입력으로, 명령줄에 안 남김). `.env`가 없으면 먼저 틀을 만듦 |
| `tools/outlier_stats.py` v1.2 | `comment_needs`, `main` | `--set success|popular|all`, `--top-level-only`, 순위를 글자로(P1) |
| `.gitignore` | `*/result/outliers/P[0-9][0-9]_*/` | 조회수 상위 사례 폴더도 공개 상태에서는 막음 (시험에서 빠져 있던 것 발견) |
| `guides/tts_guide.md` v1.8 | 3번 셀 | 저장소가 비공개여도 Kaggle 셀이 Secrets 토큰으로 `git clone`·`fetch` (`GIT_CONFIG_*` 환경 변수 — 값이 셀·출력에 안 나옴) |
| `guides/pc_analysis.md` v1.1 · `guides/pipeline.md` v1.12 · `guides/README.md` v1.12 · `CLAUDE.md` · `README.md` · `economic/README.md` | 문서 | 저장소를 비공개로 바꾸는 법, 비공개일 때 실행기 처음 받는 법(PowerShell·bash 한 줄), 댓글 전부 할당량, 두 묶음, 무엇이 올라가는지 |

### 결과 (로그·검사)
- 오프라인(가짜 API, 댓글 쪽·답글 흉내) 13개 통과: 1회차 한도 2,160 → 댓글 받는 중 2개·`exit 3`·다음 쪽 저장 → 2회차 `complete`·검색 전부 캐시 → **사례 8개 모두 댓글 수 = 최상위 + 답글 (빠짐·중복 없음)**, 조회수 상위에 구독자 90만 채널 포함·주제 밖(요리) 제외, 3회차 댓글 할당량 0, `--comments 50 --no-replies` 뒤 전부로 바꾸면 이어서 전부
- 실제 API(클라우드, 임시 폴더, `--comments 200`): 성공 사례 1개 **댓글 44/44(영상 표시 수와 같음, 최상위 26 + 답글 18)·채널 주인 1**, 조회수 상위 1개 구독자 411만 채널·조회수 355만(최상위 200에서 멈춤 — 시험 제한). 이번 시험 할당량 512 (오늘 초기화 뒤)
- `pc_analysis.py --self-test` ALL PASS (새 시나리오: 분석기 끝난 다음 회차 = OUTLIER, PUSH 만·`--quota 9500`·`--popular` 전달)
- 분석기 자가진단 25/25 (새: 공개면 요약만 / 비공개면 사례 폴더까지), git 시험: `git add -A` 는 사례 폴더를 건너뛰고 `git add -A -f -- …/outliers` 는 올림
- 실행기: `run_analyzer.sh`(토큰·API 방식)로 받은 코드가 `origin/main`과 바이트 같음, 문서의 bash 한 줄·PowerShell 한 줄(같은 방식을 파이썬으로)도 바이트 같음(BOM 유지). `run_analyzer.ps1` 자체는 이 환경에 PowerShell이 없어 실행 시험 못 함

### 알려 둘 것
- 저장소를 비공개로 바꾸기 전까지는 사례 폴더가 올라가지 않음 (코드가 막음). 바꾼 뒤에는 PC·Kaggle 모두 토큰이 있어야 받음.
- 분석기 리포트의 시청자 질문 표본(`FETCH_COMMENTS_TOP_N` 30개 영상 × 100개)은 통계용이라 그대로 — 댓글 전부는 `result/outliers/`의 두 묶음에서.
- 받기 시작한 뒤 새로 달린 댓글은 빠질 수 있음 (시간 순으로 내려가며 받음).
- 연구·교육용, 투자 권유 아님. 위험 관련 값 변경 없음. 할당량: 분석기가 끝난 날부터 성공 사례·조회수 상위에 9,500 (`--daily-quota`).

## 2026-10-13 — 주제 폴더를 economic(경제·재테크) 하나로 · 검색어 파일 분리 · PC 실행 · 할당량 초기화 뒤 자동으로 이어서

### 왜 (사용자 지시: "기존 stock, health 등 모든 주제 폴더 전부 삭제하고 경제, 재태크(economic) 폴더만 하나 만들고 코드 분석기에서 사용한 검색어 목록 같은거는 따로 빼놓고 분석기 코드 pc에서 돌릴 수 있도록 수정하고 방법 알려주고 api 할당량이 초기화된 시간이 되면 다시 자동으로 분석결과를 확인 못한 부분부터 새로 추가로 만들도록 수정해")
- 클라우드는 네트워크 정책상 `www.youtube.com`·`i.ytimg.com`이 막혀 자막·썸네일을 못 받음 (2026-10-12·13 ProxyError 403) → 집 PC 실행을 기본으로.

### 고친 것
| 파일 (버전) | 함수·항목 | 내용 |
|---|---|---|
| `stock/` `stock_backup/` `health/` `lifetips/` `selfdev/` `space/` `story/` | 삭제 | 사용자 지시. 내용(분석 결과·규칙·대본 23개·올린 영상 4개의 `youtube.json`)은 커밋 `2a68307`에 남음 |
| `economic/analyzer_config.toml` v1.0 (새로) | `[topic]`·`[keywords]`·`[ads]`·`[advanced]` | 주제 경제·재테크, `KEYWORDS_FILE = "keywords.toml"`, `QUOTA_BUDGET = 6000` ⚠️ 비용 관련 — 성공 사례 수집 4,000과 합쳐 하루 10,000 |
| `economic/keywords.toml` v1.0 (새로) | `KEYWORD_GROUPS`·`[relevance]` | **검색어 목록 분리**: 10개 그룹 × 5개 = 50개, 주제 관련어 48개·약한 관련어·제외어 |
| `youtube_topic_analyzer.py` v2.4.0 | `KEYWORDS_FILE`, `apply_keywords_file`, `keywords_template`, `load_config`, `init_config_only` | 목록 설정(`KEYWORD_GROUPS`·`EXTRA_KEYWORDS`·`EXCLUDE_KEYWORDS`·`RELEVANCE_*`)을 설정 파일 옆 `keywords.toml`에서 읽음 (설정 파일에도 있으면 검색어 파일 값 + 경고), 기본 주제 economic |
| 〃 | `stage8_push_github`, `_clean_result_dir`, `_copy_local_outliers` | 푸시가 저장소의 `<폴더>/result/outliers/`를 지우지 않고, PC의 최신 outliers 요약(csv·md·json — 사례 폴더 제외)을 함께 올림 |
| `tools/outlier_research.py` v1.2 | `load_keywords` | 검색어를 `keywords.toml`에서 (분석기와 같은 파일), 주제 이름 `[topic] TOPIC`, Python 3.10은 tomli |
| 〃 | `Api.get`, `cached_search`, `collect_api` | **이어서 돌리기:** 검색 캐시 7일·영상 정보 24시간·구독자 7일, 검색은 한도에서 150단위를 남기고 멈춰 영상 정보·구독자·댓글은 계속, 하루 할당량(403 quota)이면 새 요청 중단 → 캐시로 결과 만들고 남은 일 기록 |
| 〃 | `deep_case`, `run_topic` | 이미 받은 자막·댓글·썸네일은 다시 받지 않음, 순위가 바뀌면 폴더 이름만 바꿈, 빠진 사례는 `_old/`로 (git 제외) |
| 〃 | `write_status`, `main` | `result/outliers/status.json`(complete·pending·자막/썸네일 못 받은 것·`retry_elsewhere`), 남은 일이 있으면 종료 코드 3 |
| 〃 | `speech_stats`, `write_summary` | summary.md에 첫 1분 발췌·90초마다 흐름·전체 음절 (자막 원문은 git에 안 올리므로 Claude 분석용 요약) |
| `tools/pc_analysis.py` v1.0 (새로) | `one_round`, `round_verdict`, `run`, `wait_until`, `next_quota_reset`, `Lock` | PC 실행기: 회차 = 성공 사례(`--per-group 2 --top 20 --quota 4000`) → 분석기(`--no-push`) → `pc_progress.json` → `--push-only`. 남은 일이 있으면 **태평양 자정 + 10분**(한국 16:10 / 겨울 17:10)까지 기다렸다가 다음 회차, 최대 7회차. `--once`(작업 스케줄러용, 남으면 3), `--dry-run`, 잠금 파일(동시 실행 막기, 5분마다 갱신), 패키지 자동 설치(youtube-transcript-api·tomli·tzdata) |
| `run_analyzer.ps1` v2.0 · `run_analyzer.sh` v2.0 | 받는 파일·실행 | 기본 폴더 economic, 코드 4개(분석기·pc_analysis·outlier_research·outlier_stats)를 매번 최신으로, `analyzer_config.toml`·`keywords.toml`은 없을 때만, `tools/pc_analysis.py` 실행. `-Once`·`-RegisterTask`(매일 17:15)·`-UnregisterTask`·`-AnalyzerOnly` / `--once`·`--print-cron`·`--analyzer-only` |
| `tools/outlier_stats.py` v1.1 | `topic_regex` | 주제 낱말을 `keywords.toml`의 `RELEVANCE_TERMS`에서 |
| `tools/run_analysis.sh` v1.2 | 사용법 | 예시를 economic으로, 집 PC 안내 (동작은 v1.1 그대로) |
| `.gitignore` | `*/result/outliers/_old/` | 빠진 사례 폴더도 올리지 않음 (다른 채널의 자막·댓글 원문·썸네일) |
| `guides/pc_analysis.md` v1.0 (새로) · `guides/README.md` v1.11 · `guides/pipeline.md` v1.11 · `README.md` · `CLAUDE.md` · `economic/README.md` | 문서 | PC 실행 방법·키 넣기·회차와 이어서 돌리기·작업 스케줄러·결과 위치, 1단계 = 집 PC 기본, 옛 `stock/…` 경로는 커밋 `2a68307`의 예시 |

### 결과 (로그·검사)
- `python tools/pc_analysis.py --self-test` → `result="ALL PASS"`: 초기화 시각 7경우 × (zoneinfo·규칙 계산) — 서머타임 시작·끝나는 날 포함, 1회차 남음 → 16:10까지 기다림 → 2회차 끝(exit 0), `--once` 남음 → exit 3·`left="… 이월된 검색어 2개"`, 이미 돌고 있으면 exit 2, 잠금 파일 정리
- `tools/outlier_research.py` 오프라인 시험(가짜 API) 14개 통과: 한도 700 → 검색 5·남은 검색 15·exit 3 → 다시 → 캐시 5·새 15·exit 0 → 다시 → 할당량 0, 오래된 영상 정보는 한도 0이면 예전 숫자로(pending 0), 다음엔 다시 받음
- 실제 API(클라우드, 저장소 밖 임시 폴더): 1회차 `--quota 450` → `searches_new=3 quota_used=306 complete=False exit=3`, 2회차 `--quota 650` → `searches_cached=3 searches_new=5 quota_used=510`, 남은 검색 17 → 12. 자막·썸네일은 ProxyError 403 → `retry_elsewhere=True`로 기록 (PC에서 다시)
- 실행기 시뮬레이션: `RAW_BASE=http://127.0.0.1:8765 bash run_analyzer.sh --no-venv -- --dry-run` → 코드 4개·설정 2개 받음, `tools/pc_analysis.py economic --dry-run` 실행 확인. `run_analyzer.ps1`은 이 환경에 PowerShell이 없어 실행 시험 못 함 (UTF-8 BOM·CRLF 유지, v1.0과 같은 구조)
- 분석기 자가진단 `passed=24/24`, `economic` 설정 읽기: 그룹 10개·검색어 50개

### 알려 둘 것
- 올린 영상 4개(몰빵·물타기·빚투·패닉셀)의 `youtube.json`이 작업 폴더에서 지워져 `tools/youtube_feedback.py`·`studio_trim.py`로 그 영상들을 더는 다루지 못함 (필요하면 `git checkout 2a68307 -- stock_backup/source/<영상ID>/youtube.json`로 되살림).
- 다른 채널의 자막 전문·댓글 원문·썸네일은 공개 저장소라 올리지 않음 (사례 폴더는 PC에만). summary.md의 발췌·흐름으로 분석.
- 연구·교육용, 투자 권유 아님. 위험 관련 값(포지션·손절) 변경 없음. 할당량 값만 `QUOTA_BUDGET 6000`·성공 사례 4,000으로 명시.

## 2026-10-12 — 주식 폴더 새로 시작: 백업(stock → stock_backup) · 분석 다시 · 지시사항 새로 · 새 영상 3개 오디오 전까지

### 왜 (사용자 지시: "일단 기존 주제폴더 _backup 붙여서 백업해놓고 stock만 새로 만들어서 유튜브 성공사례 분석 코드 돌려서 분석 결과 파일 만들고 성공사례 분석(대본 내용, 댓글 반응 등 영상의 여러 정보 참고)해서 각 지시사항 파일 새로 만들고 오디오 생성 전 단계까지 결과물 만들어봐")
- 올린 주식 영상 4개가 공개 하루 조회수 0~4회, 평균 시청 약 50초 → 분석부터 다시.

### 고친 것
| 파일 | 함수·항목 | 내용 |
|---|---|---|
| `stock/` → `stock_backup/` | README 앞 ⏸ 보류 | 옛 주식 폴더 그대로 옮김 (올린 영상 4개의 youtube.json·통계 포함). `tts_narration all`·`make_summary --all`이 건너뜀. 다른 주제 폴더는 그대로 |
| `stock/analyzer_config.toml` v2.0 (새로) | `KEYWORD_GROUPS` | '실패 사연' 90개 → 9개 그룹 × 5개 45개 (사연·특징/패턴·심리·노후·ETF 장기투자·빚투·사기·실험·시장 급락), `QUOTA_BUDGET` 6000 |
| `tools/run_analysis.sh` v1.1 | 결과 복사 | **버그 수정:** `result/`를 통째로 바꾸며 `result/outliers/`(outlier_research 결과)까지 지우던 것 → 옮겼다가 되돌림 (`bash -n` 확인. 지우기 부분은 안전 검사 때문에 실제 실행 시험은 못 함) |
| `tools/outlier_stats.py` v1.0 (새로) | `title_stats`, `comment_needs` | data_insights 숫자 재현: 제목 요소·길이·채널 크기별 성공 비율, 댓글 갈래(낱말 규칙). 옛 후보로 손 계산과 같은 결과 확인(120개·31개·금액 15/36) |
| `stock/guides/data_insights.md` v3.0 | 전체 | 작은 채널 성공 사례 33개 형식 분류, 제목 요소(437개), 길이(4~8분 7%), 챕터 구성, 댓글 1,103개, 사용자 결정 4개 |
| `stock/guides/script_rules.md` v2.2 | 3·5·6·9번 | "망하는 과정형"(단계 4~5 + 장치 4~5), 10~12분, 빚·미수 사연 동정 금지, 재구성 의심 막기, 근거 은행 +20줄 |
| `stock/guides/title_rules.md` v2.1 | 3·4·8번 | 우선 소재 3개, "과정·벌어진 일"은 T2에서만 시험, 손실 낱말은 공식을 해치지 않을 때만 |
| `stock/guides/thumbnail_rules.md` v2.0 · `upload_rules.md` v2.0 · `source/used_content.md` v2.2 | — | 썸네일 규칙 그대로 옮김, AI 음성 안내·챕터 = 단계 이름, 옛 영상 사용 내용 이어받고 새 영상 3개 추가 |
| `guides/pipeline.md` v1.10 | 1단계 4번 | outlier_stats, 같은 날 분석기와 할당량 나누기, 네트워크 정책(자막·썸네일 막힘) |
| `stock/source/pandon-2026-10/` · `bonjeon-2026-10/` · `jisu-2026-10/` (새) | 대본·SRT·README·제목·썸네일 3·업로드 시트·요약 | 판돈 키우기(알테오젠) · 손절·본전(크래프톤) · 장기투자 이탈(네이버) |

### 결과 (로그·검사)
- 성공 사례 API 수집 `[DONE] candidates=1075 qualified=33 deep=20 quota_used=3653`, 분석기 `[SUMMARY] quota_used=5833` (영상 1,589개, 키워드 44/45), 복구 `[DONE] quota_used=22 cases=20` — 합계 9,508 / 하루 10,000
- `srt_tool check`: pandon 문장 125 / 자막 144 · 끝 11:31 · 사연 124음절 ✅ / bonjeon 133 / 149 · 11:25 · 123음절 ✅ / jisu 124 / 156 · 11:36 · 123음절 ✅ — 셋 다 "✅ 이상 없음", 챕터 13개 YouTube 규칙 통과, `youtube_upload --dry-run` 문제는 영상 파일 없음 1개뿐
- 목표 분량 변화: 옛 영상 7:39~7:58 → 새 영상 추정 11:25~11:36 (근거: 4~8분 성공 7% vs 8~12분 23%)

### 알려 둘 것
- 자막·썸네일은 받지 못함: 이 클라우드 환경 네트워크 정책이 `www.youtube.com`·`i.ytimg.com`을 막음 (ProxyError 403). "대본 내용"은 설명란·챕터·태그·댓글로 봄.
- `candidates.csv`는 run_analysis.sh v1.0 버그로 지워짐 → 자세히 본 20개만 복구, 다음 할당량에 다시 수집해야 함.
- 주가는 뉴스·리포트에 나온 종가로 검산 (시세 사이트 접속이 막힘). 각 README의 "렌더 전에 다시 확인" 표에 남김: 네이버 2025-12-30 종가(시가총액으로 맞음 확인), 크래프톤 7/15 역산 종가 등.
- 같은 사연 종목 겹침을 검토 중 발견(장기투자 이탈 첫 안이 판돈과 같은 알테오젠 하락) → 네이버로 바꿈.
- 사연자 목소리가 같은 날 S07(40대 초반 남성)로 고정됨 → 썸네일 인물을 40대 초반 남성으로.
- 연구·교육용, 투자 권유 아님. 위험 관련 값 변경 없음.

## 2026-10-12 — 목소리 고정: 사연자 S07(말 속도 조금 더 빠르게)·진행자 H04 (tts_narration v1.6)

### 왜 (사용자 지시: "사연자는 말하는 속도 조금 더 빠르게 해서 S07, 진행자는 H04로 정했어 수정해")

### 고친 것
| 파일 | 함수·항목 | 내용 |
|---|---|---|
| `voices/storyteller.json` v2.1, `voices/ref/storyteller.wav`·`.json` (새로) | `pick S07` | engine clone, 기준 소리 = S07 샘플 기준 소리(107.1Hz, 시드 3402, sha1 b2098b3eb85b6a0a), gap 0.55, lock. **pace {min 4.2, max 5.2} → {speed 1.1, min 4.6, max 5.8, max_stretch 0.15}** (⚠️ 말 속도 설정 변경 — 사용자 지시) |
| `voices/host.json`, `voices/ref/host.wav`·`.json` | `pick H04` | 진행자 기준 소리 H01(따뜻한 중저음) → **H04**(30대 초반, 또렷하고 밝은 중저음). 옛 소리는 git 기록 |
| `tools/tts_narration.py` v1.6 | `pace_ok`, `make_sentence` | `pace.speed`: 모든 문장을 이 배수로 빠르게 한 뒤 [min, max] 안으로(음 높이 그대로, 최대 ±max_stretch), 짧은 문장도 speed 만큼. speed 없으면 v1.5와 같음. 로그 `[PACE] … speed=` |
| 〃 | `frozen_current`, `samples_status`, `write_samples_readme` | 고른 뒤 current 후보(S01·H01) 샘플은 '고르기 전 목소리' 기록으로 두고 다시 만들지 않음 (고친 문제: pick 뒤 README에 '⏳ 아직 없음'으로 나오고 samples 가 2개를 다시 만들려 함) |
| 〃 | `check_speakers` | custom_voice 역할이 없으면 CustomVoice 모델(3.8GB)을 불러오지 않음 (고친 문제: 두 역할 모두 clone 인데 화자 확인만을 위해 내려받아 이 세션 디스크가 거의 참 — Kaggle에서도 시간·메모리 낭비) |
| `voices/samples/README.md`·`samples.json` | | S07·H04 '✅ 고름', pace 설명에 speed |
| `CLAUDE.md`, `guides/tts_guide.md` v1.7 | 4-0 | 고른 결과·속도 기록 |

### 확인 (같은 문장 3+3개를 이 세션 CPU에서 실제 모델로 — `build --txt`, 9분 32초)
| 역할 | 문장 | 생성 속도 → 맞춘 속도 (음절/초) | 배율 | 높이 |
|---|---|---|---|---|
| 사연자 S07 | 1 "그날 계좌를 열어 보고…" | 4.99 → 5.48 | ×1.100 | 118.8Hz |
| 〃 | 2 "-800만 원이 찍힌…" | 4.80 → 5.27 | ×1.100 | 125.7Hz |
| 〃 | 3 "조금만 기다렸으면…" | 5.35 → 5.78 | ×1.084 (상한 5.8) | 106.2Hz |
| 진행자 H04 | 1~3 | 6.08 · 5.78 · 6.38 (pace 없음) | - | 137·118·119Hz |
- 전(S07 샘플, 옛 pace): 같은 3문장 4.19 · 5.22 · 5.16 → 후: 5.48 · 5.27 · 5.78. 문장마다 생성 결과가 달라(시드) 원래 속도도 다르지만, 같은 문장 기준 약 10% 빨라짐. 품질 검사 6문장 모두 통과(ok=True)
- 이미 올린 주식 영상 4개(`stock_backup/`, ⏸ 보류)는 옛 목소리 그대로. 지금 Kaggle `all` 을 돌리면 오디오가 없는 15개 대본을 S07·H04로 만든다 — 15개 모두 사연 72~137초로 20~30초 규칙에 어긋남 → 사용자 결정 필요
- 연구·교육용, 투자 권유 아님

## 2026-10-12 — 패닉셀 영상 사연 줄이기: 스튜디오에서 자를 구간 5개, 대본·SRT·챕터를 잘라 낸 영상 기준으로 (studio_trim v1.0)

### 왜 (사용자 지시: "패닉셀 영상 오디오 편집은 되는것 같은데 사연 부분을 줄일려고 하는데 자를 부분좀 알려줘봐 그리고 대본 파일도 수정해봐")
- 패닉셀 평균 시청 약 50초인데 사연이 16문장·84초 → 대부분 진행자 설명(1:24) 전에 나감. 올린 영상은 오디오를 바꿀 수 없으므로 스튜디오 '자르기 및 컷 → 새 컷'으로 문장을 뺀다 (URL·조회수·댓글 유지)

### 고친 것
| 파일 | 함수·항목 | 내용 |
|---|---|---|
| `tools/studio_trim.py` v1.0 (신규) | `plan_cuts`, `gap_at`, `refine`, `remap`, `rewrite_txt/srt/upload`, `write_sheet`, `preview` | 뺄 문장 번호 → 스튜디오 컷 시각(원본 시간, 0.1초 단위). 컷 시작 = 앞 문장 소리 끝 뒤 + 빼는 문장 화면 전환 전, 컷 끝 = 뒤 문장 화면 전환(round(SRT×fps)) 뒤 + 소리 시작(-40 dBFS, 1샘플 단위) 전. 단위 값이 창 밖이면 소리를 지키고 '화면 N프레임' 보고. apply = 대본·SRT·upload.md 챕터(문장 번호 다시 매김)·youtube.json(chapters·chaptersBeforeTrim·studioTrim)·`studio_trim.md`. 미리보기 mp4 |
| `tools/srt_tool.py` v1.6 | `check` | 올린 영상(youtube.json)은 사연 길이를 음절 추정 대신 실측(진행자 첫 문장 시작 ≤ 30초)으로 판정 |
| `tools/make_summary.py` v1.3.3 | 오디오 줄 | 스튜디오 컷 영상은 '원본 렌더 오디오 + 컷'으로, 올린 영상에 'Kaggle에서 다시'를 안내하지 않음 |
| `tools/tts_narration.py` v1.5.1 | `cmd_check` | 올린 영상은 대본이 달라도 '다시 만든다' 안내 안 함 (`all`은 원래 올린 영상을 건너뜀 — 확인: `action=skip status=uploaded`) |
| `stock_backup/source/panicsell-2026-10/` (같은 날 다른 세션에서 `stock` → `stock_backup` 으로 옮김) | 대본 v1.3·SRT·upload.md·youtube.json·README v1.3·summary·`studio_trim.md` | 사연 5문장(원본 1·9·11·13·15), 문장 92→81 / 자막 111→100, 끝 7:43.9→6:48.4, 챕터 12개 다시 계산(0:28 진행자) |
| `guides/upload_guide.md` v1.5 (10번), `guides/README.md` v1.10 | 올린 영상 줄이기 | 순서·주의(저장한 편집은 되돌릴 수 없음, 조회수 10만 넘으면 저장 제한 가능) |

### 결과 (로그 `[CUT]`·`[STORY]`·`[SRT]`)
| 컷 | 시작 | 끝 | 길이 | 빼는 문장 | 남는 쉼 | 화면 스침 | 소리 잘림 |
|---|---|---|---|---|---|---|---|
| 1 | 0:06.1 | 0:40.6 | 34.5초 | 2–8 | 0.52초 | 1프레임 (0.01초 입력이면 40.64로 0) | 0 |
| 2 | 0:45.0 | 0:50.3 | 5.3초 | 10 | 0.50초 | 0 | 0 |
| 3 | 0:55.2 | 1:01.1 | 5.9초 | 12 | 0.53초 | 1프레임 (61.14면 0) | 0 |
| 4 | 1:07.5 | 1:11.2 | 3.7초 | 14 | 0.42초 | 0 | 0 |
| 5 | 1:18.0 | 1:24.1 | 6.1초 | 16 | 0.42초 | 0 | 0 |

- 전후: 사연 16문장·84.1초 → 5문장(읽는 음절 127), 진행자 시작 1:24.1 → **0:28.6**, 영상 7:43.9 → 6:48.4 (−55.5초). `srt_tool check --expect 81/100` ✅, 실측 진행자 시작 28.6초 ✅
- 검증: 렌더 영상의 자막 시각 = 저장소 SRT(문장 92개 차이 0.0초). 이음매 5곳 프레임(직전·직후·+0.04·+0.4초)을 미리보기에서 확인 — 컷 2 뒤 뉴스 카드가 0.3초 사라지는 모습, 컷 5 뒤 찢어진 종이 전환 아래 휴대폰 '+11%'가 0.5초 보임
- 지시사항과 다른 점: 첫 문장이 '가장 아픈 결과'가 아님(오디오를 바꿀 수 없음). 규칙대로 하려면 새로 녹음해 새 영상으로 올려야 함 → 사용자 결정
- `narration.mp3`·`tts_narration.json`·영상 코드는 원본 렌더 기록으로 둠 (다시 렌더 안 함). 연구·교육용, 투자 권유 아님. 위험 관련 값 변경 없음
- 도구 실행 예(지금 경로): `python tools/studio_trim.py plan stock_backup panicsell-2026-10 --drop … --video <렌더한 final_1080p.mp4>`

## 2026-10-12 — 사연자 남자 목소리 후보 S07·S08 (억울·자책 연기 톤), 말 속도 맞추기, 터미널에서 바로 듣기 (tts_narration v1.5)

### 왜 (사용자 지시: "오디오 코드에서 사연자 목소리를 남자로 해서 손실봐서 억울하고 자책하듯 연기톤을 설정하고 자연스럽게 속도조절해서 터미널에서 바로 들을 수 있게해")

### 고친 것
| 파일 | 함수·항목 | 내용 |
|---|---|---|
| `voices/samples/samples.json` v1.1 | 사연자 후보 | **S07** 40대 초반 남성 — 억울하다가 자책으로 가라앉는 연기 톤(낮고 살짝 허스키, 아픈 숫자 앞 한숨, 소리치거나 울지 않음) · **S08** 30대 후반 남성 — 밤에 친구에게 털어놓듯 억울함과 자책, 살짝 떨리는 중저음. 둘 다 시드 4개로 기준 소리를 골라(남성 80~170Hz) 복제, `pace` 4.2~5.2음절/초, 문장 쉼 0.55초 |
| `tools/tts_narration.py` v1.5 | `pace_ok`, `atempo`, `make_sentence` | 말 속도 맞추기: 고른 문장의 속도가 `pace` 범위 밖이면 음 높이는 그대로(ffmpeg atempo) ±15%(`max_stretch`) 안에서 늘이거나 줄임 → 다시 검사. 로그 `[PACE] rate_before rate_after factor target`, 보고서 '속도 맞춤 ×f'. `pace`는 목소리 설정 키(`VOICE_KEYS`)·식별값(`voice_ids`)·캐시 키에 들어감 → 바꾸면 그 역할 오디오를 다시 만듦 |
| 〃 | `sample_spec`, `make_samples`, `cmd_pick` | 후보의 `pace`·`gap`을 샘플에 쓰고, pick 하면 역할 설정으로 옮김. 샘플 메타에 `pace`·`pace_factors` |
| 〃 | `play`, `listen`, `cmd_listen`, `samples --play` | 터미널에서 바로 듣기: `listen S07 S08`(샘플 ID·역할 이름·파일 경로) → ffplay·afplay·mpv(wav면 paplay·aplay). 소리 장치가 없으면(ffplay는 종료 코드 0으로 바로 끝남 → 오류 문구·걸린 시간 < 길이의 50%로 판단) 경로와 Kaggle·Jupyter용 `IPython.display.Audio` 한 줄을 알려 줌 |
| `guides/tts_guide.md` v1.6 | 4-0 | 후보 표에 S07·S08, 바로 듣기·말 속도 맞추기 설명 |
| `CLAUDE.md` | 작업 지시사항 | 사연자는 남자 목소리(억울·자책 연기 톤, 자연스러운 속도) — 후보 S07·S08, `listen`으로 바로 듣기 |
| `voices/samples/storyteller/S07*`, `S08*`, `README.md` | 샘플 | 실제 모델(Qwen3-TTS 1.7B VoiceDesign → Base 복제)로 이 세션 CPU에서 만듦(11분 26초). 가짜 오디오 아님 |

### 결과 (로그 `[VOICE]`·`[TTS]`·`[PACE]`·`[SAMPLES]`)
| 후보 | 기준 소리 시도(시드: 높이 Hz·속도·결과) | 고른 기준 소리 | 미리 듣기 높이 | 속도(음절/초) | 속도 맞춤 배율(문장 1·2·3) | 문제 |
|---|---|---|---|---|---|---|
| S07 | 3401: 102·3.95·무음 1.7초 ✗ / 3402: 107·4.01 ✓ / 3403: 96·4.38 ✓ / 3404: 138·4.43·무음 1.0초 ✗ | 3402 (107Hz, 목표 115에 가장 가까움) | 108.1Hz | 4.86 | ×1.028(4.09→4.19) · ×0.994(5.23→5.22) · 그대로 | 없음 |
| S08 | 3501: 121·4.77 ✓ / 3502: 140·4.59·무음 1.6초 ✗ / 3503: 156·4.69 ✓ / 3504: 148·5.54 ✓ | 3501 (121Hz, 목표 125) | 135.6Hz | 5.06 | 그대로(세 문장 모두 4.95~5.12로 범위 안) | 없음 |
| (비교) S06 | v1.4 | - | 133.7Hz | **5.67** (빠름 — pace 없음) | - | - |

- 아직 고르지 않음: 사연자·진행자 모두 `picked` 없음 → Kaggle 셀은 계속 샘플만 만든다 (`pick S07 H01` 등을 사용자가 말하면 고정).
- 위험 관련 값(포지션·손절 등)은 바뀌지 않음 — 오디오 도구만. 연구·교육용, 투자 권유 아님.

## 2026-10-12 — 성공 사례 분석 다시: 작은 채널·최근·배수 기준 + 댓글의 시청자 니즈 (outlier_research v1.1, 주제별 data_insights v2.0)

### 왜 (사용자 지시: "유튜브 성공 사례 분석 제대로 하고 있는거 맞아? 되도록 최근에 업로드 되고 구독자수 별로 없지만 그에 비해 조회수가 잘나오는 영상들에서 어떤 내용이 들어있고 댓글 내용 등에서 시청자의 니즈가 뭐고 어떻게 해야 그게 만족되는지 파악해서 지시사항에 반영되고 있냐고 … 기존 지시사항에 묻어가는거 같은데 그것부터 다시 확인하고 문제 있으면 수정해서 주제별로 다시 분석결과 만들어봐")

### 확인한 문제 (점검 결과)
| 문제 | 근거 |
|---|---|
| 분석기 성공 사례 8개가 작은 채널 성공이 아님 | 점수의 35%가 조회수 → 구독자 204만·135만·80만 채널(배수 0.8~6) 포함. 쇼츠도 섞임(주식 8개 중 5개, 생활꿀팁 6개가 1.5분 미만) |
| 최근 영상이 아님 | 분석기 검색에 업로드 기간 제한이 없어 건강·자기계발·생활꿀팁 롱폼 가운데 나이 800~955일 → 180일 안·작은 채널 롱폼 성공 0~1개 |
| 주식 결과를 빌려 씀 | 주식 밖 5개 주제는 자막·썸네일을 못 받아 말 속도·도입부·썸네일을 "주식 결과 임시"로 씀 (주제마다 7~11곳) |
| 댓글은 모았지만 니즈 분석 없음 | 주제마다 1,200~2,100개 수집, 질문 몇 개 인용뿐 |

### 고친 것
| 영역 | 파일 | 내용 |
|---|---|---|
| 도구 | `tools/outlier_research.py` v1.1 (신규) | 기준: 최근 180일(모자라면 365·730일) · 구독자 5만 이하 · 조회수 ≥ 구독자×3 · 1만 회 이상 · 4분 이상 · 채널당 2개 → 배수 순 15개를 자세히(설명·챕터·인기 댓글 100·썸네일·자막). YouTube Data API(`YOUTUBE_API_KEY` 또는 집 PC `.env`, 할당량 한도), 4~20분·20분 넘음 둘 다 검색. `--from-existing`(키 없이 분석기 결과에서). 자막은 클라우드 IP 막힘(RequestBlocked) → 집 PC. yt-dlp 페이지 읽기는 봇 확인에 막혀 쓰지 않음(피해 가지 않음) |
| 자료 | `*/result/outliers/{candidates,outliers}.csv`, `summary.md` | 주제마다 후보·성공 사례 표. 사례 폴더(자막·댓글 원문·썸네일)는 다른 사람 것이라 .gitignore |
| 지시사항 | `guides/pipeline.md` v1.9 (1단계 4번·2단계 2번), `guides/README.md` v1.9, `CLAUDE.md`, `README.md` | 근거는 주제 자기 자료의 작은 채널 성공 사례 + 시청자 니즈. 빌리기 금지("근거 없음"이면 규칙으로 안 만듦). 분석기 success_cases는 근거로 안 씀. data_insights 필수 절(성공 사례 표·들어 있는 것·시청자 니즈·반영 표) |
| 지시사항 | `guides/script_guide.md` v2.4.1, `guides/thumbnail_guide.md` v1.3.1 | 옛 절 번호 대신 절 이름, "성공 썸네일 대부분 감정 얼굴"(주식 관찰) → 주제별 숫자(사람 있는 비율: 주식 14/15, 사연 13/15, 생활꿀팁 6/24, 우주 0/10) |
| 분석 | 6개 주제 `guides/data_insights.md` v2.0 | 0 자료와 한계 · 1 작은 채널 성공 사례 · 2 들어 있는 것(제목·길이·형식·썸네일 직접 확인) · 3 시청자 니즈(댓글을 읽고 나눔: 질문·고민·요청·칭찬·비판, 개수·좋아요·인용·"어떻게 채우나") · 4 반영 표·사용자 결정 필요 · 5 지난 판에서 고친 것 · 6 다음 수집 · 7 분석기 통계(참고) |
| 주제 규칙 | stock(script v1.6·title v1.4·thumbnail v1.3·upload v1.1), health(script v1.4·title v1.3·thumbnail v1.3·upload v1.2), space(script v1.3·title v1.2·thumbnail v1.2·upload v1.2), selfdev(script v1.3·title v1.2·thumbnail v1.2·upload v1.2), story(script v1.3·title v1.3·thumbnail v1.3·upload v1.2), lifetips(script v1.3·title v1.2·thumbnail v1.2·upload v1.1), 주제 README | 니즈에 맞춘 대본·제목·썸네일·업로드 규칙, 빌린 근거 삭제·"근거 없음" 표시. 사용자 지시(사연 20~30초, 썸네일 하단 2줄·검은 배경, 색 뜻, 합성 콘텐츠 예)는 그대로 — 데이터가 다르면 각 data_insights 4번 "사용자 결정 필요"에 |

### 주제별 성공 사례 수 (기존 자료 — 최근성은 분석기 검색의 한계)
| 주제 | 엄격 기준 성공 | 기간 | 댓글 읽은 수 | 썸네일 직접 확인 |
|---|---|---|---|---|
| stock | 30 (주제 밖 4 제외) | 365일 | 748 (성공 11개 영상, 전부 손으로 분류) | 15 |
| health | 2 (+넓힌 묶음 13·9) | 730일 | 1,243 (441 직접) | 22 |
| space | 23 | 180일 | 2,078 | 15 |
| selfdev | 5 (+넓힌 4) | 730일 | 459 (+1,592 참고) | 17 |
| story | 18 | 180일 | 1,679 (236 직접) | 15 |
| lifetips | 9 (+넓힌 24) | 730일 | 1,416 | 32 |

## 2026-10-12 — 새 주식 영상 추격 매수 (chugyeok-2026-10) — 오디오 전까지 패키지

### 왜 (사용자 지시: "다음 주제 하나 선정해서 오디오 생성 단계전까지 결과물들 만들어봐")
- 주제: `stock/guides/title_rules.md` 3번 상시 고민 "급등주 따라 샀다가 꼭대기에서 물렸어요" — 만든 4개(몰빵·물타기·빚투·패닉셀)와 겹치지 않고, 1차 제목 피드백 14번(좋음)이 이 분류
- 사연 20~30초 규칙(같은 날 바꾼 `script_guide.md` v2.4)으로 쓴 첫 대본

| 영역 | 파일 | 내용 |
|---|---|---|
| 대본 | `stock/source/chugyeok-2026-10/chugyeok-2026-10.txt`·`.srt` v1.0 | 문장 103 / 자막 120, 끝 9:23(SRT 추정 — 앞 4개 영상은 실제가 추정의 약 92%), 고지 공백 문장 20 뒤 8초. **사연 5문장·121음절 ≈ 27초, 진행자 0:25.8 시작**. `srt_tool.py check` 5항목 ✅ |
| 사연 | 같은 파일·README 검산 | 써클(CRCL) 2025: 6/5 공모가 31달러 → 6/20 종가 240.28달러에 4천만 원 매수(공모가의 7.75배) → 6/23 +386만 원 → 6/24·6/27 하루 -15.5%씩 → -996만 원 ("380만 원 → -1천만 원"). 2026-10 80달러대(README, stockanalysis). 사연자 성별은 정하지 않음(목소리를 아직 고르지 않아서) |
| 문제·방법 | 같은 파일 | 문제 4(많이 오른 뒤 값 — 순이익의 440배·주관사 목표 80달러 / 먼저 산 쪽이 판다 — 아크·8월 1천만 주 매도 / 매수가 몰린 종목의 뒤 — 로빈후드 연구 -4.7%, 금감원 테마주 72% / 서두르면 확인을 건너뜀 — 매출 99% 이자, 아문디 포모 19%) · 방법 5(얼마나·왜·누가 팔고 있는지 확인, 놓치기 싫은 몫 5%=200만 원, 소식 들은 날은 사지 않고 일주일 뒤) |
| 제목·썸네일·업로드 | `titles.md`(T1 채택 60자), `thumbnails/thumbnail_1~3.md`(v1.3 규칙: 하단 2줄, 3번 검은 배경 — 수익 380만원 빨강·손실 -1천만원 노랑), `upload.md`(합성 콘텐츠 예), `summary.md`, `README.md` | `youtube_upload.py --dry-run`: 영상 파일 없음만 |
| 공유 목록 | `stock/source/used_content.md` v1.7, `stock/guides/title_rules.md` v1.3, `stock/guides/script_rules.md` v1.5(근거 자료 은행 7줄), `stock/README.md`, `README.md` | 제작 현황·사용한 근거·다음에 피할 것(미국 주식 사연 3번, 시작 금액 4천만 원 2번, 기다리기·일부만 넣기 방법) |
- 렌더 전에 다시 확인: 문장 4 "지금도 주가는 제가 산 값의 절반이 안 돼요"(120.14달러 아래일 때 맞음)와 문장 25 "2026년 10월 80달러대" — README의 확인 절. 확인한 값: 2026-08-13 종가 75.44달러(ChartRow), 10월 80달러대는 README 출처(stockanalysis)
- 주식 4개 위 수정: `stock/guides`·`lifetips`·`story` script_rules 변경 이력 표 칸 수(4칸) 맞춤

## 2026-10-12 — 사연 20~30초 (script_guide v2.4, srt_tool v1.5) · 목소리 샘플을 듣고 고르기 (tts_narration v1.4)

### 왜 바꿨나 (사용자 지시: "패닉셀 영상이 평균 시청시간이 50초 정도되는데 20~30초 정도로 앞에 사연을 짧지만 강렬하게 하도록 지시사항 수정하고 오디오는 일단 사연자랑, 진행자 목소리 샘플을 각각 여러 개 생성하도록 수정해봐 내가 선택하면 그걸로 일관되게 하게")
- 실측(`tts_narration.json`): 패닉셀 사연 16문장·83.1초, 진행자는 1:24에 시작 → 평균 시청 50초면 대부분 진행자 설명 전에 나감. 다른 주식 영상 사연 64.7~96.0초. 사연자 속도 4.31~4.61 읽는 음절/초(쉼 포함)

| 영역 | 함수/파일 | 변경 내용 |
|---|---|---|
| 지시사항 | `guides/script_guide.md` v2.4 (0-1의 13번, 2-1) | 사연 = 5~7문장·읽는 음절 85~125(약 20~30초), 첫 문장에 결과 숫자, 진행자 0:30 전 시작, 압축 5비트 표(결과 먼저 → 행동·금액 → 결정적 장면 → 반전 확인 → 한탄)와 패닉셀 예(124음절 ≈ 28초) |
| 지시사항 | 주제 `script_rules.md` (stock v1.4, health v1.3, lifetips·selfdev·space·story v1.2) | "1분 안" → "첫 문장", story 의 사연 18~26문장 규칙 폐기 |
| 근거 | `stock/guides/data_insights.md` v1.1 10번 | 우리 영상 성과 표: 패닉셀 평균 시청 약 50초 / 사연 83초 |
| 도구 | `tools/srt_tool.py` v1.5 `story_sentences`·`story_length`·`check` | 사연 파트(라벨에 '사연') 읽는 음절이 125를 넘으면 ❌, 85 미만이면 ⚠️. 출력 `/ 사연 N문장·M음절 ≈ S초 ✅/❌` (추정 = 음절 ÷ 4.4, 패닉셀 추정 85초 vs 실측 83초) |
| 도구 | `tools/tts_narration.py` v1.4 `samples`·`pick` (신규), `design_best`(VoiceDesign 고르기 공통, `ensure_reference`가 씀), `load_samples_cfg`·`sample_ident`·`samples_status`·`make_samples`·`write_samples_readme`·`run_samples`·`unpicked_roles`, `cmd_all`·`cmd_build` 잠금 | 후보 12개(`voices/samples/samples.json`: 사연자 S01 지금 Sohee·S02~S03 Sohee 말투·S04~S06 묘사(여성 2·남성 1) / 진행자 H01 지금·H02~H06 묘사)마다 같은 문장 샘플 mp3 → `voices/samples/`. 묘사 후보는 기준 소리(시드 3개 중 높이·속도·무음 검사) → 복제로 읽어 실제 내레이션과 같은 방식. `pick S0? H0?`: current 그대로 / 화자·말투 고정 / 기준 소리를 `voices/ref/<역할>.wav`로 + clone, lock, `picked` 기록. 두 역할을 고르기 전에는 `all`이 샘플만, `build`는 멈춤. 이미 업로드한 영상은 목소리가 바뀌어도 다시 만들지 않음 |
| 설정 | `voices/samples/samples.json`(신규), `voices/samples/README.md`(자동), `voices/storyteller.json`·`host.json`(`_항목.picked`) | 후보·문장 정의, 고르는 표 |
| 지시사항 | `guides/tts_guide.md` v1.5 (3번 0단계, 4-0, 4-1, 6번), `guides/pipeline.md` v1.8, `guides/README.md` v1.8, `CLAUDE.md`, `README.md` | 목소리 고르기 순서, 사연 20~30초 |

- 시험(가짜 소리, 임시 사본 + 로컬 원격): `all --fake --push` → 후보 12개 샘플·README·커밋·push ok, 다시 실행하면 make=0 / `pick S04 H01` → 사연자 clone(기준 소리 복사·해시 확인)·진행자 그대로, 잠금 풀림, `build health prediabetes-2026-10 --fake` 성공 / `pick S02 H03` → 사연자 Sohee 말투 고정·진행자 새 기준 소리 / 바뀐 뒤 `pick S01` 거절 / 고르기 전 `build` 멈춤. 실제 모델 이름으로 본 `check`: 사연자만 바뀜, 진행자 그대로
- 지금 대본 19개 모두 사연이 67~137초라 `srt_tool.py check`에서 ❌ (주식 4개는 이미 업로드 — 고치지 않음, 나머지 15개는 사용자 결정 대기)

## 2026-10-11 — 올린 영상 통계 → 피드백 자료 (youtube_feedback v1.0 신규, youtube_auth v1.1)

### 왜 (사용자 지시: "영상을 올렸는데 관련 통계 자료들을 통해 피드백할 수 있는 자료를 만들어서 저장소에 올리는 코드도 만들어 분석은 하지말고 테스트만 해")
- 주식 영상 4개를 올렸고(2026-10-11 21:00 KST 예약 공개), 다음 영상에 반영할 근거가 될 통계를 대본 문장·챕터에 맞춰 모아 둘 도구가 없었음
- 지시사항(guides)은 바꾸지 않음. 실제 통계 수집·분석은 하지 않고 가짜 API 응답으로만 시험

| 영역 | 함수/파일 | 변경 내용 |
|---|---|---|
| 도구 | `tools/youtube_feedback.py` v1.0 (신규) `Live`·`collect`·`render_feedback`·`render_overview`·`git_push`·`run`·`check` | `youtube.json`이 있는 영상마다: Data API(공개 지표·상태·길이) + Analytics API(합계·일별·시청 지속 100점·유입 경로) + 댓글(작성자 이름 저장 안 함) → `source/<영상ID>/stats/<한국 날짜>.json`(원자료, 같은 날은 다시 안 부름) · `feedback.md`(빠진/오른 구간 → 그 시간의 대본 문장·파트·챕터, 챕터별 유지, 수집일별 추이) · `<주제>/feedback.md`(모음). `--push`는 결과 파일만 커밋 → pull --rebase → main 푸시(2·4·8·16초 다시). 공개 전 영상은 건너뜀. 예약 시각이 지났는데 비공개면 '비공개 잠김' 경고. 각 부분이 따로 실패해도 문서는 만듦. 해석은 넣지 않음. 로그 `[SCAN]·[SOURCE]·[COLLECT]·[CHECK]·[FEEDBACK]·[OVERVIEW]·[PUSH]` |
| 도구 | `tools/youtube_auth.py` v1.1 `SCOPES`·`main` | 권한에 `yt-analytics.readonly` 추가. 발급 뒤 허용되지 않은 권한(동의 화면에서 체크를 뺀 것)을 경고 |
| 시험 | `tools/tests/test_youtube_feedback.py` v1.0 (신규) | 14개: 계산(길이·표·보간·챕터 유지·빠진 구간), 키·권한별 plan, 빚투 대본·SRT 사본 + 가짜 API로 처음부터 끝까지(빠진 구간 1:32–1:36 → 문장 15·16·챕터 '사연', 같은 날 캐시, --refresh, 다음 날 추이 2줄, 작성자 이름 없음), --dry-run, 공개 전 건너뜀, 권한 없음·일부 실패, 임시 원격 저장소로 git_push(결과 파일만 커밋) |
- 시험: `python3 -m unittest discover -s tools/tests -v` → 14개 통과 (Python 3.13·3.11, 0.4초)
- 실제 키 확인(`--check`, 통계는 받지 않음): OAuth 권한 `youtube.upload` 하나뿐 → 상세 분석 불가, 공개 지표·댓글은 API 키로 가능. 상세 분석을 쓰려면 ① 업로드용 Google Cloud 프로젝트에서 "YouTube Analytics API" 사용 설정 ② PC에서 `youtube_auth.py`(v1.1) 다시 실행 — 권한 체크 칸 모두 체크 ③ 새 `YOUTUBE_REFRESH_TOKEN`을 환경 설정에
- ⚠️ 저장소가 공개라서 `--push`로 올린 통계·댓글 내용은 누구나 볼 수 있음

## 2026-10-11 — 업로드 설정 '변경되거나 합성된 콘텐츠' = 예 (youtube_upload v1.3)

### 왜 바꿨나 (사용자 지시: "합성 콘텐츠 예로 하고")
- 내레이션(사연자·진행자)이 실제 사람처럼 들리는 AI 합성 음성이고 재구성 사연을 고백처럼 읽는다. 업로드 지시사항도 "애매하면 예"였는데 시트 19개가 모두 "아니요"였음

| 영역 | 함수/파일 | 변경 내용 |
|---|---|---|
| 도구 | `tools/youtube_upload.py` v1.3 `read_synthetic`(신규)·`read_sheet`·`upload_video`·`run` | 업로드 시트 설정 표의 '변경되거나 합성된 콘텐츠' 줄(예/아니요)을 읽어 `status.containsSyntheticMedia`로 등록 (YouTube Data API, 2024-10-30 추가된 속성). 줄이 없으면 예. 로그 `[SHEET] ... synthetic=예`, `youtube.json`에 기록 |
| 산출물 | 19개 `*/source/*/upload.md` | 설정 표 그 줄을 "**예** — AI 합성 음성 내레이션"으로 |
| 지시사항 | `guides/upload_guide.md` v1.4 (6번), `guides/pipeline.md` v1.7 (4단계 4번), `guides/README.md` v1.7, `selfdev`·`space` `upload_rules.md` v1.1, `CLAUDE.md` | 합성 콘텐츠 = 예 |
- 확인: `youtube_upload.py --dry-run` (stock molppang·bittu, health prediabetes) → `synthetic=예`, 결과 "문제 없음"(주식). 판정 함수: 줄 없음 → 예, "아니요" → 아니요, "**예**" → 예
- 오디오: `tts_narration.py all --dry-run` → 19개 중 make 15(오디오 없음), skip 4(주식 4개, 지금 대본·목소리와 같음) — 다시 만들지 않음

## 2026-10-11 — 음량 -14 LUFS (loudnorm v1.0, publish v1.3.0) · 썸네일 하단 제목 2줄·검은 배경 제목형 (thumbnail_guide v1.3) · 몰빵 업로드 자료

### 왜 바꿨나 (사용자 지시: "음량 맞추고 몰빵 업로드 자료 만들고 썸네일에 보니까 짧막한 문구만 중간중간 있고 하단에 두줄의 제목 관련 문구가 없잖아 지시사항에 반영해 그리고 썸네일 중 하나는 그냥 검은 배경에 제목 문구를 잘보이도록 그대로 넣는걸로 해봐 빨간색, 노란색 강조할 부분은 강조하고")
- 음량: 렌더한 4개가 -19.7~-20.5 LUFS. 유튜브는 큰 소리만 줄이고 작은 소리는 키워 주지 않아 다른 영상보다 작게 들림
- 썸네일: 사용자가 만든 주식 썸네일 9개(beb8e1e)에 "담보 부족", "-2,500만 원" 같은 짧은 문구만 있고 무슨 일인지 알려 주는 제목 문구가 없음

| 영역 | 함수/파일 | 변경 내용 |
|---|---|---|
| 도구 | `tools/loudnorm.py` v1.0 (신규) `measure`·`normalize`·`build_filter` | 측정(ffmpeg loudnorm) → 이득 = -14 - I → 이득 더한 피크가 -1.5 dBTP를 넘으면 리미터(alimiter, 한도 -2.0 dBFS, 5ms, 지연 보정) → 결과 다시 측정(목표 ±0.3 LU, TP ≤ -1.5)·필요하면 보정해 최대 3번 → 길이 같을 때만 원본 교체. 영상 스트림 복사. 이미 기준 안이면 건너뜀. 로그 `[LOUDNESS] stage=measure/plan/pass/done` |
| 도구 | `tools/publish.sh` v1.3.0 | 렌더·오디오 확인 바로 뒤 `loudnorm.py` (실패하면 그 영상만 멈춤, 원본 렌더는 그대로) |
| 지시사항 | `CLAUDE.md`, `guides/video_guide.md` v3.6, `guides/pipeline.md` v1.6, `guides/README.md` v1.6, `README.md` | 음량 규칙(-14 LUFS·트루 피크 -1.5 dBTP 이하, 내레이션 파일은 그대로) |
| 지시사항 | `guides/thumbnail_guide.md` v1.3 (1·2·3·4·4-1·4-2·6·7번), `guides/title_guide.md` v2.1 (11번 5항), 주제별 `thumbnail_rules.md` (stock·story v1.2, health v1.2, space·selfdev·lifetips v1.1), `CLAUDE.md` | 모든 썸네일 아래쪽에 제목 문구 2줄(짝 제목 앞 문장을 줄인 것, 한 줄 14자·합 26자 이내), 위쪽 펀치 문구는 1개·10자 이내. thumbnail_3 = 검은 배경 제목형(채택 제목 앞 문장 글자 그대로 3~4줄, 흰 글자 + 노랑·빨강 강조 3곳 이하) — 대비 축은 기본에서 뺌. 빨강 뜻은 주제 규칙: 주식·사연은 손실 숫자를 빨강으로 쓰지 않음(→ 노랑) |

### 측정 (전 → 후, `python3 tools/loudnorm.py --all`, 4코어 238초)
| 영상 | 통합 음량 LUFS | 트루 피크 dBTP | LRA | 이득 | 리미터 | 길이 |
|---|---|---|---|---|---|---|
| bittu-2026-10 | -19.68 → **-14.08** | -4.49 → -1.84 | 6.4 → 6.3 | +5.68 dB | 씀 | 458.333초 그대로 |
| multagi-2026-10 | -20.48 → **-14.07** | -4.43 → -1.88 | 6.0 → 5.9 | +6.48 dB | 씀 | 472.833초 그대로 |
| panicsell-2026-10 | -19.67 → **-14.07** | -4.43 → -1.86 | 5.8 → 5.8 | +5.67 dB | 씀 | 464.933초 그대로 |
| molppang-2026-10 | -20.35 → **-14.06** | -4.46 → -1.86 | 6.1 → 6.1 | +6.35 dB | 씀 | 477.033초 그대로 |
- 영상 스트림 md5가 4개 모두 전과 같음 (화면은 그대로). 30초 시험 구간에서 원본과 처리본의 오디오 지연 0ms (교차 상관) → 자막 싱크 그대로. 같은 파일에 다시 돌리면 `stage=skip reason=이미_기준_안`

### 썸네일 프롬프트 다시 쓰기 (19개 영상, 57개 파일)
| 영역 | 파일 | 변경 내용 |
|---|---|---|
| 산출물 | 18개 영상 `thumbnails/thumbnail_1·2.md` (v1.x → 다음 버전) | 그림은 위쪽 60%로, 펀치 문구 1개(10자 이내)만 남김, 하단 제목 2줄 추가([A]에 "Bottom title" 지시, [B]는 아래쪽 빈 어두운 띠) |
| 산출물 | 18개 영상 `thumbnails/thumbnail_3.md` (v2.0) | 대비 → 검은 배경 제목형: 채택 제목 앞 문장을 글자 그대로 3~4줄, 강조 노랑·빨강 3곳 이하(주제 색 뜻대로), [B]는 편집 프로그램으로 직접(1280×720 #000000, Noto Sans KR Black 약 100px) |
| 산출물 | 18개 영상 `titles.md` (T3 줄 괄호만), `README.md`(썸네일 줄) | 짝 썸네일 3 설명을 "(검은 배경 제목형 — 채택 제목 문구)"로 |
| 이미지 | `stock/source/{bittu,multagi,panicsell}-2026-10/thumbnails/thumbnail_1~3.png` → `thumbnails/old/` | 옛 규칙으로 만든 이미지(하단 제목 없음, 3번은 대비형)를 지우지 않고 옮김 → 업로드 도구가 옛 이미지를 쓰지 않고, 요약·`thumbnail_todo.md`에 다시 만들 것으로 나옴 |
| 지시사항 | `health`·`lifetips`·`selfdev`·`space` `thumbnail_rules.md` 문구 절 | 옛 "2줄 이하, 20자 이내" → 펀치 1개·10자, 하단 2줄 한 줄 14자·합 26자 |
| 산출물 | `*/summary.md` 19개, `*/thumbnail_todo.md` 6개 주제 (5개 새로) | `make_summary.py --all`, `--thumb-todo` 다시 생성 |
- 검사(임시 스크립트): 19개 영상 × 3개 모두 통과 — 1·2번은 [A]에 하단 2줄(줄마다 14자 이내·합 26자 이내), 3번은 #000000·3~4줄·이은 글자 = 채택 제목 앞 문장(마침표만 뺌)

### 몰빵 업로드 자료 (`stock/source/molppang-2026-10/`)
- `titles.md`: T1(채택) "한 종목에만 몰빵해서 얻은 천만원 수익이 -2천만원이 됐습니다. 한 종목 올인한 사람들의 최악의 결말" (기준 제목, `stock/guides/title_rules.md` 5번), T2 속마음·공통점, T3 짧은 변형(CEO 이적 소식)
- `thumbnails/thumbnail_1~3.md` (v1.3 규칙: 계좌 카드 +1,000만 원 → -2,000만 원 / 가상 인물 / 검은 배경 제목형)
- `upload.md`: 설명란·챕터 12개(오디오에 맞춘 SRT 시각)·태그 15개·고정 댓글·투자 유의 사항·출처. `youtube_upload.py --dry-run` 결과 "문제 없음". 블룸버그 2022-02-11 링크는 검색 결과로 기사 제목·주소 확인("두 명만 매도 의견")
- `stock/README.md`·`README.md` 몰빵 줄 갱신

## 2026-10-11 — Kaggle 내레이션으로 영상 4개 렌더 + 요약 상태표 오류 수정 (make_summary v1.3.2)

### 왜 바꿨나 (사용자 지시: "오디오 만들어졌는지 확인하고 잘됐으면 영상 만들어")
- 4개 영상(bittu·multagi·panicsell·molppang)의 `narration.mp3` 확인: `tts_narration.py check` 모두 ok, 보고서상 다시 할 문장 0, 진행자 목소리 높이 135~138Hz로 영상마다 같음
- 자막은 align-audio v1.2(`tts_narration.json`의 문장 시각)로 맞춘 뒤 렌더. 몰빵은 영상 코드가 없어서 새로 만듦 (`video/CHANGELOG.md`)

| 영역 | 함수/파일 | 변경 내용 |
|---|---|---|
| 도구 | `tools/make_summary.py` v1.3.2 `build` 상태표 | 썸네일 줄이 프롬프트 파일이 없어도 "프롬프트 3개 ✅"로 나오던 오류 → `thumbnails/thumbnail_N.md` 개수를 세서 3개가 아니면 "❌ 프롬프트 n/3". 다른 영상 3개는 결과 같음(생성 시각 줄만 다름) |
| 산출물 | `stock/source/molppang-2026-10/summary.md` (신규) | 몰빵 요약: 제목·썸네일 프롬프트·업로드 시트가 아직 없다고 표시 (업로드 전에 필요) |
| 렌더(커밋 안 함) | `stock/out/<영상ID>/final_1080p.mp4` | bittu 7:38, multagi 7:53, panicsell 7:45, molppang 7:57. 통합 음량 약 -20 LUFS. 유튜브 키가 없어 업로드는 건너뜀 |
## 2026-10-11 — 주식 밖 5개 주제: 분석 → 주제 규칙 → 영상 3개씩 패키지(오디오 전까지)

### 왜 (사용자 지시)
- "주식을 제외한 나머지 건강, 우주 등 주제도 분석기 돌려서 오디오 전까지 3개까지 만들어봐" → 주제마다 최대 3개 (사용자 선택)

### 1단계 분석 (클라우드, `bash tools/run_analysis.sh <주제> -- --keywords 13 --skip-install`)
| 주제 | 쿼터 | 수집 | 비고 |
|---|---|---|---|
| health · space · selfdev · story · lifetips | 1,958 · 1,782 · 1,920 · 1,990 · 2,006 (합 9,656 / 하루 10,000) | 주제마다 키워드 13개(설정 48개 중, 카테고리 순환) | 남은 키워드는 다음 실행에서 (검색 7일 캐시) |
- 클라우드 네트워크 정책으로 `suggestqueries.google.com`(자동완성 수요), `www.youtube.com`(자막·쇼츠 확인), 썸네일 이미지가 막힘 → 수요 점수 0, 성공사례 대본·썸네일 없음. 각 주제 `guides/data_insights.md`에 한계로 적고 말하기 속도·도입부·썸네일은 주식 결과를 임시로 씀

### 2단계 주제 규칙 (각 `<주제>/guides/`, `README.md`, `source/used_content.md`, `voices/storyteller.json`)
- health v1.1~1.2(분석 반영, 1900년대 자료 DPP는 사용 불가), space·selfdev·lifetips v1.0~1.1(새로 만듦), story v1.0~1.2(대본 규칙 새로 만듦)
- 건강·사연 README의 ⏸ 보류 해제 (보류 조건이 "분석 결과 전까지"였음) → 내레이션 도구가 이 주제들도 읽음
- 주제마다 사연자 말투만 덮어쓰는 `voices/storyteller.json` (공통 instruct가 "주식 손실 고백"이라). 화자 Sohee·진행자 기준 목소리는 그대로

### 3단계 영상 패키지 15개 (각 `<주제>/source/<영상ID>/`: 대본 TXT·SRT·README(검산·출처)·제목 3개·썸네일 프롬프트 3개·업로드 시트·요약)
| 주제 | 영상ID (추정 길이) |
|---|---|
| 건강 | prediabetes-2026-10 v1.1 (9:03, DPP → 영국 NDPP·독일 PLIS 2023) · supplement-liver-2026-10 (11:48) · sarcopenia-2026-10 (10:18) |
| 우주 | nuriho-2026-10 (11:52) · voyager-2026-10 (12:14) · asteroid-2026-10 (12:28) |
| 자기계발 | miraclemorning-2026-10 (11:01) · habit21-2026-10 (10:37) · dopaminedetox-2026-10 (11:57) |
| 사연 | myeoneuri-2026-10 (12:14) · jeungyeo-2026-10 (12:20) · chayongjeung-2026-10 (11:13) |
| 생활꿀팁 | washer-2026-10 (8:39) · heater-2026-10 (8:43) · bleach-2026-10 (8:29) |
- 15개 모두 `srt_tool.py check` 4항목 ✅, `tts_narration.py all --dry-run`에 15개 모두 "오디오 없음 → make"로 잡힘
- 읽는 소리 사전 `tts_lexicon.tsv`: health(kg·범위 물결표), selfdev(범위 물결표), 영상별(H3·2024 YR4·119·AST/ALT 등) — TTS에만 쓰고 대본·자막은 그대로
- 확인하지 못한 숫자는 쓰지 않음: 예) 근감소증 '50~64세 의자 일어서기 10초'(출처마다 10/12초) → 확인된 12초 기준으로, 소행성 생존 용품 230만 → 150만 원(가격 확인분만)
- 이 환경은 WebFetch·curl로 원문을 열 수 없어 모든 근거를 웹 검색 결과의 인용으로 확인 — 각 README 출처 표에 확인 방법을 적음

### 다음
- 사용자: Kaggle 셀 하나(`python tools/tts_narration.py all --push`, `guides/tts_guide.md` 3번) → 15개 오디오가 대본 폴더마다 main에 올라감 → "오디오 올렸어" → 4단계(영상 코드·렌더·비공개 업로드, 한 번에 최대 3개)
- 썸네일 이미지는 사용자가 각 `thumbnails/thumbnail_N.md`의 [A] 프롬프트로 이미지 AI에서


## 2026-10-11 — 진행자는 중저음 남성, 모든 대본에서 같은 목소리 (tts_narration v1.3)

### 왜 바꿨나 (사용자 지시)
- 진행자 목소리는 중저음의 남성이지만 적당히 귀에 쏙쏙 들어오고 신뢰도 높은 목소리로, 그리고 대본마다 달라지면 안 된다
- 문제: 지금 모델(CustomVoice)의 한국어 원어민 화자는 여성 Sohee 하나뿐 (남성 화자는 외국인 억양). 패키지 소스(`qwen-tts` 0.1.1)로 확인한 방법: VoiceDesign `generate_voice_design(text, instruct, language)` → Base `create_voice_clone_prompt(ref_audio=(wav, sr), ref_text)` + `generate_voice_clone(..., voice_clone_prompt)`

| 영역 | 함수/파일 | 변경 내용 |
|---|---|---|
| 도구 | `tools/tts_narration.py` v1.3 `QwenPool` (QwenEngine 대체) | 모델 세 가지를 필요할 때 불러옴: 사연자 CustomVoice(GPU 0), 진행자 Base 복제(GPU 1), 기준 목소리 만들기 VoiceDesign(한 번만, 끝나면 내림). GPU 하나면 번갈아 올림. 복제 프롬프트는 기준 목소리마다 한 번 |
| 도구 | 같은 파일 `ensure_reference`, `voice` 명령 | `voices/ref/host.wav`가 없으면 `voices/host.json`의 design 묘사로 시드 6개 만들어 검사(목소리 높이 85~150Hz, 110Hz에 가깝게, 속도 3.8~6.0음절/초, 무음 1초 이하) → 고른 것을 `voices/ref/host.wav`·`host.json`(해시 포함)로 저장하고 main에 올림. 범위 밖뿐이면 멈춤, 못 올리면 오디오를 만들지 않음 |
| 도구 | 같은 파일 `f0_median`(신규), `make_sentence` | 목소리 높이(기본 주파수) 측정: 40ms 구간 FFT 자기상관, 큰 소리·주기가 뚜렷한 구간 중간값. 진행자 문장이 기준 ±30% 밖이면 다시(최대 3번), 보고서에 문장마다 높이 |
| 도구 | 같은 파일 `load_voices`(lock·engine·clone 검사), `attach_reference`(해시 검사), `voice_ids`, `voice_mismatch`, `repo_status`, `cmd_check` | 진행자 `lock`: 주제·영상 덮어쓰기·명령줄 값 무시. 오디오마다 목소리 정체(모델·기준 목소리 해시·설정)를 남기고, 바뀌면 "다른 목소리"로 다시 만듦 (v1.2 이하 오디오도 다시). `--split`은 복제 모델이 있으면 막음(한 프로세스가 GPU 2개) |
| 설정 | `voices/host.json` v2.0, `voices/storyteller.json` v1.2 | 진행자: engine clone, lock, design(30대 후반 남성, 따뜻한 중저음 바리톤, 뉴스 앵커·다큐 내레이터처럼 신뢰감, 또렷한 발음, 숫자에 힘, 보통 속도 / 기준 문장 49음절 약 10초). 사연자: engine custom_voice(그대로 Sohee) |
| 도구 | `tools/publish.sh` v1.2.2 | 건너뜀 표시: 옛 대본·목소리로 만든 오디오 |
| 지시사항 | `guides/tts_guide.md` v1.4(1번 모델 표, 4-1), `guides/pipeline.md` v1.5, `guides/README.md` v1.5, `CLAUDE.md`, `README.md` | 진행자 목소리 규칙과 바꾸는 법 |

### 검증 (가짜 소리, 로컬 시험용 원격 저장소)
- 높이 측정: 110Hz 톱니파 → 110.1Hz, 120Hz+잡음 → 120.0, 220Hz → 220.2, 무음 → 0. 9초 소리 한 번 약 26ms
- 첫 실행: 기준 목소리 시도 6번(198·123·175·99·152·76Hz) → 범위 안 3개 중 110Hz에 가까운 99Hz 선택 → `voices/ref/host.wav` 커밋·푸시 → 빚투·패닉셀 진행자 문장 모두 같은 기준(해시 같음), 문장 높이 97~105Hz
- 다시 실행: 둘 다 "지금 대본·목소리와 같음"으로 건너뜀 / 주제 폴더에 진행자 덮어쓰기 파일 → lock으로 무시, check ok
- 기준 목소리를 바꿈(design 시드 변경 + `voice --force --push`) → 두 영상 `check` ok=False "목소리:host", `publish.sh`가 건너뜀 → `all --push`가 둘 다 새 목소리로 다시 만들어 올림(두 영상 기준 해시 같음)
- `--split` 막음, `--assemble-only` 캐시로 잇기 정상
- 실제 남성 목소리는 Kaggle 첫 실행에서 만들어짐 (이 환경은 모델을 받을 수 없음)

## 2026-10-11 — Kaggle 셀 `git pull` 오류 해결 (tts_narration v1.2.1, tts_guide v1.3.1)

- 증상: `error: Your local changes to the following files would be overwritten by merge: tools/publish.sh`
- 원인: Kaggle의 저장소 사본에서 `tools/publish.sh`의 실행 권한(파일 모드 100755)만 바뀐 상태 → main의 같은 파일이 바뀌자(v1.2.1 주석) `git pull`이 합치지 못하고 멈춤. 같은 상황을 재현해 확인(실행 권한을 뺀 사본 + 한 커밋 뒤 → pull 이 같은 오류)
- 셀: `git pull` → `git config core.fileMode false && git fetch -q origin main && git reset -q --hard origin/main` (사본을 main과 똑같이). 재현한 사본에서 깨끗하게 최신(43c7e9c)으로 맞춰짐
- `tools/tts_narration.py` v1.2.1 `Git.run`: 모든 git 실행에 `core.fileMode=false`. `push_preflight`: 사본의 다른 변경 파일을 경고로 알림(커밋하지 않음)
- 올리기가 실패해 사본에만 남은 커밋이 reset으로 지워져도 결과는 `tts_out/upload/`에 남아 다음 `all --push`가 다시 올림 (시험으로 확인)

## 2026-10-11 — 오디오는 하나로(고르지 않음), 결과는 Kaggle에서 대본 폴더마다 GitHub에 자동으로 (tts_narration v1.2)

### 왜 바꿨나 (사용자 지시)
1. 오디오를 고르지 말고 그냥 하나로
2. 결과 파일을 GitHub에 올리도록 — 오디오는 대본별 폴더에 각각

| 영역 | 함수/파일 | 변경 내용 |
|---|---|---|
| 도구 | `tools/tts_narration.py` v1.2 — `cmd_sample`, `SAMPLE_STYLES`, `preset`, `--story-style/--story-instruct` 삭제 | 말투 시험·선택 단계 없음. 역할마다 설정 파일의 말투 하나 |
| 도구 | 같은 파일 `build_episode` | 역할만 이은 트랙(`storyteller.mp3`·`host.mp3`) 삭제 → 결과 오디오는 영상마다 `narration.mp3` 하나. 보고서는 `tts_report.md`로 결과 옆에. mp3를 못 만들면 멈춤 |
| 도구 | 같은 파일 `get_token`, `Git`, `push_preflight`, `push_results`, `cmd_push` (신규), `all/build --push`, `push` 명령 | 영상 하나가 끝날 때마다 결과 3개(`narration.mp3`·`tts_narration.json`·`tts_report.md`)를 **그 영상의 대본 폴더** `<주제>/source/<영상ID>/`에 복사 → 그 파일만 커밋 → `pull --rebase --autostash` → `push origin HEAD:main` (최대 4번, 2·4·8·16초 간격). 토큰은 환경 변수 또는 Kaggle Secrets `GITHUB_TOKEN`, `GIT_ASKPASS`로만 넘김(로그·명령줄·원격 주소·설정에 없음, 출력은 가림). 시작 전 `push --dry-run`(없는 브랜치 이름)으로 권한 확인 → 안 되면 GPU 쓰기 전에 멈춤. 두 프로세스(`--split`)는 잠금 파일로 차례로. 안전장치: 옛 대본 결과·저장소의 더 나중 결과는 안 올림, 가짜 소리는 github.com에 안 올림, 다른 확장자 옛 내레이션은 지움 |
| 설정 | `voices/storyteller.json`·`host.json` v1.1 | `preset` 삭제 |
| 지시사항 | `guides/tts_guide.md` v1.3, `guides/pipeline.md` v1.4, `guides/README.md` v1.4, `CLAUDE.md`, `README.md`, `tools/make_summary.py` v1.3.1(문구), `tools/publish.sh` v1.2.1(주석) | Kaggle 셀 하나, GitHub 토큰 만들기(이 저장소만·Contents 읽기/쓰기·Kaggle Secrets), 문제가 생겼을 때 표, zip·웹 업로드는 마지막 수단 |

### 검증 (가짜 소리, 로컬 시험용 원격 저장소 — 실제 GitHub에는 올리지 않음)
- 전후 비교 (빚투, `--fake`): v1.1 mp3 내보내기 3개(narration + 역할 트랙 2) 18.2초 → v1.2 1개 8.2초. 문장 시각·역할(사연자 1–16 / 진행자 17–88)·쉼 구성은 v1.1과 같음
- `all --push`: 빚투·패닉셀 영상마다 커밋 1개, 각 커밋에 그 대본 폴더의 3파일만 → 원격이 앞서 있어도 rebase 후 push 성공. 다시 실행하면 둘 다 has_audio로 건너뜀, `check` ok=True, `publish.sh --dry-run` 후보 2개
- 거부(pre-receive) → 4번 다시 시도 후 ok=False·종료 1 → 원격이 받아 주자 `push`가 남아 있던 커밋을 올림
- `--split 0/2·1/2` 동시 실행 → 두 영상 모두 올라감(잠금)
- 얕은 clone(`--depth 1`, Kaggle 셀과 같음)이 원격보다 뒤처져 있어도 올라감
- 가드: 가짜 소리 + github.com 원격 → 멈춤 / 토큰 없음 → 모델을 불러오기 전에 멈춤 / 옛 대본 결과 → 안 올림 / 저장소에 더 나중 결과 → 안 덮어씀 / 로그에 토큰 문자열 0회
- 실제 모델 음성·실제 GitHub 올리기는 Kaggle에서 처음 실행

## 2026-10-10 — 사연자·진행자 두 목소리, 대본 전부 한 번에 오디오, 스토리보드 삭제, 사례는 최신으로 (tts_narration v1.1)

### 왜 바꿨나 (사용자 지시)
1. 요약에 스토리보드까지 하라고 했는데 그건 하지 말고, 오디오가 만들어지면 그냥 영상을 만든다 (승인 단계 없음)
2. 대본에서 사연자와 진행자 파트를 나누고, 역할마다 목소리 톤 설정 파일을 만들고, 역할마다 정해진 경로에 오디오가 생기게
3. 대본이 생성된 파일들을 모두 읽고 오디오가 생기게
4. 대본 4개의 사례는 되도록 최신 사례로 — 1900년대는 너무 옛날
5. 오디오 생성 코드를 실행하는 코드(Kaggle 셀)를 알려 주고, 말한 내용을 모두 지시사항에 반영

| 영역 | 함수/파일 | 변경 내용 |
|---|---|---|
| 도구 | `tools/tts_narration.py` v1.1 `load_voices`, `role_of`, `instruct_for`, `plan_items` | 역할 = 목소리 설정 파일 `voices/<역할>.json`. 파트 라벨에 `parts` 낱말('사연')이 있으면 사연자, 없으면 `"*"` 역할(진행자). 주제·영상 폴더의 같은 이름 파일이 덮어씀. 역할별 문장 범위·말투를 `[ROLE]`·`[STYLE]` 로그로, `plan.ts`의 `STORY_LAST`와 사연자 끝 번호 비교 |
| 도구 | 같은 파일 `build_episode` | 정해진 경로: `OUT/upload/<주제>/source/<영상ID>/narration.mp3`+`tts_narration.json`(저장소와 같은 경로), 역할별 `OUT/<영상ID>/<역할>/S###.wav`·`<역할>.mp3`. 문장 사이 쉼은 역할 설정 `gap` |
| 도구 | 같은 파일 `cmd_all`, `discover`, `pack`, `cmd_check` (신규) | `all`: 저장소의 대본(`*/source/<id>/<id>.txt`)을 모두 읽어 할 일 표 → 모델 한 번 불러 차례로 만들고 zip. 건너뜀: 보류 주제(⏸)·업로드한 영상·지금 대본 오디오가 있는 영상. 옛 대본 오디오는 다시 만듦(`--keep-stale`로 끔). GPU 2개 `--split 0/2·1/2` → `pack`. `check`: 저장소 오디오가 지금 대본으로 만든 것인지(대본 해시·바뀐 문장 번호) |
| 도구 | 같은 파일 `QwenEngine`, `cache_key` | 화자·생성 설정을 문장마다(역할 설정) 넘김. 캐시 키는 v1.0과 같은 모양(기본 설정이면 v1.0 캐시 그대로). `--out-dir`은 결과 최상위 폴더로 |
| 설정 | `voices/storyteller.json`, `voices/host.json` (신규) | v1.0의 말투 그대로 옮김: 사연자 = 억울·후회 고백, 진행자 = 차분한 진행 + `part_instruct`(분석·방법 = 또렷한 설명, 마무리 = 따뜻한 인사). Sohee, 시드 1234, 쉼 0.45초 |
| 도구 | `tools/make_summary.py` v1.3 | 스토리보드 절·상태 줄 삭제 → "내레이션 역할"(사연자 1–16 · 진행자 17–88)·"영상 코드" 상태, 대본 파트마다 🎙 역할, 오디오가 옛 대본이면 ⚠️. `--all`은 보류 주제 건너뜀 |
| 도구 | `tools/publish.sh` v1.2 | 스토리보드 단계 삭제. `tts_narration.json`이 있으면 `check`로 옛 대본 오디오를 건너뜀. 영상 코드가 없으면 "Claude가 만든 뒤 다시(승인 대기 없음)" |
| 대본 | 몰빵 v2.1 (문장 40~43, 45~47) | 베셈바인더(1926~2016년 미국 주식) → 자본시장연구원 2024(2023년 말까지 10년 국내 상장사 52%가 1년짜리 안전한 채권보다 못 벎, 대형주 58%)·한국경제 2026(코스피가 두 배 넘게 오른 6월까지 지수를 이긴 종목 4% 미만). JP모건(1980년 이후) → 엔씨소프트·LG생활건강 2021년 고점 대비 -70% 넘게·5년 넘게 회복 못 함·그사이 코스피 2배. 카카오는 물타기에 써서 뺌. 문장 51 손실 회피 출처를 2024 메타분석(JEL)으로. 자막 117 → 116 |
| 대본 | 패닉셀 v1.1 (문장 80~85) | 탈러 등 1997년 실험 → 자본시장연구원 2021(2020년 개인투자자 20만 명: 신규 투자자 거래 두 배 가까이, 비용 뺀 수익률 기존 15% vs 신규 -1.2%, 자주 사고팔수록 시장보다 덜 벎). 자막 109 → 111, 정리 챕터 8:01 → 8:09 |
| 대본 | 물타기 v1.4 (문장 41~45, 49~55) | 오딘 1998(1987~1993년 계좌) → 자본시장연구원 2022(2020년 개인 약 20만 명: 산 다음 날 수익 종목 41% vs 손실 종목 22% 매도, 처분효과 최강 그룹 -9.8% vs 손실부터 정리한 그룹 +4.9%). 베어링스 은행 1995 → 카카오 2021~2026(빅테크 규제 주간 개인 1조 원 넘게, 2022년 2조 원 넘게 순매수, 소액주주 206만 명, 2026-10 3만 2천 원대 = 고점의 5분의 1 미만). 자막 110 → 107, 챕터 4:23부터 다시 계산 |
| 지시사항 | `guides/pipeline.md` v1.3, `guides/README.md` v1.3, `guides/video_guide.md` v3.5, `guides/tts_guide.md` v1.2, `guides/script_guide.md` v2.3, `stock/guides/script_rules.md` v1.3, `CLAUDE.md`, `README.md` | 3단계에서 영상 코드·스토리보드·승인 삭제 → 4단계 0번(오디오가 생기면 Claude가 영상 코드, still 자체 점검, 바로 렌더). 3-6 내레이션(역할·설정 파일·`all`·zip·GitHub 웹 올리기). 사례는 되도록 최신(2020년대 먼저, 1900년대 사건·자료 쓰지 않음). Kaggle 셀 4개 |

### 검증
- `--fake`(가짜 소리) 빚투: 사연자 16문장(1–16)·진행자 72문장(17–88), `plan.ts` STORY_LAST=16 일치. 쉼 구성은 v1.0과 같음(문장 83·파트 3·카드 1·끝 1), 555.45초. `npm run align-audio --dry-run`이 고지 카드 쉼 7.98초를 찾고 자막 105개를 맞춤
- `all --split 0/2`·`1/2` 동시 실행 → 4개 영상(빚투·몰빵·물타기·패닉셀) 각각 made, 보류 주제(건강) 건너뜀 → `pack` zip 8개 파일 45.6MB → 다시 `all --dry-run`은 4개 모두 done
- `check`: 같은 대본 ok=True(종료 0) / 대본 해시·문장 52 바꾼 메타 → ok=False changed=52(종료 1), `all`은 stale로 표시. `publish.sh --dry-run`이 옛 대본 오디오를 건너뜀
- `--assemble-only`(88/88 캐시), `--redo 12,15`(사연자 2문장만 시도 2), `--shard 0/2·1/2` → `--assemble-only` 92문장, `sample --roles`(대본·내장 문장), `sample --story-style B`
- 실제 모델 음성은 이 환경에서 만들 수 없음(Hugging Face 차단) → Kaggle에서 사용자가 실행

## 2026-10-10 — 내레이션 만들기: 오픈소스 음성 AI(Qwen3-TTS)를 Kaggle에서 (tts_narration v1.0)

### 왜 바꿨나 (사용자 지시)
1. edge-tts는 너무 어색하다 → 오픈소스 음성 AI로 자연스럽게
2. Kaggle에서 돌아가는 코드로
3. 사연은 주식 손실로 억울하고 후회하는 톤으로

| 영역 | 함수/파일 | 변경 내용 |
|---|---|---|
| 도구 | `tools/tts_narration.py` v1.0 (신규) | Qwen3-TTS 1.7B CustomVoice(Apache-2.0, 한국어 화자 Sohee) + 파트별 말투 지시(`STYLES`: 사연=억울·후회, 진행자·분석·마무리=차분한 설명). `sample`(말투 A~D 비교) / `build`(대본 → `narration.mp3` + `report.md`) |
| 도구 | 같은 파일 `read_script` | 문장·카드 판정은 `srt_tool.parse_txt`·`parse_cards`를 그대로 씀(결과가 다르면 멈춤) |
| 도구 | 같은 파일 `make_sentence`, `check` | 문장마다 검사(말 속도 2.5~8음절/초, 문장 안 무음 1.8초 이하, NaN·빈 소리) → 시드를 바꿔 최대 3번, 통과 못 하면 가장 나은 것 + "귀로 확인" 표시. 문장 파일 캐시(글·말투·화자·설정이 같으면 재사용), `--redo`는 새 시드 |
| 도구 | 같은 파일 `cmd_build` 잇기 | 문장 사이 0.45초·파트 1.0초 무음, 고지 카드 자리 4~8초(`parse_cards` 길이, 최소 3.5초 규칙), 첫 문장 앞 0.3초. 볼륨은 전체 이득 하나(RMS −18dBFS, 최고점 −1dBFS) |
| 도구 | 같은 파일 `tts_text` | TTS 입력만 `-800만` → "마이너스 800만", `+55만` → "플러스 55만" (대본·자막은 그대로), 선택 사전 `tts_lexicon.tsv` |
| 도구 | 같은 파일 `QwenEngine` | T4(연산 능력 7.5)는 float32 기본(bfloat16 장치 없음, float16은 NaN 위험), A100 등은 bfloat16. GPU 2개 나눠 만들기 `--shard 0/2·1/2` + `--assemble-only` |
| 지시사항 | `guides/tts_guide.md` v1.1 (신규, v1.1: 셀에 도구 파일을 붙여 넣지 말 것·한 셀 시험),  `guides/pipeline.md` v1.2, `guides/README.md` v1.2, 저장소 `README.md` | Kaggle 셀 4개(설치 → 말투 시험 → 전체 → 듣기·내려받기), 도구 규칙, 말투 바꾸는 법 |

### 검증
- 모델 API: `qwen-tts` 0.1.1 패키지 소스로 확인 — `Qwen3TTSModel.from_pretrained`, `generate_custom_voice(text, speaker, language, instruct, **generate kwargs)`, 출력 24kHz(24000 ÷ 1920 = 초당 12.5 프레임), 0.6B는 instruct 무시
- 이 작업 환경에서는 Hugging Face 접속이 막혀(403) **실제 모델 음성은 만들지 못함** → Kaggle에서 사용자가 `sample` 실행 필요
- `--fake`(가짜 소리)로 패닉셀 대본 전체: 문장 92개, 9분 23초 mp3 11.3MB. `npm run align-audio`(임시 SRT로)가 고지 카드 쉼 7.97초를 찾고 자막 109개를 맞춤, `srt_tool check` ✅. 문장 92개 시작 시각이 도구 기록과 최대 0.11초 차이
- 캐시: 두 번째 실행은 생성 0개 / `--redo 12,15`는 그 2문장만 새 시드(시도 2) / `--shard 0/2·1/2` 46개씩 → `--assemble-only` 92개 / `--story-style B`는 사연 문장만 다시
- 검사·재시도: 1회차 너무 김+무음 2.9초 → 2회차 NaN → 3회차 통과 / 3번 모두 너무 빠름 → 3회차를 쓰고 `report.md` "귀로 확인할 문장"에 표시 / 생성 오류 1번 → 2회차 통과

## 2026-10-10 — 전체 진행 순서(pipeline)와 자동화 도구 · 분석기 v2.3.1

### 왜 바꿨나 (사용자 지시)
1. 분석 결과가 없으면 분석기를 돌리고 → 결과로 지시사항·주제 탐색 → 제목 3개·썸네일 프롬프트 3개·업로드 정보·대본 → 영상별 요약 문서 → 오디오가 생기면 렌더·유튜브 비공개 업로드(최대 3개, 제목·썸네일 등록)
2. 썸네일은 프롬프트 파일만 만든다 (이미지는 다른 이미지 AI가 만든다)
3. 앞으로 main에 바로 올린다 (`CLAUDE.md`)

| 영역 | 함수/파일 | 변경 내용 |
|---|---|---|
| 분석기 | `youtube_topic_analyzer.py` v2.3.1 `load_keys` | `.env`가 없어도 환경변수 `YOUTUBE_API_KEY`가 있으면 실행 (클라우드). 없으면 예전처럼 템플릿 생성·종료 |
| 도구 | `tools/run_analysis.sh` v1.0 (신규) | 클라우드 분석: `--no-push --no-video --no-open` → `output/<주제>/result` → `<주제>/result` 복사 (영상·음성 제외) |
| 도구 | `tools/youtube_auth.py` v1.0 (신규) | 사용자 PC에서 한 번: OAuth(PKCE·루프백)로 업로드용 리프레시 토큰 발급 |
| 도구 | `tools/youtube_upload.py` v1.1 (신규) | upload.md 기준 비공개 업로드(이어 올리기), 챕터를 지금 SRT로 재계산, 한국어 자막, 채택 제목의 짝 썸네일 1개(1280×720·2MB 이하 JPG로 자동 변환), `youtube.json` 기록, `--dry-run`·`--check-auth` |
| 도구 | `tools/make_summary.py` v1.0 (신규) | 영상별 `summary.md`(상태·제목 3개·썸네일 프롬프트·설명란·태그·고정 댓글·스토리보드·대본), `--thumb-todo`로 이미지 없는 썸네일 프롬프트 모음 |
| 도구 | `tools/publish.sh` v1.0 (신규) | 4단계: 오디오(`narration.*`)가 있고 아직 안 올린 영상 → align-audio → 타입 검사 → 스토리보드 → 렌더(길이·오디오 확인) → 업로드 → 요약 문서, 최대 3개 |
| 지시사항 | `guides/pipeline.md` v1.0 (신규), `guides/README.md` v1.1, `upload_guide.md` v1.2(9번 API 업로드), `thumbnail_guide.md` v1.2(프롬프트만), `video_guide.md` v3.4(8·9번), `script_guide.md` v2.2(5-4), 저장소 `README.md`, `CLAUDE.md` | 전체 순서·키 설정·Claude에게 하는 말 예시, 비공개 잠금·테스트 및 비교 제약 |

### 검증
- `load_keys`: .env 없음 + 환경변수 키 → 계속 진행(.env 안 만듦) / .env 없음 + 키 없음 → 템플릿 생성·종료
- `run_analysis.sh`: 가짜 분석 결과로 복사 확인 (mp4 제외)
- `youtube_upload.py`: 실제 시트 3개 `--dry-run` 통과(챕터 12개 재계산, 태그 93~113자). 로컬 가짜 API로 전 과정: 20MB 이어 올리기, 자막 110개, 1536×1024 PNG → 1280×720 JPG 변환·등록, `youtube.json`, 재실행 시 건너뜀
- `publish.sh --dry-run`: 오디오 없음 → 대상 0 / 가짜 오디오 → 물타기 대상, 빚투는 "영상 코드 없음"으로 제외. 렌더 명령은 30프레임으로 확인
- 실제 유튜브 업로드는 키가 아직 없어 하지 못함

## 2026-10-09 — 새 주제 설정 파일 5개 (분석기 코드는 v2.3.0 그대로)

| 폴더 | 주제 | 내용 |
|---|---|---|
| `selfdev/analyzer_config.toml` | 자기계발 | 검색어 48개(무기력·번아웃 / 미루기·습관 / 도파민 중독 / 루틴·갓생 / 나이대·직장인 / 자존감·성공 습관) |
| `health/analyzer_config.toml` | 건강 | 검색어 48개(혈당·당뇨 / 간·혈압·콜레스테롤 / 검진·나이대 / 영양제·약 / 노화·통증 / 습관·몸의 신호) |
| `space/analyzer_config.toml` | 우주 | 검색어 48개(사고·실화 / 미스터리 / 크기·끝·탄생 / 탐사 / 뉴스·위험 / 다큐 포맷), 동음이의어 제외(우주소녀·로켓배송·화성시 등) |
| `story/analyzer_config.toml` | 사연을 통한 교훈 | 검색어 48개(가족 갈등 / 돈·배신·결혼 후회 / 인생 후회 / 인간관계 / 사연 포맷 / 사이다·감동) |
| `lifetips/analyzer_config.toml` | 생활꿀팁 | 검색어 48개(난방·전기 절약 / 곰팡이·냄새 / 청소 / 정리·살림 / 자취·이사 / 겨울 안전·상식), '청소년'·'대표이사' 제외 |

- 근거: 2026-10-09 YouTube 자동완성(쿼터 0) — 씨앗 검색어 250개를 조회해 실제로 이어지는 표현만 골랐다. 단독 주제어("우주", "사연", "자기계발")는 채널·노래·게임 이름이 섞여 넣지 않았다.
- 모두 `KEYWORD_MODE = "curated"`. "both"로 바꿀 때 쓰도록 자동완성 제외어(`EXCLUDE_KEYWORDS`)도 넣어 둠.
- 검증: 분석기 `apply_config_file`로 5개 모두 로드(모르는 설정 0개), 검색어 240개 중복 0개, `topic_relevance`로 검색어 240개 모두 관련 판정, 미끼 제목 22개(예: "우주소녀 다영 직캠", "청소년 상담 사례", "양파 채썰기") 모두 무관 판정.

## 2026-10-09 — 영상 제작 도구 (분석기는 v2.3.0 그대로)

### 왜 바꿨나 (사용자 지시: "일단 그냥 영상 만들어봐", "업로드 템플릿을 지시사항에 추가해서 만들어")

| 영역 | 함수/파일 | 변경 내용 |
|---|---|---|
| 도구 | `tools/srt_tool.py` v1.1 `export_remotion`, `parse_cards` | 대본의 `[장면]` 고지 카드 위치·길이(글자 수 ÷ 7 + 1초, 4~8초)와 자막을 영상용 `subtitles.ts`로 내보내기 |
| 도구 | `tools/srt_tool.py` v1.2 `video_times`, `export_upload` (신규) | 업로드용 SRT(고지 카드만큼 뒤 자막을 밂) + `--chapters "자막번호=제목"` → 영상 시간 챕터, YouTube 챕터 규칙(0:00 시작·3개 이상·10초 이상·순서) 검사 |
| 영상 | `video/` (신규, Remotion 4.0.534) | 공통 디자인·컴포넌트, 스토리보드 스크립트, 첫 영상 `multagi-2026-10` (31장면 + 고지 카드, 8분 29초) — `video/CHANGELOG.md` |
| 지시사항 | `guides/upload_guide.md`, `stock/guides/upload_rules.md` (신규), `guides/video_guide.md` v3.2 | 업로드 시트 규칙, 첫 영상 제작에서 정한 방식(로컬 폰트·plan.ts·storyboard.mjs) 반영 |

### 검증
- `srt_tool.py check` 통과(자막 91개), `upload` → 업로드용 SRT 자막 24부터 +8.0초, 챕터 12개 "✅ YouTube 챕터 규칙 통과"
- `video/`: `tsc --noEmit` 통과, 스토리보드 still 44장 검수(9개 장면 수정 후 다시 렌더)
- 전체 렌더: `final_1080p.mp4` 1920×1080 · 30fps · 15,285프레임 · 8분 29.5초 · 71.9MB · H.264, 오디오 없음(내레이션 전). 렌더 857초(4코어, concurrency 4). mp4에서 뽑은 프레임 8장이 스토리보드와 일치

## v2.3.0 — 2026-10-09 — 주제별 설정 파일 분리 · wget 실행기 · 저장소 구조 정리

### 왜 바꿨나 (사용자 지시)
1. 주식 말고 다른 주제로도 영상을 만들 수 있게, **공통으로 쓰는 코드·지시사항은 최상위**로, 주제별 내용은 주제 폴더로 나눈다.
2. 분석 코드의 키워드처럼 **바뀔 수 있는 값은 따로 설정 파일**에서 고칠 수 있게 한다.
3. 분석 코드를 **wget으로 받아서 실행**하는 스크립트를 만든다.

| 영역 | 함수/파일 | 변경 내용 |
|---|---|---|
| 설정 | `stock/analyzer_config.toml` (신규) | 주식 검색어 9개 카테고리·90개, 관련어(강한/약한/제외), 광고 의심 기준, GitHub 저장소를 코드에서 옮김. `[advanced]`에 바꿀 수 있는 주요 설정과 기본값(주석) |
| 설정 | `[설정 2]` 기본값 | 코드에는 주제와 무관한 기본값만 남김: `KEYWORD_MODE="autocomplete"`, `KEYWORD_GROUPS={}`, 관련어 `[]`(= TOPIC 한 단어). ⚠️ **설정 파일 없이 실행하면 주식도 자동완성 모드로 동작** (설정 파일이 없으면 틀을 만들고 경고) |
| 설정 | `apply_config_file`, `flatten_config`, `config_template`, `resolve_config_path` (신규) | TOML 읽기(3.11+ `tomllib`, 3.10은 `tomli` 자동 설치). `[섹션]`을 펼쳐 같은 이름의 설정을 덮어씀. 형식 오류(줄·칸 번호)·형식 불일치는 실행 전에 멈춤, 모르는 이름은 비슷한 이름 제안(오타), 정수↔실수 자동 변환, 설정 파일로 못 바꾸는 키(`AUTO_INSTALL_PACKAGES`, `UPDATE_YTDLP_DAILY`) 안내 |
| 실행부 | `load_config`, `init_config_only`, `--config`, `--init-config` | 우선순위 코드 기본값 < 설정 파일 < 명령줄. 기본 경로 `<스크립트 폴더>/<--folder 또는 PROJECT_FOLDER>/analyzer_config.toml`. `--init-config`는 새 주제 설정 파일 틀만 만들고 종료(덮어쓰지 않음). `--push-only`도 설정 파일의 폴더를 따름 |
| 리포트 | `write_report`, `write_run_info` | 사용한 설정 파일(스크립트 폴더 기준 상대경로 — PC 사용자 이름 노출 방지)·생성 여부 표시 |
| Stage 1 | `stage1_keyword_discovery` | 🐛 자동완성 모드에서 수요 점수 열이 object 형식이 되어 pandas 3에서 `nlargest` 오류 → 숫자 형식으로 고정 (설정 파일 없는 새 주제가 이 경로를 타므로 수정) |
| 자가진단 | `run_self_test`, `SELFTEST_TOPIC_CFG` | 🐛 가짜 데이터가 '주식' 제목이라 다른 주제 설정이면 자가진단이 실패하던 문제 → 주제 관련 값을 고정. 설정 파일 읽기·검증 테스트 추가 → **23개** |
| 실행기 | `run_analyzer.ps1`, `run_analyzer.sh` (신규) | 분석 코드는 매번 최신으로, 설정 파일은 없을 때만 GitHub raw에서 받음(wget / Invoke-WebRequest, 없으면 curl). `.venv` 자동 생성, `-Folder/-Topic/-Branch/-UpdateConfig` 옵션, 키가 없으면 안내 |
| 도구 | `tools/srt_tool.py` (신규) | 대본 TXT → SRT 생성(`build --reuse`: 바뀐 문장만 새로 계산)·검사(`check`). 지시사항 5-2 규칙(1자막=1문장, 22자 줄바꿈, 50자 제한, 빈 시간 없음, 초당 5.2음절) |
| 저장소 | `guides/`, `stock/guides/`, `stock/source/`, `stock/titles/` | 영상 제작 지시사항을 공통(`guides/`)과 주식 전용(`stock/guides/`)으로 나눔 — 각 파일의 변경 이력 참고 |

### 검증
- 자가진단 23/23. 기본값·주식 설정·다른 주제 설정(부동산) 모두 통과
- CLI: `--init-config` 생성·덮어쓰기 방지, 형식 오류(따옴표 없음 → 줄·칸 번호), 형식 불일치(숫자 자리에 글자), `--config` 경로 없음 → 모두 분석 전에 멈춤(종료 코드 1)
- 모의 전체 실행 4회 통과:
  - 주식 설정 파일 (Python 3.11): 90개 키워드 curated 모드, 푸시까지
  - 설정 파일 없음 (Python 3.11 / 3.13·pandas 3): 틀 생성 → 자동완성 150개 → 리포트·푸시
- 실행기: `run_analyzer.sh`(bash)와 `run_analyzer.ps1`(PowerShell 7.4)을 로컬 서버에서 받아 실행 → 코드·설정 다운로드, `.env` 생성 안내, `-UpdateConfig` 백업, 새 주제 설정 틀 생성, 실제 YouTube API 호출(가짜 키 → `API_KEY_INVALID`로 정상 종료)
- ⚠️ Windows PowerShell 5.1(윈도우 기본)에서는 실행해 보지 못함. UTF-8 BOM 저장, `-UseBasicParsing`, TLS 1.2 설정으로 대비

## v2.2.0 — 2026-10-09 — 실제 실행 결과(20261009_204204) 검토 후 수정: 검색 일일 한도 · 광고 의심 영상 · 제목 예시 · 재인코딩

### 왜 바꿨나 (v2.1.0 실제 실행 로그·데이터에서 확인된 문제)
1. **검색 74회 중 34회 실패** — `429 RATE_LIMIT_EXCEEDED: ... limit 'Search Queries per day'` (유닛 쿼터와 별개인 *일일 검색 횟수 한도*). 코드는 이를 일반 오류로 보고 남은 키워드를 계속 요청(34번 모두 실패), 실패한 키워드는 이월 목록에도 없었고 리포트는 "이월 16개"만 표시
2. **광고 집행(유료 홍보) 영상이 성공사례 1위** — 구독자 681명 채널의 쇼츠가 조회수 274만·좋아요 0.16%·댓글 3개(아웃라이어 8,690배). 성공 영상 95개 중 8개가 이런 형태(좋아요 <0.25% & 댓글 <0.05/1,000회, 전체 중앙값은 좋아요 0.97%·댓글 1.19/1,000회)
3. **제목 예시가 소재와 안 맞음** — '주식 폭락 전재산 손실' 같은 실패 사연 키워드에 「수수료 0.1% 차이가 만드는 결과」「현실적으로 수익 내는 방법」 같은 일반 투자 템플릿이 붙음
4. **불필요한 재인코딩 약 11분** — 공개 저장소라 영상은 어차피 GitHub에 안 올라가는데 49MB 맞추려고 240p로 재인코딩(성공사례 단계 775초 중 약 696초). 최저 비트레이트에서 같은 재인코딩을 두 번 반복(4분)
5. 자가진단의 **모의 다운로드 경고**("봇 확인 차단 → 다운로드 중단")가 실제 로그에 섞여 혼동

| 영역 | 함수/설정 | 변경 내용 |
|---|---|---|
| API | `is_daily_limit` (신규), `YouTubeClient._request`, `QuotaExceededError.kind` | 429/403 + 'per day' 메시지 → 일일 한도로 판정, 재시도 없이 즉시 중단. 거부된 요청은 예산 추적에서 차감 안 함(실제로 실행 안 됨). 분당 제한(`RATE_LIMIT_EXCEEDED`, per minute)은 재시도 대상에 추가 |
| Stage 2 | `collect_search` | 한도 도달 후 새 검색 중단(1회만 실패), **캐시에 있는 검색은 계속 사용**, 못 한 키워드는 사유와 함께 이월(`deferred_reason`: 예산 초과/일일 검색 횟수/일일 쿼터) |
| Stage 3 | `flag_ad_suspects` (신규), `AD_SUSPECT_FILTER`/`AD_SUSPECT_MIN_VIEWS=50,000`/`AD_SUSPECT_MAX_LIKE_RATE=0.25%`/`AD_SUSPECT_MAX_COMMENT_RATE=0.05/1,000` | 고조회수인데 좋아요율·댓글률이 **둘 다** 극히 낮은 영상 → 성과 분석(`perf`)·성공 판정·성공사례·키워드별 참고 영상에서 제외 (좋아요/댓글 숨김이면 판단 보류). ⚠️ 성공 판정 기준 변경 → 성공 비율·키워드 점수가 v2.1.0과 달라짐 |
| Stage 4 | `analyze_keywords`, `recent_hot` | 키워드별 성과·참고 영상·최근 급상승에서 광고 의심 영상 제외 (검색 경쟁도 계산에는 그대로 포함 — 실제 검색 화면 경쟁자이므로) |
| Stage 6 | `process_success_case`, `ensure_max_size`, `videos_go_to_github` (신규) | 영상이 GitHub에 안 올라가는 게 확실하면(공개 저장소·푸시 안 함) **재인코딩 생략 → 원본 화질 유지**. 비공개 저장소면 기존대로 49MB 이하로. 최저 비트레이트(60kbps)에서 같은 재인코딩 반복 방지 |
| Stage 7 | `keyword_intent`, `make_titles`, `TITLE_TEMPLATES_BY_INTENT` (신규) | 키워드 성격(실패·손실 사연 / 사기·피해 / 일반)별 제목 템플릿. 데이터에서 효과가 확인된 제목 요소 순서는 그대로 |
| Stage 7 | 리포트 | 이월 사유별 개수, 광고 의심 제외 목록, 기준선 부족 시 "채널 평균 비교 불가" 표시(기존 "-배"), `videos.csv` 에 `on_topic`·`topic_reason`·`ad_suspect`·`category`·`found_by` 열 추가 |
| 자가진단 | `_quiet_logs` 외 4개 검사 | 모의 다운로드 로그 숨김 + 일일 한도 판정 / 한도 도달 시 이월·캐시 계속 / 광고 의심 판정 / 성격별 제목 → **22개** |

### 검증
- 자가진단 22/22
- 모의 전체 실행(실제 v2.1.0 429 응답 형식 재현, 30회 후 한도): 429는 **1번만** 발생 → 새 검색 중단, 이월 60개(예산 16 + 한도 44), 쿼터 추적 3,223(거부된 요청 미차감), 광고 영상 3개 제외(성공 3개 제거), 공개 저장소 → 재인코딩 생략, 제목 예시 성격별 생성
- 비공개 저장소 모의 실행: 재인코딩(57→25MB)·푸시 정상
- 최저 비트레이트 가드: 0.05MB 목표로 강제 → 1회 후 "재인코딩 중단" 경고
- Python 3.11/pandas 2.2 · 3.13/pandas 3.0 실행 통과

## v2.1.0 — 2026-10-09 — 카테고리별 검색어 · 주제 관련성 필터 · GitHub 쓰기권한 확인/--push-only

### 왜 바꿨나
1. 검색어를 사연·노후·가족 갈등·사기 피해 등 **카테고리별로 다양하게** 지정하고 싶음
2. `git push` 가 `Permission to ... denied to yeomin1024` 로 실패 — 토큰은 인증되지만 **쓰기 권한이 없음**. 기존 사전 확인은 저장소 API의 '계정' 권한(관리자)을 봐서 토큰 권한 부족을 못 잡았음
3. 성공사례에 `홈쇼핑_방송_사고` 같은 **주제와 무관한 영상**이 들어감 — YouTube 검색은 무관한 인기 영상도 섞어 보여주는데 조회수·배수만으로 골랐기 때문

| 영역 | 함수/설정 | 변경 내용 |
|---|---|---|
| 설정 | `KEYWORD_MODE`, `KEYWORD_GROUPS`(9개 카테고리·90개), `AUTOCOMPLETE_TOP_N` | 카테고리별 직접 지정 검색어 (기본 = 요청하신 8개 카테고리 80개 + '사연·썰·다큐 포맷' 10개). 기존 자동완성 방식은 `"autocomplete"`/`"both"` 로 선택 |
| 설정 | `SEARCH_ORDERS` | **`["relevance","viewCount"]` → `["relevance"]`** (키워드 수 증가에 따른 쿼터 절약, 키워드당 100유닛) |
| 설정 | `SEARCH_CACHE_TTL_HOURS=168`, `BASELINE_CACHE_TTL_HOURS=72` | 검색 7일·채널 업로드 목록 3일 캐시 → 하루 예산 초과 키워드를 다음 실행에서 이어서 수집 |
| Stage 1 | `keyword_demand`, `score_keyword_demand`, `round_robin_priority` | 키워드별 검색 수요 = 자동완성이 표현을 어디까지 알아보는지(깊이×폭, 쿼터 0). 카테고리를 번갈아 배치해 예산이 모자라도 모든 카테고리가 골고루 수집 |
| Stage 2 | `plan_quota` | 캐시된 검색은 0유닛으로 항상 포함, 나머지는 우선순위대로 예산까지 → 초과분 이월(로그·리포트 표시) |
| Stage 3 | `topic_relevance` (신규), `RELEVANCE_TERMS`/`RELEVANCE_WEAK_TERMS`/`RELEVANCE_EXCLUDE` | 제목·태그의 강한 관련어(또는 설명란 2회 이상, 약한 관련어+맥락)로 주제 관련 판정, '주식회사' 등 오탐 표현 제거. 무관 영상은 성과 분석·성공 판정·성공사례에서 제외하고 `data/excluded_offtopic.csv` 로 기록 |
| Stage 4 | `analyze_keywords`, `analyze_categories` (신규) | 수요·경쟁을 **주제 관련 영상만**으로 계산, `relevant_share`·`content_gap`(검색 상위 중 무관 영상 비율) 추가, 카테고리별 요약 |
| Stage 4 | `KEYWORD_SCORE_WEIGHTS` | ⚠️ **가중치 변경**: median_outlier 0.15→0.10, fresh_share 0.10→0.05, content_gap 0.10 신규 (합계 1.0) — 무관 영상이 많은 검색어 = 볼 영상이 부족한 공백 |
| Stage 6 | `select_success_cases`, `MAX_CASES_PER_CATEGORY=2` | 주제 관련 영상만, 카테고리당 최대 2개(부족하면 완화) → 여러 소재를 골고루 |
| Stage 8 | `check_push_access` (신규), `reload_github_token`, `push_only`, `--push-only` | 토큰의 실제 쓰기 권한을 git 푸시 엔드포인트로 **분석 전에** 확인, 토큰 종류(fine-grained/classic)별 해결 방법 안내, 푸시 직전 `.env` 재확인, 분석 없이 결과만 올리는 `--push-only` |
| 리포트 | 카테고리별 기회 표·차트(`12_category_opportunity.png`), 이월 키워드, 무관 영상 목록, 성공사례의 카테고리·검색어 | |

### 검증
- 자가진단 18/18 (관련성 필터: 홈쇼핑·'주식회사'·곤충 '개미' 제외 / 수요 점수: 실제 자동완성 응답 기반 / 카테고리 순환 / 캐시 인식 쿼터 / 토큰 403·scope 부족 판정)
- 모의 데이터 전체 실행: 90개 키워드 중 74개 수집·16개 이월 → **같은 폴더 2회차 실행에서 74개 캐시 재사용(0유닛) + 16개 추가 = 90개 완료**, 무관 영상('홈쇼핑 방송 사고') 제외·성공사례 6개가 6개 카테고리에 분산
- 쓰기 권한 없는 토큰 시나리오: 시작 시 경고 → 분석 완료 → 푸시만 안내와 함께 건너뜀 / `--push-only` 로 기존 결과 푸시 성공
- 실제 YouTube 자동완성으로 90개 키워드 수요 점수 계산 확인 (259개 질의)
- Python 3.10~3.13 컴파일, Python 3.11/pandas 2.2 · 3.13/pandas 3.0 실행 통과
- ⚠️ 실제 GitHub 403 응답은 이 환경에서 재현 불가 (GitHub 표준 동작 기준 구현 + 푸시 오류 메시지 해석으로 이중 대비)

## v2.0.0 — 2026-10-09 — 내 PC에서 실행하는 단일 스크립트로 전환

Kaggle 노트북(`youtube_topic_analyzer.ipynb`, v1.2.0) → **`youtube_topic_analyzer.py`** 하나로 교체 (노트북은 git 기록 `977bc4f` 에 보존).
분석 로직·점수 가중치·성공 기준·위험 관련 기본값은 **변경 없음**.

| 영역 | 함수/위치 | 변경 내용 · 이유 |
|---|---|---|
| 키 | `.env` (`load_env_file`, `load_keys`) | Kaggle Secrets → 스크립트 폴더의 `.env`. 처음 실행 시 템플릿 자동 생성, `.gitignore` 등록. 값은 앞뒤 4자만 표시 |
| 설정 | 스크립트 상단 [설정 2] + 명령줄 | `--topic --folder --result-folder --keywords --cases --no-video --no-push --no-open --log-level --skip-install` (변경값은 로그에 기록). 주제만 바꾸고 폴더가 `stock` 이면 덮어쓰기 경고 |
| 설치 | `bootstrap` | 필요한 패키지 자동 설치(pip), yt-dlp 하루 1회 업데이트, faster-whisper 설치 실패 시 24시간 재시도 안 함, Python 3.10 미만 차단, 콘솔 UTF-8 |
| 경로 | `init_run` | 결과 = `<스크립트 폴더>/output/<PROJECT_FOLDER>/<RESULT_FOLDER>`, 캐시·임시 = `.yt_work/` (재실행 시 캐시 재사용 → 쿼터 절약) |
| Windows | `rmtree_force`, `close_log_files`, `run_git`, `ensure_max_size`, subprocess 전반 | git 읽기전용 파일 삭제, 열린 로그 파일 잠금 해제, `core.longpaths`·`credential.helper=`(로그인 팝업 방지), `os.replace`, 하위 프로세스 출력 UTF-8 디코딩 |
| 차트 | `setup_chart_style` | 맑은 고딕(Windows)·AppleGothic(macOS)·나눔고딕(Linux) 순 탐색, 없으면 나눔고딕 자동 다운로드. 항상 PNG 저장(Agg) |
| 다운로드 | `run_ytdlp`, `prepare_cookies`, `ytdlp_base_opts` | 일시 오류(간헐 403·응답 추출 실패·5xx·타임아웃) 자동 재시도(3초·8초), 스크립트 폴더 `cookies*.txt` 자동 인식, `COOKIES_FROM_BROWSER` 지원. PC용 다운로드 스크립트 생성 기능 제거(이미 PC) |
| GitHub | `stage8_push_github` | Git 미설치 시 안내 후 건너뜀, 푸시 실패는 PC 결과에 영향 없이 경고만 |
| 마무리 | `stage8_finish` (신규, Kaggle 출력 대체) | 결과 요약, 선택 zip, 결과 폴더 열기(탐색기/Finder) |

### 검증
- 문법: Python 3.10 / 3.11 / 3.12 / 3.13 컴파일 통과 (SyntaxWarning 없음), pyflakes 미정의 이름 없음
- 자가진단 13/13 (일시 오류 재시도 테스트 추가)
- **새 가상환경 첫 실행 재현**: `.env` 자동 생성 → 패키지 자동 설치 → 키 없으면 안내 후 종료 → (가짜 키) 자가진단·실제 자동완성 수집까지 진행 후 실제 YouTube API가 키 오류를 반환하자 안내 메시지와 함께 종료
- 모의 YouTube 데이터 + 로컬 git 원격으로 전체 실행 통과 (Python 3.11/pandas 2.2, 3.13/pandas 3.0), 봇 확인 시나리오·`cookies.txt` 자동 인식 확인
- 실제 YouTube: 시스템 ffmpeg 없이(번들 ffmpeg) 영상+음성 병합 다운로드, 길이 측정, 재인코딩, 자막 수집 성공
- ⚠️ 실제 Windows/macOS 기기와 실제 API 키로는 실행하지 않음 (Windows 대응은 코드 검토 기준)

## v1.2.0 — 2026-10-09 — YouTube 봇 확인('Sign in to confirm you're not a bot') 대응

원인: Kaggle(구글 클라우드 데이터센터 IP)에서 yt-dlp 요청 시 YouTube가 로그인(봇 확인)을 요구. 분석 로직·점수는 **변경 없음**.

| 영역 | 셀/함수 | 변경 내용 · 이유 |
|---|---|---|
| 키 | 블록 1 | 선택 Secret `YTDLP_PROXY`(주거용 프록시) 추가 |
| 설정 | 블록 2 | `YTDLP_CLIENT_FALLBACK`, `YTDLP_MAX_BOT_BLOCKS=2`, `WRITE_LOCAL_DOWNLOAD_SCRIPT` 추가. `YTDLP_COOKIES_FILE` 비우면 데이터셋 자동 탐색 |
| 공통 | `find_cookie_files`, `inspect_cookies`, `prepare_cookies` | `/kaggle/input/**/*cookie*.txt` 자동 인식, 쿠키 점검(로그인 쿠키 유무·만료 — **이름만 기록, 값은 기록 안 함**). 쿠키 처리를 `init_run` 에서 분리 |
| Stage 6 | `refresh_download_auth` (신규) | Stage 6 셀 실행 때마다 쿠키/프록시 Secret을 다시 읽고 봇 확인 상태 초기화 → **쿠키 추가 후 Stage 6만 재실행** 가능 |
| Stage 6 | `run_ytdlp` (신규), `ytdlp_download`, `transcript_via_ytdlp` | 봇 확인 시 다른 YouTube 클라이언트(tv_simply → tv → web_embedded → mweb)로 재시도, 성공 클라이언트 재사용. **연속 2개 영상**이 모두 막히면 이번 실행의 yt-dlp 시도 중단(시간 낭비·IP 평판 악화 방지). 같은 영상의 영상/자막/음성 시도는 1회로 집계 |
| Stage 6 | `transcript_via_api`, `ytdlp_base_opts` | 프록시 지원(yt-dlp, youtube-transcript-api) |
| Stage 6 | `write_local_download_script` (신규) | 막힌 사례만 담은 `success_cases/download_on_pc.py` 생성 — 가정용 IP(내 PC)에서 영상·대본을 같은 폴더 구조로 받기 |
| Stage 6/7 | 상태·리포트 | 영상 상태 `blocked(bot_check)`, 리포트·요약에 해결 방법 안내 |

### 검증
- 자가진단 12/12 (쿠키 점검, 클라이언트 재시도 → tv 기억, 연속 차단 시 중단 테스트 추가)
- 봇 확인을 항상 반환하는 가짜 yt-dlp로 Stage 0~8 전체 실행: 2번째 영상에서 중단, 이후 사례는 즉시 건너뜀, `download_on_pc.py` 생성·리포트 안내 확인
- 실제 YouTube: 쿠키 파일을 붙인 상태에서 래퍼 경유 영상·자막 다운로드 성공, 생성된 `download_on_pc.py` 를 실제로 실행해 영상+대본 저장 성공
- Python 3.11/pandas 2.2 및 Python 3.13/pandas 3.0 모두 통과
- ⚠️ 실제 Kaggle IP에서의 봇 확인 해소 여부는 이 환경에서 재현할 수 없어 미검증 (쿠키 품질·계정 상태에 따라 다름)

## v1.1.0 — 2026-10-09 — Kaggle 노트북 실행 + Kaggle Secrets로 키 읽기

실행 환경을 Colab → **Kaggle Notebooks** 로 전환. 분석 로직(Stage 1~4)·점수 가중치·성공 기준은 **변경 없음**.

| 영역 | 셀/함수 | 변경 내용 · 이유 |
|---|---|---|
| 키 입력 | 블록 1 (`read_secret`) | 셀 입력칸·Colab Secrets·getpass 제거 → `kaggle_secrets.UserSecretsClient().get_secret()` 로만 읽음 (로컬 테스트용 환경변수 폴백). Secret 이름은 `SECRET_LABELS` 로 변경 가능. 선택 Secret `YTDLP_COOKIES` 추가 |
| 설정 | 블록 2 | Colab `#@param` 폼, `VIDEO_FALLBACK_TO_DRIVE`·`SAVE_TO_GOOGLE_DRIVE`·`DRIVE_FOLDER` 제거 → `MAKE_RESULT_ZIP` 추가 |
| 설치 | 블록 3 | Internet Off 감지 시 안내와 함께 중단, 한글 폰트 apt 실패 시 Google Fonts에서 다운로드, `imageio-ffmpeg` 추가(시스템 ffmpeg 없을 때) |
| 공통 | `init_run`, `find_ffmpeg`, `prepare_cookies` | 결과 = `/kaggle/working/<PROJECT_FOLDER>/<RESULT_FOLDER>` (Kaggle Output), 캐시·임시파일 = `/tmp` (Output 미포함). 키가 없으면 초기화에서 즉시 중단. 쿠키 Secret(base64/원문) → 권한 600 파일, `/kaggle/input` 쿠키는 복사 후 사용(읽기전용 대비) |
| Stage 5 | `setup_chart_style`, `_save` | 인라인 표시 조건을 노트북 여부로 변경, 다운로드 폰트 경로 추가 |
| Stage 6 | `ytdlp_base_opts`, `media_duration`, `ensure_max_size`, `transcript_via_whisper` | yt-dlp에 `ffmpeg_location` 지정, ffprobe 없으면 `ffmpeg -i` 로 길이 파싱, Whisper GPU는 `compute_type="auto"`(P100 등 대비) + GPU 오류 시 CPU 재시도, 안내 문구 Kaggle 기준 |
| Stage 8 | `stage8_kaggle_output` (신규), `stage8_save_drive` (삭제) | Google Drive 저장 → Kaggle 출력 정리 + `<PROJECT_FOLDER>_<RESULT_FOLDER>.zip`. 공개 저장소에서 GitHub에 못 올린 영상은 Kaggle 출력에 보관됨을 로그·리포트에 표시 |

### 위험 관련 기본값 — 변경 없음
`QUOTA_BUDGET=9000`, `SUCCESS_CASE_COUNT=8`, `VIDEO_MAX_MB=49`, `ALLOW_VIDEO_UPLOAD_TO_PUBLIC_REPO=False`

### 검증
- Kaggle 모사 환경(Python 3.11.17 · pandas 2.2.3 · 가짜 `kaggle_secrets` · `/kaggle/working`)에서 전체 Stage 실행 통과 (공개/비공개 저장소 모두)
- 키를 Secrets에서만 읽음 확인, Secret 미등록 시 안내 후 중단 확인, 출력·git 기록에 키/토큰 문자열 없음 확인
- 시스템 ffmpeg 없이(imageio-ffmpeg) 길이 측정·재인코딩·yt-dlp 병합 경로 동작 확인
- node 없이 deno만으로 실제 yt-dlp 자막·영상 다운로드 성공
- 자가진단 10/10 통과

## v1.0.0 — 2026-10-09 — 최초 작성

구독자 0명 채널이 '주제(기본: 주식)'에서 조회수를 가장 잘 받을 영상을 찾는 Colab 노트북.

| 영역 | 셀/함수 | 내용 |
|---|---|---|
| 키 입력 | 블록 1 (`_resolve_secret`) | YouTube API 키·GitHub 토큰을 별도 블록에서 입력. 셀 입력 → Colab Secrets → 환경변수 → getpass 순서 |
| 설정 | 블록 2 | `TOPIC`(주제 변경 가능), `PROJECT_FOLDER`(결과 상위 폴더, 없으면 생성), `RESULT_FOLDER`, 수집/성공 기준/다운로드 옵션 |
| 설치 | 블록 3 | yt-dlp[default] + deno(JS 런타임), youtube-transcript-api, kiwipiepy, faster-whisper, 한글 폰트 |
| 공통 | `setup_logging`, `log`, `stage_timer`, `JsonCache`, `init_run` | `[STAGE] [시각] [레벨] key=value` 구조화 로그, 토큰 마스킹, 단계별 소요시간, API 응답 캐시, 시드 고정, 위험 설정 변경 경고 |
| API | `YouTubeClient` | 쿼터 예산 추적(요청 전 예약), 재시도/백오프, 치명 오류(키 오류·API 미사용) 안내, 50개 묶음 병렬 요청 |
| Stage 1 | `stage1_keyword_discovery` | YouTube 자동완성 확장(ㄱ~ㅎ, 가~하, a~z, 수식어, 2단계) → 검색 수요 점수, 유사 키워드 중복 제거 |
| Stage 2 | `stage2_collect`, `plan_quota` | 검색(관련도=실제 검색화면, 조회수순=기간 내 히트) → 영상/채널 상세 → 채널 최근 업로드 기준선. 쿼터 부족 시 키워드 수 자동 축소(전/후 로그) |
| Stage 3 | `validate_videos`, `compute_outlier_scores` | 중복·결측·범위·미래날짜 검증, 일평균 조회수, 구독자 대비 조회수, **채널 기준선 대비 아웃라이어 배수**(leave-one-out, 포맷별, 14일 미만 영상 제외로 누적 편향 방지), 쇼츠 판별 |
| Stage 4 | `analyze_keywords` 외 | 키워드 기회점수(가중치 명시), 채널명 검색 제외, 제목 요소 효과(Mann-Whitney + BH-FDR 보정), 형태소 단어 분석, 길이/포맷/요일·시간/채널 규모, 제목 클러스터(KMeans, 시드 고정), 태그, 댓글 질문 |
| Stage 5 | `stage5_charts` | 차트 11종 PNG (색각이상 검증 팔레트, 이중축 없음) |
| Stage 6 | `stage6_success_cases` | 성공사례 선정(소규모 채널·롱폼 쿼터, 채널당 1개) → 썸네일, 영상(용량 초과 시 ffmpeg 재인코딩), 대본(자막 API → yt-dlp 단일 트랙 → Whisper), 메타데이터, 댓글 |
| Stage 7 | `stage7_report` | `README.md` 리포트(추천 아이디어·업로드 플랜·체크리스트·방법론), `analysis.xlsx`, `data/*.csv`, `run_info.json`, `run_log.txt` |
| Stage 8 | `stage8_push_github`, `stage8_save_drive` | `<PROJECT_FOLDER>/<RESULT_FOLDER>`로 커밋·푸시(폴더 자동 생성, 토큰은 헤더로만 전달), 100MB 초과 파일 제외, **공개 저장소면 영상 파일은 GitHub 대신 Drive** |

### 위험 관련 기본값 (변경 시 로그·리포트에 경고)
- `QUOTA_BUDGET=9000` (일일 한도 10,000)
- `SUCCESS_CASE_COUNT=8`, `VIDEO_MAX_MB=49`, `VIDEO_MAX_HEIGHT=480`
- `ALLOW_VIDEO_UPLOAD_TO_PUBLIC_REPO=False` — 공개 저장소에 타인 영상을 올리지 않도록 기본 차단 (저작권)

### 검증
- 오프라인 자가진단 10/10 통과 (심어둔 3배 효과를 lift 3.02배로 탐지 등)
- 모의 YouTube 데이터 + 로컬 git 원격으로 Stage 0~8 전체 실행: 공개/비공개 저장소, 기존 결과 교체, 다른 폴더 보존, 쿼터 부족 시나리오
- 실제 네트워크: 쇼츠 판별, 자막 API, yt-dlp 자막·영상 다운로드, ffmpeg 재인코딩, faster-whisper 동작 확인
- pandas 2.2.3 / 3.0.6 모두 경고 없이 동작
