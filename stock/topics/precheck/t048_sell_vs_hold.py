#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-29 — 최초. T048 '폭락 경고 믿고 팔았다면?'을 문제형으로 바꾸며 (사용자 지시 2026-10-29 "1번 평가판은 사실형으로 하지 말고
#          문제나 테스트형으로 좀 해봐 왜 다 사실형이야") — 그날 판 사람(1년 동안 미국 단기 국채 이자)과 버틴 사람(S&P 500 배당 포함)의 1년 뒤를 견줌.
#          precheck.py T048 은 '1년 뒤 S&P 500 이 경고한 날보다 높았나'만 셈 → 판 사람의 이자까지 넣어도 버틴 쪽이 이겼는지 따로 확인.
# 자료: stock/source/timing-test-2026-10/calc/sp500tr_daily.csv (^SP500TR) · irx_daily.csv (^IRX 13주 국채 연 %) — 매수 시기 편 calc 가 받은 것 그대로.
# 현금: 날마다 그날 ^IRX 금리로 (다음 거래일까지 날수 ÷ 365) 복리. 1년 뒤 = 같은 달·날 또는 그 뒤 첫 거래일.
# 실행: python3 -B stock/topics/precheck/t048_sell_vs_hold.py → precheck/t048_sell_vs_hold.json
# ※ 연구·교육용 — 투자 권유가 아님.
import bisect
import csv
import json
import logging
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
CALC = HERE.parent.parent / "source" / "timing-test-2026-10" / "calc"
WARN = {"2021-01-22": "그랜섬 '거품' 경고 보도", "2022-06-01": "다이먼 '경제 허리케인'", "2022-06-03": "머스크 '아주 나쁜 예감'",
        "2023-01-31": "버리 '팔아라'(1월 31일 기준)", "2023-08-14": "버리 하락 베팅 공시"}
logging.basicConfig(level=logging.INFO, format="[%(stage)s] %(message)s")
log = logging.getLogger("t048")


def load(name):
    with (CALC / name).open(encoding="utf-8") as f:
        rows = [r for r in csv.reader(f) if r and not r[0].startswith("#")]
    out = [(r[0], float(r[1])) for r in rows[1:] if r[1]]
    log.info("source=%s rows=%d range=%s~%s", name, len(out), out[0][0], out[-1][0], extra={"stage": "LOAD"})
    return out


def main():
    tr, ir = load("sp500tr_daily.csv"), dict(load("irx_daily.csv"))
    ds = [d for d, _ in tr]
    res = []
    for d0, who in WARN.items():
        i = bisect.bisect_left(ds, d0)
        j = bisect.bisect_left(ds, str(int(d0[:4]) + 1) + d0[4:])
        hold = 10000 * tr[j][1] / tr[i][1]
        cash, last = 10000.0, None
        for k in range(i, j):
            r = ir.get(ds[k], last)
            last = r
            cash *= (1 + r / 100) ** ((date.fromisoformat(ds[k + 1]) - date.fromisoformat(ds[k])).days / 365)
        res.append({"date": d0, "who": who, "start": ds[i], "end": ds[j], "hold_10k": round(hold), "sell_cash_10k": round(cash),
                    "winner": "버틴 사람" if hold > cash else "판 사람", "gap": round(hold - cash)})
        log.info("date=%s end=%s hold=%.0f sell=%.0f gap=%+.0f", d0, ds[j], hold, cash, hold - cash, extra={"stage": "CALC"})
    (HERE / "t048_sell_vs_hold.json").write_text(json.dumps({"tool": "t048_sell_vs_hold.py v1.0", "results": res}, ensure_ascii=False, indent=1), "utf-8")
    log.info("hold_wins=%d/%d min_gap=%d", sum(r["winner"] == "버틴 사람" for r in res), len(res), min(r["gap"] for r in res), extra={"stage": "DONE"})


if __name__ == "__main__":
    main()
