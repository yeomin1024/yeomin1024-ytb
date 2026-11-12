# VERSION: v1.0 — 2026-11-12 — 대본 숫자 계산 (환급까지 최소 기간, 10명 중 7명)
"""python3 crisis/source/pon-kkaejyeosseo-2026-11/calc/calc.py
근거: 전기통신금융사기 피해 방지 및 피해금 환급에 관한 특별법 (시행 2026-10-02, 법률 제22047호, legalize-kr 미러 원문)
  제5조 채권소멸절차 개시 공고 요청(지체 없이) · 제9조 최초 공고일부터 2개월 지나면 채권 소멸 · 제10조 소멸일부터 14일 안에 환급금 결정
  피해자 연령: 경찰청 2025년 1~7월 메신저피싱 피해자 3,950명 중 60대·70대 이상 72% (이상휘 의원실, 보도)
"""
import logging
from datetime import date, timedelta

logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.getLogger("calc")


def L(stage, **kv):
    from datetime import datetime
    log.info(f"[{stage}] [{datetime.now():%Y-%m-%dT%H:%M:%S}] " + " ".join(f"{k}={v}" for k, v in kv.items()))


def add_months(d: date, m: int) -> date:
    y, mo = divmod(d.month - 1 + m, 12)
    return d.replace(year=d.year + y, month=mo + 1)


# 가장 빠른 경우: 지급정지 당일 공고(지체 없이 → 0일로 가정, 실제로는 더 걸림)
notice = date(2026, 1, 1)                         # 날짜는 계산용 예시 — 결과는 날수만 씀
extinct = add_months(notice, 2)                   # 제9조: 공고일부터 2개월
decide = extinct + timedelta(days=14)             # 제10조: 소멸일부터 14일 안
days = (decide - notice).days
L("CALC", item="환급금 결정까지 최소", notice=notice, extinct=extinct, decide=decide, days=days,
  months=round(days / 30.4, 2), script="빨라도 두 달 반쯤", ok=2.3 <= days / 30.4 <= 2.6,
  note="공고 요청까지의 시간·이의제기·실제 입금 날짜는 넣지 않음 → 실제로는 더 김")

victims, share60 = 3_950, 0.72
L("CALC", item="60대 이상 비율", victims=victims, share=share60, of10=round(share60 * 10, 1),
  script="10명 중 7명이 60대 이상", ok=round(share60 * 10) == 7)
