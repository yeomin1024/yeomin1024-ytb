#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-11-25 — 신규: 다음 심리 영상 주제 탐색 (많이 본 영상 + 최근 7일 댓글 · 큰 채널 주제 · 성공 대리 지표 · 겹침 · 트렌드 묶음)
#   사용자 지시 2026-11-25 "1. 관심 높은 키워드 … 2. 시청자 많이 본 영상 탐색 … 3. 구독자 많은 채널이 많이 다루는 주제 … 4. 어떤 주제가 시청자들에게
#   성공적으로 추천됐는지 …" → "2번에서 최근 7일 동안으로 변경하고 최근 댓글 수로 무게를 주도록 해 그리고 시청자들이 이미 알고 있는 내용, 즉 비슷한
#   주제로 많이 시청한 영상과 겹치면 안돼니까 확인해야해 트렌드 사이트 허용했으니 탐색해서 주제 여러 개 알려줘봐".
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.0 | 2026-11-25 | (같은 날 고침) 주제 묶음·심리 비중은 제목만 (태그가 묶음을 흐림) · 2-1-1 올린 지 90일+ 영상만 · 뉴스·음악·콩트 거름 | report · big_tables · related |
# | v1.0 | 2026-11-25 | 최초 — recent(조회수 상위 + 최근 7일 댓글 수 무게) · big(구독자 10만+ 심리 채널 최근 1년 주제·채널 안 상대 조회수) · proxies(좋아요÷조회수 등 대리 지표) · overlap(이미 많이 본 영상) · trends(구글 트렌드 묶음·CSV 합치기) · report | 전부 |
"""다음 심리 영상 주제 탐색 — 숫자와 원문만 만든다 (주제 판단은 이 결과를 읽는 Claude 가 `next_topic.md` 에).

자료
  - psychology/cloud_cache/cache.tgz — 지난 탐색(2026-11-11)의 영상 3,238개(제목·설명·태그·길이·조회수·좋아요·댓글 수)·채널 1,585곳·유튜브 자동완성
  - psychology/result/outliers/compare.csv — 주제 묶음(theme)·주제 밖 표시(exclude)·성공 사례 표시(success)
  - YouTube Data API (키 = 환경 변수 YOUTUBE_API_KEY — 출력하지 않음): commentThreads(최신순) · channels · playlistItems · videos

명령
  recent   2번 — 주제 관련 4분+ 영상을 조회수 큰 순으로 N개(기본 300) → 최신 댓글 최대 500개 → 최근 7일 댓글 수 = 무게 (7일 안 댓글 0 이면 대상 밖)
  big      3번 — 구독자 10만+ · 주제 관련 영상 3개+ 채널 → 최근 365일 업로드 전부 → 심리 비중 30%+ 채널만 '심리 큰 채널' → 주제별 채널 수·채널 안 상대 조회수
  report   4번 대리 지표(좋아요÷조회수 · 댓글÷조회수 · 조회수÷구독자 — 같은 구독자 구간 안에서) · 겹침(주제마다 가장 많이 본 영상) · 자동완성 · 트렌드 묶음
  trends   사용자가 받은 구글 트렌드 CSV(psychology/result/next_topic/trends/*.csv) → 기준 낱말로 묶음끼리 이어 붙인 관심도 순위
결과: psychology/result/next_topic/ (recent.json.gz · big.json.gz · next_topic_data.md · trends_batches.md · trends.md)

한계 — 다른 채널 영상의 클릭률·시청 지속률·트래픽 소스(홈 피드/검색)는 공개 API 로 볼 수 없다 → 대리 지표(추정)만.
  주제 묶음은 제목·태그 낱말 규칙(형태소 분석 아님 — 한 영상이 여러 묶음에 들 수 있음). 연구·교육용 도구 — 심리 진단·치료가 아님.
실행 예: python3 psychology/source/next_topic.py recent --top 300 && python3 psychology/source/next_topic.py big && python3 psychology/source/next_topic.py report
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
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PSY = ROOT / "psychology"
OUT = PSY / "result" / "next_topic"
CACHE_TGZ = PSY / "cloud_cache" / "cache.tgz"
COMPARE = PSY / "result" / "outliers" / "compare.csv"
API = "https://www.googleapis.com/youtube/v3/"
VERSION = "v1.0"

RECENT_DAYS = 7          # 사용자 지시 2026-11-25 "2번에서 최근 7일 동안으로 변경"
MAX_COMMENT_PAGES = 5    # 최신 댓글 100개씩 최대 5쪽 (7일 안 댓글이 500개 넘으면 '500+')
BIG_MIN_SUBS = 100_000   # 3번 '구독자 많은 채널' = 10만 이상 (사용자에게 말한 기본값)
BIG_MIN_TOPIC_VIDEOS = 3 # 지난 탐색에서 주제 관련 영상이 3개 이상 나온 채널만 후보
BIG_PSY_SHARE = 0.15     # 최근 1년 롱폼 중 좁은 심리 낱말(PSY_STRICT) 제목 15%+ = 심리 큰 채널 (30% 로는 책과삶·세바시·김창옥TV 같은 마음 강연 채널이 빠짐 — 2026-11-25 분포를 보고 정함)
BROADCAST = re.compile(r"tvn|jtbc|mbc|sbs|kbs|ebs|채널a|mbn|btn|drama|voyage|\bent\b|개그|예능|엠뚜루|디글|비보", re.I)   # 방송사 클립 채널은 뺌
BIG_DAYS = 365
LONG_SEC = 240           # 4분 이상 = 롱폼
MEGA_VIEWS = 1_000_000   # 겹침: 같은 묶음에 100만+ 영상이 있으면 '이미 많이 본 내용' 후보
log = logging.getLogger("next_topic")

# 주제 묶음 — 제목 + 태그 (소문자) 에 낱말 규칙. 순서 = 표 순서.
TOPICS = [
    ("나르시시스트", r"나르|자기애성"),
    ("가스라이팅", r"가스라이팅"),
    ("소시오·사이코패스", r"소시오|사이코패스"),
    ("손절·거리 두기", r"손절|거리\s?두|멀리\s?해야|끊어야|정리해야|걸러야|피해야"),
    ("무례한 사람 대처", r"무례|선\s?넘|무시하는|말을? 함부로|기분 나쁘게"),
    ("말투·대화법", r"말투|대화법|말하는 법|화법|말버릇|말하기|한마디"),
    ("자존감", r"자존감"),
    ("열등감·질투", r"열등감|질투|시기심|비교하"),
    ("눈치·거절 못함", r"눈치|착한\s?아이|거절|호구|착한 사람"),
    ("불안·걱정", r"불안|걱정|초조"),
    ("우울", r"우울"),
    ("공황", r"공황"),
    ("ADHD", r"adhd"),
    ("번아웃·무기력", r"번아웃|무기력|의욕"),
    ("미루기·게으름", r"미루|게으"),
    ("외로움·혼자", r"외로|혼자|고독"),
    ("애착·회피형", r"애착|회피형|불안형"),
    ("연애·이별", r"연애|이별|헤어|짝사랑|재회|썸"),
    ("부부·결혼", r"부부|남편|아내|결혼|이혼"),
    ("엄마·부모", r"엄마|부모|아버지|아빠|어머니"),
    ("시댁·고부", r"시댁|시어머니|며느리|장모|처가|고부"),
    ("자녀·육아", r"자녀|육아|아들|딸|아이를|사춘기"),
    ("형제·가족", r"형제|자매|가족|친척"),
    ("친구", r"(?<![여남자])친구|우정"),
    ("직장·상사", r"직장|회사|상사|동료|팀장|출근"),
    ("트라우마·어린 시절", r"트라우마|어린\s?시절|내면\s?아이|상처"),
    ("분노·화", r"분노|화가 나|화를 내|화내|짜증|욱하|열받"),
    ("감정 조절", r"감정\s?조절|감정을|감정이"),
    ("예민함", r"예민|민감|hsp"),
    ("내향·외향", r"내향|외향|내성적|소심"),
    ("MBTI·성격 유형", r"mbti|성격\s?유형|에니어그램|infp|intj|enfp"),
    ("심리테스트", r"심리\s?테스트|테스트"),
    ("속마음·행동 읽기", r"거짓말|속마음|표정|몸짓|행동으로|심리 읽|꿰뚫"),
    ("뇌과학·도파민", r"뇌과학|뇌가|도파민|뇌를"),
    ("습관·자기 관리", r"(?<!투자 )습관|루틴|자기\s?관리"),
    ("수면", r"수면|불면|잠이|잠을"),
    ("행복·인생", r"행복|인생|삶의|잘 사는"),
    ("나이 듦·노년", r"노후|노년|나이\s?들|늙|중년|[456]0대"),
    ("돈·소비 심리", r"(?<![떼])돈[을이은 ]|부자|소비|가난|돈 관리"),
    ("범죄 심리", r"범죄|살인(?!디)|프로파일|연쇄"),
    ("멘탈·마음가짐", r"멘탈|마음가짐|마음공부|마음 다스"),
]
TOPIC_RX = [(n, re.compile(rx, re.I)) for n, rx in TOPICS]
# 주제 관련(compare.csv)이어도 심리 정보 영상이 아닌 것 — 뉴스·음악·게임·브이로그·콩트·예능 클립 (2026-11-25 조회수 상위 320개 제목을 Claude 가 읽고 정함)
NOISE_TITLE = re.compile(r"음악|music|playlist|플레이리스트|노래|bgm|asmr|브이로그|vlog|뉴스|게임|웹드라마|드라마|ㅋㅋ|\[순풍|여돌|kpop|자장가|백색소음|명상음악", re.I)
NOISE_CHANNEL = re.compile(r"뉴스|news|보물섬|흔한남매|별놈들|준우|총몇명|김더티|동네친구|다나나|빽능|방울이|프롬아블|락카페|klab|픽고|미우새|동상이몽|예능|왕자", re.I)
# 심리 채널 가려내기용 (좁게) — 가족·돈·인생 같은 넓은 낱말은 방송·예능 제목에도 흔해서 뺌
PSY_STRICT = re.compile(r"심리|정신과|정신건강|상담|마음|감정|자존감|불안|우울|공황|adhd|트라우마|나르|가스라이팅|애착|회피형|번아웃|무기력|멘탈|뇌과학|성격|인간관계|손절|사이코패스|소시오", re.I)
PSY_RX = re.compile("|".join(rx for _, rx in TOPICS) + r"|심리|마음|정신과|상담|감정|성격|관계", re.I)


def stamp(stage: str, **kv) -> None:
    log.info("[%s] [%s] %s", stage, time.strftime("%Y-%m-%dT%H:%M:%S"), " ".join(f"{k}={v}" for k, v in kv.items()))


def topics_of(text: str) -> list[str]:
    return [n for n, rx in TOPIC_RX if rx.search(text)]


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
def load_cache() -> tuple[dict, dict, dict]:
    """cache.tgz → (영상 dict, 채널 dict, 자동완성 dict) — 풀지 않고 메모리에서."""
    vids, chans, auto = {}, {}, {}
    try:
        tf = tarfile.open(CACHE_TGZ, "r:gz")
    except (OSError, tarfile.TarError) as ex:
        raise SystemExit(f"[LOAD] {CACHE_TGZ.relative_to(ROOT)} 를 읽지 못함 ({ex}) — cloud_run.py psychology resume 으로 캐시를 먼저")
    with tf:
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
    rows = {r["id"]: r for r in csv.DictReader(open(COMPARE, encoding="utf-8-sig"))}
    for vid, v in vids.items():
        r = rows.get(vid, {})
        v["theme"], v["exclude"], v["success"] = r.get("theme", ""), r.get("exclude", "주제 밖(compare 없음)"), r.get("success") == "True"
        v["in_compare"] = r.get("in_compare") == "True"
        v["subs"] = (chans.get(v.get("channel_id"), {}) or {}).get("subs") or 0
    stamp("LOAD", videos=len(vids), channels=len(chans), autocomplete_seeds=len(auto), cache_saved=json.loads(
        (PSY / "cloud_cache" / "cache.json").read_text("utf-8")).get("saved", "?"))
    return vids, chans, auto


def related(vids: dict) -> list[dict]:
    """주제 관련 롱폼 — compare.csv 에서 뺀 것(주제 밖·외국·라이브·타로)이 아니고 4분 이상 · 뉴스·음악·콩트·예능 클립(NOISE_*)이 아님."""
    base = [v for v in vids.values() if v["exclude"] == "" and (v.get("duration") or 0) >= LONG_SEC and not v.get("live")]
    keep = [v for v in base if not NOISE_TITLE.search(v["title"]) and not NOISE_CHANNEL.search(v.get("channel") or "")]
    if not getattr(related, "_logged", False):
        stamp("FILTER", related_long=len(base), kept=len(keep), noise=len(base) - len(keep), rule="NOISE_TITLE·NOISE_CHANNEL (뉴스·음악·콩트·예능)")
        related._logged = True
    return keep


# ─────────── API ───────────
class Api:
    def __init__(self):
        self.key = os.environ.get("YOUTUBE_API_KEY", "")
        if not self.key:
            raise SystemExit("[API] YOUTUBE_API_KEY 없음 — 환경 변수로 넣는다 (값은 출력하지 않음)")
        self.units = 0

    COST = {"search": 100}       # YouTube 할당량 단위 (그 밖의 list 는 1)

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
                    raise SystemExit(f"[API] 할당량 끝 ({ep}) — 한국 17시 뒤 다시 (지금까지 {self.units}단위)")
                if e.code in (429, 500, 503) and attempt < 3:
                    time.sleep(2 ** attempt * 3)
                    continue
                raise SystemExit(f"[API] {ep} HTTP {e.code} {reason} — 입력 {params.get('videoId') or params.get('id') or params.get('playlistId')} · 다음: 잠시 뒤 다시")
            except (urllib.error.URLError, TimeoutError) as e:
                if attempt < 3:
                    time.sleep(2 ** attempt * 3)
                    continue
                raise SystemExit(f"[API] {ep} 네트워크 실패 ({type(e).__name__}) — 프록시·인터넷 확인 뒤 다시")
        return {}


def save_gz(name: str, obj) -> Path:
    OUT.mkdir(parents=True, exist_ok=True)
    p = OUT / name
    with gzip.open(p, "wt", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False)
    return p


def load_gz(name: str, default=None):
    p = OUT / name
    if not p.exists():
        return default
    with gzip.open(p, "rt", encoding="utf-8") as f:
        return json.load(f)


# ─────────── 2. 많이 본 영상 + 최근 7일 댓글 ───────────
def cmd_recent(a) -> int:
    vids, _, _ = load_cache()
    pool = sorted(related(vids), key=lambda v: -(v.get("view_count") or 0))[: a.top]
    stamp("RECENT", pool=len(pool), rule=f"주제 관련 4분+ · 조회수 큰 순 {a.top}개 (올린 날짜 상관없음)",
          views_min=pool[-1]["view_count"] if pool else 0, window_days=RECENT_DAYS)
    old = load_gz("recent.json.gz", {}) or {}
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
                latest = max(latest or s["publishedAt"], s["publishedAt"])      # 고정 댓글이 맨 앞에 올 수 있어 최댓값
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
            save_gz("recent.json.gz", {"asof": now_utc().isoformat(timespec="seconds"), "window_days": RECENT_DAYS, "videos": res})
    meta = {v["id"]: {k: v.get(k) for k in ("title", "channel", "channel_id", "published", "duration", "view_count", "like_count",
                                              "comment_count", "subs", "theme", "success", "tags")} for v in pool}
    save_gz("recent.json.gz", {"asof": now_utc().isoformat(timespec="seconds"), "window_days": RECENT_DAYS, "top": a.top,
                               "videos": res, "meta": meta, "tool": f"next_topic.py {VERSION}"})
    alive = [k for k, r in res.items() if r["recent7"] > 0]
    stamp("RECENT", status="done", units=api.units, videos=len(res), with_recent7=len(alive),
          recent7_total=sum(r["recent7"] for r in res.values()), disabled=sum(r["disabled"] for r in res.values()))
    return 0


# ─────────── 3. 큰 채널 ───────────
def cmd_big(a) -> int:
    vids, chans, _ = load_cache()
    cnt = defaultdict(int)
    for v in related(vids) + [v for v in vids.values() if v["exclude"] == "" and (v.get("duration") or 0) < LONG_SEC]:
        cnt[v["channel_id"]] += 1
    cands = sorted([c for c, n in cnt.items() if n >= BIG_MIN_TOPIC_VIDEOS and ((chans.get(c) or {}).get("subs") or 0) >= BIG_MIN_SUBS],
                   key=lambda c: -chans[c]["subs"])
    stamp("BIG", candidates=len(cands), rule=f"구독자 {BIG_MIN_SUBS:,}+ · 지난 탐색 주제 관련 영상 {BIG_MIN_TOPIC_VIDEOS}+")
    api = Api()
    old = load_gz("big.json.gz", {}) or {}
    data = old.get("channels", {}) if old.get("asof", "")[:10] == now_utc().strftime("%Y-%m-%d") else {}
    up = {}
    for k in range(0, len(cands), 50):
        j = api.get("channels", part="contentDetails", id=",".join(cands[k:k + 50]), maxResults=50)
        for it in j.get("items", []):
            up[it["id"]] = it["contentDetails"]["relatedPlaylists"]["uploads"]
    cut = now_utc() - dt.timedelta(days=BIG_DAYS)
    for i, c in enumerate(cands, 1):
        if c in data or c not in up:
            continue
        ids, token, pages = [], None, 0
        while pages < 8:
            p = {"part": "contentDetails", "playlistId": up[c], "maxResults": 50}
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
                rows.append({"id": it["id"], "title": sn["title"], "tags": sn.get("tags", [])[:30], "published": sn["publishedAt"],
                             "dur": iso_dur(it["contentDetails"].get("duration", "")), "views": int(stt.get("viewCount", 0) or 0),
                             "likes": int(stt.get("likeCount", 0) or 0), "comments": int(stt.get("commentCount", 0) or 0),
                             "live": sn.get("liveBroadcastContent", "none") != "none"})
        data[c] = {"title": chans[c].get("title"), "subs": chans[c]["subs"], "videos": rows}
        if i % 10 == 0:
            stamp("BIG", done=i, of=len(cands), units=api.units)
            save_gz("big.json.gz", {"asof": now_utc().isoformat(timespec="seconds"), "channels": data})
    save_gz("big.json.gz", {"asof": now_utc().isoformat(timespec="seconds"), "channels": data, "tool": f"next_topic.py {VERSION}",
                            "rule": {"min_subs": BIG_MIN_SUBS, "min_topic_videos": BIG_MIN_TOPIC_VIDEOS, "days": BIG_DAYS, "psy_share": BIG_PSY_SHARE}})
    stamp("BIG", status="done", units=api.units, channels=len(data), videos=sum(len(d["videos"]) for d in data.values()))
    return 0


# ─────────── 4. 대리 지표 · 겹침 · 자동완성 · 트렌드 묶음 · 보고 ───────────
def band(subs: int) -> str:
    return "1만 미만" if subs < 10_000 else "1만~10만" if subs < 100_000 else "10만~50만" if subs < 500_000 else "50만+"


def med(xs, default=0.0):
    xs = [x for x in xs if x is not None]
    return st.median(xs) if xs else default


def fmt(n) -> str:
    n = float(n)
    return f"{n / 1e4:,.1f}만" if n >= 1e4 else f"{n:,.0f}"


def big_tables(big: dict) -> tuple[list[str], dict, list[dict]]:
    """심리 큰 채널만 → 주제별 채널 수·영상 수·채널 안 상대 조회수 (가운데값·1.5배+ 몫)."""
    lines, by_topic, allv = [], defaultdict(list), []
    psy_ch = []
    now = now_utc()
    for c, d in big.get("channels", {}).items():
        long = [v for v in d["videos"] if v["dur"] >= LONG_SEC and not v["live"]]
        if not long:
            continue
        share = sum(1 for v in long if PSY_STRICT.search(v["title"])) / len(long)     # 제목만 (방송·뉴스 채널의 태그가 심리 낱말을 잔뜩 품고 있음)
        if share < BIG_PSY_SHARE or BROADCAST.search(d["title"] or ""):
            continue
        aged = [v for v in long if (now - parse_ts(v["published"])).days >= 14]
        m = med([v["views"] for v in aged]) or 1
        psy_ch.append((d["title"], d["subs"], len(long), share, m))
        for v in aged:
            v2 = dict(v, rel=v["views"] / m, ch=d["title"], subs=d["subs"])
            allv.append(v2)
            for t in topics_of(v["title"]):
                by_topic[t].append(v2)
    psy_ch.sort(key=lambda x: -x[1])
    lines += [f"심리 큰 채널 {len(psy_ch)}곳 (구독자 10만+ · 최근 1년 롱폼 중 심리 낱말(PSY_STRICT) 제목 {BIG_PSY_SHARE:.0%}+ · 방송사 클립 채널 뺌): " +
              " · ".join(f"{n} {fmt(s)}({k}편·{sh:.0%})" for n, s, k, sh, _ in psy_ch), ""]
    lines += ["| 주제 | 다룬 큰 채널 수 | 영상 수 | 채널 안 상대 조회수 가운데값 | 채널 평소의 1.5배+ 몫 | 가장 잘 된 영상 (상대·조회수·채널) |", "|---|---|---|---|---|---|"]
    stats = {}
    for t, _ in TOPICS:
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
    return lines, stats, allv


def cmd_report(a) -> int:
    vids, chans, auto = load_cache()
    rel = related(vids)
    rec = load_gz("recent.json.gz", {}) or {}
    big = load_gz("big.json.gz", {}) or {}
    L = ["# 다음 심리 영상 주제 탐색 — 자료 (숫자·원문만)", "",
         f"> `psychology/source/next_topic.py` {VERSION} · {time.strftime('%Y-%m-%d %H:%M')} · 사용자 지시 2026-11-25 (1~4번 + \"2번에서 최근 7일 … 최근 댓글 수로 무게 … 비슷한 주제로 많이 시청한 영상과 겹치면 안돼니까 확인\")",
         f"> 자료: 지난 탐색 캐시(2026-11-11) 주제 관련 롱폼 {len(rel):,}개 · 최근 7일 댓글 {rec.get('asof', '없음')[:16]} · 큰 채널 업로드 {big.get('asof', '없음')[:16]}.",
         "> **한계**: 다른 채널의 클릭률·시청 지속률·트래픽 소스는 공개 API 에 없음 → 아래는 대리 지표(추정). 주제 묶음 = 제목·태그 낱말 규칙(겹침 있음). 인과 아님. 연구·교육용.", ""]

    # 2번 — 최근 7일 댓글 무게
    rv, meta = rec.get("videos", {}), rec.get("meta", {})
    w_topic, n_topic, v_topic, cm_topic = defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(list)
    for vid, r in rv.items():
        m = meta.get(vid) or vids.get(vid) or {}
        ts = topics_of(m.get("title") or "")          # 제목만 — 태그는 채널마다 낱말을 잔뜩 넣어 묶음이 흐려짐 (v1.0 시험에서 확인)
        for t in ts:
            if r["recent7"] > 0:
                w_topic[t] += r["recent7"]
                n_topic[t] += 1
                v_topic[t] += m.get("view_count") or 0
                cm_topic[t] += [dict(c, vid=vid) for c in r["comments"]]
    tot = sum(r["recent7"] for r in rv.values()) or 1
    L += [f"## 2. 많이 본 영상 + 지금도 보는지 — 조회수 상위 {len(rv)}개 중 최근 {RECENT_DAYS}일 댓글이 있는 {sum(1 for r in rv.values() if r['recent7'])}개 (무게 = 최근 7일 댓글 수, 합 {tot:,})", "",
          "| 주제 | 최근 7일 댓글 (무게) | 몫 | 영상 수 (7일 댓글 있음) | 그 영상 조회수 합 |", "|---|---|---|---|---|"]
    for t in sorted(w_topic, key=lambda t: -w_topic[t]):
        L.append(f"| {t} | {w_topic[t]:,} | {w_topic[t] / tot:.0%} | {n_topic[t]} | {fmt(v_topic[t])} |")
    L += ["", "### 2-1. 최근 7일 댓글이 많은 영상 (상위 25)", "", "| 최근 7일 댓글 | 조회수 | 올린 날 | 제목 | 채널 |", "|---|---|---|---|---|"]
    for vid, r in sorted(rv.items(), key=lambda kv: -kv[1]["recent7"])[:25]:
        m = meta.get(vid, {})
        L.append(f"| {r['recent7']}{'+' if r.get('capped') else ''} | {fmt(m.get('view_count') or 0)} | {(m.get('published') or '')[:10]} | {(m.get('title') or '')[:46]} | {m.get('channel', '')} |")
    # 2-1-1 오래된 영상(올린 지 90일+)인데 최근 7일 댓글이 있음 = 지금도 찾아보는 주제 (새 영상은 원래 댓글이 몰림)
    ev_w, ev_n = defaultdict(int), defaultdict(int)
    for vid, r in rv.items():
        m = meta.get(vid) or {}
        if r["recent7"] and m.get("published") and (now_utc() - parse_ts(m["published"])).days >= 90:
            for t in topics_of(m.get("title") or ""):
                ev_w[t] += r["recent7"]
                ev_n[t] += 1
    L += ["", "### 2-1-1. 올린 지 90일 넘은 영상만 — 최근 7일 댓글 (새 영상 효과를 뺀 '지금도 찾아보는' 주제)", "",
          "| 주제 | 최근 7일 댓글 | 영상 수 |", "|---|---|---|"] + [f"| {t} | {ev_w[t]} | {ev_n[t]} |" for t in sorted(ev_w, key=lambda t: -ev_w[t])]
    L += ["", "### 2-2. 주제별 최근 7일 댓글 — 공감 많은 순 5개 (니즈 원문, 작성자 정보 없음)", ""]
    for t in sorted(w_topic, key=lambda t: -w_topic[t])[:16]:
        top = sorted(cm_topic[t], key=lambda c: -c["like"])[:5]
        L.append(f"- **{t}**: " + " / ".join(f"「{c['text'][:90]}」(♥{c['like']})" for c in top))
    stamp("REPORT", part="recent", topics=len(w_topic), weight_total=tot)

    # 3번 — 큰 채널
    bl, bstats, allbig = big_tables(big) if big else (["(big 을 먼저)"], {}, [])
    L += ["", "## 3. 구독자 많은 심리 채널이 많이 다루는 주제 — 최근 1년 롱폼 (상대 조회수 = 그 영상 조회수 ÷ 그 채널 롱폼 가운데값 — 채널 크기를 뺀 주제 힘)", ""] + bl

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
        for t in topics_of(v["title"]):
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
    for t, _ in TOPICS:
        g = agg.get(t)
        if not g or g["n"] < 5:
            continue
        proxy[t] = {"like": med(g["like_i"]), "cmt": med(g["cmt_i"]), "reach": med(g["reach"]), "succ": (g["succ"] / g["cmp"]) if g["cmp"] else None, "n": g["n"]}
        p = proxy[t]
        succ = f"{p['succ']:.0%} ({g['succ']}/{g['cmp']})" if g["cmp"] else "—"
        L.append(f"| {t} | {g['n']} | {p['like']:.2f} | {p['cmt']:.2f} | {p['reach']:.2f} | {succ} | {fmt(med(g['views']))} |")

    # 겹침 — 주제마다 가장 많이 본 영상 (캐시 + 큰 채널 업로드)
    pool = {v["id"]: (v["title"], v.get("view_count") or 0, v.get("channel", ""), (v.get("published") or "")[:10]) for v in rel}
    for v in allbig:
        pool.setdefault(v["id"], (v["title"], v["views"], v["ch"], v["published"][:10]))
    L += ["", f"## 5. 겹침 확인 — 주제마다 가장 많이 본 영상 5개 (시청자가 이미 아는 내용 · 100만+ = ⚠)", ""]
    for t, rx in TOPIC_RX:
        xs = sorted(((tt, vv, ch, pd) for tt, vv, ch, pd in pool.values() if rx.search(tt)), key=lambda x: -x[1])[:5]
        if xs:
            L.append(f"- **{t}**: " + " / ".join(f"{'⚠' if vv >= MEGA_VIEWS else ''}「{tt[:40]}」{fmt(vv)}·{ch}·{pd[:4]}" for tt, vv, ch, pd in xs))

    # 자동완성 (유튜브 검색창 — 지난 탐색 2026-11-11)
    L += ["", "## 6. 유튜브 자동완성 (지난 탐색 2026-11-11 · 검색창에 사람들이 치는 말 — 관심도 보조)", ""]
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
        for t in topics_of(s):
            tcount[t] += 1
    L += ["", "자동완성 안 주제 낱말 수: " + " · ".join(f"{t} {n}" for t, n in sorted(tcount.items(), key=lambda x: -x[1]))]
    save_gz("summary.json.gz", {"recent_w": w_topic, "big": bstats, "proxy": proxy, "auto": tcount, "asof": now_utc().isoformat(timespec="seconds")})
    (OUT / "next_topic_data.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    write_trend_batches()
    stamp("REPORT", status="done", out=(OUT / "next_topic_data.md").relative_to(ROOT), lines=len(L))
    return 0


# ─────────── 겹침 — 후보마다 유튜브 검색 (사용자 지시 "비슷한 주제로 많이 시청한 영상과 겹치면 안돼니까 확인해야해") ───────────
# 후보 = 댓글 요청·최근 7일 댓글·큰 채널 표에서 Claude 가 뽑은 것 (근거는 next_topic.md). q = 시청자가 칠 법한 검색어.
CANDS = [
    ("A", "의자 안 넣고 그냥 가는 사람", ["의자 안 넣는 사람 심리", "의자 그냥 두고 가는 사람"], r"의자"),
    ("B", "필요 없는 걸 자꾸 주는 사람", ["유통기한 지난 선물 주는 사람 심리", "필요없는 물건 자꾸 주는 사람 심리"], r"선물|유통기한|물건을? (자꾸 )?주|떠넘|나눠 ?주|퍼주"),
    ("C", "힘들 때만 연락하는 사람", ["힘들 때만 연락하는 사람 심리", "감정쓰레기통 취급하는 사람"], r"힘들 때만|필요할 때만|감정\s?쓰레기통|하소연"),
    ("D", "말을 부풀리는 사람", ["과장해서 말하는 사람 심리", "말 부풀리는 사람 심리"], r"과장|부풀|허세|뻥|지어내"),
    ("E", "매번 늦는 사람", ["약속 시간에 매번 늦는 사람 심리", "지각하는 사람 심리"], r"늦는|지각"),
    ("F", "아쉬울 때만 친절한 사람", ["사람 봐가며 태도 바꾸는 사람 심리", "필요할 때만 친절한 사람"], r"태도|필요할 때만|아쉬울 때|사람 봐가|강약약강"),
    ("G", "말끝마다 반박하는 사람", ["말끝마다 반박하는 사람 심리", "말꼬리 잡는 사람 심리"], r"반박|말꼬리|토 ?다|딴지|태클"),
    ("H", "자기를 3인칭으로 부르는 사람", ["자기를 3인칭으로 부르는 사람 심리"], r"3인칭|삼인칭|자기 이름"),
    ("I", "불평불만이 입에 붙은 사람", ["불평불만 많은 사람 심리"], r"불평|불만|투덜|부정적인"),
    ("J", "자랑만 하는 친구", ["자랑하는 사람 심리", "만나면 자랑만 하는 친구"], r"자랑"),
    ("K", "얻어먹기만 하는 사람", ["얻어먹기만 하는 사람 심리", "계산할 때 사라지는 사람"], r"얻어먹|계산할 때|밥값|더치|빈대"),
    ("L", "남의 뒷말을 나한테 옮기는 사람", ["말 옮기는 사람 심리", "뒷담화 전하는 사람 심리"], r"말 ?옮기|말을 옮|전하는|이간질"),
    ("M", "자기 얘기만 하는 사람", ["자기 얘기만 하는 사람 심리"], r"자기 (얘기|이야기)만|자기 말만|대화 독점"),
    ("N", "강한 사람에게 약하고 약한 사람에게 강한 사람", ["강약약강 심리"], r"강약약강|강자.*약자|약자.*강"),
]


def cmd_overlap(a) -> int:
    api = Api()
    old = load_gz("overlap.json.gz", {}) or {}
    res = old.get("queries", {})
    for key, name, qs, _core in CANDS:
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
            save_gz("overlap.json.gz", {"asof": now_utc().isoformat(timespec="seconds"), "queries": res})
    L = ["# 겹침 확인 — 후보마다 유튜브 검색 (한국 · 관련성 순 25개 중 제목에 핵심 낱말이 있는 것 = 같은 주제)", "",
         f"> `next_topic.py` {VERSION} · {time.strftime('%Y-%m-%d %H:%M')} · 100만+ = ⚠ (시청자가 이미 많이 본 내용 — 같은 각도면 피함). 검색 1회 = 100단위.", ""]
    summary = {}
    for key, name, qs, core in CANDS:
        allv = {}
        for q in qs:
            for x in res.get(q, []):
                allv[x["id"]] = x
        crx = re.compile(core)
        same = [x for x in allv.values() if crx.search(x["title"])]           # 제목에 그 후보의 핵심 낱말이 있는 것만 = 같은 주제
        lng = sorted([x for x in same if x["dur"] > 180], key=lambda x: -x["views"])
        sht = sorted([x for x in same if x["dur"] <= 180], key=lambda x: -x["views"])
        summary[key] = {"name": name, "same": len(same), "long_max": lng[0]["views"] if lng else 0, "long_n_100k": sum(1 for x in lng if x["views"] >= 100_000),
                        "short_max": sht[0]["views"] if sht else 0, "long_top": lng[:3]}
        L.append(f"## {key}. {name} — 검색어: {' · '.join(qs)} · 핵심 낱말 `{core}` (검색 결과 {len(allv)}개 중 같은 주제 {len(same)}개)")
        L.append("- 롱폼: " + (" / ".join(f"{'⚠' if x['views'] >= MEGA_VIEWS else ''}「{x['title'][:48]}」 {fmt(x['views'])}·{x['ch']}·{x['pub'][:7]}" for x in lng[:5]) or "없음"))
        L.append("- 쇼츠: " + (" / ".join(f"{'⚠' if x['views'] >= MEGA_VIEWS else ''}「{x['title'][:40]}」 {fmt(x['views'])}·{x['ch']}" for x in sht[:3]) or "없음"))
        L.append("")
    save_gz("overlap_summary.json.gz", summary)
    (OUT / "overlap.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    stamp("OVERLAP", status="done", queries=len(res), units=api.units)
    return 0


# ─────────── 1. 구글 트렌드 (유튜브 검색) — 사용자가 받은 CSV ───────────
TREND_ANCHOR = "심리"
TREND_WORDS = ["선물 심리", "허세", "뒷담화", "강약약강", "밥값", "말꼬리", "의자 심리", "자기 얘기만",   # 후보 주제 머리말 (next_topic.md)
               "나르시시스트", "가스라이팅", "손절", "자존감", "열등감", "눈치", "불안", "우울증", "공황장애", "ADHD", "번아웃", "무기력",
               "외로움", "회피형", "애착", "이별", "부부싸움", "엄마", "시어머니", "사춘기", "친구 관계", "직장 상사", "트라우마", "분노조절",
               "예민", "내향인", "MBTI", "심리테스트", "거짓말", "도파민", "습관", "불면증", "행복", "노후", "멘탈", "말투", "인간관계", "소시오패스"]


def write_trend_batches() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "trends").mkdir(exist_ok=True)
    L = ["# 구글 트렌드 묶음 (유튜브 검색 · 한국 · 최근 12개월)", "",
         f"> `next_topic.py` {VERSION} — 이 환경에서 trends.google.com 이 자동 요청에 HTTP 429 (구글이 막음) → 사람이 브라우저로 받는다.",
         f"> 한 번에 5개까지라 묶음마다 기준 낱말 「{TREND_ANCHOR}」를 넣고 4개씩 → 기준 낱말 값으로 묶음끼리 이어 붙인다 (`next_topic.py trends`).",
         "> 받는 법: 주소 열기 → '시간 흐름에 따른 관심도' 오른쪽 위 ⤓(CSV) → 파일 이름을 `batch_NN.csv` 로 → `psychology/result/next_topic/trends/` 에 올리거나 채팅에 붙임.", ""]
    for i in range(0, len(TREND_WORDS), 4):
        words = [TREND_ANCHOR] + TREND_WORDS[i:i + 4]
        q = urllib.parse.quote(",".join(words))
        L.append(f"{i // 4 + 1:02d}. {', '.join(words[1:])} — https://trends.google.com/trends/explore?date=today%2012-m&geo=KR&gprop=youtube&q={q}&hl=ko")
    (OUT / "trends_batches.md").write_text("\n".join(L) + "\n", encoding="utf-8")


def cmd_trends(a) -> int:
    files = sorted((OUT / "trends").glob("*.csv"))
    if not files:
        stamp("TRENDS", level="warn", msg="CSV 없음", next="trends_batches.md 의 주소에서 받아 psychology/result/next_topic/trends/ 에")
        return 1
    score = {}
    for f in files:
        rows = [r for r in csv.reader(io.StringIO(f.read_text("utf-8-sig"))) if r]
        hdr_i = next(i for i, r in enumerate(rows) if len(r) > 1 and re.match(r"(주|Week|월|Month|날짜|Day)", r[0]))
        hdr = [re.sub(r":.*$", "", h).strip() for h in rows[hdr_i]]
        data = rows[hdr_i + 1:]
        cols = {h: [float(re.sub(r"[^\d.]", "", r[j]) or 0) for r in data] for j, h in enumerate(hdr) if j}
        if TREND_ANCHOR not in cols:
            stamp("TRENDS", level="warn", file=f.name, msg=f"기준 낱말 {TREND_ANCHOR} 칸 없음 — 뺌")
            continue
        base = st.mean(cols[TREND_ANCHOR]) or 1
        for h, xs in cols.items():
            if h == TREND_ANCHOR:
                continue
            last = st.mean(xs[-13:]) if len(xs) >= 13 else st.mean(xs)
            prev = st.mean(xs[-26:-13]) if len(xs) >= 26 else last
            score[h] = {"rel": st.mean(xs) / base, "recent_rel": last / base, "trend": (last / prev) if prev else 0, "file": f.name}
    L = ["# 구글 트렌드 — 유튜브 검색 관심도 (기준 「심리」 = 1.00)", "", "| 낱말 | 12개월 평균 (심리 대비) | 최근 3개월 (심리 대비) | 최근 3개월 ÷ 그 전 3개월 | 파일 |", "|---|---|---|---|---|"]
    for h, s in sorted(score.items(), key=lambda kv: -kv[1]["rel"]):
        L.append(f"| {h} | {s['rel']:.2f} | {s['recent_rel']:.2f} | {s['trend']:.2f} | {s['file']} |")
    (OUT / "trends.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    stamp("TRENDS", status="done", words=len(score), files=len(files))
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="다음 심리 영상 주제 탐색 자료")
    ap.add_argument("cmd", choices=["recent", "big", "report", "trends", "overlap"])
    ap.add_argument("--top", type=int, default=300)
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args(argv)
    logging.basicConfig(level=a.log_level, format="%(message)s")
    t0 = time.time()
    rc = {"recent": cmd_recent, "big": cmd_big, "report": cmd_report, "trends": cmd_trends, "overlap": cmd_overlap}[a.cmd](a)
    stamp("DONE", cmd=a.cmd, seconds=round(time.time() - t0, 1))
    return rc


if __name__ == "__main__":
    sys.exit(main())
