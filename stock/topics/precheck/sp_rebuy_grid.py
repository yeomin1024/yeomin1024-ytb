#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-11-09 — 첫 폭락(−10%) → 첫 반등(+5%) 뒤 '일정 비율 매수' 규칙 격자 · 원금 회복률 비교 (사용자 지시 2026-11-09
#          "아니 기술적 지표로 매수하는 방법은 1가지만 하고 일정 비율 매수 방법을 여러가지로 해봐 몇% 하락 시 투자금의 % 매수하기 또는 반등 구간마다 몇%매수할지 등
#          여러가지 수치 변경하면서 원금 회복률 비교해서 알려줘").
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.0 | 2026-11-09 | 최초 | run_plan · grid · main |
#
# 사건 = sp_crash_trade.py events (SPY 배당 포함 · 252일 최고가에 100% → 종가 −X → 최저 종가에서 +r0 첫 반등 R · 한 사이클에 한 번).
# 매수할 돈 = R 다음 날 종가에 주식의 f 를 매도 (기본 f = 50%). 그 뒤 (판단 = 그날 종가 · 매매 = 다음 날 종가 · 현금 = ^IRX 이자):
#   A drop{d}_buy{y}  기준 값(처음 = 판 값, 사면 = 그날 산 값)보다 d 넘게 떨어지면 투자금(원금 1)의 y 만큼 매수 — 돈이 떨어질 때까지 되풀이.
#   B reb{rr}_buy{y}  기준 저점(처음 = 판 값, 사면 = 그날 산 값부터 다시)에서 rr 넘게 반등하면 투자금의 y 만큼 매수 — 되풀이.
#   _peak = 산 값(고점)을 종가로 되찾으면 남은 돈 모두 매수 · 없으면 남은 돈은 현금으로 둠.
#   비교: hold 보유 · trend200 (기술적 지표 하나 — 종가가 200일선 아래면 다음 날 현금, 위면 다음 날 매수, 처음부터 계좌 전체) · sell_peak (판 뒤 고점 되찾을 때만 다시 매수).
# 판정: 원금 회복률 = 1년·3년 안에 계좌가 원금(1) 이상이 된 날이 있었던 사건 몫 · 끝 수익 = 기간 끝 계좌 > 1 · 끝 중간값 · 가장 나쁨 · 회복까지 걸린 날(중간값).
# 민감도: 위 순위 규칙을 X 7.5·10·15% × r0 3·5·7% · f 30·50·100% 로 다시.
# 한계: 사건 9~23번 · 규칙 수십 개 중 고르면 우연히 좋아 보일 수 있음(그래서 민감도·옆 수치를 같이 봄) · 세금·수수료 없음 · 과거 자료.
# 출력: sp_rebuy_grid_<날짜>.json · sp_rebuy_grid.md. ※ 연구·교육용 — 투자 권유 아님.
from __future__ import annotations

import itertools
import json
import logging
import sys
import time
from datetime import date, datetime, timezone
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import sp_crash_trade as T  # noqa: E402  (load · events · ma — 같은 사건)

VERSION = "v1.0"
ROOT = T.ROOT
H = {"1y": 252, "3y": 756}
X0, R0, F0 = 0.10, 0.05, 0.50
DROPS, REBS, BUYS = (0.05, 0.075, 0.10, 0.15, 0.20), (0.03, 0.05, 0.07, 0.10), (0.10, 0.15, 0.20, 0.25)
log = T.log


def run_plan(v, cr, ma200, e, horizon, kind, f=F0, d=None, rr=None, y=None, peak=True):
    R, B = e["R"], e["B"]; end = R + 1 + horizon
    if end >= len(v):
        return None
    units, cash = 1.0 / B, 0.0
    vals = np.empty(end - R)
    if kind == "hold":
        return v[R + 1:end + 1] / B
    if kind == "trend200":
        pend = None
        for k, t in enumerate(range(R + 1, end + 1)):
            cash *= 1 + cr[t]
            if (pend == "sell" or (t == R + 1 and v[R] < ma200[R])) and units > 0:
                cash += units * v[t]; units = 0.0
            elif pend == "buy" and cash > 0:
                units += cash / v[t]; cash = 0.0
            pend = None
            if units > 0 and v[t] < ma200[t]: pend = "sell"
            elif units == 0 and v[t] > ma200[t]: pend = "buy"
            vals[k] = cash + units * v[t]
        return vals
    pend, ref, done = 0.0, None, False
    for k, t in enumerate(range(R + 1, end + 1)):
        cash *= 1 + cr[t]
        if t == R + 1:                                    # 첫 반등 다음 날 — 주식의 f 매도
            q = units * f; cash += q * v[t]; units -= q; ref = v[t]
        if pend > 0 and cash > 1e-12:
            amt = min(pend, cash); units += amt / v[t]; cash -= amt; ref = v[t]
        pend = 0.0
        vals[k] = cash + units * v[t]
        if done or cash <= 1e-12:
            continue
        if peak and v[t] >= B:
            pend = cash; done = True; continue
        if kind == "drop" and v[t] <= ref * (1 - d):
            pend = min(y, cash)
        elif kind == "reb":
            ref = min(ref, v[t])                          # 기준 저점
            if v[t] >= ref * (1 + rr):
                pend = min(y, cash)
    return vals


def judge(path, n):
    w = path[:n]; hit = np.nonzero(w >= 1.0)[0]
    return {"rec": bool(len(hit)), "days": int(hit[0]) if len(hit) else None, "end": float(w[-1]), "profit": bool(w[-1] > 1.0)}


def summarize(paths: list, n: int) -> dict | None:
    J = [judge(p, n) for p in paths if p is not None and len(p) >= n]
    if not J:
        return None
    ends = [j["end"] for j in J]; days = [j["days"] for j in J if j["rec"]]
    return {"n": len(J), "rec": int(sum(j["rec"] for j in J)), "rec_pct": round(100 * np.mean([j["rec"] for j in J]), 1), "profit": int(sum(j["profit"] for j in J)),
            "end_median": round(float(np.median(ends)), 3), "end_worst": round(float(min(ends)), 3), "days_median": int(np.median(days)) if days else None}


def plans():
    P = [("hold", dict(kind="hold")), ("trend200", dict(kind="trend200")), ("sell_peak", dict(kind="drop", d=9.9, y=0.0))]
    for pk in (True, False):
        tag = "_peak" if pk else ""
        P += [(f"drop{int(d * 1000) / 10:g}_buy{int(y * 100)}{tag}", dict(kind="drop", d=d, y=y, peak=pk)) for d, y in itertools.product(DROPS, BUYS)]
        P += [(f"reb{int(rr * 100)}_buy{int(y * 100)}{tag}", dict(kind="reb", rr=rr, y=y, peak=pk)) for rr, y in itertools.product(REBS, BUYS)]
    return P


def grid(s, irx, ma200, X, r0, f, names=None) -> dict:
    v, cr = s.values, irx.values / 100 / 252
    E = T.events(s, X, r0); out = {"_n": len(E)}
    for name, kw in plans():
        if names and name not in names:
            continue
        kw = dict(kw); kw.setdefault("f", f)
        if name == "sell_peak":
            kw["peak"] = True
        row = {}
        for hk, n in H.items():
            sm = summarize([run_plan(v, cr, ma200, e, n, **kw) for e in E], n)
            if sm:
                row[hk] = sm
        out[name] = row
    return out


def main() -> None:
    t0 = time.perf_counter()
    s, irx = T.load(); ma200 = T.ma(s, 200)
    G = grid(s, irx, ma200, X0, R0, F0)
    log("EVENTS", X=X0, r0=R0, f=F0, n=G["_n"])
    rank = sorted([k for k in G if k != "_n"], key=lambda k: (-G[k]["3y"]["rec_pct"], -G[k]["1y"]["rec_pct"], -G[k]["3y"]["end_worst"], -G[k]["3y"]["end_median"]))
    for k in rank:
        a, b = G[k]["1y"], G[k]["3y"]
        log("RANK", plan=k, rec1y=f"{a['rec']}/{a['n']}", rec3y=f"{b['rec']}/{b['n']}", end3y_med=b["end_median"], end3y_worst=b["end_worst"], profit3y=f"{b['profit']}/{b['n']}",
            days_med=b["days_median"])
    # 민감도 — 위 10개 + 비교 셋
    top = [k for k in rank if k not in ("hold", "trend200", "sell_peak")][:10] + ["hold", "trend200", "sell_peak"]
    sens = {}
    for X, r0 in itertools.product((0.075, 0.10, 0.15), (0.03, 0.05, 0.07)):
        g = grid(s, irx, ma200, X, r0, F0, names=set(top)); sens[f"X{X}_r{r0}_f{F0}"] = {k: {h: f"{g[k][h]['rec']}/{g[k][h]['n']}" for h in H} for k in top} | {"_n": g["_n"]}
    for f in (0.3, 1.0):
        g = grid(s, irx, ma200, X0, R0, f, names=set(top)); sens[f"X{X0}_r{R0}_f{f}"] = {k: {h: f"{g[k][h]['rec']}/{g[k][h]['n']}" for h in H} for k in top} | {"_n": g["_n"]}
    for k in top:
        log("SENS", plan=k, **{v_: f"{sens[v_][k]['1y']}|{sens[v_][k]['3y']}" for v_ in sens})
    res = {"version": VERSION, "made": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "rules": {"X": X0, "r0": R0, "f": F0, "drops": DROPS, "rebs": REBS, "buys": BUYS, "horizons": H},
           "grid": G, "rank": rank, "top": top, "sensitivity": sens}
    out = HERE / f"sp_rebuy_grid_{date.today().isoformat()}.json"
    out.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    log("DONE", out=out.relative_to(ROOT), plans=len(rank), sec=round(time.perf_counter() - t0, 2))


if __name__ == "__main__":
    main()
