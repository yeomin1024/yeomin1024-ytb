#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-10-18 — niche_scan v1.1 시험 7개 더함 (TestShortsForeign): 쇼츠 성공 기준·거르기, 외국 영상을 켠 주제만 '외국 영상'을 남김,
#          is_foreign_info = outlier_research.is_foreign, foreign = true 분야 → keywords_foreign.txt, 쇼츠 보고서·외국 영상 몫·주제 관련 몫
#          (사용자 지시 2026-10-18 "수학문제 띄워놓고 시청자가 맞춰보는 영상이 조회수 잘 나오고 구독자 많이 모을 수 있는지 탐색해볼래?")
# (v1.0 — 2026-10-16 — 새 채널 분야 비교 tools/niche_scan.py v1.0 시험 (사용자 지시 2026-10-16: "… 어떤 채널을 만들어야 조회수 높은 영상
#          만들고 구독자 많이 모을 수 있을지 전체적으로 탐색해봐 저장소에 디렉토리 new로 만들어서 …").)
#          임시 폴더를 ROOT 로 — 진짜 YouTube·GitHub 에 요청하지 않음 (niche_scan 은 원래 인터넷을 쓰지 않음).
"""cd tools/tests && python3 -m unittest test_niche_scan -v"""
import csv
import json
import sys
import tempfile
import tomllib
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import niche_scan as ns          # noqa: E402
import outlier_research as orr   # noqa: E402
import success_analysis as sa    # noqa: E402

NOW = datetime(2026, 10, 16, 9, 0, tzinfo=timezone.utc)
NICHES = '''
[[niche]]
name = "01. 건강"
group = "A"
keywords = ["건강정보", "혈당"]
words = ["건강", "혈당"]
make = "중"
make_why = "검수 필요"

[[niche]]
name = "02. 역사"
group = "A"
keywords = ["역사 이야기", "세계사"]
words = ["역사"]
make = "상"
make_why = "지도"

[[niche]]
name = "03. 요리"
group = "B"
keywords = ["요리"]
words = ["요리"]
make = "하"
make_why = "촬영"
'''
RULES = '''
[success]
MAX_AGE_DAYS = 180
MAX_SUBS = 50000
MIN_RATIO = 3.0
MIN_VIEWS = 10000
MIN_MINUTES = 4.0
[compare]
MIN_AGE_DAYS = 7
PER_CHANNEL = 2
[growth]
NEW_CHANNEL_MONTHS = 24
MIN_SUBS = 1000
MAX_SUBS = 200000
[shorts]
MAX_SECONDS = 180
MIN_AGE_DAYS = 3
MAX_AGE_DAYS = 180
MAX_SUBS = 50000
MIN_RATIO = 3.0
MIN_VIEWS = 50000
[shorts_compare]
MIN_AGE_DAYS = 3
PER_CHANNEL = 2
[exclude]
OFF_TOPIC = ["토토"]
AD_SUSPECT_MIN_VIEWS = 50000
AD_SUSPECT_MAX_LIKE_RATE = 0.0025
AD_SUSPECT_MAX_COMMENT_RATE = 0.00005
'''


def row(vid, q, subs, views, age=30, minutes=10.0, ch=None, likes=None, comments=None, title=None, flag=""):
    qs = q if isinstance(q, list) else [q]
    return {"id": vid, "title": title or f"영상 {vid}", "channel": ch or f"ch_{vid}", "channel_id": ch or f"UC_{vid}", "subs": subs,
            "views": views, "ratio": round(views / max(subs, 100), 2) if subs is not None else None, "age_days": age,
            "views_per_day": round(views / max(age, 1), 1), "minutes": minutes,
            "likes": views // 50 if likes is None else likes, "comments": views // 500 if comments is None else comments,
            "published": "2026-09-16", "queries": "", "flag": flag, "sources": [f"검색:{x}" for x in qs]}


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "t1").mkdir()
        (self.root / "t1" / "niches.toml").write_text(NICHES, "utf-8")
        (self.root / "t1" / "analysis_rules.toml").write_text(RULES, "utf-8")

    def tearDown(self):
        self.tmp.cleanup()


class TestNiches(Base):
    def test_round_robin_order(self):
        n = ns.load_niches(self.root, "t1")
        self.assertEqual([k for _, k in ns.round_robin(n)], ["건강정보", "역사 이야기", "요리", "혈당", "세계사"])

    def test_duplicate_keyword_rejected(self):
        (self.root / "t1" / "niches.toml").write_text(NICHES.replace('keywords = ["요리"]', 'keywords = ["혈 당"]'), "utf-8")
        with self.assertRaises(SystemExit):
            ns.load_niches(self.root, "t1")

    def test_sync_files_readable_by_existing_tools(self):
        ns.cmd_sync(self.root, "t1")
        kws = orr.read_keyword_list(self.root / "t1" / "keywords.txt")
        self.assertEqual(kws, ["건강정보", "역사 이야기", "요리", "혈당", "세계사"])           # 주석 줄은 무시되고 순서 그대로
        themes = sa.load_themes(self.root, "t1")
        self.assertEqual(list(themes), ["01. 건강", "02. 역사", "03. 요리"])
        self.assertEqual(sa.theme_of("혈당 낮추는 음식", [], themes), "01. 건강")


class TestRules(Base):
    def setUp(self):
        super().setUp()
        self.S, self.C, self.G, self.E = ns.load_rules(self.root, "t1")

    def test_success_boundaries(self):
        ok = row("a", "건강정보", 50000, 150000, age=180)
        self.assertTrue(ns.is_success(ok, self.S))
        self.assertFalse(ns.is_success(dict(ok, subs=50001, ratio=None), self.S))           # 구독자 5만 넘음
        self.assertFalse(ns.is_success(dict(ok, views=149999), self.S))                     # 배수 3 미만
        self.assertFalse(ns.is_success(dict(ok, age_days=181), self.S))                     # 180일 넘음
        self.assertFalse(ns.is_success(dict(ok, subs=None), self.S))                        # 구독자 숨김 = 모름
        self.assertTrue(ns.is_success(row("b", "x", 10, 10000), self.S))                     # 구독자 100 미만은 100 으로 → ×100
        self.assertFalse(ns.is_success(row("c", "x", 10, 9999), self.S))                     # 조회수 1만 미만

    def test_drop_reasons(self):
        self.assertEqual(ns.drop_reason(row("a", "q", 100, 1000, age=6), self.S, self.C, self.E), "올린 지 7일 안 됨")
        self.assertEqual(ns.drop_reason(row("a", "q", 100, 1000, minutes=3.9), self.S, self.C, self.E), "짧음")
        self.assertEqual(ns.drop_reason(row("a", "q", 100, 1000, title="토토 분석"), self.S, self.C, self.E), "뺀 낱말")
        self.assertEqual(ns.drop_reason(row("a", "q", 100, 100000, likes=10, comments=1), self.S, self.C, self.E), "광고 의심")
        self.assertIsNone(ns.drop_reason(row("a", "q", 100, 100000, likes=10, comments=100), self.S, self.C, self.E))   # 댓글은 많음 → 아님
        self.assertEqual(ns.drop_reason(row("a", "q", 100, 1000, flag="외국 영상"), self.S, self.C, self.E), "외국 영상")


class TestReport(Base):
    def write_explore(self, rows, channels, pending=()):
        web = self.root / "t1" / "result" / "web"
        web.mkdir(parents=True)
        (web / "explore.json").write_text(json.dumps({"generated": "x", "weeks": 26, "rows": rows, "pending": list(pending)}, ensure_ascii=False), "utf-8")
        cache = self.root / "t1" / "result" / "outliers" / ".cache"
        cache.mkdir(parents=True)
        (cache / "channels.json").write_text(json.dumps(channels, ensure_ascii=False), "utf-8")
        f = orr.search_cache_file(cache, "건강정보", "medium", 182)
        f.write_text(json.dumps({"q": "건강정보", "dur": "medium", "fetched": NOW.isoformat(), "total": 1000000, "ids": ["h1", "h2"]}), "utf-8")

    def test_counts_and_score(self):
        new = (NOW - timedelta(days=300)).isoformat()                  # 개설 약 10개월
        old = (NOW - timedelta(days=3000)).isoformat()
        rows = [
            row("h1", "건강정보", 20000, 200000, ch="UCnew"),          # 성공, 새 채널(구독자 2만 → 2년 안 1만)
            row("h2", "혈당", 2_000_000, 900000, ch="UCbig"),          # 큰 채널
            row("h3", ["건강정보", "세계사"], 30000, 30000, ch="UCmid"),  # 두 분야 — 성공 아님(배수 1)
            row("h4", "건강정보", 1000, 5000, age=3),                   # 7일 안 → 뺌
            row("s1", "세계사", 5000, 60000, ch="UCold"),              # 성공, 오래된 채널
            row("x1", "모르는 검색어", 100, 100000),                     # 분야 없음 → 뺌 (경고)
        ]
        chans = {"UCnew": {"subs": 20000, "created": new, "title": "새채널", "videos": 30},
                 "UCbig": {"subs": 2_000_000, "created": old, "title": "큰채널"},
                 "UCmid": {"subs": 30000, "created": old, "title": "중간"},
                 "UCold": {"subs": 5000, "created": old, "title": "옛채널"}}
        self.write_explore(rows, chans, pending=["요리 (medium)", "요리 (long)"])
        S, C, G, E = ns.load_rules(self.root, "t1")
        res = {r["niche"]: r for r in ns.collect(rows, ns.load_niches(self.root, "t1"), chans, S, C, G, E, NOW)}
        h, s, c = res["01. 건강"], res["02. 역사"], res["03. 요리"]
        self.assertEqual((h["videos"], h["success"], h["channels"]), (3, 1, 3))
        self.assertEqual(h["dropped"], {"올린 지 7일 안 됨": 1})
        self.assertAlmostEqual(h["success_rate"], 0.333)
        self.assertEqual(h["big_share"], 0.333)
        self.assertEqual(h["small_share"], 0.667)
        self.assertEqual((h["new_channels"], h["new10k"]), (1, 1))
        self.assertEqual(h["fast"][0]["subs_per_month"], round(20000 / (300 / 30.44)))
        self.assertEqual((s["videos"], s["success"]), (2, 1))                       # h3 는 두 분야에 다 셈
        self.assertEqual((c["videos"], c["success_rate"]), (0, None))
        scored = ns.score(list(res.values()))
        self.assertEqual(scored[-1]["niche"], "03. 요리")                            # 값이 없으면 맨 뒤
        self.assertTrue(all(0 <= (r["score"] or 0) <= 100 for r in scored))

    def test_per_channel_cap_keeps_most_recent(self):
        """한 채널이 표본을 덮지 않게 — 채널당 최근 PER_CHANNEL(시험 2)개까지, 성공 여부와 무관하게 최근 순."""
        rows = [row(f"q{i}", "퀴즈", 1000, 100000, age=10 + i, ch="UCflood") for i in range(5)] + [row("o1", "퀴즈", 1000, 500, ch="UCother")]
        niches = ns.load_niches(self.root, "t1") + [{"name": "04. 퀴즈", "group": "A", "keywords": ["퀴즈"], "words": [], "make": "상", "make_why": ""}]
        S, C, G, E = ns.load_rules(self.root, "t1")
        r = {x["niche"]: x for x in ns.collect(rows, niches, {}, S, C, G, E, NOW)}["04. 퀴즈"]
        self.assertEqual(sorted(v["id"] for v in r["_videos"]), ["o1", "q0", "q1"])            # 가장 최근 2개 (10·11일)
        self.assertEqual(r["dropped"], {"채널당 2개 넘음": 3})
        self.assertEqual((r["videos"], r["channels"], r["success"]), (3, 2, 2))
        self.assertEqual(r["success_channel_share"], 0.5)

    def test_score_ignores_small_vpd_with_few_small_videos(self):
        """작은 채널 영상이 MIN_SMALL 개 미만이면 그 분야 점수에서 '작은 채널 하루 조회수'를 뺌 (2026-10-16 여행: 작은 채널 6개 → 중앙값 23,817)."""
        res = [{"niche": "a", "success_rate": 0.4, "small_vpd_median": 100.0, "small_n": 50, "new10k_share": 0.3},
               {"niche": "b", "success_rate": 0.1, "small_vpd_median": 99999.0, "small_n": 3, "new10k_share": 0.1},
               {"niche": "c", "success_rate": 0.2, "small_vpd_median": 50.0, "small_n": 40, "new10k_share": 0.2}]
        out = {r["niche"]: r for r in ns.score(res)}
        self.assertIsNone(out["b"]["pct_small_vpd_median"])
        self.assertEqual(out["b"]["score"], 0.0)                                   # 남은 두 숫자 모두 꼴찌
        self.assertEqual(out["a"]["score"], 100.0)

    def test_brand_hint(self):
        hints = ["KBS", "공식", "SOL"]
        self.assertEqual(ns.brand_hint("에헤라 티비 : KBS LIFE", hints), "KBS")
        self.assertEqual(ns.brand_hint("○○ 공식 채널", hints), "공식")
        self.assertIsNone(ns.brand_hint("Solar 이야기", hints))                    # 영문은 낱말 단위 — SOL ≠ Solar

    def test_report_files(self):
        rows = [row("h1", "건강정보", 20000, 200000), row("s1", "세계사", 5000, 60000)]
        self.write_explore(rows, {}, pending=["요리 (medium)"])
        out = ns.cmd_report(self.root, "t1", now=NOW)
        self.assertEqual(out["niches"], 3)
        md = (self.root / "t1" / "result" / "niche" / "niche_scan.md").read_text("utf-8")
        self.assertIn("## 1. 분야 비교", md)
        self.assertIn("| 03. 요리 | 요리 |", md)                                    # 검색어별 표 — 못 한 검색
        self.assertIn("1,000,000", md)                                              # 유튜브 결과 수 추정
        with (self.root / "t1" / "result" / "niche" / "niche_videos.csv").open(encoding="utf-8-sig") as f:
            got = list(csv.DictReader(f))
        self.assertEqual(sorted(r["id"] for r in got), ["h1", "s1"])
        self.assertEqual({r["success"] for r in got}, {"True"})

    def test_missing_explore_fails_clearly(self):
        with self.assertRaises(SystemExit) as e:
            ns.cmd_report(self.root, "t1", now=NOW)
        self.assertIn("탐색 목록이 없음", str(e.exception))


FOREIGN_NICHE = """
[[niche]]
name = "04. Math puzzle"
group = "A"
foreign = true
keywords = ["math puzzle", "mental math"]
words = ["math"]
"""


class TestShortsForeign(Base):
    """v1.1 — 쇼츠·외국 영상."""

    def test_shorts_success_rule(self):
        S, C, G, E = ns.load_rules(self.root, "t1", shorts=True)
        ok = dict(row("s", "q", 50000, 150000, age=3, minutes=0.5), seconds=30)
        self.assertTrue(ns.is_success(ok, S, shorts=True))
        self.assertFalse(ns.is_success(dict(ok, views=149999), S, shorts=True))          # 배수 3 미만
        self.assertFalse(ns.is_success(dict(row("t", "q", 1000, 49999, age=10, minutes=0.5), seconds=30), S, shorts=True))   # 쇼츠는 조회수 5만 이상
        self.assertFalse(ns.is_success(dict(ok, age_days=2), S, shorts=True))           # 3일 안 됨
        self.assertFalse(ns.is_success(dict(ok, age_days=181), S, shorts=True))
        S_long, *_ = ns.load_rules(self.root, "t1")
        self.assertFalse(ns.is_success(ok, S_long))                                      # 0.5분 → 롱폼 4분 기준에는 안 맞음 (섞이지 않음)

    def test_shorts_drop_reasons(self):
        S, C, G, E = ns.load_rules(self.root, "t1", shorts=True)
        base = dict(row("s", "q", 1000, 100000, age=10, minutes=0.5), seconds=30)
        self.assertIsNone(ns.drop_reason(base, S, C, E, shorts=True))                    # 4분 미만이어도 쇼츠는 빼지 않음
        self.assertEqual(ns.drop_reason(dict(base, age_days=2), S, C, E, shorts=True), "올린 지 3일 안 됨")
        self.assertEqual(ns.drop_reason(dict(base, seconds=181), S, C, E, shorts=True), "180초 넘음")
        self.assertEqual(ns.drop_reason(dict(base, flag="부풀림 의심"), S, C, E, shorts=True), "부풀림 의심")
        self.assertEqual(ns.drop_reason(dict(base, flag="쇼츠 아님?"), S, C, E, shorts=True), "쇼츠 아님?")
        self.assertIsNone(ns.drop_reason(dict(base, likes=1, comments=0), S, C, E, shorts=True))   # 롱폼 광고 의심 규칙은 안 씀 (표시가 맡음)

    def test_foreign_kept_only_when_on(self):
        S, C, G, E = ns.load_rules(self.root, "t1")
        r = row("f", "q", 1000, 100000, flag="외국 영상")
        self.assertEqual(ns.drop_reason(r, S, C, E), "외국 영상")
        self.assertIsNone(ns.drop_reason(r, S, C, E, foreign_ok=True))
        self.assertEqual(ns.drop_reason(dict(r, flag="라이브 방송"), S, C, E, foreign_ok=True), "라이브 방송")

    def test_is_foreign_info_matches_outlier_research(self):
        for info in ({"title": "Can you solve this?"}, {"title": "수학 퀴즈"}, {"title": "x", "audio_lang": "ko"}, {"title": "수학", "audio_lang": "en"},
                     {"title": "music", "audio_lang": "zxx"}, {"title": "음악", "lang": "und"}):
            self.assertEqual(ns.is_foreign_info(info), orr.is_foreign(info), info)

    def test_sync_writes_foreign_keywords(self):
        (self.root / "t1" / "niches.toml").write_text(NICHES + FOREIGN_NICHE, "utf-8")
        out = ns.cmd_sync(self.root, "t1")
        self.assertEqual((out["keywords"], out["foreign_keywords"]), (5, 2))
        self.assertEqual(orr.read_keyword_list(self.root / "t1" / "keywords_foreign.txt"), ["math puzzle", "mental math"])
        self.assertNotIn("math puzzle", orr.read_keyword_list(self.root / "t1" / "keywords.txt"))

    def test_sync_without_foreign_leaves_foreign_file(self):
        f = self.root / "t1" / "keywords_foreign.txt"
        f.write_text("stocks\n", "utf-8")
        self.assertEqual(ns.cmd_sync(self.root, "t1")["foreign_keywords"], 0)
        self.assertEqual(f.read_text("utf-8"), "stocks\n")                              # foreign 분야가 없으면 손대지 않음

    def test_shorts_report_with_foreign(self):
        (self.root / "t1" / "analyzer_config.toml").write_text("[search]\nINCLUDE_FOREIGN = true\n", "utf-8")
        (self.root / "t1" / "keywords.toml").write_text('[relevance]\nRELEVANCE_TERMS = ["건강"]\n', "utf-8")
        web = self.root / "t1" / "result" / "web"
        web.mkdir(parents=True)
        rows = [dict(row("e1", "건강정보", 20000, 300000, minutes=0.6), seconds=35, relevant=True),
                dict(row("k1", "건강정보", 20000, 300000, minutes=0.6), seconds=40, relevant=False),
                dict(row("b1", "혈당", 20000, 900000, minutes=0.5, likes=10), seconds=6, flag="부풀림 의심")]
        (web / "shorts_explore.json").write_text(json.dumps({"generated": "x", "weeks": 26, "rows": rows, "pending": ["요리 (short)"]}), "utf-8")
        sc = self.root / "t1" / "result" / "outliers" / ".cache" / "shorts"
        sc.mkdir(parents=True)
        (sc / "e1.json").write_text(json.dumps({"id": "e1", "title": "Health tips", "audio_lang": "en"}), "utf-8")
        (sc / "k1.json").write_text(json.dumps({"id": "k1", "title": "건강 꿀팁", "audio_lang": "ko"}), "utf-8")
        orr.search_cache_file(sc, "건강정보", "short", 182).write_text(
            json.dumps({"q": "건강정보", "dur": "short", "fetched": NOW.isoformat(), "total": 5000, "ids": ["e1", "k1"]}), "utf-8")
        out = ns.cmd_report(self.root, "t1", now=NOW, shorts=True)
        self.assertEqual(out["niches"], 3)
        d = self.root / "t1" / "result" / "niche"
        md = (d / "niche_scan_shorts.md").read_text("utf-8")
        self.assertIn("· 쇼츠 (숫자·원문만)", md)
        self.assertIn("외국 영상 몫", md)
        self.assertIn("주제 관련 몫", md)
        self.assertIn("| 01. 건강 | 건강정보 | 2 |", md)                                   # 쇼츠 검색 결과 칸 하나
        with (d / "niche_scan_shorts.csv").open(encoding="utf-8-sig") as f:
            h = {r["niche"]: r for r in csv.DictReader(f)}["01. 건강"]
        self.assertEqual((h["videos"], h["success"], h["foreign_share"], h["rel_share"]), ("2", "2", "0.5", "0.5"))   # 부풀림 의심은 뺌
        self.assertEqual(h["success_seconds_median"], "37.5")
        self.assertFalse((d / "niche_scan.md").exists())                                  # 롱폼 파일은 건드리지 않음


if __name__ == "__main__":
    unittest.main()
