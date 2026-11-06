#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v2.1 — 2026-11-06 — 김씨 1억 되찾기 · 그대로 vs 60/40 잔고 · 3배 안정 수익 ⊂ 그대로. (v2.0 한 잣대 · v1.9 실제 TQQQ · v1.8 B9010 · v1.7 사연 숫자 · v1.6 코스피 달력 · v1.5 저장소 분류 기준·안정 수익 · v1.4 코스피 · v1.3 '지금' = 지금 고점 뒤 · v1.2 같음은 뒤집힘 아님 · v1.1 고점 = 최근 1년 최고가 · v1.0 최초) 폭락 대처 편 숫자 (사용자 지시 2026-11-06 "주식 시장 폭락 했는데 폭락 대처 방법 전달 주제로 해서 지금 상황과
#          가장 비슷한 폭락 사례, 대처 방향 + 전문가 조언 및 대처 사례 탐색해서 요약본 구성해봐").
#
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v2.1 | 2026-11-06 | 반론 검토 3회차: counts_D119_3y 에 kim_recover_1억 (3년 뒤 ×1.289 이상) · hold_end_beats_mix · lev3_stable_subset_of_hold · lev3_synthetic_hits · lev3_3y_end · lev3_check.qqq_x | main |
# | v2.0 | 2026-11-06 | 반론 검토 2회차: counts_D119_3y (3년 안 20% 넘게 준 적 · 안정 수익 · 3배가 3년 뒤 더 남은 횟수) · lev3_check (TQQQ 첫날~지금 가정 3배 vs 실제) · story.qqq_only_now | main |
# | v1.9 | 2026-11-06 | 반론 검토 1회차: 3배를 실제 TQQQ(조정 종가)로, 2010년 전은 빌리는 비용(국채 이자 × 2) 넣은 가정 계산 (v1.8 까지 빌리는 비용 빠짐 — '상') · from_peak_top5 (고점 날부터 대처별 가장 낮은 값 — '미리 나눠 담았다면') · dotcom_recover · 줄마다 lev3_real | paths · strategies · main |
# | v1.8 | 2026-11-06 | B9010 = 버핏 2013년 서한의 90(S&P 500)·10(단기 국채) — 대처 여섯째 · Q8 · 사연 '같은 날 9 대 1 이었다면' (사용자 지시 "…경력을 언급해야지 … 실질적인 대처 방법을 제목에 … 대본도 써봐") | paths · main |
# | v1.7 | 2026-11-06 | 사연 — 나스닥 고점 날 1억(QQQ 7천만 + TQQQ 3천만)이 지금 얼마인가 (전문가 중심 편 — 사용자 지시 "…사연 + 과거 사례 비교 + 전문가 + 문제…") | main |
# | v1.6 | 2026-11-06 | 코스피 직전 1년 상승 = 달력 365일 (지금 245거래일·과거 252거래일로 서로 다르게 세던 것) · 옛 고점 되찾은 해 = 달력 날수 | main |
# | v1.5 | 2026-11-06 | 분류를 저장소 기준(README 정답 미리 확인 3 — 가장 약한 칸 ≥55%·기본 칸 ≥60%)과 엄격 기준(한 번도 안 짐) 둘 다 · 대처마다 안정 수익 확률(채널 정답 기준) | main |
# | v1.4 | 2026-11-06 | 코스피 — 1년 최고가에서 처음 40% 넘게 빠진 사건과 그 뒤 · 2026-06-23 하루 −10% 다음 날 이후 | main |
# | v1.3 | 2026-11-06 | '지금' = 지금 고점 뒤 사건 (2026년 첫 사건 = 봄 하락을 잡던 버그) · 2026년 앞 사건도 비교 대상에 | main |
# | v1.2 | 2026-11-06 | 비교 결과를 이김·짐·같음으로 — 같음(예: 둘 다 min 1.0)은 뒤집힘이 아님 (논리 오류 고침, 판정 규칙 그대로) | judge · main |
# | v1.1 | 2026-11-06 | 고점 = 최근 1년 최고가 (역대 최고가로는 2008년 폭락이 빠졌음 — 판정 규칙은 그대로) · 사건 표에 그 뒤 결과 칸 | episodes · main |
# | v1.0 | 2026-11-06 | 최초 — 비슷한 폭락 찾기(similar) · 대처 다섯 가지 결과(strategies) · 민감도(sensitivity) · 코스피 큰 하락 날(kospi_days) · 자체 시험 | 전부 |
#
# ── 판정 규칙 (계산 전에 정함 — 채널 설명 3번 5 '오래 통하나', stock/topics/README.md '정답 미리 확인') ──
# 폭락 사건 = 나스닥 종합(^IXIC)이 최근 1년 최고가에서 처음 D 넘게 빠진 날 (D = 지금 낙폭, 2026-11-05 −11.9%). 새 고점을 찍어야 다음 사건. 2000-01-01 뒤 사건만.
# 닮음 = 그날의 네 값 — ① 고점에서 그날까지 거래일 ② 같은 날 S&P 500 낙폭 ③ 고점~그날 나스닥 하루 최대 낙폭 ④ 고점 전 1년 상승률 — 을 표준화한 거리.
#        한 값씩 빼고 다시 재도 1위가 같으면 '가장 비슷한 사례' 확정, 아니면 상위 묶음으로만 말함.
# 대처 다섯 (사건 날 종가에 정함 — 그날까지 알려진 값만, 미리 보기 없음):
#   HOLD 나스닥100(QQQ, 조정 종가) 그대로 · CASH 전부 팔고 예금(미국 13주 국채 이자 ^IRX, 전날 금리) ·
#   REBUY 팔았다가 QQQ 가 판 뒤 가장 낮은 값보다 20% 오른 첫날 다시 사기 · MIX 주식 60(SPY) + 채권 40(VBMFX) 으로 줄이고 달마다 비율 맞춤 ·
#   B9010 (v1.8) 버핏 9 대 1 — SPY 90 + 단기 국채 10, 달마다 비율 맞춤 ·
#   LEV3 나스닥100 3배 — v1.9: 실제 TQQQ(2010-02~) · 그 전은 가정 계산(QQQ 하루 수익 × 3 − 빌리는 비용 13주 국채 이자 × 2 − 연 0.95%)
# 잣대 (채널 목적 '덜 잃었나'): 그날 값 = 1 → 1년·3년 안 가장 낮은 값(더 빠진 폭) · 그날 값을 되찾은 날 · 3년 뒤 값 · 안정 수익(3년 뒤 예금보다 더 남고
#   한 번도 0.8 아래로 안 감 — precheck/risk.py stable 과 같음).
# 정답 분류: 모든 사건·모든 민감도 칸(D 10%·11.9%·15% × 1·3년)에서 같은 쪽 → 정답형 · 갈리면 조건부형(몇 번 중 몇 번으로만 말함).
# 자료: Yahoo Finance chart API v8 일별 (close·adjclose) → 이 폴더 *.csv (있으면 그대로 — 다시 받지 않음). 1999년 값은 2000년 사건의 ④ 상승률에만 씀.
# 실행: python3 -B stock/source/crash-plan-2026-11/calc/calc.py [--selftest] [--log-level DEBUG] → results.json
# ※ 연구·교육용 — 투자 권유가 아님. 과거 결과가 앞으로를 보장하지 않음.
import argparse
import csv
import json
import logging
import math
import statistics as st
import time
import urllib.parse
import urllib.request
from datetime import date, datetime, timezone
from pathlib import Path

VERSION = "v2.1"
HERE = Path(__file__).resolve().parent
OUT = HERE / "results.json"
SYMS = ["^IXIC", "^GSPC", "^KS11", "QQQ", "SPY", "VBMFX", "^IRX", "TQQQ"]   # v1.7: TQQQ = 사연(실제 3배 상품, 2010년부터)
START = "2000-01-01"
Y1, Y3 = 252, 756
LEV_FEE = 0.0095
log = logging.getLogger("crash_plan")


def L(stage, msg, *a, level=logging.INFO):
    log.log(level, f"[{stage}] [{datetime.now().isoformat(timespec='seconds')}] " + msg, *a)


# ── 자료 ──────────────────────────────────────────────────────────────────────
def fetch(sym):
    path = HERE / f"{sym.lstrip('^')}.csv"
    if not path.exists():
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(sym)}?period1=0&period2={int(time.time())}&interval=1d"
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=60) as r:
                res = json.load(r)["chart"]["result"][0]
        except Exception as e:  # noqa: BLE001
            L("FETCH", "sym=%s error=%s next=네트워크·프록시 확인(/root/.ccr/README.md) 뒤 다시 실행", sym, e, level=logging.ERROR)
            raise
        q = res["indicators"]["quote"][0]["close"]
        adj = (res["indicators"].get("adjclose") or [{}])[0].get("adjclose") or q
        rows = {}
        for t, c, a in zip(res["timestamp"], q, adj):
            if c is not None and a is not None:
                rows[datetime.fromtimestamp(t, tz=timezone.utc).date().isoformat()] = (c, a)
        with path.open("w", encoding="utf-8", newline="") as f:
            f.write(f"# {sym} 일별 — Yahoo Finance chart API v8 (close · adjclose 배당·분할 반영), {date.today().isoformat()} 받음 · calc.py {VERSION}\n")
            w = csv.writer(f)
            w.writerow(["date", "close", "adjclose"])
            w.writerows((d, c, a) for d, (c, a) in sorted(rows.items()))
        L("FETCH", "sym=%s rows=%d saved=%s", sym, len(rows), path.name)
    with path.open(encoding="utf-8") as f:
        rows = [r for r in csv.reader(f) if r and not r[0].startswith("#")][1:]
    col = 1 if sym.startswith("^") else 2                 # 지수 = 종가(가격) · 펀드 = 조정 종가(분배금 포함)
    px = {r[0]: float(r[col]) for r in rows if r[col]}
    validate(sym, px)
    return px


def validate(sym, px):
    ds = sorted(px)
    nonpos = sum(1 for d in ds if px[d] <= 0)
    gaps = sum(1 for a, b in zip(ds, ds[1:]) if (date.fromisoformat(b) - date.fromisoformat(a)).days > 10)
    jumps = [(b, round(100 * (px[b] / px[a] - 1), 1)) for a, b in zip(ds, ds[1:]) if px[a] > 0 and abs(px[b] / px[a] - 1) > 0.20]
    L("VALIDATE", "sym=%s rows=%d from=%s to=%s nonpositive=%d gaps>10d=%d jumps>20%%=%d", sym, len(ds), ds[0], ds[-1], nonpos, gaps, len(jumps))
    if nonpos and sym != "^IRX":
        L("VALIDATE", "sym=%s 0 이하 값 %d개 — CSV 확인", sym, nonpos, level=logging.WARNING)
    for j in jumps[:3]:
        L("VALIDATE", "sym=%s big_move=%s %+.1f%%", sym, *j, level=logging.WARNING)


def ffill(days, px):
    """거래일 달력(days)에 맞춰 앞 값으로 채움 — 그날 없는 값은 그 전 값 (미래 값 안 씀)."""
    out, last, ks, j = [], None, sorted(px), 0
    for d in days:
        while j < len(ks) and ks[j] <= d:
            last = px[ks[j]]; j += 1
        out.append(last)
    return out


# ── 폭락 사건 ─────────────────────────────────────────────────────────────────
def episodes(days, ix, sp, D, win=Y1):
    """나스닥이 고점(최근 1년 최고가)에서 처음 D 넘게 빠진 날 — 다시 1년 최고가를 찍어야 다음 사건.
    v1.1: 고점 = 역대 최고가였을 때는 나스닥이 2000년 고점을 2015년에야 되찾아 2008년 폭락이 사건에서 빠졌음 → 최근 1년 최고가 (결과를 보기 전 정의 고침)."""
    armed, ev = True, []
    for i in range(1, len(days)):
        lo = max(0, i - win)
        pk_i = max(range(lo, i + 1), key=lambda k: ix[k])
        if pk_i == i:                                   # 1년 최고가를 새로 찍음 → 다음 사건을 셀 수 있음
            armed = True
            continue
        if armed and ix[i] / ix[pk_i] - 1 <= -D:
            armed = False
            if days[i] < START:
                continue
            worst = min(ix[k] / ix[k - 1] - 1 for k in range(pk_i + 1, i + 1))
            run = ix[pk_i] / ix[max(pk_i - Y1, 0)] - 1
            sp_pk = max(sp[lo:i + 1])
            ev.append({"hit": days[i], "i": i, "peak": days[pk_i], "days_from_peak": i - pk_i, "ix_dd": ix[i] / ix[pk_i] - 1,
                       "sp_dd": sp[i] / sp_pk - 1, "worst_day": worst, "runup_1y": run})
    return ev


FEATS = ("days_from_peak", "sp_dd", "worst_day", "runup_1y")


def similar(ev, now, feats=FEATS):
    pool = ev + [now]
    z = {}
    for f in feats:
        xs = [e[f] for e in pool]
        m, s = st.mean(xs), st.pstdev(xs) or 1.0
        z[f] = (m, s)
    def dist(e):
        return math.sqrt(sum(((e[f] - z[f][0]) / z[f][1] - (now[f] - z[f][0]) / z[f][1]) ** 2 for f in feats))
    return sorted(((round(dist(e), 3), e["hit"]) for e in ev))


# ── 대처 다섯 ─────────────────────────────────────────────────────────────────
def paths(i0, H, qqq, spy, bnd, irx, days, tqqq=None):
    n = min(H, len(days) - 1 - i0)
    cash = [1.0]
    for k in range(i0 + 1, i0 + n + 1):
        r = (irx[k - 1] or 0) / 100.0
        cash.append(cash[-1] * (1 + r) ** (1 / 252))
    hold = [qqq[k] / qqq[i0] for k in range(i0, i0 + n + 1)]
    # v1.9: 3배 = 실제 TQQQ(조정 종가)가 그날 있으면 그것 · 없으면(2010-02 전) 가정 계산 — 하루 수익 × 3 − 빌리는 비용(13주 국채 이자 × 2) − 연 0.95%
    #       (v1.8 까지는 빌리는 비용을 빼지 않아 실제보다 좋게 나왔음 — 반론 검토 1회차 '상')
    lev = [1.0]
    real = tqqq is not None and tqqq[i0] is not None
    for k in range(i0 + 1, i0 + n + 1):
        if real and tqqq[k] is not None:
            lev.append(lev[-1] * tqqq[k] / tqqq[k - 1])
        else:
            fin = 2 * (irx[k - 1] or 0) / 100.0 / 252
            lev.append(max(lev[-1] * (1 + 3 * (qqq[k] / qqq[k - 1] - 1) - fin - LEV_FEE / 252), 0.0))
    reb, inq, lo, units = [1.0], False, qqq[i0], 0.0
    cval = 1.0
    for k in range(i0 + 1, i0 + n + 1):
        if not inq:
            cval *= cash[k - i0] / cash[k - i0 - 1]
            lo = min(lo, qqq[k])
            if qqq[k] >= lo * 1.2:                      # 그날 종가에 산다 (그날까지 본 가장 낮은 값 기준)
                inq, units = True, cval / qqq[k]
            reb.append(cval)
        else:
            reb.append(units * qqq[k])
    mix, s_u, b_u = [1.0], 0.6 / spy[i0], 0.4 / bnd[i0]
    for k in range(i0 + 1, i0 + n + 1):
        v = s_u * spy[k] + b_u * bnd[k]
        if days[k][:7] != days[k - 1][:7]:              # 달이 바뀐 첫 거래일에 60·40 으로
            s_u, b_u = 0.6 * v / spy[k], 0.4 * v / bnd[k]
        mix.append(v)
    # v1.8: B9010 = 버핏 2013년 주주 서한 '90%는 아주 싼 S&P 500 인덱스 펀드, 10%는 단기 국채' — SPY 90 + 단기 국채(13주 국채 이자 = CASH 길) 10, 달마다 비율 맞춤
    b9, su, cu = [1.0], 0.9 / spy[i0], 0.1 / cash[0]
    for k in range(i0 + 1, i0 + n + 1):
        v = su * spy[k] + cu * cash[k - i0]
        if days[k][:7] != days[k - 1][:7]:
            su, cu = 0.9 * v / spy[k], 0.1 * v / cash[k - i0]
        b9.append(v)
    return {"HOLD": hold, "CASH": cash, "REBUY": reb, "MIX": mix, "LEV3": lev, "B9010": b9}


def measure(p, cash, horizon):
    v = p[:horizon + 1]
    mn = min(v)
    imn = v.index(mn)
    rec = next((k for k in range(imn, len(v)) if v[k] >= 1.0), None) if mn < 1.0 else 0
    return {"end": round(v[-1], 3), "min": round(mn, 3), "recover_days": rec, "below80": mn < 0.8,
            "stable": bool(v[-1] > cash[min(horizon, len(cash) - 1)] and mn >= 0.8), "full": len(v) - 1 == horizon}


def strategies(ev, days, S):
    out = []
    for e in ev:
        i0 = e["i"]
        P = paths(i0, Y3, S["QQQ"], S["SPY"], S["VBMFX"], S["^IRX"], days, S.get("TQQQ"))
        row = {"hit": e["hit"], "lev3_real": S.get("TQQQ") is not None and S["TQQQ"][i0] is not None}
        for h, name in ((Y1, "1y"), (Y3, "3y")):
            row[name] = {k: measure(v, P["CASH"], h) for k, v in P.items() if len(v) - 1 >= min(h, len(v) - 1)}
        out.append(row)
    return out


def judge(rows, horizon, key, sign, a, b):
    """v1.2: a·b 의 key 값 비교 → (이김, 짐, 같음, 사건 수). sign=+1 이면 a 가 클 때 이김, −1 이면 작을 때.
    같음 = 둘 다 같은 값 (예: 사건 뒤 바로 올라 둘 다 한 번도 시작값 아래로 안 감 — min 1.0) — 뒤집힘으로 세지 않음."""
    full = [r for r in rows if r[horizon]["HOLD"]["full"]]
    w = l = t = 0
    for r in full:
        x, y = r[horizon][a][key], r[horizon][b][key]
        if x == y:
            t += 1
        elif (x - y) * sign > 0:
            w += 1
        else:
            l += 1
    return w, l, t, len(full)


QUESTIONS = {                                  # (잣대, 방향, a, b) — a 가 b 보다 (방향) 인가
    "Q3_hold_beats_cash_end": ("end", +1, "HOLD", "CASH"),
    "Q4_lev3_deeper_than_hold": ("min", -1, "LEV3", "HOLD"),
    "Q5_mix_shallower_than_hold": ("min", +1, "MIX", "HOLD"),
    "Q6_hold_beats_rebuy_end": ("end", +1, "HOLD", "REBUY"),
    "Q7_mix_beats_cash_end": ("end", +1, "MIX", "CASH"),
    "Q8_b9010_shallower_than_hold": ("min", +1, "B9010", "HOLD"),      # v1.8
}


def kospi_days(days_k, k, thr=-0.08):
    out = []
    for i in range(1, len(days_k)):
        r = k[i] / k[i - 1] - 1
        if r <= thr and days_k[i] >= START:
            nxt = k[i + 1] / k[i] - 1 if i + 1 < len(k) else None
            m1 = min(k[i:i + 22]) / k[i] - 1
            y1 = k[i + Y1] / k[i] - 1 if i + Y1 < len(k) else None
            out.append({"day": days_k[i], "drop": round(100 * r, 2), "next_day": nxt and round(100 * nxt, 2),
                        "more_drop_1m": round(100 * m1, 1), "after_1y": y1 if y1 is None else round(100 * y1, 1)})
    return out


def selftest():
    days = [f"2001-01-{i:02d}" for i in range(1, 30)]
    ix = [100, 110, 105, 96, 95, 120, 100, 90] + [90] * 21
    sp = [100] * 29
    ev = episodes(days, ix, sp, 0.12)
    assert [e["hit"] for e in ev] == ["2001-01-04", "2001-01-07"], ev       # 96/110 = −12.7% · 새 고점 120 뒤 100/120 = −16.7%
    assert abs(ev[0]["worst_day"] - (96 / 105 - 1)) < 1e-9
    q = [1.0, 0.9, 0.8, 0.96, 1.2]
    P = paths(0, 4, q, [1] * 5, [1] * 5, [0.0] * 5, ["2001-01-01", "2001-01-02", "2001-01-03", "2001-01-04", "2001-02-01"])
    assert P["REBUY"][3] == 1.0 and abs(P["REBUY"][4] - 1.0 * 1.2 / 0.96) < 1e-9, P["REBUY"]      # 0.8×1.2=0.96 에 다시 삼
    assert abs(P["LEV3"][1] - (1 - 0.3 - LEV_FEE / 252)) < 1e-9
    m = measure(q, [1] * 5, 4)
    assert m["min"] == 0.8 and m["recover_days"] == 4 and m["below80"] is False
    L("SELFTEST", "ok episodes=%s rebuy=%s lev=%s", [e["hit"] for e in ev], [round(x, 3) for x in P["REBUY"]], round(P["LEV3"][1], 4))


def main(argv=None):
    ap = argparse.ArgumentParser(description="폭락 대처 편 계산 (연구·교육용)")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args(argv)
    logging.basicConfig(level=a.log_level, format="%(message)s")
    if a.selftest:
        selftest(); return
    t0 = time.time()
    L("START", "version=%s symbols=%s", VERSION, ",".join(SYMS))
    raw = {s: fetch(s) for s in SYMS}
    days = sorted(d for d in raw["^IXIC"] if d >= "1998-01-01")
    S = {s: ffill(days, raw[s]) for s in SYMS if s != "^KS11"}
    ix, sp = S["^IXIC"], S["^GSPC"]
    pk = max(range(len(days)), key=lambda i: ix[i] if days[i] >= "2026-01-01" else -1)
    D_now = -(ix[-1] / ix[pk] - 1)
    L("DATA", "calendar=%s~%s days=%d nasdaq_peak=%s now=%s drawdown=%.1f%%", days[0], days[-1], len(days), days[pk], days[-1], -100 * D_now)
    res = {"version": VERSION, "made": date.today().isoformat(), "note": "연구·교육용 — 투자 권유 아님. 지수는 가격, 펀드는 조정 종가. LEV3 는 가정 계산.",
           "now": {"day": days[-1], "nasdaq_peak": days[pk], "nasdaq_dd_pct": round(-100 * D_now, 1)}}
    sens = {}
    for D in (0.10, round(D_now, 3), 0.15):
        ev_all = episodes(days, ix, sp, D)
        # v1.3: '지금' = 지금 고점(days[pk]) 뒤의 사건 — 예전엔 2026년 첫 사건(봄 하락)을 잡았음
        now = next((e for e in ev_all if e["peak"] >= days[pk]), None)
        ev = [e for e in ev_all if e["hit"] < days[pk]]
        if now is None:                                     # 지금 낙폭보다 큰 기준(15%)이면 '지금'은 사건이 아님 — 그 칸은 결과 비교만
            now = {"hit": days[-1], "days_from_peak": len(days) - 1 - pk, "sp_dd": sp[-1] / max(sp[pk - 300:]) - 1,
                   "worst_day": min(ix[k] / ix[k - 1] - 1 for k in range(pk + 1, len(days))), "runup_1y": ix[pk] / ix[pk - Y1] - 1}
        rank = similar(ev, now)
        drop1 = {f: similar(ev, now, tuple(x for x in FEATS if x != f))[0][1] for f in FEATS}
        rows = strategies(ev, days, S)
        qs = {}
        for q, (key, sign, x, y) in QUESTIONS.items():
            for h in ("1y", "3y"):
                qs[f"{q}_{h}"] = judge(rows, h, key, sign, x, y)
        top = [h for _, h in rank[:5]]
        sens[f"D{int(round(D * 1000))}"] = {"D_pct": round(100 * D, 1), "episodes": len(ev), "now_features": {f: round(now[f], 4) for f in FEATS},
                                           "rank": rank[:8], "top1_drop_one_feature": drop1, "top1_stable": len(set(drop1.values()) | {rank[0][1]}) == 1,
                                           "questions": qs, "rows": rows, "events": [{k: (round(v, 4) if isinstance(v, float) else v) for k, v in e.items() if k != "i"} for e in ev],
                                           "top5_more_drop20_1y": sum(1 for r in rows if r["hit"] in top and r["1y"]["HOLD"]["below80"])}
        L("CALC", "D=%.1f%% episodes=%d top5=%s top1_stable=%s", 100 * D, len(ev), top, sens[f"D{int(round(D * 1000))}"]["top1_stable"])
        for q, v in qs.items():
            L("RESULT", "D=%.1f%% %s win=%d lose=%d tie=%d n=%d", 100 * D, q, *v)
    # 분류: 질문마다 모든 칸에서 진 사건이 0 (또는 이긴 사건이 0) 인가 — 같음은 뒤집힘이 아님 (v1.2)
    cls = {}
    for q in QUESTIONS:
        cells = [s["questions"][f"{q}_{h}"] for s in sens.values() for h in ("1y", "3y")]
        never_lose = all(l == 0 and w > 0 for w, l, t, n in cells if n)
        never_win = all(w == 0 and l > 0 for w, l, t, n in cells if n)
        # v1.5: 저장소 기준 (stock/topics/README.md '정답 미리 확인' 3) — 모든 칸에서 이긴 쪽이 같고 가장 약한 칸 ≥ 55% · 기본 칸(D 지금·3년) ≥ 60%
        shares = [w / n for w, l, t, n in cells if n]
        base = sens[f"D{int(round(D_now * 1000))}"]["questions"][f"{q}_3y"]
        repo = "정답형" if (min(shares) >= 0.55 and base[0] / base[3] >= 0.60) else ("조건부형" if max(shares) > 0.5 > min(shares) else "차이 작음")
        cls[q] = {"cells": cells, "class_strict": "정답형" if (never_lose or never_win) else "조건부형", "class_repo": repo,
                  "weakest_share": round(min(shares), 3), "base_share": round(base[0] / base[3], 3)}
        L("JUDGE", "%s cells(win,lose,tie,n)=%s strict=%s repo=%s weakest=%.0f%% base=%.0f%%", q, cells, cls[q]["class_strict"], repo,
          100 * min(shares), 100 * base[0] / base[3])
    # v1.5: 안정 수익 확률 (채널 정답 기준 — 3년 뒤 예금보다 더 남고 한 번도 0.8 아래로 안 감) · 대처마다 · 칸마다
    stab = {}
    for key, s in sens.items():
        full = [r for r in s["rows"] if r["3y"]["HOLD"]["full"]]
        stab[key] = {k: f"{sum(r['3y'][k]['stable'] for r in full)}/{len(full)}" for k in ("HOLD", "MIX", "LEV3", "REBUY", "CASH", "B9010")}
        stab[key]["median_min"] = {k: round(st.median(r["3y"][k]["min"] for r in full), 3) for k in ("HOLD", "MIX", "LEV3", "REBUY", "B9010")}
        stab[key]["worst_min"] = {k: min(r["3y"][k]["min"] for r in full) for k in ("HOLD", "MIX", "LEV3", "REBUY", "B9010")}
        L("RESULT", "stable_3y %s %s median_min=%s worst_min=%s", key, {k: v for k, v in stab[key].items() if isinstance(v, str)},
          stab[key]["median_min"], stab[key]["worst_min"])
    res["sensitivity"] = sens
    res["classes"] = cls
    res["stable_3y"] = stab
    # v2.0: 한 잣대로 세기 (반론 검토 2회차) — 기본 칸(D 지금 · 3년 결과가 있는 사건)
    full = [r for r in sens[f"D{int(round(D_now * 1000))}"]["rows"] if r["3y"]["HOLD"]["full"]]
    res["counts_D119_3y"] = {
        "n": len(full),
        "below80": {k: sum(r["3y"][k]["below80"] for r in full) for k in ("HOLD", "MIX", "LEV3", "B9010", "CASH")},
        "stable": {k: sum(r["3y"][k]["stable"] for r in full) for k in ("HOLD", "MIX", "LEV3", "B9010", "CASH")},
        "lev3_end_beats_hold": sum(r["3y"]["LEV3"]["end"] > r["3y"]["HOLD"]["end"] for r in full),
        "lev3_end_beats_hold_hits": [r["hit"] for r in full if r["3y"]["LEV3"]["end"] > r["3y"]["HOLD"]["end"]],
        "hits": [r["hit"] for r in full]}
    # v2.1 (반론 검토 3회차): 김씨 1억 되찾기 — 폭락 날 계좌가 7,759/10,000 이라 3년 뒤 ×(10,000/7,759) 이상이면 1억 회복
    need = 10_000 / 7_759
    c = res["counts_D119_3y"]
    c["kim_need_x"] = round(need, 4)
    c["kim_recover_1억"] = {k: sum(r["3y"][k]["end"] >= need for r in full) for k in ("HOLD", "CASH", "LEV3", "MIX", "B9010")}
    c["hold_end_beats_mix"] = sum(r["3y"]["HOLD"]["end"] > r["3y"]["MIX"]["end"] for r in full)
    st_hold = {r["hit"] for r in full if r["3y"]["HOLD"]["stable"]}
    st_lev = {r["hit"] for r in full if r["3y"]["LEV3"]["stable"]}
    c["lev3_stable_subset_of_hold"] = st_lev <= st_hold
    c["lev3_synthetic_hits"] = [r["hit"] for r in full if not r["lev3_real"]]
    c["lev3_3y_end"] = {r["hit"]: r["3y"]["LEV3"]["end"] for r in full if r["hit"] in ("2000-04-03", "2008-01-04")}
    L("RESULT", "counts_D119_3y=%s", res["counts_D119_3y"])
    # v2.0: 가정 3배 vs 실제 TQQQ — 겹치는 기간(TQQQ 첫날 ~ 지금) 누적 값 비교 (가정 계산 오차)
    t3 = S["TQQQ"]; i_t = next(i for i in range(len(days)) if t3[i] is not None)
    syn = paths(i_t, len(days) - 1 - i_t, S["QQQ"], S["SPY"], S["VBMFX"], S["^IRX"], days, None)["LEV3"]
    real = [t3[k] / t3[i_t] for k in range(i_t, len(days))]
    yrs = (date.fromisoformat(days[-1]) - date.fromisoformat(days[i_t])).days / 365.25
    res["lev3_check"] = {"from": days[i_t], "to": days[-1], "synthetic_x": round(syn[-1], 2), "real_x": round(real[-1], 2),
                         "cagr_gap_pct": round(100 * ((syn[-1]) ** (1 / yrs) - (real[-1]) ** (1 / yrs)), 2),
                         "max_dd_synth": round(min(v / max(syn[:k + 1]) for k, v in enumerate(syn)) - 1, 3),
                         "max_dd_real": round(min(v / max(real[:k + 1]) for k, v in enumerate(real)) - 1, 3)}
    qv = S["QQQ"]; res["lev3_check"]["qqq_x"] = round(qv[-1] / qv[i_t], 2)          # v2.1: 같은 기간 나스닥100(QQQ) 배수
    L("RESULT", "lev3_check=%s", res["lev3_check"])
    kd = sorted(raw["^KS11"]); kv = [raw["^KS11"][d] for d in kd]
    res["kospi_8pct_days"] = kospi_days(kd, kv)
    kp = max((i for i in range(len(kd)) if kd[i] >= "2026-01-01"), key=lambda i: kv[i])
    def cal_runup(pi):
        """v1.6: 고점 날 종가 ÷ 달력 1년(365일) 전 그날 또는 그 전 마지막 종가 − 1 (지금·과거 사건을 같은 방법으로)."""
        d0 = (date.fromisoformat(kd[pi]).replace(year=date.fromisoformat(kd[pi]).year - 1)).isoformat()
        j = max(k for k in range(pi + 1) if kd[k] <= d0) if kd[0] <= d0 else 0
        return round(100 * (kv[pi] / kv[j] - 1), 1)
    res["kospi_now"] = {"peak": kd[kp], "peak_close": kv[kp], "now": kd[-1], "close": kv[-1], "dd_pct": round(100 * (kv[-1] / kv[kp] - 1), 1),
                        "runup_1y_to_peak_pct": cal_runup(kp)}
    # v1.4: 코스피 — 1년 최고가에서 처음 40% 넘게 빠진 사건 (지금 −44.5%) · 그 뒤 (가격 지수)
    kev = []
    for e in episodes(kd, kv, kv, 0.40):
        i = e["i"]
        fut = kv[i:]
        pi = kd.index(e["peak"])
        rec = next((j for j in range(len(fut)) if fut[j] >= kv[pi]), None)
        kev.append({"hit": e["hit"], "peak": e["peak"], "days_from_peak": e["days_from_peak"], "runup_1y_pct": cal_runup(pi),
                    "more_drop_pct": round(100 * (min(fut[:Y3 + 1]) / kv[i] - 1), 1),
                    "after_1y_pct": round(100 * (kv[i + Y1] / kv[i] - 1), 1) if i + Y1 < len(kv) else None,
                    "after_3y_pct": round(100 * (kv[i + Y3] / kv[i] - 1), 1) if i + Y3 < len(kv) else None,
                    "peak_again": kd[i + rec] if rec is not None else None,
                    "years_to_peak_again": round((date.fromisoformat(kd[i + rec]) - date.fromisoformat(e["hit"])).days / 365.25, 1) if rec is not None else None})
    res["kospi_40pct_events"] = kev
    j23 = kd.index("2026-06-23")
    res["kospi_2026_06_23"] = {"close": kv[j23], "next_day_pct": round(100 * (kv[j23 + 1] / kv[j23] - 1), 2),
                               "min_after": round(min(kv[j23:]), 2), "min_after_pct": round(100 * (min(kv[j23:]) / kv[j23] - 1), 1),
                               "now_vs_pct": round(100 * (kv[-1] / kv[j23] - 1), 1)}
    L("RESULT", "kospi_40pct_events=%s", [(k["hit"], k["runup_1y_pct"], k["more_drop_pct"], k["years_to_peak_again"]) for k in kev])
    L("RESULT", "kospi_2026_06_23=%s", res["kospi_2026_06_23"])
    L("RESULT", "kospi_now=%s kospi_8pct_days=%d", res["kospi_now"], len(res["kospi_8pct_days"]))
    # v1.9: '미리 나눠 담았다면' = 고점 날부터 (폭락 날이 아니라) — 닮은 다섯 번(D119 상위 5) · 1년·3년 안 가장 낮은 값
    top5 = [h for _, h in sens["D119"]["rank"][:5]]
    evd = {e["hit"]: e for e in episodes(days, ix, sp, round(D_now, 3))}
    fp = {}
    for h in top5:
        pi = days.index(evd[h]["peak"])
        P = paths(pi, Y3, S["QQQ"], S["SPY"], S["VBMFX"], S["^IRX"], days, S.get("TQQQ"))
        fp[h] = {"peak": days[pi], "1y": {k: round(min(v[:Y1 + 1]), 3) for k, v in P.items()}, "3y": {k: round(min(v), 3) for k, v in P.items()}}
        L("RESULT", "from_peak hit=%s peak=%s 1y_min=%s", h, days[pi], fp[h]["1y"])
    res["from_peak_top5"] = fp
    # v1.9: 닷컴 — 2000-04-03(사건 날) 나스닥100(QQQ 배당 포함) 값을 되찾은 날
    q = S["QQQ"]; i00 = days.index("2000-04-03")
    tr = min(range(i00, min(i00 + Y3, len(days) - 1) + 1), key=lambda k: q[k])          # 3년 안 바닥 — 그 뒤 처음 되찾은 날 (며칠 뒤 잠깐 반등한 날 ✗)
    back = next((days[k] for k in range(tr + 1, len(days)) if q[k] >= q[i00]), None)
    res["dotcom_recover"] = {"from": "2000-04-03", "back": back, "years": round((date.fromisoformat(back) - date.fromisoformat("2000-04-03")).days / 365.25, 1) if back else None}
    L("RESULT", "dotcom_recover=%s", res["dotcom_recover"])
    # v1.7: 사연 — 가상 인물 김씨: 나스닥 고점 날(10-06) 1억 = 나스닥100 ETF(QQQ) 7천만 원 + 3배 레버리지(TQQQ) 3천만 원 → 지금(조정 종가)
    q, t3 = raw["QQQ"], raw["TQQQ"]
    d0, d1 = days[pk], days[-1]
    qv, tv = 7_000 * q[d1] / q[d0], 3_000 * t3[d1] / t3[d0]          # 만 원
    res["story"] = {"start": d0, "end": d1, "qqq_in": 7000, "tqqq_in": 3000, "qqq_now": round(qv), "tqqq_now": round(tv), "total_now": round(qv + tv),
                    "loss_total": round(10_000 - qv - tv), "loss_qqq": round(7000 - qv), "loss_tqqq": round(3000 - tv),
                    "tqqq_share_of_loss_pct": round(100 * (3000 - tv) / (10_000 - qv - tv), 1),
                    "day_qqq_pct": round(100 * (q[d1] / q[days[-2]] - 1), 1), "day_tqqq_pct": round(100 * (t3[d1] / t3[days[-2]] - 1), 1),
                    "unit": "만 원", "note": "가상 인물 · 실제 ETF 조정 종가 · 세금·수수료·환율 빼고"}
    sp = raw["SPY"]
    irx_d0 = raw["^IRX"].get(d0) or 0.0
    b9_now = 10_000 * (0.9 * sp[d1] / sp[d0] + 0.1 * (1 + irx_d0 / 100) ** (21 / 252))      # 한 달(약 21거래일) 국채 이자 — 달 안이라 비율 맞춤 없음
    res["story"]["b9010_now"] = round(b9_now)
    res["story"]["qqq_only_now"] = round(10_000 * q[d1] / q[d0])          # v2.0: 3배 없이 1억 모두 나스닥100이었다면
    res["story"]["b9010_note"] = "같은 날 1억을 S&P 500(SPY) 90 + 단기 국채 10 으로 넣었다면 (국채 = 그날 13주 국채 이자로 21거래일)"
    L("RESULT", "story=%s", res["story"])
    OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1), "utf-8")
    L("END", "saved=%s seconds=%.1f", OUT.name, time.time() - t0)


if __name__ == "__main__":
    main()
