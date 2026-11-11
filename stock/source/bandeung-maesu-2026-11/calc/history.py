#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.3.1 — 2026-11-11 — stuck_rebound: 자료 마지막 날이 급반등이면 건너뜀(IndexError 고침) · 코스피에도 같은 실험(kospi_bridge.stuck). v1.3 — 2026-11-11 — ① stuck_rebound: '이미 깊이 물린 상태(1년 최고가 대비 −30% 아래)에서 급반등이 나온 다음 날' 버틴 경우 vs 절반 매도 뒤 판 값 ±10% 에서 다시 매수(먼저 온 쪽)
#   — 페르소나 검토(물린 개미): 옛 실험(주식 80·현금 20 · 평단 −10% 에 절반 매도)은 "−50% 물린 사람에겐 버스 떠난 얘기"라 그 대목에서 이탈 → 처지에 맞는 실험으로.
#   ⚠ 위험 관련 규칙이 바뀜: 대본의 '이미 물렸다면' 실험 = (옛) 평단 −10% 절반 매도·판 값 −10·20·30% 재매수 → (새) 급반등 다음 날 절반 매도·판 값 ±10% 재매수. 옛 숫자(5번 대 2번 · 36.6% 대 29.1%)는 대본 v7 에서 안 씀.
#   ② single_stocks: 미국 대형주가 최고가(배당 포함)를 되찾기까지 — '지수의 기록은 종목에 그대로 맞지 않는다'의 근거 (자료 stock/topics/precheck/data/CSCO·INTC·GE·C·AIG.csv).
# v1.2 — 2026-11-11 — kospi_bridge(코스피 지수 — 배당 없음 — 의 30% 넘는 하락과 회복 · 급반등 가짜 몫): 근거가 미국뿐이라 국장에 물린 시청자가 '남 얘기'로 듣는 것을 받는 한두 문장용
#   (같은 정의 · 자료 stock/topics/precheck/data/_KS11.csv — 2026-11-10 까지).
# v1.1 — 2026-11-11 — fake_buyers(가짜 반등 15번 다음 날 매수한 경우의 매수가 회복 — 대본 v7 도입·사실 2) · 검사 1개 더함.
# v1.0 — 2026-11-11 — 새로: 대본 v6(아예 새로 씀 — '폭락 뒤 반등, 진짜인지 또 떨어질지 불안'을 미국 증시의 지난 기록으로 풀어 줌)에 쓰는 역사 숫자.
#   사용자 지시 2026-11-11 "이거 대본을 아예 새로 쓰자 페르소나 활용해서 쓰고 시청자의 생각은 폭락 후 반등했는데 이게 진짜로 반등하는건지 또 떨어질려고 하는건지 불안하다는거야
#   이걸 미국 주식 시장의 역사라는 정해져 있는 사실들을 근거로 해소로 해야돼".
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.3 | 2026-11-11 | stuck_rebound(새 실험 · 민감도 ±5·10·15% × −20·−30%) · single_stocks · 검사 2개 더함 | stuck_rebound·single_stocks·main |
# | v1.2 | 2026-11-11 | kospi_bridge: 코스피 30% 넘는 하락 횟수·회복 기간·진행 중인 하락·급반등 가짜 몫 (declines·rebound_days 를 그대로 씀) | kospi_bridge·main |
# | v1.1 | 2026-11-11 | fake_buyers: longform 의 반등 20번 가운데 실제 가짜 15번 — 반등 다음 날 산 값 회복까지 거래일(1년 안 · 가장 짧은 · 가운데 · 가장 긴) | main |
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

VERSION = "v1.3.1"
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


def stuck_rebound(P: np.ndarray, I, R: list[dict], dd: float = -0.30, X: float = 0.10) -> dict:
    """깊이 물린 상태(전날 종가가 1년 최고가보다 dd 넘게 낮음)에서 나온 급반등 날 t — 그 하락의 최고가에 매수해 보유 중인 사람.
    버팀 = 그대로. 절반 = t+1 종가(S)에 절반 매도 → 종가가 S×(1−X) 아래 또는 S×(1+X) 위가 된 첫날의 다음 날 종가에 판 돈으로 모두 다시 매수.
    판단은 그날 종가, 매매는 다음 거래일 종가. 본전 = 계좌 값이 최고가에 산 값(주식 1주 = 최고가)을 되찾은 날."""
    hi_prev = pd.Series(P).rolling(252, min_periods=60).max().shift(1).values
    dec = declines(P, I, 0.15)
    rows = []
    for r in R:
        t = r["t"]
        if P[t - 1] / hi_prev[t] - 1 > dd or t + 1 >= len(P):        # v1.3.1: 자료 마지막 날이 급반등이면 '다음 날 종가'가 없음 → 뺌 (코스피 2026-11-10 에서 IndexError)
            continue
        e = next((x for x in dec if x["pk"] < t < (x["rec"] if x["rec"] is not None else len(P))), None)
        if e is None:
            continue
        s = t + 1; S = P[s]; Ppk = P[e["pk"]]
        k = next((j for j in range(s + 1, len(P)) if P[j] <= S * (1 - X) or P[j] >= S * (1 + X)), None)
        if k is None or k + 1 >= len(P):
            continue                                             # 아직 결과가 안 난 날은 뺌
        side = "down" if P[k] <= S * (1 - X) else "up"
        rb = k + 1
        shares = 0.5 + 0.5 * S / P[rb]
        val = lambda j: (0.5 * P[j] + 0.5 * S) if j < rb else shares * P[j]   # noqa: E731
        end = min(s + 252, len(P) - 1)
        hb = next((j for j in range(s, len(P)) if P[j] >= Ppk), None)
        qb = next((j for j in range(s, len(P)) if val(j) >= Ppk), None)
        rows.append({"date": r["date"], "side": side, "below_peak": round(float(S / Ppk - 1) * 100, 1), "wait_days": rb - s, "shares": round(float(shares), 4),
                     "hold_min_1y": round(float(P[s:end + 1].min() / S - 1) * 100, 1), "half_min_1y": round(float(min(val(j) for j in range(s, end + 1)) / S - 1) * 100, 1),
                     "hold_years": round((I[hb] - I[s]).days / 365.25, 2) if hb is not None else None, "half_years": round((I[qb] - I[s]).days / 365.25, 2) if qb is not None else None})
    dn, up = [x for x in rows if x["side"] == "down"], [x for x in rows if x["side"] == "up"]
    med = lambda xs, k_: round(float(np.median([x[k_] for x in xs if x[k_] is not None])), 2) if xs else None   # noqa: E731
    both = [x for x in rows if x["hold_years"] is not None and x["half_years"] is not None]
    return {"dd": dd, "X": X, "n": len(rows), "years": sorted({x["date"][:4] for x in rows}), "below_peak_median": med(rows, "below_peak"),
            "down_first": len(dn), "up_first": len(up), "shares_down": med(dn, "shares"), "shares_up": med(up, "shares"),
            "shares_down_pct": round((float(np.median([x["shares"] for x in dn])) - 1) * 100, 1) if dn else None,      # 내려간 쪽: 주식 수가 몇 % 늘었나 (가운데 값)
            "shares_up_pct": round((float(np.median([x["shares"] for x in up])) - 1) * 100, 1) if up else None,        # 오른 쪽: 몇 % 줄었나
            "max_later_months": None, "max_sooner_years_abs": None, "shares_mean": round(float(np.mean([x["shares"] for x in rows])), 3),
            "wait_days_median": med(rows, "wait_days"), "hold_min_1y_median": med(rows, "hold_min_1y"), "half_min_1y_median": med(rows, "half_min_1y"),
            "hold_min_1y_worst": min(x["hold_min_1y"] for x in rows), "half_min_1y_worst": min(x["half_min_1y"] for x in rows),
            "hold_years_median": med(both, "hold_years"), "half_years_median": med(both, "half_years"),
            "half_sooner": sum(1 for x in both if x["half_years"] < x["hold_years"]), "half_later": sum(1 for x in both if x["half_years"] > x["hold_years"]),
            "down_years": [med(dn, "hold_years"), med(dn, "half_years")], "up_years": [med(up, "hold_years"), med(up, "half_years")],
            "max_later_years": round(max(x["half_years"] - x["hold_years"] for x in both), 2), "max_sooner_years": round(min(x["half_years"] - x["hold_years"] for x in both), 2), "rows": rows}
    # (위 None 두 칸은 아래에서 채움 — 대본에 '길어야 다섯 달' 꼴로 쓰려고)


def single_stocks() -> dict:
    """미국 대형주 — 그 하락의 최고가(배당 포함 수정 종가)에 매수했다면 되찾은 날. 파일이 없으면 그 종목은 빠짐 + 로그."""
    out = {}
    for sym, name, years in (("CSCO", "시스코", (2000, 2001)), ("INTC", "인텔", (2000, 2001)), ("GE", "제너럴 일렉트릭", (2000, 2001)), ("C", "씨티그룹", (2007,)), ("AIG", "AIG", (2007,))):
        p = C.ROOT / f"stock/topics/precheck/data/{sym}.csv"
        try:
            a = pd.read_csv(p, comment="#", parse_dates=["date"]).set_index("date")["adjclose"].astype(float)
        except Exception as e:  # noqa: BLE001
            log("STOCK", symbol=sym, file=str(p), err=repr(e)[:80], next="precheck.py fetch 로 받기 — 없으면 대본에서 그 종목 문장을 뺌"); continue
        a = a[a > 0]
        seg = a[[y in years for y in a.index.year]]
        pk = seg.idxmax(); after = a[a.index > pk]
        rec = after[after >= a[pk]]
        out[sym] = {"name": name, "peak": pk.strftime("%Y-%m-%d"), "recovered": rec.index[0].strftime("%Y-%m-%d") if len(rec) else None,
                    "years": round((rec.index[0] - pk).days / 365.25, 1) if len(rec) else None, "worst": round(float(after.min() / a[pk] - 1) * 100, 1),
                    "now_vs_peak": round(float(a.iloc[-1] / a[pk] - 1) * 100, 1), "last": a.index[-1].strftime("%Y-%m-%d"),
                    "years_since_peak": round((a.index[-1] - pk).days / 365.25, 1)}
        log("STOCK", symbol=sym, **out[sym])
    return out


def kospi_bridge() -> dict | None:
    """코스피 지수(배당 없음) — 미국과 같은 정의로. 파일이 없으면 None + 로그 (대본에 안 쓰면 됨)."""
    p = C.ROOT / "stock/topics/precheck/data/_KS11.csv"
    try:
        ks = pd.read_csv(p, comment="#", parse_dates=["date"]).set_index("date")["close"].astype(float)
    except Exception as e:  # noqa: BLE001
        log("KOSPI", file=str(p), err=repr(e), next="stock/topics/precheck/precheck.py fetch('^KS11') 로 받기 — 없으면 대본에서 코스피 문장을 뺌")
        return None
    bad = int(ks.index.duplicated().sum() + ks.isna().sum() + (ks <= 0).sum())
    if bad:
        log("KOSPI", issue="중복·빈 값·0 이하", n=bad, action="뺌"); ks = ks[~ks.index.duplicated()].dropna(); ks = ks[ks > 0]
    P, I = ks.values, ks.index
    rows = []
    for e in declines(P, I, 0.30):
        pk, lo, rec = e["pk"], e["lo"], e["rec"]
        rows.append({"peak": d(I, pk), "low": d(I, lo), "depth": round(float(P[lo] / P[pk] - 1) * 100, 1), "recovered": d(I, rec) if rec is not None else None,
                     "years_peak_to_recover": round((I[rec] - I[pk]).days / 365.25, 1) if rec is not None else None})
    done = [r for r in rows if r["recovered"]]
    R = [r for r in rebound_days(P, I) if r["kind"] != "진행 중"]
    out = {"last": d(I, len(P) - 1), "declines_30": len(rows), "past": len(done), "recovered": len(done), "ongoing": [r for r in rows if not r["recovered"]],
           "years_min": min(r["years_peak_to_recover"] for r in done), "years_max": max(r["years_peak_to_recover"] for r in done), "rows": rows,
           "rebound_days": len(R), "rebound_fake": sum(r["kind"] == "가짜" for r in R), "rebound_fake_share": round(sum(r["kind"] == "가짜" for r in R) / len(R), 3)}
    st = stuck_rebound(P, I, rebound_days(P, I))                 # v1.3.1: 같은 '깊이 물린 상태의 절반 매도' 실험을 코스피에
    out["stuck"] = {k: v for k, v in st.items() if k != "rows"}
    out["stuck"]["max_later_months"] = round(st["max_later_years"] * 12, 1)
    log("KOSPI", **{k: v for k, v in out.items() if k != "rows"})
    return out


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
    # 6. 가짜 반등에 매수한 경우 — longform 의 20번 가운데 실제 가짜였던 것만 (산 값 = 반등 다음 날 종가 · 회복 = 그 뒤 3년 안 가장 낮은 날 다음에 산 값을 되찾은 날)
    kind = {e["rebound"]: e["actual"] for e in lf["signal"]["events"]}
    rec = {dd_: n_ for dd_, n_ in lf["type1"]["recovery"]["events"]}
    fk = sorted(rec[k] for k, v in kind.items() if v == "fake")
    fb = {"n": len(fk), "recovered": sum(1 for x in fk if x is not None), "within_1y": sum(1 for x in fk if x is not None and x <= 252), "min_days": fk[0],
          "median_days": int(np.median(fk)), "max_days": fk[-1], "max_years": round(fk[-1] / 252, 1), "min_weeks": round(fk[0] / 5, 1)}
    log("FAKE_BUYERS", **fb)
    # 7. 깊이 물린 상태의 급반등 — 버팀 vs 절반 매도(판 값 ±10% 재매수)
    SR = stuck_rebound(P, I, R)
    SR["max_later_months"] = round(SR["max_later_years"] * 12, 1); SR["max_sooner_years_abs"] = abs(SR["max_sooner_years"])
    log("STUCK", **{k: v for k, v in SR.items() if k != "rows"})
    sr_sens = {f"dd{int(-dd_ * 100)}_x{int(x_ * 100)}": {k: v for k, v in stuck_rebound(P, I, R, dd_, x_).items() if k in ("n", "down_first", "up_first", "shares_mean", "hold_min_1y_median", "half_min_1y_median", "hold_years_median", "half_years_median", "half_sooner", "half_later", "max_later_years")}
               for dd_ in (-0.30, -0.20) for x_ in (0.05, 0.10, 0.15)}
    log("STUCK_SENS", **sr_sens)
    SS = single_stocks()
    # 8. 화면 주석·반론용 사실 — 2008-10-13 지수 상승률(S&P 500 지수 ^GSPC — SPY 종가와 다름) · 주가만(SPY 종가, 배당 없음)으로 최고가를 되찾기까지
    notes = {}
    try:
        g = pd.read_csv(C.ROOT / "stock/topics/precheck/data/_GSPC.csv", comment="#", parse_dates=["date"]).set_index("date")["close"].astype(float)
        notes["gspc_2008_10_13"] = round(float(g.pct_change()["2008-10-13"]) * 100, 1)
        w_ = g["2008-10-14":][:126]                                  # 그날 종가 대비 그 뒤 6개월 안 가장 낮은 값 (지수 기준 — 내레이션은 지수 숫자로 맞춤)
        notes["gspc_more_drop_after"] = round(float(w_.min() / g["2008-10-13"] - 1) * 100, 1); notes["gspc_low_date"] = w_.idxmin().strftime("%Y-%m-%d")
        sc = pd.read_csv(C.SPY_CSV, comment="#", parse_dates=["date"]).set_index("date")["close"].astype(float)
        for pk_ in ("2000-03-24", "2007-10-09"):
            aft = sc[sc.index > pk_]; rc_ = aft[aft >= sc[pk_]].index[0]
            notes[f"price_only_years_{pk_[:4]}"] = round((rc_ - pd.Timestamp(pk_)).days / 365.25, 1)
        notes["spy_2008_10_13"] = round(float(spy.pct_change()["2008-10-13"]) * 100, 1)
    except Exception as e:  # noqa: BLE001
        log("NOTES", err=repr(e)[:120], next="precheck.py fetch('^GSPC') — 없으면 대본에서 지수 숫자·'주가만' 문장을 뺌")
    log("NOTES", **notes)
    checks = {"깊이 물린 급반등: 내려간 쪽 + 오른 쪽 = 전체": SR["down_first"] + SR["up_first"] == SR["n"],
              "절반 매도: 내려가면 주식 수가 늘고 오르면 줄어듦": (SR["shares_down"] or 2) > 1 > (SR["shares_up"] or 0),
              "가짜 반등 수 = longform 실제 가짜": fb["n"] == fv["signal"]["actual_fake"],
              "급반등 수 = 진짜 + 가짜 + 진행 중": reb["n"] == reb["fake"] + reb["real"] + (reb["n"] - reb["decided"]),
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
           "fake_buyers": fb, "stuck_rebound": {**SR, "sens": sr_sens}, "single_stocks": SS, "notes": notes, "kospi_bridge": kospi_bridge(),
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
