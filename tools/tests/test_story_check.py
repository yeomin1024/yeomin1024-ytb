# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-10-21 — story_check v1.1: 제목 맨 앞 낱말의 끝 조사 · 마무리 다음 화 예고.
# (v1.0) — 2026-10-21 — tools/story_check.py v1.0 시험: 맞는 대본은 문제 0, 규칙마다 어긴 대본은 그 문제만 (네트워크·저장소 안 건드림).
"""python3 -m unittest test_story_check  (tools/tests 에서)"""
import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
for k in ("GITHUB_TOKEN", "GH_TOKEN"):
    os.environ.pop(k, None)
import story_check as sc  # noqa: E402

TITLE = "반토막 계좌, 6년 만에 찾은 매수 원칙 3가지"
GOOD = """-도입
반토막 난 계좌를 오늘도 열어 봤어요.
6년 동안 넣은 돈의 절반이 사라졌죠.
아내에게는 아직 말도 못 했어요.
왜 나만 이럴까, 정말 답답하더라고요.
그래도 처음부터 다시 복기해 보기로 했어요.
책과 자료를 읽고 백테스트도 돌려서, 드디어 방법을 찾았어요.
-방법1
첫 번째는 한 종목에 계좌의 10%만 넣는 거예요.
저는 한 종목에 전부 넣었거든요.
-방법2
두 번째는 매달 같은 날 같은 금액을 매수하는 거예요.
저는 떨어질 때마다 더 매수하는 물타기, 그러니까 평단을 낮추려고 더 매수한 거죠.
-방법3
마지막 세 번째는 빌린 돈으로 투자하지 않는 거예요.
빚이 있으면 하락장을 견딜 수가 없더라고요.
-정리
오늘 찾은 세 가지, 정리해볼게요.
[장면] 정리
1 한 종목 10%
2 매달 같은 금액
3 빚투 없이
-마무리
이 세 가지만큼은 꼭 지켜 볼게요.
원금 회복, 그리고 파이어까지 포기하지 않을게요.
여러분의 투자도 꼭 성공하길 바랄게요.
시청해주셔서 감사합니다.
"""


def run(text, title=TITLE, intro_ok=False):
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "s.txt"
        p.write_text(text, "utf-8")
        return sc.check(p, title, intro_ok=intro_ok)


class Good(unittest.TestCase):
    def test_no_problems(self):
        probs, warns, info = run(GOOD)
        self.assertEqual(probs, [], probs)
        self.assertTrue(any("물타기" in i for i in info))          # 개미 낱말은 처음 나온 문장을 보여 줌
        self.assertFalse(any("해요체가 아님" in w or "사다·팔다" in w for w in warns), warns)

    def test_intro_estimate(self):
        parts = dict(sc.parts_of(self._file(GOOD)))
        syl, sec = sc.intro_seconds(parts["도입"])
        self.assertLessEqual(sec, sc.INTRO_MAX_SEC)
        self.assertGreater(syl, 50)

    def _file(self, text):
        d = tempfile.mkdtemp()
        p = Path(d) / "s.txt"
        p.write_text(text, "utf-8")
        return p


class Bad(unittest.TestCase):
    def test_title_head_missing(self):
        probs, _, _ = run(GOOD.replace("반토막 난 계좌를", "제 계좌를"))
        self.assertTrue(any("제목 맨 앞 낱말 '반토막'" in p for p in probs), probs)

    def test_intro_too_long(self):
        long = GOOD.replace("아내에게는 아직 말도 못 했어요.\n",
                            "아내에게는 아직 말도 못 했어요.\n" + "매일 밤 계좌를 열었다 닫았다 하면서 잠을 제대로 못 잤어요.\n" * 6)
        probs, _, _ = run(long)
        self.assertTrue(any(p.startswith("도입 추정") for p in probs), probs)
        probs, warns, _ = run(long, intro_ok=True)          # v1.3 사용자가 통과시킨 도입 → 경고
        self.assertFalse(any(p.startswith("도입 추정") for p in probs), probs)
        self.assertTrue(any("사용자가 통과시킴" in w for w in warns), warns)

    def test_intro_between_target_and_limit(self):         # v1.3 30~35초 = 경고만 (목표 30 · 마지노선 35)
        mid = GOOD.replace("아내에게는 아직 말도 못 했어요.\n", "아내에게는 아직 말도 못 했어요.\n" + "밤마다 계좌를 열어 봤어요.\n" * 7)
        probs, warns, _ = run(mid)                           # 추정 약 33.7초
        self.assertFalse(any(p.startswith("도입 추정") for p in probs), probs)
        self.assertTrue(any(w.startswith("도입 추정") and "목표" in w for w in warns), warns)

    def test_ordinal(self):
        probs, _, _ = run(GOOD.replace("두 번째는 매달", "또 하나는 매달"))
        self.assertTrue(any("-방법2 첫 문장" in p for p in probs), probs)

    def test_card_missing(self):
        probs, _, _ = run(GOOD.replace("[장면] 정리\n1 한 종목 10%\n2 매달 같은 금액\n3 빚투 없이\n", ""))
        self.assertTrue(any("정리 카드가 없음" in p for p in probs), probs)

    def test_card_too_long(self):
        probs, _, _ = run(GOOD.replace("3 빚투 없이", "3 빚투 없이 하락장을 견딜 수 있는 여윳돈으로만 오래오래 꾸준하게 나눠서 투자하고 계좌는 한 달에 한 번만 열어 보기"))
        self.assertTrue(any("정리 카드" in p and "자 >" in p for p in probs), probs)

    def test_last_sentence(self):
        probs, _, _ = run(GOOD.replace("시청해주셔서 감사합니다.", "다음에 또 만나요."))
        self.assertTrue(any("마지막 문장" in p for p in probs), probs)

    def test_part_order_and_story_label(self):
        probs, _, _ = run(GOOD.replace("-방법2", "-사연"))
        self.assertTrue(any("파트 순서" in p for p in probs), probs)
        self.assertTrue(any("'사연'" in p for p in probs), probs)

    def test_banned_and_tone(self):
        probs, warns, _ = run(GOOD.replace("빚이 있으면 하락장을 견딜 수가 없더라고요.", "그때 떡상만 믿었다."))
        self.assertTrue(any("떡상" in p for p in probs), probs)
        self.assertTrue(any("해요체가 아님" in w for w in warns), warns)

    def test_buy_sell_word(self):
        _, warns, _ = run(GOOD.replace("저는 한 종목에 전부 넣었거든요.", "저는 한 종목만 샀거든요."))
        self.assertTrue(any("사다·팔다" in w for w in warns), warns)

    def test_title_head_particle(self):
        probs, _, _ = run(GOOD, title="반토막은 이렇게 다시 시작합니다")      # '반토막은' → '반토막' 으로 찾음
        self.assertFalse(any("제목 맨 앞 낱말" in p for p in probs), probs)
        probs, _, _ = run(GOOD, title="계좌보다 무서운 건 포기")                # '계좌'는 첫 문장에 있음
        self.assertFalse(any("제목 맨 앞 낱말" in p for p in probs), probs)
        probs, _, _ = run(GOOD, title="손절보다 무서운 건 포기")                # '손절'은 첫 문장에 없음
        self.assertTrue(any("제목 맨 앞 낱말" in p for p in probs), probs)

    def test_series_preview_ok(self):
        _, warns, _ = run(GOOD.replace("여러분의 투자도", "다음 이야기에서는 빨리 메우려다 망한 이유를 꺼내 볼게요.\n여러분의 투자도"))
        self.assertFalse(any("-마무리 문장" in w for w in warns), warns)

    def test_no_title(self):
        probs, warns, _ = run(GOOD, title=None)
        self.assertEqual(probs, [])
        self.assertTrue(any("--title" in w for w in warns))


if __name__ == "__main__":
    unittest.main()
