#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-30 — 최초. 정답 미리 확인 4회차 (사용자 지시 2026-10-30 "1, 2단계만 평가 했으니 다시 업데이트 해봐" — 1단계 14개 중 12개·2단계 6개를
#          '뻔함 · 차트만 봐도 앎 · 관심 없음 · 시청자는 자기 수익에만 관심'으로 버림, 좋음 = T046(계좌 확인 주기 — 호기심) · T050(하락장 대처 — 실제 회사)).
#          새 후보 8개 — 지수 차트 사실이 아니라 '내 종목·내 계좌·하락장 대처'를 실제 종목·업종 자료로. precheck.py v1.3 이 불러 TOPICS4 에 넣음.
#
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.0 | 2026-10-30 | 최초 — 손절 −10% · 폭락 종목 다음 날 · 라이벌 5쌍 · 하락장 업종 · 하락장 승자 업종 따라 사기 · 오른 종목 vs 내린 종목 · 하락장 전 회사 특징 · 장중 vs 밤사이 | 전부 |
#
# 미리 보기 점검 (lookahead): 사는 날 판단은 그날 종가까지 아는 값만 — 손절은 그날 종가가 −10% 아래면 그날 종가에 팖 · 폭락 종목은 다음 거래일 종가에 삼 ·
#   하락장 '덜 빠진 업종 따라 사기'는 바닥 날(그때는 바닥인지 모름) 대신 하락장이 끝났다고 알려진 날(지수가 바닥에서 20% 오른 날)에 삼 ·
#   재무 특징은 회계연도 끝 + 75일이 지난 숫자만 (2025 하락장 = FY2023).
# ⚠ 생존 편향: 종목 자료는 지금 S&P 500 회사만 — 무너져 빠진 회사가 없음. 주제마다 결론이 편향과 같은 쪽이면 미확인 (stocks._biased).
# ※ 연구·교육용 — 투자 권유가 아님.
import csv
import json
import time
import urllib.parse
import urllib.request
from datetime import date, datetime, timezone
from pathlib import Path

import numpy as np

import risk
import stocks

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
VERSION = "v1.0"
YEAR = 252                      # 거래일
pct, usd = stocks.pct, stocks.usd
CELLS = (("2005~08", 2005, 2008), ("2009~19", 2009, 2019), ("2020~24", 2020, 2024))


def _d(s):
    return date.fromisoformat(s).toordinal()


def _starts(o, y0=2005, y1=2024, fwd=YEAR):
    """달마다 첫 거래일 위치 (앞으로 fwd 거래일이 있어야)."""
    out, last = [], None
    for k, x in enumerate(o):
        dd = date.fromordinal(int(x))
        if y0 <= dd.year <= y1 and (dd.year, dd.month) != last and k + fwd < len(o):
            out.append(k)
            last = (dd.year, dd.month)
    return out


def _cell(y):
    for lab, a, b in CELLS:
        if a <= y <= b:
            return lab
    return None


# ================================================================ 1. 손절 −10%
def stop_loss(B, I, P, F):
    """종목 하나를 사서 1년 — 그냥 들고 있기 vs 산 값보다 10% 빠진 날 종가에 팔고 국채 vs 팔고 S&P 500 으로 갈아타기. 안정 = 끝에 국채보다 더 + 원금 20% 넘게 안 줄어듦."""
    i0, o, syms, A = risk.matrix(I, P, start=date(2004, 1, 1))
    cash, tr = B.cash[i0:], I.tr[i0:]
    res = {lab: {"n": 0, "hold_st": 0, "stop_st": 0, "sw_st": 0, "hold_end": [], "stop_end": [], "sw_end": [], "hit": 0, "stop_beats_hold": 0, "sw_beats_hold": 0} for lab, *_ in CELLS}
    for s in _starts(o):
        lab = _cell(date.fromordinal(int(o[s])).year)
        w = A[s:s + YEAR + 1] / A[s]
        ok = ~np.isnan(w).any(axis=0)
        w = w[:, ok]
        c = cash[s:s + YEAR + 1] / cash[s]
        t = tr[s:s + YEAR + 1] / tr[s]
        hit = (w <= 0.90)
        first = np.where(hit.any(axis=0), hit.argmax(axis=0), -1)
        hold_end, hold_min = w[-1], w.min(axis=0)
        stop_end, sw_end, stop_min, sw_min = hold_end.copy(), hold_end.copy(), hold_min.copy(), hold_min.copy()
        for j in np.flatnonzero(first >= 0):
            k = first[j]
            v = w[k, j]
            stop_end[j] = v * c[-1] / c[k]
            path_sw = v * t[k:] / t[k]
            sw_end[j] = path_sw[-1]
            stop_min[j] = w[:k + 1, j].min()
            sw_min[j] = min(stop_min[j], path_sw.min())
        R = res[lab]
        R["n"] += w.shape[1]
        R["hit"] += int((first >= 0).sum())
        R["hold_st"] += int(((hold_end > c[-1]) & (hold_min >= 0.8)).sum())
        R["stop_st"] += int(((stop_end > c[-1]) & (stop_min >= 0.8)).sum())
        R["sw_st"] += int(((sw_end > c[-1]) & (sw_min >= 0.8)).sum())
        R["stop_beats_hold"] += int((stop_end > hold_end)[first >= 0].sum())
        R["sw_beats_hold"] += int((sw_end > hold_end)[first >= 0].sum())
        R["hold_end"].append(float(np.median(hold_end)))
        R["stop_end"].append(float(np.median(stop_end)))
        R["sw_end"].append(float(np.median(sw_end)))
    tab, dif_stop, dif_sw = {}, {}, {}
    for lab, R in res.items():
        n = R["n"]
        tab[lab] = {"n": n, "손절 걸림": pct(R["hit"] / n), "그냥 보유 안정": pct(R["hold_st"] / n), "손절→국채 안정": pct(R["stop_st"] / n),
                    "손절→S&P500 안정": pct(R["sw_st"] / n), "걸린 것 중 손절이 더 남음": pct(R["stop_beats_hold"] / max(R["hit"], 1)),
                    "걸린 것 중 갈아타기가 더 남음": pct(R["sw_beats_hold"] / max(R["hit"], 1)),
                    "1년 수익 중앙값(보유·손절·갈아타기)": " · ".join(pct(float(np.median(R[k])) - 1) for k in ("hold_end", "stop_end", "sw_end"))}
        dif_stop[lab] = (R["stop_st"] - R["hold_st"]) / n
        dif_sw[lab] = (R["sw_st"] - R["hold_st"]) / n
    cl_stop, why_stop = risk.classify_diff(dif_stop, "2009~19")
    cl_sw, why_sw = risk.classify_diff(dif_sw, "2009~19")
    # 편향 크기 점검: 빠진 회사(해마다 지금 구성의 약 5% 라고 크게 잡음)가 모두 1년에 −50% 였다고 넣으면 — 그 회사는 보유·손절(→국채) 모두 '안정' 아님
    #   (손절이 걸리면 끝 값이 산 값의 90% 남짓이라 국채보다 늘 적음 → 손절→국채가 안정인 것은 손절이 안 걸린 것뿐) → 차이는 1/1.05 로만 줄고 방향은 그대로.
    MISS = 0.05
    adj = {k: v / (1 + MISS) for k, v in dif_stop.items()}
    cl_adj, _ = risk.classify_diff(adj, "2009~19")
    r = {"class": cl_adj if cl_adj == cl_stop else "조건부형",
         "answer": f"−10% 손절선이 1년 안에 걸린 몫 " + " · ".join(f"{k} {v['손절 걸림']}" for k, v in tab.items()) +
                   " | 안정 수익 확률 (그냥 보유 → 손절 후 국채 · 손절 후 S&P 500) — " + " | ".join(f"{k}: {v['그냥 보유 안정']} → {v['손절→국채 안정']} · {v['손절→S&P500 안정']}" for k, v in tab.items()),
         "table": tab, "parts": {"손절→국채 vs 보유": cl_stop, "손절→S&P 500 vs 보유": cl_sw},
         "bias_check": {"빠진 회사 몫(가정)": pct(MISS), "손절→국채 − 보유 (편향 넣음)": {k: f"{v * 100:+.1f}%p" for k, v in adj.items()}, "분류": cl_adj},
         "why": f"손절→국채 {cl_stop}({why_stop}) — 빠진 회사 5%가 모두 −50% 였다고 넣어도 {cl_adj}(차이 1/1.05 로만 줄어듦: 그런 회사는 보유·손절 모두 '안정' 아님) · "
                f"손절→S&P 500 {cl_sw}({why_sw}) — 편향이 보유 쪽이라 갈아타기 몫은 실제로는 더 클 수 있음 · 정답으로는 '손절 후 현금은 보유보다 덜 안정적'과 '걸린 몫'만 씀"}
    return r


# ================================================================ 2. 하루 −10% 폭락한 종목, 다음 날 사기
def crash_buy(B, I, P, F):
    """지수는 5% 넘게 안 빠진 날 혼자 10% 넘게 빠진 종목 (30일 안 되풀이는 뺌) — 다음 거래일 종가에 사서 1개월 · 1년 vs 같은 날 S&P 500."""
    rows = []
    lo, hi = _d("2005-01-01"), _d("2024-10-27")
    ir = np.concatenate([[0.0], I.tr[1:] / I.tr[:-1] - 1])
    for s, p in P.items():
        r = p.adj[1:] / p.adj[:-1] - 1
        last = -10 ** 9
        for k in np.flatnonzero(r <= -0.10):
            dj = int(p.o[k + 1])
            if not (lo <= dj <= hi) or dj - last < 30 or k + 2 >= len(p.o):
                continue
            ii = int(np.searchsorted(I.o, dj, side="right")) - 1
            if ii < 1 or I.o[ii] != dj or ir[ii] <= -0.05:
                continue
            last = dj
            d0 = int(p.o[k + 2])
            x = stocks._rel(p, I, d0, h=365)
            m = stocks._rel(p, I, d0, h=30)
            if x and m:
                seg = p.adj[(p.o >= d0) & (p.o <= d0 + 365)] / p.at(d0)
                rows.append((s, date.fromordinal(dj).isoformat(), x[0], x[1], m[0], m[1], float(seg.min())))
    a = np.array([(r[2], r[3], r[4], r[5], r[6]) for r in rows])
    yrs = np.array([int(r[1][:4]) for r in rows])
    cm = {}
    for lab, y0, y1 in CELLS:
        mk = (yrs >= y0) & (yrs <= y1)
        cm[lab] = float(np.mean(a[mk, 0] > a[mk, 1])) - 0.5 if mk.sum() >= 30 else None
    cl, why = risk.classify_diff(cm, "2009~19")
    r = {"class": cl if cl != "정답형" else "사실형",
         "answer": f"혼자 하루 10% 넘게 빠진 종목을 다음 날 산 {len(rows)}번 — 1년 뒤 S&P 500보다 더 남은 몫 {pct(float(np.mean(a[:, 0] > a[:, 1])))} · "
                   f"1년 수익 중앙값 {pct(float(np.median(a[:, 0])))} (같은 날 S&P 500 {pct(float(np.median(a[:, 1])))}) · 1개월 뒤 더 남은 몫 {pct(float(np.mean(a[:, 2] > a[:, 3])))} · "
                   f"1년 안에 산 값보다 20% 넘게 더 빠진 적 {pct(float(np.mean(a[:, 4] < 0.8)))}",
         "cells": {k: pct(v + 0.5) if v is not None else "-" for k, v in cm.items()}, "n": len(rows),
         "why": f"칸(시작 연도) {why} · 편향: 폭락 뒤 무너져 빠진 회사가 없음 — '사도 됐다' 쪽으로 미는 편향"}
    if np.mean(a[:, 0] > a[:, 1]) > 0.5:
        return stocks._biased(r, "지수보다 더 남은 몫이 절반 넘음 — 편향과 같은 쪽")
    return r


# ================================================================ 3. 라이벌 5쌍
PAIRS = [("KO", "PEP", "코카콜라", "펩시"), ("V", "MA", "비자", "마스터카드"), ("HD", "LOW", "홈디포", "로우스"), ("XOM", "CVX", "엑슨모빌", "셰브론"),
         ("AMD", "INTC", "AMD", "인텔"), ("WMT", "TGT", "월마트", "타깃"), ("JPM", "BAC", "JP모건", "뱅크오브아메리카"), ("MCD", "SBUX", "맥도날드", "스타벅스")]


def rivals(B, I, P, F):
    """라이벌 회사 쌍 — 5년 · 10년 (배당 포함 수정 종가, 1만 달러) · 같은 기간 S&P 500."""
    end = int(I.o[-1])
    out = {}
    for y in (5, 10):
        a = end - int(y * 365.25)
        ix = I.at(end) / I.at(a)
        rows = []
        for s1, s2, n1, n2 in PAIRS:
            if s1 not in P or s2 not in P or not (P[s1].has(a - 7, end) and P[s2].has(a - 7, end)):
                continue
            v1, v2 = P[s1].at(end) / P[s1].at(a), P[s2].at(end) / P[s2].at(a)
            rows.append({"pair": f"{n1} vs {n2}", "1": usd(10000 * v1), "2": usd(10000 * v2), "winner": n1 if v1 > v2 else n2, "gap": f"{max(v1, v2) / min(v1, v2):.2f}배",
                         "both_beat_sp500": bool(v1 > ix and v2 > ix), "neither_beat": bool(v1 < ix and v2 < ix)})
        out[f"{y}년"] = {"start": date.fromordinal(a).isoformat(), "end": date.fromordinal(end).isoformat(), "sp500": usd(10000 * ix), "pairs": rows}
    flips = [r["pair"] for r, q in zip(out["5년"]["pairs"], out["10년"]["pairs"]) if r["winner"] != q["winner"]]
    return {"class": "사실형", "answer": "10년(1만 달러): " + " · ".join(f"{r['pair']} → {r['winner']} ({r['gap']})" for r in out["10년"]["pairs"]) +
                                     f" · S&P 500 {out['10년']['sp500']} | 5년과 10년 승자가 바뀐 쌍: {', '.join(flips) or '없음'}",
            "table": out, "why": "지난 사실 — 고른 쌍(유명한 라이벌)이라 규칙으로 넓히지 않음 · 두 회사 모두 지금 S&P 500 에 있음"}


# ================================================================ 4·5. 하락장 업종 · 하락장에서 버틴 업종 따라 사기
SECTORS = {"XLB": "소재", "XLE": "에너지", "XLF": "금융", "XLI": "산업재", "XLK": "기술", "XLP": "필수소비재", "XLU": "유틸리티", "XLV": "헬스케어", "XLY": "임의소비재",
           "XLC": "통신서비스", "XLRE": "부동산"}
BEARS = [("2007-10-09", "2009-03-09", "금융위기"), ("2020-02-19", "2020-03-23", "코로나"), ("2022-01-03", "2022-10-12", "2022 금리 인상"), ("2025-02-19", "2025-04-08", "2025 관세")]


def _sector_series(B):
    return {k: B.series(k) for k in SECTORS}


def _ret(v, a, b, d):
    ia, ib = int(np.searchsorted(d, a, side="right")) - 1, int(np.searchsorted(d, b, side="right")) - 1
    return float(v[ib] / v[ia] - 1) if ia >= 0 and ib >= 0 and v[ia] == v[ia] and v[ib] == v[ib] and v[ia] > 0 else None


def sector_bear(B, I, P, F):
    """하락장(S&P 500 고점 날 → 바닥 날)마다 업종 ETF(배당 포함) 수익 — 가장 덜 빠진·가장 많이 빠진 업종."""
    S = _sector_series(B)
    d = np.array([x.toordinal() for x in B.d])
    out, least = {}, []
    for a, b, name in BEARS:
        ix = _ret(B.tr, _d(a), _d(b), d)
        rs = {SECTORS[k]: _ret(v, _d(a), _d(b), d) for k, v in S.items() if v is not None}
        rs = {k: x for k, x in rs.items() if x is not None}
        order = sorted(rs.items(), key=lambda kv: -kv[1])
        out[name] = {"window": f"{a} → {b}", "sp500": pct(ix), "best": [f"{k} {pct(x)}" for k, x in order[:3]], "worst": [f"{k} {pct(x)}" for k, x in order[-3:]],
                     "n_sectors": len(rs), "beat_index": [k for k, x in order if x > ix]}
        least.append(order[0][0])
    same = len(set(least)) == 1
    return {"class": "사실형", "answer": "가장 덜 빠진 업종: " + " · ".join(f"{n} {out[n]['best'][0]} (S&P 500 {out[n]['sp500']})" for *_, n in BEARS) +
                                     f" — {'매번 같음' if same else '매번 같지 않음'}",
            "table": out, "why": "업종 ETF(SPDR, 배당 포함) — 지수 단위라 생존 편향 없음 · 하락장 = S&P 500 고점 날 → 바닥 날"}


def sector_chase(B, I, P, F):
    """하락장이 끝났다고 알려진 날(바닥 뒤 S&P 500 이 바닥보다 20% 오른 첫날)에, 그 하락장에서 가장 덜 빠진 업종 vs 가장 많이 빠진 업종 vs S&P 500 — 1년·2년."""
    S = _sector_series(B)
    d = np.array([x.toordinal() for x in B.d])
    out, cm1 = {}, {}
    for a, b, name in BEARS:
        rs = {k: _ret(v, _d(a), _d(b), d) for k, v in S.items() if v is not None}
        rs = {k: x for k, x in rs.items() if x is not None}
        best, worst = max(rs, key=rs.get), min(rs, key=rs.get)
        ib = int(np.searchsorted(d, _d(b), side="right")) - 1
        lowp = B.price[ib]
        k = next((j for j in range(ib, len(d)) if B.price[j] >= lowp * 1.2), None)
        if k is None:
            continue
        row = {"bear": name, "buy_day": date.fromordinal(int(d[k])).isoformat(), "best_sector": SECTORS[best], "worst_sector": SECTORS[worst]}
        for h, lab in ((365, "1y"), (730, "2y")):
            if d[k] + h > d[-1]:
                continue
            e = int(d[k] + h)
            row[lab] = {"버틴 업종": pct(_ret(S[best], int(d[k]), e, d)), "많이 빠진 업종": pct(_ret(S[worst], int(d[k]), e, d)), "S&P 500": pct(_ret(B.tr, int(d[k]), e, d))}
            if lab == "1y":
                cm1[name] = _ret(S[best], int(d[k]), e, d) - _ret(B.tr, int(d[k]), e, d)
        out[name] = row
    lost = sum(1 for v in cm1.values() if v < 0)
    return {"class": "사실형", "answer": "하락장 끝(바닥 +20% 날)에 '가장 덜 빠진 업종'을 산 1년 — " + " · ".join(
        f"{n}: {out[n]['best_sector']} {out[n]['1y']['버틴 업종']} vs S&P 500 {out[n]['1y']['S&P 500']} (많이 빠진 {out[n]['worst_sector']} {out[n]['1y']['많이 빠진 업종']})"
        for n in out if "1y" in out[n]) + f" — S&P 500 보다 덜 번 때 {lost}/{len(cm1)}번",
            "table": out, "why": "업종 ETF — 생존 편향 없음 · 사는 날은 하락장이 끝났다고 알려진 날(바닥을 그날 알 수 없어서) · 4번뿐이라 규칙으로 넓히지 않음"}


# ================================================================ 6. 내 계좌의 오른 종목 vs 내린 종목
def winners_losers(B, I, P, F):
    """1년 전에 산 종목이 지금 +30% 넘게 오른 것 vs −30% 넘게 내린 것 — 다음 1년 (배당 포함) · S&P 500 보다 더 남은 몫 · 원금(지금 값)보다 20% 넘게 더 빠진 적."""
    i0, o, syms, A = risk.matrix(I, P, start=date(2003, 1, 1))
    tr = I.tr[i0:]
    res = {lab: {"win": [], "lose": [], "win_beat": [], "lose_beat": [], "win_dd": [], "lose_dd": []} for lab, *_ in CELLS}
    for s in _starts(o):
        if s < YEAR:
            continue
        lab = _cell(date.fromordinal(int(o[s])).year)
        past = A[s] / A[s - YEAR] - 1
        w = A[s:s + YEAR + 1] / A[s]
        ok = ~np.isnan(past) & ~np.isnan(w).any(axis=0)
        ix = tr[s + YEAR] / tr[s] - 1
        nxt, mn = w[-1] - 1, w.min(axis=0)
        for key, m in (("win", ok & (past >= 0.30)), ("lose", ok & (past <= -0.30))):
            if m.sum():
                res[lab][key] += list(nxt[m])
                res[lab][key + "_beat"] += list(nxt[m] > ix)
                res[lab][key + "_dd"] += list(mn[m] < 0.8)
    tab, cm = {}, {}
    for lab, R in res.items():
        tab[lab] = {"오른 종목 n": len(R["win"]), "내린 종목 n": len(R["lose"]),
                    "다음 1년 중앙값 (오른·내린)": f"{pct(float(np.median(R['win'])))} · {pct(float(np.median(R['lose'])))}",
                    "S&P 500보다 더 남은 몫 (오른·내린)": f"{pct(float(np.mean(R['win_beat'])))} · {pct(float(np.mean(R['lose_beat'])))}",
                    "1년 안에 20% 넘게 더 빠진 적 (오른·내린)": f"{pct(float(np.mean(R['win_dd'])))} · {pct(float(np.mean(R['lose_dd'])))}"}
        cm[lab] = float(np.mean(R["win_beat"])) - float(np.mean(R["lose_beat"]))
    cl, why = risk.classify_diff(cm, "2009~19")
    r = {"class": cl, "answer": "다음 1년 S&P 500 보다 더 남은 몫 (오른 종목 · 내린 종목) — " + " | ".join(f"{k}: {v['S&P 500보다 더 남은 몫 (오른·내린)']}" for k, v in tab.items()) +
                               " · 20% 넘게 더 빠진 적 — " + " | ".join(f"{k}: {v['1년 안에 20% 넘게 더 빠진 적 (오른·내린)']}" for k, v in tab.items()),
         "table": tab, "why": f"{why} · 편향: 내린 종목 쪽에서 무너져 빠진 회사가 없음 — '내린 종목을 남겨도 됐다' 쪽으로 미는 편향"}
    if np.mean(list(cm.values())) < 0 and cl in ("정답형", "차이 작음"):
        return stocks._biased(r, "내린 종목이 더 나음 — 편향과 같은 쪽")
    return r


# ================================================================ 7. 하락장 전 회사 특징
def bear_traits(B, I, P, F):
    """하락장에 덜 빠진 쪽은? — 값으로 아는 특징(직전 1년 많이 오른 종목 vs 덜 오른 종목, 위 20% vs 아래 20%)은 하락장 4번 ·
    재무 특징(흑자 vs 적자 · 빚 ÷ 영업이익 낮음 vs 높음 · PER 낮음 vs 높음)은 2025 하락장 1번 (FY2023 — 그때 알려진 숫자)."""
    i0, o, syms, A = risk.matrix(I, P, start=date(2006, 1, 1))
    out = {"직전 1년 상승률": {}}
    for a, b, name in BEARS:
        ia, ib = int(np.searchsorted(o, _d(a), side="right")) - 1, int(np.searchsorted(o, _d(b), side="right")) - 1
        past = A[ia] / A[ia - YEAR] - 1
        dd = A[ib] / A[ia] - 1
        ok = ~np.isnan(past) & ~np.isnan(dd)
        q20, q80 = np.quantile(past[ok], [0.2, 0.8])
        hi_, lo_ = dd[ok & (past >= q80)], dd[ok & (past <= q20)]
        out["직전 1년 상승률"][name] = {"많이 오른 20%": pct(float(np.median(hi_))), "덜 오른 20%": pct(float(np.median(lo_))), "n": int(ok.sum()),
                                   "덜 빠진 쪽": "많이 오른 쪽" if np.median(hi_) > np.median(lo_) else "덜 오른 쪽"}
    a, b = "2025-02-19", "2025-04-08"
    ia, ib = int(np.searchsorted(o, _d(a), side="right")) - 1, int(np.searchsorted(o, _d(b), side="right")) - 1
    F2 = {}
    for fp in (stocks.BULK / "fa2").glob("*.json"):
        F2[fp.stem] = json.loads(fp.read_text("utf-8"))["series"]

    def fy(series, sym, key):
        v = (series.get(sym) or {}).get(key) or {}
        ks = [k for k in v if _d(k) + 75 <= _d(a)]
        return v[max(ks)] if ks else None
    rows = []
    for j, s in enumerate(syms):
        if np.isnan(A[ia, j]) or np.isnan(A[ib, j]):
            continue
        ni, eps = fy(F, s, "annualNetIncome"), fy(F, s, "annualDilutedEPS")
        debt, ebit = fy(F2, s, "annualTotalDebt"), fy(F2, s, "annualEBIT")
        price = P[s].at(_d(a), "close")
        rows.append((s, A[ib, j] / A[ia, j] - 1, ni, (debt / ebit) if (debt is not None and ebit and ebit > 0) else None, (price / eps) if (eps and eps > 0) else None))
    dd = np.array([r[1] for r in rows])
    fin = {}
    prof = [r[1] for r in rows if r[2] is not None and r[2] > 0]
    loss = [r[1] for r in rows if r[2] is not None and r[2] <= 0]
    fin["흑자 vs 적자"] = {"흑자": pct(float(np.median(prof))), "적자": pct(float(np.median(loss))), "n": f"{len(prof)} · {len(loss)}"}
    for idx, lab, lowname, highname in ((3, "빚 ÷ 영업이익", "빚 적은 20%", "빚 많은 20%"), (4, "PER", "PER 낮은 20%", "PER 높은 20%")):
        v = [(r[idx], r[1]) for r in rows if r[idx] is not None]
        x = np.array([t[0] for t in v])
        y = np.array([t[1] for t in v])
        q20, q80 = np.quantile(x, [0.2, 0.8])
        fin[lab] = {lowname: pct(float(np.median(y[x <= q20]))), highname: pct(float(np.median(y[x >= q80]))), "n": len(v)}
    out["2025 하락장 재무 특징 (FY2023)"] = {"window": f"{a} → {b}", "S&P 500": pct(I.at(_d(b), I.px) / I.at(_d(a), I.px) - 1), "전체 중앙값": pct(float(np.median(dd))), **fin}
    mom = out["직전 1년 상승률"]
    flips = len({v["덜 빠진 쪽"] for v in mom.values()}) > 1
    return {"class": "조건부형" if flips else "사실형",
            "answer": "직전 1년 많이 오른 20% vs 덜 오른 20% 하락장 중앙값 — " + " · ".join(f"{k}: {v['많이 오른 20%']} vs {v['덜 오른 20%']}" for k, v in mom.items()) +
                      " | 2025 (FY2023): 흑자 {흑자} vs 적자 {적자} · ".format(**fin["흑자 vs 적자"]) +
                      " · ".join(f"{k} " + " vs ".join(f"{kk} {vv}" for kk, vv in v.items() if kk != "n") for k, v in fin.items() if k != "흑자 vs 적자"),
            "table": out, "why": ("직전 상승률은 하락장마다 덜 빠진 쪽이 바뀜 — 조건부" if flips else "직전 상승률은 4번 모두 같은 쪽") +
                                 " · 재무 특징은 2025 한 번뿐(자료가 FY2022 부터 — 2022 하락장은 그때 몰랐던 숫자라 안 씀) · 편향: 무너져 빠진 회사가 없어 약한 쪽(적자·빚 많음)을 좋게 보는 쪽"}


# ================================================================ 8. 장중 vs 밤사이
def _open_close(sym):
    """SPY 시가·종가 (배당·분할 반영 안 한 값 — 같은 날 안의 비율이라 분할은 상관없음 · 배당락은 밤사이 몫을 조금 낮춤)."""
    path = DATA / f"{sym}_oc.csv"
    if not path.exists():
        url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(sym)}?period1=725846400&period2={int(time.time())}&interval=1d")
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=60) as r:
            res = json.load(r)["chart"]["result"][0]
        q = res["indicators"]["quote"][0]
        rows = [(datetime.fromtimestamp(t, tz=timezone.utc).date().isoformat(), op, cl) for t, op, cl in zip(res["timestamp"], q["open"], q["close"]) if op and cl]
        with path.open("w", encoding="utf-8", newline="") as f:
            f.write(f"# {sym} 일별 시가·종가 — Yahoo Finance chart API v8 (분할 반영 · 배당 반영 안 함), {date.today().isoformat()} 받음 · round4.py {VERSION}\n")
            w = csv.writer(f)
            w.writerow(["date", "open", "close"])
            w.writerows(rows)
    with path.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(ln for ln in f if not ln.startswith("#")))
    return [r["date"] for r in rows], np.array([float(r["open"]) for r in rows]), np.array([float(r["close"]) for r in rows])


def overnight(B, I, P, F):
    """SPY — 장중(그날 시가 → 종가)만 들고 있기 vs 밤사이(전날 종가 → 그날 시가)만 들고 있기 vs 계속 들고 있기 · 1만 달러 · 시기별."""
    ds, op, cl = _open_close("SPY")
    intra = cl / op
    night = np.concatenate([[1.0], op[1:] / cl[:-1]])
    yrs = np.array([int(x[:4]) for x in ds])
    out = {}
    for lab, y0, y1 in (("2000~2009", 2000, 2009), ("2010~2019", 2010, 2019), ("2020~2026", 2020, 2026), ("2000~2026", 2000, 2026)):
        m = (yrs >= y0) & (yrs <= y1)
        out[lab] = {"장중만": usd(10000 * float(np.prod(intra[m]))), "밤사이만": usd(10000 * float(np.prod(night[m]))), "계속 (가격만)": usd(10000 * float(np.prod(intra[m] * night[m]))),
                    "장중이 오른 날 몫": pct(float(np.mean(intra[m] > 1)))}
    night_wins = [k for k, v in out.items() if k != "2000~2026" and float(v["밤사이만"].replace(",", "").replace("달러", "")) > float(v["장중만"].replace(",", "").replace("달러", ""))]
    return {"class": "사실형" if len(night_wins) == 3 else "조건부형",
            "answer": "SPY 1만 달러 (가격만) — " + " | ".join(f"{k}: 장중만 {v['장중만']} · 밤사이만 {v['밤사이만']} · 계속 {v['계속 (가격만)']}" for k, v in out.items()) +
                      f" — 밤사이가 더 남은 시기 {len(night_wins)}/3",
            "table": out, "first_day": ds[0], "why": "지수 ETF — 생존 편향 없음 · 수수료·세금 없음 · 배당은 빠짐(밤사이 몫을 조금 낮게 보는 쪽)"}


TOPICS4 = {"R4_stop": stop_loss, "R4_crash": crash_buy, "R4_rivals": rivals, "R4_sector": sector_bear, "R4_chase": sector_chase,
           "R4_winlose": winners_losers, "R4_traits": bear_traits, "R4_night": overnight}
