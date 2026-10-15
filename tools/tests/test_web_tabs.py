#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-15 — 웹 화면 v2.0 '한 화면 · 주제 탭' 시험 (사용자 지시: "헷갈리니까 하나의 사이트에서 그냥 탭 만들어서 다른 주제
#          볼 수 있게 하자 서로 캐시는 공유하지 않도록 하고" · "설정도 다 따로써야해"): 주제마다 작업 따로·동시에 · 요청의 X-Topic ·
#          키는 그 주제 .env 에만 · 주제 키 파일 복사 · 예전 공동 캐시 옮기기 · 음성인식은 PC 에서 하나(다른 주제는 줄) · 분석기 캐시 주제마다.
#          진짜 YouTube·GitHub 에 요청하지 않는다 (test_quota_saving 의 Base — 임시 폴더를 ROOT 로, GITHUB_TOKEN 류는 지움).
"""python3 -m unittest tools.tests.test_web_tabs -v"""
import io
import json
import sys
import threading
import time
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from test_quota_saving import Base, orr, pc, web  # noqa: E402

ROOT_REPO = Path(__file__).resolve().parents[2]


class _Headers(dict):
    def get(self, k, d=None):
        return super().get(k, d)


def handler(path, topic=None, body=None):
    h = web.Handler.__new__(web.Handler)
    sent = {}
    h._send = lambda code, b, ctype=None: sent.update(code=code, body=b)
    h._host_ok = lambda: True
    h._authorized = lambda: True
    raw = json.dumps(body or {}).encode("utf-8")
    h.headers = _Headers({"X-Topic": topic or "", "Content-Length": str(len(raw))})
    h.rfile = io.BytesIO(raw)
    h.path = path
    return h, sent


class TestTabs(Base):
    def setUp(self):
        super().setUp()
        web.orr = orr                                                         # main() 이 넣는 도구 (시험은 직접)
        for t in ("economic", "stock"):
            d = self.root / t
            d.mkdir()
            (d / "analyzer_config.toml").write_text(f'[topic]\nTOPIC = "{t}"\nPROJECT_FOLDER = "{t}"\n', "utf-8")
            (d / "keywords.txt").write_text("주식\n", "utf-8")
        web.STATE.update(topic="economic", topics=["economic", "stock"], port=8765)
        web.release_topic()
        web.JOBS.clear()

    def tearDown(self):
        web.release_topic()
        super().tearDown()

    def test_jobs_per_topic_run_together(self):
        go = threading.Event()

        def work(t, tag):
            web.step(f"{tag} 시작", 0, 2)
            web.log("TEST", topic=t, note=f"{tag} 로그")
            go.wait(5)
            web.step(f"{tag} 끝", 2, 2)
            return {"tag": tag}
        ok1, _ = web.start_job("주식 탐색", work, "stock", "S")
        ok2, _ = web.start_job("재테크 승인", work, "economic", "E")
        self.assertTrue(ok1 and ok2)                                          # 다른 주제 작업은 동시에
        self.assertFalse(web.start_job("또", work, "stock", "X")[0])          # 같은 주제는 하나씩
        time.sleep(0.2)
        self.assertEqual((web.job_of("stock")["status"], web.job_of("economic")["status"]), ("running", "running"))
        self.assertEqual(web.job_of("stock")["step"], "S 시작")
        self.assertEqual(web.job_of("economic")["step"], "E 시작")
        go.set()
        for t in ("stock", "economic"):
            for _ in range(50):
                if web.job_of(t)["status"] != "running":
                    break
                time.sleep(0.05)
        self.assertEqual(web.job_of("stock")["result"], {"tag": "S"})
        self.assertEqual(web.tabs_view(), {"economic": "done", "stock": "done"})

    def test_request_topic_header(self):
        h, _ = handler("/api/state", "stock")
        self.assertEqual(h._topic(), "stock")
        for bad in ("", "../etc", "nope", "ECONOMIC"):
            h, _ = handler("/api/state", bad)
            self.assertEqual(h._topic(), "economic")                          # 없거나 틀리면 처음 탭
        h, sent = handler("/api/job", "stock")
        h.do_GET()
        self.assertEqual((sent["code"], sent["body"]["topic"]), (200, "stock"))

    def test_keys_saved_per_topic(self):
        (self.root / ".env").write_text("YOUTUBE_API_KEY=ROOTKEY0001\nGITHUB_TOKEN=\n", "utf-8")
        self.assertTrue(pc.ensure_topic_env("economic"))                      # 처음엔 맨 위 .env 를 복사
        self.assertFalse(pc.ensure_topic_env("economic"))                     # 한 번만
        self.assertIn("ROOTKEY0001", (self.root / "economic" / ".env").read_text("utf-8"))
        h, sent = handler("/api/env", "stock", {"YOUTUBE_API_KEY": "STOCKKEY0002"})
        h.do_POST()
        self.assertEqual(sent["code"], 200, sent)
        self.assertIn("YOUTUBE_API_KEY=STOCKKEY0002", (self.root / "stock" / ".env").read_text("utf-8"))
        self.assertNotIn("STOCKKEY0002", (self.root / ".env").read_text("utf-8"))           # 맨 위 .env 는 그대로
        self.assertNotIn("STOCKKEY0002", (self.root / "economic" / ".env").read_text("utf-8"))   # 다른 주제 키도 그대로
        self.assertEqual(pc.find_secret("YOUTUBE_API_KEY", "stock"), ("STOCKKEY0002", "stock/.env"))
        self.assertEqual(pc.find_secret("YOUTUBE_API_KEY", "economic"), ("ROOTKEY0001", "economic/.env"))
        self.assertIn("stock", web.LOCKS)                                     # POST 하면 그 탭을 잡음

    def test_shared_cache_retired_and_topic_cache_reset(self):
        old = self.root / ".yt_work" / "cache" / "yt_api" / "ab"
        old.mkdir(parents=True)
        (old / "x.json").write_text("{}", "utf-8")
        dst = pc.retire_shared_cache()
        self.assertFalse((self.root / ".yt_work" / "cache").exists())
        self.assertTrue((dst / "yt_api" / "ab" / "x.json").is_file())
        self.assertIsNone(pc.retire_shared_cache())                           # 한 번만
        (self.root / ".yt_work" / "cache_stock").mkdir()
        (self.root / ".yt_work" / "cache_economic").mkdir()
        r = pc.reset_topic_cache("stock")
        self.assertIn(".yt_work/cache_stock", r["moved"])
        self.assertTrue((self.root / ".yt_work" / "cache_economic").is_dir())   # 다른 주제 캐시는 그대로

    def test_whisper_one_at_a_time_queue(self):
        web.WHISPER.update(status="running", topic="economic", queued=[], rerun=False)
        try:
            ok, msg = web.start_whisper("stock", "시험")
            self.assertFalse(ok)
            self.assertIn("한 번에 하나", msg)
            self.assertEqual(web.WHISPER["queued"], ["stock"])
            web.start_whisper("stock", "시험")
            self.assertEqual(web.WHISPER["queued"], ["stock"])                # 두 번 줄 서지 않음
            ok, _ = web.start_whisper("economic", "시험")                     # 같은 주제는 '끝나면 다시'
            self.assertFalse(ok)
            self.assertTrue(web.WHISPER["rerun"])
            self.assertEqual(web.whisper_view("stock")["queued"], ["stock"])
        finally:
            web.WHISPER.update(status="idle", topic=None, queued=[], rerun=False)

    def test_analyzer_cache_per_topic(self):
        sys.path.insert(0, str(ROOT_REPO))
        import youtube_topic_analyzer as y
        a = y.topic_cache_dir(Path("/w"), {"PROJECT_FOLDER": "economic"})
        b = y.topic_cache_dir(Path("/w"), {"PROJECT_FOLDER": "stock"})
        self.assertEqual((a.name, b.name), ("cache_economic", "cache_stock"))
        self.assertNotEqual(a, Path("/w") / "cache")                          # 예전 공동 캐시는 안 씀


if __name__ == "__main__":
    unittest.main()
