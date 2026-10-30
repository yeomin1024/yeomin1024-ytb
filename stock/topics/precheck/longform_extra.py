#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-30 — 최초. 쇼츠·롱폼 요약본(사용자 지시 2026-10-30 "… 쇼츠 내용과 연결되는 구체적인 내용들을 롱폼 요약본으로 작성해봐 …
#          롱폼도 반전이나 의외의 사실, 예상치 못한 사실, 반론에 등등 …")의 반론 장에 쓸 숫자 세 가지:
#   A. 밤사이만·장중만 들고 있기에 매매 비용을 넣으면 (SPY 시가·종가 2000~2026, 가격만 — round4.py overnight 와 같은 계산 + 비용)
#   B. 하락장 4번 — 11개 업종(그때 있던 업종)에 미리 똑같이 나눠 담았다면 고점 → 바닥 (round4.py sector_bear 와 같은 날짜 · 업종 ETF 배당 포함)
#   C. 반론 '그래도 기술주가 제일 많이 올랐다' — 기술 업종만 vs 9개 업종 똑같이(처음에 나눠 담고 그대로) vs S&P 500, 5년 · 매달 시작 · 안정 수익 확률
#      (안정 = 끝에 국채보다 더 + 원금보다 20% 넘게 준 적 없음 — risk.py stable 과 같은 뜻)
# 자료: precheck/data/SPY_oc.csv · XL*.csv (adjclose) · stock/source/timing-test-2026-10/calc/sp500tr_daily.csv · irx_daily.csv — 새로 받지 않음.
# 실행: python3 -B stock/topics/precheck/longform_extra.py → precheck/longform_extra_<날짜>.json
# ※ 연구·교육용 — 투자 권유가 아님.
import bisect
import csv
import json
import logging
from datetime import date
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
CALC = HERE.parent.parent / "source" / "timing-test-2026-10" / "calc"
VERSION = "v1.0"
COSTS = (0.0, 0.0001, 0.0005, 0.001)      # 매매 한 번(매수 또는 매도)마다 비용 몫 — 0 · 0.01% · 0.05% · 0.1%
SECTORS = {"XLB": "소재", "XLE": "에너지", "XLF": "금융", "XLI": "산업재", "XLK": "기술", "XLP": "필수소비재", "XLU": "유틸리티", "XLV": "헬스케어", "XLY": "임의소비재",
           "XLC": "통신서비스", "XLRE": "부동산"}
NINE = ["XLB", "XLE", "XLF", "XLI", "XLK", "XLP", "XLU", "XLV", "XLY"]     # 1998-12 부터 있는 9개 — C 의 긴 구간용
BEARS = [("2007-10-09", "2009-03-09", "금융위기"), ("2020-02-19", "2020-03-23", "코로나"), ("2022-01-03", "2022-10-12", "2022 금리 인상"), ("2025-02-19", "2025-04-08", "2025 관세")]
logging.basicConfig(level=logging.INFO, format="[%(stage)s] %(message)s")
log = logging.getLogger("longform_extra")


def _rows(path):
    with path.open(encoding="utf-8") as f:
        rows = [r for r in csv.reader(f) if r and not r[0].startswith("#")]
    return rows[0], rows[1:]


def load_calc(name):
    _, rows = _rows(CALC / name)
    out = [(r[0], float(r[1])) for r in rows if r[1]]
    log.info("source=%s rows=%d range=%s~%s", name, len(out), out[0][0], out[-1][0], extra={"stage": "LOAD"})
    return out


def load_adj(sym):
    head, rows = _rows(DATA / f"{sym}.csv")
    k = head.index("adjclose")
    out = {r[0]: float(r[k]) for r in rows if len(r) > k and r[k]}
    return out


def overnight_costs():
    head, rows = _rows(DATA / "SPY_oc.csv")
    ds = [r[0] for r in rows]
    op = np.array([float(r[1]) for r in rows])
    cl = np.array([float(r[2]) for r in rows])
    intra = cl / op
    night = np.concatenate([[1.0], op[1:] / cl[:-1]])
    m = np.array([2000 <= int(x[:4]) <= 2026 for x in ds])
    n = int(m.sum())
    out = {"period": f"{ds[int(np.argmax(m))]} ~ {ds[-1]}", "days": n, "trades_each": 2 * n, "hold_price_only_10k": round(10000 * float(np.prod(intra[m] * night[m]))), "by_cost": {}}
    for c in COSTS:
        f = (1 - c) ** 2                       # 하루에 한 번 사고 한 번 팖
        out["by_cost"][f"{c * 100:.2f}%"] = {"장중만_10k": round(10000 * float(np.prod(intra[m] * f))), "밤사이만_10k": round(10000 * float(np.prod(night[m] * f)))}
        log.info("cost=%.2f%% intraday=%s overnight=%s hold=%s days=%d", c * 100, out["by_cost"][f"{c * 100:.2f}%"]["장중만_10k"],
                 out["by_cost"][f"{c * 100:.2f}%"]["밤사이만_10k"], out["hold_price_only_10k"], n, extra={"stage": "A_NIGHT"})
    return out


def on_dates(ds, series):
    """series(날짜 → 값)를 ds 날짜에 맞춤 — 그날 값이 없으면 앞날 값 (앞날도 없으면 nan)."""
    keys = sorted(series)
    out = np.full(len(ds), np.nan)
    for i, d in enumerate(ds):
        j = bisect.bisect_right(keys, d) - 1
        if j >= 0:
            out[i] = series[keys[j]]
    return out


def main():
    tr = load_calc("sp500tr_daily.csv")
    ir = dict(load_calc("irx_daily.csv"))
    ds = [d for d, _ in tr]
    trv = np.array([v for _, v in tr])
    S = {k: on_dates(ds, load_adj(k)) for k in SECTORS}
    log.info("sectors=%s first=%s", len(S), {k: ds[int(np.argmax(~np.isnan(v)))] for k, v in S.items()}, extra={"stage": "LOAD"})
    # 국채 이자로 불린 현금 (timing_cases.py 와 같은 계산 — 그날 값이 없으면 앞날 값)
    cash = np.ones(len(ds))
    last = None
    for k in range(1, len(ds)):
        last = ir.get(ds[k - 1], last)
        cash[k] = cash[k - 1] * (1 + (last or 0) / 100) ** ((date.fromisoformat(ds[k]) - date.fromisoformat(ds[k - 1])).days / 365)

    A = overnight_costs()

    B = {}
    for a, b, name in BEARS:
        ia, ib = bisect.bisect_left(ds, a), bisect.bisect_left(ds, b)
        have = [k for k in SECTORS if S[k][ia] == S[k][ia]]
        mix = float(np.mean([S[k][ib] / S[k][ia] for k in have]) - 1)
        worst = float(np.min(np.mean([S[k][ia:ib + 1] / S[k][ia] for k in have], axis=0)) - 1)
        B[name] = {"window": f"{a} → {b}", "n_sectors": len(have), "mix_peak_to_trough": f"{mix * 100:+.1f}%", "mix_worst": f"{worst * 100:+.1f}%",
                   "tech": f"{(S['XLK'][ib] / S['XLK'][ia] - 1) * 100:+.1f}%", "sp500": f"{(trv[ib] / trv[ia] - 1) * 100:+.1f}%"}
        log.info("bear=%s n=%d mix=%s tech=%s sp500=%s", name, len(have), B[name]["mix_peak_to_trough"], B[name]["tech"], B[name]["sp500"], extra={"stage": "B_MIX"})

    # C. 5년 · 매달 첫 거래일 시작 · 1999-01 ~ (끝이 자료 안)
    starts = [i for i in range(1, len(ds)) if ds[i][:7] != ds[i - 1][:7] and ds[i] >= "1999-01-01"]
    C = {}
    cells = (("1999~2008 시작", "1999", "2008"), ("2009~2021 시작", "2009", "2021"), ("전체", "1999", "2021"))
    for lab, y0, y1 in cells:
        acc = {"기술만": [], "9개 업종 똑같이": [], "S&P 500": []}
        ends = {"기술만": [], "9개 업종 똑같이": [], "S&P 500": []}
        for s in starts:
            if not (y0 <= ds[s][:4] <= y1):
                continue
            e = bisect.bisect_left(ds, f"{int(ds[s][:4]) + 5:04d}{ds[s][4:]}")
            if e >= len(ds):
                continue
            c = cash[s:e + 1] / cash[s]
            paths = {"기술만": S["XLK"][s:e + 1] / S["XLK"][s], "9개 업종 똑같이": np.mean([S[k][s:e + 1] / S[k][s] for k in NINE], axis=0), "S&P 500": trv[s:e + 1] / trv[s]}
            for k, v in paths.items():
                acc[k].append(bool(v[-1] > c[-1] and np.nanmin(v) >= 0.8))
                ends[k].append(float(v[-1]))
        C[lab] = {k: {"n": len(v), "stable": f"{np.mean(v) * 100:.1f}%", "median_end_10k": round(10000 * float(np.median(ends[k])))} for k, v in acc.items()}
        log.info("cell=%s %s", lab, json.dumps(C[lab], ensure_ascii=False), extra={"stage": "C_STABLE"})

    out = HERE / f"longform_extra_{date.today().isoformat()}.json"
    out.write_text(json.dumps({"tool": f"longform_extra.py {VERSION}", "A_overnight_costs": A, "B_sector_mix_bears": B,
                               "C_tech_vs_mix_5y": {"rule": "5년 · 매달 첫 거래일 시작 · 안정 = 끝에 국채보다 더 + 원금 20% 넘게 준 적 없음 · 9개 업종 = 처음에 똑같이 나눠 담고 그대로(다시 맞추지 않음)",
                                                    "cells": C}}, ensure_ascii=False, indent=1), "utf-8")
    log.info("file=%s", out.name, extra={"stage": "DONE"})


if __name__ == "__main__":
    main()
