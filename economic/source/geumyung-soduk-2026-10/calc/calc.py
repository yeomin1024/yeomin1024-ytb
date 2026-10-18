#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""배당·이자로 생활비 — 금융소득 연 2,000만 원과 건보료 — 대본 숫자 계산 (단위: 만 원, 건보료는 원)

VERSION: v1.0 — 2026-10-18 — 최초 작성 (대본 geumyung-soduk-2026-10.txt v1.0 의 숫자를 모두 이 코드로 낸다)
  - A '남편 이름 일반 계좌 6억 원' vs B '부부로 나누고(3억·3억) 해마다 ISA 2,000만 원씩' vs B0 '나누기만' vs B+ 'ISA + 연금저축'
  - 소득세(제62조 비교과세) · 피부양자 2,000만 원 기준(부부 모두) · 지역 보험료(이자·배당 1,000만 원 기준) · 3년 합계 · 민감도

법 (GitHub legalize-kr 에서 2026-10-18 시행 중인 판 — `tools/law_text.py --source mirror`, 자세히 ../checklist.md A표):
  - 소득세법 [시행 2026-04-21] [제21548호] (legalize-kr c4699a2b1b)
      제14조 ③6호 이자·배당 합계 2천만 원(종합과세기준금액) 이하이면 종합소득에 합산하지 않음 · ③1·5호 비과세·조특법 분리과세 소득은 합산 안 함
      제62조 기준금액을 넘으면 산출세액 = max(1호 (초과분+다른 소득 − 공제) × 기본세율 + 2천만 × 14%, 2호 이자·배당 × 14% + 다른 소득 기본세율)
      제55조 기본세율 6·15·24·35·38…% · 제50조 기본공제 1명 150만 원(배우자는 소득금액 100만 원 이하)
      제61조 ② 특별세액공제(표준세액공제 포함)는 원천징수세율을 적용받는 이자·배당 산출세액에서 빼지 못함
      제129조 ①1호 라목·2호 나목 이자·배당 원천징수 14% · 제17조 ③ 배당가산 11%(Gross-up — 민감도에서만)
      제20조의3 ①2호 다목 연금계좌 운용 수익은 꺼낼 때 연금소득 · 제129조 ①5의2 연금수령 5%(70세 미만)
  - 조세특례제한법 [시행 2026-06-02] [제21738호] (legalize-kr 52e78d52d5)
      제91조의18 ① ISA 이자·배당은 비과세 한도까지 비과세, 넘는 몫 9% 분리과세 · ② 일반형 200만 원 · ③ 연 2천만 원(누적), 총 1억 원
      제129조의2 ① 직전 3개 과세기간 중 한 번이라도 제14조③6호 소득이 2천만 원을 넘은 사람은 ISA 가입·연장 불가
      제104조의27 고배당기업 배당 분리과세 14~30% (2026-01-01 이후 받는 배당, 신청해야) — 계산에는 넣지 않음 (건보료 반영은 확인 필요)
  - 지방세법 [시행 2026-01-01] [제21308호] 제103조의13 ① 원천징수 소득세의 10% · 제92조 종합소득 지방소득세 = 소득세 세율의 1/10
  - 국민건강보험법 시행령 [시행 2026-10-01] [제36675호] 제41조 ① 이자·배당 포함(비과세 제외) · ③ 1~10월분 전전년도, 11·12월분 전년도 자료
      제44조 ① 보험료율 1만분의 719 · ② 재산 점수당 211.5원
  - 국민건강보험법 시행규칙 [시행 2026-09-28] [제1202호] 제44조 ① 단서 이자·배당(제14조③6호) 1,000만 원 이하면 합산 안 함 · ②1호 이자·배당 전액
      ③ 지역 소득월액 28만 원 이하이면 하한 보험료 · 제2조 ③9호 요건을 못 채우면 공단이 확인한 날 다음 날 피부양자 상실
  - 시행규칙 별표 1의2 피부양자 소득 2천만 원 이하·재산 과표 5.4억 이하·기혼자는 부부 모두 / 시행령 별표 4 재산 점수표 / 하한 20,160원 고시
      → PDF 라 이 환경에서 다시 받지 못함: `economic/source/toejik-geonbo-2026-10/checklist.md` (2026-10-14 law.go.kr 원문 확인) 숫자를 그대로 씀
  - 노인장기요양보험법 시행령 [시행 2026-05-12] 제4조 100만분의 9,448 (건보료의 0.9448/7.19 = 13.14%) — 대본 숫자에는 넣지 않음
  - 상속세 및 증여세법 [시행 2026-01-01] 제53조 1호 배우자에게서 받은 증여 10년 6억 원 공제

가정 (사실이 아니라 예시 — 대본에서 '봤습니다'로 말함, README 3번 표):
  - 58세 동갑 부부, 둘 다 일하지 않음(남편은 56세에 퇴직), 국민연금은 아직 받지 않음, 직장에 다니는 자녀의 피부양자.
  - 금융자산 6억 원이 모두 남편 이름 일반 계좌. 이자·배당 연 4% = 2,400만 원(월 200만 원)으로 생활비. 이자·배당 모두 배당가산(Gross-up) 없는 것으로 봄.
  - 집: 남편 이름 아파트 한 채, 재산세 과세표준 3억 원 (퇴직 후 건보료 편과 같은 집 → 재산 몫 같음).
  - B: 3억 원을 아내 이름으로 (배우자 증여 6억 공제 안 — 증여세 0원, 신고). 부부가 해마다 1월에 ISA 에 2,000만 원씩 3년 (일반형 200만 원).
       ISA 안 이익은 ISA 에 그대로 둔다(일반 계좌 원금은 ISA 로 옮긴 만큼만 줄어듦). 3년째 끝에 해지 → (이익 − 200) × 9.9%.
  - 3년 = 이자·배당을 받는 해 3번. 건보료는 그해 소득이 '다음 해 11월부터 12개월' 잡힌다 (시행령 제41조 ③) → 3년이면 36개월.
  - 건보료는 장기요양보험료를 넣지 않은 금액 (퇴직 후 건보료 편과 같은 방식) — 넣은 금액은 민감도에서 따로.
연구·교육용 예시 계산 — 세무·보험·투자 권유 아님. 실제 보험료는 공단 고지, 세금은 신고 금액이 기준.

실행:  cd economic/source/geumyung-soduk-2026-10/calc && python3 calc.py        # 대본 숫자 + 민감도 (stdout)
       python3 calc.py --log-level DEBUG
로그:  [STAGE] 시각 key=value (stderr)
"""
import argparse
import logging
import math
import sys
import time

VERSION = "v1.0"
LOG = logging.getLogger("geumyung_calc")


def log(stage, level=logging.INFO, **kv):
    LOG.log(level, "[%s] %s %s", stage, time.strftime("%Y-%m-%dT%H:%M:%S"), " ".join(f"{k}={v}" for k, v in kv.items()))


# ───────────────────────── 법 (2026-10-18 시행 중) ─────────────────────────
LOCAL = 1.10                       # 지방소득세 = 소득세의 10% (지방세법 제103조의13 ①, 제92조)
WH = 0.14                          # 이자·배당 원천징수 14% (소득세법 제129조 ①1호 라목·2호 나목)
FIN_LIMIT = 2000                   # 이자소득등 종합과세기준금액 2천만 원 (제14조 ③6호)
BASIC_DED = 150                    # 기본공제 1명 150만 원 (제50조)
BRACKETS = [(1400, 0.06), (5000, 0.15), (8800, 0.24), (15000, 0.35), (30000, 0.38), (50000, 0.40), (100000, 0.42), (math.inf, 0.45)]
GROSS_UP = 0.11                    # 배당가산 11% (제17조 ③ — 민감도에서만)
ISA_FREE = 200                     # ISA 비과세 일반형 200만 원 (조특법 제91조의18 ②2호)
ISA_TAX = 0.09 * LOCAL             # 넘는 몫 9% 분리과세 + 지방세 = 9.9%
ISA_YEAR = 2000                    # ISA 해마다 2천만 원 (③5 — 누적 계산식)
PEN_YEAR = 1800                    # 연금계좌 납입 1년 1,800만 원 (소득세법 시행령 제40조의2 ②1호 가목 — isa-mangi 확인표)
PEN_TAX = 0.05 * LOCAL             # 연금수령 70세 미만 5% + 지방세 = 5.5% (제129조 ①5의2)

RATE = 0.0719                      # 건강보험료율 (시행령 제44조 ①)
POINT_WON = 211.5                  # 재산 점수당 금액 (시행령 제44조 ②)
LOCAL_MIN = 20_160                 # 지역 월 보험료 하한 (고시 — toejik 확인표 A)
LOCAL_MIN_INCOME_MONTH = 280_000   # 소득월액 28만 원 이하 → 하한 (시행규칙 제44조 ③)
FIN_CUT_KENBO = 1000               # 이자·배당 1,000만 원 이하면 건보료 소득에 넣지 않음 (시행규칙 제44조 ① 단서)
DEP_INCOME_LIMIT = 2000            # 피부양자 소득 기준 2천만 원 (별표 1의2 제1호 가목)
DEP_PROP_LIMIT = 54000             # 피부양자 재산 기준 과표 5.4억 원 (만 원)
PROPERTY_DEDUCT = 10000            # 재산 기본 공제 1억 원 (별표 4 제1호)
LTC_RATIO = round(0.9448 / 7.19, 4)  # 장기요양 = 건보료 × 0.1314 (노인장기요양보험법 시행령 제4조)
WORK_EXTRA_DED = 2000              # 직장가입자 보수 외 소득 공제 2천만 원 (법 제71조 ① · 시행령 제41조 ④)
SPOUSE_GIFT_DED = 60000            # 배우자 증여 10년 6억 원 (상증법 제53조 1호)

# 시행령 별표 4 제3호 재산등급별 점수 (재산금액 만 원 '이하' 상한, 점수) — toejik-geonbo-2026-10/calc/calc.py 와 같은 표 (2026-10-14 PDF)
PROP_TABLE = [
    (450, 22), (900, 44), (1350, 66), (1800, 97), (2250, 122), (2700, 146), (3150, 171), (3600, 195), (4050, 219), (4500, 244),
    (5020, 268), (5590, 294), (6220, 320), (6930, 344), (7710, 365), (8590, 386), (9570, 412), (10700, 439), (11900, 465), (13300, 490),
    (14800, 516), (16400, 535), (18300, 559), (20400, 586), (22700, 611), (25300, 637), (28100, 659), (31300, 681), (34900, 706), (38800, 731),
    (43200, 757), (48100, 785), (53600, 812), (59700, 841), (66500, 881), (74000, 921), (82400, 961), (91800, 1001), (103000, 1041), (114000, 1091),
    (127000, 1141), (142000, 1191), (158000, 1241), (176000, 1291), (196000, 1341), (218000, 1391), (242000, 1451), (270000, 1511), (300000, 1571), (330000, 1641),
    (363000, 1711), (399300, 1781), (439230, 1851), (483153, 1921), (531468, 1991), (584615, 2061), (643077, 2131), (707385, 2201), (778124, 2271), (math.inf, 2341),
]

# ───────────────────────── 가정 ─────────────────────────
ASSET = 60000                      # 금융자산 6억 원 (만 원)
YIELD = 0.04                       # 이자·배당 연 4%
HOUSE_BASE = 30000                 # 집 과세표준 3억 원
YEARS = 3


def basic_tax(base):
    """종합소득 기본세율 산출세액 (만 원). base ≤ 0 이면 0."""
    if base <= 0:
        return 0.0
    tax, low = 0.0, 0.0
    for cap, r in BRACKETS:
        if base > low:
            tax += (min(base, cap) - low) * r
        low = cap
    return tax


def income_tax(fin, other=0.0, persons=1, gross_up_share=0.0):
    """한 사람 1년 소득세(만 원, 지방세 빼고). fin = 일반 계좌 이자·배당(제14조③6호 대상), other = 다른 종합소득금액.
    persons = 기본공제 인원(본인 1 + 소득 없는 배우자 1). gross_up_share = 이자·배당 중 배당가산 대상 비율(민감도).
    반환 (결정세액, 원천징수, 추가 납부, 1호, 2호, 종합과세 여부)."""
    withheld = fin * WH
    if fin <= FIN_LIMIT:                               # 분리과세로 끝 — 다른 소득만 기본세율
        add = basic_tax(other - persons * BASIC_DED) if other > 0 else 0.0
        return withheld + add, withheld, add, None, None, False
    # 배당가산: 기준금액을 넘는 몫 중 배당가산 대상 배당에만 (이자 → 가산 없는 배당 → 가산 배당 순으로 2천만 원을 채운다고 봄)
    over = fin - FIN_LIMIT
    gu_div = fin * gross_up_share
    gu_over = min(over, gu_div)
    gross = gu_over * GROSS_UP
    deduct = persons * BASIC_DED
    t1 = basic_tax(over + gross + other - deduct) + FIN_LIMIT * WH                 # 제62조 1호
    t2 = fin * WH + basic_tax(other - max(0.0, deduct - 0)) if other > 0 else fin * WH  # 제62조 2호 (다른 소득 없으면 이자·배당 × 14%)
    calc = max(t1, t2)
    div_credit = min(gross, max(0.0, t1 - t2))                                     # 배당세액공제 = 가산액, 1호−2호 한도 (제56조 ④)
    decided = calc - div_credit                                                    # 표준세액공제는 원천징수세율 몫에서 못 뺌 (제61조 ②)
    return decided, withheld, decided - withheld, t1, t2, True


def property_points(base_man):
    amt = base_man - PROPERTY_DEDUCT
    if amt <= 0:
        return 0
    for cap, pts in PROP_TABLE:
        if amt <= cap:
            return pts
    raise ValueError(base_man)


def kenbo_fin_income(fin_person):
    """건보료 소득으로 잡히는 한 사람의 이자·배당 (만 원): 1,000만 원 이하면 0, 넘으면 전부."""
    return 0.0 if fin_person <= FIN_CUT_KENBO else fin_person


def local_premium(fin_people, house=HOUSE_BASE, other_income=0.0):
    """지역가입자 세대 월 건보료 (원, 장기요양 제외). fin_people = 세대원별 일반 계좌 이자·배당 목록(만 원)."""
    inc_year = sum(kenbo_fin_income(f) for f in fin_people) + other_income
    inc_month_won = inc_year * 10_000 / 12
    inc_part = LOCAL_MIN if inc_month_won <= LOCAL_MIN_INCOME_MONTH else inc_month_won * RATE
    prop_part = property_points(house) * POINT_WON
    return inc_part + prop_part, inc_part, prop_part


def dependent_ok(fin_people, house=HOUSE_BASE):
    """피부양자 요건(소득·재산) — 부부 모두 소득 2천만 원 이하 + 재산 과표 5.4억 이하."""
    return all(kenbo_fin_income(f) <= DEP_INCOME_LIMIT for f in fin_people) and house <= DEP_PROP_LIMIT


def scenario(name, split, isa_year=0.0, pen_year=0.0, years=YEARS, yld=YIELD, house=HOUSE_BASE, has_child=True, asset=ASSET):
    """여러 해 시나리오. 반환: 해마다 (사람별 일반 계좌 이자·배당, 소득세+지방세, 월 건보료) 와 합계."""
    people = 2 if split else 1
    gen = [asset / people] * people                     # 일반 계좌 원금
    isa = [0.0] * people
    isa_gain = [0.0] * people
    pen = [0.0] * people
    pen_gain = [0.0] * people
    rows, tax_total, prem_total, defer_total = [], 0.0, 0.0, 0.0
    for y in range(1, years + 1):
        for i in range(people):                         # 1월에 옮김 (ISA 는 일반 계좌 원금에서, 연금저축도)
            mv_isa = min(isa_year, gen[i]) if isa_year else 0.0
            gen[i] -= mv_isa
            isa[i] += mv_isa
            mv_pen = min(pen_year, gen[i]) if pen_year else 0.0
            gen[i] -= mv_pen
            pen[i] += mv_pen
        fin = [g * yld for g in gen]                     # 일반 계좌 이자·배당 (생활비로 다 씀 → 원금 그대로)
        for i in range(people):
            g = (isa[i] + isa_gain[i]) * yld            # ISA 안 이익은 ISA 안에 쌓임
            isa_gain[i] += g
            pg = (pen[i] + pen_gain[i]) * yld
            pen_gain[i] += pg
        persons_ded = 2 if people == 1 else 1           # 한 사람 이름이면 소득 없는 배우자 기본공제
        tax = 0.0
        for f in fin:
            decided, *_ = income_tax(f, persons=persons_ded)
            tax += decided * LOCAL
        if y == years and isa_year:                     # 3년째 끝 ISA 해지
            for i in range(people):
                tax += max(0.0, isa_gain[i] - ISA_FREE) * ISA_TAX
        dep = has_child and dependent_ok(fin, house)
        prem, inc_part, prop_part = (0.0, 0.0, 0.0) if dep else local_premium(fin, house)
        prem_total += prem * 12 / 10_000                # 그해 소득 → 다음 해 11월부터 12개월 (만 원)
        tax_total += tax
        rows.append(dict(year=y, fin=[round(f, 1) for f in fin], tax=tax, dependent=dep, prem=prem, inc_part=inc_part, prop_part=prop_part))
        log("YEAR", scenario=name, year=y, fin="/".join(f"{f:.1f}" for f in fin), tax=round(tax, 1), dependent=dep, prem_month=round(prem))
    if pen_year:                                         # 연금저축 이익은 나중에 연금으로 받을 때 5.5% (B 에 불리하게 넣음)
        defer_total = sum(pen_gain) * PEN_TAX
    return dict(name=name, rows=rows, tax=tax_total, prem=prem_total, defer=defer_total, total=tax_total + prem_total + defer_total,
                isa_gain=isa_gain, pen_gain=pen_gain)


def breakeven(persons):
    """다른 소득이 없을 때, 이자·배당이 얼마를 넘어야 종합과세로 소득세가 늘기 시작하나 (만 원, 10만 원 단위)."""
    f = FIN_LIMIT
    while f < 30000:
        _, _, add, *_ = income_tax(f, persons=persons)
        if add > 0.05:
            return f
        f += 10
    return None


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--log-level", default="INFO")
    a = ap.parse_args()
    logging.basicConfig(stream=sys.stderr, level=getattr(logging, a.log_level.upper(), logging.INFO), format="%(message)s")
    log("START", version=VERSION, asset=ASSET, yield_=YIELD, house=HOUSE_BASE)
    P = print

    P(f"# geumyung-soduk-2026-10 calc {VERSION} — 단위: 만 원 (건보료 월액은 원)\n")
    fin_a = ASSET * YIELD
    P(f"## 1. 예시 부부 — 1년 이자·배당 {fin_a:,.0f}만 원 (6억 × {YIELD:.0%}, 월 {fin_a / 12:,.0f}만 원)")

    # 소득세
    dA, wA, addA, t1, t2, comp = income_tax(fin_a, persons=2)
    P(f"- A 한 사람 이름: 원천징수 {wA:,.1f} (+지방 {wA * 0.1:,.1f} = {wA * LOCAL:,.1f}) · 종합과세 {comp} · 제62조 1호 {t1:,.1f} vs 2호 {t2:,.1f} → 결정 {dA:,.1f} · 추가 납부 {addA:,.1f}")
    dB, wB, addB, *_ = income_tax(fin_a / 2, persons=1)
    P(f"- B0 부부로 나눔: 한 사람 {fin_a / 2:,.0f} → 분리과세, 세금 {dB * LOCAL:,.1f} × 2 = {2 * dB * LOCAL:,.1f}")
    P(f"- 다른 소득이 없으면 소득세가 늘기 시작하는 이자·배당: 본인+배우자 공제 {breakeven(2):,.0f} · 본인만 {breakeven(1):,.0f}")
    for share in (0.5, 1.0):
        d, w, add, t1g, t2g, _ = income_tax(fin_a, persons=2, gross_up_share=share)
        P(f"  · (민감도) 배당가산 대상 배당 {share:.0%}: 1호 {t1g:,.1f} vs 2호 {t2g:,.1f} → 추가 {add:,.1f}")
    f = FIN_LIMIT
    while f < 30000:
        _, _, add, *_ = income_tax(f, persons=2, gross_up_share=1.0)
        if add > 0.05:
            break
        f += 10
    P(f"  · (민감도) 전부 배당가산 대상 배당이면 소득세가 늘기 시작: {f:,.0f}")

    # 건보료
    premA, incA, propA = local_premium([fin_a])
    P(f"- A 건보료: 남편 소득 {kenbo_fin_income(fin_a):,.0f} > 피부양자 기준 {DEP_INCOME_LIMIT:,} → 부부 모두 탈락 → 지역 월 {premA:,.0f}원 (소득 {incA:,.0f} + 재산 {propA:,.0f} = {property_points(HOUSE_BASE)}점)"
      f" · 1년 {premA * 12 / 10_000:,.1f}만 · 장기요양 넣으면 월 {premA * (1 + LTC_RATIO):,.0f}원 · 1년 {premA * (1 + LTC_RATIO) * 12 / 10_000:,.1f}만")
    P(f"- B0 건보료: 한 사람 {fin_a / 2:,.0f} ≤ {DEP_INCOME_LIMIT:,} → 피부양자 {dependent_ok([fin_a / 2] * 2)} → 0원\n")

    # 3년 시나리오
    P("## 2. 3년 (이자·배당을 받는 해 3번 → 건보료는 다음 해 11월부터 36개월)")
    A = scenario("A", split=False)
    B0 = scenario("B0", split=True)
    B = scenario("B", split=True, isa_year=ISA_YEAR)
    Bp = scenario("B+", split=True, isa_year=ISA_YEAR, pen_year=PEN_YEAR)
    for s in (A, B0, B, Bp):
        yrs = " | ".join(f"{r['year']}년째 이자·배당 {'/'.join(f'{x:,.0f}' for x in r['fin'])} 세금 {r['tax']:,.1f} 건보 월 {r['prem']:,.0f}원" for r in s["rows"])
        P(f"- {s['name']}: 세금 {s['tax']:,.1f} + 건보료 {s['prem']:,.1f} + 나중 연금 세금 {s['defer']:,.1f} = **{s['total']:,.1f}**  ({yrs})")
    P(f"- 차이 A − B = {A['total'] - B['total']:,.1f} (건보료 {A['prem'] - B['prem']:,.1f} + 세금 {A['tax'] - B['tax']:,.1f}) · A − B0 = {A['total'] - B0['total']:,.1f} · A − B+ = {A['total'] - Bp['total']:,.1f}")
    P(f"- B 의 ISA 이익 (3년, 한 사람): {B['isa_gain'][0]:,.1f} → 해지 세금 {(B['isa_gain'][0] - ISA_FREE) * ISA_TAX:,.1f}")
    P(f"- B 첫해 세금 {B['rows'][0]['tax']:,.1f} vs A {A['rows'][0]['tax']:,.1f} (차이 {A['rows'][0]['tax'] - B['rows'][0]['tax']:,.1f})\n")

    # 이미 넘었다면
    P("## 3. 이미 올해 2,000만 원을 넘었다면")
    P(f"- 올해 소득 → 내년 11월부터 12개월 지역 보험료 {premA * 12 / 10_000:,.1f}만 (그 사이 내년 몫부터 나누면 그다음 해 11월에 다시 피부양자 신고)")
    P(f"- 3년 동안 고치지 않으면 건보료 {A['prem']:,.1f}만 → 바로 고치면 {premA * 12 / 10_000:,.1f}만 (줄어드는 몫 {A['prem'] - premA * 12 / 10_000:,.1f})")
    P(f"- 남편: 올해가 종합과세 대상이면 다음 3년 ISA 가입·연장 불가 (조특법 제129조의2) → 아내 이름 ISA")
    P(f"- 아내에게 옮길 3억 원 ≤ 배우자 증여 공제 {SPOUSE_GIFT_DED:,} → 증여세 0원 (신고)\n")

    # 지역가입자 (피부양자가 될 곳이 없을 때)
    P("## 4. 자녀가 직장인이 아니라 이미 지역가입자라면 (기준 = 한 사람 이자·배당 1,000만 원)")
    for s in (scenario("A-지역", split=False, has_child=False), scenario("B0-지역", split=True, has_child=False),
              scenario("B-지역", split=True, isa_year=ISA_YEAR, has_child=False), scenario("B+-지역", split=True, isa_year=ISA_YEAR, pen_year=PEN_YEAR, has_child=False)):
        P(f"- {s['name']}: " + " | ".join(f"{r['year']}년째 {'/'.join(f'{x:,.0f}' for x in r['fin'])} → 월 {r['prem']:,.0f}원 (소득 몫 {r['inc_part']:,.0f})" for r in s["rows"])
          + f" · 3년 건보료 {s['prem']:,.1f}만")
    P("")

    # 직장에 다니는 50대
    for fin in (2400,):
        extra = (fin - WORK_EXTRA_DED) * 10_000 / 12 * RATE
        P(f"## 5. 아직 직장인이면 — 월급 외 이자·배당 {fin:,} → 넘는 {fin - WORK_EXTRA_DED:,}만 원에 월 {extra:,.0f}원 따로 (법 제71조)\n")

    # 만기 때 한꺼번에 받는 이자
    lump = 10000 * 0.035 * 3
    P(f"## 6. 한 해에 몰리는 이자 — 1억 원을 3년 만기(연 3.5%, 단리)로 넣고 만기에 받으면 그해 이자 {lump:,.0f}만 원 (시행령 제45조 4호: 실제로 받는 날)\n")

    # 민감도
    P("## 7. 민감도 — A − B (3년, 만 원)")
    for yld in (0.03, 0.035, 0.04, 0.05):
        a_, b_ = scenario("A", False, yld=yld), scenario("B", True, isa_year=ISA_YEAR, yld=yld)
        P(f"- 수익률 {yld:.1%}: 1년 이자·배당 {ASSET * yld:,.0f} · A {a_['total']:,.1f} − B {b_['total']:,.1f} = {a_['total'] - b_['total']:,.1f} (A 피부양자 {a_['rows'][0]['dependent']})")
    for house in (20000, 30000, 40000):
        a_, b_ = scenario("A", False, house=house), scenario("B", True, isa_year=ISA_YEAR, house=house)
        pm, _, _ = local_premium([fin_a], house)
        P(f"- 집 과표 {house / 10000:.0f}억: A 월 {pm:,.0f}원 · A − B = {a_['total'] - b_['total']:,.1f}")
    P(f"- 장기요양 넣으면 A 3년 건보료 {A['prem'] * (1 + LTC_RATIO):,.1f} → A − B = {A['total'] + A['prem'] * LTC_RATIO - B['total']:,.1f}")
    for asset in (50000, 55000):
        a_ = scenario("A", False, asset=asset)
        P(f"- 금융자산 {asset / 10000:.1f}억 (1년 {asset * YIELD:,.0f}): A 피부양자 {a_['rows'][0]['dependent']} · 건보료 {a_['prem']:,.1f}")
    log("DONE", version=VERSION, A=round(A["total"], 1), B=round(B["total"], 1), diff=round(A["total"] - B["total"], 1))


if __name__ == "__main__":
    main()
