#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.5 — 2026-10-23 — 주인공 숫자를 B(손실 2억 5천 = 전재산의 70%)로 통일 (사용자 지시 2026-10-23 "손실은 70%로 하고").
#          가상 연표: 2026-06-18 계좌 순 2억 7,714만 + 보증금 8,000만 = 전재산 3억 5,714만(꼭대기) → 지금 계좌 평가 6,714만 − 마통 4,000만
#          = 순 2,714만 + 보증금 = 1억 714만. recovery_math·persona_april(6월 꼭대기에서 절반 매도했다면)·recover_b(투자할 수 있는 돈 = 순 2,714만)를
#          이 숫자로 다시 셈 · dca_10y 에 평균(mean_x) · months_to_recover(원금 2억 4천 회복 — 설정 A 기준)는 뺌. 넣은 돈(원금) 2억 4천·4월 원금 회복 +800만은 그대로.
# (v1.4) — 2026-10-22 — 테스트 대본 ①(국장 대신 미장): 코스피 '박스피'(2010-12 ~ 2017 무렵 1,900~2,000대) 기간의 S&P 500 가격 변화.
# (v1.3) — 2026-10-22 — 요약본 B(사용자 지시 "올해 반도체 주식 종목에 투자했다가 전재산의 -70%인 2억 5천을 손해봤어요"):
#          전재산·남은 돈·되찾을 배수 · 잃은 2억 5천을 '천천히' 되찾는 데 걸린 기간(남은 돈 + 매달 적립 / 매달 적립만, 20년 창).
# (v1.2) — 2026-10-21 — 3화 원금 회복한 날 절반 매도(설정 숫자) · 4화 매달 같은 금액 10년(여러 시작 달).
# (v1.1) — 2026-10-21 — 주인공 숫자(리딩방 비용·매매 횟수·수수료와 세금 — 가정 적음)·손실 수학 정확한 값·또 잃으면·하루 하락 비율.
# (v1.0) — 2026-10-21 — 새로: 개미 재기 일지 1~4화 대본 숫자 (사용자 지시 2026-10-21 "아래 주제들로 일본 축제 영상 대본 내용 만들 때 처럼
#          한 파일에 대본 내용, 제목 등 종합해서 넣어 … 그리고 시리즈물이라는 것도 고려해"). 대본의 숫자는 이 코드 출력(results.json)만 쓴다.
#          자료: S&P 500 월평균 가격(Shiller + FRED, datasets/s-and-p-500 커밋 고정 — tools/backtest/data.py) · FRED S&P 500 일별 종가(최근 약 10년).
#          **배당 빼고 가격만** (월별 배당은 2023-06 뒤 없음) → 지수에 남아 있던 사람의 결과는 실제보다 적게 나온다 (보수적).
#          환율·세금·수수료·현금 이자는 넣지 않는다 (대본 '한계'에 적음). 레버리지는 일별 3배 맞추기, 보수·이자 비용 없음 (실제 ETF 보다 좋게 나옴).
#          미래 정보 금지: 각 시점의 판단은 그 시점까지의 가격만 본다 (급등 판정 = 지난 6개월 가격). ※ 연구·교육용 — 투자 권유가 아니다.
"""python3 stock/story/calc/series_calc.py   → stock/story/calc/results.json (+ 로그)"""
import json
import logging
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
from backtest import data  # noqa: E402

VERSION = "v1.5"
OUT = Path(__file__).resolve().parent / "results.json"
LOG = logging.getLogger("series_calc")
START = "2000-01-01"          # 2000년 이후 (사례는 최근 먼저 — CLAUDE.md)

# 주인공 설정 (stock/story/protagonist.md v1.1 3번 — 만 원)
B_LOSS, B_SHARE = 25000, 0.70   # 손실 2억 5천 = 전재산의 70% (가상 — v1.5 부터 주인공 숫자)
P = dict(principal=24000, deposit=8000, minus_loan=4000, debt_june=8000, june_put_in=23600, monthly=100)
P["wealth_peak"] = round(B_LOSS / B_SHARE)                 # 2026-06-18 전재산 3억 5,714만 (꼭대기)
P["wealth_now"] = P["wealth_peak"] - B_LOSS                # 지금 1억 714만
P["peak_net"] = P["wealth_peak"] - P["deposit"]            # 6-18 계좌 순 2억 7,714만
P["net"] = P["wealth_now"] - P["deposit"]                  # 지금 계좌 순 2,714만 (투자할 수 있는 돈)
P["account"] = P["net"] + P["minus_loan"]                  # 지금 계좌 평가 6,714만


def log(stage, **kv):
    LOG.info("[%s] [%s] %s", stage, time.strftime("%Y-%m-%dT%H:%M:%S"), " ".join(f"{k}={v}" for k, v in kv.items()))


def recovery_math():
    """손실 → 되찾는 데 필요한 수익률. 주인공(B): 전재산 1억 714만 → 3억 5,714만 · 원금 2억 4천 대비 계좌 순 · '또 반을 잃으면'."""
    out = {str(loss): round(100 * (1 / (1 - loss / 100) - 1), 1) for loss in (10, 20, 30, 50, 70)}
    out["persona_loss_pct"] = round(100 * B_LOSS / P["wealth_peak"], 1)
    out["persona_need_x"] = round(P["wealth_peak"] / P["wealth_now"], 2)
    out["persona_need_pct"] = round(100 * (P["wealth_peak"] / P["wealth_now"] - 1), 1)
    out["principal_vs_net_pct"] = round(100 * (P["net"] / P["principal"] - 1), 1)
    half = P["net"] / 2
    out["again_half_wealth_만원"] = round(P["deposit"] + half)
    out["again_half_need_x"] = round(P["wealth_peak"] / (P["deposit"] + half), 2)
    log("RECOVERY", table=out)
    return out


def persona_costs():
    """설정의 가정으로 센 비용 (가상): 리딩방 월 30만 × 2021-01~2022-12 · 매매 약 1,200번(매수·매도 반씩), 한 번 평균 500만 원,
    수수료 0.015%(매수·매도마다) · 증권거래세 평균 0.18%(매도만 — 2020~2026 세율 0.15~0.25% 사이의 어림)."""
    reading_room = 30 * 24
    trades, avg, fee, tax = 1200, 500, 0.00015, 0.0018
    cost = trades * avg * fee + (trades / 2) * avg * tax
    months = 78
    out = dict(reading_room_만원=reading_room, trades=trades, trades_per_year=round(trades / (months / 12)),
               days_per_trade=round(months / 12 * 250 / trades, 1), fee_tax_만원=round(cost),
               assumptions="리딩방 30만×24개월 · 매매 1,200번·평균 500만 원·수수료 0.015%·거래세 평균 0.18%(매도) · 78개월·한 해 거래일 250")
    log("PERSONA_COSTS", **out)
    return out


def drawdowns(price: pd.Series, min_drop=0.15):
    """월평균 가격의 큰 하락 (고점 → 바닥 ≥ min_drop): 바닥에서 포기한 사람 vs 남은 사람 (고점에 1억 원)."""
    p = price.to_numpy()
    idx = price.index
    out, i = [], 0
    peak_i = 0
    while i < len(p):
        if p[i] >= p[peak_i]:
            peak_i = i
        dd = p[i] / p[peak_i] - 1
        if dd <= -min_drop:
            tr = i
            j = i
            while j < len(p) and p[j] < p[peak_i]:
                if p[j] < p[tr]:
                    tr = j
                j += 1
            rec = j if j < len(p) else None
            stay_5y = p[min(tr + 60, len(p) - 1)] / p[peak_i]
            out.append(dict(peak=str(idx[peak_i].date())[:7], trough=str(idx[tr].date())[:7], drop_pct=round(100 * (p[tr] / p[peak_i] - 1), 1),
                            quit_value_만원=round(10000 * p[tr] / p[peak_i]),
                            months_trough_to_peak=(rec - tr) if rec is not None else None,
                            stay_5y_after_trough_만원=round(10000 * stay_5y), stay_5y_end=str(idx[min(tr + 60, len(p) - 1)].date())[:7],
                            stay_now_만원=round(10000 * p[-1] / p[peak_i]), now=str(idx[-1].date())[:7]))
            peak_i = j if j < len(p) else len(p) - 1
            i = j
            continue
        i += 1
    log("DRAWDOWNS", n=len(out), detail=[(d["peak"], d["trough"], d["drop_pct"]) for d in out])
    return out


def holding_loss(price: pd.Series):
    p = price.to_numpy()
    out = {}
    for h in (1, 12, 36, 60, 120, 180):
        r = p[h:] / p[:-h] - 1
        out[f"{h}m"] = dict(windows=len(r), loss_share_pct=round(100 * float((r < 0).mean()), 1),
                            worst_pct=round(100 * float(r.min()), 1), best_pct=round(100 * float(r.max()), 1))
    log("HOLDING_LOSS", **{k: v["loss_share_pct"] for k, v in out.items()})
    return out


def lev3(daily: pd.Series):
    r = daily.pct_change().dropna()
    i1 = (1 + r).cumprod()
    i3 = (1 + (3 * r).clip(lower=-1)).cumprod()
    def dd(s):
        return round(100 * float((s / s.cummax() - 1).min()), 1)
    def between(s, a, b):
        sa, sb = s[s.index >= a].iloc[0], s[s.index <= b].iloc[-1]
        return round(100 * (sb / sa - 1), 1)
    out = dict(first=str(daily.index[0].date()), last=str(daily.index[-1].date()), trading_days=len(r),
               x1_multiple=round(float(i1.iloc[-1]), 2), x3_multiple=round(float(i3.iloc[-1]), 2),
               x1_max_drawdown_pct=dd(i1), x3_max_drawdown_pct=dd(i3),
               covid_x1_pct=between(i1, "2020-02-19", "2020-03-23"), covid_x3_pct=between(i3, "2020-02-19", "2020-03-23"),
               y2022_x1_pct=between(i1, "2022-01-03", "2022-10-12"), y2022_x3_pct=between(i3, "2022-01-03", "2022-10-12"),
               covid_x3_1억_to_만원=round(10000 * (1 + between(i3, "2020-02-19", "2020-03-23") / 100)))   # v1.5 예시 1억 (A 숫자 7,000만 대신)
    log("LEV3", **out)
    return out


def margin_call():
    """신용 담보유지비율 140%(통상 — 증권사·종목마다 다름): 내 돈 1억 + 신용 1억 = 2억 어치 → 평가액 < 1.4억 이면 반대매매."""
    own, loan, keep = 10000, 10000, 1.40
    drop = 1 - keep * loan / (own + loan)
    out = dict(own_만원=own, loan_만원=loan, keep_ratio=keep, position_drop_pct=round(100 * drop, 1),
               underlying_drop_if_2x_pct=round(100 * drop / 2, 1), own_left_at_call_만원=round((own + loan) * (1 - drop) - loan))
    log("MARGIN", **out)
    return out


def missing_best_days(daily: pd.Series):
    r = daily.pct_change().dropna()
    full = float((1 + r).prod())
    best = r.sort_values(ascending=False)
    worst_idx = set(r.sort_values().index[:20])
    pos = {d: k for k, d in enumerate(r.index)}
    near = sum(any(abs(pos[d] - pos[w]) <= 10 for w in worst_idx) for d in best.index[:10])
    out = dict(full_multiple=round(full, 2), down_day_share_pct=round(100 * float((r < 0).mean()), 1),
               miss10_multiple=round(float((1 + r.drop(best.index[:10])).prod()), 2),
               miss20_multiple=round(float((1 + r.drop(best.index[:20])).prod()), 2),
               best10_within_10days_of_worst20=int(near),
               best10_dates=[str(d.date()) for d in best.index[:10]])
    log("MISS_BEST", **{k: v for k, v in out.items() if k != "best10_dates"})
    return out


def persona_april():
    """가상 연표: 2026-04-27 순 2억 4,100만(넣은 돈 2억 3,300만 — 처음 원금 회복) → 6-18 순 2억 7,714만(넣은 돈 2억 3,600만, 꼭대기)
    → 지금 순 2,714만. 6-18 에 빚을 내지 않고 절반을 매도해 현금으로 뒀다면: 현금 절반(이자 0) + 남은 절반은 코스피 7월 하락 −34.01%
    (머니투데이 2026-07-30 — 실제 값)만큼 떨어졌다고 가정."""
    april, april_put, june, june_put, kospi_jul = 24100, 23300, P["peak_net"], P["june_put_in"], -0.3401
    half_cash = june / 2
    half_kept = june / 2 * (1 + kospi_jul)
    out = dict(april_net_만원=april, april_over_put_in_만원=april - april_put, june_net_만원=june, june_over_put_in_만원=june - june_put,
               now_net_만원=P["net"], lost_since_june_만원=june - P["net"], half_sold_june_만원=round(half_cash + half_kept),
               half_sold_better_만원=round(half_cash + half_kept - P["net"]), kospi_july_pct=round(100 * kospi_jul, 2))
    log("PERSONA_APRIL", **out)
    return out


def dca_10y(price: pd.Series, months=120, amount=100):
    """시작 달마다 매달 같은 금액(100만 원)을 120개월 넣었을 때 끝 값 vs 넣은 돈 (가격만, 그 달 가격으로 매수)."""
    p = price.to_numpy()
    res = []
    for s in range(len(p) - months + 1):
        units = sum(amount / p[s + j] for j in range(months))
        res.append(units * p[s + months - 1] / (amount * months))
    r = np.array(res)
    out = dict(starts=len(r), first_start=str(price.index[0].date())[:7], last_start=str(price.index[len(r) - 1].date())[:7],
               put_in_만원=amount * months, loss_share_pct=round(100 * float((r < 1).mean()), 1), loss_count=int((r < 1).sum()),
               median_x=round(float(np.median(r)), 2), mean_x=round(float(r.mean()), 2),   # v1.5 평균 (1화 대본 '평균 수익 배수')
               worst_x=round(float(r.min()), 2), best_x=round(float(r.max()), 2))
    log("DCA_10Y", **out)
    return out




def persona_b(quiet=False):
    """요약본 B 숫자 (가상): 손실 2억 5천 = 전재산의 70% → 손실 전 전재산·남은 돈·되찾으려면 몇 배."""
    loss, share = B_LOSS, B_SHARE
    before = loss / share
    left = before - loss
    out = dict(loss_만원=loss, share_pct=70, before_만원=round(before), left_만원=round(left),
               need_x=round(before / left, 2), need_pct=round(100 * (before / left - 1), 1),
               deposit_만원=P["deposit"], net_now_만원=P["net"], account_now_만원=P["account"], minus_loan_만원=P["minus_loan"])
    if not quiet:
        log("PERSONA_B", **out)
    return out


def months_to_gain(price: pd.Series, seed, monthly, target_gain, max_months=240):
    """시작 달마다: seed 를 넣고 매달 monthly 를 더 넣을 때, 계좌 − 넣은 돈 전체 ≥ target_gain 이 되는 첫 달 (가격만, 그 달 가격으로 매수).
    max_months 안에 자료가 다 없는 시작 달은 뺌. → 잃은 돈만큼 '번 돈'이 쌓이는 데 걸린 기간."""
    p = price.to_numpy()
    res = []
    for s in range(len(p)):
        if s + max_months >= len(p):
            break
        units = seed / p[s] if seed else 0.0
        hit = None
        for m in range(0, max_months + 1):
            if m > 0 or not seed:
                units += monthly / p[s + m]
            paid = seed + monthly * (m + (0 if seed else 1))
            if m > 0 and units * p[s + m] - paid >= target_gain:
                hit = m
                break
        res.append(hit)
    got = [m for m in res if m is not None]
    return dict(seed_만원=round(seed), monthly_만원=monthly, target_gain_만원=target_gain, window_months=max_months, starts=len(res),
                first_start=str(price.index[0].date())[:7], last_start=str(price.index[len(res) - 1].date())[:7],
                reached=len(got), not_reached=len(res) - len(got),
                median_years=round(float(np.median(got)) / 12, 1) if got else None,
                fastest_years=round(min(got) / 12, 1) if got else None, slowest_years=round(max(got) / 12, 1) if got else None)


def recover_b(price: pd.Series):
    b = persona_b(quiet=True)
    seed = P["net"]                                        # v1.5 투자할 수 있는 돈 = 계좌 순 2,714만 (보증금 8,000만은 집)
    out = dict(seed_plus_100=months_to_gain(price, seed, 100, b["loss_만원"]),
               seed_plus_200=months_to_gain(price, seed, 200, b["loss_만원"]),
               monthly_100_only=months_to_gain(price, 0, 100, b["loss_만원"]))
    for k, v in out.items():
        log("RECOVER_B", case=k, starts=v["starts"], reached=v["reached"], median_y=v["median_years"], fastest_y=v["fastest_years"], slowest_y=v["slowest_years"])
    return out


def boxpi_sp(price: pd.Series):
    """코스피가 2,000을 되찾은 2010-12(2010-12-14)부터 '7년여' 박스권(뉴시스 2021-01-07) 동안 S&P 500 월평균 가격 변화 — 2010-12 → 2016-12 · 2017-12."""
    a = float(price.loc["2010-12-01"])
    out = dict(start="2010-12", sp_2010_12=round(a, 1))
    for end in ("2016-12-01", "2017-12-01"):
        b = float(price.loc[end])
        out[f"to_{end[:7]}_pct"] = round(100 * (b / a - 1), 1)
    log("BOXPI_SP", **out)
    return out


def fomo(price: pd.Series, rally=0.15, look=6, hold=24, k=12):
    """급등 판정: 지난 look 개월 가격이 rally 이상 오른 달(그 달까지 가격만). 그 달에 1억 원을 한 번에 vs k 개월 나눠 (기다리는 돈 이자 0),
    hold 개월 뒤 값. 비교로 모든 달도 같은 계산."""
    p = price.to_numpy()
    def run(starts):
        lump, split = [], []
        for s in starts:
            e = s + hold
            if e >= len(p):
                continue
            lump.append(10000 * p[e] / p[s])
            units = sum((10000 / k) / p[s + j] for j in range(k))
            split.append(units * p[e])
        lump, split = np.array(lump), np.array(split)
        return dict(n=len(lump), lump_avg_만원=round(float(lump.mean())), split_avg_만원=round(float(split.mean())),
                    lump_worst_만원=round(float(lump.min())), split_worst_만원=round(float(split.min())),
                    lump_loss_share_pct=round(100 * float((lump < 10000).mean()), 1), split_loss_share_pct=round(100 * float((split < 10000).mean()), 1))
    rally_starts = [s for s in range(look, len(p)) if p[s] / p[s - look] - 1 >= rally]
    out = dict(rule=f"지난 {look}개월 +{int(rally * 100)}% 이상", hold_months=hold, split_months=k,
               rally_months=len(rally_starts), rally=run(rally_starts), all_months=run(range(look, len(p))))
    log("FOMO", rally_months=len(rally_starts), rally=out["rally"], all=out["all_months"])
    return out


def main():
    logging.basicConfig(level=logging.INFO, format="%(message)s", stream=sys.stderr)
    t0 = time.time()
    m, meta = data.sp500_monthly()
    price = m["price"].loc[START:].dropna()
    d = data.sp500_daily()
    daily = (d[0] if isinstance(d, tuple) else d).dropna()
    log("LOAD", monthly_first=str(price.index[0].date()), monthly_last=str(price.index[-1].date()), months=len(price),
        daily_first=str(daily.index[0].date()), daily_last=str(daily.index[-1].date()), days=len(daily), dataset_commit=data.DATASET_COMMIT)
    res = dict(version=VERSION, made=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), dataset_commit=data.DATASET_COMMIT,
               assumptions="S&P 500 가격만(배당 빼고) · 환율·세금·수수료·현금 이자 없음 · 3배는 일별 맞추기·비용 없음 · 월평균 가격",
               persona=P, persona_costs=persona_costs(), recovery_math=recovery_math(), drawdowns=drawdowns(price),
               holding_loss=holding_loss(price), lev3=lev3(daily), margin_call=margin_call(), missing_best_days=missing_best_days(daily),
               fomo=fomo(price), persona_april=persona_april(), dca_10y=dca_10y(price), persona_b=persona_b(), recover_b=recover_b(price), boxpi_sp=boxpi_sp(price))
    OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1), "utf-8")
    log("DONE", out=str(OUT.relative_to(ROOT)), sec=round(time.time() - t0, 1))


if __name__ == "__main__":
    main()
