#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-11-04 — 2편(daebi-test-2026-11) 대본 v17 (이씨 · 상승장의 잘못된 '생각' 다섯 개) 영상 그래프 선·화면 숫자.
#   숫자 출처 = stock/topics/precheck/longform_ep2.py v1.0 (longform_ep2_2026-11-02.json) — 같은 자료·같은 날짜·같은 규칙(함수를 그대로 불러 씀).
#   여기서는 화면 선 모양과 화면에 쓰는 숫자 글(num — '−84%' 같은 꼴)만 뽑고, 끝 값이 계산 json 과 같은지 맞춰 봄 (다르면 끝 코드 1).
#   점 = 거래일마다(짧은 창) 또는 2·3·5거래일마다(끝 날은 꼭 넣음) · 값 = 시작 날 1 기준(또는 최고가 1 기준) — 달러 기준 변화율, 환율·세금·수수료 뺌.
#   출력: video/episodes/daebi-test-2026-11/series.js (window.SERIES). 실행: python3 -B stock/source/daebi-test-2026-11/calc/series.py
#   사용자 지시 2026-11-04 (quick_board 규칙 43 — 편마다 화면을 다르게, 숫자 화면은 그 편의 실제 계산으로만).
#   ※ 연구·교육용 — 투자 권유가 아님.
import json
import logging
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "stock/topics/precheck"))
import longform_ep2 as E2  # noqa: E402
import longform_items as L  # noqa: E402

VERSION = "v1.0"
logging.basicConfig(level=logging.INFO, format="[%(stage)s] %(message)s")
log = logging.getLogger("series")
CALC_JSON = ROOT / "stock/topics/precheck/longform_ep2_2026-11-02.json"
DST = ROOT / "video/episodes/daebi-test-2026-11/series.js"
ZM_PEAK = "2020-10-19"          # 줌 최고가 날 (longform_ep2 c3·c5 와 같음)


def info(stage, msg, *a):
    log.info(msg, *a, extra={"stage": stage})


def thin(rows, step, keep=()):
    """step 거래일마다 + 끝 날 + keep 날(가장 낮은 날·최고가 날 — 화면 점이 선 위에 정확히 오게)."""
    if step <= 1:
        return rows
    out = rows[::step]
    if out[-1] != rows[-1]:
        out.append(rows[-1])
    have = {r[0] for r in out}
    out += [r for r in rows if r[0] in set(keep) and r[0] not in have]
    return sorted(out, key=lambda r: r[0])


def pct(x, sign=True):
    """화면 글: −84% · +57% (반올림 — 대본의 '84%까지'·'50% 넘게' 와 같은 값)."""
    v = round(x * 100)
    return ("+" if v > 0 and sign else "−" if v < 0 else "") + f"{abs(v)}%"


def main():
    t0 = time.time()
    D1, D2, D3, D4, D5, END, NOW = E2.D1, E2.D2, E2.D3, E2.D4, E2.D5, E2.END, E2.NOW
    S = L.load()
    for sym in ("ZM", "PTON", "DIS", "META", "AMZN"):
        S[sym] = E2.ser(sym)
    tr, spx, zm, pt, dis, meta, amzn = S["TR"], S["SPX"], S["ZM"], S["PTON"], S["DIS"], S["META"], S["AMZN"]
    days = lambda s, a, b: [d for d in s.k if a <= d <= b]
    norm = lambda s, a, b, step, keep=(): thin([[d, round(s.at(d) / s.at(a), 4)] for d in days(s, a, b)], step, keep)
    info("DATES", "d1=%s d2=%s d3=%s d4=%s d5=%s end=%s now=%s zm_peak=%s", D1, D2, D3, D4, D5, END, NOW, ZM_PEAK)

    # 이씨 경로 (다섯 번 모두 오답) — longform_ep2.main 의 wv(d) 와 같은 규칙 (1억 원 = 1.0)
    acc_c2 = 1 + zm.chg(D1, D2)
    zm_part = 1.0 * (1 + zm.chg(D2, D3))

    def lee(d):
        if d < D2:
            return zm.at(d) / zm.at(D1)
        v = (acc_c2 - 1) * pt.at(d) / pt.at(D2)
        v += (zm.at(d) / zm.at(D2)) if d < D3 else zm_part * dis.at(d) / dis.at(D3)
        if d >= D4:
            v += (E2.DEBT * tr.at(d) / tr.at(D4) if d < D5 else E2.DEBT * (tr.at(D5) / tr.at(D4)) * zm.at(d) / zm.at(D5)) - E2.DEBT
        return v

    # 다섯 번 모두 정답 — longform_ep2 lee_right (90% S&P 500 배당 포함 + 10% 줌 그대로)
    right = lambda d: (1 - E2.KEEP_ZM) * (1 + tr.chg(D1, d)) + E2.KEEP_ZM * (1 + zm.chg(D1, d))

    out = {"made": "2026-11-04", "src": f"series.py {VERSION} · longform_ep2 {E2.VERSION} 자료",
           "dates": {"d1": D1, "d2": D2, "d3": D3, "d4": D4, "d5": D5, "end": END, "now": NOW, "zm_peak": ZM_PEAK}}
    # 도입 — S&P 500 가격(그날 1) · 이씨 계좌(1 = 1억 원)
    out["intro_sp"] = norm(spx, D1, END, 5)
    out["intro_lee"] = thin([[d, round(lee(d), 4)] for d in days(tr, D1, END)], 5)
    # ① 2020년 한 해 — 줌 · S&P 500 (2019-12-31 = 1) · 그 뒤 4년 줌 (그날 1)
    out["c1_zm_pre"] = norm(zm, "2019-12-31", D1, 2)
    out["c1_spx_pre"] = norm(spx, "2019-12-31", D1, 2)
    c1lo, c1lday = zm.low(D1, END)
    c3lo, c3lday = dis.low(D3, END)
    c5lo, c5lday = zm.low(D5, END)
    mlo, mday = meta.low(D4, "2022-12-30")
    alo, aday = amzn.low(D4, "2022-12-30")
    out["c1_wrong"] = norm(zm, D1, END, 5, (c1lday,))
    # ② 펠로톤 그날까지 1년 (2020-02-12 = 1) · 그 뒤 (그날 1)
    out["c2_pton_pre"] = norm(pt, "2020-02-12", D2, 2)
    out["c2_wrong"] = norm(pt, D2, END, 5, ("2022-12-30",))
    # ③ 줌 최고가부터 그날까지 (최고가 1) · 디즈니 1년 반 (2020-03-23 = 1) · 그 뒤 (그날 1) · 2022년 메타·아마존 (2021-12-31 = 1)
    out["c3_zm_fall"] = norm(zm, ZM_PEAK, D3, 2)
    out["c3_dis_pre"] = norm(dis, "2020-03-23", D3, 2)
    out["c3_wrong"] = norm(dis, D3, END, 5, (c3lday,))
    out["c3_meta"] = norm(meta, D4, "2022-12-30", 2, (mday,))
    out["c3_amzn"] = norm(amzn, D4, "2022-12-30", 2, (aday,))
    # ④ 2021년 S&P 500 (2020-12-31 = 1) + 그해 최고가를 새로 쓴 날 · 빌린 돈으로 산 지수(배당 포함, 그날 1)
    mx, rec21 = -1.0, []
    for d, v in zip(spx.k, spx.v):
        if v > mx:
            mx = float(v)
            if d[:4] == "2021":
                rec21.append(d)
    out["c4_spx2021"] = norm(spx, "2020-12-31", "2021-12-31", 1)
    out["c4_records"] = rec21
    lo4, lday4 = tr.low(D4, END)
    back4 = tr.back(D4, tr.at(D4), after=lday4)
    pk4 = spx.peak_before("2022-12-30")[0]
    out["c4_wrong"] = norm(tr, D4, END, 3, (pk4, lday4, back4))
    # ⑤ 줌 최고가부터 그날까지 (최고가 1) · 그 뒤 (그날 1) · 최고가부터 지금까지 (최고가 1)
    out["c5_zm_fall"] = norm(zm, ZM_PEAK, D5, 2)
    out["c5_wrong"] = norm(zm, D5, END, 5, (c5lday,))
    out["c5_zm_now"] = norm(zm, ZM_PEAK, NOW, 5)
    # 정리 — 이씨 길 · 다섯 번 모두 정답 길 (1 = 1억 원)
    out["end_lee"] = out["intro_lee"]
    out["end_right"] = thin([[d, round(right(d), 4)] for d in days(tr, D1, END)], 5)

    # 묶음 통계 (지금 S&P 500 종목 — 생존 편향은 결론 반대쪽, longform_ep2 survivorship)
    B = E2.bulk_all()
    w2 = E2.winners_2020(B, 2.0)
    rec = E2.records(spx)
    c2lo = pt.chg(D2, "2022-12-30")
    out["dates"].update({"c1_low": c1lday, "c3_low": c3lday, "c4_low": lday4, "c4_back": back4, "spx_peak": pk4, "c5_low": c5lday, "meta_low": mday, "amzn_low": aday})
    # 화면 글 (대본 숫자와 같은 반올림)
    acc0 = 100_000_000
    out["num"] = {
        "acc0": f"₩{acc0:,}", "lee_end": f"₩{round(lee(END) * acc0, -4):,.0f}", "lee_end_pct": pct(lee(END) - 1), "spx_4y": pct(spx.chg(D1, END)),
        "c1_zm": f"×{zm.at(D1) / zm.at('2019-12-31'):.2f}", "c1_spx": pct(spx.chg("2019-12-31", D1)), "c1_worst": pct(c1lo), "c1_end": pct(zm.chg(D1, END)),
        "c1_n2x": str(w2["n"]), "c1_half": str(w2["halved_by_2022"]),
        "c2_gain": pct(acc_c2 - 1), "c2_gain_won": f"₩{round((acc_c2 - 1) * acc0, -5):,.0f}", "c2_pton": f"×{pt.at(D2) / pt.at('2020-02-12'):.2f}",
        "c2_2022": pct(c2lo), "c2_end": pct(pt.chg(D2, END)), "c2_need": f"×{1 / (1 + pt.chg(D2, END)):.1f}",
        "c3_zm": pct(zm.at(D3) / zm.at(ZM_PEAK) - 1), "c3_dis": f"×{dis.at(D3) / dis.at('2020-03-23'):.2f}", "c3_worst": pct(c3lo), "c3_end": pct(dis.chg(D3, END)),
        "c3_meta": pct(mlo), "c3_amzn": pct(alo),
        "c4_rec21": str(len(rec21)), "c4_loan": f"₩{round(E2.DEBT * acc0):,}", "c4_worst": pct(lo4), "c4_months": f"{L.months(D4, back4):.1f}", "c4_years": f"{L.months(D4, back4) / 12:.1f}",
        "c4_days": str(rec["days"]), "c4_fell10": str(rec["fell_10pct_2y"]),
        "c5_zm": f"{round(zm.at(D5) / zm.at(ZM_PEAK) * 100)}%", "c5_worst": pct(c5lo), "c5_end": pct(zm.chg(D5, END)),
        "c5_need": f"×{zm.at(ZM_PEAK) / zm.at(D5):.2f}", "c5_now": f"{round(zm.at(NOW) / zm.at(ZM_PEAK) * 100)}%",
    }
    info("NUM", "%s", json.dumps(out["num"], ensure_ascii=False))

    # 계산 json 과 맞춰 보기 (json 은 소수 4자리 — 같은 반올림으로)
    J = json.loads(CALC_JSON.read_text("utf-8"))
    r = E2.r
    chk = [
        ("intro_sp_end", r(out["intro_sp"][-1][1] - 1), J["intro"]["spx_4y"]),
        ("intro_lee_end", r(lee(END)), J["lee_wrong"]["total_end"]),
        ("lee_worst", r(min(lee(d) for d in days(tr, D1, END)) - 1), J["lee_wrong"]["worst"]),
        ("c1_zm_2020", r(out["c1_zm_pre"][-1][1] - 1), J["c1"]["zm_2020"]),
        ("c1_spx_2020", r(out["c1_spx_pre"][-1][1] - 1), J["c1"]["spx_2020"]),
        ("c1_worst", r(c1lo), J["c1"]["wrong_zm"]["worst"]),
        ("c1_end", r(out["c1_wrong"][-1][1] - 1), J["c1"]["wrong_zm"]["to_end"]),
        ("c1_winners", (w2["n"], w2["halved_by_2022"]), (J["stat_winners_2020"]["2.0"]["n"], J["stat_winners_2020"]["2.0"]["halved_by_2022"])),
        ("c2_gain", r(acc_c2 - 1), J["c2"]["gain_since_c1"]),
        ("c2_pton_1y", r(out["c2_pton_pre"][-1][1] - 1), J["c2"]["pton_1y"]),
        ("c2_2022", r(c2lo), J["c2"]["wrong_pton"]["to_2022end"]),
        ("c2_end", r(out["c2_wrong"][-1][1] - 1), J["c2"]["wrong_pton"]["to_end"]),
        ("c2_need", r(1 / (1 + pt.chg(D2, END)), 1), J["c2"]["pton_need_to_recover"]),
        ("c3_zm", r(out["c3_zm_fall"][-1][1] - 1), J["c3"]["zm_from_peak"]),
        ("c3_dis_18m", r(out["c3_dis_pre"][-1][1] - 1), J["c3"]["dis_18m"]),
        ("c3_worst", r(c3lo), J["c3"]["wrong_dis"]["worst"]),
        ("c3_end", r(out["c3_wrong"][-1][1] - 1), J["c3"]["wrong_dis"]["to_end"]),
        ("c3_meta", r(mlo), J["c3"]["big_2022_low_from_2021_end"]["META"][0]),
        ("c3_amzn", r(alo), J["c3"]["big_2022_low_from_2021_end"]["AMZN"][0]),
        ("c4_rec21", len(rec21), J["c4"]["records"]["records_2021"]),
        ("c4_days", rec["days"], J["c4"]["records"]["days"]),
        ("c4_fell10", int(rec["fell_10pct_2y"]), int(J["c4"]["records"]["fell_10pct_2y"])),
        ("c4_worst", r(lo4), J["c4"]["wrong_debt_tr"]["worst"]),
        ("c4_back", back4, J["c4"]["back_to_start"]),
        ("c4_months", L.months(D4, back4), J["c4"]["months_to_back"]),
        ("c4_peak", pk4, J["c4"]["spx_peak"][0]),
        ("c5_quarter", r(zm.at(D5) / zm.at(ZM_PEAK), 3), J["c5"]["zm_quarter"]),
        ("c5_worst", r(c5lo), J["c5"]["wrong_zm"]["worst"]),
        ("c5_end", r(out["c5_wrong"][-1][1] - 1), J["c5"]["wrong_zm"]["to_end"]),
        ("c5_need", r(zm.at(ZM_PEAK) / zm.at(D5), 2), J["c5"]["need_x_to_peak"]),
        ("c5_now", r(zm.at(NOW) / zm.at(ZM_PEAK), 3), J["c5"]["zm_now_vs_peak"]),
        ("end_right", r(right(END)), J["lee_right"]["total_end"]),
    ]
    bad = [c for c in chk if c[1] != c[2]]
    for name, got, want in chk:
        info("CHECK", "check=%s got=%s calc=%s ok=%s", name, got, want, got == want)
    if bad:
        info("FAIL", "mismatch=%s next=계산 규칙을 longform_ep2.py 와 다시 맞춤", bad)
        return 1
    info("SERIES", "keys=%s points=%d", list(out), sum(len(v) for v in out.values() if isinstance(v, list)))
    DST.parent.mkdir(parents=True, exist_ok=True)
    DST.write_text(f"// 자동 생성 — stock/source/daebi-test-2026-11/calc/series.py {VERSION} (손으로 고치지 않음)\nwindow.SERIES = " + json.dumps(out, ensure_ascii=False) + ";\n", "utf-8")
    info("DONE", "file=%s bytes=%d sec=%.1f", DST.relative_to(ROOT), DST.stat().st_size, time.time() - t0)
    return 0


if __name__ == "__main__":
    sys.exit(main())
