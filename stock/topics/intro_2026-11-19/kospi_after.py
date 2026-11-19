#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.2 — 2026-11-19 — 도입 검토 1회차(review/answers_r1) 반영: 사건마다 코스피 '고점 전 2년 바닥 → 고점' 몇 배 (`kospi_runup_x` — 귀로 듣기 쉬운 배수) · 고점 날짜.
# (v1.1 — 2026-11-19 — 고점 = **최근 2년(504거래일) 안 가장 높은 종가** (v1.0 은 자료 첫날부터의 고점이라 하이닉스가 2000년 고점을 2025년까지 못 넘어
#          2001~2025년 내내 '−40% 아래'로 잡혀 사실상 삼성전자 하나로 사건을 셈 — 2008 하닉 −98.5% 같은 값). 코스피 고점·되찾기도 같은 2년 고점.
# (v1.0 — 2026-11-19 — 제목 「삼성전자, 하이닉스 폭락 후 코스피 주가 이걸 보면 전망이 보일 겁니다」(사용자 제목) 의 숫자 — 도입 후보에 쓸 것만.
#   규칙(계산 전에 정함):
#   · '삼전·하닉 폭락' = 두 종목이 **모두** 직전 고점 대비 −40% 아래에 있는 첫날 (한 번 시작하면 둘 중 하나가 고점의 80% 위로 올라올 때까지 같은 사건).
#     값 = 종가(가격 · 배당 뺌 — 하이닉스 2003년 전 배당 반영 값이 깨져 있어 셋 다 같은 조건). 자료: 삼전·하닉 2000-01 · 코스피 1996-12 부터.
#   · 그날 코스피가 자기 고점 대비 어디였나 · 그날부터 코스피 1·3·5년 뒤 · 3년 안 더 빠진 폭 · 코스피 고점 되찾기까지.
#   · 같은 꼴로 '한 종목만 −40%' 날도 (참고).
#   · 지금 = 2026 사건 — 코스피가 이미 얼마나 따라 빠졌나.
#   로그: [STAGE] [시각] key=value · 실행: python3 stock/topics/intro_2026-11-19/kospi_after.py
#   ※ 연구·교육용 — 투자 권유가 아님. 과거가 앞날을 보장하지 않음. 사건 수가 적음.
import importlib.util
import json
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pandas as pd
WIN = 504                                                              # 최근 2년 ≈ 504거래일

ROOT = Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location("c", ROOT / "stock/topics/titles_2026-11-18/calc.py")
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)
log = c.log


def load(sym, st):
    d, cl, _ = c.fetch(sym, start=st)
    return np.asarray(d), np.asarray(cl, dtype=float)


def at(d, px, day):
    return float(px[max(0, int(np.searchsorted(d, day, side="right")) - 1)])


def main():
    sd, sp = load("005930.KS", date(2000, 1, 1))
    hd, hp = load("000660.KS", date(2000, 1, 1))
    kd, kp = load("^KS11", date(1996, 12, 1))
    days = sorted(set(sd) & set(hd) & set(kd))
    S = np.array([at(sd, sp, x) for x in days]); H = np.array([at(hd, hp, x) for x in days]); K = np.array([at(kd, kp, x) for x in days])
    D = np.array(days)
    Srun = pd.Series(S).rolling(WIN, min_periods=1).max().to_numpy()
    Hrun = pd.Series(H).rolling(WIN, min_periods=1).max().to_numpy()
    Kfull_run = pd.Series(kp).rolling(WIN, min_periods=1).max().to_numpy()
    sdd, hdd = S / Srun - 1, H / Hrun - 1
    warm = 60                                                          # 자료 시작 60거래일 뒤부터 (그 전 고점을 모름)
    out = {"rule": "고점 = 최근 2년 안 가장 높은 종가 · 삼전·하닉 둘 다 그 고점 대비 −40% 아래인 첫날 (둘 중 하나가 고점 80% 위로 오르면 사건 끝) · 종가 · 코스피 그날부터", "both": [], "now": {}}
    i, n = warm, len(D)
    while i < n:
        if sdd[i] <= -0.4 and hdd[i] <= -0.4:
            day = D[i]
            kpk = at(kd, Kfull_run, day)
            k0 = at(kd, kp, day)
            ev = {"day": str(day), "samsung_dd_pct": round(sdd[i] * 100, 1), "hynix_dd_pct": round(hdd[i] * 100, 1), "kospi_dd_pct": round((k0 / kpk - 1) * 100, 1)}
            jk = int(np.searchsorted(kd, day, side="right")) - 1
            jp = max(0, jk - WIN + 1) + int(np.argmax(kp[max(0, jk - WIN + 1):jk + 1]))          # 그날까지 2년 안 코스피 고점
            jl = max(0, jp - WIN + 1) + int(np.argmin(kp[max(0, jp - WIN + 1):jp + 1]))          # 그 고점 전 2년 안 바닥
            ev.update({"kospi_peak_day": str(kd[jp]), "kospi_runup_x": round(float(kp[jp] / kp[jl]), 2), "kospi_runup_low_day": str(kd[jl])})
            for y in (1, 3, 5):
                t = day + timedelta(days=int(365.25 * y))
                ev[f"kospi_{y}y_pct"] = round((at(kd, kp, t) / k0 - 1) * 100, 1) if t <= kd[-1] else None
            j0 = int(np.searchsorted(kd, day)); j3 = min(len(kd) - 1, int(np.searchsorted(kd, day + timedelta(days=3 * 365))))
            ev["kospi_further_3y_pct"] = round((kp[j0:j3 + 1].min() / k0 - 1) * 100, 1)
            ev["kospi_low_day"] = str(kd[j0 + int(np.argmin(kp[j0:j3 + 1]))])
            back = np.flatnonzero(kp[j0:] >= kpk)
            ev["kospi_years_to_peak"] = round((kd[j0 + back[0]] - day).days / 365.25, 1) if len(back) else None
            # 사건 끝 = 둘 중 하나가 고점 80% 위
            k = i
            while k < n and sdd[k] <= -0.2 and hdd[k] <= -0.2:
                k += 1
            ev["episode_end"] = str(D[k]) if k < n else None
            out["both"].append(ev)
            log("BOTH", **ev)
            i = k + 1
            continue
        i += 1
    kpk_now = float(Kfull_run[-1]); ipk = int(np.argmax(kp))
    out["now"] = {"kospi_peak": str(kd[ipk]), "kospi_dd_pct": round((kp[-1] / kpk_now - 1) * 100, 1), "samsung_dd_pct": round(sdd[-1] * 100, 1),
                  "hynix_dd_pct": round(hdd[-1] * 100, 1), "last": str(D[-1])}
    done = [e for e in out["both"] if e["kospi_3y_pct"] is not None]
    out["summary"] = {"episodes": len(out["both"]), "with_3y": len(done),
                      "kospi_dd_range": [min(e["kospi_dd_pct"] for e in out["both"]), max(e["kospi_dd_pct"] for e in out["both"])],
                      "kospi_further_range": [min(e["kospi_further_3y_pct"] for e in done), max(e["kospi_further_3y_pct"] for e in done)] if done else None,
                      "kospi_1y": [e["kospi_1y_pct"] for e in out["both"] if e["kospi_1y_pct"] is not None],
                      "kospi_3y": [e["kospi_3y_pct"] for e in done],
                      "kospi_years_to_peak": [e["kospi_years_to_peak"] for e in out["both"]]}
    log("NOW", **out["now"]); log("SUMMARY", **out["summary"])
    p = Path(__file__).with_suffix(".json")
    p.write_text(json.dumps(out, ensure_ascii=False, indent=1), "utf-8")
    log("DONE", out=p)


if __name__ == "__main__":
    main()
