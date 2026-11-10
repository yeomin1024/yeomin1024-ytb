#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-11-10 — '지금 판'(tools/trend_scan.py → stock/result/trend/trend_2026-11-10.md)을 페르소나에 대입해 고른 제목 2개의 정답 미리 확인.
#   사용자 지시 2026-11-10 "현재 트렌드를 페르소나에 대입해서 사람들의 심리를 파악해서 그들이 만족하게 할 수 있는 영상을 만들어야해 … 그렇게해서 다시 2개 알려줘봐".
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.0 | 2026-11-10 | 최초 — R '코스피 폭락장 급반등, 그 뒤' · H '반토막 뒤 본전까지 — 버틴 사람 vs 매달 더 산 사람 vs 던진 사람' | rebounds·breakeven·main |
#
# 규칙 (판단 = 그날 종가까지 · 앞날 자료 안 씀 · 자료 = 코스피 지수 종가(배당 없음) stock/topics/precheck/data/_KS11.csv, 2000년~):
#   R 급반등 날 = 전날 종가가 252거래일 최고가보다 dd(10%) 넘게 낮은 상태에서 하루 +th(3%) 넘게 오른 날 — 반등 편(calc.py)과 같은 정의, 단 가까운 날도 모두 셈(gap 0) + gap 60 도 같이.
#     가짜 = 그 뒤 fut(126)거래일 안에 '반등 전 20거래일의 가장 낮은 종가' 아래로 종가가 내려감. 아직 126거래일이 안 지난 날은 '진행 중'(이미 깼으면 가짜로 확정).
#     + 폭락(최고가 → 다시 그 값을 되찾기 전 가장 낮은 날, 30% 넘는 하락)마다: 바닥 전 급반등이 몇 번 있었나.
#   H 폭락 = 코스피가 252거래일 최고가보다 30% 넘게 하락한 구간. 세 사람 모두 **최고가 날 종가에 같은 돈 1 을 넣음**(고점에 물린 사람):
#     버틴 사람 = 그대로 보유 → 종가가 산 값을 되찾은 날.  더 산 사람 = 다음 달부터 달마다 첫 거래일 종가에 처음 돈의 add(2%)씩 더 삼 → 계좌 값 ≥ 넣은 돈 합계가 된 첫날.
#     던진 사람 = 종가가 산 값보다 sell(40%) 넘게 낮아진 다음 거래일 종가에 모두 매도 → 그 뒤 현금 (손실 확정 · 판 값 대비 1·3년 뒤 지수).
#     민감도: add 1·2·5% · 폭락 기준 25·30·40%.
# 출력: stock/topics/precheck/trend_titles_2026-11-10.json. ※ 연구·교육용 — 투자 권유 아님. 세금·수수료·배당 없음. 과거 자료이며 앞으로도 같다는 보장은 없음.
from __future__ import annotations

import json
import logging
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

VERSION = "v1.0"
HERE = Path(__file__).resolve().parent
OUT = HERE / "trend_titles_2026-11-10.json"
logging.basicConfig(level=logging.INFO, format="%(message)s", stream=sys.stdout)


def log(stage: str, level: int = logging.INFO, **kv) -> None:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    logging.log(level, f"[{stage}] [{ts}] " + " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, (dict, list)) else v}" for k, v in kv.items()))


def load(name: str = "_KS11") -> pd.Series:
    p = HERE / "data" / f"{name}.csv"
    try:
        s = pd.read_csv(p, comment="#", parse_dates=["date"]).set_index("date")["close"].astype(float)
    except Exception as e:  # noqa: BLE001
        log("FAIL", logging.ERROR, stage="load", file=p, err=repr(e), next="precheck.py fetch('^KS11') 로 다시 받기")
        raise SystemExit(1)
    dup, nan, bad = int(s.index.duplicated().sum()), int(s.isna().sum()), int((s <= 0).sum())
    log("LOAD", name=name, rows=len(s), first=s.index[0].date(), last=s.index[-1].date(), dup=dup, nan=nan, nonpositive=bad,
        max_gap_days=int(s.index.to_series().diff().dt.days.max()), max_day_move=round(float(s.pct_change().abs().max()), 3))
    if dup or nan or bad:
        log("DATA", logging.WARNING, issue="중복·빈 값·0 이하", action="뺌")
        s = s[~s.index.duplicated()].dropna(); s = s[s > 0]
    return s


def crashes(P: np.ndarray, th: float) -> list[tuple[int, int, int]]:
    """(최고가 날, 가장 낮은 날, 되찾은 날 또는 len) — 252거래일 최고가보다 th 넘게 하락한 구간."""
    hi = pd.Series(P).rolling(252, min_periods=1).max().values
    out, i = [], 0
    while i < len(P):
        if P[i] / hi[i] - 1 <= -th:
            pk = int(np.argmax(P[max(0, i - 251):i + 1])) + max(0, i - 251)
            j = i
            while j < len(P) and P[j] < P[pk]:
                j += 1
            out.append((pk, int(np.argmin(P[pk:j])) + pk, j)); i = j
        else:
            i += 1
    return out


# ---------------------------------------------------------------- R 급반등
def rebounds(s: pd.Series, th: float = 0.03, dd: float = 0.10, gap: int = 0, fut: int = 126, bottom_n: int = 20) -> dict:
    P, I = s.values, s.index
    ev, last = [], -10 ** 9
    for t in range(252, len(P)):
        prev_hi = P[t - 252:t].max()                                   # 전날까지의 최고가
        if P[t - 1] / prev_hi - 1 <= -dd and P[t] / P[t - 1] - 1 >= th and t - last > gap:
            ev.append(t); last = t
    rows = []
    for t in ev:
        bottom = P[t - bottom_n:t].min()
        w = P[t + 1:t + 1 + fut]
        brk = next((k for k, v in enumerate(w) if v < bottom), None)
        done = t + fut < len(P)
        kind = "가짜" if brk is not None else ("진짜" if done else "진행 중")
        f = lambda h: round(float(P[t + h] / P[t] - 1) * 100, 1) if t + h < len(P) else None   # noqa: E731
        rows.append({"date": I[t].strftime("%Y-%m-%d"), "day": round(float(P[t] / P[t - 1] - 1) * 100, 1), "kind": kind,
                     "break_date": I[t + 1 + brk].strftime("%Y-%m-%d") if brk is not None else None, "days_to_break": (brk + 1) if brk is not None else None,
                     "more_drop": round(float(w.min() / P[t] - 1) * 100, 1) if len(w) else None, "w1": f(5), "m1": f(21), "m6": f(126)})
    known = [r for r in rows if r["kind"] != "진행 중"]
    fake = [r for r in known if r["kind"] == "가짜"]
    res = {"th": th, "dd": dd, "gap": gap, "n": len(rows), "decided": len(known), "fake": len(fake), "real": len(known) - len(fake),
           "fake_share": round(len(fake) / len(known), 3) if known else None,
           "fake_days_to_break_median": int(np.median([r["days_to_break"] for r in fake])) if fake else None,
           "more_drop_median": round(float(np.median([r["more_drop"] for r in known])), 1) if known else None,
           "w1_up": sum(1 for r in known if r["w1"] is not None and r["w1"] > 0), "m6_up": sum(1 for r in known if r["m6"] is not None and r["m6"] > 0), "events": rows}
    log("REBOUND", th=th, dd=dd, gap=gap, n=res["n"], decided=res["decided"], fake=res["fake"], real=res["real"], fake_share=res["fake_share"],
        days_to_break_median=res["fake_days_to_break_median"], more_drop_median=res["more_drop_median"], w1_up=res["w1_up"], m6_up=res["m6_up"])
    return res


def rebounds_per_crash(s: pd.Series, R: dict, th: float = 0.30) -> list[dict]:
    P, I = s.values, s.index
    day = {r["date"]: r for r in R["events"]}
    out = []
    for pk, lo, j in crashes(P, th):
        if I[pk].year < 2000:
            continue
        before = [d for d in day if I[pk] < pd.Timestamp(d) < I[lo]]
        out.append({"peak": I[pk].strftime("%Y-%m-%d"), "low": I[lo].strftime("%Y-%m-%d"), "mdd": round(float(P[lo] / P[pk] - 1) * 100, 1),
                    "rebounds_before_low": len(before), "of_them_fake": sum(1 for d in before if day[d]["kind"] == "가짜"), "ongoing": j >= len(P)})
        log("REB_CRASH", **out[-1])
    return out


# ---------------------------------------------------------------- H 본전까지
def breakeven(s: pd.Series, th: float = 0.30, add: float = 0.02, sell: float = 0.40) -> dict:
    P, I = s.values, s.index
    month_first = np.zeros(len(P), bool)
    ym = I.year * 12 + I.month
    month_first[1:] = ym[1:] != ym[:-1]
    rows = []
    for pk, lo, j in crashes(P, th):
        if I[pk].year < 2000:
            continue
        ongoing = j >= len(P)
        # 버틴 사람
        hold_days = None if ongoing else j - pk
        # 더 산 사람 — 최고가 날 1 + 다음 달부터 달마다 add
        units, put, be = 1.0 / P[pk], 1.0, None
        for t in range(pk + 1, len(P)):
            if month_first[t]:
                units += add / P[t]; put += add
            if units * P[t] >= put:
                be = t; break
        last = len(P) - 1
        # 던진 사람
        sold = next((t + 1 for t in range(pk + 1, min(j, len(P) - 1)) if P[t] / P[pk] - 1 <= -sell), None)
        r = {"peak": I[pk].strftime("%Y-%m-%d"), "low": I[lo].strftime("%Y-%m-%d"), "mdd": round(float(P[lo] / P[pk] - 1) * 100, 1), "ongoing": ongoing,
             "hold_recovered": None if ongoing else I[j].strftime("%Y-%m-%d"), "hold_years": None if ongoing else round((I[j] - I[pk]).days / 365.25, 1),
             "add_recovered": I[be].strftime("%Y-%m-%d") if be is not None else None, "add_years": round((I[be] - I[pk]).days / 365.25, 1) if be is not None else None,
             "add_put_total": None, "sold": I[sold].strftime("%Y-%m-%d") if sold else None}
        if be is None:                                           # 아직 못 되찾음 — 오늘 손실률
            u2, p2 = 1.0 / P[pk], 1.0
            for t in range(pk + 1, len(P)):
                if month_first[t]:
                    u2 += add / P[t]; p2 += add
            r.update({"hold_now": round(float(P[last] / P[pk] - 1) * 100, 1), "add_now": round(float(u2 * P[last] / p2 - 1) * 100, 1), "add_put_total": round(p2, 2),
                      "add_breakeven_index": round(float(p2 / u2), 0), "hold_breakeven_index": round(float(P[pk]), 0), "index_now": round(float(P[last]), 0)})
        if sold:
            f = lambda y: round(float(P[sold + 252 * y] / P[sold] - 1) * 100, 1) if sold + 252 * y < len(P) else None   # noqa: E731
            r.update({"sold_loss": round(float(P[sold] / P[pk] - 1) * 100, 1), "after_sold_1y": f(1), "after_sold_3y": f(3),
                      "after_sold_more_drop": round(float(P[sold:min(j, len(P))].min() / P[sold] - 1) * 100, 1)})
        rows.append(r)
        log("BREAKEVEN", th=th, add=add, **{k: v for k, v in r.items() if v is not None})
    past = [r for r in rows if not r["ongoing"]]
    res = {"th": th, "add": add, "sell": sell, "episodes": rows, "past": len(past),
           "add_sooner": sum(1 for r in past if r["add_years"] is not None and r["add_years"] < r["hold_years"]),
           "hold_years_median": float(np.median([r["hold_years"] for r in past])) if past else None,
           "add_years_median": float(np.median([r["add_years"] for r in past if r["add_years"] is not None])) if past else None,
           "hold_years_max": max((r["hold_years"] for r in past), default=None), "add_years_max": max((r["add_years"] for r in past if r["add_years"] is not None), default=None)}
    log("BREAKEVEN_SUM", **{k: v for k, v in res.items() if k != "episodes"})
    return res


def selftest() -> None:
    idx = pd.bdate_range("2001-01-01", periods=700)
    # 251일 100 · 252번째 날 101(최고가) → 70 → +5% 급반등 73.5 → 65 → 60(가장 낮음) → +5% 63 → 그 뒤 계속 오름
    v = [100.0] * 251 + [101.0, 70.0, 73.5, 65.0, 60.0, 63.0] + list(np.linspace(64, 120, 700 - 257))
    s = pd.Series(v, index=idx)
    R = rebounds(s)
    assert [(r["date"], r["kind"]) for r in R["events"][:2]] == [(idx[253].strftime("%Y-%m-%d"), "가짜"), (idx[256].strftime("%Y-%m-%d"), "진짜")], R["events"][:3]
    assert R["events"][0]["days_to_break"] == 1 and R["events"][0]["more_drop"] == round((60 / 73.5 - 1) * 100, 1)      # 다음 날 65 < 반등 전 저점 70
    c = crashes(s.values, 0.30)
    assert c[0][0] == 251 and c[0][1] == 255 and s.values[c[0][2]] >= 101 and s.values[c[0][2] - 1] < 101, c           # 최고가 101 → 가장 낮은 60 → 101 을 되찾은 첫날
    H = breakeven(s, th=0.30, add=0.02, sell=0.35)
    e = H["episodes"][0]
    assert e["hold_years"] > e["add_years"], e                                                                          # 더 산 사람이 먼저 본전
    assert e["sold"] == idx[255].strftime("%Y-%m-%d") and e["sold_loss"] == round((60 / 101 - 1) * 100, 1), e           # 254번째 날 65(−35.6%) → 다음 날 60 에 매도
    print("[SELFTEST] ok — rebounds(가짜·진짜)·crashes·breakeven(버틴·더 산·던진)")


def main() -> None:
    if "--selftest" in sys.argv:
        try:
            selftest()
        except AssertionError as e:
            print("[SELFTEST] FAIL", e); raise SystemExit(1)
        return
    t0 = time.time()
    s = load()                                                    # 1999년 값은 2000년 사건의 '252거래일 최고가'를 구하는 데만 쓰임
    R = rebounds(s)
    out = {"version": VERSION, "made": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
           "rebound": {"main": R, "per_crash": rebounds_per_crash(s, R),
                       "sens": {f"th{int(th * 100)}_dd{int(dd * 100)}_gap{g}": {k: v for k, v in rebounds(s, th, dd, g).items() if k != "events"}
                                for th in (0.03, 0.04, 0.05) for dd in (0.10, 0.20) for g in (0, 60)}},
           "breakeven": {"main": breakeven(s), "sens": {f"th{int(th * 100)}_add{int(a * 100)}": {k: v for k, v in breakeven(s, th, a).items() if k != "episodes"}
                                                         for th in (0.25, 0.30, 0.40) for a in (0.01, 0.02, 0.05)}}}
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    log("DONE", out=OUT.name, sec=round(time.time() - t0, 2))


if __name__ == "__main__":
    main()
