# VERSION: v1.0 — 2026-10-17 — youtube_upload.py v1.12 언어별 자막: 올릴 파일 고르기 · 할당량이 끝나면 멈추고 남은 언어 (네트워크·키 없이 — 가짜 업로드 함수)
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import youtube_upload as yu  # noqa: E402


class CaptionFiles(unittest.TestCase):
    def setUp(self):
        self.d = Path(tempfile.mkdtemp())
        (self.d / "subs").mkdir()
        (self.d / "v.srt").write_text("1\n00:00:00,000 --> 00:00:01,000\n가\n", "utf-8")
        for lang in ("en", "ja"):
            (self.d / "subs" / f"v.{lang}.srt").write_text("1\n00:00:00,000 --> 00:00:01,000\nx\n", "utf-8")

    def test_ko_only(self):
        self.assertEqual([l for l, _ in yu.caption_files(self.d, "v", "ko")], ["ko"])

    def test_all_existing(self):
        self.assertEqual([l for l, _ in yu.caption_files(self.d, "v", "all")], ["ko", "en", "ja"])

    def test_quota_stops_and_keeps_rest(self):
        calls = []

        def fake(token, vid, f, lang="ko"):
            if len(calls) == 2:
                raise RuntimeError('HTTP 403 …: {"error": {"errors": [{"reason": "quotaExceeded"}]}}')
            calls.append(lang)
            return f"id-{lang}"
        orig, yu.upload_captions = yu.upload_captions, fake
        try:
            done, rest = yu.upload_caption_set("t", "VID", yu.caption_files(self.d, "v", "all"))
        finally:
            yu.upload_captions = orig
        self.assertEqual(done, {"ko": "id-ko", "en": "id-en"})
        self.assertEqual(rest, ["ja"])

    def test_resume_skips_done(self):
        seen = []
        orig, yu.upload_captions = yu.upload_captions, lambda t, v, f, lang="ko": seen.append(lang) or f"id-{lang}"
        try:
            done, rest = yu.upload_caption_set("t", "VID", yu.caption_files(self.d, "v", "all"), {"ko": "k", "en": "e"})
        finally:
            yu.upload_captions = orig
        self.assertEqual(seen, ["ja"])
        self.assertEqual(rest, [])


if __name__ == "__main__":
    unittest.main()
