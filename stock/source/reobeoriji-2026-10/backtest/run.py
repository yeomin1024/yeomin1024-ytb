# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-16 — 최초. 주식 4번 레버리지 1·2·3배를 오래 모으면 (사용자 지시 2026-10-16 "이제 니즈에 따라 어떻게 테스트 계획 세우고 하는지
#          알겠지? 같은 방식으로 필요한 소스 생성해서 3개 영상 미리보기 영상 만들어봐"). 계획(결과를 보기 전에 정함 — ../README.md 1번):
#          1배 = QQQ 총수익(실제) · 2배·3배 = 나스닥100 총수익 하루 수익률 × L − 빌린 몫 이자(전날 13주 국채 + 웃돈 s) − 보수 0.95% (매일 배수 맞춤 — QLD·TQQQ 와 같은 구조)
#          · 웃돈 s 는 실제 QLD(2006~, 가장 김)의 끝 값이 맞도록 한 번 정하고, 같은 s 로 TQQQ(2010~)를 맞춰 봄 (따로 맞추지 않음 — 확인)
#          · 본 실험 = 1999-04-01 부터 매달 첫 거래일 $500 씩 세 계좌에 똑같이 매수 (수수료 0.25%) ~ 2026-10-15 (닷컴 하락 포함)
#          · 확인 = 처음에 한 번 $10,000 · 시작 달을 바꾼 10년 적립 계좌 전부 · 실제 QLD·TQQQ 로 2010-03 부터 적립 · 25년 적립 계좌.
"""레버리지 백테스트 (연구·교육용 — 투자 권유가 아니다. 과거 결과는 미래를 보장하지 않는다).
실행: python3 stock/source/reobeoriji-2026-10/backtest/run.py   → results.json · results.md · run.log · anim.js
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
from backtest import data as bd          # noqa: E402
from backtest import leverage as lv      # noqa: E402

VERSION = "v1.0"
END, UNTIL = "2026-10-15", "2026-10-16"
MONTHLY, LUMP, FEE = 500.0, 10_000.0, 0.0025
ER_LEV, ER_QQQ = 0.0095, 0.0020          # 2·3배 보수 0.95% (QLD·TQQQ 설명서 총보수 수준) · QQQ 0.20% (총수익에 이미 들어 있음 — 지수 총수익을 만들 때 되더함)
START = "1999-04-01"                     # QQQ 상장(1999-03-10) 다음 달 첫 거래일
REAL_START = "2010-03-01"                # TQQQ 상장(2010-02-11) 다음 달 첫 거래일
ROLL_YEARS = 10
LS = (1, 2, 3)


def setup_log():
    fmt = logging.Formatter("%(message)s")
    root = logging.getLogger(); root.setLevel(logging.INFO)
    for h in list(root.handlers):
        root.removeHandler(h)
    for h in (logging.FileHandler(HERE / "run.log", "w", "utf-8"), logging.StreamHandler(sys.stdout)):
        h.setFormatter(fmt); root.addHandler(h)


def log(stage, **kv):
    logging.getLogger("run").info("[%s] %s %s", stage, time.strftime("%Y-%m-%dT%H:%M:%S"), " ".join(f"{k}={v}" for k, v in kv.items()))


def rint(x):
    return int(np.floor(float(x) + 0.5))


def load(sym, **kw):
    df, meta = bd.yahoo_daily(sym, **kw)
    df = df.loc[:END]
    log("DATA", symbol=sym, rows=len(df), first=str(df.index[0].date()), last=str(df.index[-1].date()), sha256=meta.get("sha256", "?")[:12])
    return df


def fit_spread(idx_tr, irx, real_tr, L):
    """흉내 끝 값 = 실제 끝 값이 되는 웃돈 s (이분법, 연 −2~5%)."""
    lo, hi = -0.02, 0.05
    for _ in range(60):
        mid = (lo + hi) / 2
        r = lv.daily_returns(idx_tr, irx, L, ER_LEV, mid)
        ix = r.index.intersection(real_tr.index)
        sim = float((1 + r.loc[ix].iloc[1:]).prod()); real = float(real_tr.loc[ix].iloc[-1] / real_tr.loc[ix].iloc[0])
        if sim > real:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def maxdd(v, dates, a=None, b=None):
    s = pd.Series(v, index=dates).loc[a:b]
    peak = s.cummax(); dd = s / peak - 1
    i = int(np.argmin(dd.to_numpy())); j = int(np.argmax(s.to_numpy()[:i + 1]))
    return {"peak_date": str(s.index[j].date()), "trough_date": str(s.index[i].date()), "dd": round(float(dd.iloc[i]), 6)}


def summ(g, label):
    out = {"label": label}
    for L in LS:
        x = g[L]
        out[f"x{L}"] = round(float(x["val"][-1]), 2)
    out["paid"] = rint(g[1]["paid"][-1]); out["start"] = str(g[1]["dates"][0].date()); out["end"] = str(g[1]["dates"][-1].date())
    out["years"] = round((g[1]["dates"][-1] - g[1]["dates"][0]).days / 365.25, 2)
    out["x2_over_x1"] = round(out["x2"] / out["x1"], 4); out["x3_over_x1"] = round(out["x3"] / out["x1"], 4)
    log("RESULT", **out)
    return out


def main():
    setup_log()
    t0 = time.time()
    log("RUN", version=VERSION, engine=lv.VERSION, monthly=MONTHLY, lump=LUMP, fee=FEE, er_lev=ER_LEV, end=END, note="연구·교육용 — 투자 권유 아님")
    qqq, qld, tqqq = load("QQQ", until=UNTIL), load("QLD", until=UNTIL), load("TQQQ", until=UNTIL)
    irx = bd.yahoo_daily("^IRX")[0]["close"].loc[:END]
    tr = qqq["tr"]
    days = pd.Series(tr.index, index=tr.index).diff().dt.days.fillna(0)
    idx_tr = (1 + tr.pct_change().fillna(0) + ER_QQQ * days / 365).cumprod()       # 나스닥100 총수익 ≈ QQQ 총수익 + 보수 0.20%
    # 웃돈 s: QLD 로 정하고 TQQQ 로 확인
    s = fit_spread(idx_tr, irx, qld["tr"], 2)
    track = {"spread": round(s, 5), "qld": lv.track(lv.daily_returns(idx_tr, irx, 2, ER_LEV, s), qld["tr"], "QLD (s 를 맞춘 곳)"),
             "tqqq": lv.track(lv.daily_returns(idx_tr, irx, 3, ER_LEV, s), tqqq["tr"], "TQQQ (같은 s — 확인)"),
             "tqqq_s0": lv.track(lv.daily_returns(idx_tr, irx, 3, ER_LEV, 0.0), tqqq["tr"], "TQQQ (s=0)")}
    s3 = fit_spread(idx_tr, irx, tqqq["tr"], 3)
    track["spread_if_fit_tqqq"] = round(s3, 5)
    log("FIT", spread=round(s, 5), spread_tqqq_alone=round(s3, 5), tqqq_cagr_gap=round(track["tqqq"]["cagr_gap"], 5), tqqq_end_ratio=round(track["tqqq"]["end_ratio_sim_over_real"], 4))
    R = {1: tr.pct_change().fillna(0.0).rename("x1")}
    for L in (2, 3):
        R[L] = lv.daily_returns(idx_tr, irx, L, ER_LEV, s)
    res = {"version": VERSION, "engine": lv.VERSION, "monthly": MONTHLY, "lump": LUMP, "fee": FEE, "er_lev": ER_LEV, "end": END, "start": START, "track": track}
    # 장난감 예 (코드로 셈): +10% 다음 −10%
    res["toy"] = {f"x{L}": round((1 + 0.10 * L) * (1 - 0.10 * L) - 1, 4) for L in LS}
    # 가격 길 (1999-03-10 = 1) · 가장 크게 떨어진 폭
    lvl = {L: (1 + R[L].loc["1999-03-10":]).cumprod() for L in LS}
    res["dd_dotcom"] = {f"x{L}": maxdd(lvl[L].to_numpy(), lvl[L].index, "1999-03-10", "2002-12-31") for L in LS}
    res["dd_2008"] = {f"x{L}": maxdd(lvl[L].to_numpy(), lvl[L].index, "2007-06-01", "2009-06-30") for L in LS}
    res["dd_2022"] = {f"x{L}": maxdd(lvl[L].to_numpy(), lvl[L].index, "2021-06-01", "2023-06-30") for L in LS}
    res["level_end"] = {f"x{L}": round(float(lvl[L].iloc[-1]), 4) for L in LS}
    # 그 해가 제자리였는데 배수가 녹은 해 (자료 성질): 1배 연 수익률 |r|<5% 인 해
    yr = {}
    for y in range(2000, 2026):
        row = {}
        for L in LS:
            a0 = lvl[L].loc[:f"{y - 1}-12-31"].iloc[-1]; a1 = lvl[L].loc[:f"{y}-12-31"].iloc[-1]
            row[f"x{L}"] = round(float(a1 / a0 - 1), 4)
        yr[str(y)] = row
    res["year_ret"] = yr
    res["year_ret_exact"] = {y: {f"x{L}": float((lvl[L].loc[:f"{y}-12-31"].iloc[-1]) / (lvl[L].loc[:f"{int(y) - 1}-12-31"].iloc[-1]) - 1) for L in LS} for y in yr}
    log("YEARS", detail=",".join(f"{y}:{v['x1']:+.0%}/{v['x2']:+.0%}/{v['x3']:+.0%}" for y, v in yr.items()))
    log("DD", dotcom=res["dd_dotcom"], y2008=res["dd_2008"], y2022=res["dd_2022"])
    # 본 실험: 매달 $500
    G = {L: lv.grow(R[L], 0.0, MONTHLY, FEE, START, END) for L in LS}
    res["main"] = summ(G, "1·2·3배 매달 $500")
    res["facts"] = facts(G)
    # 한 번에 $10,000
    GL = {L: lv.grow(R[L], LUMP, 0.0, FEE, START, END) for L in LS}
    res["lump"] = summ(GL, "1·2·3배 한 번에 $10,000")
    res["lump_low"] = {f"x{L}": {"date": str(GL[L]["dates"][int(np.argmin(GL[L]["val"]))].date()), "val": round(float(GL[L]["val"].min()), 2)} for L in LS}
    # 실제 ETF (TQQQ 상장 뒤): QQQ·QLD·TQQQ 총수익으로 적립
    RR = {1: qqq["tr"].pct_change().fillna(0), 2: qld["tr"].pct_change().fillna(0), 3: tqqq["tr"].pct_change().fillna(0)}
    GR = {L: lv.grow(RR[L], 0.0, MONTHLY, FEE, REAL_START, END) for L in LS}
    res["real"] = summ(GR, "실제 QQQ·QLD·TQQQ 매달 $500")
    GS = {L: lv.grow(R[L], 0.0, MONTHLY, FEE, REAL_START, END) for L in LS}
    res["real_sim"] = summ(GS, "흉내 1·2·3배 매달 $500 (같은 기간)")
    res["real_dd2022"] = {f"x{L}": maxdd(GR[L]["val"], GR[L]["dates"], "2021-06-01", "2023-06-30") for L in LS}
    # 시작 달을 바꾼 10년 적립 계좌
    res["rolling"] = rolling(R, ROLL_YEARS)
    res["rolling25"] = rolling(R, 25)
    (HERE / "results.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), "utf-8")
    write_md(res)
    write_anim(G, res, GL, GR, GS)
    log("RUN", done=True, sec=round(time.time() - t0, 1))


def facts(G):
    d = G[1]["dates"]; paid = G[1]["paid"]; V = {L: G[L]["val"] for L in LS}
    S = lambda i: str(d[i].date())
    F = {"year": {}}
    for y in sorted(set(d.year)):
        k = np.flatnonzero(d.year == y)[-1]
        F["year"][int(y)] = {"date": S(k), "paid": rint(paid[k]), **{f"x{L}": round(float(V[L][k]), 2) for L in LS}}
    # 닷컴: 2002 바닥 (그 해 가장 낮은 날) · 넣은 돈 대비
    for key, (a, b) in {"dot": ("2000-01-01", "2003-03-31"), "gfc": ("2008-01-01", "2009-06-30"), "covid": ("2020-01-01", "2020-04-30"), "y2022": ("2022-01-01", "2023-01-31"), "y2025": ("2025-01-01", "2025-06-30")}.items():
        m = np.flatnonzero((d >= pd.Timestamp(a)) & (d <= pd.Timestamp(b)))
        row = {}
        for L in LS:
            lo = m[int(np.argmin(V[L][m]))]; hi = m[int(np.argmax(V[L][m[:list(m).index(lo) + 1]]))]
            row[f"x{L}"] = {"high_date": S(hi), "high": round(float(V[L][hi]), 2), "low_date": S(lo), "low": round(float(V[L][lo]), 2),
                            "drop": round(float(V[L][lo] / V[L][hi] - 1), 6), "paid_low": rint(paid[lo]), "vs_paid_low": round(float(V[L][lo] / paid[lo] - 1), 6)}
        F[key] = row
    # 넣은 돈을 처음 넘은 날 · 다시 아래로 간 마지막 날 (그날까지)
    for L in LS:
        above = V[L] >= paid
        ch = np.flatnonzero(above[1:] != above[:-1]) + 1
        F[f"x{L}_above_paid_share"] = round(float(above.mean()), 4)
        F[f"x{L}_last_cross"] = S(int(ch[-1])) if len(ch) else None
        F[f"x{L}_last_cross_up"] = bool(above[ch[-1]]) if len(ch) else None
    # 순위가 바뀐 날 (3배가 1배를 처음 앞선 날 · 그 뒤 마지막 바뀜)
    ab = V[3] > V[1]
    ch = np.flatnonzero(ab[2:] != ab[1:-1]) + 2
    F["x3_vs_x1_changes"] = [{"date": S(i), "x3_ahead": bool(ab[i])} for i in ch]
    ab2 = V[2] > V[1]; ch2 = np.flatnonzero(ab2[2:] != ab2[1:-1]) + 2
    F["x2_vs_x1_changes"] = [{"date": S(i), "x2_ahead": bool(ab2[i])} for i in ch2]
    last_up = [c for c in F["x3_vs_x1_changes"] if c["x3_ahead"]][-1]["date"]
    kk = int(np.flatnonzero(d >= pd.Timestamp(last_up))[0])
    F["x3_ahead_since"] = {"date": last_up, "stayed": bool((V[3][kk:] > V[1][kk:]).all()), "share_before": round(float((V[3][:kk] > V[1][:kk]).mean()), 4),
                           "years_before": round((d[kk] - d[0]).days / 365.25, 2)}
    F["milestones"] = {f"x{L}": {str(t): (S(int(np.flatnonzero(V[L] >= t)[0])) if (V[L] >= t).any() else None) for t in (100_000, 1_000_000, 10_000_000)} for L in LS}
    F["peak"] = {f"x{L}": {"date": S(int(np.argmax(V[L]))), "val": round(float(V[L].max()), 2)} for L in LS}
    log("FACTS", dot=F["dot"], gfc=F["gfc"], y2022=F["y2022"], x3_vs_x1=F["x3_vs_x1_changes"][:6], milestones=F["milestones"])
    return F


def rolling(R, years):
    d = R[1].loc[START:END].index
    m = d.to_period("M"); starts = np.flatnonzero(np.r_[True, m[1:] != m[:-1]])
    rows = []
    for sidx in starts:
        sd = d[sidx]; ed = sd + pd.DateOffset(years=years)
        if ed > d[-1]:
            break
        g = {L: lv.grow(R[L], 0.0, MONTHLY, FEE, sd, ed) for L in LS}
        rows.append({"start": str(sd.date()), "paid": rint(g[1]["paid"][-1]), **{f"x{L}": round(float(g[L]["val"][-1]), 2) for L in LS}})
    X = {L: np.array([r[f"x{L}"] for r in rows]) for L in LS}; P = np.array([r["paid"] for r in rows])
    rep = {"years": years, "windows": len(rows), "first_start": rows[0]["start"], "last_start": rows[-1]["start"],
           "x3_gt_x1": int((X[3] > X[1]).sum()), "x2_gt_x1": int((X[2] > X[1]).sum()), "x3_gt_x2": int((X[3] > X[2]).sum()),
           "x1_lt_paid": int((X[1] < P).sum()), "x2_lt_paid": int((X[2] < P).sum()), "x3_lt_paid": int((X[3] < P).sum()),
           "x3_best": {"start": rows[int(np.argmax(X[3] / X[1]))]["start"], "ratio": round(float((X[3] / X[1]).max()), 3)},
           "x3_worst": {"start": rows[int(np.argmin(X[3] / X[1]))]["start"], "ratio": round(float((X[3] / X[1]).min()), 4)},
           "x3_min": {"start": rows[int(np.argmin(X[3]))]["start"], "val": round(float(X[3].min()), 2), "paid": int(P[int(np.argmin(X[3]))])},
           "median_x3_over_x1": round(float(np.median(X[3] / X[1])), 3), "median_x2_over_x1": round(float(np.median(X[2] / X[1])), 3), "rows": rows}
    log("ROLL", **{k: v for k, v in rep.items() if k != "rows"})
    return rep


def money(x):
    return f"${x:,.0f}"


def write_md(res):
    L = [f"# 레버리지 1·2·3배 결과 ({res['version']}, 엔진 leverage {res['engine']}) — 자동 생성, 손으로 고치지 않음", "",
         "※ 연구·교육용 — 투자 권유 아님. 2·3배는 흉내 (실제 ETF 와 맞춘 웃돈 s — 아래). 과거 결과는 미래를 보장하지 않는다.", "",
         f"- 웃돈 s (QLD 로 맞춤) = {res['track']['spread']:.3%} · TQQQ 를 같은 s 로: 연 차이 {res['track']['tqqq']['cagr_gap']:+.2%}, 끝 값 비 ×{res['track']['tqqq']['end_ratio_sim_over_real']:.3f} (TQQQ 만으로 맞추면 s = {res['track']['spread_if_fit_tqqq']:.3%})", "",
         "| 실험 | 기간 | 넣은 돈 | 1배 | 2배 | 3배 | 2배÷1배 | 3배÷1배 |", "|---|---|---:|---:|---:|---:|---:|---:|"]
    for k in ("main", "lump", "real", "real_sim"):
        r = res[k]
        L.append(f"| {r['label']} | {r['start']}~{r['end']} ({r['years']}년) | {money(r['paid'])} | {money(r['x1'])} | {money(r['x2'])} | {money(r['x3'])} | ×{r['x2_over_x1']:.2f} | ×{r['x3_over_x1']:.2f} |")
    for nm in ("rolling", "rolling25"):
        ro = res[nm]
        L += ["", f"## 시작 달을 바꾼 {ro['years']}년 적립 계좌 {ro['windows']}개 ({ro['first_start']}~{ro['last_start']})", "",
              f"- 3배 > 1배 {ro['x3_gt_x1']} · 2배 > 1배 {ro['x2_gt_x1']} · 3배 > 2배 {ro['x3_gt_x2']} · 넣은 돈보다 적음: 1배 {ro['x1_lt_paid']} · 2배 {ro['x2_lt_paid']} · 3배 {ro['x3_lt_paid']}",
              f"- 3배÷1배 가장 큼 {ro['x3_best']} · 가장 작음 {ro['x3_worst']} · 가운데 ×{ro['median_x3_over_x1']}"]
    L += ["", "## 해 끝 (본 실험)", "", "| 해 | 넣은 돈 | 1배 | 2배 | 3배 |", "|---|---:|---:|---:|---:|"]
    for y, v in res["facts"]["year"].items():
        L.append(f"| {y} | {money(v['paid'])} | {money(v['x1'])} | {money(v['x2'])} | {money(v['x3'])} |")
    (HERE / "results.md").write_text("\n".join(L) + "\n", "utf-8")


def sample(g, keys, step=3):
    ix = sorted(set(range(0, len(g[1]["dates"]), step)) | {len(g[1]["dates"]) - 1})
    return {"dates": [g[1]["dates"][i].strftime("%Y-%m-%d") for i in ix], "paid": [rint(g[1]["paid"][i]) for i in ix],
            **{f"x{L}": [round(float(g[L]["val"][i]), 2) for i in ix] for L in keys}}


def write_anim(G, res, GL, GR, GS):
    d = G[1]["dates"]
    obj = {"version": VERSION, "start": res["start"], "end": res["end"], "dates": [x.strftime("%Y-%m-%d") for x in d], "paid": [rint(x) for x in G[1]["paid"]],
           **{f"x{L}": [rint(x) for x in G[L]["val"]] for L in LS},
           **{k: res[k] for k in ("main", "lump", "lump_low", "real", "real_sim", "real_dd2022", "facts", "toy", "dd_dotcom", "dd_2008", "dd_2022", "year_ret", "track", "level_end")},
           "rolling": {x: res["rolling"][x] for x in res["rolling"] if x != "rows"} | {"pts": [[r["start"], r["paid"], r["x1"], r["x2"], r["x3"]] for r in res["rolling"]["rows"]]},
           "rolling25": {x: res["rolling25"][x] for x in res["rolling25"] if x != "rows"},
           "lump_daily": sample(GL, LS), "real_daily": sample(GR, LS), "real_sim3": sample(GS, (3,))["x3"]}
    (HERE / "anim.js").write_text("// 자동 생성 (run.py " + VERSION + ") — 손으로 고치지 않음\nwindow.LV = " + json.dumps(obj, ensure_ascii=False, separators=(",", ":")) + ";\n", "utf-8")
    log("ANIM", days=len(d), bytes=(HERE / "anim.js").stat().st_size)


if __name__ == "__main__":
    main()
