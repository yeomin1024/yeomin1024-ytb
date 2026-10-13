# PC에서 분석 돌리기 — 경제·재테크(`economic`)

버전: v1.0 — 2026-10-13 — 새로 만듦 (사용자 지시: "분석기 코드 pc에서 돌릴 수 있도록 수정하고 방법 알려주고 api 할당량이 초기화된 시간이 되면 다시 자동으로 분석결과를 확인 못한 부분부터 새로 추가로 만들도록")

※ 연구·교육용 분석 도구입니다. 투자 조언이 아닙니다.

## 왜 PC에서 돌리나

| 받는 것 | 클라우드(Claude Code) | 집 PC |
|---|---|---|
| 검색·영상 정보·구독자 수·댓글 (YouTube Data API, `www.googleapis.com`) | 됨 | 됨 |
| 자막 (`www.youtube.com`) | **안 됨** — 네트워크 정책 때문에 ProxyError 403 (2026-10-12·13 확인) | 됨 (2026-10-09 PC 실행 8/8 성공) |
| 썸네일 이미지 (`i.ytimg.com`) | **안 됨** — 같은 이유 | 됨 |

성공 사례를 대본 내용까지 분석하려면 자막이 필요해서 PC에서 돌립니다.
(클라우드에서 받으려면 환경 설정 → 네트워크 접근 → 허용 도메인에 `www.youtube.com`·`i.ytimg.com`을 넣어야 합니다. YouTube가 클라우드 IP를 막을 수도 있어 PC가 더 확실합니다.)

## 처음 한 번 (Windows)

1. **Python 3.10 이상** 설치 — [python.org](https://www.python.org/downloads/) 설치 첫 화면에서 **"Add python.exe to PATH"** 체크
2. **Git** 설치 — https://git-scm.com/downloads (결과를 GitHub에 올릴 때 필요. 기본 설정 그대로 "Next")
3. 작업할 폴더를 만듭니다. 예: `문서\ytb`
4. 그 폴더에서 PowerShell을 엽니다 (탐색기 주소창에 `powershell` 입력 후 Enter) → 아래 두 줄 실행
   ```powershell
   wget https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/main/run_analyzer.ps1 -OutFile run_analyzer.ps1
   powershell -ExecutionPolicy Bypass -File .\run_analyzer.ps1
   ```
   - PowerShell 7이면 첫 줄 대신: `curl.exe -L -o run_analyzer.ps1 https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/main/run_analyzer.ps1`
5. 처음에는 키가 없어서 멈추고 **`.env` 파일**이 생깁니다. 메모장으로 열어 `=` 뒤에 값을 붙여넣고 저장합니다 (따옴표 없이).
   ```
   YOUTUBE_API_KEY=AIza...         ← 필수
   GITHUB_TOKEN=github_pat_...     ← 권장 (없으면 결과는 PC에만)
   ```
   - **YOUTUBE_API_KEY:** [Google Cloud 콘솔](https://console.cloud.google.com/) → 프로젝트 → API 및 서비스 → 라이브러리 → "YouTube Data API v3" 사용 → 사용자 인증 정보 → API 키 만들기. 클라우드 환경에 넣은 키와 같은 키를 써도 됩니다 (그러면 하루 10,000단위를 함께 씁니다).
   - **GITHUB_TOKEN:** GitHub → Settings → Developer settings → Personal access tokens → **Fine-grained tokens** → Generate new token → Repository access: **Only select repositories → `yeomin1024-ytb`** → Permissions → Repository permissions → **Contents: Read and write** → Generate. 나온 값(`github_pat_…`)을 붙여넣기.
   - `.env`는 이 PC에만 있고 GitHub에 올라가지 않습니다. 키 값은 로그에도 찍히지 않습니다 (`youtube_key=있음`처럼만).
6. 4번의 둘째 줄을 다시 실행합니다. 처음에는 패키지 설치로 몇 분 걸립니다.

macOS / Linux:
```bash
wget -O run_analyzer.sh https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/main/run_analyzer.sh
bash run_analyzer.sh
```

## 실행하면 일어나는 일

실행기(`run_analyzer.ps1` / `.sh`, v2.0)가 코드를 최신으로 받고, 설정·검색어 파일은 없을 때만 받은 뒤 `tools/pc_analysis.py economic`을 실행합니다. 한 **회차**는:

| 순서 | 하는 일 | 할당량 (하루 10,000단위) |
|---|---|---|
| ① 성공 사례 | `tools/outlier_research.py` — `economic/keywords.toml`의 검색어 그룹 10개 × 앞 2개 × 길이 2(4~20분·20분 넘음) = 검색 40번 → 최근·구독자 5만 이하·조회수 ≥ 구독자×3·4분 이상 → 상위 20개의 **자막·썸네일·댓글 100개** | 최대 4,000 (검색 1번 = 100) |
| ② 주제 분석 | `youtube_topic_analyzer.py` — 검색어 50개로 주제 전체 분석 (키워드 기회·제목 패턴·길이·시청자 질문 등) | 최대 6,000 (`economic/analyzer_config.toml`의 `QUOTA_BUDGET`) |
| ③ 올리기 | 진행 상태 `pc_progress.json`을 쓰고 GitHub `economic/result/`에 푸시 | 0 |
| ④ 남은 일이 있으면 | **할당량이 초기화될 때까지 기다렸다가 다음 회차** | — |

**이어서 돌리기:** 두 도구 모두 받은 검색 결과(7일)·영상 정보·자막·댓글을 PC에 저장해 둡니다. 다음 회차는 받은 것은 할당량 0으로 다시 쓰고 **못 한 부분만 새로 받아** 결과에 더합니다.
- 남은 일 = 할당량 때문에 못 한 검색·영상 정보·댓글 (`economic/result/outliers/status.json`의 `pending`), 분석기의 이월 검색어 (`run_info.json`의 `keywords.deferred`), 네트워크 때문에 못 받은 자막
- **할당량 초기화 = 미국 태평양 시간 자정** → 한국 시간 **오후 4시**(3월 둘째 일요일 ~ 11월 첫 일요일, 서머타임) / **오후 5시**(그 밖). 실행기는 그 **10분 뒤**(16:10 / 17:10)에 다음 회차를 시작합니다.
- 화면 로그 예: `[ROUND] … round=1 complete=False left="성공 사례: 남은 검색 2·… / 분석기: 이월된 검색어 3개" next_round=2026-10-14T16:10+09:00`
- 최대 7회차(7일). 끝나면 `[DONE] … note="못 한 일 없음 — 끝"`.

## 기다리는 방법 둘 중 하나

**A. 창을 열어 두기 (기본)** — 위 명령을 실행해 두고 PowerShell 창을 닫지 않습니다. 남은 일이 있으면 알아서 다음 날 이어서 돌고, 다 끝나면 멈춥니다.
- PC가 **절전 모드**로 들어가면 그동안은 멈춥니다 (깨어나면 바로 이어서). 설정 → 시스템 → 전원 → "절전 모드 전환"을 **안 함**으로 두면 확실합니다.

**B. 작업 스케줄러에 맡기기 (창을 닫아도 됨)**
```powershell
powershell -ExecutionPolicy Bypass -File .\run_analyzer.ps1 -RegisterTask     # 매일 17:15 에 한 회차씩 (-Once)
powershell -ExecutionPolicy Bypass -File .\run_analyzer.ps1 -UnregisterTask   # 끄기
```
- 17:15면 서머타임이든 아니든 초기화가 지난 시각입니다. PC가 켜져 있고 로그인돼 있어야 돕니다.
- A와 B를 함께 해도 같은 주제가 두 번 동시에 돌지 않습니다 (잠금 파일 `.yt_work/pc_analysis_economic.lock`).
- macOS/Linux: `bash run_analyzer.sh --print-cron`이 보여 주는 줄을 `crontab -e`에 붙여넣기.

## 진행 상황·결과 보기

| 어디 | 무엇 |
|---|---|
| PC 화면 / `.yt_work/pc_analysis_economic.log` | 전체 로그 (`[ROUND]`·`[OUTLIER]`·`[ANALYZER]`·`[PUSH]`·`[WAIT]`) |
| PC `.yt_work/pc_progress_economic.json` | 마지막 회차 요약: 끝났는지, 남은 일, 다음 회차 시각 |
| PC `output/economic/result/` | 분석기 결과 전체 (리포트 `README.md`, `analysis.xlsx`, 차트, 성공사례) |
| PC `economic/result/outliers/` | 성공 사례: `summary.md`·`outliers.csv`·`candidates.csv`·`status.json` + 사례 폴더 `NN_<영상ID>/`(자막 `transcript.txt`·썸네일·댓글 원문) |
| GitHub `economic/result/` | 분석기 결과 + `outliers/`의 csv·md·json + `pc_progress.json` |

**공개 저장소라서** 다른 채널의 자막 전문·댓글 원문·썸네일(사례 폴더)은 GitHub에 올리지 않고 PC에만 둡니다. 대신 `summary.md`에 사례마다 설명 앞부분·챕터·**첫 20초·첫 1분 발췌·90초마다 흐름**·말 속도·인기 댓글 10개(짧게)가 들어가서, Claude가 GitHub만 보고도 내용·댓글을 분석할 수 있습니다.
(자막 전문을 Claude가 읽어야 하면: 저장소를 비공개로 바꾸는 방법이 있습니다 — 사용자가 정할 일입니다.)

다 끝나면 Claude에게 **"economic 분석 끝났어, 결과로 지시사항이랑 주제 만들어줘"**라고 하면 `guides/pipeline.md` 2단계부터 진행합니다.

## 검색어 바꾸기

- 검색어 목록은 **`economic/keywords.toml`** 하나에 있습니다 (분석기와 성공 사례 수집이 같이 씀): `[KEYWORD_GROUPS]` 그룹별 검색어, `EXCLUDE_KEYWORDS`(제목에 있으면 뺌), `[relevance]` 주제 관련어.
- PC에 있는 파일은 실행기가 덮어쓰지 않습니다. 메모장으로 고치면 다음 회차부터 적용됩니다. GitHub 최신으로 바꾸려면 `-UpdateConfig` (기존 파일은 `.bak`).
- 성공 사례 수집은 그룹마다 **앞에서부터** `--per-group`개(기본 2)를 씁니다 → 중요한 검색어를 앞에 두세요.

## 옵션

| 하고 싶은 것 | Windows | macOS / Linux |
|---|---|---|
| 한 회차만 | `-Once` | `--once` |
| 실행할 명령·다음 초기화 시각만 보기 | `--dry-run` | `-- --dry-run` |
| 설정·검색어 파일도 GitHub 최신으로 | `-UpdateConfig` | `--update-config` |
| 예전처럼 분석기만 한 번 | `-AnalyzerOnly` | `--analyzer-only` |
| 성공 사례 수집 할당량·개수 | `--outlier-quota 3000 --per-group 1 --top 15` | `-- --outlier-quota 3000 …` |
| 성공 사례만 / 분석기만 | `--skip-analyzer` / `--skip-outliers` | `-- --skip-analyzer` … |
| 다른 주제 폴더 | `-Folder <폴더>` | `--folder <폴더>` |

직접 실행: `python tools/pc_analysis.py economic [--once] [--dry-run]` · 점검: `python tools/pc_analysis.py --self-test`

종료 코드: `0` 다 끝남 · `3` 할당량 때문에 남은 일이 있음 (다음 실행이 이어서) · `2` 같은 주제가 이미 도는 중 · `1` 오류 (로그의 `next_step`·`hint` 확인)

## 문제 해결

- **`YOUTUBE_API_KEY 없음`** → `.env`를 메모장으로 열어 키를 넣고 저장 → 다시 실행
- **`같은 주제 분석이 이미 돌고 있음`** → 다른 창(또는 작업 스케줄러)에서 도는 중입니다. 확실히 멈춘 것이면 `--force`
- **자막이 `RequestBlocked`·`IpBlocked`** → 짧은 시간에 많이 받아 YouTube가 잠시 막은 것입니다. 남은 일로 세어 다음 회차에 다시 받습니다 (VPN은 끄세요).
- **`푸시 건너뜀 reason="GITHUB_TOKEN 없음"`** → `.env`에 토큰을 넣으면 다음 회차에 올라갑니다. 바로 올리려면 `python youtube_topic_analyzer.py --config economic/analyzer_config.toml --push-only`
- **`Permission … denied`** → 토큰의 Contents 권한이 Read and write인지, 저장소가 `yeomin1024-ytb`로 선택됐는지 확인 (`README.md` 문제 해결)
- **PowerShell "스크립트를 실행할 수 없습니다"** → 꼭 `powershell -ExecutionPolicy Bypass -File .\run_analyzer.ps1` 형태로 실행

## 변경 이력

| 버전 | 날짜 | 내용 |
|---|---|---|
| v1.0 | 2026-10-13 | 새로 만듦: PC 실행 방법, 회차·이어서 돌리기, 할당량 초기화 시각, 작업 스케줄러, 공개 저장소에 올리는 것·안 올리는 것 |
