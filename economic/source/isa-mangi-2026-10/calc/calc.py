#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ISA 만기 때 할 일 — 대본 숫자 계산 (단위: 만 원)

VERSION: v1.0 — 2026-10-14 — 최초 작성 (대본 isa-mangi-2026-10.txt v1.0 의 숫자)
  - A 방법 '그냥 찾기'(만기 돈을 정기예금에) vs B 방법 '연금계좌 3,000만 원 + 새 ISA' vs C 방법 '만기 연장'
  - 3년(다음 만기까지)·6년(은퇴 전 두 번) 세금 합계, 공제받는 사람 / 세금이 없는 사람, 민감도

법 (law.go.kr 현행 원문, 2026-10-14 받음 — checklist.md A표):
  - 조세특례제한법 [시행 2026.9.18] [법률 제21467호] 제91조의18
      ① 비과세 한도를 넘는 이자·배당은 9% 분리과세 (+ 지방소득세 10% → 9.9%)
      ② 비과세 한도 200만 원 (서민형 400만 원)  ③4 계약기간 3년 이상  ③5 총 1억 원, 연간 = 2천만 원 × (1 + 경과 연수) − 누적 납입
      ⑤ 손익을 합쳐 해지일에 계산  ⑪ 3년이 지난 뒤 연금계좌로 옮기면 그날 만기로 봄
  - 소득세법 [시행 2026.7.1] [법률 제21221호] 제59조의3 ① 12%(종합소득금액 4,500만 원·총급여 5,500만 원 이하 15%) ③④ 전환금액 10%·최대 300만 원 추가
      제61조 ② 세액공제는 산출세액을 넘지 못함, ③ 못 받은 만큼은 공제받지 않은 것으로 봄
      제129조 ①1호 라목 이자 14% · ①5의2 연금수령 5%(70세 미만)·4%·3% · ①6호 나목 연금외수령 15%
  - 소득세법 시행령 [시행 2026.10.1] [대통령령 제36737호] 제118조의2 ③ 만기일부터 60일 이내 · 제40조의2 ②1호 1,800만 원과 별도
  - 지방세법 [시행 2026.7.1] 제103조의13 ① 원천징수 소득세의 10% 를 지방소득세로

가정 (사실이 아니라 예시 — 대본에서 '봤습니다'로 말함):
  - 61세 직장인, 총급여 6,000만 원 → 연금계좌 공제율 13.2%. 65세까지 일함(64세 10월 두 번째 이전 때도 소득세를 냄).
  - 평소 연금저축 600·IRP 300 을 넣어 1년 공제 기준 900만 원을 이미 채움 → ISA 이전으로 더 받는 공제 대상은 300만 원뿐
    (평소 넣지 않았다면 전환금액이 600/900 기준도 채움 — 제59조의3 ③④, 대본에는 넣지 않음, README '넣지 않은 것').
  - ISA 는 2023년 10월 가입, 2023·2024·2025년에 2,000만 원씩 = 원금 6,000만 원, 만기(2026년 10월) 잔액 6,800만 원(이익 800만 원).
  - 예금·ISA·연금계좌 모두 연 3.5% (같은 수익 → 세금 차이만 봄). 다른 수익률은 민감도.
  - 새 ISA 첫해 한도 2,000만 원을 넘는 돈은 다음 해 1월까지 3개월 예금에 둠.
  - 연금계좌에서 나중에 낼 세금 = (공제받은 300만 원 + 불어난 몫) × 5.5% (70세 전에 연금으로 받는다고 봄 — 가장 높은 연금 세율이라 B에 불리한 쪽).
  - 건보료는 넣지 않음 (이 예에서 예금 이자 1년 약 236만 원 < 이자·배당 기준 1,000만 원이라 영향 없음).
연구·교육용 예시 계산 — 세무·투자 권유 아님.

실행:  python3 calc.py            # 대본 숫자 + 민감도
       python3 calc.py --log-level DEBUG
로그:  [STAGE] 시각 key=value (stderr)
"""
import argparse
import logging
import sys
import time

VERSION = "v1.0"
LOG = logging.getLogger("isa_calc")


def log(stage, level=logging.INFO, **kv):
    LOG.log(level, "[%s] %s %s", stage, time.strftime("%Y-%m-%dT%H:%M:%S"), " ".join(f"{k}={v}" for k, v in kv.items()))


# ----------------------------------------------------------------------------- 법 (2026-10-14 현행)
LOCAL = 1.10                      # 지방소득세 = 소득세의 10%
ISA_TAX = 0.09 * LOCAL            # 9.9%
ISA_FREE = {"일반형": 200, "서민형": 400}
ISA_YEAR = 2000                   # 연간 납입: 2천만 원 × (1 + 경과 연수) − 누적 납입
DEP_TAX = 0.14 * LOCAL            # 예금 이자 15.4%
TR_RATE, TR_CAP = 0.10, 300       # 전환금액의 10%, 최대 300만 원
CREDIT_NAT = {"13.2%": 0.12, "16.5%": 0.15}   # 소득세 몫 (지방세 포함하면 13.2%·16.5%)
PEN_RATE = {"70세 미만": 0.05 * LOCAL, "70~79세": 0.04 * LOCAL, "80세 이상": 0.03 * LOCAL}
NONPEN = 0.15 * LOCAL             # 연금외수령 16.5%

# ----------------------------------------------------------------------------- 가정
R = 0.035
AGE0 = 61
ISA1_PRIN, ISA1_GAIN = 6000, 800
TRANSFER = 3000                   # 공제 한도 300만 원을 다 쓰는 금액 (3,000 × 10%)
PARK = 0.25                       # 10월 → 다음 해 1월
WITHDRAW = "70세 미만"


def isa_settle(principal, gain, kind="일반형"):
    """ISA 해지: 이익이 비과세 한도를 넘는 몫에 9.9%. 반환 (받는 돈, 세금)."""
    tax = max(0.0, gain - ISA_FREE[kind]) * ISA_TAX
    return principal + gain - tax, tax


def credit_amount(transfer, rate_key, tax_room=None):
    """ISA 전환금액 추가 공제 (지방세 포함 금액). tax_room = 그해 남은 결정세액(소득세 몫, 만 원). 0 이면 공제 0."""
    base = min(transfer * TR_RATE, TR_CAP)
    nat = base * CREDIT_NAT[rate_key]
    if tax_room is not None:
        nat = min(nat, max(tax_room, 0.0))
    used_base = nat / CREDIT_NAT[rate_key] if CREDIT_NAT[rate_key] else 0.0   # 제61조 ③: 못 받은 만큼은 공제받지 않은 것
    return nat * LOCAL, used_base


def path_a(years, rate=R):
    """A: 만기 해지 → 받은 돈을 정기예금에. 이자에 해마다 15.4%."""
    cash, isa_tax = isa_settle(ISA1_PRIN, ISA1_GAIN)
    dep_tax = 0.0
    for _ in range(years):
        it = cash * rate
        dep_tax += it * DEP_TAX
        cash += it * (1 - DEP_TAX)
    total = isa_tax + dep_tax
    log("PATH_A", years=years, rate=rate, isa_tax=round(isa_tax, 1), dep_tax=round(dep_tax, 1), total=round(total, 1), end_cash=round(cash, 1))
    return dict(isa_tax=isa_tax, dep_tax=dep_tax, credit=0.0, pen_defer=0.0, total=total, end=cash, first_year_dep_tax=None)


def path_b(years, rate=R, credit_key="13.2%", working_until=65, tax_room=None, withdraw=WITHDRAW, transfer=TRANSFER, kind_new="일반형"):
    """B: 만기 해지 → 3,000만 원 연금계좌 → 나머지 새 ISA (첫해 2,000, 나머지는 다음 해 1월) → 3년마다 반복.
    working_until: 이 나이 전(미만)에 이전하면 공제를 받음. tax_room: 공제를 받을 수 있는 결정세액(소득세 몫) — None 이면 충분."""
    cash, isa_tax = isa_settle(ISA1_PRIN, ISA1_GAIN)
    tot = dict(isa_tax=isa_tax, dep_tax=0.0, credit=0.0, pen_defer=0.0)
    pens = []          # (넣은 돈, 넣은 시점 t, 공제받은 몫)
    t = 0
    while t < years:
        age = AGE0 + t
        p = min(transfer, cash)
        if age < working_until:
            cr, used = credit_amount(p, credit_key, tax_room)
        else:
            cr, used = 0.0, 0.0
        tot["credit"] += cr
        pens.append((p, t, used))
        rest = cash - p
        hold = min(3, years - t)
        pieces, k = [], 0                                    # (넣는 돈, 예금에서 기다린 해): 첫해 2,000 → 다음 해 1월부터 해마다 2,000
        while rest > 1e-9:
            amt = min(ISA_YEAR, rest)
            pieces.append((amt, 0.0 if k == 0 else PARK + (k - 1)))
            rest -= amt
            k += 1
        val = paid_in = 0.0
        for amt, wait in pieces:
            tot["dep_tax"] += amt * rate * wait * DEP_TAX       # 기다리는 동안 예금 이자 세금
            amt_in = amt * (1 + rate * wait * (1 - DEP_TAX))
            paid_in += amt_in
            val += amt_in * (1 + rate) ** (hold - wait)
        first, x = pieces[0][0] if pieces else 0.0, sum(a for a, _ in pieces[1:])
        gain = val - paid_in
        cash, t_isa = isa_settle(paid_in, gain, kind_new)
        tot["isa_tax"] += t_isa
        log("CYCLE", t=t, age=age, transfer=round(p, 1), credit=round(cr, 1), new_isa_first=round(first, 1), park=round(x, 1),
            isa_gain=round(gain, 1), isa_tax=round(t_isa, 1), cash_after=round(cash, 1))
        t += 3
    pen_val = sum(p * (1 + rate) ** (years - t0) for p, t0, _ in pens)
    pen_in = sum(p for p, _, _ in pens)
    deducted = sum(u for _, _, u in pens)
    pen_gain = pen_val - pen_in
    w = NONPEN if withdraw == "연금외" else PEN_RATE[withdraw]
    tot["pen_defer"] = (deducted + pen_gain) * w
    total = tot["isa_tax"] + tot["dep_tax"] + tot["pen_defer"] - tot["credit"]
    end = cash + pen_val - tot["pen_defer"] + tot["credit"]       # 돌려받은 공제도 손에 남는 돈 (이자 없이 더함)
    log("PATH_B", years=years, rate=rate, credit_key=credit_key, working_until=working_until, withdraw=withdraw,
        isa_tax=round(tot["isa_tax"], 1), dep_tax=round(tot["dep_tax"], 1), credit=round(tot["credit"], 1),
        pen_in=round(pen_in, 1), pen_gain=round(pen_gain, 1), deducted=round(deducted, 1), pen_defer=round(tot["pen_defer"], 1),
        total=round(total, 1), end_after_tax=round(end, 1))
    return dict(**tot, total=total, end=end, pen_val=pen_val, pen_gain=pen_gain, deducted=deducted)


def path_c(years, rate=R):
    """C: 만기를 연장해 그대로 두고, years 년 뒤 해지 (새 납입 없음)."""
    val = (ISA1_PRIN + ISA1_GAIN) * (1 + rate) ** years
    gain = val - ISA1_PRIN
    end, tax = isa_settle(ISA1_PRIN, gain)
    log("PATH_C", years=years, rate=rate, gain=round(gain, 1), isa_tax=round(tax, 1), end=round(end, 1))
    return dict(total=tax, end=end)


# ----------------------------------------------------------------------------- 결정세액 근사 (검산용 — 대본에 숫자로 쓰지 않음)
def wage_tax_nat(gross, insurance_rate=0.09, dependents=1):
    """총급여 → 결정세액(소득세 몫, 만 원) 근사. 근로소득공제(제47조 표)·기본공제 150×인원(제50조)·
    4대 보험료 공제 = 총급여 × insurance_rate(근사)·기본세율(제55조)·근로소득세액공제(제59조)·표준세액공제 13(제59조의4 ⑨1).
    다른 공제(카드·의료비 등)는 넣지 않음 → 실제 결정세액은 이보다 작을 수 있다."""
    g = gross
    if g <= 500: ded = g * 0.7
    elif g <= 1500: ded = 350 + (g - 500) * 0.4
    elif g <= 4500: ded = 750 + (g - 1500) * 0.15
    elif g <= 10000: ded = 1200 + (g - 4500) * 0.05
    else: ded = 1475 + (g - 10000) * 0.02
    ded = min(ded, 2000)
    base = max(g - ded - 150 * dependents - g * insurance_rate, 0)
    br = [(1400, .06, 0), (5000, .15, 126), (8800, .24, 576), (15000, .35, 1544), (30000, .38, 1994)]
    calc = base * .40 - 2594
    for top, r, sub in br:
        if base <= top:
            calc = max(base * r - sub, 0)
            break
    wc = calc * 0.55 if calc <= 130 else 71.5 + (calc - 130) * 0.30
    if g <= 3300: cap = 74
    elif g <= 7000: cap = max(74 - (g - 3300) * 0.008, 66)
    elif g <= 12000: cap = max(66 - (g - 7000) * 0.5, 50)
    else: cap = max(50 - (g - 12000) * 0.5, 20)
    det = max(calc - min(wc, cap) - 13, 0)
    return det


def pension_deduction(total):
    """연금소득공제 (소득세법 제47조의2 표, 한도 900) — 앞 영상 calc/tax.py 와 같음."""
    if total <= 350: d = total
    elif total <= 700: d = 350 + (total - 350) * 0.4
    elif total <= 1400: d = 490 + (total - 700) * 0.2
    else: d = 630 + (total - 1400) * 0.1
    return min(d, 900)


def pension_only_tax_nat(monthly, taxable_share=0.65, spouse=True):
    """국민연금만 받는 사람의 결정세액(소득세 몫). 과세 몫 65%(2002년 이후 납입분, 소득세법 제20조의3 ②) — 앞 영상과 같은 가정.
    기본공제 150(본인) + 배우자 150(소득 없는 배우자), 표준세액공제 7(제59조의4 ⑨2호 나목)."""
    tot = monthly * 12 * taxable_share
    inc = tot - pension_deduction(tot)
    base = max(inc - 150 - (150 if spouse else 0), 0)
    br = [(1400, .06, 0), (5000, .15, 126), (8800, .24, 576)]
    calc = next(max(base * r - sub, 0) for top, r, sub in br if base <= top)
    return max(calc - 7, 0)


def main(argv=None):
    global ISA1_GAIN, PARK
    ap = argparse.ArgumentParser(description="ISA 만기 계산 (대본 isa-mangi-2026-10)")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args(argv)
    logging.basicConfig(level=getattr(logging, a.log_level), format="%(message)s", stream=sys.stderr)
    log("START", version=VERSION, rate=R, age0=AGE0, isa_principal=ISA1_PRIN, isa_gain=ISA1_GAIN, transfer=TRANSFER)

    out = []
    p = out.append
    cash0, t0 = isa_settle(ISA1_PRIN, ISA1_GAIN)
    p(f"■ 만기 ISA: 원금 {ISA1_PRIN:,} + 이익 {ISA1_GAIN:,} = {ISA1_PRIN + ISA1_GAIN:,}만 원 → 해지 세금 ({ISA1_GAIN} − 200) × 9.9% = {t0:.1f}만 원, 받는 돈 {cash0:,.1f}만 원")
    cr_hi, _ = credit_amount(TRANSFER, "13.2%")
    cr_lo, _ = credit_amount(TRANSFER, "16.5%")
    p(f"■ 연금계좌 3,000만 원 이전 → 추가 공제 대상 min(10%, 300) = 300만 원 → 돌려받는 세금 13.2% {cr_hi:.1f}만 원 / 16.5% {cr_lo:.1f}만 원")
    p(f"  · 3,000만 원보다 더 옮겨도 공제 대상은 300만 원 그대로 (6,000만 원 × 10% = 600 → 300)")
    p(f"  · 공제받은 300만 원을 나중에 연금으로 받으면 세금 5.5% {300 * PEN_RATE['70세 미만']:.1f} · 4.4% {300 * PEN_RATE['70~79세']:.1f} / 한꺼번에(연금외수령) 16.5% {300 * NONPEN:.1f}만 원")
    p(f"    → 13.2% 사람이 한꺼번에 찾으면 {cr_hi:.1f} − {300 * NONPEN:.1f} = {cr_hi - 300 * NONPEN:.1f}만 원 (손해), 연금으로 받으면 {cr_hi - 300 * PEN_RATE['70세 미만']:.1f}만 원 남음")
    a1 = cash0 * R * DEP_TAX
    p(f"■ 예금 이자 세금 첫해: {cash0:,.1f} × 3.5% = {cash0 * R:.1f}만 원 이자 → 15.4% {a1:.1f}만 원 (건보료 이자 기준 1,000만 원 아래)")

    p("\n■ 3년 (다음 만기, 61→64세) — 세금 합계 = ISA 세금 + 예금 이자 세금 + 연금계좌에서 나중에 낼 세금 − 돌려받는 공제")
    A3, B3, C3 = path_a(3), path_b(3), path_c(3)
    B3r = path_b(3, working_until=0)                       # 은퇴: 공제 0
    B3lo = path_b(3, credit_key="16.5%")
    for name, r in (("A 그냥 찾기", A3), ("B 연금+새 ISA (13.2%)", B3), ("B (16.5%)", B3lo), ("B (세금 없는 은퇴자, 공제 0)", B3r)):
        p(f"  {name:24s} 합계 {r['total']:6.1f} | ISA {r['isa_tax']:.1f} 예금 {r['dep_tax']:.1f} 연금 나중 {r['pen_defer']:.1f} 공제 −{r['credit']:.1f} | 3년 뒤 손에 남는 돈 {r['end']:,.1f}")
    p(f"  C 연장 후 3년 뒤 해지        합계 {C3['total']:6.1f} | 3년 뒤 {C3['end']:,.1f}")
    d3 = A3["total"] - B3["total"]
    p(f"  → A − B = {d3:.1f}만 원 (16.5% 사람 {A3['total'] - B3lo['total']:.1f}, 은퇴자 {A3['total'] - B3r['total']:.1f}) · 손에 남는 돈 차이 {B3['end'] - A3['end']:.1f} · 한 달 {d3 / 36:.1f}만 원")
    p(f"  → C − B = {C3['total'] - B3['total']:.1f}만 원")

    p("\n■ 6년 (은퇴 전 두 번 이전: 61세·64세, 67세에 셋째 ISA 해지)")
    A6, B6, B6r = path_a(6), path_b(6), path_b(6, working_until=0)
    C6 = path_c(6)
    for name, r in (("A 그냥 찾기", A6), ("B 연금+새 ISA (13.2%)", B6), ("B (은퇴자, 공제 0)", B6r)):
        p(f"  {name:24s} 합계 {r['total']:6.1f} | ISA {r['isa_tax']:.1f} 예금 {r['dep_tax']:.1f} 연금 나중 {r['pen_defer']:.1f} 공제 −{r['credit']:.1f} | 6년 뒤 {r['end']:,.1f}")
    p(f"  C 연장 6년 뒤 해지           합계 {C6['total']:6.1f}")
    d6 = A6["total"] - B6["total"]
    p(f"  → A − B = {d6:.1f}만 원 · 한 달 {d6 / 72:.1f}만 원 · 손에 남는 돈 차이 {B6['end'] - A6['end']:.1f}")

    p("\n■ 공제가 결정세액에 막히는지 (제61조 ②) — 근사: 4대 보험 9%, 본인만 기본공제, 카드·의료비 등 다른 공제 없음")
    for g, own in ((6000, 900), (6000, 0), (4000, 900), (4000, 0)):
        det = wage_tax_nat(g)
        rk = "13.2%" if g > 5500 else "16.5%"
        reg = own * CREDIT_NAT[rk]                       # 평소 연금저축·IRP 공제(소득세 몫)
        room = det - reg
        cr, used = credit_amount(TRANSFER, rk, room)
        p(f"  총급여 {g:,} · 평소 연금 {own} → 결정세액 약 {det:.0f}(소득세) − 평소 공제 {reg:.0f} = 남은 {room:.0f} → ISA 이전 공제 {cr:.1f}만 원 (인정 {used:.0f}/300)")
    for m, sp in ((110, True), (110, False), (150, False)):
        det = pension_only_tax_nat(m, spouse=sp)
        cr, used = credit_amount(TRANSFER, "16.5%", det)
        p(f"  국민연금만 월 {m}만 원 (배우자 공제 {'있음' if sp else '없음'}) → 결정세액 {det:.1f}(소득세) → ISA 이전 공제 {cr:.1f}만 원")
    rng = [pension_only_tax_nat(110, sh, sp) * LOCAL for sh in (0.5, 0.65, 0.8, 1.0) for sp in (True, False)]
    p(f"  국민연금만 월 110만 원, 과세 몫 50~100%·배우자 공제 있음/없음 → 1년 세금(지방세 포함) {min(rng):.1f}~{max(rng):.1f}만 원 → '30만 원도 안 돼서 49만 5천 원을 다 못 받음'")
    log("RETIREE", tax_min=round(min(rng), 1), tax_max=round(max(rng), 1))
    log("TAXROOM", gross6000=round(wage_tax_nat(6000), 1), gross4000=round(wage_tax_nat(4000), 1),
        pension110=round(pension_only_tax_nat(110), 1), pension110_single=round(pension_only_tax_nat(110, spouse=False), 1))

    p("\n■ 민감도 — 3년 A − B (만 원)")
    for rr in (0.02, 0.035, 0.05, 0.07):
        a_, b_, br_ = path_a(3, rr), path_b(3, rr), path_b(3, rr, working_until=0)
        p(f"  수익률 {rr:.1%}: 13.2% {a_['total'] - b_['total']:6.1f} · 은퇴자 {a_['total'] - br_['total']:6.1f}")
    for w in ("70세 미만", "70~79세", "연금외"):
        b_ = path_b(3, withdraw=w)
        p(f"  연금계좌 꺼내는 방식 {w:6s}: A − B = {A3['total'] - b_['total']:.1f}")
    keep = ISA1_GAIN
    for g in (0, 800, 2000):
        ISA1_GAIN = g
        a_, b_ = path_a(3), path_b(3)
        p(f"  첫 ISA 이익 {g:5,}: A − B = {a_['total'] - b_['total']:.1f} (ISA 해지 세금은 A·B 같음 {isa_settle(ISA1_PRIN, g)[1]:.1f})")
    ISA1_GAIN = keep
    for tr in (1000, 3000, 6000):
        b_ = path_b(3, transfer=tr)
        p(f"  연금계좌로 옮기는 돈 {tr:,}: 공제 {b_['credit']:.1f}, A − B = {A3['total'] - b_['total']:.1f}")

    for pk in (0.25, 1.0):
        PARK = pk
        b_ = path_b(3)
        p(f"  새 ISA 둘째 납입까지 기다리는 기간 {pk}년{' (1월에 한도가 생김)' if pk < 1 else ' (가입 1년 뒤에 한도가 생김)'}: A − B = {A3['total'] - b_['total']:.1f}")
    PARK = 0.25

    p("\n■ 민감도 — 6년 A − B (만 원)")
    for rr in (0.02, 0.035, 0.05):
        a_, b_, blo, br_ = path_a(6, rr), path_b(6, rr), path_b(6, rr, credit_key="16.5%"), path_b(6, rr, working_until=0)
        p(f"  수익률 {rr:.1%}: 13.2% {a_['total'] - b_['total']:6.1f} · 16.5% {a_['total'] - blo['total']:6.1f} · 은퇴자 {a_['total'] - br_['total']:6.1f}")
    for w in ("70~79세", "연금외"):
        b_ = path_b(6, withdraw=w)
        p(f"  연금계좌 꺼내는 방식 {w}: A − B = {A6['total'] - b_['total']:.1f}")

    p("\n■ 늦게 고치면 — 60일이 지나 그냥 예금에 둔 해마다")
    p(f"  예금 이자 세금 1년 약 {a1:.1f}만 원 (6,740만 원 × 3.5% × 15.4%), 이번 ISA 의 연금 이전 공제 {cr_hi:.1f}만 원은 되돌릴 수 없음")
    p("\n■ 대본 숫자 (문장 번호 = srt_tool 문장 순서, 대본 v1.0)")
    late_isa = B3["isa_tax"] - t0
    p(f"  3·64 세금 3년: A {A3['total']:.1f} → 약 172 / B {B3['total']:.1f} → 약 76")
    p(f"  45·65 첫 ISA 해지 세금 {t0:.1f} (59만 4천 원), 받는 돈 {cash0:,.1f} → 6,740 / 49 남은 돈 {cash0 - TRANSFER:,.1f} → 3,740")
    p(f"  50·51 예금 1년 이자 {cash0 * R:.1f} → 236, 세금 {a1:.1f} → 약 36 / 66 3년 예금 이자 세금 {A3['dep_tax']:.1f} → 112")
    p(f"  68 B 가 나중에 낼 세금 = 새 ISA {late_isa:.1f} + 연금저축 {B3['pen_defer']:.1f} = {late_isa + B3['pen_defer']:.1f} → 약 53 (+ 3개월 예금 {B3['dep_tax']:.1f} = '거의 내지 않음')")
    PARK = 1.0
    d3_late, d6_late = A3["total"] - path_b(3)["total"], A6["total"] - path_b(6)["total"]
    PARK = 0.25
    p(f"  6·69 3년 차이 {d3:.1f} → 96 (새 ISA 둘째 납입이 1년 뒤라면 {d3_late:.1f} → 문장 6 '90만 원이 넘고')")
    p(f"  6·70 6년 차이 {d6:.1f} → 약 2백만 원 (둘째 납입이 1년 뒤라면 {d6_late:.1f})")
    p(f"  27·28·37·38 공제 {cr_hi:.1f}·{cr_lo:.1f} / 한꺼번에 {300 * NONPEN:.1f} / 연금 {300 * PEN_RATE['70세 미만']:.1f}, 남는 돈 {cr_hi - 300 * PEN_RATE['70세 미만']:.1f}")
    p(f"  53 연장(C) − B = {C3['total'] - B3['total']:.1f} → 약 57 / 72 은퇴자 A − B = {A3['total'] - B3r['total']:.1f} → 약 73")
    print("\n".join(out))
    log("DONE", d3=round(d3, 1), d6=round(d6, 1), credit_hi=round(cr_hi, 1), credit_lo=round(cr_lo, 1))


if __name__ == "__main__":
    main()
