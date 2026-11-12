# 주식 — 2단계 대본 평가판 세션 (이 세션은 이 판 하나만)

VERSION: v1.5 — 2026-11-12 — 3번 **페르소나 반복 검증**(이탈·반론 2회차 이상 · 편 package.json 제목·썸네일 피드 시험) — board_check v1.11 이 기록이 없으면 ❌ — 사용자 지시 "제목,썸네일, 대본 만들때 자꾸 페르소나 반복 검증 빼먹는데 빼먹지 말도록 주제별 지시사항 수정해봐".
(v1.4) — 2026-11-04 — 말머리는 편마다 다르게 · 다른 편과 같은 문장 ✗ (quick_board 규칙 43 · board_check K10).
(v1.3) — 2026-11-04 — 꼴 요약에 질문 뒤 '선택해 보세요.' · '3, 2, 1.' (quick_board 규칙 41).
(v1.2 — 2026-11-04 — 꼴 요약 = 선택마다 바로 정답·해설 (quick_board 규칙 25).)
(v1.1 — 2026-11-03 — 주제 판의 E1~E4(1~4편, `existing`)는 새로 쓰지 않음 · 주제 판 피드백 reply 의 '대본 반영 필요' 를 그 편 대본에.)
(v1.0 — 2026-11-03 — 사용자 지시 2026-11-03 "새 세션 3개에서 각각 '지시사항 읽고 주제 평가판, 대본 평가판, 쇼츠 평가판 만들어'라고만 해도 지금처럼 할 수 있게 … 세션당 평가판 하나야".
※ 연구·교육용 — 투자 권유가 아님.

**사용자가 "지시사항 읽고 대본 평가판 만들어"(또는 "대본 피드백 했어") → 이 파일만 읽고 아래 순서대로.** 주제·쇼츠 판은 다른 세션 — 이 세션은 롱폼 대본·그 계산·`stock/topics/board/script_board.json`·`stock/topics/대본피드백판.html` 만 고친다.
판 = **https://claude.ai/artifact/7UQobTs4TU45V4GCMqWCZz** (이미 있음 — 늘 같은 주소를 갱신). 주제 판(읽기만) = https://claude.ai/artifact/Rawg2U7g3tEdSvEu5skTDN.

## 0. 시작

```bash
git pull --rebase origin main
python3 - <<'E'                                   # 이미 판에 있는 대본 (1~4편 + extra)
import json; print([e['key'] for e in json.load(open('stock/topics/board/script_board.json'))['extra']])
E
```
- 주제 판: `ArtifactData list verdicts`(url = 주제 판) → **verdict == pass 인데 extra 에 아직 없는 id** = 새로 쓸 대본.
- 대본 판: `ArtifactData query feedback where status == new` · `list verdicts` (통과 = 쇼츠 세션이 가져감).

## 1. 할 일

| 상태 | 할 일 |
|---|---|
| 대본 판 새 피드백 | 그 대본을 고침 (2번 규칙) → 계산 다시 → 3번 점검 → 판 → done·reply · 대본 판(v)을 올림 |
| 주제 판 통과 · 대본 없음 | 새 롱폼 대본 (2번) → 3번 → extra 에 한 줄 → 판 |
| 주제 판 E1~E4 (1~4편 — 기획안 `existing` = 이미 이 판에 있는 key) | 새로 쓰지 않음 · 주제 판 `feedback` 중 reply 에 **'대본 반영 필요 (e?-long)'** 가 있고 아직 반영 안 한 것 → 그 편 대본(`stock/topics/롱폼대본_2026-10-31.md` 표의 파일)에 반영 → `LONG_VER` 올림 |
| 둘 다 없음 | 사용자에게 "주제 판에서 통과한 새 주제가 없습니다" 한 줄 |

## 2. 대본 쓰기 (한 편 = 계산 파일 하나 + 대본 폴더 하나)

읽을 것: 그 기획안(`stock/topics/board/topics_*.json` 의 그 id) · `stock/guides/quick_board.md` **4번(롱폼 대본 꼴 + 사용자 피드백 규칙 1~17)·5번(계산)** · 본보기 하나 `stock/source/ppalli-test-2026-11/ppalli-test-2026-11.txt` (1편 v11).
- 폴더 `stock/source/<영문-짧게>-test-<연-월>/` — 대본 `<폴더명>.txt` (한 줄 한 문장 · `-장 이름` 줄) · `upload.md`(설명란·계산 기준·챕터·출처) · `tts_lexicon.tsv`(영어·숫자 읽는 소리).
- 계산 = **새 파일** `stock/topics/precheck/longform_<id>.py` (`longform_items.py` 의 load·Ser 를 가져다 씀, 새 종목은 `precheck.fetch`) → `longform_<id>_<날짜>.json`. 대본 숫자는 이 출력만.
- 꼴 요약: 도입(편마다 다른 꼴 — 규칙 17) → 선택 1~5 (**주어 = '당신'** — 규칙 23 · 배경·그때 뉴스·왜 올랐는지 사실 → '여기서 당신은 …하시겠습니까?' / '아니면 …하시겠습니까?' — 보기에 수치 ✗ → '선택해 보세요.' → '3, 2, 1.' (규칙 41) → **'이때는 …것이 옳은 선택입니다.' → 바로 그 선택의 해설**(그날·종목 → 오답·정답 결과 → 물론… → 하지만… → 통계 하나 → 결론) — 규칙 25) → 결과(인물 결과 → 통과·주의·불통과) → 정리(사용자 문장 꼴, 공통점 문장 ✗) → '그럼 모두 성공 투자 하시기 바랍니다.' → '시청해주셔서 감사합니다.' · 7~8분(6.3음절/초) · 50자 넘는 문장 ✗.
- 여러 편을 한꺼번에 쓸 땐 편마다 작업자(fork)로 나눠도 됨 — 공유 파일(script_board.json·도구)은 이 세션이 마지막에 한 번에.

## 3. 점검 → 판 → 답

```bash
python3 tools/board_check.py script stock <대본.txt> --calc <json> --upload <upload.md> --allow "<사용자 문장 일부>"   # ❌ 0
python3 tools/persona_review.py stock <대본.txt>
# ★ 페르소나 반복 검증 (빠뜨리지 않음 — guides/persona_loop.md): 이탈(대상 페르소나 = 기획안 persona) · 반론, 각 2회차 이상 · 회차마다 새 Agent · 대본을 고치면 그 단계 다시
python3 tools/persona_gate.py prompt stock script_exit <편 폴더>/persona_loop.json <영상ID> --script <대본.txt> --persona <P?> --out <지시문.md>
python3 tools/persona_gate.py prompt stock script_rebuttal <편 폴더>/persona_loop.json <영상ID> --script <대본.txt> --out <지시문.md>
python3 tools/persona_gate.py add … → check <편 폴더>/persona_loop.json <영상ID> --script <대본.txt> --plan <편 폴더>/package.json   # 모두 ✅
# 편 제목·썸네일 문구는 <편 폴더>/package.json (기획안에서 옮김) — 바꾸면 title 피드 시험도 다시 (upload.md 1번 제목 = package.json title)
# script_board.json 'extra' 에 {key:'B11-long', ep:'B11', label:'B11 <주제>', kind:'long', title, ver:'대본 v1', file}
python3 tools/script_feedback_board.py --only long        # 대본피드백판.html 만 (쇼츠 판은 건드리지 않음)
```
- 1~4편 대본을 고치면 `tools/script_feedback_board.py` 의 `LONG_VER` 를, 새 편은 extra 의 `ver` 를 올림 + `stock/topics/롱폼대본_2026-10-31.md` 표 줄.
- 판 올리기: 다른 세션에서 처음 올릴 땐 `Artifact action=read url=<판>` 한 번 → `Artifact publish file_path=stock/topics/대본피드백판.html url=<판>`.
- 피드백 답: `ArtifactData batch` — `update {status:"done", reply:"<몇 번 줄을 어떻게 · 숫자>", updatedAt}` (`if_version`).
- 판정('통과 (쇼츠로)')은 사용자가 판에서 — 채팅으로 "○편 통과/쇼츠로 넘겨"라고 하면 그때만 `verdicts/<key>` 에 `{key, ver, verdict:"pass", updatedAt, by:"채팅 — …"}`.

## 4. 끝

- 새 피드백이 규칙이 될 만하면 `quick_board.md` 4번 규칙에 한 줄 (원문 인용).
- `CHANGELOG.md`·`guides/status.md` 맨 위 한 줄 → 커밋 → `git pull --rebase origin main` → `git push origin HEAD:main` (부딪히면 양쪽 줄 모두 남김).
- 사용자에게: 판 주소 · 새 대본·고친 줄 · "통과한 대본의 쇼츠는 쇼츠 평가판 세션에서 '쇼츠 평가판 만들어'".
- 오디오는 대본이 main 에 있어야 (Kaggle 셀) — 영상 과정은 `quick_board.md` 6번 (이 세션 일이 아님).

### 읽지 않는 것
`guides/status.md` 전체 · `analysis.md` · 주제·쇼츠 판 HTML · 다른 편 대본(본보기 하나 말고) · `board_1_topic.md`·`board_3_shorts.md`.
