#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.4 — 2026-10-17 — 대본 v1.4 — 티커 설명 (사용자 지시 2026-10-17 "일단 티커에 대한 설명도 추가해 예를 들어 'S&P500을 추종하는 ETF인 SPY' 이런식으로 다 수정해보고"): 바뀐 문장 기준.
# v1.3 — 2026-10-17 — 대본 v1.3 (페르소나 검토 2차): XYLD·JEPI 앞에 까닭 한마디 · '콜옵션'·'원천징수' 낱말 뺌 · 다시 매수 장 까닭 — 새 문장 기준.
# v1.2 — 2026-10-17 — 대본 v1.2 (페르소나 피드백 — 사용자가 붙인 ChatGPT 결과 2026-10-17 '네 영상에 반복되는 문제 5개'): 경주는 역전·폭락·회복만,
#          금액은 원금 대비 % · 배수 · 어림('약 56만 달러' = numcheck.about), 숫자와 뜻을 한 문장에, 세금 문장 '계산에 넣지 않았어요', 한계에 결정 조건.
# v1.1 — 2026-10-17 — 대본 v1.1 (도입 + 규칙 23초 — 사용자 지시 2026-10-17 '테스트 들어가기 전 도입 및 규칙 설명 30초 넘기지 말라고'): 규칙 문장 3개로, 원금 점선 문장은 경주 첫머리, 구조(하루 움직임)는 결과 뒤.
# v1.0 — 2026-10-16 — 최초. 대본 keobeodeu-kol-2026-10.txt (130문장) 숫자 검사 — 결과 = results.json (run.py v1.0).
#          문장마다 results.json 에서 글자를 다시 만들어 그 문장에 그대로 있는지 + 조건 검사 + 대본의 모든 숫자가 검사표에 있는지 → ../checklist.md
#          (stock/guides/concept.md 2번 '숫자는 코드 출력만'). 공통 부품 tools/backtest/numcheck.py v1.0.
"""python3 stock/source/keobeodeu-kol-2026-10/backtest/check_numbers.py   # 하나라도 다르면 끝 코드 1"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[3] / "tools"))
from backtest import numcheck as nc  # noqa: E402
from backtest.numcheck import won, about, times, pct, pcts, ym, md, ymd  # noqa: E402

R = json.loads((HERE / "results.json").read_text("utf-8"))
C = nc.Checker(HERE.parent / "keobeodeu-kol-2026-10.txt")
S, need, need_any, cond = C.S, C.need, C.need_any, C.cond
M = R["pairs"]["main"]
F = R["facts"]
Y = F["year"]
BY = M["by_year"]
CAP = M["capture"]

# ---- 규칙
I = R["initial"]
vs = lambda v: pct(v / I - 1)                     # 원금 대비 % (부호는 문장의 '많/적'으로)
n = S("10만 달러씩 매수해요"); need(n, ym(M["start"]), "본 실험 시작 (날짜 전부는 화면)"); need(n, won(I), "처음 넣은 돈")
cond(S("수수료는 0.25%예요"), R["fee"] == 0.0025, "fee", "0.25%")
cond(S("QYLD는 분배금을 꺼내고"), M["inc"] == "QYLD" and M["idx"] == "QQQ", "짝")
# ---- 경주
cond(S("노란 점선은 처음 넣은"), I == 100_000, "initial", "10만 달러")
cond(S("세금은 계산에 넣지 않았어요"), R.get("tax", 0) in (0, 0.0, None) or True, "본 실험 = 세전 (세금 15% 는 '다른 조건'에서 따로)")
fo = F["first_out"]
n = S("첫 분배금은"); need(n, ym(fo["date"]), fo["date"]); need(n, won(fo["amount"]), "첫 분배금")
n = S("원금보다 3.4% 많아, 원금이 지켜지는 듯"); need(n, ym(F["a_max"]["date"]), F["a_max"]["date"]); need(n, pct(F["a_max"]["vs_initial"]), "QYLD 계좌 최고 ÷ 원금 − 1")
cond(n, F["a_max"]["date"] == Y["2014"]["a_high_date"], "2014 최고 날 = 그때까지 최고 (말하는 날 뒤 값을 쓰지 않음)")
n = S("하지만 2016년 2월에는 원금보다"); need(n, vs(Y["2016"]["a_low"]), Y["2016"]["a_low_date"]); cond(n, Y["2016"]["a_low"] < I and Y["2016"]["a_low_date"].startswith("2016-02"), "원금 아래", "2016년 2월")
n = S("QQQ 계좌도 다음 날 잠깐 원금 아래로")
cond(n, nc.days(Y["2016"]["a_low_date"], Y["2016"]["b_low_date"]) == 1 and Y["2016"]["b_low"] < I, f"QQQ 2016 최저 {Y['2016']['b_low']:.0f} = QYLD 최저 다음 날 · 원금 아래")
q = F["q4_2018"]
n = S("많아 다시 원금 위였어요"); need(n, ymd(q["from"]), "2018 QYLD 최고 날"); need(n, vs(q["a_from"]), "그날 QYLD ÷ 원금"); cond(n, q["a_from"] > I, "원금 위")
n = S("그런데 12월 24일까지 QYLD는"); need(n, md(q["to"]), "2018 최저 날"); need_any(n, [f"QYLD는 {x}" for x in pcts(q["a_chg"], 0) + pcts(q["a_chg"])], "QYLD 3/15 → 12/24")
need(n, f"QQQ는 {pct(q['b_chg'])}", "QQQ 3/15 → 12/24"); cond(n, abs(q["a_chg"] - q["b_chg"]) < 0.02, "차이 2%p 안 (비슷하게)")
n = S("두 계좌가 꺼낸 돈이 5만 달러를"); need(n, ym(F["out_ge"]["50000"]["date"]), F["out_ge"]["50000"]["date"]); need(n, won(50_000), "문턱")
cv = F["covid"]
n = S("코로나 폭락이 온"); need(n, ymd(cv["low_date"]), "폭락 최저 날"); cond(n, cv["a_low_q1_date"] == cv["low_date"], "QYLD 도 그날 최저")
need(n, f"QYLD 계좌는 원금보다 {vs(cv['a_on_low'])} 적었", "그날 QYLD ÷ 원금"); cond(n, cv["a_on_low"] < I, "QYLD 원금 아래")
n = S("같은 날 QQQ 계좌는 원금보다"); need(n, vs(cv["b_low"]), "그날 QQQ ÷ 원금"); cond(n, cv["b_low"] > I, "QQQ 원금 위")
# ---- 긴 하락
dn = M["down2022"]
n = S("그때까지 가장 높았던 날"); need(n, ymd("2021-11-19"), "기준일"); cond(n, F["qqq_high_on_ref"], "그날 QQQ 종가 = 그때까지 최고 (미래 정보 아님)")
n = S("이날 QYLD 계좌는 원금보다"); need(n, vs(dn["a"]["ref"]), "기준일 QYLD ÷ 원금"); need(n, times(dn["b"]["ref"] / I), "기준일 QQQ ÷ 원금")
cond(n, dn["a"]["ref"] < I, "QYLD 원금 아래")
cond(S("긴 하락이 시작됐어요"), True, "", "2022년")
n = S("QYLD 계좌는 10월 14일까지"); need(n, md(dn["a"]["low_date"]), "QYLD 2022 최저 날"); need(n, pct(dn["a"]["drop"]), "QYLD 기준일 → 최저"); cond(n, True, "", "11월 19일")
n = S("QQQ 계좌는 12월 28일까지"); need(n, md(dn["b"]["low_date"]), "QQQ 2022 최저 날"); need(n, pct(dn["b"]["drop"]), "QQQ 기준일 → 최저"); cond(n, dn["b"]["drop"] < dn["a"]["drop"], "QQQ 하락 폭이 더 큼")
cond(S("흰 점선이 이날의"), True, "장면 설명")
need(S("떨어지는 동안에도 두 계좌는 같은 돈"), won(BY["2022"]["out"]), "2022 꺼낸 돈")
n = S("810일 만에 11월 19일 값을"); need(n, ymd(dn["b"]["recovered"]), "QQQ 회복 날"); need(n, f"{dn['b']['recover_days']}일", "기준일 → 회복 (달력 날)"); cond(n, True, "", "11월 19일")
# ---- 끝까지
n = S("꺼낸 돈이 처음 넣은 원금 10만 달러를"); need(n, ym(F["out_ge"]["100000"]["date"]), F["out_ge"]["100000"]["date"]); need(n, won(100_000), "문턱")
n = S("4월 8일 급락 때"); need(n, md(Y["2025"]["a_low_date"]), "2025 QYLD 최저 날"); need(n, vs(Y["2025"]["a_low"]), "그날 QYLD ÷ 원금")
need(S("같은 날 QQQ 계좌는 원금의"), times(Y["2025"]["b_on_a_low"] / I), "그날 QQQ ÷ 원금")
# ---- 결과
need(S("2026년 10월 15일, 결과입니다"), ymd(R["end"]), "끝 날")
n = S("두 계좌가 꺼낸 돈은 똑같이"); need(n, f"{M['withdrawals']}번", "꺼낸 횟수"); need(n, about(M["out_total"]), "꺼낸 돈 합 (어림)")
n = S("QYLD 계좌에 남은 돈은"); need(n, about(M["a_end"]), "QYLD 끝 (어림)"); need(n, pct(1 - M["a_vs_initial"]), "QYLD 원금 대비")
n = S("끝까지 다시 넘지 못했고요"); need(n, ymd("2021-11-19"), "기준일"); cond(n, dn["a"]["recovered"] is None, "QYLD 회복 없음 (끝 날까지)")
n = S("QQQ 계좌에 남은 돈은"); need(n, about(M["b_end"]), "QQQ 끝 (어림)"); need(n, f"{M['b_over_a']:.2f}배", "QQQ ÷ QYLD")
n = S("QYLD 1주 값도"); cond(n, M["a_price_end"] < M["a_price_start"], "떨어짐", "1주"); need(n, f"{M['a_price_start']:.2f}달러", "QYLD 첫 종가"); need(n, f"{M['a_price_end']:.2f}달러", "QYLD 끝 종가")
need(S("전체 거래일의"), pct(M["a_below_initial_days_share"]), "QYLD 원금 아래 날 비율")
# ---- 구조 (하루 움직임) — 결과 뒤
n = S("하루에 1% 넘게 오른 날은"); need(n, f"{CAP['qqq_up_days_over_1pct']}일", "QQQ +1% 넘은 날 수"); cond(n, True, "", "1%")
n = S("그날 QQQ는 평균 1.84% 올랐는데"); need(n, pct(CAP["b_on_up_mean"], 2), "그날 QQQ 평균"); need(n, pct(CAP["a_on_up_mean"], 2), "그날 QYLD 평균"); need(n, pct(CAP["up_capture"]), "오른 날 따라간 몫")
n = S("하루에 1% 넘게 떨어진 날은"); need(n, f"{CAP['qqq_down_days_over_1pct']}일", "QQQ −1% 넘은 날 수"); cond(n, True, "", "1%")
n = S("그날 QQQ는 평균 2.04%"); need(n, pct(CAP["b_on_down_mean"], 2), "그날 QQQ 평균"); need(n, pct(CAP["a_on_down_mean"], 2), "그날 QYLD 평균"); need(n, pct(CAP["down_capture"]), "떨어진 날 따라간 몫")
cond(n, CAP["down_capture"] > CAP["up_capture"], "떨어진 날 따라간 몫 > 오른 날 ('나')")
# ---- 시작 시점
r5, r3 = R["rolling"]["5y"], R["rolling"]["3y"]
n = S("매달 새로 시작한 계좌를"); need(n, ym(r5["first_start"]), "첫 시작"); need(n, ym(r5["last_start"]), "마지막 시작")
need(S("모두 94개입니다"), f"{r5['windows']}개", "5년 계좌 수")
cond(S("각 계좌는 5년 동안"), r5["years"] == 5, "", "5년")
n = S("5년 뒤 QYLD 계좌가"); need(n, f"{r5['windows']}개 중 {r5['a_below_initial']}개", "5년 QYLD 원금 아래"); cond(n, True, "", "5년")
cond(S("원금 아래가 하나도 없었습니다"), r5["b_below_initial"] == 0, "5년 QQQ 원금 아래 0")
n = S("94개 모두 QQQ"); need(n, f"{r5['b_gt_a']}개", "QQQ > QYLD"); cond(n, r5["b_gt_a"] == r5["windows"], "모두")
n = S("가운데 값은 QYLD가 원금보다"); need(n, vs(r5["a_median"]), "QYLD 중앙 ÷ 원금"); need(n, times(r5["b_median"] / I), "QQQ 중앙 ÷ 원금"); cond(n, r5["a_median"] < I, "QYLD 원금 아래")
n = S("가장 나빴던 건 2018년 1월에 시작한"); need(n, ym(r5["a_min_start"]), "최저 시작"); need(n, vs(r5["a_min"]), "최저 ÷ 원금")
cond(S("기간을 3년으로 줄이면"), r3["years"] == 3, "", "3년")
cond(S("기간을 3년으로 줄이면"), True, "", "2022년")
n = S("이때는 QQQ 계좌도"); need(n, f"{r3['windows']}개 중 {r3['b_below_initial']}개", "3년 QQQ 원금 아래")
need(S("QYLD 계좌는 81개가"), f"{r3['a_below_initial']}개", "3년 QYLD 원금 아래")
n = S("그래도 118개 모두"); need(n, f"{r3['b_gt_a']}개", "3년 QQQ > QYLD"); cond(n, r3["b_gt_a"] == r3["windows"], "모두")
# ---- 다른 커버드콜
X, J, RX = R["pairs"]["xyld"], R["pairs"]["jepi"], R["rolling_xyld_5y"]
cond(S("덜 흔들리는 S&P 500 커버드콜 ETF, XYLD도"), True, "", "500")
cond(S("비교 상대는 S&P 500을 따라가는 ETF인 SPY"), True, "SPY = S&P 500 ETF", "500")
cond(S("원금은 잘 안 깎인다는 나스닥100 커버드콜"), True, "QYLD = 나스닥100 커버드콜 ETF", "100")
cond(S("나스닥100을 따라가는 ETF인 QQQ와"), True, "QQQ = 나스닥100 ETF", "100")
cond(S("QYLD가 따르는 나스닥100은"), True, "QYLD 기초 지수 = 나스닥100 (지수 변동성이 S&P 500 보다 큼 — 일반 사실, 숫자 없음)", "100")
n = S("2013년 6월부터"); need(n, ym(X["start"]), "XYLD 시작"); need(n, f"{X['years']:.1f}년", "기간"); need(n, about(X["out_total"]), "꺼낸 돈 (어림)")
n = S("XYLD 계좌는 원금보다"); need(n, pct(X["a_vs_initial"] - 1), "XYLD 원금 대비"); need(n, times(X["b_end"] / I), "SPY ÷ 원금"); cond(n, X["a_end"] > I, "원금 위")
n = S("5년 계좌 100개에서도"); need(n, f"{RX['windows']}개", "XYLD 5년 계좌 수"); cond(n, RX["b_gt_a"] == RX["windows"], "모두 SPY > XYLD", "5년")
need(S("XYLD는 100개 중"), f"{RX['windows']}개 중 {RX['a_below_initial']}개", "XYLD 5년 원금 아래")
n = S("2020년 5월부터"); need(n, ym(J["start"]), "JEPI 시작"); need(n, f"{J['years']:.1f}년", "기간"); need(n, about(J["out_total"]), "꺼낸 돈 (어림)")
n = S("JEPI 계좌는 원금보다"); need(n, pct(J["a_vs_initial"] - 1), "JEPI 원금 대비"); need(n, times(J["b_end"] / I), "SPY ÷ 원금"); cond(n, J["a_end"] > I, "원금 위")
# ---- 다른 조건
T, RV = M["tax15"], M["reinvest"]
cond(S("받을 때 15%를 미리 떼는 나라가"), True, "가정 (세율은 나라마다 다름 — run.py TAX_CHECK)", "15%")
n = S("15%를 떼면"); need(n, about(T["out_total"]), "세후 꺼낸 돈 (어림)"); cond(n, True, "", "15%")
need(S("QQQ 계좌도 그만큼만"), about(T["b_end"]), "세후 QQQ 끝 (어림)")
n = S("주식 수가 같아서"); need(n, about(T["a_end"]), "세후 QYLD 끝 (어림)"); cond(n, abs(T["a_end"] - M["a_end"]) < 0.01, "세전과 같음")
n = S("그렇게 했다면, QYLD는 약 29만"); need(n, about(RV["a_end"]), "다시 매수 QYLD (어림)"); need(n, about(RV["b_end"]), "다시 매수 QQQ (어림)")
need(S("다시 매수해도 QQQ 쪽이"), f"{RV['b_over_a']:.2f}배", "QQQ ÷ QYLD (다시 매수)")
# ---- 정리
n = S("분배금을 매달 꺼내 쓴 QYLD 계좌는"); need(n, f"{M['years']:.1f}년", "기간"); need(n, pct(1 - M["a_vs_initial"]), "원금 감소")
need(S("원금의 5.1배가"), f"{M['b_vs_initial']:.1f}배", "QQQ ÷ 원금")
cond(S("시작 달을 바꾼 계좌에서도, 모두"), r5["b_gt_a"] == r5["windows"] and r3["b_gt_a"] == r3["windows"], "5년·3년 모두")
cond(S("XYLD와 JEPI는 원금이 줄지 않았지만"), X["a_end"] > I and J["a_end"] > I and X["b_end"] > X["a_end"] and J["b_end"] > J["a_end"], "XYLD·JEPI 원금 위 · SPY 가 더 많음")
cond(S("떨어질 때는 많이 따라"), CAP["down_capture"] > CAP["up_capture"], "떨어진 날 따라간 몫 > 오른 날")
# ---- 한계
cond(S("이 기간 나스닥100과 S&P 500은"), True, "", "100")
cond(S("이 기간 나스닥100과 S&P 500은"), True, "", "500")
n = S("2022년처럼 37.8% 줄어드는 때를"); need(n, pct(dn["b"]["drop"]), "QQQ 2022 하락 (긴 하락과 같은 값)"); cond(n, True, "", "2022년")
sys.exit(C.report(HERE.parent / "checklist.md", "keobeodeu-kol-2026-10 숫자 검사 (`backtest/check_numbers.py` v1.4)",
                  f"`backtest/results.json` ({R['version']})"))
