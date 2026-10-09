# yeomin1024-ytb

## 📊 `youtube_topic_analyzer.ipynb` — 0명 채널을 위한 YouTube 주제 분석기 (Kaggle)

[![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/yeomin1024/yeomin1024-ytb/blob/main/youtube_topic_analyzer.ipynb)

'주식'(또는 원하는 주제)에서 **어떤 키워드·제목·포맷·길이의 영상이 구독자 수와 무관하게 터지는지** 분석하고,
결과를 이 저장소의 `<PROJECT_FOLDER>/<RESULT_FOLDER>/` (기본 `stock/result/`)에 저장합니다.

### 사용법 (Kaggle)
1. **노트북 열기**: 위 *Open in Kaggle* 버튼 — 또는 Kaggle → *Create → New Notebook* → *File → Import Notebook* 에서 이 `.ipynb` 업로드
2. **Internet 켜기**: 오른쪽 *Notebook options* → **Internet: On** (휴대폰 인증 계정 필요)
3. **Secrets 등록**: 상단 *Add-ons → Secrets* → 아래 이름으로 추가하고 **Attach(체크)**
   | Label | 값 |
   |---|---|
   | `YOUTUBE_API_KEY` | YouTube Data API v3 키 |
   | `GITHUB_TOKEN` | GitHub Fine-grained 토큰 (이 저장소, Contents: Read and write) |
   | `YTDLP_COOKIES` *(선택)* | 봇 확인 오류 시 cookies.txt (`base64 -w0 cookies.txt` 결과 권장) |
   | `YTDLP_PROXY` *(선택)* | 주거용 프록시 URL (`http://user:pass@host:port`) |
4. **블록 2 ⚙️** 에서 `TOPIC`(주제), `PROJECT_FOLDER`(결과 상위 폴더, 없으면 자동 생성) 지정
5. **Run All** — 결과를 Kaggle에도 보관하려면 **Save Version → Save & Run All**
6. *(선택)* *Accelerator → GPU T4* — 자막 없는 영상의 음성인식(Whisper)이 빨라집니다

### 🤖 `Sign in to confirm you're not a bot` 오류 해결
Kaggle(구글 클라우드 IP)은 YouTube 봇 확인에 자주 걸립니다. **로그인 쿠키**를 넣으면 대부분 해결됩니다.
1. 크롬/엣지 **시크릿 창**에서 YouTube 로그인 (**보조 구글 계정** 권장)
2. 같은 탭에서 `https://www.youtube.com/robots.txt` 이동 → 확장 프로그램 **Get cookies.txt LOCALLY** 로 `cookies.txt` 저장 → **시크릿 창 바로 닫기**
3. Kaggle: *Create → New Dataset* 으로 `cookies.txt` 업로드(**Private**) → 노트북 **Add Input** 으로 연결 (자동 인식)
   또는 Secret `YTDLP_COOKIES` 에 base64 값 등록 + Attach
4. **Stage 6 셀만 다시 실행** → Stage 7·8 실행
5. 그래도 막히면 결과의 `success_cases/download_on_pc.py` 를 **내 PC**에서 실행 (`pip install -U "yt-dlp[default]" deno imageio-ffmpeg` → `python download_on_pc.py`)

### 결과물
| 위치 | 내용 |
|---|---|
| GitHub `stock/result/README.md` | 분석 리포트 — 추천 영상 아이디어, 첫 10개 업로드 플랜, 키워드 기회점수, 제목 패턴, 포맷/길이, 타이밍, 채널 규모, 시청자 질문 |
| `analysis.xlsx`, `data/*.csv` | 모든 분석 표 |
| `charts/*.png` | 차트 11종 |
| `success_cases/NN_.../` | 성공사례별 `transcript.txt`(대본), `video.mp4`, `thumbnail.jpg`, `metadata.json`, `comments.csv` |
| `run_info.json`, `run_log.txt` | 설정·쿼터·소요시간·데이터 기간 등 재현 정보와 전체 로그 |
| Kaggle `/kaggle/working/stock/result/` + `stock_result.zip` | 위 전체 (영상 포함) — Output 탭에서 다운로드 |

### 주의
- 연구/교육용 분석 도구입니다. 투자 조언이 아닙니다.
- 이 저장소가 **public**이면 타인 영상 파일은 GitHub에 올리지 않고 **Kaggle 출력에만** 저장합니다 (저작권). private으로 바꾸면 영상도 GitHub에 함께 올라갑니다.
- Kaggle 노트북을 Public으로 공유하면 출력(영상 포함)도 공개되니 Private으로 유지하세요.
- 변경 내역은 [`CHANGELOG.md`](CHANGELOG.md) 참고.
