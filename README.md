# yeomin1024-ytb

## 📊 `youtube_topic_analyzer.py` — 0명 채널을 위한 YouTube 주제 분석기 (내 PC 실행용)

'주식'(또는 원하는 주제)에서 **어떤 키워드·제목·포맷·길이의 영상이 구독자 수와 무관하게 터지는지** 분석하고,
결과를 PC의 `output/<PROJECT_FOLDER>/<RESULT_FOLDER>/` 와 이 저장소의 `<PROJECT_FOLDER>/<RESULT_FOLDER>/` (기본 `stock/result/`)에 저장합니다.
Windows · macOS · Linux 에서 동작합니다.

### 처음 한 번 (준비)
1. **Python 3.10 이상** 설치 — Windows는 [python.org](https://www.python.org/downloads/) 설치 화면에서 **"Add python.exe to PATH"** 체크
2. **Git** 설치 (GitHub에 결과 올릴 때 필요) — https://git-scm.com/downloads
3. 이 저장소를 내려받기: `git clone https://github.com/yeomin1024/yeomin1024-ytb.git` (또는 `youtube_topic_analyzer.py` 파일만 받아도 됨)
4. 그 폴더에서 터미널(Windows: PowerShell) 열고 가상환경 만들기:
   ```
   python -m venv .venv
   .venv\Scripts\activate          # Windows
   source .venv/bin/activate       # macOS / Linux
   ```

### 실행
```
python youtube_topic_analyzer.py
```
- **처음 실행**하면 같은 폴더에 `.env` 파일이 생기고 필요한 패키지가 자동 설치됩니다(수 분).
  `.env` 를 메모장으로 열어 아래 값을 넣고 저장한 뒤 **다시 실행**하세요. (`.env` 는 `.gitignore` 에 등록되어 GitHub에 올라가지 않습니다)
  ```
  YOUTUBE_API_KEY=AIza...        # 필수 — Google Cloud Console에서 YouTube Data API v3 사용 설정 후 API 키 발급
  GITHUB_TOKEN=github_pat_...    # 권장 — Fine-grained 토큰, 이 저장소 Contents: Read and write (없으면 PC에만 저장)
  ```
- 전체 실행 시간: 보통 10~30분 (성공사례 영상 수·길이에 따라). 같은 날 다시 실행하면 API 응답이 캐시되어 쿼터를 거의 쓰지 않습니다.

### 자주 쓰는 옵션
```
python youtube_topic_analyzer.py --topic 부동산 --folder realestate   # 다른 주제 → 다른 폴더에 저장
python youtube_topic_analyzer.py --no-push                            # GitHub 푸시 없이 PC에만
python youtube_topic_analyzer.py --cases 3 --no-video                 # 성공사례 3개, 영상 파일 없이(대본·썸네일만)
python youtube_topic_analyzer.py --push-only                          # 분석 없이, PC에 있는 결과만 GitHub에 푸시
python youtube_topic_analyzer.py --help                               # 전체 옵션
```
그 밖의 설정(분석 기간, 성공 기준, 쿼터 예산 등)은 `youtube_topic_analyzer.py` 맨 위 **[설정 2]** 영역에서 바꿀 수 있습니다.

### 🔎 검색 키워드 (카테고리별)
`[설정 2]` 의 **`KEYWORD_GROUPS`** 에 카테고리별 검색어가 들어 있습니다 (기본: 투자 실패 사연·노후자금·가족 갈등·리딩방 피해·투자 방식 실패·폭락·교훈·판결/뉴스·사연 포맷 — 9개 카테고리 90개). 자유롭게 추가·삭제하세요.
- 키워드 1개 = 검색 1회(100유닛). 하루 한도(10,000유닛, 그리고 프로젝트별 **일일 검색 횟수 한도** 'Search Queries per day')를 넘는 키워드는 **다음 날(한국시간 오후 4~5시 리셋 이후) 다시 실행하면 이어서 수집**합니다 (이미 받은 검색은 7일간 쿼터 0으로 재사용). 같은 날 여러 번 돌리면 검색 한도가 먼저 찹니다.
- 리포트에 **카테고리(소재)별 기회** 표가 생겨, 어떤 사연 유형이 유리한지 비교할 수 있습니다.
- `KEYWORD_MODE = "autocomplete"` 로 바꾸면 예전처럼 주제어 자동완성으로 키워드를 자동 발굴합니다 (`"both"` = 둘 다).
- 검색 결과에 섞여 나오는 **주제와 무관한 영상**(예: 홈쇼핑 방송 사고)은 `RELEVANCE_TERMS` 기준으로 걸러서 분석·성공사례에서 제외합니다.
- **광고로 조회수를 산 것으로 의심되는 영상**(조회수는 많은데 좋아요·댓글이 거의 없음)도 성과 분석·성공사례에서 제외합니다 (`AD_SUSPECT_*` 설정).

### 결과물
| 위치 | 내용 |
|---|---|
| `README.md` (결과 폴더) | 분석 리포트 — 추천 영상 아이디어, 첫 10개 업로드 플랜, 키워드 기회점수, 제목 패턴, 포맷/길이, 타이밍, 채널 규모, 시청자 질문 |
| `analysis.xlsx`, `data/*.csv` | 모든 분석 표 |
| `charts/*.png` | 차트 12종 |
| `success_cases/NN_.../` | 성공사례별 `transcript.txt`(대본), `video.mp4`, `thumbnail.jpg`, `metadata.json`, `comments.csv` |
| `run_info.json`, `run_log.txt` | 설정·쿼터·소요시간·데이터 기간 등 재현 정보와 전체 로그 |

### 문제 해결
- **`Sign in to confirm you're not a bot`**: 가정용 인터넷에서는 드뭅니다. VPN을 끄고 다시 실행하거나, 시크릿 창에서 YouTube 로그인 → `youtube.com/robots.txt` 이동 → 확장 프로그램 *Get cookies.txt LOCALLY* 로 `cookies.txt` 저장 → 시크릿 창 닫기 → **스크립트와 같은 폴더에 `cookies.txt`** 를 두고 다시 실행 (자동 인식). 또는 설정 `COOKIES_FROM_BROWSER = "firefox"`.
- **`Permission to yeomin1024/yeomin1024-ytb.git denied`** (푸시 거부): 토큰은 맞지만 **쓰기 권한이 없는** 상태입니다.
  - Fine-grained 토큰(`github_pat_…`): GitHub → Settings → Developer settings → Personal access tokens → Fine-grained tokens → 해당 토큰 → **Edit** →
    ① Repository access 에 `yeomin1024-ytb` 포함 ② Repository permissions → **Contents: Read and write** → Update (토큰 값은 그대로 사용 가능)
  - Classic 토큰(`ghp_…`): **repo** 범위 체크 → Update token
  - 고친 뒤 분석을 다시 돌릴 필요 없이 **`python youtube_topic_analyzer.py --push-only`** 로 PC에 있는 결과만 올리면 됩니다.
  - 스크립트가 시작할 때 쓰기 권한을 미리 확인해서 알려주고, 분석이 도는 동안 `.env` 를 고쳐 저장하면 푸시 직전에 다시 읽습니다.
- **`429 RATE_LIMIT_EXCEEDED ... 'Search Queries per day'`**: 오늘 검색 횟수 한도에 도달한 것입니다. 스크립트가 바로 검색을 멈추고 남은 키워드를 이월합니다 → 한국시간 오후 4~5시 이후 같은 설정으로 다시 실행하세요. 한도 확인: Google Cloud Console → API 및 서비스 → YouTube Data API v3 → 할당량.
- **GitHub 푸시가 건너뛰어짐**: `.env` 의 `GITHUB_TOKEN` 과 Git 설치 여부 확인 (결과는 PC에 그대로 있음).
- **패키지 설치 실패**: 가상환경(.venv)을 켠 상태인지 확인 후 `python -m pip install -r requirements.txt`.

### 주의
- 연구/교육용 분석 도구입니다. 투자 조언이 아닙니다.
- 이 저장소가 **public**이면 타인 영상 파일은 GitHub에 올리지 않고 **PC에만 원본 화질로** 저장합니다 (저작권). private으로 바꾸면 영상도 GitHub에 함께 올라가며, 이때는 GitHub 용량 제한 때문에 49MB 이하로 재인코딩합니다.
- 변경 내역은 [`CHANGELOG.md`](CHANGELOG.md) 참고.
