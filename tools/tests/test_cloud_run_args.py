# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-21 — tools/cloud_run.py v1.5.1 인자 읽기 시험: '-' 로 시작하는 영상 ID(예: -Fl1y9riPs4)가 옵션으로 읽히지 않음
#          (2026-10-21 132개 승인이 argparse 오류 exit 2 로 시작도 못 함). 파싱만 — 명령은 돌리지 않음 (저장소·네트워크 안 건드림).
"""python3 -m unittest test_cloud_run_args  (tools/tests 에서)"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import cloud_run as cr  # noqa: E402


class Args(unittest.TestCase):
    def test_dash_id(self):
        a = cr.parse_args(["stock", "approve", "-Fl1y9riPs4", "V4mCCBmoCdc", "_-RPtfTtpL0"])
        self.assertEqual(a.ids, ["-Fl1y9riPs4", "V4mCCBmoCdc", "_-RPtfTtpL0"])

    def test_options_still_options(self):
        a = cr.parse_args(["stock", "list", "--unchecked", "--log-level", "DEBUG"])   # '--unchecked'·'--log-level' 도 11자 — 옵션 그대로
        self.assertTrue(a.unchecked)
        self.assertEqual(a.log_level, "DEBUG")
        self.assertEqual(a.ids, [])
        a = cr.parse_args(["stock", "uncheck", "--shorts", "-abcdefghij"])
        self.assertTrue(a.shorts)
        self.assertEqual(a.ids, ["-abcdefghij"])

    def test_double_dash(self):
        a = cr.parse_args(["stock", "approve", "--", "-Fl1y9riPs4"])
        self.assertEqual(a.ids, ["-Fl1y9riPs4"])


if __name__ == "__main__":
    unittest.main()
