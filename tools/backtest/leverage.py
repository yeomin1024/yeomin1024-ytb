# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-16 — 최초. 주식 4번(레버리지 1·2·3배 오래 모으기) 계산 (사용자 지시 2026-10-16 "같은 방식으로 필요한 소스 생성해서
#          3개 영상 미리보기 영상 만들어봐"): 지수 하루 수익률로 L배 ETF 를 만들고(매일 배수를 다시 맞춤 — 실제 QLD·TQQQ 와 같은 구조),
#          보수·차입 비용을 뺀다 → 실제 QLD(2006~)·TQQQ(2010~)와 맞는지 확인 (track()) · 한 번에 / 매달 적립 계좌 (grow()).
"""L배 일일 레버리지 ETF 흉내 (연구·교육용 — 투자 권유가 아니다. 과거 결과는 미래를 보장하지 않는다).

하루 수익률 (t-1 → t):
    r_L[t] = L × r_idx[t] − (L − 1) × (rf[t-1] + spread) × Δ일/365 − er × Δ일/365
    r_idx  = 지수(가격) 하루 수익률 — 실제 2배·3배 ETF 는 가격 지수의 '하루' 수익률 × L 을 목표로 한다 (배당은 목표에 없음)
    rf     = 전날 13주 국채 금리(^IRX, 연 %) — 빌린 (L−1) 몫의 이자. 미래 정보 아님 (전날 값)
    spread = 금리 위에 더 내는 차입 웃돈 (기본 0 — track() 로 실제 ETF 와 차이를 보고 부르는 쪽이 정함)
    er     = 운용 보수 (연, 예: QLD 0.95% · TQQQ 0.84% — 부르는 쪽이 정함)
    Δ일    = 달력 날 수 (주말 이자·보수도 셈)
  하루 r_L ≤ −100% 이면 그날 0 (바닥) — 그 뒤는 0 (로그 경고).
grow(r, dates, initial, monthly, fee): 첫날 initial 매수(+ 달 첫 거래일마다 monthly 매수, 매수 비용 fee) → 날마다 값·넣은 돈.
"""
import logging
import time

import numpy as np
import pandas as pd

LOG = logging.getLogger("backtest.leverage")
VERSION = "v1.0"


def log(stage, level=logging.INFO, **kv):
    LOG.log(level, "[%s] %s %s", stage, time.strftime("%Y-%m-%dT%H:%M:%S"), " ".join(f"{k}={v}" for k, v in kv.items()))


def daily_returns(idx_close, rf_pct, L, er=0.0, spread=0.0):
    """idx_close: 지수 종가 Series · rf_pct: 연 % Series (같은 날로 맞춤, 빈 날은 앞 값) → L배 하루 수익률 Series (첫날 0)."""
    c = idx_close.astype(float)
    rf = rf_pct.reindex(c.index).ffill().bfill().astype(float) / 100.0
    if rf.isna().any():
        raise ValueError("[LEVERAGE] 금리 자료가 비어 있음 → ^IRX 기간 확인")
    r = c.pct_change().fillna(0.0)
    days = pd.Series(c.index, index=c.index).diff().dt.days.fillna(0).to_numpy(float)
    rf_prev = rf.shift(1).fillna(rf.iloc[0]).to_numpy(float)
    out = L * r.to_numpy(float) - (L - 1) * (rf_prev + spread) * days / 365.0 - er * days / 365.0
    out[0] = 0.0
    bust = np.flatnonzero(out <= -1.0)
    if len(bust):
        log("LEVERAGE", logging.WARNING, check="wipeout", L=L, date=str(c.index[bust[0]].date()), r=round(out[bust[0]], 4))
        out[bust[0]] = -1.0
        out[bust[0] + 1:] = 0.0
    return pd.Series(out, index=c.index, name=f"x{L}")


def track(sim_r, real_close, name):
    """흉내 vs 실제 ETF (같은 날): 연 수익률 차이·하루 차이 표준편차·끝 값 비율 → dict (로그)."""
    real = real_close.astype(float)
    idx = sim_r.index.intersection(real.index)
    s = (1 + sim_r.loc[idx].iloc[1:]).cumprod()
    q = real.loc[idx] / real.loc[idx].iloc[0]
    q = q.iloc[1:]
    years = (idx[-1] - idx[0]).days / 365.25
    cs, cq = float(s.iloc[-1]), float(q.iloc[-1])
    d = sim_r.loc[idx].iloc[1:] - real.loc[idx].pct_change().iloc[1:]
    rep = {"name": name, "from": str(idx[0].date()), "to": str(idx[-1].date()), "years": round(years, 2),
           "sim_cagr": cs ** (1 / years) - 1, "real_cagr": cq ** (1 / years) - 1, "end_ratio_sim_over_real": cs / cq,
           "daily_diff_sd": float(d.std()), "daily_diff_mean": float(d.mean())}
    rep["cagr_gap"] = rep["sim_cagr"] - rep["real_cagr"]
    log("VALIDATE", name=name, **{k: (round(v, 5) if isinstance(v, float) else v) for k, v in rep.items() if k != "name"})
    return rep


def grow(r, initial=0.0, monthly=0.0, fee=0.0025, start=None, end=None):
    """r: 하루 수익률 Series → dict(dates, val, paid). start 날 종가에 initial 매수, 그 뒤 달 첫 거래일마다 monthly 매수 (start 달 포함 안 함 —
    start 날이 첫 매수). 매수 비용 fee."""
    x = r.loc[pd.Timestamp(start) if start else r.index[0]:pd.Timestamp(end) if end else r.index[-1]]
    n = len(x)
    if n < 2:
        raise ValueError("[LEVERAGE] 기간이 너무 짧음")
    m = x.index.to_period("M")
    new_month = np.r_[False, m[1:] != m[:-1]]
    rv = x.to_numpy(float)
    val, paid = np.empty(n), np.empty(n)
    v = (initial + monthly) * (1 - fee)
    p = initial + monthly
    val[0], paid[0] = v, p
    for i in range(1, n):
        v *= 1 + rv[i]
        if new_month[i] and monthly > 0:
            v += monthly * (1 - fee)
            p += monthly
        val[i], paid[i] = v, p
    return {"dates": x.index, "val": val, "paid": paid}
