#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v2.0 — 2026-11-07 — 사용자 지시 "수익률을 실시간으로 표시해 개미들도 분할 매수는 하잖아 잘못되게 해서 그렇지 · 역대 폭락들 중 손실을 줄이면서
#          매수하는 방법을 찾아서 그걸 전문가 의견이랑 합쳐서 적용해 (spy 매수 기준으로 평단 기준 몇퍼센트 떨어져야 얼마만큼 매수하는지) · 금액 안보여줘도 돼".
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v2.0 | 2026-11-07 | ^GSPC → SPY 수정 종가(배당 포함) · 현금 = ^IRX 국채 이자 · 금액(원) 대신 계좌 수익률(%) · 개미 = 잘못된 물타기(반등에 50%·평단 −5%마다 25%·다 쓴 뒤 평단 −20% 공포 매도) · 대가 = 규칙 격자 108개를 역대 반등 20번에 시험해 고름(전문가 원칙 + 원금 −20% 넘게 준 횟수 최소) + 한 사건씩 빼고 검증 · 평가 12개월 | load·events·sim·pick·main |
# | v1.0 | 2026-11-07 | 최초 (^GSPC · 1억 원 · 개미 한 번에 · 대가 5등분 10%마다 · 6개월) | — |
#
# 규칙 (판단 = 그날 종가, 매매 = 다음 거래일 종가 · 같은 종가로 판단·매매 ✗ · 평단 = 지금까지 산 값의 평균):
#   반등 사건 = 2000년 이후, 전날 종가가 252거래일 최고가보다 10% 넘게 낮은 상태에서 하루 +3% 넘게 오른 날 (앞 사건과 60거래일 넘게 떨어진 것만).
#   첫 매수 = 반등 날 다음 거래일 종가. 남은 돈 = 현금(^IRX 단기 국채 이자, 날마다 연 이율 ÷ 252).
#   개미 (흔한 잘못된 물타기 — 가정): 반등에 투자금의 50% → 평단보다 5% 떨어질 때마다 25% (두 번째엔 남은 돈 전부) → 돈을 다 쓴 뒤 평단보다 20% 넘게
#        떨어지면 겁이 나서 전부 매도, 그 뒤 현금.
#   대가 = 아래 격자에서 고름 — 첫 매수 비중 A0 · 평단 대비 하락폭 D · 다음 매수 크기 = 직전 × G (마지막은 남은 돈) · 팔지 않음.
#        전문가 원칙: 하워드 막스(2020-03 메모 「Nobody Knows II」 — 바닥까지 넣을 돈을 정하고 일부만 먼저, 떨어지면 남은 돈으로 더) → A0 ≤ 30% ·
#                    워런 버핏(2008-10 뉴욕타임스 「Buy American. I Am.」 — 남들이 두려워할 때 욕심을) → 떨어질수록 더 크게 G ≥ 1.5 · 빚·손절 없음.
#        자료 기준(순서대로): ① 원금보다 20% 넘게 줄어든 사건 수가 가장 적음 ② 가장 크게 줄어든 폭이 가장 작음 ③ 안정 수익(예금보다 더 + 원금 −20% 넘게 안 줄어듦 —
#                    stock/topics/precheck/risk.py 와 같은 정의) 사건 수가 많음 ④ 12개월 수익률 중앙값이 큼.
#        검증 = 한 사건씩 빼고 나머지 19번으로 같은 기준으로 고른 규칙을 뺀 사건에 넣어 봄 (표본 안 최적화 낙관을 보려고).
#   평가 = 첫 매수일부터 12개월 뒤(그날이 없으면 다음 거래일) · 수익률 = 계좌 전체(주식 + 현금) ÷ 처음 투자금 − 1.
# 출력: calc/result.json + 영상용 video/episodes/bandeung-maesu-2026-11-shorts/data.js. ※ 연구·교육용 — 투자 권유 아님. 세금·수수료·환율 없음.
from __future__ import annotations

import itertools
import json
import logging
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

VERSION = "v2.0"
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SPY_CSV = ROOT / "stock/topics/precheck/data/SPY.csv"                    # SPY 일별 (adjclose = 배당·분할 반영) — Yahoo chart API, 2026-10-29 받음
IRX_CSV = ROOT / "stock/source/timing-test-2026-10/calc/irx_daily.csv"   # ^IRX 13주 국채 금리(%) — Yahoo chart API, 2026-10-28 받음
OUT = HERE / "result.json"
DATA_JS = ROOT / "video/episodes/bandeung-maesu-2026-11-shorts/data.js"
H_MONTHS = 12
REB_TH, DD_TH, GAP = 0.03, -0.10, 60
LOSS_L = 0.20
ANT = {"first": 0.50, "drop": 0.05, "size": 0.25, "max_buys": 3, "stop": 0.20}
GRID_A0 = [0.10, 0.15, 0.20, 0.25, 0.30, 0.40]
GRID_D = [0.05, 0.075, 0.10, 0.125, 0.15, 0.20]
GRID_G = [1.0, 1.5, 2.0]
SCENES = {"real": "2025-04-09", "fake": "2020-03-02"}

logging.basicConfig(level=logging.INFO, format="%(message)s", stream=sys.stdout)
def log(stage: str, **kv) -> None:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    logging.info(f"[{stage}] [{ts}] " + " ".join(f"{k}={v}" for k, v in kv.items()))


def load() -> tuple[pd.Series, pd.Series]:
    try:
        spy = pd.read_csv(SPY_CSV, comment="#", parse_dates=["date"]).set_index("date")["adjclose"].astype(float)
        irx = pd.read_csv(IRX_CSV, comment="#", parse_dates=["date"]).set_index("date")["close"].astype(float)
    except Exception as e:  # noqa: BLE001
        log("FAIL", stage="data", spy=SPY_CSV, irx=IRX_CSV, err=repr(e), next="precheck.py · timing-test calc.py --fetch 로 다시 받기")
        raise
    for name, s in (("SPY", spy), ("IRX", irx)):
        log("DATA", source=name, rows=len(s), first=s.index[0].date(), last=s.index[-1].date(), dup=int(s.index.duplicated().sum()),
            na=int(s.isna().sum()), nonpositive=int((s <= 0).sum()) if name == "SPY" else "-", gaps_over_5d=int((s.index.to_series().diff().dt.days > 5).sum()))
    if spy.index.duplicated().any() or spy.isna().any() or (spy <= 0).any():
        raise SystemExit("SPY 자료 이상 — 중복·빈 값·0 이하")
    irx = irx.reindex(spy.index).ffill()
    if irx.isna().any():
        log("WARN", stage="data", msg="IRX 앞부분 빈 값 → 0 으로", n=int(irx.isna().sum())); irx = irx.fillna(0.0)
    return spy, irx


def events(spy: pd.Series) -> list[int]:
    r = spy.pct_change(); hi = spy.rolling(252, min_periods=60).max(); dd = spy.shift(1) / hi.shift(1) - 1
    cand = spy.index[(r >= REB_TH) & (dd <= DD_TH) & (spy.index >= "2000-01-01")]
    out, last = [], None
    for d in cand:
        i = spy.index.get_loc(d)
        if last is None or i - last > GAP:
            out.append(i); last = i
    return out


class Sim:
    """판단은 그날 종가, 매매는 다음 거래일 종가. rows = 날마다 [순번, 계좌(처음 = 1), 주식 비중, 평단(없으면 0)]."""

    def __init__(self, spy: pd.Series, irx: pd.Series):
        self.P = spy.values; self.I = spy.index; self.CR = irx.values / 100 / 252

    def end_of(self, e: int, months: int) -> int | None:
        t = self.I[e + 1] + pd.DateOffset(months=months)
        j = int(np.searchsorted(self.I.values, np.datetime64(t)))
        return j if j < len(self.I) else None

    def run(self, e: int, months: int, first: float, nextf, stop: float | None = None, max_buys: int = 99, keep_rows: bool = False):
        end = self.end_of(e, months)
        if end is None:
            return None
        cash, units, cost, pend, sell, nb, out, dep, mn = 1.0, 0.0, 0.0, first, False, 0, False, 1.0, 1.0
        trades, rows = [], []
        for i in range(e + 1, end + 1):
            p = self.P[i]; cash *= 1 + self.CR[i]; dep *= 1 + self.CR[i]
            if sell and units > 0:
                cash += units * p; trades.append(("SELL", i, units * p)); units = 0.0; out = True; sell = False
            if pend > 0 and not out:
                amt = cash if nb + 1 >= max_buys else min(pend, cash)
                units += amt / p; cost += amt; cash -= amt; nb += 1; trades.append(("BUY", i, amt)); pend = 0.0
            v = cash + units * p; mn = min(mn, v)
            avg = cost / units if units > 0 else 0.0
            if keep_rows:
                rows.append([i, v, (units * p) / v if v > 0 else 0.0, avg])
            if units > 0 and not out:
                nx = nextf(nb)
                if nx and nb < max_buys and cash > 1e-9 and p <= avg * (1 - nx[0]):
                    pend = nx[1]
                if stop and nb >= max_buys and p <= avg * (1 - stop):
                    sell = True
        return {"ret": v - 1, "mdd": mn - 1, "dep": dep - 1, "buys": nb, "trades": trades, "rows": rows, "end": end}


def stable(x: dict) -> bool:
    return x["ret"] > x["dep"] and x["mdd"] >= -LOSS_L


def master_next(a0: float, d: float, g: float):
    sizes = [a0 * g ** k for k in range(1, 40)]
    return lambda nb: (d, sizes[nb - 1]) if nb - 1 < len(sizes) else None


def ant_run(sim: Sim, e: int, months: int, keep_rows=False):
    return sim.run(e, months, ANT["first"], lambda nb: (ANT["drop"], ANT["size"]), stop=ANT["stop"], max_buys=ANT["max_buys"], keep_rows=keep_rows)


def pick(cache: dict, evs: list[int]) -> tuple:
    pool = [g for g in cache if g[0] <= 0.30 and g[2] >= 1.5]                      # 전문가 원칙 (막스 · 버핏)
    def k(g):
        res = [cache[g][e] for e in evs]
        return (-sum(1 for x in res if x["mdd"] < -LOSS_L), round(min(x["mdd"] for x in res), 3), sum(stable(x) for x in res), float(np.median([x["ret"] for x in res])))
    return max(pool, key=k)


def summary(res: list[dict]) -> dict:
    r = np.array([x["ret"] for x in res]); m = np.array([x["mdd"] for x in res])
    return {"n": len(res), "stable": int(sum(stable(x) for x in res)), "loss20": int((m < -LOSS_L).sum()), "median_ret": round(float(np.median(r)) * 100, 1),
            "worst_ret": round(float(r.min()) * 100, 1), "worst_mdd": round(float(m.min()) * 100, 1), "win": int((r > 0).sum())}


def main() -> None:
    t0 = time.perf_counter()
    spy, irx = load()
    sim = Sim(spy, irx)
    ev = [e for e in events(spy) if sim.end_of(e, H_MONTHS) is not None]
    log("EVENTS", n=len(ev), rule=f"dd<={DD_TH:.0%} & day>={REB_TH:.0%} & gap>{GAP}", dates=",".join(spy.index[e].strftime("%Y-%m-%d") for e in ev))
    log("RULES", ant=json.dumps(ANT), grid=f"A0{GRID_A0} D{GRID_D} G{GRID_G}", horizon_m=H_MONTHS, cash="^IRX", trade="decide close t, trade close t+1")
    grid = list(itertools.product(GRID_A0, GRID_D, GRID_G))
    cache = {g: {e: sim.run(e, H_MONTHS, g[0], master_next(*g)) for e in ev} for g in grid}
    ant = {e: ant_run(sim, e, H_MONTHS) for e in ev}
    lump = {e: sim.run(e, H_MONTHS, 1.0, lambda nb: None) for e in ev}
    best = pick(cache, ev)
    S_ant, S_mas, S_lump = summary(list(ant.values())), summary([cache[best][e] for e in ev]), summary(list(lump.values()))
    log("PICK", a0=best[0], drop=best[1], growth=best[2], sizes="/".join(f"{best[0] * best[2] ** k * 100:.2f}%" for k in range(5)))
    for name, sm in (("ant", S_ant), ("master", S_mas), ("lump", S_lump)):
        log("SUMMARY", who=name, **sm)
    # 한 사건씩 빼고 검증
    loo = []
    for e in ev:
        b = pick(cache, [x for x in ev if x != e]); x = cache[b][e]
        loo.append({"rebound": spy.index[e].strftime("%Y-%m-%d"), "rule": b, "ret": round(x["ret"] * 100, 1), "mdd": round(x["mdd"] * 100, 1), "stable": bool(stable(x))})
    S_loo = {"loss20": int(sum(1 for o in loo if o["mdd"] < -LOSS_L * 100)), "stable": int(sum(bool(o["stable"]) for o in loo)), "worst_mdd": float(min(o["mdd"] for o in loo)),
             "rules": sorted({tuple(o["rule"]) for o in loo})}
    log("LOO", **{k: (v if not isinstance(v, list) else ";".join(map(str, v))) for k, v in S_loo.items()})
    # 사건별 표
    per = []
    for e in ev:
        a, m = ant[e], cache[best][e]
        per.append({"rebound": spy.index[e].strftime("%Y-%m-%d"), "ant_ret": round(a["ret"] * 100, 1), "ant_mdd": round(a["mdd"] * 100, 1),
                    "master_ret": round(m["ret"] * 100, 1), "master_mdd": round(m["mdd"] * 100, 1), "master_buys": int(m["buys"]), "ant_sold": any(t[0] == "SELL" for t in a["trades"])})
        log("EVENT", **per[-1])
    # 영상 두 장면 (그래프 앞부분 = 반등 전 120거래일 안 최고가부터)
    scenes = {}
    for key, d in SCENES.items():
        e = spy.index.get_loc(pd.Timestamp(d))
        a = ant_run(sim, e, H_MONTHS, keep_rows=True); m = sim.run(e, H_MONTHS, best[0], master_next(*best), keep_rows=True)
        b0 = e + 1; base = spy.iloc[b0]
        pk = int(np.argmax(spy.values[max(0, e - 120):e + 1])) + max(0, e - 120)
        pre = list(range(pk, b0))
        rows = [[spy.index[i].strftime("%Y-%m-%d"), round(spy.iloc[i] / base * 100, 3), 0.0, 0.0, 0.0, 0.0, 0.0] for i in pre]
        for ra, rm in zip(a["rows"], m["rows"]):
            i = ra[0]
            rows.append([spy.index[i].strftime("%Y-%m-%d"), round(spy.iloc[i] / base * 100, 3), round((ra[1] - 1) * 100, 2), round((rm[1] - 1) * 100, 2),
                         round(ra[2] * 100, 1), round(rm[2] * 100, 1), round(rm[3] / base * 100, 3) if rm[3] else 0.0])
        bottom = min(range(len(pre), len(rows)), key=lambda k: rows[k][1])
        tr = lambda x: [[t[0], spy.index[t[1]].strftime("%Y-%m-%d"), round(t[2] * 100, 2)] for t in x["trades"]]
        scenes[key] = {"rebound": d, "rebound_ret": round((spy.iloc[e] / spy.iloc[e - 1] - 1) * 100, 2), "first_buy": spy.index[b0].strftime("%Y-%m-%d"),
                       "end": spy.index[a["end"]].strftime("%Y-%m-%d"), "pre_n": len(pre), "peak": spy.index[pk].strftime("%Y-%m-%d"),
                       "crash_before": round((spy.iloc[e - 1] / spy.iloc[pk] - 1) * 100, 1), "more_drop": round((rows[bottom][1] / 100 - 1) * 100, 1),
                       "bottom": rows[bottom][0], "ant_ret": round(a["ret"] * 100, 1), "ant_mdd": round(a["mdd"] * 100, 1), "master_ret": round(m["ret"] * 100, 1),
                       "master_mdd": round(m["mdd"] * 100, 1), "ant_trades": tr(a), "master_trades": tr(m), "rows": rows}
        log("SCENE", key=key, rebound=d, kind="fake" if rows[bottom][1] < rows[len(pre) - 1][1] * (spy.iloc[e - 1] / spy.iloc[e]) else "real",
            more_drop=scenes[key]["more_drop"], bottom=rows[bottom][0], ant_ret=scenes[key]["ant_ret"], master_ret=scenes[key]["master_ret"],
            ant_trades=len(a["trades"]), master_buys=m["buys"])
    res = {"version": VERSION, "made": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
           "source": {"spy": str(SPY_CSV.relative_to(ROOT)), "irx": str(IRX_CSV.relative_to(ROOT))},
           "rules": {"ant": ANT, "master": {"a0": best[0], "drop": best[1], "growth": best[2]}, "horizon_m": H_MONTHS, "events_rule": [REB_TH, DD_TH, GAP], "loss_l": LOSS_L},
           "summary": {"ant": S_ant, "master": S_mas, "lump": S_lump, "loo": S_loo}, "events": per, "loo": loo, "scenes": scenes}
    OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1, default=str), encoding="utf-8")
    key = {k: {f: v[f] for f in v if f != "rows"} for k, v in scenes.items()}
    DATA_JS.write_text(
        f"// 자동 생성 — stock/source/bandeung-maesu-2026-11/calc/result.json (calc.py {VERSION}, {res['made']}) · 고치지 말고 calc 를 다시 돌림\n"
        "// SER.<장면> = [날짜, SPY(첫 매수일 종가 = 100), 개미 수익률 %, 대가 수익률 %, 개미 주식 비중 %, 대가 주식 비중 %, 대가 평단(첫 매수일 = 100, 없으면 0)]\n"
        f"window.SER={json.dumps({k: v['rows'] for k, v in scenes.items()}, ensure_ascii=False)};\n"
        f"window.KEY={json.dumps(key, ensure_ascii=False)};\n"
        f"window.RULE={json.dumps(res['rules'], ensure_ascii=False)};\n"
        f"window.SUM={json.dumps({'ant': S_ant, 'master': S_mas, 'loo': {k: v for k, v in S_loo.items() if k != 'rules'}}, ensure_ascii=False)};\n"
        "// EV = 반등 사건 [날짜, 개미 12개월 수익률 %, 개미 가장 크게 줄어든 폭 %, 대가 12개월 수익률 %, 대가 가장 크게 줄어든 폭 %]\n"
        f"window.EV={json.dumps([[p['rebound'], p['ant_ret'], p['ant_mdd'], p['master_ret'], p['master_mdd']] for p in per])};\n", encoding="utf-8")
    log("DONE", out=OUT.relative_to(ROOT), data_js=DATA_JS.relative_to(ROOT), sec=round(time.perf_counter() - t0, 2))


if __name__ == "__main__":
    main()
