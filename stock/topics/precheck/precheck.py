#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-10-29 — 2회차 (사용자 지시 2026-10-29 "주식 주제 평가판 평가했는데 다시 주제 탐색해봐"): 새 후보 T027~T039 · 다시 짠 좋음 주제
#          T003·T011·T012·T022 를 stocks.py(지금 S&P 500 구성 종목 일괄 자료 — bulk.py 캐시)로 계산 · --tag (결과 파일 이름 뒤) · --selftest-stocks ·
#          옛 T003(가장 오른 10일) 은 T003_r1 로 남김 · NO_DATA 에서 T011·T012·T022 뺌 (이제 계산).
# (v1.0 — 2026-10-29 — 최초. 주제 '정답 미리 확인' (사용자 지시 2026-10-29 "그렇게 절차정하고 주제 걸러봐 기존 3개도 확인해서").
#          요약본을 쓰기 전에 후보마다 실제 자료로 결론이 기간·시작 시기·가정을 바꿔도 같은지 계산한다 (절차: stock/topics/README.md '정답 미리 확인').)
#
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.1 | 2026-10-29 | 2회차 — stocks.py 연결(TOPICS2) · --tag · --selftest-stocks · T003_r1 · NO_DATA 줄임 | main · TOPICS · NO_DATA |
# | v1.0 | 2026-10-29 | 최초 (같은 날 고침: classify_full — 앞 시기 자료가 없으면 정답형 ✗ · T007 JEPI 예외 적음) — 받기(캐시) · 비교 칸(기간 × 시작 시기 × 가정) · 주제 26개 + 기존 2편(포트폴리오 항목) 계산 · JSON | 전부 |
#
# 실행: python3 -B stock/topics/precheck/precheck.py            (캐시 CSV 가 없으면 Yahoo 에서 받음 — 있으면 네트워크 안 씀)
#       python3 -B stock/topics/precheck/precheck.py --refetch  (모두 다시 받기)
# 자료: Yahoo Finance chart API v8 (일별 · 수정 종가 adjclose = 배당·분할 반영) — data/<기호>.csv. 지수 ^SP500TR·^GSPC·^IRX 는 매수 시기 편 calc 의 CSV 를 그대로 씀.
# 미리 보기 점검: 모든 규칙은 그날 종가까지 알려진 값으로만 정한다 (calc 와 같음).
# 분류 (계산 전에 정함 — README 와 같음):
#   정답형  = 비교의 이긴 쪽이 모든 칸(기간 2·5년 · 시작 2000~08 / 2009~ · 가정 바꿈)에서 같고, 가장 약한 칸도 55% 이상 · 기본 칸 60% 이상
#   차이없음 = 모든 칸에서 45~55% 이고 금액 차이도 작음 → "차이가 없다"가 정답 (정답형의 한 갈래)
#   조건부형 = 칸에 따라 이긴 쪽이 바뀜 → 정답을 맞히는 꼴(테스트·문제의 '정답') ✗, 비교·내기의 크기로만
#   사실형  = 지난 한 구간의 숫자 (몇 년·몇 %) — 숫자 자체는 분명, 규칙으로 넓히면 안 됨
#   계산형  = 법·수식으로 정해짐 — 가정 범위에서 같은지만 확인 (법령 원문 확인은 따로)
#   미확인  = 자료가 이 환경에 없음 (무엇이 필요한지 적음)
# ※ 연구·교육용 — 투자 권유가 아님.
import argparse
import csv
import json
import logging
import sys
import time
import urllib.parse
import urllib.request
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
DATA = HERE / "data"
TIMING = ROOT / "stock" / "source" / "timing-test-2026-10" / "calc"
sys.path.insert(0, str(TIMING))
sys.path.insert(0, str(ROOT / "tools"))
import calc as T  # noqa: E402  매수 시기 편 calc (month_starts · windows · cash_index · align_irx · load · big_declines)
import stocks  # noqa: E402  v1.1 2회차 — 지금 S&P 500 구성 종목 자료로 계산하는 주제 (TOPICS2)

VERSION = "v1.1"
EARLY, LATE_FROM = (2000, 2008), 2009
MAIN_MIN, CELL_MIN = 0.60, 0.55


class StageFormatter(logging.Formatter):
    def format(self, record):
        return f"[{getattr(record, 'stage', 'PRE')}] [{self.formatTime(record, '%Y-%m-%dT%H:%M:%S')}] {record.getMessage()}"


log = logging.getLogger("topic-precheck")


def out(stage, **kv):
    log.info(" ".join(f"{k}={v}" for k, v in kv.items()), extra={"stage": stage})


def warn(stage, **kv):
    log.warning(" ".join(f"{k}={v}" for k, v in kv.items()), extra={"stage": stage})


def pct(x):
    return f"{x * 100:.1f}%"


# ---------- 받기 (캐시) ----------
def fetch(symbol, refetch=False, start=date(1999, 1, 1)):
    """수정 종가(adjclose)와 배당 — data/<기호>.csv 가 있으면 읽기만."""
    path = DATA / f"{symbol.replace('^', '_').replace('=', '_')}.csv"
    if path.exists() and not refetch:
        return read_csv(path, symbol)
    p1 = int(datetime(start.year, start.month, start.day, tzinfo=timezone.utc).timestamp())
    url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(symbol)}"
           f"?period1={p1}&period2={int(time.time())}&interval=1d&events=div%2Csplit")
    last = None
    for wait in (0, 2, 4, 8):
        time.sleep(wait)
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=60) as r:
                res = json.load(r)["chart"]["result"][0]
            ts_ = res["timestamp"]
            q = res["indicators"]["quote"][0]["close"]
            adj = res["indicators"].get("adjclose", [{}])[0].get("adjclose", q)
            divs = {datetime.fromtimestamp(int(k), tz=timezone.utc).date().isoformat(): v["amount"]
                    for k, v in res.get("events", {}).get("dividends", {}).items()}
            rows = [(datetime.fromtimestamp(t, tz=timezone.utc).date().isoformat(), c, a) for t, c, a in zip(ts_, q, adj) if c is not None and a is not None]
            DATA.mkdir(parents=True, exist_ok=True)
            with path.open("w", encoding="utf-8", newline="") as f:
                f.write(f"# {symbol} 일별 — Yahoo Finance chart API v8 (close · adjclose 배당·분할 반영 · div 그날 배당), {date.today().isoformat()} 받음 · precheck.py {VERSION}\n")
                w = csv.writer(f)
                w.writerow(["date", "close", "adjclose", "div"])
                w.writerows((d_, f"{c:.6f}", f"{a:.6f}", divs.get(d_, "")) for d_, c, a in rows)
            out("FETCH", symbol=symbol, rows=len(rows), first=rows[0][0], last=rows[-1][0], divs=len(divs))
            return read_csv(path, symbol)
        except Exception as e:
            last = e
            warn("FETCH", symbol=symbol, error=repr(e)[:120], retry=wait * 2 or 2)
    log.error(f"symbol={symbol} error={last!r} next_step=네트워크 확인 뒤 --refetch", extra={"stage": "FETCH"})
    return None


def read_csv(path, symbol):
    with path.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(line for line in f if not line.startswith("#")))
    d = np.array([date.fromisoformat(r["date"]) for r in rows])
    s = {"d": d, "close": np.array([float(r["close"]) for r in rows]), "adj": np.array([float(r["adjclose"]) for r in rows]),
         "div": np.array([float(r["div"]) if r["div"] else 0.0 for r in rows])}
    out("LOAD", symbol=symbol, rows=len(d), first=d[0], last=d[-1])
    return s


def on(dref, d, v):
    """dref 날짜마다 그날까지 알려진 마지막 값 (앞 값 채움 · 첫 날 전은 nan)."""
    idx = np.searchsorted(d, dref, side="right") - 1
    x = v[np.clip(idx, 0, None)].astype(float)
    x[idx < 0] = np.nan
    return x


# ---------- 비교 칸 ----------
def cells(a, b, st, d, horizon):
    """a(미루지 않은 쪽·첫 쪽) 가 b 를 이긴 몫 — 전체 · 앞(2000~08 시작) · 뒤(2009~)."""
    y = np.array([d[i].year for i in st])
    res = {}
    for name, m in (("all", np.ones(len(st), bool)), ("early", (y >= EARLY[0]) & (y <= EARLY[1])), ("late", y >= LATE_FROM)):
        res[name] = {"n": int(m.sum()), "a_wins": float(np.mean(a[m] > b[m])) if m.sum() else None,
                     "mean_diff_pct": float(np.mean(a[m] / b[m] - 1)) if m.sum() else None}
    return {horizon: res}


def classify(cellmap):
    """cellmap: {칸 이름: a 가 이긴 몫} → 정답형(a/b) · 차이없음 · 조건부형."""
    v = [x for x in cellmap.values() if x is not None]
    if not v:
        return "미확인", "칸 없음"
    if all(x >= 0.5 for x in v) and min(v) >= CELL_MIN and max(v) >= MAIN_MIN:
        return "정답형", f"첫 쪽 — 가장 약한 칸 {pct(min(v))}"
    if all(x <= 0.5 for x in v) and max(v) <= 1 - CELL_MIN and min(v) <= 1 - MAIN_MIN:
        return "정답형", f"둘째 쪽 — 가장 약한 칸 {pct(1 - max(v))}"
    if all(0.45 <= x <= 0.55 for x in v):
        return "차이없음", f"모든 칸 {pct(min(v))}~{pct(max(v))}"
    return "조건부형", f"칸에 따라 {pct(min(v))}~{pct(max(v))}"


def classify_full(cellmap):
    """classify + 시작 시기 검사가 빠진 경우(앞 시기 자료 없음)는 정답형으로 보지 않음."""
    cl, why = classify(cellmap)
    if cl in ("정답형", "차이없음") and not any("앞" in k for k in cellmap):
        return "미확인", f"{cl} 쪽이지만 2009년 이후 자료뿐 (하락기 검사 못 함) — {why}"
    return cl, why


def flat(c):
    """{h: {all/early/late: {...}}} → {'5y·앞': a_wins, …}"""
    lab = {"all": "전체", "early": "앞", "late": "뒤"}
    return {f"{h}·{lab[k]}": v["a_wins"] for h, r in c.items() for k, v in r.items() if v["n"] >= 12}


# ---------- 공통 자료 ----------
class Base:
    def __init__(self, refetch):
        self.d, self.tr = T.load("sp500tr")
        gd, gp = T.load("gspc")
        idd, iv = T.load("irx")
        self.gd, self.gp = gd, gp
        self.irx = T.align_irx(self.d, idd, iv)
        self.cash = T.cash_index(self.d, self.irx)
        self.cash5 = np.cumprod(1 + 0.05 * np.array([0] + [(self.d[i] - self.d[i - 1]).days for i in range(1, len(self.d))], dtype=float) / 365)
        self.ms, self.mk = T.month_starts(self.d)
        self.W = {h: T.windows(self.ms, self.mk, self.d, m) for h, m in (("2y", 24), ("5y", 60), ("10y", 120))}
        self.price = on(self.d, gd, gp)
        self.refetch = refetch

    def series(self, sym, field="adj"):
        s = fetch(sym, self.refetch)
        return None if s is None else on(self.d, s["d"], s[field])


# ---------- 주제마다 ----------
def t001(B):
    """보유 기간별 손실 구간 비율 (배당 포함 · 매달 시작)."""
    rows = {}
    for H in (1, 3, 5, 7, 10, 12, 15, 20):
        W = T.windows(B.ms, B.mk, B.d, 12 * H)
        if not W:
            continue
        st = np.array([s for s, e, _ in W])
        loss = np.array([B.tr[e] < B.tr[s] for s, e, _ in W])
        lossp = np.array([B.price[e] < B.price[s] for s, e, _ in W])
        y = np.array([B.d[s].year for s in st])
        rows[f"{H}y"] = {"n": len(W), "last_start": B.d[st[-1]].isoformat(), "loss": float(loss.mean()), "loss_price": float(lossp.mean()),
                         "loss_early": float(loss[y <= 2008].mean()) if (y <= 2008).any() else None,
                         "loss_late": float(loss[y >= 2009].mean()) if (y >= 2009).any() else None, "independent": int((2026 - 2000) // H),
                         "loss_starts": sorted({B.d[s].isoformat()[:7] for s, x in zip(st, loss) if x})}
    zero = next((k for k, v in rows.items() if v["loss"] == 0), None)
    return {"class": "사실형", "answer": f"2000년 이후 매달 시작: 손실 구간이 처음 0% 가 되는 보유 기간 = {zero}",
            "why": "지난 한 자료의 숫자 — 겹치지 않는 구간 수가 적어(15년이면 1개) '앞으로도 15년이면 손실 없다'로 넓히면 안 됨",
            "table": rows}


def t002(B):
    """고점에 산 사람이 본전(배당 포함)까지 걸린 햇수 — S&P 500 TR · QQQ(수정 종가)."""
    qqq = B.series("QQQ")
    out_ = {}
    for name, v in (("S&P500TR", B.tr), ("QQQ", qqq)):
        r = {}
        for lab, a, b in (("2000", date(2000, 1, 1), date(2000, 12, 31)), ("2007", date(2007, 1, 1), date(2008, 6, 30)), ("2021", date(2021, 6, 1), date(2022, 6, 30))):
            m = np.flatnonzero((B.d >= a) & (B.d <= b) & ~np.isnan(v))
            i = m[np.argmax(v[m])]
            back = np.flatnonzero(v[i + 1:] >= v[i])
            r[lab] = {"peak": B.d[i].isoformat(), "years": round((B.d[i + 1 + back[0]] - B.d[i]).days / 365.25, 1) if len(back) else None}
        out_[name] = r
    longer = {k: ("QQQ" if (out_["QQQ"][k]["years"] or 99) > (out_["S&P500TR"][k]["years"] or 99) else "S&P") for k in ("2000", "2007", "2021")}
    return {"class": "사실형", "answer": "고점 세 번의 본전까지 햇수 (아래 표)", "longer": longer,
            "why": "숫자는 분명 · '나스닥이 더 오래 걸린다'는 2000년에만 맞음 (2007·2021 은 반대이거나 비슷) → 규칙으로 말하면 조건부", "table": out_}


def t003_r1(B):
    """(1회차 T003 — 2회차에서 주제를 다시 짜 stocks.t003 으로 바꿈) 가장 오른 10일 · 가장 빠진 10일을 놓치면 (2006-10-27 ~ 2026-10-27, 배당 포함 · 놓친 날은 수익 0)."""
    i0 = int(np.searchsorted(B.d, date(2006, 10, 27)))
    r = B.tr[i0 + 1:] / B.tr[i0:-1] - 1
    order = np.argsort(r)
    best, worst = order[-10:], order[:10]
    def total(skip):
        rr = r.copy()
        rr[list(skip)] = 0.0
        return float(np.prod(1 + rr))
    allx = total([])
    near = int(sum(any(abs(int(b) - int(w)) <= 10 for w in order[:20]) for b in best))
    return {"class": "조건부형", "answer": f"놓친 날에 따라: 전부 {allx:.2f}배 · 최고 10일 놓침 {total(best):.2f}배 · 최악 10일 놓침 {total(worst):.2f}배 · 둘 다 놓침 {total(np.concatenate([best, worst])):.2f}배",
            "best_near_worst20_within_10days": f"{near}/10",
            "why": "'최고의 날만 놓친다'는 가정이 결론을 만듦 — 같이 붙어 있는 최악의 날도 피하면 결과가 뒤집힘. 실제 '판 사람' 규칙(10% 빠지면 팔고 N개월 뒤)은 매수 시기 편 calc 에서 시작 시기에 따라 뒤집힘(qz_sell6) → 테스트의 정답으로 쓰면 안 됨"}


def t004(B):
    """5% 오르면 팔고(양도세 22% · 수수료 0.25%), 판 값보다 3% 빠지면 다시 사기 vs 보유 (끝에 둘 다 세후로 정산 · 밖에 있는 돈은 국채 이자)."""
    res = {}
    for tax in (0.22, 0.0):
        A, Bv, ST = [], [], {}
        for h in ("2y", "5y"):
            a_, b_, st_ = [], [], []
            for s, e, _ in B.W[h]:
                fee = 0.0025
                inm, units, cost = True, (1 - fee) / B.tr[s], 1.0          # 산 금액(세금 기준) = 1
                cash, sale_px = 0.0, None
                for i in range(s + 1, e + 1):
                    if inm and B.tr[i] >= cost / units * 1.05:              # 산 값보다 5% 위 → 매도
                        v = units * B.tr[i] * (1 - fee)
                        cash = v - tax * max(v - cost, 0)
                        inm, sale_px, cash_t = False, B.tr[i], i
                    elif not inm and B.tr[i] <= sale_px * 0.97:             # 판 값보다 3% 아래 → 다시 매수
                        cash *= B.cash[i] / B.cash[cash_t]
                        units, cost, inm = cash * (1 - fee) / B.tr[i], cash, True
                if inm:
                    v = units * B.tr[e] * (1 - fee)
                    rule = v - tax * max(v - cost, 0)
                else:
                    rule = cash * B.cash[e] / B.cash[cash_t]
                hv = (1 - fee) / B.tr[s] * B.tr[e] * (1 - fee)
                hold = hv - tax * max(hv - 1, 0)
                a_.append(hold); b_.append(rule); st_.append(s)
            ST.update(cells(np.array(a_), np.array(b_), np.array(st_), B.d, h))
        res["tax22" if tax else "notax"] = ST
    fm = {**{f"세22·{k}": v for k, v in flat(res["tax22"]).items()}, **{f"세0·{k}": v for k, v in flat(res["notax"]).items()}}
    cl, why = classify_full(fm)
    return {"class": cl, "answer": "보유(첫 쪽)가 이긴 몫 — 칸별 아래", "cells": fm, "why": why}


def t005(B):
    """매달 같은 금액 적립: S&P 500 TR vs 국채(예금) — 5·10·15년 · 물가 연 2.5% 로 불린 원금과도."""
    res, fm = {}, {}
    for H in (5, 10, 15):
        W = T.windows(B.ms, B.mk, B.d, 12 * H)
        a, b, c_, st = [], [], [], []
        for s, e, buys in W:
            a.append(sum(B.tr[e] / B.tr[x] for x in buys))
            b.append(sum(B.cash[e] / B.cash[x] for x in buys))
            c_.append(sum(1.025 ** ((B.d[e] - B.d[x]).days / 365.25) for x in buys))
            st.append(s)
        a, b, c_, st = map(np.array, (a, b, c_, st))
        y = np.array([B.d[s].year for s in st])
        res[f"{H}y"] = {"n": len(W), "vs_bill": float(np.mean(a > b)), "vs_cpi25": float(np.mean(a > c_)),
                        "vs_bill_early": float(np.mean((a > b)[y <= 2008])), "vs_bill_late": float(np.mean((a > b)[y >= 2009])) if (y >= 2009).any() else None,
                        "lost_starts": sorted({B.d[s].year for s, x in zip(st, a > b) if not x})}
        fm.update({f"{H}y·전체": res[f"{H}y"]["vs_bill"], f"{H}y·앞": res[f"{H}y"]["vs_bill_early"]})
        if res[f"{H}y"]["vs_bill_late"] is not None:
            fm[f"{H}y·뒤"] = res[f"{H}y"]["vs_bill_late"]
    cl, why = classify_full(fm)
    return {"class": cl, "answer": "적립(첫 쪽)이 국채 적립을 이긴 몫", "cells": fm, "table": res, "why": why + " · 물가는 원자료(FRED·BLS)가 이 환경에서 막혀 연 2.5% 가정"}


def t006(B):
    """환노출(달러 수익 × 원/달러) vs 환헤지(달러 수익 + 금리 차 d) — d = −1.5 · 0 · +1.5%/년 (한미 금리 차 원자료 없음)."""
    fx = B.series("KRW=X", "close")
    fm = {}
    for dlt in (-0.015, 0.0, 0.015):
        for h in ("2y", "5y"):
            a, b, st = [], [], []
            for s, e, _ in B.W[h]:
                if np.isnan(fx[s]) or B.d[s] < date(2010, 1, 1):
                    continue
                yrs = (B.d[e] - B.d[s]).days / 365.25
                a.append(B.tr[e] / B.tr[s] * fx[e] / fx[s]); b.append(B.tr[e] / B.tr[s] * (1 + dlt) ** yrs); st.append(s)
            fm[f"차{dlt * 100:+.1f}%·{h}"] = float(np.mean(np.array(a) > np.array(b)))
    cl, why = classify_full(fm)
    return {"class": cl, "answer": "환노출(첫 쪽)이 이긴 몫 (2010~ 시작)", "cells": fm, "why": why + " · 원/달러가 오른 구간이면 환노출, 내린 구간이면 환헤지 — 앞날 환율에 거는 것"}


def t007(B):
    """커버드콜(QYLD·XYLD·JEPI) vs 지수(QQQ·SPY): 하락 때 낙폭 · 하락 시작 2년 뒤 (수정 종가)."""
    sy = {k: B.series(k) for k in ("QYLD", "QQQ", "XYLD", "SPY", "JEPI")}
    events = {"2018-10": date(2018, 10, 1), "2020-02": date(2020, 2, 19), "2021-12": date(2021, 12, 27)}
    tab = {}
    for ev, t0 in events.items():
        i = int(np.searchsorted(B.d, t0)); j = int(np.searchsorted(B.d, t0 + timedelta(days=730)))
        k = min(j, len(B.d) - 1)
        row = {}
        for nm, v in sy.items():
            if np.isnan(v[i]):
                continue
            seg = v[i:k + 1]
            row[nm] = {"mdd": float(np.min(seg / np.maximum.accumulate(seg) - 1)), "ret2y": float(v[k] / v[i] - 1)}
        tab[ev] = row
    ok = all(r["QYLD"]["mdd"] > r["QQQ"]["mdd"] and r["QYLD"]["ret2y"] < r["QQQ"]["ret2y"] for r in tab.values() if "QYLD" in r)
    jepi = tab.get("2021-12", {}).get("JEPI"), tab.get("2021-12", {}).get("SPY")
    note = (" · 단 2021-12 JEPI 는 SPY 보다 덜 빠지고(" + pct(jepi[0]["mdd"]) + " vs " + pct(jepi[1]["mdd"]) + ") 2년 뒤도 더 남음(" + pct(jepi[0]["ret2y"]) + " vs " + pct(jepi[1]["ret2y"]) + ") → 'QYLD vs QQQ' 로만, 커버드콜 전부로 넓히면 안 됨") if all(jepi) else ""
    return {"class": "정답형" if ok else "조건부형", "answer": "하락 세 번 모두 'QYLD 가 덜 빠지고, 2년 뒤엔 QQQ 가 더 남음'" if ok else "하락마다 다름",
            "table": tab, "why": "구조(오를 몫을 팔아 분배)에서 나오는 결과라 세 번 모두 같은 쪽인지 봄" + note}


def t008(B):
    """배당 재투자(TR) vs 가격 지수 — 2000-01 → 끝 · 10년 구간 최소·최대."""
    s, e = int(np.searchsorted(B.d, date(2000, 1, 3))), len(B.d) - 1
    full = float((B.tr[e] / B.tr[s]) / (B.price[e] / B.price[s]))
    r10 = [(B.tr[e_] / B.tr[s_]) / (B.price[e_] / B.price[s_]) for s_, e_, _ in B.W["10y"]]
    return {"class": "정답형", "answer": f"2000-01 → {B.d[e]}: 배당 포함이 가격 지수의 {full:.2f}배 · 10년 구간 {min(r10):.2f}~{max(r10):.2f}배 (늘 1 넘음)",
            "why": "수식으로 늘 성립 (배당 ≥ 0) · 다만 '쓴 사람'은 쓴 배당을 이미 썼다는 반론 — 비교는 '남은 돈'만"}


def t013(B, rate=0.08):
    """신용 2배 (자기 돈 1 + 빌린 돈 1, 연 rate) · 담보 비율 = 주식 값 ÷ 빚 < 140% 면 반대매매 — 2년 안에 닿은 구간 비율."""
    fm = {}
    for rt in (0.08, 0.05):
        hit, st = [], []
        for s, e, _ in B.W["2y"]:
            a = 2 * B.tr[s:e + 1] / B.tr[s]
            debt = (1 + rt) ** (np.array([(x - B.d[s]).days for x in B.d[s:e + 1]]) / 365)
            hit.append(bool(np.any(a / debt < 1.4))); st.append(s)
        hit, st = np.array(hit), np.array(st)
        y = np.array([B.d[s].year for s in st])
        fm.update({f"금리{rt * 100:.0f}%·전체": float(hit.mean()), f"금리{rt * 100:.0f}%·앞": float(hit[y <= 2008].mean()), f"금리{rt * 100:.0f}%·뒤": float(hit[y >= 2009].mean())})
    return {"class": "사실형", "answer": "2년 안 반대매매 선에 닿은 구간 비율 (칸별)", "cells": fm,
            "why": "비율이 시기에 따라 크게 다름 — '흔하다'는 앞 시기 숫자, 뒤 시기는 훨씬 적음 → 결론은 시기와 함께 말해야 함"}


def t014(B):
    """은퇴해 해마다 처음 금액의 4% 를 꺼냄 (물가 연 2.5%·2%·3.5% 로 늘림) — 은퇴한 해별로 끝에 남은 금액 (처음 = 1)."""
    tab = {}
    for infl in (0.02, 0.025, 0.035):
        row = {}
        for Y in range(2000, 2017):
            i = int(np.searchsorted(B.d, date(Y, 1, 1)))
            bal, wd = 1.0, 0.04
            for k in range(Y, 2026):
                a = int(np.searchsorted(B.d, date(k, 1, 1))); b = int(np.searchsorted(B.d, date(k + 1, 1, 1)))
                bal = (bal - wd) * B.tr[min(b, len(B.d) - 1)] / B.tr[a]
                wd *= 1 + infl
                if bal <= 0:
                    bal = 0.0
                    break
            row[Y] = round(bal, 2)
        tab[f"물가{infl * 100:.1f}%"] = row
    r = tab["물가2.5%"]
    return {"class": "사실형", "answer": f"2000년 은퇴 {r[2000]} · 2009년 {r[2009]} · 2010년 {r[2010]} (처음 = 1, 2026년 초 기준 · 100% 주식)",
            "table": tab, "why": "'은퇴한 해에 따라 갈린다'가 바로 결론 — 조건부를 숨기지 않는 사실형 (60/40 은 채권 원자료가 2003년부터라 빼고 100% 주식만)"}


def t016(B):
    """반도체 지수(^SOX 가격) vs S&P 500(가격): 하락장 세 번의 최대 낙폭 · 2000 고점 본전 햇수."""
    sox = B.series("^SOX", "close")
    tab = {}
    for lab, a, b in (("2000~02", date(2000, 1, 1), date(2003, 3, 31)), ("2007~09", date(2007, 7, 1), date(2009, 6, 30)), ("2022", date(2021, 11, 1), date(2022, 12, 31))):
        m = (B.d >= a) & (B.d <= b)
        row = {}
        for nm, v in (("SOX", sox), ("S&P500", B.price)):
            seg = v[m]
            row[nm] = float(np.min(seg / np.maximum.accumulate(seg) - 1))
        row["ratio"] = round(row["SOX"] / row["S&P500"], 2)
        tab[lab] = row
    ok2 = all(r["ratio"] >= 2 for r in tab.values())
    return {"class": "사실형", "answer": "하락장 세 번 낙폭 비 (SOX ÷ S&P) — " + " · ".join(f"{k} {v['ratio']}배" for k, v in tab.items()),
            "two_x_every_time": ok2, "table": tab, "why": "'2배 넘게'가 세 번 모두 맞는지가 결론의 성패"}


def t017(B):
    """일부 종목만 (목록 원자료 없음): 2022년 고점 대비 −50% 넘게 빠진 큰 나스닥 종목 몇 곳 — 2024-12 말 종가가 2021년 고점 이상인가."""
    names = ["META", "NFLX", "AMZN", "TSLA", "NVDA", "PYPL", "ZM", "DOCU", "MRNA", "LCID", "ILMN", "WBD"]
    rows = {}
    for nm in names:
        v = B.series(nm, "close")
        if v is None:
            continue
        m21 = (B.d >= date(2021, 1, 1)) & (B.d <= date(2021, 12, 31))
        m22 = (B.d >= date(2022, 1, 1)) & (B.d <= date(2022, 12, 31))
        if np.all(np.isnan(v[m21])):
            continue
        hi = np.nanmax(v[m21]); lo = np.nanmin(v[m22])
        i24 = int(np.searchsorted(B.d, date(2024, 12, 31), side="right")) - 1
        rows[nm] = {"fell": round(float(lo / hi - 1), 2), "recovered_2024": bool(v[i24] >= hi)}
    fell = {k: v for k, v in rows.items() if v["fell"] <= -0.5}
    rec = sum(v["recovered_2024"] for v in fell.values())
    return {"class": "미확인", "answer": f"고른 {len(fell)}곳 중 2024년 말 회복 {rec}곳 (목록 일부 — 결론 판정 못 함)", "table": rows,
            "why": "그때 나스닥 100 구성 목록 원자료가 없음 · 큰 종목은 다수 회복 → 후보 결론('3분의 1 아래')이 틀렸을 가능성"}


def t020(B):
    """커버드콜 ETF: 최근 12개월 분배율(시작 때) 순위 vs 2년 총수익 순위 — 2023-10 시작 · 2022-01 시작."""
    syms = ["QYLD", "XYLD", "RYLD", "JEPI", "JEPQ", "SPYI", "DIVO"]
    data = {s: fetch(s, B.refetch) for s in syms}
    res = {}
    for lab, t0 in (("2022-01", date(2022, 1, 3)), ("2023-10", date(2023, 10, 2))):
        yl, tr = [], []
        for s, x in data.items():
            if x is None or x["d"][0] > t0 - timedelta(days=365):
                continue
            i = int(np.searchsorted(x["d"], t0)); j = int(np.searchsorted(x["d"], t0 + timedelta(days=730)))
            j = min(j, len(x["d"]) - 1)
            dv = x["div"][(x["d"] > x["d"][i] - timedelta(days=365)) & (x["d"] <= x["d"][i])].sum()
            yl.append(dv / x["close"][i]); tr.append(x["adj"][j] / x["adj"][i] - 1)
        if len(yl) >= 3:
            rk = lambda z: np.argsort(np.argsort(z))
            res[lab] = {"n": len(yl), "rank_corr": round(float(np.corrcoef(rk(yl), rk(tr))[0, 1]), 2)}
    neg = all(v["rank_corr"] < 0 for v in res.values())
    return {"class": "정답형" if neg and len(res) == 2 else "조건부형", "answer": "분배율 순위와 2년 총수익 순위의 상관 — " + " · ".join(f"{k}: {v['rank_corr']} ({v['n']}개)" for k, v in res.items()),
            "why": "ETF 수가 적어(4~7개) 순위 상관은 흔들림 · 두 시작 시점에서 같은 부호인지만 봄"}


def t021(B):
    """금(GC=F 선물 종가) vs S&P 500 TR — 매달 시작 5·10년 구간 · 시작 시기별."""
    gold = B.series("GC=F", "close")
    fm = {}
    for h in ("5y", "10y"):
        a, b, st = [], [], []
        for s, e, _ in B.W[h]:
            if np.isnan(gold[s]):
                continue
            a.append(B.tr[e] / B.tr[s]); b.append(gold[e] / gold[s]); st.append(s)
        c = cells(np.array(a), np.array(b), np.array(st), B.d, h)
        fm.update(flat(c))
    s0 = int(np.flatnonzero(~np.isnan(gold))[0])
    full = {"from": B.d[s0].isoformat(), "sp_tr_x": round(float(B.tr[-1] / B.tr[s0]), 2), "gold_x": round(float(gold[-1] / gold[s0]), 2)}
    cl, why = classify_full(fm)
    return {"class": cl, "answer": "S&P 500(첫 쪽)이 금을 이긴 몫", "cells": fm, "full": full, "why": why}


def t023(B):
    """ARKK vs S&P 500 TR — 2015년부터 매달 시작한 2년 구간 · 2021-02 고점 하나."""
    ark = B.series("ARKK")
    a, b, st = [], [], []
    for s, e, _ in B.W["2y"]:
        if np.isnan(ark[s]):
            continue
        a.append(B.tr[e] / B.tr[s]); b.append(ark[e] / ark[s]); st.append(s)
    a, b, st = map(np.array, (a, b, st))
    y = np.array([B.d[s].year for s in st])
    by = {f"{y0}~{y1}": float(np.mean((a > b)[(y >= y0) & (y <= y1)])) for y0, y1 in ((2015, 2018), (2019, 2020), (2021, 2024))}
    return {"class": "조건부형", "answer": "S&P 500 이 ARKK 를 이긴 몫 (시작한 해별) — " + " · ".join(f"{k} {pct(v)}" for k, v in by.items()),
            "why": "2021-02 고점 하나만 고르면 결론이 정해짐 (한 구간의 운) · 시작한 해에 따라 정반대"}


def t024(B):
    """국채 금리(^IRX) 4% 이상인 달에 시작: 2년 S&P 500 TR vs 국채 — 시기별."""
    a, b, st = [], [], []
    for s, e, _ in B.W["2y"]:
        if B.irx[s] < 4.0:
            continue
        a.append(B.tr[e] / B.tr[s]); b.append(B.cash[e] / B.cash[s]); st.append(s)
    a, b, st = map(np.array, (a, b, st))
    y = np.array([B.d[s].year for s in st])
    by = {lab: (float(np.mean((a > b)[m])), int(m.sum())) for lab, m in (("2000~01", y <= 2001), ("2006~07", (y >= 2006) & (y <= 2008)), ("2023~", y >= 2023))}
    return {"class": "조건부형", "answer": "주식이 이긴 몫 — " + " · ".join(f"{k} {pct(v[0])}({v[1]}번)" for k, v in by.items()),
            "why": "'금리가 높아도 주식'은 2023년 한 구간 — 금리 4% 넘던 다른 두 때는 국채가 이김"}


def t025(B):
    """액면분할 1년 뒤 수익 − S&P 500 TR (같은 1년)."""
    ev = [("AAPL", date(2014, 6, 9)), ("AAPL", date(2020, 8, 31)), ("TSLA", date(2020, 8, 31)), ("TSLA", date(2022, 8, 25)), ("NVDA", date(2021, 7, 20)), ("NVDA", date(2024, 6, 10))]
    rows = {}
    for nm, t0 in ev:
        v = B.series(nm)
        i = int(np.searchsorted(B.d, t0)); j = int(np.searchsorted(B.d, t0 + timedelta(days=365)))
        if j >= len(B.d):
            continue
        rows[f"{nm} {t0}"] = round(float((v[j] / v[i]) - (B.tr[j] / B.tr[i])), 2)
    small = all(abs(x) < 0.05 for x in rows.values())
    return {"class": "정답형" if small else "사실형", "answer": "분할 1년 뒤 초과 수익 — " + " · ".join(f"{k} {v:+.0%}" for k, v in rows.items()),
            "why": "'1주 가격은 싸고 비쌈과 무관'(시가총액 = 주가 × 주식 수)은 늘 성립 · '분할 효과 없음(5%p 안)'은 사례마다 크게 갈려 결론으로 못 씀"}


def t026(B):
    """매달 같은 날짜에 적립 (첫 거래일 · 10일 · 20일 · 마지막 거래일 · 배당 포함) — 10년·20년 구간마다 가장 큰 차이."""
    def nth(y, m, kind):
        a = int(np.searchsorted(B.d, date(y, m, 1)))
        b = int(np.searchsorted(B.d, date(y + (m == 12), m % 12 + 1, 1)))
        if kind == "first":
            return a
        if kind == "last":
            return b - 1
        return int(np.searchsorted(B.d, date(y, m, kind)))
    res = {}
    for H in (10, 20):
        diffs = []
        for y0 in range(2000, 2027 - H):
            vals = []
            for kind in ("first", 10, 20, "last"):
                end = int(np.searchsorted(B.d, date(y0 + H, 1, 1))) - 1
                vals.append(sum(B.tr[end] / B.tr[nth(y, m, kind)] for y in range(y0, y0 + H) for m in range(1, 13)))
            diffs.append(max(vals) / min(vals) - 1)
        res[f"{H}y"] = {"n": len(diffs), "max_diff": round(float(max(diffs)), 4), "median_diff": round(float(np.median(diffs)), 4)}
    ok = all(v["max_diff"] < 0.02 for v in res.values())
    return {"class": "정답형" if ok else "조건부형", "answer": "날짜별 적립 최종 금액의 가장 큰 차이 — " + " · ".join(f"{k} 최대 {v['max_diff'] * 100:.2f}% (가운데 {v['median_diff'] * 100:.2f}%)" for k, v in res.items()),
            "why": "'날짜는 거의 상관없다'(차이없음 쪽의 정답) — 모든 시작 해에서 2% 안인지 봄"}


# ---------- 기존 편: 포트폴리오 항목 ----------
def portfolio(B):
    """포트폴리오 편 항목 2~5 — 2년 구간(매달 시작) '수익 ÷ 가장 크게 빠진 폭'이 큰 쪽 · 수익만으로도."""
    qqq, spy, schd, agg, efa = (B.series(s) for s in ("QQQ", "SPY", "SCHD", "AGG", "EFA"))
    r = np.concatenate([[0.0], B.tr[1:] / B.tr[:-1] - 1])
    lev2 = np.cumprod(1 + 2 * r - (B.irx / 100 + 0.009) / 252)            # 2배 레버리지 (빌린 몫 국채 금리 + 총보수 0.9%)
    out_ = {}
    def score(v, s, e):
        seg = v[s:e + 1]
        ret = seg[-1] / seg[0] - 1
        mdd = -np.min(seg / np.maximum.accumulate(seg) - 1)
        return ret, ret / max(mdd, 0.01)
    def mix(parts, s, e, rebal_days=252):                                    # parts: [(값 배열, 비중)] · 1년마다 다시 맞춤
        val = np.ones(e - s + 1)
        w = [wt for _, wt in parts]; units = [wt / v[s] for v, wt in parts]; last = s
        for k, i in enumerate(range(s, e + 1)):
            tot = sum(u * v[i] for u, (v, _) in zip(units, parts))
            val[k] = tot
            if i - last >= rebal_days:
                units = [tot * wt / v[i] for (v, wt) in parts]; last = i
        return val
    items = {
        "2 QQQ만 vs S&P500": lambda s, e: (score(B.tr, s, e), score(qqq, s, e)),
        "3 SCHD만 vs S&P500": lambda s, e: (score(B.tr, s, e), score(schd, s, e)),
        "4 레버리지 2배 10% 섞기 vs 0%": lambda s, e: (score(B.tr, s, e), score(mix([(B.tr, 0.9), (lev2, 0.1)], s, e), 0, e - s)),
        "4b 레버리지 2배 50% 섞기 vs 0%": lambda s, e: (score(B.tr, s, e), score(mix([(B.tr, 0.5), (lev2, 0.5)], s, e), 0, e - s)),
        "5 주식만 vs 주식60·채권20·해외20 (1년마다 맞춤)": lambda s, e: (score(B.tr, s, e), score(mix([(B.tr, 0.6), (agg, 0.2), (efa, 0.2)], s, e), 0, e - s)),
    }
    for name, f in items.items():
        fm = {}
        for h in ("2y", "5y"):
            a_r, b_r, a_s, b_s, st = [], [], [], [], []
            for s, e, _ in B.W[h]:
                try:
                    (ra, sa), (rb, sb) = f(s, e)
                except Exception:
                    continue
                if np.isnan(ra) or np.isnan(rb) or np.isnan(sa) or np.isnan(sb):
                    continue
                a_r.append(ra); b_r.append(rb); a_s.append(sa); b_s.append(sb); st.append(s)
            if not st:
                continue
            fm.update({f"수익÷낙폭·{k}": v for k, v in flat(cells(np.array(a_s), np.array(b_s), np.array(st), B.d, h)).items()})
            fm.update({f"수익·{k}": v for k, v in flat(cells(np.array(a_r), np.array(b_r), np.array(st), B.d, h)).items()})
        cl, why = classify_full({k: v for k, v in fm.items() if k.startswith("수익÷낙폭")})
        out_[name] = {"class": cl, "answer": "S&P 500 만(첫 쪽)이 이긴 몫", "cells": fm, "why": why}
    return out_


TOPICS = {"T001": t001, "T002": t002, "T003_r1": t003_r1, "T004": t004, "T005": t005, "T006": t006, "T007": t007, "T008": t008,
          "T013": t013, "T014": t014, "T016": t016, "T017": t017, "T020": t020, "T021": t021, "T023": t023, "T024": t024, "T025": t025, "T026": t026}
NO_DATA = {  # 계산하지 않은 후보 — 까닭 (분류는 README 기준으로 Claude 가 판단)
    "T009": ("계산형", "법(소득세법·건강보험법 시행령·시행규칙)으로 정해지지만 건보료는 재산·다른 소득에 따라 사람마다 크게 갈림 → 한 사람 예시로만 · 재테크(economic) 쪽 주제"),
    "T010": ("미확인", "2019~2023 공모 규모 상위 20곳 목록 원자료가 필요 (이 환경에 없음) · 결과는 그 5년(2021 거품 포함)에 기대 → 다른 해 묶음도 봐야 함"),
    "T015": ("계산형", "세법 계산 — 공제율(13.2·16.5%) · 수익률(4~10%) · 연금 수령 세율 범위에서 같은 쪽인지 법령 원문과 함께 따로 계산 · 재테크(economic) 쪽과 겹침"),
    "T018": ("계산형", "소득세법 산수(250만 원 공제를 두 해에 두 번) — 결과는 정해짐 · 법령 원문(2026 시행) 확인만 필요"),
    "T019": ("계산형", "총보수 차이 0.5%p × 20년 ≈ 9.5% — 수익률과 상관없이 거의 같음 (수식) · 운용사 공시 보수 확인만 필요"),
}


def selftest_stocks(B, I, P, F):
    """stocks.py 점검 — 자료 크기 · 알려진 분할 · −20% 날 · 1년 비교 함수 · 배당 삭감 판정 (실패하면 1 반환)."""
    from datetime import date as _d
    checks = []
    checks.append(("구성 종목 500개 이상", len(P) >= 500, len(P)))
    a = P.get("AAPL")
    k = np.flatnonzero(a.split >= 2) if a else []
    checks.append(("애플 2020-08-31 4대1 분할", any(_d.fromordinal(int(a.o[i])) == _d(2020, 8, 31) and a.split[i] == 4 for i in k), len(k)))
    ev = stocks.t003(B, I, P, F)["table"]
    checks.append(("−20% 첫날에 2020-03 이 있음", any(r["day"].startswith("2020-03") for r in ev), [r["day"] for r in ev]))
    x = stocks._rel(P["NVDA"], I, I.next_trading(_d(2023, 5, 30).toordinal()))
    checks.append(("엔비디아 2023-05-30 1년 뒤 비교가 계산됨", bool(x) and x[0] > 0, x))
    i = stocks.Px()
    i.o = np.array([_d(2020, m, 1).toordinal() for m in (1, 4, 7, 10)] + [_d(2021, m, 1).toordinal() for m in (1, 4, 7, 10)])
    i.div = np.array([1, 1, 1, 1, 0.5, 0.5, 0.5, 0.5])
    checks.append(("배당 1 → 0.5 를 삭감으로 봄", stocks._cut(i, _d(2020, 12, 31).toordinal(), _d(2021, 12, 31).toordinal()) is not None, None))
    i.div = np.array([1, 1, 1, 1, 1, 1, 1, 1.05])
    checks.append(("배당 그대로면 삭감 아님", stocks._cut(i, _d(2020, 12, 31).toordinal(), _d(2021, 12, 31).toordinal()) is None, None))
    bad = 0
    for name, ok, info in checks:
        (out if ok else warn)("SELFTEST", check=name.replace(" ", "_"), ok=ok, info=str(info)[:100])
        bad += not ok
    out("SELFTEST", passed=len(checks) - bad, failed=bad)
    return 1 if bad else 0


def main():
    ap = argparse.ArgumentParser(description="주제 정답 미리 확인 (연구·교육용)")
    ap.add_argument("--refetch", action="store_true")
    ap.add_argument("--only", nargs="*", default=None, help="T001 T004 … 만")
    ap.add_argument("--tag", default="", help="결과 파일 이름 뒤 (예: r2 → precheck_<날짜>_r2.json)")
    ap.add_argument("--selftest-stocks", action="store_true", help="stocks.py 자료·함수 점검만")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args()
    h = logging.StreamHandler(sys.stdout)
    h.setFormatter(StageFormatter())
    log.addHandler(h)
    log.setLevel(a.log_level)
    logging.getLogger("timing-test-calc").setLevel(logging.WARNING)
    t0 = time.time()
    out("START", version=VERSION, rule=f"정답형 = 모든 칸 같은 쪽 · 가장 약한 칸 ≥ {pct(CELL_MIN)} · 기본 ≥ {pct(MAIN_MIN)}", early=EARLY, late_from=LATE_FROM)
    B = Base(a.refetch)
    res = {}
    need2 = [t for t in stocks.TOPICS2 if not a.only or t in a.only]
    if need2 or a.selftest_stocks:
        I, P, F = stocks.Ix(B), stocks.load_bulk(lambda st, **kv: out(st, **kv)), stocks.load_fa()
        out("LOAD", source="bulk/fa/*.json", symbols=len(F), note="지금 S&P 500 구성 종목 — 생존 편향은 주제마다 bias 칸")
        if a.selftest_stocks:
            return selftest_stocks(B, I, P, F)
    for tid in need2:
        try:
            r = stocks.TOPICS2[tid](B, I, P, F)
        except Exception as e:
            warn("TOPIC", id=tid, error=repr(e)[:160], next_step="stocks.py 함수·bulk 자료 확인")
            r = {"class": "미확인", "answer": "-", "why": f"계산 실패: {e!r}"[:200]}
        res[tid] = r
        out("TOPIC", id=tid, cls=r["class"], answer=str(r["answer"])[:170])
    for tid, f in TOPICS.items():
        if a.only and tid not in a.only:
            continue
        try:
            r = f(B)
        except Exception as e:
            warn("TOPIC", id=tid, error=repr(e)[:160], next_step="자료·함수 확인")
            r = {"class": "미확인", "answer": "-", "why": f"계산 실패: {e!r}"[:200]}
        res[tid] = r
        out("TOPIC", id=tid, cls=r["class"], answer=str(r["answer"])[:150])
    for tid, (cl, why) in NO_DATA.items():
        if a.only and tid not in a.only:
            continue
        res[tid] = {"class": cl, "answer": "-", "why": why, "computed": False}
        out("TOPIC", id=tid, cls=cl, answer="계산 안 함", why=why[:80])
    if not a.only:
        pf = portfolio(B)
        for k, v in pf.items():
            out("PORTFOLIO", item=k.replace(" ", "_"), cls=v["class"], why=v["why"])
        res["portfolio-test-2026-10"] = pf
    path = HERE / f"precheck_{date.today().isoformat()}{'_' + a.tag if a.tag else ''}.json"
    with path.open("w", encoding="utf-8") as f:
        json.dump({"version": VERSION, "made": datetime.now(timezone.utc).isoformat(timespec="seconds"), "data_last": B.d[-1].isoformat(),
                   "rule": {"MAIN_MIN": MAIN_MIN, "CELL_MIN": CELL_MIN, "early": EARLY, "late_from": LATE_FROM}, "results": res},
                  f, ensure_ascii=False, indent=1, default=str)
    out("DONE", file=path.relative_to(ROOT), topics=len(res), seconds=f"{time.time() - t0:.1f}", note="연구·교육용 — 투자 권유 아님")


stocks.bind(classify=classify, classify_full=classify_full, cells=cells, flat=flat, on=on, fetch=fetch)

if __name__ == "__main__":
    sys.exit(main())
