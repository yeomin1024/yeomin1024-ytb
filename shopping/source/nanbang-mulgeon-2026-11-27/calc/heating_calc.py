#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.9 — 2026-11-27 — 쇼츠 반론 2회차: net_generous = 히터 전기요금 − 넉넉히 친 가스비 (1만 7,200원 — 아낀 가스비를 빼도 더 내는 돈). 다른 값 그대로.
# (v1.8 — 2026-11-27 — 쇼츠 반론 1회차: generous_4h = 히터 켜는 4시간에 한 달 난방비의 절반을 쓴다고 넉넉히 칠 때 보일러를 꺼서 아끼는 최대 (6만 원 — 고르게 쓴다는 가정 없이도 히터 손해가 남는지) · say_base_man (평소 전기요금 약 5만 원). 다른 값 그대로.
# (v1.7 — 2026-11-27 — 쇼츠 대본용 ratios.heater_vs_carbon_elec (히터 ÷ 탄소매트 한 달 전기요금 = 9.1 — '아홉 배 넘게'). 다른 값 그대로.
# (v1.6 — 2026-11-27 — 반론 4회차(K4): 반만 켠 히터 전기요금을 '4시간 보일러를 꺼서' 메우려면 난방비가 한 달 얼마인 집이어야 하나 (heater_half_breakeven_heating_gas) · 어림 200와트 × 5시간 = 700원 열 번 (rule_x10). 다른 값 그대로.
# (v1.5 — 2026-11-27 — 반론 3회차(K3): 매트 값 예(5만 원) ÷ 한 겨울 남는 돈 = 본전까지 겨울 수 · 어림 700원 × 12 (약 8,400원). 다른 값 그대로.
# (v1.4 — 2026-11-27 — 반론 2회차(K2) 반영: ① max_if_off = 그 시간 동안 보일러를 아예 꺼도 아끼는 난방 가스비 (55·26도 같은 뜻 없는 숫자 대신 — 히터 4시간 2만 원) · ② 탄소매트 4도 낮춤일 때 한 달·한 겨울(넉 달) 남는 돈 · ③ 400 넘을 때 기본요금 오름 (부가세 넣음) · ④ winter_months = 4. 다른 값 그대로.
# (v1.3 — 2026-11-27 — 반론 1회차(K1) 반영 — 계산 틀을 바꿈:
#   ① 매트·히터는 '하루 종일 2도 낮춤'(가정) 대신 **쓰는 시간 동안 보일러를 몇 도 낮춰야 본전인가**(본전 도수) — 쓰는 시간과 아끼는 시간을 맞춤 (상 K3 줄 41)
#   ② 7% 는 가스비 전체가 아니라 **난방에 쓴 가스비**에만 (온수·요리·기본요금 뺌 — 중 K4 줄 88) → 예시 집 = '난방에 한 달 12만 원'
#   ③ 물건 값은 계산에 없음을 밝히고 본전 달 수 공식 (상 K4 줄 44) · ④ 히터도 '반만 켜질 때' 한 줄 (중 K7 줄 60)
#   ⑤ 부가세 넣은 1킬로와트시당 값 132 · 236 · 338원 + 어림 '100와트를 하루 1시간, 한 달 = 약 700원' (중 K5 줄 89 · 이탈 E1 줄 82)
#   ⑥ 3단계 단가는 2단계와 견줌 (하 — 줄 57) · 외풍 막기도 같은 틀(하루 종일 1도면 얼마)로.
# (v1.2 — ratios) (v1.1 — say()) (v1.0 — 2026-11-27 — 새로 (사용자 지시 "… 그 물건들로 어떤 이득을 얻을 수 있는지에 대해 영상을 만드는게 좋을것 같아 한번해봐"))
#   대본의 숫자는 이 출력만 쓴다 (CLAUDE.md '숫자는 계산 코드 출력만'). 출처(SOURCES)와 가정(ASSUME)을 나눔 — 가정은 대본에서 '예를 들어'로만.
#   ※ 연구·교육용 — 구매 권유가 아니다. 요금은 바뀔 수 있다.
"""python3 calc/heating_calc.py [--json] [--selftest]"""
import argparse
import json
import logging
import sys
from datetime import datetime, timezone

VERSION = "v1.9"
LOG = logging.getLogger("heating_calc")

SOURCES = {
    "elec_tiers": {
        "value": [(200, 910, 120.0), (400, 1600, 214.6), (None, 7300, 307.3)],   # (상한 kWh, 기본요금, 원/kWh) — 주택용 저압 · 기타계절(1~6월·9~12월)
        "src": "한전 주택용(저압) 요금표 2023-05-16 시행 — 2026 기타계절 값으로 여러 계산 페이지가 같음. 기후환경요금·연료비조정요금·전력산업기반기금은 2026 값 확인 못 해 뺌 → 고지서는 조금 더 나옴",
        "checked": "2026-11-27 검색 발췌 — ⚠️ 한전ON 원문 확인 필요",
    },
    "vat": {"value": 0.10, "src": "부가가치세 10%", "checked": "법정"},
    "per_degree_saving": {"value": 0.07, "src": "한국에너지공단 — 난방 온도 1도 낮추면 에너지 소비 약 7% 절감 (정책브리핑 보도)", "checked": "검색 발췌 — ⚠️ 원문"},
}

ASSUME = {
    "base_kwh": 300,          # 평소 한 달 전기 (예시 집 — 2단계에 있음)
    "heating_gas": 120000,    # v1.3: 난방에 쓴 가스비 한 달 (온수·요리·기본요금 뺌 — 예시 집)
    "days": 30,
    "hours_day": 24,
    "items": [
        {"key": "carbon", "name": "탄소매트·전기요 (1인용 150W)", "watt": 150, "hours": 8},
        {"key": "water", "name": "온수매트 (300W)", "watt": 300, "hours": 8},
        {"key": "heater", "name": "전기히터·온풍기 (2,000W)", "watt": 2000, "hours": 4},
        {"key": "heater_half", "name": "전기히터 반만 켜질 때 (평균 1,000W)", "watt": 1000, "hours": 4},
        {"key": "humid_us", "name": "초음파식 가습기 (30W)", "watt": 30, "hours": 10},
        {"key": "humid_heat", "name": "가열식 가습기 (300W)", "watt": 300, "hours": 10},
    ],
    "draft_deg": 1,                 # 외풍 막기 — 하루 종일 1도 낮출 수 있다면 (조건)
    "draft_price_example": 10000,   # 본전 달 수 예 — '1만 원어치 문풍지' (예시 값 — 실제 값은 링크에서)
    "rule_watt": 100,               # 어림: 100와트를 하루 1시간, 한 달
    "mat_example_deg": 4,           # v1.4: 탄소매트로 잠잘 때 4도를 낮춘다면 (예)
    "winter_months": 4,             # v1.4: 한 겨울 = 넉 달 (12~3월 — 예)
    "mat_price_example": 50000,     # v1.5: 탄소매트 값 예 (실제 값은 링크에서 — 대본 '5만 원짜리라면')
}


def elec_bill(kwh, tiers=None, vat=None):
    """주택용 누진 전기요금 (기본요금 + 전력량요금 + 부가세 10%)."""
    tiers = tiers or SOURCES["elec_tiers"]["value"]
    vat = SOURCES["vat"]["value"] if vat is None else vat
    left, prev_cap, energy, base = kwh, 0, 0.0, tiers[0][1]
    for cap, b, rate in tiers:
        span = (cap - prev_cap) if cap is not None else left
        use = min(left, span)
        if use > 0:
            base = b
        energy += max(use, 0) * rate
        left -= use
        prev_cap = cap if cap is not None else prev_cap
        if left <= 0:
            break
    return round((base + energy) * (1 + vat))


def say(won, approx=None):
    """대본용 말 — 100원 단위 반올림 (바뀌면 '약'), 만 단위."""
    sign = "-" if won < 0 else ""
    w = abs(int(round(won)))
    r = int(round(w / 100.0)) * 100
    pre = "약 " if (approx if approx is not None else r != w) else ""
    man, rest = divmod(r, 10000)
    txt = f"{man}만 {rest:,}원" if man and rest else (f"{man}만 원" if man else f"{rest:,}원")
    return sign + pre + txt


def say_man(won):
    """v1.6: 만 원 단위 반올림 — 큰 어림값용 (219,822 → '약 22만 원')."""
    return f"약 {int(round(won / 10000.0))}만 원"


def tier_of(kwh):
    return 1 if kwh <= 200 else 2 if kwh <= 400 else 3


def per_degree_for_hours(hours, a=None):
    """보일러를 '그 시간 동안만' 1도 낮출 때 한 달 아끼는 난방 가스비 (⚖️ 가정: 아끼는 양이 낮춘 시간에 비례)."""
    a = a or ASSUME
    return a["heating_gas"] * SOURCES["per_degree_saving"]["value"] * hours / a["hours_day"]


def compute(a=None):
    a = a or ASSUME
    base_bill = elec_bill(a["base_kwh"])
    rows = []
    for it in a["items"]:
        kwh = it["watt"] * it["hours"] * a["days"] / 1000
        extra = elec_bill(a["base_kwh"] + kwh) - base_bill
        pdeg = per_degree_for_hours(it["hours"], a)
        be = extra / pdeg if pdeg else None
        rows.append({**it, "kwh": round(kwh, 1), "total_kwh": a["base_kwh"] + kwh, "tier_after": tier_of(a["base_kwh"] + kwh),
                     "elec_extra": extra, "say_extra": say(extra), "per_degree_hours": round(pdeg), "say_per_degree_hours": say(pdeg),
                     "breakeven_deg": round(be, 1) if be else None,
                     "max_if_off": round(a["heating_gas"] * it["hours"] / a["hours_day"]), "say_max_if_off": say(a["heating_gas"] * it["hours"] / a["hours_day"])})
    vat = 1 + SOURCES["vat"]["value"]
    t = SOURCES["elec_tiers"]["value"]
    one_deg_all_day = per_degree_for_hours(24, a)
    draft_save = one_deg_all_day * a["draft_deg"]
    rule_kwh = a["rule_watt"] * 1 * a["days"] / 1000
    out = {
        "base_bill": base_bill, "say_base_bill": say(base_bill),
        "one_degree_all_day": round(one_deg_all_day), "say_one_degree_all_day": say(one_deg_all_day),
        "draft_save": round(draft_save), "say_draft_save": say(draft_save),
        "draft_payback_months": round(a["draft_price_example"] / draft_save, 1),
        "rate_vat": {"tier1": round(t[0][2] * vat), "tier2": round(t[1][2] * vat), "tier3": round(t[2][2] * vat)},
        "tier3_vs_tier2_rate": round(t[2][2] / t[1][2], 2),
        "rule_of_thumb": {"kwh": rule_kwh, "won_tier2": round(rule_kwh * t[1][2] * vat), "say": say(rule_kwh * t[1][2] * vat)},
        "rows": rows,
    }
    r = {x["key"]: x for x in rows}
    mat_net = r["carbon"]["per_degree_hours"] * a["mat_example_deg"] - r["carbon"]["elec_extra"]
    out["carbon_example"] = {"deg": a["mat_example_deg"], "net_month": mat_net, "say_net_month": say(mat_net),
                             "net_winter": mat_net * a["winter_months"], "say_net_winter": say(mat_net * a["winter_months"])}
    out["carbon_example"]["price"] = a["mat_price_example"]
    out["carbon_example"]["payback_winters"] = round(a["mat_price_example"] / (mat_net * a["winter_months"]), 1)
    out["rule_x12"] = {"won": 700 * 12, "say": say(700 * 12, approx=True)}   # 대본 어림 '약 700원'이 열두 번 (150와트 × 8시간)
    out["heater_half_breakeven_heating_gas"] = round(r["heater_half"]["elec_extra"] * a["hours_day"] / r["heater_half"]["hours"])
    out["say_heater_half_breakeven_heating_gas"] = say_man(out["heater_half_breakeven_heating_gas"])
    out["rule_x10"] = {"watt": 200, "hours": 5, "times": 200 / a["rule_watt"] * 5, "won": 700 * 10, "say": say(700 * 10, approx=True)}   # 대본 어림 예
    out["generous_4h"] = round(a["heating_gas"] * 0.5)
    out["say_generous_4h"] = say(out["generous_4h"])
    out["say_base_man"] = say_man(base_bill)
    out["net_generous"] = r["heater"]["elec_extra"] - out["generous_4h"]
    out["say_net_generous"] = say(out["net_generous"])
    out["base_jump_3"] = round((t[2][1] - t[1][1]) * vat)
    out["say_base_jump_3"] = say((t[2][1] - t[1][1]) * vat)
    out["ratios"] = {"heater_vs_carbon_watt": round(r["heater"]["watt"] / r["carbon"]["watt"], 1),
                     "water_vs_carbon_breakeven": round(r["water"]["breakeven_deg"] / r["carbon"]["breakeven_deg"], 1),
                     "heat_vs_us_humid_elec": round(r["humid_heat"]["elec_extra"] / r["humid_us"]["elec_extra"], 1),
                     "heater_vs_carbon_elec": round(r["heater"]["elec_extra"] / r["carbon"]["elec_extra"], 1)}
    return out


def log(stage, **kv):
    LOG.info("[%s] [%s] %s", stage, datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S"),
             " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) and ' ' in v else v}" for k, v in kv.items()))


def selftest():
    assert elec_bill(300) == 51766 and elec_bill(540) == 128966, (elec_bill(300), elec_bill(540))
    o = compute()
    r = {x["key"]: x for x in o["rows"]}
    # 손 계산: 탄소매트 8시간 1도 = 120,000 × 0.07 × 8/24 = 2,800원 → 본전 = 8,498 / 2,800 = 3.0도
    assert r["carbon"]["per_degree_hours"] == 2800 and r["carbon"]["breakeven_deg"] == 3.0, r["carbon"]
    assert r["water"]["breakeven_deg"] == 6.1, r["water"]["breakeven_deg"]
    # 히터 4시간 1도 = 1,400원 → 77,200 / 1,400 = 55.1도 (불가능)
    assert r["heater"]["breakeven_deg"] == 55.1 and r["heater"]["tier_after"] == 3
    assert r["heater_half"]["kwh"] == 120 and r["heater_half"]["tier_after"] == 3, "반만 켜져도 420킬로와트시 — 400 넘음"
    assert o["one_degree_all_day"] == 8400 and o["draft_payback_months"] == 1.2
    assert o["rate_vat"] == {"tier1": 132, "tier2": 236, "tier3": 338}, o["rate_vat"]
    assert o["rule_of_thumb"]["won_tier2"] == 708 and o["rule_of_thumb"]["say"] == "약 700원"
    assert r["heater"]["max_if_off"] == 20000 and r["carbon"]["max_if_off"] == 40000
    assert r["heater"]["elec_extra"] > r["heater_half"]["elec_extra"] > r["heater"]["max_if_off"], "히터는 반만 켜져도 보일러를 끈 것보다 비쌈"
    assert o["carbon_example"]["net_month"] == 2702 and o["carbon_example"]["say_net_month"] == "약 2,700원"
    assert o["base_jump_3"] == 6270
    assert o["heater_half_breakeven_heating_gas"] == 219822 and o["say_heater_half_breakeven_heating_gas"] == "약 22만 원", o["say_heater_half_breakeven_heating_gas"]
    assert o["ratios"]["heater_vs_carbon_elec"] == 9.1
    assert o["generous_4h"] == 60000 and o["generous_4h"] < r["heater"]["elec_extra"], "넉넉히 쳐도 히터 전기요금이 더 큼"
    assert o["say_base_man"] == "약 5만 원"
    assert o["net_generous"] == 17200 and o["say_net_generous"] == "1만 7,200원"
    assert o["rule_x10"]["times"] == 10 and o["rule_x10"]["say"] == "약 7,000원"
    assert o["carbon_example"]["payback_winters"] == 4.6 and o["rule_x12"]["say"] == "약 8,400원", (o["carbon_example"], o["rule_x12"])
    # 검산: 히터 전기요금 = 2단계 100kWh + 3단계 140kWh + 기본요금 오름 (모두 부가세)
    assert round(100 * 214.6 * 1.1 + 140 * 307.3 * 1.1 + 6270) == 77200
    print("[SELFTEST] ok — 본전 도수 탄소매트", r["carbon"]["breakeven_deg"], "· 온수매트", r["water"]["breakeven_deg"], "· 히터", r["heater"]["breakeven_deg"],
          "· 반만", r["heater_half"]["breakeven_deg"], "· 1도 하루 종일", o["say_one_degree_all_day"])


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    if a.selftest:
        selftest()
        return 0
    log("INPUT", tool=f"heating_calc.py {VERSION}", base_kwh=ASSUME["base_kwh"], heating_gas=ASSUME["heating_gas"], per_degree=SOURCES["per_degree_saving"]["value"])
    o = compute()
    log("BASE", base_bill=o["base_bill"], one_degree_all_day=o["one_degree_all_day"], draft_payback_months=o["draft_payback_months"], rate_vat=o["rate_vat"],
        rule="100W×1h×30일=" + o["rule_of_thumb"]["say"])
    for x in o["rows"]:
        log("ITEM", key=x["key"], kwh=x["kwh"], tier_after=x["tier_after"], elec_extra=x["elec_extra"], per_degree_hours=x["per_degree_hours"], breakeven_deg=x["breakeven_deg"])
    o["version"] = VERSION
    o["sources"] = {k: {kk: (vv if kk != "value" else str(vv)) for kk, vv in v.items()} for k, v in SOURCES.items()}
    o["assume"] = {k: v for k, v in ASSUME.items() if k != "items"}
    if a.json:
        print(json.dumps(o, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
