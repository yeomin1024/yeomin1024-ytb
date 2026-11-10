#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-11-10 — 새로: 분석 자료에 나온 작은 채널들의 **구독자가 실제로 얼마나 늘었는지**를 재는 도구
#   (사용자 질문 2026-11-10 "구독자를 빠르게 모으기 위해서는 채널방향을 어떻게 잡아야해" — 조회수가 아니라 구독자 증가를 직접 봄).
#   · 대상 = persona_evidence 의 제목 비교 집단(한국어·주제 안·4분↑·7~180일·수집 때 구독자 5만 이하) 영상의 채널
#   · 받는 것(YouTube Data API v3 · API 키 · 공개 자료만): videos.list(영상 → 채널 ID, 50개에 1단위 — 한 번 받으면 channel_ids.json 에 두고 다시 안 받음)
#       · channels.list(구독자·총조회·영상 수·만든 날, 50개에 1단위) → 그날 스냅숏 channel_growth/<날짜>.json
#   · 내는 것: channel_growth.md — ① 수집 때(compare.csv) 대비 증가 ② 앞 스냅숏 대비 증가(날짜가 정확) ③ 채널 꼴별 가운데값
#       ④ 구독 전환(구독자 ÷ 채널 총조회) ⑤ 빨리 큰 새 채널. 채널 꼴은 <주제>/persona_judge.toml [channel_format] (Claude 가 제목을 읽고 붙임)
#   · 한계: 구독자 수는 API 가 세 자리로 반올림 · compare.csv 의 구독자는 받은 날이 영상마다 달라(2026-10-15~28) ①은 '약 3주' · 상관이지 원인이 아님
#   · 키는 환경 변수 YOUTUBE_API_KEY (출력·저장 ✗). 연구·교육용 — 투자 권유가 아님.
# 사용:
#   python3 tools/channel_growth.py stock            # 스냅숏 받고 보고서 다시 (약 10~65단위)
#   python3 tools/channel_growth.py stock --report   # API 없이 가장 최근 스냅숏으로 보고서만
#   python3 tools/channel_growth.py --selftest
import argparse
import collections
import datetime
import json
import logging
import os
import statistics
import sys
import time
import tomllib
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import persona_evidence as PE  # noqa: E402  제목 비교 집단(build_set_a)·log

VERSION = "v1.0"
LOG = logging.getLogger("channel_growth")
API = "https://www.googleapis.com/youtube/v3/"


def log(stage, level=logging.INFO, **kv):
    ts = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    LOG.log(level, "[%s] [%s] %s", stage, ts, " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) else v}" for k, v in kv.items()))


def call(path, **q):
    q["key"] = os.environ["YOUTUBE_API_KEY"]
    try:
        with urllib.request.urlopen(API + path + "?" + urllib.parse.urlencode(q), timeout=40) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "ignore")[:200].replace("\n", " ")
        log("API", logging.ERROR, path=path, status=e.code, body=body, next="403 quotaExceeded 면 태평양 자정 뒤 다시 · 400 이면 ID 목록 확인")
        return None
    except Exception as e:  # 네트워크
        log("API", logging.ERROR, path=path, error=f"{type(e).__name__}: {e}", next="네트워크·프록시 확인 뒤 다시")
        return None


def chunks(xs, n=50):
    for i in range(0, len(xs), n):
        yield xs[i:i + n]


def median(xs):
    xs = list(xs)
    return statistics.median(xs) if xs else None


def growth(then, now):
    return (now - then) / then if then else None


def fetch(topic, base):
    cfg = PE.load_cfg(topic)
    A, _ = PE.build_set_a(topic, cfg)
    idp = base / "channel_ids.json"
    vch = json.loads(idp.read_text("utf-8")) if idp.exists() else {}
    need = [r["id"] for r in A if r["id"] not in vch]
    units = 0
    for ch in chunks(need):
        r = call("videos", part="snippet", id=",".join(ch), fields="items(id,snippet/channelId)")
        units += 1
        if r is None:
            return None
        got = {it["id"]: it["snippet"]["channelId"] for it in r.get("items", [])}
        for v in ch:
            vch[v] = got.get(v, "")       # 지워진·비공개 영상은 빈 값으로 적어 다시 안 물음
    idp.write_text(json.dumps(vch, ensure_ascii=False, indent=0) + "\n", "utf-8")
    ids = sorted({c for c in vch.values() if c})
    snap = {}
    for ch in chunks(ids):
        r = call("channels", part="snippet,statistics", id=",".join(ch), fields="items(id,snippet(title,publishedAt),statistics)")
        units += 1
        if r is None:
            return None
        for it in r.get("items", []):
            s = it["statistics"]
            if s.get("hiddenSubscriberCount"):
                continue
            snap[it["id"]] = {"title": it["snippet"]["title"], "born": it["snippet"]["publishedAt"][:10], "subs": int(s.get("subscriberCount", 0)),
                              "views": int(s.get("viewCount", 0)), "videos": int(s.get("videoCount", 0))}
    day = time.strftime("%Y-%m-%d", time.gmtime())
    d = base / "channel_growth"
    d.mkdir(exist_ok=True)
    (d / f"{day}.json").write_text(json.dumps({"day": day, "tool": f"channel_growth.py {VERSION}", "channels": snap}, ensure_ascii=False, indent=0) + "\n", "utf-8")
    log("FETCH", set_a=len(A), new_video_lookups=len(need), channels=len(snap), units=units, snapshot=f"channel_growth/{day}.json")
    return day


def load_snaps(base):
    d = base / "channel_growth"
    out = []
    for p in sorted(d.glob("*.json")) if d.exists() else []:
        j = json.loads(p.read_text("utf-8"))
        out.append((j["day"], j["channels"]))
    return out


def fmt_of(name, formats):
    for k, subs in formats.items():
        if any(s in name for s in subs):
            return k
    return None


def build_rows(topic, base, snap, day):
    cfg = PE.load_cfg(topic)
    A, _ = PE.build_set_a(topic, cfg)
    vch = json.loads((base / "channel_ids.json").read_text("utf-8"))
    formats = cfg.get("channel_format", {})
    by = collections.defaultdict(list)
    for r in A:
        c = vch.get(r["id"])
        if c and c in snap:
            by[c].append(r)
    today = datetime.date.fromisoformat(day)
    rows = []
    for c, vs in by.items():
        s = snap[c]
        then = max(v["subs"] for v in vs)
        best = max(vs, key=lambda v: v["score"])
        rows.append({"id": c, "name": s["title"], "then": then, "now": s["subs"], "gain": s["subs"] - then, "pct": growth(then, s["subs"]),
                     "age": (today - datetime.date.fromisoformat(s["born"])).days, "videos": s["videos"], "views": s["views"],
                     "conv": s["subs"] / s["views"] if s["views"] else None, "n": len(vs), "ok": sum(1 for v in vs if v["ok"]),
                     "title": best["title"], "format": fmt_of(s["title"], formats)})
    return rows


def render(topic, rows, day, prev):
    o = []
    w = o.append
    w(f"# {topic} — 작은 채널의 구독자 증가 (자동)")
    w("")
    w(f"스냅숏 {day} · `tools/channel_growth.py {VERSION}` · 대상 = 제목 비교 집단(수집 때 구독자 5만 이하) 채널 {len(rows)}개. 읽는 법·권고는 `{topic}/guides/channel_direction.md`.")
    w("※ '수집 때'는 compare.csv 의 구독자(2026-10-15~28 사이 — 영상마다 받은 날이 다름) → **약 3주** 증가. API 구독자 수는 세 자리로 반올림. 상관이지 원인이 아니다. 투자 권유 아님.")
    w("")
    g = [r["pct"] for r in rows if r["pct"] is not None]
    w(f"- 증가율 가운데값 **{median(g):+.1%}** · 상위 10% 선 {sorted(g)[int(len(g) * .9)]:+.1%} · 줄어든 채널 {sum(1 for x in g if x < 0)}개.")
    w(f"- 만든 지 1년 안 채널 {sum(1 for r in rows if r['age'] <= 365)}개 · 6개월 안 {sum(1 for r in rows if r['age'] <= 183)}개.")
    w("")
    w("## 1. 채널 꼴별 (꼴 = `persona_judge.toml [channel_format]` — 제목을 읽고 붙인 것, 수집 때 2만 이하·지금 1천 이상·자료 3개↑ 또는 성공 1↑)")
    sel = [r for r in rows if r["format"] and r["then"] <= 20000 and r["now"] >= 1000 and (r["n"] >= 3 or r["ok"] >= 1)]
    by = collections.defaultdict(list)
    for r in sel:
        by[r["format"]].append(r)
    w("| 꼴 | 채널 | 약 3주 증가율 가운데 | +10%↑ | 구독 전환 가운데 (2년 안 채널) | 가장 큰 곳 |")
    w("|---|---|---|---|---|---|")
    for k, v in sorted(by.items(), key=lambda x: -median(r["pct"] for r in x[1])):
        cv = [r["conv"] for r in v if r["age"] <= 730 and r["conv"]]
        top = max(v, key=lambda r: r["pct"])
        w(f"| {k} | {len(v)} | **{median(r['pct'] for r in v):+.1%}** | {sum(1 for r in v if r['pct'] >= .10)}/{len(v)} | {f'{median(cv):.2%} ({len(cv)})' if len(cv) >= 3 else '적음'} | {top['name'][:14]} {top['pct']:+.0%} |")
    w("")
    w("구독 전환 = 지금 구독자 ÷ 채널 총조회 (조회 1만 번에 구독 몇 명). 채널 수가 5~20개라 **방향만** 본다.")
    w("")
    w("## 2. 약 3주 동안 구독자가 가장 많이 는 곳 (수집 때 2만 이하)")
    w("| 증가 | 구독자 | 채널 나이 · 영상 수 | 구독 전환 | 채널 | 대표 제목 |")
    w("|---|---|---|---|---|---|")
    for r in sorted([r for r in rows if r["then"] <= 20000], key=lambda r: -r["gain"])[:25]:
        w(f"| +{r['gain']:,.0f} ({r['pct']:+.0%}) | {r['then']:,.0f} → {r['now']:,} | {r['age']}일 · {r['videos']} | {r['conv']:.2%} | {r['name'][:16]} | {PE.flat(r['title'], 50)} |")
    w("")
    w("## 3. 만든 지 1년 안에 3천 명을 넘긴 곳 — 영상 한 편이 구독자를 얼마나 데려왔나")
    w("| 영상당 구독자 | 구독자 · 영상 · 나이 | 구독 전환 | 약 3주 | 채널 | 대표 제목 |")
    w("|---|---|---|---|---|---|")
    for r in sorted([r for r in rows if r["age"] <= 365 and r["now"] >= 3000 and r["videos"] <= 400], key=lambda r: -r["now"] / max(1, r["videos"]))[:20]:
        w(f"| {r['now'] / max(1, r['videos']):.0f} | {r['now']:,} · {r['videos']} · {r['age']}일 | {r['conv']:.2%} | {r['pct']:+.0%} | {r['name'][:16]} | {PE.flat(r['title'], 46)} |")
    w("")
    if prev:
        pday, psnap = prev
        days = (datetime.date.fromisoformat(day) - datetime.date.fromisoformat(pday)).days
        w(f"## 4. 앞 스냅숏({pday}) 대비 — {days}일 동안 (날짜가 정확한 증가)")
        d = [(r["now"] - psnap[r["id"]]["subs"], r) for r in rows if r["id"] in psnap]
        for gain, r in sorted(d, key=lambda x: -x[0])[:15]:
            w(f"- +{gain:,} · {psnap[r['id']]['subs']:,} → {r['now']:,} · {r['name'][:16]} ({r['format'] or '꼴 없음'})")
        w("")
    return "\n".join(o) + "\n"


def selftest():
    assert growth(100, 150) == 0.5 and growth(0, 10) is None
    assert list(chunks(list(range(5)), 2)) == [[0, 1], [2, 3], [4]]
    assert fmt_of("테스프레소", {"지금": ["테스프"], "그 밖": ["없음"]}) == "지금" and fmt_of("모름", {"지금": ["테스프"]}) is None
    assert median([]) is None and median([1, 3]) == 2
    print("[SELFTEST] ok — growth·chunks·fmt_of·median")
    return 0


def main(argv):
    ap = argparse.ArgumentParser(description="작은 채널 구독자 증가 스냅숏·보고서")
    ap.add_argument("topic", nargs="?", default="stock")
    ap.add_argument("--report", action="store_true", help="API 를 부르지 않고 가장 최근 스냅숏으로 보고서만")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args(argv)
    logging.basicConfig(level=getattr(logging, a.log_level), format="%(message)s", stream=sys.stdout)
    PE.LOG.setLevel(logging.WARNING)
    if a.selftest:
        return selftest()
    base = ROOT / a.topic / "result" / "outliers"
    if not a.report:
        if not os.environ.get("YOUTUBE_API_KEY"):
            log("ERROR", logging.ERROR, where="env", missing="YOUTUBE_API_KEY", next="--report 로 저장된 스냅숏만 쓰거나 키가 있는 환경에서 다시")
            return 1
        if fetch(a.topic, base) is None:
            log("STOP", logging.ERROR, reason="API 실패 — 스냅숏을 쓰지 않음")
            return 1
    snaps = load_snaps(base)
    if not snaps:
        log("ERROR", logging.ERROR, where="snapshot", next="먼저 --report 없이 한 번 실행")
        return 1
    day, snap = snaps[-1]
    rows = build_rows(a.topic, base, snap, day)
    (base / "channel_growth.md").write_text(render(a.topic, rows, day, snaps[-2] if len(snaps) > 1 else None), "utf-8")
    g = [r["pct"] for r in rows if r["pct"] is not None]
    log("REPORT", day=day, channels=len(rows), median_growth=round(median(g), 4), labeled=sum(1 for r in rows if r["format"]), snapshots=len(snaps), md=f"{a.topic}/result/outliers/channel_growth.md")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
