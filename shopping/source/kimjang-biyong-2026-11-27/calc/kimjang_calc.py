#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.2 — 2026-11-27 — 반론 3회차: say.bought_minus_salted_floor = 만 원 아래 버림 + '넘게' (38만 7,890 → '38만 원 넘게' — 반올림한 77만·38만 5천으로 셈해도 맞음). 다른 값 그대로.
# (v1.1 — 2026-11-27 — 반론 2회차: say.bought_minus_salted_1k = 천 원 단위 (38만 7,890 → '약 38만 8천 원' — 38만 5천 원과 같은 단위). 다른 값 그대로.
# (v1.0 — 2026-11-27 — 새로 (사용자 지시 2026-11-27 "1번 김장으로 쇼츠 대본 만들어줘" — 후보 shopping/result/next_topic/winter_topics.md 1번).
#   4인 가족 김장 세 가지 길(직접 담그기 · 절임배추 · 사 먹기)의 값과 차이 — 쇼츠 대본의 숫자는 이 출력만 쓴다 (CLAUDE.md '숫자는 계산 코드 출력만').
#   출처 = 한국물가협회 2026-11-18 발표 (11월 10~12일 · 전국 6대 도시 전통시장·대형마트·온라인몰 · 김장 재료 15개 품목) — 뉴스1·파이낸셜뉴스 보도 (검색 발췌, ⚠️ 협회 원문 확인 필요).
#   기준량 = 포기김치 58.2kg · 깍두기 9.9kg · 총각김치 7.4kg (4인 가족). 직접 담그기 = 재료를 전통시장에서 산 값.
# ※ 연구·교육용 — 구매 권유가 아니다. 값은 해마다·지역마다 다르다.
"""python3 calc/kimjang_calc.py [--json] [--selftest]"""
import argparse
import json
import logging
import sys
from datetime import datetime, timezone

VERSION = "v1.2"
LOG = logging.getLogger("kimjang_calc")
SOURCE = {
    "org": "한국물가협회", "released": "2026-11-18", "surveyed": "2026-11-10~12", "where": "전국 6대 도시 전통시장·대형마트·온라인몰, 김장 재료 15개 품목",
    "basis": "4인 가족 — 포기김치 58.2kg · 깍두기 9.9kg · 총각김치 7.4kg",
    "links": ["https://www.news1.kr/economy/trend/6357827", "https://www.fnnews.com/news/202611160701209048"],
    "checked": "2026-11-27 검색 발췌 — ⚠️ 협회 원문 확인 필요",
}
COST = {"direct": 339670, "salted": 384730, "bought": 772620}           # 원 — 직접 담그기(전통시장 재료) · 절임배추 · 완제품
PER_HEAD = {"direct": 21230, "salted": 24050, "bought": 48290}          # 원 — 배추 한 포기당 (보도 값)


def say(won, unit=1000):
    """대본용 말: unit 단위 반올림 + '약' (바뀌면) — 339,670 → '약 34만 원' (unit 10000) · 45,060 → '약 4만 5천 원' (unit 1000)."""
    r = int(round(won / unit)) * unit
    pre = "약 " if r != won else ""
    man, rest = divmod(r, 10000)
    if rest == 0:
        return f"{pre}{man}만 원" if man else f"{pre}0원"
    if rest % 1000 == 0 and rest:
        return f"{pre}{man}만 {rest // 1000}천 원" if man else f"{pre}{rest // 1000}천 원"
    return f"{pre}{man}만 {rest:,}원" if man else f"{pre}{rest:,}원"


def compute():
    d, s, b = COST["direct"], COST["salted"], COST["bought"]
    heads = {k: round(COST[k] / PER_HEAD[k], 1) for k in COST}
    out = {
        "cost": COST, "per_head": PER_HEAD, "heads": heads,
        "salted_minus_direct": s - d, "salted_pct": round((s - d) / d * 100, 1),
        "bought_minus_direct": b - d, "bought_ratio": round(b / d, 2), "direct_share_of_bought": round(d / b, 2),
        "bought_minus_salted": b - s, "per_head_salted_minus_direct": PER_HEAD["salted"] - PER_HEAD["direct"],
    }
    out["say"] = {
        "bought": say(b, 10000), "direct": say(d, 10000), "salted": say(s, 5000),
        "salted_minus_direct": say(s - d, 1000), "bought_minus_salted": say(b - s, 10000),
        "per_head_diff": say(out["per_head_salted_minus_direct"], 100),
        "bought_minus_salted_1k": say(b - s, 1000),
        "bought_minus_salted_floor": f"{(b - s) // 10000}만 원 넘게",
    }
    return out


def log(stage, **kv):
    LOG.info("[%s] [%s] %s", stage, datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S"),
             " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) and ' ' in v else v}" for k, v in kv.items()))


def selftest():
    o = compute()
    assert o["salted_minus_direct"] == 45060 and o["salted_pct"] == 13.3, "보도: 절임배추 4만 5,060원(13.3%) 더"
    assert o["bought_minus_direct"] == 432950 and o["bought_ratio"] == 2.27, "보도: 완제품 43만 2,950원 더 · 2.27배"
    assert all(abs(v - 16) < 0.1 for v in o["heads"].values()), o["heads"]          # 세 값 모두 배추 16포기 기준으로 맞음
    assert o["direct_share_of_bought"] < 0.5, "직접 담그기 = 사 먹는 값의 절반도 안 됨"
    assert o["say"] == {"bought": "약 77만 원", "direct": "약 34만 원", "salted": "약 38만 5천 원", "salted_minus_direct": "약 4만 5천 원",
                        "bought_minus_salted": "약 39만 원", "per_head_diff": "약 2,800원", "bought_minus_salted_1k": "약 38만 8천 원", "bought_minus_salted_floor": "38만 원 넘게"}, o["say"]
    assert o["say"]["bought_minus_salted_floor"] == "38만 원 넘게" and 770000 - 385000 >= 380000, "반올림 값으로 셈해도 38만 원 넘음"
    print("[SELFTEST] ok — 포기 수", o["heads"], "· 절임 +", o["salted_minus_direct"], "· 사 먹기 ×", o["bought_ratio"])


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    if a.selftest:
        selftest()
        return 0
    o = compute()
    log("INPUT", tool=f"kimjang_calc.py {VERSION}", source=f"{SOURCE['org']} {SOURCE['released']}", basis=SOURCE["basis"])
    log("RESULT", **{k: v for k, v in o.items() if isinstance(v, (int, float))}, say=json.dumps(o["say"], ensure_ascii=False))
    if a.json:
        print(json.dumps({"version": VERSION, "source": SOURCE, **o}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
