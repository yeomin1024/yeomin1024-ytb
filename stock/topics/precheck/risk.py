#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-29 — 최초. 정답 기준 = **리스크를 줄이면서 안정적 수익** (사용자 지시 2026-10-29 "기존 3건(재무제표, 매수 시기, 포트폴리오)도
#          기준을 리스크를 줄이면서 안정적 수익내는걸 기준으로 해서 다시 구성해봐 주제는 좋으니까") + 주제 탐색 3회차 새 후보(T043~T055)·T022 다시 짬.
#
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.0 | 2026-10-29 | 최초 (같은 날 고침: 팔기 규칙이 사기 분기로 들어가던 것 · classify_diff 뒤집힘 기준 · SCHD 항목 · 재무제표 사례 5곳 모두) — 안정 수익 확률 · 기존 3편(포트폴리오·매수 시기·재무제표) 다시 계산 · 새 후보 13개 + T022 | 전부 |
#
# **안정 수익** (한 구간): ① 끝에 예금(미국 단기 국채 이자 ^IRX)보다 더 남고 ② 그사이 한 번도 원금(처음 넣은 돈)보다 L(기본 20%) 넘게 줄지 않음.
#   안정 수익 확률 = 그런 구간의 몫. 비교는 '그 선택의 확률 − 비교 대상의 확률'(%p). 칸 = 기간(2·5년) × 시작 시기(2000~08 / 2009~) × L(15·20·25%).
#   분류(classify_diff): 어느 칸에서도 1%p 넘게 뒤집히지 않고 기본 칸(5년·2009~·L20) ≥ 5%p → 정답형 · 모든 칸 3%p 안 → 차이없음 · 늘 같은 방향이지만 5%p 미만 → 차이 작음 · 그 밖 조건부형.
# 미리 보기 점검: 규칙(10% 빠지면 사기·팔기, 재무 경고)은 그날까지 알려진 값만 — 재무 수치는 회계연도 끝 + 122일(발표 뒤)부터.
# ⚠ 생존 편향: 종목 자료는 지금 S&P 500 회사만 — 함수마다 why 에 편향 방향.
# ※ 연구·교육용 — 투자 권유가 아님.
import json
from datetime import date

import numpy as np

import stocks as S

VERSION = "v1.0"
YEAR = 365
LS = (0.15, 0.20, 0.25)
SEED = 20261029


def pct(x, nd=1):
    return "-" if x is None or x != x else f"{x * 100:.{nd}f}%"


def pp(x):
    return "-" if x is None or x != x else f"{x * 100:+.1f}%p"


def stable(v, c, L=0.20):
    """v·c = 같은 구간의 값(처음 = 1) — 끝에 예금보다 더 남고 원금보다 L 넘게 준 적 없음."""
    return bool(v[-1] > c[-1] and np.nanmin(v) >= 1 - L)


TIE = 0.01      # 1%p 안은 같음으로 봄


def classify_diff(cm, main_key=None):
    """v1.1 (같은 날 첫 계산 뒤 고침 — 처음 '모든 칸 3%p 이상' 문턱은 근거 없이 정한 값이었고, README 의 조건부형 뜻은 '칸에 따라 이긴 쪽이 바뀜'):
    정답형 = 어느 칸에서도 반대쪽으로 1%p 넘게 뒤집히지 않고 + 기본 칸(없으면 평균) 5%p 이상 · 차이없음 = 모든 칸 3%p 안 · 방향은 늘 같지만 기본 칸 5%p 미만 = '차이 작음' · 그 밖 조건부형."""
    v = [x for x in cm.values() if x is not None]
    if not v:
        return "미확인", "칸 없음"
    m = cm.get(main_key) if main_key and cm.get(main_key) is not None else float(np.mean(v))
    if all(abs(x) < 0.03 for x in v):
        return "차이없음", f"모든 칸 {pp(min(v))}~{pp(max(v))}"
    if all(x > -TIE for x in v):
        side = "그 선택이 더 높음"
    elif all(x < TIE for x in v):
        side = "비교 대상이 더 높음"
    else:
        return "조건부형", f"칸에 따라 뒤집힘 {pp(min(v))}~{pp(max(v))}"
    if abs(m) >= 0.05:
        return "정답형", f"어느 칸에서도 뒤집히지 않음 · {side} · 기본 칸 {pp(m)} · 범위 {pp(min(v))}~{pp(max(v))}"
    return "차이 작음", f"방향은 늘 같음({side})이지만 기본 칸 {pp(m)} — 5%p 미만"


def matrix(I, P, start=date(1999, 1, 1)):
    """지금 구성 종목 수정 종가를 지수 날짜에 맞춘 표 (행 = 거래일, 열 = 종목 · 자료 전·뒤는 nan)."""
    i0 = int(np.searchsorted(I.o, start.toordinal()))
    o = I.o[i0:]
    syms = sorted(P)
    A = np.full((len(o), len(syms)), np.nan)
    for j, s in enumerate(syms):
        p = P[s]
        k = np.searchsorted(p.o, o, side="right") - 1
        ok = (k >= 0) & (o <= p.o[-1])
        A[ok, j] = p.adj[k[ok]]
    return i0, o, syms, A


def win_cells(starts_year, values, L_key=None):
    """구간 시작 연도 → 앞(2000~08)·뒤(2009~) 평균."""
    y = np.array(starts_year)
    v = np.array(values, dtype=float)
    out = {}
    for lab, m in (("앞", (y >= 2000) & (y <= 2008)), ("뒤", y >= 2009)):
        out[lab] = float(np.nanmean(v[m])) if m.sum() >= 12 else None
    return out


# ================================================================ 기존 편 1 — 포트폴리오
def ep_portfolio(B, I, P, F):
    """항목마다 'S&P 500 만' vs 그 선택의 안정 수익 확률 (2·5년 · 매달 시작 · L 15·20·25%)."""
    ser = {s: B.series(s) for s in ("QQQ", "DVY", "SCHD", "AGG", "EFA")}
    r = np.concatenate([[0.0], B.tr[1:] / B.tr[:-1] - 1])
    lev2 = np.cumprod(1 + 2 * r - (B.irx / 100 + 0.009) / 252)

    def mix(parts, s, e, rebal=252):
        val = np.ones(e - s + 1)
        units = [wt / v[s] for v, wt in parts]
        last = s
        for k, i in enumerate(range(s, e + 1)):
            tot = sum(u * v[i] for u, (v, _) in zip(units, parts))
            val[k] = tot
            if i - last >= rebal:
                units = [tot * wt / v[i] for (v, wt) in parts]
                last = i
        return val

    def path(v, s, e):
        seg = v[s:e + 1]
        return seg / seg[0]

    i0, o, syms, A = matrix(I, P)                              # B 와 I 는 같은 날짜 (I = stocks.Ix(B))
    items = {
        "2 기술주(QQQ)만": lambda s, e: path(ser["QQQ"], s, e),
        "3 배당 ETF(DVY — 2003년 11월부터)": lambda s, e: path(ser["DVY"], s, e),
        "3b 배당 ETF(SCHD — 2011년 10월부터)": lambda s, e: path(ser["SCHD"], s, e),
        "4 레버리지 2배를 10% 섞기": lambda s, e: mix([(B.tr, 0.9), (lev2, 0.1)], s, e),
        "4b 레버리지 2배를 50% 섞기": lambda s, e: mix([(B.tr, 0.5), (lev2, 0.5)], s, e),
        "5 주식60·미국채권20·해외주식20 (1년마다 맞춤)": lambda s, e: mix([(B.tr, 0.6), (ser["AGG"], 0.2), (ser["EFA"], 0.2)], s, e),
        "5b 주식60·채권40 (1년마다 맞춤)": lambda s, e: mix([(B.tr, 0.6), (ser["AGG"], 0.4)], s, e),
    }
    res = {}
    for name, f in items.items():
        cells, detail = {}, {}
        for h in ("2y", "5y"):
            for L in LS:
                ys, a, b, ra, rb, ma, mb = [], [], [], [], [], [], []
                for s, e, _ in B.W[h]:
                    try:
                        vb = f(s, e)
                    except Exception:
                        continue
                    if vb is None or np.isnan(vb).any():
                        continue
                    va, c = path(B.tr, s, e), path(B.cash, s, e)
                    ys.append(B.d[s].year)
                    a.append(stable(va, c, L)); b.append(stable(vb, c, L))
                    ra.append(va[-1] - 1); rb.append(vb[-1] - 1); ma.append(va.min() - 1); mb.append(vb.min() - 1)
                for lab, m in (("앞", (np.array(ys) <= 2008)), ("뒤", (np.array(ys) >= 2009))):
                    if m.sum() < 12:
                        continue
                    k = f"{h}·{lab}·L{int(L * 100)}"
                    pa, pb = float(np.mean(np.array(a)[m])), float(np.mean(np.array(b)[m]))
                    cells[k] = pb - pa
                    if L == 0.20:
                        detail[f"{h}·{lab}"] = {"n": int(m.sum()), "spx_stable": pct(pa), "alt_stable": pct(pb),
                                                "spx_ret_median": pct(float(np.median(np.array(ra)[m]))), "alt_ret_median": pct(float(np.median(np.array(rb)[m]))),
                                                "spx_worst_from_start_median": pct(float(np.median(np.array(ma)[m]))), "alt_worst_from_start_median": pct(float(np.median(np.array(mb)[m]))),
                                                "spx_worst": pct(float(np.min(np.array(ma)[m]))), "alt_worst": pct(float(np.min(np.array(mb)[m])))}
        cl, why = classify_diff(cells, "5y·뒤·L20" if "5y·뒤·L20" in cells else None)
        res[name] = {"class": cl, "why": why, "cells": {k: pp(v) for k, v in cells.items()}, "detail": detail,
                     "answer": "안정 수익 확률(그 선택 − S&P 500 만): " + " · ".join(f"{k} {pp(v)}" for k, v in cells.items() if k.endswith("L20"))}
    res["1 한 종목만"] = _single_stock(B, I, A, i0)
    return res


def _single_stock(B, I, A, i0):
    """지금 S&P 500 종목 하나만 (그 구간 시작에 자료가 있는 모든 종목의 평균 확률) vs S&P 500 — 빠진 회사가 없어 한 종목 쪽을 좋게 보는 쪽."""
    cells, detail = {}, {}
    for h in ("2y", "5y"):
        for L in (0.20,):
            ys, a, b = [], [], []
            for s, e, _ in B.W[h]:
                if s < i0:
                    continue
                seg = A[s - i0:e - i0 + 1]
                ok = ~np.isnan(seg[0]) & ~np.isnan(seg[-1])
                if ok.sum() < 100:
                    continue
                R = seg[:, ok] / seg[0, ok]
                c = B.cash[s:e + 1] / B.cash[s]
                va = B.tr[s:e + 1] / B.tr[s]
                st = (R[-1] > c[-1]) & (np.nanmin(R, axis=0) >= 1 - L)
                ys.append(B.d[s].year); a.append(stable(va, c, L)); b.append(float(st.mean()))
            y = np.array(ys)
            for lab, m in (("앞", y <= 2008), ("뒤", y >= 2009)):
                if m.sum() < 12:
                    continue
                pa, pb = float(np.mean(np.array(a)[m])), float(np.mean(np.array(b)[m]))
                cells[f"{h}·{lab}"] = pb - pa
                detail[f"{h}·{lab}"] = {"n": int(m.sum()), "spx_stable": pct(pa), "one_stock_stable": pct(pb)}
    cl, why = classify_diff(cells)
    return {"class": cl, "why": why + " · 빠진 회사가 없어 한 종목 쪽 확률을 크게 보는 쪽 — S&P 500 이 높으면 결론은 더 단단", "cells": {k: pp(v) for k, v in cells.items()},
            "detail": detail, "answer": "안정 수익 확률(한 종목 − S&P 500): " + " · ".join(f"{k} {pp(v)}" for k, v in cells.items())}


# ================================================================ 기존 편 2 — 매수 시기
def ep_timing(B, I, P, F):
    """10만 달러를 매달 첫 거래일에 — 선택마다 안정 수익 확률 (그 구간 '예금만' 보다 더 남고 원금 −L 넘게 안 줄어듦)."""
    ms = np.array(B.ms)
    px = B.price

    def first_ge(day):
        return int(np.searchsorted(I.o, day, side="left"))

    def run(opt, s, e):
        C = B.cash[s:e + 1] / B.cash[s]
        T = B.tr[s:e + 1] / B.tr[s]
        n = e - s + 1
        if opt == "한 번에":
            return T
        if opt.startswith("나눠"):
            k = int("".join(ch for ch in opt if ch.isdigit()))
            m = [x - s for x in ms[(ms >= s)][:k]]
            v = np.zeros(n)
            cash = C.copy()
            for j in m:
                cash[j:] -= (1 / k) * C[j:] / C[j]
                v[j:] += (1 / k) * T[j:] / T[j]
            return v + cash
        if opt == "석 달 뒤":
            j = int(ms[ms >= s][3] - s) if (ms >= s).sum() > 3 else n
            v = C.copy()
            if j < n:
                v[j:] = C[j] * T[j:] / T[j]
            return v
        if opt == "10% 빠지면 팔고 6개월 뒤":
            seg = px[s:e + 1]
            hit = np.flatnonzero(seg <= 0.9 * px[s])
            if not len(hit):
                return T
            f = int(hit[0])
            g = first_ge(int(I.o[s + f]) + 182) - s
            v = T.copy()
            if g >= n:
                v[f:] = T[f] * C[f:] / C[f]
            else:
                v[f:g] = T[f] * C[f:g] / C[f]
                v[g:] = T[f] * C[g] / C[f] * T[g:] / T[g]
            return v
        if opt.startswith("10% 빠지면 사기"):
            lim = YEAR if "1년" in opt else 5 * YEAR
            o0 = int(I.o[s])
            seg = px[s:e + 1]
            hit = np.flatnonzero((seg <= 0.9 * px[s]) & (I.o[s:e + 1] <= o0 + lim))
            if len(hit):
                j = int(hit[0])
            elif "1년" in opt:
                j = first_ge(o0 + YEAR) - s
            else:
                j = n
            v = C.copy()
            if j < n:
                v[j:] = C[j] * T[j:] / T[j]
            return v
        raise ValueError(opt)

    opts = ["한 번에", "나눠 6개월", "나눠 12개월", "석 달 뒤", "10% 빠지면 사기(1년까지)", "10% 빠지면 사기(5년까지)", "10% 빠지면 팔고 6개월 뒤"]
    out = {}
    base = {}
    for opt in opts:
        cells, detail = {}, {}
        for h in ("2y", "5y"):
            for L in LS:
                ys, st, rets, worst = [], [], [], []
                for s, e, _ in B.W[h]:
                    v = run(opt, s, e)
                    c = B.cash[s:e + 1] / B.cash[s]
                    ys.append(B.d[s].year); st.append(stable(v, c, L)); rets.append(v[-1] - 1); worst.append(v.min() - 1)
                y = np.array(ys)
                for lab, m in (("앞", y <= 2008), ("뒤", y >= 2009)):
                    k = f"{h}·{lab}·L{int(L * 100)}"
                    p = float(np.mean(np.array(st)[m]))
                    base.setdefault(opt, {})[k] = p
                    if L == 0.20:
                        detail[f"{h}·{lab}"] = {"n": int(m.sum()), "stable": pct(p), "ret_median": pct(float(np.median(np.array(rets)[m]))),
                                                "worst_from_start_median": pct(float(np.median(np.array(worst)[m]))), "worst": pct(float(np.min(np.array(worst)[m]))),
                                                "loss_vs_start_20": pct(float(np.mean(np.array(worst)[m] < -0.20)))}
        out[opt] = {"detail": detail}
    for opt in opts[1:]:
        cells = {k: base[opt][k] - base["한 번에"][k] for k in base[opt]}
        cl, why = classify_diff(cells, "5y·뒤·L20")
        out[opt].update({"class": cl, "why": why, "cells": {k: pp(v) for k, v in cells.items()},
                         "answer": "안정 수익 확률(이 선택 − 한 번에): " + " · ".join(f"{k} {pp(v)}" for k, v in cells.items() if k.endswith("L20"))})
    out["한 번에"].update({"class": "기준", "answer": " · ".join(f"{k} {pct(v)}" for k, v in base["한 번에"].items() if k.endswith("L20"))})
    return out


# ================================================================ 기존 편 3 — 재무제표
def _fa(F2, s, key):
    return {date.fromisoformat(k): v for k, v in (F2.get(s, {}).get(key) or {}).items()}


def load_fa2():
    out = {}
    for fp in sorted((S.BULK / "fa2").glob("*.json")):
        out[fp.stem] = json.loads(fp.read_text("utf-8"))["series"]
    return out


def ep_jaemu(B, I, P, F):
    """싸 보이는 회사(PER 15 미만) 중 '경고'(매출 감소 + 빚을 감당할 힘 약함 — 이자보상 4배 미만 또는 빚 ÷ 영업이익 5배 넘음) vs '깨끗'(매출 늘고 둘 다 아님)
    → 회계연도 끝 + 122일에 사서 1년 뒤: 30% 넘게 빠진 적 · 안정 수익(예금보다 더 + 20% 넘게 안 빠짐) — 지금 구성 종목만(경고 쪽 위험을 작게 보는 쪽)."""
    F2 = load_fa2()
    rows = []
    for s, p in P.items():
        rev, eps = S._fy(F, s, "annualTotalRevenue"), S._fy(F, s, "annualDilutedEPS")
        oi, ie, debt = _fa(F2, s, "annualOperatingIncome"), _fa(F2, s, "annualInterestExpense"), _fa(F2, s, "annualTotalDebt")
        ks = sorted(rev)
        for e0, e1 in zip(ks, ks[1:]):
            if not (300 <= (e1 - e0).days <= 430) or e1 not in eps or eps[e1] <= 0:
                continue
            t0 = I.next_trading(e1.toordinal() + 122)
            if not p.has(t0, t0 + YEAR) or t0 + YEAR > I.last:
                continue
            pe = p.at(t0, "close") / eps[e1]
            o_, i_, d_ = oi.get(e1), ie.get(e1), debt.get(e1, 0.0)
            if o_ is None:
                continue
            cover = (o_ / i_) if i_ and i_ > 0 else float("inf")
            d_oi = (d_ / o_) if o_ > 0 else float("inf")
            weak = cover < 4 or d_oi > 5
            down = rev[e1] < rev[e0]
            k0 = int(np.searchsorted(p.o, t0))
            k1 = int(np.searchsorted(p.o, t0 + YEAR, side="right")) - 1
            path = p.adj[k0:k1 + 1] / p.adj[k0]
            c = I.at(t0 + YEAR, I.cash) / I.at(t0, I.cash)
            rows.append({"sym": s, "fy": e1.isoformat(), "t0y": date.fromordinal(t0).year, "pe": pe, "warn": down and weak, "clean": (not down) and (not weak),
                         "down": down, "weak": weak, "big_loss": bool(path.min() <= 0.70), "stable": bool(path[-1] > c and path.min() >= 0.80),
                         "ret": float(path[-1] - 1)})
    cheap = [r for r in rows if r["pe"] < 15]
    out = {"n_all": len(rows), "n_cheap": len(cheap)}
    for scope, R in (("싸 보이는 회사(PER 15 미만)", cheap), ("모든 흑자 회사", rows)):
        cells, tab = {}, {}
        for y in sorted({r["t0y"] for r in R}):
            w = [r for r in R if r["t0y"] == y and r["warn"]]
            c = [r for r in R if r["t0y"] == y and r["clean"]]
            if len(w) < 5 or len(c) < 5:
                continue
            tab[str(y)] = {"warn_n": len(w), "clean_n": len(c), "warn_big_loss": pct(np.mean([r["big_loss"] for r in w])), "clean_big_loss": pct(np.mean([r["big_loss"] for r in c])),
                           "warn_stable": pct(np.mean([r["stable"] for r in w])), "clean_stable": pct(np.mean([r["stable"] for r in c])),
                           "warn_ret_median": pct(float(np.median([r["ret"] for r in w]))), "clean_ret_median": pct(float(np.median([r["ret"] for r in c])))}
            cells[str(y)] = float(np.mean([r["stable"] for r in c]) - np.mean([r["stable"] for r in w]))
        cl, why = classify_diff(cells)
        out[scope] = {"class": cl, "why": why + " (값 = 깨끗 − 경고, 안정 수익 확률) · 경고 쪽 위험은 빠진 회사가 없어 작게 잡힘", "cells": {k: pp(v) for k, v in cells.items()}, "table": tab}
    out["cases"] = _jaemu_cases(I, P)
    return out


def _jaemu_cases(I, P):
    cases = [("RL", "랄프로렌", "2024-07-31"), ("KSS", "콜스", "2024-06-03"), ("EXPE", "익스피디아", "2024-05-01"), ("BBWI", "배스앤바디웍스", "2024-06-03"), ("URBN", "어반아웃피터스", "2024-06-03")]
    out = []
    for s, name, d0 in cases:
        p = P.get(s)
        if p is None:                                         # 지금 S&P 500 이 아닌 회사(콜스·배스앤바디웍스·어반아웃피터스) — 따로 받음 (precheck data/)
            f = S.fetch(s)
            p = S.Px()
            p.o = np.array([x.toordinal() for x in f["d"]])
            p.adj, p.close, p.div = f["adj"], f["close"], f["div"]
        t0 = I.next_trading(date.fromisoformat(d0).toordinal())
        r = {"sym": s, "name": name, "t0": d0}
        for h, lab in ((YEAR, "1y"), (2 * YEAR, "2y")):
            if t0 + h > I.last:
                continue
            k0 = int(np.searchsorted(p.o, t0))
            k1 = int(np.searchsorted(p.o, t0 + h, side="right")) - 1
            path = p.adj[k0:k1 + 1] / p.adj[k0]
            c = I.at(t0 + h, I.cash) / I.at(t0, I.cash)
            r[lab] = {"end_10k": round(10000 * path[-1]), "worst_from_start": pct(path.min() - 1), "stable": bool(path[-1] > c and path.min() >= 0.8),
                      "big_loss_30": bool(path.min() <= 0.7)}
        out.append(r)
    return out


EPISODES = {"portfolio-test-2026-10": ep_portfolio, "timing-test-2026-10": ep_timing, "jaemu-test-2026-10": ep_jaemu}


# ================================================================ 새 후보 (3회차)
def t043(B, I, P, F):
    """무작위 1·5·10·30종목(같은 금액, 그대로 둠) vs S&P 500 — 3년 구간 1월 시작 2010~2023 · 주마다 값으로 '가장 크게 줄어든 때'."""
    rng = np.random.default_rng(SEED)
    i0, o, syms, A = matrix(I, P)
    rows = {}
    for Y in range(2010, 2024):
        s = int(np.searchsorted(I.o, date(Y, 1, 1).toordinal()))
        e = int(np.searchsorted(I.o, date(Y + 3, 1, 1).toordinal())) - 1
        if e >= len(I.o):
            continue
        seg = A[s - i0:e - i0 + 1]
        ok = ~np.isnan(seg[0]) & ~np.isnan(seg[-1])
        R = seg[:, ok] / seg[0, ok]
        R = R[np.r_[0:len(R):5, len(R) - 1]]
        c = I.cash[e] / I.cash[s]
        idx = I.tr[s:e + 1] / I.tr[s]
        r = {"n_stocks": int(ok.sum()), "index": {"lost30": bool(idx.min() <= 0.7), "stable": bool(idx[-1] > c and idx.min() >= 0.8), "ret": pct(idx[-1] - 1)}}
        for k in (1, 5, 10, 30):
            if k == 1:
                V = R
            else:
                pick = np.array([rng.choice(R.shape[1], k, replace=False) for _ in range(2000)])
                V = R[:, pick].mean(axis=2)
            mn, end = np.nanmin(V, axis=0), V[-1]
            r[str(k)] = {"lost30": float(np.mean(mn <= 0.7)), "stable": float(np.mean((end > c) & (mn >= 0.8))), "beat_index": float(np.mean(end > idx[-1]))}
        rows[f"{Y}-01~{Y + 3}-01"] = r
    def avg(k, key, yrs):
        return float(np.mean([v[k][key] for kk, v in rows.items() if int(kk[:4]) in yrs]))
    early, late = range(2010, 2017), range(2017, 2024)
    summ = {k: {"lost30_2010_16": pct(avg(k, "lost30", early)), "lost30_2017_23": pct(avg(k, "lost30", late)), "stable_all": pct(avg(k, "stable", range(2010, 2024))),
                "beat_index_all": pct(avg(k, "beat_index", range(2010, 2024)))} for k in ("1", "5", "10", "30")}
    idx_lost = sum(v["index"]["lost30"] for v in rows.values())
    idx_st = float(np.mean([v["index"]["stable"] for v in rows.values()]))
    # v1.0 고침(첫 계산 뒤): '원금 30% 넘게 줄어든 확률'은 시장 전체가 30% 넘게 빠진 구간(2020년 시작)에선 종목이 많을수록 오히려 높아져(평균에 모임) 단조가 아님
    #   → 안정 수익 확률로 봄: 지수가 안정적이었던 구간에서 1 < 5 < 10 < 30 인지 · 결론은 14구간 평균(사실형)
    calm = [v for v in rows.values() if v["index"]["stable"]]
    mono = all(v["1"]["stable"] <= v["5"]["stable"] <= v["10"]["stable"] + 0.005 <= v["30"]["stable"] + 0.01 for v in calm)
    cl = "사실형"
    return {"class": cl, "answer": f"원금이 30% 넘게 줄어든 적 있을 확률(3년, 14구간 평균): 1개 {summ['1']['lost30_2010_16']}/{summ['1']['lost30_2017_23']}(앞/뒤 구간) · 5개 {summ['5']['lost30_2017_23']} · "
                                   f"10개 {summ['10']['lost30_2017_23']} · 30개 {summ['30']['lost30_2017_23']}(뒤) · 지수는 14구간 중 {idx_lost}번 · 안정 수익 확률: 1개 {summ['1']['stable_all']} · 30개 {summ['30']['stable_all']} · 지수 {pct(idx_st)}",
            "summary": summ, "table": {k: {kk: (vv if kk in ('n_stocks', 'index') else {a: pct(b) for a, b in vv.items()}) for kk, vv in v.items()} for k, v in rows.items()},
            "why": f"지수가 안정적이었던 {len(calm)}구간에서 종목이 많을수록 안정 수익 확률이 높았는지 = {mono} · 나머지 {len(rows) - len(calm)}구간(2020·2022년 시작)은 지수 자체가 20% 넘게 빠져 종목이 많을수록 지수처럼 같이 실패 · 빠진 회사가 없어 한 종목 위험을 작게 보는 쪽(결론 쪽으로 단단) · 시드 {SEED} · 2,000번 뽑기 · 주마다 값(하루 값보다 하락폭을 조금 작게 봄)"}


def t044(B, I, P, F):
    """연말마다 지난 1년 하루 변동 폭 다섯 묶음 → 다음 1년 (20% 넘게 빠진 적 · 안정 수익 · 수익)."""
    rows = {}
    for Y in range(2009, 2025):
        c0 = I.next_trading(date(Y + 1, 1, 1).toordinal()) - 1
        c0 = int(I.o[int(np.searchsorted(I.o, c0, side="right")) - 1])
        c1 = c0 + YEAR
        if c1 > I.last:
            continue
        cash = I.at(c1, I.cash) / I.at(c0, I.cash)
        vals = []
        for s, p in P.items():
            k0 = int(np.searchsorted(p.o, c0, side="right")) - 1
            if k0 < 253 or p.o[-1] < c1:
                continue
            lr = np.diff(np.log(p.adj[k0 - 252:k0 + 1]))
            vol = float(np.std(lr)) * np.sqrt(252)
            k1 = int(np.searchsorted(p.o, c1, side="right")) - 1
            path = p.adj[k0:k1 + 1] / p.adj[k0]
            vals.append((vol, bool(path.min() <= 0.8), bool(path[-1] > cash and path.min() >= 0.8), float(path[-1] - 1)))
        vals.sort()
        q = len(vals) // 5
        lo, hi = vals[:q], vals[-q:]
        rows[str(Y + 1)] = {"n": len(vals), "low_dd20": float(np.mean([v[1] for v in lo])), "high_dd20": float(np.mean([v[1] for v in hi])),
                            "low_stable": float(np.mean([v[2] for v in lo])), "high_stable": float(np.mean([v[2] for v in hi])),
                            "low_ret": float(np.mean([v[3] for v in lo])), "high_ret": float(np.mean([v[3] for v in hi])),
                            "low_ret_med": float(np.median([v[3] for v in lo])), "high_ret_med": float(np.median([v[3] for v in hi]))}
    cm = {y: r["low_stable"] - r["high_stable"] for y, r in rows.items()}
    cl, why = classify_diff({y: v for y, v in cm.items()})
    risk_lower = sum(1 for r in rows.values() if r["low_dd20"] < r["high_dd20"])
    ret_higher = sum(1 for r in rows.values() if r["low_ret_med"] > r["high_ret_med"])
    n = len(rows)
    return {"class": cl, "answer": f"덜 출렁인 20% vs 많이 출렁인 20% (다음 1년, {n}해): 20% 넘게 빠진 확률 평균 {pct(np.mean([r['low_dd20'] for r in rows.values()]))} vs {pct(np.mean([r['high_dd20'] for r in rows.values()]))} "
                                   f"(덜 출렁인 쪽이 낮은 해 {risk_lower}/{n}) · 안정 수익 {pct(np.mean([r['low_stable'] for r in rows.values()]))} vs {pct(np.mean([r['high_stable'] for r in rows.values()]))} · "
                                   f"수익 중앙값이 덜 출렁인 쪽이 높은 해 {ret_higher}/{n}",
            "table": {y: {k: (v if k == "n" else pct(v)) for k, v in r.items()} for y, r in rows.items()},
            "why": f"{why} (값 = 덜 출렁인 쪽 − 많이 출렁인 쪽 안정 수익 확률) · 빠진 회사가 없어 많이 출렁인 쪽(무너진 회사가 빠짐)을 좋게 보는 쪽"}


def t045(B, I, P, F):
    """빅테크 7개 몫 — 처음 시가총액 비중(종가 × 그 전 회계연도 희석 주식 수) × 주가 수익. 같은 회사 여러 주식(GOOG·FOX·NWS)은 하나만."""
    dup = {"GOOG", "FOX", "NWS"}
    m7 = ("AAPL", "MSFT", "NVDA", "AMZN", "GOOGL", "META", "TSLA")
    out = {}
    for lab, a, b in (("2023-01~2025-12", date(2023, 1, 1), date(2025, 12, 31)), ("2025", date(2025, 1, 1), date(2025, 12, 31)), ("2024", date(2024, 1, 1), date(2024, 12, 31))):
        s0 = I.next_trading(a.toordinal())
        s1 = int(I.o[int(np.searchsorted(I.o, b.toordinal(), side="right")) - 1])
        caps = {}
        for s, p in P.items():
            if s in dup or not p.has(s0, s1):
                continue
            try:
                if date.fromisoformat(p.added) > a:
                    continue
            except ValueError:
                pass
            sh = S._fy(F, s, "annualDilutedAverageShares")                 # Yahoo 는 분할을 반영한 주식 수 (엔비디아 FY2023 250억 주)
            if not sh:
                continue
            n_ = sh[min(sh, key=lambda k: abs(k.toordinal() - s0))]           # 시작에 가장 가까운 회계연도 (1월에 끝나는 회사 — 엔비디아·월마트 — 도 넣으려고)
            cap = p.at(s0, "close") * n_
            caps[s] = (cap, p.at(s1, "close") / p.at(s0, "close") - 1)
        tot = sum(c for c, _ in caps.values())
        contrib = {s: c / tot * r for s, (c, r) in caps.items()}
        allr = sum(contrib.values())
        m7c = sum(contrib.get(s, 0) for s in m7)
        rest_w = sum(c for s, (c, _) in caps.items() if s not in m7) / tot
        ix = I.at(s1, I.px) / I.at(s0, I.px) - 1
        out[lab] = {"n": len(caps), "calc_index_ret": pct(allr), "real_index_ret": pct(ix), "gap": pp(allr - ix), "m7_share_of_gain": pct(m7c / allr),
                    "m7_weight_start": pct(1 - rest_w), "rest_ret": pct((allr - m7c) / rest_w), "m7_ret": pct(m7c / (1 - rest_w)),
                    "nvda_share": pct(contrib.get("NVDA", 0) / allr), "by": {s: pct(contrib.get(s, 0) / allr) for s in m7}}
    main = out["2023-01~2025-12"]
    ok = abs(float(main["gap"].rstrip("%p"))) <= 5               # v1.0 고침(첫 계산 뒤 3%p → 5%p — 계산 합 82.7% vs 실제 79.0%, 어림이라 숫자는 '약'으로만)
    return {"class": "사실형" if ok else "미확인", "answer": f"2023~2025년: 빅테크 7개 몫 {main['m7_share_of_gain']} (처음 비중 {main['m7_weight_start']}) · 엔비디아 혼자 {main['nvda_share']} · 7개 {main['m7_ret']} vs 나머지 {main['rest_ret']} · 계산 합 {main['calc_index_ret']} vs 실제 지수 {main['real_index_ret']}",
            "table": out, "why": "어림 계산(유동 주식 비중을 안 씀 · 빠진 회사 없음) — 계산 합이 실제 지수 상승과 5%p 안일 때만 사실형(숫자는 '약') · 2022년에 이미 들어와 있던 회사만"}


def t046(B, I, P, F):
    o0 = date(2000, 1, 1).toordinal()
    m = I.o >= o0
    tr, o = I.tr[m], I.o[m]
    d = np.diff(tr) / tr[:-1]
    days = [date.fromordinal(int(x)) for x in o]
    mon = {}
    for x, v in zip(days, tr):
        mon[(x.year, x.month)] = v
    mv = np.array(list(mon.values()))
    mr = mv[1:] / mv[:-1] - 1
    yr = {}
    for x, v in zip(days, tr):
        yr[x.year] = v
    yv = np.array([yr[y] for y in sorted(yr) if y <= 2025])
    y0 = I.at(date(2000, 1, 1).toordinal() - 1)
    yrr = np.concatenate([[yv[0] / y0 - 1], yv[1:] / yv[:-1] - 1])
    w5 = [B.tr[e] / B.tr[s] - 1 for s, e, _ in B.W["5y"]]
    w5l = [B.tr[e] / B.tr[s] - 1 for s, e, _ in B.W["5y"] if B.d[s].year >= 2009]
    late = np.array([x.year >= 2009 for x in days[1:]])
    res = {"day": float(np.mean(d < 0)), "day_2009": float(np.mean(d[late] < 0)), "month": float(np.mean(mr < 0)), "year": float(np.mean(yrr < 0)),
           "y5": float(np.mean(np.array(w5) < 0)), "y5_2009": float(np.mean(np.array(w5l) < 0)), "n_years": len(yrr)}
    return {"class": "사실형", "answer": f"손실인 비율 — 하루 {pct(res['day'])} · 한 달 {pct(res['month'])} · 1년(달력) {pct(res['year'])} ({int(round(res['year'] * res['n_years']))}/{res['n_years']}해) · 5년 {pct(res['y5'])} (2009년 이후 시작 {pct(res['y5_2009'])})",
            "table": {k: (pct(v) if k != "n_years" else v) for k, v in res.items()}, "why": "2000년 이후 사실 · 확인 주기가 길수록 손실을 보는 횟수가 줄어듦"}


def t047(B, I, P, F):
    days = [date.fromordinal(int(x)) for x in I.o]
    mon = {}
    for x, v in zip(days, I.tr):
        mon[(x.year, x.month)] = v
    keys = sorted(mon)
    ret = {}
    for a, b in zip(keys, keys[1:]):
        if 2000 <= b[0] <= 2025:
            ret[b] = mon[b] / mon[a] - 1
    tab = {}
    for mth in range(1, 13):
        v = np.array([r for (y, m_), r in ret.items() if m_ == mth])
        ve = np.array([r for (y, m_), r in ret.items() if m_ == mth and y <= 2008])
        vl = np.array([r for (y, m_), r in ret.items() if m_ == mth and y >= 2009])
        worst = min(((r, y) for (y, m_), r in ret.items() if m_ == mth))
        tab[mth] = {"down_share": float(np.mean(v < 0)), "mean": float(v.mean()), "median": float(np.median(v)), "worst": worst,
                    "down_share_2000_08": float(np.mean(ve < 0)), "down_share_2009": float(np.mean(vl < 0)), "mean_2009": float(vl.mean())}
    by_down = sorted(tab, key=lambda m_: -tab[m_]["down_share"])
    by_mean = sorted(tab, key=lambda m_: tab[m_]["mean"])
    return {"class": "사실형", "answer": f"가장 자주 빠진 달 {by_down[0]}월({pct(tab[by_down[0]]['down_share'])}) · 평균이 가장 나쁜 달 {by_mean[0]}월({pct(tab[by_mean[0]]['mean'])}) · "
                                   f"10월: 빠진 해 {pct(tab[10]['down_share'])} · 평균 {pct(tab[10]['mean'])} · 가장 크게 빠진 10월 {tab[10]['worst'][1]}년 {pct(tab[10]['worst'][0])}",
            "table": {m_: {k: (pct(v) if not isinstance(v, tuple) else f"{v[1]}년 {pct(v[0])}") for k, v in r.items()} for m_, r in tab.items()},
            "order_by_down_share": by_down, "why": "26년 사실 · 달마다 26번뿐이라 '9월에 팔아라' 규칙이 아님 (앞·뒤 시기 따로 적음)"}


def t048(B, I, P, F):
    ev = [("그랜섬 '거품' 경고 보도", "2021-01-22"), ("다이먼 '경제 허리케인'", "2022-06-01"), ("머스크 '경제에 아주 나쁜 예감'", "2022-06-03"),
          ("버리 '팔아라'(연초 — 3월에 '틀렸다')", "2023-01-31"), ("버리 S&P 500·나스닥 하락 베팅 공시", "2023-08-14")]
    rows = S.event_rows(I, ev)
    for r in rows:
        d0 = date.fromisoformat(r["buy_day"]).toordinal()
        m = (I.o >= d0) & (I.o <= d0 + YEAR)
        k = int(np.argmin(np.where(m, I.tr, np.inf)))
        r["worst_within_1y"] = pct(I.tr[k] / I.at(d0) - 1)
        r["worst_day"] = date.fromordinal(int(I.o[k])).isoformat()
    lower = [r["event"] for r in rows if r.get("1y", 1) < 0]
    big = [r["event"] for r in rows if float(r["worst_within_1y"].rstrip("%")) <= -20]
    return {"class": "사실형", "answer": f"1년 뒤 경고한 날보다 낮았던 때 {len(lower)}/{len(rows)} · 그사이 20% 넘게 빠진 때 {len(big)}/{len(rows)} ({', '.join(big) or '없음'})",
            "table": rows, "why": "5번 사실 · 날짜는 보도(대본 전 원문 — 버리 '팔아라' 날짜는 연초로만 확인) · 경고 뒤 실제로 빠진 때도 있어 '경고는 늘 틀린다'가 아님 — 그날 팔았다면 1년 뒤 얼마였나만"}


def t049(B, I, P, F):
    o0 = date(2000, 1, 1).toordinal()
    run_max = np.maximum.accumulate(I.px)
    ath = (I.px >= run_max) & (I.o >= o0) & (I.o + YEAR <= I.last)
    anyd = (I.o >= o0) & (I.o + YEAR <= I.last)
    j = np.searchsorted(I.o, I.o + YEAR, side="right") - 1
    loss = I.tr[j] < I.tr
    yrs = np.array([date.fromordinal(int(x)).year for x in I.o])
    res = {}
    for lab, m in (("전체", np.ones(len(I.o), bool)), ("2000~08", (yrs <= 2008)), ("2009~", yrs >= 2009)):
        res[lab] = {"ath_days": int((ath & m).sum()), "ath_loss": float(np.mean(loss[ath & m])) if (ath & m).sum() else None,
                    "any_loss": float(np.mean(loss[anyd & m])), "ath_ret_median": float(np.median((I.tr[j] / I.tr - 1)[ath & m])) if (ath & m).sum() else None}
    k07 = int(np.flatnonzero((yrs == 2007) & ath)[-1])
    r07 = I.tr[j[k07]] / I.tr[k07] - 1
    diff_late = res["2009~"]["ath_loss"] - res["2009~"]["any_loss"]
    diff_early = (res["2000~08"]["ath_loss"] or 0) - res["2000~08"]["any_loss"]
    cl = "사실형" if (diff_late > 0) == (diff_early > 0) else "조건부형"     # v1.0 고침(첫 계산 뒤 — '비슷해야 사실형'으로 잘못 적었음): 두 시기 같은 방향이면 사실형
    return {"class": cl, "answer": f"1년 뒤 손실 확률 — 최고가 날 vs 아무 날: 2009년 이후 {pct(res['2009~']['ath_loss'])} vs {pct(res['2009~']['any_loss'])} · 2000~08년 {pct(res['2000~08']['ath_loss'])} vs {pct(res['2000~08']['any_loss'])} "
                                   f"(최고가 날 {res['2000~08']['ath_days']}일) · 2007년 마지막 최고가({date.fromordinal(int(I.o[k07]))})에 산 1만 달러 1년 뒤 {round(10000 * (1 + r07)):,}달러",
            "table": {k: {kk: (pct(vv) if isinstance(vv, float) else vv) for kk, vv in v.items()} for k, v in res.items()},
            "why": f"차이(최고가 − 아무 날): 2009~ {pp(diff_late)} · 2000~08 {pp(diff_early)} — 앞 시기 최고가는 2000·2007년 고점이라 날 수가 적고 결과가 몰림"}


def t050(B, I, P, F):
    wins = [("2020-02-19", "2020-03-23"), ("2022-01-03", "2022-10-12"), ("2025-02-19", "2025-04-08")]
    a5, b5 = date(2020, 10, 27).toordinal(), date(2025, 10, 27).toordinal()
    ix5 = I.at(b5) / I.at(a5) - 1
    idx_dd = [I.at(date.fromisoformat(b).toordinal(), I.px) / I.at(date.fromisoformat(a).toordinal(), I.px) - 1 for a, b in wins]
    cnt, all3, both, names = 0, 0, 0, []
    for s, p in P.items():
        if not p.has(date(2019, 12, 31).toordinal(), b5):
            continue
        cnt += 1
        dd = [p.at(date.fromisoformat(b).toordinal()) / p.at(date.fromisoformat(a).toordinal()) - 1 for a, b in wins]
        if all(x > y for x, y in zip(dd, idx_dd)):
            all3 += 1
            r5 = p.at(b5) / p.at(a5) - 1
            if r5 > ix5:
                both += 1
                names.append((s, p.sector, pct(r5, 0)))
    sect = {}
    for _, sc, _ in names:
        sect[sc] = sect.get(sc, 0) + 1
    return {"class": "사실형", "answer": f"{cnt}종목 중 세 하락장 모두 지수보다 덜 빠진 종목 {all3}개({pct(all3 / cnt)}) · 그중 5년 수익도 지수({pct(ix5)})보다 높은 종목 {both}개({pct(both / cnt)})",
            "index_drops": [pct(x) for x in idx_dd], "sectors": dict(sorted(sect.items(), key=lambda x: -x[1])), "names": names[:40],
            "why": "지금 남은 회사만이라 비율을 크게 보는 쪽 — '드물다'는 결론은 더 단단 · 같은 기간(지수 고점~바닥)으로 잼"}


def t051(B, I, P, F):
    tab = {"1년": 0.652, "5년": 0.763, "10년": 0.843, "20년": 0.920}
    return {"class": "사실형", "answer": "미국 대형주 펀드 중 S&P 500보다 못한 비율 (SPIVA 2024년 말): " + " · ".join(f"{k} {pct(v)}" for k, v in tab.items()),
            "table": {k: pct(v) for k, v in tab.items()}, "why": "보고서 숫자(2차 정리로 확인 — 1년 65.2% 는 여러 곳 · 5·10·20년은 대본 전 S&P DJI 원문 PDF) · 15년 숫자는 확인 못 해 쓰지 않음"}


def t052(B, I, P, F):
    """배당락 날 (전날 종가 × (1 + 그날 지수 움직임) − 그날 종가) ÷ 배당금 — 특별배당(앞 4번 중앙값의 2배 넘음)은 뺌."""
    by = {}
    for s, p in P.items():
        k = np.flatnonzero(p.div > 0)
        for n_, j in enumerate(k):
            d0 = int(p.o[j])
            y = date.fromordinal(d0).year
            if not (2015 <= y <= 2025) or j == 0:
                continue
            prev = p.div[k[max(0, n_ - 4):n_]]
            if len(prev) >= 2 and p.div[j] > 2 * np.median(prev):
                continue
            c_1, c0, dv = p.close[j - 1], p.close[j], p.div[j]
            if dv / c_1 < 0.001:
                continue
            m = I.at(d0, I.px) / I.at(int(p.o[j - 1]), I.px) - 1
            drop = c_1 * (1 + m) - c0
            by.setdefault(y, []).append((drop, dv, dv / c_1))
    tab, cm = {}, {}
    for y, v in sorted(by.items()):
        a = np.array(v)
        ratio = a[:, 0].sum() / a[:, 1].sum()
        tab[str(y)] = {"n": len(v), "drop_over_div": pct(ratio), "median_yield_per_payment": pct(float(np.median(a[:, 2])), 2)}
        cm[str(y)] = ratio
    allv = np.array([x for v in by.values() for x in v])
    tot = allv[:, 0].sum() / allv[:, 1].sum()
    lo, hi = min(cm.values()), max(cm.values())
    cl = "정답형" if lo >= 0.85 else "사실형"          # v1.0 고침(첫 계산 뒤): 해마다 65~116% 로 흔들림(하루 주가 움직임이 배당보다 큼) → 결론은 11년 '평균'으로만(사실형)
    return {"class": cl, "answer": f"배당락 날 주가는 배당금의 평균 {pct(tot)}만큼 빠짐 (해마다 {pct(lo)}~{pct(hi)} · {len(allv):,}번) — 세금 15%를 떼면 받는 배당은 85% → 전날 사서 받고 판 사람은 평균 {pp(0.85 - tot)} (배당금 대비)",
            "table": tab, "why": "해마다 85% 넘게 빠지면 '세금 떼면 손해'가 정답형 · 같은 날 지수 움직임은 뺌(종목마다 1배로 둠) · 하루 주가 흔들림이 배당보다 커서 한 번 한 번은 들쭉날쭉 — 합으로 봄"}


def t053(B, I, P, F):
    days = [date.fromordinal(int(x)) for x in I.o]
    yrs = np.array([x.year for x in days])
    tab = {}
    for Y in range(2000, 2026):
        m = yrs == Y
        v = I.px[m]
        prev = I.px[np.flatnonzero(yrs == Y - 1)[-1]]
        seg = np.concatenate([[prev], v])
        dd = float((seg / np.maximum.accumulate(seg) - 1).min())
        tab[Y] = {"ret": float(v[-1] / prev - 1), "intra_dd": dd}
    up = [Y for Y, r in tab.items() if r["ret"] > 0]
    up10 = [Y for Y in up if tab[Y]["intra_dd"] <= -0.10]
    return {"class": "사실형", "answer": f"2000~2025년 오른 해 {len(up)}번 중 그해 중간에 10% 넘게 빠진 해 {len(up10)}번 ({', '.join(map(str, up10))}) · 오른 해의 중간 하락폭 평균 {pct(np.mean([tab[Y]['intra_dd'] for Y in up]))} · "
                                   f"2025년 중간 {pct(tab[2025]['intra_dd'])} → 한 해 {pct(tab[2025]['ret'])}",
            "table": {Y: {"ret": pct(r["ret"]), "intra_dd": pct(r["intra_dd"])} for Y, r in tab.items()}, "why": "26년 사실 (가격 지수 · 그해 안 고점 대비)"}


def t054(B, I, P, F):
    yr = {}
    for x, v in zip((date.fromordinal(int(o)) for o in I.o), I.tr):
        yr[x.year] = v
    rets = {Y: yr[Y] / yr[Y - 1] - 1 for Y in range(2000, 2026)}
    bins = [(-9, -0.10, "−10% 아래"), (-0.10, 0, "−10~0%"), (0, 0.07, "0~7%"), (0.07, 0.13, "7~13%"), (0.13, 0.20, "13~20%"), (0.20, 9, "20% 넘음")]
    cnt = {lab: [Y for Y, r in rets.items() if a <= r < b] for a, b, lab in bins}
    mean = float(np.mean(list(rets.values())))
    cagr = (yr[2025] / yr[1999]) ** (1 / 26) - 1
    return {"class": "사실형", "answer": f"26년 중 7~13% 오른 해 {len(cnt['7~13%'])}번 ({', '.join(map(str, cnt['7~13%']))}) · 20% 넘음 {len(cnt['20% 넘음'])}번 · 손실 {len(cnt['−10~0%']) + len(cnt['−10% 아래'])}번 · "
                                   f"평균 {pct(mean)} · 해마다 복리로 {pct(cagr)}",
            "table": {lab: v for lab, v in cnt.items()}, "years": {Y: pct(r) for Y, r in rets.items()}, "why": "26년 사실 (배당 포함)"}


def t055(B, I, P, F):
    tab = {}
    for Y in range(2010, 2026):
        a, b = date(Y, 1, 1).toordinal(), date(Y, 12, 31).toordinal()
        ix = I.at(b, I.px) / I.at(a - 1, I.px) - 1
        dds, calm = [], 0
        for s, p in P.items():
            if not p.has(a - 7, b):
                continue
            k0 = int(np.searchsorted(p.o, a - 1, side="right")) - 1
            k1 = int(np.searchsorted(p.o, b, side="right")) - 1
            v = p.adj[k0:k1 + 1]
            dd = float((v / np.maximum.accumulate(v) - 1).min())
            dds.append(dd)
        dds = np.array(dds)
        tab[Y] = {"index_ret": ix, "n": len(dds), "dd20": float(np.mean(dds <= -0.20)), "calm10": float(np.mean(dds > -0.10))}
    up = [Y for Y, r in tab.items() if r["index_ret"] > 0]
    avg20 = float(np.mean([tab[Y]["dd20"] for Y in up]))
    return {"class": "사실형", "answer": f"지수가 오른 해({len(up)}번) 평균 — 그해 중간에 20% 넘게 빠진 적 있는 종목 {pct(avg20)} · 10%도 안 빠진 종목 {pct(np.mean([tab[Y]['calm10'] for Y in up]))} · 2023년 {pct(tab[2023]['dd20'])}",
            "table": {Y: {k: (v if k == "n" else pct(v)) for k, v in r.items()} for Y, r in tab.items()},
            "why": "사실 · 빠진 회사가 없어 흔들림을 작게 보는 쪽(결론 쪽으로 단단) · 그해 안 고점 대비"}


def _regular_payments(p):
    """정기 배당만 — 특별배당(앞 4번 중앙값의 1.5배 넘음) 뺌 · 실적 따라 바뀌는 분배금(최근 8번 변동계수 0.35 넘음)은 None."""
    k = np.flatnonzero(p.div > 0)
    o, v = p.o[k], p.div[k]
    keep = np.ones(len(v), bool)
    for i in range(len(v)):
        prev = v[max(0, i - 4):i]
        if len(prev) >= 2 and v[i] > 1.5 * np.median(prev):
            keep[i] = False
    return o[keep], v[keep]


def t022(B, I, P, F):
    """연말 정기 배당률 상위 10% vs 나머지 배당 주는 회사 — 다음 1년 30% 넘게 빠진 적 · 안정 수익 · 3년 안 삭감."""
    rows = {}
    for Y in range(2014, 2025):
        c0 = int(I.o[int(np.searchsorted(I.o, date(Y, 12, 31).toordinal(), side="right")) - 1])
        c1 = c0 + YEAR
        if c1 > I.last:
            continue
        cash = I.at(c1, I.cash) / I.at(c0, I.cash)
        vals = []
        for s, p in P.items():
            if not p.has(c0 - 3 * YEAR, c1):
                continue
            o, v = _regular_payments(p)
            last8 = v[(o <= c0)][-8:]
            if len(last8) < 4 or np.std(last8) / np.mean(last8) > 0.35:
                continue
            ttm = v[(o > c0 - YEAR) & (o <= c0)].sum()
            if ttm <= 0:
                continue
            yld = ttm / p.at(c0, "close")
            k0 = int(np.searchsorted(p.o, c0, side="right")) - 1
            k1 = int(np.searchsorted(p.o, c1, side="right")) - 1
            path = p.adj[k0:k1 + 1] / p.adj[k0]
            cut = None
            for i in np.flatnonzero((o > c0) & (o <= c0 + 3 * YEAR)):
                prev = v[max(0, i - 4):i]
                if len(prev) >= 2 and v[i] < 0.75 * float(np.median(prev)):
                    cut = True
                    break
            gaps = np.diff(np.concatenate([o[(o > c0 - YEAR) & (o <= c0)][-1:], o[(o > c0) & (o <= c0 + 3 * YEAR)], [min(c0 + 3 * YEAR, I.last)]]))
            usual = float(np.median(np.diff(o[o <= c0][-8:]))) if (o <= c0).sum() >= 3 else 91.0
            if cut is None and len(gaps) and gaps.max() > max(200, 1.6 * usual):      # 끊김 (1년에 한 번 주는 회사는 365일이 보통)
                cut = True
            vals.append((yld, s, bool(path.min() <= 0.70), bool(path[-1] > cash and path.min() >= 0.80), bool(cut), float(path[-1] - 1)))
        vals.sort(reverse=True)
        q = max(len(vals) // 10, 1)
        top, rest = vals[:q], vals[q:]
        rows[str(Y)] = {"n": len(vals), "top_min_yield": pct(top[-1][0]), "top_big_loss": float(np.mean([v[2] for v in top])), "rest_big_loss": float(np.mean([v[2] for v in rest])),
                        "top_stable": float(np.mean([v[3] for v in top])), "rest_stable": float(np.mean([v[3] for v in rest])),
                        "top_cut3": float(np.mean([v[4] for v in top])) if c0 + 3 * YEAR <= I.last else None,
                        "rest_cut3": float(np.mean([v[4] for v in rest])) if c0 + 3 * YEAR <= I.last else None,
                        "top3": [(v[1], pct(v[0])) for v in top[:3]]}
    cm = {y: r["rest_stable"] - r["top_stable"] for y, r in rows.items()}
    cl0, why = classify_diff(cm)
    riskier = sum(1 for r in rows.values() if r["top_big_loss"] >= r["rest_big_loss"])
    cutmore = [r for r in rows.values() if r["top_cut3"] is not None]
    cm_cut = sum(1 for r in cutmore if r["top_cut3"] > r["rest_cut3"])
    n = len(rows)
    # 편향: 지금 남은 회사만 → 배당률 높은 쪽 위험을 작게 봄. 높은 쪽이 위험하다는 결론이면 단단 · 덜 위험하다는 결론이면 믿을 수 없음
    # v1.0 고침(첫 계산 뒤): 안정 수익 확률은 해마다 갈리고 상위 쪽이 조금 높아 편향 쪽(미확인). 대신 결론을 편향과 반대쪽 두 가지로만 —
    #   ① 30% 넘게 빠진 확률이 상위 쪽이 낮지 않음(같거나 높은 해가 절반 넘음) ② 3년 안 배당 삭감이 상위 쪽이 많음(3분의 2 넘는 해) → 둘 다면 사실형
    if riskier > n / 2 and cm_cut >= 2 * len(cutmore) / 3:
        cl = "사실형"
    else:
        cl = "미확인"
    return {"class": cl, "computed_class": cl0, "answer": f"배당률 상위 10% vs 나머지 ({n}해): 1년 안 30% 넘게 빠진 확률 {pct(np.mean([r['top_big_loss'] for r in rows.values()]))} vs {pct(np.mean([r['rest_big_loss'] for r in rows.values()]))} "
                                                          f"(상위가 같거나 높은 해 {riskier}/{n}) · 안정 수익 {pct(np.mean([r['top_stable'] for r in rows.values()]))} vs {pct(np.mean([r['rest_stable'] for r in rows.values()]))} · "
                                                          f"3년 안 삭감 {pct(np.mean([r['top_cut3'] for r in cutmore]))} vs {pct(np.mean([r['rest_cut3'] for r in cutmore]))} (상위가 많은 해 {cm_cut}/{len(cutmore)})",
            "table": {y: {k: (pct(v) if isinstance(v, float) else v) for k, v in r.items()} for y, r in rows.items()},
            "why": f"{why} (값 = 나머지 − 상위 안정 수익 확률) · 지금 남은 회사만이라 상위 쪽 위험을 작게 보는 쪽 — 상위가 더 위험하면 결론 단단, 덜 위험하면 미확인 · 특별배당·변동 분배금 뺌"}


TOPICS3 = {"T022": t022, "T043": t043, "T044": t044, "T045": t045, "T046": t046, "T047": t047, "T048": t048, "T049": t049, "T050": t050,
           "T051": t051, "T052": t052, "T053": t053, "T054": t054, "T055": t055}
