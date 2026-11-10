#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-11-04 — '1_매도후재매수.sold_to_end' 고침: 판 돈을 공포가 가라앉은 날 모두 다시 사면 끝 값 = 국채 이자 × TR(끝)/TR(다시 산 날) − 1.
#   옛 식은 '같은 돈으로 살 수 있는 주식이 8% 줄었다'(TR d1/TR d1b)를 두 번 곱해 0.4513(대본 '45%') — 2026-11-04 4편 장면 파일을 만들며 찾음 (옛 값은 sold_to_end_v10_bug 로 남김).
# (v1.0) — 2026-11-02 — 주식 롱폼 4편 대본 v9 (정씨) 숫자 — 대본 평가판 피드백 (사용자 원문, 2026-11-02):
#   "이건 폭락 중 공포에 매몰되지 않고 안전한 계획을 가지면서 매수할 수 있는지 테스트하는거야 항목 다시 쓰고 멘트좀 겹치지 않게 해봐 주제에 맞게"
#   → 다섯 선택 모두 '폭락 중 매수'의 다른 면: ① 첫 충격에 모두 매도·공포가 가라앉으면 재매수 vs 계획을 꺼냄 ② 무엇을 — 가장 많이 빠진 인기 종목 vs 지수
#     ③ 어떤 돈으로 — 빚(신용) vs 투자용으로 둔 돈만 ④ 반등에 — 남은 돈 한 번에 vs 계획의 다음 단계만 ⑤ 새 바닥에 — 멈추고 매도 vs 생활에 지장 없는 돈인지 확인하고 이어 감.
#   이야기 기간 = 2022-01-03(S&P 500 최고가 — '폭락이 시작된 날') ~ 2025-12-31 (4년 — 사용자 규칙 '기간은 4년 안').
# 자료(새로 받지 않음): longform_items.load() — calc/gspc_daily.csv(가격) · sp500tr_daily.csv(배당 포함) · irx_daily.csv(13주 국채) · precheck/data/VIX.csv
#   · precheck/data/MRNA.csv · NFLX.csv (수정 종가) · bulk/px/*.csv (지금 S&P 500 구성 종목 — 생존 편향, git 밖 · bulk_manifest.json).
# 가정(설명란 '계산 기준'에 그대로): 금액 = 원 × 달러 기준 변화율(환율·세금·수수료 뺌) · 넣지 않은 현금 = 13주 국채 이자 ·
#   빚(신용) = 연 8% 이자(매일 붙음) · 담보 비율(가진 주식 값 ÷ 빌린 돈과 이자)이 140% 아래로 내려간 날 종가에 모두 강제 매도(반대매매)하고 빚을 갚음.
# 실행: python3 -B stock/topics/precheck/longform_ep4.py → precheck/longform_ep4_<날짜>.json
# ※ 연구·교육용 — 투자 권유가 아님.
#
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.0 | 2026-11-02 | 최초 — 4편 v9 다섯 선택·정씨 경로·정답 경로·통계 | 전부 |
import csv
import json
import logging
import sys
from datetime import date
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import longform_items as L  # noqa: E402  (load·Ser·rd 재사용 — 그 파일은 고치지 않음)

VERSION = "v1.1"
log = logging.getLogger("longform_ep4")
PK, END = "2022-01-03", "2025-12-31"
LOAN_RATE, CALL = 0.08, 1.40
R = {}


def put(key, **kw):
    R[key] = kw
    log.info("key=%s %s", key, json.dumps(kw, ensure_ascii=False)[:600], extra={"stage": "EP4"})


def first(ser, cond, a, b):
    for k in ser.k[ser.i(a):ser.i(b) + 1]:
        if cond(k):
            return k
    return None


def bulk_ser(sym):
    p = HERE / "bulk" / "px" / f"{sym}.csv"
    rows = [r for r in csv.reader(p.open(encoding="utf-8")) if r and not r[0].startswith("#")][1:]
    return L.Ser(sym, {r[0]: float(r[2]) for r in rows if r[2]})


class Acct:
    """원 단위 계좌 (1 = 1억 원). 지수 = TR 좌수 · 종목 = 주 수 · 현금 = 국채 · 빚 = 연 8% 이자."""

    def __init__(self, S, cash):
        self.S, self.idx, self.stk, self.cash, self.loan = S, 0.0, 0.0, cash, 0.0
        self.last = None

    def roll(self, d):
        if self.last and d > self.last:
            self.cash *= self.S["CASH"].at(d) / self.S["CASH"].at(self.last)
            days = (date.fromisoformat(d) - date.fromisoformat(self.last)).days
            self.loan *= (1 + LOAN_RATE) ** (days / 365)
        self.last = d

    def value(self, d, M):
        return self.idx * self.S["TR"].at(d) + self.stk * M.at(d) + self.cash - self.loan


def ep4(S):
    tr, spx, vix, cash = S["TR"], S["SPX"], S["VIX"], S["CASH"]
    M, NF = S["MRNA"], S["NFLX"]
    peak = spx.at(PK)
    put("기간", start=PK, end=END, years=L.yrs(PK, END), spx_chg=round(spx.chg(PK, END), 4), tr_chg=round(tr.chg(PK, END), 4))
    vavg = float(np.mean([vix.at(k) for k in vix.k if k <= END]))
    # ── 날짜 (규칙으로 고름 — 결과를 보고 고르지 않음)
    d1 = first(vix, lambda k: vix.at(k) > 35, PK, END)                       # ① 2022년 공포 지수가 처음 35를 넘은 날
    d1b = first(vix, lambda k: vix.at(k) < 20, d1, END)                       # 공포가 가라앉은 날 = 처음 20 아래
    d2 = first(spx, lambda k: spx.at(k) <= peak * 0.85, PK, END)              # ② 지수가 최고가보다 처음 15% 넘게 빠진 날
    d3 = first(spx, lambda k: spx.at(k) <= peak * 0.80, PK, END)              # ③ 처음 20% 넘게 — 하락장
    jl, jld = spx.low(d3, "2022-07-29")                                        # 6월 바닥
    d4 = first(spx, lambda k: spx.at(k) >= spx.at(jld) * 1.15, jld, END)      # ④ 6월 바닥보다 처음 15% 넘게 반등한 날
    d5 = first(spx, lambda k: spx.at(k) < spx.at(jld), d4, END)               # ⑤ 6월 바닥 아래로 다시 내려간 날
    lo, lod = spx.low(PK, END)
    put("날짜", d1=d1, d1_vix=round(vix.at(d1), 2), d1_spx_dd=round(spx.at(d1) / peak - 1, 4), vix_avg_1990=round(vavg, 1),
        d1b=d1b, d1b_vix=round(vix.at(d1b), 2), d2=d2, d2_dd=round(spx.at(d2) / peak - 1, 4), d3=d3, d3_dd=round(spx.at(d3) / peak - 1, 4),
        june_low=jld, june_dd=round(spx.at(jld) / peak - 1, 4), d4=d4, d4_from_low=round(spx.at(d4) / spx.at(jld) - 1, 4),
        rally_peak=spx.k[spx.i(jld) + int(np.argmax(spx.v[spx.i(jld):spx.i(d5)]))], d5=d5, d5_dd=round(spx.at(d5) / peak - 1, 4),
        bottom=lod, bottom_dd=round(spx.at(lod) / peak - 1, 4))

    # ── ① 모두 매도 → 공포 지수 20 아래에서 재매수 vs 보유
    put("1_매도후재매수", sell=d1, sell_spx=round(spx.at(d1), 2), rebuy=d1b, rebuy_spx=round(spx.at(d1b), 2),
        rebuy_higher=round(spx.at(d1b) / spx.at(d1) - 1, 4), shares_kept=round(spx.at(d1) / spx.at(d1b), 4),
        hold_to_end=round(tr.chg(d1, END), 4),
        sold_to_end=round(cash.at(d1b) / cash.at(d1) * tr.at(END) / tr.at(d1b) - 1, 4),   # v1.1 판 돈(국채 이자 붙음)을 d1b 에 모두 다시 → 끝 (옛 식은 줄어든 주식 비율을 두 번 곱해 0.4513)
        sold_to_end_v10_bug=round((tr.at(d1) / tr.at(d1b)) * tr.chg(d1b, END) + (tr.at(d1) / tr.at(d1b)) - 1, 4),
        later_low_from_rebuy=round(spx.at(lod) / spx.at(d1b) - 1, 4))
    # 1990 이후: 공포 지수가 35를 넘은 첫날(그 전 60거래일 35 아래) 매도 → 처음 20 아래 재매수 — 재매수 값이 판 값보다 높았던 횟수
    ev, below = [], 0
    for i, k in enumerate(vix.k):
        if k > END or vix.v[i] <= 35:
            below += 1
            continue
        if below >= 60:
            rb = first(vix, lambda x: vix.at(x) < 20, k, vix.k[-1])
            if rb:
                ev.append((k, rb, round(spx.at(rb) / spx.at(k) - 1, 4)))
        below = 0
    put("1_역사", rule="VIX 35 초과 첫날(앞 60거래일 35 이하) 매도 → 처음 20 미만 재매수", events=ev,
        n=len(ev), rebuy_higher=sum(1 for e in ev if e[2] > 0))

    # ── ③ 가장 많이 빠진 인기 종목(모더나) vs 지수 — d2 매수
    put("3_모더나", day=d2, mrna_from_peak=round(M.at(d2) / max(M.v[:M.i(d2) + 1]) - 1, 4), mrna_peak_day=M.k[int(np.argmax(M.v[:M.i(d2) + 1]))],
        mrna_to_end=round(M.chg(d2, END), 4), mrna_worst=round(M.low(d2, END)[0], 4), mrna_worst_day=M.low(d2, END)[1],
        mrna_max_after=round(max(M.v[M.i(d2):M.i("2023-01-31")]) / M.at(d2) - 1, 4),
        mrna_max_day=M.k[M.i(d2) + int(np.argmax(M.v[M.i(d2):M.i("2023-01-31")]))],
        idx_to_end=round(tr.chg(d2, END), 4), idx_worst=round(tr.low(d2, END)[0], 4), idx_worst_day=tr.low(d2, END)[1],
        nflx_from_peak=round(NF.at(d2) / max(NF.v[NF.i("2021-05-09"):NF.i(d2) + 1]) - 1, 4), nflx_to_end=round(NF.chg(d2, END), 4))
    # 지금 S&P 500 구성 종목 중 그날 1년 최고가보다 가장 많이 빠진 5% — 그 뒤 2년
    names = {r["Symbol"]: r["Security"] for r in csv.DictReader((HERE / "bulk" / "constituents.csv").open(encoding="utf-8"))}
    y2 = f"{int(d2[:4]) + 2}{d2[4:]}"
    rows = []
    for sym in names:
        try:
            s = bulk_ser(sym)
        except (OSError, ValueError, IndexError):
            continue
        if s.k[0] > f"{int(d2[:4]) - 1}{d2[4:]}" or s.k[-1] < y2:
            continue
        i, j = s.i(d2), s.i(f"{int(d2[:4]) - 1}{d2[4:]}")
        rows.append((float(s.v[i] / np.max(s.v[j:i + 1]) - 1), sym, s.chg(d2, y2), s.low(d2, y2)[0]))
    rows.sort()
    top = rows[:max(1, len(rows) // 20)]
    i2y, ilo = tr.chg(d2, y2), tr.low(d2, y2)[0]
    put("3_역사", rule="지금 S&P 500 구성 종목 · 그날 1년 최고가 대비 하락 상위 5% · 그날 매수 → 2년", universe=len(rows), n=len(top),
        syms=[r[1] for r in top], worst_more_than_30=sum(1 for r in top if r[3] < -0.30), median_worst=round(float(np.median([r[3] for r in top])), 4),
        lag_index=sum(1 for r in top if r[2] < i2y), below_cost=sum(1 for r in top if r[2] < 0),
        idx_2y=round(i2y, 4), idx_worst_2y=round(ilo, 4), bias="생존 편향 — 그사이 빠진·망한 회사가 없어 하락 종목 쪽을 좋게 보이게 함(결론 반대쪽)")

    # ── ② 빚(신용) — 공포가 가라앉은 날(d1b) 가진 돈만큼 빌려(1:1) 지수 매수 · 1990 이후 하락장
    def margin_path(Ser_, d_own, own, d_loan, loan, end):
        sh = own / Ser_.at(d_own) + loan / Ser_.at(d_loan)
        debt, last, call = loan, d_loan, None
        for k in Ser_.k[Ser_.i(d_loan) + 1:Ser_.i(end) + 1]:
            debt *= (1 + LOAN_RATE) ** ((date.fromisoformat(k) - date.fromisoformat(last)).days / 365)
            last = k
            if sh * Ser_.at(k) < CALL * debt:
                call = k
                break
        if call:
            eq = sh * Ser_.at(call) - debt
            return {"call": call, "price_drop_from_loan_day": round(Ser_.at(call) / Ser_.at(d_loan) - 1, 4), "equity_at_call": round(eq, 4),
                    "equity_end": round(eq * cash.at(end) / cash.at(call), 4), "debt_at_call": round(debt, 4)}
        return {"call": None, "equity_end": round(sh * Ser_.at(end) - debt, 4)}
    def lev_equity(a, b, lev=1.0):
        out = []
        for k in tr.k[tr.i(a):tr.i(b) + 1]:
            debt_ = lev * (1 + LOAN_RATE) ** ((date.fromisoformat(k) - date.fromisoformat(a)).days / 365)
            out.append(((1 + lev) * tr.at(k) / tr.at(a) - debt_, k))
        return out
    le = lev_equity(d1b, END)
    w = min(le)
    put("2_빚", day=d1b, vix=round(vix.at(d1b), 2), rally_from_d1=round(spx.at(d1b) / spx.at(d1) - 1, 4), lev="1:1",
        equity_worst=round(w[0] - 1, 4), equity_worst_day=w[1], own_worst=round(tr.low(d1b, END)[0], 4),
        call_ratio_at_worst=round((2 * tr.at(w[1]) / tr.at(d1b)) / (1 + LOAN_RATE) ** ((date.fromisoformat(w[1]) - date.fromisoformat(d1b)).days / 365), 4),
        interest_to_worst=round((1 + LOAN_RATE) ** ((date.fromisoformat(w[1]) - date.fromisoformat(d1b)).days / 365) - 1, 4))
    # 1990 이후 하락장(가격이 최고가보다 20% 넘게 빠진 첫날) — 그날 1:1 로 빌려 지수를 샀다면 반대매매(빌린 날보다 약 30% 더 하락) 선까지 갔나
    bears, i, n = [], 0, len(spx.k)
    while i < n:
        k = spx.k[i]
        if k < "1990-01-01":
            i += 1
            continue
        pkd, _ = spx.peak_before(k)
        if spx.v[i] <= spx.at(pkd) * 0.80:
            back = spx.back(k, spx.at(pkd), after=k)
            mp2 = margin_path(spx, k, 1.0, k, 1.0, back or spx.k[-1])
            low2, lowd2 = spx.low(k, back or spx.k[-1])
            bears.append({"peak": pkd, "first_20": k, "further_low": round(low2, 4), "low_day": lowd2, "call": mp2.get("call")})
            i = spx.i(back) + 1 if back else n
            continue
        i += 1
    put("2_역사", rule="1990 이후 S&P 500 가격 최고가보다 처음 20% 넘게 빠진 날 1:1 신용 매수(연 8%, 담보 140%)", bears=bears,
        n=len(bears), calls=sum(1 for b in bears if b["call"]))

    # ── ④ 반등 — d4 에 남은 돈 한 번에 vs 계획의 다음 단계(최고가보다 25% 아래)만
    d_next = first(spx, lambda k: spx.at(k) <= peak * 0.75, d4, END)
    put("4_반등", day=d4, from_june_low=round(spx.at(d4) / spx.at(jld) - 1, 4), all_in_to_bottom=round(spx.at(lod) / spx.at(d4) - 1, 4),
        all_in_worst=round(tr.low(d4, END)[0], 4), all_in_to_end=round(tr.chg(d4, END), 4), next_step_day=d_next,
        next_step_dd=round(spx.at(d_next) / peak - 1, 4) if d_next else None, next_step_cheaper=round(spx.at(d_next) / spx.at(d4) - 1, 4) if d_next else None,
        plan_to_end=round(tr.chg(d_next, END), 4) if d_next else None)
    # 1990 이후 하락장 안에서: 그때까지 바닥보다 15% 넘게 반등한 첫날 → 그 뒤 더 낮은 바닥이 왔나
    rallies = []
    for b in bears:
        a, z = b["peak"], spx.back(b["first_20"], spx.at(b["peak"]), after=b["first_20"]) or spx.k[-1]
        run_lo, run_lod, armed = None, None, True
        for k in spx.k[spx.i(a):spx.i(z) + 1]:
            v = spx.at(k)
            if run_lo is None or v < run_lo:
                run_lo, run_lod, armed = v, k, True
            elif armed and v >= run_lo * 1.15 and v <= spx.at(a) * 0.95:
                later = spx.low(k, z)
                rallies.append({"day": k, "from_low": round(v / run_lo - 1, 4), "low_before": run_lod, "new_low_after": bool(later[0] < run_lo / v - 1), "next_low": later[1]})
                armed = False
    put("4_역사", rule="하락장(위 bears) 안 — 그때까지 바닥보다 처음 15% 넘게 반등한 날(최고가 5% 아래까지만) · 그 뒤 그 바닥보다 더 내려갔나",
        rallies=rallies, n=len(rallies), new_low=sum(1 for r in rallies if r["new_low_after"]))

    # ── ⑤ 새 바닥(d5) — 멈추고 매도 vs 이어 감
    put("5_새바닥", day=d5, dd=round(spx.at(d5) / peak - 1, 4), sell_to_end=round(cash.chg(d5, END), 4), hold_to_end=round(tr.chg(d5, END), 4),
        hold_worst=round(tr.low(d5, END)[0], 4), hold_worst_day=tr.low(d5, END)[1], back_to_peak=spx.back(d5, peak, after=d5))
    hist5 = []
    for b in bears:
        a = b["first_20"]
        prev_lo = spx.low(b["peak"], a)[1]
        z = spx.back(a, spx.at(b["peak"]), after=a) or spx.k[-1]
        # 하락장 들어선 뒤 처음 15% 반등 → 그 앞 바닥 아래로 다시 내려간 날
        r = next((x for x in rallies if b["peak"] <= x["day"] <= z and x["new_low_after"]), None)
        if not r:
            continue
        nl = first(spx, lambda k: spx.at(k) < spx.at(r["low_before"]), r["day"], z)
        y2d = f"{int(nl[:4]) + 2}{nl[4:]}"
        y4d = f"{int(nl[:4]) + 4}{nl[4:]}"
        hist5.append({"new_low": nl, "hold_2y": round(tr.chg(nl, y2d), 4), "cash_2y": round(cash.chg(nl, y2d), 4),
                      "hold_4y": round(tr.chg(nl, y4d), 4), "cash_4y": round(cash.chg(nl, y4d), 4)})
    put("5_역사", rule="하락장 안 첫 15% 반등 뒤 그 앞 바닥을 다시 깬 날 — 매도(국채) vs 보유, 2년", cases=hist5, n=len(hist5),
        hold_more=sum(1 for h in hist5 if h["hold_2y"] > h["cash_2y"]), hold_more_4y=sum(1 for h in hist5 if h["hold_4y"] > h["cash_4y"]))

    # ── 정씨 경로 (오답 다섯) — 1억 = 지수 6천만(최고가 날 매수) + 떨어지면 사려고 남긴 현금 4천만
    #    ① d1 지수 모두 매도 → ② d1b 공포가 가라앉자 판 돈으로 다시 사고, 판 돈만큼 빌려(신용) 더 매수 → ③ d2 지수 절반을 팔아 모더나
    #    → ④ d4 반등에 남겨 둔 현금 4천만을 한 번에 지수로 → ⑤ d5 지수 모두 매도·빚 갚고 멈춤 (모더나는 그대로) → 2025-12-31
    days = [k for k in tr.k if PK <= k <= END]
    idx, stk, c, res_, debt, last = 0.6 / tr.at(PK), 0.0, 0.0, 0.4, 0.0, PK
    ev, vals, ratio_min = [], [], 9.9
    for k in days:
        g = cash.at(k) / cash.at(last)
        c *= g
        res_ *= g
        debt *= (1 + LOAN_RATE) ** ((date.fromisoformat(k) - date.fromisoformat(last)).days / 365)
        last = k
        if k == d1:
            c += idx * tr.at(k); ev.append(("① 지수 모두 매도", k, round(idx * tr.at(k), 4))); idx = 0.0
        if k == d1b:
            debt = c; idx = 2 * c / tr.at(k); ev.append(("② 판 돈으로 다시 + 판 돈만큼 빌려 지수", k, round(c, 4), round(debt, 4))); c = 0.0
        if k == d2:
            half = idx * tr.at(k) / 2; idx /= 2; stk = half / M.at(k); ev.append(("③ 지수 절반을 팔아 모더나", k, round(half, 4)))
        if k == d4:
            idx += res_ / tr.at(k); ev.append(("④ 남겨 둔 현금 한 번에 지수", k, round(res_, 4))); res_ = 0.0
        if k == d5:
            got = idx * tr.at(k); c += got - debt; ev.append(("⑤ 지수 모두 매도·빚 갚음", k, round(got, 4), round(debt, 4))); idx, debt = 0.0, 0.0
        if debt > 0:
            ratio = (idx * tr.at(k) + stk * M.at(k)) / debt
            ratio_min = min(ratio_min, ratio)
            if ratio < CALL:
                ev.append(("반대매매", k)); c += idx * tr.at(k) + stk * M.at(k) - debt; idx, stk, debt = 0.0, 0.0, 0.0
        vals.append(idx * tr.at(k) + stk * M.at(k) + c + res_ - debt)
    put("정씨", events=ev, end_value=round(vals[-1], 4), loss=round(vals[-1] - 1, 4), worst=round(min(vals) - 1, 4),
        worst_day=days[int(np.argmin(vals))], mrna_end=round(stk * M.at(END), 4), mrna_in=round(next(e[2] for e in ev if e[0].startswith("③")), 4),
        cash_end=round(c, 4), min_collateral_ratio=round(ratio_min, 4), d5_loss_vs_start=round(vals[days.index(d5)] - 1, 4))

    # ── 정답 경로 — 지수 6천만 보유 + 현금 4천만은 예를 들어 최고가보다 10·15·20·25% 아래 날에 1천만 원씩 지수로, 빚 없음
    steps = [first(spx, lambda k, t=t: spx.at(k) <= peak * (1 - t), PK, END) for t in (0.10, 0.15, 0.20, 0.25)]
    idx, c, last, vals2 = 0.6 / tr.at(PK), 0.4, PK, []
    for k in days:
        c *= cash.at(k) / cash.at(last)
        last = k
        if k in steps:
            idx += 0.1 / tr.at(k); c -= 0.1
        vals2.append(idx * tr.at(k) + c)
    put("정답", steps=steps, end_value=round(vals2[-1], 4), worst=round(min(vals2) - 1, 4), worst_day=days[int(np.argmin(vals2))])
    return R


def main():
    logging.basicConfig(level=logging.INFO, format="[%(stage)s] %(message)s")
    S = L.load()
    for sym in ("MRNA", "NFLX"):
        S[sym] = L.Ser(sym, L.rd(HERE / "data" / f"{sym}.csv", "adjclose"))
    out = HERE / f"longform_ep4_{date.today().isoformat()}.json"
    res = ep4(S)
    out.write_text(json.dumps({"tool": f"longform_ep4.py {VERSION}", "data_last": S["TR"].k[-1], "assume": {"loan_rate": LOAN_RATE, "call_ratio": CALL,
                   "money": "1억 원 × 달러 기준 변화율 (환율·세금·수수료 뺌)", "cash": "13주 국채"}, "4편_v9": res}, ensure_ascii=False, indent=1), encoding="utf-8")
    log.info("file=%s keys=%d", out.name, len(res), extra={"stage": "DONE"})


if __name__ == "__main__":
    main()
