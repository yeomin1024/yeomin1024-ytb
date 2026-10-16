# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-16 — tools/tts_narration.py v1.9 시험: 쇼츠 대본(<영상ID>/shorts/<영상ID>-shorts.txt)을 찾고
#          결과 경로가 쇼츠 폴더가 되는지 (사용자 지시 2026-10-16 "일단 이 쇼츠만 영상 만들어봐" — 쇼츠도 오디오 먼저).
#          임시 폴더만 씀 — 모델·네트워크 없음.
"""cd tools/tests && python3 -m unittest test_tts_shorts -v"""
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import tts_narration as tn  # noqa: E402


class TtsShortsPaths(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.patch = mock.patch.object(tn, "ROOT", self.root)
        self.patch.start()
        long_dir = self.root / "economic" / "source" / "v1"
        (long_dir / "shorts").mkdir(parents=True)
        (long_dir / "v1.txt").write_text("-장\n문장 하나.\n", "utf-8")
        (long_dir / "shorts" / "v1-shorts.txt").write_text("-장\n쇼츠 문장.\n", "utf-8")
        (long_dir / "shorts" / "notes.txt").write_text("쇼츠가 아닌 글", "utf-8")       # 이름이 맞지 않으면 대본 아님
        (long_dir / "other.txt").write_text("롱폼이 아닌 글", "utf-8")

    def tearDown(self):
        self.patch.stop()
        self.tmp.cleanup()

    def test_src_dir(self):
        self.assertEqual(tn.src_dir("economic", "v1"), self.root / "economic" / "source" / "v1")
        self.assertEqual(tn.src_dir("economic", "v1-shorts"), self.root / "economic" / "source" / "v1" / "shorts")

    def test_script_entries_finds_long_and_shorts_only(self):
        got = [(t, v, p.relative_to(self.root).as_posix()) for t, v, p in tn.script_entries()]
        self.assertEqual(got, [("economic", "v1", "economic/source/v1/v1.txt"),
                               ("economic", "v1-shorts", "economic/source/v1/shorts/v1-shorts.txt")])

    def test_episode_paths_upload_mirrors_repo(self):
        out = Path(self.tmp.name) / "out"
        p = tn.episode_paths(out, "economic", "v1-shorts")
        self.assertEqual(p["upload"], out / "upload" / "economic" / "source" / "v1" / "shorts")
        self.assertEqual(p["narration"].name, "narration.mp3")
        self.assertEqual(tn.episode_paths(out, "economic", "v1")["upload"], out / "upload" / "economic" / "source" / "v1")

    def test_repo_audio_in_shorts_folder(self):
        self.assertIsNone(tn.repo_audio("economic", "v1-shorts"))
        (self.root / "economic" / "source" / "v1" / "shorts" / "narration.mp3").write_bytes(b"x")
        self.assertEqual(tn.repo_audio("economic", "v1-shorts").name, "narration.mp3")
        self.assertIsNone(tn.repo_audio("economic", "v1"))                            # 롱폼 오디오와 섞이지 않음


if __name__ == "__main__":
    unittest.main()
