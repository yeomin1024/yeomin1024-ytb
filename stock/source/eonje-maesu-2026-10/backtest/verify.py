#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-16 — 최초. run.py 결과를 엔진(daily.py 상태 기계)과 따로 쓴 계산으로 다시 낸다 (사용자 선호: 정확성·추적 가능성 먼저).
"""cd stock/source/eonje-maesu-2026-10/backtest && python3 verify.py

엔진 클래스를 쓰지 않고 규칙 글(run.py 머리말)만 보고 다시 쓴 계산으로 본 실험 끝 값·매수·매도 횟수를 다시 내서 results.json 과 맞춘다.
  - 사고팔기 반복 7개: 날마다 '보유 여부'를 반복문으로 정하고 (d 종가 판단 → d+1 종가 거래), 끝 값 = 비용 × 보유 구간 총수익 곱
  - 사는 방법 3개 + 관망: 산 날·금액을 규칙대로 다시 정해 끝 값을 낸다
차이가 1e-9(상대)를 넘으면 실패로 끝낸다.
"""
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[3] / "tools"))
from backtest import data as bd  # noqa: E402
from backtest import daily as dl  # noqa: E402

CAP, COST = 10_000.0, 0.001


def series():
    close, _ = bd.sp500_daily_long()
    mon, meta = bd.sp500_monthly()
    end = pd.Timestamp(meta["dividend_until"]) + pd.offsets.MonthEnd(0)
    c = close.loc[:end]
    tr = dl.tr_index_daily(c, mon["dividend"].dropna())
    return c, tr


def inout_positions(key, p, idx, s, e):
    """보유 여부 h[d] = d 종가 거래 뒤 보유 중인가. 판단은 d-1 종가까지 (시작일 s 는 s-1 까지)."""
    n = len(p)
    sma = lambda k: pd.Series(p).rolling(k).mean().to_numpy()                 # noqa: E731
    s50, s200 = sma(50), sma(200)
    hi55 = pd.Series(p).shift(1).rolling(55).max().to_numpy()
    lo20 = pd.Series(p).shift(1).rolling(20).min().to_numpy()
    # RSI (와일더) — 직접
    d_ = np.diff(p)
    up, dn = np.clip(d_, 0, None), np.clip(-d_, 0, None)
    rsi = np.full(n, np.nan)
    au, ad = up[:14].mean(), dn[:14].mean()
    rsi[14] = 100 - 100 / (1 + au / ad)
    for i in range(15, n):
        au = (au * 13 + up[i - 1]) / 14
        ad = (ad * 13 + dn[i - 1]) / 14
        rsi[i] = 100 - 100 / (1 + au / ad) if ad else 100.0
    months = idx.to_period("M")
    is_me = np.r_[months[1:] != months[:-1], False]
    me = np.where(is_me)[0]
    mom_sig = np.full(n, np.nan)
    for j in range(12, len(me)):
        mom_sig[me[j]] = 1.0 if p[me[j]] > p[me[j - 12]] else 0.0
    h = np.zeros(n, bool)
    hold = False
    ref = None
    entry = None
    last_mom = np.nan
    for j in range(len(me)):
        if me[j] < s - 1 and not np.isnan(mom_sig[me[j]]):
            last_mom = mom_sig[me[j]]
    for d in range(s, e + 1):
        q = d - 1                                                              # 판단 날
        want = hold
        if key == "sma200":
            want = p[q] > s200[q]
        elif key == "gc50_200":
            want = s50[q] > s200[q]
        elif key == "mom12":
            if d == s:
                want = bool(last_mom == 1.0)
            elif is_me[q]:
                want = bool(mom_sig[q] == 1.0)
        elif key == "brk55_20":
            if d > s:
                want = (p[q] > hi55[q]) if not hold else not (p[q] < lo20[q])
            else:
                want = False
        elif key == "rsi30_70":
            if d > s:
                want = (rsi[q] < 30) if not hold else not (rsi[q] > 70)
            else:
                want = False
        elif key == "stop10":
            if d == s:
                want = True
            elif hold:
                ref = max(ref, p[q])
                want = not (p[q] <= 0.9 * ref * (1 + 1e-12))
            else:
                ref = min(ref, p[q])
                want = p[q] >= 1.1 * ref * (1 - 1e-12)
        elif key == "tp10":
            if d == s:
                want = True
            elif hold:
                want = not (p[q] >= 1.1 * entry * (1 - 1e-12))
            else:
                ref = max(ref, p[q])
                want = p[q] <= 0.9 * ref * (1 + 1e-12)
        if want != hold:                                                       # d 종가에 거래
            hold = want
            if key in ("stop10", "tp10"):
                ref = p[d]
                if hold:
                    entry = p[d]
        h[d] = hold
    return h


def wealth_inout(h, tr, s, e):
    w = CAP
    trades = 0
    prev = False
    for d in range(s, e + 1):
        if d > s and prev:
            w *= tr[d] / tr[d - 1]
        if h[d] != prev:
            w *= 1 - COST
            trades += 1
        prev = h[d]
    return w, trades


def main():
    c, trs = series()
    p, tr, idx = c.to_numpy(), trs.to_numpy(), c.index
    s = int(idx.searchsorted(pd.Timestamp("1991-01-02")))
    e = int(idx.searchsorted(pd.Timestamp("2023-06-30"), side="right") - 1)
    res = json.loads((HERE / "results.json").read_text("utf-8"))["main"]
    bad = 0
    out = []
    for key in ("stop10", "tp10", "sma200", "gc50_200", "brk55_20", "rsi30_70", "mom12"):
        h = inout_positions(key, p, idx, s, e)
        w, n = wealth_inout(h, tr, s, e)
        st = res[key]["stats"]
        ok = abs(w / st["final"] - 1) < 1e-9 and n == st["buys"] + st["sells"]
        bad += not ok
        out.append((key, w, st["final"], n, st["buys"] + st["sells"], ok))
    # 관망·사는 방법 3개
    ath = np.maximum.accumulate(p)
    w_hold = CAP * (1 - COST) * tr[e] / tr[s]
    q = s - 1
    # dip10: 첫 날(판단 s-1)부터 −10% 인 첫 판단 날 + 1 에 전부
    k = next(d for d in range(s - 1, e) if p[d] <= 0.9 * ath[d] * (1 + 1e-12))
    w_dip = CAP * (1 - COST) * tr[e] / tr[k + 1]
    # ladder: 시작 1/4 + 이미 닿은 단계, 그 뒤 새 단계마다 남은 현금의 몫
    lv = [0.10, 0.20, 0.30]
    units, cash, got = 0.0, CAP, 0
    dd0 = 1 - p[q] / ath[q]
    need = 1 + sum(dd0 >= x - 1e-12 for x in lv)
    buys = []
    amt = cash * need / 4
    units += amt * (1 - COST) / tr[s]
    cash -= amt
    got = need
    buys.append(s)
    for d in range(s, e):
        if got >= 4:
            break
        dd = 1 - p[d] / ath[d]
        nd = max(got, 1 + sum(dd >= x - 1e-12 for x in lv))
        if nd > got:
            amt = cash * (nd - got) / (4 - got)
            units += amt * (1 - COST) / tr[d + 1]
            cash -= amt
            got = nd
            buys.append(d + 1)
    w_lad = units * tr[e] + cash
    # dca12: 시작일 + 그 뒤 11번의 새 달 첫 거래일
    months = idx.to_period("M")
    firsts = [s] + [d for d in range(s + 1, e + 1) if months[d] != months[d - 1]][:11]
    units, cash = 0.0, CAP
    for j, d in enumerate(firsts):
        amt = cash / (12 - j)
        units += amt * (1 - COST) / tr[d]
        cash -= amt
    w_dca = units * tr[e] + cash
    for key, w, nb in (("hold", w_hold, 1), ("dip10", w_dip, 1), ("ladder", w_lad, len(buys)), ("dca12", w_dca, 12)):
        st = res[key]["stats"]
        ok = abs(w / st["final"] - 1) < 1e-9 and nb == st["buys"]
        bad += not ok
        out.append((key, w, st["final"], nb, st["buys"], ok))
    print("| 전략 | 따로 계산 | results.json | 거래 수(따로) | 거래 수(json) | 같음 |\n|---|---:|---:|---:|---:|---|")
    for key, w, r, n1, n2, ok in out:
        print(f"| {key} | {w:,.2f} | {r:,.2f} | {n1} | {n2} | {'✅' if ok else '❌'} |")
    print(f"\n[VERIFY] mismatches={bad}")
    print(f"[VERIFY] dip10 첫 판단 날 = {idx[k].date()} (종가 {p[k]:.2f}, 그때 최고 {ath[k]:.2f}, {p[k] / ath[k] - 1:+.2%}) → 산 날 {idx[k + 1].date()}")
    print(f"[VERIFY] ladder 산 날 = {[str(idx[d].date()) for d in buys]}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
