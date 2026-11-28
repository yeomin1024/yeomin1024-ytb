#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0.1 — 2026-11-28 — 받기 실패한 기호는 지난 요약을 남김 (market.json 을 빈 것으로 덮지 않음).
# 이전 v1.0 — 2026-11-28 — 최초. 주식 시장 일별 숫자(지수·VIX·환율·대표 종목 종가) → <주제>/result/next_topic/market/ — 성공 사례가 '어떤 시장
#          날'에 올라왔는지(시기)와 시청자 심리를 맞춰 보려고. 사용자 지시 2026-11-28 "시기에 맞는 주제를 찾는게 지금 너가 할일이야 매일 변화하는
#          주식시장이 변화하고 그에 따라 시청자들이 어떤 심리여서 무슨 영상을 찾게되는지 이걸 너가 분석해서 파악해야 한다고".
#          자료 = Yahoo Finance 차트 API (query1.finance.yahoo.com — 이 환경 허용 목록에 2026-11-28 더함 · 키 없음 · 할당량 없음).
#
# CHANGELOG
#   v1.0 2026-11-28  fetch · show · selftest. 날짜 = 그 거래소 현지 날짜 (미국 지수 = 뉴욕, 코스피 = 서울). 한국 시각 대응은 쓰는 쪽에서
#                    (미국 장 마감 = 한국 다음 날 05~06시).
#   v1.0.1 2026-11-28  fetch — 실패한 기호는 지난 market.json 요약을 그대로 남기고 `stale` 에 적음 (CSV 는 원래 안 건드림).
#                    까닭: 허용 목록에 Yahoo 가 없는 환경('스톡롱런')에서 12개 모두 403 → market.json symbols={} 로 덮여
#                    daily_topic.py 시장 표가 비었음 (2026-11-28 21:26 KST). 함수 merge_summary · selftest 1줄 더함.
#
# 쓰는 법
#   python3 tools/market_data.py stock fetch [--range 1y]    # 기호마다 CSV + market.json (요약)
#   python3 tools/market_data.py stock show                   # 최근 20 거래일 표
#   python3 tools/market_data.py selftest
#
# 연구·교육용 — 투자 조언이 아님. 값은 Yahoo 가 주는 종가(close) 그대로 (배당·분할 보정 안 함).
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import logging
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

VERSION = "v1.0.1"
ROOT = Path(__file__).resolve().parent.parent
KST = dt.timezone(dt.timedelta(hours=9))
# 기호 → (이름, 묶음). 묶음: us = 미국 지수 · kr = 한국 · risk = 공포·환율 · stock = 대표 종목·ETF
SYMBOLS = {
    "^GSPC": ("S&P500", "us"), "^IXIC": ("나스닥", "us"), "^SOX": ("필라델피아 반도체", "us"),
    "^KS11": ("코스피", "kr"), "005930.KS": ("삼성전자", "kr"), "000660.KS": ("SK하이닉스", "kr"),
    "^VIX": ("VIX 공포지수", "risk"), "KRW=X": ("원/달러 환율", "risk"),
    "SOXL": ("SOXL", "stock"), "TQQQ": ("TQQQ", "stock"), "NVDA": ("엔비디아", "stock"), "TSLA": ("테슬라", "stock"),
}
API = "https://query1.finance.yahoo.com/v8/finance/chart/{sym}?range={rng}&interval=1d&includePrePost=false"
UA = "Mozilla/5.0 (research script)"


def log(stage: str, level: int = logging.INFO, **kv) -> None:
    ts = dt.datetime.now(KST).isoformat(timespec="seconds")
    logging.log(level, f"[{stage}] [{ts}] " + " ".join(f"{k}={v}" for k, v in kv.items()))


def out_dir(topic: str) -> Path:
    return ROOT / topic / "result/next_topic/market"


def parse_chart(j: dict) -> list[dict]:
    """Yahoo chart JSON → [{date, close}] (현지 날짜 · close 없는 날 뺌)."""
    res = ((j or {}).get("chart") or {}).get("result") or []
    if not res:
        return []
    r = res[0]
    off = int((r.get("meta") or {}).get("gmtoffset") or 0)
    ts = r.get("timestamp") or []
    q = (((r.get("indicators") or {}).get("quote")) or [{}])[0]
    closes = q.get("close") or []
    out = []
    for t, c in zip(ts, closes):
        if c is None:
            continue
        d = dt.datetime.fromtimestamp(t + off, dt.timezone.utc).date().isoformat()
        out.append({"date": d, "close": round(float(c), 4)})
    seen, uniq = set(), []                                    # 같은 날 두 번(장중 마지막 봉) 이면 뒤 것
    for x in reversed(out):
        if x["date"] not in seen:
            seen.add(x["date"])
            uniq.append(x)
    return list(reversed(uniq))


def with_returns(rows: list[dict]) -> list[dict]:
    prev = None
    for x in rows:
        x["chg"] = round((x["close"] / prev - 1) * 100, 2) if prev else None
        prev = x["close"]
    hi = None
    for x in rows:                                            # 고점 대비 (지금까지 가장 높은 종가)
        hi = x["close"] if hi is None else max(hi, x["close"])
        x["from_high"] = round((x["close"] / hi - 1) * 100, 2)
    return rows


def fetch_one(sym: str, rng: str) -> list[dict]:
    url = API.format(sym=urllib.parse.quote(sym, safe=""), rng=rng)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return with_returns(parse_chart(json.loads(r.read().decode("utf-8"))))


def merge_summary(old: dict, new: dict, bad: list[str]) -> tuple[dict, list[str]]:
    """새로 받은 요약 + 실패한 기호는 지난 요약 그대로 (v1.0.1). 돌려줌 = (합친 요약, 지난 것을 남긴 기호)."""
    merged, stale = dict(new), []
    for sym in bad:
        if sym in (old or {}) and sym not in merged:
            merged[sym] = dict(old[sym])
            stale.append(sym)
    return merged, stale


def fetch(topic: str, rng: str) -> int:
    t0 = time.time()
    od = out_dir(topic)
    od.mkdir(parents=True, exist_ok=True)
    summary, bad = {}, []
    log("LOAD", topic=topic, source="Yahoo Finance chart API", range=rng, symbols=len(SYMBOLS))
    for sym, (name, grp) in SYMBOLS.items():
        try:
            rows = fetch_one(sym, rng)
        except Exception as e:                                # 한 기호가 실패해도 나머지는 받음 — 무엇이 왜 실패했는지 남김
            bad.append(sym)
            log("LOAD", logging.WARNING, symbol=sym, error=f"{type(e).__name__}: {str(e)[:160]}", next="네트워크 허용 목록(query1.finance.yahoo.com)·기호 확인 뒤 다시")
            continue
        if not rows:
            bad.append(sym)
            log("LOAD", logging.WARNING, symbol=sym, note="자료 없음")
            continue
        fn = sym.replace("^", "").replace("=", "_").replace(".", "_") + ".csv"
        with (od / fn).open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["date", "close", "chg", "from_high"])
            w.writeheader()
            w.writerows(rows)
        chg = [x["chg"] for x in rows if x["chg"] is not None]
        summary[sym] = {"name": name, "group": grp, "file": fn, "first": rows[0]["date"], "last": rows[-1]["date"], "days": len(rows),
                        "last_close": rows[-1]["close"], "last_chg": rows[-1]["chg"], "from_high": rows[-1]["from_high"],
                        "worst_day": min(rows[1:], key=lambda x: x["chg"])["date"] if len(rows) > 1 else None,
                        "worst_chg": min(chg) if chg else None}
        log("LOAD", symbol=sym, name=name, rows=len(rows), first=rows[0]["date"], last=rows[-1]["date"], last_chg=rows[-1]["chg"], from_high=rows[-1]["from_high"])
        time.sleep(0.4)                                       # 차트 API 를 몰아서 부르지 않게
    mp = od / "market.json"
    try:
        old = json.loads(mp.read_text("utf-8")).get("symbols") or {} if mp.is_file() else {}
    except (json.JSONDecodeError, OSError) as e:
        old = {}
        log("LOAD", logging.WARNING, note="지난 market.json 읽기 실패 — 새로 받은 것만 씀", error=f"{type(e).__name__}: {str(e)[:120]}")
    merged, stale = merge_summary(old, summary, bad)
    if stale:
        log("LOAD", logging.WARNING, note="받기 실패한 기호는 지난 숫자를 남김", stale=",".join(stale),
            last=",".join(sorted({merged[s]["last"] for s in stale})), next="허용 목록에 query1.finance.yahoo.com 있는 환경에서 다시")
    mp.write_text(json.dumps({"updated": dt.datetime.now(KST).isoformat(timespec="seconds"), "tool": f"market_data.py {VERSION}",
                              "source": "Yahoo Finance chart API (close · 현지 날짜)", "range": rng, "symbols": merged, "failed": bad, "stale": stale},
                             ensure_ascii=False, indent=1) + "\n", "utf-8")
    log("DONE", topic=topic, ok=len(summary), stale=len(stale), failed=",".join(bad) or "-", dir=str(od.relative_to(ROOT)), sec=round(time.time() - t0, 1))
    return 0 if summary else 1


def load(topic: str) -> dict[str, dict[str, dict]]:
    """{기호: {날짜: {close, chg, from_high}}} — 받은 CSV 에서."""
    od = out_dir(topic)
    meta = json.loads((od / "market.json").read_text("utf-8")) if (od / "market.json").is_file() else {"symbols": {}}
    out = {}
    for sym, m in meta["symbols"].items():
        p = od / m["file"]
        if p.is_file():
            out[sym] = {r["date"]: {"close": float(r["close"]), "chg": float(r["chg"]) if r["chg"] else None, "from_high": float(r["from_high"])}
                        for r in csv.DictReader(p.open(encoding="utf-8"))}
    return out


def show(topic: str, days: int = 20) -> int:
    M = load(topic)
    if not M:
        log("SHOW", logging.WARNING, note="자료 없음 — fetch 먼저")
        return 1
    dates = sorted(M.get("^GSPC", {}))[-days:]
    cols = [s for s in ("^GSPC", "^IXIC", "^SOX", "^KS11", "^VIX", "KRW=X", "SOXL") if s in M]
    print("| 날짜 | " + " | ".join(SYMBOLS[s][0] for s in cols) + " |")
    print("|---|" + "---|" * len(cols))
    for d in dates:
        cells = []
        for s in cols:
            x = M[s].get(d)
            cells.append("–" if not x else (f"{x['close']:.1f}" if s == "^VIX" else f"{x['chg']:+.1f}%" if x["chg"] is not None else "–"))
        print(f"| {d} | " + " | ".join(cells) + " |")
    return 0


def selftest() -> int:
    ok = True

    def check(name, cond):
        nonlocal ok
        print(("PASS " if cond else "FAIL ") + name)
        ok = ok and bool(cond)
    j = {"chart": {"result": [{"meta": {"gmtoffset": -18000}, "timestamp": [1763643600, 1763730000, 1763730000 + 3600],
                                "indicators": {"quote": [{"close": [100.0, None, 90.0]}]}}]}}
    rows = with_returns(parse_chart(j))
    check("현지 날짜 · close 없는 봉 뺌", [r["date"] for r in rows] == ["2025-11-20", "2025-11-21"] and rows[1]["close"] == 90.0)
    check("하루 변화·고점 대비", rows[1]["chg"] == -10.0 and rows[1]["from_high"] == -10.0 and rows[0]["chg"] is None)
    check("빈 응답", parse_chart({}) == [] and parse_chart({"chart": {"result": []}}) == [])
    m, st_ = merge_summary({"A": {"last": "2026-11-27"}, "B": {"last": "2026-11-27"}}, {"A": {"last": "2026-11-30"}}, ["B", "C"])
    check("실패 기호는 지난 요약 남김 (v1.0.1)", m["A"]["last"] == "2026-11-30" and m["B"]["last"] == "2026-11-27" and "C" not in m and st_ == ["B"])
    print("selftest:", "OK" if ok else "FAIL")
    return 0 if ok else 1


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="주식 시장 일별 숫자 (Yahoo Finance 차트)")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    ap.add_argument("topic", nargs="?", default="stock")
    ap.add_argument("cmd", nargs="?", default="fetch", choices=["fetch", "show", "selftest"])
    ap.add_argument("--range", default="1y", help="1mo·3mo·6mo·1y·2y (기본 1y)")
    a = ap.parse_args(argv)
    logging.basicConfig(level=getattr(logging, a.log_level), format="%(message)s", stream=sys.stdout)
    if a.topic == "selftest" or a.cmd == "selftest":
        return selftest()
    return fetch(a.topic, a.range) if a.cmd == "fetch" else show(a.topic)


if __name__ == "__main__":
    raise SystemExit(main())
