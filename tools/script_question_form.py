#!/usr/bin/env python3
# VERSION: v1.0 — 2026-11-04 — 주식 1~4편 대본을 질문형 선택 + 바로 정답·해설로 옮기는 한 번용 도구 (quick_board 규칙 25). 사용: python3 tools/script_question_form.py <저장소> <미리보기 폴더> [--write]
#   연구·교육용 — 투자 권유 아님.
# 1~4편 대본: 선택마다 '여기서 당신은 …하시겠습니까? / 아니면 …하시겠습니까?' → '이때는 …것이 옳은 선택입니다.' → 그 선택의 해설을 바로 뒤로.
# 사용자 지시 2026-11-04 "대본을 여기서 첫번째 압니다. 하지말고 여기서 당신은 ~매수하시겠습니까? 아니면 매수하지 않으시겠습니까? 하고
#   이 때는 매수하지 않는 것이 옳은 선택입니다. 이런식으로 정답 말하고 해설 말하는 식으로 옮겨서 고쳐봐 모든 대본 다".
import re, sys, json
from pathlib import Path
ROOT = Path(sys.argv[1]); WRITE = "--write" in sys.argv
END = [("않습니다.", "않으시겠습니까?"), ("합니다.", "하시겠습니까?"), ("둡니다.", "두시겠습니까?"), ("넣습니다.", "넣으시겠습니까?"),
       ("버팁니다.", "버티시겠습니까?"), ("줄입니다.", "줄이시겠습니까?"), ("늘립니다.", "늘리시겠습니까?"), ("삽니다.", "사시겠습니까?"),
       ("기다립니다.", "기다리시겠습니까?"), ("봅니다.", "보시겠습니까?"), ("갑니다.", "가시겠습니까?"), ("멈춥니다.", "멈추시겠습니까?")]
def ask(t):
    for a, b in END:
        if t.endswith(a):
            return t[: -len(a)] + b
    raise SystemExit(f"끝말 바꾸기 없음: {t}")
FIRST = {("ppalli", 1): "이때는 매수하지 않는 것이 옳은 선택입니다."}     # 사용자 예문 그대로 ('이 때' → 맞춤법 '이때')
INTRO_FIX = {"다 고른 뒤에는, 이씨와 같은 생각을 몇 번 했는지만 세어 보시면 됩니다.": "고를 때마다, 이씨와 같은 생각을 했는지 세어 보시면 됩니다."}
ORD = {"첫": 1, "두": 2, "세": 3, "네": 4, "다섯": 5}
out = {}
for k in ("ppalli", "daebi", "signal", "gongpo"):
    p = ROOT / f"stock/source/{k}-test-2026-11/{k}-test-2026-11.txt"
    parts, cur = [], None
    for ln in p.read_text("utf-8").splitlines():
        if ln.startswith("-"):
            cur = [ln[1:].strip(), []]; parts.append(cur)
        elif ln.strip():
            cur[1].append(ln.strip())
    P = {name: ss for name, ss in parts}
    ans = P["정답과 해설"]
    heads = [i for i, s in enumerate(ans) if re.match(r"(첫|두|세|네|다섯) 번째 선택의 정답은 [AB]번, ", s)]
    summ = next(i for i, s in enumerate(ans) if re.match(r".씨는 다섯 번 모두 틀린 쪽을 골랐습니다", s))
    assert len(heads) == 5 and heads[0] == 2 and summ > heads[-1], (k, heads, summ)
    new = []
    for name, ss in parts:
        if name == "도입":
            new.append((name, [INTRO_FIX.get(s, s) for s in ss]))
        elif name.startswith("선택 "):
            n = int(name.split()[1])
            qi = next(i for i, s in enumerate(ss) if re.match(r"여기서 .+ 번째 선택입니다", s))
            a = re.match(r"A번, (.+)", ss[qi + 1]).group(1); b = re.match(r"B번, (.+)", ss[qi + 2]).group(1)
            assert qi + 3 == len(ss), (k, n, ss[qi:])
            h = heads[n - 1]; e = heads[n] if n < 5 else summ
            m = re.match(r"(?:첫|두|세|네|다섯) 번째 선택의 정답은 ([AB])번, (.+)것입니다\.$", ans[h])
            assert m, ans[h]
            right = FIRST.get((k, n)) or f"이때는 {m.group(2)}것이 옳은 선택입니다."
            new.append((name, ss[:qi] + [f"여기서 당신은 {ask(a)}", f"아니면 {ask(b)}", right] + ans[h + 1: e]))
        elif name == "정답과 해설":
            continue
        elif name == "결과":
            new.append((name, ans[summ:] + ss))
        else:
            new.append((name, ss))
    txt = "\n\n".join("-" + name + "\n" + "\n".join(ss) for name, ss in new) + "\n"
    old_n = sum(len(ss) for _, ss in parts); new_n = sum(len(ss) for _, ss in new)
    long = [(s, len(s)) for _, ss in new for s in ss if len(s) > 50 and ("시겠습니까" in s or "옳은 선택" in s)]
    out[k] = {"old": old_n, "new": new_n, "long_new_lines": long}
    if WRITE:
        p.write_text(txt, "utf-8")
    else:
        Path(sys.argv[2], f"{k}.txt").write_text(txt, "utf-8")
print(json.dumps(out, ensure_ascii=False, indent=1))
