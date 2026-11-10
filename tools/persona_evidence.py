#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-11-10 — 새로: '판단용 페르소나'(stock/guides/persona_judge.md)의 근거 숫자·원문을 **원자료에서 직접** 다시 뽑는 도구
#   (사용자 지시 2026-11-10 "저장소에 분석 결과 자료(제목, 썸네일 문구, 댓글 등)를 보고 … 페르소나 파일 만들어 … 분석 자료가 잘못된게 있을 수 있으니
#    확인하면서 최대한 날것의 자료를 보도록 해").
#   · 읽는 것(가공 전 자료): <주제>/result/outliers/W_*/metadata.json · comments.jsonl · compare.csv · thumb_codes.tsv · persona_sample_labels.tsv
#     (analysis.md·personas.md·content_analysis 같은 2차 결과는 읽지 않음 — 그 숫자를 검산하려는 도구)
#   · 거르는 것(설정 <주제>/persona_judge.toml): 외국 영상 · 주제 밖 · 댓글 이벤트 영상 · 방송 뉴스·정치 · 같은 댓글 중복 줄 · 채널 주인 · 도배
#   · 내는 것: persona_evidence.md (사람이 읽는 표·원문) · persona_evidence.json (같은 숫자)
#       0 자료·걸러낸 것 · 1 영상 묶음 · 2 시청자 처지(손 분류 표본) · 3 제목 특징별 성공 배수 · 4 길이별 · 5 썸네일 문구 · 6 댓글 신호 · 7 시간 표시 · 8 나이
#   · 제목 배수 = 작은 채널(≤5만)·7~180일·4분↑·주제 안 영상끼리, 구독자 구간별 성공률로 기대값을 맞춘 '관찰 ÷ 기대' (상관이지 원인이 아님)
#   · 재현: 무작위는 SEED 고정 · 표준 라이브러리만 · 쓰기는 두 파일뿐 (--check 는 아무것도 안 씀)
#   연구·교육용 — 투자 권유가 아님.
# 사용:
#   python3 tools/persona_evidence.py stock            # 근거 파일 두 개를 다시 만듦
#   python3 tools/persona_evidence.py stock --check    # 계산만 하고 쓰지 않음 (요약 로그)
#   python3 tools/persona_evidence.py --selftest       # 작은 가짜 자료로 계산 검사
import argparse
import collections
import csv
import json
import logging
import math
import random
import re
import statistics
import sys
import time
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VERSION = "v1.0"
LOG = logging.getLogger("persona_evidence")
HANGUL = re.compile(r"[가-힣]")
TS = re.compile(r"(?<!\d)(\d{1,2}):(\d{2})(?::(\d{2}))?(?!\d)")
ME = re.compile(r"저는|제가|저도|전 |난 |나는|내가|나도|저희|제 |내 |우리 ?(집|부부|남편|아내|와이프)")
AGE = re.compile(r"(?<!\d)([2-7])0 ?대|(?<!\d)([2-7]\d) ?(살|세)(?!대)")
LABELS = {"A": "물림·손실 중", "A2": "국장 정리·미장 이동", "B": "지수·레버리지 ETF 적립", "C": "배당·은퇴·파이어(현금흐름)",
          "C2": "계좌·세금 실무", "D": "초보·막 시작", "E": "단타·매매", "G": "수익 경험·훈수", "H": "전문가·유튜버 불신",
          "M": "시황 의견·전망", "O": "그 밖(출연자 칭찬·잡담·무관)"}
GROUPS = {"L_long": "장기·ETF·배당·연금·기초", "M_market": "국내·미국 시황", "P_psy": "심리·실패·투자 일반", "T_trade": "매매·종목·차트",
          "V_lev": "빚투·레버리지", "N_news": "방송 뉴스·정치 (뺌)", "X_off": "주제 밖 (뺌)", "E_event": "댓글 이벤트 (뺌)"}
CORE_OUT = ("N_news", "X_off", "E_event")


def log(stage, level=logging.INFO, **kv):
    ts = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    LOG.log(level, "[%s] [%s] %s", stage, ts, " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) else v}" for k, v in kv.items()))


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def flat(s, n=None):
    s = re.sub(r"\s+", " ", s or "").strip()
    return s if n is None or len(s) <= n else s[:n] + "…"


# ------------------------------------------------------------------ 읽기
def load_cfg(topic):
    p = ROOT / topic / "persona_judge.toml"
    if not p.exists():
        raise SystemExit(f"[ERROR] 설정 없음: {p} — stock/persona_judge.toml 을 본떠 만든다")
    cfg = tomllib.loads(p.read_text("utf-8"))
    ex = cfg["exclude"]
    for k in ("NEWS_CHANNEL", "POLITICS_TITLE", "OFF_TITLE", "SPAM", "POLITICS_COMMENT"):
        ex["_" + k] = re.compile(ex[k])
    for f in cfg.get("title_feature", []) + cfg.get("signal", []):
        f["_re"] = re.compile(f["re"])
    return cfg


def group_of(m, cfg):
    """영상 하나를 묶음에 — 주제 밖·이벤트·뉴스가 먼저, 나머지는 compare.csv 자동 주제(theme)로."""
    ex = cfg["exclude"]
    if m["id"] in ex["OFF"]:
        return "X_off"
    if m["id"] in ex["EVENT"]:
        return "E_event"
    if ex["_NEWS_CHANNEL"].search(m.get("channel", "")) or ex["_POLITICS_TITLE"].search(m.get("title", "")):
        return "N_news"
    t = (m.get("theme") or "")[:2]
    if t in ("2.", "3.", "10", "1."):
        return "L_long"
    if t in ("8.", "11"):
        return "P_psy"
    if t in ("7.", "6."):
        return "T_trade"
    if t == "9.":
        return "V_lev"
    return "M_market"


def dedupe(rows):
    """같은 댓글 ID 가 여러 줄이면 좋아요가 큰 한 줄만 (comments.jsonl 에 이어 받기 중복이 있음)."""
    best = {}
    for r in rows:
        k = r.get("id")
        if k is None:
            continue
        if k not in best or int(r.get("likes") or 0) > int(best[k].get("likes") or 0):
            best[k] = r
    return list(best.values())


def load_raw(topic, cfg):
    base = ROOT / topic / "result" / "outliers"
    theme, flag_success = {}, {}
    for r in csv.DictReader(open(base / "compare.csv", encoding="utf-8-sig")):
        theme[r["id"]] = r.get("theme", "")
    ap = base / "approved.csv"
    if ap.exists():
        for r in csv.DictReader(open(ap, encoding="utf-8-sig")):
            flag_success[r["id"]] = r.get("success") == "True"
    V, C = {}, []
    integ = collections.Counter()
    for d in sorted(base.glob("W_*")):
        mp = d / "metadata.json"
        if not mp.exists():
            integ["no_metadata"] += 1
            continue
        try:
            m = json.loads(mp.read_text("utf-8"))
        except json.JSONDecodeError:
            integ["bad_metadata"] += 1
            LOG.warning("[DATA] metadata 못 읽음 dir=%s", d.name)
            continue
        integ["videos_all"] += 1
        if m.get("foreign"):
            integ["videos_foreign"] += 1
            continue
        m["theme"] = theme.get(m["id"], "")
        m["flag_success"] = flag_success.get(m["id"], False)
        m["has_transcript"] = (d / "transcript.txt").exists()
        m["g"] = group_of(m, cfg)
        V[m["id"]] = m
        rows = []
        cp = d / "comments.jsonl"
        if cp.exists():
            for ln in open(cp, encoding="utf-8"):
                try:
                    rows.append(json.loads(ln))
                except json.JSONDecodeError:
                    integ["bad_comment_lines"] += 1
        integ["comment_rows"] += len(rows)
        uniq = dedupe(rows)
        integ["comment_unique"] += len(uniq)
        if len(rows) != len(uniq):
            integ["videos_with_dup_rows"] += 1
        for c in uniq:
            C.append((m["id"], c.get("id"), c.get("parent"), int(c.get("likes") or 0), c.get("text") or "", bool(c.get("creator"))))
    integ["videos_kr"] = len(V)
    integ["transcripts_kr"] = sum(1 for m in V.values() if m["has_transcript"])
    integ["flag_success_kr"] = sum(1 for m in V.values() if m["flag_success"])
    integ["flag_success_off_topic"] = sum(1 for m in V.values() if m["flag_success"] and m["g"] == "X_off")
    integ["flag_success_news"] = sum(1 for m in V.values() if m["flag_success"] and m["g"] == "N_news")
    return V, C, dict(integ)


def viewers(C, cfg):
    spam = cfg["exclude"]["_SPAM"]
    out, dropped = [], collections.Counter()
    for c in C:
        if c[5]:
            dropped["creator"] += 1
        elif spam.search(c[4]):
            dropped["spam"] += 1
        else:
            out.append(c)
    return out, dict(dropped)


# ------------------------------------------------------------------ 제목 (compare.csv)
def bucket(subs, cuts):
    for i, c in enumerate(cuts):
        if subs < c:
            return i
    return len(cuts)


def build_set_a(topic, cfg):
    p = cfg["set_a"]
    off = cfg["exclude"]["_OFF_TITLE"]
    A, why = [], collections.Counter()
    for r in csv.DictReader(open(ROOT / topic / "result" / "outliers" / "compare.csv", encoding="utf-8-sig")):
        if not HANGUL.search(r["title"]):
            why["not_korean"] += 1
            continue
        if r.get("exclude"):
            why["excluded_by_analyzer"] += 1
            continue
        mi, ag, su, vi = num(r["minutes"]), num(r["age_days"]), num(r["subs"]), num(r["views"])
        if None in (mi, ag, su, vi) or su <= 0:
            why["missing_number"] += 1
            continue
        if mi < p["MIN_MINUTES"] or not (p["MIN_AGE_DAYS"] <= ag <= p["MAX_AGE_DAYS"]) or su > p["MAX_SUBS"]:
            why["outside_range"] += 1
            continue
        if off.search(r["title"]):
            why["off_topic_title"] += 1
            continue
        score = (vi / ag) / max(su, 100)
        A.append({"id": r["id"], "title": r["title"], "channel": r["channel"], "subs": su, "views": vi, "age": ag, "minutes": mi,
                  "score": score, "ok": score >= p["MIN_VPD_SUBS"] and vi >= p["MIN_VIEWS"], "b": bucket(su, p["SUBS_BUCKETS"])})
    return A, dict(why)


def lift(group, rate):
    """관찰 성공 ÷ 기대 성공 (기대 = 그 영상의 구독자 구간 성공률을 더한 값). 95% 구간은 포아송 근사."""
    obs = sum(1 for r in group if r["ok"])
    exp = sum(rate[r["b"]] for r in group)
    if exp <= 0:
        return {"n": len(group), "obs": obs, "exp": 0.0, "lift": None, "lo": None, "hi": None}
    return {"n": len(group), "obs": obs, "exp": round(exp, 2), "lift": round(obs / exp, 2),
            "lo": round(max(0.0, (obs - 1.96 * math.sqrt(obs)) / exp), 2), "hi": round((obs + 1.96 * math.sqrt(obs)) / exp, 2)}


def rates(A):
    b = collections.defaultdict(lambda: [0, 0])
    for r in A:
        b[r["b"]][0] += 1
        b[r["b"]][1] += r["ok"]
    return {k: (v[1] / v[0] if v[0] else 0.0) for k, v in b.items()}


def title_lifts(A, cfg):
    p = cfg["set_a"]
    rate = rates(A)
    by_ch = collections.defaultdict(list)
    for r in A:
        by_ch[r["channel"]].append(r)
    capped_sets = []
    for s in range(30):
        rnd = random.Random(p["SEED"] + s)
        B = []
        for g in by_ch.values():
            g = g[:]
            rnd.shuffle(g)
            B += g[:p["CHANNEL_CAP"]]
        capped_sets.append((B, rates(B)))
    old = [r for r in A if r["age"] >= 30]
    old_rate = rates(old)
    rows = []
    for f in cfg["title_feature"]:
        rx = f["_re"]
        g = [r for r in A if rx.search(r["title"])]
        if not g:
            continue
        L = lift(g, rate)
        ch = collections.Counter(r["channel"] for r in g if r["ok"])
        L["name"] = f["name"]
        L["success_channels"] = len(ch)
        L["top_channel_share"] = round(ch.most_common(1)[0][1] / L["obs"], 2) if L["obs"] else 0.0
        caps = [lift([r for r in B if rx.search(r["title"])], rt)["lift"] for B, rt in capped_sets]
        caps = [x for x in caps if x is not None]
        L["lift_channel_capped"] = round(sum(caps) / len(caps), 2) if caps else None
        L["lift_30d_plus"] = lift([r for r in old if rx.search(r["title"])], old_rate)["lift"]
        L["n_30d_plus"] = sum(1 for r in old if rx.search(r["title"]))
        rows.append(L)
    rows.sort(key=lambda x: -(x["lift"] or 0))
    return rows, rate


def length_lifts(A, rate):
    out = []
    for lo, hi in [(4, 8), (8, 13), (13, 17), (17, 22), (22, 30), (30, 400)]:
        g = [r for r in A if lo <= r["minutes"] < hi]
        L = lift(g, rate)
        L["range"] = f"{lo}~{hi if hi < 400 else ''}분"
        out.append(L)
    for lo, hi in [(0, 30), (30, 40), (40, 50), (50, 60), (60, 200)]:
        g = [r for r in A if lo <= len(r["title"]) < hi]
        L = lift(g, rate)
        L["range"] = f"제목 {lo}~{hi if hi < 200 else ''}자"
        out.append(L)
    return out


def crash_share(topic):
    mo = collections.defaultdict(lambda: [0, 0])
    rx = re.compile(r"폭락|급락|붕괴|서킷|검은 ?(월|화|수|목|금)|패닉|투매|하락장")
    for r in csv.DictReader(open(ROOT / topic / "result" / "outliers" / "compare.csv", encoding="utf-8-sig")):
        if not HANGUL.search(r["title"]) or r.get("exclude") or not r.get("published"):
            continue
        m = mo[r["published"][:7]]
        m[0] += 1
        m[1] += bool(rx.search(r["title"]))
    months = sorted(mo)[-7:]
    return [{"month": k, "titles": mo[k][0], "crash": mo[k][1], "share": round(mo[k][1] / mo[k][0], 3)} for k in months]


# ------------------------------------------------------------------ 썸네일 (성공 사례만 — 비교 집단 없음)
def thumb_stats(topic, V):
    p = ROOT / topic / "result" / "outliers" / "thumb_codes.tsv"
    if not p.exists():
        return None
    R = []
    for ln in open(p, encoding="utf-8"):
        if ln.startswith("#"):
            continue
        c = ln.rstrip("\n").split("\t")
        if len(c) < 7 or c[1] not in V:
            continue
        m = V[c[1]]
        if m["g"] in CORE_OUT:
            continue
        R.append({"id": c[1], "image": c[2], "face": c[3], "main": c[5], "sub": c[6], "title": m["title"], "ratio": m["views"] / max(1, m["subs"])})
    if not R:
        return None
    n = len(R)
    L = sorted(len(re.sub(r"\s", "", r["main"])) for r in R)
    feats = {"숫자": r"\d", "금액·기간·%": r"\d+ ?(억|만|천|년|개월|%|배)", "손실·경고 낱말": r"망|잃|물린|폭락|급락|위험|함정|손절|붕괴|증발|날렸|무너|털리|곡소리|위기|도박|반토막|-\d",
             "물음표": r"\?", "방법·법": r"법\b|방법|매매법|투자법", "큰따옴표·작은따옴표": r"[\"“”']", "1인칭 고백": r"했습니다|팔았|샀다|깨달|않아요|떠납니다",
             "종목·상품 이름": r"QLD|TQQQ|S&P|ETF|삼성전자|하이닉스|삼전|닉스|나스닥|코스피|커버드콜|배당"}
    ft = []
    for k, pat in feats.items():
        g = [r for r in R if re.search(pat, r["main"])]
        ft.append({"name": k, "n": len(g), "share": round(len(g) / n, 2), "median_ratio": round(statistics.median(r["ratio"] for r in g), 1) if g else None})

    def words(s):
        return set(re.findall(r"[가-힣A-Za-z0-9&]{2,}", s))
    ov = [len(words(r["main"]) & words(r["title"])) / max(1, len(words(r["main"]))) for r in R]
    voice = [r["sub"] for r in R if re.search(r"[\"“”]|\.\.|!!|ㅋ|~", r["sub"])]
    return {"n": n, "main_len_median": L[n // 2], "main_len_q1": L[n // 4], "main_len_q3": L[3 * n // 4], "has_sub": sum(1 for r in R if r["sub"].strip()),
            "image": collections.Counter(r["image"] for r in R).most_common(), "face": collections.Counter(r["face"] for r in R).most_common(),
            "features": ft, "median_ratio_all": round(statistics.median(r["ratio"] for r in R), 1),
            "title_overlap_median": round(statistics.median(ov), 2), "same_as_title": sum(1 for x in ov if x >= 0.8), "different_from_title": sum(1 for x in ov if x <= 0.2),
            "sub_voice_n": len(voice), "sub_voice_examples": [flat(v, 40) for v in voice[:12]],
            "top": [{"ratio": round(r["ratio"], 1), "main": r["main"], "sub": r["sub"], "title": flat(r["title"], 60)} for r in sorted(R, key=lambda r: -r["ratio"])[:25]]}


# ------------------------------------------------------------------ 댓글 신호
def pick(cs, V, n=6, per_video=2, lo=12, hi=220):
    seen, out = collections.Counter(), []
    for c in sorted(cs, key=lambda c: -c[3]):
        if not (lo <= len(c[4]) <= hi) or seen[c[0]] >= per_video:
            continue
        seen[c[0]] += 1
        out.append({"likes": c[3], "video": c[0], "title": flat(V[c[0]]["title"], 44), "text": flat(c[4], 170)})
        if len(out) >= n:
            break
    return out


def signals(core, cfg, V):
    out = []
    for s in cfg["signal"]:
        cs = [c for c in core if s["_re"].search(c[4])]
        out.append({"key": s["key"], "kind": s["kind"], "name": s["name"], "n": len(cs), "videos": len({c[0] for c in cs}),
                    "likes": sum(c[3] for c in cs), "samples": pick(cs, V)})
    return out


def timestamps(core, V):
    pos, summary = [], 0
    for c in core:
        ms = TS.findall(c[4])
        if not ms:
            continue
        if len(ms) >= 4:
            summary += 1
            continue
        h = ms[0]
        sec = int(h[0]) * 3600 + int(h[1]) * 60 + int(h[2]) if h[2] else int(h[0]) * 60 + int(h[1])
        L = (V[c[0]].get("minutes") or 0) * 60
        if 0 < sec <= L:
            pos.append((sec / L, sec, c))
    dec = collections.Counter(min(9, int(p[0] * 10)) for p in pos)
    early = collections.Counter("0~30초" if p[1] <= 30 else "30~60초" if p[1] <= 60 else "1~2분" if p[1] <= 120 else "2~5분" if p[1] <= 300 else "5분 뒤" for p in pos)
    liked = pick([p[2] for p in pos], V, n=10, per_video=1)
    return {"moment_comments": len(pos), "summary_comments": summary, "videos": len({p[2][0] for p in pos}), "deciles": [dec[i] for i in range(10)],
            "by_time": [(k, early[k]) for k in ("0~30초", "30~60초", "1~2분", "2~5분", "5분 뒤")], "top_liked": liked}


def ages(core_top, V):
    a, by_v = collections.Counter(), collections.Counter()
    for c in core_top:
        if not ME.search(c[4]):
            continue
        m = AGE.search(c[4])
        if m:
            a[(m.group(1) or m.group(2)[0]) + "0대"] += 1
            by_v[c[0]] += 1
    tot = sum(a.values())
    top6 = by_v.most_common(6)
    return {"n": tot, "dist": sorted(a.items()), "top6_share": round(sum(n for _, n in top6) / tot, 2) if tot else 0,
            "top6": [{"title": flat(V[v]["title"], 40), "n": n} for v, n in top6]}


def sample_labels(cfg):
    p = ROOT / cfg["LABEL_SAMPLE"]
    if not p.exists():
        return None
    t, n = collections.Counter(), 0
    for ln in open(p, encoding="utf-8"):
        if ln.startswith("#") or ln.startswith("no\t"):
            continue
        c = ln.rstrip("\n").split("\t")
        if len(c) >= 2 and c[1] in LABELS:
            t[c[1]] += 1
            n += 1
    rows = [{"label": k, "name": LABELS[k], "n": t[k], "share": round(t[k] / n, 3),
             "ci": round(1.96 * math.sqrt((t[k] / n) * (1 - t[k] / n) / n), 3)} for k in LABELS]
    return {"n": n, "rows": rows}


# ------------------------------------------------------------------ 모으기
def build(topic):
    t0 = time.time()
    cfg = load_cfg(topic)
    V, C, integ = load_raw(topic, cfg)
    log("LOAD", topic=topic, videos_all=integ["videos_all"], foreign=integ.get("videos_foreign", 0), korean=integ["videos_kr"],
        comment_rows=integ["comment_rows"], unique=integ["comment_unique"], dup_rows=integ["comment_rows"] - integ["comment_unique"],
        dup_videos=integ.get("videos_with_dup_rows", 0), transcripts=integ["transcripts_kr"], sec=round(time.time() - t0, 1))
    if integ["comment_rows"] != integ["comment_unique"]:
        log("DATA", logging.WARNING, issue="comments.jsonl 에 같은 댓글이 여러 줄", dup_share=round(1 - integ["comment_unique"] / integ["comment_rows"], 3), action="ID 로 중복 제거 뒤 셈")
    if integ["flag_success_off_topic"]:
        log("DATA", logging.WARNING, issue="approved.csv '성공 사례'에 주제 밖 영상", n=integ["flag_success_off_topic"], action="묶음 X_off 로 뺌")
    vw, dropped = viewers(C, cfg)
    gv, gc = collections.Counter(m["g"] for m in V.values()), collections.Counter(V[c[0]]["g"] for c in vw)
    core = [c for c in vw if V[c[0]]["g"] not in CORE_OUT]
    core_top = [c for c in core if not c[2]]
    log("FILTER", viewer_comments=len(vw), creator=dropped.get("creator", 0), spam=dropped.get("spam", 0), core=len(core), core_top_level=len(core_top),
        news=gc["N_news"], off_topic=gc["X_off"], event=gc["E_event"])
    A, why = build_set_a(topic, cfg)
    tl, rate = title_lifts(A, cfg)
    log("TITLE", set_a=len(A), success=sum(r["ok"] for r in A), base=round(sum(r["ok"] for r in A) / len(A), 3), channels=len({r["channel"] for r in A}),
        bucket_rates=json.dumps({k: round(v, 3) for k, v in sorted(rate.items())}), dropped=json.dumps(why, ensure_ascii=False))
    sg = signals(core_top, cfg, V)   # 답글은 서로 다투는 말이 많아 최상위 댓글만
    for s in sg:
        log("SIGNAL", logging.DEBUG, key=s["key"], kind=s["kind"], n=s["n"], videos=s["videos"])
    E = {"tool": f"persona_evidence.py {VERSION}", "config": f"{topic}/persona_judge.toml {cfg.get('VERSION')}", "generated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
         "topic": topic, "integrity": integ, "dropped": dropped,
         "exclude": {"OFF": cfg["exclude"]["OFF"], "EVENT": cfg["exclude"]["EVENT"]},
         "groups": [{"key": k, "name": GROUPS[k], "videos": gv[k], "viewer_comments": gc[k]} for k in GROUPS],
         "core": {"comments": len(core), "top_level": len(core_top), "videos": sum(gv[k] for k in GROUPS if k not in CORE_OUT)},
         "sample": sample_labels(cfg), "crash_titles": crash_share(topic),
         "set_a": {"n": len(A), "success": sum(r["ok"] for r in A), "channels": len({r["channel"] for r in A}), "dropped": why,
                   "bucket_rates": {str(k): round(v, 3) for k, v in sorted(rate.items())}, "cuts": cfg["set_a"]["SUBS_BUCKETS"]},
         "title_lifts": tl, "length_lifts": length_lifts(A, rate),
         "top_titles": [{"score": round(r["score"], 2), "views": int(r["views"]), "subs": int(r["subs"]), "minutes": r["minutes"], "title": flat(r["title"], 70)}
                        for r in sorted([r for r in A if r["ok"]], key=lambda r: -r["score"])[:30]],
         "thumbs": thumb_stats(topic, V), "signals": sg, "timestamps": timestamps(core, V), "ages": ages(core_top, V)}
    E["seconds"] = round(time.time() - t0, 1)
    log("DONE", sec=E["seconds"], signals=len(sg), title_features=len(tl))
    return E


# ------------------------------------------------------------------ 쓰기
def fx(x):
    return "—" if x is None else f"×{x:.2f}"


def render(E):
    I, o = E["integrity"], []
    w = o.append
    w(f"# {E['topic']} 판단용 페르소나 — 근거 (원자료에서 다시 뽑음 · 자동)")
    w("")
    w(f"만든 때 {E['generated']} · `tools/{E['tool']}` · 설정 `{E['config']}` · 손으로 고치지 않는다 (걸러낼 영상·정규식은 설정에서). 읽는 법·판단표는 `{E['topic']}/guides/persona_judge.md`.")
    w("※ 연구·교육용 — 댓글·제목에서 센 숫자이며 투자 권유가 아니다. 정규식 숫자는 거칠다 — 규모의 순서만 보고, 뜻은 아래 원문으로 확인한다.")
    w("")
    w("## 0. 자료와 걸러낸 것")
    w(f"- 승인 영상 {I['videos_all']}개 = 외국 {I.get('videos_foreign', 0)} + **한국 {I['videos_kr']}**. 한국 영상 대본은 {I['transcripts_kr']}개뿐 (대부분 앞 5분) — 대본 근거는 적다.")
    w(f"- 댓글 줄 {I['comment_rows']:,} → **같은 댓글 중복 줄 {I['comment_rows'] - I['comment_unique']:,}개를 빼고** {I['comment_unique']:,}개 (중복이 있던 영상 {I.get('videos_with_dup_rows', 0)}개) → 채널 주인 {E['dropped'].get('creator', 0):,} · 도배 {E['dropped'].get('spam', 0):,} 제외.")
    w(f"- approved.csv '성공 사례' 표시 {I['flag_success_kr']}개 가운데 **주제 밖 {I['flag_success_off_topic']}개** · 뉴스·정치 {I['flag_success_news']}개 — 아래 묶음에서 뺌.")
    w(f"- **핵심 묶음** = 뉴스·주제 밖·이벤트를 뺀 영상 {E['core']['videos']}개의 시청자 댓글 **{E['core']['comments']:,}개** (최상위 {E['core']['top_level']:,}). 2·6·7·8번은 이 묶음.")
    w("")
    w("| 뺀 영상 | 까닭 |")
    w("|---|---|")
    for k, v in E["exclude"]["OFF"].items():
        w(f"| `{k}` | 주제 밖 — {v} |")
    for k, v in E["exclude"]["EVENT"].items():
        w(f"| `{k}` | 이벤트 — {v} |")
    w("")
    w("## 1. 영상 묶음")
    w("| 묶음 | 영상 | 시청자 댓글 |")
    w("|---|---|---|")
    for g in E["groups"]:
        w(f"| {g['name']} | {g['videos']} | {g['viewer_comments']:,} |")
    w("")
    w("제목에 폭락·급락·붕괴·서킷이 든 한국어 영상 몫 (compare.csv, 올린 달): " + " · ".join(f"{c['month'][5:]}월 {c['share']:.0%}({c['crash']}/{c['titles']})" for c in E["crash_titles"]))
    w("")
    S = E["sample"]
    w("## 2. 시청자가 처한 상황 — 손으로 분류한 표본")
    if S:
        w(f"1인칭 댓글에서 무작위 {S['n']}개를 Claude 가 한 줄씩 읽고 분류 (`persona_sample_labels.tsv` — 뽑은 법은 그 파일 머리). ±는 95% 구간.")
        w("")
        w("| 갈래 | 댓글 | 몫 |")
        w("|---|---|---|")
        for r in S["rows"]:
            w(f"| {r['label']} {r['name']} | {r['n']} | {r['share']:.1%} ±{r['ci']:.1%} |")
        own = [r for r in S["rows"] if r["label"] not in ("H", "M", "O")]
        tot = sum(r["n"] for r in own)
        w("")
        w(f"자기 처지가 드러난 {tot}개만 보면: " + " · ".join(f"{r['name']} {r['n'] / tot:.0%}" for r in sorted(own, key=lambda r: -r['n'])))
    w("")
    w("## 3. 제목 특징별 성공 배수 (작은 채널끼리)")
    A = E["set_a"]
    w(f"집단: 한국어 제목 · 주제 안 · 4분 이상 · 올린 지 7~180일 · 구독자 5만 이하 **{A['n']}개**(채널 {A['channels']}) · 성공 {A['success']}개({A['success'] / A['n']:.1%}) = 구독자당 하루 조회수 ≥ 0.1 그리고 조회수 ≥ 1만.")
    w(f"구독자 구간별 성공률이 달라({', '.join(f'{v:.1%}' for v in A['bucket_rates'].values())} — 구간 경계 {A['cuts']}) **배수 = 관찰 ÷ 그 구간 기대**. '채널당 4개'·'30일↑'은 한 채널·갓 올린 영상이 결과를 덮는지 보는 검산.")
    w("")
    w("| 제목 특징 | 영상 | 성공 | 배수 [95%] | 채널당 4개 | 30일↑(영상) | 성공 채널 수 · 최다 채널 몫 |")
    w("|---|---|---|---|---|---|---|")
    for r in E["title_lifts"]:
        w(f"| {r['name']} | {r['n']} | {r['obs']} | **{fx(r['lift'])}** [{r['lo']}~{r['hi']}] | {fx(r['lift_channel_capped'])} | {fx(r['lift_30d_plus'])} ({r['n_30d_plus']}) | {r['success_channels']} · {r['top_channel_share']:.0%} |")
    w("")
    w("읽는 법: 구간이 1을 걸치면 '차이 없음'. 상관이지 원인이 아니다 (같은 채널이 같은 꼴을 반복함 — 최다 채널 몫을 본다).")
    w("")
    w("### 3-1. 작은 채널 성공 제목 30 (구독자당 하루 조회수 순)")
    for r in E["top_titles"]:
        w(f"- {r['score']:.2f} · 조회 {r['views']:,} · 구독 {r['subs']:,} · {r['minutes']:.0f}분 — {r['title']}")
    w("")
    w("## 4. 길이별 성공 배수 (같은 집단)")
    w("| 구간 | 영상 | 성공 | 배수 [95%] |")
    w("|---|---|---|---|")
    for r in E["length_lifts"]:
        w(f"| {r['range']} | {r['n']} | {r['obs']} | {fx(r['lift'])} [{r['lo']}~{r['hi']}] |")
    w("")
    T = E["thumbs"]
    w("## 5. 썸네일 문구 — 성공 사례만 (비교 집단 없음 → '많이 쓰는 꼴'이지 '효과'가 아님)")
    if T:
        w(f"한국·주제 안 성공 썸네일 {T['n']}장 (`thumb_codes.tsv` — Claude 가 그림을 보고 옮김; 2026-11-10 9장을 그림과 대조해 1장 오기를 고침).")
        w(f"- 주요 문구 글자 수(공백 빼고) 가운데값 **{T['main_len_median']}자** (사분위 {T['main_len_q1']}~{T['main_len_q3']}) · 보조 문구 있음 {T['has_sub']}장.")
        w(f"- 제목과 같은 낱말 몫 가운데값 {T['title_overlap_median']:.0%} — 제목과 거의 같음 {T['same_as_title']}장 · 거의 다름 {T['different_from_title']}장.")
        w("- 그림: " + " · ".join(f"{k} {v}" for k, v in T["image"]) + " / 표정: " + " · ".join(f"{k} {v}" for k, v in T["face"]))
        w("- 주요 문구 특징: " + " · ".join(f"{f['name']} {f['share']:.0%}" for f in T["features"]))
        w(f"- 보조 문구가 '사람 말'(따옴표·말줄임) {T['sub_voice_n']}장: " + " / ".join(T["sub_voice_examples"]))
        w("")
        w("| 배수 | 주요 문구 | 보조 문구 | 제목 |")
        w("|---|---|---|---|")
        for r in T["top"]:
            w(f"| {r['ratio']} | {r['main']} | {r['sub']} | {r['title']} |")
    w("")
    w("## 6. 댓글 신호 — 떠나는 까닭 · 계속 보는 까닭 · 믿음 · 제목 반응")
    names = {"leave": "떠나는 까닭", "keep": "계속 보는 까닭", "trust": "믿음·불신", "click": "제목·썸네일 반응"}
    for kind in ("leave", "keep", "trust", "click"):
        w(f"### {names[kind]}")
        for s in [s for s in E["signals"] if s["kind"] == kind]:
            w(f"**{s['name']}** — 댓글 {s['n']:,} · 영상 {s['videos']} · 좋아요 합 {s['likes']:,}")
            for q in s["samples"]:
                w(f"  - 👍{q['likes']} \"{q['text']}\" ← {q['title']}")
        w("")
    X = E["timestamps"]
    w("## 7. 시간 표시 댓글 (어느 대목을 짚는가)")
    w(f"한 순간을 짚은 댓글 {X['moment_comments']}개(영상 {X['videos']}) · 요약·목차형 {X['summary_comments']}개. 영상 길이 10등분 위치: {X['deciles']} · 시각별: " + " · ".join(f"{k} {v}" for k, v in X["by_time"]))
    for q in X["top_liked"]:
        w(f"- 👍{q['likes']} \"{q['text']}\" ← {q['title']}")
    w("")
    G = E["ages"]
    w("## 8. 나이를 밝힌 댓글 (참고 — 시청자 나이 분포가 아님)")
    w(f"{G['n']}개: " + " · ".join(f"{k} {v}({v / G['n']:.0%})" for k, v in G["dist"]) + f". 영상 6개가 {G['top6_share']:.0%}를 냄 → 은퇴·배당 생활 영상에서 나이를 적는 사람이 많을 뿐.")
    for t in G["top6"]:
        w(f"- {t['n']}개 ← {t['title']}")
    w("")
    return "\n".join(o) + "\n"


# ------------------------------------------------------------------ 검사
def selftest():
    cfg = {"exclude": {"OFF": {"x1": "off"}, "EVENT": {"e1": "ev"}, "_NEWS_CHANNEL": re.compile("KBS"), "_POLITICS_TITLE": re.compile("대통령")}}
    assert group_of({"id": "x1", "channel": "a", "title": "b", "theme": "2. 장기"}, cfg) == "X_off"
    assert group_of({"id": "e1", "channel": "a", "title": "b", "theme": "2. 장기"}, cfg) == "E_event"
    assert group_of({"id": "n", "channel": "KBS News", "title": "b", "theme": "5. 국내"}, cfg) == "N_news"
    assert group_of({"id": "n", "channel": "a", "title": "주식", "theme": "8. 투자 심리"}, cfg) == "P_psy"
    assert group_of({"id": "n", "channel": "a", "title": "주식", "theme": "10. 노후"}, cfg) == "L_long"
    d = dedupe([{"id": "a", "likes": 1}, {"id": "a", "likes": 5}, {"id": "b", "likes": 0}, {"likes": 3}])
    assert len(d) == 2 and next(x for x in d if x["id"] == "a")["likes"] == 5
    assert bucket(500, [1000, 5000]) == 0 and bucket(1000, [1000, 5000]) == 1 and bucket(9999, [1000, 5000]) == 2
    # 배수: 구간 0 성공률 10%, 구간 1 성공률 50% — 특징 영상 4개(구간 0 둘·구간 1 둘) 가운데 3개 성공 → 기대 1.2 → 2.5
    A = [{"b": 0, "ok": i < 10} for i in range(100)] + [{"b": 1, "ok": i < 50} for i in range(100)]
    rt = rates(A)
    assert abs(rt[0] - 0.1) < 1e-9 and abs(rt[1] - 0.5) < 1e-9
    L = lift([{"b": 0, "ok": True}, {"b": 0, "ok": False}, {"b": 1, "ok": True}, {"b": 1, "ok": True}], rt)
    assert L["obs"] == 3 and abs(L["exp"] - 1.2) < 1e-9 and L["lift"] == 2.5, L
    assert lift([], rt)["lift"] is None
    assert TS.findall("3:45 여기 1:02:03 끝") == [("3", "45", ""), ("1", "02", "03")]
    assert AGE.search("저는 52살입니다").group(2) == "52" and AGE.search("40대 직장인").group(1) == "4" and not AGE.search("2026년 150만 원")
    assert flat("a\n b  c", 3) == "a b…"
    print("[SELFTEST] ok — group·dedupe·bucket·lift·timestamp·age·flat")
    return 0


def main(argv):
    ap = argparse.ArgumentParser(description="판단용 페르소나 근거를 원자료에서 다시 뽑음")
    ap.add_argument("topic", nargs="?", default="stock")
    ap.add_argument("--check", action="store_true", help="계산만 하고 파일을 쓰지 않음")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args(argv)
    logging.basicConfig(level=getattr(logging, a.log_level), format="%(message)s", stream=sys.stdout)
    if a.selftest:
        return selftest()
    try:
        E = build(a.topic)
    except FileNotFoundError as e:
        log("ERROR", logging.ERROR, stage="load", missing=str(e), next="주제 폴더의 result/outliers 와 persona_judge.toml 을 확인")
        return 1
    if a.check:
        log("CHECK", wrote=False)
        return 0
    base = ROOT / a.topic / "result" / "outliers"
    (base / "persona_evidence.md").write_text(render(E), "utf-8")
    (base / "persona_evidence.json").write_text(json.dumps(E, ensure_ascii=False, indent=1) + "\n", "utf-8")
    log("WRITE", md=str((base / "persona_evidence.md").relative_to(ROOT)), json=str((base / "persona_evidence.json").relative_to(ROOT)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
