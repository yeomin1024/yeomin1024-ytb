# yeomin1024-ytb — 0명 채널을 위한 YouTube 주제 분석 + 영상 제작 지시사항

주제(기본: 주식)에서 **어떤 영상이 구독자 수와 무관하게 터지는지** 분석하고, 그 결과를 근거로 **대본·제목·썸네일·모션그래픽 영상**을 만드는 저장소입니다.
연구·교육용입니다. 투자 조언이 아닙니다.

## 폴더 구조

```
youtube_topic_analyzer.py   ← 분석 코드 (모든 주제 공통)
run_analyzer.ps1            ← Windows: 분석 코드를 wget으로 받아 실행
run_analyzer.sh             ← macOS/Linux: 분석 코드를 wget으로 받아 실행
requirements.txt
tools/srt_tool.py           ← 대본 TXT → SRT 자막 생성·검사, 영상용·업로드용 변환 (모든 주제 공통)
guides/                     ← 영상 제작 공통 지시사항 (모든 주제) — guides/README.md 부터 읽기
  title_guide.md · script_guide.md · thumbnail_guide.md · video_guide.md · upload_guide.md · archive/
video/                      ← Remotion 프로젝트, 모든 주제가 같이 씀 — video/README.md (PC에 Node.js 필요)
stock/                      ← 주제 폴더: 주식
  analyzer_config.toml      ← 분석 설정 (검색 키워드·관련어 등) — 여기만 고치면 됨
  result/                   ← 분석 결과 (분석기가 GitHub에 올림)
  guides/                   ← 주식 전용 규칙 + data_insights.md(분석 결과 요약 = 지시사항 근거)
  titles/                   ← 제목 피드백 시트
  source/<영상ID>/          ← 영상별 대본 TXT·SRT·README·titles.md·thumbnails/·upload.md
  out/<영상ID>/             ← 장면 구성표·스토리보드 (완성 영상 mp4는 git에 올리지 않음)
selfdev/ · health/ · space/ · story/ · lifetips/   ← 다른 주제 폴더 (health는 규칙·첫 대본, story는 규칙 초안 — 둘 다 분석 결과 전까지 보류. 나머지는 분석 설정만)
```
| 폴더 | 주제 | 실행 |
|---|---|---|
| `selfdev/` | 자기계발 | `python youtube_topic_analyzer.py --config selfdev/analyzer_config.toml` |
| `health/` | 건강 | `python youtube_topic_analyzer.py --config health/analyzer_config.toml` |
| `space/` | 우주 | `python youtube_topic_analyzer.py --config space/analyzer_config.toml` |
| `story/` | 사연을 통한 교훈 | `python youtube_topic_analyzer.py --config story/analyzer_config.toml` |
| `lifetips/` | 생활꿀팁 | `python youtube_topic_analyzer.py --config lifetips/analyzer_config.toml` |

다른 주제도 `stock/`과 같은 모양의 폴더(예: `realestate/`)를 만들어 씁니다 → [새 주제 시작하기](guides/README.md#새-주제-시작하기-예-부동산)

---

## 1. 분석기 실행

### 클라우드(Claude Code)에서 — 키만 넣으면 Claude가 실행
- 클라우드 환경 설정에 `YOUTUBE_API_KEY`를 넣으면(`guides/pipeline.md` "처음 한 번 할 일" A·E) `.env` 없이 돌아갑니다 (분석기 v2.3.1).
- Claude에게 "stock 분석 돌려줘"라고 하면 `bash tools/run_analysis.sh stock`으로 실행하고 결과를 `stock/result/`에 넣어 main에 올립니다 (성공사례 영상 파일은 받지 않음).

### 방법 A — wget으로 받아서 실행 (새 폴더에서, 저장소를 받을 필요 없음)

**Windows (PowerShell)** — 작업할 빈 폴더에서:
```powershell
wget https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/main/run_analyzer.ps1 -OutFile run_analyzer.ps1
powershell -ExecutionPolicy Bypass -File .\run_analyzer.ps1
```
- `wget`은 Windows PowerShell 5.1(윈도우 기본)에 들어 있는 명령입니다.
- PowerShell 7을 쓰면 첫 줄 대신 `curl.exe -L -o run_analyzer.ps1 https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/main/run_analyzer.ps1`을 쓰세요.

**macOS / Linux:**
```bash
wget -O run_analyzer.sh https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/main/run_analyzer.sh
bash run_analyzer.sh
```

실행기가 하는 일:
1. `youtube_topic_analyzer.py`를 매번 최신으로 받는다.
2. `stock/analyzer_config.toml`은 **없을 때만** 받는다. 내가 고친 설정을 덮어쓰지 않는다.
3. `.venv` 가상환경을 만들고 실행한다. 필요한 패키지는 분석기가 자동 설치한다.

| 하고 싶은 것 | Windows | macOS / Linux |
|---|---|---|
| 다른 주제 | `.\run_analyzer.ps1 -Folder realestate -Topic 부동산` | `bash run_analyzer.sh --folder realestate --topic 부동산` |
| 설정 파일도 최신으로 (기존은 `.bak`) | `-UpdateConfig` | `--update-config` |
| main에 합치기 전 브랜치에서 받기 | `-Branch claude/dreamy-brown-r105x4` | `--branch claude/dreamy-brown-r105x4` |
| 분석기 옵션 전달 | `.\run_analyzer.ps1 --no-push --cases 3` | `bash run_analyzer.sh -- --no-push --cases 3` |

### 방법 B — 저장소를 받아서 실행
1. **Python 3.10 이상** 설치 — Windows는 [python.org](https://www.python.org/downloads/) 설치 화면에서 **"Add python.exe to PATH"** 체크
2. **Git** 설치 (GitHub에 결과 올릴 때 필요) — https://git-scm.com/downloads
3. `git clone https://github.com/yeomin1024/yeomin1024-ytb.git` → 그 폴더에서:
   ```
   python -m venv .venv
   .venv\Scripts\activate          # Windows   (macOS/Linux: source .venv/bin/activate)
   python youtube_topic_analyzer.py                                     # stock/analyzer_config.toml 로 실행
   ```

### 처음 실행할 때
- 같은 폴더에 `.env` 파일이 생깁니다. 메모장으로 열어 아래 값을 넣고 저장한 뒤 **다시 실행**하세요.
- `.env`는 `.gitignore`에 등록되어 GitHub에 올라가지 않습니다.
  ```
  YOUTUBE_API_KEY=AIza...        # 필수 — Google Cloud Console에서 YouTube Data API v3 사용 설정 후 API 키 발급
  GITHUB_TOKEN=github_pat_...    # 권장 — Fine-grained 토큰, 이 저장소 Contents: Read and write (없으면 PC에만 저장)
  ```
- 전체 실행 시간은 보통 10~30분입니다. 같은 날 다시 실행하면 API 응답이 캐시되어 쿼터를 거의 쓰지 않습니다.

### ⚙️ 설정 파일 — `stock/analyzer_config.toml`
검색 키워드처럼 **주제마다 바뀌는 값은 코드가 아니라 이 파일**에 있습니다. 메모장으로 열어 값만 고치면 됩니다.

| 구역 | 내용 |
|---|---|
| `[topic]` | 주제(`TOPIC`), 저장 폴더(`PROJECT_FOLDER`) |
| `[keywords]` · `[KEYWORD_GROUPS]` | 키워드 모드, **카테고리별 검색어** (기본 9개 카테고리·90개) |
| `[relevance]` | 주제 관련성 필터 — 무관한 영상(예: 홈쇼핑 방송 사고) 제외용 관련어 |
| `[ads]` | 광고로 조회수를 산 것으로 의심되는 영상 제외 기준 |
| `[advanced]` | (선택) 분석 기간·쿼터 예산·성공 기준 등 — `#`을 지우고 고치면 적용 |

- 우선순위: 코드 기본값 < 설정 파일 < 명령줄 옵션
- 오타·형식 오류는 실행 전에 알려 줍니다. 예: `QUOTA_BUDGTE(→ QUOTA_BUDGET?)`, "QUOTA_BUDGET: 숫자여야 함"
- 키워드 1개 = 검색 1회(100유닛)입니다.
  - 하루 한도는 10,000유닛이고, 프로젝트별 **일일 검색 횟수 한도**('Search Queries per day')도 있습니다.
  - 한도를 넘는 키워드는 **다음 날(한국시간 오후 4~5시 리셋 이후) 다시 실행하면 이어서 수집**합니다. 이미 받은 검색은 7일간 쿼터 0으로 재사용합니다.
  - 같은 날 여러 번 돌리면 검색 한도가 먼저 찹니다.

### 자주 쓰는 옵션
```
python youtube_topic_analyzer.py --config stock/analyzer_config.toml       # 설정 파일 지정
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

분석 결과를 지시사항에 쓸 수 있게 요약한 파일은 `<주제폴더>/guides/data_insights.md`입니다 (주식: [stock/guides/data_insights.md](stock/guides/data_insights.md)).

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
- **PowerShell에서 "스크립트를 실행할 수 없습니다":** `powershell -ExecutionPolicy Bypass -File .\run_analyzer.ps1`처럼 실행하세요.

---

## 2. 영상 만들기

전체 순서는 [`guides/pipeline.md`](guides/pipeline.md)에 있습니다 (Claude Code가 이 순서로 진행). 요약:
1. **분석** — 결과가 없으면 분석기 실행 (클라우드: `bash tools/run_analysis.sh <주제폴더>`, 키 `YOUTUBE_API_KEY`)
2. **지시사항·주제** — 분석 결과로 주제 규칙을 만들거나 고치고, 주제 후보를 고른다
3. **영상마다** — 대본 TXT·SRT, 제목 3개, 썸네일 **프롬프트** 3개, 업로드 시트, 영상 코드·스토리보드(승인) → 요약 문서 `summary.md`
4. **오디오가 생기면** (`<주제폴더>/source/<영상ID>/narration.mp3`) — SRT 맞춤 → 렌더 → 유튜브 **비공개** 업로드, 한 번에 최대 3개 (`bash tools/publish.sh`)
5. 그 뒤 스튜디오에서: 테스트 및 비교(썸네일 3개)·자동 더빙 확인·공개 전환 → 결과 기록

처음 한 번 할 일(키 4개 넣기, 채널 인증)은 [`guides/pipeline.md`](guides/pipeline.md) "처음 한 번 할 일"에 있습니다.

| 영상 | 상태 | 위치 |
|---|---|---|
| 몰빵 `molppang-2026-10` | 제작 완료 · v2.0 대본(엔론 삭제, 문장 91 / 자막 117) | `stock/source/molppang-2026-10/` |
| 물타기 `multagi-2026-10` | 대본 v1.3 (문장 91 / 자막 110) · 제목 T1 채택 · 썸네일 프롬프트 3개 · 업로드 시트 · 영상 1차 완성(무음) — 내레이션 녹음 대기 | `stock/source/multagi-2026-10/`, `stock/out/multagi-2026-10/` |
| 빚투 `bittu-2026-10` | 대본 v1.1 (문장 88 / 자막 105, 문장 27 뒤 고지 공백) · 제목 T1 채택 · 썸네일 프롬프트 3개 · 업로드 시트 · 영상 코드·스토리보드 — 내레이션 대기 | `stock/source/bittu-2026-10/` |
| 패닉셀 `panicsell-2026-10` | 대본 v1.0 (문장 92 / 자막 109, 문장 26 뒤 고지 공백) · 제목 T1 채택 · 썸네일 프롬프트 3개 · 업로드 시트 · 영상 코드·스토리보드 — 내레이션 대기 | `stock/source/panicsell-2026-10/` |
| 건강: 당뇨 전단계 `prediabetes-2026-10` | ⏸ 보류 — 사용자 지시(2026-10-10): 분석 결과가 없는 주제는 아직 진행하지 않음. 대본 (문장 86 / 자막 103)·제목·썸네일·업로드 시트는 만들어 둔 상태 | `health/source/prediabetes-2026-10/` |
| 사연 주제 | ⏸ 보류 — 같은 이유. 주제 규칙 초안(`story/guides/`)만 있음, 대본 없음 | `story/` |

자막 파일 검사·생성:
```
python tools/srt_tool.py check stock/source/multagi-2026-10/multagi-2026-10.txt stock/source/multagi-2026-10/multagi-2026-10.srt
python tools/srt_tool.py build <대본.txt> <새.srt> --reuse <기존.srt>   # 고친 문장만 새로 계산, 나머지는 기존 줄바꿈·길이 유지
python tools/srt_tool.py check <대본.txt> <자막.srt> --expect 91/117      # 문장 / 자막 / SRT–TXT 일치 / 고지 공백
python tools/srt_tool.py measure <대본.txt>                                # 문장별 자막 폭(1432px)과 앞줄·뒷줄
python tools/srt_tool.py remotion <대본.txt> <자막.srt> video/src/episodes/<영상ID>/subtitles.ts   # 영상용 데이터 (문장 번호 기준)
python tools/srt_tool.py upload <대본.txt> <자막.srt> --chapters "1=…;15=…"   # 챕터 시간 (SRT는 그대로 업로드)
# 녹음 후 (video/ 에서): npm run align-audio -- <주제폴더> <영상ID>   ← 오디오는 고치지 않고 SRT를 맞춤
```

자동 진행 도구 (저장소 최상위에서):
```
bash tools/run_analysis.sh stock                      # 1단계: 클라우드에서 분석 (환경변수 YOUTUBE_API_KEY)
python tools/make_summary.py --all                    # 3-5: 영상별 요약 문서 summary.md
python tools/make_summary.py --thumb-todo stock       # 이미지가 없는 썸네일 프롬프트 모음 → stock/thumbnail_todo.md
bash tools/publish.sh --dry-run                       # 4단계 대상 확인 (오디오 있음·아직 안 올림·영상 코드 있음)
bash tools/publish.sh                                 # 4단계: SRT 맞춤 → 렌더 → 비공개 업로드 (최대 3개)
python tools/youtube_upload.py stock <영상ID> --dry-run   # 업로드할 값만 확인
python tools/youtube_upload.py --check-auth           # 업로드 키 확인 (채널 이름)
python tools/youtube_auth.py --client-id … --client-secret …   # (내 PC에서 한 번) 업로드용 리프레시 토큰 발급
```

---

## 주의
- 연구/교육용 분석 도구이고, 영상은 투자 교육 콘텐츠입니다. 특정 종목의 매수·매도를 권유하지 않습니다.
- 이 저장소가 **public**이면 타인 영상 파일은 GitHub에 올리지 않고 **PC에만 원본 화질로** 저장합니다 (저작권).
  - private으로 바꾸면 영상도 GitHub에 함께 올라갑니다. 이때는 GitHub 용량 제한 때문에 49MB 이하로 재인코딩합니다.
- 렌더한 완성 영상(`*/out/**/*.mp4`)은 용량 때문에 git에 올리지 않습니다 (`.gitignore`).
- 변경 내역: 분석 코드는 [`CHANGELOG.md`](CHANGELOG.md), 지시사항은 각 파일 아래 "변경 이력" 표에 있습니다.
