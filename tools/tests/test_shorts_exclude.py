#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-15 — 쇼츠 분석 v1.1 '돈 이야기 아님' 빼기·정보 요청 아닌 댓글 거르기 시험 (사용자 지시: "고쳐서 다시 분석해보자").
#          주제마다 따로 쓰는 규칙(economic·stock analysis_rules.toml [shorts_exclude]) 그대로 읽고, 2026-10-15 실제 제목으로 확인.
#          네트워크·GitHub 요청 없음.
"""python3 -m unittest tools.tests.test_shorts_exclude -v"""
import os
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
for k in ("GITHUB_TOKEN", "GH_TOKEN"):
    os.environ.pop(k, None)

import shorts_analysis as sh  # noqa: E402


def x(title, channel="채널", desc="", vid="aaaaaaaaaaa"):
    return {"id": vid, "title": title, "channel": channel, "description": desc}


class ShortsExcludeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rules = {t: sh.load_rules(ROOT, t) for t in ("economic", "stock")}

    def off(self, item, topic="economic"):
        return sh.off_kind(item, self.rules[topic])

    def test_each_topic_has_its_own_rules(self):
        for t, r in self.rules.items():
            with self.subTest(topic=t):
                self.assertEqual([k["name"] for k in r["shorts_exclude"]["kinds"]],
                                 ["운세·사주", "연예·예능·드라마", "명언·인생조언", "정치", "다른 뜻"])
        self.assertTrue(self.rules["economic"]["shorts_exclude"]["videos"])         # 눈으로 본 목록은 재테크에만
        self.assertEqual(self.rules["stock"]["shorts_exclude"]["videos"], {})

    def test_excluded_real_titles(self):
        cases = [
            (x("자식에게 돈 안 받아도 노후 생활비가 끊이지 않는 띠 3가지", "오늘의복운"), "운세·사주"),
            (x("노후가 평안해지는 나이는 언제...? #사주", "강남 돼지보살"), "운세·사주"),
            (x("[리센느] 노후 준비 끝난 걸그룹"), "연예·예능·드라마"),
            (x("대출받아 집짓고 6천짜리 리스차 끄는 무일푼 남친. #jtbc #연애전쟁 #사랑"), "연예·예능·드라마"),
            (x("고객놈 주식 파산시킨 신입 주식 브로커의 최후", desc="소개해드린 영상은 풀 버전 감상을 적극 권장드립니다. 영화 : 돈"), "연예·예능·드라마"),
            (x("노후에 초라해지는 최악의 습관  #명언 #노년 #노후 #60대"), "명언·인생조언"),
            (x("사면된 박근혜가 받고 있는 대통령연금은?"), "정치"),
            (x("노후차를 새 차처럼 만드는 3가지 꿀팁"), "다른 뜻"),
        ]
        for item, kind in cases:
            with self.subTest(title=item["title"]):
                self.assertTrue(self.off(item).startswith(f"{sh.OFF_KIND} — {kind}("), self.off(item))

    def test_kept_money_titles(self):
        """2026-10-15 실측 오탐 — 남아야 하는 돈 이야기."""
        for item in (x("외국인들이 삼전·닉스 파는 진짜 이유?/ 자사주 소각 #채널A #shorts #경제시그널"),     # '자사주' ≠ 사주
                     x("단타로 샀는데 장기투자 중? 물린 주주 멘탈 변화 11단계"),                         # '단타로' ≠ 타로
                     x("친정 부모님이 노후 자금 털어 사주신 아파트"),                                   # '사주신' = 사 주다
                     x("주식 오래 한 사람들이 결국 깨닫는 투자 원칙 10가지 #명언"),                     # 명언이어도 돈 이야기
                     x("세계 8대 불가사의는 피라미드가 아닙니다 #복리 #투자 #돈공부", "삶의 방향키 명언"),
                     x("8월대전망 빈센트 vs. 알상무 #장르만여의도 #코스피 #이재명"),                    # 정치는 해시태그 뺀 제목만
                     x("부모님 보살핌 비용, 노후 자금으로 얼마나 들까"),                              # '보살핌' ≠ 보살
                     x("국민연금 30% 덜 받아도… 전문가가 당겨 받겠다는 이유")):
            with self.subTest(title=item["title"]):
                self.assertEqual(self.off(item), "")
                self.assertEqual(self.off(item, "stock"), "")

    def test_reviewed_video_list(self):
        why = self.off(x("외국인이 한국에서부러워하는 노후", vid="v9w_oAOUVEQ"))
        self.assertTrue(why.startswith(f"{sh.OFF_KIND} — 다른 뜻(눈으로 봄"), why)
        self.assertEqual(self.off(x("외국인이 한국에서부러워하는 노후", vid="v9w_oAOUVEQ"), "stock"), "")   # 다른 주제엔 안 씀

    def test_flags_and_not_info_comments(self):
        rules = self.rules["economic"]
        item = {**x("노후에 상처 안 받는 지혜로운 10가지 #명언"), "is_short": True, "short_basis": "세로", "tags": [], "views": 1000,
                "likes": 50, "comments_total": 5, "live": False, "was_live": False, "audio_lang": "ko", "lang": "ko"}
        self.assertTrue(sh.flags(item, rules, {"strong": ["노후"], "weak": [], "exclude": []}).startswith(sh.OFF_KIND))
        rx = rules["shorts_needs"]["NOT_INFO_RX"]
        for t in ("65뱀띠 재물복 부탁드립니다 감사합니다 선생님", "트롯 한곡 조심히 부탁드립니다", "62년생 로또1등당첨 꼭되게해주세요"):
            self.assertTrue(rx.search(t), t)
        for t in ("우선 1억을 어떻게 모으는지 알려주세요", "고가매수가 위험한 진짜 이유도 올려주세요", "당겨받는 이유가 궁금한데 안나오네"):
            self.assertFalse(rx.search(t), t)
        success = [{"no": 1, "id": "a", "comments": [{"text": "65뱀띠 재물복 부탁드립니다", "likes": 3, "reply": False, "creator": False},
                                                       {"text": "우선 1억을 어떻게 모으는지 알려주세요", "likes": 1, "reply": False, "creator": False}]}]
        nd = sh.comment_needs(success, rules)
        self.assertEqual(nd["not_info_asks"], 1)
        self.assertEqual([q["text"] for q in nd["requests"]], ["우선 1억을 어떻게 모으는지 알려주세요"])


if __name__ == "__main__":
    unittest.main()
