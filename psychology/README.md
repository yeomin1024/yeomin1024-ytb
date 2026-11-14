# 심리 주제 폴더 (`psychology/`) — 클라우드에서 분석

VERSION: v1.4 — 2026-11-12 — **제목·썸네일·대본 페르소나 반복 검증** 절 (`guides/persona_loop.md`) — 사용자 지시 "제목,썸네일, 대본 만들때 자꾸 페르소나 반복 검증 빼먹는데 빼먹지 말도록 주제별 지시사항 수정해봐".
(v1.3 — 2026-11-12 — **대본 4편** (사용자 지시 "그래 content_analysis 고쳐 지시사항 규칙대로 4가지 대본 만드는 것 까지 해봐 챗지피티한테도 페르소나로 검증해보라고 할거니까 명령 알려주고"): `source/first_video.md` 1·5·6번 주제 4편 — `source/<영상ID>/<영상ID>.txt`·`.srt`·`대본_근거.md`·`persona_review.md` · ChatGPT 검증 파일 `source/chatgpt_persona_review.md` (`tools/chatgpt_persona_review.py` v1.0) · `content_analysis.py` v1.0.3 (앞 5분 대본은 흥미 장치 4구간을 세지 않음) · 성공 사례 대본 50개.)
(v1.2 — 2026-11-12 — **main 기준 정리** (사용자 지시 "main 쪽을 기준으로 두고, 제 브랜치에서 쓸모 있는 것만 main 데이터 위에 다시 적용하고 심리랑 관련없는 주제는 제외"): 주제 밖 28개 뺌(`excluded_videos.md`) · 페르소나 최근 흐름(`personas.toml` v1.2 TREND_DAYS 28 · `tools/personas.py` v1.1.1) · 썸네일 94장 분류(성공 사례 전부) · 댓글 96개 더 · 대본 47개(PC) · 추천에 다른 안 — 조회수 5만 규칙(v1.1)과 함께 성공 사례 **94**(`source/first_video.md` 6번).)
(v1.1 — 2026-11-12 — 성공 사례에 조회수 5만 이상 (규칙 v1.1) · 분석 다시 · 대본 받을 목록 다시 (사용자 지시 2026-11-12 "일단 대본 받아야 하니까 명령 좀 알려줘 … 조회수가 구독자수 대비가 높아도 조회수 별로 안나오면 성공사례에서 빼야해").)
(v1.0 — 2026-11-11 — 새로 만듦 (사용자 지시 2026-11-11 "가장 최근에 주식 주제에서 했던 것처럼 심리 주제로 분석 코드 돌려서 해당 주제 유튜브 분석에 필요한 자료 받고 페르소나 구성해서 내가 어떤 제목, 썸네일 문구, 보조문구로 영상 만들어야 하는지 하나 알려줘봐 그리고 최근 트렌드도 반영해야 돼").)

- 새 채널 분야 탐색 `new/niches.toml` 의 **'07. 심리·인간관계'**(new/ 결과 성공 비율 32%)를 그 분야만의 폴더로 분석한다. 방법은 주식·역사와 같다 (`stock/guides/quick_flow.md` 1~8단계 — 주제 이름만 `psychology`).
- 결과 숫자: `result/outliers/analysis.md` (숫자·원문만). 제목·썸네일 추천(판단)은 `source/first_video.md`.
- ※ 연구·교육용 분석 — 의료·심리 상담이 아니다. 정신건강 정보는 대본 전에 연구·공공기관 자료로 확인한다.

## 클라우드에서 분석 (`tools/cloud_run.py`)

```bash
python3 tools/cloud_run.py psychology status                       # 할당량·탐색 목록·승인 수·남은 것
python3 tools/cloud_run.py psychology resume                       # 할당량·하루 검색 횟수 때문에 남은 탐색·댓글·채널 기준선
python3 tools/cloud_run.py psychology explore --weeks 26           # 롱폼 탐색 (검색어 28개 × 4~20분·20분 넘음 = 56번 ≈ 5,600단위)
python3 tools/cloud_run.py psychology explore --shorts --weeks 26  # 쇼츠 탐색 (롱폼 탐색이 끝난 뒤 — 28번 ≈ 2,800단위)
python3 tools/cloud_run.py psychology list --checked               # 새 추천
python3 tools/cloud_run.py psychology uncheck ID …                 # 심리가 아닌 추천 풀기 (투자 심리·타로·노래 등)
python3 tools/cloud_run.py psychology approve                      # 추천 승인 → 설명·자막·썸네일·댓글 → 분석
python3 tools/cloud_run.py psychology analyze                      # 롱폼·쇼츠 분석 다시 (할당량 0)
python3 tools/tag_keywords.py psychology --write-keywords          # 검색어를 실제 영상 태그로 다시 고르기 (씨앗 검색 — 할당량)
```

- **키**: 환경 변수 `YOUTUBE_API_KEY` — `history/`·`new/` 와 같은 키라 같은 날 하루 10,000단위·하루 검색 횟수를 함께 쓴다.
- **캐시**: `psychology/cloud_cache/` (명령 뒤 저절로 묶음 — 새 컨테이너에서도 이어서).
- ⚠️ PC 웹 화면에서 심리 탭을 켜지 않는다 (PC 결과로 GitHub 의 `result/outliers/` 를 덮음). 대본은 '대본만 받기' (`tools/pc_transcribe.py list psychology` → PC `run_analyzer.ps1 -Transcribe -Folder psychology`).
- 예약 작업은 만들지 않음 (2026-10-24 사용자 지시 — 분석은 시킬 때).

## 파일

| 파일 | 내용 |
|---|---|
| `analyzer_config.toml` | 분석기 설정 v1.0 — 주제 이름 '심리', 외국 영상 꺼짐 |
| `keywords.txt` | 탐색 검색어 — `tools/tag_keywords.py` 가 실제 영상 태그에서 고름 |
| `tag_rules.toml` | 태그 → 검색어 규칙 v1.0 — 씨앗 4개(심리학·인간관계·자존감·심리) · 빼는 말(투자 심리·타로·사주·종교 설교·음악) · 주제 낱말 필수 |
| `tag_candidates.md`·`.csv` | 태그 표 (채널 수 순, 왜 뺐는지) |
| `keywords.toml` | 관련어 v1.0 — 강한·약한 관련어 · 지우는 표현('투자 심리'·'매수 심리'·'심리적 지지선'·타로·사주) |
| `analysis_rules.toml` | 분석 기준 v1.0 — 주식·재테크·역사와 같은 세 묶음 · 심리 형식 7개 · 점술 빼기 |
| `personas.toml` | 시청자 페르소나 설정 v1.0 → `result/outliers/personas.md` (분석 끝에 저절로) |
| `result/outliers/` | 승인한 영상 자료(`W_<영상ID>/`) · `analysis.md` · `personas.md` · `comment_titles.md` · `comment_clusters.md` · `content_analysis.md` |
| `source/first_video.md` | **첫 영상 제목·썸네일 문구·보조 문구 추천 (판단)** — 1번 추천 + 6번 다른 안(가족 편) |
| `source/<영상ID>/` (4편) | 대본 v1.0 — `geureut-moa-2026-11`(그릇 모아 두는 사람) · `eomma-gibun-2026-11`(엄마 기분 살피던 사람) · `eomma-hasoyeon-2026-11`(엄마 하소연) · `sangcheo-gonggyeok-2026-11`(상처받은 사람이 공격적) — 대본·SRT(✅)·`대본_근거.md`(출처·확인 필요)·`persona_review.md` |
| `source/chatgpt_persona_review.md` | ChatGPT 페르소나 검증 파일 (페르소나 6명 + 규칙 9 + 대본 4편 문장 번호 + 답 양식) — 다시 만들기 `python3 tools/chatgpt_persona_review.py psychology` (편 목록 `source/chatgpt_review_list.json`) |
| `excluded_videos.md` | 주제 밖이라 뺀 승인 영상 28개 (까닭·되살리기) — 종교·범죄 사건·뇌과학/공부법·육아·연애 예능 리뷰 등 |
| `result/outliers/thumb_codes.tsv` | 성공 사례 썸네일 122장 분류 (Claude 가 그림을 봄) → `content_analysis.md` 2번 |
| `cloud_cache/` | 탐색 캐시 묶음 |

## 회차 기록

| 때 | 한 일 | 할당량 | 결과 |
|---|---|---|---|
| 2026-11-11 18:22~22:48 KST (사용자 지시 — 첫 회차) | 설정 · 씨앗 검색 · 태그 검색어 28개 · 롱폼 탐색 26주 · 추천 훑기(193개 풂) · 승인 317 · 분석 · 페르소나 감사·고침(v1.1) · 댓글 묶음 · 댓글 니즈 C01~C26 · 확인·콘텐츠 엑셀 · 대본 받을 목록 | 씨앗 812 + 탐색 7,886 (기간 없는 검색 22번 포함) + 승인 1,914 = 하루 몫 다 씀 | 탐색 2,722 · 성공 사례 **135** · 하루 조회수 상위 77 · 조회수 상위 77 · 비교 집단 757 (성공 32%) · 페르소나 5명 (5060 · 부모·가족 상처 · 배우자·시댁 · 학생·청년 · 우울·불안) · 첫 영상 추천 `source/first_video.md` |
| 2026-11-12 01:00~01:31 KST (사용자 PC) | `run_analyzer.ps1 -Transcribe -Folder psychology` | 대본 46개 올라옴 (자막 21 · 음성인식 1차 25) → **오류로 멈춤** (커밋 "오류 전까지 — 영상 5개" — 오류 줄은 PC 창에만) |
| 2026-11-12 13:37 KST (사용자 지시 2026-11-12 "일단 대본 받아야 하니까 명령 좀 알려줘 … 조회수가 구독자수 대비가 높아도 조회수 별로 안나오면 성공사례에서 빼야해") | 규칙 v1.1 (`[success] MIN_VIEWS` 1만 → 5만 — 관련 롱폼 7~182일 조회수 가운데값 55,419) · `analyze` · `pc_transcribe.py list psychology` | 할당량 0 · 성공 사례 135 → **106** (조회수로 30 빠짐·채널 자리 1 들어옴) · 대본 받을 목록 296 (끝까지 271 · 2차 25) |

| 2026-11-12 13:20~13:55 KST (사용자 지시 — main 기준 정리) | 주제 밖 28개 뺌 (사례 폴더 지움 · 푼 추천에 넣음 · OFF_TOPIC v1.1) · `resume` 댓글 96/125 · 분석 다시 (대본 47 — PC · 조회수 5만 규칙과 합침) · 페르소나 TREND_DAYS · 썸네일 94장 · 댓글 묶음·니즈·콘텐츠·확인 엑셀 다시 · 대본 목록 269 | 2,318 (댓글 — 오늘 몫 끝) | 승인 289 · 성공 사례 94 · 비교 집단 734 (24%) · 페르소나 6명 (최근 28일: 부모·가족 상처 12.2% → 16.0% · 직장 13.6% → 16.4%) |

## 제목·썸네일·대본 — 페르소나 반복 검증 (빠뜨리지 않음 · 2026-11-12)
- 사용자 지시 "제목,썸네일, 대본 만들때 자꾸 페르소나 반복 검증 빼먹는데 빼먹지 말도록 주제별 지시사항 수정해봐" → 제목·썸네일 문구·보조 문구·대본(롱폼·쇼츠)을 쓰거나 바꿀 때마다 `guides/persona_loop.md` 세 단계(`title` · `script_exit` · `script_rebuttal`), 각 2회차 이상 · 회차마다 새 하위 에이전트 · 마지막 회차 = 지금 글. 기록 `psychology/source/<영상ID>/persona_loop.json` (`tools/persona_gate.py`) · 페르소나 = `result/outliers/personas.json` · 반론 = `rebuttal_persona.md`.
- ChatGPT 페르소나 검증(`source/chatgpt_persona_review.md`)은 사용자가 돌리는 **덧붙임** — 그 답도 `persona_gate.py add` 로 회차에 넣을 수 있지만, Claude 하위 에이전트 회차를 대신하지 않는다 (사용자를 기다리느라 검증을 건너뛰지 않게).

## 영상 — 만스피 꼴 (2026-11-13)
- 사용자 지시 "만스피 영상처럼 영상 만들거니까 챗지피티한테 만들 이미지 생성 명령 알려줘" → "1시간 마다 오디오 확인하고 생긴것 부터 영상 만들어".
- 그림: `source/<영상ID>/images_chatgpt.md` (생성 `source/images_build.py`) → ChatGPT 가 `puppet/`(배경판) · `puppet/motion/`(기준·동작 3장·소품) · `images/TH-CHAR.jpg`(썸네일 그림, 문구는 코드).
- 자르기: `python3 psychology/source/puppet_slice.py <영상ID>` → `puppet/cut/` + `manifest.js` (시트마다 그린 키가 달라 900px 로 맞춤 · 앉은 자세 비율 `POSE` · 앞 물건 `FG`).
- 장면: `video/episodes/<영상ID>/index.html` + 공통 엔진 `video/render/psy_anim.js` (만스피 v3.1 엔진 바탕 — 세계 층 카메라 · 원화 바꿔 끼우기 · 머리 옆 말풍선 · 판 카드 · 배치 칸 HEAD/LOW/LIST).
- 순서: 오디오 → `node video/scripts/align-audio.mjs psychology <영상ID> --no-export`(자막을 실제 오디오에) → `render.mjs sync` → `check`·`layout-check` 문제 0 → `render.mjs video` → 완성 mp4 장면을 직접 봄 (음량 맞춤이 8번 안에 못 맞추면 `tools/loudnorm.py <mp4> --target -13.9` 뒤 기본 기준으로 다시 잼).
- 썸네일 (2026-11-13 — 사용자 지시 "썸네일 만스피처럼 문구 코드로 얹어서 만들어"): `python3 psychology/source/thumbs_build.py` → `source/<영상ID>/thumbnails/thumbnail_{1,2,3}.json`·`.jpg` (그림 = `images/TH-CHAR.jpg` · 문구 = `video/render/thumb.mjs`). 1 = 본안(아래 2줄 + 흰 말풍선) · 2 = 실험(보조 문구 없음) · 3 = 실험(강조 색 바꿈 + 노란 말풍선) — 문구는 package.json 그대로(페르소나 관문 title 통과 · 다르면 도구가 멈춤) · 말풍선은 머리 옆 빈 곳, 꼬리는 말하는 사람 쪽 · 2줄째는 오른쪽 아래 18% 비움. 문구가 다른 실험안은 persona_loop title 단계부터.
- 업로드 (2026-11-14 — 사용자 지시 "업로드 시트 만들고 uploads 브랜치에 올려"): 시트 `source/<영상ID>/upload.md` (생성 `source/upload_sheets.py` — 제목 = package.json · 설명란 소개 2줄·챕터·출처·알려 드립니다·도움받을 곳·해시태그 2 · 태그 19~21개 · 고정 댓글) · `tools/upload_pack.py check psychology …` 네 편 ✅ · `pack` → 영상 = `uploads` 브랜치 `psychology/<영상ID>/` 90MB 조각 3개 · 확인값 main `source/<영상ID>/video.json`. 추천 공개 순서 = 그릇 → 엄마 기분 → 상처 → 하소연 (하루 한 편). ⚠ `psychology/youtube_channel.json` 없음 → PC 화면 psychology 탭에 심리 채널 키만 · 처음 올린 뒤 '기억'.
- 결과 (2026-11-13, 이 컨테이너 `psychology/out/<영상ID>/final_1080p.mp4` — git 에는 넣지 않음): 엄마 기분 7:44 · 하소연 7:56 · 그릇 7:28 · 상처 7:44 — 모두 -14 LUFS 안팎 · 트루 피크 -1.5 dBTP 이하.

## 다음 할 일
0. 영상 네 편 — 썸네일·업로드 시트·uploads 브랜치 끝 → 사용자 PC `유튜브_업로드.bat` → psychology 탭에서 [업로드] (하루 한 편 · 예약 날짜 칸) (대본 페르소나 관문: 이탈 단계 네 편 ❌ · 하소연 반론 ❌ 결정 기다림).
1. 할당량이 초기화되면 (한국 17시) `resume` — 댓글 덜 받은 29개 · 같은 채널 기준선 107곳 → `analyze`.
2. 쇼츠 탐색 `explore --shorts --weeks 26` (28번 ≈ 2,800단위) → 추천 훑기 → 승인.
3. 사용자 PC 대본만 받기 이어서 (`transcript_todo.md` — 분석 뒤 다시 만든 목록 · 01:31 오류로 한 번 멈춤, 같은 명령으로 이어 받음 · PC 로그 `.yt_work\transcribe_log_psychology.txt`) → `analyze` 다시.
4. 새 성공 사례가 생기면 그 썸네일만 `thumb_codes.tsv` 에 더함 → `content_analysis.py psychology`.

## 한계
- 대본 47개 (PC — 자막 끝까지 20 · 음성인식 앞 5분 27) · 나머지는 설명으로 대신 (대본 근거로 안 씀).
- 쇼츠는 아직 탐색 전 · 같은 채널 기준선 없음 (할당량).
- 페르소나 감사(v1.0 규칙, Claude 가 무작위 댓글을 읽음): 5060 12/14 · 부모·가족 상처 7/9 · 직장 7/9 · 배우자·시댁 5/9 · 학생·청년 5/9 · 우울·불안 5/9 — 뒤 셋은 대강의 크기로만.
