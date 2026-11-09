#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-11-09 — S&P 500 의 가장 흔한 폭락 폭 + 그 폭으로 '첫 폭락 → 첫 반등'부터 거래했을 때 늘 수익인 방법이 있나 (사용자 지시 2026-11-09
#          "주식시장에서 가장 빈번하게 일어나는 에센피500 폭락은 주로 고점에서 몇 퍼센트 하락이야? 그 하락 폭을 기준으로 첫 폭락 해서 투자금 100% 물려있는데
#          첫 반등왔을 때 이후로 거래한다고 했을 때 항상 수익을 얻는 거래 방법은 뭔지 테스트해봐").
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.0 | 2026-11-09 | 최초 (같은 날 고침: 다음 사건 조건 '되찾음 그리고 1년' → '되찾음 또는 1년' — 머리 설명대로) | declines · ath_episodes · events · strat · main |
#
# 자료: SPY 수정 종가(배당 포함, 2000-01-03 ~) · 현금 = ^IRX 13주 국채 (calc.py 와 같은 파일).
# 1) 빈도: ① 하락 한 번 한 번 — 고점에서 내려가다 바닥에서 5% 넘게 반등하면 그 하락이 끝난 것으로 셈 (지그재그 5%) ② 최고가 기준 — 사상 최고가에서 다시 최고가를 되찾을 때까지 가장 깊은 하락.
# 2) 거래 시험 (판단 = 그날 종가 · 매매 = 다음 거래일 종가 · 계좌 처음 = 1 = 고점에 100% 산 원금):
#    사건 = 종가가 252거래일 최고가(산 값)보다 X 넘게 하락(첫 폭락) → 그 뒤 '지금까지의 최저 종가'보다 r 넘게 오른 첫날 R(첫 반등).
#           한 사이클에 한 번 — 다음 사건은 산 값을 되찾은 뒤, 또는 R 에서 252거래일이 지난 뒤.
#    방법 (R 다음 날부터): hold 보유 · trend{n} 종가가 n일 이동평균 아래면 다음 날 현금, 위면 다음 날 주식 · half_ladder{s} R 에 절반 매도 → 판 값보다 s·2s·3s 떨어질 때마다
#           판 뒤 현금의 1/3 → 산 값(고점)을 되찾으면 나머지 · all_ladder{s} 같은 사다리를 모두 매도로 · half_peak R 에 절반 매도 → 산 값을 되찾으면 다시 매수
#    판정: 1·2·3·5년 뒤 계좌 > 1 (원금보다 위) = 수익 · '늘 수익' = 모든 사건에서 수익 · 민감도: X 7.5·10·15% × r 3·5·7% · 시기 2000~2012 / 2013~.
# 한계: 2000년 이후 미국 대형주 지수 하나 · 사건 수가 적음(20번 안팎) · 과거에 늘 수익이었어도 앞으로 늘 그렇다는 보장 없음.
# 출력: sp_crash_trade_<날짜>.json · sp_crash_trade.md. ※ 연구·교육용 — 투자 권유 아님. 세금·수수료 없음.
from __future__ import annotations

import itertools
import json
import logging
import sys
import time
from datetime import date, datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

VERSION = "v1.0"
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SPY_CSV = HERE / "data/SPY.csv"
IRX_CSV = ROOT / "stock/source/timing-test-2026-10/calc/irx_daily.csv"
H = {"1y": 252, "2y": 504, "3y": 756, "5y": 1260}
X_MAIN, R_MAIN = 0.10, 0.05

logging.basicConfig(level=logging.INFO, format="%(message)s", stream=sys.stdout)
def log(stage: str, **kv) -> None:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    logging.info(f"[{stage}] [{ts}] " + " ".join(f"{k}={v}" for k, v in kv.items()))


def load() -> tuple[pd.Series, pd.Series]:
    try:
        s = pd.read_csv(SPY_CSV, comment="#", parse_dates=["date"]).set_index("date")["adjclose"].astype(float)
        irx = pd.read_csv(IRX_CSV, comment="#", parse_dates=["date"]).set_index("date")["close"].astype(float)
    except Exception as e:  # noqa: BLE001
        log("FAIL", stage="data", err=repr(e), next="precheck.py fetch SPY · timing-test calc.py --fetch"); raise
    s = s["2000-01-01":]
    log("DATA", source="SPY", rows=len(s), first=s.index[0].date(), last=s.index[-1].date(), dup=int(s.index.duplicated().sum()), bad=int((s <= 0).sum() + s.isna().sum()))
    irx = irx.reindex(s.index).ffill().fillna(0.0)
    return s, irx


def declines(s: pd.Series, rev: float = 0.05) -> list[dict]:
    v, I = s.values, s.index; out = []; up = True; pk = tr = 0
    for i in range(1, len(v)):
        if up:
            if v[i] > v[pk]: pk = i
            elif v[i] <= v[pk] * (1 - rev): up = False; tr = i
        else:
            if v[i] < v[tr]: tr = i
            elif v[i] >= v[tr] * (1 + rev):
                out.append({"peak": I[pk].strftime("%Y-%m-%d"), "trough": I[tr].strftime("%Y-%m-%d"), "depth": round((v[tr] / v[pk] - 1) * 100, 1)}); up = True; pk = i
    return out


def ath_episodes(s: pd.Series, th: float = -0.05) -> list[dict]:
    v, I = s.values, s.index; out = []; pk = 0; tr = None
    for i in range(1, len(v)):
        if v[i] >= v[pk]:
            if tr is not None and v[tr] / v[pk] - 1 <= th:
                out.append({"peak": I[pk].strftime("%Y-%m-%d"), "trough": I[tr].strftime("%Y-%m-%d"), "depth": round((v[tr] / v[pk] - 1) * 100, 1), "regained": I[i].strftime("%Y-%m-%d")})
            pk, tr = i, None
        elif tr is None or v[i] < v[tr]:
            tr = i
    return out


def buckets(depths: list[float]) -> dict:
    B = [("5~10%", -5, -10), ("10~15%", -10, -15), ("15~20%", -15, -20), ("20~30%", -20, -30), ("30~40%", -30, -40), ("40% 넘게", -40, -100)]
    return {k: sum(1 for d in depths if b < d <= a) for k, a, b in B}


def events(s: pd.Series, X: float, r: float) -> list[dict]:
    v, I = s.values, s.index; out = []; i = 252; last_R = -10 ** 9; need_regain = None
    while i < len(v) - 1:
        if need_regain is not None and v[i] >= need_regain:
            need_regain = None
        hi = int(np.argmax(v[i - 251:i + 1])) + i - 251; B = v[hi]
        if v[i] <= B * (1 - X) and (need_regain is None or i - last_R > 252):      # 한 사이클에 한 번 — 산 값을 되찾았거나 R 에서 1년 지남
            low = v[i]; j = i
            while j < len(v) - 1:
                j += 1; low = min(low, v[j])
                if v[j] >= low * (1 + r):
                    break
            if j >= len(v) - 2:
                break
            out.append({"peak_date": I[hi].strftime("%Y-%m-%d"), "B": float(B), "crash": I[i].strftime("%Y-%m-%d"), "R": j, "R_date": I[j].strftime("%Y-%m-%d"),
                        "value_R": round(v[j] / B, 3), "low_to_R": round((low / B - 1) * 100, 1)})
            last_R, need_regain, i = j, B, j + 1; continue
        i += 1
    return out


def ma(s: pd.Series, n: int) -> np.ndarray:
    return s.rolling(n).mean().values


def strat(s: pd.Series, irx: pd.Series, ev: dict, kind: str, p=None, horizon: int = 756) -> np.ndarray | None:
    v = s.values; cr = irx.values / 100 / 252; R = ev["R"]; B = ev["B"]; end = R + 1 + horizon
    if end >= len(v):
        return None
    units, cash = 1.0 / B, 0.0                           # 고점에 100% (원금 1)
    out = []; pend = None
    if kind == "hold":
        return v[R + 1:end + 1] / B
    if kind.startswith("trend"):
        m = MA[p]; inv = True
        for t in range(R + 1, end + 1):
            cash *= 1 + cr[t]
            if pend == "sell" and units > 0: cash += units * v[t]; units = 0.0
            if pend == "buy" and cash > 0: units += cash / v[t]; cash = 0.0
            pend = None
            want = v[t] > m[t]
            if t == R + 1 and v[R] < m[R] and units > 0:  # R 날 판단 — 이동평균 아래면 R 다음 날 매도
                cash += units * v[t]; units = 0.0
            elif units > 0 and not want: pend = "sell"
            elif units == 0 and want: pend = "buy"
            out.append(cash + units * v[t])
        return np.array(out)
    # 사다리 · half_peak
    frac = 1.0 if kind == "all_ladder" else 0.5
    sold_p = None; c0 = 0.0; k = 0; steps = [] if kind == "half_peak" else [p, 2 * p, 3 * p]; done = False
    for t in range(R + 1, end + 1):
        cash *= 1 + cr[t]
        if t == R + 1:
            q = units * frac; cash += q * v[t]; units -= q; sold_p = v[t]; c0 = cash
        if pend is not None and cash > 1e-12:
            amt = min(pend, cash); units += amt / v[t]; cash -= amt
        pend = None
        if not done and cash > 1e-12:
            if v[t] >= B:
                pend = cash; done = True
            elif k < len(steps) and v[t] <= sold_p * (1 - steps[k]):
                pend = cash if k == len(steps) - 1 else c0 / len(steps); k += 1
        out.append(cash + units * v[t])
    return np.array(out)


def judge(path: np.ndarray, n: int) -> dict:
    w = path[:n]
    return {"end": float(w[-1]), "profit": bool(w[-1] > 1.0), "min": float(w.min())}


def run(s, irx, X, r, kinds, period=None) -> dict:
    E = events(s, X, r)
    if period:
        E = [e for e in E if period[0] <= e["R_date"][:4] <= period[1]]
    res = {"n_events": len(E), "events": [{k: v for k, v in e.items() if k != "R"} for e in E], "by": {}}
    for name, kind, p in kinds:
        row = {}
        for hk, n in H.items():
            J = []
            for e in E:
                path = strat(s, irx, e, kind, p, horizon=n)
                if path is not None:
                    J.append(judge(path, n))
            if J:
                ends = [j["end"] for j in J]
                row[hk] = {"n": len(J), "profit": int(sum(j["profit"] for j in J)), "all_profit": all(j["profit"] for j in J),
                           "median": round(float(np.median(ends)), 3), "worst": round(float(min(ends)), 3), "worst_min": round(float(min(j["min"] for j in J)), 3)}
        res["by"][name] = row
    return res


MA: dict = {}


def main() -> None:
    t0 = time.perf_counter()
    s, irx = load()
    for n in (50, 100, 150, 200):
        MA[n] = ma(s, n)
    # 1) 빈도
    D = declines(s); A = ath_episodes(s)
    yrs = (s.index[-1] - s.index[0]).days / 365.25
    big = [d for d in D if d["depth"] <= -10]
    freq = {"years": round(yrs, 1), "zigzag_5pct": {"n": len(D), "buckets": buckets([d["depth"] for d in D]), "per_year_over10": round(len(big) / yrs, 1),
                                                   "median_over10": round(float(np.median([d["depth"] for d in big])), 1)},
            "ath": {"n": len(A), "buckets": buckets([a["depth"] for a in A]), "list": A}}
    log("FREQ", kind="zigzag5", n=len(D), **freq["zigzag_5pct"]["buckets"], per_year_over10=freq["zigzag_5pct"]["per_year_over10"], median_over10=freq["zigzag_5pct"]["median_over10"])
    log("FREQ", kind="ath", n=len(A), **freq["ath"]["buckets"])
    # 2) 거래 시험
    kinds = [("hold", "hold", None)] + [(f"trend{n}", "trend", n) for n in (50, 100, 150, 200)] + \
            [(f"half_ladder{int(p * 100)}", "half_ladder", p) for p in (0.05, 0.10)] + [(f"all_ladder{int(p * 100)}", "all_ladder", p) for p in (0.05, 0.10)] + [("half_peak", "half_peak", None)]
    main_res = run(s, irx, X_MAIN, R_MAIN, kinds)
    log("EVENTS", X=X_MAIN, r=R_MAIN, n=main_res["n_events"], dates=",".join(e["R_date"] for e in main_res["events"]))
    for name, row in main_res["by"].items():
        log("TRADE", X=X_MAIN, r=R_MAIN, who=name, **{k: f"{v['profit']}/{v['n']}·med{v['median']}·worst{v['worst']}" for k, v in row.items()})
    # 민감도 — X × r · 시기
    sens = {}
    for X, r in itertools.product((0.075, 0.10, 0.15), (0.03, 0.05, 0.07)):
        rr = run(s, irx, X, r, kinds)
        sens[f"X{X}_r{r}"] = {name: {hk: f"{v['profit']}/{v['n']}" for hk, v in row.items()} for name, row in rr["by"].items()}
        sens[f"X{X}_r{r}"]["_n"] = rr["n_events"]
    for per in (("2000", "2012"), ("2013", "2026")):
        rr = run(s, irx, X_MAIN, R_MAIN, kinds, period=per)
        sens[f"period{per[0]}-{per[1]}"] = {name: {hk: f"{v['profit']}/{v['n']}" for hk, v in row.items()} for name, row in rr["by"].items()}
    always = {}
    for name, *_ in kinds:
        for hk in H:
            ok = all(sens[k][name].get(hk, "0/1").split("/")[0] == sens[k][name].get(hk, "0/1").split("/")[1] for k in sens if name in sens[k] and hk in sens[k][name])
            always[f"{name}_{hk}"] = ok
    log("ALWAYS", **{k: v for k, v in always.items() if v} or {"none": True})
    res = {"version": VERSION, "made": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "freq": freq, "main": main_res, "sensitivity": sens, "always_all_variants": always,
           "rules": {"X": X_MAIN, "r": R_MAIN, "horizons_days": H}}
    out = HERE / f"sp_crash_trade_{date.today().isoformat()}.json"
    out.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    log("DONE", out=out.relative_to(ROOT), sec=round(time.perf_counter() - t0, 2))


if __name__ == "__main__":
    main()
