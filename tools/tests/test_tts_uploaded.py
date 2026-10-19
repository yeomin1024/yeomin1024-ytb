# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-10-19 — v1.12 NO_TTS.md (시험용 영상 빼기 — 사용자 지시 "테스트용은 오디오 만들지마") 시험 더함
# (v1.0 — 2026-10-19 — tools/tts_narration.py v1.11 시험: 업로드한 영상(youtube.json)은 all·build 어느 길로도 오디오를 만들지 않는다
#          (사용자 지시 2026-10-19 "업로드 완료한건 오디오 생성하지 말도록 하고"). 임시 폴더만 씀 — 모델·네트워크·토큰 없음.
"""cd tools/tests && python3 -m unittest test_tts_uploaded -v"""
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import tts_narration as tn  # noqa: E402


class TtsUploadedSkip(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.patch = mock.patch.object(tn, "ROOT", self.root)
        self.patch.start()
        test_dir = self.root / "economic" / "source" / "trial" / "shorts"
        test_dir.mkdir(parents=True)
        (test_dir / "trial-shorts.txt").write_text("-장\n시험 문장.\n", "utf-8")
        (test_dir / "NO_TTS.md").write_text("# 시험용 — 오디오 만들지 않음\n", "utf-8")
        for vid, uploaded in (("old", True), ("new", False)):
            d = self.root / "economic" / "source" / vid
            (d / "shorts").mkdir(parents=True)
            (d / f"{vid}.txt").write_text("-장\n문장 하나.\n", "utf-8")
            (d / "shorts" / f"{vid}-shorts.txt").write_text("-장\n쇼츠 문장.\n", "utf-8")
            if uploaded:
                (d / "youtube.json").write_text("{}", "utf-8")
                (d / "shorts" / "youtube.json").write_text("{}", "utf-8")

    def tearDown(self):
        self.patch.stop()
        self.tmp.cleanup()

    def args(self, **kw):
        base = dict(topics="economic", ids=None, include_hold=False, force=False, keep_stale=False)
        base.update(kw)
        return types.SimpleNamespace(**base)

    def plan(self, **kw):
        with mock.patch.object(tn, "voice_mismatch", return_value=[]):
            return {p["video"]: p for p in tn.discover(self.args(**kw), self.root / "out")}

    def test_uploaded_record(self):
        self.assertTrue(tn.uploaded_record("economic", "old"))
        self.assertTrue(tn.uploaded_record("economic", "old-shorts"))
        self.assertIsNone(tn.uploaded_record("economic", "new"))
        self.assertIsNone(tn.uploaded_record("economic", "new-shorts"))

    def test_all_skips_uploaded_even_with_force(self):
        for force in (False, True):
            p = self.plan(force=force)
            self.assertEqual(p["old"]["action"], "skip")
            self.assertEqual(p["old-shorts"]["action"], "skip")
            self.assertEqual(p["old"]["status"], "uploaded")
            self.assertEqual(p["new"]["action"], "make")
            self.assertEqual(p["new-shorts"]["action"], "make")
            self.assertEqual(p["trial-shorts"]["action"], "skip")
            self.assertEqual(p["trial-shorts"]["status"], "no_tts")

    def test_build_refuses_uploaded_before_model(self):
        a = types.SimpleNamespace(topic="economic", id="old-shorts", out_dir=str(self.root / "out"))
        with mock.patch.object(tn, "make_engine") as eng, self.assertRaises(SystemExit):
            tn.cmd_build(a)
        eng.assert_not_called()

    def test_no_tts_marker(self):
        self.assertIn("시험용", tn.no_tts_reason("economic", "trial-shorts"))
        self.assertIsNone(tn.no_tts_reason("economic", "new"))
        a = types.SimpleNamespace(topic="economic", id="trial-shorts", out_dir=str(self.root / "out"))
        with mock.patch.object(tn, "make_engine") as eng, self.assertRaises(SystemExit):
            tn.cmd_build(a)
        eng.assert_not_called()

    def test_build_episode_backstop(self):
        with self.assertRaises(SystemExit):
            tn.build_episode(None, "economic", "old", types.SimpleNamespace(), self.root / "out")


if __name__ == "__main__":
    unittest.main()
