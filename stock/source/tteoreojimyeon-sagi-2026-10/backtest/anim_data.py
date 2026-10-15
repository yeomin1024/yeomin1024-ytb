#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-15 — 영상 애니메이션 자료 (사용자 지시 2026-10-15 "날짜가 지남에 따라 백테스트 수치를 실시간 비교하는 과정을
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

VERSION = "v1.0"
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

    res = json.loads((HERE / "results.json").read_text("utf-8"))["results"]   # 같은 값인지 결과 파일과 맞춰 봄
    assert sum(1 for _, r in out["t10"] if r > 1) == res["E1"]["main_10y"]["drop10_cash0"]["dca_wins"]
    assert sum(1 for _, r in out["t20"] if r > 1) == res["E1"]["main_10y"]["drop20_cash0"]["dca_wins"]
    assert sum(out["up12"]) == res["E8_base"]["fwd12_up"] and sum(out["ath"]) == res["E8_base"]["after_high_months"]
    assert abs(out["race"]["best_b"]["b_end"] - res["E7"]["first"]["dip_krw"]) <= 1
    assert abs(out["lump"]["lump"][11] / 1e8 - res["E3"]["main_12m_all_cash0"]["lump_worst"]) < 1e-4
    assert abs(out["lump"]["split"][11] / 1e8 - res["E3"]["main_12m_all_cash0"]["split_at_lump_worst"]) < 1e-4
    (HERE / "anim.js").write_text("// 자동 생성 — backtest/anim_data.py " + VERSION + " (손으로 고치지 않음)\nwindow.ANIM=" +
                                  json.dumps(out, ensure_ascii=False, separators=(",", ":")) + ";\n", "utf-8")
    log("DONE", file=HERE / "anim.js", months=len(out["dates"]), t10=len(out["t10"]), median_window=med)


if __name__ == "__main__":
    main()
