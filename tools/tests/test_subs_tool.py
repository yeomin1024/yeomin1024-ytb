# VERSION: v1.2.0 — 2026-10-23 — subs_tool v1.2.0: 조·천억·'2억 5천' · 단위 낱말 · [장면] 카드 시험.
# (v1.1.0) — 2026-10-18 — subs_tool v1.1.0 자막 나누기 시험: 짧은 조각 없음 · 일본어 낱말(Python·가타카나·1,700) 안에서 안 끊음 · 두 줄 고르게.
# v1.0.1 — 2026-10-17 — 'K·M' 뒤 글자 · 일본어 7万5千 시험 추가.
# v1.0 — 2026-10-17 — tools/subs_tool.py 숫자 맞추기·자막 나누기 시험 (사용자 지시 2026-10-17 "외국어 자막 대본도 필요하지? 쇼츠, 롱폼 각각 언어별로 작성해봐")
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import subs_tool as st  # noqa: E402


class KoValues(unittest.TestCase):
    def test_man_cheon(self):
        self.assertEqual([v for v, _ in st.ko_values("약 7만 5천 달러로, 원금보다 25.3% 적어요.")], [75000, 25.3])

    def test_month_and_year(self):
        self.assertEqual(st.ko_values("2013년 12월, 두 계좌에 원금 10만 달러씩 넣었어요."), [(2013, "num"), (12, "month"), (100000, "num")])

    def test_comma_thousands(self):
        self.assertEqual([v for v, _ in st.ko_values("첫 분배금은 2014년 1월, 1,024달러였어요.")], [2014, 1, 1024])


class Match(unittest.TestCase):
    def ok(self, ko, tr, lang):
        miss, _ = st.num_problems(ko, tr, lang)
        self.assertEqual(miss, [], f"{lang}: {tr}")

    def test_en(self):
        self.ok("2013년 12월, 두 계좌에 원금 10만 달러씩 넣었어요.", "In December 2013, each account got $100,000 of principal.", "en")

    def test_de_decimal_comma(self):
        self.ok("QYLD 계좌에 남은 돈은 약 7만 5천 달러로, 원금보다 25.3% 적어요.", "Im QYLD-Konto blieben etwa 75.000 $, 25,3 % weniger als das Kapital.", "de")

    def test_tr_percent_first(self):
        self.ok("원금보다 25.3% 적어요.", "Anaparanın %25,3 altında.", "tr")

    def test_ja_man(self):
        self.ok("QQQ 계좌에는 약 51만 달러, QYLD의 6.83배가 남았습니다.", "QQQ口座には約51万ドル、QYLDの6.83倍が残りました。", "ja")
        self.ok("약 7만 5천 달러", "約7万5千ドル", "ja")

    def test_vi_month(self):
        self.ok("2013년 12월에 시작", "Bắt đầu vào tháng 12 năm 2013", "vi")

    def test_no_fake_million(self):
        _, extra = st.num_problems("나스닥100은 크게 오르내려요.", "Nasdaq-100 mà QYLD theo biến động mạnh.", "vi")
        self.assertEqual(extra, [])

    def test_ja_compound_no_extra(self):
        _, extra = st.num_problems("약 7만 5천 달러", "約7万5千ドル", "ja")
        self.assertEqual(extra, [])

    def test_missing(self):
        miss, _ = st.num_problems("원금보다 25.3% 적어요.", "It is below the principal.", "en")
        self.assertEqual(miss, ["25.3"])


class Cues(unittest.TestCase):
    def test_short_one_cue(self):
        self.assertEqual(len(st.cue_parts("Thanks for watching.", "en")), 1)

    def test_long_split_two_lines_max(self):
        t = "People say a covered call ETF keeps your principal even if you spend its monthly payouts, but does it really hold up over thirteen years?"
        for p in st.cue_parts(t, "en"):
            self.assertLessEqual(len(st.wrap(p, "en")), 2)



class SplitV11(unittest.TestCase):
    """v1.1.0 — 2026-10-18 첫 실제 오디오 SRT 에서 찾은 것."""
    JA = "本当かどうか、AIが書いたPythonコードで過去の実際の価格を使ってバックテストしました。"

    def test_no_tiny_fragment(self):
        parts = st.cue_parts(self.JA, "ja")
        self.assertGreater(len(parts), 1)
        for p in parts:
            self.assertGreaterEqual(len(p), st.MIN_PART * len(self.JA) - 1, p)
            self.assertLessEqual(len(st.wrap(p, "ja")), 2)

    def test_ja_never_inside_word(self):
        for p in st.cue_parts(self.JA, "ja"):
            lines = st.wrap(p, "ja")
            for a, b in zip(lines, lines[1:]):
                self.assertGreater(st.ja_score(a[-1], b[0]), 0, (a, b))
        lines = st.wrap("3倍口座は約1,700万ドルで、1倍の約200万ドルの8.55倍でした。", "ja")
        self.assertTrue(all("1,700" in l or "1,7" not in l for l in lines), lines)

    def test_two_lines_balanced(self):
        lines = st.wrap("It mixes stocks with notes that work like selling that right to buy.", "en")
        self.assertEqual(len(lines), 2)
        self.assertLess(abs(len(lines[0]) - len(lines[1])), 15, lines)


class V120Test(unittest.TestCase):                           # v1.2.0 — 조·천억·'2억 5천' · 단위 낱말 · [장면] 카드
    def test_korean_units(self):
        self.assertEqual(st.ko_values("신용 잔고는 38조 6천억 원"), [(38600000000000.0, "num")])
        self.assertEqual(st.ko_values("이 2억 5천은"), [(250000000.0, "num")])
        self.assertEqual(st.ko_values("7만 5천 원"), [(75000.0, "num")])

    def test_scale_words(self):
        self.assertEqual(st.tr_values("hit 38.6 trillion won", "en"), {38600000000000.0})
        self.assertEqual(st.tr_values("2,5 Milliarden Won", "de"), {2500000000.0})
        self.assertEqual(st.tr_values("38兆6千億ウォン", "ja"), {38600000000000.0})
        self.assertEqual(st.num_problems("38조 6천억 원", "38.6 trillion won", "en"), ([], []))

    def test_cards_not_sentences(self):
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "s.txt"
            f.write_text("-정리\n정리해볼게요.\n[장면] 정리\n1\n2\n-마무리\n감사합니다.\n", "utf-8")
            self.assertEqual(st.structure(f), [("label", "-정리"), ("s", "정리해볼게요."), ("label", "-마무리"), ("s", "감사합니다.")])


if __name__ == "__main__":
    unittest.main()
