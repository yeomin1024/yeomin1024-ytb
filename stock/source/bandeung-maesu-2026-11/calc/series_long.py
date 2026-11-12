#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-11-12 — 반등 편 롱폼 영상(장면 v1.0)의 그래프 자료 — 사용자 지시 "오디오 만들었으니 반등 영상 만들어봐"
#   읽기만: history_result.json v1.4 · longform_result.json v1.3 (같은 폴더, 대본 v7.2 의 숫자 출처) · 가격 CSV (SPY · ^GSPC · ^KS11)
#   쓰기: video/episodes/bandeung-maesu-2026-11/data.js (window.D) — 화면 숫자는 모두 이 파일 또는 대본 그대로.
#   검사: 대본에 나오는 숫자를 자료에서 다시 계산해 같은지 본다 (다르면 멈춤).
# 연구·교육용 — 투자 권유 아님.
from __future__ import annotations

import json
import logging
import sys
import time
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
OUT = ROOT / "video/episodes/bandeung-maesu-2026-11/data.js"
DATA = ROOT / "stock/topics/precheck/data"

logging.basicConfig(level=logging.INFO, format="%(message)s")
LOG = logging.getLogger("series_long")


def log(stage: str, **kv) -> None:
    LOG.info("[%s] [%s] %s", stage, time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), " ".join(f"{k}={v}" for k, v in kv.items()))


def load(name: str, col: str = "close") -> pd.Series:
    p = DATA / name
    try:
        s = pd.read_csv(p, comment="#", parse_dates=["date"]).set_index("date")[col].astype(float).dropna()
    except Exception as e:  # 자료가 없으면 멈춤 — 다음 할 일을 알림
        log("INPUT", level="error", file=str(p), err=repr(e)[:120], next="stock/topics/precheck/precheck.py 로 받거나 브랜치 ccr-38db670e-r10a62 에서 가져옴")
        raise SystemExit(2)
    if s.index.duplicated().any():
        log("INPUT", level="warn", file=name, dup=int(s.index.duplicated().sum()))
        s = s[~s.index.duplicated()]
    log("INPUT", file=name, col=col, rows=len(s), start=s.index[0].date(), end=s.index[-1].date())
    return s


def check(name: str, got: float, want: float, tol: float = 0.05) -> None:
    ok = abs(got - want) <= tol
    log("CHECK", what=name, got=round(got, 2), script=want, ok=ok)
    if not ok:
        raise SystemExit(f"숫자가 대본과 다름: {name} {got} ≠ {want}")


def pct(a: float, b: float) -> float:
    return (b / a - 1) * 100


def main() -> int:
    t0 = time.time()
    h = json.loads((HERE / "history_result.json").read_text("utf-8"))
    lf = json.loads((HERE / "longform_result.json").read_text("utf-8"))
    log("INPUT", history=h["version"], longform=lf["version"])
    spy = load("SPY.csv", "adjclose")
    spyc = load("SPY.csv", "close")
    gspc = load("_GSPC.csv", "close")
    ks = load("_KS11.csv", "close")

    # ① 2000~2026 흐름 (주 단위 SPY 수정 종가) + 급반등 83번 자리
    wk = spy["2000-01-01":"2026-10-28"].resample("W-FRI").last().dropna()
    base = wk.iloc[0]
    tl = [[d.strftime("%Y-%m-%d"), round(v / base * 100, 2)] for d, v in wk.items()]
    reb = []
    for e in h["rebound_days"]["events"]:
        d = pd.Timestamp(e["date"])
        i = int(wk.index.searchsorted(d))
        reb.append([min(i, len(wk) - 1), 1 if e["kind"] == "가짜" else 0])
    fake = sum(r[1] for r in reb)
    check("급반등 수", len(reb), 83, 0)
    check("가짜 수", fake, 56, 0)

    # ② 2008-10-13 하루 11.6% → 그날보다 32.6% 더 (^GSPC 일별)
    g = gspc["2008-08-01":"2009-04-30"]
    i13 = g.index.get_loc(pd.Timestamp("2008-10-13"))
    check("2008-10-13 하루 %", pct(g.iloc[i13 - 1], g.iloc[i13]), 11.6)
    low = g["2008-10-13":"2009-03-31"].min()
    check("그날보다 더 떨어짐 %", pct(g.iloc[i13], low), -32.6)
    d08 = [[d.strftime("%Y-%m-%d"), round(v, 2)] for d, v in g.items()]

    # ③ 2020 코로나: 바닥 전 급반등 5번 + 3월 24일 (SPY 종가 — 9.1%)
    c = spyc["2020-02-03":"2020-04-30"]
    ch = c.pct_change() * 100
    days = [d for d, v in ch["2020-02-19":"2020-03-24"].items() if v >= 3]
    before = [d for d in days if d < pd.Timestamp("2020-03-23")]
    check("바닥 전 급반등 수", len(before), 5, 0)
    check("3월 24일 %", float(ch[pd.Timestamp("2020-03-24")]), 9.1)
    d20 = [[d.strftime("%Y-%m-%d"), round(v, 2)] for d, v in c.items()]
    r20 = [d.strftime("%Y-%m-%d") for d in days]

    # ④ 닷컴 꼭대기에 매수: 본전(2000-03-24 수정 종가)을 넘었다 다시 아래 → 마지막으로 아래였던 날 2011-12-20 (11.7년)
    dc = spy["2000-01-01":"2013-06-30"].resample("W-FRI").last().dropna()
    pk = float(spy[pd.Timestamp("2000-03-24")])
    dot = [[d.strftime("%Y-%m-%d"), round(v / pk * 100, 2)] for d, v in dc.items()]
    rd = h["notes"]["dotcom_redip"]
    check("닷컴 꼭대기 → 마지막 본전 아래 년", (pd.Timestamp(rd["last_below"]) - pd.Timestamp("2000-03-24")).days / 365.25, 11.7)

    # ⑤ 코스피: 지금 최고가보다 42.5% 아래
    kn = h["kospi_bridge"]["now"]
    check("코스피 최고가 대비 %", kn["below_1y_high"], -42.5, 0)
    kw = ks["2025-06-01":"2026-11-10"].resample("W-FRI").last().dropna()
    kpk = float(kw.max())
    kospi = [[d.strftime("%Y-%m-%d"), round(v / kpk * 100, 2)] for d, v in kw.items()]

    # ⑥ 묶은 반등 20번 + 신호
    sig = lf["signal"]
    ev20 = [[e["rebound"], 1 if e["actual"] == "fake" else 0, 1 if e["hit"] else 0] for e in sig["events"]]
    check("묶은 반등 수", len(ev20), 20, 0)
    check("그중 가짜", sum(e[1] for e in ev20), 15, 0)
    check("신호 맞힘", sum(e[2] for e in ev20), 13, 0)

    # ⑦ 깊이 물린 급반등 32번 (먼저 내려감 down / 먼저 오름 up)
    sr = h["stuck_rebound"]
    st = [[r["date"], r["decline_peak"], r["side"], r["below_peak"]] for r in sr["rows"]]
    check("깊이 물린 급반등", len(st), 32, 0)
    check("먼저 오름", sum(1 for r in st if r[2] == "up"), 14, 0)

    ss = h["single_stocks"]
    big8 = [{"t": k, "name": ss[k]["name"], "years": ss[k]["years"]} for k in ["MSFT", "CSCO", "GE", "INTC", "XOM", "WMT", "IBM", "ORCL"]]
    check("10년 넘게 걸린 곳", sum(1 for b in big8 if b["years"] > 10), 6, 0)
    check("씨티그룹 지금 %", ss["C"]["now_vs_peak"], -67.0, 0)

    D = {
        "made": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "src": {"history": h["version"], "longform": lf["version"]},
        "tl": tl, "reb": reb, "d08": d08, "d20": d20, "r20": r20, "dot": dot,
        "dotRedip": {"recovered": rd["recovered"], "lastBelow": rd["last_below"]},
        "declines": [{k: r[k] for k in ("peak", "low", "depth", "years_peak_to_recover", "after_low_1m")} for r in h["declines"]["rows"]],
        "kospiRows": h["kospi_bridge"]["rows"], "kospi": kospi, "kospiNow": kn,
        "ev20": ev20, "stuck": st, "stuckBy": sr["by_decline"], "big8": big8, "citi": {"now": ss["C"]["now_vs_peak"], "peak": ss["C"]["peak"]},
        "fakeBuyers": h["fake_buyers"], "cash": lf["cash_plan"] if "cash_plan" in lf else h["from_longform"]["cash_plan"],
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("/* 반등 편 롱폼 그래프 자료 — stock/source/bandeung-maesu-2026-11/calc/series_long.py v1.0 가 만듦 (손으로 고치지 않음) · 연구·교육용 */\n"
                   f"window.D={json.dumps(D, ensure_ascii=False, separators=(',', ':'))};\n", "utf-8")
    log("DONE", file=str(OUT.relative_to(ROOT)), kb=round(OUT.stat().st_size / 1024, 1), tl=len(tl), d08=len(d08), d20=len(d20), dot=len(dot), sec=round(time.time() - t0, 2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
