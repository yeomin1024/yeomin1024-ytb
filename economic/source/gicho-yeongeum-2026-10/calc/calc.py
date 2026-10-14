#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""VERSION: v1.0 — 2026-10-14 — 최초 작성. 대본 gicho-yeongeum-2026-10.txt v1.0 의 숫자를 모두 낸다.

기초연금 받을 수 있나 — 예시 부부의 소득인정액·기초연금액(최소)·민감도 (단위: 원, 월)

근거 (law.go.kr 현행 원문, 2026-10-14 받음):
- 기초연금법 [시행 2025.10.1] [법률 제21065호]: 제2조4호(소득인정액 = 본인·배우자 소득평가액 + 재산의 소득환산액),
  제3조①②③(선정기준액 이하·수급자 70%·직역연금 제외), 제5조④⑤(국민연금 연계: 기준연금액 − 2/3×A급여 + 부가연금액 1/2),
  제6조①(국민연금 급여액등 ≤ 기준연금액 150% → 기준연금액 전액), 제7조(상한), 제8조①(부부 각각 20% 감액)·②(소득역전 감액),
  제14조①(신청한 날이 속하는 달부터 지급)
- 기초연금법 시행령 [시행 2026.7.30] [대통령령 제36371호]: 제2조(소득 범위), 제3조(재산 범위), 제4조②(부부 선정기준액 = 단독×160%),
  제10조(150~200% 구간: max(250% − 국민연금, 제5조 금액)), 제11조(소득역전 감액 지급 수준), 제13조의2(수급희망 이력관리·신청 간주)
- 기초연금법 시행규칙 [시행 2026.7.30] [보건복지부령 제1180호]: 제2조(소득평가액), 제3조(재산가액 = 시가표준액 등),
  제4조(소득환산액 = {(일반재산 − 기본재산액) + (금융재산 − 2천만) − 부채} × 4% ÷ 12 + 고급 자동차·회원권 가액), 제7조의2(이력관리 5년)
- 고시 「기초연금 지급대상자 선정기준액, 기준연금액 및 소득인정액 산정 세부기준에 관한 고시」
  [시행 2026.7.30] [보건복지부고시 제2026-156호]: 제2조(2026 선정기준액 단독 2,470,000 / 부부 3,952,000), 제3조(기준연금액 349,700),
  제6조(근로소득 기본공제 월 116만 원 + 나머지 30%, 부부 각각), 제6조의2(이자소득 월 4만 원 제외), 제8조(기본재산액 대도시 13,500만·
  중소도시 8,500만·농어촌 7,250만, 표 그림 flSeq=167629165), 제9조(금융재산 2,000만 원 제외), 제11조(차량가액 4천만 원 이상 → 가액 전부 소득, 차령 10년 이상 등 제외)

가정 (사실이 아니라 계산용 예시 — README 3번 표와 같음):
- 67세 동갑 부부, 대도시(서울) 거주, 둘 다 기초연금 신청
- 집: 본인 명의 아파트 한 채, 공시가격(시가표준액) 5억 원, 대출 없음
- 자동차: 10년 안 된 승용차 한 대, 차량가액 1,000만 원 (4천만 원 미만 → 일반재산)
- 예금: 부부 합쳐 4,000만 원, 금리 연 3.5% → 이자 월 116,667원. 이자 공제 월 4만 원은 '가구에 한 번'으로 보수적으로 둠(사람마다면 더 낮아짐)
- 국민연금(노령연금, 부양가족연금 제외): 남편 월 120만 원, 아내 월 50만 원. 일해서 버는 돈 없음
- 남편의 A급여액(소득재분배급여금액)은 사람마다 달라 모름 → 대본은 '최소'(부가연금액 = 기준연금액의 1/2)만 말함. 민감도에서 범위를 봄
- 직역연금(공무원·군인·사학·별정우체국) 없음, 자녀 명의 집에 살지 않음

실행: python3 calc.py            (대본 숫자)
      python3 calc.py -v         (민감도 표까지)
로그: [STAGE] 시각 key=value (stderr). 연구·교육용 — 수급 판정·법률 자문 아님.
"""
import logging
import sys
import time

VERSION = "v1.0"
LOG = logging.getLogger("gicho_calc")

# ---------- 2026 제도 값 (고시 제2026-156호, 시행령, 시행규칙) ----------
SEL_SINGLE = 2_470_000          # 선정기준액 단독 (고시 제2조)
SEL_COUPLE = 3_952_000          # 선정기준액 부부 (고시 제2조 = 단독 × 160%, 영 제4조②)
SEL_SINGLE_2025 = 2_280_000     # 작년 단독 선정기준액 (보건복지부 2025년 보도자료 제목 — 운영 근거, checklist B)
BASE = 349_700                  # 기준연금액 (고시 제3조)
BASIC_ASSET = {"대도시": 135_000_000, "중소도시": 85_000_000, "농어촌": 72_500_000}   # 고시 제8조
FIN_DEDUCT = 20_000_000         # 금융재산 제외 (고시 제9조)
CONV = 0.04                     # 재산의 소득환산율 연 4% (규칙 제4조②)
WORK_DEDUCT = 1_160_000         # 근로소득 기본공제 (고시 제6조①1)
WORK_EXTRA = 0.30               # 추가공제 30% (고시 제6조①2)
INT_DEDUCT = 40_000             # 이자소득 월 4만 원 제외 (고시 제6조의2)
LUX_CAR = 40_000_000            # 차량가액 4천만 원 이상 → 가액 전부 소득 (고시 제11조)
COUPLE_CUT = 0.20               # 부부 감액 (법 제8조①)

# ---------- 예시 부부 (가정) ----------
EX = dict(region="대도시", house=500_000_000, car=10_000_000, debt=0, deposit=40_000_000, rate=0.035,
          pen_h=1_200_000, pen_w=500_000, work_h=0, work_w=0, a_h=None, int_per_person=False)


def log(stage, **kv):
    LOG.info("[%s] %s %s", stage, time.strftime("%Y-%m-%dT%H:%M:%S"), " ".join(f"{k}={v}" for k, v in kv.items()))


def work_income(w):
    """근로소득 중 소득으로 잡히는 돈 (한 사람). 고시 제6조: 116만 원 빼고 나머지의 70%."""
    return max(w - WORK_DEDUCT, 0) * (1 - WORK_EXTRA)


def property_conv(region, house, car, debt, deposit):
    """재산의 소득환산액 (월). 규칙 제4조①: {(일반 − 기본재산액)⁺ + (금융 − 2천만)⁺ − 부채}⁺ × 4% ÷ 12 + 고급차 가액."""
    lux = car if car >= LUX_CAR else 0
    general = house + (car if car < LUX_CAR else 0)
    g = max(general - BASIC_ASSET[region], 0)
    f = max(deposit - FIN_DEDUCT, 0)
    net = max(g + f - debt, 0)
    return net * CONV / 12 + lux, g, f


def income_eval(p):
    """소득평가액 (월): 국민연금(공적이전소득, 전액) + 근로소득(공제 뒤) + 이자소득(월 4만 원 뺀 나머지)."""
    interest = p["deposit"] * p["rate"] / 12
    if p["int_per_person"]:      # 예금을 반씩 나눠 두고 사람마다 4만 원씩 뺀다고 볼 때
        int_counted = 2 * max(interest / 2 - INT_DEDUCT, 0)
    else:                        # 가구에 한 번만 뺀다고 볼 때 (보수적)
        int_counted = max(interest - INT_DEDUCT, 0)
    work = work_income(p["work_h"]) + work_income(p["work_w"])
    return p["pen_h"] + p["pen_w"] + work + int_counted, interest, int_counted, work


def linked_amount(pension, a_benefit=None):
    """국민연금 연계 뒤 기초연금액 (한 사람, 부부 감액 전). 법 제5조⑤·제6조·제7조, 영 제10조.
    a_benefit(A급여액)를 모르면 None → 최소값(부가연금액)을 돌려준다 (> 150% 일 때)."""
    if pension <= BASE * 1.5:                               # 법 제6조①
        return BASE, "전액(150% 이하)"
    floor = BASE * 0.5                                      # 부가연금액 (법 제5조⑤3)
    art5 = floor if a_benefit is None else min(max(BASE - a_benefit * 2 / 3, 0) + floor, BASE)
    if pension <= BASE * 2.0:                               # 영 제10조: 큰 쪽
        return max(BASE * 2.5 - pension, art5), "150~200% 구간"
    return art5, "200% 초과 → 제5조 산식" + ("(최소)" if a_benefit is None else "")


def couple_benefit(sia, amt_h, amt_w):
    """부부 감액(20%)과 소득역전 감액. 법 제8조, 영 제11조②⑤."""
    h, w = amt_h * (1 - COUPLE_CUT), amt_w * (1 - COUPLE_CUT)
    if sia + h + w > SEL_COUPLE:                            # 소득역전 → 기준에서 소득인정액을 뺀 만큼(최소 기준연금액 20%)
        gap = SEL_COUPLE - sia
        tot = BASE * 0.2 if gap <= BASE * 0.2 else min(gap, h + w)
        h, w = tot * h / (h + w), tot * w / (h + w)
        h, w = max(h, BASE * 0.1), max(w, BASE * 0.1)
    return h, w


def evaluate(p, tag="예시"):
    conv, g, f = property_conv(p["region"], p["house"], p["car"], p["debt"], p["deposit"])
    inc, interest, int_counted, work = income_eval(p)
    sia = inc + conv
    ok = sia <= SEL_COUPLE
    amt_h, why_h = linked_amount(p["pen_h"], p["a_h"])
    amt_w, why_w = linked_amount(p["pen_w"])
    h, w = couple_benefit(sia, amt_h, amt_w) if ok else (0, 0)
    log("EVAL", tag=tag, house=p["house"], deposit=p["deposit"], pen_h=p["pen_h"], pen_w=p["pen_w"], region=p["region"],
        conv=round(conv), income=round(inc), sia=round(sia), ok=ok, h=round(h), w=round(w))
    return dict(conv=conv, g=g, f=f, inc=inc, interest=interest, int_counted=int_counted, work=work, sia=sia, ok=ok,
                amt_h=amt_h, why_h=why_h, amt_w=amt_w, why_w=why_w, h=h, w=w, total=h + w)


def max_house(p):
    """다른 조건이 같을 때 선정기준액 안에 드는 집 공시가격의 최대 (만 원 단위로 내림)."""
    lo, hi = 0, 3_000_000_000
    while hi - lo > 10_000:
        mid = (lo + hi) // 2
        q = dict(p, house=mid)
        conv, _, _ = property_conv(q["region"], q["house"], q["car"], q["debt"], q["deposit"])
        if income_eval(q)[0] + conv <= SEL_COUPLE:
            lo = mid
        else:
            hi = mid
    return lo


def won(x):
    return f"{round(x):,}원"


def main(verbose=False):
    logging.basicConfig(level=logging.INFO, format="%(message)s", stream=sys.stderr)
    log("START", version=VERSION)
    print(f"== 2026 제도 값 (고시 제2026-156호 등) ==")
    print(f"선정기준액 단독 {won(SEL_SINGLE)} · 부부 {won(SEL_COUPLE)} (= 단독 × 160% = {won(SEL_SINGLE * 1.6)})")
    print(f"작년 단독 {won(SEL_SINGLE_2025)} → 올해 {won(SEL_SINGLE)}: {won(SEL_SINGLE - SEL_SINGLE_2025)} 오름")
    print(f"기준연금액 {won(BASE)} · 부부 둘 다 전액이면 {won(BASE * 2 * 0.8)} (한 사람 {won(BASE * 0.8)}, 20% 감액 {won(BASE * 0.2)})")
    print(f"국민연금 연계: 150% = {won(BASE * 1.5)} 이하면 전액 · 200% = {won(BASE * 2)} · 250% = {won(BASE * 2.5)} · 최소(부가연금액) {won(BASE * 0.5)}")
    print(f"재산 1억 원(공제 뒤) → 월 {won(100_000_000 * CONV / 12)} 소득 · 고급차 4,000만 원 → 월 {won(LUX_CAR)} 소득(전부)")
    print(f"근로소득 월 200만 원 → 소득으로 잡히는 돈 {won(work_income(2_000_000))} ((200만 − 116만) × 70%)")
    print(f"기본재산액 {', '.join(f'{k} {v // 10000:,}만' for k, v in BASIC_ASSET.items())} · 금융재산 {FIN_DEDUCT // 10000:,}만 원 제외")

    r = evaluate(EX)
    print(f"\n== 예시 부부 (67세 동갑, 대도시) ==")
    print(f"가정: 집 공시가격 {won(EX['house'])} · 차량가액 {won(EX['car'])} · 대출 {won(EX['debt'])} · 예금 {won(EX['deposit'])}"
          f" (금리 {EX['rate'] * 100:.1f}%) · 국민연금 남편 {won(EX['pen_h'])}·아내 {won(EX['pen_w'])} (합 {won(EX['pen_h'] + EX['pen_w'])}) · 근로소득 없음")
    print(f"1단계 재산: 집 공시가격 {won(EX['house'])} + 차 {won(EX['car'])} = {won(EX['house'] + EX['car'])} − 기본재산액 {won(BASIC_ASSET[EX['region']])} = {won(r['g'])}")
    print(f"          예금 {won(EX['deposit'])} − {won(FIN_DEDUCT)} = {won(r['f'])} → 합 {won(r['g'] + r['f'])} × 4% ÷ 12 = 월 {won(r['conv'])}")
    print(f"2단계 소득: 국민연금 {won(EX['pen_h'])} + {won(EX['pen_w'])} = {won(EX['pen_h'] + EX['pen_w'])}"
          f" + 이자 {won(r['interest'])} − 4만 = {won(r['int_counted'])} → 월 {won(r['inc'])}")
    print(f"3단계 소득인정액: {won(r['inc'])} + {won(r['conv'])} = {won(r['sia'])} vs 부부 기준 {won(SEL_COUPLE)}"
          f" → {'받음' if r['ok'] else '못 받음'} (여유 {won(SEL_COUPLE - r['sia'])})")
    print(f"금액: 아내 {won(r['amt_w'])}({r['why_w']}) × 0.8 = {won(r['w'])} · 남편 {won(r['amt_h'])}({r['why_h']}) × 0.8 = {won(r['h'])}")
    print(f"부부 합계 최소 월 {won(r['total'])} · 1년(12개월) {won(r['total'] * 12)} · 소득역전 확인 {won(r['sia'] + r['total'])} ≤ {won(SEL_COUPLE)}")
    mh = max_house(EX)
    rmh = evaluate(dict(EX, house=mh), tag="경계")
    print(f"다른 조건이 같을 때 대상이 되는 집 공시가격 최대: {won(mh)} (그때 부부 합계 월 {won(rmh['total'])} — 기준에 가까워 줄어듦)")
    log("RESULT", sia=round(r["sia"]), total_min=round(r["total"]), year_min=round(r["total"] * 12), max_house=mh)

    # A급여액을 알면 남편 금액이 얼마나 되나 (대본은 최소만 말함)
    print("\n== 남편 A급여액(소득재분배급여금액)에 따른 남편 기초연금 (부부 감액 뒤) ==")
    for a in (300_000, 400_000, 500_000, 600_000):
        amt, why = linked_amount(EX["pen_h"], a)
        print(f"  A급여 {won(a)} → {won(amt)} × 0.8 = {won(amt * 0.8)} ({why}) · 부부 합계 {won(amt * 0.8 + r['w'])}")

    # 국민연금 구간 예 (한 사람, 부부 감액 전)
    print("\n== 국민연금 월액별 기초연금 (한 사람, 감액 전, A급여 모를 때 최소) ==")
    for pen in (500_000, 524_550, 600_000, 699_400, 800_000, 1_500_000):
        amt, why = linked_amount(pen)
        print(f"  국민연금 {won(pen)} → {won(amt)} ({why})")

    if verbose:
        print("\n== 민감도 (예시 부부에서 하나씩 바꿈) — 받는지·부부 합계 최소·집 공시가격 최대 ==")
        cases = [("기본", {}),
                 ("집 4억", {"house": 400_000_000}), ("집 6억", {"house": 600_000_000}), ("집 7억", {"house": 700_000_000}),
                 ("예금 2천만", {"deposit": 20_000_000}), ("예금 1억", {"deposit": 100_000_000}),
                 ("금리 2.5%", {"rate": 0.025}), ("금리 4.5%", {"rate": 0.045}),
                 ("이자 공제 사람마다", {"int_per_person": True}),
                 ("중소도시", {"region": "중소도시"}), ("농어촌", {"region": "농어촌"}),
                 ("국민연금 남 150만·여 60만", {"pen_h": 1_500_000, "pen_w": 600_000}),
                 ("남편 경비 월 200만 원", {"work_h": 2_000_000}),
                 ("주택담보대출 1억", {"debt": 100_000_000}),
                 ("차 4,500만 원(고급차)", {"car": 45_000_000})]
        for name, ch in cases:
            p = dict(EX, **ch)
            q = evaluate(p, tag=name)
            print(f"  {name:<22} 소득인정액 {won(q['sia']):>12} {'받음' if q['ok'] else '못 받음':<4} 부부 최소 {won(q['total']):>10}"
                  f" · 집 최대 {won(max_house(p))}")
    log("END", version=VERSION)


if __name__ == "__main__":
    main("-v" in sys.argv)
