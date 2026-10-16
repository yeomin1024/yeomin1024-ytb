# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-16 — 주식 1번 v4 '성공률' 백테스트. 사용자 지시 2026-10-16 "수익률로 비교하지말고 성공 기준을 매수 후 해당 지점에서
#          m%이하로 떨어지지 않고 매수 지점에서 n% 이상 상승하면 성공으로 하자" · 앞선 지시 "조건 발생이 너무 희소해서 거래 횟수가 없고 현금 가지고 있는
#          기간이 많아서 그런것 같아 매수 방법으로 다 변경해보고 매도 규칙도 변경해봐":
#          매수 = 자주 나오는 매수 방법 10가지 (entry.RULES_V4 — 예전 10가지와 같은 집안, 문턱만 넓힘: 문턱은 발생 빈도로만 정함, 성공률은 보지 않음)
#          매도 = 산 값보다 +n% (성공) 또는 −m% (실패) 종가가 먼저 나온 날 → 다음 거래일 종가 (entry.simulate(barrier=(m, n)))
#          m = n = 5% (대칭 — 50% 가 동전 던지기 · 거래 수: ±10% 는 방법마다 10년 20~26번 판정뿐, ±5% 는 39~84번) · 확인: ±3%·±10%·(5,10)·(10,5)
#          잣대 = 성공률 (성공 ÷ 판정 난 거래) vs '아무 날 매수'(any — 매도 다음 날 바로 다시 매수) · 날마다 매수했다면(신호 날 전부) · 1994~2015 확인.
#          예전 v3 (끝 값 비교, 산 뒤 최고 −10% 매도)은 ../run.py v3.0 그대로.
"""성공률 백테스트 (연구·교육용 — 투자 권유가 아니다. 과거 결과는 미래를 보장하지 않는다).
실행: python3 stock/source/eonje-maesu-2026-10/backtest/barrier/run.py   → results.json · results.md · trades.csv · run.log · anim.js
"""
import json
import logging
import math
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / "tools"))
from backtest import data as bd          # noqa: E402
from backtest import entry as en         # noqa: E402

VERSION = "v1.0"
START, CAPITAL, COST = "2016-01-01", 10_000.0, 0.0025          # 수수료 = 국내 주요 증권사 미국 주식 온라인 기본 약 0.25% (v3 와 같음)
M, N = 0.05, 0.05                                              # 실패 −5% · 성공 +5% (산 값 기준, 종가)
GRID = [(0.03, 0.03), (0.05, 0.05), (0.10, 0.10), (0.05, 0.10), (0.10, 0.05)]
LONG = ("1994-03-01", "2015-12-31")                            # 확인 기간 (2000~02·2008 하락 포함)
KEYS = ["any"] + en.ORDER_V4


def setup_log():
    fmt = logging.Formatter("%(message)s")
    root = logging.getLogger(); root.setLevel(logging.INFO)
    for h in list(root.handlers):
        root.removeHandler(h)
    for h in (logging.FileHandler(HERE / "run.log", "w", "utf-8"), logging.StreamHandler(sys.stdout)):
        h.setFormatter(fmt); root.addHandler(h)


def log(stage, **kv):
    logging.getLogger("run").info("[%s] %s %s", stage, time.strftime("%Y-%m-%dT%H:%M:%S"), " ".join(f"{k}={v}" for k, v in kv.items()))


def binom_p(k, n, p0):
    """정확 이항 검정 양쪽 p 값 (관측 확률 이하인 경우의 합) — 표본이 작다는 것을 숫자로 보이려고 (scipy 없이)."""
    if n == 0:
        return float("nan")
    pk = [math.comb(n, i) * p0 ** i * (1 - p0) ** (n - i) for i in range(n + 1)]
    return float(min(1.0, sum(q for q in pk if q <= pk[k] * (1 + 1e-9))))


def event_level(ind, s, e, mn, keys):
    """신호가 나온 날마다 따로 샀다면 (겹쳐도 셈 — 표본이 많지만 서로 독립이 아님): 신호 d → d+1 종가 매수 → 먼저 닿은 쪽."""
    m, n = mn
    c = ind["close"]
    # 날마다: d+1 에 사면 성공(1)/실패(0)/판정 없음(nan)
    res = np.full(len(c), np.nan)
    for d in range(s - 1, e):
        b = d + 1
        bp = c[b]
        up, dn = bp * (1 + n), bp * (1 - m)
        for j in range(b + 1, e + 1):
            if c[j] >= up * (1 - 1e-12):
                res[d] = 1; break
            if c[j] <= dn * (1 + 1e-12):
                res[d] = 0; break
    out = {}
    for k in keys:
        sig = np.array([bool(en.ALL_RULES[k][0](ind, d)) for d in range(s - 1, e)])
        r = res[s - 1:e][sig]
        r = r[~np.isnan(r)]
        out[k] = {"days": int(sig.sum()), "decided": int(len(r)), "success_rate": float(r.mean()) if len(r) else None}
    return out


def run_period(close, tr, vix, start, end, mn, label, keys=KEYS):
    ind = en.indicators(close, vix)
    dates = close.index
    s, e = int(dates.searchsorted(pd.Timestamp(start))), int(dates.searchsorted(pd.Timestamp(end), side="right") - 1)
    out = {}
    for k in keys:
        r = en.simulate(k, ind, s, e, capital=CAPITAL, cost=COST, px=tr.to_numpy(), dates=dates, barrier=mn)
        st = en.stats(r, CAPITAL)
        out[k] = (r, st)
    log("RESULT", label=label, m=mn[0], n=mn[1], start=str(dates[s].date()), end=str(dates[e].date()),
        rates=",".join(f"{k}:{out[k][1]['success_rate']:.0%}({out[k][1]['wins']}/{out[k][1]['wins'] + out[k][1]['losses']})" for k in keys))
    return out, ind, (s, e)


def main():
    setup_log()
    t0 = time.time()
    spy, meta_s = bd.yahoo_daily("SPY"); vix_df, meta_v = bd.yahoo_daily("^VIX")
    close, tr, vix = spy["close"], spy["tr"], vix_df["close"]
    END = str(close.index[-1].date())
    log("DATA", spy=f"{close.index[0].date()}~{END} rows={len(close)}", vix=f"{vix.index[0].date()}~{vix.index[-1].date()}", use=f"{START}~{END}",
        sell=f"+{N:.0%} 성공 / −{M:.0%} 실패 (종가) → 다음 날 종가", cost=COST)
    out, ind, (s, e) = run_period(close, tr, vix, START, END, (M, N), "main")
    dates = close.index
    # 신호 빈도 (문턱을 정한 근거 — 성공률이 아님)
    freq = {}
    for k in KEYS:
        sig = np.array([bool(en.ALL_RULES[k][0](ind, d)) for d in range(s, e + 1)])
        dd = np.flatnonzero(sig)
        freq[k] = {"share_days": float(sig.mean()), "episodes": int(np.sum(np.diff(np.r_[-10, dd]) > 1))}
    base = out["any"][1]["success_rate"]
    ev = event_level(ind, s, e, (M, N), KEYS)
    p0 = ev["any"]["success_rate"]                                # 날마다 샀을 때 성공률 = '아무 날' 확률
    log("RESULT", base_sequential=f"{base:.1%}", base_every_day=f"{p0:.1%} ({ev['any']['decided']} days)")
    rows = {}
    for k in KEYS:
        st = out[k][1]
        nn = st["wins"] + st["losses"]
        rows[k] = {**st, "vs_any_pp": (st["success_rate"] - p0) if nn else None, "binom_p_vs_every_day": binom_p(st["wins"], nn, p0),
                   "event": ev[k], "freq": freq[k]}
        log("RESULT", rule=k, trades=len(out[k][0].trades), decided=nn, wins=st["wins"], losses=st["losses"], undecided=st["undecided"],
            rate=f"{st['success_rate']:.1%}", vs_every_day=f"{(st['success_rate'] - p0) * 100:+.1f}%p", p=f"{rows[k]['binom_p_vs_every_day']:.2f}",
            event_rate=f"{ev[k]['success_rate']:.1%}({ev[k]['decided']})", invested=f"{st['invested_share']:.0%}",
            days_to_decide=f"{st['avg_days_to_decide']:.0f}" if st["avg_days_to_decide"] else "-")
    rank = sorted(en.ORDER_V4, key=lambda k: (-rows[k]["success_rate"], -rows[k]["wins"]))
    grid = {}
    for mn in GRID:
        o, _, _ = run_period(close, tr, vix, START, END, mn, f"grid{int(mn[0]*100)}_{int(mn[1]*100)}")
        evg = event_level(ind, s, e, mn, ["any"])["any"]["success_rate"]
        grid[f"{int(mn[0]*100)}_{int(mn[1]*100)}"] = {"every_day": evg, **{k: {"rate": o[k][1]["success_rate"], "wins": o[k][1]["wins"], "losses": o[k][1]["losses"]} for k in KEYS}}
    o_long, ind_long, (sl, el) = run_period(close, tr, vix, LONG[0], LONG[1], (M, N), "long1994_2015")
    ev_long = event_level(ind_long, sl, el, (M, N), KEYS)
    long = {"every_day": ev_long["any"]["success_rate"], **{k: {"rate": o_long[k][1]["success_rate"], "wins": o_long[k][1]["wins"], "losses": o_long[k][1]["losses"],
                                                              "event_rate": ev_long[k]["success_rate"]} for k in KEYS}}
    def spearman(a, b):
        ra = {k: i for i, k in enumerate(sorted(en.ORDER_V4, key=lambda k: -a[k]))}; rb = {k: i for i, k in enumerate(sorted(en.ORDER_V4, key=lambda k: -b[k]))}
        return 1 - 6 * sum((ra[k] - rb[k]) ** 2 for k in en.ORDER_V4) / (10 * 99)
    main_r = {k: rows[k]["success_rate"] for k in en.ORDER_V4}
    corr = {g: spearman(main_r, {k: grid[g][k]["rate"] for k in en.ORDER_V4}) for g in grid}
    corr["long1994_2015"] = spearman(main_r, {k: long[k]["rate"] for k in en.ORDER_V4})
    log("RESULT", rank=",".join(rank), spearman=json.dumps({k: round(v, 2) for k, v in corr.items()}))
    res = {
        "version": VERSION, "engine": en.VERSION, "made_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "note": "연구·교육용. 투자 권유가 아니다. 과거 결과는 미래를 보장하지 않는다. 대본·화면 숫자는 이 파일에서만.",
        "params": {"asset": "SPY (S&P 500 ETF) 일별 — 신호·성공 판정은 종가, 계좌 값은 배당 재투자 총수익", "start": str(dates[s].date()), "end": str(dates[e].date()),
                   "capital": CAPITAL, "cost": COST, "m": M, "n": N,
                   "success": f"산 값보다 +{N:.0%} 종가가 −{M:.0%} 종가보다 먼저 나오면 성공 (그날 판정 → 다음 거래일 종가에 매도)",
                   "buy_timing": "신호 = 그날 종가까지, 매수 = 다음 거래일 종가 · 들고 있는 동안 새로 사지 않음 · 매도한 날 신호가 있으면 다음 날 다시 매수",
                   "baseline": "any = 매도한 다음 날 바로 다시 매수 (신호 없음) · every_day = 날마다 샀다면 (모든 거래일을 따로 셈)",
                   "threshold_basis": "문턱은 10년 동안 신호가 나온 날·묶음 수·거래 수만 보고 정함 (성공률을 보지 않음 — results 의 freq)",
                   "rules": {k: {"name": en.ALL_RULES[k][1], "condition": en.ALL_RULES[k][2]} for k in KEYS}},
        "data": {k: {kk: v.get(kk) for kk in ("url", "fetched_at", "sha256", "first", "last", "rows")} for k, v in {"spy": meta_s, "vix": meta_v}.items()},
        "base": {"sequential_any": base, "every_day": p0, "every_day_decided": ev["any"]["decided"]},
        "rules": rows, "rank_by_success": rank,
        "trades": {k: out[k][0].trades for k in KEYS},
        "grid": grid, "long": long, "spearman_vs_main": corr,
    }
    (HERE / "results.json").write_text(json.dumps(res, ensure_ascii=False, indent=1, default=float), "utf-8")
    pd.DataFrame([{"rule": k, "buy_date": t["buy_date"], "buy_price": round(t["buy_price"], 2), "target": round(t["target"], 2), "stop": round(t["stop"], 2),
                   "result": t["result"], "hit_date": t.get("hit_date"), "sell_date": t["sell_date"], "sell_price": round(t["sell_price"], 2),
                   "days": t["days"], "ret": round(t["ret"], 6), "open": t["open"]} for k in KEYS for t in out[k][0].trades]).to_csv(HERE / "trades.csv", index=False)
    write_md(res)
    write_anim(close, ind, out, s, e, res)
    log("DONE", files="results.json,results.md,trades.csv,anim.js,run.log", sec=f"{time.time() - t0:.1f}")


def pc(x, d=1):
    return "—" if x is None or (isinstance(x, float) and np.isnan(x)) else f"{x * 100:.{d}f}%"


def write_md(res):
    P, R, B = res["params"], res["rules"], res["base"]
    L = [f"# 매수 방법 10가지 — 성공률 (`barrier/run.py` {VERSION}, 엔진 `entry.py` {res['engine']}, {res['made_at']})", "",
         "> 연구·교육용. 투자 권유가 아니다. 과거 결과는 미래를 보장하지 않는다. 숫자는 이 파일·`results.json` 의 코드 출력만 쓴다.", "",
         f"- 자산: {P['asset']} · 기간 {P['start']} ~ {P['end']} · 시작 돈 $10,000 · 수수료 {P['cost']:.2%}",
         f"- **성공 = {P['success']}**", f"- 매수: {P['buy_timing']}", f"- 기준: {P['baseline']}", f"- 문턱: {P['threshold_basis']}",
         f"- 기준 성공률: 아무 날(매도 다음 날 바로 다시 매수) **{pc(B['sequential_any'])}** · 날마다 샀다면 **{pc(B['every_day'])}** ({B['every_day_decided']}일)", "",
         "## 1. 본 실험 (±5%, 성공률 순)", "",
         "| # | 매수 방법 | 조건 | 성공 | 실패 | 성공률 | 날마다 대비 | p (날마다 확률과 같다면) | 신호 날마다 샀다면 | 판정까지 평균 | 주식 보유 | 신호 묶음 |",
         "|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for i, k in enumerate(res["rank_by_success"], 1):
        r = R[k]
        L.append(f"| {i} | {P['rules'][k]['name']} | {P['rules'][k]['condition']} | {r['wins']} | {r['losses']} | {pc(r['success_rate'])} | {r['vs_any_pp'] * 100:+.1f}%p | "
                 f"{r['binom_p_vs_every_day']:.2f} | {pc(r['event']['success_rate'])} ({r['event']['decided']}일) | {r['avg_days_to_decide']:.0f}일 | {pc(r['invested_share'], 0)} | {r['freq']['episodes']} |")
    a = R["any"]
    L.append(f"| — | *{P['rules']['any']['name']}* | {P['rules']['any']['condition']} | {a['wins']} | {a['losses']} | {pc(a['success_rate'])} | — | — | {pc(a['event']['success_rate'])} | {a['avg_days_to_decide']:.0f}일 | {pc(a['invested_share'], 0)} | — |")
    L += ["", "## 2. 확인 — 성공·실패 폭을 바꾸면 (성공률)", "", "| 매수 방법 | " + " | ".join(f"−{g.split('_')[0]}% / +{g.split('_')[1]}%" for g in res["grid"]) + " | 1994~2015 (±5%) |",
          "|---|" + "---:|" * (len(res["grid"]) + 1)]
    for k in KEYS:
        L.append(f"| {P['rules'][k]['name']} | " + " | ".join(f"{pc(res['grid'][g][k]['rate'])} ({res['grid'][g][k]['wins']}/{res['grid'][g][k]['wins'] + res['grid'][g][k]['losses']})" for g in res["grid"])
                 + f" | {pc(res['long'][k]['rate'])} ({res['long'][k]['wins']}/{res['long'][k]['wins'] + res['long'][k]['losses']}) |")
    L.append("| *날마다 샀다면* | " + " | ".join(pc(res["grid"][g]["every_day"]) for g in res["grid"]) + f" | {pc(res['long']['every_day'])} |")
    L += ["", "- 순위 상관 (본 실험 대비, Spearman): " + " · ".join(f"{k} {v:+.2f}" for k, v in res["spearman_vs_main"].items()), "",
          "## 3. 한계", "",
          "- 성공·실패는 종가로만 본다 (장중 고가·저가는 없음). 판정 다음 날 종가에 팔아 실제 수익률은 ±5% 보다 조금 다르다.",
          "- 거래가 방법마다 34~85번 — 성공률 차이 몇 %p 는 우연으로도 나온다 (p 값 칸). '신호 날마다 샀다면' 은 날이 많지만 서로 겹쳐 독립이 아니다.",
          "- 오르는 시장(2016~2026)에서는 같은 폭이라도 성공이 실패보다 잦다 → 50% 가 아니라 '아무 날' 성공률과 견준다.",
          "- 끝 값(계좌 돈)은 이 실험의 잣대가 아니다 (results.json rules.*.final 에 참고로만)."]
    (HERE / "results.md").write_text("\n".join(L) + "\n", "utf-8")


def write_anim(close, ind, out, s, e, res):
    d = close.index[s:e + 1]; sl = slice(s, e + 1)
    r2 = lambda a: [None if (x is None or (isinstance(x, float) and np.isnan(x))) else round(float(x), 2) for x in a]
    AN = {"v": VERSION, "made_at": res["made_at"], "dates": [x.strftime("%Y-%m-%d") for x in d], "close": r2(close.iloc[sl]), "ticker": "SPY",
          "lines": {"sma5": r2(ind["sma5"][sl]), "sma20": r2(ind["sma20"][sl]), "hi20": r2(ind["hi20"][sl]), "max20": r2(ind["max20"][sl]),
                    "ath": r2(ind["ath"][sl]), "rsi14": r2(ind["rsi14"][sl]), "vix": r2(ind["vix"][sl]), "ret1": r2(ind["ret1"][sl] * 100),
                    "close_21ago": [round(float(close.iloc[i - 21]), 2) for i in range(s, e + 1)]},
          "m": M, "n": N, "cost": COST, "capital": CAPITAL, "order": en.ORDER_V4, "base": res["base"], "rules": {}}
    for k in KEYS:
        r, st = out[k]
        AN["rules"][k] = {"holding": "".join("1" if h else "0" for h in r.holding), "value": [round(float(x), 2) for x in r.value],
                          "trades": [{"b": t["buy_i"] - s, "s": t["sell_i"] - s, "h": (t["hit_i"] - s) if t.get("hit_i") is not None else None,
                                      "bp": round(t["buy_price"], 2), "sp": round(t["sell_price"], 2), "tg": round(t["target"], 2), "sl": round(t["stop"], 2),
                                      "res": {"win": "w", "loss": "l"}.get(t["result"]), "r": round(t["ret"], 6), "open": t["open"]} for t in r.trades],
                          "rate": st["success_rate"], "wins": st["wins"], "losses": st["losses"]}
        w = sum(t["res"] == "w" for t in AN["rules"][k]["trades"]); l = sum(t["res"] == "l" for t in AN["rules"][k]["trades"])
        assert (w, l) == (res["rules"][k]["wins"], res["rules"][k]["losses"]), k
        assert len(AN["rules"][k]["holding"]) == len(AN["dates"]), k
    AN["summary"] = {"rank": res["rank_by_success"], "rates": {k: res["rules"][k]["success_rate"] for k in KEYS},
                     "grid": res["grid"], "long": res["long"], "spearman": res["spearman_vs_main"]}
    txt = ("// 자동 생성 — stock/source/eonje-maesu-2026-10/backtest/barrier/run.py " + VERSION + " (손으로 고치지 않음). 연구·교육용 — 투자 권유 아님.\n"
           "window.AN = " + json.dumps(AN, ensure_ascii=False, separators=(",", ":")) + ";\n")
    (HERE / "anim.js").write_text(txt, "utf-8")
    log("RESULT", anim="anim.js", days=len(d), kb=round(len(txt) / 1024))


if __name__ == "__main__":
    main()
