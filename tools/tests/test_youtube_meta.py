# VERSION: v1.0 — 2026-10-18 — youtube_upload.py v1.13 --update-meta · 오디오 언어 (네트워크·키 없이 — 가짜 함수)
# (사용자 지시 2026-10-18 "설명은 부호, 정말 간단한 영어로 간략하게 표현하도록 해봐 그리고 태그 같은 것도 영어로 하고 한국어로 쓰여진 곳은 정말 간단한 영어로 수정할 수 있어? 모든 영상")
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import youtube_upload as yu  # noqa: E402


class SnippetBody(unittest.TestCase):
    def test_audio_language_separate(self):
        b = yu.snippet_body({"title": "T", "description": "D", "tags": ["a"], "default_language": "en", "audio_language": "ko"})
        self.assertEqual((b["defaultLanguage"], b["defaultAudioLanguage"]), ("en", "ko"))

    def test_audio_language_defaults_to_default(self):
        b = yu.snippet_body({"title": "T", "description": "D", "tags": [], "default_language": "ko"})
        self.assertEqual(b["defaultAudioLanguage"], "ko")

    def test_setting_row(self):
        md = "| 기본 언어 | en |\n| 오디오 언어 | ko (내레이션) |\n"
        self.assertEqual(yu.read_setting(md, "오디오 언어", "x"), "ko")


class UpdateMeta(unittest.TestCase):
    def setUp(self):
        self.d = Path(tempfile.mkdtemp())
        (self.d / "youtube.json").write_text(json.dumps({"videoId": "VID", "publishAt": "2026-10-19T08:00:00Z"}), "utf-8")
        self.meta = {"title": "When to buy?", "description": "Hi\n\n■ Chapters\n0:00 A\n", "tags": ["SPY"], "chapter_spec": None,
                     "synthetic": True, "default_language": "en", "audio_language": "ko", "captions": True, "caption_mode": "all",
                     "localizations": {"ko": {"title": "언제", "description": "Hi"}}}
        self.sent = []
        self.orig = (yu.src_dir, yu.read_sheet, yu.access_token, yu.check_channel, yu.request)
        yu.src_dir = lambda t, v: self.d
        yu.read_sheet = lambda t, v: dict(self.meta)
        yu.access_token = lambda: "tok"
        yu.check_channel = lambda t, tok: ("UC", "STOCK LAB")

        def fake_request(method, url, token, data=None, headers=None, retries=4):
            body = json.loads(data)
            self.sent.append((method, url, body))
            return 200, {}, {"snippet": body["snippet"], "localizations": body["localizations"]}
        yu.request = fake_request

    def tearDown(self):
        yu.src_dir, yu.read_sheet, yu.access_token, yu.check_channel, yu.request = self.orig

    def test_sends_snippet_and_localizations_only(self):
        st = yu.update_meta("stock", "v")
        method, url, body = self.sent[0]
        self.assertEqual(method, "PUT")
        self.assertIn("part=snippet,localizations", url)
        self.assertNotIn("status", body)                       # 공개 상태·예약 시각은 건드리지 않음
        self.assertEqual(body["snippet"]["defaultAudioLanguage"], "ko")
        self.assertEqual(st["publishAt"], "2026-10-19T08:00:00Z")
        self.assertEqual(st["defaultLanguage"], "en")

    def test_dry_run_sends_nothing(self):
        yu.update_meta("stock", "v", dry_run=True)
        self.assertEqual(self.sent, [])

    def test_default_language_not_in_localizations(self):
        self.meta["localizations"]["en"] = {"title": "x", "description": "y"}
        with self.assertRaises(SystemExit):
            yu.update_meta("stock", "v")
        self.assertEqual(self.sent, [])


if __name__ == "__main__":
    unittest.main()
