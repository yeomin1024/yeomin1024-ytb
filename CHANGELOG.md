# CHANGELOG — youtube_topic_analyzer.ipynb

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
