#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-11-11 — 새로: 대본 v6(아예 새로 씀 — '폭락 뒤 반등, 진짜인지 또 떨어질지 불안'을 미국 증시의 지난 기록으로 풀어 줌)에 쓰는 역사 숫자.
#   사용자 지시 2026-11-11 "이거 대본을 아예 새로 쓰자 페르소나 활용해서 쓰고 시청자의 생각은 폭락 후 반등했는데 이게 진짜로 반등하는건지 또 떨어질려고 하는건지 불안하다는거야
#   이걸 미국 주식 시장의 역사라는 정해져 있는 사실들을 근거로 해소로 해야돼".
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.0 | 2026-11-11 | 최초 | declines·rebound_days·after_low·best_days·time_under·main |
#
# 자료: SPY 일별 수정 종가(배당 포함) — calc.py load() 와 같은 파일(stock/topics/precheck/data/SPY.csv, 1999-01-04 ~ 2026-10-28). 2000년 이후만 셈
#       (사례·자료는 2000년대부터 — CLAUDE.md '1900년대 사건·자료는 쓰지 않음'. 1999년 값은 2000년 첫 해의 '1년 최고가'를 구하는 데만).
# 규칙 (판단 = 그날 종가까지 · 앞날 자료 안 씀):
#   큰 하락 = 종가가 252거래일(1년) 최고가보다 TH(15%) 넘게 낮아진 구간 — 최고가 날 → 그 값을 되찾기 전 가장 낮은 날(바닥) → 되찾은 첫날. 민감도 10·20%.
#   급반등 날 = 전날 종가가 1년 최고가보다 10% 넘게 낮은 상태에서 하루 +3% 넘게 오른 날 (calc.py events 와 같은 조건 · 가까운 날도 모두 셈).
#     가짜 = 그 뒤 126거래일(약 6개월) 안에 종가가 '급반등 전 20거래일의 가장 낮은 종가' 아래로 내려감 (longform.py 의 '실제'와 같은 정의).
#   바닥 뒤 = 바닥 날 종가 대비 21·63·126·252거래일 뒤 값 · 종가가 200일 이동평균선 위로 처음 올라선 날(흔히 말하는 '추세 확인')까지 이미 오른 폭.
#   가장 크게 오른 날 = 2000년 이후 하루 상승률 상위 20일 — 그 전날 종가가 1년 최고가보다 10%·20% 넘게 낮았던 날이 몇 번인가.
# 출력: calc/history_result.json (+ longform_result.json 의 final_v5 숫자를 그대로 옮겨 한곳에서 대조). ※ 연구·교육용 — 투자 권유 아님. 세금·수수료·환율 없음.
#       과거 기록이며 앞으로도 같다는 보장은 없음. 지수(SPY)의 기록 — 개별 종목·다른 나라 시장에는 그대로 맞지 않음.
from __future__ import annotations

import json
import logging
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import calc as C  # noqa: E402  (같은 자료·같은 사건 정의)

VERSION = "v1.0"
OUT = HERE / "history_result.json"
START = "2000-01-01"


def log(stage: str, **kv) -> None:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    logging.info(f"[{stage}] [{ts}] " + " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, (dict, list)) else v}" for k, v in kv.items()))


def d(I, i: int) -> str:
    return I[i].strftime("%Y-%m-%d")


def declines(P: np.ndarray, I, th: float) -> list[dict]:
    """1년 최고가보다 th 넘게 낮아진 구간. (최고가 날 pk · 바닥 lo · 되찾은 날 j — 아직이면 None)"""
    hi = pd.Series(P).rolling(252, min_periods=1).max().values
    out, i = [], 0
    while i < len(P):
        if I[i] >= pd.Timestamp(START) and P[i] / hi[i] - 1 <= -th:
            a = max(0, i - 251)
            pk = a + int(np.argmax(P[a:i + 1]))
            j = i
            while j < len(P) and P[j] < P[pk]:
                j += 1
            lo = pk + int(np.argmin(P[pk:j]))
            out.append({"pk": pk, "lo": lo, "rec": j if j < len(P) else None})
            i = j
        else:
            i += 1
    return out


def rebound_days(P: np.ndarray, I, th: float = 0.03, dd: float = 0.10, fut: int = 126, bottom_n: int = 20) -> list[dict]:
    rows = []
    for t in range(252, len(P)):
        if I[t] < pd.Timestamp(START):
            continue
        prev_hi = P[t - 252:t].max()
        if P[t - 1] / prev_hi - 1 <= -dd and P[t] / P[t - 1] - 1 >= th:
            bottom = P[t - bottom_n:t].min()
            w = P[t + 1:t + 1 + fut]
            brk = next((k for k, v in enumerate(w) if v < bottom), None)
            kind = "가짜" if brk is not None else ("진짜" if t + fut < len(P) else "진행 중")
            rows.append({"t": t, "date": d(I, t), "day": round(float(P[t] / P[t - 1] - 1) * 100, 1), "kind": kind, "days_to_break": (brk + 1) if brk is not None else None,
                         "more_drop": round(float(w.min() / P[t] - 1) * 100, 1) if len(w) else None})
    return rows


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(message)s", stream=sys.stdout)
    t0 = time.perf_counter()
    spy, _ = C.load()
    P, I = spy.values, spy.index
    log("LOAD", rows=len(P), first=d(I, 0), last=d(I, len(P) - 1), counted_from=START)
    ma200 = pd.Series(P).rolling(200).mean().values

    # 1. 급반등 날 — 모두
    R = rebound_days(P, I)
    known = [r for r in R if r["kind"] != "진행 중"]
    fake = [r for r in known if r["kind"] == "가짜"]
    reb = {"n": len(R), "decided": len(known), "fake": len(fake), "real": len(known) - len(fake), "fake_share": round(len(fake) / len(known), 3),
           "days_to_break_median": int(np.median([r["days_to_break"] for r in fake])), "more_drop_median": round(float(np.median([r["more_drop"] for r in known])), 1)}
    log("REBOUND", **reb)
    sens = {}
    for th in (0.03, 0.04, 0.05):
        for dd_ in (0.10, 0.20):
            x = [r for r in rebound_days(P, I, th, dd_) if r["kind"] != "진행 중"]
            sens[f"th{int(th * 100)}_dd{int(dd_ * 100)}"] = {"n": len(x), "fake": sum(r["kind"] == "가짜" for r in x), "fake_share": round(sum(r["kind"] == "가짜" for r in x) / len(x), 3)}
    log("REBOUND_SENS", **sens)

    # 2. 큰 하락 — 바닥까지 · 그 사이 급반등 · 되찾기까지 · 바닥 뒤
    def table(th: float) -> list[dict]:
        rows = []
        for e in declines(P, I, th):
            pk, lo, rec = e["pk"], e["lo"], e["rec"]
            before = [r for r in R if pk < r["t"] < lo]
            f = lambda h: round(float(P[lo + h] / P[lo] - 1) * 100, 1) if lo + h < len(P) else None   # noqa: E731
            up200 = next((k for k in range(lo + 1, len(P)) if not np.isnan(ma200[k]) and P[k] > ma200[k]), None)
            rows.append({"peak": d(I, pk), "low": d(I, lo), "depth": round(float(P[lo] / P[pk] - 1) * 100, 1), "months_to_low": round((I[lo] - I[pk]).days / 30.44, 1),
                         "rebounds_before_low": len(before), "biggest_rebound_before_low": max((r["day"] for r in before), default=None),
                         "recovered": d(I, rec) if rec is not None else None, "years_peak_to_recover": round((I[rec] - I[pk]).days / 365.25, 1) if rec is not None else None,
                         "years_low_to_recover": round((I[rec] - I[lo]).days / 365.25, 1) if rec is not None else None,
                         "after_low_1m": f(21), "after_low_3m": f(63), "after_low_6m": f(126), "after_low_1y": f(252),
                         "above_ma200_date": d(I, up200) if up200 is not None else None, "gain_from_low_at_ma200": round(float(P[up200] / P[lo] - 1) * 100, 1) if up200 is not None else None,
                         "days_low_to_ma200": (up200 - lo) if up200 is not None else None})
        return rows
    T = table(0.15)
    for r in T:
        log("DECLINE", **{k: v for k, v in r.items() if v is not None})
    done = [r for r in T if r["recovered"]]
    med = lambda k, rows=T: round(float(np.median([r[k] for r in rows if r[k] is not None])), 1)   # noqa: E731
    summ = {"th": 0.15, "n": len(T), "recovered": len(done), "years_peak_to_recover_min": min(r["years_peak_to_recover"] for r in done),
            "years_peak_to_recover_max": max(r["years_peak_to_recover"] for r in done), "years_peak_to_recover_median": med("years_peak_to_recover", done),
            "within_1y": sum(1 for r in done if r["years_peak_to_recover"] <= 1.0), "within_2y": sum(1 for r in done if r["years_peak_to_recover"] <= 2.0),
            "rebounds_before_low_total": sum(r["rebounds_before_low"] for r in T), "declines_with_rebound_before_low": sum(1 for r in T if r["rebounds_before_low"] > 0),
            "after_low_1m_median": med("after_low_1m"), "after_low_1m_min": min(r["after_low_1m"] for r in T if r["after_low_1m"] is not None),
            "after_low_3m_median": med("after_low_3m"), "after_low_1y_median": med("after_low_1y"), "after_low_1y_min": min(r["after_low_1y"] for r in T if r["after_low_1y"] is not None),
            "gain_at_ma200_median": med("gain_from_low_at_ma200"), "gain_at_ma200_min": min(r["gain_from_low_at_ma200"] for r in T if r["gain_from_low_at_ma200"] is not None),
            "gain_at_ma200_max": max(r["gain_from_low_at_ma200"] for r in T if r["gain_from_low_at_ma200"] is not None)}
    log("DECLINE_SUM", **summ)
    sens_d = {}
    for th in (0.10, 0.20):
        x = table(th); dn = [r for r in x if r["recovered"]]
        sens_d[f"th{int(th * 100)}"] = {"n": len(x), "recovered": len(dn), "years_max": max(r["years_peak_to_recover"] for r in dn), "years_median": med("years_peak_to_recover", dn),
                                        "after_low_1m_median": med("after_low_1m", x)}
    log("DECLINE_SENS", **sens_d)

    # 3. 가장 크게 오른 날 20번
    s0 = int(np.searchsorted(I.values, np.datetime64(START)))
    ret = P[1:] / P[:-1] - 1
    hi_prev = pd.Series(P).rolling(252, min_periods=60).max().shift(1).values        # 전날까지의 1년 최고가
    idx = [i for i in np.argsort(-ret) + 1 if i >= s0][:20]
    best = [{"date": d(I, i), "day": round(float(ret[i - 1]) * 100, 1), "below_high_prev": round(float(P[i - 1] / hi_prev[i] - 1) * 100, 1),
             "more_drop_6m": round(float(P[i + 1:i + 127].min() / P[i] - 1) * 100, 1) if i + 1 < len(P) else None,          # 그날 종가 대비 그 뒤 6개월 안 가장 낮은 값
             "low_6m_date": d(I, i + 1 + int(np.argmin(P[i + 1:i + 127]))) if i + 1 < len(P) else None} for i in idx]
    bd = {"n": len(best), "in_decline_10": sum(1 for b in best if b["below_high_prev"] <= -10), "in_decline_20": sum(1 for b in best if b["below_high_prev"] <= -20),
          "top5": best[:5], "smallest": best[-1]["day"], "fell_below_after": sum(1 for x in best if x["more_drop_6m"] is not None and x["more_drop_6m"] < 0),
          "fell_10_more_after": sum(1 for x in best if x["more_drop_6m"] is not None and x["more_drop_6m"] <= -10)}
    log("BEST_DAYS", **bd)

    # 4. 고점보다 낮았던 날의 몫
    hi_now = pd.Series(P).rolling(252, min_periods=60).max().values
    ddn = P[s0:] / hi_now[s0:] - 1
    tu = {"days": int(len(ddn)), "below_10": round(float((ddn <= -0.10).mean()), 3), "below_20": round(float((ddn <= -0.20).mean()), 3)}
    log("TIME_UNDER", **tu)

    # 5. 기존 계산(longform.py final_v5)을 그대로 옮김 — 대본 v6 도 같은 숫자를 씀
    lf = json.loads((HERE / "longform_result.json").read_text(encoding="utf-8"))
    fv = lf["final_v5"]
    checks = {"급반등 수 = 진짜 + 가짜 + 진행 중": reb["n"] == reb["fake"] + reb["real"] + (reb["n"] - reb["decided"]),
              "큰 하락은 모두 최고가 날 < 바닥 날": all(r["peak"] < r["low"] for r in T),
              "되찾은 구간은 바닥 뒤 1년 값이 있음": all(r["after_low_1y"] is not None for r in done),
              "가장 크게 오른 날 20개": bd["n"] == 20}
    for name, ok in checks.items():
        if not ok:
            log("CHECK", name=name, result="FAIL", next="대본에 쓰기 전에 고칠 것"); raise SystemExit(f"검사 실패: {name}")
    log("CHECK", n=len(checks), result="ok")
    res = {"version": VERSION, "made": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "source": {"spy": str(C.SPY_CSV.relative_to(C.ROOT)), "from": START, "to": d(I, len(P) - 1)},
           "rebound_days": {**reb, "sens": sens, "events": [{k: v for k, v in r.items() if k != "t"} for r in R]},
           "declines": {"summary": summ, "rows": T, "sens": sens_d}, "best_days": {**bd, "all": best}, "time_under": tu,
           "from_longform": {"version": lf["version"], "signal": fv["signal"], "cash_plan": fv["cash_plan"], "stuck": fv["stuck"], "intro": fv["intro"]}}
    OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1, default=str), encoding="utf-8")
    log("DONE", out=str(OUT.relative_to(C.ROOT)), sec=round(time.perf_counter() - t0, 2))


def selftest() -> None:
    I = pd.bdate_range("2000-06-01", periods=700)
    v = np.array([100.0] * 251 + [101.0, 70.0, 73.5, 65.0, 60.0, 63.0] + list(np.linspace(64, 120, 700 - 257)))
    e = declines(v, I, 0.15)
    assert len(e) == 1 and e[0]["pk"] == 251 and e[0]["lo"] == 255 and v[e[0]["rec"]] >= 101 > v[e[0]["rec"] - 1], e
    R = rebound_days(v, I)
    assert [(r["t"], r["kind"]) for r in R[:2]] == [(253, "가짜"), (256, "진짜")] and R[0]["days_to_break"] == 1, R[:2]     # 73.5 다음 날 65 < 반등 전 저점 70
    assert rebound_days(v, I, th=0.06) == [] or all(r["day"] >= 6 for r in rebound_days(v, I, th=0.06))
    print("[SELFTEST] ok — declines(최고가·바닥·되찾은 날)·rebound_days(가짜·진짜)")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        selftest()
    else:
        main()
