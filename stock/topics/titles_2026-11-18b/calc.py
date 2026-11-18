#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-11-18 — 사용자가 고른 성공 사례 8편을 본뜬 다음 제목 5안의 숫자 (사용자 지시 "…이것들만 성공 사례로 해서 왜 조회수가 많이 터졌는지 … 분석해서 다음으로 조회수가 많이 나올만할 제목 5개 만들어봐").
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
VERSION = "v1.0"

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

def main():
    t0 = time.time(); out = {"tool": f"calc.py {VERSION}", "made": datetime.now(timezone.utc).isoformat(timespec="seconds")}
    out["P_kospi_peak_4people"] = calc_P(); log("P", **{k: v["pct"] for k, v in out["P_kospi_peak_4people"]["people"].items()}, start=out["P_kospi_peak_4people"]["start"])
    out["R_retire_timing"] = calc_R(); log("R", **{k: v["multiple"] for k, v in out["R_retire_timing"]["endings"].items()})
    out["L_qld_dca_2000"] = calc_L(); log("L", **{k: (v["worst_vs_paid_pct"], v["years_until_last_below"], v["now_won"]) for k, v in out["L_qld_dca_2000"].items()})
    out["D_dca_pause_won"] = calc_D(); log("D", **{k: (v["keep_won"], v["pause_won"]) for k, v in out["D_dca_pause_won"].items()})
    out["X_fx"] = calc_X(); log("X", **{k: (v["spy_usd_pct"], v["usdkrw_pct"], v["spy_krw_pct"]) for k, v in out["X_fx"].items()})
    (HERE / "result.json").write_text(json.dumps(out, ensure_ascii=False, indent=1, default=str), encoding="utf-8")
    log("DONE", seconds=round(time.time() - t0, 1))

if __name__ == "__main__":
    main()
