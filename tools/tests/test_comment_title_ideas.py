# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-21 — tools/comment_title_ideas.py v1.0 시험: 댓글 갈래(질문·요청 / 주장·믿음 / 뺌) — 한국어·영어 (네트워크·저장소 안 건드림).
"""python3 -m unittest test_comment_title_ideas  (tools/tests 에서)"""
import os
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
for k in ("GITHUB_TOKEN", "GH_TOKEN"):
    os.environ.pop(k, None)
import comment_title_ideas as cti  # noqa: E402


class KindOf(unittest.TestCase):
    def test_korean(self):
        self.assertEqual(cti.kind_of("ISA계좌 개설후 ETF 투자하면 3년뒤 해지할때 ETF도 모두 매도하고 끝내야 되나요?", "한국"), "질문·요청")
        self.assertEqual(cti.kind_of("미국배당다우존스도 강의해 주세요.", "한국"), "질문·요청")
        self.assertEqual(cti.kind_of("무지성 적립해도 인플레는 이깁니다 은행도 이기구요", "한국"), "주장·믿음")
        self.assertIsNone(cti.kind_of("국민연금 특검해야 합니다 대통령이 책임져라", "한국"))      # 정치 댓글은 뺌
        self.assertIsNone(cti.kind_of("목소리가 너무 좋으세요 결국 구독합니다", "한국"))          # 투자 낱말 없음

    def test_english(self):
        self.assertEqual(cti.kind_of("What happens when the market drops 20-40% and stays down 2-3 years?", "미국"), "질문·요청")
        self.assertEqual(cti.kind_of("conclusion: never sell. invest, dont trade", "미국"), "주장·믿음")
        self.assertIsNone(cti.kind_of("Great video, thanks!", "미국"))

    def test_clean(self):
        self.assertEqual(cti.clean("a\n\n b   c"), "a b c")


if __name__ == "__main__":
    unittest.main()
