# 지금 상태·다음 할 일 (인수인계)

버전: v1.9 — 2026-10-16 — **재테크 분석을 클라우드로** (사용자 지시 "이 환경은 이제 저장소에 있는 재테크 주제 (economic 경로)를 유튜브 분석 코드 실행해서 분석하는 환경이야 기존 분석 결과에 이어서 한번 해보고 사용량 초기화 될때마다 분석을 계속 이어서하면 돼 캐시를 저장소에 남겨서 분석 이어서 할 수 있게 하고"): 첫 회차(승인 280 → 311, 성공 사례 162 → 182)·캐시 `economic/cloud_cache/`·매일 예약 작업 — 아래 2-3. (v1.8 — 2026-10-16 — **주식 분석을 클라우드에서** (`tools/cloud_run.py` v1.3 — 웹 화면 작업을 명령으로) · 주식 **외국 영상 켬** · 승인 102 → **185개** · `analysis.md` 다시 · 탐색 캐시 `stock/cloud_cache/cache.tgz` · **음성인식 보류** (아래 2-0). (v1.7 — 2026-10-16 — 주식 채널 **업로드 시험 성공** (클라우드에서 데모 40초 비공개 업로드, `stock/source/upload-test-2026-10-16/`). (v1.6 — 2026-10-16 — 재테크 채널 설정 문서 `economic/channel.md`(채널 설명·키워드). (v1.5 — 2026-10-16 — 주식 1번 소리 없는 미리보기 영상 렌더(추정 시각, `render.mjs` v1.2 `--estimated-preview` — 최종본 아님). (v1.4 — 2026-10-16 — 주식 1번 썸네일 프롬프트 v2.0(결말을 가림 — 두 선택 대치 + 닫힌 상자). (v1.3 — 2026-10-16 — 주식 1번 제목·대본 도입을 사용자 피드백대로 다시(결말 없음·맨 앞 니즈 낱말 '저점 매수'·'최고점보다 10%'·매수/매도, 대본 v1.2 141문장, 장면 파일 v1.1). (v1.2 — 2026-10-15 — 주식 1번: 제목(10개 언어)·대본 143문장·글자 없는 썸네일 프롬프트·업로드 시트·장면 파일(추정 시각) 끝, 오디오만 남음. (v1.1 — 주식 1번 주제 백테스트·결론 끝 (`tools/backtest/` v1.1).) (v1.0 — 2026-10-15 — 최초. 사용자 지시: "이제 이 대화 지울건데 남겨둬야 할 정보 있으면 저장소에 남겨놔".)

- 대화가 지워져도 다음 대화가 여기서 이어 가도록 남긴다.
- 규칙은 `CLAUDE.md`, 지시사항 목록은 `guides/README.md`, 전체 순서는 `guides/pipeline.md`에 있다.
- 이 문서는 **그때그때의 상태**만 적는다. 일이 끝나면 고친다 (버전을 올림).
- ※ 연구·교육용. 투자·세무 권유가 아니다.

## 1. 한눈에 (2026-10-15 기준)

| 주제 | 지금 단계 | 다음 할 일 |
|---|---|---|
| **재테크** `economic/` | 롱폼 4편 끝: 대본·오디오(Kaggle)·영상 렌더·업로드 시트(`upload.md`). 쇼츠 4편 제목·대본(`shorts/`, `0f6276e`) | ① 업로드 확인 ② 썸네일 3편 ③ 쇼츠 오디오·영상 ④ 채널 설정 붙였는지·결과로 키워드 고치기 (아래 2-2) |
| **재테크 분석** (클라우드) | 2026-10-16 첫 회차: 승인 롱폼 311(+31)·쇼츠 154, 성공 사례 182, 쇼츠 탐색 검색 15/36 (쇼츠 분석은 PC 결과 그대로 둠) | 예약 작업이 매일 한국 16:15(서머타임 끝나면 17:15)에 이어서 — 쇼츠 탐색 나머지 21개 → 쇼츠 분석 다시 (아래 2-3) |
| **주식** `stock/` | 1번 `tteoreojimyeon-sagi-2026-10`: 백테스트·제목 v2.0(10개 언어, 결말 없음)·대본 v1.2(도입에 결말 없음)·썸네일 프롬프트 v2.0(글자 없음·결말 가림)·업로드 시트 v2.0·**장면 파일 v1.1(추정 시각)** 끝 · **업로드 시험 성공**(클라우드 → STOCK LAB 채널, 비공개 데모 `3FJPCemQ0fw`) | ① 사용자: Kaggle 내레이션(범위 `stock`) ② 오디오가 오면 sync → check → video → Drive ③ 썸네일 ChatGPT ④ 다른 언어 오디오 여부(사용자 답) / 2~4번은 일별 ETF 자료 필요 (아래 2-1) |

## 2. 다음 대화에서 할 일 (순서대로)

### 2-0. 주식 분석 — 클라우드에서 (2026-10-16)

**정한 것 (사용자 지시 2026-10-16)**
- "이 환경은 이제 저장소에 있는 주식 주제 (stock 경로)를 유튜브 분석 코드 실행해서 분석하는 환경이야" → 주식 분석은 클라우드에서 `python3 tools/cloud_run.py stock …` (`stock/README.md` '클라우드에서 분석').
- "잠깐 주식 주제는 외국 영상도 포함해" → `stock/analyzer_config.toml` v3.2 `INCLUDE_FOREIGN = true`.
- "저장소에 올려" → 탐색 캐시 `stock/cloud_cache/cache.tgz` (새 컨테이너가 저절로 풂 — 검색을 다시 안 함).
- "일단 음성인식은 보류하고 시간되면 이어서 진행해" → **음성인식 안 함** (클라우드는 소리 받기가 막힘·Whisper 없음). PC 쪽을 '클라우드 결과를 받아 음성인식만' 하게 고치는 일도 보류.
- ⚠️ 그동안 PC 웹 화면은 **`-Folder economic`** 으로만 켠다 — PC 가 켤 때·음성인식 15분마다 자기 `stock/result/outliers/` 로 GitHub 것을 통째로 바꿔 클라우드 승인분이 지워짐. → **v1.9: 재테크도 클라우드라 PC 웹 화면은 아예 켜지 않는다** (아래 2-3).

**지금 (2026-10-16 16:20 KST)**
- 탐색 26주(외국 영상 포함): 검색 106/110번 (4번은 하루 검색 횟수 한도 429 — 91번째 뒤), 목록 2,350개.
- 승인 185개 (예전 102 + 오늘 83 — 추천 87개 중 주식이 아닌 4개 뺌: 힌디 영화 이야기·영화 결말 요약·인도 정당 채널·Daily Show).
- `stock/result/outliers/analysis.md` (2026-10-16 07:19 UTC): 성공 사례 111 · 비교 집단 343(성공 27%) · 같은 채널 기준선 52곳 · 수요공급 검색어 53 · 자동완성 435.
  - 성공 사례 글 출처: 자막 18 · 음성인식(앞 5분) 13 · 설명 78 · 없음 2.
- 외국 영상 켜기 전 한국어 검색 캐시 80개는 `.yt_work/old/` 로 옮겼다 (시장표의 검색어별 결과 수가 두 번 더해지지 않게).

**남은 일 (순서대로)**
1. **2026-10-16 22:23 KST 뒤** (자막 요청 6시간 쉼이 끝난 뒤): `python3 tools/cloud_run.py stock captions` — 대본 없는 승인 영상 130개의 자막만 다시 (할당량 0). 새 컨테이너면 쉼 기록이 없으므로 바로 됨. 받은 게 있으면 `analyze` → 커밋.
   - 연속 2번 막히면 저절로 6시간 쉼 (`orr.transcript`). 유튜브가 클라우드 주소를 로봇 확인(www.google.com/sorry — 막힌 주소 → ProxyError)이나 RequestBlocked 로 자주 막음 — 첫 승인 때 83개 중 24개만 받힘.
2. **2026-10-17 16:10 KST 뒤** (할당량 초기화): `python3 tools/cloud_run.py stock resume` — 못 받은 댓글 10개 · 새 채널 기준선 47곳 + 채널 정보 15곳 · 남은 검색 4번 → `python3 tools/cloud_run.py stock analyze` → `git add stock/result/outliers stock/cloud_cache` → main.
3. 그 뒤 새로 볼 것: `list --unchecked` 로 추천 밖의 좋은 영상, 쇼츠(`explore --shorts` — 검색 55번 ≈ 5,500단위·하루 검색 횟수 한도 주의).
4. 결과가 모이면: 주식 지시사항 재료 `stock/guides/data_insights.md` 다시 (외국 사례 포함 — 외국 사례의 제목·댓글 낱말 통계는 규칙으로 만들지 않음, CLAUDE.md).

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

**끝난 것 (2026-10-15, 이어서)**
- 주식 전용 지시사항 `stock/guides/` (README v1.1 = 전 세계 대상: 제목 10개 언어·글자 없는 썸네일·자막 없음·언어 없는 화면·실시간 비교 애니메이션, data_insights v1.1).
- 1번 제목 `titles.md` v2.0(한국어 R1~R3 + 9개 언어 — 2026-10-16 사용자 피드백으로 결말 없이, 맨 앞 '저점 매수'), 대본 v1.2 141문장(도입은 니즈·공감 → 질문 → 백테스트로 확인, 숫자 50개 `checklist.md` ✅), 썸네일 프롬프트 3개(`thumbnails/`, 글자 없음), 업로드 시트 `upload.md`(언어별 제목·설명 JSON, 자막 올리기 아니요).
- 장면 파일 `video/episodes/tteoreojimyeon-sagi-2026-10/index.html` v1.0 — 자막 없음·낱말 없음, 실시간 경주 3개(2000.01 · 2006.10 · 목돈 2008.04)·163번 토너먼트 막대 등. 숫자는 `backtest/anim.js`(← `anim_data.py`)만.
  - 2026-10-16 사용자 요청으로 **소리 없는 미리보기**를 렌더해 대화로 보냄 (`stock/out/tteoreojimyeon-sagi-2026-10/preview_estimated_silent.mp4` — 컨테이너에만, git·Drive 아님). 최종본은 오디오 뒤.
  - 지금 데이터 칸은 **추정 시각**(`render.mjs sync --estimate`, 9분 28초 — 대본 v1.2) — `check` 문제 0, still 78장 점검. 이 시각으로는 `video`가 거부된다.

**업로드 시험 (2026-10-16, 사용자 지시 "한번 업로드 잘되는지 데모 영상 만들어서 업로드 테스트해봐")**
- 데모 = 1번 장면 파일 도입 0~40초, 추정 시각·소리 없음 (`render.mjs video … --estimated-preview --from 0 --to 40`, 33초). 시트 `stock/source/upload-test-2026-10-16/upload.md`, 기록 `youtube.json`.
- 클라우드 환경 변수 키(`YOUTUBE_CLIENT_ID`·`SECRET`·`REFRESH_TOKEN`)의 채널 = **`편안한 음악 Relaxing Music` (UC7Rw5HWgKz5njCCciX8IVJQ)** — 사용자: "내가 아직 채널명 변경안해서 그래" → 이 채널이 STOCK LAB.
  - ⚠️ 그래서 클라우드 키로 **재테크(economic) 영상을 올리면 STOCK LAB 에 올라간다.** 클라우드에서 economic 을 올리지 않는다 (재테크는 PC 업로더·PC `.env` 키).
- 결과: https://youtu.be/3FJPCemQ0fw (비공개, 예약 없음) — 올리기·처리 성공, 언어별 제목·설명 9개 + ko, 기본·오디오 언어 ko, 교육, 아동용 아님, 자막 안 올림, 썸네일 등록 성공, 합성 콘텐츠 예(`videos.update` 응답으로 확인 — `videos.list` 는 이 칸을 안 보여 줌). 표는 시트 9번.
- 아직 모르는 것: 예약 공개(`publishAt`)는 시험 영상이 공개되면 안 돼서 걸지 않았다 · **비공개 잠금**(감사 전 API 프로젝트)은 API 로 안 보인다 → 사용자가 스튜디오에서 이 영상 공개 상태에 잠금 표시가 있는지 본다. 잠겨 있으면 예약 공개도 안 되니 `pipeline.md` '업로드 주의'.
- 사용자 할 일: 스튜디오에서 이 영상 확인 → 지우기 (`youtube.json` 은 기록으로 둔다 — 지우면 PC 업로더가 다시 올릴 영상으로 봄).

**할 일**
1. 사용자: Kaggle 셀에서 범위 `stock` → `narration.mp3`·`tts_narration.json` 이 `stock/source/tteoreojimyeon-sagi-2026-10/`에 올라옴.
   - 읽는 소리 `stock/tts_lexicon.tsv` (S&P500 → 에스앤피 오백).
2. 오디오가 오면: `git pull` → `python tools/tts_narration.py check stock tteoreojimyeon-sagi-2026-10` → `cd video && npm run align-audio -- stock tteoreojimyeon-sagi-2026-10`
   → `node video/render/render.mjs sync stock tteoreojimyeon-sagi-2026-10` → `check` → `stills`(점검) → `video` → `python tools/drive_videos.py upload stock tteoreojimyeon-sagi-2026-10` (Drive 권한이 없으면 원본을 대화로).
   - 실제 오디오 길이가 9~12분(`stock/guides/README.md` 5번)인지 본다. 추정은 9분 28초.
3. 썸네일: ChatGPT 메시지는 `thumbnails/README.md` 5번. 그림이 대화에 오면 검수(글자·숫자가 하나도 없는지 확대) → `thumbnail_N.*`.
   - **업로드는 클라우드에서 바로 된다** (2026-10-16 시험 — 아래 '업로드 시험'). 오디오 뒤 렌더가 끝나면 `python tools/youtube_upload.py stock tteoreojimyeon-sagi-2026-10 --dry-run` → `--publish-at +1h` (업로드 시트 7번). PC 업로더(`run_uploader.ps1 -Topic stock`)는 Drive 원본이 있을 때의 다른 길.
4. 사용자 답 기다림: 내레이션을 한국어 하나로 둘지, 다른 언어 오디오(자동 더빙 말고)를 만들지 (`stock/guides/README.md` 5번).
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
4. **채널 설정**: 채널 설명·채널 키워드·재생목록 3개는 `economic/channel.md` v1.1에 있다 (2026-10-16 사용자에게 알려 줌 — 키워드는 사용자 피드백으로 범용 재테크 23개로 줄임).
   - 사용자가 스튜디오에 붙였는지 묻는다.
   - 영상이 올라가고 2주쯤 지나면 스튜디오 '트래픽 소스 → 유튜브 검색 → 검색어'를 받아 키워드 순서를 고치고, 예고편 영상을 숫자로 고른다.
   - 영상이 늘면 설명의 '지금까지 다룬 주제'를 바꾼다.

### 2-3. 재테크 분석 — 클라우드에서 매일 이어서 (2026-10-16)

- 명령·기록: `economic/README.md` '클라우드에서 분석', 규칙 `guides/pc_analysis.md` '클라우드에서 돌리기'.
- 예약 작업 **'재테크 분석 이어서 (할당량 초기화 뒤 매일)'** `trig_01SqSL5wVdzeVt66GZbH4WCB` — cron `CRON_TZ=America/Los_Angeles 15 0 * * *`, 이 세션(`session_017oyVmRFNg1VHWX76syTr4A`)을 깨움. 순서: pull → status → resume → 탐색(롱폼·쇼츠 26주) → 새 추천 승인 → analyze → 커밋 → main(+ 세션 브랜치) 푸시 → 이 문서 1번 표.
- 캐시 `economic/cloud_cache/cache.tgz` (첫 회차 16.4MB, 파일 14,782개 — 검색 72·영상 정보 8,961·쇼츠 5,585·채널 업로드 목록 159).
  - ⚠️ 묶음이 통째로 바뀌므로 커밋마다 저장소 기록이 그만큼 커진다 (하루 한 번 ≈ 16MB). 커지면 파일별 저장(바뀐 파일만 기록)으로 바꾸는 것을 사용자에게 묻는다.
- 키: 클라우드 환경 변수 `YOUTUBE_API_KEY` — 주식 세션과 같은 키면 하루 할당량을 함께 쓴다(장부는 컨테이너마다 따로라 화면 값보다 덜 남을 수 있음). 재테크만 다른 키를 쓰려면 환경 변수 `YOUTUBE_API_KEY_ECONOMIC` (`outlier_research.load_api_key` 가 먼저 읽음).
- **PC 웹 화면은 켜지 않는다** (주식·재테크 모두 클라우드 — 켜면 PC 결과로 GitHub 사례 폴더가 바뀜). 음성인식(남은 약 411개 + 새로 27개)은 그래서 보류.
- 자막: 클라우드에서 대부분 막힘 (YouTube → `www.google.com/sorry` → `ProxyError`). 첫 회차 31개 중 4개만.

## 3. PC에서 사용자가 돌리는 것 (명령)

| 무엇 | 명령 (PowerShell, 분석기 폴더) | 문서 |
|---|---|---|
| 분석기 (웹 화면, 주제 탭) — ⚠️ **2026-10-16 부터 켜지 않음** (주식·재테크 모두 클라우드, 위 2-3) | `powershell -ExecutionPolicy Bypass -File run_analyzer.ps1 -Folder stock` (여러 개: `-Folder economic,stock`) → `http://127.0.0.1:8765/` | `guides/pc_analysis.md`, `stock/README.md` |
| 실행기 새로 받기 | `curl.exe -L -o run_analyzer.ps1 https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/main/run_analyzer.ps1` | 같은 곳 |
| 캐시 비우기 | `run_analyzer.ps1 -ResetCache -Folder <주제>` (지우지 않고 `.yt_work/old/`로) | 같은 곳 |
| 유튜브 업로드 (예약 공개) | `powershell -ExecutionPolicy Bypass -File run_uploader.ps1` (`-DryRun` 확인만 · `-Auth` 처음 인증 · `-RegisterTask` 1시간마다 자동) | `guides/upload_guide.md` 11번 |
| 내레이션 | Kaggle 셀 하나 (범위 버튼: 전체·주제 하나) → `tools/tts_narration.py all --push` | `guides/tts_guide.md` |

- PowerShell은 **관리자가 아닌 창**으로 연다.
  - 관리자 창은 git '소유자가 다름' 문제를 만들었다. 분석기 v2.14.1이 자기 작업 폴더는 고쳐 둠.
- 코드가 바뀌어도 실행 명령은 같다. 켤 때마다 최신 코드를 받으니, 켜 둔 창은 닫고 다시 켠다.

## 4. 알려진 문제·주의

**클라우드 네트워크** (2026-10-15 · 2026-10-16 고침)
- 2026-10-16 사용자가 허용: `www.youtube.com`(자막 — 그래도 유튜브가 자주 막음)·`i.ytimg.com`(썸네일)·`suggestqueries.google.com`(자동완성). `youtube.com` 만으로는 안 됨(→ www 로 넘김).
- 아직 막힘: `*.googlevideo.com`(소리 — 그런데 유튜브가 클라우드 주소에 '로봇 확인 로그인'을 요구해 허용해도 소리 받기는 안 됨, 2026-10-16 yt-dlp 시험), `www.google.com`(유튜브 로봇 확인 페이지).
- 막힌 곳: Yahoo Finance, Stooq, FRED, KRX, 한국은행 ECOS, **law.go.kr**.
  - 그래서 `tools/law_text.py`로 법령을 확인하는 일도 지금은 클라우드에서 안 된다.
- 되는 곳: GitHub(raw 포함), pypi.
- 사용자가 클라우드 환경 설정 → Network access에서 도메인을 더하면 된다.

**새 컨테이너에서 렌더하기 전** (2026-10-16)
- 글꼴·gsap 이 git 에 없다 → `node video/scripts/get-fonts.mjs` (Noto Sans·Serif KR → `video/public/fonts/`) + `cd video/render && npm install`. 글꼴이 없으면 `render.mjs` 가 `page.evaluate: NetworkError` 로 멈춘다.

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
| v1.9 | 2026-10-16 | 재테크 분석을 클라우드로 (첫 회차·캐시·매일 예약 작업), PC 웹 화면 켜지 않음 |
| v1.7 | 2026-10-16 | 주식 업로드 시험 성공 (클라우드 키 = STOCK LAB 채널, 지금 이름 '편안한 음악 Relaxing Music'), 렌더 전 글꼴 받기 |
| v1.8 | 2026-10-16 | 주식 분석을 클라우드에서 (`cloud_run.py` v1.3), 외국 영상 켬, 승인 185개, 음성인식 보류, 남은 일(2-0) |
| v1.1 | 2026-10-15 | 주식 1번 백테스트·결론 끝, 2~4번 자료 길 |
| v1.0 | 2026-10-15 | 최초 (대화를 지우기 전 인수인계) |
