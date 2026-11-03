# 주식 — 1단계 주제 평가판 세션 (이 세션은 이 판 하나만)

VERSION: v1.1 — 2026-11-03 — 1~4편(이미 대본이 있는 편)도 판에 — `topics_1-4편.json` E1~E4 (`existing` 칸) — 사용자 지시 "주식 주제 평가판에 대본 4개 올려봐 피드백하게".
(v1.0 — 2026-11-03 — 사용자 지시 2026-11-03 "새 세션 3개에서 각각 '지시사항 읽고 주제 평가판, 대본 평가판, 쇼츠 평가판 만들어'라고만 해도 지금처럼 할 수 있게 … 세션당 평가판 하나야 그리고 주제는 분석결과도 참고하는거야".
※ 연구·교육용 — 투자 권유가 아님.

**사용자가 "지시사항 읽고 주제 평가판 만들어"(또는 "주제 평가판 피드백 했어") → 이 파일만 읽고 아래 순서대로.** 대본·쇼츠 판은 다른 세션이 맡는다 — 이 세션은 `stock/topics/board/topics_*.json`·`stock/topics/주제평가판.html` 만 고친다.
판 = **https://claude.ai/artifact/Rawg2U7g3tEdSvEu5skTDN** (이미 있음 — 늘 같은 주소를 갱신, 새 판을 만들지 않음).

## 0. 시작 (명령 3개)

```bash
git pull --rebase origin main
python3 tools/flow_status.py stock 2>&1 | tail -n 25      # 분석이 언제 것인지 (읽기만)
python3 - <<'E'                                            # 지금 묶음의 기획안 id·주제 (이미 낸 것과 겹치지 않게)
import json,glob
for f in sorted(glob.glob('stock/topics/board/topics_*.json')):
    for p in json.load(open(f))['packages']: print(f[-15:-5], p['id'], p['theme'])
E
```
- 판 상태: `ArtifactData list verdicts`(url = 위 판) — {id, verdict pass·hold·fail} · `ArtifactData query feedback where status == new`.
- 분석이 7일 넘게 묵었으면 사용자에게 한 줄로 알림 (분석은 사용자가 시킬 때만 — `stock/guides/quick_flow.md` 1~8단계). 묵은 분석으로도 진행.

## 1. 할 일 고르기

| 판 상태 | 할 일 |
|---|---|
| 새 피드백(status=new) | 그 기획안 칸을 고침 → 2번 점검 → 판 다시 → 피드백마다 done·reply |
| 판정 hold(보류) | 피드백 뜻대로 고침 (피드백이 없으면 사용자에게 무엇을 바꿀지 한 줄로 물음) |
| 판정 fail(탈락) | 그 주제는 다시 쓰지 않음 (비슷한 주제도) — 다음 묶음에서 까닭을 피함 |
| 판정 pass(통과) | 이 세션은 할 일 없음 — **대본 평가판 세션**이 가져감 |
| **E1~E4 (1~4편 — `existing` 칸, 이미 대본 있음)** 피드백 | `stock/topics/board/topics_1-4편.json` 의 그 칸을 고침 · 대본도 바뀌어야 하면 reply 끝에 **'대본 반영 필요 (e?-long)'** — 대본 세션이 그 편 대본에 반영 (이 세션은 대본을 고치지 않음) |
| '평가 전' 기획안이 없음 (모두 판정됨) 또는 사용자가 "새로" | **새 묶음 10개** (3번) |

## 2. 주제는 분석 결과로 (필수 — 사용자 "주제는 분석결과도 참고하는거야")

새 기획안을 쓰기 전에 이것만 읽는다 (합쳐 약 2만 자):
1. `stock/guides/channel.md` 0~1번 — 채널 목적 = **리스크를 줄이고 천천히 버는 장기 투자 · 숫자는 '덜 잃었나'** · 꼴 = 테스트형 (호기심 먼저).
2. `stock/result/outliers/analysis.md` **0번 '자료와 한계'만** (`sed -n '/^## 0\./,/^## 1\./p'`).
3. `stock/result/outliers/personas.md` **0번 표** — 기획안 `persona` 칸 (P1 3040 직장인 · P2 6070 · P3 50대 노후).
4. `stock/result/outliers/comment_titles.md` **1번 '한눈에'** — 댓글 니즈 K01~ (시청자가 실제로 묻는 것) → 기획안마다 하나 이상.
5. `stock/result/outliers/comment_clusters.md` **'한국 · 1~4주 전' 표** — 요즘 늘어난 댓글 묶음.
6. `stock/result/outliers/content_analysis.md` (2천 자) + `stock/guides/data_insights.md` **5-1** — 제목·썸네일 문구 숫자 (손해·경고·질문형 배수 · 보조 = 속마음 말).
7. 이미 쓴 것: `stock/topics/롱폼대본_2026-10-31.md` 표(1~4편 항목) · 위 0번 목록 · 판 fail — 같은 주제·같은 항목 ✗.

→ 기획안 `basis` 칸에 **어느 분석 숫자·니즈를 따랐는지** 적는다 (예: "댓글 니즈 K01 빚내서 투자 · P1 원하는 말 '여윳돈' · 5-1 손해·경고형 배수 22.9 · 보조 = 속마음 말 배수 338"). 근거가 없으면 그 주제는 쓰지 않는다.

## 3. 새 묶음 10개 — `stock/topics/board/topics_<오늘>.json`

꼴·칸 = `stock/guides/quick_board.md` **2번 표만** (id 는 이어서 — B11…). 핵심:
- `message`(전달 내용 한 문장) · `approach`(테스트형 · 인물 성씨 · 실제 날짜 · 다섯 갈림길 · 정답 판정 기준) · `title` 「…사람은 절대 통과 못하는 주식 테스트」(화면 2줄) · `thumb_main`(2줄) · `thumb_sub` · `verify`(다른 기간·하락장으로 정답이 뒤집히나) · `basis` · 쇼츠 칸 `s_title`·`s_thumb_main`·`s_thumb_sub`·`s_message` 는 **써 두기만** (3단계에서 씀).
- 정답이 기간·가정에 따라 뒤집힐 것 같으면 `stock/topics/precheck/precheck.py`·`risk.py` 로 미리 확인하고(`stock/topics/README.md` 7번), 뒤집히면 그 주제는 뺀다.
- 사용자 피드백 규칙(quick_board 4번 '사용자 피드백 규칙' 1~17)이 기획안 단계에도 걸리는 것: 4년 안 · S&P 500 비교 · 종목은 ETF 말고 · 편끼리 항목·멘트 겹치지 않게(14·17) · 보기에 사람마다 다른 수치 ✗(12).

## 4. 점검 → 판 → 답

```bash
python3 tools/board_check.py package stock stock/topics/board/topics_<날짜>.json --write                # 롱폼 칸 ❌ 0 까지
python3 tools/board_check.py package stock stock/topics/board/topics_<날짜>.json --stage shorts --write # 쇼츠 칸(써 둔 것) 점검만
python3 tools/topic_board.py                                                                             # 주제평가판.html (이 판만)
```
- 판 올리기: 다른 세션에서 처음 올릴 땐 `Artifact action=read url=https://claude.ai/artifact/Rawg2U7g3tEdSvEu5skTDN` 한 번 → `Artifact publish file_path=stock/topics/주제평가판.html url=<같은 주소>` (capabilities 는 빼면 그대로).
- 피드백 답: `ArtifactData batch` 로 피드백마다 `update {status:"done", reply:"<무엇을 어떻게>", updatedAt}` (`if_version` = 읽은 version).
- 판정은 사용자가 판에서 누른다 — Claude 가 대신 쓰지 않음 (사용자가 채팅으로 "○○ 통과"라고 하면 그때만 `verdicts/<id>` 에 씀).

## 5. 끝

- 사용자 피드백이 규칙이 될 만하면 `quick_board.md` 4번 '사용자 피드백 규칙'에 한 줄 (원문 인용).
- `CHANGELOG.md`·`guides/status.md` 맨 위 한 줄 → 커밋 → `git pull --rebase origin main` → `git push origin HEAD:main` (세션이 작업 브랜치를 정해 주면 그 브랜치에도). 다른 세션과 CHANGELOG·status 맨 위가 부딪히면 **양쪽 줄 모두 남김**.
- 사용자에게: 판 주소 · 새로 올린 기획안 수 · 반영한 피드백 · "통과한 주제는 대본 평가판 세션에서 '대본 평가판 만들어'".

### 읽지 않는 것
`guides/status.md` 전체 · `analysis.md` 0번 밖 · 대본·쇼츠 판 · 다른 단계 지시서(`board_2_script.md`·`board_3_shorts.md`) · `CHANGELOG.md`.
