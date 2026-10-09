# CHANGELOG — youtube_topic_analyzer.ipynb

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
