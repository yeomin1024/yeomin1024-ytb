# 주식 — 3단계 쇼츠 평가판 세션 (이 세션은 이 판 하나만)

VERSION: v1.1 — 2026-11-12 — 3번 **페르소나 반복 검증**(쇼츠 칸 title --shorts · 쇼츠 대본 이탈·반론 2회차 이상) — 사용자 지시 "제목,썸네일, 대본 만들때 자꾸 페르소나 반복 검증 빼먹는데 빼먹지 말도록 주제별 지시사항 수정해봐".
(v1.0 — 2026-11-03 — 사용자 지시 2026-11-03 "새 세션 3개에서 각각 '지시사항 읽고 주제 평가판, 대본 평가판, 쇼츠 평가판 만들어'라고만 해도 지금처럼 할 수 있게 … 세션당 평가판 하나야".)
※ 연구·교육용 — 투자 권유가 아님.

**사용자가 "지시사항 읽고 쇼츠 평가판 만들어"(또는 "쇼츠 피드백 했어") → 이 파일만 읽고 아래 순서대로.** 이 세션은 쇼츠 대본·쇼츠 칸·`stock/topics/board/shorts_board.json`·`stock/topics/board/shorts_pk.json`·`stock/topics/쇼츠안_2026-10-30.md`·`stock/topics/쇼츠평가판.html` 만 고친다 (롱폼 대본·주제 기획안은 다른 세션).
판 = **https://claude.ai/artifact/Mjfwm81meE2vyHH71UqAt2** (이미 있음 — 늘 같은 주소를 갱신). 대본 판(읽기만) = https://claude.ai/artifact/7UQobTs4TU45V4GCMqWCZz.

## 0. 시작

```bash
git pull --rebase origin main
python3 - <<'E'                                   # 이미 판에 있는 쇼츠
import json; print([(i['key'], i['long_key']) for i in json.load(open('stock/topics/board/shorts_board.json'))['items']])
E
```
- 대본 판: `ArtifactData list verdicts`(url = 대본 판) → **verdict == pass('통과 (쇼츠로)')인데 items 의 long_key 에 없는 key** = 새로 쓸 쇼츠.
- 쇼츠 판: `ArtifactData query feedback where status == new` · `list verdicts` ('통과 (영상으로)' = 영상 과정으로 — `quick_board.md` 6번, 이 세션 일이 아님).

## 1. 할 일

| 상태 | 할 일 |
|---|---|
| 쇼츠 판 새 피드백 | 칸 피드백(`field` = s_title·s_thumb_main·s_thumb_sub) → 그 칸 · 줄 피드백(`lines`) → 쇼츠 대본 → 3번 점검 → 판 → done·reply · 판(v)을 올림 |
| 대본 판 통과 · 쇼츠 없음 | 새 쇼츠 (2번) → 3번 → items 에 한 줄 → 판 |
| 둘 다 없음 | 사용자에게 "대본 판에서 통과한 새 편이 없습니다" 한 줄 |

## 2. 쇼츠 쓰기 — 규칙 = `stock/guides/quick_board.md` 4번 규칙 **19~22** + 2번 표 's_message' 줄 (1편 쇼츠 꼴)

- **'이 ○○' = 짝 롱폼 다섯 항목 가운데 대표 항목 하나** (규칙 22) — 그 항목의 오답을 반전 한 문장 → 시청자 반응(편마다 다른 꼴) → 이유 → 그 항목 해설의 숫자(롱폼 문장 그대로) → 강조 → 속담 → 무엇을 → 결론(욕심을 버리고·대비하며·천천히) → **끝 멘트 「다른 테스트가 궁금하다면 구독하고 채널에서 확인하세요.」** · 50~55초(약 12줄) · 지금 시장을 가정하는 말 ✗(20) · 다른 편 쇼츠와 문장 꼴 겹치지 않게(17·21) · '매수하세요' 같은 권유 꼴 ✗.
- 읽을 것: 짝 롱폼 대본의 그 항목 부분만 · `stock/topics/쇼츠안_2026-10-30.md` 의 쇼츠 하나(본보기 — 2편 v7) · 기획안의 써 둔 쇼츠 칸.
- **1~4편**: 쇼츠안 md 의 그 편 절(표 = 대본, `- 썸네일 문구:`·`- 썸네일 보조 문구:`·`- 점검:` 줄)을 고침 · 판(v) = 도구의 `SHORT_VER`.
- **새 편(B11…)**: 쇼츠 대본 `stock/source/<그 편 폴더>/shorts.txt` (한 줄 한 문장) · 칸은 **`stock/topics/board/shorts_pk.json`**(이 세션 파일 — `{"packages":[{id, s_title, s_thumb_main:[2줄], s_thumb_sub, s_message:"(쇼츠 대본 참고)"}]}`, 기획안의 써 둔 칸에서 시작) → items 에 `{"key":"B11-short","ep":"B11","label":"B11 <주제>","from":"file","file":"<shorts.txt>","fields_from":"stock/topics/board/shorts_pk.json#B11","long_key":"B11-long","ver":"v1"}`.
- 쇼츠 제목: 화면 2줄 안(`title_fit --shorts`) — 사용자가 준 제목은 그대로 두고 점검 칸에만 적음. 썸네일 문구가 비면 Claude 안을 먼저 채움("너가 일단 만들어봐").

## 3. 점검 → 판 → 답

```bash
python3 tools/board_check.py script stock <쇼츠.txt> --kind short --calc <짝 롱폼 계산 json> --allow "<사용자 문장 일부>"  # ❌ 0 (끝 멘트·숫자 대조)
python3 tools/board_check.py package stock stock/topics/board/shorts_pk.json --stage shorts --write                         # 새 편 칸
python3 tools/script_feedback_board.py --only short          # 쇼츠평가판.html 만 (대본 판은 건드리지 않음)
# ★ 판에 올리기 전 페르소나 반복 검증 (빠뜨리지 않음 — guides/persona_loop.md): 쇼츠 칸 title --shorts (항목 <id>-shorts) · 쇼츠 대본 script_exit·script_rebuttal (기록 = 쇼츠 대본 폴더 persona_loop.json) — 각 2회차 이상
```
- 1~4편 쇼츠 대본을 점검할 땐 md 표를 파일로 뽑아서: `python3 -c "import sys;sys.argv=['x'];sys.path.insert(0,'tools');import script_feedback_board as M;e,_=M.shorts_md();open('<scratchpad>/eN.txt','w').write('\n'.join(l['t'] for l in e[N]['lines']))"`.
- 판 올리기: 다른 세션에서 처음 올릴 땐 `Artifact action=read url=<판>` 한 번 → `Artifact publish file_path=stock/topics/쇼츠평가판.html url=<판>`.
- 피드백 답: `ArtifactData batch` — `update {status:"done", reply:"<무엇을 어떻게>", updatedAt}` (`if_version`).
- 판정('통과 (영상으로)')은 사용자가 판에서 — 채팅 지시가 있을 때만 대신 씀.

## 4. 끝

- 새 피드백이 규칙이 될 만하면 `quick_board.md` 4번 규칙에 한 줄 (원문 인용).
- `CHANGELOG.md`·`guides/status.md` 맨 위 한 줄 → 커밋 → `git pull --rebase origin main` → `git push origin HEAD:main` (부딪히면 양쪽 줄 모두 남김).
- 사용자에게: 판 주소 · 새 쇼츠·고친 줄 · '통과 (영상으로)' 뒤 할 일(오디오는 main 의 대본으로 Kaggle 셀 → 영상, `quick_board.md` 6번).

### 읽지 않는 것
`guides/status.md` 전체 · `analysis.md` · 롱폼 대본 전체(그 항목만) · 주제·대본 판 HTML · `board_1_topic.md`·`board_2_script.md`.
