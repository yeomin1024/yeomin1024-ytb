#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0.0 — 2026-11-23 — incident_cases.py v1.1.0 단위 시험 (작은 표본 — 할당량·네트워크 없음)
"""실행: python3 psychology/source/test_incident_cases.py   (또는 python3 -m pytest psychology/source/test_incident_cases.py)"""
from __future__ import annotations

import sys
import tempfile
from datetime import timedelta
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import incident_cases as ic  # noqa: E402

RULES = {"MIN_AGE_DAYS": 7, "MAX_AGE_DAYS": 180, "MAX_SUBS": 50000, "MIN_VPD_SUBS": 0.1, "MIN_VIEWS": 50000,
         "MIN_MINUTES": 4.0}


def _row(vid, title, views, subs, days_ago, sec=600, live=False, source="search", channel_id=None):
    return {"video_id": vid, "title": title, "channel_id": channel_id or f"C_{vid}", "channel": f"ch_{vid}",
            "published": (ic.AS_OF - timedelta(days=days_ago)).strftime("%Y-%m-%dT%H:%M:%SZ"), "description": "",
            "tags": "", "views": views, "likes": None if views is None else views // 100, "comments": 10, "duration_sec": sec, "live": live,
            "subs": subs, "source": source, "query": "", "window": ""}


def test_case_words():
    hit = ["밀그램 복종 실험", "강서 고문 살인사건의 진실", "방관자 효과란 무엇인가", "스톡홀름 증후군", "인지부조화 사례"]
    miss = ["의자 집어넣는 사람들의 심리", "자존감 높이는 방법", "생각이 많을수록 손해보는 이유"]
    for t in hit:
        assert ic.CASE_WORDS.search(t), t
    for t in miss:
        assert not ic.CASE_WORDS.search(t), t


def test_validate_drops_and_merges():
    df = pd.DataFrame([
        _row("a", "실험 A", 1000, 10, 30),
        _row("a", "실험 A", 900, 10, 30, source="psy_cache"),      # 같은 영상 두 출처 → 하나 (검색 쪽 통계)
        _row("b", "English only", 1000, 10, 30),                   # 한글 없음
        _row("c", "라이브 실험", 1000, 10, 30, live=True),          # 라이브
        _row("d", "짧은 실험", 1000, 10, 30, sec=100),               # 4분 미만
        _row("e", "통계 없는 실험", None, 10, 30),                   # 조회수 없음
    ])
    out = ic.validate(df)
    assert list(out["video_id"]) == ["a"]
    assert out.iloc[0]["views"] == 1000 and out.iloc[0]["source"] == "psy_cache|search"


def test_features_ratio_floor_and_success():
    df = pd.DataFrame([
        _row("s", "성공 사건", 200_000, 20_000, 60),        # 하루 3,333 ÷ 2만 = 0.167 ≥ 0.1 · 5만 이상 → 성공
        _row("t", "조회수 모자람 사건", 40_000, 1_000, 60),   # 5만 미만 → 아님
        _row("u", "오래된 사건", 900_000, 20_000, 400),       # 180일 넘음 → 아님
        _row("v", "큰 채널 사건", 2_000_000, 1_500_000, 30),  # 구독자 5만 넘음 → 아님
        _row("w", "구독자 0 실험", 5_000, 0, 30),             # 배수는 100 으로 나눔
    ])
    d = ic.features(ic.validate(df), RULES).set_index("video_id")
    assert bool(d.loc["s", "success"]) and not d.loc[["t", "u", "v"], "success"].any()
    assert d.loc["w", "ratio"] == 50.0                       # 5,000 ÷ max(0,100)
    assert d.loc["v", "size"] == "큰 채널(≥100만)" and d.loc["s", "size"] == "작은 채널(≤5만)"


def test_labels_and_groups():
    df = pd.DataFrame([
        _row("x1", "가스라이팅 사건 1", 100_000, 10_000, 30, channel_id="C1"),
        _row("x2", "가스라이팅 사건 2", 50_000, 10_000, 30, channel_id="C1"),
        _row("x3", "실험 3", 10_000, 2_000_000, 30, channel_id="C2"),
        _row("x4", "사건 4 (판정 안 함)", 10_000, 2_000, 30, channel_id="C3"),
    ])
    with tempfile.TemporaryDirectory() as tmp:
        p = Path(tmp) / "labels.tsv"
        p.write_text("# 주석 줄\nvideo_id\tkeep\tkind\tcase\tconcept\tnote\n"
                     "x1\t1\tcrime\tA 사건\t가스라이팅·지배|세뇌·그루밍\t\n"
                     "x2\t1\tcrime\tA 사건\t가스라이팅·지배\t\n"
                     "x3\t0\t\t\t\t일반론\n", encoding="utf-8")
        lab = ic.read_labels(p)
    d = ic.features(ic.classify(ic.validate(df), lab), RULES)
    assert int(d["is_case"].sum()) == 2 and int((d["candidate"] & ~d["labeled"]).sum()) == 1
    ce = ic.concept_rows(d[d["is_case"]])
    assert sorted(ce["concept_one"]) == ["가스라이팅·지배", "가스라이팅·지배", "세뇌·그루밍"]
    g = ic.group_table(ce, "concept_one").set_index("concept_one")
    assert g.loc["가스라이팅·지배", "videos"] == 2 and g.loc["가스라이팅·지배", "views_sum"] == 150_000
    assert g.loc["가스라이팅·지배", "views_median_cap"] == 75_000
    assert np.isclose(g.loc["가스라이팅·지배", "ratio_median"], 7.5)   # (10 + 5) ÷ 2


def test_slim_keeps_needed_fields():
    raw = {"items": [{"id": "v1", "snippet": {"title": "t", "channelId": "c", "channelTitle": "ch", "publishedAt": "2026",
                                              "description": "x" * 999, "tags": list("abcdefghijklmnopqrstuvwxyz1234567"),
                                              "thumbnails": {"big": 1}, "liveBroadcastContent": "none"},
                      "statistics": {"viewCount": "5"}, "contentDetails": {"duration": "PT5M", "definition": "hd"}}]}
    s = ic.slim("videos", raw)["items"][0]
    assert "thumbnails" not in s["snippet"] and len(s["snippet"]["description"]) == 300 and len(s["snippet"]["tags"]) == 30
    assert s["contentDetails"] == {"duration": "PT5M"} and s["statistics"]["viewCount"] == "5"
    assert ic.iso_duration_sec("PT1H2M3S") == 3723


if __name__ == "__main__":
    ic.setup_logging()
    import logging
    ic.log.setLevel(logging.WARNING)
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for t in tests:
        t()
        print(f"[TEST] ok {t.__name__}")
    print(f"[TEST] passed={len(tests)}")
