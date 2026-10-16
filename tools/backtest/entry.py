# -*- coding: utf-8 -*-
# VERSION: v1.4 — 2026-10-16 — 무작위 매수 기준 (사용자 지시 2026-10-16 "그럼 신호 없이 무작위로 매수 했을 때랑 비교하는 거지? 그게 맞는거 같은데"):
#          barrier_table() = 거래일마다 그날 종가에 샀다면 먼저 닿는 쪽(성공·실패)과 그 날 · random_entry() = 신호 없이 날짜만 무작위로 산 계좌 R 개
#          (방법과 같은 규칙: 매도한 날 뒤 기다리는 거래일 수를 그 방법의 실제 기다림에서 무작위로 뽑음 → 같은 횟수·같은 쉬는 기간, 날짜만 무작위)
#          — 시드 고정·로그. 판정은 simulate(barrier=…) 와 같은 종가·같은 허용 오차 (시험이 같은지 확인). 매수 규칙·simulate 는 그대로.
# (v1.3 — 2026-10-16 — 성공 판정 매도 'barrier=(m, n)' + 자주 나오는 매수 방법 10가지(RULES_V4·ORDER_V4) + 기준 'any'(매도 다음 날 바로 다시 매수).
#          사용자 지시 2026-10-16 "수익률로 비교하지말고 성공 기준을 매수 후 해당 지점에서 m%이하로 떨어지지 않고 매수 지점에서 n% 이상 상승하면
#          성공으로 하자" · 앞선 지시 "조건 발생이 너무 희소해서 거래 횟수가 없고 현금 가지고 있는 기간이 많아서 그런것 같아 매수 방법으로 다 변경해보고
#          매도 규칙도 변경해봐": 산 뒤 종가가 산 값 × (1+n) 이상이 먼저 나오면 성공(win), 산 값 × (1−m) 이하가 먼저 나오면 실패(loss) — 그 날 종가를 보고)
#          다음 거래일 종가에 매도 (다른 규칙과 같은 '다음 날' 약속). 거래 기록에 result·hit_i·target·stop. 예전 규칙(RULES)·trail·hold 는 그대로.
# (v1.2 — 2026-10-16 — 공통 매도 규칙에 '산 뒤 최고 종가에서 n% 떨어지면 매도'(trail) 더함 (사용자 지시 2026-10-16 "매도 조건을 1년뒤로
#          하지말고 매수 이후 고점에서 n%하락할 때로 해봐 n은 너가 적당히 설정하고"): simulate(trail=0.10) — 그날 종가가 산 뒤 최고 종가 × (1−n) 이하면
#          다음 거래일 종가에 매도 (매수와 같은 '다음 날' 약속). 거래 기록에 최고 종가·그날·매도 신호 날. hold(보유 기간)는 trail=None 일 때만 (예전 그대로).
# (v1.1 — 2026-10-16 — buy_and_hold(): 첫날 전부 매수 후 끝까지 보유한 값 (사용자 지시 2026-10-16 "1번째 박스에는 맨처음에 매수하고
#          그냥 냅둔 수익도 표시해" — 경주로 견주지 않고 계좌 칸에 참고로 함께 보임). 매수 규칙·시뮬레이션은 그대로.)
# (v1.0 — 2026-10-16 — 최초. 사용자 지시 2026-10-16 "2016년부터 현재까지로 설정하고 지금은 매수만 보는 거니까 매수에 관련된 것만
#          테스트해야지 왜 손절이 있어 매도 규칙은 똑같이 해 그리고 buy and hold랑 비교하지말고 주가 차트에서 매수/매도 지점을 표시하는 걸로 하자":
#          매수 신호 10가지 × 같은 매도 규칙(산 날부터 정해진 거래일 뒤 종가에 매도) — 매수 신호만 다르게 해서 '언제 매수'만 견준다.)
"""매수 신호 시험 — 매수 규칙만 다르고 매도 규칙은 모두 같다 (연구·교육용 — 투자 권유가 아니다. 과거 결과는 미래를 보장하지 않는다).

시점 약속 (미래 정보 금지):
  - 신호는 거래일 d 의 종가까지(그날 종가·지표)만 본다. 그 신호로 사는 것은 다음 거래일 d+1 의 종가.
    (예외: '매달 첫 거래일' 은 달력이라 미리 안다 — d 에서 '내일이 새 달 첫 거래일인가'를 본다.)
  - 매도 규칙 (모든 규칙 같음):
      trail=n (v1.2, 기본으로 부르는 쪽이 정함) — 산 날부터 그날까지 최고 종가(산 날 포함)를 따라가다가, 종가가 최고 × (1−n) 이하가 된 날 → 다음 거래일 종가에 전부 매도.
      trail=None — 산 날부터 hold 거래일 뒤 그날 종가에 전부 매도 (v1.0).
  - 판 날 종가로 다시 신호를 본다 → 신호가 있으면 다음 날 산다. 보유 중에 나온 신호는 쓰지 않는다 (돈이 이미 들어가 있음).
  - 돈: 모두 같은 capital(기본 $10,000)으로 시작, 더 넣거나 빼지 않는다. 살 때는 가진 현금 전부, 팔 때는 전부.
  - 매매 비용: 사고팔 때마다 거래 금액의 cost (기본 0.1%). 세금·환율은 넣지 않는다 (부르는 쪽이 한계에 적음).
  - 현금 이자: cash_ret[d] (d-1 → d, 기본 0). 값: px (기본 = 가격 close. 총수익 지수를 주면 배당 포함으로 셈).
  - 끝날 e 에 아직 들고 있으면 e 종가로 평가하고 '보유 중'(open)으로 적는다 (판 것으로 세지 않음).

매수 규칙 (교과서 기본값 그대로 — 결과를 보고 바꾸지 않음, stock/guides/concept.md 2·5번):
  m1      정해진 날: 매달 첫 거래일에 매수
  dip10   저점 매수: 종가가 그때까지 최고 종가보다 10% 이상 낮으면 매수
  dip20   큰 하락 매수: 종가가 그때까지 최고 종가보다 20% 이상 낮으면 매수
  drop2   급락 다음 날: 하루에 2% 이상 떨어진 다음 날 매수
  vix30   공포지수: VIX 종가가 30 이상이면 매수
  rsi30   과매도: RSI(14, 와일더)가 30 미만이면 매수
  ma200   200일선 돌파: 종가가 200일 이동평균 아래에서 위로 올라선 날 → 다음 날 매수
  gc      골든 크로스: 50일 평균이 200일 평균 아래에서 위로 올라선 날 → 다음 날 매수
  hi52    신고가 돌파: 종가가 지난 252 거래일(오늘 빼고)의 최고 종가를 넘으면 매수
  mom12   12개월 모멘텀: 종가가 252 거래일 전 종가보다 높으면 매수

자주 나오는 매수 방법 (v1.3 — RULES_V4, 같은 이름 짝: 예전 규칙을 문턱만 넓힘 — 문턱은 '10년 동안 신호 묶음 수·거래 수'만 보고 정함, 성공률은 보지 않음):
  any     기준: 매도한 다음 날 바로 다시 매수 (신호 없음 — '아무 날 매수')
  m1      매달 첫 거래일 (그대로)
  hi20    20일 신고가 돌파: 종가 > 지난 20 거래일(오늘 빼고) 최고 종가
  mom21   1개월 모멘텀: 종가 > 21 거래일 전 종가
  x20     20일선 위로 돌파: 종가가 20일 평균 아래 → 위
  gc520   골든 크로스(5·20일): 5일 평균이 20일 평균 아래 → 위
  drop1   −1% 하락 다음 날: 그날 하루 수익률 ≤ −1%
  rsi40   RSI(14) 40 아래
  vix20   VIX 종가 20 이상
  dd20_5  단기 저점: 종가 ≤ 최근 20 거래일(오늘 포함) 최고 종가 × 0.95
  dd5     최고가 −5%: 종가 ≤ 그때까지 최고 종가 × 0.95
"""
import logging
import time
from dataclasses import dataclass, field

import numpy as np
import pandas as pd

from . import daily as dl

LOG = logging.getLogger("backtest.entry")
VERSION = "v1.4"
HOLD_DAYS = 252                                                  # 기본 공통 매도: 산 날부터 252 거래일(약 1년) 뒤 종가
_TOL = 1e-12                                                     # 문턱 비교 허용 오차 (0.9×100 = 90.00000000000001 같은 부동소수 끝자리)


def log(stage, level=logging.INFO, **kv):
    LOG.log(level, "[%s] %s %s", stage, time.strftime("%Y-%m-%dT%H:%M:%S"), " ".join(f"{k}={v}" for k, v in kv.items()))


# ----------------------------------------------------------------------------- 지표 (그날 종가까지)
def indicators(close, vix=None):
    """매수 규칙이 쓰는 지표 (모두 그날 종가까지 — 미래 정보 없음). vix 는 close 날짜에 맞춘다 (없는 날 = NaN → 신호 없음)."""
    p = close.to_numpy(float)
    idx = close.index
    month = idx.to_period("M")
    ind = {
        "close": p,
        "ath": np.maximum.accumulate(p),                             # 그날까지 최고 종가 (오늘 포함)
        "ret1": np.r_[np.nan, p[1:] / p[:-1] - 1.0],                 # 그날 하루 수익률
        "sma50": dl.sma(p, 50), "sma200": dl.sma(p, 200),
        "rsi14": dl.rsi_wilder(p, 14),
        "hi252": dl.prior_max(p, 252),                               # 지난 252 거래일 최고 종가 (오늘 빼고)
        "mom252": np.r_[np.full(252, np.nan), p[252:] / p[:-252] - 1.0],
        "sma5": dl.sma(p, 5), "sma20": dl.sma(p, 20),                # v1.3
        "hi20": dl.prior_max(p, 20),                                 # 지난 20 거래일 최고 종가 (오늘 빼고)
        "max20": pd.Series(p).rolling(20, min_periods=20).max().to_numpy(),   # 최근 20 거래일 최고 종가 (오늘 포함)
        "mom21": np.r_[np.full(21, np.nan), p[21:] / p[:-21] - 1.0],
        "month_first": np.r_[True, month[1:] != month[:-1]],        # 새 달 첫 거래일 (달력 — 미리 앎)
        "vix": np.full(len(p), np.nan),
    }
    if vix is not None:
        v = vix.reindex(idx)
        ind["vix"] = v.to_numpy(float)
        miss = int(np.isnan(ind["vix"]).sum())
        log("SIGNAL", data="vix_aligned", days=len(p), missing_days=miss,
            vix_last=str(vix.index.max().date()), note="VIX 가 없는 날은 vix30 신호 없음")
    log("SIGNAL", indicators="ath,ret1,sma50,sma200,rsi14,hi252,mom252,month_first,vix", days=len(p),
        first=str(idx[0].date()), last=str(idx[-1].date()),
        first_sma200=str(idx[np.argmax(~np.isnan(ind["sma200"]))].date()) if (~np.isnan(ind["sma200"])).any() else "-")
    return ind


def _cross_up(a, b, d):
    """d 에 a 가 b 아래(또는 같음)에서 위로 올라섰나 (d-1: a ≤ b, d: a > b)."""
    if d < 1 or np.isnan(a[d]) or np.isnan(b[d]) or np.isnan(a[d - 1]) or np.isnan(b[d - 1]):
        return False
    return a[d - 1] <= b[d - 1] and a[d] > b[d]


# 규칙: key → (신호 함수(ind, d) → bool, 한국어 이름, 조건 설명)
def _m1(i, d):
    return d + 1 < len(i["close"]) and bool(i["month_first"][d + 1])


def _dip(k):
    return lambda i, d: i["close"][d] <= (1.0 - k) * i["ath"][d] * (1 + _TOL)


def _drop2(i, d):
    r = i["ret1"][d]
    return not np.isnan(r) and r <= -0.02 + _TOL


def _vix30(i, d):
    v = i["vix"][d]
    return not np.isnan(v) and v >= 30.0 - _TOL


def _rsi30(i, d):
    v = i["rsi14"][d]
    return not np.isnan(v) and v < 30.0


def _ma200(i, d):
    return _cross_up(i["close"], i["sma200"], d)


def _gc(i, d):
    return _cross_up(i["sma50"], i["sma200"], d)


def _hi52(i, d):
    h = i["hi252"][d]
    return not np.isnan(h) and i["close"][d] > h


def _mom12(i, d):
    m = i["mom252"][d]
    return not np.isnan(m) and m > 0.0


RULES = {
    "m1":    (_m1,      "매달 첫 거래일 매수",            "새 달 첫 거래일"),
    "dip10": (_dip(0.10), "고점 −10% 저점 매수",          "종가 ≤ 그때까지 최고 종가 × 0.9"),
    "dip20": (_dip(0.20), "고점 −20% 큰 하락 매수",       "종가 ≤ 그때까지 최고 종가 × 0.8"),
    "drop2": (_drop2,   "−2% 급락 다음 날 매수",          "그날 하루 수익률 ≤ −2%"),
    "vix30": (_vix30,   "공포지수 VIX 30 이상 매수",      "VIX 종가 ≥ 30"),
    "rsi30": (_rsi30,   "RSI 30 아래 과매도 매수",        "RSI(14) < 30"),
    "ma200": (_ma200,   "200일선 위로 돌파 매수",         "종가가 200일 평균 아래 → 위"),
    "gc":    (_gc,      "골든 크로스 매수",               "50일 평균이 200일 평균 아래 → 위"),
    "hi52":  (_hi52,    "52주 신고가 돌파 매수",          "종가 > 지난 252 거래일 최고 종가"),
    "mom12": (_mom12,   "12개월 모멘텀 매수",             "종가 > 252 거래일 전 종가"),
}
ORDER = list(RULES)


# v1.3 — 자주 나오는 매수 방법 (예전 규칙과 같은 집안, 문턱만 넓힘)
def _nz(x):
    return not np.isnan(x)


RULES_V4 = {
    "any":    (lambda i, d: True,                                                         "아무 날 (매도 다음 날 바로 다시 매수)", "신호 없음"),
    "m1":     (_m1,                                                                       "매달 첫 거래일 매수",        "새 달 첫 거래일"),
    "hi20":   (lambda i, d: _nz(i["hi20"][d]) and i["close"][d] > i["hi20"][d],           "20일 신고가 돌파 매수",      "종가 > 지난 20 거래일 최고 종가"),
    "mom21":  (lambda i, d: _nz(i["mom21"][d]) and i["mom21"][d] > 0.0,                   "1개월 모멘텀 매수",          "종가 > 21 거래일 전 종가"),
    "x20":    (lambda i, d: _cross_up(i["close"], i["sma20"], d),                         "20일선 위로 돌파 매수",      "종가가 20일 평균 아래 → 위"),
    "gc520":  (lambda i, d: _cross_up(i["sma5"], i["sma20"], d),                          "골든 크로스(5·20일) 매수",  "5일 평균이 20일 평균 아래 → 위"),
    "drop1":  (lambda i, d: _nz(i["ret1"][d]) and i["ret1"][d] <= -0.01 + _TOL,           "−1% 하락 다음 날 매수",      "그날 하루 수익률 ≤ −1%"),
    "rsi40":  (lambda i, d: _nz(i["rsi14"][d]) and i["rsi14"][d] < 40.0,                  "RSI 40 아래 매수",           "RSI(14) < 40"),
    "vix20":  (lambda i, d: _nz(i["vix"][d]) and i["vix"][d] >= 20.0 - _TOL,              "공포지수 VIX 20 이상 매수",  "VIX 종가 ≥ 20"),
    "dd20_5": (lambda i, d: _nz(i["max20"][d]) and i["close"][d] <= 0.95 * i["max20"][d] * (1 + _TOL), "단기 저점 매수 (20일 고점 −5%)", "종가 ≤ 최근 20 거래일 최고 종가 × 0.95"),
    "dd5":    (_dip(0.05),                                                                "최고가 −5% 매수",            "종가 ≤ 그때까지 최고 종가 × 0.95"),
}
ORDER_V4 = ["m1", "hi20", "mom21", "x20", "gc520", "drop1", "rsi40", "vix20", "dd20_5", "dd5"]     # 영상 순서 (any 는 기준)
ALL_RULES = {**RULES, **RULES_V4}


# ----------------------------------------------------------------------------- 시뮬레이션
@dataclass
class Run:
    key: str
    dates: pd.DatetimeIndex
    value: np.ndarray                 # 그날 종가 기준 계좌 가치
    holding: np.ndarray               # 그날 종가 뒤 주식을 들고 있나 (bool)
    trades: list = field(default_factory=list)
    hold: object = HOLD_DAYS            # 매도 규칙 설명: 정수 = 보유 거래일, ('trail', n) = 최고점에서 n% 하락


def simulate(key, ind, s, e, hold=HOLD_DAYS, capital=10_000.0, cost=0.001, px=None, cash_ret=None, dates=None, trail=None, barrier=None):
    """규칙 key 로 s..e (거래일 위치, 둘 다 포함) 를 돌린다 → Run.
    px: 사고파는 값 (기본 ind['close']). 신호·최고 종가·성공 판정은 늘 ind['close'](가격)로 본다.
    trail: 0~1 이면 '최고 종가에서 trail 만큼 떨어지면 다음 날 매도', None 이면 hold 거래일 뒤 매도.
    barrier: (m, n) 이면 (v1.3) 산 뒤 종가가 산 값 × (1+n) 이상 → 성공 / × (1−m) 이하 → 실패, 먼저 나온 쪽으로 판정하고 다음 날 매도 (trail·hold 보다 먼저)."""
    sig = ALL_RULES[key][0]
    price = ind["close"] if px is None else np.asarray(px, float)
    n = e - s + 1
    val, held = np.empty(n), np.zeros(n, bool)
    close = ind["close"]
    cash, units, buy_i, buy_cash = float(capital), 0.0, None, 0.0
    peak, peak_i, sell_pending = 0.0, None, False
    trades = []
    pending = s >= 1 and sig(ind, s - 1)                         # 시작일 s 의 매수는 s-1 종가까지 본 신호
    for j in range(n):
        d = s + j
        if j > 0 and cash_ret is not None and units == 0.0:
            cash *= 1.0 + cash_ret[d]
        if pending:                                              # d 종가에 전부 매수
            buy_cash, units = cash, cash * (1.0 - cost) / price[d]
            cash, buy_i, pending = 0.0, d, False
            peak, peak_i = float(close[d]), d
            trades.append({"rule": key, "buy_i": d, "buy_price": float(close[d]), "buy_px": float(price[d]),
                           "buy_cash": float(buy_cash)})
            if barrier is not None:
                m_, n_ = barrier
                trades[-1].update({"target": float(close[d]) * (1 + n_), "stop": float(close[d]) * (1 - m_), "result": None, "hit_i": None})
        elif units > 0.0 and (sell_pending if (trail is not None or barrier is not None) else d - buy_i >= hold):   # 공통 매도
            cash, sell_px = units * price[d] * (1.0 - cost), float(price[d])
            t = trades[-1]
            t.update({"sell_i": d, "sell_price": float(close[d]), "sell_px": sell_px, "sell_cash": float(cash),
                      "ret": float(cash / t["buy_cash"] - 1.0), "days": int(d - buy_i), "open": False,
                      "peak_price": peak, "peak_i": int(peak_i)})
            units, buy_i, sell_pending = 0.0, None, False
        val[j] = cash + units * price[d]
        held[j] = units > 0.0
        if units > 0.0 and barrier is not None and not sell_pending and trades[-1].get("result") is None and d > buy_i:   # v1.3 성공 판정
            t = trades[-1]
            if close[d] >= t["target"] * (1 - _TOL):
                t["result"], t["hit_i"] = "win", d
            elif close[d] <= t["stop"] * (1 + _TOL):
                t["result"], t["hit_i"] = "loss", d
            if t.get("result") is not None and d < e:            # 끝날(e)에 판정되면 판정만 적고 '보유 중'으로 둠 (팔 다음 날이 없음)
                sell_pending = True
        if units > 0.0 and trail is not None and barrier is None and not sell_pending and d < e:
            if close[d] > peak:
                peak, peak_i = float(close[d]), d
            if close[d] <= (1.0 - trail) * peak * (1 + _TOL):    # 최고에서 trail 이상 하락 → 다음 날 매도
                sell_pending = True
                trades[-1]["stop_i"] = d
        if units == 0.0 and not pending and d < e and sig(ind, d):
            pending = True
    if units > 0.0:                                              # 끝날까지 들고 있음 → 끝날 종가로 평가 (판 것으로 세지 않음)
        t = trades[-1]
        if close[e] > peak:
            peak, peak_i = float(close[e]), e
        t.update({"sell_i": e, "sell_price": float(close[e]), "sell_px": float(price[e]), "sell_cash": float(val[-1]),
                  "ret": float(val[-1] / t["buy_cash"] - 1.0), "days": int(e - buy_i), "open": True,
                  "peak_price": peak, "peak_i": int(peak_i)})
    idx = dates[s:e + 1] if dates is not None else pd.RangeIndex(n)
    if dates is not None:
        for t in trades:
            t["buy_date"], t["sell_date"] = str(dates[t["buy_i"]].date()), str(dates[t["sell_i"]].date())
    for t in trades:
        if barrier is not None and dates is not None:
            t["hit_date"] = str(dates[t["hit_i"]].date()) if t.get("hit_i") is not None else None
    return Run(key, idx, val, held, trades, ("barrier", barrier) if barrier is not None else ("trail", trail) if trail is not None else hold)


# ----------------------------------------------------------------------------- 무작위 매수 기준 (v1.4)
def barrier_table(close, s, e, m, n):
    """거래일 b(s..e)의 종가에 샀다면: 산 뒤 처음으로 종가 ≥ 산 값 × (1+n) → 성공(1) / ≤ × (1−m) → 실패(0) 가 나온 날 h.
    → (res, hit) 길이 len(close) — b 의 값만 채움 (e 까지 판정 없으면 res = -1, hit = -1). simulate(barrier=…) 와 같은 비교·허용 오차.
    미래 정보: b 의 판정은 b 뒤 종가로 '나중에' 정해지는 결과이고, 무작위 매수 날짜를 고를 때는 쓰지 않는다 (날짜는 기다림 수로만 정함)."""
    p = np.asarray(close, float)
    res, hit = np.full(len(p), -1, np.int8), np.full(len(p), -1, np.int64)
    for b in range(s, e + 1):
        up, dn = p[b] * (1 + n) * (1 - _TOL), p[b] * (1 - m) * (1 + _TOL)
        seg = p[b + 1:e + 1]
        if not len(seg):
            continue
        iu, idn = np.flatnonzero(seg >= up), np.flatnonzero(seg <= dn)
        ju, jd = (iu[0] if len(iu) else 1 << 60), (idn[0] if len(idn) else 1 << 60)
        if ju == jd == 1 << 60:
            continue
        if ju < jd:
            res[b], hit[b] = 1, b + 1 + ju
        else:                                                    # 같은 날 둘 다는 불가능 (n, m > 0)
            res[b], hit[b] = 0, b + 1 + jd
    return res, hit


def method_waits(run, s):
    """그 방법이 실제로 기다린 거래일 수: 첫 매수는 (신호 날 − (s−1)), 그 뒤는 (신호 날 − 매도한 날). 신호 날 = 매수 날 − 1."""
    out, prev = [], s - 1
    for t in run.trades:
        out.append(int(t["buy_i"] - 1 - prev))
        if t["open"]:
            break
        prev = t["sell_i"]
    return np.array(out, np.int64)


def random_entry(table, waits, s, e, runs=2000, seed=20261016):
    """신호 없이 날짜만 무작위로 산 계좌 runs 개 (같은 매도 규칙). 기다림 = waits 에서 복원 추출 (방법과 같은 분포 → 비슷한 횟수·쉬는 기간).
    signal 날 d = 마지막 매도 날 + 기다림 → d+1 종가 매수 → table 판정 날 h → h+1 매도 (h = e 이면 판정만 세고 보유 중).
    → dict: wins·losses (runs × (e−s+1), 그날까지 판정 난 누적 — int32), rates (runs,), trades (runs,), seed."""
    res, hit = table
    rng = np.random.default_rng(seed)
    L = e - s + 1
    W, Lo = np.zeros((runs, L), np.int32), np.zeros((runs, L), np.int32)
    nt = np.zeros(runs, np.int64)
    waits = np.asarray(waits, np.int64)
    if not len(waits):
        raise ValueError("[TRADE] random_entry: 방법의 기다림이 비어 있음 (거래 0) → 무작위 기준을 만들 수 없음")
    for r in range(runs):
        last = s - 1
        while True:
            d = last + int(waits[rng.integers(len(waits))])
            b = d + 1
            if b > e:
                break
            nt[r] += 1
            if res[b] < 0:                                       # 끝까지 판정 없음 (보유 중)
                break
            h = int(hit[b])
            (W if res[b] == 1 else Lo)[r, h - s] += 1
            if h + 1 > e:
                break
            last = h + 1
    W, Lo = np.cumsum(W, axis=1, dtype=np.int32), np.cumsum(Lo, axis=1, dtype=np.int32)
    dec = W[:, -1] + Lo[:, -1]
    rates = np.where(dec > 0, W[:, -1] / np.maximum(dec, 1), np.nan)
    log("TRADE", random_runs=runs, seed=seed, waits=len(waits), wait_median=float(np.median(waits)),
        trades_median=float(np.median(nt)), rate_mean=f"{np.nanmean(rates):.3f}", rate_p5=f"{np.nanpercentile(rates, 5):.3f}", rate_p95=f"{np.nanpercentile(rates, 95):.3f}")
    return {"wins": W, "losses": Lo, "rates": rates, "trades": nt, "seed": seed, "runs": runs}


def stats(run, capital=10_000.0):
    """결과 한 줄. 거래 승률·평균은 다 판 거래만 (보유 중인 마지막 거래는 따로)."""
    v = run.value
    closed = [t for t in run.trades if not t["open"]]
    rets = np.array([t["ret"] for t in closed], float)
    peak = np.maximum.accumulate(v)
    dd = v / peak - 1.0
    dd_i = int(np.argmin(dd))
    yrs = (run.dates[-1] - run.dates[0]).days / 365.25 if isinstance(run.dates, pd.DatetimeIndex) else len(v) / 252
    flat = ~run.holding
    waits, k = [], 0                                             # 현금으로 기다린 구간 길이 (거래일)
    for f in flat:
        if f:
            k += 1
        elif k:
            waits.append(k)
            k = 0
    if k:
        waits.append(k)
    op = [t for t in run.trades if t["open"]]
    return {
        "rule": run.key, "sell_rule": (f"{run.hold[0]}{run.hold[1]}" if isinstance(run.hold, tuple) else f"hold{run.hold}d"), "final": float(v[-1]), "total_return": float(v[-1] / capital - 1.0),
        "wins": sum(t.get("result") == "win" for t in run.trades), "losses": sum(t.get("result") == "loss" for t in run.trades),
        "undecided": sum(t.get("result") is None for t in run.trades) if isinstance(run.hold, tuple) and run.hold[0] == "barrier" else None,
        "success_rate": (lambda w, l: w / (w + l) if w + l else float("nan"))(sum(t.get("result") == "win" for t in run.trades), sum(t.get("result") == "loss" for t in run.trades)),
        "avg_days_to_decide": float(np.mean([t["hit_i"] - t["buy_i"] for t in run.trades if t.get("hit_i") is not None])) if any(t.get("hit_i") is not None for t in run.trades) else None,
        "cagr": float((v[-1] / capital) ** (1 / yrs) - 1.0) if yrs > 0 else float("nan"),
        "trades_closed": len(closed), "trades_open": len(op), "buys": len(run.trades),
        "win_rate": float((rets > 0).mean()) if len(rets) else float("nan"),
        "avg_trade": float(rets.mean()) if len(rets) else float("nan"),
        "median_trade": float(np.median(rets)) if len(rets) else float("nan"),
        "best_trade": float(rets.max()) if len(rets) else float("nan"),
        "worst_trade": float(rets.min()) if len(rets) else float("nan"),
        "open_trade_ret": float(op[0]["ret"]) if op else None,
        "invested_share": float(run.holding.mean()),
        "longest_wait_days": int(max(waits)) if waits else 0,
        "max_dd": float(dd.min()),
        "max_dd_date": str(run.dates[dd_i].date()) if isinstance(run.dates, pd.DatetimeIndex) else dd_i,
        "first_buy": run.trades[0].get("buy_date") if run.trades else None,
    }


def run_all(close, start, end, vix=None, keys=None, hold=HOLD_DAYS, capital=10_000.0, cost=0.001, px=None, cash_ret=None,
            label="main", trail=None):
    """규칙 전부를 같은 기간·같은 돈·같은 매도 규칙으로 → {key: (Run, stats)}. 단계 로그를 남긴다."""
    t0 = time.time()
    ind = indicators(close, vix)
    dates = close.index
    s, e = int(dates.searchsorted(pd.Timestamp(start))), int(dates.searchsorted(pd.Timestamp(end), side="right") - 1)
    if s < 252:
        raise ValueError(f"[SIGNAL] 시작 전 자료가 252 거래일보다 짧음 (s={s}) → 지표(200일선·52주·12개월)가 비어 있음. 자료를 더 앞에서부터 넣으세요")
    log("SIGNAL", label=label, start=str(dates[s].date()), end=str(dates[e].date()), days=e - s + 1,
        sell=f"trail{trail:.0%}" if trail is not None else f"hold{hold}d",
        cost=cost, capital=capital, px="close(가격만)" if px is None else "given", cash="0" if cash_ret is None else "given")
    out = {}
    for k in keys or ORDER:
        r = simulate(k, ind, s, e, hold, capital, cost, px, cash_ret, dates, trail=trail)
        st = stats(r, capital)
        out[k] = (r, st)
        log("TRADE", label=label, rule=k, buys=st["buys"], closed=st["trades_closed"], open=st["trades_open"],
            first_buy=st["first_buy"], invested=f"{st['invested_share']:.1%}", win=f"{st['win_rate']:.0%}" if st["trades_closed"] else "-",
            avg_trade=f"{st['avg_trade']:+.2%}" if st["trades_closed"] else "-")
    best = max(out, key=lambda k: out[k][1]["final"])
    log("RESULT", label=label, rules=len(out), best=best, best_final=f"{out[best][1]['final']:,.0f}",
        finals=",".join(f"{k}:{out[k][1]['final']:,.0f}" for k in out), sec=f"{time.time() - t0:.2f}")
    return out, ind, (s, e)


def forward_returns(close, start, end, hold=HOLD_DAYS, cost=0.001):
    """참고값 — 아무 날(s..e-hold 의 모든 거래일)에 사서 hold 거래일 뒤 판 수익률 분포 (비용 포함).
    규칙의 '매수 날짜'가 아무 날보다 나았는지 보는 잣대 (관망과 견주는 것이 아님)."""
    p = close.to_numpy(float)
    dates = close.index
    s, e = int(dates.searchsorted(pd.Timestamp(start))), int(dates.searchsorted(pd.Timestamp(end), side="right") - 1)
    i = np.arange(s, e - hold + 1)
    r = p[i + hold] / p[i] * (1 - cost) ** 2 - 1.0
    rep = {"hold_days": hold, "n_days": int(len(r)), "from": str(dates[s].date()), "to_last_buy": str(dates[e - hold].date()),
           "mean": float(r.mean()), "median": float(np.median(r)), "win_rate": float((r > 0).mean()),
           "p10": float(np.percentile(r, 10)), "p90": float(np.percentile(r, 90))}
    log("RESULT", reference="any_day_buy", **{k: (f"{v:+.2%}" if isinstance(v, float) else v) for k, v in rep.items()})
    return rep


def buy_and_hold(close, start, end, capital=10_000.0, cost=0.001, px=None):
    """참고값 — 시작일(s) 종가에 전부 사서 끝(e)까지 그대로 둔 계좌 (Buy and Hold). 판 적이 없으므로 끝 값은 평가 값 (매도 비용 없음).
    규칙과 같은 날·같은 돈·같은 매수 비용. → (값 배열 s..e, stats dict)."""
    dates = close.index
    s, e = int(dates.searchsorted(pd.Timestamp(start))), int(dates.searchsorted(pd.Timestamp(end), side="right") - 1)
    price = close.to_numpy(float) if px is None else np.asarray(px, float)
    units = capital * (1.0 - cost) / price[s]
    v = units * price[s:e + 1]
    dd = v / np.maximum.accumulate(v) - 1.0
    yrs = (dates[e] - dates[s]).days / 365.25
    st = {"rule": "buy_and_hold", "buy_date": str(dates[s].date()), "buy_price": float(close.iloc[s]), "end_date": str(dates[e].date()),
          "final": float(v[-1]), "total_return": float(v[-1] / capital - 1.0), "cagr": float((v[-1] / capital) ** (1 / yrs) - 1.0),
          "max_dd": float(dd.min()), "max_dd_date": str(dates[s + int(np.argmin(dd))].date())}
    log("RESULT", reference="buy_and_hold", buy=st["buy_date"], final=f"{st['final']:,.0f}", total=f"{st['total_return']:+.2%}",
        max_dd=f"{st['max_dd']:.1%}", note="경주로 견주지 않음 — 계좌 칸 참고값")
    return v, st

