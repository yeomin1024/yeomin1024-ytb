#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-10-29 — 재무 둘째 묶음 `fundamentals2` → bulk/fa2/ (빚·영업이익·이자 비용·영업현금흐름·잉여현금·현금) — 재무제표 편을 '리스크를 줄이며 안정적 수익' 기준으로
#          다시 짜며 경고 신호(빚을 감당할 힘·매출 방향)를 503곳으로 확인하려고 (사용자 지시 2026-10-29 "기존 3건 … 리스크를 줄이면서 안정적 수익내는걸 기준으로 해서 다시 구성해봐").
# (v1.0 — 2026-10-29 — 최초. 정답 미리 확인 2회차 (사용자 지시 2026-10-29 "주식 주제 평가판 평가했는데 다시 주제 탐색해봐") —
#          실제 종목 주제(편입·분할·작년 1등·10배 종목·배당률 상위·이익과 주가)를 계산하려고 S&P 500 현재 구성 종목을 한꺼번에 받는다.
#
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.1 | 2026-10-29 | fundamentals2 (FA2_TYPES → bulk/fa2/) | fundamentals · main |
# | v1.0 | 2026-10-29 | 최초 — 구성 종목 목록 · 종목마다 일별 주가(배당·분할) · 연간 재무(매출·순이익·희석 EPS) 캐시 | 전부 |
#
# 실행: python3 -B stock/topics/precheck/bulk.py prices        (bulk/px/<기호>.csv 가 있으면 건너뜀 — 처음 한 번 약 5분)
#       python3 -B stock/topics/precheck/bulk.py fundamentals  (bulk/fa/<기호>.json)
#       python3 -B stock/topics/precheck/bulk.py fundamentals2 (bulk/fa2/<기호>.json — 빚·영업이익·이자 비용·현금흐름, v1.1)
# 자료: 구성 종목 = github.com/datasets/s-and-p-500-companies data/constituents.csv (지금 구성 · 'Date added' 편입일)
#       주가 = Yahoo Finance chart API v8 (close · adjclose · 배당 · 분할) · 재무 = Yahoo fundamentals-timeseries (연간 약 4년)
# ⚠ 생존 편향: 지금 S&P 500 에 있는 회사만 — 그사이 빠진·망한 회사는 없음. 주제마다 편향이 결론을 어느 쪽으로 미는지 precheck.py 가 적는다.
# 캐시 bulk/ 는 git 에 넣지 않음 (.gitignore — 약 500 종목 × 일별 26년). 목록·받은 날·행 수는 bulk_manifest.json 으로 올림.
# ※ 연구·교육용 — 투자 권유가 아님.
import csv
import json
import logging
import sys
import time
import urllib.parse
import urllib.request
from datetime import date, datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
BULK = HERE / "bulk"
LIST_URL = "https://raw.githubusercontent.com/datasets/s-and-p-500-companies/main/data/constituents.csv"
VERSION = "v1.1"
SLEEP = 0.3

logging.basicConfig(level=logging.INFO, format="[%(stage)s] [%(asctime)s] %(message)s", datefmt="%Y-%m-%dT%H:%M:%S")
log = logging.getLogger("bulk")


def out(stage, lvl=logging.INFO, **kv):
    log.log(lvl, " ".join(f"{k}={v}" for k, v in kv.items()), extra={"stage": stage})


def get(url, tries=(0, 2, 4, 8, 16)):
    last = None
    for w in tries:
        time.sleep(w)
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except Exception as e:  # 429·네트워크 — 기다렸다 다시
            last = e
            out("FETCH", logging.WARNING, url=url[:90], error=repr(e)[:100], retry_after=w * 2 or 2)
    raise RuntimeError(f"받기 실패 url={url[:90]} error={last!r} — 다음: 잠시 뒤 다시 실행 (받은 것은 건너뜀)")


def constituents(refetch=False):
    path = BULK / "constituents.csv"
    if refetch or not path.exists():
        BULK.mkdir(parents=True, exist_ok=True)
        path.write_bytes(get(LIST_URL))
    with path.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    out("LOAD", source="constituents.csv", rows=len(rows), modified=datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc).date())
    return rows


def ysym(s):
    return s.replace(".", "-")


def prices(sym, start=date(1999, 1, 1)):
    path = BULK / "px" / f"{sym}.csv"
    if path.exists():
        return "cached"
    p1 = int(datetime(start.year, start.month, start.day, tzinfo=timezone.utc).timestamp())
    url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(ysym(sym))}"
           f"?period1={p1}&period2={int(time.time())}&interval=1d&events=div%2Csplit")
    res = json.loads(get(url))["chart"]["result"][0]
    ts_ = res.get("timestamp") or []
    q = res["indicators"]["quote"][0]
    adj = res["indicators"].get("adjclose", [{}])[0].get("adjclose", q["close"])
    ev = res.get("events", {})
    day = lambda k: datetime.fromtimestamp(int(k), tz=timezone.utc).date().isoformat()  # noqa: E731
    divs = {day(k): v["amount"] for k, v in ev.get("dividends", {}).items()}
    spl = {day(k): v["numerator"] / v["denominator"] for k, v in ev.get("splits", {}).items() if v.get("denominator")}
    path.parent.mkdir(parents=True, exist_ok=True)
    n = 0
    with path.open("w", encoding="utf-8", newline="") as f:
        f.write(f"# {sym} 일별 — Yahoo chart v8 (close·adjclose·div·split 비율) {date.today().isoformat()} 받음 · bulk.py {VERSION}\n")
        w = csv.writer(f)
        w.writerow(["date", "close", "adjclose", "volume", "div", "split"])
        for t, c, a, v in zip(ts_, q["close"], adj, q.get("volume") or [None] * len(ts_)):
            if c is None or a is None:
                continue
            d_ = day(t)
            w.writerow([d_, f"{c:.6f}", f"{a:.6f}", v or "", divs.get(d_, ""), spl.get(d_, "")])
            n += 1
    return n


FA_TYPES = ["annualTotalRevenue", "annualNetIncome", "annualDilutedEPS", "annualDilutedAverageShares", "annualStockholdersEquity",
            "annualRepurchaseOfCapitalStock", "annualCashDividendsPaid"]


FA2_TYPES = ["annualTotalDebt", "annualOperatingIncome", "annualEBIT", "annualInterestExpense", "annualOperatingCashFlow",
             "annualFreeCashFlow", "annualCashAndCashEquivalents"]


def fundamentals2(sym):
    return fundamentals(sym, FA2_TYPES, "fa2")


def fundamentals(sym, types=None, sub="fa"):
    types = types or FA_TYPES
    path = BULK / sub / f"{sym}.json"
    if path.exists():
        return "cached"
    url = (f"https://query1.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/timeseries/{urllib.parse.quote(ysym(sym))}"
           f"?type={','.join(types)}&period1=946684800&period2={int(time.time()) + 86400 * 400}")
    res = json.loads(get(url))["timeseries"]["result"]
    o = {}
    for r in res:
        t = r["meta"]["type"][0]
        o[t] = {x["asOfDate"]: x["reportedValue"]["raw"] for x in (r.get(t) or []) if x}
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({"symbol": sym, "fetched": date.today().isoformat(), "series": o}, ensure_ascii=False), "utf-8")
    return sum(len(v) for v in o.values())


def main(argv):
    what = argv[1] if len(argv) > 1 else "prices"
    rows = constituents()
    fn = {"prices": prices, "fundamentals": fundamentals, "fundamentals2": fundamentals2}[what]
    done = fail = cached = 0
    t0 = time.time()
    failed = []
    for i, r in enumerate(rows):
        s = r["Symbol"]
        try:
            n = fn(s)
            if n == "cached":
                cached += 1
                continue
            done += 1
            time.sleep(SLEEP)
        except Exception as e:
            fail += 1
            failed.append(s)
            out("FETCH", logging.ERROR, symbol=s, error=repr(e)[:160], next_step="다시 실행하면 이것만 받음")
        if (i + 1) % 50 == 0:
            out("FETCH", kind=what, progress=f"{i + 1}/{len(rows)}", fetched=done, cached=cached, failed=fail, sec=round(time.time() - t0))
    man = HERE / "bulk_manifest.json"
    M = json.loads(man.read_text("utf-8")) if man.exists() else {}
    M[what] = {"made": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "list": LIST_URL, "symbols": len(rows),
               "fetched": done, "cached": cached, "failed": failed, "tool": f"bulk.py {VERSION}"}
    man.write_text(json.dumps(M, ensure_ascii=False, indent=1), "utf-8")
    out("DONE", kind=what, symbols=len(rows), fetched=done, cached=cached, failed=len(failed), sec=round(time.time() - t0))


if __name__ == "__main__":
    main(sys.argv)
