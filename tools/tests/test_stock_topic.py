#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-15 — 주식 주제 폴더(stock/) 설정이 분석 도구에서 읽히는지 + tag_keywords v1.3 TAG_OTHER 시험
#          (사용자 지시: "주식 주제로 유튜브 분석기 돌리기위한 세팅 좀 해줘 stock 폴더 만들고 검색어 설정 같은거 말이야").
#          네트워크·GitHub 요청 없음 (파일만 읽음).
"""python3 -m unittest tools.tests.test_stock_topic -v"""
import os
import sys
import tomllib
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
for k in ("GITHUB_TOKEN", "GH_TOKEN"):
    os.environ.pop(k, None)

import outlier_research as orr  # noqa: E402
import tag_keywords as tk  # noqa: E402


class StockTopicTest(unittest.TestCase):
    def test_config_files_parse(self):
        for name in ("analyzer_config.toml", "keywords.toml", "tag_rules.toml", "analysis_rules.toml"):
            with self.subTest(name=name):
                tomllib.loads((ROOT / "stock" / name).read_text("utf-8"))
        cfg = tomllib.loads((ROOT / "stock" / "analyzer_config.toml").read_text("utf-8"))
        flat = {}
        for k, v in cfg.items():
            flat.update(v if isinstance(v, dict) else {k: v})
        self.assertEqual(flat.get("TOPIC"), "주식")
        self.assertEqual(flat.get("PROJECT_FOLDER"), "stock")
        self.assertIs(flat.get("DOWNLOAD_VIDEOS"), False)      # 다른 사람의 영상 파일은 받지 않음

    def test_keywords_load(self):
        kw, exclude, name, path, rel = orr.load_keywords("stock", 0)
        self.assertEqual(name, "주식")
        self.assertTrue(str(path).endswith("stock/keywords.txt"))
        terms = [t for _, t in kw]
        self.assertGreaterEqual(len(terms), 20)
        self.assertEqual(len(terms), len({orr._norm(t) for t in terms}))   # 겹치는 검색어 없음
        self.assertIn("주식", rel["strong"])
        rules = tk.load_rules("stock")
        for t in terms:                                         # 빼는 말(종목 이름·부동산·코인·뉴스 …)이 검색어에 없음
            keep = orr._norm(t) in rules["keep"]
            self.assertFalse(not keep and any(x.lower() in t.lower() for x in rules["exclude"]), t)

    def test_tag_other_label(self):
        rules = tk.load_rules("stock")
        self.assertEqual(rules["other"], "기타 주식")
        self.assertEqual(tk.theme_of("알수없는태그", rules["themes"], rules["other"]), "기타 주식")
        self.assertEqual(tk.theme_of("알수없는태그", {}), tk.OTHER_DEFAULT)        # TAG_OTHER 없으면 예전처럼
        self.assertEqual(tk.load_rules("economic")["other"], "기타 재테크")        # 재테크 주제는 그대로


if __name__ == "__main__":
    unittest.main()
