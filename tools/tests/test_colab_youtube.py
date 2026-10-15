# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-15 — tools/colab_youtube.py v1.0 시험 (임시 폴더·가짜 업로드 — 네트워크·GitHub·유튜브 없음)
r"""
  python3 -m unittest tools.tests.test_colab_youtube -v     (저장소 최상위에서)

1) 준비된 영상 고르기: upload.md + 영상 파일(source/ 압축본) 있고 youtube.json 없는 것만, out/ 원본이 있으면 그것 먼저
2) 예약 시각: 실행 시각 + delay, 영상마다 + gap
3) 할당량 초과(quotaExceeded) → 남은 영상은 올리지 않고 not_run, 종료 코드 1
"""
import datetime as dt
import io
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(TOOLS))
import colab_youtube as cy  # noqa: E402
import youtube_upload as yu  # noqa: E402


class ColabYoutubeTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.old = (cy.ROOT, yu.ROOT, yu.run, yu.check_auth)
        cy.ROOT = yu.ROOT = self.root
        for vid, files in {"a-2026-10": ["upload.md", "final_1080p.mp4"],          # 준비됨 (압축본)
                           "b-2026-10": ["upload.md", "final_1080p.mp4", "youtube.json"],  # 이미 올림
                           "c-2026-10": ["upload.md"],                              # 영상 없음
                           "d-2026-10": ["upload.md"]}.items():                     # out/ 원본만
            d = self.root / "economic" / "source" / vid
            d.mkdir(parents=True)
            for f in files:
                (d / f).write_text("x", "utf-8")
        o = self.root / "economic" / "out" / "d-2026-10"
        o.mkdir(parents=True)
        (o / "final_1080p.mp4").write_text("x", "utf-8")

    def tearDown(self):
        cy.ROOT, yu.ROOT, yu.run, yu.check_auth = self.old
        self.tmp.cleanup()

    def test_find_ready(self):
        ready, skipped = cy.find_ready()
        self.assertEqual([v for _, v, _ in ready], ["a-2026-10", "d-2026-10"])
        self.assertEqual(ready[0][2], self.root / "economic/source/a-2026-10/final_1080p.mp4")
        self.assertEqual(ready[1][2], self.root / "economic/out/d-2026-10/final_1080p.mp4")   # 원본 먼저
        self.assertEqual(dict(skipped), {"b-2026-10": "이미 올림 (youtube.json)", "c-2026-10": "영상 파일 없음 (렌더 → tools/compress_video.py)"})

    def test_parse_span(self):
        self.assertEqual(cy.parse_span("1h"), dt.timedelta(hours=1))
        self.assertEqual(cy.parse_span("90m"), dt.timedelta(minutes=90))
        with self.assertRaises(SystemExit):
            cy.parse_span("1 day")

    def test_schedule_and_quota_stop(self):
        calls = []

        def fake_run(topic, vid, dry_run=False, video=None, publish_at=None, **kw):
            calls.append((vid, publish_at))
            raise RuntimeError('HTTP 403 https://www.googleapis.com/upload/youtube/v3/videos: {"reason": "quotaExceeded"}')

        yu.run, yu.check_auth = fake_run, lambda: None
        env = {k: "x" for k in ("YOUTUBE_CLIENT_ID", "YOUTUBE_CLIENT_SECRET", "YOUTUBE_REFRESH_TOKEN")}
        import os
        old_env = {k: os.environ.get(k) for k in env}
        os.environ.update(env)
        try:
            out = io.StringIO()
            with redirect_stdout(out):
                code = cy.main(["--no-push", "--delay", "2h", "--gap", "24h"])
        finally:
            for k, v in old_env.items():
                if v is None:
                    os.environ.pop(k, None)
                else:
                    os.environ[k] = v
        self.assertEqual(code, 1)
        self.assertEqual(len(calls), 1)                       # 첫 영상에서 할당량 → 둘째는 부르지 않음
        when = dt.datetime.strptime(calls[0][1], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=dt.timezone.utc)
        self.assertAlmostEqual((when - dt.datetime.now(dt.timezone.utc)).total_seconds(), 7200, delta=120)
        text = out.getvalue()
        self.assertIn("| a-2026-10 | failed |", text)
        self.assertIn("| d-2026-10 | not_run |", text)
        self.assertIn("[STOP]", text)

    def test_dry_run_needs_no_keys(self):
        seen = []
        yu.run = lambda topic, vid, dry_run=False, video=None, publish_at=None, **kw: seen.append((vid, dry_run, publish_at))
        yu.check_auth = lambda: self.fail("dry-run 은 인증하지 않음")
        with redirect_stdout(io.StringIO()):
            code = cy.main(["--dry-run"])
        self.assertEqual(code, 0)
        self.assertEqual(seen, [("a-2026-10", True, None), ("d-2026-10", True, None)])


if __name__ == "__main__":
    unittest.main()
