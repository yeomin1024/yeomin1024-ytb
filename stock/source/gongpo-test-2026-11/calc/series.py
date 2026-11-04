#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-11-04 — 계산 json 을 longform_ep4 v1.1(longform_ep4_2026-11-04.json)로 · 알려진 차이(KNOWN) 없앰 → 끝 값 검사(CHECK c1_sold_end) + c1_sold_label "+58%".
# VERSION: v1.0 — 2026-11-04 — 4편(정씨 · 폭락장 계획 매수) 대본 v17 영상 그래프 선 · 공포 지수 바늘 값 · 통계 점.
#   숫자 출처 = stock/topics/precheck/longform_ep4.py v1.0 (longform_ep4_2026-11-02.json '4편_v9') — 같은 자료·같은 날짜·같은 규칙.
#   ① longform_ep4.ep4() 를 다시 돌려 계산 json 과 모든 값이 같은지 먼저 봄 (다르면 끝 코드 1).
#   ② 화면 선 모양만 뽑고, 선의 끝·가장 낮은 값이 계산 값과 같은지 맞춰 봄 (다르면 끝 코드 1).
#   ③ 알려진 차이 1개 (KNOWN) — 계산 json '1_매도후재매수.sold_to_end' 0.4513 (대본 문장 25 '45%')은 주식 수 감소(−8%)를
#      두 번 곱한 값: (TR d1/TR d1b) × (TR 끝/TR d1b) − 1. 판 돈을 3월 28일에 모두 다시 넣은 길은 TR 끝/TR d1b × 국채 이자 − 1 = +58%.
#      화면 선은 바른 길(+58%)로 그리고 끝 숫자는 쓰지 않음 — 대본·계산을 고치면 장면 파일 C1_SOLD_LABEL 한 줄만 바꿈. 끝 코드 0 (경고만).
#   점 = 거래일마다(짧은 창) 또는 2·3·5거래일마다(끝 날은 꼭 넣음) · 값 = 기준 날 1 (달러 기준 변화율 — 환율·세금·수수료 뺌).
#   출력: video/episodes/gongpo-test-2026-11/series.js (window.SERIES). 실행: python3 -B stock/source/gongpo-test-2026-11/calc/series.py
#   ※ 연구·교육용 — 투자 권유가 아님.
import json
import logging
import sys
import time
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
PRE = ROOT / "stock/topics/precheck"
sys.path.insert(0, str(PRE))
import longform_items as L  # noqa: E402
import longform_ep4 as E  # noqa: E402

VERSION = "v1.1"
log = logging.getLogger("series_ep4")
CALC_JSON = PRE / "longform_ep4_2026-11-04.json"   # v1.1 sold_to_end 고친 계산 (longform_ep4 v1.1)
DST = ROOT / "video/episodes/gongpo-test-2026-11/series.js"
WAR = "2022-02-24"                       # 러시아 우크라이나 침공 (대본 문장 22 '열하루 뒤')


def info(stage, msg, *a):
    log.info(msg, *a, extra={"stage": stage})


def same(a, b, path=""):
    """계산 json 과 다시 돌린 값 비교 → 다른 곳 목록."""
    if isinstance(a, dict) and isinstance(b, dict):
        out = []
        for k in set(a) | set(b):
            out += same(a.get(k), b.get(k), f"{path}.{k}")
        return out
    if isinstance(a, (list, tuple)) and isinstance(b, (list, tuple)):
        if len(a) != len(b):
            return [(path, f"len {len(a)}", f"len {len(b)}")]
        out = []
        for i, (x, y) in enumerate(zip(a, b)):
            out += same(x, y, f"{path}[{i}]")
        return out
    if isinstance(a, float) or isinstance(b, float):
        return [] if a is not None and b is not None and abs(a - b) < 1e-9 else [(path, a, b)]
    return [] if a == b else [(path, a, b)]


def main():
    t0 = time.time()
    S = L.load()
    for sym in ("MRNA", "NFLX"):
        S[sym] = L.Ser(sym, L.rd(PRE / "data" / f"{sym}.csv", "adjclose"))
    tr, spx, cash, vix, M, NF = S["TR"], S["SPX"], S["CASH"], S["VIX"], S["MRNA"], S["NFLX"]

    # ① 계산 모듈 다시 돌림 → json 과 같은가
    R = json.loads(json.dumps(E.ep4(S), ensure_ascii=False))
    J = json.loads(CALC_JSON.read_text("utf-8"))["4편_v9"]
    diff = same(R, J)
    info("RECALC", "keys=%d diff=%d", len(R), len(diff))
    if diff:
        info("FAIL", "recalc_diff=%s next=longform_ep4.py 와 자료를 다시 맞춤", diff[:8])
        return 1
    D, PK, END = J["날짜"], J["기간"]["start"], J["기간"]["end"]
    d1, d1b, d2, d4, d5, jld, lod = D["d1"], D["d1b"], D["d2"], D["d4"], D["d5"], D["june_low"], D["bottom"]
    nxt = J["4_반등"]["next_step_day"]
    peak = spx.at(PK)
    info("DATES", "peak=%s d1=%s d1b=%s d2=%s june_low=%s d4=%s d5=%s next=%s bottom=%s end=%s", PK, d1, d1b, d2, jld, d4, d5, nxt, lod, END)

    days = lambda a, b: [d for d in tr.k if a <= d <= b]

    def thin(rows, step=1, must=()):
        """step 거래일마다 + 끝 날 + must 날(가장 높은·낮은 날 — 화면 꼬리표가 선 위에 오게)."""
        if step <= 1:
            return rows
        keep = {i for i in range(0, len(rows), step)} | {len(rows) - 1} | {i for i, r in enumerate(rows) if r[0] in must}
        return [rows[i] for i in sorted(keep)]

    r4 = lambda x: round(float(x), 4)
    pk_n = lambda a, b, step=1: thin([[d, r4(spx.at(d) / peak)] for d in days(a, b)], step)       # S&P 500 가격 ÷ 최고가(2022-01-03)
    base_n = lambda s, d0, a, b, step=1: thin([[d, r4(s.at(d) / s.at(d0))] for d in days(a, b)], step)

    # ── 정씨 경로 · 정답 경로 (longform_ep4.ep4 와 같은 규칙 — 날마다 값, 1 = 1억 원)
    LR = E.LOAN_RATE

    def jeong_path():
        idx, stk, c, res_, debt, last, out = 0.6 / tr.at(PK), 0.0, 0.0, 0.4, 0.0, PK, []
        for k in days(PK, END):
            g = cash.at(k) / cash.at(last)
            c *= g
            res_ *= g
            debt *= (1 + LR) ** ((date.fromisoformat(k) - date.fromisoformat(last)).days / 365)
            last = k
            if k == d1:
                c += idx * tr.at(k); idx = 0.0
            if k == d1b:
                debt = c; idx = 2 * c / tr.at(k); c = 0.0
            if k == d2:
                half = idx * tr.at(k) / 2; idx /= 2; stk = half / M.at(k)
            if k == d4:
                idx += res_ / tr.at(k); res_ = 0.0
            if k == d5:
                c += idx * tr.at(k) - debt; idx, debt = 0.0, 0.0
            out.append([k, idx * tr.at(k) + stk * M.at(k) + c + res_ - debt])
        return out

    def good_path():
        steps = J["정답"]["steps"]
        idx, c, last, out = 0.6 / tr.at(PK), 0.4, PK, []
        for k in days(PK, END):
            c *= cash.at(k) / cash.at(last)
            last = k
            if k in steps:
                idx += 0.1 / tr.at(k); c -= 0.1
            out.append([k, idx * tr.at(k) + c])
        return out

    jp, gp = jeong_path(), good_path()
    JP = dict(jp)
    out = {"made": "2026-11-04", "src": f"series.py {VERSION} · longform_ep4.py {E.VERSION} 자료", "end": END,
           "dates": {"peak": PK, "war": WAR, "d1": d1, "d1b": d1b, "d2": d2, "june_low": jld, "d4": d4, "d5": d5, "next": nxt, "bottom": lod,
                     "plan_steps": J["정답"]["steps"], "war_days": (date.fromisoformat(d1) - date.fromisoformat(WAR)).days},
           "vix": {k: round(vix.at(v), 2) for k, v in (("peak", PK), ("d1", d1), ("d1b", d1b), ("d2", d2), ("d4", d4), ("d5", d5))},
           "vix_avg": D["vix_avg_1990"],
           "plan_levels": [0.90, 0.85, 0.80, 0.75]}
    # 도입 — S&P 500 가격(최고가 1) vs 정씨 계좌(1 = 1억 원) · 정리 — 계획대로(정답) vs 정씨
    out["intro_idx"] = pk_n(PK, END, 5)
    out["intro_jeong"] = thin([[d, r4(v)] for d, v in jp], 5)
    out["good"] = thin([[d, r4(v)] for d, v in gp], 5)
    out["jeong_marks"] = [[d, r4(JP[d])] for d in (d1, d1b, d2, d4, d5)]
    # ① 앞 — 최고가 → 2022-03-07 (−12%) · 매도/재매수 근처 확대 · 4년 길 (그대로 vs 매도 후 재매수 — 바른 길)
    out["c1_pre"] = pk_n(PK, d1)
    out["c1_zoom"] = pk_n("2022-02-14", "2022-04-14")
    out["c1_hold"] = base_n(tr, d1, d1, END, 5)
    sold = [[d, r4(cash.at(d) / cash.at(d1))] for d in days(d1, d1b)]
    reb = cash.at(d1b) / cash.at(d1)
    sold += [[d, r4(reb * tr.at(d) / tr.at(d1b))] for d in days(d1b, END)][1:]
    out["c1_sold"] = thin(sold, 5)
    # 1990 이후 공포 지수 35 넘은 첫날 17번 — 재매수 값이 판 값보다 높았나
    out["vix17"] = [[e[0][:4], e[2] > 0] for e in J["1_역사"]["events"]]
    # ② 앞 — 03-07 → 03-28 (+9%) · 빚 1:1 (빌린 날 1) vs 빚 없음 · 담보 비율 (주식 값 ÷ 빌린 돈과 이자)
    out["c2_pre"] = [[d, r4(spx.at(d) / spx.at(d1))] for d in days(d1, d1b)]
    w2 = "2022-12-30"
    debt = lambda k: (1 + LR) ** ((date.fromisoformat(k) - date.fromisoformat(d1b)).days / 365)
    out["c2_own"] = base_n(tr, d1b, d1b, w2)
    out["c2_lev"] = thin([[d, r4(2 * tr.at(d) / tr.at(d1b) - debt(d))] for d in days(d1b, w2)])
    out["c2_ratio"] = thin([[d, r4(2 * tr.at(d) / tr.at(d1b) / debt(d))] for d in days(d1b, w2)])
    out["call"] = E.CALL
    out["bears4"] = [[b["first_20"][:4], bool(b["call"])] for b in J["2_역사"]["bears"]]
    # ③ 앞 — 최고가 → 05-09 (−17%) · 모더나 1년 최고가 → 05-09 (−72%) · 그 뒤 모더나 vs 지수(배당 포함) · 넷플릭스
    out["c3_pre"] = pk_n(PK, d2)
    mpk = J["3_모더나"]["mrna_peak_day"]
    out["c3_mrna_pre"] = thin([[d, r4(M.at(d) / M.at(mpk))] for d in [x for x in M.k if mpk <= x <= d2]], 2)
    out["c3_mrna"] = thin([[d, r4(M.at(d) / M.at(d2))] for d in [x for x in M.k if d2 <= x <= END]], 3, (J["3_모더나"]["mrna_max_day"], J["3_모더나"]["mrna_worst_day"]))
    out["c3_idx"] = thin(base_n(tr, d2, d2, END), 3, (J["3_모더나"]["idx_worst_day"],))
    out["nflx"] = {"from_peak": J["3_모더나"]["nflx_from_peak"], "to_end": J["3_모더나"]["nflx_to_end"]}
    # 지금 S&P 500 회사 중 그날 1년 최고가보다 가장 많이 빠진 24곳 — 그 뒤 2년 안 30% 넘게 더 빠졌나 (longform_ep4 3_역사 와 같은 규칙)
    y2, y1 = f"{int(d2[:4]) + 2}{d2[4:]}", f"{int(d2[:4]) - 1}{d2[4:]}"
    syms24 = []
    for sym in J["3_역사"]["syms"]:
        s = E.bulk_ser(sym)
        syms24.append([sym, bool(s.low(d2, y2)[0] < -0.30)])
    out["syms24"] = syms24
    # ④ 앞 — 6월 바닥 → 08-12 (+17%) · 6월 ~ 12월 창 (한 번에 vs 다음 가격 −25%)
    out["c4_pre"] = pk_n("2022-05-02", d4)
    out["c4_win"] = pk_n("2022-06-01", "2022-12-30")
    out["rallies10"] = [[r["day"][:4], r["new_low_after"]] for r in J["4_역사"]["rallies"]]
    # ⑤ 앞 — 6월 바닥 → 09-26 (바닥 다시 깸) · 그 뒤 보유(배당 포함) vs 매도·국채
    out["c5_pre"] = pk_n("2022-06-01", d5)
    out["c5_hold"] = thin(base_n(tr, d5, d5, END), 3, (J["5_새바닥"]["hold_worst_day"],))
    out["c5_cash"] = thin([[d, r4(cash.at(d) / cash.at(d5))] for d in days(d5, END)], 3)
    out["cases3"] = [[c["new_low"][:4], c["hold_4y"], c["cash_4y"]] for c in J["5_역사"]["cases"]]
    # 화면 숫자 (선이 아닌 값 — 계산 json 과 맞춰 봄)
    out["nums"] = {"j_d1": J["정씨"]["events"][0][2],   # 정씨 ① 판 날 지수 몫 (계산 json 값 그대로 — 아래에서 다시 계산과 맞춰 봄)
                    "shares": r4(spx.at(d1) / spx.at(d1b) - 1), "c2_spx_low": r4(spx.at(lod) / spx.at(d1b) - 1),
                   "c4_rally": r4(spx.at(d4) / spx.at(jld) - 1), "c4_allin_end": r4(tr.chg(d4, END)), "c4_plan_end": r4(tr.chg(nxt, END))}

    # ② 선 끝·가장 낮은 값 ↔ 계산 json
    mn = lambda rows: min(v for _, v in rows)
    lev_all = [2 * tr.at(d) / tr.at(d1b) - debt(d) for d in days(d1b, END)]
    wday = days(d1b, END)[lev_all.index(min(lev_all))]
    chk = [
        ("intro_jeong_end", r4(jp[-1][1]), J["정씨"]["end_value"]),
        ("intro_jeong_worst", r4(min(v for _, v in jp) - 1), J["정씨"]["worst"]),
        ("good_end", r4(gp[-1][1]), J["정답"]["end_value"]),
        ("intro_idx_end", r4(out["intro_idx"][-1][1] - 1), J["기간"]["spx_chg"]),
        ("jeong_d1", r4(0.6 * tr.at(d1) / tr.at(PK)), J["정씨"]["events"][0][2]),
        ("c1_pre_end", r4(out["c1_pre"][-1][1] - 1), D["d1_spx_dd"]),
        ("c1_zoom_rebuy", r4(spx.at(d1b) / spx.at(d1) - 1), J["1_매도후재매수"]["rebuy_higher"]),
        ("c1_hold_end", r4(out["c1_hold"][-1][1] - 1), J["1_매도후재매수"]["hold_to_end"]),
        ("vix17", (len(out["vix17"]), sum(1 for _, x in out["vix17"] if x)), (J["1_역사"]["n"], J["1_역사"]["rebuy_higher"])),
        ("c2_pre_end", r4(out["c2_pre"][-1][1] - 1), J["2_빚"]["rally_from_d1"]),
        ("c2_lev_worst", r4(min(lev_all) - 1), J["2_빚"]["equity_worst"]),
        ("c2_lev_worst_day", wday, J["2_빚"]["equity_worst_day"]),
        ("c2_lev_win", r4(mn(out["c2_lev"]) - 1) if wday <= w2 else None, J["2_빚"]["equity_worst"]),
        ("c2_own_worst", r4(mn(out["c2_own"]) - 1), J["2_빚"]["own_worst"]),
        ("c2_ratio_min", r4(mn(out["c2_ratio"])), J["2_빚"]["call_ratio_at_worst"]),
        ("bears4", (len(out["bears4"]), sum(1 for _, x in out["bears4"] if x)), (J["2_역사"]["n"], J["2_역사"]["calls"])),
        ("c3_pre_end", r4(out["c3_pre"][-1][1] - 1), D["d2_dd"]),
        ("c3_mrna_pre_end", r4(out["c3_mrna_pre"][-1][1] - 1), J["3_모더나"]["mrna_from_peak"]),
        ("c3_mrna_end", r4(out["c3_mrna"][-1][1] - 1), J["3_모더나"]["mrna_to_end"]),
        ("c3_mrna_max", r4(max(v for d, v in out["c3_mrna"] if d <= "2023-01-31") - 1), J["3_모더나"]["mrna_max_after"]),
        ("c3_idx_end", r4(out["c3_idx"][-1][1] - 1), J["3_모더나"]["idx_to_end"]),
        ("c3_idx_worst", r4(mn(out["c3_idx"]) - 1), J["3_모더나"]["idx_worst"]),
        ("syms24", (len(syms24), sum(1 for _, x in syms24 if x)), (J["3_역사"]["n"], J["3_역사"]["worst_more_than_30"])),
        ("c4_pre_rally", r4(spx.at(d4) / spx.at(jld) - 1), J["4_반등"]["from_june_low"]),
        ("c4_to_bottom", r4(spx.at(lod) / spx.at(d4) - 1), J["4_반등"]["all_in_to_bottom"]),
        ("c4_next_cheaper", r4(spx.at(nxt) / spx.at(d4) - 1), J["4_반등"]["next_step_cheaper"]),
        ("c4_next_dd", r4(dict(out["c4_win"])[nxt] - 1), J["4_반등"]["next_step_dd"]),
        ("c4_allin_end", r4(tr.chg(d4, END)), J["4_반등"]["all_in_to_end"]),
        ("c4_plan_end", r4(tr.chg(nxt, END)), J["4_반등"]["plan_to_end"]),
        ("rallies10", (len(out["rallies10"]), sum(1 for _, x in out["rallies10"] if x)), (J["4_역사"]["n"], J["4_역사"]["new_low"])),
        ("c5_pre_end", r4(out["c5_pre"][-1][1] - 1), J["5_새바닥"]["dd"]),
        ("c5_hold_end", r4(out["c5_hold"][-1][1] - 1), J["5_새바닥"]["hold_to_end"]),
        ("c5_hold_worst", r4(mn(out["c5_hold"]) - 1), J["5_새바닥"]["hold_worst"]),
        ("c5_cash_end", r4(out["c5_cash"][-1][1] - 1), J["5_새바닥"]["sell_to_end"]),
        ("cases3", (len(out["cases3"]), sum(1 for _, h, c in out["cases3"] if h > c)), (J["5_역사"]["n"], J["5_역사"]["hold_more_4y"])),
        ("vix_d1", out["vix"]["d1"], D["d1_vix"]),
        ("vix_d1b", out["vix"]["d1b"], D["d1b_vix"]),
        ("war_days", out["dates"]["war_days"], 11),
        ("nums.j_d1", abs(0.6 * tr.at(d1) / tr.at(PK) - out["nums"]["j_d1"]) < 1e-4, True),
        ("nums.shares", out["nums"]["shares"], r4(J["1_매도후재매수"]["shares_kept"] - 1)),
        ("nums.c2_spx_low", out["nums"]["c2_spx_low"], J["1_매도후재매수"]["later_low_from_rebuy"]),
        ("nums.c4_rally", out["nums"]["c4_rally"], J["4_반등"]["from_june_low"]),
        ("nums.c4_allin_end", out["nums"]["c4_allin_end"], J["4_반등"]["all_in_to_end"]),
        ("nums.c4_plan_end", out["nums"]["c4_plan_end"], J["4_반등"]["plan_to_end"]),
    ]
    bad = [c for c in chk if c[1] != c[2]]
    for name, got, want in chk:
        info("CHECK", "check=%s got=%s calc=%s ok=%s", name, got, want, got == want)
    # ③ (v1.1) 다시 산 길 끝 값 = 계산 json sold_to_end (longform_ep4 v1.1 에서 고침 — 옛 0.4513 은 주식 수 감소를 두 번 곱함)
    sold_ok = r4(out["c1_sold"][-1][1] - 1)
    sold_json = J["1_매도후재매수"]["sold_to_end"]
    info("CHECK", "check=c1_sold_end got=%s calc=%s ok=%s (선 = 국채 이자 없이 · 계산 = 국채 이자 포함 — 0.002 안)", sold_ok, sold_json, abs(sold_ok - sold_json) <= 0.002)
    if abs(sold_ok - sold_json) > 0.002:
        bad.append(("c1_sold_end", sold_ok, sold_json))
    out["c1_sold_label"] = f"+{round(sold_json * 100)}%"
    if bad:
        info("FAIL", "mismatch=%s next=계산 규칙을 longform_ep4 와 다시 맞춤", bad)
        return 1
    info("SERIES", "keys=%s points=%d", list(out), sum(len(v) for v in out.values() if isinstance(v, list)))
    DST.parent.mkdir(parents=True, exist_ok=True)
    DST.write_text(f"// 자동 생성 — stock/source/gongpo-test-2026-11/calc/series.py {VERSION} (손으로 고치지 않음)\nwindow.SERIES = "
                   + json.dumps(out, ensure_ascii=False) + ";\n", "utf-8")
    info("DONE", "file=%s bytes=%d sec=%.1f", DST.relative_to(ROOT), DST.stat().st_size, time.time() - t0)
    return 0


if __name__ == "__main__":
    sys.exit(main())
