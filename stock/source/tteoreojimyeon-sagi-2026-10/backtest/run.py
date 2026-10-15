#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.2 — 2026-10-15 — E1d 추가: 2016-03 부터는 일별 종가로 켜진 달에 그 달 평균 가격으로 사기 (월평균이 2020-03 같은 짧은 폭락을
#          놓치는 것 보정 — 떨어지면 사기에 유리한 쪽으로). (v1.1 — 2026-10-15 — E6 추가: 월평균이 짧은 폭락을 작게 보이는지 — FRED 일별 종가로 켜진 달 비교 (2016~).
#          (v1.0 — 2026-10-15 — 최초. 주식 1번 주제 "너무 올랐으니 떨어지면 사겠다" 가설 백테스트 (사용자 지시 2026-10-15 "주식 채널 컨셉은
#          ai로 코드 만들어서 가설을 백테스트해서 검증해보는거니까 고려해서 주제 4가지 정해봐 계속해" → stock/source/topic_candidates.md 1번).
#          규칙: stock/guides/concept.md 2번. 엔진: tools/backtest v1.0 (시험 tools/tests/test_backtest.py).))
"""
가설 (시청자 댓글): "S&P500 이 너무 올랐다 → 떨어지면 사겠다(현금으로 기다리기)" · "환율도 높고 S&P500 이 너무 올랐을 때
한꺼번에 너무 많이 샀다 — 후회" · "폭락장 대비는 어떻게?" (topic_candidates.md 1-2)

실험
  E1  매달 같은 돈: 매달 사기 vs 떨어지면 사기 (고점 대비 5·10·20·30% 떨어진 달에 모은 현금을 모두)
      굴리는 기간 10·20년, 매달 시작 · 현금 이자 0 / 10년 금리(넉넉하게)
      기간: 본 분석 2000-01 시작 ~ 자료가 다 있는 달(배당·금리) · 넓혀 보기 1950-01 시작
  E1p 가격만(배당 빼고 두 방법 모두) — 자료 끝(2026)까지 넣어 최근 3년도 같은지
  E2  E1 중 '사상 최고치 바로 다음 달'에 시작한 기간만
  E3  목돈: 한 번에 vs 12달 나눠서 — 1·5·10년 뒤 (전체 / 사상 최고치 다음 달 시작)
  E4  사상 최고치 다음 달에 산 뒤 1·5·10년 수익률 vs 아무 달에 산 뒤
  E5  '떨어지면' 신호가 얼마나 자주 켜지나 · 가장 오래 안 켜진 기간
  E1d E1 본 분석을 다시 — 2016-03 부터는 '일별 종가가 고점 대비 x%' 가 켜진 달에 그 달 평균 가격으로 산다 (그 전은 월평균 신호)
  E6  월평균 가격이 짧은 폭락(예: 2020-03)을 작게 보이는지 — FRED 일별 종가(2016~, 가격만)로 '고점 대비 x%' 가 켜진 달 비교

결과: results.json (모든 숫자) · results.md (표) · windows_main_10y.csv (기간마다 끝 값 — 차트용) · run.log
대본·화면의 숫자는 이 결과 파일에서만 가져온다. 연구·교육용 — 투자 권유가 아니다. 과거 결과는 미래를 보장하지 않는다.

    python3 stock/source/tteoreojimyeon-sagi-2026-10/backtest/run.py            # 캐시 자료로
    python3 stock/source/tteoreojimyeon-sagi-2026-10/backtest/run.py --refresh  # 자료 다시 받기
"""
import argparse
import json
import logging
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / "tools"))
from backtest import VERSION as ENGINE_VERSION  # noqa: E402
from backtest import data as bd  # noqa: E402
from backtest import monthly as bm  # noqa: E402

VERSION = "v1.2"
MAIN_START = "2000-01-01"        # 본 분석 시작 (CLAUDE.md: 사례·자료는 되도록 최신 — 2000년 닷컴 고점부터)
EXT_START = "1950-01-01"         # 넓혀 보기 (같은 결론인지 확인용 — 대본에서는 한 줄)
DROPS = [0.05, 0.10, 0.20, 0.30]
HORIZONS_Y = [10, 20]
SPLIT_K = 12
LUMP_HORIZONS_M = [12, 60, 120]
MONTHLY_KRW = 1_000_000          # 대본 예시: 매달 100만 원 (달러 수익률 그대로 — 환율 빼고)
LOG = logging.getLogger("tteoreojimyeon")


def log(stage, level=logging.INFO, **kv):
    LOG.log(level, "[%s] %s %s", stage, time.strftime("%Y-%m-%dT%H:%M:%S"), " ".join(f"{k}={v}" for k, v in kv.items()))


def setup_logging(level):
    fmt = logging.Formatter("%(message)s")
    root = logging.getLogger()
    root.setLevel(level)
    for h in list(root.handlers):
        root.removeHandler(h)
    sh = logging.StreamHandler(sys.stderr)
    sh.setFormatter(fmt)
    fh = logging.FileHandler(HERE / "run.log", mode="w", encoding="utf-8")
    fh.setFormatter(fmt)
    root.addHandler(sh)
    root.addHandler(fh)


def pos(index, date):
    return int(index.searchsorted(pd.Timestamp(date)))


def r4(x):
    return None if x is None or (isinstance(x, float) and np.isnan(x)) else round(float(x), 4)


def e1(tri, price, cashes, idx, first, last, horizon_m, only=None, label="", sig_for=None):
    """매달 사기 vs 떨어지면 사기 — 굴리는 기간마다 끝 값. only = 시작 달 고르기(bool 배열). sig_for(drop) → 신호 배열 (기본: 월평균)."""
    s, e = bm.windows(len(tri), horizon_m, first=first, last=last)
    if only is not None:
        keep = only[s]
        s, e = s[keep], e[keep]
    out = {"windows": int(len(s))}
    if not len(s):
        return out, None
    dca = bm.dca_wealth(tri, s, e)
    out["first_start"], out["last_start"] = bm.month_labels(idx, [s[0], s[-1]])
    out["contributed_krw"] = MONTHLY_KRW * horizon_m
    out["dca_median_krw"] = int(round(np.median(dca) * MONTHLY_KRW))
    table = {"start": bm.month_labels(idx, s), "end": bm.month_labels(idx, e), "dca": dca}
    for cname, cash in cashes.items():
        for drop in DROPS:
            sig = sig_for(drop) if sig_for else bm.dip_signal(price, drop)
            res = bm.dip_wealth(tri, cash, bm.next_true(sig), s, e)
            key = f"drop{int(drop * 100)}_{cname}"
            sm = bm.summarize(dca, res["wealth"], "dca", "dip")
            sm.update({
                "dip_median_krw": int(round(np.median(res["wealth"]) * MONTHLY_KRW)),
                "median_gap_krw": int(round(np.median(dca - res["wealth"]) * MONTHLY_KRW)),
                "cash_left_share_median": r4(np.median(res["cash_left"] / res["wealth"])),
                "never_bought_windows": int((res["buy_months"] == 0).sum()),
                "avg_wait_months_median": r4(np.median(res["avg_wait_months"])),
                "dip_best": {"start": bm.month_labels(idx, [s[int(np.argmin(dca / res["wealth"]))]])[0],
                             "ratio_dca_over_dip": r4((dca / res["wealth"]).min())},
                "dca_best": {"start": bm.month_labels(idx, [s[int(np.argmax(dca / res["wealth"]))]])[0],
                             "ratio_dca_over_dip": r4((dca / res["wealth"]).max())},
            })
            out[key] = {k: (r4(v) if isinstance(v, float) else v) for k, v in sm.items()}
            table[key] = res["wealth"]
            log("TRADE", exp=label, horizon_m=horizon_m, key=key, windows=len(s), dca_wins=sm["dca_wins"],
                ratio_median=f"{sm['ratio_median']:.4f}", never_bought=out[key]["never_bought_windows"])
    return out, pd.DataFrame(table)


def main(argv=None):
    ap = argparse.ArgumentParser(description="떨어지면 사기 vs 매달 사기 백테스트 (연구·교육용)")
    ap.add_argument("--refresh", action="store_true", help="자료 다시 받기")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args(argv)
    setup_logging(getattr(logging, a.log_level))
    t0 = time.time()
    log("START", version=VERSION, engine=ENGINE_VERSION, refresh=a.refresh)

    # 1. 자료
    df, meta = bd.sp500_monthly(refresh=a.refresh)
    complete = pd.Timestamp(meta["complete_until"])
    full = df.loc[:complete]                       # 배당·금리가 다 있는 달까지 (총수익)
    idx = full.index
    price = full["price"].to_numpy()
    tri = bm.total_return_index(price, full["dividend"].to_numpy())
    cashes = {"cash0": bm.cash_index(len(tri)), "cashRate": bm.cash_index(len(tri), full["long_rate"].to_numpy())}
    log("DATA", used_first=idx[0].date(), used_last=idx[-1].date(), months=len(idx),
        dropped_tail_months=int((df.index > complete).sum()), note="배당·금리가 비어 있는 끝 달은 총수익에서 뺌 (E1p 가격만에서는 씀)")

    # 2. 신호 (E5)
    main_first, ext_first = pos(idx, MAIN_START), pos(idx, EXT_START)
    e5 = {}
    for drop in DROPS:
        sig = bm.dip_signal(price, drop)
        for name, f in (("main", main_first), ("ext", ext_first)):
            seg = sig[f:]
            runs, cur = [], 0
            for v in seg:
                cur = 0 if v else cur + 1
                runs.append(cur)
            longest = int(max(runs)) if runs else 0
            end_i = f + int(np.argmax(runs)) if runs else f
            e5[f"drop{int(drop * 100)}_{name}"] = {
                "signal_months": int(seg.sum()), "months": int(len(seg)), "share": r4(seg.mean()),
                "longest_no_signal_months": longest,
                "longest_no_signal_until": bm.month_labels(idx, [end_i])[0]}
            log("SIGNAL", drop=drop, period=name, signal_months=int(seg.sum()), months=len(seg), share=f"{seg.mean():.3f}",
                longest_no_signal_months=longest)

    # 3. E1·E2 (총수익)
    high = bm.at_high(price)
    res = {"E1": {}, "E2": {}}
    win_csv = None
    for name, f in (("main", main_first), ("ext", ext_first)):
        for hy in HORIZONS_Y:
            hm = hy * 12
            r, tab = e1(tri, price, cashes, idx, f, len(tri) - 1, hm, label=f"E1_{name}")
            res["E1"][f"{name}_{hy}y"] = r
            if name == "main" and hy == 10:
                win_csv = tab
            r2, _ = e1(tri, price, cashes, idx, f, len(tri) - 1, hm, only=high, label=f"E2_{name}")
            res["E2"][f"{name}_{hy}y"] = r2

    # 4. E1p 가격만 (배당 빼고, 자료 끝까지) — 최근 3년 포함해도 같은지
    p_all = df["price"].to_numpy()
    pri = p_all / p_all[0]
    idx_all = df.index
    res["E1p"] = {}
    for hy in HORIZONS_Y:
        r, _ = e1(pri, p_all, {"cash0": bm.cash_index(len(pri))}, idx_all, pos(idx_all, MAIN_START), len(pri) - 1, hy * 12,
                  label="E1p_main")
        res["E1p"][f"main_{hy}y_price_only_to_{idx_all[-1].strftime('%Y-%m')}"] = r

    # 5. E3 목돈 한 번에 vs 12달 나눠서
    res["E3"] = {}
    for name, f in (("main", main_first), ("ext", ext_first)):
        for hm in LUMP_HORIZONS_M:
            s, e = bm.windows(len(tri), hm, first=f)
            for subset, keep in (("all", np.ones(len(s), bool)), ("after_high", high[s])):
                ss, ee = s[keep], e[keep]
                if not len(ss):
                    continue
                for cname, cash in cashes.items():
                    lump, split = bm.lump_vs_split(tri, cash, ss, ee, k=SPLIT_K)
                    sm = bm.summarize(lump, split, "lump", "split")
                    sm["first_start"], sm["last_start"] = bm.month_labels(idx, [ss[0], ss[-1]])
                    sm["lump_loss_windows"] = int((lump < 1).sum())
                    sm["split_loss_windows"] = int((split < 1).sum())
                    sm["lump_worst"] = r4(lump.min())
                    sm["split_worst"] = r4(split.min())
                    res["E3"][f"{name}_{hm}m_{subset}_{cname}"] = {k: (r4(v) if isinstance(v, float) else v) for k, v in sm.items()}
                    log("TRADE", exp="E3", period=name, horizon_m=hm, subset=subset, cash=cname, windows=len(ss),
                        lump_wins=sm["lump_wins"], ratio_median=f"{sm['ratio_median']:.4f}")

    # 6. E4 사상 최고치 다음 달에 산 뒤 수익률 vs 아무 달
    res["E4"] = {}
    for name, f in (("main", main_first), ("ext", ext_first)):
        for hm in LUMP_HORIZONS_M:
            fwd = bm.forward_return(tri, hm)
            seg = np.arange(f, len(tri))
            ok = ~np.isnan(fwd[seg])
            allm, him = seg[ok], seg[ok & high[seg]]
            res["E4"][f"{name}_{hm}m"] = {
                "all_months": int(len(allm)), "all_median_annual": r4(np.median(fwd[allm])),
                "all_positive_share": r4((fwd[allm] > 0).mean()),
                "high_months": int(len(him)),
                "high_median_annual": r4(np.median(fwd[him])) if len(him) else None,
                "high_positive_share": r4((fwd[him] > 0).mean()) if len(him) else None}
            log("RESULT", exp="E4", period=name, horizon_m=hm, **{k: v for k, v in res["E4"][f"{name}_{hm}m"].items()})

    res["E5"] = e5

    # 7. E6 일별 종가 vs 월평균 — 같은 '고점 대비 x%' 가 켜진 달 (2016~, 가격만)
    try:
        daily, dmeta = bd.sp500_daily(refresh=a.refresh)
        d_peak = daily.cummax()
        first_m = daily.index.min().to_period("M") + 1            # 첫 달은 고점 기록이 짧아 뺌
        mp = df["price"]
        m_peak = mp.cummax()
        res["E6"] = {"daily_first": dmeta["first"], "daily_last": dmeta["last"], "note":
                     "일별: 그 달 어느 날 종가가 그날까지 최고 종가의 (1-x) 이하 · 월평균: 그 달 평균이 그때까지 최고 월평균의 (1-x) 이하. "
                     "일별 고점은 2016-02 부터만 셈 (그 전 고점은 모름 — 2016 년 초 몇 달은 덜 켜질 수 있음)"}
        for drop in DROPS:
            dm = sorted({t.to_period("M") for t in daily.index[(daily <= (1 - drop) * d_peak).to_numpy()]})
            dm = [m for m in dm if m >= first_m]
            last_m = daily.index.max().to_period("M")
            mm = [t.to_period("M") for t in mp.index[(mp <= (1 - drop) * m_peak).to_numpy()]]
            mm = [m for m in mm if first_m <= m <= last_m]
            only_daily = sorted(set(dm) - set(mm))
            res["E6"][f"drop{int(drop * 100)}"] = {
                "daily_months": [str(m) for m in dm], "monthly_avg_months": [str(m) for m in mm],
                "only_daily": [str(m) for m in only_daily]}
            log("SIGNAL", exp="E6", drop=drop, daily_months=len(dm), monthly_avg_months=len(mm),
                only_daily=",".join(str(m) for m in only_daily) or "-")
    except RuntimeError as e:
        res["E6"] = {"error": str(e)}
        log("SIGNAL", logging.WARNING, exp="E6", error=e, note="일별 자료 없이 계속 (한계에 적음)")

    # 8. E1d 일별 신호 섞기 (2016-03 ~ 총수익 끝) — 떨어지면 사기에 유리한 쪽 점검
    if "error" not in res["E6"]:
        hybrid_from = pd.Timestamp(daily.index.min()).to_period("M") + 1
        month_of = idx.to_period("M")
        use_daily = np.asarray(month_of >= hybrid_from)

        def sig_hybrid(drop):
            sig = bm.dip_signal(price, drop)
            hit = {pd.Period(m) for m in res["E6"][f"drop{int(drop * 100)}"]["daily_months"]}
            daily_sig = np.array([m in hit for m in month_of])
            return np.where(use_daily, daily_sig, sig)        # 일별: 켜진 그 달에 그 달 평균으로 (그 달 앞쪽 높은 값이 섞여 보수적)
        res["E1d"] = {}
        for hy in HORIZONS_Y:
            r, _ = e1(tri, price, cashes, idx, main_first, len(tri) - 1, hy * 12, label="E1d_main", sig_for=sig_hybrid)
            res["E1d"][f"main_{hy}y_daily_signal_from_{hybrid_from}"] = r
    out = {
        "version": VERSION, "engine": ENGINE_VERSION, "generated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "data": {k: meta[k] for k in ("url", "fetched_at", "sha256", "rows", "first", "last", "dividend_until",
                                       "long_rate_until", "complete_until", "license", "about") if k in meta},
        "params": {"main_start": MAIN_START, "ext_start": EXT_START, "drops": DROPS, "horizons_y": HORIZONS_Y,
                   "split_k": SPLIT_K, "lump_horizons_m": LUMP_HORIZONS_M, "monthly_krw": MONTHLY_KRW,
                   "costs": "매매 수수료·세금·환율 넣지 않음 (두 방법 같은 자산). 현금 이자: 0 또는 10년 국채 금리(넉넉하게)",
                   "timing": "달 t 에 넣는 돈은 달 t 월평균 가격으로 · 신호는 달 t-1 까지 가격만 · 끝까지 못 산 현금은 현금으로 셈"},
        "results": res,
        "seconds": round(time.time() - t0, 2),
    }
    (HERE / "results.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), "utf-8")
    if win_csv is not None:
        win_csv.to_csv(HERE / "windows_main_10y.csv", index=False, float_format="%.6f")
    (HERE / "results.md").write_text(render_md(out), "utf-8")
    log("DONE", seconds=out["seconds"], results=HERE / "results.json")
    return out


def won(x):
    return f"{x / 10_000:,.0f}만 원"


def render_md(o):
    R = o["results"]
    L = [f"# 백테스트 결과 — 떨어지면 사기 vs 매달 사기 (`run.py` {o['version']}, 엔진 {o['engine']})", "",
         f"- 만든 시각: {o['generated']} · 걸린 시간 {o['seconds']}초",
         f"- 자료: {o['data'].get('about')} — {o['data'].get('url')} (받은 시각 {o['data'].get('fetched_at')}, sha256 {o['data'].get('sha256', '')[:12]}…)",
         f"- 총수익(배당 재투자)은 배당·금리가 다 있는 **{o['data']['complete_until'][:7]}** 까지. 가격만 보는 E1p 는 {o['data']['last'][:7]} 까지.",
         f"- 시점: {o['params']['timing']}",
         f"- 비용: {o['params']['costs']}",
         "- ※ 연구·교육용. 투자 권유가 아니다. 과거 결과는 미래를 보장하지 않는다. 겹치는 기간을 매달 시작해 센 것이라 기간끼리 독립이 아니다.", ""]
    L += ["## E1. 매달 사기 vs 떨어지면 사기 (매달 100만 원)", "",
          "| 기간 | 시작 | 기간 수 | 넣은 돈 | 떨어지면(고점 대비) | 현금 이자 | 매달 사기가 더 많은 기간 | 끝 값 중앙값: 매달 / 떨어지면 | 차이 중앙값 | 끝까지 못 산 현금 비율(중앙값) | 한 번도 못 산 기간 |",
          "|---|---|---|---|---|---|---|---|---|---|---|"]
    for tag, rr in (("E1", R["E1"]), ("E1d 2016~ 일별 신호", R.get("E1d", {})), ("E1p 가격만", R["E1p"])):
        for k, r in rr.items():
            if not r.get("windows"):
                continue
            for key, v in r.items():
                if not key.startswith("drop"):
                    continue
                drop, cname = key.split("_")
                L.append(f"| {tag} {k} | {r['first_start']}~{r['last_start']} | {r['windows']} | {won(r['contributed_krw'])} | {drop[4:]}% | "
                         f"{'0' if cname == 'cash0' else '10년 금리'} | {v['dca_wins']}/{v['windows']} ({v['dca_wins_share'] * 100:.0f}%) | "
                         f"{won(r['dca_median_krw'])} / {won(v['dip_median_krw'])} | {won(v['median_gap_krw'])} | "
                         f"{v['cash_left_share_median'] * 100:.0f}% | {v['never_bought_windows']} |")
    L += ["", "## E2. 사상 최고치 다음 달에 시작한 기간만", "",
          "| 기간 | 기간 수 | 떨어지면 | 현금 이자 | 매달 사기가 더 많은 기간 | 끝 값 비율 중앙값 (매달/떨어지면) |", "|---|---|---|---|---|---|"]
    for k, r in R["E2"].items():
        for key, v in r.items():
            if key.startswith("drop"):
                drop, cname = key.split("_")
                L.append(f"| {k} | {r['windows']} | {drop[4:]}% | {'0' if cname == 'cash0' else '10년 금리'} | "
                         f"{v['dca_wins']}/{v['windows']} ({v['dca_wins_share'] * 100:.0f}%) | {v['ratio_median']:.3f} |")
    L += ["", "## E3. 목돈 — 한 번에 vs 12달 나눠서", "",
          "| 경우 | 기간 수 | 한 번에가 더 많은 기간 | 비율 중앙값 (한 번에/나눠서) | 가장 나쁜 끝 값: 한 번에 / 나눠서 (원금 1) |", "|---|---|---|---|---|"]
    for k, v in R["E3"].items():
        L.append(f"| {k} | {v['windows']} | {v['lump_wins']}/{v['windows']} ({v['lump_wins_share'] * 100:.0f}%) | {v['ratio_median']:.3f} | "
                 f"{v['lump_worst']:.3f} / {v['split_worst']:.3f} |")
    L += ["", "## E4. 사상 최고치 다음 달에 산 뒤 vs 아무 달에 산 뒤 (연 수익률 중앙값, 오른 비율)", "",
          "| 경우 | 아무 달 (n) | 사상 최고치 다음 달 (n) |", "|---|---|---|"]
    for k, v in R["E4"].items():
        hi = "—" if v["high_median_annual"] is None else f"{v['high_median_annual'] * 100:.1f}% · 오름 {v['high_positive_share'] * 100:.0f}% ({v['high_months']})"
        L.append(f"| {k} | {v['all_median_annual'] * 100:.1f}% · 오름 {v['all_positive_share'] * 100:.0f}% ({v['all_months']}) | {hi} |")
    L += ["", "## E5. '떨어지면' 신호가 켜진 달", "", "| 경우 | 켜진 달 / 전체 | 가장 오래 안 켜진 기간 (끝난 달) |", "|---|---|---|"]
    for k, v in R["E5"].items():
        L.append(f"| {k} | {v['signal_months']}/{v['months']} ({v['share'] * 100:.0f}%) | {v['longest_no_signal_months']}달 ({v['longest_no_signal_until']}) |")
    e6 = R.get("E6") or {}
    L += ["", f"## E6. 월평균 vs 일별 종가 — '고점 대비 x%'가 켜진 달 ({e6.get('daily_first', '?')[:7]}~{e6.get('daily_last', '?')[:7]}, 가격만)", "",
          f"- {e6.get('note', e6.get('error', ''))}", "", "| 떨어지면 | 일별 종가로 켜진 달 | 월평균으로 켜진 달 | 일별로만 켜진 달 |", "|---|---|---|---|"]
    for k, v in e6.items():
        if k.startswith("drop"):
            L.append(f"| {k[4:]}% | {len(v['daily_months'])} | {len(v['monthly_avg_months'])} | {', '.join(v['only_daily']) or '없음'} |")
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    main()
