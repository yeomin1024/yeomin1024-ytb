# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-17 — tools/backtest/shorts_numcheck.py v1.0.1 시험: 숫자 덩어리(숫자 + 단위) 자르기 · 앞에 숫자가 붙은 곳은 맞다고 보지 않음.
"""python3 -m unittest test_shorts_numcheck  (tools/tests 에서)"""
import re
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "backtest"))
import shorts_numcheck as sn  # noqa: E402


def found(tok, text):
    return bool(re.search(r"(?<![\d,.])" + re.escape(tok), text))   # shorts_numcheck.check() 와 같은 규칙


class TokensTest(unittest.TestCase):
    def test_units(self):
        self.assertEqual(sn.tokens("3배 레버리지에 매달 500달러씩, 2001년 넣은 돈의 92.3%가"), ["3배", "500달러", "2001년", "92.3%"])
        self.assertEqual(sn.tokens("계좌 2천 개의 평균은 51.8%"), ["2천", "51.8%"])
        self.assertEqual(sn.tokens("매달 1,000달러씩"), ["1,000달러"])
        self.assertEqual(sn.tokens("S&P 500을 따라가는"), ["500"])          # 단위 없는 숫자는 숫자만

    def test_no_prefix_match(self):
        self.assertFalse(found("13년", "2013년 12월에 넣은 계좌"))           # '13년' 이 '2013년' 에 걸리면 안 됨 (v1.0.1)
        self.assertTrue(found("13년", "13년 뒤 원금"))
        self.assertFalse(found("2.2%", "SPY는 22.2% 줄어"))
        self.assertTrue(found("22.2%", "SPY는 22.2% 줄어"))


if __name__ == "__main__":
    unittest.main()
