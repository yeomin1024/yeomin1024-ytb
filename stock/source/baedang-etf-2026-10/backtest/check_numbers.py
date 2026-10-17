#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-10-17 — 대본 v1.1 (도입 + 규칙 24초 — 사용자 지시 2026-10-17 '테스트 들어가기 전 도입 및 규칙 설명 30초 넘기지 말라고'): 규칙 문장 2개로, 15% 세율 문장은 '다른 조건', 구조(배당 한 번)는 결과 뒤.
# v1.0 — 2026-10-16 — 최초. 대본 baedang-etf-2026-10.txt 숫자 검사 — 결과 = results.json (run.py v1.0). 공통 부품 tools/backtest/numcheck.py v1.0.
#          문장마다 results.json 에서 글자를 다시 만들어 그 문장에 그대로 있는지 + 조건 + 대본의 모든 숫자가 검사표에 있는지 → ../checklist.md.
"""python3 stock/source/baedang-etf-2026-10/backtest/check_numbers.py   # 하나라도 다르면 끝 코드 1"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[3] / "tools"))
from backtest import numcheck as nc  # noqa: E402
from backtest.numcheck import won, pct, ym, md, ymd, rint  # noqa: E402

R = json.loads((HERE / "results.json").read_text("utf-8"))
C = nc.Checker(HERE.parent / "baedang-etf-2026-10.txt")
S, need, need_any, cond = C.S, C.need, C.need_any, C.cond
M, F = R["main"], R["facts"]
Y = F["year"]
X = lambda v: f"{v:.2f}배"


def ye(anchor, y, both=True):
    n = S(anchor); v = Y[str(y)]
    need(n, won(v["a"]), f"{y} 말 SCHD"); need(n, won(v["b"]), f"{y} 말 SPY"); cond(n, True, "", f"{y}년")
    return n


# ---- 규칙
n = S("2011년부터 매달 1,000달러씩"); need(n, f"{M['start'][:4]}년부터", "시작 해 (날짜 전부는 화면)"); need(n, won(R["monthly"]), "매달")
n = S("배당은 15%를 떼고"); cond(n, R["tax"] == 0.15, "tax", "15%"); cond(n, R["fee"] == 0.0025, "fee", "0.25%")
cond(S("15%는 많은 나라가"), True, "가정 (세율은 나라마다 다름 — run.py TAX)", "15%")
# ---- 구조: 배당 한 번
E = R["div_example"]
n = S("SCHD 계좌에는"); need(n, ymd(E["date"]), "예 날짜"); need(n, nc.comma(rint(E["shares"])).replace(",", ",") and f"{rint(E['shares']) // 10000}만 {nc.comma(rint(E['shares']) % 10000)}주", "주식 수")
n = S("1주에 0.278달러"); cond(n, True, "1주당", "1주"); need(n, f"{E['dps']:.3f}달러", "1주 배당"); need(n, won(E["gross"]), "배당 합 (세전)")
n = S("세금 15%, 561달러를"); need(n, won(E["tax"]), "세금"); need(n, won(E["net"]), "남은 돈"); cond(n, True, "", "15%")
n = S("이 돈으로 그날"); need(n, f"{E['price']:.2f}달러", "그날 종가"); need(n, f"{rint(E['new_shares'])}주", "새 주식 수")
cond(n, abs(E["shares"] + E["new_shares"] - E["check_shares_after"]) < 0.02, "주식 수가 계좌 기록과 맞음")
n = S("2025년 배당률은"); cond(n, True, "", "2025년"); need(n, pct(R["props"]["SCHD"]["2025"]["yield"]), "SCHD 2025 배당률"); need(n, pct(R["props"]["SPY"]["2025"]["yield"]), "SPY 2025 배당률")
# ---- 경주
n = S("첫 배당은 2011년 12월"); need(n, f"SPY {won(F['b_first_div']['gross'])}", "SPY 첫 배당"); need(n, f"SCHD {won(F['a_first_div']['gross'])}", "SCHD 첫 배당")
cond(n, F["a_first_div"]["date"].startswith("2011-12") and F["b_first_div"]["date"].startswith("2011-12"), "둘 다 2011-12", "2011년 12월")
n = ye("2012년 말 넣은 돈은", 2012); need(n, won(Y["2012"]["paid"], thousand=True), "2012 말 넣은 돈")
ye("2013년 말에는 SCHD", 2013); ye("2014년 말, SCHD", 2014)
n = ye("넣은 돈 5만 달러는", 2015); need(n, won(Y["2015"]["paid"]), "2015 말 넣은 돈")
n = ye("SCHD가 8만 4,248달러로", 2016); cond(n, Y["2016"]["lead"] == "a", "2016 말 SCHD 앞섬")
n = ye("2017년 말에는 SCHD 11만", 2017); cond(S("둘이 거의 같았습니다"), abs(Y["2017"]["a"] / Y["2017"]["b"] - 1) < 0.005, "차이 0.5% 안 (거의 같음)")
ch = F["lead_change_dates"]
n = S("앞선 계좌가 43번"); need(n, f"{sum(1 for x in ch if x['date'] <= '2017-12-31')}번", "2017년까지 바뀐 횟수"); cond(n, True, "", "2017년")
n = S("2018년 1월 2일부터는 SPY"); cond(n, any(x["date"] == "2018-01-02" and x["lead"] == "b" for x in ch) and not any("2018-01-03" <= x["date"] < "2021-03-05" for x in ch), "2018-01-02 SPY 앞섬 · 2021-03 까지 바뀜 없음", "2018년 1월 2일")
ye("2018년 말에는 SCHD 11만 9", 2018)
n = S("2019년 한 해, SCHD는 배당"); need(n, won(Y["2019"]["a_div_y"]), "2019 SCHD 배당"); need(n, won(Y["2019"]["b_div_y"]), "2019 SPY 배당"); cond(n, True, "", "2019년")
n = S("넣은 돈이 10만 달러가 됐어요"); need(n, ym(F["paid_ge"]["100000"]), "10만 날"); need(n, won(100_000), "문턱")
cv = F["covid"]
n = S("코로나 폭락 때는"); need(n, md(cv["a"]["low_date"]), "최저 날"); n2 = S("SCHD 계좌는 32.8%"); need(n2, pct(cv["a"]["drop"]), "SCHD 하락"); need(n2, pct(cv["b"]["drop"]), "SPY 하락")
cond(n, cv["a"]["low_date"] == cv["b"]["low_date"] and cv["a"]["high_date"].startswith("2020-02") and cv["b"]["high_date"].startswith("2020-02"), "2월 최고 → 같은 날 최저")
ye("2020년 말에는 SCHD 20만", 2020); ye("2021년 말, SCHD 27만", 2021)
# ---- 하락장
cond(S("2022년, 긴 하락장이 왔어요"), True, "", "2022년")
n = S("4월에는 SCHD가 다시 앞섰습니다"); last_apr = [x for x in ch if x["date"].startswith("2022-04")][-1]
cond(n, last_apr["lead"] == "a" and not any("2022-04-21" <= x["date"] < "2023-04-26" for x in ch), f"2022-04 마지막 바뀜 {last_apr['date']} SCHD · 2023-04-26 까지 그대로", "4월")
y22 = F["y2022"]
n = S("그해 SCHD 계좌는 14.6%"); need(n, pct(y22["a"]["drop"]), "SCHD 2022 하락"); need(n, pct(y22["b"]["drop"]), "SPY 2022 하락")
n = ye("2022년 말에는 SCHD 27만", 2022); cond(n, Y["2022"]["lead"] == "a", "SCHD 앞섬")
n = S("2023년 1월 6일, SCHD는"); need(n, ymd(F["max_gap_a"]["date"]), "SCHD 가장 앞선 날"); need(n, won(F["max_gap_a"]["gap"]), "차이")
n = S("2023년 4월 26일, SPY가 다시"); cond(n, F["last_lead_change"] == {"date": "2023-04-26", "lead": "b"}, "마지막 바뀜", "2023년 4월 26일")
ye("2023년 말, SCHD 30만", 2023)
n = S("넣은 돈이 15만 달러가 됐습니다"); need(n, ym(F["paid_ge"]["150000"]), "15만 날"); need(n, won(150_000), "문턱")
ye("2024년 말, SCHD 34만", 2024)
n = S("2025년 한 해 배당은"); need(n, won(Y["2025"]["a_div_y"]), "2025 SCHD 배당"); need(n, won(Y["2025"]["b_div_y"]), "2025 SPY 배당"); cond(n, True, "", "2025년")
ye("2025년 말에는 SCHD 37만", 2025)
# ---- 결과
need(S("2026년 10월 15일, 결과입니다"), ymd(R["end"]), "끝 날")
n = S("두 계좌 모두 180번"); need(n, f"{round(M['paid'] / R['monthly'])}번", "매수 횟수"); need(n, won(M["paid"]), "넣은 돈")
need(S("SCHD 계좌는 48만"), won(M["a_end"]), "SCHD 끝"); need(S("SPY 계좌는 58만"), won(M["b_end"]), "SPY 끝")
n = S("SPY 계좌가 10만 6,119달러"); need(n, won(M["gap"]), "차이"); need(n, X(M["b_over_a"]), "SPY ÷ SCHD")
n = S("2023년 4월 26일 뒤로"); cond(n, F["last_lead_change"]["date"] == "2023-04-26" and F["last_lead_change"]["lead"] == "b", "그 뒤 바뀜 없음", "2023년 4월 26일")
need(S("SCHD가 앞선 날은"), pct(M["a_lead_days_share"]), "SCHD 앞선 날 비율")
n = S("받은 배당은 SCHD가"); need(n, won(M["a_div"]), "SCHD 배당 합"); need(n, won(M["b_div"]), "SPY 배당 합"); need(n, f"{M['div_ratio']:.1f}배", "배당 비")
n = S("낸 세금도 SCHD"); need(n, won(M["a_tax"]), "SCHD 세금"); need(n, won(M["b_tax"]), "SPY 세금")
n = S("지난 1년 배당은"); need(n, won(F["last12"]["a_div"]), "SCHD 지난 1년"); need(n, won(F["last12"]["b_div"]), "SPY 지난 1년"); cond(n, True, "", "1년")
n = S("2012년부터는 해마다"); cond(n, all(v["a_div_y"] > v["b_div_y"] for y, v in Y.items() if int(y) >= 2012), "2012~ 해마다 SCHD 배당 > SPY", "2012년")
# ---- 해마다
AT, ATS = R["annual_tr"], R["annual_tr_summary"]
cond(S("세금과 수수료를 빼고, 배당을 다시 넣은 1년"), True, "", "1년")
n = S("14년 중, SCHD가 더 많이 오른 해는"); need(n, f"{ATS['years']}년 중", "해 수"); need(n, f"{ATS['schd_wins']}번", "SCHD 이긴 해"); cond(n, True, "", "2012년"); cond(n, True, "", "2025년")
for y, anchor, word in [("2022", "2022년에는 SCHD", "하락"), ("2023", "2023년에는 SCHD", "상승"), ("2024", "2024년에는 SCHD", "상승"), ("2025", "2025년에는 SCHD", "상승")]:
    n = S(anchor); cond(n, True, "", f"{y}년"); need(n, pct(AT[y]["SCHD"]), f"{y} SCHD"); need(n, pct(AT[y]["SPY"]), f"{y} SPY"); cond(n, (AT[y]["SCHD"] < 0) == (word == "하락") and (AT[y]["SPY"] < 0) == (word == "하락"), f"{y} {word}")
# ---- 다른 조건
T0, T3, SA, LP = R["tax_checks"]["0.00"], R["tax_checks"]["0.30"], R["sell_all"], R["lump"]
n = S("세금을 0%로 하면"); need(n, won(T0["a_end"]), "0% SCHD"); need(n, won(T0["b_end"]), "0% SPY"); cond(n, True, "", "0%")
need(S("세금이 없어도 SPY가"), X(T0["b_over_a"]), "0% 비")
n = S("30%를 떼면"); need(n, X(T3["b_over_a"]), "30% 비"); cond(n, T3["b_over_a"] > M["b_over_a"], "커짐", "30%")
cond(S("늘어난 돈에 15% 세금을 내면"), SA["cg_tax"] == 0.15, "", "15%")
n = S("SCHD 44만"); need(n, won(SA["a"]), "매도 뒤 SCHD"); need(n, won(SA["b"]), "매도 뒤 SPY")
n = S("배당으로 세금을 미리 냈기 때문에"); need(n, X(SA["b_over_a"]), "매도 뒤 비"); cond(n, SA["b_over_a"] < M["b_over_a"] and M["a_basis"] > M["b_basis"], "줄어듦 · SCHD 취득 원가가 더 큼")
n = S("처음에 10만 달러를 한 번에"); need(n, won(R["lump"]["paid"]), "한 번에")
n = S("SCHD 61만"); need(n, won(LP["a_end"]), "한 번 SCHD"); need(n, won(LP["b_end"]), "한 번 SPY"); need(n, X(LP["b_over_a"]), "한 번 비")
# ---- 시작 시점
R5, R10 = R["rolling"]["5y"], R["rolling"]["10y"]
n = S("달마다 시작한 5년 적립 계좌를"); need(n, ym(R5["first_start"]), "첫 시작"); need(n, ym(R5["last_start"]), "마지막 시작"); cond(n, R5["years"] == 5, "", "5년")
need(S("모두 120개입니다"), f"{R5['windows']}개", "5년 계좌 수")
need(S("SCHD가 더 많이 남은 건 120개 중"), f"{R5['windows']}개 중 {R5['a_gt_b']}개", "SCHD 많음")
n = S("가장 크게 앞선 건"); need(n, ym(R5["a_best_start"]), "SCHD 가장 앞선 시작"); need(n, X(R5["a_best_ratio"]), "SCHD ÷ SPY")
n = S("2020년 11월에 시작한 계좌는"); need(n, ym(R5["b_best_start"]), "SPY 가장 앞선 시작"); need(n, X(R5["b_best_ratio"]), "SPY ÷ SCHD")
n = S("10년 적립 계좌 60개에서는"); need(n, f"{R10['windows']}개", "10년 계좌 수"); need(n, f"{R10['a_gt_b']}개", "SCHD 많음"); cond(n, R10["years"] == 10, "", "10년")
# ---- 더 긴 기간 (VYM)
V, VF, RV = R["vym"], R["vym_facts"], R["rolling_vym_10y"]
n = S("SCHD는 2011년에 생겨서"); cond(n, R["first_day"]["SCHD"].startswith("2011"), f"SCHD 첫 거래일 {R['first_day']['SCHD']}", "2011년"); cond(n, True, "", "2008년")
cond(S("2006년에 생긴 배당 ETF, VYM"), R["first_day"]["VYM"].startswith("2006"), f"VYM 첫 거래일 {R['first_day']['VYM']}", "2006년")
n = S("2006년 12월부터, 같은 규칙으로"); need(n, ym(V["start"]), "VYM 시작"); need(n, won(R["monthly"]), "매달")
n = S("2008년 금융위기 때, VYM 계좌는"); need(n, pct(VF["crisis_a"]["drop"]), "VYM 하락"); need(n, pct(VF["crisis_b"]["drop"]), "SPY 하락"); cond(n, True, "", "2008년")
n = S("2011년 10월 말까지는"); cond(n, VF["at_schd_start"]["date"].startswith("2011-10") and VF["at_schd_start"]["a"] > VF["at_schd_start"]["b"], "VYM 앞섬", "2011년 10월")
n = S("VYM 6만 6,764달러"); need(n, won(VF["at_schd_start"]["a"]), "VYM"); need(n, won(VF["at_schd_start"]["b"]), "SPY")
n = S("넣은 돈은 23만 9천 달러예요"); need(n, ymd(V["end"]), "끝"); need(n, won(V["paid"], thousand=True), "넣은 돈")
n = S("VYM 80만"); need(n, won(V["a_end"]), "VYM 끝"); need(n, won(V["b_end"]), "SPY 끝")
need(S("SPY가 1.35배 많았어요"), X(V["b_over_a"]), "VYM 비")
n = S("10년 적립 계좌 119개 중"); need(n, f"{RV['windows']}개 중", "VYM 10년 수"); need(n, f"{RV['a_gt_b']}개", "VYM 많음"); cond(n, True, "", "10년")
# ---- 정리
n = S("세금 15%를 떼고 15년 동안"); cond(n, round(M["years"]) == 15, f"{M['years']}년", "15년"); cond(n, True, "", "15%")
need(S("SPY 계좌가 SCHD 계좌의 1.22배"), X(M["b_over_a"]), "본 실험 비")
need(S("세금이 없어도 1.19배였습니다"), X(T0["b_over_a"]), "0% 비")
need(S("SCHD는 배당을 2.1배 받았고"), f"{M['div_ratio']:.1f}배", "배당 비"); cond(S("SCHD는 배당을 2.1배 받았고"), M["tax_ratio"] > 2.0, f"세금 비 {M['tax_ratio']}")
cond(S("2022년 같은 하락장에서는 SCHD가 덜"), y22["a"]["drop"] > y22["b"]["drop"], "2022 SCHD 덜 떨어짐", "2022년")
need(S("SCHD가 앞선 계좌도 있었지만"), f"{R5['windows']}개 중 {R5['a_gt_b']}개", "5년")
n = S("10년 계좌 119개 중 114개"); need(n, f"{RV['windows']}개 중 {RV['b_gt_a']}개", "VYM 10년 SPY 많음"); cond(n, True, "", "2006년"); cond(n, True, "", "10년")
sys.exit(C.report(HERE.parent / "checklist.md", "baedang-etf-2026-10 숫자 검사 (`backtest/check_numbers.py` v1.0)", f"`backtest/results.json` ({R['version']})"))
