# 새 세션 3단계 — 분석·페르소나 → 제목·썸네일 → 대본 (주식·역사·심리·위기)

VERSION: v1.0 — 2026-11-12 — 새로 (사용자 지시 2026-11-12 "새 새션이 생겨도 아래와 같이 똑같이 수행할 수 있도록 지시사항 파일들 수정해 1. 주제 분석 … 2.롱폼과 쇼츠 제목, 썸네일 문구 … 3.롱폼과 쇼츠 대본 작성 …" · 같은 날 "재테크는 하지 말고 심리, 위기 주제를 그렇게 만들어").

- 새 세션은 **이 파일 + 아래 표의 그 주제 줄**만 읽고 시작한다. 단계 안에서 가리킨 절만 더 읽는다 (긴 지시사항 전체를 읽지 않음 — 토큰).
- 사용자가 "<주제> 1단계"·"<주제> 분석 판 업데이트"·"<주제> 제목 만들어"·"<주제> 대본 써"처럼 말하면 그 단계부터. 주제를 말하지 않으면 묻지 말고 주식.
- 재테크(`economic/`)는 이 흐름에 넣지 않는다 (사용자 지시 2026-11-12) — 재테크는 `economic/guides/quick_board.md` 그대로.
- ※ 연구·교육용 — 투자 권유·의료·심리 상담·안전 지침이 아님. 안전 수칙(위기)은 공식 지침으로, 정신건강 정보(심리)는 연구·공공기관 자료로 확인한다.

## 0. 주제 표

| 주제 | 분석 판 (아티팩트) | 분석 코드 | 분석 결과 페르소나 | 대본 받기 | 대본·쇼츠 평가판 |
|---|---|---|---|---|---|
| 주식 `stock` | `stock/boards/urls.json` | `tools/cloud_run.py stock …` | `stock/result/outliers/personas.json` | `pc_transcribe.py list stock` | `stock/guides/quick_board.md` 의 2·3단계 판 |
| 역사 `history` | `history/boards/urls.json` | `tools/cloud_run.py history …` | `history/result/outliers/personas.json` | `pc_transcribe.py list history` | `history/topics/` (없으면 처음 만듦 — 3-4) |
| 심리 `psychology` | `psychology/boards/urls.json` | `tools/cloud_run.py psychology …` | `psychology/result/outliers/personas.json` | `pc_transcribe.py list psychology` | `psychology/topics/` (없으면 처음 만듦) |
| 위기 `crisis` | `crisis/boards/urls.json` | `crisis/code/crisis_lab.py run·analyze` (표준 분석기 전) | `crisis/result/personas.json` (`final`) | 아직 없음 (1-0) | `crisis/topics/` (없으면 처음 만듦) |

판 주소가 `urls.json` 에 없으면 그 판을 아직 올리지 않은 것 — 1-6 대로 처음 올리고 적는다.

## 1단계 — 주제 분석 · 시청자 페르소나 · 분석 판

**1-0. 위기만** — `crisis/` 는 자체 분석(`crisis_lab.py`)이라 고정 채널 탐색·대본 받기가 아직 없다. 판에 들어온 채널은 `crisis/targets.json` 에 적어 두고(판 db 는 status `held`, reply "위기는 표준 분석기로 옮긴 뒤 탐색") 사용자에게 표준 분석기로 옮길지 묻는다 (`crisis/README.md` '이 저장소에서의 위치').

**1-1. 고정 채널 (사용자가 판에 넣은 것)** — 판 db `channels` 에서 `status = new` 만 읽는다 (`ArtifactData list`, 판 주소 = `urls.json` analysis).
→ `python3 tools/cloud_run.py <주제> add <ID·주소·@이름 …>` (채널마다 1단위 · `<주제>/targets.json`) → 줄마다 `ArtifactData update` status `done`(reply "추가됨: <채널 이름> · 영상 N개") 또는 `fail`(reply 까닭) → 다음 `explore` 부터 그 채널의 최근 N주 영상이 '추가한 채널'로 체크된다. 빼기 `remove UC…` · 목록 `targets`.

**1-2. 분석** — 시킬 때만 (예약 작업은 꺼 둠). `python3 tools/cloud_run.py <주제> status` → `explore --weeks 26` → `list --checked` (주제 밖은 `uncheck`) → `approve` → `analyze` → `python3 tools/personas.py <주제>` (분석 결과 페르소나). 할당량이 모자라면 `resume` · 태평양 자정 +10분. 자세한 것은 `guides/pc_analysis.md` 만 그 절.

**1-3. 대본 받을 개수** — `python3 tools/pc_transcribe.py list <주제>` → `transcript_todo.json` 의 `n`·`command`.
- 규칙 (`pc_transcribe.py` v1.2): 목표 = **한국어 성과 상위 50개에 앞 5분 대본** (분석이 세는 첫 20초·첫 1분·말 속도는 앞 5분 안 · 50개면 비율 ±14%p — v1.1 결정). 모자란 만큼만, **성공 사례 먼저** → 모자라면 하루 조회수 상위 → 조회수 상위. 명령 = `run_analyzer.ps1 -Transcribe -Folder <주제> --groups … --limit N --first-only`.
- 판에 개수·명령·먼저 받을 영상 5개가 보인다 (1-6). PC 는 main 의 `transcript_todo.csv` 순서로 받으므로 **목록 파일은 main 에 있어야** 한다.

**1-4. 페르소나 매일 업데이트** (사용자 지시 "매일 업데이트 해야함") — 그날 그 주제로 처음 일할 때 먼저: `python3 tools/persona_live.py status <주제>` 가 `done_today=False` 면 아래 순서. 처음이면 `persona_live.py init <주제>` (분석 결과 페르소나로).
1. 최근 유튜브: `python3 tools/trend_scan.py <주제>` (그날 것이 없을 때만 · 주식 약 1,900단위 · 역사·심리 `--quota 1450 --videos 15 --small 5` 약 1,360 · 위기 `--days 14 --videos 20 --small 10` 약 1,080 — 설정 `<주제>/persona_judge.toml`). 할당량이 모자라면 `--reuse-videos`(그날 찾은 영상으로 댓글만) 또는 지난 trend(14일 안)로.
2. 뉴스·외부 정보: WebSearch 3~6건 (최근 7일 · 그 시청자의 처지를 바꾸는 것 — 주식 = 시장·개인 손실, 역사 = 사극·전시·발굴, 심리 = 정신건강·직장·관계 통계, 위기 = 사기 유형·사고·공식 안전 지침) → `<주제>/result/persona/news_<날짜>.json` `[{title, source, date, url, note}]` — 검색 결과에서 본 것만, 정치인·정당 이름 ✗, 피해자·용의자 이름 ✗.
3. `python3 tools/persona_live.py inputs <주제>` → `inputs_<날짜>.md` **이 한 장만** 읽는다 (지금 페르소나 · 최근 영상·댓글 · 뉴스 · 분석 원문 · 바꿀 것 꼴).
4. 바꿀 것 → `<주제>/result/persona/changes_<날짜>.json` — 페르소나마다 **상황 · 호기심 · 걱정 · 불안 · 원하는 것**(+ 버릇) 을 더함·바꿈·뺌·다시 확인(keep). 줄마다 `basis`(왜 — 80자 안) + `src`(근거).
   - 생각(호기심·걱정·불안)·원하는 것·버릇은 **시청자 말(`c:` 댓글 원문 그대로 12자 이상)이 꼭 하나** — 뉴스·시장만으로는 '상황'만 바꾼다. 댓글이 받쳐 주지 않는 마음은 지어내지 않는다.
   - 칸마다 4개까지 · 14일 넘게 다시 확인 안 한 것은 keep 이나 remove.
5. `python3 tools/persona_live.py apply <주제> <changes.json>` — 하나라도 틀리면 아무것도 안 바뀜 → `[REJECT]` 줄을 고쳐 다시. 내역은 `log.md`·`live.json` 에 저절로 (날짜 · 페르소나 · 칸 · 무엇을 · 근거).
6. 피드 시험 검토자 설명이 그 주제에 없으면 `python3 tools/persona_live.py feed <주제> --out <주제>/feed_personas.toml` (처지 + 원문 댓글만 — 주식은 손으로 고른 `stock/feed_personas.toml` 이 있으니 who 의 손실 폭·comments 만 그날 것으로).

**1-5. 분석 판 다시 만들기** — `python3 tools/analysis_board.py <주제>` → `<주제>/boards/분석판.html` (페르소나 카드 · 근거 펼침 · 업데이트 내역 표 · 고정 채널 칸 · 대본 받기 개수·명령 · 분석 현황). 손으로 고치지 않는다 (틀 `tools/templates/analysis_board.html`).

**1-6. 판 올리기** — 같은 주소로: `Artifact` publish `file_path=<주제>/boards/분석판.html`, `url=<urls.json analysis>` (다른 세션이 올린 판이면 먼저 `Artifact read` 한 번). 처음이면 `capabilities: {db: {}, user: {}}` · icon `persona` 로 올리고 주소를 `<주제>/boards/urls.json` `{"analysis": "<주소>"}` 에 적는다. db 채널은 다시 올려도 그대로.

**1-7. 끝** — `git pull --rebase` → 커밋 (`live.json`·`log.md`·`news_*`·`changes_*`·`inputs_*`·`trend_*`·`boards/` · targets.json) → 푸시. `guides/status.md` 그 주제 줄 한 줄.

## 2단계 — 롱폼·쇼츠 제목 · 썸네일 문구

**2-0. 안 개수** — 롱폼 = **본안 1 + 실험안 2** (스튜디오 '테스트 및 비교' 3장). 쇼츠 = **롱폼과 별개로 만들어도 된다** (사용자 지시 2026-11-12 "쇼츠는 꼭 롱폼 내용과 연결될 필요없이 별개로 생성하면 됨") — 쇼츠 분석 결과(`<주제>/result/outliers/shorts/analysis.md` — 없는 주제는 `cloud_run.py <주제> explore --shorts` 부터)와 페르소나로 따로 주제를 고르고, 롱폼 짝 프롤로그형은 고를 수 있는 꼴 하나일 뿐.

**2-1. 재료** — 1-4 를 오늘 했는지 먼저. 페르소나마다 오늘의 `상황·호기심·걱정·불안·원하는 것`(분석 판 = `live.json`)에서 **한 사람의 지금 말**로 시작한다 (`stock/guides/persona_judge.md` 9-1). 숫자는 계산 코드 출력만.

**2-2. 이미 있는가 · 흔한가** (사용자 지시 "유튜브 이미 올라와 있거나 중복되거나 비슷한 내용이 많으면 안됨") — `python3 tools/title_dupe.py <주제> --title "…" --title "…" [--shorts] [--live]`
- 견주는 것: 탐색 목록 전부 · 받은 사례 · 최근 훑기 · 우리 채널 영상 (+ `--live` 유튜브 검색 1번 100단위).
- ❌ = 같은 제목 · 우리 채널 영상과 비슷 · 같은 내용(핵심 낱말 60% 이상 같음)이 최근 180일 6개 이상 → 그 안은 버리거나 결과·물음을 바꾼다. ⚠ 는 표의 비슷한 제목을 읽고 '우리만의 결과·물음인가'를 한 줄로 적는다 (글자 셈이라 뜻이 같은 다른 말은 못 잡음).
- 그다음 `python3 tools/title_fit.py <주제>` (쇼츠 `--shorts`) — 모바일·PC 2줄.

**2-3. 클릭 패널 (보정 앵커)** — `python3 tools/ctr_check.py <주제> check <안.json>` → `panel <안.json> <n>` → 지시문을 **회차마다 새 하위 에이전트**(페르소나 몫대로)에게 → 답을 `add` → `report`. 실제 성공·덜 된 영상(앵커)을 섞어 같은 잣대로 잼 — 통과 = `pass_rule`(가장 좋은 안 ≥ 성공 앵커 점수 · 나머지 두 안 ≥ 중간 · 앵커를 가름). 못 넘으면 고쳐서 다음 회차. (역사 13회차 기록 `history/topics/ctr/final_2026-11-11.md` 참고.)

**2-4. 피드 시험 (블라인드)** — 패널을 넘은 3안을 `python3 tools/feed_sheet.py <주제> --title … --thumb "큰 글자 1 / 2 | 말풍선 | 꼬리표" … --out <scratchpad>/feed` 로 이번 주 실제 영상 사이에 섞어, 어느 게 우리 건지 모르는 새 검토자에게 '뭘 누를까' (`stock/guides/persona_judge.md` 9-7 — 검토자 설명 = 처지 + 원문 댓글만). 통과 = 확인 회차에서 두 페르소나 모두 3위 안 · 처음 30초 내레이션 뒤에도 계속 봄 · '속는 느낌' 낱말 없음. 못 넘으면 고쳐서 새 검토자로 다시 — **통과할 때까지 반복**.

**2-5. 썸네일** — 문구가 정해지면 그림 프롬프트(`guides/thumbnail_guide.md` 그 주제 절)와 문구 코드(`video/render/thumb.mjs` — 주식 꼴) · 보조 문구는 사람을 가리지 않게. 기록 `<편>/persona_judge_review.md` (회차 · 누가 어디서 걸렸나 · 고친 것). 사용자에게는 **최종 3안만** (본안 1 + 실험안 2, 쇼츠는 따로).

## 3단계 — 롱폼·쇼츠 대본

**3-1. 쓰기** — 롱폼 `guides/script_guide.md` 0번 · 주식은 `stock/guides/quick_board.md` 규칙 · 마지막 문장 "시청해주셔서 감사합니다." · 숫자는 계산 코드 출력만 · 제목이 약속한 숫자는 30초 안에. 쇼츠는 50~55초 — 롱폼과 별개 쇼츠면 그 쇼츠 하나로 끝나는 물음·답.

**3-2. TTS 꼴** (사용자 지시 "오디오가 이상하게 생성되지 않도록 최대한 모델에게 익숙한 형식으로 생성, 특히 숫자 주의") — `python3 tools/tts_check.py <대본.txt> --write-lexicon` → ❌ 0 까지.
- ❌ = 소수(42.5%·3.7년 → 사전에 '사십이 점 오 퍼센트') · 천 단위 쉼표 숫자(1,800만 → 사전 또는 '천팔백만') · 물결 범위(3~5 → '3에서 5') · 기호(/ × → ≈ =) · 문장 머리 'A,'(→ 'A번,') · 숫자 분수(4분의 1).
- ⚠ = 사전에 없는 영어 · 55음절 넘는 문장 · 6음절 안 문장 · 해라체 끝 · 서수 쉼표 나열 · 괄호 · 단위 없는 큰 숫자. 근거 `guides/tts_guide.md` 5-1·5-2·5-5.

**3-3. 이탈 검증 — 통과할 때까지** — `stock/guides/persona_judge.md` 9번 그대로 (모든 주제): ① 내가 먼저 그 페르소나가 되어 문장마다 `번호 | 상태 | 머릿속 말` ② 내 판단을 모르는 **새 검토자 둘**(그 주제 페르소나 중 몫이 큰 둘 · 설명은 처지 + 원문 댓글)에게 번호 붙인 대본만 ③ '이탈'·지루 세 문장 연속·안 풀린 의심을 고쳐 **회차마다 새 검토자**로 다시 ④ 멈춤 = 두 검토자 모두 이탈 0 · 끝까지 봄. 주식은 반론 페르소나(`board_check.py`) ❌ 0 도.

**3-4. 대본 평가판에 올리기** — 대본이 통과하면 `<주제>/topics/board/script_board.json`(롱폼)·`shorts_board.json`(쇼츠 — 별개 쇼츠는 `"independent": true`)에 한 줄 → `python3 tools/script_feedback_board.py <주제> --only long|short` → 같은 주소로 publish (처음이면 `capabilities: {db: {}, user: {}}` → 주소를 `<주제>/topics/board/urls.json` `long`·`short` 에). 사용자는 문장마다 피드백·판정 → 다음 세션은 db `feedback` 의 `status=new` 만 읽고 반영 → 대본 고침 → 3-2·3-3 다시 → 판 다시 올림 → 그 피드백 `done`·`reply`.

**3-5. 끝** — 커밋·푸시 (대본·사전·검증 기록·판). 오디오는 사용자가 Kaggle 셀로 (`guides/tts_guide.md`) — 대본은 main 에 있어야 받는다.

## 바뀐 내역
| 버전 | 날짜 | 바뀐 것 |
|---|---|---|
| v1.0 | 2026-11-12 | 최초 — 3단계 · 주제 표(주식·역사·심리·위기, 재테크 뺌) · 도구 persona_live·analysis_board·title_dupe·tts_check · cloud_run add · pc_transcribe 추천 · trend_scan 쇼츠 댓글 |
