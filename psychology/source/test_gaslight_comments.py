#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0.0 — 2026-11-23 — gaslight_comments.py v1.0.0 단위 시험 (작은 표본)
"""실행: python3 psychology/source/test_gaslight_comments.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import gaslight_comments as gc  # noqa: E402


def test_words():
    assert gc.GAS.search("엄마한테 가스 라이팅 당했어요") and not gc.GAS.search("가스레인지 불")
    assert gc.REALIZE.search("그땐 몰랐는데 그게 가스라이팅이었네요") and not gc.REALIZE.search("가스라이팅 하는 사람 특징")
    assert gc.START_KIND.search("처음엔 세상 상냥하고 잘해주다가 점점") and not gc.START_KIND.search("처음 봤을 때 무서웠다")


def test_relation_order_and_tactics():
    assert gc.relation_of("시어머니가 효도를 강요") == ["시댁"]          # '어머니'가 들어가도 시댁만
    assert gc.relation_of("남편이 친구를 못 만나게") == ["배우자", "친구·지인"]
    assert gc.relation_of("형광등 아래서") == []                         # '형' 한 글자로는 안 잡힘
    rows = [{"vid": "v", "id": "1", "likes": 3, "is_reply": False, "creator": False, "published": "",
             "text": "엄마가 늘 죄책감을 심었는데 이제야 가스라이팅인 줄 알았어요"},
            {"vid": "v", "id": "2", "likes": 0, "is_reply": False, "creator": False, "published": "", "text": "좋은 영상"}]
    g = gc.features(rows)
    assert len(g) == 1 and g[0]["realize"] and g[0]["rel"] == ["부모"] and g[0]["tactics"] == ["죄책감"]


def test_validate_and_clean():
    rows = [{"vid": "v", "id": "1", "text": "a", "creator": False}, {"vid": "v", "id": "1", "text": "a", "creator": False},
            {"vid": "v", "id": "2", "text": " ", "creator": False}, {"vid": "v", "id": "3", "text": "b", "creator": True}]
    assert [r["id"] for r in gc.validate(rows)] == ["1"]
    assert gc.clean("@user-ab12 저도요|정말\n그래요") == "@… 저도요／정말 그래요"


if __name__ == "__main__":
    import logging
    gc.log.addHandler(logging.NullHandler())
    gc.log.setLevel(logging.WARNING)
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for t in tests:
        t()
        print(f"[TEST] ok {t.__name__}")
    print(f"[TEST] passed={len(tests)}")
