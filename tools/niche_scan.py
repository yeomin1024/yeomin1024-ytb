#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-16 — 신규: 새 채널 분야 비교 (사용자 지시 2026-10-16: "이외에도 내가 어떤 채널을 만들어야 조회수 높은 영상 만들고
#          구독자 많이 모을 수 있을지 전체적으로 탐색해봐 저장소에 디렉토리 new로 만들어서 새로운 주제 탐색하기 위한 세팅해서 탐색해봐").
#          ① sync   — <주제>/niches.toml(분야·검색어·제목 낱말·제작 판단) → keywords.txt('돌아가며' 순서) + tag_rules.toml(TAG_THEMES)
#          ② report — 웹 화면·cloud_run 탐색 결과(result/web/explore.json)와 탐색 캐시(result/outliers/.cache — 채널 개설일·검색 결과 수)만
#                     읽어(할당량 0, 인터넷 안 씀) 분야마다: 수요(하루 조회수) · 작은 채널이 조회수 상위에 끼는 정도(성공 비율 —
#                     CLAUDE.md 성공 기준 그대로, <주제>/analysis_rules.toml [success]) · 빨리 큰 새 채널 · 검색 결과 수(공급 추정) →
#                     result/niche/niche_scan.md (+ niche_scan.csv · niche_videos.csv · niche_channels.csv)
#          분석 로직(탐색·추천·성공 사례 분석)은 바꾸지 않음 — 이미 받은 탐색 자료를 분야별로 다시 셀 뿐.
# ※ 연구·교육용 분석 도구. 투자·의료·법률 권유가 아니다.
"""새 채널 분야 비교 (할당량 0).

  python3 tools/niche_scan.py new sync      # niches.toml → keywords.txt + tag_rules.toml
  python3 tools/niche_scan.py new report    # 탐색 결과 → new/result/niche/niche_scan.md · .csv

로그: [STAGE] [시각] key=value (web_ui·cloud_run 과 같은 꼴). --log-level DEBUG 면 영상마다 거른 까닭도.
"""
import argparse
import csv
import json
import logging
import re
import statistics
import sys
import tomllib
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

VERSION = "v1.0"
ROOT = Path(__file__).resolve().parent.parent
KST = timezone(timedelta(hours=9))
LOG = logging.getLogger("niche")
MIN_SAMPLE = 30                    # 분야 표본(영상)이 이보다 적으면 '표본 적음' — 점수는 내지만 표시
MIN_SMALL = 10                     # 작은 채널 영상이 이보다 적으면 '작은 채널 하루 조회수'를 점수에 쓰지 않음 (2026-10-16: 여행 표본 79개 중 작은 채널 6개 → 중앙값 23,817)
BIG_SUBS = 1_000_000               # 큰 채널 (진입 장벽 참고)
NEW_10K = 10_000                   # '2년 안에 구독자 1만' — 빨리 큰 새 채널
TOP_EXAMPLES = 5                   # 분야마다 성공 영상·빨리 큰 채널 예 몇 개
TOP_FAST = 30                      # 분야를 넘나드는 빨리 큰 새 채널 표
DEFAULT_SUCCESS = {"MAX_AGE_DAYS": 180, "MAX_SUBS": 50000, "MIN_RATIO": 3.0, "MIN_VIEWS": 10000, "MIN_MINUTES": 4.0}
DEFAULT_COMPARE = {"MIN_AGE_DAYS": 7, "PER_CHANNEL": 5}
DEFAULT_GROWTH = {"NEW_CHANNEL_MONTHS": 24, "MIN_SUBS": 1000, "MAX_SUBS": 200000, "BRAND_HINT": []}
DEFAULT_EXCLUDE = {"OFF_TOPIC": [], "AD_SUSPECT_MIN_VIEWS": 50000, "AD_SUSPECT_MAX_LIKE_RATE": 0.0025, "AD_SUSPECT_MAX_COMMENT_RATE": 0.00005}
SCORE_PARTS = (("success_rate", "작은 채널 성공 비율"), ("small_vpd_median", "작은 채널 영상 하루 조회수 중앙값"),
               ("new10k_share", "2년 안에 1만 모은 채널 비율"))


def log(stage, level=logging.INFO, **kv):
    LOG.log(level, "[%s] [%s] %s", stage, datetime.now().isoformat(timespec="seconds"),
            " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) and ' ' in v else v}" for k, v in kv.items()))


def _toml(p):
    return tomllib.loads(Path(p).read_text("utf-8")) if Path(p).is_file() else {}


def _read_json(p, default):
    try:
        return json.loads(Path(p).read_text("utf-8"))
    except (OSError, ValueError):
        return default


def _norm(q):
    return re.sub(r"\s+", "", str(q)).lower()


# ---------------------------------------------------------------- 분야 정의
def load_niches(root, topic):
    """<주제>/niches.toml → [{name, group, keywords, words, make, make_why}] — 검사: 이름·검색어 겹침, 빈 검색어."""
    p = root / topic / "niches.toml"
    if not p.is_file():
        raise SystemExit(f"[START] ❌ {p} 없음 — 분야 정의 파일을 먼저 만드세요 (예: new/niches.toml)")
    niches = []
    seen_kw, seen_name = {}, set()
    for n in _toml(p).get("niche") or []:
        name = str(n.get("name") or "").strip()
        kws = [str(k).strip() for k in n.get("keywords") or [] if str(k).strip()]
        if not name or not kws:
            raise SystemExit(f"[START] ❌ {p}: 이름이나 검색어가 빈 분야 — {n}")
        if name in seen_name:
            raise SystemExit(f"[START] ❌ {p}: 분야 이름이 겹침 — {name}")
        seen_name.add(name)
        for k in kws:
            if _norm(k) in seen_kw:
                raise SystemExit(f"[START] ❌ {p}: 검색어 '{k}' 가 '{seen_kw[_norm(k)]}' 와 '{name}' 두 분야에 있음 — 한 분야에만")
            seen_kw[_norm(k)] = name
        niches.append({"name": name, "group": str(n.get("group") or "A"), "keywords": kws,
                       "words": [str(w) for w in n.get("words") or [] if str(w).strip()],
                       "make": str(n.get("make") or "-"), "make_why": str(n.get("make_why") or "")})
    log("NICHES", topic=topic, niches=len(niches), keywords=len(seen_kw), file=p.relative_to(root).as_posix())
    return niches


def round_robin(niches):
    """검색 순서: 1번째 검색어를 모든 분야(파일 순서)에서 먼저, 그다음 2번째 … — 할당량·검색 횟수 한도가 중간에 끝나도 모든 분야가 1개씩은."""
    out, depth = [], max(len(n["keywords"]) for n in niches)
    for i in range(depth):
        out += [(n["name"], n["keywords"][i]) for n in niches if i < len(n["keywords"])]
    return out


def cmd_sync(root, topic):
    niches = load_niches(root, topic)
    order = round_robin(niches)
    now = datetime.now(KST).isoformat(timespec="minutes")
    lines = [f"# 검색어 목록 — 새 주제 탐색 ({topic}) · 만든 도구: tools/niche_scan.py {VERSION} sync · {now}",
             f"# ⚠️ 손으로 고치지 말고 {topic}/niches.toml 을 고친 뒤 python3 tools/niche_scan.py {topic} sync",
             "# 순서 = '돌아가며': 모든 분야의 1번째 검색어 → 2번째 … (할당량·하루 검색 횟수 한도가 중간에 끝나도 모든 분야가 1개씩은 먼저)",
             f"# 검색어 {len(order)}개 × (4~20분·20분 넘음 검색 2번 = 200단위) ≈ {len(order) * 200:,}단위 + 영상·채널 정보", ""]
    rnd = -1
    depth_of = {}
    for name, kw in order:
        d = next(i for i, k in enumerate(next(n for n in niches if n["name"] == name)["keywords"]) if k == kw)
        depth_of[kw] = d
        if d != rnd:
            rnd = d
            lines.append(f"# ── {d + 1}번째 검색어 ──")
        lines.append(f"{kw}")
    kw_p = root / topic / "keywords.txt"
    kw_p.write_text("\n".join(lines) + "\n", "utf-8")
    themes = "\n".join(f'"{n["name"]}" = [{", ".join(json.dumps(w, ensure_ascii=False) for w in n["words"])}]' for n in niches)
    tag = f'''# =====================================================================================================
# 주제 묶음 — 새 주제 탐색 ({topic}) · ⚠️ 만든 파일: tools/niche_scan.py {VERSION} sync · {now}
# 손으로 고치지 말고 {topic}/niches.toml 의 words 를 고친 뒤 python3 tools/niche_scan.py {topic} sync
# 읽는 코드: tools/success_analysis.py (analysis.md '주제별 성공 비율' — 제목에서 가장 긴 낱말이 맞는 분야, 없으면 태그로, 그래도 없으면 '기타')
# 이 폴더는 태그로 검색어를 고르지 않는다 (tools/tag_keywords.py 안 씀 — 분야를 넘나드는 비교라 분야마다 넓은 검색어로 찔러 봄, niches.toml 머리말)
# =====================================================================================================

TAG_OTHER = "기타"

[TAG_THEMES]
{themes}
'''
    (root / topic / "tag_rules.toml").write_text(tag, "utf-8")
    tomllib.loads(tag)                                                     # 쓴 파일이 읽히는지 바로 확인
    log("SYNC", topic=topic, keywords=len(order), first_round=sum(1 for v in depth_of.values() if v == 0),
        files=f"{topic}/keywords.txt,{topic}/tag_rules.toml", est_units=len(order) * 200)
    return {"keywords": len(order), "niches": len(niches)}


# ---------------------------------------------------------------- 규칙
def load_rules(root, topic):
    d = _toml(root / topic / "analysis_rules.toml")
    S = {**DEFAULT_SUCCESS, **{k: v for k, v in (d.get("success") or {}).items() if k in DEFAULT_SUCCESS}}
    C = {**DEFAULT_COMPARE, **{k: v for k, v in (d.get("compare") or {}).items() if k in DEFAULT_COMPARE}}
    G = {**DEFAULT_GROWTH, **{k: v for k, v in (d.get("growth") or {}).items() if k in DEFAULT_GROWTH}}
    E = {**DEFAULT_EXCLUDE, **{k: v for k, v in (d.get("exclude") or {}).items() if k in DEFAULT_EXCLUDE}}
    log("RULES", success=json.dumps(S, ensure_ascii=False), min_age_days=C["MIN_AGE_DAYS"], per_channel=C["PER_CHANNEL"], growth=json.dumps(G, ensure_ascii=False),
        off_topic=len(E["OFF_TOPIC"]), file=f"{topic}/analysis_rules.toml" if d else "(없음 — 기본값)")
    return S, C, G, E


# ---------------------------------------------------------------- 영상 거르기·성공 판정
def drop_reason(r, S, C, E):
    """분야 표본에서 뺄 까닭 (없으면 None). 성공 사례 분석(success_analysis)의 비교 집단과 같은 기준 — 나이·길이·광고 의심·뺀 낱말."""
    age, views = r.get("age_days"), int(r.get("views") or 0)
    if age is None:
        return "올린 날 모름"
    if age < C["MIN_AGE_DAYS"]:
        return f"올린 지 {C['MIN_AGE_DAYS']}일 안 됨"
    if float(r.get("minutes") or 0) < S["MIN_MINUTES"]:
        return "짧음"
    if r.get("flag"):
        return str(r["flag"])                                            # 주소로 넣은 라이브·외국 영상 (탐색은 빼지 않고 표시만)
    title = str(r.get("title") or "")
    if any(w in title for w in E["OFF_TOPIC"]):
        return "뺀 낱말"
    likes, comments = int(r.get("likes") or 0), int(r.get("comments") or 0)
    if (views >= E["AD_SUSPECT_MIN_VIEWS"] and likes / views < E["AD_SUSPECT_MAX_LIKE_RATE"]
            and comments / views < E["AD_SUSPECT_MAX_COMMENT_RATE"]):
        return "광고 의심"
    return None


def is_success(r, S):
    """CLAUDE.md 성공 기준 (analysis_rules.toml [success]): 180일 안·구독자 5만 이하·조회수 1만 이상·조회수 ≥ 구독자 × 3 (100 미만은 100)·4분 이상."""
    subs = r.get("subs")
    if subs is None or r.get("age_days") is None:
        return False
    return (subs <= S["MAX_SUBS"] and r["age_days"] <= S["MAX_AGE_DAYS"] and int(r.get("views") or 0) >= S["MIN_VIEWS"]
            and int(r.get("views") or 0) / max(subs, 100) >= S["MIN_RATIO"] and float(r.get("minutes") or 0) >= S["MIN_MINUTES"])


def brand_hint(name, hints):
    """채널 이름에 기관·방송사·브랜드 낱말 → 그 낱말 (success_analysis '[growth] BRAND_HINT' 와 같은 뜻 — 빼지 않고 표시만). 영문은 낱말 단위."""
    name = str(name or "")
    for h in hints:
        if re.fullmatch(r"[A-Za-z]+", h):
            if re.search(rf"(?<![A-Za-z]){re.escape(h)}(?![A-Za-z])", name, re.I):
                return h
        elif h in name:
            return h
    return None


def months_since(created, now):
    try:
        c = datetime.fromisoformat(str(created).replace("Z", "+00:00"))
    except ValueError:
        return None
    c = c if c.tzinfo else c.replace(tzinfo=timezone.utc)
    return max((now - c).days / 30.44, 0.0)


def _median(xs):
    xs = [x for x in xs if x is not None]
    return round(statistics.median(xs), 1) if xs else None


def _share(a, b):
    return round(a / b, 3) if b else None


# ---------------------------------------------------------------- 분야별로 세기
def cap_per_channel(vids, per_channel, dropped):
    """한 채널은 최근 영상 per_channel 개까지 (analysis_rules.toml [compare] PER_CHANNEL — success_analysis 비교 집단과 같은 규칙).
    2026-10-16 첫 탐색: 퀴즈 분야 176개 중 51개가 한 채널, 생활정보 40개가 한 방송사 채널 → 한 채널이 비율을 덮음. 성공 여부와 무관하게 '최근' 순으로 고름."""
    by_ch = defaultdict(list)
    for v in vids:
        by_ch[v.get("channel_id") or v.get("channel")].append(v)
    keep = []
    for vs in by_ch.values():
        vs = sorted(vs, key=lambda v: (v.get("age_days") if v.get("age_days") is not None else 10 ** 6, v.get("id")))
        keep += vs[:per_channel]
        if len(vs) > per_channel:
            dropped[f"채널당 {per_channel}개 넘음"] += len(vs) - per_channel
    return sorted(keep, key=lambda v: v.get("id"))


def niche_of_queries(niches):
    return {_norm(k): n["name"] for n in niches for k in n["keywords"]}


def collect(rows, niches, channels, S, C, G, E, now):
    """explore.json rows → 분야별 표본·숫자. 검색으로 찾은 영상만 (채널·주소로 넣은 영상은 분야를 모름).
    한 영상이 두 분야 검색어에 모두 걸리면 두 분야에 다 셈 (한계에 적음)."""
    q2n = niche_of_queries(niches)
    by = {n["name"]: {"videos": {}, "dropped": Counter(), "queries": Counter()} for n in niches}
    unknown_q, dup_ids = Counter(), 0
    seen = set()
    for r in rows:
        if r.get("id") in seen:
            dup_ids += 1
            continue
        seen.add(r.get("id"))
        qs = [s.split(":", 1)[1] for s in r.get("sources") or [] if str(s).startswith("검색:")]
        names = []
        for q in qs:
            nm = q2n.get(_norm(q))
            if nm is None:
                unknown_q[q] += 1
            elif nm not in names:
                names.append(nm)
        if not names:
            continue
        why = drop_reason(r, S, C, E)
        for nm in names:
            if why:
                by[nm]["dropped"][why] += 1
                LOG.debug("[DROP] niche=%s id=%s why=%s", nm, r.get("id"), why)
                continue
            by[nm]["videos"][r["id"]] = r
    if dup_ids:
        log("VALIDATE", logging.WARNING, note="탐색 목록에 같은 영상 ID 가 두 번 — 처음 것만 셈", duplicates=dup_ids)
    if unknown_q:
        log("VALIDATE", logging.WARNING, note="niches.toml 에 없는 검색어로 찾은 영상 — 분야를 몰라 뺌 (검색어를 바꾼 뒤 sync 를 안 했나?)",
            queries=",".join(f"{q}:{n}" for q, n in unknown_q.most_common(10)))
    out = []
    for n in niches:
        b = by[n["name"]]
        vids = cap_per_channel(list(b["videos"].values()), C["PER_CHANNEL"], b["dropped"])
        b["videos"] = {v["id"]: v for v in vids}
        q_succ = Counter()
        for v in vids:                                                     # 검색어별 표본·성공 (채널당 상한 뒤) — 분야 안에서 검색어끼리 결과가 맞는지
            for q in dict.fromkeys(s.split(":", 1)[1] for s in v.get("sources") or [] if str(s).startswith("검색:")):
                if q2n.get(_norm(q)) == n["name"]:
                    b["queries"][q] += 1
                    q_succ[q] += is_success(v, S)
        known = [v for v in vids if v.get("subs") is not None]
        small = [v for v in known if v["subs"] <= S["MAX_SUBS"]]
        succ = [v for v in vids if is_success(v, S)]
        chans = {}
        for v in vids:
            chans.setdefault(v.get("channel_id") or v.get("channel"), []).append(v)
        new_rows = []
        for cid, vs in chans.items():
            ch = channels.get(cid) or {}
            m = months_since(ch.get("created"), now) if ch.get("created") else None
            subs = ch.get("subs") if ch.get("subs") is not None else vs[0].get("subs")
            if m is None or subs is None:
                continue
            if m <= G["NEW_CHANNEL_MONTHS"] and G["MIN_SUBS"] <= subs <= G["MAX_SUBS"]:
                best = max(vs, key=lambda v: int(v.get("views") or 0))
                cname = ch.get("title") or best.get("channel")
                new_rows.append({"channel": cname, "channel_id": cid, "subs": subs, "brand": brand_hint(cname, G["BRAND_HINT"]),
                                 "months": round(m, 1), "subs_per_month": round(subs / max(m, 1.0)),
                                 "channel_videos": ch.get("videos"), "best_title": best.get("title"), "best_views": int(best.get("views") or 0),
                                 "best_id": best.get("id"), "niche": n["name"]})
        no_created = sum(1 for cid in chans if not (channels.get(cid) or {}).get("created"))
        new10k = [x for x in new_rows if x["subs"] >= NEW_10K]
        succ_ch = {v.get("channel_id") for v in succ}
        res = {
            "niche": n["name"], "group": n["group"], "make": n["make"], "make_why": n["make_why"],
            "keywords": n["keywords"], "query_hits": dict(b["queries"]), "query_success": dict(q_succ),
            "videos": len(vids), "channels": len(chans), "dropped": dict(b["dropped"]),
            "views_median": _median([int(v.get("views") or 0) for v in vids]),
            "vpd_median": _median([float(v.get("views_per_day") or 0) for v in vids]),
            "subs_known": len(known), "small_share": _share(len(small), len(known)),
            "big_share": _share(sum(1 for v in known if v["subs"] >= BIG_SUBS), len(known)),
            "small_n": len(small), "small_vpd_median": _median([float(v.get("views_per_day") or 0) for v in small]),
            "small_ratio_median": _median([v.get("ratio") for v in small]),
            "success": len(succ), "success_channels": len(succ_ch), "success_rate": _share(len(succ), len(vids)),
            "success_channel_share": _share(len(succ_ch), len(chans)),
            "success_minutes_median": _median([float(v.get("minutes") or 0) for v in succ]),
            "success_subs_median": _median([v.get("subs") for v in succ]),
            "minutes_median": _median([float(v.get("minutes") or 0) for v in vids]),
            "new_channels": len(new_rows), "new10k": len(new10k), "new10k_share": _share(len(new10k), len(chans)),
            "new_spm_median": _median([x["subs_per_month"] for x in new_rows]),
            "no_created": no_created, "small_sample": len(vids) < MIN_SAMPLE,
            "examples": sorted(succ, key=lambda v: -(v.get("ratio") or 0))[:TOP_EXAMPLES],
            "fast": sorted(new_rows, key=lambda x: -x["subs_per_month"]),
            "_videos": vids,                                             # niche_videos.csv — 거르기·채널당 상한 뒤 표본 그대로
        }
        out.append(res)
        log("NICHE", niche=n["name"], videos=res["videos"], channels=res["channels"], success=res["success"],
            success_rate=res["success_rate"], small_vpd_median=res["small_vpd_median"], new10k=res["new10k"],
            dropped=",".join(f"{k}:{v}" for k, v in b["dropped"].items()) or "-")
    return out


def score(res):
    """참고 점수 = 세 숫자(SCORE_PARTS)의 분야 안 백분위(0~1) 평균 × 100. 값이 없는 숫자는 빼고 평균. 규칙이 아니라 줄 세우기."""
    def val(r, key):
        if key == "small_vpd_median" and (r.get("small_n") or 0) < MIN_SMALL:
            return None                                                        # 작은 채널 영상이 적으면 중앙값이 우연에 흔들림
        return r[key]
    for key, _ in SCORE_PARTS:
        vals = sorted(val(r, key) for r in res if val(r, key) is not None)
        for r in res:
            v = val(r, key)
            if v is None or len(vals) < 2:
                r[f"pct_{key}"] = None
                continue
            lo = sum(1 for x in vals if x < v)
            eq = sum(1 for x in vals if x == v)
            r[f"pct_{key}"] = round((lo + (eq - 1) / 2) / (len(vals) - 1), 3)      # 같은 값은 가운데 순위
    for r in res:
        ps = [r[f"pct_{k}"] for k, _ in SCORE_PARTS if r[f"pct_{k}"] is not None]
        r["score"] = round(100 * sum(ps) / len(ps), 1) if ps else None
    return sorted(res, key=lambda r: (r["score"] is None, -(r["score"] or 0)))


# ---------------------------------------------------------------- 검색 상태
def search_status(cache_dir, niches, explore):
    """검색어마다: 받은 검색(길이별 결과 수·유튜브 결과 수 추정 totalResults) · 못 한 검색 (explore.json pending)."""
    q2n = niche_of_queries(niches)
    st = {}
    for f in sorted(Path(cache_dir).glob("search_*.json")) if Path(cache_dir).is_dir() else []:
        d = _read_json(f, {})
        q = d.get("q")
        if not q or _norm(q) not in q2n or d.get("dur") not in ("medium", "long"):
            continue
        s = st.setdefault(_norm(q), {"q": q, "niche": q2n[_norm(q)], "dur": {}, "total": {}, "fetched": None})
        s["dur"][d["dur"]] = len(d.get("ids") or [])
        s["total"][d["dur"]] = d.get("total")
        s["fetched"] = max(filter(None, [s["fetched"], d.get("fetched")]), default=None)
    pend = Counter(re.sub(r"\s*\((medium|long)\)$", "", p) for p in explore.get("pending") or [])
    for n in niches:
        for k in n["keywords"]:
            s = st.setdefault(_norm(k), {"q": k, "niche": n["name"], "dur": {}, "total": {}, "fetched": None})
            s["pending"] = pend.get(k, 0)
    return st


# ---------------------------------------------------------------- 쓰기
def _fmt(x, pct=False):
    if x is None:
        return "-"
    if pct:
        return f"{x * 100:.0f}%"
    if isinstance(x, float) and not x.is_integer():
        return f"{x:,.1f}"
    return f"{int(x):,}"


def _qs(succ, n):
    return "-" if not n else f"{succ or 0} ({(succ or 0) / n * 100:.0f}%)"


def _pct100(x):
    return "-" if x is None else f"{x * 100:.0f}"


def _md(s):
    return str(s or "").replace("|", "/").replace("\n", " ")


def write_report(root, topic, res, st, explore, S, C, G, now, out_dir):
    out_dir.mkdir(parents=True, exist_ok=True)
    total_v = sum(r["videos"] for r in res)
    pending = sum(s.get("pending", 0) for s in st.values())
    searched = sum(len(s["dur"]) for s in st.values())
    L = [f"# 새 채널 분야 비교 — {topic} (숫자·원문만)", "",
         f"만든 때: {now.astimezone(KST).isoformat(timespec='minutes')} · 도구: `tools/niche_scan.py {VERSION} report` (할당량 0 — 탐색 목록·캐시만 읽음) · "
         f"탐색: {explore.get('generated') or '-'} · 최근 {explore.get('weeks') or '-'}주 · 받은 검색 {searched}번 · 못 한 검색 {pending}번",
         "", "※ 연구·교육용. 해석·추천은 이 파일에 없다 (추천은 `new/README.md`·`new/channel_ideas.md` — 판단을 따로 적음).", "",
         "## 0. 읽는 법·한계 (먼저)", "",
         "- **표본** = 분야 검색어로 찾은 롱폼(4~20분·20분 넘음 검색, 각각 **최근 기간 조회수 순 상위 50개**, 한국어·라이브 아님) 중 "
         f"올린 지 {C['MIN_AGE_DAYS']}일 넘고 {S['MIN_MINUTES']:g}분 이상·광고 의심 아님, **한 채널은 최근 {C['PER_CHANNEL']}개까지** (`[compare] PER_CHANNEL` — "
         "한 채널이 비율을 덮지 않게). → '그 분야에서 **가장 많이 본 영상들**'이다 (분야 전체가 아님).",
         f"- **성공** = CLAUDE.md 성공 기준 그대로 (`{topic}/analysis_rules.toml` [success]): {S['MAX_AGE_DAYS']}일 안 · 구독자 {S['MAX_SUBS']:,} 이하 · "
         f"조회수 {S['MIN_VIEWS']:,} 이상 · 조회수 ≥ 구독자 × {S['MIN_RATIO']:g}. **성공 비율** = 성공 ÷ 표본 → '작은 채널이 그 분야 조회수 상위에 끼는 정도'. "
         "**성공 채널 몫** = 성공 영상이 하나라도 있는 채널 ÷ 표본 채널.",
         "- **하루 조회수** = 조회수 ÷ 올린 뒤 날 수. **작은 채널 하루 조회수** = 구독자 5만 이하 채널 영상만 — 작은 채널이 그 분야에서 받는 수요.",
         f"- **새 채널** = 개설 {G['NEW_CHANNEL_MONTHS']}개월 안 · 구독자 {G['MIN_SUBS']:,}~{G['MAX_SUBS']:,} (`[growth]`). **2년 안 1만** = 그중 구독자 {NEW_10K:,} 이상 — "
         "비율은 그 분야 표본 채널 수로 나눔. 월 증가 = 구독자 ÷ 개설 뒤 달 수 (평균 — 최근 속도 아님).",
         "- **검색 결과 수** = YouTube 가 주는 totalResults (추정치 — 공급의 대략적인 크기, 정확하지 않음).",
         "- **참고 점수** = 성공 비율 · 작은 채널 하루 조회수 · 2년 안 1만 비율의 분야 안 백분위 평균 × 100. 줄 세우기용이지 규칙이 아니다. "
         "광고 단가(RPM)·제작 비용·경쟁 채널의 질은 들어 있지 않다.",
         "- **만들기(판단)** 칸은 측정이 아니라 Claude 판단 (`niches.toml` make — 지금 제작 방식: 얼굴 없음·AI 내레이션 하나·HTML 애니메이션).",
         "- 한 영상이 두 분야 검색어에 걸리면 두 분야에 다 셈. A 분야는 검색어 2개(표본 최대 200), B·기준은 1개(최대 100) — 그래서 개수 대신 비율로 견줌.",
         f"- 표본 {MIN_SAMPLE}개 미만 분야는 ⚠️ (차이가 우연일 수 있음). 검색어 하나가 분야를 다 대표하지 못함 — 좋은 분야는 그 분야 폴더를 따로 만들어 태그로 다시 본다.",
         "- 한국어 영상만 (`INCLUDE_FOREIGN = false`). 구독자 수는 지금 값(올린 때 값이 아님).", ""]
    L += ["## 1. 분야 비교 (참고 점수 순)", "",
          "| # | 분야 | 갈래 | 만들기(판단) | 표본 | 채널 | 하루 조회수 중앙값 | 작은 채널 몫 | 큰 채널(100만↑) 몫 | 작은 채널 하루 조회수 (영상 수) | 작은 채널 배수 중앙값 | 성공 (채널) | **성공 비율** | 성공 채널 몫 | 성공 영상 길이(분) | 새 채널 | 2년 안 1만 (비율) | 새 채널 월 증가 중앙값 | 참고 점수 |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for i, r in enumerate(res, 1):
        L.append("| " + " | ".join([
            str(i), _md(r["niche"]) + (" ⚠️" if r["small_sample"] else ""), r["group"], r["make"], _fmt(r["videos"]), _fmt(r["channels"]),
            _fmt(r["vpd_median"]), _fmt(r["small_share"], True), _fmt(r["big_share"], True),
            f"{_fmt(r['small_vpd_median'])} ({r['small_n']}{' ⚠️' if r['small_n'] < MIN_SMALL else ''})",
            _fmt(r["small_ratio_median"]), f"{r['success']} ({r['success_channels']})", f"**{_fmt(r['success_rate'], True)}**",
            _fmt(r["success_channel_share"], True), _fmt(r["success_minutes_median"]), _fmt(r["new_channels"]), f"{r['new10k']} ({_fmt(r['new10k_share'], True)})", _fmt(r["new_spm_median"]),
            _fmt(r["score"])]) + " |")
    L += ["", "(갈래: A = 지금 제작 방식으로 만들 수 있음 · B = 촬영 필요(비교용) · 기준 = 지금 채널. 점수를 나눠 본 값은 아래 2번 표. "
          f"작은 채널 영상이 {MIN_SMALL}개 미만이면 ⚠️ — 그 분야 점수는 작은 채널 하루 조회수를 빼고 나머지 두 숫자로)", ""]
    L += ["## 2. 점수 나눠 보기 · 뺀 영상", "", "백분위 0~100 (분야 안 순위 — 100 이 가장 높음, '-' = 점수에 안 씀).", "", "| 분야 | 성공 비율 백분위 | 작은 채널 하루 조회수 백분위 | 2년 안 1만 비율 백분위 | 뺀 영상 (까닭:수) | 개설일 모르는 채널 |",
          "|---|---|---|---|---|---|"]
    for r in res:
        L.append(f"| {_md(r['niche'])} | {_pct100(r['pct_success_rate'])} | {_pct100(r['pct_small_vpd_median'])} | {_pct100(r['pct_new10k_share'])} | "
                 f"{', '.join(f'{k}:{v}' for k, v in r['dropped'].items()) or '-'} | {r['no_created']} |")
    L += ["", "## 3. 검색어별 (분야 안에서 검색어끼리 결과가 맞는지)", "",
          "| 분야 | 검색어 | 4~20분 결과 | 20분 넘음 결과 | 표본에 든 영상 | 성공 (비율) | 유튜브 결과 수(추정, 4~20분 / 20분 넘음) | 못 한 검색 | 받은 때 |",
          "|---|---|---|---|---|---|---|---|---|"]
    hits = {r["niche"]: r["query_hits"] for r in res}
    qsucc = {r["niche"]: r["query_success"] for r in res}
    for s in sorted(st.values(), key=lambda s: (s["niche"], s["q"])):
        tot = s["total"]
        L.append(f"| {_md(s['niche'])} | {_md(s['q'])} | {_fmt(s['dur'].get('medium'))} | {_fmt(s['dur'].get('long'))} | "
                 f"{_fmt(hits.get(s['niche'], {}).get(s['q']))} | {_qs(qsucc.get(s['niche'], {}).get(s['q']), hits.get(s['niche'], {}).get(s['q']))} | "
                 f"{_fmt(tot.get('medium'))} / {_fmt(tot.get('long'))} | {s.get('pending') or 0} | "
                 f"{str(s.get('fetched') or '-')[:16]} |")
    L += ["", f"## 4. 분야를 넘나드는 빨리 큰 새 채널 (개설 {G['NEW_CHANNEL_MONTHS']}개월 안 · 월 구독자 증가 순 {TOP_FAST}곳)", "",
          "이름만 보고 연예인·방송사·브랜드 채널을 다 가려내지 못함 (`[growth] BRAND_HINT` 낱말만 표시) — 유명인 덕에 큰 채널이 섞여 있다.", "",
          "| # | 채널 | 분야 | 구독자 | 개설 뒤 달 | 월 증가 | 채널 영상 수 | 표본에서 가장 많이 본 영상 | 조회수 |", "|---|---|---|---|---|---|---|---|---|"]
    allfast = {}
    for r in res:
        for x in r["fast"]:
            a = allfast.setdefault(x["channel_id"], dict(x, niches=[]))
            a["niches"].append(r["niche"])
    for i, x in enumerate(sorted(allfast.values(), key=lambda x: -x["subs_per_month"])[:TOP_FAST], 1):
        L.append(f"| {i} | {_md(x['channel'])}{' (기관·브랜드? ' + x['brand'] + ')' if x.get('brand') else ''} | {_md(', '.join(x['niches']))} | {_fmt(x['subs'])} | {x['months']:.1f} | {_fmt(x['subs_per_month'])} | "
                 f"{_fmt(x['channel_videos'])} | [{_md(x['best_title'])[:60]}](https://youtu.be/{x['best_id']}) | {_fmt(x['best_views'])} |")
    L += ["", "## 5. 분야별 예 (성공 영상 배수 순 · 빨리 큰 새 채널)", ""]
    for r in res:
        L += [f"### {r['niche']} — 표본 {r['videos']} · 성공 {r['success']} ({_fmt(r['success_rate'], True)}) · 검색어 {', '.join(r['keywords'])}", ""]
        if r["examples"]:
            L += ["| 성공 영상 | 채널 | 구독자 | 조회수 | 배수 | 분 | 올린 지(일) |", "|---|---|---|---|---|---|---|"]
            for v in r["examples"]:
                L.append(f"| [{_md(v.get('title'))[:70]}](https://youtu.be/{v['id']}) | {_md(v.get('channel'))} | {_fmt(v.get('subs'))} | "
                         f"{_fmt(v.get('views'))} | {_fmt(v.get('ratio'))} | {_fmt(v.get('minutes'))} | {_fmt(v.get('age_days'))} |")
        else:
            L.append("성공 영상 없음.")
        if r["fast"]:
            L += ["", "빨리 큰 새 채널: " + " · ".join(f"{_md(x['channel'])} (구독자 {_fmt(x['subs'])}, {x['months']:.0f}개월, 월 {_fmt(x['subs_per_month'])})"
                                                for x in r["fast"][:TOP_EXAMPLES])]
        L.append("")
    md = out_dir / "niche_scan.md"
    md.write_text("\n".join(L) + "\n", "utf-8")
    cols = ["niche", "group", "make", "videos", "channels", "views_median", "vpd_median", "subs_known", "small_share", "big_share",
            "small_n", "small_vpd_median", "small_ratio_median", "success", "success_channels", "success_rate", "success_channel_share",
            "success_minutes_median", "success_subs_median", "minutes_median", "new_channels", "new10k", "new10k_share",
            "new_spm_median", "no_created", "small_sample", "pct_success_rate", "pct_small_vpd_median", "pct_new10k_share", "score"]
    with (out_dir / "niche_scan.csv").open("w", newline="", encoding="utf-8-sig") as f:
        wr = csv.writer(f)
        wr.writerow(cols + ["keywords", "dropped", "make_why"])
        for r in res:
            wr.writerow([r[c] for c in cols] + [" | ".join(r["keywords"]), json.dumps(r["dropped"], ensure_ascii=False), r["make_why"]])
    with (out_dir / "niche_videos.csv").open("w", newline="", encoding="utf-8-sig") as f:
        wr = csv.writer(f)
        wr.writerow(["niche", "id", "title", "channel", "channel_id", "subs", "views", "ratio", "views_per_day", "minutes", "age_days", "published",
                     "likes", "comments", "success", "queries"])
        for r in res:
            for v in sorted(r["_videos"], key=lambda v: -int(v.get("views") or 0)):
                wr.writerow([r["niche"], v["id"], v.get("title"), v.get("channel"), v.get("channel_id"), v.get("subs"), v.get("views"), v.get("ratio"),
                             v.get("views_per_day"), v.get("minutes"), v.get("age_days"), v.get("published"), v.get("likes"), v.get("comments"),
                             is_success(v, S), v.get("queries")])
    with (out_dir / "niche_channels.csv").open("w", newline="", encoding="utf-8-sig") as f:
        wr = csv.writer(f)
        wr.writerow(["channel", "channel_id", "niches", "subs", "months", "subs_per_month", "channel_videos", "brand_hint", "best_title", "best_views", "best_id"])
        for x in sorted(allfast.values(), key=lambda x: -x["subs_per_month"]):
            wr.writerow([x["channel"], x["channel_id"], " | ".join(x["niches"]), x["subs"], x["months"], x["subs_per_month"], x["channel_videos"],
                         x.get("brand") or "", x["best_title"], x["best_views"], x["best_id"]])
    log("WRITE", file=md.relative_to(root).as_posix(), niches=len(res), videos=total_v, fast_channels=len(allfast),
        csv="niche_scan.csv,niche_videos.csv,niche_channels.csv")
    return md


def cmd_report(root, topic, now=None):
    now = now or datetime.now(timezone.utc)
    niches = load_niches(root, topic)
    S, C, G, E = load_rules(root, topic)
    ex_p = root / topic / "result" / "web" / "explore.json"
    explore = _read_json(ex_p, {})
    rows = explore.get("rows") or []
    if not rows:
        raise SystemExit(f"[LOAD] ❌ 탐색 목록이 없음 ({ex_p.relative_to(root)}) — 먼저 python3 tools/cloud_run.py {topic} explore --weeks 26")
    cache = root / topic / "result" / "outliers" / ".cache"
    channels = {k: v for k, v in _read_json(cache / "channels.json", {}).items() if isinstance(v, dict)}
    no_subs = sum(1 for r in rows if r.get("subs") is None)
    log("LOAD", explore=ex_p.relative_to(root).as_posix(), generated=explore.get("generated"), weeks=explore.get("weeks"), rows=len(rows),
        hidden_subs=no_subs, channels_cached=len(channels), pending_searches=len(explore.get("pending") or []),
        pending_videos=explore.get("pending_videos"))
    if explore.get("pending"):
        log("LOAD", logging.WARNING, note="못 한 검색이 있음 — 그 검색어의 분야는 표본이 작음 (할당량 초기화 뒤 resume → 다시 report)",
            pending=len(explore["pending"]))
    res = collect(rows, niches, channels, S, C, G, E, now)
    res = score(res)
    st = search_status(cache, niches, explore)
    md = write_report(root, topic, res, st, explore, S, C, G, now, root / topic / "result" / "niche")
    top = [f"{r['niche']}={r['score']}" for r in res[:5]]
    log("RESULT", file=md.relative_to(root).as_posix(), top5=",".join(top))
    return {"niches": len(res), "top5": top}


# ---------------------------------------------------------------- 명령
def main(argv=None):
    ap = argparse.ArgumentParser(description="새 채널 분야 비교 (할당량 0)")
    ap.add_argument("topic", help="주제 폴더 (예: new)")
    ap.add_argument("cmd", choices=["sync", "report"])
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args(argv)
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass
    logging.basicConfig(level=getattr(logging, a.log_level), format="%(message)s", stream=sys.stdout)
    if not re.fullmatch(r"[a-z][a-z0-9_-]{1,30}", a.topic):
        raise SystemExit(f"[START] ❌ 주제 폴더 이름이 이상함: {a.topic}")
    log("START", tool=f"niche_scan.py {VERSION}", topic=a.topic, cmd=a.cmd)
    res = cmd_sync(ROOT, a.topic) if a.cmd == "sync" else cmd_report(ROOT, a.topic)
    log("DONE", cmd=a.cmd, result=json.dumps(res, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
