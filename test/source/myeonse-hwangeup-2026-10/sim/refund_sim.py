#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-24 — 최초. 사용자 지시 "11월 이후 면세 방법 변경되고 가장 빠르게 면세 받기 위한 시뮬레이션을 돌려봐 시간 재서".
r"""
일본 면세 '사후 환급(리판드 방식)' — 공항에서 면세 확인·환급까지 걸리는 시간 모의실험 (연구·교육용, 여행·세무 조언 아님)

무엇을 재나
  공항 출발 로비에 도착한 때부터 '면세 확인(세관) 끝 + (현금을 고르면) 현금을 받은 때'까지의 분.
  체크인·보안 검사·출국 심사처럼 면세와 상관없이 누구나 거치는 시간은 넣지 않는다.

어떻게
  - 여행자가 무작위(포아송)로 도착 → 면세 수속 단말기(여러 대, 먼저 온 순서) → 빨간색이면 세관 검사 창구
    → 현금 환급을 고르면 현금 환급 단말기. 창구·단말기마다 '대수'가 있는 줄(다중 서버 FIFO 대기열).
  - 일부 소모품을 써 버린 사람은 단말기 대신 세관 창구로 바로 (国税庁 리플릿 — 확인표 문장 근거).
  - 휴대전화 수속(일곱 개 공항, 전용 와이파이 구역의 비지트 재팬 웹)은 단말기 줄을 서지 않는다고 본다.
  - 혼잡도 3가지(한산·보통·붐빔) × 전략 6가지를 반복(rep)마다 다른 난수로 돌려 가운데값·상위 10% 시간을 낸다.
  - 전략별 시간은 '탐침 여행자'(전략을 고정한 소수 여행자, 전체의 약 2%)로 잰다 — 줄의 붐빔은 일반 여행자 섞임이 만든다.

한계 (결과를 읽기 전에)
  - 단말기·세관 창구·현금 단말기 대수, 한 사람 처리 시간, 빨간색 비율은 **공개된 숫자가 없어 가정**이다 (PARAMS 의 note).
    그래서 '몇 분'은 가정에 따라 바뀐다. 가정이 달라도 바뀌지 않는 것은 **전략 사이의 순서와 차이의 까닭**이다.
  - 2026-11-01 시행 전이라 실제 측정값으로 맞춰 볼 수 없다. 시행 뒤 실제 대기 시간이 나오면 PARAMS 를 고쳐 다시 돌린다.

  python3 test/source/myeonse-hwangeup-2026-10/sim/refund_sim.py                 # 기본 (결과 표 → sim/results.md)
  python3 test/source/myeonse-hwangeup-2026-10/sim/refund_sim.py --reps 50 --log-level DEBUG
  python3 test/source/myeonse-hwangeup-2026-10/sim/refund_sim.py --selftest      # 대기열 계산 시험

CHANGELOG
  v1.0 — 2026-10-24 — 최초 (대기열 모델 · 전략 6 — 줄을 보고 단말기/휴대전화 고르기 포함 · 혼잡도 3 · 빨간색일 때 시간 ·
         민감도: 단말기 대수·빨간색 비율 · 기존 방식과 비교)
"""
import argparse
import heapq
import logging
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

VERSION = "v1.0"
HERE = Path(__file__).resolve().parent
LOG = logging.getLogger("refund_sim")

# ---------------- 가정 (분 · 대 · 비율) — note 에 근거 또는 '가정' ----------------
PARAMS = {
    "walk_to_kiosk": dict(v=(0.5, 1.0, 2.0), note="로비 안에서 단말기까지 걷기 — 가정 (삼각분포 최소·최빈·최대)"),
    "kiosk_prereg": dict(v=(0.4, 0.7, 1.2), note="단말기에 여권 대고 확인 — 비지트 재팬 웹·환급 방법을 미리 등록한 사람. 공개 측정값 없음 → 가정"),
    "kiosk_noprep": dict(v=(0.8, 1.5, 3.0), note="같은 일, 준비 없이 화면 안내를 처음 읽는 사람 — 가정"),
    "phone": dict(v=(1.0, 2.0, 4.0), note="전용 와이파이 구역까지 가서 휴대전화로 수속 (일곱 개 공항, 관광청) — 줄 없음으로 봄, 시간은 가정"),
    "walk_to_customs": dict(v=(1.0, 2.0, 3.0), note="세관 검사 창구까지 걷기 — 가정"),
    "inspect_packed": dict(v=(1.5, 3.0, 5.0), note="빨간색 → 산 물건 보여 주기, 면세품을 가방 하나에 모아 둔 사람 — 가정"),
    "inspect_mixed": dict(v=(2.0, 4.0, 8.0), note="같은 일, 면세품이 여러 가방에 섞인 사람 — 가정"),
    "partial_counter": dict(v=(3.0, 5.0, 10.0), note="일부를 써 버려 단말기 대신 세관 창구에서 신고 (国税庁 리플릿) — 처리 시간은 가정"),
    "walk_to_cash": dict(v=(1.0, 2.0, 4.0), note="현금 환급 단말기까지 — 하네다는 출국 후 구역, 나리타는 출국 전 구역 (트래블보이스 2026-10-21) — 걷는 시간은 가정"),
    "cash_service": dict(v=(0.7, 1.0, 1.5), note="현금 환급 '약 1분' (일본공항빌딩·글로리 발표, 트래블보이스 2026-10-21)"),
    "kiosks": dict(v=10, note="한 터미널 면세 수속 단말기 대수 — 공개 숫자 없음 → 가정 (민감도 6·10·16)"),
    "customs_counters": dict(v=6, note="세관 검사 창구 수 — 가정"),
    "cash_kiosks": dict(v=2, note="한 곳의 현금 환급 단말기 대수 — 3개 공항 5곳만 공개, 대수는 없음 → 가정"),
    "p_red": dict(v=0.10, note="단말기에서 빨간색이 뜰 비율 — 공개 숫자 없음 → 가정 (민감도 0.05·0.10·0.20)"),
    "mix_prereg": dict(v=0.30, note="일반 여행자 중 미리 등록한 비율 — 가정"),
    "mix_phone": dict(v=0.10, note="일반 여행자 중 휴대전화 수속 비율 — 가정"),
    "mix_partial": dict(v=0.10, note="일반 여행자 중 일부를 써 버린 비율 — 가정"),
    "mix_packed": dict(v=0.40, note="일반 여행자 중 면세품을 한 가방에 모은 비율 — 가정"),
    "mix_cash": dict(v=0.30, note="일반 여행자 중 현금 환급을 고른 비율 — 가정"),
    "window_h": dict(v=4.0, note="붐비는 시간대 길이(시간) — 그 안에 도착한 사람만 잼, 앞뒤 1시간은 줄이 차고 빠지는 구간으로 뺌"),
}
# 혼잡도 = 면세 수속이 필요한 출발 여행자 수(시간당). 단말기 10대·평균 처리 약 1.5분이면 시간당 약 400명이 한계.
# 참고: 2019년 방일객의 54.9% 가 면세 수속 (관광청) — 터미널 시간당 출발 외국인 수는 공개 숫자가 없어 혼잡도는 가정.
CROWDS = {"한산": 180, "보통": 330, "붐빔": 450}

# 전략 (탐침 여행자 속성) — 사람이 고를 수 있는 것만
STRATEGIES = {
    "S1 준비 없음": dict(prereg=False, phone=False, choose=False, partial=True, packed=False, cash=True,
                       desc="미리 등록 X · 단말기 · 섞인 영수증에서 과자를 먹음(→ 세관 창구) · 짐 섞임 · 현금 환급"),
    "S2 보통": dict(prereg=False, phone=False, choose=False, partial=False, packed=False, cash=True,
                  desc="미리 등록 X · 단말기 · 먹을 것은 따로 계산 · 짐 섞임 · 현금 환급"),
    "S3 미리 등록 + 현금": dict(prereg=True, phone=False, choose=False, partial=False, packed=True, cash=True,
                          desc="비지트 재팬 웹·환급 방법 미리 등록 · 단말기 · 먹을 것 따로 · 면세품 한 가방 · 공항에서 현금"),
    "S4 미리 등록 + 카드": dict(prereg=True, phone=False, choose=False, partial=False, packed=True, cash=False,
                          desc="S3 과 같고 환급은 카드로 (공항에서 기다리지 않음 — 돈은 나중에 들어옴, 며칠인지는 공식 설명 없음)"),
    "S5 휴대전화 수속": dict(prereg=True, phone=True, choose=False, partial=False, packed=True, cash=False,
                        desc="S4 + 단말기 대신 늘 휴대전화 수속 (일곱 개 공항, 전용 와이파이 구역)"),
    "S6 가장 빠르게": dict(prereg=True, phone=False, choose=True, partial=False, packed=True, cash=False,
                       desc="S4 + 단말기 줄을 보고 더 빠른 쪽(단말기 / 휴대전화)을 고름"),
}
PROBE_ATTRS = ("prereg", "phone", "choose", "partial", "packed", "cash")


def tri(rng, key, n, P=PARAMS):
    a, m, b = P[key]["v"]
    return rng.triangular(a, m, b, size=n)


def fifo_multi(arrive, service, servers):
    """먼저 온 순서 다중 서버 대기열 → (서비스 시작, 끝). arrive·service 는 같은 길이 배열 (분)."""
    order = np.argsort(arrive, kind="stable")
    start = np.empty_like(arrive)
    free = [0.0] * servers                      # 서버마다 다음에 비는 시각 (최소 힙)
    heapq.heapify(free)
    for i in order:
        f = heapq.heappop(free)
        s = max(arrive[i], f)
        start[i] = s
        heapq.heappush(free, s + service[i])
    return start, start + service


def one_rep(rng, lam_per_h, P, probes_per_strategy=10):
    """한 번 돌림 → {전략: [걸린 분]} + 진단 값."""
    win = P["window_h"]["v"] * 60.0
    total = win + 120.0                          # 앞뒤 1시간씩
    n = rng.poisson(lam_per_h * total / 60.0)
    t_arr = np.sort(rng.uniform(0, total, n))
    attrs = {
        "prereg": rng.random(n) < P["mix_prereg"]["v"],
        "phone": rng.random(n) < P["mix_phone"]["v"],
        "partial": rng.random(n) < P["mix_partial"]["v"],
        "packed": rng.random(n) < P["mix_packed"]["v"],
        "cash": rng.random(n) < P["mix_cash"]["v"],
        "choose": np.zeros(n, dtype=bool),
        "probe": np.full(n, "", dtype=object),
    }
    # 탐침 여행자: 재는 구간 안 무작위 시각
    for name, st in STRATEGIES.items():
        k = probes_per_strategy
        t_arr = np.concatenate([t_arr, rng.uniform(60.0, 60.0 + win, k)])
        for a in PROBE_ATTRS:
            attrs[a] = np.concatenate([attrs[a], np.full(k, st[a])])
        attrs["probe"] = np.concatenate([attrs["probe"], np.full(k, name, dtype=object)])
    N = len(t_arr)
    phone = attrs["phone"] & ~attrs["partial"]          # 써 버린 사람은 휴대전화 수속 못 함 → 세관 창구
    at_kiosk = ~phone & ~attrs["partial"]

    # 1단계: 단말기 줄 / 휴대전화 / (써 버린 사람은 바로 세관 창구로)
    walk = tri(rng, "walk_to_kiosk", N, P)
    k_arr = t_arr + walk
    k_srv = np.where(attrs["prereg"], tri(rng, "kiosk_prereg", N, P), tri(rng, "kiosk_noprep", N, P))
    done1 = np.full(N, np.nan)
    wait_k = np.zeros(N)
    idx = np.where(at_kiosk)[0]
    s, e = fifo_multi(k_arr[idx], k_srv[idx], P["kiosks"]["v"])
    done1[idx], wait_k[idx] = e, s - k_arr[idx]
    t_phone = k_arr + tri(rng, "phone", N, P)
    idx_p = np.where(phone)[0]
    done1[idx_p] = t_phone[idx_p]
    ch = attrs["choose"] & at_kiosk                      # 줄을 보고 고름: 단말기 끝 시각과 휴대전화 끝 시각 중 이른 쪽
    done1[ch] = np.minimum(done1[ch], t_phone[ch])

    # 2단계: 세관 창구 — 빨간색(단말기·휴대전화) + 써 버린 사람
    red = (~attrs["partial"]) & (rng.random(N) < P["p_red"]["v"])
    to_c = red | attrs["partial"]
    c_arr = np.where(attrs["partial"], t_arr, done1) + tri(rng, "walk_to_customs", N, P)
    c_srv = np.where(attrs["partial"], tri(rng, "partial_counter", N, P),
                     np.where(attrs["packed"], tri(rng, "inspect_packed", N, P), tri(rng, "inspect_mixed", N, P)))
    done2 = done1.copy()
    wait_c = np.zeros(N)
    idx = np.where(to_c)[0]
    s, e = fifo_multi(c_arr[idx], c_srv[idx], P["customs_counters"]["v"])
    done2[idx], wait_c[idx] = e, s - c_arr[idx]

    # 3단계: 현금 환급 단말기 (현금을 고른 사람)
    cash_arr = done2 + tri(rng, "walk_to_cash", N, P)
    cash_srv = tri(rng, "cash_service", N, P)
    done3 = done2.copy()
    wait_cash = np.zeros(N)
    idx = np.where(attrs["cash"])[0]
    s, e = fifo_multi(cash_arr[idx], cash_srv[idx], P["cash_kiosks"]["v"])
    done3[idx], wait_cash[idx] = e, s - cash_arr[idx]

    took = done3 - t_arr
    in_win = (t_arr >= 60.0) & (t_arr <= 60.0 + win)
    out = {name: took[(attrs["probe"] == name)] for name in STRATEGIES}
    out.update({name + "|red": took[(attrs["probe"] == name) & red] for name in STRATEGIES})
    out["_all"] = took[in_win & (attrs["probe"] == "")]
    diag = {"n": int(n), "kiosk_wait_med": float(np.median(wait_k[in_win & at_kiosk])) if (in_win & at_kiosk).any() else 0.0,
            "customs_wait_med": float(np.median(wait_c[in_win & to_c])) if (in_win & to_c).any() else 0.0,
            "cash_wait_med": float(np.median(wait_cash[in_win & attrs["cash"]])) if (in_win & attrs["cash"]).any() else 0.0}
    # 전략별 단계 나눔 (탐침만, 분)
    parts = {}
    for name in STRATEGIES:
        m = attrs["probe"] == name
        parts[name] = dict(kiosk_or_phone=float(np.nanmean(np.where(attrs["partial"][m], 0.0, done1[m] - t_arr[m]))),
                           customs=float(np.mean((done2 - np.where(np.isnan(done1), t_arr, done1))[m] * to_c[m])) if m.any() else 0.0,
                           cash=float(np.mean((done3 - done2)[m])))
    return out, diag, parts


def run(reps, seed, P=PARAMS, crowds=CROWDS):
    rng = np.random.default_rng(seed)
    res = {}
    for cname, lam in crowds.items():
        acc = {k: [] for k in list(STRATEGIES) + [s + "|red" for s in STRATEGIES] + ["_all"]}
        diags, parts_acc = [], {k: [] for k in STRATEGIES}
        t0 = time.perf_counter()
        for _ in range(reps):
            out, diag, parts = one_rep(rng, lam, P)
            for k, v in out.items():
                acc[k].extend(v.tolist())
            diags.append(diag)
            for k, v in parts.items():
                parts_acc[k].append(v)
        res[cname] = dict(lam=lam, times={k: np.array(v) for k, v in acc.items()},
                          kiosk_wait=float(np.median([d["kiosk_wait_med"] for d in diags])),
                          customs_wait=float(np.median([d["customs_wait_med"] for d in diags])),
                          cash_wait=float(np.median([d["cash_wait_med"] for d in diags])),
                          parts={k: {p: float(np.mean([x[p] for x in v])) for p in v[0]} for k, v in parts_acc.items()},
                          seconds=time.perf_counter() - t0)
        log("SIM", crowd=cname, per_hour=lam, reps=reps, travelers_per_rep=int(np.mean([d["n"] for d in diags])),
            kiosk_wait_med=res[cname]["kiosk_wait"], customs_wait_med=res[cname]["customs_wait"],
            cash_wait_med=res[cname]["cash_wait"], seconds=res[cname]["seconds"])
        for k in STRATEGIES:
            t = res[cname]["times"][k]
            log("RESULT", level=logging.DEBUG, crowd=cname, strategy=k, median=float(np.median(t)), mean=float(np.mean(t)))
    return res


def log(stage, level=logging.INFO, **kv):
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    LOG.log(level, f"[{stage}] [{ts}] " + " ".join(f"{k}={v:.2f}" if isinstance(v, float) else f"{k}={v}" for k, v in kv.items()))


def fmt(t):
    """가운데값 + 평균. 상위 10% 는 빨간색 비율(10%) 경계에 걸려 반복마다 크게 흔들려 쓰지 않음 — 빨간색일 때는 따로 표."""
    return f"{np.median(t):.1f}분 (평균 {np.mean(t):.1f}분)"


def sensitivity(reps, seed):
    """단말기 대수·빨간색 비율을 바꿔 S2·S4 가 어떻게 되는지 (붐빔 기준)."""
    rows = []
    for kiosks in (6, 10, 16):
        for p_red in (0.05, 0.10, 0.20):
            P = {k: dict(v) for k, v in PARAMS.items()}
            P["kiosks"]["v"], P["p_red"]["v"] = kiosks, p_red
            r = run(reps, seed, P, {"붐빔": CROWDS["붐빔"]})["붐빔"]
            t2, t4, t6 = (r["times"][k] for k in ("S2 보통", "S4 미리 등록 + 카드", "S6 가장 빠르게"))
            rows.append((kiosks, p_red, np.median(t2), np.median(t4), np.median(t6), np.mean(t6), r["kiosk_wait"], r["customs_wait"]))
            log("SENS", kiosks=kiosks, p_red=p_red, s2_med=rows[-1][2], s4_med=rows[-1][3], s6_med=rows[-1][4], s6_mean=rows[-1][5],
                kiosk_wait_med=rows[-1][6], customs_wait_med=rows[-1][7])
    return rows


def write_md(res, sens, reps, seed, secs, path):
    o = [f"# 일본 면세 사후 환급 — 공항 시간 모의실험 결과 ({VERSION})", "",
         f"만든 때 {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')} · `refund_sim.py` · 반복 {reps}번 · 난수 씨앗 {seed} · 돌린 시간 {secs:.1f}초", "",
         "> **가정으로 돌린 모의실험이다 — 실제로 잰 시간이 아니다.** 단말기·창구 대수, 한 사람 처리 시간, 빨간색 비율은 공개된 숫자가 없어 가정했다 (아래 '가정' 표).",
         "> 가정이 바뀌어도 그대로인 것은 **전략 사이의 순서**와 **어디서 시간이 드는지**다. 연구·교육용 — 여행·세무 조언 아님.", "",
         "잰 구간: 공항 출발 로비 도착 → 면세 확인(세관) 끝 → (현금을 고르면) 현금 받기까지. 체크인·보안 검사·출국 심사는 누구나 거치므로 뺐다.",
         "기존 방식(2026-10-31까지 산 물건): 공항에서 면세 때문에 할 일 없음 → **0분** (세관 검사는 강제 아님).", "",
         "## 전략", "", "| 전략 | 하는 일 |", "|---|---|"]
    o += [f"| {k} | {v['desc']} |" for k, v in STRATEGIES.items()]
    o += ["", "## 결과 — 가운데값 (평균)", "",
          "| 혼잡도 (면세 여행자/시간) | " + " | ".join(STRATEGIES) + " | 단말기 줄 | 세관 창구 줄 | 현금 단말기 줄 |",
          "|---|" + "---|" * (len(STRATEGIES) + 3)]
    for c, r in res.items():
        o.append(f"| {c} ({r['lam']}명) | " + " | ".join(fmt(r["times"][k]) for k in STRATEGIES)
                 + f" | {r['kiosk_wait']:.1f}분 | {r['customs_wait']:.1f}분 | {r['cash_wait']:.1f}분 |")
    o += ["", "줄 = 그 줄에 선 사람의 기다린 시간 가운데값.", "", "## 빨간색이 떴을 때 (세관 검사장에서 물건 보여 주기) — 가운데값", "",
          "| 혼잡도 | " + " | ".join(STRATEGIES) + " |", "|---|" + "---|" * len(STRATEGIES)]
    for c, r in res.items():
        o.append(f"| {c} | " + " | ".join((f"{np.median(r['times'][k + '|red']):.1f}분" if len(r['times'][k + '|red']) else "—") for k in STRATEGIES) + " |")
    o += ["", "S1 은 써 버린 물건 때문에 처음부터 세관 창구로 가므로 '빨간색' 경우가 없음(—).", "", "## 어디서 시간이 드나 (보통 혼잡, 평균 분)", "",
          "| 전략 | 단말기·휴대전화 | 세관 창구 (빨간색·써 버린 물건) | 현금 받기 |", "|---|---|---|---|"]
    for k, p in res["보통"]["parts"].items():
        o.append(f"| {k} | {p['kiosk_or_phone']:.1f} | {p['customs']:.1f} | {p['cash']:.1f} |")
    o += ["", "## 민감도 — 붐빌 때, 단말기 대수·빨간색 비율을 바꾸면 (가운데값)", "",
          "| 단말기 | 빨간색 비율 | S2 보통 | S4 미리 등록 + 카드 | S6 가장 빠르게 (평균) | 단말기 줄 | 세관 창구 줄 |", "|---|---|---|---|---|---|---|"]
    o += [f"| {k}대 | {int(p * 100)}% | {a:.1f}분 | {b:.1f}분 | {c:.1f}분 ({cm:.1f}분) | {w:.1f}분 | {cw:.1f}분 |" for k, p, a, b, c, cm, w, cw in sens]
    o += ["", "단말기가 모자라면(6대) 단말기 줄이 길어져 그 뒤 세관·현금 줄로 가는 흐름이 늦춰진다 — 그래서 뒤 줄이 오히려 짧게 나올 수 있다 (가운데값은 빨간색이 아닌 사람이 대부분)."]
    o += ["", "## 가정", "", "| 이름 | 값 | 근거·가정 |", "|---|---|---|"]
    o += [f"| {k} | {v['v']} | {v['note']} |" for k, v in PARAMS.items()]
    o += ["", "| 혼잡도 | 면세 여행자/시간 |", "|---|---|"] + [f"| {k} | {v} |" for k, v in CROWDS.items()]
    path.write_text("\n".join(o) + "\n", encoding="utf-8")
    log("WRITE", file=str(path))


def selftest():
    """대기열 계산 시험: 손으로 푼 예 + 한 서버 줄의 평균 대기(M/M/1 공식)와 비교."""
    s, e = fifo_multi(np.array([0.0, 0.0, 0.0, 1.0]), np.array([2.0, 2.0, 2.0, 1.0]), 2)
    assert s.tolist() == [0.0, 0.0, 2.0, 2.0] and e.tolist() == [2.0, 2.0, 4.0, 3.0], (s, e)
    rng = np.random.default_rng(1)
    lam, mu, n = 0.8, 1.0, 200_000                 # 이용률 0.8 → 평균 대기 Wq = ρ/(μ-λ) = 4.0
    arr = np.cumsum(rng.exponential(1 / lam, n))
    s, _ = fifo_multi(arr, rng.exponential(1 / mu, n), 1)
    wq = float(np.mean((s - arr)[n // 10:]))
    assert abs(wq - 4.0) < 0.4, wq
    log("SELFTEST", ok=True, mm1_wq=wq, expected=4.0)
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description="일본 면세 사후 환급 공항 시간 모의실험 (가정 기반)")
    ap.add_argument("--reps", type=int, default=200)
    ap.add_argument("--seed", type=int, default=20261101)
    ap.add_argument("--out", default=str(HERE / "results.md"))
    ap.add_argument("--no-sens", action="store_true", help="민감도 표 건너뜀")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args(argv)
    logging.basicConfig(level=a.log_level, format="%(message)s", stream=sys.stdout)
    if a.selftest:
        return selftest()
    log("CONFIG", version=VERSION, reps=a.reps, seed=a.seed, crowds=",".join(f"{k}:{v}" for k, v in CROWDS.items()),
        kiosks=PARAMS["kiosks"]["v"], customs_counters=PARAMS["customs_counters"]["v"], cash_kiosks=PARAMS["cash_kiosks"]["v"],
        p_red=PARAMS["p_red"]["v"], note="가정 기반 — 실제 측정 아님")
    t0 = time.perf_counter()
    res = run(a.reps, a.seed)
    sens = [] if a.no_sens else sensitivity(max(20, a.reps // 4), a.seed)
    secs = time.perf_counter() - t0
    for c, r in res.items():
        log("SUMMARY", crowd=c, **{k.split()[0]: f"{np.median(r['times'][k]):.1f}/{np.mean(r['times'][k]):.1f}/{np.median(r['times'][k + '|red']) if len(r['times'][k + '|red']) else float('nan'):.1f}" for k in STRATEGIES},
            note="가운데값/평균/빨간색일때 (분)")
    write_md(res, sens, a.reps, a.seed, secs, Path(a.out))
    log("DONE", seconds=secs)
    return 0


if __name__ == "__main__":
    sys.exit(main())
