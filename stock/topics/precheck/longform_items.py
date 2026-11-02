#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v2.2 — 2026-11-02 — 1편 대본 v9 (피드백판 1편 롱폼 10건) — nasdaq_1_v22(): 업스타트 · 현금 3천만 · 2025 관세 하락장 기준(비중 절반 → 3번 나눠) · C3.ai 펀더멘털 · 아이온큐 비중 · 김씨 경로 4년 안.
# (v2.1 — 2026-11-01 — 1편 다섯 습관(남 따라 사기·현금 없음·기준 없음·손절 안 함·분산 안 함) — nasdaq_1_v21() · MSTR 자료.
# (v2.0 — 2026-11-01 — 1편을 나스닥 100(QQQ)·QLD·ARKK·SMCI(AI 서버)로 (사용자 지시 "S&P500 말고 나스닥 지수로 해 … 전기차 회사라고 하지말고 최근 트렌드인 AI 관련 종목") — nasdaq_1().
# (v1.9 — 2026-11-01 — 반론 5회차(3편): 200일 규칙 판 횟수·손해 보고 판 수 · 버리 글 다음 날(2023-02-01) 기준 2년.
# (v1.8 — 2026-11-01 — 반론 4회차: 3편 200일 평균을 1988년부터(신호 29번) · 200일 규칙 다시 · 박씨 묶음 원금 회복·지금 · 2편 한꺼번에 vs 나눠 1990년대 · 1년 보유 손실 몫 · −20% 매도 하락장별.
# (v1.7 — 2026-11-01 — 반론 3회차 나머지: 한꺼번에 vs 나눠 2000 이후(20% 넘게 줄어든 몫·안정 몫) · −20% 매도 124번의 원금 · 200일 신호 배당 포함 · 정씨 정답(페이팔 10%).
# (v1.6 — 2026-11-01 — 반론 3회차: 테슬라 같은 날 · 김씨·정답 경로 지금까지.
# (v1.5 — 2026-11-01 — 반론 2회차 나머지: 이씨 여윳돈 2년 · 박씨 은행주+2배 · 200일 평균 사고팔기 규칙 · 경고 2년 · 2008 넉 달 나눠 vs 기다림 · −60% 날 뒤 · 정씨 정답 경로.
# (v1.4 — 2026-11-01 — 반론 2회차: 김씨 1번 = 한꺼번에(손절 항목 뺌 — 손절 뒤 현금은 정의상 안정 기준을 못 넘음) · 2배 지금까지 · 루시드 같은 기간 지수.
# (v1.3 — 2026-11-01 — 반론 검토 1회차 나머지: 금액은 달러(환율 뺌) · 김씨 4년 경로 · 2배가 더 번 상승기 · 신호 날 전부 매도 vs 보유(2·5년, 모든 신호) ·
#          유명인 경고 1년 안 가장 크게 빠진 폭 · 정씨 경로(8만 투자 + 2만 남김) · 바닥 나눠 넣기 vs 최고가 회복까지 기다리기 · 하락장 들어선 날 매달 매수 이어 가기 vs 멈춤(4·5년).
# (v1.2 — 2026-11-01 — 반론 검토 1회차 반영: 이씨 돈을 넷으로 나눔(계좌·비상금·전세금·5년 안 쓸 여윳돈) · 페이팔 10% 남김 · −20% 매도 vs 보유 5년(1990년 이후 매달 시작 전부).
# (v1.1 — 2026-11-01 — 사연 인물 경로(김씨·이씨·박씨·최씨·정씨) 더함 (사용자 지시 2026-11-01 "…항목을 한 사람의 케이스로 다 설명가능하고 시기가 달라서
#          그렇게 하기 힘들면 여러 사람 케이스로 해 사연 인물은 김씨, 이씨 등 성씨로 하고 … 대표 항목 5개로 줄여"). 함정 답만 고른 경로의 돈 · 항목 사이 기간의 변화.
# (v1.0 — 2026-10-31 — 최초.) 주식 롱폼 1~4편 대본(사용자 지시 2026-10-31 "롱폼 내용은 1편 쇼츠 처럼 도입부는 좋지 않은 사례인 A씨 사연을 짧게 … 항목 선택지는 …
#          2가지로만 … 시청자의 통념을 깨부술 수 있는 항목(틀리기 쉽도록) 반전 요소 … 항목의 상황은 예전 그 당시 과거 데이터로 재현하고 정답로 과거 데이터로 참고하면 돼
#          1~4편까지 롱폼 대본 다시 만들어")의 A씨 사연·항목 40개 숫자 — 대본의 숫자는 모두 이 파일 출력(또는 적힌 다른 계산 파일)에서.
# 자료(새로 받지 않음): calc/gspc_daily.csv(가격) · sp500tr_daily.csv(배당 포함) · irx_daily.csv(13주 국채) · precheck/data/*.csv · bulk/px/*.csv (adjclose — 분할·배당 반영) · VIX.csv
# 2배 상품(LEV2) = S&P 500 배당 포함 하루 수익 × 2 − (13주 국채 금리 + 총보수 0.9%)/252 (precheck.py portfolio 와 같은 계산 — 실제 상품이 아닌 재현).
# 실행: python3 -B stock/topics/precheck/longform_items.py → precheck/longform_items_<날짜>.json
# ※ 연구·교육용 — 투자 권유가 아님.
import bisect
import csv
import json
import logging
from datetime import date
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
CALC = HERE.parent.parent / "source" / "timing-test-2026-10" / "calc"
VERSION = "v2.2"
logging.basicConfig(level=logging.INFO, format="[%(stage)s] %(message)s")
log = logging.getLogger("longform_items")


def rd(path, col):
    with path.open(encoding="utf-8") as f:
        rows = [r for r in csv.reader(f) if r and not r[0].startswith("#")]
    k = rows[0].index(col)
    return {r[0]: float(r[k]) for r in rows[1:] if len(r) > k and r[k]}


class Ser:
    """날짜 → 값 (그날 값이 없으면 앞 거래일 값)."""

    def __init__(self, name, d):
        self.name, self.k = name, sorted(d)
        self.v = np.array([d[x] for x in self.k])

    def i(self, day):
        return max(0, bisect.bisect_right(self.k, day) - 1)

    def at(self, day):
        return float(self.v[self.i(day)])

    def day(self, day):
        return self.k[self.i(day)]

    def chg(self, a, b):
        return self.at(b) / self.at(a) - 1

    def low(self, a, b):
        """a 날 대비 a~b 사이 가장 낮은 값의 변화와 그 날."""
        i, j = self.i(a), self.i(b)
        m = i + int(np.argmin(self.v[i:j + 1]))
        return float(self.v[m] / self.v[i] - 1), self.k[m]

    def peak_before(self, a):
        i = self.i(a)
        m = int(np.argmax(self.v[:i + 1]))
        return self.k[m], float(self.v[i] / self.v[m] - 1)

    def back(self, a, level, after=None):
        """after(없으면 a) 뒤 처음으로 level 이상이 된 날 (없으면 None)."""
        s = self.i(after or a) + 1
        hit = np.nonzero(self.v[s:] >= level)[0]
        return None if not len(hit) else self.k[s + int(hit[0])]

    def first_below(self, a, frac):
        """a 날 값의 (1+frac) 아래로 처음 내려간 날 (frac = −0.5 면 반 토막)."""
        i = self.i(a)
        hit = np.nonzero(self.v[i:] <= self.v[i] * (1 + frac))[0]
        return None if not len(hit) else self.k[i + int(hit[0])]


def yrs(a, b):
    return round((date.fromisoformat(b) - date.fromisoformat(a)).days / 365.25, 1)


def months(a, b):
    return round((date.fromisoformat(b) - date.fromisoformat(a)).days / 30.44, 1)


def pct(x):
    return f"{x * 100:+.1f}%"


def load():
    spx = Ser("S&P 500 가격", rd(CALC / "gspc_daily.csv", "close"))
    tr = Ser("S&P 500 배당 포함", rd(CALC / "sp500tr_daily.csv", "close"))
    irx = Ser("13주 국채", rd(CALC / "irx_daily.csv", "close"))
    cash = [1.0]
    for a, b in zip(tr.k[:-1], tr.k[1:]):
        cash.append(cash[-1] * (1 + irx.at(a) / 100) ** ((date.fromisoformat(b) - date.fromisoformat(a)).days / 365))
    CASH = Ser("국채 현금", dict(zip(tr.k, cash)))
    r = np.concatenate([[0.0], tr.v[1:] / tr.v[:-1] - 1])
    rate = np.array([irx.at(d) for d in tr.k])
    LEV2 = Ser("2배 상품(재현)", dict(zip(tr.k, np.cumprod(1 + 2 * r - (rate / 100 + 0.009) / 252))))
    S = {"SPX": spx, "TR": tr, "CASH": CASH, "LEV2": LEV2, "VIX": Ser("공포 지수", rd(HERE / "data" / "VIX.csv", "close"))}
    for sym in ("ARKK", "META", "PYPL", "LCID", "XLK", "XLF", "AGG", "TSLA"):
        S[sym] = Ser(sym, rd(HERE / "data" / f"{sym}.csv", "adjclose"))
    log.info("loaded=%s spx=%s~%s", list(S), spx.k[0], spx.k[-1], extra={"stage": "LOAD"})
    return S


def buy(S, d0, years=2, months=1, panic=None):
    """d0 부터 years 년 — months 번에 나눠 매수(안 넣은 돈은 국채) · panic = 원금의 (1+panic) 아래로 처음 내려간 날 전부 매도하고 국채.
    → 끝 값(원금 1) · 가장 낮았던 값과 그날 · 매도한 날과 그때 값."""
    tr, cash = S["TR"], S["CASH"]
    i = tr.i(d0)
    j = tr.i(f"{int(tr.k[i][:4]) + years:04d}{tr.k[i][4:]}")
    y, m, dd = int(tr.k[i][:4]), int(tr.k[i][5:7]), tr.k[i][8:]
    buys = {i} | {bisect.bisect_left(tr.k, f"{y + (m - 1 + k) // 12:04d}-{(m - 1 + k) % 12 + 1:02d}-{dd}") for k in range(1, months)}   # 다음 달부터는 그날 또는 다음 거래일 (timing_cases.py 와 같음)
    c, u, worst, wday, sold = 1.0, 0.0, 1.0, tr.k[i], None
    for k in range(i, j + 1):
        if k in buys and sold is None:
            u += (1 / months) / tr.v[k]
            c -= 1 / months
        val = c + u * tr.v[k]
        if val < worst:
            worst, wday = val, tr.k[k]
        if panic is not None and sold is None and val < 1 + panic:
            sold, c, u = (tr.k[k], round(val, 4)), val, 0.0
        if k < j:
            c *= cash.v[k + 1] / cash.v[k]
    return {"start": tr.k[i], "end": tr.k[j], "end_value": round(c + u * tr.v[j], 4), "worst": round(worst - 1, 4), "worst_day": wday, "sold": sold}


def facts(S):
    spx, tr, lev, vix = S["SPX"], S["TR"], S["LEV2"], S["VIX"]
    F = {}

    def put(ep, key, **kw):
        F.setdefault(ep, {})[key] = kw
        log.info("ep=%s key=%s %s", ep, key, json.dumps(kw, ensure_ascii=False), extra={"stage": "ITEM"})

    def stock(ep, key, sym, d0, low_to="2026-10-28"):
        s = S[sym]
        lo, lday = s.low(d0, low_to)
        put(ep, key, sym=sym, day=s.day(d0), prior_1y=pct(s.chg(f"{int(d0[:4]) - 1}{d0[4:]}", d0)), low=pct(lo), low_day=lday,
            now=pct(s.chg(d0, s.k[-1])), now_day=s.k[-1], back=s.back(d0, s.at(d0), after=lday),
            sp500_same_low=pct(tr.low(d0, lday)[0]), sp500_same_now=pct(tr.chg(d0, tr.k[-1])))

    # ===== 1편 — 빨리 벌고 싶다는 생각
    stock(1, "A씨_ARKK", "ARKK", "2021-02-12")
    stock(1, "1_LCID", "LCID", "2021-11-16")
    for d0 in ("2007-10-09",):
        b = f"{int(d0[:4]) + 2}{d0[4:]}"
        put(1, "2_LEV2_" + d0, lev_back=lev.back(d0, lev.at(d0), after=lev.low(d0, b)[1]), tr_back=tr.back(d0, tr.at(d0), after=tr.low(d0, b)[1]), lev_low=pct(lev.low(d0, b)[0]), tr_low=pct(tr.low(d0, b)[0]), lev_2y=pct(lev.chg(d0, b)), tr_2y=pct(tr.chg(d0, b)))
    # 3. −10% 손절 (2020-02-19 최고가 매수 → 처음 −10% 아래 날 매도 → 국채) vs 보유
    d_stop = tr.first_below("2020-02-19", -0.10)
    sold_val = tr.at(d_stop) / tr.at("2020-02-19")
    put(1, "3_stop", buy_day="2020-02-19", stop_day=d_stop, stop_value=pct(sold_val - 1), hold_low=pct(tr.low("2020-02-19", "2020-12-31")[0]),
        hold_back=tr.back("2020-02-19", tr.at("2020-02-19"), after=d_stop), hold_1y=pct(tr.chg("2020-02-19", "2021-02-19")),
        stop_1y=pct(sold_val * (1 + S["CASH"].chg(d_stop, "2021-02-19")) - 1))
    put(1, "5_lump_split_2022-01-03", lump=buy(S, "2022-01-03"), split=buy(S, "2022-01-03", months=12))
    stock(1, "6_META", "META", "2021-09-07")
    # 7. 1년 수익 20% — 1990년 이후 매일 시작한 1년 (배당 포함)
    i90 = tr.i("1990-01-02")
    one = []
    for k in range(i90, len(tr.k)):
        e = tr.i(f"{int(tr.k[k][:4]) + 1}{tr.k[k][4:]}")
        if e >= len(tr.k) - 1 and tr.k[-1] < f"{int(tr.k[k][:4]) + 1}{tr.k[k][4:]}":
            break
        one.append(tr.v[e] / tr.v[k] - 1)
    one = np.array(one)
    put(1, "7_1y_20pct", n=len(one), ge20=pct(float(np.mean(one >= 0.20))), lt0=pct(float(np.mean(one < 0))), median=pct(float(np.median(one))))
    put(1, "8_2000", tr_1y=pct(tr.chg("2000-01-03", "2001-01-03")), tr_12y=pct(tr.chg("2000-01-03", "2012-01-03")), tr_now=pct(tr.chg("2000-01-03", tr.k[-1])))
    i0, i1 = spx.i("2021-12-31"), spx.i("2022-12-30")
    put(1, "9_2022_daily", down_days=int(np.sum(np.diff(spx.v[i0:i1 + 1]) < 0)), days=int(i1 - i0), tr_2022=pct(tr.chg("2021-12-31", "2022-12-30")))
    put(1, "10_ARKK_vs_TR_2022-10-12", arkk_2y=pct(S["ARKK"].chg("2022-10-12", "2024-10-11")), tr_2y=pct(tr.chg("2022-10-12", "2024-10-11")),
        arkk_low=pct(S["ARKK"].low("2022-10-12", "2024-10-11")[0]), tr_low=pct(tr.low("2022-10-12", "2024-10-11")[0]),
        arkk_from_peak=pct(S["ARKK"].peak_before("2022-10-12")[1]), tr_from_peak=pct(tr.peak_before("2022-10-12")[1]))

    # ===== 2편 — 계속 오르겠지
    put(2, "A씨_2022-01-03", r=buy(S, "2022-01-03", panic=-0.20), hold=buy(S, "2022-01-03"))
    ath = [k for k in range(1, len(spx.v)) if spx.v[k] > spx.v[:k].max()]
    put(2, "1_2021", ath_2021=sum(1 for k in ath if spx.k[k][:4] == "2021"), tr_2021=pct(tr.chg("2020-12-31", "2021-12-31")),
        tr_2022=pct(tr.chg("2021-12-31", "2022-12-30")), low_2022=pct(spx.low("2022-01-03", "2022-12-30")[0]))
    lo, ld = spx.low("2024-01-19", spx.k[-1])
    put(2, "2_2024-01-19", low_after=pct(lo), low_day=ld, now=pct(spx.chg("2024-01-19", spx.k[-1])), tr_now=pct(tr.chg("2024-01-19", tr.k[-1])))
    put(2, "3_2020-02-19", lump=buy(S, "2020-02-19"), split=buy(S, "2020-02-19", months=12))
    xl, xd = S["XLK"].low("2000-03-27", "2003-12-31")
    sl, sd = tr.low("2000-03-24", "2003-12-31")
    put(2, "4_2000_tech", xlk_prior_1y=pct(S["XLK"].chg("1999-03-26", "2000-03-27")), xlk_low=pct(xl), xlk_back=S["XLK"].back("2000-03-27", S["XLK"].at("2000-03-27"), after=xd),
        tr_low=pct(sl), tr_back=tr.back("2000-03-24", tr.at("2000-03-24"), after=sd))
    stock(2, "5_PYPL_peak", "PYPL", "2021-07-23")
    put(2, "6_2007-10-09_6040", note="purpose_numbers_2026-10-31.json A '2003-09 부터' — 주식만 −55.3% 4.5년 · 주식 60·채권 40 −34.0% 3.1년 (고점 2007-10-09)")
    put(2, "8_2018-09-20_lev", lev_low=pct(lev.low("2018-09-20", "2018-12-31")[0]), tr_low=pct(tr.low("2018-09-20", "2018-12-31")[0]),
        lev_low_2y=pct(lev.low("2018-09-20", "2020-09-20")[0]), tr_low_2y=pct(tr.low("2018-09-20", "2020-09-20")[0]))

    # ===== 3편 — 위험 신호
    xf, xfd = S["XLF"].low("2007-08-03", "2012-12-31")
    put(3, "A씨_XLF_2007-08-03", xlf_from_peak=pct(S["XLF"].peak_before("2007-08-03")[1]), low=pct(xf), low_day=xfd,
        back=S["XLF"].back("2007-08-03", S["XLF"].at("2007-08-03"), after=xfd), spx_from_peak=pct(spx.peak_before("2007-08-03")[1]),
        vix=round(vix.at("2007-08-03"), 1))
    for key, d0, b in (("2_2022-11-10_역전", "2022-11-10", "2024-11-08"), ("3_2018-12-21_VIX30", "2018-12-21", "2020-12-21"), ("5_2015-08-24", "2015-08-24", "2017-08-24")):
        put(3, key, spx_from_peak=pct(spx.peak_before(d0)[1]), tr_2y=pct(tr.chg(d0, b)), tr_low=pct(tr.low(d0, b)[0]), vix=round(vix.at(d0), 1))
    put(3, "1_2007-08-03_200일", spx_from_peak=pct(spx.peak_before("2007-08-03")[1]), to_trough=pct(spx.low("2007-08-03", "2009-12-31")[0]))
    xl2, xd2 = S["XLK"].low("2000-04-14", "2003-12-31")
    put(3, "4_2000-04-14_tech", xlk_from_peak=pct(S["XLK"].peak_before("2000-04-14")[1]), xlk_low=pct(xl2), xlk_low_day=xd2, spx_low=pct(spx.low("2000-04-14", "2003-12-31")[0]))
    put(3, "6_2006-08-01_역전", rise_to_peak=pct(spx.chg("2006-08-01", "2007-10-09")), months=round(yrs("2006-08-01", "2007-10-09") * 12),
        peak_to_trough=pct(spx.chg("2007-10-09", "2009-03-09")))
    put(3, "10_2015-07-08_200일", spx_from_peak=pct(spx.peak_before("2015-07-08")[1]), tr_2y=pct(tr.chg("2015-07-08", "2017-07-07")), tr_low=pct(tr.low("2015-07-08", "2017-07-07")[0]))
    t48 = json.loads((HERE / "t048_sell_vs_hold.json").read_text(encoding="utf-8"))["results"]
    put(3, "5_2023-01-31_버리", **next(r for r in t48 if r["date"] == "2023-01-31"), spx_from_peak=pct(spx.peak_before("2023-01-31")[1]))
    put(3, "7_2022-01-21_lev", spx_from_peak=pct(spx.peak_before("2022-01-21")[1]), lev_low=pct(lev.low("2022-01-21", "2022-12-31")[0]), tr_low=pct(tr.low("2022-01-21", "2022-12-31")[0]))

    # ===== 4편 — 공포 속 매수
    put(4, "A씨_2020-02-19", r=buy(S, "2020-02-19", panic=-0.20), hold=buy(S, "2020-02-19"), sale_vix=round(vix.at("2020-03-12"), 1),
        tr_back=tr.back("2020-02-19", tr.at("2020-02-19"), after="2020-03-23"))
    put(4, "1_2008-09-29", vix=round(vix.at("2008-09-29"), 1), lump=buy(S, "2008-09-29"), split=buy(S, "2008-09-29", months=12))
    put(4, "2_2020-03-23", vix=round(vix.at("2020-03-23"), 1), spx_from_peak=pct(spx.peak_before("2020-03-23")[1]), lump=buy(S, "2020-03-23"), cash_2y=pct(S["CASH"].chg("2020-03-23", "2022-03-23")))
    put(4, "3_2008-10-10", spx_from_peak=pct(spx.peak_before("2008-10-10")[1]), lump=buy(S, "2008-10-10"), split=buy(S, "2008-10-10", months=12))
    put(4, "4_2009-03-09", vix=round(vix.at("2009-03-09"), 1), spx_from_peak=pct(spx.peak_before("2009-03-09")[1]), lump=buy(S, "2009-03-09"),
        back_to_2007_peak_tr=tr.back("2009-03-09", tr.at("2007-10-09")))
    put(4, "6_2022-06-13", spx_from_peak=pct(spx.peak_before("2022-06-13")[1]), split=buy(S, "2022-06-13", months=12), cash_2y=pct(S["CASH"].chg("2022-06-13", "2024-06-13")))
    put(4, "7_2001-09-17_lev", vix=round(vix.at("2001-09-17"), 1), lev_low=pct(lev.low("2001-09-17", "2003-09-17")[0]), tr_low=pct(tr.low("2001-09-17", "2003-09-17")[0]),
        lev_2y=pct(lev.chg("2001-09-17", "2003-09-17")), tr_2y=pct(tr.chg("2001-09-17", "2003-09-17")))
    d60 = S["PYPL"].first_below("2021-07-23", -0.6)
    stock(4, "8_PYPL_-60", "PYPL", d60)
    put(4, "9_2020-08-10", tr_to_2021_end=pct(tr.chg("2020-08-10", "2021-12-31")), tr_now=pct(tr.chg("2020-08-10", tr.k[-1])))
    put(4, "10_2025-04-08", vix=round(vix.at("2025-04-08"), 1), spx_from_peak=pct(spx.peak_before("2025-04-08")[1]), tr_now=pct(tr.chg("2025-04-08", tr.k[-1])),
        spx_low_after=pct(spx.low("2025-04-08", spx.k[-1])[0]), spx_back=spx.back("2025-04-08", spx.at(spx.peak_before("2025-04-08")[0])))
    return F


def paths(S):
    """사연 인물이 함정 답만 골랐을 때의 돈 (원금 1) — 대본 도입·해설의 숫자."""
    tr, cash, lev, spx = S["TR"], S["CASH"], S["LEV2"], S["SPX"]
    P = {}

    def put(key, **kw):
        P[key] = kw
        log.info("path=%s %s", key, json.dumps(kw, ensure_ascii=False), extra={"stage": "PATH"})

    # 김씨 (1편): 최고가 매수 → −10% 손절(현금) → 기술 펀드 전부 → 전기차 회사 전부 → 2배 상품 전부 → 가장 많이 빠진 기술 펀드 전부
    d1 = tr.first_below("2020-02-19", -0.10)
    steps = [("손절 (S&P 500 → 현금)", "TR", "2020-02-19", d1), ("현금 (국채)", "CASH", d1, "2021-02-12"), ("기술 펀드 ARKK", "ARKK", "2021-02-12", "2021-11-16"),
             ("전기차 회사 LCID", "LCID", "2021-11-16", "2022-01-03"), ("2배 상품", "LEV2", "2022-01-03", "2022-10-12"), ("기술 펀드 ARKK", "ARKK", "2022-10-12", "2024-10-11")]
    v, rows = 1.0, []
    for name, sym, a, b in steps:
        c = S[sym].chg(a, b)
        v *= 1 + c
        rows.append({"step": name, "from": a, "to": b, "chg": pct(c), "value": round(v, 4)})
    put("김씨", steps=rows, value_at_last_choice=rows[4]["value"], value_2y_after=rows[5]["value"],
        hold_tr_to_last_choice=round(1 + tr.chg("2020-02-19", "2022-10-12"), 4), hold_tr_2y_after=round(1 + tr.chg("2020-02-19", "2024-10-11"), 4),
        years_to_last_choice=yrs("2020-02-19", "2022-10-12"), months_steps=[months(a, b) for _, _, a, b in steps])
    # 이씨 (2편): 1억 한꺼번에 2022-01-03 → 2022-06-13 원금 80% 아래 첫날 매도 (facts.2 A씨_2022-01-03 와 같음) + 페이팔 비중
    # 계좌 1억(페이팔 7천만 · 지수 3천만, 2021-07-23) + 비상금 2천만 · 전세금 8천만(2022-01-03 한꺼번에 1억) → 2022-06-13 모두 매도 (만 원)
    pyp = 7000 * (1 + S["PYPL"].chg("2021-07-23", "2022-06-13"))
    idx = 3000 * (1 + tr.chg("2021-07-23", "2022-06-13"))
    lump = 10000 * (1 + tr.chg("2022-01-03", "2022-06-13"))
    hold2 = 7000 * (1 + S["PYPL"].chg("2021-07-23", "2024-01-03")) + 3000 * (1 + tr.chg("2021-07-23", "2024-01-03")) + 10000 * (1 + tr.chg("2022-01-03", "2024-01-03"))
    plan = 3000 * (1 + tr.chg("2021-07-23", "2022-06-13")) + 7000 * (1 + tr.chg("2021-07-23", "2022-06-13"))   # 함정을 피했다면: 페이팔 비중을 지수로 덜어 냄 · 비상금·전세금은 예금
    put("이씨", pypl_to_2022_06_13=pct(S["PYPL"].chg("2021-07-23", "2022-06-13")), months_jan_to_jun=months("2022-01-03", "2022-06-13"),
        sold_total_manwon=round(pyp + idx + lump), parts_manwon={"페이팔": round(pyp), "지수": round(idx), "새해 1억": round(lump)}, put_in_manwon=20000,
        loss_manwon=round(20000 - (pyp + idx + lump)), hold_all_2024_01_03_manwon=round(hold2),
        no_trap_account_2022_06_13_manwon=round(plan), deposit_cash_2022_06_13_manwon=round(10000 * (1 + cash.chg("2022-01-03", "2022-06-13"))))
    # 박씨 (3편): 신호 날 2배 상품 → 두 달 뒤 최고가 → 바닥
    put("박씨", lev_signal_to_peak=pct(lev.chg("2007-08-03", "2007-10-09")), lev_peak_to_trough=pct(lev.chg("2007-10-09", "2009-03-09")),
        lev_signal_to_trough=pct(lev.chg("2007-08-03", "2009-03-09")), spx_signal_to_peak=pct(spx.chg("2007-08-03", "2007-10-09")))
    # 최씨 (3편): 금리 역전 날 전부 매도 → 석 달 뒤 다시 매수 → 유명 투자자 '팔아라'
    put("최씨", spx_inversion_to_rebuy=pct(spx.chg("2022-11-10", "2023-01-31")), tr_inversion_2y=pct(tr.chg("2022-11-10", "2024-11-08")))
    # 정씨 (4편): 최고가 매수 → 공포에 매도 → 지수가 다시 그 최고가로 → 결제 회사 −60% → 하락장
    sale = spx.at("2020-03-12")
    lo, ld = spx.low("2020-08-10", spx.k[-1])
    put("정씨", sale_value=round(1 + tr.chg("2020-02-19", "2020-03-12"), 4), spx_aug_vs_sale=pct(spx.at("2020-08-10") / sale - 1),
        spx_min_after_aug_vs_sale=pct(spx.at(ld) / sale - 1), spx_min_after_aug_day=ld, months_mar12_to_aug10=months("2020-03-12", "2020-08-10"), months_mar23_to_aug10=months("2020-03-23", "2020-08-10"),
        years_aug_to_pypl=yrs("2020-08-10", "2022-02-07"), months_pypl_to_bear=months("2022-02-07", "2022-06-13"),
        vix_median_1990=round(float(np.median(S["VIX"].v)), 1), vix_on_sale=round(S["VIX"].at("2020-03-12"), 1),
        spx_price_back_to_peak=spx.back("2020-02-19", spx.at("2020-02-19"), after="2020-03-23"))

    # 이씨 v1.2 (2편 반론 1회차): 계좌 1억(2021-07-23 페이팔 7천 · 지수 3천) · 비상금 2천 · 전세금 8천 · 여윳돈 5천(5년 넘게 안 씀, 2022-01-03)
    #   함정: 페이팔 그대로 · 비상금·전세금 2022-01-03 지수에 · 여윳돈 한꺼번에 · 2022-06-13 모두 매도
    #   함정 없이: 페이팔 10%만(나머지 지수) · 비상금·전세금 예금 · 여윳돈 12개월 나눠 · 보유
    e = "2022-06-13"
    trap = (7000 * (1 + S["PYPL"].chg("2021-07-23", e)) + 3000 * (1 + tr.chg("2021-07-23", e)) + 10000 * (1 + tr.chg("2022-01-03", e)) + 5000 * (1 + tr.chg("2022-01-03", e)))
    sp = buy(S, "2022-01-03", years=2, months=12)
    i_e = tr.i(e)
    # 나눠 매수 중 그날 값: buy() 와 같은 일정으로 다시 셈
    y, m, dd = 2022, 1, "03"
    sched = [tr.i("2022-01-03")] + [bisect.bisect_left(tr.k, f"{y + (m - 1 + k) // 12:04d}-{(m - 1 + k) % 12 + 1:02d}-{dd}") for k in range(1, 12)]
    c, u = 1.0, 0.0
    for k in range(tr.i("2022-01-03"), i_e + 1):
        if k in sched:
            u += (1 / 12) / tr.v[k]
            c -= 1 / 12
        if k < i_e:
            c *= cash.v[k + 1] / cash.v[k]
    split_e = c + u * tr.v[i_e]
    good = (1000 * (1 + S["PYPL"].chg("2021-07-23", e)) + 9000 * (1 + tr.chg("2021-07-23", e)) + 10000 * (1 + cash.chg("2022-01-03", e)) + 5000 * split_e)
    put("이씨_v1.2", put_in_manwon=25000, trap_sold_manwon=round(trap), trap_loss_manwon=round(25000 - trap), no_trap_same_day_manwon=round(good),
        spare_lump_on_day=round(1 + tr.chg("2022-01-03", e), 4), spare_split_on_day=round(split_e, 4), spare_lump_2y=round(1 + tr.chg("2022-01-03", "2024-01-03"), 4),
        spare_split_2y=sp["end_value"], spare_lump_5y=round(1 + tr.chg("2022-01-03", "2027-01-03") if tr.k[-1] >= "2027-01-03" else 1 + tr.chg("2022-01-03", tr.k[-1]), 4),
        jeonse_part_on_day_manwon=round(8000 * (1 + tr.chg("2022-01-03", e))), jeonse_part_2022_12_30_manwon=round(8000 * (1 + tr.chg("2022-01-03", "2022-12-30"))),
        pypl70_half_hit=pct(-0.35))
    # −20% 매도 vs 보유 — 1990년 이후 매달 첫 거래일에 한꺼번에 산 뒤 5년 안에 원금의 80% 아래로 간 때 전부: 5년 뒤 보유 vs (그날 매도 → 국채)
    starts = [k for k in range(1, len(tr.k)) if tr.k[k][:7] != tr.k[k - 1][:7] and tr.k[k] >= "1990-01-01"]
    rows = []
    for k0 in starts:
        e5 = tr.i(f"{int(tr.k[k0][:4]) + 5:04d}{tr.k[k0][4:]}")
        if tr.k[-1] < f"{int(tr.k[k0][:4]) + 5:04d}{tr.k[k0][4:]}":
            break
        seg = tr.v[k0:e5 + 1] / tr.v[k0]
        hit = np.nonzero(seg < 0.8)[0]
        if not len(hit):
            continue
        ks = k0 + int(hit[0])
        hold = float(seg[-1])
        sold = float(seg[hit[0]] * cash.v[e5] / cash.v[ks])
        rows.append((tr.k[k0], hold, sold))
    hb = [h > s_ for _, h, s_ in rows]
    put("매도20_vs_보유_5년", n=len(rows), hold_better=sum(hb), share=pct(float(np.mean(hb)) if rows else float("nan")),
        median_hold=round(float(np.median([h for _, h, _ in rows])), 3), median_sold=round(float(np.median([s_ for _, _, s_ in rows])), 3),
        sold_better_starts=sorted({d[:7] for (d, h, s_) in rows if s_ >= h})[:40], first=rows[0][0] if rows else None, last=rows[-1][0] if rows else None)

    # ---------- v1.3 (반론 1회차)
    # 1편 김씨: 2배 상품을 산 뒤 2년(2024-01-03)까지 · 처음 지수를 그대로 · 2배가 더 번 상승기
    v4 = P["김씨"]["steps"][3]["value"]
    k_end = "2024-01-03"
    put("김씨_v1.3", value_2024_01_03=round(v4 * (1 + lev.chg("2022-01-03", k_end)), 4), hold_tr_2024_01_03=round(1 + tr.chg("2020-02-19", k_end), 4),
        years=yrs("2020-02-19", k_end), lev_bull_2009_2021=pct(lev.chg("2009-03-09", "2021-12-31")), tr_bull_2009_2021=pct(tr.chg("2009-03-09", "2021-12-31")),
        lev_low_2001=pct(lev.low("2001-09-17", "2003-09-17")[0]), tr_low_2001=pct(tr.low("2001-09-17", "2003-09-17")[0]))
    # 3편: 신호 날 전부 매도(현금) vs 보유 — 2년·5년 (crash_tests 와 같은 신호 정의: 60거래일 꺼졌다가 처음 켜진 날)
    vix, tnx = S["VIX"], Ser("10년 국채", rd(HERE / "data" / "TNX.csv", "close"))
    irx = Ser("13주", rd(CALC / "irx_daily.csv", "close"))
    ds = [d for d in spx.k if d >= "1990-01-02"]
    pxv = np.array([spx.at(d) for d in ds])
    ma = np.array([np.nan] * 199 + [float(pxv[i - 199:i + 1].mean()) for i in range(199, len(pxv))])
    sigs = {"200일 평균 아래": pxv < ma, "공포 지수 30 넘음": np.array([vix.at(d) > 30 for d in ds]), "장단기 금리 역전": np.array([tnx.at(d) - irx.at(d) < 0 for d in ds])}
    out = {}
    for name, on in sigs.items():
        on = np.where(np.isnan(on.astype(float)), False, on)
        starts, last = [], -10 ** 9
        for i, x in enumerate(on):
            if x:
                if i - last > 60:
                    starts.append(ds[i])
                last = i
        res = {}
        for yy in (2, 5):
            rows = []
            for d in starts:
                e = f"{int(d[:4]) + yy:04d}{d[4:]}"
                if e > tr.k[-1]:
                    continue
                rows.append((d, 1 + tr.chg(d, e), 1 + cash.chg(d, e)))
            res[f"{yy}년"] = {"n": len(rows), "hold_better": sum(h > c for _, h, c in rows), "sold_better": [d for d, h, c in rows if c >= h]}
        out[name] = {"n_signals": len(starts), **res}
    put("신호_전부매도_vs_보유", **out)
    put("3편_추가", tr_from_2007_08_03_low=pct(tr.low("2007-08-03", "2009-12-31")[0]),
        burry_1y_low=pct(tr.low("2023-01-31", "2024-01-31")[0]),
        warnings_1y_low={d: pct(tr.low(d, f"{int(d[:4]) + 1}{d[4:]}")[0]) for d in ("2021-01-22", "2022-06-01", "2022-06-03", "2023-01-31", "2023-08-14")})
    # 4편 정씨: 10만 달러 중 8만 최고가 투자 · 2만 남김 → 함정: 3/12 매도 · 바닥에 기다림 · 최고가 근처에서도 기다림 · 2022-02-07 남은 돈 모두 페이팔 · (매달 매수 멈춤)
    e4 = "2024-06-13"
    cash_after = 8 * (1 + tr.chg("2020-02-19", "2020-03-12")) * (1 + cash.chg("2020-03-12", "2022-02-07")) + 2 * (1 + cash.chg("2020-02-19", "2022-02-07"))
    trap4 = cash_after * (1 + S["PYPL"].chg("2022-02-07", e4))
    good4 = 8 * (1 + tr.chg("2020-02-19", e4)) + 2 * (1 + tr.chg("2020-03-23", e4))
    put("정씨_v1.3", invest=8, reserve=2, cash_on_2022_02_07=round(cash_after, 3), trap_2024_06_13=round(trap4, 3), loss=round(10 - trap4, 3),
        hold_index_2024_06_13=round(good4, 3), years=yrs("2020-02-19", e4), sale_frac=round(1 + tr.chg("2020-02-19", "2020-03-12"), 4))
    # 4편 2번: 바닥(3/23)부터 넉 달 나눠 vs 최고가로 돌아온 날(TR 2020-08-10)까지 기다렸다 한꺼번에 → 2022-03-23 값
    s4 = buy(S, "2020-03-23", years=2, months=4)
    put("4편_2_바닥", split4_2y=s4["end_value"], split4_worst=s4["worst"], wait_to_peak_then_lump_2y=round((1 + cash.chg("2020-03-23", "2020-08-10")) * (1 + tr.chg("2020-08-10", "2022-03-23")), 4),
        lump_2008_09_29_worst=-0.3798, split_2008_09_29_worst=-0.1036)
    # 4편 3번: 2020-08-10 부터 12개월 나눠 2년 · 그날보다 10% 아래로 내려간 적
    s3 = buy(S, "2020-08-10", years=2, months=12)
    lo3, ld3 = spx.low("2020-08-10", spx.k[-1])
    put("4편_3_최고가근처", split12_2y=s3["end_value"], split12_worst=s3["worst"], spx_min_after=pct(lo3), spx_min_day=ld3)
    # 4편 5번: 하락장에 들어선 날(최고가 대비 −20% 첫날)부터 매달 1씩 12번 사기를 이어 감 vs 멈추고 현금 → 최고가 회복 날 한꺼번에 · 4년·5년 뒤 (모은 돈 12 대비)
    bears = [("2000-03-24", "닷컴"), ("2007-10-09", "금융위기"), ("2020-02-19", "코로나"), ("2022-01-03", "2022")]
    rows = []
    for pk, name in bears:
        lvl = spx.at(pk)
        d0 = spx.first_below(pk, -0.20)
        back = spx.back(pk, lvl, after=d0)
        i0 = tr.i(d0)
        y, m, dd = int(d0[:4]), int(d0[5:7]), d0[8:]
        sched = [i0] + [bisect.bisect_left(tr.k, f"{y + (m - 1 + k) // 12:04d}-{(m - 1 + k) % 12 + 1:02d}-{dd}") for k in range(1, 12)]
        res = {"bear": name, "entry": d0, "back_to_peak": back}
        for yy in (2, 4, 5):
            e = f"{int(d0[:4]) + yy:04d}{d0[4:]}"
            if e > tr.k[-1]:
                continue
            ie = tr.i(e)
            cont = sum(tr.v[ie] / tr.v[k] * 1.0 for k in sched if k <= ie)        # 이어 감: 12번 산 것의 그날 값
            # 멈춤: 같은 날짜에 넣을 돈을 현금으로 모아 두었다가, 최고가 회복 날(그 전에 끝나면 끝날) 한꺼번에
            pause = 0.0
            for k in sched:
                if k > ie:
                    continue
                kb = tr.i(back) if back and back <= e else ie
                kb = max(kb, k)
                pause += (cash.v[kb] / cash.v[k]) * (tr.v[ie] / tr.v[kb])
            res[f"{yy}년"] = {"continue": round(cont / 12, 4), "pause": round(pause / 12, 4)}
        rows.append(res)
    put("4편_5_하락장_매달", rows=rows)
    # v1.4 김씨: 최고가 날 한꺼번에 → 기술 펀드 → 전기차 → 2배 → 2024-01-03
    seq = [("TR", "2020-02-19", "2021-02-12"), ("ARKK", "2021-02-12", "2021-11-16"), ("LCID", "2021-11-16", "2022-01-03"), ("LEV2", "2022-01-03", "2024-01-03")]
    v = 1.0
    vals = []
    for sym, a_, b_ in seq:
        v *= 1 + S[sym].chg(a_, b_)
        vals.append(round(v, 4))
    put("김씨_v1.4", steps=vals, value_2024_01_03=vals[-1], hold_tr_2024_01_03=round(1 + tr.chg("2020-02-19", "2024-01-03"), 4),
        lump_2020_02_19=buy(S, "2020-02-19"), split_2020_02_19=buy(S, "2020-02-19", months=12),
        lev_now=pct(lev.chg("2022-01-03", lev.k[-1])), tr_now=pct(tr.chg("2022-01-03", tr.k[-1])), lev_back=lev.back("2022-01-03", lev.at("2022-01-03"), after="2022-10-12"),
        lcid_same_tr_low=pct(tr.low("2021-11-16", S["LCID"].k[-1])[0]), lcid_same_tr_now=pct(tr.chg("2021-11-16", tr.k[-1])),
        lev_2001_09_17_low=pct(lev.low("2001-09-17", "2002-12-31")[0]), tr_2001_09_17_low=pct(tr.low("2001-09-17", "2002-12-31")[0]))
    # ---------- v1.5
    irx_s = Ser("13주", rd(CALC / "irx_daily.csv", "close"))
    put("2편_v1.5", irx_2021_12_31=round(irx_s.at("2021-12-31"), 2), tr_low_from_2021_12_31=pct(tr.low("2021-12-31", "2022-12-30")[0]),
        spare_lump_sold_2y=round(0.7871 * (1 + cash.chg("2022-06-13", "2024-01-03")), 4), spare_split_hold_2y=buy(S, "2022-01-03", months=12)["end_value"],
        tr_2021_07_23_now_price=pct(spx.chg("2021-07-23", spx.k[-1])))
    xf = S["XLF"]
    bank_lev = 0.5 * (1 + xf.chg("2007-08-03", "2009-03-09")) + 0.5 * (1 + lev.chg("2007-08-03", "2009-03-09"))
    put("박씨_v1.5", bank_half_lev_half_to_trough=round(bank_lev, 4), xlf_from_signal_low=pct(xf.low("2007-08-03", "2009-12-31")[0]),
        xlf_from_peak_2007_10_09_low=pct(xf.low("2007-10-09", "2009-12-31")[0]), lev_from_2007_10_09_low=pct(lev.low("2007-10-09", "2009-12-31")[0]),
        tr_from_2007_10_09_low=pct(tr.low("2007-10-09", "2009-12-31")[0]), months_signal_to_trough=months("2007-08-03", "2009-03-09"))
    # 200일 평균 사고팔기 규칙: 그날 종가가 200일 평균 위면 다음 날 지수(배당 포함), 아래면 다음 날 현금 (1990-10-16 ~)
    i0 = 200
    hold_v, rule_v, trades, cur = [1.0], [1.0], 0, None
    days = ds[i0:]
    for k in range(i0, len(ds) - 1):
        above = pxv[k] > ma[k]
        if cur is not None and above != cur:
            trades += 1
        cur = above
        a_, b_ = ds[k], ds[k + 1]
        r_tr = tr.at(b_) / tr.at(a_)
        r_c = cash.at(b_) / cash.at(a_)
        hold_v.append(hold_v[-1] * r_tr)
        rule_v.append(rule_v[-1] * (r_tr if above else r_c))
    hv, rv = np.array(hold_v), np.array(rule_v)
    yrs_ = (date.fromisoformat(ds[-1]) - date.fromisoformat(ds[i0])).days / 365.25
    put("200일_규칙", start=ds[i0], end=ds[-1], hold_max_dd=pct(float((hv / np.maximum.accumulate(hv) - 1).min())), rule_max_dd=pct(float((rv / np.maximum.accumulate(rv) - 1).min())),
        hold_cagr=pct(float(hv[-1] ** (1 / yrs_) - 1)), rule_cagr=pct(float(rv[-1] ** (1 / yrs_) - 1)), trades=trades, note="신호는 그날 종가로 보고 다음 날부터 따름(앞날 정보 없음) · 세금·수수료 뺌")
    # 경고 다섯 번 — 2년 보유 vs 현금 · 2년 안 그날 대비 가장 크게 빠진 폭
    W = {}
    for d in ("2021-01-22", "2022-06-01", "2022-06-03", "2023-01-31", "2023-08-14"):
        e2 = f"{int(d[:4]) + 2}{d[4:]}"
        W[d] = {"hold_2y": pct(tr.chg(d, e2)), "cash_2y": pct(cash.chg(d, e2)), "low_2y": pct(tr.low(d, e2)[0])}
    put("경고_2년", **W)
    # 4편: 2008-09-29 넉 달 나눠 vs 기다림(현금 → TR 2007 고점 회복 2012-04-02 까지 = 2년 동안은 현금)
    s08 = buy(S, "2008-09-29", years=2, months=4)
    put("4편_2008_넉달", split4=s08, wait_cash_2y=pct(cash.chg("2008-09-29", "2010-09-29")), lump=buy(S, "2008-09-29"))
    # −60% 날 뒤: 페이팔 · 메타 · 지수(같은 날부터)
    out60 = {}
    for sym, pk in (("PYPL", "2021-07-23"), ("META", "2021-09-07")):
        d60 = S[sym].first_below(pk, -0.6)
        out60[sym] = {"day": d60, "further_low": pct(S[sym].low(d60, S[sym].k[-1])[0]), "now": pct(S[sym].chg(d60, S[sym].k[-1])),
                      "tr_low": pct(tr.low(d60, tr.k[-1])[0]), "tr_now": pct(tr.chg(d60, tr.k[-1]))}
    put("−60%_날_뒤", **out60)
    # 정씨 정답 경로: 8만 보유 + 2만을 3/23부터 넉 달 나눠 → 2024-06-13
    # 2만 달러를 2020-03-23 부터 넉 달(매달 같은 날 또는 다음 거래일)에 나눠 → 2024-06-13 값 (안 넣은 돈은 국채)
    k0 = tr.i("2020-03-23")
    sched = [k0] + [bisect.bisect_left(tr.k, f"2020-{3 + j:02d}-23") for j in range(1, 4)]
    ke = tr.i("2024-06-13")
    c, u = 1.0, 0.0
    for k in range(k0, ke + 1):
        if k in sched:
            u += 0.25 / tr.v[k]
            c -= 0.25
        if k < ke:
            c *= cash.v[k + 1] / cash.v[k]
    def split_to(d0, n, end):
        """d0 부터 n 달에 나눠 넣고(매달 같은 날 또는 다음 거래일, 안 넣은 돈은 국채) end 날 값 (원금 1)."""
        k0_, ke_ = tr.i(d0), tr.i(end)
        y_, m_, dd_ = int(d0[:4]), int(d0[5:7]), d0[8:]
        sc = [k0_] + [bisect.bisect_left(tr.k, f"{y_ + (m_ - 1 + j) // 12:04d}-{(m_ - 1 + j) % 12 + 1:02d}-{dd_}") for j in range(1, n)]
        c_, u_ = 1.0, 0.0
        for k in range(k0_, ke_ + 1):
            if k in sc:
                u_ += (1 / n) / tr.v[k]
                c_ -= 1 / n
            if k < ke_:
                c_ *= cash.v[k + 1] / cash.v[k]
        return round(c_ + u_ * tr.v[ke_], 4)

    put("김씨_정답", split12_2020_02_19_to_2024_01_03=split_to("2020-02-19", 12, "2024-01-03"),
        split12_to_now=split_to("2020-02-19", 12, tr.k[-1]), kim_path_to_now=round(P["김씨_v1.4"]["steps"][2] * (1 + lev.chg("2022-01-03", lev.k[-1])), 4),
        tsla_2021_11_16_low=pct(S["TSLA"].low("2021-11-16", S["TSLA"].k[-1])[0]), tsla_2021_11_16_now=pct(S["TSLA"].chg("2021-11-16", S["TSLA"].k[-1])),
        tsla_prior_1y=pct(S["TSLA"].chg("2020-11-16", "2021-11-16")))
    put("정씨_정답", value_2024_06_13=round(8 * (1 + tr.chg("2020-02-19", "2024-06-13")) + 2 * (c + u * tr.v[ke]), 3), reserve_split4_value=round(c + u * tr.v[ke], 4))
    # 3편 최씨 5번: 2023-10-20 200일 평균 신호 (crash_tests B 목록) — 최고가 대비 · 2년 보유 vs 현금 · 그사이 가장 크게 빠진 폭
    put("3편_최씨_200일", spx_from_peak=pct(spx.peak_before("2023-10-20")[1]), tr_2y=pct(tr.chg("2023-10-20", "2025-10-20")),
        cash_2y=pct(cash.chg("2023-10-20", "2025-10-20")), tr_low_2y=pct(tr.low("2023-10-20", "2025-10-20")[0]),
        months_burry_to_signal=months("2023-01-31", "2023-10-20"))

    # ---------- v1.7 (반론 3회차)
    # 1편 1번·2편 4번: 한꺼번에 vs 12달 나눠 — 2000년 이후 매달 첫 거래일 시작, 2년·5년, 2000~2008 시작 / 2009 이후 시작
    #   원금 20% 넘게 줄어든 적 있는 몫 · 안정(끝에 국채 현금보다 더 + 원금 20% 넘게 안 줄어듦) 몫 · 늘어난 돈 가운데 값
    mstarts = [tr.k[k] for k in range(1, len(tr.k)) if tr.k[k][:7] != tr.k[k - 1][:7] and tr.k[k] >= "2000-01-01"]
    LS = {}
    for yy in (2, 5):
        for era, lo_, hi_ in (("2000~2008", "2000-01-01", "2008-12-31"), ("2009~", "2009-01-01", "2099-12-31")):
            acc = {"lump": [], "split": []}
            for d in mstarts:
                if not (lo_ <= d <= hi_) or f"{int(d[:4]) + yy:04d}{d[4:]}" > tr.k[-1]:
                    continue
                cash_end = 1 + cash.chg(d, f"{int(d[:4]) + yy:04d}{d[4:]}")
                for kind, mm in (("lump", 1), ("split", 12)):
                    b_ = buy(S, d, years=yy, months=mm)
                    acc[kind].append((b_["end_value"], b_["worst"], cash_end))
            LS[f"{yy}년·{era}"] = {kind: {"n": len(v_), "dd20_share": pct(float(np.mean([w < -0.2 for _, w, _ in v_]))),
                                          "stable_share": pct(float(np.mean([(e_ > c_) and (w >= -0.2) for e_, w, c_ in v_]))),
                                          "median_gain": pct(float(np.median([e_ - 1 for e_, _, _ in v_])))} for kind, v_ in acc.items()}
    put("한꺼번에_vs_나눠_2000_이후", rule="매달 첫 거래일 시작 · 나눠 = 12달(안 넣은 돈은 국채) · 원금 20% = 시작 날 원금 대비", **LS)
    # 2편 5번: −20% 매도 vs 보유 124번 — 매도한 쪽이 원금 아래로 끝난 수 · 보유한 쪽이 원금을 되찾은 수 · 매도 뒤 보유한 쪽의 가장 낮은 값
    mk = [k for k in range(1, len(tr.k)) if tr.k[k][:7] != tr.k[k - 1][:7] and tr.k[k] >= "1990-01-01"]   # 매도20_vs_보유_5년 과 같은 시작 (위 starts 는 v1.3 에서 신호 날짜로 바뀜)
    rows20 = []
    for k0 in mk:
        e5d = f"{int(tr.k[k0][:4]) + 5:04d}{tr.k[k0][4:]}"
        if tr.k[-1] < e5d:
            break
        e5 = tr.i(e5d)
        seg = tr.v[k0:e5 + 1] / tr.v[k0]
        hit = np.nonzero(seg < 0.8)[0]
        if not len(hit):
            continue
        ks = k0 + int(hit[0])
        rows20.append({"hold": float(seg[-1]), "sold": float(seg[hit[0]] * cash.v[e5] / cash.v[ks]), "hold_min_after": float(seg[hit[0]:].min())})
    put("매도20_v1.7", n=len(rows20), sold_below_principal=sum(r["sold"] < 1 for r in rows20), hold_back_to_principal=sum(r["hold"] >= 1 for r in rows20),
        hold_min_after_median=round(float(np.median([r["hold_min_after"] for r in rows20])), 3),
        hold_min_below_70=pct(float(np.mean([r["hold_min_after"] < 0.7 for r in rows20]))), hold_end_below_principal=sum(r["hold"] < 1 for r in rows20))
    # 3편: 200일 신호 날부터 바닥까지 — 배당 포함(TR) · 2년 안 TR 이 20% 넘게 빠진 신호
    bear_sig = {"닷컴": ("1999-09-23", "2002-10-09"), "금융위기": ("2007-08-03", "2009-03-09"), "코로나": ("2020-02-27", "2020-03-23"), "2022": ("2022-01-21", "2022-10-12")}
    on = pxv < ma
    st200, last = [], -10 ** 9
    for i_, x in enumerate(on):
        if x and not np.isnan(ma[i_]):
            if i_ - last > 60:
                st200.append(ds[i_])
            last = i_
    put("3편_v1.7", signal_to_trough_tr={k: pct(tr.low(a_, b_)[0]) for k, (a_, b_) in bear_sig.items()},
        signal_to_trough_price={k: pct(spx.low(a_, b_)[0]) for k, (a_, b_) in bear_sig.items()},
        tr_dd20_within_2y=[d for d in st200 if f"{int(d[:4]) + 2:04d}{d[4:]}" <= tr.k[-1] and tr.low(d, f"{int(d[:4]) + 2:04d}{d[4:]}")[0] < -0.2],
        n_signals=len(st200), lev2_vs_tr_drawdown_ratio={k: round(lev.low(a_, b_)[0] / tr.low(a_, b_)[0], 2) for k, (a_, b_) in
                                                        {"2001-09": ("2001-09-17", "2002-12-31"), "2007-10": ("2007-10-09", "2009-12-31"), "2022": ("2022-01-03", "2022-12-30"),
                                                         "2018-09-20 2년": ("2018-09-20", "2020-09-20")}.items()},
        sectors_source="purpose_numbers_2026-10-31.json A_sectors (1999-01-04~): S&P 500 −55.3% · 그보다 깊은 업종 6개(소재·에너지·금융·산업재·기술·임의소비재) · 되찾기 금융 10.1년·기술 16.9년 · S&P 500 4.5년")
    # 4편 정씨 정답 경로 + 4번 정답(페이팔을 계좌의 10%만큼) — 2022-02-07 에 계좌 10% 를 페이팔로 → 2024-06-13
    v0207 = 8 * (1 + tr.chg("2020-02-19", "2022-02-07")) + 2 * split_to("2020-03-23", 4, "2022-02-07")
    put("정씨_정답_v1.7", account_2022_02_07=round(v0207, 3),
        with_pypl10_2024_06_13=round(v0207 * (0.9 * (1 + tr.chg("2022-02-07", "2024-06-13")) + 0.1 * (1 + S["PYPL"].chg("2022-02-07", "2024-06-13"))), 3),
        without_pypl_2024_06_13=round(v0207 * (1 + tr.chg("2022-02-07", "2024-06-13")), 3),
        wait_10pct_2008_10_08_lump=buy(S, "2008-10-08"))

    # ---------- v1.8 (반론 4회차 — 3편)
    # 200일 평균을 1988년 자료부터 냄 (v1.3 의 ds·ma 는 1990-01-02 부터라 1990-10-15 가 가짜 첫 신호였음) · 신호·2년 결과·200일 규칙 다시
    pxa = spx.v
    ma_full = np.array([np.nan] * 199 + [float(pxa[i - 199:i + 1].mean()) for i in range(199, len(pxa))])
    i90 = spx.i("1990-01-02")
    if spx.k[i90] < "1990-01-02":
        i90 += 1
    on_f = pxa < ma_full
    # 꺼짐·켜짐을 1988년부터 이어서 세고, 1990-01-02 이후에 처음 켜진 날만 셈 (60거래일 넘게 꺼졌다가 켜진 날)
    sig_f, last = [], -10 ** 9
    for i_ in range(199, len(pxa)):
        if on_f[i_]:
            if i_ - last > 60 and i_ >= i90:
                sig_f.append(spx.k[i_])
            last = i_
    rows2 = []
    for d in sig_f:
        e2 = f"{int(d[:4]) + 2:04d}{d[4:]}"
        if e2 > tr.k[-1]:
            continue
        rows2.append({"day": d, "tr_low_2y": tr.low(d, e2)[0], "hold_2y": 1 + tr.chg(d, e2), "cash_2y": 1 + cash.chg(d, e2)})
    # 200일 규칙 (평균은 1988년부터) — 1990-01-02 부터: 그날 종가가 평균 위면 다음 날 지수(배당 포함), 아래면 현금
    hv_, rv_, tr_n, cur = [1.0], [1.0], 0, None
    for k in range(i90, len(pxa) - 1):
        above = pxa[k] > ma_full[k]
        if cur is not None and above != cur:
            tr_n += 1
        cur = above
        a_, b_ = spx.k[k], spx.k[k + 1]
        hv_.append(hv_[-1] * tr.at(b_) / tr.at(a_))
        rv_.append(rv_[-1] * (tr.at(b_) / tr.at(a_) if above else cash.at(b_) / cash.at(a_)))
    hv_, rv_ = np.array(hv_), np.array(rv_)
    yy_ = (date.fromisoformat(spx.k[-1]) - date.fromisoformat(spx.k[i90])).days / 365.25
    # 박씨 묶음(금융 반 · 2배 반, 2007-08-03) — 원금 되찾은 날 · 지수(배당 포함) 같은 날부터 원금 되찾은 날 · 지금
    xf = S["XLF"]
    common = [d for d in xf.k if d >= "2007-08-03" and d <= lev.k[-1]]
    bundle = np.array([0.5 * xf.at(d) / xf.at("2007-08-03") + 0.5 * lev.at(d) / lev.at("2007-08-03") for d in common])
    b_back = next((common[i_] for i_ in range(len(common)) if common[i_] > "2009-03-09" and bundle[i_] >= 1), None)
    put("3편_v1.8", ma_from="1988-01-04", signals_from="1990-01-02", n_signals=len(sig_f), first_signals=sig_f[:3], n_with_2y=len(rows2),
        no_dd20_2y=sum(r["tr_low_2y"] >= -0.2 for r in rows2), dd20_2y=[r["day"] for r in rows2 if r["tr_low_2y"] < -0.2],
        hold_better_2y=sum(r["hold_2y"] > r["cash_2y"] for r in rows2), sold_better_2y=[r["day"] for r in rows2 if r["cash_2y"] >= r["hold_2y"]],
        rule_from=spx.k[i90], rule_max_dd=pct(float((rv_ / np.maximum.accumulate(rv_) - 1).min())), hold_max_dd=pct(float((hv_ / np.maximum.accumulate(hv_) - 1).min())),
        rule_trades=tr_n, rule_end=round(float(rv_[-1]), 2), hold_end=round(float(hv_[-1]), 2), rule_over_hold=round(float(rv_[-1] / hv_[-1]), 3),
        rule_cagr=pct(float(rv_[-1] ** (1 / yy_) - 1)), hold_cagr=pct(float(hv_[-1] ** (1 / yy_) - 1)), cash_end=round(cash.at(spx.k[-1]) / cash.at(spx.k[i90]), 2),
        bundle_trough=round(float(bundle.min()), 4), bundle_back_to_principal=b_back, bundle_years_to_back=yrs("2007-08-03", b_back) if b_back else None,
        tr_back_to_0803=tr.back("2007-08-03", tr.at("2007-08-03"), after="2009-03-09"), tr_years_to_back=yrs("2007-08-03", tr.back("2007-08-03", tr.at("2007-08-03"), after="2009-03-09")),
        bundle_now=round(float(bundle[-1]), 2), tr_now_from_0803=round(1 + tr.chg("2007-08-03", tr.k[-1]), 2), bundle_now_day=common[-1],
        sector_recover_note="purpose_numbers A_sectors: years_to_recover = 그 하락의 고점 → 고점 회복 (바닥부터가 아님)")

    # ---------- v1.8 (반론 4회차 — 2편·1편)
    # 한꺼번에 vs 12달 나눠 — 1990~1999 시작 · 1990 이후 전체 (v1.7 은 2000 이후만)
    m90 = [tr.k[k] for k in range(1, len(tr.k)) if tr.k[k][:7] != tr.k[k - 1][:7] and tr.k[k] >= "1990-01-01"]
    LS90 = {}
    for yy in (2, 5):
        for era, lo_, hi_ in (("1990~1999", "1990-01-01", "1999-12-31"), ("1990~", "1990-01-01", "2099-12-31")):
            acc = {"lump": [], "split": []}
            for d in m90:
                if not (lo_ <= d <= hi_) or f"{int(d[:4]) + yy:04d}{d[4:]}" > tr.k[-1]:
                    continue
                cash_end = 1 + cash.chg(d, f"{int(d[:4]) + yy:04d}{d[4:]}")
                for kind, mm in (("lump", 1), ("split", 12)):
                    b_ = buy(S, d, years=yy, months=mm)
                    acc[kind].append((b_["end_value"], b_["worst"], cash_end))
            LS90[f"{yy}년·{era}"] = {kind: {"n": len(v_), "stable_n": int(sum((e_ > c_) and (w >= -0.2) for e_, w, c_ in v_)),
                                            "stable_share": pct(float(np.mean([(e_ > c_) and (w >= -0.2) for e_, w, c_ in v_]))),
                                            "dd20_n": int(sum(w < -0.2 for _, w, _ in v_))} for kind, v_ in acc.items()}
    put("한꺼번에_vs_나눠_1990", **LS90)
    # 지수 1년 보유 손실 몫 — 매달 첫 거래일 시작 (배당 포함)
    one = {}
    for era, lo_ in (("1990~", "1990-01-01"), ("2000~", "2000-01-01")):
        v1 = [tr.chg(d, f"{int(d[:4]) + 1:04d}{d[4:]}") for d in m90 if d >= lo_ and f"{int(d[:4]) + 1:04d}{d[4:]}" <= tr.k[-1]]
        one[era] = {"n": len(v1), "loss_share": pct(float(np.mean([x < 0 for x in v1])))}
    put("1년_보유_손실", **one)
    # −20% 매도 124번 — 하락장별 (매도 날로 나눔): 수 · 보유해도 5년 뒤 원금 아래 · 보유 − 매도 가운데 값
    by = {}
    for k0 in mk:
        e5d = f"{int(tr.k[k0][:4]) + 5:04d}{tr.k[k0][4:]}"
        if tr.k[-1] < e5d:
            break
        e5 = tr.i(e5d)
        seg = tr.v[k0:e5 + 1] / tr.v[k0]
        hit = np.nonzero(seg < 0.8)[0]
        if not len(hit):
            continue
        ks = k0 + int(hit[0])
        dsell = tr.k[ks]
        bear = "닷컴" if dsell < "2005-01-01" else ("금융위기" if dsell < "2015-01-01" else "코로나")
        hold, sold = float(seg[-1]), float(seg[hit[0]] * cash.v[e5] / cash.v[ks])
        by.setdefault(bear, []).append((hold, sold))
    put("매도20_하락장별", **{b: {"n": len(v_), "hold_below_principal": int(sum(h < 1 for h, _ in v_)), "hold_minus_sold_median": round(float(np.median([h - s_ for h, s_ in v_])), 2)}
                              for b, v_ in by.items()})

    # ---------- v1.8 (반론 4회차 — 4편·1편)
    # 4편 5번: 하락장에 들어선 날부터 매달 1씩 12번 — 이어 감(가는 길 가장 낮은 값 = 그때까지 넣은 돈 대비) vs 멈추고 예금(매달 넣을 돈을 예금에만)
    rows5 = []
    for pk, name in bears:
        d0 = spx.first_below(pk, -0.20)
        i0 = tr.i(d0)
        y, m, dd = int(d0[:4]), int(d0[5:7]), d0[8:]
        sched = [i0] + [bisect.bisect_left(tr.k, f"{y + (m - 1 + k) // 12:04d}-{(m - 1 + k) % 12 + 1:02d}-{dd}") for k in range(1, 12)]
        res = {"bear": name, "entry": d0}
        for yy in (2, 4):
            e = f"{int(d0[:4]) + yy:04d}{d0[4:]}"
            if e > tr.k[-1]:
                continue
            ie = tr.i(e)
            units, put_in, worst = 0.0, 0.0, 0.0
            for k in range(i0, ie + 1):
                if k in sched:
                    units += 1 / tr.v[k]
                    put_in += 1
                worst = min(worst, units * tr.v[k] / put_in - 1)
            dep = sum(cash.v[ie] / cash.v[k] for k in sched if k <= ie)
            n_in = sum(1 for k in sched if k <= ie)
            res[f"{yy}년"] = {"continue": round(units * tr.v[ie] / n_in, 4), "continue_worst": pct(worst), "deposit_only": round(dep / n_in, 4)}
        rows5.append(res)
    put("4편_5_이어감_vs_예금", rows=rows5)
    # 4편 3번: 최고가 근처(배당 포함 지수가 그때까지 최고가의 98% 이상)인 달 첫 거래일에 시작 — A 1년 12번 나눠 vs B 그날보다 10% 싸지면(첫날) 그때부터 1년 12번 나눠 (그 전엔 국채 현금)
    def split_path(d_start, trig, e_):
        """d_start 부터 e_ 까지 — trig 날(없으면 끝까지 현금)부터 12달 나눠 매수 · 끝 값과 가장 낮은 값 (원금 1)."""
        ks, ke_ = tr.i(d_start), tr.i(e_)
        sc = set()
        if trig is not None:
            kt = tr.i(trig)
            y_, m_, dd_ = int(tr.k[kt][:4]), int(tr.k[kt][5:7]), tr.k[kt][8:]
            sc = {kt} | {bisect.bisect_left(tr.k, f"{y_ + (m_ - 1 + j) // 12:04d}-{(m_ - 1 + j) % 12 + 1:02d}-{dd_}") for j in range(1, 12)}
        c_, u_, left, worst_ = 1.0, 0.0, 12, 1.0
        for k in range(ks, ke_ + 1):
            if k in sc and left > 0:
                amt = c_ / left
                u_ += amt / tr.v[k]
                c_ -= amt
                left -= 1
            worst_ = min(worst_, c_ + u_ * tr.v[k])
            if k < ke_:
                c_ *= cash.v[k + 1] / cash.v[k]
        return c_ + u_ * tr.v[ke_], worst_ - 1
    runmax = np.maximum.accumulate(tr.v)
    NH = {}
    for yy in (2, 5):
        for era, lo_, hi_ in (("1990~1999", "1990-01-01", "1999-12-31"), ("2000~2008", "2000-01-01", "2008-12-31"), ("2009~", "2009-01-01", "2099-12-31"), ("1990~", "1990-01-01", "2099-12-31")):
            a_st, b_st, n_ = 0, 0, 0
            for d in m90:
                e_ = f"{int(d[:4]) + yy:04d}{d[4:]}"
                if not (lo_ <= d <= hi_) or e_ > tr.k[-1] or tr.v[tr.i(d)] < 0.98 * runmax[tr.i(d)]:
                    continue
                ce = 1 + cash.chg(d, e_)
                ea, wa = split_path(d, d, e_)
                trig = tr.first_below(d, -0.10)
                eb, wb = split_path(d, trig if trig and trig <= e_ else None, e_)
                n_ += 1
                a_st += (ea > ce) and (wa >= -0.2)
                b_st += (eb > ce) and (wb >= -0.2)
            NH[f"{yy}년·{era}"] = {"n": n_, "split_now_stable": pct(a_st / n_) if n_ else None, "wait10_then_split_stable": pct(b_st / n_) if n_ else None}
    put("4편_3_최고가근처_기다렸다나눠", rule="시작 = 배당 포함 지수가 그때까지 최고가의 98% 이상인 달 첫 거래일 · B = 그날보다 10% 아래로 처음 내려간 날부터 12달 나눠(그 전·안 넣은 돈은 국채)", **NH)
    # 4편 2번: 2008-10-08(9/29 보다 10% 아래 첫날) 한꺼번에 → 2010-09-29 (넉 달 나눠와 같은 끝 날)
    put("4편_2_10%기다림_같은끝", lump_2008_10_08_to_2010_09_29=round(1 + tr.chg("2008-10-08", "2010-09-29"), 4))
    # 1편 5번: 2024-01-03 지수 매수 → 2026-10-27 · 2000년 이후 매달 시작 5년 보유가 국채 현금보다 더 남긴 몫 · '지금' = 2026-10-27 종가로 맞춤
    NOW = "2026-10-27"
    m5 = [d for d in mstarts if f"{int(d[:4]) + 5:04d}{d[4:]}" <= tr.k[-1]]
    put("1편_5번_지수_보유", tr_2024_01_03_to_now=pct(tr.chg("2024-01-03", NOW)), tr_low=pct(tr.low("2024-01-03", NOW)[0]), cash=pct(cash.chg("2024-01-03", NOW)),
        five_year_beat_cash_2000=pct(float(np.mean([tr.chg(d, f"{int(d[:4]) + 5:04d}{d[4:]}") > cash.chg(d, f"{int(d[:4]) + 5:04d}{d[4:]}") for d in m5]))), n=len(m5),
        now=NOW, arkk_2021_02_12_now=pct(S["ARKK"].chg("2021-02-12", NOW)), tsla_2021_11_16_now=pct(S["TSLA"].chg("2021-11-16", NOW)),
        lcid_2021_11_16_now=pct(S["LCID"].chg("2021-11-16", NOW)), pypl_2021_07_23_now=pct(S["PYPL"].chg("2021-07-23", NOW)), pypl_2022_02_07_now=pct(S["PYPL"].chg("2022-02-07", NOW)),
        kim_correct_path_2022_peak_dd=pct(float(min(0.0, tr.low("2022-01-03", "2022-12-30")[0]))))

    # ---------- v1.9 (반론 5회차 — 3편)
    # 200일 규칙(3편_v1.8 과 같은 규칙): 판 횟수·산 횟수 · 판 값이 산 값(배당 포함 지수)보다 낮았던 수
    sells, buys_, below, buy_px, cur = 0, 0, 0, None, None
    for k in range(i90, len(pxa) - 1):
        above = bool(pxa[k] > ma_full[k])
        nxt = spx.k[k + 1]
        if cur is None:
            if above:
                buy_px = tr.at(nxt)
        elif above != cur:
            if above:
                buys_ += 1
                buy_px = tr.at(nxt)
            else:
                sells += 1
                below += tr.at(nxt) < buy_px
        cur = above
    # 버리 'Sell' 글은 2023-01-31 장 마감 뒤 — 팔 수 있는 첫 종가 2023-02-01 기준 2년
    put("3편_v1.9", rule_sells=sells, rule_buys=buys_, rule_sells_below_buy=int(below), rule_end_over_cash=round(float(rv_[-1]) / (cash.at(spx.k[-1]) / cash.at(spx.k[i90])), 1),
        cash_from_2007_08_03_now=round(1 + cash.chg("2007-08-03", NOW), 2),
        burry_from_2023_02_01={"hold_2y": pct(tr.chg("2023-02-01", "2025-02-01")), "cash_2y": pct(cash.chg("2023-02-01", "2025-02-01")), "low_2y": pct(tr.low("2023-02-01", "2025-02-01")[0])},
        note="판·산 값 = 신호 다음 날 종가 (배당 포함)")
    # 200일 규칙 — 앞날 정보 없이: k 날 종가로 신호를 보고 k+1 날 종가에 사고팖 (v1.8 은 k 날 종가에 바로 따름 = 같은 종가 체결)
    hv2, rv2 = [1.0], [1.0]
    for k in range(i90, len(pxa) - 2):
        above = pxa[k] > ma_full[k]
        r_tr = tr.at(spx.k[k + 2]) / tr.at(spx.k[k + 1])
        r_c = cash.at(spx.k[k + 2]) / cash.at(spx.k[k + 1])
        hv2.append(hv2[-1] * r_tr)
        rv2.append(rv2[-1] * (r_tr if above else r_c))
    hv2, rv2 = np.array(hv2), np.array(rv2)
    put("200일_규칙_다음날", start=spx.k[i90 + 1], end=spx.k[-1], rule_max_dd=pct(float((rv2 / np.maximum.accumulate(rv2) - 1).min())),
        hold_max_dd=pct(float((hv2 / np.maximum.accumulate(hv2) - 1).min())), rule_end=round(float(rv2[-1]), 2), hold_end=round(float(hv2[-1]), 2),
        rule_over_hold=round(float(rv2[-1] / hv2[-1]), 3), rule_over_cash=round(float(rv2[-1]) / (cash.at(spx.k[-1]) / cash.at(spx.k[i90 + 1])), 1), trades=sells + buys_)

    # ---------- v1.9 (반론 5회차 — 2편)
    # 여윳돈 5만(2022-01-03) — '지금'(2026-10-27) 값: 매도(2022-06-13 한꺼번에 0.7871 → 국채) · 한꺼번에 보유 · 12달 나눠 보유 · 예금만
    put("2편_여윳돈_지금", now=NOW, sold=round(0.7871 * (1 + cash.chg("2022-06-13", NOW)), 4), lump_hold=round(1 + tr.chg("2022-01-03", NOW), 4),
        split_hold=split_to("2022-01-03", 12, NOW), deposit=round(1 + cash.chg("2022-01-03", NOW), 4))
    # −20% 매도 124번 — 분모(5년이 찬 1990년 이후 매달 시작) · 보유가 같은 5년 예금보다 더 남긴 수 · 매도가 예금보다 더 남긴 수
    n_all, hold_beat, sold_beat = 0, 0, 0
    for k0 in mk:
        e5d = f"{int(tr.k[k0][:4]) + 5:04d}{tr.k[k0][4:]}"
        if tr.k[-1] < e5d:
            break
        n_all += 1
        e5 = tr.i(e5d)
        seg = tr.v[k0:e5 + 1] / tr.v[k0]
        hit = np.nonzero(seg < 0.8)[0]
        if not len(hit):
            continue
        ks = k0 + int(hit[0])
        dep = cash.v[e5] / cash.v[k0]
        hold_beat += seg[-1] > dep
        sold_beat += seg[hit[0]] * cash.v[e5] / cash.v[ks] > dep
    put("매도20_v1.9", n_starts=n_all, hold_beat_deposit=int(hold_beat), sold_beat_deposit=int(sold_beat))
    # 2편 1번: 계좌 10만(2021-07-23 페이팔 7만 · 지수 3만) — A 그대로 vs B 페이팔 1만만 남기고 6만을 지수로(옮길 때 이익의 22% 세금을 낸다고 해도) → 지금
    pyg = 0.78 / 1.78        # 1년 만에 78% 오른 주식을 팔 때 판 돈 가운데 이익 몫 (1년 전에 샀다고 봄)
    tax = 6 * pyg * 0.22
    a_now = 7 * (1 + S["PYPL"].chg("2021-07-23", NOW)) + 3 * (1 + tr.chg("2021-07-23", NOW))
    b_now = 1 * (1 + S["PYPL"].chg("2021-07-23", NOW)) + 9 * (1 + tr.chg("2021-07-23", NOW))
    b_now_tax = 1 * (1 + S["PYPL"].chg("2021-07-23", NOW)) + (9 - tax) * (1 + tr.chg("2021-07-23", NOW))
    put("2편_1번_지금", now=NOW, a_now=round(a_now, 2), b_now=round(b_now, 2), tax_if_22pct=round(tax, 2), b_now_after_tax=round(b_now_tax, 2),
        note="세금 = 판 6만 달러 가운데 이익 몫(0.78/1.78) × 22% — 어림, 한국 해외 주식 양도세 기본 공제는 뺌")

    # ---------- v1.9 (반론 5회차 — 4편: 정답 기준 = 안정 먼저(예금보다 더 + 그날보다 20% 넘게 안 줄어듦), 같으면 더 남긴 쪽)
    # 1번: 2020-03-12 그날 기준 보유의 가장 낮은 값 · 2년 · 공포 지수 40 첫날(crash_tests C_vix40 날짜) 보유의 안정 수
    vix_days = [c["date"] for c in json.loads((HERE / "crash_tests_2026-10-31.json").read_text(encoding="utf-8"))["C_vix40"]["cases"]]
    vrows = []
    for d in vix_days:
        e2 = f"{int(d[:4]) + 2:04d}{d[4:]}"
        if e2 > tr.k[-1]:
            continue
        lo_, _ = tr.low(d, e2)
        vrows.append({"day": d, "hold_stable": bool((tr.chg(d, e2) > cash.chg(d, e2)) and lo_ >= -0.2), "hold_beat_cash": bool(tr.chg(d, e2) > cash.chg(d, e2)), "low": pct(lo_)})
    # 4번: 2022-02-07 계좌 = 지수 90% + 페이팔 10% (그대로 둠) — 그날 기준 가장 낮은 값 · 2024-06-13 · 지금
    pv = lambda d: 0.9 * tr.at(d) / tr.at("2022-02-07") + 0.1 * S["PYPL"].at(d) / S["PYPL"].at("2022-02-07")
    pdays = [d for d in tr.k if "2022-02-07" <= d <= NOW]
    pvals = np.array([pv(d) for d in pdays])
    put("4편_v1.9", day1_hold_low_from_2020_03_12=pct(tr.low("2020-03-12", "2022-03-12")[0]), day1_hold_2y=pct(tr.chg("2020-03-12", "2022-03-12")),
        vix40=vrows, vix40_n=len(vrows), vix40_hold_stable=sum(r["hold_stable"] for r in vrows), vix40_hold_beat_cash=sum(r["hold_beat_cash"] for r in vrows),
        pypl10_low=pct(float(pvals.min() - 1)), pypl10_low_day=pdays[int(np.argmin(pvals))], pypl10_2024_06_13=pct(pv("2024-06-13") - 1), pypl10_now=pct(pv(NOW) - 1),
        trap_loss_split={"sale": round(8 - 8 * 0.7336, 3), "pypl": round(P["정씨_v1.3"]["cash_on_2022_02_07"] - P["정씨_v1.3"]["trap_2024_06_13"], 3)},
        pause_until_peak_2022_2y=P["4편_5_하락장_매달"]["rows"][3]["2년"]["pause"],
        note="vix_days = crash_tests_2026-10-31.json C_vix40 cases 의 날짜 (공포 지수 40 을 석 달 넘게 안 넘다가 처음 넘은 날)")
    return P


def nasdaq_1(S):
    """v2.0 — 1편 김씨를 나스닥 100(QQQ 수정 종가 = 배당 포함)으로 (사용자 지시 2026-11-01 "S&P500 말고 나스닥 지수로 해 그래야 상황을 더 극한으로").
    선택: ① 2020-02-19 나스닥 최고가 — 한꺼번에 vs 12달 나눠 ② 2021-02-12 ARKK(1년 2.7배) ③ 2021-12-27 나스닥 최고가 — 1배 vs 2배(QLD 실제 ETF)
    ④ 2024-03-13 SMCI(AI 서버 — 1년 13배) ⑤ 2025-01-02 단타. 금액 = 1억 원에 달러 기준 변화율을 곱함(환율 변화는 뺌 — 설명란에 밝힘)."""
    q, cash, irx = S["QQQ"], S["CASH"], Ser("13주", rd(CALC / "irx_daily.csv", "close"))
    NOW = "2026-10-27"
    R = {}

    def put(key, **kw):
        R[key] = kw
        log.info("key=%s %s", key, json.dumps(kw, ensure_ascii=False)[:600], extra={"stage": "NASDAQ1"})

    def split_ser(ser, d0, n, end):
        """d0 부터 n 달에 나눠 매수(매달 같은 날 또는 다음 거래일 · 안 넣은 돈은 국채) → end 값 · 그사이 가장 낮은 값 (원금 1)."""
        k0, ke = ser.i(d0), ser.i(end)
        y_, m_, dd_ = int(d0[:4]), int(d0[5:7]), d0[8:]
        sc = {k0} | {bisect.bisect_left(ser.k, f"{y_ + (m_ - 1 + j) // 12:04d}-{(m_ - 1 + j) % 12 + 1:02d}-{dd_}") for j in range(1, n)}
        c, u, worst, wday = 1.0, 0.0, 1.0, ser.k[k0]
        for k in range(k0, ke + 1):
            if k in sc:
                u += (1 / n) / ser.v[k]
                c -= 1 / n
            val = c + u * ser.v[k]
            if val < worst:
                worst, wday = val, ser.k[k]
            if k < ke:
                c *= cash.at(ser.k[k + 1]) / cash.at(ser.k[k])
        return {"end": round(c + u * ser.v[ke], 4), "worst": pct(worst - 1), "worst_day": wday}

    d1, d2, d3, d4, d5 = "2020-02-19", "2021-02-12", "2021-12-27", "2024-03-13", "2025-01-02"
    put("날짜", d1=d1, d1_is_peak=q.peak_before(d1)[0] == d1, d3=d3, d3_is_peak=q.peak_before(d3)[0] == d3, d4_smci_peak=S["SMCI"].peak_before("2024-12-31")[0], d5=d5)
    # ① 한꺼번에 vs 12달 나눠
    lo1, lo1d = q.low(d1, "2020-12-31")
    put("1_한꺼번에_vs_나눠", lump_worst=pct(lo1), lump_worst_day=lo1d, lump_back_to_start=q.back(d1, q.at(d1), after=lo1d), months_to_back=months(d1, q.back(d1, q.at(d1), after=lo1d)),
        split12=split_ser(q, d1, 12, "2021-02-19"), split_first_tranche_share=round(1 / 12, 4), lump_1y=round(1 + q.chg(d1, "2021-02-19"), 4),
        qqq_prior_1y=pct(q.chg("2019-02-19", d1)), note="나눠 넣기 가장 낮은 값 = 그때까지 넣은 돈 + 아직 안 넣은 국채 현금 전체 대비")
    # ② ARKK
    A = S["ARKK"]
    put("2_ARKK", prior_1y=round(1 + A.chg("2020-02-12", d2), 2), low=pct(A.low(d2, NOW)[0]), low_day=A.low(d2, NOW)[1], now=pct(A.chg(d2, NOW)),
        qqq_low=pct(q.low(d2, NOW)[0]), qqq_now=pct(q.chg(d2, NOW)))
    # ③ 1배 vs 2배 — QLD 실제 ETF (2021-12-27 ~) · 2000년 나스닥 2배는 재현(QQQ 하루 수익 × 2 − (13주 금리 + 0.95%)/252)
    Q2 = S["QLD"]
    rq = np.concatenate([[0.0], q.v[1:] / q.v[:-1] - 1])
    rate = np.array([irx.at(d) for d in q.k])
    syn2 = Ser("나스닥 2배(재현)", dict(zip(q.k, np.cumprod(1 + 2 * rq - (rate / 100 + 0.0095) / 252))))
    put("3_1배_vs_2배", qld_prior_1y=pct(Q2.chg("2020-12-27", d3)), qqq_prior_1y=pct(q.chg("2020-12-27", d3)),
        qld_2022_low=pct(Q2.low(d3, "2022-12-31")[0]), qqq_2022_low=pct(q.low(d3, "2022-12-31")[0]),
        qld_now=pct(Q2.chg(d3, NOW)), qqq_now=pct(q.chg(d3, NOW)), qld_back=Q2.back(d3, Q2.at(d3), after="2022-12-28"), qqq_back=q.back(d3, q.at(d3), after="2022-12-28"),
        syn2_2000_low=pct(syn2.low("2000-03-27", "2003-12-31")[0]), qqq_2000_low=pct(q.low("2000-03-27", "2003-12-31")[0]),
        syn2_2000_back=syn2.back("2000-03-27", syn2.at("2000-03-27"), after="2002-10-07"), qqq_2000_back=q.back("2000-03-27", q.at("2000-03-27"), after="2002-10-07"))
    # ④ SMCI (AI 서버) · 같은 날 나스닥 · 엔비디아
    M, N = S["SMCI"], S["NVDA"]
    put("4_SMCI", prior_1y=round(1 + M.chg("2023-03-13", d4), 1), low=pct(M.low(d4, NOW)[0]), low_day=M.low(d4, NOW)[1], now=pct(M.chg(d4, NOW)),
        qqq_low=pct(q.low(d4, NOW)[0]), qqq_now=pct(q.chg(d4, NOW)), nvda_now=pct(N.chg(d4, NOW)), nvda_low=pct(N.low(d4, NOW)[0]))
    # 김씨 경로 (함정만) · 정답 경로
    seq = [(q, d1, d2), (A, d2, d3), (Q2, d3, d4), (M, d4, d5)]
    v, steps, mx, mxd = 1.0, [], 1.0, d1
    for ser, a_, b_ in seq:
        for d in ser.k:
            if a_ <= d <= b_:
                x = v * ser.at(d) / ser.at(a_)
                if x > mx:
                    mx, mxd = x, d
        v *= 1 + ser.chg(a_, b_)
        steps.append(round(v, 4))
    good = split_ser(q, d1, 12, d5)
    put("김씨_경로", steps=steps, at_d5=steps[-1], peak=round(mx, 4), peak_day=mxd, years=yrs(d1, d5), kim_to_now_if_held_smci=round(steps[2] * (1 + M.chg(d4, NOW)), 4),
        correct_at_d5=good["end"], correct_worst=good["worst"], correct_now=split_ser(q, d1, 12, NOW)["end"], won="1억 원 × 값", d5_qqq_now=pct(q.chg(d5, NOW)), d5_qqq_low=pct(q.low(d5, NOW)[0]))
    return R


def nasdaq_1_v21(S):
    """v2.1 — 1편을 사용자가 준 다섯 습관으로 (사용자 지시 2026-11-01 "1편을 아래 5가지로 항목 만들어서 재구성하고 …
    -남들이 좋다고 한 종목을 따라 산다 -최악의 상황에 대비하여 현금을 남겨놓지 않는다 -상황에 따른 매수, 매도 기준이 없다
    -자신의 실수를 인정하지 않고 손절하지 않는다 -여러 종목, 섹터 등 분배하지 않는다").
    ① 2021-02-12 ARKK(동료·친구가 산 1년 2.7배 ETF) vs 나스닥 ② 같은 날 1억 전부 vs 2천만 현금 남김 ③ 2022-06-13 나스닥 −30% — 그때그때(김씨: 06-16 매도 → 최고가 회복 2023-12-13 재매수) vs 기준대로 보유
    ④ 2024-08-28 SMCI(2024-03-13 지인 추천 매수 · 회계 문제 보고서·연간 보고서 지연) 버팀 vs 손절하고 나스닥 ⑤ 2024-11-20 MSTR(비트코인 사 모으는 회사, 1년 9.3배) 전부 vs 지수.
    금액 = 1억 원 × 달러 기준 변화율 (환율 뺌)."""
    q, A, cash = S["QQQ"], S["ARKK"], S["CASH"]
    M, B = S["SMCI"], S["MSTR"]
    NOW = "2026-10-27"
    d1, d3, dSell, dBack, dS, d4, d5 = "2021-02-12", "2022-06-13", "2022-06-16", "2023-12-13", "2024-03-13", "2024-08-28", "2024-11-20"
    R = {}

    def put(key, **kw):
        R[key] = kw
        log.info("key=%s %s", key, json.dumps(kw, ensure_ascii=False)[:600], extra={"stage": "NASDAQ1v21"})

    put("1_남따라", arkk_prior_1y=round(1 + A.chg("2020-02-12", d1), 2), arkk_low=pct(A.low(d1, NOW)[0]), arkk_now=pct(A.chg(d1, NOW)),
        qqq_low=pct(q.low(d1, NOW)[0]), qqq_low_day=q.low(d1, NOW)[1], qqq_now=pct(q.chg(d1, NOW)))
    put("2_현금", qqq_low_from_d1=pct(q.low(d1, "2022-12-31")[0]), all_in_low_manwon=round(10000 * (1 + q.low(d1, "2022-12-31")[0])),
        keep_cash_low_manwon=round(8000 * (1 + q.low(d1, "2022-12-31")[0]) + 2000 * (1 + cash.chg(d1, q.low(d1, "2022-12-31")[1]))))
    put("3_기준", qqq_peak_to_d3=pct(q.chg("2021-12-27", d3)), further_low=pct(q.low(d3, "2022-12-31")[0]), hold_to_now=pct(q.chg(d3, NOW)),
        panic_to_now=pct((1 + q.chg(d3, dSell)) * (1 + cash.chg(dSell, dBack)) * (1 + q.chg(dBack, NOW)) - 1), years_out=yrs(dSell, dBack),
        morningstar="Mind the Gap 2024 (미국 · 2023년까지 10년): 투자자 수익이 펀드 수익보다 해마다 약 1.1%p 낮음 = 10년 수익의 약 15%를 놓침")
    put("4_손절", smci_buy_to_d4=pct(M.chg(dS, d4)), months=months(dS, d4), further_low=pct(M.low(d4, NOW)[0]), further_low_day=M.low(d4, NOW)[1],
        smci_now=pct(M.chg(d4, NOW)), qqq_low=pct(q.low(d4, NOW)[0]), qqq_now=pct(q.chg(d4, NOW)),
        odean="Odean 1998 Journal of Finance (미국 할인 증권사 1만 계좌): 판 이익 종목이 들고 있던 손실 종목보다 다음 1년 약 3.4%p 더 오름")
    put("5_분산", mstr_prior_1y=round(1 + B.chg("2023-11-20", d5), 1), mstr_low=pct(B.low(d5, NOW)[0]), mstr_low_day=B.low(d5, NOW)[1], mstr_now=pct(B.chg(d5, NOW)),
        qqq_low=pct(q.low(d5, NOW)[0]), qqq_now=pct(q.chg(d5, NOW)), sectors="purpose_numbers_2026-10-31.json A_sectors: 1999년 이후 9개 업종 중 6개가 S&P 500(−55.3%)보다 깊이 빠짐")
    # 김씨(오답만): 1억 → ARKK → 06-16 모두 매도(국채) → 2023-12-13 나스닥 → 2024-03-13 SMCI(지인 추천) → 버팀 → 2024-11-20 MSTR → 지금
    w = 10000 * (1 + A.chg(d1, dSell))
    w *= 1 + cash.chg(dSell, dBack)
    w *= 1 + q.chg(dBack, dS)
    w *= 1 + M.chg(dS, d5)
    w *= 1 + B.chg(d5, NOW)
    # 정답만: 8천 나스닥 보유 + 2천 현금(국채)
    g = 8000 * (1 + q.chg(d1, NOW)) + 2000 * (1 + cash.chg(d1, NOW))
    put("김씨_경로", wrong_now_manwon=round(w), wrong_loss=pct(w / 10000 - 1), correct_now_manwon=round(g), years=yrs(d1, NOW), qqq_same=pct(q.chg(d1, NOW)))
    return R


def nasdaq_1_v22(S):
    """v2.2 — 1편 대본 v9 (사용자 피드백판 2026-11-02, 1편 롱폼 10건):
    도입 = 4년 안·−70% 안팎 · ① ETF 말고 기술주 종목 · ② 현금 더 (2천 → 3천만 원) · ③ 정답 = 위험한 국면에서 기준대로 비중을 줄이고 나눠 다시 매수
    · ④ 펀더멘털에 문제가 생긴 그날 매도 · ⑤ 분배(한 종목 비중)에 중점 — 1번(종목 따라 사기)과 겹치지 않게.
    ① 2023-08-01 업스타트(UPST, 1년 3.0배) vs 나스닥 ② 같은 날 1억 전부 vs 3천만 원 현금 남김
    ③ 2025-03-10 나스닥(QQQ)이 고점(2025-02-19)보다 처음 10% 넘게 하락한 날 — 그때그때(김씨: 2025-04-08 바닥에서 모두 매도 → 최고가를 되찾은 2025-06-24 다시 매수)
       vs 기준대로(다음 거래일 03-11 종가에 주식 절반 매도 → 04-01·05-01·06-02 세 번에 나눠 다시 매수, 기다리는 현금은 국채 이자)
    ④ 2025-07-01 지인 추천으로 C3.ai(AI) 매수(계좌의 절반) → 2025-08-11 예상보다 훨씬 적은 매출 예비 발표·한 해 전망 철회로 하루 −25.6% — 그날 종가에 매도해 나스닥 vs 버팀
    ⑤ 2025-10-13 아이온큐(IONQ, 양자 컴퓨터, 1년 7.6배 · 그해 최고가) — 계좌의 절반 vs 10%까지만(나머지 나스닥). 비중은 산 뒤 다시 맞추지 않음.
    금액 = 1억 원 × 달러 기준 변화율 (환율·세금·수수료 뺌) · 현금 = 13주 국채 이자."""
    q, cash, U, C, I = S["QQQ"], S["CASH"], S["UPST"], S["AI"], S["IONQ"]
    NOW = "2026-10-27"
    d1, dPk, dSig, dCut, dRe, dP, dB = "2023-08-01", "2025-02-19", "2025-03-10", "2025-03-11", ("2025-04-01", "2025-05-01", "2025-06-02"), "2025-04-08", "2025-06-24"
    dTip, d4, d5 = "2025-07-01", "2025-08-11", "2025-10-13"
    R = {}

    def put(key, **kw):
        R[key] = kw
        log.info("key=%s %s", key, json.dumps(kw, ensure_ascii=False)[:700], extra={"stage": "NASDAQ1v22"})

    def mix_path(parts, a, b):
        """parts = [(Ser, 무게)] — a 날 산 뒤 그대로 둠 → b 날 값 · 가장 낮은 값과 그 날 (원금 1)."""
        days = [d for d in q.k if a <= d <= b]
        vals = [sum(w * s.at(d) / s.at(a) for s, w in parts) for d in days]
        m = int(np.argmin(vals))
        return round(vals[-1], 4), round(vals[m], 4), days[m]

    def rule(a_sig, cut, re_days, frac=0.5, end=NOW):
        """신호 날 원금 1 — cut 날 종가에 frac 매도(국채) → re_days 에 같은 몫으로 다시 매수. → (end 값, 가장 낮은 값, 그 날)."""
        u, c, part, lo, lod = 1 / q.at(a_sig), 0.0, None, 1.0, a_sig
        for d in [x for x in q.k if a_sig <= x <= end]:
            if d == q.day(cut) and c == 0.0:
                c = u * frac * q.at(d); u *= 1 - frac; part = c / len(re_days)
            if part and d in {q.day(x) if q.day(x) >= x else q.k[q.i(x) + 1] for x in re_days} and c > 1e-12:
                u += part / q.at(d); c -= part
            v = u * q.at(d) + c
            if v < lo:
                lo, lod = v, d
            if c > 0:
                nxt = q.k[min(q.i(d) + 1, len(q.k) - 1)]
                c *= 1 + cash.chg(d, nxt)
        return round(u * q.at(end) + c, 4), round(lo, 4), lod

    # ① 남 따라 사기
    put("1_남따라", upst_prior_1y=round(1 + U.chg("2022-08-01", d1), 2), upst_low=pct(U.low(d1, NOW)[0]), upst_low_day=U.low(d1, NOW)[1], upst_now=pct(U.chg(d1, NOW)),
        qqq_low=pct(q.low(d1, NOW)[0]), qqq_low_day=q.low(d1, NOW)[1], qqq_now=pct(q.chg(d1, NOW)), years_to_now=yrs(d1, NOW))
    # ② 현금 3천만 원 — 2025 봄 하락장 (최고가 02-19 → 바닥 04-08)
    v_pk, v_lo = 10000 * (1 + q.chg(d1, dPk)), 10000 * (1 + q.chg(d1, dP))
    put("2_현금", all_in_at_peak_manwon=round(v_pk), all_in_at_low_manwon=round(v_lo), drop_manwon=round(v_pk - v_lo), drop_pct=pct(v_lo / v_pk - 1), days=(date.fromisoformat(dP) - date.fromisoformat(dPk)).days,
        all_in_vs_principal_at_low=pct(v_lo / 10000 - 1), cash3000_at_low_manwon=round(3000 * (1 + cash.chg(d1, dP))), invest7000_drop_manwon=round(0.7 * (v_pk - v_lo)))
    # ③ 위험한 국면 — 기준대로 비중 절반 줄이고 나눠 다시 vs 그때그때(바닥 매도·최고가 회복 뒤 재매수) vs 그대로
    r_now, r_lo, r_lod = rule(dSig, dCut, dRe)
    panic = (1 + q.chg(dSig, dP)) * (1 + cash.chg(dP, dB)) * (1 + q.chg(dB, NOW))
    put("3_기준", qqq_peak=dPk, peak_to_sig=pct(q.chg(dPk, dSig)), sig_is_first_minus10=q.first_below(dPk, -0.10) == dSig,
        rule_now=pct(r_now - 1), rule_low=pct(r_lo - 1), rule_low_day=r_lod, hold_now=pct(q.chg(dSig, NOW)), hold_low=pct(q.low(dSig, NOW)[0]), hold_low_day=q.low(dSig, NOW)[1],
        panic_now=pct(panic - 1), panic_sell_vs_sig=pct(q.chg(dSig, dP)), panic_out_days=(date.fromisoformat(dB) - date.fromisoformat(dP)).days, back_day_is_new_high=q.at(dB) >= q.at(dPk),
        rule_1y=pct(rule(dSig, dCut, dRe, end="2026-03-10")[0] - 1), hold_1y=pct(q.chg(dSig, "2026-03-10")),
        morningstar="Mind the Gap 2024 (미국 · 2023년까지 10년): 투자자 수익이 펀드 수익보다 해마다 약 1.1%p 낮음 = 10년 수익의 약 15%를 놓침")
    # ④ 펀더멘털 — C3.ai 2025-08-11
    put("4_손절", ai_tip_to_before=pct(C.chg(dTip, "2025-08-08")), ai_day_drop=pct(C.chg("2025-08-08", d4)), ai_tip_to_d4=pct(C.chg(dTip, d4)),
        further_low=pct(C.low(d4, NOW)[0]), further_low_day=C.low(d4, NOW)[1], ai_now=pct(C.chg(d4, NOW)), qqq_low=pct(q.low(d4, NOW)[0]), qqq_now=pct(q.chg(d4, NOW)),
        odean="Odean 1998 Journal of Finance (미국 할인 증권사 1만 계좌): 판 이익 종목이 들고 있던 손실 종목보다 다음 1년 약 3.4%p 더 오름")
    # ⑤ 분배 — 아이온큐 비중
    h_now, h_lo, h_lod = mix_path([(I, 0.5), (q, 0.5)], d5, NOW)
    t_now, t_lo, t_lod = mix_path([(I, 0.1), (q, 0.9)], d5, NOW)
    put("5_분배", ionq_prior_1y=round(1 + I.chg("2024-10-11", d5), 1), ionq_is_peak_2025=I.peak_before("2025-12-31")[0] == d5, ionq_low=pct(I.low(d5, NOW)[0]), ionq_low_day=I.low(d5, NOW)[1], ionq_now=pct(I.chg(d5, NOW)),
        half_now=pct(h_now - 1), half_low=pct(h_lo - 1), half_low_day=h_lod, ten_now=pct(t_now - 1), ten_low=pct(t_lo - 1), ten_low_day=t_lod,
        qqq_now=pct(q.chg(d5, NOW)), sectors="purpose_numbers_2026-10-31.json A_sectors: 1999년 이후 9개 업종 중 6개가 S&P 500(−55.3%)보다 깊이 빠짐")
    # 김씨 (오답만): 1억 → UPST 전부 → 04-08 모두 매도(국채) → 06-24 나스닥 → 07-01 계좌 절반 C3.ai → 버팀 → 10-13 계좌 절반을 나스닥에서 아이온큐로 → 지금
    w = 10000 * (1 + U.chg(d1, dP)) * (1 + cash.chg(dP, dB)) * (1 + q.chg(dB, dTip))
    wC, wQ = w / 2, w / 2
    wC *= 1 + C.chg(dTip, d5); wQ *= 1 + q.chg(dTip, d5)
    half = (wC + wQ) / 2
    wI, wQ = half, wQ - half
    kim_d5 = wC + wI + wQ
    wC *= 1 + C.chg(d5, NOW); wI *= 1 + I.chg(d5, NOW); wQ *= 1 + q.chg(d5, NOW)
    kim = wC + wI + wQ
    # 정답만: 7천 나스닥 + 3천 국채 → ③ 기준대로(나스닥 몫) → 07-01 주식 몫 절반 C3.ai → 08-11 매도·나스닥 → 10-13 계좌의 10% 아이온큐(나스닥에서) → 지금
    g_cash = 3000 * (1 + cash.chg(d1, NOW))
    g_q = 7000 * (1 + q.chg(d1, dSig))
    g_q *= rule(dSig, dCut, dRe, end=dTip)[0]
    gC, gQ = g_q / 2, g_q / 2
    gC *= 1 + C.chg(dTip, d4); gQ *= 1 + q.chg(dTip, d4)
    gQ += gC
    gQ *= 1 + q.chg(d4, d5)
    acct = gQ + 3000 * (1 + cash.chg(d1, d5))
    gI = 0.1 * acct; gQ -= gI
    good = gQ * (1 + q.chg(d5, NOW)) + gI * (1 + I.chg(d5, NOW)) + g_cash
    put("김씨_경로", wrong_now_manwon=round(kim), wrong_loss=pct(kim / 10000 - 1), wrong_at_d5_manwon=round(kim_d5), wrong_parts_now_manwon={"AI": round(wC), "IONQ": round(wI), "QQQ": round(wQ)},
        correct_now_manwon=round(good), correct_gain=pct(good / 10000 - 1), years=yrs(d1, NOW), qqq_same=pct(q.chg(d1, NOW)),
        note="김씨 = 함정 답만 · 정답 = 정답만 (④의 지인 추천 매수는 이야기 전제 — 두 길 모두 산 것으로 셈)")
    return R


def main():
    S = load()
    for sym in ("QQQ", "QLD", "SMCI", "NVDA", "MSTR", "UPST", "AI", "IONQ"):
        S[sym] = Ser(sym, rd(HERE / "data" / f"{sym}.csv", "adjclose"))
    F = facts(S)
    P = paths(S)
    N1 = nasdaq_1(S)
    N2 = nasdaq_1_v21(S)
    N3 = nasdaq_1_v22(S)
    out = HERE / f"longform_items_{date.today().isoformat()}.json"
    out.write_text(json.dumps({"tool": f"longform_items.py {VERSION}", "data_last": S["TR"].k[-1], "facts": F, "paths": P, "nasdaq_1편": N1, "nasdaq_1편_v2.1": N2, "nasdaq_1편_v2.2": N3}, ensure_ascii=False, indent=1), "utf-8")
    log.info("file=%s items=%d", out.name, sum(len(v) for v in F.values()), extra={"stage": "DONE"})


if __name__ == "__main__":
    main()
