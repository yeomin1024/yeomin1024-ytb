#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-11-10 — SK하이닉스는 수정 종가(adjclose) 대신 종가(close): Yahoo 수정 종가가 2000-01-04~2002-12-26 778일 동안 음수(잘못된 배당 한 건 탓) — v1.0 은 그 줄을 빼서
#   2003년부터만 셌음 → 종가(분할 반영 · 하루 최대 변동 32%)로 2000년부터. 코스피·삼성전자·SPY 숫자는 그대로.
# v1.0 — 2026-11-10 — 새 편 제목 후보 2개의 '정답 미리 확인' (사용자 지시 2026-11-10 "분석 자료 및 페르소나 활용해서 앞으로 올릴 영상 제목 2개 알려줘").
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.1 | 2026-11-10 | SK하이닉스 = close (adjclose 음수 778일) | t2_sell_then_rise |
# | v1.0 | 2026-11-10 | 최초 — T1 '같은 1억, 국장 vs 미장(원화 기준) 누가 덜 잃었나' · T2 '"내가 팔면 오른다" — 폭락 중 급락한 날 팔았다면' | load·t1_kr_vs_us·t2_sell_then_rise·main |
#
# 왜 이 둘인가 (stock/guides/persona_judge.md 2번 — 전체 댓글 92,094개):
#   T1 = '국장 vs 미장'은 어느 영상 밑에서나 나오는 말 2위(보통 영상 6.9%) · 제목 꼴 '두 사람·같은 돈' ×2.40 · '실제 데이터' ×1.91.
#   T2 = 좋아요 상위 댓글 "내가 나가는 순간 삼전하닉 ㅈㄴ 날라갈꺼라서 못나감"(👍2,916) · "내가 삼전닉스 나가면 외국인이 돌아오고 만스피 감"(👍1,403) — 물린 개미의 자조.
# 규칙 (앞날 자료를 쓰지 않음 — 판단 = 그날 종가까지 · 매매 = 다음 거래일 종가):
#   T1: 한국 투자자 두 사람이 같은 날 같은 원화를 코스피(^KS11 — 배당 없는 지수) / S&P 500(SPY 종가 × 원·달러, 배당 없는 값으로 맞춤)에 넣음.
#       폭락 = 코스피가 252거래일 최고가보다 20% 넘게 하락한 구간(최고가 날 → 가장 낮은 날). 구간마다 두 사람의 가장 크게 줄어든 폭(원화).
#       + 아무 달 첫 거래일에 넣고 12개월 동안 원금보다 20% 넘게 줄어든 적이 있는 달 수 (2004년~) · 민감도: 달러 값 그대로(환율 뺌)·배당 포함 SPY.
#   T2: '폭락 중 급락한 날' = 종가가 252거래일 최고가보다 20% 넘게 낮은 상태에서 하루 th% 넘게 하락한 날(앞 사건과 20거래일 넘게 떨어진 것만).
#       다음 거래일 종가에 매도했다고 보고, 매도가 대비 5·21·63·252거래일 뒤 값이 더 높았던 횟수 · 그 뒤 252거래일 안 가장 낮은 값(더 떨어진 폭).
#       대상 = 코스피(th 3%) · 삼성전자 · SK하이닉스(th 5%) · SPY(th 3%) · 2000년~. 민감도: th ±1%p · 최고가 대비 −10%/−30%.
# 출력: stock/topics/precheck/next_titles_2026-11-10.json. ※ 연구·교육용 — 투자 권유 아님. 세금·수수료 없음. 과거 자료이며 앞으로도 같다는 보장은 없음.
from __future__ import annotations

import json
import logging
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

VERSION = "v1.1"
HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
OUT = HERE / "next_titles_2026-11-10.json"
HORIZONS = {"1주": 5, "1달": 21, "3달": 63, "1년": 252}

logging.basicConfig(level=logging.INFO, format="%(message)s", stream=sys.stdout)


def log(stage: str, level: int = logging.INFO, **kv) -> None:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    logging.log(level, f"[{stage}] [{ts}] " + " ".join(f"{k}={v}" for k, v in kv.items()))


def load(name: str, col: str = "close") -> pd.Series:
    """일별 값 — 빈 값·중복 날짜·0 이하를 검사하고 기록."""
    path = DATA / f"{name}.csv"
    try:
        d = pd.read_csv(path, comment="#", parse_dates=["date"]).set_index("date")
    except Exception as e:  # noqa: BLE001
        log("FAIL", logging.ERROR, stage="load", file=path, err=repr(e), next="precheck.py fetch(<기호>) 로 다시 받기")
        raise SystemExit(1)
    s = d[col].astype(float)
    dup, nan, bad = int(s.index.duplicated().sum()), int(s.isna().sum()), int((s <= 0).sum())
    gap = int(s.index.to_series().diff().dt.days.max())
    jump = float(s.pct_change().abs().max())
    log("LOAD", name=name, col=col, rows=len(s), first=s.index[0].date(), last=s.index[-1].date(), dup=dup, nan=nan, nonpositive=bad, max_gap_days=gap, max_day_move=round(jump, 3))
    if dup or nan or bad:
        log("DATA", logging.WARNING, name=name, issue="중복·빈 값·0 이하", action="중복은 첫 값, 빈 값·0 이하는 뺌")
        s = s[~s.index.duplicated()].dropna()
        s = s[s > 0]
    return s


def mdd(v: np.ndarray) -> float:
    return float((v / np.maximum.accumulate(v) - 1).min())


# ---------------------------------------------------------------- T1 국장 vs 미장
def t1_kr_vs_us() -> dict:
    ks, spy, spy_adj, fx = load("_KS11"), load("SPY"), load("SPY", "adjclose"), load("KRW_X")
    idx = ks.index.intersection(spy.index).intersection(fx.index)          # 세 시장이 모두 연 날만 (환율 자료가 2003-12 부터)
    ks, us_krw, us_usd, us_adj_krw = ks[idx], (spy * fx)[idx], spy[idx], (spy_adj * fx)[idx]
    log("T1", days=len(idx), first=idx[0].date(), last=idx[-1].date(), note="코스피·SPY 모두 배당 없는 값 · SPY 는 원화로")
    # 폭락 구간 = 코스피가 252거래일 최고가보다 20% 넘게 하락 (최고가 날 → 다시 그 최고가를 되찾기 전 가장 낮은 날)
    K = ks.values
    hi = pd.Series(K).rolling(252, min_periods=1).max().values
    eps, i = [], 0
    while i < len(K):
        if K[i] / hi[i] - 1 <= -0.20:
            pk = int(np.argmax(K[max(0, i - 251):i + 1])) + max(0, i - 251)
            j = i
            while j < len(K) and K[j] < K[pk]:
                j += 1
            lo = int(np.argmin(K[pk:j])) + pk
            eps.append((pk, lo, j))
            i = j
        else:
            i += 1
    rows = []
    for pk, lo, j in eps:
        seg = slice(pk, min(j, len(K)))
        r = {"peak": idx[pk].strftime("%Y-%m-%d"), "low": idx[lo].strftime("%Y-%m-%d"), "recovered": idx[j].strftime("%Y-%m-%d") if j < len(K) else None,
             "kospi_mdd": round(mdd(K[seg]) * 100, 1), "us_krw_mdd": round(mdd(us_krw.values[seg]) * 100, 1), "us_usd_mdd": round(mdd(us_usd.values[seg]) * 100, 1),
             "us_krw_at_kospi_low": round((us_krw.values[lo] / us_krw.values[pk] - 1) * 100, 1), "fx_peak_to_low": round((fx[idx].values[lo] / fx[idx].values[pk] - 1) * 100, 1)}
        r["less_loss"] = "미장" if r["us_krw_mdd"] > r["kospi_mdd"] else "국장"
        rows.append(r)
        log("T1_EP", **r)
    # 아무 달 첫 거래일에 넣고 12개월 — 원금보다 20% 넘게 줄어든 적이 있는 달 수
    first_days = pd.Series(np.arange(len(idx)), index=idx).groupby([idx.year, idx.month]).first().values
    cnt = {"kospi": 0, "us_krw": 0, "us_usd": 0, "us_adj_krw": 0}
    n = 0
    worst = {k: 0.0 for k in cnt}
    for b in first_days:
        if b + 252 >= len(idx):
            continue
        n += 1
        for k, s in (("kospi", ks), ("us_krw", us_krw), ("us_usd", us_usd), ("us_adj_krw", us_adj_krw)):
            w = s.values[b:b + 253] / s.values[b] - 1
            cnt[k] += bool(w.min() <= -0.20)
            worst[k] = min(worst[k], float(w.min()))
    roll = {"months": n, "loss20_months": cnt, "worst_within_12m": {k: round(v * 100, 1) for k, v in worst.items()}}
    log("T1_ROLL", **{k: json.dumps(v) for k, v in roll.items()})
    whole = {"kospi_mdd": round(mdd(ks.values) * 100, 1), "us_krw_mdd": round(mdd(us_krw.values) * 100, 1), "us_usd_mdd": round(mdd(us_usd.values) * 100, 1),
             "kospi_total": round((ks.values[-1] / ks.values[0] - 1) * 100, 0), "us_krw_total": round((us_krw.values[-1] / us_krw.values[0] - 1) * 100, 0)}
    less = sum(1 for r in rows if r["less_loss"] == "미장")
    verdict = {"episodes": len(rows), "us_less_loss": less, "kospi_less_loss": len(rows) - less,
               "robust_without_fx": sum(1 for r in rows if r["us_usd_mdd"] > r["kospi_mdd"])}
    log("T1_VERDICT", **verdict, **whole)
    return {"range": [idx[0].strftime("%Y-%m-%d"), idx[-1].strftime("%Y-%m-%d")], "episodes": rows, "rolling_12m": roll, "whole": whole, "verdict": verdict}


# ---------------------------------------------------------------- T2 내가 팔면 오른다
def t2_one(name: str, s: pd.Series, th: float, dd: float = -0.20, gap: int = 20) -> dict:
    P = s.values
    hi = pd.Series(P).rolling(252, min_periods=1).max().values
    ret = np.zeros(len(P)); ret[1:] = P[1:] / P[:-1] - 1
    ev, last = [], -10 ** 9
    for t in range(252, len(P) - 1):
        if P[t] / hi[t] - 1 <= dd and ret[t] <= -th and t - last > gap:      # t 날 종가까지만 보고 판단
            ev.append(t); last = t
    res = {"n": len(ev), "th": th, "dd": dd}
    for lab, h in HORIZONS.items():
        ok = [t for t in ev if t + 1 + h < len(P)]
        up = sum(1 for t in ok if P[t + 1 + h] > P[t + 1])                 # 매도 = t+1 종가
        res[lab] = {"n": len(ok), "higher": up, "share": round(up / len(ok), 3) if ok else None,
                    "median_move": round(float(np.median([P[t + 1 + h] / P[t + 1] - 1 for t in ok])) * 100, 1) if ok else None}
    ok = [t for t in ev if t + 1 + 252 < len(P)]
    more = [float(P[t + 1:t + 2 + 252].min() / P[t + 1] - 1) for t in ok]
    res["more_drop_within_1y"] = {"n": len(ok), "median": round(float(np.median(more)) * 100, 1) if ok else None, "worst": round(min(more) * 100, 1) if ok else None,
                                  "fell_20_more": sum(1 for m in more if m <= -0.20)}
    res["events"] = [s.index[t].strftime("%Y-%m-%d") for t in ev]
    log("T2", name=name, th=round(th, 2), dd=dd, n=res["n"], **{k: f"{v['higher']}/{v['n']}" for k, v in res.items() if isinstance(v, dict) and "higher" in v},
        more_drop_median=res["more_drop_within_1y"]["median"], more_drop_worst=res["more_drop_within_1y"]["worst"], fell_20_more=res["more_drop_within_1y"]["fell_20_more"])
    return res


def t2_sell_then_rise() -> dict:
    series = {"코스피": (load("_KS11"), 0.03), "삼성전자": (load("005930.KS", "adjclose"), 0.05), "SK하이닉스": (load("000660.KS", "close"), 0.05), "SPY": (load("SPY", "adjclose"), 0.03)}
    out = {}
    for name, (s, th) in series.items():
        s = s["2000":]
        out[name] = {"main": t2_one(name, s, th),
                     "sens": {f"th{round((th + d) * 100)}_dd{int(-dd * 100)}": {k: v for k, v in t2_one(name, s, th + d, dd).items() if k != "events"}
                              for d in (-0.01, 0.01) for dd in (-0.10, -0.20, -0.30)}}
    # 기준선 — 아무 날 팔았을 때 1년 뒤 더 높았던 몫 (같은 기간) : '폭락한 날 팔면 유난히 오르나'를 보려면 이것과 견줘야 함
    base = {}
    for name, (s, _) in series.items():
        P = s["2000":].values
        base[name] = {lab: round(float(np.mean(P[h + 1:] > P[1:-h])), 3) for lab, h in HORIZONS.items()}
    log("T2_BASE", **{k: json.dumps(v, ensure_ascii=False) for k, v in base.items()})
    return {"by": out, "baseline_any_day": base}


def selftest() -> None:
    assert abs(mdd(np.array([100, 120, 60, 90])) + 0.5) < 1e-9
    s = pd.Series([100.0] * 252 + [70.0, 66.0, 60.0, 80.0] + [80.0] * 300, index=pd.bdate_range("2001-01-01", periods=556))
    r = t2_one("fake", s, 0.05, dd=-0.20, gap=20)
    # 252번째 날 −30% (최고가보다 30% 아래 · 하루 −5% 넘게) = 사건 1개 · 253·254번째 날 급락은 20거래일 안이라 뺌 · 매도 = 253번째 날 종가 66 → 5거래일 뒤 80 (더 높음)
    assert r["n"] == 1 and r["events"][0] == s.index[252].strftime("%Y-%m-%d"), r
    assert r["1주"] == {"n": 1, "higher": 1, "share": 1.0, "median_move": 21.2}, r["1주"]
    assert r["more_drop_within_1y"]["worst"] == -9.1, r["more_drop_within_1y"]                # 66 → 60
    print("[SELFTEST] ok")


def main() -> None:
    t0 = time.time()
    if "--selftest" in sys.argv:
        try:
            selftest()
        except AssertionError as e:
            print("[SELFTEST] FAIL", e); raise SystemExit(1)
        return
    out = {"version": VERSION, "made": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "t1": t1_kr_vs_us(), "t2": t2_sell_then_rise()}
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    log("DONE", out=OUT.relative_to(HERE.parents[2]), sec=round(time.time() - t0, 2))


if __name__ == "__main__":
    main()
