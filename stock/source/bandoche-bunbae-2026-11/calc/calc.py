#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-11-06 — 사용자 지시 "아니 2월 이후 저점에서 산게 아니라 다 회복하고 불타기 계속했다고 가정하면 되잖아 너가 알아서 맞춰":
#          v1.0(2월 말 올인·사서 그대로)은 실제 종가로 A 가 끝까지 이김(7월 말 A +262% · B +25%) → A 규칙을 바꿈:
#          · 갈아타기 = 2월 저점 뒤 A 계좌가 2월 전 최고치를 '다 회복'한 날 → 그다음 거래일 종가에 전부 SOXL·SNDK 반반
#          · 불타기 = 갈아탄 뒤 바구니(SOXL·SNDK)가 새 최고가로 마감한 주마다 그 주 처음 한 번, 다음 거래일 종가에 ADD(처음 돈의 50%)를 더 넣어 반반으로 삼
#          · 수익률 = 증권 앱 평가손익률 = (평가금액 − 넣은 돈 합계) ÷ 넣은 돈 합계 · B 는 처음 돈만 ('원래 하던 방식' — 사용자 흐름).
#            B 도 같은 날 같은 돈을 넣는 길은 B_SAME_ADDS=True (그달 비중대로 나눠 삼) — 이때 B 수익률이 '넣은 돈이 늘어' 17% → 6% 로
#            내려가 보여(손실이 아님) 화면 곡선에는 쓰지 않음: 11/5 B +10.3% · 비교용으로만 로그
#          · 끝 = 받은 자료의 마지막 거래일(2026-11-05) — 7월 AI 버블론 폭락(7/29 저점) 뒤 반등, 11월 두 번째 폭락까지
#          · 판단은 그날 종가, 사는 것은 다음 거래일 종가 (같은 종가로 판단·매매하지 않음 — v1.0 B 의 전날 신호와 같은 원칙)
# 이전 v1.0 — 2026-11-06 — 사용자 지시 "AI, 반도체 종목에 몰빵한 A, 시장 상황에 따라 종목 분배한 B … 2025년 4월 상승장이 시작될 때 …
#          2026년 2월 … 올인 (SNDK, SOXL) … 2026년 7월 AI 버블론으로 주가가 크게 폭락 … 결국 승리자는 B" — 쇼츠 이야기의 숫자(캐릭터 위
#          실시간 수익률·수익 곡선)를 실제 종가로 계산 (CLAUDE.md: 종목 이름을 쓰면 숫자는 실제 종가로). 규칙은 미리 정하고 지난 값만 씀:
#   시작 = 2025-04-09 종가 (4월 상승장 첫날) · 둘 다 100 으로 시작 · 끝 = END (기본 2026-07-31)
#   A 1단계 (시작 ~ 2026-02 마지막 거래일 종가): NVDA·AVGO·AMD·TSM 같은 비중, 사서 그대로
#   A 2단계 (그다음 거래일 시가 대신 2월 마지막 종가로 갈아탐 ~ 끝): SOXL·SNDK 같은 비중 '올인', 사서 그대로
#   B: 섹터 대표 ETF 6개(XLK 기술·XLV 헬스케어·XLF 금융·XLP 필수소비재·XLE 에너지·XLI 산업) 같은 비중 + 현금(BIL 단기국채)
#      매달 첫 거래일에 다시 맞춤 — 전날 S&P 500(SPY) 종가가 200일 평균 위면 주식 80 / 현금 20, 아래면 주식 40 / 현금 60
#   수익률 = 수정 종가(배당·분할 반영) · 세금·수수료 없음 · 환율 없음(달러 기준)
# 출력: calc/result.json (일별 두 곡선 · 단계별 숫자) + 로그. ※ 연구·교육용 — 투자 권유 아님.
from __future__ import annotations

import argparse
import csv
import json
import logging
import time
import urllib.parse
import urllib.request
from datetime import date, datetime, timezone
from pathlib import Path

import numpy as np

VERSION = "v1.1"
HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
START = date(2025, 4, 9)
SWITCH_MONTH = (2026, 2)                       # A 가 갈아타는 달 (그 달 마지막 거래일 종가)
A1 = ["NVDA", "AVGO", "AMD", "TSM"]
A2 = ["SOXL", "SNDK"]
B_SAME_ADDS = False                            # True 면 B 도 A 와 같은 날 같은 돈을 넣음 (비교용)
ADD = 50.0                                     # 불타기 한 번에 더 넣는 돈 (처음 돈 100 = 1,000만 원 → 500만 원)
B_SECTORS = {"XLK": "기술", "XLV": "헬스케어", "XLF": "금융", "XLP": "필수소비재", "XLE": "에너지", "XLI": "산업"}
CASH = "BIL"
MARKET = "SPY"
RISK_ON, RISK_OFF = 0.80, 0.40                 # 주식 비중 (나머지 현금)
MA_DAYS = 200

logging.basicConfig(level=logging.INFO, format="[%(stage)s] [%(asctime)s] %(message)s", datefmt="%Y-%m-%dT%H:%M:%S")
log = logging.getLogger("calc")


def out(stage, **kv):
    log.info(" ".join(f"{k}={v}" for k, v in kv.items()), extra={"stage": stage})


def fetch(symbol: str, refetch: bool) -> dict:
    """수정 종가 — data/<기호>.csv 가 있으면 읽기만 (precheck.py 와 같은 Yahoo chart API v8)."""
    path = DATA / f"{symbol}.csv"
    if refetch or not path.exists():
        p1 = int(datetime(2023, 6, 1, tzinfo=timezone.utc).timestamp())
        url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(symbol)}"
               f"?period1={p1}&period2={int(time.time())}&interval=1d&events=div%2Csplit")
        last = None
        for wait in (0, 2, 4, 8):
            time.sleep(wait)
            try:
                with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=60) as r:
                    res = json.load(r)["chart"]["result"][0]
                q = res["indicators"]["quote"][0]["close"]
                adj = res["indicators"].get("adjclose", [{}])[0].get("adjclose", q)
                rows = [(datetime.fromtimestamp(t, tz=timezone.utc).date().isoformat(), c, a)
                        for t, c, a in zip(res["timestamp"], q, adj) if c is not None and a is not None]
                DATA.mkdir(parents=True, exist_ok=True)
                with path.open("w", encoding="utf-8", newline="") as f:
                    f.write(f"# {symbol} 일별 — Yahoo Finance chart API v8 (close · adjclose 배당·분할 반영), {date.today().isoformat()} 받음 · calc.py {VERSION}\n")
                    w = csv.writer(f)
                    w.writerow(["date", "close", "adjclose"])
                    w.writerows((d, f"{c:.6f}", f"{a:.6f}") for d, c, a in rows)
                out("FETCH", symbol=symbol, rows=len(rows), first=rows[0][0], last=rows[-1][0])
                break
            except Exception as e:      # noqa: BLE001 — 네트워크 오류는 다시 시도
                last = e
                log.warning(f"symbol={symbol} error={e!r} retry_in={wait * 2 or 2}s", extra={"stage": "FETCH"})
        else:
            raise SystemExit(f"[FETCH] {symbol} 받기 실패 ({last!r}) — 네트워크(query1.finance.yahoo.com) 확인 뒤 --refetch")
    with path.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(line for line in f if not line.startswith("#")))
    d = np.array([date.fromisoformat(r["date"]) for r in rows])
    a = np.array([float(r["adjclose"]) for r in rows])
    if len(np.unique(d)) != len(d):
        raise SystemExit(f"[DATA] {symbol} 날짜가 겹침")
    gaps = np.diff(d).astype("timedelta64[D]").astype(int) if len(d) > 1 else np.array([])
    out("LOAD", symbol=symbol, rows=len(d), first=d[0], last=d[-1], max_gap_days=int(gaps.max()) if len(gaps) else 0,
        nonpositive=int((a <= 0).sum()))
    return {"d": d, "a": a}


def aligned(series: dict, days: np.ndarray, sym: str) -> np.ndarray:
    """기준 날짜(days)에 맞춘 수정 종가 — 그날 값이 없으면 바로 앞 값 (앞 값도 없으면 멈춤)."""
    s = series[sym]
    idx = np.searchsorted(s["d"], days, side="right") - 1
    if (idx < 0).any():
        raise SystemExit(f"[DATA] {sym} 이 {days[np.argmax(idx < 0)]} 전에 값이 없음")
    miss = int((s["d"][idx] != days).sum())
    if miss:
        out("DATA", symbol=sym, filled_from_previous_day=miss)
    return s["a"][idx]


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="반도체 몰빵 A vs 나눠 담기 B — 실제 종가 계산 " + VERSION)
    ap.add_argument("--refetch", action="store_true")
    ap.add_argument("--end", default="2026-11-05")
    a = ap.parse_args(argv)
    end = date.fromisoformat(a.end)
    syms = sorted(set(A1 + A2 + list(B_SECTORS) + [CASH, MARKET]))
    S = {s: fetch(s, a.refetch) for s in syms}
    spy = S[MARKET]
    days = spy["d"][(spy["d"] >= START) & (spy["d"] <= end)]
    if days[0] != START:
        raise SystemExit(f"[DATA] 시작일 {START} 이 거래일이 아님 (첫 거래일 {days[0]})")
    P = {s: aligned(S, days, s) for s in syms}
    out("SPLIT", start=days[0], end=days[-1], trading_days=len(days),
        note="계산 구간 하나 (학습·검증 나눔 없음 — 규칙은 계산 전에 정함)")

    # ---- A: 1단계 같은 비중 사서 그대로 → 2월 저점 뒤 '다 회복'한 다음 거래일에 SOXL·SNDK 로 → 불타기 ----
    v1 = sum(P[s] / P[s][0] for s in A1) / len(A1) * 100
    pre = [i for i, d in enumerate(days) if d < date(*SWITCH_MONTH, 1)]
    feb = [i for i, d in enumerate(days) if (d.year, d.month) == SWITCH_MONTH]
    peak_pre = float(v1[pre].max())
    feb_low = feb[int(np.argmin(v1[feb]))]
    rec = next((i for i in range(feb_low, len(days)) if v1[i] >= peak_pre), None)
    if rec is None or rec + 1 >= len(days):
        raise SystemExit("[SIGNAL] A 가 2월 전 최고치를 회복하지 못함 — 규칙 확인")
    sw = rec + 1                                                        # 판단 = 회복한 날 종가 · 매매 = 다음 거래일 종가
    sh = {s: v1[sw] / len(A2) / P[s][sw] for s in A2}
    invested = np.full(len(days), 100.0)
    value = v1.copy()
    adds, hi, wk_done, pending = [], None, None, False
    own = 100.0
    for i in range(sw, len(days)):
        if pending:                                                     # 어제 새 최고가 → 오늘 종가에 더 삼
            for s in A2:
                sh[s] += ADD / len(A2) / P[s][i]
            own += ADD
            adds.append(dict(date=days[i].isoformat(), add=ADD, invested=own))
            out("SIGNAL", who="A", pyramid_buy=days[i], add=ADD, invested_total=own)
            pending = False
        basket = sum(sh[s] * P[s][i] for s in A2)
        value[i], invested[i] = basket, own
        idx = sum(P[s][i] / P[s][sw] for s in A2) / len(A2)              # 갈아탄 날 = 1 인 바구니 값 (새 최고가 판단용)
        if hi is None or idx > hi:
            newhigh = hi is not None
            hi = idx
            wk = days[i].isocalendar()[:2]
            if newhigh and wk != wk_done and i + 1 < len(days):
                pending, wk_done = True, wk
    A = (value - invested) / invested * 100 + 100                       # 100 기준 평가 (100 = 본전) — 아래는 A-100 = 평가손익률
    out("SIGNAL", who="A", stage1=",".join(A1), peak_before_feb=round(peak_pre - 100, 1), feb_low=days[feb_low],
        recovered=days[rec], switch_date=days[sw], value_at_switch=round(float(v1[sw]), 1), stage2=",".join(A2),
        pyramid_adds=len(adds), invested_total=own)

    # ---- B: 매달 첫 거래일에 다시 맞춤 · 비중은 전날 SPY 와 200일 평균으로 (지난 값만) ----
    spy_all_d, spy_all_a = spy["d"], spy["a"]
    def risk_on(day_idx: int) -> tuple[bool, float, float]:
        k = np.searchsorted(spy_all_d, days[day_idx], side="left") - 1      # 전 거래일
        if k < MA_DAYS - 1:
            raise SystemExit("[SIGNAL] 200일 평균을 낼 지난 값이 모자람")
        ma = float(spy_all_a[k - MA_DAYS + 1: k + 1].mean())
        return spy_all_a[k] > ma, float(spy_all_a[k]), ma
    B = np.empty(len(days))
    hold = {}
    value = 100.0
    regimes = []
    add_days = {a_["date"]: a_["add"] for a_ in adds}
    invB = np.full(len(days), 100.0)
    ownB = 100.0
    w = RISK_ON
    for i in range(len(days)):
        new_month = i == 0 or days[i].month != days[i - 1].month
        if i > 0:
            value = sum(n * P[s][i] for s, n in hold.items())
        if new_month:
            on, px, ma = risk_on(i)
            w = RISK_ON if on else RISK_OFF
            hold = {s: value * w / len(B_SECTORS) / P[s][i] for s in B_SECTORS}
            hold[CASH] = value * (1 - w) / P[CASH][i]
            regimes.append(dict(date=days[i].isoformat(), stocks=w, cash=round(1 - w, 2), spy=round(px, 2), ma200=round(ma, 2)))
            out("SIGNAL", who="B", rebalance=days[i], stocks_pct=int(w * 100), cash_pct=int(round((1 - w) * 100)),
                spy_prev=round(px, 2), ma200=round(ma, 2), above=on)
        if B_SAME_ADDS and days[i].isoformat() in add_days:                              # A 와 같은 날 같은 돈 — 그달 비중대로 나눠 삼
            amt = add_days[days[i].isoformat()]
            for s_ in B_SECTORS:
                hold[s_] += amt * w / len(B_SECTORS) / P[s_][i]
            hold[CASH] += amt * (1 - w) / P[CASH][i]
            ownB += amt
            out("SIGNAL", who="B", same_add=days[i], add=amt, stocks_pct=int(w * 100), invested_total=ownB)
        invB[i] = ownB
        B[i] = value if i == 0 else sum(n * P[s][i] for s, n in hold.items())
    B = (B - invB) / invB * 100 + 100                                   # 100 기준 (A 와 같은 평가손익률)

    # ---- 단계별 숫자 ----
    def near(iso):
        return int(np.searchsorted(days, date.fromisoformat(iso), side="right") - 1)
    def dd(v):
        run = np.maximum.accumulate(v)
        k = int(np.argmin(v / run - 1))
        return round(float((v / run - 1)[k] * 100), 1), days[k].isoformat()
    peakA = int(np.argmax(A))
    jul = [i for i, d in enumerate(days) if (d.year, d.month) == (2026, 7)]
    jul_low = jul[int(np.argmin(A[jul]))] if jul else len(days) - 1
    marks = {
        "start": (0, "2025-04 시작"),
        "gap_2025": (int(np.argmax(A[:feb[0]])), "2월 전 A 최고 (A 압도)"),
        "feb_low": (feb_low, "2026-02 조금 하락"),
        "switch": (sw, "다 회복 → SOXL·SNDK 올인"),
        "peak_A": (peakA, "A 최고 (불타기 중)"),
        "jul_low": (jul_low, "2026-07 AI 버블론 폭락 저점"),
        "sep_end": (near("2026-09-30"), "반등"),
        "end": (len(days) - 1, "끝 (11월 두 번째 폭락)"),
    }
    summary = {k: dict(date=days[i].isoformat(), what=w, A=round(float(A[i]) - 100, 1), B=round(float(B[i]) - 100, 1),
                       A_invested=round(float(invested[i]), 1))
               for k, (i, w) in marks.items()}
    for k, v in summary.items():
        out("RESULT", mark=k, date=v["date"], A_return_pct=v["A"], B_return_pct=v["B"], A_invested=v["A_invested"], what=v["what"])
    ddA, ddB = dd(A), dd(B)
    out("RESULT", A_max_drawdown_pct=ddA[0], A_dd_date=ddA[1], B_max_drawdown_pct=ddB[0], B_dd_date=ddB[1])
    if jul:
        out("RESULT", july_A_pts=round(float(A[jul[-1]] - A[jul[0] - 1]), 1), july_B_pct=round(float(B[jul[-1]] / B[jul[0] - 1] - 1) * 100, 1))
    for s in A1 + A2:
        out("RESULT", symbol=s, start_to_end_pct=round(float(P[s][-1] / P[s][0] - 1) * 100, 1),
            switch_to_end_pct=round(float(P[s][-1] / P[s][sw] - 1) * 100, 1))
    res = dict(version=VERSION, generated=datetime.now().isoformat(timespec="seconds"),
               rules=dict(start=START.isoformat(), end=days[-1].isoformat(), A1=A1, A2=A2, switch=days[sw].isoformat(),
                          recovered=days[rec].isoformat(), pyramid_add=ADD, pyramid_adds=adds, A_return="평가손익률 (넣은 돈 합계 기준)",
                          B_sectors=B_SECTORS, cash=CASH, market=MARKET, ma_days=MA_DAYS, risk_on=RISK_ON, risk_off=RISK_OFF),
               marks=summary, drawdown=dict(A=ddA, B=ddB), regimes=regimes,
               daily=[dict(d=d.isoformat(), A=round(float(x) - 100, 2), B=round(float(y) - 100, 2), inv=round(float(v), 1))
                      for d, x, y, v in zip(days, A, B, invested)])
    (HERE / "result.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    out("SUMMARY", file=str((HERE / "result.json").name), days=len(days), A_end=summary["end"]["A"], B_end=summary["end"]["B"],
        winner="B" if B[-1] > A[-1] else "A")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
