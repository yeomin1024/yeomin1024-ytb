#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.2 — 2026-11-19 — 블로그 '현실적인 대안' 절에 쓸 단순 계산 두 개를 코드로 (글 속 숫자는 계산 출력만):
#          · split: 지금 남은 돈(6월 고점 1,000만 원 → 지금 삼전 값)에 매달 50만 원을 새로 지수로 넣으면 그 종목 몫이 몇 % 로 줄어드나 (가격이 그대로라는 가정)
#          · stress: 그 종목이 내 돈의 몇 % 일 때 하이닉스 2007 처럼 한 번 더 빠지면(−73.7%) 전체 돈이 얼마나 줄어드나
#          · recovery: 고점 되찾기까지 걸린 해 — 2년·3년 넘은 횟수
#          · now 에 '고점 전 해 첫 거래일 → 고점' 오른 폭 (얼마나 빨리 올랐다 빠졌는지) · 고점 1,000만 원 → 지금 몇 만 원 · 지금 환율
#          · summary 에 1년 뒤 '버티기 > 전부 S&P' 횟수 · 선택지별 1년·3년 뒤 가장 낮은·높은 값 (반만 옮기면 폭이 좁아지는지)
# (v1.1 — 2026-11-19 — 공정한 비교로 고침 (블로그 글 전 — 사용자 지시 "일단 블로그 글 형식으로 만들어봐 파일 형태로 알려주고"):
#          삼전·하닉(배당 포함 수정 종가) ↔ SPY 수정 종가(배당 포함 — v1.0 은 ^GSPC 가격만이라 불리했음) · 코스피 = ^KS11 가격 ↔ ^GSPC 가격 (둘 다 배당 뺌 —
#          KODEX 200 은 Yahoo 자료가 2007년 8일·2008년 없음이라 못 씀)
#          · 그날·1년·3년 뒤 원/달러 환율도 기록 (갈아탄 쪽 결과가 환율 때문인지 보이게).
# (v1.0 — 2026-11-19 — 주제 미리 계산: "코스피·삼성전자·SK하이닉스로 크게 손실 본 사람들의 현실적인 대안" (사용자 지시 2026-11-19
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
    if (np.asarray(d)[0] - start).days > 400:                  # 캐시가 짧으면 (다른 계산이 짧게 받아 둠) 처음부터 다시 받음
        log("REFETCH", symbol=sym, cached_first=d[0], want=start)
        d, cl, adj = c.fetch(sym, start=start, refetch=True)
    px = np.asarray(adj if adj is not None else cl, dtype=float)
    d = np.asarray(d)
    ok = np.isfinite(px) & (px > 0)
    log("LOAD", symbol=sym, rows=int(ok.sum()), first=d[ok][0], last=d[ok][-1])
    return d[ok], px[ok]


def at(d, px, day):
    return px[max(0, int(np.searchsorted(d, day, side="right")) - 1)]


def main():
    fx_d, fx = series("KRW=X", date(2000, 1, 1))
    spy_d, spy = series("SPY", date(1993, 1, 1))
    gsp_d, gsp = series("^GSPC", date(1990, 1, 1))
    out = {"rule": "직전 고점 대비 −40% 를 처음 찍은 날 · 고점에 100 넣은 사람이 그날 고른 길 → 1년·3년 뒤 금액 (삼전·하닉 = 배당 포함 수정 종가 ↔ SPY 배당 포함 원화 환산 · 코스피 = 가격 지수 ↔ S&P 500 가격 지수 원화 환산 (둘 다 배당 뺌) · 세금·수수료·환전 비용 뺌)",
           "start": str(fx_d[0]), "events": [], "now": {}, "counter": {}}
    for sym, name, (sp_d, sp) in (("005930.KS", "삼성전자", (spy_d, spy)), ("000660.KS", "SK하이닉스", (spy_d, spy)), ("^KS11", "코스피", (gsp_d, gsp))):
        sp_krw = lambda day, sp_d=sp_d, sp=sp: at(sp_d, sp, day) * at(fx_d, fx, day)   # noqa: E731
        d, px = series(sym, date(1995, 1, 1))
        run = np.maximum.accumulate(px)
        ip = int(np.argmax(px))
        y0 = int(np.searchsorted(d, date(d[ip].year, 1, 1)))
        out["now"][name] = {"from_peak_pct": round(float(px[-1] / px.max() - 1) * 100, 1), "peak": str(d[ip]), "last": str(d[-1]),
                            "year_start": str(d[y0]), "year_start_to_peak_pct": round(float(px[ip] / px[y0] - 1) * 100, 1),
                            "per_1000_manwon_now": round(float(1000 * px[-1] / px.max()))}
        start = max(fx_d[0], date(2004, 1, 1))          # 하이닉스 2003년은 자료 시작 직후라 뺌
        i, n = 0, len(px)
        while i < n:
            if d[i] >= start and px[i] <= run[i] * 0.6:
                peak, h = run[i], i
                v0 = px[h] / peak
                ev = {"name": name, "hit": str(d[h]), "value_at_hit": round(v0 * 100), "krw_at_hit": round(float(at(fx_d, fx, d[h])))}
                for yrs in (1, 3):
                    j = int(np.searchsorted(d, date(d[h].year + yrs, d[h].month, min(d[h].day, 28))))
                    if j >= n:
                        ev[f"{yrs}y"] = None
                        continue
                    hold, spr = px[j] / px[h], sp_krw(d[j]) / sp_krw(d[h])
                    ev[f"{yrs}y"] = {"hold": round(v0 * hold * 100), "half_sp": round(v0 * (0.5 * hold + 0.5 * spr) * 100), "all_sp": round(v0 * spr * 100),
                                     "krw": round(float(at(fx_d, fx, d[j]))), "sp_usd_pct": round(float(at(sp_d, sp, d[j]) / at(sp_d, sp, d[h]) - 1) * 100, 1)}
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
    one = [e for e in out["events"] if e.get("1y")]
    out["summary"]["with_1y"] = len(one)
    out["summary"]["hold_beats_all_sp_1y"] = sum(1 for e in one if e["1y"]["hold"] > e["1y"]["all_sp"])
    out["summary"]["all_sp_3y_at_or_above_100"] = sum(1 for e in done if e["3y"]["all_sp"] >= 100)
    out["summary"]["range"] = {f"{y}_{k}": [min(e[y][k] for e in grp), max(e[y][k] for e in grp)]
                               for y, grp in (("1y", one), ("3y", done)) for k in ("hold", "half_sp", "all_sp")}
    out["fx_now"] = {"date": str(fx_d[-1]), "krw": round(float(fx[-1]))}
    # 단순 계산 (가정을 글에 같이 밝힘 — 앞날 예측이 아님)
    yrs = sorted(e["years_to_peak"] for e in out["events"] if e["years_to_peak"] is not None)
    out["recovery"] = {"years_sorted": yrs, "over_2y": sum(1 for y in yrs if y > 2), "over_3y": sum(1 for y in yrs if y > 3), "n": len(yrs)}
    hold_now = round(1000 * (1 + out["now"]["삼성전자"]["from_peak_pct"] / 100))          # 만 원
    out["split"] = {"assume": "6월 고점에 1,000만 원 → 지금 삼전 값 · 매달 50만 원을 지수로 · 가격은 그대로라고 가정 (매도 없음)",
                    "hold_now_manwon": hold_now, "monthly_manwon": 50,
                    "rows": [{"months": m, "stock_share_pct": round(hold_now / (hold_now + 50 * m) * 100, 1)} for m in (0, 6, 12, 24, 36)]}
    worst = -min(e["further_drop_3y_pct"] for e in out["events"])
    out["stress"] = {"assume": f"그 종목이 한 번 더 {worst}% 빠진다면 (하이닉스 2007 이 −40% 뒤 더 빠진 폭) · 나머지 돈은 그대로",
                     "drop_pct": worst, "rows": [{"weight_pct": w, "total_loss_pct": round(w * worst / 100, 1)} for w in (100, 50, 30, 10)]}
    log("EXTRA", recovery=out["recovery"], split=[r["stock_share_pct"] for r in out["split"]["rows"]], stress=[r["total_loss_pct"] for r in out["stress"]["rows"]])
    p = Path(__file__).with_suffix(".json")
    p.write_text(json.dumps(out, ensure_ascii=False, indent=1), "utf-8")
    log("DONE", out=p, summary=out["summary"])


if __name__ == "__main__":
    main()
