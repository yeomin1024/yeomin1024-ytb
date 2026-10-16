#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.2 — 2026-10-16 — facts 절 (대본 문장마다 숫자 근거): 현금으로 기다린 가장 긴 기간(전략별 3개), 2020년 코로나 구간 사고판 날,
#          분할 매수 1991년 지수 변화·평균 산 값, 하락 분할 매수가 남은 돈을 넣기까지 지수 변화, 10년 기간 가장 좋을 때·나쁠 때 시작일,
#          10년 기간을 '관망이 그 기간 안에 40%(확인 35%) 넘게 떨어졌나'로 나눈 이긴 수 (시작 시기 나누기보다 까닭이 바로 보임).
# (v1.1 — 2026-10-16 — analysis 절 더함 (대본 숫자 근거): 큰 하락 구간(관망 낙폭 19% 넘게)마다 전략별 낙폭·회복, 관망 대비 앞선 날·
#          가장 앞선 때·마지막으로 앞선 날, 10년 기간을 시작 시기(1991–1999 · 2000–2008 · 2009–2013)로 나눈 이긴 수, 관망과 같은 기간 수(ties).
# (v1.0 — 2026-10-16 — 최초.) 사용자 지시 2026-10-16 "흔히 사용하는 매수 전략을 10가지 정도 골라서 그냥 매수하고 관망하는거랑
#          비교(투자 금액은 변동없이 동일하게)하면 이게 시청자들이 원하는 언제 사야할까를 만족하는거 아니야? … 이걸 위한 티커, 테스트 기간을
#          적당하게 잡아보고 보완할게 있으면 보완해 … 마지막은 종합 통계내서 결론".
"""주식 1번 (v2) — 매수 전략 10가지 vs 매수 후 관망 백테스트 (연구·교육용 — 투자 권유가 아니다. 과거 결과는 미래를 보장하지 않는다).

  cd stock/source/eonje-maesu-2026-10/backtest && python3 run.py          # → results.json · results.md · trades.csv · rolling_10y.csv · run.log

정한 것 (결과를 보기 전에 정함 — 바꾸면 바꾼 것을 README 에 적는다):
  자산(티커)   S&P 500 지수 총수익 (배당 재투자) — SPY·VOO·IVV 가 따라가는 지수. 종목·상품 추천이 아님
  기간         1991-01-02 ~ 2023-06-30 (32.5년: 걸프전 뒤 · 닷컴 · 금융위기 · 코로나 · 2022 하락 포함).
               시작이 1991 인 까닭: 일별 자료 첫날 1990-01-02 + 200일선을 만들 1년. 끝이 2023-06 인 까닭: 배당 자료(Shiller)가 있는 마지막 달
  돈           $10,000 를 시작일에 한 번 — 전략과 관망 모두 같은 돈, 더 넣거나 빼지 않음
  사고팔기     신호는 그날 종가까지만 보고 다음 거래일 종가에 (미래 정보 금지), 매매 비용 0.1% (사고팔 때마다), 현금 이자 0
  여러 시작    10년 기간을 1991-01 부터 매달 시작 (271번) — 전략마다 관망보다 끝 값이 큰 기간 수
  확인         비용 0 · 현금에 T-bill 이자(1991-01~2018-11, Fama-French RF) · 현금에 10년 국채 금리(위쪽 한계) · 가격만 2026-02 까지 ·
               나스닥 종합(가격만) 2000-01~2018-12 · 20년 기간
빠진 것: 세금(매도할 때마다 내는 양도세 — 자주 사고파는 전략에 더 불리), 환율, ETF 보수(약 0.03~0.1%/년, 모두 같음), 호가 차이.
"""
import json
import logging
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / "tools"))
from backtest import daily as dl  # noqa: E402
from backtest import data as bd  # noqa: E402

VERSION = "v1.2"
CAPITAL, COST = 10_000.0, 0.001
MAIN = ("1991-01-02", "2023-06-30")
ROLL_FIRST, ROLL_LAST = "1991-01-01", "2013-07-31"
NAMES = {"hold": "매수 후 관망", "dca12": "12개월 분할 매수", "dip10": "고점 대비 −10% 저점 매수", "ladder": "하락 분할 매수(물타기) ¼씩 −10·−20·−30%",
         "stop10": "손절 −10% · 반등 +10% 재매수", "tp10": "익절 +10% · −10% 재매수", "sma200": "200일 이동평균선", "gc50_200": "골든·데드 크로스 50/200",
         "brk55_20": "신고가 돌파 55일 · 20일 저점 매도", "rsi30_70": "RSI 30 매수 · 70 매도", "mom12": "12개월 모멘텀"}


def setup_log():
    fmt = logging.Formatter("%(message)s")
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    for h in (logging.StreamHandler(sys.stdout), logging.FileHandler(HERE / "run.log", "w", "utf-8")):
        h.setFormatter(fmt)
        root.addHandler(h)


def log(stage, **kv):
    dl.log(stage, **kv)


def load():
    close, meta_c = bd.sp500_daily_long()
    mon, meta_m = bd.sp500_monthly()
    rf, meta_rf = bd.ff_rf_monthly()
    nq, meta_n = bd.nasdaq_daily()
    div_until = pd.Timestamp(meta_m["dividend_until"]) + pd.offsets.MonthEnd(0)
    c_tr = close.loc[: div_until]
    tr = dl.tr_index_daily(c_tr, mon["dividend"].dropna())
    log("DATA", sp500_daily=f"{close.index[0].date()}~{close.index[-1].date()}", rows=len(close), tr_until=str(c_tr.index[-1].date()),
        nasdaq=f"{nq.index[0].date()}~{nq.index[-1].date()}", rf=f"{rf.index[0].date()}~{rf.index[-1].date()}")
    return close, c_tr, tr, mon, rf, nq, {"sp500_daily": meta_c, "sp500_monthly": meta_m, "ff_rf": meta_rf, "nasdaq_daily": meta_n}


def check_tr_against_monthly(tr, mon):
    """일별 총수익 지수의 연율을 월별(Shiller 월평균 가격) 총수익 지수와 맞춰 본다 — 같은 배당 자료, 가격만 일별 vs 월평균."""
    from backtest import monthly as bm
    m = mon.loc["1991-01-01":"2023-06-01"].dropna(subset=["dividend"])
    tri = bm.total_return_index(m["price"].to_numpy(), m["dividend"].to_numpy())
    yrs_m = (len(tri) - 1) / 12
    cagr_m = tri[-1] ** (1 / yrs_m) - 1
    t = tr.loc["1991-01-02":"2023-06-30"]
    yrs_d = (t.index[-1] - t.index[0]).days / 365.25
    cagr_d = (t.iloc[-1] / t.iloc[0]) ** (1 / yrs_d) - 1
    log("VALIDATE", check="일별 총수익 vs 월별 총수익 (1991~2023-06)", daily_cagr=f"{cagr_d:.3%}", monthly_cagr=f"{cagr_m:.3%}",
        diff_pp=f"{(cagr_d - cagr_m) * 100:+.3f}")
    if abs(cagr_d - cagr_m) > 0.003:
        raise RuntimeError("[VALIDATE] 일별·월별 총수익 연율 차이가 0.3%p 를 넘음 → 배당 나누기 확인")
    return {"daily_cagr": cagr_d, "monthly_cagr": cagr_m}


def pack(res, close_idx):
    """run_all 결과 → JSON 용 dict (stats + 거래 기록)."""
    out = {}
    for k, (run, st) in res.items():
        trades = [{"buy": str(close_idx[t["buy_i"]].date()), "sell": str(close_idx[t["sell_i"]].date()), "ret": round(t["ret"], 6),
                   "days": t["days"], "open": t["open"]} for t in run.trades]
        fills = [{"date": str(close_idx[f["i"]].date()), "side": f["side"], "frac": round(f["frac"], 6), "amount": round(f["amount"], 2)}
                 for f in run.fills]
        out[k] = {"name": NAMES[k], "stats": st, "fills": fills, "trades": trades}
    return out


def summary_vs_hold(res):
    h = res["hold"][1]
    rows = []
    for k in dl.ORDER:
        st = res[k][1]
        rows.append({"key": k, "final": st["final"], "vs_hold_pct": st["final"] / h["final"] - 1, "cagr": st["cagr"], "mdd": st["mdd"],
                     "beat_hold": st["final"] > h["final"], "mdd_better": st["mdd"] > h["mdd"]})
    return {"hold_final": h["final"], "hold_cagr": h["cagr"], "hold_mdd": h["mdd"], "beat": sum(r["beat_hold"] for r in rows),
            "mdd_better": sum(r["mdd_better"] for r in rows), "rows": rows}


ERAS = (("1991-1999", "1991-01-01", "1999-12-31"), ("2000-2008", "2000-01-01", "2008-12-31"), ("2009-2013", "2009-01-01", "2013-12-31"))


def rolling_summary(df, eras=None):
    out = {"windows": int(len(df)), "first_start": str(df["start"].iloc[0].date()), "last_start": str(df["start"].iloc[-1].date())}
    if eras:
        out["eras"] = {}
        for name, a, b in eras:
            sub = df[(df["start"] >= a) & (df["start"] <= b)]
            out["eras"][name] = {"windows": int(len(sub)), **{k: int((sub[k] > sub["hold"] * (1 + 1e-9)).sum()) for k in dl.ORDER}}
    if "hold_mdd" in df:
        out["by_hold_mdd"] = {}
        for thr in (0.40, 0.35):
            big, small = df[df["hold_mdd"] <= -thr], df[df["hold_mdd"] > -thr]
            out["by_hold_mdd"][f"{thr:.2f}"] = {
                "big_windows": int(len(big)), "small_windows": int(len(small)), "small_worst_hold_mdd": float(small["hold_mdd"].min()),
                "big": {k: int((big[k] > big["hold"] * (1 + 1e-9)).sum()) for k in dl.ORDER},
                "small": {k: int((small[k] > small["hold"] * (1 + 1e-9)).sum()) for k in dl.ORDER}}
    for k in dl.ORDER:
        rel = df[k] / df["hold"] - 1
        out[k] = {"wins": int((rel > 1e-9).sum()), "ties": int((rel.abs() <= 1e-9).sum()), "median_vs_hold": float(rel.median()), "best_vs_hold": float(rel.max()),
                  "worst_vs_hold": float(rel.min()), "mdd_better": int((df[k + "_mdd"] > df["hold_mdd"]).sum()),
                  "median_mdd": float(df[k + "_mdd"].median())}
    out["hold_median_mdd"] = float(df["hold_mdd"].median())
    return out


def crashes(res, min_dd=0.19):
    """관망 평가 금액이 고점보다 min_dd 넘게 떨어진 구간 → 고점·바닥·회복 날짜와 전략별 그 구간 변화 (코드가 찾음 — 손으로 고르지 않음)."""
    h = res["hold"][0]
    v, dates = h.value, h.dates
    peak = np.maximum.accumulate(v)
    dd = v / peak - 1
    out, i, n = [], 0, len(v)
    while i < n:
        if dd[i] < -min_dd:
            j = i
            while j < n and dd[j] < 0:
                j += 1
            t = i + int(np.argmin(dd[i:j]))
            p0 = int(np.where(v[: t + 1] == peak[t])[0][-1])
            rec = min(j, n - 1)
            e = {"peak": str(dates[p0].date()), "trough": str(dates[t].date()), "recovered": str(dates[rec].date()) if j < n else None,
                 "hold_drop": float(v[t] / v[p0] - 1), "strategies": {}}
            for k in dl.ORDER:
                vv = res[k][0].value
                e["strategies"][k] = {"drop": float(vv[t] / vv[p0] - 1), "rebound_to_hold_recovery": float(vv[rec] / vv[t] - 1),
                                      "stock_share_at_trough": float(res[k][0].stock_share[t])}
            out.append(e)
            i = j
        else:
            i += 1
    for e in out:
        log("RESULT", crash=f"{e['peak']}→{e['trough']}", hold=f"{e['hold_drop']:+.1%}",
            **{k: f"{x['drop']:+.1%}" for k, x in e["strategies"].items()})
    return out


def leads(res):
    """전략 평가 금액 ÷ 관망 평가 금액의 흐름: 앞선 날 비율·가장 앞섰을 때·가장 뒤졌을 때·마지막으로 앞선 날."""
    h = res["hold"][0]
    out = {}
    for k in dl.ORDER:
        r = res[k][0].value / h.value
        ahead = np.where(r > 1 + 1e-9)[0]
        out[k] = {"days_ahead": float((r > 1 + 1e-9).mean()), "max_ratio": float(r.max()), "max_date": str(h.dates[int(r.argmax())].date()),
                  "min_ratio": float(r.min()), "min_date": str(h.dates[int(r.argmin())].date()), "final_ratio": float(r[-1]),
                  "last_ahead": str(h.dates[ahead[-1]].date()) if len(ahead) else None,
                  "first_ahead": str(h.dates[ahead[0]].date()) if len(ahead) else None}
    return out


def facts(res, close, tr, roll10):
    """대본이 말하는 숫자들 (모두 이 함수 출력 — 손으로 계산하지 않음)."""
    h = res["hold"][0]
    dates = h.dates
    out = {"cash_spells": {}, "fills_2020": {}, "worst_best_10y_start": {}}
    for k in dl.ORDER:
        run = res[k][0]
        z = run.stock_share < 1e-9
        spells, i, n = [], 0, len(z)
        while i < n:
            if z[i]:
                j = i
                while j < n and z[j]:
                    j += 1
                spells.append({"from": str(dates[i].date()), "to": str(dates[j - 1].date()), "trading_days": int(j - i),
                               "calendar_days": int((dates[j - 1] - dates[i]).days) + 1})
                i = j
            else:
                i += 1
        out["cash_spells"][k] = sorted(spells, key=lambda x: -x["trading_days"])[:3]
        out["fills_2020"][k] = [{"date": str(close.index[f["i"]].date()), "side": f["side"]}
                                for f in run.fills if "2020-01-01" <= str(close.index[f["i"]].date()) <= "2020-12-31"]
        rel = roll10[k] / roll10["hold"] - 1
        out["worst_best_10y_start"][k] = {"worst": float(rel.min()), "worst_start": str(roll10["start"].iloc[int(rel.idxmin())].date()),
                                          "best": float(rel.max()), "best_start": str(roll10["start"].iloc[int(rel.idxmax())].date())}
    c91 = close.loc["1991-01-01":"1991-12-31"]
    dca = res["dca12"][0]
    buys = [f for f in dca.fills if f["side"] == "buy"]
    trv = np.asarray(tr, float)
    s0 = buys[0]["i"]
    avg_tr = sum(f["amount"] for f in buys) / sum(f["amount"] / trv[f["i"]] for f in buys)
    out["dca12"] = {"first_buy": str(close.index[buys[0]["i"]].date()), "last_buy": str(close.index[buys[-1]["i"]].date()),
                    "index_1991_change": float(c91.iloc[-1] / c91.iloc[0] - 1), "index_first_to_last_buy": float(close.iloc[buys[-1]["i"]] / close.iloc[s0] - 1),
                    "avg_cost_vs_first_day": float(avg_tr / trv[s0] - 1)}
    lad = res["ladder"][0]
    lb = [f for f in lad.fills if f["side"] == "buy"]
    out["ladder"] = {"buys": [{"date": str(close.index[f["i"]].date()), "share_of_start": round(f["amount"] / CAPITAL, 4)} for f in lb],
                     "tr_growth_start_to_3rd_buy": float(trv[lb[1]["i"]] / trv[lb[0]["i"]]) if len(lb) > 1 else None,
                     "tr_growth_start_to_last_buy": float(trv[lb[-1]["i"]] / trv[lb[0]["i"]])}
    log("RESULT", facts="cash_spells,fills_2020,dca12,ladder,worst_best_10y_start",
        dca_1991=f"{out['dca12']['index_1991_change']:+.1%}", ladder_wait_growth=f"×{out['ladder']['tr_growth_start_to_3rd_buy']:.2f}",
        tp10_longest_cash=out["cash_spells"]["tp10"][0] if out["cash_spells"]["tp10"] else "-")
    return out


def main():
    setup_log()
    t0 = time.time()
    log("START", tool=f"run.py {VERSION}", engine=f"daily.py {dl.VERSION}", capital=CAPITAL, cost=COST, main=f"{MAIN[0]}~{MAIN[1]}",
        note="연구·교육용 — 투자 권유 아님")
    close, c_tr, tr, mon, rf, nq, metas = load()
    chk = check_tr_against_monthly(tr, mon)

    # 1) 본 실험: S&P500 총수익, 1991-01-02~2023-06-30, 비용 0.1%, 현금 이자 0
    main_res = dl.run_all(c_tr, tr, *MAIN, capital=CAPITAL, cost=COST, label="main")
    idx = c_tr.index

    # 2) 확인들
    sens = {}
    sens["cost0"] = summary_vs_hold(dl.run_all(c_tr, tr, *MAIN, capital=CAPITAL, cost=0.0, label="cost0"))
    sub = ("1991-01-02", "2018-11-30")
    c_sub, tr_sub = c_tr.loc[:sub[1]], tr.loc[:sub[1]]
    rf_arr = dl.cash_daily(c_sub.index, rf.loc[str(c_sub.index[0].date())[:7] + "-01":], "month_pct")
    sens["tbill_sub_cash0"] = summary_vs_hold(dl.run_all(c_sub, tr_sub, *sub, capital=CAPITAL, cost=COST, label="sub_cash0"))
    sens["tbill_sub_cashRF"] = summary_vs_hold(dl.run_all(c_sub, tr_sub, *sub, capital=CAPITAL, cost=COST, cash_ret=rf_arr, label="sub_cashRF"))
    gs10 = dl.cash_daily(c_tr.index, mon["long_rate"].loc["1990-01-01":"2023-06-01"], "annual_pct")
    sens["cash_gs10"] = summary_vs_hold(dl.run_all(c_tr, tr, *MAIN, capital=CAPITAL, cost=COST, cash_ret=gs10, label="cash_gs10"))
    sens["price_only_2026"] = summary_vs_hold(dl.run_all(close, close, "1991-01-02", str(close.index[-1].date()), capital=CAPITAL, cost=COST,
                                                         label="price_only_2026"))
    sens["nasdaq_price_2000_2018"] = summary_vs_hold(dl.run_all(nq, nq, "2000-01-03", "2018-12-31", capital=CAPITAL, cost=COST, label="nasdaq"))
    sens["nasdaq_price_2003_2018"] = summary_vs_hold(dl.run_all(nq, nq, "2003-01-02", "2018-12-31", capital=CAPITAL, cost=COST, label="nasdaq_2003"))

    # 3) 여러 시작 시점: 10년 기간 매달 (S&P500 총수익) + 20년 + 나스닥 10년
    roll10 = dl.rolling(c_tr, tr, ROLL_FIRST, ROLL_LAST, years=10, capital=CAPITAL, cost=COST, label="rolling_10y")
    roll10.to_csv(HERE / "rolling_10y.csv", index=False, float_format="%.6f", date_format="%Y-%m-%d")
    roll20 = dl.rolling(c_tr, tr, ROLL_FIRST, "2003-07-31", years=20, capital=CAPITAL, cost=COST, label="rolling_20y")
    rollnq = dl.rolling(nq, nq, "2000-01-01", "2009-01-31", years=10, capital=CAPITAL, cost=COST, label="rolling_nasdaq_10y")

    main_pack = pack(main_res, idx)
    rows = []
    for k, v in main_pack.items():
        for t in v["trades"]:
            rows.append({"strategy": k, **t})
    pd.DataFrame(rows).to_csv(HERE / "trades.csv", index=False)
    results = {
        "version": VERSION, "engine": dl.VERSION, "created": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "settings": {"asset": "S&P 500 총수익 지수 (배당 재투자)", "main": MAIN, "capital": CAPITAL, "cost": COST, "cash": 0.0,
                     "execution": "신호 다음 거래일 종가", "rolling": {"years": 10, "first": ROLL_FIRST, "last": ROLL_LAST}},
        "data": {k: {kk: vv for kk, vv in m.items() if kk not in ("validate",)} for k, m in metas.items()},
        "checks": {"tr_daily_vs_monthly": chk},
        "main": main_pack, "main_summary": summary_vs_hold(main_res),
        "rolling_10y": rolling_summary(roll10, ERAS), "rolling_20y": rolling_summary(roll20), "rolling_nasdaq_10y": rolling_summary(rollnq),
        "analysis": {"crashes": crashes(main_res), "leads": leads(main_res)},
        "facts": facts(main_res, c_tr, tr, roll10),
        "sensitivity": sens,
    }
    (HERE / "results.json").write_text(json.dumps(results, ensure_ascii=False, indent=1, default=str), "utf-8")
    write_md(results)
    log("DONE", seconds=f"{time.time() - t0:.1f}", files="results.json,results.md,trades.csv,rolling_10y.csv,run.log")


def pct(x, d=1):
    return "—" if x is None else f"{x * 100:+.{d}f}%"


def write_md(r):
    L = [f"# 매수 전략 10가지 vs 매수 후 관망 — 결과 (`run.py` {r['version']}, 엔진 `daily.py` {r['engine']}, {r['created']})", "",
         "> 연구·교육용. 투자 권유가 아니다. 과거 결과는 미래를 보장하지 않는다. 숫자는 이 파일·`results.json` 의 코드 출력만 쓴다.", "",
         f"- 자산: {r['settings']['asset']} · 기간 {r['settings']['main'][0]} ~ {r['settings']['main'][1]} · 시작 돈 ${r['settings']['capital']:,.0f} (모두 같음, 더 넣지 않음)",
         f"- 사고팔기: {r['settings']['execution']} · 비용 {r['settings']['cost']:.1%} · 현금 이자 0", "",
         "## 1. 본 실험 (한 번, 1991-01-02 → 2023-06-30)", "",
         "| 전략 | 끝 값 | 관망 대비 | 연율 | 최대 낙폭 | 주식 비율 | 매수·매도 | 거래 승률 | 가장 긴 현금 |", "|---|---:|---:|---:|---:|---:|---:|---:|---:|"]
    h = r["main"]["hold"]["stats"]
    for k in ["hold"] + list(dl.ORDER):
        st = r["main"][k]["stats"]
        L.append(f"| {r['main'][k]['name']} | ${st['final']:,.0f} | {pct(st['final'] / h['final'] - 1) if k != 'hold' else '—'} | {st['cagr']:.2%} | "
                 f"{st['mdd']:.1%} ({st['mdd_date']}) | {st['exposure']:.0%} | {st['buys']}·{st['sells']} | "
                 f"{'—' if st['win_rate'] is None else f'{st['win_rate']:.0%}'} | {st['longest_cash_days']}일 |")
    s = r["main_summary"]
    L += ["", f"- 관망보다 끝 값이 큰 전략: **{s['beat']} / 10** · 최대 낙폭이 관망보다 작은 전략: **{s['mdd_better']} / 10**", "",
          f"## 2. 여러 시작 시점 — 10년 기간 {r['rolling_10y']['windows']}번 ({r['rolling_10y']['first_start']} ~ {r['rolling_10y']['last_start']} 시작)", "",
          "| 전략 | 관망보다 많은 기간 | 가운데 값(관망 대비) | 가장 좋을 때 | 가장 나쁠 때 | 낙폭이 더 작은 기간 | 낙폭 가운데 값 |", "|---|---:|---:|---:|---:|---:|---:|"]
    for k in dl.ORDER:
        x = r["rolling_10y"][k]
        L.append(f"| {r['main'][k]['name']} | {x['wins']} / {r['rolling_10y']['windows']} | {pct(x['median_vs_hold'])} | {pct(x['best_vs_hold'])} | "
                 f"{pct(x['worst_vs_hold'])} | {x['mdd_better']} / {r['rolling_10y']['windows']} | {x['median_mdd']:.1%} |")
    L.append(f"| 매수 후 관망 | — | — | — | — | — | {r['rolling_10y']['hold_median_mdd']:.1%} |")
    er = r["rolling_10y"]["eras"]
    L += ["", "### 시작 시기별 — 관망보다 많은 기간", "", "| 전략 | " + " | ".join(f"{k} 시작 ({v['windows']}번)" for k, v in er.items()) + " | 관망과 같음 |",
          "|---|" + "---:|" * (len(er) + 1)]
    for k in dl.ORDER:
        L.append(f"| {r['main'][k]['name']} | " + " | ".join(str(v[k]) for v in er.values()) + f" | {r['rolling_10y'][k]['ties']} |")
    for thr, x in r["rolling_10y"]["by_hold_mdd"].items():
        L += ["", f"### 관망이 그 기간 안에 {float(thr):.0%} 넘게 떨어진 기간({x['big_windows']}번) vs 아닌 기간({x['small_windows']}번, 그 안 관망 최대 낙폭 {x['small_worst_hold_mdd']:.1%})", "",
              "| 전략 | 큰 하락이 있던 기간에서 관망보다 많음 | 없던 기간에서 관망보다 많음 |", "|---|---:|---:|"]
        for k in dl.ORDER:
            L.append(f"| {r['main'][k]['name']} | {x['big'][k]} / {x['big_windows']} | {x['small'][k]} / {x['small_windows']} |")
    L += ["", "## 2-1. 큰 하락 구간 (관망 평가 금액이 고점보다 19% 넘게 — 코드가 찾음)", "",
          "| 구간 (고점 → 바닥) | 관망 | " + " | ".join(r["main"][k]["name"].split(" ")[0] for k in dl.ORDER) + " |", "|---|---:|" + "---:|" * len(dl.ORDER)]
    for e in r["analysis"]["crashes"]:
        L.append(f"| {e['peak']} → {e['trough']} | {e['hold_drop']:+.1%} | " + " | ".join(f"{e['strategies'][k]['drop']:+.1%}" for k in dl.ORDER) + " |")
    L += ["", "## 2-2. 관망과 비교한 흐름 (전략 ÷ 관망)", "", "| 전략 | 앞선 날 | 가장 앞섰을 때 | 가장 뒤졌을 때 | 마지막으로 앞선 날 | 끝 |", "|---|---:|---:|---:|---:|---:|"]
    for k in dl.ORDER:
        x = r["analysis"]["leads"][k]
        L.append(f"| {r['main'][k]['name']} | {x['days_ahead']:.0%} | ×{x['max_ratio']:.2f} ({x['max_date']}) | ×{x['min_ratio']:.2f} ({x['min_date']}) | {x['last_ahead'] or '—'} | ×{x['final_ratio']:.3f} |")
    for key, title in (("rolling_20y", "20년 기간"), ("rolling_nasdaq_10y", "나스닥 종합(가격만) 10년 기간")):
        x = r[key]
        L += ["", f"## {title} {x['windows']}번 ({x['first_start']} ~ {x['last_start']} 시작)", "", "| 전략 | 관망보다 많은 기간 | 가운데 값 |", "|---|---:|---:|"]
        for k in dl.ORDER:
            L.append(f"| {r['main'][k]['name']} | {x[k]['wins']} / {x['windows']} | {pct(x[k]['median_vs_hold'])} |")
    L += ["", "## 3. 확인 (본 실험과 다른 가정)", "", "| 가정 | 관망 끝 값 | 관망보다 많은 전략 | 낙폭이 더 작은 전략 |", "|---|---:|---:|---:|"]
    labels = {"cost0": "비용 0", "tbill_sub_cash0": "1991-01~2018-11, 현금 이자 0", "tbill_sub_cashRF": "1991-01~2018-11, 현금에 T-bill 이자",
              "cash_gs10": "현금에 10년 국채 금리 (위쪽 한계)", "price_only_2026": "가격만 1991-01~2026-02", "nasdaq_price_2000_2018": "나스닥 종합 가격만 2000~2018",
              "nasdaq_price_2003_2018": "나스닥 종합 가격만 2003~2018"}
    for k, v in r["sensitivity"].items():
        L.append(f"| {labels[k]} | ${v['hold_final']:,.0f} | {v['beat']} / 10 | {v['mdd_better']} / 10 |")
    L += ["", "### 전략별 (관망 대비 끝 값)", "", "| 전략 | " + " | ".join(labels[k] for k in r["sensitivity"]) + " |", "|---|" + "---:|" * len(r["sensitivity"])]
    for i, k in enumerate(dl.ORDER):
        L.append(f"| {r['main'][k]['name']} | " + " | ".join(pct(v["rows"][i]["vs_hold_pct"]) for v in r["sensitivity"].values()) + " |")
    c = r["checks"]["tr_daily_vs_monthly"]
    L += ["", "## 4. 자료 검사", "", f"- 일별 총수익 연율 {c['daily_cagr']:.3%} vs 월별(Shiller 월평균 가격) {c['monthly_cagr']:.3%}",
          f"- 일별 종가: {r['data']['sp500_daily']['first']} ~ {r['data']['sp500_daily']['last']} ({r['data']['sp500_daily']['rows']}일) — "
          f"skfolio ~{r['data']['sp500_daily']['splice']['skfolio_until']} + FRED {r['data']['sp500_daily']['splice']['fred_from']}~ "
          f"(겹치는 기간 값이 다른 날 {', '.join(r['data']['sp500_daily']['splice']['overlap_days_where_values_differ_fred_used']) or '없음'} → FRED)",
          f"- skfolio~arch 겹침 {r['data']['sp500_daily']['overlap_skfolio_arch']['common_days']}일 최대 차이 {r['data']['sp500_daily']['overlap_skfolio_arch']['max_rel_diff']:.2e}"]
    (HERE / "results.md").write_text("\n".join(L) + "\n", "utf-8")


if __name__ == "__main__":
    main()
