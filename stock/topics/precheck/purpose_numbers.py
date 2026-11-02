#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-10-31 — A 에 '가장 오래 묶인 기간'(고점 아래에 머문 가장 긴 시간 — 가장 깊은 하락의 회복과 다를 수 있음) 더함
#          (사용자 지시 "니가 만든 2~4편으로 하지말고 내가 채팅에 쓴걸로" — 3편 '섹터 포트폴리오 분배' 제목 숫자).
# (v1.0 — 2026-10-31 — 최초.) 쇼츠·롱폼을 채널 목적에 맞게 다시 쓰는 데 쓸 '리스크' 숫자
#          (사용자 지시 2026-10-31 "… 리스크는 최대한 줄이고 천천히 수익내면서 장기 투자하는거 이게 이 채널의 목적인데 왜 다른 내용이 있는거야 다시 수정해봐").
#   더 벌었나가 아니라 — 가장 크게 빠진 폭 · 원금(고점) 회복에 걸린 해 · 반 토막(−50%) 난 적이 있나.
#   A. 업종 하나에만 vs 9개 업종 똑같이(1년마다 맞춤) vs S&P 500 vs 주식 60·채권 40(1년마다 맞춤) — 1999~2026 (채권 AGG 는 2003-09 부터라 같은 기간도 따로)
#   B. 누구나 아는 미국 회사 16곳(라이벌 8쌍) — 2016-10-27 → 2026-10-27 안에서 가장 크게 빠진 폭 · S&P 500 같은 기간
# 자료(새로 받지 않음): precheck/data/XL*.csv · AGG.csv (adjclose) · precheck/bulk/px/<기호>.csv (adjclose) · stock/source/timing-test-2026-10/calc/sp500tr_daily.csv
# 실행: python3 -B stock/topics/precheck/purpose_numbers.py → precheck/purpose_numbers_<날짜>.json
# ※ 연구·교육용 — 투자 권유가 아님.
import bisect
import csv
import json
import logging
from datetime import date
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
DATA, BULK = HERE / "data", HERE / "bulk" / "px"
CALC = HERE.parent.parent / "source" / "timing-test-2026-10" / "calc"
VERSION = "v1.1"
NINE = {"XLB": "소재", "XLE": "에너지", "XLF": "금융", "XLI": "산업재", "XLK": "기술", "XLP": "필수소비재", "XLU": "유틸리티", "XLV": "헬스케어", "XLY": "임의소비재"}
FAMOUS = {"KO": "코카콜라", "PEP": "펩시", "V": "비자", "MA": "마스터카드", "HD": "홈디포", "LOW": "로우스", "XOM": "엑슨모빌", "CVX": "셰브론",
          "AMD": "AMD", "INTC": "인텔", "WMT": "월마트", "TGT": "타깃", "JPM": "JP모건", "BAC": "뱅크오브아메리카", "MCD": "맥도날드", "SBUX": "스타벅스"}
logging.basicConfig(level=logging.INFO, format="[%(stage)s] %(message)s")
log = logging.getLogger("purpose_numbers")


def read(path, col):
    with path.open(encoding="utf-8") as f:
        rows = [r for r in csv.reader(f) if r and not r[0].startswith("#")]
    k = rows[0].index(col)
    return {r[0]: float(r[k]) for r in rows[1:] if len(r) > k and r[k]}


def align(ds, s):
    keys = sorted(s)
    out = np.full(len(ds), np.nan)
    for i, d in enumerate(ds):
        j = bisect.bisect_right(keys, d) - 1
        if j >= 0 and keys[j] >= ds[0]:
            out[i] = s[keys[j]]
    return out


def drawdown(ds, v):
    """가장 크게 빠진 폭 · 그 고점 날 · 바닥 날 · 고점을 다시 넘은 날(없으면 None) · 걸린 해."""
    ok = ~np.isnan(v)
    v, d = v[ok], [x for x, m in zip(ds, ok) if m]
    peak = np.maximum.accumulate(v)
    dd = v / peak - 1
    t = int(np.argmin(dd))
    p = int(np.argmax(v[:t + 1]))
    rec = next((k for k in range(t, len(v)) if v[k] >= v[p]), None)
    yrs = None if rec is None else round((date.fromisoformat(d[rec]) - date.fromisoformat(d[p])).days / 365.25, 1)
    return {"max_dd": f"{dd[t] * 100:.1f}%", "peak": d[p], "trough": d[t], "recovered": None if rec is None else d[rec], "years_to_recover": yrs,
            "_dd": float(dd[t])}


def longest_under(ds, v):
    """고점 아래에 머문 가장 긴 시간 — (해, 시작 고점 날, 다시 넘은 날 또는 '아직')."""
    ok = ~np.isnan(v)
    v, d = v[ok], [x for x, m in zip(ds, ok) if m]
    peak, pi, best = v[0], 0, (0.0, d[0], d[0])
    for i in range(1, len(v)):
        if v[i] >= peak:
            yrs = (date.fromisoformat(d[i]) - date.fromisoformat(d[pi])).days / 365.25
            if yrs > best[0]:
                best = (yrs, d[pi], d[i])
            peak, pi = v[i], i
    yrs = (date.fromisoformat(d[-1]) - date.fromisoformat(d[pi])).days / 365.25
    if yrs > best[0]:
        best = (yrs, d[pi], "아직")
    return {"years": round(best[0], 1), "from_peak": best[1], "back": best[2]}


def rebal(ds, parts):
    """parts = [(값 배열, 비중)] · 해가 바뀌는 첫 거래일마다 비중을 다시 맞춤."""
    val = np.ones(len(ds))
    units = [w / v[0] for v, w in parts]
    for i in range(len(ds)):
        tot = sum(u * v[i] for u, (v, _) in zip(units, parts))
        val[i] = tot
        if i and ds[i][:4] != ds[i - 1][:4]:
            units = [tot * w / v[i] for v, w in parts]
    return val


def main():
    with (CALC / "sp500tr_daily.csv").open(encoding="utf-8") as f:
        rows = [r for r in csv.reader(f) if r and not r[0].startswith("#")][1:]
    tr_all = {r[0]: float(r[1]) for r in rows if r[1]}
    log.info("source=sp500tr_daily.csv rows=%d", len(tr_all), extra={"stage": "LOAD"})

    # ---------- A. 1999-01-04 ~ 2026-10-27
    ds = [d for d in sorted(tr_all) if d >= "1999-01-04"]
    tr = np.array([tr_all[d] for d in ds])
    S = {k: align(ds, read(DATA / f"{k}.csv", "adjclose")) for k in NINE}
    agg = align(ds, read(DATA / "AGG.csv", "adjclose"))
    log.info("range=%s~%s sectors=%d agg_first=%s", ds[0], ds[-1], len(S), ds[int(np.argmax(~np.isnan(agg)))], extra={"stage": "LOAD"})
    A = {"window": f"{ds[0]} ~ {ds[-1]}", "업종 하나": {}}
    for k, name in NINE.items():
        A["업종 하나"][name] = drawdown(ds, S[k])
        A["업종 하나"][name]["longest_under"] = longest_under(ds, S[k])
        log.info("sector=%s %s", name, {x: y for x, y in A["업종 하나"][name].items() if not x.startswith("_")}, extra={"stage": "A_DD"})
    A["S&P 500"] = drawdown(ds, tr)
    A["S&P 500"]["longest_under"] = longest_under(ds, tr)
    mix = rebal(ds, [(S[k], 1 / 9) for k in NINE])
    A["9개 업종 똑같이 (1년마다 맞춤)"] = drawdown(ds, mix)
    A["9개 업종 똑같이 (1년마다 맞춤)"]["longest_under"] = longest_under(ds, mix)
    dd_one = sorted(v["_dd"] for v in A["업종 하나"].values())
    A["업종 하나 — 범위"] = {"least": f"{dd_one[-1] * 100:.1f}%", "most": f"{dd_one[0] * 100:.1f}%",
                         "half_or_worse": sum(x <= -0.5 for x in dd_one), "n": len(dd_one)}
    # 주식 60·채권 40 은 AGG 가 있는 날부터 — 같은 기간 S&P 500 · 업종 하나도 다시
    i0 = int(np.argmax(~np.isnan(agg)))
    d2 = ds[i0:]
    A["2003-09 부터"] = {"window": f"{d2[0]} ~ {d2[-1]}", "S&P 500": drawdown(d2, tr[i0:]),
                       "주식 60·채권 40 (1년마다 맞춤)": drawdown(d2, rebal(d2, [(tr[i0:], 0.6), (agg[i0:], 0.4)])),
                       "업종 하나": {NINE[k]: drawdown(d2, S[k][i0:])["max_dd"] for k in NINE}}
    for k in ("S&P 500", "9개 업종 똑같이 (1년마다 맞춤)"):
        log.info("%s %s", k, {x: y for x, y in A[k].items() if not x.startswith("_")}, extra={"stage": "A_DD"})
    log.info("from_2003 %s", json.dumps({k: (v["max_dd"], v["years_to_recover"]) for k, v in A["2003-09 부터"].items() if isinstance(v, dict) and "max_dd" in v},
                                        ensure_ascii=False), extra={"stage": "A_DD"})

    # ---------- B. 2016-10-27 ~ 2026-10-27
    d3 = [d for d in sorted(tr_all) if "2016-10-27" <= d <= "2026-10-27"]
    B = {"window": f"{d3[0]} ~ {d3[-1]}", "S&P 500": drawdown(d3, np.array([tr_all[d] for d in d3])), "회사": {}}
    for sym, name in FAMOUS.items():
        v = align(d3, read(BULK / f"{sym}.csv", "adjclose"))
        B["회사"][name] = drawdown(d3, v)
    half = [n for n, v in B["회사"].items() if v["_dd"] <= -0.5]
    worse = [n for n, v in B["회사"].items() if v["_dd"] < B["S&P 500"]["_dd"]]
    B["반 토막(−50% 이상) 난 적"] = {"n": len(half), "회사": half}
    B["S&P 500 보다 크게 빠진 적"] = {"n": len(worse), "of": len(FAMOUS)}
    log.info("sp500=%s half=%d %s worse_than_index=%d/%d", B["S&P 500"]["max_dd"], len(half), half, len(worse), len(FAMOUS), extra={"stage": "B_DD"})
    for n, v in B["회사"].items():
        log.info("co=%s dd=%s peak=%s trough=%s recovered=%s", n, v["max_dd"], v["peak"], v["trough"], v["recovered"], extra={"stage": "B_DD"})

    def clean(o):
        if isinstance(o, dict):
            return {k: clean(v) for k, v in o.items() if not k.startswith("_")}
        return o

    out = HERE / f"purpose_numbers_{date.today().isoformat()}.json"
    out.write_text(json.dumps({"tool": f"purpose_numbers.py {VERSION}", "rule": "배당 포함 수정 종가 · 가장 크게 빠진 폭 = 그때까지 고점 대비 · 회복 = 그 고점을 다시 넘은 첫날",
                               "A_sectors": clean(A), "B_famous16": clean(B)}, ensure_ascii=False, indent=1), "utf-8")
    log.info("file=%s", out.name, extra={"stage": "DONE"})


if __name__ == "__main__":
    main()
