# VERSION: v1.0 — 2026-10-25 — 처음 만듦: 가상 인물 김 과장 계좌 숫자 (요약본 v1.0)
"""주식으로 빨리 부자 되려던 김 과장(가상) 계좌 계산.

요약본 `../요약본.txt` 의 숫자는 모두 이 출력만 쓴다.
가정은 ASSUME 에 모았고, 실제 주가 자료가 아니라 이야기용 가정이다
(세금·수수료·신용 이자는 넣지 않음). ※ 연구·교육용 — 투자 권유가 아님.
"""
import logging

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] [CALC] %(message)s")
log = logging.getLogger("calc")

ASSUME = {
    "seed": 2_000,             # 만 원 — 4월 첫 매수 (비상금)
    "first_gain": 0.30,        # 한 달 수익률 (가정)
    "account": 10_000,         # 만 원 — 5월 예금·적금을 깨 맞춘 계좌 (내 돈)
    "margin_loan": 10_000,     # 만 원 — 6월 18일 신용융자
    "maint_ratio": 1.40,       # 담보유지비율 (통상 140% — 헤럴드경제 2026-03-04)
    "drop_step1": 0.25,        # 산 값 대비 주가 하락 — 7월 초 (가정)
    "chase_loss": 0.25,        # 반대매매 뒤 남은 돈으로 2배 단타한 손실률 (가정)
}


def main():
    a = ASSUME
    log.info("assume %s", " ".join(f"{k}={v}" for k, v in a.items()))

    gain = a["seed"] * a["first_gain"]
    log.info("stage=첫수익 seed=%d gain=%d after=%d", a["seed"], gain, a["seed"] + gain)
    added = a["account"] - (a["seed"] + gain)
    log.info("stage=몰빵 added=%d account=%d", added, a["account"])

    own, loan = a["account"], a["margin_loan"]
    pos = own + loan
    log.info("stage=빚 position=%d own=%d loan=%d", pos, own, loan)

    # 1) 주가 -25% → 내 돈
    p1 = pos * (1 - a["drop_step1"])
    e1 = p1 - loan
    log.info("stage=버티기 drop=%.0f%% position=%d equity=%d equity_chg=%.0f%%",
             a["drop_step1"] * 100, p1, e1, (e1 / own - 1) * 100)

    # 2) 반대매매 선: 평가액 = 대출 × 담보유지비율
    p_mc = loan * a["maint_ratio"]
    drop_mc = 1 - p_mc / pos
    e2 = p_mc - loan
    log.info("stage=반대매매 trigger_drop=%.0f%% position=%d equity=%d equity_chg=%.0f%%",
             drop_mc * 100, p_mc, e2, (e2 / own - 1) * 100)
    # 비교: 빚 없이 내 돈만 같은 하락
    e2_nodebt = own * (1 - drop_mc)
    log.info("compare=빚없음 same_drop=%.0f%% equity=%d equity_chg=%.0f%% forced_sale=no",
             drop_mc * 100, e2_nodebt, (e2_nodebt / own - 1) * 100)

    # 3) 만회 단타
    e3 = e2 * (1 - a["chase_loss"])
    log.info("stage=한방 equity=%d equity_chg=%.0f%% total_loss=%d", e3, (e3 / own - 1) * 100, own - e3)

    # 되찾는 데 필요한 수익률 (손실의 비대칭)
    for loss in (0.30, 0.50, 0.60, 0.70):
        log.info("recover loss=%.0f%% need=+%.1f%%", loss * 100, (1 / (1 - loss) - 1) * 100)

    # 2배 상품: 하루 -10%, 다음 날 +11% (기초 주가는 거의 제자리)
    base = 0.90 * 1.11
    lev2 = (1 - 0.20) * (1 + 0.22)
    log.info("lev2 base_two_days=%.1f%% lev2_two_days=%.1f%%", (base - 1) * 100, (lev2 - 1) * 100)

    # 사전 점검 (이야기 숫자와 어긋나면 멈춤)
    checks = {
        "equity1=-50%": round(e1 / own - 1, 4) == -0.50,
        "equity2=-60%": round(e2 / own - 1, 4) == -0.60,
        "equity3=-70%": round(e3 / own - 1, 4) == -0.70,
        "trigger=-30%": round(drop_mc, 4) == 0.30,
    }
    bad = [k for k, ok in checks.items() if not ok]
    if bad:
        log.warning("check failed %s — 요약본 숫자와 다름, 가정을 확인", bad)
        raise SystemExit(1)
    log.info("check ok %s", " ".join(checks))


if __name__ == "__main__":
    main()
