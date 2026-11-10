#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.3 — 2026-11-10 — ① 버그: v1.1 에서 더한 유형 2 민감도 변수 이름(sens)이 판별법 민감도(sens)를 덮어써 result 의 signal.sensitivity 에 다른 표가 들어가 있었음 → bsens 로 나눔
#   (로그 [SENS] 숫자는 맞았고 대본·설명란에 쓴 숫자도 로그 것이라 바뀌는 숫자 없음) ② 대본 v5 에 나오는 숫자를 한곳에 모은 final_v5 + 서로 맞는지 검사 ([FINAL]) ③ 절반 매도가 실제로 실행된 사건 수(B_new_sold)
#   — 사용자 지시 2026-11-10 "진짜,가짜반등 대본도 고쳐보고 제목 등 영상 만들 때 필요한거 생성해줘".
# (v1.2 — 2026-11-08 — 자주 오는 하락(−10%) 기준 · 바로 매수 vs 다음 반등 날 (type_v3) — 사용자 지시 "평단보다 20% 떨어진거는 너무 드문 거 아니야? 좀 빈번하게 일어나는 폭락으로 생각하고 다시 설정해 그리고 다음 반등에서 사는게 맞는거야니야?".
# (v1.1 — 2026-11-08 — 사용자 대본 수정판의 유형 둘 시험 (plan_run · type_v2) — 사용자 지시 "아래 느낌으로 수정했는데 보완해서 다시 알려줘".
# (v1.0 — 2026-11-08 — 롱폼 「바닥인 줄 알고 샀는데 — 진짜 반등 · 가짜 반등」 계산 (사용자 대본 틀 2026-11-08 "아래 대본 틀을 짜봤는데 이런 느낌으로 롱폼 대본 만들어봐").
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.3 | 2026-11-10 | signal.sensitivity 덮어쓰기 버그 고침(bsens) · final_v5(대본 v5 숫자 모음 + 일관성 검사) · B_new_sold | main |
# | v1.2 | 2026-11-08 | type_v3: 빈도(반등 다음 날 값보다 5·7.5·10·15·20% 더 하락한 사건 수) · 유형 1 새 규칙(첫 5% · 평단 −10%마다 5%씩 · 최고가 되찾으면 나머지) · 유형 2 새 규칙(평단 −10% 아래 → 절반 매도 → 판 값 −10·20·30% 마다 1/3, 바로 매수) · 바로 vs 다음 반등 날 격자 108 · 유형 2 매도 기준 10·15·20% 민감도 | main(type_v3) — v1.0·v1.1 출력 그대로 |
# | v1.1 | 2026-11-08 | 사용자 수정판 유형 1·2 시험: A(현금 많음) 대가 규칙 · 반등할 때마다 일정 비율(사용자 안) · 다음 반등 날 실행(사용자 안) / B(주식 80 · 현금 20) 보유 · 모두 매도 · 절반 매도 → 판 값 −10·20·30% 뒤 반등 날 현금 1/3씩 → 최고가 되찾으면 나머지(사용자 안 + quick_board 규칙 6) · 민감도 | plan_run · main(type_v2) — v1.0 출력은 그대로 |
# | v1.0 | 2026-11-08 | 최초 (도입 = 2022-05-04 반등 날 종가에 1천만 원 · '1년 뒤' = 12개월(calc.py end_of 와 같음) · 사례마다 2주 안 20일선 대비 가장 높은 종가) — 흔한 판별법(반등 뒤 2주 안 20일선 + 거래량) 적중 · 다른 판별법·기간 민감도 · 사례 셋(2020-03 · 2022-06 · 2025-04) · 버핏 2008-10 · 유형 셋(물림·절반·현금) | 전부 (calc.py v2.0 의 load·events·Sim·master_next·ant_run 을 그대로 씀 — 쇼츠 숫자와 같게) |
#
# 규칙 (판단 = 그날 종가까지의 자료만 · 매매 = 다음 거래일 종가 — calc.py 와 같음):
#   반등 사건 = calc.py events (2000년 이후 · 전날 종가가 252거래일 최고가보다 10% 넘게 낮음 · 하루 +3% 넘게 · 앞 사건과 60거래일 넘게) → 20번 (12개월 평가가 되는 것만).
#   바닥 = 반등 날 앞 20거래일 안의 가장 낮은 종가.
#   흔한 판별법 (가정 — 흔히 말하는 '거래량 실린 20일선 돌파'): 반등 날부터 10거래일(2주) 안에, 종가가 20일 이동평균선 위 + 그날 거래량이 앞 20거래일 평균보다 많은
#        날이 있으면 '진짜 신호' (그날 판단) · 없으면 '가짜 신호' (10거래일째 판단 — 그 전에 바닥을 깨면 그날).
#   실제 = 판단한 날 뒤 6개월(126거래일) 안에 종가가 바닥 아래로 내려가면 '가짜 반등', 아니면 '진짜 반등'.
#   민감도 (반론 K3): 판단 기간 5·10·20일 × 이동평균 20·50일 × 실제 기간 3·6·12개월 · 다른 판별법 (RSI 30 회복 · 50일선 · 200일선 — 반등 날 기준).
#   유형 (12개월 · 계좌 = 주식 + 현금(^IRX 이자) · 처음 투자금 = 1):
#     1 물린 채 현금 없음 = 반등에 모두 매수 → (가) 원금보다 20% 넘게 하락하면 겁이 나 모두 매도 vs (나) 그대로 보유 — 12·36개월 · 원금 회복까지 걸린 날.
#     2 절반 매수 + 현금 절반 = 반등에 50% → (가) 개미(calc.py ANT — 평단 −5%마다 25%, 다 쓴 뒤 평단 −20% 매도) vs (나) 계획(남은 50%를 평단 −20%마다 직전 × 1.5 —
#       10.5% · 15.8% · 나머지, 팔지 않음).
#     3 현금만 = calc.py 대가 규칙(반등에 10% · 평단 −20%마다 직전 × 1.5, 팔지 않음) · 덧붙인 안 = 같은 규칙 + 반등 전 최고가를 되찾으면 남은 현금 모두 매수
#       (stock/guides/quick_board.md 규칙 6 '다 채우기 전 최고가를 되찾으면 남은 현금 모두' 와 같은 생각).
# 출력: calc/longform_result.json. ※ 연구·교육용 — 투자 권유 아님. 세금·수수료·환율 없음. 과거 자료이며 앞으로도 같다는 보장은 없음.
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

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import calc as C  # noqa: E402  (calc.py v2.0 — 쇼츠와 같은 사건·같은 시뮬레이션)

VERSION = "v1.3"
ROOT = C.ROOT
OHLCV_CSV = HERE / "spy_ohlcv.csv"     # SPY 거래량 — Yahoo chart API v8, 2026-11-08 받음 (가격은 SPY.csv adjclose 를 씀)
OUT = HERE / "longform_result.json"
SIG_WIN, MA_N, VOL_N, BOTTOM_N, FUT_N = 10, 20, 20, 20, 126
CASES = {"c1": "2020-03-02", "c2": "2008-03-11", "c3": "2025-04-09"}       # 모두 사건 목록 20번 안 · c2 = 신호 진짜 → 실제 가짜 (2020년대에는 이 꼴이 없음 — SIGNAL 로그)
NEWS = {"c1": ["2020-03-09", "2020-03-16"], "c2": ["2008-03-18", "2008-09-15"], "c3": ["2025-05-12"]}   # 뉴스 날 하루 등락 (대본 사실 — 날짜는 공개 보도)
INTRO = "2022-05-04"                   # 도입 사례 (사례 셋과 겹치지 않는 2020년대 가짜 반등)
BUFFETT = "2008-10-16"                 # 뉴욕타임스 기고 「Buy American. I Am.」 온라인 게재일 (그날 종가로 판단 → 다음 날 종가 매수로 봄)
PLAN2 = 0.5 / (1.5 + 1.5 ** 2 + 1.5 ** 3)  # 유형 2 계획: 남은 50% 를 a·1.5a·나머지로 → a = 7.02% 시작값 (첫 추가 = a × 1.5 = 10.5%)

log = C.log


def load():
    spy, irx = C.load()
    try:
        o = pd.read_csv(OHLCV_CSV, comment="#", parse_dates=["date"]).set_index("date")
    except Exception as e:  # noqa: BLE001
        log("FAIL", stage="data", file=OHLCV_CSV, err=repr(e), next="Yahoo chart API 로 SPY 거래량 다시 받기 (longform.py 머리 주석)")
        raise
    vol = o["volume"].astype(float).reindex(spy.index)
    log("DATA", source="SPY_ohlcv", rows=len(o), first=o.index[0].date(), last=o.index[-1].date(), dup=int(o.index.duplicated().sum()),
        missing_on_spy_days=int(vol.isna().sum()), zero_vol=int((vol == 0).sum()))
    if vol.isna().any() or (vol <= 0).any():
        raise SystemExit("거래량 자료 이상 — SPY.csv 날짜에 빈 값·0")
    return spy, irx, vol


class Ind:
    """지표 — t 날 값은 t 날 종가까지만 씀 (거래량 평균은 t 날을 뺀 앞 N일)."""

    def __init__(self, spy: pd.Series, vol: pd.Series):
        self.P = spy.values; self.V = vol.values; self.I = spy.index
        self.ma = {n: spy.rolling(n).mean().values for n in (20, 50, 200)}
        self.vavg = vol.shift(1).rolling(VOL_N).mean().values
        d = spy.diff(); up = d.clip(lower=0); dn = -d.clip(upper=0)
        self.rsi = (100 - 100 / (1 + up.ewm(alpha=1 / 14, adjust=False).mean() / dn.ewm(alpha=1 / 14, adjust=False).mean())).values

    def bottom(self, e: int) -> int:
        return int(np.argmin(self.P[e - BOTTOM_N:e])) + e - BOTTOM_N

    def judge(self, e: int, win: int = SIG_WIN, ma: int = MA_N, fut: int = FUT_N) -> dict:
        b = self.bottom(e); low = self.P[b]; sig = None; dec = None
        for j in range(e, min(e + win, len(self.P))):
            if self.P[j] < low:          # 신호 전에 바닥을 깸 → 그날 '가짜'로 판단
                dec = j; break
            if self.P[j] > self.ma[ma][j] and self.V[j] > self.vavg[j]:
                sig = j; dec = j; break
        if dec is None:
            dec = min(e + win - 1, len(self.P) - 1)
        after = self.P[dec + 1:dec + 1 + fut]
        broke = bool((self.P[e:dec + 1] < low).any() or (after < low).any())
        first_break = None
        if broke:
            seg = self.P[e:dec + 1 + fut]; k = int(np.argmax(seg < low)); first_break = self.I[e + k].strftime("%Y-%m-%d")
        pred_real = sig is not None
        return {"rebound": self.I[e].strftime("%Y-%m-%d"), "bottom": self.I[b].strftime("%Y-%m-%d"), "signal": "real" if pred_real else "fake",
                "decide": self.I[dec].strftime("%Y-%m-%d"), "actual": "fake" if broke else "real", "hit": pred_real == (not broke), "break_date": first_break,
                "close_vs_ma20_on_rebound": round((self.P[e] / self.ma[20][e] - 1) * 100, 1), "vol_ratio_on_rebound": round(self.V[e] / self.vavg[e], 2),
                "vol_ratio_on_decide": round(self.V[dec] / self.vavg[dec], 2), "close_vs_ma_on_decide": round((self.P[dec] / self.ma[ma][dec] - 1) * 100, 1)}


def pct(a: float, b: float) -> float:
    return round((a / b - 1) * 100, 1)


def at(spy: pd.Series, d: str) -> int:
    return spy.index.get_loc(pd.Timestamp(d))


def case_facts(spy: pd.Series, ind: Ind, sim: C.Sim, key: str, d: str) -> dict:
    e = at(spy, d); P = spy.values
    pk = int(np.argmax(P[max(0, e - 252):e])) + max(0, e - 252)
    j = ind.judge(e)
    w = P[e + 1:e + 1 + 252]; mn = int(np.argmin(w)) + e + 1
    # 반등 뒤 고점(바닥 깨기 전) — 2022 여름 반등처럼 오른 만큼
    stop = spy.index.get_loc(pd.Timestamp(j["break_date"])) if j["break_date"] else min(e + 126, len(P) - 1)
    hi_i = int(np.argmax(P[e:stop + 1])) + e
    rec = next((k for k in range(e + 1, len(P)) if P[k] >= P[pk]), None)
    out = {"rebound": d, "peak": spy.index[pk].strftime("%Y-%m-%d"), "drop_before": pct(P[e - 1], P[pk]), "rebound_day": pct(P[e], P[e - 1]),
           "judge": j, "low_1y": spy.index[mn].strftime("%Y-%m-%d"), "more_drop_from_rebound": pct(P[mn], P[e]),
           "rally_high": spy.index[hi_i].strftime("%Y-%m-%d"), "rally_from_bottom": pct(P[hi_i], P[ind.bottom(e)]),
           "ret_1y_from_buy": pct(P[sim.end_of(e, 12)], P[e + 1]),
           "max_vs_ma20_until_decide": round(float(max(P[k] / ind.ma[20][k] - 1 for k in range(e, at(spy, j["decide"]) + 1))) * 100, 1),
           "peak_regained": spy.index[rec].strftime("%Y-%m-%d") if rec else None,
           "news": {n: pct(P[at(spy, n)], P[at(spy, n) - 1]) for n in NEWS.get(key, [])}}
    if j["break_date"]:
        out["below_bottom_by_low"] = pct(P[mn], P[ind.bottom(e)])
    log("CASE", key=key, **{k: v for k, v in out.items() if k not in ("judge", "news")}, signal=j["signal"], actual=j["actual"], hit=j["hit"],
        decide=j["decide"], vol_ratio=j["vol_ratio_on_decide"], vs_ma=j["close_vs_ma_on_decide"], news=json.dumps(out["news"]))
    return out


def buffett(spy: pd.Series) -> dict:
    P = spy.values; e = at(spy, BUFFETT); b = e + 1
    w = P[b:b + 252]; mn = int(np.argmin(w)) + b
    rec = next((k for k in range(mn, len(P)) if P[k] >= P[b]), None)
    I = spy.index
    end = lambda y: min(int(np.searchsorted(I.values, np.datetime64(I[b] + pd.DateOffset(years=y)))), len(P) - 1)  # noqa: E731  (calc.py end_of 와 같은 달력 기준)
    out = {"op_ed": BUFFETT, "buy": spy.index[b].strftime("%Y-%m-%d"), "low": spy.index[mn].strftime("%Y-%m-%d"), "more_drop": pct(P[mn], P[b]),
           "back_to_buy_price": spy.index[rec].strftime("%Y-%m-%d") if rec else None, "ret_1y": pct(P[end(1)], P[b]), "ret_5y": pct(P[end(5)], P[b])}
    log("BUFFETT", **out)
    return out


def run_lump(sim: C.Sim, e: int, months: int, stop: float | None):
    """유형 1 — 반등 다음 날 모두 매수. stop 이면 원금(계좌 처음 값)보다 stop 넘게 줄면 다음 날 모두 매도 → 현금."""
    end = sim.end_of(e, months)
    if end is None:
        return None
    P, CR = sim.P, sim.CR; b = e + 1; units = 1.0 / P[b]; cash = 0.0; sold = None; mn = 1.0; pend = False
    for i in range(b + 1, end + 1):
        cash *= 1 + CR[i]
        if pend:
            cash += units * P[i]; units = 0.0; sold = i; pend = False
        v = cash + units * P[i]; mn = min(mn, v)
        if stop and units > 0 and v < 1 - stop:
            pend = True
    rec = None
    if mn < 1 and units > 0:
        below = next(i for i in range(b, end + 1) if P[i] < P[b])
        rec = next((k for k in range(below, len(P)) if P[k] >= P[b]), None)
    return {"ret": v - 1, "mdd": mn - 1, "sold": sim.I[sold].strftime("%Y-%m-%d") if sold else None, "recover_days": (rec - b) if rec else None}


def recovery_days(spy: pd.Series, e: int, look: int = 252 * 3) -> int | None:
    """반등 다음 날 산 값 — 그 뒤 3년 안 가장 낮은 날 다음에 다시 산 값을 되찾기까지 거래일 (가장 낮은 날도 산 값 위면 0 · 못 되찾으면 None)."""
    P = spy.values; b = e + 1
    w = P[b:b + look]; mn = int(np.argmin(w)) + b
    if P[mn] >= P[b]:
        return 0
    rec = next((k for k in range(mn, len(P)) if P[k] >= P[b]), None)
    return (rec - b) if rec else None


def plan2_next(nb: int):
    """유형 2 계획 — 첫 매수(50%)가 nb=1. 그 뒤 평단 −20%마다 10.5% → 15.8% → 나머지(max_buys=4 로 마지막은 남은 돈 전부)."""
    sizes = [PLAN2 * 1.5 ** k for k in range(1, 4)]
    return (0.20, sizes[nb - 1]) if nb - 1 < len(sizes) else None


def master_plus(sim: C.Sim, spy: pd.Series, e: int, months: int, a0: float, d: float, g: float):
    """유형 3 덧붙인 안 — calc.py 대가 규칙 + 반등 전 252일 최고가를 종가로 되찾은 날 다음 날 남은 현금 모두."""
    end = sim.end_of(e, months)
    if end is None:
        return None
    P, CR = sim.P, sim.CR
    peak = float(np.max(P[max(0, e - 252):e]))
    nextf = C.master_next(a0, d, g)
    cash, units, cost, pend, nb, mn, all_in = 1.0, 0.0, 0.0, a0, 0, 1.0, False
    dep = 1.0
    for i in range(e + 1, end + 1):
        p = P[i]; cash *= 1 + CR[i]; dep *= 1 + CR[i]
        if pend > 0 and cash > 1e-12:
            amt = min(pend, cash); units += amt / p; cost += amt; cash -= amt; nb += 1; pend = 0.0
        v = cash + units * p; mn = min(mn, v)
        if all_in or cash <= 1e-12:
            continue
        if p >= peak:
            pend = cash; all_in = True; continue
        nx = nextf(nb)
        if nx and units > 0 and p <= (cost / units) * (1 - nx[0]):
            pend = nx[1]
    return {"ret": v - 1, "mdd": mn - 1, "dep": dep - 1, "all_in": all_in}


def plan_run(sim: C.Sim, spy: pd.Series, e: int, months: int, w0: float, step=None, each=None, wait_reb=False, partial=None, peak_all=False):
    """v1.1 — 계획 하나를 반등 사건 e 에 (판단 = 그날 종가 · 매매 = 다음 날 종가 · 현금 = ^IRX 이자).
    w0 = 반등 다음 날 첫 매수 비중 · step=(D, G, A0) 평단 −D 마다 직전 × G (calc.py 대가 규칙과 같음) · each = 반등 날마다 처음 돈의 each 매수
    wait_reb = 조건이 된 뒤 '반등 날'(하루 +3% · 252일 최고가보다 10% 넘게 아래 — 사건 규칙과 같은 날)에만 실행
    partial=(trig, frac, ladder) 평단 −trig 아래면 주식 frac 매도 → 판 값 −ladder[k] 아래(+wait_reb면 그 뒤 반등 날)에 판 뒤 현금을 똑같이 나눠 다시 매수
    peak_all = 반등 전 252일 최고가를 종가로 되찾으면 남은 현금 모두."""
    end = sim.end_of(e, months)
    if end is None:
        return None
    P, CR = sim.P, sim.CR
    peak = float(np.max(P[max(0, e - 252):e]))
    b = e + 1; units = w0 / P[b]; cost = w0; cash = 1.0 - w0; dep = 1.0; mn = 1.0
    nb, last, pend, trig_on, sold, lad_k, c0, all_in = 1, w0, 0.0, False, None, 0, 0.0, False
    sold_n = rebuy_n = 0
    for i in range(b + 1, end + 1):
        p = P[i]; cash *= 1 + CR[i]; dep *= 1 + CR[i]
        if pend > 0 and cash > 1e-12:
            amt = min(pend, cash); units += amt / p; cost += amt; cash -= amt; pend = 0.0
        if sold == "pending":
            q = units * partial[1]; cash += q * p; cost *= 1 - partial[1]; units -= q; sold = float(p); c0 = cash; sold_n += 1
        v = cash + units * p; mn = min(mn, v)
        avg = cost / units if units > 1e-12 else 0.0
        if peak_all and not all_in and cash > 1e-9 and p >= peak:
            pend = cash; all_in = True; continue
        if each is not None and REB[i] and cash > 1e-9:
            pend = each if cash - each > 1e-9 else cash
        if step and units > 0 and cash > 1e-9:
            D, G, A0 = step
            if p <= avg * (1 - D):
                trig_on = True
            if trig_on and (not wait_reb or REB[i]):
                last = A0 * G if nb == 1 else last * G; nb += 1; pend = min(last, cash); trig_on = False
        if partial:
            trig, frac, lad = partial
            if sold is None and units > 0 and p <= avg * (1 - trig):
                sold = "pending"
            elif isinstance(sold, float) and lad_k < len(lad) and cash > 1e-9:
                if p <= sold * (1 - lad[lad_k]):
                    trig_on = True
                if trig_on and (not wait_reb or REB[i]):
                    pend = cash if lad_k == len(lad) - 1 else c0 / len(lad); lad_k += 1; trig_on = False; rebuy_n += 1
    return {"ret": v - 1, "mdd": mn - 1, "dep": dep - 1, "sold": sold_n, "rebuys": rebuy_n, "all_in": all_in}


REB = None   # 반등 날 표시 (main 에서 채움 — 사건 규칙: 하루 +3% · 전날 종가가 252일 최고가보다 10% 넘게 아래)


def summ(res: list[dict]) -> dict:
    r = np.array([x["ret"] for x in res]); m = np.array([x["mdd"] for x in res])
    st = sum(1 for x in res if "dep" in x and x["ret"] > x["dep"] and x["mdd"] >= -C.LOSS_L)
    return {"n": len(res), "loss20": int((m < -C.LOSS_L).sum()), "median_ret": round(float(np.median(r)) * 100, 1), "worst_ret": round(float(r.min()) * 100, 1),
            "worst_mdd": round(float(m.min()) * 100, 1), "win": int((r > 0).sum()), "stable": int(st) if any("dep" in x for x in res) else None}


def main() -> None:
    t0 = time.perf_counter()
    spy, irx, vol = load()
    sim = C.Sim(spy, irx); ind = Ind(spy, vol)
    ev = [e for e in C.events(spy) if sim.end_of(e, C.H_MONTHS) is not None]
    log("EVENTS", n=len(ev), dates=",".join(spy.index[e].strftime("%Y-%m-%d") for e in ev))

    # 1. 흔한 판별법 적중
    J = [ind.judge(e) for e in ev]
    for j in J:
        log("SIGNAL", **{k: j[k] for k in ("rebound", "bottom", "signal", "decide", "actual", "hit", "break_date", "vol_ratio_on_decide", "close_vs_ma_on_decide")})
    hits = sum(j["hit"] for j in J); fakes = sum(j["actual"] == "fake" for j in J)
    conf = {f"{p}->{a}": sum(1 for j in J if j["signal"] == p and j["actual"] == a) for p in ("real", "fake") for a in ("real", "fake")}
    main_rule = {"win_days": SIG_WIN, "ma": MA_N, "fut_days": FUT_N, "hits": hits, "n": len(J), "actual_fake": fakes, "always_fake_hits": fakes, "confusion": conf}
    log("RULE", **{k: (json.dumps(v) if isinstance(v, dict) else v) for k, v in main_rule.items()})

    # 1-1. 민감도 (K3) — 판단 기간 × 이동평균 × 실제 기간
    sens = []
    for win, ma, fut in itertools.product((5, 10, 20), (20, 50), (63, 126, 252)):
        jj = [ind.judge(e, win, ma, fut) for e in ev]
        sens.append({"win": win, "ma": ma, "fut": fut, "hits": sum(x["hit"] for x in jj), "actual_fake": sum(x["actual"] == "fake" for x in jj)})
    hr = [s["hits"] for s in sens]
    log("SENS", combos=len(sens), hits_min=min(hr), hits_max=max(hr), never_20=all(h < 20 for h in hr),
        best=json.dumps(max(sens, key=lambda s: s["hits"])), beats_always_fake=sum(1 for s in sens if s["hits"] > s["actual_fake"]))
    # 1-2. 다른 흔한 판별법 (반등 날 하나로 판단 · 실제 = 6개월)
    others = {}
    for name, f in (("rsi30", lambda e: ind.rsi[max(0, e - 10):e].min() < 30 and ind.rsi[e] >= 30),
                    ("ma50", lambda e: ind.P[e] > ind.ma[50][e]), ("ma200", lambda e: ind.P[e] > ind.ma[200][e])):
        h = sum(1 for e, j in zip(ev, J) if bool(f(e)) == (j["actual"] == "real"))
        others[name] = {"hits": h, "pred_real": int(sum(bool(f(e)) for e in ev))}
    log("OTHERS", **{k: json.dumps(v) for k, v in others.items()})

    # 2. 사례 셋
    cases = {k: case_facts(spy, ind, sim, k, d) for k, d in CASES.items()}
    # 2-1. 도입 — 바닥인 줄 알고 반등 날 종가에 1천만 원 (가상 사례 · 숫자는 실제 SPY)
    e = at(spy, INTRO); P = spy.values; w = P[e + 1:e + 1 + 63]; mn = int(np.argmin(w)) + e + 1
    intro = {"rebound": INTRO, "rebound_day": pct(P[e], P[e - 1]), "drop_before": pct(P[e - 1], float(np.max(P[max(0, e - 252):e]))),
             "low": spy.index[mn].strftime("%Y-%m-%d"), "more_drop": pct(P[mn], P[e]), "won": 10_000_000,
             "loss_won": int(round(10_000_000 * (P[mn] / P[e] - 1) / 10_000) * 10_000)}
    log("INTRO", **intro)

    # 3. 전문가 — 버핏 2008
    bf = buffett(spy)

    # 4. 유형
    #  유형 1: 모두 매수 → 겁이 나 매도 vs 보유
    t1 = {}
    for months in (12, 36):
        hold = [run_lump(sim, e, months, None) for e in ev]; pan = [run_lump(sim, e, months, C.LOSS_L) for e in ev]
        ok = [(e, h, p) for e, h, p in zip(ev, hold, pan) if h and p]
        sold = [(e, h, p) for e, h, p in ok if p["sold"]]
        t1[f"{months}m"] = {"n": len(ok), "panic_sold": len(sold),
                            "sold_events": [{"rebound": spy.index[e].strftime("%Y-%m-%d"), "sold": p["sold"], "panic_ret": round(p["ret"] * 100, 1),
                                             "hold_ret": round(h["ret"] * 100, 1)} for e, h, p in sold],
                            "hold_better_in_sold": sum(1 for _, h, p in sold if h["ret"] > p["ret"]),
                            "hold_median": round(float(np.median([h["ret"] for _, h, _ in ok])) * 100, 1)}
        log("TYPE1", months=months, n=len(ok), panic_sold=len(sold), hold_better_in_sold=t1[f"{months}m"]["hold_better_in_sold"],
            detail=json.dumps(t1[f"{months}m"]["sold_events"], ensure_ascii=False))
    rec = [(spy.index[e].strftime("%Y-%m-%d"), recovery_days(spy, e)) for e in ev]
    known = [r for _, r in rec if r is not None]
    t1["recovery"] = {"events": rec, "within_1y": sum(1 for r in known if r <= 252), "max_days": max(known), "max_years": round(max(known) / 252, 1),
                      "max_event": max((x for x in rec if x[1] is not None), key=lambda x: x[1])[0], "not_recovered": sum(1 for _, r in rec if r is None)}
    log("RECOVERY", within_1y=t1["recovery"]["within_1y"], n=len(rec), max_years=t1["recovery"]["max_years"], max_event=t1["recovery"]["max_event"],
        not_recovered=t1["recovery"]["not_recovered"])

    #  유형 2: 절반 + 현금 절반
    ant = [C.ant_run(sim, e, C.H_MONTHS) for e in ev]
    p2 = [sim.run(e, C.H_MONTHS, 0.5, plan2_next, stop=None, max_buys=4) for e in ev]
    t2 = {"ant": summ(ant), "plan": summ(p2), "plan_sizes": [round(PLAN2 * 1.5 ** k * 100, 1) for k in range(1, 4)],
          "per": [{"rebound": spy.index[e].strftime("%Y-%m-%d"), "ant_ret": round(a["ret"] * 100, 1), "ant_mdd": round(a["mdd"] * 100, 1),
                   "plan_ret": round(p["ret"] * 100, 1), "plan_mdd": round(p["mdd"] * 100, 1), "plan_buys": int(p["buys"])} for e, a, p in zip(ev, ant, p2)]}
    t2["ant_24m"] = summ([C.ant_run(sim, e, 24) for e in ev if sim.end_of(e, 24) is not None])
    t2["plan_24m"] = summ([sim.run(e, 24, 0.5, plan2_next, stop=None, max_buys=4) for e in ev if sim.end_of(e, 24) is not None])
    log("TYPE2", ant=json.dumps(t2["ant"]), plan=json.dumps(t2["plan"]), sizes=t2["plan_sizes"], ant_24m=json.dumps(t2["ant_24m"]), plan_24m=json.dumps(t2["plan_24m"]))
    for x in t2["per"]:
        log("TYPE2_EVENT", **x)

    #  유형 3: 현금만 — 대가 규칙(쇼츠) · + 최고가 되찾으면 나머지 · 한 번에
    R = json.loads((HERE / "result.json").read_text(encoding="utf-8"))["rules"]["master"]
    a0, dd_, g = R["a0"], R["drop"], R["growth"]
    mas = [sim.run(e, C.H_MONTHS, a0, C.master_next(a0, dd_, g)) for e in ev]
    mp = [master_plus(sim, spy, e, C.H_MONTHS, a0, dd_, g) for e in ev]
    lump = [sim.run(e, C.H_MONTHS, 1.0, lambda nb: None) for e in ev]
    pool = [g for g in itertools.product(C.GRID_A0, C.GRID_D, C.GRID_G) if g[0] <= 0.30 and g[2] >= 1.5]   # calc.pick 의 전문가 원칙 (막스 · 버핏)
    t3 = {"rule": R, "grid_rules": len(C.GRID_A0) * len(C.GRID_D) * len(C.GRID_G), "pool_rules": len(pool), "master": summ(mas), "master_plus": summ(mp), "lump": summ(lump), "plus_all_in": sum(1 for x in mp if x["all_in"]),
          "per": [{"rebound": spy.index[e].strftime("%Y-%m-%d"), "master_ret": round(m["ret"] * 100, 1), "plus_ret": round(p["ret"] * 100, 1),
                   "plus_mdd": round(p["mdd"] * 100, 1), "plus_all_in": p["all_in"], "lump_ret": round(l_["ret"] * 100, 1)} for e, m, p, l_ in zip(ev, mas, mp, lump)]}
    # 24개월로 늘려도 (K3)
    t3["master_24m"] = summ([sim.run(e, 24, a0, C.master_next(a0, dd_, g)) for e in ev if sim.end_of(e, 24) is not None])
    t3["master_plus_24m"] = summ([master_plus(sim, spy, e, 24, a0, dd_, g) for e in ev if sim.end_of(e, 24) is not None])
    t3["ant_24m"] = summ([C.ant_run(sim, e, 24) for e in ev if sim.end_of(e, 24) is not None])
    for k in ("master", "master_plus", "lump", "master_24m", "master_plus_24m", "ant_24m"):
        log("TYPE3", who=k, **t3[k])
    log("TYPE3", who="grid", grid_rules=t3["grid_rules"], pool_rules=t3["pool_rules"])
    log("TYPE3", who="plus_all_in", n=t3["plus_all_in"], c3=json.dumps([p for p in t3["per"] if p["rebound"] == CASES["c3"]]))

    # 5. v1.1 — 사용자 수정판 유형 둘 (A 현금 많음 · B 주식 80 + 현금 20)
    global REB
    hi252 = spy.rolling(252, min_periods=60).max().values; Pv = spy.values
    REB = np.zeros(len(Pv), bool); REB[1:] = (Pv[1:] / Pv[:-1] - 1 >= C.REB_TH) & (Pv[:-1] / hi252[:-1] - 1 <= C.DD_TH)
    MAS = (dd_, g, a0)
    PART = (0.20, 0.5, [0.10, 0.20, 0.30])
    tv = {}
    for months in (12, 36):
        k = f"{months}m"; ok = [e for e in ev if sim.end_of(e, months) is not None]
        run = lambda **kw: [plan_run(sim, spy, e, months, **kw) for e in ok]  # noqa: E731
        A = {"master_plus": run(w0=a0, step=MAS, peak_all=True), "master_wait_reb": run(w0=a0, step=MAS, wait_reb=True, peak_all=True),
             "each_10": run(w0=0.10, each=0.10), "each_20": run(w0=0.20, each=0.20), "lump": run(w0=1.0)}
        B = {"hold": run(w0=0.8), "sell_all": run(w0=0.8, partial=(0.20, 1.0, [])),
             "half_sell": run(w0=0.8, partial=PART, wait_reb=True, peak_all=True), "half_sell_now": run(w0=0.8, partial=PART, peak_all=True)}
        tv[k] = {"A": {n: summ(r) for n, r in A.items()}, "B": {n: summ(r) for n, r in B.items()}}
        hs = B["half_sell"]
        tv[k]["B_half_detail"] = {"sold": sum(1 for x in hs if x["sold"]), "sold_then_peak": sum(1 for x in hs if x["sold"] and x["all_in"]),
                                  "sold_then_rebuy": sum(1 for x in hs if x["rebuys"])}
        bsens = {}                                                      # v1.3: sens → bsens (판별법 민감도 sens 를 덮어쓰던 버그)
        for frac, lad, wr in itertools.product((0.3, 0.5), ([0.05, 0.10, 0.15], [0.10, 0.20, 0.30], [0.20, 0.30, 0.40]), (False, True)):
            bsens[f"sell{frac}_lad{'/'.join(str(int(x * 100)) for x in lad)}_wait{int(wr)}"] = summ(run(w0=0.8, partial=(0.20, frac, lad), wait_reb=wr, peak_all=True))["loss20"]
        tv[k]["B_sens_loss20"] = bsens
        for grp in ("A", "B"):
            for n, sm in tv[k][grp].items():
                log("TYPE_V2", months=months, group=grp, who=n, **sm)
        log("TYPE_V2", months=months, group="B", who="half_detail", **tv[k]["B_half_detail"])
        log("TYPE_V2", months=months, group="B", who="sens_loss20", min=min(bsens.values()), max=max(bsens.values()), detail=json.dumps(bsens))

    # 6. v1.2 — 자주 오는 하락 기준 (사용자 지시) · 바로 vs 다음 반등 날
    A3 = {"a0": 0.05, "drop": 0.10, "growth": 1.0}                 # 첫 5% · 평단 −10% 마다 처음 돈의 5% 씩 · 최고가 되찾으면 나머지
    B3 = (0.10, 0.5, [0.10, 0.20, 0.30])                              # 평단 −10% 아래 → 절반 매도 → 판 값 −10·20·30% 마다 판 뒤 현금 1/3
    freq = {f"{int(D * 1000) / 10:g}%": sum(1 for e in ev if Pv[e + 1:sim.end_of(e, 12) + 1].min() <= Pv[e + 1] * (1 - D)) for D in (0.05, 0.075, 0.10, 0.15, 0.20)}
    log("TYPE_V3", who="freq_12m", n=len(ev), **freq)
    t3v = {"rules": {"A": dict(A3, peak_all=True, exec="조건 다음 날 종가"), "B": {"start": "주식 80% · 현금 20%", "trigger_below_avg": B3[0], "sell": B3[1],
                                                                                  "rebuy_below_sell_price": B3[2], "exec": "조건 다음 날 종가", "peak_all": True}},
           "freq_12m": freq}
    st = lambda res: {**summ(res), "mean_ret": round(float(np.mean([x["ret"] for x in res])) * 100, 1)}  # noqa: E731
    for months in (12, 36):
        k = f"{months}m"; ok = [e for e in ev if sim.end_of(e, months) is not None]
        run = lambda **kw: [plan_run(sim, spy, e, months, **kw) for e in ok]  # noqa: E731
        stepA = (A3["drop"], A3["growth"], A3["a0"])
        rA, rAw = run(w0=A3["a0"], step=stepA, peak_all=True), run(w0=A3["a0"], step=stepA, wait_reb=True, peak_all=True)
        rB, rBw = run(w0=0.8, partial=B3, peak_all=True), run(w0=0.8, partial=B3, wait_reb=True, peak_all=True)
        t3v[k] = {"A_new": st(rA), "A_new_wait": st(rAw), "A_old_master_plus": st(run(w0=a0, step=MAS, peak_all=True)), "A_each_10": st(run(w0=0.10, each=0.10)),
                  "A_lump": st(run(w0=1.0)), "B_new": st(rB), "B_new_wait": st(rBw), "B_hold": st(run(w0=0.8)), "B_sell_all": st(run(w0=0.8, partial=(0.10, 1.0, [])))}
        t3v[k]["A_new_loss20_events"] = [{"rebound": spy.index[e].strftime("%Y-%m-%d"), "mdd": round(x["mdd"] * 100, 1)} for e, x in zip(ok, rA) if x["mdd"] < -C.LOSS_L]
        t3v[k]["B_new_sold"] = sum(1 for x in rB if x.get("sold"))          # v1.3: 평단 −10% 에 닿아 절반 매도가 실제로 실행된 사건 수
        t3v[k]["A_new_per"] = {spy.index[e].strftime("%Y-%m-%d"): round(x["ret"] * 100, 1) for e, x in zip(ok, rA)}
        t3v[k]["B_trigger_sens"] = {f"trig{int(tg * 100)}_lad{'/'.join(str(int(x * 100)) for x in ld)}_wait{int(wr)}": st(run(w0=0.8, partial=(tg, 0.5, ld), wait_reb=wr, peak_all=True))
                                    for tg, ld, wr in itertools.product((0.10, 0.15, 0.20), ([0.05, 0.10, 0.15], [0.10, 0.20, 0.30]), (False, True))}
        for n_ in ("A_new", "A_new_wait", "A_old_master_plus", "A_each_10", "A_lump", "B_new", "B_new_wait", "B_hold", "B_sell_all"):
            log("TYPE_V3", months=months, who=n_, **t3v[k][n_])
        log("TYPE_V3", months=months, who="A_new_loss20_events", events=json.dumps(t3v[k]["A_new_loss20_events"]))
    # 바로 vs 다음 반등 날 — 유형 1 격자 (첫 5·10·20% × 평단 −5~−20% × 1.0~1.5배 × 12·36개월)
    cmp_ = {"fewer_loss20": 0, "more_loss20": 0, "same_loss20": 0, "wait_mean_higher": 0, "n": 0, "mean_diff": []}
    for a0_, D_, G_ in itertools.product((0.05, 0.10, 0.20), (0.05, 0.075, 0.10, 0.125, 0.15, 0.20), (1.0, 1.25, 1.5)):
        for months in (12, 36):
            ok = [e for e in ev if sim.end_of(e, months) is not None]
            nw = [plan_run(sim, spy, e, months, w0=a0_, step=(D_, G_, a0_), peak_all=True) for e in ok]
            wt = [plan_run(sim, spy, e, months, w0=a0_, step=(D_, G_, a0_), wait_reb=True, peak_all=True) for e in ok]
            ln_, lw_ = summ(nw)["loss20"], summ(wt)["loss20"]
            md = float(np.mean([x["ret"] for x in wt]) - np.mean([x["ret"] for x in nw])) * 100
            cmp_["n"] += 1; cmp_["fewer_loss20"] += lw_ < ln_; cmp_["more_loss20"] += lw_ > ln_; cmp_["same_loss20"] += lw_ == ln_
            cmp_["wait_mean_higher"] += md > 0; cmp_["mean_diff"].append(md)
    cmp_["mean_diff_median_pp"] = round(float(np.median(cmp_.pop("mean_diff"))), 1)
    t3v["wait_vs_now_grid"] = cmp_
    log("TYPE_V3", who="wait_vs_now_grid", **cmp_)

    # 7. v1.3 — 대본 v5 에 나오는 숫자를 한곳에 (대본 ↔ 계산 대조용) + 서로 맞는지 검사
    conf = main_rule["confusion"]
    a12, b12, b36 = t3v["12m"], t3v["12m"], t3v["36m"]
    fin = {"intro": {"date": intro["rebound"], "rebound_day": intro["rebound_day"], "low": intro["low"], "more_drop": intro["more_drop"], "loss_won": intro["loss_won"],
                     "weeks": round((pd.Timestamp(intro["low"]) - pd.Timestamp(intro["rebound"])).days / 7, 1)},
           "signal": {"n": len(J), "hits": hits, "actual_fake": fakes, "always_fake_hits": fakes, "real_signals": conf["real->real"] + conf["real->fake"],
                      "real_signals_then_fake": conf["real->fake"], "fake_signals": conf["fake->fake"] + conf["fake->real"], "fake_signals_then_real": conf["fake->real"],
                      "sens_combos": len(sens), "sens_hits_min": min(hr), "sens_hits_max": max(hr), "sens_all_correct": sum(1 for h in hr if h == len(J)),
                      "sens_beats_always_fake": sum(1 for x in sens if x["hits"] > x["actual_fake"]), "others": {k_: v_["hits"] for k_, v_ in others.items()}},
           "cash_plan": {"rule": A3, "loss20_plan_12m": a12["A_new"]["loss20"], "loss20_lump_12m": a12["A_lump"]["loss20"], "median_plan_12m": a12["A_new"]["median_ret"],
                         "median_lump_12m": a12["A_lump"]["median_ret"], "plan_loss20_events": a12["A_new_loss20_events"], "plan_worst_mdd": a12["A_new"]["worst_mdd"]},
           "stuck": {"recovered": len(t1["recovery"]["events"]) - t1["recovery"]["not_recovered"], "within_1y": t1["recovery"]["within_1y"], "max_years": t1["recovery"]["max_years"],
                     "max_event": t1["recovery"]["max_event"], "hold_loss20_12m": b12["B_hold"]["loss20"], "half_loss20_12m": b12["B_new"]["loss20"], "half_sold_12m": b12["B_new_sold"],
                     "n_36m": b36["B_hold"]["n"], "hold_loss20_36m": b36["B_hold"]["loss20"], "half_loss20_36m": b36["B_new"]["loss20"],
                     "hold_median_36m": b36["B_hold"]["median_ret"], "half_median_36m": b36["B_new"]["median_ret"], "half_sold_36m": b36["B_new_sold"]}}
    sg = fin["signal"]
    checks = {"hits=맞힌 진짜+맞힌 가짜": sg["hits"] == conf["real->real"] + conf["fake->fake"], "신호 합=사건 수": sg["real_signals"] + sg["fake_signals"] == sg["n"],
              "실제 가짜=진짜 신호 뒤 가짜+가짜 신호 뒤 가짜": sg["actual_fake"] == conf["real->fake"] + conf["fake->fake"],
              "도입 손실=1천만 원×더 하락": abs(intro["loss_won"] - round(10_000_000 * intro["more_drop"] / 100, -4)) <= 10_000,
              "36개월 표본 < 12개월 표본": fin["stuck"]["n_36m"] < len(J)}
    for name_, ok_ in checks.items():
        if not ok_:
            log("FINAL", check=name_, result="FAIL", next="대본 v5 숫자를 쓰기 전에 이 검사를 먼저 고칠 것")
            raise SystemExit(f"final_v5 검사 실패: {name_}")
    for part, v_ in fin.items():
        log("FINAL", part=part, **{k_: (json.dumps(x_, ensure_ascii=False) if isinstance(x_, (dict, list)) else x_) for k_, x_ in v_.items()})
    log("FINAL", checks=len(checks), result="ok")

    res = {"version": VERSION, "made": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
           "source": {"spy": str(C.SPY_CSV.relative_to(ROOT)), "irx": str(C.IRX_CSV.relative_to(ROOT)), "volume": str(OHLCV_CSV.relative_to(ROOT))},
           "rules": {"signal": {"win_days": SIG_WIN, "ma": MA_N, "vol_avg_days": VOL_N, "bottom_days": BOTTOM_N, "fut_days": FUT_N},
                     "events_rule": [C.REB_TH, C.DD_TH, C.GAP], "horizon_m": C.H_MONTHS, "plan2_sizes_pct": t2["plan_sizes"]},
           "signal": {"main": main_rule, "events": J, "sensitivity": sens, "others": others},
           "intro": intro, "cases": cases, "buffett": bf, "type1": t1, "type2": t2, "type3": t3,
           "type_v2": {"rules": {"A_master": {"a0": a0, "drop": dd_, "growth": g, "peak_all": True}, "A_each": "반등 날마다 처음 돈의 10%·20%",
                                 "B_start": "주식 80% · 현금 20% (반등 다음 날)", "B_half_sell": {"trigger_below_avg": 0.20, "sell": 0.5, "rebuy_below_sell_price": [0.10, 0.20, 0.30],
                                 "rebuy_size": "판 뒤 현금 1/3씩(마지막은 남은 돈)", "exec": "조건 뒤 반등 날", "peak_all": True}}, **tv},
           "type_v3": t3v, "final_v5": fin}
    OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1, default=str), encoding="utf-8")
    log("DONE", out=OUT.relative_to(ROOT), sec=round(time.perf_counter() - t0, 2))


if __name__ == "__main__":
    main()
