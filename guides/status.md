# 지금 상태·다음 할 일 (인수인계)

버전: v1.14 — 2026-10-16 — **주식 1번을 다시 만듦**: '매수 규칙 10가지 vs 사서 들고 있기(관망)' (`stock/source/eonje-maesu-2026-10/` — S&P 500 일별 총수익 32년·같은 $10,000·백테스트·대본 125문장·실시간 대시보드 장면·제목·업로드 시트·썸네일 프롬프트, 소리 없는 미리보기 렌더) · 예전 1번은 `_old/`로 (아래 2-1). 사용자 지시 "흔히 사용하는 매수 전략을 10가지 정도 골라서 그냥 매수하고 관망하는거랑 비교(투자 금액은 변동없이 동일하게)". (v1.13 — 2026-10-16 — **역사 분석 `history/` (클라우드)** — 폴더·규칙 새로, 매일 예약 작업 (아래 2-5). 사용자 지시 "이 환경은 이제 저장소에 있는 역사 주제 (history경로 없으면 만들것)를 유튜브 분석 코드 실행해서 분석하는 환경이야 사용량 초기화 될때마다 분석을 계속 이어서하면 돼 캐시를 저장소에 남겨서 분석 이어서 할 수 있게 하고". (v1.12 — 2026-10-16 — 재테크 4편 **완성 점검**: 렌더 4편 끝(이 컨테이너), 썸네일 프롬프트 3편(기초연금·ISA·건보료) 새로, 업로드 시트 v1.2(클라우드에서 바로 올림). 사용자 지시 "앞으로 여기서 재테크 영상 업로드 할거니까 영상 4개 완성하기 위해 뭐가 필요한지 확인하고 없으면 만들어". (v1.11 — 2026-10-16 — **새 채널 분야 탐색 `new/`** (분야 27개, 첫 탐색·분야 비교 — 아래 2-4, 추천 `new/channel_ideas.md`). (v1.10 — 2026-10-16 — 재테크 채널 **업로드 시험 성공** (재테크 클라우드 환경 키 = **부자백서**, 1편 도입 51초 실제 오디오·자막 구움, 비공개, `economic/source/upload-test-2026-10-16/`) · 업로드 도구 v1.7 올리기 전 채널 확인(`<주제>/youtube_channel.json`). (v1.9 — 2026-10-16 — **재테크 분석을 클라우드로** (사용자 지시 "이 환경은 이제 저장소에 있는 재테크 주제 (economic 경로)를 유튜브 분석 코드 실행해서 분석하는 환경이야 기존 분석 결과에 이어서 한번 해보고 사용량 초기화 될때마다 분석을 계속 이어서하면 돼 캐시를 저장소에 남겨서 분석 이어서 할 수 있게 하고"): 첫 회차(승인 280 → 311, 성공 사례 162 → 182)·캐시 `economic/cloud_cache/`·매일 예약 작업 — 아래 2-3. (v1.8 — 2026-10-16 — **주식 분석을 클라우드에서** (`tools/cloud_run.py` v1.3 — 웹 화면 작업을 명령으로) · 주식 **외국 영상 켬** · 승인 102 → **185개** · `analysis.md` 다시 · 탐색 캐시 `stock/cloud_cache/cache.tgz` · **음성인식 보류** (아래 2-0). (v1.7 — 2026-10-16 — 주식 채널 **업로드 시험 성공** (클라우드에서 데모 40초 비공개 업로드, `stock/source/upload-test-2026-10-16/`). (v1.6 — 2026-10-16 — 재테크 채널 설정 문서 `economic/channel.md`(채널 설명·키워드). (v1.5 — 2026-10-16 — 주식 1번 소리 없는 미리보기 영상 렌더(추정 시각, `render.mjs` v1.2 `--estimated-preview` — 최종본 아님). (v1.4 — 2026-10-16 — 주식 1번 썸네일 프롬프트 v2.0(결말을 가림 — 두 선택 대치 + 닫힌 상자). (v1.3 — 2026-10-16 — 주식 1번 제목·대본 도입을 사용자 피드백대로 다시(결말 없음·맨 앞 니즈 낱말 '저점 매수'·'최고점보다 10%'·매수/매도, 대본 v1.2 141문장, 장면 파일 v1.1). (v1.2 — 2026-10-15 — 주식 1번: 제목(10개 언어)·대본 143문장·글자 없는 썸네일 프롬프트·업로드 시트·장면 파일(추정 시각) 끝, 오디오만 남음. (v1.1 — 주식 1번 주제 백테스트·결론 끝 (`tools/backtest/` v1.1).) (v1.0 — 2026-10-15 — 최초. 사용자 지시: "이제 이 대화 지울건데 남겨둬야 할 정보 있으면 저장소에 남겨놔".)))))))))))))

- 대화가 지워져도 다음 대화가 여기서 이어 가도록 남긴다.
- 규칙은 `CLAUDE.md`, 지시사항 목록은 `guides/README.md`, 전체 순서는 `guides/pipeline.md`에 있다.
- 이 문서는 **그때그때의 상태**만 적는다. 일이 끝나면 고친다 (버전을 올림).
- ※ 연구·교육용. 투자·세무 권유가 아니다.

## 1. 한눈에 (2026-10-15 기준)

| 주제 | 지금 단계 | 다음 할 일 |
|---|---|---|
| **재테크** `economic/` | 롱폼 4편: 대본·오디오·장면·업로드 시트 v1.2 끝 · **완성 렌더 4편 끝**(2026-10-16, 이 클라우드 컨테이너에만) · 썸네일: 1편 이미지 있음, 2~4편 프롬프트만(이미지 기다림) · 부자백서 채널에는 아직 시험 영상 1개뿐 · 쇼츠 4편 제목·대본만 | ① 사용자: 시험 영상 잠금 확인 → 1편 업로드 시각 정하기 ② 사용자: 2~4편 썸네일 ChatGPT → Claude 검수 → 업로드 ③ 쇼츠 오디오·영상 ④ 채널 설정 (아래 2-2) |
| **재테크 분석** (클라우드) | 2026-10-16 첫 회차: 승인 롱폼 311(+31)·쇼츠 154, 성공 사례 182, 쇼츠 탐색 검색 15/36 (쇼츠 분석은 PC 결과 그대로 둠) | 예약 작업이 매일 한국 16:15(서머타임 끝나면 17:15)에 이어서 — 쇼츠 탐색 나머지 21개 → 쇼츠 분석 다시 (아래 2-3) |
| **주식** `stock/` | **1번을 다시 만듦 (2026-10-16)** `eonje-maesu-2026-10` — 매수 규칙 10가지 vs 관망, S&P 500 총수익 1991~2023 일별·같은 $10,000: 백테스트(엔진 `daily.py` v1.0·다시 계산 일치·숫자 117개 ✅)·제목 v1.0(10개 언어, 결말 없음)·대본 v1.0 125문장(추정 9분 4초)·**실시간 대시보드 장면 v1.0**(check 문제 0, 소리 없는 미리보기 렌더)·업로드 시트 v1.0·썸네일 프롬프트 3개 · 예전 1번은 `_old/` · 업로드 시험 성공(STOCK LAB, 비공개 데모 `3FJPCemQ0fw`) | ① 사용자: Kaggle 내레이션(범위 `stock`) ② 오디오가 오면 sync → check → video → 클라우드에서 바로 업로드(`--publish-at +1h`) ③ 썸네일 ChatGPT(`stock/thumbnails_chatgpt.md`) ④ 다른 언어 오디오 여부(사용자 답) / 2~4번은 일별 ETF 자료 필요 (아래 2-1) |
| **새 채널 탐색** `new/` | 2026-10-16 첫 탐색: 분야 27개 · 검색 88번(8,918단위) · 표본 2,898 → `new/result/niche/niche_scan.md` · 추천 `new/channel_ideas.md` (1 역사 해설 · 2 시니어 건강(실험·숫자형) · 3 심리, 사연은 보류) | 사용자가 **역사**를 고름 (2026-10-16) → `history/` (아래 2-5). 건강·심리는 아직 (아래 2-4) |
| **역사 분석** `history/` (클라우드) | 2026-10-16 폴더·규칙만 (설정 5개 · `topics.txt`). 태그 씨앗 검색은 **못 함** — 키 `58333e86` 이 '하루 검색 횟수' 한도(429)에 걸림 (같은 날 `new/` 검색 88번) · 검색어 0 · 승인 0 | 예약 작업이 매일 한국 16:20(서머타임 끝나면 17:20)에 이어서 — 첫 회차 10-17: 씨앗 검색 → 검색어 40개 → 탐색 26주 → 승인 → `analysis.md` (아래 2-5) |

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
- 주제 후보와 근거: `stock/source/topic_candidates.md` (v1.1 — 1번을 '매수 규칙 10가지 vs 관망'으로 바꿈).
  1. **(지금 1번)** 매수 타이밍 — 흔히 쓰는 매수 규칙 10가지 vs 사서 들고 있기(관망), 같은 1만 달러
  2. "원금 안 깎여요" 커버드콜 — 분배금을 받아 쓰면 10년 뒤 원금은?
  3. 배당 ETF vs 지수 — 세금 떼고
  4. 레버리지 1·2·3배 25년 (닷컴 포함)
- 분석 자료: `stock/result/outliers/analysis.md` (클라우드 분석, 승인 185개 — 2-0).

**1번을 다시 만듦 (2026-10-16, 사용자 지시 "매수 전략을 2가지만 비교하고 금액이 정해지지 않아서 비교가 힘들잖아 … 흔히 사용하는 매수 전략을 10가지 정도 골라서 그냥 매수하고 관망하는거랑 비교(투자 금액은 변동없이 동일하게) … 전력을 다하라고")**
- 새 1번 = **`stock/source/eonje-maesu-2026-10/`** (README v1.0에 방법·근거·결과·한계). 예전 1번(떨어지면 사기 vs 매달 사기)은 `stock/source/_old/tteoreojimyeon-sagi-2026-10/`·`video/episodes/_old/`로 보관 — 도구가 보지 않음 (`stock/source/_old/README.md`).
- 자료: **S&P 500 일별 총수익(배당 재투자) 1991-01-02 ~ 2023-06-30 (32년)** — 클라우드가 Yahoo·FRED를 못 열어 **pypi 휠에 든 자료**(skfolio 1.9.0 S&P 500 일별 + FRED 2016-02-12부터 이어 붙임 — 겹치는 날 차이 최대 0.12%(2일) · arch 8.0.0과는 같음)에 Shiller 월 배당을 날로 나눠 더함. 나스닥(가격만)·Fama-French 무위험 금리는 확인용. 모두 sha256 고정 (`tools/backtest/data.py` v1.2).
- 규칙: 모두 **$10,000 한 번** (더 넣지 않음) · 신호는 그날 종가, 매매는 **다음 거래일 종가**(미래 정보 없음) · 비용 0.1% · 현금 이자 0. 엔진 `tools/backtest/daily.py` v1.0 (시험 12개 `tools/tests/test_backtest_daily.py`), 따로 다시 계산한 `backtest/verify.py`와 같음.
- 10가지 (영상 순서): 12개월 분할 · 고점 −10% 저점 매수 · 물타기(¼씩 −10·−20·−30%) · 익절 +10% · RSI 30/70 · 신고가 돌파 55/20일 · 200일선 · 골든·데드 크로스 50/200 · 12개월 모멘텀 · 손절 −10%(+10% 반등 재매수). 근거 = 주식 분석 댓글 73,272개 낱말 수 (README 2번).
- 결과 (`backtest/results.md`): 32년 한 번 → 관망 $259,164보다 많은 규칙 **1/10**(손절 −10% $303,475), 최대 낙폭이 더 작은 규칙 7/10 · 10년 기간 271번 → 손절 193·골든 크로스 189·모멘텀 153번 이김, **이긴 기간은 거의 다 40% 넘는 폭락이 든 기간**(폭락 없는 76번에서는 0~9번) · 20년 151번·나스닥 109번으로 확인 (나스닥에서는 손절 24/109).
- 대본 v1.0 **125문장, 추정 9분 4초**(도입 s1–5 약 22초 — 결과를 말하지 않음, 매수·매도 낱말) · 숫자 117개 `checklist.md` ✅ (`backtest/check_numbers.py`) · 읽는 소리 `stock/tts_lexicon.tsv` v1.1 (RSI → 알에스아이).
- 장면 `video/episodes/eonje-maesu-2026-10/index.html` v1.0 — **실시간 대시보드**: 날짜 카운터, 위 = A(관망)·B(규칙) 평가 금액 곡선(로그), 아래 = S&P 500 가격 + 매수▲·매도▼ 표시, 옆 = A·B 금액·배수·B÷A·지금 주식/현금·거래 수·마지막 거래 손익 막대, 폭락 구간 띠. 끝에 종합(끝 값 막대·271칸 지도·낙폭 막대·20년·나스닥·한계·정리). 숫자는 `backtest/anim.js`(← `anim_data.py` v1.1)만. `render.mjs check` 문제 0 · 소리 없는 미리보기 렌더 끝 (544.2초, `stock/out/eonje-maesu-2026-10/preview_estimated_silent.mp4` — 컨테이너에만, git 아님).
- 제목 `titles.md` v1.0 R1 "매수 타이밍, 손절·익절·이평선 등 매수 규칙 10가지는 사서 들고만 있기보다 더 벌까? 32년 백테스트"(58자) + 9개 언어 · 업로드 시트 `upload.md` v1.0 (`--dry-run`: 문제는 '영상 파일 없음' 하나) · 썸네일 프롬프트 3개(글자 없음·결말 가림) + `stock/thumbnails_chatgpt.md`.

**업로드 시험 (2026-10-16, 사용자 지시 "한번 업로드 잘되는지 데모 영상 만들어서 업로드 테스트해봐")**
- 데모 = 예전 1번 장면 도입 0~40초, 추정 시각·소리 없음. 시트 `stock/source/upload-test-2026-10-16/upload.md`, 기록 `youtube.json`.
- 클라우드 환경 변수 키(`YOUTUBE_CLIENT_ID`·`SECRET`·`REFRESH_TOKEN`)의 채널 = **`편안한 음악 Relaxing Music` (UC7Rw5HWgKz5njCCciX8IVJQ)** — 사용자: "내가 아직 채널명 변경안해서 그래" → 이 채널이 STOCK LAB.
  - ⚠️ **클라우드 환경마다 키가 다르다** — 주식 환경 키 = STOCK LAB, **재테크 환경 키 = 부자백서** (2026-10-16 확인, 2-2). 업로드 도구 v1.7 이 올리기 전에 키의 채널을 `<주제>/youtube_channel.json` 과 비교해 다르면 멈춘다.
- 결과: https://youtu.be/3FJPCemQ0fw (비공개, 예약 없음) — 올리기·처리 성공, 언어별 제목·설명 9개 + ko, 기본·오디오 언어 ko, 교육, 아동용 아님, 자막 안 올림, 썸네일 등록 성공, 합성 콘텐츠 예. 표는 시트 9번.
- 아직 모르는 것: 예약 공개(`publishAt`)는 걸지 않았다 · **비공개 잠금**(감사 전 API 프로젝트)은 API 로 안 보인다 → 사용자가 스튜디오에서 잠금 표시를 본다 (`pipeline.md` '업로드 주의').
- 사용자 할 일: 스튜디오에서 이 영상 확인 → 지우기 (`youtube.json` 은 기록으로 둔다).

**할 일**
1. 사용자: Kaggle 셀에서 범위 `stock` → `narration.mp3`·`tts_narration.json` 이 `stock/source/eonje-maesu-2026-10/`에 올라옴 (`_old/`는 안 읽음).
2. 오디오가 오면: `git pull` → `python tools/tts_narration.py check stock eonje-maesu-2026-10` → `cd video && npm run align-audio -- stock eonje-maesu-2026-10`
   → `node video/render/render.mjs sync stock eonje-maesu-2026-10` → `check` → `stills`(점검) → `video`.
   - 새 컨테이너면 먼저 `node video/scripts/get-fonts.mjs` + `cd video/render && npm install` (4번).
   - 장면의 문장 기준점(`SEG`)은 문장 시각을 따르므로 오디오 시각만 바뀌면 그대로 된다. 실제 길이가 9~12분(`stock/guides/README.md` 5번)인지 본다.
3. 업로드 (클라우드에서 바로): `python tools/youtube_upload.py stock eonje-maesu-2026-10 --dry-run` → `--publish-at +1h` (시트 7번). PC 업로더(`run_uploader.ps1 -Topic stock`)는 Drive 원본이 있을 때의 다른 길.
4. 썸네일: 사용자가 ChatGPT에 `stock/thumbnails_chatgpt.md` 주소 한 줄 → 그림이 대화에 오면 검수(글자·숫자가 하나도 없는지 확대) → `thumbnail_N.*`.
5. 사용자 답 기다림: 내레이션을 한국어 하나로 둘지, 다른 언어 오디오(자동 더빙 말고)를 만들지 (`stock/guides/README.md` 5번).
6. 2~4번 주제(커버드콜·배당 vs 지수·레버리지)는 **일별 ETF 수정주가·분배금**이 필요하다.
   - Yahoo가 클라우드에서 막혀 있다 (4번). pypi 휠에 그런 자료가 있는지 먼저 찾아본다 (1번은 이 길로 됨).
   - 없으면 사용자가 Network access에 `query1.finance.yahoo.com`·`query2.finance.yahoo.com`·`fc.yahoo.com`을 더하거나, PC에서 받은 자료를 `stock/data/`에 둔다. 둘 다 안 되면 사용자에게 묻는다.

### 2-2. 재테크 — 남은 것

**업로드 시험 (2026-10-16, 재테크 클라우드 환경, 사용자 지시 "… 최종적으로 영상을 만들어 부자백서 채널에 업로드 할 환경이야 한번 업로드 잘되는지 데모 영상 만들어서 업로드 테스트해봐")**
- 이 환경의 키(`YOUTUBE_CLIENT_ID`·`SECRET`·`REFRESH_TOKEN`) = **부자백서** (UCJ1gjiL7VuAhMQSfAhxAefg) — `--check-auth`, `economic/youtube_channel.json`.
- 데모 = 1편 `eunte-kkeonaeseugi-2026-10` 도입 0~51초, **실제 오디오·자막 구움** (`render.mjs video economic eunte-kkeonaeseugi-2026-10 --from 0 --to 51` 88초 → `loudnorm.py` -14.22 LUFS / -1.69 dBTP). 시트 `economic/source/upload-test-2026-10-16/upload.md`, 기록 `youtube.json`.
- 결과: https://youtu.be/CGuiF0dP6Bw (비공개, 예약 없음) — 올리기·처리 `succeeded`, **한국어 자막 올리기 성공**(serving), 썸네일 webp → JPG 변환·등록 성공, 합성 콘텐츠 예, 교육·ko·아동용 아님. **예약 공개 값(`publishAt`)이 API 로 걸리는 것도 확인** (2026-12-31 로 걸었다가 바로 지움). 표는 시트 9번.
- 이 키에 Google **Drive 권한은 없다** — 클라우드에서 바로 올리면 필요 없음.
- 아직 모르는 것: 감사 전 API 프로젝트의 **비공개 잠금** → 사용자가 스튜디오에서 이 영상 공개 상태에 잠금 표시가 있는지 본다.
- 사용자 할 일: 스튜디오에서 확인 → 지우기 (`youtube.json` 은 기록으로 둔다).
- **실제 영상 올리는 길 (이 환경 — 사용자 지시 2026-10-16 "앞으로 여기서 재테크 영상 업로드 할거니까", CLAUDE.md)**: (새 컨테이너면) `node video/scripts/get-fonts.mjs` + `cd video/render && npm install` → `node video/render/render.mjs video economic <영상ID>` (실측 한 편 약 12분 — 아래 표) → `python tools/youtube_upload.py economic <영상ID> --dry-run` → `--publish-at <시각>`.
  - 두 번 올리지 않게: 올리기 전 부자백서 업로드 목록을 읽는다 (2026-10-16 09:04Z 읽음 — 시험 영상 `CGuiF0dP6Bw` 1개뿐, 4편은 아직 안 올라감).

**4편 완성 점검 (2026-10-16, 사용자 지시 "앞으로 여기서 재테크 영상 업로드 할거니까 영상 4개 완성하기 위해 뭐가 필요한지 확인하고 없으면 만들어")**
| 확인 | 결과 |
|---|---|
| 오디오 = 지금 대본 (`tts_narration.py check`) | 4편 ok (99·98·93·94문장) |
| 장면 파일 = 실제 오디오 시각 (`script_sha1` 같음, 추정 아님) | 4편 ✅ |
| SRT (`srt_tool.py check`) | 4편 ✅ (50자 넘는 문장 경고 2개씩 — 새 대본용 경고) |
| 장면 배치 (`render.mjs check`) | 4편 문제 0 (컷 58·48·47·61) |
| 업로드 시트 (`--dry-run`) | 4편 챕터 9개 통과 · 채널 = 부자백서. 1편은 '문제 없음'(영상·썸네일 있음), 2~4편은 썸네일 이미지만 없음 |
| 마지막 문장 | 4편 '시청해주셔서 감사합니다.' |

완성 렌더 (`render.mjs video economic <영상ID>` — 음량 맞춤 포함, `economic/out/<영상ID>/final_1080p.mp4`, 이 컨테이너에만):

| 영상 | 길이 | 음량 / 트루 피크 | 크기 | 걸린 시간 |
|---|---|---|---|---|
| eunte-kkeonaeseugi-2026-10 | 7:58.5 | -14.24 LUFS / -1.69 dBTP | 30MB | 11분 |
| gicho-yeongeum-2026-10 | 7:12.1 | -14.25 LUFS / -1.59 dBTP | 25MB | 9분 |
| isa-mangi-2026-10 | 7:01.4 | -14.15 LUFS / -1.59 dBTP | 25MB | 9분 |
| toejik-geonbo-2026-10 | 7:08.7 | -14.29 LUFS / -1.7 dBTP | 25MB | 9분 |

1. **업로드 (이 환경에서)**
   - 1편 `eunte-kkeonaeseugi-2026-10`: 바로 올릴 수 있다 (썸네일 이미지 있음). 사용자가 공개 시각을 정하면 `--publish-at`.
   - 2~4편: 썸네일 이미지가 오면 검수 → `thumbnail_N.*` → 올림. 업로드 도구는 썸네일 없이도 올리므로 **이미지가 오기 전에는 올리지 않는다** (시트 6번).
   - 예약 간격: PC 업로더와 같게 첫 영상 뒤 24시간마다 (하루 최대 4개) — 사용자가 다르게 정하면 그대로.
   - 그 전에 사용자가 시험 영상 `CGuiF0dP6Bw` 의 **비공개 잠금** 여부를 스튜디오에서 본다 (잠겨 있으면 예약 공개가 안 됨 → `guides/pipeline.md` '업로드 주의').
   - 원본 mp4 는 컨테이너가 바뀌면 없어진다 → 다시 렌더 (장면 파일·오디오·SRT는 저장소에 있음). 이 키에 Drive 권한 없음.
2. **썸네일**: 1편은 이미지 3장 있음. 2~4편은 **프롬프트 v1.0 (2026-10-16 새로)** — `economic/source/<영상ID>/thumbnails/` (`README.md` 근거·`thumbnail_1~3.md`·`chatgpt.md`·`analysis/`).
   - 하단 2줄: 기초연금 「60·70대 기초연금 신청 안 하면 / 부부 1년 500만 원 손해」 · ISA 「50·60대 ISA 만기 돈 연금저축 / 안 옮기면 3년에 96만 원 손해」 · 건보료 「50·60대 건보료 0원 되는 순서 / 은퇴 후 그냥 두면 월 30만 원」.
   - 나이 낱말은 영상마다 댓글에서 센 나이로 (기초연금 60대 54%·70대 35% → '60·70대', ISA 50대 47%, 건보료 50·60대 34%씩).
   - 실험안 ②는 세 편 모두 '사람 없음' → 결과를 함께 본다. 건보료 ①(한 사람)은 1편 본안(한 사람) vs 실험 ①(부부)와 거꾸로.
   - **사용자가 ChatGPT에 보낼 메시지 (9장 한 번에, 지시사항 v3.3)**: `이 파일을 열어 끝까지 읽고, 파일에 적힌 썸네일을 1번부터 차례로 모두 만들어서 장마다 적힌 저장 경로에 올려 줘.` + `https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/main/economic/thumbnails_chatgpt.md` (`make_summary.py --chatgpt-all economic`). ChatGPT가 못 올리면 그림을 번호 순서대로 Claude 대화에 붙임 → 검수(`guides/thumbnail_guide.md` 10번) → 각 경로에.
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

### 2-4. 새 채널 분야 탐색 — `new/` (2026-10-16)

- 사용자 지시: "이외에도 내가 어떤 채널을 만들어야 조회수 높은 영상 만들고 구독자 많이 모을 수 있을지 전체적으로 탐색해봐 저장소에 디렉토리 new로 만들어서 새로운 주제 탐색하기 위한 세팅해서 탐색해봐".
- 방법: 분야 27개(`new/niches.toml` — A 지금 제작 방식 17 · B 촬영 8 · 기준 재테크·주식)를 검색어 1~2개(44개)로 찔러 같은 잣대로 견줌. `tools/niche_scan.py` v1.0 (`sync` → keywords.txt·tag_rules.toml, `report` → 분야 비교, 할당량 0). 명령·기록 `new/README.md`.
- 결과 (`new/result/niche/niche_scan.md`): 성공 비율(작은 채널이 조회수 상위에 끼는 몫) 역사 41% · 건강 42% · 사연 42% · 철학·낭독 36% · 심리 32% · 부업 31% vs **재테크·주식 2%** (넓은 검색어 상위의 54~57% 가 100만 채널).
- 추천(판단, `new/channel_ideas.md`): 1 역사 해설(지도·연표 애니메이션 — 지금 도구와 가장 맞음) · 2 시니어 건강(실험·숫자형 — 검수 필요) · 3 심리. 사연·야담 낭독은 숫자는 가장 좋지만 70분 길이·2025-07 YouTube '대량 생산 콘텐츠' 수익 정책 위험으로 보류.
- 이 환경(세션 `session_01SRoFoFtN3NYBU9zAymzwi6`, 키 지문 `58333e86`) 네트워크는 `www.youtube.com`·`i.ytimg.com`·`suggestqueries.google.com` 이 막혀 자막·썸네일·자동완성이 안 된다 (API `googleapis.com` 은 됨). 2026-10-16 남은 할당량 ≈ 880단위 (다음 초기화 한국 10-17 16:00).
- **다음**: 사용자가 분야를 고르면 → 그 분야 폴더를 만들고(`analyzer_config.toml`·`keywords.toml`·`tag_rules.toml`·`analysis_rules.toml` — `new/` 를 본뜸) `topics.txt` 에 더함 → `tag_keywords.py <폴더> --write-keywords` → `cloud_run.py <폴더> explore --weeks 26` → `approve` → `analyze` → 지시사항·주제.

### 2-5. 역사 분석 — `history/` 클라우드에서 매일 이어서 (2026-10-16)

- 사용자 지시: "이 환경은 이제 저장소에 있는 역사 주제 (history경로 없으면 만들것)를 유튜브 분석 코드 실행해서 분석하는 환경이야 사용량 초기화 될때마다 분석을 계속 이어서하면 돼 캐시를 저장소에 남겨서 분석 이어서 할 수 있게 하고".
- 명령·기록·규칙 근거: `history/README.md`. 설정 `analyzer_config.toml` v1.0(외국 영상 꺼짐) · `keywords.toml` v1.0(관련어) · `tag_rules.toml` v1.0(씨앗 8·역사 낱말 필수·묶음 12) · `analysis_rules.toml` v1.0(성공 기준 CLAUDE.md 그대로, 형식 5가지).
- 예약 작업 **'역사 분석 이어서 (할당량 초기화 뒤 매일)'** `trig_01TEbPHqXpzYY3hj6LhyBb7q` — cron `CRON_TZ=America/Los_Angeles 20 0 * * *` (재테크 00:15 와 main 푸시가 겹치지 않게 5분 늦춤), 이 세션(`session_01Nd9n754WdtaqPq45t3uPSZ`)을 깨움. 순서: pull → status → (검색어가 없으면) `tag_keywords.py history --write-keywords` → resume → 탐색 26주 → 추천 훑고(역사가 아닌 것만 uncheck) 승인 → analyze → (롱폼 탐색이 끝났으면) 쇼츠 → 커밋 → main(+ 세션 브랜치) → 이 문서 1번 표.
- 캐시 `history/cloud_cache/cache.tgz` — 첫 탐색 뒤 생김. `tag_keywords.py` 는 혼자 묶지 않으므로 그 뒤 `cloud_run.py history cache-save`.
- 키: 환경 변수 `YOUTUBE_API_KEY` (지문 `58333e86…` = `new/` 탐색과 같은 키). 역사만 다른 키는 `YOUTUBE_API_KEY_HISTORY`.
- 이 환경 네트워크: `www.youtube.com`·`i.ytimg.com`·`suggestqueries.google.com` 막힘(프록시 403) → 자막·썸네일·자동완성 없음 (영상 설명으로 대신 — 대본 근거로 쓰지 않음). 사용자가 Network access 에 더하면 받음.
- **PC 웹 화면에서 역사 탭을 켜지 않는다** (켜면 PC 결과로 GitHub 의 `history/result/outliers/` 를 바꿈). 음성인식은 하지 않음.
- 하루 예상: 씨앗 검색 16 + 탐색 검색 80 = 96번 ≈ 9,600단위 — 할당량·하루 검색 횟수 한도(주식 91번째에 429)로 첫날 다 못 하면 다음 날 이어서. 승인(댓글 전부)은 그 다음.
- 결과가 모이면: `history/guides/data_insights.md` (지시사항 재료) → 주제 후보 (`guides/pipeline.md` 2단계).

## 3. PC에서 사용자가 돌리는 것 (명령)

| 무엇 | 명령 (PowerShell, 분석기 폴더) | 문서 |
|---|---|---|
| 분석기 (웹 화면, 주제 탭) — ⚠️ **2026-10-16 부터 켜지 않음** (주식·재테크·역사 모두 클라우드, 위 2-3·2-5) | `powershell -ExecutionPolicy Bypass -File run_analyzer.ps1 -Folder stock` (여러 개: `-Folder economic,stock`) → `http://127.0.0.1:8765/` | `guides/pc_analysis.md`, `stock/README.md` |
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
| v1.14 | 2026-10-16 | 주식 1번을 '매수 규칙 10가지 vs 관망'으로 다시 만듦 (`eonje-maesu-2026-10`), 예전 1번 `_old/` 보관 — 1번 표·2-1 |
| v1.13 | 2026-10-16 | 역사 분석 `history/` (클라우드): 폴더·규칙 새로, 첫날 씨앗 검색은 하루 검색 횟수 한도로 못 함, 매일 예약 작업 — 1번 표·2-5 |
| v1.12 | 2026-10-16 | 재테크 4편 완성 점검: 렌더 4편, 썸네일 프롬프트 3편, 업로드 시트 v1.2(클라우드 업로드), CLAUDE.md 업로드 규칙, ChatGPT 모아 보기 |
| v1.11 | 2026-10-16 | 새 채널 분야 탐색 `new/` (분야 27개 첫 탐색·`tools/niche_scan.py` v1.0·추천 `new/channel_ideas.md`) — 1번 표·2-4 |
| v1.10 | 2026-10-16 | 재테크 업로드 시험 성공 (재테크 클라우드 환경 키 = 부자백서, 자막·썸네일·예약 값 확인), 업로드 도구 v1.7 채널 확인 |
| v1.9 | 2026-10-16 | 재테크 분석을 클라우드로 (첫 회차·캐시·매일 예약 작업), PC 웹 화면 켜지 않음 |
| v1.7 | 2026-10-16 | 주식 업로드 시험 성공 (클라우드 키 = STOCK LAB 채널, 지금 이름 '편안한 음악 Relaxing Music'), 렌더 전 글꼴 받기 |
| v1.8 | 2026-10-16 | 주식 분석을 클라우드에서 (`cloud_run.py` v1.3), 외국 영상 켬, 승인 185개, 음성인식 보류, 남은 일(2-0) |
| v1.1 | 2026-10-15 | 주식 1번 백테스트·결론 끝, 2~4번 자료 길 |
| v1.0 | 2026-10-15 | 최초 (대화를 지우기 전 인수인계) |
