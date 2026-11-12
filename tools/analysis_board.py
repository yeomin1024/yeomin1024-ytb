#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-11-12 — 심리(psychology)·위기(crisis) — 위기는 표준 분석기 전이라 분석 현황에 안내 줄 (사용자 지시 "재테크는 하지 말고 심리, 위기 주제를 그렇게 만들어")
# (v1.0 — 2026-11-12 — 새로: 주제별 분석 판 (<주제>/boards/분석판.html) — 시청자 페르소나(live.json)·업데이트 내역·대본 받기 개수와 PC 명령·고정 채널
#   사용자 지시 2026-11-12 "탐색할 고정 채널을 아이디를 내가 넣을 수 있도록 주제별 아티팩트 만들기 - 다운 받아야 하는 적당한 대본 개수 설정해서 아티팩트에 명령 표시
#   … 시청자 페르소나들 만들어서 내용 아티팩트에 올린다 … 페르소나 업데이트 시 아티팩트에 어떤 근거로 어떻게 업데이트 했는지 짧막하게 내역 남기기".
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.1 | 2026-11-12 | 심리·위기 이름 · 표준 분석기 전 주제(crisis) 안내 줄 · 주제마다 고지 줄(NOTES) | build_data |
# | v1.0 | 2026-11-12 | 최초 | build_data·render·main |
#
# 읽는 것 (쓰지 않음): <주제>/result/persona/live.json (tools/persona_live.py) · <주제>/result/outliers/transcript_todo.json (tools/pc_transcribe.py list)
#   · <주제>/targets.json (tools/cloud_run.py add) · <주제>/result/outliers/analysis.json · personas.json(만든 때) · result/trend/trend_<날짜>.json(영상 제목·시장) · result/persona/news_*.json
# 쓰는 것: <주제>/boards/분석판.html (틀 tools/templates/analysis_board.html — 판 데이터는 /*BOARD:BEGIN*/…/*BOARD:END*/ 사이 JSON)
# 판 주소: <주제>/boards/urls.json {"analysis": "https://claude.ai/artifact/…"} — 처음 올린 뒤 Claude 가 적음. 같은 주소로 다시 올리면 db(channels)는 그대로.
# 쓰기: python3 tools/analysis_board.py <주제> [--check]     (--check = 파일을 쓰지 않고 셈만)
#       python3 tools/analysis_board.py --selftest
# ※ 연구·교육용 — 투자 권유 아님.
from __future__ import annotations

import argparse
import json
import logging
import re
import sys
import tempfile
import time
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = "v1.1"
TPL = ROOT / "tools" / "templates" / "analysis_board.html"
BEGIN, END = "/*BOARD:BEGIN*/", "/*BOARD:END*/"
NAMES = {"stock": "주식", "history": "역사", "psychology": "심리", "crisis": "위기", "economic": "재테크", "music": "음악", "test": "시험"}
NOTES = {"stock": "연구·교육용이며 투자 권유가 아닙니다.", "history": "사실은 사료·연구로 확인합니다.",
         "psychology": "연구·교육용이며 의료·심리 상담이 아닙니다.", "crisis": "안전 수칙은 공식 지침(소방청·경찰청·국민재난안전포털)으로 확인합니다."}
LOG_ROWS = 60
LOG = logging.getLogger("analysis_board")


def log(stage: str, level: int = logging.INFO, **kv) -> None:
    ts = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    LOG.log(level, f"[{stage}] [{ts}] " + " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) else v}" for k, v in kv.items()))


def read_json(p: Path, default=None):
    try:
        return json.loads(p.read_text("utf-8"))
    except (OSError, ValueError):
        return default


def build_data(root: Path, topic: str, today: str | None = None) -> dict:
    today = today or date.today().isoformat()
    name = NAMES.get(topic, topic)
    live = read_json(root / topic / "result" / "persona" / "live.json")
    if not live:
        log("LOAD", logging.WARNING, topic=topic, live="없음", next=f"python3 tools/persona_live.py init {topic}")
        live = {"personas": [], "log": [], "updated": ""}
    od = root / topic / "result" / "outliers"
    a = read_json(od / "analysis.json", {}) or {}
    pj = read_json(od / "personas.json", {}) or {}
    tr = read_json(od / "transcript_todo.json", {}) or {}
    tg = read_json(root / topic / "targets.json", {}) or {}
    pname = {p["key"]: p["name"] for p in live.get("personas", [])}
    # 근거 칸에 보일 이름 — 영상 제목·뉴스 제목·시장 한 줄 (근거로 쓴 것만)
    used = {s for p in live.get("personas", []) for f in ("situation", "habit", "curiosity", "worry", "anxiety", "wants")
            for it in ((([p[f]] if p.get(f) else []) if f in ("situation", "habit") else (p.get(f) or []))) for s in it.get("src") or []}
    used |= {s for x in live.get("log", [])[:LOG_ROWS] for s in x.get("src") or []}
    videos, market, news = {}, {}, {}
    trend = sorted((root / topic / "result" / "trend").glob("trend_*.json"), reverse=True)
    for p in trend[:3]:
        t = read_json(p, {}) or {}
        for k in ("top_long", "top_small", "fresh", "top_short"):
            for v in t.get(k) or []:
                if f"v:{v['id']}" in used:
                    videos.setdefault(v["id"], v.get("title", "")[:80])
        for m in t.get("market") or []:
            if f"m:{m['name']}" in used:
                market.setdefault(m["name"], f"{m.get('date')} 종가 {m.get('close')} · 1년 최고가 대비 {m.get('from_high')}% · 5일 {m.get('d5')}%")
    nfiles = sorted((root / topic / "result" / "persona").glob("news_*.json"), reverse=True)
    for p in nfiles[:10]:
        for n in read_json(p, []) or []:
            if f"n:{n.get('url')}" in used:
                news.setdefault(n["url"], {"title": n.get("title", ""), "source": n.get("source", ""), "date": n.get("date", "")})
    personas = []
    for p in live.get("personas", []):
        personas.append({k: p.get(k) for k in ("key", "name", "n", "who", "situation", "habit", "curiosity", "worry", "anxiety", "wants", "quotes")})
    logs = [{**x, "persona_name": pname.get(x.get("persona"), "전체" if x.get("persona") == "*" else x.get("persona"))} for x in live.get("log", [])[:LOG_ROWS]]
    D = {"tool": f"analysis_board.py {VERSION}", "topic": topic, "name": name, "title": f"{name} 분석 판", "note": NOTES.get(topic, "연구·교육용입니다."), "made": datetime.now().strftime("%Y-%m-%d %H:%M"),
         "today": today, "updated": live.get("updated", ""), "stale_days": 14, "personas": personas, "log": logs,
         "videos": videos, "market": market, "news": news,
         "targets": [{"id": c["id"], "title": c.get("title", ""), "videos": c.get("videos"), "added": c.get("added", "")} for c in tg.get("channels") or []],
         "transcript": {k: tr.get(k) for k in ("n", "why", "command", "first", "made", "first_pass_audio_min", "by_group")} if tr else {},
         "analysis": {"generated": str(a.get("generated", ""))[:10], "success": len(a.get("success_cases") or []),
                      "vpd": len((a.get("vpd_top") or {}).get("cases") or []), "views": len((a.get("views_top") or {}).get("cases") or []),
                      "personas_made": str(pj.get("made", "") or str(live.get("source_personas", "")).rsplit("(", 1)[-1].rstrip(")"))[:10],
                      "note": "" if a else f"표준 분석기 전 — 자체 분석 결과({topic}/result/analysis.md)를 씀. 대본 받기·고정 채널 탐색은 표준 분석기로 옮긴 뒤 (guides/flow.md 1-0)"},
         "trend_date": trend[0].stem[6:] if trend else "", "news_date": nfiles[0].stem[5:] if nfiles else ""}
    return D


def render(D: dict, tpl: str) -> str:
    if BEGIN not in tpl or END not in tpl or "{{TITLE}}" not in tpl:
        raise SystemExit("[ERROR] 틀에 자리표가 없음 — tools/templates/analysis_board.html 의 {{TITLE}}·BOARD 칸")
    js = json.dumps(D, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
    head, rest = tpl.split(BEGIN, 1)
    _, tail = rest.split(END, 1)
    return (head + BEGIN + js + END + tail).replace("{{TITLE}}", D["title"])


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="주제별 분석 판 만들기 (<주제>/boards/분석판.html)")
    ap.add_argument("topic", nargs="?"); ap.add_argument("--check", action="store_true"); ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args(argv)
    logging.basicConfig(level=getattr(logging, a.log_level), format="%(message)s", stream=sys.stdout)
    if a.selftest:
        return selftest()
    if not a.topic or not re.match(r"^[a-z][a-z0-9_-]{1,30}$", a.topic) or not (ROOT / a.topic).is_dir():
        ap.error("주제 폴더를 주세요 — 예: stock · economic · history")
    t0 = time.perf_counter()
    D = build_data(ROOT, a.topic)
    page = render(D, TPL.read_text("utf-8"))
    out = ROOT / a.topic / "boards" / "분석판.html"
    old = out.read_text("utf-8") if out.exists() else ""
    log("DATA", topic=a.topic, personas=len(D["personas"]), filled=sum(1 for p in D["personas"] for f in ("situation", "curiosity", "worry", "anxiety", "wants") if p.get(f)),
        log_rows=len(D["log"]), targets=len(D["targets"]), transcript_n=D["transcript"].get("n", "-"), updated=D["updated"] or "-",
        trend=D["trend_date"] or "-", news=D["news_date"] or "-", bytes=len(page.encode("utf-8")))
    if not a.check:
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page, "utf-8")
    urls = read_json(out.parent / "urls.json", {}) or {}
    log("DONE", topic=a.topic, wrote=not a.check, file=str(out.relative_to(ROOT)), changed=page != old, url=urls.get("analysis") or "(아직 안 올림 — 처음 올린 뒤 boards/urls.json)",
        seconds=round(time.perf_counter() - t0, 2))
    return 0


def selftest() -> int:
    ok = True

    def chk(name, cond):
        nonlocal ok
        ok &= bool(cond)
        print(("✅ " if cond else "❌ ") + name)

    with tempfile.TemporaryDirectory() as d:
        R = Path(d)
        (R / "demo/result/persona").mkdir(parents=True)
        (R / "demo/result/outliers").mkdir(parents=True)
        (R / "demo/result/persona/live.json").write_text(json.dumps({"updated": "2026-11-12", "personas": [
            {"key": "w", "name": "직장인", "who": "40대", "situation": {"text": "</script><b>x", "date": "2026-11-12", "src": ["m:코스피"], "basis": "b"},
             "worry": [], "curiosity": [], "anxiety": [], "wants": [], "quotes": []}],
            "log": [{"date": "2026-11-12", "persona": "w", "field": "situation", "op": "set", "before": "", "after": "a", "basis": "b", "src": ["m:코스피"]}]}, ensure_ascii=False), "utf-8")
        (R / "demo/result/outliers/transcript_todo.json").write_text(json.dumps({"n": 12, "command": "powershell … --limit 12", "why": "w"}), "utf-8")
        D = build_data(R, "demo", "2026-11-12")
        chk("데이터: 페르소나 1·내역 1·대본 12", len(D["personas"]) == 1 and len(D["log"]) == 1 and D["transcript"]["n"] == 12)
        page = render(D, TPL.read_text("utf-8"))
        chk("판: 제목 채움", "<title>demo 분석 판</title>" in page)
        body = page.split(BEGIN, 1)[1].split(END, 1)[0]
        chk("판: 데이터 안 </script> 막음", "</script>" not in body and "<\\/script>" in body)
        chk("판: db 채널 칸", 'collection("channels")' in page)
    print("[SELFTEST] " + ("✅ 모두 통과" if ok else "❌ 실패 있음"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
