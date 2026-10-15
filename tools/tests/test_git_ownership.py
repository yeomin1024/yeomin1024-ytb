#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-15 — git '소유자가 다름'(dubious ownership) 시험 (사용자 보고: "[GITHUB] ❌ 푸시 실패 … git add 실패 (code=128):
#          fatal: detected dubious ownership in repository at 'D:/유튜브 분석기/.yt_work/_github_clone_stock' 왜이래").
#          분석기 v2.14.1 run_git 이 자기 작업 폴더(.yt_work 아래)에서만 safe.directory 를 붙이는지 — 다른 사용자 소유 폴더를 만들어
#          확인 (리눅스에서 root 일 때만 — 소유자를 바꿀 수 있어야 함). 진짜 GitHub 요청 없음.
"""cd tools/tests && python3 -m unittest test_git_ownership -v"""
import importlib.util
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

REPO = Path(__file__).resolve().parents[2]


@unittest.skipUnless(hasattr(os, "geteuid") and os.geteuid() == 0 and shutil.which("git")
                     and importlib.util.find_spec("requests"), "root·git·requests 가 있어야 (소유자를 바꿔 시험)")
class TestGitOwnership(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sys.path.insert(0, str(REPO))
        import youtube_topic_analyzer as y
        cls.y = y

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.base = Path(self.tmp.name) / "유튜브 분석기"
        self.patch = mock.patch.object(self.y, "BASE_DIR", self.base)
        self.patch.start()

    def tearDown(self):
        self.patch.stop()
        self.tmp.cleanup()

    def _foreign_repo(self, path):
        path.mkdir(parents=True)
        subprocess.run(["git", "init", "-q", str(path)], check=True)
        (path / "a.txt").write_text("a", "utf-8")
        for p in [path, *path.rglob("*")]:
            os.chown(p, 4321, 4321)                    # 다른 사용자 소유 (Windows: Administrators 그룹 소유와 같은 상황)
        return path

    def test_own_work_clone_is_trusted(self):
        clone = self._foreign_repo(self.base / ".yt_work" / "_github_clone_stock")
        code, out = self.y.run_git(["add", "a.txt"], clone)              # 예전: fatal: detected dubious ownership
        self.assertEqual(code, 0, out)
        self.assertIn("safe.directory=" + clone.resolve().as_posix(), " ".join(self.y._safe_dir_args(clone)))

    def test_other_folders_still_checked(self):
        other = self._foreign_repo(Path(self.tmp.name) / "남의 저장소")
        self.assertEqual(self.y._safe_dir_args(other), [])               # 분석기 작업 폴더가 아니면 git 검사 그대로
        with self.assertRaises(RuntimeError) as cm:
            self.y.run_git(["add", "a.txt"], other)
        self.assertIn("dubious ownership", str(cm.exception))
        self.assertIn("git config --global --add safe.directory", str(cm.exception))   # 손으로 고치는 한 줄


if __name__ == "__main__":
    unittest.main()
