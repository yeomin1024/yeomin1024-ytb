#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0.1 — 2026-10-17 — 앞에 숫자가 붙은 곳은 맞다고 보지 않음 (예: "13년" 이 "2013년" 에 걸림).
# v1.0 — 2026-10-17 — 최초. 주식 쇼츠 대본의 숫자가 모두 그 롱폼 대본에 있는지 검사 (stock/guides/shorts_insights.md 5번 ·
#          guides/shorts_guide.md 4번 3항 '숫자는 그 롱폼에 있는 것만'). 사용자 지시 2026-10-17 "저번에 쇼츠 만들었었으니까 같은 방식으로 영상 당
#          쇼츠 1개씩 만들어봐". 롱폼 숫자는 check_numbers.py 가 results.json 으로 이미 맞춰 봤으므로, 쇼츠는 '롱폼 대본에 같은 글자가 있나'만 본다.
#          숫자 + 단위(%·달러·년·월·번·가지·개·배·만·천·일·주)를 한 덩어리로 찾아, 롱폼 대본 전체에 그대로 있어야 통과. 결과 = shorts/checklist.md.
"""python3 tools/backtest/shorts_numcheck.py stock [영상ID ...]    # 영상ID 를 빼면 <주제>/source/*/shorts/*-shorts.txt 전부 · 하나라도 없으면 끝 코드 1"""
import argparse
import logging
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import srt_tool  # noqa: E402

TOKEN = re.compile(r"\d[\d,.]*\d|\d")
UNIT = re.compile(r"\s?(%|달러|년|월|번|가지|개|배|만|천|일|주)")
log = logging.getLogger("shorts_numcheck")


def tokens(sentence):
    """문장의 숫자 덩어리 → ['92.3%', '500달러', '2001년', ...] (단위가 없으면 숫자만)."""
    out = []
    for m in TOKEN.finditer(sentence):
        u = UNIT.match(sentence, m.end())
        out.append(sentence[m.start():u.end()] if u else m.group())
    return out


def check(topic, vid):
    src = ROOT / topic / "source" / vid
    short_txt = src / "shorts" / f"{vid}-shorts.txt"
    long_txt = src / f"{vid}.txt"
    longs = srt_tool.parse_txt(long_txt)
    rows, bad = [], 0
    for i, s in enumerate(srt_tool.parse_txt(short_txt), 1):
        for t in tokens(s):
            pat = re.compile(r"(?<![\d,.])" + re.escape(t))       # 앞에 숫자가 붙지 않게 ('13년' 이 '2013년' 에 걸리지 않음)
            hit = [n for n, x in enumerate(longs, 1) if pat.search(x)]
            ok = bool(hit)
            bad += not ok
            rows.append(f"| {i} | {s} | `{t}` | {', '.join(f's{n}' for n in hit[:4]) or '—'} | {'✅' if ok else '❌'} |")
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    out = src / "shorts" / "checklist.md"
    out.write_text("\n".join([
        f"# {vid}-shorts 숫자 검사 (`tools/backtest/shorts_numcheck.py` v1.0.1)", "",
        f"- {now} · 쇼츠 대본 `{short_txt.name}` · 롱폼 대본 `{long_txt.name}` ({len(longs)}문장) · 숫자 {len(rows)}개 · 없음 {bad}",
        "- 쇼츠의 숫자 덩어리(숫자 + 단위)가 롱폼 대본에 그대로 있어야 한다 — 롱폼 숫자는 `backtest/check_numbers.py` 가 결과 파일로 맞춰 봤다.", "",
        "| 쇼츠 문장 | 대본 | 숫자 | 롱폼 문장 | 결과 |", "|---:|---|---|---|---|", *rows, ""]), "utf-8")
    log.info(f"video={vid}-shorts sentences={len(srt_tool.parse_txt(short_txt))} numbers={len(rows)} missing={bad} → {out.relative_to(ROOT)}")
    for r in rows:
        if "❌" in r:
            log.warning(f"롱폼에 없음: {r}")
    return bad


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("topic")
    ap.add_argument("ids", nargs="*")
    a = ap.parse_args()
    logging.basicConfig(level=logging.INFO, format="[%(name)s] %(message)s")
    ids = a.ids or sorted(p.parent.parent.name for p in (ROOT / a.topic / "source").glob("*/shorts/*-shorts.txt") if not p.parent.parent.name.startswith("_"))
    bad = sum(check(a.topic, v) for v in ids)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
