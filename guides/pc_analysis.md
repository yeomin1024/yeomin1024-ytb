# PC에서 분석 돌리기 — 경제·재테크(`economic`)

버전: v1.3 — 2026-10-13 — 실행 명령을 어느 터미널에서나 되게: `-File run_analyzer.ps1`(`.\` 없음), 받기는 `curl.exe`(PowerShell·명령 프롬프트·Git Bash 공통), 문제 해결에 '-File 인수가 없습니다' (사용자 PC 오류 2026-10-13) (v1.2 — 2026-10-13 — 사용자 지시 "동시에 병렬로 다른 주제 분석도 가능하도록 해야해 그럼 검색어 설정 파일, 키설정 파일도 여러개": 여러 주제를 동시에(`-Folder economic,health`), 주제마다 검색어·키 파일, 같은 키는 할당량 N등분, 프로젝트 여러 개로 할당량 늘리기는 정책 위반 (v1.1 — 2026-10-13 — 사용자 지시 "비공개로 돌릴테니까 전부 다 업로드되게 하고 댓글은 전부 받도록 수정해 그리고 구독자 수 상관없이 조회수 많이 나온 영상 댓글은 전부 받아야해": 댓글 전부(답글 포함)·조회수 상위 영상 20개, 비공개 저장소면 사례 폴더까지 전부 GitHub 에, 비공개 저장소에서 코드 받기(토큰) (v1.0 — 2026-10-13 — 새로 만듦 (사용자 지시: "분석기 코드 pc에서 돌릴 수 있도록 수정하고 방법 알려주고 api 할당량이 초기화된 시간이 되면 다시 자동으로 분석결과를 확인 못한 부분부터 새로 추가로 만들도록"))))

※ 연구·교육용 분석 도구입니다. 투자 조언이 아닙니다.

## 왜 PC에서 돌리나

| 받는 것 | 클라우드(Claude Code) | 집 PC |
|---|---|---|
| 검색·영상 정보·구독자 수·댓글 (YouTube Data API, `www.googleapis.com`) | 됨 | 됨 |
| 자막 (`www.youtube.com`) | **안 됨** — 네트워크 정책 때문에 ProxyError 403 (2026-10-12·13 확인) | 됨 (2026-10-09 PC 실행 8/8 성공) |
| 썸네일 이미지 (`i.ytimg.com`) | **안 됨** — 같은 이유 | 됨 |

성공 사례를 대본 내용까지 분석하려면 자막이 필요해서 PC에서 돌립니다.

## 저장소를 비공개로 바꾸기 (사례 폴더까지 전부 올리려면 — 먼저 한 번)

다른 채널의 자막 전문·댓글 전부·썸네일·영상은 **저장소가 비공개일 때만** GitHub 에 올라갑니다. 코드가 올리기 전에 GitHub 에 공개 여부를 물어보고, 공개면 요약 파일만 올립니다 (2026-10-13 확인: 지금은 **공개**).
1. GitHub 저장소 화면 → **Settings** → General 맨 아래 **Danger Zone** → **Change repository visibility** → **Make private** → 확인 문구 입력
2. 비공개가 되면 **토큰 없이는 코드를 받을 수 없습니다.** 그래서:
   - PC: `.env`의 `GITHUB_TOKEN`이 꼭 있어야 합니다 (아래 5번). 실행기 v2.1이 그 토큰으로 GitHub API 에서 코드를 받습니다.
   - Kaggle(내레이션): `guides/tts_guide.md` 3번 셀(v1.8)을 그대로 쓰면 Secrets 의 토큰으로 받습니다. 예전 셀은 `git clone`이 실패합니다.
   - Claude Code(클라우드): 세션에 연결된 GitHub 앱으로 받으므로 그대로 됩니다.
3. 비공개로 바꾼 뒤 첫 회차부터 `economic/result/outliers/`의 사례 폴더(`01_…`·`P01_…`)와 분석기 성공사례 영상(49MB 이하로 줄임)이 함께 올라갑니다.
(클라우드에서 받으려면 환경 설정 → 네트워크 접근 → 허용 도메인에 `www.youtube.com`·`i.ytimg.com`을 넣어야 합니다. YouTube가 클라우드 IP를 막을 수도 있어 PC가 더 확실합니다.)

## 처음 한 번 (Windows)

1. **Python 3.10 이상** 설치 — [python.org](https://www.python.org/downloads/) 설치 첫 화면에서 **"Add python.exe to PATH"** 체크
2. **Git** 설치 — https://git-scm.com/downloads (결과를 GitHub에 올릴 때 필요. 기본 설정 그대로 "Next")
3. 작업할 폴더를 만듭니다. 예: `문서\ytb`
4. 그 폴더에서 PowerShell을 엽니다 (탐색기 주소창에 `powershell` 입력 후 Enter) → 실행기를 받아 실행합니다.
   - **저장소가 공개일 때:**
     ```powershell
     curl.exe -L -o run_analyzer.ps1 https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/main/run_analyzer.ps1
     powershell -ExecutionPolicy Bypass -File run_analyzer.ps1
     ```
     (`curl.exe`는 Windows 10·11 에 들어 있고 PowerShell·명령 프롬프트·Git Bash 어디서나 됩니다. 예전 안내의 `wget … -OutFile`은 PowerShell 에서만 됨)
   - **저장소가 비공개일 때** (첫 줄이 토큰을 물어봄 — 5번의 GITHUB_TOKEN 값을 붙여넣고 Enter):
     ```powershell
     $t = Read-Host "GitHub 토큰"; $r = Invoke-RestMethod -Headers @{Authorization="Bearer $t"} -Uri "https://api.github.com/repos/yeomin1024/yeomin1024-ytb/contents/run_analyzer.ps1?ref=main"; [IO.File]::WriteAllBytes("$PWD\run_analyzer.ps1", [Convert]::FromBase64String($r.content)); Remove-Variable t
     powershell -ExecutionPolicy Bypass -File run_analyzer.ps1
     ```
     이미 받아 둔 `run_analyzer.ps1`이 v2.0이면 위 첫 줄로 한 번 새로 받으세요 (v2.0은 비공개 저장소에서 코드를 못 받음).
5. 처음에는 키가 없어서 멈추고 **`.env` 파일**이 생깁니다. 메모장으로 열어 `=` 뒤에 값을 붙여넣고 저장합니다 (따옴표 없이).
   ```
   YOUTUBE_API_KEY=AIza...         ← 필수
   GITHUB_TOKEN=github_pat_...     ← 비공개 저장소면 필수 (코드 받기·결과 올리기). 공개 저장소면 권장 (없으면 결과는 PC에만)
   ```
   - **YOUTUBE_API_KEY:** [Google Cloud 콘솔](https://console.cloud.google.com/) → 프로젝트 → API 및 서비스 → 라이브러리 → "YouTube Data API v3" 사용 → 사용자 인증 정보 → API 키 만들기. 클라우드 환경에 넣은 키와 같은 키를 써도 됩니다 (그러면 하루 10,000단위를 함께 씁니다).
   - **GITHUB_TOKEN:** GitHub → Settings → Developer settings → Personal access tokens → **Fine-grained tokens** → Generate new token → Repository access: **Only select repositories → `yeomin1024-ytb`** → Permissions → Repository permissions → **Contents: Read and write** → Generate. 나온 값(`github_pat_…`)을 붙여넣기.
   - `.env`는 이 PC에만 있고 GitHub에 올라가지 않습니다. 키 값은 로그에도 찍히지 않습니다 (`youtube_key=있음`처럼만).
6. 4번의 둘째 줄을 다시 실행합니다. 처음에는 패키지 설치로 몇 분 걸립니다.

macOS / Linux:
```bash
wget -O run_analyzer.sh https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/main/run_analyzer.sh     # 공개 저장소일 때
# 비공개 저장소일 때: read -rsp "GitHub 토큰: " T; echo; printf 'header = "Authorization: Bearer %s"\n' "$T" | curl -fsSL -K - -H "Accept: application/vnd.github.raw" -o run_analyzer.sh "https://api.github.com/repos/yeomin1024/yeomin1024-ytb/contents/run_analyzer.sh?ref=main"; unset T
bash run_analyzer.sh
```

## 실행하면 일어나는 일

실행기(`run_analyzer.ps1` / `.sh`, v2.1)가 코드를 최신으로 받고, 설정·검색어 파일은 없을 때만 받은 뒤 `tools/pc_analysis.py economic`을 실행합니다. 한 **회차**는:

| 순서 | 하는 일 | 할당량 (하루 10,000단위) |
|---|---|---|
| ① 성공 사례 + 조회수 상위 | `tools/outlier_research.py` v1.3 — `economic/keywords.toml`의 검색어 그룹 10개 × 앞 2개 × 길이 2(4~20분·20분 넘음) = 검색 40번 → 후보에서 두 묶음을 골라 **자막·썸네일·댓글 전부(답글 포함)**:<br>· **성공 사례 20개** — 최근 180일·구독자 5만 이하·조회수 ≥ 구독자×3·4분 이상 (폴더 `01_<영상ID>`…)<br>· **조회수 상위 20개 — 구독자 수 상관없음**, 주제 관련·4분 이상·최근 365일, 조회수 순 (폴더 `P01_<영상ID>`…, 성공 사례와 겹치면 그 폴더) | 첫날 최대 4,000 (검색 3,850 + 영상 정보·댓글). **분석기가 끝난 다음 날부터 9,500 — 거의 다 댓글에** |
| ② 주제 분석 | `youtube_topic_analyzer.py` — 검색어 50개로 주제 전체 분석 (키워드 기회·제목 패턴·길이·시청자 질문 등). **이월 검색어 없이 끝나면 다음 회차부터 건너뜀** (7일 안, 다시 돌리려면 `--rerun-analyzer`) | 최대 6,000 (`economic/analyzer_config.toml`의 `QUOTA_BUDGET`) |
| ③ 올리기 | 진행 상태 `pc_progress.json`을 쓰고 GitHub `economic/result/`에 푸시 — **비공개 저장소면 사례 폴더까지 전부** | 0 |
| ④ 남은 일이 있으면 | **할당량이 초기화될 때까지 기다렸다가 다음 회차** | — |

**댓글 전부의 할당량:** 영상마다 약 (최상위 댓글 수 ÷ 100) + (답글이 5개 넘는 댓글 수) 단위. 예: 댓글 3,000개 영상 ≈ 30~80단위. 40개 영상이면 보통 하루~이틀이고, 댓글이 아주 많은 영상이 있으면 며칠 걸립니다 — 쪽마다 저장하므로 멈춘 쪽부터 이어 받습니다. 받기 시작한 뒤 새로 달린 댓글은 빠질 수 있습니다 (시간 순으로 내려가며 받음).

**이어서 돌리기:** 두 도구 모두 받은 검색 결과(7일)·영상 정보·자막·댓글을 PC에 저장해 둡니다. 다음 회차는 받은 것은 할당량 0으로 다시 쓰고 **못 한 부분만 새로 받아** 결과에 더합니다.
- 남은 일 = 할당량 때문에 못 한 검색·영상 정보·댓글 (`economic/result/outliers/status.json`의 `pending`), 분석기의 이월 검색어 (`run_info.json`의 `keywords.deferred`), 네트워크 때문에 못 받은 자막
- **할당량 초기화 = 미국 태평양 시간 자정** → 한국 시간 **오후 4시**(3월 둘째 일요일 ~ 11월 첫 일요일, 서머타임) / **오후 5시**(그 밖). 실행기는 그 **10분 뒤**(16:10 / 17:10)에 다음 회차를 시작합니다.
- 화면 로그 예: `[ROUND] … round=1 complete=False left="성공 사례: 남은 검색 2·… / 분석기: 이월된 검색어 3개" next_round=2026-10-14T16:10+09:00`
- 남은 일에는 **댓글을 아직 다 못 받은 영상**도 들어갑니다 (`status.json`의 `pending.comments`).
- 최대 10회차(10일). 끝나면 `[DONE] … note="못 한 일 없음 — 끝"`.

## 기다리는 방법 둘 중 하나

**A. 창을 열어 두기 (기본)** — 위 명령을 실행해 두고 PowerShell 창을 닫지 않습니다. 남은 일이 있으면 알아서 다음 날 이어서 돌고, 다 끝나면 멈춥니다.
- PC가 **절전 모드**로 들어가면 그동안은 멈춥니다 (깨어나면 바로 이어서). 설정 → 시스템 → 전원 → "절전 모드 전환"을 **안 함**으로 두면 확실합니다.

**B. 작업 스케줄러에 맡기기 (창을 닫아도 됨)**
```powershell
powershell -ExecutionPolicy Bypass -File run_analyzer.ps1 -RegisterTask     # 매일 17:15 에 한 회차씩 (-Once)
powershell -ExecutionPolicy Bypass -File run_analyzer.ps1 -UnregisterTask   # 끄기
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
| PC `economic/result/outliers/` | `summary.md`·`outliers.csv`(성공 사례)·`popular.csv`(조회수 상위)·`candidates.csv`·`status.json` + 사례 폴더 `01_<영상ID>/`·`P01_<영상ID>/`: `transcript.txt`·`thumbnail.jpg`·`description.txt`·`metadata.json`·**`comments.csv`(댓글 전부, 좋아요 순 — 답글 여부·채널 주인 댓글 표시)**·`comments.jsonl`·`comments_state.json`(이어 받기) |
| GitHub `economic/result/` | 분석기 결과 + `pc_progress.json` + `outliers/` — **비공개 저장소: 사례 폴더까지 전부** / 공개 저장소: csv·md·json 요약만 |

- 댓글 기록에는 작성자 이름을 넣지 않습니다 (답글인지, 그 영상 채널 주인이 쓴 댓글인지만).
- 공개 저장소일 때도 `summary.md`에 사례마다 설명 앞부분·챕터·첫 20초·첫 1분 발췌·90초마다 흐름·말 속도·댓글 받은 수·인기 댓글 10개가 들어갑니다.

다 끝나면 Claude에게 **"economic 분석 끝났어, 결과로 지시사항이랑 주제 만들어줘"**라고 하면 `guides/pipeline.md` 2단계부터 진행합니다.

## 검색어 바꾸기

- 검색어 목록은 **`economic/keywords.toml`** 하나에 있습니다 (분석기와 성공 사례 수집이 같이 씀): `[KEYWORD_GROUPS]` 그룹별 검색어, `EXCLUDE_KEYWORDS`(제목에 있으면 뺌), `[relevance]` 주제 관련어.
- PC에 있는 파일은 실행기가 덮어쓰지 않습니다. 메모장으로 고치면 다음 회차부터 적용됩니다. GitHub 최신으로 바꾸려면 `-UpdateConfig` (기존 파일은 `.bak`).
- 성공 사례 수집은 그룹마다 **앞에서부터** `--per-group`개(기본 2)를 씁니다 → 중요한 검색어를 앞에 두세요.

## 여러 주제를 동시에

주제 폴더마다 **검색어 설정 파일**과 **키 설정 파일**이 따로 있고, 실행기가 주제마다 따로 돌립니다 (`tools/pc_analysis.py` v1.2).

| 파일 (주제마다) | 무엇 | 어디에 |
|---|---|---|
| `<주제>/keywords.toml` | 검색어 그룹·관련어 (분석기·성공 사례 수집이 같이 씀) | GitHub (Claude 가 만듦) → 실행기가 PC로 받음 (없을 때만) |
| `<주제>/analyzer_config.toml` | 주제 이름·저장 폴더·할당량 `QUOTA_BUDGET` 등 | 〃 |
| `<주제>/.env` | 이 주제만 쓰는 키 (`YOUTUBE_API_KEY`·`GITHUB_TOKEN`). **비우면 맨 위 `.env` 키** | **PC에만** (git 에 올라가지 않음). 처음 실행 때 빈 틀이 생김 |

키를 찾는 순서: `<주제>/.env` → 환경 변수 `YOUTUBE_API_KEY_<주제>`(예: `YOUTUBE_API_KEY_ECONOMIC`) → 맨 위 `.env` → 환경 변수 `YOUTUBE_API_KEY`.

```powershell
powershell -ExecutionPolicy Bypass -File run_analyzer.ps1 -Folder economic,health                 # 두 주제를 동시에
powershell -ExecutionPolicy Bypass -File run_analyzer.ps1 -Folder economic,health -RegisterTask   # 매일 17:15 에 두 주제 한 회차씩
```
macOS/Linux: `bash run_analyzer.sh --folder economic,health`

- 화면 줄 앞에 `[economic]`·`[health]`가 붙습니다. 주제마다 로그 `.yt_work/pc_analysis_<주제>.log`, 진행 `pc_progress_<주제>.json`, 잠금 파일이 따로라 서로 기다리지 않습니다.
- 패키지 준비(설치·yt-dlp 업데이트)는 처음에 한 번만 하고 주제마다 프로세스를 띄웁니다. 분석기의 git 작업 폴더·임시 폴더도 주제마다 따로입니다 (분석기 v2.6.0).
- **할당량:** YouTube 할당량은 Google Cloud **프로젝트**마다 하루 10,000단위입니다. 같은 키(같은 프로젝트)를 쓰는 주제가 N개면 실행기가 **하루 할당량을 N등분**합니다 (성공 사례·분석기 `QUOTA_BUDGET` 모두). 그만큼 주제마다 며칠 더 걸리지만, 남은 부분은 매일 자동으로 이어서 받습니다.
- ⚠️ **할당량을 늘리려고 Google Cloud 프로젝트를 주제마다 새로 만들어 키를 따로 쓰면 안 됩니다.** YouTube API 개발자 정책이 같은 도구를 여러 프로젝트로 나눠 할당량을 더 받는 것('sharding')을 금지하고, 어기면 할당량 축소·키 회수·계정 정지가 될 수 있습니다 ([정책 안내](https://developers.google.com/youtube/terms/developer-policies-guide)). 할당량이 더 필요하면 Google Cloud 콘솔의 **할당량 증가 신청**(YouTube API 준수 감사)을 하세요. `<주제>/.env`에는 정말 다른 용도·다른 사람의 프로젝트 키가 있을 때만 넣습니다.
- **새 주제 추가:** Claude 에게 "<주제> 검색어 만들어줘"라고 하면 `<폴더>/analyzer_config.toml`·`keywords.toml`을 만들어 main 에 올립니다. 그다음 `-Folder economic,<폴더>`로 실행. (직접 만들려면 `python youtube_topic_analyzer.py --topic <주제> --folder <폴더> --init-config` 후 `keywords.toml`을 채우고 `KEYWORD_MODE = "curated"`)

## 옵션

| 하고 싶은 것 | Windows | macOS / Linux |
|---|---|---|
| 한 회차만 | `-Once` | `--once` |
| 실행할 명령·다음 초기화 시각만 보기 | `--dry-run` | `-- --dry-run` |
| 설정·검색어 파일도 GitHub 최신으로 | `-UpdateConfig` | `--update-config` |
| 예전처럼 분석기만 한 번 | `-AnalyzerOnly` | `--analyzer-only` |
| 성공 사례·조회수 상위 할당량·개수 | `--outlier-quota 3000 --daily-quota 9500 --per-group 1 --top 15 --popular 30` | `-- --outlier-quota 3000 …` |
| 분석기를 다시 돌리기 (끝났어도) | `--rerun-analyzer` | `-- --rerun-analyzer` |
| 성공 사례만 / 분석기만 | `--skip-analyzer` / `--skip-outliers` | `-- --skip-analyzer` … |
| 다른 주제 폴더 / 여러 주제를 동시에 | `-Folder <폴더>` / `-Folder economic,health` | `--folder <폴더>` / `--folder economic,health` |

직접 실행: `python tools/pc_analysis.py economic [--once] [--dry-run]` · 점검: `python tools/pc_analysis.py --self-test`

종료 코드: `0` 다 끝남 · `3` 할당량 때문에 남은 일이 있음 (다음 실행이 이어서) · `2` 같은 주제가 이미 도는 중 · `1` 오류 (로그의 `next_step`·`hint` 확인)

## 문제 해결

- **`-File 매개 변수에 대한 인수 '.run_analyzer.ps1'이(가) 없습니다`** (2026-10-13 사용자 PC) → 경로의 `\`가 사라진 것입니다. **Git Bash**(또는 WSL·VS Code 의 bash 터미널)는 `\`를 지워 `.\run_analyzer.ps1`이 `.run_analyzer.ps1`이 됩니다. 그 창에서는 받기 줄(`wget … -OutFile`)도 PowerShell 문법이라 안 돼서 파일이 없을 수도 있습니다.
  1. 창이 **PowerShell**인지 확인 (프롬프트가 `PS C:\…>`로 시작). 아니면 시작 메뉴에서 "Windows PowerShell"을 열고 `cd` 로 작업 폴더로 이동
  2. 파일이 있는지: `dir run_analyzer.ps1` (Git Bash 면 `ls run_analyzer.ps1`). 없으면 `curl.exe -L -o run_analyzer.ps1 https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/main/run_analyzer.ps1`
  3. 실행은 `\` 없이: `powershell -ExecutionPolicy Bypass -File run_analyzer.ps1` — PowerShell·명령 프롬프트·Git Bash 어디서나 됩니다
- **`YOUTUBE_API_KEY 없음`** → `.env`를 메모장으로 열어 키를 넣고 저장 → 다시 실행
- **`같은 주제 분석이 이미 돌고 있음`** → 다른 창(또는 작업 스케줄러)에서 도는 중입니다. 확실히 멈춘 것이면 `--force`
- **자막이 `RequestBlocked`·`IpBlocked`** → 짧은 시간에 많이 받아 YouTube가 잠시 막은 것입니다. 남은 일로 세어 다음 회차에 다시 받습니다 (VPN은 끄세요).
- **`푸시 건너뜀 reason="GITHUB_TOKEN 없음"`** → `.env`에 토큰을 넣으면 다음 회차에 올라갑니다. 바로 올리려면 `python youtube_topic_analyzer.py --config economic/analyzer_config.toml --push-only`
- **실행기 `받기 실패 … 404`** → 저장소가 비공개인데 토큰이 없거나 그 저장소를 못 읽는 토큰입니다. `.env`의 `GITHUB_TOKEN`, 토큰의 Repository access(`yeomin1024-ytb`)·Contents 권한을 확인하세요.
- **`Permission … denied`** → 토큰의 Contents 권한이 Read and write인지, 저장소가 `yeomin1024-ytb`로 선택됐는지 확인 (`README.md` 문제 해결)
- **PowerShell "스크립트를 실행할 수 없습니다"** → 꼭 `powershell -ExecutionPolicy Bypass -File run_analyzer.ps1` 형태로 실행

## 변경 이력

| 버전 | 날짜 | 내용 |
|---|---|---|
| v1.3 | 2026-10-13 | 사용자 PC 오류 "-File 매개 변수에 대한 인수 '.run_analyzer.ps1'이(가) 없습니다": Git Bash 등이 `\`를 지움 → 모든 실행 명령을 `-File run_analyzer.ps1`로, 받기는 `curl.exe`, 문제 해결 항목 |
| v1.2 | 2026-10-13 | 사용자 지시: 여러 주제를 동시에 — "여러 주제를 동시에" 절(주제마다 검색어·키 파일, 키 찾는 순서, 같은 키 할당량 N등분, sharding 정책 경고, 새 주제 추가), 옵션 표 |
| v1.1 | 2026-10-13 | 사용자 지시: 댓글 전부(답글 포함, 쪽마다 이어 받기)·조회수 상위 20개(구독자 무관), 비공개 저장소면 사례 폴더까지 전부 올림·저장소를 비공개로 바꾸는 법·토큰으로 실행기 받기, 분석기가 끝난 날부터 할당량 9,500을 댓글에, 최대 10회차 |
| v1.0 | 2026-10-13 | 새로 만듦: PC 실행 방법, 회차·이어서 돌리기, 할당량 초기화 시각, 작업 스케줄러, 공개 저장소에 올리는 것·안 올리는 것 |
