# 페르소나 반복 검증 — 제목·썸네일·대본 (모든 주제 공통 · 빠뜨리지 않음)

VERSION: v1.1 — 2026-11-13 — 주제별 통과 기준 `<주제>/persona_gate.json` (`tools/persona_gate.py` v1.1 · 지금 `crisis/` 만: 반론 중 ≤ 3, 회차 10까지 — 사용자 지시 2026-11-13 "엘리베이터는 P4로 바꾸고 반론은 중 3 이하로 해"). 기준이 바뀌면 `rejudge`.
이전 v1.0 — 2026-11-12 — 사용자 지시 "제목,썸네일, 대본 만들때 자꾸 페르소나 반복 검증 빼먹는데 빼먹지 말도록 주제별 지시사항 수정해봐".
※ 연구·교육용 — 투자·세무 상담이 아님.

**제목·썸네일 문구·보조 문구를 새로 쓰거나 바꿀 때, 대본(롱폼·쇼츠)을 새로 쓰거나 한 줄이라도 바꿀 때 — 아래 반복 검증을 끝내기 전에는 평가판·대본 판·업로드 시트·사용자에게 '완성'으로 내놓지 않는다.**
규칙 점검(`tools/board_check.py`)은 페르소나 검증이 아니다 — 둘 다 한다. 기록은 `tools/persona_gate.py` 로만 남기고, `board_check.py` v1.11 이 그 기록을 읽어 없거나 오래되면 ❌.

## 1. 세 단계 (주제마다 같음)

| 단계 | 무엇을 | 누가 (회차마다 **새** 하위 에이전트 — 같은 이름 다시 ✗) | 통과 (마지막 회차) |
|---|---|---|---|
| `title` 제목·썸네일 피드 시험 | 제목 + 썸네일 주요 문구 + 보조 문구 (쇼츠는 쇼츠 칸) | 대상 페르소나 1 + 반론 페르소나 1 | 둘 다: 실제 영상 제목 9개 사이에 섞인 홈 화면에서 **누름** · 제목+썸네일을 보고도 누름 · '낚시' 아님 |
| `script_exit` 대본 이탈 | 대본 전체 (줄 번호) | 그 편 대상 페르소나 1 (`[페르소나]` 칸 · 기획안 `persona`) | 끄고 싶은 줄 0 · 풀이 없이 모르는 말 0 · 끝까지 봄 |
| `script_rebuttal` 대본 반론 | 대본 전체 | 반론 페르소나 1 (`<주제>/result/outliers/rebuttal_persona.md` K1~K8 — 없으면 일반 반론 시청자) | 상 0 · 중 ≤ 1 (주제 파일 `<주제>/persona_gate.json` 이 있으면 그 값 — crisis 중 ≤ 3) · 옳은 선택(결론)이 분명 |

- **2회차 이상** — 1회차가 통과여도 새 검토자로 한 번 더 (한 사람의 운 막기). 지적을 고쳤으면 고친 글로 다음 회차.
- **마지막 회차가 본 글 = 지금 글** — 회차 뒤에 한 글자라도 고치면(대본 줄·제목·썸네일 문구) 그 단계는 다시 ❌ → 새 회차. (주석 `#` 줄·빈 줄은 상관없음.)
- 페르소나 = 그 주제 분석 결과만 (`<주제>/result/outliers/personas.json`·`rebuttal_persona.md`). 다른 주제 페르소나를 빌리지 않는다.

## 2. 명령 (한 회차)

```bash
# 기록 파일: 편 = <편 폴더>/persona_loop.json (항목 = 영상ID — 쇼츠는 <쇼츠 폴더>/persona_loop.json · 항목 = 쇼츠 대본 이름)
#            기획안 묶음 = <topics_날짜>.persona.json (항목 = 기획안 id · 쇼츠 칸은 <id>-shorts)
python3 tools/persona_gate.py prompt <주제> title <기록> <항목> --plan <편 폴더>/package.json --out <지시문.md>              # 기획안 묶음이면 --plan <topics.json>#<id> · 쇼츠 칸 --shorts
python3 tools/persona_gate.py prompt <주제> script_exit <기록> <항목> --script <대본.txt> --persona P3 --out <지시문.md>
python3 tools/persona_gate.py prompt <주제> script_rebuttal <기록> <항목> --script <대본.txt> --out <지시문.md>
#   → Agent(general-purpose, 새로) 에게 "<지시문.md> 를 읽고 그대로 하라"만 준다 (다른 회차 결과·Claude 의 생각을 넣지 않음). 답 JSON 은 지시문이 정한 자리에.
python3 tools/persona_gate.py add <기록> <항목> <단계> <답1.json> [<답2.json>] --fixed "<이 회차 뒤 고친 것>"
python3 tools/persona_gate.py check <기록> <항목> --script <대본.txt> --plan <package.json>     # 단계마다 ✅ 까지
python3 tools/persona_gate.py status <기록>                                                      # 회차 표 (사용자에게 보여 줄 때)
python3 tools/persona_gate.py rejudge <기록>                                                     # 주제 기준이 바뀐 뒤 지난 회차를 다시 셈 (옛 판정 pass_before)
```
- 여러 편을 함께 하면 편마다 검토자를 따로, 한 메시지에 나란히 띄운다 (병렬).
- 지시문에는 실제 영상 제목(그 주제 `compare.csv` 최근 90일 한국어 제목)이 섞여 있어 검토자는 어느 것이 우리 것인지 모른다 — 지시문을 고쳐 우리 것을 알려 주지 않는다.

## 3. 편 기획 칸 `package.json` (편 폴더 — 제목·썸네일의 한 곳)

`{"id","persona","title","thumb_main":[2줄],"thumb_sub","s_title","s_thumb_main","s_thumb_sub"}` — 기획안에서 옮겨 와 편에서 고치는 곳. 업로드 시트 1번 제목 = 이 `title` (다르면 `board_check.py script … --upload` ❌). 썸네일 JSON 문구도 이 칸과 같게.

## 4. 멈출 때

- 단계마다 **5회차**(주제 파일 `max_rounds` 가 있으면 그 값)에도 통과 못 하면 멈추고, 남은 지적을 그대로(회차 표 `status`) 사용자에게 알리고 사용자가 정한다 — 통과로 적지 않는다.
- 사용자가 직접 준 문구(제목·문장)는 바꾸지 않는다 — 검증은 하고, 걸리면 '사용자 문구라 그대로 · 지적: …'으로 알린다.

## 5. 끝에 사용자에게

편마다 한 줄: `제목 n회차 ✅ · 이탈 n회차 ✅ · 반론 n회차 ✅ (상 0 · 중 m)` + 회차마다 고친 것 한 줄씩 (`status` 표).
