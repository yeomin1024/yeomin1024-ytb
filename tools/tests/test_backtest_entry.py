# -*- coding: utf-8 -*-
# VERSION: v1.3 — 2026-10-16 — 성공 판정 매도 barrier(m, n)·새 매수 방법(RULES_V4) 시험 더함. (v1.2 — 2026-10-16 — 최고점 −n% 매도(trail) 시험 더함.) (v1.1 — 2026-10-16 — buy_and_hold 시험 더함.) (v1.0 — 2026-10-16 — tools/backtest/entry.py v1.0 시험 (매수 신호 10가지 × 같은 매도 규칙). 네트워크 없이 만든 자료로.)
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

    def test_trail_sells_next_day_after_drop_from_peak(self):
        """trail: 종가 ≤ 산 뒤 최고 종가 × 0.9 가 된 다음 거래일 종가에 판다. 그 전에는 팔지 않는다."""
        path = [100, 105, 110, 104, 99.5, 98, 97, 115, 125]
        c = series([120.0] * 100 + [100.0] * 199 + path + [125.0] * 50)   # 앞의 120 = 그때까지 최고 → 100 은 −16.7% (dip10 신호)
        ind = en.indicators(c)
        s = 299
        r = en.simulate("dip10", ind, s, len(c) - 1, trail=0.10, dates=c.index, cost=0.0)
        t = r.trades[0]
        self.assertEqual(t["buy_i"], s)                                       # s-1 종가 신호 → s 종가 매수
        self.assertEqual(t["stop_i"], s + 5)                                  # 98 ≤ 110 × 0.9 = 99 (99.5 는 아님)
        self.assertEqual(t["sell_i"], s + 6)                                  # 다음 날 97 에 매도
        self.assertAlmostEqual(t["peak_price"], 110.0)
        self.assertAlmostEqual(t["ret"], 97 / 100 - 1)
        self.assertEqual(r.trades[1]["buy_i"], s + 7)                         # 판 날도 신호(97 ≤ 108) → 다음 날 다시 매수

    def test_trail_no_lookahead_and_no_overlap(self):
        cut = 600
        alt = self.close.copy()
        alt.iloc[cut + 1:] *= np.linspace(0.6, 1.7, len(alt) - cut - 1)
        for k in en.ORDER:
            ia, ib = en.indicators(self.close, self.vix), en.indicators(alt, self.vix)
            ra = en.simulate(k, ia, 300, len(alt) - 1, trail=0.08, dates=self.close.index)
            rb = en.simulate(k, ib, 300, len(alt) - 1, trail=0.08, dates=alt.index)
            j = cut - 300
            np.testing.assert_allclose(ra.value[:j + 1], rb.value[:j + 1], err_msg=k)
            for x, y in zip(ra.trades, ra.trades[1:]):
                self.assertGreater(y["buy_i"], x["sell_i"], k)
            prod = np.prod([1 + t["ret"] for t in ra.trades]) if ra.trades else 1.0
            self.assertAlmostEqual(ra.value[-1], 10_000 * prod, places=6, msg=k)

    def test_run_all_needs_history(self):
        with self.assertRaises(ValueError):
            en.run_all(self.close, self.close.index[100], self.close.index[-1], vix=self.vix)




class BarrierTest(unittest.TestCase):
    """v1.3 성공 판정 매도: 산 값 × (1+n) 이상이 먼저면 성공, × (1−m) 이하가 먼저면 실패 — 그날 종가로 판정, 다음 날 종가에 매도."""
    def setUp(self):
        rng = np.random.default_rng(11)                                 # 시드 고정 (재현)
        self.close = series(100 * np.exp(np.cumsum(rng.normal(0.0003, 0.011, 900))))
        self.vix = series(18 + 6 * np.abs(rng.normal(0, 1, 900)))

    def sim(self, key, close=None, mn=(0.05, 0.05)):
        c = self.close if close is None else close
        ind = en.indicators(c, self.vix)
        return en.simulate(key, ind, 300, len(c) - 1, cost=0.001, dates=c.index, barrier=mn), ind

    def test_first_barrier_decides(self):
        """판정 = 산 뒤 먼저 닿은 쪽 · 그 전에는 두 선 사이 · 매도는 판정 다음 날."""
        for k in en.ORDER_V4 + ["any"]:
            r, ind = self.sim(k)
            p = ind["close"]
            self.assertTrue(r.trades, k)
            for t in r.trades:
                if t["result"] is None:
                    continue
                h = t["hit_i"]
                between = p[t["buy_i"] + 1:h]
                self.assertTrue(np.all((between < t["target"]) & (between > t["stop"])), (k, t["buy_date"]))
                if t["result"] == "win":
                    self.assertGreaterEqual(p[h], t["target"] * (1 - 1e-12))
                else:
                    self.assertLessEqual(p[h], t["stop"] * (1 + 1e-12))
                if not t["open"]:
                    self.assertEqual(t["sell_i"], h + 1, (k, t["buy_date"]))

    def test_target_and_stop_from_buy_price(self):
        r, _ = self.sim("m1", mn=(0.04, 0.07))
        for t in r.trades:
            self.assertAlmostEqual(t["target"], t["buy_price"] * 1.07, places=9)
            self.assertAlmostEqual(t["stop"], t["buy_price"] * 0.96, places=9)

    def test_any_rebuys_next_day(self):
        """기준 'any' = 매도한 다음 날 바로 다시 매수."""
        r, _ = self.sim("any")
        for a, b in zip(r.trades, r.trades[1:]):
            self.assertEqual(b["buy_i"], a["sell_i"] + 1)

    def test_no_lookahead_barrier(self):
        """d 뒤 가격을 바꿔도 d 까지 판정·매도가 끝난 거래는 같다."""
        cut = 650
        alt = self.close.copy()
        alt.iloc[cut + 1:] *= np.linspace(0.5, 1.8, len(alt) - cut - 1)
        for k in en.ORDER_V4 + ["any"]:
            a, _ = self.sim(k)
            b, _ = self.sim(k, close=alt)
            fa = [(t["buy_i"], t["sell_i"], t["result"]) for t in a.trades if not t["open"] and t["sell_i"] <= cut]
            fb = [(t["buy_i"], t["sell_i"], t["result"]) for t in b.trades if not t["open"] and t["sell_i"] <= cut]
            self.assertEqual(fa, fb, k)
            self.assertTrue(np.allclose(a.value[:cut - 300 + 1], b.value[:cut - 300 + 1]), k)

    def test_stats_success_rate(self):
        r, _ = self.sim("drop1")
        st = en.stats(r)
        w = sum(t["result"] == "win" for t in r.trades); l = sum(t["result"] == "loss" for t in r.trades)
        self.assertEqual((st["wins"], st["losses"]), (w, l))
        self.assertAlmostEqual(st["success_rate"], w / (w + l))

if __name__ == "__main__":
    unittest.main()
