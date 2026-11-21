#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-11-21 — 지금 한국 유튜브 인기 영상(chart=mostPopular) 수집 → 이슈 쇼츠 주제 찾기용.
#   사용자 지시 2026-11-21 "좀 지금 뜨겁게 이슈되고 있는 것좀 찾아봐 다른 세션에서 유튜브 API하면 되잖아 시험 관련 말고".
#   이 도구는 YouTube Data API 키가 있는 세션(googleapis.com 이 열린 환경 — 음악·재테크 분석 세션)에서 돌린다.
#   · videos.list chart=mostPopular regionCode=<나라> — 전체(최대 200개) + 카테고리별(뉴스·인물·엔터·과학기술·노하우·교육·스포츠·게임·음악·코미디·자동차)
#     호출마다 1단위 (전체 4쪽 + 카테고리 11 × 최대 1쪽 ≈ 15단위)
#   · 결과: new/result/trending/trending_<나라>_<시각>.json (원자료) · .md (순위표 · 제목 낱말 상위 · 카테고리별 상위)
#   · --push: main 에 커밋·푸시 (GITHUB_TOKEN 있는 세션)
# 사용: YOUTUBE_API_KEY=… python3 tools/trending_scan.py [--region KR] [--push]
# 로그: [STAGE] [시각] key=value … · 키 값은 출력하지 않음 (끝 4자리만)
from __future__ import annotations

import argparse
import collections
import datetime as dt
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VERSION = "v1.0"
API = "https://www.googleapis.com/youtube/v3/videos"
CATS = {"25": "뉴스·정치", "22": "인물·블로그", "24": "엔터테인먼트", "28": "과학기술", "26": "노하우·스타일",
        "27": "교육", "17": "스포츠", "20": "게임", "10": "음악", "23": "코미디", "2": "자동차"}
STOP = set("the a an of to in on for and is are 이 그 저 것 수 등 및 더 왜 뭐 진짜 지금 오늘 결국 그냥 이제 다시 처음 정말 너무 이런 이거 그거 shorts 쇼츠".split())
KST = dt.timezone(dt.timedelta(hours=9))


def log(stage: str, **kv) -> None:
    print(f"[{stage}] [{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}] " + " ".join(f"{k}={v}" for k, v in kv.items()), flush=True)


def api_key() -> str:
    for k in ("YOUTUBE_API_KEY", "YOUTUBE_API_KEY_MUSIC", "YOUTUBE_API_KEY_ECONOMIC", "YOUTUBE_API_KEY_NEW", "YOUTUBE_API_KEY_HISTORY"):
        v = os.environ.get(k, "").strip()
        if v:
            log("KEY", env=k, tail=v[-4:])
            return v
    raise SystemExit("[KEY] ❌ YOUTUBE_API_KEY 환경 변수가 없음 → 키가 있는 세션(음악·재테크 분석 환경)에서 실행")


def get(params: dict, retries: int = 3) -> dict:
    url = API + "?" + urllib.parse.urlencode(params)
    for i in range(retries):
        try:
            with urllib.request.urlopen(url, timeout=30) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            body = e.read()[:300].decode(errors="replace")
            if e.code in (400, 404):            # 그 나라에 없는 카테고리 차트 등 — 건너뜀
                log("API", status=e.code, category=params.get("videoCategoryId", "-"), note=body.replace(" ", "_")[:120])
                return {}
            if e.code == 403:
                raise SystemExit(f"[API] ❌ 403 (할당량·키 제한) {body}")
            time.sleep(2 ** i)
        except (urllib.error.URLError, TimeoutError) as e:
            log("API", retry=i + 1, error=str(e)[:120])
            time.sleep(2 ** i)
    raise SystemExit(f"[API] ❌ 연결 실패 → googleapis.com 이 열린 세션에서 다시 ({url[:80]}…)")


def iso_dur(s: str) -> int:
    m = re.fullmatch(r"P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", s or "")
    if not m:
        return 0
    d, h, mi, se = (int(x or 0) for x in m.groups())
    return d * 86400 + h * 3600 + mi * 60 + se


def row(it: dict, rank: int, chart: str) -> dict:
    sn, st, cd = it.get("snippet", {}), it.get("statistics", {}), it.get("contentDetails", {})
    pub = sn.get("publishedAt", "")
    age_h = None
    if pub:
        age_h = round((dt.datetime.now(dt.timezone.utc) - dt.datetime.fromisoformat(pub.replace("Z", "+00:00"))).total_seconds() / 3600, 1)
    views = int(st.get("viewCount", 0) or 0)
    return {"chart": chart, "rank": rank, "id": it["id"], "title": sn.get("title", ""), "channel": sn.get("channelTitle", ""),
            "category": CATS.get(sn.get("categoryId", ""), sn.get("categoryId", "")), "published": pub, "age_h": age_h,
            "views": views, "likes": int(st.get("likeCount", 0) or 0), "comments": int(st.get("commentCount", 0) or 0),
            "views_per_h": round(views / age_h) if age_h else None, "sec": iso_dur(cd.get("duration", "")),
            "tags": (sn.get("tags") or [])[:8], "url": f"https://youtu.be/{it['id']}"}


def scan(region: str, key: str) -> list[dict]:
    rows, units = [], 0
    base = {"part": "snippet,statistics,contentDetails", "chart": "mostPopular", "regionCode": region, "maxResults": 50, "key": key}
    tok, rank = None, 0
    for _ in range(4):                                    # 전체 최대 200
        j = get(dict(base, **({"pageToken": tok} if tok else {})))
        units += 1
        for it in j.get("items", []):
            rank += 1
            rows.append(row(it, rank, "전체"))
        tok = j.get("nextPageToken")
        if not tok:
            break
    log("SCAN", chart="전체", videos=rank)
    for cid, name in CATS.items():
        j = get(dict(base, videoCategoryId=cid))
        units += 1
        for k, it in enumerate(j.get("items", []), 1):
            rows.append(row(it, k, name))
        log("SCAN", chart=name, videos=len(j.get("items", [])))
    log("QUOTA", units=units)
    return rows


def words(titles: list[str]) -> list[tuple[str, int]]:
    c = collections.Counter()
    for t in titles:
        seen = set()
        for w in re.findall(r"[가-힣A-Za-z0-9]{2,}", re.sub(r"#\S+", " ", t)):
            w = w.lower()
            if w in STOP or w.isdigit() or w in seen:
                continue
            seen.add(w)
            c[w] += 1
    return c.most_common(40)


def report(rows: list[dict], region: str, stamp: str) -> str:
    allr = [r for r in rows if r["chart"] == "전체"]
    out = [f"# 유튜브 인기 영상 ({region}) — {stamp} KST", "",
           f"`tools/trending_scan.py` {VERSION} · videos.list chart=mostPopular · 전체 {len(allr)}개 + 카테고리별. 숫자는 받은 때 기준.", "",
           "## 1. 전체 순위 (쇼츠 = 3분 이하)", "", "| # | 제목 | 채널 | 카테고리 | 조회수 | 시간당 | 올린 지 | 길이 |", "|---|---|---|---|---|---|---|---|"]
    for r in allr:
        t = r["title"].replace("|", "/")[:70]
        vph = f"{r['views_per_h']:,}" if isinstance(r["views_per_h"], int) else "-"
        length = "쇼츠" if r["sec"] and r["sec"] <= 180 else f"{r['sec'] // 60}분"
        out.append(f"| {r['rank']} | [{t}]({r['url']}) | {r['channel'][:20].replace('|', '/')} | {r['category']} | {r['views']:,} | {vph} | {r['age_h']}h | {length} |")
    out += ["", "## 2. 전체 순위 제목 낱말 상위 (영상 몇 개에 나왔나)", "", "| 낱말 | 영상 수 |", "|---|---|"]
    out += [f"| {w} | {n} |" for w, n in words([r["title"] for r in allr])]
    out += ["", "## 3. 카테고리별 상위 10", ""]
    for name in CATS.values():
        cr = [r for r in rows if r["chart"] == name][:10]
        if not cr:
            continue
        out += [f"### {name}", ""] + [f"{r['rank']}. [{r['title'][:70]}]({r['url']}) — {r['channel'][:20]} · {r['views']:,}회 · {r['age_h']}h" for r in cr] + [""]
    return "\n".join(out) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="지금 유튜브 인기 영상(mostPopular) 수집")
    ap.add_argument("--region", default="KR")
    ap.add_argument("--push", action="store_true", help="main 에 커밋·푸시")
    a = ap.parse_args(argv)
    t0 = time.time()
    log("START", tool=f"trending_scan.py {VERSION}", region=a.region, push=a.push)
    rows = scan(a.region, api_key())
    if not rows:
        raise SystemExit("[SCAN] ❌ 받은 영상이 없음 (mostPopular 차트가 비었거나 막힘)")
    stamp = dt.datetime.now(KST).strftime("%Y-%m-%d %H:%M")
    fn = dt.datetime.now(KST).strftime("%Y%m%d-%H%M")
    d = ROOT / "new" / "result" / "trending"
    d.mkdir(parents=True, exist_ok=True)
    jp, mp = d / f"trending_{a.region}_{fn}.json", d / f"trending_{a.region}_{fn}.md"
    jp.write_text(json.dumps({"tool": f"trending_scan.py {VERSION}", "region": a.region, "fetched_kst": stamp, "rows": rows},
                             ensure_ascii=False, indent=1), "utf-8")
    mp.write_text(report(rows, a.region, stamp), "utf-8")
    log("WRITE", json=str(jp.relative_to(ROOT)), md=str(mp.relative_to(ROOT)), rows=len(rows))
    if a.push:
        g = lambda *x: subprocess.run(["git", "-C", str(ROOT), *x], capture_output=True, text=True)
        g("add", str(jp), str(mp))
        r = g("commit", "-m", f"[이슈 쇼츠] 유튜브 인기 영상 {a.region} {stamp} KST — trending_scan.py {VERSION}")
        for i in range(4):
            g("pull", "--rebase", "origin", "main")
            p = g("push", "origin", "HEAD:main")
            if p.returncode == 0:
                log("PUSH", result="ok")
                break
            time.sleep(2 ** (i + 1))
        else:
            log("PUSH", result="fail", error=p.stderr[-200:].replace("\n", " "))
    log("DONE", sec=round(time.time() - t0, 1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
