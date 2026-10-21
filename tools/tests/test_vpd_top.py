#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-10-21 — web_ui v2.4.1: 추천 경계 = min(목록 경계, 지난 분석 경계) 시험 2개 (분석 경계 아래 목록 영상도 추천 · 분석 경계가
#          목록 경계보다 높으면 목록 경계 그대로 · TOP_PCT 가 다르면 지난 분석 경계를 쓰지 않음)
# (v1.0 — 2026-10-21 — '하루 조회수 상위' 시험 (사용자 지시 2026-10-21 "주제 탐색 시 구독자, 날짜 상관 없이 업로드 기간 대비 조회수가 높은
#          영상은 모두 분석 대상에 넣어" — 상위 10%·성공 사례와 따로 묶음): outlier_research v2.6 top_pct_threshold · web_ui v2.4 preselect ·
#          success_analysis v1.5 vpd_top_group·comment_needs. 네트워크·GitHub 요청 없음.
"""python3 -m unittest tools.tests.test_vpd_top -v"""
import os
import sys
import unittest
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
for k in ("GITHUB_TOKEN", "GH_TOKEN"):
    os.environ.pop(k, None)

import outlier_research as orr      # noqa: E402
import success_analysis as sa       # noqa: E402
import web_ui as web                # noqa: E402

web.orr = orr                       # web_ui.main 이 하는 불러오기 (preselect 가 orr.top_pct_threshold 를 씀)


def row(i, vpd, views=None, subs=1_000_000, short=False, relevant=True, src="검색:주식"):
    return {"id": f"v{i:010d}", "views_per_day": vpd, "views": views if views is not None else int(vpd * 10), "subs": subs,
            "ratio": round((views or vpd * 10) / subs, 2), "in_window": True, "short": short, "relevant": relevant, "sources": [src]}


class ThresholdTest(unittest.TestCase):
    def test_top_pct(self):
        vals = list(range(1, 101))                                # 1..100
        self.assertEqual(orr.top_pct_threshold(vals, 10), 91.0)  # 상위 10% = 91~100 (10개)
        self.assertEqual(orr.top_pct_threshold(vals, 25), 76.0)
        self.assertEqual(orr.top_pct_threshold([5], 10), 5.0)    # 한 개면 그것
        self.assertIsNone(orr.top_pct_threshold([], 10))
        self.assertIsNone(orr.top_pct_threshold(vals, 0))         # 0 = 끔
        self.assertEqual(orr.top_pct_threshold([3, None, 7], 50), 7.0)   # None 은 셈에서 뺌


class PreselectTest(unittest.TestCase):
    def test_vpd_top_regardless_of_subs(self):
        rows = [row(i, vpd=i) for i in range(1, 101)]             # 구독자 100만 — 작은 채널 성공 사례가 아님
        info = {}
        r = web.preselect(rows, 10, info)
        vtop = {k for k, v in r.items() if v == "하루 조회수 상위"}
        pop = {k for k, v in r.items() if v == "조회수 상위"}
        self.assertEqual(info["threshold"], 91.0)
        self.assertEqual(info["pool"], 100)
        self.assertEqual(len(vtop | pop), 20)                     # 상위 10% 10개 + 조회수 상위 20 (겹침) — 하루 조회수 상위 10개는 모두 추천
        self.assertTrue(all(rows[i]["id"] in vtop | pop for i in range(90, 100)))

    def test_off_and_pool_rules(self):
        rows = [row(i, vpd=i) for i in range(1, 51)] + [row(99, vpd=10 ** 6, short=True), row(98, vpd=10 ** 6, relevant=False),
                                                        row(97, vpd=10 ** 6, src="채널:어느 채널")]
        r = web.preselect(rows, 0)                                # 0 = 끔 → 하루 조회수 상위 없음
        self.assertNotIn("하루 조회수 상위", r.values())
        r = web.preselect(rows, 10)
        for vid in ("v0000000099", "v0000000098"):                # 쇼츠·주제 밖은 모집단·추천에서 빠짐
            self.assertNotIn(vid, r)
        self.assertNotEqual(r.get("v0000000097"), "하루 조회수 상위")   # 검색이 아닌 채널 영상은 모집단 밖 (그쪽은 '추가한 채널' 규칙)

    def test_analysis_threshold_lowers_cut(self):
        rows = [row(i, vpd=i) for i in range(1, 101)]
        info = {}
        r = web.preselect(rows, 10, info, analysis_thr=70.0)       # 분석(모든 검색) 경계 70 < 목록 경계 91 → 70 이상 모두 추천
        self.assertEqual(info["list_threshold"], 91.0)
        self.assertEqual(info["threshold"], 70.0)
        self.assertTrue(all(rows[i]["id"] in r for i in range(69, 100)))
        self.assertNotIn(rows[68]["id"], r)                         # 69 는 경계 아래 (조회수 상위 20 도 아님)
        info = {}
        web.preselect(rows, 10, info, analysis_thr=95.0)            # 분석 경계가 더 높으면 목록 경계 그대로
        self.assertEqual(info["threshold"], 91.0)
        info = {}
        r = web.preselect(rows, 0, info, analysis_thr=70.0)         # 0 = 끔 — 분석 경계가 있어도 하루 조회수 상위 없음
        self.assertNotIn("하루 조회수 상위", r.values())

    def test_analysis_threshold_read(self):
        import json, shutil, tempfile
        tmp = Path(tempfile.mkdtemp())
        saved = web.out_dir
        try:
            web.out_dir = lambda t: tmp
            self.assertIsNone(web.vpd_analysis_threshold("tt", 10))                       # 분석 없음
            (tmp / "analysis.json").write_text(json.dumps({"vpd_top": {"pct": 10, "threshold": 19570.8}}), "utf-8")
            self.assertEqual(web.vpd_analysis_threshold("tt", 10), 19570.8)
            self.assertIsNone(web.vpd_analysis_threshold("tt", 20))                       # TOP_PCT 가 다르면 쓰지 않음
            (tmp / "analysis.json").write_text(json.dumps({"vpd_top": {"pct": 10, "threshold": None}}), "utf-8")
            self.assertIsNone(web.vpd_analysis_threshold("tt", 10))                       # 모집단이 작아 경계 없음
        finally:
            web.out_dir = saved
            shutil.rmtree(tmp)


def case(i, vpd, channel="C1", subs=2_000_000, age=30, minutes=20.0, exclude="", comments=()):
    now = datetime(2026, 10, 21, tzinfo=timezone.utc)
    return {"id": f"c{i:010d}", "title": f"제목 {i}", "channel": channel, "channel_id": channel, "subs": subs, "views": int(vpd * age),
            "vpd": vpd, "ratio": round(vpd * age / subs, 2), "age_days": age, "published": now - timedelta(days=age), "minutes": minutes,
            "theme": "기타", "format": sa.FORMAT_OTHER, "src": "설명", "comments_fetched": len(comments), "comments_total": len(comments),
            "exclude": exclude, "comments": [{"text": t, "creator": False, "likes": 3, "reply": False} for t in comments]}


class GroupTest(unittest.TestCase):
    def rules(self, **kw):
        r = {k: dict(v) for k, v in sa.DEFAULT_RULES.items()}
        r["vpd_top"].update({"MIN_POOL": 5, **kw})
        return r

    def test_group_any_subs_any_age_per_channel(self):
        pool = [case(i, vpd=i * 100, channel=f"P{i}") for i in range(1, 41)]          # 검색 모집단 40개 (하루 100~4,000)
        cases = [case(101, vpd=5000, channel="A", age=900), case(102, vpd=4500, channel="A"), case(103, vpd=4200, channel="A"),
                 case(104, vpd=3900, channel="B", subs=3000), case(105, vpd=50, channel="C"), case(106, vpd=9000, channel="D", exclude="뺀 주제(코인)")]
        rows_all = pool + cases
        searched = {x["id"] for x in rows_all}
        res, group = sa.vpd_top_group(cases, rows_all, searched, [], self.rules())
        self.assertIsNotNone(res["threshold"])
        ids = [c["id"] for c in group]
        self.assertEqual(ids[:2], ["c0000000101", "c0000000102"])                    # 900일 지난 영상·구독자 200만도 들어감 (날짜·구독자 상관없이)
        self.assertNotIn("c0000000103", ids)                                         # 채널 A 는 2개까지
        self.assertEqual(res["channel_cut"], 1)
        self.assertIn("c0000000104", ids)                                            # 작은 채널도 경계를 넘으면 함께
        self.assertNotIn("c0000000105", ids)                                         # 경계 아래
        self.assertEqual([x["id"] for x in res["excluded"]], ["c0000000106"])        # 뺄 까닭(주제 밖·광고 의심 등)은 뺌
        self.assertEqual(res["older_than_success"], 1)
        self.assertEqual(res["missing_total"], sum(1 for x in pool if x["vpd"] >= res["threshold"]))   # 자료 없는 후보 = 모집단에서 넘은 것

    def test_small_pool_off(self):
        cases = [case(1, vpd=100)]
        res, group = sa.vpd_top_group(cases, cases, {"c0000000001"}, [], self.rules(MIN_POOL=30))
        self.assertIsNone(res["threshold"])
        self.assertEqual(group, [])

    def test_comment_needs_same_rules(self):
        cs = [case(1, vpd=10, comments=["다음엔 배당 ETF 도 다뤄 주세요", "좋은 정보 감사합니다", "구독했어요 다음 영상 기대합니다"])]
        cs[0]["vno"] = 1
        needs, st = sa.comment_needs(cs, lambda c: f"V{c['vno']}")
        self.assertEqual(st["viewer"], 3)
        self.assertNotIn("needs", cs[0])                                            # store=False 면 사례에 적지 않음 (성공 사례 값을 덮지 않게)
        self.assertTrue(any(q["no"] == "V1" for qs in needs["top"].values() for q in qs))
        needs2, _ = sa.comment_needs(cs, lambda c: 1, store=True)
        self.assertIsInstance(cs[0]["needs"], Counter)


if __name__ == "__main__":
    unittest.main()
