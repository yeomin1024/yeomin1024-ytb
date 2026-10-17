# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-17 — tools/tts_narration.py v1.10 시험: 파트 라벨 글자만 바뀐 대본은 '바뀐 문장만 다시'가 되고,
#          파트 경계나 읽는 목소리(역할)가 바뀌면 예전처럼 '전부 다시'가 되는지 (patch_candidate — 모델 없음).
#          사용자 피드백 2026-10-17 "아니 너무 또 길게 풀어서 쓰면 읽기 힘들잖아 최대한 짧지만 이해가 다 되도록 다시 고쳐봐".
#          임시 폴더만 씀 — 네트워크·GitHub 없음.
"""cd tools/tests && python3 -m unittest test_tts_patch_labels -v"""
import json
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import tts_narration as tn  # noqa: E402

VOICES = {"host": {"gap": 0.45, "parts": ["*"]}, "storyteller": {"gap": 0.45, "parts": ["사연"]}}
OLD = [("문장 하나.", "도입"), ("문장 둘.", "도입"), ("문장 셋.", "원칙 하나"), ("문장 넷.", "원칙 하나"), ("문장 다섯.", "정리")]


class PatchLabels(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.patches = [mock.patch.object(tn, "ROOT", root),
                        mock.patch.object(tn, "voice_mismatch", lambda meta, topic, vid: []),
                        mock.patch.object(tn, "load_voices", lambda topic, vid, args, quiet=False: VOICES)]
        for p in self.patches:
            p.start()
        src = root / "economic" / "source" / "v1"
        src.mkdir(parents=True)
        (src / "narration.mp3").write_bytes(b"x")
        items = [{"n": i + 1, "role": tn.role_of(p, VOICES), "part": p, "text": t, "start": i * 2.0, "end": i * 2.0 + 1.5}
                 for i, (t, p) in enumerate(OLD)]
        meta = {"script_sha1": "old", "items": items, "voices": {r: {"gap": v["gap"]} for r, v in VOICES.items()},
                "gaps": {"lead_in": 0.3, "part": 1.0, "tail": 0.8, "cards": []}}
        (src / tn.META_NAME).write_text(json.dumps(meta, ensure_ascii=False), "utf-8")
        self.args = types.SimpleNamespace(full=False, force=False, lead_in=0.3, part_gap=1.0, tail=0.8)

    def tearDown(self):
        for p in self.patches:
            p.stop()
        self.tmp.cleanup()

    def cand(self, rows):
        return tn.patch_candidate("economic", "v1", rows, [], self.args)

    def test_label_rename_with_text_change_is_partial(self):
        rows = [("문장 하나.", "도입"), ("문장 둘.", "도입"), ("문장 셋, 고침.", "원칙 하나, 새 이름"), ("문장 넷.", "원칙 하나, 새 이름"), ("문장 다섯.", "정리")]
        changed, why = self.cand(rows)
        self.assertIsNone(why)
        self.assertEqual(changed, [3])

    def test_boundary_change_is_full(self):
        rows = [("문장 하나.", "도입"), ("문장 둘.", "원칙 하나"), ("문장 셋.", "원칙 하나"), ("문장 넷.", "원칙 하나"), ("문장 다섯.", "정리")]
        changed, why = self.cand(rows)
        self.assertIsNone(changed)
        self.assertIn("나눔이 다름", why)

    def test_role_change_is_full(self):
        rows = [("문장 하나.", "도입 사연"), ("문장 둘.", "도입 사연"), ("문장 셋.", "원칙 하나"), ("문장 넷.", "원칙 하나"), ("문장 다섯.", "정리")]
        changed, why = self.cand(rows)
        self.assertIsNone(changed)
        self.assertIn("역할", why)

    def test_text_only_change_still_partial(self):
        rows = list(OLD)
        rows[4] = ("문장 다섯, 고침.", "정리")
        changed, why = self.cand(rows)
        self.assertEqual((changed, why), ([5], None))


if __name__ == "__main__":
    unittest.main()
