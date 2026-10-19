#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""VERSION: v1.1.1 — 2026-10-19 — 대본 v2.1(주인공이 알아 가는 이야기 — 동창 박 씨 = 2년 당김 경우)에 쓰는 월 차이 줄을 8번 절에 더함.
이전 v1.1 — 2026-10-19 — 대본 v2.0(사연형 — 기사 사례를 각색한 가상 인물 김 씨) 숫자를 8번 절에 더함.
         사용자 지시 2026-10-19 "기사 내용은 그냥 참고이고 현재 기준에 맞게 각색하면 돼 … 대본 알려줘봐".
         김 씨 = 1966년생(받는 나이 64세 — 부칙 <제8541호> 제8조 '1965년부터 1968년까지 출생자는 4세'), 59세 퇴직 후 바로 5년 당김,
         64세 예상 월 90만 원. 1~7번(예시 부부, v1.0)은 바꾸지 않음.
이전 v1.0 — 2026-10-18 — 최초 작성. 대본 gungmin-sigi-2026-10.txt v1.0 의 숫자를 모두 낸다.

국민연금 언제 받을까 — 1969년생 57세 남편의 국민연금을 60세(5년 당김)·65세(제때)·70세(5년 미룸)에 받을 때
받는 돈 합계, 합계가 같아지는 나이, 건보료 피부양자 기준, 일하면서 받을 때, 당겨 받다 멈출 때, 아내의 추납 (단위: 원)

근거 (GitHub legalize-kr 에서 2026-10-18 시행 중인 판 — tools/law_text.py v1.1 --source mirror, law.go.kr 은 이 클라우드에서 막힘):
- 국민연금법 [시행 2026-05-26] [법률 제21689호] (legalize-kr 7db6bb741c)
  제61조①(가입기간 10년 이상 → 노령연금)·②(조기노령연금: 소득이 있는 업무에 종사하지 않으면 5년 전부터 청구),
  제62조①(연기: 전부 또는 일부)·②(연기 1개월마다 1천분의 6 가산)·③(일부 연기 50~90%),
  제63조②(조기: 5년 전 1천분의 700, 1년마다 1천분의 60 = 1개월마다 1천분의 5),
  제63조의2(소득활동 감액 — 2025.12.16 개정: 초과소득월액 200만 원 미만 구간 삭제, 공포 후 6개월 시행, 2025년 1월 1일 이후 소득부터),
  제66조①②③(조기노령연금 지급 정지·재지급: 재수급 당시 비율에서 기수급 1개월마다 1천분의 5를 뺌),
  제77조①1(10년 미만 → 60세에 반환일시금), 제92조①③④(추납: 10년 미만 범위, 납부 기한 달 보험료 × 개월 수, 분할),
  부칙 <제8541호> 제8조(1969년 이후 출생 지급연령 + 5세), 부칙 <제11143호> 제6조·<제13100호> 제4조(연기 연령 + 5세),
  부칙 <제20903호> 제4조②(지역·임의가입자 보험료율 2026년 1천분의 95, 해마다 1천분의 5씩 올라 2033년 1천분의 130)
- 국민연금법 시행령 [시행 2025-12-16] [대통령령 제35909호] (legalize-kr 39b62d3952): 제45조①(소득이 있는 업무 = 근로·사업소득 금액 월평균이
  법 제51조①1호 금액(A값) 초과), 제62조③(추납 60회 분할)
- 국민건강보험법 시행령 [시행 2026-10-01] [대통령령 제36675호] (legalize-kr 4cc370eb35) 제41조①5호(공적연금소득은 전부 소득)
- 국민건강보험법 시행규칙 별표 1의2 (피부양자 소득 연 2천만 원 이하, 기혼자는 부부 모두) · 제44조②(지역 소득월액: 연금소득 100분의 50)
  · 시행령 제44조(보험료율 7.19%) · 노인장기요양보험법 시행령 제4조(0.9448%) — economic/source/toejik-geonbo-2026-10/checklist.md 에서
  2026-10-14 law.go.kr 원문으로 확인한 것을 그대로 씀

가정 (사실이 아니라 계산용 예시 — README 3번 표와 같음):
- 1969년생 동갑 부부, 2026년 만 57세. 남편은 회사원, 60세 정년 퇴직 예정. 65세(수급 개시)부터 받을 국민연금 예상 월 130만 원
  (지금 돈 가치 — 공단 '내 연금 알아보기' 예상액이라고 가정, 부양가족연금 제외)
- 연금은 해마다 물가만큼 오르므로(법 제51조②) 모든 금액을 지금 돈 가치로 계산 — 기본은 가입자 평균 소득(A값)도 물가만큼 오른다고 봄
  (A값이 물가보다 빨리 오르면 당겨 받는 쪽이 더 불리 → 민감도 S1)
- 이자·할인율 0 (기본). 받은 연금을 불린다고 보면 → 민감도 S2
- 세금(연금소득세)은 넣지 않음. 건보료는 '원칙 셋'에서 소득 몫만 따로 셈 (재산 몫은 사람마다 달라 넣지 않음)
- 아내: 결혼 전 7년(84개월) 가입, 그 뒤 소득 없음(무소득 배우자 — 법 제9조1호 적용 제외 기간) → 60세 전에 10년이 안 됨.
  추납 기준소득월액은 월 100만 원으로 가정 (임의가입자 최저 금액은 확인 필요 — checklist C)
- A값(가입자 평균 소득) 2026년 3,193,511원 — 영상 설명·댓글로만 확인 (공식 고시 확인 필요 — checklist C)

실행: python3 calc.py          (대본 숫자)
      python3 calc.py -v       (민감도 표까지)
로그: [STAGE] 시각 key=value (stderr). 연구·교육용 — 연금 상담·법률 자문 아님.
"""
import logging
import sys
import time

VERSION = "v1.1.1"
LOG = logging.getLogger("gungmin_calc")

# ---------- 제도 값 ----------
NORMAL_AGE = 65                 # 1969년 이후 출생 노령연금 지급연령 (법 제61조① 60세 + 부칙 제8조 5세)
EARLY_MIN_AGE = 60              # 조기노령연금 (법 제61조② 55세 + 5세)
DEFER_MAX_AGE = 70              # 연기 끝 (법 제62조① 65세 + 부칙 제6조 5세)
EARLY_CUT_PER_MONTH = 0.005     # 조기: 1개월마다 1천분의 5 (법 제63조② — 1년 1천분의 60, 5년 1천분의 700)
DEFER_ADD_PER_MONTH = 0.006     # 연기: 1개월마다 1천분의 6 (법 제62조②)
DEFER_PARTIAL = (0.5, 0.6, 0.7, 0.8, 0.9)   # 일부 연기 (법 제62조③)
DEP_LIMIT = 20_000_000          # 피부양자 소득 연 2천만 원 이하 (시행규칙 별표 1의2 제1호 가목), 공적연금 전부 (시행령 제41조①5호)
HI_RATE = 0.0719                # 건강보험료율 (시행령 제44조, 2026)
LOCAL_PENSION_SHARE = 0.5       # 지역 소득월액에 연금소득 반영 비율 (시행규칙 제44조②2호)
LTC_RATIO = round(0.9448 / 7.19, 4)   # 장기요양 = 건보료 × 0.1314 (노인장기요양보험법 시행령 제4조)
A_VALUE_2026 = 3_193_511        # A값 2026 — ⚠️ 영상 설명·댓글로만 확인 (checklist C 1)
WORK_BRACKETS = [               # 법 제63조의2 (2025.12.16 개정 뒤): 초과소득월액 구간 → (하한, 기본 감액, 비율)
    (2_000_000, 150_000, 0.15),
    (3_000_000, 300_000, 0.20),
    (4_000_000, 500_000, 0.25),
]
WORK_BRACKETS_OLD = [           # 개정 전 (2025.11.25 판) — 비교용
    (0, 0, 0.05),
    (1_000_000, 50_000, 0.10),
    (2_000_000, 150_000, 0.15),
    (3_000_000, 300_000, 0.20),
    (4_000_000, 500_000, 0.25),
]
VOL_RATE = {2026: 0.095, 2027: 0.100, 2028: 0.105, 2029: 0.110, 2030: 0.115, 2031: 0.120, 2032: 0.125, 2033: 0.130}  # 부칙 제4조② · 제88조④
MIN_YEARS_MONTHS = 120          # 가입기간 10년 (법 제61조①)

# ---------- 예시 (가정) ----------
P65 = 1_300_000                 # 남편 65세 예상 월 노령연금 (지금 가치)
WIFE_MONTHS = 84                # 아내 가입 7년
WIFE_BASE_INCOME = 1_000_000    # 추납 기준소득월액 (가정)

# ---------- 대본 v2.0 각색 사례 (가정 — 기사 사례를 바탕으로 지금 법에 맞게 각색한 가상 인물) ----------
KIM_NORMAL_AGE = 64             # 1965~1968년생 노령연금 지급연령 (본칙 60세 + 부칙 <제8541호> 제8조 4세)
KIM_EARLY_AGE = 59              # 5년 당김 (제61조② 5년 전부터 — 같은 부칙으로 55 + 4)
KIM_P = 900_000                 # 64세부터 받을 예상 월 노령연금 (지금 돈 가치, 부양가족연금 제외)
KIM_ALT_AGE = 62                # '3년만 버텼다면' — 2년만 당김
KIM_STOP_AFTER = 12             # 59세부터 12개월 받고 60세에 지급 정지 신청 (제66조①2·②1·③1)
LOCAL_MIN_HI = 20_160           # 지역 소득월액 28만 원 이하 → 월 보험료 하한 (시행규칙 제44조③ 단서 · 상한·하한 고시 제3조 2호 — toejik 확인표 A 46)
LOCAL_MIN_INCOME_MONTH = 280_000


def log(stage, **kv):
    LOG.info("[%s] %s %s", stage, time.strftime("%Y-%m-%dT%H:%M:%S"), " ".join(f"{k}={v}" for k, v in kv.items()))


def man(won):
    """원 → '1,234.5만' 같은 만 원 표기."""
    v = won / 10_000
    return f"{v:,.1f}만" if abs(v - round(v)) > 1e-9 else f"{v:,.0f}만"


def age_str(months_from_birth):
    y, m = divmod(round(months_from_birth), 12)
    return f"{y}세 {m}개월"


def early_ratio(months_early):
    """조기노령연금 비율 (부양가족연금 제외): 1 − 0.005 × 당긴 개월 수 (5년 = 0.70)."""
    return 1 - EARLY_CUT_PER_MONTH * months_early


def defer_ratio(months_deferred):
    """연기 가산 비율: 1 + 0.006 × 미룬 개월 수 (5년 = 1.36)."""
    return 1 + DEFER_ADD_PER_MONTH * months_deferred


def cumulative(monthly, start_age, end_age, real_disc=0.0):
    """start_age 부터 end_age 까지 받은 연금 합계 (월 단위, 할인율 real_disc 이면 57세 기준 현재가치)."""
    total = 0.0
    m0 = round(start_age * 12)
    m1 = round(end_age * 12)
    for m in range(m0, m1):
        total += monthly / ((1 + real_disc) ** ((m - 57 * 12) / 12))
    return total


def breakeven(a_monthly, a_start, b_monthly, b_start, real_disc=0.0, horizon=110):
    """a(먼저 받기 시작)와 b 의 합계가 같아지는(b가 앞서는) 나이 (개월 단위). 없으면 None."""
    ca = cb = 0.0
    for m in range(round(a_start * 12), horizon * 12):
        d = (1 + real_disc) ** ((m - 57 * 12) / 12)
        ca += a_monthly / d
        if m >= round(b_start * 12):
            cb += b_monthly / d
        if cb >= ca and m >= round(b_start * 12):
            return m + 1
    return None


def breakeven_exact(r_a, start_a, r_b, start_b):
    """할인 없는 연속 근사: r_a(t − start_a) = r_b(t − start_b) 의 t."""
    return (r_b * start_b - r_a * start_a) / (r_b - r_a)


def work_cut(excess, brackets=WORK_BRACKETS, pension=None):
    """법 제63조의2 감액 (월). excess = 초과소득월액 (소득월액 − A값). 감액은 노령연금의 1/2 까지."""
    cut = 0.0
    for lo, base, rate in brackets:
        if excess >= lo:
            cut = base + (excess - lo) * rate
    if pension is not None:
        cut = min(cut, pension / 2)
    return max(cut, 0.0)


def local_hi_income_part(annual_pension):
    """지역가입자 건보료 중 소득 몫 (월, 장기요양 포함). 소득월액 = 연금 × 50% ÷ 12, 보험료 10원 미만 버림."""
    inc_month = annual_pension * LOCAL_PENSION_SHARE / 12
    hi = int(inc_month * HI_RATE // 10 * 10)
    ltc = int(hi * LTC_RATIO // 10 * 10)
    return inc_month, hi, ltc, hi + ltc


def main(verbose=False):
    logging.basicConfig(level=logging.INFO, stream=sys.stderr, format="%(message)s")
    log("START", version=VERSION, P65=P65)
    out = []
    P = out.append

    # 1. 세 가지 선택의 월 연금
    a = P65 * early_ratio(60)          # 60세 (5년 당김)
    b = P65                            # 65세
    c = P65 * defer_ratio(60)          # 70세 (5년 미룸)
    log("MONTHLY", early60=round(a), normal65=b, defer70=round(c))
    P("## 1. 세 가지 선택 — 남편의 월 국민연금 (지금 돈 가치)")
    P(f"- A 60세부터 (5년 당김, 비율 {early_ratio(60):.2f}): 월 **{man(a)} 원** — 65세보다 월 {man(b - a)} 원 덜 받음 (1년 {man((b - a) * 12)} 원)")
    P(f"- B 65세부터 (제때): 월 **{man(b)} 원**")
    P(f"- C 70세부터 (5년 미룸, 비율 {defer_ratio(60):.2f}): 월 **{man(c)} 원** — 65세보다 월 {man(c - b)} 원 더 받음")
    P(f"- 1년 당김 = {(1 - early_ratio(12)) * 100:.0f}% 덜, 1년 미룸 = {(defer_ratio(12) - 1) * 100:.1f}% 더")
    P(f"- A 가 65세 전 5년 동안 먼저 받는 돈: {man(a)} × 60개월 = **{man(a * 60)} 원**")

    # 2. 합계가 같아지는 나이
    be_ab = breakeven(a, 60, b, 65)
    be_bc = breakeven(b, 65, c, 70)
    be_ac = breakeven(a, 60, c, 70)
    ex_ab = breakeven_exact(early_ratio(60), 60, 1.0, 65)
    ex_bc = breakeven_exact(1.0, 65, defer_ratio(60), 70)
    log("BREAKEVEN", AB=age_str(be_ab), BC=age_str(be_bc), AC=age_str(be_ac), AB_exact=round(ex_ab, 2), BC_exact=round(ex_bc, 2))
    P("\n## 2. 받는 돈 합계가 같아지는 나이 (할인 없음, 지금 돈 가치)")
    P(f"- A(60세) vs B(65세): **{age_str(be_ab)}** (연속 근사 {ex_ab:.2f}세) → 대본 '약 77세' — 그 뒤로 오래 살수록 B가 더 받음")
    P(f"- B(65세) vs C(70세): **{age_str(be_bc)}** (연속 근사 {ex_bc:.2f}세) → 대본 '약 84세'")
    P(f"- A(60세) vs C(70세): {age_str(be_ac)}")
    P("- 당긴 해 수 k 에 따라 (A값 물가만큼): 같아지는 나이 = 81.7 − k 세")
    for k in range(1, 6):
        r = early_ratio(12 * k)
        be = breakeven(P65 * r, 65 - k, b, 65)
        P(f"  - {k}년 당김 ({65 - k}세부터, {r * 100:.0f}% = 월 {man(P65 * r)} 원): {age_str(be)}")
    P("- 미룬 해 수 k: 같아지는 나이 = 78.9 + k 세")
    for k in range(1, 6):
        r = defer_ratio(12 * k)
        be = breakeven(b, 65, P65 * r, 65 + k)
        P(f"  - {k}년 미룸 ({65 + k}세부터, {r * 100:.1f}% = 월 {man(P65 * r)} 원): {age_str(be)}")

    # 3. 몇 살까지 받으면 합계가 얼마
    P("\n## 3. 몇 살까지 받으면 — 합계 (지금 돈 가치)")
    P("| 나이 | A 60세 | B 65세 | C 70세 | B − A | C − B |")
    P("|---|---|---|---|---|---|")
    totals = {}
    for end in (65, 70, 75, 77, 80, 84, 85, 90, 95):
        ta = cumulative(a, 60, end)
        tb = cumulative(b, 65, end) if end > 65 else 0
        tc = cumulative(c, 70, end) if end > 70 else 0
        totals[end] = (ta, tb, tc)
        P(f"| {end}세 | {man(ta)} | {man(tb)} | {man(tc)} | {man(tb - ta)} | {man(tc - tb)} |")
    log("TOTALS", at75=[round(x) for x in totals[75]], at90=[round(x) for x in totals[90]])

    # 4. 원칙 둘 — 일하면서
    P("\n## 4. 일하면서 받으면 (A값 2026 = 3,193,511원 ⚠️)")
    P(f"- 조기노령연금: 근로·사업소득 금액(근로소득공제·필요경비 뒤) 월평균이 A값 {man(A_VALUE_2026)} 원을 넘으면 청구 못 함 / 받던 중이면 그 기간 지급 정지 (법 제61조②·제66조①1, 시행령 제45조①)")
    lim = A_VALUE_2026 + 2_000_000
    P(f"- 노령연금(65세부터 5년): 초과소득월액 200만 원 미만이면 감액 없음 → 소득 금액 월 **{man(lim)} 원** 미만이면 그대로 (2026년 6월 시행, 2025년 소득부터)")
    for inc in (3_000_000, 4_500_000, 5_000_000, 5_500_000, 6_500_000):
        ex = max(inc - A_VALUE_2026, 0)
        new = work_cut(ex, WORK_BRACKETS, b)
        old = work_cut(ex, WORK_BRACKETS_OLD, b) if ex > 0 else 0
        P(f"  - 소득 금액 월 {man(inc)}: 초과 {man(ex)} → 감액 지금 {man(new)} 원 (개정 전 {man(old)} 원)")
    # 근로소득 금액 계산 예 (총급여 → 근로소득공제, 소득세법 제47조) — 대본 숫자 아님, 감 잡기용
    def wage_income(gross_year):
        g = gross_year
        if g <= 5_000_000:
            d = g * 0.7
        elif g <= 15_000_000:
            d = 3_500_000 + (g - 5_000_000) * 0.4
        elif g <= 45_000_000:
            d = 7_500_000 + (g - 15_000_000) * 0.15
        elif g <= 100_000_000:
            d = 12_000_000 + (g - 45_000_000) * 0.05
        else:
            d = 14_750_000 + (g - 100_000_000) * 0.02
        return g - min(d, 20_000_000)
    for gm in (3_000_000, 4_000_000, 4_500_000, 6_000_000):
        wi = wage_income(gm * 12) / 12
        P(f"  - (참고) 월급 {man(gm)} → 근로소득 금액 월 {man(round(wi))} — A값 초과 {'예' if wi > A_VALUE_2026 else '아니오'}")

    # 5. 원칙 셋 — 건보료 피부양자
    P("\n## 5. 건보료 피부양자 소득 기준 연 2,000만 원 (공적연금 전부, 부부 모두)")
    for name, mon in (("A 60세", a), ("B 65세", b), ("C 70세", c)):
        yr = mon * 12
        P(f"- {name}: 연 {man(yr)} 원 → {'넘음 ❌ (부부 모두 피부양자에서 빠짐)' if yr > DEP_LIMIT else '기준 안 ✅'}")
    max_m = max(m for m in range(0, 61) if P65 * defer_ratio(m) * 12 <= DEP_LIMIT)
    P(f"- 전부 미룰 때 기준 안: **{max_m}개월**까지 (월 {man(P65 * defer_ratio(max_m))} 원, 연 {man(P65 * defer_ratio(max_m) * 12)} 원) · 4년(48개월) = 연 {man(P65 * defer_ratio(48) * 12)} 원")
    for share in DEFER_PARTIAL:
        mon = P65 * (1 - share) + P65 * share * defer_ratio(60)
        P(f"- 일부 {int(share * 100)}% 미룸 → 65~69세 월 {man(P65 * (1 - share))} 원, 70세부터 월 {man(mon)} 원 (연 {man(mon * 12)} 원) {'✅' if mon * 12 <= DEP_LIMIT else '❌'}")
    inc_m, hi, ltc, tot = local_hi_income_part(c * 12)
    log("LOCAL_HI", income_month=round(inc_m), hi=hi, ltc=ltc, total=tot)
    P(f"- C 가 피부양자에서 빠지면 지역 건보료 소득 몫: 연금 연 {man(c * 12)} × 50% ÷ 12 = 소득월액 {man(round(inc_m))} 원 × 7.19% = {hi:,}원 + 장기요양 {ltc:,}원 = **월 {tot:,}원** (재산 몫 빼고)")
    be_bc_hi = breakeven(b, 65, c - tot, 70)
    P(f"- 건보료 소득 몫을 뺀 C(월 {man(c - tot)}) vs B: 같아지는 나이 **{age_str(be_bc_hi)}** (건보료 없을 때 {age_str(be_bc)})")
    # 물가: 기준은 고정 금액
    for infl in (0.02,):
        for year, label, mon_real in ((2034, "65세 B", b), (2039, "70세 B", b), (2039, "70세 C", c)):
            nom = mon_real * (1 + infl) ** (year - 2026)
            P(f"- (물가 연 {infl * 100:.0f}% 가정) {year}년 {label}: 명목 월 {man(round(nom))} 원 = 연 {man(round(nom * 12))} 원 {'❌ 2,000만 넘음' if nom * 12 > DEP_LIMIT else '✅'} — 기준 2,000만 원은 고정 금액")

    # 6. 이미 당겨 받는다면 — 지급 정지 (법 제66조)
    P("\n## 6. 당겨 받다가 65세 전에 멈추면 (법 제66조① 2호·③)")
    for got in (12, 24, 36):
        r = 1 - EARLY_CUT_PER_MONTH * got
        P(f"- 60세부터 {got}개월 받고 멈춤 → 65세부터 비율 {r:.2f} → 월 **{man(P65 * r)} 원** (그대로 두면 {man(a)} 원)")
    r12 = 1 - EARLY_CUT_PER_MONTH * 12
    be_stop = breakeven(a, 61, P65 * r12, 65)  # 61세부터 계속 받는 것 vs 61~65 멈추고 65부터 94%
    P(f"- 1년 받고 멈춤 vs 계속 받음: 61~65세 못 받는 돈 {man(a * 48)} 원, 65세부터 월 {man(P65 * r12 - a)} 원 더 → 같아지는 나이 {age_str(be_stop)}")

    # 7. 아내 — 가입 기간 10년과 추납
    need = MIN_YEARS_MONTHS - WIFE_MONTHS
    P("\n## 7. 아내 — 10년(120개월) 채우기")
    P(f"- 가입 {WIFE_MONTHS}개월 → 모자란 {need}개월 ({need // 12}년). 못 채우면 60세에 낸 보험료 + 이자를 한 번에 돌려받고 끝 (법 제77조①1)")
    for yr in (2026, 2027, 2028):
        cost = WIFE_BASE_INCOME * VOL_RATE[yr] * need
        P(f"- {yr}년에 추납 ({need}개월, 기준소득월액 {man(WIFE_BASE_INCOME)} × {VOL_RATE[yr] * 100:.1f}%): **{man(cost)} 원** · 한 달치 {man(WIFE_BASE_INCOME * VOL_RATE[yr])} 원")
    c26 = WIFE_BASE_INCOME * VOL_RATE[2026] * need
    c27 = WIFE_BASE_INCOME * VOL_RATE[2027] * need
    P(f"- 내년(2027)이면 {man(c27 - c26)} 원 더 ({(c27 / c26 - 1) * 100:.1f}%) — 보험료율이 해마다 0.5%포인트씩 오름 (2033년 13%)")
    P(f"- 60회 분할 가능 (시행령 제62조③, 이자 더함) · 임의가입자 추납 한 달치 상한 = A값 × 그해 비율 = {man(round(A_VALUE_2026 * VOL_RATE[2026]))} 원 (2026)")
    log("CHUNAP", need=need, cost2026=round(c26), cost2027=round(c27))

    # 8. 대본 v2.0 — 각색 사례 김 씨 (1966년생, 받는 나이 64세, 59세에 5년 당김)
    ke = KIM_P * early_ratio(60)
    kn = KIM_P
    P("\n## 8. 대본 v2.0 각색 사례 — 김 씨 (1966년생 · 받는 나이 64세 · 59세에 5년 당김 · 64세 예상 월 90만 원)")
    P(f"- 월 연금: 5년 당김 비율 {early_ratio(60):.2f} → 월 **{man(ke)} 원** (64세부터였다면 {man(kn)} 원) — 매달 **{man(kn - ke)} 원** 덜 받음")
    P(f"- 김 씨의 계산: 64세부터 84세까지 20년 × 월 {man(kn - ke)} 원 = **{man((kn - ke) * 12 * 20)} 원**")
    P(f"- 빠진 돈: 59~64세 5년 먼저 받은 돈 {man(ke)} × 60개월 = **{man(ke * 60)} 원**")
    months_to_eat = ke * 60 / (kn - ke)
    P(f"- 먼저 받은 돈을 매달 {man(kn - ke)} 원씩 다 까먹는 데: {months_to_eat:.0f}개월 = **{int(months_to_eat // 12)}년 {round(months_to_eat % 12)}개월**")
    be_k = breakeven(ke, KIM_EARLY_AGE, kn, KIM_NORMAL_AGE)
    P(f"- 합계가 같아지는 나이: **{age_str(be_k)}** (받기 시작하고 {age_str(be_k - KIM_EARLY_AGE * 12).replace('세', '년')}) — 당긴 해 수·금액과 상관없이 '받기 시작하고 16년 8개월'")
    for k in (1, 2, 3, 4, 5):
        bek = breakeven(KIM_P * early_ratio(12 * k), KIM_NORMAL_AGE - k, kn, KIM_NORMAL_AGE)
        P(f"  - {k}년 당김: {age_str(bek)} = 받기 시작하고 {age_str(bek - (KIM_NORMAL_AGE - k) * 12).replace('세', '년')}")
    P("| 몇 살까지 | 5년 당김(59세) | 제때(64세) | 차이 (제때 − 당김) |")
    P("|---|---|---|---|")
    kt = {}
    for end in (64, 70, 75, 80, 84, 85, 90):
        ta = cumulative(ke, KIM_EARLY_AGE, end)
        tb = cumulative(kn, KIM_NORMAL_AGE, end) if end > KIM_NORMAL_AGE else 0
        kt[end] = (ta, tb)
        P(f"| {end}세 | {man(ta)} | {man(tb)} | {man(tb - ta)} {'(당김이 이득)' if tb < ta else '(당김이 손해)'} |")
    log("KIM_TOTALS", be=age_str(be_k), d75=round(kt[75][1] - kt[75][0]), d84=round(kt[84][1] - kt[84][0]), d80=round(kt[80][1] - kt[80][0]), d85=round(kt[85][1] - kt[85][0]), d90=round(kt[90][1] - kt[90][0]))
    # 3년만 버텼다면 — 62세에 2년만 당김
    ka = KIM_P * early_ratio(12 * (KIM_NORMAL_AGE - KIM_ALT_AGE))
    bridge = ke * 12 * (KIM_ALT_AGE - KIM_EARLY_AGE)
    P(f"- 3년만 버텼다면 (대본 v2.1 동창 박 씨): {KIM_ALT_AGE}세에 2년만 당김, 비율 {early_ratio(24):.2f} → 월 **{man(ka)} 원** — 김 씨(5년 당김)보다 매달 **{man(ka - ke)} 원** 더")
    P(f"  - 59~62세 3년을 5년 당겼을 때의 월 {man(ke)} 원만큼 모아 둔 돈으로 메우면: {man(ke)} × 36개월 = **{man(bridge)} 원** (생활비는 두 경우 같게 맞춤)")
    be_alt = breakeven(ke, KIM_EARLY_AGE, ka, KIM_ALT_AGE)
    P(f"  - 5년 당김 vs 2년 당김 합계가 같아지는 나이: **{age_str(be_alt)}**")
    for end in (75, 80, 85, 90):
        t5 = cumulative(ke, KIM_EARLY_AGE, end)
        t2 = cumulative(ka, KIM_ALT_AGE, end)
        P(f"  - {end}세까지: 2년 당김 {man(t2)} vs 5년 당김 {man(t5)} → 2년 당김이 **{man(t2 - t5)} 원** {'더' if t2 > t5 else '덜'} (메운 돈은 생활비가 같아 비교에서 빠짐)")
    log("KIM_ALT", alt_month=round(ka), bridge=round(bridge), be=age_str(be_alt), d85=round(cumulative(ka, KIM_ALT_AGE, 85) - cumulative(ke, KIM_EARLY_AGE, 85)))
    # 이미 신청했다면 — 60세에 지급 정지 (제66조)
    rs = 1 - EARLY_CUT_PER_MONTH * KIM_STOP_AFTER
    ks = KIM_P * rs
    lost = ke * 12 * (KIM_NORMAL_AGE - KIM_EARLY_AGE - KIM_STOP_AFTER / 12)
    P(f"- 60세에 지급 정지(12개월 받고): 64세에 다시, 비율 {rs:.2f} → 월 **{man(ks)} 원** (계속 받으면 {man(ke)} 원 — 매달 {man(ks - ke)} 원 더)")
    P(f"  - 멈춘 60~64세 4년에 못 받는 돈: {man(ke)} × 48개월 = {man(lost)} 원 → 매달 {man(ks - ke)} 원씩 메우는 데 {lost / (ks - ke):.0f}개월 = {int(lost / (ks - ke) // 12)}년 {round(lost / (ks - ke) % 12)}개월")
    cont = lambda end: cumulative(ke, KIM_EARLY_AGE, end)
    stop = lambda end: cumulative(ke, KIM_EARLY_AGE, KIM_EARLY_AGE + KIM_STOP_AFTER / 12) + (cumulative(ks, KIM_NORMAL_AGE, end) if end > KIM_NORMAL_AGE else 0)
    be_stop = next(m for m in range(KIM_NORMAL_AGE * 12, 110 * 12) if stop(m / 12) >= cont(m / 12))
    P(f"  - 멈춤 vs 계속 받음 합계가 같아지는 나이: **{age_str(be_stop)}**")
    for end in (80, 85, 90):
        P(f"  - {end}세까지: 멈춤 {man(stop(end))} vs 계속 {man(cont(end))} → 멈춤이 {man(stop(end) - cont(end))} 원 {'더' if stop(end) > cont(end) else '덜'}")
    log("KIM_STOP", ratio=rs, month=round(ks), be=age_str(be_stop))
    # 건보료 — 연금이 늘린 지역 건보료 소득 몫 (재산 몫은 당기든 미루든 같음)
    yr = ke * 12
    inc_m, hi, ltc, tot = local_hi_income_part(yr)
    if inc_m <= LOCAL_MIN_INCOME_MONTH:
        hi = LOCAL_MIN_HI
        ltc = int(hi * LTC_RATIO // 10 * 10)
        tot = hi + ltc
    base_hi = LOCAL_MIN_HI
    base_ltc = int(base_hi * LTC_RATIO // 10 * 10)
    P(f"- 건보료(지역가입자, 소득 몫만): 연금 연 {man(yr)} 원 × 50% = {man(yr * LOCAL_PENSION_SHARE)} 원 → 소득월액 {man(round(inc_m))} 원 (28만 원 초과)")
    P(f"  - 연금 없을 때: 하한 {base_hi:,}원 + 장기요양 {base_ltc:,}원 = {base_hi + base_ltc:,}원 → 연금 받은 뒤: {hi:,}원 + {ltc:,}원 = {tot:,}원 → 늘어난 돈 **월 {tot - base_hi - base_ltc:,}원**")
    P(f"  - 피부양자 소득 기준 연 2,000만 원 vs 김 씨 연금 연 {man(yr)} 원 → {'기준 안 ✅ (자녀 피부양자라면 0원 그대로)' if yr <= DEP_LIMIT else '넘음 ❌'}")
    log("KIM_HI", income_month=round(inc_m), before=base_hi + base_ltc, after=tot, diff=tot - base_hi - base_ltc)

    if verbose:
        P("\n## S1. 민감도 — A값(가입자 평균 소득)이 물가보다 해마다 g 만큼 빨리 오르면 (당겨 받으면 그만큼 덜 반영)")
        P("| g | 60세 연금 ÷ 65세 연금 | 같아지는 나이 A vs B |")
        P("|---|---|---|")
        for g in (0.0, 0.005, 0.01, 0.015, 0.02):
            ra = early_ratio(60) / (1 + g) ** 5
            be = breakeven(P65 * ra, 60, b, 65)
            P(f"| {g * 100:.1f}%p | {ra:.3f} | {age_str(be)} |")
            log("SENS_WAGE", g=g, ratio=round(ra, 4), be=age_str(be))
        P("- 미루기(B vs C)는 65세에 정한 금액에 물가만 더하므로(법 제62조②) g 와 상관없이 같음")
        P("\n## S2. 민감도 — 받은 연금을 해마다 실질 r 로 불린다고 보면 (현재가치로 비교)")
        P("| r | A vs B | B vs C |")
        P("|---|---|---|")
        for r in (0.0, 0.01, 0.02, 0.03):
            e1 = breakeven(a, 60, b, 65, r)
            e2 = breakeven(b, 65, c, 70, r)
            P(f"| {r * 100:.0f}% | {age_str(e1) if e1 else '없음'} | {age_str(e2) if e2 else '없음'} |")
            log("SENS_DISC", r=r, AB=age_str(e1) if e1 else None, BC=age_str(e2) if e2 else None)
        P("\n## S3. 민감도 — 65세 예상 연금이 달라도 같아지는 나이는 같음 (비율로만 정해짐)")
        for p in (800_000, 1_000_000, 1_300_000, 1_600_000):
            e1 = breakeven(p * early_ratio(60), 60, p, 65)
            e2 = breakeven(p, 65, p * defer_ratio(60), 70)
            P(f"- 65세 월 {man(p)}: A vs B {age_str(e1)} · B vs C {age_str(e2)} · 70세 연 {man(p * defer_ratio(60) * 12)} {'❌' if p * defer_ratio(60) * 12 > DEP_LIMIT else '✅'}")
    log("END", lines=len(out))
    print("\n".join(out))


if __name__ == "__main__":
    main(verbose="-v" in sys.argv[1:])
