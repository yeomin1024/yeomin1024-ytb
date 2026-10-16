# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-10-16 — buy_and_hold 시험 더함. (v1.0 — 2026-10-16 — tools/backtest/entry.py v1.0 시험 (매수 신호 10가지 × 같은 매도 규칙). 네트워크 없이 만든 자료로.)
"""python3 -m unittest test_backtest_entry  (tools/tests 에서)"""
import sys
import unittest
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from backtest import entry as en  # noqa: E402


def series(vals, start="2014-01-01"):
    return pd.Series(np.asarray(vals, float), index=pd.bdate_range(start, periods=len(vals)))


class EntryTest(unittest.TestCase):
    def setUp(self):
        rng = np.random.default_rng(7)                                  # 시드 고정 (재현)
        self.close = series(100 * np.exp(np.cumsum(rng.normal(0.0003, 0.011, 900))))
        self.vix = series(20 + 15 * np.abs(rng.normal(0, 1, 900)))

    def sim(self, key, hold=60, cost=0.001, close=None, vix=None):
        c = self.close if close is None else close
        ind = en.indicators(c, self.vix if vix is None else vix)
        return en.simulate(key, ind, 300, len(c) - 1, hold=hold, cost=cost, dates=c.index), ind

    def test_buy_next_day_and_sell_after_hold(self):
        """신호 다음 날 종가에 사고, 산 날부터 hold 거래일 뒤 종가에 판다."""
        r, ind = self.sim("drop2", hold=40)
        self.assertTrue(r.trades)
        for t in r.trades:
            self.assertTrue(en.RULES["drop2"][0](ind, t["buy_i"] - 1), "산 날 전날에 신호가 있어야 함")
            if not t["open"]:
                self.assertEqual(t["sell_i"] - t["buy_i"], 40)

    def test_no_signal_used_while_holding(self):
        """보유 중에는 새로 사지 않는다 — 거래가 겹치지 않는다."""
        for k in en.ORDER:
            r, _ = self.sim(k, hold=50)
            for a, b in zip(r.trades, r.trades[1:]):
                self.assertGreater(b["buy_i"], a["sell_i"], k)

    def test_trade_return_includes_cost(self):
        r, ind = self.sim("m1", hold=30, cost=0.002)
        t = next(t for t in r.trades if not t["open"])
        p = ind["close"]
        want = p[t["sell_i"]] / p[t["buy_i"]] * (1 - 0.002) ** 2 - 1
        self.assertAlmostEqual(t["ret"], want, places=12)

    def test_no_lookahead(self):
        """d 뒤 가격을 바꿔도 d 까지의 거래·가치는 같다."""
        cut = 600
        alt = self.close.copy()
        alt.iloc[cut + 1:] *= np.linspace(0.6, 1.7, len(alt) - cut - 1)
        for k in en.ORDER:
            a, _ = self.sim(k, hold=45)
            b, _ = self.sim(k, hold=45, close=alt)
            j = cut - 300
            np.testing.assert_allclose(a.value[:j + 1], b.value[:j + 1], err_msg=k)
            self.assertEqual([t["buy_i"] for t in a.trades if t["buy_i"] <= cut], [t["buy_i"] for t in b.trades if t["buy_i"] <= cut], k)

    def test_value_identity(self):
        """끝 값 = 시작 돈 × 거래 수익 곱 (현금 이자 0, 보유 중이면 평가 값)."""
        for k in en.ORDER:
            r, _ = self.sim(k, hold=70)
            prod = np.prod([1 + t["ret"] for t in r.trades]) if r.trades else 1.0
            self.assertAlmostEqual(r.value[-1], 10_000 * prod, places=6, msg=k)

    def test_dip_threshold_float_edge(self):
        """종가가 정확히 최고가 × 0.9 이면 신호 (부동소수 끝자리 허용)."""
        c = series([100.0] * 299 + [90.0] + [95.0] * 100)
        ind = en.indicators(c)
        self.assertTrue(en.RULES["dip10"][0](ind, 299))
        self.assertFalse(en.RULES["dip10"][0](ind, 300))

    def test_cross_rules_fire_only_on_cross(self):
        c = series(list(np.linspace(100, 80, 300)) + list(np.linspace(80, 120, 200)))
        ind = en.indicators(c)
        days = [d for d in range(len(c)) if en.RULES["ma200"][0](ind, d)]
        self.assertEqual(len(days), 1)
        d = days[0]
        self.assertLessEqual(ind["close"][d - 1], ind["sma200"][d - 1])
        self.assertGreater(ind["close"][d], ind["sma200"][d])

    def test_vix_missing_day_no_signal(self):
        v = self.vix.copy()
        v.iloc[:] = 40.0
        v = v.drop(v.index[400])
        ind = en.indicators(self.close, v)
        self.assertFalse(en.RULES["vix30"][0](ind, 400))
        self.assertTrue(en.RULES["vix30"][0](ind, 401))

    def test_buy_and_hold_matches_m1_first_trade(self):
        """Buy and Hold = 첫날 매수(비용 포함) 뒤 그대로. 첫날 매수하는 규칙(m1)의 첫 거래가 팔기 전까지 같은 값."""
        c = self.close
        s = c.index[300]
        v, st = en.buy_and_hold(c, s, c.index[-1], cost=0.001)
        self.assertAlmostEqual(v[0], 10_000 * 0.999, places=9)
        self.assertAlmostEqual(st["final"], 10_000 * 0.999 * c.iloc[-1] / c.iloc[300], places=6)
        ind = en.indicators(c, self.vix)
        r = en.simulate("m1", ind, 300, len(c) - 1, hold=60, dates=c.index)
        if r.trades and r.trades[0]["buy_i"] == 300:
            np.testing.assert_allclose(r.value[:60], v[:60])

    def test_run_all_needs_history(self):
        with self.assertRaises(ValueError):
            en.run_all(self.close, self.close.index[100], self.close.index[-1], vix=self.vix)


if __name__ == "__main__":
    unittest.main()
