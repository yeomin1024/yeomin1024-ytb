# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-16 — 최초 (같은 날 고침: 장면용 anim.js 에 XYLD·JEPI 짝 3거래일마다 값·반올림 0.5 올림·사실(facts)). 주식 2번 커버드콜 원금 (사용자 지시 2026-10-16 "이제 니즈에 따라 어떻게 테스트 계획 세우고 하는지 알겠지?
#          같은 방식으로 필요한 소스 생성해서 3개 영상 미리보기 영상 만들어봐"). 계획(결과를 보기 전에 정함 — ../README.md 1번):
#          본 실험 = QYLD(나스닥100 커버드콜) 계좌 vs QQQ(같은 나스닥100) 계좌, 같은 $100,000 · 같은 날 같은 금액을 꺼내 씀
#          (QYLD 분배금 전부 → QQQ 는 그 금액만큼 매도) · QYLD 첫 거래일 2013-12-12 ~ 2026-10-15 · 수수료 0.25% · 세전.
#          확인 = XYLD(S&P500 커버드콜) vs SPY · JEPI vs SPY · 원천징수 15% · 분배금을 다시 넣으면(총수익) · 시작 달을 바꾼 5년·3년 계좌 전부.
"""커버드콜 원금 백테스트 (연구·교육용 — 투자 권유가 아니다. 과거 결과는 미래를 보장하지 않는다).
실행: python3 stock/source/keobeodeu-kol-2026-10/backtest/run.py   → results.json · results.md · run.log · anim.js
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
from backtest import income as ic        # noqa: E402

VERSION = "v1.0"
END, UNTIL = "2026-10-15", "2026-10-16"          # 마지막 완결 거래일 (오늘 장중 값 뺌) — 1번 영상과 같은 끝
INITIAL, FEE = 100_000.0, 0.0025                 # 같은 $100,000 · 사고팔 때 0.25% (1번 영상과 같음)
PAIRS = {                                        # 이름: (분배 ETF, 지수 ETF) — 같은 지수를 따라가는 짝
    "main": ("QYLD", "QQQ"),                     # 나스닥100 커버드콜 vs 나스닥100
    "xyld": ("XYLD", "SPY"),                     # S&P500 커버드콜 vs S&P500
    "jepi": ("JEPI", "SPY"),                     # 저변동 주식 + 콜옵션 연계 채권(ELN) vs S&P500 (진화형 예)
}
TAX_CHECK = 0.15                                 # 원천징수 15% (많은 나라의 미국 배당 조약 세율 — 나라마다 다름, 세전이 본 실험)
ROLL_YEARS = [5, 3]                              # 시작 달을 바꾼 계좌 (달 첫 거래일마다 시작)
DOWN_REF = "2021-11-19"                          # 2022 하락 기준일 = QQQ 가 2022 바닥 전에 찍은 마지막 최고 종가 날 (자료로 확인 — 아래 down())


def setup_log():
    fmt = logging.Formatter("%(message)s")
    root = logging.getLogger(); root.setLevel(logging.INFO)
    for h in list(root.handlers):
        root.removeHandler(h)
    for h in (logging.FileHandler(HERE / "run.log", "w", "utf-8"), logging.StreamHandler(sys.stdout)):
        h.setFormatter(fmt); root.addHandler(h)


def log(stage, **kv):
    logging.getLogger("run").info("[%s] %s %s", stage, time.strftime("%Y-%m-%dT%H:%M:%S"), " ".join(f"{k}={v}" for k, v in kv.items()))


def load(sym):
    df, meta = bd.yahoo_daily(sym, until=UNTIL)
    df = df.loc[:END]
    log("DATA", symbol=sym, rows=len(df), first=str(df.index[0].date()), last=str(df.index[-1].date()), dividends=int((df["div"] > 0).sum()),
        sha256=meta.get("sha256", "?")[:12])
    return df


def yield_stats(df, start):
    """분배율 (자료 성질 — 결과 전): 해마다 받은 분배금 ÷ 그해 첫 종가."""
    d = df.loc[start:]
    out = {}
    for y, g in d.groupby(d.index.year):
        if len(g) < 200:
            continue
        out[int(y)] = round(float(g["div"].sum() / g["close"].iloc[0]), 4)
    return out


def summary(r, label):
    a, b, out = r["a_val"], r["b_val"], r["out_cum"]
    d = r["dates"]
    yrs = (d[-1] - d[0]).days / 365.25
    s = {"label": label, "start": str(d[0].date()), "end": str(d[-1].date()), "years": round(yrs, 2), "withdrawals": len(r["events"]),
         "out_total": round(float(out[-1]), 2), "a_end": round(float(a[-1]), 2), "b_end": round(float(b[-1]), 2),
         "a_vs_initial": round(float(a[-1] / INITIAL), 4), "b_vs_initial": round(float(b[-1] / INITIAL), 4),
         "b_over_a": round(float(b[-1] / a[-1]), 4), "a_min": round(float(a.min()), 2), "a_min_date": str(d[int(a.argmin())].date()),
         "b_min": round(float(b.min()), 2), "b_min_date": str(d[int(b.argmin())].date()),
         "a_below_initial_days_share": round(float((a < INITIAL).mean()), 4), "b_below_initial_days_share": round(float((b < INITIAL).mean()), 4),
         "a_price_start": round(float(r["a_close"][0]), 4), "a_price_end": round(float(r["a_close"][-1]), 4),
         "first_month_out": round(float(r["events"][0][1]), 2) if r["events"] else None,
         "last_12m_out": round(float(sum(c for i, c in r["events"] if (d[-1] - d[i]).days <= 365)), 2), "b_broke": r["b_broke"]}
    # 해마다 꺼낸 돈 · 해 끝 계좌 값
    by_year = {}
    for y in sorted(set(d.year)):
        m = np.flatnonzero(d.year == y)
        k = m[-1]
        by_year[int(y)] = {"out": round(float(sum(c for i, c in r["events"] if d[i].year == y)), 2),
                           "a": round(float(a[k]), 2), "b": round(float(b[k]), 2)}
    s["by_year"] = by_year
    log("RESULT", **{k: v for k, v in s.items() if k != "by_year"})
    return s


def down(r, ref):
    """2022 하락: ref 날 계좌 값 → 그날부터 2022-12-31 까지 가장 낮은 값(날) → ref 값을 다시 넘은 첫날 (없으면 None) · 끝 값."""
    d = r["dates"]
    k = int(d.get_indexer([pd.Timestamp(ref)])[0])
    if k < 0:
        raise ValueError(f"[DOWN] {ref} 가 거래일이 아님")
    k2 = int(np.flatnonzero(d <= pd.Timestamp("2022-12-31"))[-1])
    out = {}
    for key in ("a_val", "b_val"):
        v = r[key]
        lo = k + int(np.argmin(v[k:k2 + 1]))
        back = np.flatnonzero(v[lo:] >= v[k])
        rec = lo + int(back[0]) if len(back) else None
        out[key[0]] = {"ref": round(float(v[k]), 2), "low": round(float(v[lo]), 2), "low_date": str(d[lo].date()),
                       "drop": round(float(v[lo] / v[k] - 1), 4), "recovered": str(d[rec].date()) if rec is not None else None,
                       "recover_days": int((d[rec] - d[k]).days) if rec is not None else None,
                       "end_vs_ref": round(float(v[-1] / v[k] - 1), 4)}
    out["out_ref_to_end"] = round(float(r["out_cum"][-1] - r["out_cum"][k]), 2)
    log("DOWN", ref=ref, **{f"{k_}_{x}": y for k_, v_ in out.items() if isinstance(v_, dict) for x, y in v_.items()})
    return out


def rolling(inc, idx, years, tax=0.0):
    """달 첫 거래일마다 시작해 years 년 뒤(그날 또는 앞 거래일)까지 → 표."""
    A, B = ic.common(inc, idx, inc.index[0], END)
    starts = ic.month_starts(A.index)
    rows = []
    for s in starts:
        if s == 0:
            continue                                         # 첫 달은 상장 날 중간이라 달 첫 거래일이 아님 → 다음 달부터
        sd = A.index[s]
        ed = sd + pd.DateOffset(years=years)
        if ed > A.index[-1]:
            break
        r = ic.withdraw_pair(inc, idx, sd, ed, INITIAL, FEE, tax, quiet=True)
        rows.append({"start": str(sd.date()), "end": str(r["dates"][-1].date()), "a": round(float(r["a_val"][-1]), 2),
                     "b": round(float(r["b_val"][-1]), 2), "out": round(float(r["out_cum"][-1]), 2)})
    a = np.array([x["a"] for x in rows]); b = np.array([x["b"] for x in rows])
    rep = {"years": years, "windows": len(rows), "first_start": rows[0]["start"], "last_start": rows[-1]["start"],
           "a_below_initial": int((a < INITIAL).sum()), "b_below_initial": int((b < INITIAL).sum()), "b_gt_a": int((b > a).sum()),
           "a_min": round(float(a.min()), 2), "a_min_start": rows[int(a.argmin())]["start"], "a_max": round(float(a.max()), 2),
           "a_max_start": rows[int(a.argmax())]["start"], "b_min": round(float(b.min()), 2), "b_min_start": rows[int(b.argmin())]["start"],
           "b_max": round(float(b.max()), 2), "a_median": round(float(np.median(a)), 2), "b_median": round(float(np.median(b)), 2),
           "rows": rows}
    log("ROLL", **{k: v for k, v in rep.items() if k != "rows"})
    return rep


def facts(r, qqq_close):
    """대본·장면이 말하는 날짜별 사실 (모두 계좌 값에서 — 그날까지의 값만)."""
    d, a, b, out = r["dates"], r["a_val"], r["b_val"], r["out_cum"]
    ev = r["events"]
    S = lambda i: str(d[i].date())
    first = lambda c: (lambda k: {"date": S(int(k[0])), "a": round(float(a[k[0]]), 2), "b": round(float(b[k[0]]), 2), "out": round(float(out[k[0]]), 2)}
                       if len(k) else None)(np.flatnonzero(c))
    F = {"first_out": {"date": S(ev[0][0]), "amount": round(float(ev[0][1]), 2)},
         "out_ge": {str(t): first(out >= t) for t in (25_000, 50_000, 75_000, 100_000)},
         "b_ge": {str(t): first(b >= t) for t in (150_000, 200_000, 300_000, 400_000, 500_000)},
         "a_lt": {str(t): first(a < t) for t in (95_000, 90_000, 80_000, 70_000, 65_000)},
         "a_max": {"date": S(int(a.argmax())), "a": round(float(a.max()), 2), "vs_initial": round(float(a.max() / INITIAL - 1), 4)},
         "events": {S(i): round(float(c), 2) for i, c in ev}}
    yl = {}
    for y in sorted(set(d.year)):
        m = np.flatnonzero(d.year == y)
        ia, ib = m[int(a[m].argmin())], m[int(b[m].argmin())]
        ja, jb = m[int(a[m].argmax())], m[int(b[m].argmax())]
        yl[int(y)] = {"a_low": round(float(a[ia]), 2), "a_low_date": S(ia), "b_low": round(float(b[ib]), 2), "b_low_date": S(ib),
                      "a_high": round(float(a[ja]), 2), "a_high_date": S(ja), "b_high": round(float(b[jb]), 2), "b_high_date": S(jb),
                      "b_on_a_low": round(float(b[ia]), 2), "a_on_b_high": round(float(a[jb]), 2), "b_on_a_high": round(float(b[ja]), 2)}
    F["year"] = yl
    # 2018 4분기: 2018 QYLD 계좌 최고 날 → 그해 최저 날 (두 계좌)
    y18 = yl[2018]
    i_hi, i_lo = d.get_loc(pd.Timestamp(y18["a_high_date"])), d.get_loc(pd.Timestamp(y18["a_low_date"]))
    F["q4_2018"] = {"from": S(i_hi), "to": S(i_lo), "a_from": round(float(a[i_hi]), 2), "a_to": round(float(a[i_lo]), 2),
                    "b_from": round(float(b[i_hi]), 2), "b_to": round(float(b[i_lo]), 2),
                    "a_chg": round(float(a[i_lo] / a[i_hi] - 1), 4), "b_chg": round(float(b[i_lo] / b[i_hi] - 1), 4)}
    # 2020 코로나: 2020 QQQ 계좌 최고(폭락 전) → 3월 최저
    m20 = np.flatnonzero((d >= pd.Timestamp("2020-01-01")) & (d <= pd.Timestamp("2020-03-31")))
    j_lo = m20[int(b[m20].argmin())]; j_hi = m20[int(b[m20[:list(m20).index(j_lo) + 1]].argmax())]
    F["covid"] = {"b_high_date": S(j_hi), "b_high": round(float(b[j_hi]), 2), "a_on_b_high": round(float(a[j_hi]), 2),
                  "low_date": S(j_lo), "b_low": round(float(b[j_lo]), 2), "a_on_low": round(float(a[j_lo]), 2),
                  "a_low_q1": round(float(a[m20].min()), 2), "a_low_q1_date": S(int(m20[int(a[m20].argmin())]))}
    # 2021-11-19 이 그때까지 QQQ 최고 종가였나 (미래 정보 없이 말할 수 있나)
    q = qqq_close.loc[:DOWN_REF]
    F["qqq_high_on_ref"] = bool(q.iloc[-1] >= q.max() - 1e-9)
    # 해마다 가장 많이·적게 나온 달 (그해 안에서만)
    em = {}
    for y in sorted(set(d.year)):
        e = [(S(i), c) for i, c in ev if d[i].year == y]
        if e:
            mx, mn = max(e, key=lambda x: x[1]), min(e, key=lambda x: x[1])
            em[int(y)] = {"max_date": mx[0], "max": round(mx[1], 2), "min_date": mn[0], "min": round(mn[1], 2), "n": len(e)}
    F["out_month"] = em
    log("FACTS", first_out=F["first_out"], a_max=F["a_max"], q4_2018=F["q4_2018"], covid=F["covid"], qqq_high_on_ref=F["qqq_high_on_ref"])
    return F


def total_return(df, start):
    d = df.loc[start:END]
    tr = ((d["close"] + d["div"]) / d["close"].shift(1)).fillna(1.0).cumprod()
    return tr


def main():
    setup_log()
    t0 = time.time()
    log("RUN", version=VERSION, income=ic.VERSION, initial=INITIAL, fee=FEE, end=END, note="연구·교육용 — 투자 권유 아님")
    D = {s: load(s) for s in sorted({x for p in PAIRS.values() for x in p})}
    # 0. 자료 성질 (결과 전): 분배율 해마다
    props = {s: yield_stats(D[s], D[s].index[0]) for s in ("QYLD", "XYLD", "JEPI", "QQQ", "SPY")}
    for s, v in props.items():
        log("PROPS", symbol=s, yearly_yield=",".join(f"{y}:{x:.1%}" for y, x in v.items()))
    # 2022 하락 기준일 확인: QQQ 종가가 2022 바닥 전 마지막 최고였던 날
    q = D["QQQ"]["close"].loc["2021-01-01":"2022-12-31"]
    ref_check = str(q.loc[:q.idxmin()].idxmax().date())
    log("PROPS", down_ref_expected=DOWN_REF, down_ref_from_data=ref_check, qqq_2022_low=str(q.idxmin().date()))
    if ref_check != DOWN_REF:
        raise RuntimeError(f"[PROPS] 2022 하락 기준일이 자료와 다름 ({ref_check}) → DOWN_REF 확인")
    res = {"version": VERSION, "engine": ic.VERSION, "initial": INITIAL, "fee": FEE, "end": END, "props": props, "pairs": {}}
    main_r, runs = None, {}
    for name, (a, b) in PAIRS.items():
        start = max(D[a].index[0], D[b].index[0])
        r = ic.withdraw_pair(D[a], D[b], start, END, INITIAL, FEE)
        runs[name] = r
        res["pairs"][name] = {"inc": a, "idx": b, **summary(r, f"{a} vs {b}")}
        if name == "main":
            main_r = r
            res["pairs"][name]["down2022"] = down(r, DOWN_REF)
            res["facts"] = facts(r, D[b]["close"])
            rt = ic.withdraw_pair(D[a], D[b], start, END, INITIAL, FEE, TAX_CHECK)
            res["pairs"][name]["tax15"] = summary(rt, f"{a} vs {b} 원천징수 15%")
            # 분배금을 다시 넣으면 (총수익): 꺼내 쓰지 않은 두 계좌
            ta, tb = total_return(D[a], start), total_return(D[b], start)
            res["pairs"][name]["reinvest"] = {"a_end": round(float(INITIAL * (1 - FEE) * ta.iloc[-1] / ta.iloc[0]), 2),
                                              "b_end": round(float(INITIAL * (1 - FEE) * tb.iloc[-1] / tb.iloc[0]), 2),
                                              "a_price_only_end": round(float(INITIAL * (1 - FEE) * D[a]["close"].iloc[-1] / D[a]["close"].loc[start]), 2)}
            rv = res["pairs"][name]["reinvest"]
            rv["b_over_a"] = round(rv["b_end"] / rv["a_end"], 4)
            log("REINVEST", **rv)
            # 하루 수익률 성질: 오른 날·내린 날 (커버드콜은 오를 때 덜 오르고 내릴 때 거의 같이 내린다 — 원칙 확인)
            ra, rb = D[a]["close"].loc[start:].pct_change(), D[b]["close"].loc[start:].pct_change()
            j = ra.index.intersection(rb.index)[1:]
            up, dn = rb.loc[j] > 0.01, rb.loc[j] < -0.01
            cap = {"qqq_up_days_over_1pct": int(up.sum()), "a_on_up_mean": round(float(ra.loc[j][up].mean()), 5),
                   "b_on_up_mean": round(float(rb.loc[j][up].mean()), 5), "qqq_down_days_over_1pct": int(dn.sum()),
                   "a_on_down_mean": round(float(ra.loc[j][dn].mean()), 5), "b_on_down_mean": round(float(rb.loc[j][dn].mean()), 5)}
            cap["up_capture"] = round(float(ra.loc[j][up].mean() / rb.loc[j][up].mean()), 4)       # 반올림 전 값으로 나눔
            cap["down_capture"] = round(float(ra.loc[j][dn].mean() / rb.loc[j][dn].mean()), 4)
            res["pairs"][name]["capture"] = cap
            log("CAPTURE", **res["pairs"][name]["capture"])
    res["rolling"] = {f"{y}y": rolling(D["QYLD"], D["QQQ"], y) for y in ROLL_YEARS}
    res["rolling_xyld_5y"] = rolling(D["XYLD"], D["SPY"], 5)
    (HERE / "results.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), "utf-8")
    write_md(res)
    write_anim(main_r, res, runs)
    log("RUN", done=True, sec=round(time.time() - t0, 1))


def money(x):
    return f"${x:,.0f}"


def write_md(res):
    m = res["pairs"]["main"]
    L = [f"# 커버드콜 원금 백테스트 결과 ({res['version']}, 엔진 income {res['engine']}) — 자동 생성, 손으로 고치지 않음", "",
         "※ 연구·교육용 — 투자 권유 아님. 세전 (원천징수 15% 는 확인). 과거 결과는 미래를 보장하지 않는다.", "",
         "## 본 실험 · 확인 짝", "", "| 짝 | 기간 | 꺼낸 횟수 | 꺼낸 돈 합 | 분배 ETF 계좌 끝 | 지수 ETF 계좌 끝 | 지수 ÷ 분배 |", "|---|---|---:|---:|---:|---:|---:|"]
    for k, p in res["pairs"].items():
        L.append(f"| {p['label']} | {p['start']}~{p['end']} ({p['years']}년) | {p['withdrawals']} | {money(p['out_total'])} | {money(p['a_end'])} | {money(p['b_end'])} | ×{p['b_over_a']:.2f} |")
    t = m["tax15"]
    L += ["", f"- 원천징수 15%: 꺼낸 돈 {money(t['out_total'])} · QYLD {money(t['a_end'])} · QQQ {money(t['b_end'])}",
          f"- 분배금을 다시 넣으면 (꺼내지 않음): QYLD {money(m['reinvest']['a_end'])} · QQQ {money(m['reinvest']['b_end'])} · QYLD 가격만 {money(m['reinvest']['a_price_only_end'])}",
          f"- QYLD 1주 값: {m['a_price_start']} → {m['a_price_end']}", "", "## 2022 하락 (기준일 " + DOWN_REF + ")", ""]
    for k, v in m["down2022"].items():
        if isinstance(v, dict):
            L.append(f"- {k}: {money(v['ref'])} → 최저 {money(v['low'])} ({v['low_date']}, {v['drop']:+.1%}) → 회복 {v['recovered']} ({v['recover_days']}일) · 끝 {v['end_vs_ref']:+.1%}")
    L += ["", "## 시작 달을 바꾼 계좌", "", "| 기간 | 계좌 수 | 시작 | QYLD 원금 아래 | QQQ 원금 아래 | QQQ > QYLD | QYLD 중앙 | QQQ 중앙 | QYLD 최저 (시작) |", "|---|---:|---|---:|---:|---:|---:|---:|---|"]
    for k, v in list(res["rolling"].items()) + [("XYLD 5y", res["rolling_xyld_5y"])]:
        L.append(f"| {k} | {v['windows']} | {v['first_start']}~{v['last_start']} | {v['a_below_initial']} | {v['b_below_initial']} | {v['b_gt_a']} | {money(v['a_median'])} | {money(v['b_median'])} | {money(v['a_min'])} ({v['a_min_start']}) |")
    L += ["", "## 해마다 (본 실험)", "", "| 해 | 꺼낸 돈 | QYLD 해 끝 | QQQ 해 끝 |", "|---|---:|---:|---:|"]
    for y, v in m["by_year"].items():
        L.append(f"| {y} | {money(v['out'])} | {money(v['a'])} | {money(v['b'])} |")
    (HERE / "results.md").write_text("\n".join(L) + "\n", "utf-8")


def rint(x):
    """반올림 (0.5 는 올림 — 대본 글자·검사와 같음. Python round() 는 짝수 쪽이라 쓰지 않음)."""
    return int(np.floor(float(x) + 0.5))


def write_anim(r, res, runs):
    """장면용: 날마다 두 계좌 값·꺼낸 돈 누적·QYLD 1주 값 (숫자는 이 파일만 씀)."""
    d = r["dates"]
    obj = {"version": VERSION, "dates": [x.strftime("%Y-%m-%d") for x in d], "a": [rint(x) for x in r["a_val"]],
           "b": [rint(x) for x in r["b_val"]], "out": [rint(x) for x in r["out_cum"]],
           "pa": [round(float(x), 3) for x in r["a_close"]], "pb": [round(float(x), 3) for x in r["b_close"]],
           "ev": [[int(i), round(float(c), 2)] for i, c in r["events"]],
           "summary": {k: v for k, v in res["pairs"]["main"].items() if k not in ("by_year",)},
           "by_year": res["pairs"]["main"]["by_year"],
           "checks": {k: {x: v[x] for x in ("label", "start", "end", "years", "out_total", "a_end", "b_end", "b_over_a")} for k, v in res["pairs"].items()},
           "rolling": {k: {x: v[x] for x in v if x != "rows"} | {"pts": [[w["start"], w["a"], w["b"]] for w in v["rows"]]} for k, v in res["rolling"].items()},
           "rolling_xyld_5y": {x: res["rolling_xyld_5y"][x] for x in res["rolling_xyld_5y"] if x != "rows"},
           "pairs_daily": {k: (lambda q, ix: {"dates": [q["dates"][i].strftime("%Y-%m-%d") for i in ix], "a": [rint(q["a_val"][i]) for i in ix],
                                             "b": [rint(q["b_val"][i]) for i in ix], "out": [rint(q["out_cum"][i]) for i in ix]})(
                               runs[k], sorted(set(range(0, len(runs[k]["dates"]), 3)) | {len(runs[k]["dates"]) - 1})) for k in ("xyld", "jepi")},
           "props": res["props"], "facts": {k: v for k, v in res["facts"].items() if k != "events"},
           "capture": res["pairs"]["main"]["capture"], "down2022": res["pairs"]["main"]["down2022"],
           "tax15": {x: res["pairs"]["main"]["tax15"][x] for x in ("out_total", "a_end", "b_end", "b_over_a")}, "reinvest": res["pairs"]["main"]["reinvest"]}
    (HERE / "anim.js").write_text("// 자동 생성 (run.py " + VERSION + ") — 손으로 고치지 않음\nwindow.CC = " + json.dumps(obj, ensure_ascii=False, separators=(",", ":")) + ";\n", "utf-8")
    log("ANIM", days=len(d), bytes=(HERE / "anim.js").stat().st_size)


if __name__ == "__main__":
    main()
