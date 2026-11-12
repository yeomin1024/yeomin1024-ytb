# VERSION: v1.0 — 2026-11-12 — 대본 숫자 2개 계산 (하루 출동 건수, 4명 중 1명)
"""python3 crisis/source/ellibeiteo-gathim-2026-11/calc/calc.py
근거: 소방청 승강기 사고 구조출동 2023년 40,940건 (중부일보 보도) · 2024년 승강기 사고 구조인원 28,598명 = 전체 구조인원의 24.9% (소방청 2024 소방활동 분석 보도)
"""
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.getLogger("calc")


def L(stage, **kv):
    log.info(f"[{stage}] [{datetime.now():%Y-%m-%dT%H:%M:%S}] " + " ".join(f"{k}={v}" for k, v in kv.items()))


dispatch_2023, days_2023 = 40_940, 365          # 2023년은 윤년 아님
per_day = dispatch_2023 / days_2023
L("CALC", item="하루 평균 출동", dispatch_2023=dispatch_2023, days=days_2023, per_day=round(per_day, 1),
  script="하루에 110건이 넘는 셈입니다", ok=per_day > 110)

rescued_2024, share_2024 = 28_598, 0.249
total_rescued = rescued_2024 / share_2024
L("CALC", item="4명 중 1명", rescued_2024=rescued_2024, share=share_2024, implied_total=round(total_rescued),
  one_in=round(1 / share_2024, 2), script="119가 구조한 사람 4명 중 1명", ok=abs(1 / share_2024 - 4) < 0.1)
