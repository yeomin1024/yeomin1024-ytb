#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.2 — 2026-11-13 — B24 작년 1등 업종 따라가기 vs S&P 500 · B25 겹친 분산(기술 ETF 셋) vs S&P 500 더함.
# (v1.1) — 2026-11-13 — B26 예금만(지수가 예금을 이긴 몫 4·10년) · B28 손실 난 해 뒤 그만두기 vs 보유 더함.
# (v1.0) — 2026-11-13 — 주제 기획안 묶음 2026-11-13(B21~B30) 정답 미리 확인 — 사용자 지시 "예전 만들어 놓았던건 다 삭제해 니가 새로 만들어야지
#          지시사항대로 하면 돼잖아" → "판정 기록은 남기고 시작해" (stock/guides/board_1_topic.md 3번: 정답이 기간·가정에 따라 뒤집힐 것 같으면 미리 확인, 뒤집히면 뺌).
#
# 정답 기준 = risk.py 와 같은 '안정 수익' (한 구간): ① 끝에 예금(미국 13주 국채 이자, longform_items CASH)보다 더 남고 ② 그사이 원금보다 20% 넘게 줄지 않음.
# 칸 = 보유 기간(2·4년) × 시작 시기(상품이 나온 날~2008 / 2009~). 비교 = 그 선택의 확률 − S&P 500(SPY) 확률 (%p).
#   B21 레버리지(QLD 2배) · B24 한 업종(섹터 ETF 11개 + 반도체 지수 ^SOX) · B27 커버드콜(QYLD·XYLD·JEPI·JEPQ)
#   B30 목돈 한 번에 vs 12달 나눠 넣기(SPY · 아직 안 넣은 돈은 예금) · B22 '5% 오르면 팔고 3% 빠지면 다시 사기' vs 보유(SPY)
# 시작일은 20거래일마다 하나 (겹치는 구간 — 몫으로만 봄). 숫자는 기획안 단계 확인용 — 대본 숫자는 편마다 새 계산 파일(quick_board 규칙 16).
# ※ 연구·교육용 — 투자 권유가 아님.
#
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.0 | 2026-11-13 | 최초 | stable_share · check_* · main |
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
END = "2026-10-27"
STEP = 20
LOSS = 0.20
LOG = logging.getLogger("board_2026-11-13")          # longform_items 의 basicConfig(stage 칸) 와 따로 — 자기 handler
LOG.propagate = False
_h = logging.StreamHandler(sys.stdout)
_h.setFormatter(logging.Formatter("%(message)s"))
LOG.addHandler(_h)
LOG.setLevel(logging.INFO)


def log(tag, /, **kv):
    LOG.info(f"[{tag}] [{date.today()}] " + " ".join(f"{k}={v}" for k, v in kv.items()))


def add_y(d, y):
    return f"{int(d[:4]) + y}{d[4:]}"


def path(s, a, b):
    """a~b 의 값(처음 = 1) 배열."""
    i, j = bisect.bisect_left(s.k, a), bisect.bisect_right(s.k, b) - 1
    v = np.asarray(s.v[i:j + 1], float)
    return v / v[0]


def stable(v, cash_end):
    return bool(v[-1] > cash_end and v.min() >= 1 - LOSS)


def starts(s, frm, to, years):
    out = []
    for n, d in enumerate(s.k):
        if n % STEP or d < frm or d > to or add_y(d, years) > END:
            continue
        out.append(d)
    return out


def share(fn, ds):
    r = [fn(d) for d in ds]
    r = [x for x in r if x is not None]
    return (round(float(np.mean(r)), 4) if r else None), len(r)


def cell(name, s, C, years, frm, to, SPY):
    ds = starts(s, max(frm, s.k[0]), to, years)
    a, n = share(lambda d: stable(path(s, d, add_y(d, years)), 1 + C.chg(d, add_y(d, years))), ds)
    b, _ = share(lambda d: stable(path(SPY, d, add_y(d, years)), 1 + C.chg(d, add_y(d, years))), ds)
    diff = None if a is None or b is None else round(a - b, 4)
    return {"name": name, "years": years, "from": ds[0] if ds else None, "n": n, "stable": a, "spy_stable": b, "diff_pp": diff}


def dca_path(SPY, C, d, years, months=12):
    """목돈을 12달에 나눠 SPY 에 — 아직 안 넣은 돈은 예금. 전체 돈(처음 = 1) 기준 값 배열."""
    k = SPY.k
    i0 = bisect.bisect_left(k, d)
    j = bisect.bisect_right(k, add_y(d, years)) - 1
    buys = [k[min(bisect.bisect_left(k, f"{int(d[:4]) + (int(d[5:7]) - 1 + m) // 12}-{(int(d[5:7]) - 1 + m) % 12 + 1:02d}{d[7:]}"), len(k) - 1)] for m in range(months)]
    units = 0.0
    cash = 1.0
    vals = []
    bi = 0
    for t in range(i0, j + 1):
        day = k[t]
        if t > i0:
            cash *= 1 + C.chg(k[t - 1], day)
        while bi < months and buys[bi] <= day:
            amt = cash / (months - bi)
            units += amt / SPY.v[t]
            cash -= amt
            bi += 1
        vals.append(units * SPY.v[t] + cash)
    return np.array(vals)


def swing_path(SPY, C, d, years, up=0.05, down=0.03):
    """보유 중 산 값보다 up 오르면 모두 팔아 예금 → 판 값보다 down 빠지면 모두 다시 삼."""
    k = SPY.k
    i0 = bisect.bisect_left(k, d)
    j = bisect.bisect_right(k, add_y(d, years)) - 1
    hold, units, cash, ref, trades = True, 1.0 / SPY.v[i0], 0.0, SPY.v[i0], 0
    vals = []
    for t in range(i0, j + 1):
        p = SPY.v[t]
        if t > i0 and not hold:
            cash *= 1 + C.chg(k[t - 1], k[t])
        if hold and p >= ref * (1 + up):
            cash, units, hold, ref, trades = units * p, 0.0, False, p, trades + 1
        elif not hold and p <= ref * (1 - down):
            units, cash, hold, ref, trades = cash / p, 0.0, True, p, trades + 1
        vals.append(units * p + cash)
    return np.array(vals), trades


def main():
    S = L.load()
    C = S["CASH"]
    X = {s: L.Ser(s, L.rd(HERE / "data" / f"{s}.csv", "adjclose")) for s in
         ["SPY", "QQQ", "QLD", "QYLD", "XYLD", "JEPI", "JEPQ", "XLK", "XLE", "XLF", "XLV", "XLY", "XLP", "XLU", "XLI", "XLB", "XLRE", "XLC"]}
    X["SOX"] = L.Ser("SOX", L.rd(HERE / "data" / "_SOX.csv", "adjclose"))
    SPY = X["SPY"]
    for s, v in X.items():
        log("LOAD", sym=s, first=v.k[0], last=v.k[-1], rows=len(v.k))
    out = {"tool": f"board_2026-11-13.py {VERSION}", "made": str(date.today()), "rule": f"끝에 예금보다 더 + 원금보다 {LOSS:.0%} 넘게 안 줄어듦 · 시작일 {STEP}거래일마다", "checks": {}}
    grid = [(2, "1990-01-01", "2008-12-31"), (2, "2009-01-01", END), (4, "1990-01-01", "2008-12-31"), (4, "2009-01-01", END)]
    for key, syms in {"B21_leverage": ["QLD", "QQQ"], "B27_coveredcall": ["QYLD", "XYLD", "JEPI", "JEPQ"],
                      "B24_sector": ["XLK", "XLE", "XLF", "XLV", "XLY", "XLP", "XLU", "XLI", "XLB", "XLRE", "XLC", "SOX"]}.items():
        rows = [cell(s, X[s], C, y, a, b, SPY) for s in syms for (y, a, b) in grid]
        rows = [r for r in rows if r["n"] >= 10]
        out["checks"][key] = rows
        for r in rows:
            log("CELL", check=key, **r)
    rows = []
    for y, a, b in grid:
        ds = starts(SPY, max(a, SPY.k[0]), b, y)
        lump, n = share(lambda d: stable(path(SPY, d, add_y(d, y)), 1 + C.chg(d, add_y(d, y))), ds)
        dca, _ = share(lambda d: stable(dca_path(SPY, C, d, y), 1 + C.chg(d, add_y(d, y))), ds)
        dd_l, _ = share(lambda d: bool(path(SPY, d, add_y(d, y)).min() < 1 - LOSS), ds)
        dd_d, _ = share(lambda d: bool(dca_path(SPY, C, d, y).min() < 1 - LOSS), ds)
        more, _ = share(lambda d: bool(path(SPY, d, add_y(d, y))[-1] > dca_path(SPY, C, d, y)[-1]), ds)
        rows.append({"years": y, "from": ds[0], "n": n, "lump_stable": lump, "dca_stable": dca, "lump_dd20": dd_l, "dca_dd20": dd_d, "lump_ends_higher": more})
        log("CELL", check="B30_lump_vs_dca", **rows[-1])
    out["checks"]["B30_lump_vs_dca"] = rows
    rows = []
    for up, down in [(0.05, 0.03), (0.10, 0.05)]:
        for y, a, b in grid:
            ds = starts(SPY, max(a, SPY.k[0]), b, y)
            hold, n = share(lambda d: stable(path(SPY, d, add_y(d, y)), 1 + C.chg(d, add_y(d, y))), ds)
            sw, _ = share(lambda d: stable(swing_path(SPY, C, d, y, up, down)[0], 1 + C.chg(d, add_y(d, y))), ds)
            beat, _ = share(lambda d: bool(swing_path(SPY, C, d, y, up, down)[0][-1] > path(SPY, d, add_y(d, y))[-1]), ds)
            tr = [swing_path(SPY, C, d, y, up, down)[1] for d in ds]
            rows.append({"rule": f"+{up:.0%} 팔고 −{down:.0%} 다시", "years": y, "from": ds[0], "n": n, "hold_stable": hold, "swing_stable": sw,
                         "swing_beats_hold": beat, "trades_median": int(np.median(tr))})
            log("CELL", check="B22_swing", **rows[-1])
    out["checks"]["B22_swing"] = rows
    TR = S["TR"]                                         # S&P 500 배당 포함 (1988~)
    rows = []
    for y in (4, 10):
        for a, b in (("1990-01-01", "2008-12-31"), ("2009-01-01", END)):
            ds = starts(TR, a, b, y)
            beat, n = share(lambda d: bool(1 + TR.chg(d, add_y(d, y)) > 1 + C.chg(d, add_y(d, y))), ds)
            rows.append({"years": y, "from": ds[0], "n": n, "index_beats_deposit": beat})
            log("CELL", check="B26_deposit_only", **rows[-1])
    out["checks"]["B26_deposit_only"] = rows
    rows = []                                            # 손실 난 해(1년)가 끝나면 모두 팔고 예금으로 — 다시 안 돌아감 vs 그대로 보유
    for y in (4, 10):
        for a, b in (("1990-01-01", "2008-12-31"), ("2009-01-01", END)):
            ds = starts(TR, a, b, y)
            def quit_wins(d, y=y):
                e = add_y(d, y)
                t = d
                while add_y(t, 1) <= e:
                    if TR.chg(t, add_y(t, 1)) < 0:
                        q = (1 + TR.chg(d, add_y(t, 1))) * (1 + C.chg(add_y(t, 1), e))
                        return bool(q > 1 + TR.chg(d, e))
                    t = add_y(t, 1)
                return None                              # 손실 난 해가 없던 구간은 셈에서 뺌
            w, n = share(quit_wins, ds)
            rows.append({"years": y, "from": ds[0], "n_with_loss_year": n, "quit_ends_higher": w})
            log("CELL", check="B28_quit_after_loss_year", **rows[-1])
    out["checks"]["B28_quit_after_loss_year"] = rows
    SECT = ["XLK", "XLE", "XLF", "XLV", "XLY", "XLP", "XLU", "XLI", "XLB"]   # 1999 부터 있는 9개
    def chase_path(d, y):
        """해마다 첫 거래일에 '지난 1년 가장 많이 오른 업종 ETF' 로 모두 갈아탐 (작년 1등 따라가기)."""
        e, t, v, vals = add_y(d, y), d, 1.0, []
        while t < e:
            u = min(add_y(t, 1), e)
            best = max(SECT, key=lambda s_: X[s_].chg(add_y(t, -1), t))
            seg = path(X[best], t, u) * v
            vals.extend(seg[1:] if vals else seg)
            v = seg[-1]
            t = u
        return np.array(vals)
    rows = []
    for y, a, b in grid:
        ds = starts(SPY, max(a, "2000-01-01"), b, y)
        ch, n = share(lambda d: stable(chase_path(d, y), 1 + C.chg(d, add_y(d, y))), ds)
        sp, _ = share(lambda d: stable(path(SPY, d, add_y(d, y)), 1 + C.chg(d, add_y(d, y))), ds)
        more, _ = share(lambda d: bool(chase_path(d, y)[-1] > path(SPY, d, add_y(d, y))[-1]), ds)
        rows.append({"years": y, "from": ds[0], "n": n, "chase_stable": ch, "spy_stable": sp, "chase_ends_higher": more})
        log("CELL", check="B24_chase_last_year_best_sector", **rows[-1])
    out["checks"]["B24_chase_last_year_best_sector"] = rows
    def mix_path(syms, d, y):                            # 처음에 같은 몫으로 나눠 사고 그대로 둠
        return np.mean([path(X[s_], d, add_y(d, y)) for s_ in syms], axis=0)
    rows = []
    for name, syms in {"기술 겹침 QQQ+XLK+SOX": ["QQQ", "XLK", "SOX"], "업종 셋 XLK+XLV+XLP": ["XLK", "XLV", "XLP"]}.items():
        for y, a, b in grid:
            ds = [d for d in starts(SPY, max(a, "1999-03-10"), b, y)]
            try:
                mx, n = share(lambda d: stable(mix_path(syms, d, y), 1 + C.chg(d, add_y(d, y))), ds)
            except ValueError:
                continue
            sp, _ = share(lambda d: stable(path(SPY, d, add_y(d, y)), 1 + C.chg(d, add_y(d, y))), ds)
            rows.append({"mix": name, "years": y, "from": ds[0], "n": n, "mix_stable": mx, "spy_stable": sp, "diff_pp": round(mx - sp, 4)})
            log("CELL", check="B25_fake_diversification", **rows[-1])
    out["checks"]["B25_fake_diversification"] = rows
    f = HERE / f"board_2026-11-13_{date.today()}.json"
    f.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", "utf-8")
    log("DONE", out=f.name)


if __name__ == "__main__":
    main()
