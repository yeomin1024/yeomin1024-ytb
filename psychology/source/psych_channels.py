#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0.2 — 2026-11-27 — 키: PSYCHOLOGY_YOUTUBE_API_KEY → YOUTUBE_API_KEY_PSYCHOLOGY → YOUTUBE_API_KEY 순서 (주제 접두사 — 사용자 지시 2026-11-27 "주제별 접두사를 변수명에 붙여서 구분되도록해"). 시작할 때 한 번 정함.
# (이전) VERSION: v1.0.1 — 2026-11-23 — 고침: 방송사(JTBC News·디글·EBS 등)가 '심리 전문'으로 들어가던 것 — 우리 자료는 그 채널의
#          심리 영상만 골라 모아 '심리 영상 60%' 규칙이 부풀었음. 심리 전문 = 채널 이름에 심리 낱말, 또는 설명에 심리 낱말 +
#          우리 자료 영상도 심리 쪽 · 방송사·뉴스 이름(BROADCAST)은 늘 종합 · 불교·신부·영성·명상(RELIGION)은 따로 묶음
# (이전) v1.0.0 — 2026-11-23 — 신규: 심리 관련 채널을 구독자 많은 순으로 (사용자 지시 2026-11-23 "심리 관련 구독자 많은순으로 채널 알려줘")
"""
psych_channels.py — 심리 관련 한국 채널 목록 (구독자 순)

흐름
  1. LOAD-A : 심리 분석 캐시(psychology/cloud_cache/cache.tgz)의 영상·채널 정보 (할당량 0)
              + incident_cases 검색 캐시(result/incidents/api_cache.json.gz)의 영상·채널
  2. LOAD-B : 채널 검색 CHANNEL_QUERIES (search type=channel, KR, ko, 50개씩 — 검색 1번 100단위)
              → channels.list 로 구독자·영상 수·조회수·개설일 · 응답은 result/channels/api_cache.json.gz
  3. CLASSIFY : 우리 자료에서 그 채널 영상(4분 이상·라이브 뺌) 중 제목에 심리 낱말(PSY_TITLE)이 든 수
              · 채널 이름·설명에 심리 낱말(PSY_NAME) → '심리 전문' = 이름/설명 낱말 또는 (심리 영상 3개+ · 60%+)
              · NOT_PSY(사람이 본 주제 밖 채널) 는 뺌
  4. EXPORT : result/channels/psych_channels.md · .csv

한계: 구독자 수는 받은 날 값(YouTube 가 앞 3자리로 반올림) · '심리 영상 수'는 우리가 모은 영상만 센 것(채널 전체 아님)
      · 채널 검색은 검색어에 걸린 채널만 — 한국 심리 채널 전부는 아님 · 해외 채널(country≠KR)은 뺌
실행: python3 psychology/source/psych_channels.py run      # 채널 검색 (캐시 없을 때만 API)
      python3 psychology/source/psych_channels.py analyze  # 캐시만
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
from collections import defaultdict
from datetime import datetime
from pathlib import Path

import requests

VERSION = "v1.0.2"
HERE = Path(__file__).resolve().parent
PSY = HERE.parent
OUT_DIR = PSY / "result" / "channels"
API_CACHE = OUT_DIR / "api_cache.json.gz"
PSY_TGZ = PSY / "cloud_cache" / "cache.tgz"
INC_CACHE = PSY / "result" / "incidents" / "api_cache.json.gz"
API = "https://www.googleapis.com/youtube/v3"

CHANNEL_QUERIES = ["심리학", "심리", "정신과 의사", "심리상담", "마음 심리"]   # 5번 ≈ 500단위
PSY_TITLE = re.compile(r"심리|정신과|정신건강|나르시시|자존감|인간관계|우울|불안|트라우마|가스라이팅|애착|소시오|사이코패스|공황|"
                       r"멘탈|감정|상처|외로움|마음")
PSY_NAME = re.compile(r"심리|마음|정신과|정신건강|멘탈|상담|마인드|psych|감정|트라우마|자존감|뇌과학|뇌부자", re.I)
# Claude 가 본 주제 밖 채널 (이름·영상이 심리 낱말에 걸렸지만 심리 채널이 아님) — 까닭과 함께
NOT_PSY = {
    "KBO": "야구", "티몬과품바 X 포캣멍GO": "반려동물", "쓰까르": "먹방", "톡쏘능": "반려견 예능", "SUNBA선바": "게임",
    "미우새": "예능", "play 채널A": "종합 예능", "MBN Entertainment": "종합 예능", "조승연의 탐구생활": "교양 종합",
    "KBS Entertain": "예능", "KBS Drama": "드라마", "IVE": "가수", "SBS TV동물농장x애니멀봐": "동물",
}
MIN_SUBS = 10_000
BROADCAST = re.compile(r"News|뉴스|YTN|MBC|KBS|SBS|JTBC|tvN|채널A|채널아하|EBS|라디오|TV조선|MBN|연합|엠뚜루마뚜루|디글|교양 Voyage|"
                       r"JTBC|Voyage|STORY|티비엔", re.I)
RELIGION = re.compile(r"스님|불교|BTN|붓다|법륜|목사|교회|신부|영성|명상|법문|선원")

log = logging.getLogger("psych_channels")


def L(stage: str, level: int = logging.INFO, **kv) -> None:
    log.log(level, " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if not isinstance(v, str) or ' ' in v else v}"
                            for k, v in kv.items()), extra={"stage": stage})


class F(logging.Formatter):
    def format(self, r):
        lv = "" if r.levelno == logging.INFO else f" level={r.levelname}"
        return f"[{getattr(r, 'stage', 'MAIN')}] [{datetime.now():%Y-%m-%dT%H:%M:%S}]{lv} {r.getMessage()}"


class YT:
    COST = {"search": 100, "channels": 1}

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
        self.units += self.COST.get(endpoint, 1)
        if r.status_code != 200:
            L("LOAD", logging.WARNING, error=f"http{r.status_code}", endpoint=endpoint, body=r.text[:150],
              next_step="할당량이면 한국 17시 뒤 run 다시")
            return None
        d = r.json()
        if endpoint == "search":
            d = {"items": [{"id": it["id"], "snippet": {k: it["snippet"].get(k) for k in ("title", "description")}}
                           for it in d.get("items", [])]}
        else:
            d = {"items": [{"id": it["id"], "snippet": {k: it.get("snippet", {}).get(k) for k in
                                                        ("title", "description", "publishedAt", "country")},
                            "statistics": it.get("statistics", {})} for it in d.get("items", [])]}
        self.cache[h] = d
        self.dirty = True
        return d

    def save(self):
        if self.dirty:
            OUT_DIR.mkdir(parents=True, exist_ok=True)
            API_CACHE.write_bytes(gzip.compress(json.dumps(self.cache, ensure_ascii=False).encode(), mtime=0))


def load_known() -> tuple[dict, dict]:
    """채널 정보(id → dict)와 채널별 영상 통계(id → n, psy, top)."""
    chans, vids = {}, {}
    if PSY_TGZ.exists():
        with tarfile.open(PSY_TGZ) as tf:
            for m in tf.getmembers():
                if not (m.isfile() and m.name.endswith(".json") and "/.cache/" in m.name):
                    continue
                d = json.load(io.TextIOWrapper(tf.extractfile(m), encoding="utf-8"))
                if m.name.endswith("/channels.json"):
                    for cid, c in d.items():
                        chans[cid] = {"title": c.get("title"), "subs": c.get("subs"), "videos": c.get("videos"),
                                      "views": c.get("views"), "created": (c.get("created") or "")[:10],
                                      "country": c.get("country"), "desc": ""}
                elif isinstance(d, dict) and "channel_id" in d:
                    vids[d["id"]] = {"cid": d["channel_id"], "title": d["title"], "views": d.get("view_count") or 0,
                                     "ok": not (d.get("live") or d.get("was_live")) and (d.get("duration") or 0) >= 240}
    if INC_CACHE.exists():
        for v in json.loads(gzip.decompress(INC_CACHE.read_bytes())).values():
            for it in v.get("items", []):
                sn, cd = it.get("snippet", {}), it.get("contentDetails")
                if cd is None or "channelId" not in sn:
                    continue
                m = re.fullmatch(r"P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", cd.get("duration") or "")
                sec = sum(int(x or 0) * k for x, k in zip(m.groups(), (86400, 3600, 60, 1))) if m else 0
                vids.setdefault(it["id"], {"cid": sn["channelId"], "title": sn.get("title", ""),
                                           "views": int(it.get("statistics", {}).get("viewCount", 0)),
                                           "ok": sn.get("liveBroadcastContent", "none") == "none" and sec >= 240})
    agg = defaultdict(lambda: {"n": 0, "psy": 0, "top": ("", 0)})
    for v in vids.values():
        if not v["ok"]:
            continue
        a = agg[v["cid"]]
        a["n"] += 1
        if PSY_TITLE.search(v["title"]):
            a["psy"] += 1
            if v["views"] > a["top"][1]:
                a["top"] = (v["title"], v["views"])
    L("LOAD", source="psychology cache + incidents cache", channels_known=len(chans), videos=len(vids),
      channels_with_videos=len(agg))
    return chans, agg


def load_search(yt: YT, chans: dict) -> set:
    found, desc = set(), {}
    for q in CHANNEL_QUERIES:
        d = yt.get("search", part="snippet", q=q, type="channel", maxResults=50, regionCode="KR", relevanceLanguage="ko")
        for it in (d or {}).get("items", []):
            cid = it["id"].get("channelId")
            if cid:
                found.add(cid)
                desc[cid] = it["snippet"].get("description") or ""
    need = sorted(found)
    for i in range(0, len(need), 50):
        d = yt.get("channels", part="snippet,statistics", id=",".join(need[i:i + 50]), maxResults=50)
        for it in (d or {}).get("items", []):
            sn, st = it["snippet"], it["statistics"]
            chans[it["id"]] = {"title": sn.get("title"), "subs": None if st.get("hiddenSubscriberCount") else
                               int(st.get("subscriberCount", 0)), "videos": int(st.get("videoCount", 0)),
                               "views": int(st.get("viewCount", 0)), "created": (sn.get("publishedAt") or "")[:10],
                               "country": sn.get("country"), "desc": (sn.get("description") or desc.get(it["id"], ""))[:300]}
    L("LOAD", source="search type=channel (KR, ko)", queries=CHANNEL_QUERIES, channels_found=len(found),
      api_calls=yt.calls, units=yt.units, cache_hits=yt.hits)
    return found


def classify(chans: dict, agg: dict, found: set) -> list[dict]:
    rows, dropped = [], defaultdict(int)
    for cid, c in chans.items():
        a = agg.get(cid, {"n": 0, "psy": 0, "top": ("", 0)})
        if cid not in found and a["psy"] == 0:
            continue
        title = c.get("title") or ""
        if title in NOT_PSY:
            dropped["not_psy"] += 1
            continue
        if c.get("country") not in (None, "", "KR"):
            dropped["foreign"] += 1
            continue
        if not c.get("subs") or int(c["subs"]) < MIN_SUBS:
            dropped["small_or_hidden"] += 1
            continue
        in_name = bool(PSY_NAME.search(title))
        in_desc = bool(PSY_NAME.search(c.get("desc") or ""))
        by_videos = a["psy"] >= 3 and a["psy"] / max(a["n"], 1) >= 0.6
        if not (in_name or in_desc or a["psy"] >= 3):
            dropped["weak"] += 1
            continue
        if RELIGION.search(title) or RELIGION.search(c.get("desc") or ""):
            kind = "종교·명상"
        elif BROADCAST.search(title):
            kind = "종합(심리 영상 자주)"
        elif in_name or (in_desc and (by_videos or cid in found)):
            kind = "심리 전문"
        elif a["psy"] >= 3:
            kind = "종합(심리 영상 자주)"
        else:
            dropped["weak"] += 1
            continue
        rows.append({"cid": cid, "title": title, "subs": int(c["subs"]), "videos": c.get("videos"),
                     "views": c.get("views"), "created": c.get("created", "")[:4],
                     "kind": kind,
                     "psy": a["psy"], "n": a["n"], "top_title": a["top"][0], "top_views": a["top"][1],
                     "from": "검색" if cid in found else "영상"})
    rows.sort(key=lambda r: -r["subs"])
    L("CLASSIFY", kept=len(rows), specialist=sum(r["kind"] == "심리 전문" for r in rows), **{f"drop_{k}": v for k, v in dropped.items()})
    return rows


def n(x):
    if x is None:
        return "-"
    x = float(x)
    return f"{x / 1e8:.1f}억" if x >= 1e8 else (f"{x / 1e4:,.1f}만" if x >= 1e4 else f"{x:,.0f}")


def export(rows: list[dict], yt: YT, t0: float) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUT_DIR / "psych_channels.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    out = ["# 심리 관련 채널 — 구독자 많은 순", "",
           f"VERSION: {VERSION} — 도구 `psychology/source/psych_channels.py` · 사용자 지시 2026-11-23 \"심리 관련 구독자 많은순으로 채널 알려줘\"", "",
           "## 0. 읽는 법", f"- 자료: 심리 분석 캐시 + 사건 사례 검색 캐시의 영상·채널 + 채널 검색 {len(CHANNEL_QUERIES)}개 ({' · '.join(CHANNEL_QUERIES)}).",
           "- **심리 전문** = 채널 이름에 심리 낱말(심리·마음·정신과·멘탈·상담·감정…) — 또는 채널 설명에 심리 낱말이 있고 우리 자료 영상도 심리 쪽.",
           "- **종합** = 방송사·교양·책 채널처럼 심리 영상을 자주(3개 이상) 올리지만 심리만 하지는 않는 채널 (방송사 이름은 늘 여기).",
           "- **종교·명상** = 스님·불교·명상 채널 (마음·관계 영상이 많지만 심리 분석 때 주제 밖으로 뺀 갈래).",
           "- '심리 영상'은 **우리가 모은 영상만** 센 것 — 채널 전체 영상 수가 아님. 구독자는 받은 날 값(앞 3자리 반올림).",
           f"- 구독자 {MIN_SUBS:,}명 미만·해외·주제 밖(Claude 가 본 {len(NOT_PSY)}곳 — 야구·먹방·예능 등)은 뺌.", ""]
    for no, kind in enumerate(("심리 전문", "종합(심리 영상 자주)", "종교·명상"), 1):
        rs = [r for r in rows if r["kind"] == kind]
        note = " — 심리 분석 때 주제 밖(종교)으로 뺀 갈래" if kind == "종교·명상" else ""
        out += [f"## {no}. {kind} ({len(rs)}곳){note}", "",
                "| # | 채널 | 구독자 | 영상 수 | 총 조회수 | 개설 | 우리 자료 심리 영상 | 대표 심리 영상 (조회수) |", "|---|---|---|---|---|---|---|---|"]
        for i, r in enumerate(rs[:60], 1):
            top = r["top_title"].replace("|", "／")[:60] if r["top_title"] else "-"
            out.append(f"| {i} | [{r['title']}](https://www.youtube.com/channel/{r['cid']}) | {n(r['subs'])} | {r['videos'] or '-'} | "
                       f"{n(r['views'])} | {r['created']} | {r['psy']}/{r['n']} | {top} ({n(r['top_views']) if r['top_views'] else '-'}) |")
        out.append("")
    out.append(f"_API {yt.calls}번 · {yt.units}단위 · 캐시 {yt.hits}번 · {time.time() - t0:.1f}초_")
    (OUT_DIR / "psych_channels.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    L("EXPORT", md=str((OUT_DIR / "psych_channels.md").relative_to(PSY.parent)), rows=len(rows))


def main(argv) -> int:
    h = logging.StreamHandler(sys.stdout)
    h.setFormatter(F())
    log.handlers[:] = [h]
    log.setLevel(os.environ.get("LOG_LEVEL", "INFO").upper())
    cmd = argv[1] if len(argv) > 1 else "analyze"
    t0 = time.time()
    L("START", tool=f"psych_channels.py {VERSION}", cmd=cmd)
    yt = YT(next((os.environ[k].strip() for k in ("PSYCHOLOGY_YOUTUBE_API_KEY", "YOUTUBE_API_KEY_PSYCHOLOGY", "YOUTUBE_API_KEY") if os.environ.get(k, "").strip()), ""), offline=(cmd != "run"))
    chans, agg = load_known()
    found = load_search(yt, chans)
    yt.save()
    rows = classify(chans, agg, found)
    if not rows:
        L("RESULT", logging.WARNING, error="0 rows", next_step="run 으로 채널 검색")
        return 1
    export(rows, yt, t0)
    L("RESULT", seconds=round(time.time() - t0, 1), api_units=yt.units)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
