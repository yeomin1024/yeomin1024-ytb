# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-22 — tools/comment_types.py v1.0 시험: 규칙 유형 예시·Wilson 범위·보정(줄이 적으면 합친 줄·fallback)·표본 씨앗 고정
#          (임시 폴더만 — 저장소 결과·네트워크·GitHub 안 건드림).
"""python3 -m unittest test_comment_types  (tools/tests 에서)"""
import json
import os
import shutil
import sys
import tempfile
import unittest
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
for k in ("GITHUB_TOKEN", "GH_TOKEN"):
    os.environ.pop(k, None)
import comment_types as ct  # noqa: E402


class Classify(unittest.TestCase):
    def test_examples(self):
        cases = {
            "국민연금 특검해야 합니다": "G",
            "ISA계좌 개설후 ETF 투자하면 3년뒤 해지할때 다 매도해야 되나요?": "Q",
            "What is the best ETF to buy now?": "Q",
            "언제적 방송이야!!!!": "C",
            "이해하기 쉽게 설명해 주셔서 정말 유익했습니다": "P",
            "저도 퇴직금 절반 넣어서 손실 -47% 중입니다": "E",
            "빚투는 투기 입니다": "O",
            "ㅋㅋㅋㅋㅋㅋ": "R",
            "❤❤❤": "R",
            "오픈 채팅방 리딩방 오세요": "S",
            "Question 1 = buy, loss 5000": "S",
            "5:30 타임라인 정리 감사": "I",                      # 시각 + 글 = 정보 (칭찬보다 먼저)
        }
        for text, want in cases.items():
            self.assertEqual(ct.classify(text), want, text)

    def test_every_comment_gets_one_code(self):
        for t in ("", "   ", "아무 말", "Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod"):
            self.assertIn(ct.classify(t), ct.TYPE_ORDER)


class Stats(unittest.TestCase):
    def test_wilson(self):
        lo, hi = ct.wilson(50, 100)
        self.assertLess(lo, 0.5)
        self.assertGreater(hi, 0.5)
        self.assertAlmostEqual((lo + hi) / 2, 0.5, places=2)
        self.assertEqual(ct.wilson(0, 0), (None, None))

    def test_calibrate(self):
        rows = {"한국어": {"G": Counter({"G": 8, "O": 2})}, "전체": {"G": Counter({"G": 8, "O": 2}), "R": Counter({"R": 1})}}
        fb = Counter({"O": 1, "R": 1})
        est = ct.calibrate(Counter({"G": 100}), "한국어", rows, fb)
        self.assertAlmostEqual(est["G"], 0.8)
        self.assertAlmostEqual(est["O"], 0.2)
        est = ct.calibrate(Counter({"R": 10}), "한국어", rows, fb)           # 줄이 MIN_ROW 미만 → 합친 줄도 1개뿐 → fallback
        self.assertAlmostEqual(est["O"], 0.5)
        self.assertAlmostEqual(est["R"], 0.5)
        self.assertAlmostEqual(sum(est.values()), 1.0)


class SampleSeed(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.saved = ct.ROOT
        ct.ROOT = self.tmp
        out = self.tmp / "tt" / "result" / "outliers"
        for i in range(3):
            d = out / f"W_v{i:010d}"
            d.mkdir(parents=True)
            (d / "metadata.json").write_text(json.dumps({"id": f"v{i:010d}", "video_lang": "ko" if i < 2 else "en"}), "utf-8")
            lines = ["id,parent,is_reply,likes,replies,creator,published,text"]
            lines += [f"c{i}_{k},,False,{k},0,{'True' if k == 0 else 'False'},2026-10-01T00:00:00,댓글 {i} {k}" for k in range(30)]
            (d / "comments.csv").write_text("\n".join(lines), "utf-8")
        self.out = out

    def tearDown(self):
        ct.ROOT = self.saved
        shutil.rmtree(self.tmp)

    def test_same_seed_same_sample(self):
        ct.cmd_sample("tt")
        a = (self.out / "comment_type_sample.tsv").read_text("utf-8")
        ct.cmd_sample("tt")
        self.assertEqual(a, (self.out / "comment_type_sample.tsv").read_text("utf-8"))
        self.assertNotIn("c0_0", a)                                          # 채널 주인 댓글은 모집단 밖
        rows = a.strip().split("\n")[1:]
        self.assertEqual(sum(1 for r in rows if "\t한국어\t" in r), 58)       # 한국어 모집단 58 (< 600) → 전부
        self.assertEqual(sum(1 for r in rows if "\t영어\t" in r), 29)


if __name__ == "__main__":
    unittest.main()
