#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-10-15 — 검색어가 모두 주식 낱말(TAG_REQUIRE)인지 · 주제 캐시 치우기(pc_analysis v1.13 reset_topic_cache·fresh_start) ·
#          분석기가 FRESH_START 를 '모르는 설정'으로 보지 않는지 (사용자 지시: "아니 검색어 다 주식 관련으로 변경하고 그리고 왜 예전 재테크
#          캐시가 남아 있어 이거 어떻게해"). 캐시 시험은 임시 폴더를 저장소 대신 씀 (진짜 파일·GitHub 안 건드림)
# (v1.0 — 2026-10-15 — 주식 주제 폴더(stock/) 설정이 분석 도구에서 읽히는지 + tag_keywords v1.3 TAG_OTHER 시험
#          (사용자 지시: "주식 주제로 유튜브 분석기 돌리기위한 세팅 좀 해줘 stock 폴더 만들고 검색어 설정 같은거 말이야").
#          네트워크·GitHub 요청 없음 (파일만 읽음).)
"""python3 -m unittest tools.tests.test_stock_topic -v"""
import os
import sys
import tempfile
import tomllib
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
for k in ("GITHUB_TOKEN", "GH_TOKEN"):
    os.environ.pop(k, None)

import outlier_research as orr  # noqa: E402
import pc_analysis as pc  # noqa: E402
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

    def test_keywords_all_stock_words(self):
        """v1.1: 검색어마다 주식 낱말(TAG_REQUIRE) 하나 이상 — 재테크·연금·노후준비·부자·반도체 같은 넓은 말 없음."""
        rules = tk.load_rules("stock")
        self.assertTrue(rules["require"])
        terms = orr.read_keyword_list(ROOT / "stock" / "keywords.txt")
        for t in terms:
            self.assertTrue(any(w.lower() in t.lower() for w in rules["require"]), t)
        for broad in ("재테크", "연금", "노후준비", "부자", "투자", "반도체", "2차전지", "퇴직연금", "ISA", "연금저축"):
            self.assertNotIn(broad, terms)
        self.assertNotIn("재테크", (ROOT / "stock" / "keywords.txt").read_text("utf-8"))   # 묶음 이름에도 없음
        self.assertEqual(tk.load_rules("economic")["require"], [])                          # 재테크 주제는 그대로

    def test_require_rule_in_choose(self):
        rules = {"exclude": [], "keep": [], "require": ["주식"], "themes": {}, "other": "기타"}
        stats = {"주식초보": {"channels": 9, "videos": 9, "views": 1}, "재테크": {"channels": 9, "videos": 9, "views": 1}}
        picked, rows = tk.choose(stats, rules, 40, 5)
        self.assertEqual([r["tag"] for r in picked], ["주식초보"])
        self.assertTrue(next(r for r in rows if r["tag"] == "재테크")["why"].startswith("주제 낱말 없음"))

    def test_analyzer_accepts_fresh_start(self):
        sys.path.insert(0, str(ROOT))
        import youtube_topic_analyzer as y
        cfg = y.collect_config(vars(y))
        r = y.apply_config_file(cfg, ROOT / "stock" / "analyzer_config.toml")
        self.assertFalse([u for u in r["unknown"] if "FRESH_START" in u], r["unknown"])
        self.assertNotIn("FRESH_START", cfg)


class TopicCacheResetTest(unittest.TestCase):
    """pc_analysis v1.13 — 임시 폴더를 저장소(ROOT) 대신."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self._root = pc.ROOT
        pc.ROOT = self.root
        for f in ("t", "e"):
            (self.root / f).mkdir()
        (self.root / "t" / "analyzer_config.toml").write_text('[topic]\nTOPIC = "주식"\nPROJECT_FOLDER = "t"\nFRESH_START = "2026-10-15"\n', "utf-8")
        (self.root / "e" / "analyzer_config.toml").write_text('[topic]\nTOPIC = "재테크"\nPROJECT_FOLDER = "e"\n', "utf-8")
        for f in ("t", "e"):
            od = self.root / f / "result" / "outliers"
            (od / ".cache").mkdir(parents=True)
            (od / ".cache" / "search_x.json").write_text("{}", "utf-8")
            (od / "W_abc").mkdir()
            (od / "W_abc" / "metadata.json").write_text("{}", "utf-8")
            (self.root / f / "result" / "web").mkdir()
            (self.root / f / "result" / "web" / "explore.json").write_text("{}", "utf-8")
            (self.root / "output" / f / "result" / "success_cases").mkdir(parents=True)

    def tearDown(self):
        pc.ROOT = self._root
        self.tmp.cleanup()

    def test_reset_cache_keeps_approved(self):
        r = pc.reset_topic_cache("e")
        self.assertEqual(sorted(r["moved"]), ["e/result/outliers/.cache", "e/result/web"])
        self.assertFalse((self.root / "e" / "result" / "outliers" / ".cache").exists())
        self.assertTrue((self.root / "e" / "result" / "outliers" / "W_abc" / "metadata.json").is_file())   # 승인한 자료는 그대로
        self.assertTrue((self.root / "output" / "e" / "result").is_dir())                                 # 분석기 결과도 그대로
        self.assertTrue((self.root / r["to"] / "e" / "result" / "outliers" / ".cache" / "search_x.json").is_file())  # 지우지 않고 옮김
        self.assertTrue((self.root / "t" / "result" / "outliers" / ".cache").is_dir())                    # 다른 주제는 안 건드림
        self.assertEqual(pc.reset_topic_cache("e")["moved"], [])                                          # 두 번째는 치울 것 없음

    def test_fresh_start_once(self):
        self.assertIsNone(pc.fresh_start("e"))                                       # FRESH_START 없는 주제(재테크)는 그대로
        self.assertTrue((self.root / "e" / "result" / "outliers" / "W_abc").is_dir())
        r = pc.fresh_start("t")
        self.assertEqual(sorted(r["moved"]), ["output/t", "t/result"])
        self.assertFalse((self.root / "t" / "result").exists())
        self.assertTrue((self.root / "t" / "analyzer_config.toml").is_file())        # 설정은 그대로
        self.assertIsNone(pc.fresh_start("t"))                                       # 같은 날짜면 다시 안 함
        cfg = self.root / "t" / "analyzer_config.toml"
        cfg.write_text(cfg.read_text("utf-8").replace("2026-10-15", "2026-10-16"), "utf-8")
        (self.root / "t" / "result" / "web").mkdir(parents=True)
        self.assertEqual(pc.fresh_start("t")["moved"], ["t/result"])                 # 날짜를 바꾸면 한 번 더


if __name__ == "__main__":
    unittest.main()
