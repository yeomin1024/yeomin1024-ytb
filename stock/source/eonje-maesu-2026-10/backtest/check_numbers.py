#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v3.2 — 2026-10-17 — 대본 v3.2 (페르소나 검토 2차 — 비교가 바뀔 때 까닭 한마디 · 전문용어(골든 크로스·모멘텀) 대신 풀어서 · '10달' → '10개월'): 새 문장 기준·조건.
# v3.1 — 2026-10-17 — 대본 v3.1 (페르소나 피드백 — 사용자가 붙인 ChatGPT 검토 2026-10-17 '네 영상에 반복되는 문제 5개'): 경주 해설을 대표 장면만
#          (해마다 판정 문장 뺌), 무작위 계좌를 만든 방법(같은 매도 규칙 · 날짜만 무작위 · 기다린 날 수는 그 방법 기록에서) 조건 검사, 결과 + 뜻을 한 문장,
#          수수료는 도입에서 한계로, 범위만 말하는 방법(mom21·x20)은 result(mean=False).
# v3.0 — 2026-10-16 — 대본 v3.0 (성공률 — +5% 가 −2% 보다 먼저 · 무작위 매수 2천 개와 견줌) 숫자 검사. 결과 = barrier/results.json (barrier/run.py v2.0).
#          사용자 지시 2026-10-16 "그럼 신호 없이 무작위로 매수 했을 때랑 비교하는 거지? 그게 맞는거 같은데 그리고 m을 1~2%로 해야 엄격하게 봐서 성공 확률이
#          줄지 m은 내가 말한 범위에서 적절하게 정해서 영상 만들어봐". 문장마다 results.json 에서 글자를 다시 만들어 그 문장에 그대로 있는지 + 조건 검사 +
#          대본의 모든 숫자가 검사표에 있는지 → ../checklist.md (stock/guides/concept.md 2번 '숫자는 코드 출력만').
# (v2.2 — 2026-10-16 — 대본 v2.1 (끝 값 비교, results.json = run.py v3.0) — 커밋 28e1b7b 에 그대로.)
"""cd stock/source/eonje-maesu-2026-10/backtest && python3 check_numbers.py   # 하나라도 다르면 끝 코드 1

%는 소수 한 자리 (반올림). 날짜 사실(연속 성공·실패, 신호가 없던 기간, 해마다 판정)은 results.json rules.<방법>.facts 에서.
"""
import json
import re
import sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[3] / "tools"))
import srt_tool  # noqa: E402

R = json.loads((HERE / "barrier" / "results.json").read_text("utf-8"))
SENT = srt_tool.parse_txt(HERE.parent / "eonje-maesu-2026-10.txt")
P, RU, CK, CM = R["params"], R["rules"], R["checks"], R["choose_m"]
ORDER = ["m1", "hi20", "mom21", "x20", "gc520", "drop1", "rsi40", "vix20", "dd20_5", "dd5"]
TREND = {"hi20", "mom21", "x20", "gc520"}
NATIVE = {2: "두", 3: "세", 4: "네", 5: "다섯", 6: "여섯", 7: "일곱", 8: "여덟", 9: "아홉", 10: "열"}
assert set(ORDER) == set(P["rules"]) - {"any"}, "방법 목록이 results.json 과 다름"


def p1(x):
    return f"{abs(x) * 100:.1f}%"


def ym(d):
    y, m, _ = d.split("-")
    return f"{int(y)}년 {int(m)}월"


def days(a, b):
    return (date.fromisoformat(b) - date.fromisoformat(a)).days


checks = []                                       # (문장 번호, 기대 글자, 근거, 맞나 — 글자가 아니라 조건일 때)


def S(anchor):
    """anchor 가 든 문장 번호 (하나만 있어야 함)."""
    hits = [i + 1 for i, s in enumerate(SENT) if anchor in s]
    if len(hits) != 1:
        raise SystemExit(f"[CHECK] 문장 찾기 '{anchor}' → {len(hits)}개 {hits} (하나여야 함)")
    return hits[0]


def need(n, text, why):
    checks.append((n, text, why, None))


def cond(n, ok, why, token=""):
    checks.append((n, token, why, bool(ok)))


def F(k):
    return RU[k]["facts"]


def year(k, y):
    v = F(k)["by_year"][str(y)]
    return v["wins"], v["losses"]


def yrs(k, years):
    w = l = 0
    for y in years:
        v = F(k)["by_year"].get(str(y), {"wins": 0, "losses": 0}); w += v["wins"]; l += v["losses"]
    return w, l


def yr_count(k, anchor, years, fmt, tokens=()):
    """연도별 판정 문장: fmt 의 {d}=판정 수 {w}=성공 {l}=실패 → 문장에 그대로 있어야 함."""
    w, l = yrs(k, years)
    n = S(anchor)
    need(n, fmt.format(d=w + l, w=w, l=l), f"{k} {'+'.join(map(str, years))} 판정 {w}-{l}")
    for tok in tokens:
        cond(n, True, "", tok)


def yr_words(k, anchor, years, fmt, tokens=()):
    w, l = yrs(k, years)
    n = S(anchor)
    need(n, fmt.format(D=NATIVE[w + l], Wn=NATIVE[w]), f"{k} {'+'.join(map(str, years))} 판정 {w}-{l}")
    for tok in tokens:
        cond(n, True, "", tok)


def yr_all(k, anchor, years, cnt):
    w, l = yrs(k, years)
    n = S(anchor)
    need(n, f"{NATIVE[cnt]} 번", f"{k} {years} 판정 수"); cond(n, (w, l) == (cnt, 0), f"{k} {years} {w}-{l} (모두 성공)", f"{years[0]}년")


def ye_rate(k, anchor, y):
    ye = F(k)["year_end"][y]
    n = S(anchor)
    need(n, p1(ye["rate"]), f"{k} {ye['date']} 성공률"); need(n, p1(ye["rand"]), f"{k} {ye['date']} 무작위 평균"); cond(n, True, "", f"{y}년")


def lead_lag(k, which, anchor, ym_, token):
    x = F(k)[which]
    n = S(anchor)
    need(n, p1(x["rate"]), f"{k} {'가장 앞선' if which == 'lead' else '가장 뒤진'} 날 {x['date']} 성공률"); need(n, p1(x["rand"]), "그날 무작위 평균")
    cond(n, x["date"].startswith(ym_), x["date"], token)
    return x


def cash(k, anchor, ym_, dmin, dmax, tokens):
    c = F(k)["longest_cash"]
    n = S(anchor)
    cond(n, c["after"].startswith(ym_) and dmin <= days(c["after"], c["buy"]) - 1 < dmax, f"{k} 가장 긴 현금 {c} (달력 {days(c['after'], c['buy']) - 1}일)", tokens[0])
    for tok in tokens[1:]:
        cond(n, True, "", tok)


def covid(k, anchor, fmt):
    cv = F(k)["covid"]
    n = S(anchor)
    need(n, fmt.format(d=cv["wins"] + cv["losses"], w=cv["wins"], l=cv["losses"]), f"{k} {cv['from']}~{cv['to']} 판정"); cond(n, True, "", "2020년")


def streak(k, which, anchor, cnt, a_ym, b_ym, tokens):
    st = F(k)["streak"][which]
    n = S(anchor)
    cond(n, st["n"] == cnt and st["from_buy"].startswith(a_ym) and st["to_hit"].startswith(b_ym), f"{k} 연속 {which} {st}", tokens[0])
    for tok in tokens[1:]:
        cond(n, True, "", tok)


def result(k, a_res, a_rand, mean=True):
    """결과 문장 (판정 N번 중 W번 성공, X%) + 무작위 문장 (평균 · 90% 범위 · 범위 안). mean=False: 평균은 말하지 않음 (카드에만)."""
    r = RU[k]
    n = S(a_res)
    need(n, f"판정 {r['decided']}번 중 {r['wins']}번 성공", f"{k} 판정·성공 수")
    need(n, p1(r["success_rate"]), f"{k} 성공률")
    m = S(a_rand)
    if mean:
        need(m, p1(r["rand_mean"]), f"{k} 무작위 평균 (계좌 {P['runs']}개)")
    need(m, p1(r["rand_p5"]), f"{k} 무작위 5번째")
    need(m, p1(r["rand_p95"]), f"{k} 무작위 95번째")
    cond(m, not r["outside_90"], f"{k} 무작위 90% 범위 안")


# ---- 도입 (규칙 — 정한 조건)
n = S("많이 쓰는 매수 신호 10가지가")
need(n, f"{len(ORDER)}가지", "매수 방법 수")
n = S("2016년부터 지금까지, SPY로")
cond(n, P["start"].startswith("2016"), f"기간 시작 {P['start']}", "2016년")
n = S("성공은 매수한 값보다 5% 오르는 것")
need(n, f"{P['n'] * 100:.0f}%", "성공 +n")
need(n, f"{P['m'] * 100:.0f}%", "실패 −m")
n = S("비교 상대는 같은 매도 규칙으로, 날짜만 무작위로")
cond(n, P["runs"] == 2000, f"무작위 계좌 {P['runs']}개", "2천")
cond(n, "같은 매도 규칙" in P["baseline"] and "날짜만 무작위" in P["baseline"], f"params.baseline: {P['baseline']}")

# ---- 1 매달 첫 거래일
k = "m1"; f = F(k); r = RU[k]
cond(S("무작위 계좌의 매도 뒤 기다리는 날 수는"), "기다리는 거래일 수를 그 방법의 실제 기다림에서 무작위로 뽑음" in P["baseline"],
     "params.baseline — 기다리는 날 수 = 그 방법의 실제 기다림에서 뽑음 (barrier/run.py vs_random · entry.method_waits)")
ye = f["year_end"]["2021"]
n = S("2021년 말에는 성공률 56.1%로")
need(n, p1(ye["rate"]), f"m1 {ye['date']} 성공률"); need(n, p1(ye["rand"]), f"m1 {ye['date']} 무작위 평균")
cond(n, ye["rate"] > ye["rand"], "높았다", "2021년")
w, l = year(k, 2022)
n = S("그런데 2022년에는 판정 12번 중 11번이 실패")
need(n, f"판정 {w + l}번 중 {l}번이 실패", "m1 2022 판정"); cond(n, True, "", "2022년")
n = S("2023년부터는 무작위 평균과 거의 붙어서")
cond(n, f["max_abs_diff_since_2023"] <= 0.02, f"2023년부터 무작위 평균과 차이 최대 {f['max_abs_diff_since_2023'] * 100:.2f}%p (≤ 2)", "2023년")
n = S("결과는 80번 중 37번 성공")
need(n, f"{r['decided']}번 중 {r['wins']}번 성공", "m1 판정·성공 수"); need(n, p1(r["success_rate"]), "m1 성공률")
need(n, p1(r["rand_mean"]), f"m1 무작위 평균 (계좌 {P['runs']}개)")
cond(n, 0 < r["rand_mean"] - r["success_rate"] < 0.02, f"조금 낮았다 ({(r['success_rate'] - r['rand_mean']) * 100:+.1f}%p)", "조금 낮았어요")
n = S("회색 띠는 무작위 계좌 90%가 들어간 범위, 41.5%")
cond(n, True, "90% 범위 = 5번째~95번째", "90%")
need(n, p1(r["rand_p5"]), "m1 무작위 5번째"); need(n, p1(r["rand_p95"]), "m1 무작위 95번째")
cond(S("이 띠 안이면 무작위와 차이가 없다는 뜻인데"), not r["outside_90"], "m1 범위 안")

# ---- 2 20일 신고가 (추세 신호 시작)
n = S("두 번째부터 다섯 번째까지는 오를 때")
cond(n, ORDER[1:5] == ["hi20", "mom21", "x20", "gc520"] and all(x in TREND for x in ORDER[1:5]), "2~5번 = 추세 신호")
k = "hi20"; f = F(k)
cond(S("두 번째, 20일 신고가 돌파 매수"), "20 거래일" in P["rules"][k]["condition"], P["rules"][k]["condition"], "20")
cond(S("종가가 지난 20 거래일의 가장 높은 종가를"), "20" in P["rules"][k]["condition"], P["rules"][k]["condition"], "20")
ye_rate(k, "2019년 말 성공률은 58.8%로", "2019")
cond(S("2019년 말 성공률은 58.8%로"), f["year_end"]["2019"]["rate"] > f["year_end"]["2019"]["rand"], "높았다")
cash(k, "2022년 4월에 매도한 뒤로는 석 달 가까이", "2022-04", 75, 92, ["2022년 4월"])
yr_count(k, "그해 판정은 6번 중 5번이 실패", [2022], "{d}번 중 {l}번이 실패")
cond(S("판정이 20번 쌓인 뒤로는, 성공률이 무작위 평균보다 낮은 날이"), f["share_days_ahead"] == 1.0, f"hi20 판정 20번 뒤 무작위보다 앞선 날 몫 {f['share_days_ahead']}", "20번")
result(k, "결과는 판정 63번 중 31번", "무작위 평균 47.1%, 범위 41.3%")

# ---- 3 1개월 모멘텀
k = "mom21"; f = F(k)
cond(S("오늘 종가가 21 거래일 전 종가보다"), "21" in P["rules"][k]["condition"], P["rules"][k]["condition"], "21")
cond(S("세 번째는 신고가가 아니어도, 한 달 전보다"), "21" in P["rules"][k]["condition"], "21 거래일 ≈ 한 달 (v3.2 — '1개월 모멘텀' 낱말 뺌)")
x = lead_lag(k, "lead", "2020년 6월에는 성공률 63.0%로", "2020-06", "2020년 6월")
cond(S("2020년 6월에는 성공률 63.0%로"), x["rate"] - x["rand"] > 0.1, f"크게 앞섬 ({(x['rate'] - x['rand']) * 100:+.1f}%p)")
yr_count(k, "하지만 2022년에는 판정 12번 중 10번이 실패", [2022], "판정 {d}번 중 {l}번이 실패", ["2022년"])
cash(k, "2025년 2월 말에 매도한 뒤로는 두 달 넘게", "2025-02", 60, 90, ["2025년 2월"])
result(k, "결과는 판정 81번 중 42번", "무작위 범위 43.3%에서 52.6%의 위쪽 끝", mean=False)
cond(S("무작위 범위 43.3%에서 52.6%의 위쪽 끝"), RU[k]["rand_p95"] - RU[k]["success_rate"] < 0.01 and not RU[k]["outside_90"], "95번째와 1%p 안 · 범위 안")

# ---- 4 20일선 돌파
k = "x20"; f = F(k)
cond(S("네 번째는 차트에 많이 그리는 20일 평균선"), "20일" in P["rules"][k]["condition"], P["rules"][k]["condition"], "20일")
cond(S("종가가 20일 평균을 아래에서 위로"), "20일" in P["rules"][k]["condition"], "", "20일")
streak(k, "win", "2016년 7월부터 2018년 1월까지 다섯 번 연속 성공", 5, "2016-07", "2018-01", ["2016년 7월", "2018년 1월"])
x = lead_lag(k, "lead", "2021년 12월에는 성공률 64.7%로", "2021-12", "2021년 12월")
cond(S("2021년 12월에는 성공률 64.7%로"), x["rate"] - x["rand"] > 0.1, f"크게 앞섬 ({(x['rate'] - x['rand']) * 100:+.1f}%p)")
st = f["streak"]["loss"]
cond(S("그 뒤 2022년 7월까지는 여섯 번 연속 실패"), st["n"] == 6 and st["to_hit"].startswith("2022-07") and st["from_buy"] >= "2021-12-01", f"x20 연속 실패 {st}", "2022년 7월")
cond(S("판정이 20번 쌓인 뒤로는, 무작위 평균보다 낮은 날이 없었습니다"), f["share_days_ahead"] == 1.0, f"x20 앞선 날 몫 {f['share_days_ahead']}", "20번")
result(k, "결과는 판정 71번 중 37번", "그래도 무작위 범위 40.3%에서 54.3% 안이라", mean=False)
cond(S("지금까지 본 네 가지 중 가장 높아요"), max(ORDER[:4], key=lambda x: RU[x]["success_rate"]) == "x20", "1~4번 중 x20 가장 높음")

# ---- 5 골든 크로스 5·20
k = "gc520"; f = F(k)
cond(S("다섯 번째는 평균선 두 개를 함께"), "5일" in P["rules"][k]["condition"] and "20일" in P["rules"][k]["condition"], P["rules"][k]["condition"])
n = S("짧은 5일 평균이 긴 20일 평균을 아래에서 위로")
cond(n, True, P["rules"][k]["condition"], "5일"); cond(n, True, "", "20일")
c = f["longest_cash"]
n = S("2017년 9월에 매도한 뒤, 다음 매수는 2018년 2월")
cond(n, c["after"].startswith("2017-09") and c["buy"].startswith("2018-02"), f"gc520 가장 긴 현금 {c}", "2017년 9월"); cond(n, True, "", "2018년 2월")
lg = lead_lag(k, "lag", "2022년 7월에는 성공률 40.0%로", "2022-07", "2022년 7월")
cond(S("2022년 7월에는 성공률 40.0%로"), lg["rate"] < lg["rand"], "낮았다")
st = f["streak"]["loss"]
cond(S("바로 전에 여섯 번 연속 실패가"), st["n"] == 6 and st["to_hit"] <= lg["date"], f"gc520 연속 실패 {st}")
st = f["streak"]["win"]
cond(S("그 뒤로는 2023년 6월까지 다섯 번 연속 성공"), st["n"] == 5 and st["to_hit"].startswith("2023-06") and st["from_buy"] >= lg["date"][:7], f"gc520 연속 성공 {st}", "2023년 6월")
yr_count(k, "2024년부터는 판정 12번 중 7번이 성공", [2024, 2025, 2026], "판정 {d}번 중 {w}번이 성공", ["2024년"])
result(k, "결과는 판정 50번 중 25번", "무작위 평균 47.4%, 범위 38.6%")
cond(S("결과는 판정 50번 중 25번"), abs(RU[k]["success_rate"] - 0.5) < 1e-12, "딱 50%")
n = S("판정이 10가지 중 가장 적어서, 범위도 넓었습니다")
cond(n, min(ORDER, key=lambda x: RU[x]["decided"]) == k and (RU[k]["rand_p95"] - RU[k]["rand_p5"]) > (RU["m1"]["rand_p95"] - RU["m1"]["rand_p5"]), "판정 수 가장 적음 · 범위가 m1 보다 넓음", "10가지")

# ---- 6 하루 −1%
cond(S("여섯 번째부터는 떨어질 때 매수하는"), all(x not in TREND for x in ORDER[5:]), "6~10번 = 떨어질 때 매수")
k = "drop1"; f = F(k)
cond(S("여섯 번째, 하루에 1% 이상 떨어지면"), "−1%" in P["rules"][k]["condition"], P["rules"][k]["condition"], "1%")
yr_count(k, "2018년 한 해에만 판정 12번 중 8번이 실패", [2018], "판정 {d}번 중 {l}번이 실패", ["2018년"])
lg = lead_lag(k, "lag", "2019년 1월에는 성공률 35.0%로", "2019-01", "2019년 1월")
cond(S("2019년 1월에는 성공률 35.0%로"), lg["rand"] - lg["rate"] > 0.1, f"크게 뒤짐 ({(lg['rate'] - lg['rand']) * 100:+.1f}%p)")
yr_count(k, "2022년에도 20번 중 13번이 실패", [2022], "{d}번 중 {l}번이 실패", ["2022년"])
cond(S("판정이 20번 쌓인 뒤로는, 무작위 평균보다 높은 날이 하루도"), f["share_days_ahead"] == 0.0, f"drop1 앞선 날 몫 {f['share_days_ahead']}", "20번")
result(k, "결과는 판정 95번 중 44번", "무작위 평균은 46.8%, 범위는 40.7%")

# ---- 7 RSI 40
k = "rsi40"; f = F(k)
cond(S("일곱 번째, RSI 40 아래 매수"), "< 40" in P["rules"][k]["condition"], P["rules"][k]["condition"], "40")
cond(S("RSI는 최근 14일 동안"), "(14)" in P["rules"][k]["condition"], "RSI(14)", "14일")
cond(S("40 아래면 많이 떨어진 상태로"), "< 40" in P["rules"][k]["condition"], "", "40")
x = lead_lag(k, "lead", "2019년 11월에는 성공률 61.9%로", "2019-11", "2019년 11월")
cond(S("2019년 11월에는 성공률 61.9%로"), x["rate"] - x["rand"] > 0.1, f"크게 앞섬 ({(x['rate'] - x['rand']) * 100:+.1f}%p)")
covid(k, "2020년 코로나 폭락 때는 판정 7번 중 5번이 실패", "판정 {d}번 중 {l}번이 실패")
cash(k, "2020년 11월에 매도한 뒤로는 10개월 넘게", "2020-11", 304, 335, ["2020년 11월", "10개월"])
yr_count(k, "2022년에는 판정 14번 중 11번이 실패", [2022], "판정 {d}번 중 {l}번이 실패", ["2022년"])
need(S("그래서 주식을 든 날은 35%뿐이었습니다"), f"{RU[k]['invested_share'] * 100:.0f}%", "rsi40 주식 보유 비율")
result(k, "결과는 판정 62번 중 30번", "무작위 평균은 46.7%, 범위는 38.0%")

# ---- 8 VIX 20
k = "vix20"; f = F(k)
cond(S("여덟 번째, 공포지수 VIX 20 이상"), "≥ 20" in P["rules"][k]["condition"], P["rules"][k]["condition"], "20")
c = f["longest_cash"]
n = S("2016년 11월에 매도한 뒤로는 1년 넘게")
cond(n, c["after"].startswith("2016-11") and days(c["after"], c["buy"]) - 1 > 365, f"vix20 가장 긴 현금 {c}", "2016년 11월"); cond(n, True, "", "1년")
w, l = yrs(k, [2020])
n = S("2020년에는 판정 22번 중 11번이 성공, 딱 절반")
need(n, f"판정 {w + l}번 중 {w}번이 성공", "vix20 2020"); cond(n, w == l, "절반", "2020년")
yr_count(k, "2022년에는 24번 중 18번이 실패였고, 8월부터", [2022], "{d}번 중 {l}번이 실패", ["2022년"])
streak(k, "loss", "2022년에는 24번 중 18번이 실패였고, 8월부터", 6, "2022-08", "2022-10", ["8월", "10월"])
yr_count(k, "2023년부터는 판정 23번 중 14번이 성공으로", [2023, 2024, 2025, 2026], "판정 {d}번 중 {w}번이 성공", ["2023년"])
w, l = yrs(k, [2023, 2024, 2025, 2026]); cond(S("2023년부터는 판정 23번 중 14번이 성공으로"), w / (w + l) > 0.5, f"vix20 2023~ {w}-{l} 절반 넘음")
result(k, "결과는 판정 101번 중 48번", "무작위 평균 47.3%와 거의 같았고")
cond(S("무작위 평균 47.3%와 거의 같았고"), abs(RU[k]["vs_rand_pp"]) < 0.005, f"vix20 무작위 평균과 차이 {RU[k]['vs_rand_pp'] * 100:+.2f}%p")

# ---- 9 20일 고점 −5%
k = "dd20_5"; f = F(k)
n = S("아홉 번째, 최근 20 거래일 고점보다 5%")
cond(n, "20 거래일" in P["rules"][k]["condition"] and "0.95" in P["rules"][k]["condition"], P["rules"][k]["condition"], "20"); cond(n, True, "", "5%")
c = f["longest_cash"]
n = S("2016년 7월에 매도한 뒤, 다음 신호는 2018년 2월")
cond(n, c["after"].startswith("2016-07") and c["buy"].startswith("2018-02"), f"dd20_5 가장 긴 현금 {c}", "2016년 7월"); cond(n, True, "", "2018년 2월")
covid(k, "2020년 코로나 폭락 때는 판정 9번 중 6번이 실패", "판정 {d}번 중 {l}번이 실패")
yr_count(k, "2022년에도 15번 중 11번이 실패", [2022], "{d}번 중 {l}번이 실패", ["2022년"])
n = S("주식을 든 날은 23%로, 10가지 중 가장 적었습니다")
need(n, f"{RU[k]['invested_share'] * 100:.0f}%", "dd20_5 주식 보유 비율")
cond(n, min(ORDER, key=lambda x: RU[x]["invested_share"]) == k, "보유 비율 가장 적음", "10가지")
result(k, "결과는 판정 59번 중 29번", "무작위 평균은 46.5%, 범위는 38.0%")

# ---- 10 고점 −5%
k = "dd5"; f = F(k)
cond(S("마지막 열 번째, 그때까지 최고 종가보다 5%"), "0.95" in P["rules"][k]["condition"], P["rules"][k]["condition"], "5%")
cond(S("아홉 번째보다 길게 본 저점 매수"), "20 거래일" in P["rules"]["dd20_5"]["condition"] and "20 거래일" not in P["rules"][k]["condition"], "dd20_5 = 최근 20 거래일 고점 · dd5 = 그때까지 최고 종가 (더 긺)")
c = f["longest_cash"]
n = S("이 방법도 2016년 7월에 매도한 뒤로는 1년 반 넘게")
cond(n, c["after"].startswith("2016-07") and 1.5 < (days(c["after"], c["buy"]) - 1) / 365.25 < 2.0, f"dd5 가장 긴 현금 {c}", "2016년 7월"); cond(n, True, "", "1년")
w, l = yrs(k, [2019]); n = S("그해 판정 다섯 번이 모두 성공했거든요"); need(n, "다섯 번", "dd5 2019 판정 수"); cond(n, (w, l) == (5, 0), f"dd5 2019 {w}-{l} (모두 성공)")
ye_rate(k, "2019년 말 성공률은 56.5%로", "2019")
cond(S("2019년 말 성공률은 56.5%로"), f["year_end"]["2019"]["rate"] > f["year_end"]["2019"]["rand"], "높았다")
covid(k, "2020년 코로나 폭락 때는 10번 중 6번이 실패", "{d}번 중 {l}번이 실패")
yr_count(k, "2022년에는 26번 중 19번이 실패로", [2022], "{d}번 중 {l}번이 실패", ["2022년"])
cond(S("2022년에는 26번 중 19번이 실패로"), max(ORDER, key=lambda x: yrs(x, [2022])[1]) == k, "2022 실패 수 10가지 중 가장 많음", "10가지")
yr_count(k, "2023년부터는 23번 중 14번이 성공해", [2023, 2024, 2025, 2026], "{d}번 중 {w}번이 성공", ["2023년"])
w, l = yrs(k, [2023, 2024, 2025, 2026]); cond(S("2023년부터는 23번 중 14번이 성공해"), w / (w + l) > 0.5 and yrs(k, [2022])[1] > yrs(k, [2022])[0], f"dd5 2023~ {w}-{l} 절반 넘음 (2022 은 실패가 더 많음 → 다시)")
result(k, "결과는 판정 94번 중 45번", "무작위 평균은 47.1%, 범위는 40.8%")

# ---- 종합
cond(S("10가지 결과를 한 번에"), len(ORDER) == 10, "", "10가지")
cond(S("점은 각 방법의 성공률, 회색 띠는"), True, "90% 범위", "90%")
rk = R["rank_by_success"]
n = S("가장 높은 건 20일선 돌파 매수")
cond(n, rk[0] == "x20", f"1위 {rk[0]}", "20일선"); need(n, p1(RU["x20"]["success_rate"]), "x20 성공률")
n = S("가장 낮은 건 매달 첫 거래일 매수")
cond(n, rk[-1] == "m1", f"10위 {rk[-1]}"); need(n, p1(RU["m1"]["success_rate"]), "m1 성공률")
cond(S("위쪽 다섯 개 중 네 개는"), sum(x in TREND for x in rk[:5]) == 4, f"위 5개 {rk[:5]}")
n = S("하지만 10가지 모두 무작위 범위 안이라, 무작위 매수와 차이가 없었어요")
cond(n, not any(RU[x]["outside_90"] for x in ORDER), "모두 범위 안", "10가지")
n = S("가장 높은 20일선 돌파도, 무작위 계좌 가운데 13%는")
need(n, f"{RU['x20']['share_random_ge'] * 100:.0f}%", "x20 이상인 무작위 계좌 몫"); cond(n, True, "", "20일선")

# ---- 다른 조건
c1, c15, cl = CK["m0.010"], CK["m0.015"], CK["long1994_2015"]
above = lambda c: [x for x in ORDER if c[x]["outside_90"] and c[x]["rate"] > c[x]["rand_p95"]]
below = lambda c: [x for x in ORDER if c[x]["outside_90"] and c[x]["rate"] < c[x]["rand_p5"]]
cond(S("실패 기준 2%가 너무 느슨했던"), P["m"] == 0.02, "본 실험 m = 2%", "2%")
n = S("1%로 더 엄격하게 하면")
need(n, p1(c1["every_day"]), "m 1% 아무 날 매수 성공률"); cond(n, True, "m = 1%", "1%")
n = S("이때는 20일선 돌파만 범위 위로")
cond(n, above(c1) == ["x20"] and not below(c1), f"m 1%: 위 {above(c1)} 아래 {below(c1)}", "20일선")
n = S("1.5%에서는 범위를 벗어난 방법이 없었고요")
cond(n, not above(c15) and not below(c15), "m 1.5%: 범위 밖 없음", "1.5%")
n = S("기간을 1994년부터 2015년으로 바꿔 봤어요")
cond(n, True, "이번 10년 = 2016~", "10년")
cond(n, cl["start"].startswith("1994") and cl["end"].startswith("2015"), f"{cl['start']}~{cl['end']}", "1994년"); cond(n, True, "", "2015년")
n = S("이 기간엔 20일선 돌파가 33.3%로")
need(n, p1(cl["x20"]["rate"]), "1994~2015 x20 성공률")
cond(n, min(ORDER, key=lambda x: cl[x]["rate"]) == "x20", "1994~2015 x20 가장 낮음", "10가지"); cond(n, True, "", "20일선")
n = S("이 기간에도 10가지 모두 무작위 범위 안")
cond(n, not above(cl) and not below(cl), "1994~2015 범위 밖 없음", "10가지")

# ---- 정리
n = S("추세 신호가 이번 10년에는 조금 앞섰어요")
cond(n, all(RU[x]["vs_rand_pp"] > 0 for x in TREND), "2016~ 추세 4개 무작위 평균보다 위", "10년")
n = S("하지만 그 전 22년에는")
cond(n, round(days(cl["start"], cl["end"]) / 365.25) == 22, f"{cl['start']}~{cl['end']} ≈ 22년", "22년")
cond(n, sum(cl[x]["rate"] < cl[x]["rand_mean"] for x in TREND) == 2, "1994~2015 추세 4개 중 2개 무작위 평균보다 낮음")
cond(S("2022년처럼 계속 떨어진 해에는"), all(year(x, 2022)[1] > year(x, 2022)[0] for x in ORDER), "2022 모든 방법 실패 > 성공", "2022년")
n = S("성공률을 크게 바꾼 건 매수 신호가 아니라")
spread = max(RU[x]["success_rate"] for x in ORDER) - min(RU[x]["success_rate"] for x in ORDER)
ev2, ev1 = CM["m"]["0.0200"]["every_day"], CM["m"]["0.0100"]["every_day"]
cond(n, (ev2 - ev1) > spread, f"m 2%→1% 아무 날 성공률 {ev2:.3f}→{ev1:.3f} 차이 > 방법 사이 차이 {spread:.3f}")

# ---- 한계
cond(S("이 결과는 SPY 하나, 2016년부터의 자료"), P["start"].startswith("2016"), "", "2016년")
need(S("판정 다음 날 매도하며 수수료"), f"{P['cost'] * 100:.2f}%", "수수료 params.cost (v3.1 도입 → 한계)")
cond(S("그래서 성공인데 손해, 실패인데 이익인 거래도"), sum(RU[x]["label_ret_mismatch"] for x in ORDER) > 0, f"판정과 수익 부호가 다른 거래 {sum(RU[x]['label_ret_mismatch'] for x in ORDER)}개")

# ---- 검사
rows, bad = [], 0
for n, text, why, ok in checks:
    s = SENT[n - 1]
    hit = (text in s) if ok is None else (ok and (not text or text in s))
    bad += not hit
    rows.append(f"| {n} | {s} | `{text}` | {why} | {'✅' if hit else '❌'} |")
nums_bad = []
covered = {}
for n, text, _, _ in checks:
    covered.setdefault(n, set()).update(re.findall(r"\d[\d,.]*", text))
for n, s in enumerate(SENT, 1):
    for tok in re.findall(r"\d[\d,.]*", s):
        tok = tok.rstrip(",.")
        if tok not in covered.get(n, set()):
            nums_bad.append(f"문장 {n}: '{tok}' — {s}")
L = ["# eonje-maesu-2026-10 숫자 검사 (`backtest/check_numbers.py` v3.2)", "",
     f"- 대본 `eonje-maesu-2026-10.txt` {len(SENT)}문장 · 결과 `backtest/barrier/results.json` ({R['version']}, {R['made_at']})",
     f"- 검사 {len(checks)}개 · 맞음 {len(checks) - bad} · 틀림 {bad} · 검사표에 없는 숫자 {len(nums_bad)}", "",
     "| 문장 | 대본 | 찾는 글자 | 근거 | 결과 |", "|---:|---|---|---|---|"] + rows
if nums_bad:
    L += ["", "## 검사표에 없는 숫자", ""] + [f"- {x}" for x in nums_bad]
(HERE.parent / "checklist.md").write_text("\n".join(L) + "\n", "utf-8")
print(f"[CHECK] sentences={len(SENT)} numbers={len(checks)} ok={len(checks) - bad} bad={bad} uncovered={len(nums_bad)} → ../checklist.md")
for x in nums_bad[:40]:
    print("  ", x)
for r in rows:
    if "❌" in r:
        print("  ", r)
sys.exit(1 if bad or nums_bad else 0)
