# -*- coding: utf-8 -*-
# VERSION: v2.0 — 2026-10-16 — 실패 −2% · 무작위 매수 기준. 사용자 지시 2026-10-16 "그럼 신호 없이 무작위로 매수 했을 때랑 비교하는 거지? 그게 맞는거
#          같은데 그리고 m을 1~2%로 해야 엄격하게 봐서 성공 확률이 줄지 m은 내가 말한 범위에서 적절하게 정해서 영상 만들어봐":
#          m = 2% — 1~2% 안에서 '자료 성질'만 보고 정함 (매수 방법 순위를 보기 전, 아래 0번 표가 근거): 하루 변동 표준편차 약 1.1% · 1% 면 실패의 약 17% 가
#          산 다음 날 하루 만에 정해짐 (보통 하루 흔들림이 판정) → 2% 면 약 7%. n = 5% 그대로.
#          기준 = 신호 없이 날짜만 무작위로 산 계좌 (entry.random_entry — 방법마다 같은 기다림 분포·같은 매도 규칙, RUNS 개, 시드 고정)
#          → 성공률 평균·90% 범위(5~95번째)·p(양쪽: 무작위가 이만큼 벗어날 확률) · 날짜마다 그날까지의 무작위 평균·범위 (영상 카드).
#          확인: m 1%·1.5% (사용자 범위 안) · 1994~2015. 참고: 날마다 샀다면(every_day) · 매도 다음 날 바로 다시(any).
# (v1.0 — 2026-10-16 — ±5% 성공률, 기준 = any·every_day. 사용자 지시 "수익률로 비교하지말고 성공 기준을 … m%이하로 떨어지지 않고 … n% 이상 상승하면
#          성공으로 하자" · 앞선 지시 "조건 발생이 너무 희소해서 … 매수 방법으로 다 변경해보고 매도 규칙도 변경해봐": 매수 = 자주 나오는 매수 방법 10가지
#          (entry.RULES_V4 — 문턱은 발생 빈도로만 정함), 매도 = 산 값보다 +n%·−m% 종가 중 먼저 → 다음 거래일 종가. 예전 v3 (끝 값 비교)은 ../run.py v3.0 그대로.)
"""성공률 백테스트 (연구·교육용 — 투자 권유가 아니다. 과거 결과는 미래를 보장하지 않는다).
실행: python3 stock/source/eonje-maesu-2026-10/backtest/barrier/run.py   → results.json · results.md · trades.csv · run.log · anim.js
"""
import json
import logging
import sys
import time
import warnings
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / "tools"))
from backtest import data as bd          # noqa: E402
from backtest import entry as en         # noqa: E402

VERSION = "v2.0"
START, CAPITAL, COST = "2016-01-01", 10_000.0, 0.0025          # 수수료 = 국내 주요 증권사 미국 주식 온라인 기본 약 0.25% (v3 와 같음)
M, N = 0.02, 0.05                                              # 실패 −2% · 성공 +5% (산 값 기준, 종가) — m 은 아래 M_CHOICES 표(자료 성질)로 정함
M_CHOICES = [0.01, 0.0125, 0.015, 0.0175, 0.02]                 # 사용자 범위 1~2% — 성질만 셈 (매수 방법은 돌리지 않음)
CHECK_M = [0.01, 0.015]                                        # 확인 (사용자 범위 안)
RUNS, RUNS_CHECK, SEED = 2000, 1000, 20261016                  # 무작위 매수 계좌 수 · 시드 (방법마다 SEED + 순번)
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


def choose_m(close, s, e):
    """m 고르기 근거 (자료 성질만 — 매수 방법 결과는 보지 않음): 하루 변동 · m 마다 날마다 샀다면 성공률 · 실패 중 산 다음 날 바로 정해진 몫 · 판정까지 거래일(중앙)."""
    p = close.to_numpy(float)
    r = p[s + 1:e + 1] / p[s:e] - 1
    out = {"daily_std": float(r.std()), "share_abs_ge_1pct": float((np.abs(r) >= 0.01).mean()), "share_abs_ge_2pct": float((np.abs(r) >= 0.02).mean()),
           "share_down_le_1pct": float((r <= -0.01).mean()), "share_down_le_2pct": float((r <= -0.02).mean()), "m": {}}
    for m in M_CHOICES:
        res, hit = en.barrier_table(p, s, e, m, N)
        b = np.arange(s, e + 1); ok = res[b] >= 0
        days = (hit[b] - b)[ok]; rr = res[b][ok]
        fail_day1 = int(((days == 1) & (rr == 0)).sum())
        out["m"][f"{m:.4f}"] = {"every_day": float(rr.mean()), "decided": int(ok.sum()), "fail_day1_of_fails": fail_day1 / max(1, int((rr == 0).sum())),
                                "days_median": float(np.median(days))}
        log("SIGNAL", choose_m=f"{m:.2%}", every_day=f"{rr.mean():.1%}", fail_day1_of_fails=f"{out['m'][f'{m:.4f}']['fail_day1_of_fails']:.1%}",
            days_median=f"{np.median(days):.0f}")
    log("SIGNAL", daily_std=f"{out['daily_std']:.2%}", abs_ge_1pct=f"{out['share_abs_ge_1pct']:.1%}", abs_ge_2pct=f"{out['share_abs_ge_2pct']:.1%}",
        chosen_m=f"{M:.0%}", why="1% = 하루 변동 표준편차 안쪽 → 하루 흔들림이 판정 / 2% = 사용자 범위 안 가장 넓음, 무작위 성공률 반쯤")
    return out


def vs_random(run, table, s, e, runs, seed):
    """방법 하나를 같은 기다림 분포의 무작위 매수 runs 개와 견줌 → (요약 dict, 무작위 원자료)."""
    st = en.stats(run)
    waits = en.method_waits(run, s)
    mc = en.random_entry(table, waits, s, e, runs=runs, seed=seed)
    rates = mc["rates"][~np.isnan(mc["rates"])]
    obs = st["success_rate"]
    up, dn = float((rates >= obs - 1e-12).mean()), float((rates <= obs + 1e-12).mean())
    summ = {"rand_mean": float(rates.mean()), "rand_p5": float(np.percentile(rates, 5)), "rand_p95": float(np.percentile(rates, 95)),
            "rand_trades_median": float(np.median(mc["trades"])), "p_two": min(1.0, 2 * min(up, dn)), "share_random_ge": up,
            "outside_90": bool(obs < np.percentile(rates, 5) or obs > np.percentile(rates, 95)), "runs": runs, "seed": seed,
            "waits_median": float(np.median(waits)), "waits_n": int(len(waits))}
    return summ, mc


def running_random(mc):
    """날짜마다 그날까지 판정 난 것으로 센 무작위 계좌 성공률: 평균·5번째·95번째 (계좌 절반 이상이 판정 1개 이상인 날부터 — 그 전은 NaN)."""
    W, L = mc["wins"], mc["losses"]
    dec = W + L
    with np.errstate(invalid="ignore", divide="ignore"), warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)          # 판정이 하나도 없는 날의 평균 (NaN 으로 둠 — 결과와 무관)
        rate = np.where(dec > 0, W / np.maximum(dec, 1), np.nan)
        enough = (dec > 0).mean(axis=0) >= 0.5
        mean = np.where(enough, np.nanmean(rate, axis=0), np.nan)
        p5 = np.where(enough, np.nanpercentile(rate, 5, axis=0), np.nan)
        p95 = np.where(enough, np.nanpercentile(rate, 95, axis=0), np.nan)
    return mean, p5, p95


def facts(run, mc, dates, s, e, min_dec=20):
    """대본에 쓸 수 있는 사실 (모두 그 방법 거래·무작위 계좌에서 계산): 연속 성공·실패 · 2020년 2~4월·2022년 판정 · 가장 긴 현금 기다림 ·
    그날까지 성공률이 무작위 평균보다 가장 앞섰던·뒤졌던 때 (방법 판정 min_dec 개 이후)."""
    T = run.trades
    dec = [t for t in T if t.get("result") is not None]
    out = {}
    best = {"win": (0, None, None), "loss": (0, None, None)}
    cur, n, a = None, 0, None
    for t in dec:
        if t["result"] == cur:
            n += 1
        else:
            cur, n, a = t["result"], 1, t
        if n > best[cur][0]:
            best[cur] = (n, a["buy_date"], t["hit_date"])
    out["streak"] = {k: {"n": v[0], "from_buy": v[1], "to_hit": v[2]} for k, v in best.items()}
    def window(a, b):
        x = [t for t in dec if a <= t["hit_date"] <= b]
        return {"wins": sum(t["result"] == "win" for t in x), "losses": sum(t["result"] == "loss" for t in x), "from": a, "to": b}
    out["covid"] = window("2020-02-19", "2020-04-30")
    out["y2022"] = window("2022-01-01", "2022-12-31")
    waits = []
    prev = s - 1
    for t in T:
        waits.append((t["buy_i"] - prev - 1, prev, t["buy_i"]))
        if t["open"]:
            break
        prev = t["sell_i"]
    w = max(waits)
    out["longest_cash"] = {"days": int(w[0]), "after": str(dates[max(w[1], s)].date()), "buy": str(dates[w[2]].date())}
    out["by_year"] = {}
    for y in sorted({t["hit_date"][:4] for t in dec}):
        x = [t for t in dec if t["hit_date"].startswith(y)]
        out["by_year"][y] = {"wins": sum(t["result"] == "win" for t in x), "losses": sum(t["result"] == "loss" for t in x)}
    mean, _, _ = running_random(mc)
    Wc = np.zeros(e - s + 1, int); Lc = np.zeros(e - s + 1, int)
    for t in dec:
        (Wc if t["result"] == "win" else Lc)[t["hit_i"] - s] += 1
    Wc, Lc = np.cumsum(Wc), np.cumsum(Lc)
    ok = (Wc + Lc >= min_dec) & ~np.isnan(mean)
    diff = np.where(ok, Wc / np.maximum(Wc + Lc, 1) - mean, np.nan)
    if ok.any():
        i_hi, i_lo = int(np.nanargmax(diff)), int(np.nanargmin(diff))
        out["lead"] = {"pp": float(diff[i_hi]), "date": str(dates[s + i_hi].date()), "rate": float(Wc[i_hi] / (Wc[i_hi] + Lc[i_hi])), "rand": float(mean[i_hi]), "decided": int(Wc[i_hi] + Lc[i_hi])}
        out["lag"] = {"pp": float(diff[i_lo]), "date": str(dates[s + i_lo].date()), "rate": float(Wc[i_lo] / (Wc[i_lo] + Lc[i_lo])), "rand": float(mean[i_lo]), "decided": int(Wc[i_lo] + Lc[i_lo])}
        out["share_days_ahead"] = float(np.nanmean(diff[ok] > 0))
    since = dates[s:e + 1] >= pd.Timestamp("2023-01-01")
    out["max_abs_diff_since_2023"] = float(np.nanmax(np.abs(diff[since & ok]))) if (since & ok).any() else None
    out["year_end"] = {}                                         # 해마다 마지막 거래일: 그날까지 성공률 · 무작위 평균
    yrs = pd.Series(np.arange(e - s + 1), index=dates[s:e + 1]).groupby(dates[s:e + 1].year).max()
    for y, j in yrs.items():
        if Wc[j] + Lc[j] and not np.isnan(mean[j]):
            out["year_end"][str(y)] = {"date": str(dates[s + j].date()), "rate": float(Wc[j] / (Wc[j] + Lc[j])), "rand": float(mean[j]),
                                       "wins": int(Wc[j]), "losses": int(Lc[j])}
    return out


def main():
    setup_log()
    t0 = time.time()
    spy, meta_s = bd.yahoo_daily("SPY"); vix_df, meta_v = bd.yahoo_daily("^VIX")
    close, tr, vix = spy["close"], spy["tr"], vix_df["close"]
    END = str(close.index[-1].date())
    log("DATA", spy=f"{close.index[0].date()}~{END} rows={len(close)}", vix=f"{vix.index[0].date()}~{vix.index[-1].date()}", use=f"{START}~{END}",
        sell=f"+{N:.0%} 성공 / −{M:.0%} 실패 (종가) → 다음 날 종가", cost=COST, runs=RUNS, seed=SEED)
    dates = close.index
    s0, e0 = int(dates.searchsorted(pd.Timestamp(START))), len(close) - 1
    mchoice = choose_m(close, s0, e0)
    out, ind, (s, e) = run_period(close, tr, vix, START, END, (M, N), "main")
    table = en.barrier_table(ind["close"], s, e, M, N)
    freq = {}
    for k in KEYS:
        sig = np.array([bool(en.ALL_RULES[k][0](ind, d)) for d in range(s, e + 1)])
        dd = np.flatnonzero(sig)
        freq[k] = {"share_days": float(sig.mean()), "episodes": int(np.sum(np.diff(np.r_[-10, dd]) > 1))}
    ev = event_level(ind, s, e, (M, N), KEYS)
    p0 = ev["any"]["success_rate"]
    rows, mcs = {}, {}
    for j, k in enumerate(KEYS):
        r, st = out[k]
        summ, mc = vs_random(r, table, s, e, RUNS, SEED + j)
        mcs[k] = mc
        nn = st["wins"] + st["losses"]
        mism = sum(1 for t in r.trades if (t.get("result") == "win" and not t["open"] and t["ret"] < 0) or (t.get("result") == "loss" and not t["open"] and t["ret"] > 0))
        rows[k] = {**st, **summ, "decided": nn, "vs_rand_pp": st["success_rate"] - summ["rand_mean"], "event": ev[k], "freq": freq[k], "label_ret_mismatch": mism,
                   "facts": facts(r, mc, dates, s, e)}
        log("RESULT", rule=k, trades=len(r.trades), decided=nn, wins=st["wins"], losses=st["losses"], rate=f"{st['success_rate']:.1%}",
            random=f"{summ['rand_mean']:.1%} [{summ['rand_p5']:.1%}~{summ['rand_p95']:.1%}]", vs_random=f"{rows[k]['vs_rand_pp'] * 100:+.1f}%p",
            p=f"{summ['p_two']:.2f}", outside90=summ["outside_90"], days_to_decide=f"{st['avg_days_to_decide']:.0f}", invested=f"{st['invested_share']:.0%}")
    rank = sorted(en.ORDER_V4, key=lambda k: (-rows[k]["success_rate"], -rows[k]["wins"]))
    checks = {}
    for m in CHECK_M:
        o, ind_c, _ = run_period(close, tr, vix, START, END, (m, N), f"check_m{m:.3f}")
        tb = en.barrier_table(ind_c["close"], s, e, m, N)
        c = {"every_day": event_level(ind_c, s, e, (m, N), ["any"])["any"]["success_rate"]}
        for j, k in enumerate(en.ORDER_V4):
            sm, _ = vs_random(o[k][0], tb, s, e, RUNS_CHECK, SEED + 100 + j)
            c[k] = {"rate": o[k][1]["success_rate"], "wins": o[k][1]["wins"], "losses": o[k][1]["losses"], **{x: sm[x] for x in ("rand_mean", "rand_p5", "rand_p95", "p_two", "outside_90")}}
        checks[f"m{m:.3f}"] = c
    o_long, ind_long, (sl, el) = run_period(close, tr, vix, LONG[0], LONG[1], (M, N), "long1994_2015")
    tbl = en.barrier_table(ind_long["close"], sl, el, M, N)
    c = {"every_day": event_level(ind_long, sl, el, (M, N), ["any"])["any"]["success_rate"], "start": str(dates[sl].date()), "end": str(dates[el].date())}
    for j, k in enumerate(en.ORDER_V4):
        sm, _ = vs_random(o_long[k][0], tbl, sl, el, RUNS_CHECK, SEED + 200 + j)
        c[k] = {"rate": o_long[k][1]["success_rate"], "wins": o_long[k][1]["wins"], "losses": o_long[k][1]["losses"], **{x: sm[x] for x in ("rand_mean", "rand_p5", "rand_p95", "p_two", "outside_90")}}
    checks["long1994_2015"] = c
    for g, c in checks.items():
        log("RESULT", check=g, every_day=f"{c['every_day']:.1%}", above_band=sum(c[k]["outside_90"] and c[k]["rate"] > c[k]["rand_p95"] for k in en.ORDER_V4),
            below_band=sum(c[k]["outside_90"] and c[k]["rate"] < c[k]["rand_p5"] for k in en.ORDER_V4),
            rates=",".join(f"{k}:{c[k]['rate']:.0%}/{c[k]['rand_mean']:.0%}" for k in en.ORDER_V4))
    res = {
        "version": VERSION, "engine": en.VERSION, "made_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "note": "연구·교육용. 투자 권유가 아니다. 과거 결과는 미래를 보장하지 않는다. 대본·화면 숫자는 이 파일에서만.",
        "params": {"asset": "SPY (S&P 500 ETF) 일별 — 신호·성공 판정은 종가, 계좌 값은 배당 재투자 총수익", "start": str(dates[s].date()), "end": str(dates[e].date()),
                   "capital": CAPITAL, "cost": COST, "m": M, "n": N, "runs": RUNS, "runs_check": RUNS_CHECK, "seed": SEED,
                   "success": f"산 값보다 +{N:.0%} 종가가 −{M:.0%} 종가보다 먼저 나오면 성공 (그날 판정 → 다음 거래일 종가에 매도)",
                   "buy_timing": "신호 = 그날 종가까지, 매수 = 다음 거래일 종가 · 들고 있는 동안 새로 사지 않음 · 매도한 날 신호가 있으면 다음 날 다시 매수",
                   "baseline": f"무작위 매수 = 신호 없이 날짜만 무작위 (매도한 날 뒤 기다리는 거래일 수를 그 방법의 실제 기다림에서 무작위로 뽑음 — 같은 매도 규칙) {RUNS}개, 시드 {SEED}+순번",
                   "threshold_basis": "매수 방법 문턱은 v1.0 그대로 (10년 동안 신호가 나온 날·묶음 수만 보고 정함 — 성공률을 보지 않음)",
                   "m_basis": "m 은 1~2% 안에서 자료 성질(choose_m)만 보고 정함 — 매수 방법 결과를 보기 전",
                   "rules": {k: {"name": en.ALL_RULES[k][1], "condition": en.ALL_RULES[k][2]} for k in KEYS}},
        "data": {k: {kk: v.get(kk) for kk in ("url", "fetched_at", "sha256", "first", "last", "rows")} for k, v in {"spy": meta_s, "vix": meta_v}.items()},
        "choose_m": mchoice,
        "base": {"every_day": p0, "every_day_decided": ev["any"]["decided"], "sequential_any": out["any"][1]["success_rate"]},
        "rules": rows, "rank_by_success": rank,
        "trades": {k: out[k][0].trades for k in KEYS},
        "checks": checks,
    }
    (HERE / "results.json").write_text(json.dumps(res, ensure_ascii=False, indent=1, default=float), "utf-8")
    pd.DataFrame([{"rule": k, "buy_date": t["buy_date"], "buy_price": round(t["buy_price"], 2), "target": round(t["target"], 2), "stop": round(t["stop"], 2),
                   "result": t["result"], "hit_date": t.get("hit_date"), "sell_date": t["sell_date"], "sell_price": round(t["sell_price"], 2),
                   "days": t["days"], "ret": round(t["ret"], 6), "open": t["open"]} for k in KEYS for t in out[k][0].trades]).to_csv(HERE / "trades.csv", index=False)
    write_md(res)
    write_anim(close, ind, out, s, e, res, mcs)
    log("DONE", files="results.json,results.md,trades.csv,anim.js,run.log", sec=f"{time.time() - t0:.1f}")


def pc(x, d=1):
    return "—" if x is None or (isinstance(x, float) and np.isnan(x)) else f"{x * 100:.{d}f}%"


def write_md(res):
    P, R, B, C = res["params"], res["rules"], res["base"], res["choose_m"]
    L = [f"# 매수 방법 10가지 — 성공률 vs 무작위 매수 (`barrier/run.py` {VERSION}, 엔진 `entry.py` {res['engine']}, {res['made_at']})", "",
         "> 연구·교육용. 투자 권유가 아니다. 과거 결과는 미래를 보장하지 않는다. 숫자는 이 파일·`results.json` 의 코드 출력만 쓴다.", "",
         f"- 자산: {P['asset']} · 기간 {P['start']} ~ {P['end']} · 시작 돈 $10,000 · 수수료 {P['cost']:.2%}",
         f"- **성공 = {P['success']}**", f"- 매수: {P['buy_timing']}", f"- **기준 = {P['baseline']}**", f"- 문턱: {P['threshold_basis']}", f"- m: {P['m_basis']}",
         f"- 참고: 날마다 샀다면 {pc(B['every_day'])} ({B['every_day_decided']}일) · 매도 다음 날 바로 다시 매수 {pc(B['sequential_any'])}", "",
         "## 0. m 고르기 — 자료 성질 (매수 방법 결과를 보기 전)", "",
         f"- SPY 하루 변동 표준편차 {pc(C['daily_std'], 2)} · 하루 ±1% 이상 움직인 날 {pc(C['share_abs_ge_1pct'])} · ±2% 이상 {pc(C['share_abs_ge_2pct'])} · −2% 이하 {pc(C['share_down_le_2pct'])}", "",
         "| m (실패) | 날마다 샀다면 성공률 | 실패 중 산 다음 날 바로 정해진 몫 | 판정까지 거래일 (중앙) |", "|---:|---:|---:|---:|"]
    for m, v in C["m"].items():
        L.append(f"| −{float(m) * 100:g}% | {pc(v['every_day'])} | {pc(v['fail_day1_of_fails'])} | {v['days_median']:.0f} |")
    L += ["", f"→ **m = {P['m']:.0%}** (1% 는 하루 보통 흔들림 안쪽이라 산 다음 날 하루가 실패를 정하는 일이 잦음 · 사용자 범위 1~2% 안에서 가장 넓은 값)", "",
          f"## 1. 본 실험 (−{P['m']:.0%} / +{P['n']:.0%}, 성공률 순)", "",
          "| # | 매수 방법 | 조건 | 성공 | 실패 | 성공률 | 무작위 평균 | 무작위 90% 범위 | 차이 | p (양쪽) | 판정까지 평균 | 주식 보유 | 판정과 수익 부호가 다른 거래 |",
          "|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for i, k in enumerate(res["rank_by_success"], 1):
        r = R[k]
        L.append(f"| {i} | {P['rules'][k]['name']} | {P['rules'][k]['condition']} | {r['wins']} | {r['losses']} | {pc(r['success_rate'])} | {pc(r['rand_mean'])} | "
                 f"{pc(r['rand_p5'])}~{pc(r['rand_p95'])} | {r['vs_rand_pp'] * 100:+.1f}%p | {r['p_two']:.2f} | {r['avg_days_to_decide']:.0f}일 | {pc(r['invested_share'], 0)} | {r['label_ret_mismatch']} |")
    a = R["any"]
    L.append(f"| — | *{P['rules']['any']['name']}* | {P['rules']['any']['condition']} | {a['wins']} | {a['losses']} | {pc(a['success_rate'])} | {pc(a['rand_mean'])} | — | — | — | {a['avg_days_to_decide']:.0f}일 | {pc(a['invested_share'], 0)} | {a['label_ret_mismatch']} |")
    L += ["", "## 2. 확인 — m 을 바꾸면 · 다른 기간 (성공률 / 무작위 평균, ▲▼ = 무작위 90% 범위 밖)", "",
          "| 매수 방법 | " + " | ".join(res["checks"]) + " |", "|---|" + "---:|" * len(res["checks"])]
    for k in en.ORDER_V4:
        cells = []
        for g, c in res["checks"].items():
            x = c[k]; mark = (" ▲" if x["rate"] > x["rand_p95"] else " ▼") if x["outside_90"] else ""
            cells.append(f"{pc(x['rate'])} / {pc(x['rand_mean'])}{mark} ({x['wins']}/{x['wins'] + x['losses']}, p {x['p_two']:.2f})")
        L.append(f"| {P['rules'][k]['name']} | " + " | ".join(cells) + " |")
    L.append("| *날마다 샀다면* | " + " | ".join(pc(c["every_day"]) for c in res["checks"].values()) + " |")
    L += ["", "## 3. 한계", "",
          "- 성공·실패는 종가로만 본다 (장중 고가·저가는 없음). 판정 다음 날 종가에 매도해 실제 수익률은 +5%·−2% 와 다르다 (마지막 칸: 성공인데 손해·실패인데 이익인 거래 수).",
          f"- 무작위 매수는 {P['runs']}개 계좌 (시드 고정). p = 무작위 계좌가 그 방법만큼 (위든 아래든) 벗어난 몫 × 2. 방법 10개를 한꺼번에 보므로 p 0.1 하나쯤은 우연으로도 나온다.",
          "- 무작위는 방법마다 기다림 분포를 맞췄다 (같은 횟수·쉬는 기간 → 날짜만 다름). 날마다 샀다면 은 모든 날을 따로 센 참고값 (겹쳐서 독립이 아님).",
          "- 이 기간(2016~2026)은 오른 시장이다. 다른 기간은 2번 표 (1994~2015) 로만 확인했다."]
    (HERE / "results.md").write_text("\n".join(L) + "\n", "utf-8")


def write_anim(close, ind, out, s, e, res, mcs):
    d = close.index[s:e + 1]; sl = slice(s, e + 1)
    r2 = lambda a: [None if (x is None or (isinstance(x, float) and np.isnan(x))) else round(float(x), 2) for x in a]
    AN = {"v": VERSION, "made_at": res["made_at"], "dates": [x.strftime("%Y-%m-%d") for x in d], "close": r2(close.iloc[sl]), "ticker": "SPY",
          "lines": {"sma5": r2(ind["sma5"][sl]), "sma20": r2(ind["sma20"][sl]), "hi20": r2(ind["hi20"][sl]), "max20": r2(ind["max20"][sl]),
                    "ath": r2(ind["ath"][sl]), "rsi14": r2(ind["rsi14"][sl]), "vix": r2(ind["vix"][sl]), "ret1": r2(ind["ret1"][sl] * 100),
                    "close_21ago": [round(float(close.iloc[i - 21]), 2) for i in range(s, e + 1)]},
          "m": M, "n": N, "cost": COST, "capital": CAPITAL, "runs": RUNS, "order": en.ORDER_V4, "base": res["base"], "rules": {}}
    for k in KEYS:
        r, st = out[k]
        W, L = mcs[k]["wins"], mcs[k]["losses"]
        dec = W + L
        with np.errstate(invalid="ignore", divide="ignore"):
            rate = np.where(dec > 0, W / np.maximum(dec, 1), np.nan)
        mean, p5, p95 = running_random(mcs[k])
        pm = lambda a: [None if np.isnan(x) else int(round(x * 1000)) for x in a]     # 천분율 정수 (파일 크기)
        R = res["rules"][k]
        AN["rules"][k] = {"holding": "".join("1" if h else "0" for h in r.holding),
                          "trades": [{"b": t["buy_i"] - s, "s": t["sell_i"] - s, "h": (t["hit_i"] - s) if t.get("hit_i") is not None else None,
                                      "bp": round(t["buy_price"], 2), "sp": round(t["sell_price"], 2), "tg": round(t["target"], 2), "sl": round(t["stop"], 2),
                                      "res": {"win": "w", "loss": "l"}.get(t["result"]), "r": round(t["ret"], 6), "open": t["open"]} for t in r.trades],
                          "rate": st["success_rate"], "wins": st["wins"], "losses": st["losses"],
                          "rnd": {"mean": pm(mean), "p5": pm(p5), "p95": pm(p95)},
                          "rndFinal": {x: R[x] for x in ("rand_mean", "rand_p5", "rand_p95", "p_two", "outside_90", "rand_trades_median")}}
        w = sum(t["res"] == "w" for t in AN["rules"][k]["trades"]); l = sum(t["res"] == "l" for t in AN["rules"][k]["trades"])
        assert (w, l) == (R["wins"], R["losses"]), k
        assert len(AN["rules"][k]["holding"]) == len(AN["dates"]) == len(AN["rules"][k]["rnd"]["mean"]), k
        assert abs((AN["rules"][k]["rnd"]["mean"][-1] or 0) / 1000 - R["rand_mean"]) < 0.0015, (k, "무작위 평균 끝 값 = 요약")
    AN["summary"] = {"rank": res["rank_by_success"], "rates": {k: res["rules"][k]["success_rate"] for k in KEYS},
                     "checks": res["checks"], "choose_m": res["choose_m"],
                     "mismatch": {k: res["rules"][k]["label_ret_mismatch"] for k in en.ORDER_V4},
                     "share_random_ge": {k: res["rules"][k]["share_random_ge"] for k in en.ORDER_V4},
                     "by_year": {k: res["rules"][k]["facts"]["by_year"] for k in en.ORDER_V4}}
    txt = ("// 자동 생성 — stock/source/eonje-maesu-2026-10/backtest/barrier/run.py " + VERSION + " (손으로 고치지 않음). 연구·교육용 — 투자 권유 아님.\n"
           "window.AN = " + json.dumps(AN, ensure_ascii=False, separators=(",", ":")) + ";\n")
    (HERE / "anim.js").write_text(txt, "utf-8")
    log("RESULT", anim="anim.js", days=len(d), kb=round(len(txt) / 1024))


if __name__ == "__main__":
    main()
