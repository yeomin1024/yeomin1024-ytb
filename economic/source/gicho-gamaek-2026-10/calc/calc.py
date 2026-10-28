#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""국민연금 때문에 깎이는 기초연금 — 국민연금이 늘면 합계는 어떻게 되나 (요약본 숫자 계산, 단위: 원)

VERSION: v0.1 — 2026-10-28 — 최초 (요약본 단계 — 대본 단계에서 v1.0 으로 넓힘). 주제 T007 (economic/topics/주제탐색.md).
  사용자 지시 2026-10-28 "주식 주제 관련 세션에서 했던것처럼 똑같은 방식으로 진행해서 유튜브 분석부터 요약본까지 만들어봐".
  - 국민연금 중 소득재분배급여(A급여)가 늘 때 기초연금·합계 — 감액이 시작되는 선 · 바닥 · 1만 원당 변화 · 부부 감액

법 (legalize-kr, 2026-10-28 에 시행 중인 판 — `tools/law_text.py 기초연금법 --source auto`):
  - 기초연금법 [시행 2025-10-01] [제21065호] 제5조 ⑤ 국민연금 수급권자 기초연금액 = max(0, 기준연금액 − 소득재분배급여금액 × 2/3) + 부가연금액(기준연금액의 1/2)
      제7조 기준연금액을 넘으면 기준연금액 · 제8조 ① 부부 모두 수급권자면 각각 20% 감액 · ② 소득인정액 + 기초연금액이 선정기준액 이상이면 넘는 범위에서 감액(대본 단계)
  - 2026년 기준연금액 349,700원 — economic/source/gicho-yeongeum-2026-10/checklist.md (보건복지부 고시, 2026-10-14 확인)
가정 (예시): 국민연금 중 A급여 몫은 가입 이력마다 다름 → 이 계산은 A급여 금액으로 표를 만듦 (대본 단계에서 사례 부부의 A급여를 국민연금법 제51조로 계산).
연구·교육용 예시 계산 — 연금 상담·권유 아님. 실제 금액은 국민연금공단·주민센터 결정이 기준.

실행:  cd economic/source/gicho-gamaek-2026-10/calc && python3 calc.py   (숫자 stdout · 로그 stderr)
로그:  [STAGE] [시각] key=value
"""
import argparse
import logging
import sys
import time
from datetime import datetime, timezone

VERSION = "v0.1"
LOG = logging.getLogger("calc")
BASE = 349_700                # 2026년 기준연금액 (원)
EXTRA = BASE / 2              # 부가연금액 (제5조 ⑤3호)
COUPLE_CUT = 0.20             # 제8조 ① 부부 감액


def log(stage, **kv):
    LOG.info("[%s] [%s] %s", stage, datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S"), " ".join(f"{k}={v}" for k, v in kv.items()))


def basic(a_benefit, couple=False):
    """기초연금액 (원) — 제5조 ⑤ · 제7조 한도 · (부부면) 제8조 ① 20% 감액."""
    amt = min(BASE, max(0.0, BASE - a_benefit * 2 / 3) + EXTRA)
    return amt * (1 - COUPLE_CUT) if couple else amt


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args(argv)
    logging.basicConfig(level=a.log_level, format="%(message)s", stream=sys.stderr)
    t0 = time.monotonic()
    log("START", tool=f"calc.py {VERSION}", base=BASE, extra=EXTRA)
    start = BASE * 3 / 4          # 여기부터 깎임: BASE − 2/3·A + BASE/2 < BASE  ⇔  A > 3/4·BASE
    floor = BASE * 3 / 2          # 여기서 바닥: BASE − 2/3·A ≤ 0  ⇔  A ≥ 1.5·BASE
    print(f"- 감액이 시작되는 A급여: {start:,.0f}원 (기준연금액의 4분의 3) · 바닥이 되는 A급여: {floor:,.0f}원 (기준연금액의 150%)")
    print(f"- 바닥(부가연금액): 한 사람 {EXTRA:,.0f}원 · 부부 각자 {EXTRA * (1 - COUPLE_CUT):,.0f}원 (부부 감액 20%)")
    print(f"- 기준연금액 전액: 한 사람 {BASE:,.0f}원 · 부부 각자 {BASE * (1 - COUPLE_CUT):,.0f}원")
    print("\n| A급여 (월) | 기초연금 (한 사람) | 국민연금 A급여 + 기초연금 | A급여 1만 원 늘 때 합계 변화 |")
    print("|---|---|---|---|")
    min_gain = None
    for a_ in (0, 200_000, 262_275, 300_000, 400_000, 524_550, 600_000):
        b, b2 = basic(a_), basic(a_ + 10_000)
        gain = (a_ + 10_000 + b2) - (a_ + b)
        min_gain = gain if min_gain is None else min(min_gain, gain)
        print(f"| {a_:,} | {b:,.0f} | {a_ + b:,.0f} | {gain:+,.0f} |")
        log("CALC", a_benefit=a_, basic=round(b), total=round(a_ + b), gain_per_10k=round(gain))
    print(f"\n- 국민연금(A급여)이 1만 원 늘 때 합계가 가장 적게 느는 경우: {min_gain:+,.0f}원 — 0원보다 크므로 '더 받는 쪽이 이득'")
    log("DECIDE", rule="A급여 1만 원 증가당 합계 변화 > 0 이면 '국민연금을 더 받는 쪽이 이득'", min_gain=round(min_gain), verdict="더 받는 쪽" if min_gain > 0 else "덜 받는 쪽")
    log("DONE", seconds=round(time.monotonic() - t0, 3))
    return 0


if __name__ == "__main__":
    sys.exit(main())
