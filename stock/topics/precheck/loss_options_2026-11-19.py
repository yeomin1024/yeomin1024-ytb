#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-11-19 — 주제 미리 계산: "코스피·삼성전자·SK하이닉스로 크게 손실 본 사람들의 현실적인 대안" (사용자 지시 2026-11-19
#          "코스피, 삼성 전자, sk하이닉스로 크게 손실 본 사람들 현실적인 대안이라는 주제가 먹힐지 내용을 어떻게 할건지 알려줘봐").
#          · 과거 같은 자리 = 직전 고점 대비 −40% 를 처음 찍은 날 (2003-12 이후 — 원/달러 일별 자료가 그때부터).
#          · 선택지: 버티기 · 반만 S&P 500(원화)으로 · 전부 S&P 500(원화)으로 → 1년·3년 뒤 금액 (고점에 100 넣은 사람 기준) · 그 뒤 더 빠진 폭 · 고점 되찾기까지.
#          · 반례(회복 못 한 종목): 카카오 · 에코프로 · LG에너지솔루션 — 고점 대비 지금.
#          자료 = Yahoo 수정 종가 (배당 반영) · 세금·수수료·환전 비용 뺌. ※ 연구·교육용 — 투자 권유가 아님. 과거가 앞날을 보장하지 않음.
import importlib.util
import json
import logging
from datetime import date, datetime, timezone
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location("c", ROOT / "stock/topics/titles_2026-11-18b/calc.py")
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)
logging.basicConfig(level=logging.INFO, format="%(message)s")
LOG = logging.getLogger("lossopt")


def log(stage, **kv):
    LOG.info("[%s] [%s] %s", stage, datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), " ".join(f"{k}={v}" for k, v in kv.items()))


def series(sym, start):
    d, cl, adj = c.fetch(sym, start=start)
    px = np.asarray(adj if adj is not None else cl, dtype=float)
    d = np.asarray(d)
    ok = np.isfinite(px) & (px > 0)
    log("LOAD", symbol=sym, rows=int(ok.sum()), first=d[ok][0], last=d[ok][-1])
    return d[ok], px[ok]


def at(d, px, day):
    return px[max(0, int(np.searchsorted(d, day, side="right")) - 1)]


def main():
    fx_d, fx = series("KRW=X", date(2000, 1, 1))
    sp_d, sp = series("^GSPC", date(1990, 1, 1))
    sp_krw = lambda day: at(sp_d, sp, day) * at(fx_d, fx, day)   # noqa: E731
    out = {"rule": "직전 고점 대비 −40% 를 처음 찍은 날 · 고점에 100 넣은 사람이 그날 고른 길 → 1년·3년 뒤 금액 (수정 종가 · S&P 500 은 원화 환산 · 세금·수수료 뺌)",
           "start": str(fx_d[0]), "events": [], "now": {}, "counter": {}}
    for sym, name in (("005930.KS", "삼성전자"), ("000660.KS", "SK하이닉스"), ("^KS11", "코스피")):
        d, px = series(sym, date(1995, 1, 1))
        run = np.maximum.accumulate(px)
        out["now"][name] = {"from_peak_pct": round(float(px[-1] / px.max() - 1) * 100, 1), "peak": str(d[int(np.argmax(px))]), "last": str(d[-1])}
        start = max(fx_d[0], date(2004, 1, 1))          # 하이닉스 2003년은 자료 시작 직후라 뺌
        i, n = 0, len(px)
        while i < n:
            if d[i] >= start and px[i] <= run[i] * 0.6:
                peak, h = run[i], i
                v0 = px[h] / peak
                ev = {"name": name, "hit": str(d[h]), "value_at_hit": round(v0 * 100)}
                for yrs in (1, 3):
                    j = int(np.searchsorted(d, date(d[h].year + yrs, d[h].month, min(d[h].day, 28))))
                    if j >= n:
                        ev[f"{yrs}y"] = None
                        continue
                    hold, spr = px[j] / px[h], sp_krw(d[j]) / sp_krw(d[h])
                    ev[f"{yrs}y"] = {"hold": round(v0 * hold * 100), "half_sp": round(v0 * (0.5 * hold + 0.5 * spr) * 100), "all_sp": round(v0 * spr * 100)}
                j3 = min(n - 1, int(np.searchsorted(d, date(d[h].year + 3, d[h].month, min(d[h].day, 28)))))
                ev["further_drop_3y_pct"] = round(float(px[h:j3 + 1].min() / px[h] - 1) * 100, 1)
                k = h
                while k < n and px[k] < peak:
                    k += 1
                ev["years_to_peak"] = round((d[k] - d[h]).days / 365.25, 1) if k < n else None
                out["events"].append(ev)
                i = k if k < n else n
                continue
            i += 1
    for sym, name, st in (("035720.KS", "카카오", date(2010, 1, 1)), ("086520.KQ", "에코프로", date(2015, 1, 1)), ("373220.KS", "LG에너지솔루션", date(2022, 1, 1))):
        d, px = series(sym, st)
        out["counter"][name] = {"peak": str(d[int(np.argmax(px))]), "from_peak_now_pct": round(float(px[-1] / px.max() - 1) * 100, 1),
                                "years_since_peak": round((d[-1] - d[int(np.argmax(px))]).days / 365.25, 1)}
    done = [e for e in out["events"] if e.get("3y")]
    out["summary"] = {"events": len(out["events"]), "with_3y": len(done),
                      "hold_3y_at_or_above_100": sum(1 for e in done if e["3y"]["hold"] >= 100),
                      "hold_beats_all_sp_3y": sum(1 for e in done if e["3y"]["hold"] > e["3y"]["all_sp"]),
                      "years_to_peak_range": [min(e["years_to_peak"] for e in out["events"] if e["years_to_peak"] is not None),
                                              max(e["years_to_peak"] for e in out["events"] if e["years_to_peak"] is not None)],
                      "worst_1y_hold": min((e["1y"]["hold"], e["name"], e["hit"]) for e in out["events"] if e.get("1y"))}
    p = Path(__file__).with_suffix(".json")
    p.write_text(json.dumps(out, ensure_ascii=False, indent=1), "utf-8")
    log("DONE", out=p, summary=out["summary"])


if __name__ == "__main__":
    main()
