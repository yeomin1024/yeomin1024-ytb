#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""연금저축·IRP 55세부터 받을 때 — 나눠 받기 vs 몰아 받기 세금 (요약본 숫자 계산, 단위: 만 원)

VERSION: v0.1 — 2026-10-28 — 최초 (요약본 단계 — 대본 단계에서 v1.0 으로 넓힘). 주제 T012 (economic/topics/주제탐색.md).
  사용자 지시 2026-10-28 "주식 주제 관련 세션에서 했던것처럼 똑같은 방식으로 진행해서 유튜브 분석부터 요약본까지 만들어봐".
  - 같은 1억 2천만 원을 A '10년 나눠 연 1,200만 원' · B '5년 몰아 연 2,400만 원 — 16.5% 분리과세' · C '5년 몰아 — 종합과세(다른 소득 없음)'

법 (legalize-kr, 2026-10-28 에 시행 중인 판 — `tools/law_text.py 소득세법 --source auto`):
  - 소득세법 [시행 2026-04-21] [제21548호]
      제14조 ③9호 다목 — 사적연금(연금계좌) 연금소득 합계가 연 1,500만 원 이하이면 분리과세 (종합소득에 넣지 않음)
      제129조 ①5의2 가목 — 연금수령 원천징수 70세 미만 5% · 70~80세 4% · 80세 이상 3%
      제64조의4 — 1,500만 원을 넘으면 '종합과세' 와 '그 연금소득 × 15% 분리' 중 고름
      제47조의2 연금소득공제 (350만 이하 전액 · 700만 이하 350 + 40% · 1,400만 이하 490 + 20% · 넘으면 630 + 10%, 최대 900만 원)
      제55조 기본세율 1,400만 원 이하 6% · 5,000만 원 이하 84만 + 15% · 제50조 기본공제 1명 150만 원
  - 지방소득세 = 소득세의 10% (5% → 5.5%, 15% → 16.5%)
가정 (예시): 57세 퇴직자, 연금저축·IRP 평가액 1억 2천만 원 (모두 세액공제 받은 돈과 수익 — 과세 대상), 국민연금은 65세부터라 받는 동안 다른 소득 없음,
  배우자 공제·그 밖 공제 없음. 연금수령한도(시행령 제40조의7)는 대본 단계에서 확인. 운용 수익은 넣지 않음.
연구·교육용 예시 계산 — 세무·투자 권유 아님.

실행:  cd economic/source/yeonjeo-suryeong-2026-10/calc && python3 calc.py   (숫자 stdout · 로그 stderr)
로그:  [STAGE] [시각] key=value
"""
import argparse
import logging
import sys
import time
from datetime import datetime, timezone

VERSION = "v0.1"
LOG = logging.getLogger("calc")
TOTAL = 12_000            # 꺼낼 돈 (만 원)
SEP_LIMIT = 1_500         # 제14조 ③9호 다목
RATE_UNDER70 = 0.05       # 제129조 ①5의2 가목
RATE_SEP = 0.15           # 제64조의4
LOCAL = 0.10
BASIC = 150               # 제50조 기본공제


def log(stage, **kv):
    LOG.info("[%s] [%s] %s", stage, datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S"), " ".join(f"{k}={v}" for k, v in kv.items()))


def pension_deduction(x):
    """제47조의2 연금소득공제 (만 원)."""
    if x <= 350:
        d = x
    elif x <= 700:
        d = 350 + (x - 350) * 0.40
    elif x <= 1400:
        d = 490 + (x - 700) * 0.20
    else:
        d = 630 + (x - 1400) * 0.10
    return min(d, 900)


def basic_tax(base):
    """제55조 기본세율 (만 원) — 이 예시 범위(8,800만 원 이하)."""
    if base <= 1400:
        return base * 0.06
    if base <= 5000:
        return 84 + (base - 1400) * 0.15
    return 624 + (base - 5000) * 0.24


def tax_split(per_year):
    """연 1,500만 원 이하 — 분리과세 5% (+지방 10%)."""
    return per_year * RATE_UNDER70 * (1 + LOCAL)


def tax_sep15(per_year):
    return per_year * RATE_SEP * (1 + LOCAL)


def tax_global(per_year):
    """다른 소득이 없을 때 종합과세 — 연금소득공제 · 기본공제 · 기본세율 (+지방 10%). 원천징수 5% 는 정산되므로 결과만."""
    income = per_year - pension_deduction(per_year)
    base = max(0.0, income - BASIC)
    return basic_tax(base) * (1 + LOCAL)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args(argv)
    logging.basicConfig(level=a.log_level, format="%(message)s", stream=sys.stderr)
    t0 = time.monotonic()
    log("START", tool=f"calc.py {VERSION}", total=TOTAL, sep_limit=SEP_LIMIT)
    rows = []
    for name, years, fn in (("A 10년 나눠 (연 1,200만)", 10, tax_split), ("B 5년 몰아 — 16.5% 분리", 5, tax_sep15),
                            ("C 5년 몰아 — 종합과세 (다른 소득 없음)", 5, tax_global), ("D 8년 나눠 (연 1,500만)", 8, tax_split)):
        per = TOTAL / years
        if fn is tax_split and per > SEP_LIMIT:
            log("CHECK", plan=name, warning="연 1,500만 원을 넘어 분리과세 5% 를 쓸 수 없음")
            continue
        t = fn(per)
        rows.append((name, years, per, t, t * years))
        print(f"- {name}: 해마다 {per:,.0f}만 원 · 세금 해마다 {t:,.1f}만 원 · {years}년 합계 {t * years:,.0f}만 원 (실효 {t / per:.1%})")
        log("CALC", plan=name.split()[0], years=years, per_year=round(per), tax_year=round(t, 1), tax_total=round(t * years))
    best = min(rows, key=lambda r: r[4])
    print(f"\n- 세금이 가장 적은 길: {best[0]} — {best[4]:,.0f}만 원")
    a_, b_ = rows[0][4], rows[1][4]
    print(f"- A(나눠) vs B(몰아 16.5%): {b_ - a_:,.0f}만 원 차이")
    log("DECIDE", rule="10년(또는 더 길게) 세금 합계가 가장 작은 길", verdict=best[0].split()[0], best_total=round(best[4]))
    log("DONE", seconds=round(time.monotonic() - t0, 3))
    return 0


if __name__ == "__main__":
    sys.exit(main())
