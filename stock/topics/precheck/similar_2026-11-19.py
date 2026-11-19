#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-11-19 — 지금(2026-06 고점 → 11-19)과 가장 비슷한 과거 시기 찾기 (사용자 지시 "지금 상황이랑 가장 비슷한 시기는 언제고 어떻게 비슷한지 얘기해봐").
#   규칙(계산 전에 정함):
#   · 후보 = 큰 하락(고점 대비 −40% 안팎) 앞의 고점들 — 코스피·삼성전자·SK하이닉스·필라델피아 반도체(^SOX)·나스닥100(^NDX)·닛케이(^N225)·대만(^TWII)·카카오·에코프로.
#     고점 = 정한 기간 안의 가장 높은 종가. 지금 = 2026-06 고점 (코스피 6-22 · 삼성전자 6-18 · 하이닉스 6-22).
#   · 값 = 종가(가격 · 배당 뺌 — 지수·종목 모두 같은 조건). 하이닉스 2000 은 Yahoo 배당 반영 값이 깨져 있어 종가가 유일.
#   · 닮은 정도 1 — 모양: 고점 365일 전 → 고점 150일 뒤(지금 = 6-22 뒤 150일)를 5일 간격으로, log(값 ÷ 고점) 의 차이 제곱 평균의 제곱근(RMSE) · 작을수록 닮음.
#     오르막(−365~0)·내리막(0~+150) RMSE 도 따로.
#   · 닮은 정도 2 — 숫자: 고점 전 1년·6개월 오른 폭 · 2년 안 바닥 → 고점 오른 폭 · 고점 뒤 −40% 까지 걸린 날 · 고점 150일 뒤 값.
#   · 그 뒤 = '고점 150일 뒤'(지금과 같은 때)에 있던 사람이 본 것: 그 뒤 3년 안 더 빠진 폭 · 1·3·5년 뒤 값(그때 대비) · 고점 되찾기까지 해.
#   · 같은 때 미국 쪽(반도체 지수·나스닥100·S&P 500) 2026 고점 대비 지금 (`context_2026`)
#   로그: [STAGE] [시각] key=value · 실행: python3 stock/topics/precheck/similar_2026-11-19.py
#   ※ 연구·교육용 — 투자 권유가 아님. 과거가 앞날을 보장하지 않음. 닮은 정도는 가격 모양만 본 것 — 까닭(경제·업종)은 숫자가 말해 주지 않음.
import importlib.util
import json
import logging
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location("c", ROOT / "stock/topics/titles_2026-11-18/calc.py")
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)
logging.basicConfig(level=logging.INFO, format="%(message)s")
LOG = logging.getLogger("similar")
DAYS_AFTER = 150                      # 2026-06-22 → 2026-11-19
OFFS = np.arange(-365, DAYS_AFTER + 1, 5)

# (기호, 이름, 고점 찾을 기간 시작, 끝, 자료 시작)
CANDS = [
    ("^KS11", "코스피", "1999-06-01", "2000-06-30", "1996-12-01"),
    ("^KS11", "코스피", "2007-01-01", "2008-06-30", "1996-12-01"),
    ("^KS11", "코스피", "2010-06-01", "2011-12-31", "1996-12-01"),
    ("^KS11", "코스피", "2017-06-01", "2018-12-31", "1996-12-01"),
    ("^KS11", "코스피", "2021-01-01", "2021-12-31", "1996-12-01"),
    ("005930.KS", "삼성전자", "2000-01-01", "2000-12-31", "2000-01-01"),
    ("005930.KS", "삼성전자", "2007-06-01", "2008-08-31", "2000-01-01"),
    ("005930.KS", "삼성전자", "2020-12-01", "2021-06-30", "2000-01-01"),
    ("005930.KS", "삼성전자", "2024-01-01", "2024-12-31", "2000-01-01"),
    ("000660.KS", "SK하이닉스", "2000-01-01", "2000-06-30", "2000-01-01"),
    ("000660.KS", "SK하이닉스", "2007-01-01", "2007-12-31", "2000-01-01"),
    ("000660.KS", "SK하이닉스", "2010-06-01", "2011-12-31", "2000-01-01"),
    ("000660.KS", "SK하이닉스", "2014-01-01", "2015-06-30", "2000-01-01"),
    ("000660.KS", "SK하이닉스", "2020-12-01", "2021-12-31", "2000-01-01"),
    ("000660.KS", "SK하이닉스", "2024-01-01", "2024-12-31", "2000-01-01"),
    ("^SOX", "미국 반도체 지수", "1999-06-01", "2000-12-31", "1994-01-01"),
    ("^SOX", "미국 반도체 지수", "2021-06-01", "2022-06-30", "1994-01-01"),
    ("^SOX", "미국 반도체 지수", "2024-01-01", "2024-12-31", "1994-01-01"),
    ("^NDX", "나스닥100", "1999-06-01", "2000-12-31", "1985-10-01"),
    ("^NDX", "나스닥100", "2021-06-01", "2022-06-30", "1985-10-01"),
    ("^N225", "닛케이225", "1989-01-01", "1990-06-30", "1965-01-01"),
    ("^TWII", "대만 가권", "1989-06-01", "1990-12-31", "1987-01-01"),
    ("^TWII", "대만 가권", "1997-01-01", "1997-12-31", "1987-01-01"),
    ("^TWII", "대만 가권", "1999-06-01", "2000-12-31", "1987-01-01"),
    ("035720.KS", "카카오", "2021-01-01", "2021-12-31", "2010-01-01"),
    ("086520.KQ", "에코프로", "2023-01-01", "2023-12-31", "2015-01-01"),
]
NOW = [("^KS11", "코스피", "1996-12-01"), ("005930.KS", "삼성전자", "2000-01-01"), ("000660.KS", "SK하이닉스", "2000-01-01")]


def log(stage, **kv):
    LOG.info("[%s] [%s] %s", stage, datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), " ".join(f"{k}={v}" for k, v in kv.items()))


_cache = {}


def series(sym, start):
    if sym not in _cache:
        st = date.fromisoformat(start)
        try:
            d, cl, _ = c.fetch(sym, start=st)
            if (d[0] - st).days > 400 and sym not in ("^TWII",):
                log("REFETCH", symbol=sym, cached_first=d[0], want=st)
                d, cl, _ = c.fetch(sym, start=st, refetch=True)
        except SystemExit as e:                                  # 받기 실패 — 그 후보만 빼고 계속
            log("WARN", symbol=sym, error=str(e)[:120], next="그 후보는 뺌")
            _cache[sym] = None
            return None
        _cache[sym] = (np.asarray(d), np.asarray(cl, dtype=float))
    return _cache[sym]


def at(d, px, day):
    return float(px[max(0, int(np.searchsorted(d, day, side="right")) - 1)])


def features(d, px, ip):
    pk_d, pk = d[ip], px[ip]
    f = {"peak": str(pk_d)}
    for k, days in (("run_1y_pct", 365), ("run_6m_pct", 182)):
        f[k] = round((pk / at(d, px, pk_d - timedelta(days=days)) - 1) * 100, 1) if pk_d - timedelta(days=days) >= d[0] else None
    lo_i = int(np.searchsorted(d, pk_d - timedelta(days=730)))
    if pk_d - timedelta(days=730) >= d[0]:
        j = lo_i + int(np.argmin(px[lo_i:ip + 1]))
        f["run_from_2y_low_pct"] = round((pk / px[j] - 1) * 100, 1)
        f["low_to_peak_days"] = int((pk_d - d[j]).days)
    else:
        f["run_from_2y_low_pct"], f["low_to_peak_days"] = None, None
    hit = np.flatnonzero(px[ip:] <= pk * 0.6)
    f["days_to_minus40"] = int((d[ip + hit[0]] - pk_d).days) if len(hit) else None
    t150 = pk_d + timedelta(days=DAYS_AFTER)
    if t150 > d[-1]:
        f["at_150d_pct"] = None
        return f
    v150 = at(d, px, t150)
    i150 = max(0, int(np.searchsorted(d, t150, side="right")) - 1)
    f["at_150d_pct"] = round((v150 / pk - 1) * 100, 1)
    f["low_within_150d_pct"] = round((px[ip:i150 + 1].min() / pk - 1) * 100, 1)
    # 그 뒤 — 고점 150일 뒤에 있던 사람
    j3 = int(np.searchsorted(d, t150 + timedelta(days=3 * 365)))
    f["after_further_drop_3y_pct"] = round((px[i150:min(j3, len(px) - 1) + 1].min() / v150 - 1) * 100, 1)
    for yrs in (1, 3, 5):
        t = t150 + timedelta(days=int(yrs * 365.25))
        f[f"after_{yrs}y_pct"] = round((at(d, px, t) / v150 - 1) * 100, 1) if t <= d[-1] else None
    back = np.flatnonzero(px[i150:] >= pk)
    f["years_150d_to_peak"] = round((d[i150 + back[0]] - t150).days / 365.25, 1) if len(back) else None
    f["peak_regained"] = str(d[i150 + back[0]]) if len(back) else None
    return f


def path(d, px, ip):
    pk_d, pk = d[ip], px[ip]
    if pk_d - timedelta(days=365) < d[0] or pk_d + timedelta(days=DAYS_AFTER) > d[-1] + timedelta(days=3):
        return None
    return np.array([np.log(at(d, px, pk_d + timedelta(days=int(k))) / pk) for k in OFFS])


def rmse(a, b, mask=None):
    m = np.ones(len(a), bool) if mask is None else mask
    return round(float(np.sqrt(np.mean((a[m] - b[m]) ** 2))), 3)


def main():
    out = {"rule": "종가(배당 뺌) · 모양 = 고점 −365일~+150일 log(값/고점) RMSE (5일 간격) · 그 뒤 = 고점 150일 뒤에 있던 사람 기준", "now": {}, "cands": []}
    now_paths = {}
    for sym, name, st in NOW:
        s = series(sym, st)
        d, px = s
        ip = int(np.argmax(px))
        f = features(d, px, ip)
        f["now_pct"] = round((px[-1] / px[ip] - 1) * 100, 1)
        f["last"] = str(d[-1])
        out["now"][name] = f
        now_paths[name] = np.array([np.log(at(d, px, d[ip] + timedelta(days=int(k))) / px[ip]) if d[ip] + timedelta(days=int(k)) <= d[-1] else np.nan for k in OFFS])
        log("NOW", name=name, **{k: v for k, v in f.items() if k in ("peak", "run_1y_pct", "run_6m_pct", "run_from_2y_low_pct", "days_to_minus40", "now_pct")})
    pre, post = OFFS <= 0, OFFS >= 0
    for sym, name, a, b, st in CANDS:
        s = series(sym, st)
        if s is None:
            continue
        d, px = s
        lo, hi = np.searchsorted(d, date.fromisoformat(a)), np.searchsorted(d, date.fromisoformat(b), side="right")
        if hi <= lo:
            log("WARN", symbol=sym, window=f"{a}~{b}", note="자료 없음 — 뺌")
            continue
        ip = lo + int(np.argmax(px[lo:hi]))
        f = features(d, px, ip)
        f.update({"symbol": sym, "name": name, "data_first": str(d[0])})
        p = path(d, px, ip)
        f["rmse"] = {}
        if p is not None:
            for nm, q in now_paths.items():
                ok = np.isfinite(q)
                f["rmse"][nm] = {"all": rmse(p, q, ok), "up": rmse(p, q, ok & pre), "down": rmse(p, q, ok & post)}
        out["cands"].append(f)
        log("CAND", name=name, peak=f["peak"], run_1y=f["run_1y_pct"], run_2y_low=f["run_from_2y_low_pct"], d40=f["days_to_minus40"],
            at150=f.get("at_150d_pct"), rmse_kospi=f["rmse"].get("코스피", {}).get("all"))
    out["context_2026"] = {}                                         # 같은 때 미국 쪽 (이번 하락이 한국·반도체만인지)
    for sym, name, st in (("^SOX", "미국 반도체 지수", "1994-01-01"), ("^NDX", "나스닥100", "1985-10-01"), ("^GSPC", "S&P 500", "1950-01-01")):
        sres = series(sym, st)
        if sres is None:
            continue
        d, px = sres
        lo = int(np.searchsorted(d, date(2026, 1, 1)))
        ip = lo + int(np.argmax(px[lo:]))
        out["context_2026"][name] = {"peak_2026": str(d[ip]), "now_pct": round((px[-1] / px[ip] - 1) * 100, 1), "last": str(d[-1]),
                                    "run_1y_pct": round((px[ip] / at(d, px, d[ip] - timedelta(days=365)) - 1) * 100, 1)}
    log("CONTEXT", **{k: v for k, v in out["context_2026"].items()})
    out["rank"] = {nm: sorted(([f["rmse"][nm]["all"], f["name"], f["peak"]] for f in out["cands"] if nm in f["rmse"]))[:6] for nm in now_paths}
    for nm, r in out["rank"].items():
        log("RANK", now=nm, top=r[:4])
    p = Path(__file__).with_suffix(".json")
    p.write_text(json.dumps(out, ensure_ascii=False, indent=1), "utf-8")
    log("DONE", out=p)


if __name__ == "__main__":
    main()
