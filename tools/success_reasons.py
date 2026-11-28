#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-11-28 — 비교 집단 성공 비율을 주제 묶음 × 국면 · 제목 꼴 × 국면으로도 (어떤 때 어떤 주제·꼴이 잘 되나 — 표본 15개 이상만) · 판단 문서용.
# (v1.0) — 2026-11-28 — 최초. 성공 사례 전부의 '왜 됐나' 표 + 시기(시장 국면)별 성공 비율·시청자 심리·제목/썸네일 꼴 —
#          사용자 지시 2026-11-28 "시기에 맞는 주제를 찾는게 지금 너가 할일이야 매일 변화하는 주식시장이 변화하고 그에 따라 시청자들이 어떤 심리여서
#          무슨 영상을 찾게되는지 이걸 너가 분석해서 파악해야 한다고 … 권하는 순서 1,2 진행해봐" (2 = 성공 사례 전부 이유 표 + 상위 10편 깊게).
#
# CHANGELOG
#   v1.0 2026-11-28  build · selftest. 입력 = studio_board.success_rows (판 ① 목록과 같은 판정) · 승인 자료 W_<id>/ (metadata·comments) ·
#                    캐시 .cache/<id>.json·uploads_<채널>.json (채널 평소) · tools/market_data.py 시장 숫자 · thumb_codes_v2.tsv (있으면).
#                    출력 = <주제>/result/next_topic/success_why/00_all.md (판 ① 결과 맨 위) + <주제>/result/next_topic/success_reasons.csv.
#
# 국면(시장 상태) — 올린 시각 바로 전 미국 장 마감(한국 다음 날 05~06시) 기준, 앞 2거래일 안:
#   폭락 직후 = 필라델피아 반도체 ≤ −5% 또는 나스닥 ≤ −3% · 급등 직후 = 반도체 ≥ +5% 또는 나스닥 ≥ +3% (폭락이 아니면) ·
#   공포 = VIX ≥ 25 · 조정 = 나스닥 고점 대비 −5% 아래 · 평온 = 그 밖.  코스피 급락 = 올린 때 바로 전 코스피 장 ≤ −3% (따로 표시).
# 성공 비율 = 같은 국면에 올라온 '비교 집단'(compare.csv · 제외·외국·4분 미만·구독자 5만 넘음 뺌 · 7~180일) 중 성공 사례 몫.
#
# 연구·교육용 — 투자 조언이 아님. 클릭률·시청 지속률·트래픽 소스는 공개 자료에 없어 다루지 않음 (댓글·숫자로 미루어 봄).
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import logging
import re
import statistics as st
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import market_data as md          # noqa: E402
import outlier_research as orr    # noqa: E402

VERSION = "v1.1"
ROOT = Path(__file__).resolve().parent.parent
KST = dt.timezone(dt.timedelta(hours=9))
HANGUL = re.compile(r"[가-힣]")

CRASH_SOX, CRASH_NDQ, JUMP_SOX, JUMP_NDQ, FEAR_VIX, CORR_NDQ, KOSPI_DROP = -5.0, -3.0, 5.0, 3.0, 25.0, -5.0, -3.0
REGIMES = ["폭락 직후", "급등 직후", "공포", "조정", "평온"]

PSY = {   # 댓글 속 심리 (답글 아닌 댓글 · 영상 주인 댓글 뺌 · 낱말 세기 — 사람 분류 아님)
    "손실·공포": r"물렸|물림|물려|손절|잃었|잃고|털렸|털림|패닉|무섭|무서워|공포|죽고 ?싶|멘붕|반토막|마이너스|깡통|청산|박살|폭락",
    "희망·바닥": r"반등|바닥|줍줍|기회|저점|오른다|올라간|회복|떡상|대폭등|추매|매수 ?타이밍",
    "분노·탓": r"세력|작전|조작|사기|정부|정권|놈들|도둑|탓|짜고|설계|의도",
    "궁금·질문": r"\?|까요|나요|궁금|알려 ?주|어떻게 해야|뭔가요|인가요|할까",
    "감사·칭찬": r"감사|고맙|정리|도움|유익|좋은 영상|잘 ?봤|잘 ?보았|최고|명쾌|퀄리티",
    "계획·원칙": r"분할|계획|원칙|리밸런싱|비중|현금|포트폴리오|장기|적립|분산",
    "버팀·체념": r"버티|버틴|존버|기다리|견디|묵히|물타|참는|지나가리",
}
TITLE = {  # 제목 꼴
    "숫자": r"\d", "금액": r"\d[\d,.]*\s*(조|억|만 ?원|달러|원)", "퍼센트": r"[−\-+]?\d+(\.\d+)?\s*%", "티커": r"\b(SOXL|TQQQ|QQQ|QLD|VOO|SPY|SCHD|JEPI|JEPQ|SOXX|NVDA|TSLA)\b",
    "질문": r"\?|까\b|까요|나요|일까|할까|될까", "따옴표": r"[\"“”‘’']", "대비·반전": r"\bvs\b|VS|개인은|월가는|반대|정반대|하지만|그런데",
    "공포 낱말": r"폭락|공포|털렸|증발|청산|폭탄|위기|무너|박살|반토막|손실|망했|대폭락|급락",
    "희망 낱말": r"반등|바닥|기회|대폭등|신호|상승|회복|저점",
    "월가·큰손": r"월가|큰손|헤지펀드|버핏|드러켄밀러|손정의|피터 ?틸|기관|외국인",
    "한국 개인": r"서학개미|개미|동학개미|한국 개인",
    "세금·제도": r"세금|양도세|양도소득세|건보료|건강보험|배당소득세|ISA|연금저축|금투세",
}


def log(stage: str, level: int = logging.INFO, **kv) -> None:
    ts = dt.datetime.now(KST).isoformat(timespec="seconds")
    logging.log(level, f"[{stage}] [{ts}] " + " ".join(f"{k}={v}" for k, v in kv.items()))


def read_json(p: Path, default=None):
    try:
        return json.loads(p.read_text("utf-8"))
    except Exception:
        return default


# ─────────────────────────────── 시장 국면
def us_close_utc(d: str) -> dt.datetime:
    """미국 장 마감(16:00 뉴욕)의 UTC 시각 — 서머타임(3월 둘째 일요일 ~ 11월 첫 일요일)이면 20:00, 아니면 21:00."""
    day = dt.date.fromisoformat(d)

    def nth_sunday(y, m, n):
        x = dt.date(y, m, 1)
        x += dt.timedelta(days=(6 - x.weekday()) % 7)
        return x + dt.timedelta(weeks=n - 1)
    edt = nth_sunday(day.year, 3, 2) <= day < nth_sunday(day.year, 11, 1)
    return dt.datetime(day.year, day.month, day.day, 20 if edt else 21, tzinfo=dt.timezone.utc)


def regime_at(pub: dt.datetime, M: dict) -> dict:
    """올린 시각 → 바로 전 미국 장(앞 2거래일 안)의 국면 + 그날 숫자. 자료가 없으면 {}."""
    spx = M.get("^GSPC") or {}
    days = sorted(d for d in spx if us_close_utc(d) <= pub)
    if not days:
        return {}
    last2 = days[-2:]

    def ch(sym, d):
        x = (M.get(sym) or {}).get(d)
        return x["chg"] if x and x["chg"] is not None else None
    sox = [c for c in (ch("^SOX", d) for d in last2) if c is not None]
    ndq = [c for c in (ch("^IXIC", d) for d in last2) if c is not None]
    d0 = days[-1]
    vix = ((M.get("^VIX") or {}).get(d0) or {}).get("close")
    ndq_hi = ((M.get("^IXIC") or {}).get(d0) or {}).get("from_high")
    if (sox and min(sox) <= CRASH_SOX) or (ndq and min(ndq) <= CRASH_NDQ):
        reg = "폭락 직후"
    elif (sox and max(sox) >= JUMP_SOX) or (ndq and max(ndq) >= JUMP_NDQ):
        reg = "급등 직후"
    elif vix is not None and vix >= FEAR_VIX:
        reg = "공포"
    elif ndq_hi is not None and ndq_hi <= CORR_NDQ:
        reg = "조정"
    else:
        reg = "평온"
    ks = M.get("^KS11") or {}
    kclose = lambda d: dt.datetime.fromisoformat(d + "T06:30:00+00:00")   # 코스피 마감 15:30 KST
    kd = sorted(d for d in ks if kclose(d) <= pub)
    k0 = kd[-1] if kd else None
    kchg = (ks.get(k0) or {}).get("chg") if k0 else None
    return {"regime": reg, "us_day": d0, "sox": ch("^SOX", d0), "ndq": ch("^IXIC", d0), "spx": ch("^GSPC", d0), "vix": vix, "ndq_from_high": ndq_hi,
            "soxl": ch("SOXL", d0), "kospi_day": k0, "kospi": kchg, "kospi_drop": bool(kchg is not None and kchg <= KOSPI_DROP),
            "sox_min2": min(sox) if sox else None, "ndq_min2": min(ndq) if ndq else None}


# ─────────────────────────────── 영상 하나
def load_comments(folder: str, vid: str) -> list[dict]:
    p = ROOT / folder / "result/outliers" / f"W_{vid}" / "comments.jsonl"
    if not p.is_file():
        return []
    seen, out = set(), []
    for ln in p.open(encoding="utf-8"):
        try:
            c = json.loads(ln)
        except json.JSONDecodeError:
            continue
        if c.get("id") in seen:
            continue
        seen.add(c.get("id"))
        out.append(c)
    return out


def comment_stats(cms: list[dict], pub: dt.datetime | None) -> dict:
    top = [c for c in cms if not c.get("parent") and not c.get("creator")]
    out = {"n": len(cms), "top": len(top)}
    if pub and cms:
        hrs = []
        for c in cms:
            try:
                hrs.append((dt.datetime.fromisoformat(str(c["published"])[:19] + "+00:00") - pub).total_seconds() / 3600)
            except (KeyError, ValueError):
                pass
        if hrs:
            out["first24"] = round(sum(1 for h in hrs if h < 24) / len(hrs) * 100)
            byday = Counter(int(h // 24) for h in hrs if h >= 0)
            out["peak_day"] = max(byday.items(), key=lambda kv: kv[1])[0] if byday else None
            out["first_h"] = round(min(hrs), 1)
    for k, rx in PSY.items():
        out[k] = round(sum(1 for c in top if re.search(rx, str(c.get("text", "")))) / len(top) * 100) if top else None
    out["best"] = [{"likes": c.get("likes", 0), "text": re.sub(r"\s+", " ", str(c.get("text", "")))[:110]}
                   for c in sorted(top, key=lambda c: -(c.get("likes") or 0))[:3]]
    return out


def channel_base(folder: str, vid: str, ch_id: str, pub: dt.datetime | None) -> dict:
    """채널 다른 영상(올린 지 7일 넘은 것 · 이 영상 앞뒤 90일) 조회수 가운데값 + 이 영상 전 최고."""
    C = ROOT / folder / "result/outliers/.cache"
    up = read_json(C / f"uploads_{ch_id}.json", {}) or {}
    vs, before = [], []
    for i in up.get("ids") or []:
        if i == vid:
            continue
        d = read_json(C / f"{i}.json")
        if not d or not d.get("published") or d.get("view_count") is None:
            continue
        try:
            p = dt.datetime.fromisoformat(d["published"].replace("Z", "+00:00"))
            f = dt.datetime.fromisoformat(d["fetched"]) if d.get("fetched") else None
        except ValueError:
            continue
        if f and (f - p).days < 7:
            continue
        if pub and abs((p - pub).days) > 90:
            continue
        vs.append(int(d["view_count"]))
        if pub and p < pub:
            before.append(int(d["view_count"]))
    return {"n": len(vs), "median": int(st.median(vs)) if vs else None, "best_before": max(before) if before else None,
            "first_hit": bool(before) and False}


def title_feats(t: str) -> list[str]:
    return [k for k, rx in TITLE.items() if re.search(rx, t)]


def thumb_codes(folder: str) -> dict:
    p = ROOT / folder / "result/outliers/thumb_codes_v2.tsv"
    out = {}
    if p.is_file():
        rd = csv.reader((ln for ln in p.open(encoding="utf-8") if not ln.startswith("#")), delimiter="\t")
        head = next(rd, None)
        for row in rd:
            if head and len(row) >= len(head) - 1:
                d = dict(zip(head, row))
                out[d.get("id")] = d
    return out


# ─────────────────────────────── 모으기
def collect(folder: str) -> tuple[list[dict], dict]:
    import studio_board as sb
    M = md.load(folder)
    rows, cnt = sb.success_rows(folder, None, {})
    th = thumb_codes(folder)
    C = ROOT / folder / "result/outliers"
    out = []
    for r in rows:
        meta = read_json(C / f"W_{r['id']}" / "metadata.json", {}) or {}
        cache = read_json(C / ".cache" / f"{r['id']}.json", {}) or {}
        pub_s = meta.get("published_at") or cache.get("published")
        pub = dt.datetime.fromisoformat(pub_s.replace("Z", "+00:00")) if pub_s and "T" in pub_s else None
        ch_id = meta.get("channel_id") or cache.get("channel_id") or ""
        likes = meta.get("likes") if meta.get("likes") is not None else cache.get("like_count")
        reg = regime_at(pub, M) if pub else {}
        cs_ = comment_stats(load_comments(folder, r["id"]), pub)
        base = channel_base(folder, r["id"], ch_id, pub) if ch_id else {}
        k = pub.astimezone(KST) if pub else None
        out.append({**r, "pub": pub_s, "kst": k.strftime("%m-%d %a %H시") if k else "", "dow": "월화수목금토일"[k.weekday()] if k else "",
                    "hour": k.hour if k else None, "like": round(int(likes) / max(r["v"], 1) * 100, 2) if likes not in (None, "") else None,
                    "reg": reg, "cm": cs_, "base": base, "ratio_ch": round(r["v"] / base["median"], 1) if base.get("median") else None,
                    "first_hit": bool(base.get("best_before") is not None and r["v"] >= 3 * max(base["best_before"], 1)),
                    "tf": title_feats(r["t"]), "thumb": th.get(r["id"], {})})
    log("COLLECT", folder=folder, success=len(out), with_comments=sum(1 for x in out if x["cm"]["n"]), with_regime=sum(1 for x in out if x["reg"]),
        with_base=sum(1 for x in out if x["base"].get("median")), thumbs=sum(1 for x in out if x["thumb"]))
    return out, cnt


def pool_rates(folder: str, M: dict, S: dict) -> dict:
    """비교 집단(compare.csv · 성공 판정과 같은 범위) 의 국면별 영상 수·성공 수."""
    p = ROOT / folder / "result/outliers/compare.csv"
    tot, suc = Counter(), Counter()
    tt, ts_, ft, fs = Counter(), Counter(), Counter(), Counter()     # v1.1 (국면, 묶음) · (국면, 제목 꼴)
    C = ROOT / folder / "result/outliers/.cache"
    if not p.is_file():
        return {}
    for r in csv.DictReader(p.open(encoding="utf-8-sig")):
        if r.get("exclude") or not HANGUL.search(r.get("title", "")):
            continue
        try:
            subs, v, a, m = float(r["subs"] or 0), float(r["views"] or 0), float(r["age_days"] or 0), float(r["minutes"] or 0)
        except ValueError:
            continue
        if subs > S["MAX_SUBS"] or m < S["MIN_MINUTES"] or not (S["MIN_AGE_DAYS"] <= a <= S["MAX_AGE_DAYS"]):
            continue
        d = read_json(C / f"{r['id']}.json", {}) or {}
        ps = d.get("published")
        if not ps:
            continue
        reg = regime_at(dt.datetime.fromisoformat(ps.replace("Z", "+00:00")), M).get("regime")
        if not reg:
            continue
        tot[reg] += 1
        x = {"subs": subs, "views": v, "age_days": a, "views_per_day": v / max(a, 1)}
        ok = orr.success_core(x, S)
        if ok:
            suc[reg] += 1
        for key in (reg, "전체"):
            th = r.get("theme") or "(없음)"
            tt[(key, th)] += 1
            ts_[(key, th)] += ok
            for f in title_feats(r.get("title", "")):
                ft[(key, f)] += 1
                fs[(key, f)] += ok
    out = {g: {"pool": tot[g], "success": suc[g], "rate": round(suc[g] / tot[g] * 100, 1) if tot[g] else None} for g in REGIMES}
    out["_theme"] = {f"{k[0]}|{k[1]}": [tt[k], ts_[k]] for k in tt}
    out["_title"] = {f"{k[0]}|{k[1]}": [ft[k], fs[k]] for k in ft}
    return out


# ─────────────────────────────── 문서
def pct(x):
    return "–" if x is None else f"{x}%"


def write(folder: str, rows: list[dict], cnt: dict, rates: dict, M: dict) -> Path:
    od = ROOT / folder / "result/next_topic"
    (od / "success_why").mkdir(parents=True, exist_ok=True)
    # CSV
    cols = ["id", "t", "ch", "s", "v", "vs", "a", "kst", "regime", "us_day", "sox", "ndq", "vix", "kospi", "ratio_ch", "first_hit", "like",
            "cm_n", "first24", "peak_day"] + list(PSY) + ["title_feats", "thumb_bg", "thumb_person", "thumb_frame", "theme", "q"]
    with (od / "success_reasons.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for x in rows:
            g, c = x["reg"], x["cm"]
            w.writerow([x["id"], x["t"], x["ch"], x["s"], x["v"], x["vs"], x["a"], x["kst"], g.get("regime"), g.get("us_day"), g.get("sox"), g.get("ndq"),
                        g.get("vix"), g.get("kospi"), x["ratio_ch"], int(x["first_hit"]), x["like"], c["n"], c.get("first24"), c.get("peak_day")]
                       + [c.get(k) for k in PSY] + ["·".join(x["tf"]), x["thumb"].get("bg", ""), x["thumb"].get("person", ""), x["thumb"].get("frame", ""),
                                                     x.get("th", ""), "·".join((x.get("q") or []) + (x.get("qa") or []))])
    L = []
    A = L.append
    S = cnt.get("rules") or {}
    A("# 성공 사례 전부 — 왜 됐나 · 시기(시장 국면)·시청자 심리\n")
    A(f"VERSION: {VERSION} — {dt.date.today().isoformat()} — `tools/success_reasons.py {VERSION}` 가 만듦 (손으로 고치지 않음 — 해석은 `next_topic.md`·영상별 문서).")
    A('사용자 지시 2026-11-28 "시기에 맞는 주제를 찾는게 지금 너가 할일이야 … 시청자들이 어떤 심리여서 무슨 영상을 찾게되는지 … 권하는 순서 1,2 진행해봐".\n')
    A("※ 연구·교육용 — 투자 조언이 아님. 클릭률·시청 지속률·유입 경로는 공개 자료에 없음 → 시장 숫자·댓글·채널 평소 대비로 미루어 봄. 댓글 심리는 낱말 세기(사람 분류 아님).\n")
    A("## 0. 자료\n")
    n_c = sum(1 for x in rows if x["cm"]["n"])
    A(f"- 성공 사례 **{len(rows)}개** (판 ① 목록과 같은 판정 — 구독자 5만 이하 · 구독자 구간별 조회수 하한 · 구독자당 하루 조회수 {S.get('MIN_VPD_SUBS')} 이상 · {S.get('MIN_AGE_DAYS')}~{S.get('MAX_AGE_DAYS')}일 · {S.get('MIN_MINUTES')}분 이상 · 외국·제외 뺌) · 댓글 받은 것 {n_c} · 비교 집단 {cnt.get('compare'):,}")
    mm = read_json(ROOT / folder / "result/next_topic/market/market.json", {}) or {}
    A(f"- 시장 숫자: `tools/market_data.py` (Yahoo Finance 종가 · {mm.get('updated', '?')[:10]} 받음) — S&P500 · 나스닥 · 필라델피아 반도체(SOX) · 코스피 · VIX · 원/달러 · SOXL·TQQQ·엔비디아·테슬라·삼성전자·SK하이닉스")
    A(f"- 국면 = 올린 시각 바로 전 미국 장 마감(한국 다음 날 05~06시) 기준 앞 2거래일: **폭락 직후**(반도체 ≤ {CRASH_SOX:.0f}% 또는 나스닥 ≤ {CRASH_NDQ:.0f}%) · **급등 직후**(반도체 ≥ +{JUMP_SOX:.0f}% 또는 나스닥 ≥ +{JUMP_NDQ:.0f}%) · **공포**(VIX ≥ {FEAR_VIX:.0f}) · **조정**(나스닥 고점 대비 {CORR_NDQ:.0f}% 아래) · **평온**.\n")
    # 1 시기
    A("## 1. 시기 — 어떤 시장 날에 올린 영상이 성공했나\n")
    A("| 국면 | 비교 집단 영상 | 그중 성공 사례 | 성공 비율 | 성공 사례 몫 |")
    A("|---|---|---|---|---|")
    total_s = sum(1 for x in rows if x["reg"])
    for g in REGIMES:
        rt = rates.get(g) or {}
        ns = sum(1 for x in rows if x["reg"].get("regime") == g)
        A(f"| {g} | {rt.get('pool', 0):,} | {rt.get('success', 0):,} | {pct(rt.get('rate'))} | {ns} ({round(ns / max(total_s, 1) * 100)}%) |")
    allp = sum((rates.get(g) or {}).get("pool", 0) for g in REGIMES)
    alls = sum((rates.get(g) or {}).get("success", 0) for g in REGIMES)
    A(f"\n전체 성공 비율 {round(alls / max(allp, 1) * 100, 1)}% ({alls:,}/{allp:,}). '비교 집단' = compare.csv 중 성공 판정과 같은 범위(제외·외국·4분 미만·구독자 5만 넘음 뺌 · 7~180일).")
    kd = [x for x in rows if x["reg"].get("kospi_drop")]
    A(f"- 코스피 급락(올린 때 바로 전 코스피 장 ≤ {KOSPI_DROP:.0f}%) 뒤 올린 성공 사례: {len(kd)}개.")
    dow = Counter(x["dow"] for x in rows if x["dow"])
    A("- 올린 요일(한국): " + " · ".join(f"{d} {dow.get(d, 0)}" for d in "월화수목금토일"))
    hrs = Counter((x["hour"] // 3) * 3 for x in rows if x["hour"] is not None)
    A("- 올린 시각(한국, 3시간 묶음): " + " · ".join(f"{h:02d}~{h + 2:02d}시 {hrs.get(h, 0)}" for h in range(0, 24, 3)) + "\n")
    # 2 심리 by regime
    A("## 2. 시기별 시청자 심리 — 성공 사례 댓글 (답글 아닌 댓글 중 그 낱말이 든 몫, 영상마다 낸 값의 가운데값)\n")
    A("| 국면 | 영상(댓글 있음) | " + " | ".join(PSY) + " |")
    A("|---|---|" + "---|" * len(PSY))
    for g in REGIMES:
        xs = [x for x in rows if x["reg"].get("regime") == g and x["cm"].get("top")]
        if not xs:
            continue
        A(f"| {g} | {len(xs)} | " + " | ".join(pct(round(st.median(x['cm'][k] for x in xs))) for k in PSY) + " |")
    A("")
    # 3 title feats by regime
    A("## 3. 시기별 제목 꼴 (성공 사례 중 그 꼴이 든 몫)\n")
    A("| 국면 | 성공 사례 | " + " | ".join(TITLE) + " |")
    A("|---|---|" + "---|" * len(TITLE))
    for g in REGIMES:
        xs = [x for x in rows if x["reg"].get("regime") == g]
        if xs:
            A(f"| {g} | {len(xs)} | " + " | ".join(f"{round(sum(1 for x in xs if k in x['tf']) / len(xs) * 100)}%" for k in TITLE) + " |")
    A("")
    # 4 themes by regime
    A("## 4. 시기별 주제 묶음 (분석기 묶음 · 성공 사례 수)\n")
    themes = Counter(x.get("th") or "(없음)" for x in rows)
    tlist = [t for t, _ in themes.most_common(10)]
    A("| 묶음 | 전체 | " + " | ".join(REGIMES) + " |")
    A("|---|---|" + "---|" * len(REGIMES))
    for t in tlist:
        A(f"| {t} | {themes[t]} | " + " | ".join(str(sum(1 for x in rows if (x.get('th') or '(없음)') == t and x['reg'].get('regime') == g)) for g in REGIMES) + " |")
    A("")
    # 4-1 · 4-2 pool rates (v1.1)
    def rate_table(kind, labels, title):
        tb = rates.get(kind) or {}
        A(title)
        A("| " + ("묶음" if kind == "_theme" else "제목 꼴") + " | 전체 | " + " | ".join(REGIMES) + " |")
        A("|---|---|" + "---|" * len(REGIMES))
        for lab in labels:
            cells = []
            for key in ["전체"] + REGIMES:
                n, k = tb.get(f"{key}|{lab}", [0, 0])
                cells.append(f"**{round(k / n * 100, 1)}%** ({k}/{n})" if n >= 15 and key != "전체" and n and k / n * 100 >= 2 * max(alls / max(allp, 1) * 100, 0.1)
                             else (f"{round(k / n * 100, 1)}% ({k}/{n})" if n >= 15 else (f"({k}/{n})" if n else "–")))
            A(f"| {lab} | " + " | ".join(cells) + " |")
        A(f"\n비율 = 비교 집단 중 성공 사례 몫 (표본 15개 아래는 괄호만) · **굵게** = 전체 성공 비율({round(alls / max(allp, 1) * 100, 1)}%)의 2배 이상.\n")
    th_all = sorted({k.split("|", 1)[1] for k in (rates.get("_theme") or {}) if k.startswith("전체|")}, key=lambda t: -(rates["_theme"].get(f"전체|{t}", [0, 0])[0]))
    rate_table("_theme", th_all[:12], "## 4-1. 시기별 주제 묶음 성공 비율 (비교 집단 — 어떤 때 어떤 주제가 잘 되나)\n")
    rate_table("_title", list(TITLE), "## 4-2. 시기별 제목 꼴 성공 비율 (비교 집단)\n")
    # 5 thumbnails
    tx = [x for x in rows if x["thumb"]]
    if tx:
        A(f"## 5. 시기별 썸네일 꼴 (Claude 가 그림을 보고 분류 — `thumb_codes_v2.tsv` · {len(tx)}장)\n")
        for key, lab in (("bg", "바탕"), ("person", "인물"), ("frame", "문구 꼴")):
            vals = [v for v, _ in Counter(x["thumb"].get(key, "") for x in tx).most_common(6) if v]
            A(f"| {lab} | 전체 | " + " | ".join(REGIMES) + " |")
            A("|---|---|" + "---|" * len(REGIMES))
            for v in vals:
                A(f"| {v} | {sum(1 for x in tx if x['thumb'].get(key) == v)} | " + " | ".join(
                    str(sum(1 for x in tx if x['thumb'].get(key) == v and x['reg'].get('regime') == g)) for g in REGIMES) + " |")
            A("")
    # 6 spread
    A("## 6. 어떻게 퍼졌나 — 채널 평소 대비 · 댓글이 몰린 때\n")
    rc = [x["ratio_ch"] for x in rows if x["ratio_ch"]]
    A(f"- 채널 평소(같은 채널 다른 영상 앞뒤 90일 · 7일 넘은 것) 대비 조회수: 가운데값 **{st.median(rc):.1f}배** ({len(rc)}개) · 10배 넘음 {sum(1 for v in rc if v >= 10)} · 3배 아래 {sum(1 for v in rc if v < 3)}" if rc else "- 채널 평소 자료 없음")
    fh = [x for x in rows if x["first_hit"]]
    A(f"- **채널 첫 히트**(이 영상 전 최고의 3배 넘음): {len(fh)}개")
    f24 = [x["cm"]["first24"] for x in rows if x["cm"].get("first24") is not None]
    if f24:
        A(f"- 댓글 중 올린 뒤 24시간 안 몫: 가운데값 {st.median(f24):.0f}% · 80% 넘음(첫날 폭발) {sum(1 for v in f24 if v >= 80)} · 20% 아래(늦게 퍼짐) {sum(1 for v in f24 if v < 20)}")
    A("")
    # 7 now
    A("## 7. 지금 시장 (받은 마지막 거래일)\n")
    spx = M.get("^GSPC") or {}
    if spx:
        d0 = sorted(spx)[-1]
        now = regime_at(us_close_utc(d0) + dt.timedelta(hours=1), M)
        A(f"- 미국 {d0} 마감 기준 국면: **{now.get('regime')}** · 나스닥 {now.get('ndq'):+.1f}% (고점 대비 {now.get('ndq_from_high'):.1f}%) · 반도체 {now.get('sox'):+.1f}% · VIX {now.get('vix'):.1f} · SOXL {now.get('soxl'):+.1f}%")
        for sym in ("^SOX", "^KS11", "005930.KS", "000660.KS", "SOXL", "NVDA", "KRW=X"):
            x = (M.get(sym) or {})
            if x:
                dl = sorted(x)[-1]
                last20 = sorted(x)[-21:]
                c20 = round((x[dl]["close"] / x[last20[0]]["close"] - 1) * 100, 1) if len(last20) > 1 else None
                A(f"  - {md.SYMBOLS[sym][0]}: {dl} {x[dl]['chg']:+.1f}% · 20거래일 {c20:+.1f}% · 1년 고점 대비 {x[dl]['from_high']:.1f}%")
    A("")
    # 8 table
    A(f"## 8. 성공 사례 {len(rows)}개 (구독자당 하루 조회수 큰 순)\n")
    A("| # | 올린 때(한국) | 국면 | 제목 | 채널 | 구독자 | 조회수 | 점수 | 채널 평소 대비 | 댓글 | 24시간 몫 | 심리 상위 | 제목 꼴 |")
    A("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for i, x in enumerate(sorted(rows, key=lambda x: -(x["vs"] or 0)), 1):
        c = x["cm"]
        psy = sorted(((k, c.get(k) or 0) for k in PSY), key=lambda kv: -kv[1])[:2] if c.get("top") else []
        t = x["t"].replace("|", "｜")[:50]
        A(f"| {i} | {x['kst']} | {x['reg'].get('regime', '–')}{' · 코스피↓' if x['reg'].get('kospi_drop') else ''} | [{t}](https://www.youtube.com/watch?v={x['id']}) | "
          f"{x['ch'][:10].replace('|', '｜')} | {x['s']:,} | {x['v']:,} | {x['vs']:.2f} | {('%.1f배' % x['ratio_ch']) if x['ratio_ch'] else '–'}{' · 첫 히트' if x['first_hit'] else ''} | "
          f"{c['n'] or '–'} | {pct(c.get('first24'))} | {' · '.join(f'{k} {v}%' for k, v in psy if v) or '–'} | {'·'.join(x['tf']) or '–'} |")
    p = od / "success_why" / "00_all.md"
    p.write_text("\n".join(L) + "\n", "utf-8")
    log("WRITE", md=str(p.relative_to(ROOT)), csv=str((od / "success_reasons.csv").relative_to(ROOT)), kb=round(p.stat().st_size / 1024, 1))
    return p


def build(folder: str) -> int:
    t0 = time.time()
    import studio_board as sb
    S = sb.success_rules(folder)
    M = md.load(folder)
    if not M:
        log("BUILD", logging.WARNING, folder=folder, note="시장 숫자 없음 — python3 tools/market_data.py <주제> fetch 먼저")
        return 1
    rows, cnt = collect(folder)
    rates = pool_rates(folder, M, S)
    log("RATES", **{g: f"{(rates.get(g) or {}).get('success', 0)}/{(rates.get(g) or {}).get('pool', 0)}" for g in REGIMES}, themes=len(rates.get("_theme") or {}))
    write(folder, rows, cnt, rates, M)
    log("DONE", folder=folder, success=len(rows), sec=round(time.time() - t0, 1))
    return 0


def selftest() -> int:
    ok = True

    def check(name, cond):
        nonlocal ok
        print(("PASS " if cond else "FAIL ") + name)
        ok = ok and bool(cond)
    check("미국 장 마감 UTC — 겨울 21시 · 여름 20시", us_close_utc("2026-11-20").hour == 21 and us_close_utc("2026-07-15").hour == 20)
    M = {"^GSPC": {"2026-11-19": {"close": 1, "chg": -1, "from_high": -2}, "2026-11-20": {"close": 1, "chg": -3.7, "from_high": -6}},
         "^SOX": {"2026-11-20": {"close": 1, "chg": -10.7, "from_high": -40}}, "^IXIC": {"2026-11-20": {"close": 1, "chg": -5.3, "from_high": -12}},
         "^VIX": {"2026-11-20": {"close": 35.9, "chg": 20, "from_high": 0}}, "^KS11": {"2026-11-20": {"close": 1, "chg": -5.2, "from_high": -40}}}
    r = regime_at(dt.datetime(2026, 11, 21, 10, tzinfo=dt.timezone.utc), M)
    check("11-21 10:00 UTC = 11-20 미국 장 폭락 직후 · 코스피 급락", r["regime"] == "폭락 직후" and r["us_day"] == "2026-11-20" and r["kospi_drop"])
    r2 = regime_at(dt.datetime(2026, 11, 20, 20, tzinfo=dt.timezone.utc), M)
    check("마감 전(20:00 UTC)이면 전날 장", r2["us_day"] == "2026-11-19")
    cs_ = comment_stats([{"id": "a", "parent": None, "published": "2026-11-21T11:00:00", "text": "물렸다 반등 오나요?", "likes": 3},
                         {"id": "b", "parent": "a", "published": "2026-11-23T11:00:00", "text": "감사", "likes": 0}], dt.datetime(2026, 11, 21, 10, tzinfo=dt.timezone.utc))
    check("댓글 심리·24시간 몫", cs_["손실·공포"] == 100 and cs_["희망·바닥"] == 100 and cs_["궁금·질문"] == 100 and cs_["first24"] == 50 and cs_["top"] == 1)
    check("제목 꼴", set(title_feats("“SOXL 개미 다 털렸다”…6.2조 원 걸린 서학개미, 계산해 보니")) >= {"티커", "따옴표", "공포 낱말", "한국 개인", "금액"})
    print("selftest:", "OK" if ok else "FAIL")
    return 0 if ok else 1


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="성공 사례 전부 — 왜 됐나 · 시기·심리")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    ap.add_argument("folder", nargs="?", default="stock")
    ap.add_argument("cmd", nargs="?", default="build", choices=["build", "selftest"])
    a = ap.parse_args(argv)
    logging.basicConfig(level=getattr(logging, a.log_level), format="%(message)s", stream=sys.stdout)
    if a.folder == "selftest" or a.cmd == "selftest":
        return selftest()
    return build(a.folder)


if __name__ == "__main__":
    raise SystemExit(main())
