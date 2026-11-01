#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-11-01 — 1편(대본 v8) 영상 그래프용 실제 종가 선 (사용자 지시 2026-11-01 "1편만 영상 관련 소스 만들어봐 이미지 chatgpt 말할거 알려주고").
#   숫자 출처는 stock/topics/precheck/longform_items.py v2.1 (nasdaq_1_v21) 과 같은 자료·같은 날짜 — 여기서는 화면 선 모양만 뽑음.
#   점 = 5거래일마다 (끝 날은 꼭 넣음) · 값 = 시작 날 1 기준 (배당 포함 수정 종가 · 달러 기준 변화율 — 환율 뺌).
#   출력: video/episodes/ppalli-test-2026-11/series.js (window.SERIES) — 장면 코드가 읽음. 실행: python3 -B stock/source/ppalli-test-2026-11/calc/series.py
#   ※ 연구·교육용 — 투자 권유가 아님.
import json
import logging
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "stock/topics/precheck"))
import longform_items as L  # noqa: E402

logging.basicConfig(level=logging.INFO, format="[%(stage)s] %(message)s")
log = logging.getLogger("series")
NOW = "2026-10-27"


def pts(ser, a, b, step=5):
    i, j = ser.i(a), ser.i(b)
    idx = list(range(i, j + 1, step))
    if idx[-1] != j:
        idx.append(j)
    base = float(ser.v[i])
    return [[ser.k[k], round(float(ser.v[k]) / base, 4)] for k in idx]


def main():
    S = L.load()
    R = lambda s: L.Ser(s, L.rd(L.HERE / "data" / f"{s}.csv", "adjclose"))
    q, A, M, B, cash = R("QQQ"), S["ARKK"], R("SMCI"), R("MSTR"), S["CASH"]
    d1, d3, dSell, dBack, dS, d4, d5 = "2021-02-12", "2022-06-13", "2022-06-16", "2023-12-13", "2024-03-13", "2024-08-28", "2024-11-20"
    out = {"made": "2026-11-01", "now": NOW, "src": "series.py v1.0 · longform_items v2.1 자료"}
    out["intro_qqq"] = pts(q, d1, NOW)
    out["i1_arkk"], out["i1_qqq"] = pts(A, d1, NOW), pts(q, d1, NOW)
    out["i2_allin"] = pts(q, d1, "2022-12-30")
    out["i2_keep"] = [[d, round(0.8 * v + 0.2 * (1 + cash.chg(d1, d)), 4)] for d, v in out["i2_allin"]]
    out["i3_hold"] = pts(q, d3, NOW)
    # 김씨: 06-16 모두 매도 → 국채 현금 → 2023-12-13 다시 매수
    p = []
    for d, v in out["i3_hold"]:
        if d <= dSell:
            p.append([d, v])
        elif d <= dBack:
            p.append([d, round((1 + q.chg(d3, dSell)) * (1 + cash.chg(dSell, d)), 4)])
        else:
            p.append([d, round((1 + q.chg(d3, dSell)) * (1 + cash.chg(dSell, dBack)) * (1 + q.chg(dBack, d)), 4)])
    out["i3_panic"] = p
    out["i4_smci"], out["i4_qqq"] = pts(M, d4, NOW), pts(q, d4, NOW)
    out["i4_buy"] = pts(M, dS, d4)            # 산 날부터 그날까지 (−63%)
    out["i5_mstr"], out["i5_qqq"] = pts(B, d5, NOW), pts(q, d5, NOW)
    out["i5_prior"] = pts(B, "2023-11-20", d5)
    # 김씨 길(오답만) · 정답 길 — 1억 원 기준 (만 원)
    kim, good = [], []
    for d, _ in pts(q, d1, NOW):
        if d <= dSell:
            w = 10000 * (1 + A.chg(d1, d))
        elif d <= dBack:
            w = 10000 * (1 + A.chg(d1, dSell)) * (1 + cash.chg(dSell, d))
        elif d <= dS:
            w = 10000 * (1 + A.chg(d1, dSell)) * (1 + cash.chg(dSell, dBack)) * (1 + q.chg(dBack, d))
        elif d <= d5:
            w = 10000 * (1 + A.chg(d1, dSell)) * (1 + cash.chg(dSell, dBack)) * (1 + q.chg(dBack, dS)) * (1 + M.chg(dS, d))
        else:
            w = 10000 * (1 + A.chg(d1, dSell)) * (1 + cash.chg(dSell, dBack)) * (1 + q.chg(dBack, dS)) * (1 + M.chg(dS, d5)) * (1 + B.chg(d5, d))
        kim.append([d, round(w)])
        good.append([d, round(8000 * (1 + q.chg(d1, d)) + 2000 * (1 + cash.chg(d1, d)))])
    out["end_kim"], out["end_good"] = kim, good
    log.info("keys=%s kim_end=%s good_end=%s i1_arkk_min=%s i3_hold_end=%s i3_panic_end=%s", list(out), kim[-1], good[-1],
             min(v for _, v in out["i1_arkk"]), out["i3_hold"][-1], out["i3_panic"][-1], extra={"stage": "SERIES"})
    dst = ROOT / "video/episodes/ppalli-test-2026-11/series.js"
    dst.write_text("// 자동 생성 — stock/source/ppalli-test-2026-11/calc/series.py v1.0 (손으로 고치지 않음)\nwindow.SERIES = " + json.dumps(out, ensure_ascii=False) + ";\n", "utf-8")
    log.info("file=%s bytes=%d", dst.relative_to(ROOT), dst.stat().st_size, extra={"stage": "DONE"})


if __name__ == "__main__":
    main()
