#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-16 — youtube_upload v1.7 시험: 올리기 전 채널 확인 (<주제>/youtube_channel.json vs 키의 채널)
#          (사용자 지시 2026-10-16 "… 부자백서 채널에 업로드 할 환경이야 한번 업로드 잘되는지 데모 영상 만들어서 업로드 테스트해봐" —
#          클라우드 환경마다 키의 채널이 달라 재테크 영상이 STOCK LAB 에 올라갈 수 있었음).
#          진짜 YouTube 요청 없음 — request·access_token 을 가짜로 바꾼다.
"""cd tools/tests && python3 -m unittest test_upload_channel -v"""
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import youtube_upload as yu  # noqa: E402

BUJA = "UCJ1gjiL7VuAhMQSfAhxAefg"
STOCK = "UC7Rw5HWgKz5njCCciX8IVJQ"
SHEET = "# 시트\n\n## 1. 제목\n```\n시험 제목\n```\n\n## 2. 설명란\n```\n설명\n```\n\n## 4. 태그\n```\n시험\n```\n"


def fake_channels(channel_id, title, calls):
    def fake_request(method, url, token, data=None, headers=None, retries=4):
        calls.append(url.split("?")[0])
        if "/channels" in url:
            return 200, {}, {"items": [{"id": channel_id, "snippet": {"title": title}}]}
        if "uploadType=resumable" in url:
            return 200, {"Location": "https://upload.example/session"}, {}
        return 200, {}, {"id": "VID123"}
    return fake_request


class TestChannelCheck(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.patches = [mock.patch.object(yu, "ROOT", self.root), mock.patch.object(yu, "access_token", lambda: "tok"),
                        mock.patch.dict(os.environ, {"YOUTUBE_CLIENT_ID": "x", "YOUTUBE_CLIENT_SECRET": "x",
                                                     "YOUTUBE_REFRESH_TOKEN": "x"})]
        for p in self.patches:
            p.start()
        self.src = self.root / "economic" / "source" / "v1"
        self.src.mkdir(parents=True)
        (self.src / "upload.md").write_text(SHEET, "utf-8")
        (self.root / "economic" / "out" / "v1").mkdir(parents=True)
        (self.root / "economic" / "out" / "v1" / "final_1080p.mp4").write_bytes(b"0" * 10)

    def tearDown(self):
        for p in reversed(self.patches):
            p.stop()
        self.tmp.cleanup()

    def write_channel(self, cid, name):
        (self.root / "economic" / "youtube_channel.json").write_text(json.dumps({"channel_id": cid, "name": name}), "utf-8")

    def test_match_uploads_and_records_channel(self):
        self.write_channel(BUJA, "부자백서")
        calls = []
        with mock.patch.object(yu, "request", fake_channels(BUJA, "부자백서", calls)):
            res = yu.run("economic", "v1")
        self.assertEqual(res["videoId"], "VID123")
        self.assertEqual((res["channel"], res["channelId"]), ("부자백서", BUJA))
        self.assertLess(calls.index(f"{yu.API}/channels"), calls.index(f"{yu.UPLOAD_API}/videos"))   # 확인이 올리기보다 먼저

    def test_mismatch_stops_before_upload(self):
        self.write_channel(BUJA, "부자백서")
        calls = []
        with mock.patch.object(yu, "request", fake_channels(STOCK, "편안한 음악 Relaxing Music", calls)):
            with self.assertRaises(SystemExit) as cm:
                yu.run("economic", "v1")
        self.assertIn("다른 채널", str(cm.exception))
        self.assertNotIn(f"{yu.UPLOAD_API}/videos", calls)                 # 영상은 보내지 않음
        self.assertFalse((self.src / "youtube.json").exists())

    def test_no_file_is_unchecked_but_uploads(self):
        calls = []
        with mock.patch.object(yu, "request", fake_channels(STOCK, "아무 채널", calls)):
            res = yu.run("economic", "v1")
        self.assertEqual(res["channelId"], STOCK)                          # 예전처럼 올리되 어느 채널인지 기록

    def test_dry_run_reports_mismatch(self):
        self.write_channel(BUJA, "부자백서")
        calls = []
        with mock.patch.object(yu, "request", fake_channels(STOCK, "다른 채널", calls)):
            self.assertIsNone(yu.run("economic", "v1", dry_run=True))     # 멈추지 않고 문제로 셈
        self.assertEqual(calls, [f"{yu.API}/channels"])                     # 읽기 1번만

    def test_broken_file_stops(self):
        (self.root / "economic" / "youtube_channel.json").write_text('{"channel_id": "abc"}', "utf-8")
        with self.assertRaises(SystemExit):
            yu.expected_channel("economic")


if __name__ == "__main__":
    unittest.main()
