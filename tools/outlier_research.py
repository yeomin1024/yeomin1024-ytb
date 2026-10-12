#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-12 — 신규: 최근에 올라온, 구독자는 적은데 조회수가 구독자의 몇 배인 롱폼 영상(작은 채널 성공 사례)을
#          주제마다 찾아 내용(자막·설명·챕터)과 댓글을 모은다. 사용자 지시: "되도록 최근에 업로드 되고 구독자수 별로 없지만 그에 비해
#          조회수가 잘나오는 영상들에서 어떤 내용이 들어있고 댓글에서 시청자의 니즈가 뭔지" — 분석기(youtube_topic_analyzer.py)의
#          성공 사례 8개는 쇼츠·대형 채널이 섞이고(조회수 가중 35%), 주식 밖 주제는 자막을 못 받아 주식 결과를 빌려 썼던 문제를 고친다.
r"""
사용법 (저장소 최상위):
  python3 tools/outlier_research.py stock                       # 주제 하나
  python3 tools/outlier_research.py stock health space selfdev story lifetips
  옵션: --per-group 2   키워드 그룹마다 검색할 키워드 수 (<주제>/analyzer_config.toml 의 KEYWORD_GROUPS 앞에서부터)
        --days 180      최근 며칠 안에 올라온 영상 (모자라면 --fallback-days 365 까지 넓힘)
        --max-subs 50000 --min-ratio 3 --min-views 10000 --min-sec 240   성공 사례 기준
        --top 15        자막·댓글을 모을 성공 사례 수 (채널당 최대 --per-channel 2)
        --comments 100  사례마다 모을 댓글 수 (인기순)
        --long          20분 넘는 영상도 검색 (검색 횟수 두 배)
        --quota 9000    이번 실행 API 단위 한도
        --from-existing 분석기 결과에서 고르기 (API 키 없이)
        --refresh       캐시 무시

수집 방법:
  기본 — YouTube Data API v3 (환경 변수 YOUTUBE_API_KEY, 분석기와 같은 키):
    검색 search.list (publishedAfter = 지금 - days, videoDuration=medium(4~20분)[+long], order=viewCount, KR·ko) — 100단위/번
    영상 videos.list (설명·태그·길이·조회수), 채널 channels.list (구독자), 댓글 commentThreads.list (인기순) — 1단위/번
    --quota 로 이번 실행 한도(기본 9000단위, 하루 10,000 — 분석기·피드백 도구와 같은 키면 함께 줄어든다). 넘기 전에 검색을 멈춘다.
    검색 횟수 = 키워드 그룹 × --per-group (× 2 if --long): 주식 9×2 = 18번(1,800단위), 다른 주제 6×2 = 12번(1,200단위) → 6개 주제 약 7,800단위.
  키: 환경 변수 YOUTUBE_API_KEY, 없으면 저장소 최상위 .env 의 YOUTUBE_API_KEY= (집 PC, 분석기와 같은 파일 — git 에 올라가지 않음)
  자막: youtube-transcript-api (한국어). 클라우드 IP 는 YouTube 가 막는다(2026-10-12 확인: RequestBlocked) → 집 PC 에서 실행하면 받힌다.
        못 받으면 '자막 막힘'으로 적고 설명·챕터·댓글로 분석한다.
  --from-existing: 네트워크 검색 없이 분석기 결과(<주제>/result/data/videos.csv·audience_comments.csv)에서 같은 기준으로 고른다
        (썸네일만 i.ytimg.com 에서 받음). 분석기 검색이 최근 영상만 찾은 것이 아니라 최근·작은 채널 사례가 적을 수 있다.
  yt-dlp 로 YouTube 페이지를 직접 읽는 방법은 쓰지 않는다: 클라우드 IP 는 곧 "봇 확인"에 막힌다(2026-10-12 확인). 확인을 피해 가지 않는다.

결과 (<주제>/result/outliers/):
  candidates.csv  검색에서 걸린 롱폼 후보 전부 (구독자·조회수·배수·올린 날)            ← git
  outliers.csv    기준을 통과한 성공 사례 (배수 순)                                   ← git
  summary.md      사례 표 + 사례마다 설명 앞부분·챕터·도입부·말 속도·인기 댓글 (짧게 인용) ← git (분석 문서의 근거)
  <순위>_<영상ID>/ metadata.json · description.txt · transcript.txt · comments.csv · thumbnail.jpg
                  ← 다른 사람의 글·이미지라 git 에 올리지 않는다 (.gitignore). 이 세션의 분석에만 쓴다
로그: [STAGE] [시각] key=value (SEARCH·VIDEO·FILTER·DEEP·DONE)
※ 연구·교육용. 다른 채널 영상을 내려받지 않는다(메타데이터·자막 글·댓글만).
"""
import argparse
import csv
import json
import logging
import os
import re
import sys
import time
import tomllib
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VERSION = "v1.0"
LOG = logging.getLogger("outlier")
HANGUL = re.compile(r"[가-힣]")


def log(stage, level=logging.INFO, **kv):
    LOG.log(level, "[%s] [%s] %s", stage, datetime.now().isoformat(timespec="seconds"),
            " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) and ' ' in v else v}" for k, v in kv.items()))


def load_keywords(topic, per_group):
    cfg_p = ROOT / topic / "analyzer_config.toml"
    if not cfg_p.is_file():
        raise SystemExit(f"[START] ❌ {cfg_p} 없음 — 주제 폴더 확인")
    cfg = tomllib.loads(cfg_p.read_text("utf-8"))
    groups = cfg.get("KEYWORD_GROUPS") or {}
    kws = [(g, k) for g, ks in groups.items() for k in ks[:per_group]]
    exclude = [w for w in (cfg.get("EXCLUDE_KEYWORDS") or []) if w]
    return kws, exclude, cfg.get("TOPIC", topic)


API = "https://www.googleapis.com/youtube/v3/"
COST = {"search": 100, "videos": 1, "channels": 1, "commentThreads": 1}


class Api:
    """YouTube Data API v3 (키는 환경 변수 YOUTUBE_API_KEY — 값은 로그에 쓰지 않음). 사용 단위를 세고 한도 전에 멈춘다."""

    def __init__(self, key, quota):
        self.key, self.quota, self.used = key, quota, 0

    def get(self, kind, **params):
        if self.used + COST[kind] > self.quota:
            raise QuotaStop(f"이번 실행 한도 {self.quota}단위 — 사용 {self.used}")
        url = API + kind + "?" + urllib.parse.urlencode({**params, "key": self.key})
        for attempt in range(3):
            try:
                with urllib.request.urlopen(urllib.request.Request(url), timeout=30) as r:
                    self.used += COST[kind]
                    return json.loads(r.read().decode("utf-8"))
            except urllib.error.HTTPError as e:
                body = e.read().decode("utf-8", "replace")[:300]
                if e.code == 403 and ("quota" in body.lower()):
                    raise QuotaStop("하루 할당량(10,000단위) 소진 — 내일 다시 (캐시는 남음)")
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
        out = []
        for i in range(0, len(ids), 50):
            out += self.get("videos", part="snippet,contentDetails,statistics", id=",".join(ids[i:i + 50])).get("items", [])
        return out

    def channels(self, ids):
        out = {}
        for i in range(0, len(ids), 50):
            for it in self.get("channels", part="statistics", id=",".join(ids[i:i + 50])).get("items", []):
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


class QuotaStop(Exception):
    pass


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


def speech_stats(snips):
    """자막으로 말 속도(한글 음절/분 — 말하는 구간 기준)와 도입부(첫 20초) 글."""
    if not snips:
        return {}
    syl = sum(len(HANGUL.findall(s["text"])) for s in snips)
    span = max(1e-6, snips[-1]["start"] + snips[-1]["duration"] - snips[0]["start"])
    hook = " ".join(s["text"] for s in snips if s["start"] < 20).replace("\n", " ")
    first60 = " ".join(s["text"] for s in snips if s["start"] < 60).replace("\n", " ")
    return {"syl": syl, "syl_per_sec": round(syl / span, 2), "hook20": hook[:300], "first60_syl": len(HANGUL.findall(first60))}


def collect_api(topic, a, api, kws, exclude, out):
    """검색(최근·조회수 순) → 영상·채널 정보 → 후보 행 목록. 캐시: out/.cache/<id>.json"""
    cache_dir = out / ".cache"
    since = (datetime.now(timezone.utc) - timedelta(days=a.fallback_days)).strftime("%Y-%m-%dT00:00:00Z")
    found = {}
    for g, q in kws:
        for dur in (("medium", "long") if a.long else ("medium",)):
            try:
                ids = api.search(q, since, dur)
            except QuotaStop as e:
                log("SEARCH", logging.WARNING, topic=topic, note=str(e), searched=len(found))
                break
            for vid in ids:
                found.setdefault(vid, []).append(q)
            log("SEARCH", query=q, group=g, dur=dur, results=len(ids), quota_used=api.used)
        else:
            continue
        break
    need = [v for v in found if a.refresh or not (cache_dir / f"{v}.json").is_file()]
    for it in api.videos(need):
        sn, cd, st = it["snippet"], it["contentDetails"], it.get("statistics", {})
        info = {"id": it["id"], "title": sn.get("title"), "channel": sn.get("channelTitle"), "channel_id": sn.get("channelId"),
                "published": sn.get("publishedAt"), "description": sn.get("description"), "tags": sn.get("tags"),
                "duration": iso_seconds(cd.get("duration")), "live": sn.get("liveBroadcastContent") != "none",
                "view_count": int(st.get("viewCount", 0)), "like_count": int(st.get("likeCount", 0) or 0),
                "comment_count": int(st.get("commentCount", 0) or 0)}
        (cache_dir / f"{it['id']}.json").write_text(json.dumps(info, ensure_ascii=False), "utf-8")
    infos = [json.loads((cache_dir / f"{v}.json").read_text("utf-8")) for v in found if (cache_dir / f"{v}.json").is_file()]
    subs = api.channels(sorted({i["channel_id"] for i in infos}))
    rows = []
    for i in infos:
        if any(w in (i["title"] or "") for w in exclude):
            continue
        i["subs"] = subs.get(i["channel_id"])
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


def run_topic(topic, a, api):
    t0 = time.time()
    out = ROOT / topic / "result" / "outliers"
    (out / ".cache").mkdir(parents=True, exist_ok=True)
    kws, exclude, topic_name = load_keywords(topic, a.per_group)
    source = "existing" if a.from_existing else "api"
    log("START", topic=topic, name=topic_name, source=source, keywords=len(kws), per_group=a.per_group, days=a.days,
        max_subs=a.max_subs, min_ratio=a.min_ratio, min_views=a.min_views, min_sec=a.min_sec, tool=f"outlier_research.py {VERSION}")
    now = datetime.now(timezone.utc)
    existing_comments = {}
    if a.from_existing:
        infos, existing_comments = collect_existing(topic)
        found = {}
    else:
        infos, found = collect_api(topic, a, api, kws, exclude, out)
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
        q = [r for r in rows if r["subs"] and r["subs"] <= a.max_subs and r["ratio"] and r["ratio"] >= a.min_ratio
             and r["views"] >= a.min_views and r["age_days"] is not None and r["age_days"] <= days and r["minutes"] * 60 >= a.min_sec]
        return sorted(q, key=lambda r: -r["ratio"])
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
    for k, r in enumerate(top, 1):
        d = out / f"{k:02d}_{r['id']}"
        d.mkdir(parents=True, exist_ok=True)
        info = next(i for i in infos if i["id"] == r["id"])
        (d / "description.txt").write_text(info.get("description") or "", "utf-8")
        if a.from_existing:
            cms = existing_comments.get(r["id"], [])
        else:
            try:
                cms = api.comments(r["id"], a.comments)
            except (QuotaStop, RuntimeError) as e:
                cms = []
                log("DEEP", logging.WARNING, id=r["id"], step="comments", error=str(e)[:150])
        with open(d / "comments.csv", "w", newline="", encoding="utf-8-sig") as f:
            w = csv.DictWriter(f, fieldnames=["likes", "text", "replies", "published"])
            w.writeheader()
            w.writerows(cms)
        snips, lang, st = transcript(r["id"]) if not a.no_transcript else ([], "-", "건너뜀(--no-transcript)")
        if snips:
            (d / "transcript.txt").write_text("\n".join(f"[{x['start']:7.1f}] {x['text']}" for x in snips), "utf-8")
        stats = speech_stats(snips)
        try:
            req = urllib.request.Request(f"https://i.ytimg.com/vi/{r['id']}/hqdefault.jpg", headers={"User-Agent": "Mozilla/5.0"})
            (d / "thumbnail.jpg").write_bytes(urllib.request.urlopen(req, timeout=20).read())
        except Exception as e:
            log("DEEP", logging.WARNING, id=r["id"], step="thumbnail", error=str(e)[:100])
        meta = {**r, "rank": k, "source": source, "tags": info.get("tags"), "chapters": chapters_from(info.get("description") or ""),
                "transcript_lang": lang, "transcript_status": st, **stats, "comments_fetched": len(cms),
                "tool": f"outlier_research.py {VERSION}", "collected": datetime.now().isoformat(timespec="seconds")}
        (d / "metadata.json").write_text(json.dumps(meta, ensure_ascii=False, indent=1), "utf-8")
        deep.append((meta, info, cms))
        log("DEEP", topic=topic, rank=k, id=r["id"], subs=r["subs"], views=r["views"], ratio=r["ratio"], age=r["age_days"],
            minutes=r["minutes"], transcript=st if st != "ok" else lang, comments=len(cms))
    write_summary(out, topic, topic_name, a, used_days, rows, q, deep, source)
    log("DONE", topic=topic, source=source, candidates=len(rows), qualified=len(q), deep=len(deep),
        quota_used=api.used if api else 0, minutes=round((time.time() - t0) / 60, 1), out=str(out.relative_to(ROOT)))


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
         "다른 채널의 자막·댓글 원문·썸네일은 git 에 올리지 않고(각 사례 폴더, .gitignore), 여기에는 짧게만 인용한다.", "",
         f"- 기준: 최근 {used_days}일 안 · 구독자 {a.max_subs:,}명 이하 · 조회수 ≥ 구독자 × {a.min_ratio} · 조회수 {a.min_views:,} 이상 · "
         f"{a.min_sec // 60}분 이상 (쇼츠 제외) · 채널당 {a.per_channel}개까지",
         (f"- 후보 {len(rows)}개 — 자료: YouTube Data API 검색(`analyzer_config.toml` 키워드 그룹마다 {a.per_group}개, 최근 {a.fallback_days}일·조회수 순·4~20분"
          + (", 20분 넘음" if a.long else "") + ")" if source == "api" else
          f"- 후보 {len(rows)}개 — 자료: 분석기 결과 `result/data/videos.csv` (⚠️ 분석기 검색은 최근 영상만 찾지 않았다 — 최근·작은 채널 사례가 적으면 API 수집으로 다시)")
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
            L.append(f"- 말 속도 {meta['syl_per_sec']}음절/초 · 첫 1분 {meta['first60_syl']}음절")
        else:
            L.append(f"- 자막: {meta['transcript_status']}")
        top = sorted(cms, key=lambda c: -int(c.get("likes") or 0))[:10]
        if top:
            L.append(f"- 인기 댓글 {len(cms)}개 중 상위 10 (좋아요):")
            L += [f"  - ({c.get('likes')}) {short(c.get('text'), 140)}" for c in top]
        L.append("")
    (out / "summary.md").write_text("\n".join(L), "utf-8")


def main():
    ap = argparse.ArgumentParser(description="작은 채널 성공 사례(최근·롱폼·조회수/구독자 배수) 수집 — 내용·댓글 분석용")
    ap.add_argument("topics", nargs="+")
    ap.add_argument("--per-group", type=int, default=2)
    ap.add_argument("--days", type=int, default=180)
    ap.add_argument("--fallback-days", type=int, default=365)
    ap.add_argument("--max-subs", type=int, default=50000)
    ap.add_argument("--min-ratio", type=float, default=3.0)
    ap.add_argument("--min-views", type=int, default=10000)
    ap.add_argument("--min-sec", type=int, default=240)
    ap.add_argument("--top", type=int, default=15)
    ap.add_argument("--per-channel", type=int, default=2)
    ap.add_argument("--comments", type=int, default=100)
    ap.add_argument("--long", action="store_true", help="20분 넘는 영상도 검색")
    ap.add_argument("--quota", type=int, default=9000, help="이번 실행 API 단위 한도 (주제 여러 개를 함께 셈. 하루 10,000)")
    ap.add_argument("--from-existing", action="store_true", help="분석기 결과에서 고르기 (API 키 없이)")
    ap.add_argument("--no-transcript", action="store_true", help="자막 받기 건너뜀 (클라우드 IP 는 막힘)")
    ap.add_argument("--refresh", action="store_true")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args()
    logging.basicConfig(level=getattr(logging, a.log_level), format="%(message)s", stream=sys.stdout)
    api = None
    if not a.from_existing:
        key = os.environ.get("YOUTUBE_API_KEY", "")
        env_p = ROOT / ".env"     # 집 PC: 분석기와 같은 .env (git 에 올라가지 않음). 값은 출력하지 않는다
        if not key and env_p.is_file():
            m = re.search(r"^\s*YOUTUBE_API_KEY\s*=\s*['\"]?([^'\"\s]+)", env_p.read_text("utf-8"), re.M)
            key = m.group(1) if m else ""
        if not key:
            raise SystemExit("[START] ❌ 환경 변수 YOUTUBE_API_KEY 가 없음 → 클라우드 환경 설정(Network secrets/환경 변수)에 넣고 새 세션에서, "
                             "또는 집 PC 에서 실행 (키 없이 기존 자료로만: --from-existing)")
        api = Api(key, a.quota)
    for t in a.topics:
        try:
            run_topic(t, a, api)
        except SystemExit:
            raise
        except Exception as e:   # 한 주제가 실패해도 다음 주제
            log("DONE", logging.ERROR, topic=t, error=f"{type(e).__name__}: {str(e)[:200]}", hint="--sleep 을 늘리거나 잠시 뒤 다시 (캐시는 남음)")


if __name__ == "__main__":
    main()
