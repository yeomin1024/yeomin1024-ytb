# yeomin1024-ytb — 0명 채널을 위한 YouTube 주제 분석 + 영상 제작 지시사항

주제(지금: **경제·재테크** `economic/`)에서 **어떤 영상이 구독자 수와 무관하게 터지는지** 분석하고, 그 결과를 근거로 **대본·제목·썸네일·모션그래픽 영상**을 만드는 저장소입니다.
연구·교육용입니다. 투자 조언이 아닙니다.

> 2026-10-13 사용자 지시로 주제 폴더를 모두 지우고(stock·stock_backup·health·lifetips·selfdev·space·story) `economic/` 하나로 새로 시작했습니다.
> 지운 폴더의 분석 결과·규칙·대본·업로드 기록은 git 기록 커밋 `2a68307`에 있습니다 (예: `git show 2a68307:stock/README.md`).

## 폴더 구조

```
youtube_topic_analyzer.py   ← 분석 코드 (모든 주제 공통)
run_analyzer.ps1            ← Windows: 코드를 받아 PC 분석 실행 (할당량 초기화 뒤 자동으로 이어서) — guides/pc_analysis.md
run_analyzer.sh             ← macOS/Linux: 같은 일
requirements.txt
tools/pc_analysis.py        ← PC 분석 실행기: 성공 사례 + 주제 분석 → GitHub, 남은 일은 할당량 초기화(한국 오후 4~5시) 뒤 자동으로 이어서
tools/outlier_research.py   ← 작은 채널 성공 사례(최근·구독자 5만 이하·조회수≥구독자×3·롱폼) + 자막·썸네일·댓글
tools/srt_tool.py           ← 대본 TXT → SRT 자막 생성·검사, 영상용·업로드용 변환 (모든 주제 공통)
tools/tts_narration.py      ← 대본 TXT → 내레이션 narration.mp3 하나 (Qwen3-TTS, Kaggle GPU). 사연자·진행자 두 목소리, 대본 전부 한 번에, 대본 폴더마다 GitHub에 자동으로(all --push) — guides/tts_guide.md
voices/                     ← 내레이션 목소리 설정: storyteller.json(사연자 S07) · host.json(진행자 H04) · ref/(기준 목소리 — 모든 대본이 복제)
guides/                     ← 영상 제작 공통 지시사항 (모든 주제) — guides/README.md 부터 읽기
  pipeline.md · pc_analysis.md · title_guide.md · script_guide.md · thumbnail_guide.md · video_guide.md · upload_guide.md · tts_guide.md · archive/
video/                      ← Remotion 프로젝트, 모든 주제가 같이 씀 — video/README.md (PC에 Node.js 필요)
economic/                   ← 주제 폴더: 경제·재테크 — economic/README.md
  analyzer_config.toml      ← 분석 설정 (주제 이름·저장 폴더·할당량 등)
  keywords.toml             ← 검색어 목록 (분석기·성공 사례 수집이 같이 씀) — 검색어는 여기만 고치면 됨
  .env                      ← (PC에만, git 제외) 이 주제만 쓰는 키 — 비우면 맨 위 .env. 여러 주제를 동시에: run_analyzer.ps1 -Folder economic,health
  result/                   ← 분석 결과 (PC 실행이 GitHub에 올림) · result/outliers/ 성공 사례·조회수 상위 (댓글 전부 — 비공개 저장소면 사례 폴더까지)
  guides/                   ← (분석 뒤) 주제 전용 규칙 + data_insights.md(분석 결과 요약 = 지시사항 근거)
  source/<영상ID>/          ← (주제를 고른 뒤) 영상별 대본 TXT·SRT·README·titles.md·thumbnails/·upload.md
  out/<영상ID>/             ← 완성 영상 자리 (mp4는 git에 올리지 않음). 스토리보드는 만들지 않음
```

다른 주제도 `economic/`과 같은 모양의 폴더(예: `realestate/`)를 만들어 씁니다 → [새 주제 시작하기](guides/README.md#새-주제-시작하기-예-부동산)

---

## 1. 분석기 실행

### 집 PC에서 — 권장 (자막·썸네일까지, 할당량이 끝나면 다음 날 자동으로 이어서)
**자세한 방법: [`guides/pc_analysis.md`](guides/pc_analysis.md)** — Windows는 작업할 폴더의 PowerShell에서:
```powershell
curl.exe -L -o run_analyzer.ps1 https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/main/run_analyzer.ps1
powershell -ExecutionPolicy Bypass -File run_analyzer.ps1                 # 끝날 때까지 (창을 열어 두기)
powershell -ExecutionPolicy Bypass -File run_analyzer.ps1 -RegisterTask   # 또는: 매일 17:15 에 한 회차씩 자동 (창을 닫아도 됨)
```
- 한 회차 = 성공 사례 수집(`tools/outlier_research.py`, 약 4,000단위) → 주제 분석(분석기, 6,000단위) → GitHub `economic/result/`에 올림.
- 할당량 때문에 못 한 검색·영상 정보·댓글·자막이 남으면 **할당량 초기화(태평양 자정 = 한국 오후 4시, 11~3월엔 5시) 10분 뒤** 다음 회차를 돌아 **못 한 부분만** 새로 받습니다 (받은 것은 캐시, 할당량 0).

### 클라우드(Claude Code)에서 — 검색·댓글만 (자막·썸네일은 네트워크 정책상 못 받음)
- 클라우드 환경 설정에 `YOUTUBE_API_KEY`를 넣으면(`guides/pipeline.md` "처음 한 번 할 일" A·E) `.env` 없이 돌아갑니다.
- Claude에게 "economic 분석 돌려줘"라고 하면 `bash tools/run_analysis.sh economic`으로 실행하고 결과를 `economic/result/`에 넣어 main에 올립니다 (성공사례 영상 파일은 받지 않음).

### 방법 A — wget으로 받아서 실행 (새 폴더에서, 저장소를 받을 필요 없음)

**Windows (PowerShell)** — 작업할 빈 폴더에서:
```powershell
curl.exe -L -o run_analyzer.ps1 https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/main/run_analyzer.ps1
powershell -ExecutionPolicy Bypass -File run_analyzer.ps1
```
- `wget`은 Windows PowerShell 5.1(윈도우 기본)에 들어 있는 명령입니다.
- `curl.exe`는 Windows 10·11에 들어 있어 PowerShell·명령 프롬프트·Git Bash 어디서나 됩니다. 실행 줄은 `.\` 없이 `-File run_analyzer.ps1` (Git Bash는 `\`를 지워 "-File 매개 변수에 대한 인수 '.run_analyzer.ps1'이(가) 없습니다" 오류가 남).

**macOS / Linux:**
```bash
wget -O run_analyzer.sh https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/main/run_analyzer.sh
bash run_analyzer.sh
```

실행기(v2.0)가 하는 일:
1. 코드(`youtube_topic_analyzer.py`·`tools/pc_analysis.py`·`tools/outlier_research.py`·`tools/outlier_stats.py`)를 매번 최신으로 받는다.
2. `economic/analyzer_config.toml`·`economic/keywords.toml`은 **없을 때만** 받는다. 내가 고친 설정·검색어를 덮어쓰지 않는다.
3. `.venv` 가상환경을 만들고 `tools/pc_analysis.py economic`을 실행한다. 필요한 패키지는 자동 설치한다.

| 하고 싶은 것 | Windows | macOS / Linux |
|---|---|---|
| 한 회차만 | `-Once` | `--once` |
| 매일 자동 (작업 스케줄러 / cron) | `-RegisterTask` · 끄기 `-UnregisterTask` | `--print-cron` → `crontab -e`에 붙여넣기 |
| 다른 주제 폴더 / 여러 주제를 동시에 | `-Folder realestate` / `-Folder economic,realestate` | `--folder realestate` / `--folder economic,realestate` |
| 설정·검색어 파일도 최신으로 (기존은 `.bak`) | `-UpdateConfig` | `--update-config` |
| 예전처럼 분석기만 한 번 | `-AnalyzerOnly` (뒤 인자는 분석기 옵션, 예: `--no-push --cases 3`) | `--analyzer-only -- --no-push --cases 3` |
| `tools/pc_analysis.py` 옵션 전달 | `.\run_analyzer.ps1 --dry-run` | `bash run_analyzer.sh -- --dry-run` |

### 방법 B — 저장소를 받아서 실행
1. **Python 3.10 이상** 설치 — Windows는 [python.org](https://www.python.org/downloads/) 설치 화면에서 **"Add python.exe to PATH"** 체크
2. **Git** 설치 (GitHub에 결과 올릴 때 필요) — https://git-scm.com/downloads
3. `git clone https://github.com/yeomin1024/yeomin1024-ytb.git` → 그 폴더에서:
   ```
   python -m venv .venv
   .venv\Scripts\activate          # Windows   (macOS/Linux: source .venv/bin/activate)
   python tools/pc_analysis.py economic                                  # 성공 사례 + 분석기, 남으면 다음 날 이어서
   python youtube_topic_analyzer.py --config economic/analyzer_config.toml   # 분석기만 한 번
   ```

### 처음 실행할 때
- 같은 폴더에 `.env` 파일이 생깁니다. 메모장으로 열어 아래 값을 넣고 저장한 뒤 **다시 실행**하세요.
- `.env`는 `.gitignore`에 등록되어 GitHub에 올라가지 않습니다.
  ```
  YOUTUBE_API_KEY=AIza...        # 필수 — Google Cloud Console에서 YouTube Data API v3 사용 설정 후 API 키 발급
  GITHUB_TOKEN=github_pat_...    # 권장 — Fine-grained 토큰, 이 저장소 Contents: Read and write (없으면 PC에만 저장)
  ```
- 전체 실행 시간은 보통 10~30분입니다. 같은 날 다시 실행하면 API 응답이 캐시되어 쿼터를 거의 쓰지 않습니다.

### ⚙️ 설정 파일 — `economic/analyzer_config.toml` + 검색어 파일 `economic/keywords.toml`
주제마다 바뀌는 값은 코드가 아니라 이 두 파일에 있습니다. 메모장으로 열어 값만 고치면 됩니다.

| 파일 · 구역 | 내용 |
|---|---|
| `analyzer_config.toml` `[topic]` | 주제(`TOPIC`), 저장 폴더(`PROJECT_FOLDER`) |
| `analyzer_config.toml` `[keywords]` | 키워드 모드, 검색어 파일 이름(`KEYWORDS_FILE = "keywords.toml"`) |
| `analyzer_config.toml` `[ads]` | 광고로 조회수를 산 것으로 의심되는 영상 제외 기준 |
| `analyzer_config.toml` `[advanced]` | (선택) 분석 기간·쿼터 예산·성공 기준 등 — `#`을 지우고 고치면 적용 |
| **`keywords.toml`** | **그룹별 검색어** `[KEYWORD_GROUPS]`(10개 그룹·50개) · `EXTRA_KEYWORDS` · `EXCLUDE_KEYWORDS` · `[relevance]` 주제 관련어(무관한 영상 제외) — 분석기와 `tools/outlier_research.py`가 같이 씀 |

- 우선순위: 코드 기본값 < 설정 파일 < 검색어 파일(목록만) < 명령줄 옵션
- 오타·형식 오류는 실행 전에 알려 줍니다. 예: `QUOTA_BUDGTE(→ QUOTA_BUDGET?)`, "QUOTA_BUDGET: 숫자여야 함"
- 키워드 1개 = 검색 1회(100유닛)입니다.
  - 하루 한도는 10,000유닛이고, 프로젝트별 **일일 검색 횟수 한도**('Search Queries per day')도 있습니다.
  - 한도를 넘는 키워드는 **다음 날(한국시간 오후 4~5시 리셋 이후) 다시 실행하면 이어서 수집**합니다. 이미 받은 검색은 7일간 쿼터 0으로 재사용합니다.
  - 같은 날 여러 번 돌리면 검색 한도가 먼저 찹니다.

### 자주 쓰는 옵션
```
python youtube_topic_analyzer.py --config economic/analyzer_config.toml    # 설정 파일 지정
python youtube_topic_analyzer.py --topic 부동산 --folder realestate --init-config   # 새 주제 설정 파일 만들기
python youtube_topic_analyzer.py --no-push                                 # GitHub 푸시 없이 PC에만
python youtube_topic_analyzer.py --cases 3 --no-video                      # 성공사례 3개, 영상 파일 없이(대본·썸네일만)
python youtube_topic_analyzer.py --push-only                               # 분석 없이, PC에 있는 결과만 GitHub에 푸시
python youtube_topic_analyzer.py --help                                    # 전체 옵션
```

### 결과물 (`<주제폴더>/result/`)
| 위치 | 내용 |
|---|---|
| `README.md` | 분석 리포트 — 추천 영상 아이디어, 첫 10개 업로드 플랜, 키워드·카테고리 기회점수, 제목 패턴, 포맷/길이, 타이밍, 채널 규모, 시청자 질문 |
| `analysis.xlsx`, `data/*.csv` | 모든 분석 표 |
| `charts/*.png` | 차트 12종 |
| `success_cases/NN_.../` | 성공사례별 `transcript.txt`(대본), `thumbnail.jpg`, `metadata.json`, `comments.csv` (영상 파일은 PC에만) |
| `run_info.json`, `run_log.txt` | 설정·쿼터·소요시간·데이터 기간 등 재현 정보와 전체 로그 |

| `outliers/` | 작은 채널 성공 사례 + 구독자 무관 조회수 상위 (`tools/outlier_research.py` v1.3): `summary.md`·`outliers.csv`·`popular.csv`·`candidates.csv`·`status.json` + 사례 폴더 `01_…`·`P01_…`(자막·**댓글 전부**·썸네일 — **저장소가 비공개일 때만** GitHub에, 공개면 PC에만) |
| `pc_progress.json` | PC 실행 진행 상태 (`tools/pc_analysis.py`): 회차·끝났는지·남은 일·다음 회차 시각 |

분석 결과를 지시사항에 쓸 수 있게 요약한 파일은 `<주제폴더>/guides/data_insights.md`입니다 (경제·재테크는 분석 뒤 만듦).

### 문제 해결
- **`Sign in to confirm you're not a bot`:** 가정용 인터넷에서는 드뭅니다.
  - VPN을 끄고 다시 실행하세요.
  - 또는 쿠키를 쓰세요: 시크릿 창에서 YouTube 로그인 → `youtube.com/robots.txt` 이동 → 확장 프로그램 *Get cookies.txt LOCALLY*로 `cookies.txt` 저장 → 시크릿 창 닫기 → **스크립트와 같은 폴더에 `cookies.txt`**를 두고 다시 실행 (자동 인식).
  - 또는 설정 `COOKIES_FROM_BROWSER = "firefox"`.
- **`Permission to yeomin1024/yeomin1024-ytb.git denied`** (푸시 거부): 토큰은 맞지만 **쓰기 권한이 없는** 상태입니다.
  - Fine-grained 토큰(`github_pat_…`): GitHub → Settings → Developer settings → Personal access tokens → Fine-grained tokens → 해당 토큰 → **Edit**
    ① Repository access에 `yeomin1024-ytb` 포함 ② Repository permissions → **Contents: Read and write** → Update (토큰 값은 그대로 사용 가능)
  - Classic 토큰(`ghp_…`): **repo** 범위 체크 → Update token
  - 고친 뒤 분석을 다시 돌릴 필요 없이 **`python youtube_topic_analyzer.py --push-only`**로 PC에 있는 결과만 올리면 됩니다.
- **`429 RATE_LIMIT_EXCEEDED ... 'Search Queries per day'`:** 오늘 검색 횟수 한도에 도달한 것입니다.
  - 스크립트가 바로 검색을 멈추고 남은 키워드를 이월합니다 → 한국시간 오후 4~5시 이후 같은 설정으로 다시 실행하세요.
  - 한도 확인: Google Cloud Console → API 및 서비스 → YouTube Data API v3 → 할당량
- **`[CONFIG] ❌ 설정 파일 형식 오류`:** 메시지의 줄·칸 번호를 확인하세요. 글자는 `"따옴표"` 안에, 목록은 `["가", "나"]`처럼 씁니다.
- **GitHub 푸시가 건너뛰어짐:** `.env`의 `GITHUB_TOKEN`과 Git 설치 여부를 확인하세요 (결과는 PC에 그대로 있음).
- **패키지 설치 실패:** 가상환경(.venv)을 켠 상태인지 확인 후 `python -m pip install -r requirements.txt`.
- **PowerShell에서 "스크립트를 실행할 수 없습니다":** `powershell -ExecutionPolicy Bypass -File run_analyzer.ps1`처럼 실행하세요.

---

## 2. 영상 만들기

전체 순서는 [`guides/pipeline.md`](guides/pipeline.md)에 있습니다 (Claude Code가 이 순서로 진행). 요약:
1. **분석** — 결과가 없으면 분석기 실행 (클라우드: `bash tools/run_analysis.sh <주제폴더>`, 키 `YOUTUBE_API_KEY`)
2. **지시사항·주제** — 분석 결과로 주제 규칙을 만들거나 고치고, 주제 후보를 고른다
3. **영상마다** — 대본 TXT·SRT(사례는 되도록 최신), 제목 3개, 썸네일 **프롬프트** 3개, 업로드 시트 → 요약 문서 `summary.md` (스토리보드 없음)
4. **오디오 만들기 (Kaggle 셀 하나)** — `python tools/tts_narration.py all --push`: 대본을 모두 읽어 사연자·진행자 목소리(`voices/`)로 영상마다 오디오 하나 → 대본 폴더마다 GitHub에 자동으로 올림 ([`guides/tts_guide.md`](guides/tts_guide.md))
5. **오디오가 생기면** (`<주제폴더>/source/<영상ID>/narration.mp3`) — 영상 코드가 없으면 Claude가 만들고(승인 없음) → SRT 맞춤 → 렌더 → 음량 맞춤(-14 LUFS) → 유튜브 **비공개** 업로드 + 1시간 뒤 예약 공개, 한 번에 최대 3개 (`bash tools/publish.sh`)
6. 그 뒤 스튜디오에서: 테스트 및 비교(썸네일 3개)·자동 더빙 확인·공개 전환 → 결과 기록

처음 한 번 할 일(키 4개 넣기, 채널 인증)은 [`guides/pipeline.md`](guides/pipeline.md) "처음 한 번 할 일"에 있습니다.

영상 목록: 아직 없음 — `economic/` 분석이 끝나고 주제를 고르면 `economic/source/<영상ID>/`에 만듭니다.
(2026-10-13 이전에 만든 영상 23개 — 주식 8개(채널에 올라간 몰빵·물타기·빚투·패닉셀 포함, 업로드 기록 `stock_backup/source/<영상ID>/youtube.json`)·건강·우주·자기계발·사연·생활꿀팁 각 3개 — 의 대본·기록은 커밋 `2a68307`에 있습니다.)

자막 파일 검사·생성:
```
python tools/srt_tool.py check economic/source/<영상ID>/<영상ID>.txt economic/source/<영상ID>/<영상ID>.srt
python tools/srt_tool.py build <대본.txt> <새.srt> --reuse <기존.srt>   # 고친 문장만 새로 계산, 나머지는 기존 줄바꿈·길이 유지
python tools/srt_tool.py check <대본.txt> <자막.srt> --expect 91/117      # 문장 / 자막 / SRT–TXT 일치 / 고지 공백
python tools/srt_tool.py measure <대본.txt>                                # 문장별 자막 폭(1432px)과 앞줄·뒷줄
python tools/srt_tool.py remotion <대본.txt> <자막.srt> video/src/episodes/<영상ID>/subtitles.ts   # 영상용 데이터 (문장 번호 기준)
python tools/srt_tool.py upload <대본.txt> <자막.srt> --chapters "1=…;15=…"   # 챕터 시간 (SRT는 그대로 업로드)
# 녹음 후 (video/ 에서): npm run align-audio -- <주제폴더> <영상ID>   ← 오디오는 고치지 않고 SRT를 맞춤
```

자동 진행 도구 (저장소 최상위에서):
```
python tools/pc_analysis.py economic                   # 1단계 (집 PC): 성공 사례 + 분석 → GitHub, 남으면 다음 날 자동으로 이어서 — guides/pc_analysis.md
bash tools/run_analysis.sh economic                   # 1단계 (클라우드): 분석기만 (자막·썸네일 없음, 환경변수 YOUTUBE_API_KEY)
python tools/make_summary.py --all                    # 3-5: 영상별 요약 문서 summary.md
python tools/make_summary.py --thumb-todo economic    # 이미지가 없는 썸네일 프롬프트 모음 → economic/thumbnail_todo.md
python tools/tts_narration.py all --push              # (Kaggle GPU) 대본 전부 → 영상마다 narration.mp3 하나 → 대본 폴더마다 GitHub에 올림 → guides/tts_guide.md
python tools/tts_narration.py check economic <영상ID>  # 저장소 오디오가 지금 대본으로 만든 것인지
python3 tools/outlier_research.py economic --per-group 2 --top 20 --popular 20   # 성공 사례 + 조회수 상위(구독자 무관), 댓글 전부 — (최근·구독자 5만 이하·조회수≥구독자×3·롱폼) + 자막·댓글·썸네일 → <주제>/result/outliers/ (다시 돌리면 남은 부분만)
python3 tools/outlier_stats.py economic               # 성공 사례 결과로 제목 요소·댓글 니즈 숫자 다시 계산 (주제 관련어는 keywords.toml)
python tools/tts_narration.py samples --push           # (Kaggle GPU) 목소리 후보 샘플 → voices/samples/ (목소리를 고르기 전에는 all 이 이것만 함)
python tools/tts_narration.py pick S04 H01             # 고른 목소리로 고정 (GPU 필요 없음 — 사용자가 고르면 Claude 가 실행)
bash tools/publish.sh --dry-run                       # 4단계 대상 확인 (오디오 있음·아직 안 올림·영상 코드 있음)
bash tools/publish.sh                                 # 4단계: SRT 맞춤 → 렌더 → 음량 맞춤(-14 LUFS) → 비공개 업로드 (최대 3개)
python tools/loudnorm.py --all                        # 이미 렌더한 영상들 음량만 다시 맞추기 (영상 스트림은 그대로)
python tools/youtube_upload.py economic <영상ID> --dry-run   # 업로드할 값만 확인
python tools/youtube_upload.py --check-auth           # 업로드 키 확인 (채널 이름)
python tools/youtube_auth.py --client-id … --client-secret …   # (내 PC에서 한 번) 업로드용 리프레시 토큰 발급
```

---

## 주의
- 연구/교육용 분석 도구이고, 영상은 투자 교육 콘텐츠입니다. 특정 종목의 매수·매도를 권유하지 않습니다.
- 이 저장소가 **public**이면 타인 영상 파일·성공 사례 폴더(자막 전문·댓글 전부·썸네일)는 GitHub에 올리지 않고 **PC에만** 저장합니다 (저작권).
  - **private으로 바꾸면 전부 GitHub에 함께 올라갑니다** (사용자 지시 2026-10-13 — 바꾸는 법: [`guides/pc_analysis.md`](guides/pc_analysis.md) "저장소를 비공개로 바꾸기"). 영상은 GitHub 용량 제한 때문에 49MB 이하로 재인코딩합니다.
  - 비공개 저장소는 토큰이 있어야 코드를 받습니다: PC는 `.env`의 `GITHUB_TOKEN`(실행기 v2.1), Kaggle은 `guides/tts_guide.md` 3번 셀(v1.8).
- 렌더한 완성 영상(`*/out/**/*.mp4`)은 용량 때문에 git에 올리지 않습니다 (`.gitignore`).
- 변경 내역: 분석 코드는 [`CHANGELOG.md`](CHANGELOG.md), 지시사항은 각 파일 아래 "변경 이력" 표에 있습니다.
