#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-15 — youtube_upload v1.6 시험: 언어별 제목·설명(localizations)·기본 언어·자막 올리기 여부
#          (사용자 지시 2026-10-15 "주식 주제는 전세계 사람들 대상 … 영상에 자막 달지말고 … 그 언어로 제목 각각 만들어").
#          진짜 YouTube 요청 없음 — request 를 가짜로 바꿔 보낸 주소·본문만 본다.
"""cd tools/tests && python3 -m unittest test_upload_localizations -v"""
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import youtube_upload as yu  # noqa: E402

SHEET = """# 업로드 시트

## 1. 제목
```
떨어지면 사겠다? 23년 치 백테스트 163번 중 117번 졌다
```

## 2. 설명란
```
설명
```

## 4. 태그
```
S&P500, 백테스트
```

## 5. 언어별 제목·설명 (localizations)
```
{"en": {"title": "Waiting for a dip? 117 of 163 backtests lost", "description": "English description"},
 "ja": {"title": "下落を待つと？", "description": ""}}
```

## 6. 업로드 설정
| 항목 | 값 |
|---|---|
| 기본 언어 | ko |
| 자막 올리기 | **아니요** (전 세계 대상) |
| 변경되거나 합성된 콘텐츠 | 예 |
"""


class TestLocalizations(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.patch = mock.patch.object(yu, "ROOT", self.root)
        self.patch.start()
        self.src = self.root / "stock" / "source" / "v1"
        self.src.mkdir(parents=True)

    def tearDown(self):
        self.patch.stop()
        self.tmp.cleanup()

    def test_read_sheet(self):
        (self.src / "upload.md").write_text(SHEET, "utf-8")
        m = yu.read_sheet("stock", "v1")
        self.assertEqual(m["default_language"], "ko")
        self.assertFalse(m["captions"])
        self.assertEqual(sorted(m["localizations"]), ["en", "ja"])
        self.assertEqual(m["localizations"]["en"]["title"], "Waiting for a dip? 117 of 163 backtests lost")
        self.assertEqual(yu.validate(m), [])

    def test_old_sheet_defaults(self):
        (self.src / "upload.md").write_text(SHEET.split("## 5.")[0], "utf-8")
        m = yu.read_sheet("stock", "v1")
        self.assertEqual((m["default_language"], m["captions"], m["localizations"]), ("ko", True, {}))   # 예전 시트 그대로

    def test_broken_json_stops(self):
        (self.src / "upload.md").write_text(SHEET.replace('"ja": {', '"ja" {'), "utf-8")
        with self.assertRaises(SystemExit):
            yu.read_sheet("stock", "v1")

    def test_validate_long_and_default_lang(self):
        m = {"title": "t", "description": "", "tags": [], "default_language": "ko",
             "localizations": {"en": {"title": "x" * 101, "description": ""}, "ko": {"title": "중복", "description": ""}}}
        probs = yu.validate(m)
        self.assertTrue(any("en 제목 101자" in p for p in probs))
        self.assertTrue(any("기본 언어(ko)" in p for p in probs))

    def test_upload_body_has_localizations(self):
        seen = {}

        def fake_request(method, url, token, data=None, headers=None, retries=4):
            if "uploadType=resumable" in url:
                seen["url"], seen["body"] = url, json.loads(data)
                return 200, {"Location": "https://upload.example/session"}, {}
            return 200, {}, {"id": "VID123"}
        video = self.root / "v.mp4"
        video.write_bytes(b"0" * 10)
        meta = {"title": "t", "description": "d", "tags": [], "synthetic": True, "default_language": "ko",
                "localizations": {"en": {"title": "T", "description": "D"}}}
        with mock.patch.object(yu, "request", fake_request):
            vid = yu.upload_video("tok", video, meta, "private")
        self.assertEqual(vid, "VID123")
        self.assertIn("part=snippet,status,localizations", seen["url"])
        self.assertEqual(seen["body"]["localizations"], {"en": {"title": "T", "description": "D"}})
        self.assertEqual(seen["body"]["snippet"]["defaultLanguage"], "ko")


if __name__ == "__main__":
    unittest.main()
