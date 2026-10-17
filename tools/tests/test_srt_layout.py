# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-17 — tools/srt_tool.py v1.7 시험: 한 문장 = 자막 하나 (길면 같은 자막 안에서 두 줄, 두 줄로도 넘을 때만 자막 2개),
#          줄바꿈은 쉼표·절 경계에서 ('나이에 / 따라'·'본 / 걸'·'2,100만 원에서 / 약' X), 예전 규칙('line', 주식)은 그대로,
#          build --reuse 는 옛 길이(자막 2개였으면 합)를 그대로, check 는 '하나에 들어가는데 나뉨'을 잡음.
#          사용자 지시 2026-10-17 "자막 좀 되도록 한 문장은 한 자막으로 표시되게해 길지 않은 문장도 잘라서 자막 띄우잖아
#          문장이 길면 적당한 곳에 분리하도록 해서 반영해". 임시 폴더만 씀 — 네트워크·GitHub 없음.
"""cd tools/tests && python3 -m unittest test_srt_layout -v"""
import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import srt_tool as st  # noqa: E402

SHORT = "결론부터 말씀드리겠습니다."
TWO = "국민연금은 남편이 한 달에 110만 원, 아내가 40만 원, 합쳐서 150만 원이에요."          # 롱폼 두 줄
LONG = ("A 부부가 65세 말에 이렇게 고치면, 평생 세금 차이는 2,100만 원에서 약 1,300만 원으로, "
        "피부양자에서 빠지는 기간은 5년에서 1년으로 줄어요.")                              # 롱폼 두 줄로도 넘음


def lines_of(cue):
    return cue.split("\n")


class Layout(unittest.TestCase):
    def test_layout_of_path(self):
        self.assertEqual(st.layout_of("economic/source/a/a.txt"), "long")
        self.assertEqual(st.layout_of("economic/source/a/shorts/a-shorts.txt"), "shorts")
        self.assertEqual(st.layout_of("stock/source/b/b.txt"), "line")

    def test_short_sentence_one_line(self):
        self.assertEqual(st.cue_split(SHORT, "long"), [SHORT])

    def test_two_line_sentence_is_one_cue(self):
        cues = st.cue_split(TWO, "long")
        self.assertEqual(len(cues), 1)                      # 예전(line)에는 자막 2개
        self.assertEqual(len(st.split_px(TWO)), 2)
        a, b = lines_of(cues[0])
        self.assertTrue(a.endswith(","), a)                 # 줄바꿈은 쉼표 뒤
        self.assertEqual(f"{a} {b}", TWO)
        for x in (a, b):
            self.assertLessEqual(st.text_px(x, 52), st.LAYOUTS["long"]["width"])

    def test_too_long_is_two_cues_at_comma(self):
        cues = st.cue_split(LONG, "long")
        self.assertEqual(len(cues), 2)
        self.assertEqual(" ".join(c.replace("\n", " ") for c in cues), LONG)
        self.assertTrue(cues[0].replace("\n", " ").endswith(","), cues[0])
        self.assertNotIn("원에서\n약", cues[0] + cues[1])    # 범위는 한 덩어리
        self.assertNotIn("원에서", cues[0].split("\n")[-1][-3:])

    def test_fixed_phrases_kept(self):
        t = "하지만 한 사람이 1년에 1,500만 원 이하로 꺼내면, 세금은 나이에 따라 5.5%에서 3.3%뿐이고, 피부양자 소득에도 들어가지 않습니다."
        joined = "|".join(st.cue_split(t, "long"))
        self.assertNotIn("나이에\n따라", joined)
        self.assertNotIn("나이에|따라", joined)
        t2 = "김씨 부부는 은퇴 첫해에만 세금과 건보료로 200만 원 넘게 손해 본 걸 알게 됐습니다."
        for c in st.cue_split(t2, "shorts"):
            for x in lines_of(c):
                self.assertFalse(x.startswith("걸 "), c)   # '본 / 걸' X

    def test_noun_ending_like_clause(self):
        t = "연금저축에서 1,800만 원을 남편 혼자 꺼내면 세금이 약 118만 원입니다."
        self.assertEqual(st.cue_split(t, "long"), ["연금저축에서 1,800만 원을 남편 혼자 꺼내면\n세금이 약 118만 원입니다."])

    def test_line_layout_unchanged(self):                   # 주식(stock/) — 예전 앞줄·뒷줄 자막 2개 그대로
        self.assertEqual(st.cue_split(TWO, "line"), st.split_px(TWO))
        self.assertTrue(all("\n" not in c for c in st.cue_split(TWO, "line")))


class BuildCheck(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        d = Path(self.tmp.name) / "economic" / "source" / "v1"
        d.mkdir(parents=True)
        self.txt = d / "v1.txt"
        self.txt.write_text(f"-도입\n{SHORT}\n{TWO}\n\n-끝\n{LONG}\n", "utf-8")
        self.srt = d / "v1.srt"

    def tearDown(self):
        self.tmp.cleanup()

    def run_quiet(self, fn, *a):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            r = fn(*a)
        return r, buf.getvalue()

    def test_build_then_check(self):
        self.run_quiet(st.build, str(self.txt), str(self.srt))
        subs = st.parse_srt(str(self.srt))
        self.assertEqual(len(subs), 1 + 1 + 2)              # 짧은 문장 1 · 두 줄 문장 1 · 긴 문장 2
        self.assertEqual(len(subs[1]["lines"]), 2)
        r, out = self.run_quiet(st.check, str(self.txt), str(self.srt))
        self.assertEqual(r, 0, out)
        self.assertIn("모양 long", out)

    def test_check_flags_needless_split(self):
        a, b = st.split_px(TWO)                             # 예전 SRT: 두 줄에 들어가는 문장이 자막 2개
        self.srt.write_text(
            f"1\n00:00:00,300 --> 00:00:02,000\n{SHORT}\n\n"
            f"2\n00:00:02,000 --> 00:00:04,000\n{a}\n\n3\n00:00:04,000 --> 00:00:06,000\n{b}\n\n"
            + "".join(f"{4 + k}\n00:00:{6 + 3 * k:02d},000 --> 00:00:{9 + 3 * k:02d},000\n{c}\n\n"
                      for k, c in enumerate(st.cue_split(LONG, "long"))), "utf-8")
        r, out = self.run_quiet(st.check, str(self.txt), str(self.srt))
        self.assertEqual(r, 1)
        self.assertIn("문장 2: 자막 하나(2줄)에 들어가는데 자막 2개로 나뉨", out)

    def test_reuse_keeps_total_length(self):
        a, b = st.split_px(TWO)
        old = Path(self.tmp.name) / "old.srt"
        old.write_text(f"1\n00:00:00,300 --> 00:00:02,000\n{SHORT}\n\n"
                       f"2\n00:00:02,000 --> 00:00:03,500\n{a}\n\n3\n00:00:03,500 --> 00:00:06,250\n{b}\n", "utf-8")
        self.run_quiet(st.build, str(self.txt), str(self.srt), str(old))
        subs = st.parse_srt(str(self.srt))
        self.assertAlmostEqual(subs[0]["end"] - subs[0]["start"], 1.7, places=3)
        self.assertAlmostEqual(subs[1]["end"] - subs[1]["start"], 4.25, places=3)   # 1.5 + 2.75 — 자막 2개 → 하나, 길이는 합
        self.assertEqual(subs[1]["text"], TWO)


if __name__ == "__main__":
    unittest.main()
