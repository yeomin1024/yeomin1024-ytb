#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-11-24 — 신규: 심리 성공 사례 썸네일 문구 갈래 세기 (주요 문구·보조 문구)
#   사용자 지시 2026-11-24 "실험형 썸네일 문구 성공 사례 분석해서 한거야? 분석해서 만들고 이유를 아니까를 진작에 할걸(예시) 이런식으로 고쳐봐".
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.0 | 2026-11-24 | 최초 — 주요 문구 9갈래 · 보조 문구 4갈래 · 갈래마다 장 수·몫·구독자 배수 가운데값·예시 | classify · main |
"""psychology/result/outliers/thumb_codes.tsv(성공 사례 썸네일 — Claude 가 그림을 보고 옮긴 주요·보조 문구) 를
compare.csv(조회수·구독자 배수)와 이어 문구 갈래를 센다 → psychology/result/outliers/thumb_text_patterns.md

한계: 성공 사례만 있음(실패 쪽 썸네일 문구는 분류하지 않았음) → '많이 쓰인 꼴'과 '그 안에서 배수가 큰 꼴'만 말할 수 있고,
'이 꼴이 성공을 만든다'는 말할 수 없다. 갈래는 낱말 규칙(정규식) — 한 문구가 여러 갈래에 들 수 있다. 연구·교육용.
실행: python3 psychology/source/thumb_text_patterns.py
"""
from __future__ import annotations

import csv
import re
import statistics as st
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "psychology" / "result" / "outliers"

MAIN = [   # (갈래, 정규식, 설명)
    ("이유형", r"이유", "'~하는 이유' — 까닭을 알려 준다는 약속"),
    ("특징·비밀형", r"특징|공통점|비밀|심리|신호|습관", "'~하는 사람 특징·심리·비밀'"),
    ("소름·놀람 낱말", r"소름|무서|놀라|충격|치명", "감정을 세게 거는 낱말"),
    ("명령·경고형", r"마세요|마라|하세요|해라|하라|버리세요|하지 마", "'~하지 마세요 / ~하라'"),
    ("질문형", r"\?|까$|까\?", "물음으로 끝남"),
    ("1인칭 고백형", r"(^|[ '\"])(나|내|나는|내가|나를|나만|내 )|요\.{2,}|요…|다$|네\.{2,}|없다|졌다", "'나는 친구가 없다'·'혼자가 편해졌다' — 그 사람 목소리"),
    ("후회·가정형", r"진작|더라면|할걸|했으면|몰랐", "'이 책을 진작 알았더라면…'"),
    ("숫자", r"\d", "가짓수·나이·연도"),
    ("말줄임", r"\.\.|…", "말끝을 흐림"),
]
SUB = [
    ("인물 속마음·대사", r"\.\.|…|!|\?|요$|해$|어$|네$|지$|됐어|만;;", "그림 속 사람이 하는 말·속마음 ('제발 그만 오면 안되나..', '언젠간 쓰겠지..')"),
    ("권위·출처", r"정신과|의사|교수|전문의|정약용|쇼펜하우어|사르트르|니체|대표", "'정신과의사'·'김형석 교수'"),
    ("숫자", r"\d", "'12년'·'65세'·'3일'"),
]


def load():
    try:
        rows = [r for r in csv.reader(open(OUT / "thumb_codes.tsv", encoding="utf-8"), delimiter="\t") if r and not r[0].startswith("#")]
        cmp = {r["id"]: r for r in csv.DictReader(open(OUT / "compare.csv", encoding="utf-8-sig"))}
    except OSError as ex:
        sys.exit(f"[LOAD] 분석 결과를 읽지 못함 ({ex}) — cloud_run.py psychology analyze 먼저")
    hdr, rows = rows[0], rows[1:]
    out = []
    for r in rows:
        d = dict(zip(hdr, r))
        c = cmp.get(d["id"])
        if not c or c.get("success") != "True":          # 지금 성공 사례만
            continue
        d["ratio"] = float(c["ratio"] or 0)
        d["views"] = int(float(c["views"] or 0))
        d["title"] = c["title"]
        out.append(d)
    return out


def table(items, cats, key):
    n = len(items)
    lines = [f"| 갈래 | 장 수 | 몫 | 구독자 배수 가운데값 | 조회수 가운데값 | 예시 (배수) |", "|---|---|---|---|---|---|"]
    base = st.median([i["ratio"] for i in items])
    res = []
    for name, rx, desc in cats:
        hit = [i for i in items if i[key] and re.search(rx, i[key])]
        if not hit:
            lines.append(f"| {name} | 0 | 0% | — | — | — |")
            continue
        med = st.median([i["ratio"] for i in hit])
        ex = " · ".join(f"「{i[key][:22]}」({i['ratio']:.0f})" for i in sorted(hit, key=lambda x: -x["ratio"])[:3])
        lines.append(f"| {name} — {desc} | {len(hit)} | {len(hit) / n * 100:.0f}% | {med:.1f} (전체 {base:.1f}) | {st.median([i['views'] for i in hit]):,.0f} | {ex} |")
        res.append((name, len(hit), med))
    return lines, res


def main() -> int:
    t0 = time.time()
    items = load()
    print(f"[LOAD] [{time.strftime('%Y-%m-%dT%H:%M:%S')}] success_thumbs={len(items)} with_sub={sum(1 for i in items if i['sub_text'])}")
    L = ["# 심리 성공 사례 썸네일 문구 갈래", "",
         f"> `psychology/source/thumb_text_patterns.py` v1.0 · {time.strftime('%Y-%m-%d')} · 사용자 지시 \"실험형 썸네일 문구 성공 사례 분석해서 한거야? 분석해서 만들고 …\"",
         f"> 자료: `thumb_codes.tsv` 성공 사례 {len(items)}장 (Claude 가 그림을 보고 옮긴 문구) + `compare.csv` 배수. **한계: 성공 사례만** — 많이 쓰인 꼴·그 안에서 배수가 큰 꼴만 보임, 인과 아님. 갈래는 낱말 규칙(겹침 있음).", ""]
    L += ["## 1. 주요 문구 (큰 글자)", ""]
    t, res_m = table(items, MAIN, "main_text")
    L += t
    subs = [i for i in items if i["sub_text"]]
    L += ["", f"## 2. 보조 문구 (말풍선·꼬리표) — 있는 썸네일 {len(subs)}/{len(items)}장 ({len(subs) / len(items) * 100:.0f}%)", ""]
    t, res_s = table(subs, SUB, "sub_text")
    L += t
    L += ["", "## 3. 가운데값 비교 — 보조 문구가 있는 썸네일 vs 없는 썸네일", "",
          f"- 있음 {len(subs)}장 배수 가운데값 {st.median([i['ratio'] for i in subs]):.1f} · 없음 {len(items) - len(subs)}장 {st.median([i['ratio'] for i in items if not i['sub_text']]):.1f}", ""]
    (OUT / "thumb_text_patterns.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    for name, n, med in res_m + res_s:
        print(f"[PATTERN] {name} n={n} ratio_median={med:.1f}")
    print(f"[DONE] out={(OUT / 'thumb_text_patterns.md').relative_to(ROOT)} seconds={time.time() - t0:.1f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
