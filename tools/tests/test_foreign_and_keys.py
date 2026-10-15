#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-15 — 외국 영상 켜고 끄기 · 주제마다 다른 키 시험 (사용자 지시: "야 키도 나눠서 쓸수 있게해 주제별로 다른키 넣을거니까
#          그리고 주식은 외국 영상도 다 분석할 건데 확인해봐 on/off 기능(default off) 있는지 확인하고 없으면 추가해").
#          outlier_research v2.4 · web_ui v2.1 · success_analysis v1.4 · shorts_analysis v1.2 · 분석기 v2.13.0 · pc_analysis v1.15.
#          진짜 YouTube·GitHub 에 요청하지 않는다 (test_quota_saving 의 Base — 임시 폴더를 ROOT 로, urlopen 가짜, GITHUB_TOKEN 류 지움).
"""cd tools/tests && python3 -m unittest test_foreign_and_keys -v"""
import hashlib
import json
import os
import sys
import tempfile
import tomllib
import types
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent))
from test_quota_saving import KEY, Base, FakeYouTube, orr, pc, web  # noqa: E402
from test_web_tabs import handler  # noqa: E402

import shorts_analysis as sh  # noqa: E402
import success_analysis as sa  # noqa: E402

REPO = Path(__file__).resolve().parents[2]
EN = "eeeeeeeeee1"          # 가짜 영어 영상
KO = "kkkkkkkkkk1"          # 가짜 한국어 영상
CONFIG = ('# 머리 주석\n[topic]\nTOPIC = "{t}"\nPROJECT_FOLDER = "{t}"\n\n[search]\nREGION_CODE = "KR"\nLANGUAGE = "ko"\n\n'
          '[advanced]\nQUOTA_BUDGET = 6000                  # 주석 그대로\n')


class FakeYT2(FakeYouTube):
    """ID 가 e 로 시작하면 영어 영상 (defaultAudioLanguage=en, 제목에 한글 없음)."""

    def _video(self, v):
        d = super()._video(v)
        if v.startswith("e"):
            d["snippet"].update(title=f"How I invest in stocks {v}", defaultAudioLanguage="en", description="stock market dividend",
                                tags=["stocks"])
        return d


def info(title, lang="", live=False):
    return {"id": "x", "title": title, "audio_lang": lang, "lang": "", "live": live, "was_live": False}


class TestRules(unittest.TestCase):
    def test_is_foreign_and_exclusion(self):
        self.assertTrue(orr.is_foreign(info("How to invest", "en")))
        self.assertTrue(orr.is_foreign(info("How to invest")))                 # 언어 표시 없음 + 한글 없음
        self.assertFalse(orr.is_foreign(info("ETF 투자 How to", "")))
        self.assertFalse(orr.is_foreign(info("Stock", "ko-KR")))
        self.assertFalse(orr.is_foreign(info("Music only", "zxx")))           # 말 없음 = 모름 → 빼지 않음
        nfd = __import__("unicodedata").normalize("NFD", "내 노후 10억이면 충분할까?")      # 맥에서 쓴 제목 (풀어쓴 자모)
        self.assertNotRegex(nfd, "[가-힣]")
        self.assertFalse(orr.is_foreign(info(nfd)))                            # 2026-10-15 실측 오탐 — 한국어 영상
        self.assertEqual(orr.exclusion_reason(info("How to invest", "en")), orr.FOREIGN)     # 기본 = 뺌 (예전 그대로)
        self.assertIsNone(orr.exclusion_reason(info("How to invest", "en"), foreign_ok=True))
        self.assertEqual(orr.exclusion_reason(info("Stocks LIVE", "en", live=True), foreign_ok=True), "라이브 방송")   # 라이브는 늘 뺌

    def test_build_rows_switch(self):
        from datetime import datetime, timezone
        now = datetime.now(timezone.utc)
        base = {"channel": "c", "channel_id": "UC1", "subs": 1000, "view_count": 9000, "duration": 600, "published": "2026-10-01T00:00:00Z"}
        infos = [{**base, "id": KO, "title": "주식 이야기", "audio_lang": "ko"}, {**base, "id": EN, "title": "Stocks", "audio_lang": "en"}]
        self.assertEqual([r["id"] for r in orr.build_rows(infos, {}, now)], [KO])
        rows = orr.build_rows(infos, {}, now, foreign_ok=True)
        self.assertEqual({r["id"]: r["flag"] for r in rows}, {KO: "", EN: orr.FOREIGN})       # 남기고 표시만
        self.assertEqual({r["id"]: r["flag"] for r in orr.build_rows(infos, {}, now, keep={EN})}, {KO: "", EN: orr.FOREIGN})   # 주소로 넣은 영상

    def test_search_cache_key(self):
        d = Path("/c")
        old = hashlib.sha1("주식|medium|56|viewCount|KR|ko".encode("utf-8")).hexdigest()[:16]
        self.assertEqual(orr.search_cache_file(d, "주식", "medium", 56).name, f"search_{old}.json")       # 끈 주제 캐시는 그대로
        self.assertEqual(orr.search_cache_file(d, "주식", "medium", 56, "ko"), orr.search_cache_file(d, "주식", "medium", 56))
        self.assertNotEqual(orr.search_cache_file(d, "주식", "medium", 56, None), orr.search_cache_file(d, "주식", "medium", 56))
        self.assertEqual((orr.search_lang(False), orr.search_lang(True)), ("ko", None))

    def test_useful_novel_counts_foreign_only_when_any(self):
        with tempfile.TemporaryDirectory() as td:
            (Path(td) / f"{EN}.json").write_text(json.dumps({"id": EN, "title": "Stocks", "audio_lang": "en", "duration": 600,
                                                             "published": "2026-10-10T00:00:00Z"}), "utf-8")
            self.assertEqual(orr._useful_novel(td, {"dur": "medium", "novel": [EN]}, 56), 0)
            self.assertEqual(orr._useful_novel(td, {"dur": "medium", "novel": [EN], "lang": orr.ANY_LANG}, 56), 1)

    def test_configs_default_off(self):
        for t in ("economic", "stock"):
            with self.subTest(topic=t):
                cfg = tomllib.loads((REPO / t / "analyzer_config.toml").read_text("utf-8"))
                self.assertIs(cfg["search"]["INCLUDE_FOREIGN"], False)
                self.assertFalse(orr.include_foreign(t, REPO))
        rel = orr.load_keywords("stock", 0)[4] if orr.ROOT == REPO else None
        if rel:                                                                 # 영어 주식 영상도 주제 관련으로 (stock/keywords.toml v1.1)
            self.assertTrue(orr.relevant({"title": "How I pick dividend stocks", "tags": [], "description": ""}, rel))


class TestTranscriptAnyLang(Base):
    def _fake_api(self, tracks):
        class TL(list):
            def find_manually_created_transcript(self, langs):
                return next(t for t in self if not t.is_generated and t.language_code in langs)

            def find_generated_transcript(self, langs):
                return next(t for t in self if t.is_generated and t.language_code in langs)

        class Api:
            def list(self, vid):
                return TL(tracks)
        return types.SimpleNamespace(YouTubeTranscriptApi=Api)

    def _track(self, code, gen):
        return types.SimpleNamespace(language_code=code, is_generated=gen,
                                     fetch=lambda: [types.SimpleNamespace(text=f"hello {code}", start=0.0, duration=1.0)])

    def test_foreign_video_gets_its_own_captions(self):
        mod = self._fake_api([self._track("en", True), self._track("en", False)])
        with mock.patch.dict(sys.modules, {"youtube_transcript_api": mod}):
            self.assertEqual(orr._transcript_fetch("v")[2], "한국어 자막 없음")                 # 한국어 영상은 예전 그대로
            snips, lang, st = orr._transcript_fetch("v", any_lang=True)
        self.assertEqual((st, lang, snips[0]["text"]), ("ok", "en", "hello en"))             # 수동 자막 먼저
        with mock.patch.dict(sys.modules, {"youtube_transcript_api": self._fake_api([])}):
            self.assertEqual(orr._transcript_fetch("v", any_lang=True)[2], "자막 없음")


class TestWebForeign(Base):
    def setUp(self):
        super().setUp()
        self.urlopen.stop()
        self.yt = FakeYT2()
        self.urlopen = mock.patch.object(orr.urllib.request, "urlopen", self.yt)
        self.urlopen.start()
        web.orr = orr
        web.wa = types.SimpleNamespace(run=lambda t: {"windows": [], "cases": 0}, load_cases=lambda out: [])
        for t in ("economic", "stock"):
            (self.root / t).mkdir()
            (self.root / t / "analyzer_config.toml").write_text(CONFIG.format(t=t), "utf-8")
            (self.root / t / "keywords.txt").write_text("주식\n", "utf-8")
        web.STATE.update(topic="economic", topics=["economic", "stock"], port=8765)
        web.release_topic()
        web.JOBS.clear()
        self.ac = mock.patch.object(orr, "fetch_autocomplete", lambda q, c, refresh=False, fetch=None: ([], True))
        self.ac.start()

    def tearDown(self):
        self.ac.stop()
        web.release_topic()
        super().tearDown()

    def post(self, topic, on):
        h, sent = handler("/api/foreign", topic, {"on": on})
        h.do_POST()
        return sent

    def test_toggle_writes_only_that_topic(self):
        self.assertFalse(web.foreign_ok("stock"))                              # 줄이 없으면 꺼짐
        sent = self.post("stock", True)
        self.assertEqual(sent["code"], 200, sent)
        self.assertTrue(sent["body"]["include_foreign"])
        self.assertIn("GITHUB_TOKEN 없음", sent["body"]["message"])            # 시험은 GitHub 에 올리지 않음
        text = (self.root / "stock" / "analyzer_config.toml").read_text("utf-8")
        cfg = tomllib.loads(text)
        self.assertIs(cfg["search"]["INCLUDE_FOREIGN"], True)                  # [search] 밑에
        self.assertEqual(cfg["advanced"]["QUOTA_BUDGET"], 6000)
        self.assertIn("# 주석 그대로", text)
        self.assertIn("# 머리 주석", text)
        self.assertFalse(web.foreign_ok("economic"))                           # 다른 탭 설정은 그대로
        self.assertTrue(web.state_view("stock")["include_foreign"])
        self.assertIn("이미", self.post("stock", True)["body"]["message"])
        self.assertFalse(self.post("stock", False)["body"]["include_foreign"])
        self.assertEqual(text.count("INCLUDE_FOREIGN"), (self.root / "stock" / "analyzer_config.toml").read_text("utf-8").count("INCLUDE_FOREIGN"))
        (self.root / "economic" / "analyzer_config.toml").write_text('[topic]\nTOPIC = "e"\n', "utf-8")     # [search] 없음 → 끝에
        web.set_include_foreign("economic", True)
        self.assertIs(tomllib.loads((self.root / "economic" / "analyzer_config.toml").read_text("utf-8"))["search"]["INCLUDE_FOREIGN"], True)

    def test_explore_off_then_on(self):
        self.yt.search_ids[("주식", "medium")] = [KO, EN]
        r = web.job_explore("stock", 8, True)
        ex = json.loads((self.root / "stock" / "result" / "web" / "explore.json").read_text("utf-8"))
        self.assertEqual([x["id"] for x in ex["rows"]], [KO])                  # 꺼짐 = 외국 영상 뺌 (예전 그대로)
        self.assertEqual(ex.get("excluded", r.get("excluded")), {orr.FOREIGN: 1})
        searches = [q for k, q in self.yt.calls if k == "search"]
        self.assertTrue(searches and all(q.get("relevanceLanguage") == "ko" for q in searches))
        est = web.estimate("stock", 8, True)
        self.assertEqual(est["cached"], est["searches"])
        self.post("stock", True)
        self.assertEqual(web.estimate("stock", 8, True)["cached"], 0)          # 켜면 언어 지정 없는 검색 캐시는 아직 없음
        web.job_explore("stock", 8, True)
        new = [q for k, q in self.yt.calls if k == "search"][len(searches):]
        self.assertTrue(new and all("relevanceLanguage" not in q for q in new))
        ex = json.loads((self.root / "stock" / "result" / "web" / "explore.json").read_text("utf-8"))
        self.assertEqual({x["id"]: x["flag"] for x in ex["rows"]}, {KO: "", EN: orr.FOREIGN})
        n = self.yt.count("search")
        web.job_explore("stock", 8, True)
        self.assertEqual(self.yt.count("search"), n)                           # 켠 검색도 캐시
        self.post("stock", False)
        web.job_explore("stock", 8, True)
        self.assertEqual(self.yt.count("search"), n)                           # 다시 끄면 예전(ko) 캐시 그대로 — 새 검색 없음
        ex = json.loads((self.root / "stock" / "result" / "web" / "explore.json").read_text("utf-8"))
        self.assertEqual([x["id"] for x in ex["rows"]], [KO])

    def test_post_blocked_while_job_runs(self):
        web.JOBS["stock"] = {**web.new_job(), "status": "running", "name": "탐색"}
        sent = self.post("stock", True)
        self.assertNotEqual(sent["code"], 200)
        self.assertFalse(web.foreign_ok("stock"))


class TestAnalysisForeign(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        for t, on in (("off", None), ("on", "true")):
            (self.root / t).mkdir()
            (self.root / t / "analyzer_config.toml").write_text(
                f'[topic]\nTOPIC = "{t}"\n[search]\n' + (f"INCLUDE_FOREIGN = {on}\n" if on else ""), "utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    def test_rules_and_flags(self):
        off, on = sa.load_rules(self.root, "off"), sa.load_rules(self.root, "on")
        self.assertEqual((off["include_foreign"], on["include_foreign"]), (False, True))
        x = {"title": "How I invest in stocks", "audio_lang": "en", "lang": "", "live": False, "was_live": False, "tags": [],
             "description": "", "views": 5000, "likes": 100, "comments_total": 10, "theme": "기타"}
        rel = {"strong": [], "weak": [], "exclude": []}
        self.assertEqual(sa.flags(x, off, rel), orr.FOREIGN)
        self.assertEqual(sa.flags(x, on, rel), "")
        self.assertEqual(sa.flags({**x, "live": True}, on, rel), "라이브 방송")
        self.assertTrue(sh.load_rules(self.root, "on")["include_foreign"])          # 쇼츠 분석도 같은 설정
        self.assertTrue(sa._base({"id": "e", "title": "Stocks", "audio_lang": "en"}, 100, None)["foreign"])


@unittest.skipUnless(__import__("importlib").util.find_spec("requests"), "분석기는 requests 가 있어야 불러옴")
class TestAnalyzer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sys.path.insert(0, str(REPO))
        import youtube_topic_analyzer as y
        cls.y = y

    def test_config_and_search_language(self):
        y = self.y
        cfg = y.collect_config(vars(y))
        r = y.apply_config_file(cfg, REPO / "stock" / "analyzer_config.toml")
        self.assertFalse([u for u in r["unknown"] if "INCLUDE_FOREIGN" in u], r["unknown"])
        self.assertIs(cfg["INCLUDE_FOREIGN"], False)
        self.assertEqual(y.search_language(cfg), "ko")
        self.assertIsNone(y.search_language({**cfg, "INCLUDE_FOREIGN": True}))
        self.assertTrue(y.video_is_foreign("en-US", "주식"))
        self.assertFalse(y.video_is_foreign("", "주식 이야기"))
        self.assertTrue(y.video_is_foreign(None, "Stocks"))
        self.assertFalse(y.video_is_foreign(None, __import__("unicodedata").normalize("NFD", "주식 이야기")))

    def test_queue_items_and_whisper_language(self):
        y = self.y
        with tempfile.TemporaryDirectory() as td:
            tb = Path(td)
            od = tb / "t" / "result" / "outliers"
            for vid, meta in (("aaaaaaaaaa1", {"title": "주식 이야기"}), ("bbbbbbbbbb1", {"title": "Stocks", "video_lang": "en"}),
                              ("cccccccccc1", {"title": "Stocks", "foreign": False})):
                (od / f"W_{vid}").mkdir(parents=True)
                (od / f"W_{vid}" / "metadata.json").write_text(json.dumps({"id": vid, "transcript_status": "자막 없음", "seconds": 300, **meta}), "utf-8")
            items = y.speech_queue_items({"PROJECT_FOLDER": "t", "RESULT_FOLDER": "result"}, tb / "out", base=tb)
        self.assertEqual({i["video_id"]: i["foreign"] for i in items}, {"aaaaaaaaaa1": False, "bbbbbbbbbb1": True, "cccccccccc1": False})
        seen = []

        class Model:
            def __init__(self, *a, **k):
                pass

            def transcribe(self, audio, language=None, **k):
                seen.append(language)
                return iter([types.SimpleNamespace(start=0.0, end=1.0, text=" hi")]), types.SimpleNamespace(language=language or "en")
        fake = types.SimpleNamespace(WhisperModel=Model)
        cfg = {**y.collect_config(vars(y)), "WHISPER_MODEL": "fake-model"}
        with mock.patch.dict(sys.modules, {"faster_whisper": fake}), mock.patch.object(y, "find_ffmpeg", lambda: "ffmpeg"), \
                mock.patch.object(y.subprocess, "run", lambda *a, **k: types.SimpleNamespace(stdout=b"\0\0" * 1600)), \
                mock.patch.dict(y._WHISPER, {}, clear=True):
            _, m_ko = y.transcript_via_whisper(Path("a.m4a"), cfg, 1)
            _, m_en = y.transcript_via_whisper(Path("a.m4a"), cfg, 1, foreign=True)
        self.assertEqual(seen, ["ko", None])                                    # 외국 영상은 Whisper 가 언어를 알아냄
        self.assertEqual((m_ko["language"], m_en["language"]), ("ko", "en"))


class TestKeysPerTopic(Base):
    def setUp(self):
        super().setUp()
        web.orr = orr                                                         # main() 이 넣는 도구 (시험은 직접)
        for t in ("economic", "stock"):
            (self.root / t).mkdir()
            (self.root / t / "analyzer_config.toml").write_text(CONFIG.format(t=t), "utf-8")
        web.STATE.update(topic="economic", topics=["economic", "stock"], port=8765)

    def test_different_keys_separate_quota(self):
        (self.root / "economic" / ".env").write_text("YOUTUBE_API_KEY=KEY-ECONOMIC-0001\n", "utf-8")
        (self.root / "stock" / ".env").write_text("YOUTUBE_API_KEY=KEY-STOCK-0002\n", "utf-8")
        self.assertEqual(orr.load_api_key("stock"), ("KEY-STOCK-0002", "stock/.env"))
        self.assertEqual(pc.find_secret("YOUTUBE_API_KEY", "economic"), ("KEY-ECONOMIC-0001", "economic/.env"))
        qe, qs = web.quota_view("economic"), web.quota_view("stock")
        self.assertNotEqual(qe["key"], qs["key"])
        self.assertEqual((qe["same_key"], qs["same_key"]), ([], []))
        self.assertNotIn("KEY-STOCK", json.dumps(qs))                           # 키 값은 내보내지 않음 (지문만)
        pc.KeyLedger("KEY-STOCK-0002").add(3000, "web_explore", "stock")
        self.assertEqual(web.quota_view("stock")["used"], 3000)
        self.assertEqual(web.quota_view("economic")["used"], 0)                 # 다른 키는 할당량 따로
        (self.root / "economic" / ".env").write_text("YOUTUBE_API_KEY=KEY-STOCK-0002\n", "utf-8")
        self.assertEqual(web.quota_view("economic")["same_key"], ["stock"])     # 같은 키면 함께 셈
        self.assertEqual(web.quota_view("economic")["used"], 3000)

    def test_topic_env_template_without_root_env(self):
        self.assertFalse((self.root / ".env").exists())
        self.assertTrue(pc.ensure_topic_env("stock"))
        text = (self.root / "stock" / ".env").read_text("utf-8")
        self.assertIn("주제마다 다른 키", text)
        self.assertIn("\nYOUTUBE_API_KEY=\n", text)
        self.assertEqual(pc.find_secret("YOUTUBE_API_KEY", "stock")[1], "env:YOUTUBE_API_KEY")   # 비우면 다음 차례 키
        self.assertFalse(pc.ensure_topic_env("stock"))                          # 한 번만
        os.environ.pop("YOUTUBE_API_KEY", None)
        h, sent = handler("/api/env", "stock", {"YOUTUBE_API_KEY": "KEY-STOCK-0003"})
        h.do_POST()
        self.assertEqual(sent["code"], 200, sent)
        self.assertEqual(pc.find_secret("YOUTUBE_API_KEY", "stock"), ("KEY-STOCK-0003", "stock/.env"))
        self.assertEqual(pc.find_secret("YOUTUBE_API_KEY", "economic")[0], "")  # 다른 주제에는 안 들어감


if __name__ == "__main__":
    unittest.main()
