#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-10-15 — 장면 숫자 num(results.json 값 그대로)·하락 폭 dd·기간별 평균 단가 비 cost10·목돈 비 l12/l120 더함,
#          목돈 race 12달(2008-04 … 2009-03 — lump_vs_split 의 끝 달 s+11 과 같게).
# v1.0 — 2026-10-15 — 영상 애니메이션 자료 (사용자 지시 2026-10-15 "날짜가 지남에 따라 백테스트 수치를 실시간 비교하는 과정을
#          애니메이션으로 표현하면 좋겠지"). run.py 와 같은 엔진·같은 규칙(월평균 −10%, 현금 이자 0, 매달 100만 원)으로 월별 값을 뽑아
#          backtest/anim.js (window.ANIM) 에 쓴다 — 장면 파일(video/episodes/<영상ID>/index.html)은 이 값만 그린다 (숫자를 손으로 적지 않음).
"""python3 stock/source/tteoreojimyeon-sagi-2026-10/backtest/anim_data.py   →  backtest/anim.js

ANIM (원 단위는 매달 100만 원 기준)
  dates            2000-01 … 2023-06 (총수익 자료 끝까지)
  tri              S&P500 총수익 지수 (2000-01 = 1)
  ath              그 달이 '사상 최고치 다음 달'인지 (0/1) — run.py E4·E8_base 와 같은 at_high
  up12             그 달에 사서 1년 뒤 올랐는지 (0/1, 마지막 12달은 없음)
  t10 / t20        10년 기간 163개의 [시작 달, A/B 비율] — −10% / −20% 기다리기
  t20y             20년 기간 43개의 [시작 달, A/B 비율] — −10%
  race             기간 2개(2000-01 시작 = B가 가장 크게 이긴 때 · 차이가 가운데 값인 때)의 달마다
                   [넣은 돈, A 평가액, B 주식 평가액, B 현금, B가 산 달 0/1]
  rule             규칙 보기용 2018-01 … 2019-06 월평균 가격·그때까지 최고치·최고치의 90%·B 신호
  lump             2008-04 시작 목돈 1억 원: 한 번에 vs 12달 나눠서, 달마다 평가액 (12개, 2008-04 … 2009-03)
  dd               월평균 가격의 그때까지 최고치 대비 하락 폭 (2000-01 …, 큰 하락 장면 어둡게)
  cost10           10년 163개의 [시작 달, B 평균 산 값 ÷ A 평균 산 값] (1 아래 = B가 싸게 삼)
  l12 / l120       목돈 12달·10년 [시작 달, 한 번에 ÷ 12달 나눠서], l12 에 사상 최고치 다음 달 표시 [시작, 비, 0/1]
  num              대본이 말하는 숫자 (results.json 키 그대로 — 장면은 이 값으로만 숫자를 쓴다)
연구·교육용 — 투자 권유 아님.
"""
import json
import logging
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / "tools"))
from backtest import data as bd  # noqa: E402
from backtest import monthly as bm  # noqa: E402

VERSION = "v1.1"
C = 1_000_000
LOG = logging.getLogger("anim")


def log(stage, **kv):
    LOG.info("[%s] %s %s", stage, time.strftime("%Y-%m-%dT%H:%M:%S"), " ".join(f"{k}={v}" for k, v in kv.items()))


def main():
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    df, meta = bd.sp500_monthly()
    full = df.loc[:pd.Timestamp(meta["complete_until"])]
    idx, price = full.index, full["price"].to_numpy()
    tri = bm.total_return_index(price, full["dividend"].to_numpy())
    cash = bm.cash_index(len(tri))
    f = int(idx.searchsorted(pd.Timestamp("2000-01-01")))
    lab = lambda i: idx[i].strftime("%Y-%m")
    out = {"version": VERSION, "data_sha256": meta["sha256"][:12], "complete_until": meta["complete_until"][:7]}
    out["dates"] = [lab(i) for i in range(f, len(tri))]
    out["tri"] = [round(float(tri[i] / tri[f]), 5) for i in range(f, len(tri))]
    high = bm.at_high(price)
    out["ath"] = [int(high[i]) for i in range(f, len(tri))]
    fwd = bm.forward_return(tri, 12)
    out["up12"] = [int(fwd[i] > 0) for i in range(f, len(tri)) if not np.isnan(fwd[i])]

    def tourn(drop, horizon):
        s, e = bm.windows(len(tri), horizon, first=f)
        dca = bm.dca_wealth(tri, s, e)
        dip = bm.dip_wealth(tri, cash, bm.next_true(bm.dip_signal(price, drop)), s, e)["wealth"]
        return [[lab(a), round(float(x / y), 4)] for a, x, y in zip(s, dca, dip)]
    out["t10"], out["t20"], out["t20y"] = tourn(0.10, 120), tourn(0.20, 120), tourn(0.10, 240)

    sig10 = bm.dip_signal(price, 0.10)

    def race(start):
        s = int(idx.searchsorted(pd.Timestamp(start)))
        e = s + 119
        rows, units_a, units_b, cash_b = [], 0.0, 0.0, 0.0
        for t in range(s, e + 1):                 # 한 달씩 실제로 사고 모으기 (bm.naive_* 와 같은 계산)
            units_a += 1.0 / tri[t]
            cash_b += 1.0
            bought = bool(sig10[t])
            if bought:
                units_b += cash_b / tri[t]
                cash_b = 0.0
            rows.append([round((t - s + 1) * C), round(units_a * tri[t] * C), round(units_b * tri[t] * C), round(cash_b * C), int(bought)])
        a_end, b_end = rows[-1][1], rows[-1][2] + rows[-1][3]
        chk = bm.dip_trades(tri, cash, sig10, s, e)
        assert abs(chk["wealth"] * C - b_end) < 1, "race 와 dip_trades 가 다름"
        log("RACE", start=start, end=lab(e), a_end=a_end, b_end=b_end, buys=sum(r[4] for r in rows))
        return {"start": start, "end": lab(e), "rows": rows, "a_end": a_end, "b_end": b_end}
    s10, e10 = bm.windows(len(tri), 120, first=f)
    dca10 = bm.dca_wealth(tri, s10, e10)
    dip10 = bm.dip_wealth(tri, cash, bm.next_true(sig10), s10, e10)["wealth"]
    gaps = dca10 - dip10
    med = lab(s10[int(np.argmin(np.abs(gaps - np.median(gaps))))])
    out["race"] = {"best_b": race("2000-01"), "median": race(med)}

    r0, r1 = int(idx.searchsorted(pd.Timestamp("2018-01-01"))), int(idx.searchsorted(pd.Timestamp("2019-06-01")))
    peak = bm.prior_peak(price)
    out["rule"] = [[lab(i), round(float(price[i]), 1), round(float(max(peak[i], price[i - 1])), 1), int(sig10[i])] for i in range(r0, r1 + 1)]

    ls = int(idx.searchsorted(pd.Timestamp("2008-04-01")))
    lump = [round(100_000_000 * tri[ls + k] / tri[ls]) for k in range(12)]   # 12달 = lump_vs_split(k=12) 의 끝 달 s+11
    split = []
    for k in range(12):                          # 1/12 씩 k 달까지 산 주식 + 아직 안 넣은 현금 (이자 0)
        units = sum((1 / 12) / tri[ls + j] for j in range(min(k + 1, 12)))
        left = max(0, 12 - (k + 1)) / 12
        split.append(round(100_000_000 * (units * tri[ls + k] + left)))
    out["lump"] = {"start": "2008-04", "lump": lump, "split": split}
    log("LUMP", lump_end=lump[-1], split_end=split[-1])

    runmax = np.maximum.accumulate(price)
    out["dd"] = [round(float(price[i] / runmax[i] - 1), 3) for i in range(f, len(tri))]
    s10b, e10b = bm.windows(len(tri), 120, first=f)
    out["cost10"] = [[lab(a), round(float(bm.dip_trades(tri, cash, sig10, a, b)["avg_cost"] / bm.dca_avg_cost(tri, a, b)), 4)]
                     for a, b in zip(s10b, e10b)]
    s12, e12 = bm.windows(len(tri), 12, first=f)
    lp, sp = bm.lump_vs_split(tri, cash, s12, e12)
    out["l12"] = [[lab(a), round(float(x / y), 4), int(high[a])] for a, x, y in zip(s12, lp, sp)]
    s120, e120 = bm.windows(len(tri), 120, first=f)
    lp1, sp1 = bm.lump_vs_split(tri, cash, s120, e120)
    out["l120"] = [[lab(a), round(float(x / y), 4)] for a, x, y in zip(s120, lp1, sp1)]

    R = json.loads((HERE / "results.json").read_text("utf-8"))
    res = R["results"]   # 같은 값인지 결과 파일과 맞춰 봄
    E1, E8, E3, E4, E7 = res["E1"], res["E8"], res["E3"], res["E4"], res["E7"]
    m10, m20 = E1["main_10y"], E1["main_20y"]
    e1p = next(v for k, v in res["E1p"].items() if k.startswith("main_10y"))
    e1d = next(v for k, v in res["E1d"].items() if k.startswith("main_10y"))
    l12r, l120r, lhr = E3["main_12m_all_cash0"], E3["main_120m_all_cash0"], E3["main_12m_after_high_cash0"]
    out["num"] = {
        "first": R["params"]["main_start"][:7], "end": R["data"]["complete_until"][:7], "price_last": R["data"]["last"][:7],
        "windows10": m10["windows"], "a10": m10["drop10_cash0"]["dca_wins"], "b10": E8["drop10_monthly"]["b_wins"],
        "last_start10": m10["last_start"], "contributed10": m10["contributed_krw"], "monthly": C,
        "b_max10": E8["drop10_monthly"]["b_max_ratio"], "a_max10": E8["drop10_monthly"]["a_max_ratio"],
        "b_win_starts10": E8["drop10_monthly"]["b_win_starts"], "a_win_first10": E8["drop10_monthly"]["a_win_first_start"],
        "a_median10_krw": m10["dca_median_krw"], "gap_median10_krw": m10["drop10_cash0"]["median_gap_krw"],
        "first_dip_krw": E7["first"]["dip_krw"], "first_dca_krw": E7["first"]["dca_krw"], "first_gap_krw": E7["first"]["gap_krw"],
        "windows20y": m20["windows"], "a20y": m20["drop10_cash0"]["dca_wins"], "contributed20y": m20["contributed_krw"],
        "gap_median20y_krw": m20["drop10_cash0"]["median_gap_krw"],
        "a10_cash_rate": m10["drop10_cashRate"]["dca_wins"], "a10_drop5": m10["drop5_cash0"]["dca_wins"],
        "a10_daily": e1d["drop10_cash0"]["dca_wins"], "daily_from": "2016-03",
        "fwd12_months": res["E8_base"]["fwd12_months"], "fwd12_up": res["E8_base"]["fwd12_up"],
        "wait_months_median": E7["avg_wait_months_median"], "cost_ratio_median": E7["avg_cost_ratio_median"],
        "cost_higher_windows": E7["dip_avg_cost_higher_windows"],
        "a20": E8["drop20_monthly"]["a_wins"], "b20": E8["drop20_monthly"]["b_wins"], "b_max20": E8["drop20_monthly"]["b_max_ratio"],
        "a_max20": E8["drop20_monthly"]["a_max_ratio"], "b_win_starts20": E8["drop20_monthly"]["b_win_starts"],
        "a_win_first20": E8["drop20_monthly"]["a_win_first_start"],
        "main_months": res["E8_base"]["main_months"], "after_high_months": res["E8_base"]["after_high_months"],
        "e4_60_high": E4["main_60m"]["high_median_annual"], "e4_60_all": E4["main_60m"]["all_median_annual"],
        "e4_12_high": E4["main_12m"]["high_median_annual"], "e4_12_all": E4["main_12m"]["all_median_annual"],
        "l12_windows": l12r["windows"], "l12_wins": l12r["lump_wins"], "l12_ratio_median": l12r["ratio_median"],
        "l120_windows": l120r["windows"], "l120_wins": l120r["lump_wins"], "lh_windows": lhr["windows"], "lh_wins": lhr["lump_wins"],
        "lump_worst_start": l12r["lump_worst_start"], "lump_worst": l12r["lump_worst"], "split_at_lump_worst": l12r["split_at_lump_worst"],
        "p_windows10": e1p["windows"], "p_a10": e1p["drop10_cash0"]["dca_wins"],
    }
    assert sum(1 for _, r in out["t10"] if r > 1) == res["E1"]["main_10y"]["drop10_cash0"]["dca_wins"]
    assert sum(1 for _, r in out["t20"] if r > 1) == res["E1"]["main_10y"]["drop20_cash0"]["dca_wins"]
    assert sum(out["up12"]) == res["E8_base"]["fwd12_up"] and sum(out["ath"]) == res["E8_base"]["after_high_months"]
    assert abs(out["race"]["best_b"]["b_end"] - res["E7"]["first"]["dip_krw"]) <= 1
    assert abs(out["lump"]["lump"][11] / 1e8 - res["E3"]["main_12m_all_cash0"]["lump_worst"]) < 1e-4
    assert abs(out["lump"]["split"][11] / 1e8 - res["E3"]["main_12m_all_cash0"]["split_at_lump_worst"]) < 1e-4
    n = out["num"]
    assert sum(1 for _, r in out["t20"] if r < 1) == n["b20"] and sum(1 for _, r in out["t20y"] if r > 1) == n["a20y"] == len(out["t20y"])
    assert sum(1 for _, r in out["cost10"] if r > 1) == n["cost_higher_windows"]
    assert abs(float(np.median([r for _, r in out["cost10"]])) - n["cost_ratio_median"]) < 1e-3
    assert sum(1 for _, r, _h in out["l12"] if r > 1) == n["l12_wins"] and len(out["l12"]) == n["l12_windows"]
    assert sum(1 for _, r in out["l120"] if r > 1) == n["l120_wins"] and len(out["l120"]) == n["l120_windows"]
    hl = [r for _, r, h in out["l12"] if h]
    assert len(hl) == n["lh_windows"] and sum(1 for r in hl if r > 1) == n["lh_wins"]
    assert abs(max(r for _, r in out["t10"]) - n["a_max10"]) < 1e-3 and abs(1 / min(r for _, r in out["t10"]) - n["b_max10"]) < 1e-3
    assert abs(out["race"]["median"]["a_end"] - out["race"]["median"]["b_end"] - n["gap_median10_krw"]) <= 1
    log("NUM", keys=len(n), a10=n["a10"], b10=n["b10"], a20=n["a20"], b20=n["b20"], cost_median=n["cost_ratio_median"], wait=n["wait_months_median"])
    (HERE / "anim.js").write_text("// 자동 생성 — backtest/anim_data.py " + VERSION + " (손으로 고치지 않음)\nwindow.ANIM=" +
                                  json.dumps(out, ensure_ascii=False, separators=(",", ":")) + ";\n", "utf-8")
    log("DONE", file=HERE / "anim.js", months=len(out["dates"]), t10=len(out["t10"]), median_window=med)


if __name__ == "__main__":
    main()
