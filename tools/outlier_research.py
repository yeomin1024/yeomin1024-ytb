#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.2 — 2026-10-13 — PC 실행·이어서 돌리기 (사용자 지시: "분석기 코드 pc에서 돌릴 수 있도록", "api 할당량이 초기화된 시간이 되면
#          다시 자동으로 분석결과를 확인 못한 부분부터 새로 추가로"):
#          ① 검색어는 <주제>/keywords.toml 에서 (분석기 v2.4.0과 같은 파일, 없으면 analyzer_config.toml)
#          ② 검색 결과 캐시(.cache/search_*.json, 기본 7일) — 다시 돌리면 받은 검색은 할당량 0, 못 한 검색만 새로
#          ③ 할당량이 끝나도 멈추지 않고 캐시로 계속 → status.json 에 못 한 검색·영상 정보·댓글을 적음 (tools/pc_analysis.py 가 읽음)
#          ④ 사례 폴더에 이미 받은 자막(transcript.json)·썸네일·댓글이 있으면 다시 받지 않음
#          ⑤ summary.md 에 자막 첫 1분 발췌·구간별 흐름(90초마다 첫 문장 앞부분), Python 3.10(tomli) 지원
#          ⑥ 주제 이름을 설정의 [topic] TOPIC 에서 제대로 읽음, EXCLUDE_KEYWORDS 를 [keywords] 섹션에서도 읽음
#          ⑦ 영상 정보 캐시는 24시간·구독자 수는 7일 지나면 다시 받음 (조회수가 바뀌므로). 할당량이 없으면 예전 숫자로 계속
#          ⑧ 검색은 이번 실행 한도에서 150단위를 남기고 멈춤 → 남은 단위로 영상 정보·구독자·댓글은 계속 받음
# (v1.1 — 2026-10-12 — 기본 검색에 20분 넘는 영상도, 키워드는 그룹마다 1개(할당량 같게)
#  v1.0 — 2026-10-12 — 신규: 최근·작은 채널·조회수가 구독자의 몇 배인 롱폼 영상(작은 채널 성공 사례)의 내용(자막·설명·챕터)과 댓글)
r"""
사용법 (저장소 최상위, 또는 PC 실행 폴더):
  python tools/outlier_research.py economic                     # 주제 하나
  python tools/outlier_research.py economic --per-group 2 --top 20
  옵션: --per-group 1   검색어 그룹마다 검색할 검색어 수 (<주제>/keywords.toml 의 KEYWORD_GROUPS 앞에서부터)
        --days 180      최근 며칠 안에 올라온 영상 (모자라면 --fallback-days 365 까지 넓힘)
        --max-subs 50000 --min-ratio 3 --min-views 10000 --min-sec 240   성공 사례 기준
        --top 15        자막·댓글을 모을 성공 사례 수 (채널당 최대 --per-channel 2)
        --comments 100  사례마다 모을 댓글 수 (인기순)
        --no-long       20분 넘는 영상은 검색하지 않음 (기본은 4~20분과 20분 넘음 둘 다)
        --quota 9000    이번 실행 API 단위 한도 (하루 10,000 — 분석기와 같은 키면 나눠 쓴다)
        --search-ttl-hours 168   검색 결과 캐시 유효 시간 (이 안에 다시 돌리면 받은 검색은 할당량 0)
        --from-existing 분석기 결과에서 고르기 (API 키 없이)
        --refresh       캐시 무시 (검색·영상 정보·자막·썸네일·댓글 모두 새로)

수집 방법:
  YouTube Data API v3 (환경 변수 YOUTUBE_API_KEY, 없으면 이 폴더의 .env — 분석기와 같은 키):
    검색 search.list (최근 --fallback-days 일·조회수 순·4~20분·20분 넘음, KR·ko) — 100단위/번 · 영상 videos.list · 채널 channels.list
    · 댓글 commentThreads.list — 1단위/번. 검색 횟수 = 검색어 그룹 × --per-group × 2(길이 둘).
  할당량이 끝나면(이번 실행 한도 또는 하루 10,000): 새 요청을 멈추고 캐시에 있는 것만으로 결과를 만든다.
    못 한 검색·영상 정보·댓글은 status.json 의 pending 에 남는다 → 할당량이 초기화된 뒤 같은 명령을 다시 돌리면 그 부분만 새로 받는다.
    (태평양 자정 = 한국 시간 오후 4시(서머타임) / 5시. tools/pc_analysis.py 가 자동으로 기다렸다가 다시 돌린다)
  자막: youtube-transcript-api (한국어). 집 PC 에서는 받힌다. 클라우드는 네트워크 정책·YouTube 차단으로 못 받을 수 있다
        (2026-10-12: RequestBlocked / 2026-10-12 다른 환경: ProxyError 403). 못 받으면 status.json 에 적고 설명·챕터·댓글로 분석한다.
  yt-dlp 로 YouTube 페이지를 직접 읽는 방법은 쓰지 않는다 (봇 확인을 피해 가지 않는다).

결과 (<주제>/result/outliers/):
  candidates.csv  검색에서 걸린 롱폼 후보 전부 (구독자·조회수·배수·올린 날)                 ← git
  outliers.csv    기준을 통과한 성공 사례 (배수 순)                                        ← git
  summary.md      사례 표 + 사례마다 설명 앞부분·챕터·도입부·첫 1분·구간별 흐름·말 속도·인기 댓글 (짧게 인용) ← git
  status.json     이번 실행 상태: 검색 완료/남은 검색(pending)·할당량 멈춤·자막·썸네일·댓글 받은 수 (이어서 돌리기용)  ← git
  <순위>_<영상ID>/ metadata.json · description.txt · transcript.txt·transcript.json · comments.csv · thumbnail.jpg
                  ← 다른 사람의 글·이미지라 git 에 올리지 않는다 (.gitignore). 이 PC·세션의 분석에만 쓴다
  _old/           이번 상위에서 빠진 사례 폴더 (다시 들어오면 재사용, git 에 올리지 않음)
  .cache/         영상 정보·검색 결과 캐시 (git 에 올리지 않음)
로그: [STAGE] [시각] key=value (START·SEARCH·VIDEO·FILTER·DEEP·STATUS·DONE)
※ 연구·교육용. 다른 채널 영상을 내려받지 않는다(메타데이터·자막 글·댓글만).
"""
import argparse
import csv
import hashlib
import json
import logging
import os
import re
import shutil
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

try:
    import tomllib                      # Python 3.11+
except ModuleNotFoundError:             # Python 3.10 → tomli (분석기가 자동 설치)
    import tomli as tomllib

ROOT = Path(__file__).resolve().parent.parent
VERSION = "v1.2"
LOG = logging.getLogger("outlier")
HANGUL = re.compile(r"[가-힣]")
SEARCH_TTL_HOURS = 168
VIDEO_TTL_HOURS = 24          # 영상 조회수: 하루 지나면 다시 (videos.list 50개 = 1단위)
CHANNEL_TTL_HOURS = 168       # 구독자 수: 7일
SEARCH_RESERVE = 150          # 검색이 한도를 다 쓰지 않게 남기는 단위 (영상 정보·구독자·댓글용)
OUTLINE_EVERY_SEC = 90
NETWORK_ERRORS = ("RequestBlocked", "IpBlocked", "ProxyError", "ConnectionError", "Timeout", "TooManyRequests", "URLError")


def log(stage, level=logging.INFO, **kv):
    LOG.log(level, "[%s] [%s] %s", stage, datetime.now().isoformat(timespec="seconds"),
            " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) and ' ' in v else v}" for k, v in kv.items()))


def _flat(data):
    """TOML 섹션을 한 단계로 펼침 (KEYWORD_GROUPS 처럼 값이 표인 설정은 그대로) — 분석기 flatten_config 와 같은 규칙."""
    out = {}
    for k, v in data.items():
        if k == "KEYWORD_GROUPS" or not isinstance(v, dict):
            out[k] = v
        else:
            out.update(v)
    return out


def load_keywords(topic, per_group):
    """→ ([(그룹, 검색어)], 제외 낱말, 주제 이름, 검색어 파일 경로). 검색어는 keywords.toml(분석기 v2.4.0), 없으면 analyzer_config.toml."""
    cfg_p = ROOT / topic / "analyzer_config.toml"
    if not cfg_p.is_file():
        raise SystemExit(f"[START] ❌ {cfg_p} 없음 — 주제 폴더 확인")
    cfg = _flat(tomllib.loads(cfg_p.read_text("utf-8")))
    kw_name = str(cfg.get("KEYWORDS_FILE") or "keywords.toml")
    kw_p = Path(kw_name) if Path(kw_name).is_absolute() else cfg_p.parent / kw_name
    src = _flat(tomllib.loads(kw_p.read_text("utf-8"))) if kw_p.is_file() else cfg
    groups = src.get("KEYWORD_GROUPS") or cfg.get("KEYWORD_GROUPS") or {}
    kws = [(g, k) for g, ks in groups.items() for k in ks[:per_group]]
    exclude = [w for w in (src.get("EXCLUDE_KEYWORDS") or cfg.get("EXCLUDE_KEYWORDS") or []) if w]
    return kws, exclude, cfg.get("TOPIC", topic), (kw_p if kw_p.is_file() else cfg_p)


API = "https://www.googleapis.com/youtube/v3/"
COST = {"search": 100, "videos": 1, "channels": 1, "commentThreads": 1}


class QuotaStop(Exception):
    """kind: run_budget(이번 실행 한도 --quota) / daily(하루 할당량 소진)."""

    def __init__(self, msg, kind):
        super().__init__(msg)
        self.kind = kind


class Api:
    """YouTube Data API v3 (키는 환경 변수 YOUTUBE_API_KEY — 값은 로그에 쓰지 않음). 사용 단위를 세고 한도 전에 멈춘다.
    검색(100단위)은 한도에서 SEARCH_RESERVE 를 남기고 멈춘다 → 남은 단위로 영상 정보·구독자·댓글(1단위)은 계속 받는다.
    하루 할당량이 끝나면(daily) 같은 실행에서는 새 요청을 하지 않는다. stopped = 처음 멈춘 까닭."""

    def __init__(self, key, quota):
        self.key, self.quota, self.used, self.stopped = key, quota, 0, None

    def get(self, kind, **params):
        if self.stopped == "daily":
            raise QuotaStop("하루 할당량 소진 — 새 요청 안 함", "daily")
        limit = self.quota - (SEARCH_RESERVE if kind == "search" else 0)
        if self.used + COST[kind] > limit:
            self.stopped = self.stopped or "run_budget"
            raise QuotaStop(f"이번 실행 한도 {self.quota}단위 — 사용 {self.used}" + (f" (검색은 {SEARCH_RESERVE}단위 남김)" if kind == "search" else ""),
                            "run_budget")
        url = API + kind + "?" + urllib.parse.urlencode({**params, "key": self.key})
        for attempt in range(3):
            try:
                with urllib.request.urlopen(urllib.request.Request(url), timeout=30) as r:
                    self.used += COST[kind]
                    return json.loads(r.read().decode("utf-8"))
            except urllib.error.HTTPError as e:
                body = e.read().decode("utf-8", "replace")[:300]
                if e.code == 403 and ("quota" in body.lower()):
                    self.stopped = "daily"
                    raise QuotaStop("하루 할당량(10,000단위) 소진 — 태평양 자정(한국 오후 4~5시) 뒤 다시 (캐시는 남음)", "daily")
                if e.code in (403, 404) and kind == "commentThreads":   # 댓글 막힌 영상
                    return {"items": []}
                if attempt == 2 or e.code < 500:
                    raise RuntimeError(f"HTTP {e.code} {kind}: {body}")
            except urllib.error.URLError as e:
                if attempt == 2:
                    raise RuntimeError(f"{kind}: {e}")
            time.sleep(2 ** attempt)

    def search(self, q, published_after, duration):
        d = self.get("search", part="snippet", q=q, type="video", order="viewCount", publishedAfter=published_after,
                     videoDuration=duration, regionCode="KR", relevanceLanguage="ko", maxResults=50)
        return [it["id"]["videoId"] for it in d.get("items", []) if it.get("id", {}).get("videoId")]

    def videos(self, ids):
        return self.get("videos", part="snippet,contentDetails,statistics", id=",".join(ids)).get("items", [])

    def channels(self, ids):
        out = {}
        for it in self.get("channels", part="statistics", id=",".join(ids)).get("items", []):
            st = it.get("statistics", {})
            out[it["id"]] = None if st.get("hiddenSubscriberCount") else int(st.get("subscriberCount", 0))
        return out

    def comments(self, vid, n):
        d = self.get("commentThreads", part="snippet", videoId=vid, order="relevance", maxResults=min(n, 100), textFormat="plainText")
        out = []
        for it in d.get("items", []):
            c = it["snippet"]["topLevelComment"]["snippet"]
            out.append({"likes": c.get("likeCount", 0), "text": (c.get("textDisplay") or "").replace("\r", " "),
                        "replies": it["snippet"].get("totalReplyCount", 0), "published": c.get("publishedAt", "")[:10]})
        return out


def iso_seconds(iso):
    m = re.fullmatch(r"P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", iso or "")
    if not m:
        return 0
    d, h, mi, se = (int(x or 0) for x in m.groups())
    return d * 86400 + h * 3600 + mi * 60 + se


def transcript(vid):
    """→ (조각 목록 [{text,start,duration}], 언어, 상태). 한국어 자막 → 자동 생성 한국어."""
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
        api = YouTubeTranscriptApi()
        tl = api.list(vid)
        tr = None
        for finder in (tl.find_manually_created_transcript, tl.find_generated_transcript):
            try:
                tr = finder(["ko"])
                break
            except Exception:
                continue
        if tr is None:
            return [], "-", "한국어 자막 없음"
        snips = [{"text": s.text, "start": s.start, "duration": s.duration} for s in tr.fetch()]
        return snips, tr.language_code + ("(자동)" if tr.is_generated else ""), "ok"
    except Exception as e:
        return [], "-", f"{type(e).__name__}: {str(e)[:120]}"


def is_network_failure(status):
    """자막 실패가 네트워크·차단 때문인가 (다른 곳·다른 날 다시 하면 받을 수 있음) — '한국어 자막 없음'은 아님."""
    return any(w in str(status) for w in NETWORK_ERRORS)


def speech_stats(snips):
    """자막으로 말 속도(한글 음절/초 — 말하는 구간 기준), 도입부(첫 20초), 첫 1분 발췌, 구간별 흐름(90초마다 첫 문장 앞부분)."""
    if not snips:
        return {}
    syl = sum(len(HANGUL.findall(s["text"])) for s in snips)
    span = max(1e-6, snips[-1]["start"] + snips[-1]["duration"] - snips[0]["start"])
    hook = " ".join(s["text"] for s in snips if s["start"] < 20).replace("\n", " ")
    first60 = " ".join(s["text"] for s in snips if s["start"] < 60).replace("\n", " ")
    outline, next_t = [], 0.0
    for s in snips:
        if s["start"] >= next_t:
            outline.append({"t": int(s["start"]), "text": short(s["text"], 45)})
            next_t = (int(s["start"]) // OUTLINE_EVERY_SEC + 1) * OUTLINE_EVERY_SEC
    return {"syl": syl, "syl_per_sec": round(syl / span, 2), "hook20": hook[:300], "first60": first60[:400],
            "first60_syl": len(HANGUL.findall(first60)), "outline": outline[:20]}


def cached_search(api, cache_dir, q, since, dur, fallback_days, ttl_h, refresh):
    """검색 캐시: (검색어, 길이, 기간) 이 같고 ttl_h 안이면 할당량 0. → (영상 ID 목록, 캐시 여부). 할당량이 없으면 QuotaStop."""
    key = hashlib.sha1(f"{q}|{dur}|{fallback_days}|viewCount|KR|ko".encode("utf-8")).hexdigest()[:16]
    f = cache_dir / f"search_{key}.json"
    if f.is_file() and not refresh:
        try:
            d = json.loads(f.read_text("utf-8"))
            age_h = (datetime.now(timezone.utc) - datetime.fromisoformat(d["fetched"])).total_seconds() / 3600
            if age_h <= ttl_h:
                return d["ids"], True
        except (ValueError, KeyError):
            pass
    ids = api.search(q, since, dur)
    f.write_text(json.dumps({"q": q, "dur": dur, "fallback_days": fallback_days, "fetched": datetime.now(timezone.utc).isoformat(),
                             "ids": ids}, ensure_ascii=False), "utf-8")
    return ids, False


def collect_api(topic, a, api, kws, exclude, out, state):
    """검색(최근·조회수 순) → 영상·채널 정보 → 후보 행 목록. 캐시: out/.cache/. 할당량이 끝나면 캐시만으로 계속하고 state 에 남김."""
    cache_dir = out / ".cache"
    since = (datetime.now(timezone.utc) - timedelta(days=a.fallback_days)).strftime("%Y-%m-%dT00:00:00Z")
    found = {}
    for g, q in kws:
        for dur in (("medium", "long") if a.long else ("medium",)):
            try:
                ids, hit = cached_search(api, cache_dir, q, since, dur, a.fallback_days, a.search_ttl_hours, a.refresh)
            except QuotaStop as e:
                state["quota_stop"] = state["quota_stop"] or e.kind
                state["pending_searches"].append(f"{q} ({dur})")
                continue
            state["searched" if not hit else "search_cached"] += 1
            for vid in ids:
                found.setdefault(vid, []).append(q)
            log("SEARCH", query=q, group=g, dur=dur, results=len(ids), cached=hit, quota_used=api.used)
    if state["pending_searches"]:
        log("SEARCH", logging.WARNING, topic=topic, note="할당량이 끝나 못 한 검색 — status.json pending, 다음 실행에 이어서",
            pending=len(state["pending_searches"]), stop=state["quota_stop"])
    def fresh(path, ttl_h):
        """캐시 파일이 ttl_h 시간 안에 받은 것인가 (조회수·구독자 수는 바뀌므로 오래된 것은 다시 — 50개에 1단위)."""
        if a.refresh or not path.is_file():
            return False
        try:
            t = datetime.fromisoformat(json.loads(path.read_text("utf-8")).get("fetched", "2000-01-01T00:00:00+00:00"))
        except (ValueError, AttributeError):
            return False
        return (datetime.now(timezone.utc) - t).total_seconds() / 3600 <= ttl_h

    need = [v for v in found if not fresh(cache_dir / f"{v}.json", VIDEO_TTL_HOURS)]
    missing = sum(1 for v in need if not (cache_dir / f"{v}.json").is_file())
    log("VIDEO", topic=topic, found=len(found), refresh=len(need), new=missing, ttl_h=VIDEO_TTL_HOURS)
    for i in range(0, len(need), 50):
        chunk = need[i:i + 50]
        try:
            items = api.videos(chunk)
        except QuotaStop as e:
            state["quota_stop"] = state["quota_stop"] or e.kind
            left = need[i:]
            state["pending_videos"] += sum(1 for v in left if not (cache_dir / f"{v}.json").is_file())   # 없는 것만 '못 함'
            state["stale_videos"] += sum(1 for v in left if (cache_dir / f"{v}.json").is_file())        # 예전 숫자로 계속
            log("VIDEO", logging.WARNING, note="할당량이 끝나 영상 정보 못 받음 — 다음 실행에 이어서 (있던 캐시는 예전 숫자로 씀)",
                pending=state["pending_videos"], stale=state["stale_videos"])
            break
        for it in items:
            sn, cd, st = it["snippet"], it["contentDetails"], it.get("statistics", {})
            info = {"id": it["id"], "title": sn.get("title"), "channel": sn.get("channelTitle"), "channel_id": sn.get("channelId"),
                    "published": sn.get("publishedAt"), "description": sn.get("description"), "tags": sn.get("tags"),
                    "duration": iso_seconds(cd.get("duration")), "live": sn.get("liveBroadcastContent") != "none",
                    "view_count": int(st.get("viewCount", 0)), "like_count": int(st.get("likeCount", 0) or 0),
                    "comment_count": int(st.get("commentCount", 0) or 0), "fetched": datetime.now(timezone.utc).isoformat()}
            (cache_dir / f"{it['id']}.json").write_text(json.dumps(info, ensure_ascii=False), "utf-8")
    infos = [json.loads((cache_dir / f"{v}.json").read_text("utf-8")) for v in found if (cache_dir / f"{v}.json").is_file()]
    subs_cache_p = cache_dir / "channels.json"     # {채널ID: {"subs": n|null, "fetched": 시각}}
    subs_cache = json.loads(subs_cache_p.read_text("utf-8")) if subs_cache_p.is_file() and not a.refresh else {}
    subs_cache = {k: v for k, v in subs_cache.items() if isinstance(v, dict)}       # v1.1 이전 형식(숫자만)은 다시 받음
    now = datetime.now(timezone.utc)

    def ch_fresh(cid):
        v = subs_cache.get(cid)
        try:
            return bool(v) and (now - datetime.fromisoformat(v["fetched"])).total_seconds() / 3600 <= CHANNEL_TTL_HOURS
        except (ValueError, KeyError, TypeError):
            return False
    ch_need = sorted({i["channel_id"] for i in infos if not ch_fresh(i["channel_id"])})
    for i in range(0, len(ch_need), 50):
        try:
            got = api.channels(ch_need[i:i + 50])
        except QuotaStop as e:
            state["quota_stop"] = state["quota_stop"] or e.kind
            state["pending_channels"] += sum(1 for c in ch_need[i:] if c not in subs_cache)
            log("VIDEO", logging.WARNING, note="할당량이 끝나 채널 구독자 수 못 받음 — 다음 실행에 이어서",
                pending=state["pending_channels"])
            break
        stamp = datetime.now(timezone.utc).isoformat()
        subs_cache.update({cid: {"subs": n, "fetched": stamp} for cid, n in got.items()})
    subs_cache_p.write_text(json.dumps(subs_cache, ensure_ascii=False), "utf-8")
    rows = []
    for i in infos:
        if any(w in (i["title"] or "") for w in exclude):
            continue
        i["subs"] = (subs_cache.get(i["channel_id"]) or {}).get("subs")
        rows.append(i)
    return rows, found


def collect_existing(topic):
    """분석기 결과(videos.csv)를 같은 모양으로. 설명은 없고, 댓글은 audience_comments.csv 에 있는 영상만."""
    import pandas as pd
    v = pd.read_csv(ROOT / topic / "result" / "data" / "videos.csv")
    rows = []
    for _, r in v.iterrows():
        rows.append({"id": r["video_id"], "title": r["title"], "channel": r["channel_title"], "channel_id": r["channel_id"],
                     "published": str(r["published_at"]), "description": "", "tags": r.get("tags"),
                     "duration": int(r["duration_sec"] or 0) if r["duration_sec"] == r["duration_sec"] else 0, "live": False,
                     "view_count": int(r["views"]), "like_count": int(r["likes"]) if r["likes"] == r["likes"] else 0,
                     "comment_count": int(r["comments"]) if r["comments"] == r["comments"] else 0,
                     "subs": int(r["subscribers"]) if r["subscribers"] == r["subscribers"] else None})
    c = pd.read_csv(ROOT / topic / "result" / "data" / "audience_comments.csv")
    cm = {vid: [{"likes": int(x.likes or 0), "text": str(x.comment), "replies": int(x.replies or 0), "published": str(x.published_at)[:10]}
                for x in g.itertuples()] for vid, g in c.groupby("video_id")}
    return rows, cm


def _read_comments(path):
    if not path.is_file():
        return None
    with open(path, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def deep_case(d, r, info, a, api, source, existing_comments, state):
    """사례 하나: 설명·댓글·자막·썸네일. 이미 받은 것은 다시 받지 않음(--refresh 면 다시). → (meta, comments)."""
    d.mkdir(parents=True, exist_ok=True)
    (d / "description.txt").write_text(info.get("description") or "", "utf-8")
    # 댓글
    cms = None if a.refresh else _read_comments(d / "comments.csv")
    if cms:
        state["comments_reused"] += 1
    elif source == "existing":
        cms = existing_comments.get(r["id"], [])
    else:
        try:
            cms = api.comments(r["id"], a.comments)
        except QuotaStop as e:
            state["quota_stop"] = state["quota_stop"] or e.kind
            state["pending_comments"].append(r["id"])
            cms = []
        except RuntimeError as e:
            cms = []
            log("DEEP", logging.WARNING, id=r["id"], step="comments", error=str(e)[:150])
        with open(d / "comments.csv", "w", newline="", encoding="utf-8-sig") as f:
            w = csv.DictWriter(f, fieldnames=["likes", "text", "replies", "published"])
            w.writeheader()
            w.writerows(cms)
    # 자막
    tj = d / "transcript.json"
    if tj.is_file() and not a.refresh:
        saved = json.loads(tj.read_text("utf-8"))
        snips, lang, st = saved["snippets"], saved["lang"], "ok"
        state["transcripts_reused"] += 1
    elif a.no_transcript:
        snips, lang, st = [], "-", "건너뜀(--no-transcript)"
    else:
        snips, lang, st = transcript(r["id"])
        if snips:
            tj.write_text(json.dumps({"lang": lang, "snippets": snips}, ensure_ascii=False), "utf-8")
            (d / "transcript.txt").write_text("\n".join(f"[{x['start']:7.1f}] {x['text']}" for x in snips), "utf-8")
    if not snips:
        state["transcript_missing"].append({"id": r["id"], "status": st, "retry_elsewhere": is_network_failure(st)})
    # 썸네일
    th = d / "thumbnail.jpg"
    if not (th.is_file() and th.stat().st_size > 0) or a.refresh:
        try:
            req = urllib.request.Request(f"https://i.ytimg.com/vi/{r['id']}/hqdefault.jpg", headers={"User-Agent": "Mozilla/5.0"})
            th.write_bytes(urllib.request.urlopen(req, timeout=20).read())
        except Exception as e:
            state["thumbnail_missing"].append(r["id"])
            log("DEEP", logging.WARNING, id=r["id"], step="thumbnail", error=str(e)[:100])
    stats = speech_stats(snips)
    meta = {**r, "source": source, "tags": info.get("tags"), "chapters": chapters_from(info.get("description") or ""),
            "transcript_lang": lang, "transcript_status": st, **stats, "comments_fetched": len(cms),
            "tool": f"outlier_research.py {VERSION}", "collected": datetime.now().isoformat(timespec="seconds")}
    (d / "metadata.json").write_text(json.dumps(meta, ensure_ascii=False, indent=1), "utf-8")
    return meta, cms


def new_state():
    return {"quota_stop": None, "searched": 0, "search_cached": 0, "pending_searches": [], "pending_videos": 0,
            "pending_channels": 0, "pending_comments": [], "stale_videos": 0, "transcript_missing": [], "thumbnail_missing": [],
            "transcripts_reused": 0, "comments_reused": 0}


def write_status(out, topic, a, api, state, rows, q, deep, kw_file):
    """이어서 돌리기용 상태 (tools/pc_analysis.py 가 읽음). complete = 할당량 때문에 못 한 일이 없음."""
    pending = bool(state["pending_searches"] or state["pending_videos"] or state["pending_channels"] or state["pending_comments"])
    st = {"tool": f"outlier_research.py {VERSION}", "updated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
          "topic": topic, "keywords_file": str(kw_file.relative_to(ROOT)) if kw_file.is_relative_to(ROOT) else kw_file.name,
          "per_group": a.per_group, "top": a.top, "quota_used": api.used if api else 0, "quota_stop": state["quota_stop"],
          "searches_new": state["searched"], "searches_cached": state["search_cached"],
          "pending": {"searches": state["pending_searches"], "videos": state["pending_videos"], "channels": state["pending_channels"],
                      "comments": state["pending_comments"]}, "stale_videos": state["stale_videos"],
          "candidates": len(rows), "qualified": len(q), "deep": len(deep),
          "transcripts_ok": len(deep) - len(state["transcript_missing"]), "transcript_missing": state["transcript_missing"],
          "thumbnails_ok": len(deep) - len(state["thumbnail_missing"]), "thumbnail_missing": state["thumbnail_missing"],
          "complete": not pending,
          "next": ("완료" if not pending else "할당량이 초기화된 뒤(태평양 자정 = 한국 오후 4시·겨울 5시) 같은 명령을 다시 — 받은 것은 캐시, 남은 것만 새로")}
    (out / "status.json").write_text(json.dumps(st, ensure_ascii=False, indent=1), "utf-8")
    log("STATUS", topic=topic, complete=st["complete"], quota_stop=state["quota_stop"] or "-", pending_searches=len(state["pending_searches"]),
        pending_videos=state["pending_videos"], pending_comments=len(state["pending_comments"]),
        transcripts=f"{st['transcripts_ok']}/{len(deep)}", thumbnails=f"{st['thumbnails_ok']}/{len(deep)}")
    return st


def run_topic(topic, a, api):
    t0 = time.time()
    out = ROOT / topic / "result" / "outliers"
    (out / ".cache").mkdir(parents=True, exist_ok=True)
    kws, exclude, topic_name, kw_file = load_keywords(topic, a.per_group)
    source = "existing" if a.from_existing else "api"
    state = new_state()
    log("START", topic=topic, name=topic_name, source=source, keywords=len(kws), keywords_file=kw_file.name, per_group=a.per_group,
        days=a.days, max_subs=a.max_subs, min_ratio=a.min_ratio, min_views=a.min_views, min_sec=a.min_sec, quota=a.quota,
        tool=f"outlier_research.py {VERSION}")
    now = datetime.now(timezone.utc)
    existing_comments = {}
    if a.from_existing:
        infos, existing_comments = collect_existing(topic)
        found = {}
    else:
        infos, found = collect_api(topic, a, api, kws, exclude, out, state)
    rows = []
    for i in infos:
        if i.get("live") or not i.get("duration"):
            continue
        try:
            pub = datetime.fromisoformat(str(i["published"]).replace("Z", "+00:00"))
            pub = pub if pub.tzinfo else pub.replace(tzinfo=timezone.utc)
            age = (now - pub).days
        except Exception:
            age = None
        subs, views = i.get("subs"), i.get("view_count") or 0
        ratio = round(views / max(subs, 100), 2) if subs else None
        rows.append({"id": i["id"], "title": i["title"], "channel": i["channel"], "channel_id": i["channel_id"], "subs": subs,
                     "views": views, "ratio": ratio, "age_days": age, "views_per_day": round(views / max(age or 1, 1), 1),
                     "minutes": round(i["duration"] / 60, 1), "likes": i.get("like_count"), "comments": i.get("comment_count"),
                     "published": str(i["published"])[:10], "queries": " | ".join(dict.fromkeys(found.get(i["id"], []))),
                     "url": f"https://www.youtube.com/watch?v={i['id']}"})
    fields = list(rows[0].keys()) if rows else ["id"]
    with open(out / "candidates.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(sorted(rows, key=lambda r: -(r["ratio"] or 0)))

    def qualify(days):
        qq = [r for r in rows if r["subs"] and r["subs"] <= a.max_subs and r["ratio"] and r["ratio"] >= a.min_ratio
              and r["views"] >= a.min_views and r["age_days"] is not None and r["age_days"] <= days and r["minutes"] * 60 >= a.min_sec]
        return sorted(qq, key=lambda r: -r["ratio"])
    used_days, q = a.days, qualify(a.days)
    for wider in (a.fallback_days, 730):
        if len(q) >= a.top or used_days >= wider:
            continue
        used_days, q = wider, qualify(wider)
        log("FILTER", logging.WARNING, topic=topic, note=f"최근 사례가 {a.top}개보다 적어 {wider}일로 넓힘", qualified=len(q))
    per_ch, top = {}, []
    for r in q:
        if per_ch.get(r["channel_id"], 0) >= a.per_channel:
            continue
        per_ch[r["channel_id"]] = per_ch.get(r["channel_id"], 0) + 1
        top.append(r)
    top = top[:a.top]
    log("FILTER", topic=topic, candidates=len(rows), qualified=len(q), days=used_days, chosen=len(top),
        ratios=",".join(str(r["ratio"]) for r in top))
    with open(out / "outliers.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=fields + ["rank"])
        w.writeheader()
        for k, r in enumerate(q, 1):
            w.writerow({**r, "rank": k})
    deep = []
    old_dir = out / "_old"       # 이번 상위에서 빠진 사례 폴더 (다시 들어오면 받은 자막·댓글 재사용). git 에 올리지 않음
    for k, r in enumerate(top, 1):
        old = [p for base in (out, old_dir) for p in base.glob(f"[0-9][0-9]_{r['id']}") if p.is_dir()]  # 순위가 바뀌면 폴더 이름만 바꿈
        d = out / f"{k:02d}_{r['id']}"
        if old and old[0] != d and not d.exists():
            old[0].rename(d)
        info = next(i for i in infos if i["id"] == r["id"])
        meta, cms = deep_case(d, {**r, "rank": k}, info, a, api, source, existing_comments, state)
        deep.append((meta, info, cms))
        log("DEEP", topic=topic, rank=k, id=r["id"], subs=r["subs"], views=r["views"], ratio=r["ratio"], age=r["age_days"],
            minutes=r["minutes"], transcript=meta["transcript_status"] if meta["transcript_status"] != "ok" else meta["transcript_lang"],
            comments=len(cms))
    keep = {f"{k:02d}_{r['id']}" for k, r in enumerate(top, 1)}
    moved = 0
    for p in out.glob("[0-9][0-9]_*"):
        if p.is_dir() and p.name not in keep:
            old_dir.mkdir(exist_ok=True)
            dst = old_dir / p.name
            if dst.exists():
                shutil.rmtree(dst)
            p.rename(dst)
            moved += 1
    if moved:
        log("DEEP", topic=topic, note="이번 상위에서 빠진 사례 폴더를 _old/ 로 옮김", moved=moved)
    write_summary(out, topic, topic_name, a, used_days, rows, q, deep, source)
    st = write_status(out, topic, a, api, state, rows, q, deep, kw_file)
    log("DONE", topic=topic, source=source, candidates=len(rows), qualified=len(q), deep=len(deep), complete=st["complete"],
        quota_used=api.used if api else 0, minutes=round((time.time() - t0) / 60, 1), out=str(out.relative_to(ROOT)))
    return st


def chapters_from(desc):
    """설명란의 '0:00 제목' 줄 → 챕터 목록 (YouTube 챕터 규칙과 같은 모양)."""
    out = []
    for ln in desc.splitlines():
        m = re.match(r"\s*\(?((?:\d+:)?\d{1,2}:\d{2})\)?\s*[-–—|:]?\s*(.+)", ln)
        if m:
            parts = [int(x) for x in m.group(1).split(":")]
            sec = parts[-1] + 60 * parts[-2] + (3600 * parts[0] if len(parts) == 3 else 0)
            out.append({"start": sec, "title": m.group(2).strip()})
    return out if len(out) >= 3 and out[0]["start"] == 0 else []


def short(s, n):
    s = re.sub(r"\s+", " ", str(s or "")).strip()
    return s if len(s) <= n else s[: n - 1] + "…"


def write_summary(out, topic, name, a, used_days, rows, q, deep, source):
    L = [f"# {name} — 작은 채널 성공 사례 (최근·롱폼·조회수가 구독자의 몇 배)", "",
         f"자동 생성 — `tools/outlier_research.py` {VERSION} ({datetime.now().strftime('%Y-%m-%d %H:%M')}). "
         "다른 채널의 자막·댓글 원문·썸네일은 git 에 올리지 않고(각 사례 폴더, .gitignore), 여기에는 짧게만 인용한다. "
         "진행 상태(못 한 검색·자막·썸네일)는 `status.json`.", "",
         f"- 기준: 최근 {used_days}일 안 · 구독자 {a.max_subs:,}명 이하 · 조회수 ≥ 구독자 × {a.min_ratio} · 조회수 {a.min_views:,} 이상 · "
         f"{a.min_sec // 60}분 이상 (쇼츠 제외) · 채널당 {a.per_channel}개까지",
         (f"- 후보 {len(rows)}개 — 자료: YouTube Data API 검색(검색어 그룹마다 {a.per_group}개, 최근 {a.fallback_days}일·조회수 순·4~20분"
          + (", 20분 넘음" if a.long else "") + ")" if source == "api" else
          f"- 후보 {len(rows)}개 — 자료: 분석기 결과 `result/data/videos.csv` (⚠️ 분석기 검색은 최근 영상만 찾지 않았다)")
         + f" → 기준 통과 {len(q)}개 → 자세히 {len(deep)}개", "",
         "| # | 제목 | 채널 | 구독자 | 조회수 | 배수 | 며칠 전 | 길이(분) | 말 속도(음절/초) | 댓글 |", "|---|---|---|---|---|---|---|---|---|---|"]
    for meta, info, cms in deep:
        L.append(f"| {meta['rank']} | [{short(meta['title'], 60)}]({meta['url']}) | {short(meta['channel'], 20)} | {meta['subs']:,} | {meta['views']:,} | "
                 f"{meta['ratio']} | {meta['age_days']} | {meta['minutes']} | {meta.get('syl_per_sec', '-')} | {meta.get('comments') or 0} |")
    L += [""]
    for meta, info, cms in deep:
        L += [f"## {meta['rank']}. {short(meta['title'], 90)}", "",
              f"- {meta['url']} · {meta['channel']} · 구독자 {meta['subs']:,} · 조회수 {meta['views']:,} (×{meta['ratio']}) · "
              f"{meta['published']} ({meta['age_days']}일 전) · {meta['minutes']}분" + (f" · 검색어: {meta['queries']}" if meta['queries'] else ""),
              f"- 설명 앞부분: {short(info.get('description'), 300) or '(이 자료에는 설명 없음)'}"]
        if meta.get("chapters"):
            L.append("- 챕터: " + " / ".join(f"{int(c['start'] // 60)}:{int(c['start'] % 60):02d} {short(c['title'], 30)}"
                                           for c in meta["chapters"][:15]))
        if meta.get("hook20"):
            L.append(f"- 도입부(첫 20초, 자막 {meta['transcript_lang']}): {short(meta['hook20'], 220)}")
            L.append(f"- 첫 1분 발췌: {short(meta.get('first60'), 300)}")
            L.append(f"- 말 속도 {meta['syl_per_sec']}음절/초 · 첫 1분 {meta['first60_syl']}음절 · 전체 {meta.get('syl', 0):,}음절")
            if meta.get("outline"):
                L.append(f"- 구간별 흐름({OUTLINE_EVERY_SEC}초마다 첫 문장 앞부분): "
                         + " / ".join(f"{o['t'] // 60}:{o['t'] % 60:02d} {o['text']}" for o in meta["outline"]))
        else:
            L.append(f"- 자막: {meta['transcript_status']}")
        top = sorted(cms, key=lambda c: -int(c.get("likes") or 0))[:10]
        if top:
            L.append(f"- 인기 댓글 {len(cms)}개 중 상위 10 (좋아요):")
            L += [f"  - ({c.get('likes')}) {short(c.get('text'), 140)}" for c in top]
        L.append("")
    (out / "summary.md").write_text("\n".join(L), "utf-8")


def load_api_key():
    key = os.environ.get("YOUTUBE_API_KEY", "").strip()
    env_p = ROOT / ".env"     # 집 PC: 분석기와 같은 .env (git 에 올라가지 않음). 값은 출력하지 않는다
    if not key and env_p.is_file():
        m = re.search(r"^\s*YOUTUBE_API_KEY\s*=\s*['\"]?([^'\"\s]+)", env_p.read_text("utf-8"), re.M)
        key = m.group(1) if m else ""
    return key


def main(argv=None):
    ap = argparse.ArgumentParser(description="작은 채널 성공 사례(최근·롱폼·조회수/구독자 배수) 수집 — 내용·댓글 분석용, 이어서 돌리기 지원")
    ap.add_argument("topics", nargs="+")
    ap.add_argument("--per-group", type=int, default=1)
    ap.add_argument("--days", type=int, default=180)
    ap.add_argument("--fallback-days", type=int, default=365)
    ap.add_argument("--max-subs", type=int, default=50000)
    ap.add_argument("--min-ratio", type=float, default=3.0)
    ap.add_argument("--min-views", type=int, default=10000)
    ap.add_argument("--min-sec", type=int, default=240)
    ap.add_argument("--top", type=int, default=15)
    ap.add_argument("--per-channel", type=int, default=2)
    ap.add_argument("--comments", type=int, default=100)
    ap.add_argument("--no-long", dest="long", action="store_false", help="20분 넘는 영상은 검색하지 않음")
    ap.add_argument("--quota", type=int, default=9000, help="이번 실행 API 단위 한도 (주제 여러 개를 함께 셈. 하루 10,000)")
    ap.add_argument("--search-ttl-hours", type=float, default=SEARCH_TTL_HOURS, help="검색 캐시 유효 시간 (기본 168 = 7일)")
    ap.add_argument("--from-existing", action="store_true", help="분석기 결과에서 고르기 (API 키 없이)")
    ap.add_argument("--no-transcript", action="store_true", help="자막 받기 건너뜀")
    ap.add_argument("--refresh", action="store_true", help="캐시·이미 받은 자막·썸네일·댓글을 무시하고 새로")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args(argv)
    logging.basicConfig(level=getattr(logging, a.log_level), format="%(message)s", stream=sys.stdout)
    api = None
    if not a.from_existing:
        key = load_api_key()
        if not key:
            raise SystemExit("[START] ❌ YOUTUBE_API_KEY 가 없음 → 이 폴더의 .env 에 YOUTUBE_API_KEY=... (PC) 또는 클라우드 환경 변수 "
                             "(키 없이 기존 자료로만: --from-existing)")
        api = Api(key, a.quota)
    statuses = {}
    for t in a.topics:
        try:
            statuses[t] = run_topic(t, a, api)
        except SystemExit:
            raise
        except Exception as e:   # 한 주제가 실패해도 다음 주제
            log("DONE", logging.ERROR, topic=t, error=f"{type(e).__name__}: {str(e)[:200]}", hint="잠시 뒤 다시 (캐시는 남음)")
            statuses[t] = {"complete": False, "error": f"{type(e).__name__}: {str(e)[:200]}"}
    return 0 if all(s.get("complete") for s in statuses.values()) else 3   # 3 = 못 한 일이 남음 (할당량·오류) → 다시 돌리면 이어서


if __name__ == "__main__":
    sys.exit(main())
