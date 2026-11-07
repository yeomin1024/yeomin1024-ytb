#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-11-07 — 사용자 지시 "폭락 후 반등인데 어떤 매수 방법이 가장 안전할지 · 투자 금액 1억원으로 일반 개미, 대가 매수/매도 비교 ·
#          진짜 반등 일때는 수익 … 가짜 반등이어서 더 큰 하락이 발생하면 손실 · 대가 … 투자 금액 적절히 분할해서 기준 정해서" — 쇼츠 숫자를 실제
#          S&P 500 지수 종가로 계산. 규칙은 미리 정하고 그날까지의 값만 씀 (판단 = 그날 종가, 매매 = 다음 거래일 종가 · 같은 종가로 판단·매매 ✗).
#   개미 = 반등 날 다음 거래일 종가에 1억 원 전부 매수 → 종가가 산 값보다 20% 넘게 떨어진 날 겁이 나서 → 다음 거래일 종가에 전부 매도, 그 뒤 현금.
#   대가 = 1억 원을 5번(2,000만 원씩)으로 나눔 (하워드 막스 2020-03 「Nobody Knows II」 — 바닥까지 넣을 총액을 정하고 일부만 먼저, 떨어지면 남은 돈으로 더):
#          첫 2,000만 원 = 반등 날 다음 거래일 종가 · 종가가 첫 매수가보다 10%·20%·30%·40% 떨어진 날마다 → 다음 거래일 종가에 2,000만 원씩 · 팔지 않음.
#   평가 = 첫 매수일부터 6개월 뒤(그날이 없으면 다음 거래일) 종가 · 현금 이자 0 · 배당 없음(지수 종가) · 세금·수수료·환율 없음.
#   영상 두 장면: 진짜 반등 2025-04-09(+9.52%) · 가짜 반등 2020-03-02(+4.60%) — 가짜 = 반등 뒤 6개월 안에 반등 전날 종가 밑으로 내려감.
#   견고성: 2000년 이후 '52주 고점에서 10% 넘게 빠진 상태에서 하루 +4% 넘게 오른 날'(앞 사건과 60거래일 넘게 떨어진 것) 모두 · 6개월·12개월.
# 출력: calc/result.json (두 장면 일별 값·매매 표·숫자) + 영상용 video/episodes/bandeung-maesu-2026-11-shorts/data.js. ※ 연구·교육용 — 투자 권유 아님.
from __future__ import annotations

import json
import logging
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

VERSION = "v1.0"
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SRC = ROOT / "stock/source/timing-test-2026-10/calc/gspc_daily.csv"     # ^GSPC 일별 종가 (Yahoo chart API, 2026-10-28 받음)
OUT = HERE / "result.json"
DATA_JS = ROOT / "video/episodes/bandeung-maesu-2026-11-shorts/data.js"
CAP = 100_000_000                      # 1억 원
ANT_STOP = 0.20                        # 개미 공포 매도 기준 (산 값보다 20% 넘게 하락)
SPLITS = 5                             # 대가 분할 횟수
STEP = 0.10                            # 대가 추가 매수 간격 (첫 매수가 대비)
HORIZON_M = 6
SCENES = {"real": "2025-04-09", "fake": "2020-03-02"}

logging.basicConfig(level=logging.INFO, format="%(message)s", stream=sys.stdout)
def log(stage: str, **kv) -> None:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    logging.info(f"[{stage}] [{ts}] " + " ".join(f"{k}={v}" for k, v in kv.items()))


def load() -> pd.Series:
    try:
        s = pd.read_csv(SRC, comment="#", parse_dates=["date"]).set_index("date")["close"].astype(float)
    except Exception as e:  # noqa: BLE001
        log("FAIL", stage="data", path=SRC, err=repr(e), next="timing-test calc.py --fetch 로 다시 받기")
        raise
    dup = int(s.index.duplicated().sum()); na = int(s.isna().sum()); bad = int((s <= 0).sum())
    gaps = int((s.index.to_series().diff().dt.days > 5).sum())
    log("DATA", source=SRC.relative_to(ROOT), rows=len(s), first=s.index[0].date(), last=s.index[-1].date(), dup=dup, na=na, nonpositive=bad, gaps_over_5d=gaps)
    if dup or na or bad:
        raise SystemExit("데이터 이상 — 중복·빈 값·0 이하가 있음")
    return s


def nxt(s: pd.Series, d: pd.Timestamp) -> pd.Timestamp | None:
    i = s.index.get_loc(d) + 1
    return s.index[i] if i < len(s) else None


def run(s: pd.Series, rebound: str, months: int = HORIZON_M) -> dict:
    R = pd.Timestamp(rebound)
    if R not in s.index:
        raise SystemExit(f"반등 날 {rebound} 이 거래일이 아님")
    b0 = nxt(s, R)
    end = s.index[s.index >= b0 + pd.DateOffset(months=months)][0]
    win = s[b0:end]
    trades = {"ant": [], "master": []}
    # 개미
    ant_units = CAP / s[b0]; ant_cash = 0.0; trades["ant"].append(("BUY", b0, s[b0], CAP))
    sell_flag = None
    # 대가
    m_units = CAP / SPLITS / s[b0]; m_cash = CAP - CAP / SPLITS; done = 1; trades["master"].append(("BUY", b0, s[b0], CAP / SPLITS))
    pending = 0
    rows = []
    for d, v in win.items():
        # 1) 어제 판단한 매매를 오늘 종가에
        if sell_flag is not None and ant_units > 0:
            ant_cash = ant_units * v; trades["ant"].append(("SELL", d, v, ant_cash)); ant_units = 0.0; sell_flag = None
        if pending:
            amt = CAP / SPLITS * pending
            m_units += amt / v; m_cash -= amt; done += pending
            trades["master"] += [("BUY", d, v, CAP / SPLITS)] * pending; pending = 0
        # 2) 오늘 종가로 판단 (내일 매매)
        if ant_units > 0 and v <= trades["ant"][0][2] * (1 - ANT_STOP):
            sell_flag = d
        if d > b0 or True:
            want = sum(1 for k in range(1, SPLITS) if v <= s[b0] * (1 - STEP * k))   # 지금까지 넘은 기준 수
            pending = max(0, (1 + want) - done)
        rows.append([d.strftime("%Y-%m-%d"), round(v / s[b0] * 100, 3), round(ant_units * v + ant_cash), round(m_units * v + m_cash)])
    pending = 0                                                                   # 평가일 뒤 매매는 하지 않음
    # 그래프 앞부분 = 반등 전 120거래일 안 최고가(폭락 시작)부터 첫 매수 전날까지 — 둘 다 아직 현금 1억
    i0 = s.index.get_loc(R); look = s.iloc[max(0, i0 - 120):i0 + 1]; peak = look.idxmax()
    pre = [[d.strftime("%Y-%m-%d"), round(v / s[b0] * 100, 3), CAP, CAP] for d, v in s[peak:b0].iloc[:-1].items()]
    ant_end, m_end = rows[-1][2], rows[-1][3]
    pre_low = s[:R].iloc[-2]                                                       # 반등 전날 종가
    kind = "fake" if s[R:R + pd.DateOffset(months=6)].min() < pre_low else "real"
    res = {
        "rebound": rebound, "rebound_ret_pct": round((s[R] / s.iloc[s.index.get_loc(R) - 1] - 1) * 100, 2), "kind": kind,
        "first_buy": b0.strftime("%Y-%m-%d"), "end": end.strftime("%Y-%m-%d"), "months": months,
        "index_buy": round(s[b0], 2), "index_end": round(s[end], 2), "index_min": round(win.min(), 2), "index_min_date": win.idxmin().strftime("%Y-%m-%d"),
        "index_more_drop_pct": round((win.min() / s[b0] - 1) * 100, 1),
        "ant_end": ant_end, "ant_pnl": ant_end - CAP, "ant_min_pnl": min(r[2] for r in rows) - CAP,
        "master_end": m_end, "master_pnl": m_end - CAP, "master_min_pnl": min(r[3] for r in rows) - CAP, "master_buys": done,
        "master_invested": int(CAP / SPLITS * done),
        "peak": peak.strftime("%Y-%m-%d"), "index_peak": round(s[peak], 2), "crash_pct": round((s[:R].iloc[-2] / s[peak] - 1) * 100, 1),
        "pre_n": len(pre),
        "trades": {k: [[a, d.strftime("%Y-%m-%d"), round(p, 2), round(x)] for a, d, p, x in v] for k, v in trades.items()},
        "rows": pre + rows,
    }
    return res


def events(s: pd.Series) -> list[str]:
    r = s.pct_change(); hi = s.rolling(252, min_periods=60).max()
    dd = (s.shift(1) / hi.shift(1) - 1)
    cand = s.index[(r >= 0.04) & (dd <= -0.10) & (s.index >= "2000-01-01")]
    out, last = [], None
    for d in cand:
        if last is None or s.index.get_loc(d) - s.index.get_loc(last) > 60:
            out.append(d.strftime("%Y-%m-%d")); last = d
    return out


def main() -> None:
    t0 = time.perf_counter()
    s = load()
    log("RULES", cap=CAP, ant=f"all-in next close, stop -{ANT_STOP:.0%} then cash", master=f"{SPLITS} splits, +1 each -{STEP:.0%} from first buy, no sell",
        horizon_m=HORIZON_M, cash_rate=0, dividends="none", trade="decide at close t, trade at close t+1")
    scenes = {}
    for key, d in SCENES.items():
        x = run(s, d)
        scenes[key] = x
        log("SCENE", key=key, rebound=d, ret=x["rebound_ret_pct"], kind=x["kind"], buy=x["first_buy"], end=x["end"], more_drop=x["index_more_drop_pct"],
            ant_pnl=x["ant_pnl"], ant_min=x["ant_min_pnl"], master_pnl=x["master_pnl"], master_min=x["master_min_pnl"], master_buys=x["master_buys"])
        for who in ("ant", "master"):
            for t in x["trades"][who]:
                log("TRADE", scene=key, who=who, act=t[0], date=t[1], price=t[2], won=t[3])
        if x["kind"] != key:
            log("WARN", scene=key, msg="장면 분류가 기대와 다름", got=x["kind"])
    # 견고성
    rob = []
    for d in events(s):
        for m in (6, 12):
            try:
                x = run(s, d, m)
            except (IndexError, SystemExit):
                continue
            rob.append({"rebound": d, "months": m, "kind": x["kind"], "ret": x["rebound_ret_pct"], "ant_pnl": x["ant_pnl"], "master_pnl": x["master_pnl"],
                        "ant_min": x["ant_min_pnl"], "master_min": x["master_min_pnl"], "master_buys": x["master_buys"]})
    df = pd.DataFrame(rob)
    for m in (6, 12):
        g = df[df.months == m]
        for kind in ("real", "fake"):
            h = g[g.kind == kind]
            if len(h):
                log("ROBUST", months=m, kind=kind, n=len(h), ant_win=int((h.ant_pnl > 0).sum()), master_win=int((h.master_pnl > 0).sum()),
                    master_better=int((h.master_pnl > h.ant_pnl).sum()), ant_worst=int(h.ant_pnl.min()), master_worst=int(h.master_pnl.min()),
                    ant_min_worst=int(h.ant_min.min()), master_min_worst=int(h.master_min.min()))
    g6 = df[df.months == 6]
    summ = {"n": int(len(g6)), "ant_win": int((g6.ant_pnl > 0).sum()), "master_win": int((g6.master_pnl > 0).sum()),
            "first": g6.rebound.min(), "last": g6.rebound.max(), "master_worst": int(g6.master_pnl.min()), "master_worst_at": g6.loc[g6.master_pnl.idxmin(), "rebound"],
            "ant_worst": int(g6.ant_pnl.min()), "ant_worst_at": g6.loc[g6.ant_pnl.idxmin(), "rebound"]}
    log("ROBUST_TOTAL", months=6, **summ)
    res = {"version": VERSION, "robust_summary_6m": summ, "made": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "source": str(SRC.relative_to(ROOT)),
           "rules": {"cap": CAP, "ant_stop": ANT_STOP, "splits": SPLITS, "step": STEP, "horizon_m": HORIZON_M, "cash_rate": 0},
           "scenes": scenes, "robust": rob}
    OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    # 영상용 data.js (두 장면 일별: [날짜, 지수(첫 매수=100), 개미 평가금액, 대가 평가금액])
    key = {k: {f: v[f] for f in v if f not in ("rows",)} for k, v in scenes.items()}
    DATA_JS.parent.mkdir(parents=True, exist_ok=True)
    DATA_JS.write_text(
        f"// 자동 생성 — stock/source/bandeung-maesu-2026-11/calc/result.json (calc.py {VERSION}, {res['made']})\n"
        "// SER.<장면> = [날짜, S&P 500(첫 매수일 종가 = 100), 개미 평가금액(원), 대가 평가금액(원)] · KEY = 화면 숫자 (모두 calc). 고치지 말고 calc 를 다시 돌림.\n"
        f"window.SER={json.dumps({k: v['rows'] for k, v in scenes.items()}, ensure_ascii=False)};\n"
        f"window.KEY={json.dumps(key, ensure_ascii=False)};\n"
        "// ROB = 2000년 이후 반등 사건 (6개월 뒤) [반등 날, 진짜/가짜, 개미 수익?, 대가 수익?] · ROB_SUM = 합계\n"
        f"window.ROB={json.dumps([[x['rebound'], x['kind'], x['ant_pnl'] > 0, x['master_pnl'] > 0] for x in rob if x['months'] == 6])};\n"
        f"window.ROB_SUM={json.dumps(summ, ensure_ascii=False)};\n", encoding="utf-8")
    log("DONE", out=OUT.relative_to(ROOT), data_js=DATA_JS.relative_to(ROOT), robust_rows=len(rob), sec=round(time.perf_counter() - t0, 2))


if __name__ == "__main__":
    main()
