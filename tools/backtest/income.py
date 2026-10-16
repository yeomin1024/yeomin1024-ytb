# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-16 — 최초. 주식 2번(커버드콜 원금)·3번(배당 ETF vs 지수 세후) 계좌 계산 (사용자 지시 2026-10-16
#          "이제 니즈에 따라 어떻게 테스트 계획 세우고 하는지 알겠지? 같은 방식으로 필요한 소스 생성해서 3개 영상 미리보기 영상 만들어봐").
#          withdraw_pair() = 분배금을 꺼내 쓴 ETF 계좌 vs 같은 날 같은 금액을 매도해 꺼낸 지수 ETF 계좌 · reinvest() = 배당을 (원천징수 뒤) 다시 매수한 계좌
#          (한 번에 / 매달 적립) · liquidate() = 끝에 모두 매도하고 차익에 세금을 낸 값 · month_starts() = 달 첫 거래일.
"""분배금·배당 계좌 계산 (연구·교육용 — 투자 권유가 아니다. 과거 결과는 미래를 보장하지 않는다).

자료: data.yahoo_daily(sym) 의 DataFrame[close(분할 반영 종가), div(그날이 배당락일이면 1주당 배당)].
시점 약속 (미래 정보 금지):
  - 사는 값·파는 값은 그날 종가. 배당은 배당락일 종가에 받은 것으로 셈 (실제 지급은 며칠 뒤 — 영향이 작아 한계에 적음).
  - 계좌는 그날까지의 종가·배당만으로 값을 정한다 (뒤 날 값을 보지 않음 — 시험이 확인).
  - 매매 비용 fee: 살 때·팔 때 거래 금액의 fee (기본 0.25% — 1번 영상과 같음). 배당 재투자 매수에도 fee.

withdraw_pair(inc, idx, start, end, initial, fee, tax=0):
  A = 분배금 ETF (inc): start 종가에 initial 전부 매수 → 배당락일마다 (1주당 배당 × 주식 수)를 꺼내 씀 (다시 넣지 않음). 주식 수는 그대로.
  B = 지수 ETF (idx): start 종가에 initial 전부 매수 → 자기 배당은 그날 종가에 다시 매수(세후·fee) → A 가 꺼낸 날, A 와 같은 금액을
      손에 쥐도록 B 주식을 그날 종가에 매도 (fee 만큼 더 팖). B 가 모자라면 남은 것 전부(바닥남)로 적음.
  → 두 계좌가 꺼낸 돈은 날짜·금액이 같다. 남은 계좌 값(원금)만 다르다.
reinvest(df, start, end, initial, tax, fee, monthly=0):
  배당락일마다 배당 × (1 − tax) 를 그날 종가에 다시 매수 (fee). monthly > 0 이면 달 첫 거래일마다 monthly 를 더 넣어 매수 (fee).
  세금: tax = 배당 원천징수율 (나라마다 다름 — 부르는 쪽이 0%·15%·30% 처럼 여러 값으로 확인). 판 차익 세금은 liquidate().
"""
import logging
import time

import numpy as np
import pandas as pd

LOG = logging.getLogger("backtest.income")
VERSION = "v1.0"


def log(stage, level=logging.INFO, **kv):
    LOG.log(level, "[%s] %s %s", stage, time.strftime("%Y-%m-%dT%H:%M:%S"), " ".join(f"{k}={v}" for k, v in kv.items()))


def _slice(df, start, end):
    d = df.loc[pd.Timestamp(start):pd.Timestamp(end)]
    if d.empty:
        raise ValueError(f"[INCOME] 기간 {start}~{end} 에 자료가 없음 → 날짜·심볼 확인")
    if d["close"].isna().any() or (d["close"] <= 0).any():
        raise ValueError(f"[INCOME] 기간 {start}~{end} 종가에 빈 값·0 이하가 있음 → 자료 확인")
    return d


def common(a, b, start, end):
    """두 자료의 같은 거래일만 (한쪽에만 있는 날은 뺌 — 로그)."""
    a, b = _slice(a, start, end), _slice(b, start, end)
    idx = a.index.intersection(b.index)
    drop = (len(a) - len(idx), len(b) - len(idx))
    if drop != (0, 0):
        log("INCOME", logging.WARNING, check="common_days", only_a=drop[0], only_b=drop[1], kept=len(idx))
    return a.loc[idx], b.loc[idx]


def month_starts(index):
    """달 첫 거래일의 위치 (index 안 순번)."""
    m = index.to_period("M")
    return np.flatnonzero(np.r_[True, m[1:] != m[:-1]])


def withdraw_pair(inc, idx, start, end, initial=100_000.0, fee=0.0025, tax=0.0, quiet=False):
    """→ dict: dates, a_val, b_val, out_cum(꺼낸 돈 누적, 두 계좌 같음), a_shares, b_shares, events[(i, 꺼낸 돈)], b_broke(바닥난 날 i 또는 None)."""
    A, B = common(inc, idx, start, end)
    ca, da = A["close"].to_numpy(float), A["div"].to_numpy(float)
    cb, db = B["close"].to_numpy(float), B["div"].to_numpy(float)
    n = len(ca)
    sa = initial * (1 - fee) / ca[0]
    sb = initial * (1 - fee) / cb[0]
    a_val, b_val, out_cum, b_sh = (np.empty(n) for _ in range(4))
    out, events, broke = 0.0, [], None
    for i in range(n):
        if i > 0 and db[i] > 0 and sb > 0:                       # B 자기 배당 → 세후 다시 매수
            sb += sb * db[i] * (1 - tax) * (1 - fee) / cb[i]
        if i > 0 and da[i] > 0:                                  # A 분배금 → 꺼내 씀 (세후 금액)
            cash = sa * da[i] * (1 - tax)
            out += cash
            events.append((i, cash))
            need = cash / (1 - fee) / cb[i]                      # B 가 같은 금액을 손에 쥐려면 팔 주식 수
            if need >= sb:
                if broke is None:
                    broke = i
                    log("INCOME", logging.WARNING, check="b_depleted", date=str(B.index[i].date()), need=round(need, 4), have=round(sb, 4))
                sb = 0.0
            else:
                sb -= need
        a_val[i], b_val[i], out_cum[i], b_sh[i] = sa * ca[i], sb * cb[i], out, sb
    log("INCOME", logging.DEBUG if quiet else logging.INFO, kind="withdraw_pair", start=str(A.index[0].date()), end=str(A.index[-1].date()), days=n, withdrawals=len(events),
        out_total=round(out, 2), a_end=round(a_val[-1], 2), b_end=round(b_val[-1], 2), fee=fee, tax=tax)
    return {"dates": A.index, "a_val": a_val, "b_val": b_val, "out_cum": out_cum, "a_shares": sa, "b_shares": b_sh,
            "events": events, "b_broke": broke, "a_close": ca, "b_close": cb}


def reinvest(df, start, end, initial=100_000.0, tax=0.15, fee=0.0025, monthly=0.0, dates=None, quiet=False):
    """→ dict: dates, val, shares, paid(넣은 돈 누적), div_gross(받은 배당 누적, 세전), tax_paid(누적), basis(취득 원가 누적).
    dates 를 주면 그 거래일만 씀 (두 계좌의 날을 맞출 때). quiet=True 면 결과 로그를 DEBUG 로 (굴리는 계좌 수백 개 — 집계만 INFO)."""
    D = _slice(df, start, end)
    if dates is not None:
        D = D.loc[D.index.intersection(dates)]
    c, d = D["close"].to_numpy(float), D["div"].to_numpy(float)
    n = len(c)
    buy_days = set(month_starts(D.index).tolist()) if monthly > 0 else set()
    sh = initial * (1 - fee) / c[0]
    paid, basis, gross, taxed = initial, initial, 0.0, 0.0
    val, shares, paid_c, gross_c, tax_c, basis_c = (np.empty(n) for _ in range(6))
    for i in range(n):
        if i > 0 and d[i] > 0:
            g = sh * d[i]
            gross += g
            taxed += g * tax
            net = g * (1 - tax)
            sh += net * (1 - fee) / c[i]
            basis += net
        if i > 0 and i in buy_days:
            sh += monthly * (1 - fee) / c[i]
            paid += monthly
            basis += monthly
        val[i], shares[i], paid_c[i], gross_c[i], tax_c[i], basis_c[i] = sh * c[i], sh, paid, gross, taxed, basis
    log("INCOME", logging.DEBUG if quiet else logging.INFO, kind="reinvest", start=str(D.index[0].date()), end=str(D.index[-1].date()), days=n, tax=tax, fee=fee, monthly=monthly,
        paid=round(paid, 2), div_gross=round(gross, 2), tax_paid=round(taxed, 2), end_val=round(val[-1], 2))
    return {"dates": D.index, "val": val, "shares": shares, "paid": paid_c, "div_gross": gross_c, "tax_paid": tax_c, "basis": basis_c}


def liquidate(val, basis, cg_tax, fee=0.0025):
    """끝에 모두 매도: 매도 비용 fee, 차익(매도 금액 − 취득 원가)이 있으면 cg_tax 만큼 세금. → 손에 남는 돈."""
    gross = val * (1 - fee)
    gain = max(0.0, gross - basis)
    return gross - cg_tax * gain
