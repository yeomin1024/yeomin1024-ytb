#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-15 — Windows 파일 바꿔치기 막힘(WinError 5) 시험 (사용자 보고: "[JOB] stock 승인 — 자료 받고 분석 실패 … PermissionError:
#          [WinError 5] 액세스가 거부되었습니다: …quota_key_….json.tmp -> …quota_key_….json 왜이래"). 리눅스에서 os.replace·읽기를 가짜로 막아
#          pc_analysis v1.18 replace_retry·KeyLedger, web_ui v2.3.1 _read_json·_write_json 확인. 진짜 YouTube·GitHub 요청 없음.
"""cd tools/tests && python3 -m unittest test_windows_files -v"""
import json
import sys
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent))
from test_quota_saving import KEY, Base, orr, pc, web  # noqa: E402

REAL_REPLACE = pc.os.replace


def flaky_replace(fail_times):
    """처음 fail_times 번은 WinError 5 처럼 PermissionError, 그다음은 진짜 os.replace."""
    state = {"n": 0}

    def fn(src, dst):
        state["n"] += 1
        if state["n"] <= fail_times:
            raise PermissionError(13, "액세스가 거부되었습니다 (시험)")
        return REAL_REPLACE(src, dst)
    fn.state = state
    return fn


class TestWindowsFiles(Base):
    def setUp(self):
        super().setUp()
        self.sleep = mock.patch.object(pc.time, "sleep")       # 다시 할 때 쉬는 시간은 건너뜀
        self.sleep.start()

    def tearDown(self):
        self.sleep.stop()
        super().tearDown()

    def test_replace_retry_then_ok(self):
        kl = pc.KeyLedger(KEY)
        with mock.patch.object(pc.os, "replace", flaky_replace(3)) as fr:
            self.assertTrue(kl.reserve(100, "web_approve", "stock"))
        self.assertEqual(fr.state["n"], 4)
        self.assertEqual(kl.used(), 100)                                   # 다시 해서 적힘

    def test_never_ok_job_continues(self):
        kl = pc.KeyLedger(KEY)
        kl.reserve(50, "web", "stock")
        with mock.patch.object(pc.os, "replace", flaky_replace(10 ** 6)):
            self.assertTrue(kl.reserve(1, "web_approve", "stock"))        # 예전: PermissionError 로 승인 작업이 멈춤
            kl.refund(1, "web_approve", "stock")                         # 오류 없이 넘어감
        self.assertEqual(kl.used(), 50)                                    # 못 적은 1단위만 빠짐 — 장부는 그대로
        self.assertFalse(list(Path(kl.p.parent).glob("quota_key_*.tmp")))  # 임시 파일 안 남김

    def test_read_blocked_does_not_wipe(self):
        kl = pc.KeyLedger(KEY)
        kl.reserve(700, "web", "stock")
        real_read = pc.read_text_retry

        def blocked(path, *a, **k):
            if str(path).endswith(kl.p.name):
                raise PermissionError(13, "시험")
            return real_read(path, *a, **k)
        with mock.patch.object(pc, "read_text_retry", blocked):
            self.assertEqual(kl.snapshot()["used"], 700)                   # 화면: 마지막으로 읽은 값
            self.assertTrue(kl.reserve(5, "web", "stock"))                 # 쓰는 쪽: 읽기 실패면 덮어쓰지 않고 넘어감
        self.assertEqual(kl.used(), 700)                                   # 예전: 빈 장부로 보고 0 으로 덮어쓸 수 있었음

    def test_read_text_retry(self):
        p = self.root / "x.json"
        p.write_text('{"a": 1}', "utf-8")
        calls = {"n": 0}
        real = Path.read_text

        def flaky(self_, *a, **k):
            calls["n"] += 1
            if calls["n"] <= 2:
                raise PermissionError(13, "시험")
            return real(self_, *a, **k)
        with mock.patch.object(Path, "read_text", flaky):
            self.assertEqual(pc.read_text_retry(p), '{"a": 1}')
        self.assertIsNone(pc.read_text_retry(self.root / "없음.json"))

    def test_web_json_retry(self):
        p = self.root / "economic" / "result" / "web" / "explore.json"
        web._write_json(p, {"checked": ["a"]})
        with mock.patch.object(pc.os, "replace", flaky_replace(2)):
            web._write_json(p, {"checked": ["a", "b"]})
        self.assertEqual(web._read_json(p, {})["checked"], ["a", "b"])
        self.assertFalse(list(p.parent.glob("*.tmp")))


if __name__ == "__main__":
    unittest.main()
