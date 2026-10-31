#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-31 — 최초. 주식 롱폼 1~4편 대본(사용자 지시 2026-10-31 "롱폼 내용은 1편 쇼츠 처럼 도입부는 좋지 않은 사례인 A씨 사연을 짧게 … 항목 선택지는 …
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
VERSION = "v1.0"
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
    for sym in ("ARKK", "META", "PYPL", "LCID", "XLK", "XLF", "AGG"):
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


def main():
    S = load()
    F = facts(S)
    out = HERE / f"longform_items_{date.today().isoformat()}.json"
    out.write_text(json.dumps({"tool": f"longform_items.py {VERSION}", "data_last": S["TR"].k[-1], "facts": F}, ensure_ascii=False, indent=1), "utf-8")
    log.info("file=%s items=%d", out.name, sum(len(v) for v in F.values()), extra={"stage": "DONE"})


if __name__ == "__main__":
    main()
