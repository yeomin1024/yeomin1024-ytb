# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-16 — 최초. 사용자 지시 2026-10-16 "흔히 사용하는 매수 전략을 10가지 정도 골라서 그냥 매수하고 관망하는거랑
#          비교(투자 금액은 변동없이 동일하게) … 가장 단순한 전략과 비교를 하는거지 이걸 위한 티커, 테스트 기간을 적당하게 잡아보고 보완할게
#          있으면 보완해": 일별 자료로 매수 전략 10가지 vs 매수 후 관망 — 같은 돈을 한 번 넣고 더 넣지 않음, 신호는 그날 종가까지만 보고
#          다음 날 종가에 사고팖, 매매 비용, 거래 기록, 여러 시작 시점(굴리는 기간), 현금 이자 0·T-bill·10년 금리 확인.
"""일별 백테스트 — 매수 전략 vs 매수 후 관망 (연구·교육용 — 투자 권유가 아니다. 과거 결과는 미래를 보장하지 않는다).

시점 약속 (미래 정보 금지):
  - 신호는 거래일 d 의 종가까지(close[0..d])만 본다. 그 신호로 사고파는 것은 다음 거래일 d+1 의 종가.
  - 시작일 s 의 첫 거래: 신호를 s-1 종가까지로 정해 s 종가에 한다. 매수 후 관망은 s 종가에 전부 산다.
  - 수익은 총수익 지수(tr, 배당 재투자)로 센다. 사고파는 판단은 가격(close)으로 한다 (사람이 보는 지수 값).
  - 현금은 cash_ret[d] (d-1 → d 하루 이자, 기본 0).
  - 매매 비용: 사거나 팔 때마다 거래 금액의 cost (기본 0.1%). 세금·환율은 넣지 않는다 (부르는 쪽이 한계에 적음).
  - 투자 금액: 모두 같은 돈(capital)을 시작일에 갖고 시작하고 더 넣거나 빼지 않는다.

전략 (규칙은 교과서 기본값 그대로 — 결과를 보고 바꾸지 않음, stock/guides/concept.md 5번 과최적화):
  hold        매수 후 관망: 시작일에 전부 사서 끝까지 들고 있음 (비교 기준)
  dca12       분할 매수: 같은 돈을 12번에 나눠 매달 첫 거래일에 1/12씩 (남은 현금 ÷ 남은 횟수), 그 뒤 보유
  dip10       저점 매수: 그때까지 최고 종가보다 10% 이상 낮은 날이 오면 다음 날 전부 매수, 그 뒤 보유
  ladder      하락 분할 매수(물타기): 시작일에 1/4, 최고가 대비 −10%·−20%·−30% 에 닿을 때마다 1/4씩 (한 단계 한 번), 그 뒤 보유
  stop10      손절 −10% · 반등 재매수: 보유 중 최고 종가보다 10% 떨어지면 매도, 매도 뒤 최저 종가보다 10% 오르면 재매수
  tp10        익절 +10% · 저점 재매수: 산 값보다 10% 오르면 매도, 매도 뒤 최고 종가보다 10% 떨어지면 재매수
  sma200      200일 이동평균선: 종가 > 200일 평균이면 보유, 아니면 현금
  gc50_200    골든·데드 크로스: 50일 평균 > 200일 평균이면 보유, 아니면 현금
  brk55_20    신고가 돌파(터틀 2): 종가가 지난 55일 최고 종가를 넘으면 매수, 지난 20일 최저 종가 아래로 가면 매도
  rsi30_70    RSI(14, 와일더): 30 미만이면 매수, 70 초과면 매도
  mom12       12개월 모멘텀: 달 마지막 거래일 종가가 12달 전 달 마지막 종가보다 높으면 다음 달 보유, 아니면 현금
"""
import logging
import time
from dataclasses import dataclass, field

import numpy as np
import pandas as pd

LOG = logging.getLogger("backtest.daily")
VERSION = "v1.0"
TRADING_DAYS = 252


def log(stage, level=logging.INFO, **kv):
    LOG.log(level, "[%s] %s %s", stage, time.strftime("%Y-%m-%dT%H:%M:%S"), " ".join(f"{k}={v}" for k, v in kv.items()))


# ----------------------------------------------------------------------------- 지수
def tr_index_daily(close, monthly_dividend):
    """일별 총수익 지수. monthly_dividend = 달 첫날 index 의 12개월 배당(연율, 지수 단위 — Shiller D).
    그 달 배당(D/12)을 그 달 거래일 수로 나눠 매일 더한다: tr[d] = tr[d-1] × (P[d] + D_m/12/n_m) / P[d-1].
    배당 자료가 없는 달이 있으면 멈춘다 (부르는 쪽이 배당이 있는 기간까지 자른다)."""
    close = close.astype(float)
    month = close.index.to_period("M")
    dmap = monthly_dividend.copy()
    dmap.index = dmap.index.to_period("M")
    d_m = month.map(dmap.to_dict().get)
    if pd.isna(np.array(d_m, dtype=float)).any():
        miss = sorted({str(m) for m, v in zip(month, d_m) if v is None or pd.isna(v)})
        raise ValueError(f"[INDEX] 배당 자료가 없는 달: {miss[:3]}… → 배당이 있는 기간까지 잘라서 넣으세요")
    n_m = pd.Series(1, index=close.index).groupby(month).transform("sum").to_numpy()
    div_day = np.asarray(d_m, float) / 12.0 / n_m
    p = close.to_numpy()
    r = np.ones(len(p))
    r[1:] = (p[1:] + div_day[1:]) / p[:-1]
    tr = pd.Series(np.cumprod(r), index=close.index, name="tr")
    yrs = (close.index[-1] - close.index[0]).days / 365.25
    log("INDEX", kind="total_return_daily", days=len(tr), growth=f"{tr.iloc[-1]:.4g}",
        price_growth=f"{p[-1] / p[0]:.4g}", tr_cagr=f"{tr.iloc[-1] ** (1 / yrs) - 1:.4%}", price_cagr=f"{(p[-1] / p[0]) ** (1 / yrs) - 1:.4%}")
    return tr


def cash_daily(index, monthly_rate, kind):
    """현금 하루 이자 배열 (d-1 → d). kind='month_pct' (그 달 수익률 %, Fama-French RF) · 'annual_pct' (연 %, 10년 금리 — 위쪽 한계).
    그 달 수익률을 거래일 수로 복리 나눔. 자료가 없는 달이 있으면 멈춘다."""
    month = index.to_period("M")
    m = monthly_rate.copy()
    m.index = m.index.to_period("M")
    v = np.array(month.map(m.to_dict().get), dtype=float)
    if np.isnan(v).any():
        raise ValueError("[INDEX] 금리 자료가 없는 달이 있음 → 기간을 자르세요")
    R = v / 100.0 if kind == "month_pct" else v / 100.0 / 12.0
    n_m = pd.Series(1, index=index).groupby(month).transform("sum").to_numpy()
    c = (1.0 + R) ** (1.0 / n_m) - 1.0
    c[0] = 0.0
    return c


# ----------------------------------------------------------------------------- 지표 (그날 종가까지)
def sma(p, n):
    s = pd.Series(p).rolling(n, min_periods=n).mean().to_numpy()
    return s


def rsi_wilder(p, n=14):
    """와일더 RSI: 첫 값 = n 일 평균, 그 뒤 (이전×(n-1) + 오늘)/n."""
    p = np.asarray(p, float)
    d = np.diff(p, prepend=np.nan)
    up, dn = np.where(d > 0, d, 0.0), np.where(d < 0, -d, 0.0)
    out = np.full(len(p), np.nan)
    if len(p) <= n:
        return out
    au, ad = up[1:n + 1].mean(), dn[1:n + 1].mean()
    for i in range(n, len(p)):
        if i > n:
            au = (au * (n - 1) + up[i]) / n
            ad = (ad * (n - 1) + dn[i]) / n
        out[i] = 100.0 if ad == 0 else 100.0 - 100.0 / (1.0 + au / ad)
    return out


def prior_max(p, n):
    """그 전 n 거래일의 최고 종가 (오늘 빼고): max(p[d-n..d-1])."""
    return pd.Series(p).shift(1).rolling(n, min_periods=n).max().to_numpy()


def prior_min(p, n):
    return pd.Series(p).shift(1).rolling(n, min_periods=n).min().to_numpy()


def indicators(close):
    """전략이 쓰는 지표 전부 (그날 종가까지만 — 미래 정보 없음)."""
    p = close.to_numpy(float)
    idx = close.index
    month = idx.to_period("M")
    last_of_month = np.r_[month[1:] != month[:-1], True]          # 달 마지막 거래일 (마지막 날은 자료 끝 — 달이 안 끝났을 수 있음)
    last_of_month[-1] = False                                    # 자료 끝날을 달 마지막으로 보지 않음 (그 뒤 날짜를 알아야 함)
    me_idx = np.where(last_of_month)[0]
    mom = np.full(len(p), np.nan)                                # 달 마지막 날: 12달 전 달 마지막 종가 대비
    for k in range(12, len(me_idx)):
        mom[me_idx[k]] = p[me_idx[k]] / p[me_idx[k - 12]] - 1.0
    first_of_month = np.r_[True, month[1:] != month[:-1]]
    ind = {"close": p, "ath": np.maximum.accumulate(p), "sma50": sma(p, 50), "sma200": sma(p, 200),
           "hi55": prior_max(p, 55), "lo20": prior_min(p, 20), "rsi14": rsi_wilder(p, 14),
           "mom12": mom, "month_end": last_of_month, "month_first": first_of_month}
    log("SIGNAL", indicators="ath,sma50,sma200,hi55,lo20,rsi14,mom12", days=len(p),
        first_sma200=str(idx[np.argmax(~np.isnan(ind["sma200"]))].date()), month_ends=int(last_of_month.sum()))
    return ind


# ----------------------------------------------------------------------------- 전략 (상태 기계)
_TOL = 1e-12                                                     # 문턱 비교 허용 오차 (1.1×100 = 110.00000000000001 같은 부동소수 끝자리)


def _ge(a, b):
    return a >= b * (1 - _TOL)


def _le(a, b):
    return a <= b * (1 + _TOL)


class Strategy:
    """decide(d) 는 거래일 d 종가까지 보고 다음 날 할 일을 돌려준다: ('buy', 현금 중 비율) · ('sell', 1.0) · None.
    on_fill(d, side, …) 은 산 날·판 날에 불린다 (산 값·최고가 추적용)."""
    key = "?"
    kind = "inout"           # inout = 사고팔기 반복 · entry = 사는 방법만 (그 뒤 보유)

    def __init__(self, ind):
        self.i = ind
        self.holding = False

    def start(self, s):
        """시작일 s 에 할 일 (s-1 종가까지 본 판단). 기본: decide(s-1)."""
        return self.decide(s - 1)

    def decide(self, d):
        raise NotImplementedError

    def on_fill(self, d, side):
        self.holding = side == "buy" or (self.holding and side != "sell")


class Hold(Strategy):
    key, kind = "hold", "entry"

    def start(self, s):
        return ("buy", 1.0)

    def decide(self, d):
        return None


class DCA12(Strategy):
    key, kind = "dca12", "entry"

    def __init__(self, ind, k=12):
        super().__init__(ind)
        self.k, self.done = k, 0

    def start(self, s):
        return ("buy", 1.0 / self.k)

    def on_fill(self, d, side):
        super().on_fill(d, side)
        self.done += 1

    def decide(self, d):
        if self.done >= self.k or d + 1 >= len(self.i["close"]):
            return None
        if self.i["month_first"][d + 1]:                          # 내일이 새 달 첫 거래일 → 내일 1/남은 횟수
            return ("buy", 1.0 / (self.k - self.done))
        return None


class Dip10(Strategy):
    key, kind = "dip10", "entry"

    def __init__(self, ind, drop=0.10):
        super().__init__(ind)
        self.drop = drop

    def decide(self, d):
        if self.holding or d < 0:
            return None
        return ("buy", 1.0) if _le(self.i["close"][d], (1 - self.drop) * self.i["ath"][d]) else None


class Ladder(Strategy):
    key, kind = "ladder", "entry"

    def __init__(self, ind, levels=(0.10, 0.20, 0.30)):
        super().__init__(ind)
        self.levels, self.bought = levels, 0                     # 산 칸 수 (1 = 시작일 1/4)

    def _need(self, d):
        dd = 1 - self.i["close"][d] / self.i["ath"][d] if d >= 0 else 0.0
        return 1 + sum(dd >= lv - _TOL for lv in self.levels)

    def start(self, s):
        need = self._need(s - 1)
        self._pending = need
        return ("buy", need / 4.0)

    def on_fill(self, d, side):
        super().on_fill(d, side)
        self.bought = self._pending

    def decide(self, d):
        if self.bought >= 4:
            return None
        need = max(self._need(d), self.bought)
        if need > self.bought:
            self._pending = need
            return ("buy", (need - self.bought) / (4.0 - self.bought))
        return None


class Stop10(Strategy):
    key = "stop10"

    def __init__(self, ind, down=0.10, up=0.10):
        super().__init__(ind)
        self.down, self.up, self.ref = down, up, None

    def start(self, s):
        return ("buy", 1.0)

    def on_fill(self, d, side):
        super().on_fill(d, side)
        self.ref = self.i["close"][d]                           # 보유 중엔 최고가, 현금일 땐 최저가

    def decide(self, d):
        p = self.i["close"][d]
        if self.holding:
            self.ref = max(self.ref, p)
            return ("sell", 1.0) if _le(p, (1 - self.down) * self.ref) else None
        self.ref = min(self.ref, p)
        return ("buy", 1.0) if _ge(p, (1 + self.up) * self.ref) else None


class TP10(Strategy):
    key = "tp10"

    def __init__(self, ind, gain=0.10, drop=0.10):
        super().__init__(ind)
        self.gain, self.drop, self.entry, self.high = gain, drop, None, None

    def start(self, s):
        return ("buy", 1.0)

    def on_fill(self, d, side):
        super().on_fill(d, side)
        if side == "buy":
            self.entry = self.i["close"][d]
        else:
            self.high = self.i["close"][d]

    def decide(self, d):
        p = self.i["close"][d]
        if self.holding:
            return ("sell", 1.0) if _ge(p, (1 + self.gain) * self.entry) else None
        self.high = max(self.high, p)
        return ("buy", 1.0) if _le(p, (1 - self.drop) * self.high) else None


class StateRule(Strategy):
    """그날 상태(want: 보유/현금)만으로 정하는 전략 — 상태가 바뀔 때 사고판다."""

    def want(self, d):
        raise NotImplementedError

    def decide(self, d):
        w = self.want(d)
        if w is None:
            return None
        if w and not self.holding:
            return ("buy", 1.0)
        if not w and self.holding:
            return ("sell", 1.0)
        return None


class SMA200(StateRule):
    key = "sma200"

    def want(self, d):
        m = self.i["sma200"][d]
        return None if np.isnan(m) else bool(self.i["close"][d] > m)


class GC50_200(StateRule):
    key = "gc50_200"

    def want(self, d):
        a, b = self.i["sma50"][d], self.i["sma200"][d]
        return None if np.isnan(b) else bool(a > b)


class Mom12(StateRule):
    key = "mom12"

    def __init__(self, ind):
        super().__init__(ind)
        me = np.where(ind["month_end"] & ~np.isnan(ind["mom12"]))[0]
        last = np.full(len(ind["close"]), -1)                     # d 에 알고 있는 가장 최근 달 마지막 날
        last[me] = me
        self.last_me = np.maximum.accumulate(last)

    def want(self, d):
        k = self.last_me[d] if d >= 0 else -1
        return None if k < 0 else bool(self.i["mom12"][k] > 0)

    def start(self, s):
        return super().decide(s - 1)                             # 가장 최근 달 마지막 날의 판단으로 시작

    def decide(self, d):
        return super().decide(d) if self.i["month_end"][d] else None   # 달 마지막 거래일에만 판단 → 다음 달 첫 거래일에 사고팖


class Breakout(Strategy):
    key = "brk55_20"

    def decide(self, d):
        p, hi, lo = self.i["close"][d], self.i["hi55"][d], self.i["lo20"][d]
        if np.isnan(hi) or np.isnan(lo):
            return None
        if not self.holding:
            return ("buy", 1.0) if p > hi else None
        return ("sell", 1.0) if p < lo else None

    def start(self, s):
        return None                                              # 처음엔 현금 — 첫 돌파를 기다림


class RSI3070(Strategy):
    key = "rsi30_70"

    def decide(self, d):
        r = self.i["rsi14"][d]
        if np.isnan(r):
            return None
        if not self.holding:
            return ("buy", 1.0) if r < 30 else None
        return ("sell", 1.0) if r > 70 else None

    def start(self, s):
        return None                                              # 처음엔 현금 — 첫 과매도(30 미만)를 기다림


STRATEGIES = {c.key: c for c in (Hold, DCA12, Dip10, Ladder, Stop10, TP10, SMA200, GC50_200, Breakout, RSI3070, Mom12)}
ORDER = ["dca12", "dip10", "ladder", "stop10", "tp10", "sma200", "gc50_200", "brk55_20", "rsi30_70", "mom12"]


# ----------------------------------------------------------------------------- 시뮬레이션
@dataclass
class Run:
    key: str
    dates: pd.DatetimeIndex
    value: np.ndarray            # 그날 종가 기준 평가 금액
    stock_share: np.ndarray      # 평가 금액 중 주식 비율 (0~1)
    fills: list = field(default_factory=list)   # dict(date, side, frac, amount, price, tr, value_after)
    trades: list = field(default_factory=list)  # 사고팔기 한 번 = dict(buy_date, sell_date, ret, days, open)


def simulate(key, ind, tr, s, e, capital=10_000.0, cost=0.001, cash_ret=None, record=True):
    """거래일 s~e 동안 전략 key 를 돌린다 (s 종가에 첫 거래). → Run."""
    strat = STRATEGIES[key](ind)
    trv = tr if isinstance(tr, np.ndarray) else np.asarray(tr, float)
    n = e - s + 1
    val = np.empty(n)
    share = np.empty(n)
    cash, units = float(capital), 0.0
    fills, trades = [], []
    open_buy = None                                              # (날짜 위치, tr, 비용 뺀 들어간 돈) — 사고팔기 반복 전략의 열린 거래
    pending = strat.start(s)
    cr = cash_ret
    for j in range(n):
        d = s + j
        if j > 0 and cr is not None:
            cash *= 1.0 + cr[d]
        if pending is not None:
            side, frac = pending
            if side == "buy" and cash > 0:
                amt = cash * frac
                units += amt * (1.0 - cost) / trv[d]
                cash -= amt
                strat.on_fill(d, "buy")
                if record:
                    fills.append({"i": d, "side": "buy", "frac": frac, "amount": amt})
                if strat.kind == "inout":
                    open_buy = (d, trv[d])
            elif side == "sell" and units > 0:
                amt = units * trv[d]
                cash += amt * (1.0 - cost)
                units = 0.0
                strat.on_fill(d, "sell")
                if record:
                    fills.append({"i": d, "side": "sell", "frac": 1.0, "amount": amt})
                if open_buy is not None:
                    trades.append({"buy_i": open_buy[0], "sell_i": d, "ret": trv[d] / open_buy[1] * (1 - cost) ** 2 - 1.0,
                                   "days": d - open_buy[0], "open": False})
                    open_buy = None
        sv = units * trv[d]
        val[j] = cash + sv
        share[j] = sv / val[j] if val[j] > 0 else 0.0
        pending = strat.decide(d) if d < e else None
    if open_buy is not None:
        trades.append({"buy_i": open_buy[0], "sell_i": e, "ret": trv[e] / open_buy[1] * (1 - cost) - 1.0,
                       "days": e - open_buy[0], "open": True})
    return Run(key, ind["_index"][s:e + 1] if "_index" in ind else None, val, share, fills, trades)


def stats(run, capital=10_000.0):
    v = run.value
    yrs = (run.dates[-1] - run.dates[0]).days / 365.25
    peak = np.maximum.accumulate(v)
    dd = v / peak - 1.0
    r = np.diff(v) / v[:-1]
    closed = [t for t in run.trades if not t["open"]]
    cash_runs, cur = [], 0
    for x in run.stock_share:
        cur = cur + 1 if x < 1e-9 else 0
        cash_runs.append(cur)
    out = {"final": float(v[-1]), "total_return": float(v[-1] / capital - 1), "cagr": float((v[-1] / capital) ** (1 / yrs) - 1),
           "mdd": float(dd.min()), "mdd_date": str(run.dates[int(dd.argmin())].date()),
           "vol": float(r.std(ddof=1) * np.sqrt(TRADING_DAYS)), "exposure": float(run.stock_share.mean()),
           "buys": sum(f["side"] == "buy" for f in run.fills), "sells": sum(f["side"] == "sell" for f in run.fills),
           "round_trips": len(closed), "win_rate": float(np.mean([t["ret"] > 0 for t in closed])) if closed else None,
           "avg_trade": float(np.mean([t["ret"] for t in closed])) if closed else None,
           "best_trade": float(max(t["ret"] for t in closed)) if closed else None,
           "worst_trade": float(min(t["ret"] for t in closed)) if closed else None,
           "longest_cash_days": int(max(cash_runs) if cash_runs else 0), "years": round(yrs, 2)}
    out["sharpe0"] = float(r.mean() / r.std(ddof=1) * np.sqrt(TRADING_DAYS)) if r.std() > 0 else None
    return out


def prepare(close, tr):
    """지표 + 날짜(index) 를 한 dict 로."""
    ind = indicators(close)
    ind["_index"] = close.index
    return ind, np.asarray(tr, float)


def run_all(close, tr, start, end, keys=None, capital=10_000.0, cost=0.001, cash_ret=None, label="main"):
    """[start, end] 날짜 안의 첫·마지막 거래일로 hold + 전략들 → {key: (Run, stats)}."""
    ind, trv = prepare(close, tr)
    idx = close.index
    s = int(idx.searchsorted(pd.Timestamp(start)))
    e = int(idx.searchsorted(pd.Timestamp(end), side="right") - 1)
    if s < 1 or e <= s:
        raise ValueError(f"[TRADE] 기간이 자료 밖: {start}~{end} (자료 {idx[0].date()}~{idx[-1].date()}, 첫날 앞에 하루 이상 필요)")
    t0 = time.time()
    out = {}
    for k in ["hold"] + (keys or ORDER):
        run = simulate(k, ind, trv, s, e, capital, cost, cash_ret)
        out[k] = (run, stats(run, capital))
    h = out["hold"][1]
    log("TRADE", label=label, start=str(idx[s].date()), end=str(idx[e].date()), days=e - s + 1, cost=cost,
        cash="0" if cash_ret is None else "rate", hold_final=f"{h['final']:.0f}", seconds=f"{time.time() - t0:.2f}")
    for k in (keys or ORDER):
        st = out[k][1]
        log("RESULT", label=label, strategy=k, final=f"{st['final']:.0f}", vs_hold=f"{st['final'] / h['final'] - 1:+.1%}",
            cagr=f"{st['cagr']:.2%}", mdd=f"{st['mdd']:.1%}", exposure=f"{st['exposure']:.0%}", buys=st["buys"], sells=st["sells"])
    return out


def rolling(close, tr, first_start, last_start, years=10, keys=None, capital=10_000.0, cost=0.001, cash_ret=None, label="rolling"):
    """매달 첫 거래일에 시작하는 years 년 기간마다 hold 와 전략들의 끝 값 → DataFrame(시작일 × 전략).
    끝 = 시작일 + years 년 바로 전 거래일. 기간마다 전략을 처음 상태로 다시 시작한다."""
    ind, trv = prepare(close, tr)
    idx = close.index
    month = idx.to_period("M")
    firsts = np.where(np.r_[True, month[1:] != month[:-1]])[0]
    firsts = [i for i in firsts if pd.Timestamp(first_start) <= idx[i] <= pd.Timestamp(last_start)]
    rows = []
    t0 = time.time()
    for s in firsts:
        end_date = idx[s] + pd.DateOffset(years=years)
        e = int(idx.searchsorted(end_date) - 1)
        if e >= len(idx) or idx[e] < end_date - pd.Timedelta(days=10):
            continue
        row = {"start": idx[s], "end": idx[e]}
        for k in ["hold"] + (keys or ORDER):
            r = simulate(k, ind, trv, s, e, capital, cost, cash_ret, record=False)
            row[k] = r.value[-1]
            v = r.value
            row[k + "_mdd"] = float((v / np.maximum.accumulate(v) - 1).min())
        rows.append(row)
    df = pd.DataFrame(rows)
    log("TRADE", label=label, windows=len(df), years=years, first=str(df["start"].iloc[0].date()), last=str(df["start"].iloc[-1].date()),
        seconds=f"{time.time() - t0:.1f}")
    return df
