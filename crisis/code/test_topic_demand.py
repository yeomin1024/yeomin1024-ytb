# VERSION: v1.0.0 — 2026-11-23 — topic_demand 분류·성공 판정·채널 자르기 단위 테스트 (topic_demand v1.1.0 기준)
"""python3 -m unittest crisis/code/test_topic_demand.py  (네트워크 불필요)"""
import re
import sys
import unittest
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import topic_demand as td  # noqa: E402


def frame(rows):
    df = pd.DataFrame(rows)
    for c, v in {"tags": "", "description": "", "channel_id": "c1", "subs": 1000.0, "views": 100_000.0,
                 "duration_sec": 60.0, "age_days": 30.0, "published": pd.Timestamp("2026-10-24", tz="UTC")}.items():
        if c not in df:
            df[c] = v
    return df


class TestTopicDemand(unittest.TestCase):
    def test_on_topic_excludes_variety_show(self):
        df = frame([{"topic": "winter_run", "title": "하하가 런닝맨에서 웃은 장면"},
                    {"topic": "winter_run", "title": "겨울 러닝 심정지 주의"},
                    {"topic": "camping_co", "title": "잠자던 노부부 일산화탄소 중독"}])   # 캠핑 낱말 없음 → 주제 밖
        out = td.on_topic(df)
        self.assertEqual(out["title"].tolist(), ["겨울 러닝 심정지 주의"])

    def test_safety_regex_no_false_positive(self):
        self.assertIsNone(re.search(td.SAFETY, "우후죽순 도심 마라톤에 쓴소리"))
        self.assertIsNone(re.search(td.SAFETY, "이 가격 실화냐 러닝화"))
        self.assertIsNotNone(re.search(td.SAFETY, "러닝 중 쓰러진 여성 심정지"))

    def test_focus_camping_is_co_only(self):
        f = td.TOPICS["camping_co"]["focus"]
        self.assertIsNone(re.search(f, "동계 캠핑 화목난로 후기"))
        self.assertIsNotNone(re.search(f, "차박 중 일산화탄소 경보기 울림"))

    def test_success_rules(self):
        df = frame([
            {"title": "쇼츠 성공", "duration_sec": 50, "subs": 10_000, "views": 60_000, "age_days": 30},    # ×6 · 5만+
            {"title": "쇼츠 5만 미만", "duration_sec": 50, "subs": 1_000, "views": 40_000, "age_days": 30},
            {"title": "롱폼 성공", "duration_sec": 600, "subs": 2_000, "views": 12_000, "age_days": 30},     # ×6 · 1만+
            {"title": "롱폼 4분 미만", "duration_sec": 200, "subs": 2_000, "views": 50_000, "age_days": 30},
            {"title": "큰 채널", "duration_sec": 600, "subs": 60_000, "views": 900_000, "age_days": 30},
            {"title": "지난 겨울 롱폼", "duration_sec": 600, "subs": 2_000, "views": 12_000, "age_days": 300},
            {"title": "구독자 숨김", "duration_sec": 600, "subs": None, "views": 900_000, "age_days": 30},
        ])
        self.assertEqual(df.loc[td.success_mask(df, 180), "title"].tolist(), ["쇼츠 성공", "롱폼 성공"])
        self.assertEqual(df.loc[td.success_mask(df, 365), "title"].tolist(), ["쇼츠 성공", "롱폼 성공", "지난 겨울 롱폼"])

    def test_cap_channel(self):
        df = frame([{"title": str(i), "channel_id": "big", "views": float(i)} for i in range(10)]
                   + [{"title": "solo", "channel_id": "small", "views": 5.0}])
        out = td.cap_channel(df, 3)
        self.assertEqual(sorted(out.loc[out["channel_id"] == "big", "views"].tolist()), [7.0, 8.0, 9.0])
        self.assertEqual(len(out), 4)


if __name__ == "__main__":
    unittest.main()
