# VERSION: v1.0 — 2026-11-23 — ADHD A씨 vs B씨 대본 숫자 계산 (사용자 지시 "사실 확인 남은 거 먼저 해봐")
# CHANGELOG
# - v1.0 (2026-11-23): 첫 판. 성인·30대 여성 진료 인원 배수(2020→2025), BMJ 2025 첫 사건 감소율을 계산해 대본 문장과 맞춤.
"""대본 숫자는 이 파일의 출력만 쓴다 (CLAUDE.md '숫자는 계산 코드 출력만').

입력값은 모두 보도·논문에 적힌 그대로이며 출처는 SOURCES 에 둔다.
교육·정보용 계산일 뿐 의학적 진단·처방이 아니다.

실행: python3 psychology/source/adhd-ab-2026-11/calc_numbers.py [--log-level DEBUG]
"""
import argparse
import logging

LOG = logging.getLogger("adhd_calc")

# 국민건강보험공단 진료 인원 (ADHD, 20세 이상 = 성인) — 같은 공단 자료를 두 의원실이 해마다 공개
NHIS = {
    "adult_2020": 25_297,     # 남인순 의원실 (2025-09 공개, 2020~2024)
    "adult_2024": 122_614,    # 같은 자료
    "adult_2025": 152_675,    # 권칠승 의원실 (2026-09-28 공개, 2020~2025)
    "f30_2020": 2_325,        # 30대 여성 — 두 공개 자료 모두 2,325명
    "f30_2024": 20_624,       # 남인순 의원실
    "f30_2025": 27_076,       # 권칠승 의원실
    "age30_2020_a": 6_194,    # 30대 전체 (남인순) — 두 자료가 같은 묶음인지 확인용
    "age30_2020_b": 6_194,    # 30대 전체 (권칠승)
    "total_2025": 317_964,    # 전체 (권칠승)
}

# BMJ 2025;390:e083658 (Zhang L 등, 스웨덴 등록 자료, 6~64세 14만 8,581명, 진단 3개월 안 약 시작 vs 안 함, 2년)
# 첫 사건 비율비(IRR) — 1에서 뺀 값이 '적었다' 비율
BMJ_FIRST_IRR = {"자살 시도 같은 행동": 0.83, "약물 오남용": 0.85, "교통사고": 0.88, "범죄": 0.87}
BMJ_N = 148_581

SOURCES = {
    "adult_2020/2024, f30_2024": "헤럴드경제 2025-10-07 · 쿠키뉴스 kuk202509290119 (남인순 의원실, 건보공단)",
    "adult_2025, f30_2025, total_2025": "메디칼타임즈 ID=1170897 · 베이비뉴스 idxno=154822 (권칠승 의원실, 건보공단, 2026-09-28)",
    "BMJ": "doi 10.1136/bmj-2024-083658 · BMJ Group·카롤린스카 보도자료 · Epocrates 요약(범죄 65.1 vs 76.1, IRR 0.87)",
}


def ratio(a, b):
    """b ÷ a — 몇 배 늘었나."""
    if a <= 0:
        raise ValueError(f"기준값이 0 이하: {a}")
    return b / a


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    args = ap.parse_args()
    logging.basicConfig(level=args.log_level, format="[%(name)s] %(message)s")

    # 두 의원실 자료가 같은 묶음인지 — 2020년 30대·30대 여성이 같아야 섞어 써도 됨
    same = NHIS["age30_2020_a"] == NHIS["age30_2020_b"]
    LOG.info("[CHECK] 2020 30대 남인순=%s 권칠승=%s → 같은 묶음=%s", NHIS["age30_2020_a"], NHIS["age30_2020_b"], same)
    if not same:
        LOG.warning("[CHECK] 두 자료의 2020년 값이 다름 — 성인 2020→2025 배수를 쓰지 말 것")
    share = NHIS["adult_2025"] / NHIS["total_2025"]
    LOG.info("[CHECK] 2025 성인 비중 = %.1f%% (보도 48.0%%)", share * 100)

    a24 = ratio(NHIS["adult_2020"], NHIS["adult_2024"])
    a25 = ratio(NHIS["adult_2020"], NHIS["adult_2025"])
    f24 = ratio(NHIS["f30_2020"], NHIS["f30_2024"])
    f25 = ratio(NHIS["f30_2020"], NHIS["f30_2025"])
    LOG.info("[CALC] 성인 2020→2024 = %.2f배 (옛 대본 '4년 사이 5배 가까이')", a24)
    LOG.info("[CALC] 성인 2020→2025 = %.2f배 → 대본 '5년 사이 6배 넘게'", a25)
    LOG.info("[CALC] 30대 여성 2020→2024 = %.2f배 (옛 대본 8.87배)", f24)
    LOG.info("[CALC] 30대 여성 2020→2025 = %.2f배 → 대본 '11.6배'", f25)
    assert a25 > 6.0, "‘6배 넘게’가 틀림"
    assert round(f25, 1) == 11.6, "‘11.6배’가 틀림"

    for k, irr in BMJ_FIRST_IRR.items():
        LOG.info("[CALC] BMJ 첫 사건 %s IRR %.2f → %d%% 적음", k, irr, round((1 - irr) * 100))
    LOG.info("[CALC] BMJ 대상 %s명 → 대본 '14만 8천여 명'", f"{BMJ_N:,}")
    for k, v in SOURCES.items():
        LOG.debug("[SOURCE] %s — %s", k, v)


if __name__ == "__main__":
    main()
