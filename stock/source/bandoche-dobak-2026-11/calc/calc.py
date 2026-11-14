#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.3 — 2026-11-14 — 대본 v6(사용자 도입 · 리스크 자세히) 보도 숫자 더함: 메가스피드 48억 달러·24만 개 · 시게이트 3억 달러(2023) · 수출 통제 일곱 나라 · 싱가포르 청구 20% · HBM 3분의 2 · 미국 반도체 지수 3.43%
# (v1.2 — 2026-11-14 — 반론 3회차: 나눠 사기 예(600만 원 ÷ 6개월) · 물타기 손실률(28% vs 36%) 출력
# (v1.1 — 2026-11-14 — 반론 1회차 반영: 물타기 뒤 움직임 ±30% → ±20% (코스피 한 달 28% 와 같은 잣대 — 앞으로 한 달 움직임) · 2배 왕복 -20/+25 → 하루 -10%·다음 날 +10% (하루 단위 조건을 대본에 밝힘) · 엔비디아 하루 흔들림은 대본에서 뺌(숫자 유지)
# (v1.0 — 2026-11-14 — 최초 (사용자 지시 2026-11-14 "현재 반도체 주식에 투자하는건 도박이잖아 … 그 흐름으로 대본 만들어서 파일로 줘봐").
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.3 | 2026-11-14 | FACTS 8개 더함 (대본 v6·v7 — 시게이트 5년 조건 포함) | FACTS |
# | v1.2 | 2026-11-14 | split_example · averaging_down 손실률 | GIVEN·averaging_down·main |
# | v1.1 | 2026-11-14 | next_move 0.30→0.20 · lev_down/up 0.20/0.25 → 0.10/0.10 · assert 새 값 | GIVEN·main |
# | v1.0 | 2026-11-14 | 물타기 손익 · 본전 회복에 필요한 상승률 · 2배 상품 제자리 손해 · 코스피 하락률 · 엔비디아 하루 흔들림 · 보도 숫자(출처)를 result.json 에 | averaging_down·recovery·leverage_round_trip·pct_change·main |
#
# 대본 bandoche-dobak-2026-11.txt 의 숫자는 이 출력(result.json)만 쓴다.
#   계산 숫자 = 아래 함수 (가정은 GIVEN 에 — 20% 는 가정, 근거는 코스피 10월 초 → 11월 9일 하락률).
#   보도 숫자 = FACTS (2026-11-14 검색 결과 요약 — 이 환경에선 기사 사이트가 막혀 원문을 못 엶 → checklist.md '확인 필요').
# 로그: [STAGE] [시각] key=value (START · GIVEN · CALC · FACTS · WRITE · DONE). 무작위 없음 (seed 불필요). 세금·수수료 없음.
# ※ 연구·교육용 — 투자 권유가 아님.
from __future__ import annotations

import json
import logging
import sys
import time
from pathlib import Path

VERSION = "v1.3"
HERE = Path(__file__).resolve().parent
LOG = logging.getLogger("calc")

GIVEN = {
    "first_buy_won": 10_000_000,      # 처음 매수 1,000만 원 (예시)
    "first_drop": 0.20,               # 처음 하락 20% (예시)
    "add_won": 10_000_000,            # 물타기 1,000만 원 (예시 — 처음과 같은 금액)
    "next_move": 0.20,                # 그 뒤 ±20% (가정 — 근거: 코스피 한 달 남짓 -27.83%, 같은 한 달 잣대)
    "recovery_drop": 0.40,            # 10월 2배 상품 평균 -39.99% 를 반올림한 40%
    "lev_down": 0.10, "lev_up": 0.10, # 2배 상품 왕복 예: 기초 주가 하루 -10% → 다음 날 +10%
    "leverage": 2.0,
    "split_total_won": 6_000_000,     # 나눠 사기 예: 사기로 정한 금액
    "split_months": 6,                # 여섯 달에 나눔
}

FACTS = [  # (key, 값, 단위, 무엇, 출처) — 대본 문장과 짝은 checklist.md
    ("nvda_open_drop_pct", 14, "%", "퇴진 발표일(미국 11-12) 엔비디아 장 초반 하락", "https://www.fnnews.com/news/202611122331487035"),
    ("nvda_close_drop_pct", 4.34, "%", "같은 날 종가 하락", "https://www.cnbc.com/2026/11/12/nvidia-nvda-jensen-huang-second-affair.html"),
    ("nvda_month_drop_pct", 20, "%", "그 전 한 달 하락 ('more than 20%')", "https://www.cnbc.com/2026/11/12/nvidia-nvda-jensen-huang-second-affair.html"),
    ("years_at_nvidia", 33, "년", "33년 만에 퇴진", "https://www.hankyung.com/article/2026111339411"),
    ("hynix_1113_drop_pct", 3.03, "%", "11-13 한국 SK하이닉스 하락 (121만 6천 원)", "검색 요약 — 기사 확인 필요 (blockmedia/wowtv 추정)"),
    ("samsung_1113_drop_pct", 0.96, "%", "11-13 한국 삼성전자 하락 (20만 6천 원)", "검색 요약 — 기사 확인 필요"),
    ("megaspeed_usd_100m", 48, "억 달러 넘게", "메가스피드가 2년 동안 산 엔비디아 칩 (뉴욕타임스)", "https://www.cbsnews.com/news/nvidia-jensen-huang-investigation-china-intelligence/"),
    ("chips_banned_count_10k", 24, "만 개", "중국 수출 금지 칩 24만 개 의혹 (수사 당국)", "https://www.cbsnews.com/news/nvidia-jensen-huang-investigation-china-intelligence/"),
    ("seagate_fine_usd_100m", 3, "억 달러", "2023 시게이트 화웨이 수출 위반 벌금 — 상무부 단독 최대 · 순이익 두 배 넘게", "https://stblaw.com/about-us/publications/view/2023/04/28/bis-imposes-$300m-fine-largest-penalty-ever-against-seagate-for-violating-huawei-foreign-direct-product-rule"),
    ("seagate_denial_order_years", 5, "년", "시게이트 합의 — 5년 수출 금지 명령 유예(어기면 발동)", "https://stblaw.com/about-us/publications/view/2023/04/28/bis-imposes-$300m-fine-largest-penalty-ever-against-seagate-for-violating-huawei-foreign-direct-product-rule"),
    ("export_rule_countries", 7, "나라", "AI 칩 수출 통제 대상에 더한다는 나라 (싱가포르·말레이시아·태국·인도네시아·브라질·노르웨이·남아공 — 보도, 확정 전)", "https://en.sedaily.com/world/2026/11/12/us-set-to-tighten-ai-chip-export-curbs-on-singapore"),
    ("nvda_singapore_bill_pct", 20, "%", "엔비디아 FY2026 1분기(2025-02~04) 매출 중 싱가포르 청구 몫 — 청구지 기준 (검색 요약: 공시 인용)", "https://fourweekmba.com/ai-chip-export-rules-explained-nvidia-billed-52b-to-singapore/ — 10-Q 원문 확인 필요"),
    ("hynix_nvda_hbm4_share", "3분의 2", "", "엔비디아 차세대(베라 루빈) HBM4 물량 중 SK하이닉스 몫 (보도)", "https://m.news.nate.com/view/20260128n33368"),
    ("h200_china_approval", "2025-12", "", "몇 달 로비 끝에 트럼프가 H200 중국 판매 허가 (25% 몫)", "https://www.pbs.org/newshour/world/trump-approves-sale-of-more-advanced-nvidia-computer-chips-used-in-ai-to-china"),
    ("sox_1113_drop_pct", 3.43, "%", "11-13 미국 필라델피아 반도체지수 하락", "검색 요약 — 기사 확인 필요"),
    ("samsung_1110_open_pct", 5, "%", "11-10 삼성전자 시초가 상승 (5.00%)", "https://www.fnnews.com/news/202611101041161898"),
    ("hynix_1110_open_pct", 6.87, "%", "11-10 SK하이닉스 시초가 상승", "https://www.fnnews.com/news/202611101041161898"),
    ("chips_diverted_usd_100m", 75, "억 달러", "중국 등으로 넘어갔다는 칩 (보도 — '최소')", "검색 요약 — 한국 보도 (hankyung/fnnews/nate 중) 확인 필요"),
    ("chips_diverted_krw_jo", 10, "조 원", "위 금액의 원화 (보도 '약 10조원')", "검색 요약 — 확인 필요"),
    ("house_committees", 3, "곳", "젠슨 황을 부른 하원 위원회", "https://www.cnn.com/2026/11/11/business/live-news/nvidia-jensen-huang-investigation-fallout"),
    ("foreign_sell_2days_jo", 6, "조 원 넘게", "11월 초 폭락 이틀 외국인 순매도 (6조 1,620억 원)", "https://m.news.nate.com/view/20261106n23018"),
    ("kospi_crash_day_pct", 8, "% 넘게", "11월 초 코스피 장중 하락 → 서킷브레이커", "https://m.news.nate.com/view/20261106n23018"),
    ("kospi_oct_start", 6971.35, "pt", "10월 초 코스피", "https://www.fnnews.com/news/202611091833468507"),
    ("kospi_1109", 5031.48, "pt", "11-09 코스피", "https://www.fnnews.com/news/202611091833468507"),
    ("lev_etf_count", 14, "종", "삼성전자·SK하이닉스 2배 상품 수", "검색 요약 — 아주경제·서울경제TV·딜사이트 중 확인 필요"),
    ("lev_etf_oct_avg_pct", -39.99, "%", "10월 한 달 2배 상품 14종 평균 수익률", "검색 요약 — 확인 필요"),
]


def log(stage: str, **kv) -> None:
    LOG.info("[%s] [%s] %s", stage, time.strftime("%Y-%m-%dT%H:%M:%S"), " ".join(f"{k}={v}" for k, v in kv.items()))


def averaging_down(first: int, drop: float, add: int, move: float) -> dict:
    """물타기 했을 때와 안 했을 때 — 그 뒤 move 만큼 오르거나 내렸을 때 계좌 값·손익 (원)."""
    after_drop = first * (1 - drop)
    out = {"after_drop": round(after_drop)}
    for name, m in (("down", -move), ("up", move)):
        with_add = (after_drop + add) * (1 + m)
        without = after_drop * (1 + m)
        out[name] = {
            "with_add_value": round(with_add), "with_add_pnl": round(with_add - (first + add)),
            "without_value": round(without), "without_pnl": round(without - first),
        }
    out["down"]["with_add_loss_rate_pct"] = round(out["down"]["with_add_pnl"] / (first + add) * 100, 1)
    out["down"]["without_loss_rate_pct"] = round(out["down"]["without_pnl"] / first * 100, 1)
    out["extra_loss_from_add"] = out["down"]["without_pnl"] - out["down"]["with_add_pnl"]
    out["range_with_add"] = out["up"]["with_add_pnl"] - out["down"]["with_add_pnl"]
    out["range_without"] = out["up"]["without_pnl"] - out["down"]["without_pnl"]
    out["range_ratio"] = round(out["range_with_add"] / out["range_without"], 2)
    return out


def recovery(drop: float) -> float:
    """drop 만큼 빠진 뒤 본전까지 필요한 상승률 (%)."""
    return round((1 / (1 - drop) - 1) * 100, 1)


def leverage_round_trip(down: float, up: float, lev: float) -> dict:
    """기초 주가가 하루 -down, 다음 날 +up 일 때 기초·2배 상품 값 (하루 단위 2배 — 수수료·이자 없음)."""
    base = (1 - down) * (1 + up)
    lever = (1 - lev * down) * (1 + lev * up)
    return {"base_pct": round((base - 1) * 100, 1), "lev_pct": round((lever - 1) * 100, 1)}


def pct_change(a: float, b: float) -> float:
    return round((b / a - 1) * 100, 2)


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(message)s", stream=sys.stdout)
    t0 = time.time()
    log("START", version=VERSION)
    log("GIVEN", **GIVEN)
    f = {k: v for k, v, *_ in FACTS}
    res = {
        "version": VERSION,
        "given": GIVEN,
        "averaging_down": averaging_down(GIVEN["first_buy_won"], GIVEN["first_drop"], GIVEN["add_won"], GIVEN["next_move"]),
        "recovery_pct_after_40": recovery(GIVEN["recovery_drop"]),
        "leverage_round_trip": leverage_round_trip(GIVEN["lev_down"], GIVEN["lev_up"], GIVEN["leverage"]),
        "split_per_month_won": GIVEN["split_total_won"] // GIVEN["split_months"],
        "kospi_oct_to_1109_pct": pct_change(f["kospi_oct_start"], f["kospi_1109"]),
        "nvda_intraday_swing_pctp": round(f["nvda_open_drop_pct"] - f["nvda_close_drop_pct"], 2),
        "facts": [{"key": k, "value": v, "unit": u, "what": w, "source": s} for k, v, u, w, s in FACTS],
    }
    ad = res["averaging_down"]
    log("CALC", after_drop=ad["after_drop"], down_with_add=ad["down"]["with_add_pnl"], down_without=ad["down"]["without_pnl"],
        up_with_add=ad["up"]["with_add_pnl"], up_without=ad["up"]["without_pnl"], extra_loss=ad["extra_loss_from_add"], range_ratio=ad["range_ratio"])
    log("CALC", recovery_after_40=res["recovery_pct_after_40"], lev_round_trip=res["leverage_round_trip"],
        kospi_drop=res["kospi_oct_to_1109_pct"], nvda_swing_pctp=res["nvda_intraday_swing_pctp"])
    # 점검 — 계산이 기대와 어긋나면 멈춤 (대본 숫자와 짝)
    assert ad["down"]["with_add_value"] == 14_400_000 and ad["extra_loss_from_add"] == 2_000_000, ad
    assert res["leverage_round_trip"]["base_pct"] == -1.0 and res["leverage_round_trip"]["lev_pct"] == -4.0
    log("CALC", split_per_month=res["split_per_month_won"], loss_rate_with_add=ad["down"]["with_add_loss_rate_pct"], loss_rate_without=ad["down"]["without_loss_rate_pct"])
    assert res["split_per_month_won"] == 1_000_000
    log("FACTS", n=len(FACTS), unverified=sum("확인 필요" in s for *_, s in FACTS))
    out = HERE / "result.json"
    out.write_text(json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")
    log("WRITE", path=out.relative_to(HERE.parent.parent.parent.parent))
    log("DONE", seconds=round(time.time() - t0, 3))
    return 0


if __name__ == "__main__":
    sys.exit(main())
