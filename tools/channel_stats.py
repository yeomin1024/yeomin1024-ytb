#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.2 — 2026-11-27 — 키: YOUTUBE_API_KEY 가 없으면 --topic 의 <주제>_YOUTUBE_API_KEY (사용자 지시 2026-11-27 "주제별 접두사를 변수명에 붙여서 구분되도록해"). 한 번 정한 키로 끝까지 (오류가 나도 바꾸지 않음). 함수 main.
# (v1.1) — 2026-11-27 — 꺼 둔 주제(studio/state/topics.json)만의 채널은 받지 않음 — 사용자 지시 "비활성화하면 … 에이전트가 보지도 않도록". 함수 our_channels.
# (v1.0) — 2026-11-27 — 최초: 내 채널 공개 지표 → 제작 판 '채널 분석' (사용자 지시 2026-11-27 "채널 분석 - 유튜브와 연동하여 내 채널 분석 자료 확인 가능").
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.1 | 2026-11-27 | 꺼 둔 주제만의 채널 뺌 | our_channels |
# | v1.0 | 2026-11-27 | 최초 — 채널 찾기(youtube.json · youtube_channel.json) · channels.list · 올린 영상 목록 최근 50 · videos.list 지표 · 시청 분석(youtube_feedback 결과가 있으면 붙임) | 모두 |
"""내 채널(우리가 올린 채널) 공개 지표를 받아 studio/channels/channels.json 에 쓴다 — 제작 판이 읽음.

  YOUTUBE_API_KEY=… python3 tools/channel_stats.py [--max 50] [--push]

  - 채널 = 저장소의 */source/**/youtube.json 'channelId' + */youtube_channel.json 'channel_id' (모두 · 주제 상관없이)
  - 단위: 채널마다 channels.list 1 + playlistItems.list 1 + videos.list 1 ≈ 3단위 (하루 10,000 가운데)
  - 공개 자료만 (구독자·조회수·좋아요·댓글·길이). 예약·비공개 영상은 이 키로 안 보임.
  - 시청 지속·클릭률·유입 경로 = 채널 주인 OAuth (tools/youtube_feedback.py — PC) → 그 결과(<주제>/source/<영상ID>/stats/)가 있으면 영상 줄에 붙임.
  로그: [STAGE] [시각] key=value … · 키 값은 출력하지 않음.
"""
import argparse
import datetime as dt
import glob
import json
import logging
import os
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "studio" / "channels" / "channels.json"
API = "https://www.googleapis.com/youtube/v3"
VERSION = "v1.2"
KST = dt.timezone(dt.timedelta(hours=9))
LOG = logging.getLogger("channel_stats")


def log(stage, level=logging.INFO, **kv):
    LOG.log(level, "[%s] [%s] %s", stage, dt.datetime.now(KST).strftime("%Y-%m-%dT%H:%M:%S"), " ".join(f"{k}={v}" for k, v in kv.items()))


def get(path: str, key: str, **params) -> dict:
    u = f"{API}/{path}?" + urllib.parse.urlencode(dict(params, key=key))
    try:
        with urllib.request.urlopen(u, timeout=40) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")[:300]
        raise SystemExit(f"[API] ❌ {path} HTTP {e.code}: {body} — 키·할당량 확인 (값은 출력하지 않음)")
    except urllib.error.URLError as e:
        raise SystemExit(f"[API] ❌ {path} 연결 실패: {e.reason} — googleapis.com 이 열린 세션에서")


def our_channels() -> dict:
    """채널 ID → {name, topics}."""
    out: dict = {}
    for f in glob.glob(str(ROOT / "*" / "source" / "**" / "youtube*.json"), recursive=True):
        try:
            j = json.loads(Path(f).read_text("utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        cid = j.get("channelId") or ""
        if re.fullmatch(r"UC[A-Za-z0-9_-]{22}", cid):
            topic = Path(f).relative_to(ROOT).parts[0]
            o = out.setdefault(cid, {"name": j.get("channel", ""), "topics": set()})
            o["topics"].add(topic)
    for f in glob.glob(str(ROOT / "*" / "youtube_channel.json")):
        try:
            j = json.loads(Path(f).read_text("utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        cid = j.get("channel_id") or ""
        if re.fullmatch(r"UC[A-Za-z0-9_-]{22}", cid):
            o = out.setdefault(cid, {"name": j.get("name", ""), "topics": set()})
            o["topics"].add(Path(f).parent.name)
    sys.path.insert(0, str(ROOT / "tools"))
    import topic_state                                        # v1.1
    off = topic_state.disabled()
    skip = [c for c, o in out.items() if o["topics"] and o["topics"] <= off]
    if skip:
        log("TOPIC", skipped_channels=",".join(skip), disabled=",".join(sorted(off)), note="꺼 둔 주제만의 채널 — 받지 않음")
    return {c: o for c, o in out.items() if c not in skip}


def iso_dur(s: str) -> tuple[str, int]:
    m = re.fullmatch(r"P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", s or "")
    if not m:
        return "", 0
    d, h, mi, se = (int(x or 0) for x in m.groups())
    sec = d * 86400 + h * 3600 + mi * 60 + se
    return (f"{sec // 3600}:{sec % 3600 // 60:02d}:{sec % 60:02d}" if sec >= 3600 else f"{sec // 60}:{sec % 60:02d}"), sec


def analytics_of(video_id: str) -> dict | None:
    """youtube_feedback.py 원자료가 저장소에 있으면 그 영상의 요약 몇 칸."""
    for f in sorted(glob.glob(str(ROOT / "*" / "source" / "**" / "stats" / "*.json"), recursive=True), reverse=True):
        try:
            j = json.loads(Path(f).read_text("utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if j.get("videoId") == video_id or (j.get("video") or {}).get("id") == video_id:
            keep = {k: j[k] for k in ("averageViewDuration", "averageViewPercentage", "impressions", "impressionsClickThroughRate", "trafficSources") if k in j}
            return keep or {"file": str(Path(f).relative_to(ROOT))}
    return None


def run(key: str, max_n: int) -> dict:
    chans = our_channels()
    log("START", tool=f"channel_stats.py {VERSION}", channels=len(chans), key=f"…{key[-4:]}" if key else "없음")
    if not chans:
        raise SystemExit("[START] ❌ 저장소에 채널 ID 가 없음 (youtube.json · youtube_channel.json)")
    ids = list(chans)
    res = get("channels", key, part="snippet,statistics,contentDetails", id=",".join(ids), maxResults=50)
    now = dt.datetime.now(dt.timezone.utc)
    out = []
    for it in res.get("items", []):
        cid, st = it["id"], it.get("statistics", {})
        up = it.get("contentDetails", {}).get("relatedPlaylists", {}).get("uploads", "")
        rec = {"id": cid, "title": it["snippet"].get("title", ""), "topics": sorted(chans[cid]["topics"]),
               "subs": int(st.get("subscriberCount", 0)), "hidden_subs": bool(st.get("hiddenSubscriberCount")),
               "views": int(st.get("viewCount", 0)), "videos": int(st.get("videoCount", 0)), "recent": []}
        if up and rec["videos"]:
            pl = get("playlistItems", key, part="contentDetails", playlistId=up, maxResults=min(50, max_n))
            vids = [x["contentDetails"]["videoId"] for x in pl.get("items", [])]
            if vids:
                vd = get("videos", key, part="snippet,statistics,contentDetails", id=",".join(vids), maxResults=50)
                for v in vd.get("items", []):
                    s = v.get("statistics", {})
                    pub = v["snippet"].get("publishedAt", "")
                    dur, sec = iso_dur(v.get("contentDetails", {}).get("duration", ""))
                    days = max((now - dt.datetime.fromisoformat(pub.replace("Z", "+00:00"))).total_seconds() / 86400, 1) if pub else None
                    views = int(s.get("viewCount", 0))
                    rec["recent"].append({"id": v["id"], "title": v["snippet"].get("title", ""), "published": pub, "views": views,
                                          "likes": int(s["likeCount"]) if "likeCount" in s else None, "comments": int(s.get("commentCount", 0)),
                                          "duration": dur, "seconds": sec, "shorts": 0 < sec <= 180 and "#shorts" in (v["snippet"].get("title", "") + v["snippet"].get("description", "")).lower() or 0 < sec <= 60,
                                          "vpd": round(views / days, 1) if days else None, "analytics": analytics_of(v["id"])})
                rec["recent"].sort(key=lambda r: r["published"], reverse=True)
        out.append(rec)
        log("CHANNEL", id=cid, title=rec["title"].replace(" ", "_"), subs=rec["subs"], views=rec["views"], videos=rec["videos"], recent=len(rec["recent"]))
    missing = [c for c in ids if c not in {x["id"] for x in out}]
    if missing:
        log("CHANNEL", logging.WARNING, missing=",".join(missing), note="API 가 돌려주지 않음 — 채널 ID 확인")
    return {"tool": f"channel_stats.py {VERSION}", "made": dt.datetime.now(KST).strftime("%Y-%m-%d %H:%M"),
            "source": "YouTube Data API v3 공개 지표 (channels · playlistItems · videos)", "channels": out,
            "note": "시청 지속·클릭률·유입 경로는 PC tools/youtube_feedback.py (OAuth) 결과가 있으면 영상 줄에 붙음"}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="내 채널 공개 지표 → studio/channels/channels.json")
    ap.add_argument("--max", type=int, default=50, help="채널마다 최근 영상 수 (최대 50)")
    ap.add_argument("--push", action="store_true", help="결과 파일만 커밋·푸시 (main)")
    ap.add_argument("--topic", default="", help="v1.2 이 주제의 키(<주제>_YOUTUBE_API_KEY)로 읽기 — 없으면 YOUTUBE_API_KEY")
    ap.add_argument("--log-level", default="INFO")
    a = ap.parse_args(argv)
    logging.basicConfig(level=getattr(logging, a.log_level, logging.INFO), format="%(message)s", stream=sys.stdout)
    sys.path.insert(0, str(ROOT / "tools"))
    import topic_keys                                        # v1.2 주제 접두사 키
    key, src = topic_keys.get("YOUTUBE_API_KEY", a.topic or None)
    log("KEYS", source=src, topic=a.topic or "-")
    if not key:
        raise SystemExit("[START] ❌ YOUTUBE_API_KEY 가 없음 — 키가 있는 세션에서 (값은 채팅에 붙이지 않음)")
    data = run(key, a.max)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", "utf-8")
    log("DONE", out=str(OUT.relative_to(ROOT)), channels=len(data["channels"]), videos=sum(len(c["recent"]) for c in data["channels"]))
    if a.push:
        r = subprocess.run(f'git -C "{ROOT}" add "{OUT}" && git -C "{ROOT}" commit -m "[채널 분석] 공개 지표 (tools/channel_stats.py {VERSION})" && git -C "{ROOT}" pull --rebase -q && git -C "{ROOT}" push -q origin HEAD:main',
                           shell=True, capture_output=True, text=True)
        log("PUSH", ok=r.returncode == 0, note=(r.stderr or r.stdout)[-200:].replace("\n", " ") if r.returncode else "main 에 올림")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
