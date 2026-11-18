#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-11-18 — F 나스닥100 30% 넘는 하락·회복 기간 더함 (제목 T1 을 반도체 → 나스닥100 — 페르소나 P1 이 2회차 모두 '반도체 지수는 내 상품이 아님').
#   · E5 = 같은 규칙을 폭락 고점에서 시작한 5년(2000-03 · 2007-10 · 2008-01) · 3년(2020-02 · 2022-01) 으로 (제목 T5 숫자).
# 이전 v1.0 — 2026-11-18 — 제목 5안의 숫자 (사용자 지시 "주식 주제 페르소나와 유튜브 분석 결과를 최신화하여 참고해서 만들 영상 제목 5개 알려줘봐").
#   제목 숫자는 이 계산 출력만 (CLAUDE.md — 숫자는 계산 코드 출력만). 자료 = Yahoo Finance chart API v8 일별 (close · adjclose = 배당·분할 반영).
#   판정 규칙(계산 전에 정함):
#   A 계좌 보는 간격: SPY 수정 종가(배당 포함) — 간격 n 거래일 뒤 값이 그날보다 낮으면 '손실'. 간격 = 1일·1달(21)·1년(252)·3년(756)·5년(1260), 모든 시작일.
#   B S&P 500(^GSPC, 가격 지수 — 배당 뺌) 고점보다 20% 아래로 처음 마감한 날(하락장마다 한 번 · 고점 회복 전 다시 세지 않음) → 1년 뒤 버틴 사람(보유) 수익률. 판 사람 = 그날 현금(0%).
#      '판 사람이 이김' = 1년 뒤 보유 수익률 < 0. 1950-01 이후.
#   C 배당·커버드콜 ETF vs SPY: 같은 하락 구간(SPY 고점 → SPY 저점 날짜)에서 각자의 수정 종가 하락률. 구간 = SPY 가 고점보다 15% 넘게 빠진 하락(2020·2022·2025 등).
#   D 반도체 지수(^SOX, 가격): 고점보다 50% 넘게 빠진 하락마다 — 고점 → 그 고점을 다시 넘은 날까지 걸린 해.
#   F 나스닥100(^NDX 가격 · QQQ 배당 포함): 고점보다 30% 넘게 빠진 하락마다 — 고점 → 고점을 다시 넘은 날까지 걸린 해·달.
#   E 월 적립(SPY 수정 종가, 매달 첫 거래일 같은 돈): '계속' vs '멈춤'(고점보다 20% 아래인 달은 사지 않고 현금으로 모음 → 고점을 되찾은 달에 모은 돈을 한꺼번에 삼). 시작 2000-01 · 2007-01 · 2019-01 · 2021-01, 끝 = 마지막 거래일.
# 로그: [STAGE] [시각] key=value  · 실행: python3 stock/topics/titles_2026-11-18/calc.py [--refetch]
# ※ 연구·교육용 — 투자 권유가 아님. 과거 자료라 앞으로도 같다는 보장은 없음.
from __future__ import annotations
import csv, json, sys, time, urllib.parse, urllib.request
from datetime import date, datetime, timezone
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
VERSION = "v1.1"

def log(stage, **kv):
    print(f"[{stage}] [{time.strftime('%Y-%m-%dT%H:%M:%S')}] " + " ".join(f"{k}={v}" for k, v in kv.items()), flush=True)

def fetch(sym, start=date(1950, 1, 1), refetch=False):
    p = DATA / f"{sym.replace('^','_')}.csv"
    if not p.exists() or refetch:
        p1 = int(datetime(start.year, start.month, start.day, tzinfo=timezone.utc).timestamp())
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(sym)}?period1={p1}&period2={int(time.time())}&interval=1d&events=div%2Csplit"
        last = None
        for w in (0, 2, 5, 10):
            time.sleep(w)
            try:
                with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=60) as r:
                    res = json.load(r)["chart"]["result"][0]
                break
            except Exception as e:      # 네트워크·Yahoo 오류 — 다시
                last = e; log("FETCH", symbol=sym, error=repr(e)[:100], retry=w)
        else:
            raise SystemExit(f"[FETCH] ❌ {sym}: {last!r} → 네트워크 확인 뒤 --refetch")
        q = res["indicators"]["quote"][0]["close"]; adj = res["indicators"].get("adjclose", [{}])[0].get("adjclose", q)
        rows = [(datetime.fromtimestamp(t, tz=timezone.utc).date().isoformat(), c, a) for t, c, a in zip(res["timestamp"], q, adj) if c is not None and a is not None]
        DATA.mkdir(parents=True, exist_ok=True)
        with p.open("w", encoding="utf-8", newline="") as f:
            f.write(f"# {sym} Yahoo chart v8 · {date.today()} 받음 · calc.py {VERSION}\n"); w_ = csv.writer(f); w_.writerow(["date","close","adj"]); w_.writerows(rows)
    with p.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(l for l in f if not l.startswith("#")))
    d = np.array([date.fromisoformat(r["date"]) for r in rows]); c = np.array([float(r["close"]) for r in rows]); a = np.array([float(r["adj"]) for r in rows])
    ok = np.isfinite(c) & (c > 0)
    log("LOAD", symbol=sym, rows=int(ok.sum()), first=d[ok][0], last=d[ok][-1])
    return d[ok], c[ok], a[ok]

def calc_A(d, a):
    out = {}
    for name, n in (("1일", 1), ("1달", 21), ("1년", 252), ("3년", 756), ("5년", 1260)):
        r = a[n:] / a[:-n] - 1
        out[name] = {"loss_pct": round(float((r < 0).mean() * 100), 1), "samples": int(len(r))}
    return {"symbol": "SPY", "from": str(d[0]), "to": str(d[-1]), "by_interval": out}

def calc_B(d, c):
    ev, peak, in_bear = [], c[0], False
    pk_i = 0
    for i in range(len(c)):
        if c[i] > peak: peak, pk_i, in_bear = c[i], i, False
        if not in_bear and c[i] <= peak * 0.8:
            in_bear = True
            j = np.searchsorted(d, date(d[i].year + 1, d[i].month, min(d[i].day, 28)))
            r1 = float(c[j] / c[i] - 1) if j < len(c) else None
            # 그 하락장의 바닥 (고점 회복 전 가장 낮은 값)
            k = i
            while k < len(c) and c[k] < peak: k += 1
            low = float(c[i:k].min() / peak - 1); low_after = float(c[i:k].min() / c[i] - 1)
            ev.append({"day": str(d[i]), "peak_day": str(d[pk_i]), "hold_1y_pct": None if r1 is None else round(r1 * 100, 1),
                       "worst_from_peak_pct": round(low * 100, 1), "more_drop_after_day_pct": round(low_after * 100, 1),
                       "recovered": str(d[k]) if k < len(c) else None})
    done = [e for e in ev if e["hold_1y_pct"] is not None]
    return {"symbol": "^GSPC (가격 지수)", "events": ev, "n_with_1y": len(done),
            "sell_wins": sum(e["hold_1y_pct"] < 0 for e in done), "hold_wins": sum(e["hold_1y_pct"] > 0 for e in done)}

def dd_windows(d, a, thr=0.15, start=date(2006, 12, 1)):
    m = d >= start; d, a = d[m], a[m]
    out, peak, pk = [], a[0], 0
    i = 0
    while i < len(a):
        if a[i] > peak: peak, pk = a[i], i
        if a[i] <= peak * (1 - thr):
            k = i
            while k < len(a) and a[k] < peak: k += 1
            tr = i + int(np.argmin(a[i:k])) if k > i else i
            out.append((d[pk], d[tr], round(float(a[tr] / peak - 1) * 100, 1), d[k] if k < len(a) else None))
            i = k; peak = a[k] if k < len(a) else peak; pk = k
            continue
        i += 1
    return out

def calc_C(series):
    sd, sa = series["SPY"][0], series["SPY"][2]
    wins = dd_windows(sd, sa)
    res = []
    for pk, tr, spy_dd, rec in wins:
        row = {"spy_peak": str(pk), "spy_trough": str(tr), "SPY": spy_dd}
        for s in ("SCHD", "VYM", "DVY", "JEPI", "QYLD", "XYLD"):
            d, _, a = series[s]
            if d[0] > pk: row[s] = None; continue
            m = (d >= pk) & (d <= tr)
            seg = a[m]
            row[s] = round(float(seg.min() / seg[0] - 1) * 100, 1) if len(seg) else None
        res.append(row)
    return {"rule": "SPY 고점~저점 구간 안에서 각 ETF 의 첫날 대비 가장 낮은 값 (수정 종가)", "windows": res}

def calc_D(d, c):
    ev, peak, pk = [], c[0], 0
    i = 0
    while i < len(c):
        if c[i] > peak: peak, pk = c[i], i
        if c[i] <= peak * 0.5:
            k = i
            while k < len(c) and c[k] < peak: k += 1
            tr = i + int(np.argmin(c[i:k]))
            ev.append({"peak": str(d[pk]), "half_day": str(d[i]), "trough": str(d[tr]), "worst_pct": round(float(c[tr] / peak - 1) * 100, 1),
                       "recovered": str(d[k]) if k < len(c) else None,
                       "years_to_recover": round((d[k] - d[pk]).days / 365.25, 1) if k < len(c) else None,
                       "years_from_half_day": round((d[k] - d[i]).days / 365.25, 1) if k < len(c) else None})
            i = k; peak = c[k] if k < len(c) else peak; pk = k
            continue
        i += 1
    cur = {"last": str(d[-1]), "from_peak_pct": round(float(c[-1] / c.max() - 1) * 100, 1), "peak": str(d[int(np.argmax(c))])}
    return {"symbol": "^SOX (가격)", "events": ev, "now": cur}

def calc_F(d, s, label, thr=0.30):
    ev, peak, pk, i = [], s[0], 0, 0
    while i < len(s):
        if s[i] > peak: peak, pk = s[i], i
        if s[i] <= peak * (1 - thr):
            k = i
            while k < len(s) and s[k] < peak: k += 1
            tr = i + int(np.argmin(s[i:k]))
            ev.append({"peak": str(d[pk]), "trough": str(d[tr]), "worst_pct": round(float(s[tr] / peak - 1) * 100, 1),
                       "recovered": str(d[k]) if k < len(s) else None,
                       "years": round((d[k] - d[pk]).days / 365.25, 1) if k < len(s) else None,
                       "months": round((d[k] - d[pk]).days / 30.44, 1) if k < len(s) else None})
            i = k; peak = s[k] if k < len(s) else peak; pk = k
            continue
        i += 1
    return {"series": label, "events": ev, "now_from_peak_pct": round(float(s[-1] / s.max() - 1) * 100, 1), "peak": str(d[int(np.argmax(s))]), "last": str(d[-1])}

def calc_E(d, c, a, monthly=1.0):
    res = {}
    for y0 in (2000, 2007, 2019, 2021):
        m = d >= date(y0, 1, 1); dd, cc, aa = d[m], c[m], a[m]
        firsts = [0] + [i for i in range(1, len(dd)) if dd[i].month != dd[i - 1].month]
        peak_c = c[d < date(y0, 1, 1)].max() if (d < date(y0, 1, 1)).any() else cc[0]
        sh_a = sh_b = cash_b = 0.0; paid = 0.0; paused = 0
        pk = peak_c
        for i in firsts:
            pk = max(pk, cc[:i + 1].max()) if i else max(pk, cc[0])
            paid += monthly
            sh_a += monthly / aa[i]
            if cc[i] <= pk * 0.8:
                cash_b += monthly; paused += 1
            else:
                sh_b += (monthly + cash_b) / aa[i]; cash_b = 0.0
        va = sh_a * aa[-1]; vb = sh_b * aa[-1] + cash_b
        res[str(y0)] = {"months": len(firsts), "paused_months": paused, "paid": paid, "keep": round(va, 2), "pause": round(vb, 2),
                        "pause_vs_keep_pct": round((vb / va - 1) * 100, 1), "to": str(dd[-1])}
    return {"rule": "매달 첫 거래일 1(돈 단위) — 멈춤 = 그달 첫날 S&P 500 가격이 그때까지 고점의 80% 이하면 현금으로, 아니면 모은 현금까지 삼 · 배당은 SPY 수정 종가로", "starts": res}

def calc_E5(gd, gc, sd, sa, windows=((2000, 3, 5), (2007, 10, 5), (2008, 1, 5), (2020, 2, 3), (2022, 1, 3))):
    idx = np.clip(np.searchsorted(gd, sd), 0, len(gd) - 1); gcs = gc[idx]
    out = {}
    for y0, m0, yrs in windows:
        m = (sd >= date(y0, m0, 1)) & (sd < date(y0 + yrs, m0, 1)); dd, cc, aa = sd[m], gcs[m], sa[m]
        firsts = [0] + [i for i in range(1, len(dd)) if dd[i].month != dd[i - 1].month]
        pk = gc[gd < date(y0, m0, 1)].max()
        a = b = cash = 0.0; paused = 0
        for i in firsts:
            pk = max(pk, cc[:i + 1].max())
            a += 1 / aa[i]
            if cc[i] <= pk * 0.8: cash += 1; paused += 1
            else: b += (1 + cash) / aa[i]; cash = 0.0
        paid = len(firsts); va = a * aa[-1]; vb = b * aa[-1] + cash
        out[f"{y0}-{m0:02d}+{yrs}y"] = {"months": paid, "paused_months": paused, "keep_return_pct": round((va / paid - 1) * 100, 1),
                                          "pause_return_pct": round((vb / paid - 1) * 100, 1), "diff_krw_if_500k_month": round((va - vb) * 500000), "end": str(dd[-1])}
    return out

def main():
    refetch = "--refetch" in sys.argv
    t0 = time.time()
    S = {}
    S["^GSPC"] = fetch("^GSPC", refetch=refetch)
    for s in ("SPY", "SCHD", "VYM", "DVY", "JEPI", "QYLD", "XYLD"):
        S[s] = fetch(s, start=date(1993, 1, 1), refetch=refetch)
    S["^SOX"] = fetch("^SOX", start=date(1994, 1, 1), refetch=refetch)
    S["^NDX"] = fetch("^NDX", start=date(1985, 1, 1), refetch=refetch)
    S["QQQ"] = fetch("QQQ", start=date(1999, 3, 1), refetch=refetch)
    out = {"tool": f"calc.py {VERSION}", "made": datetime.now(timezone.utc).isoformat(timespec="seconds")}
    out["A_view_interval"] = calc_A(S["SPY"][0], S["SPY"][2]); log("A", **{k: v["loss_pct"] for k, v in out["A_view_interval"]["by_interval"].items()})
    out["B_bear20"] = calc_B(S["^GSPC"][0], S["^GSPC"][1]); log("B", events=len(out["B_bear20"]["events"]), sell_wins=out["B_bear20"]["sell_wins"], hold_wins=out["B_bear20"]["hold_wins"])
    out["C_dividend_etf"] = calc_C(S); log("C", windows=len(out["C_dividend_etf"]["windows"]))
    out["D_sox_half"] = calc_D(S["^SOX"][0], S["^SOX"][1]); log("D", events=len(out["D_sox_half"]["events"]), now=out["D_sox_half"]["now"])
    out["F_ndx30"] = {"price": calc_F(S["^NDX"][0], S["^NDX"][1], "^NDX 가격"), "total_return": calc_F(S["QQQ"][0], S["QQQ"][2], "QQQ 수정 종가 (배당 포함)")}
    log("F", price=[(e["peak"], e["years"], e["months"]) for e in out["F_ndx30"]["price"]["events"]], tr=[(e["peak"], e["years"]) for e in out["F_ndx30"]["total_return"]["events"]], now=out["F_ndx30"]["price"]["now_from_peak_pct"])
    # E: 멈춤 판단은 ^GSPC 가격(고점 대비), 사고파는 값은 SPY 수정 종가 → 두 자료의 날짜를 맞춤
    gd, gc, _ = S["^GSPC"]; sd, _, sa = S["SPY"]
    idx = np.searchsorted(gd, sd); idx = np.clip(idx, 0, len(gd) - 1)
    out["E_dca_pause"] = calc_E(sd, gc[idx], sa)
    out["E5_dca_pause_short"] = calc_E5(gd, gc, sd, sa); log("E5", **{k: f"{v['keep_return_pct']}/{v['pause_return_pct']}" for k, v in out["E5_dca_pause_short"].items()}); log("E", **{k: v["pause_vs_keep_pct"] for k, v in out["E_dca_pause"]["starts"].items()})
    (HERE / "result.json").write_text(json.dumps(out, ensure_ascii=False, indent=1, default=str), encoding="utf-8")
    log("DONE", out=str((HERE / "result.json").relative_to(HERE.parents[2])), seconds=round(time.time() - t0, 1))

if __name__ == "__main__":
    main()
