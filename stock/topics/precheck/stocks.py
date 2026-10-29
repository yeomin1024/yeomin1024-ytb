#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-29 — 최초. 정답 미리 확인 2회차 (사용자 지시 2026-10-29 "주식 주제 평가판 평가했는데 다시 주제 탐색해봐") —
#          평가에서 좋음을 받은 쪽(실제 사건·실제 회사)의 후보를 계산한다. precheck.py v1.1 이 불러 TOPICS 에 넣음.
#
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.0 | 2026-10-29 | 최초 — 구성 종목 일괄 자료(bulk.py 캐시) · 사건 날짜 뒤 1년 · 종목 사건 연구(편입·분할·급등) · 작년 1등 · 10배 종목 하락폭 · 배당률 상위 · 이익과 주가 · PER · 자사주 · 버크셔 · 전문가 예측 | 전부 |
#
# 미리 보기 점검 (lookahead): 사는 날의 판단은 그날 종가까지 알려진 값만 — 재무 수치(회계연도 E)는 E+75일(발표 뒤로 잡은 날)부터 씀 ·
#   편입·분할은 그날(효력일) 종가에 삼 · 급등은 다음 거래일 종가에 삼. 이익과 주가(T011)는 '같은 해 설명'이라 사는 규칙이 아님 — 결과에 적음.
# ⚠ 생존 편향: 종목 자료는 지금 S&P 500 회사만 — 주제마다 편향이 결론을 어느 쪽으로 미는지 bias 칸에 적음.
# ※ 연구·교육용 — 투자 권유가 아님.
import csv
import json
import pickle
from datetime import date, timedelta
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
BULK = HERE / "bulk"
classify = classify_full = cells = flat = on = fetch = None     # precheck.py 가 bind() 로 넣음 (같은 분류 규칙)


def bind(**kw):
    globals().update(kw)
VERSION = "v1.0"
YEAR = 365


def _o(d):
    return d.toordinal()


class Px:
    __slots__ = ("sym", "o", "close", "adj", "div", "split", "sector", "added")

    def at(self, day, field="adj"):
        """day(서수) 이하 마지막 거래일 값 — 자료 전이면 nan."""
        i = int(np.searchsorted(self.o, day, side="right")) - 1
        return float(getattr(self, field)[i]) if i >= 0 else float("nan")

    def has(self, a, b):
        return len(self.o) and self.o[0] <= a and self.o[-1] >= b


def load_bulk(log):
    """bulk/px/*.csv → {기호: Px} (pickle 캐시 bulk/px.pkl — CSV 가 더 새로우면 다시)."""
    pk = BULK / "px.pkl"
    files = sorted((BULK / "px").glob("*.csv"))
    if not files:
        raise RuntimeError("bulk/px 가 비어 있음 — 다음: python3 -B stock/topics/precheck/bulk.py prices")
    if pk.exists() and pk.stat().st_mtime >= max(f.stat().st_mtime for f in files):
        with pk.open("rb") as f:
            P = pickle.load(f)
        log("LOAD", source="bulk/px.pkl", symbols=len(P))
        return P
    meta = {r["Symbol"]: r for r in csv.DictReader((BULK / "constituents.csv").open(encoding="utf-8"))}
    P = {}
    for fp in files:
        with fp.open(encoding="utf-8") as f:
            rows = list(csv.DictReader(ln for ln in f if not ln.startswith("#")))
        if not rows:
            continue
        p = Px()
        p.sym = fp.stem
        p.o = np.array([_o(date.fromisoformat(r["date"])) for r in rows])
        p.close = np.array([float(r["close"]) for r in rows])
        p.adj = np.array([float(r["adjclose"]) for r in rows])
        p.div = np.array([float(r["div"]) if r["div"].strip() else 0.0 for r in rows])
        p.split = np.array([float(r["split"]) if r["split"].strip() else 0.0 for r in rows])
        m = meta.get(p.sym, {})
        p.sector, p.added = m.get("GICS Sector", ""), m.get("Date added", "")
        P[p.sym] = p
    with pk.open("wb") as f:
        pickle.dump(P, f)
    log("LOAD", source="bulk/px/*.csv", symbols=len(P), rows=sum(len(p.o) for p in P.values()))
    return P


def load_fa():
    out = {}
    for fp in sorted((BULK / "fa").glob("*.json")):
        s = json.loads(fp.read_text("utf-8"))["series"]
        out[fp.stem] = s
    return out


class Ix:
    """S&P 500 배당 포함(tr)·가격(px) 지수 — 서수 날짜로 빠르게."""

    def __init__(self, B):
        self.o = np.array([_o(x) for x in B.d])
        self.tr, self.px, self.cash = B.tr, B.price, B.cash
        self.last = int(self.o[-1])

    def at(self, day, v=None):
        v = self.tr if v is None else v
        i = int(np.searchsorted(self.o, day, side="right")) - 1
        return float(v[i]) if i >= 0 else float("nan")

    def next_trading(self, day):
        """day 이상 첫 거래일 (장이 닫힌 날의 사건 → 다음 거래일)."""
        i = int(np.searchsorted(self.o, day, side="left"))
        return int(self.o[min(i, len(self.o) - 1)])


def pct(x, nd=1):
    return "-" if x is None or x != x else f"{x * 100:.{nd}f}%"


def usd(x):
    return "-" if x is None or x != x else f"{x:,.0f}달러"


def frac(xs):
    xs = [x for x in xs if x is not None]
    return float(np.mean(xs)) if xs else None


# ---------------------------------------------------------------- 사건 날짜 뒤 지수
def event_rows(I, events, horizons=((30, "1m"), (YEAR, "1y"), (2 * YEAR, "2y"))):
    rows = []
    for name, ds in events:
        d0 = I.next_trading(_o(date.fromisoformat(ds)))
        r = {"event": name, "date": ds, "buy_day": date.fromordinal(d0).isoformat()}
        for h, lab in horizons:
            if d0 + h <= I.last:
                r[lab] = I.at(d0 + h) / I.at(d0) - 1
                r[f"{lab}_usd_10k"] = round(10000 * (1 + r[lab]))
        rows.append(r)
    return rows


def t028(B, I, P, F):
    ev = [("9·11 뒤 다시 연 날", "2001-09-17"), ("이라크전 시작", "2003-03-20"), ("러시아 크림반도", "2014-03-03"), ("솔레이마니 공습", "2020-01-03"),
          ("우크라이나 침공", "2022-02-24"), ("하마스 공격 뒤 첫 거래일", "2023-10-09"), ("이란의 이스라엘 공습 뒤 첫 거래일", "2024-04-15"),
          ("이스라엘-이란 공습", "2025-06-13"), ("미국의 이란 핵시설 공습 뒤 첫 거래일", "2025-06-23")]
    rows = event_rows(I, ev)
    y1 = [r for r in rows if "1y" in r]
    loss1 = [r["event"] for r in y1 if r["1y"] < 0]
    loss1m = [r["event"] for r in rows if r.get("1m", 0) < 0]
    base = _base_rate(I, YEAR)
    return {"class": "사실형", "answer": f"1년 뒤 손실 {len(loss1)}/{len(y1)}번 ({', '.join(loss1) or '없음'}) · 1개월 뒤 손실 {len(loss1m)}/{len(rows)}번",
            "base_rate_1y_positive": pct(base), "table": rows,
            "why": "사건마다 숫자는 분명(사실) · 9번은 적고 서로 다른 때라 '전쟁 나면 사라'는 규칙으로 넓히면 안 됨 — 손실은 사건보다 그때 이어진 하락장(2001·2022)이 만듦 · 날짜는 보도 기준(대본 전 원문 확인)"}


def _base_rate(I, h):
    """2000년 이후 아무 날이나 넣었을 때 h 일 뒤 오른 몫 (비교 기준)."""
    o0 = _o(date(2000, 1, 1))
    idx = np.flatnonzero((I.o >= o0) & (I.o + h <= I.last))
    j = np.searchsorted(I.o, I.o[idx] + h, side="right") - 1
    return float(np.mean(I.tr[j] > I.tr[idx]))


def t029(B, I, P, F):
    ev = [("2001년 첫 인하", "2001-01-03"), ("2007년 첫 인하", "2007-09-18"), ("2019년 첫 인하", "2019-07-31"), ("2024년 첫 인하", "2024-09-18")]
    hk = [("2004년 첫 인상", "2004-06-30"), ("2015년 첫 인상", "2015-12-16"), ("2022년 첫 인상", "2022-03-16")]
    rows, hikes = event_rows(I, ev), event_rows(I, hk)
    extra = event_rows(I, [("2020년 긴급 인하(따로)", "2020-03-03")])
    loss = [r["event"] for r in rows if r.get("1y", 0) < 0]
    big = [r["event"] for r in rows if r.get("1y", 0) < -0.10]
    hup = [r["event"] for r in hikes if r.get("1y", 0) > 0]
    return {"class": "사실형", "answer": f"인하 시작 1년 뒤 손실 {len(loss)}/4번 ({', '.join(loss) or '없음'}) · 10% 넘게 빠짐 {len(big)}번 · 인상 시작 1년 뒤 늘어남 {len(hup)}/3번 ({', '.join(hup) or '없음'})",
            "table": rows + extra, "hikes": hikes,
            "why": "7번뿐인 사실 · 2001·2007 인하는 경기 침체가 시작될 때라 손실 — '금리 인하 = 오른다'도 '인상 = 빠진다'도 맞지 않았음 · 날짜는 연준 발표일(대본 전 원문 확인)"}


def t040(B, I, P, F):
    ev = [("S&P 강등 뒤 첫 거래일", "2011-08-08"), ("피치 강등 뒤 첫 거래일", "2023-08-02"), ("무디스 강등 뒤 첫 거래일", "2025-05-19")]
    rows = event_rows(I, ev)
    up = [r["event"] for r in rows if r.get("1y", -1) > 0]
    m1 = [r["event"] for r in rows if r.get("1m", 0) < 0]
    return {"class": "사실형", "answer": f"1년 뒤 늘어남 {len(up)}/{sum(1 for r in rows if '1y' in r)}번 · 1개월 뒤 손실 {len(m1)}/{len(rows)}번 ({', '.join(m1) or '없음'})", "table": rows,
            "why": "3번뿐인 사실 · '나쁜 뉴스 = 팔 때'를 3번으로 뒤집는 규칙이 아님 · 날짜는 발표 보도(장 마감 뒤 발표 → 다음 거래일 — 대본 전 원문 확인)"}


def t042(B, I, P, F):
    ev = [("2001년 침체 선언", "2001-11-26"), ("2008년 침체 선언", "2008-12-01"), ("2020년 침체 선언", "2020-06-08")]
    rows = event_rows(I, ev)
    for r in rows:
        d0 = _o(date.fromisoformat(r["buy_day"]))
        m = (I.o >= d0 - 2 * YEAR) & (I.o <= d0 + 2 * YEAR)
        k = int(np.argmin(np.where(m, I.px, np.inf)))
        r["bottom_within_2y"] = date.fromordinal(int(I.o[k])).isoformat()
        r["bottom_vs_declare"] = "선언 뒤" if I.o[k] > d0 else "선언 전"
        r["drop_after_declare_to_bottom"] = pct(I.px[k] / I.at(d0, I.px) - 1) if I.o[k] > d0 else "-"
    up = [r["event"] for r in rows if r.get("1y", -1) > 0]
    return {"class": "사실형", "answer": f"1년 뒤 늘어남 {len(up)}/3번 ({', '.join(up) or '없음'}) · 바닥이 선언 뒤였던 때 {sum(1 for r in rows if r['bottom_vs_declare'] == '선언 뒤')}/3",
            "table": rows, "why": "3번뿐인 사실 · 선언은 침체가 시작된 지 몇 달 뒤라 바닥과 가까울 때가 많았지만 2001·2008 은 선언 뒤에 더 빠짐 → '선언 날 사라' 규칙이 아님 · 날짜는 NBER 발표(대본 전 원문 확인)"}


def t041(B, I, P, F):
    """원·달러 1,400원을 넘은 날(1,300원 아래로 내려갔다 다시 넘으면 새로 셈) 원화로 S&P 500(배당 포함)을 사서 1년 뒤 원화 금액."""
    s = fetch("KRW=X")
    fo, fx = np.array([_o(x) for x in s["d"]]), s["close"]
    ev, armed = [], True
    for o_, v in zip(fo, fx):
        if armed and v >= 1400:
            ev.append(int(o_))
            armed = False
        elif v < 1300:
            armed = True
    def fx_at(day):
        i = int(np.searchsorted(fo, day, side="right")) - 1
        return float(fx[i])
    rows = []
    for e in ev:
        d0 = I.next_trading(e)
        if d0 + YEAR > I.last:
            continue
        usd_r = I.at(d0 + YEAR) / I.at(d0)
        fx_r = fx_at(d0 + YEAR) / fx_at(d0)
        rows.append({"day": date.fromordinal(e).isoformat(), "fx": round(fx_at(d0), 1), "fx_1y": round(fx_at(d0 + YEAR), 1), "usd_return": pct(usd_r - 1),
                     "fx_change": pct(fx_r - 1), "krw_return": pct(usd_r * fx_r - 1), "krw_10m_after_1y": round(1e7 * usd_r * fx_r)})
    loss = [r["day"] for r in rows if r["krw_10m_after_1y"] < 1e7]
    # 비교: 2004년 이후 아무 날이나 원화로 샀을 때 1년 뒤 원화 손실 몫
    o0 = _o(date(2004, 1, 1))
    idx = [k for k in range(len(fo)) if fo[k] >= o0 and fo[k] + YEAR <= I.last]
    anyloss = frac([I.at(int(fo[k]) + YEAR) / I.at(int(fo[k])) * fx_at(int(fo[k]) + YEAR) / fx[k] < 1 for k in idx[::5]])
    return {"class": "사실형", "answer": f"1,400원 넘은 날 {len(rows)}번 중 1년 뒤 원화 손실 {len(loss)}번 ({', '.join(loss) or '없음'}) · 아무 날(2004~, 5일마다) 원화 손실 몫 {pct(anyloss)}",
            "table": rows, "why": "5번 중 3번이 2008~09년 한 위기 안 — 사실상 사건 3개 · 환율 몫은 1년 뒤 환율이 내려갔는지에 달림(그날엔 모름) → '1,400원이면 사지 마라/사라' 규칙이 아님 · Yahoo KRW=X 종가(매매기준율과 조금 다름)"}


def t033(B, I, P, F):
    ys = {}
    for y in range(1999, 2026):
        a, b = I.at(_o(date(y, 1, 1)) - 1), I.at(_o(date(y + 1, 1, 1)) - 1)
        ys[y] = b / a - 1
    a26 = I.at(I.last) / I.at(_o(date(2026, 1, 1)) - 1) - 1
    hot = [y for y in range(2000, 2025) if ys[y] > 0.20]
    nxt = {y: ys[y + 1] for y in hot}
    up = [y for y in hot if nxt[y] > 0]
    return {"class": "사실형", "answer": f"20% 넘게 오른 해 {len(hot)}번 중 다음 해에도 오른 때 {len(up)}번 · 빠진 해: {', '.join(str(y + 1) for y in hot if nxt[y] <= 0) or '없음'}",
            "table": {str(y): {"return": pct(ys[y]), "next": pct(nxt[y])} for y in hot}, "y2025": pct(ys[2025]), "y2026_to_last": pct(a26),
            "why": "연도별 사실 · 표본이 작아 '다음 해도 오른다'는 규칙이 아님 (오른 몫은 아무 해나 오른 몫과 비교해 적음)",
            "any_year_up": f"{sum(1 for y in range(2000, 2026) if ys[y] > 0)}/{2026 - 2000}"}


def t003(B, I, P, F):
    """S&P 500 가격 지수가 고점보다 20% 빠진 첫날 (새 고점이 나오면 다시 셈) — 판 사람(1년 현금 뒤 다시) · 버틴 사람 · 더 산 1만 달러."""
    o0 = _o(date(2000, 1, 1))
    m = I.o >= _o(date(1999, 1, 1))
    o, px = I.o[m], I.px[m]
    peak, armed, ev, near = px[0], True, [], []
    for k in range(1, len(o)):
        if px[k] > peak:                           # 새 고점 → 다음 −20% 를 다시 셈
            peak, armed = px[k], True
        dd = px[k] / peak
        if armed and dd <= 0.80 and o[k] >= o0:
            ev.append(int(o[k]))
            armed = False
    # 20% 에 못 미친 큰 하락 (밝히기만)
    for a, b in (("2018-09-20", "2019-03-01"), ("2025-02-01", "2025-06-01"), ("2011-04-29", "2011-12-31")):
        mm = (I.o >= _o(date.fromisoformat(a))) & (I.o <= _o(date.fromisoformat(b)))
        pk = I.px[(I.o >= _o(date.fromisoformat(a)) - 200) & (I.o <= _o(date.fromisoformat(b)))].max()
        near.append({"window": f"{a}~{b}", "max_drawdown_close": pct(I.px[mm].min() / pk - 1)})
    rows = []
    for d0 in ev:
        r = {"day": date.fromordinal(d0).isoformat()}
        for h, lab in ((YEAR, "1y"), (2 * YEAR, "2y")):
            if d0 + h > I.last:
                continue
            hold = I.at(d0 + h) / I.at(d0)
            cash1 = I.at(d0 + YEAR, I.cash) / I.at(d0, I.cash)
            sell = cash1 if h == YEAR else cash1 * I.at(d0 + h) / I.at(d0 + YEAR)
            r[lab] = {"hold_10k": round(10000 * hold), "sell_10k": round(10000 * sell), "winner": "판 사람" if sell > hold else "버틴 사람",
                      "extra_10k_bought": round(10000 * hold), "extra_10k_cash": round(10000 * (I.at(d0 + h, I.cash) / I.at(d0, I.cash)))}
        bottom = I.px[(I.o >= d0) & (I.o <= d0 + 2 * YEAR)].min() / I.at(d0, I.px) - 1
        r["further_drop_within_2y"] = pct(bottom)
        rows.append(r)
    s1 = [r["day"][:7] for r in rows if r.get("1y", {}).get("winner") == "판 사람"]
    s2 = [r["day"][:7] for r in rows if r.get("2y", {}).get("winner") == "판 사람"]
    n1, n2 = sum(1 for r in rows if "1y" in r), sum(1 for r in rows if "2y" in r)
    return {"class": "사실형", "answer": f"−20% 첫날 {len(rows)}번 · 1년 뒤 판 사람이 더 남음 {len(s1)}/{n1} ({', '.join(s1) or '없음'}) · 2년 뒤 {len(s2)}/{n2} ({', '.join(s2) or '없음'})",
            "table": rows, "near_misses": near,
            "why": "사건마다 누가 더 남았는지는 사실 · 판 쪽이 이긴 때는 그 뒤로 더 빠진 때(2001·2008) — 그날엔 알 수 없었음 → '−20%면 팔아라/버텨라' 규칙(조건부형)으로 넓히지 않고 사건별 문제로만 · −20%(종가) 판정은 가격 지수"}


# ---------------------------------------------------------------- 종목 사례
def _rel(p, I, d0, h=YEAR):
    """d0(서수 — 거래일) 종가에 산 종목 1년 뒤 ÷ 같은 날 지수 1년 뒤 → (종목 수익, 지수 수익) · 자료 없으면 None."""
    if d0 + h > min(I.last, int(p.o[-1])) or p.o[0] > d0:
        return None
    a0, a1 = p.at(d0), p.at(d0 + h)
    if not (a0 > 0 and a1 > 0):
        return None
    return a1 / a0 - 1, I.at(d0 + h) / I.at(d0) - 1


def t027(B, I, P, F):
    ev = [("AAPL", "2018-08-02"), ("AMZN", "2018-09-04"), ("MSFT", "2019-04-25"), ("GOOGL", "2020-01-16"), ("META", "2021-06-28"),
          ("TSLA", "2021-10-25"), ("NVDA", "2023-05-30"), ("AVGO", "2024-12-13")]
    rows, alt = [], {}
    for s, ds in ev:
        d0 = I.next_trading(_o(date.fromisoformat(ds)))
        r = {"sym": s, "day": ds}
        for h, lab in ((182, "6m"), (YEAR, "1y"), (2 * YEAR, "2y")):
            x = _rel(P[s], I, d0, h)
            if x:
                r[lab] = {"stock": pct(x[0]), "sp500": pct(x[1]), "stock_10k": round(10000 * (1 + x[0])), "beat": x[0] > x[1]}
        rows.append(r)
        # 날짜를 앞뒤 5거래일 옮겨도 1년 뒤 이긴 쪽이 같은지
        k = int(np.searchsorted(I.o, d0))
        alt[s] = sorted({bool(x[0] > x[1]) for j in range(max(k - 5, 0), min(k + 6, len(I.o))) if (x := _rel(P[s], I, int(I.o[j])))})
    w1 = [r["sym"] for r in rows if r.get("1y", {}).get("beat")]
    n1 = sum(1 for r in rows if "1y" in r)
    flip = [s for s, v in alt.items() if len(v) > 1]
    return {"class": "사실형", "answer": f"1년 뒤 S&P 500보다 더 남음 {len(w1)}/{n1} ({', '.join(w1)}) · 날짜 ±5거래일에 이긴 쪽이 바뀌는 회사: {', '.join(flip) or '없음'}",
            "table": rows, "why": "회사마다 사실 · 8곳은 적어 '큰 뉴스 날 사도 된다/늦었다' 규칙이 아님 · 1조 달러 첫날은 보도 기준(장중·종가가 갈림 — 대본 전 원문 확인)"}


def t031(B, I, P, F):
    rows = []
    for s, p in P.items():
        try:
            d = date.fromisoformat(p.added)
        except ValueError:
            continue
        if not (date(2015, 1, 1) <= d <= date(2025, 10, 27)):
            continue
        d0 = I.next_trading(_o(d))
        if p.o[0] > d0 - 5:                       # 편입 날 이전 주가가 없으면 (분사·새 상장) 뺌
            continue
        x = _rel(p, I, d0)
        if x:
            rows.append((s, d.isoformat(), x[0], x[1]))
    return _event_summary("편입일 종가에 사서 1년", rows, "빠진 회사가 없음 — 편입 뒤 나빠져 다시 빠진 회사가 없어 이긴 몫을 크게 보는 쪽",
                          cases=("TSLA", "PLTR", "UBER", "SMCI", "COIN", "DELL", "ABNB", "HOOD", "APP"))


def t039(B, I, P, F):
    rows, pre = [], []
    for s, p in P.items():
        for k in np.flatnonzero(p.split >= 2.0):
            d0 = int(p.o[k])
            if not (_o(date(2010, 1, 1)) <= d0 <= _o(date(2025, 10, 27))):
                continue
            x = _rel(p, I, d0)
            if x:
                rows.append((s, date.fromordinal(d0).isoformat(), x[0], x[1]))
                if p.o[0] <= d0 - YEAR:
                    pre.append(p.at(d0) / p.at(d0 - YEAR) - 1)
    r = _event_summary("분할 첫날 종가에 사서 1년", rows, "빠진 회사가 없음 — 분할하는 회사는 대개 많이 오른 회사라 빠지는 일이 드묾 · 편향은 이긴 몫을 크게 보는 쪽",
                       cases=("NVDA", "AAPL", "TSLA", "AMZN", "GOOGL", "AVGO", "WMT", "CMG"))
    r["pre_split_1y_median"] = pct(float(np.median(pre))) if pre else "-"
    return r


def t035(B, I, P, F):
    rows = []
    lo, hi = _o(date(2015, 1, 1)), _o(date(2025, 10, 27))
    for s, p in P.items():
        r = p.adj[1:] / p.adj[:-1] - 1
        last = -10 ** 9
        for k in np.flatnonzero(r >= 0.10):
            dj = int(p.o[k + 1])                   # 급등한 날
            if not (lo <= dj <= hi) or dj - last < 30 or k + 2 >= len(p.o):
                continue
            last = dj
            d0 = int(p.o[k + 2])                   # 다음 거래일 종가에 삼
            x = _rel(p, I, d0)
            if x:
                rows.append((s, date.fromordinal(dj).isoformat(), x[0], x[1]))
    r = _event_summary("+10% 다음 거래일 종가에 사서 1년", rows, "빠진 회사가 없음 — 급등 뒤 무너져 빠진 회사가 없어 이긴 몫을 크게 보는 쪽", cases=())
    return _biased(r, "이긴 몫이 절반을 넘는데 편향도 같은 쪽 — 급등 뒤 무너져 S&P 500 에서 빠진 회사, 그때 S&P 500 에 없던 작은 회사의 급등이 섞임")


def _biased(r, note):
    """v1.0 편향이 계산 결과와 같은 쪽이면 결론을 믿을 수 없음 → 미확인 (숫자는 참고로 남김)."""
    r["computed_class"], r["class"] = r["class"], "미확인"
    r["answer"] = "(참고 — 편향) " + r["answer"]
    r["why"] = f"계산 결과는 {r['computed_class']}지만 쓸 수 없음 — {note} · {r['why']}"
    return r


def _event_summary(rule, rows, bias, cases=()):
    """사건 연구 요약 — 해마다 이긴 몫(칸) → 분류 (정답형 55/60% · 차이없음 45~55% · 그 밖 조건부형)."""
    if not rows:
        return {"class": "미확인", "answer": "-", "why": "사건 0개"}
    by = {}
    for s, ds, a, b in rows:
        by.setdefault(ds[:4], []).append(a > b)
    early = [a > b for s, ds, a, b in rows if ds[:4] <= "2019"]
    late = [a > b for s, ds, a, b in rows if ds[:4] >= "2020"]
    allw = [a > b for *_, a, b in rows]
    cm = {"전체": frac(allw), "2015~19": frac(early) if len(early) >= 12 else None, "2020~25": frac(late) if len(late) >= 12 else None}
    years = {y: {"n": len(v), "beat": pct(frac(v))} for y, v in sorted(by.items())}
    cl, why = classify({k: v for k, v in cm.items() if v is not None})
    ex = np.array([a - b for *_, a, b in rows])
    case_rows = [{"sym": s, "day": ds, "stock": pct(a), "sp500": pct(b)} for s, ds, a, b in rows if s in cases]
    yb = [v for v in by.values() if len(v) >= 10]
    yrs_above = sum(1 for v in yb if np.mean(v) > 0.5)
    return {"class": cl, "answer": f"{rule}: 지수보다 더 남은 몫 {pct(cm['전체'])} (n={len(rows)}) · 2015~19 {pct(cm['2015~19'])} · 2020~25 {pct(cm['2020~25'])} · "
                                   f"해마다(10건 이상) 절반 넘게 이긴 해 {yrs_above}/{len(yb)} · 초과수익 중앙값 {pct(float(np.median(ex)))} · 평균 {pct(float(ex.mean()))}",
            "why": f"{why} · 편향: {bias}", "bias": bias, "years": years, "cases": case_rows, "n": len(rows)}


def t030(B, I, P, F):
    """해마다 전년 상승률 상위 10종목(지금 구성 종목 · 전년 초에 주가 있음) → 다음 1년 총수익 평균·중앙값 vs 지수."""
    rows = {}
    for Y in range(2010, 2026):
        a0, a1, a2 = _o(date(Y - 1, 1, 1)) - 1, _o(date(Y, 1, 1)) - 1, _o(date(Y + 1, 1, 1)) - 1
        if a2 > I.last:
            continue
        perf = []
        for s, p in P.items():
            if not p.has(a0 - 7, a2):
                continue
            perf.append((p.at(a1) / p.at(a0) - 1, p.at(a2) / p.at(a1) - 1, s))
        perf.sort(reverse=True)
        top, bot = perf[:10], perf[-10:]
        ix = I.at(a2) / I.at(a1) - 1
        rows[Y] = {"index": ix, "top_mean": float(np.mean([x[1] for x in top])), "top_median": float(np.median([x[1] for x in top])),
                   "top_beat": sum(1 for x in top if x[1] > ix), "bottom_mean": float(np.mean([x[1] for x in bot])),
                   "top": [(x[2], pct(x[0], 0), pct(x[1], 0)) for x in top[:3]], "n": len(perf)}
    lose_mean = [Y for Y, r in rows.items() if r["top_mean"] < r["index"]]
    lose_med = [Y for Y, r in rows.items() if r["top_median"] < r["index"]]
    n = len(rows)
    cm = {"앞(2010~17)·평균": frac([r["top_mean"] > r["index"] for Y, r in rows.items() if Y <= 2017]),
          "뒤(2018~25)·평균": frac([r["top_mean"] > r["index"] for Y, r in rows.items() if Y >= 2018]),
          "전체·중앙값": frac([r["top_median"] > r["index"] for r in rows.values()])}
    cl0, why = classify(cm)
    cl = "미확인"
    why = (f"계산 결과는 {cl0}({why})지만 쓸 수 없음 — ① 그해 S&P 500 에 없던 회사가 섞임(지금 구성 종목으로 골라서) ② 1등 뒤 무너져 빠진 회사가 없어 '따라 사도 됐다' 쪽으로 밂 "
           "→ 그때의 구성 종목 목록과 빠진 회사 주가가 있어야 함")
    return {"class": cl, "computed_class": cl0, "answer": f"(참고 — 편향) 작년 상위 10종목이 지수보다 덜 남은 해: 평균 {len(lose_mean)}/{n} · 중앙값 {len(lose_med)}/{n}",
            "cells": {k: pct(v) for k, v in cm.items()},
            "table": {str(Y): {"index": pct(r["index"]), "top10_mean": pct(r["top_mean"]), "top10_median": pct(r["top_median"]), "top10_beat": f"{r['top_beat']}/10",
                               "bottom10_mean": pct(r["bottom_mean"]), "top3": r["top"]} for Y, r in rows.items()},
            "why": why}


def t032(B, I, P, F):
    """3년에 3배(배당 포함) 넘게 오른 종목의 그 3년 안 가장 큰 하락폭 — 1월 시작 2010~2023."""
    rows = {}
    for Y in range(2010, 2024):
        a, b = _o(date(Y, 1, 1)) - 1, _o(date(Y + 3, 1, 1)) - 1
        if b > I.last:
            continue
        hits = []
        for s, p in P.items():
            if not p.has(a - 7, b):
                continue
            if p.at(b) / p.at(a) < 3:
                continue
            m = (p.o > a) & (p.o <= b)
            v = p.adj[m]
            mdd = float((v / np.maximum.accumulate(v) - 1).min())
            hits.append((s, p.at(b) / p.at(a), mdd))
        if len(hits) >= 10:                       # 10곳 미만 구간은 몫이 크게 흔들려 뺌
            rows[f"{Y}-01~{Y + 3}-01"] = {"n": len(hits), "dd30": frac([h[2] <= -0.30 for h in hits]), "dd40": frac([h[2] <= -0.40 for h in hits]),
                                    "dd50": frac([h[2] <= -0.50 for h in hits]),
                                    "examples": [(h[0], f"{h[1]:.1f}배", pct(h[2], 0)) for h in sorted(hits, key=lambda h: -h[1])[:6]]}
    tot = sum(r["n"] for r in rows.values())
    d30 = [r["dd30"] for r in rows.values()]
    last = rows.get("2023-01~2026-01")
    cl = "사실형" if last else "미확인"
    return {"class": cl, "answer": (f"가장 최근 구간 2023-01~2026-01: 3배 넘은 {last['n']}곳 중 30% 넘게 빠진 몫 {pct(last['dd30'])} · 40% {pct(last['dd40'])} · 50% {pct(last['dd50'])} · 예: "
                                    + ", ".join(f"{a} {b} 중 최대 {c}" for a, b, c in last["examples"]) if last else "-")
                                   + f" | 구간마다(10곳 이상 {len(rows)}개 · 연인원 {tot}) {pct(min(d30))}~{pct(max(d30))} — 구간에 따라 갈림",
            "table": {k: {**v, "dd30": pct(v["dd30"]), "dd40": pct(v["dd40"]), "dd50": pct(v["dd50"])} for k, v in rows.items()},
            "why": "회사마다 사실(가장 최근 구간) · 고른 종목이 대박 종목이라 생존 편향과 상관없음 · 구간마다 44~88% 로 갈려 '대박 종목은 늘 반토막'이라는 규칙(조건부형)으로 넓히지 않음",
            "ten_x_10y": _ten_x(I, P)}


def _ten_x(I, P):
    out = {}
    for Y in (2005, 2010, 2015):
        a, b = _o(date(Y, 10, 1)), _o(date(Y + 10, 10, 1))
        hits = []
        for s, p in P.items():
            if p.has(a - 7, b) and p.at(b) / p.at(a) >= 10:
                v = p.adj[(p.o > a) & (p.o <= b)]
                hits.append(float((v / np.maximum.accumulate(v) - 1).min()))
        out[f"{Y}-10~{Y + 10}-10"] = {"n": len(hits), "dd40": pct(frac([h <= -0.40 for h in hits])), "dd50": pct(frac([h <= -0.50 for h in hits]))}
    return out


def t038(B, I, P, F):
    rows = {}
    for Y in range(2010, 2024):
        a, b = _o(date(Y, 1, 1)) - 1, _o(date(Y + 3, 1, 1)) - 1
        if b > I.last:
            continue
        ix = I.at(b) / I.at(a)
        r = [p.at(b) / p.at(a) for p in P.values() if p.has(a - 7, b)]
        r = np.array(r)
        rows[f"{Y}-01~{Y + 3}-01"] = {"n": len(r), "beat": float(np.mean(r > ix)), "beat_2x": float(np.mean(r > 2 * ix))}
    b = [v["beat"] for v in rows.values()]
    l2 = [rows.get("2022-01~2025-01"), rows.get("2023-01~2026-01")]
    ok2 = all(x and x["beat"] < 0.45 for x in l2)
    cl = "사실형" if ok2 else "미확인"
    why = ("최근 두 구간 모두 45% 미만 — 지금 구성 종목만이라 빠진 회사를 넣으면 더 낮음(결론 쪽으로 단단)" if ok2 else "최근 구간도 45% 넘음 — 편향이 결론 쪽이 아님") + \
          " · 2010~2017년 시작 구간(57~64%)은 13년 넘게 살아남은 회사만이라 부풀어 쓰지 않음"
    return {"class": cl, "answer": f"최근 2022-01~2025-01 {pct(l2[0]['beat'] if l2[0] else None)} · 2023-01~2026-01 {pct(l2[1]['beat'] if l2[1] else None)} (지수 2배 넘게 오른 종목 {pct(l2[1]['beat_2x'] if l2[1] else None)}) | 3년 구간 {len(rows)}개 전체 {pct(min(b))}~{pct(max(b))}",
            "table": {k: {"n": v["n"], "beat": pct(v["beat"]), "beat_2x_index": pct(v["beat_2x"])} for k, v in rows.items()},
            "why": f"{why} · 편향: 지금 구성 종목만 — 그사이 빠진(대개 진) 회사가 없어 이긴 몫을 크게 보는 쪽 → 45% 미만이면 결론은 더 단단함"}


def t034(B, I, P, F):
    s = fetch("BRK-B")
    brk = on(B.d, s["d"], s["adj"])
    c = {}
    for h in ("2y", "5y"):
        W = B.W[h]
        st = np.array([a for a, e, _ in W])
        ok = ~np.isnan(brk[st])
        a = np.array([brk[e] / brk[s_] for s_, e, _ in W])[ok]
        bb = np.array([B.tr[e] / B.tr[s_] for s_, e, _ in W])[ok]
        c.update(cells(a, bb, st[ok], B.d, h))
    cm = flat(c)
    cl, why = classify_full(cm)
    return {"class": cl, "answer": "버크셔가 지수보다 더 남은 몫: " + " · ".join(f"{k} {pct(v)}" for k, v in cm.items()),
            "cells": c, "why": why + " · 버크셔 B주 수정 종가(배당 없음) vs S&P 500 배당 포함"}


# ---------------------------------------------------------------- 재무제표·배당
def _fy(F, s, key):
    return {date.fromisoformat(k): v for k, v in (F.get(s, {}).get(key) or {}).items()}


def t011(B, I, P, F):
    """순이익 +30% 이상 회계연도(앞 해 순이익 > 0)의 그 회계연도 주가 총수익 · 시작 PER (앞 해 말 종가 ÷ 앞 해 희석 EPS)."""
    rows = []
    for s, p in P.items():
        ni, eps = _fy(F, s, "annualNetIncome"), _fy(F, s, "annualDilutedEPS")
        ks = sorted(ni)
        for e0, e1 in zip(ks, ks[1:]):
            if not (300 <= (e1 - e0).days <= 430) or ni[e0] <= 0:
                continue
            g = ni[e1] / ni[e0] - 1
            o0, o1 = _o(e0), _o(e1)
            if not p.has(o0 - 7, o1) or o1 > I.last:
                continue
            r = p.at(o1) / p.at(o0) - 1
            pe0 = p.at(o0, "close") / eps[e0] if eps.get(e0, 0) > 0 else None
            pe1 = p.at(o1, "close") / eps[e1] if eps.get(e1, 0) > 0 else None
            rows.append({"sym": s, "fy_end": e1.isoformat(), "ni_growth": g, "ret": r, "pe0": pe0, "pe1": pe1,
                         "eps_growth": (eps[e1] / eps[e0] - 1) if eps.get(e0, 0) > 0 and e1 in eps else None})
    big = [r for r in rows if r["ni_growth"] >= 0.30]
    by = {}
    for r in big:
        by.setdefault(r["fy_end"][:4], []).append(r)
    cells_ = {}
    for y, v in sorted(by.items()):
        fell = [r for r in v if r["ret"] < 0]
        rose = [r for r in v if r["ret"] >= 0]
        pf = [r["pe0"] for r in fell if r["pe0"]]
        pr = [r["pe0"] for r in rose if r["pe0"]]
        cells_[y] = {"n": len(v), "fell": len(fell) / len(v), "pe0_fell_median": float(np.median(pf)) if pf else None,
                     "pe0_rose_median": float(np.median(pr)) if pr else None}
    use = {y: c for y, c in cells_.items() if c["n"] >= 15}
    fell_ok = all(c["fell"] >= 0.20 for c in use.values())
    pe_ok = all((c["pe0_fell_median"] or 0) > (c["pe0_rose_median"] or 0) for c in use.values())
    cases = sorted([r for r in big if r["ret"] < -0.15 and r["pe0"]], key=lambda r: r["ret"])[:8]
    allf = frac([r["ret"] < 0 for r in big])
    band_ok = all(0.15 <= c["fell"] <= 0.25 for c in use.values())                # 해마다 '다섯에 하나 안팎'
    cl = "사실형" if band_ok else "조건부형"
    allco = {}
    for r in rows:
        allco.setdefault("down" if r["ni_growth"] < 0 else ("big" if r["ni_growth"] >= 0.30 else "mid"), []).append(r["ret"] < 0)
    return {"class": cl, "answer": f"순이익 +30% 이상 회계연도 {len(big)}건 중 그해 주가가 빠진 몫 {pct(allf)} · 해마다 "
                                   + " · ".join(f"{y}년 끝 {pct(c['fell'])}(n={c['n']}, 시작 PER 빠진 쪽 {c['pe0_fell_median'] or 0:.0f} vs 오른 쪽 {c['pe0_rose_median'] or 0:.0f})" for y, c in use.items()),
            "fell_ge_20pct_every_year": fell_ok, "fell_15_25pct_every_year": band_ok, "pe_higher_in_fell_every_year": pe_ok,
            "fell_share_by_ni_group": {k: f"{pct(frac(v))} (n={len(v)})" for k, v in allco.items()},
            "cases": [{"sym": r["sym"], "fy_end": r["fy_end"], "ni_growth": pct(r["ni_growth"], 0), "ret": pct(r["ret"], 0),
                       "pe0": round(r["pe0"], 1), "pe1": round(r["pe1"], 1) if r["pe1"] else None} for r in cases],
            "why": "해마다 빠진 몫이 15~25% 안이면 사실형('다섯에 하나 안팎') · 20% 문턱은 해에 따라 갈려 쓰지 않음 · 시작 PER 이 빠진 쪽에서 더 높은지는 해마다 달라 까닭으로 쓰지 않음 · 같은 해 설명(사는 규칙 아님 — 회계연도 실적은 끝난 뒤 발표) · 회계연도 2023~2025(Yahoo 연간 4년) · 지금 구성 종목만 — 빠진 회사는 대개 더 나빠 '빠진 몫'을 작게 보는 쪽 · 시작 PER 은 앞 해 말 종가 ÷ 앞 해 EPS(그때는 아직 발표 전일 수 있음 — 설명용)"}


def t036(B, I, P, F):
    """회계연도 말 E 의 희석 EPS 로 E+75일(발표 뒤) 종가 PER — 100배 초과 · 15배 미만 → 그날부터 1년 vs 지수."""
    grp = {"over100": {}, "under15": {}}
    for s, p in P.items():
        eps = _fy(F, s, "annualDilutedEPS")
        for e, v in eps.items():
            if v <= 0:
                continue
            d0 = I.next_trading(_o(e) + 75)
            if not p.has(d0, d0) or d0 + YEAR > I.last:
                continue
            pe = p.at(d0, "close") / v
            x = _rel(p, I, d0)
            if not x:
                continue
            k = "over100" if pe > 100 else ("under15" if pe < 15 else None)
            if k:
                grp[k].setdefault(str(e.year), []).append((s, pe, x[0] > x[1], x[0], x[1]))
    res = {}
    for k, by in grp.items():
        res[k] = {y: {"n": len(v), "beat": pct(frac([z[2] for z in v])), "ex": [(z[0], round(z[1]), pct(z[3], 0)) for z in v[:4]]} for y, v in sorted(by.items())}
    cm = {f"PER100+·{y}": frac([z[2] for z in v]) for y, v in grp["over100"].items() if len(v) >= 8}
    cl, why = classify(cm) if cm else ("미확인", "표본 적음")
    return _biased({"class": cl, "answer": "PER 100배 넘는 쪽이 지수를 이긴 몫 — " + " · ".join(f"{k} {pct(v)}" for k, v in cm.items()) +
            " | 15배 미만 — " + " · ".join(f"{y} {v['beat']}(n={v['n']})" for y, v in res["under15"].items()),
            "table": res, "why": why + " · 회계연도 2022~2024 (Yahoo 연간) · 지금 구성 종목만"},
                   "PER 100배 넘는 쪽은 해마다 8~17곳뿐이고, 비싼 주식 중 무너져 빠진 회사가 없어 이긴 몫을 크게 보는 쪽 — 결론(이겼다·갈렸다)이 편향과 같은 쪽")


def t037(B, I, P, F):
    """자사주 매입 ÷ 시가총액(E+75일 종가 × 희석 평균 주식 수) 상위 10% → 그날부터 1년 평균 vs 지수."""
    by = {}
    for s, p in P.items():
        rep, sh = _fy(F, s, "annualRepurchaseOfCapitalStock"), _fy(F, s, "annualDilutedAverageShares")
        for e, v in rep.items():
            if e not in sh or sh[e] <= 0:
                continue
            d0 = I.next_trading(_o(e) + 75)
            if not p.has(d0, d0):
                continue
            mc = p.at(d0, "close") * sh[e]
            x = _rel(p, I, d0)
            if x and mc > 0:
                by.setdefault(str(e.year), []).append((s, -v / mc, x[0], x[1]))
    res, cm = {}, {}
    for y, v in sorted(by.items()):
        if len(v) < 100:
            continue
        v.sort(key=lambda z: -z[1])
        top = v[:max(len(v) // 10, 1)]
        tm, ixm = float(np.mean([z[2] for z in top])), float(np.mean([z[3] for z in top]))
        res[y] = {"n_all": len(v), "n_top": len(top), "buyback_yield_min_top": pct(top[-1][1]), "top_mean": pct(tm), "index_same_days": pct(ixm), "top_above_index": tm > ixm,
                  "top_beat_share": pct(frac([z[2] > z[3] for z in top])), "ex": [(z[0], pct(z[1]), pct(z[2], 0)) for z in top[:4]]}
        cm[y] = frac([z[2] > z[3] for z in top])
    cl, why = classify(cm) if cm else ("미확인", "표본 적음")
    wins = sum(1 for y in res if res[y]["top_above_index"])
    return _biased({"class": cl, "answer": f"자사주 상위 10% 평균이 지수보다 높은 해 {wins}/{len(res)} · 이긴 종목 몫 " + " · ".join(f"{y} {res[y]['top_beat_share']}" for y in res),
                    "table": res, "why": why + " · 회계연도 2022~2024 · 지금 구성 종목만"},
                   "3해 중 2해가 절반 안팎인데 빠진 회사가 없어 이긴 몫을 크게 보는 쪽 — '이겼다·갈렸다'가 편향과 같은 쪽 (2022년 35% 만 단단)")


def _payments(p):
    k = np.flatnonzero(p.div > 0)
    return p.o[k], p.div[k]


def _cut(p, a, b):
    """(a, b] 안 배당 삭감 — 한 번 배당 < 앞 4번 중앙값 × 0.75 · 또는 끊김(앞 3년 배당 간격 중앙값의 2배와 150일 중 큰 것보다 길게 안 줌)."""
    po, pv = _payments(p)
    for j in np.flatnonzero((po > a) & (po <= b)):
        prev = pv[max(0, j - 4):j]
        if len(prev) >= 2 and pv[j] < 0.75 * float(np.median(prev)):
            return date.fromordinal(int(po[j])).isoformat()
    past = po[(po > a - 3 * YEAR) & (po <= a)]
    med = float(np.median(np.diff(past))) if len(past) >= 3 else 91.0
    seq = list(po[(po > a - 2 * YEAR) & (po <= a)][-1:]) + list(po[(po > a) & (po <= b)]) + [b]
    for u, v in zip(seq, seq[1:]):
        if v - u > max(2 * med, 150):
            return f"끊김 {date.fromordinal(int(u)).isoformat()} 뒤"
    return None


def t022(B, I, P, F):
    """연말(2014~2022) 배당률 상위 10곳 — 3년 안 배당 삭감(한 번 배당 < 앞 4번 중앙값 × 0.75, 또는 앞 간격 중앙값의 2배·150일 넘게 끊김) · 3년 총수익 vs 지수."""
    rows = {}
    for Y in range(2014, 2023):
        a, b = _o(date(Y + 1, 1, 1)) - 1, _o(date(Y + 4, 1, 1)) - 1
        if b > I.last:
            continue
        cand = []
        for s, p in P.items():
            if not p.has(a - 400, b):
                continue
            po, pv = _payments(p)
            ttm = pv[(po > a - YEAR) & (po <= a)].sum()
            if ttm <= 0:
                continue
            cand.append((ttm / p.at(a, "close"), s))
        cand.sort(reverse=True)
        top = cand[:10]
        res = []
        for yld, s in top:
            p = P[s]
            res.append({"sym": s, "yield": yld, "cut": _cut(p, a, b), "tr3": p.at(b) / p.at(a) - 1, "sector": p.sector})
        ix = I.at(b) / I.at(a) - 1
        tm = float(np.mean([r["tr3"] for r in res]))
        rows[f"{Y}년 말"] = {"cuts": sum(1 for r in res if r["cut"]), "top_mean_3y": pct(tm), "index_3y": pct(ix), "below_index": tm < ix,
                            "top_median_3y": pct(float(np.median([r["tr3"] for r in res]))), "top10": res}
    n = len(rows)
    c2 = sum(1 for r in rows.values() if r["cuts"] >= 2)
    bl = sum(1 for r in rows.values() if r["below_index"])
    cl0 = "정답형" if c2 >= 2 * n / 3 and bl >= 2 * n / 3 else ("조건부형" if c2 <= n / 2 or bl <= n / 2 else "사실형")    # 둘 다 2/3 넘는 해 = 정답형 · 하나라도 절반 이하 = 조건부형
    cl = "미확인"
    return {"class": cl, "computed_class": cl0, "answer": f"(참고 — 쓸 수 없음) 연말 {n}번 중 3년 안 2곳 이상 배당을 깎은 해 {c2}번 · 3년 총수익이 지수보다 낮은 해 {bl}번 · 평균 삭감 {np.mean([r['cuts'] for r in rows.values()]):.1f}곳",
            "table": {k: {kk: vv for kk, vv in v.items() if kk != 'top10'} | {"top10": [(r['sym'], pct(r['yield']), r['cut'] or '-', pct(r['tr3'], 0)) for r in v['top10']]} for k, v in rows.items()},
            "why": "쓸 수 없음 — ① 특별배당·분사 몫이 배당률 1등으로 잡힘(KLAC 2014 · DHR·LDOS 2016) ② 그때 S&P 500 에 없던 회사(APO·KKR·BX — 실적 따라 바뀌는 분배금)가 섞여 '삭감'이 부풀고 ③ 배당을 깎고 무너져 빠진 회사가 없어 총수익은 지수보다 높게 나옴(9번 중 8번) "
                   "→ 그때의 구성 종목 목록과 빠진 회사 주가가 있어야 함 · 다우 30(구성 이력이 짧고 분명)으로 바꾸려 했으나 월그린스(WBA — 2024년 배당 48% 삭감)가 2025년 상장 폐지로 Yahoo 자료 없음"}


def t012(B, I, P, F):
    """연초 월가 연말 목표치(보도) vs 실제 연말 종가(^GSPC)."""
    tg = {2022: (5000, "중앙값 약 5,000 (Bloomberg 집계 — investmentnews 보도)"), 2023: (4009, "평균 4,009 (Forbes)"),
          2024: (4861, "평균 4,861 (2023년 말 조사 — Financial Samurai·WT Wealth 정리)"), 2025: (6570, "중앙값 6,570 (Bloomberg 1월 조사 — Schwab 정리) · CNBC 평균 6,630")}
    rows, miss10, wrong_dir = {}, [], []
    for y, (t, src) in tg.items():
        act = I.at(_o(date(y + 1, 1, 1)) - 1, I.px)
        start = I.at(_o(date(y, 1, 1)) - 1, I.px)
        m = act / t - 1
        rows[str(y)] = {"target": t, "actual": round(act, 2), "miss": pct(m), "start": round(start, 2), "target_dir": "오름" if t > start else "내림",
                        "actual_dir": "오름" if act > start else "내림", "source": src}
        if abs(m) > 0.10:
            miss10.append(y)
        if (t > start) != (act > start):
            wrong_dir.append(y)
    return {"class": "사실형", "answer": f"4년 중 10% 넘게 빗나간 해 {len(miss10)}번 ({', '.join(map(str, miss10))}) · 방향이 틀린 해 {', '.join(map(str, wrong_dir)) or '없음'}",
            "table": rows, "extra": "Nationwide: 지난 16년 중 13년 월가 연말 목표치가 실제보다 낮았고 평균 약 10% 빗나감",
            "why": "보도 숫자(2차 출처 섞임 — 대본 전 Bloomberg·CNBC 원문 확인) · 4년은 적어 '예측은 늘 틀린다'가 아니라 '해마다 얼마 빗나갔나'만 · 2020·2021 조사 값은 이 환경에서 못 찾음"}


TOPICS2 = {"T003": t003, "T011": t011, "T012": t012, "T022": t022, "T027": t027, "T028": t028, "T029": t029, "T030": t030, "T031": t031,
           "T032": t032, "T033": t033, "T034": t034, "T035": t035, "T036": t036, "T037": t037, "T038": t038, "T039": t039,
           "T040": t040, "T041": t041, "T042": t042}
