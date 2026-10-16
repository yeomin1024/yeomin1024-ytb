#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v2.1 — 2026-10-16 — 문장 번호 대신 문장 안 글자(앵커)로 찾음 + 대본 v2.1 에 더한 문장 11개 검사.
# (v2.0 — 2026-10-16 — 대본 v2.0(매수 신호 10가지 × 같은 매도 규칙, SPY 2016~2026-10) 숫자 검사. 문장마다 results.json(run.py v3.0)에서
#          글자를 다시 만들어 그 문장에 그대로 있는지 + 대본의 모든 숫자가 검사표나 '규칙 값' 목록에 있는지 → ../checklist.md
#          (stock/guides/concept.md 2번 '숫자는 코드 출력만'). (v1.0 — v1 대본용 — stock/source/_old/eonje-maesu-2026-10-v1/))
"""cd stock/source/eonje-maesu-2026-10/backtest && python3 check_numbers.py   # 하나라도 다르면 끝 코드 1

말로 읽는 금액은 천 달러 단위 반올림 ('5만 3천 달러' = $52,997), %는 소수 한 자리.
"""
import json
import re
import sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[3] / "tools"))
import srt_tool  # noqa: E402

R = json.loads((HERE / "results.json").read_text("utf-8"))
SENT = srt_tool.parse_txt(HERE.parent / "eonje-maesu-2026-10.txt")
RU, TR, BH, RE, F, CK = R["rules"], R["trades"], R["buy_and_hold"], R["reentry"], R["facts"], R["checks"]


def p1(x):
    return f"{abs(x) * 100:.1f}%"


def usd(v):
    t = int(round(v / 1000.0))
    man, cheon = divmod(t, 10)
    return f"{man}만 {cheon}천 달러" if cheon else f"{man}만 달러"


def usd_short(v):                                # '4만 4천' (뒤에 '달러' 없이 이어 말할 때)
    return usd(v).replace(" 달러", "")


def kdate(d, year=True):
    y, m, dd = d.split("-")
    return (f"{int(y)}년 " if year else "") + f"{int(m)}월 {int(dd)}일"


def kym(d):
    y, m, _ = d.split("-")
    return f"{int(y)}년 {int(m)}월"


def years(a, b):
    return (date.fromisoformat(b) - date.fromisoformat(a)).days / 365.25


def tr_of(rule, buy=None, sell=None):
    for t in TR[rule]:
        if (buy is None or t["buy_date"] == buy) and (sell is None or t["sell_date"] == sell):
            return t
    raise KeyError((rule, buy, sell))


def next_buy(rule, sell_date):
    T = TR[rule]
    for a, b in zip(T, T[1:]):
        if a["sell_date"] == sell_date:
            return b
    raise KeyError((rule, sell_date))


def rank(k):
    return R["rank_by_final"].index(k) + 1


checks = []                                       # (문장 번호, 기대 글자, 근거, 맞나 — 글자가 아니라 조건일 때)


def S(anchor):
    """anchor 가 든 문장 번호 (하나만 있어야 함 — 대본을 고쳐도 검사가 엉뚱한 문장을 보지 않게, v2.1)."""
    hits = [i + 1 for i, s in enumerate(SENT) if anchor in s]
    if len(hits) != 1:
        raise SystemExit(f"[CHECK] 문장 찾기 '{anchor}' → {len(hits)}개 {hits} (하나여야 함)")
    return hits[0]


def need(n, text, why):
    checks.append((n, text, why, None))


def cond(n, ok, why, token=""):
    checks.append((n, token, why, bool(ok)))


# ---- 규칙 (값이 아니라 정한 조건 — 결과가 아님)
P = R["params"]
cond(S('2016년부터 지금까지, AI가 짠 코드로 백테스트해서 확인해 보겠습니다.'), P["start"].startswith("2016"), "기간 시작 2016", "2016년")
cond(S('모두 1만 달러로 시작하고, 배당은 다시 투자합니다.'), P["capital"] == 10000, "시작 돈 $10,000", "1만 달러")
need(S('사고팔 때마다 수수료 0.25%를 뗍니다.'), f"{P['cost'] * 100:.2f}%", "수수료 params.cost")
need(S('산 뒤 가장 높았던 종가보다 10% 떨어지면, 다음 날 매도합니다.'), f"{P['trail'] * 100:.0f}%", "매도 params.trail")
need(S('그래서 많이 쓰는 매수 신호 10가지를 같은 조건으로 시험해 보겠습니다.'), f"{len(P['rules'])}가지", "규칙 수")
need(S('시험하는 건 S&P 500을 따라가는 ETF, SPY입니다.'), "S&P 500", "지수 이름")
need(S('매도 규칙은 10가지 모두 같습니다.'), f"{len(P['rules'])}가지", "규칙 수")
cond(S('지난 1년 가장 높았던 종가를 넘어서는 날, 매수합니다.'), True, "52주 = 252 거래일 = 1년", "1년")

# ---- 1 매달 첫 거래일
t = tr_of("m1", buy=TR["m1"][0]["buy_date"])
need(S('2016년 1월 4일 첫 매수가 2018년 2월까지 34.8% 올랐습니다.'), kdate(t["buy_date"]), "m1 첫 매수 날")
need(S('2016년 1월 4일 첫 매수가 2018년 2월까지 34.8% 올랐습니다.'), kym(t["sell_date"]), "m1 첫 거래 판 달")
need(S('2016년 1월 4일 첫 매수가 2018년 2월까지 34.8% 올랐습니다.'), p1(t["ret"]), "m1 첫 거래 수익률")
t = next(t for t in TR["m1"] if t["buy_date"].startswith("2020-03"))
need(S('2020년 3월 코로나 폭락 때는 7.2% 손해를 보고 매도했어요.'), kym(t["buy_date"]), "m1 2020-03 매수")
need(S('2020년 3월 코로나 폭락 때는 7.2% 손해를 보고 매도했어요.'), p1(t["ret"]), "m1 2020-03 거래 손해")
cond(S('2020년 3월 코로나 폭락 때는 7.2% 손해를 보고 매도했어요.'), t["ret"] < 0, "손해")
t2 = next_buy("m1", t["sell_date"])
cond(S('다음 달 첫날 다시 매수했고, 이 거래가 75.1% 올랐습니다.'), t2["buy_date"] == "2020-04-01", "다음 달 첫날 다시 매수 (2020-04-01)")
need(S('다음 달 첫날 다시 매수했고, 이 거래가 75.1% 올랐습니다.'), p1(t2["ret"]), "m1 2020-04 거래 수익률")
need(S('13번 매수해서, 끝 값은 4만 1천 달러입니다.'), f"{RU['m1']['buys']}번", "m1 매수 수")
need(S('13번 매수해서, 끝 값은 4만 1천 달러입니다.'), usd(RU["m1"]["final"]), "m1 끝 값")
need(S('그대로 둔 계좌 4만 6천 달러보다는 적어요.'), usd(BH["final"]), "BUY & HOLD 끝 값")
cond(S('그대로 둔 계좌 4만 6천 달러보다는 적어요.'), RU["m1"]["final"] < BH["final"], "m1 < BUY & HOLD")

# ---- 2 52주 신고가
need(S('두 번째, 52주 신고가 돌파 매수입니다.'), "52주", "규칙 이름 (252 거래일)")
t = tr_of("hi52", sell="2020-02-28")
b = next_buy("hi52", "2020-02-28")
need(S('2020년 2월 28일에 매도한 뒤, 다시 산 건 8월 19일이었어요.'), kdate(t["sell_date"]), "hi52 2020 매도 날")
need(S('2020년 2월 28일에 매도한 뒤, 다시 산 건 8월 19일이었어요.'), kdate(b["buy_date"], year=False), "hi52 다시 매수 날")
need(S('판 값보다 13.8% 비싸게 다시 산 셈입니다.'), p1(b["buy_price"] / t["sell_price"] - 1), "hi52 판 값 대비 다시 산 값")
b2 = next_buy("hi52", "2022-02-23")
need(S('2022년 2월에 판 뒤로는 1년 넘게 신호가 없었고요.'), "2022년 2월", "hi52 2022-02 매도")
cond(S('2022년 2월에 판 뒤로는 1년 넘게 신호가 없었고요.'), years("2022-02-23", b2["buy_date"]) > 1.0, f"1년 넘게 신호 없음 (다음 매수 {b2['buy_date']})", "1년")
need(S('7번 매수해서, 끝 값은 2만 3천 달러입니다.'), f"{RU['hi52']['buys']}번", "hi52 매수 수")
need(S('7번 매수해서, 끝 값은 2만 3천 달러입니다.'), usd(RU["hi52"]["final"]), "hi52 끝 값")

# ---- 3 12개월 모멘텀
need(S('세 번째, 12개월 모멘텀 매수입니다.'), "12개월", "규칙 이름")
cond(S('오늘 종가가 1년 전 종가보다 높으면 매수합니다.'), True, "규칙 조건 252 거래일 = 1년", "1년")
t = next(t for t in TR["mom12"] if t["buy_date"].startswith("2022-05"))
need(S('2022년 5월에 산 주식은 13.3% 손해를 보고 매도했어요.'), kym(t["buy_date"]), "mom12 2022-05 매수")
need(S('2022년 5월에 산 주식은 13.3% 손해를 보고 매도했어요.'), p1(t["ret"]), "mom12 2022-05 거래 손해")
b = next_buy("mom12", t["sell_date"])
need(S('1년 전보다 낮은 날이 이어져, 다시 산 건 2023년 5월이었습니다.'), kym(b["buy_date"]), "mom12 다시 매수 달")
cond(S('1년 전보다 낮은 날이 이어져, 다시 산 건 2023년 5월이었습니다.'), True, "규칙 조건 1년", "1년")
need(S('13번 매수해서, 끝 값은 2만 6천 달러입니다.'), f"{RU['mom12']['buys']}번", "mom12 매수 수")
need(S('13번 매수해서, 끝 값은 2만 6천 달러입니다.'), usd(RU["mom12"]["final"]), "mom12 끝 값")

# ---- 4 200일선
need(S('네 번째, 200일 이동평균선 돌파 매수입니다.'), "200일", "규칙 이름")
need(S('종가가 200일 평균을 아래에서 위로 뚫는 날, 매수합니다.'), "200일", "규칙 조건")
t = tr_of("ma200", sell="2020-03-10")
b = next_buy("ma200", "2020-03-10")
need(S('2020년 3월에 매도하고, 평균선을 다시 넘은 5월 말에 샀어요.'), kym(t["sell_date"]), "ma200 2020-03 매도")
cond(S('2020년 3월에 매도하고, 평균선을 다시 넘은 5월 말에 샀어요.'), b["buy_date"] >= "2020-05-20" and b["buy_date"][:7] == "2020-05", f"5월 말 다시 매수 ({b['buy_date']})", "5월")
need(S('이 거래가 42.2% 올라, 이 규칙에서 가장 큰 수익이었습니다.'), p1(b["ret"]), "ma200 그 거래 수익률")
cond(S('이 거래가 42.2% 올라, 이 규칙에서 가장 큰 수익이었습니다.'), abs(b["ret"] - RU["ma200"]["best_trade"]) < 1e-12, "이 규칙에서 가장 큰 수익")
need(S('판 값보다는 평균 4.9% 비싸게 다시 샀어요.'), p1(RE["ma200"]["mean_change"]), "ma200 다시 산 값 평균")
need(S('11번 매수해서, 끝 값은 2만 6천 달러입니다.'), f"{RU['ma200']['buys']}번", "ma200 매수 수")
need(S('11번 매수해서, 끝 값은 2만 6천 달러입니다.'), usd(RU["ma200"]["final"]), "ma200 끝 값")

# ---- 5 골든 크로스
need(S('50일 평균선이 200일 평균선을 위로 뚫으면 매수합니다.'), "50일", "규칙 조건")
need(S('50일 평균선이 200일 평균선을 위로 뚫으면 매수합니다.'), "200일", "규칙 조건")
need(S('판 거래 4번이 모두 수익이었어요.'), f"{RU['gc']['trades_closed']}번", "gc 판 거래 수")
cond(S('판 거래 4번이 모두 수익이었어요.'), RU["gc"]["win_rate"] == 1.0, "모두 수익")
b = next_buy("gc", "2023-10-30")
need(S('2023년 10월에 판 뒤, 다시 산 건 2025년 7월이었어요.'), "2023년 10월", "gc 2023-10 매도")
need(S('2023년 10월에 판 뒤, 다시 산 건 2025년 7월이었어요.'), kym(b["buy_date"]), "gc 다시 매수 달")
need(S('판 값보다 49.3% 비싼 값이었습니다.'), p1(b["buy_price"] / tr_of("gc", sell="2023-10-30")["sell_price"] - 1), "gc 판 값 대비 다시 산 값")
need(S('5번 매수해서, 끝 값은 2만 3천 달러입니다.'), f"{RU['gc']['buys']}번", "gc 매수 수")
need(S('5번 매수해서, 끝 값은 2만 3천 달러입니다.'), usd(RU["gc"]["final"]), "gc 끝 값")

# ---- 6 급락 다음 날
need(S('하루에 2% 넘게 떨어지면, 다음 날 매수합니다.'), "2%", "규칙 조건")
need(S('10가지 가운데 가장 많은 14번을 매수했어요.'), "10가지", "규칙 수")
need(S('10가지 가운데 가장 많은 14번을 매수했어요.'), f"{RU['drop2']['buys']}번", "drop2 매수 수")
cond(S('10가지 가운데 가장 많은 14번을 매수했어요.'), RU["drop2"]["buys"] == max(r["buys"] for r in RU.values()), "가장 많음")
t = next(t for t in TR["drop2"] if t["buy_date"].startswith("2018-12"))
need(S('2018년 12월에는 산 뒤 13.1% 떨어져 매도했고요.'), kym(t["buy_date"]), "drop2 2018-12 매수")
need(S('2018년 12월에는 산 뒤 13.1% 떨어져 매도했고요.'), p1(t["ret"]), "drop2 2018-12 거래 손해")
t = tr_of("drop2", buy="2020-03-19")
need(S('2020년 3월 19일에 다시 산 거래는 80.3% 올랐습니다.'), kdate(t["buy_date"]), "drop2 2020-03-19 매수")
need(S('2020년 3월 19일에 다시 산 거래는 80.3% 올랐습니다.'), p1(t["ret"]), "drop2 그 거래 수익률")
need(S('끝 값은 4만 달러입니다.'), usd(RU["drop2"]["final"]), "drop2 끝 값")

# ---- 7 RSI
need(S('일곱 번째, RSI 30 아래 과매도 매수입니다.'), "30", "규칙 조건")
need(S('RSI는 최근 14일 동안 오른 폭과 내린 폭을 견준 숫자예요.'), "14일", "RSI(14)")
need(S('30 아래면 많이 팔린 상태로 보고, 매수합니다.'), "30", "규칙 조건")
t = tr_of("rsi30", buy="2020-03-24")
need(S('2020년 3월 24일, 바닥 다음 날 매수한 거래가 77.2% 올랐어요.'), kdate(t["buy_date"]), "rsi30 2020-03-24 매수")
cond(S('2020년 3월 24일, 바닥 다음 날 매수한 거래가 77.2% 올랐어요.'), F["spy_2020_bottom"]["date"] == "2020-03-23", "바닥 다음 날 (2020 바닥 = 2020-03-23)")
need(S('2020년 3월 24일, 바닥 다음 날 매수한 거래가 77.2% 올랐어요.'), p1(t["ret"]), "rsi30 그 거래 수익률")
b = next_buy("rsi30", "2023-10-30")
need(S('2023년 10월에 판 뒤로는 1년 넘게 기다렸고요.'), "2023년 10월", "rsi30 2023-10 매도")
cond(S('2023년 10월에 판 뒤로는 1년 넘게 기다렸고요.'), years("2023-10-30", b["buy_date"]) > 1.0, f"1년 넘게 기다림 ({b['buy_date']})", "1년")
need(S('9번 매수해서, 끝 값은 4만 4천 달러입니다.'), f"{RU['rsi30']['buys']}번", "rsi30 매수 수")
need(S('9번 매수해서, 끝 값은 4만 4천 달러입니다.'), usd(RU["rsi30"]["final"]), "rsi30 끝 값")

# ---- 8 VIX
need(S('여덟 번째, 공포지수 VIX 30 이상 매수입니다.'), "30", "규칙 조건")
need(S('첫 매수가 2018년 2월이라, 처음 2년은 현금으로 기다렸습니다.'), kym(RU["vix30"]["first_buy"]), "vix30 첫 매수 달")
cond(S('첫 매수가 2018년 2월이라, 처음 2년은 현금으로 기다렸습니다.'), 1.9 < years(P["start"], RU["vix30"]["first_buy"]) < 2.3, "처음 2년 현금", "2년")
t = tr_of("vix30", buy="2020-03-18")
need(S('2020년 3월 18일에 산 거래는 80.7% 올랐어요.'), kdate(t["buy_date"]), "vix30 2020-03-18 매수")
need(S('2020년 3월 18일에 산 거래는 80.7% 올랐어요.'), p1(t["ret"]), "vix30 그 거래 수익률")
need(S('11번 매수해서, 끝 값은 3만 4천 달러입니다.'), f"{RU['vix30']['buys']}번", "vix30 매수 수")
need(S('11번 매수해서, 끝 값은 3만 4천 달러입니다.'), usd(RU["vix30"]["final"]), "vix30 끝 값")

# ---- 9 고점 −20%
need(S('아홉 번째, 고점보다 20% 떨어지면 사는 큰 하락 매수입니다.'), "20%", "규칙 조건")
need(S('그때까지 가장 높았던 종가보다 20% 이상 낮으면 매수해요.'), "20%", "규칙 조건")
t = tr_of("dip20", buy="2020-03-18")
need(S('2020년 3월 18일에 산 거래가 80.7% 올랐습니다.'), kdate(t["buy_date"]), "dip20 2020-03-18 매수")
need(S('2020년 3월 18일에 산 거래가 80.7% 올랐습니다.'), p1(t["ret"]), "dip20 그 거래 수익률")
cond(S('그런데 2023년 10월에 판 뒤로는 한 번도 사지 못했어요.'), F["dip20_after_last_sale"]["last_sale"] == "2023-10-30" and not TR["dip20"][-1]["open"], "2023-10 판 뒤 매수 없음", "2023년 10월")
need(S('그런데 2023년 10월에 판 뒤로는 한 번도 사지 못했어요.'), "2023년 10월", "dip20 마지막 매도")
need(S('2025년 4월에도 고점보다 19.0%까지만 떨어졌기 때문입니다.'), kym(F["dip20_after_last_sale"]["min_dd_date"]), "그 뒤 가장 깊은 하락 달")
need(S('2025년 4월에도 고점보다 19.0%까지만 떨어졌기 때문입니다.'), p1(F["dip20_after_last_sale"]["min_dd"]), "그 뒤 가장 깊은 하락")
cond(S('3년 가까이 현금으로 기다려, 끝 값은 2만 4천 달러입니다.'), 2.75 < F["dip20_after_last_sale"]["years_to_end"] < 3.0, "3년 가까이", "3년")
need(S('3년 가까이 현금으로 기다려, 끝 값은 2만 4천 달러입니다.'), usd(RU["dip20"]["final"]), "dip20 끝 값")

# ---- 10 고점 −10%
need(S('마지막 열 번째, 고점보다 10% 떨어지면 사는 저점 매수입니다.'), "10%", "규칙 조건")
need(S('판 뒤에도 고점보다 10% 아래면, 바로 다음 날 다시 매수해요.'), "10%", "규칙 조건")
m = [t for t in TR["dip10"] if t["buy_date"].startswith("2020-03") and t["ret"] < 0]
cond(S('2020년 3월에는 7.2%, 8.3% 손해로 두 번 매도했어요.'), len(m) == 2, "2020-03 두 번 손해 매도")
need(S('2020년 3월에는 7.2%, 8.3% 손해로 두 번 매도했어요.'), "2020년 3월", "dip10 2020-03")
for t in m:
    need(S('2020년 3월에는 7.2%, 8.3% 손해로 두 번 매도했어요.'), p1(t["ret"]), f"dip10 {t['buy_date']} 거래 손해")
t = tr_of("dip10", buy="2020-03-18")
need(S('3월 18일에 또 매수했고, 이 거래가 80.7% 올랐습니다.'), kdate(t["buy_date"], year=False), "dip10 2020-03-18 매수")
need(S('3월 18일에 또 매수했고, 이 거래가 80.7% 올랐습니다.'), p1(t["ret"]), "dip10 그 거래 수익률")
t = TR["dip10"][-1]
cond(S('2025년 4월 급락 때도 매수해서, 지금 54.9% 수익 중이에요.'), t["open"] and t["buy_date"].startswith("2025-04"), "2025-04 매수 · 보유 중")
need(S('2025년 4월 급락 때도 매수해서, 지금 54.9% 수익 중이에요.'), kym(t["buy_date"]), "dip10 2025-04 매수")
need(S('2025년 4월 급락 때도 매수해서, 지금 54.9% 수익 중이에요.'), p1(t["ret"]), "dip10 보유 중 수익률")
need(S('13번 매수해서, 끝 값은 5만 3천 달러입니다.'), f"{RU['dip10']['buys']}번", "dip10 매수 수")
need(S('13번 매수해서, 끝 값은 5만 3천 달러입니다.'), usd(RU["dip10"]["final"]), "dip10 끝 값")
need(S('그대로 둔 계좌 4만 6천 달러보다 많아요.'), usd(BH["final"]), "BUY & HOLD 끝 값")
cond(S('그대로 둔 계좌 4만 6천 달러보다 많아요.'), RU["dip10"]["final"] > BH["final"], "dip10 > BUY & HOLD")

# ---- 종합
need(S('10가지 결과를 한 번에 보겠습니다.'), "10가지", "규칙 수")
cond(S('1위는 고점보다 10% 떨어지면 사는 저점 매수, 5만 3천 달러입니다.'), R["rank_by_final"][0] == "dip10", "1위 = dip10", "1위")
need(S('1위는 고점보다 10% 떨어지면 사는 저점 매수, 5만 3천 달러입니다.'), "10%", "dip10 조건")
need(S('1위는 고점보다 10% 떨어지면 사는 저점 매수, 5만 3천 달러입니다.'), usd(RU["dip10"]["final"]), "dip10 끝 값")
cond(S('2위 RSI 4만 4천, 3위 매달 첫 거래일 4만 1천 달러예요.'), R["rank_by_final"][1] == "rsi30" and R["rank_by_final"][2] == "m1", "2위 rsi30, 3위 m1", "2위")
need(S('2위 RSI 4만 4천, 3위 매달 첫 거래일 4만 1천 달러예요.'), "3위", "순위")
need(S('2위 RSI 4만 4천, 3위 매달 첫 거래일 4만 1천 달러예요.'), usd_short(RU["rsi30"]["final"]), "rsi30 끝 값")
need(S('2위 RSI 4만 4천, 3위 매달 첫 거래일 4만 1천 달러예요.'), usd(RU["m1"]["final"]), "m1 끝 값")
need(S('그대로 둔 계좌 4만 6천 달러를 넘은 건 하나뿐이었습니다.'), usd(BH["final"]), "BUY & HOLD 끝 값")
cond(S('그대로 둔 계좌 4만 6천 달러를 넘은 건 하나뿐이었습니다.'), R["rules_above_buy_and_hold"] == ["dip10"], "넘은 건 하나")
bottom = R["rank_by_final"][-5:]
trend = {"hi52", "mom12", "ma200", "gc"}
cond(S('아래 다섯 개 중 네 개는, 오를 때 사는 추세 규칙이었어요.'), sum(k in trend for k in bottom) == 4, f"아래 5개 {bottom} 중 추세 4개", "다섯")
cond(S('2020년 2월 28일, 10가지 모두 같은 날 매도했어요.'), all(any(t["sell_date"] == "2020-02-28" for t in TR[k]) for k in TR), "2020-02-28 10가지 모두 매도", "10가지")
need(S('2020년 2월 28일, 10가지 모두 같은 날 매도했어요.'), kdate("2020-02-28"), "같은 매도 날")
ch = sorted(RE[k]["mean_change"] for k in trend)
need(S('추세 규칙 네 개는 판 값보다 평균 4.0%에서 15.9% 비싸게 다시 샀어요.'), p1(ch[0]), "추세 규칙 다시 산 값 평균 (가장 작은)")
need(S('추세 규칙 네 개는 판 값보다 평균 4.0%에서 15.9% 비싸게 다시 샀어요.'), p1(ch[-1]), "추세 규칙 다시 산 값 평균 (가장 큰)")
cond(S('추세 규칙 네 개는 판 값보다 평균 4.0%에서 15.9% 비싸게 다시 샀어요.'), ch[0] > 0, "모두 비싸게", "네 개")
need(S('저점 매수는 평균 1.4% 싸게, 대부분 다음 날 바로 다시 샀고요.'), p1(RE["dip10"]["mean_change"]), "dip10 다시 산 값 평균")
cond(S('저점 매수는 평균 1.4% 싸게, 대부분 다음 날 바로 다시 샀고요.'), RE["dip10"]["mean_change"] < 0, "싸게")
gaps = [b["buy_i"] - a["sell_i"] for a, b in zip(TR["dip10"], TR["dip10"][1:])]
cond(S('저점 매수는 평균 1.4% 싸게, 대부분 다음 날 바로 다시 샀고요.'), sum(g == 1 for g in gaps) > len(gaps) / 2, f"대부분 다음 날 ({sum(g == 1 for g in gaps)}/{len(gaps)})")
need(S('큰 하락 매수는 7.3% 싸게 샀지만, 주식을 든 날이 42%뿐이었습니다.'), p1(RE["dip20"]["mean_change"]), "dip20 다시 산 값 평균")
need(S('큰 하락 매수는 7.3% 싸게 샀지만, 주식을 든 날이 42%뿐이었습니다.'), f"{RU['dip20']['invested_share'] * 100:.0f}%", "dip20 주식 보유 비율")

# ---- 다른 조건
def above(name):
    c = CK[name]
    bh = c.get("_buy_and_hold", BH)["final"]
    return sum(c[k]["final"] > bh for k in c if not k.startswith("_"))


need(S('5%로 바꾸면, 그대로 둔 계좌를 넘은 규칙이 하나도 없었어요.'), "5%", "확인 trail5")
cond(S('5%로 바꾸면, 그대로 둔 계좌를 넘은 규칙이 하나도 없었어요.'), above("trail5") == 0, "−5% 넘은 규칙 0", "하나도")
need(S('15%나 20%로 하면 세 개씩 넘었습니다.'), "15%", "확인 trail15")
need(S('15%나 20%로 하면 세 개씩 넘었습니다.'), "20%", "확인 trail20")
cond(S('15%나 20%로 하면 세 개씩 넘었습니다.'), above("trail15") == 3 and above("trail20") == 3, "−15%·−20% 세 개씩", "세 개")
cond(S('수수료를 0으로 해도 두 개뿐이었고요.'), above("cost0") == 2, "수수료 0 두 개", "0으로")

# ---- 정리
cond(S('이번 10년 동안, 신호를 기다린 규칙 10개 중 9개는 그대로 둔 계좌보다 적었습니다.'), True, "기간 약 10년", "10년")
need(S('이번 10년 동안, 신호를 기다린 규칙 10개 중 9개는 그대로 둔 계좌보다 적었습니다.'), "10개", "규칙 수")
cond(S('이번 10년 동안, 신호를 기다린 규칙 10개 중 9개는 그대로 둔 계좌보다 적었습니다.'), 10 - len(R["rules_above_buy_and_hold"]) == 9, "9개는 적음", "9개")
need(S('넘은 하나도, 떨어지면 바로 다시 사서 주식을 97% 들고 있던 규칙이었어요.'), f"{RU['dip10']['invested_share'] * 100:.0f}%", "dip10 주식 보유 비율")
need(S('그대로 둔 계좌는 2020년 3월에 33.7% 떨어지는 걸 견뎌야 했고요.'), kym(BH["max_dd_date"]), "BUY & HOLD 최대 낙폭 달")
need(S('그대로 둔 계좌는 2020년 3월에 33.7% 떨어지는 걸 견뎌야 했고요.'), p1(BH["max_dd"]), "BUY & HOLD 최대 낙폭")
cond(S('이 결과는 지난 10년의 자료입니다.'), True, "기간 약 10년", "10년")

# ---- v2.1 더한 문장
def wins(k):
    c = [t for t in TR[k] if not t["open"]]
    return len(c), sum(t["ret"] > 0 for t in c)


n_, w_ = wins("m1")
need(S("판 거래 12번 중 7번이 수익이었어요."), f"{n_}번 중 {w_}번", "m1 판 거래·이긴 거래")
n_, w_ = wins("hi52")
need(S("판 거래 6번 중 4번이 수익이었고"), f"{n_}번 중 {w_}번", "hi52 판 거래·이긴 거래")
need(S("판 거래 6번 중 4번이 수익이었고"), f"{RU['hi52']['invested_share'] * 100:.0f}%", "hi52 주식 보유 비율")
m20 = [t for t in TR["mom12"] if t["buy_date"].startswith("2020-03")]
cond(S("2020년 3월에는 두 번 연속 손해를"), len(m20) == 2 and all(t["ret"] < 0 for t in m20)
     and TR["mom12"].index(m20[1]) == TR["mom12"].index(m20[0]) + 1, "mom12 2020-03 두 거래 연속 손해", "2020년 3월")
n_, w_ = wins("mom12")
need(S("판 거래 12번 중 6번만"), f"{n_}번 중 {w_}번", "mom12 판 거래·이긴 거래")
t = next(t for t in TR["ma200"] if t["buy_date"].startswith("2018-11"))
need(S("2018년 11월에 산 주식은"), kym(t["buy_date"]), "ma200 2018-11 매수")
need(S("2018년 11월에 산 주식은"), p1(t["ret"]), "ma200 그 거래 손해")
need(S("그래서 주식을 든 날이"), f"{RU['gc']['invested_share'] * 100:.0f}%", "gc 주식 보유 비율")
b20 = [t["buy_date"] for t in TR["drop2"] if t["buy_date"].startswith("2020-03")]
cond(S("보름 사이 세 번이나"), len(b20) == 3 and (date.fromisoformat(b20[-1]) - date.fromisoformat(b20[0])).days <= 15,
     f"drop2 2020-03 매수 {b20}", "2020년 3월")
n_, w_ = wins("rsi30")
need(S("판 거래 8번 중 5번"), f"{n_}번 중 {w_}번", "rsi30 판 거래·이긴 거래")
t = next(t for t in TR["vix30"] if t["buy_date"].startswith("2024-08"))
need(S("2024년 8월에도 VIX가"), kym(t["buy_date"]), "vix30 2024-08 매수")
need(S("2024년 8월에도 VIX가"), "30", "규칙 조건")
need(S("2024년 8월에도 VIX가"), p1(t["ret"]), "vix30 그 거래 수익률")
n_, w_ = wins("dip20")
need(S("판 거래 5번 중 4번"), f"{n_}번 중 {w_}번", "dip20 판 거래·이긴 거래")
b22 = [t for t in TR["dip10"] if t["buy_date"].startswith("2022")]
cond(S("한 해에 네 번 매수"), len(b22) == 4, f"dip10 2022 매수 {len(b22)}번", "2022년")

# ---- 검사
rows, bad = [], 0
for n, text, why, ok in checks:
    s = SENT[n - 1]
    hit = (text in s) if ok is None else ok
    bad += not hit
    rows.append(f"| {n} | {s} | `{text}` | {why} | {'✅' if hit else '❌'} |")
# 대본의 모든 숫자가 검사표에 있나
nums_bad = []
covered = {}
for n, text, _, _ in checks:
    covered.setdefault(n, set()).update(re.findall(r"\d[\d,.]*", text))
for n, s in enumerate(SENT, 1):
    for tok in re.findall(r"\d[\d,.]*", s):
        tok = tok.rstrip(",.")
        if tok not in covered.get(n, set()):
            nums_bad.append(f"문장 {n}: '{tok}' — {s}")
L = ["# eonje-maesu-2026-10 숫자 검사 (`backtest/check_numbers.py` v2.0)", "",
     f"- 대본 `eonje-maesu-2026-10.txt` {len(SENT)}문장 · 결과 `backtest/results.json` ({R['version']}, {R['made_at']})",
     f"- 검사 {len(checks)}개 · 맞음 {len(checks) - bad} · 틀림 {bad} · 검사표에 없는 숫자 {len(nums_bad)}", "",
     "| 문장 | 대본 | 찾는 글자 | 근거 | 결과 |", "|---:|---|---|---|---|"] + rows
if nums_bad:
    L += ["", "## 검사표에 없는 숫자", ""] + [f"- {x}" for x in nums_bad]
(HERE.parent / "checklist.md").write_text("\n".join(L) + "\n", "utf-8")
print(f"[CHECK] numbers={len(checks)} ok={len(checks) - bad} bad={bad} uncovered={len(nums_bad)} → ../checklist.md")
for x in nums_bad[:30]:
    print("  ", x)
for r in rows:
    if "❌" in r:
        print("  ", r)
sys.exit(1 if bad or nums_bad else 0)
