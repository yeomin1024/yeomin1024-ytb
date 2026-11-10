# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-11-06 — clip_short v1.1 단위 앞 줄바꿈 금지 시험 더함.
# 이전 v1.0 — 2026-11-06 — tools/clip_short.py v1.0 시험: 자막 줄바꿈(한 줄·두 줄·두 줄 넘으면 멈춤) · 화면 시간 맞추기(늦춤 1.35배 한도·
#          마지막 장면 멈춤·pingpong) · 그래프 날짜 · 이름표가 카드 안 (글꼴 필요 — 없으면 건너뜀: node video/scripts/get-fonts.mjs)
r"""
  python3 -m unittest tools.tests.test_clip_short -v     (저장소 최상위에서)
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import clip_short as cs  # noqa: E402

HAVE_FONT = cs.FONT.exists() and cs.FONT_B.exists()
CHART = dict(dates=dict(start="2021.01", end="2022.10"), baseline=dict(y=100),
             lines=[dict(who="A", label="SOXL", points=[[0, 100], [0.5, 215], [1.0, 25]]),
                    dict(who="B", label="나눠 담기", points=[[0, 100], [0.5, 128], [1.0, 127]])])


class TestClipShort(unittest.TestCase):
    def test_schedule(self):
        plan = dict(clips=[dict(name="S01", use_from=0.2, use_to=2.2, show_sec=3.0),                     # 2.0초 → 1.35배 + 0.3초 멈춤
                           dict(name="S02", use_from=0.2, use_to=2.3, loop="pingpong", show_sec=3.4),    # 4.2초 → 자름
                           dict(name="S03", use_from=0.2, use_to=3.0, show_sec=3.2, format="duo_chart", scale=0.8)])
        s = cs.schedule(plan)
        self.assertEqual((s[0]["slow"], s[0]["hold"]), (1.35, 0.3))
        self.assertEqual((s[1]["src_len"], s[1]["slow"], s[1]["hold"], s[1]["ping"]), (4.2, 1.0, 0.0, True))
        self.assertEqual((s[2]["slow"], s[2]["hold"], s[2]["chart"], s[2]["scale"]), (1.143, 0.0, True, 0.8))
        self.assertEqual([x["t0"] for x in s], [0.0, 3.0, 6.4])

    def test_date(self):
        self.assertEqual([cs._date(CHART, x) for x in (0.0, 0.5, 1.0)], ["2021.01", "2021.11", "2022.10"])   # 0.5×21달 = 10.5 → round 짝수 쪽 10

    @unittest.skipUnless(HAVE_FONT, "글꼴 없음")
    def test_wrap(self):
        f = cs.font(cs.CAP["size"])
        self.assertEqual(cs.wrap("짧은 자막", f, 834), ["짧은 자막"])
        two = cs.wrap("폭락이 오자 A는 원금까지 잃었고, B는 여전히 수익입니다", f, 834)
        self.assertEqual(len(two), 2)
        self.assertTrue(all(f.getlength(t) <= 834 for t in two))
        money = cs.wrap("넣은 5,500만 원 중 2,000만 원 넘게 잃었습니다.", f, 834)   # v1.1 — 단위 앞에서 끊지 않음
        self.assertFalse(any(line.startswith(cs.NO_BREAK_BEFORE) for line in money[1:]), money)
        with self.assertRaises(SystemExit):
            cs.wrap("아주 긴 자막 " * 12, f, 834)                               # 두 줄로도 넘으면 멈춤 (자막 2줄까지)

    @unittest.skipUnless(HAVE_FONT, "글꼴 없음")
    def test_chart_labels_inside_panel(self):
        fonts = dict(date=cs.font(44, True), small=cs.font(36), label=cs.font(38, True))
        for x in (0.05, 0.5, 0.78, 1.0):                                     # 선이 엇갈리는 때·끝에서도 이름표가 카드 안 (넘으면 SystemExit)
            im = cs.chart_layer(CHART, x, fonts)
            x0, y0, x1, y1 = im.getbbox()
            self.assertGreaterEqual(x0, cs.PANEL[0])
            self.assertLessEqual(x1, cs.PANEL[2] + 1)                       # getbbox 는 끝 픽셀 + 1 (카드 자체가 1020 까지)
            self.assertLessEqual(y1, cs.PANEL[3] + 1)


if __name__ == "__main__":
    unittest.main()
