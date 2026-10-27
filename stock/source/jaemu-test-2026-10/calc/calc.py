#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-10-27 — 가상 회사 → 실제 미국 회사 10곳 (사용자 지시 "왜 가상의 종목을 해? 미국 주식 과거 데이터 다 나와 있잖아
#          거기서 해당 시점의 제무재표에서 찾으면 되잖아 정답과 오답을 섞고 그리고 앞으로 미국주식 기준이야 그리고 종목은 되도록 다 알만한거로 해").
#          도입도 미국(마이크론). 회사마다 '실적 발표 뒤 첫 종가(t0) 때 공개된 재무제표'만 쓰고, 1년 뒤 종가(t1)로 결과를 공개.
# (v1.0 — 2026-10-27 — 최초: 도입 SK하이닉스 · 항목 가상 회사.)
#
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.1 | 2026-10-27 | SRC·QUESTIONS 를 실제 미국 회사로 · 가격 csv us_cases_prices.csv · 미리 보기 점검(재무제표 날짜 < t0) · 결과 표 | main · load_prices · CASES |
# | v1.0 | 2026-10-27 | 최초 | main · load_prices · sentence_report |
#
# 실행: python3 stock/source/jaemu-test-2026-10/calc/calc.py            (INFO)
#       python3 stock/source/jaemu-test-2026-10/calc/calc.py --debug    (DEBUG — 문장마다 글자 수)
# 입력: 아래 CASES·INTRO_SRC (값마다 출처) + 같은 폴더 us_cases_prices.csv (Yahoo 종가, 2026-10-27 받음). 네트워크 없음.
# 미리 보기 편향 점검: 회사마다 재무제표 기간 끝(fy_end)·발표일(release) < t0 인지 검사 — t0 에 몰랐던 숫자는 상황 문장에 쓰지 않는다.
# 고른 방법 (치우침을 숨기지 않음): 재무제표가 그 뒤 결과를 잘 설명한 사례를 골랐다 → 대본 정리에서 그렇다고 말함 (요약본 [근거] 3번).
# ※ 연구·교육용 — 투자 권유가 아님.
import csv
import logging
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / "tools"))
import test_score as ts  # noqa: E402

VERSION = "v1.1"
B = 1e9  # 달러 → 10억 달러

# ---------------------------------------------------------------- 입력 — 도입 (미국)
INTRO_SRC = {
    "ticker": "MU",
    "record_quarter": "FY2026 3분기 (6월 발표) 매출 414.6억 달러 — 사상 최대 (Micron 보도 요약, 요약본 [근거] 2번)",
    "release": "2026-06-24",          # 장 마감 뒤 발표로 보임 (6/25 종가 +15.7%) — 고점 = 6/25 종가 (csv)
}

# ---------------------------------------------------------------- 입력 — 항목 10 (실제 회사)
# fy_end = 재무제표 기간 끝 · release = 실적 발표일 · t0 = 발표 뒤 첫 종가일 (csv) · 숫자 단위 달러
# 출처: Yahoo Finance fundamentals-timeseries (annual*, 2026-10-27 받음) = 'YF' · 회사 발표·보도 = 요약본 [근거] 2번
CASES = {
    1: dict(ticker="PFE", name="화이자", fy_end="2022-12-31", release="2023-01-31",
            revenue=100.3 * B,              # 회사 발표 '사상 최대' (YF annualTotalRevenue 101.17 — 다른 수입 포함)
            covid_2022=(37.5 + 19.0) * B,   # Comirnaty·Paxlovid 2022 — 회사 2023 전망(-64%·-58%)에서 거꾸로 셈 (보도)
            covid_2023_guide=(13.5 + 8.0) * B,  # 같은 날(1/31) 회사가 낸 2023 전망
            eps=5.47,                       # YF annualDilutedEPS
            revenue_next=59.554 * B),       # YF 2023 매출 — [REF] t0 에는 몰랐던 값 (해설 공개용)
    2: dict(ticker="META", name="메타", fy_end="2022-12-31", release="2023-02-01",
            net_income=23.20 * B, net_income_prev=39.37 * B,   # 10-K (−41% 보도) · 2021 은 회사 발표 값
            rl_loss=13.717 * B,                                 # Reality Labs 영업손실 (10-K)
            ocf=50.48 * B, eps=8.59),                           # YF
    3: dict(ticker="NVDA", name="엔비디아", fy_end="2023-01-29", release="2023-02-22",
            net_income=4.37 * B, ni_change_pct=-55,             # 회사 발표 (−55%)
            eps=0.174,                                          # YF (2024 10:1 분할 반영 — csv 종가와 같은 기준)
            dc_revenue=15.01 * B, dc_growth_pct=41, gaming_revenue=9.07 * B,  # 10-K
            eps_next=1.19),                                     # YF FY2024 — [REF] t0 에는 몰랐던 값
    4: dict(ticker="AMZN", name="아마존", fy_end="2022-12-31", release="2023-02-02",
            net_income=-2.72 * B, op_income=12.25 * B, ocf=46.75 * B,  # YF
            rivian_loss=12.7 * B, last_loss_year=2014),         # 보도 (리비안 평가 손실 · 2014 뒤 첫 연간 적자)
    5: dict(ticker="INTC", name="인텔", fy_end="2023-12-30", release="2024-01-25",
            net_income=1.69 * B, dividends=3.09 * B, fcf=-14.28 * B, eps=0.40,  # YF
            dividend_suspended="2024-08-01"),                   # 10-Q (t0 뒤 사건 — 해설 공개용)
    6: dict(ticker="AMC", name="AMC", fy_end="2021-12-31", release="2022-03-01",
            shares_2019=104e6, shares_2021=514e6,               # 보도 (2019 말 약 1억 400만 → 2021 약 5억 1,400만)
            net_income=-1.2698 * B),                            # 회사 발표 (8-K 2022-03-01)
    7: dict(ticker="MCD", name="맥도날드", fy_end="2022-12-31", release="2023-01-31",
            equity=-6.00 * B, net_income=6.18 * B, op_income=10.35 * B, interest=1.21 * B,
            buyback=3.90 * B, dividends=4.17 * B,               # YF
            net_income_next=8.469 * B),                         # YF 2023 — [REF]
    8: dict(ticker="BA", name="보잉", fy_end="2023-12-31", release="2024-01-31",
            equity=-17.23 * B, op_income=-0.82 * B, interest=2.46 * B, net_income=-2.22 * B,  # YF
            loss_years="2019~2023"),                            # 보도·연차 보고 (5년 연속 순손실)
    9: dict(ticker="SIVB", name="실리콘밸리은행", fy_end="2022-12-31", release="2023-02-24",  # 10-K 낸 날
            htm_unrealized_loss=15.158 * B, equity=16.295 * B,  # 10-K 주석 (보도·자료 인용)
            close_0308=267.83, close_0309=106.04, bank_closed="2023-03-10"),  # 소송 공고 · FDIC
    10: dict(ticker="WE", name="위워크", fy_end="2023-06-30", release="2023-08-08",  # 2분기 보고서 — '계속 기업' 의문
             after_hours_price=0.21, bankruptcy="2023-11-06"),
}

QUESTIONS = [  # (번호, 짧은 이름, 과락 문항인가, 보기 → 점수) — 요약본 [항목N] 의 보기 순서와 같아야 한다
    (1, "화이자 — 사상 최대 매출·PER 8", False, {"A": 0, "B": 10, "C": 5}),
    (2, "메타 — 순이익 -41%·현금 505억", False, {"A": 0, "B": 5, "C": 10}),
    (3, "엔비디아 — PER 136", False, {"A": 10, "B": 0, "C": 5}),
    (4, "아마존 — 8년 만의 적자·본업 흑자", False, {"A": 0, "B": 5, "C": 10}),
    (5, "인텔 — 순이익보다 많은 배당", False, {"A": 10, "B": 0, "C": 5}),
    (6, "AMC — 주식 수 5배", False, {"A": 0, "B": 10, "C": 5}),
    (7, "맥도날드 — 자본 마이너스(자사주)", False, {"A": 10, "B": 0, "C": 5}),
    (8, "보잉 — 자본 마이너스(적자)·이자", False, {"A": 0, "B": 5, "C": 10}),
    (9, "실리콘밸리은행 — 숨은 손실 ≈ 자본", True, {"A": 0, "B": 10, "C": 5}),
    (10, "위워크 — 회사 스스로 존속 의문", True, {"A": 10, "B": 5, "C": 0}),
]
BUY_IS_RIGHT = {2, 3, 4, 7}   # 10점 답이 '매수 검토·위험 크지 않음' 쪽인 항목 (나머지는 '매수하지 않음' 쪽) — 정답·오답 섞임 점검용

VIRTUAL = [  # 문제 1~10 의 점수 줄 (실제 사람 아님)
    ("V1 까닭을 읽는 사람", [10, 10, 10, 10, 10, 5, 10, 10, 10, 10]),
    ("V2 늘 피하는 사람", [10, 0, 0, 0, 10, 10, 0, 10, 10, 10]),
    ("V3 늘 매수하는 사람", [0, 5, 5, 5, 0, 0, 5, 0, 5, 5]),
    ("V4 다 맞혔지만 위워크에 몰빵", [10, 10, 10, 10, 10, 10, 10, 10, 10, 0]),
    ("V5 딱 70점", [10, 10, 10, 10, 5, 5, 5, 5, 5, 5]),
]

INTRO = [
    "최근 사상 최대 실적을 낸 회사도 주가가 크게 빠져, 손실 본 투자자가 많습니다.",
    "미국 마이크론은 6월 사상 최대 매출을 발표했지만, 넉 달 만에 주가가 25% 빠졌습니다.",
    "이렇게 손해 보는 투자자들에겐, 공통된 판단 습관이 있습니다.",
    "그것을 바탕으로, 실제 미국 회사들의 재무제표로 테스트를 만들었습니다.",
    "회사 이름은 해설에서 공개합니다.",
    "항목마다 본인의 답을 고르고, 그 점수를 모두 더해 주세요.",
    "그럼 시작하겠습니다.",
]
SHORTS = [
    "재무제표를 보고도, 손해 볼 사람일까?",
    "실제 미국 회사들의 재무제표로 만든 테스트입니다.",
    "항목마다 본인의 답을 골라 보세요.",
    "매출이 사상 최대인데 PER 이 8인 회사, 매수하시나요?",
    "순이익이 41% 줄어든 회사, 어떻게 보시나요?",
    "PER 이 136인 회사, 비싸다고 보시나요?",
    "8년 만에 한 해 적자를 낸 회사, 어떻게 보시나요?",
    "번 돈보다 배당을 더 준 회사, 매수하시나요?",
    "2년 만에 주식 수가 5배가 된 회사, 어떻게 보시나요?",
    "자본이 마이너스인 회사, 곧 망할 거라 보시나요?",
    "이자를 영업으로 벌지 못한 큰 회사, 매수하시나요?",
    "숨은 채권 손실이 자본만큼 큰 은행, 매수하시나요?",
    "스스로 존속을 의심한 회사에, 남은 돈을 넣으시나요?",
    "선택한 답과 실제 회사의 결과는 아래 영상에서 확인하세요.",
]
LONG_RATE = 5.67     # 롱폼 실측 음절/초, 문장 사이 쉼 포함 (첫 편 요약본 v1.9)
SHORT_RATE = 6.33    # 쇼츠 실측 음절/초 (첫 편 shorts.md 1번)
SHORT_GAP = 0.46     # 쇼츠 문장 사이 쉼(초)
SHORT_END = 2.5      # 쇼츠 끝 화면(초)
MAX_CHARS = 50       # 한 문장 = 자막 하나, 50자 이하 (quick_test.md 7번)


# ---------------------------------------------------------------- 로그
class StageFormatter(logging.Formatter):
    def format(self, record):
        stage = getattr(record, "stage", "CALC")
        return f"[{stage}] [{self.formatTime(record, '%Y-%m-%dT%H:%M:%S')}] {record.getMessage()}"


log = logging.getLogger("jaemu-test-calc")


def out(stage, **kv):
    log.info(" ".join(f"{k}={v}" for k, v in kv.items()), extra={"stage": stage})


def pct(a, b):
    return (a / b - 1) * 100


def bn(x):
    return f"{x / B:.2f}"


def load_prices(path):
    """us_cases_prices.csv → {ticker: (t0_date, t0_close, t1_date, t1_close)}. 0 이하·겹친 종목·날짜 순서를 점검한다."""
    try:
        with open(path, encoding="utf-8") as f:
            rows = list(csv.DictReader(line for line in f if not line.startswith("#")))
    except OSError as e:
        log.error(f"file={path} error={e} next_step=Yahoo chart API 에서 다시 받기 (요약본 [근거] 1번)", extra={"stage": "LOAD"})
        raise
    prices, problems = {}, []
    for r in rows:
        t = r["ticker"]
        v = (r["t0_date"], float(r["t0_close"]), r["t1_date"], float(r["t1_close"]))
        if t in prices:
            problems.append(f"겹친 종목 {t}")
        if v[1] <= 0 or v[3] <= 0:
            problems.append(f"0 이하 {t}")
        if v[2] <= v[0]:
            problems.append(f"t1 <= t0 {t}")
        prices[t] = v
    out("LOAD", file=path.name, tickers=len(prices), problems=problems or "-")
    if problems:
        log.warning(f"problems={problems} next_step=csv 를 출처와 다시 대조", extra={"stage": "CHECK"})
    return prices


def syllables(text):
    """읽는 음절 대충 세기 — 한글 글자 + 숫자·영문 글자 하나씩 (PER·AMC 처럼 읽는 소리가 긴 말은 조금 짧게 잡힘)."""
    return len(re.findall(r"[가-힣0-9A-Za-z]", text))


def sentence_report(name, sentences, rate, gap=0.0, end=0.0):
    over = [i + 1 for i, s in enumerate(sentences) if len(s) > MAX_CHARS]
    syl = sum(syllables(s) for s in sentences)
    sec = syl / rate + gap * (len(sentences) - 1) + end
    for i, s in enumerate(sentences, 1):
        log.debug(f"{name}#{i} chars={len(s)} syllables={syllables(s)} text={s}", extra={"stage": "TEXT"})
    out("TEXT", part=name, sentences=len(sentences), syllables=syl, est_sec=f"{sec:.1f}", over_50_chars=over or "-")
    if over:
        log.warning(f"part={name} over={over} next_step=쉼표·절 경계에서 둘로", extra={"stage": "TEXT"})
    return sec


def main():
    h = logging.StreamHandler(sys.stdout)
    h.setFormatter(StageFormatter())
    log.addHandler(h)
    log.setLevel(logging.DEBUG if "--debug" in sys.argv else logging.INFO)
    out("LOAD", version=VERSION, test_score=ts.VERSION, cases=len(CASES), source="CASES dict + us_cases_prices.csv")
    p = load_prices(HERE / "us_cases_prices.csv")

    # ------------------------------------------------------------ 도입 — 마이크론 (csv: t0 = 2026 종가 최고, t1 = 마지막 종가)
    mu = p["MU"]
    out("INTRO", peak=f"{mu[0]}:{mu[1]:,.2f}", last=f"{mu[2]}:{mu[3]:,.2f}", from_peak_pct=f"{pct(mu[3], mu[1]):.1f}",
        record=INTRO_SRC["record_quarter"], say="6월 사상 최대 매출 → 넉 달 만에 주가 25% ↓")

    # ------------------------------------------------------------ 미리 보기 점검 — 재무제표·발표일이 t0 보다 앞인가
    look = []
    for q, c in CASES.items():
        t0 = p[c["ticker"]][0] if c["ticker"] in p else c["release"]
        if not (c["fy_end"] < c["release"] <= t0):
            look.append(q)
    out("LOOKAHEAD", checked=len(CASES), problems=look or "-", rule="fy_end < release <= t0 · *_next·사건 날짜는 해설 공개에만")
    if look:
        log.warning(f"questions={look} next_step=t0 를 발표 뒤로 옮김", extra={"stage": "LOOKAHEAD"})

    # ------------------------------------------------------------ 항목별 숫자 (상황 문장 = t0 에 공개된 값만)
    c = CASES[1]
    t = p[c["ticker"]]
    out("Q1", revenue_bn=bn(c["revenue"]), covid_share_pct=f"{c['covid_2022'] / c['revenue'] * 100:.0f}",
        per=f"{t[1] / c['eps']:.1f}", covid_guide_change_pct=f"{pct(c['covid_2023_guide'], c['covid_2022']):.0f}",
        say="매출 1,000억 달러 처음 · 절반 넘게 코로나 · PER 8 · 그날 전망 코로나 매출 60% 넘게 ↓")
    out("REVEAL", q=1, name=c["name"], t0=f"{t[0]}:{t[1]}", t1=f"{t[2]}:{t[3]}", change_pct=f"{pct(t[3], t[1]):.1f}",
        revenue_next_change_pct=f"{pct(c['revenue_next'], c['revenue']):.0f}")
    c = CASES[2]
    t = p[c["ticker"]]
    out("Q2", ni_change_pct=f"{pct(c['net_income'], c['net_income_prev']):.0f}", rl_loss_bn=bn(c["rl_loss"]), ocf_bn=bn(c["ocf"]),
        per=f"{t[1] / c['eps']:.1f}", say="순이익 41% ↓ · 메타버스 137억 달러 손실 · 본업 현금 505억 달러")
    out("REVEAL", q=2, name=c["name"], t0=f"{t[0]}:{t[1]}", t1=f"{t[2]}:{t[3]}", multiple=f"{t[3] / t[1]:.2f}")
    c = CASES[3]
    t = p[c["ticker"]]
    out("Q3", ni_change_pct=c["ni_change_pct"], per=f"{t[1] / c['eps']:.0f}", dc_bn=bn(c["dc_revenue"]), dc_growth_pct=c["dc_growth_pct"],
        dc_is_largest=c["dc_revenue"] > c["gaming_revenue"], say="순이익 55% ↓ · PER 136 · 데이터센터 41% ↑ 가장 큰 사업")
    out("REVEAL", q=3, name=c["name"], t0=f"{t[0]}:{t[1]}", t1=f"{t[2]}:{t[3]}", multiple=f"{t[3] / t[1]:.2f}",
        per_on_next_eps=f"{t[1] / c['eps_next']:.0f}", eps_next_multiple=f"{c['eps_next'] / c['eps']:.1f}", note="[REF] 다음 해 이익 6.8배")
    c = CASES[4]
    t = p[c["ticker"]]
    out("Q4", years_since_loss=2022 - c["last_loss_year"], net_income_bn=bn(c["net_income"]), op_income_bn=bn(c["op_income"]),
        ocf_bn=bn(c["ocf"]), say="8년 만에 적자 · 순손실 27억 · 영업이익 122억 흑자")
    out("REVEAL", q=4, name=c["name"], rivian_loss_bn=bn(c["rivian_loss"]), t0=f"{t[0]}:{t[1]}", t1=f"{t[2]}:{t[3]}",
        change_pct=f"{pct(t[3], t[1]):.1f}")
    c = CASES[5]
    t = p[c["ticker"]]
    out("Q5", dividends_bn=bn(c["dividends"]), net_income_bn=bn(c["net_income"]), payout_ratio=f"{c['dividends'] / c['net_income']:.2f}",
        fcf_bn=bn(c["fcf"]), per=f"{t[1] / c['eps']:.0f}", say="배당 31억 · 순이익 17억 · 쓴 현금이 143억 많음")
    out("REVEAL", q=5, name=c["name"], dividend_suspended=c["dividend_suspended"], t0=f"{t[0]}:{t[1]}", t1=f"{t[2]}:{t[3]}",
        change_pct=f"{pct(t[3], t[1]):.1f}")
    c = CASES[6]
    t = p[c["ticker"]]
    out("Q6", shares_multiple=f"{c['shares_2021'] / c['shares_2019']:.1f}", net_income_bn=bn(c["net_income"]), say="2년 사이 주식 수 5배 · 순손실 12억 넘음")
    out("REVEAL", q=6, name=c["name"], t0=f"{t[0]}:{t[1]}", t1=f"{t[2]}:{t[3]}", change_pct=f"{pct(t[3], t[1]):.1f}",
        note="Yahoo 종가는 2023 1:10 병합만 반영 · 2022-08 APE 배당 가치 빼고 셈 — 대본은 '절반 넘게'만")
    c = CASES[7]
    t = p[c["ticker"]]
    out("Q7", equity_bn=bn(c["equity"]), net_income_bn=bn(c["net_income"]), interest_cover=f"{c['op_income'] / c['interest']:.1f}",
        buyback_plus_div_bn=bn(c["buyback"] + c["dividends"]), say="자본 60억 마이너스 · 순이익 62억 · 영업이익이 이자의 8배 넘음")
    out("REVEAL", q=7, name=c["name"], ni_next_bn=bn(c["net_income_next"]), t0=f"{t[0]}:{t[1]}", t1=f"{t[2]}:{t[3]}",
        change_pct=f"{pct(t[3], t[1]):.1f}")
    c = CASES[8]
    t = p[c["ticker"]]
    out("Q8", equity_bn=bn(c["equity"]), op_income_bn=bn(c["op_income"]), interest_bn=bn(c["interest"]), loss_years=c["loss_years"],
        say="자본 172억 마이너스 · 몇 년째 적자 · 이자 25억을 영업으로 못 벎")
    out("REVEAL", q=8, name=c["name"], t0=f"{t[0]}:{t[1]}", t1=f"{t[2]}:{t[3]}", change_pct=f"{pct(t[3], t[1]):.1f}")
    c = CASES[9]
    out("Q9", htm_loss_bn=bn(c["htm_unrealized_loss"]), equity_bn=bn(c["equity"]),
        loss_to_equity_pct=f"{c['htm_unrealized_loss'] / c['equity'] * 100:.0f}", say="숨은 손실 152억 · 자본 163억")
    out("REVEAL", q=9, name=c["name"], day_0309_pct=f"{pct(c['close_0309'], c['close_0308']):.1f}", bank_closed=c["bank_closed"],
        days_after_10k=14, say="2주 뒤 문을 닫음")
    c = CASES[10]
    out("Q10", after_hours_price=c["after_hours_price"], say="주가 1달러도 안 됨")
    out("REVEAL", q=10, name=c["name"], bankruptcy=c["bankruptcy"], say="3개월 뒤 파산 신청")

    # ------------------------------------------------------------ 점수 규칙 (공용) + 정답·오답 섞임
    problems = ts.check_rules(QUESTIONS, out, log)
    out("MIX", buy_side_right=sorted(BUY_IS_RIGHT), avoid_side_right=sorted(set(CASES) - BUY_IS_RIGHT),
        note="10점 답이 '매수 쪽' 4 · '피하는 쪽' 6 — 늘 피하거나 늘 사면 통과 못 함 (VIRTUAL V2·V3)")
    ts.run_virtual(QUESTIONS, VIRTUAL, out)

    # ------------------------------------------------------------ 문장 길이
    intro_sec = sentence_report("intro", INTRO, LONG_RATE)
    if intro_sec > 30:
        log.warning(f"intro_sec={intro_sec:.1f} next_step=도입을 30초 안으로 줄임", extra={"stage": "TEXT"})
    sentence_report("shorts", SHORTS, SHORT_RATE, SHORT_GAP, SHORT_END)
    out("SCRIPT", rule=f"{ts.PASS_MIN}점 이상 통과 · {ts.CAUTION_MIN}~{ts.PASS_MIN - 5} 주의 · {ts.CAUTION_MIN - 5} 이하 불통과 · 9·10번 0점 과락",
        rule_problems=problems, lookahead_problems=len(look))
    out("DONE", note="연구·교육용 — 투자 권유 아님")


if __name__ == "__main__":
    main()
