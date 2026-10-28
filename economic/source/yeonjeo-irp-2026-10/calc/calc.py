#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""연금저축 600만 원 + IRP 300만 원 — 넣는 순서에 따른 연말정산 환급 (요약본 숫자 계산, 단위: 만 원)

VERSION: v0.1 — 2026-10-28 — 최초 (요약본 단계 — 대본 단계에서 v1.0 으로 넓힘). 주제 T003 (economic/topics/주제탐색.md).
  사용자 지시 2026-10-28 "주식 주제 관련 세션에서 했던것처럼 똑같은 방식으로 진행해서 유튜브 분석부터 요약본까지 만들어봐".
  - A '연금저축에만 900만 원' vs B '연금저축 600만 + IRP 300만 원' vs C '연금저축 600만 원만' — 해마다 환급·10년 합계

법 (legalize-kr, 2026-10-28 에 시행 중인 판 — `tools/law_text.py 소득세법 --source auto`):
  - 소득세법 [시행 2026-04-21] [제21548호] 제59조의3 ① 연금계좌 납입액의 12% (종합소득금액 4,500만 원 이하 · 근로소득만 있으면 총급여 5,500만 원 이하는 15%)
      — 연금저축계좌 연 600만 원 넘는 몫은 없는 것 · 연금저축 600만 원 안 + 퇴직연금계좌(IRP) 합계 연 900만 원 넘는 몫도 없는 것
  - 지방세법 제103조의13 — 지방소득세 = 소득세의 10% → 공제율 12% → 13.2%, 15% → 16.5% (화면·대본 표기)
  - 세액공제는 결정세액(산출세액)을 넘어 돌려주지 않는다 — 결정세액이 작으면 환급이 줄어듦 (주제 T002, 대본 단계에서 사례 계산)
가정 (예시): 직장인 둘 — 총급여 4,800만 원(15%) · 7,000만 원(12%), 결정세액은 공제액보다 크다고 봄, 10년 같은 금액.
연구·교육용 예시 계산 — 세무·투자 권유 아님.

실행:  cd economic/source/yeonjeo-irp-2026-10/calc && python3 calc.py   (숫자 stdout · 로그 stderr)
로그:  [STAGE] [시각] key=value
"""
import argparse
import logging
import sys
import time
from datetime import datetime, timezone

VERSION = "v0.1"
LOG = logging.getLogger("calc")
RATE_LOW, RATE_HIGH = 0.15, 0.12          # 제59조의3 ① (총급여 5,500만 원 이하 15% · 넘으면 12%)
LOCAL = 0.10                             # 지방소득세 = 소득세의 10%
LIMIT_PENSION, LIMIT_TOTAL = 600, 900    # 연금저축 한도 · 연금저축 + IRP 합계 한도 (만 원)
YEARS = 10


def log(stage, **kv):
    LOG.info("[%s] [%s] %s", stage, datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S"), " ".join(f"{k}={v}" for k, v in kv.items()))


def credit_base(pension, irp):
    """공제 대상 금액 — 연금저축은 600만 원까지, 연금저축(600 안) + IRP 는 900만 원까지."""
    p = min(pension, LIMIT_PENSION)
    return min(p + irp, LIMIT_TOTAL)


def refund(pension, irp, rate):
    """해마다 돌려받는 돈 (지방소득세 포함, 만 원) — 결정세액이 충분하다고 봄."""
    return round(credit_base(pension, irp) * rate * (1 + LOCAL), 2)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args(argv)
    logging.basicConfig(level=a.log_level, format="%(message)s", stream=sys.stderr)
    t0 = time.monotonic()
    log("START", tool=f"calc.py {VERSION}", years=YEARS, limits=f"{LIMIT_PENSION}/{LIMIT_TOTAL}")
    plans = {"A 연금저축 900": (900, 0), "B 연금저축 600 + IRP 300": (600, 300), "C 연금저축 600": (600, 0)}
    out = {}
    for label, rate in (("총급여 4,800만 원 (15% → 16.5%)", RATE_LOW), ("총급여 7,000만 원 (12% → 13.2%)", RATE_HIGH)):
        print(f"\n## {label}")
        for name, (p, i) in plans.items():
            r = refund(p, i, rate)
            out[(label, name)] = r
            print(f"- {name}: 넣은 돈 {p + i}만 원 · 공제 대상 {credit_base(p, i)}만 원 · 해마다 환급 {r:.1f}만 원 · {YEARS}년 {r * YEARS:,.0f}만 원")
            log("CALC", case=label.split()[1], plan=name.split()[0], paid=p + i, base=credit_base(p, i), refund=r)
        a_, b_ = out[(label, "A 연금저축 900")], out[(label, "B 연금저축 600 + IRP 300")]
        print(f"- 차이 B − A: 해마다 {b_ - a_:.1f}만 원 · {YEARS}년 {(b_ - a_) * YEARS:,.0f}만 원 (같은 900만 원을 넣고도)")
        log("DECIDE", case=label.split()[1], rule="B 환급 > A 환급 이면 'IRP 300 먼저'", diff=round(b_ - a_, 2), verdict="B" if b_ > a_ else "같음")
    log("DONE", seconds=round(time.monotonic() - t0, 3))
    return 0


if __name__ == "__main__":
    sys.exit(main())
