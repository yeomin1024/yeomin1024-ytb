#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-10-16 — 대본 v1.2(141문장: 도입에서 결과 숫자를 뺌 — 사용자 지시 2026-10-16 "대본 내용도 처음에 결말을 말하지마")에 맞춰 문장 번호를 다시. 도입의 117·46·1.2%·25% 확인은 결과 파트 문장(38·44·50·52)으로 옮김.
# v1.0 — 2026-10-15 — 대본 숫자 ↔ 백테스트 결과 파일 대조 (stock/guides/concept.md 2번 "숫자는 코드 출력만").
#          사용자 지시 2026-10-15 "제목, 대본, 썸네일 프롬프트, 영상까지 다 만들어봐". 결과: ../checklist.md
"""대본 문장의 숫자가 results.json 과 맞는지 하나씩 확인한다. 하나라도 틀리면 종료 코드 1.

    python3 stock/source/tteoreojimyeon-sagi-2026-10/backtest/check_numbers.py
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
EP = HERE.parent
VID = EP.name
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / "tools"))
import srt_tool  # noqa: E402

R = json.loads((HERE / "results.json").read_text("utf-8"))
RES = R["results"]
S = srt_tool.parse_txt(EP / f"{VID}.txt")


def man(krw):            # 원 → '1억 2,934만' 식 (만 원 아래 반올림)
    m = round(krw / 10_000)
    eok, rest = divmod(m, 10_000)
    return (f"{eok}억 " if eok else "") + (f"{rest:,}만" if rest else "")


def pct(x, nd=1):
    return f"{x * 100:.{nd}f}%"


E1, E8, E3, E4, E7, E7d = RES["E1"], RES["E8"], RES["E3"], RES["E4"], RES["E7"], RES["E7d"]
m10, m20 = E1["main_10y"], E1["main_20y"]
d10m, d10d = E8["drop10_monthly"], E8["drop10_daily_from_2016_03"]
d20m, d20d = E8["drop20_monthly"], E8["drop20_daily_from_2016_03"]
e1p = next(v for k, v in RES["E1p"].items() if k.startswith("main_10y"))
e1d = next(v for k, v in RES["E1d"].items() if k.startswith("main_10y"))
b = RES["E8_base"]
l12, l120, lh = E3["main_12m_all_cash0"], E3["main_120m_all_cash0"], E3["main_12m_after_high_cash0"]

# (문장 번호, 문장에 있어야 할 글, 결과 키, 값, 맞는지)
CHECKS = [
    (38, "163번 중 117번", "E1.main_10y.drop10_cash0", f"{m10['windows']}·{m10['drop10_cash0']['dca_wins']}", m10["windows"] == 163 and m10["drop10_cash0"]["dca_wins"] == 117),
    (7, "23년", "data.first~complete_until", f"2000-01~{R['data']['complete_until'][:7]}", R["data"]["complete_until"].startswith("2023-06")),
    (44, "46번", "E8.drop10_monthly.b_wins", d10m["b_wins"], d10m["b_wins"] == 46),
    (50, "1.2%", "E8.drop10_monthly.b_max_ratio", d10m["b_max_ratio"], pct(d10m["b_max_ratio"] - 1) == "1.2%"),
    (52, "25% 넘게", "E8.drop10 a_max_ratio (월평균·일별)", f"{d10m['a_max_ratio']}·{d10d['a_max_ratio']}", min(d10m["a_max_ratio"], d10d["a_max_ratio"]) > 1.25),
    (11, "2000년 1월부터 2023년 6월", "params.main_start · data.complete_until", f"{R['params']['main_start'][:7]}·{R['data']['complete_until'][:7]}", R["params"]["main_start"].startswith("2000-01") and R["data"]["complete_until"].startswith("2023-06")),
    (18, "1억 2,000만 원", "E1.main_10y.contributed_krw", m10["contributed_krw"], m10["contributed_krw"] == 120_000_000),
    (30, "2013년 7월", "E1.main_10y.last_start", m10["last_start"], m10["last_start"] == "2013-07"),
    (38, "163번 중 117번", "E1.main_10y.drop10_cash0.dca_wins", m10["drop10_cash0"]["dca_wins"], m10["drop10_cash0"]["dca_wins"] == 117),
    (39, "일곱 번꼴", "117/163", f"{117 / 163:.3f}", 0.65 <= 117 / 163 < 0.75),
    (40, "2억 957만 원", "E1.main_10y.dca_median_krw", m10["dca_median_krw"], man(m10["dca_median_krw"]) == "2억 957만"),
    (41, "898만 원", "E1.main_10y.drop10_cash0.median_gap_krw", m10["drop10_cash0"]["median_gap_krw"], man(m10["drop10_cash0"]["median_gap_krw"]) == "898만"),
    (44, "2000년 1월부터 2003년 10월", "E8.drop10 b_win_starts (월평균·일별)", d10m["b_win_starts"], d10m["b_win_starts"] == ["2000-01", "2003-10"] == d10d["b_win_starts"]),
    (49, "1억 2,934만 원", "E7.first.dip_krw", E7["first"]["dip_krw"], man(E7["first"]["dip_krw"]) == "1억 2,934만"),
    (49, "1억 2,785만 원", "E7.first.dca_krw", E7["first"]["dca_krw"], man(E7["first"]["dca_krw"]) == "1억 2,785만"),
    (50, "150만 원", "E7.first.gap_krw", E7["first"]["gap_krw"], man(-E7["first"]["gap_krw"]) == "150만"),
    (51, "2003년 11월 이후", "E8.drop10 a_win_first_start · 그 뒤 모두", f"{d10m['a_win_first_start']} · {d10m['a_win_all_after_first']}", d10m["a_win_first_start"] == "2003-11" and d10m["a_win_all_after_first"] and d10d["a_win_all_after_first"]),
    (54, "43번 모두", "E1.main_20y.drop10_cash0", f"{m20['drop10_cash0']['dca_wins']}/{m20['windows']}", m20["drop10_cash0"]["dca_wins"] == m20["windows"] == 43),
    (55, "2억 4,000만 원", "E1.main_20y.contributed_krw", m20["contributed_krw"], m20["contributed_krw"] == 240_000_000),
    (55, "약 4,000만 원", "E1.main_20y.drop10_cash0.median_gap_krw", m20["drop10_cash0"]["median_gap_krw"], 3_950_0000 <= m20["drop10_cash0"]["median_gap_krw"] <= 4_050_0000),
    (57, "114번", "E1.main_10y.drop10_cashRate.dca_wins", m10["drop10_cashRate"]["dca_wins"], m10["drop10_cashRate"]["dca_wins"] == 114),
    (58, "116번", "E1.main_10y.drop5_cash0.dca_wins", m10["drop5_cash0"]["dca_wins"], m10["drop5_cash0"]["dca_wins"] == 116),
    (59, "117번", "E1d.main_10y.drop10_cash0.dca_wins", e1d["drop10_cash0"]["dca_wins"], e1d["drop10_cash0"]["dca_wins"] == 117),
    (64, "270번 중 198번", "E8_base.fwd12", f"{b['fwd12_up']}/{b['fwd12_months']}", (b["fwd12_months"], b["fwd12_up"]) == (270, 198)),
    (65, "73%", "198/270", f"{198 / 270:.3f}", f"{b['fwd12_up'] / b['fwd12_months'] * 100:.0f}%" == "73%"),
    (67, "11개월", "E7.avg_wait_months_median (월평균·일별)", f"{E7['avg_wait_months_median']}·{E7d['avg_wait_months_median']}", all(10.5 <= x < 11.5 for x in (E7["avg_wait_months_median"], E7d["avg_wait_months_median"]))),
    (75, "절반이 넘는 기간", "E7 평균 단가 B<A 기간 (월평균·일별)", f"{E7['windows'] - E7['dip_avg_cost_higher_windows']}·{E7d['windows'] - E7d['dip_avg_cost_higher_windows']}/163", min(E7["windows"] - E7["dip_avg_cost_higher_windows"], E7d["windows"] - E7d["dip_avg_cost_higher_windows"]) > 163 / 2),
    (76, "1%가 채 안", "E7.avg_cost_ratio_median (월평균·일별)", f"{E7['avg_cost_ratio_median']}·{E7d['avg_cost_ratio_median']}", all(0.99 <= x < 1 for x in (E7["avg_cost_ratio_median"], E7d["avg_cost_ratio_median"]))),
    (84, "79번", "E8.drop20 a_wins (월평균·일별)", f"{d20m['a_wins']}·{d20d['a_wins']}", d20m["a_wins"] == d20d["a_wins"] == 79),
    (86, "2006년 12월까지", "E8.drop20 b_win_starts", d20m["b_win_starts"], d20m["b_win_starts"] == ["2000-01", "2006-12"] == d20d["b_win_starts"]),
    (87, "11.5%", "E8.drop20.b_max_ratio", d20m["b_max_ratio"], pct(d20m["b_max_ratio"] - 1) == "11.5%"),
    (88, "2007년 1월 이후", "E8.drop20 a_win_first_start · 그 뒤 모두", d20m["a_win_first_start"], d20m["a_win_first_start"] == "2007-01" and d20m["a_win_all_after_first"] and d20d["a_win_all_after_first"]),
    (89, "1.4배 넘게", "E8.drop20 a_max_ratio (월평균·일별)", f"{d20m['a_max_ratio']}·{d20d['a_max_ratio']}", min(d20m["a_max_ratio"], d20d["a_max_ratio"]) > 1.4),
    (95, "넷 중 한 달꼴", "E8_base.after_high_months/main_months", f"{b['after_high_months']}/{b['main_months']}", 0.2 <= b["after_high_months"] / b["main_months"] < 0.3),
    (97, "10.8%", "E4.main_60m.high_median_annual", E4["main_60m"]["high_median_annual"], pct(E4["main_60m"]["high_median_annual"]) == "10.8%"),
    (98, "10.6%", "E4.main_60m.all_median_annual", E4["main_60m"]["all_median_annual"], pct(E4["main_60m"]["all_median_annual"]) == "10.6%"),
    (100, "9.0%", "E4.main_12m.high_median_annual", E4["main_12m"]["high_median_annual"], pct(E4["main_12m"]["high_median_annual"]) == "9.0%"),
    (100, "11.4%", "E4.main_12m.all_median_annual", E4["main_12m"]["all_median_annual"], pct(E4["main_12m"]["all_median_annual"]) == "11.4%"),
    (104, "271번 중 195번", "E3.main_12m_all_cash0", f"{l12['lump_wins']}/{l12['windows']}", (l12["windows"], l12["lump_wins"]) == (271, 195)),
    (105, "4.4%", "E3.main_12m_all_cash0.ratio_median", l12["ratio_median"], pct(l12["ratio_median"] - 1) == "4.4%"),
    (106, "163번 중 108번", "E3.main_120m_all_cash0", f"{l120['lump_wins']}/{l120['windows']}", (l120["windows"], l120["lump_wins"]) == (163, 108)),
    (109, "69번 중 47번", "E3.main_12m_after_high_cash0", f"{lh['lump_wins']}/{lh['windows']}", (lh["windows"], lh["lump_wins"]) == (69, 47)),
    (111, "2008년 4월", "E3.main_12m_all_cash0.lump_worst_start", l12["lump_worst_start"], l12["lump_worst_start"] == "2008-04"),
    (111, "43%", "E3.main_12m_all_cash0.lump_worst", l12["lump_worst"], f"{(1 - l12['lump_worst']) * 100:.0f}%" == "43%"),
    (112, "26%", "E3.main_12m_all_cash0.split_at_lump_worst", l12["split_at_lump_worst"], f"{(1 - l12['split_at_lump_worst']) * 100:.0f}%" == "26%"),
    (114, "40% 넘게", "E3.main_12m_all_cash0.lump_worst", l12["lump_worst"], l12["lump_worst"] < 0.6),
    (115, "셋 중 둘", "195/271", f"{195 / 271:.2f}", 0.6 <= l12["lump_wins"] / l12["windows"] < 0.75),
    (117, "4% 남짓", "E3.main_12m_all_cash0.ratio_median", l12["ratio_median"], 1.04 <= l12["ratio_median"] < 1.05),
    (127, "202번 중 156번", "E1p.main_10y_price_only.drop10_cash0", f"{e1p['drop10_cash0']['dca_wins']}/{e1p['windows']}", (e1p["windows"], e1p["drop10_cash0"]["dca_wins"]) == (202, 156)),
    (127, "2026년 9월", "data.last", R["data"]["last"][:7], R["data"]["last"].startswith("2026-09")),
]


def main():
    rows, bad = [], 0
    for n, frag, key, val, ok in CHECKS:
        in_text = frag in S[n - 1]
        good = bool(ok) and in_text
        bad += not good
        rows.append(f"| {n} | {S[n - 1]} | {frag} | `{key}` = {val} | {'✅' if good else '❌' + ('' if in_text else ' (문장에 글이 없음)')} |")
        print(f"[CHECK] sentence={n} frag={frag!r} key={key} value={val} ok={good}")
    md = [f"# {VID} 숫자 확인표 (`backtest/check_numbers.py` v1.1)", "",
          f"- 결과 파일: `backtest/results.json` (`run.py` {R['version']}, 엔진 {R['engine']}, 만든 시각 {R['generated']})",
          f"- 자료: {R['data'].get('url')} (sha256 {R['data'].get('sha256', '')[:12]}…)",
          "- 대본의 숫자는 모두 이 표의 결과 키에서 나온다 (stock/guides/concept.md 2번). 대본·결과가 바뀌면 이 코드를 다시 돌린다.",
          "- 법령 사실이 없는 영상이라 법령 확인은 없다. 자료 방식(월평균)이 숫자를 바꾸는지는 일별 신호로 같은 숫자인지 함께 봤다 ('월평균·일별').",
          "- ※ 연구·교육용. 투자 권유가 아님.", "",
          "| 문장 | 대본 | 숫자 | 결과 키 = 값 | 상태 |", "|---|---|---|---|---|"] + rows + ["",
          f"결과: {len(CHECKS) - bad}/{len(CHECKS)} ✅" + ("" if not bad else f" · ❌ {bad}개 — 대본이나 결과를 고칠 것")]
    (EP / "checklist.md").write_text("\n".join(md) + "\n", "utf-8")
    print(f"[DONE] checks={len(CHECKS)} bad={bad} out={EP / 'checklist.md'}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
