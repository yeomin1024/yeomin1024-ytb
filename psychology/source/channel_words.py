#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0.2 — 2026-11-27 — 키: PSYCHOLOGY_YOUTUBE_API_KEY → YOUTUBE_API_KEY_PSYCHOLOGY → YOUTUBE_API_KEY 순서 (주제 접두사 — 사용자 지시 2026-11-27 "주제별 접두사를 변수명에 붙여서 구분되도록해"). 시작할 때 한 번 정함.
# (이전) VERSION: v1.0.1 — 2026-11-23 — 고침: 이름만 심리인 채널 5곳을 뺌(EXCLUDE_CH — 업로드 제목을 Claude 가 봄: 연예인 명언·노래·
#          자기계발·육아·연애 예능 리뷰) 하고 다음 순위로 30곳을 채움 · 뜻 없는 말토막(하는·않는·있는…)을 낱말 순위에서 뺌(FUNC_STOP)
# (이전) v1.0.0 — 2026-11-23 — 신규: 구독자 많은 심리 전문 채널들이 공통으로 쓰는 주제·제목 낱말 순위
#          (사용자 지시 2026-11-23 "그럼 구독자 많은 채널에서 공통적으로 등장하는 주제, 단어들이 뭐야 순위매겨서 알려줘봐")
"""
channel_words.py — 큰 심리 채널의 최근 롱폼 제목에서 주제·낱말·제목 꼴 순위

흐름
  1. LOAD     : result/channels/psych_channels.csv 에서 '심리 전문' 구독자 상위 TOP_N 채널
                → channels.list(contentDetails) 업로드 목록 → playlistItems 최근 PAGES×50편 → videos.list 통계·길이
                (응답은 result/channels/uploads_cache.json.gz — 다시 돌리면 할당량 0)
  2. VALIDATE : 4분 미만(쇼츠)·라이브·통계 없음·올린 지 7일 미만 뺌 (뺀 수 로그)
  3. FEATURE  : 주제 = psychology/tag_rules.toml [TAG_THEMES] (제목에서 가장 긴 글자가 맞는 묶음 — 분석기와 같은 규칙)
                낱말 = tools/content_analysis.py words() (끝 조사를 거칠게 뗌 — 콘텐츠 분석과 같은 함수)
                제목 꼴 = tools/content_analysis.py title_types()
                채널 평소 대비 = 조회수 ÷ 그 채널 (이번 표본) 조회수 가운데값 — 채널 크기를 뺀 성과
  4. METRICS  : 주제·낱말·제목 꼴마다 — 쓰는 채널 수(공통) · 영상 수 · 평소 대비 가운데값 · 평소보다 잘된 비율
  5. EXPORT   : result/channels/channel_words.md · channel_words.csv

한계: 채널마다 최근 PAGES×50편만 (오래된 영상 없음) · 낱말 자르기는 거칠다(형태소 분석 아님) · '평소 대비'는 그 채널
      표본 안에서만 비교 · 채널 선정은 psych_channels.py 의 '심리 전문' 분류를 따름
실행: python3 psychology/source/channel_words.py run      # 캐시 없을 때만 API (채널 30곳 ≈ 120단위)
      python3 psychology/source/channel_words.py analyze  # 캐시만
"""
from __future__ import annotations

import csv
import gzip
import hashlib
import json
import logging
import os
import re
import statistics as st
import sys
import time
import tomllib
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import requests

VERSION = "v1.0.2"
HERE = Path(__file__).resolve().parent
PSY = HERE.parent
ROOT = PSY.parent
sys.path.insert(0, str(ROOT / "tools"))
from content_analysis import title_types, words  # noqa: E402 — 콘텐츠 분석과 같은 낱말·제목 꼴 규칙

OUT_DIR = PSY / "result" / "channels"
CH_CSV = OUT_DIR / "psych_channels.csv"
API_CACHE = OUT_DIR / "uploads_cache.json.gz"
TAG_RULES = PSY / "tag_rules.toml"
API = "https://www.googleapis.com/youtube/v3"
AS_OF = datetime(2026, 11, 23, tzinfo=timezone.utc)
TOP_N = 30            # 심리 전문 채널 구독자 상위 몇 곳
PAGES = 2             # 채널마다 최근 50 × PAGES 편
MIN_SEC = 240
MIN_AGE = 7
MIN_CH_WORD = 4       # 낱말 순위: 이만큼 다른 채널이 쓴 낱말만 (한 채널 시리즈 이름을 거름)
# v1.0.1: 이름엔 심리·마음이 있지만 최근 업로드가 다른 주제인 채널 (Claude 가 업로드 제목을 보고 정함)
EXCLUDE_CH = {
    "멘탈케어::힐링 심리학 채널::": "연예인 명언·스포츠 (최근 98편 중 78편 주제 묶음 없음)",
    "마음치유 락카페": "노래 모음",
    "이하영의 마음운동": "성공·자기계발",
    "이민주육아상담소": "육아 — 심리 분석 때 주제 밖으로 뺀 갈래 (excluded_videos.md)",
    "심리대화": "연애 예능(나는솔로) 리뷰 — 심리 분석 때 주제 밖으로 뺀 갈래",
}
# v1.0.1: 뜻 없는 말토막 (동사·형용사 활용형 조각) — 낱말 순위에서만 뺌
FUNC_STOP = {"하는", "않는", "없는", "되는", "있는", "하지", "못하", "말하", "보이", "이런", "내가", "있다", "보세", "있습니다",
             "하고", "사는", "위한", "어떻게", "하면", "해야", "합니다", "입니다", "그런", "이렇게", "되는", "같은", "이것", "이게",
             "한다", "했다", "하세요", "마세요", "없다", "않고", "다른", "모든", "많은", "얼마나", "무조건"}
EXTRA_STOP = {"ep", "편", "부", "풀버전", "full", "feat", "ft", "with", "sub", "eng", "kor", "shorts", "the"}

log = logging.getLogger("channel_words")


def L(stage: str, level: int = logging.INFO, **kv) -> None:
    log.log(level, " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if not isinstance(v, str) or ' ' in v else v}"
                            for k, v in kv.items()), extra={"stage": stage})


class F(logging.Formatter):
    def format(self, r):
        lv = "" if r.levelno == logging.INFO else f" level={r.levelname}"
        return f"[{getattr(r, 'stage', 'MAIN')}] [{datetime.now():%Y-%m-%dT%H:%M:%S}]{lv} {r.getMessage()}"


class YT:
    def __init__(self, key, offline):
        self.key, self.offline, self.units, self.calls, self.hits = key, offline, 0, 0, 0
        self.cache = json.loads(gzip.decompress(API_CACHE.read_bytes())) if API_CACHE.exists() else {}
        self.dirty = False

    def get(self, endpoint, **params):
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
        self.units += 1                      # channels·playlistItems·videos 모두 1단위
        if r.status_code != 200:
            L("LOAD", logging.WARNING, error=f"http{r.status_code}", endpoint=endpoint, body=r.text[:150],
              next_step="할당량이면 한국 17시 뒤 run 다시")
            return None
        d = r.json()
        items = d.get("items", [])
        if endpoint == "channels":
            d = {"items": [{"id": it["id"], "uploads": it["contentDetails"]["relatedPlaylists"]["uploads"]} for it in items]}
        elif endpoint == "playlistItems":
            d = {"nextPageToken": d.get("nextPageToken"),
                 "items": [{"videoId": it["contentDetails"]["videoId"]} for it in items]}
        elif endpoint == "videos":
            d = {"items": [{"id": it["id"], "title": it["snippet"]["title"], "channelId": it["snippet"]["channelId"],
                            "publishedAt": it["snippet"]["publishedAt"],
                            "live": it["snippet"].get("liveBroadcastContent", "none") != "none",
                            "views": it.get("statistics", {}).get("viewCount"),
                            "duration": it.get("contentDetails", {}).get("duration")} for it in items]}
        self.cache[h] = d
        self.dirty = True
        return d

    def save(self):
        if self.dirty:
            API_CACHE.write_bytes(gzip.compress(json.dumps(self.cache, ensure_ascii=False).encode(), mtime=0))


def iso_sec(s):
    m = re.fullmatch(r"P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", s or "")
    return sum(int(x or 0) * k for x, k in zip(m.groups(), (86400, 3600, 60, 1))) if m else 0


def pick_channels() -> list[dict]:
    with open(CH_CSV, encoding="utf-8-sig") as f:
        rows = [r for r in csv.DictReader(f) if r["kind"] == "심리 전문"]
    rows.sort(key=lambda r: -int(r["subs"]))
    skipped = [r["title"] for r in rows if r["title"] in EXCLUDE_CH]
    top = [r for r in rows if r["title"] not in EXCLUDE_CH][:TOP_N]
    L("LOAD", source=str(CH_CSV.relative_to(ROOT)), specialist=len(rows), excluded=skipped, picked=len(top),
      subs_range=f"{int(top[-1]['subs']):,}~{int(top[0]['subs']):,}")
    return top


def load_uploads(yt: YT, chans: list[dict]) -> list[dict]:
    ids = [c["cid"] for c in chans]
    up = {}
    for i in range(0, len(ids), 50):
        d = yt.get("channels", part="contentDetails", id=",".join(ids[i:i + 50]), maxResults=50)
        up.update({it["id"]: it["uploads"] for it in (d or {}).get("items", [])})
    vids = []
    for cid in ids:
        if cid not in up:
            L("LOAD", logging.WARNING, channel=cid, error="no uploads playlist", next_step="run 다시")
            continue
        token = None
        for _ in range(PAGES):
            d = yt.get("playlistItems", part="contentDetails", playlistId=up[cid], maxResults=50, pageToken=token) \
                if token else yt.get("playlistItems", part="contentDetails", playlistId=up[cid], maxResults=50)
            if not d:
                break
            vids += [it["videoId"] for it in d["items"]]
            token = d.get("nextPageToken")
            if not token:
                break
    rows = []
    for i in range(0, len(vids), 50):
        d = yt.get("videos", part="snippet,statistics,contentDetails", id=",".join(vids[i:i + 50]), maxResults=50)
        rows += (d or {}).get("items", [])
    L("LOAD", source="uploads playlists (최근 순)", channels=len(up), video_ids=len(vids), videos=len(rows),
      api_calls=yt.calls, units=yt.units, cache_hits=yt.hits)
    return rows


def theme_of(title: str, themes: dict) -> str:
    best, blen = "기타", 0
    for name, ws in themes.items():
        for w in ws:
            if w.lower() in title.lower() and len(w) > blen:
                best, blen = name, len(w)
    return best


def validate(rows: list[dict]) -> list[dict]:
    out, drop = [], defaultdict(int)
    for r in rows:
        if r["views"] is None:
            drop["no_views"] += 1
            continue
        if r["live"]:
            drop["live"] += 1
            continue
        if iso_sec(r["duration"]) < MIN_SEC:
            drop["short_lt_4min"] += 1
            continue
        age = (AS_OF - datetime.fromisoformat(r["publishedAt"].replace("Z", "+00:00"))).days
        if age < MIN_AGE:
            drop["age_lt_7d"] += 1
            continue
        out.append(dict(r, views=int(r["views"]), age=age, sec=iso_sec(r["duration"])))
    L("VALIDATE", rows_in=len(rows), **{f"drop_{k}": v for k, v in drop.items()}, rows_out=len(out),
      date_range=f"{min(r['publishedAt'] for r in out)[:10]}~{max(r['publishedAt'] for r in out)[:10]}" if out else "-")
    return out


def features(rows: list[dict], themes: dict) -> list[dict]:
    by_ch = defaultdict(list)
    for r in rows:
        by_ch[r["channelId"]].append(r["views"])
    med = {c: st.median(v) for c, v in by_ch.items()}
    for r in rows:
        r["rel"] = r["views"] / med[r["channelId"]] if med[r["channelId"]] else 0
        r["theme"] = theme_of(r["title"], themes)
        r["words"] = sorted({w for w in words(r["title"]) if w not in EXTRA_STOP and w not in FUNC_STOP and not w.isdigit()})
        r["types"] = title_types(r["title"])
    L("FEATURE", themes_from=str(TAG_RULES.relative_to(ROOT)), word_fn="tools/content_analysis.py words()",
      channels=len(med), videos=len(rows))
    return rows


def group(rows: list[dict], key) -> list[dict]:
    g = defaultdict(list)
    for r in rows:
        for k in key(r):
            g[k].append(r)
    out = []
    for k, rs in g.items():
        rel = [r["rel"] for r in rs]
        top = max(rs, key=lambda r: r["views"])
        out.append({"key": k, "channels": len({r["channelId"] for r in rs}), "videos": len(rs),
                    "share": len(rs) / len(rows), "rel_median": st.median(rel), "above": sum(x > 1 for x in rel) / len(rel),
                    "top_title": top["title"], "top_views": top["views"], "top_id": top["id"]})
    return out


def pct(x):
    return f"{x * 100:.0f}%"


def nn(x):
    return f"{x / 1e4:,.1f}만" if x >= 1e4 else f"{x:,.0f}"


def esc(s):
    return s.replace("|", "／")[:58]


def export(rows, chans, yt, t0):
    themes = sorted(group(rows, lambda r: [r["theme"]]), key=lambda x: -x["videos"])
    wds = [w for w in group(rows, lambda r: r["words"]) if w["channels"] >= MIN_CH_WORD]
    common = sorted(wds, key=lambda x: (-x["channels"], -x["videos"]))
    perf = sorted([w for w in wds if w["videos"] >= 15 and w["channels"] >= 6], key=lambda x: -x["rel_median"])
    types = sorted(group(rows, lambda r: r["types"] or ["(꼴 없음)"]), key=lambda x: -x["videos"])
    with open(OUT_DIR / "channel_words.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["kind", "key", "channels", "videos", "share", "rel_median", "above_channel_median", "top_views", "top_title"])
        for kind, rs in (("theme", themes), ("word", common), ("title_type", types)):
            for x in rs:
                w.writerow([kind, x["key"], x["channels"], x["videos"], f"{x['share']:.4f}", f"{x['rel_median']:.3f}",
                            f"{x['above']:.3f}", x["top_views"], x["top_title"]])
    nch = len({r["channelId"] for r in rows})
    o = ["# 구독자 많은 심리 채널 — 공통 주제·제목 낱말 순위", "",
         f"VERSION: {VERSION} — 도구 `psychology/source/channel_words.py` · 기준일 {AS_OF:%Y-%m-%d} · 사용자 지시 2026-11-23 "
         "\"그럼 구독자 많은 채널에서 공통적으로 등장하는 주제, 단어들이 뭐야 순위매겨서 알려줘봐\"", "",
         "## 0. 읽는 법·한계",
         f"- 채널 = `psych_channels.md` '심리 전문' 구독자 상위 {len(chans)}곳 ({nn(int(chans[-1]['subs']))}~{nn(int(chans[0]['subs']))}) · "
         f"영상 = 채널마다 최근 업로드 {PAGES * 50}편 중 4분 이상·라이브 아님·올린 지 7일 넘음 → **{len(rows):,}편 · {nch}곳**.",
         "- **공통** = 그 주제·낱말을 쓴 채널 수 (많을수록 큰 채널 여럿이 함께 씀). **평소 대비** = 조회수 ÷ 그 채널 조회수 가운데값 "
         "(1보다 크면 그 채널 평소보다 잘됨 — 채널 크기를 뺀 성과). **잘된 비율** = 평소 대비 1을 넘은 영상 비율.",
         "- 주제 = `tag_rules.toml` [TAG_THEMES] 9묶음(분석기와 같은 규칙) · 낱말 = `tools/content_analysis.py` words() (조사를 거칠게 뗌 — 형태소 분석 아님).",
         f"- 낱말은 {MIN_CH_WORD}개 채널 넘게 쓴 것만 (한 채널 시리즈 이름 거름). 숫자·'ep'·'풀버전' 같은 표시 낱말·'하는·않는' 같은 말토막은 뺌.",
         "- 뺀 채널 (이름만 심리 — 업로드 제목을 Claude 가 봄): " + " · ".join(f"{k} ({v})" for k, v in EXCLUDE_CH.items()), "",
         "## 1. 주제 순위 (영상 수 순)", "",
         "| # | 주제 | 쓴 채널 | 영상 | 비율 | 평소 대비 가운데값 | 잘된 비율 | 대표 영상 (조회수) |", "|---|---|---|---|---|---|---|---|"]
    for i, x in enumerate(themes, 1):
        o.append(f"| {i} | {x['key']} | {x['channels']}/{nch} | {x['videos']} | {pct(x['share'])} | {x['rel_median']:.2f} | "
                 f"{pct(x['above'])} | [{esc(x['top_title'])}](https://youtu.be/{x['top_id']}) ({nn(x['top_views'])}) |")
    o += ["", f"## 2. 공통 낱말 순위 — 쓴 채널 수 순 (상위 40)", "",
          "| # | 낱말 | 쓴 채널 | 영상 | 평소 대비 가운데값 | 잘된 비율 | 대표 영상 (조회수) |", "|---|---|---|---|---|---|---|"]
    for i, x in enumerate(common[:40], 1):
        o.append(f"| {i} | {x['key']} | {x['channels']}/{nch} | {x['videos']} | {x['rel_median']:.2f} | {pct(x['above'])} | "
                 f"[{esc(x['top_title'])}](https://youtu.be/{x['top_id']}) ({nn(x['top_views'])}) |")
    o += ["", "## 3. 잘되는 낱말 순위 — 평소 대비 가운데값 순 (영상 15편·채널 6곳 넘는 낱말만, 상위 25 · 하위 10)", "",
          "| # | 낱말 | 평소 대비 가운데값 | 잘된 비율 | 쓴 채널 | 영상 |", "|---|---|---|---|---|---|"]
    for i, x in enumerate(perf[:25], 1):
        o.append(f"| {i} | {x['key']} | {x['rel_median']:.2f} | {pct(x['above'])} | {x['channels']} | {x['videos']} |")
    o += ["", "하위 10 (평소보다 덜 된 낱말):", "", "| 낱말 | 평소 대비 가운데값 | 잘된 비율 | 쓴 채널 | 영상 |", "|---|---|---|---|---|"]
    for x in perf[-10:]:
        o.append(f"| {x['key']} | {x['rel_median']:.2f} | {pct(x['above'])} | {x['channels']} | {x['videos']} |")
    o += ["", "## 4. 제목 꼴 (콘텐츠 분석과 같은 규칙 — 한 제목에 여럿)", "",
          "| 꼴 | 쓴 채널 | 영상 | 비율 | 평소 대비 가운데값 | 잘된 비율 |", "|---|---|---|---|---|---|"]
    for x in types:
        o.append(f"| {x['key']} | {x['channels']} | {x['videos']} | {pct(x['share'])} | {x['rel_median']:.2f} | {pct(x['above'])} |")
    o += ["", "## 5. 채널", "", "| 채널 | 구독자 | 이번 표본(롱폼) |", "|---|---|---|"]
    cnt = defaultdict(int)
    for r in rows:
        cnt[r["channelId"]] += 1
    for c in chans:
        o.append(f"| {c['title']} | {nn(int(c['subs']))} | {cnt.get(c['cid'], 0)} |")
    o += ["", f"_API {yt.calls}번 {yt.units}단위 · 캐시 {yt.hits}번 · {time.time() - t0:.1f}초_"]
    (OUT_DIR / "channel_words.md").write_text("\n".join(o) + "\n", encoding="utf-8")
    L("EXPORT", md=str((OUT_DIR / "channel_words.md").relative_to(ROOT)), themes=len(themes), words=len(common),
      perf_words=len(perf), top_theme=themes[0]["key"], top_word=common[0]["key"] if common else "-")


def main(argv) -> int:
    h = logging.StreamHandler(sys.stdout)
    h.setFormatter(F())
    log.handlers[:] = [h]
    log.setLevel(os.environ.get("LOG_LEVEL", "INFO").upper())
    cmd = argv[1] if len(argv) > 1 else "analyze"
    t0 = time.time()
    L("START", tool=f"channel_words.py {VERSION}", cmd=cmd, top_n=TOP_N, pages=PAGES)
    with open(TAG_RULES, "rb") as f:
        themes = tomllib.load(f)["TAG_THEMES"]
    yt = YT(next((os.environ[k].strip() for k in ("PSYCHOLOGY_YOUTUBE_API_KEY", "YOUTUBE_API_KEY_PSYCHOLOGY", "YOUTUBE_API_KEY") if os.environ.get(k, "").strip()), ""), offline=(cmd != "run"))
    chans = pick_channels()
    rows = load_uploads(yt, chans)
    yt.save()
    rows = features(validate(rows), themes)
    if not rows:
        L("RESULT", logging.WARNING, error="0 videos", next_step="run 으로 업로드 목록 받기")
        return 1
    export(rows, chans, yt, t0)
    L("RESULT", seconds=round(time.time() - t0, 1), api_units=yt.units)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
