#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-11-04 — 박씨 길 ④: '지수가 최고가를 되찾은 날(2024-01-19) 다시 매수' → 'D4 부터 1년(365일) 현금으로 기다린 뒤(2024-07-25) 다시 매수'.
#   까닭: 대본 문장 79 「박씨처럼 1년 동안 현금으로 기다렸다면, 이자로 5% 느는 데 그쳤을 것입니다」와 박씨 길이 어긋났음 (3편 장면 에이전트가 찾음,
#   사용자 지시 2026-11-04 "3편 고쳐") → 계산을 대본에 맞춤. 박씨 끝 값 3,442.6 → 3,145.7만 원 (대본 문장 2 '3천4백만' → '3천1백만'). 다른 값은 모두 같음.
#   '4_결과.reentry_ath'(지수 최고가 회복 날)는 통계로 그대로 둠. 옛 박씨 끝 값은 '박씨_길.END_value_v10' 으로 남김.
# VERSION: v1.0 — 2026-11-02 — 주식 롱폼 3편 대본 v9 숫자 (박씨 · 거시 지표로 국면 읽기 테스트)
#   사용자 지시 2026-11-02 (대본 평가판 3편 피드백): "이 주제는 장단기 금리차, 원유, 경제 지표 등 기본적인 거시경제 지표로
#   주식시장 국면을 어느정도 파악 가능한지를 테스해야해 항목 다 변경해".
#   다섯 장면: ① 금리 인상 예고 + S&P 500 최고가 (2022-01-03) ② 국제 유가 급등 (2022-03-08) ③ 장단기 금리차(10년 − 3개월) 역전 (2022-11-10)
#   ④ 금리 인상 멈춤 + 유가 진정, 역전은 계속 (2023-07-26) ⑤ 실업률 발표 뒤 3주 −8% (2024-08-05).
#   자료(새로 받은 것: data/CL_F.csv 국제 유가 WTI 선물 · data/SHOP.csv 쇼피파이):
#     S&P 500 가격·배당 포함·13주 국채 = timing-test-2026-10/calc · 10년 국채 = data/TNX.csv · 나스닥 100 = data/QQQ.csv
#   장단기 금리차 = ^TNX(10년 국채 금리) − ^IRX(13주 국채 금리) 그날 종가 (뉴욕 연준이 경기 침체 확률에 쓰는 '10년 − 3개월' 꼴 · ^IRX 는 할인율 기준이라 근사).
#   역전 = 그 값이 0 아래로 내려가 20거래일 넘게 이어진 첫날 · 끝 = 다시 0 위로 20거래일 넘게 이어진 첫날.
#   연준 금리 인상 시작·마지막 날짜는 계산이 아니라 발표 사실(미국 연방준비제도 FOMC 발표문) — 아래 HIKE_START · HIKE_LAST.
#   대출 = 신용대출(반대매매 없음) · 이자 = 그날 13주 국채 금리 + 3%p (가정 — 설명란 계산 기준에 적음).
#   금액 = 원 × 달러 기준 변화율 (환율·세금·수수료 뺌). 현금 = 13주 국채 이자.
# 실행: python3 -B stock/topics/precheck/longform_ep3.py → precheck/longform_ep3_<날짜>.json
# ※ 연구·교육용 — 투자 권유가 아님.
import json
import logging
import sys
from datetime import date, timedelta
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from longform_items import CALC, Ser, load, rd  # noqa: E402

VERSION = "v1.1"
log = logging.getLogger("longform_ep3")

HIKE_START = ["1994-02-04", "1999-06-30", "2004-06-30", "2015-12-16", "2022-03-16"]   # 연준 첫 인상 (FOMC 발표)
HIKE_LAST = ["1995-02-01", "2000-05-16", "2006-06-29", "2018-12-19", "2023-07-26"]    # 연준 마지막 인상 (FOMC 발표)
D1, D2, D3, D4, D5 = "2022-01-03", "2022-03-08", "2022-11-10", "2023-07-26", "2024-08-05"
END = "2025-12-31"          # 박씨 이야기 끝 (4년 안 — 사용자 규칙)
NOW = "2026-10-27"
LOAN_SPREAD = 0.03          # 신용대출 이자 = 13주 국채 + 3%p


def plus(d, days):
    return (date.fromisoformat(d) + timedelta(days=days)).isoformat()


def r4(x):
    return round(float(x), 4)


def main():
    S = load()
    spx, tr, cash = S["SPX"], S["TR"], S["CASH"]
    irx = Ser("13주 국채", rd(CALC / "irx_daily.csv", "close"))
    tnx = Ser("10년 국채", rd(HERE / "data" / "TNX.csv", "close"))
    oil = Ser("국제 유가 WTI", rd(HERE / "data" / "CL_F.csv", "close"))
    shop = Ser("쇼피파이", rd(HERE / "data" / "SHOP.csv", "adjclose"))
    qqq = Ser("나스닥 100", rd(HERE / "data" / "QQQ.csv", "adjclose"))
    R = {}

    def put(key, **kw):
        R[key] = kw
        log.info("key=%s %s", key, json.dumps(kw, ensure_ascii=False)[:600], extra={"stage": "EP3"})

    spread = lambda d: tnx.at(d) - irx.at(d)  # noqa: E731

    # ── 도입: 같은 4년 S&P 500
    put("도입_지수", start=D1, end=END, years=round((date.fromisoformat(END) - date.fromisoformat(D1)).days / 365.25, 2),
        spx_chg=r4(spx.chg(D1, END)), tr_chg=r4(tr.chg(D1, END)))

    # ── ① 2022-01-03 S&P 500 최고가 · 금리 오르기 시작 · 성장주
    lo10 = tnx.low("2020-01-01", D1)
    put("1_장면", day=D1, spx_close=round(spx.at(D1), 2), spx_is_ath=spx.peak_before(D1)[0] == D1,
        tnx=round(tnx.at(D1), 3), tnx_low_2020=[round(tnx.at("2020-01-01") * (1 + lo10[0]), 3), lo10[1]],
        tnx_x_from_low=round(tnx.at(D1) / (tnx.at("2020-01-01") * (1 + lo10[0])), 2), irx=irx.at(D1),
        shop_x_2y=round(shop.at(D1) / shop.at("2019-12-31"), 2), shop_peak=shop.peak_before(D1),
        shop_x_to_peak=round(shop.at(shop.peak_before(D1)[0]) / shop.at("2019-12-31"), 2))
    s_lo, s_lod = shop.low(D1, END)
    t_lo, t_lod = tr.low(D1, END)
    put("1_결과", shop_low=[r4(s_lo), s_lod], shop_back=shop.back(D1, shop.at(D1), after=s_lod), shop_now=r4(shop.chg(D1, NOW)),
        tr_low=[r4(t_lo), t_lod], tr_back=tr.back(D1, tr.at(D1), after=t_lod),
        spx_low=list(spx.low(D1, END)), qqq_low=list(qqq.low(D1, END)),
        note="그대로 둔 성장주 vs 지수 — 가장 크게 빠진 폭·원금 되찾은 날 (덜 잃기)")
    hs = []
    for d in HIKE_START:
        lo = spx.low(d, plus(d, 548))
        q = qqq.low(d, plus(d, 548)) if d >= "1999-03-10" else (None, None)
        hs.append({"hike_start": d, "spx_low_18m": r4(lo[0]), "qqq_low_18m": None if q[0] is None else r4(q[0])})
    put("1_통계_금리인상시작", rows=hs, spx_worst_range=[min(x["spx_low_18m"] for x in hs), max(x["spx_low_18m"] for x in hs)],
        qqq_deeper=sum(1 for x in hs if x["qqq_low_18m"] is not None and x["qqq_low_18m"] < x["spx_low_18m"]),
        qqq_n=sum(1 for x in hs if x["qqq_low_18m"] is not None))

    # ── ② 2022-03-08 국제 유가 급등
    prev = [d for d in oil.k if d < D2 and oil.at(d) >= oil.at(D2)]
    put("2_장면", day=D2, oil=round(oil.at(D2), 2), oil_chg_from_D1=r4(oil.chg(D1, D2)), oil_last_higher=prev[-1] if prev else None,
        spx_from_D1=r4(spx.chg(D1, D2)), shop_from_D1=r4(shop.chg(D1, D2)), irx=irx.at(D2))
    # 반론 K3 확인용 (대본엔 안 씀): 2003년 이후 국제 유가가 3년 만에 가장 높았던 날(1년에 한 번만) 뒤 12개월 S&P 500
    ev3 = []
    for d in oil.k:
        if d < "2003-08-23" or d > plus(NOW, -365) or (ev3 and d <= plus(ev3[-1]["day"], 365)):
            continue
        j = oil.i(plus(d, -3 * 365))
        if oil.v[oil.i(d)] >= oil.v[j:oil.i(d)].max():
            ev3.append({"day": d, "oil": round(oil.at(d), 2), "spx_low_12m": r4(spx.low(d, plus(d, 365))[0]), "spx_12m": r4(spx.chg(d, plus(d, 365)))})
    put("2_확인_유가3년최고", rows=ev3, n=len(ev3), fell_10=sum(1 for e in ev3 if e["spx_low_12m"] <= -0.10),
        note="유가 급등만으로 하락을 말할 수는 없음 — 대본은 '빚을 늘리지 않음'(금리 상승 국면)만 정답으로 씀")
    rally = max(spx.at(d) for d in spx.k if D2 <= d <= "2022-04-08") / spx.at(D2) - 1
    sh_lo = shop.low(D2, D3)
    put("2_결과", irx_D2=irx.at(D2), irx_D3=irx.at(D3), loan_rate_D2=round(irx.at(D2) + 3, 2), loan_rate_D3=round(irx.at(D3) + 3, 2),
        shop_D2_D3=r4(shop.chg(D2, D3)), shop_low=[r4(sh_lo[0]), sh_lo[1]], spx_rally_1m=r4(rally),
        spx_low_to_D3=list(spx.low(D2, D3)), cash_D2_D3=r4(cash.chg(D2, D3)),
        note="대출로 산 성장주 vs 현금 · 그 뒤 한 달 반등도 셈 (물론)")

    # ── ③ 장단기 금리차 역전
    days = [d for d in tnx.k if d >= "1990-01-02"]
    sp = np.array([spread(d) for d in days])
    inv = []
    i = 0
    while i < len(days):
        if sp[i] < 0 and np.all(sp[i:i + 20] < 0) and (not inv or days[i] > inv[-1][1]):
            j = i
            while j < len(days) - 1 and not np.all(sp[j:j + 20] > 0):
                j += 1
            inv.append((days[i], days[j]))
            i = j
        i += 1
    rows = []
    for a, b in inv:
        # 역전 첫날 뒤의 최고가(역전 날 이후만)에서 처음으로 20% 넘게 빠진 날 = 하락장 · 그 최고가 날 = 하락 시작
        k0 = spx.i(a)
        run = np.maximum.accumulate(spx.v[k0:])
        hit = np.nonzero(spx.v[k0:] <= run * 0.8)[0]
        bear = spx.k[k0 + int(hit[0])] if len(hit) else None
        pk = spx.k[k0 + int(np.argmax(spx.v[k0:k0 + int(hit[0]) + 1]))] if bear else None
        rows.append({"start": a, "end": b, "bear_day": bear, "peak_before_bear": pk,
                     "months_to_peak": None if not pk else round((date.fromisoformat(pk) - date.fromisoformat(a)).days / 30.44, 1),
                     "tr_2y": r4(tr.chg(a, plus(a, 730))), "cash_2y": r4(cash.chg(a, plus(a, 730)))})
    put("3_통계_역전", rows=rows, n=len(rows), with_bear=sum(1 for r in rows if r["bear_day"]),
        lag_months=[r["months_to_peak"] for r in rows if r["bear_day"]],
        with_bear_2y=sum(1 for r in rows if r["bear_day"] and r["bear_day"] <= plus(r["start"], 730)),
        sell_better_2y=sum(1 for r in rows if r["cash_2y"] > r["tr_2y"]))
    put("3_장면", day=D3, spread=round(spread(D3), 3), tnx=round(tnx.at(D3), 3), irx=irx.at(D3), spx_from_D1=r4(spx.chg(D1, D3)),
        first_neg=next(d for d in days if d >= "2022-10-01" and spread(d) < 0), inversion=[r for r in rows if r["start"] == D3])
    put("3_결과", cash_2y=r4(cash.chg(D3, plus(D3, 730))), tr_2y=r4(tr.chg(D3, plus(D3, 730))), tr_low_after=list(tr.low(D3, plus(D3, 730))),
        tr_to_END=r4(tr.chg(D3, END)), cash_to_END=r4(cash.chg(D3, END)))

    # ── ④ 금리 인상 멈춤 + 유가 진정 (역전은 계속)
    put("4_장면", spread_min_before=[round(float(min(spread(d) for d in days if D3 <= d <= D4)), 3), min((d for d in days if D3 <= d <= D4), key=spread)], day=D4, irx=irx.at(D4), irx_3m_before=irx.at(plus(D4, -91)), irx_1y_before=irx.at(plus(D4, -365)),
        oil=round(oil.at(D4), 2), oil_from_D2=r4(oil.chg(D2, D4)), spread=round(spread(D4), 3), spx_from_D1=r4(spx.chg(D1, D4)),
        spx_from_low=r4(spx.chg("2022-10-12", D4)))
    reentry = spx.back(D1, spx.at(D1), after="2022-10-12")
    put("4_결과", cash_1y=r4(cash.chg(D4, plus(D4, 365))), tr_1y=r4(tr.chg(D4, plus(D4, 365))), tr_low_1y=list(tr.low(D4, plus(D4, 365))),
        spx_low_1y=list(spx.low(D4, plus(D4, 365))), reentry_ath=reentry, spx_D4_to_reentry=r4(spx.chg(D4, reentry)),
        inversion_end=[r["end"] for r in rows if r["start"] == D3])
    hl = []
    for d in HIKE_LAST:
        e = plus(d, 365)
        hl.append({"last_hike": d, "spx_1y": r4(spx.chg(d, e)), "tr_1y": r4(tr.chg(d, e)), "spx_low_1y": r4(spx.low(d, e)[0])})
    put("4_통계_마지막인상", rows=hl, up_1y=sum(1 for x in hl if x["spx_1y"] > 0), n=len(hl))

    # ── ⑤ 2024-08-05 (실업률 발표 2024-08-02 뒤)
    pk5 = spx.peak_before(D5)
    n_days = spx.i(D5) - spx.i(pk5[0])
    put("5_장면", day=D5, spx_peak=pk5[0], spx_from_peak=r4(pk5[1]), trading_days=n_days, vix=round(S["VIX"].at(D5), 2),
        oil=round(oil.at(D5), 2), oil_from_D2=r4(oil.chg(D2, D5)), tnx=round(tnx.at(D5), 3), tnx_3w_before=round(tnx.at(pk5[0]), 3),
        spread=round(spread(D5), 3), quoted="미국 노동통계국(BLS) 2024-08-02 발표: 2024년 7월 실업률 4.3% (계산 아님 — 인용)")
    put("5_결과", spx_back=spx.back(D5, spx.at(pk5[0]), after=D5), tr_to_END=r4(tr.chg(D5, END)), cash_to_END=r4(cash.chg(D5, END)),
        spx_low_after=list(spx.low(D5, END)), tr_low_after=list(tr.low(D5, END)))
    # 1990년 이후 '최고가 근처(5% 안)에서 한 달(21거래일) 안에 8% 넘게 빠진' 때 → 그 고점을 되찾기 전 20% 넘게 빠졌나
    k, v = spx.k, spx.v
    ath = np.maximum.accumulate(v)
    ev, i = [], 21
    while i < len(k):
        w0 = i - 21
        p = w0 + int(np.argmax(v[w0:i + 1]))
        if v[i] <= v[p] * 0.92 and v[p] >= ath[p] * 0.95 and k[i] >= "1990-01-01":
            j = i
            while j < len(k) and v[j] < v[p]:
                j += 1
            ev.append({"peak": k[p], "hit_8": k[i], "low": r4(v[i:j].min() / v[p] - 1), "back": k[j] if j < len(k) else None})
            i = j
        i += 1
    put("5_통계_8퍼센트하락", rows=ev, n=len(ev), bear=sum(1 for e in ev if e["low"] <= -0.2))

    # ── 박씨 길 (다섯 번 모두 오답) · 정답 길
    def loan_grow(a, b):
        f = 1.0
        for x, y in zip([d for d in tr.k if a <= d < b], [d for d in tr.k if a < d <= b]):
            f *= (1 + (irx.at(x) / 100 + LOAN_SPREAD)) ** ((date.fromisoformat(y) - date.fromisoformat(x)).days / 365)
        return f

    # 박씨: D1 8천만 쇼피파이 + 2천만 S&P 500 → D2 신용대출 3천만으로 쇼피파이 더 → D3 모두 매도·대출 갚음 → 현금
    #       → D4 현금으로 1년(365일) 기다림 → 그날(park_re) 모두 지수 → D5 모두 매도 → END 현금
    #       (v1.1: v1.0 은 지수가 최고가를 다시 넘은 날(reentry, 2024-01-19)에 다시 샀음 — 대본 문장 79 '1년 동안'과 어긋나 고침)
    park_re = plus(D4, 365)
    sh0, ix0 = 8000.0, 2000.0
    sh2 = sh0 * shop.at(D2) / shop.at(D1)
    ix2 = ix0 * tr.at(D2) / tr.at(D1)
    loan = 3000.0
    sh2b = sh2 + loan
    sh3 = sh2b * shop.at(D3) / shop.at(D2)
    ix3 = ix2 * tr.at(D3) / tr.at(D2)
    owe3 = loan * loan_grow(D2, D3)
    c3 = sh3 + ix3 - owe3
    c_re = c3 * cash.at(park_re) / cash.at(D3)
    ix5 = c_re * tr.at(D5) / tr.at(park_re)
    c_end = ix5 * cash.at(END) / cash.at(D5)
    c_re10 = c3 * cash.at(reentry) / cash.at(D3)                                   # v1.0 길 (비교용)
    c_end10 = c_re10 * tr.at(D5) / tr.at(reentry) * cash.at(END) / cash.at(D5)
    # 가장 낮을 때 (순자산 = 주식 − 대출)
    worst = (1e18, None)
    for d in [x for x in tr.k if D1 <= x <= D3]:
        if d < D2:
            val = sh0 * shop.at(d) / shop.at(D1) + ix0 * tr.at(d) / tr.at(D1)
        else:
            val = sh2b * shop.at(d) / shop.at(D2) + ix2 * tr.at(d) / tr.at(D2) - loan * loan_grow(D2, d)
        if val < worst[0]:
            worst = (val, d)
    put("박씨_길", start_won=10000, shop=sh0, index=ix0, D2_value=round(sh2 + ix2, 1), loan=loan, loan_rate_assumption="13주 국채 + 3%p",
        D3_shop=round(sh3, 1), D3_index=round(ix3, 1), D3_owe=round(owe3, 1), D3_cash=round(c3, 1), reentry=park_re, reentry_rule="D4 + 365일 (1년 현금 대기)", reentry_cash=round(c_re, 1), cash_wait_chg=r4(cash.chg(D4, park_re)), END_value_v10=round(c_end10, 1),
        D5_value=round(ix5, 1), END_value=round(c_end, 1), END_chg=r4(c_end / 10000 - 1), worst_net=[round(worst[0], 1), worst[1]],
        unit="만 원")

    # 정답 길: D1 쇼피파이를 2천만만 남기고 8천만 지수(예) → D2 대출 없이 주식의 3분의 1 현금(예) → D3 그대로 → D4 현금을 지수로 → D5 보유 → END
    a_sh, a_ix = 2000.0, 8000.0
    a_sh2, a_ix2 = a_sh * shop.at(D2) / shop.at(D1), a_ix * tr.at(D2) / tr.at(D1)
    a_c = (a_sh2 + a_ix2) / 3
    a_sh2, a_ix2 = a_sh2 * 2 / 3, a_ix2 * 2 / 3
    a_sh4, a_ix4 = a_sh2 * shop.at(D4) / shop.at(D2), a_ix2 * tr.at(D4) / tr.at(D2)
    a_c4 = a_c * cash.at(D4) / cash.at(D2)
    a_ix4b = a_ix4 + a_c4
    a_end = a_sh4 * shop.at(END) / shop.at(D4) + a_ix4b * tr.at(END) / tr.at(D4)
    vals = []
    for d in [x for x in tr.k if D1 <= x <= END]:
        if d < D2:
            val = a_sh * shop.at(d) / shop.at(D1) + a_ix * tr.at(d) / tr.at(D1)
        elif d < D4:
            val = a_sh2 * shop.at(d) / shop.at(D2) + a_ix2 * tr.at(d) / tr.at(D2) + a_c * cash.at(d) / cash.at(D2)
        else:
            val = a_sh4 * shop.at(d) / shop.at(D4) + a_ix4b * tr.at(d) / tr.at(D4)
        vals.append((val, d))
    wv = min(vals)
    put("정답_길", shop=a_sh, index=a_ix, D2_cash=round(a_c, 1), END_value=round(a_end, 1), END_chg=r4(a_end / 10000 - 1),
        worst=[round(wv[0], 1), wv[1], r4(wv[0] / 10000 - 1)], unit="만 원",
        note="정답의 '비중을 줄인다'·'현금을 늘린다'의 수치는 예 (쇼피파이 2천만 원만 · 주식의 3분의 1 현금) — 사람마다 다름")
    # 박씨 처음 그대로(오답 ①만, 대출·매도 없이) 끝까지 들고 있었다면 — 반론 K2 확인용
    hold_all = sh0 * shop.at(END) / shop.at(D1) + ix0 * tr.at(END) / tr.at(D1)
    put("확인_그대로보유", END_value=round(hold_all, 1), END_chg=r4(hold_all / 10000 - 1),
        note="① 오답(성장주 그대로)만 하고 아무것도 안 했다면 — 쇼피파이가 2025년에 원금을 되찾아 손실이 줄어듦. 박씨 손실의 대부분은 ②대출·③바닥 매도·④⑤에서 생김")

    out = HERE / f"longform_ep3_{date.today().isoformat()}.json"
    out.write_text(json.dumps({"tool": f"longform_ep3.py {VERSION}", "data_last": tr.k[-1], "ep3": R}, ensure_ascii=False, indent=1), "utf-8")
    log.info("file=%s keys=%d", out.name, len(R), extra={"stage": "DONE"})


if __name__ == "__main__":
    main()
