#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.2 — 2026-11-27 — 주제 접두사 키 (<주제>_YOUTUBE_API_KEY · tools/topic_keys.apply — 사용자 지시 2026-11-27 "주제별 접두사를 변수명에 붙여서 구분되도록해").
# (v1.1) — 2026-11-27 — 꺼 둔 주제(studio/state/topics.json)는 시작하지 않음 — 사용자 지시 2026-11-27 "비활성화하면 … 에이전트가 보지도 않도록". 함수 main.
# (v1.0) — 2026-11-25 — 새로: 주제마다 쓰는 '다음 영상 주제 탐색' (psychology/source/next_topic.py v1.1 의 네 단계를 그대로 —
#          주제 묶음·주제 채널 낱말·거르기·겹침 후보·트렌드 낱말은 <주제>/next_topic.toml 로 뺌) + suggest(유튜브 자동완성 실시간)
#   사용자 지시 2026-11-25 "심리 주제에서 했던 것처럼 주제탐색에 필요한 4가지 그대로 수행해서 영상 만들 주제 알려줘 그리고 트렌드 사이트는 왜
#   막히는거야 안 막히고 돌리는 방법 없어? 내가 코드를 실행한다던가".
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.0 | 2026-11-25 | 최초 — 심리 v1.1 계산 그대로 (recent·big·report·overlap·trends) · 설정 파일 · 캐시 두 조각(.001·.002) 읽기 · suggest · trends_batches.json (PC 트렌드 받기 tools/pc_trends.py 용) | 모두 |
"""다음 영상 주제 탐색 — 숫자와 원문만 만든다 (주제 판단은 이 결과를 읽는 Claude 가 `<주제>/result/next_topic/next_topic.md` 에).

네 단계 (심리 세션 사용자 지시 2026-11-25):
  1. 관심 높은 키워드 — suggest(유튜브 자동완성, 할당량 0) + trends(구글 트렌드 CSV — 사람이 받거나 PC tools/pc_trends.py)
  2. 시청자가 많이 본 영상 — recent: 주제 관련 4분+ 롱폼 조회수 상위 N개 → 최신 댓글 → 최근 7일 댓글 수 = 무게
  3. 구독자 많은 채널이 많이 다루는 주제 — big: 구독자 10만+ · 주제 채널(STRICT 낱말 제목 15%+) 최근 1년 → 주제별 채널 수·채널 안 상대 조회수
  4. 성공적으로 추천된 주제 — report: 대리 지표(좋아요÷조회수 · 댓글÷조회수 · 조회수÷구독자 — 같은 구독자 구간 안) · 비교 집단 성공 비율
  + 겹침 — overlap: 후보마다 유튜브 검색 → 제목에 핵심 낱말이 있는 같은 주제 영상 · 100만+ = ⚠ (시청자가 이미 많이 본 내용)

자료: <주제>/cloud_cache/cache.tgz (또는 .001·.002 조각) · <주제>/result/outliers/compare.csv · YouTube Data API (키 = 환경 변수 YOUTUBE_API_KEY — 출력 안 함)
     · suggestqueries.google.com (유튜브 자동완성)
설정: <주제>/next_topic.toml (주제 묶음 [[topics]] · [filter] · [big] · [trends] · [[overlap]])
결과: <주제>/result/next_topic/ (recent.json.gz · big.json.gz · next_topic_data.md · suggest.md · overlap.md · trends_batches.md·.json · trends.md)

  python3 tools/next_topic.py history recent --top 300
  python3 tools/next_topic.py history big
  python3 tools/next_topic.py history report
  python3 tools/next_topic.py history suggest            # 자동완성 (설정 [trends] WORDS + 주제 묶음 이름의 첫 낱말)
  python3 tools/next_topic.py history overlap            # 설정 [[overlap]] 후보마다 검색 1~2번 (1번 = 100단위)
  python3 tools/next_topic.py history trends             # trends/batch_NN.csv 합치기

한계 — 다른 채널 영상의 클릭률·시청 지속률·트래픽 소스는 공개 API 로 볼 수 없다 → 대리 지표(추정)만. 주제 묶음은 제목 낱말 규칙. 연구·교육용.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import gzip
import io
import json
import logging
import os
import re
import statistics as st
import sys
import tarfile
import time
import tomllib
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
API = "https://www.googleapis.com/youtube/v3/"
SUGGEST = "https://suggestqueries.google.com/complete/search"
VERSION = "v1.2"
RECENT_DAYS = 7          # 심리 사용자 지시 2026-11-25 "2번에서 최근 7일 동안으로 변경"
MAX_COMMENT_PAGES = 5    # 최신 댓글 100개씩 최대 5쪽
LONG_SEC = 240           # 4분 이상 = 롱폼
MEGA_VIEWS = 1_000_000   # 겹침: 100만+ = 이미 많이 본 내용
log = logging.getLogger("next_topic")


def stamp(stage: str, **kv) -> None:
    log.info("[%s] [%s] %s", stage, time.strftime("%Y-%m-%dT%H:%M:%S"), " ".join(f"{k}={v}" for k, v in kv.items()))


class Cfg:
    """주제 설정 — <주제>/next_topic.toml."""

    def __init__(self, topic: str):
        self.topic = topic
        self.dir = ROOT / topic
        p = self.dir / "next_topic.toml"
        try:
            d = tomllib.loads(p.read_text("utf-8"))
        except (OSError, tomllib.TOMLDecodeError) as ex:
            raise SystemExit(f"[CONFIG] {p.relative_to(ROOT)} 를 읽지 못함 ({ex}) — 주제 설정을 먼저 만든다 (history/next_topic.toml 참고)")
        self.raw = d
        self.name = d.get("name", topic)
        self.topics = [(t["name"], t["rx"]) for t in d.get("topics", [])]
        self.topic_rx = [(n, re.compile(rx, re.I)) for n, rx in self.topics]
        f = d.get("filter", {})
        self.noise_title = re.compile(f.get("NOISE_TITLE") or r"$^", re.I)
        self.noise_channel = re.compile(f.get("NOISE_CHANNEL") or r"$^", re.I)
        self.broadcast = re.compile(f.get("BROADCAST") or r"$^", re.I)
        self.strict = re.compile(f.get("STRICT") or r"$^", re.I)
        b = d.get("big", {})
        self.big_min_subs = int(b.get("MIN_SUBS", 100_000))
        self.big_min_topic_videos = int(b.get("MIN_TOPIC_VIDEOS", 3))
        self.big_share = float(b.get("SHARE", 0.15))
        self.big_days = int(b.get("DAYS", 365))
        t = d.get("trends", {})
        self.trend_anchor = t.get("ANCHOR") or self.name
        self.trend_words = list(t.get("WORDS") or [])
        self.cands = [(o["key"], o["name"], list(o.get("queries") or []), o.get("core") or r"$^") for o in d.get("overlap", []) if o.get("queries")]
        self.out = self.dir / "result" / "next_topic"
        self.compare = self.dir / "result" / "outliers" / "compare.csv"
        stamp("CONFIG", topic=topic, file=str(p.relative_to(ROOT)), topics=len(self.topics), overlap_cands=len(self.cands),
              trend_words=len(self.trend_words), big_min_subs=self.big_min_subs, big_share=self.big_share)

    def topics_of(self, text: str) -> list[str]:
        return [n for n, rx in self.topic_rx if rx.search(text or "")]


def now_utc() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def parse_ts(s: str) -> dt.datetime:
    return dt.datetime.fromisoformat(s.replace("Z", "+00:00"))


def iso_dur(s: str) -> int:
    m = re.fullmatch(r"P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", s or "")
    if not m:
        return 0
    d, h, mi, se = (int(x or 0) for x in m.groups())
    return d * 86400 + h * 3600 + mi * 60 + se


# ─────────── 자료 읽기 ───────────
def open_cache(c: Cfg) -> tarfile.TarFile:
    """cache.tgz 또는 조각(cache.tgz.001, .002 …)을 이어 붙여 메모리에서 연다 (cloud_run.py 가 50MB 넘으면 조각으로 저장)."""
    cdir = c.dir / "cloud_cache"
    whole = cdir / "cache.tgz"
    parts = sorted(cdir.glob("cache.tgz.[0-9][0-9][0-9]"))
    try:
        if whole.is_file():
            return tarfile.open(whole, "r:gz")
        if parts:
            return tarfile.open(fileobj=io.BytesIO(b"".join(p.read_bytes() for p in parts)), mode="r:gz")
    except (OSError, tarfile.TarError) as ex:
        raise SystemExit(f"[LOAD] {cdir.relative_to(ROOT)} 캐시를 읽지 못함 ({ex}) — cloud_run.py {c.topic} resume 으로 캐시를 먼저")
    raise SystemExit(f"[LOAD] {cdir.relative_to(ROOT)} 에 cache.tgz 가 없음 — cloud_run.py {c.topic} explore 먼저")


def load_cache(c: Cfg) -> tuple[dict, dict, dict]:
    """캐시 → (영상 dict, 채널 dict, 자동완성 dict) — 풀지 않고 메모리에서."""
    vids, chans, auto = {}, {}, {}
    with open_cache(c) as tf:
        for m in tf.getmembers():
            if not m.isfile() or "/.cache/" not in m.name:
                continue
            base = m.name.rsplit("/", 1)[-1]
            body = tf.extractfile(m).read()
            if base == "channels.json":
                chans = json.loads(body)
            elif base == "autocomplete.json":
                auto = json.loads(body)
            elif re.fullmatch(r"[A-Za-z0-9_-]{11}\.json", base):
                vids[base[:-5]] = json.loads(body)
    try:
        rows = {r["id"]: r for r in csv.DictReader(open(c.compare, encoding="utf-8-sig"))}
    except OSError as ex:
        raise SystemExit(f"[LOAD] {c.compare.relative_to(ROOT)} 없음 ({ex}) — cloud_run.py {c.topic} analyze 먼저")
    for vid, v in vids.items():
        r = rows.get(vid, {})
        v["theme"], v["exclude"], v["success"] = r.get("theme", ""), r.get("exclude", "주제 밖(compare 없음)"), r.get("success") == "True"
        v["in_compare"] = r.get("in_compare") == "True"
        v["subs"] = (chans.get(v.get("channel_id"), {}) or {}).get("subs") or 0
    saved = "?"
    try:
        saved = json.loads((c.dir / "cloud_cache" / "cache.json").read_text("utf-8")).get("saved", "?")
    except (OSError, ValueError):
        pass
    stamp("LOAD", videos=len(vids), channels=len(chans), autocomplete_seeds=len(auto), compare_rows=len(rows), cache_saved=saved)
    return vids, chans, auto


def related(c: Cfg, vids: dict) -> list[dict]:
    """주제 관련 롱폼 — compare.csv 에서 뺀 것(주제 밖·외국·라이브)이 아니고 4분 이상 · 음악·게임·뉴스 등(NOISE_*)이 아님."""
    base = [v for v in vids.values() if v["exclude"] == "" and (v.get("duration") or 0) >= LONG_SEC and not v.get("live")]
    keep = [v for v in base if not c.noise_title.search(v["title"]) and not c.noise_channel.search(v.get("channel") or "")]
    if not getattr(related, "_logged", False):
        stamp("FILTER", related_long=len(base), kept=len(keep), noise=len(base) - len(keep), rule="NOISE_TITLE·NOISE_CHANNEL")
        related._logged = True
    return keep


# ─────────── API ───────────
class Api:
    COST = {"search": 100}       # YouTube 할당량 단위 (그 밖의 list 는 1)

    def __init__(self):
        self.key = os.environ.get("YOUTUBE_API_KEY", "")
        if not self.key:
            raise SystemExit("[API] YOUTUBE_API_KEY 없음 — 환경 변수로 넣는다 (값은 출력하지 않음)")
        self.units = 0

    def get(self, ep: str, **params) -> dict:
        params["key"] = self.key
        cost = self.COST.get(ep, 1)
        url = API + ep + "?" + urllib.parse.urlencode(params)
        for attempt in range(4):
            try:
                with urllib.request.urlopen(url, timeout=40) as r:
                    self.units += cost
                    return json.load(r)
            except urllib.error.HTTPError as e:
                self.units += cost
                body = e.read().decode("utf-8", "replace")
                reason = (re.search(r'"reason":\s*"([^"]+)"', body) or [None, "?"])[1]
                if reason in ("commentsDisabled", "videoNotFound", "forbidden", "channelNotFound", "playlistNotFound"):
                    return {"_error": reason}
                if reason in ("quotaExceeded", "dailyLimitExceeded"):
                    raise SystemExit(f"[API] 할당량 끝 ({ep}) — 한국 17시 뒤 다시 (지금까지 {self.units}단위 · 받은 것은 저장됨, 다시 실행하면 이어서)")
                if e.code in (429, 500, 503) and attempt < 3:
                    time.sleep(2 ** attempt * 3)
                    continue
                raise SystemExit(f"[API] {ep} HTTP {e.code} {reason} — 입력 {params.get('videoId') or params.get('id') or params.get('playlistId') or params.get('q')} · 다음: 잠시 뒤 다시")
            except (urllib.error.URLError, TimeoutError) as e:
                if attempt < 3:
                    time.sleep(2 ** attempt * 3)
                    continue
                raise SystemExit(f"[API] {ep} 네트워크 실패 ({type(e).__name__}) — 프록시·인터넷 확인 뒤 다시")
        return {}


def save_gz(c: Cfg, name: str, obj) -> Path:
    c.out.mkdir(parents=True, exist_ok=True)
    p = c.out / name
    with gzip.open(p, "wt", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False)
    return p


def load_gz(c: Cfg, name: str, default=None):
    p = c.out / name
    if not p.exists():
        return default
    with gzip.open(p, "rt", encoding="utf-8") as f:
        return json.load(f)


# ─────────── 2. 많이 본 영상 + 최근 7일 댓글 ───────────
def cmd_recent(c: Cfg, a) -> int:
    vids, _, _ = load_cache(c)
    pool = sorted(related(c, vids), key=lambda v: -(v.get("view_count") or 0))[: a.top]
    stamp("RECENT", pool=len(pool), rule=f"주제 관련 4분+ · 조회수 큰 순 {a.top}개 (올린 날짜 상관없음)",
          views_min=pool[-1]["view_count"] if pool else 0, window_days=RECENT_DAYS)
    old = load_gz(c, "recent.json.gz", {}) or {}
    res = old.get("videos", {}) if old.get("asof", "")[:10] == now_utc().strftime("%Y-%m-%d") else {}
    api = Api()
    cut = now_utc() - dt.timedelta(days=RECENT_DAYS)
    for i, v in enumerate(pool, 1):
        if v["id"] in res:
            continue
        got, latest, token, pages, disabled = [], None, None, 0, False
        while pages < MAX_COMMENT_PAGES:
            p = {"part": "snippet", "videoId": v["id"], "order": "time", "maxResults": 100, "textFormat": "plainText"}
            if token:
                p["pageToken"] = token
            j = api.get("commentThreads", **p)
            pages += 1
            if j.get("_error"):
                disabled = True
                break
            items = j.get("items", [])
            for it in items:
                s = it["snippet"]["topLevelComment"]["snippet"]
                t = parse_ts(s["publishedAt"])
                latest = max(latest or s["publishedAt"], s["publishedAt"])
                if t >= cut:          # 작성자 이름·채널 ID 는 넣지 않음 (CLAUDE.md)
                    got.append({"t": s["publishedAt"][:16], "like": s.get("likeCount", 0), "reply": it["snippet"].get("totalReplyCount", 0),
                                "text": re.sub(r"\s+", " ", s.get("textDisplay", ""))[:400]})
            token = j.get("nextPageToken")
            if not token or not items or parse_ts(items[-1]["snippet"]["topLevelComment"]["snippet"]["publishedAt"]) < cut:
                break
        res[v["id"]] = {"recent7": len(got), "capped": bool(token) and pages >= MAX_COMMENT_PAGES and len(got) >= 100 * MAX_COMMENT_PAGES,
                        "latest": latest, "disabled": disabled, "comments": got}
        if i % 25 == 0:
            stamp("RECENT", done=i, of=len(pool), units=api.units)
            save_gz(c, "recent.json.gz", {"asof": now_utc().isoformat(timespec="seconds"), "window_days": RECENT_DAYS, "videos": res})
    res = {v["id"]: res[v["id"]] for v in pool if v["id"] in res}     # 지금 목록만 (거르기 규칙이 바뀌면 빠진 영상의 지난 결과는 버림)
    meta = {v["id"]: {k: v.get(k) for k in ("title", "channel", "channel_id", "published", "duration", "view_count", "like_count",
                                              "comment_count", "subs", "theme", "success")} for v in pool}
    save_gz(c, "recent.json.gz", {"asof": now_utc().isoformat(timespec="seconds"), "window_days": RECENT_DAYS, "top": a.top,
                                  "videos": res, "meta": meta, "tool": f"next_topic.py {VERSION}"})
    alive = [k for k, r in res.items() if r["recent7"] > 0]
    stamp("RECENT", status="done", units=api.units, videos=len(res), with_recent7=len(alive),
          recent7_total=sum(r["recent7"] for r in res.values()), disabled=sum(r["disabled"] for r in res.values()))
    return 0


# ─────────── 3. 큰 채널 ───────────
def cmd_big(c: Cfg, a) -> int:
    vids, chans, _ = load_cache(c)
    cnt = defaultdict(int)
    for v in related(c, vids) + [v for v in vids.values() if v["exclude"] == "" and (v.get("duration") or 0) < LONG_SEC]:
        cnt[v["channel_id"]] += 1
    cands = sorted([ch for ch, n in cnt.items() if n >= c.big_min_topic_videos and ((chans.get(ch) or {}).get("subs") or 0) >= c.big_min_subs],
                   key=lambda ch: -chans[ch]["subs"])
    if a.max_channels:
        cands = cands[: a.max_channels]
    stamp("BIG", candidates=len(cands), rule=f"구독자 {c.big_min_subs:,}+ · 지난 탐색 주제 관련 영상 {c.big_min_topic_videos}+" + (f" · 큰 순 {a.max_channels}곳까지" if a.max_channels else ""))
    api = Api()
    old = load_gz(c, "big.json.gz", {}) or {}
    data = old.get("channels", {}) if old.get("asof", "")[:10] == now_utc().strftime("%Y-%m-%d") else {}
    up = {}
    for k in range(0, len(cands), 50):
        j = api.get("channels", part="contentDetails", id=",".join(cands[k:k + 50]), maxResults=50)
        for it in j.get("items", []):
            up[it["id"]] = it["contentDetails"]["relatedPlaylists"]["uploads"]
    cut = now_utc() - dt.timedelta(days=c.big_days)
    for i, ch in enumerate(cands, 1):
        if ch in data or ch not in up:
            continue
        ids, token, pages = [], None, 0
        while pages < 8:
            p = {"part": "contentDetails", "playlistId": up[ch], "maxResults": 50}
            if token:
                p["pageToken"] = token
            j = api.get("playlistItems", **p)
            pages += 1
            if j.get("_error"):
                break
            its = j.get("items", [])
            ids += [it["contentDetails"]["videoId"] for it in its if parse_ts(it["contentDetails"].get("videoPublishedAt") or "1970-01-01T00:00:00Z") >= cut]
            token = j.get("nextPageToken")
            if not token or not its or parse_ts(its[-1]["contentDetails"].get("videoPublishedAt") or "1970-01-01T00:00:00Z") < cut:
                break
        rows = []
        for k in range(0, len(ids), 50):
            j = api.get("videos", part="snippet,statistics,contentDetails", id=",".join(ids[k:k + 50]), maxResults=50)
            for it in j.get("items", []):
                sn, stt = it["snippet"], it.get("statistics", {})
                rows.append({"id": it["id"], "title": sn["title"], "published": sn["publishedAt"],
                             "dur": iso_dur(it["contentDetails"].get("duration", "")), "views": int(stt.get("viewCount", 0) or 0),
                             "likes": int(stt.get("likeCount", 0) or 0), "comments": int(stt.get("commentCount", 0) or 0),
                             "live": sn.get("liveBroadcastContent", "none") != "none"})
        data[ch] = {"title": chans[ch].get("title"), "subs": chans[ch]["subs"], "videos": rows}
        if i % 10 == 0:
            stamp("BIG", done=i, of=len(cands), units=api.units)
            save_gz(c, "big.json.gz", {"asof": now_utc().isoformat(timespec="seconds"), "channels": data})
    save_gz(c, "big.json.gz", {"asof": now_utc().isoformat(timespec="seconds"), "channels": data, "tool": f"next_topic.py {VERSION}",
                               "rule": {"min_subs": c.big_min_subs, "min_topic_videos": c.big_min_topic_videos, "days": c.big_days, "share": c.big_share}})
    stamp("BIG", status="done", units=api.units, channels=len(data), videos=sum(len(d["videos"]) for d in data.values()))
    return 0


# ─────────── 4. 대리 지표 · 겹침 · 자동완성 · 보고 ───────────
def band(subs: int) -> str:
    return "1만 미만" if subs < 10_000 else "1만~10만" if subs < 100_000 else "10만~50만" if subs < 500_000 else "50만+"


def med(xs, default=0.0):
    xs = [x for x in xs if x is not None]
    return st.median(xs) if xs else default


def fmt(n) -> str:
    n = float(n)
    return f"{n / 1e4:,.1f}만" if n >= 1e4 else f"{n:,.0f}"


def big_tables(c: Cfg, big: dict) -> tuple[list[str], dict, list[dict]]:
    """주제 큰 채널만 → 주제별 채널 수·영상 수·채널 안 상대 조회수 (가운데값·1.5배+ 몫)."""
    lines, by_topic, allv, kept = [], defaultdict(list), [], []
    now = now_utc()
    for ch, d in big.get("channels", {}).items():
        long = [v for v in d["videos"] if v["dur"] >= LONG_SEC and not v["live"]]
        if not long:
            continue
        share = sum(1 for v in long if c.strict.search(v["title"])) / len(long)     # 제목만
        if share < c.big_share or c.broadcast.search(d["title"] or ""):
            continue
        aged = [v for v in long if (now - parse_ts(v["published"])).days >= 14]
        m = med([v["views"] for v in aged]) or 1
        kept.append((d["title"], d["subs"], len(long), share, m))
        for v in aged:
            v2 = dict(v, rel=v["views"] / m, ch=d["title"], subs=d["subs"])
            allv.append(v2)
            for t in c.topics_of(v["title"]):
                by_topic[t].append(v2)
    kept.sort(key=lambda x: -x[1])
    lines += [f"{c.name} 큰 채널 {len(kept)}곳 (구독자 {c.big_min_subs // 10000}만+ · 최근 1년 롱폼 중 STRICT 낱말 제목 {c.big_share:.0%}+ · 방송사 클립 채널 뺌): " +
              " · ".join(f"{n} {fmt(s)}({k}편·{sh:.0%})" for n, s, k, sh, _ in kept), ""]
    lines += ["| 주제 | 다룬 큰 채널 수 | 영상 수 | 채널 안 상대 조회수 가운데값 | 채널 평소의 1.5배+ 몫 | 가장 잘 된 영상 (상대·조회수·채널) |", "|---|---|---|---|---|---|"]
    stats = {}
    for t, _ in c.topics:
        xs = by_topic.get(t, [])
        if not xs:
            lines.append(f"| {t} | 0 | 0 | — | — | — |")
            continue
        nch = len({x["ch"] for x in xs})
        mr = med([x["rel"] for x in xs])
        hi = sum(1 for x in xs if x["rel"] >= 1.5) / len(xs)
        best = max(xs, key=lambda x: x["rel"])
        stats[t] = {"channels": nch, "videos": len(xs), "rel_med": mr, "hi": hi}
        lines.append(f"| {t} | {nch} | {len(xs)} | {mr:.2f} | {hi:.0%} | 「{best['title'][:34]}」 {best['rel']:.1f}배 · {fmt(best['views'])} · {best['ch']} |")
    stamp("BIG_TABLE", channels_kept=len(kept), videos=len(allv))
    return lines, stats, allv


def cmd_report(c: Cfg, a) -> int:
    vids, chans, auto = load_cache(c)
    rel = related(c, vids)
    rec = load_gz(c, "recent.json.gz", {}) or {}
    big = load_gz(c, "big.json.gz", {}) or {}
    L = [f"# 다음 {c.name} 영상 주제 탐색 — 자료 (숫자·원문만)", "",
         f"> `tools/next_topic.py {c.topic}` {VERSION} · {time.strftime('%Y-%m-%d %H:%M')} · 네 단계 = 심리 세션 사용자 지시 2026-11-25 (1~4번 + 최근 7일 댓글 무게 + 겹침 확인) 그대로",
         f"> 자료: 지난 탐색 캐시 주제 관련 롱폼 {len(rel):,}개 · 최근 7일 댓글 {rec.get('asof', '없음')[:16]} · 큰 채널 업로드 {big.get('asof', '없음')[:16]}.",
         "> **한계**: 다른 채널의 클릭률·시청 지속률·트래픽 소스는 공개 API 에 없음 → 아래는 대리 지표(추정). 주제 묶음 = 제목 낱말 규칙(겹침 있음). 인과 아님. 연구·교육용.", ""]

    # 2번 — 최근 7일 댓글 무게
    rv, meta = rec.get("videos", {}), rec.get("meta", {})
    w_topic, n_topic, v_topic, cm_topic = defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(list)
    for vid, r in rv.items():
        m = meta.get(vid) or vids.get(vid) or {}
        for t in c.topics_of(m.get("title") or ""):        # 제목만
            if r["recent7"] > 0:
                w_topic[t] += r["recent7"]
                n_topic[t] += 1
                v_topic[t] += m.get("view_count") or 0
                cm_topic[t] += [dict(x, vid=vid) for x in r["comments"]]
    tot = sum(r["recent7"] for r in rv.values()) or 1
    L += [f"## 2. 많이 본 영상 + 지금도 보는지 — 조회수 상위 {len(rv)}개 중 최근 {RECENT_DAYS}일 댓글이 있는 {sum(1 for r in rv.values() if r['recent7'])}개 (무게 = 최근 7일 댓글 수, 합 {tot:,})", "",
          "| 주제 | 최근 7일 댓글 (무게) | 몫 | 영상 수 (7일 댓글 있음) | 그 영상 조회수 합 |", "|---|---|---|---|---|"]
    for t in sorted(w_topic, key=lambda t: -w_topic[t]):
        L.append(f"| {t} | {w_topic[t]:,} | {w_topic[t] / tot:.0%} | {n_topic[t]} | {fmt(v_topic[t])} |")
    L += ["", "### 2-1. 최근 7일 댓글이 많은 영상 (상위 25)", "", "| 최근 7일 댓글 | 조회수 | 올린 날 | 제목 | 채널 |", "|---|---|---|---|---|"]
    for vid, r in sorted(rv.items(), key=lambda kv: -kv[1]["recent7"])[:25]:
        m = meta.get(vid, {})
        L.append(f"| {r['recent7']}{'+' if r.get('capped') else ''} | {fmt(m.get('view_count') or 0)} | {(m.get('published') or '')[:10]} | {(m.get('title') or '')[:46]} | {m.get('channel', '')} |")
    ev_w, ev_n = defaultdict(int), defaultdict(int)
    for vid, r in rv.items():
        m = meta.get(vid) or {}
        if r["recent7"] and m.get("published") and (now_utc() - parse_ts(m["published"])).days >= 90:
            for t in c.topics_of(m.get("title") or ""):
                ev_w[t] += r["recent7"]
                ev_n[t] += 1
    L += ["", "### 2-1-1. 올린 지 90일 넘은 영상만 — 최근 7일 댓글 (새 영상 효과를 뺀 '지금도 찾아보는' 주제)", "",
          "| 주제 | 최근 7일 댓글 | 영상 수 |", "|---|---|---|"] + [f"| {t} | {ev_w[t]} | {ev_n[t]} |" for t in sorted(ev_w, key=lambda t: -ev_w[t])]
    L += ["", "### 2-2. 주제별 최근 7일 댓글 — 공감 많은 순 5개 (니즈 원문, 작성자 정보 없음)", ""]
    for t in sorted(w_topic, key=lambda t: -w_topic[t])[:16]:
        top = sorted(cm_topic[t], key=lambda x: -x["like"])[:5]
        L.append(f"- **{t}**: " + " / ".join(f"「{x['text'][:90]}」(♥{x['like']})" for x in top))
    stamp("REPORT", part="recent", topics=len(w_topic), weight_total=tot)

    # 3번 — 큰 채널
    bl, bstats, allbig = big_tables(c, big) if big else (["(big 을 먼저)"], {}, [])
    L += ["", f"## 3. 구독자 많은 {c.name} 채널이 많이 다루는 주제 — 최근 1년 롱폼 (상대 조회수 = 그 영상 조회수 ÷ 그 채널 롱폼 가운데값 — 채널 크기를 뺀 주제 힘)", ""] + bl

    # 4번 — 대리 지표 (같은 구독자 구간 안에서)
    by_band = defaultdict(list)
    for v in rel:
        if v.get("view_count") and v.get("subs"):
            by_band[band(v["subs"])].append(v)
    bmed = {b: (med([(x.get("like_count") or 0) / x["view_count"] for x in xs]), med([(x.get("comment_count") or 0) / x["view_count"] for x in xs]))
            for b, xs in by_band.items()}
    agg = defaultdict(lambda: {"n": 0, "like_i": [], "cmt_i": [], "reach": [], "succ": 0, "cmp": 0, "views": []})
    for v in rel:
        if not v.get("view_count") or not v.get("subs"):
            continue
        lm, cmm = bmed[band(v["subs"])]
        li = ((v.get("like_count") or 0) / v["view_count"]) / lm if lm else None
        ci = ((v.get("comment_count") or 0) / v["view_count"]) / cmm if cmm else None
        for t in c.topics_of(v["title"]):
            g = agg[t]
            g["n"] += 1
            g["like_i"].append(li)
            g["cmt_i"].append(ci)
            g["reach"].append(v["view_count"] / max(v["subs"], 100))
            g["views"].append(v["view_count"])
            if v["in_compare"]:
                g["cmp"] += 1
                g["succ"] += v["success"]
    L += ["", "## 4. 성공 대리 지표 — 지난 탐색 주제 관련 롱폼 (구독자 구간마다 가운데값으로 나눔 → 1 보다 크면 그 구간 평소보다 큼)", "",
          "구간 가운데값 (좋아요÷조회수 · 댓글÷조회수): " + " · ".join(f"{b} {bmed[b][0] * 100:.2f}% · {bmed[b][1] * 100:.3f}% ({len(by_band[b])}개)" for b in sorted(bmed)), "",
          "| 주제 | 영상 수 | 좋아요 지수 (끝까지 본 간접 지표) | 댓글 지수 (반응) | 조회수÷구독자 가운데값 (구독자 밖 추천 간접 지표) | 비교 집단 성공 비율 | 조회수 가운데값 |", "|---|---|---|---|---|---|---|"]
    proxy = {}
    for t, _ in c.topics:
        g = agg.get(t)
        if not g or g["n"] < 5:
            continue
        proxy[t] = {"like": med(g["like_i"]), "cmt": med(g["cmt_i"]), "reach": med(g["reach"]), "succ": (g["succ"] / g["cmp"]) if g["cmp"] else None, "n": g["n"]}
        p = proxy[t]
        succ = f"{p['succ']:.0%} ({g['succ']}/{g['cmp']})" if g["cmp"] else "—"
        L.append(f"| {t} | {g['n']} | {p['like']:.2f} | {p['cmt']:.2f} | {p['reach']:.2f} | {succ} | {fmt(med(g['views']))} |")

    # 5. 겹침 — 주제마다 가장 많이 본 영상 (캐시 + 큰 채널 업로드)
    pool = {v["id"]: (v["title"], v.get("view_count") or 0, v.get("channel", ""), (v.get("published") or "")[:10]) for v in rel}
    for v in allbig:
        pool.setdefault(v["id"], (v["title"], v["views"], v["ch"], v["published"][:10]))
    L += ["", "## 5. 겹침 확인 — 주제마다 가장 많이 본 영상 5개 (시청자가 이미 아는 내용 · 100만+ = ⚠)", ""]
    for t, rx in c.topic_rx:
        xs = sorted(((tt, vv, ch, pd) for tt, vv, ch, pd in pool.values() if rx.search(tt)), key=lambda x: -x[1])[:5]
        if xs:
            L.append(f"- **{t}**: " + " / ".join(f"{'⚠' if vv >= MEGA_VIEWS else ''}「{tt[:40]}」{fmt(vv)}·{ch}·{pd[:4]}" for tt, vv, ch, pd in xs))

    # 6. 유튜브 자동완성 (지난 탐색 캐시)
    L += ["", "## 6. 유튜브 자동완성 (지난 탐색 캐시 · 검색창에 사람들이 치는 말 — 관심도 보조)", ""]
    sug = []
    for seed, v in auto.items():
        try:
            s = v["s"] if isinstance(v, dict) else json.loads(v.replace("'", '"'))["s"]
        except (ValueError, KeyError, TypeError):
            s = re.findall(r"'([^']+)'", str(v))[:10]
        sug += s
        L.append(f"- {seed}: " + ", ".join(s[:10]))
    tcount = defaultdict(int)
    for s in sug:
        for t in c.topics_of(s):
            tcount[t] += 1
    L += ["", "자동완성 안 주제 낱말 수: " + " · ".join(f"{t} {n}" for t, n in sorted(tcount.items(), key=lambda x: -x[1]))]
    save_gz(c, "summary.json.gz", {"recent_w": w_topic, "big": bstats, "proxy": proxy, "auto": tcount, "asof": now_utc().isoformat(timespec="seconds")})
    (c.out / "next_topic_data.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    write_trend_batches(c)
    stamp("REPORT", status="done", out=(c.out / "next_topic_data.md").relative_to(ROOT), lines=len(L))
    return 0


# ─────────── 1. 관심 키워드 — 유튜브 자동완성 (실시간, 할당량 0) ───────────
def suggest(q: str) -> list[str]:
    url = SUGGEST + "?" + urllib.parse.urlencode({"client": "firefox", "ds": "yt", "hl": "ko", "gl": "kr", "q": q})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(url, timeout=20) as r:
                j = json.loads(r.read().decode("utf-8", "replace"))
                return [s for s in (j[1] if len(j) > 1 else []) if isinstance(s, str)]
        except (urllib.error.URLError, TimeoutError, ValueError) as e:
            if attempt < 2:
                time.sleep(2 + attempt * 3)
                continue
            stamp("SUGGEST", level="warn", q=q, error=type(e).__name__, next="suggestqueries.google.com 이 허용됐는지 (환경 네트워크) 확인")
    return []


def cmd_suggest(c: Cfg, a) -> int:
    """설정 [trends] WORDS (+ --q 로 더함) 마다 유튜브 자동완성 → 몇 개가 나오는지·무엇이 나오는지. 자동완성은 많이 친 말을 먼저 보여 줌 (값은 상대 — 검색 수 아님)."""
    words = list(dict.fromkeys(c.trend_words + (a.q or [])))
    if not words:
        stamp("SUGGEST", level="warn", msg="낱말 없음", next=f"{c.topic}/next_topic.toml [trends] WORDS 를 채우거나 --q 로")
        return 1
    res = {}
    for w in words:
        s = suggest(w)
        res[w] = s
        time.sleep(0.6)
    L = [f"# 유튜브 자동완성 — {c.name} 후보 낱말 (한국어·한국 · {time.strftime('%Y-%m-%d %H:%M')})", "",
         f"> `tools/next_topic.py {c.topic} suggest` {VERSION} · suggestqueries.google.com (ds=yt) — 검색창에 그 낱말을 치면 뜨는 말 (최대 10개).",
         "> 읽는 법: 자동완성이 0~2개면 그 말로 검색하는 사람이 드묾 · 뒤에 붙는 말(예 '…이유'·'…실제')이 시청자가 궁금해하는 각도. 검색 수 숫자가 아님 — 관심도 보조.", "",
         "| 낱말 | 자동완성 수 | 자동완성 (위에서부터) |", "|---|---|---|"]
    for w in words:
        L.append(f"| {w} | {len(res[w])} | {' · '.join(res[w][:10]) or '—'} |")
    c.out.mkdir(parents=True, exist_ok=True)
    (c.out / "suggest.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    save_gz(c, "suggest.json.gz", {"asof": now_utc().isoformat(timespec="seconds"), "words": res})
    stamp("SUGGEST", status="done", words=len(words), with_suggestions=sum(1 for w in words if res[w]), out=(c.out / "suggest.md").relative_to(ROOT))
    return 0


# ─────────── 겹침 — 후보마다 유튜브 검색 ───────────
def cmd_overlap(c: Cfg, a) -> int:
    if not c.cands:
        stamp("OVERLAP", level="warn", msg="후보 없음", next=f"{c.topic}/next_topic.toml [[overlap]] 을 채움")
        return 1
    api = Api()
    old = load_gz(c, "overlap.json.gz", {}) or {}
    res = old.get("queries", {})
    for key, name, qs, _core in c.cands:
        for q in qs:
            if q in res:
                continue
            j = api.get("search", part="snippet", q=q, type="video", regionCode="KR", relevanceLanguage="ko", maxResults=25)
            ids = [it["id"]["videoId"] for it in j.get("items", []) if it.get("id", {}).get("videoId")]
            vs = api.get("videos", part="snippet,statistics,contentDetails", id=",".join(ids), maxResults=50) if ids else {}
            res[q] = [{"id": it["id"], "title": it["snippet"]["title"], "ch": it["snippet"]["channelTitle"], "pub": it["snippet"]["publishedAt"][:10],
                       "views": int(it.get("statistics", {}).get("viewCount", 0) or 0), "dur": iso_dur(it["contentDetails"].get("duration", ""))}
                      for it in vs.get("items", [])]
            stamp("OVERLAP", cand=key, q=q, results=len(res[q]), top_views=max([x["views"] for x in res[q]] or [0]), units=api.units)
            save_gz(c, "overlap.json.gz", {"asof": now_utc().isoformat(timespec="seconds"), "queries": res})
    L = ["# 겹침 확인 — 후보마다 유튜브 검색 (한국 · 관련성 순 25개 중 제목에 핵심 낱말이 있는 것 = 같은 주제)", "",
         f"> `tools/next_topic.py {c.topic} overlap` {VERSION} · {time.strftime('%Y-%m-%d %H:%M')} · 100만+ = ⚠ (시청자가 이미 많이 본 내용 — 같은 각도면 피함). 검색 1회 = 100단위.", ""]
    summary = {}
    for key, name, qs, core in c.cands:
        allv = {}
        for q in qs:
            for x in res.get(q, []):
                allv[x["id"]] = x
        crx = re.compile(core)
        same = [x for x in allv.values() if crx.search(x["title"])]
        lng = sorted([x for x in same if x["dur"] > 180], key=lambda x: -x["views"])
        sht = sorted([x for x in same if x["dur"] <= 180], key=lambda x: -x["views"])
        summary[key] = {"name": name, "same": len(same), "long_max": lng[0]["views"] if lng else 0, "long_n_100k": sum(1 for x in lng if x["views"] >= 100_000),
                        "short_max": sht[0]["views"] if sht else 0, "long_top": lng[:3]}
        L.append(f"## {key}. {name} — 검색어: {' · '.join(qs)} · 핵심 낱말 `{core}` (검색 결과 {len(allv)}개 중 같은 주제 {len(same)}개)")
        L.append("- 롱폼: " + (" / ".join(f"{'⚠' if x['views'] >= MEGA_VIEWS else ''}「{x['title'][:48]}」 {fmt(x['views'])}·{x['ch']}·{x['pub'][:7]}" for x in lng[:5]) or "없음"))
        L.append("- 쇼츠: " + (" / ".join(f"{'⚠' if x['views'] >= MEGA_VIEWS else ''}「{x['title'][:40]}」 {fmt(x['views'])}·{x['ch']}" for x in sht[:3]) or "없음"))
        L.append("")
    save_gz(c, "overlap_summary.json.gz", summary)
    (c.out / "overlap.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    stamp("OVERLAP", status="done", queries=len(res), units=api.units)
    return 0


# ─────────── 1. 구글 트렌드 — 묶음 주소(사람이 받기) · 묶음 목록(PC tools/pc_trends.py) · CSV 합치기 ───────────
def trend_batches(c: Cfg) -> list[list[str]]:
    return [[c.trend_anchor] + c.trend_words[i:i + 4] for i in range(0, len(c.trend_words), 4)]


def write_trend_batches(c: Cfg) -> None:
    c.out.mkdir(parents=True, exist_ok=True)
    (c.out / "trends").mkdir(exist_ok=True)
    batches = trend_batches(c)
    L = [f"# 구글 트렌드 묶음 (유튜브 검색 · 한국 · 최근 12개월) — {c.name}", "",
         f"> `tools/next_topic.py {c.topic}` {VERSION} — 클라우드는 trends.google.com 이 막힘 (환경 허용 목록 밖이면 프록시 403 · 허용해도 구글이 서버 주소 자동 요청에 HTTP 429).",
         f"> 받는 방법 둘: ① PC 에서 `powershell -ExecutionPolicy Bypass -File run_analyzer.ps1 -Trends -Folder {c.topic}` (tools/pc_trends.py — 묶음을 차례로 받아 GitHub 에) "
         "② 아래 주소를 브라우저로 열기 → '시간 흐름에 따른 관심도' 오른쪽 위 ⤓(CSV) → 파일 이름을 `batch_NN.csv` 로 → "
         f"`{c.topic}/result/next_topic/trends/` 에 올리거나 채팅에 붙임.",
         f"> 한 번에 5개까지라 묶음마다 기준 낱말 「{c.trend_anchor}」를 넣고 4개씩 → 기준 낱말 값으로 묶음끼리 이어 붙인다 (`next_topic.py {c.topic} trends`).", ""]
    for i, words in enumerate(batches, 1):
        q = urllib.parse.quote(",".join(words))
        L.append(f"{i:02d}. {', '.join(words[1:])} — https://trends.google.com/trends/explore?date=today%2012-m&geo=KR&gprop=youtube&q={q}&hl=ko")
    (c.out / "trends_batches.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    (c.out / "trends_batches.json").write_text(json.dumps({"topic": c.topic, "anchor": c.trend_anchor, "geo": "KR", "gprop": "youtube",
                                                          "time": "today 12-m", "made": now_utc().isoformat(timespec="seconds"),
                                                          "batches": [{"n": i, "file": f"batch_{i:02d}.csv", "words": w} for i, w in enumerate(batches, 1)]},
                                                         ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    stamp("TREND_BATCHES", batches=len(batches), words=len(c.trend_words), anchor=c.trend_anchor)


def trend_val(x: str) -> float:
    """구글 트렌드 칸 값 — '<1' = 0.5 (1 보다 작음), 빈칸 = 0."""
    x = x.strip()
    if x.startswith("<"):
        return 0.5
    try:
        return float(x)
    except ValueError:
        return 0.0


def cmd_trends(c: Cfg, a) -> int:
    files = sorted((c.out / "trends").glob("batch_*.csv"))
    if not files:
        stamp("TRENDS", level="warn", msg="CSV 없음", next=f"trends_batches.md 의 주소에서 받거나 PC 에서 run_analyzer.ps1 -Trends -Folder {c.topic}")
        return 1
    anchor = c.trend_anchor
    score = {}
    for f in files:
        rows = [r for r in csv.reader(io.StringIO(f.read_text("utf-8-sig"))) if r]
        try:
            hdr_i = next(i for i, r in enumerate(rows) if len(r) > 1 and re.match(r"(주|Week|월|Month|날짜|Day|date)", r[0], re.I))
        except StopIteration:
            stamp("TRENDS", level="warn", file=f.name, msg="머리 줄(주,…) 없음 — 뺌")
            continue
        hdr = [re.sub(r":.*$", "", h).strip() for h in rows[hdr_i]]
        data = rows[hdr_i + 1:]
        cols = {h: [trend_val(r[j]) for r in data] for j, h in enumerate(hdr) if j}
        if anchor not in cols:
            stamp("TRENDS", level="warn", file=f.name, msg=f"기준 낱말 {anchor} 칸 없음 — 뺌")
            continue
        base = st.mean(cols[anchor]) or 1
        stamp("TRENDS", file=f.name, weeks=len(data), first=data[0][0], last=data[-1][0], anchor_mean=round(base, 1),
              words="·".join(h for h in cols if h != anchor))
        for h, xs in cols.items():
            if h == anchor:
                continue
            last = st.mean(xs[-13:]) if len(xs) >= 13 else st.mean(xs)
            prev = st.mean(xs[-26:-13]) if len(xs) >= 26 else last
            score[h] = {"rel": st.mean(xs) / base, "recent_rel": last / base, "trend": (last / prev) if prev else 0,
                        "last4": st.mean(xs[-4:]) / base, "peak": max(xs), "file": f.name, "low_anchor": base < 20}
    L = [f"# 구글 트렌드 — 유튜브 검색 관심도 (한국 · 최근 12개월 · 기준 「{anchor}」 = 1.00)", "",
         f"> `tools/next_topic.py {c.topic} trends` {VERSION} · {time.strftime('%Y-%m-%d %H:%M')} · CSV {len(files)}개 (`trends/batch_NN.csv`). 묶음마다 '{anchor}'를 같이 넣어 그 평균으로 나눔 → 묶음끼리 비교 가능.",
         f"> 값 = 그 낱말 평균 ÷ 같은 묶음 '{anchor}' 평균. 구글 트렌드는 0~100 상대값·정수라 기준 평균이 20 미만인 묶음(⚠)은 작은 낱말 값이 거칢. '<1' = 0.5.",
         "> **한계**: 정확히 그 낱말을 친 검색만 셈 — 긴 말은 검색이 적어도 주제 관심이 없다는 뜻은 아님 (홈 피드로 퍼지는 주제는 검색에 기대지 않음).", "",
         f"| 순위 | 낱말 | 12개월 평균 ({anchor} 대비) | 최근 3개월 | 최근 4주 | 최근 3개월 ÷ 그 전 3개월 | 최고값 (묶음 안 0~100) | 묶음 |", "|---|---|---|---|---|---|---|---|"]
    for i, (h, s_) in enumerate(sorted(score.items(), key=lambda kv: -kv[1]["rel"]), 1):
        L.append(f"| {i} | {h} | {s_['rel']:.2f} | {s_['recent_rel']:.2f} | {s_['last4']:.2f} | {s_['trend']:.2f} | {s_['peak']:.0f} | {s_['file']}{' ⚠' if s_['low_anchor'] else ''} |")
    (c.out / "trends.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    save_gz(c, "trends.json.gz", score)
    stamp("TRENDS", status="done", words=len(score), files=len(files))
    return 0


CMDS = {"recent": cmd_recent, "big": cmd_big, "report": cmd_report, "suggest": cmd_suggest, "overlap": cmd_overlap, "trends": cmd_trends,
        "batches": lambda c, a: (write_trend_batches(c), 0)[1]}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="다음 영상 주제 탐색 자료 (주제마다)")
    ap.add_argument("topic")
    ap.add_argument("cmd", choices=list(CMDS))
    ap.add_argument("--top", type=int, default=300, help="recent: 조회수 상위 몇 개 (기본 300)")
    ap.add_argument("--max-channels", type=int, default=0, help="big: 구독자 큰 순 몇 곳까지 (0 = 모두)")
    ap.add_argument("--q", action="append", help="suggest: 더 볼 낱말 (여러 번)")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args(argv)
    import topic_state                                       # v1.1 꺼 둔 주제는 읽지도 탐색하지도 않음
    topic_state.guard(a.topic, "next_topic.py")
    import topic_keys                                        # v1.2 주제 접두사 키 — 시작할 때 한 번
    topic_keys.apply(a.topic, say=print)
    logging.basicConfig(level=a.log_level, format="%(message)s")
    t0 = time.time()
    c = Cfg(a.topic)
    rc = CMDS[a.cmd](c, a)
    stamp("DONE", topic=a.topic, cmd=a.cmd, seconds=round(time.time() - t0, 1))
    return rc


if __name__ == "__main__":
    sys.exit(main())
