#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-11-13 — 주제 기획안 묶음 2026-11-13(B21~) 숫자 — 사용자 지시 "아니 테스트 붙이지 말라고 그것도 예전 룰이잖아 예전거 적용하지 마
#          다 삭제해 너가 새로 만들라니까 다시해" (stock/guides/board_1_topic.md v1.4 3번: 숫자는 이 묶음 계산 파일 출력만).
#
# 주제마다 한 칸 (모두 실제 종가 — S&P 500 배당 포함 ^SP500TR · 가격 ^GSPC · 예금 = 미국 13주 국채 이자 ^IRX 누적(longform_items CASH) · ETF 수정 종가):
#   holding   보유 기간별 손실로 끝난 몫 (1990~ 시작일 5거래일마다 · 1·3·5·10·15·20년)
#   best_days 2006~2025 20년, 가장 많이 오른 날 10·20일을 놓쳤다면 (그날만 현금 — 수익 0)
#   dca_vs_deposit 매달 같은 돈: S&P 500 적립 vs 예금 적립, 10년 (1990-01 ~ 2015-10 시작 달마다) + 최근 10년 예(월 100만 원)
#   dividend  SCHD·DVY vs SPY — 2008·2020·2022 하락장 낙폭 · 전체 기간 배당 포함 수익
#   coveredcall JEPI vs SPY · QYLD vs QQQ — 2022 낙폭 · 그 뒤 회복 · 전체
#   leverage  TQQQ·QLD — 2021-11 고점 뒤 가장 깊은 낙폭 · 고점 회복일 · QQQ 가 1년 동안 ±5% 안(제자리)일 때 TQQQ 손실 몫
#   lump_vs_dca 목돈 한 번에 vs 12달 나눠(안 넣은 돈은 예금) 4년 — 더 남은 몫 · 원금 20% 넘게 줄어든 적 몫
#   peaks     S&P 500(가격·배당 포함)·QQQ 최고점에 산 뒤 그 값을 되찾은 날 (2000·2007·2022)
#   swing     '5% 오르면 팔고 3% 빠지면 다시' vs 그냥 보유 vs 처음부터 80% 보유 + 20% 예금 (SPY 4년)
# 시작일이 겹치는 구간이라 몫으로만 본다. 금액은 달러 기준 변화율(환율·세금·수수료 뺌). ※ 연구·교육용 — 투자 권유가 아님.
#
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.0 | 2026-11-13 | 최초 | main 과 칸마다 함수 |
import bisect
import json
import logging
import sys
from datetime import date
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import longform_items as L  # noqa: E402
import precheck as P  # noqa: E402

VERSION = "v1.0"
END = "2025-12-31"
LOG = logging.getLogger("plans_2026-11-13")
LOG.propagate = False
_h = logging.StreamHandler(sys.stdout)
_h.setFormatter(logging.Formatter("%(message)s"))
LOG.addHandler(_h)
LOG.setLevel(logging.INFO)


def log(tag, /, **kv):
    LOG.info(f"[{tag}] [{date.today()}] " + " ".join(f"{k}={v}" for k, v in kv.items()))


def add_y(d, y):
    return f"{int(d[:4]) + y}{d[4:]}"


def add_m(d, m):
    y, mo = int(d[:4]), int(d[5:7]) - 1 + m
    return f"{y + mo // 12}-{mo % 12 + 1:02d}{d[7:]}"


def seg(s, a, b):
    i, j = bisect.bisect_left(s.k, a), bisect.bisect_right(s.k, b) - 1
    v = np.asarray(s.v[i:j + 1], float)
    return v / v[0]


def r4(x):
    return None if x is None else round(float(x), 4)


def holding(TR, SPX):
    out = {}
    for y in (1, 3, 5, 10, 15, 20):
        for name, s in (("tr", TR), ("price", SPX)):
            ds = [d for n, d in enumerate(s.k) if n % 5 == 0 and d >= "1990-01-01" and add_y(d, y) <= END]
            r = np.array([s.chg(d, add_y(d, y)) for d in ds])
            out[f"{y}y_{name}"] = {"n": len(r), "loss_share": r4((r < 0).mean()), "worst": r4(r.min()), "median": r4(np.median(r))}
            log("HOLD", years=y, kind=name, **out[f"{y}y_{name}"])
    return out


def best_days(TR):
    i, j = bisect.bisect_left(TR.k, "2006-01-01"), bisect.bisect_right(TR.k, END) - 1
    v = np.asarray(TR.v[i:j + 1], float)
    r = v[1:] / v[:-1] - 1
    days = TR.k[i + 1:j + 1]
    order = np.argsort(r)[::-1]
    full = float(np.prod(1 + r) - 1)
    out = {"from": TR.k[i], "to": TR.k[j], "trading_days": len(r), "full": r4(full)}
    for n in (10, 20):
        rr = r.copy()
        rr[order[:n]] = 0.0
        out[f"miss_best_{n}"] = r4(np.prod(1 + rr) - 1)
    worst = set(np.argsort(r)[:20].tolist())
    near = sum(1 for k in order[:10] if any(abs(int(k) - w) <= 10 for w in worst))
    out["best10"] = [[days[k], r4(r[k])] for k in order[:10]]
    out["best10_within_10days_of_worst20"] = near
    log("BEST", **{k: v for k, v in out.items() if k != "best10"})
    return out


def dca_vs_deposit(TR, C, monthly=100):
    def run(start, months=120):
        units = dep = 0.0
        d = start
        for m in range(months):
            day = add_m(start, m)
            units += monthly / TR.at(day)
            dep = dep * (1 + C.chg(add_m(start, m - 1), day)) + monthly if m else monthly
            d = day
        e = add_m(start, months)
        dep *= 1 + C.chg(d, e)
        return units * TR.at(e), dep
    starts = [f"{y}-{m:02d}-01" for y in range(1990, 2016) for m in range(1, 13) if f"{y}-{m:02d}-01" <= "2015-10-01"]
    res = [run(s) for s in starts]
    ratio = np.array([a / b for a, b in res])
    ex_tr, ex_dep = run("2015-11-01")
    out = {"windows": len(starts), "years": 10, "dca_beats_deposit": r4((ratio > 1).mean()), "worst_ratio": r4(ratio.min()),
           "worst_start": starts[int(np.argmin(ratio))], "median_ratio": r4(np.median(ratio)),
           "example": {"start": "2015-11-01", "end": "2025-11-01", "monthly_man": monthly, "put_in_man": monthly * 120,
                       "dca_man": round(ex_tr), "deposit_man": round(ex_dep)}}
    log("DCA", **{k: v for k, v in out.items() if k != "example"}, example=out["example"])
    return out


def dd(s, a, b):
    """a~b 사이 그 전 최고점 대비 가장 깊은 낙폭."""
    v = seg(s, a, b)
    return r4((v / np.maximum.accumulate(v) - 1).min())


def dividend(X):
    rng = {"2008": ("2007-10-09", "2009-03-09"), "2020": ("2020-02-19", "2020-03-23"), "2022": ("2022-01-03", "2022-10-12")}
    out = {}
    for sym in ("SCHD", "DVY", "SPY"):
        s = X[sym]
        row = {"first": s.k[0]}
        for k, (a, b) in rng.items():
            if s.k[0] <= a:
                row[f"chg_{k}"] = r4(s.chg(a, b))
        row["total_2012_2025"] = r4(s.chg("2012-01-03", END)) if s.k[0] <= "2012-01-03" else None
        row["total_2022_2025"] = r4(s.chg("2022-01-03", END))
        out[sym] = row
        log("DIV", sym=sym, **row)
    return out


def coveredcall(X):
    out = {}
    for sym, base in (("JEPI", "SPY"), ("QYLD", "QQQ")):
        s, b = X[sym], X[base]
        first = max(s.k[0], "2014-01-02") if sym == "QYLD" else s.k[0]
        row = {"vs": base, "first": first,
               "chg_2022": r4(s.chg("2022-01-03", "2022-10-12")), "base_chg_2022": r4(b.chg("2022-01-03", "2022-10-12")),
               "after_2022": r4(s.chg("2022-10-12", END)), "base_after_2022": r4(b.chg("2022-10-12", END)),
               "total": r4(s.chg(first, END)), "base_total": r4(b.chg(first, END)),
               "dd_whole": dd(s, first, END), "base_dd_whole": dd(b, first, END)}
        out[sym] = row
        log("CC", sym=sym, **row)
    return out


def leverage(X):
    out = {}
    for sym in ("TQQQ", "QLD", "QQQ"):
        s = X[sym]
        pk = "2021-11-19"
        low, lowday = s.low(pk, "2022-12-31")
        back = s.back(pk, s.at(pk), after=lowday)
        out[sym] = {"peak": pk, "deepest": r4(low), "deepest_day": lowday, "back_to_peak": back, "years_to_back": L.yrs(pk, back) if back else None}
        log("LEV", sym=sym, **out[sym])
    q, t = X["QQQ"], X["TQQQ"]
    r = [t.chg(d, add_y(d, 1)) for n, d in enumerate(t.k) if n % 5 == 0 and add_y(d, 1) <= END and abs(q.chg(d, add_y(d, 1))) <= 0.05]
    r = np.array(r)
    out["flat_1y"] = {"band": 0.05, "n": len(r), "tqqq_loss_share": r4((r < 0).mean()), "tqqq_median": r4(np.median(r)), "from": t.k[0]}
    log("LEV", **out["flat_1y"])
    return out


def lump_vs_dca(TR, C, years=4):
    def dca(d):
        k = TR.k
        i0, j = bisect.bisect_left(k, d), bisect.bisect_right(k, add_y(d, years)) - 1
        buys = [add_m(d, m) for m in range(12)]
        units, cash, bi, vals = 0.0, 1.0, 0, []
        for t in range(i0, j + 1):
            if t > i0:
                cash *= 1 + C.chg(k[t - 1], k[t])
            while bi < 12 and buys[bi] <= k[t]:
                amt = cash / (12 - bi)
                units += amt / TR.v[t]
                cash -= amt
                bi += 1
            vals.append(units * TR.v[t] + cash)
        return np.array(vals)
    out = {}
    for a, b in (("1990-01-01", "2008-12-31"), ("2009-01-01", END)):
        ds = [d for n, d in enumerate(TR.k) if n % 20 == 0 and a <= d <= b and add_y(d, years) <= END]
        lumps = [seg(TR, d, add_y(d, years)) for d in ds]
        dcas = [dca(d) for d in ds]
        row = {"from": ds[0], "n": len(ds), "lump_ends_higher": r4(np.mean([l[-1] > c[-1] for l, c in zip(lumps, dcas)])),
               "lump_dd20": r4(np.mean([l.min() < 0.8 for l in lumps])), "dca_dd20": r4(np.mean([c.min() < 0.8 for c in dcas])),
               "lump_worst": r4(min(l.min() for l in lumps) - 1), "dca_worst": r4(min(c.min() for c in dcas) - 1)}
        out[a[:4]] = row
        log("LUMP", **row)
    return out


def peaks(SPX, TR, X):
    out = {}
    for name, s, pk in (("spx_2000", SPX, "2000-03-24"), ("tr_2000", TR, "2000-03-24"), ("spx_2007", SPX, "2007-10-09"), ("tr_2007", TR, "2007-10-09"),
                        ("spx_2022", SPX, "2022-01-03"), ("tr_2022", TR, "2022-01-03"), ("qqq_2000", X["QQQ"], "2000-03-27")):
        low, lowday = s.low(pk, add_y(pk, 3))
        back = s.back(pk, s.at(pk), after=lowday)
        out[name] = {"peak": pk, "deepest": r4(low), "deepest_day": lowday, "back": back, "years": L.yrs(pk, back) if back else None}
        log("PEAK", name=name, **out[name])
    return out


def swing(SPY, C, years=4, up=0.05, down=0.03):
    def sw(d):
        k = SPY.k
        i0, j = bisect.bisect_left(k, d), bisect.bisect_right(k, add_y(d, years)) - 1
        hold, units, cash, ref, n = True, 1.0 / SPY.v[i0], 0.0, SPY.v[i0], 0
        vals = []
        for t in range(i0, j + 1):
            p = SPY.v[t]
            if t > i0 and not hold:
                cash *= 1 + C.chg(k[t - 1], k[t])
            if hold and p >= ref * (1 + up):
                cash, units, hold, ref, n = units * p, 0.0, False, p, n + 1
            elif not hold and p <= ref * (1 - down):
                units, cash, hold, ref, n = cash / p, 0.0, True, p, n + 1
            vals.append(units * p + cash)
        return np.array(vals), n
    out = {}
    for a, b in (("1999-01-01", "2008-12-31"), ("2009-01-01", END)):
        ds = [d for n_, d in enumerate(SPY.k) if n_ % 20 == 0 and a <= d <= b and add_y(d, years) <= END]
        rows = []
        for d in ds:
            h = seg(SPY, d, add_y(d, years))
            c = np.array([1 + C.chg(d, x) for x in SPY.k[bisect.bisect_left(SPY.k, d):bisect.bisect_right(SPY.k, add_y(d, years))]])
            mix = 0.8 * h + 0.2 * c
            s_, n = sw(d)
            dep = c[-1]
            st = lambda v: bool(v[-1] > dep and v.min() >= 0.8)  # noqa: E731
            rows.append((st(h), st(s_), st(mix), s_[-1] > h[-1], s_[-1] > mix[-1], n))
        r = np.array(rows, float)
        out[a[:4]] = {"from": ds[0], "n": len(ds), "hold_stable": r4(r[:, 0].mean()), "swing_stable": r4(r[:, 1].mean()), "mix80_stable": r4(r[:, 2].mean()),
                      "swing_beats_hold": r4(r[:, 3].mean()), "swing_beats_mix80": r4(r[:, 4].mean()), "trades_median": int(np.median(r[:, 5]))}
        log("SWING", **out[a[:4]])
    return out


def main():
    S = L.load()
    SPX, TR, C = S["SPX"], S["TR"], S["CASH"]
    X = {}
    for sym in ("SPY", "QQQ", "QLD", "SCHD", "DVY", "JEPI", "QYLD", "TQQQ"):
        d = P.fetch(sym)
        if d is None:
            LOG.error(f"[LOAD] symbol={sym} 받기 실패 — next_step=네트워크 확인 뒤 다시")
            sys.exit(1)
        X[sym] = L.Ser(sym, L.rd(HERE / "data" / f"{sym}.csv", "adjclose"))   # fetch 는 data/<기호>.csv 를 만들거나 읽기만
        log("LOAD", sym=sym, first=X[sym].k[0], last=X[sym].k[-1], rows=len(X[sym].k))
    out = {"tool": f"plans_2026-11-13.py {VERSION}", "made": str(date.today()), "end": END,
           "holding": holding(TR, SPX), "best_days": best_days(TR), "dca_vs_deposit": dca_vs_deposit(TR, C),
           "dividend": dividend(X), "coveredcall": coveredcall(X), "leverage": leverage(X), "lump_vs_dca": lump_vs_dca(TR, C),
           "peaks": peaks(SPX, TR, X), "swing": swing(X["SPY"], C)}
    f = HERE / f"plans_2026-11-13_{date.today()}.json"
    f.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", "utf-8")
    log("DONE", out=f.name)


if __name__ == "__main__":
    main()
