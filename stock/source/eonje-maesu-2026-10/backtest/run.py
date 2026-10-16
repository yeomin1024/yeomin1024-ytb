# -*- coding: utf-8 -*-
# VERSION: v3.0 — 2026-10-16 — 사용자 지시 2026-10-16 "매도 조건을 1년뒤로 하지말고 매수 이후 고점에서 n%하락할 때로 해봐 n은 너가 적당히 설정하고
#          그리고 수수료도 평균으로 설정해 그리고 허용했으니 기간 늘려": 매도 = 산 뒤 최고 종가에서 10% 떨어지면 다음 날 매도 (모든 규칙 같음),
#          수수료 0.25%(국내 주요 증권사 미국 주식 온라인 기본 수수료), 자산 = SPY(S&P 500 ETF) 종가 + 배당 재투자 총수익 (Yahoo — 사용자가 허용),
#          기간 2016-01-04 ~ 자료 끝(2026-10-15). 엔진 entry.py v1.2 (trail). 확인: n 5·15·20% · 수수료 0.07%·0 · 현금 T-bill 이자 · 가격만.
#          + 다시 매수(판 뒤 다음 매수)의 값·기다린 날 (results.json reentry — 끝 통계 장면·대본 근거).
# (v2.1 — 2026-10-16 — Buy and Hold 참고값 (계좌 칸).) (v2.0 — 2026-10-16 — 매수 신호 10가지 × 같은 매도 규칙(252 거래일 뒤), S&P 500 2016~2026-02.)
#          (v1.x — 매수 규칙 10가지 vs 관망 32년 — stock/source/_old/eonje-maesu-2026-10-v1/backtest/)
"""매수 신호 10가지 — 같은 돈 · 같은 매도 규칙 (연구·교육용 — 투자 권유가 아니다. 과거 결과는 미래를 보장하지 않는다).

실행:  python3 stock/source/eonje-maesu-2026-10/backtest/run.py [--refresh]   (--refresh = Yahoo 에서 다시 받기)
결과:  results.json · results.md · trades.csv · run.log · anim.js (장면 파일 자료 — 숫자는 이 파일에서만)

본 실험
  자산     SPY (S&P 500 ETF) 일별 — 신호·최고점은 종가, 계좌 값은 배당 재투자 총수익 (Yahoo 종가 + 배당, 우리가 계산)
           공포지수 규칙만 ^VIX 일별 종가
  기간     2016-01-04 (첫 거래일) ~ 자료 끝 (2026-10-15)
  돈       $10,000 한 번, 더 넣지 않음. 살 때 전부, 팔 때 전부
  매수     규칙마다 다름 (entry.RULES) — 신호는 그날 종가까지, 사는 것은 다음 거래일 종가
  매도     모든 규칙 같음 — 산 뒤 최고 종가에서 10% 떨어진 날(종가) → 다음 거래일 종가에 전부 매도
  수수료   사고팔 때마다 0.25% (국내 주요 증권사 미국 주식 온라인 기본 — 이벤트는 0.03~0.09%) · 현금 이자 0
확인 (결론을 바꾸는지 보기)
  n = 5·15·20% · 수수료 0.07%·0 · 현금에 T-bill(^IRX) 이자 · 배당 빼고 가격만
"""
import argparse
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
from backtest import data as bd          # noqa: E402
from backtest import entry as en         # noqa: E402

VERSION = "v3.0"
START = "2016-01-01"
CAPITAL = 10_000.0
COST = 0.0025                            # 사고팔 때마다 — 국내 주요 증권사 미국 주식 온라인 기본 수수료 약 0.25% (2026, 이벤트 0.03~0.09%)
TRAIL = 0.10                             # 매도: 산 뒤 최고 종가에서 10% — 댓글 손절 % 중 가장 많이 나온 값 (README 1번)
CHECK_TRAIL = [0.05, 0.15, 0.20]
CHECK_COST = [0.0007, 0.0]


def setup_log():
    fmt = logging.Formatter("%(message)s")
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    for h in list(root.handlers):
        root.removeHandler(h)
    fh = logging.FileHandler(HERE / "run.log", "w", "utf-8")
    sh = logging.StreamHandler(sys.stdout)
    for h in (fh, sh):
        h.setFormatter(fmt)
        root.addHandler(h)
    return logging.getLogger("run")


def log(stage, **kv):
    logging.getLogger("run").info("[%s] %s %s", stage, time.strftime("%Y-%m-%dT%H:%M:%S"), " ".join(f"{k}={v}" for k, v in kv.items()))


def load(refresh=False):
    spy, meta_s = bd.yahoo_daily("SPY", refresh=refresh)
    vix, meta_v = bd.yahoo_daily("^VIX", refresh=refresh)
    irx, meta_i = bd.yahoo_daily("^IRX", refresh=refresh)
    close, tr = spy["close"], spy["tr"]
    # 대조: Yahoo ^VIX vs datasets/finance-vix (커밋 고정) — 기간 안에서
    try:
        vix_d, _ = bd.vix_daily()
        c = vix["close"].loc[START:].index.intersection(vix_d.loc[START:].index)
        rel = (vix["close"].loc[c] / vix_d.loc[c] - 1).abs()
        log("VALIDATE", vix_yahoo_vs_datasets=f"days={len(c)} max_rel={rel.max():.4%} over_0.1pct={int((rel > 1e-3).sum())}")
    except Exception as e:  # noqa: BLE001
        log("VALIDATE", vix_yahoo_vs_datasets=f"skip ({e!r:.80})")
    log("DATA", spy=f"{close.index[0].date()}~{close.index[-1].date()} rows={len(close)} divs={int((spy['div'] > 0).sum())}",
        vix=f"{vix.index[0].date()}~{vix.index[-1].date()}", irx=f"{irx.index[0].date()}~{irx.index[-1].date()}",
        use=f"{START}~{close.index[-1].date()}")
    return close, tr, vix["close"], irx["close"], {"spy": meta_s, "vix": meta_v, "irx": meta_i}


def pct(x, d=1):
    return "—" if x is None or (isinstance(x, float) and np.isnan(x)) else f"{x * 100:+.{d}f}%"


def tbill_cash(index, irx):
    """^IRX(13주 T-bill 할인율, 연 %) → 하루 현금 수익률 (d-1 → d). 빈 날은 앞 값."""
    y = irx.reindex(index).ffill().bfill().to_numpy(float) / 100.0
    c = (1.0 + y) ** (1.0 / 252) - 1.0
    c[0] = 0.0
    return np.r_[0.0, c[:-1]]                                   # d-1 의 금리로 d-1 → d 이자 (그날 금리는 그날 뒤에 앎)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--refresh", action="store_true")
    a = ap.parse_args()
    setup_log()
    t0 = time.time()
    close, tr, vix, irx, metas = load(a.refresh)
    END = str(close.index[-1].date())
    out, ind, (s, e) = en.run_all(close, START, END, vix=vix, capital=CAPITAL, cost=COST, px=tr.to_numpy(), trail=TRAIL)
    dates = close.index
    bh_v, bh = en.buy_and_hold(close, START, END, capital=CAPITAL, cost=COST, px=tr.to_numpy())

    checks = {}
    for n in CHECK_TRAIL:
        o, _, _ = en.run_all(close, START, END, vix=vix, capital=CAPITAL, cost=COST, px=tr.to_numpy(), trail=n, label=f"trail{n:.0%}")
        checks[f"trail{int(n * 100)}"] = {k: o[k][1] for k in o}
    for c in CHECK_COST:
        o, _, _ = en.run_all(close, START, END, vix=vix, capital=CAPITAL, cost=c, px=tr.to_numpy(), trail=TRAIL, label=f"cost{c:.2%}")
        checks[f"cost{c * 100:g}"] = {k: o[k][1] for k in o}
        checks[f"cost{c * 100:g}"]["_buy_and_hold"] = en.buy_and_hold(close, START, END, capital=CAPITAL, cost=c, px=tr.to_numpy())[1]
    cash = tbill_cash(dates, irx)
    o, _, _ = en.run_all(close, START, END, vix=vix, capital=CAPITAL, cost=COST, px=tr.to_numpy(), cash_ret=cash, trail=TRAIL, label="cash_tbill")
    checks["cash_tbill"] = {k: o[k][1] for k in o}
    o, _, _ = en.run_all(close, START, END, vix=vix, capital=CAPITAL, cost=COST, px=None, trail=TRAIL, label="price_only")
    checks["price_only"] = {k: o[k][1] for k in o}
    checks["price_only"]["_buy_and_hold"] = en.buy_and_hold(close, START, END, capital=CAPITAL, cost=COST)[1]

    reentry = {}
    for k in en.ORDER:                                            # 판 뒤 다음 매수: 판 값 대비 다시 산 값, 기다린 거래일
        T = out[k][0].trades
        ch = [b["buy_price"] / a["sell_price"] - 1.0 for a, b in zip(T, T[1:])]
        gp = [b["buy_i"] - a["sell_i"] for a, b in zip(T, T[1:])]
        reentry[k] = {"n": len(ch), "mean_change": float(np.mean(ch)) if ch else None, "median_gap_days": float(np.median(gp)) if gp else None,
                      "higher": int(sum(c > 0 for c in ch)), "lower_or_same": int(sum(c <= 0 for c in ch))}
        log("RESULT", rule=k, reentries=len(ch), mean_rebuy_vs_sell=f"{np.mean(ch):+.2%}" if ch else "-",
            median_wait=f"{np.median(gp):.0f}d" if gp else "-")
    # 대본 근거 사실 (코드로 셈): 2020년 바닥, 고점 −20% 규칙이 마지막으로 판 뒤 가장 깊었던 하락
    c20 = close.loc["2020"]
    last_sale = max(t["sell_i"] for t in out["dip20"][0].trades if not t["open"])
    dd_after = (close / close.cummax() - 1.0).iloc[last_sale + 1:e + 1]
    facts = {"spy_2020_bottom": {"date": str(c20.idxmin().date()), "close": float(c20.min())},
             "dip20_after_last_sale": {"last_sale": str(dates[last_sale].date()), "min_dd": float(dd_after.min()),
                                       "min_dd_date": str(dd_after.idxmin().date()), "years_to_end": float((dates[e] - dates[last_sale]).days / 365.25)}}
    log("RESULT", facts=json.dumps(facts, ensure_ascii=False))
    rank = sorted(out, key=lambda k: -out[k][1]["final"])
    beat = [k for k in out if out[k][1]["final"] > bh["final"]]
    log("RESULT", main_rank=",".join(rank), buy_and_hold=f"{bh['final']:,.0f}", rules_above_bh=len(beat))
    for name, c in checks.items():
        rk = sorted([k for k in c if not k.startswith("_")], key=lambda k: -c[k]["final"])
        bhc = c.get("_buy_and_hold", bh)["final"]
        log("RESULT", check=name, top3=",".join(rk[:3]), bottom=rk[-1], above_bh=sum(c[k]["final"] > bhc for k in rk))

    res = {
        "version": VERSION, "engine": en.VERSION, "made_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "note": "연구·교육용. 투자 권유가 아니다. 과거 결과는 미래를 보장하지 않는다. 대본·화면 숫자는 이 파일에서만.",
        "params": {"asset": "SPY (S&P 500 ETF) 일별 — 신호는 종가, 계좌는 배당 재투자 총수익", "start": str(dates[s].date()), "end": str(dates[e].date()),
                   "capital": CAPITAL, "cost": COST, "cost_source": "국내 주요 증권사 미국 주식 온라인 기본 수수료 약 0.25% (2026 — 이벤트 0.03~0.09%)",
                   "cash_interest": 0, "trail": TRAIL,
                   "sell_rule": "산 뒤 최고 종가(산 날 포함)에서 10% 떨어진 날 종가 → 다음 거래일 종가에 전부 매도 (모든 규칙 같음)",
                   "buy_timing": "신호 = 그날 종가까지, 매수 = 다음 거래일 종가",
                   "rules": {k: {"name": en.RULES[k][1], "condition": en.RULES[k][2]} for k in en.ORDER}},
        "data": {k: {kk: v.get(kk) for kk in ("url", "fetched_at", "sha256", "first", "last", "rows", "dividends", "tr_vs_yahoo_adjclose")}
                 for k, v in metas.items()},
        "rules": {k: out[k][1] for k in en.ORDER},
        "trades": {k: out[k][0].trades for k in en.ORDER},
        "rank_by_final": rank,
        "buy_and_hold": bh,
        "rules_above_buy_and_hold": beat,
        "reentry": reentry,
        "facts": facts,
        "checks": checks,
        "spy": {"start_close": float(close.iloc[s]), "end_close": float(close.iloc[e]), "max": float(close.iloc[s:e + 1].max()),
                "max_date": str(close.iloc[s:e + 1].idxmax().date())},
    }
    (HERE / "results.json").write_text(json.dumps(res, ensure_ascii=False, indent=1, default=float), "utf-8")

    rows = []
    for k in en.ORDER:
        for t in out[k][0].trades:
            rows.append({"rule": k, "buy_date": t["buy_date"], "buy_price": round(t["buy_price"], 2), "peak_price": round(t["peak_price"], 2),
                         "sell_date": t["sell_date"], "sell_price": round(t["sell_price"], 2), "days": t["days"], "ret": round(t["ret"], 6),
                         "open": t["open"], "buy_cash": round(t["buy_cash"], 2), "sell_cash": round(t["sell_cash"], 2)})
    pd.DataFrame(rows).to_csv(HERE / "trades.csv", index=False)
    write_md(res)
    write_anim(close, ind, out, s, e, res, bh_v)
    log("RESULT", file="results.json,results.md,trades.csv,anim.js", sec=f"{time.time() - t0:.1f}")


def write_md(res):
    P, b = res["params"], res["buy_and_hold"]
    L = [f"# 매수 신호 10가지 — 같은 돈·같은 매도 규칙 (`run.py` {VERSION}, 엔진 `entry.py` {res['engine']}, {res['made_at']})", "",
         "> 연구·교육용. 투자 권유가 아니다. 과거 결과는 미래를 보장하지 않는다. 숫자는 이 파일·`results.json` 의 코드 출력만 쓴다.", "",
         f"- 자산: {P['asset']} · 기간 {P['start']} ~ {P['end']} · 시작 돈 $10,000 (모두 같음, 더 넣지 않음)",
         f"- 매수: 규칙마다 다름 — {P['buy_timing']} · **매도: {P['sell_rule']}**",
         f"- 수수료 {P['cost'] * 100:.2f}% ({P['cost_source']}) · 현금 이자 0",
         f"- SPY 종가: {res['spy']['start_close']:,.2f} → {res['spy']['end_close']:,.2f} (기간 최고 {res['spy']['max']:,.2f}, {res['spy']['max_date']})",
         f"- 참고 **BUY & HOLD** (첫날 {b['buy_date']} 종가에 전부 매수 → 그대로): ${b['final']:,.0f} · {pct(b['total_return'])} · 최대 낙폭 {pct(b['max_dd'])} ({b['max_dd_date']})",
         f"- BUY & HOLD 보다 많이 남긴 규칙: **{len(res['rules_above_buy_and_hold'])} / 10**", "",
         "## 1. 본 실험 (끝 값 순)", "",
         "| # | 규칙 | 조건 | 끝 값 | 누적 | 매수 | 판 거래 | 이긴 거래 | 거래 평균 | 가장 좋은 · 나쁜 거래 | 주식 보유 비율 | 최대 낙폭 | 첫 매수 |",
         "|---:|---|---|---:|---:|---:|---:|---:|---:|---|---:|---:|---|"]
    for i, k in enumerate(res["rank_by_final"], 1):
        r = res["rules"][k]
        L.append(f"| {i} | {P['rules'][k]['name']} | {P['rules'][k]['condition']} | ${r['final']:,.0f} | {pct(r['total_return'])} | {r['buys']} | "
                 f"{r['trades_closed']}{' + 보유 중 1' if r['trades_open'] else ''} | {(r['win_rate'] * 100):.0f}% | {pct(r['avg_trade'])} | "
                 f"{pct(r['best_trade'])} · {pct(r['worst_trade'])} | {r['invested_share'] * 100:.0f}% | {pct(r['max_dd'])} | {r['first_buy']} |")
    L += ["", "### 판 뒤 다시 매수 (판 값 대비 다시 산 값 · 기다린 거래일 가운데 값)", "", "| 규칙 | 다시 매수 | 평균 | 판 값보다 비싸게 | 기다린 날 |", "|---|---:|---:|---:|---:|"]
    for k in res["rank_by_final"]:
        q = res["reentry"][k]
        L.append(f"| {P['rules'][k]['name']} | {q['n']} | {pct(q['mean_change'])} | {q['higher']} / {q['n']} | {q['median_gap_days']:.0f}일 |")
    L += ["", "## 2. 거래 (BUY → 최고 → SELL)", ""]
    for k in en.ORDER:
        L.append(f"**{P['rules'][k]['name']}** — " + " · ".join(
            f"{t['buy_date']} {t['buy_price']:,.2f} → (최고 {t['peak_price']:,.2f}) → {t['sell_date']} {t['sell_price']:,.2f} {pct(t['ret'])}{' (보유 중)' if t['open'] else ''}"
            for t in res["trades"][k]))
        L.append("")
    c = res["checks"]
    L += ["## 3. 확인 — 조건을 바꾸면 순위가 바뀌나 (끝 값)", "",
          "| 규칙 | 본 실험 (−10%, 0.25%) | −5% | −15% | −20% | 수수료 0.07% | 수수료 0 | 현금 T-bill 이자 | 가격만 |", "|---|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for k in res["rank_by_final"]:
        L.append(f"| {P['rules'][k]['name']} | ${res['rules'][k]['final']:,.0f} | " + " | ".join(
            f"${c[n][k]['final']:,.0f}" for n in ("trail5", "trail15", "trail20", "cost0.07", "cost0", "cash_tbill", "price_only")) + " |")
    L.append(f"| *BUY & HOLD* | ${b['final']:,.0f} | — | — | — | ${c['cost0.07']['_buy_and_hold']['final']:,.0f} | ${c['cost0']['_buy_and_hold']['final']:,.0f} | — | ${c['price_only']['_buy_and_hold']['final']:,.0f} |")
    L += ["", "## 4. 한계", "",
          "- SPY 는 ETF 라 운용 보수(연 0.0945%)가 값에 이미 들어 있다. 세금·환전 비용은 넣지 않았다.",
          "- 매도는 '종가로 판단 → 다음 날 종가'라 실제 손절 주문(장중 체결)과 값이 다를 수 있다.",
          "- 현금 이자 0 (확인 칸에 T-bill 이자). 수수료 0.25% 는 국내 주요 증권사 기본 — 이벤트·해외 증권사는 더 낮다 (확인 칸).",
          "- 기간이 약 10년, 판 거래가 규칙마다 적어 승률·평균은 표본이 작다. Yahoo 자료는 받은 날(meta)과 sha256 으로 남긴다."]
    (HERE / "results.md").write_text("\n".join(L) + "\n", "utf-8")


def write_anim(close, ind, out, s, e, res, bh_v):
    """장면 파일 자료 (window.AN). 날짜는 s..e 거래일 전부, 값은 코드 출력을 반올림만."""
    d = close.index[s:e + 1]
    sl = slice(s, e + 1)
    AN = {"v": VERSION, "made_at": res["made_at"], "dates": [x.strftime("%Y-%m-%d") for x in d],
          "close": [round(float(x), 2) for x in close.iloc[sl]], "ticker": "SPY",
          "lines": {"ath": [round(float(x), 2) for x in ind["ath"][sl]],
                    "sma50": [round(float(x), 2) for x in ind["sma50"][sl]],
                    "sma200": [round(float(x), 2) for x in ind["sma200"][sl]],
                    "hi252": [round(float(x), 2) for x in ind["hi252"][sl]],
                    "rsi14": [round(float(x), 2) for x in ind["rsi14"][sl]],
                    "vix": [None if np.isnan(x) else round(float(x), 2) for x in ind["vix"][sl]],
                    "ret1": [round(float(x) * 100, 3) for x in ind["ret1"][sl]],
                    "close_252ago": [round(float(close.iloc[i - 252]), 2) for i in range(s, e + 1)]},
          "trail": TRAIL, "cost": COST, "capital": CAPITAL, "order": en.ORDER,
          "bh": [round(float(x), 2) for x in bh_v],
          "rules": {}}
    for k in en.ORDER:
        r, st = out[k]
        AN["rules"][k] = {"value": [round(float(x), 2) for x in r.value], "holding": "".join("1" if h else "0" for h in r.holding),
                          "trades": [{"b": t["buy_i"] - s, "s": t["sell_i"] - s, "bp": round(t["buy_price"], 2), "sp": round(t["sell_price"], 2),
                                      "pk": round(t["peak_price"], 2), "pi": t["peak_i"] - s, "st": (t["stop_i"] - s) if "stop_i" in t else None,
                                      "r": round(t["ret"], 6), "open": t["open"], "bc": round(t["buy_cash"], 2), "sc": round(t["sell_cash"], 2)}
                                     for t in r.trades],
                          "final": round(st["final"], 2), "win": st["win_rate"], "avg": st["avg_trade"]}
        assert abs(AN["rules"][k]["value"][-1] - res["rules"][k]["final"]) < 0.01, k
        assert len(AN["rules"][k]["value"]) == len(AN["dates"]), k
    assert abs(AN["bh"][-1] - res["buy_and_hold"]["final"]) < 0.01 and len(AN["bh"]) == len(AN["dates"])
    ck = res["checks"]

    def above(name):                                         # BUY & HOLD 보다 많이 남긴 규칙 수 (그 확인의 BUY & HOLD 와 비교)
        c = ck[name]
        bh = c.get("_buy_and_hold", res["buy_and_hold"])["final"]
        return int(sum(c[k]["final"] > bh for k in c if not k.startswith("_")))
    AN["summary"] = {"rank": res["rank_by_final"], "finals": {k: round(res["rules"][k]["final"], 2) for k in en.ORDER},
                     "invested": {k: round(res["rules"][k]["invested_share"], 4) for k in en.ORDER},
                     "buys": {k: res["rules"][k]["buys"] for k in en.ORDER},
                     "reentry": {k: {"mean": res["reentry"][k]["mean_change"], "gap": res["reentry"][k]["median_gap_days"]} for k in en.ORDER},
                     "bh": {k: res["buy_and_hold"][k] for k in ("final", "total_return", "max_dd", "max_dd_date")},
                     "above": {"trail10": len(res["rules_above_buy_and_hold"]), "trail5": above("trail5"), "trail15": above("trail15"),
                               "trail20": above("trail20"), "cost0": above("cost0")},
                     "facts": res["facts"]}
    txt = ("// 자동 생성 — stock/source/eonje-maesu-2026-10/backtest/run.py " + VERSION + " (손으로 고치지 않음). 연구·교육용 — 투자 권유 아님.\n"
           "window.AN = " + json.dumps(AN, ensure_ascii=False, separators=(",", ":")) + ";\n")
    (HERE / "anim.js").write_text(txt, "utf-8")
    log("RESULT", anim="anim.js", days=len(d), kb=round(len(txt) / 1024))


if __name__ == "__main__":
    main()
