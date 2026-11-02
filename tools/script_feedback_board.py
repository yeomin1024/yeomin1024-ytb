#!/usr/bin/env python3
# VERSION: v1.0 — 2026-11-02 — 주식 1~4편 롱폼·쇼츠 대본을 피드백판(stock/topics/대본피드백판.html)의 SCRIPTS 칸에 채움
#   (사용자 지시 2026-11-02 "그 1~4편 롱폼, 쇼츠 각각 대본 별로 피드백 남길 수 있도록 아티팩트로 만들어볼래? 대본의 여러 줄을 선택해서 각각 피드백 달 수 있도록").
#   · 롱폼 = stock/topics/롱폼대본_2026-10-31.md 표의 제목·대본 파일 → 파일의 '-○○' 줄은 장 이름, 나머지 빈 줄 아닌 줄 = 문장 (번호 = 오디오·자막 문장 번호와 같음)
#   · 쇼츠 = stock/topics/쇼츠안_2026-10-30.md 의 '## N편 — 제목' 아래 표 (# · 역할 · 대본)
#   · 대본이 바뀌면 이 도구를 다시 돌리고 같은 주소로 다시 올림 — 저장된 피드백(db)은 그대로 (피드백의 ver 칸으로 어느 판에 단 것인지 구분).
#   연구·교육용 도구 — 투자 권유가 아님.
# 사용: python3 tools/script_feedback_board.py [--check]   (--check = 파일을 쓰지 않고 셈만)
import json, re, sys, time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOARD = ROOT / "stock/topics/대본피드백판.html"
LONG_INDEX = ROOT / "stock/topics/롱폼대본_2026-10-31.md"
SHORTS = ROOT / "stock/topics/쇼츠안_2026-10-30.md"
LONG_VER, SHORT_VER = "대본 v8", "쇼츠 v5"
BEGIN, END = "/*SCRIPTS:BEGIN*/", "/*SCRIPTS:END*/"


def log(stage, **kv):
    ts = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    print(f"[{stage}] [{ts}] " + " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) else v}" for k, v in kv.items()))


def longform():
    out = []
    rows = re.findall(r"^\|\s*([1-4])\s*\|\s*([^|]+?)\s*\|\s*`([^`]+\.txt)`", LONG_INDEX.read_text(encoding="utf-8"), re.M)
    if len(rows) != 4:
        log("ERROR", stage="longform_index", found=len(rows), file=str(LONG_INDEX.relative_to(ROOT)), next="표 꼴(| 편 | 제목 | `대본` |)이 바뀌었는지 확인")
        sys.exit(1)
    for ep, title, rel in rows:
        f = ROOT / rel
        sec, lines = None, []
        for raw in f.read_text(encoding="utf-8").splitlines():
            t = raw.strip()
            if not t:
                continue
            if t.startswith("-"):
                sec = t[1:].strip()
                continue
            lines.append({"n": len(lines) + 1, "t": t, "sec": sec})
        out.append({"key": f"e{ep}-long", "ep": int(ep), "kind": "long", "title": title.strip(), "ver": LONG_VER, "file": rel, "lines": lines})
        log("LOAD", script=f"e{ep}-long", file=rel, sentences=len(lines), sections=len({l["sec"] for l in lines}))
    return out


def shorts():
    out, cur = [], None
    for raw in SHORTS.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^##\s*([1-4])편\s*—\s*(.+?)\s*$", raw)
        if m:
            title = re.sub(r"\s*\((Claude )?안\)\s*$", "", m.group(2)).strip()
            cur = {"key": f"e{m.group(1)}-short", "ep": int(m.group(1)), "kind": "short", "title": title, "ver": SHORT_VER,
                   "file": str(SHORTS.relative_to(ROOT)) + f" {m.group(1)}편", "lines": []}
            out.append(cur)
            continue
        if raw.startswith("## "):
            cur = None
            continue
        r = re.match(r"^\|\s*(\d+)\s*\|\s*([^|]*?)\s*\|\s*(.+?)\s*\|\s*$", raw)
        if cur is not None and r:
            cur["lines"].append({"n": int(r.group(1)), "role": r.group(2), "t": r.group(3), "sec": None})
    for s in out:
        nums = [l["n"] for l in s["lines"]]
        if nums != list(range(1, len(nums) + 1)):
            log("WARN", script=s["key"], issue="쇼츠 줄 번호가 1부터 이어지지 않음", nums=str(nums))
        log("LOAD", script=s["key"], file=s["file"], lines=len(s["lines"]))
    if len(out) != 4:
        log("ERROR", stage="shorts", found=len(out), next="'## N편 — 제목' 머리가 4개인지 확인")
        sys.exit(1)
    return out


def main(argv):
    scripts = longform() + shorts()
    scripts.sort(key=lambda s: (s["ep"], s["kind"] != "long"))
    data = json.dumps({"scripts": scripts}, ensure_ascii=False, separators=(",", ":"))
    html = BOARD.read_text(encoding="utf-8")
    a, b = html.find(BEGIN), html.find(END)
    if a < 0 or b < a:
        log("ERROR", stage="inject", file=str(BOARD.relative_to(ROOT)), next="SCRIPTS:BEGIN/END 표시를 되살림")
        sys.exit(1)
    new = html[: a + len(BEGIN)] + data + html[b:]
    log("DATA", scripts=len(scripts), lines=sum(len(s["lines"]) for s in scripts), bytes=len(data.encode("utf-8")))
    if "--check" in argv:
        log("DONE", wrote=False, note="--check")
        return
    BOARD.write_text(new, encoding="utf-8")
    log("DONE", wrote=True, file=str(BOARD.relative_to(ROOT)), changed=new != html)


if __name__ == "__main__":
    main(sys.argv[1:])
