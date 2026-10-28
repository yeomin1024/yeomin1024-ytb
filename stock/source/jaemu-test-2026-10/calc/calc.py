#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.3 — 2026-10-28 — 정답·오답 섞기 + 2년 뒤 (사용자 지시 "재무제표 왜 오답은 같이 안넣었어 그리고 2년뒤를 보는걸로 해"):
#          정답 3곳(그때 싸 보였고 2년 뒤 오름) + 오답 2곳(그때 싸 보였지만 2년 뒤 빠짐 — 재무제표에 경고가 보였던 곳) · 기준 연도의 앞 연도와
#          견준 추세(매출·이익률·잉여현금·주식 수)를 함께 · 결과 = 2년 뒤 종가 · 외부 영향 점검(업종 ETF·같은 업종 회사).
# (v1.2 — 2026-10-27 — 저평가 정답 5곳·3년 뒤. v1.1 — 실제 회사 10곳. v1.0 — 최초.)
#
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.3 | 2026-10-28 | 정답 3 · 오답 2 · 2년 · 앞 연도 추세 · 정답 쪽과 결과가 같은지 검사 · 폭스·윌리엄스소노마·태피스트리·스프라우츠 뺌 | main · case_report |
# | v1.2 | 2026-10-27 | 저평가 5곳 · 3년 · 분해·외부 영향 | main · case_report |
# | v1.1 | 2026-10-27 | 실제 미국 회사 10곳 | main |
# | v1.0 | 2026-10-27 | 최초 | main |
#
# 실행: python3 -B stock/source/jaemu-test-2026-10/calc/calc.py
# 입력: 같은 폴더 us_value_fundamentals.csv · us_value_prices.csv (Yahoo, 2026-10-28 받음). 네트워크 없음.
# 미리 보기 점검: t0 = 기준 연도 끝 + 122일 뒤 첫 종가 — 상황(문항)은 기준 연도·앞 연도 숫자와 t0 까지의 주가만. 2년 뒤 연도는 t2 보다 90일 앞에 끝난 것.
# ※ 연구·교육용 — 투자 권유가 아님.
import csv
import logging
import math
import sys
from datetime import date, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / "tools"))
import test_score as ts  # noqa: E402

VERSION = "v1.3"
B = 1e9
LEVELS = (0, 10, 20)

# side = 정답(싸 보였고 올랐음 → 20점 = 숫자로 확인하고 매수 검토) · 오답(싸 보였지만 빠짐 → 20점 = 경고를 읽고 매수하지 않음)
CASES = {
    1: dict(ticker="RL", name="랄프로렌", side="정답", fy0="2024-03-31", fyp="2023-03-31", fy2="2026-03-31", etf="XRT", peer=None),
    2: dict(ticker="KSS", name="콜스", side="오답", fy0="2024-01-31", fyp="2023-01-31", fy2="2026-01-31", etf="XRT", peer="M"),
    3: dict(ticker="EXPE", name="익스피디아", side="정답", fy0="2023-12-31", fyp="2022-12-31", fy2="2025-12-31", etf="XLY", peer="BKNG"),
    4: dict(ticker="BBWI", name="배스앤바디웍스", side="오답", fy0="2024-01-31", fyp="2023-01-31", fy2="2026-01-31", etf="XRT", peer="ULTA"),
    5: dict(ticker="URBN", name="어반아웃피터스", side="정답", fy0="2024-01-31", fyp="2023-01-31", fy2="2026-01-31", etf="XRT", peer=None),
}
QUESTIONS = [  # 20점 자리 섞음 — 대본 단계에서 보기 글을 이 순서로 (요약본 [항목])
    (1, "랄프로렌 — 정답", False, {"A": 0, "B": 20, "C": 10}),
    (2, "콜스 — 오답", False, {"A": 10, "B": 0, "C": 20}),
    (3, "익스피디아 — 정답", False, {"A": 20, "B": 0, "C": 10}),
    (4, "배스앤바디웍스 — 오답", False, {"A": 0, "B": 10, "C": 20}),
    (5, "어반아웃피터스 — 정답", False, {"A": 20, "B": 10, "C": 0}),
]
VIRTUAL = [
    ("V1 숫자를 읽는 사람", [20, 20, 20, 20, 20]),
    ("V2 PER 만 보고 다 사는 사람", [20, 0, 20, 0, 20]),      # 싸 보이면 늘 매수 → 정답 셋만 맞음
    ("V3 걱정되면 다 피하는 사람", [0, 20, 0, 20, 0]),
    ("V4 숫자 없이 조금씩", [10, 10, 10, 10, 10]),
]


class StageFormatter(logging.Formatter):
    def format(self, record):
        return f"[{getattr(record, 'stage', 'CALC')}] [{self.formatTime(record, '%Y-%m-%dT%H:%M:%S')}] {record.getMessage()}"


log = logging.getLogger("jaemu-test-calc")


def out(stage, **kv):
    log.info(" ".join(f"{k}={v}" for k, v in kv.items()), extra={"stage": stage})


def rows_of(path):
    try:
        with open(path, encoding="utf-8") as f:
            return list(csv.DictReader(line for line in f if not line.startswith("#")))
    except OSError as e:
        log.error(f"file={path} error={e} next_step=Yahoo 에서 다시 받기", extra={"stage": "LOAD"})
        raise


def load_fund(path):
    f = {}
    for r in rows_of(path):
        f.setdefault((r["ticker"], r["fy_end"][:7]), {})[r["field"]] = float(r["value"])
    out("LOAD", file=path.name, years=len(f))
    return f


def load_prices(path):
    p = {(r["ticker"], r["of"]): (r["t0_date"], float(r["t0_close"]), r["t2_date"], float(r["t2_close"]),
                                  float(r["ago_close"]) if r["ago_close"] else None) for r in rows_of(path)}
    bad = [k for k, v in p.items() if v[1] <= 0 or v[3] <= 0 or v[2] <= v[0]]
    out("LOAD", file=path.name, rows=len(p), problems=bad or "-")
    return p


def pct(a, b):
    return (a / b - 1) * 100


def case_report(q, c, F, P):
    """그때(기준 연도 + 앞 연도 추세) · 2년 뒤 · 분해 · 비교. (미리 보기 문제 수, 정답 쪽과 결과가 어긋나는가)"""
    t = c["ticker"]
    a, p, b = F[(t, c["fy0"][:7])], F[(t, c["fyp"][:7])], F[(t, c["fy2"][:7])]
    t0d, t0, t2d, t2, ago = P[(t, t)]
    look = int(date.fromisoformat(c["fy0"]) + timedelta(days=118) > date.fromisoformat(t0d)) + \
        int(date.fromisoformat(c["fy2"]) + timedelta(days=90) > date.fromisoformat(t2d))
    mc = t0 * a["OrdinarySharesNumber"]
    opm = lambda x: x["OperatingIncome"] / x["TotalRevenue"] * 100  # noqa: E731
    then = dict(price=f"{t0:.2f}", per=f"{t0 / a['DilutedEPS']:.1f}", fcf_yield_pct=f"{a['FreeCashFlow'] / mc * 100:.1f}",
                revenue_change_pct=f"{pct(a['TotalRevenue'], p['TotalRevenue']):.0f}", op_margin=f"{opm(p):.1f}→{opm(a):.1f}",
                fcf_bn=f"{p['FreeCashFlow'] / B:.2f}→{a['FreeCashFlow'] / B:.2f}",
                shares_change_pct=f"{pct(a['OrdinarySharesNumber'], p['OrdinarySharesNumber']):.1f}",
                debt_to_op_income=f"{a['TotalDebt'] / a['OperatingIncome']:.1f}",
                interest_cover=f"{a['OperatingIncome'] / a['InterestExpense']:.1f}", change_1y_pct=f"{pct(t0, ago):.0f}")
    if a.get("Inventory") and p.get("Inventory"):
        then["inventory_change_pct"] = f"{pct(a['Inventory'], p['Inventory']):.0f}"
    if a.get("CashDividendsPaid"):
        then["dividend_of_net_income_pct"] = f"{-a['CashDividendsPaid'] / a['NetIncome'] * 100:.0f}"
    if a["StockholdersEquity"] < 0:
        then["equity_bn"] = f"{a['StockholdersEquity'] / B:.2f}"
    out(f"Q{q}", name=c["name"], side=c["side"], t0=t0d, **then)
    px, epsx = t2 / t0, b["DilutedEPS"] / a["DilutedEPS"]
    rev = dict(t2=t2d, price_x=f"{px:.2f}", eps_x=f"{epsx:.2f}", per=f"{t0 / a['DilutedEPS']:.1f}→{t2 / b['DilutedEPS']:.1f}",
               op_margin_2y=f"{opm(a):.1f}→{opm(b):.1f}", revenue_x=f"{b['TotalRevenue'] / a['TotalRevenue']:.2f}",
               shares_x=f"{b['OrdinarySharesNumber'] / a['OrdinarySharesNumber']:.2f}",
               eps_share_of_move_pct=f"{math.log(epsx) / math.log(px) * 100:.0f}")
    if a.get("CashDividendsPaid") and b.get("CashDividendsPaid"):
        rev["dividend_paid_change_pct"] = f"{pct(b['CashDividendsPaid'], a['CashDividendsPaid']):.0f}"
    out("REVEAL", q=q, name=c["name"], **rev)
    cmp = {f"{k}_x": f"{P[(c[k2], t)][3] / P[(c[k2], t)][1]:.2f}" for k, k2 in (("etf", "etf"), ("peer", "peer")) if c.get(k2)}
    spx = P[("^GSPC", t)][3] / P[("^GSPC", t)][1]
    etfx = P[(c["etf"], t)][3] / P[(c["etf"], t)][1]
    out("EXTERNAL", q=q, spx_x=f"{spx:.2f}", **cmp, vs_etf=f"{px / etfx:.2f}", note="업종 ETF 대비 — 1 에서 멀수록 회사 자체 까닭")
    mismatch = (c["side"] == "정답" and px <= spx) or (c["side"] == "오답" and px >= 1)
    if mismatch:
        log.warning(f"q={q} side={c['side']} price_x={px:.2f} spx_x={spx:.2f} problem=정답·오답 표시와 결과가 어긋남", extra={"stage": "CHECK"})
    return look, mismatch


def main():
    h = logging.StreamHandler(sys.stdout)
    h.setFormatter(StageFormatter())
    log.addHandler(h)
    log.setLevel(logging.INFO)
    out("LOAD", version=VERSION, test_score=ts.VERSION, cases=len(CASES), horizon="2년")
    F = load_fund(HERE / "us_value_fundamentals.csv")
    P = load_prices(HERE / "us_value_prices.csv")
    mu = P[("MU", "MU")]
    out("INTRO", ticker="MU", peak=f"{mu[0]}:{mu[1]:.2f}", last=f"{mu[2]}:{mu[3]:.2f}", from_peak_pct=f"{pct(mu[3], mu[1]):.1f}")
    res = [case_report(q, c, F, P) for q, c in CASES.items()]
    out("LOOKAHEAD", checked=len(CASES), problems=sum(r[0] for r in res), mismatches=sum(r[1] for r in res))
    out("MIX", right_side=[q for q, c in CASES.items() if c["side"] == "정답"], trap_side=[q for q, c in CASES.items() if c["side"] == "오답"])
    problems = ts.check_rules(QUESTIONS, out, log, levels=LEVELS)
    ts.run_virtual(QUESTIONS, VIRTUAL, out)
    out("DONE", rule_problems=problems, note="연구·교육용 — 투자 권유 아님")


if __name__ == "__main__":
    main()
