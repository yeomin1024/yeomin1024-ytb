# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-23 — tools/story_kit.py v1.0 시험: 금액 읽기 · 장면 표 문법(인형·화면) · 제작안 절 읽기 · 쇼츠 길이 추정.
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import story_kit as sk  # noqa: E402


class AmountTest(unittest.TestCase):
    def test_won(self):
        self.assertEqual(sk.amount("전재산의 2억 5천만 원을 잃었어요."), "₩250,000,000")
        self.assertEqual(sk.amount("1억 원 남짓 남았어요."), "₩100,000,000")
        self.assertEqual(sk.amount("매달 100만 원씩 넣어요."), "₩1,000,000")
        self.assertEqual(sk.amount("7천만 원이 남았죠."), "₩70,000,000")

    def test_first_one_wins(self):
        # 앞에 나온 것이 화면에 — 70% 가 2억 5천보다 먼저
        self.assertEqual(sk.amount("전재산의 70%인 2억 5천만 원을 손해 봤어요."), "−70%")

    def test_pct_sign_and_multiple(self):
        self.assertEqual(sk.amount("한 달 동안 34% 넘게 떨어졌죠."), "−34%")
        self.assertEqual(sk.amount("같은 기간 81% 올랐어요."), "+81%")
        self.assertEqual(sk.amount("넣은 돈의 1.63배가 됐어요."), "×1.63")
        self.assertIsNone(sk.amount("숫자가 없는 문장이에요."))

    def test_jo_is_not_won(self):
        self.assertIsNone(sk.amount("신용 잔고는 38조 6천억 원이었어요."))


class GrammarTest(unittest.TestCase):
    def test_puppets(self):
        p = sk.parse_puppets("PHONE@L>rise+13:반도체:RESOLVE@L")
        self.assertEqual(p[0], dict(pose="PHONE", pos="L", move="rise", flip=False))
        self.assertEqual(p[1]["pose"], "RESOLVE")
        self.assertEqual(p[1]["at"], [13, "반도체"])
        with self.assertRaises(ValueError):
            sk.parse_puppets("ANGRY@L")

    def test_screens(self):
        self.assertEqual(sk.parse_screen("K1 357140000>107140000", {}, None), {"type": "K1", "from": "357140000", "to": "107140000"})
        k2 = sk.parse_screen("K2 2020,*2024,2026", {}, None)
        self.assertEqual(k2["years"], ["2020", "2024", "2026"])
        self.assertEqual(k2["hl"], ["2024"])
        k3 = sk.parse_screen("K3 100,49,180 base=100 lab=2007,2009,2026 end=+81% @21:S&P", {}, None)
        self.assertEqual(k3["values"], [100.0, 49.0, 180.0])
        self.assertEqual(k3["base"], 100.0)
        self.assertEqual(k3["end"], "+81%")
        self.assertEqual(k3["at"], [21, "S&P"])
        k4 = sk.parse_screen("K4 1Y:24.3%:R 15Y:0%", {}, None)
        self.assertEqual(k4["items"][0], {"lab": "1Y", "val": "24.3%", "c": "R"})
        self.assertIsNone(k4["items"][1]["c"])
        k5 = sk.parse_screen("K5 !x3 +basket", {}, None)
        self.assertEqual(k5["icons"], [{"k": "x3", "m": "!"}, {"k": "basket", "m": "+"}])
        self.assertEqual(sk.parse_screen("BIG −70% R", {}, None), {"type": "BIG", "text": "−70%", "c": "R"})
        self.assertEqual(sk.parse_screen("K6", {5: {"lines": ["가", "나"]}}, 5)["lines"], ["가", "나"])
        for bad in ("K9 1", "K5 rocket", "K6"):
            with self.assertRaises(ValueError):
                sk.parse_screen(bad, {}, None)


class PlanTest(unittest.TestCase):
    PLAN = ("■ 제목\nR1. 주식으로 전재산 날려도, 포기 안 하면 진짜 손해가 아닙니다\nR2. 다른 안\n\n"
            "■ 쇼츠 제목\n1. 반도체로 2억 5천 잃었어요\n\n"
            "■ 쇼츠 대본 (약 50초)\n첫 문장이에요.\n둘째 문장이에요.\n\n■ 근거\n- 하나\n")

    def test_sections(self):
        self.assertEqual(sk.numbered(sk.section(self.PLAN, "제목"))[0], "주식으로 전재산 날려도, 포기 안 하면 진짜 손해가 아닙니다")
        self.assertEqual(sk.numbered(sk.section(self.PLAN, "쇼츠 제목")), ["반도체로 2억 5천 잃었어요"])
        self.assertEqual(sk.shorts_lines(self.PLAN), ["첫 문장이에요.", "둘째 문장이에요."])

    def test_estimate(self):
        t = sk.est(["가나다라마바사아자차카타파하" * 3])     # 42음절 ÷ 6.3
        self.assertAlmostEqual(t, 42 / 6.3, places=1)


class DupTest(unittest.TestCase):                           # v1.2 앞 화와 겹침 검사 도우미
    def test_nums_in(self):
        got = sk.nums_in(["전재산의 70%인 2억 5천만 원을 손해 봤어요.", "2021년에 8번 매매했어요.", "매달 100만 원씩 넣어요."])
        self.assertIn("70%", got)
        self.assertIn("2억5천만원", got)
        self.assertIn("100만원", got)
        self.assertNotIn("2021년", got)                       # 연도는 뺌
        self.assertNotIn("8번", got)                          # 짧은 것은 뺌

    def test_norm(self):
        self.assertEqual(sk.norm("여러분의 투자도, 꼭 성공하길 바랄게요."), "여러분의투자도꼭성공하길바랄게요")


if __name__ == "__main__":
    unittest.main()
