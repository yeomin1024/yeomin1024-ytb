#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-11-27 — 키: PSYCHOLOGY_YOUTUBE_API_KEY → YOUTUBE_API_KEY_PSYCHOLOGY → YOUTUBE_API_KEY 순서 (주제 접두사 — 사용자 지시 2026-11-27 "주제별 접두사를 변수명에 붙여서 구분되도록해"). 시작할 때 한 번 정함.
# (이전) VERSION: v1.0 — 2026-11-24 — 신규: ADHD 관련 영상 제목·태그에서 많이 쓰인 낱말
#   사용자 지시 2026-11-24 "진작 할걸 이렇게 바꾸고 ADHD 관련 영상에서 많이 쓰인 단어 알려줘봐".
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.0 | 2026-11-24 | 최초 — adhd.csv 영상의 제목 낱말·태그 (videos.list snippet, 캐시) · 낱말마다 영상 수·조회수 가운데값·상위 25% 몫 | fetch · count · main |
"""psychology/result/topics/adhd.csv (topic_success.py adhd — ADHD 관련 영상 137개, 최근 180일)의 제목 낱말과 태그를 센다.
→ psychology/result/topics/adhd_words.md

- 제목 낱말 = tools/content_analysis.py words() (끝 조사 거칠게 뗌 · 한 글자·불용어 뺌) — 한 영상에 여러 번 나와도 1번.
- 태그 = YouTube videos.list part=snippet 의 tags (50개씩 · 1단위) — 응답은 psychology/result/topics/adhd_tags_cache.json.gz 에 두고 다시 받지 않음.
- 낱말마다: 쓴 영상 수 · 그 영상들의 조회수 가운데값 · '조회수 상위 25%' 영상 중 몫 vs 나머지 중 몫 (배 = 상위 몫 ÷ 나머지 몫).
한계: 최근 180일 검색 위쪽 꼬리 137개 · 낱말 규칙(형태소 분석 아님) · 인과 아님. 정신건강 정보 영상 — 연구·교육용 (의료 상담 아님).
실행: python3 psychology/source/adhd_words.py [--offline]   (키: 환경 변수 YOUTUBE_API_KEY — 출력하지 않음)
"""
from __future__ import annotations

import argparse
import collections
import csv
import gzip
import json
import os
import statistics as st
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
from content_analysis import words  # noqa: E402

TOP = ROOT / "psychology" / "result" / "topics"
CACHE = TOP / "adhd_tags_cache.json.gz"
MIN_N = 4          # 이보다 적은 영상에 나온 낱말은 표에서 뺌


def log(stage, **kv):
    print(f"[{stage}] [{time.strftime('%Y-%m-%dT%H:%M:%S')}] " + " ".join(f"{k}={v}" for k, v in kv.items()), flush=True)


def fetch(ids, offline):
    cache = json.load(gzip.open(CACHE, "rt", encoding="utf-8")) if CACHE.exists() else {}
    need = [i for i in ids if i not in cache]
    if need and offline:
        log("FETCH", level="warn", missing=len(need), note="--offline 이라 태그 없이")
    elif need:
        key = next((os.environ[k].strip() for k in ("PSYCHOLOGY_YOUTUBE_API_KEY", "YOUTUBE_API_KEY_PSYCHOLOGY", "YOUTUBE_API_KEY") if os.environ.get(k, "").strip()), "")
        if not key:
            sys.exit("[FETCH] YOUTUBE_API_KEY 없음 — 환경 변수로 넣거나 --offline")
        for k in range(0, len(need), 50):
            q = urllib.parse.urlencode({"part": "snippet", "id": ",".join(need[k:k + 50]), "key": key, "maxResults": 50})
            try:
                with urllib.request.urlopen(f"https://www.googleapis.com/youtube/v3/videos?{q}", timeout=30) as r:
                    data = json.load(r)
            except Exception as ex:                       # 키 값은 출력하지 않음
                sys.exit(f"[FETCH] videos.list 실패 ({type(ex).__name__}) — 네트워크·할당량 확인 뒤 다시 (--offline 이면 태그 없이)")
            for it in data.get("items", []):
                cache[it["id"]] = {"tags": it["snippet"].get("tags", []), "title": it["snippet"].get("title", "")}
            for i in need[k:k + 50]:
                cache.setdefault(i, {"tags": [], "title": "", "missing": True})
        with gzip.open(CACHE, "wt", encoding="utf-8") as f:
            json.dump(cache, f, ensure_ascii=False)
        log("FETCH", calls=(len(need) + 49) // 50, units=(len(need) + 49) // 50, cached=len(cache))
    return cache


def norm_tag(t):
    t = t.strip().lower().replace(" ", "")
    return t


def count(rows, getter):
    """낱말 → 영상 id 집합."""
    m = collections.defaultdict(set)
    for r in rows:
        for w in set(getter(r)):
            m[w].add(r["video_id"])
    return m


def table(m, rows, top_ids, title, n_show=40):
    views = {r["video_id"]: int(r["views"]) for r in rows}
    n_top, n_rest = len(top_ids), len(rows) - len(top_ids)
    out = [f"## {title}", "", "| 순위 | 낱말 | 영상 수 | 몫 | 조회수 가운데값 | 상위 25% 중 몫 | 나머지 중 몫 | 배 |", "|---|---|---|---|---|---|---|---|"]
    items = sorted(((w, ids) for w, ids in m.items() if len(ids) >= MIN_N), key=lambda x: (-len(x[1]), x[0]))
    for i, (w, ids) in enumerate(items[:n_show], 1):
        a = len(ids & top_ids) / n_top if n_top else 0
        b = len(ids - top_ids) / n_rest if n_rest else 0
        lift = f"{a / b:.1f}" if b else ("∞" if a else "—")
        out.append(f"| {i} | {w} | {len(ids)} | {len(ids) / len(rows) * 100:.0f}% | {st.median(views[x] for x in ids):,.0f} | {a * 100:.0f}% | {b * 100:.0f}% | {lift} |")
    return out, items


def main(argv=None):
    ap = argparse.ArgumentParser(description="ADHD 관련 영상 제목·태그 낱말")
    ap.add_argument("--offline", action="store_true")
    a = ap.parse_args(argv)
    t0 = time.time()
    try:
        rows = list(csv.DictReader(open(TOP / "adhd.csv", encoding="utf-8-sig")))
    except OSError as ex:
        sys.exit(f"[LOAD] adhd.csv 없음 ({ex}) — python3 psychology/source/topic_success.py adhd 먼저")
    log("LOAD", videos=len(rows), source="psychology/result/topics/adhd.csv")
    cache = fetch([r["video_id"] for r in rows], a.offline)
    vs = sorted(int(r["views"]) for r in rows)
    q3 = vs[int(len(vs) * 0.75)]
    top_ids = {r["video_id"] for r in rows if int(r["views"]) >= q3}
    log("SPLIT", top25_views_min=q3, top=len(top_ids), rest=len(rows) - len(top_ids))
    tw, titems = table(count(rows, lambda r: words(r["title"])), rows, top_ids, "1. 제목 낱말 (영상 수 순)")
    with_tags = [r for r in rows if cache.get(r["video_id"], {}).get("tags")]
    tg, gitems = table(count(with_tags, lambda r: [norm_tag(t) for t in cache[r["video_id"]]["tags"]]), with_tags,
                       top_ids & {r["video_id"] for r in with_tags}, f"2. 태그 (태그가 있는 영상 {len(with_tags)}개 · 띄어쓰기·대소문자 무시)")
    L = ["# ADHD 관련 영상에서 많이 쓰인 낱말", "",
         f"> `psychology/source/adhd_words.py` v1.0 · {time.strftime('%Y-%m-%d')} · 사용자 지시 \"ADHD 관련 영상에서 많이 쓰인 단어 알려줘봐\"",
         f"> 자료: `adhd.csv` {len(rows)}개 (최근 180일 · ADHD 제목 · 검색 위쪽 꼬리) · 조회수 상위 25% = {q3:,}회 이상 {len(top_ids)}개. "
         f"'배' = 상위 25% 영상 중 그 낱말을 쓴 몫 ÷ 나머지 중 몫 (1보다 크면 잘 된 영상 쪽에 더 많음 · 표본 작음). 영상 {MIN_N}개 미만 낱말은 뺌. 인과 아님.", ""]
    L += tw + [""] + tg + [""]
    (TOP / "adhd_words.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    for w, ids in titems[:15]:
        log("TITLE", word=w, videos=len(ids))
    for w, ids in gitems[:15]:
        log("TAG", tag=w, videos=len(ids))
    log("DONE", out=(TOP / "adhd_words.md").relative_to(ROOT), seconds=round(time.time() - t0, 1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
