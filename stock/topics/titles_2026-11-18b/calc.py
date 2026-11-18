#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-11-18 — 성공 사례 10편(차트 너머 2편·오피디 1편 더함) 뒤 제목 다시 — K 코스피 고점 대비 −40%·−45% 과거 · S −20%마다 판 사람(계좌 최대 낙폭 포함) · H 사상 최고 날 매수 · G 은퇴 5년 전 나눠 옮기기 · G2 은퇴 달 전부(1982~2026) · C30 S&P 500(배당 포함)+현금 30% 더함 · S 에 되사는 규칙 3가지(전 고점 · 판 값 · 바닥 +20%).
# 이전 v1.0 — 2026-11-18 — 사용자가 고른 성공 사례 8편을 본뜬 다음 제목 5안의 숫자 (사용자 지시 "…이것들만 성공 사례로 해서 왜 조회수가 많이 터졌는지 … 분석해서 다음으로 조회수가 많이 나올만할 제목 5개 만들어봐").
#   자료 = Yahoo Finance chart API v8 일별 (calc 는 stock/topics/titles_2026-11-18/calc.py 의 fetch 를 씀 — 같은 data/ 캐시).
#   판정 규칙(계산 전에 정함):
#   P 코스피 고점 네 사람: 코스피(^KS11) 2026 고점 날 종가에 1억 원씩 — 삼성전자(005930.KS) · SK하이닉스(000660.KS) · KODEX 200(069500.KS 수정 종가) · S&P 500(SPY 수정 종가 × 원/달러 KRW=X) → 마지막 거래일 원화 값.
#   R 은퇴 시점: S&P 500(^GSPC 가격 — 배당 빼고, 보수적) 매달 첫 거래일 50만 원 20년 적립, 끝(은퇴) 달만 바꿔 원화 금액(달러 수익률을 원화 금액에 그대로 — 환율 효과 뺌). 2000-03 · 2002-10 · 2007-10 · 2009-03.
#   L QLD 적립: 나스닥100(^NDX) 하루 수익률 × 2 − (보수 0.95% + 13주 국채 ^IRX)/252 로 만든 2배 지수(2006-06-21 부터는 실제 QLD 수정 종가로 이음) vs QQQ(배당 포함) — 2000-03-27 나스닥 고점 달부터 매달 50만 원 → 원금(넣은 돈)을 다시 넘은 마지막 날까지 걸린 해, 지금 값.
#   D 적립 멈춤 금액: titles_2026-11-18 calc E5 와 같은 규칙, 월 50만 원으로 원화 금액 (2008-01~2012-12 · 2000-03~2005-02).
#   X 환율: SPY(달러) vs SPY×KRW=X(원화) — 2026-06-22(코스피 고점) · 2026-10-06(S&P 고점) 부터 지금까지.
# 로그: [STAGE] [시각] key=value · ※ 연구·교육용 — 투자 권유가 아님. 과거 자료라 앞으로도 같다는 보장은 없음.
import importlib.util, json, time
from datetime import date, datetime, timezone
from pathlib import Path
import numpy as np
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("c", HERE.parent / "titles_2026-11-18" / "calc.py"); C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
fetch, log = C.fetch, C.log
VERSION = "v1.1"

def at(s, dt):
    d, c, a = s; i = int(np.searchsorted(d, dt, side="right") - 1); return i

def calc_P():
    K = fetch("^KS11", start=date(2025, 1, 1)); SS = fetch("005930.KS", start=date(2025, 1, 1)); HX = fetch("000660.KS", start=date(2025, 1, 1))
    KD = fetch("069500.KS", start=date(2025, 1, 1)); SPY = fetch("SPY", start=date(1993, 1, 1)); FX = fetch("KRW=X", start=date(2025, 1, 1))
    kd, kc, _ = K; pk = int(np.argmax(kc)); d0 = kd[pk]; d1 = kd[-1]
    def ret(s, adj=True):
        i0, i1 = at(s, d0), at(s, d1); v = s[2] if adj else s[1]; return float(v[i1] / v[i0])
    fx = float(FX[1][at(FX, d1)] / FX[1][at(FX, d0)])
    spy_usd = ret(SPY); spy_krw = spy_usd * fx
    people = {"삼성전자": ret(SS, False), "SK하이닉스": ret(HX, False), "KODEX 200 (코스피)": ret(KD), "S&P 500 (SPY, 원화)": spy_krw}
    out = {k: {"won": round(1e8 * v), "pct": round((v - 1) * 100, 1)} for k, v in people.items()}
    out["반반 (SK하이닉스 5천 + S&P 500 5천)"] = {"won": round(5e7 * people["SK하이닉스"] + 5e7 * spy_krw), "pct": round(((people["SK하이닉스"] + spy_krw) / 2 - 1) * 100, 1)}
    return {"start": str(d0), "end": str(d1), "kospi_peak": round(float(kc[pk]), 2), "usdkrw_change_pct": round((fx - 1) * 100, 1), "spy_usd_pct": round((spy_usd - 1) * 100, 1), "people": out}

def dca_value(d, v, start, end, monthly=500000):
    m = (d >= start) & (d <= end); dd, vv = d[m], v[m]
    firsts = [0] + [i for i in range(1, len(dd)) if dd[i].month != dd[i - 1].month]
    sh = sum(monthly / vv[i] for i in firsts); paid = monthly * len(firsts)
    return sh * vv[-1], paid, str(dd[-1])

def calc_R():
    G = fetch("^GSPC"); d, c, _ = G; out = {}
    for y, mth in ((2000, 3), (2002, 10), (2007, 10), (2009, 3)):
        end = date(y, mth, 28)
        val, paid, last = dca_value(d, c, date(y - 20, mth, 1), end)
        out[f"{y}-{mth:02d}"] = {"value_won": round(val), "paid_won": round(paid), "multiple": round(val / paid, 2), "last_day": last}
    return {"rule": "^GSPC 가격(배당 뺌) 20년 매달 50만 원 · 은퇴 달 마지막 거래일 값", "endings": out}

def lev2():
    N = fetch("^NDX", start=date(1985, 1, 1)); I = fetch("^IRX", start=date(1985, 1, 1)); Q = fetch("QLD", start=date(2006, 1, 1))
    d, c, _ = N; r = np.diff(c) / c[:-1]
    irx = np.array([I[1][min(max(at(I, x), 0), len(I[1]) - 1)] for x in d[1:]]) / 100
    lr = 2 * r - (0.0095 + irx) / 252
    sim = np.concatenate([[1.0], np.cumprod(1 + lr)])
    # 2006-06-21 부터 실제 QLD 로 이음
    qd, _, qa = Q; j0 = int(np.searchsorted(d, qd[0])); base = sim[j0] / qa[0]
    for k, x in enumerate(qd):
        j = int(np.searchsorted(d, x))
        if j < len(d) and d[j] == x: sim[j] = qa[k] * base
    return d, sim

def calc_L():
    d, q2 = lev2(); QQ = fetch("QQQ", start=date(1999, 3, 1)); qd, _, qa = QQ
    res = {}
    for name, (dd, vv) in (("QLD(2배)", (d, q2)), ("QQQ", (qd, qa))):
        m = dd >= date(2000, 3, 1); dd2, vv2 = dd[m], vv[m]
        firsts = [0] + [i for i in range(1, len(dd2)) if dd2[i].month != dd2[i - 1].month]
        sh = 0.0; paid = 0.0; under_last = None; fi = 0; worst = 0.0
        for i in range(len(dd2)):
            if fi < len(firsts) and firsts[fi] == i:
                sh += 500000 / vv2[i]; paid += 500000; fi += 1
            val = sh * vv2[i]
            worst = min(worst, val / paid - 1)
            if val < paid: under_last = dd2[i]
        res[name] = {"start": str(dd2[0]), "months": len(firsts), "paid_won": round(paid), "now_won": round(sh * vv2[-1]),
                     "worst_vs_paid_pct": round(worst * 100, 1), "last_day_below_paid": str(under_last),
                     "years_until_last_below": round((under_last - dd2[0]).days / 365.25, 1) if under_last else None}
    return res

def calc_D():
    gd, gc, _ = fetch("^GSPC"); sd, _, sa = fetch("SPY", start=date(1993, 1, 1))
    r = C.calc_E5(gd, gc, sd, sa, windows=((2008, 1, 5), (2000, 3, 5), (2007, 10, 5)))
    for k, v in r.items():
        paid = v["months"] * 500000
        v["paid_won"] = paid; v["keep_won"] = round(paid * (1 + v["keep_return_pct"] / 100)); v["pause_won"] = round(paid * (1 + v["pause_return_pct"] / 100))
    return r

def calc_X():
    SPY = fetch("SPY", start=date(1993, 1, 1)); FX = fetch("KRW=X", start=date(2025, 1, 1)); out = {}
    for d0 in (date(2026, 6, 22), date(2026, 10, 6)):
        i0, i1 = at(SPY, d0), len(SPY[0]) - 1; j0, j1 = at(FX, d0), len(FX[0]) - 1
        usd = SPY[2][i1] / SPY[2][i0]; fx = FX[1][j1] / FX[1][j0]
        out[str(d0)] = {"spy_usd_pct": round((usd - 1) * 100, 1), "usdkrw_pct": round((fx - 1) * 100, 1), "spy_krw_pct": round((usd * fx - 1) * 100, 1), "fx_start": round(float(FX[1][j0]), 1), "fx_now": round(float(FX[1][j1]), 1)}
    return out

def calc_K(thr=0.45):
    d, cl, _ = fetch("^KS11", start=date(1990, 1, 1)); ev = []; peak = cl[0]; pk = 0; i = 0
    while i < len(cl):
        if cl[i] > peak: peak, pk = cl[i], i
        if cl[i] <= peak * (1 - thr):
            k = i
            while k < len(cl) and cl[k] < peak: k += 1
            tr = i + int(np.argmin(cl[i:k])) if k > i else i
            ev.append({"peak": str(d[pk]), "hit": str(d[i]), "trough": str(d[tr]), "more_fall_pct": round(float(cl[tr] / cl[i] - 1) * 100, 1),
                       "worst_pct": round(float(cl[tr] / peak - 1) * 100, 1), "recovered": str(d[k]) if k < len(cl) else None,
                       "years_hit_to_recover": round((d[k] - d[i]).days / 365.25, 1) if k < len(cl) else None,
                       "years_peak_to_recover": round((d[k] - d[pk]).days / 365.25, 1) if k < len(cl) else None})
            i = k; peak = cl[k] if k < len(cl) else peak; pk = k; continue
        i += 1
    return {"rule": "^KS11 가격 · 고점 대비 −45% 를 처음 찍은 날 → 그 뒤 바닥까지 더 빠진 폭 · 고점 되찾기까지", "events": ev, "now": {"last": str(d[-1]), "close": round(float(cl[-1]), 2), "from_peak_pct": round(float(cl[-1] / cl.max() - 1) * 100, 1), "max_dd_pct": round(float(cl[d >= date(2026, 6, 22)].min() / cl.max() - 1) * 100, 1)}}

def calc_S():
    d, cl, _ = fetch("^KS11", start=date(1990, 1, 1)); out = {}
    for start in (date(1997, 1, 1), date(2000, 1, 1), date(2007, 1, 1), date(2010, 1, 1), date(2016, 1, 1)):
        m = d >= start; dd, cc = d[m], cl[m]
        firsts = set([0] + [i for i in range(1, len(dd)) if dd[i].month != dd[i - 1].month])
        sh_a = sh_b = cash_b = paid = 0.0; out_ = False; peak = cl[d < start].max() if (d < start).any() else cc[0]; sells = 0
        va_pk = vb_pk = 0.0; dd_a = dd_b = 0.0
        for i in range(len(dd)):
            if cc[i] > peak: peak = cc[i]
            if i in firsts:
                paid += 5e5; sh_a += 5e5 / cc[i]
                if out_: cash_b += 5e5
                else: sh_b += 5e5 / cc[i]
            if not out_ and cc[i] <= peak * 0.8:
                cash_b += sh_b * cc[i]; sh_b = 0; out_ = True; sells += 1; sell_peak = peak
            elif out_ and cc[i] >= sell_peak:
                sh_b += cash_b / cc[i]; cash_b = 0; out_ = False
            # 계좌 최대 낙폭 = 그때까지 계좌 최고 금액 대비 (넣은 돈 늘어나는 것 포함 — 대략)
            va, vb = sh_a * cc[i], sh_b * cc[i] + cash_b
            va_pk, vb_pk = max(va_pk, va), max(vb_pk, vb)
            dd_a, dd_b = min(dd_a, va / va_pk - 1), min(dd_b, vb / vb_pk - 1)
        out[str(start)] = {"paid_won": round(paid), "keep_won": round(sh_a * cc[-1]), "sell20_won": round(sh_b * cc[-1] + cash_b), "sells": sells, "sell20_now_in_cash": out_,
                           "keep_account_mdd_pct": round(dd_a * 100, 1), "sell20_account_mdd_pct": round(dd_b * 100, 1)}
    return {"rule": "^KS11 가격(배당 뺌) 매달 첫 거래일 50만 원 · 판 사람 = 고점 대비 −20% 면 다 팔고 현금(이자 0)으로 모으다 그 고점을 되찾으면 다시 다 삼", "starts": out}

def calc_H():
    out = {}
    for name, sym, st, old, frm in (("^KS11", "^KS11", date(1990, 1, 1), 1145.66, date(2007, 7, 1)), ("^GSPC", "^GSPC", date(1950, 1, 1), 0.0, date(1950, 1, 1)),
                                    ("^GSPC_2007", "^GSPC", date(1950, 1, 1), 0.0, date(2007, 7, 1))):
        d, cl, _ = fetch(sym, start=st); run = np.maximum.accumulate(np.maximum(cl, old))
        ath = [i for i in range(1, len(cl)) if cl[i] >= run[i - 1] and cl[i] > old and d[i] >= frm]
        o = {"from": str(frm), "ath_days": len(ath), "ath_days_by_year": {}}
        for i in ath: o["ath_days_by_year"][str(d[i].year)] = o["ath_days_by_year"].get(str(d[i].year), 0) + 1
        for H, tag in ((250, "1y"), (750, "3y")):
            r = np.array([cl[i + H] / cl[i] - 1 for i in ath if i + H < len(cl)])
            idx = np.array([i for i in range(len(cl) - H) if d[i] >= frm]); allr = cl[idx + H] / cl[idx] - 1
            o[tag] = {"with": int(len(r)), "loss_pct": round(float((r < 0).mean() * 100), 1), "median_pct": round(float(np.median(r) * 100), 1),
                      "worst_pct": round(float(r.min() * 100), 1), "all_days_loss_pct": round(float((allr < 0).mean() * 100), 1)}
        o["loss_1y_pct"] = o["1y"]["loss_pct"]; out[name] = o
    out["note"] = "코스피는 1994년 고점(1,145.66)을 처음 넘은 2007-07 부터 셈 (Yahoo 자료가 1996-12 부터) · ^GSPC_2007 = 같은 기간 S&P 500 · 1년 = 250 · 3년 = 750거래일 · 가격 지수 · 최고 날은 몇 해에 몰림(ath_days_by_year) — 날 수로 센 몫"
    return out

def calc_G():
    gd, gc, _ = fetch("^GSPC"); Id, Ic, _ = fetch("^IRX", start=date(1960, 1, 1))
    def irx(x):
        i = max(0, int(np.searchsorted(Id, x, side="right") - 1)); return Ic[i] / 100
    out = {}
    for y, mo in ((2000, 3), (2002, 10), (2007, 10), (2009, 3), (2020, 3), (2022, 10)):
        start, end = date(y - 20, mo, 1), date(y, mo, 28); m = (gd >= start) & (gd <= end); dd, cc = gd[m], gc[m]
        firsts = [0] + [i for i in range(1, len(dd)) if dd[i].month != dd[i - 1].month]
        pure = sum(5e5 / cc[i] for i in firsts) * cc[-1]
        g0 = date(y - 5, mo, 1); sh = cash = 0.0; nleft = len([i for i in firsts if dd[i] >= g0]); first = True
        for i in firsts:
            if not first: cash *= 1 + irx(dd[i]) / 12
            first = False
            if dd[i] < g0: sh += 5e5 / cc[i]
            else:
                cash += 5e5; mv = sh / max(1, nleft); sh -= mv; cash += mv * cc[i]; nleft -= 1
        out[f"{y}-{mo:02d}"] = {"paid_won": 5e5 * len(firsts), "stay_won": round(pure), "glide_won": round(sh * cc[-1] + cash), "end": str(dd[-1])}
    return {"rule": "^GSPC 가격(배당 뺌) 20년 매달 50만 원 · 나눠 옮김 = 은퇴 5년 전부터 새 돈은 현금, 주식은 남은 달 수로 나눠 매달 현금으로(13주 국채 ^IRX 이자) · 환율 뺌", "endings": out}

def calc_G2():
    gd, gc, _ = fetch("^GSPC"); Id, Ic, _ = fetch("^IRX", start=date(1960, 1, 1))
    def irx(x):
        i = max(0, int(np.searchsorted(Id, x, side="right") - 1)); return Ic[i] / 100
    mf = [0] + [i for i in range(1, len(gd)) if gd[i].month != gd[i - 1].month]; res = []
    for k in range(240, len(mf)):
        idx = mf[k - 240:k]; endi = mf[k]
        if gd[idx[0]] < date(1962, 1, 1): continue
        pure = sum(5e5 / gc[i] for i in idx) * gc[endi]; sh = cash = 0.0; nleft = 60
        for j, i in enumerate(idx):
            if j: cash *= 1 + irx(gd[i]) / 12
            if j < 180: sh += 5e5 / gc[i]
            else:
                cash += 5e5; mv = sh / max(1, nleft); sh -= mv; cash += mv * gc[i]; nleft -= 1
        cash *= 1 + irx(gd[endi]) / 12; res.append((str(gd[endi]), pure, sh * gc[endi] + cash))
    p = np.array([x[1] for x in res]); g = np.array([x[2] for x in res]); ip, ig = int(p.argmin()), int(g.argmin())
    q = lambda a, x: round(float(np.percentile(a, x)) / 1e8, 2)
    return {"rule": "^GSPC 가격(배당 뺌) · 은퇴 달 = 매달 첫 거래일(1982-01~지금) · 그 전 240달 매달 50만 원(넣은 돈 1.2억) · 나눠 옮김 = 마지막 60달은 새 돈 현금 + 주식을 남은 달 수로 나눠 현금으로(^IRX 이자)",
            "months": len(res), "first": res[0][0], "last": res[-1][0],
            "stay": {"min_eok": round(float(p.min()) / 1e8, 2), "min_at": res[ip][0], "glide_same_day_eok": round(float(g[ip]) / 1e8, 2), "p10_eok": q(p, 10), "median_eok": q(p, 50), "max_eok": q(p, 100)},
            "glide": {"min_eok": round(float(g.min()) / 1e8, 2), "min_at": res[ig][0], "p10_eok": q(g, 10), "median_eok": q(g, 50), "max_eok": q(g, 100)},
            "glide_more_pct": round(float((g > p).mean()) * 100, 1)}

def calc_C30():
    sd, _, sa = fetch("SPY"); Id, Ic, _ = fetch("^IRX", start=date(1960, 1, 1))
    def irx(x):
        i = max(0, int(np.searchsorted(Id, x, side="right") - 1)); return Ic[i] / 100
    out = {"rule": "SPY 수정 종가(배당 포함) 1993-01-29~ · 현금 = 13주 미국 국채(^IRX) 이자 · 해마다 첫 거래일에 비중을 다시 맞춤 · 달러 기준 · 세금·수수료 뺌"}
    for w in (1.0, 0.7, 0.5):
        vs, vc = w, 1 - w; v = [1.0]
        for i in range(1, len(sd)):
            vs *= sa[i] / sa[i - 1]; vc *= (1 + irx(sd[i])) ** ((sd[i] - sd[i - 1]).days / 365.25)
            if sd[i].year != sd[i - 1].year:
                t = vs + vc; vs, vc = t * w, t * (1 - w)
            v.append(vs + vc)
        v = np.array(v); pk = np.maximum.accumulate(v); yrs = (sd[-1] - sd[0]).days / 365.25; lu = 0; st = None
        for i in range(len(v)):
            if v[i] < pk[i]: st = i if st is None else st
            elif st is not None: lu = max(lu, (sd[i] - sd[st]).days); st = None
        if st is not None: lu = max(lu, (sd[-1] - sd[st]).days)
        r1 = v[250:] / v[:-250] - 1
        out[f"stock{int(w*100)}"] = {"cagr_pct": round(float(v[-1] ** (1 / yrs) - 1) * 100, 2), "mdd_pct": round(float((v / pk - 1).min()) * 100, 1),
                                     "longest_under_years": round(lu / 365.25, 1), "multiple": round(float(v[-1]), 2),
                                     "loss_1y_pct": round(float((r1 < 0).mean()) * 100, 1), "worst_1y_pct": round(float(r1.min()) * 100, 1)}
    return out

def calc_S_rules():
    d, cl, _ = fetch("^KS11", start=date(1990, 1, 1)); out = {}
    for start in (date(1997, 1, 1), date(2000, 1, 1), date(2007, 1, 1), date(2010, 1, 1), date(2016, 1, 1)):
        m = d >= start; dd, cc = d[m], cl[m]; fi = set([0] + [i for i in range(1, len(dd)) if dd[i].month != dd[i - 1].month]); row = {}
        for rule in ("peak", "sellpx", "low20"):
            sh_a = sh_b = cash = paid = 0.0; out_ = False; peak = cl[d < start].max() if (d < start).any() else cc[0]; sells = 0
            for i in range(len(dd)):
                if not out_ and cc[i] > peak: peak = cc[i]
                if i in fi:
                    paid += 5e5; sh_a += 5e5 / cc[i]
                    if out_: cash += 5e5
                    else: sh_b += 5e5 / cc[i]
                if not out_ and cc[i] <= peak * 0.8:
                    cash += sh_b * cc[i]; sh_b = 0; out_ = True; sells += 1; sp = peak; spx = cc[i]; low = cc[i]
                elif out_:
                    low = min(low, cc[i])
                    if (rule == "peak" and cc[i] >= sp) or (rule == "sellpx" and cc[i] >= spx) or (rule == "low20" and cc[i] >= low * 1.2):
                        sh_b += cash / cc[i]; cash = 0; out_ = False; peak = cc[i]
            row[rule] = {"keep_eok": round(sh_a * cc[-1] / 1e8, 2), "sell_eok": round((sh_b * cc[-1] + cash) / 1e8, 2), "sells": sells, "now_cash": out_}
        out[str(start)] = row
    return {"rule": "S 와 같고 되사는 때만 바꿈 — peak = 판 때의 전 고점 회복 · sellpx = 판 값 회복 · low20 = 판 뒤 바닥에서 +20%", "starts": out}

def main():
    t0 = time.time(); out = {"tool": f"calc.py {VERSION}", "made": datetime.now(timezone.utc).isoformat(timespec="seconds")}
    out["P_kospi_peak_4people"] = calc_P(); log("P", **{k: v["pct"] for k, v in out["P_kospi_peak_4people"]["people"].items()}, start=out["P_kospi_peak_4people"]["start"])
    out["R_retire_timing"] = calc_R(); log("R", **{k: v["multiple"] for k, v in out["R_retire_timing"]["endings"].items()})
    out["L_qld_dca_2000"] = calc_L(); log("L", **{k: (v["worst_vs_paid_pct"], v["years_until_last_below"], v["now_won"]) for k, v in out["L_qld_dca_2000"].items()})
    out["D_dca_pause_won"] = calc_D(); log("D", **{k: (v["keep_won"], v["pause_won"]) for k, v in out["D_dca_pause_won"].items()})
    out["K_kospi40"] = calc_K(0.40); log("K40", events=[(e["hit"], e["more_fall_pct"], e["years_hit_to_recover"]) for e in out["K_kospi40"]["events"]])
    out["K_kospi45"] = calc_K(); log("K", events=[(e["hit"], e["more_fall_pct"], e["years_hit_to_recover"]) for e in out["K_kospi45"]["events"]])
    out["S_sell20_kospi"] = calc_S(); log("S", **{k: (v["keep_won"], v["sell20_won"]) for k, v in out["S_sell20_kospi"]["starts"].items()})
    out["H_ath_buy"] = calc_H(); log("H", **{k: v["loss_1y_pct"] for k, v in out["H_ath_buy"].items() if isinstance(v, dict)})
    out["G_glide"] = calc_G(); log("G", **{k: (v["stay_won"], v["glide_won"]) for k, v in out["G_glide"]["endings"].items()})
    out["G2_glide_all"] = calc_G2(); log("G2", months=out["G2_glide_all"]["months"], stay=out["G2_glide_all"]["stay"], glide=out["G2_glide_all"]["glide"], glide_more_pct=out["G2_glide_all"]["glide_more_pct"])
    out["C30_cash_mix"] = calc_C30(); log("C30", **{k: (v["cagr_pct"], v["mdd_pct"], v["multiple"], v["loss_1y_pct"]) for k, v in out["C30_cash_mix"].items() if k != "rule"})
    out["S_rules"] = calc_S_rules(); log("S_rules", **{k: {r: (x["keep_eok"], x["sell_eok"]) for r, x in v.items()} for k, v in out["S_rules"]["starts"].items()})
    out["X_fx"] = calc_X(); log("X", **{k: (v["spy_usd_pct"], v["usdkrw_pct"], v["spy_krw_pct"]) for k, v in out["X_fx"].items()})
    (HERE / "result.json").write_text(json.dumps(out, ensure_ascii=False, indent=1, default=str), encoding="utf-8")
    log("DONE", seconds=round(time.time() - t0, 1))

if __name__ == "__main__":
    main()
