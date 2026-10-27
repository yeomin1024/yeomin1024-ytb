#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.2 — 2026-10-27 — (브링커 → 폭스 · 사건 주가 EVENT) 정답 = '재무제표로 저평가였고 3년 뒤 크게 오른' 미국 회사 5곳 · 외부 영향 점검 (사용자 지시
#          "재무제표로 저평가 종목 판단하여 몇년 후 크게 주가가 오른 사례를 정답으로해서 변경해 너무 유명한거 말고 적당히 알만한 종목들로 선정해"
#          → "5개 정도만 찾고 재무지표를 상세하게 분석하는 걸로 해 그런건 외부 영향이 있을 거야 최대한 외부 영향이 없는걸로 찾아봐").
#          5항목 × 0·10·20점 · 3년 주가 배수 = 주당이익(EPS) 배수 × PER 배수 로 나눠 '회사 실적 때문인지 시장 평가 때문인지' 보이고,
#          같은 기간 업종 ETF·같은 업종 회사·S&P 500 과 견줘 업종 전체의 바람(외부 영향)이 아니었는지 점검.
# (v1.1 — 2026-10-27 — 실제 미국 회사 10곳(정답·오답 섞기) · 도입 마이크론. v1.0 — 최초: SK하이닉스 · 가상 회사.)
#
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.2 | 2026-10-27 | 저평가 5곳 · csv 2개(us_value_fundamentals·us_value_prices)에서 읽음 · 분해·외부 영향 점검 · 반대 예 BLDR · 0·10·20점 | main · load_fund · load_prices · case_report |
# | v1.1 | 2026-10-27 | 실제 미국 회사 10곳 · 미리 보기 점검 | main · load_prices |
# | v1.0 | 2026-10-27 | 최초 | main · load_prices · sentence_report |
#
# 실행: python3 -B stock/source/jaemu-test-2026-10/calc/calc.py            (INFO)
#       python3 -B stock/source/jaemu-test-2026-10/calc/calc.py --debug    (DEBUG — 문장마다 글자 수)
# 입력: 같은 폴더 us_value_fundamentals.csv · us_value_prices.csv (Yahoo, 2026-10-27 받음). 네트워크 없음 → 같은 입력이면 같은 출력.
# 미리 보기 점검: t0 = 회계연도 끝 + 122일 뒤 첫 종가 (연차 보고서가 모두 나온 뒤) — 상황 문장은 그 연도 숫자와 t0 까지의 주가만.
#                 3년 뒤 연도(fy3)는 t3 보다 90일 이상 앞에 끝난 것만 (그때 발표돼 있던 실적).
# 고른 방법(치우침): 크게 오른 사례만 골랐다 → 정리에서 반대 예(같은 때 더 싸 보였던 BLDR 3년 뒤 -20%)를 함께 말한다.
# ※ 연구·교육용 — 투자 권유가 아님.
import csv
import logging
import math
import re
import sys
from datetime import date, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / "tools"))
import test_score as ts  # noqa: E402

VERSION = "v1.2"
B = 1e9
LEVELS = (0, 10, 20)   # 5항목 × 20 = 100점 (통과 70 · 주의 40~60 · 불통과 30 이하 — test_score 기준 그대로)

# 회사 · 회계연도(그때 · 3년 뒤) · 비교 대상 — 숫자는 csv 에서
CASES = {
    1: dict(ticker="WSM", name="윌리엄스소노마", what="가구·주방용품 회사 (포터리반)", fy0="2023-01-31", fy3="2026-01-31", etf="XRT", peer="RH",
            fear="미국 주택 거래가 크게 줄어, 가구가 안 팔릴 거라는 걱정"),
    2: dict(ticker="TPR", name="태피스트리", what="가방 브랜드 회사 (코치·케이트 스페이드)", fy0="2023-06-30", fy3="2026-06-30", etf="XRT", peer=None,
            fear="2023-08 다른 패션 회사를 85억 달러에 인수하겠다고 발표 → 빚이 늘 거라는 걱정 (2024-11 인수 취소)"),
    3: dict(ticker="FOXA", name="폭스 코퍼레이션", what="방송 회사 (폭스 뉴스·폭스 스포츠)", fy0="2023-06-30", fy3="2026-06-30", etf="XLC", peer="CMCSA",
            fear="유료 방송 가입자가 해마다 줄어 방송 회사의 앞날이 어둡다는 걱정"),
    4: dict(ticker="EXPE", name="익스피디아", what="온라인 여행 예약 회사", fy0="2022-12-31", fy3="2025-12-31", etf="XLY", peer="BKNG",
            fear="주가가 1년 새 절반 가까이 빠짐 · PER 43"),
    5: dict(ticker="SFM", name="스프라우츠 파머스 마켓", what="식료품 마트 회사", fy0="2022-12-31", fy3="2025-12-31", etf="XLP", peer="KR",
            fear="눈에 띄는 것 없는 평범한 PER 16"),
}
COUNTER = dict(ticker="BLDR", name="빌더스 퍼스트소스", fy0="2022-12-31", fy3="2025-12-31", etf="XLI")  # 반대 예 (정리에서만)
# 뺀 후보 (요약본 [근거] 3번): 브링커(EAT) — 3년 5.9배·업종보다 3.8배로 회사 실력이 컸지만, 그때 재무제표(PER 15·잉여현금 4.8%·자본 마이너스·이자 3.2배)로는
#   '저평가'라 하기 어려워 10점 답을 결과 없이 정당화할 수 없음 → 뺌. 숫자는 csv 에 남김 (DROPPED 줄).
DROPPED = dict(ticker="EAT", name="브링커 (칠리스)", fy0="2023-06-30", fy3="2026-06-30", etf="XLY", peer="DRI")

QUESTIONS = [  # (번호, 짧은 이름, 과락 문항인가, 보기 → 점수) — 요약본 [항목N] 의 보기 순서와 같아야 한다
    (1, "윌리엄스소노마 — PER 7·잉여현금 9%", False, {"A": 0, "B": 20, "C": 10}),
    (2, "태피스트리 — PER 7·잉여현금 12%", False, {"A": 10, "B": 0, "C": 20}),
    (3, "폭스 — PER 13·잉여현금 10%·자사주 14%", False, {"A": 20, "B": 0, "C": 10}),
    (4, "익스피디아 — PER 43·잉여현금 19%", False, {"A": 0, "B": 10, "C": 20}),
    (5, "스프라우츠 — PER 16·자사주·이익률", False, {"A": 20, "B": 10, "C": 0}),
]
VIRTUAL = [  # 실제 사람 아님 — 규칙이 뜻대로 움직이는지
    ("V1 숫자를 읽는 사람", [20, 20, 20, 20, 20]),
    ("V2 걱정 뉴스에 늘 피하는 사람", [0, 0, 0, 0, 0]),
    ("V3 숫자 없이 조금씩 사는 사람", [10, 10, 10, 10, 10]),
    ("V4 딱 70점", [20, 20, 20, 10, 0]),
    ("V5 60점", [20, 20, 10, 10, 0]),
]

INTRO = [
    "최근 인기 종목만 쫓다가, 손실 본 투자자가 많습니다.",
    "미국 마이크론은 6월 사상 최대 매출을 발표했지만, 넉 달 만에 주가가 25% 빠졌습니다.",
    "반대로 재무제표로 보면 싸게 팔리다가, 몇 년 뒤 몇 배가 된 회사도 있습니다.",
    "실제 미국 회사 다섯 곳의 재무제표로, 저평가를 알아보는 테스트를 만들었습니다.",
    "회사 이름은 해설에서 공개합니다.",
    "항목마다 답을 고르고, 그 점수를 모두 더해 주세요.",
    "그럼 시작하겠습니다.",
]
SHORTS = [
    "재무제표만 보고, 몇 배 오를 주식을 알아볼 수 있을까?",
    "실제 미국 회사 다섯 곳의 재무제표로, 저평가를 알아보는 테스트입니다.",
    "본인이라면 어떻게 할지, 항목마다 답을 골라 보세요.",
    "모두 그때 공개된 숫자만 보여 드립니다.",
    "집이 안 팔린다는 뉴스 속, PER 7에 이익률 17%인 가구 회사, 매수하시나요?",
    "인수로 빚이 는다는 걱정 속, PER 7에 잉여현금 12%인 가방 회사는요?",
    "시청자가 준다는 방송 회사가, 시가총액의 14%만큼 자사주를 산다면요?",
    "PER 43인데, 잉여현금이 시가총액의 19%인 여행 회사는요?",
    "PER 16으로 평범해 보이는 식료품 마트 회사는요?",
    "다섯 회사의 이름과 3년 뒤 주가는, 아래 영상에서 확인하세요.",
]
LONG_RATE, SHORT_RATE, SHORT_GAP, SHORT_END, MAX_CHARS = 5.67, 6.33, 0.46, 2.5, 50


# ---------------------------------------------------------------- 로그
class StageFormatter(logging.Formatter):
    def format(self, record):
        stage = getattr(record, "stage", "CALC")
        return f"[{stage}] [{self.formatTime(record, '%Y-%m-%dT%H:%M:%S')}] {record.getMessage()}"


log = logging.getLogger("jaemu-test-calc")


def out(stage, **kv):
    log.info(" ".join(f"{k}={v}" for k, v in kv.items()), extra={"stage": stage})


def rows_of(path):
    try:
        with open(path, encoding="utf-8") as f:
            return list(csv.DictReader(line for line in f if not line.startswith("#")))
    except OSError as e:
        log.error(f"file={path} error={e} next_step=Yahoo 에서 다시 받기 (요약본 [근거] 1번)", extra={"stage": "LOAD"})
        raise


def load_fund(path):
    """{(ticker, fy_end): {field: value}} — 같은 칸이 두 번 나오면 경고."""
    f, dup = {}, []
    for r in rows_of(path):
        key = (r["ticker"], r["fy_end"])
        if r["field"] in f.setdefault(key, {}):
            dup.append(key + (r["field"],))
        f[key][r["field"]] = float(r["value"])
    out("LOAD", file=path.name, rows=sum(len(v) for v in f.values()), years=len(f), duplicates=dup or "-")
    return f


def load_prices(path):
    """{(ticker, of): (t0_date, t0, t3_date, t3, ago)} — 0 이하·날짜 순서 점검."""
    p, bad = {}, []
    for r in rows_of(path):
        v = (r["t0_date"], float(r["t0_close"]), r["t3_date"], float(r["t3_close"]), float(r["ago_close"]) if r["ago_close"] else None)
        if v[1] <= 0 or v[3] <= 0 or v[2] <= v[0]:
            bad.append(r["ticker"])
        p[(r["ticker"], r["of"])] = v
    out("LOAD", file=path.name, rows=len(p), problems=bad or "-")
    return p


def case_report(q, c, F, P):
    """한 회사: 그때 숫자(상황 문장) · 3년 뒤 숫자(해설) · 분해 · 비교. 미리 보기 문제 수를 돌려준다."""
    t = c["ticker"]
    a, b = F[(t, c["fy0"])], F[(t, c["fy3"])]
    t0d, t0, t3d, t3, ago = P[(t, t)]
    look = 0
    if date.fromisoformat(c["fy0"]) + timedelta(days=122) > date.fromisoformat(t0d):
        look += 1
    if date.fromisoformat(c["fy3"]) + timedelta(days=90) > date.fromisoformat(t3d):
        look += 1
    mc = t0 * a["OrdinarySharesNumber"]
    eps0, eps3 = a["DilutedEPS"], b["DilutedEPS"]
    opm0 = a["OperatingIncome"] / a["TotalRevenue"] * 100
    opm3 = b["OperatingIncome"] / b["TotalRevenue"] * 100
    then = dict(price=f"{t0:.2f}", mcap_bn=f"{mc / B:.2f}", per=f"{t0 / eps0:.1f}", fcf_yield_pct=f"{a['FreeCashFlow'] / mc * 100:.1f}",
                op_margin_pct=f"{opm0:.1f}", revenue_bn=f"{a['TotalRevenue'] / B:.2f}", net_income_bn=f"{a['NetIncome'] / B:.3f}",
                buyback_of_mcap_pct=f"{-a.get('RepurchaseOfCapitalStock', 0) / mc * 100:.1f}",
                net_debt_bn=f"{(a['TotalDebt'] - a.get('CashCashEquivalentsAndShortTermInvestments', 0)) / B:.2f}",
                equity_bn=f"{a['StockholdersEquity'] / B:.2f}")
    if a["StockholdersEquity"] > 0:
        then["roe_pct"] = f"{a['NetIncome'] / a['StockholdersEquity'] * 100:.0f}"
    if a.get("InterestExpense"):
        then["interest_cover"] = f"{a['OperatingIncome'] / a['InterestExpense']:.1f}"
    if ago:
        then["change_1y_pct"] = f"{(t0 / ago - 1) * 100:.0f}"
    out(f"Q{q}", name=c["name"], t0=t0d, **then)
    px, epsx = t3 / t0, eps3 / eps0
    perx = px / epsx
    nix, shx = b["NetIncome"] / a["NetIncome"], b["OrdinarySharesNumber"] / a["OrdinarySharesNumber"]
    eps_share = math.log(epsx) / math.log(px) * 100
    out("REVEAL", q=q, name=c["name"], t3=t3d, price_x=f"{px:.2f}", revenue_x=f"{b['TotalRevenue'] / a['TotalRevenue']:.2f}",
        op_margin=f"{opm0:.1f}→{opm3:.1f}", net_income_x=f"{nix:.2f}", shares_x=f"{shx:.2f}", eps_x=f"{epsx:.2f}",
        per=f"{t0 / eps0:.1f}→{t3 / eps3:.1f}", per_x=f"{perx:.2f}", eps_share_of_rise_pct=f"{eps_share:.0f}")
    cmp = {}
    for k in ("etf", "peer"):
        if c.get(k):
            x0, x3 = P[(c[k], t)][1], P[(c[k], t)][3]
            cmp[f"{c[k]}_x"] = f"{x3 / x0:.2f}"
    s0, s3 = P[("^GSPC", t)][1], P[("^GSPC", t)][3]
    etfx = P[(c["etf"], t)][3] / P[(c["etf"], t)][1]
    out("EXTERNAL", q=q, spx_x=f"{s3 / s0:.2f}", **cmp, vs_etf=f"{px / etfx:.2f}",
        note="업종 ETF 보다 몇 배 더 올랐나 — 업종 전체 바람이면 1 에 가까움")
    if eps_share < 40:
        log.warning(f"q={q} name={c['name']} eps_share={eps_share:.0f}% note=상승의 대부분이 PER 회복(시장 평가) — 해설에서 그렇다고 말함",
                    extra={"stage": "EXTERNAL"})
    return look


def syllables(text):
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
    out("LOAD", version=VERSION, test_score=ts.VERSION, cases=len(CASES))
    F = load_fund(HERE / "us_value_fundamentals.csv")
    P = load_prices(HERE / "us_value_prices.csv")

    mu = P[("MU", "MU")]
    out("INTRO", peak=f"{mu[0]}:{mu[1]:,.2f}", last=f"{mu[2]}:{mu[3]:,.2f}", from_peak_pct=f"{(mu[3] / mu[1] - 1) * 100:.1f}",
        say="6월 사상 최대 매출(FY26 3분기) → 넉 달 만에 25% ↓")

    look = sum(case_report(q, c, F, P) for q, c in CASES.items())
    log.info("뺀 후보 — 아래 Q0·REVEAL q=0 은 대본에 쓰지 않음 (요약본 [근거] 3번)", extra={"stage": "DROPPED"})
    case_report(0, DROPPED, F, P)
    out("LOOKAHEAD", checked=len(CASES), problems=look, rule="fy0 + 122일 ≤ t0 · fy3 + 90일 ≤ t3")
    if look:
        log.warning(f"lookahead_problems={look} next_step=t0·t3 날짜 다시", extra={"stage": "LOOKAHEAD"})

    # 사건 주가 — 태피스트리 인수 발표·무산 (상황·해설 문장)
    for ev in ("deal_announced", "deal_cancelled"):
        d0, p0, d1, p1, _ = P[("TPR", ev)]
        out("EVENT", ticker="TPR", event=ev, before=f"{d0}:{p0:.2f}", after=f"{d1}:{p1:.2f}", day_change_pct=f"{(p1 / p0 - 1) * 100:.1f}")
    pre, t0 = P[("TPR", "deal_announced")][1], P[("TPR", "TPR")][1]
    out("EVENT", ticker="TPR", pre_deal_to_t0_pct=f"{(t0 / pre - 1) * 100:.0f}", say="발표 날 16% ↓ · 석 달 새 32% ↓ → PER 7")
    # 반대 예 — 같은 때 더 싸 보였지만 3년 뒤 빠진 회사 (정리에서 치우침 알림)
    c = COUNTER
    a = F[(c["ticker"], c["fy0"])]
    t0d, t0, t3d, t3, _ = P[(c["ticker"], c["ticker"])]
    mc = t0 * a["OrdinarySharesNumber"]
    out("COUNTER", name=c["name"], t0=t0d, per=f"{t0 / a['DilutedEPS']:.1f}", fcf_yield_pct=f"{a['FreeCashFlow'] / mc * 100:.1f}",
        t3=t3d, price_x=f"{t3 / t0:.2f}", eps_x=f"{F[(c['ticker'], c['fy3'])]['DilutedEPS'] / a['DilutedEPS']:.2f}",
        etf_x=f"{P[(c['etf'], c['ticker'])][3] / P[(c['etf'], c['ticker'])][1]:.2f}")

    problems = ts.check_rules(QUESTIONS, out, log, levels=LEVELS)
    ts.run_virtual(QUESTIONS, VIRTUAL, out)
    intro_sec = sentence_report("intro", INTRO, LONG_RATE)
    if intro_sec > 30:
        log.warning(f"intro_sec={intro_sec:.1f} next_step=도입을 30초 안으로 줄임", extra={"stage": "TEXT"})
    sentence_report("shorts", SHORTS, SHORT_RATE, SHORT_GAP, SHORT_END)
    out("SCRIPT", rule=f"{ts.PASS_MIN}점 이상 통과 · {ts.CAUTION_MIN}~{ts.PASS_MIN - 10} 주의 · {ts.CAUTION_MIN - 10} 이하 불통과 · 과락 없음",
        rule_problems=problems, lookahead_problems=look)
    out("DONE", note="연구·교육용 — 투자 권유 아님")


if __name__ == "__main__":
    main()
