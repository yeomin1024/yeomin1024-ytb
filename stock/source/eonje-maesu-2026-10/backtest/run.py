# -*- coding: utf-8 -*-
# VERSION: v2.0 — 2026-10-16 — 다시 만듦 (사용자 지시 2026-10-16 "기간이 너무 긴거 아니야? 그리고 왜 현재는 포함 안했어 2016년부터 현재까지로
#          설정하고 지금은 매수만 보는 거니까 매수에 관련된 것만 테스트해야지 왜 손절이 있어 매도 규칙은 똑같이 해 그리고 buy and hold랑
#          비교하지말고 주가 차트에서 매수/매도 지점을 표시하는 걸로 하자"): 매수 신호 10가지 × 같은 매도 규칙(산 날부터 252 거래일 뒤 매도),
#          S&P 500 일별 2016-01-04 ~ 자료 끝(2026-02-11), 같은 $10,000. 엔진 tools/backtest/entry.py v1.0. 관망과 견주지 않는다.
#          (v1.x — 매수 규칙 10가지 vs 관망 32년 — stock/source/_old/eonje-maesu-2026-10-v1/backtest/)
"""매수 신호 10가지 — 같은 돈 · 같은 매도 규칙 (연구·교육용 — 투자 권유가 아니다. 과거 결과는 미래를 보장하지 않는다).

실행:  python3 stock/source/eonje-maesu-2026-10/backtest/run.py
결과:  results.json · results.md · trades.csv · run.log · anim.js (장면 파일 자료 — 숫자는 이 파일에서만)

본 실험
  자산     S&P 500 지수 일별 종가 (가격만 — 배당 빠짐, 모든 규칙 같은 조건). VIX 일별 종가 (공포지수 규칙만)
  기간     2016-01-04 (첫 거래일) ~ 2026-02-11 (클라우드에서 받을 수 있는 S&P 500 일별 자료의 끝)
  돈       $10,000 한 번, 더 넣지 않음. 살 때 전부, 팔 때 전부
  매수     규칙마다 다름 (entry.RULES) — 신호는 그날 종가까지, 사는 것은 다음 거래일 종가
  매도     모든 규칙 같음 — 산 날부터 252 거래일(약 1년) 뒤 그날 종가
  비용     사고팔 때 0.1% · 현금 이자 0
확인 (결론을 바꾸는지 보기)
  보유 기간 21·63·126 거래일 · 비용 0 · 참고값 '아무 날 매수 → 252 거래일 뒤 매도' 분포 (관망 아님 — 매수 날짜의 값어치를 보는 잣대)
"""
import json
import logging
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / "tools"))
from backtest import data as bd          # noqa: E402
from backtest import entry as en         # noqa: E402

VERSION = "v2.0"
START, END = "2016-01-01", "2026-02-11"
CAPITAL, COST, HOLD = 10_000.0, 0.001, en.HOLD_DAYS
CHECK_HOLDS = [21, 63, 126]


def setup_log():
    fmt = logging.Formatter("%(message)s")
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    for h in list(root.handlers):
        root.removeHandler(h)
    fh = logging.FileHandler(HERE / "run.log", "w", "utf-8")
    sh = logging.StreamHandler(sys.stdout)
    for h in (fh, sh):
        h.setFormatter(fmt)
        root.addHandler(h)
    return logging.getLogger("run")


def log(stage, **kv):
    logging.getLogger("run").info("[%s] %s %s", stage, time.strftime("%Y-%m-%dT%H:%M:%S"), " ".join(f"{k}={v}" for k, v in kv.items()))


def load():
    close, meta_c = bd.sp500_daily_long()
    vix, meta_v = bd.vix_daily()
    if close.index.max() < pd.Timestamp(END):
        raise SystemExit(f"[DATA] S&P 500 자료가 {END} 전에 끝남 ({close.index.max().date()}) → END 를 자료 끝으로")
    log("DATA", sp500=f"{close.index[0].date()}~{close.index[-1].date()} rows={len(close)}",
        vix=f"{vix.index[0].date()}~{vix.index[-1].date()} rows={len(vix)}", use=f"{START}~{END}",
        note="S&P 500 일별 자료는 2026-02-11 까지 (FRED 사본 — 클라우드에서 Yahoo·FRED 직접 받기는 막힘)")
    return close, vix, {"sp500_daily": meta_c, "vix_daily": meta_v}


def pct(x, d=1):
    return "—" if x is None or (isinstance(x, float) and np.isnan(x)) else f"{x * 100:+.{d}f}%"


def main():
    setup_log()
    t0 = time.time()
    close, vix, metas = load()
    out, ind, (s, e) = en.run_all(close, START, END, vix=vix, hold=HOLD, capital=CAPITAL, cost=COST)
    dates = close.index
    ref = en.forward_returns(close, START, END, hold=HOLD, cost=COST)

    # 확인: 다른 보유 기간 · 비용 0
    checks = {}
    for h in CHECK_HOLDS:
        o, _, _ = en.run_all(close, START, END, vix=vix, hold=h, capital=CAPITAL, cost=COST, label=f"hold{h}")
        checks[f"hold{h}"] = {k: o[k][1] for k in o}
        checks[f"hold{h}"]["_reference"] = en.forward_returns(close, START, END, hold=h, cost=COST)
    o, _, _ = en.run_all(close, START, END, vix=vix, hold=HOLD, capital=CAPITAL, cost=0.0, label="cost0")
    checks["cost0"] = {k: o[k][1] for k in o}

    rank = sorted(out, key=lambda k: -out[k][1]["final"])
    for name, c in checks.items():
        rk = sorted([k for k in c if not k.startswith("_")], key=lambda k: -c[k]["final"])
        log("RESULT", check=name, top3=",".join(rk[:3]), bottom=rk[-1], main_top3=",".join(rank[:3]))

    res = {
        "version": VERSION, "engine": en.VERSION, "made_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "note": "연구·교육용. 투자 권유가 아니다. 과거 결과는 미래를 보장하지 않는다. 대본·화면 숫자는 이 파일에서만.",
        "params": {"asset": "S&P 500 지수 일별 종가 (가격만 — 배당 빠짐)", "start": str(dates[s].date()), "end": str(dates[e].date()),
                   "capital": CAPITAL, "cost": COST, "cash_interest": 0, "hold_days": HOLD,
                   "sell_rule": "산 날부터 252 거래일 뒤 그날 종가에 전부 매도 (모든 규칙 같음)",
                   "buy_timing": "신호 = 그날 종가까지, 매수 = 다음 거래일 종가", "rules": {k: {"name": en.RULES[k][1], "condition": en.RULES[k][2]} for k in en.ORDER}},
        "data": {k: {kk: v.get(kk) for kk in ("url", "wheel", "member", "commit", "sha256", "first", "last", "rows", "splice")} for k, v in metas.items()},
        "rules": {k: out[k][1] for k in en.ORDER},
        "trades": {k: out[k][0].trades for k in en.ORDER},
        "rank_by_final": rank,
        "reference_any_day": ref,
        "checks": checks,
        "index": {"start_close": float(close.iloc[s]), "end_close": float(close.iloc[e]),
                  "max": float(close.iloc[s:e + 1].max()), "max_date": str(close.iloc[s:e + 1].idxmax().date())},
    }
    (HERE / "results.json").write_text(json.dumps(res, ensure_ascii=False, indent=1, default=float), "utf-8")

    rows = []
    for k in en.ORDER:
        for t in out[k][0].trades:
            rows.append({"rule": k, "buy_date": t["buy_date"], "buy_price": round(t["buy_price"], 2), "sell_date": t["sell_date"],
                         "sell_price": round(t["sell_price"], 2), "days": t["days"], "ret": round(t["ret"], 6), "open": t["open"],
                         "buy_cash": round(t["buy_cash"], 2), "sell_cash": round(t["sell_cash"], 2)})
    pd.DataFrame(rows).to_csv(HERE / "trades.csv", index=False)

    write_md(res, out)
    write_anim(close, vix, ind, out, s, e, res)
    log("RESULT", file="results.json,results.md,trades.csv,anim.js", rank=",".join(rank), sec=f"{time.time() - t0:.1f}")


def write_md(res, out):
    P = res["params"]
    L = [f"# 매수 신호 10가지 — 같은 돈·같은 매도 규칙 (`run.py` {VERSION}, 엔진 `entry.py` {res['engine']}, {res['made_at']})", "",
         "> 연구·교육용. 투자 권유가 아니다. 과거 결과는 미래를 보장하지 않는다. 숫자는 이 파일·`results.json` 의 코드 출력만 쓴다.", "",
         f"- 자산: {P['asset']} · 기간 {P['start']} ~ {P['end']} · 시작 돈 $10,000 (모두 같음, 더 넣지 않음)",
         f"- 매수: 규칙마다 다름 — {P['buy_timing']} · **매도: {P['sell_rule']}** · 비용 0.1% · 현금 이자 0",
         f"- S&P 500: {res['index']['start_close']:,.2f} → {res['index']['end_close']:,.2f} (기간 최고 {res['index']['max']:,.2f}, {res['index']['max_date']})", "",
         "## 1. 본 실험 (끝 값 순)", "",
         "| # | 규칙 | 조건 | 끝 값 | 누적 | 매수 | 판 거래 | 이긴 거래 | 거래 평균 | 가장 좋은 · 나쁜 거래 | 주식 보유 비율 | 가장 긴 현금 | 첫 매수 |",
         "|---:|---|---|---:|---:|---:|---:|---:|---:|---|---:|---:|---|"]
    for i, k in enumerate(res["rank_by_final"], 1):
        r = res["rules"][k]
        L.append(f"| {i} | {P['rules'][k]['name']} | {P['rules'][k]['condition']} | ${r['final']:,.0f} | {pct(r['total_return'])} | {r['buys']} | "
                 f"{r['trades_closed']}{' + 보유 중 1' if r['trades_open'] else ''} | {(r['win_rate'] * 100):.0f}% | {pct(r['avg_trade'])} | "
                 f"{pct(r['best_trade'])} · {pct(r['worst_trade'])} | {r['invested_share'] * 100:.0f}% | {r['longest_wait_days']}일 | {r['first_buy']} |")
    ref = res["reference_any_day"]
    L += ["", f"- 참고값 (관망 아님): **아무 날** {ref['from']} ~ {ref['to_last_buy']} 에 사서 252 거래일 뒤 판 {ref['n_days']}번 — 평균 {pct(ref['mean'])} · 가운데 {pct(ref['median'])} · 이긴 비율 {ref['win_rate'] * 100:.0f}% · 아래 10% {pct(ref['p10'])} · 위 10% {pct(ref['p90'])}", "",
          "## 2. 거래 (BUY → SELL)", ""]
    for k in en.ORDER:
        L.append(f"**{P['rules'][k]['name']}** — " + " · ".join(
            f"{t['buy_date']} {t['buy_price']:,.0f} → {t['sell_date']} {t['sell_price']:,.0f} {pct(t['ret'])}{' (보유 중)' if t['open'] else ''}" for t in res["trades"][k]))
        L.append("")
    L += ["## 3. 확인 — 보유 기간·비용을 바꾸면 순위가 바뀌나", "", "| 규칙 | 본 실험 252일 | 126일 | 63일 | 21일 | 비용 0 |", "|---|---:|---:|---:|---:|---:|"]
    for k in res["rank_by_final"]:
        c = res["checks"]
        L.append(f"| {P['rules'][k]['name']} | ${res['rules'][k]['final']:,.0f} | ${c['hold126'][k]['final']:,.0f} | ${c['hold63'][k]['final']:,.0f} | "
                 f"${c['hold21'][k]['final']:,.0f} | ${c['cost0'][k]['final']:,.0f} |")
    L += ["", "## 4. 한계", "",
          "- 가격만이다 (배당 약 1.5%/년 빠짐 — 주식을 오래 든 규칙일수록 덜 셈). 현금 이자 0 (2023~2025 처럼 금리가 높을 때 현금으로 기다린 규칙을 덜 셈). 두 효과는 방향이 반대다.",
          "- S&P 500 일별 자료가 2026-02-11 에서 끝난다 (클라우드에서 받을 수 있는 가장 최근). 그 뒤는 들어 있지 않다.",
          "- 판 거래가 규칙마다 2~9번이라 거래 평균·승률은 표본이 작다. 끝 값은 시작 날·보유 기간에 따라 달라진다 (3번 확인).",
          "- 세금·환율은 넣지 않았다. 지수 자체를 사고판 것으로 셈 (실제로는 ETF — 보수 약 0.03~0.1%/년)."]
    (HERE / "results.md").write_text("\n".join(L) + "\n", "utf-8")


def write_anim(close, vix, ind, out, s, e, res):
    """장면 파일 자료 (window.AN). 날짜는 s..e 거래일 전부, 값은 코드 출력을 반올림만."""
    d = close.index[s:e + 1]
    AN = {"v": VERSION, "made_at": res["made_at"], "dates": [x.strftime("%Y-%m-%d") for x in d],
          "close": [round(float(x), 2) for x in close.iloc[s:e + 1]],
          "lines": {"ath": [round(float(x), 2) for x in ind["ath"][s:e + 1]],
                    "sma50": [round(float(x), 2) for x in ind["sma50"][s:e + 1]],
                    "sma200": [round(float(x), 2) for x in ind["sma200"][s:e + 1]],
                    "hi252": [round(float(x), 2) for x in ind["hi252"][s:e + 1]],
                    "rsi14": [round(float(x), 2) for x in ind["rsi14"][s:e + 1]],
                    "vix": [None if np.isnan(x) else round(float(x), 2) for x in ind["vix"][s:e + 1]],
                    "ret1": [round(float(x) * 100, 3) for x in ind["ret1"][s:e + 1]],
                    "close_252ago": [round(float(close.iloc[i - 252]), 2) for i in range(s, e + 1)]},
          "hold_days": HOLD, "capital": CAPITAL, "order": en.ORDER,
          "rules": {}}
    for k in en.ORDER:
        r, st = out[k]
        AN["rules"][k] = {"value": [round(float(x), 2) for x in r.value], "holding": "".join("1" if h else "0" for h in r.holding),
                          "trades": [{"b": t["buy_i"] - s, "s": t["sell_i"] - s, "bp": round(t["buy_price"], 2), "sp": round(t["sell_price"], 2),
                                      "r": round(t["ret"], 6), "open": t["open"], "bc": round(t["buy_cash"], 2), "sc": round(t["sell_cash"], 2)}
                                     for t in r.trades],
                          "final": round(st["final"], 2), "win": st["win_rate"], "avg": st["avg_trade"]}
        # 장면 숫자 = 결과 파일 숫자 (반올림만) 확인
        assert abs(AN["rules"][k]["value"][-1] - res["rules"][k]["final"]) < 0.01, k
        assert len(AN["rules"][k]["value"]) == len(AN["dates"]), k
    txt = ("// 자동 생성 — stock/source/eonje-maesu-2026-10/backtest/run.py " + VERSION + " (손으로 고치지 않음). 연구·교육용 — 투자 권유 아님.\n"
           "window.AN = " + json.dumps(AN, ensure_ascii=False, separators=(",", ":")) + ";\n")
    (HERE / "anim.js").write_text(txt, "utf-8")
    log("RESULT", anim="anim.js", days=len(d), kb=round(len(txt) / 1024))


if __name__ == "__main__":
    main()
