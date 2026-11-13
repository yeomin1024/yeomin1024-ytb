#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.4 — 2026-11-13 — 반론 4회차(중 K3: 선택 2 '제자리였던 때'는 결과로 고른 표본 · 선택 3 근거가 바닥 날 하나) → dd_buy = 산 날 알 수 있는 조건(1년 안 최고가보다 25% 넘게 빠진 날) — c2.dd25_6m(SQQQ 반년) · c3.dd25_1y(SPXU 1년) · 다른 값 바꿈 없음.
# (v1.3) — 2026-11-13 — 반론 3회차(중 K3: 선택 1 근거가 한 구간뿐) → c1.sh_4y_vs_cash = SH 를 아무 날 사서 4년 들고 간 때 현금보다 적게 남은 몫(roll_vs) · 다른 값 바꿈 없음.
# (v1.2) — 2026-11-13 — 반론 2회차 → 선택 1 계좌 합계(바닥 날·2025년 말) · 장면마다 2025년 말 값 · 공포 지수 40 넘은 사건 수 · 제자리 2% 로도 확인(robust).
# (v1.1) — 2026-11-12 — 반론 검토 1회차(상: 선택 3 '오르면 정리'가 타이밍을 가르치고 선택 1 정답을 뒤집음) → 선택 3 을 빼고 차례를 바꿈:
#          ③ 2022-10-12 바닥 — 잃은 돈 되찾으려 3배 인버스 · ④ 2023-07-31 — 거품 같아 지수 몫을 인버스로 · 제자리 기준 5% 를 대본에 · 공포 지수 40 넘은 날 통계 · 경로 다시.
# (v1.0) — 2026-11-12 — 주식 롱폼 B19 「인버스로 폭락 대비」 (임씨) 숫자 — 사용자 지시 2026-11-12 "새 영상 2개 대본까지 만들어봐"
#   (주제 = 기획안 topics_2026-11-04.json B19 — 댓글 니즈 K10 '레버리지는 횡보장·하락장에 녹나' · K07 · 페르소나 P1 3040 직장인).
#   다섯 선택(모두 '폭락 대비'의 다른 면 — 옳은 행동은 서로 다름, quick_board 규칙 39):
#     ① 2022-01-03 최고가 — 대비를 인버스 상품으로 vs 현금 비중으로     ② 2022-06-16 — 나스닥 3배 인버스를 연말까지 vs 사지 않음 (지수 제자리 · 상품만 줄어듦)
#     ③ 2022-09-30 — 1월에 산 인버스가 올랐을 때 계속 보유 vs 정리      ④ 2022-10-12 바닥 — 잃은 돈을 되찾으려 3배 인버스 vs 하지 않음
#     ⑤ 2025-04-08 공포 지수 52 — 공포 지수 상품 매수 vs 사지 않음
#   이야기 기간 = 2022-01-03 ~ 2025-12-31 (4년 — 규칙 1·16).
# 자료: longform_items.load() (S&P 500 가격·배당 포함·13주 국채·VIX) + precheck/data/{SH,SDS,SPXU,SQQQ,QQQ,UVXY}.csv (Yahoo 수정 종가 — 2026-11-12 받음)
#   SH = S&P 500 하루 −1배 · SDS = −2배 · SPXU = −3배 · SQQQ = 나스닥 100 −3배 · UVXY = 공포 지수(VIX) 선물 1.5배 상품.
# 가정(업로드 시트 7번): 금액 = 원 × 달러 기준 변화율(환율·세금·수수료 뺌) · 현금 = 13주 국채 이자 · 상품 값 = 수정 종가(운용 보수 반영된 실제 값).
# 실행: python3 -B stock/topics/precheck/longform_b19.py → precheck/longform_b19_<날짜>.json
# ※ 연구·교육용 — 투자 권유가 아님.
#
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.1 | 2026-11-12 | 선택 3 → '거품 같아 인버스로'(2023-07-31) · 차례 바꿈 · 공포 지수 40 넘은 날 통계 · 경로 다시 | main |
# | v1.0 | 2026-11-12 | 최초 — 다섯 선택 · 제자리 장 통계 · 임씨 경로 · 옳은 경로 | 전부 |
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

VERSION = "v1.2"
logging.disable(logging.INFO)
END = "2025-12-31"
SYMS = ("SH", "SDS", "SPXU", "SQQQ", "QQQ", "UVXY")
OUT: dict = {"tool": f"longform_b19.py {VERSION}", "made": date.today().isoformat(), "story": ["2022-01-03", END],
             "basis": "상품 = Yahoo 수정 종가 · S&P 500 가격(^GSPC)·배당 포함(^SP500TR) · 현금 = 13주 국채 이자 · 원 = 달러 기준 변화율"}


def log(tag, /, **kv):
    print(f"[{tag}] [{date.today()}] " + " ".join(f"{k}={v}" for k, v in kv.items()), flush=True)


def add_m(d, m):
    y, mo, dd = map(int, d.split("-"))
    mo += m
    y += (mo - 1) // 12
    mo = (mo - 1) % 12 + 1
    return f"{y:04d}-{mo:02d}-{min(dd, 28):02d}"


def flat(idx, inv, months, band=0.05):
    """기초 지수가 그 기간 ±band 안(제자리)이었던 시작일마다 상품의 변화 → 개수 · 가운데 값 · 줄어든 몫."""
    out = []
    for d in inv.k:
        e = add_m(d, months)
        if e > END:
            break
        if abs(idx.chg(d, e)) <= band:
            out.append(inv.chg(d, e))
    a = np.array(out)
    return {"n": int(len(a)), "median": round(float(np.median(a)), 4), "down_share": round(float((a < 0).mean()), 4), "months": months, "band": band,
            "from": inv.k[0]}


def roll_loss(s, years):
    k, v = s.k, s.v
    n = loss = 0
    for i, d in enumerate(k):
        e = add_m(d, 12 * years)
        if e > END:
            break
        j = bisect.bisect_right(k, e) - 1
        n += 1
        loss += v[j] < v[i]
    return {"n": n, "loss_share": round(loss / n, 4), "from": k[0], "years": years}


def roll_vs(s, other, years):
    """s 를 아무 날 사서 years 년 들고 갔을 때, 같은 날 other(현금)에 둔 것보다 적게 남은 몫 — 겹치는 시작일 모두 셈."""
    n = worse = 0
    for d in s.k:
        e = add_m(d, 12 * years)
        if e > END:
            break
        n += 1
        worse += s.chg(d, e) < other.chg(d, e)
    return {"n": n, "worse_share": round(worse / n, 4), "from": s.k[0], "years": years}


def dd_buy(idx, inv, th, months, win=252):
    """산 날 알 수 있는 조건 — 기초 지수가 1년(win 거래일) 안 최고가보다 th 넘게 빠진 날마다 inv 를 사서 months 달 들고 갔을 때."""
    ik, iv = idx.k, np.asarray(idx.v, float)
    out, days = [], []
    for d in inv.k:
        e = add_m(d, months)
        if e > END:
            break
        i = bisect.bisect_right(ik, d) - 1
        if iv[i] / iv[max(0, i - win + 1):i + 1].max() - 1 <= -th:
            out.append(inv.chg(d, e))
            days.append(d)
    a = np.array(out)
    return {"n": int(len(a)), "down_share": round(float((a < 0).mean()), 4), "median": round(float(np.median(a)), 4), "th": th, "months": months,
            "from": inv.k[0], "years": sorted({d[:4] for d in days})}


def main():
    S = L.load()
    SPX, TR, C, VIX = S["SPX"], S["TR"], S["CASH"], S["VIX"]
    X = {s: L.Ser(s, L.rd(HERE / "data" / f"{s}.csv", "adjclose")) for s in SYMS}
    ch = lambda s, a, b: round((X[s] if s in X else {"SPX": SPX, "TR": TR, "CASH": C}[s]).chg(a, b), 4)  # noqa: E731
    OUT["stats"] = {"qqq_flat_6m_sqqq": flat(X["QQQ"], X["SQQQ"], 6), "spx_flat_1y_sds": flat(SPX, X["SDS"], 12), "spx_flat_1y_sh": flat(SPX, X["SH"], 12),
                    "uvxy_1y": roll_loss(X["UVXY"], 1), "sh_1y": roll_loss(X["SH"], 1), "spxu_1y": roll_loss(X["SPXU"], 1)}
    for k_, v_ in OUT["stats"].items():
        log("STAT", name=k_, **v_)
    c1 = {"day": "2022-01-03", "spx_record": SPX.peak_before("2022-01-04")[0] == "2022-01-03", "sh_to_low": ch("SH", "2022-01-03", "2022-10-12"),
          "spx_to_low": ch("SPX", "2022-01-03", "2022-10-12"), "sh_to_end": ch("SH", "2022-01-03", END), "cash_to_end": ch("CASH", "2022-01-03", END),
          "spx_to_end": ch("SPX", "2022-01-03", END)}
    c2 = {"day": "2022-06-16", "to": "2022-12-30", "qqq": ch("QQQ", "2022-06-16", "2022-12-30"), "sqqq": ch("SQQQ", "2022-06-16", "2022-12-30"),
          "qqq_ytd": ch("QQQ", "2021-12-31", "2022-06-16")}
    c3 = {"day": "2022-10-12", "spx_from_peak": ch("SPX", "2022-01-03", "2022-10-12"), "tr_from_start": ch("TR", "2022-01-03", "2022-10-12"),
          "spxu_1y": ch("SPXU", "2022-10-12", "2023-10-12"), "spx_1y": ch("SPX", "2022-10-12", "2023-10-12"), "spxu_to_end": ch("SPXU", "2022-10-12", END),
          "tr_to_end": ch("TR", "2022-10-12", END), "spxu_flat_6m": flat(SPX, X["SPXU"], 6)}
    c4 = {"day": "2023-07-31", "ytd": ch("SPX", "2022-12-30", "2023-07-31"), "sh_to_end": ch("SH", "2023-07-31", END), "spx_to_end": ch("SPX", "2023-07-31", END),
          "tr_to_end": ch("TR", "2023-07-31", END), "dip_to_1027": ch("SPX", "2023-07-31", "2023-10-27"), "sh_to_1027": ch("SH", "2023-07-31", "2023-10-27"),
          "sh_since_jan22": ch("SH", "2022-01-03", "2023-07-31")}
    def vix_buy(level):
        k = [d for d in X["UVXY"].k if VIX.at(d) >= level and add_m(d, 12) <= END]
        r1 = np.array([X["UVXY"].chg(d, add_m(d, 1)) for d in k])
        r12 = np.array([X["UVXY"].chg(d, add_m(d, 12)) for d in k])
        return {"level": level, "days": len(k), "down_1m": round(float((r1 < 0).mean()), 4), "down_12m": round(float((r12 < 0).mean()), 4)}
    best_day = max(((d, X["UVXY"].v[i] / X["UVXY"].v[i - 1] - 1) for i, d in enumerate(X["UVXY"].k) if i and "2025-03-01" <= d <= "2025-04-08"), key=lambda x: x[1])
    c5 = {"day": "2025-04-08", "vix": round(VIX.at("2025-04-08"), 1), "vix_avg_2024": round(float(np.mean([VIX.at(d) for d in VIX.k if "2024-01-01" <= d <= "2024-12-31"])), 1),
          "uvxy_1m": ch("UVXY", "2025-04-08", "2025-05-08"), "uvxy_end": ch("UVXY", "2025-04-08", END), "spx_1m": ch("SPX", "2025-04-08", "2025-05-08"),
          "spx_drop_before": ch("SPX", "2025-02-19", "2025-04-08"), "uvxy_best_day": [best_day[0], round(float(best_day[1]), 4)], "vix40": vix_buy(40)}
    M_ = 1e4
    acct = lambda d, other: 7000 * M_ * (1 + TR.chg("2022-01-03", d)) + 3000 * M_ * (1 + other.chg("2022-01-03", d))  # noqa: E731
    c1["acct"] = {d: {"index_inverse_man": round(acct(d, X["SH"]) / M_), "index_cash_man": round(acct(d, C) / M_),
                      "inverse_vs_cash": round(acct(d, X["SH"]) / acct(d, C) - 1, 4), "cash_vs_inverse": round(acct(d, C) / acct(d, X["SH"]) - 1, 4)}
                  for d in ("2022-10-12", END)}
    c2["dd25_6m"] = dd_buy(X["QQQ"], X["SQQQ"], 0.25, 6)
    c3["dd25_1y"] = dd_buy(SPX, X["SPXU"], 0.25, 12)
    log("STAT", name="c2_dd25_6m", **c2["dd25_6m"])
    log("STAT", name="c3_dd25_1y", **c3["dd25_1y"])
    c1["sh_4y_vs_cash"] = roll_vs(X["SH"], C, 4)
    log("STAT", name="sh_4y_vs_cash", **c1["sh_4y_vs_cash"])
    c2["sqqq_to_end"] = ch("SQQQ", "2022-06-16", END)
    days40 = [d for d in X["UVXY"].k if VIX.at(d) >= 40 and add_m(d, 12) <= END]
    ev = [d for i, d in enumerate(days40) if i == 0 or (np.datetime64(d) - np.datetime64(days40[i - 1])).astype(int) > 60]
    c5["vix40"]["episodes"] = ev
    OUT["robust_2pct"] = {"spx_flat_1y_sh": flat(SPX, X["SH"], 12, 0.02), "qqq_flat_6m_sqqq": flat(X["QQQ"], X["SQQQ"], 6, 0.02),
                          "spx_flat_6m_spxu": flat(SPX, X["SPXU"], 6, 0.02)}
    OUT["choices"] = {"1": c1, "2": c2, "3": c3, "4": c4, "5": c5}
    for n_, c in OUT["choices"].items():
        log("CHOICE", n=n_, **{k: (L.pct(v) if isinstance(v, float) and k != "vix" and not k.startswith("vix") else v) for k, v in c.items()})
    # 임씨 경로 (다섯 번 모두 반대로): ① 1/3 지수 7천 + 1배 인버스 3천 ② 6/16 적금 1천 → 나스닥 3배 인버스 ③ 10/12 지수 7천을 모두 팔아 S&P 3배 인버스로
    #   ④ 2023-07-31 새로 모은 2천 → 지수 대신 1배 인버스(거품 걱정) ⑤ 2025-04-08 모은 2천 → 공포 지수 상품 · 모두 끝까지 그대로
    M = 1e4
    sh = 3000 * M * (1 + X["SH"].chg("2022-01-03", END)) + 2000 * M * (1 + X["SH"].chg("2023-07-31", END))
    sq = 1000 * M * (1 + X["SQQQ"].chg("2022-06-16", END))
    spxu = 7000 * M * (1 + TR.chg("2022-01-03", "2022-10-12")) * (1 + X["SPXU"].chg("2022-10-12", END))
    uv = 2000 * M * (1 + X["UVXY"].chg("2025-04-08", END))
    lim_end = sh + sq + spxu + uv
    # 옳은 길: 지수 7천 그대로 · 대비 3천 = 현금 · 적금 1천 = 현금 · ④ 2천 = 계획대로 지수 · ⑤ 2천 = 현금
    good_end = 7000 * M * (1 + TR.chg("2022-01-03", END)) + 3000 * M * (1 + C.chg("2022-01-03", END)) + 1000 * M * (1 + C.chg("2022-06-16", END)) \
        + 2000 * M * (1 + TR.chg("2023-07-31", END)) + 2000 * M * (1 + C.chg("2025-04-08", END))
    put_in = 15000
    OUT["paths"] = {"put_in_man": put_in, "lim_end_man": round(lim_end / M), "good_end_man": round(good_end / M), "lim_vs_put_in": round(lim_end / (put_in * M) - 1, 4),
                    "good_vs_put_in": round(good_end / (put_in * M) - 1, 4), "spx_4y": ch("SPX", "2022-01-03", END), "tr_4y": ch("TR", "2022-01-03", END),
                    "parts_man": {"SH": round(sh / M), "SQQQ": round(sq / M), "SPXU": round(spxu / M), "UVXY": round(uv / M)},
                    "biggest_loss_part": "SPXU (③ 바닥에서 지수 7천을 3배 인버스로)",
                    "note": "넣은 돈 1억 5천만 원(처음 1억 + 적금 1천 + 새로 모은 2천 + 모은 돈 2천) · 같은 날 같은 돈으로 옳은 길과 견줌"}
    log("PATH", **{k: v for k, v in OUT["paths"].items() if k != "note"})
    out = HERE / f"longform_b19_{date.today().isoformat()}.json"
    out.write_text(json.dumps(OUT, ensure_ascii=False, indent=1, default=str) + "\n", "utf-8")
    log("DONE", out=out.name)


if __name__ == "__main__":
    main()
