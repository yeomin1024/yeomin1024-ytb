#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.4 — 2026-11-28 — 대본용 예시: 하루 −10% 뒤 +10% (1배·3배) · 엔비디아 11-23 하루 · 큰 반등 날부터 지수 200일선 회복까지 거래일.
# 이전 v1.3 — 2026-11-28 — summary: 결과가 있는 큰 반등 날마다 방법 견줌 수(가장 나빴던 때 · 끝 결과) · 이번 구간 큰 반등 뒤 새 저점 수.
# 이전 v1.2 — 2026-11-28 — 구간 끝 = 새 1년 최고가 (v1.1 은 옛 고점 값을 되찾을 때까지라 2025-04 폭락이 또 합쳐짐) · 이번 구간 큰 반등 날의 '지금까지' 결과 · 방법마다 1년 동안 가장 나빴던 때.
# 이전 v1.1 — 2026-11-28 — 고점 = 지난 1년(252거래일) 최고 종가 (v1.0 은 10년 누적 최고라 2025-04 폭락이 2022 구간에 합쳐졌음 — 시청자가 말하는 '고점 대비'는 최근 고점).
# 이전 v1.0 — 2026-11-28 — 최초. 주식 #1 'SOXL 반등, 지금 사도 될까 — 사기 전 확인할 것' 대본의 모든 숫자 (사용자 지시 2026-11-28
#          "1번으로 대본 만들어봐" · "변수 발생할 수 있는 이벤트 일정, 전문가 스탠스, 현재 호재와 악재, 기술적 지표, 과거 사례 모두 확인해서 해야돼").
# CHANGELOG
#   v1.0 2026-11-28  지금(11-27 마감) 숫자 · 기술 지표(이동평균·RSI·200일선) · 과거 SOXL 고점 대비 −70% 넘은 하락 구간 · 그 안의 '큰 반등 날'
#                    (고점 대비 −80% 넘게 하락한 채 하루 +14% 넘게 오른 날 — 2026-11-27 +14.2% 와 같은 꼴) 뒤 결과 · 세 가지 사는 방법 비교
#                    (한 번에 · 가격 기준 나눠 사기 · 반도체 지수 200일선 회복 뒤) · 지수가 고점을 되찾은 날 SOXL 은 어디였나.
#   v1.1 2026-11-28  고점 = 그날까지 지난 252거래일 최고 종가 (하락 구간·큰 반등 날 모두) · 구간 끝 = 그 고점을 되찾은 날.
#   v1.2 2026-11-28  구간 끝 = 그날 종가가 지난 252거래일 최고가 (새 1년 최고) · 큰 반등 날마다 '지금까지'(1년이 안 찬 이번 구간): 그 뒤 가장 낮은 값 ·
#                    그날 앞 구간 최저가보다 더 내려갔나(new_low) · 지금까지 수익률 · 방법마다 1년 동안 예산 대비 가장 나빴던 값(worst).
#   v1.3 2026-11-28  summary — 대본 문장 '일곱 번 모두 …'·'세 번 중 두 번' 같은 셈을 손으로 세지 않게.
#   v1.4 2026-11-28  example(−10% 뒤 +10%: 1배 −1.0% · 3배 −9.0%) · nvda_1123 · signal 마다 trend_days(그날부터 지수 200일선 회복까지 거래일).
# 쓰는 법: python3 calc/soxl_check.py [--refresh] [--log-level DEBUG]  → calc/soxl_check_<마지막 거래일>.json
# 자료 = Yahoo Finance 차트 API 일별 종가(수정 종가 아님 — 분할 반영 종가) · 10년 · calc/data/*.csv 에 저장해 다시 받지 않음(--refresh 면 다시).
# ※ 연구·교육용 — 투자 권유가 아님. 과거 결과는 앞으로를 보장하지 않음. 수수료·세금·환율은 넣지 않음.
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import logging
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / "tools"))
VERSION = "v1.4"
KST = dt.timezone(dt.timedelta(hours=9))
SYMS = ["SOXL", "^SOX", "NVDA", "^IXIC", "^GSPC", "^VIX"]
DD_EPISODE = -0.70      # 하락 구간 = 고점 대비 이보다 깊게
DD_SIGNAL = -0.80       # 큰 반등 날 조건 1 — 고점 대비 이보다 깊게 하락한 상태
UP_SIGNAL = 0.14        # 큰 반등 날 조건 2 — 하루 상승률 (2026-11-27 SOXL +14.2%)
SPLIT_STEPS = (0.0, -0.15, -0.30)   # 가격 기준 나눠 사기: 첫 매수가 대비 그대로 · −15% · −30% 에 1/3 씩 (사용자 규칙 6 — 기간이 아니라 가격)
HOLD = 252              # 1년 = 252 거래일


def log(stage, level=logging.INFO, **kv):
    logging.log(level, f"[{stage}] [{dt.datetime.now(KST).isoformat(timespec='seconds')}] " + " ".join(f"{k}={v}" for k, v in kv.items()))


def load(sym: str, refresh: bool) -> list[dict]:
    p = HERE / "data" / (sym.replace("^", "IDX_") + ".csv")
    if p.is_file() and not refresh:
        rows = [{"date": r["date"], "close": float(r["close"])} for r in csv.DictReader(p.open(encoding="utf-8"))]
        log("LOAD", sym=sym, source="cache", rows=len(rows), first=rows[0]["date"], last=rows[-1]["date"])
        return rows
    import market_data as md
    try:
        raw = md.fetch_one(sym, "10y")
    except Exception as e:
        raise SystemExit(f"[LOAD] {sym} 받기 실패 ({type(e).__name__}: {e}) — 허용 목록 query1.finance.yahoo.com 확인 · 캐시가 있으면 --refresh 없이")
    rows = [{"date": r["date"], "close": float(r["close"])} for r in raw if r.get("close")]
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["date", "close"]); w.writeheader(); w.writerows(rows)
    log("LOAD", sym=sym, source="Yahoo 10y daily", rows=len(rows), first=rows[0]["date"], last=rows[-1]["date"])
    return rows


def validate(sym, rows):
    ds = [r["date"] for r in rows]
    dup = len(ds) - len(set(ds))
    bad = [r for r in rows if not (r["close"] > 0)]
    gaps = sum(1 for a, b in zip(ds, ds[1:]) if (dt.date.fromisoformat(b) - dt.date.fromisoformat(a)).days > 5)
    big = [(b["date"], round(b["close"] / a["close"] - 1, 3)) for a, b in zip(rows, rows[1:]) if abs(b["close"] / a["close"] - 1) > (0.6 if sym == "SOXL" else 0.3)]
    log("VALIDATE", logging.WARNING if (dup or bad or gaps) else logging.INFO, sym=sym, dup=dup, nonpositive=len(bad), gaps_over_5d=gaps, big_moves=big[:5])
    if sorted(ds) != ds:
        raise SystemExit(f"[VALIDATE] {sym} 날짜 순서가 아님")


def sma(xs, n, i):
    return sum(xs[i - n + 1:i + 1]) / n if i + 1 >= n else None


def rsi(xs, n=14):
    """Wilder RSI — i 시점 값은 i 까지의 종가만 씀 (앞날 자료 없음)."""
    out = [None] * len(xs)
    if len(xs) <= n:
        return out
    g = [max(xs[i] - xs[i - 1], 0) for i in range(1, len(xs))]
    l = [max(xs[i - 1] - xs[i], 0) for i in range(1, len(xs))]
    ag, al = sum(g[:n]) / n, sum(l[:n]) / n
    out[n] = 100 - 100 / (1 + ag / al) if al else 100
    for i in range(n + 1, len(xs)):
        ag = (ag * (n - 1) + g[i - 1]) / n
        al = (al * (n - 1) + l[i - 1]) / n
        out[i] = 100 - 100 / (1 + ag / al) if al else 100
    return out


def pct(a, b):
    return round((a / b - 1) * 100, 1)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--refresh", action="store_true")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args(argv)
    logging.basicConfig(level=getattr(logging, a.log_level), format="%(message)s", stream=sys.stdout)
    t0 = time.time()
    D = {s: load(s, a.refresh) for s in SYMS}
    for s, rows in D.items():
        validate(s, rows)
    soxl = D["SOXL"]
    dates = [r["date"] for r in soxl]
    C = [r["close"] for r in soxl]
    sox_map = {r["date"]: r["close"] for r in D["^SOX"]}
    # SOX 를 SOXL 날짜에 맞춤 (같은 미국 장 — 빠진 날은 앞 값)
    S, last = [], None
    for d in dates:
        last = sox_map.get(d, last); S.append(last)
    if any(x is None for x in S):
        raise SystemExit("[ALIGN] SOX 앞쪽 값이 비어 있음")
    n = len(C) - 1
    log("ALIGN", days=len(C), first=dates[0], last=dates[n])

    # ── 지금
    i1y = max(0, n - HOLD + 1)
    hi_i = max(range(i1y, n + 1), key=lambda i: C[i])
    shi_i = max(range(i1y, n + 1), key=lambda i: S[i])
    r_soxl, r_sox = rsi(C), rsi(S)
    chg = lambda xs, i: round((xs[i] / xs[i - 1] - 1) * 100, 1)
    recent = [{"date": dates[i], "soxl": chg(C, i), "sox": chg(S, i)} for i in range(n - 6, n + 1)]
    now = {
        "date": dates[n], "soxl": C[n], "soxl_high": C[hi_i], "soxl_high_date": dates[hi_i], "soxl_from_high": pct(C[n], C[hi_i]),
        "soxl_need_x": round(C[hi_i] / C[n], 1), "soxl_need_pct": pct(C[hi_i], C[n]),
        "sox": S[n], "sox_high": S[shi_i], "sox_high_date": dates[shi_i], "sox_from_high": pct(S[n], S[shi_i]), "sox_need_pct": pct(S[shi_i], S[n]),
        "sox_from_soxl_high_date": pct(S[n], S[hi_i]),
        "soxl_ma": {k: round(sma(C, k, n), 2) for k in (20, 50, 200)}, "sox_ma": {k: round(sma(S, k, n), 1) for k in (20, 50, 200)},
        "soxl_vs_ma": {k: pct(C[n], sma(C, k, n)) for k in (20, 50, 200)}, "sox_vs_ma": {k: pct(S[n], sma(S, k, n)) for k in (20, 50, 200)},
        "rsi14_soxl": round(r_soxl[n], 1), "rsi14_sox": round(r_sox[n], 1),
        "rsi14_soxl_min_20d": round(min(r_soxl[n - 19:n + 1]), 1),
        "sox_days_below_ma200": next((k for k in range(0, 400) if S[n - k] >= sma(S, 200, n - k)), None),
        "recent": recent,
    }
    vix = {r["date"]: r["close"] for r in D["^VIX"]}
    vd = sorted(vix)
    now["vix"] = vix[vd[-1]]
    now["vix_max_30d"] = max(vix[d] for d in vd[-22:])
    now["vix_max_30d_date"] = max(vd[-22:], key=lambda d: vix[d])
    log("NOW", soxl=C[n], from_high=now["soxl_from_high"], need_x=now["soxl_need_x"], sox_from_high=now["sox_from_high"], rsi_soxl=now["rsi14_soxl"],
        soxl_vs_ma200=now["soxl_vs_ma"][200], sox_vs_ma200=now["sox_vs_ma"][200], vix=now["vix"])

    # ── 과거 하락 구간 (고점 대비 −70% 넘게)
    def peak_idx(i):                                   # 그날 앞(그날 포함) 252거래일 안 최고 종가의 자리 — 앞날 자료 없음
        lo = max(0, i - HOLD + 1)
        return max(range(lo, i + 1), key=lambda k: C[k])
    eps, i = [], 0
    while i < len(C):
        p = peak_idx(i)
        if C[i] / C[p] - 1 <= DD_EPISODE:
            t = i
            j = i
            while j < len(C) and not (j > i and C[j] >= C[peak_idx(j)]):   # 새 1년 최고가가 나올 때까지 한 구간
                if C[j] < C[t]:
                    t = j
                j += 1
            eps.append({"peak_i": p, "trough_i": t, "dd": C[t] / C[p] - 1, "end_i": j if j < len(C) else None})
            i = j + 1
        else:
            i += 1
    episodes = []
    for e in eps:
        p, t = e["peak_i"], e["trough_i"]
        rec = {"peak": dates[p], "trough": dates[t], "dd": round(e["dd"] * 100, 1), "days_to_trough": t - p,
               "recovered": dates[e["end_i"]] if e.get("end_i") else None, "ongoing": e.get("end_i") is None}
        # SOX 가 SOXL 고점 날 값을 되찾은 첫날, 그날 SOXL 은 고점 대비 몇 %
        k = next((j for j in range(t, len(C)) if S[j] >= S[p]), None)
        rec["sox_back_to_peak_date"] = dates[k] if k else None
        rec["soxl_from_peak_that_day"] = pct(C[k], C[p]) if k else None
        rec["sox_dd_same_trough"] = pct(S[t], S[p])
        episodes.append(rec)
        log("EPISODE", **{k_: v for k_, v in rec.items()})

    # ── 큰 반등 날 (고점 대비 −80% 넘게 하락한 채 하루 +14% 넘게)
    signals = []
    for i in range(1, len(C)):
        p = peak_idx(i - 1)
        if C[i - 1] / C[p] - 1 <= DD_SIGNAL and C[i] / C[i - 1] - 1 >= UP_SIGNAL:
            signals.append(i)
    sig_rows = []
    ma200 = [sma(S, 200, i) for i in range(len(S))]
    def ep_low_before(i):                               # 그날 앞, 같은 하락 구간(그날 1년 고점 뒤) 최저가
        p = peak_idx(i - 1)
        return min(C[p:i])

    def method_paths(i, end):
        """세 방법의 예산(1) 대비 가치 — 날마다. 반환 (끝 가치, 가장 나쁜 가치, 산 날들, 투자 비율)."""
        b0, units, cash, buys, hits = C[i], 0.0, 1.0, [], set()
        one = [C[k] / C[i] for k in range(i, end + 1)]
        split_v = []
        for k in range(i, end + 1):
            for j, step in enumerate(SPLIT_STEPS):
                if j in hits:
                    continue
                if (j == 0 and k == i) or (j and C[k] <= b0 * (1 + step)):
                    units += (1 / 3) / C[k]; cash -= 1 / 3; buys.append(dates[k]); hits.add(j)
            split_v.append(units * C[k] + cash)
        kb = next((k for k in range(i, end + 1) if ma200[k] and S[k] >= ma200[k]), None)
        trend_v = [1.0 if (kb is None or k < kb) else C[k] / C[kb] for k in range(i, end + 1)]
        return ({"end": one[-1] - 1, "worst": min(one) - 1},
                {"end": split_v[-1] - 1, "worst": min(split_v) - 1, "buys": buys, "invested": 1 - cash},
                {"end": trend_v[-1] - 1, "worst": min(trend_v) - 1, "buy": dates[kb] if kb is not None else None})

    for i in signals:
        end = i + HOLD
        row = {"date": dates[i], "up": round((C[i] / C[i - 1] - 1) * 100, 1), "close": C[i], "dd_prev": pct(C[i - 1], C[peak_idx(i - 1)]),
               "low_before": ep_low_before(i)}
        e2 = min(end, n)
        if e2 > i:
            seg = C[i + 1:e2 + 1]
            o, sp, tr = method_paths(i, e2)
            row["so_far"] = {"to": dates[e2], "full_year": end <= n, "ret": pct(C[e2], C[i]), "min_after": pct(min(seg), C[i]),
                             "min_after_date": dates[i + 1 + seg.index(min(seg))], "new_low": min(seg) < row["low_before"],
                             "one": {k: round(v * 100, 1) for k, v in o.items()},
                             "split": {"end": round(sp["end"] * 100, 1), "worst": round(sp["worst"] * 100, 1), "buys": sp["buys"], "invested": round(sp["invested"] * 100)},
                             "trend": {"end": round(tr["end"] * 100, 1), "worst": round(tr["worst"] * 100, 1), "buy": tr["buy"]}}
        if end <= n:
            seg = C[i + 1:end + 1]
            row.update(ret_1y=pct(C[end], C[i]), min_after=pct(min(seg), C[i]), new_low_after=min(seg) < min(C[max(0, i - 260):i]),
                       ret_3m=pct(C[i + 63], C[i]), ret_6m=pct(C[i + 126], C[i]))
            # 세 가지 사는 방법 (같은 돈 · 같은 끝날 = 그날 + 1년)
            one = C[end] / C[i] - 1
            b0, units, cash, buys = C[i], 0.0, 1.0, []
            for j, step in enumerate(SPLIT_STEPS):
                lvl = b0 * (1 + step)
                hit = next((k for k in range(i, end + 1) if C[k] <= lvl), None) if j else i
                if hit is not None:
                    units += (1 / 3) / C[hit]; cash -= 1 / 3; buys.append(dates[hit])
            split = units * C[end] + cash - 1
            k = next((k for k in range(i, end + 1) if ma200[k] and S[k] >= ma200[k]), None)
            trend = (C[end] / C[k] - 1) if k is not None else 0.0
            row.update(one_shot=round(one * 100, 1), split=round(split * 100, 1), split_buys=buys, split_invested=round((1 - cash) * 100),
                       trend=round(trend * 100, 1), trend_buy=dates[k] if k is not None else None,
                       one_min_value=round((min(C[i:end + 1]) / C[i] - 1) * 100, 1))
        sig_rows.append(row)
    log("SIGNALS", n=len(sig_rows), dates=",".join(r["date"] for r in sig_rows))
    for r in sig_rows:
        log("SIGNAL", logging.DEBUG, **r)
    # 구간마다 첫 큰 반등 날만 (같은 하락 구간 안의 뒤 신호는 겹침 — 따로 셈)
    first_per_ep = []
    for e in episodes:
        xs = [r for r in sig_rows if e["peak"] <= r["date"] <= (e["recovered"] or "9999")]
        if xs:
            first_per_ep.append({"episode_peak": e["peak"], "first_signal": xs[0], "signals_in_episode": len(xs),
                                 "later_new_low": sum(1 for r in xs if r.get("new_low_after"))})
    measured = [r for r in sig_rows if r.get("so_far")]
    past = [r for r in measured if r["so_far"]["full_year"]]
    cur = [r for r in measured if not r["so_far"]["full_year"]]
    summ = {
        "signals_measured": len(measured), "signals_past_full_year": len(past), "signals_current_episode": len(cur) + sum(1 for r in sig_rows if not r.get("so_far")),
        "split_worst_better_than_one": sum(1 for r in measured if r["so_far"]["split"]["worst"] > r["so_far"]["one"]["worst"]),
        "split_end_better_than_one": sum(1 for r in measured if r["so_far"]["split"]["end"] > r["so_far"]["one"]["end"]),
        "past_one_year_positive": sum(1 for r in past if r["so_far"]["one"]["end"] > 0),
        "past_min_after_range": [min(r["so_far"]["min_after"] for r in past), max(r["so_far"]["min_after"] for r in past)] if past else None,
        "current_new_low_after": sum(1 for r in cur if r["so_far"]["new_low"]), "current_measured": len(cur),
        "sox_back_soxl_gap": [e["soxl_from_peak_that_day"] for e in episodes if e["soxl_from_peak_that_day"] is not None],
    }
    summ["example_down_up_10"] = {"x1": round((0.9 * 1.1 - 1) * 100, 1), "x3": round((0.7 * 1.3 - 1) * 100, 1)}
    nv = {r["date"]: r["close"] for r in D["NVDA"]}
    nd = sorted(nv)
    summ["nvda_1123"] = round((nv["2026-11-23"] / nv[nd[nd.index("2026-11-23") - 1]] - 1) * 100, 1) if "2026-11-23" in nv else None
    for r in sig_rows:
        tb = (r.get("so_far") or {}).get("trend", {}).get("buy")
        r["trend_days"] = (dates.index(tb) - dates.index(r["date"])) if tb else None
    log("SUMMARY", **summ)
    out = {"tool": f"soxl_check.py {VERSION}", "made": dt.datetime.now(KST).isoformat(timespec="seconds"), "source": "Yahoo Finance chart API 일별 종가 10년",
           "rules": {"episode_dd": DD_EPISODE, "signal_dd": DD_SIGNAL, "signal_up": UP_SIGNAL, "split_steps": SPLIT_STEPS, "hold_days": HOLD,
                     "trend": "반도체 지수(^SOX) 종가 ≥ 200일 평균 첫날 한 번에", "split": "첫날 1/3 · 첫 매수가 −15% 에 1/3 · −30% 에 1/3 — 안 닿으면 현금(0%)",
                     "costs": "수수료·세금·환율 없음"},
           "now": now, "summary": summ, "episodes": episodes, "signals": sig_rows, "first_per_episode": first_per_ep}
    p = HERE / f"soxl_check_{dates[n]}.json"
    p.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", "utf-8")
    log("DONE", out=str(p.relative_to(ROOT)), sec=round(time.time() - t0, 1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
