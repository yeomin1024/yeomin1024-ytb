#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-15 — 하루 검색 횟수 한도(HTTP 429 'Search Queries per day') 시험 (사용자 보고: "RuntimeError: HTTP 429 search: …
#          Quota exceeded for quota metric 'Search Queries' and limit 'Search Queries per day' … 왜 이래 사용량 3000 남았는데").
#          outlier_research v2.5 daily_limit_kind·검색만 멈춤 · pc_analysis v1.17 장부(검색 수·막힘·알려진 한도) · web_ui v2.3 탐색·이어서·화면 값.
#          진짜 YouTube·GitHub 에 요청하지 않는다 (test_quota_saving 의 Base — 임시 폴더를 ROOT 로, urlopen 가짜, GITHUB_TOKEN 류 지움).
"""cd tools/tests && python3 -m unittest test_search_limit -v"""
import io
import json
import sys
import types
import unittest
import urllib.error
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent))
from test_quota_saving import KEY, Base, FakeYouTube, orr, pc, web  # noqa: E402

SEARCH_DAY = ('{"error": {"code": 429, "message": "Quota exceeded for quota metric \'Search Queries\' and limit \'Search Queries per day\' '
              'of service \'youtube.googleapis.com\' for consumer \'project_number:1\'.", "status": "RESOURCE_EXHAUSTED", '
              '"errors": [{"reason": "rateLimitExceeded"}]}}')
UNITS_DAY = ('{"error": {"code": 429, "message": "Quota exceeded for quota metric \'Queries\' and limit \'Queries per day\' of service '
             '\'youtube.googleapis.com\'", "status": "RESOURCE_EXHAUSTED"}}')
PER_MINUTE = ('{"error": {"code": 429, "message": "Quota exceeded for quota metric \'Queries\' and limit \'Queries per minute\' of service '
              '\'youtube.googleapis.com\'", "status": "RESOURCE_EXHAUSTED"}}')


class FakeYTLimit(FakeYouTube):
    """search_ok 번 검색이 된 뒤로는 429 'Search Queries per day'. minute_errors 번은 분당 제한 429 (그다음 성공)."""

    def __init__(self, search_ok=2, minute_errors=0):
        super().__init__()
        self.search_ok, self.minute_errors, self.search_done = search_ok, minute_errors, 0

    def __call__(self, req, timeout=30):
        url = req.full_url if hasattr(req, "full_url") else str(req)
        if "/search?" in url:
            if self.minute_errors:
                self.minute_errors -= 1
                self.calls.append(("search429m", {}))
                raise urllib.error.HTTPError(url, 429, "Too Many Requests", {}, io.BytesIO(PER_MINUTE.encode()))
            if self.search_done >= self.search_ok:
                self.calls.append(("search429", {}))
                raise urllib.error.HTTPError(url, 429, "Too Many Requests", {}, io.BytesIO(SEARCH_DAY.encode()))
            self.search_done += 1
        return super().__call__(req, timeout)


class TestClassify(unittest.TestCase):
    def test_daily_limit_kind(self):
        self.assertEqual(orr.daily_limit_kind(429, SEARCH_DAY), "search_daily")
        self.assertEqual(orr.daily_limit_kind(403, SEARCH_DAY), "search_daily")
        self.assertEqual(orr.daily_limit_kind(429, UNITS_DAY), "daily")
        self.assertEqual(orr.daily_limit_kind(403, '{"error": {"errors": [{"reason": "quotaExceeded"}], "message": "quota"}}'), "daily")
        self.assertIsNone(orr.daily_limit_kind(429, PER_MINUTE))                 # 분당 제한 — 다시 하면 됨
        self.assertIsNone(orr.daily_limit_kind(404, SEARCH_DAY))


class TestSearchLimit(Base):
    def setUp(self):
        super().setUp()
        self.urlopen.stop()
        self.yt = FakeYTLimit(search_ok=2)
        self.urlopen = mock.patch.object(orr.urllib.request, "urlopen", self.yt)
        self.urlopen.start()
        web.orr = orr
        web.wa = types.SimpleNamespace(run=lambda t: {"windows": [], "cases": 0}, load_cases=lambda out: [])
        d = self.root / "economic"
        d.mkdir()
        (d / "analyzer_config.toml").write_text('[topic]\nTOPIC = "e"\nPROJECT_FOLDER = "economic"\n', "utf-8")
        (d / "keywords.txt").write_text("연금\n", "utf-8")
        web.STATE.update(topic="economic", topics=["economic"], port=8765)
        web.release_topic()
        web.JOBS.clear()
        self.ac = mock.patch.object(orr, "fetch_autocomplete", lambda q, c, refresh=False, fetch=None: ([], True))
        self.ac.start()

    def tearDown(self):
        self.ac.stop()
        web.release_topic()
        super().tearDown()

    def test_explore_stops_searches_only(self):
        (self.root / "economic" / "keywords.txt").write_text("연금\n노후\n", "utf-8")
        self.yt.search_ids[("연금", "medium")] = ["aaaaaaaaaa1", "aaaaaaaaaa2"]
        self.yt.search_ids[("연금", "long")] = ["bbbbbbbbbb1"]
        r = web.job_explore("economic", 8, True)                                # 예전: RuntimeError 로 탐색이 통째로 멈춤
        self.assertEqual(r["pending"], ["노후 (medium)", "노후 (long)"])          # 3번째 검색에서 막힘 → 나머지 검색은 이어서 할 것으로
        self.assertIn("검색 횟수 한도", r["search_stop"])
        self.assertEqual(self.yt.count("search429"), 1)                          # 막힌 뒤에는 검색을 더 보내지 않음
        self.assertGreaterEqual(self.yt.count("videos"), 1)                      # 영상 정보(1단위)는 계속
        ex = json.loads((self.root / "economic" / "result" / "web" / "explore.json").read_text("utf-8"))
        self.assertEqual({x["id"] for x in ex["rows"]}, {"aaaaaaaaaa1", "aaaaaaaaaa2", "bbbbbbbbbb1"})
        self.assertEqual(ex["search_stop"], "search_daily")
        q = web.quota_view("economic")
        self.assertEqual(q["searches"], 2)
        self.assertEqual(q["search_blocked"]["at"], 2)
        self.assertEqual(q["search_cap"], 2)
        self.assertEqual(q["used"], 2 * 100 + self.yt.count("videos") + self.yt.count("channels"))   # 거부된 검색은 장부에서 돌려줌
        est = web.estimate("economic", 8, True)
        self.assertTrue(est["search_blocked"])
        self.assertEqual(est["search_cap"], 2)
        # 같은 키의 다른 창·주제(새 Api)도 오늘은 검색을 보내지 않음
        api = orr.Api(KEY, 5000, ledger=pc.KeyLedger(KEY), what="t", topic="x")
        with self.assertRaises(orr.QuotaStop) as cm:
            api.search("다른 주제", "2026-08-01T00:00:00Z", "medium")
        self.assertEqual(cm.exception.kind, "search_daily")
        self.assertEqual(self.yt.count("search429"), 1)
        # 이어서 하기: 남은 것이 검색뿐이면 오늘은 건너뜀
        self.assertEqual(web._resume_explore("economic", "시험"), {"explore_resume": "검색 횟수 한도 — 다음 초기화 뒤"})

    def test_next_day_searches_again_and_cap_kept(self):
        kl = pc.KeyLedger(KEY)
        kl.count_search(3)
        kl.mark_search_blocked("시험")
        self.assertTrue(kl.search_blocked())
        tomorrow = pc.KeyLedger(KEY, now_fn=lambda: datetime.now(timezone.utc) + timedelta(days=1))
        self.assertIsNone(tomorrow.search_blocked())                             # 초기화 뒤 = 새 날 → 다시 검색
        self.assertEqual(tomorrow.snapshot()["searches"], 0)
        self.assertEqual(tomorrow.search_cap(), 3)                               # 알려진 한도는 남음
        tomorrow.count_search(5)
        tomorrow.mark_search_blocked("시험")
        self.assertEqual(tomorrow.search_cap(), 3)                               # 가장 작은 값

    def test_per_minute_429_retries(self):
        self.yt.minute_errors = 1
        self.yt.search_ids[("연금", "medium")] = ["aaaaaaaaaa1"]
        api = orr.Api(KEY, 5000, ledger=pc.KeyLedger(KEY))
        with mock.patch.object(orr.time, "sleep") as sl:
            ids = api.search("연금", "2026-08-01T00:00:00Z", "medium")
        self.assertEqual(ids, ["aaaaaaaaaa1"])
        self.assertEqual(self.yt.count("search429m"), 1)
        self.assertTrue(sl.called)
        self.assertIsNone(api.search_stopped)

    def test_units_day_429_stops_everything(self):
        api = orr.Api(KEY, 5000, ledger=pc.KeyLedger(KEY))
        url = "https://www.googleapis.com/youtube/v3/videos"

        def boom(req, timeout=30):
            raise urllib.error.HTTPError(url, 429, "Too Many Requests", {}, io.BytesIO(UNITS_DAY.encode()))
        with mock.patch.object(orr.urllib.request, "urlopen", boom):
            with self.assertRaises(orr.QuotaStop) as cm:
                api.videos(["aaaaaaaaaa1"])
        self.assertEqual(cm.exception.kind, "daily")
        self.assertTrue(pc.KeyLedger(KEY).snapshot()["exhausted"])


if __name__ == "__main__":
    unittest.main()
