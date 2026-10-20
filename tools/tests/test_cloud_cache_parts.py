# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-20 — tools/cloud_run.py v1.4 캐시 묶음 나누기 시험 (임시 폴더만 씀 — 저장소·네트워크 안 건드림).
"""python3 -m unittest test_cloud_cache_parts  (tools/tests 에서)"""
import json
import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import cloud_run as cr  # noqa: E402


class CacheParts(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.saved = (cr.ROOT, cr.w.out_dir, cr.CACHE_PART_BYTES)
        cr.ROOT = self.tmp
        cr.w.out_dir = lambda t: self.tmp / t / "result" / "outliers"
        self.cache = self.tmp / "tt" / "result" / "outliers" / ".cache"
        self.cache.mkdir(parents=True)
        for i in range(40):     # 압축이 잘 안 되는 내용 — 조각이 여러 개 나오게
            (self.cache / f"vid{i:08d}.json").write_bytes(json.dumps({"id": i, "r": os.urandom(400).hex()}).encode())

    def tearDown(self):
        cr.ROOT, cr.w.out_dir, cr.CACHE_PART_BYTES = self.saved
        shutil.rmtree(self.tmp)

    def _arc(self):
        return cr.cache_paths("tt")[0]

    def test_small_stays_single(self):
        cr.CACHE_PART_BYTES = 10_000_000
        r = cr.cache_save("tt")
        self.assertEqual(r["cache_parts"], 0)
        self.assertTrue(self._arc().is_file())
        self.assertEqual(cr.cache_parts(self._arc()), [])

    def test_split_load_and_shrink_back(self):
        cr.CACHE_PART_BYTES = 8_000
        r = cr.cache_save("tt")
        parts = cr.cache_parts(self._arc())
        self.assertGreater(r["cache_parts"], 1)
        self.assertEqual(len(parts), r["cache_parts"])
        self.assertFalse(self._arc().exists())
        self.assertTrue(all(p.stat().st_size <= 8_000 for p in parts))
        info = json.loads(cr.cache_paths("tt")[1].read_text())
        self.assertEqual(info["parts"], [p.name for p in parts])
        before = {f.name: f.read_bytes() for f in self.cache.iterdir()}
        shutil.rmtree(self.cache)
        r = cr.cache_load("tt")
        self.assertTrue(r["cache_loaded"])
        self.assertEqual({f.name: f.read_bytes() for f in self.cache.iterdir()}, before)
        cr.CACHE_PART_BYTES = 10_000_000          # 다시 작아지면 조각을 지우고 cache.tgz 하나
        r = cr.cache_save("tt")
        self.assertEqual(r["cache_parts"], 0)
        self.assertTrue(self._arc().is_file())
        self.assertEqual(cr.cache_parts(self._arc()), [])

    def test_load_old_single(self):
        cr.CACHE_PART_BYTES = 10_000_000
        cr.cache_save("tt")
        shutil.rmtree(self.cache)
        self.assertTrue(cr.cache_load("tt")["cache_loaded"])
        self.assertEqual(len(list(self.cache.iterdir())), 40)


if __name__ == "__main__":
    unittest.main()
