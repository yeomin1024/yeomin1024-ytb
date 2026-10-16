#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-16 — tools/backtest/daily.py v1.0 시험 (사용자 지시 2026-10-16 "흔히 사용하는 매수 전략을 10가지 정도 골라서
#          그냥 매수하고 관망하는거랑 비교"). 가짜 가격으로만 — 네트워크 없음.
"""cd tools/tests && python3 -m unittest test_backtest_daily -v

- 미래 정보 금지: 날 k 뒤 가격을 바꿔도 k 까지의 거래·평가 금액이 그대로인지 (전략 11개 모두)
- 신호 다음 날 종가에 사고파는지 (200일선·손절·익절·저점 매수·하락 분할·RSI·돌파·12개월 모멘텀)
- 매수 후 관망 = 총수익 지수 비율 × (1 - 비용), 분할 매수 12번·넣은 돈 = 처음 돈
- 거래 기록의 수익을 곱하면 끝 값과 같은지 (현금 이자 0)
- 총수익 지수·현금 이자·와일더 RSI 손 계산
"""
import sys
import unittest
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from backtest import daily as dl  # noqa: E402

SEED = 20261016


def fake_close(n=1500, seed=SEED, start="2000-01-03"):
    rng = np.random.default_rng(seed)
    r = rng.normal(0.0003, 0.012, n)
    r[600:660] -= 0.006                                   # 큰 하락 하나 (전략들이 움직이게)
    idx = pd.bdate_range(start, periods=n)
    return pd.Series(100 * np.exp(np.cumsum(r)), index=idx, name="close")


def run(key, close, s, e, cost=0.001, tr=None, cash_ret=None):
    ind, trv = dl.prepare(close, close if tr is None else tr)
    return dl.simulate(key, ind, trv, s, e, cost=cost, cash_ret=cash_ret)


class TestNoLookahead(unittest.TestCase):
    def test_future_prices_do_not_change_past(self):
        close = fake_close()
        s, e, k = 260, 1400, 900
        rng = np.random.default_rng(1)
        changed = close.copy()
        changed.iloc[k + 1:] *= np.exp(np.cumsum(rng.normal(0, 0.03, len(close) - k - 1)))
        for key in ["hold"] + dl.ORDER:
            a = run(key, close, s, e)
            b = run(key, changed, s, e)
            fa = [f for f in a.fills if f["i"] <= k]
            fb = [f for f in b.fills if f["i"] <= k]
            self.assertEqual([(f["i"], f["side"]) for f in fa], [(f["i"], f["side"]) for f in fb], key)
            np.testing.assert_allclose(a.value[: k - s + 1], b.value[: k - s + 1], rtol=1e-12, err_msg=key)


class TestRules(unittest.TestCase):
    def test_hold_equals_index_ratio(self):
        close = fake_close()
        r = run("hold", close, 260, 1400, cost=0.001)
        self.assertAlmostEqual(r.value[-1], 10_000 * 0.999 * close.iloc[1400] / close.iloc[260], places=6)
        self.assertEqual(len(r.fills), 1)

    def test_dca12_buys_twelve_times_at_month_firsts(self):
        close = fake_close()
        s = int(np.where(close.index >= "2001-03-01")[0][0])
        r = run("dca12", close, s, s + 400, cost=0.0)
        buys = [f for f in r.fills if f["side"] == "buy"]
        self.assertEqual(len(buys), 12)
        self.assertAlmostEqual(sum(f["amount"] for f in buys), 10_000, places=6)
        months = [close.index[f["i"]].to_period("M") for f in buys]
        self.assertEqual(len(set(months)), 12)
        for f in buys[1:]:
            i = f["i"]
            self.assertNotEqual(close.index[i].to_period("M"), close.index[i - 1].to_period("M"))   # 그 달 첫 거래일
        self.assertAlmostEqual(r.stock_share[-1], 1.0, places=9)

    def test_sma200_trades_day_after_cross(self):
        close = fake_close()
        ind, _ = dl.prepare(close, close)
        r = run("sma200", close, 260, 1400)
        p, m = ind["close"], ind["sma200"]
        for f in r.fills[1:]:
            d = f["i"] - 1                                    # 신호 날 = 산·판 날 하루 전
            if f["side"] == "buy":
                self.assertGreater(p[d], m[d])
            else:
                self.assertLessEqual(p[d], m[d])

    def test_stop10_and_tp10_hand_example(self):
        px = [100, 100, 105, 110, 104, 99, 97, 95, 96, 100, 104.6, 105, 106] + [106] * 5
        idx = pd.bdate_range("2010-01-04", periods=len(px))
        close = pd.Series(px, index=idx, dtype=float)
        r = run("stop10", close, 1, len(px) - 1, cost=0.0)
        sides = [(f["i"], f["side"]) for f in r.fills]
        # 1 매수(시작) → 최고 110(3) → 99 ≤ 99(5) 신호 → 6 매도 → 최저 95(7) → 104.6 ≥ 104.5(10) 신호 → 11 매수
        self.assertEqual(sides, [(1, "buy"), (6, "sell"), (11, "buy")])
        r2 = run("tp10", close, 1, len(px) - 1, cost=0.0)
        # 1 매수 100 → 110 ≥ 110(3) 신호 → 4 매도(104) → 매도 뒤 최고 104 → 93.6 이하? 아니 (최저 95) → 그대로 현금
        self.assertEqual([(f["i"], f["side"]) for f in r2.fills], [(1, "buy"), (4, "sell")])
        self.assertAlmostEqual(r2.trades[0]["ret"], 104 / 100 - 1, places=12)

    def test_dip10_and_ladder(self):
        px = [100, 101, 102, 95, 91.8, 91, 85, 81, 75, 72, 71] + [80] * 4
        idx = pd.bdate_range("2010-01-04", periods=len(px))
        close = pd.Series(px, index=idx, dtype=float)
        r = run("dip10", close, 1, len(px) - 1, cost=0.0)
        # 최고 102 → 91.8 ≤ 91.8(4) 신호 → 5 매수
        self.assertEqual([(f["i"], f["side"]) for f in r.fills], [(5, "buy")])
        r2 = run("ladder", close, 1, len(px) - 1, cost=0.0)
        # 1 1/4 → −10%(4: 91.8) → 5 · −20%(7: 81 ≤ 81.6) → 8 · −30%(9: 72 ≤ 71.4? 아니, 10: 71 ≤ 71.4) → 11
        self.assertEqual([f["i"] for f in r2.fills], [1, 5, 8, 11])
        np.testing.assert_allclose([f["amount"] for f in r2.fills], [2500.0] * 4)

    def test_rsi_and_breakout_start_in_cash(self):
        close = fake_close()
        for key in ("rsi30_70", "brk55_20"):
            r = run(key, close, 300, 1400)
            self.assertEqual(r.stock_share[0], 0.0, key)
            self.assertTrue(r.fills and r.fills[0]["side"] == "buy", key)

    def test_mom12_changes_only_on_new_month(self):
        close = fake_close()
        r = run("mom12", close, 300, 1400)
        for f in r.fills[1:]:
            i = f["i"]
            self.assertNotEqual(close.index[i].to_period("M"), close.index[i - 1].to_period("M"))

    def test_trade_log_matches_final_value(self):
        close = fake_close()
        for key in ("stop10", "tp10", "sma200", "gc50_200", "brk55_20", "rsi30_70", "mom12"):
            r = run(key, close, 260, 1400, cost=0.001)
            prod = np.prod([1 + t["ret"] for t in r.trades])
            self.assertAlmostEqual(r.value[-1] / 10_000, prod, places=9, msg=key)


class TestIndex(unittest.TestCase):
    def test_tr_index_constant_price(self):
        idx = pd.bdate_range("2011-01-03", "2011-03-31")
        close = pd.Series(100.0, index=idx)
        div = pd.Series([12.0, 12.0, 12.0], index=pd.to_datetime(["2011-01-01", "2011-02-01", "2011-03-01"]))
        tr = dl.tr_index_daily(close, div)
        jan = idx[idx.month == 1]
        self.assertAlmostEqual(tr.loc[jan[-1]], (1 + 0.01 / len(jan)) ** (len(jan) - 1), places=12)   # 첫날은 1
        self.assertAlmostEqual(tr.iloc[-1] / tr.loc[jan[-1]], (1 + 0.01 / 20) ** 20 * (1 + 0.01 / len(idx[idx.month == 3])) ** len(idx[idx.month == 3]), places=3)

    def test_cash_daily_month_compounds(self):
        idx = pd.bdate_range("2011-01-03", "2011-02-28")
        rf = pd.Series([1.0, 1.0], index=pd.to_datetime(["2011-01-01", "2011-02-01"]))
        c = dl.cash_daily(idx, rf, "month_pct")
        feb = idx.month == 2
        self.assertAlmostEqual(np.prod(1 + c[feb]), 1.01, places=12)

    def test_rsi_matches_slow_reference(self):
        p = fake_close(300).to_numpy()
        fast = dl.rsi_wilder(p, 14)
        d = np.diff(p)
        up, dn = np.clip(d, 0, None), np.clip(-d, 0, None)
        au, ad = up[:14].mean(), dn[:14].mean()
        ref = [100 - 100 / (1 + au / ad)]
        for i in range(14, len(d)):
            au = (au * 13 + up[i]) / 14
            ad = (ad * 13 + dn[i]) / 14
            ref.append(100 - 100 / (1 + au / ad))
        np.testing.assert_allclose(fast[14:], ref, rtol=1e-12)
        self.assertTrue(np.isnan(fast[:14]).all())


if __name__ == "__main__":
    unittest.main()
