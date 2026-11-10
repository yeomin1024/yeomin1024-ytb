#!/usr/bin/env python3
# VERSION: v1.0 — 2026-11-10 — 대본 요약 평가판 (사용자 지시 2026-11-10 "반등 대본과 만스피 대본 요약 평가판 만들어서 2개만 올려봐
#          요약 평가판은 각 부분의 시작, 다음으로 넘어가는 멘트, 내용의 흐름만 표시하면 돼").
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.0 | 2026-11-10 | 최초 | parse · build · main |
#
# 원본 stock/topics/board/summary_board.json (items: key·label·title·ver·file·flow{장 이름: [흐름 줄]}) + 대본 파일
#   → 장마다 시작 = 첫 문장 · 넘어가는 멘트 = 마지막 문장 (대본 그대로) · 흐름 = 원본의 Claude 요약 · 문장 번호(대본 평가판과 같음 — '-' 장 줄·빈 줄 뺀 차례)
#   → 틀 stock/topics/board/summary_board.template.html 의 /*DATA*/ 자리에 넣어 stock/topics/요약평가판.html.
# 판 주소는 처음 올린 뒤 원본 'url' 칸에 적는다. 피드백은 판 db feedback 모음 (Claude 가 status=new 만 읽고 반영 뒤 done·reply).
# 사용: python3 tools/summary_board.py [--check]   (--check = 파일을 쓰지 않고 장·문장 수와 흐름 빠짐만 셈)
# 연구·교육용 도구 — 투자 권유가 아님.
import json
import logging
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "stock/topics/board/summary_board.json"
TPL = ROOT / "stock/topics/board/summary_board.template.html"
OUT = ROOT / "stock/topics/요약평가판.html"
MARK = "/*DATA*/null/*DATA*/"

logging.basicConfig(level=logging.INFO, format="%(message)s", stream=sys.stdout)


def log(stage: str, **kv) -> None:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    logging.info(f"[{stage}] [{ts}] " + " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) and ' ' in v else v}" for k, v in kv.items()))


def parse(path: Path) -> tuple[list[dict], int]:
    """대본 → 장 목록 [{name, from, to, start, transition}] · 문장 수. 장 줄 = '-' 로 시작."""
    chs, n = [], 0
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("-"):
            chs.append({"name": line[1:].strip(), "lines": []})
            continue
        n += 1
        if not chs:
            chs.append({"name": "(장 없음)", "lines": []})
        chs[-1]["lines"].append((n, line))
    out = []
    for c in chs:
        if not c["lines"]:
            continue
        out.append({"name": c["name"], "from": c["lines"][0][0], "to": c["lines"][-1][0], "start": c["lines"][0][1], "transition": c["lines"][-1][1]})
    return out, n


def build(src: dict) -> dict:
    items = []
    for it in src["items"]:
        path = ROOT / it["file"]
        if not path.exists():
            log("BOARD", level="error", key=it["key"], error="대본 파일 없음", file=it["file"], hint="summary_board.json 의 file 경로 확인")
            sys.exit(1)
        chs, n = parse(path)
        flow = it.get("flow", {})
        for c in chs:
            c["flow"] = flow.get(c["name"], [])
        missing = [c["name"] for c in chs if not c["flow"]]
        extra = [k for k in flow if k not in {c["name"] for c in chs}]
        log("SCRIPT", key=it["key"], ver=it["ver"], chapters=len(chs), sentences=n, flow_missing=",".join(missing) or "-", flow_unused=",".join(extra) or "-")
        if missing or extra:
            log("SCRIPT", level="warning", key=it["key"], hint="대본 장 이름이 바뀌었으면 summary_board.json 의 flow 장 이름도 고침")
        items.append({k: it[k] for k in ("key", "label", "title", "ver", "file")} | {"n": n, "chapters": chs})
    return {"made": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "items": items}


def main() -> None:
    t0 = time.perf_counter()
    check = "--check" in sys.argv
    try:
        src = json.loads(SRC.read_text(encoding="utf-8"))
        tpl = TPL.read_text(encoding="utf-8")
    except (OSError, json.JSONDecodeError) as ex:
        log("LOAD", level="error", error=str(ex), hint="stock/topics/board/summary_board.json · summary_board.template.html 확인")
        sys.exit(1)
    log("LOAD", src=str(SRC.relative_to(ROOT)), items=len(src["items"]))
    data = build(src)
    if check:
        log("DONE", wrote=False, sec=round(time.perf_counter() - t0, 3))
        return
    if MARK not in tpl:
        log("BOARD", level="error", error="틀에 DATA 자리 없음", hint="summary_board.template.html 의 /*DATA*/null/*DATA*/")
        sys.exit(1)
    html = tpl.replace(MARK, json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
    OUT.write_text(html, encoding="utf-8")
    log("DONE", wrote=True, out=str(OUT.relative_to(ROOT)), bytes=len(html.encode("utf-8")), sec=round(time.perf_counter() - t0, 3))


if __name__ == "__main__":
    main()
