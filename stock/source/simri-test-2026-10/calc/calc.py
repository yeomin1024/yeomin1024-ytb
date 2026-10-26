#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.2 — 2026-10-26 — 대본 v1.1 (사용자 지시 "미국주식지수랑 한국주식지수랑 서로 다른데 항목보면 오해할 수도 있잖아 그리고 한국
#          시청자가 반론할 수 있잖아 그럴일 없게 수정해봐 다른 나라 시청자도 포함해서"): 해설마다 한국·미국(·인도) 자료를 함께 —
#          [REF] 로 뺐던 한국 숫자 4개(리딩방·종목 82% 하락·빚 34조·2배 ETF 40대)를 다시 쓰고, 인도 SEBI 단타 71%·한국 지수 7월 말 반등 +17.9% 를 더함.
# (v1.1 — 2026-10-26 — 요약본 v1.1·대본 v1.0 (사용자 피드백 8ceb90be: 도입 = 2026년 ○월부터의 주식 시장, 해설 사례는
#          되도록 미국 주식)에 맞춤 — 고점 대비 하락·미국 투자 사기(FTC)·S&P 500 지수보다 오른 종목 비율·미국 증권사 빚(FINRA)·
#          미국 강제 매도 기준 25% → 33%·빚 두 배일 때 주가 20% 하락의 손실·모닝스타 10년 % 차이를 더함. 대본에서 뺀 한국 숫자는 REF 로.)
# (v1.0 — 2026-10-26 — 최초. 「주식 투자 실패한 사람들은 절대 통과 못하는 심리 테스트」 요약본(요약본.txt v1.0)의
#          숫자를 모두 이 코드 출력으로만 쓴다 (CLAUDE.md '숫자는 계산 코드 출력만').)
#          사용자 지시 2026-10-26: "…공신력 있는 테스트가 존재하는지 알아보고 없으면 너가 가상으로 테스트 만들어서 해봐
#          통계 같은 자료 기반으로 그리고 테스트 항목 당 점수도 부여하고 기준도 만들어서".
#
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.2 | 2026-10-26 | SRC 5개 더함(인도 SEBI 71%·지수 7/27·7/30·7/31) · 한국 숫자 4개를 REF → Q2·Q4·Q9·Q10 · Q5 인도·Q8 7월 말 반등 | main (Q2·Q4·Q5·Q8·Q9·Q10) |
# | v1.1 | 2026-10-26 | 새 SRC 8개(코스피 고점·FTC·First Trust·FINRA 빚·미국 유지 증거금 25%·예시 하락 20%) · 도입·2·4·8·9번 계산 바꿈 · 대본에서 뺀 숫자는 [REF] 로그 | main (INTRO·Q2·Q4·Q8·Q9·REF) |
# | v1.0 | 2026-10-26 | 최초 — 기사·보고서 숫자(SRC) → 대본 숫자, 점수 규칙·등급, 가상 응시 6명, 전체 경우의 수 검사 | 전부 |
#
# ※ 연구·교육용이다. 투자 권유가 아니다.
# 실행: python3 stock/source/simri-test-2026-10/calc/calc.py            (INFO)
#       python3 stock/source/simri-test-2026-10/calc/calc.py --debug    (DEBUG — 점수 분포 전부)
# 입력은 아래 SRC 하나뿐이다 (값마다 출처·기준일). 네트워크·파일 입출력 없음 → 같은 입력이면 같은 출력.

import itertools
import logging
import sys
from collections import Counter

VERSION = "v1.2"

# ---------------------------------------------------------------- 입력 (출처는 요약본 [근거] 2번과 같다)
SRC = {
    # 도입 — 2026년 6월 고점 → 10월 중순 (서울신문 2026-06-18 '사상 첫 9063.84 마감' · 고점 종가는 이전 영상 calc/prices_2026.csv, 커밋 7de247ff)
    "kospi_2026_06_18": 9063.84,      # 사상 처음 9,000 넘은 날 종가
    "kospi_2026_06_22": 9114.55,      # 2026년 종가 가운데 가장 높은 날 (이전 영상 가격 파일 6/1~9/30 중 최대)
    # 도입(REF) — 2026년 10월 하락 (뉴데일리 2026-10-15 · SBS Biz 2026-10-16 '7거래일 하락 후 겨우 상승 반전', 한국거래소·금융투자협회)
    "kospi_2026_10_02": 7003.74,      # 10월 2일 종가 (하락 시작 전)
    "kospi_2026_10_15": 5554.22,      # 10월 15일 종가 (7거래일 연속 하락 끝, 이날 -7.57%)
    "kospi_2026_10_15_day": -7.57,    # 10월 15일 하루 등락률 %
    "forced_sale_oct6_15_eok": 2981,  # 10월 6~15일 위탁매매 미수금 대비 실제 반대매매 합계 (억 원, 금융투자협회)
    "margin_loan_oct12_eok": 342886,  # 10월 12일 신용거래융자 잔고 (억 원 — 34조 2,886억, kbc 2026-10-14 '석 달 만에 최대')
    # 도입 — NH투자증권 고객 240만 명 (2025-10-30 기준, 연합뉴스 의뢰 — 세계일보·헤럴드경제 2025-11-10)
    "nh_holders": 2401502,
    "nh_losers": 1312296,
    "nh_loss_40s_pct": 59.7,
    "nh_loss_50s_pct": 60.1,
    # 1번 — Barber·Huang·Odean·Schwarz, Journal of Finance 77(6) 2022: 하루 가장 많이 산 종목의 20거래일 비정상수익률
    "robinhood_top_buy_20d_pct": -4.7,
    # 2번 — 미국 연방거래위원회(FTC) 의회 증언 2026-03-25: 2025년 신고된 사기 피해 (10억 달러)
    "ftc_2025_invest_bn": 7.9,
    "ftc_2025_total_bn": 15.9,
    # 2번 — 금융감독원 2025-08 (2024년 불법 리딩방 피해액 vs 보이스피싱 피해액, 억 원)
    "leading_room_2024_eok": 7104,
    "voice_phishing_2024_eok": 8545,
    # 2·3번 — FINRA Foundation 연구 요약 2026-04 (2024 NFCS 투자자 조사)
    "finra_fraud_loss_social_pct": 68,   # 사기 시도를 받은 SNS 이용 투자자 중 실제로 돈을 잃은 비율
    "finra_fraud_loss_nonsocial_pct": 29,
    "finra_quiz_correct_pct": 42,        # SNS 이용·핀플루언서 팔로어의 투자 지식 문제 평균 정답률
    "finra_self_rated_high_pct": 63,     # 같은 사람들 중 '내 투자 지식은 높다'고 답한 비율
    # 4번 — First Trust 'The S&P 500 Index 2025 Recap' 2026-01-08: 2025년 지수보다 더 오른 종목 비율
    "ft_2025_outperform_pct": 30.5,
    # 4번 — 뉴시스 2026-05-28 (한국거래소, 최근 한 달 코스피·코스닥 종목 등락)
    "stocks_total": 2764,
    "stocks_down": 2276,
    "kospi_2026_04_28": 6641.02,      # 이전 영상 calc/prices_2026.csv (커밋 7de247ff) 종가
    "kospi_2026_05_28": 8185.29,      # 같은 파일 · 뉴시스 기사의 5월 28일 마감 값과 같음
    # 5번 — 자본시장연구원 '코로나19 국면의 개인투자자' (2020-02 ~ 2021-01, 뉴데일리 2021-02-26) · 2022-03 포커스(김준석)
    "kcmi_trade_profit_jo": 13.0,
    "kcmi_trade_cost_jo": 13.7,       # 거래세 약 9.8조 + 수수료 약 3.9조
    "kcmi_mts_turnover_x": 1.7,       # (대본에서 뺌) 모바일(MTS) 투자자 일간 회전율 = 컴퓨터(HTS)의 약 1.7배
    # 5번 — 인도 증권거래위원회(SEBI) 2024-07-24 '주식 현물 하루 안 매매 개인 손익 분석' (2022-04 ~ 2023-03, 상위 10개 증권사 고객)
    "sebi_intraday_loss_pct": 71,
    # 6번 — 자본시장연구원 개인투자자 약 20만 명 2020-03~10 거래 (이코노미스트 2021-08-29)
    "kcmi_sell_winner_next_day_pct": 41,
    "kcmi_sell_loser_next_day_pct": 22,
    # 7번 — Brown·Imai·Vieider·Camerer, Journal of Economic Literature 62(2) 2024 (607개 추정치·150편)
    "loss_aversion_lambda": 1.955,
    "loss_example_pct": [30, 50],     # 대본은 50% (7번 상황 = 매수 가격의 절반)
    # 8번 — Morningstar 'Mind the Gap' 2026 (미국 펀드·ETF, 2016~2025 10년 연평균)
    "ms_fund_total_return_pct": 9.9,
    "ms_investor_return_pct": 8.7,
    "ms_years": 10,
    "ms_example_won_eok": 1.0,        # 예시 1억 원
    # 8번 — 한국 지수 2026년 7월 말 (이전 영상 calc/prices_2026.csv — 7/31 +17.91% 는 MTN·아이뉴스24 2026-07-31 과 같음)
    "kospi_2026_07_27": 6755.75,
    "kospi_2026_07_30": 5593.56,
    "kospi_2026_07_31": 6595.45,
    # 9번 — 한국 담보유지비율 통상 140% (헤럴드경제 2026-03-04) · 미국 FINRA Rule 4210 최소 유지 증거금 25% (내 돈 ÷ 주식값)
    "maintenance_ratio_pct": 140,
    "us_maintenance_pct": 25,
    "example_drop_pct": 20,           # 예시: 주가 20% 하락
    # 9번 — FINRA 고객 신용(margin debt) 잔고 2026년 6월 (백만 달러, Advisor Perspectives 2026-06-24 · GuruFocus) · 1년 전보다 %
    "finra_margin_2026_06_mn": 1502072,
    "finra_margin_yoy_pct": 51.5,
    "own_money": 1.0,
    "borrowed": 1.0,
    # 10번 — 헤럴드경제 2026-06-17 단독 (국회 정무위 김상훈 의원실, 상위 10개 증권사 5월 말 보유액, 억 원)
    "single_2x_total_eok": 29979,
    "single_2x_40s_eok": 10193,
    "two_x_day1_pct": -10.0,          # 예시: 기초 주가 하루 -10%
    # 10번 — Morningstar 2026 보충: 2배 단일종목 ETF 하나(CONL)의 3년(2022~2024) 연평균 — 상품 vs 투자자
    "conl_fund_pct": 47.6,
    "conl_investor_pct": -38.0,       # '38% 넘게' 잃음 (정확한 값은 원문 대조 필요)
}

# ---------------------------------------------------------------- 테스트 규칙 (설계 — 통계가 아니라 이 영상이 정한 값)
# 점수: 0 = 연구에서 손실과 이어진 행동 · 5 = 그 행동을 절반만 · 10 = 연구가 권하는 반대 행동.
# 보기 글자(A·B·C)와 점수의 짝은 문제마다 섞는다 — 늘 C 가 10점이면 시청자가 세 문제쯤에서 답 자리를 알아챈다.
QUESTIONS = [  # (번호, 짧은 이름, 과락 문항인가, 보기 → 점수) — 요약본 [테스트 내용N] 의 보기 순서와 같아야 한다
    (1, "남 따라 사기 (추격 매수)", False, {"A": 0, "B": 10, "C": 5}),
    (2, "확실한 종목 단체방", False, {"A": 10, "B": 0, "C": 5}),
    (3, "첫 수익 = 내 실력", False, {"A": 10, "B": 5, "C": 0}),
    (4, "한 종목에 몰아 넣기", False, {"A": 5, "B": 0, "C": 10}),
    (5, "자주 사고팔기", False, {"A": 10, "B": 0, "C": 5}),
    (6, "오른 것부터 팔기 (처분 효과)", False, {"A": 5, "B": 10, "C": 0}),
    (7, "산 가격만 기다리기 (손실 회피)", False, {"A": 10, "B": 5, "C": 0}),
    (8, "폭락 날 모두 팔기", False, {"A": 5, "B": 10, "C": 0}),
    (9, "빌린 돈으로 두 배 사기", True, {"A": 5, "B": 10, "C": 0}),
    (10, "두 배 상품으로 한 번에 되찾기", True, {"A": 0, "B": 5, "C": 10}),
]
LEVELS = (0, 5, 10)
PASS_MIN = 70                         # 통과: 과락 없이 70점 이상
CAUTION_MIN = 40                      # 주의: 40~65점 · 불통과: 35점 이하


def letters_for(levels):
    """점수 줄(예: [10, 10, 5, …]) → 그 점수가 나오는 보기 글자 줄 (가상 응시를 글자로 보이려고)."""
    return "".join({p: a for a, p in key.items()}[lv] for (_, _, _, key), lv in zip(QUESTIONS, levels))


def grade(answers):
    """answers: 'ABC…' 10글자 → (총점, 등급, 과락 문항 목록)."""
    if len(answers) != len(QUESTIONS) or any(a not in "ABC" for a in answers):
        raise ValueError(f"답은 A/B/C 10개여야 함: {answers!r}")
    pts = [key[a] for (_, _, _, key), a in zip(QUESTIONS, answers)]
    total = sum(pts)
    fails = [q for (q, _, cut, _), p in zip(QUESTIONS, pts) if cut and p == 0]
    if fails:
        return total, "불통과(과락)", fails
    if total >= PASS_MIN:
        return total, "통과", fails
    if total >= CAUTION_MIN:
        return total, "주의", fails
    return total, "불통과", fails


# ---------------------------------------------------------------- 로그
class StageFormatter(logging.Formatter):
    def format(self, record):
        stage = getattr(record, "stage", "CALC")
        return f"[{stage}] [{self.formatTime(record, '%Y-%m-%dT%H:%M:%S')}] {record.getMessage()}"


log = logging.getLogger("simri-test-calc")


def out(stage, **kv):
    log.info(" ".join(f"{k}={v}" for k, v in kv.items()), extra={"stage": stage})


def pct(a, b):
    return (a / b - 1) * 100


def main():
    h = logging.StreamHandler(sys.stdout)
    h.setFormatter(StageFormatter())
    log.addHandler(h)
    log.setLevel(logging.DEBUG if "--debug" in sys.argv else logging.INFO)
    s = SRC
    out("LOAD", version=VERSION, inputs=len(s), source="SRC dict (요약본 [근거] 2번)")

    # 입력 점검 — 비율은 0~100, 금액·지수는 양수
    bad = [k for k, v in s.items() if isinstance(v, (int, float)) and k.endswith("_pct") and k != "maintenance_ratio_pct"
           and not -100 <= v <= 100]
    bad += [] if 100 < s["maintenance_ratio_pct"] < 300 else ["maintenance_ratio_pct"]
    bad += [k for k in ("kospi_2026_06_22", "kospi_2026_10_15", "nh_holders", "finra_margin_2026_06_mn") if s[k] <= 0]
    bad += [] if s["kospi_2026_06_22"] >= s["kospi_2026_06_18"] else ["kospi_2026_06_22 < 06_18 (고점이 아님)"]
    if bad:
        log.warning(f"input_out_of_range keys={bad} next_step=SRC 값을 출처와 다시 대조", extra={"stage": "CHECK"})
    else:
        out("CHECK", input_range="ok")

    # 도입 — 2026년 6월 고점 → 10월 15일
    from_peak = pct(s["kospi_2026_10_15"], s["kospi_2026_06_22"])
    from_9000 = pct(s["kospi_2026_10_15"], s["kospi_2026_06_18"])
    out("INTRO", peak_jun22=s["kospi_2026_06_22"], first_9000_jun18=s["kospi_2026_06_18"], oct15=s["kospi_2026_10_15"],
        from_peak_pct=f"{from_peak:.1f}", from_jun18_pct=f"{from_9000:.1f}", say="고점보다 40% 가까이 (−38.7~−39.1%)")
    drop = pct(s["kospi_2026_10_15"], s["kospi_2026_10_02"])
    out("REF", kospi_oct2=s["kospi_2026_10_02"], kospi_oct15=s["kospi_2026_10_15"], drop_pct=f"{drop:.1f}",
        note="v1.0 도입 '2주도 안 돼 20% 넘게' — 대본에서 뺌")
    nh = s["nh_losers"] / s["nh_holders"] * 100
    out("INTRO", nh_loss_pct=f"{nh:.1f}", nh_40s=s["nh_loss_40s_pct"], nh_50s=s["nh_loss_50s_pct"],
        say="54.6% · 40대·50대는 10명 중 6명 (59.7%→6.0명, 60.1%→6.0명)",
        per10_40s=f"{s['nh_loss_40s_pct'] / 10:.1f}", per10_50s=f"{s['nh_loss_50s_pct'] / 10:.1f}")

    # 1번
    out("Q1", robinhood_20d_pct=s["robinhood_top_buy_20d_pct"], say="시장보다 평균 4.7% 낮은 성적 (20거래일)")
    # 2번
    ftc_share = s["ftc_2025_invest_bn"] / s["ftc_2025_total_bn"] * 100
    out("Q2", ftc_invest_bn=s["ftc_2025_invest_bn"], ftc_total_bn=s["ftc_2025_total_bn"], invest_share_pct=f"{ftc_share:.1f}",
        say="79억 달러 · 전체 사기 피해의 절반 가까이",
        finra_fraud_loss=f"{s['finra_fraud_loss_social_pct']}% vs {s['finra_fraud_loss_nonsocial_pct']}%",
        ratio=f"{s['finra_fraud_loss_social_pct'] / s['finra_fraud_loss_nonsocial_pct']:.2f}")
    lr = s["leading_room_2024_eok"] / s["voice_phishing_2024_eok"] * 100
    out("Q2", kr_leading_room_eok=s["leading_room_2024_eok"], vs_phishing_pct=f"{lr:.1f}", say="한국 약 7,100억 원 · 보이스피싱 피해의 83%")
    # 3번
    out("Q3", quiz_correct_pct=s["finra_quiz_correct_pct"], self_rated_high_pct=s["finra_self_rated_high_pct"])
    # 4번 — 한 종목을 아무렇게나 고르면 지수보다 못할 확률 = 1 − 지수보다 오른 비율
    out("Q4", outperform_pct=s["ft_2025_outperform_pct"], underperform_pct=f"{100 - s['ft_2025_outperform_pct']:.1f}",
        per10=f"{(100 - s['ft_2025_outperform_pct']) / 10:.1f}", say="30.5%뿐 → 열 번 중 일곱 번은 지수보다 못한 종목")
    down = s["stocks_down"] / s["stocks_total"] * 100
    k_up = pct(s["kospi_2026_05_28"], s["kospi_2026_04_28"])
    out("Q4", kr_stocks_down_pct=f"{down:.2f}", kr_index_month_pct=f"{k_up:.1f}", say="한국: 한 달 지수 20% 넘게 오를 때 종목 82% 하락")
    # 5번
    gap = s["kcmi_trade_cost_jo"] - s["kcmi_trade_profit_jo"]
    out("Q5", trade_profit_jo=s["kcmi_trade_profit_jo"], trade_cost_jo=s["kcmi_trade_cost_jo"], cost_minus_profit_eok=f"{gap * 10000:,.0f}",
        mts_turnover_x=s["kcmi_mts_turnover_x"])
    out("Q5", india_intraday_loss_pct=s["sebi_intraday_loss_pct"], say="인도: 하루 안에 매수·매도한 개인의 71%가 손실")
    # 6번
    out("Q6", sell_winner_pct=s["kcmi_sell_winner_next_day_pct"], sell_loser_pct=s["kcmi_sell_loser_next_day_pct"],
        hold_loser_pct=100 - s["kcmi_sell_loser_next_day_pct"],
        winner_vs_loser_x=f"{s['kcmi_sell_winner_next_day_pct'] / s['kcmi_sell_loser_next_day_pct']:.2f}")
    # 7번 — 손실 뒤 원래 값으로 돌아오려면 필요한 상승률
    out("Q7", loss_aversion=s["loss_aversion_lambda"], say="약 2배")
    for L in s["loss_example_pct"]:
        need = (1 / (1 - L / 100) - 1) * 100
        out("Q7", loss_pct=L, need_gain_pct=f"{need:.1f}")
    # 8번 — 같은 10년을 해마다 9.9%와 8.7%로 불리면 (예시 1억 원)
    y, base = s["ms_years"], s["ms_example_won_eok"]
    fund = base * (1 + s["ms_fund_total_return_pct"] / 100) ** y
    inv = base * (1 + s["ms_investor_return_pct"] / 100) ** y
    out("Q8", gap_pp=f"{s['ms_fund_total_return_pct'] - s['ms_investor_return_pct']:.1f}",
        fund_10y_eok=f"{fund:.4f}", investor_10y_eok=f"{inv:.4f}", diff_manwon=f"{(fund - inv) * 10000:,.0f}",
        investor_vs_fund_pct=f"{pct(inv, fund):.1f}", say="10년 동안 손에 쥐는 돈이 10% 넘게 줄어듦",
        scenario_day_drop_like=s["kospi_2026_10_15_day"])
    fall3 = pct(s["kospi_2026_07_30"], s["kospi_2026_07_27"])
    jump = pct(s["kospi_2026_07_31"], s["kospi_2026_07_30"])
    out("Q8", kr_jul27_30_pct=f"{fall3:.1f}", kr_jul31_day_pct=f"{jump:.1f}", say="사흘 동안 17% 넘게 ↓ 뒤 7/31 하루 17.9% ↑")
    # 9번 — 내 돈 1 + 빌린 돈 1 → 주식 2. 담보비율 = 주식값 / 빌린 돈
    own, loan = s["own_money"], s["borrowed"]
    stock0 = own + loan
    trigger = (s["maintenance_ratio_pct"] / 100 * loan / stock0 - 1) * 100
    # 미국: 내 돈 ÷ 주식값 = (주식 2(1+r) − 빌린 돈 1) ÷ 주식 2(1+r) = 25% 가 되는 r
    m = s["us_maintenance_pct"] / 100
    us_trigger = (loan / (stock0 * (1 - m)) - 1) * 100
    out("Q9", leverage_x=f"{stock0 / own:.1f}", kr_forced_sale_at_drop_pct=f"{trigger:.1f}", us_forced_sale_at_drop_pct=f"{us_trigger:.1f}",
        say="한국 30% · 미국 33%")
    r = -s["example_drop_pct"] / 100
    eq20 = stock0 * (1 + r) - loan
    out("Q9", example_price_drop_pct=-s["example_drop_pct"], own_money_change_pct=f"{pct(eq20, own):.1f}", say="주가 20% ↓ → 내 돈 40% ↓")
    out("Q9", finra_margin_tn=f"{s['finra_margin_2026_06_mn'] / 1e6:.2f}", yoy_pct=s["finra_margin_yoy_pct"],
        say="1조 5천억 달러 · 1년 만에 절반 넘게 늘어 사상 최대")
    eq_after = stock0 * (1 + drop / 100) - loan
    out("Q9", kr_margin_loan_jo=f"{s['margin_loan_oct12_eok'] / 10000:.2f}", say="한국 10/12 34조 원 넘음")
    out("REF", forced_sale_eok=s["forced_sale_oct6_15_eok"], oct_drop_pct=f"{drop:.1f}",
        own_money_change_pct=f"{pct(eq_after, own):.1f}", note="한국 10월 반대매매·하락 — 대본에서 뺌")
    # 10번 — 2배 상품: 하루 -10% 뒤 제자리로 돌아오는 상승률, 같은 이틀의 2배 상품
    d1 = s["two_x_day1_pct"] / 100
    d2 = 1 / (1 + d1) - 1
    two_x = (1 + 2 * d1) * (1 + 2 * d2) - 1
    out("Q10", day1_pct=f"{d1 * 100:.1f}", day2_back_to_start_pct=f"{d2 * 100:.2f}", two_x_after_2days_pct=f"{two_x * 100:.2f}",
        conl=f"fund {s['conl_fund_pct']}%/yr vs investors {s['conl_investor_pct']}%/yr")
    out("Q10", kr_single_2x_40s_pct=f"{s['single_2x_40s_eok'] / s['single_2x_total_eok'] * 100:.1f}",
        total_jo=f"{s['single_2x_total_eok'] / 10000:.2f}", say="한국 단일 종목 2배 ETF — 40대가 가장 많이 보유(34%)")

    # ------------------------------------------------------------ 테스트 규칙 검사
    out("RULE", questions=len(QUESTIONS), levels=LEVELS, max_total=len(QUESTIONS) * max(LEVELS),
        pass_min=PASS_MIN, caution=f"{CAUTION_MIN}~{PASS_MIN - 5}", fail=f"0~{CAUTION_MIN - 5}",
        cut_questions=[q for q, _, c, _ in QUESTIONS if c],
        best_letter="".join(max(k, key=k.get) for *_, k in QUESTIONS), zero_letter="".join(min(k, key=k.get) for *_, k in QUESTIONS))
    for q, name, _, key in QUESTIONS:  # 문제마다 0·5·10 이 하나씩 있는지
        if sorted(key.values()) != list(LEVELS):
            log.warning(f"q={q} key={key} problem=점수 0·5·10 이 하나씩이 아님", extra={"stage": "RULE"})
    # 모든 경우(3^10)를 채점해 등급이 빈틈·겹침 없이 나뉘는지 본다. '아무렇게나 고르면'의 비율은 사람의 분포가 아니다.
    bands, totals = Counter(), Counter()
    for combo in itertools.product("ABC", repeat=len(QUESTIONS)):
        t, g, _ = grade("".join(combo))
        bands[g] += 1
        totals[t] += 1
    n = sum(bands.values())
    out("CHECK", combos=n, **{k: f"{v} ({v / n * 100:.1f}%)" for k, v in sorted(bands.items())})
    log.debug(" ".join(f"{t}:{c}" for t, c in sorted(totals.items())), extra={"stage": "CHECK"})
    for t in range(0, 101, 5):  # 5점 단위 총점마다 등급이 하나로 정해지는지 (과락 없을 때)
        g = "통과" if t >= PASS_MIN else "주의" if t >= CAUTION_MIN else "불통과"
        log.debug(f"total={t} grade_without_cut={g}", extra={"stage": "CHECK"})

    # ------------------------------------------------------------ 가상 응시 (규칙이 뜻대로 움직이는지 보는 예 — 실제 사람 아님)
    virtual = [  # 문제 1~10 의 점수 줄 → 보기 글자로 바꿔 채점
        ("V1 원칙형", [10, 10, 10, 5, 10, 10, 10, 10, 10, 10]),
        ("V2 점수는 높지만 빚을 냄", [10, 10, 10, 10, 10, 10, 10, 10, 0, 10]),
        ("V3 따라 사고 자주 사고팖", [0, 0, 5, 0, 0, 5, 0, 0, 5, 5]),
        ("V4 75점이지만 두 배 상품", [10, 10, 10, 10, 10, 10, 5, 5, 5, 0]),
        ("V5 딱 70점", [10, 10, 10, 10, 0, 0, 5, 5, 10, 10]),
        ("V6 65점", [10, 10, 10, 0, 0, 5, 5, 5, 10, 10]),
    ]
    for name, levels in virtual:
        ans = letters_for(levels)
        t, g, fails = grade(ans)
        out("VIRTUAL", name=name.replace(" ", "_"), answers=ans, total=t, grade=g, cut_fail=fails or "-")

    out("DONE", note="연구·교육용 — 투자 권유 아님")


if __name__ == "__main__":
    main()
