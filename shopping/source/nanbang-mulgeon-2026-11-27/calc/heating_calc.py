#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.2 — 2026-11-27 — ratios: 대본의 '몇 배' (히터÷매트 W · 3단계÷1단계 단가 · 탄소매트÷온수매트 순이득 · 가열식÷초음파 전기요금) — 계산 값 그대로.
# (v1.1 — 2026-11-27 — say(): 대본에 읽을 말 (100원 단위로 반올림 + "약" · 만 단위 한국어 — "1만 2,500원") · 결과에 say_* 칸. 계산 값은 그대로.
# (v1.0 — 2026-11-27 — 새로 (사용자 지시 2026-11-27 "… 생활 관련 주제 영상들 분석해서 그 영상들과 관련된 물건들을 고르고 그 물건들로 어떤 이득을
#   얻을 수 있는지에 대해 영상을 만드는게 좋을것 같아 한번해봐" · "요즘 생활 관련해서 유행하고 있는것도 찾아봐도 좋아").
#   겨울 난방 물건마다 '한 달 이득' = 보일러를 낮춰 아끼는 가스비 − 그 물건이 더 쓰는 전기요금. 대본의 숫자는 이 출력만 쓴다 (CLAUDE.md '숫자는 계산 코드 출력만').
#   출처(SOURCES)와 가정(ASSUME)을 나눈다 — 가정은 영상에서 '예를 들어'로만 말하고, 시청자가 자기 집 숫자로 바꿔 쓰게 공식을 같이 보여 준다.
#   ※ 연구·교육용 — 구매 권유가 아니다. 요금은 바뀔 수 있다 (한 번만 말함 — topic_guide 0번 5).
"""python3 calc/heating_calc.py [--json] [--selftest]"""
import argparse
import json
import logging
import sys
from datetime import datetime, timezone

VERSION = "v1.2"
LOG = logging.getLogger("heating_calc")

# ── 출처가 있는 값 ─────────────────────────────────────────────────────────────
SOURCES = {
    "elec_tiers": {
        "value": [(200, 910, 120.0), (400, 1600, 214.6), (None, 7300, 307.3)],   # (상한 kWh, 기본요금 원, 전력량요금 원/kWh) — 주택용 저압 · 기타계절(1~6월·9~12월)
        "src": "한전 주택용(저압) 전기요금표 2023-05-16 시행 — 2026년 기타계절 단가로 여러 계산 페이지가 같은 값 (glasswallet 2026 요금표 등). 기후환경요금·연료비조정요금·전력산업기반기금은 2026 값 확인 못 해 뺌 → 실제 고지서는 조금 더 나옴",
        "checked": "2026-11-27 검색 발췌 — ⚠️ 한전ON 원문 확인 필요",
    },
    "vat": {"value": 0.10, "src": "부가가치세 10%", "checked": "법정"},
    "per_degree_saving": {
        "value": 0.07,
        "src": "한국에너지공단 — 난방 온도를 1도 낮추면 에너지 소비량 약 7% 절감 (정책브리핑 korea.kr 보도)",
        "checked": "2026-11-27 검색 발췌 — ⚠️ 공단 원문 확인 필요",
    },
    "recommended_indoor": {"value": 20, "src": "겨울철 적정 실내 온도 20도 (기후에너지환경부·에너지공단 안내)", "checked": "검색 발췌"},
}

# ── 가정 (영상에서 '예를 들어' — 집마다 다름) ─────────────────────────────────
ASSUME = {
    "base_kwh": 300,          # 평소 한 달 전기 사용량 (난방 물건 없이) — 예시 집. 200 넘으면 2단계 단가가 붙음
    "gas_bill": 150000,       # 겨울 한 달 가스비 (난방·온수 합) — 예시 집
    "days": 30,
    # 물건 = (이름, 라벨 소비전력 W, 하루 사용 시간, 한 번 사는 값 아님 — 전기만). W 는 같은 종류 흔한 라벨 값 (제품마다 다름 — 라벨 확인)
    "items": [
        {"key": "draft", "name": "문풍지·뽁뽁이·방한커튼", "watt": 0, "hours": 0, "note": "전기를 안 씀 — 외풍을 막아 보일러를 낮출 수 있게 도움"},
        {"key": "carbon", "name": "탄소매트·전기요 (1인용 150W)", "watt": 150, "hours": 8, "note": "몸이 닿는 곳만 데움 · 라벨 최대치로 계산 (실제는 온도 맞으면 쉬어 더 적음)"},
        {"key": "water", "name": "온수매트 (300W)", "watt": 300, "hours": 8, "note": "물을 데워 돌림 — 같은 크기 전기요보다 W 가 큰 편"},
        {"key": "heater", "name": "전기히터·온풍기 (2,000W)", "watt": 2000, "hours": 4, "note": "공기를 데움 — 하루 4시간만 써도 전기를 가장 많이 씀"},
        {"key": "humid_us", "name": "초음파 가습기 (30W)", "watt": 30, "hours": 10, "note": "물을 떨어 날림 — 전기는 적게 · 매일 물 세척"},
        {"key": "humid_heat", "name": "가열식 가습기 (300W)", "watt": 300, "hours": 10, "note": "물을 끓여 날림 — 전기는 초음파의 10배쯤"},
    ],
    # 보일러를 몇 도 낮추나 — 물건마다 (⚖️ 가정: 몸을 데우는 매트·히터 = 2도, 외풍 막기 = 1도, 가습기 = 0도 — 가습기의 '따뜻하게 느끼는' 효과는 숫자 근거를 못 찾아 0)
    "lower_deg": {"draft": 1, "carbon": 2, "water": 2, "heater": 2, "humid_us": 0, "humid_heat": 0},
}


def elec_bill(kwh, tiers=None, vat=None):
    """주택용 누진 전기요금 (기본요금 + 전력량요금 + 부가세 10%). 기본요금은 마지막 구간 값 하나."""
    tiers = tiers or SOURCES["elec_tiers"]["value"]
    vat = SOURCES["vat"]["value"] if vat is None else vat
    left, prev_cap, energy, base = kwh, 0, 0.0, tiers[0][1]
    for cap, b, rate in tiers:
        span = (cap - prev_cap) if cap is not None else left
        use = min(left, span)
        if use > 0 or kwh == 0:
            base = b
        energy += max(use, 0) * rate
        left -= use
        prev_cap = cap if cap is not None else prev_cap
        if left <= 0:
            break
    return round((base + energy) * (1 + vat))


def say(won, approx=None):
    """대본용 말 — 100원 단위 반올림 (바뀌면 '약'), 만 단위: 12502 → '약 1만 2,500원' · 10500 → '1만 500원' · 77200 → '7만 7,200원'."""
    sign = "-" if won < 0 else ""
    w = abs(int(won))
    r = int(round(w / 100.0)) * 100
    pre = "약 " if (approx if approx is not None else r != w) else ""
    man, rest = divmod(r, 10000)
    if man and rest:
        txt = f"{man}만 {rest:,}원"
    elif man:
        txt = f"{man}만 원"
    else:
        txt = f"{rest:,}원"
    return sign + pre + txt


def item_rows(assume=None):
    a = assume or ASSUME
    base_bill = elec_bill(a["base_kwh"])
    rows = []
    for it in a["items"]:
        kwh = it["watt"] * it["hours"] * a["days"] / 1000
        extra = elec_bill(a["base_kwh"] + kwh) - base_bill
        deg = a["lower_deg"].get(it["key"], 0)
        gas_save = round(a["gas_bill"] * SOURCES["per_degree_saving"]["value"] * deg)
        rows.append({**it, "kwh": round(kwh, 1), "elec_extra": extra, "lower_deg": deg, "gas_save": gas_save, "net": gas_save - extra,
                     "total_kwh": a["base_kwh"] + kwh, "say_extra": say(extra), "say_gas": say(gas_save), "say_net": say(gas_save - extra)})
    return base_bill, rows


def ratios(rows):
    r = {x["key"]: x for x in rows}
    t = SOURCES["elec_tiers"]["value"]
    return {"heater_vs_carbon_watt": round(r["heater"]["watt"] / r["carbon"]["watt"], 1),
            "tier3_vs_tier1_rate": round(t[2][2] / t[0][2], 2),
            "carbon_vs_water_net": round(r["carbon"]["net"] / r["water"]["net"], 1),
            "heat_vs_us_humid_elec": round(r["humid_heat"]["elec_extra"] / r["humid_us"]["elec_extra"], 1)}


def tier_of(kwh):
    return 1 if kwh <= 200 else 2 if kwh <= 400 else 3


def log(stage, **kv):
    LOG.info("[%s] [%s] %s", stage, datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S"),
             " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) and ' ' in v else v}" for k, v in kv.items()))


def selftest():
    # 손 계산: 300kWh = 기본 1,600 + 200×120 + 100×214.6 = 1,600 + 24,000 + 21,460 = 47,060 × 1.1 = 51,766
    assert elec_bill(300) == 51766, elec_bill(300)
    # 540kWh = 7,300 + 24,000 + 200×214.6(42,920) + 140×307.3(43,022) = 117,242 × 1.1 = 128,966
    assert elec_bill(540) == 128966, elec_bill(540)
    assert elec_bill(0) == round(910 * 1.1)
    base, rows = item_rows()
    r = {x["key"]: x for x in rows}
    assert r["draft"]["elec_extra"] == 0 and r["draft"]["gas_save"] == 10500
    assert r["heater"]["kwh"] == 240 and tier_of(r["heater"]["total_kwh"]) == 3, "히터 4시간이면 3단계로 넘어감"
    assert r["heater"]["net"] < 0 < r["carbon"]["net"], (r["heater"]["net"], r["carbon"]["net"])
    assert say(12502) == "약 1만 2,500원" and say(10500) == "1만 500원" and say(77200) == "7만 7,200원" and say(-56200) == "-5만 6,200원" and say(8498) == "약 8,500원", (say(12502), say(8498))
    rt = ratios(rows)
    assert rt["heater_vs_carbon_watt"] == 13.3 and rt["tier3_vs_tier1_rate"] == 2.56 and rt["carbon_vs_water_net"] == 3.1 and rt["heat_vs_us_humid_elec"] == 10.0, rt
    print("[SELFTEST] ok — 300kWh 51,766원 · 540kWh 128,966원 · 히터 순이득", r["heater"]["net"], "· 탄소매트", r["carbon"]["net"])


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    if a.selftest:
        selftest()
        return 0
    log("INPUT", tool=f"heating_calc.py {VERSION}", base_kwh=ASSUME["base_kwh"], gas_bill=ASSUME["gas_bill"], per_degree=SOURCES["per_degree_saving"]["value"],
        tiers="120.0/214.6/307.3 (200·400kWh)")
    base, rows = item_rows()
    log("BASE", base_bill=base, tier=tier_of(ASSUME["base_kwh"]))
    for x in rows:
        log("ITEM", key=x["key"], say_extra=x["say_extra"], say_net=x["say_net"], kwh=x["kwh"], elec_extra=x["elec_extra"], lower_deg=x["lower_deg"], gas_save=x["gas_save"], net=x["net"], tier_after=tier_of(x["total_kwh"]))
    out = {"version": VERSION, "sources": {k: {kk: (vv if kk != "value" else str(vv)) for kk, vv in v.items()} for k, v in SOURCES.items()},
           "assume": {k: v for k, v in ASSUME.items() if k != "items"}, "base_bill": base, "rows": rows,
           "one_degree": round(ASSUME["gas_bill"] * SOURCES["per_degree_saving"]["value"]),
           "say_one_degree": say(round(ASSUME["gas_bill"] * SOURCES["per_degree_saving"]["value"])), "say_base_bill": say(base),
           "say_heater_bill_after": say(elec_bill(ASSUME["base_kwh"] + 240)),
           "ratios": ratios(rows)}
    if a.json:
        print(json.dumps(out, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
