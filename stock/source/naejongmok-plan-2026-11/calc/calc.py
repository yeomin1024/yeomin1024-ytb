#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.2 — 2026-11-09 — 2년 판정 더함 (대본 판 피드백 "야 3년을 언제 기다려 1~2년은 몰라도").
# (v1.1 — 2026-11-09 — 미국 주식만 · 기준 폭 숫자 묶음(30% 미만 · 30~50% · 50% 이상)으로 결과 (사용자 지시 "야 일단 미국 주식 기준만 하고 … 명확하게 할 수 있는것만 해소 방법으로 제시해").
# (v1.0 — 2026-11-09 — 롱폼 「폭락 뒤 반등, 살까 기다릴까 — 내 종목·내 손실에 맞춰 정하는 법」 숫자 (사용자 지시 2026-11-09
#          "너가 가장 좋다고 생각하는 안으로 대본 쓰고 평가판에 올려봐 분량은 짧게해도 되니까 전달하고자 하는걸 명확하게 해" — 앞 대화: 종목이 달라도 · 이미 물린 사람도).
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.2 | 2026-11-09 | HOR 에 2y(504거래일) | main |
# | v1.1 | 2026-11-09 | 한국 종목·KODEX 200 뺌(미국만 — 지수 = SPY) · by_D 묶음(사건 때 기준 폭 D) 요약 · 판단이 필요한 묶음 이름(대형주·변동 큰 종목)은 대본에 안 씀 | main |
# | v1.0 | 2026-11-09 | 최초 (같은 날 더함: 물린 사람 idx_third·idx_half — 남길 몫만 남기고 나머지를 지수로 · 미국 종목 = SPY, 한국 종목 = KODEX 200) | base_drop · events · cash_plans · stuck_plans · main |
#
# '내 종목 기준 폭' D = 그 종목의 지난 2년(504거래일) 안에서 고점→저점으로 가장 크게 하락한 폭 (판단하는 날까지의 자료만 — 이번 폭락이 시작된 고점 전 2년).
# 사건 (종목마다 D 에 맞춤): 산 값 B = 252거래일 최고 종가 → 종가가 B 보다 max(10%, D/2) 넘게 하락(첫 폭락) → 그 뒤 최저 종가에서 max(5%, D/4) 넘게 오른 첫날 R(첫 반등).
#   한 사이클에 한 번 (B 를 되찾았거나 R 에서 252거래일 뒤).
# 현금 있는 사람 (R 다음 날 현금 1): all 반등에 모두 · wait 산 값 B 를 되찾으면(확실해지면) 모두 · split 반등에 1/3 → 직전에 산 값보다 D/2 떨어질 때마다 1/3 → B 를 되찾으면 나머지.
# 물린 사람 (B 에 100% → 계좌 = 주가/B): hold 보유 · restart '오늘 다시 시작' = R 다음 날 주식의 2/3 를 팔고(1/3 남김) 그 현금으로 split 과 같은 규칙
#   · idx_third 1/3 만 남기고 2/3 를 지수로 · idx_half 절반만 남기고 절반을 지수로 (지수 = 미국 종목 SPY · 한국 종목 KODEX 200 · 지수 묶음은 그 자신).
# 판정 1·3년: 현금 — 끝 값 중간값 · 가장 크게 줄어든 폭 · 세 방법 중 꼴찌였던 몫 / 물린 — 원금(1) 회복 몫 · 끝 중간값 · 가장 나쁨 · 지금보다 나빠진 몫.
# 판단 = 그날 종가 · 매매 = 다음 거래일 종가 · 현금 = ^IRX(미국 13주 국채 — 한국 종목도 같은 이자로 단순화) · 세금·수수료 없음.
# 한계: 지금 남아 있는 종목만(생존 편향) · 종목 수십 개 · 같은 하락장 안 사건 겹침 · 과거 자료. ※ 연구·교육용 — 투자 권유 아님.
from __future__ import annotations

import json
import logging
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

VERSION = "v1.2"
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
DATA = ROOT / "stock/topics/precheck/data"
IRX_CSV = ROOT / "stock/source/timing-test-2026-10/calc/irx_daily.csv"
OUT = HERE / "result.json"
GROUPS = {
    "지수": ["SPY", "QQQ"],
    "대형주": ["AAPL", "MSFT", "AMZN", "GOOGL", "META", "NFLX", "ORCL", "CSCO", "INTC", "QCOM", "BAC", "C", "F", "GE"],
    "변동 큰 종목": ["NVDA", "TSLA", "AMD", "MU", "SHOP", "PYPL", "ZM", "PTON", "DOCU", "ROKU", "SNAP", "PLTR", "COIN", "NET", "CRWD", "SQ", "XYZ",
                 "TWLO", "DKNG", "AFRM", "HOOD", "SOFI", "MARA", "RIOT", "ENPH", "PLUG", "UPST", "LCID", "RIVN", "NIO", "MRNA", "MSTR", "SMCI", "IONQ", "AI", "EBAY",
                 "ETSY", "W", "PINS", "U", "SNOW", "CHWY", "BABA", "JD", "TDOC", "FSLY", "OKTA", "CVNA", "GME", "AMC", "BYND", "AIG"],
    "레버리지 ETF": ["SOXL", "TQQQ", "TNA", "QLD"],
}
KR: dict = {}
HOR = {"1y": 252, "2y": 504, "3y": 756}

logging.basicConfig(level=logging.INFO, format="%(message)s", stream=sys.stdout)
def log(stage: str, **kv) -> None:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    logging.info(f"[{stage}] [{ts}] " + " ".join(f"{k}={v}" for k, v in kv.items()))


def read(sym: str) -> pd.Series | None:
    p = DATA / f"{sym}.csv"
    if not p.exists():
        return None
    try:
        s = pd.read_csv(p, comment="#", parse_dates=["date"]).set_index("date")["adjclose"].astype(float)
    except Exception as e:  # noqa: BLE001
        log("FAIL", stage="data", sym=sym, err=repr(e)); return None
    s = s[~s.index.duplicated(keep="last")]
    s = s[(s > 0) & s.notna()]
    return s if len(s) > 900 else None


def max_dd(v: np.ndarray) -> float:
    peak = np.maximum.accumulate(v); return float((v / peak - 1).min())


def base_drop(v: np.ndarray, end: int) -> float | None:
    """end(포함) 전 504거래일 안 가장 큰 하락 폭 (양수)."""
    if end < 504:
        return None
    return -max_dd(v[end - 504:end + 1])


def events(sym: str, s: pd.Series) -> list[dict]:
    v, I = s.values, s.index; out = []; i = 756; last_R = -10 ** 9; need = None
    while i < len(v) - 2:
        if need is not None and v[i] >= need:
            need = None
        hi = int(np.argmax(v[i - 251:i + 1])) + i - 251; B = v[hi]
        D = base_drop(v, hi)
        if D is None:
            i += 1; continue
        X, r = max(0.10, D / 2), max(0.05, D / 4)
        if v[i] <= B * (1 - X) and (need is None or i - last_R > 252):
            low = v[i]; j = i
            while j < len(v) - 2:
                j += 1; low = min(low, v[j])
                if v[j] >= low * (1 + r):
                    break
            if j >= len(v) - 2:
                break
            out.append({"sym": sym, "B": float(B), "D": round(D, 3), "X": round(X, 3), "r": round(r, 3), "peak": I[hi].strftime("%Y-%m-%d"), "R": j,
                        "R_date": I[j].strftime("%Y-%m-%d"), "value_R": round(v[j] / B, 3)})
            last_R, need, i = j, B, j + 1; continue
        i += 1
    return out


def ladder(v, cr, start, end, cash, units, unit_cash, step, B):
    """split·restart 공통 — 직전에 산 값보다 step 떨어질 때마다 unit_cash 매수 · B 회복 시 나머지 · 다음 날 종가 매매."""
    path = []; pend = 0.0; last = v[start]; done = False
    for t in range(start, end + 1):
        if t > start:
            cash *= 1 + cr[t]
        if pend > 0 and cash > 1e-12:
            amt = min(pend, cash); units += amt / v[t]; cash -= amt; last = v[t]
        pend = 0.0
        path.append(cash + units * v[t])
        if done or cash <= 1e-12:
            continue
        if v[t] >= B:
            pend = cash; done = True
        elif v[t] <= last * (1 - step):
            pend = min(unit_cash, cash)
    return np.array(path)


def cash_plans(v, cr, e, n):
    R = e["R"]; s0 = R + 1; end = s0 + n
    if end >= len(v):
        return None
    p = v[s0:end + 1]
    allp = p / p[0]
    hit = np.nonzero(p >= e["B"])[0]
    if len(hit) and hit[0] + 1 <= n:
        k = hit[0] + 1; c = np.cumprod(np.r_[1.0, 1 + cr[s0 + 1:s0 + k + 1]])
        wait = np.r_[c[:k], c[k - 1] * (1 + cr[s0 + k]) * p[k:] / p[k]] if k < len(p) else c
        wait = wait[:len(p)]
    else:
        wait = np.cumprod(np.r_[1.0, 1 + cr[s0 + 1:end + 1]])
    # split: 1/3 반등(R 다음 날)
    units = (1 / 3) / v[s0]; split = ladder(v, cr, s0, end, 2 / 3, units, 1 / 3, e["D"] / 2, e["B"])
    return {"all": allp, "wait": wait, "split": split}


def stuck_plans(v, cr, e, n, ix):
    R = e["R"]; s0 = R + 1; end = s0 + n
    if end >= len(v):
        return None
    hold = v[s0:end + 1] / e["B"]
    a0 = v[s0] / e["B"]
    units = (a0 / 3) / v[s0]; restart = ladder(v, cr, s0, end, a0 * 2 / 3, units, a0 / 3, e["D"] / 2, e["B"])
    out = {"hold": hold, "restart": restart}
    w = ix[s0:end + 1]
    if not np.isnan(w).any():
        out["idx_third"] = hold / 3 + (a0 * 2 / 3) * w / w[0]
        out["idx_half"] = hold / 2 + (a0 / 2) * w / w[0]
    return out


def main() -> None:
    t0 = time.perf_counter()
    irx = pd.read_csv(IRX_CSV, comment="#", parse_dates=["date"]).set_index("date")["close"].astype(float)
    base, E, used, missing = {}, [], {}, []
    IDX = {"SPY": read("SPY")}
    for g, syms in GROUPS.items():
        for sym in syms:
            s = read(sym)
            if s is None:
                missing.append(sym); continue
            used[sym] = g
            v = s.values
            # 흔한 하락 폭 — 2년마다 끊어 그 안 가장 큰 하락 (2010년 이후 · 자료 있는 기간)
            s2 = s["2010-01-01":]
            chunks = [-max_dd(s2.values[k:k + 504]) for k in range(0, len(s2) - 252, 504)]
            base[sym] = {"group": g, "name": KR.get(sym, sym), "median_2y_maxdrop": round(float(np.median(chunks)) * 100, 1) if chunks else None, "n_chunks": len(chunks)}
            cr = irx.reindex(s.index).ffill().fillna(0).values / 100 / 252
            ixs = IDX["SPY"]
            ix = ixs.reindex(s.index).ffill().values
            for e in events(sym, s):
                e["group"] = g; e["cash"] = {}; e["stuck"] = {}
                for hk, n in HOR.items():
                    cp, sp = cash_plans(v, cr, e, n), stuck_plans(v, cr, e, n, ix)
                    if cp:
                        e["cash"][hk] = {k: {"end": float(x[-1]), "mdd": float(x.min() - 1)} for k, x in cp.items()}
                    if sp:
                        e["stuck"][hk] = {k: {"end": float(x[-1]), "rec": bool((x >= 1.0).any()), "start": float(x[0]), "min": float(x.min())} for k, x in sp.items()}
                E.append(e)
    log("DATA", tickers=len(used), missing=",".join(missing) or "-", events=len(E))
    # 흔한 하락 폭 — 그룹별 중간값
    gb = {}
    for g in GROUPS:
        vals = [b["median_2y_maxdrop"] for b in base.values() if b["group"] == g and b["median_2y_maxdrop"]]
        gb[g] = {"n": len(vals), "median": round(float(np.median(vals)), 1) if vals else None, "range": [min(vals), max(vals)] if vals else None}
        log("BASE", group=g, **gb[g])
    for sym in ("SPY", "QQQ", "069500.KS", "005930.KS", "000660.KS", "AAPL", "NVDA", "TSLA", "SOXL"):
        if sym in base:
            log("BASE", sym=base[sym]["name"], median_2y_maxdrop=base[sym]["median_2y_maxdrop"])
    summ = {}
    for scope in ["전체"] + list(GROUPS):
        G = [e for e in E if scope == "전체" or e["group"] == scope]
        summ[scope] = {}
        for hk in HOR:
            Gc = [e for e in G if hk in e["cash"]]
            Gs = [e for e in G if hk in e["stuck"]]
            row = {"n": len(Gc)}
            for k in ("all", "wait", "split"):
                ends = [e["cash"][hk][k]["end"] for e in Gc]; mdd = [e["cash"][hk][k]["mdd"] for e in Gc]
                worst_of3 = sum(1 for e in Gc if e["cash"][hk][k]["end"] == min(e["cash"][hk][x]["end"] for x in ("all", "wait", "split")))
                best_of3 = sum(1 for e in Gc if e["cash"][hk][k]["end"] == max(e["cash"][hk][x]["end"] for x in ("all", "wait", "split")))
                row[k] = {"end_median": round(float(np.median(ends)), 3) if ends else None, "end_worst": round(float(min(ends)), 3) if ends else None,
                          "mdd_worst": round(float(min(mdd)) * 100, 1) if mdd else None, "mdd_median": round(float(np.median(mdd)) * 100, 1) if mdd else None,
                          "worst_of3": worst_of3, "best_of3": best_of3, "loss_over20": sum(1 for m in mdd if m < -0.20),
                          "ret_median_pct": round((float(np.median(ends)) - 1) * 100, 1) if ends else None,
                          "loss_over20_pct": round(100 * sum(1 for m in mdd if m < -0.20) / len(mdd), 1) if mdd else None}
            row["stuck_n"] = len(Gs)
            for k in ("hold", "restart", "idx_third", "idx_half"):
                J = [e["stuck"][hk][k] for e in Gs if k in e["stuck"][hk]]
                row["stuck_" + k] = {"rec": sum(j["rec"] for j in J), "end_median": round(float(np.median([j["end"] for j in J])), 3) if J else None,
                                     "end_worst": round(float(min(j["end"] for j in J)), 3) if J else None, "worse": sum(1 for j in J if j["end"] < j["start"]),
                                     "min_worst": round(float(min(j["min"] for j in J)), 3) if J else None,
                                     "rec_pct": round(100 * sum(j["rec"] for j in J) / len(J), 1) if J else None,
                                     "worse_pct": round(100 * sum(1 for j in J if j["end"] < j["start"]) / len(J), 1) if J else None}
            summ[scope][hk] = row
            log("CASH", scope=scope, h=hk, n=row["n"], **{k: f"med{row[k]['end_median']}·worst{row[k]['end_worst']}·mddW{row[k]['mdd_worst']}·꼴찌{row[k]['worst_of3']}·1등{row[k]['best_of3']}·−20%넘게{row[k]['loss_over20']}" for k in ("all", "wait", "split")})
            log("STUCK", scope=scope, h=hk, n=row["stuck_n"], **{k: f"rec{row['stuck_' + k]['rec']}·med{row['stuck_' + k]['end_median']}·worst{row['stuck_' + k]['end_worst']}·minW{row['stuck_' + k]['min_worst']}·나빠짐{row['stuck_' + k]['worse']}" for k in ("hold", "restart", "idx_third", "idx_half")})
    # 기준 폭(사건 때 D) 묶음 — 시청자가 숫자로 나눌 수 있게
    byD = {}
    for lab, lo, hi in (("D<30%", 0, 0.30), ("D 30~50%", 0.30, 0.50), ("D>=50%", 0.50, 9)):
        G = [e for e in E if lo <= e["D"] < hi]; byD[lab] = {}
        for hk in HOR:
            Gc = [e for e in G if hk in e["cash"]]; Gs = [e for e in G if hk in e["stuck"] and "idx_half" in e["stuck"][hk]]
            row = {"n": len(Gc), "stuck_n": len(Gs)}
            for k in ("all", "wait", "split"):
                ends = [e["cash"][hk][k]["end"] for e in Gc]; mdd = [e["cash"][hk][k]["mdd"] for e in Gc]
                row[k] = {"ret_median_pct": round((float(np.median(ends)) - 1) * 100, 1) if ends else None, "loss_over20_pct": round(100 * sum(1 for m in mdd if m < -0.2) / len(mdd), 1) if mdd else None,
                          "worst_of3": sum(1 for e in Gc if e["cash"][hk][k]["end"] == min(e["cash"][hk][x]["end"] for x in ("all", "wait", "split")))}
            for k in ("hold", "idx_half"):
                J = [e["stuck"][hk][k] for e in Gs]
                row["stuck_" + k] = {"rec_pct": round(100 * sum(j["rec"] for j in J) / len(J), 1) if J else None, "worse_pct": round(100 * sum(1 for j in J if j["end"] < j["start"]) / len(J), 1) if J else None,
                                     "end_median": round(float(np.median([j["end"] for j in J])), 3) if J else None}
            byD[lab][hk] = row
            log("BY_D", d=lab, h=hk, n=row["n"], split_last=row["split"]["worst_of3"], all_ret=row["all"]["ret_median_pct"], split_ret=row["split"]["ret_median_pct"], wait_ret=row["wait"]["ret_median_pct"],
                all_l20=row["all"]["loss_over20_pct"], split_l20=row["split"]["loss_over20_pct"], hold=json.dumps(row["stuck_hold"]), half=json.dumps(row["stuck_idx_half"]))
    res = {"version": VERSION, "made": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "groups": GROUPS, "by_D": byD, "used": used, "missing": missing, "base": base, "base_group": gb,
           "summary": summ, "events": [{k: e[k] for k in ("sym", "group", "peak", "R_date", "D", "X", "r", "value_R")} | {"cash": e["cash"], "stuck": e["stuck"]} for e in E]}
    OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    log("DONE", out=OUT.relative_to(ROOT), sec=round(time.perf_counter() - t0, 2))


if __name__ == "__main__":
    main()
