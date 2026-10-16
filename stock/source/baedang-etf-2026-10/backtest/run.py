# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-16 — 최초. 주식 3번 배당 ETF vs 지수 ETF, 배당세 떼고 (사용자 지시 2026-10-16 "이제 니즈에 따라 어떻게 테스트 계획 세우고
#          하는지 알겠지? 같은 방식으로 필요한 소스 생성해서 3개 영상 미리보기 영상 만들어봐"). 계획(결과를 보기 전에 정함 — ../README.md 1번):
#          본 실험 = 매달 첫 거래일 $1,000 씩 적립 · SCHD 계좌 vs SPY 계좌 · 배당은 받을 때 15% 원천징수 뒤 그날 종가에 다시 매수 ·
#          SCHD 첫 달 다음 달(2011-11-01) ~ 2026-10-15 · 수수료 0.25% (살 때마다 — 배당 다시 매수 포함).
#          확인 = 한 번에 $100,000 · 원천징수 0%·30% · 끝에 모두 매도하고 차익에 15% · VYM vs SPY (2006~, 2008 포함) · 시작 달을 바꾼 5년·10년 적립 계좌 전부.
"""배당 ETF vs 지수 ETF 백테스트 (연구·교육용 — 투자 권유가 아니다. 과거 결과는 미래를 보장하지 않는다).
실행: python3 stock/source/baedang-etf-2026-10/backtest/run.py   → results.json · results.md · run.log · anim.js
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
END, UNTIL = "2026-10-15", "2026-10-16"
MONTHLY, LUMP, FEE = 1_000.0, 100_000.0, 0.0025
TAX, TAX_CHECK, CG_CHECK = 0.15, [0.0, 0.30], 0.15     # 원천징수 15% (많은 나라의 미국 배당 조약 세율 — 나라마다 다름) · 확인 0%·30% · 끝 매도 차익세 15%
START = "2011-11-01"                                   # SCHD 상장(2011-10-20) 다음 달 첫 거래일 — 달 첫 거래일 적립을 처음부터 같게
VYM_START = "2006-12-01"                               # VYM 상장(2006-11-16) 다음 달 첫 거래일
ROLL_YEARS = [5, 10]


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


def load(sym):
    df, meta = bd.yahoo_daily(sym, until=UNTIL)
    df = df.loc[:END]
    log("DATA", symbol=sym, rows=len(df), first=str(df.index[0].date()), last=str(df.index[-1].date()), dividends=int((df["div"] > 0).sum()),
        sha256=meta.get("sha256", "?")[:12])
    return df


def yields(df, start):
    """자료 성질 (결과 전): 해마다 배당 ÷ 그해 첫 종가 · 배당 횟수."""
    d = df.loc[start:]
    out = {}
    for y, g in d.groupby(d.index.year):
        if len(g) < 200:
            continue
        out[int(y)] = {"yield": round(float(g["div"].sum() / g["close"].iloc[0]), 6), "n": int((g["div"] > 0).sum())}
    return out


def pair(A, B, start, initial, monthly, tax, quiet=False):
    """같은 날만 쓰는 두 계좌 (A 배당 ETF, B 지수 ETF)."""
    a, b = ic.common(A, B, start, END)
    ra = ic.reinvest(A, start, END, initial, tax, FEE, monthly, dates=a.index, quiet=quiet)
    rb = ic.reinvest(B, start, END, initial, tax, FEE, monthly, dates=b.index, quiet=quiet)
    assert (ra["dates"] == rb["dates"]).all()
    return ra, rb


def summ(ra, rb, label):
    d = ra["dates"]
    s = {"label": label, "start": str(d[0].date()), "end": str(d[-1].date()), "years": round((d[-1] - d[0]).days / 365.25, 2),
         "paid": rint(ra["paid"][-1]), "a_end": round(float(ra["val"][-1]), 2), "b_end": round(float(rb["val"][-1]), 2),
         "b_over_a": round(float(rb["val"][-1] / ra["val"][-1]), 4), "gap": round(float(rb["val"][-1] - ra["val"][-1]), 2),
         "a_div": round(float(ra["div_gross"][-1]), 2), "b_div": round(float(rb["div_gross"][-1]), 2),
         "a_tax": round(float(ra["tax_paid"][-1]), 2), "b_tax": round(float(rb["tax_paid"][-1]), 2),
         "a_basis": round(float(ra["basis"][-1]), 2), "b_basis": round(float(rb["basis"][-1]), 2),
         "a_gain": round(float(ra["val"][-1] / ra["paid"][-1] - 1), 4), "b_gain": round(float(rb["val"][-1] / rb["paid"][-1] - 1), 4),
         "a_lead_days_share": round(float((ra["val"] > rb["val"]).mean()), 4)}
    log("RESULT", **s)
    return s


def facts(ra, rb, A, B):
    """대본·장면이 말하는 날짜별 사실 (그날까지 값만)."""
    d, a, b, paid = ra["dates"], ra["val"], rb["val"], ra["paid"]
    S = lambda i: str(d[i].date())
    F = {}
    yl = {}
    for y in sorted(set(d.year)):
        m = np.flatnonzero(d.year == y); k = m[-1]
        yl[int(y)] = {"date": S(k), "a": round(float(a[k]), 2), "b": round(float(b[k]), 2), "paid": rint(paid[k]),
                      "a_div_y": round(float(ra["div_gross"][k] - (ra["div_gross"][m[0] - 1] if m[0] > 0 else 0)), 2),
                      "b_div_y": round(float(rb["div_gross"][k] - (rb["div_gross"][m[0] - 1] if m[0] > 0 else 0)), 2),
                      "a_tax_c": round(float(ra["tax_paid"][k]), 2), "b_tax_c": round(float(rb["tax_paid"][k]), 2),
                      "a_div_c": round(float(ra["div_gross"][k]), 2), "b_div_c": round(float(rb["div_gross"][k]), 2),
                      "lead": "a" if a[k] > b[k] else "b"}
    F["year"] = yl
    # 앞선 계좌가 바뀐 날 (그날까지 값)
    lead = a > b
    ch = np.flatnonzero(lead[2:] != lead[1:-1]) + 2                  # 첫날(두 계좌 같은 값 — 반올림 차이)은 빼고 둘째 날부터
    F["lead_changes"] = len(ch)
    F["lead_change_dates"] = [{"date": S(i), "lead": "a" if lead[i] else "b", "a": round(float(a[i]), 2), "b": round(float(b[i]), 2)} for i in ch]
    last = ch[-1] if len(ch) else 0
    F["last_lead_change"] = {"date": S(last), "lead": "a" if lead[last] else "b"}
    # 가장 크게 벌어진 날 (그날까지 — 끝까지 기준 최대 · 앞에서부터 셀 때 쓰지 않음)
    gap = b - a
    F["max_gap_b"] = {"date": S(int(gap.argmax())), "gap": round(float(gap.max()), 2)}
    F["max_gap_a"] = {"date": S(int(gap.argmin())), "gap": round(float(-gap.min()), 2)}
    # 하락 구간: 2020 코로나 (2월 최고 → 3월 최저), 2022 (해 최저)
    def drop(y0, y1):
        m = np.flatnonzero((d >= pd.Timestamp(y0)) & (d <= pd.Timestamp(y1)))
        out = {}
        for key, v in (("a", a), ("b", b)):
            lo = m[int(v[m].argmin())]; hi = m[int(v[m[:list(m).index(lo) + 1]].argmax())]
            out[key] = {"high_date": S(hi), "high": round(float(v[hi]), 2), "low_date": S(lo), "low": round(float(v[lo]), 2), "drop": round(float(v[lo] / v[hi] - 1), 4)}
        return out
    F["covid"] = drop("2020-01-01", "2020-04-30")
    F["y2022"] = drop("2022-01-01", "2022-12-31")
    # 배당 받은 첫날·금액 (1회)
    ia = np.flatnonzero(np.diff(ra["div_gross"]) > 0); ib = np.flatnonzero(np.diff(rb["div_gross"]) > 0)
    F["a_first_div"] = {"date": S(int(ia[0]) + 1), "gross": round(float(ra["div_gross"][ia[0] + 1]), 2)}
    F["b_first_div"] = {"date": S(int(ib[0]) + 1), "gross": round(float(rb["div_gross"][ib[0] + 1]), 2)}
    F["a_div_events"], F["b_div_events"] = int(len(ia)), int(len(ib))
    # 마지막 12개월 배당 (세전) · 끝 값 대비 배당률
    k12 = int(np.flatnonzero(d > d[-1] - pd.Timedelta(days=365))[0])
    F["last12"] = {"a_div": round(float(ra["div_gross"][-1] - ra["div_gross"][k12 - 1]), 2), "b_div": round(float(rb["div_gross"][-1] - rb["div_gross"][k12 - 1]), 2)}
    # 넣은 돈 문턱
    F["paid_ge"] = {str(t): S(int(np.flatnonzero(paid >= t)[0])) for t in (50_000, 100_000, 150_000) if (paid >= t).any()}
    log("FACTS", lead_changes=F["lead_changes"], last_lead_change=F["last_lead_change"], max_gap_b=F["max_gap_b"], max_gap_a=F["max_gap_a"],
        covid=F["covid"], y2022=F["y2022"], last12=F["last12"])
    return F


def rolling(A, B, years, tax=TAX):
    a, b = ic.common(A, B, A.index[0], END)
    starts = ic.month_starts(a.index)
    rows = []
    for s in starts:
        if s == 0:
            continue
        sd = a.index[s]; ed = sd + pd.DateOffset(years=years)
        if ed > a.index[-1]:
            break
        ra, rb = pair_window(A, B, sd, ed, tax)
        rows.append({"start": str(sd.date()), "a": round(float(ra["val"][-1]), 2), "b": round(float(rb["val"][-1]), 2), "paid": rint(ra["paid"][-1])})
    av = np.array([x["a"] for x in rows]); bv = np.array([x["b"] for x in rows])
    rep = {"years": years, "windows": len(rows), "first_start": rows[0]["start"], "last_start": rows[-1]["start"], "a_gt_b": int((av > bv).sum()),
           "b_gt_a": int((bv > av).sum()), "ratio_median": round(float(np.median(bv / av)), 4), "a_best_start": rows[int(np.argmax(av / bv))]["start"],
           "a_best_ratio": round(float((av / bv).max()), 4), "b_best_start": rows[int(np.argmax(bv / av))]["start"], "b_best_ratio": round(float((bv / av).max()), 4),
           "rows": rows}
    log("ROLL", **{k: v for k, v in rep.items() if k != "rows"})
    return rep


def pair_window(A, B, sd, ed, tax):
    a, b = ic.common(A, B, sd, ed)
    ra = ic.reinvest(A, sd, ed, MONTHLY, tax, FEE, MONTHLY, dates=a.index, quiet=True)
    rb = ic.reinvest(B, sd, ed, MONTHLY, tax, FEE, MONTHLY, dates=b.index, quiet=True)
    return ra, rb


def main():
    setup_log()
    t0 = time.time()
    log("RUN", version=VERSION, income=ic.VERSION, monthly=MONTHLY, lump=LUMP, fee=FEE, tax=TAX, end=END, note="연구·교육용 — 투자 권유 아님")
    D = {s: load(s) for s in ("SCHD", "SPY", "VYM")}
    props = {s: yields(D[s], "2012-01-01" if s != "VYM" else "2007-01-01") for s in D}
    for s, v in props.items():
        log("PROPS", symbol=s, yearly_yield=",".join(f"{y}:{x['yield']:.1%}/{x['n']}" for y, x in v.items()))
    res = {"version": VERSION, "engine": ic.VERSION, "monthly": MONTHLY, "lump": LUMP, "fee": FEE, "tax": TAX, "end": END, "props": props,
           "first_day": {s: str(D[s].index[0].date()) for s in D}}
    # 본 실험: 매달 $1,000 (첫 달 START 첫 거래일 = 첫 $1,000)
    ra, rb = pair(D["SCHD"], D["SPY"], START, MONTHLY, MONTHLY, TAX)
    res["main"] = summ(ra, rb, "SCHD vs SPY 매달 $1,000 · 원천징수 15%")
    res["main"]["div_ratio"] = round(res["main"]["a_div"] / res["main"]["b_div"], 4)
    res["main"]["tax_ratio"] = round(res["main"]["a_tax"] / res["main"]["b_tax"], 4)
    res["facts"] = facts(ra, rb, D["SCHD"], D["SPY"])
    # 해마다 총수익 (배당 재투자, 세금·비용 없음 — 상품 자체 비교) · 2012~2025 (다 찬 해)
    res["annual_tr"] = {}
    for y in range(2012, 2026):
        row = {}
        for k in ("SCHD", "SPY"):
            df = D[k]
            tr = ((df["close"] + df["div"]) / df["close"].shift(1)).fillna(1.0).cumprod()
            a0 = tr.loc[:f"{y - 1}-12-31"].iloc[-1]; a1 = tr.loc[:f"{y}-12-31"].iloc[-1]
            row[k] = round(float(a1 / a0 - 1), 4)
        res["annual_tr"][str(y)] = row
    w = sum(1 for v in res["annual_tr"].values() if v["SCHD"] > v["SPY"])
    res["annual_tr_summary"] = {"years": len(res["annual_tr"]), "schd_wins": w, "spy_wins": len(res["annual_tr"]) - w}
    log("ANNUAL", **res["annual_tr_summary"], detail=",".join(f"{y}:{v['SCHD']:+.1%}/{v['SPY']:+.1%}" for y, v in res["annual_tr"].items()))
    # 배당 한 번의 예 (본 실험 SCHD 계좌, 2025년 마지막 배당): 주식 수 × 1주 배당 → 세금 15% → 남은 돈으로 그날 종가에 매수 (수수료 0.25%)
    A = D["SCHD"].loc[ra["dates"]]
    evs = [i for i in np.flatnonzero(A["div"].to_numpy() > 0) if ra["dates"][i].year == 2025]
    i = int(evs[-1])
    assert i not in set(ic.month_starts(ra["dates"]).tolist()), "예 배당 날이 적립 날과 겹침 — 다른 날로"
    dps, px = float(A["div"].iloc[i]), float(A["close"].iloc[i])
    sh0 = float(ra["shares"][i - 1])
    gross = sh0 * dps; tax = gross * TAX; net = gross - tax; new = net * (1 - FEE) / px
    res["div_example"] = {"date": str(ra["dates"][i].date()), "shares": round(sh0, 2), "dps": round(dps, 4), "gross": round(gross, 2), "tax": round(tax, 2),
                          "net": round(net, 2), "price": round(px, 2), "new_shares": round(new, 2), "check_shares_after": round(float(ra["shares"][i]), 2)}
    log("EXAMPLE", **res["div_example"])
    # 끝에 모두 매도 · 차익 15%
    la, lb = ic.liquidate(ra["val"][-1], ra["basis"][-1], CG_CHECK, FEE), ic.liquidate(rb["val"][-1], rb["basis"][-1], CG_CHECK, FEE)
    res["sell_all"] = {"cg_tax": CG_CHECK, "a": round(float(la), 2), "b": round(float(lb), 2), "b_over_a": round(float(lb / la), 4)}
    log("SELLALL", **res["sell_all"])
    # 원천징수 0%·30%
    res["tax_checks"] = {}
    for tx in TAX_CHECK:
        xa, xb = pair(D["SCHD"], D["SPY"], START, MONTHLY, MONTHLY, tx)
        res["tax_checks"][f"{tx:.2f}"] = summ(xa, xb, f"SCHD vs SPY 원천징수 {tx:.0%}")
    # 한 번에 $100,000 (같은 시작일)
    la_, lb_ = pair(D["SCHD"], D["SPY"], START, LUMP, 0.0, TAX)
    res["lump"] = summ(la_, lb_, "SCHD vs SPY 한 번에 $100,000")
    # VYM vs SPY (2006~)
    va, vb = pair(D["VYM"], D["SPY"], VYM_START, MONTHLY, MONTHLY, TAX)
    res["vym"] = summ(va, vb, "VYM vs SPY 매달 $1,000")
    res["vym_facts"] = {}
    dv = va["dates"]
    mlo = np.flatnonzero((dv >= pd.Timestamp("2008-06-01")) & (dv <= pd.Timestamp("2009-06-30")))
    for key, rr in (("a", va), ("b", vb)):                          # 2008 금융위기: 2008-06~2009-06 최저 날 → 2007-07 부터 그날까지 최고 날 (적립 계좌 값)
        lo = mlo[int(rr["val"][mlo].argmin())]
        mh = np.flatnonzero((dv >= pd.Timestamp("2007-07-01")) & (np.arange(len(dv)) <= lo)); hi = mh[int(rr["val"][mh].argmax())]
        res["vym_facts"][f"crisis_{key}"] = {"high_date": str(rr["dates"][hi].date()), "high": round(float(rr["val"][hi]), 2), "low_date": str(rr["dates"][lo].date()),
                                             "low": round(float(rr["val"][lo]), 2), "drop": round(float(rr["val"][lo] / rr["val"][hi] - 1), 4), "paid_low": rint(rr["paid"][lo])}
    k = int(np.flatnonzero(va["dates"] <= pd.Timestamp("2011-10-31"))[-1])
    res["vym_facts"]["at_schd_start"] = {"date": str(va["dates"][k].date()), "a": round(float(va["val"][k]), 2), "b": round(float(vb["val"][k]), 2), "paid": rint(va["paid"][k])}
    log("VYM", **res["vym_facts"])
    # 시작 달을 바꾼 적립 계좌
    res["rolling"] = {f"{y}y": rolling(D["SCHD"], D["SPY"], y) for y in ROLL_YEARS}
    res["rolling_vym_10y"] = rolling(D["VYM"], D["SPY"], 10)
    (HERE / "results.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), "utf-8")
    write_md(res)
    write_anim(ra, rb, va, vb, res)
    log("RUN", done=True, sec=round(time.time() - t0, 1))


def money(x):
    return f"${x:,.0f}"


def write_md(res):
    m = res["main"]
    L = [f"# 배당 ETF vs 지수 ETF 결과 ({res['version']}, 엔진 income {res['engine']}) — 자동 생성, 손으로 고치지 않음", "",
         "※ 연구·교육용 — 투자 권유 아님. 과거 결과는 미래를 보장하지 않는다.", "",
         "| 실험 | 기간 | 넣은 돈 | 배당 ETF 끝 | 지수 ETF 끝 | 지수 ÷ 배당 | 받은 배당 (세전) 배당/지수 | 낸 배당세 배당/지수 |", "|---|---|---:|---:|---:|---:|---:|---:|"]
    rows = [res["main"], res["lump"], res["vym"]] + list(res["tax_checks"].values())
    for r in rows:
        L.append(f"| {r['label']} | {r['start']}~{r['end']} ({r['years']}년) | {money(r['paid'])} | {money(r['a_end'])} | {money(r['b_end'])} | ×{r['b_over_a']:.3f} | {money(r['a_div'])} / {money(r['b_div'])} | {money(r['a_tax'])} / {money(r['b_tax'])} |")
    s = res["sell_all"]
    L += ["", f"- 끝에 모두 매도·차익 {s['cg_tax']:.0%}: SCHD {money(s['a'])} · SPY {money(s['b'])} (×{s['b_over_a']:.3f})", "",
          "## 시작 달을 바꾼 적립 계좌", "", "| 기간 | 계좌 수 | 시작 | 배당 ETF 가 많음 | 지수가 많음 | 지수÷배당 (가운데) |", "|---|---:|---|---:|---:|---:|"]
    for k, v in list(res["rolling"].items()) + [("VYM 10y", res["rolling_vym_10y"])]:
        L.append(f"| {k} | {v['windows']} | {v['first_start']}~{v['last_start']} | {v['a_gt_b']} | {v['b_gt_a']} | ×{v['ratio_median']:.3f} |")
    L += ["", "## 해마다 (본 실험)", "", "| 해 | 넣은 돈 | SCHD | SPY | 그해 배당 SCHD/SPY |", "|---|---:|---:|---:|---:|"]
    for y, v in res["facts"]["year"].items():
        L.append(f"| {y} | {money(v['paid'])} | {money(v['a'])} | {money(v['b'])} | {money(v['a_div_y'])} / {money(v['b_div_y'])} |")
    (HERE / "results.md").write_text("\n".join(L) + "\n", "utf-8")


def write_anim(ra, rb, va, vb, res):
    d = ra["dates"]
    obj = {"version": VERSION, "dates": [x.strftime("%Y-%m-%d") for x in d], "a": [rint(x) for x in ra["val"]], "b": [rint(x) for x in rb["val"]],
           "paid": [rint(x) for x in ra["paid"]], "adiv": [rint(x) for x in ra["div_gross"]], "bdiv": [rint(x) for x in rb["div_gross"]],
           "atax": [rint(x) for x in ra["tax_paid"]], "btax": [rint(x) for x in rb["tax_paid"]],
           "aev": [int(i) for i in np.flatnonzero(np.diff(ra["div_gross"]) > 0) + 1], "bev": [int(i) for i in np.flatnonzero(np.diff(rb["div_gross"]) > 0) + 1],
           "main": res["main"], "facts": res["facts"], "sell_all": res["sell_all"], "tax_checks": res["tax_checks"], "lump": res["lump"], "vym": res["vym"],
           "vym_facts": res["vym_facts"], "props": res["props"], "annual_tr": res["annual_tr"], "annual_tr_summary": res["annual_tr_summary"], "div_example": res["div_example"],
           "rolling": {k: {x: v[x] for x in v if x != "rows"} | {"pts": [[w["start"], w["a"], w["b"]] for w in v["rows"]]} for k, v in res["rolling"].items()},
           "rolling_vym_10y": {x: res["rolling_vym_10y"][x] for x in res["rolling_vym_10y"] if x != "rows"},
           "vym_daily": (lambda ix: {"dates": [va["dates"][i].strftime("%Y-%m-%d") for i in ix], "a": [rint(va["val"][i]) for i in ix], "b": [rint(vb["val"][i]) for i in ix],
                                     "paid": [rint(va["paid"][i]) for i in ix]})(sorted(set(range(0, len(va["dates"]), 3)) | {len(va["dates"]) - 1}))}
    (HERE / "anim.js").write_text("// 자동 생성 (run.py " + VERSION + ") — 손으로 고치지 않음\nwindow.DV = " + json.dumps(obj, ensure_ascii=False, separators=(",", ":")) + ";\n", "utf-8")
    log("ANIM", days=len(d), bytes=(HERE / "anim.js").stat().st_size)


if __name__ == "__main__":
    main()
