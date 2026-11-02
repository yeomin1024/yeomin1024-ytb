#!/usr/bin/env python3
# VERSION: v1.1 — 2026-11-02 — 주제 평가판은 롱폼 칸만 (쇼츠 칸 s_*·check_shorts 는 판 데이터에서 뺌 — 쇼츠는 3단계 쇼츠 평가판에서,
#   사용자 지시 2026-11-02 "주제 탐색 평가판 -> 대본 평가판 -> 쇼츠 평가판 이렇게 3단계로 나누자").
# (v1.0 — 2026-11-02 — 주식 주제 평가판(stock/topics/주제평가판.html)의 TOPICS 칸을 기획안 묶음(stock/topics/board/topics_*.json)에서 채움
#   (사용자 지시 2026-11-02 "주제 탐색(…)도 평가 아티팩트 만들고 통과된것만 대본 평가 아티팩트로 넘겨" · "처음 평가판에 올라가기 전에는 일반, 반론 페르소나로 점검은 거쳐야해").
#   · 점검(tools/board_check.py package … --write)을 안 거쳤거나 ❌ 가 남은 기획안은 판에 올리지 않음 (로그에 남김).
#   · 판에서 사용자가 고른 판정·피드백은 아티팩트 db(verdicts·feedback) — Claude 가 ArtifactData 로 읽음 (stock/guides/quick_board.md).
#   연구·교육용 도구 — 투자 권유가 아님.
# 사용: python3 tools/topic_board.py [--check]
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOARD = ROOT / "stock/topics/주제평가판.html"
SRC = ROOT / "stock/topics/board"
BEGIN, END = "/*TOPICS:BEGIN*/", "/*TOPICS:END*/"


def log(stage, **kv):
    ts = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    print(f"[{stage}] [{ts}] " + " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) else v}" for k, v in kv.items()))


def main(argv):
    batches, skipped = [], []
    for f in sorted(SRC.glob("topics_*.json")):
        D = json.loads(f.read_text("utf-8"))
        ok = []
        for pk in D["packages"]:
            ck = pk.get("check") or {}
            if not ck.get("pass"):
                skipped.append((f.name, pk.get("id"), "점검 안 함" if not ck else "점검 ❌"))
                continue
            ok.append({k: v for k, v in pk.items() if not (k.startswith("s_") or k == "check_shorts")})
        name = "묶음 " + f.stem.replace("topics_", "")
        batches.append({"name": name, "file": str(f.relative_to(ROOT)), "packages": ok})
        log("LOAD", file=str(f.relative_to(ROOT)), packages=len(D["packages"]), on_board=len(ok))
    for s in skipped:
        log("SKIP", file=s[0], id=s[1], why=s[2], next="python3 tools/board_check.py package stock <파일> --write 로 고친 뒤 다시")
    data = json.dumps({"batches": batches}, ensure_ascii=False, separators=(",", ":"))
    html = BOARD.read_text("utf-8")
    a, b = html.find(BEGIN), html.find(END)
    if a < 0 or b < a:
        log("ERROR", file=str(BOARD.relative_to(ROOT)), next="TOPICS:BEGIN/END 표시를 되살림")
        return 1
    new = html[: a + len(BEGIN)] + data + html[b:]
    log("DATA", batches=len(batches), topics=sum(len(x["packages"]) for x in batches), skipped=len(skipped), bytes=len(data.encode()))
    if "--check" not in argv:
        BOARD.write_text(new, "utf-8")
    log("DONE", wrote="--check" not in argv, changed=new != html)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
