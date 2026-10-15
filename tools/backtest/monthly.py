# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-10-15 — dip_trades·dca_avg_cost: 떨어지면 사기의 산 달·금액·평균 산 값 (대본 '왜 그런가' 근거, 사용자 지시 2026-10-15
#          "제목, 대본, 썸네일 프롬프트, 영상까지 다 만들어봐").
# (v1.0 — 2026-10-15 — 최초 (사용자 지시 2026-10-15 "주식 채널 컨셉은 ai로 코드 만들어서 가설을 백테스트해서 검증해보는거니까").
#          월별 자료 백테스트: 총수익 지수·현금 지수·'떨어지면 사기' 신호(전달까지 자료만)·매달 사기 vs 떨어지면 사기·한 번에 vs 나눠서,
#          여러 시작 시점(굴리는 기간)을 numpy 로 한 번에. 느린 반복 계산(naive_*)과 같은 값인지 시험 tools/tests/test_backtest.py.)
"""월별 백테스트 (연구·교육용 — 투자 권유가 아니다. 과거 결과는 미래를 보장하지 않는다).

시점 약속 (미래 정보 금지):
  - 달 t 에 넣는 돈은 달 t 가격(tri[t])으로 산다. Shiller 가격은 그 달 일별 종가의 평균 → '그 달 중에 산 평균 값'.
  - '떨어지면 사기' 신호 sig[t] 는 달 t-1 까지의 가격만 본다: P[t-1] ≤ (1 - drop) × max(P[0..t-1]).
    신호가 켜진 달 t 에 그때까지 모은 현금을 모두 달 t 가격으로 산다.
  - 현금 이자는 달 t-1 의 금리로 t-1 → t 한 달 (cash[t] = cash[t-1] × (1 + r[t-1]/1200)).
  - 굴리는 기간 [s, e] 의 끝 값 = 주식 × tri[e] + 남은 현금. 끝까지 못 산 현금은 현금 그대로 센다 (계속 기다리던 사람).
비용: 매매 수수료·세금·환율은 넣지 않는다 (두 방법 모두 같은 자산 — 부르는 쪽이 한계에 적음).
"""
import logging
import time

import numpy as np
import pandas as pd

LOG = logging.getLogger("backtest.monthly")


def log(stage, level=logging.INFO, **kv):
    LOG.log(level, "[%s] %s %s", stage, time.strftime("%Y-%m-%dT%H:%M:%S"), " ".join(f"{k}={v}" for k, v in kv.items()))


# ----------------------------------------------------------------------------- 지수
def total_return_index(price, dividend):
    """총수익 지수 (배당 재투자): tri[0] = 1, tri[t] = tri[t-1] × (P[t] + D[t]/12) / P[t-1]. D = 12개월 배당(연율)."""
    p = np.asarray(price, float)
    d = np.asarray(dividend, float)
    if np.isnan(p).any() or np.isnan(d[1:]).any():
        raise ValueError("[INDEX] 가격·배당에 빈 값 — complete_until 까지 잘라서 넣으세요")
    if (p <= 0).any():
        raise ValueError("[INDEX] 0 이하 가격")
    r = (p[1:] + d[1:] / 12.0) / p[:-1]
    tri = np.concatenate([[1.0], np.cumprod(r)])
    log("INDEX", kind="total_return", months=len(tri), growth=f"{tri[-1]:.4g}")
    return tri


def cash_index(n, annual_rate_pct=None):
    """현금 지수. annual_rate_pct=None → 이자 0. 배열이면 달 t-1 금리(%)로 t-1 → t 한 달."""
    if annual_rate_pct is None:
        return np.ones(n)
    r = np.asarray(annual_rate_pct, float)
    if len(r) != n or np.isnan(r[:-1]).any():
        raise ValueError("[INDEX] 금리 길이가 다르거나 빈 값")
    return np.concatenate([[1.0], np.cumprod(1.0 + r[:-1] / 1200.0)])


# ----------------------------------------------------------------------------- 신호
def prior_peak(price):
    """peak[t] = max(P[0..t-1]) (t=0 은 NaN) — 달 t 에 이미 알고 있는 최고치."""
    p = np.asarray(price, float)
    out = np.full(len(p), np.nan)
    out[1:] = np.maximum.accumulate(p)[:-1]
    return out


def dip_signal(price, drop):
    """sig[t] = P[t-1] ≤ (1 - drop) × max(P[0..t-1]). 달 t-1 까지만 봄 (미래 정보 없음)."""
    p = np.asarray(price, float)
    peak = prior_peak(p)
    sig = np.zeros(len(p), bool)
    sig[1:] = p[:-1] <= (1.0 - drop) * peak[1:]
    return sig


def at_high(price, tol=0.0):
    """high[t] = 전달 가격이 그때까지 최고치의 (1 - tol) 이상 — '사상 최고치(근처)일 때 시작'. 달 t 에 알 수 있음."""
    p = np.asarray(price, float)
    peak = prior_peak(p)
    out = np.zeros(len(p), bool)
    out[1:] = p[:-1] >= (1.0 - tol) * peak[1:]
    return out


def next_true(sig):
    """nxt[t] = t 이상에서 처음 sig 가 켜지는 달 (없으면 len(sig))."""
    n = len(sig)
    idx = np.where(sig, np.arange(n), n)
    return np.minimum.accumulate(idx[::-1])[::-1]


# ----------------------------------------------------------------------------- 굴리는 기간 (여러 시작 시점)
def windows(n, horizon, first=0, last=None):
    """시작 s (first..) 와 끝 e = s + horizon - 1 (≤ last) 배열."""
    last = n - 1 if last is None else last
    s = np.arange(first, last - horizon + 2)
    return s, s + horizon - 1


def dca_wealth(tri, s, e):
    """매달 1씩 산 끝 값: tri[e] × Σ_{t=s..e} 1/tri[t] (벡터)."""
    cs = np.concatenate([[0.0], np.cumsum(1.0 / tri)])
    return tri[e] * (cs[e + 1] - cs[s])


def dip_wealth(tri, cash, nxt, s, e):
    """매달 1씩 모으다 신호가 켜진 달에 모은 현금을 모두 사는 끝 값 + 통계.
    → dict(wealth, cash_left, avg_wait_months, buy_months) 배열 (기간마다)."""
    n = len(tri)
    W = np.empty(len(s))
    left = np.empty(len(s))
    wait = np.empty(len(s))
    buys = np.empty(len(s), int)
    for i, (a, b) in enumerate(zip(s, e)):
        t = np.arange(a, b + 1)
        tau = nxt[t]
        bought = tau <= b
        tau_c = np.where(bought, tau, 0)
        g_buy = cash[tau_c] / cash[t] * tri[b] / tri[tau_c]
        g_cash = cash[b] / cash[t]
        g = np.where(bought, g_buy, g_cash)
        W[i] = g.sum()
        left[i] = g_cash[~bought].sum()
        wait[i] = np.where(bought, tau - t, b + 1 - t).mean()
        buys[i] = len(np.unique(tau[bought]))
    assert n >= 1
    return {"wealth": W, "cash_left": left, "avg_wait_months": wait, "buy_months": buys}


def lump_vs_split(tri, cash, s, e, k=12):
    """목돈 1 을 달 s 에 한 번에 vs k 달에 나눠서 (기다리는 돈은 현금 이자) → (한 번에 끝 값, 나눠서 끝 값)."""
    if (s + k - 1 > e).any():
        raise ValueError("[TRADE] 나눠 사는 달이 기간보다 김")
    lump = tri[e] / tri[s]
    split = np.zeros(len(s))
    for j in range(k):
        split += (1.0 / k) * cash[s + j] / cash[s] * tri[e] / tri[s + j]
    return lump, split


def forward_return(tri, horizon):
    """fwd[t] = 달 t 에 사서 horizon 달 뒤 연율 수익률 (끝을 넘으면 NaN)."""
    n = len(tri)
    out = np.full(n, np.nan)
    if horizon < n:
        out[: n - horizon] = (tri[horizon:] / tri[: n - horizon]) ** (12.0 / horizon) - 1.0
    return out


def summarize(a, b, label_a, label_b):
    """두 방법 끝 값 비교 요약: a 가 b 보다 많은 기간 비율, 비율 a/b 의 분포."""
    a, b = np.asarray(a, float), np.asarray(b, float)
    ratio = a / b
    return {
        "windows": int(len(a)),
        f"{label_a}_wins": int((a > b).sum()),
        f"{label_a}_wins_share": float((a > b).mean()) if len(a) else None,
        "ratio_median": float(np.median(ratio)) if len(a) else None,
        "ratio_p10": float(np.quantile(ratio, 0.10)) if len(a) else None,
        "ratio_p90": float(np.quantile(ratio, 0.90)) if len(a) else None,
        "ratio_min": float(ratio.min()) if len(a) else None,
        "ratio_max": float(ratio.max()) if len(a) else None,
        "compare": f"{label_a}/{label_b}",
    }


def month_labels(index, positions):
    """DatetimeIndex 의 자리 → 'YYYY-MM' 목록."""
    return [pd.Timestamp(index[i]).strftime("%Y-%m") for i in positions]


# ----------------------------------------------------------------------------- 시험용 느린 계산 (한 달씩 실제로 사고 모으기)
def naive_dca(tri, s, e):
    units = 0.0
    for t in range(s, e + 1):
        units += 1.0 / tri[t]
    return units * tri[e]


def naive_dip(tri, cash, sig, s, e):
    units, cash_amt = 0.0, 0.0
    for t in range(s, e + 1):
        if t > s:
            cash_amt *= cash[t] / cash[t - 1]          # 지난달 현금에 한 달 이자
        cash_amt += 1.0                               # 이번 달 넣는 돈
        if sig[t]:
            units += cash_amt / tri[t]
            cash_amt = 0.0
    return units * tri[e] + cash_amt


# ----------------------------------------------------------------------------- v1.1 산 기록 (기간 하나 — 대본 사례·평균 산 값)
def dip_trades(tri, cash, sig, s, e):
    """기간 [s, e] 하나를 한 달씩: 떨어지면 사기의 산 기록. → dict(trades=[(t, 산 금액, tri[t])], cash_left, units, wealth, invested).
    산 금액 = 그달까지 모은 현금(이자 포함). invested = 실제로 주식에 들어간 돈. 평균 산 값 = invested / units (tri 단위)."""
    units, cash_amt, trades, invested = 0.0, 0.0, [], 0.0
    for t in range(s, e + 1):
        if t > s:
            cash_amt *= cash[t] / cash[t - 1]
        cash_amt += 1.0
        if sig[t]:
            trades.append((t, cash_amt, tri[t]))
            units += cash_amt / tri[t]
            invested += cash_amt
            cash_amt = 0.0
    return {"trades": trades, "cash_left": cash_amt, "units": units, "wealth": units * tri[e] + cash_amt, "invested": invested,
            "avg_cost": (invested / units) if units else float("nan")}


def dca_avg_cost(tri, s, e):
    """매달 1씩 산 평균 산 값 (tri 단위) = 넣은 돈 / 산 주식 수."""
    t = np.arange(s, e + 1)
    return len(t) / np.sum(1.0 / tri[t])
