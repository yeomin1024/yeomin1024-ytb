# CHANGELOG — youtube_topic_analyzer

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
