#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-11-10 — 새로: '지금 판' 훑기 — ① 오늘 시장 상태(가격) ② 최근 N일(오늘 포함) 주식 유튜브 영상·댓글 → 판단용 페르소나(stock/guides/persona_judge.md)에 대입할 재료.
#   사용자 지시 2026-11-10 "현재 트렌드를 페르소나에 대입해서 사람들의 심리를 파악해서 그들이 만족하게 할 수 있는 영상을 만들어야해 예를 들면 현재 주식시장의 상태,
#   최근(오늘 포함) 주식 관련 유튜브 분석 등을 페르소나에 대입해 생각해보는거지".
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.0 | 2026-11-10 | 최초 | market·scan·comments·summarize·render·selftest |
#
# 하는 일 (분석기 결과 result/outliers 는 건드리지 않음 — 따로 <주제>/result/trend/ 에):
#   1. 시장 상태 — Yahoo chart API 일별 종가(<주제>/persona_judge.toml TREND_SYMBOLS): 마지막 종가 · 1년 최고가 대비 · 1·5·20거래일 변화 · 최근 10거래일 가장 큰 하루 변동 ·
#      '반등 날'(전날 종가가 252거래일 최고가보다 10% 넘게 낮은 상태에서 하루 +3% 넘게 — 반등 편 calc 와 같은 정의) 여부. 판단은 그날 종가까지만.
#   2. 유튜브 — TREND_QUERIES 검색어마다 최근 --days 일(조회수 순) + 최근 2일(조회수 순, 앞 TREND_FRESH 개 검색어) → 영상 정보·구독자 → 한국어·라이브 아님·주제 밖 아님 →
#      하루 조회수(조회수 ÷ 올린 뒤 날수, 최소 0.25일) · 구독자 대비 조회수 · 묶음(시황·뉴스/정치·장기 …: persona_evidence.group_of 와 같은 규칙).
#   3. 댓글 — 하루 조회수 상위 롱폼(뉴스·정치 채널 뺌) --videos 개 + 구독자 5만 이하 배수 상위 --small 개: 공감순 100개 + 최신순 100개 (영상마다 2단위) →
#      채널 주인·도배·중복을 빼고 **그 기간에 쓴 댓글만** persona_judge.toml [[topic]]·[[ask_type]] 로 나눔 (persona_evidence.all_comments 그대로) → 10월 수집분(persona_evidence.json)과 견줌.
#   할당량: 검색 100단위 × (검색어 수 + TREND_FRESH) + 1단위 요청 약 150 — 키 장부(pc_analysis.KeyLedger)에 적힘. 키 = 환경 변수 YOUTUBE_API_KEY (값은 출력하지 않음).
# 쓰기:
#   python3 tools/trend_scan.py stock [--days 7] [--videos 30] [--small 10] [--quota 2500]
#   python3 tools/trend_scan.py stock --market-only        # 시장 상태만 (API 단위 0)
#   python3 tools/trend_scan.py --selftest
# 출력: <주제>/result/trend/trend_<날짜>.md · .json · comments_<날짜>.jsonl (댓글 글·좋아요·쓴 때·영상 ID 만 — 작성자 이름·채널 ID 없음).
# 한계 (md 맨 위에도 적음): 공감순·최신순 200개 표본이라 '모든 댓글'인 10월 수집분과 뽑는 법이 다름 · 검색어·조회수 순이라 큰 채널·시황 영상 쪽으로 치우침 · 올린 지 하루 안 된 영상의 하루 조회수는 부풀 수 있음.
# ※ 연구·교육용 — 투자 권유 아님.
from __future__ import annotations

import argparse
import collections
import json
import logging
import os
import re
import statistics
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import persona_evidence as PE  # noqa: E402  (설정·묶음 규칙·all_comments·log)

VERSION = "v1.0"
logging.basicConfig(level=os.environ.get("LOG_LEVEL", "INFO"), format="%(message)s", stream=sys.stdout)   # persona_evidence 는 main 에서만 설정 — 여기서도 켬
log = PE.log
HANGUL = re.compile(r"[가-힣]")
DEFAULT_QUERIES = ["주식", "코스피", "국장", "증시", "주식시장", "주가", "주식투자", "미국주식", "미장", "코스닥", "나스닥", "한국주식"]   # stock/keywords.txt 에 있는 말만


# ------------------------------------------------------------------ 1. 시장 상태
def fetch_px(symbol: str, days: int = 800) -> list[tuple[str, float]]:
    """Yahoo chart API 일별 종가 (날짜, 종가). 실패하면 빈 목록 + 로그 (조용히 넘어가지 않음)."""
    p1 = int((datetime.now(timezone.utc) - timedelta(days=days)).timestamp())
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(symbol)}?period1={p1}&period2={int(time.time())}&interval=1d"
    last = None
    for wait in (0, 2, 5):
        time.sleep(wait)
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=40) as r:
                res = json.load(r)["chart"]["result"][0]
            off = int(res.get("meta", {}).get("gmtoffset", 0))
            rows = [((datetime.fromtimestamp(t + off, tz=timezone.utc)).date().isoformat(), float(c))
                    for t, c in zip(res["timestamp"], res["indicators"]["quote"][0]["close"]) if c is not None and c > 0]
            seen, out = set(), []
            for d, c in rows:                                  # 같은 날이 두 번 오면(장중 값) 뒤 것
                if d in seen:
                    out[-1] = (d, c)
                else:
                    seen.add(d); out.append((d, c))
            return out
        except Exception as e:  # noqa: BLE001
            last = repr(e)[:160]
    log("MARKET", logging.WARNING, symbol=symbol, error=last, next="네트워크·기호 확인 — 이 줄은 표에서 빠짐")
    return []


def market_one(name: str, rows: list[tuple[str, float]]) -> dict | None:
    """그날 종가까지만 써서 상태를 냄. 자료가 60일보다 적으면 None."""
    if len(rows) < 60:
        return None
    d, p = [r[0] for r in rows], [r[1] for r in rows]
    n = len(p) - 1
    win = p[max(0, n - 251):n + 1]
    hi = max(win); hi_i = max(0, n - 251) + win.index(hi)
    lo_since = min(p[hi_i:]); lo_i = hi_i + p[hi_i:].index(lo_since)
    chg = lambda k: round((p[n] / p[n - k] - 1) * 100, 1) if n - k >= 0 else None   # noqa: E731
    day = [(d[i], round((p[i] / p[i - 1] - 1) * 100, 1)) for i in range(max(1, n - 9), n + 1)]
    prev_hi = max(p[max(0, n - 252):n])                       # 전날까지의 252거래일 최고가
    rebound = bool(p[n - 1] / prev_hi - 1 <= -0.10 and p[n] / p[n - 1] - 1 >= 0.03)
    streak = 0
    for i in range(n, 0, -1):
        s = 1 if p[i] > p[i - 1] else -1
        if streak == 0 or (streak > 0) == (s > 0):
            streak += s
        else:
            break
    return {"name": name, "date": d[n], "close": round(p[n], 2), "high_1y": round(hi, 2), "high_date": d[hi_i], "from_high": round((p[n] / hi - 1) * 100, 1),
            "low_since_high": round(lo_since, 2), "low_date": d[lo_i], "low_from_high": round((lo_since / hi - 1) * 100, 1), "from_low": round((p[n] / lo_since - 1) * 100, 1),
            "d1": chg(1), "d5": chg(5), "d20": chg(20), "last10": day, "biggest_up_10d": max(day, key=lambda x: x[1]), "biggest_down_10d": min(day, key=lambda x: x[1]),
            "streak": streak, "rebound_day_today": rebound, "days_since_high": n - hi_i}


def market(cfg: dict) -> list[dict]:
    out = []
    for name, sym in cfg.get("TREND_SYMBOLS", {}).items():
        m = market_one(name, fetch_px(sym))
        if m:
            out.append(m)
            log("MARKET", name=name, date=m["date"], close=m["close"], from_high=m["from_high"], d1=m["d1"], d5=m["d5"], d20=m["d20"], low_date=m["low_date"],
                from_low=m["from_low"], rebound_day_today=m["rebound_day_today"])
    return out


# ------------------------------------------------------------------ 2. 유튜브 영상
def iso_seconds(iso: str) -> int:
    m = re.fullmatch(r"P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", iso or "")
    if not m:
        return 0
    dd, h, mi, se = (int(x or 0) for x in m.groups())
    return dd * 86400 + h * 3600 + mi * 60 + se


def video_row(it: dict, subs: dict, now: datetime, cfg: dict) -> dict | None:
    sn, st = it.get("snippet", {}), it.get("statistics", {})
    title = sn.get("title", "")
    if it.get("liveStreamingDetails") or sn.get("liveBroadcastContent") in ("live", "upcoming"):
        return {"drop": "live"}
    if len(HANGUL.findall(title)) < 0.3 * max(1, len(re.sub(r"\s", "", title))):
        return {"drop": "not_korean"}
    pub = datetime.fromisoformat(sn["publishedAt"].replace("Z", "+00:00"))
    age_d = max(0.25, (now - pub).total_seconds() / 86400)
    views = int(st.get("viewCount", 0) or 0)
    sub = subs.get(sn.get("channelId"))
    m = {"id": it["id"], "title": title, "channel": sn.get("channelTitle", ""), "channel_id": sn.get("channelId"), "published": sn["publishedAt"][:10],
         "published_at": sn["publishedAt"], "age_days": round(age_d, 2), "views": views, "views_per_day": round(views / age_d), "subs": sub,
         "ratio": round(views / sub, 2) if sub else None, "seconds": iso_seconds(it.get("contentDetails", {}).get("duration")),
         "comments": int(st.get("commentCount", 0) or 0), "likes": int(st.get("likeCount", 0) or 0), "theme": ""}
    m["kind"] = "long" if m["seconds"] >= 240 else ("short" if m["seconds"] <= 180 else "mid")
    m["g"] = PE.group_of(m, cfg)
    return m


def scan(api, cfg: dict, days: int, now: datetime) -> tuple[list[dict], dict]:
    qs = cfg.get("TREND_QUERIES") or DEFAULT_QUERIES
    fresh_n = int(cfg.get("TREND_FRESH", 6))
    after = lambda k: (now - timedelta(days=k)).strftime("%Y-%m-%dT%H:%M:%SZ")   # noqa: E731
    ids, src = [], collections.Counter()
    for win, queries in ((days, qs), (2, qs[:fresh_n])):
        for q in queries:
            try:
                got = api.search(q, after(win), duration=None, lang="ko")
            except Exception as e:  # noqa: BLE001  (QuotaStop 포함 — 남은 검색은 건너뜀)
                log("SCAN", logging.WARNING, query=q, window_days=win, error=repr(e)[:140], next="할당량이면 태평양 자정 뒤 다시 — 받은 것만으로 계속")
                break
            src[f"{win}d"] += len(got)
            ids += [i for i in got if i not in ids]
    log("SCAN", queries=len(qs), fresh_queries=fresh_n, ids=len(ids), by_window=dict(src), units=api.used)
    items = []
    for k in range(0, len(ids), 50):
        items += api.videos(ids[k:k + 50])
    ch = sorted({it["snippet"]["channelId"] for it in items})
    subs = {}
    for k in range(0, len(ch), 50):
        subs.update(api.channels(ch[k:k + 50]))
    rows, drop = [], collections.Counter()
    for it in items:
        m = video_row(it, subs, now, cfg)
        if m is None or "drop" in m:
            drop[(m or {}).get("drop", "?")] += 1; continue
        if m["age_days"] > days + 0.5:
            drop["older_than_window"] += 1; continue
        if m["g"] == "X_off":
            drop["off_topic"] += 1; continue
        rows.append(m)
    log("FILTER", kept=len(rows), dropped=dict(drop), long=sum(r["kind"] == "long" for r in rows), short=sum(r["kind"] == "short" for r in rows),
        news=sum(r["g"] == "N_news" for r in rows), units=api.used)
    return rows, dict(drop)


# ------------------------------------------------------------------ 3. 댓글
def pick_targets(rows: list[dict], n_top: int, n_small: int) -> list[dict]:
    longs = [r for r in rows if r["kind"] == "long" and r["g"] not in ("N_news", "E_event") and r["comments"] >= 30]
    top = sorted(longs, key=lambda r: -r["views_per_day"])[:n_top]
    small = [r for r in sorted(longs, key=lambda r: -(r["ratio"] or 0)) if r["subs"] and r["subs"] <= 50000 and r not in top][:n_small]
    return top + small


def comments(api, targets: list[dict], cfg: dict, since: str) -> tuple[list[tuple], dict]:
    """(영상, 댓글 ID, None, 좋아요, 글, False, 쓴 날) — persona_evidence 의 댓글 꼴. 채널 주인·도배·기간 밖·중복은 빼고 셈."""
    spam = cfg["exclude"]["_SPAM"]
    out, seen, drop = [], set(), collections.Counter()
    for v in targets:
        for order in ("relevance", "time"):
            d = api.get("commentThreads", part="snippet", videoId=v["id"], maxResults=100, order=order, textFormat="plainText")
            for it in d.get("items", []):
                s = it["snippet"]["topLevelComment"]["snippet"]
                cid = it["snippet"]["topLevelComment"]["id"]
                if cid in seen:
                    drop["dup"] += 1; continue
                seen.add(cid)
                if (s.get("authorChannelId") or {}).get("value") == v["channel_id"]:
                    drop["creator"] += 1; continue
                text = s.get("textDisplay") or ""
                if spam.search(text):
                    drop["spam"] += 1; continue
                day = s.get("publishedAt", "")[:10]
                if day < since:
                    drop["before_window"] += 1; continue
                out.append((v["id"], cid, None, int(s.get("likeCount", 0) or 0), text, False, day))
    log("COMMENTS", videos=len(targets), kept=len(out), dropped=dict(drop), units=api.used)
    return out, dict(drop)


# ------------------------------------------------------------------ 4. 모으기
TITLE_WORDS = [("폭락·급락·붕괴·패닉", r"폭락|급락|붕괴|대폭락|패닉|쇼크|공포"), ("반등·바닥·저점", r"반등|바닥|저점|데드캣"), ("삼전·하닉·반도체", r"삼성전자|삼전|하이닉스|하닉|닉스|반도체"),
               ("지금·오늘·내일·이번 주", r"지금|오늘|내일|이번 ?주|긴급|속보"), ("외국인·기관·수급·공매도", r"외국인|외인|기관|수급|공매도|세력"), ("매도·손절·탈출·팔", r"매도|손절|탈출|팔아|팔지|팔까"),
               ("매수·줍줍·사야·살 때", r"매수|줍줍|사야|살 ?때|담아|저가"), ("전망·예측·시나리오", r"전망|예측|시나리오|갈까|올까"), ("미국·나스닥·S&P", r"미국|나스닥|S&P|미장|엔비디아|테슬라"),
               ("금리·환율·연준", r"금리|환율|연준|FOMC|달러"), ("버티·존버·기다", r"버티|버텨|존버|기다"), ("국민연금·정부·정책", r"국민연금|정부|정책|금융위|대통령")]


def summarize(rows: list[dict], core: list[tuple], cfg: dict, base: dict | None) -> dict:
    V = {r["id"]: r for r in rows}
    n = len(rows)
    by_word = []
    for name, rx in TITLE_WORDS:
        hit = [r for r in rows if re.search(rx, r["title"])]
        vpd_all = statistics.median([r["views_per_day"] for r in rows]) if rows else 0
        by_word.append({"word": name, "n": len(hit), "share": round(len(hit) / n, 3) if n else 0,
                        "median_vpd": round(statistics.median([r["views_per_day"] for r in hit])) if hit else None, "median_vpd_all": round(vpd_all)})
    by_word.sort(key=lambda x: -x["n"])
    groups = collections.Counter(r["g"] for r in rows)
    al = PE.all_comments(core, cfg, V, with_nouns=False) if core else None
    cmp_ = []
    if al and base:
        b = {t["name"]: t for t in base.get("topics", [])}
        for t in al["topics"]:
            o = b.get(t["name"], {})
            cmp_.append({"name": t["name"], "group": t["group"], "n": t["n"], "share": t["share"], "video_median": t["video_median"], "likes_per": t["likes_per"],
                         "ask_share": t["ask_share"], "base_share": o.get("share"), "base_share_oct": o.get("share_now"), "base_video_median_oct": o.get("video_median_now"),
                         "vs_oct": round(t["share"] / o["share_now"], 2) if o.get("share_now") else None, "samples": t["samples"]})
    return {"videos": n, "groups": dict(groups), "title_words": by_word, "all": al, "topics_vs_base": cmp_}


def render(E: dict) -> str:
    w = (L := []).append
    w(f"# {E['topic']} — 지금 판 ({E['date']} · 최근 {E['days']}일, 오늘 포함)")
    w("")
    w(f"`tools/trend_scan.py {VERSION}` · {E['made']} · API {E['units']}단위. 판단용 페르소나(`stock/guides/persona_judge.md` 8번)에 대입할 재료 — **숫자·원문만**, 해석은 그 문서에서.")
    w("⚠ 한계: 댓글은 영상마다 공감순 100 + 최신순 100 표본(10월 수집분은 모든 댓글) · 검색어·조회수 순이라 큰 채널·시황 쪽으로 치우침 · 올린 지 하루 안 된 영상의 하루 조회수는 부풀 수 있음. ※ 연구·교육용 — 투자 권유 아님.")
    w("")
    w("## 1. 시장 상태 (그날 종가까지)")
    w("| | 날짜 | 종가 | 1년 최고가 대비 (최고가 날) | 그 뒤 가장 낮은 날 (최고가 대비) | 가장 낮은 날 대비 | 1일 | 5일 | 20일 | 최근 10거래일 가장 큰 상승 · 하락 | 오늘이 '반등 날'? |")
    w("|---|---|---|---|---|---|---|---|---|---|---|")
    for m in E["market"]:
        w(f"| {m['name']} | {m['date']} | {m['close']:,} | {m['from_high']}% ({m['high_date']}) | {m['low_date']} ({m['low_from_high']}%) | +{m['from_low']}% | {m['d1']}% | {m['d5']}% | {m['d20']}% | "
          f"{m['biggest_up_10d'][0]} +{m['biggest_up_10d'][1]}% · {m['biggest_down_10d'][0]} {m['biggest_down_10d'][1]}% | {'예' if m['rebound_day_today'] else '아니오'} |")
    w("")
    w("최근 10거래일 하루 변동: " + " / ".join(f"**{m['name']}** " + " ".join(f"{d[5:]} {c:+.1f}" for d, c in m["last10"]) for m in E["market"][:3]))
    w("")
    if not E.get("summary"):
        return "\n".join(L) + "\n"
    S = E["summary"]
    w(f"## 2. 최근 {E['days']}일 영상 {S['videos']}개 (한국어 · 라이브 뺌 · 주제 밖 뺌) — 뺀 것 {E['dropped']}")
    w("묶음: " + " · ".join(f"{k} {v}" for k, v in sorted(S["groups"].items(), key=lambda x: -x[1])))
    w("")
    w("### 2-1. 제목에 든 말 (그 말이 든 영상 수 · 몫 · 그 영상들의 하루 조회수 가운데 값 — 전체 가운데 값과 견줌)")
    w("| 제목 낱말 | 영상 | 몫 | 하루 조회수 가운데 값 | 전체 가운데 값 |")
    w("|---|---|---|---|---|")
    for t in S["title_words"]:
        w(f"| {t['word']} | {t['n']} | {t['share']:.0%} | {t['median_vpd']:,} | {t['median_vpd_all']:,} |" if t["median_vpd"] is not None else f"| {t['word']} | 0 | 0% | — | {t['median_vpd_all']:,} |")
    w("")
    for title, key, rows in (("### 2-2. 하루 조회수 상위 롱폼 (뉴스·정치 채널 뺌)", "top_long", E["top_long"]), ("### 2-3. 구독자 5만 이하 — 구독자 대비 조회수 상위 롱폼", "top_small", E["top_small"]),
                             ("### 2-4. 오늘·어제 올라온 롱폼 (하루 조회수 순)", "fresh", E["fresh"]), ("### 2-5. 쇼츠 하루 조회수 상위", "top_short", E["top_short"])):
        w(title)
        w("| 하루 조회수 | 조회수 | 구독자 | 배수 | 올린 날 | 채널 | 제목 |")
        w("|---|---|---|---|---|---|---|")
        for r in rows:
            w(f"| {r['views_per_day']:,} | {r['views']:,} | {r['subs'] or 0:,} | {r['ratio'] if r['ratio'] is not None else '—'} | {r['published'][5:]} | {PE.flat(r['channel'], 16)} | {PE.flat(r['title'], 70)} |")
        w("")
    al = S["all"]
    if al:
        w(f"## 3. 이 기간에 쓴 댓글 {al['n']:,}개 (영상 {al['videos']}개 — 공감순·최신순 표본) — 주제별, 10월 수집분과 견줌")
        w("| 주제 | 댓글 | 몫 | 보통 영상 | 댓글당 좋아요 | 묻는 몫 | 10월 수집분 몫(10월에 쓴 댓글) | 그때의 몇 배 | 세계 |")
        w("|---|---|---|---|---|---|---|---|---|")
        pc = lambda x: "—" if x is None else f"{x:.1%}"   # noqa: E731
        for t in S["topics_vs_base"]:
            w(f"| {t['name']} | {t['n']:,} | {t['share']:.1%} | {pc(t['video_median'])} | {t['likes_per']} | {t['ask_share']:.0%} | {pc(t['base_share_oct'])} | {'×' + str(t['vs_oct']) if t['vs_oct'] else '—'} | {t['group']} |")
        w("")
        w("세계별: " + " · ".join(f"**{g['name'].split(' (')[0]}** {g['share']:.1%} (보통 영상 {pc(g['video_median'])})" for g in al["groups"]))
        w("")
        w("묻는 댓글: " + " · ".join(f"{a['name'].split(' — ')[0]} {a['n']}" for a in al["ask_types"][:8]) + f" (묻는 꼴 {al['ask_nonpolitical']:,}개)")
        w("")
        w("### 3-1. 좋아요가 가장 많은 댓글 (이 기간에 쓴 것)")
        for q in al["top_liked"]:
            w(f"- 👍{q['likes']:,} \"{PE.flat(q['text'], 120)}\" — 「{PE.flat(q['title'], 36)}」 · 주제: {', '.join(q['topics']) or '없음'}")
        w("")
        w("### 3-2. 주제마다 좋아요 많은 댓글")
        for t in S["topics_vs_base"]:
            w(f"- **{t['name']}**: " + " / ".join(f"👍{q['likes']} \"{PE.flat(q['text'], 110)}\"" for q in t["samples"]))
        w("")
        w("### 3-3. 묻는 댓글 보기")
        for a in al["ask_types"][:8]:
            if a["samples"]:
                w(f"- **{a['name']}** ({a['n']}): " + " / ".join(f"👍{q['likes']} \"{PE.flat(q['text'], 110)}\"" for q in a["samples"]))
        w("")
        w("### 3-4. 오늘·어제 쓴 댓글 가운데 좋아요 많은 것")
        for q in E["fresh_comments"]:
            w(f"- {q['day'][5:]} 👍{q['likes']:,} \"{PE.flat(q['text'], 130)}\" — 「{PE.flat(q['title'], 30)}」")
    return "\n".join(L) + "\n"


def selftest() -> int:
    rows = [(f"2026-01-{i:02d}" if i <= 31 else f"2026-02-{i - 31:02d}", p) for i, p in enumerate([100.0] * 58 + [80.0, 70.0, 73.0], 1)]
    m = market_one("x", rows)
    assert m["from_high"] == -27.0 and m["low_from_high"] == -30.0 and m["from_low"] == 4.3 and m["d1"] == 4.3 and m["rebound_day_today"] is True, m     # 전날 −30% · 오늘 +4.3%
    assert m["streak"] == 1 and m["biggest_down_10d"][1] == -20.0 and market_one("y", rows[:10]) is None
    m2 = market_one("z", rows[:-1] + [(rows[-1][0], 71.0)])
    assert m2["rebound_day_today"] is False                                                           # +1.4% 는 반등 날 아님
    assert iso_seconds("PT1H2M3S") == 3723 and iso_seconds("PT45S") == 45
    cfg = {"exclude": {"OFF": {}, "EVENT": {}, "_NEWS_CHANNEL": re.compile("KBS"), "_POLITICS_TITLE": re.compile("대통령"), "_OFF_TITLE": re.compile("영화")}}
    now = datetime(2026, 11, 10, 12, tzinfo=timezone.utc)
    it = {"id": "v1", "snippet": {"title": "코스피 폭락 뒤 반등", "channelTitle": "c", "channelId": "ch", "publishedAt": "2026-11-09T12:00:00Z"},
          "statistics": {"viewCount": "1000", "commentCount": "50"}, "contentDetails": {"duration": "PT8M"}}
    r = video_row(it, {"ch": 500}, now, cfg)
    assert r["views_per_day"] == 1000 and r["ratio"] == 2.0 and r["kind"] == "long" and r["age_days"] == 1.0, r
    assert video_row({**it, "snippet": {**it["snippet"], "title": "Stock market crash"}}, {}, now, cfg) == {"drop": "not_korean"}
    assert video_row({**it, "liveStreamingDetails": {}}, {}, now, cfg) is not None and video_row({**it, "liveStreamingDetails": {"a": 1}}, {}, now, cfg) == {"drop": "live"}
    print("[SELFTEST] ok — market_one(반등 날·최고가 대비·연속)·iso_seconds·video_row(하루 조회수·배수·한국어·라이브)")
    return 0


def main(argv: list[str]) -> int:
    if "--selftest" in argv:
        return selftest()
    ap = argparse.ArgumentParser()
    ap.add_argument("topic"); ap.add_argument("--days", type=int, default=7); ap.add_argument("--videos", type=int, default=30); ap.add_argument("--small", type=int, default=10)
    ap.add_argument("--quota", type=int, default=2500); ap.add_argument("--market-only", action="store_true")
    a = ap.parse_args(argv)
    t0 = time.time()
    now = datetime.now(timezone.utc)
    cfg = PE.load_cfg(a.topic)
    date = now.astimezone(timezone(timedelta(hours=9))).strftime("%Y-%m-%d")
    out_dir = ROOT / a.topic / "result" / "trend"
    out_dir.mkdir(parents=True, exist_ok=True)
    E = {"tool": f"trend_scan.py {VERSION}", "topic": a.topic, "date": date, "days": a.days, "made": now.strftime("%Y-%m-%dT%H:%M:%SZ"), "units": 0, "market": market(cfg)}
    if not a.market_only:
        import outlier_research as orr  # noqa: E402
        import pc_analysis as pc        # noqa: E402
        key = os.environ.get("YOUTUBE_API_KEY")
        if not key:
            log("FAIL", logging.ERROR, stage="auth", missing="YOUTUBE_API_KEY", next="환경 변수에 키를 넣거나 --market-only")
            return 2
        api = orr.Api(key, a.quota, ledger=pc.KeyLedger(key), what="trend_scan", topic=a.topic)
        rows, dropped = scan(api, cfg, a.days, now)
        targets = pick_targets(rows, a.videos, a.small)
        since = (now - timedelta(days=a.days)).strftime("%Y-%m-%d")
        core, cdrop = comments(api, targets, cfg, since)
        base = None
        bp = ROOT / a.topic / "result" / "outliers" / "persona_evidence.json"
        if bp.exists():
            base = json.loads(bp.read_text(encoding="utf-8")).get("all")
        S = summarize(rows, core, cfg, base)
        V = {r["id"]: r for r in rows}
        longs = [r for r in rows if r["kind"] == "long" and r["g"] != "N_news"]
        y = (now - timedelta(days=1.5)).strftime("%Y-%m-%dT%H:%M:%SZ")
        day1 = (now - timedelta(days=1)).strftime("%Y-%m-%d")
        E.update({"units": api.used, "dropped": dropped, "comment_dropped": cdrop, "summary": S,
                  "top_long": sorted(longs, key=lambda r: -r["views_per_day"])[:30],
                  "top_small": [r for r in sorted(longs, key=lambda r: -(r["ratio"] or 0)) if r["subs"] and r["subs"] <= 50000][:20],
                  "fresh": sorted([r for r in longs if r["published_at"] >= y], key=lambda r: -r["views_per_day"])[:25],
                  "top_short": sorted([r for r in rows if r["kind"] == "short" and r["g"] != "N_news"], key=lambda r: -r["views_per_day"])[:15],
                  "fresh_comments": [{"day": c[6], "likes": c[3], "text": c[4], "title": V[c[0]]["title"]} for c in sorted((c for c in core if c[6] >= day1), key=lambda c: -c[3])[:25]],
                  "targets": [r["id"] for r in targets]})
        with (out_dir / f"comments_{date}.jsonl").open("w", encoding="utf-8") as f:          # 작성자 이름·채널 ID 없음
            for c in core:
                f.write(json.dumps({"video": c[0], "likes": c[3], "day": c[6], "text": c[4]}, ensure_ascii=False) + "\n")
        (out_dir / f"videos_{date}.json").write_text(json.dumps(rows, ensure_ascii=False, indent=0), encoding="utf-8")
    (out_dir / f"trend_{date}.md").write_text(render(E), encoding="utf-8")
    slim = {k: v for k, v in E.items()}
    (out_dir / f"trend_{date}.json").write_text(json.dumps(slim, ensure_ascii=False, indent=1, default=str), encoding="utf-8")
    log("DONE", md=str((out_dir / f"trend_{date}.md").relative_to(ROOT)), units=E["units"], sec=round(time.time() - t0, 1))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
