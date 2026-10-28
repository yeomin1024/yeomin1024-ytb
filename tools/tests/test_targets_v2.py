#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-28 — 분석 대상 세 묶음 고침 시험 (사용자 지시 2026-10-28 "1은 그렇게하고 최근에 조회수가 높을수록 더 많이 반영되도록
#          해야해 3은 할당량 남으면 진행하도록 해 나머지는 너가 추천하는 방향으로 하고"): outlier_research v2.7 views_per_day·latest_fetch·
#          success_metric·success_core·기간 없는 검색(publishedAfter 없음·남김) · success_analysis v1.6 case_weight·wshare·기간 없는 검색 캐시 나누기·
#          views_top_group · web_ui v2.5 preselect(③)·preselect_shorts(②·③). 네트워크·GitHub 요청 없음 (임시 폴더만).
"""python3 -m unittest test_targets_v2  (tools/tests 에서)"""
import json
import os
import shutil
import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
for k in ("GITHUB_TOKEN", "GH_TOKEN"):
    os.environ.pop(k, None)
import outlier_research as orr      # noqa: E402
import success_analysis as sa       # noqa: E402
import web_ui as web                # noqa: E402

web.orr = orr
NOW = datetime(2026, 10, 28, tzinfo=timezone.utc)
S_NEW = {"MAX_AGE_DAYS": 180, "MAX_SUBS": 50000, "MIN_RATIO": 3.0, "MIN_VIEWS": 10000, "MIN_MINUTES": 4.0, "CASES_PER_CHANNEL": 2,
         "MIN_AGE_DAYS": 7, "MIN_VPD_SUBS": 0.1, "WEIGHT": "score"}
S_OLD = {**S_NEW, "MIN_AGE_DAYS": 0, "MIN_VPD_SUBS": 0, "WEIGHT": ""}


class VpdTest(unittest.TestCase):
    def test_views_per_day_uses_fetch_time(self):
        pub = NOW - timedelta(days=20)
        self.assertEqual(orr.views_per_day(100000, pub, (NOW - timedelta(days=10)).isoformat(), NOW), 10000.0)   # ÷ 받은 때까지 10일
        self.assertEqual(orr.views_per_day(100000, pub, None, NOW), 5000.0)                                    # 받은 때 모름 → 오늘까지 20일
        self.assertEqual(orr.views_per_day(500, NOW - timedelta(hours=3), NOW.isoformat(), NOW), 500.0)       # 최소 1일
        self.assertEqual(orr.views_per_day(42, None, None, NOW), 42.0)                                        # 올린 날 모름 → ÷ 1 (예전과 같음)
        self.assertEqual(orr.views_per_day(10, "2026-10-18T00:00:00Z", "2026-10-23T00:00:00", NOW), 2.0)     # 글·시간대 없는 글

    def test_latest_fetch(self):
        self.assertEqual(orr.latest_fetch((100, "2026-10-01T00:00:00"), (150, "2026-10-05T00:00:00+00:00")), "2026-10-05T00:00:00+00:00")
        self.assertEqual(orr.latest_fetch((200, "2026-10-01T00:00:00"), (150, "2026-10-05T00:00:00")), "2026-10-01T00:00:00")
        self.assertIsNone(orr.latest_fetch((1, None), (2, "")))


class SuccessRuleTest(unittest.TestCase):
    def x(self, views, subs, age, vpd=None):
        return {"views": views, "subs": subs, "age_days": age, "vpd": vpd if vpd is not None else views / max(age, 1),
                "ratio": round(views / max(subs, 100), 2), "minutes": 10.0}

    def test_new_rule_is_per_day(self):
        young = self.x(60000, 10000, 20)          # ×6, 하루 3,000 = 구독자의 0.3 → 새 규칙 통과
        old = self.x(60000, 10000, 170)           # ×6 이지만 하루 353 = 0.035 → 새 규칙 탈락 (예전 규칙은 통과)
        self.assertTrue(orr.success_core(young, S_NEW))
        self.assertFalse(orr.success_core(old, S_NEW))
        self.assertTrue(orr.success_core(old, S_OLD))
        self.assertAlmostEqual(orr.success_metric(young, S_NEW), 0.3)
        self.assertEqual(orr.success_metric(young, S_OLD), 6.0)

    def test_age_views_subs_limits(self):
        self.assertFalse(orr.success_core(self.x(60000, 10000, 3), S_NEW))          # 7일 안 — 첫 며칠은 부풂
        self.assertTrue(orr.success_core(self.x(60000, 10000, 3), S_NEW, with_age=False))
        self.assertFalse(orr.success_core(self.x(9000, 1000, 20), S_NEW))           # 조회수 1만 미만
        self.assertFalse(orr.success_core(self.x(9_000_000, 60000, 20), S_NEW))     # 큰 채널
        self.assertFalse(orr.success_core({**self.x(60000, 10000, 20), "subs": None}, S_NEW))
        self.assertTrue(sa.is_success(self.x(60000, 10000, 20), S_NEW))
        self.assertFalse(sa.is_success({**self.x(60000, 10000, 20), "minutes": 3.0}, S_NEW))   # 롱폼 길이

    def test_explore_row_uses_views_per_day(self):
        r = {"views": 60000, "subs": 10000, "age_days": 20, "views_per_day": 3000.0, "ratio": 6.0, "minutes": 10.0}
        self.assertTrue(web._is_success(r, S_NEW))
        self.assertTrue(web._is_success(r))                                         # 규칙을 안 주면 예전 기본값 (×3)


class WeightTest(unittest.TestCase):
    def test_case_weight_log2(self):
        c = {"subs": 10000, "vpd": 1000.0, "views": 1, "ratio": 1}                    # 0.1 = 기준 → 1
        self.assertEqual(sa.case_weight(c, S_NEW), 1.0)
        self.assertEqual(sa.case_weight({**c, "vpd": 2000.0}, S_NEW), 2.0)            # 2배 → 2
        self.assertEqual(sa.case_weight({**c, "vpd": 8000.0}, S_NEW), 4.0)            # 8배 → 4
        self.assertEqual(sa.case_weight({**c, "vpd": 10 ** 9}, S_NEW), sa.W_CAP)      # 상한
        self.assertEqual(sa.case_weight({**c, "vpd": 8000.0}, S_OLD), 1.0)            # WEIGHT 꺼짐 → 1개씩

    def test_wshare(self):
        cs = [{"theme": "a", "weight": 3.0}, {"theme": "b", "weight": 1.0}]
        self.assertEqual(sa.wshare(cs, lambda c: c["theme"] == "a"), 0.75)
        self.assertEqual(sa.wshare([{"theme": "a"}, {"theme": "b"}], lambda c: c["theme"] == "a"), 0.5)   # 무게 없으면 1
        self.assertIsNone(sa.wshare([], lambda c: True))
        self.assertEqual(sa._share_txt(0.5, 0.75), "50% · 가중 75%")
        self.assertEqual(sa._share_txt(0.5, None), "50%")


class AlltimeSearchTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def test_api_search_without_published_after(self):
        seen = {}

        class FakeApi(orr.Api):
            def get(self, kind, _keep=None, **params):
                seen.update(params, _keep=_keep)
                return {"items": [{"id": {"videoId": "abc"}}], "pageInfo": {"totalResults": 1}}
        api = FakeApi("k", 10000)
        self.assertEqual(api.search("주식", None, "medium", lang=None, keep=2000), ["abc"])
        self.assertNotIn("publishedAfter", seen)
        self.assertEqual(seen["_keep"], 2000)
        api.search("주식", "2026-01-01T00:00:00Z", "medium")
        self.assertEqual(seen["publishedAfter"], "2026-01-01T00:00:00Z")

    def test_keep_reserve_stops_only_that_request(self):
        api = orr.Api("k", 2050)
        with self.assertRaises(orr.QuotaStop):
            api.get("search", _keep=2000, q="x")                                      # 2050 − 100 < 2000 남김 → 멈춤
        self.assertIsNone(api.stopped)                                                # 다른 요청은 계속 (멈춤 표시 없음)

    def test_cache_split(self):
        c = self.tmp
        (c / "search_a.json").write_text(json.dumps({"q": "주식", "dur": "medium", "fallback_days": 182, "since": "2026-04-01", "ids": ["w1"]}), "utf-8")
        (c / "search_b.json").write_text(json.dumps({"q": "주식", "dur": "medium", "fallback_days": 0, "since": None, "ids": ["old1", "w1"]}), "utf-8")
        (c / "search_c.json").write_text(json.dumps({"q": "주식", "dur": "short", "fallback_days": 0, "since": None, "ids": ["s1"]}), "utf-8")
        self.assertEqual(sa.load_alltime_ids(c), {"old1", "w1", "s1"})
        self.assertEqual(sa.load_alltime_ids(c, dur="short"), {"s1"})
        out = self.tmp / "out"
        (out / ".cache").mkdir(parents=True)
        for f in c.glob("search_*.json"):
            shutil.copy(f, out / ".cache" / f.name)
        searches, _, _ = sa.load_market_caches(out)
        self.assertEqual([d["fallback_days"] for d in searches], [182])               # 기간 없는 검색은 시장·② 에 안 섞임
        self.assertEqual(orr.search_cache_file(c, "q", "medium", 0, None) != orr.search_cache_file(c, "q", "medium", 182, None), True)

    def test_ttl_for_alltime(self):
        d = {"novel": [], "ttl_level": 0}
        h, level, useful = orr.search_ttl(self.tmp, d, orr.ALLTIME_TTL_HOURS, 0)
        self.assertEqual(level, 1)                                                    # 새 영상 없음 → 늦춤
        self.assertEqual(h, orr.ALLTIME_TTL_HOURS * 2)                                # 기간 비율 상한 없음


def row(i, views, vpd, short=False, src="검색:주식", window=True, flag=""):
    return {"id": f"v{i:03d}", "views": views, "views_per_day": vpd, "subs": 1_000_000, "ratio": 1.0, "in_window": window, "short": short,
            "relevant": True, "sources": [src], "flag": flag, "success": False, "age_days": 30 if window else 900}


class PreselectTest(unittest.TestCase):
    def test_views_top_includes_alltime(self):
        rows = [row(i, 1000 * i, 10) for i in range(1, 19)] + [row(100, 10 ** 8, 50, src="검색(전체 기간):주식", window=False),
                                                               row(101, 9 * 10 ** 7, 50, src="검색(전체 기간):주식", window=False)]
        info = {}
        r = web.preselect(rows, 0, info, views_pct=10)
        self.assertEqual(r.get("v100"), "조회수 상위")                                # 옛 영상(기간 밖)도 ③ 에 듦
        self.assertEqual(r.get("v101"), "조회수 상위")
        self.assertNotIn("v018", r)                                                   # 상위 10% = 20개 중 2개
        self.assertEqual(info["views_pool"], 20)
        self.assertEqual(info["views_pool_alltime_only"], 2)
        r_old = web.preselect(rows, 0)                                                # views_pct 0 → 예전 '기간 안 상위 20'
        self.assertNotIn("v100", r_old)
        self.assertEqual(r_old.get("v018"), "조회수 상위")

    def test_shorts_vpd_and_views(self):
        rows = [row(i, 1000 * i, 100 * i) for i in range(1, 21)] + [row(50, 10 ** 8, 5, src="검색(전체 기간):주식", window=False)]
        R = {"shorts_vpd_top": {"TOP_PCT": 10, "MAX_AGE_DAYS": 182}, "shorts_views_top": {"TOP_PCT": 5}}
        info = {}
        r = web.preselect_shorts(rows, {}, R, info)
        self.assertEqual([k for k, v in r.items() if v == "하루 조회수 상위"], ["v019"])   # v020 은 조회수로도 상위 → '조회수 상위' 가 덮음
        self.assertEqual(r.get("v050"), "조회수 상위")
        self.assertEqual(r.get("v020"), "조회수 상위")
        self.assertEqual((info["vpd_pool"], info["views_pool"]), (20, 21))


class ViewsTopGroupTest(unittest.TestCase):
    def test_group(self):
        def c(i, views, ch, age=30, exclude=""):
            return {"id": f"c{i}", "title": f"t{i}", "channel": ch, "channel_id": ch, "subs": 10 ** 6, "views": views, "vpd": views / age,
                    "ratio": 1.0, "age_days": age, "published": NOW - timedelta(days=age), "minutes": 10.0, "theme": "", "format": "",
                    "src": "설명", "comments_fetched": 0, "comments_total": 0, "exclude": exclude}
        pool = [c(i, 1000 * i, f"ch{i}") for i in range(1, 30)] + [c(100, 10 ** 7, "A", age=2000), c(101, 9 * 10 ** 6, "A", age=1500),
                                                                c(102, 8 * 10 ** 6, "A", age=1000), c(103, 7 * 10 ** 6, "B", exclude="주제 밖")]
        cases = [x for x in pool if x["id"] in ("c100", "c101", "c102", "c103")]
        rules = {"views_top": {"TOP_PCT": 10, "MIN_MINUTES": 4.0, "CASES_PER_CHANNEL": 2, "MIN_POOL": 10},
                 "success": {"MAX_AGE_DAYS": 180, "MAX_SUBS": 50000}}
        res, group = sa.views_top_group(cases, pool, {x["id"] for x in pool}, [], [], rules)
        self.assertEqual([g["id"] for g in group], ["c100", "c101"])                  # 채널당 2개 · 뺄 까닭(주제 밖) 뺌
        self.assertEqual(res["channel_cut"], 1)
        self.assertEqual(res["older_than_year_cases"], 2)
        self.assertEqual(res["pool"], 32)                                             # 뺄 까닭 있는 것은 모집단에서도 뺌
        off, g0 = sa.views_top_group(cases, pool, set(), [], [], {**rules, "views_top": {**rules["views_top"], "TOP_PCT": 0}})
        self.assertEqual((off["threshold"], g0), (None, []))                          # 0 = 끔


class ShortsTopGroupTest(unittest.TestCase):
    def test_vno_kept(self):
        import shorts_analysis as sha
        def c(i, views, age=10):
            return {"id": f"s{i}", "title": f"t{i}", "channel": f"ch{i}", "channel_id": f"ch{i}", "subs": 10 ** 6, "views": views, "vpd": views / age,
                    "ratio": 1.0, "age_days": age, "published": NOW - timedelta(days=age), "seconds": 30, "theme": "", "format": "", "src": "설명",
                    "comments_fetched": 0, "comments_total": 0, "exclude": "", "is_short": True}
        pool = [c(i, 1000 * i) for i in range(1, 40)]
        rules = {"shorts": {"MAX_SUBS": 50000}}
        res, group = sha.top_group("vpd", pool[-3:], pool, {"TOP_PCT": 10, "MAX_AGE_DAYS": 182, "CASES_PER_CHANNEL": 2, "MIN_POOL": 10}, [], rules)
        self.assertEqual([x["vno"] for x in res["cases"]], [1, 2, 3])                  # vpd 묶음의 V# 번호가 비지 않음 (2026-10-28 버그)
        res2, _ = sha.top_group("views", pool[-3:], pool, {"TOP_PCT": 10, "CASES_PER_CHANNEL": 2, "MIN_POOL": 10}, [], rules,
                                others={x["id"]: x["vno"] for x in group})
        self.assertEqual([x["tno"] for x in res2["cases"]], [1, 2, 3])
        self.assertEqual([x["vno"] for x in res2["cases"]], [1, 2, 3])                 # 1-5번 표의 V# 칸


if __name__ == "__main__":
    unittest.main()
