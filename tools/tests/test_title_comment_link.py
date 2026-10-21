# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-21 — tools/title_comment_link.py v1.0 시험: 낱말 뽑기·댓글에서 찾기·주·나라·주제 갈래·관심 많은 댓글 고르기·
#          메아리와 우연 겹침 (작은 가짜 사례만 — 저장소 결과·네트워크·GitHub 안 건드림).
"""python3 -m unittest test_title_comment_link  (tools/tests 에서)"""
import os
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
for k in ("GITHUB_TOKEN", "GH_TOKEN"):
    os.environ.pop(k, None)
import title_comment_link as tc  # noqa: E402


def cm(text, likes=10, creator=False, reply=False):
    return {"text": text, "likes": likes, "creator": creator, "reply": reply}


def case(i, title, comments, vpd=100):
    return {"id": f"v{i:010d}", "title": title, "comments": comments, "vpd": vpd, "channel": "C", "subs": 1000, "views": 1000}


class Words(unittest.TestCase):
    def test_words_of(self):
        w = tc.words_of("국민연금은 하락장에 얼마를 잃었을까? The Stocks to BUY now")
        self.assertIn("국민연금", w)                 # 조사 '은' 뗌
        self.assertIn("하락장", w)                   # 조사 '에' 뗌
        self.assertIn("stock", w)                    # 소문자·끝 s 뗌
        self.assertIn("buy", w)
        self.assertNotIn("the", w)                   # 영어 뜻 없는 말
        self.assertNotIn("now", w)

    def test_word_rx(self):
        self.assertTrue(tc.word_rx("stock").search("These STOCKS are cheap"))
        self.assertFalse(tc.word_rx("stock").search("livestock prices"))   # 낱말 경계
        self.assertTrue(tc.word_rx("국민연금").search("국민연금이 왜 이래요"))  # 한국어는 조사가 붙어도

    def test_week_and_country(self):
        self.assertEqual([tc.week_of(d) for d in (0, 6.9, 7, 27.9, 28, -1, None)], [1, 1, 2, 4, None, None, None])
        ch = {"A": {"country": "US"}, "B": {"country": "IN"}}
        self.assertEqual(tc.country_of({"lang": "ko", "channel_id": "B"}, ch), "한국")       # 한국어면 채널 나라 상관없이
        self.assertEqual(tc.country_of({"lang": "en", "audio_lang": "en-US", "channel_id": "A"}, ch), "미국")
        self.assertIsNone(tc.country_of({"lang": "zh-Hant", "audio_lang": "yue-HK", "channel_id": "A"}, ch))   # 미국 채널의 중국어 영상은 뺌
        self.assertIsNone(tc.country_of({"lang": "en", "channel_id": "B"}, ch))
        self.assertIsNone(tc.country_of({"lang": "en", "channel_id": "Z"}, ch))              # 채널 나라 모름

    def test_themes(self):
        self.assertIn("폭락·급락·공포", tc.themes_of("코스피 대폭락의 날"))
        self.assertIn("매수·기회·바닥", tc.themes_of("This Pullback is a Gift. I'm Buying"))
        self.assertNotIn("매도·현금·손절", tc.themes_of("Big sell-off today"))               # sell-off 는 폭락 쪽
        self.assertIn("질문(?로 끝남)", tc.themes_of("팔아야 할까?"))


class Echo(unittest.TestCase):
    def test_top_comments_filters(self):
        c = case(1, "제목", [cm("주인 댓글", 999, creator=True), cm("답글", 500, reply=True), cm("오픈채팅 오세요", 400),
                             cm("좋은 영상", 5), cm("좋아요 없음", 0)] + [cm(f"댓글 {k}", 100 - k) for k in range(25)])
        top = tc.top_comments(c)
        self.assertEqual(len(top), tc.TOP_COMMENTS)
        self.assertEqual(top[0]["text"], "댓글 0")            # 채널 주인·답글·도배 꼴 뺌, 좋아요 순
        self.assertTrue(all(m["likes"] >= tc.MIN_COMMENT_LIKES for m in top))

    def test_echo_and_baseline(self):
        a = case(1, "국민연금 182조 손실", [cm("국민연금 너무하네"), cm("국민연금이 왜"), cm("주식 어렵다"), cm("감사합니다")])
        b = case(2, "테슬라 로드스터", [cm("테슬라 최고"), cm("주식 어렵다")])
        tt = {a["id"]: {"text": "국민연금 손실 '충격'", "reader": "t"}}
        va, vb = tc.video_row(a, tt), tc.video_row(b, tt)
        self.assertAlmostEqual(va["echo_title"], 0.5)          # 4개 중 2개에 '국민연금'
        self.assertAlmostEqual(va["echo_thumb"], 0.5)
        self.assertIsNone(vb["echo_thumb"])                    # 썸네일 문구 없음
        self.assertAlmostEqual(tc.baseline_echo(va, [va, vb], "tw"), 0.0)   # a 의 댓글에 b 제목 낱말(테슬라·로드스터) 없음
        self.assertAlmostEqual(tc.baseline_echo(vb, [va, vb], "tw"), 0.0)


if __name__ == "__main__":
    unittest.main()
