#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-31 — 최초. 주식 2~4편 테스트(사용자 지시 2026-10-31 — 2편 「주식 폭락 예상하지 폭락 전 대비 테스트」 · 3편 「폭락 전 위험 감지 테스트」 ·
#          4편 「폭락 중 공포에 살 수 있을 까 테스트」)의 숫자. 모두 '덜 잃었나' 쪽 (채널 목적 — 리스크 최소 · 천천히 · 장기).
#   A. 2편 — 최고가를 찍은 날 뒤 1·2년 안에 그날보다 10%·20% 넘게 빠진 적이 있는 몫 (모든 날과 비교) · 큰 하락 4번 직전 1년 상승률 · 올해 최고가 횟수
#   B. 3편 — 신호 3가지(장단기 금리 역전 10년 − 13주 < 0 · S&P 500 이 200일 평균 아래 · 공포 지수 VIX 30 넘음)가 처음 켜진 날 뒤 1·2년 안 −20% 하락 몫(맞음·헛신호) ·
#      큰 하락 4번마다 신호가 처음 켜진 날과 그때까지 빠진 폭 · 끝까지 빠진 폭
#   C. 4편 — VIX 40 넘은 첫날 (공포가 가장 큰 때) 한꺼번에 매수 vs 12개월 나눠 매수 — 그 뒤 더 빠진 폭 · 2년 뒤 · 원금 80% 아래로 간 적
# 자료: stock/source/timing-test-2026-10/calc/gspc_daily.csv · sp500tr_daily.csv · irx_daily.csv / precheck/data/VIX.csv · TNX.csv (없으면 Yahoo chart v8 에서 받아 저장)
# 신호 '켜짐' = 그 전 60거래일 동안 꺼져 있다가 처음 켜진 날 (같은 사건을 여러 번 세지 않게).
# 실행: python3 -B stock/topics/precheck/crash_tests.py → precheck/crash_tests_<날짜>.json
# ※ 연구·교육용 — 투자 권유가 아님.
import bisect
import csv
import json
import logging
import time
import urllib.parse
import urllib.request
from datetime import date, datetime, timezone
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
CALC = HERE.parent.parent / "source" / "timing-test-2026-10" / "calc"
VERSION = "v1.0"
GAP = 60                     # 신호가 다시 켜졌다고 볼 꺼짐 거래일 수
BEARS = [("2000-03-24", "닷컴"), ("2007-10-09", "금융위기"), ("2020-02-19", "코로나"), ("2022-01-03", "2022 금리 인상")]
logging.basicConfig(level=logging.INFO, format="[%(stage)s] %(message)s")
log = logging.getLogger("crash_tests")


def read_calc(name):
    with (CALC / name).open(encoding="utf-8") as f:
        rows = [r for r in csv.reader(f) if r and not r[0].startswith("#")][1:]
    return {r[0]: float(r[1]) for r in rows if r[1]}


def yahoo(sym, fname):
    """Yahoo chart v8 일별 종가 → data/<fname>.csv (있으면 그대로 읽음)."""
    path = DATA / f"{fname}.csv"
    if not path.exists():
        url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(sym)}?period1=631152000&period2={int(time.time())}&interval=1d")
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=60) as r:
                res = json.load(r)["chart"]["result"][0]
        except Exception as e:  # noqa: BLE001
            log.error("sym=%s error=%s next=네트워크·프록시 확인 뒤 다시 실행 (README /root/.ccr)", sym, e, extra={"stage": "FETCH"})
            raise
        q = res["indicators"]["quote"][0]
        rows = [(datetime.fromtimestamp(t, tz=timezone.utc).date().isoformat(), c) for t, c in zip(res["timestamp"], q["close"]) if c is not None]
        with path.open("w", encoding="utf-8", newline="") as f:
            f.write(f"# {sym} 일별 종가 — Yahoo Finance chart API v8 (interval=1d), {date.today().isoformat()} 받음 · crash_tests.py {VERSION}\n")
            w = csv.writer(f)
            w.writerow(["date", "close"])
            w.writerows(rows)
        log.info("sym=%s rows=%d saved=%s", sym, len(rows), path.name, extra={"stage": "FETCH"})
    with path.open(encoding="utf-8") as f:
        rows = [r for r in csv.reader(f) if r and not r[0].startswith("#")][1:]
    return {r[0]: float(r[1]) for r in rows if r[1]}


def ffill(ds, s):
    keys = sorted(s)
    out = np.full(len(ds), np.nan)
    for i, d in enumerate(ds):
        j = bisect.bisect_right(keys, d) - 1
        if j >= 0:
            out[i] = s[keys[j]]
    return out


def first_on(on):
    """신호가 켜진 첫날들 — 그 전 GAP 거래일 동안 꺼져 있었던 날만."""
    out, last_on = [], -10 ** 9
    for i, x in enumerate(on):
        if x:
            if i - last_on > GAP:
                out.append(i)
            last_on = i
    return out


def fwd_dd(px, i, n):
    """i 날 종가 대비 그 뒤 n 거래일 안 가장 낮은 값의 변화 (−0.25 = 25% 더 빠짐)."""
    seg = px[i:min(len(px), i + n + 1)]
    return float(seg.min() / seg[0] - 1)


def main():
    gp = read_calc("gspc_daily.csv")
    tr_all = read_calc("sp500tr_daily.csv")
    ir_all = read_calc("irx_daily.csv")
    vix_all = yahoo("^VIX", "VIX")
    tnx_all = yahoo("^TNX", "TNX")
    ds = [d for d in sorted(gp) if d >= "1990-01-02"]
    px = np.array([gp[d] for d in ds])
    tr = ffill(ds, tr_all)
    irx, vix, tnx = ffill(ds, ir_all), ffill(ds, vix_all), ffill(ds, tnx_all)
    log.info("range=%s~%s rows=%d vix_first=%s tnx_first=%s", ds[0], ds[-1], len(ds), min(vix_all), min(tnx_all), extra={"stage": "LOAD"})
    Y1, Y2 = 252, 504
    last_full = len(ds) - 1 - Y2

    # ---------- A. 최고가 날
    allmax = np.maximum.accumulate(np.array([gp[d] for d in sorted(gp)]))
    run = dict(zip(sorted(gp), allmax))
    ath = [i for i in range(1, len(ds)) if px[i] >= run[ds[i]] and px[i] > run[ds[i - 1]]]
    A = {"ath_days_1990": len(ath), "by_year": {}}
    for i in ath:
        A["by_year"][ds[i][:4]] = A["by_year"].get(ds[i][:4], 0) + 1

    def share(idx, n, lvl):
        idx = [i for i in idx if i <= len(ds) - 1 - n]
        return round(100 * float(np.mean([fwd_dd(px, i, n) <= -lvl for i in idx])), 1), len(idx)

    A["after_ath"] = {f"{n_lab}·−{int(l * 100)}%": share(ath, n, l) for n_lab, n in (("1년", Y1), ("2년", Y2)) for l in (0.10, 0.20)}
    every = list(range(len(ds)))
    A["any_day"] = {f"{n_lab}·−{int(l * 100)}%": share(every, n, l) for n_lab, n in (("1년", Y1), ("2년", Y2)) for l in (0.10, 0.20)}
    A["before_bears"] = {}
    for d0, name in BEARS:
        i = bisect.bisect_left(ds, d0)
        j = i + int(np.argmin(px[i:i + 3 * Y1]))
        A["before_bears"][name] = {"peak": ds[i], "prior_1y": f"{(px[i] / px[i - Y1] - 1) * 100:+.1f}%", "ath_days_prior_1y": sum(1 for k in ath if i - Y1 < k <= i),
                                   "trough": ds[j], "fall": f"{(px[j] / px[i] - 1) * 100:.1f}%"}
    log.info("ath=%d after_ath=%s any_day=%s", len(ath), A["after_ath"], A["any_day"], extra={"stage": "A_ATH"})
    log.info("before_bears=%s ath_2026=%s", json.dumps(A["before_bears"], ensure_ascii=False), A["by_year"].get("2026"), extra={"stage": "A_ATH"})

    # ---------- B. 신호
    ma200 = np.array([np.nan] * 199 + [float(px[i - 199:i + 1].mean()) for i in range(199, len(px))])
    sig = {"장단기 금리 역전 (10년 − 13주 < 0)": (tnx - irx) < 0, "S&P 500 이 200일 평균 아래": px < ma200, "공포 지수 VIX 30 넘음": vix > 30}
    B = {}
    for name, on in sig.items():
        on = np.where(np.isnan(on.astype(float)), False, on)
        starts = first_on(on)
        rows = []
        for i in starts:
            full = i <= last_full
            rows.append({"date": ds[i], "dd_1y": f"{fwd_dd(px, i, Y1) * 100:.1f}%", "dd_2y": f"{fwd_dd(px, i, Y2) * 100:.1f}%" if full else None,
                         "from_peak": f"{(px[i] / run[ds[i]] - 1) * 100:.1f}%"})
        hit = [r for r in rows if r["dd_2y"] is not None]
        bear2 = sum(float(r["dd_2y"][:-1]) <= -20 for r in hit)
        per, prev_lo = {}, 0
        look = 2 * Y1 if name.startswith("장단기") else Y1      # 금리 역전은 1~2년 앞서 켜지는 신호라 2년, 나머지는 1년
        for d0, bname in BEARS:
            p = bisect.bisect_left(ds, d0)
            lo = p + int(np.argmin(px[p:p + 3 * Y1]))
            # 그 고점 look 전(앞 하락장 바닥 뒤)부터 바닥 사이에 처음 켜진 날 — 고점 전이면 '그 뒤 고점까지 더 오른 몫', 고점 뒤면 '그때까지 빠진 몫' · 둘 다 '그날부터 바닥까지'
            first = next((k for k in starts if max(p - look, prev_lo + 1) <= k <= lo), None)
            prev_lo = lo
            per[bname] = None if first is None else {
                "date": ds[first], "before_peak": first < p,
                "rise_to_peak": f"{(px[p] / px[first] - 1) * 100:+.1f}%" if first < p else None,
                "fallen_from_peak": None if first < p else f"{(px[first] / px[p] - 1) * 100:.1f}%",
                "signal_to_trough": f"{(px[lo] / px[first] - 1) * 100:.1f}%", "peak_to_trough": f"{(px[lo] / px[p] - 1) * 100:.1f}%"}
        B[name] = {"n_signals": len(rows), "n_with_2y": len(hit), "followed_by_20pct_fall_2y": bear2, "false_alarm_2y": len(hit) - bear2,
                   "bears": per, "signals": rows}
        log.info("signal=%s n=%d with2y=%d bear_after=%d false=%d bears=%s", name, len(rows), len(hit), bear2, len(hit) - bear2,
                 json.dumps({k: (v and (v["date"], v["rise_to_peak"] or v["fallen_from_peak"], v["signal_to_trough"], v["peak_to_trough"])) for k, v in per.items()}, ensure_ascii=False), extra={"stage": "B_SIG"})
    base = share(every, Y2, 0.20)
    B["_base_any_day_2y_-20%"] = base

    # ---------- C. VIX 40 넘은 첫날
    cash = np.ones(len(ds))
    for k in range(1, len(ds)):
        r = irx[k - 1] if irx[k - 1] == irx[k - 1] else 0.0
        cash[k] = cash[k - 1] * (1 + r / 100) ** ((date.fromisoformat(ds[k]) - date.fromisoformat(ds[k - 1])).days / 365)

    def run_buy(i, j, months):
        y, m, dd = int(ds[i][:4]), int(ds[i][5:7]), ds[i][8:]
        buys = {bisect.bisect_left(ds, f"{y + (m - 1 + k) // 12:04d}-{(m - 1 + k) % 12 + 1:02d}-{dd}") for k in range(months)}
        c, u, worst = 1.0, 0.0, 1.0
        for k in range(i, j + 1):
            if k in buys:
                u += (1.0 / months) / tr[k]
                c -= 1.0 / months
            worst = min(worst, c + u * tr[k])
            if k < j:
                c *= cash[k + 1] / cash[k]
        return c + u * tr[j], worst

    C = []
    for i in first_on(vix > 40):
        j = min(len(ds) - 1, i + Y2)
        a, wa = run_buy(i, j, 1)
        b, wb = run_buy(i, j, 12)
        C.append({"date": ds[i], "vix": round(float(vix[i]), 1), "from_peak": f"{(px[i] / run[ds[i]] - 1) * 100:.1f}%",
                  "further_fall": f"{fwd_dd(px, i, Y2) * 100:.1f}%", "full_2y": i + Y2 <= len(ds) - 1, "end": ds[j],
                  "lump_10k": round(a * 1e4), "lump_worst": f"{(wa - 1) * 100:.0f}%", "split_10k": round(b * 1e4), "split_worst": f"{(wb - 1) * 100:.0f}%",
                  "tbill_10k": round(cash[j] / cash[i] * 1e4)})
        log.info("vix40 date=%s vix=%.1f from_peak=%s further=%s lump=%s(%s) split=%s(%s) tbill=%s", C[-1]["date"], vix[i], C[-1]["from_peak"], C[-1]["further_fall"],
                 C[-1]["lump_10k"], C[-1]["lump_worst"], C[-1]["split_10k"], C[-1]["split_worst"], C[-1]["tbill_10k"], extra={"stage": "C_VIX40"})
    full = [c for c in C if c["full_2y"]]
    Csum = {"n": len(C), "n_full_2y": len(full), "lump_above_principal_2y": sum(c["lump_10k"] > 10000 for c in full),
            "split_above_principal_2y": sum(c["split_10k"] > 10000 for c in full),
            "lump_below_80": sum(float(c["lump_worst"][:-1]) < -20 for c in C), "split_below_80": sum(float(c["split_worst"][:-1]) < -20 for c in C)}
    log.info("vix40 summary=%s", Csum, extra={"stage": "C_VIX40"})

    out = HERE / f"crash_tests_{date.today().isoformat()}.json"
    out.write_text(json.dumps({"tool": f"crash_tests.py {VERSION}", "range": f"{ds[0]} ~ {ds[-1]}", "gap_days": GAP,
                               "A_all_time_high": A, "B_signals": B, "C_vix40": {"summary": Csum, "cases": C}}, ensure_ascii=False, indent=1), "utf-8")
    log.info("file=%s", out.name, extra={"stage": "DONE"})


if __name__ == "__main__":
    main()
