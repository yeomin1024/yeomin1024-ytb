#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-10-15 — data v1.1 일별 종가(sp500_daily) 시험 추가. (v1.0 — 2026-10-15 — tools/backtest v1.0 시험 (주식 채널 컨셉 — 사용자 지시 2026-10-15 "주식 채널 컨셉은 ai로 코드 만들어서
#          가설을 백테스트해서 검증해보는거니까"). 가짜 가격으로만 — 네트워크 없음 (자료 받기는 가짜 fetch).)
"""cd tools/tests && python3 -m unittest test_backtest -v

- 벡터 계산(dca_wealth·dip_wealth)이 한 달씩 실제로 사고 모으는 느린 계산(naive_*)과 같은지
- 미래 정보 금지: 신호 sig[t] 가 달 t 이후 가격을 바꿔도 그대로인지
- 총수익 지수·현금 지수·한 번에 vs 나눠서 손 계산
- 자료: 끝부분 0 배당 → NaN · complete_until · 캐시 다시 쓰기 · 검사(중복·빈 달)
"""
import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from backtest import data as bd  # noqa: E402
from backtest import monthly as bm  # noqa: E402

SEED = 20261015                       # 가짜 가격 시드 (재현)


def fake_prices(n=400, seed=SEED):
    rng = np.random.default_rng(seed)
    r = rng.normal(0.006, 0.045, n)
    p = 100 * np.exp(np.cumsum(r))
    d = p * 0.02 * (1 + 0.1 * rng.standard_normal(n)).clip(0.5)
    rate = (3 + rng.standard_normal(n)).clip(0.1)
    return p, d, rate


class TestMonthly(unittest.TestCase):
    def setUp(self):
        self.p, self.d, self.rate = fake_prices()
        self.tri = bm.total_return_index(self.p, self.d)

    def test_total_return_index_by_hand(self):
        p, d = np.array([100.0, 110.0, 99.0]), np.array([0.0, 12.0, 12.0])
        tri = bm.total_return_index(p, d)
        self.assertAlmostEqual(tri[1], (110 + 1) / 100)
        self.assertAlmostEqual(tri[2], tri[1] * (99 + 1) / 110)
        with self.assertRaises(ValueError):
            bm.total_return_index(p, np.array([0.0, np.nan, 1.0]))

    def test_cash_index(self):
        c = bm.cash_index(3, np.array([12.0, 24.0, 0.0]))
        self.assertAlmostEqual(c[1], 1.01)
        self.assertAlmostEqual(c[2], 1.01 * 1.02)
        self.assertTrue((bm.cash_index(5) == 1).all())

    def test_dca_matches_naive(self):
        s, e = bm.windows(len(self.tri), 120, first=1)
        w = bm.dca_wealth(self.tri, s, e)
        for i in (0, 37, len(s) - 1):
            self.assertAlmostEqual(w[i], bm.naive_dca(self.tri, s[i], e[i]), places=9)

    def test_dip_matches_naive(self):
        cash = bm.cash_index(len(self.p), self.rate)
        for drop in (0.05, 0.10, 0.20):
            sig = bm.dip_signal(self.p, drop)
            nxt = bm.next_true(sig)
            s, e = bm.windows(len(self.tri), 120, first=1)
            out = bm.dip_wealth(self.tri, cash, nxt, s, e)
            for i in range(0, len(s), 23):
                self.assertAlmostEqual(out["wealth"][i], bm.naive_dip(self.tri, cash, sig, s[i], e[i]), places=9,
                                       msg=f"drop={drop} window={i}")
            self.assertTrue((out["cash_left"] <= out["wealth"] + 1e-12).all())

    def test_signal_has_no_lookahead(self):
        sig = bm.dip_signal(self.p, 0.10)
        for t in (50, 200, 333):
            q = self.p.copy()
            q[t:] = q[t:] * 0.3                         # 달 t 부터 폭락으로 바꿔도
            self.assertTrue((bm.dip_signal(q, 0.10)[: t + 1] == sig[: t + 1]).all())   # 달 t 까지 신호는 그대로
        self.assertTrue((bm.at_high(self.p)[: 10] == bm.at_high(np.concatenate([self.p[:9], [1e9]]))[: 10]).all())

    def test_next_true(self):
        sig = np.array([False, True, False, False, True, False])
        self.assertEqual(bm.next_true(sig).tolist(), [1, 1, 4, 4, 4, 6])

    def test_lump_vs_split_by_hand(self):
        tri = np.array([1.0, 2.0, 2.0, 4.0])
        cash = np.ones(4)
        lump, split = bm.lump_vs_split(tri, cash, np.array([0]), np.array([3]), k=2)
        self.assertAlmostEqual(lump[0], 4.0)
        self.assertAlmostEqual(split[0], 0.5 * 4 + 0.5 * 2)
        with self.assertRaises(ValueError):
            bm.lump_vs_split(tri, cash, np.array([2]), np.array([3]), k=3)

    def test_forward_return(self):
        tri = np.array([1.0, 1.1, 1.21, 1.331])
        f = bm.forward_return(tri, 12)
        self.assertTrue(np.isnan(f).all())                  # 12달 뒤가 없음
        f1 = bm.forward_return(tri, 1)
        self.assertAlmostEqual(f1[0], 1.1 ** 12 - 1)
        self.assertTrue(np.isnan(f1[-1]))

    def test_summarize(self):
        r = bm.summarize([2, 1, 3], [1, 2, 3], "a", "b")
        self.assertEqual((r["windows"], r["a_wins"]), (3, 1))
        self.assertAlmostEqual(r["ratio_median"], 1.0)


class TestData(unittest.TestCase):
    CSV = ("Date,SP500,Dividend,Earnings,Consumer Price Index,Long Interest Rate,Real Price,Real Dividend,Real Earnings,PE10\n"
           "2020-01-01,100,2,0,0,1.5,0,0,0,0\n2020-02-01,101,2.1,0,0,1.6,0,0,0,0\n2020-03-01,90,2.2,0,0,1.0,0,0,0,0\n"
           "2020-04-01,95,0,0,0,0.9,0,0,0,0\n2020-05-01,99,0,0,0,0,0,0,0,0\n")

    def test_tail_zero_to_nan_and_cache(self):
        calls = []

        def fake_fetch(url):
            calls.append(url)
            return self.CSV.encode()
        with tempfile.TemporaryDirectory() as td:
            df, meta = bd.sp500_monthly(data_dir=td, fetch=fake_fetch)
            self.assertEqual(meta["complete_until"], "2020-03-01")
            self.assertEqual(meta["dividend_until"], "2020-03-01")
            self.assertEqual(meta["long_rate_until"], "2020-04-01")
            self.assertTrue(np.isnan(df.loc["2020-04-01", "dividend"]))
            self.assertEqual(len(meta["sha256"]), 64)
            df2, meta2 = bd.sp500_monthly(data_dir=td, fetch=fake_fetch)   # 두 번째는 캐시
            self.assertEqual(len(calls), 1)
            self.assertEqual(meta2["fetched_at"], meta["fetched_at"])
            pd.testing.assert_frame_equal(df, df2)

    def test_validate_reports_problems(self):
        idx = pd.to_datetime(["2020-01-01", "2020-02-01", "2020-02-01", "2020-05-01"])
        df = pd.DataFrame({"price": [1.0, 2.0, 2.0, -1.0]}, index=idx)
        rep = bd.validate_monthly(df, ["price"])
        self.assertEqual((rep["duplicates"], rep["gaps"], rep["price_nonpositive"]), (1, 1, 1))

    def test_fetch_failure_message(self):
        def boom(url):
            raise RuntimeError("[DATA] 자료 받기 실패: 시험")
        with tempfile.TemporaryDirectory() as td:
            with self.assertRaises(RuntimeError) as cm:
                bd.sp500_monthly(data_dir=td, fetch=boom)
            self.assertIn("자료 받기 실패", str(cm.exception))

    def test_daily_blank_days_dropped(self):
        csv = "observation_date,SP500\n2020-01-02,100\n2020-01-03,\n2020-01-06,.\n2020-01-07,98.5\n"
        with tempfile.TemporaryDirectory() as td:
            s, meta = bd.sp500_daily(data_dir=td, fetch=lambda url: csv.encode())
            self.assertEqual(s.tolist(), [100.0, 98.5])
            self.assertEqual((meta["rows"], meta["blank_days_dropped"]), (2, 2))
            self.assertIn("07b81e6", meta["url"])                       # 자료 저장소 커밋 고정


if __name__ == "__main__":
    unittest.main()
