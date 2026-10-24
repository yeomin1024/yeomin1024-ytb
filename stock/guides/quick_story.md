# 개미 재기 일지 — 토큰을 덜 쓰는 제작 순서 (요약 지시사항)

버전: v1.7 — 2026-10-24 — **화면에 투자 영어 허용**(KOSPI·S&P 500·BUY·SELL … `stock/story/screen_words.txt`, 국기 대신 지수 이름) · **문장마다 화면** · 소품 = **주식 그림** v3.0 · D-2 문법 `title=`·글자 칩 `'TEXT`·`LIST`·`PIE cap=` (사용자 지시 2026-10-24 "국기를 할 필요는 없잖아 그냥 KOSPI, S&P500 이거 달면 되는데 저건 영어인데 투자하는 사람이면 다 알잖아 buy, sell 같은것도 그렇고 다 알만한건 넣어도 돼" · "이미지 요소도 뭔가 주식하고 동떨어져 있어").
(v1.6 — 2026-10-24 — 설명 소품 = **공통 소품** (사용자 지시 "소품 요소를 좀 되도록 다른 주식 관련 영상에서 재사용할 수 있도록 공통된 걸 만들도록 해봐 …"): `story_kit props [낱말]` 로 있는 것부터 다시 씀 · 새 소품도 일반적인 뜻으로.
(v1.5 — 2026-10-23 — **정리 부분 없음** (사용자 지시 "그냥 정리 부분은 빼자" — '정리해볼게요'·정리 카드·K6 뺌) · **설명 소품 그림** `*이름` (사용자 지시 "설명에 필요한 이미지 요소들은 왜 생성안해?" — ChatGPT `stock/story/puppet/props_chatgpt.md`).
(v1.4 — 2026-10-23 — 화면·썸네일 **영어도 없음** (BIG icon= · #N · 썸네일 숫자·기호) (사용자 지시 2026-10-23 "야 영어 문구도 넣지마").)
(v1.3 — 2026-10-23 — 화면·썸네일 한국어 없음 · D-2 문법(K6 그림 줄 · PIE · 화살표 · 국기·%·₩⇄$ · K4 icon= · BIG 여러 낱말) (사용자 지시 2026-10-23 "외국인 대상으로도 할거니까 그것도 고려해 영상에 한글 문구 사용하지 말고 최대한 이해 잘되도록").)
(v1.2 — 2026-10-23 — 화마다 다른 경험 · facts --unused · check [DUP] (사용자 지시 "70% 잃었다는건 처음 시리즈에서만 … 중복되면 안돼").)
(v1.1 — 2026-10-23 — 도입 마지노선 35초 · 사용자 통과 줄 · 예고 문장 없음 · 돈 숫자 70% 확정 (사용자 지시 "도입은 그냥 통과시켜 손실은 70%로 하고 … 도입 마지노선 35초로해").)
(v1.0 — 2026-10-23 — 새로 만듦. 사용자 지시 2026-10-23 "주제 탐색 -> 요약본 만들기 -> 대본, 썸네일 프롬프트 등 영상 소스 -> 영상 만들기 과정을 토큰을 가장 덜 사용하는 구조로 만들어봐 저번에 그렇게 했었으니 참고해서 설계해봐" (본보기 = 재테크 `economic/guides/quick_script.md`·`quick_package.md`).)

이 파일은 아래 원본의 요약이다. 원본이 바뀌면 이 파일도 고친다 (원본이 우선).
원본: `stock/guides/story_script.md` v1.5 · `stock/story/series.md` v1.2 · `stock/story/protagonist.md` v1.3 · `stock/guides/concept.md` · `CLAUDE.md` 주식 줄.
도구: `tools/story_kit.py` v1.0 (단계 명령) · `video/render/story.js` v1.0 (장면 표 → 무대). ※ 연구·교육용 — 투자 권유 아님.

## 0. 토큰 규칙 — 왜 이렇게 하나

측정 (2026-10-23, `tools/token_cost.py`): 이야기 시리즈를 한 대화로 만든 기록(설정·1~4화 제작안·테스트 대본, API 호출 173번)의 가중 합계 1,370만.
- 캐시 읽기(쌓인 맥락을 호출마다 다시 읽음)가 약 45% · 시작 맥락 23% · 계산 코드 12% · 지시사항 읽기 11% · 웹 검색 8%.
- 그래서 **맥락을 작게, 호출을 적게** 한다.

1. **단계마다 새 대화** — A+B 한 대화 · C 한 대화 · D 한 대화. 넘겨 주기는 파일로만 (`story.json`·`요약본.md`·`<ID>_제작안.txt`·`scenes.txt`).
2. **이 파일의 그 단계 절 + 그 단계 '읽을 것'만** 읽는다.
   - 읽지 않는 것: story_script.md · protagonist.md · series.md · stock/guides/README.md · analysis.md · comment_titles.md · status.md 전체 · 지난 화 제작안 전체 · index.html · puppet.js · story.js · render.mjs · 도구 코드.
   - status.md 는 `grep -n '이야기\|재기 일지' guides/status.md` 로 그 줄만.
3. 숫자는 `story_kit nums <키>`, 사실은 `story_kit facts <낱말>` 로 읽는다 (계산 코드·results.json 전체·웹 검색 대신).
   - facts 에 없을 때만 WebSearch(standard 1~2번) → 찾으면 `stock/story/facts.md` 에 같은 꼴로 한 줄 더한다.
4. 큰 파일은 **한 번에 Write**, 고칠 땐 **Edit** 로 그 줄만. 파일 전체를 다시 쓰거나 다시 읽지 않는다.
5. 명령은 한 Bash 에 묶는다. 도구 출력은 짧게 (`| tail`·`grep`). EP-DATA·긴 JSON 을 화면에 찍지 않는다.
6. 썸네일 프롬프트·쇼츠 대본 파일·장면 파일은 **도구가 만든다** (`story_kit export`·`scenes`) — 손으로 쓰지 않는다.
7. 언어별 자막(CC) 번역은 **작업자(Agent) 하나**에 맡긴다 — 결과는 '파일 N개 · check ✅' 한 줄만 받는다.
8. still·영상 장면은 여러 장을 작게 한 장으로 모아 본다.
9. 끝나면 `python3 tools/token_cost.py ~/.claude/projects/<저장소>/<세션>.jsonl --since <시작 시각>` 의 첫 두 줄을 status 주식 절에 적는다 (다음 설계의 근거).

## 1. 늘 지킬 것 (원본 요약)

- 주인공은 `stock/story/card.md` 만 본다. 돈 숫자 = 손실 70%(2억 5천만 원 — 2026-10-23 확정). 영상 처음과 설명란에 '가상 인물·각색'.
- 말투: 해요체 1인칭. 개미 낱말은 처음 나올 때 뜻을 붙인다. 사다·팔다 → 매수·매도. 쓰지 않는 말: 떡상·떡락·가즈아·한강. 한 문장 = 한 생각, 60자 안.
- 구성:
  - `-도입`: 목표 30초 · **마지노선 35초**(200음절 안), 5~7문장. 첫 문장에 제목 맨 앞 낱말 + 결과 숫자. 그 나이대가 실제로 하는 걱정. 사용자가 통과시킨 도입은 제작안 머리에 `- 도입 통과: <날짜> 사용자` 줄.
  - `-방법1`…`-방법N` (3~5개): '첫 번째는 ~예요.' → 많은 개미의 문제 → 저도 → 해결 → 근거.
  - 정리 부분 없음 — 마지막 방법 다음 바로 `-마무리` (v1.5).
  - `-마무리`: 다짐 → 응원 → "시청해주셔서 감사합니다." (다음 화 예고 문장은 넣지 않음 — 1화 방식)
- 숫자는 코드 출력(nums)·원문 사실(facts)만. 백테스트 결론은 결과를 본 뒤에. 개별 종목 추천 없음. 사례는 2020년대 먼저.
- 시리즈: 첫 문장을 '지난 화에서'로 시작하지 않는다. **화마다 다른 경험** — 1화의 70% 손실은 1화에서만, 앞 화에 쓴 경험·근거·숫자·결심·문장은 다시 쓰지 않는다. 근거는 `story_kit facts --unused`, `check` 의 [DUP] 문제 0.
- 길이: 7~8분 (H17 6.3음절/초 — check 가 잰다). 쇼츠 50~55초: 첫 문장에 핵심(누가·언제·무엇 때문에·얼마) → 경위 → 걸린 것 → 질문 → '아래 영상에서'.
- **화면 글자 = 숫자·기호 + 투자자라면 다 아는 영어** (KOSPI·S&P 500·SOXL·BUY·SELL·HOLD·ETF·MARGIN CALL·RULE 1 … — 목록 `stock/story/screen_words.txt`, 밖이면 멈춤) · **한국어 없음**(말은 언어별 CC) · 국기 대신 지수 이름 · 화 배지 `#N`. **문장마다 그 말을 보여 주는 화면**(큰 숫자·차트·칩·목록·주식 소품) — 방법 첫 장면 `BIG RULE N Y` + 소품, 인형만 서 있는 장면은 마무리에만. 썸네일 문구는 숫자·기호 + 같은 목록 영어 (2026-10-24).

## A. 주제 탐색 (대화 1 — 호출 8번 안)

읽을 것: 이 절 · `python3 tools/story_kit.py topics` 출력 (쓴 주제 · 만드는 중 · 이야기 낱말이 든 한국 댓글 좋아요 순 — 정치 댓글 뺌).

1. `topics` 를 돌린다.
2. 후보 3개를 **대화로만** 낸다 (파일 없음). 후보마다:
   - 주제 한 줄 · 바탕 댓글(👍) · card.md 연표의 **아직 안 쓴** 사건 · 증명할 숫자(`facts --unused`·nums 키, 없으면 '새 계산') · 지난 화와 겹치는지.
3. 사용자가 고르면 `python3 tools/story_kit.py new <화> <영상ID> "<전달 내용>"` → `stock/source/<영상ID>/요약본.md`(틀)·`story.json`. 바로 B.

사용자가 주제를 정해 주면 1~2 는 건너뛴다.

## B. 요약본 (A 와 같은 대화 — 호출 10번 안)

읽을 것: `stock/story/card.md` · `요약본.md`(틀) · 필요한 키만 `nums`·`facts`.

- 꼴 = 사용자 꼴 — **텍스트로 핵심만, 사용자가 고친 것처럼** (문장으로 다듬지 않음):
  - `## 롱폼 제목` 3~5 · `## 도입` 3~5줄 · `## 문제 상황 → 해결 방법` (방법마다 문제·좋은 안·근거 줄) · `## 쇼츠 제목` 3~5 · `## 쇼츠 대본` 4~5줄.
  - 예비안은 사용자가 요청할 때만. 사용자가 고친 요약본은 빈 곳만 채운다.
- 새 숫자가 필요하면: `stock/story/calc/series_calc.py` 에 함수 하나(40줄 안) + `main()` 의 `res` 에 키 하나 → 실행 → `nums <키>`.
- 끝: 사용자에게 요약본 경로와 확인할 것(숫자 A/B · 표현 위험)만 알린다. 대화 끝.

## C. 영상 소스 (새 대화 2 — 호출 15번 안)

읽을 것: 이 절 · 사용자가 고친 `요약본.md` · `card.md` · 근거 주소가 필요한 낱말만 `facts <낱말> --url`.

**C-1. 제작안** `stock/source/<ID>/<ID>_제작안.txt` 를 한 번에 Write. 꼴 (`plan_tool` 이 읽음):

```
<영상ID> 제작안 v1.0 — <날짜>
- 길이: (story_kit check 가 고침)

■ 제목
R1. <사용자가 고른 롱폼 제목>
R2. …

■ 대본

==================== 도입 ====================
<한 줄 = 한 문장>

==================== 방법1 · <짧은 이름> ====================
첫 번째는, ….

==================== 마무리 ====================
…
시청해주셔서 감사합니다.

■ 쇼츠 제목
1. …

■ 쇼츠 대본 (약 50초)
<한 줄 = 한 문장>

■ 근거 — 숫자·사실의 출처
  - <문장 속 숫자> → nums 키 또는 facts 줄 (주소)

■ 한계 (설명란 '알려 드립니다')
  - …
```

**C-2. 검사** `python3 tools/story_kit.py check <ID>` → 길이·파트 시각·story_check·제목 2줄(롱폼·쇼츠)·쇼츠 길이.
- ❌ 는 그 문장만 Edit 하고 다시 돌린다. ⚠️ 는 판단해서 고친다. ℹ️ 는 낱말 뜻을 붙였는지 본다.

**C-3. 내보내기** (사용자가 제목 R1·대본을 승인한 뒤):

```
python3 tools/story_kit.py export <ID> --thumb "<줄1>/<줄2>" --pose PHONE --big "−70%" --bg HOME-NIGHT
```

만드는 것:
- `<ID>.txt` — 오디오 대본
- `shorts/<ID>-shorts.txt` — 쇼츠 대본
- `thumbnails/thumbnail_1~3.md` — 본안 + 실험안 2 (다른 자세 · 얼굴 크게)
- `shorts/thumbnails/thumbnail_1.md` — 쇼츠 썸네일 (사진 끝까지)
- `scenes.txt` · `shorts/scenes.txt` — 장면 표 초안

규칙:
- 썸네일 문구 = 제목을 줄인 2줄. 손해 문구면 좌절한 얼굴(PHONE·DESPAIR). 조사로 뜻을 분명히. 나쁜 상황 빨강·중요 노랑은 도구가 고른다.
- 그림은 ChatGPT 에 맡긴다: `python tools/make_summary.py --chatgpt-all stock` → 커밋 고정 주소로 새 ChatGPT 대화 (CLAUDE.md 썸네일 줄).
- 오디오: 사용자가 Kaggle 셀 하나로 (주식 범위) → `narration.mp3` 가 main 에.
- 자막(CC): 작업자 하나에 "`stock/source/<ID>/<ID>.txt` 를 한국어와 문장 1:1 로 en·hi·id·pt·es-419·ja·de·vi·tr 로 옮겨 `subs/` 에 — 규칙 `stock/guides/README.md` 4번, `tools/subs_tool.py check` ✅ 까지".
- C 끝에 커밋: 요약본·story.json·제작안·내보낸 파일.

## D. 영상 (새 대화 3 — 오디오가 온 뒤, 호출 15번 안)

읽을 것: 이 절 · `scenes.txt`(초안). 문장 번호가 헷갈릴 때만 `grep -n` 으로 대본의 그 줄.

**D-1. 순서** (한 Bash 에 묶음):

```
python3 tools/story_kit.py scenes <ID> && node video/render/render.mjs sync stock <ID> && node video/render/render.mjs check stock <ID> 2>&1 | grep CHECK | tail -5
node video/render/render.mjs stills stock <ID> --out <scratchpad>/st --w 640     # 몇 장을 한 장으로 모아 본다
node video/render/render.mjs video stock <ID>                                    # 완성 mp4 — 장면 몇 개를 뽑아 직접 본다 (CLAUDE.md)
```

- 쇼츠: `scenes <ID> --shorts` → 영상ID `<ID>-shorts`. 첫 문장 동안 썸네일 그림(K.cover) — 그림이 있어야 최종본.
- 새 컨테이너면 먼저: `cd video/render && npm install` · `node video/scripts/get-fonts.mjs`.
- 배경 5장(`stock/story/puppet/P-<배경>.jpg`)·설명 소품(`stock/story/puppet/props/<이름>.png`)이 아직 없으면 임시 그림(회색) + render check 의 page_errors. 프롬프트 = `stock/story/puppet/backgrounds_chatgpt.md` · `props_chatgpt.md` (커밋 고정 주소로 새 ChatGPT 대화에).
- 새 소품이 필요하면 `props_chatgpt.md` 표 끝에 번호·저장 경로·프롬프트를 더한다 (STYLE·CUTOUT·PROP 문단 그대로 · 글자·숫자·기호 없는 그림 · 다른 화에서 다시 써도 됨).

**D-2. 장면 표 문법** — 한 줄 = 장면 하나. 시각은 문장 번호라서 오디오가 바뀌어도 그대로다.

`문장 | 배경 | 인형(+소품) | 화면`

- 문장: `n` · `n-m` (v1.5 `정리` 줄 없음).
- 배경: HOME-NIGHT · OFFICE · STREET-DAWN · BOARD · PAPER.
- 인형: `자세[@L|C|R][>in|walk|rise|pop][!]`
  - 여럿이면 `+` 로 잇는다. 장면 안에서 바뀌면 `<문장>[:<낱말>]:자세` (종이 카드 뒤집듯 바뀜). `!` = 좌우 뒤집기.
  - 자세: BONSEOK · WALK · PHONE · DESPAIR · RESOLVE · STUDY · BACK · SMILE · CROWD.
  - 앞 장면과 배경·자세·자리가 같으면 이어진다 (들어오는 움직임 없음). 화면이 있으면 롱폼 인형은 왼쪽으로 간다.
- **소품**(v1.5): 인형 칸에 `*이름[@L|C|R][>rise|pop]` 을 `+` 로 더한다 — 예 `BACK@L+13:몰빵:*CHIP-ALL-IN@R`.
  - **먼저 `python3 tools/story_kit.py props [낱말]`** (예: `props 빚`) — 공통 소품(뜻·쓴 화·✅ 그림 있음)에서 맞는 것을 다시 쓴다. 없을 때만 `props_chatgpt.md` 표 끝에 새로 (일반적인 뜻으로 — 특정 회사·화 숫자·장면 묘사 금지, 꼭 그 화 전용이면 '전용'), 후보(…)는 표로 옮겨 프롬프트를 쓴다.
  - 이름 = `stock/story/puppet/props_chatgpt.md` (v3.0 — **주식 그림**: 차트·캔들·매매 앱·황소·곰·반도체 칩 …) 표에 있는 것만 (`MARGIN-CALL` 반대매매 · `CHIP-ALL-IN` 몰빵 · `INDEX-BASKET` 지수 · `BOX-RANGE` 박스권 · `BULL`·`BEAR` · `FEAR-GREED` 과열 · `RULE-NOTE` 원칙 · `DCA-JAR` 적립 …).
  - 롱폼은 오른쪽 바닥에 선다 (기본 `@R` — 인형은 `@L`) · 쇼츠는 위 가운데에 떠 있다 (`@C` 만). 튀어나옴(pop, 기본)·솟아오름(rise). `<문장>[:<낱말>]:*이름` = 그 말에 나타남 — 같은 자리 앞 소품은 사라짐.
  - 소품은 **화면 없는 장면이나 BIG 과만** (화면 칸과 겹침). BIG 과 같이 쓰면 숫자가 소품 위 한 줄로 올라간다 (`BIG −8.95% R icon=kr` + `*BARRIER`).
  - 같은 소품이 앞 장면과 같은 자리·배경이면 이어진다 (다시 튀어나오지 않음).
- 화면 — 뒤에 `@n[:낱말]` 을 붙이면 그 말에 나타난다:

| 적는 꼴 | 화면 |
|---|---|
| `K1 357140000>107140000` | 계좌 금액이 굴러감 (내려가면 빨강·▼%) |
| `K2 2020,2021,*2024,2026` | 연표 (`*` = 빛나는 해 · 6개 넘으면 처음·끝·빛나는 해만 글자) |
| `K3 100,49,100,498 base=100 lab=2007,2009,2013,2026 end=+398%` | 차트 (선이 그려짐 · 기준 = 노란 점선) |
| `K4 1Y:24.3%:R 10Y:6.5%:Y 15Y:0%:G icon=hourglass` | 막대 (이름:값[:색]) · `icon=` 단위 그림 (모래시계 = 기간, kr = 한국 지수) |
| `K5 !x3 !debt +basket +calendar` | 아이콘 (`!` 하지 않음 · `+` 할 것) — basket drop debt swap x3 hourglass calendar phone book up down bell lock globe coin house kr us pct fx people chart **chip**(반도체) **briefcase**(회사) **school**(학원) · `>` = 화살표 칸 |
| `K5 'KOSPI > 'S&P_500` · `K5 !'BUY !'SELL +'HOLD` | **글자 칩** (v1.8) — `'` 뒤 글자(밑줄 = 띄어쓰기), `!` 빨간 ✗ · `+` 청록 ✓. 그림과 섞어도 됨. 칸 높이는 한 줄에 맞춰짐 |
| `LIST 73:!DEBT; 74:+MAX 10% PER STOCK; 75:+3 REASONS BEFORE BUY title=MY_RULES` | **목록** (v1.8) — 줄마다 ✓/✗ + 짧은 영어, `n:` = 문장 n 에 나타남 |
| `BIG KOSPI −34% R` · `BIG RULE 1 Y` | 큰 숫자·글자 (끝이 색 — R 손해 · G 회복 · Y 기준 · W) · `icon=` 무엇의 숫자인지 그림 (debt 빚 · lock 확정 · calendar 해마다) · 소품과 같이 쓰면 소품 위 한 줄 |
| `PIE 55 R label=50%+ cap=SAMSUNG_+_SK_HYNIX title=KOSPI` | 원그래프 — 전체 중 몫 (가운데 숫자 · `cap=` 아래 짧은 글 · `icon=` 무엇의 몫) |
| 모든 칸 화면 뒤 `title=S&P_500` | **이름표 탭** (v1.8) — 칸 위 왼쪽에 지수·종목 이름 (KOSPI · S&P 500 · MY ACCOUNT · RULE 1) |

- 화면 글자는 숫자·기호 + `stock/story/screen_words.txt` 영어만 — **한국어 없음** (story_kit scenes 와 render check 가 잰다). 왼쪽 위 `#N`·끝의 `#N+1 ▶` 는 저절로 붙는다.

**D-3. 고칠 때**는 scenes.txt 의 그 줄만 Edit → `scenes` 다시. index.html·story.js 는 열지 않는다.
- 새 부품이 꼭 필요할 때만 story.js 에 더하고, 이 절 표에 한 줄 더한다.

## 끝내기 전 점검

- [ ] 그 단계 절만 읽었다 · 큰 파일을 다시 쓰거나 다시 읽지 않았다
- [ ] (C) check ❌ 0 · 제목 2줄 ✅ · 쇼츠 50~55초 · 숫자는 nums·facts 에서만, 근거 절에 출처
- [ ] (D) render check 문제 0 · still 과 완성 영상 장면을 직접 봤다
- [ ] status.md 주식 절과 맨 위 버전 줄 · token_cost 두 줄 · main 에 푸시
