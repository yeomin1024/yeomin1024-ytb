#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.2 — 2026-11-09 — 반론 검토 1차 숫자: 약세 8,000 vs 6/25 종가 · 1만 전망 날(5/11) vs 2024년 말 배수 · 2022 전망 밴드 하단 2,610 vs 실제 (사용자 지시 "…만스피 대본에도 모두 반영 … 페르소나 검증도 해").
# (v1.1 — 2026-11-08 — 2026 연간 전망 밴드(2025년 말 7곳 3,500~5,500) vs 실제 고점 · 코스피 30% 넘는 하락 국면과 회복 기간 (대본 분량 보완).)
# (v1.0 — 2026-11-08 — 롱폼 「만스피 간다는 전문가들 왜 이럴까? 절대 믿지 마세요」 숫자 (사용자 지시 2026-11-08 — 전달 내용 "믿어도 되는 말과 절대 믿지 말아야 할 전문가 말").
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.2 | 2026-11-09 | CITED kospi_2022_band [2610, 3600] · bear_vs_report_day_pct · fn_10000 vs_2024_end_x · kospi_2022.vs_band_low_pct (기존 값 그대로) | main |
# | v1.1 | 2026-11-08 | cited band_2026_top 5,500 → 고점 대비 · drawdowns(고점 −30% 넘는 국면 · 바닥 · 고점 되찾은 날 · 해) | drawdowns · main |
# | v1.0 | 2026-11-08 | 최초 — 2026 코스피 길(8,000 첫 돌파 · 고점 · 지금) · 전망이 나온 날 1억 원 · 2022 전망 3,600 vs 실제 · 월가 2022·2023 평균 전망 vs 실제 | load · main |
#
# 자료: 코스피 ^KS11 · S&P 500 ^GSPC 일별 종가 (Yahoo Finance chart API v8, 2026-11-08 받음 — calc/kospi.csv · spx.csv). 가격 지수(배당 없음).
# 인용 숫자(계산하지 않음 — 출처는 upload.md): 2026-05 증권사 목표 1만 이상 · 2026-06-25 한 외국계 1만 2,500(기본)·1만 5,000(강세)·8,000(약세) ·
#   2022 전망 상단 3,600 · 월가 2022 평균 4,975 · 2023 평균 4,083 · 매도 의견 0.1%(2025 상반기 20대 증권사) · 목표주가 달성률 19%(2000~2024, 74만 건).
# 판단 = 그날 종가. 금액 = 1억 원 × 지수 변화율 (세금·수수료 없음). ※ 연구·교육용 — 투자 권유 아님.
from __future__ import annotations

import json
import logging
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

VERSION = "v1.2"
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUT = HERE / "result.json"
CITED = {"kospi_2022_top_target": 3600, "kospi_2022_band": [2610, 3600], "band_2026_made_2025_12": [3500, 5500], "spx_2022_avg_target": 4975, "spx_2023_avg_target": 4083,
         "jpm_2026_06_25": {"base": 12500, "bull": 15000, "bear": 8000}, "kb_2026_05": 10500}
DATES = {"fn_10000_report": "2026-05-11", "jpm_15000_report": "2026-06-25"}

logging.basicConfig(level=logging.INFO, format="%(message)s", stream=sys.stdout)
def log(stage: str, **kv) -> None:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    logging.info(f"[{stage}] [{ts}] " + " ".join(f"{k}={v}" for k, v in kv.items()))


def load(name: str) -> pd.Series:
    p = HERE / name
    try:
        s = pd.read_csv(p, comment="#", parse_dates=["date"]).set_index("date")["close"].astype(float)
    except Exception as e:  # noqa: BLE001
        log("FAIL", stage="data", file=p, err=repr(e), next="Yahoo chart API 로 다시 받기 (파일 머리 주석)")
        raise
    s = s[~s.index.duplicated(keep="last")]
    log("DATA", source=name, rows=len(s), first=s.index[0].date(), last=s.index[-1].date(), na=int(s.isna().sum()), nonpositive=int((s <= 0).sum()),
        gaps_over_7d=int((s.index.to_series().diff().dt.days > 7).sum()))
    if s.isna().any() or (s <= 0).any():
        raise SystemExit(f"{name} 자료 이상 — 빈 값·0 이하")
    return s


def at(s: pd.Series, d: str) -> tuple[str, float]:
    """그날 종가 (휴장이면 그 전 거래일)."""
    x = s[:d]
    return x.index[-1].strftime("%Y-%m-%d"), float(x.iloc[-1])


def drawdowns(s: pd.Series, th: float = -0.30) -> tuple[list[dict], dict | None]:
    """고점보다 th 넘게 하락한 국면 — 이전 최고 종가 · 바닥 · 그 최고가를 다시 넘은 날 (자료 첫날 2000-01-04 부터)."""
    out, pk_v, pk_d, tr = [], float(s.iloc[0]), s.index[0], None
    for d, v in s.items():
        if v >= pk_v:
            if tr and tr[1] / pk_v - 1 <= th:
                out.append({"peak": pk_d.strftime("%Y-%m-%d"), "peak_close": round(pk_v, 2), "bottom": tr[0].strftime("%Y-%m-%d"),
                            "drop_pct": pct(tr[1], pk_v), "regained": d.strftime("%Y-%m-%d"), "years": round((d - pk_d).days / 365.25, 1)})
            pk_v, pk_d, tr = float(v), d, None
        elif tr is None or v < tr[1]:
            tr = (d, float(v))
    open_ = {"peak": pk_d.strftime("%Y-%m-%d"), "peak_close": round(pk_v, 2), "low": tr[0].strftime("%Y-%m-%d"), "drop_pct": pct(tr[1], pk_v)} if tr else None
    return out, open_


def pct(a: float, b: float) -> float:
    return round((a / b - 1) * 100, 1)


def main() -> None:
    t0 = time.perf_counter()
    k, sp = load("kospi.csv"), load("spx.csv")
    last_d, last = k.index[-1].strftime("%Y-%m-%d"), float(k.iloc[-1])
    y26 = k["2026-01-01":]
    pk_d, pk = y26.idxmax().strftime("%Y-%m-%d"), float(y26.max())
    first8k = y26[y26 >= 8000].index[0].strftime("%Y-%m-%d")
    e24, e25 = at(k, "2024-12-31"), at(k, "2025-12-31")
    res = {"version": VERSION, "made": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "cited": CITED,
           "kospi": {"end_2024": e24, "end_2025": e25, "rise_2025_pct": pct(e25[1], e24[1]), "first_close_8000": first8k,
                     "peak_2026": [pk_d, round(pk, 2)], "last": [last_d, round(last, 2)], "from_peak_pct": pct(last, pk),
                     "peak_vs_2024_end_x": round(pk / e24[1], 2), "last_vs_peak_won_1e8": int(round(1e8 * last / pk, -4))}}
    for key, d in DATES.items():
        dd, v = at(k, d)
        res["kospi"][key] = {"date": dd, "close": round(v, 2), "to_last_pct": pct(last, v), "won_1e8_now": int(round(1e8 * last / v, -4)),
                             "loss_won": int(round(1e8 * (last / v - 1), -4)), "max_after": round(float(k[dd:].max()), 2)}
    res["kospi"]["peak_vs_band_2026_top_pct"] = pct(pk, CITED["band_2026_made_2025_12"][1])
    dds, open_ = drawdowns(k)
    res["drawdowns_30"] = {"done": dds, "open": open_, "n_done": len(dds), "years_min": min(d["years"] for d in dds), "years_max": max(d["years"] for d in dds)}
    for d in dds:
        log("DRAWDOWN", **d)
    log("DRAWDOWN", open=json.dumps(open_), n_done=len(dds))
    j = CITED["jpm_2026_06_25"]
    res["kospi"]["jpm_vs_last"] = {"bear_8000_vs_last_pct": pct(last, j["bear"]), "below_bear": last < j["bear"],
                                   "bear_vs_report_day_pct": pct(j["bear"], res["kospi"]["jpm_15000_report"]["close"])}   # 약세 8,000 이 그날 종가보다 몇 % 아래였나
    res["kospi"]["fn_10000_report"]["vs_2024_end_x"] = round(res["kospi"]["fn_10000_report"]["close"] / e24[1], 2)   # 1만 전망 날 = 2024년 말의 몇 배
    # 2022 — 전망 상단 3,600 vs 실제
    e21, e22 = at(k, "2021-12-31"), at(k, "2022-12-31")
    res["kospi_2022"] = {"end_2021": e21, "end_2022": e22, "year_pct": pct(e22[1], e21[1]), "vs_top_target_pct": pct(e22[1], CITED["kospi_2022_top_target"]), "vs_band_low_pct": pct(e22[1], CITED["kospi_2022_band"][0]),
                         "max_2022": round(float(k["2022"].max()), 2)}
    # 월가 — 평균 전망 vs 실제
    s21, s22, s23 = at(sp, "2021-12-31"), at(sp, "2022-12-31"), at(sp, "2023-12-31")
    res["spx"] = {"end_2021": s21, "end_2022": s22, "end_2023": s23,
                  "miss_2022_pct": pct(s22[1], CITED["spx_2022_avg_target"]), "miss_2023_pct": pct(s23[1], CITED["spx_2023_avg_target"]),
                  "year_2022_pct": pct(s22[1], s21[1]), "year_2023_pct": pct(s23[1], s22[1])}
    for sec in ("kospi", "kospi_2022", "spx"):
        log("RESULT", section=sec, **{a: (json.dumps(b, ensure_ascii=False) if isinstance(b, (dict, list, tuple)) else b) for a, b in res[sec].items()})
    OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    log("DONE", out=OUT.relative_to(ROOT), sec=round(time.perf_counter() - t0, 2))


if __name__ == "__main__":
    main()
