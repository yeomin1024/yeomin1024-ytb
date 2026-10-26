# VERSION: v1.2 — 2026-10-26 — 대본 v2.0 도입용 비교 숫자 더함: 같은 날(4/21) 사서 끝날(9/30)까지 팔지 않은 경우 · 반대매매로 잃은 돈 (사용자 지시 "도입부는 재미 없으니까 다시쓰고")
# v1.1 — 2026-10-25 — SK하이닉스 실제 종가로 다시 계산 (사용자가 요약본에 'SK 하이닉스' 종목을 정함)
# v1.0 — 2026-10-25 — 처음 만듦: 가정한 주가 하락(25%·30%)으로 김 과장 계좌 계산
"""주식으로 빨리 부자 되려던 김 과장(가상) 계좌 계산 — SK하이닉스 실제 가격.

대본·요약본의 숫자는 모두 이 출력만 쓴다. 가격은 같은 폴더 `prices_2026.csv`
(Yahoo Finance 000660.KS · ^KS11 일봉, 2026-10-25 받음 — 6/19·7/13·7/31 종가를 기사와 맞춰 봄).

가정 (실제가 아닌 것은 여기 모음): 매수·매도는 그날 종가(반대매매만 다음 날 시가),
주 수는 금액 ÷ 가격 (소수 주), 세금·수수료·신용 이자 없음, 2배 ETF = SK하이닉스 하루 등락 × 2
(운용 보수·괴리 없음). 반대매매 시점은 증권사마다 다름 — 여기서는 담보 부족 다음 날 시가.
※ 연구·교육용 — 투자 권유가 아님.
"""
import csv
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] [CALC] %(message)s")
log = logging.getLogger("calc")

PRICES = Path(__file__).with_name("prices_2026.csv")
MAN = 10_000  # 만 원

ASSUME = {
    "buy1": ("2026-04-21", 2_000 * MAN),   # 장면1 — 비상금
    "check1": "2026-05-21",                # 장면2 — 한 달 뒤
    "buy2": ("2026-05-27", 8_000 * MAN),   # 장면3 — 적금·예금·학원비 통장
    "loan": ("2026-06-18", 10_000 * MAN),  # 장면4 — 신용융자 (코스피 처음 9,000)
    "peak": "2026-06-22",                  # 장면4 끝 — 계좌 최고
    "crash": ("2026-07-10", "2026-07-13"),  # 장면5 — 하루 폭락 (전날, 그날)
    "hold": "2026-07-20",                  # 장면5 끝 — 계속 버팀
    "breach": "2026-07-28",                # 장면6 — 담보비율 140% 아래로 마감
    "sale": "2026-07-29",                  # 장면6 — 다음 날 시가에 반대매매
    "limit_up": ("2026-07-30", "2026-07-31"),  # 장면6 끝 — 상한가
    "lev_buy": "2026-07-31",               # 장면7 — 남은 돈 전부 2배 ETF (종가)
    "lev_end": "2026-08-12",               # 장면7 — 내 돈 -70%
    "maint_ratio": 1.40,                   # 담보유지비율 (통상 140%)
}


def load():
    rows = list(csv.DictReader(PRICES.open()))
    if not rows:
        raise SystemExit(f"[ERROR] [CALC] 가격 파일이 비었음: {PRICES} — prices_2026.csv 를 다시 만드세요")
    open_ = {r["date"]: float(r["hynix_open"]) for r in rows}
    close = {r["date"]: float(r["hynix_close"]) for r in rows}
    kospi = {r["date"]: float(r["kospi_close"]) for r in rows if r["kospi_close"]}
    log.info("load file=%s rows=%d from=%s to=%s", PRICES.name, len(rows), rows[0]["date"], rows[-1]["date"])
    return open_, close, kospi


def man(won):
    return f"{won / MAN:,.0f}만"


def main():
    a = ASSUME
    o, c, k = load()

    d1, m1 = a["buy1"]
    sh1 = m1 / c[d1]
    v_check = sh1 * c[a["check1"]]
    log.info("stage=첫매수 date=%s price=%d amount=%s", d1, c[d1], man(m1))
    log.info("stage=첫수익 date=%s price=%d value=%s gain=%s chg=%+.1f%% kospi_chg=%+.1f%%",
             a["check1"], c[a["check1"]], man(v_check), man(v_check - m1), (v_check / m1 - 1) * 100,
             (k[a["check1"]] / k[d1] - 1) * 100)

    d2, m2 = a["buy2"]
    sh2 = m2 / c[d2]
    own = m1 + m2
    log.info("stage=몰빵 date=%s price=%d add=%s principal=%s account=%s",
             d2, c[d2], man(m2), man(own), man(sh1 * c[d2] + m2))

    d3, loan = a["loan"]
    sh = sh1 + sh2 + loan / c[d3]
    pos = sh * c[d3]
    log.info("stage=빚 date=%s price=%d loan=%s position=%s equity=%s",
             d3, c[d3], man(loan), man(pos), man(pos - loan))
    eq_peak = sh * c[a["peak"]] - loan
    log.info("stage=최고 date=%s price=%d equity=%s chg=%+.1f%%", a["peak"], c[a["peak"]], man(eq_peak), (eq_peak / own - 1) * 100)
    line = a["maint_ratio"] * loan / sh
    log.info("rule=담보140%% line_price=%d drop_from_loan_day=%.1f%%", line, (line / c[d3] - 1) * 100)

    p0, p1 = a["crash"]
    e0, e1 = sh * c[p0] - loan, sh * c[p1] - loan
    log.info("stage=폭락 date=%s price=%d day_chg=%+.2f%% equity=%s chg=%+.1f%% one_day=%s price_vs_loanday=%+.1f%% equity_vs_loanday=%+.1f%% kospi=%.2f",
             p1, c[p1], (c[p1] / c[p0] - 1) * 100, man(e1), (e1 / own - 1) * 100, man(e1 - e0),
             (c[p1] / c[d3] - 1) * 100, (e1 / (pos - loan) - 1) * 100, k[p1])
    eh = sh * c[a["hold"]] - loan
    log.info("stage=버티기 date=%s price=%d equity=%s chg=%+.1f%%", a["hold"], c[a["hold"]], man(eh), (eh / own - 1) * 100)

    b = a["breach"]
    ratio = sh * c[b] / loan
    log.info("stage=담보부족 date=%s price=%d ratio=%.1f%% equity=%s", b, c[b], ratio * 100, man(sh * c[b] - loan))
    if ratio >= a["maint_ratio"]:
        log.warning("check 담보비율이 140%% 이상 — 반대매매 날짜를 확인")
    s = a["sale"]
    e_sale = sh * o[s] - loan
    log.info("stage=반대매매 date=%s open=%d proceeds=%s repay=%s left=%s chg=%+.1f%%",
             s, o[s], man(sh * o[s]), man(loan), man(e_sale), (e_sale / own - 1) * 100)
    log.info("stage=반대매매 lost=%s (넣은 돈 %s - 남은 돈 %s)", man(own - e_sale), man(own), man(e_sale))   # v1.2
    sh_own = sh1 + sh2
    lu0, lu1 = a["limit_up"]
    log.info("compare=빚없음 sale_day=%s equity=%s chg=%+.1f%% | limit_up=%s equity=%s chg=%+.1f%% forced_sale=no",
             s, man(sh_own * o[s]), (sh_own * o[s] / own - 1) * 100, lu1, man(sh_own * c[lu1]), (sh_own * c[lu1] / own - 1) * 100)
    log.info("event=상한가 date=%s price=%d day_chg=%+.2f%%", lu1, c[lu1], (c[lu1] / c[lu0] - 1) * 100)
    end = max(c)
    log.info("compare=빚없음_끝 date=%s equity=%s chg=%+.1f%%", end, man(sh_own * c[end]), (sh_own * c[end] / own - 1) * 100)
    # v1.2 도입: 김 과장이 처음 산 날(4/21) 같은 값에 사서 끝날까지 팔지 않은 사람 (자기 돈만, 한 번만 삼)
    log.info("compare=같은날_들고만 buy=%s end=%s price=%d→%d chg=%+.1f%% (2천만 원이면 %s)",
             d1, end, c[d1], c[end], (c[end] / c[d1] - 1) * 100, man(m1 * c[end] / c[d1]))

    days = sorted(d for d in c if a["lev_buy"] <= d <= a["lev_end"])
    v = e_sale
    for x, y in zip(days, days[1:]):
        v *= 1 + 2 * (c[y] / c[x] - 1)
    log.info("stage=한방 buy=%s end=%s base_chg=%+.1f%% lev2_chg=%+.1f%% equity=%s chg=%+.1f%% total_loss=%s",
             a["lev_buy"], a["lev_end"], (c[a["lev_end"]] / c[a["lev_buy"]] - 1) * 100, (v / e_sale - 1) * 100,
             man(v), (v / own - 1) * 100, man(own - v))
    log.info("recover from=%s to=%s need=+%.1f%%", man(v), man(own), (own / v - 1) * 100)
    log.info("lev2_example base_two_days=%+.1f%% lev2_two_days=%+.1f%%", (0.90 * 1.11 - 1) * 100, (0.80 * 1.22 - 1) * 100)

    # 사전 점검 — 대본 숫자와 어긋나면 멈춤
    checks = {
        "first_gain~+58%": round((v_check / m1 - 1) * 100) == 58,
        "crash_eq~-35%": round((e1 / own - 1) * 100) == -35,
        "breach<140%": ratio < a["maint_ratio"],
        "sale~-60%": round((e_sale / own - 1) * 100) == -60,
        "end~-70%": round((v / own - 1) * 100) == -70,
        "same_day_hold~+45%": round((c[end] / c[d1] - 1) * 100) == 45,   # v1.2 도입 문장
    }
    bad = [name for name, ok in checks.items() if not ok]
    if bad:
        log.warning("check failed %s — 대본 숫자와 다름, 날짜·가정을 확인", bad)
        raise SystemExit(1)
    log.info("check ok %s", " ".join(checks))


if __name__ == "__main__":
    main()
