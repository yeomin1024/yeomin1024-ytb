#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-11-02 — 주식 롱폼 2편 대본 v9 의 숫자 (이씨 · 상승장의 잘못된 '생각' 다섯 개).
#   사용자 지시 2026-11-02 (대본 평가판 2편 피드백): "이 주제는 잘못된 생각을 가지고 있으면 폭락을 못피한다로 가야해
#   예를 들면 상승장에서 몰빵해서 수익 많이 내서 잘하고 있다고 생각한다 아니다 운이 좋았을 뿐이다 이런식으로 생각 선택지 나눠야해 항목 모두 바꿔".
#   다섯 생각 (날짜 = 이야기 속 그날 종가):
#     ① 2020-12-31 실력 vs 운 — 줌(ZM) 2020년 약 5배 · 오답 = 그대로 몰빵 / 정답(예) = 90% S&P 500 + 10% 줌
#     ② 2021-02-12 '번 돈은 공짜 돈' — 그때까지 번 돈(2020-12-31 뒤 줌 +28.4%)을 펠로톤(PTON)에 / 정답 = S&P 500
#     ③ 2021-09-30 '큰 회사는 안전' — 줌 판 돈 모두 디즈니(DIS) 한 곳 / 정답 = S&P 500 (여러 큰 회사)
#     ④ 2021-12-31 '이번엔 다르다' — 마이너스 통장 2천만 원으로 S&P 500 더 매수 / 정답 = 빚 없음 (이자는 셈에서 뺌 — 넣으면 손실이 더 큼)
#     ⑤ 2022-01-31 '최고가가 제값' — 빌린 돈으로 산 지수를 팔아 최고가의 4분의 1 남짓이 된 줌을 다시 / 정답 = 지수 그대로
#   끝 날 = 2024-12-31 (이야기 4년) · '지금' = 자료 끝 2026-10-27 (참고).
#   묶음 통계: bulk/px = 지금 S&P 500 종목 503개 (생존 편향 — 빠진 종목이 없음). ①·⑤ 통계는 편향이 결론 반대쪽(덜 빠지고 더 회복한 쪽)이라 보수적.
# 자료(새로 받은 것): precheck/data/ZM.csv · PTON.csv (precheck.fetch, Yahoo v8 수정 종가). 나머지는 longform_items.load() · bulk/px.
# 실행: python3 -B stock/topics/precheck/longform_ep2.py → precheck/longform_ep2_2026-11-02.json
# ※ 연구·교육용 — 투자 권유가 아님.
import json
import logging
import sys
from datetime import date
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import longform_items as L  # noqa: E402

VERSION = "v1.0"
log = logging.getLogger("longform_ep2")
D1, D2, D3, D4, D5 = "2020-12-31", "2021-02-12", "2021-09-30", "2021-12-31", "2022-01-31"
END, NOW = "2024-12-31", "2026-10-27"
DEBT = 0.2          # 1억 원 = 1.0 → 2천만 원
KEEP_ZM = 0.1       # ① 정답 예: 줌 10% 남기고 90% 를 S&P 500 으로


def info(stage, msg, *a):
    log.info(msg, *a, extra={"stage": stage})


def ser(sym):
    p = HERE / "data" / f"{sym}.csv"
    if not p.exists():
        p = HERE / "bulk" / "px" / f"{sym}.csv"
    return L.Ser(sym, L.rd(p, "adjclose"))


def r(x, n=4):
    return round(float(x), n)


def mix_path(parts, a, b):
    """parts = [(Ser, 비중)] 를 a 날 사서 b 날까지 보유 → (끝 값, 가장 낮은 값, 그날)."""
    days = [d for d in parts[0][0].k if a <= d <= b]
    vals = [sum(w * s.at(d) / s.at(a) for s, w in parts) for d in days]
    i = int(np.argmin(vals))
    return r(vals[-1]), r(min(vals) - 1), days[i]


def one(s, a, b=END):
    lo, lday = s.low(a, b)
    out = {"from": s.day(a), "price": r(s.at(a), 2), "to_2022end": r(s.chg(a, "2022-12-30")), "to_end": r(s.chg(a, END)), "to_now": r(s.chg(a, NOW)), "worst": r(lo), "worst_day": lday}
    return out


def records(spx, since="1990-01-01", horizon_days=730):
    """그날까지의 최고가를 새로 쓴 날(종가) → 그 뒤 2년 안에 그날보다 10%·20% 넘게 빠진 적이 있나 (2년 뒤 자료가 있는 날만)."""
    k, v = spx.k, spx.v
    mx, n, d10, d20, by_year = -1.0, 0, 0, 0, {}
    last = date.fromisoformat(k[-1])
    for i in range(len(v)):
        if v[i] > mx:
            mx = v[i]
            by_year[k[i][:4]] = by_year.get(k[i][:4], 0) + 1
            if k[i] < since or (last - date.fromisoformat(k[i])).days < horizon_days:
                continue
            end = date.fromisoformat(k[i]).toordinal() + horizon_days
            j = i + 1
            m = v[i]
            while j < len(v) and date.fromisoformat(k[j]).toordinal() <= end:
                m = min(m, v[j])
                j += 1
            n += 1
            d10 += m <= v[i] * 0.9
            d20 += m <= v[i] * 0.8
    return {"since": since, "days": n, "fell_10pct_2y": d10, "fell_20pct_2y": d20, "share10": r(d10 / n), "share20": r(d20 / n), "records_2021": by_year.get("2021"), "records_2020": by_year.get("2020")}


def bulk_all():
    out = {}
    for p in sorted((HERE / "bulk" / "px").glob("*.csv")):
        try:
            out[p.stem] = L.Ser(p.stem, L.rd(p, "adjclose"))
        except Exception as e:  # 자료가 비었거나 꼴이 다른 파일 — 건너뛰고 기록
            log.warning("skip %s %s", p.stem, e, extra={"stage": "BULK"})
    return out


def winners_2020(B, mult=2.0):
    """2019-12-31 에도 값이 있는 지금 S&P 500 종목 가운데 2020년에 mult 배 넘게 오른 것 → 2020-12-31 값의 반 아래로 2022년 말까지 내려간 것."""
    hit, half = [], []
    for s, x in B.items():
        if x.k[0] > "2019-12-31":
            continue
        g = x.at("2020-12-31") / x.at("2019-12-31")
        if g >= mult:
            hit.append((s, r(g, 2)))
            lo, _ = x.low("2020-12-31", "2022-12-30")
            if lo <= -0.5:
                half.append(s)
    return {"mult": mult, "n": len(hit), "halved_by_2022": len(half), "names": sorted(hit, key=lambda t: -t[1]), "halved": sorted(half)}


def deep_fallen(B, day=D5, below=0.6):
    """day 에 그날까지의 최고가보다 below 넘게 빠져 있던 지금 S&P 500 종목 → 자료 끝(지금)까지 그 최고가를 되찾았나."""
    rows = []
    for s, x in B.items():
        if x.k[0] > "2019-01-02":
            continue
        pk, dd = x.peak_before(day)
        if dd <= -below and pk >= "2020-01-01":   # 2020~ 상승장에서 쓴 최고가만 (2000년 거품 최고가 등은 뺌)
            back = x.back(day, float(x.v[x.i(pk)]))
            rows.append((s, pk, r(dd, 3), back))
    got = [t for t in rows if t[3]]
    return {"day": day, "below": below, "n": len(rows), "regained_peak_by_now": len(got), "rows": rows}


def main():
    logging.basicConfig(level=logging.INFO, format="[%(stage)s] %(asctime)s %(message)s")
    S = L.load()
    for sym in ("ZM", "PTON", "DIS", "META", "AMZN", "NFLX", "MSFT", "AAPL", "GOOGL", "NVDA"):
        S[sym] = ser(sym)
    tr, spx, zm, pt, dis = S["TR"], S["SPX"], S["ZM"], S["PTON"], S["DIS"]
    info("LOAD", "tickers=ZM,PTON,DIS,big caps · tr %s~%s · end=%s now=%s", tr.k[0], tr.k[-1], END, NOW)

    R = {"version": VERSION, "made": date.today().isoformat(), "end": END, "now": NOW}
    # ── 도입
    R["intro"] = {"spx_4y": r(spx.chg(D1, END)), "tr_4y": r(tr.chg(D1, END)), "covid_drop": r(spx.chg("2020-02-19", "2020-03-23"))}
    # ── ① 실력 vs 운
    R["c1"] = {"zm_2020": r(zm.chg("2019-12-31", D1)), "zm_from_peak_2020": zm.peak_before(D1), "spx_2020": r(spx.chg("2019-12-31", D1)), "tr_2020": r(tr.chg("2019-12-31", D1)),
               "wrong_zm": one(zm, D1)}
    v_end, worst, wday = mix_path([(tr, 1 - KEEP_ZM), (zm, KEEP_ZM)], D1, END)
    v_now = (1 - KEEP_ZM) * (1 + tr.chg(D1, NOW)) + KEEP_ZM * (1 + zm.chg(D1, NOW))
    R["c1"]["right_90_10"] = {"to_end": r(v_end - 1), "worst": worst, "worst_day": wday, "to_now": r(v_now - 1)}
    info("C1", "zm2020=%s wrong=%s right=%s", R["c1"]["zm_2020"], R["c1"]["wrong_zm"], R["c1"]["right_90_10"])
    # ── ② 번 돈은 공짜 돈
    gain = zm.chg(D1, D2)
    R["c2"] = {"gain_since_c1": r(gain), "pton_1y": r(pt.chg("2020-02-12", D2)), "wrong_pton": one(pt, D2), "right_tr": one(tr, D2),
               "pton_need_to_recover": r(1 / (1 + pt.chg(D2, END)), 1), "pton_money_end": r((zm.chg(D1, D2)) * (1 + pt.chg(D2, END)))}
    info("C2", "gain=%s pton=%s tr=%s", r(gain), R["c2"]["wrong_pton"], R["c2"]["right_tr"])
    # ── ③ 큰 회사는 안전
    R["c3"] = {"zm_since_c2": r(zm.chg(D2, D3)), "zm_from_peak": r(zm.at(D3) / zm.at("2020-10-19") - 1), "dis_18m": r(dis.chg("2020-03-23", D3)),
               "wrong_dis": one(dis, D3), "right_tr": one(tr, D3),
               "big_2022_low_from_2021_end": {s: [r(S[s].low(D4, "2022-12-30")[0]), S[s].low(D4, "2022-12-30")[1]] for s in ("META", "NFLX", "NVDA", "AMZN", "GOOGL", "MSFT", "AAPL")}}
    info("C3", "dis=%s tr=%s big=%s", R["c3"]["wrong_dis"], R["c3"]["right_tr"], R["c3"]["big_2022_low_from_2021_end"])
    # ── ④ 이번엔 다르다 (빚 2천만 원 → S&P 500, 이자 뺌)
    lo, lday = tr.low(D4, END)
    back = tr.back(D4, tr.at(D4), after=lday)
    R["c4"] = {"records": records(spx), "spx_peak": spx.peak_before("2022-12-30"), "debt": DEBT, "wrong_debt_tr": one(tr, D4),
               "debt_value_at_worst": r(DEBT * (1 + lo)), "debt_loss_at_worst": r(DEBT * lo), "back_to_start": back,
               "months_to_back": L.months(D4, back) if back else None}
    info("C4", "records=%s worst=%s back=%s", R["c4"]["records"], lo, back)
    # ── ⑤ 최고가가 제값 (빌린 돈으로 산 지수를 팔아 줌)
    R["c5"] = {"zm_vs_peak": r(zm.at(D5) / zm.at("2020-10-19") - 1), "zm_quarter": r(zm.at(D5) / zm.at("2020-10-19"), 3), "spx_from_peak": r(spx.at(D5) / spx.at("2022-01-03") - 1),
               "wrong_zm": one(zm, D5), "right_tr": one(tr, D5),
               "need_x_to_peak": r(zm.at("2020-10-19") / zm.at(D5), 2), "zm_now_vs_peak": r(zm.at(NOW) / zm.at("2020-10-19"), 3)}
    info("C5", "zm=%s tr=%s", R["c5"]["wrong_zm"], R["c5"]["right_tr"])
    # ── 이씨 경로 (다섯 번 모두 오답) — 1억 원 = 1.0
    acc_c2 = 1 + zm.chg(D1, D2)                         # ② 때 계좌
    pton_part = (acc_c2 - 1) * (1 + pt.chg(D2, END))     # 번 돈 → 펠로톤
    zm_part = 1.0 * (1 + zm.chg(D2, D3))                 # 나머지 1억 원어치 줌 → ③ 때 판 돈
    dis_part = zm_part * (1 + dis.chg(D3, END))          # 모두 디즈니
    debt_part = DEBT * (1 + tr.chg(D4, D5)) * (1 + zm.chg(D5, END)) - DEBT   # 빚 → 지수 → 줌, 끝에 빚 갚음
    total = pton_part + dis_part + debt_part
    # 가장 낮았던 때 (끝 날까지 날마다)
    days = [d for d in tr.k if D1 <= d <= END]
    def wv(d):
        if d < D2:
            return zm.at(d) / zm.at(D1)
        v = (acc_c2 - 1) * pt.at(d) / pt.at(D2)
        v += (zm.at(d) / zm.at(D2)) if d < D3 else zm_part * dis.at(d) / dis.at(D3)
        if d >= D4:
            v += (DEBT * tr.at(d) / tr.at(D4) if d < D5 else DEBT * (tr.at(D5) / tr.at(D4)) * zm.at(d) / zm.at(D5)) - DEBT
        return v
    wvals = [wv(d) for d in days]
    wi = int(np.argmin(wvals))
    R["lee_wrong"] = {"acc_at_c2": r(acc_c2), "pton_part": r(pton_part), "zm_sold_at_c3": r(zm_part), "dis_part": r(dis_part), "debt_part_net": r(debt_part),
                      "total_end": r(total), "loss_end": r(total - 1), "worst": r(min(wvals) - 1), "worst_day": days[wi],
                      "note": "빚 2천만 원은 끝 날 갚은 것으로 뺌 · 이자는 뺌(넣으면 손실이 더 큼) · 세금·수수료·환율 뺌"}
    right_end = (1 - KEEP_ZM) * (1 + tr.chg(D1, END)) + KEEP_ZM * (1 + zm.chg(D1, END))
    R["lee_right"] = {"total_end": r(right_end), "worst": R["c1"]["right_90_10"]["worst"], "worst_day": R["c1"]["right_90_10"]["worst_day"],
                      "note": "다섯 번 모두 정답 = ① 90% S&P 500 + 10% 줌 그대로 (② 펠로톤 없음 · ③ 한 회사 없음 · ④ 빚 없음 · ⑤ 줌 다시 사지 않음)"}
    info("PATH", "wrong=%s right=%s", R["lee_wrong"], R["lee_right"])
    # ── 묶음 통계 (지금 S&P 500 503 종목)
    B = bulk_all()
    R["stat_winners_2020"] = {m: winners_2020(B, m) for m in (2.0, 3.0)}
    R["stat_deep_fallen"] = deep_fallen(B)
    info("STAT", "winners2x=%s/%s winners3x=%s/%s deep=%s/%s", R["stat_winners_2020"][2.0]["halved_by_2022"], R["stat_winners_2020"][2.0]["n"],
         R["stat_winners_2020"][3.0]["halved_by_2022"], R["stat_winners_2020"][3.0]["n"], R["stat_deep_fallen"]["regained_peak_by_now"], R["stat_deep_fallen"]["n"])
    R["survivorship"] = "bulk/px = 2026-10 지금 S&P 500 종목만 — 그 사이 빠진(대개 크게 떨어진) 종목이 없어, '반 토막 난 수'는 적게·'최고가를 되찾은 수'는 많게 잡힘 → 대본 결론 쪽에 불리하게(보수적으로) 셈."
    out = HERE / f"longform_ep2_{date.today().isoformat()}.json"
    out.write_text(json.dumps(R, ensure_ascii=False, indent=1, default=str), encoding="utf-8")
    info("DONE", "wrote %s", out.name)


if __name__ == "__main__":
    main()
