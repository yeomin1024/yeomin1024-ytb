#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.5 — 2026-11-13 — 반론 5회차(상: '1991년 이후 … 아홉 해'가 10년을 못 채운 2019·2021·2023 을 뺀 걸 말하지 않음 · 중: 나머지 15.5% · 중: 임금피크제와 '10년 넘게' 부딪힘) → wait_vs_now 에 wait_wins·last_start_year·start_to · 2023-07 목돈 = 저축 보험 만기금 2천만 원(값 같음).
# (v1.4) — 2026-11-13 — 반론 4회차(중: '84.5%는 그날이 오지 않아, 바로 넣은 쪽이 더 남음'이 두 숫자를 섞음 · 몇 해인지) → wait_vs_now 에 start_years·year_list·now_wins_when_never 를 더함 (값 바꿈 없음).
# (v1.3) — 2026-11-13 — 반론 3회차(상: 보기 B '떨어지면 넣기'는 9.9% 하락 때 이겼을 길) → 보기 B = '그해 오른 만큼 다 빠질 때까지 기다리기' · 통계 wait_vs_now(1991~ 그해 20% 넘게 오른 날 — 바로 넣기 vs 그렇게 기다리기, 10년 뒤).
# (v1.2) — 2026-11-13 — 이탈 2회차(선택 4 비상금 답이 미리 보임)·반론 2회차(상: 도입 −12.5% 가 대본에서 안 보이는 경로) → 선택 4 = 2023-07-31 퇴직금 중간정산 2천만 원(오래 둘 돈)
#          '비싸 보여도 넣기' · 비상금 뺌 · 윤씨 경로 = 바닥 매도 → 기다림 → 2025-02-19 최고가에 다시(대본에 보이는 길) · 원화 셈 확인(KRW=X) · 한 해 20% 넘게 오른 뒤 10년 통계.
# (v1.1) — 2026-11-12 — 반론 검토 1회차(상: 노후 자금 '10년 넘게 쓸 일 없는 돈'에서 이사 잔금을 꺼내는 모순) → 이사 잔금 = 2025-02 집을 팔고 받은 계약금 4천만 원(따로 받은 돈) · 노후 자금 7천은 끝까지 안 꺼냄 · 경로 다시.
# (v1.0) — 2026-11-12 — 주식 롱폼 B14 「곧 쓸 돈」 (윤씨 · 보유 기간과 손실) 숫자 — 사용자 지시 2026-11-12 "새 영상 2개 대본까지 만들어봐"
#   (주제 = 기획안 topics_2026-11-04.json B14 — 댓글 니즈 K04 '나스닥·S&P 는 몇 년 들고 있어야 손실이 안 나나' 👍308 · 페르소나 P3 50대 노후 준비).
#   다섯 선택(모두 '그 돈을 언제 쓰나 = 얼마나 오래 둘 수 있나'의 다른 면 — 옳은 행동은 서로 다름, quick_board 규칙 39):
#     ① 2021-12-31 1년 뒤 쓸 전세금 — 처음부터 넣지 않음(예금)          ② 2022-08-16 넉 달 뒤 쓸 적금 만기 돈 — 반등에도 사지 않음
#     ③ 2022-10-12 10년 넘게 둘 노후 자금 — 바닥에서 팔지 않음              ④ 2023-07-31 비상금 — 따로 떼어 둠(넣지 않음 · 언제 쓸지 모름)
#     ⑤ 2025-02-19 두 달 뒤 쓸 이사 잔금(노후 자금 일부) — 쓸 날 전에 미리 빼 둠
#   이야기 기간 = 2021-12-31 ~ 2025-12-31 (4년 — 규칙 1·16). 통계 = S&P 500 배당 포함 지수, 1990년 이후 거래일마다 시작한 보유 기간.
# 자료(새로 받지 않음): longform_items.load() — calc/sp500tr_daily.csv(배당 포함) · gspc_daily.csv(가격) · irx_daily.csv(13주 국채 → 예금 대신 '현금 이자').
# 가정(업로드 시트 7번 '점검'): 금액 = 원 × 달러 기준 변화율(환율·세금·수수료 뺌) · 예금 = 13주 국채 이자로 셈(한국 예금 금리와 다름 — 대본은 '예금' 결과를 원금 그대로로만 말함).
# 실행: python3 -B stock/topics/precheck/longform_b14.py → precheck/longform_b14_<날짜>.json
# ※ 연구·교육용 — 투자 권유가 아님.
#
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.2 | 2026-11-13 | 선택 4 퇴직금 · 비상금 뺌 · 윤씨 경로 다시 · 원화 확인 · after20 통계 | main |
# | v1.1 | 2026-11-12 | 이사 잔금 = 따로 받은 계약금 · 노후 자금 7천 끝까지 · 경로·합계 다시 | main(paths) |
# | v1.0 | 2026-11-12 | 최초 — 보유 기간 통계 · 다섯 선택 · 윤씨 경로 · 옳은 경로 | 전부 |
import bisect
import json
import logging
import sys
from datetime import date
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import longform_items as L  # noqa: E402

VERSION = "v1.3"
logging.disable(logging.INFO)
STAT_FROM, END = "1990-01-02", "2025-12-31"
CONTRACT = "2025-01-17"   # v1.1 집을 판 계약금 4천만 원을 받아 지수에 넣은 날 (선택 5 — 한 달 전)
OUT: dict = {"tool": f"longform_b14.py {VERSION}", "made": date.today().isoformat(), "story": ["2021-12-31", END],
             "basis": "S&P 500 배당 포함(^SP500TR) 일별 · 예금 대신 13주 국채 이자 · 원 = 달러 기준 변화율(환율·세금·수수료 뺌)"}


def log(tag, /, **kv):
    print(f"[{tag}] [{date.today()}] " + " ".join(f"{k}={v}" for k, v in kv.items()), flush=True)


def plus_years(d, h_years=0, h_months=0):
    y, m, dd = map(int, d.split("-"))
    m2 = m + h_months
    y += h_years + (m2 - 1) // 12
    m2 = (m2 - 1) % 12 + 1
    for day in (dd, 28):
        try:
            return date(y, m2, min(day, 28) if day == 28 else day).isoformat()
        except ValueError:
            continue
    return date(y, m2, 28).isoformat()


def holding_stats(TR, years=0, months=0):
    """1990 이후 거래일마다 시작해 그 기간 들고 있었을 때: 끝에 손실인 몫 · 중간에 원금이 20% 넘게 줄어든 적이 있는 몫 · 가장 나쁜 끝."""
    k, v = TR.k, TR.v
    n = loss = dd = 0
    worst = 9.0
    for i, d in enumerate(k):
        if d < STAT_FROM:
            continue
        e = plus_years(d, years, months)
        if e > END:
            break
        j = bisect.bisect_right(k, e) - 1
        r = v[j] / v[i] - 1
        mn = v[i:j + 1].min() / v[i] - 1
        n += 1
        loss += r < 0
        dd += mn < -0.2
        worst = min(worst, r)
    return {"starts": n, "loss_share": round(loss / n, 4), "dd20_share": round(dd / n, 4), "worst_end": round(float(worst), 4),
            "label": f"{years}년" if years else f"{months}개월"}


def main():
    S = L.load()
    TR, SPX, C = S["TR"], S["SPX"], S["CASH"]
    st = {lab: holding_stats(TR, *hm) for lab, hm in {"2m": (0, 2), "3m": (0, 3), "4m": (0, 4), "1y": (1, 0), "2y": (2, 0), "3y": (3, 0), "5y": (5, 0), "10y": (10, 0), "15y": (15, 0)}.items()}
    OUT["holding"] = st
    for lab, x in st.items():
        log("STAT", period=lab, starts=x["starts"], loss=L.pct(x["loss_share"]).lstrip("+"), dd20=L.pct(x["dd20_share"]).lstrip("+"), worst=L.pct(x["worst_end"]))
    ch = lambda a, b: round(TR.chg(a, b), 4)  # noqa: E731
    c1 = {"day": "2021-12-31", "need": "2022-12-30", "tr_2021": ch("2020-12-31", "2021-12-31"), "spx_peak_next": SPX.peak_before("2022-01-04"),
          "wrong": ch("2021-12-31", "2022-12-30"), "low": TR.low("2021-12-31", "2022-12-30"), "cash": round(C.chg("2021-12-31", "2022-12-30"), 4)}
    c2 = {"day": "2022-08-16", "need": "2022-12-30", "from_peak": round(TR.at("2022-08-16") / TR.at("2022-01-03") - 1, 4),
          "rally_from_june_low": ch("2022-06-16", "2022-08-16"), "wrong": ch("2022-08-16", "2022-12-30"), "low": TR.low("2022-08-16", "2022-12-30")}
    c3 = {"day": "2022-10-12", "from_peak": round(TR.at("2022-10-12") / TR.at("2022-01-03") - 1, 4), "from_start": ch("2021-12-31", "2022-10-12"),
          "hold_to_end": ch("2022-10-12", END), "hold_from_start": ch("2021-12-31", END), "sold_cash_to_end": round(C.chg("2022-10-12", END), 4),
          "sold_total_from_start": round((1 + TR.chg("2021-12-31", "2022-10-12")) * (1 + C.chg("2022-10-12", END)) - 1, 4),
          "back_to_start": TR.back("2022-10-12", TR.at("2021-12-31"))}
    def wait_vs_now(th=0.20, years=10):              # 그해(앞 해 말부터) th 넘게 오른 날: 바로 넣기 vs '그해 오른 만큼 다 빠질 때까지' 현금으로 기다리기
        k, v = TR.k, TR.v
        n_ = win = never = win_never = 0
        yrs = set()
        for i, d in enumerate(k):
            if d < "1991-01-01":
                continue
            e = plus_years(d, years)
            if e > END:
                break
            base = TR.at(TR.day(f"{int(d[:4]) - 1}-12-31"))
            if v[i] / base - 1 <= th:
                continue
            n_ += 1
            yrs.add(d[:4])
            j = bisect.bisect_right(k, e) - 1
            hit = np.nonzero(v[i:j + 1] <= base)[0]
            if len(hit):
                b = i + int(hit[0])
                w = (1 + C.chg(d, k[b])) * (v[j] / v[b])
            else:
                w = 1 + C.chg(d, e)
                never += 1
                win_never += v[j] / v[i] >= w
            win += v[j] / v[i] >= w
        return {"th": th, "years": years, "starts": n_, "start_years": len(yrs), "year_list": sorted(yrs),
                "now_wins": round(win / n_, 4), "never_came": round(never / n_, 4),
                "now_wins_when_never": round(win_never / max(never, 1), 4), "wait_wins": round(1 - win / n_, 4),
                "last_start_year": max(yrs), "start_to": plus_years(END, -years)[:4]}
    def after_up(th=0.20, years=10):                 # 한 해(1년) 동안 th 넘게 오른 날에 넣고 years 년 들고 있었다면
        k, v = TR.k, TR.v
        n_ = loss_ = 0
        for i, d in enumerate(k):
            if d < STAT_FROM:
                continue
            e = plus_years(d, years)
            if e > END:
                break
            if TR.chg(plus_years(d, -1), d) > th:
                j = bisect.bisect_right(k, e) - 1
                n_ += 1
                loss_ += v[j] < v[i]
        return {"th": th, "years": years, "starts": n_, "loss_share": round(loss_ / n_, 4), "gain_share": round(1 - loss_ / n_, 4)}
    c4 = {"day": "2023-07-31", "ytd": ch("2022-12-30", "2023-07-31"), "invest_to_end": ch("2023-07-31", END),
          "wait_to_0219_then": round((1 + C.chg("2023-07-31", "2025-02-19")) * (1 + TR.chg("2025-02-19", END)) - 1, 4),
          "dip_1027": ch("2023-07-31", "2023-10-27"), "after20_10y": after_up(), "wait_vs_now": wait_vs_now(),
          "came_back_2022_level": next((d for d in TR.k if d > "2023-07-31" and TR.at(d) <= TR.at("2022-12-30")), None)}
    c5 = {"day": "2025-02-19", "need": "2025-04-08", "two_years": ch("2023-02-17", "2025-02-19"), "contract_to_day": ch(CONTRACT, "2025-02-19"), "wrong": ch("2025-02-19", "2025-04-08"),
          "back_day": TR.back("2025-04-08", TR.at("2025-02-19")), "to_end": ch("2025-02-19", END)}
    def top(a, b):                                   # a~b 사이 가장 높은 종가의 날 (가격 지수)
        i, j = SPX.i(a), SPX.i(b)
        m = i + int(SPX.v[i:j + 1].argmax())
        return SPX.k[m]
    c1["record_close_day"] = top("2021-06-01", "2022-12-31")
    c2["rally_top_day"] = top("2022-06-16", "2022-12-31")
    c4["summer_top_day"] = top("2023-01-03", "2023-10-27")
    c5["record_before"] = top("2024-01-02", "2025-04-08")
    OUT["choices"] = {"1": c1, "2": c2, "3": c3, "4": c4, "5": c5}
    for n_, c in OUT["choices"].items():
        log("CHOICE", n=n_, **{k: (L.pct(v) if isinstance(v, float) else v) for k, v in c.items() if not isinstance(v, (tuple, list))})
    # 윤씨 경로 (다섯 번 모두 반대로 — 대본에 보이는 길) vs 옳은 경로 · 쓴 돈(전세금 4천 · 새집 잔금 4천)은 두 길 모두 같은 날 같은 금액
    #   돈: 2021-12-31 노후 자금 7천(10년 넘게) + 전세금 3천(2022-12-30) · 적금 만기 1천(2022-08-16 — 전세금에 보탬) ·
    #       보험 만기금 2천(v1.5 — 옛 퇴직금 중간정산)(2023-07-31 — 노후용) · 집을 판 계약금 4천(CONTRACT 받음 — 2025-04-08 새집 잔금)
    M = 1e4  # 만 원
    cc = lambda a, b: 1 + C.chg(a, b)   # noqa: E731
    tt = lambda a, b: 1 + TR.chg(a, b)  # noqa: E731
    # 옳은 길: 노후 7천 지수 그대로 · 전세금·적금 예금 → 12/30 지급 · 보험 만기금 2천 7/31 지수 · 계약금 받은 날부터 예금 → 4/8 잔금
    good_long = 7000 * M * tt("2021-12-31", END) + 2000 * M * tt("2023-07-31", END)
    good_cash = (3000 * M * cc("2021-12-31", "2022-12-30") + 1000 * M * cc("2022-08-16", "2022-12-30") - 4000 * M) * cc("2022-12-30", END) \
        + (4000 * M * cc(CONTRACT, "2025-04-08") - 4000 * M) * cc("2025-04-08", END)
    good_total = good_long + good_cash
    # 윤씨: ① 노후 7천 + 전세금 3천 모두 지수 ② 8/16 적금 1천도 지수 ③ 10/12 모두 매도 → 현금 · 12/30 전세금 4천 지급
    #       ④ 7/31 보험 만기금 2천도 '비싸 보여' 현금으로 기다림(가진 현금 모두) · 계약금은 받은 날 지수에
    #       ⑤ 2/19 최고가 — 기다리던 현금을 모두 지수에 넣고, 계약금도 미리 빼지 않음 → 4/8 잔금 4천 매도
    v = 10000 * M * tt("2021-12-31", "2022-08-16") + 1000 * M
    cash = v * tt("2022-08-16", "2022-10-12")
    cash_after_sale = cash
    cash = cash * cc("2022-10-12", "2022-12-30") - 4000 * M
    cash = cash * cc("2022-12-30", "2023-07-31") + 2000 * M
    cash = cash * cc("2023-07-31", "2025-02-19")
    contract = 4000 * M * tt(CONTRACT, "2025-02-19")
    idx = (cash + contract) * tt("2025-02-19", "2025-04-08") - 4000 * M
    yoon_end = idx * tt("2025-04-08", END)
    long_put = 7000 + 2000
    OUT["paths"] = {"spent_man": 8000, "put_in_man": 7000 + 3000 + 1000 + 2000 + 4000, "long_put_man": long_put,
                    "good_end_man": round(good_total / M), "yoon_end_man": round(yoon_end / M), "yoon_vs_long": round(yoon_end / (long_put * M) - 1, 4),
                    "good_vs_long": round(good_total / (long_put * M) - 1, 4), "yoon_vs_good": round(yoon_end / good_total - 1, 4),
                    "sold_at_low_man": round(cash_after_sale / M), "index_4y": ch("2021-12-31", END), "spx_4y": round(SPX.chg("2021-12-31", END), 4),
                    "note": "굴린 돈 1억 7천만 원 · 쓴 돈 8천만 원(전세금 4천 · 잔금 4천)은 두 길 모두 같음 → 남은 돈을 오래 둘 돈 9천만 원(노후 7천 + 보험 만기금 2천)에 대어 봄"}
    # 원화로 셈해도 같은가 (USD/KRW 종가 · 예금은 원화 예금 = 환율 영향 없음으로 봄 — 대본의 '옳은 선택' 방향만 확인)
    FX = L.Ser("USD/KRW", L.rd(HERE / "data" / "KRW_X.csv", "close"))
    krw = lambda a, b: round((1 + TR.chg(a, b)) * FX.at(b) / FX.at(a) - 1, 4)  # noqa: E731
    OUT["krw_check"] = {"c1_wrong": krw("2021-12-31", "2022-12-30"), "c2_wrong": krw("2022-08-16", "2022-12-30"), "c3_hold": krw("2021-12-31", END),
                        "c3_sold": round((1 + TR.chg("2021-12-31", "2022-10-12")) * FX.at("2022-10-12") / FX.at("2021-12-31") - 1, 4),
                        "c4_invest": krw("2023-07-31", END), "c5_wrong": krw("2025-02-19", "2025-04-08"),
                        "fx": {d: round(FX.at(d), 1) for d in ("2021-12-31", "2022-10-12", "2022-12-30", "2023-07-31", "2025-02-19", "2025-04-08", END)}}
    log("KRW", **{k: v_ for k, v_ in OUT["krw_check"].items() if k != "fx"})
    log("PATH", **{k: v_ for k, v_ in OUT["paths"].items() if k != "note"})
    out = HERE / f"longform_b14_{date.today().isoformat()}.json"
    out.write_text(json.dumps(OUT, ensure_ascii=False, indent=1, default=str) + "\n", "utf-8")
    log("DONE", out=out.name)


if __name__ == "__main__":
    main()
