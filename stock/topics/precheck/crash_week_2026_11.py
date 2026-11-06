#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-11-06 — 최초. 이번 주 폭락(2026-11-05 나스닥 −5.5% · S&P 500 −4.4% / 11-06 코스피 −6.0%, 5,000 장중 붕괴)을 소재로 한
#          제목 후보의 숫자 확인 (사용자 지시 2026-11-06 "분석 코드 돌려서 이번주 성공사례 찾아서 분석 후 조회수가 잘 나올만할 제목 찾되
#          최근 상황에서 소재를 발견해서 지어야해 그리고 너가 그렇게 생각한 근거들도 말하고").
#
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.0 | 2026-11-06 | 최초 — A 급락일 뒤 보유 결과(+민감도) · B 커버드콜·배당 ETF 가 급락일에 같이 빠진 몫 · C 2억 '팔고 예금' vs '그대로' · D 이번 주 낙폭 · E 40% 넘게 빠진 뒤 원금 회복 해(댓글 '몇 년 기다리면 탈출?') | 전부 |
#
# 판정 규칙 (계산 전에 정함 — 채널 설명 3번 5 '오래 통하나'):
#   A. 지수 하루 변화 ≤ 기준(S&P 500 −4% · 나스닥 −5% · 코스피 −5%)인 날 = 급락일, 앞 급락일에서 60거래일 안이면 같은 사건.
#      그날 종가에서 1·3·5년(252·756·1260거래일) 뒤 종가가 더 높으면 '플러스'. 기준 −3/−4/−5% × 간격 20/60/120 으로 바꿔도
#      '5년 플러스 몫 > 1년 플러스 몫' 이 같은 쪽이면 정답형.
#   B. 기준 지수(QQQ·SPY, 조정 종가) 하루 ≤ −3% 인 날마다 (펀드 하루 변화 ÷ 기준 하루 변화) = 같이 빠진 몫. 중앙값 ≥ 0.7 → '급락을 거의 못 막음'.
#   C. S&P 500 급락일(A 와 같은 사건)에 2억: 그대로 5년 vs 그날 팔고 예금 연 3%(가정 — 실제 금리 아님) 5년. 가격 지수라 배당 빠짐(버틴 쪽에 불리).
# 미리 보기 점검: 급락일은 그날 종가로만 판정, 결과는 그 뒤 종가 — 판정에 미래 값을 쓰지 않음. 지수 자료라 종목 생존 편향 없음.
# 자료: Yahoo Finance chart API v8 일별 (close · adjclose) → precheck/data/week_2026-11-06/<SYM>.csv (있으면 그대로 — 다시 받지 않음).
# 실행: python3 -B stock/topics/precheck/crash_week_2026_11.py [--log-level DEBUG] [--selftest] → precheck/crash_week_2026-11-06.json
# ※ 연구·교육용 — 투자 권유가 아님. 과거 결과가 앞으로를 보장하지 않음.
import argparse
import csv
import json
import logging
import statistics as st
import time
import urllib.parse
import urllib.request
from datetime import date, datetime, timezone
from pathlib import Path

VERSION = "v1.0"
HERE = Path(__file__).resolve().parent
DATA = HERE / "data" / "week_2026-11-06"
OUT = HERE / "crash_week_2026-11-06.json"
H = {"1y": 252, "3y": 756, "5y": 1260}
GAP = 60
INDEX = {"GSPC": ("^GSPC", -0.04), "IXIC": ("^IXIC", -0.05), "KS11": ("^KS11", -0.05)}
FUNDS = {"QQQ": None, "SPY": None, "SCHD": "SPY", "JEPI": "SPY", "JEPQ": "QQQ", "QYLD": "QQQ", "TQQQ": None, "SOXL": None}
WEALTH, DEPOSIT = 200_000_000, 0.03

log = logging.getLogger("crash_week")


def L(stage, msg, *a, level=logging.INFO):
    log.log(level, f"[{stage}] [{datetime.now().isoformat(timespec='seconds')}] " + msg, *a)


def yahoo(sym):
    """일별 (date, adjclose) — 받은 CSV 가 있으면 그대로 (불필요한 다시 받기 없음)."""
    DATA.mkdir(parents=True, exist_ok=True)
    path = DATA / f"{sym.lstrip('^')}.csv"
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
                rows[datetime.fromtimestamp(t, tz=timezone.utc).date().isoformat()] = (c, a)   # 같은 날 두 번이면 마지막 값
        with path.open("w", encoding="utf-8", newline="") as f:
            f.write(f"# {sym} 일별 — Yahoo Finance chart API v8 (close · adjclose 배당·분할 반영), {date.today().isoformat()} 받음 · crash_week_2026_11.py {VERSION}\n")
            w = csv.writer(f)
            w.writerow(["date", "close", "adjclose"])
            w.writerows((d, c, a) for d, (c, a) in sorted(rows.items()))
        L("FETCH", "sym=%s rows=%d saved=%s", sym, len(rows), path.relative_to(HERE))
    with path.open(encoding="utf-8") as f:
        rows = [r for r in csv.reader(f) if r and not r[0].startswith("#")][1:]
    px = [(r[0], float(r[2])) for r in rows if r[2]]
    validate(sym, px)
    return px


def validate(sym, px):
    """빈 값·중복 날짜·순서·튀는 값 점검 — 이상은 경고로 남김 (멈추지 않음)."""
    ds = [d for d, _ in px]
    dup = len(ds) - len(set(ds))
    unordered = sum(1 for a, b in zip(ds, ds[1:]) if a >= b)
    nonpos = sum(1 for _, c in px if c <= 0)
    jumps = [(b[0], round(100 * (b[1] / a[1] - 1), 1)) for a, b in zip(px, px[1:]) if abs(b[1] / a[1] - 1) > 0.25]
    gaps = [(a[0], b[0]) for a, b in zip(px, px[1:]) if (date.fromisoformat(b[0]) - date.fromisoformat(a[0])).days > 10]
    L("VALIDATE", "sym=%s rows=%d from=%s to=%s dup=%d unordered=%d nonpositive=%d jumps>25%%=%d gaps>10d=%d",
      sym, len(px), ds[0], ds[-1], dup, unordered, nonpos, len(jumps), len(gaps))
    if dup or unordered or nonpos:
        L("VALIDATE", "sym=%s 자료 이상 — 결과를 쓰기 전에 CSV 확인", sym, level=logging.WARNING)
    for j in jumps[:5]:
        L("VALIDATE", "sym=%s big_move=%s %+.1f%% (레버리지 ETF 면 정상일 수 있음)", sym, *j, level=logging.WARNING)


def episodes(px, thr, gap=GAP):
    """급락일 (그날 종가로만 판정). 앞 급락일에서 gap 거래일 안이면 같은 사건으로 묶음."""
    ev, last = [], -10 ** 9
    for i in range(1, len(px)):
        r = px[i][1] / px[i - 1][1] - 1
        if r <= thr:
            if i - last > gap:
                ev.append((i, r))
            last = i
    return ev


def after(px, ev):
    out = {}
    for k, h in H.items():
        rs = [px[i + h][1] / px[i][1] - 1 for i, _ in ev if i + h < len(px)]
        dd = [min(c for _, c in px[i:i + h + 1]) / px[i][1] - 1 for i, _ in ev if i + h < len(px)]
        if rs:
            out[k] = {"n": len(rs), "plus": sum(r > 0 for r in rs), "plus_pct": round(100 * sum(r > 0 for r in rs) / len(rs), 1),
                      "median_pct": round(100 * st.median(rs), 1), "worst_pct": round(100 * min(rs), 1),
                      "median_more_drop_pct": round(100 * st.median(dd), 1), "worst_more_drop_pct": round(100 * min(dd), 1)}
    return out


def part_a(P):
    res = {}
    for name, (sym, thr) in INDEX.items():
        px = P[sym]
        ev = episodes(px, thr)
        days = [(px[i][0], round(100 * (px[i][1] / px[i - 1][1] - 1), 2)) for i in range(1, len(px)) if px[i][1] / px[i - 1][1] - 1 <= thr]
        a = after(px, ev)
        sens = {}
        for t in (-0.03, -0.04, -0.05):
            for g in (20, 60, 120):
                s = after(px, episodes(px, t, g))
                sens[f"thr{int(t * 100)}_gap{g}"] = {k: f"{v['plus']}/{v['n']}" for k, v in s.items()}
        same_side = all(int(v["5y"].split("/")[0]) / int(v["5y"].split("/")[1]) > int(v["1y"].split("/")[0]) / int(v["1y"].split("/")[1])
                        for v in sens.values() if "5y" in v and "1y" in v)
        y26 = [(d, c) for d, c in px if d.startswith("2026")]
        pk = max(y26, key=lambda x: x[1])
        res[name] = {"threshold_pct": thr * 100, "crash_days": len(days), "episodes": len(ev), "last_days": days[-6:], "after": a,
                     "sensitivity": sens, "judge_5y_beats_1y_all_settings": same_side,
                     "peak_2026": pk, "last": px[-1], "from_peak_pct": round(100 * (px[-1][1] / pk[1] - 1), 1),
                     "crash_days_2026": sum(1 for d, _ in days if d.startswith("2026"))}
        L("RESULT", "A index=%s thr=%.0f%% episodes=%d 1y=%s 5y=%s 5y>1y_all=%s from_2026_peak=%.1f%%", name, thr * 100, len(ev),
          f"{a['1y']['plus']}/{a['1y']['n']}", f"{a['5y']['plus']}/{a['5y']['n']}", same_side, res[name]["from_peak_pct"])
    return res


def part_b(P):
    res = {}
    for f, base in FUNDS.items():
        if not base:
            continue
        m, b = dict(P[f]), dict(P[base])
        ks = [k for k in sorted(m) if k in b]
        sh = []
        for x, y in zip(ks, ks[1:]):
            rb = b[y] / b[x] - 1
            if rb <= -0.03:
                sh.append(((m[y] / m[x] - 1) / rb, y))
        v = [s for s, _ in sh]
        res[f] = {"vs": base, "crash_days": len(v), "share_median": round(st.median(v), 2), "share_min": round(min(v), 2), "share_max": round(max(v), 2),
                  "judge": "급락을 거의 못 막음" if st.median(v) >= 0.7 else "덜 빠짐", "last": [(d, round(s, 2)) for s, d in sh[-3:]]}
        L("RESULT", "B fund=%s vs=%s crash_days=%d share_median=%.2f judge=%s", f, base, len(v), res[f]["share_median"], res[f]["judge"])
    return res


def part_c(P):
    px = P["^GSPC"]
    res = {}
    for yrs, h in ((1, 252), (5, 1260)):
        rows = []
        for i, _ in episodes(px, -0.04):
            if i + h < len(px):
                hold = WEALTH * px[i + h][1] / px[i][1]
                cash = WEALTH * (1 + DEPOSIT) ** yrs
                rows.append({"day": px[i][0], "hold_won": round(hold), "cash_won": round(cash), "diff_won": round(hold - cash)})
        d = [r["diff_won"] for r in rows]
        res[f"{yrs}y"] = {"n": len(rows), "hold_wins": sum(x > 0 for x in d), "median_diff_won": round(st.median(d)), "worst_diff_won": min(d),
                          "best_diff_won": max(d), "cases": rows}
        L("RESULT", "C years=%d n=%d hold_wins=%d median_diff=%+.0f만원 worst=%+.0f만원", yrs, len(rows), res[f'{yrs}y']['hold_wins'],
          res[f"{yrs}y"]["median_diff_won"] / 1e4, min(d) / 1e4)
    return res


def part_d(P):
    res = {}
    for f in ("SPY", "QQQ", "SCHD", "JEPQ", "TQQQ", "SOXL"):
        px = P[f]
        y26 = [(d, c) for d, c in px if d.startswith("2026")]
        pk = max(y26, key=lambda x: x[1])
        res[f] = {"last": px[-1][0], "day_pct": round(100 * (px[-1][1] / px[-2][1] - 1), 1), "peak": pk[0],
                  "from_peak_pct": round(100 * (px[-1][1] / pk[1] - 1), 1), "to_recover_pct": round(100 * (pk[1] / px[-1][1] - 1), 1)}
        L("RESULT", "D fund=%s day(%s)=%+.1f%% from_2026_peak(%s)=%+.1f%% to_recover=%+.1f%%", f, px[-1][0], res[f]["day_pct"], pk[0],
          res[f]["from_peak_pct"], res[f]["to_recover_pct"])
    return res


def part_e(P):
    """고점에서 40% 넘게 빠진 사건 — 처음 −40% 에 닿은 날부터 그 고점을 되찾기까지 해 (가격 지수, 배당 빠짐 — 실제 계좌보다 느림)."""
    res = {}
    for name, (sym, _) in INDEX.items():
        px = P[sym]
        pk_v, pk_d, hit, out = px[0][1], px[0][0], None, []
        for d, c in px:
            if c >= pk_v:
                if hit:
                    out.append({"peak": pk_d, "hit_minus40": hit, "recovered": d,
                                "years_from_hit": round((date.fromisoformat(d) - date.fromisoformat(hit)).days / 365.25, 1)})
                    hit = None
                pk_v, pk_d = c, d
            elif c / pk_v - 1 <= -0.40 and not hit:
                hit = d
        if hit:
            out.append({"peak": pk_d, "hit_minus40": hit, "recovered": None, "years_from_hit": None})
        res[name] = out
        L("RESULT", "E index=%s drawdowns>=40%%=%d years_from_hit=%s (자료 시작 %s — 그 전 고점은 모름)", name, len(out),
          [o["years_from_hit"] for o in out], px[0][0])
    return res


def selftest():
    """작은 가짜 자료로 급락일 묶기·보유 결과가 손 계산과 같은지."""
    px = [(f"d{i:04d}", 100.0) for i in range(10)]
    px[3] = ("d0003", 90.0)                    # −10% 급락
    px[4] = ("d0004", 85.0)                    # 다음 날 또 급락 → 같은 사건
    px += [(f"e{i:04d}", 120.0) for i in range(1300)]
    ev = episodes(px, -0.05, gap=60)
    assert [i for i, _ in ev] == [3], ev
    a = after(px, ev)
    assert a["1y"]["plus"] == 1 and a["5y"]["n"] == 1 and a["1y"]["median_more_drop_pct"] == round(100 * (85 / 90 - 1), 1), a
    L("SELFTEST", "ok episodes=%s after_1y=%s", ev, a["1y"])


def main(argv=None):
    ap = argparse.ArgumentParser(description="이번 주 폭락 소재 제목의 숫자 확인 (연구·교육용)")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    logging.basicConfig(level=a.log_level, format="%(message)s")
    if a.selftest:
        selftest()
        return
    t0 = time.time()
    syms = [s for s, _ in INDEX.values()] + list(FUNDS)
    L("START", "version=%s symbols=%s out=%s", VERSION, ",".join(syms), OUT.name)
    P = {s: yahoo(s) for s in syms}
    out = {"version": VERSION, "made": date.today().isoformat(), "note": "연구·교육용 — 투자 권유 아님. 지수는 가격 지수(배당 빠짐), ETF 는 조정 종가.",
           "A_after_crash_days": part_a(P), "B_fund_share_on_crash_days": part_b(P), "C_hold_vs_cash_200m": part_c(P), "D_this_week": part_d(P), "E_recovery_after_40pct": part_e(P)}
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1), "utf-8")
    L("END", "saved=%s seconds=%.1f", OUT.name, time.time() - t0)


if __name__ == "__main__":
    main()
