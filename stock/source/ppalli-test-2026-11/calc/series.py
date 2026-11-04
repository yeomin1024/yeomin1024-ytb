#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v2.1 — 2026-11-04 — 대본 v16: 선택 2 그래프 = 그날 바로 뒤 S&P 500 −10% (i2_near) · 계산 json longform_items_2026-11-04.
# (v2.0) — 2026-11-03 — 1편 대본 v12 (S&P 500 · 업스타트 · 현금 · 2025 기준대로 · C3.ai · 아이온큐) 영상 그래프 선
#   (사용자 지시 2026-11-03 "1편만 영상 만들어봐 각 요소가 어색하지 않은 위치에 있어야 하니까 위치 배치 정확히 정해서 해").
#   숫자 출처 = stock/topics/precheck/longform_items.py sp_1_v23 (longform_items_2026-11-02.json 'sp_1편_v2.3') — 같은 자료·같은 날짜·같은 규칙.
#   여기서는 화면 선 모양만 뽑고, 끝 값이 계산 json 과 같은지 맞춰 봄 (다르면 끝 코드 1).
#   점 = 거래일마다(짧은 창) 또는 3·5거래일마다(끝 날은 꼭 넣음) · 값 = 시작 날 1 기준 또는 만 원 (달러 기준 변화율 — 환율·세금·수수료 뺌).
#   출력: video/episodes/ppalli-test-2026-11/series.js (window.SERIES). 실행: python3 -B stock/source/ppalli-test-2026-11/calc/series.py
# 이전 v1.0 — 2026-11-01 — 대본 v8 (QQQ·ARKK·SMCI·MSTR).
#   ※ 연구·교육용 — 투자 권유가 아님.
import json
import logging
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "stock/topics/precheck"))
import longform_items as L  # noqa: E402

logging.basicConfig(level=logging.INFO, format="[%(stage)s] %(message)s")
log = logging.getLogger("series")
NOW = "2026-10-27"
CALC_JSON = ROOT / "stock/topics/precheck/longform_items_2026-11-04.json"


def main():
    t0 = time.time()
    S = L.load()
    for sym in ("UPST", "AI", "IONQ"):
        S[sym] = L.Ser(sym, L.rd(L.HERE / "data" / f"{sym}.csv", "adjclose"))
    tr, spx, cash, U, C, I = S["TR"], S["SPX"], S["CASH"], S["UPST"], S["AI"], S["IONQ"]
    # 날짜 = sp_1_v23 과 같은 방법
    d1, dPk = "2023-08-01", "2025-02-19"
    dSig = spx.first_below(dPk, -0.10)
    dCut = spx.k[spx.i(dSig) + 1]
    dP = spx.low(dPk, "2025-12-31")[1]
    dB = spx.back(dPk, spx.at(dPk), after=dP)
    dTip, d4, d5 = "2025-07-01", "2025-08-11", "2025-10-13"
    log.info("d1=%s peak=%s sig=%s cut=%s low=%s back=%s tip=%s d4=%s d5=%s now=%s", d1, dPk, dSig, dCut, dP, dB, dTip, d4, d5, NOW, extra={"stage": "DATES"})

    days = lambda a, b: [d for d in tr.k if a <= d <= b]
    cashv = lambda a, d: 1 + cash.chg(a, d)

    def thin(rows, step):
        if step <= 1:
            return rows
        keep = rows[::step]
        if keep[-1] != rows[-1]:
            keep.append(rows[-1])
        return keep

    def ladder_daily(a_sig, cut, end, steps=(0.05, 0.10, 0.15)):
        """sp_1_v23.ladder 와 같은 규칙 — 날마다 값(신호 날 1)과 매수한 날."""
        u, c, part, cut_px, todo, out, buys = 1 / tr.at(a_sig), 0.0, None, None, list(steps), [], []
        for d in days(a_sig, end):
            if d == cut and cut_px is None:
                c = u * 0.5 * tr.at(d); u *= 0.5; part = c / len(steps); cut_px = spx.at(d)
            elif cut_px is not None and c > 1e-12:
                while todo and spx.at(d) <= cut_px * (1 - todo[0]):
                    amt = min(part, c); u += amt / tr.at(d); c -= amt; buys.append((d, f"-{todo[0]:.0%}")); todo.pop(0)
                if todo and spx.at(d) >= spx.at(dPk) and c > 1e-12:
                    u += c / tr.at(d); buys.append((d, "최고가 회복")); c = 0.0; todo = []
            out.append([d, u * tr.at(d) + c])
            if c > 0:
                c *= 1 + cash.chg(d, tr.k[min(tr.i(d) + 1, len(tr.k) - 1)])
        return out, buys

    lad, lad_buys = ladder_daily(dSig, dCut, NOW)
    LAD = dict(lad)

    # 김씨 (오답만) — 만 원
    w_dP = 10000 * (1 + U.chg(d1, dP))
    w_dB = w_dP * cashv(dP, dB)
    w_tip = w_dB * (1 + tr.chg(dB, dTip))
    wC5 = w_tip / 2 * (1 + C.chg(dTip, d5)); wQ5 = w_tip / 2 * (1 + tr.chg(dTip, d5))
    wI5 = (wC5 + wQ5) / 2; wQ5b = wQ5 - wI5

    def kim(d):
        if d <= dP:
            return 10000 * (1 + U.chg(d1, d))
        if d <= dB:
            return w_dP * cashv(dP, d)
        if d <= dTip:
            return w_dB * (1 + tr.chg(dB, d))
        if d <= d5:
            return w_tip / 2 * (1 + C.chg(dTip, d)) + w_tip / 2 * (1 + tr.chg(dTip, d))
        return wC5 * (1 + C.chg(d5, d)) + wI5 * (1 + I.chg(d5, d)) + wQ5b * (1 + tr.chg(d5, d))

    # 정답만 — 만 원 (7천 S&P 500 + 3천 국채 → ③ 기준대로 → 07-01 주식 몫 절반 C3.ai → 08-11 매도 → 10-13 계좌의 10% 아이온큐)
    q_sig = 7000 * (1 + tr.chg(d1, dSig))
    g_q_tip = q_sig * round(LAD[tr.day(dTip)], 4)          # sp_1_v23 은 ladder(…)[0] 를 소수 4자리로 반올림해 곱함 — 같은 값을 내려고 똑같이
    gC4 = g_q_tip / 2 * (1 + C.chg(dTip, d4))
    gQ5 = g_q_tip / 2 * (1 + tr.chg(dTip, d5)); gC5 = gC4 * cashv(d4, d5)
    acct5 = gQ5 + gC5 + 3000 * cashv(d1, d5)
    gI5 = 0.1 * acct5; gQ5b = gQ5 - gI5

    def good(d):
        c3 = 3000 * cashv(d1, d)
        if d <= dSig:
            return 7000 * (1 + tr.chg(d1, d)) + c3
        if d <= dTip:
            return q_sig * LAD[d] + c3
        if d <= d4:
            return g_q_tip / 2 * (1 + tr.chg(dTip, d)) + g_q_tip / 2 * (1 + C.chg(dTip, d)) + c3
        if d <= d5:
            return g_q_tip / 2 * (1 + tr.chg(dTip, d)) + gC4 * cashv(d4, d) + c3
        return gQ5b * (1 + tr.chg(d5, d)) + gI5 * (1 + I.chg(d5, d)) + gC5 * cashv(d5, d) + c3

    norm = lambda s, a, b, step: thin([[d, round(s.at(d) / s.at(a), 4)] for d in days(a, b)], step)
    out = {"made": "2026-11-03", "now": NOW, "src": "series.py v2.0 · longform_items sp_1_v23 자료",
           "dates": {"d1": d1, "peak": dPk, "sig": dSig, "cut": dCut, "low": dP, "back": dB, "tip": dTip, "d4": d4, "d5": d5, "ladder_buys": lad_buys}}
    # 도입 — S&P 500(배당 포함) vs 김씨 (1 = 1억 원)
    out["intro_sp"] = norm(tr, d1, NOW, 5)
    out["intro_kim"] = thin([[d, round(kim(d) / 10000, 4)] for d in days(d1, NOW)], 5)
    # ① 업스타트 vs S&P 500 (그날 1)
    out["i1_upst"], out["i1_sp"] = norm(U, d1, NOW, 5), norm(tr, d1, NOW, 5)
    # ① 앞 — 업스타트 그날까지 1년 (선택 1 카드 안 작은 그래프: 1년 3배 · 올해 5배 · 하루 35%)
    u0 = "2022-08-01"
    out["i1_pre"] = [[d, round(U.at(d) / U.at(u0), 4)] for d in [x for x in U.k if u0 <= x <= d1]]
    # ⑤ 앞 — 아이온큐 그날까지 1년 (선택 5 카드 안 작은 그래프: 1년 7배)
    q0 = "2024-10-11"
    out["i5_pre"] = [[d, round(I.at(d) / I.at(q0), 4)] for d in [x for x in I.k if q0 <= x <= d5]]
    # ② v2.1 (대본 v16) — 그날(d1) 바로 뒤 하락: S&P 500 가격(그날 1) 2023-07-03 ~ 2023-12-29 — 석 달도 안 돼 −10%
    out["i2_near"] = [[d, round(spx.at(d) / spx.at(d1), 4)] for d in days("2023-07-03", "2023-12-29")]
    # ② 2025 봄 하락 — 모두 투자(만 원) · 현금 3천만 원(만 원)
    w0, w1 = "2025-01-21", "2025-04-30"
    out["i2_allin"] = [[d, round(10000 * (1 + tr.chg(d1, d)))] for d in days(w0, w1)]
    out["i2_cash"] = [[d, round(3000 * cashv(d1, d))] for d in days(w0, w1)]
    # ③ 2025 — S&P 500 가격(고점 1) · 그대로(신호 날 1) · 김씨(그때그때) · 기준대로
    w3a, w3b = "2025-01-21", "2025-08-29"
    out["i3_spx"] = [[d, round(spx.at(d) / spx.at(dPk), 4)] for d in days(w3a, w3b)]
    hold = lambda d: 1 + tr.chg(dSig, d)
    panic = lambda d: hold(d) if d <= dP else (hold(dP) * cashv(dP, d) if d <= dB else hold(dP) * cashv(dP, dB) * (1 + tr.chg(dB, d)))
    out["i3_hold"] = [[d, round(hold(d), 4)] for d in days(dSig, w3b)]
    out["i3_panic"] = [[d, round(panic(d), 4)] for d in days(dSig, w3b)]
    out["i3_rule"] = [[d, round(LAD[d], 4)] for d in days(dSig, w3b)]
    # ④ C3.ai — 07-01(지인 추천 매수)부터 · 08-11 뒤 버팀(그날 1) vs 매도(국채)
    out["i4_ai_pre"] = [[d, round(C.at(d) / C.at(d4), 4)] for d in days(dTip, d4)]
    out["i4_hold"] = norm(C, d4, NOW, 3)
    out["i4_sell"] = thin([[d, round(cashv(d4, d), 4)] for d in days(d4, NOW)], 3)
    # ⑤ 아이온큐 — 계좌의 절반 vs 10% (나머지 S&P 500, 그날 1)
    mix = lambda w, d: w * (1 + I.chg(d5, d)) + (1 - w) * (1 + tr.chg(d5, d))
    out["i5_half"] = thin([[d, round(mix(0.5, d), 4)] for d in days(d5, NOW)], 2)
    out["i5_ten"] = thin([[d, round(mix(0.1, d), 4)] for d in days(d5, NOW)], 2)
    # 끝 — 김씨 길 · 정답 길 (만 원)
    out["end_kim"] = thin([[d, round(kim(d))] for d in days(d1, NOW)], 5)
    out["end_good"] = thin([[d, round(good(d))] for d in days(d1, NOW)], 5)

    # 계산 json 과 맞춰 보기
    J = json.loads(CALC_JSON.read_text("utf-8"))["sp_1편_v2.3"]
    pc = lambda x: f"{(x - 1) * 100:+.1f}%"
    chk = [
        ("intro_sp", pc(out["intro_sp"][-1][1]), J["김씨_경로"]["sp_tr_same"]),
        ("end_kim", round(kim(NOW)), J["김씨_경로"]["wrong_now_manwon"]),
        ("end_good", round(good(NOW)), J["김씨_경로"]["correct_now_manwon"]),
        ("i1_upst_now", pc(out["i1_upst"][-1][1]), J["1_남따라"]["upst_now"]),
        ("i2_drop", round(10000 * (1 + tr.chg(d1, dPk))) - round(10000 * (1 + tr.chg(d1, dP))), J["2_현금"]["drop_manwon"]),
        ("i3_rule_now", pc(LAD[tr.day(NOW)]), J["3_기준"]["ladder_now"]),
        ("i3_panic_now", pc(panic(NOW)), J["3_기준"]["panic_now"]),
        ("i3_hold_now", pc(hold(NOW)), J["3_기준"]["hold_now"]),
        ("i4_ai_now", pc(out["i4_hold"][-1][1]), J["4_손절"]["ai_now"]),
        ("i5_half_now", pc(out["i5_half"][-1][1]), J["5_분배"]["half_now"]),
        ("i5_ten_now", pc(out["i5_ten"][-1][1]), J["5_분배"]["ten_now"]),
        ("i2_near_low", pc(min(v for d, v in out["i2_near"] if d >= d1)), J["2_현금"]["near_spx_low"]),
        ("i1_pre_1y", round(out["i1_pre"][-1][1], 2), J["1_남따라"]["upst_prior_1y"]),
        ("i5_pre_1y", round(out["i5_pre"][-1][1], 1), J["5_분배"]["ionq_prior_1y"]),
    ]
    bad = [c for c in chk if c[1] != c[2]]
    for name, got, want in chk:
        log.info("check=%s got=%s calc=%s ok=%s", name, got, want, got == want, extra={"stage": "CHECK"})
    if bad:
        log.info("mismatch=%s next=계산 규칙을 sp_1_v23 과 다시 맞춤", bad, extra={"stage": "FAIL"})
        return 1
    log.info("keys=%s points=%d", list(out), sum(len(v) for v in out.values() if isinstance(v, list)), extra={"stage": "SERIES"})
    dst = ROOT / "video/episodes/ppalli-test-2026-11/series.js"
    dst.write_text("// 자동 생성 — stock/source/ppalli-test-2026-11/calc/series.py v2.0 (손으로 고치지 않음)\nwindow.SERIES = " + json.dumps(out, ensure_ascii=False) + ";\n", "utf-8")
    log.info("file=%s bytes=%d sec=%.1f", dst.relative_to(ROOT), dst.stat().st_size, time.time() - t0, extra={"stage": "DONE"})
    return 0


if __name__ == "__main__":
    sys.exit(main())
