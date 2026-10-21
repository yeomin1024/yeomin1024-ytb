#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-21 — 새로: 개미 재기 일지 제작안(.txt) → 장면 시각 추정·오디오용 대본 뽑기·story_check 검사.
#          사용자 지시 2026-10-21 "아래 주제들로 일본 축제 영상 대본 내용 만들 때 처럼 한 파일에 대본 내용, 제목 등 종합해서 넣어 …
#          그리고 시리즈물이라는 것도 고려해". 제작안이 원본이다 — 사람이 고치면 이 도구를 다시 돌려 시각·검사를 맞춘다.
#          추정 = 읽는 음절 ÷ 6.3(H17 샘플) + 문장 사이 0.45초 · 파트가 바뀌면 1.0초 · 정리 카드 = srt_tool.parse_cards 와 같은 길이.
#          오디오가 오면 실제 시각으로 다시 맞춘다 (render.mjs sync). ※ 연구·교육용 — 투자 권유가 아니다.
"""
  python3 stock/story/calc/plan_tool.py stock/story/<제작안>.txt [--script-out <대본.txt>] [--write]
    --write       제작안의 장면 시각·길이 줄을 추정값으로 고쳐 씀
    --script-out  오디오용 대본(-도입 … [장면] 정리 …)을 그 경로에 씀 (승인 뒤 stock/source/<영상ID>/<영상ID>.txt)
끝 코드: story_check 문제가 있으면 1.
"""
import argparse
import logging
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
import srt_tool  # noqa: E402
import story_check  # noqa: E402

VERSION = "v1.0"
SYL, GAP, PART_GAP = story_check.HOST_SYL_PER_SEC, story_check.SENT_GAP, 1.0
PART_RE = re.compile(r"^=+ (\S+)(?: · .*)? =+$")
SCENE_RE = re.compile(r"^\[([A-Z]-\d+[a-z]?) \| ([^|]*) \| (.*)\]$")


def mmss(t):
    return f"{int(t // 60)}:{int(round(t % 60)):02d}" if round(t % 60) < 60 else f"{int(t // 60) + 1}:00"


def parse(lines):
    """→ (scenes, title_r1). scene = dict(i=줄 번호, id, part, sentences, card)."""
    scenes, part, cur, mode, in_body, title = [], None, None, None, False, None
    for i, raw in enumerate(lines):
        line = raw.rstrip("\n")
        s = line.strip()
        if title is None and re.match(r"^R1\. ", s):
            title = s[4:].split("  (")[0].strip()
        if s.startswith("■ 대본 + 화면 구성"):
            in_body = True
            continue
        if in_body and (s.startswith("■ ") or s.startswith("####")):
            in_body = False
        if not in_body:
            continue
        m = PART_RE.match(s)
        if m:
            part, cur, mode = m.group(1), None, None
            continue
        m = SCENE_RE.match(s)
        if m:
            cur = dict(i=i, id=m.group(1), part=part, sentences=[], card=[])
            scenes.append(cur)
            mode = None
            continue
        if cur is None:
            continue
        if s.startswith("(내레이션)"):
            mode = "nar"
            continue
        if s.startswith("(정리 카드"):
            mode = "card"
            continue
        if s.startswith("(화면)") or s.startswith("(무대)"):
            mode = None
            continue
        if not s:
            mode = None if mode == "card" else mode
            if mode == "nar":
                mode = None
            continue
        if mode == "nar":
            cur["sentences"].append(s)
        elif mode == "card":
            cur["card"].append(s)
    return scenes, title


def script_text(scenes):
    out, part = [], None
    for sc in scenes:
        if sc["part"] != part:
            part = sc["part"]
            out.append(f"-{part}")
        out += sc["sentences"]
        if sc["card"]:
            out.append("[장면] 정리")
            out += sc["card"]
    return "\n".join(out) + "\n"


def timing(scenes):
    t, part, first = 0.0, None, True
    for sc in scenes:
        start = t
        for k, s in enumerate(sc["sentences"]):
            if not first:
                t += PART_GAP if (k == 0 and sc["part"] != part) else GAP
            first = False
            t += srt_tool.syllables(s) / SYL
        part = sc["part"]
        if sc["card"]:
            chars = len("".join(sc["card"]).replace(" ", ""))
            t += round(min(8.0, max(4.0, chars / 7 + 1)), 3)
        sc["t0"], sc["t1"] = start, t
    return t


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("plan")
    ap.add_argument("--script-out")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args(argv)
    logging.basicConfig(level=logging.WARNING, format="%(message)s")
    path = Path(a.plan)
    lines = path.read_text("utf-8").split("\n")
    scenes, title = parse(lines)
    total = timing(scenes)
    sents = [s for sc in scenes for s in sc["sentences"]]
    syl = sum(srt_tool.syllables(s) for s in sents)
    by_part = {}
    for sc in scenes:
        p = by_part.setdefault(sc["part"], dict(n=0, syl=0, t0=sc["t0"], t1=sc["t1"]))
        p["n"] += len(sc["sentences"])
        p["syl"] += sum(srt_tool.syllables(s) for s in sc["sentences"])
        p["t1"] = sc["t1"]
    print(f"[PLAN] file={path.name} version={VERSION} scenes={len(scenes)} sentences={len(sents)} syllables={syl} est={mmss(total)} title={title!r}")
    for k, v in by_part.items():
        print(f"[PART] {k}: sentences={v['n']} syllables={v['syl']} {mmss(v['t0'])}~{mmss(v['t1'])}")
    if a.write:
        for sc in scenes:
            m = SCENE_RE.match(lines[sc["i"]].strip())
            lines[sc["i"]] = f"[{sc['id']} | {mmss(sc['t0'])}~{mmss(sc['t1'])} | {m.group(3)}]"
        lines = [re.sub(r"^\[1\] 롱폼 \(.*\)$", f"[1] 롱폼 (추정 {mmss(total)} — 문장 {len(sents)}개 · 읽는 음절 {syl} · plan_tool {VERSION})", l) for l in lines]
        path.write_text("\n".join(lines), "utf-8")
        print(f"[WRITE] {path}")
    text = script_text(scenes)
    if a.script_out:
        Path(a.script_out).write_text(text, "utf-8")
        print(f"[SCRIPT] {a.script_out}")
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "s.txt"
        p.write_text(text, "utf-8")
        probs, warns, info = story_check.check(p, title)
    for x in probs:
        print(f"❌ {x}")
    for x in warns:
        print(f"⚠️ {x}")
    for x in info:
        print(f"ℹ️ {x}")
    print(f"[CHECK] problems={len(probs)} warnings={len(warns)}")
    return 1 if probs else 0


if __name__ == "__main__":
    sys.exit(main())
