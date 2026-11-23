#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.1.0 — 2026-11-23 — 주제 'adhd' 더함 (사용자 지시 2026-11-23 "ADHD 관련 성공 사례 찾아봐") · 주제마다 세부 칸 이름
#          (focus_name)·아이(육아) 표시(child)·지시 문장(ask)을 TOPICS 에 둠 — 우울증 결과는 그대로
# (이전) v1.0.0 — 2026-11-23 — 신규: 주제 하나(예: 우울증 증상)의 성공 사례 영상 찾기
#          (사용자 지시 2026-11-23 "우울증 증상과 관련된 성공 사례 영상 찾아서 알려줘봐")
"""
topic_success.py — 심리 주제 하나를 골라 그 주제 영상 중 '성공 사례'(심리 analysis_rules.toml [success] 그대로)를 찾음

흐름
  1. LOAD-A : 이미 받은 캐시 — 심리 분석(psychology/cloud_cache/cache.tgz) · 사례 검색(result/incidents/api_cache.json.gz)
              · 이 도구 캐시(result/topics/api_cache.json.gz)  (할당량 0)
  2. LOAD-B : TOPICS[key]['queries'] × (videoDuration medium · long 중 TOPICS 가 고른 것)
              search(order=viewCount, KR, ko, publishedAfter = 기준일 − WINDOW_DAYS) → videos · channels
  3. VALIDATE : 통계 빠짐 · 한글 없는 제목 · 라이브 · 4분 미만 · 같은 영상
  4. FILTER : 제목에 주제 낱말(words) — 빼는 낱말(exclude: 노래·플레이리스트 등) · 세부 칸(focus: 증상·신호·자가진단…)
  5. METRICS : 하루 조회수 · 구독자 배수 · 구독자당 하루 조회수 → 성공(심리 기준) / 거의 성공(기준 하나만 못 넘음)
  6. EXPORT : result/topics/<key>.md · <key>.csv

한계: 검색은 검색어마다 조회수 상위 50개 = 위쪽 꼬리 · 성공 기준은 받은 날 조회수 기준 · 판정은 제목 낱말로만 (대본 안 봄)
실행: python3 psychology/source/topic_success.py run depression      # 캐시 없을 때만 API
      python3 psychology/source/topic_success.py analyze depression  # 캐시만
"""
from __future__ import annotations

import csv
import gzip
import hashlib
import io
import json
import logging
import os
import re
import sys
import tarfile
import time
import tomllib
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests

VERSION = "v1.1.0"
HERE = Path(__file__).resolve().parent
PSY = HERE.parent
OUT_DIR = PSY / "result" / "topics"
API_CACHE = OUT_DIR / "api_cache.json.gz"
PSY_TGZ = PSY / "cloud_cache" / "cache.tgz"
INC_CACHE = PSY / "result" / "incidents" / "api_cache.json.gz"
RULES_TOML = PSY / "analysis_rules.toml"
API = "https://www.googleapis.com/youtube/v3"
AS_OF = datetime(2026, 11, 23, tzinfo=timezone.utc)
WINDOW_DAYS = 180          # 성공 기준 MAX_AGE_DAYS 와 같음 — 검색도 그 기간만
HANGUL = re.compile(r"[가-힣]")

TOPICS = {
    "depression": {
        "name": "우울증 증상",
        "queries": ["우울증 증상", "우울증 초기 증상", "우울증 자가진단", "고기능 우울증", "우울증 신호",
                    "가면 우울증", "우울증 특징"],
        "long_queries": ["우울증 증상", "우울증 특징", "고기능 우울증"],   # 20분 넘는 영상도 (3번)
        "words": r"우울",
        "exclude": r"노래|플레이리스트|playlist|ASMR|asmr|bgm|BGM|음악|가사|피아노|lofi|로파이|노동요",
        "focus": r"증상|신호|특징|자가 ?진단|체크|테스트|징후|티 ?나|티가|말투|행동|습관|모습|변화|나타나|알아차|의심|진단|단계|유형|종류",
        "focus_name": "증상·신호 쪽",
        "ask": "우울증 증상과 관련된 성공 사례 영상 찾아서 알려줘봐",
    },
    # v1.1.0
    "adhd": {
        "name": "ADHD",
        "queries": ["성인 ADHD", "ADHD 증상", "ADHD 특징", "ADHD 자가진단", "성인 ADHD 증상", "조용한 ADHD",
                    "ADHD 약", "여성 ADHD"],
        "long_queries": ["성인 ADHD", "ADHD 특징"],
        "words": r"ADHD|adhd|Adhd|에이디에이치디|주의력 ?결핍|과잉 ?행동",
        "exclude": r"노래|플레이리스트|playlist|ASMR|asmr|bgm|BGM|음악|가사|피아노|lofi|로파이|노동요|공부 ?자극|스터디 ?윗미|study with me",
        "focus": r"증상|신호|특징|자가 ?진단|체크|테스트|징후|티 ?나|티가|말투|행동|습관|모습|유형|종류|진단",
        "focus_name": "증상·특징 쪽",
        "child": r"아이|아동|어린이|자녀|우리 ?애|유아|초등|소아|엄마표|육아|키즈|학부모",
        "ask": "ADHD 관련 성공 사례 찾아봐",
    },
}

log = logging.getLogger("topic_success")


def L(stage: str, level: int = logging.INFO, **kv) -> None:
    log.log(level, " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if not isinstance(v, str) or ' ' in v else v}"
                            for k, v in kv.items()), extra={"stage": stage})


class F(logging.Formatter):
    def format(self, r):
        lv = "" if r.levelno == logging.INFO else f" level={r.levelname}"
        return f"[{getattr(r, 'stage', 'MAIN')}] [{datetime.now():%Y-%m-%dT%H:%M:%S}]{lv} {r.getMessage()}"


def iso_sec(s: str | None) -> int:
    m = re.fullmatch(r"P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", s or "")
    return sum(int(x or 0) * k for x, k in zip(m.groups(), (86400, 3600, 60, 1))) if m else 0


class YT:
    COST = {"search": 100, "videos": 1, "channels": 1}

    def __init__(self, key, offline):
        self.key, self.offline = key, offline
        self.units = self.calls = self.hits = 0
        self.cache = json.loads(gzip.decompress(API_CACHE.read_bytes())) if API_CACHE.exists() else {}
        self.dirty = False

    def get(self, endpoint, **params):
        params = {k: v for k, v in params.items() if v is not None}
        h = hashlib.sha1(json.dumps([endpoint, params], sort_keys=True, ensure_ascii=False).encode()).hexdigest()[:16]
        if h in self.cache:
            self.hits += 1
            return self.cache[h]
        if self.offline or not self.key:
            return None
        try:
            r = requests.get(f"{API}/{endpoint}", params={**params, "key": self.key}, timeout=30)
        except requests.RequestException as e:
            L("LOAD", logging.WARNING, error="network", endpoint=endpoint, detail=str(e)[:150], next_step="run 다시")
            return None
        self.calls += 1
        self.units += self.COST.get(endpoint, 1)
        if r.status_code != 200:
            L("LOAD", logging.WARNING, error=f"http{r.status_code}", endpoint=endpoint, body=r.text[:150],
              next_step="할당량이면 한국 17시 뒤 run 다시 (받은 것은 캐시에)")
            return None
        d = r.json()
        items = d.get("items", [])
        if endpoint == "search":
            d = {"items": [{"id": it["id"]} for it in items]}
        elif endpoint == "videos":
            d = {"items": [{"id": it["id"], "snippet": {k: it["snippet"].get(k) for k in
                                                        ("title", "channelId", "channelTitle", "publishedAt", "liveBroadcastContent")},
                            "statistics": it.get("statistics", {}),
                            "contentDetails": {"duration": it.get("contentDetails", {}).get("duration")}} for it in items]}
        else:
            d = {"items": [{"id": it["id"], "statistics": it.get("statistics", {})} for it in items]}
        self.cache[h] = d
        self.dirty = True
        return d

    def save(self):
        if self.dirty:
            OUT_DIR.mkdir(parents=True, exist_ok=True)
            API_CACHE.write_bytes(gzip.compress(json.dumps(self.cache, ensure_ascii=False).encode(), mtime=0))


def load_cached() -> tuple[dict, dict]:
    """이미 받은 영상(id → row)과 채널 구독자(id → subs)."""
    vids, subs = {}, {}
    if PSY_TGZ.exists():
        with tarfile.open(PSY_TGZ) as tf:
            for m in tf.getmembers():
                if not (m.isfile() and m.name.endswith(".json") and "/.cache/" in m.name):
                    continue
                d = json.load(io.TextIOWrapper(tf.extractfile(m), encoding="utf-8"))
                if m.name.endswith("/channels.json"):
                    subs.update({cid: c.get("subs") for cid, c in d.items()})
                elif isinstance(d, dict) and "channel_id" in d:
                    vids[d["id"]] = {"video_id": d["id"], "title": d["title"], "channel_id": d["channel_id"],
                                     "channel": d.get("channel", ""), "published": d.get("published"),
                                     "views": d.get("view_count"), "likes": d.get("like_count"),
                                     "comments": d.get("comment_count"), "sec": d.get("duration") or 0,
                                     "live": bool(d.get("live") or d.get("was_live")), "source": "심리 분석 캐시",
                                     "fetched": (d.get("fetched") or "")[:10]}
    for path, label in ((INC_CACHE, "사례 검색 캐시"),):
        if not path.exists():
            continue
        for v in json.loads(gzip.decompress(path.read_bytes())).values():
            for it in v.get("items", []):
                sn = it.get("snippet", {})
                if "contentDetails" in it and "channelId" in sn:
                    st = it.get("statistics", {})
                    vids.setdefault(it["id"], {"video_id": it["id"], "title": sn.get("title", ""), "channel_id": sn["channelId"],
                                               "channel": sn.get("channelTitle", ""), "published": sn.get("publishedAt"),
                                               "views": st.get("viewCount"), "likes": st.get("likeCount"),
                                               "comments": st.get("commentCount"), "sec": iso_sec(it["contentDetails"].get("duration")),
                                               "live": sn.get("liveBroadcastContent", "none") != "none", "source": label,
                                               "fetched": "2026-11-23"})
                elif "statistics" in it and "snippet" not in it:
                    subs.setdefault(it["id"], it["statistics"].get("subscriberCount"))
    L("LOAD", source="caches (심리 분석 + 사례 검색)", videos=len(vids), channels_with_subs=len(subs))
    return vids, subs


def load_search(yt: YT, topic: dict, vids: dict, subs: dict) -> set:
    after = (AS_OF - timedelta(days=WINDOW_DAYS)).strftime("%Y-%m-%dT%H:%M:%SZ")
    hits = set()
    plan = [(q, "medium") for q in topic["queries"]] + [(q, "long") for q in topic.get("long_queries", [])]
    for q, dur in plan:
        d = yt.get("search", part="snippet", q=q, type="video", order="viewCount", maxResults=50, regionCode="KR",
                   relevanceLanguage="ko", videoDuration=dur, publishedAfter=after)
        if d is None:
            L("LOAD", logging.DEBUG if yt.offline else logging.WARNING, query=q, duration=dur, error="no_response")
            continue
        hits.update(it["id"]["videoId"] for it in d.get("items", []) if it.get("id", {}).get("videoId"))
    need = sorted(hits)
    for i in range(0, len(need), 50):
        d = yt.get("videos", part="snippet,statistics,contentDetails", id=",".join(need[i:i + 50]), maxResults=50)
        for it in (d or {}).get("items", []):
            sn, st = it["snippet"], it.get("statistics", {})
            vids[it["id"]] = {"video_id": it["id"], "title": sn.get("title", ""), "channel_id": sn.get("channelId"),
                              "channel": sn.get("channelTitle", ""), "published": sn.get("publishedAt"),
                              "views": st.get("viewCount"), "likes": st.get("likeCount"), "comments": st.get("commentCount"),
                              "sec": iso_sec(it["contentDetails"].get("duration")),
                              "live": sn.get("liveBroadcastContent", "none") != "none", "source": "주제 검색",
                              "fetched": "2026-11-23"}
    chans = sorted({vids[v]["channel_id"] for v in hits if v in vids})
    for i in range(0, len(chans), 50):
        d = yt.get("channels", part="statistics", id=",".join(chans[i:i + 50]), maxResults=50)
        for it in (d or {}).get("items", []):
            st = it.get("statistics", {})
            subs[it["id"]] = None if st.get("hiddenSubscriberCount") else st.get("subscriberCount")
    L("LOAD", source="search(order=viewCount,KR,ko)", searches=len(plan), window_days=WINDOW_DAYS,
      date_range=f"{after[:10]}~{AS_OF:%Y-%m-%d}", hits=len(hits), api_calls=yt.calls, units=yt.units, cache_hits=yt.hits)
    return hits


def rules() -> dict:
    with open(RULES_TOML, "rb") as f:
        s = tomllib.load(f)["success"]
    return {k: s[k] for k in ("MIN_AGE_DAYS", "MAX_AGE_DAYS", "MAX_SUBS", "MIN_VPD_SUBS", "MIN_VIEWS", "MIN_MINUTES")}


def evaluate(r: dict, R: dict) -> dict:
    """성공 기준마다 통과 여부 — 못 넘은 기준 이름을 돌려줌 (거의 성공 = 하나만 못 넘음)."""
    pub = datetime.fromisoformat(str(r["published"]).replace("Z", "+00:00"))
    fetched = datetime.fromisoformat(r["fetched"] + "T00:00:00+00:00") if r.get("fetched") else AS_OF
    age = max((fetched - pub).total_seconds() / 86400, 1)
    views, sub = int(r["views"]), int(r["subs"]) if r.get("subs") not in (None, "") else None
    base = max(sub or 0, 100)
    vpd = views / age
    out = {"age_days": round(age, 1), "vpd": vpd, "ratio": views / base, "vpd_subs": vpd / base, "minutes": r["sec"] / 60}
    fails = []
    if not (R["MIN_AGE_DAYS"] <= age <= R["MAX_AGE_DAYS"]):
        fails.append(f"올린 지 {age:.0f}일")
    if sub is None or sub > R["MAX_SUBS"]:
        fails.append(f"구독자 {sub if sub is not None else '숨김'}")
    if out["vpd_subs"] < R["MIN_VPD_SUBS"]:
        fails.append(f"구독자당 하루 {out['vpd_subs']:.2f}")
    if views < R["MIN_VIEWS"]:
        fails.append(f"조회수 {views:,}")
    if out["minutes"] < R["MIN_MINUTES"]:
        fails.append("4분 미만")
    out["fails"] = fails
    return out


def classify(vids: dict, subs: dict, topic: dict, R: dict) -> list[dict]:
    W, X, FO = re.compile(topic["words"]), re.compile(topic["exclude"]), re.compile(topic["focus"])
    rows, drop = [], {"no_topic_word": 0, "excluded_word": 0, "invalid": 0}
    for v in vids.values():
        t = v["title"] or ""
        if not W.search(t):
            drop["no_topic_word"] += 1
            continue
        if X.search(t):
            drop["excluded_word"] += 1
            continue
        if v["views"] in (None, "") or not HANGUL.search(t) or v["live"] or v["sec"] < 240 or not v.get("published"):
            drop["invalid"] += 1
            continue
        r = dict(v, subs=subs.get(v["channel_id"]))
        r.update(evaluate(r, R))
        r["focus"] = bool(FO.search(t))
        r["child"] = bool(re.search(topic["child"], t)) if topic.get("child") else False   # v1.1.0: 아이(육아) 쪽
        rows.append(r)
    L("VALIDATE", **{f"drop_{k}": n for k, n in drop.items()}, topic_rows=len(rows),
      success=sum(not r["fails"] for r in rows), near=sum(len(r["fails"]) == 1 for r in rows),
      focus_rows=sum(r["focus"] for r in rows))
    return rows


def n(x) -> str:
    x = float(x)
    return f"{x / 1e4:,.1f}만" if x >= 1e4 else f"{x:,.0f}"


def export(key: str, topic: dict, rows: list[dict], R: dict, yt: YT, t0: float) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    cols = ["video_id", "title", "channel", "subs", "views", "likes", "comments", "published", "age_days", "minutes",
            "vpd", "ratio", "vpd_subs", "focus", "child", "fails", "source"]
    with open(OUT_DIR / f"{key}.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for r in sorted(rows, key=lambda r: -r["vpd_subs"]):
            w.writerow({**r, "fails": " / ".join(r["fails"])})
    succ = sorted([r for r in rows if not r["fails"]], key=lambda r: -r["vpd_subs"])
    near = sorted([r for r in rows if len(r["fails"]) == 1], key=lambda r: -r["vpd"])

    def table(rs, extra=False):
        fn = topic.get("focus_name", "세부 쪽")
        ch = " 아이(육아) |" if topic.get("child") else ""
        o = [f"| # | 영상 | 채널 | 구독자 | 조회수 | 구독자 배수 | 구독자당 하루 | 올린 날 | 길이 | {fn} |{ch}" + (" 못 넘은 기준 |" if extra else ""),
             "|---|---|---|---|---|---|---|---|---|---|" + ("---|" if ch else "") + ("---|" if extra else "")]
        for i, r in enumerate(rs, 1):
            o.append(f"| {i} | [{r['title'].replace('|', '／')[:70]}](https://youtu.be/{r['video_id']}) | {r['channel'][:16]} | "
                     f"{n(r['subs']) if r['subs'] not in (None, '') else '숨김'} | {n(r['views'])} | {r['ratio']:.1f} | {r['vpd_subs']:.2f} | "
                     f"{str(r['published'])[:10]} | {r['minutes']:.1f}분 | {'예' if r['focus'] else ''} |" +
                     ((" 예 |" if r.get("child") else "  |") if ch else "") +
                     (f" {' / '.join(r['fails'])} |" if extra else ""))
        return o

    out = [f"# 심리 — '{topic['name']}' 성공 사례 영상", "",
           f"VERSION: {VERSION} — 도구 `psychology/source/topic_success.py {key}` · 기준일 {AS_OF:%Y-%m-%d} · 사용자 지시 2026-11-23 \"{topic.get('ask', '')}\"", "",
           "## 0. 읽는 법·한계",
           f"- 성공 기준 = 심리 `analysis_rules.toml [success]` 그대로: 올린 지 {R['MIN_AGE_DAYS']}~{R['MAX_AGE_DAYS']}일 · 구독자 ≤ {R['MAX_SUBS']:,} · "
           f"구독자당 하루 조회수 ≥ {R['MIN_VPD_SUBS']} · 조회수 ≥ {R['MIN_VIEWS']:,} · {R['MIN_MINUTES']:.0f}분 이상 (채널당 제한 없음).",
           f"- 자료: 심리 분석·사례 검색 캐시 + 이 주제 검색 {len(topic['queries'])}개(4~20분) + {len(topic.get('long_queries', []))}개(20분 넘음), 최근 {WINDOW_DAYS}일 · 조회수 순 50개씩 = 위쪽 꼬리만.",
           f"- 주제 = 제목에 '{topic['words']}' · 빼는 낱말 = 노래·플레이리스트·ASMR·음악 등 · **{topic.get('focus_name', '세부 쪽')}** = 제목에 증상·신호·특징·자가진단 등"
           + (" · **아이(육아)** = 제목에 아이·자녀·초등·소아 등 (심리 분석 때 육아는 주제 밖으로 뺀 갈래)." if topic.get("child") else "."),
           "- 판정은 제목 낱말로만 — 대본을 본 것이 아님. 정신건강 정보는 대본 전에 연구·공공기관 자료로 확인. 연구·교육용 (의료 상담 아님).", "",
           f"## 1. 성공 사례 ({len(succ)}개 — 구독자당 하루 조회수 순)", ""] + table(succ) + ["",
           f"## 2. 거의 성공 — 기준 하나만 못 넘음 (하루 조회수 순 상위 25 / {len(near)}개)", ""] + table(near[:25], True) + ["",
           f"_주제 영상 {len(rows)}개 · API {yt.calls}번 {yt.units}단위 · 캐시 {yt.hits}번 · {time.time() - t0:.1f}초_"]
    (OUT_DIR / f"{key}.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    L("EXPORT", md=str((OUT_DIR / f"{key}.md").relative_to(PSY.parent)), success=len(succ), near=len(near),
      success_focus=sum(r["focus"] for r in succ))


def main(argv) -> int:
    h = logging.StreamHandler(sys.stdout)
    h.setFormatter(F())
    log.handlers[:] = [h]
    log.setLevel(os.environ.get("LOG_LEVEL", "INFO").upper())
    if len(argv) < 3 or argv[1] not in ("run", "analyze") or argv[2] not in TOPICS:
        print(__doc__, "\n주제:", ", ".join(TOPICS))
        return 2
    cmd, key = argv[1], argv[2]
    t0 = time.time()
    R = rules()
    L("START", tool=f"topic_success.py {VERSION}", cmd=cmd, topic=key, as_of=f"{AS_OF:%Y-%m-%d}", success_rules=R)
    yt = YT(os.environ.get("YOUTUBE_API_KEY"), offline=(cmd != "run"))
    vids, subs = load_cached()
    load_search(yt, TOPICS[key], vids, subs)
    yt.save()
    rows = classify(vids, subs, TOPICS[key], R)
    export(key, TOPICS[key], rows, R, yt, t0)
    L("RESULT", seconds=round(time.time() - t0, 1), api_units=yt.units)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
