#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.2 — 2026-11-27 — 주제 접두사 키: 시작할 때 tools/topic_keys.apply(주제) — <주제>_YOUTUBE_API_KEY 등이 있으면 그 주제 키를 씀 (사용자 지시 2026-11-27 "주제별 접두사를 변수명에 붙여서 구분되도록해"). 오류가 나도 다른 키로 바꾸지 않음.
# (이전) VERSION: v1.1 — 2026-11-26 — --must (주제 밖 영상 빼기 — 드라마·라이브 섞임) · 하루 캐시 · '주는 사람의 심리' 형식 정규식 고침
# 이전 v1.0 — 2026-11-26 — 최초: 관련 주제 영상의 자주 쓰는 낱말·제목 형식 (조회수 무게) — guides/production_rules.md 0번
#   사용자 지시 2026-11-26 "제목 - 관련 주제 영상에서 자주 사용한 주제 관련 단어 사용 … 관련 주제 영상에서 자주 사용하는 형식 참고 / 썸네일 문구 - … 관련 주제 영상에서 자주 사용하는 형식 참고".
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.1 | 2026-11-26 | --must · 캐시 · 형식 정규식 | fetch · main |
# | v1.0 | 2026-11-26 | 최초 — 검색(관련성 순 · 최근 N개월 · 한국) → 롱폼만 → 낱말 표(편수·조회수 무게·상위 1/4 안 편수) · 형식 표 · 상위 제목 | fetch · words · formats · main |
"""관련 주제 영상 제목의 낱말·형식을 센다 (유튜브 Data API · 읽기만).

  python3 tools/related_titles.py <주제> "<검색어1>" "<검색어2>" … [--months 6] [--min-sec 240] [--out <md>]
키: 환경 변수 YOUTUBE_API_KEY (값은 출력하지 않음). 검색 한 번 100단위 + 영상·채널 정보 몇 단위.
결과: 낱말 표(그 낱말이 든 영상 수 · 그 영상들 조회수 가운데값 · 조회수 상위 1/4 안 영상 수) · 형식 표 · 조회수 상위 제목 20.
※ 숫자 · 원문만 — 고르는 판단은 사람/Claude (production_rules.md 1·3번). 연구·교육용 도구.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import statistics
import sys
import urllib.parse
import urllib.request
from pathlib import Path

VERSION = "v1.2"
ROOT = Path(__file__).resolve().parents[1]
API = "https://www.googleapis.com/youtube/v3/"
STOP = set("그리고 그런데 하지만 그래서 영상 오늘 우리 이것 이거 그것 정말 진짜로 하는 있는 없는 같은 위한 대한 되는 했던 하면 하고 해서 해야 합니다 입니다 있습니다 거예요 이런 저런 그런 모든 가지 이유 사람 사람들".split())
# 형식 (정규식 · 이름) — 제목에서 자주 보는 꼴. 새 꼴은 여기에 더함
FORMATS = [
    (r"(는|은|ㄴ)\s*사람(들)?(의|은|이)?[,\s]*(심리|특징|공통점|속마음|정체|비밀)", "~하는 사람(의) 심리·특징·공통점"),
    (r"(심리|특징|공통점|속마음)", "심리·특징·공통점·속마음 낱말"),
    (r"[|｜]", "'|' 로 덧말 붙임"),
    (r"\d+\s*가지", "N가지"),
    (r"(진짜|숨겨진|숨은|본인(만|도)\s*모르는|사실은|알고\s*보면)", "숨은 진실 낱말 (진짜·숨겨진·본인만 모르는·사실은)"),
    (r"(만은\s*아닙니다|때문만은|아니었다|아닙니다)", "반전 꼴 (~만은 아닙니다·아니었다)"),
    (r"(소름|충격|놀라운|무서운)", "감정 센 낱말 (소름·충격·놀라운·무서운)"),
    (r"(당신|혹시\s*당신|당신도)", "당신 부르기"),
    (r"\?", "물음표"),
    (r"(심리학|뇌과학|연구|실험)", "학문·연구 낱말"),
]


def log(stage: str, **kv) -> None:
    now = dt.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    print(f"[{stage}] [{now}] " + " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) and (' ' in v or not v) else v}"
                                          for k, v in kv.items()), flush=True)


def get(path: str, params: dict) -> dict:
    key = os.environ.get("YOUTUBE_API_KEY", "")
    if not key:
        raise SystemExit("[FAIL] YOUTUBE_API_KEY 없음 → 환경 변수에 키 (값은 출력하지 않음)")
    q = urllib.parse.urlencode(dict(params, key=key))
    try:
        with urllib.request.urlopen(API + path + "?" + q, timeout=30) as r:
            return json.load(r)
    except Exception as e:                                      # 키 값이 섞이지 않게 경로만 남김
        raise SystemExit(f"[FAIL] stage=api path={path} error={type(e).__name__}: {str(e)[:120]} next=할당량·네트워크 확인")


def dur_s(iso: str) -> int:
    m = re.match(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", iso or "")
    return sum(int(x or 0) * k for x, k in zip(m.groups(), (3600, 60, 1))) if m else 0


CACHE = ROOT / ".yt_work" / "related_cache"


def fetch(queries: list[str], months: int, min_sec: int) -> list[dict]:
    """같은 검색어·기간은 하루 동안 캐시(.yt_work/related_cache — 저장소 밖)를 다시 씀 (할당량 아끼기)."""
    key = re.sub(r"[^0-9A-Za-z가-힣]+", "_", "|".join(queries))[:120] + f"_{months}m_{min_sec}s_{dt.date.today()}"
    cp = CACHE / f"{key}.json"
    if cp.is_file():
        log("CACHE", hit=cp.name, note="오늘 받은 결과 — API 안 부름")
        return json.loads(cp.read_text("utf-8"))
    out = _fetch(queries, months, min_sec)
    CACHE.mkdir(parents=True, exist_ok=True)
    cp.write_text(json.dumps(out, ensure_ascii=False), "utf-8")
    return out


def _fetch(queries: list[str], months: int, min_sec: int) -> list[dict]:
    after = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=30 * months)).strftime("%Y-%m-%dT%H:%M:%SZ")
    ids: dict[str, str] = {}
    for q in queries:
        d = get("search", {"part": "snippet", "q": q, "type": "video", "regionCode": "KR", "relevanceLanguage": "ko",
                           "maxResults": 50, "publishedAfter": after})
        for it in d.get("items", []):
            ids.setdefault(it["id"]["videoId"], q)
        log("SEARCH", query=q, found=len(d.get("items", [])), units=100)
    vids, out = list(ids), []
    for i in range(0, len(vids), 50):
        for it in get("videos", {"part": "snippet,statistics,contentDetails", "id": ",".join(vids[i:i + 50])}).get("items", []):
            sec = dur_s(it["contentDetails"].get("duration", ""))
            if sec < min_sec or it["snippet"].get("liveBroadcastContent") not in (None, "none"):
                continue
            out.append({"id": it["id"], "title": it["snippet"]["title"], "channel": it["snippet"]["channelTitle"],
                        "views": int(it["statistics"].get("viewCount", 0) or 0), "published": it["snippet"]["publishedAt"][:10],
                        "sec": sec, "query": ids[it["id"]]})
    return out


def words(title: str) -> set[str]:
    t = re.sub(r"[#\[\]【】()（）<>「」『』\"'.,!?~…|｜:;/·\-]+", " ", title)
    out = set()
    for w in re.findall(r"[가-힣A-Za-z0-9]{2,}", t):
        w2 = re.sub(r"(의|은|는|이|가|을|를|에게|에서|으로|로|도|만|과|와|들)$", "", w)   # 거친 조사 떼기
        if len(w2) >= 2 and w2 not in STOP:
            out.add(w2)
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="관련 주제 영상의 낱말·제목 형식")
    ap.add_argument("topic")
    ap.add_argument("queries", nargs="+")
    ap.add_argument("--months", type=int, default=6)
    ap.add_argument("--min-sec", type=int, default=240, help="롱폼 기준 초 (기본 4분)")
    ap.add_argument("--out")
    ap.add_argument("--must", help="제목에 이 정규식이 있어야 셈 (주제 밖 영상 빼기 — 예 '주는|선물|챙겨')")
    a = ap.parse_args(argv)
    import topic_keys                                        # v1.2 주제 접두사 키 (<주제>_YOUTUBE_API_KEY …) — 시작할 때 한 번
    topic_keys.apply(a.topic, say=print)
    log("START", tool=f"related_titles.py {VERSION}", topic=a.topic, queries=len(a.queries), months=a.months, units_est=100 * len(a.queries) + 5)
    vids = fetch(a.queries, a.months, a.min_sec)
    if a.must:
        before = len(vids)
        vids = [v for v in vids if re.search(a.must, v["title"])]
        log("FILTER", must=a.must, kept=len(vids), dropped=before - len(vids))
    if not vids:
        log("FAIL", why="영상 없음", next="검색어·기간 확인")
        return 1
    vids.sort(key=lambda v: -v["views"])
    q3 = vids[max(0, len(vids) // 4 - 1)]["views"]               # 상위 1/4 경계
    top = [v for v in vids if v["views"] >= q3]
    med_all = statistics.median(v["views"] for v in vids)
    wc: dict[str, list[int]] = {}
    for v in vids:
        for w in words(v["title"]):
            wc.setdefault(w, []).append(v["views"])
    rows = [(w, len(vs), statistics.median(vs), sum(1 for x in vs if x >= q3)) for w, vs in wc.items() if len(vs) >= 3]
    rows.sort(key=lambda r: (-r[3], -r[1], -r[2]))
    frows = []
    for pat, name in FORMATS:
        hit = [v for v in vids if re.search(pat, v["title"])]
        if hit:
            frows.append((name, len(hit), statistics.median(v["views"] for v in hit), sum(1 for v in hit if v["views"] >= q3)))
    frows.sort(key=lambda r: -r[3])
    L = [f"# 관련 영상 낱말·형식 — {a.topic}", "",
         f"> `tools/related_titles.py` {VERSION} · {dt.date.today()} · 검색어 {', '.join('「'+q+'」' for q in a.queries)}{(' · 제목 거르기 /' + a.must + '/') if a.must else ''} · 최근 {a.months}개월 · 한국 · 롱폼({a.min_sec // 60}분 넘게) **{len(vids)}편** · 조회수 가운데값 {med_all:,.0f} · 상위 1/4 경계 {q3:,}",
         "> 숫자·원문만 — 제목·썸네일 문구는 `guides/production_rules.md` 1·3번대로 고름. 한계: 검색 결과(관련성 순 50개 × 검색어)만 · 조사는 거칠게 뗌.", "",
         "## 1. 자주 쓰는 낱말 (3편 넘게 · 상위 1/4 안 편수 순)", "", "| 낱말 | 편수 | 조회수 가운데값 | 상위 1/4 안 |", "|---|---|---|---|"]
    L += [f"| {w} | {n} | {m:,.0f} | {t} |" for w, n, m, t in rows[:40]]
    L += ["", "## 2. 자주 쓰는 형식", "", "| 형식 | 편수 | 조회수 가운데값 | 상위 1/4 안 |", "|---|---|---|---|"]
    L += [f"| {n} | {c} | {m:,.0f} | {t} |" for n, c, m, t in frows]
    L += ["", "## 3. 조회수 상위 20편", "", "| 조회수 | 올린 날 | 길이 | 제목 | 채널 |", "|---|---|---|---|---|"]
    L += [f"| {v['views']:,} | {v['published']} | {v['sec'] // 60}분 | {v['title'][:70]} | {v['channel'][:18]} |" for v in vids[:20]]
    text = "\n".join(L) + "\n"
    if a.out:
        Path(a.out).parent.mkdir(parents=True, exist_ok=True)
        Path(a.out).write_text(text, "utf-8")
    print(text)
    log("DONE", videos=len(vids), words=len(rows), formats=len(frows), out=a.out or "-")
    return 0


if __name__ == "__main__":
    sys.exit(main())
