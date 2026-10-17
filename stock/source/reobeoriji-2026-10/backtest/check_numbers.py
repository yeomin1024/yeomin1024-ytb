#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-10-17 — 대본 v1.1 (도입 + 규칙 24초 — 사용자 지시 2026-10-17 '테스트 들어가기 전 도입 및 규칙 설명 30초 넘기지 말라고'): 계산 방법 문장은 '실제 ETF' 앞, 매일 맞추기는 결과 뒤 · 코로나 3배 최저 vs 넣은 돈 · 2025 1배·2배 하락 문장 더함.
# v1.0 — 2026-10-16 — 최초. 대본 reobeoriji-2026-10.txt 숫자 검사 — 결과 = results.json (run.py v1.0). 공통 부품 tools/backtest/numcheck.py v1.0.
"""python3 stock/source/reobeoriji-2026-10/backtest/check_numbers.py   # 하나라도 다르면 끝 코드 1"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[3] / "tools"))
from backtest import numcheck as nc  # noqa: E402
from backtest.numcheck import won, pct, pcts, ym, md, ymd  # noqa: E402

R = json.loads((HERE / "results.json").read_text("utf-8"))
C = nc.Checker(HERE.parent / "reobeoriji-2026-10.txt")
S, need, need_any, cond = C.S, C.need, C.need_any, C.cond
M, F, Y = R["main"], R["facts"], R["facts"]["year"]
YR = R["year_ret_exact"]
X2 = lambda v: f"{v:.2f}배"


def won_big(x):
    """1,000만 달러 넘는 값: 17306585 → '1,730만 6,585달러'."""
    v = nc.rint(x); man, rest = divmod(v, 10000)
    return f"{man:,}만 {rest:,}달러" if rest else f"{man:,}만 달러"


def W_(x):
    return won_big(x) if nc.rint(x) >= 10_000_000 else won(x)


# ---- 도입·규칙
cond(S("나스닥100을 2배, 3배로"), True, "", "100"); cond(S("나스닥100을 2배, 3배로"), True, "", "2배"); cond(S("나스닥100을 2배, 3배로"), True, "", "3배")
n = S("1배·2배·3배를 백테스트로"); [cond(n, True, "", t) for t in ("1배", "2배", "3배")]; cond(n, R["start"].startswith("1999"), "시작 해 (날짜 전부는 화면)", "1999년")
n = S("2배와 3배는 QLD·TQQQ와"); cond(n, True, "", "2배"); cond(n, True, "", "3배")
cond(S("2배와 3배 계좌는 이렇게"), True, "", "2배"); cond(S("2배와 3배 계좌는 이렇게"), True, "", "3배")
n = S("두 ETF는 2006년과 2010년에"); cond(n, True, "QLD 2006-06-21 · TQQQ 2010-02-11 첫 거래일 (자료 meta)", "2006년"); cond(n, True, "", "2010년"); cond(n, True, "", "1999년")
n = S("하루 수익률의 2배, 3배를"); cond(n, R["er_lev"] == 0.0095, "보수", "0.95%"); cond(n, True, "", "100"); cond(n, True, "", "2배"); cond(n, True, "", "3배")
n = S("미국 13주 국채 금리에"); need(n, pct(R["track"]["spread"], 2), "웃돈 s"); cond(n, True, "", "13주")
need(S("실제 QLD 결과와 맞도록"), pct(R["track"]["spread"], 2), "웃돈 s")
need(S("같은 값으로 TQQQ를 계산하면"), pct(R["track"]["tqqq"]["cagr_gap"], 2), "TQQQ 연 차이"); cond(S("같은 값으로 TQQQ를 계산하면"), R["track"]["tqqq"]["cagr_gap"] < 0, "적게", "1년")
n = S("매달 500달러씩 매수하고"); need(n, won(R["monthly"]), "매달"); cond(n, R["fee"] == 0.0025, "", "0.25%")
# ---- 매일 맞추기 (장난감 예 — 코드로 셈)
cond(S("3배는 왜 폭락 때"), True, "", "3배")
T = R["toy"]
cond(S("지수가 하루에 10% 오르고"), True, "예 +10%·−10%", "10%")
need(S("1배는 1% 손해"), pct(T["x1"], 0), "1배")
n = S("2배는 20% 올랐다가"); need(n, pct(T["x2"], 0), "2배"); cond(n, True, "", "2배"); cond(n, True, "2 × 10%", "20%")
n = S("3배는 30% 올랐다가"); need(n, pct(T["x3"], 0), "3배"); cond(n, True, "", "3배"); cond(n, True, "3 × 10%", "30%")
n = S("실제로 2018년, 1배는"); need(n, pct(YR["2018"]["x1"]), "2018 1배"); cond(n, True, "", "2018년"); cond(n, True, "", "1배")
n = S("그해 2배는 8.6%"); need(n, pct(YR["2018"]["x2"]), "2018 2배"); need(n, pct(YR["2018"]["x3"]), "2018 3배"); cond(n, True, "", "2배"); cond(n, True, "", "3배")
# ---- 경주
n = S("파란 선이 1배"); [cond(n, True, "", t) for t in ("1배", "2배", "3배")]
cond(S("세로 눈금은 한 칸 오를 때마다"), True, "로그 눈금", "10배")
v = Y["1999"]; n = S("1999년 말, 넣은 돈"); need(n, won(v["paid"]), "1999 넣은 돈"); cond(n, True, "", "1999년"); n = S("1배 7,011달러"); need(n, f"1배 {won(v['x1'])}", "1배"); need(n, f"2배 {won(v['x2'])}", "2배"); need(n, f"3배 {won(v['x3'])}", "3배")
cond(S("2000년 3월부터 닷컴"), R["dd_dotcom"]["x1"]["peak_date"].startswith("2000-03"), "1배 최고 2000-03", "2000년 3월")
D3 = F["dot"]["x3"]
n = S("2001년 3월 29일, 3배 계좌는"); need(n, ymd(D3["low_date"]), "3배 최저 날"); need(n, won(D3["low"]), "3배 최저"); cond(n, True, "", "3배")
n = S("넣은 돈은 1만 2천 달러였는데"); need(n, won(D3["paid_low"], thousand=True), "그날 넣은 돈"); need(n, pct(D3["vs_paid_low"]), "넣은 돈 대비")
n = S("4월 4일, 2배는"); need(n, md(F["dot"]["x2"]["low_date"]), "2배 최저 날"); need(n, f"2배는 {won(F['dot']['x2']['low'])}", "2배"); need(n, f"1배는 {won(F['dot']['x1']['low'])}", "1배")
cond(n, F["dot"]["x1"]["low_date"] == F["dot"]["x2"]["low_date"], "같은 날")
DD = R["dd_dotcom"]
n = S("1주 값으로 보면"); need(n, pct(DD["x3"]["dd"], 2), "3배 가격 하락"); need(n, pct(DD["x2"]["dd"]), "2배 가격 하락"); cond(n, DD["x3"]["trough_date"].startswith("2002-10"), "", "2002년 10월"); cond(n, True, "1주", "1주"); cond(n, True, "", "3배"); cond(n, True, "", "2배")
need_any(S("1배도 83% 떨어졌습니다"), pcts(DD["x1"]["dd"], 0) if pct(DD["x1"]["dd"], 0) == "83%" and pct(DD["x1"]["dd"]) == "83.0%" else [pct(DD["x1"]["dd"])], "1배 가격 하락"); cond(S("1배도 83% 떨어졌습니다"), True, "", "1배")
n = S("매달 500달러씩 계속 매수했어요"); need(n, won(R["monthly"]), "매달")
n = S("2003년, 3배는"); need(n, pct(YR["2003"]["x3"]), "2003 3배"); cond(n, True, "", "2003년"); cond(n, True, "", "3배")
v = Y["2004"]; n = S("2004년 말, 넣은 돈"); need(n, won(v["paid"]), "넣은 돈"); cond(n, True, "", "2004년"); n = S("1배 3만 4,883달러"); need(n, f"1배 {won(v['x1'])}", "1배"); need(n, f"3배 {won(v['x3'])}", "3배")
v6 = Y["2006"]; n = S("2006년 말에는 1배"); need(n, f"1배 {won(v6['x1'])}", "1배"); need(n, f"3배 {won(v6['x3'])}", "3배"); cond(n, True, "", "2006년")
v = Y["2007"]; n = S("2007년 말에는 셋이"); cond(n, max(v['x1'], v['x2'], v['x3']) / min(v['x1'], v['x2'], v['x3']) < 1.03, "3% 안 (거의 같음)", "2007년"); n = S("1배 6만 7,354달러"); need(n, f"1배 {won(v['x1'])}", "1배"); need(n, f"2배 {won(v['x2'])}", "2배"); need(n, f"3배 {won(v['x3'])}", "3배")
# ---- 금융위기
G3 = F["gfc"]["x3"]
cond(S("그리고 2008년 금융위기가"), True, "", "2008년")
n = S("11월 20일, 3배 계좌는"); need(n, md(G3["low_date"]), "3배 최저 날"); need(n, won(G3["low"]), "3배"); cond(n, True, "", "3배")
n = S("넣은 돈 5만 8천 달러에서"); need(n, won(G3["paid_low"], thousand=True), "넣은 돈"); need(n, pct(G3["vs_paid_low"]), "넣은 돈 대비")
n = S("같은 날 1배는 3만"); need(n, f"1배는 {won(F['gfc']['x1']['low'])}", "1배"); need(n, f"2배는 {won(F['gfc']['x2']['low'])}", "2배"); cond(n, F["gfc"]["x1"]["low_date"] == G3["low_date"] == F["gfc"]["x2"]["low_date"], "같은 날")
n = S("2009년, 3배는"); need(n, pct(YR["2009"]["x3"]), "2009 3배"); cond(n, True, "", "2009년"); cond(n, True, "", "3배")
MS = F["milestones"]
n = S("2011년 1월, 1배 계좌가"); need(n, ym(MS["x1"]["100000"]), "1배 10만"); need(n, won(100_000), "문턱"); cond(n, True, "", "1배")
n = S("2012년 2월에는 3배 계좌도"); need(n, ym(MS["x3"]["100000"]), "3배 10만"); need(n, won(100_000), "문턱"); cond(n, True, "", "3배")
v = Y["2012"]; n = S("2012년 말에도 1배가"); cond(n, v["x1"] > v["x2"] and v["x1"] > v["x3"], "2012 말 1배 가장 많음", "2012년"); cond(n, True, "", "1배")
n = S("2013년 7월 3일, 3배가"); need(n, ymd(F["x3_ahead_since"]["date"]), "3배가 계속 앞선 첫날"); cond(n, F["x3_ahead_since"]["stayed"], "그 뒤 계속"); cond(n, True, "", "3배"); cond(n, True, "", "1배")
v = Y["2013"]; n = S("2013년 말에는 순서가"); cond(n, v["x3"] > v["x2"] > v["x1"], "3배 > 2배 > 1배 (2012 말과 반대)", "2013년"); n = S("1배 18만 7,637달러"); need(n, f"1배 {won(v['x1'])}", "1배"); need(n, f"2배 {won(v['x2'])}", "2배"); need(n, f"3배 {won(v['x3'])}", "3배")
v6 = Y["2016"]; n = S("2016년 말, 3배"); need(n, f"3배 {won(v6['x3'])}", "3배"); need(n, f"1배 {won(v6['x1'])}", "1배"); cond(n, True, "", "2016년")
n = S("2017년 6월, 3배 계좌가"); need(n, ym(MS["x3"]["1000000"]), "3배 100만"); need(n, won(1_000_000), "문턱"); cond(n, True, "", "3배")
n = S("2018년 말에는 3배가"); need(n, won(Y["2018"]["x3"]), "2018 말 3배"); cond(n, True, "", "2018년"); cond(n, True, "", "3배")
v = Y["2019"]; n = S("2019년 말, 3배"); need(n, f"3배 {won(v['x3'])}", "3배"); need(n, f"1배 {won(v['x1'])}", "1배"); cond(n, True, "", "2019년")
CV = F["covid"]
n = S("코로나 폭락 때, 2월 19일부터"); need(n, md(CV["x3"]["high_date"]), "최고 날"); need(n, md(CV["x3"]["low_date"]), "최저 날"); need(n, pct(CV["x3"]["drop"]), "3배"); cond(n, True, "", "3배")
n = S("1배는 28.5%, 2배는"); need(n, pct(CV["x1"]["drop"]), "1배"); need(n, pct(CV["x2"]["drop"]), "2배"); cond(n, True, "", "1배"); cond(n, True, "", "2배")
n = S("그래도 3월 16일 3배 계좌는"); need(n, md(CV["x3"]["low_date"]), "최저 날"); need(n, won(CV["x3"]["low"]), "3배 최저"); cond(n, True, "", "3배")
n = S("넣은 돈 12만 6천 달러보다는"); need(n, won(CV["x3"]["paid_low"], thousand=True), "그날 넣은 돈"); cond(n, CV["x3"]["low"] > CV["x3"]["paid_low"], "3배 최저 > 넣은 돈")
n = S("2021년 말, 3배는"); need(n, won(Y["2021"]["x3"]), "2021 3배"); cond(n, True, "", "2021년"); cond(n, True, "", "3배")
v = Y["2021"]; n = S("1배는 104만"); need(n, f"1배는 {won(v['x1'])}", "1배"); need(n, f"2배는 {won(v['x2'])}", "2배")
# ---- 긴 하락
Z = F["y2022"]
cond(S("2022년, 긴 하락이 왔습니다"), True, "", "2022년")
n = S("3배 계좌는 1월 3일"); need(n, md(Z["x3"]["high_date"]), "최고 날"); need(n, won(Z["x3"]["high"]), "최고"); cond(n, True, "", "3배"); n = S("12월 28일에는 178만"); need(n, md(Z["x3"]["low_date"]), "최저 날"); need(n, won(Z["x3"]["low"]), "최저")
need(S("80.9%가 줄었습니다"), pct(Z["x3"]["drop"]), "3배 하락")
n = S("2배는 62.8%, 1배는"); need(n, pct(Z["x2"]["drop"]), "2배"); need(n, pct(Z["x1"]["drop"]), "1배"); cond(n, True, "", "2배"); cond(n, True, "", "1배")
n = S("2023년, 3배는"); need(n, pct(YR["2023"]["x3"]), "2023 3배"); cond(n, True, "", "2023년"); cond(n, True, "", "3배")
n = S("2024년 12월, 3배 계좌가"); need(n, ym(MS["x3"]["10000000"]), "3배 1,000만"); cond(n, True, "", "1,000만"); cond(n, True, "", "3배")
Q = F["y2025"]["x3"]
n = S("2025년 4월 급락 때"); need(n, md(Q["high_date"]), "최고 날"); need(n, pct(Q["drop"]), "하락"); cond(n, Q["low_date"].startswith("2025-04"), "", "2025년 4월"); cond(n, True, "", "3배")
Q1, Q2 = F["y2025"]["x1"], F["y2025"]["x2"]
n = S("1배는 22.7%, 2배는"); need(n, pct(Q1["drop"]), "1배"); need(n, pct(Q2["drop"]), "2배"); cond(n, Q1["high_date"] == Q2["high_date"] == Q["high_date"] and Q1["low_date"] == Q2["low_date"] == Q["low_date"], "같은 기간 (2/19 → 4/8)"); cond(n, True, "", "1배"); cond(n, True, "", "2배")
# ---- 결과
need(S("2026년 10월 15일, 결과입니다"), ymd(R["end"]), "끝")
n = S("세 계좌 모두 331번"); need(n, f"{round(M['paid'] / R['monthly'])}번", "매수 횟수"); need(n, won(M["paid"]), "넣은 돈")
need(S("1배 계좌는 202만"), won(M["x1"]), "1배 끝"); cond(S("1배 계좌는 202만"), True, "", "1배")
need(S("2배 계좌는 792만"), won(M["x2"]), "2배 끝"); cond(S("2배 계좌는 792만"), True, "", "2배")
need(S("3배 계좌는 1,730만"), W_(M["x3"]), "3배 끝"); cond(S("3배 계좌는 1,730만"), True, "", "3배")
PK = F["peak"]["x3"]; n = S("3배 계좌가 가장 많았던 날은"); need(n, ymd(PK["date"]), "3배 가장 많던 날"); need(n, W_(PK["val"]), "그날 3배"); cond(n, True, "", "3배")
n = S("3배가 1배의 8.55배, 2배는"); need(n, X2(M["x3_over_x1"]), "3배÷1배"); need(n, X2(M["x2_over_x1"]), "2배÷1배"); cond(n, True, "", "1배"); cond(n, True, "", "3배가"); cond(n, True, "", "2배는")
n = S("2013년 7월 3일 뒤로"); need(n, ymd(F["x3_ahead_since"]["date"]), "날"); cond(n, F["x3_ahead_since"]["stayed"], "계속"); cond(n, True, "", "3배"); cond(n, True, "", "1배")
n = S("그 전 14.3년 동안은"); need(n, f"{F['x3_ahead_since']['years_before']:.1f}년", "기간"); need(n, pct(F["x3_ahead_since"]["share_before"]), "3배 앞선 날 비율"); cond(n, True, "", "3배"); cond(n, True, "", "1배")
n = S("넣은 돈보다 많았던 날은"); need(n, f"1배 {pct(F['x1_above_paid_share'])}", "1배"); need(n, f"3배 {pct(F['x3_above_paid_share'])}", "3배")
# ---- 한 번에
LP, LL = R["lump"], R["lump_low"]
n = S("세 계좌에 1만 달러씩"); need(n, ymd(R["start"]), "시작"); need(n, won(R["lump"]["paid"]), "한 번")
n = S("3배 계좌에는 13달러가"); need(n, ymd(LL["x3"]["date"]), "3배 최저 날"); need(n, won(LL["x3"]["val"]), "3배 최저"); cond(n, True, "", "3배")
n = S("처음 넣은 1만 달러의"); need(n, won(R["lump"]["paid"]), "한 번"); need(n, pct(LL["x3"]["val"] / R["lump"]["paid"] - 1, 2), "3배 최저 ÷ 넣은 돈")
n = S("2배는 450달러였고요"); need(n, won(LL["x2"]["val"]), "2배 최저"); cond(n, LL["x2"]["date"] == LL["x3"]["date"], "같은 날", "2배")
n = S("1배는 2002년 10월 9일"); need(n, ymd(LL["x1"]["date"]), "1배 최저 날"); need(n, won(LL["x1"]["val"]), "1배 최저"); cond(n, True, "", "1배")
need(S("2026년 10월 15일 값은"), ymd(LP["end"]), "끝"); n = S("1배 16만"); need(n, f"1배 {won(LP['x1'])}", "1배"); need(n, f"2배 {won(LP['x2'])}", "2배"); need(n, f"3배 {won(LP['x3'])}", "3배")
n = S("한 번에 넣은 돈은, 3배가"); need(n, pct(LP["x3_over_x1"]), "3배÷1배"); cond(n, True, "", "3배"); cond(n, True, "", "1배")
# ---- 시작 시점
RO, R25 = R["rolling"], R["rolling25"]
n = S("달마다 시작한 10년 적립 계좌를"); need(n, ym(RO["first_start"]), "첫"); need(n, ym(RO["last_start"]), "끝"); cond(n, RO["years"] == 10, "", "10년")
need(S("모두 211개입니다"), f"{RO['windows']}개", "계좌 수")
n = S("10년 뒤 3배가 1배보다"); need(n, f"{RO['windows']}개 중 {RO['x3_gt_x1']}개", "3배>1배"); cond(n, True, "", "10년"); cond(n, True, "", "3배"); cond(n, True, "", "1배")
n = S("2배가 1배보다 많았던 건"); need(n, f"{RO['x2_gt_x1']}개", "2배>1배"); cond(n, True, "", "2배"); cond(n, True, "", "1배")
n = S("넣은 돈보다 적게 남은 계좌는"); need(n, f"1배 {RO['x1_lt_paid']}개", "1배"); need(n, f"2배 {RO['x2_lt_paid']}개", "2배"); need(n, f"3배 {RO['x3_lt_paid']}개", "3배")
n = S("가장 나빴던 건"); need(n, ym(RO["x3_worst"]["start"]), "3배÷1배 가장 작은 시작"); cond(n, RO["x3_worst"]["start"] == RO["x3_min"]["start"], "3배 값도 가장 작음")
n = S("넣은 돈 6만 500달러가"); need(n, won(RO["x3_min"]["paid"]), "넣은 돈"); need(n, won(RO["x3_min"]["val"]), "3배"); need(n, pct(RO["x3_worst"]["ratio"]), "3배÷1배"); cond(n, True, "", "3배"); cond(n, True, "", "1배")
n = S("가장 좋았던 건 2008년 9월"); need(n, ym(RO["x3_best"]["start"]), "가장 좋은 시작"); need(n, X2(RO["x3_best"]["ratio"]), "3배÷1배"); cond(n, True, "", "3배"); cond(n, True, "", "1배")
n = S("25년 적립 계좌 31개에서는"); need(n, f"{R25['windows']}개", "25년 수"); cond(n, R25["x3_gt_x1"] == R25["windows"] == R25["x3_gt_x2"], "모두 3배 가장 많음", "25년"); cond(n, True, "", "3배")
# ---- 실제 ETF
RE, RS = R["real"], R["real_sim"]
n = S("TQQQ가 생긴 다음 달"); need(n, ym(RE["start"]), "시작"); need(n, won(R["monthly"]), "매달")
need(S("넣은 돈은 10만 달러입니다"), won(RE["paid"]), "넣은 돈")
n = S("QQQ 62만"); need(n, f"QQQ {won(RE['x1'])}", "QQQ"); need(n, f"QLD {won(RE['x2'])}", "QLD"); need(S("TQQQ는 528만"), f"TQQQ는 {won(RE['x3'])}", "TQQQ")
n = S("같은 기간 계산한 3배는"); need(n, won(RS["x3"]), "흉내 3배"); cond(n, RS["x3"] < RE["x3"], "실제보다 적음", "3배")
n = S("실제 TQQQ 계좌도 2022년에"); need(n, pct(R["real_dd2022"]["x3"]["dd"]), "실제 TQQQ 2022 하락"); cond(n, True, "", "2022년")
need(S("실제 QLD 계좌는"), pct(R["real_dd2022"]["x2"]["dd"]), "실제 QLD 2022 하락")
# ---- 정리
n = S("1999년부터 매달 모은 결과"); need(n, X2(M["x3_over_x1"]), "3배÷1배"); cond(n, True, "", "1999년"); cond(n, True, "", "3배"); cond(n, True, "", "1배")
n = S("2001년에는 넣은 돈의"); need(n, pct(D3["vs_paid_low"]), "2001"); cond(n, True, "", "2001년"); n = S("2008년에도 89.5%"); need(n, pct(G3["vs_paid_low"]), "2008"); cond(n, True, "", "2008년")
n = S("계속 앞서기 시작한 건"); need(n, f"{F['x3_ahead_since']['years_before']:.1f}년", "기간"); cond(n, True, "", "3배"); cond(n, True, "", "1배")
n = S("처음에 한 번에 넣었다면, 3배는"); need(n, pct(LP["x3_over_x1"]), "한 번에 3배÷1배"); cond(n, True, "", "3배"); cond(n, True, "", "1배")
n = S("211개 중 20개는"); need(n, f"{RO['windows']}개 중 {RO['x3_lt_paid']}개", "3배 넣은 돈보다 적음"); cond(n, True, "", "10년"); cond(n, True, "", "3배")
# ---- 한계
cond(S("이 기간 나스닥100은"), True, "", "100")
n = S("2배와 3배의 본 실험 값은"); cond(n, True, "", "2배"); cond(n, True, "", "3배")
sys.exit(C.report(HERE.parent / "checklist.md", "reobeoriji-2026-10 숫자 검사 (`backtest/check_numbers.py` v1.0)", f"`backtest/results.json` ({R['version']})"))
