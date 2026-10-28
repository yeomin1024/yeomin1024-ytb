# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-10-28 — target_check v1.1: 분석 묶음(V·T) 그대로 · ③ 모집단에 기간 없는 검색 · ② 는 최근만 · 판정 문구.
# v1.0 — 2026-10-28 — tools/target_check.py v1.0 시험: 세 묶음 표시·분석 상태(성공 #·V·채널당 넘음·자료 안 받음·묶음 없음)·받은 때 하루 조회수·
#          확인 결과 판정·겹침·엑셀 (임시 폴더만 — 저장소 결과·네트워크·GitHub 안 건드림).
"""python3 -m unittest test_target_check  (tools/tests 에서)"""
import os
import shutil
import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
for k in ("GITHUB_TOKEN", "GH_TOKEN"):
    os.environ.pop(k, None)
import target_check as tc  # noqa: E402

NOW = datetime(2026, 10, 28, tzinfo=timezone.utc)
RULES = {"success": {"MAX_AGE_DAYS": 180, "MAX_SUBS": 50000, "MIN_RATIO": 3.0, "MIN_VIEWS": 10000, "MIN_MINUTES": 4.0, "CASES_PER_CHANNEL": 2,
                     "MIN_AGE_DAYS": 7, "MIN_VPD_SUBS": 0.1, "WEIGHT": "score"},
         "vpd_top": {"TOP_PCT": 10, "MIN_MINUTES": 4.0, "CASES_PER_CHANNEL": 2, "MIN_POOL": 30, "MAX_AGE_DAYS": 182}}


def V(i, views, subs, age, ch="c", minutes=10.0, exclude=""):
    pub = NOW - timedelta(days=age)
    return {"id": f"v{i:03d}", "title": f"t{i}", "channel": ch, "channel_id": ch, "subs": subs, "views": views, "published": pub,
            "age_days": age, "minutes": minutes, "ratio": round(views / max(subs, 100), 2), "vpd": round(views / max(age, 1), 1),
            "exclude": exclude, "foreign": False, "theme": ""}


def long_src():
    rows = [V(i, 1000 * (i + 1), 100000, 30, ch=f"c{i}") for i in range(40)]          # 큰 채널 40개 (성공 아님)
    rows.append(V(100, 60000, 10000, 20, ch="s1"))                                     # 성공 (하루 3,000 = 구독자의 0.3) — 분석 #1
    rows.append(V(101, 50000, 10000, 20, ch="s2"))                                     # 성공 — 자료 안 받음
    rows.append(V(102, 5_000_000, 900000, 10, ch="big"))                               # 하루 조회수·조회수 모두 1위 — 분석 V1 · T1
    rows.append(V(103, 70000, 10000, 20, ch="s3", exclude="주제 밖"))                    # 뺄 까닭 → 어디에도 안 듦
    searched = {r["id"] for r in rows}                                                 # 여기까지 = 검색에서 본 영상
    rows.append(V(104, 45000, 10000, 20, ch="s4"))                                     # 검색이 아니라 채널 평소 영상으로만 본 성공 후보
    rows.append(V(105, 90_000_000, 2_000_000, 2500, ch="old"))                         # 기간 없는 검색으로만 찾은 옛 영상 — ③ 만
    cases = [{"id": "v100"}, {"id": "v102"}, {"id": "v103"}]
    fetched = {"v102": (NOW - timedelta(days=5)).isoformat()}
    data = {"vpd_top": {"threshold": 40000.0, "max_age_days": 182, "per_channel": 2, "cases": [{"id": "v102", "vno": 1}]},
            "views_top": {"threshold": 5_000_000, "per_channel": 2, "cases": [{"id": "v102", "tno": 1}]}}
    return {"rules": RULES, "data": data, "success": [{"id": "v100", "no": 1}], "rows": rows, "cases": cases, "searched": searched,
            "alltime": {"v105"}, "fetched": fetched}


class Build(unittest.TestCase):
    def setUp(self):
        meta = {tc.LONG: {"weeks": 26, "generated": "x", "pending_alltime": 3, "reason": {"v102": "조회수 상위"}},
                tc.SHORT: {"weeks": 26, "generated": "x", "pending_alltime": 0, "reason": {}}}
        self.rows, self.summary = tc.build(long_src(), None, 10, meta)
        self.by = {r["_id"]: r for r in self.rows}

    def test_groups_and_status(self):
        b = self.by
        self.assertEqual(b["v100"][tc.G1], "○")
        self.assertEqual(b["v100"][f"{tc.G1} 분석"], "분석 #1")
        self.assertEqual(b["v101"][f"{tc.G1} 분석"], "자료 안 받음")
        self.assertEqual(b["v102"][f"{tc.G2} 분석"], "분석 V1")
        self.assertEqual(b["v102"][f"{tc.G3} 분석"], "분석 T1")
        self.assertEqual(b["v102"]["탐색 추천 까닭"], "조회수 상위")
        self.assertEqual(b["v103"][tc.G1] + b["v103"][tc.G2] + b["v103"][tc.G3], "")    # 뺄 까닭 → 어느 묶음에도 안 듦
        self.assertEqual(b["v103"]["뺀 까닭"], "주제 밖")
        self.assertEqual(b["v104"]["어디서 봄"], "채널 평소 영상")
        self.assertEqual(b["v104"][tc.G1], "○")
        self.assertEqual(b["v105"]["어디서 봄"], "기간 없는 검색")
        self.assertEqual((b["v105"][tc.G2], b["v105"][tc.G3]), ("", "○"))              # 옛 영상은 ② 모집단(최근) 밖, ③ 에만
        self.assertEqual(b["v105"][f"{tc.G3} 분석"], "자료 안 받음")
        s = self.summary[tc.LONG]
        self.assertEqual(s[f"{tc.G1}_pass"], 3)
        self.assertEqual(s["g1_uploads"], 1)
        self.assertEqual((s["alltime"], s["pending_alltime"], s["oldest3"]), (1, 3, 2500))
        self.assertIsNone(self.summary[tc.SHORT])

    def test_fetch_day(self):
        self.assertEqual(self.by["v102"]["받은 날"], (NOW - timedelta(days=5)).date().isoformat())
        self.assertEqual(self.by["v100"]["받은 날"], "")

    def test_checks_and_overlap(self):
        checks = tc.check_rows(self.summary, RULES)
        self.assertEqual(len(checks), 6)
        v = {(c["분석 대상"], c["형식"]): c["판정"] for c in checks}
        self.assertEqual(v[(tc.G1, tc.LONG)], "✅ 들어감 (구독자당 하루 조회수)")
        self.assertEqual(v[(tc.G2, tc.LONG)], "✅ 들어감")
        self.assertEqual(v[(tc.G3, tc.LONG)], "⚠️ 들어감 · 기간 없는 검색 일부만")         # 기간 없는 검색 3개 남음
        self.assertEqual(v[(tc.G1, tc.SHORT)], "❌ 자료 없음")
        ov = tc.overlap_rows(self.rows)
        self.assertEqual(sum(o["영상 수"] for o in ov), sum(1 for r in self.rows if r[tc.G1] or r[tc.G2] or r[tc.G3]))


class Xlsx(unittest.TestCase):
    def test_write(self):
        import openpyxl
        tmp = Path(tempfile.mkdtemp())
        try:
            p = tmp / "t.xlsx"
            tc.write_xlsx(p, [("확인 결과", [{"분석 대상": tc.G1, "기준 통과 (모집단·자료 안)": 1234}]),
                              ("전체 목록", [{"제목": "t", "링크": "https://www.youtube.com/watch?v=a", "배수(조회수÷구독자)": 3.5, "구독자당 하루 조회수": 0.012}])], ["안내"])
            wb = openpyxl.load_workbook(p)
            self.assertEqual(wb.sheetnames, ["안내", "확인 결과", "전체 목록"])
            self.assertEqual(wb["확인 결과"]["B2"].number_format, "#,##0")
            ws = wb["전체 목록"]
            self.assertEqual(ws["C2"].number_format, "0.00")
            self.assertEqual(ws["D2"].number_format, "0.000")
            self.assertEqual(ws["B2"].hyperlink.target, "https://www.youtube.com/watch?v=a")
        finally:
            shutil.rmtree(tmp)


if __name__ == "__main__":
    unittest.main()
