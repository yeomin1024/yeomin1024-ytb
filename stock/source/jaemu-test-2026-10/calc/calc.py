#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-27 — 최초. 「재무제표 테스트」 요약본(요약본.txt v1.0)의 숫자를 모두 이 코드 출력으로만 쓴다
#          (CLAUDE.md '숫자는 계산 코드 출력만'). 사용자 지시 2026-10-27: "1번으로 일단 요약본 쇼츠 내용도 포함해서 만들어봐"
#          (1번 = 「재무제표 보고 주식 고르면 손해 볼 사람들의 테스트」 — PER 항목 포함, 판단 이유에 점수).
#
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.0 | 2026-10-27 | 최초 — 도입 실제 숫자(SK하이닉스 2분기 실적·발표일 종가) · 항목 가상 숫자 · 점수 규칙(tools/test_score.py v1.0) · 문장 길이 | main · load_prices · sentence_report |
#
# 실행: python3 stock/source/jaemu-test-2026-10/calc/calc.py            (INFO)
#       python3 stock/source/jaemu-test-2026-10/calc/calc.py --debug    (DEBUG — 문장마다 글자 수)
# 입력: 아래 SRC (값마다 출처·기준일) + 같은 폴더 sk_hynix_2026.csv (Yahoo 종가, 2026-10-27 받음). 네트워크 없음 → 같은 입력이면 같은 출력.
# 미리 보기 편향 점검: 도입 숫자는 모두 2026-10-27 이전에 공개된 값(7/29 공시 · 그날까지의 종가)만 쓴다. 항목 숫자는 가상 회사.
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

VERSION = "v1.0"

# ---------------------------------------------------------------- 입력 (출처는 요약본 [근거] 1번과 같다)
SRC = {
    # 도입 — 실제 (한국)
    "sk_q2_revenue_eok": 793187,        # SK하이닉스 2026년 2분기 연결 매출 79조 3,187억 원 — 2026-07-29 공시 (MTN·시대경제 보도)
    "sk_q2_op_profit_eok": 605426,      # 같은 분기 영업이익 60조 5,426억 원 — 분기 사상 최대 (같은 보도)
    "sk_q2_op_margin_pct": 76.3,        # 영업이익률 (같은 보도)
    "sk_q2_consensus_low_jo": 63,       # 증권가 전망 "63조 원을 넘어설 것" (MTN 2026-07-29) — [REF], 대본은 숫자 없이 "시장 예상치에 못 미쳤다"
    "sk_q2_consensus_high_jo": 64,      # "영업이익 역대 최대 64조 전망" (다음·SBS 2026-07-29) — 출처끼리 1조 차이라 대본에 안 씀
    "announce_date": "2026-07-29",      # 발표일 (아침 공시)
    "prev_date": "2026-07-28",
    "peak_date": "2026-06-22",          # 2026년 종가 최고 (csv 로 다시 확인)
    "last_date": "2026-10-27",
    # 항목 — 가상 회사 (대본은 '한 해운 회사' 처럼 이름 없이)
    "q2_per": 3,                        # PER 15 이하 검색에서 나온 해운 회사 PER
    "q2_profit_next_ratio": 1 / 3,      # 내년 이익이 올해의 3분의 1 로 줄면 (가정)
    "q3_bank_per": 5, "q3_soft_per": 40,
    "q4_op_profit_growth_pct": 50, "q4_receivable_share_pct": 50,   # 영업이익 +50% · 받지 못한 돈 = 매출의 절반
    "q5_net_profit_multiple": 10, "q5_per_before": 20,               # 순이익 10배 → PER 20 이 몇이 되나 (주가 그대로)
    "q6_debt_to_equity": 5, "q6_interest_coverage": 0.8,             # 부채 = 자본의 5배 · 영업이익 ÷ 이자 = 0.8 (이자를 다 못 냄)
    "q7_revenue_growth_pct": 30, "q7_years": 3, "q7_share_multiple": 2, "q7_profit_growth_pct": 50,
    "q8_yield_pct": 10, "q8_payout_ratio": 1.5,                      # 배당 = 순이익의 1.5배
    "q9_drop_pct": 50,                                               # 반값
    "q10_loss_years": 5,
}

QUESTIONS = [  # (번호, 짧은 이름, 과락 문항인가, 보기 → 점수) — 요약본 [항목N] 의 보기 순서와 같아야 한다
    (1, "사상 최대 실적 뉴스에 매수", False, {"A": 0, "B": 5, "C": 10}),
    (2, "PER 이 낮으면 싸다", False, {"A": 10, "B": 0, "C": 5}),
    (3, "다른 업종끼리 PER 비교", False, {"A": 0, "B": 10, "C": 5}),
    (4, "이익만 늘고 현금은 안 들어옴", False, {"A": 10, "B": 0, "C": 5}),
    (5, "한 번 판 땅으로 늘어난 순이익", False, {"A": 0, "B": 5, "C": 10}),
    (6, "이자도 못 내는 큰 회사", False, {"A": 0, "B": 10, "C": 5}),
    (7, "주식 수가 2배가 된 성장", False, {"A": 0, "B": 5, "C": 10}),
    (8, "번 돈보다 많은 배당", False, {"A": 10, "B": 0, "C": 5}),
    (9, "감사보고서를 못 낸 반값 주식", True, {"A": 0, "B": 5, "C": 10}),
    (10, "자본이 마이너스인 적자 회사", True, {"A": 5, "B": 10, "C": 0}),
]

VIRTUAL = [  # 문제 1~10 의 점수 줄 (실제 사람 아님)
    ("V1 이유를 확인하는 사람", [10, 10, 10, 10, 10, 5, 10, 10, 10, 10]),
    ("V2 숫자 하나만 보는 사람", [0, 0, 0, 0, 0, 5, 5, 0, 5, 5]),
    ("V3 다 맞혔지만 의견 거절 주식", [10, 10, 10, 10, 10, 10, 10, 10, 0, 10]),
    ("V4 딱 70점", [10, 10, 10, 10, 5, 5, 5, 5, 5, 5]),
    ("V5 65점", [10, 10, 5, 5, 5, 5, 5, 5, 10, 5]),
]

# 문장 길이 점검 — 도입(롱폼)·짝 쇼츠 대본 (요약본과 같은 글)
INTRO = [
    "최근 실적이 좋다는 회사의 주가도 크게 빠지며, 손실 본 개인이 늘고 있습니다.",
    "한국의 SK하이닉스는 분기 사상 최대 실적을 발표한 날, 주가가 10% 가까이 빠졌습니다.",
    "이렇게 실적을 보고도 손해 보는 투자자들에겐, 공통된 판단 습관이 있습니다.",
    "그것을 바탕으로, 재무제표를 잘못 읽어 손해 볼 사람인지 점검하는 테스트를 만들었습니다.",
    "항목마다 본인의 답을 고르고, 그 점수를 모두 더해 주세요.",
    "그럼 시작하겠습니다.",
]
SHORTS = [
    "실적 좋은 주식을 매수하고도, 손해 볼 사람일까?",
    "재무제표를 읽는 습관을 점검하는 테스트입니다.",
    "항목마다 본인의 답을 골라 보세요.",
    "사상 최대 실적 뉴스가 나오면, 어떻게 하시나요?",
    "PER 이 3인 주식, 싸다고 보시나요?",
    "은행과 소프트웨어 회사의 PER, 어떻게 견주시나요?",
    "이익은 늘었는데 현금이 안 들어오는 회사, 매수하시나요?",
    "순이익이 10배가 되어 PER 이 2가 된 회사, 어떻게 보시나요?",
    "이자도 다 못 내는 큰 회사, 망하지 않는다고 보시나요?",
    "매출은 늘었지만 주식 수가 2배가 된 회사, 어떻게 보시나요?",
    "번 돈보다 배당을 더 주는 회사, 매수하시나요?",
    "감사보고서를 못 내고 반값이 된 주식, 싸다고 보시나요?",
    "자본이 마이너스가 된 회사에, 남은 돈을 넣으시나요?",
    "선택한 답에 따른 결과는 아래 영상에서 확인하세요.",
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


def load_prices(path):
    """sk_hynix_2026.csv → {날짜: 종가}. 빈 값·0 이하·겹친 날짜·날짜 순서를 점검해 경고로 남긴다."""
    try:
        with open(path, encoding="utf-8") as f:
            rows = list(csv.DictReader(line for line in f if not line.startswith("#")))
    except OSError as e:
        log.error(f"file={path} error={e} next_step=Yahoo 에서 다시 받기 (요약본 [근거] 1번)", extra={"stage": "LOAD"})
        raise
    prices, problems = {}, []
    for r in rows:
        d, c = r["date"], float(r["close"])
        if d in prices:
            problems.append(f"겹친 날짜 {d}")
        if c <= 0:
            problems.append(f"0 이하 {d}")
        prices[d] = c
    dates = list(prices)
    if dates != sorted(dates):
        problems.append("날짜 순서가 섞임")
    out("LOAD", file=path.name, rows=len(prices), first=dates[0], last=dates[-1], problems=problems or "-")
    if problems:
        log.warning(f"problems={problems} next_step=csv 를 출처와 다시 대조", extra={"stage": "CHECK"})
    return prices


def syllables(text):
    """읽는 음절 대충 세기 — 한글 글자 + 숫자·영문 글자 하나씩 (PER·SK 처럼 읽는 소리가 긴 말은 조금 짧게 잡힘)."""
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
    s = SRC
    out("LOAD", version=VERSION, test_score=ts.VERSION, inputs=len(s), source="SRC dict + sk_hynix_2026.csv")
    p = load_prices(HERE / "sk_hynix_2026.csv")

    # ------------------------------------------------------------ 도입 — 실제 숫자 (한국)
    missing = [d for d in (s["prev_date"], s["announce_date"], s["peak_date"], s["last_date"]) if d not in p]
    if missing:
        log.warning(f"missing_dates={missing} next_step=csv 기간 확인", extra={"stage": "CHECK"})
        return
    peak_d = max(p, key=p.get)
    if peak_d != s["peak_date"]:
        log.warning(f"csv_peak={peak_d} src_peak={s['peak_date']} next_step=SRC peak_date 고침", extra={"stage": "CHECK"})
    day = pct(p[s["announce_date"]], p[s["prev_date"]])
    out("INTRO", op_profit_jo=f"{s['sk_q2_op_profit_eok'] / 10000:.2f}", revenue_jo=f"{s['sk_q2_revenue_eok'] / 10000:.2f}",
        margin_pct=s["sk_q2_op_margin_pct"], say="분기 사상 최대 실적 (영업이익 60조 원)")
    out("INTRO", prev=f"{s['prev_date']}:{p[s['prev_date']]:,.0f}", announce=f"{s['announce_date']}:{p[s['announce_date']]:,.0f}",
        day_change_pct=f"{day:.2f}", say="발표한 날 주가가 10% 가까이 빠졌습니다")
    out("REF", consensus_jo=f"{s['sk_q2_consensus_low_jo']}~{s['sk_q2_consensus_high_jo']}",
        miss_pct=f"{pct(s['sk_q2_op_profit_eok'] / 10000, s['sk_q2_consensus_low_jo']):.1f}~{pct(s['sk_q2_op_profit_eok'] / 10000, s['sk_q2_consensus_high_jo']):.1f}",
        say="해설: 시장 예상치에는 못 미쳤습니다 (숫자는 출처끼리 달라 안 읽음)")
    out("REF", peak=f"{s['peak_date']}:{p[s['peak_date']]:,.0f}", last=f"{s['last_date']}:{p[s['last_date']]:,.0f}",
        from_peak_pct=f"{pct(p[s['last_date']], p[s['peak_date']]):.1f}", note="6월 고점보다 절반 넘게 — 도입 숫자는 하나만이라 안 씀(설명란)")

    # ------------------------------------------------------------ 항목·해설 — 가상 회사 계산
    per_next = s["q2_per"] / s["q2_profit_next_ratio"]
    out("Q2", per_now=s["q2_per"], profit_next=f"{s['q2_profit_next_ratio']:.3f}", per_if_price_same=f"{per_next:.0f}",
        say="PER = 주가 ÷ 한 주의 이익 · 이익이 3분의 1 로 줄면 PER 3 → 9")
    out("Q3", bank_per=s["q3_bank_per"], soft_per=s["q3_soft_per"], ratio=f"{s['q3_soft_per'] / s['q3_bank_per']:.0f}", say="8분의 1")
    out("Q4", op_profit_growth_pct=s["q4_op_profit_growth_pct"], receivable_share_pct=s["q4_receivable_share_pct"])
    out("Q5", net_profit_multiple=s["q5_net_profit_multiple"], per_before=s["q5_per_before"],
        per_after=f"{s['q5_per_before'] / s['q5_net_profit_multiple']:.0f}", say="순이익 10배 → PER 20 → 2 (주가 그대로)")
    out("Q6", debt_to_equity=s["q6_debt_to_equity"], interest_coverage=s["q6_interest_coverage"],
        interest_unpaid_pct=f"{(1 - s['q6_interest_coverage']) * 100:.0f}", say="영업이익으로 이자의 80%만 냄")
    rev = (1 + s["q7_revenue_growth_pct"] / 100) ** s["q7_years"]
    per_share = (1 + s["q7_profit_growth_pct"] / 100) / s["q7_share_multiple"]
    out("Q7", revenue_multiple_3y=f"{rev:.3f}", revenue_growth_3y_pct=f"{(rev - 1) * 100:.1f}", share_multiple=s["q7_share_multiple"],
        profit_growth_pct=s["q7_profit_growth_pct"], per_share_profit_change_pct=f"{(per_share - 1) * 100:.0f}",
        say="이익 50% 늘어도 주식 수 2배 → 한 주의 이익 25% 줄어듦 · 이익이 같으면 한 주의 몫은 절반")
    out("Q8", yield_pct=s["q8_yield_pct"], payout_ratio=s["q8_payout_ratio"],
        borrowed_share_of_dividend_pct=f"{(1 - 1 / s['q8_payout_ratio']) * 100:.0f}", say="배당의 3분의 1 은 번 돈이 아님")
    back = 1 / (1 - s["q9_drop_pct"] / 100) - 1
    out("Q9", drop_pct=-s["q9_drop_pct"], back_to_start_pct=f"{back * 100:.0f}", say="반값 → 제자리까지 +100%")
    out("Q10", loss_years=s["q10_loss_years"], rule="한국: 감사의견 부적정·거절 · 사업연도 말 자본 전액 잠식 = 상장 폐지 사유 (유가증권시장 상장규정 — 요약본 [근거] 2번)")

    # ------------------------------------------------------------ 점수 규칙 (공용)
    problems = ts.check_rules(QUESTIONS, out, log)
    ts.run_virtual(QUESTIONS, VIRTUAL, out)

    # ------------------------------------------------------------ 문장 길이
    intro_sec = sentence_report("intro", INTRO, LONG_RATE)
    if intro_sec > 30:
        log.warning(f"intro_sec={intro_sec:.1f} next_step=도입을 30초 안으로 줄임", extra={"stage": "TEXT"})
    sentence_report("shorts", SHORTS, SHORT_RATE, SHORT_GAP, SHORT_END)

    out("SCRIPT", intro_day_change_pct=f"{day:.1f}", q2_per=f"{s['q2_per']}→{per_next:.0f}", q5_per=f"{s['q5_per_before']}→{s['q5_per_before'] // s['q5_net_profit_multiple']}",
        q7_per_share_pct=f"{(per_share - 1) * 100:.0f}", q9_back_pct=f"{back * 100:.0f}",
        rule=f"{ts.PASS_MIN}점 이상 통과 · {ts.CAUTION_MIN}~{ts.PASS_MIN - 5} 주의 · {ts.CAUTION_MIN - 5} 이하 불통과 · 9·10번 0점 과락",
        rule_problems=problems)
    out("DONE", note="연구·교육용 — 투자 권유 아님")


if __name__ == "__main__":
    main()
