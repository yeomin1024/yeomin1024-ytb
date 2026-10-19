# 이 저장소에서 일하는 규칙

> 2026-10-18 줄임 (사용자 지시 "1,2번 진행하고"): 여기에는 **규칙 한 줄 + 근거 문서**만 둔다. 사용자 원문 인용·날짜·이력은 근거 문서와 `guides/archive/claude_md_2026-10-18.md`(줄이기 전 전문)에. 새 규칙을 더할 때도 이 꼴을 지킨다 — 이 파일은 모든 호출마다 다시 읽힌다.

## Git·저장소
- **main 에 바로 커밋·푸시** (작업 브랜치를 만들지 않음). 올리기 전 `git pull --rebase`.
- 비밀값(.env·API 키·OAuth 토큰·쿠키)은 커밋하지 않고 출력하지도 않는다. 키는 환경 변수로만.
- 다른 사람의 설명·자막·댓글·썸네일(사례 폴더 `01_`·`P01_`·`W_`·`S_`)은 공개 저장소에도 올린다 (분석기 `UPLOAD_CASES_TO_PUBLIC_REPO = true`). 댓글 파일에 작성자 이름·채널 ID 는 넣지 않는다. 다른 사람의 영상 파일은 받지도 올리지도 않는다.
- 영상 파일(완성 영상 포함)은 git 에 넣지 않는다 — 원본은 Google Drive `내 드라이브/youtube/<주제>/<영상ID>.mp4` (`tools/drive_videos.py`).
- 푸시할 수 있는 도구를 시험할 때는 GITHUB_TOKEN 류 환경 변수를 지우고 저장소 이름을 가짜로 (시험이 진짜 GitHub 에 올리지 않게).

## 시작·문서
- 새 대화는 **`guides/status.md`(인수인계)의 '1. 한눈에' 표와 맡은 일의 절만** 읽는다 (전체 약 7만 토큰 — 맨 위 버전 줄들은 이력이라 건너뜀). 일이 끝나면 그 절과 맨 위 버전 줄을 고친다. 지시사항 목록 `guides/README.md` · 전체 순서(분석 → 주제 → 제작 → 요약 문서 → 내레이션 → 렌더·업로드) `guides/pipeline.md`.
- **재테크 영상 소스는 요약본으로 만든다**: 대본 단계 `economic/guides/quick_script.md` · 제목·썸네일·업로드·쇼츠 단계 `economic/guides/quick_package.md`. 다른 영상 폴더와 긴 지시사항은 요약본이 가리킨 절만 읽는다 (영상 한 편 토큰의 약 40%가 그 읽기였음 — `tools/token_cost.py`).
- 주제 폴더: `economic/`(재테크 — 경제 뉴스·금리·환율 해설은 뺌) · `stock/`(주식) · `history/`(역사, 분석만) · `music/`(음악, 분석만) · `new/`(새 채널 분야 탐색) · `math/`(수학 퀴즈 채널 탐색 — 쇼츠·영어 시장, 판단 `math/channel_ideas.md`). 주제별 규칙 `<주제>/guides/`. 옛 주제 폴더는 지움(커밋 `2a68307`). 새 주제는 `topics.txt` 에도 더한다.

## 제작 공통
- 스토리보드는 만들지 않고 요약 문서에도 넣지 않는다. **오디오를 먼저, 그다음 영상** — 오디오가 생기면 승인 없이 바로 영상을 만든다 (영상 코드가 없으면 Claude 가 만들고 still 로 점검).
- 영상 `guides/video_guide.md`: HTML(SVG + GSAP) → Playwright 프레임 렌더 `video/episodes/<영상ID>/index.html`. 예전 크림 배경 인포그래픽·작은 글자 금지. 한 화면 한 생각·말하는 순간 숫자·색 = 뜻(빨강 손해·청록 아낌·노랑 기준, 기준 = 노란 점선)·어려운 말 = 그림 하나·큰 글자. 세로 쇼츠는 화면 가운데·크게(1.15배, 자막 띠 가운데 540). **렌더 뒤 완성 mp4 장면을 Claude 가 직접 본다** (check 0 이어도).
- 자막은 화면에 굽는다 (주식 제외): **한 문장 = 자막 하나**, 띠를 넘으면 같은 자막 안 두 줄, **2줄까지 예외 없음** — 두 줄로도 넘을 때만 쉼표·절 경계에서 나눔, 쇼츠 첫 자막(썸네일 그림 위)은 42px 로 2줄 안 (`tools/srt_tool.py` v1.9).
- 음량 -14 LUFS·트루 피크 -1.5 dBTP 이하 (렌더 뒤 `tools/loudnorm.py` 자동).
- 내레이션 = **진행자 H04 하나로 모든 문장** (`voices/host.json`, 사연자 S07 은 꺼 둠 — `voices/storyteller.json` enabled=false). 모든 대본이 기준 목소리 `voices/ref/host.wav` 를 복제 — 손으로 바꾸지 않고, 바꿀 땐 `host.json` 을 고친 뒤 `tts_narration.py voice --force --push`(모든 오디오 다시). 목소리 다시 고르기: 사용자가 "사연자 S0?, 진행자 H0?" → `python tools/tts_narration.py pick S0? H0?` 후 커밋 (`guides/tts_guide.md` 4-0).
- 오디오는 사용자가 Kaggle 셀 하나로 (범위 버튼 — 전체 기본·주제 하나, `tools/kaggle_tts_panel.py`) → `tts_narration.py all --push` 가 대본 폴더마다 `narration.mp3` 를 main 에. 바뀐 문장이 20% 이하면 그 문장만 다시 (`--full` = 전부) — `guides/tts_guide.md`.
- 주제·제목·대본: `guides/topic_guide.md`·`title_guide.md`·`script_guide.md`.
  - 결론 = 시청자가 가장 원하는 정보(댓글 질문 묶음). 지시사항 근거(`<주제>/guides/data_insights.md`)는 그 주제의 최근·작은 채널 성공 사례(180일 안·구독자 5만 이하·조회수 ≥ 구독자×3·4분 이상)와 그 댓글로만 — 다른 주제 결과를 빌리지 않고, 없으면 '근거 없음'.
  - 제목 = 호기심 구절 + 해소 구절, 60자 이하, 숫자는 대본이 증명, **모바일·PC 목록 2줄 안**(`python3 tools/title_fit.py <주제>`, 쇼츠 `--shorts`) — 줄일 땐 핵심 낱말 맨 앞·시청자층·조건·'손해'·숫자의 주인('부부')을 남기고 꾸밈말을 뺀다.
  - 대본 = 7~8분·결론 먼저·**오늘 시행 중인 법령 원문**(`tools/law_text.py`, law.go.kr 이 막히면 `--source mirror`)·숫자는 계산 코드 출력만·`script_guide.md` 0번 피드백 1~21 (애매한 말 금지 — 무엇을·어떻게 하는지 그 문장에서 · 짧게 + 금액 뒤에 좋은지 나쁜지 · 왜·어떻게·비교 까닭·공정한 조건은 빼지 않음 등). 마지막 문장 **"시청해주셔서 감사합니다."** 사연형 = 도입 25초 → 챕터(끝 문장이 다음 궁금증) → 아주 짧은 마무리, 사연은 각색 가능(`economic/guides/quick_script.md` 5-1).
  - 사례·연구는 최신(2020년대 먼저, 1900년대 사건·자료는 쓰지 않음). 진행자 경험을 지어내지 않는다. 사연 파트는 필수 아님 — 넣으면 20~30초(5~7문장, 85~125음절, 첫 문장에 결과 숫자, 진행자는 늦어도 0:30), 진행자 하나로 읽으므로 3인칭 사례('A 부부는…').

## 썸네일 (`guides/thumbnail_guide.md`)
- **프롬프트 파일만 만든다** — 이미지는 ChatGPT 가 만들고 코드로 그리지 않는다 (있는 픽셀만 옮기는 `tools/cover_shift.py` 는 됨).
- 롱폼 3장 = 본안 1(클릭률 최대) + 실험안 2 (스튜디오 '테스트 및 비교'). 아래쪽 문구 2줄 크게(채택 제목을 줄인 말), 나쁜 상황 빨강·중요 노랑. 그림 = 그 문구의 장면 — **손해 문구면 손해를 알고 좌절한 얼굴**(미간·떨군 고개·처진 어깨·입 가림; 원인 행동이나 놀라 굳은 얼굴만 그리지 않음). 댓글 니즈 낱말은 그림 속 판·꼬리표 위 평면 글자. 디자인 근거는 그 주제 분석 결과로만.
- **조사로 뜻을 분명히** — 금액 앞 낱말이 동사의 목적어로 읽히지 않게('세금 200만 원 날린다' ✗ → '세금으로'), 헷갈리지 않으면 더하지 않음('세금 96만 원 더 낸다'). 제목·쇼츠 제목·썸네일 문구 모두.
- **재테크 쇼츠 썸네일 = 세 칸 band**: 위 0~36% 순검정 + 문구 2줄(줄마다 가운데·최대 크기, 긴 줄 너비 4~96%) · 36~72% 사진(가로 끝까지) · 72~100% 순검정, 글자·얼굴은 높이 15~85% 안 (4:5 로 잘려도 남게). 프롬프트 머리 표 `COVER_LAYOUT: band`, 검사 `tools/cover_check.py`. 그 밖의 쇼츠 썸네일(주식 등)은 사진이 화면 끝까지 — 빈 띠 금지. 영상에선 첫 문장 동안 그 그림(`K.cover`), 업로드 썸네일 = 완성 영상 0초 장면.
- ChatGPT 에 넘기기: `python tools/make_summary.py --chatgpt-all <주제>` → `<주제>/thumbnails_chatgpt.md` 를 **커밋 고정 주소**(`raw.githubusercontent.com/<저장소>/<커밋>/…`)로 **새 ChatGPT 대화**에, 메시지 "이 파일을 열어 끝까지 읽고, 파일에 적힌 썸네일을 1번부터 차례로 모두 만들어서 장마다 적힌 저장 경로에 올려 줘." + 주소. ChatGPT 가 못 올리면 사용자가 그림을 Claude 대화에 붙인다 → Claude 가 검수(그림 속 한글 확대)하고 통과한 것만 `thumbnail_N.<확장자>` 로 main 에.
- 제목이 바뀌면 썸네일 문구·그림도 다시 만들고, `thumbnails_chatgpt.md` 를 끝까지 읽어 공통 규칙이 맞는지 확인한다.

## 쇼츠 (`guides/shorts_guide.md`)
- 쇼츠 분석: 조회수 5만 이상인데 좋아요 0.2% 미만('조회수 부풀림 의심')과 주제 밖 쇼츠(연예·운세·명언·정치·다른 뜻)는 뺀다 — `<주제>/analysis_rules.toml [shorts*]`, 새 결과마다 1번 표를 훑어 규칙에 더한다. 쇼츠 지시사항은 그 주제 쇼츠 결과로만.
- **재테크 쇼츠 = 롱폼으로 보내는 프롤로그형** (롱폼 하나에 쇼츠 하나, 4번): 50~55초. 롱폼 가상 사례로 **첫 문장 하나에 핵심**(누가·언제·무엇 때문에·얼마) → 알게 된 경위(각색 가능 — 숫자·결과는 롱폼 그대로, 설명란에 '가상 사례를 각색') → 걸린 것 → '지금이라도 ○○을 줄일 수 있을까요?'(무엇을 하는지 넣어서) → '아래 영상에서 확인하세요'. 롱폼의 이유·방법은 넣지 않는다. 제목 = 사람 이름 없이 핵심 낱말 맨 앞, 손해 사연 꼴, 동사로 끝 + 조사, 2안을 보여 주고 사용자가 고름. 해시태그 2개, 롱폼 끝인사 없음. 관련 동영상 = 그 롱폼 (사용자가 스튜디오에서).
- 주식 쇼츠는 결과형 (아래 주식).

## 업로드 (`guides/upload_guide.md`)
- **재테크는 이 클라우드 환경에서 바로**: 키(`YOUTUBE_CLIENT_ID`·`SECRET`·`REFRESH_TOKEN`) = 부자백서 UCJ1gjiL7VuAhMQSfAhxAefg (`economic/youtube_channel.json`, 도구는 키의 채널이 다르면 멈춤 — 주식 환경 키 = STOCK LAB). 렌더 `node video/render/render.mjs video economic <영상ID>`(새 컨테이너면 글꼴·gsap 먼저 — status 4번) → 썸네일 검수 → `python tools/youtube_upload.py economic <영상ID> --dry-run` → `--publish-at <시각>` (비공개 + 예약 공개, `youtube.json` 을 main 에). **올리기 전에 채널 업로드 목록을 읽어 두 번 올리지 않는다.** 쇼츠 영상ID = `<영상ID>-shorts`.
- 롱폼과 짝 쇼츠는 같은 시각에 공개, 짝끼리 1시간 간격. 할당량(영상 약 2,050단위·하루 10,000·한국 16시 초기화, 예약은 올린 뒤에만)이 모자라면 롱폼부터, 짝 쇼츠가 늦어지면 이미 올린 롱폼 공개 시각을 옮김(videos.update — 합성 콘텐츠 칸 같이) — 12번. 쇼츠 썸네일은 공개 뒤 `i.ytimg.com/vi/<ID>/oardefault.jpg` 로 확인, 안 보이면 사용자가 앱에서 0초 장면. Drive 권한은 없음(mp4 는 컨테이너에만).
- '변경되거나 합성된 콘텐츠' = **예** (AI 음성) — 업로드 시트에 적고 도구가 등록.
- PC 업로더 길(`run_uploader.ps1` → `tools/pc_upload.py`, Drive 원본, 예약 기본 +1시간, 하루 최대 4개) — 11번.

## 주식 `stock/` (공통보다 먼저 `stock/guides/README.md`)
- 컨셉 = AI 가 코드를 만들어 시청자 가설을 백테스트로 검증 (`stock/guides/concept.md`: 결론은 결과를 본 뒤, 숫자는 코드 출력만, 미래 정보 금지·총수익·비용·여러 시작 시점·생존 편향, 개별 종목 추천 안 함). 주제 `stock/source/topic_candidates.md`, 근거 `stock/guides/data_insights.md`. 클라우드는 Yahoo·FRED·KRX·law.go.kr 막힘, GitHub raw 는 됨.
- 전 세계 시청자: 화면에 자막을 굽지 않고 **언어별 자막(CC)을 올림** — 한국어 + en·hi·id·pt·es-419·ja·de·vi·tr, 대본 `subs/`(롱폼)·`shorts/subs/` 는 한국어와 문장 1:1 (`tools/subs_tool.py check|build`, 업로드 v1.12 — 자막 하나 400단위, 모자라면 `--captions-only` 다음 날). 화면 글자는 언어 없이(숫자·연도·%·기호·A/B·아이콘). 제목·설명 10개 언어(`upload.md` '언어별 제목·설명' — 기본 언어 ko). **설명란 = 첫 설명(아주 간단히) + 챕터(이름 옆 괄호 영어) + 자료 + 알려 드립니다만, 각 아래 영어**, 태그 = 한국어 + 영어, 롱폼 제목도 목록 2줄 안 — 올린 영상은 `youtube_upload.py --update-meta` (README 2번).
- 썸네일 = 그림 + 쉬운 영어 낱말(BUY·SELL·TAX)·숫자·기호·티커만 (한국어·문장 없음). **시청자 니즈(댓글 질문) + 티커** — 실험 설계를 그리지 않음(`WHEN TO BUY ?` + `SPY`, 레버리지는 티커 + 배수 `TQQQ 3× > QQQ 1× ?`). **부등호 머리글 하나를 크게**(`SCHD > SPY ?`, 굵게·테두리·빛, `>`·`?` 노랑), 이름표는 꼭 필요할 때만, 어려운 말·식은 그림으로. **결말을 가림**(두 선택 같은 크기, 결과는 닫힌 상자, 이기고 진 표정·오른 계단·하락선 없음).
- 핵심 장면 = 날짜가 흐르며 두 계좌를 실시간 비교하는 애니메이션.
- 제목·대본·설명란·챕터·고정 댓글은 **결말을 말하지 않는다**: 제목 = 맨 앞 니즈 낱말 + 조건 기준점·폭 + 비교 대상·잣대 + 질문으로 끝, 도입 = 니즈·공감 → 질문 → "백테스트로 확인해 보겠습니다", 사다·팔다 → 매수·매도 (README 2·5번).
- **주식 쇼츠는 결과를 바로 말한다**(60초 안): 시험할 말(왜) → 방법(AI 가 짠 파이썬 코드로 과거 실제 가격 백테스트, 코드 카드) → 시험한 것·비교 상대와 고른 까닭 → 공정한 조건 → 결과(끝 값·차이) → '왜?' → '그 이유와, 다른 달에 시작해도 같은지는 아래 영상에서'. 왜·어떻게·비교 까닭·조건은 빼지 않고, 경주는 끝까지, 제목·쇼츠 썸네일은 결과를 말하지 않음 (README 7번).

## 분석 (`guides/pc_analysis.md`)
- 검색어 `<주제>/keywords.txt`(한 줄에 하나 — 사용자가 GitHub 에서 고치면 다음 회차에 반영) · 관련어·제외어 `keywords.toml` · 설정 `analyzer_config.toml`. 검색어는 실제 영상 태그로 (`python tools/tag_keywords.py <주제> --write-keywords`, 빼는 말·필수 낱말 `<주제>/tag_rules.toml` — 사용자가 지운 말은 되살아나지 않음, 주식은 모두 '주식' 낱말이 든 말 `TAG_REQUIRE`). 사용자가 새 주제를 말하면 Claude 가 그 세 파일을 만들어 main 에.
- PC 는 웹 화면(`run_analyzer.ps1` → `tools/web_ui.py`, 주제 탭 — 탭마다 키 `<주제>/.env`·검색어·캐시·결과 따로, 다른 키면 할당량 장부도 따로): 탐색 목록은 배수 높은 순·이미 쓴 영상·라이브는 뺌, **사용자가 승인한 영상만** 자료를 받는다. 캐시 비우기는 옮기기(`.yt_work/old/`).
- **클라우드에서 분석하는 주제: economic·stock·history·music** — `python3 tools/cloud_run.py <주제> <status|explore|list|check|approve|baseline|comments|demand|analyze|resume|wait-reset>`(웹 화면 작업 함수 그대로), 캐시 `<주제>/cloud_cache/cache.tgz`. ⚠️ **이 주제들은 PC 웹 화면 탭을 켜지 않는다** (PC 결과로 GitHub `<주제>/result/outliers/` 를 덮음) → 음성인식(PC 만)은 보류, 하려면 사용자에게 먼저 묻는다. 탐색이 덜 끝난 날은 줄어든 비교 집단 분석으로 결과를 덮지 않는다.
  - 예약 작업은 주제마다 하나: 재테크 '재테크 분석 이어서'(태평양 자정 +15분) · 역사 `trig_01HMG95DYgQiYDH7NsthAyx9`(+20분 — `trig_01TEbPHqXpzYY3hj6LhyBb7q` 는 꺼 둠, 키는 `new/` 와 같아 하루 검색 횟수를 함께 씀) · 음악 `trig_01RR9ppiEXLNHmhFotDPNPzV`(+25분, 음악 세션 `session_01KkE3gVZtik1LxawNwFrDZj` — `trig_01RWWyDUkoWgb2t4MEn6oSUR` 는 꺼 둠). 회차 기록은 각 `<주제>/README.md`.
  - 역사 추천 `history/source/topic_candidates.md`(조선 백성의 삶 주력·세계사 실험) · 음악 전제 = 작곡 AI(YuE2)로 만든 곡의 플레이리스트, 추천 `music/source/topic_candidates.md`(성공 기준 4분 이상 그대로).
- 새 분야 탐색 `new/`: `new/niches.toml` → `python3 tools/niche_scan.py new sync` → `cloud_run.py new explore --weeks 26` → `niche_scan.py new report` → `new/result/niche/niche_scan.md`(숫자만), 추천은 `new/channel_ideas.md`. 이 결과로 대본·제목 규칙을 만들지 않는다.
- 외국 영상: `<주제>/analyzer_config.toml [search] INCLUDE_FOREIGN`(기본 false — 재테크 false · 주식·음악 true), 영어 검색어 `<주제>/keywords_foreign.txt`(켠 주제만). 외국 사례의 제목·댓글 낱말 통계로 한국어 규칙을 만들지 않는다. 라이브는 늘 뺀다.
- 할당량: 단위와 따로 '하루 검색 횟수'(HTTP 429)가 있다. 할당량 때문에 남은 일은 태평양 자정 +10분에 이어서. 아끼기는 검색어를 줄이지 않고 캐시로. **할당량을 늘리려고 Google Cloud 프로젝트를 여러 개 만들라고 권하지 않는다** (정책 위반 — 할당량 증가 신청이 정식).
- 승인하면 결과를 먼저 GitHub 에, 음성인식은 뒤에서(성공 사례부터, 1차 앞 5분 → 2차 전체). 자막을 못 받으면 설명으로 대신 — 글 출처가 '설명'인 영상은 대본 근거로 쓰지 않는다. 자막 서버 차단(IpBlocked·RequestBlocked·429)은 음성인식으로 보내고, 연속 2번이면 6시간 쉼.
- 결과 = `<주제>/result/outliers/analysis.md`(숫자·원문만 — AI 는 0번 '한계'를 먼저 읽고, 대본 없는 사례·표본 적은 차이로 규칙을 만들지 않음) · 쇼츠 `shorts/analysis.md` · 받은 자료 표 `downloads.md`(업로드 날짜 포함). 성공 사례와 조회수 상위 영상(기본 20개) 댓글은 답글까지 전부. 성공 사례 영상 파일은 받지 않는다.
