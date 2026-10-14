"""연금소득 세금 (만 원) — 소득세법 [시행 2026. 7. 1.] [법률 제21221호] 원문으로 확인한 공제·세율 (2026-10-14, checklist.md A표).
VERSION: v1.1 — 2026-10-14 — 설명 고침: 국민연금 과세 몫은 이 파일이 아니라 sim4.py 의 PUB_TAX_SHARE(0.65)로 넣는다 (v1.0 설명의 '전액 과세 가정'은 sim3 v3.1 이전 것)
- 연금소득공제(제47조의2, 한도 900) · 기본세율(제55조) · 기본공제 150·배우자 150·경로우대 100(제50·51조) · 표준세액공제 7(제59조의4 ⑨) · 지방세 10%
- 사적연금 1,500만 원 이하 분리과세 5.5/4.4/3.3%(제129조 ①5의2, 제14조 ③9호), 넘으면 16.5% 분리 또는 종합 중 선택(제64조의4)
연구·교육용 예시 계산 — 세무 상담이 아님."""
def pension_deduction(total):                 # 연금소득공제 (한도 900)
    if total <= 350: d = total
    elif total <= 700: d = 350 + (total - 350) * 0.4
    elif total <= 1400: d = 490 + (total - 700) * 0.2
    else: d = 630 + (total - 1400) * 0.1
    return min(d, 900)

def income_tax(base):                         # 종합소득세 기본세율 (2023~), 지방세 별도
    br = [(1400, .06, 0), (5000, .15, 126), (8800, .24, 576), (15000, .35, 1544), (30000, .38, 1994)]
    for top, r, sub in br:
        if base <= top: return max(base * r - sub, 0)
    return base * .40 - 2594

def global_tax(pension_total, age, spouse_ok):
    inc = pension_total - pension_deduction(pension_total)
    ded = 150 + (150 if spouse_ok else 0) + (100 if age >= 70 else 0)
    t = income_tax(max(inc - ded, 0))
    t = max(t - 7, 0) if t > 0 else 0       # 표준세액공제
    return t * 1.1                          # 지방소득세 포함

def sep_rate(age):
    return 0.055 if age < 70 else 0.044 if age < 80 else 0.033

def private_pension_tax(x, public, age, spouse_ok):
    """사적연금(퇴직금 몫 제외) x 를 꺼낼 때 늘어나는 세금 — 고를 수 있는 것 중 싼 쪽."""
    if x <= 0: return 0.0, "-"
    inc_global = global_tax(public + x, age, spouse_ok) - global_tax(public, age, spouse_ok)
    sep = x * (sep_rate(age) if x <= 1500 else 0.165)
    return (sep, "분리") if sep <= inc_global else (inc_global, "종합")

if __name__ == "__main__":
    for x in (1500, 1501, 1800):
        s = 1500 >= x
        print(x, "남편(국민연금 1,320)", [round(v, 1) if isinstance(v, float) else v for v in private_pension_tax(x, 1320, 65, True)],
              "16.5%" if x > 1500 else "5.5%", round(x * (0.055 if x <= 1500 else 0.165), 1),
              "종합", round(global_tax(1320 + x, 65, True) - global_tax(1320, 65, True), 1))
    print("국민연금만 1,320 세금", round(global_tax(1320, 65, True), 1), "아내 480", round(global_tax(480, 65, False), 1))
    for x in (1500, 1501):
        print(x, "다른 소득 없는 사람", [round(v, 1) if isinstance(v, float) else v for v in private_pension_tax(x, 0, 65, False)])
