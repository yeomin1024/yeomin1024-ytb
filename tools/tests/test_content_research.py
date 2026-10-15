# -*- coding: utf-8 -*-
# VERSION: v1.0.1 — 2026-10-15 — 끝인사를 "시청해주셔서 감사합니다."로 (script_guide v3.1) — "끝까지" 약속은 첫 문장에서 잼. (v1.0 — 2026-10-14 — tools/content_research.py v1.0 시험 (임시 대본·가짜 비교 집단만 씀 — 네트워크·실제 분석 결과 없음))
r"""
  python3 -m unittest tools.tests.test_content_research -v     (저장소 최상위에서)

- 대본 문장 나누기: 파트 라벨('-…')·'[챕터]'·'[장면]' 카드 제외, 한 줄 두 문장은 둘로, '-2,500만 원…'은 문장
- measure: 읽는 음절·말투 비율·처음 나오는 시점·장치 판정
- 비교 집단 성공 비율(rate)과 표 칸 이스케이프(md)
"""
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(TOOLS))
import content_research as cr  # noqa: E402

SCRIPT = """-같은 5억, 다른 세금
지금 연금저축을 갖고 은퇴를 앞두고 계시다면, 이 숫자부터 끝까지 보세요.
결론부터 말씀드리겠습니다. 예금부터 씁니다.
왜 이렇게 차이가 날까요?
[장면] 고지
이 카드 문구는 문장이 아닙니다.
-두 부부
-2,500만 원이 사라졌습니다.
숫자는 2026년 10월 기준입니다.
시청해주셔서 감사합니다.
"""


class ContentResearchTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.path = Path(self.tmp.name) / "s.txt"
        self.path.write_text(SCRIPT, encoding="utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    def test_sentences(self):
        s = cr.script_sentences(self.path)
        self.assertEqual(s[0], "지금 연금저축을 갖고 은퇴를 앞두고 계시다면, 이 숫자부터 끝까지 보세요.")
        self.assertIn("결론부터 말씀드리겠습니다.", s)          # 한 줄 두 문장 → 둘
        self.assertIn("예금부터 씁니다.", s)
        self.assertNotIn("이 카드 문구는 문장이 아닙니다.", s)  # [장면] 카드 문구 제외
        self.assertIn("-2,500만 원이 사라졌습니다.", s)          # 음수 금액은 라벨이 아님
        self.assertEqual(len(s), 7)

    def test_measure(self):
        r = cr.measure(self.path, rate_sps=5.1)
        self.assertEqual(r["sent"], 7)
        self.assertGreater(r["syl"], 60)
        self.assertAlmostEqual(r["minutes"], r["syl"] / 5.1 / 60, places=6)
        self.assertEqual(r["first"]["결론 먼저"] is not None, True)
        self.assertTrue(r["devices"]["대상 부르기·조건 (첫 30초: ~계시다면·~라면·~분들)"])
        self.assertTrue(r["devices"]["질문으로 시작 (첫 15초)"])
        self.assertTrue(r["devices_any_time"]["끝까지 보라는 약속"])
        self.assertFalse(r["devices_any_time"]["어르신 호칭 (어머님·아버님·어르신·부모님)"])
        # 합니다체: 보세요(해요) / 말씀드리겠습니다·씁니다·사라졌습니다·기준입니다·감사합니다(합니다) / 날까요(질문)
        self.assertAlmostEqual(r["formal"], 5 / 7, places=6)
        self.assertAlmostEqual(r["q"], 1 / 7, places=6)

    def test_rate_and_md(self):
        rows = [dict(title="월 30만 원 손해", ok=True), dict(title="월 10만 원", ok=False), dict(title="방법", ok=False), dict(title="팁", ok=True)]
        n, with_, without = cr.rate(rows, lambda x: "월" in x["title"])
        self.assertEqual((n, with_, without), (2, 0.5, 0.5))
        self.assertEqual(cr.md("a|b"), "a\\|b")


if __name__ == "__main__":
    unittest.main()
