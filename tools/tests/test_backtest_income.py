# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-16 — tools/backtest/income.py v1.0·leverage.py v1.0 시험 (주식 2·3·4번). 네트워크 없이 만든 자료로.
"""python3 -m unittest test_backtest_income  (tools/tests 에서)"""
import sys
import unittest
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from backtest import income as ic  # noqa: E402
from backtest import leverage as lv  # noqa: E402


def frame(close, div=None, start="2014-01-01"):
    idx = pd.bdate_range(start, periods=len(close))
    return pd.DataFrame({"close": np.asarray(close, float), "div": np.zeros(len(close)) if div is None else np.asarray(div, float)}, index=idx)


class WithdrawPairTest(unittest.TestCase):
    def setUp(self):
        rng = np.random.default_rng(11)                                # 시드 고정 (재현)
        n = 600
        self.idx = frame(100 * np.exp(np.cumsum(rng.normal(0.0004, 0.01, n))))
        inc_close = 50 * np.exp(np.cumsum(rng.normal(0.0, 0.007, n)))
        div = np.zeros(n)
        div[20::21] = 0.5                                              # 한 달에 한 번 분배
        self.inc = frame(inc_close, div)

    def test_same_cash_out_both_accounts(self):
        """두 계좌가 꺼낸 돈 = A 분배금 × 주식 수 합 (날짜·금액 같음)."""
        r = ic.withdraw_pair(self.inc, self.idx, "2014-01-01", "2016-12-31", initial=100_000, fee=0.0025)
        sa = 100_000 * (1 - 0.0025) / self.inc["close"].iloc[0]
        expect = sa * self.inc["div"].iloc[1:len(r["dates"])].sum()
        self.assertAlmostEqual(r["out_cum"][-1], expect, places=6)
        self.assertEqual(len(r["events"]), int((self.inc["div"].iloc[1:len(r["dates"])] > 0).sum()))

    def test_a_value_is_shares_times_close(self):
        r = ic.withdraw_pair(self.inc, self.idx, "2014-01-01", "2016-12-31", fee=0.0)
        np.testing.assert_allclose(r["a_val"], r["a_shares"] * self.inc["close"].iloc[:len(r["dates"])].to_numpy())

    def test_no_withdrawal_means_b_is_buy_and_hold(self):
        """분배가 없으면 B 는 처음 산 주식 그대로 (매도 없음)."""
        inc = self.inc.copy()
        inc["div"] = 0.0
        r = ic.withdraw_pair(inc, self.idx, "2014-01-01", "2016-12-31", fee=0.0025)
        sb = 100_000 * (1 - 0.0025) / self.idx["close"].iloc[0]
        np.testing.assert_allclose(r["b_val"], sb * self.idx["close"].iloc[:len(r["dates"])].to_numpy())

    def test_no_lookahead(self):
        """뒤 날 값을 바꿔도 앞 날 계좌 값은 그대로."""
        r1 = ic.withdraw_pair(self.inc, self.idx, "2014-01-01", "2016-12-31")
        idx2 = self.idx.copy()
        idx2.iloc[400:, 0] *= 0.5
        inc2 = self.inc.copy()
        inc2.iloc[400:, 0] *= 2.0
        r2 = ic.withdraw_pair(inc2, idx2, "2014-01-01", "2016-12-31")
        np.testing.assert_allclose(r1["a_val"][:400], r2["a_val"][:400])
        np.testing.assert_allclose(r1["b_val"][:400], r2["b_val"][:400])

    def test_b_depleted_flag(self):
        """B 가 모자라면 바닥난 날을 적고 0 이 된다."""
        inc = self.inc.copy()
        inc.loc[inc["div"] > 0, "div"] = 20.0                         # 분배가 매우 큼
        idx = self.idx.copy()
        idx["close"] = np.linspace(100, 5, len(idx))                   # 지수는 계속 떨어짐
        r = ic.withdraw_pair(inc, idx, "2014-01-01", "2016-12-31")
        self.assertIsNotNone(r["b_broke"])
        self.assertEqual(r["b_val"][-1], 0.0)


class ReinvestTest(unittest.TestCase):
    def test_tax_zero_fee_zero_matches_total_return(self):
        """세금·비용 0 이면 재투자 계좌 = 총수익 지수 (data.yahoo_daily 의 tr 정의와 같음)."""
        rng = np.random.default_rng(3)
        n = 500
        c = 30 * np.exp(np.cumsum(rng.normal(0.0002, 0.01, n)))
        d = np.zeros(n)
        d[60::63] = 0.3
        df = frame(c, d)
        r = ic.reinvest(df, "2014-01-01", "2016-12-31", initial=1000, tax=0.0, fee=0.0)
        tr = ((df["close"] + df["div"]) / df["close"].shift(1)).fillna(1.0).cumprod()
        np.testing.assert_allclose(r["val"], 1000 * tr.to_numpy() / tr.iloc[0], rtol=1e-10)

    def test_tax_reduces_and_records(self):
        df = frame(np.full(300, 10.0), np.r_[np.zeros(100), [1.0], np.zeros(199)])
        r0 = ic.reinvest(df, "2014-01-01", "2016-12-31", initial=1000, tax=0.0, fee=0.0)
        r15 = ic.reinvest(df, "2014-01-01", "2016-12-31", initial=1000, tax=0.15, fee=0.0)
        self.assertAlmostEqual(r0["val"][-1], 1100.0)                  # 100주 × 배당 1 = 100 → 10주 더
        self.assertAlmostEqual(r15["val"][-1], 1085.0)
        self.assertAlmostEqual(r15["tax_paid"][-1], 15.0)
        self.assertAlmostEqual(r15["div_gross"][-1], 100.0)

    def test_monthly_contribution(self):
        df = frame(np.full(130, 10.0))
        r = ic.reinvest(df, "2014-01-01", "2016-12-31", initial=0.0, tax=0.0, fee=0.0, monthly=100)
        months = len(ic.month_starts(df.index)) - 1                    # 첫날(달 첫 거래일)은 initial 만
        self.assertAlmostEqual(r["paid"][-1], 100 * months)
        self.assertAlmostEqual(r["val"][-1], 100 * months)

    def test_liquidate(self):
        self.assertAlmostEqual(ic.liquidate(2000.0, 1000.0, 0.2, fee=0.0), 1800.0)
        self.assertAlmostEqual(ic.liquidate(900.0, 1000.0, 0.2, fee=0.0), 900.0)


class LeverageTest(unittest.TestCase):
    def setUp(self):
        idx = pd.bdate_range("2020-01-01", periods=6)
        self.close = pd.Series([100, 110, 99, 99, 108.9, 108.9], index=idx, dtype=float)
        self.rf0 = pd.Series(0.0, index=idx)

    def test_daily_reset_volatility_drag(self):
        """+10% → −10%: 1배 −1%, 2배 (1.2 × 0.8) = −4% — 매일 배수를 맞추는 구조."""
        r2 = lv.daily_returns(self.close, self.rf0, 2)
        g = (1 + r2).cumprod()
        self.assertAlmostEqual(g.iloc[2], 1.2 * 0.8)
        self.assertAlmostEqual(g.iloc[1], 1.2)

    def test_costs_calendar_days(self):
        """금리 5%·보수 1%, 3배: 하루(평일 1일)에 2×5%/365 + 1%/365 를 뺌."""
        c = pd.Series([100.0, 100.0], index=pd.to_datetime(["2020-01-02", "2020-01-03"]))
        rf = pd.Series([5.0, 5.0], index=c.index)
        r = lv.daily_returns(c, rf, 3, er=0.01)
        self.assertAlmostEqual(r.iloc[1], -(2 * 0.05 + 0.01) / 365)
        c2 = pd.Series([100.0, 100.0], index=pd.to_datetime(["2020-01-03", "2020-01-06"]))   # 금 → 월 = 3일
        r2 = lv.daily_returns(c2, rf.set_axis(c2.index), 3, er=0.01)
        self.assertAlmostEqual(r2.iloc[1], -3 * (2 * 0.05 + 0.01) / 365)

    def test_uses_previous_day_rate(self):
        """그날 금리가 아니라 전날 금리 (미래 정보 아님)."""
        c = pd.Series([100.0, 100.0, 100.0], index=pd.to_datetime(["2020-01-01", "2020-01-02", "2020-01-03"]))
        rf = pd.Series([0.0, 0.0, 50.0], index=c.index)
        r = lv.daily_returns(c, rf, 2)
        self.assertAlmostEqual(r.iloc[2], 0.0)

    def test_one_x_no_cost_equals_index(self):
        r1 = lv.daily_returns(self.close, self.rf0, 1)
        np.testing.assert_allclose((1 + r1).cumprod().to_numpy() * 100, self.close.to_numpy())

    def test_wipeout(self):
        c = pd.Series([100.0, 60.0, 90.0], index=pd.bdate_range("2020-01-01", periods=3))
        r = lv.daily_returns(c, pd.Series(0.0, index=c.index), 3)
        self.assertEqual(r.iloc[1], -1.0)
        self.assertEqual(r.iloc[2], 0.0)

    def test_grow_monthly(self):
        idx = pd.bdate_range("2020-01-30", "2020-04-10")
        r = pd.Series(0.0, index=idx)
        g = lv.grow(r, initial=0.0, monthly=100, fee=0.0)
        self.assertAlmostEqual(g["paid"][-1], 400.0)                  # 1/30 첫 매수 + 2·3·4월 첫 거래일
        self.assertAlmostEqual(g["val"][-1], 400.0)


if __name__ == "__main__":
    unittest.main()
