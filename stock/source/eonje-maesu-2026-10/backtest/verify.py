# -*- coding: utf-8 -*-
# VERSION: v2.0 — 2026-10-16 — run.py v3.0 을 따로 다시 계산 (엔진·자료 모듈을 쓰지 않음): Yahoo 캐시 CSV 를 직접 읽어 총수익·지표·신호·
#          '최고점 −10% 다음 날 매도'를 손으로 짠 반복문으로 다시 돌리고 results.json 의 끝 값·거래 날짜와 맞춰 본다.
#          (v1.0 — v1 관망 비교용 — stock/source/_old/eonje-maesu-2026-10-v1/backtest/verify.py)
"""python3 stock/source/eonje-maesu-2026-10/backtest/verify.py   → 맞으면 [VERIFY] ok, 다르면 멈춤 (연구·교육용)."""
import csv
import json
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE.parents[3] / "stock" / "data"
R = json.loads((HERE / "results.json").read_text("utf-8"))
START, END = R["params"]["start"], R["params"]["end"]
COST, TRAIL, CAP = R["params"]["cost"], R["params"]["trail"], R["params"]["capital"]


def read(sym):
    rows = list(csv.DictReader(open(DATA / f"yahoo_{sym}_daily.csv", encoding="utf-8")))
    return [r["date"][:10] for r in rows], [float(r["close"]) for r in rows], [float(r["div"]) for r in rows]


dates, close, div = read("spy")
vd, vc, _ = read("vix")
vix_map = dict(zip(vd, vc))
n = len(close)
tr = [1.0] * n
for i in range(1, n):
    tr[i] = tr[i - 1] * (close[i] + div[i]) / close[i - 1]


def sma(k):
    out, run = [None] * n, 0.0
    for i in range(n):
        run += close[i]
        if i >= k:
            run -= close[i - k]
        if i >= k - 1:
            out[i] = run / k
    return out


def rsi(k=14):
    out = [None] * n
    gains = [max(close[i] - close[i - 1], 0) for i in range(1, n)]
    losses = [max(close[i - 1] - close[i], 0) for i in range(1, n)]
    ag, al = sum(gains[:k]) / k, sum(losses[:k]) / k
    out[k] = 100.0 if al == 0 else 100 - 100 / (1 + ag / al)
    for i in range(k + 1, n):
        ag = (ag * (k - 1) + gains[i - 1]) / k
        al = (al * (k - 1) + losses[i - 1]) / k
        out[i] = 100.0 if al == 0 else 100 - 100 / (1 + ag / al)
    return out


s50, s200, r14 = sma(50), sma(200), rsi()
ath, m = [], 0.0
for c in close:
    m = max(m, c)
    ath.append(m)
EPS = 1e-12


def sig(rule, d):
    c = close[d]
    if rule == "m1":
        return d + 1 < n and dates[d + 1][:7] != dates[d][:7]
    if rule == "dip10":
        return c <= 0.9 * ath[d] * (1 + EPS)
    if rule == "dip20":
        return c <= 0.8 * ath[d] * (1 + EPS)
    if rule == "drop2":
        return d >= 1 and c / close[d - 1] - 1 <= -0.02 + EPS
    if rule == "vix30":
        v = vix_map.get(dates[d])
        return v is not None and v >= 30 - EPS
    if rule == "rsi30":
        return r14[d] is not None and r14[d] < 30
    if rule == "ma200":
        return d >= 1 and s200[d - 1] is not None and close[d - 1] <= s200[d - 1] and c > s200[d]
    if rule == "gc":
        return d >= 1 and s200[d - 1] is not None and s50[d - 1] <= s200[d - 1] and s50[d] > s200[d]
    if rule == "hi52":
        return d >= 252 and c > max(close[d - 252:d])
    if rule == "mom12":
        return d >= 252 and c > close[d - 252]
    raise KeyError(rule)


s = next(i for i, x in enumerate(dates) if x >= START)
e = max(i for i, x in enumerate(dates) if x <= END)
bad = 0
for rule in R["params"]["rules"]:
    cash, units, peak, want_buy, want_sell, buys = CAP, 0.0, 0.0, sig(rule, s - 1), False, []
    for d in range(s, e + 1):
        if want_buy:
            units, cash, peak, want_buy = cash * (1 - COST) / tr[d], 0.0, close[d], False
            buys.append(dates[d])
        elif want_sell:
            cash, units, want_sell = units * tr[d] * (1 - COST), 0.0, False
        if units and d < e:
            peak = max(peak, close[d])
            if close[d] <= (1 - TRAIL) * peak * (1 + EPS):
                want_sell = True
        if not units and not want_buy and d < e and sig(rule, d):
            want_buy = True
    final = cash + units * tr[e]
    got = R["rules"][rule]["final"]
    their = [t["buy_date"] for t in R["trades"][rule]]
    ok = math.isclose(final, got, rel_tol=1e-9) and buys == their
    bad += not ok
    print(f"[VERIFY] rule={rule} final_engine={got:,.2f} final_again={final:,.2f} buys={len(buys)} same_buy_dates={buys == their} {'ok' if ok else 'DIFF'}")
units = CAP * (1 - COST) / tr[s]
bh = units * tr[e]
okbh = math.isclose(bh, R["buy_and_hold"]["final"], rel_tol=1e-9)
print(f"[VERIFY] buy_and_hold engine={R['buy_and_hold']['final']:,.2f} again={bh:,.2f} {'ok' if okbh else 'DIFF'}")
if bad or not okbh:
    sys.exit("[VERIFY] 다름 → 엔진·자료 확인")
print("[VERIFY] ok — 10개 규칙 끝 값·매수 날짜 + BUY & HOLD 가 따로 다시 계산한 값과 같음")
