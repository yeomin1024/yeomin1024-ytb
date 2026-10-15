# 지금 상태·다음 할 일 (인수인계)

버전: v1.1 — 2026-10-15 — 주식 1번 주제 백테스트·결론 끝 (`tools/backtest/` v1.1). (v1.0 — 2026-10-15 — 최초. 사용자 지시: "이제 이 대화 지울건데 남겨둬야 할 정보 있으면 저장소에 남겨놔".)

- 대화가 지워져도 다음 대화가 여기서 이어 가도록 남긴다.
- 규칙은 `CLAUDE.md`, 지시사항 목록은 `guides/README.md`, 전체 순서는 `guides/pipeline.md`에 있다.
- 이 문서는 **그때그때의 상태**만 적는다. 일이 끝나면 고친다 (버전을 올림).
- ※ 연구·교육용. 투자·세무 권유가 아니다.

## 1. 한눈에 (2026-10-15 기준)

| 주제 | 지금 단계 | 다음 할 일 |
|---|---|---|
| **재테크** `economic/` | 롱폼 4편 끝: 대본·오디오(Kaggle)·영상 렌더·업로드 시트(`upload.md`). 쇼츠 4편 제목·대본(`shorts/`, `0f6276e`) | ① 업로드 확인 ② 썸네일 3편 ③ 쇼츠 오디오·영상 (아래 2-2) |
| **주식** `stock/` | 분석 결과 올라옴. 주제 4개·채널 컨셉. **1번 백테스트·결론 끝** (`stock/source/tteoreojimyeon-sagi-2026-10/README.md`) | 1번 제목·대본 → 오디오 → 영상 / 2~4번은 일별 ETF 자료 필요 (아래 2-1) |

## 2. 다음 대화에서 할 일 (순서대로)

### 2-1. 주식 — 첫 영상

**지금까지**
- 채널 컨셉: **AI가 코드로 가설을 백테스트해 검증** (사용자 지시 2026-10-15).
  - 규칙: `stock/guides/concept.md`.
- 주제 4개와 근거: `stock/source/topic_candidates.md`.
  1. "떨어지면 사겠다" — 기다렸다 사기 vs 매달 사기 vs 한 번에
  2. "원금 안 깎여요" 커버드콜 — 분배금을 받아 쓰면 10년 뒤 원금은?
  3. 배당 ETF vs 지수 — 세금 떼고
  4. 레버리지 1·2·3배 25년 (닷컴 포함)
- 분석 자료: `stock/result/outliers/analysis.md` (2026-10-15T14:13Z, 승인 102개).
  - 성공 67개 중 7개는 주식이 아니다.
  - `stock/analysis_rules.toml` v1.2로 빼도록 고쳤다. PC가 다시 분석하면 반영된다.

**끝난 것 (2026-10-15)**
- 공통 백테스트 코드 `tools/backtest/` v1.1 — 자료(커밋 고정·캐시·검사)와 월별 엔진.
  - 시험 `tools/tests/test_backtest.py` 13개.
- 1번 `tteoreojimyeon-sagi-2026-10`: `backtest/run.py` v1.2 → `results.json`·`results.md`.
- 결론 (README 4번): "떨어지면 사겠다"고 기다리지 말고 정해진 날 매달 산다.
  - 2000년 이후 10년 기간 163번 중 117번은 매달 산 쪽이 더 많았다.
  - 기다린 쪽이 이겨도 최대 1.2% 더, 매달 산 쪽이 이기면 최대 25% 더 많았다.
  - −20% 이상 폭락을 기다리는 것은 폭락이 언제 오느냐에 따라 갈린다.
  - 목돈은 한 번에가 3번 중 2번 더 많지만, 최악 1년 −43%를 못 버티면 12달에 나눈다 (최악 −28%).

**할 일**
1. 1번 제목(`guides/title_guide.md`) → 대본(`guides/script_guide.md` + `stock/guides/concept.md` 1번 모양).
   - 숫자는 README 3번(= `results.json` 키)에서만 가져온다.
   - 그다음 `stock/source/used_content.md`.
2. 그다음 오디오(Kaggle) → 영상(`video/episodes/<영상ID>/index.html`) → 업로드 시트. 순서는 재테크와 같다.
   - 차트 자료는 `backtest/windows_main_10y.csv`.
3. 2~4번 주제(커버드콜·배당 vs 지수·레버리지)는 **일별 ETF 수정주가·분배금**이 필요하다.
   - Yahoo가 클라우드에서 막혀 있다 (4번 참고).
   - 사용자가 Network access에 `query1.finance.yahoo.com`·`query2.finance.yahoo.com`·`fc.yahoo.com`을 더하거나, PC에서 받은 자료를 `stock/data/`에 둔다.
   - 둘 다 안 되면 사용자에게 묻는다.

### 2-2. 재테크 — 남은 것

1. **업로드 확인**
   - 4편 모두 `youtube.json`(올린 기록)과 `drive.json`(Drive 기록)이 저장소에 없다.
   - 사용자가 원본을 Drive `내 드라이브/youtube/economic/<영상ID>.mp4`에 넣었는지, PC 업로더 `run_uploader.ps1`을 돌렸는지 묻는다.
   - 원본 mp4는 git에 없고 클라우드 컨테이너도 사라진다.
     - 다시 만들려면: `node video/render/render.mjs video economic <영상ID>` → `economic/out/<영상ID>/final_1080p.mp4`
     - 장면 파일·오디오·SRT는 저장소에 있다.
2. **썸네일**: `eunte-kkeonaeseugi-2026-10`만 있다 (`thumbnails/thumbnail_1~3`).
   - `gicho-yeongeum`·`isa-mangi`·`toejik-geonbo`는 프롬프트도 없다.
   - `guides/thumbnail_guide.md` v3.2 순서를 따른다: 프롬프트 → ChatGPT → 사용자가 대화에 붙임 → 검수 → `thumbnail_N.*`.
3. **쇼츠 4편**: 제목·대본만 있다 (`economic/source/<영상ID>/shorts/shorts.md`).
   - 오디오·영상은 아직이다 (`guides/shorts_guide.md` 4번).

## 3. PC에서 사용자가 돌리는 것 (명령)

| 무엇 | 명령 (PowerShell, 분석기 폴더) | 문서 |
|---|---|---|
| 분석기 (웹 화면, 주제 탭) | `powershell -ExecutionPolicy Bypass -File run_analyzer.ps1 -Folder stock` (여러 개: `-Folder economic,stock`) → `http://127.0.0.1:8765/` | `guides/pc_analysis.md`, `stock/README.md` |
| 실행기 새로 받기 | `curl.exe -L -o run_analyzer.ps1 https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/main/run_analyzer.ps1` | 같은 곳 |
| 캐시 비우기 | `run_analyzer.ps1 -ResetCache -Folder <주제>` (지우지 않고 `.yt_work/old/`로) | 같은 곳 |
| 유튜브 업로드 (예약 공개) | `powershell -ExecutionPolicy Bypass -File run_uploader.ps1` (`-DryRun` 확인만 · `-Auth` 처음 인증 · `-RegisterTask` 1시간마다 자동) | `guides/upload_guide.md` 11번 |
| 내레이션 | Kaggle 셀 하나 (범위 버튼: 전체·주제 하나) → `tools/tts_narration.py all --push` | `guides/tts_guide.md` |

- PowerShell은 **관리자가 아닌 창**으로 연다.
  - 관리자 창은 git '소유자가 다름' 문제를 만들었다. 분석기 v2.14.1이 자기 작업 폴더는 고쳐 둠.
- 코드가 바뀌어도 실행 명령은 같다. 켤 때마다 최신 코드를 받으니, 켜 둔 창은 닫고 다시 켠다.

## 4. 알려진 문제·주의

**클라우드 네트워크** (2026-10-15)
- 막힌 곳: Yahoo Finance, Stooq, FRED, KRX, 한국은행 ECOS, **law.go.kr**.
  - 그래서 `tools/law_text.py`로 법령을 확인하는 일도 지금은 클라우드에서 안 된다.
- 되는 곳: GitHub(raw 포함), pypi.
- 사용자가 클라우드 환경 설정 → Network access에서 도메인을 더하면 된다.

**YouTube API**
- 하루 10,000단위와 따로 **'하루 검색 횟수' 한도**가 있다 (HTTP 429).
  - 2026-10-09에 40번째 검색 뒤 막혔다.
  - 탐색은 멈추지 않고 검색만 다음 초기화 뒤로 미룬다. 웹 화면 0번 칸에 보인다.
- 할당량을 늘리려고 Google Cloud 프로젝트를 여러 개 만들라고 **권하지 않는다** (정책 위반 'sharding'). 정식 길은 할당량 증가 신청이다.
- PC의 키 장부(`.yt_work/quota_key_<지문>.json`)는 PC 사용량만 센다. 같은 키를 다른 곳에서 쓰면 화면 값보다 덜 남는다.

**Windows 전용 고침은 리눅스에서 흉내 내 시험했다**
- 장부 파일 바꿔치기 막힘(WinError 5) — `pc_analysis` v1.18.
- git '소유자가 다름' — 분석기 v2.14.1.
- 실제 Windows에서 다시 나면 로그를 받아 고친다.

**시험**
- 시험은 진짜 GitHub에 올리지 않는다. `GITHUB_TOKEN` 류를 지우고 저장소 이름을 가짜로 한다 (CLAUDE.md).
- 시험 실행: `cd tools/tests && python3 -m unittest discover -p "test_*.py"`
- `test_youtube_feedback`은 지운 옛 `stock/source/bittu-…` 폴더를 찾아 오류가 난다 (예전부터, 2026-10-13 옛 stock 지움).

**자료 안 비밀값**
- 비밀값(.env·키·토큰)은 커밋하지 않는다.
- 주제마다 키는 PC의 `<주제>/.env`에만 있다.

## 5. 2026-10-15 대화에서 정한 것 (사용자 지시)

| 지시 | 반영 |
|---|---|
| "키도 나눠서 쓸수 있게해 주제별로 다른키" | 주제마다 `<주제>/.env`. 키가 다르면 할당량 장부도 따로 (웹 화면 v2.1) |
| "주식은 외국 영상도 … on/off 기능(default off)" | `<주제>/analyzer_config.toml` `[search] INCLUDE_FOREIGN` (기본 false). 웹 화면 4번 칸 [외국 영상도] |
| "주식은 영어 주식 검색어도 추가해" | `stock/keywords_foreign.txt` 15개. 외국 영상을 켰을 때만 검색 |
| HTTP 429 "Search Queries per day" | 검색만 멈추고 나머지는 계속, 화면에 검색 수 (outlier_research v2.5) |
| WinError 5 · dubious ownership | 위 4번 |
| "주식 채널 컨셉은 ai로 코드 만들어서 가설을 백테스트해서 검증" | `stock/guides/concept.md`, 주제 4개 `stock/source/topic_candidates.md` |

## 변경 이력
| 버전 | 날짜 | 내용 |
|---|---|---|
| v1.1 | 2026-10-15 | 주식 1번 백테스트·결론 끝, 2~4번 자료 길 |
| v1.0 | 2026-10-15 | 최초 (대화를 지우기 전 인수인계) |
