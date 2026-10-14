#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""VERSION: v1.0 — 2026-10-14 — 최초 작성. 대본 toejik-geonbo-2026-10.txt v1.0 의 숫자를 모두 이 코드로 낸다.

퇴직 직후 건보료 세 갈래 — ① 자녀(직장가입자)의 피부양자 ② 임의계속가입 ③ 지역가입자 — 한 달 보험료와 36개월 합계.
실행:  cd economic/source/toejik-geonbo-2026-10/calc && python3 calc.py        (로그는 stderr, 결과 표는 stdout)

근거 (law.go.kr 현행 원문, 2026-10-14 받음 — 자세히는 ../checklist.md):
  - 건강보험료율 1만분의 719 = 7.19%, 재산보험료부과점수당 211.5원 : 국민건강보험법 시행령 제44조 (2026.1.1 시행분)
  - 지역 재산 점수 = (재산세 과세표준 − 1억 원) 등급표 : 시행령 별표 4 (개정 2024.5.7)
  - 지역 소득월액: 근로·연금소득은 50%, 소득월액 28만 원 이하이면 하한 보험료로 : 시행규칙 제44조 ②·③
  - 지역 소득 자료 시기: 1~10월분은 전전년도, 11·12월분은 전년도 (연금소득은 전년도) : 시행령 제41조 ③
  - 월별 보험료 하한 20,160원(지역) : 「월별 건강보험료액의 상한과 하한에 관한 고시」 제3조 (2026.1.1 시행)
  - 임의계속가입자 보수월액 = 최근 12개월 평균, 전액 본인 부담 : 법 제110조 ③·⑤ / 보수월액보험료의 50% 경감 : 「보험료 경감고시」 제9조
  - 장기요양보험료율 100만분의 9,448 : 노인장기요양보험법 시행령 제4조 (건보료 대비 0.9448/7.19)
  - 이자·배당 합계 1,000만 원 이하이면 소득에 넣지 않음 : 시행규칙 제44조 ① 단서
  - 피부양자 소득 2,000만 원 이하, 재산 과표 5.4억 이하(5.4억 초과 9억 이하면 소득 1,000만 원 이하), 부부 모두 : 시행규칙 별표 1의2

연구·교육용 계산 예시 — 실제 보험료는 공단 고지 금액이 기준이다. 세무·보험 상담이 아니다.
"""
import datetime as dt
import logging
import math
import sys
import time

VERSION = "v1.0"

# ───────────────────────── 가정 (대본 '예시 부부') ─────────────────────────
RETIRE_DATE = dt.date(2026, 9, 30)   # 남편 퇴직일 (사용관계가 끝난 날). 60세 정년퇴직 예시
BOSU_MONTH = 5_000_000               # 퇴직 전 12개월 평균 보수월액(원) = '평균 월급 500만 원' (상여 포함, 비과세 제외)
SALARY_BY_YEAR = {                   # 근로소득(총급여) — 지역 보험료 소득 자료로 쓰이는 해의 금액 (가정: 해마다 같은 월급)
    2024: 60_000_000,
    2025: 60_000_000,
    2026: 45_000_000,                # 2026년 1~9월만 (500만 원 × 9개월)
}
HOUSE_TAX_BASE = 300_000_000         # 집(남편 이름 아파트 한 채)의 재산세 과세표준 3억 원 — 공시가격 약 5억(60%)~6.8억(44%)
INTEREST_YEAR = 3_500_000            # 예금 1억 원 × 3.5% = 이자 350만 원 → 1,000만 원 이하라 건보료 소득에서 빠짐
SPOUSE_INCOME = 0                    # 아내: 소득 없음, 재산 없음 (남편의 피부양자였음)
HAS_EMPLOYED_CHILD = True            # 아들이 직장가입자
MONTHS = 36                          # 비교 기간 = 임의계속가입 최대 기간 (시행령 제77조: 퇴직 다음 날부터 36개월)

# ───────────────────────── 2026년 제도 숫자 ─────────────────────────
RATE = 0.0719                        # 건강보험료율 (직장·지역 같음)
POINT_WON = 211.5                    # 재산보험료부과점수당 금액
LOCAL_MIN = 20_160                   # 지역가입자 월별 보험료액 하한 (고시)
LOCAL_MIN_INCOME_MONTH = 280_000     # 소득월액 28만 원 이하 → 하한 보험료로 (시행규칙 제44조 ③)
PROPERTY_DEDUCT = 100_000_000        # 재산 기본 공제 1억 원 (별표 4 제1호)
WAGE_SHARE_LOCAL = 0.5               # 지역 소득월액에서 근로·연금소득 반영 비율 (시행규칙 제44조 ②2호)
INTEREST_CUT = 10_000_000            # 이자·배당 합계 1,000만 원 이하면 넣지 않음
NIM_REDUCE = 0.5                     # 임의계속가입자 보수월액보험료 경감 비율 (보험료 경감고시 제9조)
LTC_RATIO = round(0.9448 / 7.19, 4)  # 장기요양보험료 = 건보료 × (장기요양보험료율/건강보험료율), 소수 다섯째 자리 반올림 → 0.1314
DEP_INCOME_LIMIT = 20_000_000        # 피부양자 소득 기준
DEP_PROP_LIMIT = 540_000_000         # 피부양자 재산 기준 (과표)
DEP_PROP_LIMIT2 = 900_000_000        # 5.4억 초과 9억 이하면 소득 1,000만 원 이하
DEP_INCOME_LIMIT2 = 10_000_000

# 시행령 별표 4 제3호 재산등급별 점수 (재산금액 만 원 '이하' 상한, 점수) — 60등급
PROP_TABLE = [
    (450, 22), (900, 44), (1350, 66), (1800, 97), (2250, 122), (2700, 146), (3150, 171), (3600, 195), (4050, 219), (4500, 244),
    (5020, 268), (5590, 294), (6220, 320), (6930, 344), (7710, 365), (8590, 386), (9570, 412), (10700, 439), (11900, 465), (13300, 490),
    (14800, 516), (16400, 535), (18300, 559), (20400, 586), (22700, 611), (25300, 637), (28100, 659), (31300, 681), (34900, 706), (38800, 731),
    (43200, 757), (48100, 785), (53600, 812), (59700, 841), (66500, 881), (74000, 921), (82400, 961), (91800, 1001), (103000, 1041), (114000, 1091),
    (127000, 1141), (142000, 1191), (158000, 1241), (176000, 1291), (196000, 1341), (218000, 1391), (242000, 1451), (270000, 1511), (300000, 1571), (330000, 1641),
    (363000, 1711), (399300, 1781), (439230, 1851), (483153, 1921), (531468, 1991), (584615, 2061), (643077, 2131), (707385, 2201), (778124, 2271), (math.inf, 2341),
]

LOG = logging.getLogger("toejik-geonbo")


def log(stage, **kv):
    LOG.info("[%s] %s %s", stage, time.strftime("%Y-%m-%dT%H:%M:%S"), " ".join(f"{k}={v}" for k, v in kv.items()))


def won(x):
    return f"{x:,.0f}원"


def man(x):
    return f"{x / 10_000:,.1f}만"


# ───────────────────────── 계산 함수 ─────────────────────────
def property_points(tax_base):
    """재산세 과세표준(원) → 재산보험료부과점수 (별표 4). 0 이하이면 0점."""
    amt_man = (tax_base - PROPERTY_DEDUCT) / 10_000
    if amt_man <= 0:
        return 0, 0
    for i, (cap, pts) in enumerate(PROP_TABLE, start=1):
        if amt_man <= cap:
            return pts, i
    raise ValueError(tax_base)


def local_premium(tax_base, wage_year=0, other_income_year=0, min_per_person=1):
    """지역가입자 세대 월 건보료 (장기요양 제외).
    wage_year: 소득 자료 해의 근로소득(총급여) — 50%만 반영. other_income_year: 이자·배당·사업 등 전액 반영분.
    min_per_person: 소득월액 28만 원 이하일 때 하한 보험료를 몇 번 붙이는지 (기본 1 = 세대 하나, 민감도에서 2)."""
    income_month = (wage_year * WAGE_SHARE_LOCAL + other_income_year) / 12
    if income_month <= LOCAL_MIN_INCOME_MONTH:
        inc_part = LOCAL_MIN * min_per_person          # 하한액 ÷ 보험료율 = 소득월액 → × 보험료율 = 하한액
    else:
        inc_part = income_month * RATE
    pts, grade = property_points(tax_base)
    prop_part = pts * POINT_WON
    return inc_part + prop_part, inc_part, prop_part, pts, grade


def nim_premium(bosu_month):
    """임의계속가입자 월 건보료 (장기요양 제외): 보수월액 × 7.19% 전액 본인 부담, 그중 50% 경감."""
    full = bosu_month * RATE
    return full * (1 - NIM_REDUCE), full


def data_year(year, month):
    """지역 소득월액에 쓰는 소득 자료의 해 (시행령 제41조 ③1·2호, 근로소득 기준)."""
    return year - 2 if month <= 10 else year - 1


def month_iter(start_after, n):
    """퇴직 다음 날이 속한 달부터 n개월 (y, m). 퇴직 다음 날이 1일이면 그 달부터 지역 보험료 (법 제69조 ③ 단서)."""
    d = start_after + dt.timedelta(days=1)
    y, m = d.year, d.month
    if d.day != 1:                    # 1일이 아니면 그 달은 직장 자격 기준 → 다음 달부터
        y, m = (y + (m // 12), m % 12 + 1)
    out = []
    for _ in range(n):
        out.append((y, m))
        y, m = (y + (m // 12), m % 12 + 1)
    return out


def add_months(d, k):
    y, m = d.year + (d.month - 1 + k) // 12, (d.month - 1 + k) % 12 + 1
    return dt.date(y, m, min(d.day, 28 if m == 2 else 30 if m in (4, 6, 9, 11) else 31))


def local_timeline(adjust_from=None, tax_base=HOUSE_TAX_BASE):
    """36개월 동안 지역 보험료. adjust_from: 소득 조정이 적용되는 첫 달 번호(0부터). None 이면 조정 안 함.
    가정: 조정이 받아들여지면 끊긴 근로소득은 그 뒤 계속 빠진다(11월 새 자료 때도) — 확인 필요 C표."""
    rows = []
    for i, (y, m) in enumerate(month_iter(RETIRE_DATE, MONTHS)):
        dy = data_year(y, m)
        wage = SALARY_BY_YEAR.get(dy, 0)
        if adjust_from is not None and i >= adjust_from:
            wage = 0
        prem = local_premium(tax_base, wage_year=wage)[0]
        rows.append((y, m, dy, wage, prem))
    return rows


def dependent_ok(income_year, interest_year, tax_base):
    inc = income_year + (interest_year if interest_year > INTEREST_CUT else 0)
    if tax_base <= DEP_PROP_LIMIT:
        return inc <= DEP_INCOME_LIMIT, inc
    if tax_base <= DEP_PROP_LIMIT2:
        return inc <= DEP_INCOME_LIMIT2, inc
    return False, inc


def floor10(x):
    return math.floor(x / 10) * 10


# ───────────────────────── 실행 ─────────────────────────
def main():
    logging.basicConfig(stream=sys.stderr, level=logging.INFO, format="%(message)s")
    log("START", version=VERSION, retire=RETIRE_DATE, bosu=BOSU_MONTH, tax_base=HOUSE_TAX_BASE, months=MONTHS)
    P = print

    # 1) 임의계속가입
    nim, nim_full = nim_premium(BOSU_MONTH)
    log("NIM", full=round(nim_full), reduced=round(nim), floor10=floor10(nim))
    P("## 1. 임의계속가입 (문장: 예시·원칙 둘·결과)")
    P(f"- 보수월액 {won(BOSU_MONTH)} × 7.19% = {won(nim_full)} (회사 몫 포함 전액) → 50% 경감 → **{won(nim)}** (월급에서 빠지던 내 몫과 같음)")

    # 2) 지역 — 조정 후(근로소득 없음)
    loc, inc_part, prop_part, pts, grade = local_premium(HOUSE_TAX_BASE)
    log("LOCAL_ADJ", total=round(loc), income_part=inc_part, property_part=round(prop_part), points=pts, grade=grade)
    P("\n## 2. 지역가입자 — 끊긴 월급을 소득 조정으로 뺀 뒤")
    P(f"- 재산: 과표 {man(HOUSE_TAX_BASE)} − 공제 1억 = {man(HOUSE_TAX_BASE - PROPERTY_DEDUCT)} → {grade}등급 {pts}점 × 211.5원 = **{won(prop_part)}**")
    P(f"- 소득: 이자 {man(INTEREST_YEAR)}(1,000만 이하 → 0) + 근로소득 0 → 소득월액 28만 원 이하 → 하한 **{won(inc_part)}**")
    P(f"- 합계 **{won(loc)}** (10원 미만 절사 {won(floor10(loc))})")
    P(f"- 임의계속보다 한 달 {won(nim - loc)} 쌈 → 36개월 {won((nim - loc) * MONTHS)}")

    # 3) 지역 — 아무것도 안 함 (옛 월급이 소득 자료에 남음)
    raw = local_timeline(adjust_from=None)
    P("\n## 3. 지역가입자 — 아무것도 안 할 때 (월별)")
    seg = {}
    for y, m, dy, wage, prem in raw:
        seg.setdefault((dy, round(prem)), []).append(f"{y}.{m:02d}")
    for (dy, prem), ms in seg.items():
        wage = SALARY_BY_YEAR.get(dy, 0)
        P(f"- {ms[0]}~{ms[-1]} ({len(ms)}개월): 소득 자료 {dy}년 근로소득 {man(wage)} × 50% ÷ 12 = 소득월액 {man(wage * 0.5 / 12)} → 월 **{won(prem)}**")
        log("LOCAL_RAW", first=ms[0], last=ms[-1], n=len(ms), data_year=dy, wage=wage, premium=prem)
    tot_raw = sum(r[4] for r in raw)

    # 4) 36개월 합계
    tot_nim = nim * MONTHS
    tot_loc = loc * MONTHS
    P("\n## 4. 36개월(퇴직 다음 날부터 3년) 합계 — 장기요양보험료 제외")
    P(f"- 피부양자 0원 · 지역(바로 조정) **{won(tot_loc)}** · 임의계속 **{won(tot_nim)}** · 지역(그냥 둠) **{won(tot_raw)}**")
    P(f"- 그냥 둠 − 바로 조정 = {won(tot_raw - tot_loc)}")
    log("TOTAL36", dependent=0, local_adj=round(tot_loc), nim=round(tot_nim), local_raw=round(tot_raw))

    # 5) 조정이 늦으면
    P("\n## 5. 소득 조정을 늦게 하면 (조정은 그 뒤 보험료부터 — 시행령 제41조의2 ② '이후 부과하는')")
    late = {}
    for k in (0, 3, 6, 12):
        t = sum(r[4] for r in local_timeline(adjust_from=k))
        late[k] = t
        P(f"- {k}개월 뒤 조정: 36개월 {won(t)} (바로 할 때보다 +{won(t - tot_loc)})")
        log("LATE_ADJUST", months_late=k, total=round(t), extra=round(t - tot_loc))

    # 6) 집이 크면 — 과표 6억
    loc6, inc6, prop6, pts6, g6 = local_premium(600_000_000)
    P("\n## 6. 같은 월급, 집 과표 6억 원이면")
    P(f"- 과표 6억 − 1억 = 5억 → {g6}등급 {pts6}점 → 재산분 {won(prop6)} + 하한 {won(inc6)} = **{won(loc6)}** vs 임의계속 {won(nim)} → {'임의계속이 쌈' if nim < loc6 else '지역이 쌈'} (차이 {won(loc6 - nim)})")
    ok6, _ = dependent_ok(0, INTEREST_YEAR, 600_000_000)
    P(f"- 과표 6억이어도 피부양자 가능? {ok6} (5.4억 초과 9억 이하 → 소득 1,000만 원 이하면 됨)")
    ok900, _ = dependent_ok(9_000_000, 0, 600_000_000)
    ok1100, _ = dependent_ok(11_000_000, 0, 600_000_000)
    P(f"- 대본 예시(문장 31): 과표 6억 + 소득 900만 원 → {ok900} · 소득 1,100만 원이면 → {ok1100}")
    log("HOUSE6", local=round(loc6), nim=round(nim), dependent_ok=ok6)

    # 7) 손익분기: 월급 500만 원일 때 지역이 더 비싸지는 과표
    P("\n## 7. 손익분기 — 보수월액별로 지역(조정 후)이 임의계속보다 비싸지는 과표")
    for b in (300, 400, 500, 600, 700, 800):
        n_, _ = nim_premium(b * 10_000)
        be = None
        for tb in range(0, 2_000_000_001, 1_000_000):
            if local_premium(tb)[0] > n_:
                be = tb
                break
        P(f"- 보수월액 {b}만 원 → 임의계속 {won(n_)} · 지역이 더 비싸지는 과표: {man(be)} 초과")
        log("BREAKEVEN", bosu=b * 10_000, nim=round(n_), tax_base_over=be)

    # 8) 민감도 표 (조정 후 지역 − 임의계속, 만 원)
    P("\n## 8. 민감도 — (지역 조정 후 − 임의계속) 월 차이, 만 원 (음수 = 지역이 쌈)")
    tbs = [100, 200, 300, 400, 500, 600, 700]
    P("| 보수월액 \\ 과표(백만) | " + " | ".join(str(t) for t in tbs) + " |")
    P("|---|" + "---|" * len(tbs))
    for b in (300, 400, 500, 600, 700, 800):
        n_, _ = nim_premium(b * 10_000)
        cells = [f"{(local_premium(t * 1_000_000)[0] - n_) / 10_000:+.1f}" for t in tbs]
        P(f"| {b}만 | " + " | ".join(cells) + " |")

    # 9) 결론이 가정에 흔들리는지
    P("\n## 9. 가정을 바꿔도 예시의 순서(피부양자 < 지역 조정 < 임의계속 < 그냥 둠)가 그대로인지")
    checks = []
    l2 = local_premium(HOUSE_TAX_BASE, min_per_person=2)[0]
    checks.append(("소득 하한을 부부 두 사람에게 따로 붙이면", l2, nim))
    ltc_loc = loc * (1 + LTC_RATIO)
    ltc_nim_a = nim * (1 + LTC_RATIO)
    ltc_nim_b = nim + nim_full * LTC_RATIO
    checks.append(("장기요양 포함(임의계속은 경감 뒤 금액에)", ltc_loc, ltc_nim_a))
    checks.append(("장기요양 포함(임의계속은 경감 전 금액에)", ltc_loc, ltc_nim_b))
    for name, l_, n_ in checks:
        P(f"- {name}: 지역 {won(l_)} vs 임의계속 {won(n_)} → {'지역이 쌈 (순서 그대로)' if l_ < n_ else '임의계속이 쌈 (순서 바뀜)'}")
        log("SENS", case=name.replace(' ', '_'), local=round(l_), nim=round(n_))
    for sal in (50_000_000, 70_000_000):
        w = local_premium(HOUSE_TAX_BASE, wage_year=sal)[0]
        P(f"- 그냥 둘 때 소득 자료의 연봉이 {man(sal)}이면 첫 달 {won(w)}")
    P(f"- 장기요양 포함 첫 해(그냥 둠): {won(raw[0][4] * (1 + LTC_RATIO))} · 지역 조정 {won(ltc_loc)} · 임의계속 {won(ltc_nim_a)}~{won(ltc_nim_b)}")

    # 10) 날짜 — 임의계속 신청 기한, 36개월 끝
    first_y, first_m = month_iter(RETIRE_DATE, 1)[0]
    due = add_months(dt.date(first_y, first_m, 10), 1)          # 그 달 보험료 납부기한 = 다음 달 10일 (법 제78조 ①)
    deadline = add_months(due, 2)                               # 납부기한에서 2개월이 지나기 전까지 (법 제110조 ①)
    end36 = add_months(RETIRE_DATE + dt.timedelta(days=1), 36) - dt.timedelta(days=1)
    dep90 = RETIRE_DATE + dt.timedelta(days=1) + dt.timedelta(days=90)
    P("\n## 10. 날짜 (예시: 9월 30일 퇴직)")
    P(f"- 자격 변동(지역가입자) {RETIRE_DATE + dt.timedelta(days=1)} · 첫 지역 보험료 {first_y}.{first_m:02d}월분 · 납부기한 {due} · 임의계속 신청 마감 {deadline} 무렵(그 전까지)")
    P(f"- 임의계속 최대 기간 끝 {end36} · 피부양자 90일 신고 기한 약 {dep90}")
    log("DATES", change=RETIRE_DATE + dt.timedelta(days=1), first_bill=f"{first_y}-{first_m:02d}", due=due, nim_deadline=deadline, end36=end36, dep90=dep90)

    # 11) 피부양자 판정
    ok, inc = dependent_ok(0, INTEREST_YEAR, HOUSE_TAX_BASE)
    P("\n## 11. 피부양자 판정 (끊긴 월급을 뺀 뒤)")
    P(f"- 남편 소득 {won(inc)} (이자 {man(INTEREST_YEAR)}는 1,000만 원 이하라 0) · 과표 {man(HOUSE_TAX_BASE)} ≤ 5.4억 → {ok} · 아내 소득·재산 0 → True · 자녀 직장가입자 {HAS_EMPLOYED_CHILD}")
    log("DEPENDENT", husband_income=inc, ok=ok, child=HAS_EMPLOYED_CHILD)

    # 12) 대본에서 쓰는 반올림 숫자
    P("\n## 12. 대본 숫자 (반올림)")
    P(f"- 내 몫 건보료 약 {nim / 10_000:.0f}만 원 · 지역(조정) 약 {loc / 10_000:.1f}만 원 · 재산분 약 {prop_part / 10_000:.1f}만 원 · 하한 약 {LOCAL_MIN / 10_000:.0f}만 원")
    P(f"- 그냥 둠 첫 13개월 약 {raw[0][4] / 10_000:.0f}만 원 · 다음 12개월 약 {raw[13][4] / 10_000:.0f}만 원")
    P(f"- 36개월: 그냥 둠 약 {tot_raw / 10_000:.0f}만 · 임의계속 약 {tot_nim / 10_000:.0f}만 · 지역 조정 약 {tot_loc / 10_000:.0f}만 · 차이(지역 조정 vs 임의계속) 월 약 {(nim - loc) / 10_000:.2f}만, 36개월 약 {(nim - loc) * 36 / 10_000:.0f}만")
    P(f"- 1년 늦게 조정: 약 {late[12] / 10_000:.0f}만 (바로 할 때보다 약 {(late[12] - tot_loc) / 10_000:.0f}만 더) · 연봉 6,000만의 절반 3,000만")
    log("DONE", version=VERSION)


if __name__ == "__main__":
    main()
