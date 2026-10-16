#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-10-16 — 점 = 주 마지막 거래일 + 그날 그대로 보여야 하는 날(모든 사고판 날·큰 하락 고점/바닥·최대 낙폭 날·관망보다 가장
#          앞선 날·마지막으로 앞선 날·현금으로 기다린 처음/끝·분할 매수 끝)을 더함 — 주 점만 쓰면 2009-03-09 같은 바닥이 그 주 금요일 값으로 보여
#          대본 숫자(×1.37)와 화면(×1.22)이 달랐음. 날짜 축 t(시작일부터 날 수)를 더해 화면은 시간 비례. 낙폭·비율은 반올림을 6자리로.
# (v1.0 — 2026-10-16 — 최초.) 장면 파일(video/episodes/eonje-maesu-2026-10/index.html)이 쓰는 숫자를 만든다 — 손으로 적지 않음.
#          사용자 지시 2026-10-16 "매수 전략, 단순 전략 2가지 전략 수익 곡선으로 비교하고 날짜, 주가 움직임, 투자 금액, 매수/매도 상태, 거래 수익,
#          총 누적 수익 등을 보기 편하게 날짜가 지남에 따라 변하는걸 표현해야하고".
"""cd stock/source/eonje-maesu-2026-10/backtest && python3 anim_data.py      # → anim.js (window.ANIM)

- 엔진(daily.py)으로 본 실험을 다시 돌리고, 끝 값·매수·매도 횟수가 results.json 과 같은지 assert (다르면 멈춤).
- 주 단위(그 주 마지막 거래일)로 줄인 곡선: 날짜·지수 종가·관망 평가 금액·전략 평가 금액·주식 비율·전략 지표 선.
- 사고판 날(정확한 날짜·종가)과 거래 수익, 10년 기간 271번의 전략 ÷ 관망, 큰 하락 구간, 확인 결과 수.
"""
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[3] / "tools"))
from backtest import daily as dl  # noqa: E402
from backtest import data as bd  # noqa: E402

VERSION = "v1.1"
CAP, COST = 10_000.0, 0.001


def weekly_points(idx, s, e):
    """[s, e] 안에서 주(월~일)마다 마지막 거래일 위치 + 첫날 s · 끝날 e."""
    wk = idx[s:e + 1].to_period("W-SUN")
    last = np.r_[wk[1:] != wk[:-1], True]
    pts = sorted(set([s] + list(np.where(last)[0] + s) + [e]))
    return np.array(pts)


def week_of(pts, i):
    """거래일 위치 i 의 점 번호 (i 이상인 첫 점 — 특별한 날은 점에 들어 있어 그날 그대로)."""
    return int(np.searchsorted(pts, i))


def key_days(idx, runs, res_json, s, e):
    """그날 값이 그대로 보여야 하는 날 (거래일 위치)."""
    pos = lambda d: int(idx.searchsorted(pd.Timestamp(d)))          # noqa: E731
    out = set()
    for run in runs.values():
        out.update(f["i"] for f in run.fills)
    for c in res_json["analysis"]["crashes"]:
        out.update([pos(c["peak"]), pos(c["trough"])])
    for k, x in res_json["analysis"]["leads"].items():
        out.update(pos(d) for d in (x["max_date"], x["min_date"], x["last_ahead"], x["first_ahead"]) if d)
    for k, v in res_json["main"].items():
        out.add(pos(v["stats"]["mdd_date"]))
    for k, spells in res_json["facts"]["cash_spells"].items():
        for sp in spells:
            out.update([pos(sp["from"]), pos(sp["to"])])
    out.add(pos("1991-12-31") - (0 if str(idx[pos("1991-12-31")].date()) == "1991-12-31" else 1))
    return {i for i in out if s <= i <= e}


def lines_for(key, run, ind, pts):
    p = ind["close"]
    if key == "dip10":
        return {"ref": 0.9 * ind["ath"]}
    if key == "ladder":
        return {"l1": 0.9 * ind["ath"], "l2": 0.8 * ind["ath"], "l3": 0.7 * ind["ath"]}
    if key == "sma200":
        return {"sma200": ind["sma200"]}
    if key == "gc50_200":
        return {"sma50": ind["sma50"], "sma200": ind["sma200"]}
    if key == "brk55_20":
        return {"hi55": ind["hi55"], "lo20": ind["lo20"]}
    if key == "rsi30_70":
        return {"rsi": ind["rsi14"]}
    if key == "mom12":
        me = np.where(ind["month_end"])[0]
        ref = np.full(len(p), np.nan)
        for j in range(12, len(me)):                       # me[j] 다음 날부터 다음 달 마지막 날까지: 12달 전 달 마지막 종가
            a, b = me[j], (me[j + 1] if j + 1 < len(me) else len(p) - 1)
            ref[a:b + 1] = p[me[j - 12]]
        return {"ref12": ref}
    if key in ("stop10", "tp10"):                          # 거래 기록을 따라 그날의 문턱 선을 다시 그림 (보유 중 / 현금일 때)
        out = np.full(len(p), np.nan)
        fills = run.fills
        s0, e0 = fills[0]["i"], len(p) - 1
        for n, f in enumerate(fills):
            a = f["i"]
            b = fills[n + 1]["i"] - 1 if n + 1 < len(fills) else e0
            seg = p[a:b + 1]
            if f["side"] == "buy":
                out[a:b + 1] = 0.9 * np.maximum.accumulate(seg) if key == "stop10" else 1.1 * p[a]
            else:
                out[a:b + 1] = 1.1 * np.minimum.accumulate(seg) if key == "stop10" else 0.9 * np.maximum.accumulate(seg)
        out[:s0] = np.nan
        return {"stop" if key == "stop10" else "tp": out}
    return {}


def r(x, nd):
    return None if x is None or (isinstance(x, float) and np.isnan(x)) else round(float(x), nd)


def main():
    res_json = json.loads((HERE / "results.json").read_text("utf-8"))
    close, _ = bd.sp500_daily_long()
    mon, meta = bd.sp500_monthly()
    end = pd.Timestamp(meta["dividend_until"]) + pd.offsets.MonthEnd(0)
    c = close.loc[:end]
    tr = dl.tr_index_daily(c, mon["dividend"].dropna())
    ind, trv = dl.prepare(c, tr)
    idx = c.index
    s = int(idx.searchsorted(pd.Timestamp(res_json["settings"]["main"][0])))
    e = int(idx.searchsorted(pd.Timestamp(res_json["settings"]["main"][1]), side="right") - 1)
    runs = {k: dl.simulate(k, ind, trv, s, e, CAP, COST) for k in ["hold"] + dl.ORDER}
    pts = np.array(sorted(set(weekly_points(idx, s, e)) | key_days(idx, runs, res_json, s, e)))
    for k, run in runs.items():                             # 결과 파일과 같은지
        st = res_json["main"][k]["stats"]
        assert abs(run.value[-1] / st["final"] - 1) < 1e-9, (k, run.value[-1], st["final"])
        assert sum(f["side"] == "buy" for f in run.fills) == st["buys"] and sum(f["side"] == "sell" for f in run.fills) == st["sells"], k
    rel = pts - s                                           # run.value 는 s 부터
    A = {"version": VERSION, "capital": CAP, "cost": COST, "dates": [str(idx[i].date()) for i in pts],
         "t": [int((idx[i] - idx[s]).days) for i in pts],
         "px": [r(ind["close"][i], 2) for i in pts], "hold": [r(runs["hold"].value[j], 0) for j in rel], "order": dl.ORDER,
         "names": {k: v["name"] for k, v in res_json["main"].items()}, "S": {}}
    for k in dl.ORDER:
        run = runs[k]
        L = lines_for(k, run, ind, pts)
        st = res_json["main"][k]["stats"]
        A["S"][k] = {
            "eq": [r(run.value[j], 0) for j in rel], "sh": [r(run.stock_share[j], 3) for j in rel],
            "lines": {n: [r(v[i], 2) for i in pts] for n, v in L.items()},
            "fills": [[week_of(pts, f["i"]), 1 if f["side"] == "buy" else -1, str(idx[f["i"]].date()), r(ind["close"][f["i"]], 2), r(f["frac"], 4)]
                      for f in run.fills],
            "trades": [[week_of(pts, t["buy_i"]), week_of(pts, t["sell_i"]), r(t["ret"], 5), int(t["open"])] for t in run.trades],
            "stats": {x: st[x] for x in ("final", "cagr", "mdd", "mdd_date", "exposure", "buys", "sells", "round_trips", "win_rate", "longest_cash_days")},
        }
    hs = res_json["main"]["hold"]["stats"]
    A["holdStats"] = {x: hs[x] for x in ("final", "cagr", "mdd", "mdd_date")}
    crashes = res_json["analysis"]["crashes"]
    A["crashDrops"] = {k: [r(x["strategies"][k]["drop"], 6) for x in crashes] for k in dl.ORDER}   # 하루 자료 그대로 (주 점이 아님)
    q = s - 1                                               # 저점 매수 첫 판단 날 (시작일 전날)
    A["dip10Start"] = {"date": str(idx[q].date()), "close": r(ind["close"][q], 2), "ath": r(ind["ath"][q], 2),
                       "drop": r(ind["close"][q] / ind["ath"][q] - 1, 6)}
    A["crashes"] = [[week_of(pts, int(idx.searchsorted(pd.Timestamp(x["peak"])))), week_of(pts, int(idx.searchsorted(pd.Timestamp(x["trough"])))),
                     x["peak"], x["trough"], r(x["hold_drop"], 6)] for x in crashes]
    roll = pd.read_csv(HERE / "rolling_10y.csv", parse_dates=["start"])
    A["roll"] = {"starts": [d.strftime("%Y-%m") for d in roll["start"]], "holdMdd": [r(x, 4) for x in roll["hold_mdd"]],
                 "ratio": {k: [r(x, 4) for x in (roll[k] / roll["hold"])] for k in dl.ORDER},
                 "mdd": {k: [r(x, 4) for x in roll[k + "_mdd"]] for k in dl.ORDER}}
    R10 = res_json["rolling_10y"]
    A["rollSummary"] = {k: {x: R10[k][x] for x in ("wins", "ties", "median_vs_hold")} for k in dl.ORDER}
    A["rollSummary"]["windows"] = R10["windows"]
    A["byMdd"] = R10["by_hold_mdd"]["0.40"]
    A["sens"] = {k: {"beat": v["beat"], "mdd_better": v["mdd_better"]} for k, v in res_json["sensitivity"].items()}
    A["main"] = {"beat": res_json["main_summary"]["beat"], "mdd_better": res_json["main_summary"]["mdd_better"]}
    A["facts"] = res_json["facts"]
    A["leads"] = res_json["analysis"]["leads"]
    js = "/* anim_data.py " + VERSION + " ← results.json (run.py " + res_json["version"] + ") — 손으로 고치지 않음. 연구·교육용, 투자 권유 아님 */\n"
    js += "window.ANIM=" + json.dumps(A, ensure_ascii=False, separators=(",", ":")) + ";\n"
    (HERE / "anim.js").write_text(js, "utf-8")
    # 특별한 날이 점에 그대로 있는지 (예: 관망보다 가장 앞선 날의 비율이 결과 파일과 같은지)
    for k in dl.ORDER:
        L = res_json["analysis"]["leads"][k]
        j = A["dates"].index(L["max_date"])
        assert abs(A["S"][k]["eq"][j] / A["hold"][j] - L["max_ratio"]) < 2e-4, (k, A["S"][k]["eq"][j] / A["hold"][j], L["max_ratio"])
    print(f"[ANIM] points={len(pts)} weeks={len(weekly_points(idx, s, e))} strategies={len(dl.ORDER)} bytes={len(js)} first={A['dates'][0]} last={A['dates'][-1]} asserts=ok")


if __name__ == "__main__":
    main()
