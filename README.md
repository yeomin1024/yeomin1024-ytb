# yeomin1024-ytb

## 📊 `youtube_topic_analyzer.ipynb` — 0명 채널을 위한 YouTube 주제 분석기

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yeomin1024/yeomin1024-ytb/blob/main/youtube_topic_analyzer.ipynb)

'주식'(또는 원하는 주제)에서 **어떤 키워드·제목·포맷·길이의 영상이 구독자 수와 무관하게 터지는지** 분석하고,
결과를 이 저장소의 `<PROJECT_FOLDER>/<RESULT_FOLDER>/` (기본 `stock/result/`)에 저장합니다.

### 사용법
1. 위 **Open in Colab** 버튼으로 열기 (또는 `.ipynb` 파일을 받아 Colab에 업로드)
2. **블록 1 🔑**: `YOUTUBE_API_KEY`, `GITHUB_TOKEN` 입력 — Colab 왼쪽 🔑 Secrets에 같은 이름으로 저장하는 것을 권장
3. **블록 2 ⚙️**: `TOPIC`(주제), `PROJECT_FOLDER`(결과 상위 폴더, 없으면 자동 생성) 지정
4. `런타임 → 모두 실행` (대본 음성인식을 빠르게 하려면 T4 GPU 런타임 권장)

### 결과물 (`stock/result/`)
| 파일 | 내용 |
|---|---|
| `README.md` | 분석 리포트 — 추천 영상 아이디어, 첫 10개 업로드 플랜, 키워드 기회점수, 제목 패턴, 포맷/길이, 타이밍, 채널 규모, 시청자 질문 |
| `analysis.xlsx`, `data/*.csv` | 모든 분석 표 |
| `charts/*.png` | 차트 11종 |
| `success_cases/NN_.../` | 성공사례별 `transcript.txt`(대본), `video.mp4`, `thumbnail.jpg`, `metadata.json`, `comments.csv` |
| `run_info.json`, `run_log.txt` | 설정·쿼터·소요시간·데이터 기간 등 재현 정보와 전체 로그 |

### 주의
- 연구/교육용 분석 도구입니다. 투자 조언이 아닙니다.
- 이 저장소가 **public**이면 타인 영상 파일은 GitHub에 올리지 않고 Google Drive에 저장합니다 (저작권). private으로 바꾸면 영상도 함께 올라갑니다.
- 변경 내역은 [`CHANGELOG.md`](CHANGELOG.md) 참고.
