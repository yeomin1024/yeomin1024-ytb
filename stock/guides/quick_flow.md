# 주식 — 유튜브 분석부터 요약본·대본까지 (새 세션은 이 파일 하나로)

VERSION: v1.2 — 2026-10-29 — **10b 정답 미리 확인** (요약본 전 · 사용자 지시 "왜 이렇게 주제부터 잘못 판단하는거야? … 그렇게 절차정하고 주제 걸러봐") — `stock/topics/README.md` '정답 미리 확인'. (v1.1 — 2026-10-28 — 12단계에 반론 검토 반복 (반론 페르소나 `tools/rebuttal_persona.py` · 회차마다 새 검토자). (v1.0 — 2026-10-28 — 최초 (사용자 지시 "지금 있는 주식 주제 관련 세션에서 유튜브 분석에서 요약본까지 생성하는 과정을 토큰 가장 아낄 수 있는 구조로 해서 처음 생성한 세션이 똑같이 진행할 수 있도록 지시사항 파일을 만들어 그리고 대본 하나 만들어봐"). 진행 확인 도구 `tools/flow_status.py` v1.0 · 첫 적용 대본 `stock/source/timing-test-2026-10/`.)
※ 연구·교육용 — 투자 권유가 아님.

**이 파일 + 아래 표가 가리킨 줄만 읽는다.** 규칙의 까닭이 필요할 때만 '근거' 칸의 문서 절. 재테크·역사도 같은 명령에 주제 이름만 바꿔 쓴다 (`<주제>/topics/README.md`).

## 0. 시작 — 명령 3개 (약 2천 토큰)

```bash
git pull --rebase                          # CLAUDE.md: main 에 바로. 세션이 작업 브랜치를 정해 주면 그 브랜치
python3 tools/flow_status.py stock         # 단계마다 마지막 갱신 · ✅/다시?/없음 · 편마다 다음 할 일 (읽기만, 1초)
python3 tools/cloud_run.py stock status 2>&1 | tail -n 20    # 1~2단계를 할 때만 — 할당량·승인 수·남은 것
```
- `flow_status` 의 **'다음 단계'** 줄부터 아래 1번 표의 그 줄만 한다. '다시?'는 권고 — 승인 영상이 늘지 않았으면(analysis.md 0번 승인 수 그대로) 5~8단계는 건너뛰어도 된다.
- 사용자가 할 일을 정해 주면 그 일부터 (예: "T003 으로 요약본" → 11단계, "대본" → 12단계).

### 읽지 않는 것 (토큰 — 영상 한 편 토큰의 약 40%가 이런 읽기였음, `tools/token_cost.py`)
| 파일 | 크기 | 대신 |
|---|---|---|
| `guides/status.md` 전체 | 약 7만 토큰 | 이 파일 · `flow_status` (필요하면 '1. 한눈에' 표만) |
| `stock/result/outliers/analysis.md` 전체 | 27만 자 | 0번 '자료와 한계'만 — `sed -n '/^## 0\./,/^## 1\./p'` · 주제·요약본 재료는 도구가 모아 줌(`material.md`) |
| `shorts/analysis.md` · `weekly.md` · `*.xlsx` | 13만 자 · 사람용 | 쇼츠 규칙을 만들 때만 그 절 |
| 첫 편 요약본 `simri-test-2026-10/요약본.txt` | 6만 자 | `quick_test.md` (규칙만 모음) |
| 도구 로그 | 수백 줄 | `--log-level WARNING` 또는 `\| tail -n 5` — 숫자 확인은 결과 파일·`results.json` 에서 |

## 1. 단계표

| # | 단계 | 명령 (주제 = stock) | 결과 | Claude 가 읽는 것 (이것만) | Claude 판단 |
|---|---|---|---|---|---|
| 1 | 탐색 | `cloud_run.py stock explore --weeks 26` → `explore --shorts --weeks 26` (③ 기간 없는 검색은 할당량 2,000단위 넘게 남을 때만 `explore --alltime-only`) | `stock/cloud_cache/cache.tgz` (저절로 묶음) | 끝 줄 `\| tail -n 5` | 429·403 → 멈추고 `wait-reset --then resume` (Cloud 프로젝트를 늘리라고 권하지 않음) |
| 2 | 승인·분석 | `list --checked` → 주제 밖은 `uncheck ID…` → `approve` → `analyze` (남으면 `resume`) | `result/outliers/analysis.md` · `shorts/analysis.md` · `weekly.md` · `personas.md`(저절로) | `list` 의 제목 칸 · analysis.md 0번 | 주제 밖(연예·영화·코인·정치·다른 뜻 '국장·미장')은 풀고, 되풀이되면 `stock/analysis_rules.toml` 에 더함. 탐색이 덜 끝난 날은 줄어든 비교 집단으로 결과를 덮지 않음 |
| 3 | 확인 엑셀 | `python3 tools/target_check.py stock` | `target_check.md`·`.xlsx` | md (3천 자) | — |
| 4 | 페르소나 | (2단계가 저절로) `python3 tools/personas.py stock` | `personas.md` | **0번 표만** | 손으로 고치지 않음 (사전은 `stock/personas.toml`) |
| 5 | 댓글 유형 | `python3 tools/comment_types.py stock report` | `comment_types.md` | 안 읽음 | 분류 규칙을 고칠 때만 `sample`·`evaluate` |
| 6 | 댓글 묶음 | `python3 tools/comment_clusters.py stock` | `comment_clusters.md`·`.xlsx` | '한국 · 1~4주 전' 표만 | 영어 번역 새 글 = `comment_translate_todo.tsv` → Claude 번역 → `--merge` |
| 7 | 댓글 니즈 | `comment_title_ideas.py stock candidates` → **Claude 가 고름** → `match` | `comment_titles.md` | `comment_title_candidates.tsv` 좋아요 상위 · 결과 1번 표 | 25~30개를 `comment_title_picks.tsv` 에 (정치 ✗ · 칸 = pick·country·kind·likes·video_id·comment·topic·match 정규식) |
| 8 | 콘텐츠 엑셀 | `python3 tools/content_analysis.py stock` | `content_analysis.md`·`.xlsx` | md (2천 자) | **새 성공 사례만** 그림을 보고 `thumb_codes.tsv` 에 줄 더함 — 묶음 그림 `analysis_thumbs_*.jpg`(여러 장이 한 그림), 한 장씩 열지 않음 |
| 9 | 대본 받을 목록 | `python3 tools/pc_transcribe.py list stock` | `transcript_todo.md`·`.csv` | 앞 10줄 | 사용자 PC 가 `run_analyzer.ps1 -Transcribe -Folder stock` → 대본 오면 2단계 `analyze` 다시 |
| 10 | 주제 탐색 | `python3 tools/topic_ideas.py stock status` (평가 가져오기·갱신은 3번) | `stock/topics/주제탐색.md` · 평가판 | **1번 표만** · 새 후보를 쓸 때만 `material.md`(2만 자 — 페르소나·니즈·성공 비율·쓴 주제가 다 모여 있음) | '갱신 필요'면 새 후보 25개 안팎 `pool/<날짜>.json` (칸 = `stock/topics/README.md` '후보 한 개' — 결론 = 숫자·판정 한 문장 + 판정 규칙) → `add` → 평가판 같은 주소로 다시 올림 |
| 10b | **정답 미리 확인** | `python3 -B stock/topics/precheck/precheck.py` (새 주제는 함수 하나 더함) → Claude 가 `precheck/conclusions_<날짜>.json` → `topic_ideas.py stock precheck <결과.json> <결론.json>` | `precheck_<날짜>.json` · 주제탐색.md '미리 계산' 칸 · `stock/topics/정답확인.md` | 로그 `[TOPIC]` 줄만 | 분류(정답형·차이없음·사실형·계산형·조건부형·미확인) — **조건부형은 테스트형 ✗ · 미확인은 안 씀** · 사용자에게 주제마다 '정답 한 문장 · 미리 계산 결과 · 영상 꼴' 세 줄 → 좋음·나쁨 받은 뒤 11단계 |
| 11 | 요약본 | 사용자가 주제 ID 를 고름 → 새 편 폴더 + `요약본_안.json` → `python3 tools/summary_ideas.py stock status` | 편 `요약본.txt` · `stock/topics/요약본_평가판.html` | `stock/topics/요약본_material.md`(5천 자) · `quick_test.md` 0번 · `stock/guides/channel.md` 3번(다섯 줄) | 2번 '요약본 쓰기' |
| 12 | 대본 | 사용자가 안을 고름 (또는 "대본 만들어") → `calc/calc.py` → `<영상ID>.txt` → `persona_review.py` → **반론 검토 반복** | 대본 · `calc/results.json` · `persona_review.md` · `대본_근거.md` · `대본_반론_검토.md` | `quick_test.md` 1~9·12번 + 그 편 요약본 | 2번 '대본 쓰기' |

근거: 1·2 `stock/README.md` '클라우드에서 분석' · `guides/pc_analysis.md` · 5~8 CLAUDE.md '분석' · 10·10b `stock/topics/README.md` · 11·12 `stock/guides/quick_test.md` · `channel.md`.

## 2. Claude 가 글을 쓰는 곳 — 꼴만

### 요약본 쓰기 (11단계)
0. **10b 정답 미리 확인을 통과한 주제만** (주제탐색.md '미리 계산' 칸이 비었거나 ⛔ 면 쓰지 않음) — [방향] 첫 줄에 분류와 고친 결론, 꼴은 분류가 허락하는 것만 (`stock/topics/README.md` 표).
1. 편 폴더 `stock/source/<영상ID>/` (영상ID = 영어 낱말-월, 예 `timing-test-2026-10`) · 머리에 `주제 ID: T0NN` (그 주제는 저절로 '작성중').
2. `stock/topics/settings.toml` 에 `[summary]` `EPISODES = {F = "jaemu-test-2026-10", P = "portfolio-test-2026-10", M = "timing-test-2026-10", <새 글자> = "<영상ID>"}` (글자 = 안 ID 머리 — 없으면 도구 기본 3편만).
3. `요약본_안.json` 꼴은 `stock/source/timing-test-2026-10/요약본_안.json` **첫 60줄만** 보고 따라 씀: `direction`(방향 3~5줄 + `notes` 출처) · `rounds[0].answers` 안 5개 × 칸 8개(LT·LM·LS·LF·ST·SM·SS·SF, 칸마다 `text` + `tags`).
4. 숫자는 그 편 `calc` 출력만 — 계산 전이면 `○○` + 주석 'calc 뒤'. 본문 = 영상 내용만, 출처·근거 = `#` 주석 (`quick_test.md` 0번).
5. `summary_ideas.py stock status` → ✅ 이 될 때까지 (제목 2줄 — 'PC 다음 동영상(좁은 화면)' 때문에 30자 안팎). 평가판은 Artifact publish 로 같은 주소에.

### 대본 쓰기 (12단계)
1. **계산 먼저** `stock/source/<영상ID>/calc/calc.py` — 꼴은 `timing-test-2026-10/calc/calc.py` (받기 `--fetch` 는 CSV 가 없을 때만 · 검사 VALIDATE · 판정 규칙을 계산 전에 머리 주석에 · 5년 민감도 ROBUST · 점수 `test_score.check_rules` · 가상 응시 · `--selftest` · `results.json`). 실제 주가는 Yahoo chart API (이 환경에서 됨).
2. **판정이 뒤집히는 항목은 점수에 안 씀** (`quick_test.md` 12번) — 바꾼 까닭은 calc CHANGELOG 와 `대본_근거.md` 1번에.
3. 대본 `<영상ID>.txt` = `-도입`·`-항목 N`·`-통과 기준`·`-해설`·`-정리`·`-마무리` 머리 줄 + 한 줄 한 문장(50자 이하) — 꼴은 `timing-test-2026-10.txt` (머리 주석 없음 — TTS 가 읽음, 근거는 `대본_근거.md`).
4. 검사: `python3 tools/persona_review.py stock <대본>` (풀이 없이 나온 말 0 · 50자 넘는 문장 0) · 길이 = 도구 어림 × 1.16 (첫 편 실제 6.8 → 7.9분) 이 7~8분 · 숫자마다 calc 키를 `대본_근거.md` 2번 표에.
5. **반론 검토 반복** — 반론 페르소나 `stock/result/outliers/rebuttal_persona.md` (만들기·갱신: `rebuttal_persona.py stock candidates` → Claude 가 내용 반론만 `rebuttal_picks.tsv` → `build`). 회차마다 **새 하위 에이전트**(앞 회차를 모름)에게 페르소나·대본·`results.json`·`calc.py` 를 주고 반론 표(상·중·하)·항목별 정답 명확성을 받음 → 고침 → 다시. 멈춤 = 상 0 · 중 ≤1 · 다섯 항목 명확 (최대 5회차). 검토 지시문 꼴은 `timing-test-2026-10/대본_반론_검토.md` 0번.
6. 다음은 사용자: 안·제목 평가 → 쇼츠(`quick_test.md` 9번) → Kaggle 오디오.

## 3. 사용자 평가 가져오기 (도구가 못 읽는 것)
- 주제 평가판 https://claude.ai/artifact/Y5d3kdE2nShVxRgzBBEpV8 · 요약본 평가판 https://claude.ai/artifact/BCvJ17G2sL55aSAviHqTie
- `ArtifactData list` (url = 위 주소, collection `marks`) → 결과를 스크래치 파일에 그대로 → `topic_ideas.py stock import <파일>` · `summary_ideas.py stock import <파일>` → `status`.
- 채팅 평가: `topic_ideas.py stock mark T003 좋음 "까닭"` · `summary_ideas.py stock mark M3-LT 좋음 "까닭"`. 요약본 줄 끝 `=> 좋음` 은 `status` 가 저절로 읽음.

## 4. 올리기
- 단계가 끝날 때마다 커밋: `[주식] <단계> — <한 줄 결과> (<도구 버전>)` + CLAUDE.md·세션이 정한 꼬리 줄. 비밀값(.env·키)은 넣지 않음.
- 일이 끝나면 `guides/status.md` 맨 위 버전 줄 한 줄 + `stock/README.md` 버전 줄 + `CHANGELOG.md` (같은 꼴 — 왜·바꾼 것·확인·한계).
