#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-30 — 최초. 실제 날짜마다 '그날 한 번에 매수' vs '12개월 나눠 매수' (2년 · S&P 500 배당 포함 · 아직 안 넣은 돈은 국채 이자)
#          + 그날 하루 변동(^GSPC) · 가장 낮았던 날 · '원금 −20% 에서 겁나서 전부 매도(그 뒤 국채)'했다면 (롱폼 2편 '고점에 매수해서 저점에 매도').
#          매수 시기 편 2단계 다시 짜기(사용자 평가 2026-10-30 "매수하기 좋은 케이스와 나쁜 케이스를 섞어서 문제를 내야지")와 쇼츠·롱폼 요약본
#          (사용자 지시 2026-10-30 "… 쇼츠 내용과 연결되는 구체적인 내용들을 롱폼 요약본으로 작성해봐") 의 숫자 — scratchpad 에서 옮김.
# 안정 = 2년 끝에 국채(^IRX)보다 더 남고, 그사이 원금보다 20% 넘게 준 적 없음 (risk.py 와 같은 뜻) · 이긴 쪽 = 둘 다 같은 안정 여부면 끝 값이 큰 쪽, 아니면 안정인 쪽.
# 자료: stock/source/timing-test-2026-10/calc/sp500tr_daily.csv · irx_daily.csv (매수 시기 편 calc 가 받은 것).
# 날짜는 사람이 고른 사건 날(최고가 · 바닥 · 하루 큰 폭락) 17번 — 규칙으로 넓히지 않음 (그날 상황만으로는 어느 쪽인지 갈린다는 사례).
#   최고가는 사건마다 하루 (2021-12-27 은 2022-01-03 과 같은 고점이라 뺌 — 같은 사건을 두 번 세지 않게).
# 실행: python3 -B stock/topics/precheck/timing_cases.py → precheck/timing_cases_<날짜>.json
# ※ 연구·교육용 — 투자 권유가 아님.
import bisect
import csv
import json
import logging
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
CALC = HERE.parent.parent / "source" / "timing-test-2026-10" / "calc"
VERSION = "v1.0"
CASES = [("2000-03-24", "닷컴 꼭대기", "최고가"), ("2002-10-09", "닷컴 바닥", "바닥"), ("2007-10-09", "금융위기 전 최고가", "최고가"),
         ("2008-09-29", "리먼 뒤 하루 −8.8%", "폭락 날"), ("2008-10-10", "금융위기 공포 극단", "폭락 날"), ("2009-03-09", "금융위기 바닥", "바닥"),
         ("2011-08-08", "미국 신용등급 강등 다음 날", "폭락 날"), ("2015-08-24", "중국발 급락", "폭락 날"), ("2018-09-20", "2018 최고가", "최고가"),
         ("2018-12-24", "2018 크리스마스 급락", "폭락 날"), ("2020-02-19", "코로나 전 최고가", "최고가"), ("2020-03-09", "코로나 첫 서킷브레이커", "폭락 날"),
         ("2020-03-23", "코로나 바닥", "바닥"), ("2022-01-03", "2022 첫날 최고가", "최고가"),
         ("2022-06-13", "2022 하락장 −20% 들어선 날", "폭락 날"), ("2022-10-12", "2022 바닥", "바닥"), ("2024-01-19", "2024 첫 최고가", "최고가")]
logging.basicConfig(level=logging.INFO, format="[%(stage)s] %(message)s")
log = logging.getLogger("timing_cases")


def load(name):
    with (CALC / name).open(encoding="utf-8") as f:
        rows = [r for r in csv.reader(f) if r and not r[0].startswith("#")]
    out = [(r[0], float(r[1])) for r in rows[1:] if r[1]]
    log.info("source=%s rows=%d range=%s~%s", name, len(out), out[0][0], out[-1][0], extra={"stage": "LOAD"})
    return out


def main():
    tr = load("sp500tr_daily.csv")
    ir = dict(load("irx_daily.csv"))
    px = load("gspc_daily.csv")
    pd_ = [d for d, _ in px]
    ds = [d for d, _ in tr]

    def grow(k):
        r = ir.get(ds[k])
        j = k
        while r is None and j > 0:
            j -= 1
            r = ir.get(ds[j])
        return (1 + r / 100) ** ((date.fromisoformat(ds[k + 1]) - date.fromisoformat(ds[k])).days / 365)

    def run(i, j, months, panic=False):
        """→ (끝 값, 가장 낮았던 값, 그날) · panic = 원금의 80% 아래로 처음 내려간 날 전부 매도하고 남은 기간 국채 (더 매수하지 않음)."""
        y, m, dd = int(ds[i][:4]), int(ds[i][5:7]), ds[i][8:]
        buys = {bisect.bisect_left(ds, f"{y + (m - 1 + k) // 12:04d}-{(m - 1 + k) % 12 + 1:02d}-{dd}") for k in range(months)}
        cash, units, worst, wday, sold = 1.0, 0.0, 1.0, ds[i], None
        for k in range(i, j + 1):
            if k in buys and sold is None:
                units += (1.0 / months) / tr[k][1]
                cash -= 1.0 / months
            v = cash + units * tr[k][1]
            if v < worst:
                worst, wday = v, ds[k]
            if panic and sold is None and v < 0.8:
                cash, units, sold = v, 0.0, ds[k]
            if k < j:
                cash *= grow(k)
        return cash + units * tr[j][1], worst, wday, sold

    rows = []
    for d0, name, kind in CASES:
        i = bisect.bisect_left(ds, d0)
        j = bisect.bisect_left(ds, str(int(ds[i][:4]) + 2) + ds[i][4:])
        if j >= len(ds):
            log.warning("date=%s note=2년 자료 없음 — 건너뜀", d0, extra={"stage": "CASE"})
            continue
        c = 1.0
        for k in range(i, j):
            c *= grow(k)
        a, wa, wda, _ = run(i, j, 1)
        b, wb, _, _ = run(i, j, 12)
        ap, _, _, asold = run(i, j, 1, panic=True)
        bp, _, _, bsold = run(i, j, 12, panic=True)
        q = bisect.bisect_left(pd_, ds[i])
        day = px[q][1] / px[q - 1][1] - 1 if pd_[q] == ds[i] and q > 0 else None
        peak = max(v for _, v in px[:q + 1])
        sa, sb = a > c and wa >= 0.8, b > c and wb >= 0.8
        win = ("한 번에" if a > b else "나눠") if sa == sb else ("한 번에" if sa else "나눠")
        rows.append({"date": d0, "name": name, "kind": kind, "end": ds[j], "lump_10k": round(a * 1e4), "lump_worst": f"{(wa - 1) * 100:+.0f}%", "lump_stable": sa,
                     "split_10k": round(b * 1e4), "split_worst": f"{(wb - 1) * 100:+.0f}%", "split_stable": sb, "tbill_10k": round(c * 1e4), "winner": win,
                     "day_chg": None if day is None else f"{day * 100:+.1f}%", "from_peak": f"{(px[q][1] / peak - 1) * 100:+.0f}%", "lump_worst_day": wda,
                     "panic_rule": "원금 −20% 아래로 처음 내려간 날 전부 매도 → 남은 기간 국채", "lump_panic_10k": round(ap * 1e4), "lump_panic_day": asold,
                     "split_panic_10k": round(bp * 1e4), "split_panic_day": bsold})
        log.info("date=%s kind=%s day=%s from_peak=%s lump=%.0f(%+.0f%% %s) split=%.0f(%+.0f%%) winner=%s panic_lump=%.0f(%s) panic_split=%.0f(%s)", d0, kind,
                 rows[-1]["day_chg"], rows[-1]["from_peak"], a * 1e4, (wa - 1) * 100, wda, b * 1e4, (wb - 1) * 100, win, ap * 1e4, asold, bp * 1e4, bsold, extra={"stage": "CASE"})
    by = {}
    for r in rows:
        k = by.setdefault(r["kind"], {"한 번에": 0, "나눠": 0, "n": 0, "lump_below_80": 0, "split_below_80": 0})
        k[r["winner"]] += 1
        k["n"] += 1
        k["lump_below_80"] += r["lump_panic_day"] is not None
        k["split_below_80"] += r["split_panic_day"] is not None
    out = HERE / f"timing_cases_{date.today().isoformat()}.json"
    out.write_text(json.dumps({"tool": f"timing_cases.py {VERSION}", "rule": "2년 · 안정 = 국채보다 더 + 원금 20% 넘게 안 줄어듦 · below_80 = 2년 안에 원금의 80% 아래로 내려간 번 수", "by_kind": by, "cases": rows},
                              ensure_ascii=False, indent=1), "utf-8")
    log.info("by_kind=%s file=%s", json.dumps(by, ensure_ascii=False), out.name, extra={"stage": "DONE"})


if __name__ == "__main__":
    main()
