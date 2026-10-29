#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v2.1 — 2026-10-29 — 반론 6회차(상 1 · 중 5 · 하 5)에 답함: 정답 칸 = 앞 시기 경계 넷(QUIZ_EARLY_DEFS) × 이자 둘에서 모두 같은 칸 · 칸 빈틈 없앰(<40 · 40~60 · >60) ·
#          문제 2·3·5 = 1년까지만 기다림 · 6개월 나눠 · 석 달 뒤 (v2.0 의 ±10% 끝 · 12개월 나눠 · 1년 뒤는 경계에 따라 칸이 바뀌어 QUIZ_REF 로) · QUIZ_ASYM 지우고 QUIZ_ALL(두 시기 합침).
# (v2.0 — 2026-10-29 — 문제형으로 바꿈 (사용자 지시 "1번으로 해봐" — 반론 5회차 뒤 고른 안 ①: '시기를 맞히는 규칙은 시작 시기로 나누면 뒤집혔다'):
#          문제 5개 = '2009년 이후 시작한 사람은 다섯 규칙 모두 미루거나 팔지 않은 쪽이 이겼다 — 2000~2008년에 시작했다면?' · 보기 = 규칙 쪽 · 반반 · 미루지 않은 쪽 ·
#          맞히면 20 · 틀리면 0 (QUIZ · quiz_pairs · quiz_run · big_declines). v1.x 테스트 꼴 점수 항목(q2b·q3b·q3s·q10·q6b)은 참고로 남김.)
# (v1.7 — 2026-10-28 — 반론 검토 4회차에 답함 (모두 참고·점수 그대로): q2d(끝을 정한 기다림 vs 바로) · q2e(새 값 기준 다시 10% 기다림) · q3t(매도 뒤 N개월에 다시) · q3b 가운데 값 달러.)
# (v1.6 — 2026-10-28 — 반론 검토 3회차에 답함: 점수 항목 = q2b·q3b·q3s·q10·q6b (q4b 는 재진입을 바닥 반등으로 바꾸면(q4c) 뒤집혀 참고 · q2c 는 사례가 2013~2021 상승기뿐이라 참고) · q6 버그(마지막 해 5~10월 몫 미투입) 고침 · q10(1년 뒤 넣기) · q4c · q2b 분모·시기 · 이자 5% 민감도 넓힘.
# (v1.5 — 2026-10-28 — 반론 검토 2회차에 답함: 항목 1 = q2c(최고가인 날 시작 — 사연대로) · q3s 까닭(돌아온 경우·다른 재진입) · q6b 격언 원래 꼴(5월 매도) · 현금 이자 연 5% 민감도 · 겹치지 않는 창 수 · 도입 최저 날짜.
# (v1.4 — 2026-10-28 — 반론 검토 1회차(대본_반론_검토.md)에 답함: 점수 항목 = q2b·q3b·q3s·q4b·q6 — 처음 항목 1(최고가인 날)은 q1b(바로 vs 10% 빠지면, ^GSPC)로 재니 2년 53.7%·5년 47.8% 로 뒤집혀 뺌 · 새 항목 3 = q3s · 항목 4 = q4b(멈췄다 첫날 값에 다시) · 최고가 = ^GSPC · 하락기 묶음 · 중간 낙폭 · 진 때 크기 · 5~10월 해마다 · 500달러 금액 · 도입 = 올해 첫 최고가 날.
# (v1.3 — 2026-10-28 — 항목 3 = q3b (넣는 속도: 한 번에 · 12개월 · 36개월 — 빠져도 매도 안 하는 사람으로 조건을 못 박음). 사용자 지시 "애매한게 있으면 반론이 들어온다고 명확한걸로" — 위험 성향에 따라 갈리는 '한 번에 vs 나눠 + 손절' 보기를 같은 축 셋으로. q3 는 참고.
# (v1.2 — 2026-10-28 — q3 에 가장 크게 진 구간의 10만 달러 기준 값 (대본 v1.1 '퍼센트를 달러로' — 페르소나 피드백 2번). 보기 점수·판정 그대로.
# (v1.1 — 2026-10-28 — 점수 항목 2·5 바꿈: v1.0 첫 실행에서 '10% 하락 대기'(q2)·'폭락 때만'(q5)이 5년으로 늘리면 뒤집힘(ROBUST flips)
#          → 참고로만 남기고, 항목 2 = q2b(기다리는 동안 하락 없이 먼저 10% 오른 때 — 대본 상황 그대로) · 항목 5 = q6(5~10월 피하기). 판정 규칙·5년 검사는 그대로.
# (v1.0 — 2026-10-28 — 최초. 매수 시기 테스트 편 M3(목돈 넣을 때) 대본의 숫자 — 미국 S&P 500 배당 포함 지수로 매수 규칙 다섯 쌍을
#          2000년부터 모든 달(최고가 항목은 모든 날)에 시작해 2년 뒤를 비교 (사용자 지시 2026-10-28 "대본 하나 만들어봐" — 피드백
#          stock/source/요약본_피드백_2026-10-28.md 4번이 고른 안).)
#
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v2.1 | 2026-10-29 | 반론 6회차: QUIZ_EARLY_DEFS · QZ_SPEC(dip 1년까지 · split n · sell N개월 · delay m) · QUIZ_REF · band_of 빈틈 없음 · quiz_run(경계 넷 · late2010 · two_year · 범위) · QUIZ_CHECK(이자 5% 포함) · QUIZ_ALL · selftest 12 | QZ_SPEC · quiz_pairs · band_of · quiz_run · selftest · main |
# | v2.0 | 2026-10-29 | 문제형: QUIZ(5문제·칸 규칙·보기 순서) · quiz_pairs(구간별 두 값 — 기존 함수와 같은 규칙, selftest 로 비율 대조) · quiz_run(앞·뒤 시기 × 2년·5년 · 다른 자르기 · 이자 5%) · big_declines(^GSPC 20% 넘는 하락) · QUESTIONS = 0·0·20 · VIRTUAL 글자로 | quiz_pairs · quiz_cell · band_of · quiz_run · big_declines · selftest · main |
# | v1.7 | 2026-10-28 | 반론 4회차: q2d_wait_with_end · q2e_rewait · q3t_rebuy_after · q3b median_*_usd_100k (점수 항목·판정 그대로) | q2d_wait_with_end · q2e_rewait · q3t_rebuy_after · main |
# | v1.6 | 2026-10-28 | 반론 3회차: 점수 항목 q2b·q3b·q3s·q10·q6b · q6 버그 고침 · q10_wait_months · q4c_stop_rebound · q6b_verdict · q2b eligible·spans · sens 넓힘 | q6_calendar · q10_wait_months · q4c_stop_rebound · q6b_verdict · q2b · main |
# | v1.5 | 2026-10-28 | 반론 2회차: q2c · q3s_detail · q6b_sell_in_may · sens_cash5 · nonoverlap · intro2 min_after_day · 점수 항목 1 = q2c | q2c_ath_wait_after_rise · q3s_detail · q6b_sell_in_may · nonoverlap · intro2 · main |
# | v1.4 | 2026-10-28 | 반론 1회차: 점수 항목 = q2b·q3b·q3s·q4b·q6 (q1b 는 5년에서 뒤집혀 참고) · q3s(넣은 뒤 10% 빠지면 매도→산 값에 다시) · q1b · q4b · ath_flags(^GSPC) · episodes · path_drawdown · calendar_years · intro2 · q2b 진 때 크기·다른 날 수 · q6 달러 | q1b_ath_wait · q4b_stop_reenter · ath_flags · episodes · path_drawdown · calendar_years · intro2 · q2b · q6 · main |
# | v1.3 | 2026-10-28 | 항목 3 = q3b (한 번에·12개월·36개월 · 쌍마다 이긴 구간 > 50% — 처음 쓴 '1등 몫 순서'는 5년에서 뒤집혀 머리 규칙으로 되돌림) · expect · QUESTIONS 3 · VIRTUAL V5 이름 · q3 worst_dca_minus_lump_usd | q3b_speed · q3_lump · main |
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

VERSION = "v2.1"
LEVELS = (0, 0, 20)                # v2.0 문제형: 맞히면 20 · 틀리면 0 (보기 셋 중 정답 하나)
START_EVAL = date(2000, 1, 1)     # 평가 시작 (1900년대 자료는 쓰지 않음 — 1988~1999 는 최고가·하락 폭 기준을 위한 앞 자료로만)
FETCH_FROM = date(1988, 1, 1)
SERIES = {"sp500tr": "^SP500TR", "gspc": "^GSPC", "irx": "^IRX"}
DIP = 0.10                         # 2번·4번 항목: 10% 하락
CRASH = 0.20                       # 5번 항목: 최고가보다 20% 아래
SPLIT = 12                         # 3·4번: 12개월로 나눠 넣기
MONTHLY = 24                       # 5번: 24개월 매달 넣기

# ---------- v2.1 문제형 (계산 전에 정한 것과 결과를 본 뒤 정한 것을 나눠 적음) ----------
# 질문: "2009년 이후 시작한 사람은 다섯 규칙 모두 미루거나 팔지 않은 쪽이 이겼다 — 그럼 큰 하락이 두 번 있던 2000~2008년에 시작한 사람은?"
# 시기 = 시작한 달: 앞 = 큰 하락 두 번(2000~02 · 2007~09)을 품은 시기 — 대본 숫자는 2000-01~2008-12 (QUIZ_EARLY) · 뒤 = 2009-01~ (QUIZ_LATE_FROM).
#   ⚠ 경계는 결과를 본 뒤 정함 → 정답은 경계를 한 해씩 옮긴 넷(QUIZ_EARLY_DEFS) × 현금 이자 두 가지(^IRX · 연 5%)에서 모두 같은 칸일 때만 씀.
# 칸 = 앞 시기에 '미루지 않은 쪽'(바로·한 번에·그대로)이 이긴 몫 x — 문제가 묻는 5년 뒤로:
#   rule: x < 40% (규칙 쪽이 '열 번 중 여섯 번 넘게') · now: x > 60% · even: 40~60% ('어느 쪽도 여섯 번을 넘지 못함').
#   2년은 참고: 같은 칸이 아니면 50% 기준으로 같은 쪽인지 적고 대본·설명란에 밝힘 (QUIZ two_year).
# 전제: 뒤 시기(2009~ · 2010~)의 5년과 2009~ 의 2년 모두 x > 60% (LATE_MIN).
# ⚠ v2.1 문제 다섯은 반론 6회차 뒤 후보 23개의 경계·이자 표를 보고 고름 — v2.0 의 끝 정한 기다림(±10%)·12개월 나눠·1년 뒤는
#   경계를 옮기면 even ↔ now 로 바뀌어 뺌 (QUIZ_REF 로 같이 계산해 설명란에 적음). 판정·구간(매달 첫 거래일)·현금 이자(^IRX)는 v1.x 머리 규칙 그대로.
QUIZ_EARLY = (2000, 2008)
QUIZ_EARLY_DEFS = [(2000, 2008), (2000, 2007), (2001, 2008), (2001, 2007)]
QUIZ_LATE_FROM = 2009
LATE_MIN = 0.60
QZ_SPEC = {  # 키 → (규칙 종류, 값) — quiz_pairs
    "qz_dip": ("dip", None),      # 시작한 날 값보다 10% 아래로 오면 넣기 · 구간 끝까지 안 오면 끝까지 현금
    "qz_dip1y": ("dip", 12),      # 같은데 12개월째 첫 거래일까지 안 오면 그날 넣기
    "qz_end": ("end", DIP),       # 10% 빠지거나 먼저 10% 오르면 그날 넣기 (v2.0 2번 — 참고)
    "qz_split6": ("split", 6),    # 6개월로 나눠 매달 첫 거래일에 같은 금액
    "qz_split": ("split", 12),    # 12개월로 나눠 (v2.0 3번 — 참고)
    "qz_sell3": ("sell", 3), "qz_sell6": ("sell", 6), "qz_sell9": ("sell", 9), "qz_sell12": ("sell", 12),   # 한 번에 넣은 뒤 넣은 값보다 10% 빠진 날 모두 매도 → N개월 뒤 다시
    "qz_wait3": ("delay", 3),     # 3개월째 첫 거래일에 한 번에
    "qz_year6": ("delay", 6), "qz_year": ("delay", 12),   # 6 · 12개월 뒤 (v2.0 5번 — 참고)
}
QUIZ = [  # (번호, 키, 짧은 이름, 규칙 쪽 말, 미루지 않은 쪽 말, 정답 칸, 보기 A·B·C 의 칸) — 대본 v2.1 문제 순서·보기 순서와 같게
    (1, "qz_dip", "10% 빠지면 넣기(5년까지 기다림)", "10% 하락을 기다린 쪽", "바로 넣은 쪽", "rule", ("now", "rule", "even")),
    (2, "qz_dip1y", "10% 빠지면 넣기(1년까지만)", "기다린 쪽", "바로 넣은 쪽", "even", ("even", "now", "rule")),
    (3, "qz_split6", "6개월로 나눠 넣기", "나눠 넣은 쪽", "한 번에 넣은 쪽", "even", ("rule", "now", "even")),
    (4, "qz_sell6", "10% 빠진 날 매도·6개월 뒤 다시", "팔았다 다시 넣은 쪽", "그대로 둔 쪽", "rule", ("rule", "even", "now")),
    (5, "qz_wait3", "석 달 뒤 넣기", "석 달 뒤에 넣은 쪽", "지금 넣은 쪽", "even", ("now", "even", "rule")),
]
QUIZ_REF = ["qz_end", "qz_split", "qz_year6", "qz_year", "qz_sell3", "qz_sell9", "qz_sell12"]
QUESTIONS = [(n, name, False, {L: (20 if band == ans else 0) for L, band in zip("ABC", order)}) for n, _, name, _, _, ans, order in QUIZ]
VIRTUAL_BANDS = [   # 가상 응시 (실제 사람 아님) — 칸으로 고름 → 글자로 바꿔 채점
    ("V1 시기를 타는 규칙을 가려내는 사람", [q[5] for q in QUIZ]),
    ("V2 최근 상승장 상식만 (늘 미루지 않은 쪽)", ["now"] * 5),
    ("V3 늘 규칙 쪽", ["rule"] * 5),
    ("V4 늘 어느 쪽도 아님", ["even"] * 5),
    ("V5 4번만 틀린 사람 (하락에 파는 규칙을 어느 쪽도 아니라고 봄)", ["rule", "even", "even", "even", "even"]),
    ("V6 기다림·매도는 늘 진다고 보는 사람 (1·4번 미루지 않은 쪽 · 나머지 어느 쪽도 아님)", ["now", "even", "even", "now", "even"]),
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
    res["worst_dca_minus_lump_usd_per_100k"] = res["worst_dca_usd_per_100k"] - res["worst_lump_usd_per_100k"]
    res["verdict"] = "한 번에" if res["lump_wins"] > 0.5 and res["median_stop_pct"] < res["median_dca_pct"] else "다시 볼 것"
    return res


def q3b_speed(p, c, W):
    """v1.3: 빠져도 매도하지 않는 사람 — 넣는 속도만 다름: 한 번에 vs 12개월 vs 36개월로 나눠 (기다리는 돈은 국채 이자, 창 안에 못 넣은 몫은 현금).
    판정: 이 파일 머리의 규칙 그대로 — 쌍마다 이긴 구간 > 50% (한 번에 > 12개월 · 12개월 > 36개월 · 한 번에 > 36개월 이면 보기 점수 20·10·0).
    (처음엔 '셋 중 1등 몫 순서'로 했다가 5년에서 12개월·36개월 순서가 뒤집힘 — 머리 규칙과 다른 규칙이라 되돌림. best_* 는 참고로 남김.)"""
    def spread(s, e, buys, n):
        b = buys[:n]
        inv = sum(1 / n * c[x] / c[s] * p[e] / p[x] for x in b)
        return inv + (n - len(b)) / n * c[e] / c[s]
    v = np.array([[p[e] / p[s], spread(s, e, buys, SPLIT), spread(s, e, buys, 36)] for s, e, buys in W])
    best = np.argmax(v, axis=1)
    res = dict(windows=len(W), best_lump=share(best == 0), best_dca12=share(best == 1), best_dca36=share(best == 2),
               median_lump_pct=float(np.median(v[:, 0] - 1)), median_dca12_pct=float(np.median(v[:, 1] - 1)),
               median_dca36_pct=float(np.median(v[:, 2] - 1)), lump_beats_dca36=share(v[:, 0] > v[:, 2]),
               dca12_beats_dca36=share(v[:, 1] > v[:, 2]))
    res["lump_beats_dca12"] = share(v[:, 0] > v[:, 1])
    ok = res["lump_beats_dca12"] > 0.5 and res["dca12_beats_dca36"] > 0.5 and res["lump_beats_dca36"] > 0.5
    res["verdict"] = "한 번에>12개월>36개월" if ok else "다시 볼 것"
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
    now, wait, back, rise_days = [], [], [], []
    eligible = 0
    for s in ms:
        if d[s] < START_EVAL:
            continue
        if int(np.searchsorted(d, d[s] + timedelta(days=horizon_days), side="left")) < len(d):
            eligible += 1                               # v1.6: 그 시작에서 horizon 만큼 자료가 있는 달 (분모)
        seg = p[s + 1:]
        up = np.flatnonzero(seg >= (1 + rise) * p[s])
        dn = np.flatnonzero(seg <= (1 - DIP) * p[s])
        if not len(up) or (len(dn) and dn[0] < up[0]):
            continue                                   # 먼저 빠졌으면 이 조건이 아님
        t = s + 1 + up[0]
        e = int(np.searchsorted(d, d[t] + timedelta(days=horizon_days), side="left"))
        if e >= len(d):
            continue
        rise_days.append(t)
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
               median_gap_pct=float(np.median(now / wait - 1)) if len(now) else 0.0,
               median_gap_when_wait_wins_pct=float(np.median((now / wait - 1)[now < wait])) if np.any(now < wait) else 0.0,   # v1.4 진 때의 크기
               distinct_rise_days=len(set(rise_days)), episodes=episodes(d, sorted(set(rise_days)))["count"],
               episode_spans=" ".join(episodes(d, sorted(set(rise_days)))["spans"]), eligible_starts=eligible)
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
        for x in buys[MONTHLY:]:                       # v1.6 버그 고침 (반론 3회차 #4): 마지막 해 5~10월 몫도 창 안의 다음 11월에 넣음
            if cash_u > 0 and not (5 <= d[x].month <= 10):
                units += cash_u * c[x] / p[x]
                cash_u = 0.0
        avoid.append(units * p[e] + cash_u * c[e])
    mon, avoid = np.array(mon), np.array(avoid)
    res = dict(windows=len(W), monthly_wins=share(mon > avoid), median_gap_pct=float(np.median(mon / avoid - 1)),
               median_gap_usd_500=round(float(np.median(mon - avoid)) * 500), median_end_usd_500=round(float(np.median(mon)) * 500),   # v1.4 500달러 × 24번
               within_3pct=share(np.abs(mon / avoid - 1) <= 0.03))
    res["verdict"] = "매달" if res["monthly_wins"] > 0.5 else "5~10월 피하기"
    return res


# ---------- v1.4: 1회차 반론 검토(대본_반론_검토.md 1회차)에 답하는 계산 ----------
def episodes(d, idxs, gap_days=180):
    """시작 날들을 하락기(묶음)로 묶어 셈 — 앞 시작과 gap_days 넘게 떨어지면 새 묶음. 겹친 구간을 '몇 번의 일'로 말하려고."""
    idxs = sorted(int(i) for i in idxs)
    groups = []
    for i in idxs:
        if groups and (d[i] - d[groups[-1][-1]]).days <= gap_days:
            groups[-1].append(i)
        else:
            groups.append([i])
    return {"count": len(groups), "spans": [f"{d[g[0]].isoformat()[:7]}~{d[g[-1]].isoformat()[:7]}({len(g)})" for g in groups]}


def ath_flags(gd, gp, d):
    """가격 지수(^GSPC — 뉴스의 '사상 최고가') 종가가 그날까지의 모든 종가보다 높은 날. 배당 포함 지수 날짜에 맞춤 (그날까지 값만 씀)."""
    cm = np.maximum.accumulate(gp)
    a = np.concatenate([[False], gp[1:] > cm[:-1]])
    pos = {x: i for i, x in enumerate(gd)}
    idx = np.array([pos.get(x, -1) for x in d])
    ok = idx >= 0
    out("ALIGN", series="gspc→sp500tr", days=len(d), missing=int((~ok).sum()))
    return np.where(ok, a[np.clip(idx, 0, None)], False), np.where(ok, gp[np.clip(idx, 0, None)], np.nan)


def q1b_ath_wait(d, p, c, ath, gpx, horizon_days, near=63):
    """v1.4 항목 1: 가격 지수 최고가인 날 — 바로 넣기 vs 그날 값보다 10% 빠지면 넣기 (가격 지수로 봄 · 그동안 국채 이자 · 끝까지 안 빠지면 현금).
    + 같은 시기 비교 (심슨 역설 점검): 최고가 날의 손실 비율 vs 그 앞뒤 near 거래일의 최고가 아닌 날 손실 비율 vs 아무 날."""
    ends = np.searchsorted(d, d + timedelta(days=horizon_days), side="left")
    valid = (d >= START_EVAL) & (ends < len(d))
    r = np.full(len(d), np.nan)
    r[valid] = p[ends[valid]] / p[valid] - 1
    now, wait, back, starts, nb = [], [], [], [], []
    for i in np.flatnonzero(ath & valid):
        e = ends[i]
        hit = np.flatnonzero(gpx[i + 1:e + 1] <= (1 - DIP) * gpx[i])
        now.append(p[e] / p[i])
        if len(hit):
            j = i + 1 + hit[0]
            wait.append(c[j] / c[i] * p[e] / p[j])
            back.append(True)
        else:
            wait.append(c[e] / c[i])
            back.append(False)
        starts.append(i)
        lo, hi = max(0, i - near), min(len(d), i + near + 1)
        m = valid[lo:hi] & ~ath[lo:hi]
        if m.any():
            nb.append(float(np.mean(r[lo:hi][m] < 0)))
    now, wait = np.array(now), np.array(wait)
    g = now / wait - 1
    res = dict(ath_days=len(now), now_wins=share(now > wait), dip_came=share(np.array(back)), median_gap_pct=float(np.median(g)),
               median_gap_when_wait_wins_pct=float(np.median(g[now < wait])), loss_ath=share(now < 1),
               loss_near_same_time=float(np.mean(nb)), loss_all=share(r[valid] < 0), episodes=episodes(d, starts, 365)["count"])
    res["verdict"] = "지금" if res["now_wins"] > 0.5 else "기다림"
    return res


def q3s_stop_rebuy(d, p, c, W):
    """v1.4 항목 3: 한 번에 넣은 뒤 넣은 값보다 10% 빠진 날(그날 종가) 모두 매도 → 그 뒤 처음 넣은 값 이상이 된 날 다시 모두 넣기
    (끝까지 안 돌아오면 현금 — 국채 이자) vs 그대로 보유. 10% 빠짐이 일어난 구간만 (나머지는 둘이 같음)."""
    hold, stop, starts = [], [], []
    for s, e, _ in W:
        hit = np.flatnonzero(p[s + 1:e + 1] <= (1 - DIP) * p[s])
        if not len(hit):
            continue
        j = s + 1 + hit[0]
        val = p[j] / p[s]                                  # 판 돈 (처음 1 기준)
        bk = np.flatnonzero(p[j + 1:e + 1] >= p[s])
        if len(bk):
            k = j + 1 + bk[0]
            stop.append(val * c[k] / c[j] * p[e] / p[k])
        else:
            stop.append(val * c[e] / c[j])
        hold.append(p[e] / p[s])
        starts.append(s)
    hold, stop = np.array(hold), np.array(stop)
    g = hold / stop - 1
    res = dict(windows=len(W), triggered=len(hold), hold_wins=share(hold > stop), median_gap_pct=float(np.median(g)),
               median_gap_when_stop_wins_pct=float(np.median(g[hold < stop])) if np.any(hold < stop) else 0.0,
               median_hold_pct=float(np.median(hold - 1)), median_stop_pct=float(np.median(stop - 1)), episodes=episodes(d, starts)["count"])
    res["verdict"] = "보유" if res["hold_wins"] > 0.5 else "매도"
    return res


def q4b_stop_reenter(d, p, c, W):
    """v1.4 항목 4: 12개월로 나눠 넣다가, 넣는 날 값이 첫날보다 10% 아래면 멈춤 → 그 뒤 처음으로 첫날 값 이상이 된 날 남은 돈을 한꺼번에
    (끝까지 안 돌아오면 현금 — 국채 이자) vs 계획대로 계속. 멈춤이 일어난 구간만 (나머지는 둘이 같음)."""
    cont, stop, starts = [], [], []
    for s, e, buys in W:
        b = buys[:SPLIT]
        k = next((i for i in range(1, len(b)) if p[b[i]] <= (1 - DIP) * p[b[0]]), None)
        if k is None:
            continue
        cont.append(dca_value(p, c, s, e, b, SPLIT))
        inv = sum(1 / SPLIT * c[x] / c[s] * p[e] / p[x] for x in b[:k])
        rest = (SPLIT - k) / SPLIT
        bk = np.flatnonzero(p[b[k] + 1:e + 1] >= p[b[0]])
        if len(bk):
            j = b[k] + 1 + bk[0]
            stop.append(inv + rest * c[j] / c[s] * p[e] / p[j])
        else:
            stop.append(inv + rest * c[e] / c[s])
        starts.append(s)
    cont, stop = np.array(cont), np.array(stop)
    g = cont / stop - 1
    ep = episodes(d, starts)
    res = dict(windows=len(W), triggered=len(cont), continue_wins=share(cont > stop), median_gap_pct=float(np.median(g)),
               median_gap_when_stop_wins_pct=float(np.median(g[cont < stop])) if np.any(cont < stop) else 0.0,
               episodes=ep["count"], episode_spans=" ".join(ep["spans"]))
    res["verdict"] = "계속" if res["continue_wins"] > 0.5 else "멈춤"
    return res


def path_drawdown(p, c, W, n):
    """v1.4 항목 3: 넣기 시작한 뒤 끝까지, 날마다 전체 돈(넣은 돈 + 기다리는 현금)이 처음 돈보다 가장 많이 줄었던 비율 — 구간마다 하나."""
    mins = []
    for s, e, buys in W:
        t = np.arange(s, e + 1)
        if n == 1:
            v = p[t] / p[s]
        else:
            b = np.array(buys[:n])
            units = (1 / n) * (c[b] / c[s]) / p[b]
            k = np.searchsorted(b, t, side="right")             # t 까지 넣은 횟수
            cu = np.concatenate([[0.0], np.cumsum(units)])[k]
            v = cu * p[t] + (n - k) / n * c[t] / c[s]
        mins.append(float(np.min(v) - 1))
    mins = np.array(mins)
    return {"share_dd_over_20": share(mins < -0.20), "worst_dd_pct": float(np.min(mins))}


def calendar_years(d, p, y0=2000, y1=2025):
    """v1.4 항목 5: 해마다 5~10월(5월 첫 거래일 → 11월 첫 거래일)과 11~4월 수익 (배당 포함). 오른 해 수 · 평균."""
    def first(y, m):
        i = np.searchsorted(d, date(y, m, 1))
        return int(i) if i < len(d) else None
    mo, no = [], []
    for y in range(y0, y1 + 1):
        a, b, nxt = first(y, 5), first(y, 11), first(y + 1, 5)
        if a is None or b is None:
            continue
        mo.append(p[b] / p[a] - 1)
        if nxt is not None:
            no.append(p[nxt] / p[b] - 1)
    mo, no = np.array(mo), np.array(no)
    return {"years": len(mo), "may_oct_up_years": int((mo > 0).sum()), "may_oct_mean_pct": float(mo.mean()), "nov_apr_mean_pct": float(no.mean())}


def intro2(d, p, c, ath, gpx, year):
    """v1.4 도입: 올해 처음 사상 최고가(가격 지수)를 쓴 날 — '10% 빠지면 넣겠다'던 사람이 넣었나 · 그 뒤 배당 포함 수익 · 기다린 현금 이자."""
    idx = np.flatnonzero(ath & np.array([x.year == year for x in d]))
    i = int(idx[0])
    m = float(np.nanmin(gpx[i:]) / gpx[i] - 1)
    mi = i + int(np.nanargmin(gpx[i:]))
    up = np.flatnonzero(gpx[i + 1:] >= 1.10 * gpx[i])
    return {"first_ath_day": d[i].isoformat(), "price_index_min_after_pct": m, "min_after_day": d[mi].isoformat(), "dipped_10": bool(m <= -DIP),
            "price_index_gain_since_pct": float(gpx[-1] / gpx[i] - 1), "rose_10_first_day": d[i + 1 + up[0]].isoformat() if len(up) else "-",
            "gain_since_pct": float(p[-1] / p[i] - 1), "cash_interest_pct": float(c[-1] / c[i] - 1), "last_date": d[-1].isoformat()}


# ---------- v1.5: 반론 검토 2회차에 답하는 계산 ----------
def q2c_ath_wait_after_rise(d, p, c, ath, gpx, horizon_days, rise=0.10):
    """v1.5 항목 1 (사연대로): 가격 지수 최고가인 날 '10% 빠지면 넣겠다'고 기다림 → 10% 빠지기 전에 먼저 10% 오른 날(t, 가격 지수로 봄)
    → 그때 지금 넣기 vs 처음 목표값(최고가 날 값의 90%)까지 계속 기다림. t 뒤 horizon_days 에 비교 (끝까지 안 오면 현금)."""
    now, wait, back, rise_days = [], [], [], []
    for s in np.flatnonzero(ath):
        if d[s] < START_EVAL:
            continue
        seg = gpx[s + 1:]
        up = np.flatnonzero(seg >= (1 + rise) * gpx[s])
        dn = np.flatnonzero(seg <= (1 - DIP) * gpx[s])
        if not len(up) or (len(dn) and dn[0] < up[0]):
            continue
        t = s + 1 + up[0]
        e = int(np.searchsorted(d, d[t] + timedelta(days=horizon_days), side="left"))
        if e >= len(d):
            continue
        hit = np.flatnonzero(gpx[t + 1:e + 1] <= (1 - DIP) * gpx[s])
        now.append(p[e] / p[t])
        if len(hit):
            j = t + 1 + hit[0]
            wait.append(c[j] / c[t] * p[e] / p[j])
            back.append(True)
        else:
            wait.append(c[e] / c[t])
            back.append(False)
        rise_days.append(t)
    now, wait = np.array(now), np.array(wait)
    g = now / wait - 1
    res = dict(cases=len(now), distinct_rise_days=len(set(rise_days)), episodes=episodes(d, sorted(set(rise_days)))["count"],
               now_wins=share(now > wait), came_back_to_target=share(np.array(back)), median_gap_pct=float(np.median(g)),
               median_gap_when_wait_wins_pct=float(np.median(g[now < wait])) if np.any(now < wait) else 0.0)
    res["verdict"] = "지금" if res["now_wins"] > 0.5 else "기다림"
    return res


def q3s_detail(d, p, c, W):
    """v1.5 항목 3 까닭: 넣은 값으로 돌아온 경우와 아닌 경우로 나눔 + 다른 재진입(판 뒤 가장 낮은 값에서 10% 반등한 날 다시)도 확인."""
    rec, hw_rec, sw_norec, hold2, reb = [], [], [], [], []
    for s, e, _ in W:
        hit = np.flatnonzero(p[s + 1:e + 1] <= (1 - DIP) * p[s])
        if not len(hit):
            continue
        j = s + 1 + hit[0]
        val = p[j] / p[s]
        hold = p[e] / p[s]
        bk = np.flatnonzero(p[j + 1:e + 1] >= p[s])
        if len(bk):
            k = j + 1 + bk[0]
            stop = val * c[k] / c[j] * p[e] / p[k]
            rec.append(True)
            hw_rec.append(hold > stop)
        else:
            stop = val * c[e] / c[j]
            rec.append(False)
            sw_norec.append(stop > hold)
        lows = np.minimum.accumulate(p[j:e + 1])
        rb = np.flatnonzero(p[j:e + 1] >= 1.10 * lows)
        if len(rb):
            k2 = j + rb[0]
            alt = val * c[k2] / c[j] * p[e] / p[k2]
        else:
            alt = val * c[e] / c[j]
        hold2.append(hold)
        reb.append(alt)
    hold2, reb = np.array(hold2), np.array(reb)
    return {"recovered": share(np.array(rec)), "hold_wins_when_recovered": share(np.array(hw_rec)),
            "stop_wins_when_not_recovered": share(np.array(sw_norec)), "hold_wins_vs_rebound10": share(hold2 > reb),
            "median_gap_vs_rebound10_pct": float(np.median(hold2 / reb - 1))}


def q6b_sell_in_may(d, p, c, W):
    """v1.5 항목 5 격언 원래 꼴: 24개월 매달 넣되, 해마다 5월 첫 거래일에 모두 매도해 현금 → 11월 첫 거래일에 모두 다시 넣기 (5~10월 넣을 돈도 현금)
    vs 매달 넣고 그대로. 5년 창 끝까지 같은 규칙을 이어 감."""
    mon, may = [], []
    for s, e, buys in W:
        b = buys[:MONTHLY]
        mon.append(sum(p[e] / p[x] for x in b))
        units, cash_u = 0.0, 0.0
        for n, x in enumerate(buys):
            m = d[x].month
            if n < MONTHLY:
                cash_u += 1 / c[x]
            if m == 5 and units > 0:
                cash_u += units * p[x] / c[x]
                units = 0.0
            if not (5 <= m <= 10) and cash_u > 0:
                units += cash_u * c[x] / p[x]
                cash_u = 0.0
        may.append(units * p[e] + cash_u * c[e])
    mon, may = np.array(mon), np.array(may)
    g = mon / may - 1
    return {"monthly_wins": share(mon > may), "median_gap_pct": float(np.median(g)),
            "median_gap_when_may_wins_pct": float(np.median(g[mon < may])) if np.any(mon < may) else 0.0}   # v1.6 진 때 크기


def nonoverlap(ms, mkey, d, months):
    """겹치지 않는 창 수 — 2000년 1월부터 months 개월씩 이어 자를 때."""
    keys = [k for i, k in zip(ms, mkey[ms]) if d[i] >= START_EVAL]
    return int((keys[-1] - keys[0]) // months)


# ---------- v1.6: 반론 검토 3회차에 답하는 계산 ----------
def q10_wait_months(p, c, W, k=12):
    """v1.6 항목 4: 목돈을 지금 한 번에 넣기 vs '앞일이 분명해지면' k 개월 뒤 한 번에 넣기 (그동안 국채 이자)."""
    now, later = [], []
    for s, e, buys in W:
        if len(buys) <= k:
            continue
        j = buys[k]
        now.append(p[e] / p[s])
        later.append(c[j] / c[s] * p[e] / p[j])
    now, later = np.array(now), np.array(later)
    g = now / later - 1
    res = dict(windows=len(now), now_wins=share(now > later), median_gap_pct=float(np.median(g)),
               median_gap_when_wait_wins_pct=float(np.median(g[now < later])) if np.any(now < later) else 0.0)
    res["verdict"] = "지금" if res["now_wins"] > 0.5 else "기다림"
    return res


def q4c_stop_rebound(p, c, W):
    """v1.6 참고 (반론 3회차 #1): q4b 의 재진입을 '멈춘 뒤 가장 낮은 종가보다 10% 오른 날'로 바꿈 → 계속 넣기와 비교."""
    cont, stop = [], []
    for s, e, buys in W:
        b = buys[:SPLIT]
        k = next((i for i in range(1, len(b)) if p[b[i]] <= (1 - DIP) * p[b[0]]), None)
        if k is None:
            continue
        cont.append(dca_value(p, c, s, e, b, SPLIT))
        inv = sum(1 / SPLIT * c[x] / c[s] * p[e] / p[x] for x in b[:k])
        rest = (SPLIT - k) / SPLIT
        lows = np.minimum.accumulate(p[b[k]:e + 1])
        rb = np.flatnonzero(p[b[k]:e + 1] >= 1.10 * lows)
        if len(rb):
            j = b[k] + rb[0]
            stop.append(inv + rest * c[j] / c[s] * p[e] / p[j])
        else:
            stop.append(inv + rest * c[e] / c[s])
    cont, stop = np.array(cont), np.array(stop)
    res = dict(triggered=len(cont), continue_wins=share(cont > stop), median_gap_pct=float(np.median(cont / stop - 1)))
    res["verdict"] = "계속" if res["continue_wins"] > 0.5 else "멈춤"
    return res


def q6b_verdict(d, p, c, W):
    r = q6b_sell_in_may(d, p, c, W)
    r["verdict"] = "매달" if r["monthly_wins"] > 0.5 else "격언대로"
    return r


# ---------- v1.7: 반론 검토 4회차에 답하는 계산 (모두 참고 — 점수 밖) ----------
def q2d_wait_with_end(d, p, c, W):
    """v1.7 참고: 처음부터 '10% 빠지거나, 먼저 10% 오르면 그날 넣기'(끝을 정한 기다림) vs 바로 넣기."""
    now, rule = [], []
    for s, e, _ in W:
        seg = p[s + 1:e + 1]
        dn = np.flatnonzero(seg <= (1 - DIP) * p[s])
        up = np.flatnonzero(seg >= (1 + DIP) * p[s])
        cand = [x for x in (dn[0] if len(dn) else None, up[0] if len(up) else None) if x is not None]
        now.append(p[e] / p[s])
        if cand:
            j = s + 1 + min(cand)
            rule.append(c[j] / c[s] * p[e] / p[j])
        else:
            rule.append(c[e] / c[s])
    now, rule = np.array(now), np.array(rule)
    return {"now_wins": share(now > rule), "median_gap_pct": float(np.median(now / rule - 1))}


def q2e_rewait(d, p, c, horizon_days):
    """v1.7 참고: q2b 의 '먼저 10% 오른 날' t 에서 — 지금 넣기 vs 그날 값 기준으로 다시 10% 빠지면 넣기 (끝까지 안 오면 현금)."""
    ms = np.flatnonzero(np.concatenate([[True], np.array([x.month for x in d[1:]]) != np.array([x.month for x in d[:-1]])]))
    now, wait = [], []
    for s in ms:
        if d[s] < START_EVAL:
            continue
        seg = p[s + 1:]
        up = np.flatnonzero(seg >= 1.10 * p[s])
        dn = np.flatnonzero(seg <= (1 - DIP) * p[s])
        if not len(up) or (len(dn) and dn[0] < up[0]):
            continue
        t = s + 1 + up[0]
        e = int(np.searchsorted(d, d[t] + timedelta(days=horizon_days), side="left"))
        if e >= len(d):
            continue
        hit = np.flatnonzero(p[t + 1:e + 1] <= (1 - DIP) * p[t])
        now.append(p[e] / p[t])
        wait.append(c[t + 1 + hit[0]] / c[t] * p[e] / p[t + 1 + hit[0]] if len(hit) else c[e] / c[t])
    now, wait = np.array(now), np.array(wait)
    return {"cases": len(now), "now_wins": share(now > wait), "median_gap_pct": float(np.median(now / wait - 1))}


def q3t_rebuy_after(d, p, c, W, months=(3, 4, 6, 9, 12)):
    """v1.7 참고: 넣은 뒤 10% 빠진 날 매도 → N 개월(30.4일×N) 뒤 첫 거래일에 다시 모두 넣기 vs 그대로 두기."""
    out_ = {}
    for n in months:
        hold, alt = [], []
        for s, e, _ in W:
            hit = np.flatnonzero(p[s + 1:e + 1] <= (1 - DIP) * p[s])
            if not len(hit):
                continue
            j = s + 1 + hit[0]
            k = int(np.searchsorted(d, d[j] + timedelta(days=round(30.4 * n)), side="left"))
            val = p[j] / p[s]
            alt.append(val * c[k] / c[j] * p[e] / p[k] if k < e else val * c[e] / c[j])
            hold.append(p[e] / p[s])
        hold, alt = np.array(hold), np.array(alt)
        out_[f"m{n}"] = share(hold > alt)
    return out_


# ---------- v2.0: 문제형 계산 ----------
def quiz_pairs(key, d, p, c, W):
    """v2.1 문제마다 구간별 (미루지 않은 쪽 값, 규칙 쪽 값, 시작 인덱스) — 규칙은 QZ_SPEC. 위 함수와 같은 규칙은 selftest 가 비율을 대조:
    qz_dip = q2_wait · qz_end = q2d_wait_with_end · qz_split = q3b_speed(한 번에 vs 12개월) · qz_sell6 = q3t_rebuy_after m6 · qz_year = q10_wait_months(12)."""
    kind, v = QZ_SPEC[key]
    now, rule, st = [], [], []
    for s, e, buys in W:
        if kind in ("dip", "end"):
            lim = e if kind == "end" or v is None else (buys[v] if len(buys) > v else None)   # dip 1년까지: 12개월째 첫 거래일
            if lim is None:
                continue
            seg = p[s + 1:lim + 1]
            dn = np.flatnonzero(seg <= (1 - DIP) * p[s])
            up = np.flatnonzero(seg >= (1 + v) * p[s]) if kind == "end" else np.array([], dtype=int)
            cand = [x[0] for x in (dn, up) if len(x)]
            j = s + 1 + min(cand) if cand else (lim if kind == "dip" and v is not None else None)
            b = c[j] / c[s] * p[e] / p[j] if j is not None else c[e] / c[s]     # 끝까지 안 오면 현금(국채 이자)
        elif kind == "split":
            bb = buys[:v]
            b = sum(1 / v * c[x] / c[s] * p[e] / p[x] for x in bb) + (v - len(bb)) / v * c[e] / c[s]
        elif kind == "sell":
            hit = np.flatnonzero(p[s + 1:e + 1] <= (1 - DIP) * p[s])
            if not len(hit):
                continue                                                          # 넣은 뒤 10% 빠진 구간만
            j = s + 1 + hit[0]
            k = int(np.searchsorted(d, d[j] + timedelta(days=round(30.4 * v)), side="left"))
            b = p[j] / p[s] * (c[k] / c[j] * p[e] / p[k] if k < e else c[e] / c[j])
        elif kind == "delay":
            if len(buys) <= v:
                continue
            j = buys[v]
            b = c[j] / c[s] * p[e] / p[j]
        else:
            raise ValueError(key)
        now.append(p[e] / p[s])
        rule.append(b)
        st.append(s)
    return np.array(now), np.array(rule), np.array(st, dtype=int)


def quiz_cell(now, rule):
    """한 칸 (시기 × 기간): 미루지 않은 쪽이 이긴 몫 · 수 · 가운데 값 차이 · 진 때·이긴 때 가운데 값 · 10만 달러 기준 가운데 값."""
    if not len(now):
        return {"n": 0}
    g = now / rule - 1
    return {"n": int(len(now)), "now_wins": share(now > rule), "median_gap_pct": float(np.median(g)),
            "median_gap_when_rule_wins_pct": float(np.median(g[now < rule])) if np.any(now < rule) else 0.0,
            "median_gap_when_now_wins_pct": float(np.median(g[now > rule])) if np.any(now > rule) else 0.0,
            "median_now_usd_100k": round(100000 * float(np.median(now))), "median_rule_usd_100k": round(100000 * float(np.median(rule))),
            "now_count": int(np.sum(now > rule)), "rule_count": int(np.sum(now < rule)),
            "mean_diff_usd_100k": round(100000 * float(np.mean(now - rule))), "mean_gap_pct": float(np.mean(g))}   # 평균 = 10만 달러당 (미루지 않은 쪽 − 규칙 쪽)


def band_of(x):
    """v2.1 칸 (빈틈 없음): 미루지 않은 쪽이 이긴 몫 < 40% = rule · > 60% = now · 그 사이 = even."""
    return "rule" if x < 0.40 else ("now" if x > 0.60 else "even")


def quiz_run(d, p, c, ms, mkey):
    """v2.1 문제(QUIZ)·참고(QUIZ_REF) × (2년·5년) × (앞 시기 경계 넷 · 뒤 · 전체 · 다른 자르기). 칸 판정 · 정답과 같은지 · 뒤 시기 전제."""
    yr = np.array([x.year for x in d])
    out_ = {}
    answers = {q[1]: q[5] for q in QUIZ}
    for key in [q[1] for q in QUIZ] + QUIZ_REF:
        r = {"name": next((q[2] for q in QUIZ if q[1] == key), key), "answer": answers.get(key, "-")}
        for label, months in (("2y", 24), ("5y", 60)):
            Wall = windows(ms, mkey, d, months)
            now, rule, st = quiz_pairs(key, d, p, c, Wall)
            y = yr[st]
            hb = Wall[len(Wall) // 2][0]                                      # 다른 자르기: 모든 시작 달을 수로 정확히 반 (문제마다 같은 경계)
            cells = {"early": quiz_cell(now[(y >= QUIZ_EARLY[0]) & (y <= QUIZ_EARLY[1])], rule[(y >= QUIZ_EARLY[0]) & (y <= QUIZ_EARLY[1])]),
                     "late": quiz_cell(now[y >= QUIZ_LATE_FROM], rule[y >= QUIZ_LATE_FROM]),
                     "late2010": quiz_cell(now[y >= QUIZ_LATE_FROM + 1], rule[y >= QUIZ_LATE_FROM + 1]),
                     "all": quiz_cell(now, rule),
                     "half1": quiz_cell(now[st < hb], rule[st < hb]), "half2": quiz_cell(now[st >= hb], rule[st >= hb]),
                     "half_boundary": d[hb].isoformat()}
            for a, b in QUIZ_EARLY_DEFS:
                m = (y >= a) & (y <= b)
                cells[f"e{a}_{b}"] = quiz_cell(now[m], rule[m])
            for a, b in ((2000, 2004), (2005, 2008), (2009, 2013), (2014, 2018), (2019, 2099)):
                m = (y >= a) & (y <= b)
                cells[f"y{a}_{min(b, 2026)}"] = quiz_cell(now[m], rule[m])
            if key == "qz_dip":                                               # 해설: 기다린 사람이 끝까지 못 넣은 몫 (= 시작한 날 값보다 10% 싼 날이 없었던 몫)
                for per, m in (("early", (y >= QUIZ_EARLY[0]) & (y <= QUIZ_EARLY[1])), ("late", y >= QUIZ_LATE_FROM)):
                    sm = set(st[m].tolist())
                    cells[per]["never_bought"] = share(np.array([not len(np.flatnonzero(p[s_ + 1:e_ + 1] <= (1 - DIP) * p[s_])) for s_, e_, _ in Wall if s_ in sm]))
            if key == "qz_sell6":                                             # 해설: 6개월 뒤 다시 넣은 값이 판 값보다 비쌌던 몫
                for per, m in (("early", (y >= QUIZ_EARLY[0]) & (y <= QUIZ_EARLY[1])), ("late", y >= QUIZ_LATE_FROM)):
                    hi, sm = [], set(st[m].tolist())
                    for s_, e_, _ in Wall:
                        if s_ not in sm:
                            continue
                        j = s_ + 1 + np.flatnonzero(p[s_ + 1:e_ + 1] <= (1 - DIP) * p[s_])[0]
                        k = int(np.searchsorted(d, d[j] + timedelta(days=round(30.4 * 6)), side="left"))
                        if k < e_:
                            hi.append(p[k] > p[j])
                    cells[per]["rebuy_higher"] = share(np.array(hi))
                    cells[per]["rebuy_n"] = len(hi)
            r[label] = cells
        b5 = {band_of(r["5y"][f"e{a}_{b}"]["now_wins"]) for a, b in QUIZ_EARLY_DEFS}
        b2 = {band_of(r["2y"][f"e{a}_{b}"]["now_wins"]) for a, b in QUIZ_EARLY_DEFS}
        r["early_band"] = b5.pop() if len(b5) == 1 else "gap"
        r["early_range_5y"] = [min(r["5y"][f"e{a}_{b}"]["now_wins"] for a, b in QUIZ_EARLY_DEFS), max(r["5y"][f"e{a}_{b}"]["now_wins"] for a, b in QUIZ_EARLY_DEFS)]
        r["early_range_2y"] = [min(r["2y"][f"e{a}_{b}"]["now_wins"] for a, b in QUIZ_EARLY_DEFS), max(r["2y"][f"e{a}_{b}"]["now_wins"] for a, b in QUIZ_EARLY_DEFS)]
        side = {"rule": lambda x: x < 0.5, "now": lambda x: x > 0.5, "even": lambda x: 0.40 <= x <= 0.60}.get(r["early_band"], lambda x: False)
        r["two_year"] = ("same_band" if b2 == {r["early_band"]} else
                         "same_side" if all(side(r["2y"][f"e{a}_{b}"]["now_wins"]) for a, b in QUIZ_EARLY_DEFS) else "differs")
        r["late_ok"] = min(r["5y"]["late"]["now_wins"], r["5y"]["late2010"]["now_wins"], r["2y"]["late"]["now_wins"]) > LATE_MIN
        r["matches_answer"] = r["early_band"] == r["answer"] and r["late_ok"] and r["two_year"] != "differs"
        out_[key] = r
    return out_


def big_declines(gd, gp, thr=CRASH, since=START_EVAL):
    """v2.0 해설: ^GSPC(가격 지수) 종가가 그때까지 최고 종가보다 thr 넘게 빠진 하락 — 최고가 날 · 바닥 날 · 깊이 · 최고가를 되찾은 날."""
    eps, peak, i, n = [], 0, 1, len(gp)
    while i < n:
        if gp[i] >= gp[peak]:
            peak = i
        elif gp[i] <= (1 - thr) * gp[peak]:
            rec = np.flatnonzero(gp[i:] >= gp[peak])
            end = i + int(rec[0]) if len(rec) else n
            t = peak + int(np.argmin(gp[peak:end]))
            if gd[peak] >= since:
                eps.append({"peak": gd[peak].isoformat(), "trough": gd[t].isoformat(), "depth_pct": float(gp[t] / gp[peak] - 1),
                            "recovered": gd[end].isoformat() if end < n else "-",
                            "years_peak_to_recover": round((gd[end] - gd[peak]).days / 365.25, 1) if end < n else None,
                            "months_trough_to_recover": round((gd[end] - gd[t]).days / 30.44, 1) if end < n else None})
            if end >= n:
                break
            peak, i = end, end
        i += 1
    return eps


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
    rng = np.random.default_rng(7)                                     # v2.0 quiz_pairs 가 기존 함수와 같은 규칙인지 (막걸음 가짜 자료 · seed=7)
    walk = np.exp(np.cumsum(rng.normal(0.0003, 0.012, len(d))))
    cw = np.cumprod(np.full(len(d), 1 + 0.02 / 365))
    W5 = windows(ms, mkey, d, 24)
    same = {"qz_dip": q2_wait(walk, cw, W5)["now_wins"], "qz_end": q2d_wait_with_end(d, walk, cw, W5)["now_wins"],
            "qz_split": q3b_speed(walk, cw, W5)["lump_beats_dca12"], "qz_sell6": q3t_rebuy_after(d, walk, cw, W5, (6,))["m6"],
            "qz_year": q10_wait_months(walk, cw, W5, 12)["now_wins"]}
    for key, v in same.items():
        a, b, _ = quiz_pairs(key, d, walk, cw, W5)
        ok.append(len(a) > 0 and abs(share(a > b) - v) < 1e-12)
    a, b, _ = quiz_pairs("qz_dip1y", d, rise, c0, W)                   # 오르기만 하면: 1년까지 기다린 쪽은 12개월째에 더 비싸게 삼 → 늘 짐
    ok.append(len(a) > 0 and share(a > b) == 1.0)
    a, b, _ = quiz_pairs("qz_dip1y", d, vshape, c0, W[:3])             # 처음 석 달 시작: 1년 안에 10% 아래를 지남 → 기다린 쪽이 늘 이김
    ok.append(len(a) == 3 and share(a > b) == 0.0)
    ok.append(QUESTIONS[0][3] == {"A": 0, "B": 20, "C": 0})            # 보기 순서 → 점수 (1번 정답 B)
    out("SELFTEST", checks=len(ok), passed=sum(ok), result="OK" if all(ok) else "FAIL")
    if not all(ok):
        raise SystemExit("[SELFTEST] 실패 — 규칙 코드를 다시 볼 것")


def fmt(res):
    return {k: (pctf(v) if isinstance(v, float) and ("pct" in k or k.startswith(("loss", "now", "lump", "never", "stop", "continue", "monthly", "no_", "triggered_", "median", "came_", "best_", "dca", "dip_", "dd20", "worst_dd", "within", "price_", "gain_", "cash_", "may_oct_m", "nov_", "hold_", "recovered", "stop_wins", "sell_in_may"))) else v)
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
    ath, gpx = ath_flags(gd, gp, d)
    for label, months, days in (("2y", 24, 730), ("5y", 60, 1826)):
        W = windows(ms, mkey, d, months)
        out("SPLIT", horizon=label, windows=len(W), first_start=d[W[0][0]], last_start=d[W[-1][0]], last_end=d[W[-1][1]])
        r = {"q1": q1_ath(d, p, START_EVAL, days), "q2": q2_wait(p, c, W), "q3": q3_lump(p, c, W), "q4": q4_stop(p, c, W), "q5": q5_crash(p, c, W),
             "q2b": q2b_wait_after_rise(d, p, c, days), "q6": q6_calendar(d, p, c, W), "q3b": q3b_speed(p, c, W),
             "q1b": q1b_ath_wait(d, p, c, ath, gpx, days), "q4b": q4b_stop_reenter(d, p, c, W), "q3s": q3s_stop_rebuy(d, p, c, W),
             "q2c": q2c_ath_wait_after_rise(d, p, c, ath, gpx, days), "q10": q10_wait_months(p, c, W, 12),
             "q4c": q4c_stop_rebound(p, c, W), "q6b": q6b_verdict(d, p, c, W),
             "q2d": q2d_wait_with_end(d, p, c, W), "q2e": q2e_rewait(d, p, c, days), "q3t": q3t_rebuy_after(d, p, c, W)}
        for key in ("lump", "dca12", "dca36"):                                      # v1.7 '가운데 값' 을 달러로 (10만 달러 기준)
            r["q3b"][f"median_{key}_usd_100k"] = round(100000 * (1 + r["q3b"][f"median_{key}_pct"]))
        r["q3s"].update(q3s_detail(d, p, c, W))
        r["q6"].update({f"sell_in_may_{k}": v for k, v in q6b_sell_in_may(d, p, c, W).items()})
        r["q6"]["nonoverlap_windows"] = nonoverlap(ms, mkey, d, months)
        c5 = np.cumprod(1 + 0.05 * np.array([0] + [(d[i] - d[i - 1]).days for i in range(1, len(d))], dtype=float) / 365)   # 민감도: 현금 이자 연 5% 고정
        sens = {"q2b": q2b_wait_after_rise(d, p, c5, days), "q2c": q2c_ath_wait_after_rise(d, p, c5, ath, gpx, days), "q3b": q3b_speed(p, c5, W),
                "q3s": q3s_stop_rebuy(d, p, c5, W), "q4b": q4b_stop_reenter(d, p, c5, W), "q6": q6_calendar(d, p, c5, W),
                "q10": q10_wait_months(p, c5, W, 12), "q6b": q6b_verdict(d, p, c5, W)}
        r["sens_cash5"] = {"verdicts": {k: v["verdict"] for k, v in sens.items()},
                           "shares": {"q2b": sens["q2b"]["now_wins"], "q2c": sens["q2c"]["now_wins"], "q3b_lump_vs_dca12": sens["q3b"]["lump_beats_dca12"],
                                      "q3b_dca12_vs_dca36": sens["q3b"]["dca12_beats_dca36"], "q3s": sens["q3s"]["hold_wins"],
                                      "q4b": sens["q4b"]["continue_wins"], "q6": sens["q6"]["monthly_wins"], "q10": sens["q10"]["now_wins"],
                                      "q6b": sens["q6b"]["monthly_wins"]}}
        for n, key in ((1, "lump"), (SPLIT, "dca12"), (36, "dca36")):
            dd = path_drawdown(p, c, W, n)
            r["q3b"][f"dd20_{key}"], r["q3b"][f"worst_dd_{key}_pct"] = dd["share_dd_over_20"], dd["worst_dd_pct"]
        r["q3"]["worst_start"] = d[r["q3"].pop("worst_start_idx")].isoformat()
        for q, v in r.items():
            out(f"{q.upper()}", horizon=label, **(fmt(v) if q not in ("sens_cash5", "q3t") else
                                                  {"verdicts": v["verdicts"], "shares": {k: pctf(x) for k, x in v["shares"].items()}} if q == "sens_cash5" else
                                                  {k: pctf(x) for k, x in v.items()}))
        results[label] = r

    expect = {"q2b": "지금", "q3b": "한 번에>12개월>36개월", "q3s": "보유", "q10": "지금", "q6b": "매달"}   # v2.0 부터 참고 (v1.x 테스트 꼴 점수 항목 — 대본 v1.6 까지) · v1.6 점수 항목 1~5 (q4b 는 재진입 규칙에 따라 뒤집혀(q4c) 참고 · q2c 는 사례가 2013~2021 뿐이라 참고)   # 점수 항목 1~5 (v1.4: 1 = q2b · 2 = q3b · 3 = q3s · 4 = q4b · 5 = q6 / q1b 는 5년에서 뒤집혀 참고)
    mism = [q for q, v in expect.items() if results["2y"][q]["verdict"] != v]
    flips = [q for q in results["2y"] if "verdict" in results["2y"][q] and results["2y"][q]["verdict"] != results["5y"][q]["verdict"]]
    cash5_mism = {h: [q for q in expect if results[h]["sens_cash5"]["verdicts"].get(q, results[h][q]["verdict"]) != expect[q]] for h in ("2y", "5y")}
    (warn if any(cash5_mism.values()) else out)("SENS", check="현금 이자 연 5% 고정이어도 같은 쪽인가", mismatches=cash5_mism)
    used_flips = [q for q in flips if q in expect]
    (warn if mism else out)("SIGNAL", rule="쌍마다 이긴 구간 > 50% (2년이 본 결과)", expected=expect, mismatches=mism or "-",
                            note="MISMATCH 면 QUESTIONS 보기 점수를 다시 정할 것" if mism else "보기 점수와 계산이 같은 쪽")
    (warn if used_flips else out)("ROBUST", check="5년으로 늘려도 같은 쪽인가", flips_all=flips or "-", flips_in_scored=used_flips or "-")

    it = intro(gd, gp, d, p, 2026)
    out("INTRO", **fmt(it))
    it2 = intro2(d, p, c, ath, gpx, 2026)
    out("INTRO2", **fmt(it2))
    cal = calendar_years(d, p)
    cal["irx_mean_since_2000"] = float(np.mean(iv[id_ >= START_EVAL]))       # v1.6 설명란 '2000년 이후 평균 약 2%'
    out("CASH", irx_mean_since_2000=f"{cal['irx_mean_since_2000']:.2f}%")
    out("CALENDAR", **fmt(cal))
    it["v14"] = it2
    it["calendar"] = cal
    out("NOTE", reference_only="q2 10% 하락 대기 · q5 폭락 때만", why="5년에서 뒤집힘 — 오래 통하는 결론이 아니라 점수에 안 씀 (채널 설명 3-5)",
        q2_2y=pctf(results["2y"]["q2"]["now_wins"]), q2_5y=pctf(results["5y"]["q2"]["now_wins"]),
        q5_2y=pctf(results["2y"]["q5"]["monthly_wins"]), q5_5y=pctf(results["5y"]["q5"]["monthly_wins"]))
    # ---------- v2.1 문제형 ----------
    quiz = quiz_run(d, p, c, ms, mkey)
    c5 = np.cumprod(1 + 0.05 * np.array([0] + [(d[i] - d[i - 1]).days for i in range(1, len(d))], dtype=float) / 365)
    quiz5 = quiz_run(d, p, c5, ms, mkey)                                      # 민감도: 현금 이자 연 5% 고정
    for key, q in quiz.items():
        n = next((x[0] for x in QUIZ if x[1] == key), "ref")
        out("QUIZ", q=n, key=key, answer=q["answer"], early_band=q["early_band"], cash5_band=quiz5[key]["early_band"], two_year=q["two_year"], late_ok=q["late_ok"],
            early5y=f"{pctf(q['5y']['early']['now_wins'])}({q['5y']['early']['now_count']}/{q['5y']['early']['n']})",
            range5y="~".join(pctf(x) for x in q["early_range_5y"]), range2y="~".join(pctf(x) for x in q["early_range_2y"]),
            cash5_range5y="~".join(pctf(x) for x in quiz5[key]["early_range_5y"]),
            late5y=pctf(q["5y"]["late"]["now_wins"]), late5y_2010=pctf(q["5y"]["late2010"]["now_wins"]), late2y=pctf(q["2y"]["late"]["now_wins"]),
            all5y=pctf(q["5y"]["all"]["now_wins"]), all2y=pctf(q["2y"]["all"]["now_wins"]),
            mean5y_early=q["5y"]["early"]["mean_diff_usd_100k"], mean5y_late=q["5y"]["late"]["mean_diff_usd_100k"], mean5y_all=q["5y"]["all"]["mean_diff_usd_100k"],
            median5y_early=pctf(q["5y"]["early"]["median_gap_pct"]))
        out("QUIZ_ALT", key=key, **{f"{h}_{k}": pctf(q[h][k]["now_wins"]) for h in ("2y", "5y")
                                   for k in ("half1", "half2", "y2000_2004", "y2005_2008", "y2009_2013", "y2014_2018", "y2019_2026")},
            half_boundary_2y=q["2y"]["half_boundary"], half_boundary_5y=q["5y"]["half_boundary"])
    scored = [x[1] for x in QUIZ]
    qmis = [k for k in scored if not quiz[k]["matches_answer"]]
    qmis5 = [k for k in scored if not (quiz5[k]["early_band"] == quiz[k]["answer"] and quiz5[k]["late_ok"])]
    (warn if qmis or qmis5 else out)("QUIZ_CHECK", rule="앞 시기 경계 넷 모두 같은 칸(5년) = 정답 · 2년은 같은 칸 또는 같은 쪽 · 뒤 시기 > 60% · 이자 5% 도 같음",
                                     mismatches=qmis or "-", cash5_mismatches=qmis5 or "-",
                                     two_year={k: quiz[k]["two_year"] for k in scored},
                                     note="MISMATCH 면 문제에서 빼거나 정답 칸을 다시" if qmis or qmis5 else "정답 칸과 계산이 같음")
    # 결과를 본 뒤 더한 관찰 (반론 6회차 #1 — 두 시기를 합치면): even 묶음은 합쳐도 미루지 않은 쪽이 횟수·평균 모두 앞서나 · rule 묶음은 기간에 따라 갈리나
    combined = {k: {h: {"now_wins": quiz[k][h]["all"]["now_wins"], "mean_diff_usd_100k": quiz[k][h]["all"]["mean_diff_usd_100k"],
                        "median_gap_pct": quiz[k][h]["all"]["median_gap_pct"]} for h in ("2y", "5y")} for k in scored}
    even_ok = all(combined[k][h]["now_wins"] > 0.5 and combined[k][h]["mean_diff_usd_100k"] > 0 for k in scored if quiz[k]["answer"] == "even" for h in ("2y", "5y"))
    rule_split = {k: {h: ("now" if combined[k][h]["now_wins"] > 0.5 else "rule") for h in ("2y", "5y")} for k in scored if quiz[k]["answer"] == "rule"}
    (out if even_ok else warn)("QUIZ_ALL", check="두 시기 합침(2000~): even 묶음 = 미루지 않은 쪽이 횟수 > 50% · 평균 > 0 (2년·5년)", even_ok=even_ok,
                               rule_group_count_side=rule_split, **{k: f"{pctf(v['5y']['now_wins'])}/{v['5y']['mean_diff_usd_100k']}" for k, v in combined.items()})
    declines = big_declines(gd, gp)
    for e in declines:
        out("DECLINE", **{k: (pctf(v) if k.endswith("pct") else v) for k, v in e.items()})
    problems = ts.check_rules(QUESTIONS, out, log, levels=LEVELS)
    virtual = []
    for name, bands in VIRTUAL_BANDS:
        ans = "".join("ABC"[order.index(b)] for b, (*_, order) in zip(bands, QUIZ))
        t, g, _ = ts.grade(QUESTIONS, ans)
        virtual.append({"name": name, "answers": ans, "total": t, "grade": g})
        out("VIRTUAL", name=name.replace(" ", "_"), answers=ans, total=t, grade=g)
    with (HERE / "results.json").open("w", encoding="utf-8") as f:
        json.dump({"version": VERSION, "made": datetime.now(timezone.utc).isoformat(timespec="seconds"), "data_last": d[-1].isoformat(),
                   "results": results, "intro": it, "mismatches": mism, "flips_5y": flips, "scored_v1": list(expect), "rule_problems": problems,
                   "quiz": quiz, "quiz_cash5": {k: {"early_band": v["early_band"], "late_ok": v["late_ok"], "early_range_5y": v["early_range_5y"],
                                                    "early_5y": v["5y"]["early"], "late_5y": v["5y"]["late"], "late_2y": v["2y"]["late"]} for k, v in quiz5.items()},
                   "quiz_mismatches": qmis, "quiz_cash5_mismatches": qmis5, "quiz_combined": combined, "quiz_combined_even_ok": even_ok,
                   "quiz_combined_rule_side": rule_split, "declines": declines, "virtual": virtual,
                   "scored": scored, "quiz_ref": QUIZ_REF},
                  f, ensure_ascii=False, indent=1, default=str)
    out("DONE", results="calc/results.json", rule_problems=problems, quiz_mismatches=len(qmis), v1_mismatches=len(mism), seconds=f"{time.time() - t0:.1f}",
        note="연구·교육용 — 투자 권유 아님")


if __name__ == "__main__":
    main()
