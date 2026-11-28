#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.3 — 2026-11-28 — 지표마다 1년 전(252거래일 앞)보다 (chg_1y_pct) · 반등마다 확인일부터 꼭대기까지 (confirm_to_top_pct) · 실패 반등 요약(꼭대기 뒤 80% 넘게 더 빠진 수 · 깨지기까지 날수 범위) — 반론 검토 12회차 (1년 최저와 견줌 · '여러 번' 근거 · 기간).
# 이전 v1.2 — 2026-11-28 — 메모리 회사 주가(마이크론 MU · 삼성전자 005930.KS · SK하이닉스 000660.KS) 9-30 종가 → 마지막 종가 · 1년 최고가보다 (memory) — 트렌드포스 '메모리 3사 45%' 가 다시 확인되지 않아 실제 종가로 (이탈 검토 10회차 '세 곳 이름').
# 이전 v1.1 — 2026-11-28 — 실패한 반등마다 꼭대기 뒤 가장 낮은 값까지 하락률(top_to_later_low_pct) · 지표마다 1년 최저보다 몇 % (from_low_pct) · 반도체 지수 하루 하락 순위(sox_days — 11-05 가 2025-04 뒤 가장 큰 하루 하락인지 확인).
# 이전 v1.0 — 2026-11-28 — 최초. 대본 v10(사용자 구성 — 시장 상황 → 호재 → 악재 → 변수 → 비중) 숫자:
#   ① 시장 전체 지표 (10년 국채 금리 · 브렌트유 · 달러 지수 · S&P500 · 나스닥 · 반도체 지수 · 공포 지수 — 마지막 값 · 1년 최고와 거리 · 1·3개월 변화)
#   ② 하락 구간 안의 큰 반등 — SOXL 이 그 구간의 그때까지 가장 낮은 값보다 30% 넘게 오른 횟수 · 그 뒤 그 저점을 다시 깼는지(실패) · 진짜 바닥이었는지
#   사용자 지시 2026-11-28 "여러 폭락 사례를 보면 계속 하락하는게 아니라 반등을 주면서 하락한다 / 심지어 크게 상승한 것 같으면서도 저점을 깨고 다시 하락하는 경우도 있다 …
#   야 대본 이런식으로 내가 만든 구성대로 다시 수정해봐".
# CHANGELOG
#   v1.3 2026-11-28  chg_1y_pct · confirm_to_top_pct · failed_summary
#   v1.2 2026-11-28  memory (MU · 삼성전자 · SK하이닉스)
#   v1.1 2026-11-28  rallies top_to_later_low_pct · macro_row from_low_pct · sox_days
#   v1.0 2026-11-28  최초 — macro · rallies · selftest   (soxl_check.py v1.7 의 하락 구간·자료 캐시를 그대로 씀)
# ※ 연구·교육용 — 투자 권유가 아님. 앞날 자료 없음: 반등 판정은 그날까지의 종가만으로 하고, '실패/바닥'은 그 뒤 결과로 따로 셈.
"""python3 market_check.py [--refresh] [--selftest] → market_check_<마지막 거래일>.json"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import logging
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import soxl_check as sc          # noqa: E402  (load · validate · log · 하락 구간 정의)

VERSION = "v1.3"
MACRO = {                                    # Yahoo 기호: (이름, 단위)
    "^TNX": ("미국 10년 국채 금리", "%"),
    "BZ=F": ("브렌트유", "달러/배럴"),
    "DX-Y.NYB": ("달러 지수", "지수"),
    "^GSPC": ("S&P500", "지수"),
    "^IXIC": ("나스닥", "지수"),
    "^SOX": ("필라델피아 반도체 지수", "지수"),
    "^VIX": ("공포 지수(VIX)", "지수"),
}
RALLY_UP = 0.30          # 큰 반등 = 그 구간의 그때까지 가장 낮은 종가보다 30% 넘게 (SOXL — 3배 상품이라 하루 14% 도 흔해 30% 로)
YEAR = 252


def macro_row(sym: str, rows: list[dict]) -> dict:
    C = [r["close"] for r in rows]
    D = [r["date"] for r in rows]
    i = len(C) - 1
    lo = max(0, i - YEAR + 1)
    hi_i = max(range(lo, i + 1), key=lambda k: C[k])
    lo_i = min(range(lo, i + 1), key=lambda k: C[k])
    ch = lambda n: round((C[i] / C[i - n] - 1) * 100, 1) if i - n >= 0 else None
    out = {"name": MACRO[sym][0], "unit": MACRO[sym][1], "date": D[i], "close": round(C[i], 2),
           "high_1y": round(C[hi_i], 2), "high_1y_date": D[hi_i], "from_high_pct": round((C[i] / C[hi_i] - 1) * 100, 1),
           "low_1y": round(C[lo_i], 2), "low_1y_date": D[lo_i], "from_low_pct": round((C[i] / C[lo_i] - 1) * 100, 1),
           "chg_1m_pct": ch(21), "chg_3m_pct": ch(63), "chg_1y_pct": ch(YEAR), "date_1y_ago": D[i - YEAR] if i - YEAR >= 0 else None,
           "close_1y_ago": round(C[i - YEAR], 2) if i - YEAR >= 0 else None}
    if sym == "^TNX":                                     # 금리는 % 포인트 차이도
        out["chg_1m_pt"] = round(C[i] - C[i - 21], 2)
        out["chg_3m_pt"] = round(C[i] - C[i - 63], 2)
    return out


def rallies(dates: list[str], C: list[float], start: int, end: int, up: float = RALLY_UP) -> list[dict]:
    """하락 구간 [start, end] 안의 큰 반등. 그때까지 가장 낮은 종가 L 보다 (1+up) 넘게 오른 날 = 반등 하나.
    다음 반등은 L 보다 더 낮은 종가(새 저점)가 나온 뒤에만 셈. 결과: 반등마다 저점·확인일·그 뒤 가장 높았던 값·저점을 깼는지."""
    out = []
    low_i = start
    armed = True                                          # 새 저점이 나와야 다음 반등을 셈
    for k in range(start, end + 1):
        if C[k] < C[low_i]:
            low_i = k
            armed = True
            if out and out[-1]["broken"] is None:
                out[-1]["broken"] = dates[k]              # 앞 반등의 저점을 깸 = 실패
        elif armed and C[k] >= C[low_i] * (1 + up):
            out.append({"low_date": dates[low_i], "low": round(C[low_i], 2), "confirm_date": dates[k],
                        "confirm_gain_pct": round((C[k] / C[low_i] - 1) * 100, 1), "broken": None, "_low_i": low_i, "_k": k})
            armed = False
    for r in out:                                         # 반등 꼭대기 = 확인일부터 저점이 깨진 날(없으면 구간 끝)까지 가장 높은 종가
        stop = dates.index(r["broken"]) if r["broken"] else end
        top_i = max(range(r["_k"], stop + 1), key=lambda k: C[k])
        r["top_date"], r["top_gain_pct"] = dates[top_i], round((C[top_i] / C[r["_low_i"]] - 1) * 100, 1)
        if r["broken"]:
            b = dates.index(r["broken"])
            r["days_to_break"] = b - r["_low_i"]
            later = min(range(top_i, end + 1), key=lambda k: C[k])          # v1.1 꼭대기 뒤 (구간 끝까지) 가장 낮은 종가
            r["later_low_date"], r["top_to_later_low_pct"] = dates[later], round((C[later] / C[top_i] - 1) * 100, 1)
        r["confirm_to_top_pct"] = round((C[top_i] / C[r["_k"]] - 1) * 100, 1)          # v1.3 확인일 종가부터 꼭대기까지
        r["result"] = "실패 (저점 깸)" if r["broken"] else "끝까지 안 깸"
        del r["_low_i"], r["_k"]
    return out


def build(refresh: bool) -> dict:
    rows = sc.load("SOXL", refresh)
    sc.validate("SOXL", rows)
    D, C = [r["date"] for r in rows], [r["close"] for r in rows]
    prev = json.loads((HERE / "soxl_check_2026-11-27.json").read_text("utf-8"))
    eps = []
    for e in prev["episodes"]:
        s = D.index(e["peak"])
        t = D.index(e["trough"])
        end = D.index(e["recovered"]) if e.get("recovered") else len(D) - 1   # 구간 끝 = 새 1년 최고가 (진행 중이면 지금)
        R = rallies(D, C, s, end)
        fail = [r for r in R if r["broken"]]
        eps.append({"peak": e["peak"], "trough": e["trough"], "end": D[end], "ongoing": e["ongoing"], "dd_pct": e["dd"],
                    "months_to_trough": round((dt.date.fromisoformat(e["trough"]) - dt.date.fromisoformat(e["peak"])).days / 30.44, 1),
                    "rallies": len(R), "failed": len(fail), "held": len(R) - len(fail),
                    "max_failed_gain_pct": max((r["top_gain_pct"] for r in fail), default=None), "list": R})
        log_ep = eps[-1]
        sc.log("RALLY", peak=e["peak"], trough=e["trough"], ongoing=e["ongoing"], rallies=len(R), failed=len(fail),
               max_failed_gain=log_ep["max_failed_gain_pct"])
    done = [e for e in eps if not e["ongoing"]]
    summ = {"past_episodes": len(done), "past_rallies": sum(e["rallies"] for e in done), "past_failed": sum(e["failed"] for e in done),
            "past_max_failed_gain_pct": max((e["max_failed_gain_pct"] or 0) for e in done),
            "now_rallies": eps[-1]["rallies"] if eps and eps[-1]["ongoing"] else None,
            "now_failed": eps[-1]["failed"] if eps and eps[-1]["ongoing"] else None,
            "past_failed_80plus": sum(1 for e in done for r in e["list"] if r["broken"] and r["top_to_later_low_pct"] <= -80),
            "past_days_to_break": sorted(r["days_to_break"] for e in done for r in e["list"] if r["broken"]),
            "now_failed_80plus": sum(1 for r in (eps[-1]["list"] if eps and eps[-1]["ongoing"] else []) if r["broken"] and r["top_to_later_low_pct"] <= -80),
            "now_days_to_break": sorted(r["days_to_break"] for r in (eps[-1]["list"] if eps and eps[-1]["ongoing"] else []) if r["broken"]),
            "note": "실패 = 그 반등의 시작 저점을 뒤에 종가로 깸 · days_to_break = 저점 날부터 깬 날까지 거래일 · 과거 구간은 끝(새 1년 최고가)까지 본 결과 · 진행 중 구간의 '안 깸'은 아직 모름"}
    mac = {}
    for sym in MACRO:
        try:
            r = sc.load(sym, refresh) if sym in ("^GSPC", "^IXIC", "^SOX", "^VIX") else load_any(sym, refresh)
        except SystemExit as ex:
            sc.log("MACRO", logging.WARNING, sym=sym, error=str(ex)[:160], next="이 지표는 대본에 쓰지 않음")
            continue
        sc.validate(sym, r)
        mac[sym] = macro_row(sym, r)
        sc.log("MACRO", sym=sym, **{k: mac[sym][k] for k in ("date", "close", "from_high_pct", "chg_1m_pct")})
    sox = sc.load("^SOX", refresh)                                               # v1.1 반도체 지수 하루 하락 순위
    sd = [(b["date"], (b["close"] / a["close"] - 1) * 100) for a, b in zip(sox, sox[1:])]
    def rank_since(day, since):
        v = dict(sd)[day]
        worse = [d for d, x in sd if since <= d and x < v and d != day]
        return {"date": day, "chg_pct": round(v, 1), "worse_days_since": len(worse), "since": since, "worse_list": worse[:5]}
    sox_days = {d: rank_since(d, "2025-04-10") for d in ("2026-11-05", "2026-11-20", "2026-11-24") if d in dict(sd)}
    for d, x in sox_days.items():
        sc.log("SOXDAY", day=d, chg=x["chg_pct"], worse_since_2025_04_10=x["worse_days_since"])
    memory = {}                                                                   # v1.2 메모리 회사 주가 (그 나라 통화 종가)
    for sym, nm in (("MU", "마이크론"), ("005930.KS", "삼성전자"), ("000660.KS", "SK하이닉스")):
        try:
            r = load_any(sym, refresh)
        except SystemExit as ex:
            sc.log("MEMORY", logging.WARNING, sym=sym, error=str(ex)[:160], next="이 종목은 대본에 쓰지 않음")
            continue
        sc.validate(sym, r)
        dd = {x["date"]: x["close"] for x in r}
        base_d = max(d for d in dd if d <= "2026-09-30")
        last_d = r[-1]["date"]
        yr = [x for x in r if x["date"] > (dt.date.fromisoformat(last_d) - dt.timedelta(days=365)).isoformat()]
        hi = max(yr, key=lambda x: x["close"])
        memory[sym] = {"name": nm, "base_date": base_d, "base": round(dd[base_d], 2), "date": last_d, "close": round(dd[last_d], 2),
                       "since_sep30_pct": round((dd[last_d] / dd[base_d] - 1) * 100, 1),
                       "high_1y": round(hi["close"], 2), "high_1y_date": hi["date"], "from_high_pct": round((dd[last_d] / hi["close"] - 1) * 100, 1)}
        sc.log("MEMORY", sym=sym, **{k: memory[sym][k] for k in ("base_date", "date", "since_sep30_pct", "from_high_pct")})
    return {"memory": memory, "sox_days": sox_days, "tool": f"market_check.py {VERSION}", "made": dt.datetime.now(sc.KST).isoformat(timespec="seconds"),
            "source": "Yahoo Finance chart API 일별 종가 10년 (soxl_check.py 캐시 공유)", "last_date": D[-1],
            "rules": {"rally_up": RALLY_UP, "year_days": YEAR, "episode": "soxl_check.py v1.7 — 1년 최고가보다 70% 넘게 하락한 구간 · 끝 = 새 1년 최고가"},
            "macro": mac, "rally_summary": summ, "episodes": eps}


def load_any(sym: str, refresh: bool) -> list[dict]:
    """soxl_check.load 는 '^' 만 파일 이름에서 바꿈 — '=' · '.' 기호도 되게 같은 꼴로."""
    import csv
    p = HERE / "data" / (sym.replace("^", "IDX_").replace("=", "_").replace(".", "_") + ".csv")
    if p.is_file() and not refresh:
        rows = [{"date": r["date"], "close": float(r["close"])} for r in csv.DictReader(p.open(encoding="utf-8"))]
        sc.log("LOAD", sym=sym, source="cache", rows=len(rows), first=rows[0]["date"], last=rows[-1]["date"])
        return rows
    import market_data as md
    try:
        raw = md.fetch_one(sym, "10y")
    except Exception as e:
        raise SystemExit(f"[LOAD] {sym} 받기 실패 ({type(e).__name__}: {e}) — 허용 목록 query1.finance.yahoo.com 확인")
    rows = [{"date": r["date"], "close": float(r["close"])} for r in raw if r.get("close")]
    with p.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["date", "close"]); w.writeheader(); w.writerows(rows)
    sc.log("LOAD", sym=sym, source="Yahoo 10y daily", rows=len(rows), first=rows[0]["date"], last=rows[-1]["date"])
    return rows


def selftest() -> int:
    ok = True
    def check(name, cond, **kw):
        nonlocal ok
        print(("PASS " if cond else "FAIL ") + name + ("" if cond else "  " + str(kw)))
        ok = ok and bool(cond)
    d = [f"d{i:02d}" for i in range(12)]
    # 100 → 50(저점) → 70(+40% 반등) → 40(저점 깸 — 실패) → 60(+50% 반등) → 55 → 90 (끝까지 안 깸)
    c = [100, 80, 50, 60, 70, 55, 40, 50, 60, 55, 75, 90]
    R = rallies(d, c, 0, 11)
    check("반등 두 번 · 첫째 실패 · 둘째 안 깸", len(R) == 2 and R[0]["broken"] == "d06" and R[1]["broken"] is None, R=R)
    check("첫 반등 꼭대기 = 저점 깨기 전 가장 높은 값 (+40%)", R[0]["top_gain_pct"] == 40.0 and R[0]["top_date"] == "d04")
    check("새 저점 전에는 다시 세지 않음 (50→60→55→75 는 하나)", R[1]["low_date"] == "d06" and R[1]["confirm_date"] == "d08")
    c2 = [100, 50, 64, 66, 60, 70]                         # 30% 못 넘으면 반등 아님 (64 = +28%) · 66 = +32% → 하나
    check("30% 문턱", [r["confirm_date"] for r in rallies(d[:6], c2, 0, 5)] == ["d03"])
    print("selftest: " + ("OK" if ok else "FAIL"))
    return 0 if ok else 1


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="SOXL 편 대본 v10 숫자 — 시장 전체 지표 · 하락 구간 안 큰 반등")
    ap.add_argument("--refresh", action="store_true", help="Yahoo 에서 다시 받음 (기본 = data/ 캐시)")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    logging.basicConfig(level=logging.INFO, format="%(message)s", stream=sys.stdout)
    if a.selftest:
        return selftest()
    out = build(a.refresh)
    p = HERE / f"market_check_{out['last_date']}.json"
    p.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", "utf-8")
    sc.log("DONE", out=p.name, macro=len(out["macro"]), **{k: v for k, v in out["rally_summary"].items() if k != "note"})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
