# -*- coding: utf-8 -*-
# VERSION: v1.2 — 2026-10-16 — content_research v1.1.2 나이 규칙 시험 (N세기·N0대 왕·N0대손·제N0대는 나이 아님)
# (v1.1 — 2026-10-15 — content_research v1.1 drop_off_topic 시험 추가: analysis.json 이 옛 규칙으로 만들어졌어도 지금
#          <주제>/analysis_rules.toml [exclude] OFF_TOPIC 낱말이 제목에 든 성공 사례를 빼는지 (주식 결과의 영화·시골집 미장·팬미팅·무당 영상))
# (v1.0.1 — 2026-10-15 — 끝인사를 "시청해주셔서 감사합니다."로 (script_guide v3.1) — "끝까지" 약속은 첫 문장에서 잼. (v1.0 — 2026-10-14 — tools/content_research.py v1.0 시험 (임시 대본·가짜 비교 집단만 씀 — 네트워크·실제 분석 결과 없음)))
r"""
  python3 -m unittest tools.tests.test_content_research -v     (저장소 최상위에서)

- 대본 문장 나누기: 파트 라벨('-…')·'[챕터]'·'[장면]' 카드 제외, 한 줄 두 문장은 둘로, '-2,500만 원…'은 문장
- measure: 읽는 음절·말투 비율·처음 나오는 시점·장치 판정
- 비교 집단 성공 비율(rate)과 표 칸 이스케이프(md)
- (v1.1) 지금 규칙으로 성공 사례 다시 거르기(drop_off_topic) — 규칙 파일 없음·깨짐이면 그대로
"""
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

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


class DropOffTopicTest(unittest.TestCase):
    """v1.1: 지금 analysis_rules.toml [exclude] OFF_TOPIC 으로 성공 사례를 다시 거름."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.patch = mock.patch.object(cr, "ROOT", self.root)
        self.patch.start()
        out = self.root / "stock" / "result" / "outliers"
        out.mkdir(parents=True)
        self.cases = [{"no": 1, "id": "a", "title": "시골집 고치기 | 몰탈 30포대로 미장까지", "folder": "W_a"},
                      {"no": 2, "id": "b", "title": "같은 TQQQ에 1억 (실제 데이터)", "folder": "W_b"},
                      {"no": 3, "id": "c", "title": "미장 지금 들어가도 될까? 나스닥 10년", "folder": "W_c"}]
        (out / "analysis.json").write_text(json.dumps({"generated": "t", "success_cases": self.cases}), "utf-8")

    def tearDown(self):
        self.patch.stop()
        self.tmp.cleanup()

    def rules(self, text):
        (self.root / "stock" / "analysis_rules.toml").write_text(text, "utf-8")

    def test_drops_by_current_rules(self):
        self.rules('[exclude]\nOFF_TOPIC = ["코인", "시골집", "몰탈"]\n')
        keep, dropped = cr.drop_off_topic("stock", self.cases)
        self.assertEqual([c["id"] for c in keep], ["b", "c"])       # '미장'(미국장 줄임말)만 든 #3 은 남음
        self.assertEqual(dropped, [{"id": "a", "title": self.cases[0]["title"], "why": "뺀 주제(시골집)"}])
        self.assertEqual([c["id"] for c in cr.Data("stock").cases], ["b", "c"])   # 불러올 때 적용

    def test_no_rules_file_keeps_all(self):
        keep, dropped = cr.drop_off_topic("stock", self.cases)
        self.assertEqual((len(keep), dropped), (3, []))

    def test_broken_rules_keeps_all(self):
        self.rules("[exclude\nOFF_TOPIC = [")
        keep, dropped = cr.drop_off_topic("stock", self.cases)
        self.assertEqual((len(keep), dropped), (3, []))


class AgeRegexTest(unittest.TestCase):
    """v1.1.2: 나이 규칙 — 역사 댓글의 세기·왕 대수·후손 대수·제N대는 나이가 아님."""

    def dec(self, text):
        m = cr.AGE_RX.search(text)
        return (m.group(1) or m.group(2)[0]) + "0대" if m else None

    def test_real_ages(self):
        for text, want in [("저는 60대 주부입니다", "60대"), ("올해 78세인데요", "70대"), ("46살 직장인", "40대"),
                           ("20대 때 처음 봤어요", "20대"), ("50 대 아저씨", "50대")]:
            self.assertEqual(self.dec(text), want, text)

    def test_not_ages(self):
        for text in ["기원전 27세기면 돌도끼", "조선 20대 왕 경종", "갈송 할아버지 20대손입니다", "제20대 대통령 선거",
                     "30대 임금", "고려 30대 후손", "21세기 지금"]:
            self.assertIsNone(self.dec(text), text)


if __name__ == "__main__":
    unittest.main()
