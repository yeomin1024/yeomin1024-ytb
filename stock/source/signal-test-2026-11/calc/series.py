#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-11-04 — 박씨 길 ④ = D4 부터 1년(365일) 현금 대기 뒤 다시 매수 (longform_ep3 v1.1 · longform_ep3_2026-11-04.json — 대본 문장 79 '1년 동안'과 맞춤) · 박씨 끝 '3천1백만 원'.
# VERSION: v1.0 — 2026-11-04 — 3편(signal-test-2026-11 · 지표로 국면 읽기 테스트) 대본 v17 영상의 그래프 선·화면 숫자.
#   숫자 출처 = stock/topics/precheck/longform_ep3.py v1.0 (longform_ep3_2026-11-02.json 'ep3') — 같은 자료·같은 날짜·같은 규칙으로 다시 셈.
#   여기서는 화면 선 모양(지표 선·주가 선·계기판 작은 선)과 화면에 쓰는 글(TXT — 반올림한 숫자)만 뽑고,
#   ① 계산 json 과 같은 값인지 ② 대본 v17 에 같은 숫자가 있는지 맞춰 봄 (하나라도 다르면 끝 코드 1, series.js 를 쓰지 않음).
#   자료: S&P 500 가격·배당 포함·13주 국채(현금 이자) = longform_items.load() · 10년 국채 = data/TNX.csv · 국제 유가 WTI = data/CL_F.csv
#         쇼피파이 = data/SHOP.csv · 나스닥 100 = data/QQQ.csv · 장단기 금리차 = 10년 − 13주(3개월) 그날 종가.
#   실업률 4.3% 는 자료 파일이 없음 — 미국 노동통계국(BLS) 2024-08-02 발표 인용 (선으로 그리지 않고 읽기 숫자 하나로만).
#   값 = 시작 날 1 기준 또는 만 원 (달러 기준 변화율 — 환율·세금·수수료 뺌).
#   출력: video/episodes/signal-test-2026-11/series.js (window.SERIES). 실행: python3 -B stock/source/signal-test-2026-11/calc/series.py
#   ※ 연구·교육용 — 투자 권유가 아님.
import json
import logging
import sys
import time
from datetime import date, timedelta
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "stock/topics/precheck"))
import longform_items as L  # noqa: E402

VERSION = "v1.1"
logging.basicConfig(level=logging.INFO, format="[%(stage)s] %(message)s")
log = logging.getLogger("series_ep3")
CALC_JSON = ROOT / "stock/topics/precheck/longform_ep3_2026-11-04.json"
SCRIPT = ROOT / "stock/source/signal-test-2026-11/signal-test-2026-11.txt"
DST = ROOT / "video/episodes/signal-test-2026-11/series.js"
D1, D2, D3, D4, D5 = "2022-01-03", "2022-03-08", "2022-11-10", "2023-07-26", "2024-08-05"
END = "2025-12-31"
LOAN_SPREAD = 0.03
HIKE_START = ["1994-02-04", "1999-06-30", "2004-06-30", "2015-12-16", "2022-03-16"]   # longform_ep3 과 같음 (FOMC 발표)
HIKE_LAST = ["1995-02-01", "2000-05-16", "2006-06-29", "2018-12-19", "2023-07-26"]
JOBS_QUOTE = 4.3            # BLS 2024-08-02 발표 2024년 7월 실업률 (인용 — 계산 아님)


def plus(d, days):
    return (date.fromisoformat(d) + timedelta(days=days)).isoformat()


def mon(a, b):
    """두 날 사이 달 수 (30.44일 = 한 달, 반올림)."""
    return round((date.fromisoformat(b) - date.fromisoformat(a)).days / 30.44)


def ym(n):
    """달 수 → '3Y 7M' 꼴."""
    y, m = divmod(n, 12)
    return " ".join(([f"{y}Y"] if y else []) + ([f"{m}M"] if m or not y else []))


def pct(x, nd=0, sign=True):
    v = round(x * 100, nd)
    s = f"{abs(v):.{nd}f}%"
    return (("+" if v > 0 else "−" if v < 0 else "") if sign else "") + s


def thin(rows, step):
    if step <= 1:
        return rows
    keep = rows[::step]
    if keep[-1] != rows[-1]:
        keep.append(rows[-1])
    return keep


def main():
    t0 = time.time()
    S = L.load()
    spx, tr, cash = S["SPX"], S["TR"], S["CASH"]
    irx = L.Ser("13주 국채", L.rd(L.CALC / "irx_daily.csv", "close"))
    tnx = L.Ser("10년 국채", L.rd(L.HERE / "data" / "TNX.csv", "close"))
    oil = L.Ser("국제 유가 WTI", L.rd(L.HERE / "data" / "CL_F.csv", "close"))
    shop = L.Ser("쇼피파이", L.rd(L.HERE / "data" / "SHOP.csv", "adjclose"))
    qqq = L.Ser("나스닥 100", L.rd(L.HERE / "data" / "QQQ.csv", "adjclose"))
    spread = lambda d: tnx.at(d) - irx.at(d)  # noqa: E731
    days = lambda ser, a, b: [d for d in ser.k if a <= d <= b]  # noqa: E731
    r4 = lambda x: round(float(x), 4)  # noqa: E731
    log.info("d1=%s d2=%s d3=%s d4=%s d5=%s end=%s data_last=%s", D1, D2, D3, D4, D5, END, tr.k[-1], extra={"stage": "DATES"})

    # ── 박씨 길 (다섯 번 모두 오답 — longform_ep3 '박씨_길' 과 같은 규칙) · 만 원
    def loan_grow(a, b):
        f = 1.0
        for x, y in zip([d for d in tr.k if a <= d < b], [d for d in tr.k if a < d <= b]):
            f *= (1 + (irx.at(x) / 100 + LOAN_SPREAD)) ** ((date.fromisoformat(y) - date.fromisoformat(x)).days / 365)
        return f

    reentry = plus(D4, 365)   # v1.1 박씨는 D4 부터 1년 현금으로 기다린 뒤 다시 매수 (longform_ep3 v1.1 park_re · 대본 문장 79)
    sh0, ix0, loan = 8000.0, 2000.0, 3000.0
    sh2, ix2 = sh0 * shop.at(D2) / shop.at(D1), ix0 * tr.at(D2) / tr.at(D1)
    sh2b = sh2 + loan
    sh3, ix3 = sh2b * shop.at(D3) / shop.at(D2), ix2 * tr.at(D3) / tr.at(D2)
    c3 = sh3 + ix3 - loan * loan_grow(D2, D3)
    c_re = c3 * cash.at(reentry) / cash.at(D3)
    ix5 = c_re * tr.at(D5) / tr.at(reentry)
    c_end = ix5 * cash.at(END) / cash.at(D5)
    lg = {}                                   # 대출 이자 누적 (날마다 다시 곱하면 느려서 한 번에)
    f = 1.0
    prev = None
    for d in [x for x in tr.k if D2 <= x <= D3]:
        if prev is not None:
            f *= (1 + (irx.at(prev) / 100 + LOAN_SPREAD)) ** ((date.fromisoformat(d) - date.fromisoformat(prev)).days / 365)
        lg[d] = f
        prev = d

    def park(d):
        if d < D2:
            return sh0 * shop.at(d) / shop.at(D1) + ix0 * tr.at(d) / tr.at(D1)
        if d <= D3:
            return sh2b * shop.at(d) / shop.at(D2) + ix2 * tr.at(d) / tr.at(D2) - loan * lg[d]
        if d <= reentry:
            return c3 * cash.at(d) / cash.at(D3)
        if d <= D5:
            return c_re * tr.at(d) / tr.at(reentry)
        return ix5 * cash.at(d) / cash.at(D5)

    # ── 정답 길 (longform_ep3 '정답_길' — 비중 수치는 예)
    a_sh, a_ix = 2000.0, 8000.0
    a_sh2, a_ix2 = a_sh * shop.at(D2) / shop.at(D1), a_ix * tr.at(D2) / tr.at(D1)
    a_c = (a_sh2 + a_ix2) / 3
    a_sh2, a_ix2 = a_sh2 * 2 / 3, a_ix2 * 2 / 3
    a_sh4, a_ix4 = a_sh2 * shop.at(D4) / shop.at(D2), a_ix2 * tr.at(D4) / tr.at(D2)
    a_ix4b = a_ix4 + a_c * cash.at(D4) / cash.at(D2)

    def good(d):
        if d < D2:
            return a_sh * shop.at(d) / shop.at(D1) + a_ix * tr.at(d) / tr.at(D1)
        if d < D4:
            return a_sh2 * shop.at(d) / shop.at(D2) + a_ix2 * tr.at(d) / tr.at(D2) + a_c * cash.at(d) / cash.at(D2)
        return a_sh4 * shop.at(d) / shop.at(D4) + a_ix4b * tr.at(d) / tr.at(D4)

    out = {"made": "2026-11-04", "tool": f"series.py {VERSION}", "src": "longform_ep3.py v1.1 자료·규칙", "data_last": tr.k[-1],
           "dates": {"d1": D1, "d2": D2, "d3": D3, "d4": D4, "d5": D5, "end": END, "reentry": reentry}}
    N = lambda ser, a, b, base, step=1: thin([[d, r4(ser.at(d) / ser.at(base))] for d in days(ser, a, b)], step)  # noqa: E731
    V = lambda ser, a, b, step=1, nd=3: thin([[d, round(ser.at(d), nd)] for d in days(ser, a, b)], step)  # noqa: E731

    # ── 계기판 줄 작은 선 (선택마다 그날까지 1년 — 값 글자 없이 모양만): RATE = 10년 국채 · OIL = WTI · CURVE = 10년 − 3개월
    spark = {}
    for k, dk in enumerate([D1, D2, D3, D4, D5], 1):
        a = plus(dk, -365)
        spark[k] = {"RATE": V(tnx, a, dk, 5), "OIL": V(oil, a, dk, 5, 2),
                    "CURVE": thin([[d, round(spread(d), 3)] for d in days(tnx, a, dk)], 5)}
    out["spark"] = spark

    # ── 도입: 박씨 1억 원 → · S&P 500 가격 (D1 = 1)
    out["intro_park"] = thin([[d, r4(park(d) / 10000)] for d in days(tr, D1, END)], 3)
    out["intro_spx"] = N(spx, D1, END, D1, 3)

    # ── 선택 1 이야기: 쇼피파이 2년 (2019-12-31 = 1) · S&P 500 1년 · 10년 국채 2020-03 바닥 → D1
    lo10 = tnx.low("2020-01-01", D1)
    tnx_low = tnx.at("2020-01-01") * (1 + lo10[0])
    out["s1_shop2y"] = N(shop, "2019-12-31", D1, "2019-12-31", 5)
    out["s1_spx1y"] = N(spx, plus(D1, -365), D1, D1, 3)
    out["s1_tnx"] = V(tnx, "2020-01-02", D1, 5)
    # 해설 1: 10년 국채(위) · 쇼피파이·S&P 500 배당 포함(아래, D1 = 1) — 날짜 축 D1 ~ 2025-08-29
    e1b = "2025-08-29"
    out["e1_tnx"] = V(tnx, D1, e1b, 3)
    out["e1_shop"] = N(shop, D1, e1b, D1, 3)
    out["e1_tr"] = N(tr, D1, e1b, D1, 3)
    s_lo, s_lod = shop.low(D1, END)
    t_lo, t_lod = tr.low(D1, END)
    s_back = shop.back(D1, shop.at(D1), after=s_lod)
    t_back = tr.back(D1, tr.at(D1), after=t_lod)
    hs = []
    for d in HIKE_START:
        lo = spx.low(d, plus(d, 548))
        q = qqq.low(d, plus(d, 548)) if d >= "1999-03-10" else (None, None)
        hs.append({"y": d[:4], "day": d, "spx": r4(lo[0]), "qqq": None if q[0] is None else r4(q[0])})
    out["e1_hikes"] = hs

    # ── 선택 2: WTI D1 → D2 · 2008 → D2 (주간) · 해설 2 날짜 축 D1 ~ 2022-11-30
    out["s2_oil2m"] = V(oil, D1, D2, 1, 2)
    out["s2_oil_long"] = V(oil, "2007-01-02", D2, 10, 2)
    oil_prev = [d for d in oil.k if d < D2 and oil.at(d) >= oil.at(D2)]
    e2b = "2022-11-30"
    out["e2_oil"] = V(oil, D1, e2b, 1, 2)
    out["e2_irx"] = V(irx, D1, e2b, 1, 3)
    out["e2_shop"] = N(shop, D2, e2b, D2, 1)
    rally_v, rally_d = max((spx.at(d), d) for d in spx.k if D2 <= d <= "2022-04-08")
    out["e2_spx"] = N(spx, D2, "2022-04-08", D2, 1)
    sh_lo, sh_lod = shop.low(D2, D3)

    # ── 선택 3: 장단기 금리차 (해설 3 날짜 축 2022-07-01 ~ 2024-12-31) · 그날부터 2년 지수(배당 포함)·현금
    e3a, e3b = "2022-07-01", "2024-12-31"
    out["lv"] = {"tnx_d1": round(tnx.at(D1), 3), "irx_d1": irx.at(D1), "tnx_d3": round(tnx.at(D3), 3), "irx_d3": irx.at(D3)}   # 선택 3 막대 높이 (글자 없이)
    out["s3_spread"] = thin([[d, round(spread(d), 3)] for d in days(tnx, plus(D3, -365), D3)], 3)
    out["s3_spx"] = N(spx, D1, D3, D1, 3)
    out["e3_spread"] = thin([[d, round(spread(d), 3)] for d in days(tnx, e3a, e3b)], 2)
    d3_2y = plus(D3, 730)
    out["e3_tr"] = N(tr, D3, d3_2y, D3, 2)
    out["e3_cash"] = N(cash, D3, d3_2y, D3, 2)
    tl3, tl3d = tr.low(D3, d3_2y)
    # 1990~ 역전 역사 (longform_ep3 '3_통계_역전' 과 같은 규칙)
    dd = [d for d in tnx.k if d >= "1990-01-02"]
    sp = np.array([spread(d) for d in dd])
    inv, i = [], 0
    while i < len(dd):
        if sp[i] < 0 and np.all(sp[i:i + 20] < 0) and (not inv or dd[i] > inv[-1][1]):
            j = i
            while j < len(dd) - 1 and not np.all(sp[j:j + 20] > 0):
                j += 1
            inv.append((dd[i], dd[j]))
            i = j
        i += 1
    rows = []
    for a, b in inv:
        k0 = spx.i(a)
        run = np.maximum.accumulate(spx.v[k0:])
        hit = np.nonzero(spx.v[k0:] <= run * 0.8)[0]
        bear = spx.k[k0 + int(hit[0])] if len(hit) else None
        pk = spx.k[k0 + int(np.argmax(spx.v[k0:k0 + int(hit[0]) + 1]))] if bear else None
        rows.append({"start": a, "end": b, "bear_day": bear, "peak": pk,
                     "months": None if not pk else round((date.fromisoformat(pk) - date.fromisoformat(a)).days / 30.44, 1)})
    out["e3_inv"] = rows
    out["e3_hist_spread"] = thin([[d, round(spread(d), 2)] for d in dd if d <= END], 10)
    out["e3_hist_spx"] = thin([[d, round(spx.at(d), 1)] for d in days(spx, "1990-01-02", END)], 10)

    # ── 선택 4: WTI D2 → D4 · 3개월 국채 1년 · 해설 4 날짜 축 2022-11-10 ~ 2024-12-31
    out["s4_oil"] = V(oil, D2, D4, 5, 2)
    out["s4_irx"] = V(irx, plus(D4, -365), D4, 3, 3)
    out["s4_spx"] = N(spx, "2022-10-12", D4, D1, 3)
    e4a, e4b = D3, "2024-12-31"
    out["e4_spread"] = thin([[d, round(spread(d), 3)] for d in days(tnx, e4a, e4b)], 2)
    d4_1y = plus(D4, 365)
    out["e4_tr"] = N(tr, D4, d4_1y, D4, 1)
    out["e4_cash"] = N(cash, D4, d4_1y, D4, 2)
    tl4, tl4d = tr.low(D4, d4_1y)
    hl = []
    for d in HIKE_LAST:
        hl.append({"y": d[:4], "day": d, "spx_1y": r4(spx.chg(d, plus(d, 365)))})
    out["e4_last"] = hl

    # ── 선택 5: 그날 다른 지표 · 해설 5 날짜 축 2024-07-01 ~ END
    pk5, pk5_chg = spx.peak_before(D5)
    out["s5_spx"] = N(spx, plus(pk5, -40), D5, pk5, 1)
    out["e5_oil"] = V(oil, D2, D5, 5, 2)
    out["e5_tnx3w"] = V(tnx, pk5, D5, 1, 3)
    out["e5_tnx"] = V(tnx, "2024-07-01", END, 2, 3)
    out["e5_tr"] = N(tr, D5, END, D5, 2)
    out["e5_cash"] = N(cash, D5, END, D5, 3)
    back5 = spx.back(D5, spx.at(pk5), after=D5)
    # 1990~ 최고가 근처 한 달 −8% (longform_ep3 '5_통계_8퍼센트하락' 과 같은 규칙)
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
            ev.append({"peak": k[p], "low": r4(v[i:j].min() / v[p] - 1)})
            i = j
        i += 1
    out["e5_drops"] = ev

    # ── 끝: 박씨 길 · 정답 길 (만 원)
    out["end_park"] = thin([[d, round(park(d))] for d in days(tr, D1, END)], 5)
    out["end_good"] = thin([[d, round(good(d))] for d in days(tr, D1, END)], 5)

    # ── 화면 글 (반올림 — JS 는 이 글만 씀)
    mil = lambda manwon: f"₩{int(round(manwon * 10000 / 1e6) * 1e6):,}"  # noqa: E731   백만 원 단위 (대본 '3천1백만 원')
    TXT = {
        "park0": "₩100,000,000", "park_end": mil(c_end), "spx_4y": pct(spx.chg(D1, END)),
        "alloc_g": f"₩{int(sh0 * 10000):,}", "alloc_i": f"₩{int(ix0 * 10000):,}", "shop_span": ym(mon("2019-12-31", D1)), "oil_span": ym(mon(D1, D2)),
        "shop_2y": f"×{shop.at(D1) / shop.at('2019-12-31'):.1f}", "tnx_low": f"{tnx_low:.1f}%", "tnx_d1": f"{tnx.at(D1):.1f}%",
        "tnx_x": f"×{tnx.at(D1) / tnx_low:.1f}", "shop_low": pct(s_lo), "shop_back": ym(mon(D1, s_back)), "tr_low": pct(t_lo),
        "tr_back": ym(mon(D1, t_back)), "hike_max": pct(min(h["spx"] for h in hs)),
        "oil_2m": pct(oil.chg(D1, D2)), "oil_d2": f"${oil.at(D2):.1f}", "oil_prev_year": oil_prev[-1][:4], "oil_prev": oil_prev[-1][:7].replace("-", "."),
        "spx_d2": pct(spx.chg(D1, D2)), "shop_d2": pct(shop.chg(D1, D2)), "shop_half": pct(sh_lo), "shop_half_m": ym(mon(D2, sh_lod)),
        "irx_d2": f"{irx.at(D2):.1f}%", "irx_d3": f"{irx.at(D3):.0f}%", "irx_m": ym(mon(D2, D3)), "rally": pct(rally_v / spx.at(D2) - 1),
        "spx_d3": pct(spx.chg(D1, D3)), "cash_2y": pct(cash.chg(D3, d3_2y)), "tr_low3": pct(tl3), "tr_2y": pct(tr.chg(D3, d3_2y)),
        "oil_d4": pct(oil.chg(D2, D4)), "spx_low_d4": pct(spx.chg("2022-10-12", D4)), "spx_d4": pct(spx.chg(D1, D4)),
        "cash_1y": pct(cash.chg(D4, d4_1y)), "tr_low4": pct(tl4, 1), "tr_low4_m": ym(mon(D4, tl4d)), "tr_1y": pct(tr.chg(D4, d4_1y)),
        "inv_left": ym(mon(D4, [r["end"] for r in rows if r["start"] == D3][0])),
        "jobs": f"{JOBS_QUOTE:.1f}%", "spx_d5": pct(pk5_chg, 1), "spx_d5_w": f"{round((date.fromisoformat(D5) - date.fromisoformat(pk5)).days / 7)}W",
        "oil_d5": pct(oil.chg(D2, D5)), "tnx_pk5": f"{tnx.at(pk5):.1f}%", "tnx_d5": f"{tnx.at(D5):.1f}%",
        "cash_end": pct(cash.chg(D5, END)), "back_days": f"{(date.fromisoformat(back5) - date.fromisoformat(D5)).days}", "tr_end": pct(tr.chg(D5, END)),
        "end_m": ym(mon(D5, END)), "drops_n": f"{len(ev)}", "drops_ok": f"{sum(1 for e in ev if e['low'] > -0.2)}",
    }
    out["TXT"] = TXT
    out["dates"].update({"shop_low": s_lod, "shop_back": s_back, "tr_low": t_lod, "tr_back": t_back, "rally": rally_d, "shop_half": sh_lod,
                         "tr_low3": tl3d, "d3_2y": d3_2y, "tr_low4": tl4d, "d4_1y": d4_1y, "pk5": pk5, "back5": back5, "tnx_low": lo10[1]})

    # ── ① 계산 json 과 맞춰 보기
    J = json.loads(CALC_JSON.read_text("utf-8"))["ep3"]
    inv3 = [r for r in rows if r["start"] == D3][0]
    chk = [
        ("도입 spx_chg", r4(spx.chg(D1, END)), J["도입_지수"]["spx_chg"]),
        ("박씨 END_value", round(c_end, 1), J["박씨_길"]["END_value"]),
        ("박씨 D3_cash", round(c3, 1), J["박씨_길"]["D3_cash"]),
        ("박씨 곡선 끝 = END_value", round(park(END), 1), J["박씨_길"]["END_value"]),
        ("박씨 reentry", reentry, J["박씨_길"]["reentry"]),
        ("정답 END_value", round(good(END), 1), J["정답_길"]["END_value"]),
        ("1 tnx_x_from_low", round(tnx.at(D1) / tnx_low, 2), J["1_장면"]["tnx_x_from_low"]),
        ("1 shop_x_2y", round(shop.at(D1) / shop.at("2019-12-31"), 2), J["1_장면"]["shop_x_2y"]),
        ("1 spx_is_ath", spx.peak_before(D1)[0] == D1, J["1_장면"]["spx_is_ath"]),
        ("1 shop_low", [r4(s_lo), s_lod], J["1_결과"]["shop_low"]),
        ("1 shop_back", s_back, J["1_결과"]["shop_back"]),
        ("1 tr_low", [r4(t_lo), t_lod], J["1_결과"]["tr_low"]),
        ("1 tr_back", t_back, J["1_결과"]["tr_back"]),
        ("1 hikes spx", [h["spx"] for h in hs], [x["spx_low_18m"] for x in J["1_통계_금리인상시작"]["rows"]]),
        ("1 hikes qqq", [h["qqq"] for h in hs], [x["qqq_low_18m"] for x in J["1_통계_금리인상시작"]["rows"]]),
        ("2 oil", round(oil.at(D2), 2), J["2_장면"]["oil"]),
        ("2 oil_chg_from_D1", r4(oil.chg(D1, D2)), J["2_장면"]["oil_chg_from_D1"]),
        ("2 oil_last_higher", oil_prev[-1], J["2_장면"]["oil_last_higher"]),
        ("2 spx_from_D1", r4(spx.chg(D1, D2)), J["2_장면"]["spx_from_D1"]),
        ("2 shop_from_D1", r4(shop.chg(D1, D2)), J["2_장면"]["shop_from_D1"]),
        ("2 irx_D2·D3", [irx.at(D2), irx.at(D3)], [J["2_결과"]["irx_D2"], J["2_결과"]["irx_D3"]]),
        ("2 shop_low", [r4(sh_lo), sh_lod], J["2_결과"]["shop_low"]),
        ("2 spx_rally_1m", r4(rally_v / spx.at(D2) - 1), J["2_결과"]["spx_rally_1m"]),
        ("3 spread", round(spread(D3), 3), J["3_장면"]["spread"]),
        ("3 spx_from_D1", r4(spx.chg(D1, D3)), J["3_장면"]["spx_from_D1"]),
        ("3 cash_2y", r4(cash.chg(D3, d3_2y)), J["3_결과"]["cash_2y"]),
        ("3 tr_2y", r4(tr.chg(D3, d3_2y)), J["3_결과"]["tr_2y"]),
        ("3 tr_low_after", [r4(tl3), tl3d], [r4(J["3_결과"]["tr_low_after"][0]), J["3_결과"]["tr_low_after"][1]]),
        ("3 inversions", [(r["start"], r["end"], r["bear_day"], r["months"]) for r in rows],
         [(r["start"], r["end"], r["bear_day"], r["months_to_peak"]) for r in J["3_통계_역전"]["rows"]]),
        ("4 oil_from_D2", r4(oil.chg(D2, D4)), J["4_장면"]["oil_from_D2"]),
        ("4 spx_from_low", r4(spx.chg("2022-10-12", D4)), J["4_장면"]["spx_from_low"]),
        ("4 spx_from_D1", r4(spx.chg(D1, D4)), J["4_장면"]["spx_from_D1"]),
        ("4 cash_1y", r4(cash.chg(D4, d4_1y)), J["4_결과"]["cash_1y"]),
        ("4 tr_1y", r4(tr.chg(D4, d4_1y)), J["4_결과"]["tr_1y"]),
        ("4 tr_low_1y", [r4(tl4), tl4d], [r4(J["4_결과"]["tr_low_1y"][0]), J["4_결과"]["tr_low_1y"][1]]),
        ("4 inversion_end", [inv3["end"]], J["4_결과"]["inversion_end"]),
        ("4 last hikes", [h["spx_1y"] for h in hl], [x["spx_1y"] for x in J["4_통계_마지막인상"]["rows"]]),
        ("5 spx_peak", [pk5, r4(pk5_chg)], [J["5_장면"]["spx_peak"], J["5_장면"]["spx_from_peak"]]),
        ("5 oil_from_D2", r4(oil.chg(D2, D5)), J["5_장면"]["oil_from_D2"]),
        ("5 tnx", [round(tnx.at(pk5), 3), round(tnx.at(D5), 3)], [J["5_장면"]["tnx_3w_before"], J["5_장면"]["tnx"]]),
        ("5 spx_back", back5, J["5_결과"]["spx_back"]),
        ("5 tr_to_END", r4(tr.chg(D5, END)), J["5_결과"]["tr_to_END"]),
        ("5 cash_to_END", r4(cash.chg(D5, END)), J["5_결과"]["cash_to_END"]),
        ("5 drops n·bear", [len(ev), sum(1 for e in ev if e["low"] <= -0.2)], [J["5_통계_8퍼센트하락"]["n"], J["5_통계_8퍼센트하락"]["bear"]]),
    ]
    # ── ② 대본 v17 의 숫자와 맞춰 보기 (화면 글이 대본이 말한 숫자와 같은가 — 반올림 기준은 대본 표현)
    txt = SCRIPT.read_text("utf-8")
    num = lambda s: float(s.replace("−", "-").replace("+", "").replace("%", "").replace("×", "").replace("$", "").replace("₩", "").replace(",", ""))  # noqa: E731
    sc = [  # (화면 글 키, 대본 낱말, 맞는지)
        ("park_end", "3천1백만 원", TXT["park_end"] == "₩31,000,000"),
        ("alloc", "8천만 원은 한 성장주에, 2천만 원은", TXT["alloc_g"] == "₩80,000,000" and TXT["alloc_i"] == "₩20,000,000"),
        ("shop_span", "2년 만에 3배", TXT["shop_span"] == "2Y"),
        ("oil_span", "두 달 만에 60%", TXT["oil_span"] == "2M"),
        ("spx_4y", "40% 넘게 올랐습니다", 40 <= num(TXT["spx_4y"]) < 50),
        ("shop_2y", "3배 넘게 오른", num(TXT["shop_2y"]) >= 3),
        ("tnx_x", "바닥의 3배가 넘었습니다", num(TXT["tnx_x"]) >= 3),
        ("shop_low", "81%까지 하락", TXT["shop_low"] == "−81%"),
        ("shop_back", "3년 7개월", TXT["shop_back"] == "3Y 7M"),
        ("tr_low", "24% 하락했다가", TXT["tr_low"] == "−24%"),
        ("tr_back", "2년이 안 돼", mon(D1, t_back) < 24),
        ("hike_max", "많아야 18% 하락", TXT["hike_max"] == "−18%"),
        ("hike_qqq", "네 번 중 세 번", sum(1 for h in hs if h["qqq"] is not None and h["qqq"] < h["spx"]) == 3 and sum(1 for h in hs if h["qqq"] is not None) == 4),
        ("oil_prev_year", "13년여 만에", 13 <= (date.fromisoformat(D2) - date.fromisoformat(oil_prev[-1])).days / 365.25 < 14),
        ("oil_2m", "60% 넘게 오른", 60 <= num(TXT["oil_2m"]) < 70),
        ("spx_d2", "지수는 13%", TXT["spx_d2"] == "−13%"),
        ("shop_d2", "성장주는 62% 하락", TXT["shop_d2"] == "−62%"),
        ("oil_d2", "123달러를 넘은", 123 <= oil.at(D2) < 124),
        ("shop_half", "반 토막", TXT["shop_half"] == "−50%"),
        ("shop_half_m", "일곱 달 뒤", TXT["shop_half_m"] == "7M"),
        ("irx", "0.4%에서 4%로", TXT["irx_d2"] == "0.4%" and TXT["irx_d3"] == "4%"),
        ("irx_m", "여덟 달 새", TXT["irx_m"] == "8M"),
        ("rally", "11% 다시 오르기도", TXT["rally"] == "+11%"),
        ("spx_d3", "최고가보다 18% 아래", TXT["spx_d3"] == "−18%"),
        ("cash_2y", "이자로 10% 느는", TXT["cash_2y"] == "+10%"),
        ("tr_low3", "4% 더 하락하기도", TXT["tr_low3"] == "−4%"),
        ("tr_2y", "56% 올라", TXT["tr_2y"] == "+56%"),
        ("inv", "역전 네 번 가운데 세 번", len(rows) == 4 and sum(1 for r in rows if r["bear_day"]) == 3),
        ("inv_lag", "한 달 뒤부터 14개월 뒤까지", [round(r["months"]) for r in rows if r["months"] is not None] and
         min(round(r["months"]) for r in rows if r["months"] is not None) == 1 and max(round(r["months"]) for r in rows if r["months"] is not None) == 14),
        ("oil_d4", "고점보다 36% 내려왔습니다", TXT["oil_d4"] == "−36%"),
        ("spx_low_d4", "바닥에서 28% 올랐지만", TXT["spx_low_d4"] == "+28%"),
        ("spx_d4", "최고가보다는 5% 아래", TXT["spx_d4"] == "−5%"),
        ("cash_1y", "이자로 5% 느는", TXT["cash_1y"] == "+5%"),
        ("tr_low4", "석 달 뒤 10% 가까이 하락", 9 <= -num(TXT["tr_low4"]) < 10 and TXT["tr_low4_m"] == "3M"),
        ("tr_1y", "20% 늘었을", TXT["tr_1y"] == "+20%"),
        ("inv_left", "1년 넘게 이어졌습니다", mon(D4, inv3["end"]) > 12),
        ("last_up", "다섯 번 중 네 번", sum(1 for h in hl if h["spx_1y"] > 0) == 4 and len(hl) == 5),
        ("jobs", "4.3%로 올랐다는", TXT["jobs"] == "4.3%"),
        ("spx_d5", "3주 만에 8% 넘게", 8 <= -num(TXT["spx_d5"]) < 9 and TXT["spx_d5_w"] == "3W"),
        ("oil_d5", "고점보다 41% 낮았습니다", TXT["oil_d5"] == "−41%"),
        ("tnx_5", "4.2%에서 3.8%로", TXT["tnx_pk5"] == "4.2%" and TXT["tnx_d5"] == "3.8%"),
        ("cash_end", "이자로 6% 느는", TXT["cash_end"] == "+6%"),
        ("end_m", "1년 5개월", TXT["end_m"] == "1Y 5M"),
        ("back_days", "45일 만에", TXT["back_days"] == "45"),
        ("tr_end", "34% 올라", TXT["tr_end"] == "+34%"),
        ("drops", "열여덟 번", TXT["drops_n"] == "18"),
        ("drops_ok", "열네 번은", TXT["drops_ok"] == "14"),
    ]
    bad = [c for c in chk if c[1] != c[2]]
    for name, got, want in chk:
        log.info("check=%s got=%s calc=%s ok=%s", name, json.dumps(got, ensure_ascii=False), json.dumps(want, ensure_ascii=False), got == want, extra={"stage": "CHECK"})
    for key, phrase, ok in sc:
        in_script = phrase in txt
        log.info("script=%s phrase=%s screen=%s in_script=%s ok=%s", key, json.dumps(phrase, ensure_ascii=False), TXT.get(key, "-"), in_script, bool(ok), extra={"stage": "SCRIPT"})
        if not (ok and in_script):
            bad.append((key, phrase, TXT.get(key)))
    if bad:
        log.info("mismatch=%s next=계산 규칙(longform_ep3.py)·대본 숫자와 다시 맞춤 — series.js 를 쓰지 않음", json.dumps(bad, ensure_ascii=False, default=str), extra={"stage": "FAIL"})
        return 1
    n_pts = sum(len(v) for v in out.values() if isinstance(v, list) and v and isinstance(v[0], list))
    log.info("keys=%d points=%d txt=%d", len(out), n_pts, len(TXT), extra={"stage": "SERIES"})
    DST.parent.mkdir(parents=True, exist_ok=True)
    DST.write_text(f"// 자동 생성 — stock/source/signal-test-2026-11/calc/series.py {VERSION} (손으로 고치지 않음 · 연구·교육용)\nwindow.SERIES = "
                   + json.dumps(out, ensure_ascii=False, separators=(",", ":")) + ";\n", "utf-8")
    log.info("file=%s bytes=%d sec=%.1f", DST.relative_to(ROOT), DST.stat().st_size, time.time() - t0, extra={"stage": "DONE"})
    return 0


if __name__ == "__main__":
    sys.exit(main())
