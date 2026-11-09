#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-11-09 — 고변동성 종목 100% → 폭락 → 약반등 상황에서 원금 복구 방법 시험 (사용자 지시 2026-11-09
#          "고변동성 종목에 주식 투자금 100%로 넣었는데 폭락 후 약반등한 상황에서 원금 복구 할 수 있는 가장 좋은 방법이 뭔지 테스트해봐 그리고 결론 알려줘").
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.0 | 2026-11-09 | 최초 (같은 날 고침: B 를 사건에 저장 · '지금보다 나빠짐' = 기간 끝 < D 다음 날 계좌 · 시기별 4묶음 · 절반 나스닥 100 더함) | events · paths · judge · main |
#
# 상황 (판단은 그날 종가까지의 자료만):
#   산 값 B = 그 종목의 252거래일 최고 종가 (꼭대기 근처에서 100% 매수했다고 가정) · 폭락 = 종가가 B 의 50% 이하
#   → 약반등 = 그 뒤 '지금까지의 최저 종가'보다 15% 넘게 오른 첫날 D (그날도 B 의 65% 이하여야 — 아직 깊이 물린 상태).
#   고변동성 = B 날까지 252거래일 일간 수익률의 연 변동성 40% 이상. 한 종목에서 다음 사건은 앞 D 뒤 252거래일 넘게 지나서.
# 방법 (D 종가에 판단 → D 다음 거래일 종가에 매매 · 계좌 처음 = 1 = 원금):
#   hold 그대로 보유 · spy 모두 팔아 S&P 500(SPY 배당 포함) · qqq 모두 팔아 나스닥 100(QQQ) · half 절반만 SPY 로
#   cash 모두 팔아 현금(^IRX 13주 국채) · lev2 모두 팔아 나스닥 100 2배(QQQ 하루 수익 × 2 − 단기 금리 − 연 0.95% 보수, 계산으로 재현)
#   swing  보유하다가 산 값의 80%(= 원금 −20%)까지 오르면 절반을 SPY 로 (복구 전 위험 줄이기)
# 판정 (1·3·5년): 그 기간 안에 계좌가 원금(1)을 되찾았나 · 기간 끝 계좌 · 더 잃은 폭(D 다음 날 계좌 대비 가장 낮은 값).
# 한계: 지금 Yahoo 에 남아 있는 종목만 (상장 폐지·파산 종목은 빠짐 → 보유가 실제보다 좋아 보임 = 생존 편향) · 사건이 같은 해에 몰림.
# 출력: recovery_test_<날짜>.json · recovery_test.md. ※ 연구·교육용 — 투자 권유 아님. 세금·수수료(레버리지 보수 말고)·환율 없음.
from __future__ import annotations

import json
import logging
import sys
import time
from datetime import date, datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

VERSION = "v1.0"
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
DATA = HERE / "data"
IRX_CSV = ROOT / "stock/source/timing-test-2026-10/calc/irx_daily.csv"
STOCKS = ["AAPL", "AI", "AMZN", "BBWI", "DOCU", "ILMN", "IONQ", "KSS", "LCID", "META", "MRNA", "MSTR", "NFLX", "NVDA", "PTON", "PYPL", "SHOP", "SMCI",
          "TSLA", "UPST", "URBN", "WBD", "ZM", "CSCO", "INTC", "QCOM", "ORCL", "MSFT", "EBAY", "AMD", "MU", "C", "BAC", "AIG", "F", "GE", "ROKU", "SNAP",
          "PLTR", "COIN", "RIVN", "NIO", "XYZ", "TWLO", "NET", "CRWD", "DKNG", "AFRM", "HOOD", "SOFI", "MARA", "RIOT", "ENPH", "PLUG", "BYND", "GME", "AMC",
          "CVNA", "TDOC", "FSLY", "OKTA", "ETSY", "W", "PINS", "U", "SNOW", "CHWY", "BABA", "JD"]
LEV = ["SOXL", "TQQQ", "TNA", "QLD", "ARKK"]
CRASH, REB, DEEP, VOL_MIN, GAP = 0.50, 0.15, 0.65, 0.40, 252
H_YEARS = (1, 3, 5)
METHODS = ["hold", "swing", "half", "half_qqq", "half_swing", "spy", "qqq", "lev2", "cash"]
LABEL = {"hold": "그대로 보유", "swing": "보유 → 원금 −20%까지 오르면 절반 S&P 500", "half": "절반만 S&P 500 으로", "half_qqq": "절반만 나스닥 100 으로", "half_swing": "지금 절반 S&P 500 → 원금 −20%까지 오르면 나머지도 S&P 500", "spy": "모두 S&P 500 으로",
         "qqq": "모두 나스닥 100 으로", "lev2": "모두 나스닥 100 2배로", "cash": "모두 현금(국채 이자)"}

logging.basicConfig(level=logging.INFO, format="%(message)s", stream=sys.stdout)
def log(stage: str, **kv) -> None:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    logging.info(f"[{stage}] [{ts}] " + " ".join(f"{k}={v}" for k, v in kv.items()))


def read(sym: str) -> pd.Series | None:
    p = DATA / f"{sym}.csv"
    if not p.exists():
        log("WARN", stage="data", sym=sym, issue="파일 없음", next="precheck.fetch(sym)")
        return None
    try:
        s = pd.read_csv(p, comment="#", parse_dates=["date"]).set_index("date")["adjclose"].astype(float)
    except Exception as e:  # noqa: BLE001
        log("FAIL", stage="data", sym=sym, err=repr(e)); return None
    s = s[~s.index.duplicated(keep="last")]
    bad = int((s <= 0).sum() + s.isna().sum())
    if bad:
        log("WARN", stage="data", sym=sym, bad_rows=bad, issue="0 이하·빈 값 → 뺌"); s = s[(s > 0) & s.notna()]
    return s


def events(sym: str, s: pd.Series) -> list[dict]:
    P, I = s.values, s.index
    r = np.diff(np.log(P), prepend=np.nan)
    out, i, last_d = [], 252, -10 ** 9
    while i < len(P):
        lo, hi_i = i - 251, int(np.argmax(P[i - 251:i + 1])) + i - 251
        B = P[hi_i]
        if P[i] <= CRASH * B and i - last_d > GAP:
            vol = float(np.nanstd(r[max(1, hi_i - 251):hi_i + 1]) * np.sqrt(252))
            low = P[i]; j = i
            while j < len(P) - 1:
                j += 1
                low = min(low, P[j])
                if P[j] >= (1 + REB) * low and P[j] <= DEEP * B:
                    break
                if P[j] > DEEP * B:          # 깊이 물린 채 약반등한 날 없이 올라옴 → 이 사건 아님
                    j = None; break
            else:
                j = None
            if j is not None and j < len(P) - 2:
                if vol >= VOL_MIN:
                    out.append({"sym": sym, "B": float(B), "buy_date": I[hi_i].strftime("%Y-%m-%d"), "crash_date": I[i].strftime("%Y-%m-%d"), "decide": j,
                                "decide_date": I[j].strftime("%Y-%m-%d"), "value_at_decide": round(P[j] / B, 3), "low_before": round(low / B, 3), "vol": round(vol, 2)})
                else:
                    log("SKIP", sym=sym, decide=I[j].date(), reason=f"변동성 {vol:.0%} < {VOL_MIN:.0%}")
                last_d = j; i = j + 1; continue
        i += 1
    return out


def paths(ev: dict, s: pd.Series, spy: pd.Series, qqq: pd.Series, irx: pd.Series) -> dict:
    """D 다음 날부터 방법별 계좌 (원금 = 1)."""
    I = s.index; d1 = ev["decide"] + 1
    idx = I[d1:]
    P = s.values[d1:]; B = ev["B"]
    v0 = P[0] / B
    sp = spy.reindex(idx).ffill().values; qq = qqq.reindex(idx).ffill().values; cr = irx.reindex(idx).ffill().fillna(0).values / 100 / 252
    ok = ~np.isnan(sp) & ~np.isnan(qq)
    if not ok[0]:
        return {}
    qr = np.r_[0.0, qq[1:] / qq[:-1] - 1]
    lev = np.cumprod(1 + np.r_[0.0, (2 * qr[1:] - cr[1:] - 0.0095 / 252)])
    hold = P / B
    out = {"hold": hold, "spy": v0 * sp / sp[0], "qqq": v0 * qq / qq[0], "half": 0.5 * hold + 0.5 * v0 * sp / sp[0], "half_qqq": 0.5 * hold + 0.5 * v0 * qq / qq[0],
           "cash": v0 * np.cumprod(1 + np.r_[0.0, cr[1:]]), "lev2": v0 * np.maximum(lev, 0)}
    # swing: 보유하다 계좌 0.8 이상이 된 다음 날 절반을 SPY 로
    sw = hold.copy(); k = np.argmax(hold >= 0.8) if (hold >= 0.8).any() else None
    if k is not None and k + 1 < len(hold):
        k += 1; base = hold[k]
        sw[k:] = 0.5 * hold[k:] + 0.5 * base * sp[k:] / sp[k]
    out["swing"] = sw
    # half_swing: 지금 절반 SPY · 계좌가 0.8 이상이 된 다음 날 남은 종목도 모두 SPY
    hs = 0.5 * hold + 0.5 * v0 * sp / sp[0]
    k2 = int(np.argmax(hs >= 0.8)) if (hs >= 0.8).any() else None
    if k2 is not None and k2 + 1 < len(hs):
        k2 += 1; base2 = hs[k2]
        hs = hs.copy(); hs[k2:] = base2 * sp[k2:] / sp[k2]
    out["half_swing"] = hs
    return {m: (idx, v) for m, v in out.items()}


def judge(idx, v, years: int) -> dict | None:
    n = 252 * years
    if len(v) <= n:
        return None
    w = v[:n + 1]
    rec = int(np.argmax(w >= 1.0)) if (w >= 1.0).any() else None
    return {"recovered": rec is not None, "days_to_recover": rec, "end": float(w[-1]), "start": float(w[0]), "min": float(w.min()), "further": float(w.min() / w[0] - 1)}


def main() -> None:
    t0 = time.perf_counter()
    spy, qqq = read("SPY"), read("QQQ")
    irx = pd.read_csv(IRX_CSV, comment="#", parse_dates=["date"]).set_index("date")["close"].astype(float)
    log("DATA", spy=f"{spy.index[0].date()}~{spy.index[-1].date()}", qqq=f"{qqq.index[0].date()}~{qqq.index[-1].date()}", irx_last=irx.index[-1].date())
    E, missing = [], []
    for grp, syms in (("stock", STOCKS), ("lev", LEV)):
        for sym in syms:
            s = read(sym)
            if s is None:
                missing.append(sym); continue
            for ev in events(sym, s):
                ev["group"] = grp
                ev["paths"] = paths(ev, s, spy, qqq, irx)
                if ev["paths"]:
                    E.append(ev)
    log("EVENTS", n=len(E), stocks=len({e["sym"] for e in E if e["group"] == "stock"}), lev=len([e for e in E if e["group"] == "lev"]), missing=",".join(missing) or "-")
    for e in E:
        log("EVENT", sym=e["sym"], group=e["group"], buy=e["buy_date"], decide=e["decide_date"], value=e["value_at_decide"], vol=e["vol"])
    res = {"version": VERSION, "made": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
           "rules": {"crash": CRASH, "rebound": REB, "deep": DEEP, "vol_min": VOL_MIN, "gap_days": GAP, "lev2": "2×QQQ 하루 − IRX − 0.95%/년", "swing": "계좌 0.8 되면 절반 SPY"},
           "missing": missing, "labels": LABEL, "summary": {}, "events": []}
    for grp in ("stock", "lev", "all"):
        G = [e for e in E if grp == "all" or e["group"] == grp]
        res["summary"][grp] = {}
        for h in H_YEARS:
            row = {}
            for m in METHODS:
                J = [judge(*e["paths"][m], h) for e in G]; J = [j for j in J if j]
                if not J:
                    continue
                ends = np.array([j["end"] for j in J]); fur = np.array([j["further"] for j in J])
                rec_days = [j["days_to_recover"] for j in J if j["recovered"]]
                row[m] = {"n": len(J), "recovered": int(sum(j["recovered"] for j in J)), "recovered_pct": round(100 * np.mean([j["recovered"] for j in J]), 1),
                          "end_median": round(float(np.median(ends)), 3), "end_p25": round(float(np.percentile(ends, 25)), 3), "end_worst": round(float(ends.min()), 3),
                          "end_best": round(float(ends.max()), 3), "further_median_pct": round(float(np.median(fur)) * 100, 1),
                          "further_worst_pct": round(float(fur.min()) * 100, 1), "further_over30": int((fur < -0.30).sum()),
                          "recover_years_median": round(float(np.median(rec_days)) / 252, 1) if rec_days else None,
                          "end_below_start": int(sum(1 for j in J if j["end"] < j["start"]))}
                log("SUMMARY", group=grp, years=h, method=m, **{k: v for k, v in row[m].items()})
            res["summary"][grp][f"{h}y"] = row
    for e in E:
        rec = {k: v for k, v in e.items() if k not in ("paths", "decide", "B")}
        for h in H_YEARS:
            for m in ("hold", "spy", "lev2", "swing"):
                j = judge(*e["paths"][m], h)
                rec[f"{m}_{h}y"] = None if j is None else {"rec": j["recovered"], "end": round(j["end"], 3)}
        res["events"].append(rec)
    # 시기별 (생존 편향·몰림 확인)
    era = {}
    for e in E:
        y = int(e["decide_date"][:4]); k = "2000~2002" if y <= 2002 else "2003~2009" if y < 2010 else "2010~2019" if y < 2020 else "2020~"
        for m in METHODS:
            j = judge(*e["paths"][m], 3)
            if j:
                era.setdefault(k, {}).setdefault(m, []).append(j)
    res["era_3y"] = {k: {m: {"n": len(J), "recovered_pct": round(100 * np.mean([j["recovered"] for j in J]), 1), "end_median": round(float(np.median([j["end"] for j in J])), 3),
                             "end_below_start": int(sum(1 for j in J if j["end"] < j["start"]))} for m, J in v.items()} for k, v in era.items()}
    for k, v in res["era_3y"].items():
        log("ERA", era=k, **{m: f"n{x['n']}·rec{x['recovered_pct']}%·med{x['end_median']}·worse{x['end_below_start']}" for m, x in v.items()})
    out = HERE / f"recovery_test_{date.today().isoformat()}.json"
    out.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    log("DONE", out=out.relative_to(ROOT), sec=round(time.perf_counter() - t0, 2))


if __name__ == "__main__":
    main()
