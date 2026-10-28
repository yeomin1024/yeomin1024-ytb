#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.2 — 2026-10-28 — q3 에 가장 크게 진 구간의 10만 달러 기준 값 (대본 v1.1 '퍼센트를 달러로' — 페르소나 피드백 2번). 보기 점수·판정 그대로.
# (v1.1 — 2026-10-28 — 점수 항목 2·5 바꿈: v1.0 첫 실행에서 '10% 하락 대기'(q2)·'폭락 때만'(q5)이 5년으로 늘리면 뒤집힘(ROBUST flips)
#          → 참고로만 남기고, 항목 2 = q2b(기다리는 동안 하락 없이 먼저 10% 오른 때 — 대본 상황 그대로) · 항목 5 = q6(5~10월 피하기). 판정 규칙·5년 검사는 그대로.
# (v1.0 — 2026-10-28 — 최초. 매수 시기 테스트 편 M3(목돈 넣을 때) 대본의 숫자 — 미국 S&P 500 배당 포함 지수로 매수 규칙 다섯 쌍을
#          2000년부터 모든 달(최고가 항목은 모든 날)에 시작해 2년 뒤를 비교 (사용자 지시 2026-10-28 "대본 하나 만들어봐" — 피드백
#          stock/source/요약본_피드백_2026-10-28.md 4번이 고른 안).)
#
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.2 | 2026-10-28 | q3 worst_lump/dca_usd_per_100k · ret_pct (대본 달러 표기) | q3_lump |
# | v1.1 | 2026-10-28 | 점수 항목 = q1·q2b·q3·q4·q6 (q2·q5 는 5년에서 뒤집혀 참고만) · 보기 점수·가상 응시 다시 · 도입에 가격 지수 하락 확인 · --selftest | q2b_wait_after_rise · q6_calendar · intro · selftest · QUESTIONS · VIRTUAL · main |
# | v1.0 | 2026-10-28 | 최초 — 받기(--fetch)·검사·항목 5개·도입 숫자·5년 민감도·점수 규칙 | fetch · load · validate · q1~q5 · intro · main |
#
# 실행: python3 -B stock/source/timing-test-2026-10/calc/calc.py            (네트워크 없음 — 같은 폴더 CSV 만 읽음)
#       python3 -B stock/source/timing-test-2026-10/calc/calc.py --fetch    (Yahoo 에서 CSV 다시 받기 — CSV 가 없거나 새로 할 때만)
#       python3 -B stock/source/timing-test-2026-10/calc/calc.py --selftest (가짜 자료로 규칙 시험)
# 자료: ^SP500TR (S&P 500 배당 재투자 지수 — 수익 계산) · ^GSPC (S&P 500 가격 지수 — 도입의 '사상 최고가 몇 번'만, 뉴스와 같은 지수)
#       · ^IRX (미국 13주 국채 금리 % — 기다리는 동안의 현금 이자. 할인율이라 대강의 값). 모두 달러 기준 (환율은 넣지 않음).
# 미리 보기 점검: 모든 규칙은 그날 종가까지 알려진 값으로만 결정하고 그날 종가에 산다 (최고가·하락 폭 = 그날까지의 최고 종가 기준).
# 판정 규칙 (계산 전에 정함 — 결과를 보고 바꾸지 않음): 쌍마다 A 가 B 를 이긴 구간이 50% 넘으면 A. 구간은 서로 겹쳐서 독립이 아님 — 비율은 '그 기간에 그랬다'는 기술.
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
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / "tools"))
import test_score as ts  # noqa: E402

VERSION = "v1.2"
LEVELS = (0, 10, 20)
START_EVAL = date(2000, 1, 1)     # 평가 시작 (1900년대 자료는 쓰지 않음 — 1988~1999 는 최고가·하락 폭 기준을 위한 앞 자료로만)
FETCH_FROM = date(1988, 1, 1)
SERIES = {"sp500tr": "^SP500TR", "gspc": "^GSPC", "irx": "^IRX"}
DIP = 0.10                         # 2번·4번 항목: 10% 하락
CRASH = 0.20                       # 5번 항목: 최고가보다 20% 아래
SPLIT = 12                         # 3·4번: 12개월로 나눠 넣기
MONTHLY = 24                       # 5번: 24개월 매달 넣기

# 보기 점수 — 대본 [항목] 보기 순서와 같게. expect = 계산이 맞다고 볼 쪽 (아니면 MISMATCH 경고 → 보기 점수를 다시 정함)
QUESTIONS = [
    (1, "최고가인 날", False, {"A": 0, "B": 20, "C": 10}),     # A 기다림 · B 정한 방법대로 · C 절반
    (2, "기다리는데 10% 오름", False, {"A": 0, "B": 10, "C": 20}),   # A 계속 기다림 · B 절반 지금 · C 지금 (q2b)
    (3, "한 번에 vs 나눠", False, {"A": 20, "B": 10, "C": 0}),  # A 한 번에(버틸 수 있나 따짐) · B 12개월 · C 한 번에 + 10% 빠지면 매도
    (4, "나눠 넣다 빠짐", False, {"A": 0, "B": 20, "C": 10}),   # A 멈춤 · B 계속 · C 절반
    (5, "5~10월 피하기", False, {"A": 20, "B": 0, "C": 10}),     # A 매달 · B 5~10월 피함 · C 5~10월 절반 (q6)
]
VIRTUAL = [
    ("V1 계획대로 넣는 사람", [20, 20, 20, 20, 20]),
    ("V2 늘 기다리는 사람", [0, 0, 10, 0, 0]),             # 최고가라 미룸 · 계속 기다림 · 나눠 · 멈춤 · 달 피함
    ("V3 늘 절반씩", [10, 10, 10, 10, 10]),
    ("V4 나눠 넣되 계획을 지키는 사람", [20, 20, 10, 20, 20]),
    ("V5 한 번에 넣고 빠지면 파는 사람", [20, 20, 0, 0, 20]),
]


class StageFormatter(logging.Formatter):
    def format(self, record):
        return f"[{getattr(record, 'stage', 'CALC')}] [{self.formatTime(record, '%Y-%m-%dT%H:%M:%S')}] {record.getMessage()}"


log = logging.getLogger("timing-test-calc")


def out(stage, **kv):
    log.info(" ".join(f"{k}={v}" for k, v in kv.items()), extra={"stage": stage})


def warn(stage, **kv):
    log.warning(" ".join(f"{k}={v}" for k, v in kv.items()), extra={"stage": stage})


# ---------- 받기 (--fetch 일 때만) ----------
def fetch(name, symbol):
    p1 = int(datetime(FETCH_FROM.year, FETCH_FROM.month, FETCH_FROM.day, tzinfo=timezone.utc).timestamp())
    p2 = int(time.time())
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(symbol)}?period1={p1}&period2={p2}&interval=1d"
    last = None
    for wait in (0, 2, 4, 8):
        time.sleep(wait)
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=60) as r:
                j = json.load(r)
            res = j["chart"]["result"][0]
            ts_ = res["timestamp"]
            close = res["indicators"]["quote"][0]["close"]
            rows = [(datetime.fromtimestamp(t, tz=timezone.utc).date().isoformat(), c) for t, c in zip(ts_, close) if c is not None]
            path = HERE / f"{name}_daily.csv"
            with path.open("w", encoding="utf-8", newline="") as f:
                f.write(f"# {symbol} 일별 종가 — Yahoo Finance chart API v8 (interval=1d), {date.today().isoformat()} 받음 · calc.py {VERSION} --fetch\n")
                w = csv.writer(f)
                w.writerow(["date", "close"])
                w.writerows((d, f"{c:.6f}") for d, c in rows)
            out("FETCH", symbol=symbol, rows=len(rows), first=rows[0][0], last=rows[-1][0], file=path.name)
            return
        except Exception as e:  # 네트워크·형식 — 다시 시도
            last = e
            warn("FETCH", symbol=symbol, error=repr(e)[:160], retry_after=wait * 2 or 2)
    log.error(f"symbol={symbol} error={last!r} next_step=네트워크 확인(curl -sS \"$HTTPS_PROXY/__agentproxy/status\") 뒤 --fetch 다시",
              extra={"stage": "FETCH"})
    raise SystemExit(1)


# ---------- 읽기·검사 ----------
def load(name):
    path = HERE / f"{name}_daily.csv"
    try:
        with path.open(encoding="utf-8") as f:
            rows = list(csv.DictReader(line for line in f if not line.startswith("#")))
    except OSError as e:
        log.error(f"file={path.name} error={e} next_step=python3 -B {Path(__file__).relative_to(ROOT)} --fetch", extra={"stage": "LOAD"})
        raise SystemExit(1)
    d = np.array([date.fromisoformat(r["date"]) for r in rows])
    c = np.array([float(r["close"]) for r in rows])
    out("LOAD", series=name, rows=len(d), first=d[0], last=d[-1])
    return d, c


def validate(name, d, c):
    dup = int(len(d) - len(set(d)))
    order = int(np.sum(d[1:] <= d[:-1]))
    bad = int(np.sum(~np.isfinite(c)) + np.sum(c <= 0)) if name != "irx" else int(np.sum(~np.isfinite(c)) + np.sum(c < -1))
    gaps = [(d[i - 1], d[i]) for i in range(1, len(d)) if (d[i] - d[i - 1]).days > 6]
    jumps = [] if name == "irx" else [(d[i], round((c[i] / c[i - 1] - 1) * 100, 1)) for i in range(1, len(c)) if abs(c[i] / c[i - 1] - 1) > 0.15]
    kv = dict(series=name, duplicates=dup, out_of_order=order, bad_values=bad, gaps_over_6d=len(gaps), jumps_over_15pct=len(jumps))
    (warn if (dup or order or bad or jumps) else out)("VALIDATE", **kv, examples=(gaps + jumps)[:3] or "-")   # 6일 넘는 빈 날(2001-09 휴장)은 알림만
    if dup or order or bad:
        raise SystemExit("[VALIDATE] 자료에 중복·순서·값 문제 — --fetch 로 다시 받기")


def align_irx(d, irx_d, irx_v):
    """S&P 날짜마다 그날까지 알려진 마지막 ^IRX (앞 값 채움). 처음 몇 날이 비면 첫 값."""
    idx = np.searchsorted(irx_d, d, side="right") - 1
    filled = int(np.sum(idx < 0))
    idx[idx < 0] = 0
    out("ALIGN", series="irx", target_days=len(d), filled_before_first=filled, note="앞 값 채움 — 미래 값 안 씀")
    return irx_v[idx]


def cash_index(d, y):
    """현금 1달러의 누적 값: i-1 → i 동안 i-1 날의 금리(연 %)로 단리 (날수/365)."""
    days = np.array([0] + [(d[i] - d[i - 1]).days for i in range(1, len(d))], dtype=float)
    f = 1 + np.concatenate([[0.0], y[:-1]]) / 100 * days / 365
    return np.cumprod(f)


def month_starts(d):
    m = np.array([x.year * 12 + x.month for x in d])
    return np.flatnonzero(np.concatenate([[True], m[1:] != m[:-1]])), m


def windows(ms, mkey, d, months):
    """평가 창: 시작 = 2000-01 이후 각 달의 첫 거래일, 끝 = months 개월 뒤 달의 첫 거래일 (자료 안에 있을 때만)."""
    pos = {k: i for i, k in zip(ms, mkey[ms])}
    w = []
    for i in ms:
        if d[i] < START_EVAL:
            continue
        k = mkey[i]
        if k + months in pos:
            w.append((i, pos[k + months], [pos[k + j] for j in range(months) if k + j in pos]))
    return w


def share(x):
    return float(np.mean(x)) if len(x) else float("nan")


def pctf(x):
    return f"{x * 100:.1f}%"


# ---------- 항목 ----------
def q1_ath(d, p, start_from, horizon_days):
    """사상 최고가인 날 매수 vs 아무 날 매수 — horizon_days 뒤 첫 거래일 종가까지. 최고가 = 그날까지의 모든 종가 중 최고 (1988~)."""
    cm = np.maximum.accumulate(p)
    ath = np.concatenate([[False], p[1:] >= cm[:-1]])
    ends = np.searchsorted(d, d + timedelta(days=horizon_days), side="left")
    ok = (d >= start_from) & (ends < len(d))
    r = p[ends[ok]] / p[ok] - 1
    a = ath[ok]
    res = dict(days=int(ok.sum()), ath_days=int(a.sum()), loss_all=share(r < 0), loss_ath=share(r[a] < 0),
               median_all=float(np.median(r)), median_ath=float(np.median(r[a])))
    res["verdict"] = "미루지 않음" if res["loss_ath"] <= res["loss_all"] else "최고가 날이 더 자주 손실"
    return res


def q2_wait(p, c, W):
    """지금 매수 vs '10% 빠지면 매수' — 끝까지 안 빠지면 현금(국채 이자)."""
    now, wait, never = [], [], []
    for s, e, _ in W:
        hit = np.flatnonzero(p[s + 1:e + 1] <= (1 - DIP) * p[s])
        now.append(p[e] / p[s])
        if len(hit):
            j = s + 1 + hit[0]
            wait.append(c[j] / c[s] * p[e] / p[j])
            never.append(False)
        else:
            wait.append(c[e] / c[s])
            never.append(True)
    now, wait = np.array(now), np.array(wait)
    res = dict(windows=len(W), now_wins=share(now > wait), never_dipped=share(np.array(never)),
               median_gap_pct=float(np.median(now / wait - 1)))
    res["verdict"] = "지금" if res["now_wins"] > 0.5 else "기다림"
    return res


def dca_value(p, c, s, e, buys, n):
    """n 번으로 나눠 매달 첫 거래일에 넣기 (기다리는 돈은 국채 이자)."""
    return sum(1 / n * c[b] / c[s] * p[e] / p[b] for b in buys[:n])


def q3_lump(p, c, W):
    """한 번에 vs 12개월로 나눠 vs 한 번에 넣고 10% 빠지면 매도(뒤는 현금)."""
    lump, dca, stop = [], [], []
    for s, e, buys in W:
        lump.append(p[e] / p[s])
        dca.append(dca_value(p, c, s, e, buys, SPLIT))
        hit = np.flatnonzero(p[s + 1:e + 1] <= (1 - DIP) * p[s])
        j = s + 1 + hit[0] if len(hit) else None
        stop.append(p[e] / p[s] if j is None else p[j] / p[s] * c[e] / c[j])   # 그날 종가에 매도 → 끝까지 현금
    lump, dca, stop = map(np.array, (lump, dca, stop))
    lose = lump < dca
    trig = lump != stop
    res = dict(windows=len(W), lump_wins=share(lump > dca), lump_vs_stop_wins=share(lump[trig] > stop[trig]),
               stop_triggered=share(trig), median_lump_pct=float(np.median(lump - 1)), median_dca_pct=float(np.median(dca - 1)),
               median_stop_pct=float(np.median(stop - 1)), median_gap_when_lump_loses_pct=float(np.median(lump[lose] / dca[lose] - 1)) if lose.any() else 0.0,
               worst_gap_pct=float(np.min(lump / dca - 1)), worst_start_idx=int(W[int(np.argmin(lump / dca))][0]),
               best_gap_pct=float(np.max(lump / dca - 1)))
    wi = int(np.argmin(lump / dca))            # 가장 크게 진 구간의 10만 달러 기준 2년 뒤 값 (대본 '달러로 말하기')
    res["worst_lump_usd_per_100k"], res["worst_dca_usd_per_100k"] = round(100000 * float(lump[wi])), round(100000 * float(dca[wi]))
    res["worst_lump_ret_pct"], res["worst_dca_ret_pct"] = float(lump[wi] - 1), float(dca[wi] - 1)
    res["verdict"] = "한 번에" if res["lump_wins"] > 0.5 and res["median_stop_pct"] < res["median_dca_pct"] else "다시 볼 것"
    return res


def q4_stop(p, c, W):
    """12개월로 나눠 넣다가, 넣는 날 값이 첫날보다 10% 아래면 남은 돈은 멈추고 현금 vs 계획대로 계속. 멈춤이 일어난 구간만 비교."""
    cont, stop = [], []
    for s, e, buys in W:
        b = buys[:SPLIT]
        k = next((i for i in range(1, len(b)) if p[b[i]] <= (1 - DIP) * p[b[0]]), None)
        if k is None:
            continue
        cont.append(dca_value(p, c, s, e, b, SPLIT))
        stop.append(sum(1 / SPLIT * c[x] / c[s] * p[e] / p[x] for x in b[:k]) + (SPLIT - k) / SPLIT * c[e] / c[s])
    cont, stop = np.array(cont), np.array(stop)
    res = dict(windows=len(W), triggered=len(cont), triggered_share=len(cont) / len(W) if W else 0.0,
               continue_wins=share(cont > stop), median_gap_pct=float(np.median(cont / stop - 1)) if len(cont) else 0.0)
    res["verdict"] = "계속" if res["continue_wins"] > 0.5 else "멈춤"
    return res


def q5_crash(p, c, W):
    """24개월 매달 같은 금액 vs 모아 두었다가 최고가보다 20% 넘게 아래인 날에만 그때까지 모은 돈을 모두 매수."""
    cm = np.maximum.accumulate(p)
    dd = p / cm - 1
    mon, cr, nocrash = [], [], []
    for s, e, buys in W:
        b = buys[:MONTHLY]
        mon.append(sum(p[e] / p[x] for x in b))
        units, cash_u, crashed = 0.0, 0.0, False
        bset = set(b)
        for i in range(s, e):
            if i in bset:
                cash_u += 1 / c[i]
            if dd[i] <= -CRASH and cash_u > 0:
                units += cash_u * c[i] / p[i]
                cash_u, crashed = 0.0, True
        cr.append(units * p[e] + cash_u * c[e])
        nocrash.append(not crashed)
    mon, cr = np.array(mon), np.array(cr)
    res = dict(windows=len(W), monthly_wins=share(mon > cr), no_crash_windows=share(np.array(nocrash)),
               median_gap_pct=float(np.median(mon / cr - 1)))
    res["verdict"] = "매달" if res["monthly_wins"] > 0.5 else "폭락 때만"
    return res


def q2b_wait_after_rise(d, p, c, horizon_days, rise=0.10):
    """후보 (v1.1): '10% 빠지면 사겠다'며 기다리는 동안 하락 없이 먼저 10% 오른 날(t) — 그때 지금 매수 vs 처음 목표값(시작값의 90%)까지 계속 기다림.
    시작 = 2000-01 이후 각 달 첫 거래일 · t 이후 horizon_days 뒤 첫 거래일에 비교 (계속 기다리면 끝까지 현금일 수 있음)."""
    ms = np.flatnonzero(np.concatenate([[True], np.array([x.month for x in d[1:]]) != np.array([x.month for x in d[:-1]])]))
    now, wait, back = [], [], []
    for s in ms:
        if d[s] < START_EVAL:
            continue
        seg = p[s + 1:]
        up = np.flatnonzero(seg >= (1 + rise) * p[s])
        dn = np.flatnonzero(seg <= (1 - DIP) * p[s])
        if not len(up) or (len(dn) and dn[0] < up[0]):
            continue                                   # 먼저 빠졌으면 이 조건이 아님
        t = s + 1 + up[0]
        e = int(np.searchsorted(d, d[t] + timedelta(days=horizon_days), side="left"))
        if e >= len(d):
            continue
        hit = np.flatnonzero(p[t + 1:e + 1] <= (1 - DIP) * p[s])
        now.append(p[e] / p[t])
        if len(hit):
            j = t + 1 + hit[0]
            wait.append(c[j] / c[t] * p[e] / p[j])
            back.append(True)
        else:
            wait.append(c[e] / c[t])
            back.append(False)
    now, wait = np.array(now), np.array(wait)
    res = dict(cases=len(now), required_fall_pct=1 - (1 - DIP) / (1 + rise), now_wins=share(now > wait), came_back_to_target=share(np.array(back)),
               median_gap_pct=float(np.median(now / wait - 1)) if len(now) else 0.0)
    res["verdict"] = "지금" if res["now_wins"] > 0.5 else "기다림"
    return res


def q6_calendar(d, p, c, W):
    """후보 (v1.1): 24개월 매달 넣기 vs 5~10월에는 넣지 않고 모아 두었다가 11월 첫 거래일에 한꺼번에 (그 밖 달은 매달)."""
    mon, avoid = [], []
    for s, e, buys in W:
        b = buys[:MONTHLY]
        mon.append(sum(p[e] / p[x] for x in b))
        units, cash_u = 0.0, 0.0
        for x in b:
            cash_u += 1 / c[x]
            if not (5 <= d[x].month <= 10):
                units += cash_u * c[x] / p[x]
                cash_u = 0.0
        avoid.append(units * p[e] + cash_u * c[e])
    mon, avoid = np.array(mon), np.array(avoid)
    res = dict(windows=len(W), monthly_wins=share(mon > avoid), median_gap_pct=float(np.median(mon / avoid - 1)))
    res["verdict"] = "매달" if res["monthly_wins"] > 0.5 else "5~10월 피하기"
    return res


def intro(gd, gp, d, p, year):
    """도입: 올해 S&P 500(가격 지수) 사상 최고가 종가 횟수 · 올해 첫 거래일에 '10% 빠지면 넣겠다'고 기다린 사람 vs 그날 넣은 사람 (배당 포함)."""
    cm = np.maximum.accumulate(gp)
    ath = np.concatenate([[False], gp[1:] > cm[:-1]])
    yr = np.array([x.year == year for x in gd])
    s = int(np.flatnonzero(np.array([x.year == year for x in d]))[0])
    hit = np.flatnonzero(p[s + 1:] <= (1 - DIP) * p[s])
    res = dict(year=year, ath_closes=int((ath & yr).sum()), last_date=d[-1].isoformat(), first_day=d[s].isoformat(),
               gain_since_first_day_pct=float(p[-1] / p[s] - 1), dipped=bool(len(hit)),
               dip_date=d[s + 1 + hit[0]].isoformat() if len(hit) else "-",
               peak_drawdown_ytd_pct=float(np.min(p[s:] / np.maximum.accumulate(p[s:]) - 1)))
    if len(hit):
        j = s + 1 + hit[0]
        res["waiter_gain_pct"] = float(p[-1] / p[j] - 1)
    gs = int(np.flatnonzero(yr)[0])            # 기다리는 사람이 보는 값 = 가격 지수 — 그 값으로도 10% 아래로 간 적이 있나
    res["price_index_min_vs_first_day_pct"] = float(np.min(gp[gs:]) / gp[gs] - 1)
    res["price_index_dipped"] = bool(np.min(gp[gs:]) <= (1 - DIP) * gp[gs])
    return res


def selftest():
    """작은 가짜 자료로 규칙이 뜻대로 도는지 (네트워크 없음): 값이 그대로면 한 번에 = 나눠 · 계속 오르면 한 번에가 늘 이김 · 10% 하락 대기는 하락이 오면 늘 이김."""
    d = np.array([date(2000, 1, 1) + timedelta(days=i) for i in range(1200)])
    flat, rise = np.ones(len(d)), np.linspace(1, 3, len(d))
    c0 = np.ones(len(d))
    ms, mkey = month_starts(d)
    W = windows(ms, mkey, d, 24)
    ok = []
    ok.append(abs(q3_lump(flat, c0, W)["median_lump_pct"] - q3_lump(flat, c0, W)["median_dca_pct"]) < 1e-12)
    ok.append(q3_lump(rise, c0, W)["lump_wins"] == 1.0)
    vshape = np.concatenate([np.linspace(1, 0.8, 300), np.linspace(0.8, 1.5, len(d) - 300)])
    ok.append(q2_wait(vshape, c0, W[:3])["now_wins"] == 0.0)          # 처음 석 달 시작 → 모두 10% 아래를 지남 → 기다림이 늘 이김
    ok.append(q4_stop(rise, c0, W)["triggered"] == 0)                  # 오르기만 하면 멈춤이 안 일어남
    out("SELFTEST", checks=len(ok), passed=sum(ok), result="OK" if all(ok) else "FAIL")
    if not all(ok):
        raise SystemExit("[SELFTEST] 실패 — 규칙 코드를 다시 볼 것")


def fmt(res):
    return {k: (pctf(v) if isinstance(v, float) and ("pct" in k or k.startswith(("loss", "now", "lump", "never", "stop", "continue", "monthly", "no_", "triggered_", "median", "came_"))) else v)
            for k, v in res.items()}


def main():
    ap = argparse.ArgumentParser(description="매수 시기 테스트 편 계산 (연구·교육용)")
    ap.add_argument("--fetch", action="store_true", help="Yahoo 에서 CSV 다시 받기")
    ap.add_argument("--selftest", action="store_true", help="가짜 자료로 규칙 시험만")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args()
    h = logging.StreamHandler(sys.stdout)
    h.setFormatter(StageFormatter())
    log.addHandler(h)
    log.setLevel(a.log_level)
    t0 = time.time()
    if a.selftest:
        selftest()
        return
    out("START", version=VERSION, test_score=ts.VERSION, eval_from=START_EVAL, dip=DIP, crash=CRASH, split=SPLIT, monthly=MONTHLY)
    if a.fetch:
        for n, s in SERIES.items():
            fetch(n, s)
    d, p = load("sp500tr")
    gd, gp = load("gspc")
    id_, iv = load("irx")
    for n, (x, y) in {"sp500tr": (d, p), "gspc": (gd, gp), "irx": (id_, iv)}.items():
        validate(n, x, y)
    c = cash_index(d, align_irx(d, id_, iv))
    ms, mkey = month_starts(d)
    out("FEATURE", rule="최고가·하락 폭 = 그날까지 최고 종가 · 현금 = ^IRX 단리 · 창 = 각 달 첫 거래일", cash_x_2000_to_last=f"{c[-1] / c[np.searchsorted(d, START_EVAL)]:.3f}")

    results = {}
    for label, months, days in (("2y", 24, 730), ("5y", 60, 1826)):
        W = windows(ms, mkey, d, months)
        out("SPLIT", horizon=label, windows=len(W), first_start=d[W[0][0]], last_start=d[W[-1][0]], last_end=d[W[-1][1]])
        r = {"q1": q1_ath(d, p, START_EVAL, days), "q2": q2_wait(p, c, W), "q3": q3_lump(p, c, W), "q4": q4_stop(p, c, W), "q5": q5_crash(p, c, W),
             "q2b": q2b_wait_after_rise(d, p, c, days), "q6": q6_calendar(d, p, c, W)}
        r["q3"]["worst_start"] = d[r["q3"].pop("worst_start_idx")].isoformat()
        for q, v in r.items():
            out(f"{q.upper()}", horizon=label, **fmt(v))
        results[label] = r

    expect = {"q1": "미루지 않음", "q2b": "지금", "q3": "한 번에", "q4": "계속", "q6": "매달"}   # 점수 항목 1~5 (q2·q5 는 참고)
    mism = [q for q, v in expect.items() if results["2y"][q]["verdict"] != v]
    flips = [q for q in results["2y"] if results["2y"][q]["verdict"] != results["5y"][q]["verdict"]]
    used_flips = [q for q in flips if q in expect]
    (warn if mism else out)("SIGNAL", rule="쌍마다 이긴 구간 > 50% (2년이 본 결과)", expected=expect, mismatches=mism or "-",
                            note="MISMATCH 면 QUESTIONS 보기 점수를 다시 정할 것" if mism else "보기 점수와 계산이 같은 쪽")
    (warn if used_flips else out)("ROBUST", check="5년으로 늘려도 같은 쪽인가", flips_all=flips or "-", flips_in_scored=used_flips or "-")

    it = intro(gd, gp, d, p, 2026)
    out("INTRO", **fmt(it))
    out("NOTE", reference_only="q2 10% 하락 대기 · q5 폭락 때만", why="5년에서 뒤집힘 — 오래 통하는 결론이 아니라 점수에 안 씀 (채널 설명 3-5)",
        q2_2y=pctf(results["2y"]["q2"]["now_wins"]), q2_5y=pctf(results["5y"]["q2"]["now_wins"]),
        q5_2y=pctf(results["2y"]["q5"]["monthly_wins"]), q5_5y=pctf(results["5y"]["q5"]["monthly_wins"]))
    problems = ts.check_rules(QUESTIONS, out, log, levels=LEVELS)
    ts.run_virtual(QUESTIONS, VIRTUAL, out)
    with (HERE / "results.json").open("w", encoding="utf-8") as f:
        json.dump({"version": VERSION, "made": datetime.now(timezone.utc).isoformat(timespec="seconds"), "data_last": d[-1].isoformat(),
                   "results": results, "intro": it, "mismatches": mism, "flips_5y": flips, "scored": list(expect), "rule_problems": problems},
                  f, ensure_ascii=False, indent=1, default=str)
    out("DONE", results="calc/results.json", rule_problems=problems, mismatches=len(mism), seconds=f"{time.time() - t0:.1f}",
        note="연구·교육용 — 투자 권유 아님")


if __name__ == "__main__":
    main()
