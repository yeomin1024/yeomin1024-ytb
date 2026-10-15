#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-15 — 할당량 아끼기·키 장부·창 잠금·초기화 뒤 이어서 시험 (사용자 지시: "유튜브 분석 코드를 최대한 api 사용량
#          덜쓰는 방법(단어 줄이는 방법 말고) 찾아서 수정해보고 웹 ui에 사용량 얼마나 남았는지 표시하고 그리고 분석기 여러개 열어서 각자 다른
#          주제로 탐색해도 되지? … 사용량 초기화되면 자동으로 다시 분석 마저 하는거지? 그렇게 되야해").
#          진짜 YouTube·GitHub 에 요청하지 않는다: urlopen 을 가짜로 바꾸고, 저장소 대신 임시 폴더를 ROOT 로, GITHUB_TOKEN 류는 지움.
"""python3 -m unittest tools.tests.test_quota_saving -v"""
import io
import json
import os
import subprocess
import sys
import tempfile
import threading
import types
import unittest
import urllib.error
import urllib.parse
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest import mock

TOOLS = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(TOOLS))
import outlier_research as orr   # noqa: E402
import pc_analysis as pc         # noqa: E402
import web_ui as web             # noqa: E402

KEY = "AIza-test-key-not-real-000"


def _iso(dt):
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


class _Resp(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *a):
        self.close()


class FakeYouTube:
    """urlopen 대신 — 요청 종류별로 셈. search 결과는 self.search_ids[(q, dur)] (없으면 빈 목록)."""

    def __init__(self):
        self.calls = []
        self.search_ids = {}
        self.uploads = {}            # playlistId → [영상ID] (최근 것부터)
        self.comments = {}           # videoId → 최상위 댓글 수
        self.quota_403 = False
        self.now = datetime.now(timezone.utc)

    def __call__(self, req, timeout=30):
        url = req.full_url if hasattr(req, "full_url") else str(req)
        u = urllib.parse.urlparse(url)
        kind = u.path.rsplit("/", 1)[-1]
        q = {k: v[0] for k, v in urllib.parse.parse_qs(u.query).items()}
        assert q.get("key") == KEY, "키가 요청에 들어가야 함"
        self.calls.append((kind, q))
        if self.quota_403:
            raise urllib.error.HTTPError(url, 403, "Forbidden", {}, io.BytesIO(b'{"error":{"errors":[{"reason":"quotaExceeded"}],"message":"quota"}}'))
        if kind == "search":
            ids = self.search_ids.get((q["q"], q.get("videoDuration")), [])
            data = {"items": [{"id": {"videoId": v}} for v in ids], "pageInfo": {"totalResults": len(ids) * 10}}
        elif kind == "videos":
            data = {"items": [self._video(v) for v in q["id"].split(",")]}
        elif kind == "channels":
            data = {"items": [{"id": c, "snippet": {"title": "채널 " + c[-4:], "publishedAt": "2025-01-01T00:00:00Z"},
                               "statistics": {"subscriberCount": "1200", "videoCount": "40", "viewCount": "90000"}}
                              for c in q["id"].split(",")]}
        elif kind == "playlistItems":
            ids = self.uploads[q["playlistId"]]
            start = int(q.get("pageToken") or 0)
            page = ids[start:start + 50]
            data = {"items": [{"contentDetails": {"videoId": v}} for v in page]}
            if start + 50 < len(ids):
                data["nextPageToken"] = str(start + 50)
        elif kind == "commentThreads":
            n = self.comments.get(q["videoId"], 0)
            if q.get("order") == "relevance":
                rng = range(min(100, n))
                nxt = None
            else:
                start = int(q.get("pageToken") or 0)
                rng = range(start, min(n, start + 100))
                nxt = str(start + 100) if start + 100 < n else None
            data = {"items": [{"snippet": {"totalReplyCount": 0, "topLevelComment": {
                "id": f"c{q['videoId']}_{i}", "snippet": {"textDisplay": f"댓글 {i}", "likeCount": i % 7, "publishedAt": "2026-10-01T00:00:00Z",
                                                          "authorChannelId": {"value": "UCx"}}}}} for i in rng]}
            if nxt:
                data["nextPageToken"] = nxt
        elif kind == "comments":
            data = {"items": []}
        else:
            raise AssertionError(kind)
        return _Resp(json.dumps(data).encode("utf-8"))

    def _video(self, v):
        return {"id": v, "snippet": {"title": f"재테크 연금 이야기 {v}", "channelTitle": "작은 채널", "channelId": ("UC" + v * 3)[:24].ljust(24, "x"),
                                     "publishedAt": _iso(self.now - timedelta(days=10)), "description": "연금 세금", "tags": ["연금"],
                                     "liveBroadcastContent": "none", "defaultAudioLanguage": "ko"},
                "contentDetails": {"duration": "PT12M"}, "statistics": {"viewCount": "50000", "likeCount": "900", "commentCount": "40"}}

    def count(self, kind):
        return sum(1 for k, _ in self.calls if k == kind)


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.env = mock.patch.dict(os.environ, {"YOUTUBE_API_KEY": KEY}, clear=False)
        self.env.start()
        for name in list(os.environ):                     # 시험이 진짜 GitHub 에 올리지 않게 (CLAUDE.md)
            if name.startswith(("GITHUB_TOKEN", "GH_TOKEN")):
                os.environ.pop(name)
        self.patches = [mock.patch.object(pc, "ROOT", self.root), mock.patch.object(orr, "ROOT", self.root),
                        mock.patch.object(web, "ROOT", self.root)]
        for p in self.patches:
            p.start()
        self.yt = FakeYouTube()
        self.urlopen = mock.patch.object(orr.urllib.request, "urlopen", self.yt)
        self.urlopen.start()
        (self.root / ".yt_work").mkdir()

    def tearDown(self):
        self.urlopen.stop()
        for p in self.patches:
            p.stop()
        self.env.stop()
        self.tmp.cleanup()


class TestKeyLedger(Base):
    def test_shared_between_windows_and_day_reset(self):
        a, b = pc.KeyLedger(KEY), pc.KeyLedger(KEY)          # 창 두 개 = 장부 객체 두 개, 파일 하나
        self.assertEqual(a.left(), pc.DAILY_LIMIT - pc.DAILY_MARGIN)
        self.assertTrue(a.reserve(100, "web_explore", "economic"))
        self.assertTrue(b.reserve(1, "web_explore", "health"))
        self.assertEqual(b.used(), 101)
        a.refund(1, "web_explore", "health")
        snap = b.snapshot()
        self.assertEqual(snap["used"], 100)
        self.assertEqual(snap["by_topic"], {"economic": 100, "health": 0})
        self.assertRegex(snap["reset_kst"], r"^\d\d-\d\d \d\d:\d\d$")
        self.assertNotIn(KEY, a.p.read_text("utf-8"))          # 키 자체는 파일에 없음
        self.assertNotIn(KEY, a.p.name)
        # 남은 양보다 크면 적지 않음
        self.assertFalse(a.reserve(pc.DAILY_LIMIT, "x", "economic"))
        self.assertEqual(a.used(), 100)
        # 다음 태평양 날짜 = 0부터
        later = pc.KeyLedger(KEY, now_fn=lambda: datetime.now(timezone.utc) + timedelta(days=1))
        self.assertEqual(later.used(), 0)

    def test_exhausted_means_zero_left(self):
        k = pc.KeyLedger(KEY)
        k.mark_exhausted("search 403 quota")
        self.assertEqual(k.left(), 0)
        self.assertTrue(k.snapshot()["exhausted"])
        self.assertFalse(k.reserve(1, "x", "economic"))

    def test_topic_ledger_forwards_once(self):
        led = pc.Ledger("economic")
        led.add(300, "outlier")                               # 자동 실행 (하위 도구가 끝난 뒤 보고)
        led.add(50, "web_explore", forward=False)             # 웹 화면 (요청마다 이미 키 장부에 적음)
        self.assertEqual(led.used(), 350)
        self.assertEqual(pc.KeyLedger(KEY).used(), 300)


class TestApiLedger(Base):
    def test_other_window_usage_stops_search_but_not_small_requests(self):
        kl = pc.KeyLedger(KEY, limit=500, margin=0)
        other = pc.KeyLedger(KEY, limit=500, margin=0)
        other.add(300, "web_explore", "health")               # 다른 창(다른 주제)이 이미 300 씀 → 남은 200
        api = orr.Api(KEY, 10000, ledger=kl, what="web_explore", topic="economic")
        self.yt.search_ids[("연금", "medium")] = ["a" * 11]
        with self.assertRaises(orr.QuotaStop) as cm:          # 100 + 검색 여유 150 > 200
            api.search("연금", "2026-08-01T00:00:00Z", "medium")
        self.assertEqual(cm.exception.kind, "shared")
        self.assertEqual(self.yt.count("search"), 0)          # 요청을 보내지 않음
        items = api.videos(["a" * 11])                        # 1단위 요청은 계속
        self.assertEqual(len(items), 1)
        self.assertEqual(kl.used(), 301)
        self.assertEqual(api.used, 1)

    def test_daily_403_marks_exhausted_and_refunds(self):
        kl = pc.KeyLedger(KEY)
        api = orr.Api(KEY, 10000, ledger=kl, what="web_explore", topic="economic")
        self.yt.quota_403 = True
        with self.assertRaises(orr.QuotaStop) as cm:
            api.videos(["b" * 11])
        self.assertEqual(cm.exception.kind, "daily")
        self.assertEqual(kl.used(), 0)                        # 받지 못한 요청은 돌려줌
        self.assertTrue(kl.snapshot()["exhausted"])
        self.assertEqual(kl.left(), 0)


class TestSavings(Base):
    def _video_cache(self, cache, ids, days_old=10, minutes=12):
        for v in ids:
            (cache / f"{v}.json").write_text(json.dumps({
                "id": v, "title": f"재테크 {v}", "duration": minutes * 60, "live": False, "was_live": False, "audio_lang": "ko",
                "published": _iso(datetime.now(timezone.utc) - timedelta(days=days_old)), "channel_id": "UC" + "y" * 22,
                "fetched": datetime.now(timezone.utc).isoformat()}), "utf-8")

    @staticmethod
    def _age_search_caches(cache, hours):
        for f in cache.glob("search_*.json"):
            d = json.loads(f.read_text("utf-8"))
            d["fetched"] = (datetime.fromisoformat(d["fetched"]) - timedelta(hours=hours)).isoformat()
            f.write_text(json.dumps(d), "utf-8")

    def _simulate(self, adaptive, weeks=12, window_days=56, stable=20, churn=20):
        """매주 한 번 탐색(검색어 stable+churn 개 × 4~20분·20분 넘음) — 안정된 검색어는 결과가 그대로, 바뀌는 검색어는 매주 새 영상 10개."""
        cache = self.root / f"cache_{adaptive}"
        cache.mkdir()
        api = orr.Api(KEY, 10 ** 7)
        qs = [f"안정{i}" for i in range(stable)] + [f"변화{i}" for i in range(churn)]
        for i, q in enumerate(qs):
            for dur in ("medium", "long"):
                base = [f"{'s' if q.startswith('안정') else 'c'}{i:02d}{dur[0]}{k:06d}"[:11] for k in range(40)]
                self.yt.search_ids[(q, dur)] = base
        start = self.yt.count("search")
        with mock.patch.object(orr, "search_ttl", orr.search_ttl if adaptive else (lambda c, d, base, w, now=None: (base, 0, None))):
            for week in range(weeks):
                for i, q in enumerate(qs):
                    for dur in ("medium", "long"):
                        if q.startswith("변화"):          # 매주 새 영상 10개가 위에 올라옴
                            new = [f"n{week:02d}{i:02d}{dur[0]}{k:05d}"[:11] for k in range(10)]
                            self.yt.search_ids[(q, dur)] = new + self.yt.search_ids[(q, dur)][:40]
                            self._video_cache(cache, new)
                        orr.cached_search(api, cache, q, "2026-08-01T00:00:00Z", dur, window_days, orr.SEARCH_TTL_HOURS, False)
                self._age_search_caches(cache, 7 * 24 + 1)
        return self.yt.count("search") - start

    def test_adaptive_search_ttl_saves_on_stable_queries(self):
        fixed = self._simulate(adaptive=False)
        adaptive = self._simulate(adaptive=True)
        print(f"\n[SIM] 12주·검색어 40개(안정 20·바뀜 20)×2 길이, 8주 기간: 고정 7일 {fixed}번({fixed * 100:,}단위) → 적응형 {adaptive}번"
              f"({adaptive * 100:,}단위), {100 * (fixed - adaptive) / fixed:.0f}% 덜 씀")
        self.assertEqual(fixed, 40 * 2 * 12)
        self.assertLess(adaptive, fixed)
        # 바뀌는 검색어는 매주 새로 고침 (최근 영상을 놓치지 않음): 20 × 2 × 12 = 480 이 모두 들어 있어야 함
        self.assertGreaterEqual(adaptive, 480)

    def test_ttl_cap_follows_window(self):
        d = {"novel": [], "ttl_level": 5, "fetched": datetime.now(timezone.utc).isoformat()}
        self.assertEqual(orr.search_ttl(self.root, d, 168, 56)[0], 336)      # 8주 기간 → 14일까지
        self.assertEqual(orr.search_ttl(self.root, d, 168, 84)[0], 504)      # 12주 → 21일
        self.assertEqual(orr.search_ttl(self.root, d, 168, 14)[0], 168)      # 2주 → 7일 그대로 (기본보다 짧게 하지 않음)
        self.assertEqual(orr.search_ttl(self.root, {"fetched": "x"}, 168, 56)[0], 168)   # 새로 고친 기록 없음 → 기본
        self._video_cache(self.root, [f"u{k:010d}" for k in range(3)])
        d2 = {"novel": [f"u{k:010d}" for k in range(3)], "ttl_level": 1}
        self.assertEqual(orr.search_ttl(self.root, d2, 168, 56)[:2], (168, 0))  # 쓸 만한 새 영상 3개 → 7일로 돌아감
        self._video_cache(self.root, ["shortshort1", "shortshort2", "shortshort3"], minutes=1)
        d3 = {"novel": ["shortshort1", "shortshort2", "shortshort3"], "ttl_level": 0}
        self.assertEqual(orr.search_ttl(self.root, d3, 168, 56)[:2], (336, 1))  # 쇼츠만 새로 보임 → 늦춤

    def test_channel_uploads_incremental(self):
        cache = self.root / "c"
        cache.mkdir()
        ch = {"id": "UC" + "z" * 22, "uploads": "UU" + "z" * 22, "title": "큰 채널"}
        self.yt.uploads[ch["uploads"]] = [f"v{k:010d}" for k in range(500)]
        api = orr.Api(KEY, 10 ** 6)
        ids = orr.channel_uploads(api, cache, ch, ttl_h=24)
        first = api.used
        self.assertEqual((len(ids), first), (500, 10))
        p = cache / f"uploads_{ch['id']}.json"
        d = json.loads(p.read_text("utf-8"))
        d["fetched"] = (datetime.now(timezone.utc) - timedelta(days=2)).isoformat()
        p.write_text(json.dumps(d), "utf-8")
        self.yt.uploads[ch["uploads"]] = ["new00000001", "new00000002", "new00000003"] + self.yt.uploads[ch["uploads"]]
        ids2 = orr.channel_uploads(api, cache, ch, ttl_h=24)
        print(f"\n[SIM] 영상 500개 채널 새로 고침: 예전 10단위 → {api.used - first}단위")
        self.assertEqual(api.used - first, 1)
        self.assertEqual(ids2[:3], ["new00000001", "new00000002", "new00000003"])
        self.assertEqual(len(ids2), 503)
        # 예전 형식(complete 없음 — 잘린 목록일 수 있음)은 한 번 끝까지 받음
        d = json.loads(p.read_text("utf-8"))
        d.pop("complete")
        d["fetched"] = (datetime.now(timezone.utc) - timedelta(days=2)).isoformat()
        p.write_text(json.dumps(d), "utf-8")
        before = api.used
        orr.channel_uploads(api, cache, ch, ttl_h=24)
        self.assertEqual(api.used - before, 11)

    def test_comments_single_page_skips_relevance(self):
        api = orr.Api(KEY, 10 ** 6)
        small, big = self.root / "small", self.root / "big"
        small.mkdir()
        big.mkdir()
        self.yt.comments.update({"smallvideo1": 40, "bigvideo001": 250})
        cms, st = orr.fetch_all_comments(api, small, "smallvideo1", "UCchan", 0, True, False, full=True)
        self.assertEqual((len(cms), st["units"], st["complete"], st.get("top_skipped")), (40, 1, True, True))   # 예전 2단위
        cms, st = orr.fetch_all_comments(api, big, "bigvideo001", "UCchan", 0, True, False, full=True)
        self.assertEqual((len(cms), st["units"], st["complete"]), (250, 4, True))    # 시간순 3쪽 + 인기 1쪽 (예전과 같음)
        orders = [q.get("order") for k, q in self.yt.calls if k == "commentThreads" and q["videoId"] == "bigvideo001"]
        self.assertEqual(orders, ["time", "relevance", "time", "time"])              # 인기 댓글은 둘째로 — 중간에 끊겨도 있음

    def test_video_ttl_by_age(self):
        now = datetime.now(timezone.utc)
        self.assertEqual(orr.video_ttl_h(_iso(now - timedelta(days=10)), now), 24)
        self.assertEqual(orr.video_ttl_h(_iso(now - timedelta(days=100)), now), 72)
        self.assertEqual(orr.video_ttl_h(_iso(now - timedelta(days=400)), now), 168)
        self.assertEqual(orr.video_ttl_h(None, now), 24)


class TestWindowsAndResume(Base):
    def setUp(self):
        super().setUp()
        web.orr = orr
        web.wa = types.SimpleNamespace(run=lambda t: {"windows": [], "cases": 0}, load_cases=lambda out: [])
        for t in ("economic", "health"):
            d = self.root / t
            d.mkdir()
            (d / "analyzer_config.toml").write_text(f'[topic]\nTOPIC = "{t}"\nPROJECT_FOLDER = "{t}"\n', "utf-8")
            (d / "keywords.txt").write_text("연금\n", "utf-8")
        web.STATE.update(topic="economic", topics=["economic", "health"], port=8765)
        web.WINDOW.update(lock=None, topic=None)
        web.JOB.update(status="idle", cancel=False)

    def tearDown(self):
        web.release_topic()
        super().tearDown()

    def test_one_topic_per_window(self):
        web.claim_topic("economic")
        lock_p = self.root / ".yt_work" / "web_health.lock"
        holder = subprocess.Popen([sys.executable, "-c", (
            "import sys,time;sys.path.insert(0,sys.argv[1]);import pc_analysis as pc;f=pc.os_lock(sys.argv[2]);"
            "print('locked',flush=True);time.sleep(30)"), str(TOOLS), str(lock_p)], stdout=subprocess.PIPE, text=True)
        try:
            self.assertEqual(holder.stdout.readline().strip(), "locked")      # 다른 창(프로세스)이 health 를 잡음
            (self.root / ".yt_work" / "web_health.json").write_text(json.dumps({"url": "http://127.0.0.1:8766/"}), "utf-8")
            self.assertEqual(web.topic_window("health")["url"], "http://127.0.0.1:8766/")
            with self.assertRaises(web.UserError) as cm:
                web.claim_topic("health")
            self.assertIn("8766", str(cm.exception))
            self.assertEqual(WINDOW_TOPIC(), "economic")                  # 실패하면 원래 주제 그대로
            wins = {w["topic"]: w for w in web.open_windows()}
            self.assertTrue(wins["economic"]["me"])
            self.assertFalse(wins["health"]["me"])
        finally:
            holder.kill()
            holder.wait()
            holder.stdout.close()
        self.assertIsNone(web.topic_window("health"))                      # 그 창이 꺼지면 OS 가 잠금을 풂
        web.claim_topic("health")
        self.assertEqual(WINDOW_TOPIC(), "health")

    def test_explore_resume_keeps_checks_and_finishes_pending(self):
        self.yt.search_ids[("연금", "medium")] = ["aaaaaaaaaa1", "aaaaaaaaaa2"]
        self.yt.search_ids[("연금", "long")] = ["bbbbbbbbbb1"]
        kl = pc.KeyLedger(KEY)
        kl.add(pc.DAILY_LIMIT - pc.DAILY_MARGIN - 160, "other", "health")       # 남은 160 → 검색 1번(100 + 여유 150) 못 함
        with mock.patch.object(orr, "fetch_autocomplete", lambda q, c, refresh=False, fetch=None: ([], True)):
            r = web.job_explore("economic", 8, True)
        self.assertEqual(len(r["pending"]), 2)                               # 두 검색 모두 남음
        plan = web.resume_plan("economic")
        self.assertTrue(plan["any"])
        self.assertEqual(plan["explore_searches"], 2)
        # 초기화 → 다음 날 장부 (0부터)
        tomorrow = lambda: datetime.now(timezone.utc) + timedelta(days=1)   # noqa: E731
        real = pc.KeyLedger.__init__

        def init(self_, key, now_fn=None, limit=None, margin=None):
            real(self_, key, tomorrow, limit, margin)
        with mock.patch.object(pc.KeyLedger, "__init__", init), \
                mock.patch.object(orr, "fetch_autocomplete", lambda q, c, refresh=False, fetch=None: ([], True)):
            ex = json.loads((self.root / "economic" / "result" / "web" / "explore.json").read_text("utf-8"))
            res = web.job_resume("economic", "시험")
            ex2 = json.loads((self.root / "economic" / "result" / "web" / "explore.json").read_text("utf-8"))
        self.assertTrue(res.get("explore_resumed"))
        self.assertEqual(res["explore_pending_after"], 0)
        self.assertEqual({r["id"] for r in ex2["rows"]}, {"aaaaaaaaaa1", "aaaaaaaaaa2", "bbbbbbbbbb1"})
        self.assertEqual(ex["rows"], [])
        self.assertEqual(self.yt.count("search"), 2)
        # 내가 체크를 풀어 둔 영상은 다시 탐색해도 풀린 채로
        ex2["checked"] = [i for i in ex2["checked"] if i != "aaaaaaaaaa1"]
        (self.root / "economic" / "result" / "web" / "explore.json").write_text(json.dumps(ex2), "utf-8")
        with mock.patch.object(pc.KeyLedger, "__init__", init), \
                mock.patch.object(orr, "fetch_autocomplete", lambda q, c, refresh=False, fetch=None: ([], True)):
            web.job_explore("economic", 8, True)
        ex3 = json.loads((self.root / "economic" / "result" / "web" / "explore.json").read_text("utf-8"))
        self.assertNotIn("aaaaaaaaaa1", ex3["checked"])
        self.assertEqual(self.yt.count("search"), 2)                          # 캐시 — 새 검색 없음

    def test_resume_loop_starts_job_after_reset(self):
        started = threading.Event()
        calls = []

        def fake_resume(t, why="할당량 초기화"):
            calls.append((t, why))
            started.set()
            return {}
        soon = datetime.now(timezone.utc) + timedelta(seconds=1)
        with mock.patch.object(web, "job_resume", fake_resume), \
                mock.patch.object(web, "resume_plan", lambda t: {"any": True, "explore_searches": 3}), \
                mock.patch.object(web.pc, "next_quota_reset", lambda now, margin_min=10: (soon if now < soon else soon + timedelta(days=1), "시험")):
            threading.Thread(target=web._resume_loop, daemon=True).start()
            self.assertTrue(started.wait(15), "초기화 뒤 이어서 작업이 시작되지 않음")
        self.assertEqual(calls[0], ("economic", "할당량 초기화"))
        self.assertEqual(web.RESUME["status"], "started")

    def test_quota_view_and_create_topic(self):
        pc.KeyLedger(KEY).add(1234, "web_explore", "economic")
        q = web.quota_view("economic")
        self.assertEqual((q["used"], q["left"], q["topic_used"]), (1234, pc.DAILY_LIMIT - pc.DAILY_MARGIN - 1234, 1234))
        r = web.create_topic("side-job", "부업", "부업 추천\n# 메모\n투잡\n", push=False)
        self.assertEqual(r["keywords"], 2)
        cfg = (self.root / "side-job" / "analyzer_config.toml").read_text("utf-8")
        self.assertIn('PROJECT_FOLDER = "side-job"', cfg)
        self.assertIn("side-job", web.find_topics())
        kws = orr.load_keywords("side-job", 0)[0]
        self.assertEqual([q for _, q in kws], ["부업 추천", "투잡"])
        with self.assertRaises(web.UserError):
            web.create_topic("side-job", "부업", "")                     # 이미 있음
        with self.assertRaises(web.UserError):
            web.create_topic("../evil", "x", "")                          # 경로 밖으로 못 감
        with self.assertRaises(web.UserError):
            web.create_topic("ok-name", 'a"b', "")                        # 설정 파일을 깨는 이름


def WINDOW_TOPIC():
    return web.WINDOW["topic"]


if __name__ == "__main__":
    unittest.main()
