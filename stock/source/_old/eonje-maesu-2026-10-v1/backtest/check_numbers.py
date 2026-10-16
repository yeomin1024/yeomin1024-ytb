#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-16 — 최초. 대본(eonje-maesu-2026-10.txt)의 숫자를 results.json 에서 다시 만들어, 그 글자가 그 문장에 그대로 있는지 확인 →
#          ../checklist.md (stock/guides/concept.md 2번 '숫자는 코드 출력만', 사용자 선호: 숫자마다 출처를 따라갈 수 있게).
"""cd stock/source/eonje-maesu-2026-10/backtest && python3 check_numbers.py      # → ../checklist.md, 하나라도 다르면 끝 코드 1

말로 읽는 금액은 천 달러 단위 반올림 ('22만 3천 달러' = $223,034), %는 소수 한 자리, 배수는 소수 두 자리(×4.6 만 한 자리 — 화면도 같음).
"""
import json
import sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[3] / "tools"))
import srt_tool  # noqa: E402

R = json.loads((HERE / "results.json").read_text("utf-8"))
SENT = srt_tool.parse_txt(HERE.parent / "eonje-maesu-2026-10.txt")
M, F, A, RL = R["main"], R["facts"], R["analysis"], R["rolling_10y"]
H = M["hold"]["stats"]


def pct(x):
    return f"{abs(x) * 100:.1f}%"


def pct0(x):
    return f"{abs(x) * 100:.0f}%"


def won(v):
    """천 달러 단위 반올림 → '22만 3천 달러'."""
    t = int(round(v / 1000.0))
    man, cheon = divmod(t, 10)
    return f"{man}만 {cheon}천 달러" if cheon else f"{man}만 달러"


def ym_k(d):
    y, m, _ = d.split("-")
    return f"{int(y)}년 {int(m)}월"


def md_k(d):
    _, m, dd = d.split("-")
    return f"{int(m)}월 {int(dd)}일"


def st(k):
    return M[k]["stats"]


def vs(k):
    return st(k)["final"] / H["final"] - 1


def crash(yr):
    return next(c for c in A["crashes"] if c["peak"].startswith(yr))


def fills20(k):
    return F["fills_2020"][k]


cs_tp = F["cash_spells"]["tp10"][0]
cs_rsi = F["cash_spells"]["rsi30_70"][0]
yrs_tp = (date.fromisoformat(cs_tp["to"]) - date.fromisoformat(cs_tp["from"])).days / 365.25
nW = RL["windows"]
half = nW / 2
entry, sell = ["dca12", "dip10", "ladder"], ["tp10", "rsi30_70", "brk55_20", "sma200", "gc50_200", "mom12", "stop10"]
bm = RL["by_hold_mdd"]["0.40"]
beat = [k for k in R["main_summary"]["rows"] if k["beat_hold"]]
c20 = crash("2020")
d20 = (date.fromisoformat(c20["trough"]) - date.fromisoformat(c20["peak"])).days
stop_buy20 = [f for f in fills20("stop10") if f["side"] == "buy"][0]["date"]
days_after_bottom = (date.fromisoformat(stop_buy20) - date.fromisoformat(c20["trough"])).days
ms = R["main"]["stop10"]["stats"]

# (문장 번호, 대본 글자, 값 설명, 맞는지)
CHECKS = [
    (3, "10가지", "전략 수 len(main)-1", len(M) - 1 == 10),
    (4, "1만 달러", f"settings.capital = {R['settings']['capital']:,.0f}", R["settings"]["capital"] == 10000),
    (4, "1991년", f"settings.main[0] = {R['settings']['main'][0]}", R["settings"]["main"][0].startswith("1991")),
    (4, "32년", f"stats.years = {H['years']}", int(H["years"]) == 32),
    (7, "12번", f"dca12 매수 {st('dca12')['buys']}번", st("dca12")["buys"] == 12),
    (8, "0.1%", f"settings.cost = {R['settings']['cost']}", R["settings"]["cost"] == 0.001),
    (10, "1991년 1월", R["settings"]["main"][0], ym_k(R["settings"]["main"][0]) == "1991년 1월"),
    (10, "2023년 6월", R["settings"]["main"][1], ym_k(R["settings"]["main"][1]) == "2023년 6월"),
    (11, pct(F["dca12"]["index_1991_change"]), f"facts.dca12.index_1991_change = {F['dca12']['index_1991_change']:.5f}", True),
    (12, pct(F["dca12"]["avg_cost_vs_first_day"]), f"facts.dca12.avg_cost_vs_first_day = {F['dca12']['avg_cost_vs_first_day']:.5f}", True),
    (14, "2009년 3월", f"hold mdd_date = {H['mdd_date']}", ym_k(H["mdd_date"]) == "2009년 3월"),
    (14, pct(H["mdd"]), f"hold mdd = {H['mdd']:.5f} · dca12 mdd = {st('dca12')['mdd']:.5f}", abs(H["mdd"] - st("dca12")["mdd"]) < 5e-4),
    (15, won(st("dca12")["final"]), f"dca12 final = {st('dca12')['final']:,.0f}", True),
    (15, won(H["final"]), f"hold final = {H['final']:,.0f}", True),
    (16, pct(vs("dca12")), f"dca12 vs hold = {vs('dca12'):+.5f}", vs("dca12") < 0),
    (19, "1990년 마지막 날", "anim dip10Start.date = 1990-12-31 (시작일 전 거래일)", True),
    (19, "10.5%", "anim dip10Start.drop = 330.22 / 368.95 − 1", f"{abs(330.22 / 368.95 - 1) * 100:.1f}%" == "10.5%"),
    (22, "271번", f"rolling_10y.windows = {nW}", nW == 271),
    (23, f"{RL['dip10']['wins']}번", "rolling_10y.dip10.wins", True),
    (23, f"{RL['dip10']['ties']}번", "rolling_10y.dip10.ties", True),
    (23, f"{nW - RL['dip10']['wins'] - RL['dip10']['ties']}번", "windows − wins − ties", True),
    (24, pct(F["worst_best_10y_start"]["dip10"]["worst"]), f"facts.worst_best_10y_start.dip10.worst (시작 {F['worst_best_10y_start']['dip10']['worst_start']})", True),
    (28, "절반", f"ladder 첫 매수 몫 = {F['ladder']['buys'][0]['share_of_start']}", F["ladder"]["buys"][0]["share_of_start"] == 0.5),
    (29, "2001년", f"ladder 남은 매수 = {F['ladder']['buys'][1]['date']}, {F['ladder']['buys'][2]['date']}", F["ladder"]["buys"][1]["date"].startswith("2001")),
    (30, f"{F['ladder']['tr_growth_start_to_3rd_buy']:.1f}배", f"facts.ladder.tr_growth_start_to_3rd_buy = {F['ladder']['tr_growth_start_to_3rd_buy']:.4f}", True),
    (31, won(st("ladder")["final"]), f"ladder final = {st('ladder')['final']:,.0f}", True),
    (31, pct(vs("ladder")), f"ladder vs hold = {vs('ladder'):+.5f}", vs("ladder") < 0),
    (34, f"{st('tp10')['sells']}번 매도", f"tp10 sells = {st('tp10')['sells']}", True),
    (34, f"{st('tp10')['round_trips']}번 모두 이익", f"tp10 win_rate = {st('tp10')['win_rate']}", st("tp10")["win_rate"] == 1.0),
    (35, "1991년 2월", f"facts.cash_spells.tp10[0].from = {cs_tp['from']}", ym_k(cs_tp["from"]) == "1991년 2월"),
    (36, "1997년 10월", f"facts.cash_spells.tp10[0].to = {cs_tp['to']}", ym_k(cs_tp["to"]) == "1997년 10월"),
    (36, "6년 8개월", f"{cs_tp['calendar_days']}일 = {yrs_tp:.3f}년", int(yrs_tp) == 6 and int((yrs_tp - 6) * 12) == 8),
    (38, pct(st("tp10")["mdd"]), f"tp10 mdd = {st('tp10')['mdd']:.5f}", True),
    (39, won(st("tp10")["final"]), f"tp10 final = {st('tp10')['final']:,.0f}", True),
    (39, pct(vs("tp10")), f"tp10 vs hold = {vs('tp10'):+.5f}", vs("tp10") < 0),
    (43, "1994년 3월", f"rsi 첫 매수 = {M['rsi30_70']['fills'][0]['date']}", ym_k(M["rsi30_70"]["fills"][0]["date"]) == "1994년 3월"),
    (43, "3년 넘게", f"facts.cash_spells.rsi30_70[0] = {cs_rsi['calendar_days']}일", cs_rsi["calendar_days"] > 3 * 365.25),
    (44, f"{st('rsi30_70')['round_trips']}번", "rsi round_trips", True),
    (44, pct0(st("rsi30_70")["win_rate"]), f"rsi win_rate = {st('rsi30_70')['win_rate']:.4f}", True),
    (44, pct0(st("rsi30_70")["exposure"]), f"rsi exposure = {st('rsi30_70')['exposure']:.4f}", True),
    (45, pct(st("rsi30_70")["mdd"]), f"rsi mdd = {st('rsi30_70')['mdd']:.5f}", True),
    (46, won(st("rsi30_70")["final"]), f"rsi final = {st('rsi30_70')['final']:,.0f}", True),
    (46, pct(vs("rsi30_70")), f"rsi vs hold = {vs('rsi30_70'):+.5f}", vs("rsi30_70") < 0),
    (51, f"{st('brk55_20')['buys']}번 사고", "brk buys", True),
    (51, f"{st('brk55_20')['sells']}번 팔았는데", "brk sells", True),
    (51, pct0(st("brk55_20")["win_rate"]), f"brk win_rate = {st('brk55_20')['win_rate']:.4f}", True),
    (53, pct(st("brk55_20")["mdd"]), f"brk mdd = {st('brk55_20')['mdd']:.5f}", True),
    (54, won(st("brk55_20")["final"]), f"brk final = {st('brk55_20')['final']:,.0f}", True),
    (54, pct(vs("brk55_20")), f"brk vs hold = {vs('brk55_20'):+.5f}", vs("brk55_20") < 0),
    (58, pct(crash("2000")["strategies"]["sma200"]["drop"]), "crashes[2000].sma200.drop", True),
    (58, pct(crash("2007")["strategies"]["sma200"]["drop"]), "crashes[2007].sma200.drop", True),
    (59, pct(crash("2000")["hold_drop"]), f"crashes[2000] 관망 {crash('2000')['peak']}→{crash('2000')['trough']}", True),
    (59, pct(crash("2007")["hold_drop"]), f"crashes[2007] 관망 {crash('2007')['peak']}→{crash('2007')['trough']}", True),
    (60, "2009년 3월", f"leads.sma200.max_date = {A['leads']['sma200']['max_date']}", ym_k(A["leads"]["sma200"]["max_date"]) == "2009년 3월"),
    (60, f"{A['leads']['sma200']['max_ratio']:.2f}배", "leads.sma200.max_ratio", True),
    (61, f"{st('sma200')['buys'] + st('sma200')['sells']}번", "sma200 buys + sells", True),
    (62, won(st("sma200")["final"]), f"sma200 final = {st('sma200')['final']:,.0f}", True),
    (62, pct(vs("sma200")), f"sma200 vs hold = {vs('sma200'):+.5f}", vs("sma200") < 0),
    (63, pct(st("sma200")["mdd"]), f"sma200 mdd = {st('sma200')['mdd']:.5f}", True),
    (63, pct(H["mdd"]), "hold mdd", True),
    (66, pct(crash("2007")["strategies"]["gc50_200"]["drop"]), "crashes[2007].gc50_200.drop", True),
    (67, f"{A['leads']['gc50_200']['max_ratio']:.2f}배", f"leads.gc50_200.max_ratio ({A['leads']['gc50_200']['max_date']})", True),
    (68, "한 달", f"crashes[2020] {c20['peak']}→{c20['trough']} = {d20}일", 28 <= d20 <= 35),
    (69, md_k(fills20("gc50_200")[0]["date"]), "facts.fills_2020.gc50_200[0] (매도)", fills20("gc50_200")[0]["side"] == "sell"),
    (69, md_k(fills20("gc50_200")[1]["date"]), "facts.fills_2020.gc50_200[1] (매수)", fills20("gc50_200")[1]["side"] == "buy"),
    (70, ym_k(A["leads"]["gc50_200"]["last_ahead"]), "leads.gc50_200.last_ahead", True),
    (71, pct(st("gc50_200")["mdd"]), f"gc mdd = {st('gc50_200')['mdd']:.5f} ({st('gc50_200')['mdd_date']})", st("gc50_200")["mdd_date"].startswith("2020")),
    (72, won(st("gc50_200")["final"]), f"gc final = {st('gc50_200')['final']:,.0f}", True),
    (72, pct(vs("gc50_200")), f"gc vs hold = {vs('gc50_200'):+.5f}", vs("gc50_200") < 0),
    (76, f"{A['leads']['mom12']['max_ratio']:.2f}배", f"leads.mom12.max_ratio ({A['leads']['mom12']['max_date']})", True),
    (77, md_k(fills20("mom12")[0]["date"]), "facts.fills_2020.mom12[0] (매도)", fills20("mom12")[0]["side"] == "sell"),
    (77, md_k(fills20("mom12")[1]["date"]), "facts.fills_2020.mom12[1] (매수)", fills20("mom12")[1]["side"] == "buy"),
    (78, ym_k(A["leads"]["mom12"]["last_ahead"]), "leads.mom12.last_ahead", True),
    (78, won(st("mom12")["final"]), f"mom12 final = {st('mom12')['final']:,.0f}", True),
    (79, pct(vs("mom12")), f"mom12 vs hold = {vs('mom12'):+.5f}", vs("mom12") < 0),
    (79, pct(st("mom12")["mdd"]), f"mom12 mdd = {st('mom12')['mdd']:.5f}", True),
    (83, pct(crash("2000")["strategies"]["stop10"]["drop"]), "crashes[2000].stop10.drop", True),
    (83, pct(crash("2007")["strategies"]["stop10"]["drop"]), "crashes[2007].stop10.drop", True),
    (84, "절반쯤", f"{crash('2000')['strategies']['stop10']['drop'] / crash('2000')['hold_drop']:.2f} · {crash('2007')['strategies']['stop10']['drop'] / crash('2007')['hold_drop']:.2f}",
     all(0.4 <= crash(y)["strategies"]["stop10"]["drop"] / crash(y)["hold_drop"] <= 0.6 for y in ("2000", "2007"))),
    (85, md_k(fills20("stop10")[0]["date"]), "facts.fills_2020.stop10[0] (매도)", fills20("stop10")[0]["side"] == "sell"),
    (85, "사흘", f"매수 {stop_buy20} − 바닥 {c20['trough']} = {days_after_bottom}일", days_after_bottom == 3),
    (85, md_k(stop_buy20), "facts.fills_2020.stop10 (매수)", True),
    (86, pct(crash("2022")["strategies"]["stop10"]["drop"]), "crashes[2022].stop10.drop", True),
    (86, pct(crash("2022")["hold_drop"]), "crashes[2022] 관망", crash("2022")["strategies"]["stop10"]["drop"] < crash("2022")["hold_drop"]),
    (87, "2003년", f"stop10 mdd_date = {ms['mdd_date']}", ms["mdd_date"].startswith("2003")),
    (87, pct(ms["mdd"]), f"stop10 mdd = {ms['mdd']:.5f}", True),
    (88, won(ms["final"]), f"stop10 final = {ms['final']:,.0f}", True),
    (88, pct(vs("stop10")), f"stop10 vs hold = {vs('stop10'):+.5f}", vs("stop10") > 0),
    (90, "손절 하나", f"main_summary.beat = {R['main_summary']['beat']} ({[k['key'] for k in beat]})", [k["key"] for k in beat] == ["stop10"]),
    (91, "8개", "관망보다 적은 전략 수", sum(1 for k in R["main_summary"]["rows"] if k["final"] < H["final"] * (1 - 1e-9)) == 8),
    (91, "저점 매수는 같았고", f"dip10 vs hold = {vs('dip10'):+.9f}", abs(vs("dip10")) < 1e-9),
    (93, "2013년 7월", f"rolling_10y.last_start = {RL['last_start']}", ym_k(RL["last_start"]) == "2013년 7월"),
    (94, "271번", "rolling_10y.windows", nW == 271),
    (95, "세 가지", f"절반({half}) 넘게 이긴 전략 = {[k for k in sell + entry if RL[k]['wins'] > half]}", sum(RL[k]["wins"] > half for k in entry + sell) == 3),
    (96, f"손절 {RL['stop10']['wins']}번", "rolling_10y.stop10.wins", True),
    (96, f"골든 크로스 {RL['gc50_200']['wins']}번", "rolling_10y.gc50_200.wins", True),
    (96, f"모멘텀 {RL['mom12']['wins']}번", "rolling_10y.mom12.wins", True),
    (97, "40%", "by_hold_mdd 문턱 0.40", True),
    (98, f"{bm['big_windows']}번", "by_hold_mdd.0.40.big_windows", True),
    (98, f"손절이 {bm['big']['stop10']}번", "by_hold_mdd.0.40.big.stop10", True),
    (99, f"{bm['small_windows']}번", "by_hold_mdd.0.40.small_windows", True),
    (99, "한 번도", f"by_hold_mdd.0.40.small.stop10 = {bm['small']['stop10']}", bm["small"]["stop10"] == 0),
    (100, f"{bm['small']['gc50_200']}번뿐", f"small.gc50_200 = {bm['small']['gc50_200']} · small.mom12 = {bm['small']['mom12']}", bm["small"]["gc50_200"] == bm["small"]["mom12"]),
    (102, pct(H["mdd"]), "hold mdd", True),
    (103, f"10개 중 {R['main_summary']['mdd_better']}개", "main_summary.mdd_better", True),
    (105, "2026년 2월", f"sp500_daily last = {R['data']['sp500_daily']['last']}", ym_k(R["data"]["sp500_daily"]["last"]) == "2026년 2월"),
    (105, "손절 하나", f"cost0.beat = {R['sensitivity']['cost0']['beat']} · price_only_2026.beat = {R['sensitivity']['price_only_2026']['beat']}",
     R["sensitivity"]["cost0"]["beat"] == 1 and R["sensitivity"]["price_only_2026"]["beat"] == 1
     and [r["key"] for r in R["sensitivity"]["cost0"]["rows"] if r["beat_hold"]] == ["stop10"]
     and [r["key"] for r in R["sensitivity"]["price_only_2026"]["rows"] if r["beat_hold"]] == ["stop10"]),
    (106, "2018년", "tbill_sub 기간 1991-01-02~2018-11-30 (Fama-French RF 마지막 달)", True),
    (106, "세 가지", f"tbill_sub_cashRF.beat = {R['sensitivity']['tbill_sub_cashRF']['beat']}", R["sensitivity"]["tbill_sub_cashRF"]["beat"] == 3),
    (107, f"{R['sensitivity']['nasdaq_price_2000_2018']['beat']}개", "nasdaq_price_2000_2018.beat", True),
    (108, "10개 모두", f"nasdaq_price_2003_2018.beat = {R['sensitivity']['nasdaq_price_2003_2018']['beat']}", R["sensitivity"]["nasdaq_price_2003_2018"]["beat"] == 0),
    (115, "3개", f"사는 규칙 wins = {[RL[k]['wins'] for k in entry]} (모두 < {half})", all(RL[k]["wins"] < half for k in entry)),
    (116, "4개", f"파는 규칙 중 절반 못 넘은 것 = {[k for k in sell if RL[k]['wins'] < half]}", sum(RL[k]["wins"] < half for k in sell) == 4),
    (117, "3개", f"파는 규칙 중 절반 넘은 것: 큰 하락 기간에서 이긴 몫 = {[round(bm['big'][k] / RL[k]['wins'], 3) for k in sell if RL[k]['wins'] > half]}",
     all(bm["big"][k] / RL[k]["wins"] >= 0.95 for k in sell if RL[k]["wins"] > half)),
    (119, "10개 중 8개", "관망보다 적은 전략 수 (본 실험)", sum(1 for k in R["main_summary"]["rows"] if k["final"] < H["final"] * (1 - 1e-9)) == 8),
    (120, "7개 가운데 6개", f"파는 규칙 중 본 실험에서 관망보다 적은 것 = {[k for k in sell if st(k)['final'] < H['final']]}", sum(st(k)["final"] < H["final"] for k in sell) == 6),
    (123, pct(H["mdd"]), f"hold mdd = {H['mdd']:.5f} ({H['mdd_date']})", H["mdd_date"].startswith("2009")),
]


def main():
    rows, bad = [], 0
    for n, s, src, ok in CHECKS:
        sent = SENT[n - 1]
        inside = s in sent
        good = bool(ok) and inside
        bad += not good
        rows.append(f"| {n} | `{s}` | {src} | {'✅' if good else '❌' + ('' if inside else ' (문장에 없음)')} |")
    L = ["# eonje-maesu-2026-10 숫자 확인표 (자동 — `backtest/check_numbers.py`)", "",
         f"버전: v1.0 — 2026-10-16 — 대본 {len(SENT)}문장 · `results.json` (`run.py` {R['version']}, {R['created']}). 다시 만들기: `cd backtest && python3 check_numbers.py`", "",
         "- 대본 숫자가 코드 결과에서 나왔는지 (stock/guides/concept.md 2번). 말로 읽는 금액은 천 달러 단위 반올림, %는 소수 한 자리(승률·주식 비율은 정수).",
         "- 화면 숫자는 `backtest/anim.js` (`anim_data.py` 가 results.json 과 assert 로 맞춤).", "",
         f"**결과: {len(CHECKS) - bad} / {len(CHECKS)} ✅**", "", "| 문장 | 대본 글자 | 결과 파일 값 | 확인 |", "|---:|---|---|---|"] + rows
    (HERE.parent / "checklist.md").write_text("\n".join(L) + "\n", "utf-8")
    print(f"[CHECK] numbers={len(CHECKS)} ok={len(CHECKS) - bad} bad={bad} → ../checklist.md")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
