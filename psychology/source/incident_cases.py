#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.2.1 — 2026-11-27 — 키: PSYCHOLOGY_YOUTUBE_API_KEY → YOUTUBE_API_KEY_PSYCHOLOGY → YOUTUBE_API_KEY 순서 (주제 접두사 — 사용자 지시 2026-11-27 "주제별 접두사를 변수명에 붙여서 구분되도록해"). 시작할 때 한 번 정함.
# (이전) VERSION: v1.2.0 — 2026-11-23 — '모르는 사이 가스라이팅이 된' 사례 검색어 6개 더함 (QUERIES_GAS) (사용자 지시 2026-11-23
#          "그러니까 1번 심리가 초래한 실제 사례들을 찾아보라고 사람들이 모르고 있지만 그게 가스라이팅이 어느 순간 된거지 그런거")
#          — 분류·지표는 그대로 · 6개 × 기간 2 = 12번 ≈ 1,200단위
# (이전) v1.1.0 — 2026-11-23 — 범위를 '심리가 초래한 사례'로 넓힘 (사용자 지시 2026-11-23 "그냥 꼭 큰 사건, 사고가 아닌
#          심리가 초래한 사례면 되니까 심리에 집중해 계속 진행해"): ① 심리 현상 사례 검색어 8개 더함 (QUERIES_PSY — 인지부조화·
#          확증편향·동조·복종·플라시보·학습된 무기력·집단사고·심리 효과) ② 갈래 kind 에 everyday(일상 실제 사례) · 이름을 심리 쪽으로
#          ③ 규칙 후보 낱말에 사례·실험카메라·이름 붙은 효과·증후군 더함 ④ 보고서 맨 앞을 '심리 개념별'로 (심리에 집중)
#          판정 기준(labels.tsv keep=1): 실제 사례(사건·실험·사람·관찰)를 들고 그 안의 심리를 설명하는 영상 — 수사·재판 뉴스만은 0
# (이전) v1.0.0 — 2026-11-23 — 신규: 심리가 드러난 실제 사건·사고·실험 영상 중 '사람들이 많이 본' 사례 찾기
#          (사용자 지시 2026-11-23 "심리 주제 쪽은 사람들이 가장 관심 있게 본 심리가 반영된 사건, 사고 등 사례를 찾아봐")
"""
incident_cases.py — 심리 주제: 실제 사건·사고·실험(사례)을 다룬 영상 중 조회수·반응이 큰 것 찾기

흐름
  1. LOAD-A   : 심리 분석 캐시(psychology/cloud_cache/cache.tgz — 영상 3,238개, 할당량 0)
                + compare.csv 의 구독자 수
  2. LOAD-B   : 사건 심리를 겨냥한 검색어 QUERIES × 기간 WINDOWS(전체 · 최근 365일)
                search(order=viewCount, regionCode=KR, relevanceLanguage=ko, videoDuration=medium = 4~20분) 50개씩
                → videos · channels 통계. 응답은 result/incidents/api_cache.json.gz 한 파일에 (다시 돌리면 할당량 0)
  3. VALIDATE : 통계 빠짐 · 같은 영상 두 번 · 한글 없는 제목 · 라이브 · 4분 미만 · 미래 날짜 (뺀 수를 로그로)
  4. CLASSIFY : ① 규칙(제목 낱말 CASE_WORDS)으로 '사례 후보' ② Claude 가 제목을 읽고 쓴 labels.tsv 가
                최종 판정 (keep 1 = 실제 사건·사고·실험·사회 이슈를 다룬 영상, 0 = 아님) · 갈래 · 사건 이름 · 심리 개념
                → 판정이 없는 후보는 candidates_todo.tsv (다음에 Claude 가 읽을 것)
  5. METRICS  : 조회수 · 하루 조회수 · 구독자 배수 · 좋아요율 · 성공 사례(심리 analysis_rules.toml [success] 그대로)
                갈래별 · 사건별 · 심리 개념별 묶음 (채널당 상위 3편으로 자른 가운데값 — 한 채널이 덮지 않게)
  6. EXPORT   : result/incidents/incident_cases.md · incident_cases.csv · candidates_todo.tsv

읽는 법 (한계)
  - search(order=viewCount)는 '그 검색어로 조회수 높은 순 50개' = 위쪽 꼬리만 본다. 시장 전체 크기가 아님.
  - 기존 심리 캐시는 심리학·인간관계·자존감 검색어로 모은 것이라 사건 영상이 적게 들어 있다 → LOAD-B 로 보충.
  - 조회수는 채널 크기에 크게 좌우됨 → 큰 채널(방송사)과 작은 채널(구독자 5만 이하)을 나눠 본다.
  - 판정(labels.tsv)은 Claude 가 제목·채널을 읽고 정함 — 대본을 본 것이 아님.

실행:  python3 psychology/source/incident_cases.py run       # 검색(캐시에 없을 때만 API) + 분석
       python3 psychology/source/incident_cases.py analyze   # 캐시만 (할당량 0)
       LOG_LEVEL=DEBUG python3 psychology/source/incident_cases.py analyze
주의: 연구·교육용 분석 — 의료·심리 상담이나 수사 판단이 아니다. 실제 사건을 영상으로 쓸 때는 판결문·공식 보도로
      사실을 다시 확인하고, 피해자·유족 이름과 자극적 묘사를 피한다.
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

import numpy as np
import pandas as pd
import requests

VERSION = "v1.2.1"
SEED = 0  # 무작위 요소 없음 — 재현성 기록용

HERE = Path(__file__).resolve().parent
PSY = HERE.parent                                   # psychology/
OUT_DIR = PSY / "result" / "incidents"
API_CACHE = OUT_DIR / "api_cache.json.gz"
LABELS = OUT_DIR / "labels.tsv"
PSY_CACHE_TGZ = PSY / "cloud_cache" / "cache.tgz"
COMPARE_CSV = PSY / "result" / "outliers" / "compare.csv"
RULES_TOML = PSY / "analysis_rules.toml"
API = "https://www.googleapis.com/youtube/v3"

AS_OF = datetime(2026, 11, 23, tzinfo=timezone.utc)   # 기준일 고정 (재실행해도 '며칠 지났나'가 같음)
MIN_SEC = 240            # 4분 이상 (쇼츠·짧은 클립 빼기 — 심리 성공 기준 MIN_MINUTES 와 같음)
SMALL_SUBS = 50_000      # 작은 채널 (성공 기준과 같은 선)
BIG_SUBS = 1_000_000     # 큰 채널 (방송사 등)
PER_CHANNEL = 3          # 묶음 가운데값은 채널당 조회수 상위 3편까지
RATIO_MIN_SUBS = 1_000   # 구독자 배수 가운데값은 구독자 1,000명 이상 채널만 (옛 영상 재업로드 채널이 배수를 부풀림)
TOP_SHOW = 30            # 조회수 상위 표 길이 (채널당 2편)

# 사건 심리를 겨냥한 검색어 (v1.0.0 — 14개 × 기간 2 = 28번 ≈ 2,800단위)
QUERIES = [
    "범죄심리 사건", "사건 심리 분석", "사회실험 심리", "심리학 실험", "방관자 효과",
    "군중심리 참사", "재난 생존자 심리", "사이비 세뇌 심리", "가스라이팅 사건", "사기꾼 심리",
    "프로파일러 사건 분석", "집단 광기 사건", "스톡홀름 증후군", "사이코패스 실제 사건",
]
# v1.1.0: 심리 현상이 결과를 만든 사례 (사건이 작아도 됨) — 8개 × 기간 2 = 16번 ≈ 1,600단위
QUERIES_PSY = [
    "인지부조화 사례", "확증편향 사례", "동조 실험", "복종 실험", "플라시보 효과",
    "학습된 무기력 실험", "집단사고 사례", "심리 효과 실제 사례",
]
# v1.2.0: 가까운 관계가 어느 순간 가스라이팅이 된 실제 사례
QUERIES_GAS = [
    "가스라이팅 실화", "가스라이팅 당한 줄 몰랐다", "가스라이팅 실제 사례",
    "친구 가스라이팅 사건", "가족 가스라이팅 사건", "가스라이팅 판결",
]
QUERIES = QUERIES + QUERIES_PSY + QUERIES_GAS
WINDOWS = {"all": None, "365d": 365}   # 전체 기간 · 최근 365일

# 제목에 이 낱말이 있으면 '사례 후보' (최종 판정은 labels.tsv — 규칙만으로 정하지 않음)
CASE_WORDS = re.compile(
    r"사건|살인|살해|범죄|범행|범인|참사|재난|실험|그알|그것이 ?알고|미제|연쇄|실종|납치|유괴|인질|테러|방화|"
    r"폭행|학대|사기꾼|사기 ?피해|보이스피싱|사이비|교주|세뇌|JMS|신천지|학폭|학교폭력|스토킹|교제폭력|판결|재판|법정|"
    r"교도소|감옥|수감|사형|프로파일|용의자|피의자|피해자|가해자|생존자|추락|침몰|붕괴|압사|조난|전쟁|학살|버블|투기|"
    r"광기|실화|교통사고|사고 ?현장|사고로|대형 ?사고|참변|희생|유족|스톡홀름|방관자|밀그램|스탠퍼드 ?감옥|스탠포드 ?감옥|"
    r"짐바르도|마약 ?사건|마약|도박|사이코패스|소시오패스|"
    # v1.1.0: 심리가 초래한 사례 쪽 낱말
    r"사례|실험카메라|몰래 ?카메라|관찰 ?카메라|증후군|인지부조화|확증 ?편향|동조|복종|플라시보|위약|노시보|학습된 ?무기력|"
    r"집단 ?사고|매몰 ?비용|(?:방관자|피그말리온|후광|바넘|더닝|낙인|자이가르닉|스포트라이트|밴드왜건|베르테르|파파게노|호손|"
    r"앵커링|프레이밍|링겔만|단순 ?노출|사회적 ?태만|맥락|가르시아|마시멜로|깨진 ?유리창)\s?(?:효과|실험|이론)", re.I)

KINDS = {   # labels.tsv 의 kind 값 → 보고서 이름 (v1.1.0: 심리 쪽 이름 · everyday 더함)
    "experiment": "심리 실험·사회실험",
    "crime": "범죄 속 심리 (실제 사건)",
    "accident": "사고·재난 속 심리",
    "social": "사회 이슈·유명인 사례",
    "history": "역사·기록 속 사례 (집단 광기·투기·전쟁 등)",
    "everyday": "일상 속 실제 사례 (상담·관찰·당사자)",
    "fiction": "영화·드라마 속 사례 (지어낸 이야기)",
    "story": "사연·썰 (진위 확인 어려움)",
}
REAL_KINDS = ["experiment", "crime", "accident", "social", "history", "everyday"]
HANGUL = re.compile(r"[가-힣]")

log = logging.getLogger("incident_cases")


# ─────────────────────────── 로그 ───────────────────────────
class StageFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        ts = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        lv = "" if record.levelno == logging.INFO else f" level={record.levelname}"
        return f"[{getattr(record, 'stage', 'MAIN')}] [{ts}]{lv} {record.getMessage()}"


def setup_logging() -> None:
    h = logging.StreamHandler(sys.stdout)
    h.setFormatter(StageFormatter())
    log.handlers[:] = [h]
    log.setLevel(os.environ.get("LOG_LEVEL", "INFO").upper())


def kv(**items) -> str:
    out = []
    for k, v in items.items():
        s = v if isinstance(v, str) else json.dumps(v, ensure_ascii=False, default=str)
        if isinstance(v, str) and (" " in v or "=" in v or v == ""):
            s = json.dumps(v, ensure_ascii=False)
        out.append(f"{k}={s}")
    return " ".join(out)


def L(stage: str, level: int = logging.INFO, **items) -> None:
    log.log(level, kv(**items), extra={"stage": stage})


# ─────────────────────────── API (캐시 우선 — 한 파일) ───────────────────────────
class YT:
    COST = {"search": 100, "videos": 1, "channels": 1}

    def __init__(self, key: str | None, offline: bool):
        self.key, self.offline = key, offline
        self.units = self.calls = self.cache_hits = 0
        self.quota_dead = False
        self.cache: dict = {}
        if API_CACHE.exists():
            self.cache = json.loads(gzip.decompress(API_CACHE.read_bytes()).decode("utf-8"))
        self.dirty = False
        self.used: set[str] = set()
        self.misses = 0

    @staticmethod
    def _h(endpoint: str, params: dict) -> str:
        return hashlib.sha1(json.dumps([endpoint, params], sort_keys=True, ensure_ascii=False).encode()).hexdigest()[:16]

    def get(self, endpoint: str, **params) -> dict | None:
        params = {k: v for k, v in params.items() if v is not None}
        h = self._h(endpoint, params)
        self.used.add(h)
        if h in self.cache:
            self.cache_hits += 1
            return self.cache[h]
        self.misses += 1
        if self.offline or self.quota_dead or not self.key:
            L("LOAD", logging.DEBUG, skip=endpoint, reason="offline/quota/no-key", params=params)
            return None
        try:
            r = requests.get(f"{API}/{endpoint}", params={**params, "key": self.key}, timeout=30)
        except requests.RequestException as e:
            L("LOAD", logging.WARNING, error="network", endpoint=endpoint, params=params, detail=str(e)[:200],
              next_step="잠시 뒤 run 다시 (받은 응답은 캐시에 남음)")
            return None
        self.calls += 1
        self.units += self.COST.get(endpoint, 1)
        if r.status_code in (403, 429) and ("quota" in r.text.lower() or r.status_code == 429):
            self.quota_dead = True
            L("LOAD", logging.WARNING, error=f"http{r.status_code}-quota", endpoint=endpoint, units_used=self.units,
              next_step="한국 17시(태평양 자정) 할당량 초기화 뒤 run 다시 — 캐시된 부분은 다시 받지 않음")
            return None
        if r.status_code != 200:
            L("LOAD", logging.WARNING, error=f"http{r.status_code}", endpoint=endpoint, params=params, body=r.text[:200])
            return None
        data = r.json()
        data = slim(endpoint, data)   # 캐시를 작게 (분석에 쓰는 칸만)
        self.cache[h] = data
        self.dirty = True
        return data

    def save(self) -> None:
        unused = set(self.cache) - self.used
        if unused and self.misses == 0:   # 모든 요청이 캐시에 있었을 때만 — 안 쓰는 옛 응답(검색어 묶음이 바뀌기 전) 정리
            for h in unused:
                del self.cache[h]
            self.dirty = True
            L("LOAD", cache_pruned=len(unused))
        if self.dirty:
            OUT_DIR.mkdir(parents=True, exist_ok=True)
            API_CACHE.write_bytes(gzip.compress(json.dumps(self.cache, ensure_ascii=False).encode("utf-8"), mtime=0))
            L("LOAD", cache_file=str(API_CACHE.relative_to(PSY.parent)), entries=len(self.cache),
              kb=round(API_CACHE.stat().st_size / 1024, 1))


def slim(endpoint: str, data: dict) -> dict:
    """캐시에 남길 칸만: 검색 = id·제목 · 영상 = 제목·채널·날짜·설명 300자·태그 30개·라이브·통계·길이 · 채널 = 통계."""
    items = data.get("items", [])
    if endpoint == "search":
        return {"items": [{"id": it.get("id", {}), "snippet": {"title": it.get("snippet", {}).get("title")}} for it in items]}
    if endpoint == "videos":
        keep = ("title", "channelId", "channelTitle", "publishedAt", "liveBroadcastContent")
        out = []
        for it in items:
            sn = it.get("snippet", {})
            s2 = {k: sn.get(k) for k in keep if k in sn}
            s2["description"] = (sn.get("description") or "")[:300]
            s2["tags"] = (sn.get("tags") or [])[:30]
            out.append({"id": it.get("id"), "snippet": s2, "statistics": it.get("statistics", {}),
                        "contentDetails": {"duration": it.get("contentDetails", {}).get("duration")}})
        return {"items": out}
    if endpoint == "channels":
        return {"items": [{"id": it.get("id"), "statistics": it.get("statistics", {})} for it in items]}
    return data


def iso_duration_sec(s: str | None) -> float:
    if not s:
        return np.nan
    m = re.fullmatch(r"P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", s)
    if not m:
        return np.nan
    d, h, mi, se = (int(x) if x else 0 for x in m.groups())
    return d * 86400 + h * 3600 + mi * 60 + se


# ─────────────────────────── 1. LOAD-A (기존 심리 캐시) ───────────────────────────
def load_existing() -> pd.DataFrame:
    t0 = time.time()
    if not PSY_CACHE_TGZ.exists():
        L("LOAD", logging.WARNING, source="psy_cache", error="missing", path=str(PSY_CACHE_TGZ),
          next_step="git pull 로 psychology/cloud_cache/cache.tgz 받기")
        return pd.DataFrame()
    subs = {}
    if COMPARE_CSV.exists():
        with open(COMPARE_CSV, encoding="utf-8-sig") as f:
            for r in csv.DictReader(f):
                subs[r["id"]] = r.get("subs")
    rows = []
    with tarfile.open(PSY_CACHE_TGZ) as tf:
        for m in tf.getmembers():
            if not (m.isfile() and "/.cache/" in m.name and m.name.endswith(".json")):
                continue
            try:
                d = json.load(io.TextIOWrapper(tf.extractfile(m), encoding="utf-8"))
            except (json.JSONDecodeError, UnicodeDecodeError):
                continue
            if not (isinstance(d, dict) and "view_count" in d and "id" in d):
                continue
            rows.append({"video_id": d["id"], "title": d.get("title", ""), "channel_id": d.get("channel_id"),
                         "channel": d.get("channel", ""), "published": d.get("published"),
                         "description": (d.get("description") or "")[:300],
                         "tags": "|".join((d.get("tags") or [])[:30]),
                         "views": d.get("view_count"), "likes": d.get("like_count"), "comments": d.get("comment_count"),
                         "duration_sec": d.get("duration"), "live": bool(d.get("live") or d.get("was_live")),
                         "subs": subs.get(d["id"]), "source": "psy_cache", "query": "", "window": ""})
    df = pd.DataFrame(rows)
    L("LOAD", source="psychology/cloud_cache/cache.tgz (심리 분석 탐색 2026-11-11~12)", rows=len(df),
      with_subs=int(df["subs"].notna().sum()) if len(df) else 0,
      date_range=f"{df['published'].min()[:10]}~{df['published'].max()[:10]}" if len(df) else "-",
      sec=round(time.time() - t0, 2))
    return df


# ─────────────────────────── 2. LOAD-B (사건 심리 검색) ───────────────────────────
def load_search(yt: YT) -> pd.DataFrame:
    t0 = time.time()
    hits = []
    for wk, days in WINDOWS.items():
        after = None if days is None else (AS_OF - timedelta(days=days)).strftime("%Y-%m-%dT%H:%M:%SZ")
        for q in QUERIES:
            data = yt.get("search", part="snippet", q=q, type="video", order="viewCount", maxResults=50,
                          regionCode="KR", relevanceLanguage="ko", videoDuration="medium", publishedAfter=after)
            if data is None:
                L("LOAD", logging.DEBUG if yt.offline else logging.WARNING, window=wk, query=q, error="no_response",
                  next_step="할당량·키 확인 뒤 run 다시 (받은 검색어는 캐시에 남음)")
                continue
            ids = [it["id"]["videoId"] for it in data.get("items", []) if it.get("id", {}).get("videoId")]
            hits += [(wk, q, v) for v in ids]
            L("LOAD", logging.DEBUG, window=wk, query=q, found=len(ids))
    if not hits:
        L("LOAD", logging.WARNING, source="search", error="0 hits", next_step="YOUTUBE_API_KEY·할당량 확인 뒤 run")
        return pd.DataFrame()
    hit_df = pd.DataFrame(hits, columns=["window", "query", "video_id"])
    vids = sorted(hit_df["video_id"].unique())
    rows = []
    for i in range(0, len(vids), 50):
        data = yt.get("videos", part="snippet,statistics,contentDetails", id=",".join(vids[i:i + 50]), maxResults=50)
        for it in (data or {}).get("items", []):
            sn, st, cd = it["snippet"], it.get("statistics", {}), it.get("contentDetails", {})
            rows.append({"video_id": it["id"], "title": sn.get("title", ""), "channel_id": sn.get("channelId"),
                         "channel": sn.get("channelTitle", ""), "published": sn.get("publishedAt"),
                         "description": (sn.get("description") or "")[:300], "tags": "|".join(sn.get("tags", [])[:30]),
                         "views": st.get("viewCount"), "likes": st.get("likeCount"), "comments": st.get("commentCount"),
                         "duration_sec": iso_duration_sec(cd.get("duration")),
                         "live": sn.get("liveBroadcastContent", "none") != "none"})
    vdf = pd.DataFrame(rows)
    chans = sorted(vdf["channel_id"].dropna().unique()) if len(vdf) else []
    crow = []
    for i in range(0, len(chans), 50):
        data = yt.get("channels", part="statistics", id=",".join(chans[i:i + 50]), maxResults=50)
        for it in (data or {}).get("items", []):
            st = it.get("statistics", {})
            crow.append({"channel_id": it["id"],
                         "subs": None if st.get("hiddenSubscriberCount") else st.get("subscriberCount")})
    vdf = vdf.merge(pd.DataFrame(crow, columns=["channel_id", "subs"]), on="channel_id", how="left")
    qs = hit_df.groupby("video_id").agg(query=("query", lambda s: "|".join(sorted(set(s)))),
                                        window=("window", lambda s: "|".join(sorted(set(s)))))
    df = vdf.merge(qs, left_on="video_id", right_index=True, how="left")
    df["source"] = "search"
    L("LOAD", source="YouTube Data API v3 search(order=viewCount,KR,ko,medium 4~20분)", queries=len(QUERIES),
      windows=list(WINDOWS), search_hits=len(hit_df), unique_videos=len(df), channels=len(chans),
      api_calls=yt.calls, units=yt.units, cache_hits=yt.cache_hits, sec=round(time.time() - t0, 2))
    return df


# ─────────────────────────── 3. VALIDATE ───────────────────────────
def validate(df: pd.DataFrame) -> pd.DataFrame:
    n0 = len(df)
    d = df.copy()
    for c in ("views", "likes", "comments", "subs", "duration_sec"):
        d[c] = pd.to_numeric(d[c], errors="coerce")
    d["published_dt"] = pd.to_datetime(d["published"], utc=True, errors="coerce")
    # 같은 영상이 두 출처에 있으면 검색 쪽(통계가 더 최근)을 남기고 출처를 합침
    d = d.sort_values("source", key=lambda s: s.map({"search": 0, "psy_cache": 1}))
    src = d.groupby("video_id")["source"].agg(lambda s: "|".join(sorted(set(s))))
    dup = int(d["video_id"].duplicated().sum())
    d = d.drop_duplicates("video_id", keep="first").copy()
    d["source"] = d["video_id"].map(src)
    drops = {
        "no_views": d["views"].isna(),
        "no_date": d["published_dt"].isna(),
        "future_date": d["published_dt"] > AS_OF + timedelta(days=1),
        "no_hangul_title": ~d["title"].fillna("").str.contains(HANGUL),
        "live": d["live"].fillna(False).astype(bool),
        "short_lt_4min": d["duration_sec"].fillna(0) < MIN_SEC,
    }
    bad = pd.Series(False, index=d.index)
    counts = {}
    for k, m in drops.items():
        m = m & ~bad
        counts[k] = int(m.sum())
        bad |= m
    out = d[~bad].copy()
    L("VALIDATE", rows_in=n0, duplicates_merged=dup, **{f"drop_{k}": v for k, v in counts.items()},
      rows_out=len(out), subs_missing=int(out["subs"].isna().sum()))
    return out


# ─────────────────────────── 4. CLASSIFY ───────────────────────────
def read_labels(path: Path = LABELS) -> pd.DataFrame:
    cols = ["video_id", "keep", "kind", "case", "concept", "note"]
    if not path.exists():
        return pd.DataFrame(columns=cols)
    lab = pd.read_csv(path, sep="\t", dtype=str, comment="#").fillna("")
    lab = lab[cols]
    bad_kind = lab[(lab["keep"] == "1") & ~lab["kind"].isin(KINDS)]
    if len(bad_kind):
        L("CLASSIFY", logging.WARNING, labels_bad_kind=len(bad_kind), ids=bad_kind["video_id"].tolist()[:10],
          next_step=f"labels.tsv kind 는 {list(KINDS)} 중 하나")
    dup = lab["video_id"].duplicated(keep="last")
    if dup.any():
        L("CLASSIFY", logging.WARNING, labels_duplicate=int(dup.sum()), note="마지막 줄을 씀")
        lab = lab[~dup]
    return lab


def classify(df: pd.DataFrame, labels: pd.DataFrame) -> pd.DataFrame:
    d = df.copy()
    d["rule_words"] = d["title"].fillna("").map(lambda t: ",".join(sorted(set(m.group(0) for m in CASE_WORDS.finditer(t)))))
    d["candidate"] = d["rule_words"] != ""
    d = d.merge(labels, on="video_id", how="left")
    d["labeled"] = d["keep"].notna() & (d["keep"] != "")
    d["is_case"] = d["keep"] == "1"
    d["kind_name"] = d["kind"].map(KINDS).fillna("")
    L("CLASSIFY", rule="CASE_WORDS in title", candidates=int(d["candidate"].sum()), labeled=int(d["labeled"].sum()),
      labeled_outside_rule=int((d["labeled"] & ~d["candidate"]).sum()),
      kept_cases=int(d["is_case"].sum()), rejected=int((d["labeled"] & ~d["is_case"]).sum()),
      todo=int((d["candidate"] & ~d["labeled"]).sum()))
    return d


# ─────────────────────────── 5. METRICS ───────────────────────────
def load_success_rules() -> dict:
    with open(RULES_TOML, "rb") as f:
        s = tomllib.load(f)["success"]
    return {k: s[k] for k in ("MIN_AGE_DAYS", "MAX_AGE_DAYS", "MAX_SUBS", "MIN_VPD_SUBS", "MIN_VIEWS", "MIN_MINUTES")}


def features(df: pd.DataFrame, rules: dict) -> pd.DataFrame:
    d = df.copy()
    d["age_days"] = ((AS_OF - d["published_dt"]).dt.total_seconds() / 86400).clip(lower=1)
    d["vpd"] = d["views"] / d["age_days"]
    base = d["subs"].clip(lower=100)
    d["ratio"] = d["views"] / base
    d["vpd_subs"] = d["vpd"] / base
    d["like_rate"] = d["likes"] / d["views"].replace(0, np.nan)
    d["minutes"] = d["duration_sec"] / 60
    d["size"] = np.select([d["subs"].isna(), d["subs"] <= SMALL_SUBS, d["subs"] >= BIG_SUBS],
                          ["구독자 숨김", "작은 채널(≤5만)", "큰 채널(≥100만)"], "중간 채널")
    d["success"] = ((d["age_days"] >= rules["MIN_AGE_DAYS"]) & (d["age_days"] <= rules["MAX_AGE_DAYS"]) &
                    (d["subs"] <= rules["MAX_SUBS"]) & (d["vpd_subs"] >= rules["MIN_VPD_SUBS"]) &
                    (d["views"] >= rules["MIN_VIEWS"]) & (d["minutes"] >= rules["MIN_MINUTES"]))
    return d


def cap_channel(d: pd.DataFrame, n: int = PER_CHANNEL) -> pd.DataFrame:
    return d.sort_values("views", ascending=False).groupby("channel_id", dropna=False).head(n)


def group_table(d: pd.DataFrame, key: str) -> pd.DataFrame:
    rows = []
    for k, g in d.groupby(key):
        if not k:
            continue
        c = cap_channel(g)
        top = g.sort_values("views", ascending=False).iloc[0]
        rows.append({key: k, "videos": len(g), "channels": g["channel_id"].nunique(),
                     "views_sum": int(g["views"].sum()), "views_median_cap": float(c["views"].median()),
                     "vpd_median_cap": float(c["vpd"].median()), "max_views": int(top["views"]),
                     "ratio_median": float(c.loc[c["subs"] >= RATIO_MIN_SUBS, "ratio"].median()),
                     "small_videos": int((g["size"] == "작은 채널(≤5만)").sum()),
                     "small_views_median": float(g.loc[g["size"] == "작은 채널(≤5만)", "views"].median())
                     if (g["size"] == "작은 채널(≤5만)").any() else np.nan,
                     "success": int(g["success"].sum()), "recent365": int((g["age_days"] <= 365).sum()),
                     "top_title": top["title"], "top_id": top["video_id"], "top_channel": top["channel"]})
    return pd.DataFrame(rows).sort_values("views_sum", ascending=False) if rows else pd.DataFrame()


def concept_rows(d: pd.DataFrame) -> pd.DataFrame:
    """concept 칸은 '나르시시스트|가스라이팅' 처럼 여러 개 — 하나씩 펼침."""
    e = d.assign(concept_one=d["concept"].fillna("").str.split("|")).explode("concept_one")
    e["concept_one"] = e["concept_one"].str.strip()
    return e[e["concept_one"] != ""]


# ─────────────────────────── 6. EXPORT ───────────────────────────
def n(x) -> str:
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return "-"
    x = float(x)
    if x >= 1e8:
        return f"{x / 1e8:.1f}억"
    if x >= 1e4:
        return f"{x / 1e4:.1f}만" if x < 1e6 else f"{x / 1e4:,.0f}만"
    return f"{x:,.0f}"


def rx(x) -> str:
    return "-" if x is None or (isinstance(x, float) and np.isnan(x)) else f"{x:.2f}"


def esc(s: str) -> str:
    return str(s).replace("|", "／").replace("\n", " ")[:90]


def vid_link(r) -> str:
    return f"[{esc(r['title'])}](https://youtu.be/{r['video_id']})"


def export(d: pd.DataFrame, yt: YT, rules: dict, t0: float) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    cases = d[d["is_case"]].copy()
    cols = ["video_id", "kind", "kind_name", "case", "concept", "title", "channel", "subs", "size", "views", "likes",
            "comments", "published", "age_days", "minutes", "vpd", "ratio", "vpd_subs", "like_rate", "success",
            "source", "query", "window", "note"]
    cases.sort_values("views", ascending=False)[cols].to_csv(OUT_DIR / "incident_cases.csv", index=False,
                                                              encoding="utf-8-sig", float_format="%.4g")
    todo = d[d["candidate"] & ~d["labeled"]].sort_values("views", ascending=False)
    todo[["video_id", "views", "subs", "channel", "rule_words", "title"]].to_csv(
        OUT_DIR / "candidates_todo.tsv", sep="\t", index=False)

    by_kind = group_table(cases, "kind_name")
    by_case = group_table(cases[cases["case"].fillna("") != ""], "case")
    ce = concept_rows(cases[cases["kind"].isin(REAL_KINDS)])
    by_concept = group_table(ce, "concept_one")

    L_ = []
    w = L_.append
    w("# 심리 — 사람들이 많이 본 '심리가 초래한 실제 사례' 영상 (사건·사고·실험·일상)")
    w("")
    w(f"VERSION: {VERSION} — 만든 도구 `psychology/source/incident_cases.py` · 기준일 {AS_OF:%Y-%m-%d} · "
      f"사용자 지시 2026-11-23 \"심리 주제 쪽은 사람들이 가장 관심 있게 본 심리가 반영된 사건, 사고 등 사례를 찾아봐\" · "
      f"\"그냥 꼭 큰 사건, 사고가 아닌 심리가 초래한 사례면 되니까 심리에 집중해 계속 진행해\"")
    w("")
    w("> 숫자·원문만 (판단은 맨 끝 '판단' 절에만, Claude 판단이라고 적음). 연구·교육용 — 수사·의료 판단 아님.")
    w("")
    w("## 0. 읽는 법·한계 (먼저)")
    w(f"- 자료 ① 심리 분석 탐색 캐시 (심리학·인간관계·자존감 검색어, 2026-11-11~12 받음) ② 사건 심리 검색어 {len(QUERIES)}개 × "
      f"기간 2(전체 · 최근 365일) — `search(order=viewCount, KR, ko, 4~20분)` 50개씩. ② 는 **검색어마다 조회수 위쪽 꼬리**만 본다.")
    w(f"- 검색어: {' · '.join(QUERIES)}")
    w("- 4분 미만·라이브·한글 없는 제목은 뺌. 사례 판정 = Claude 가 제목·채널을 읽고 `labels.tsv` 에 씀 (대본은 안 봄). "
      "**사례 = 실제 일(사건·사고·실험·사람·관찰)을 들고 그 안의 심리를 설명하는 영상** — 크기는 상관없음. "
      "수사·재판·뉴스만 있고 심리 설명이 없는 것은 뺌. 영화 해설·진위 모를 사연은 따로 갈래(표 1·5·7 에서 뺌).")
    w("- 조회수는 채널 크기에 크게 좌우 → 묶음 가운데값은 채널당 상위 3편으로 자름 · 작은 채널(구독자 5만 이하)을 따로 셈 · "
      f"**구독자 배수**(조회수 ÷ 구독자) 가운데값 = 채널 크기를 덜 타는 비교 (구독자 {RATIO_MIN_SUBS:,}명 미만 채널은 뺌 — "
      "2009~2015년 옛 영상 재업로드가 배수 수백 배로 부풀림).")
    w(f"- 성공 사례 = 심리 `analysis_rules.toml [success]` 그대로: 올린 지 {rules['MIN_AGE_DAYS']}~{rules['MAX_AGE_DAYS']}일 · "
      f"구독자 ≤ {rules['MAX_SUBS']:,} · 구독자당 하루 조회수 ≥ {rules['MIN_VPD_SUBS']} · 조회수 ≥ {rules['MIN_VIEWS']:,} · "
      f"{rules['MIN_MINUTES']:.0f}분 이상.")
    lab_n = int(d["labeled"].sum())
    w(f"- 판정한 영상 {lab_n:,}개 중 실제 사례 {len(cases):,}개 · 규칙 후보인데 아직 판정 안 한 것 {len(todo):,}개 "
      f"(`candidates_todo.tsv` — 조회수 낮은 쪽) → 표에 안 들어감.")
    w("")
    w("## 1. 심리 개념별 — 실제 사례만 (영화·사연 뺌 · 한 영상에 개념이 여럿이면 각각 셈 · 조회수 합 순)")
    w("")
    w("| 심리 개념 | 영상 | 채널 | 조회수 합 | 가운데값(채널당 3편) | 구독자 배수 가운데값 | 하루 조회수 가운데값 | 작은 채널 영상 | 작은 채널 가운데값 | 성공 사례 | 최근 1년 | 대표 영상 (채널) |")
    w("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for _, r in by_concept.head(40).iterrows():
        w(f"| {r['concept_one']} | {r['videos']} | {r['channels']} | {n(r['views_sum'])} | {n(r['views_median_cap'])} | "
          f"{rx(r['ratio_median'])} | {n(r['vpd_median_cap'])} | {r['small_videos']} | {n(r['small_views_median'])} | {r['success']} | {r['recent365']} | "
          f"[{esc(r['top_title'])}](https://youtu.be/{r['top_id']}) ({esc(r['top_channel'])}) |")
    w("")
    w("## 2. 사례 갈래별")
    w("")
    w("| 갈래 | 영상 | 채널 | 조회수 합 | 가운데값(채널당 3편) | 구독자 배수 가운데값 | 하루 조회수 가운데값 | 최고 | 작은 채널 영상 | 작은 채널 가운데값 | 성공 사례 | 최근 1년 |")
    w("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for _, r in by_kind.iterrows():
        w(f"| {r['kind_name']} | {r['videos']} | {r['channels']} | {n(r['views_sum'])} | {n(r['views_median_cap'])} | "
          f"{rx(r['ratio_median'])} | {n(r['vpd_median_cap'])} | {n(r['max_views'])} | {r['small_videos']} | {n(r['small_views_median'])} | "
          f"{r['success']} | {r['recent365']} |")
    w("")
    w("## 3. 이름 있는 사례별 (사건·실험·인물 — 영상 2개 이상 또는 조회수 합 순 상위 40)")
    w("")
    w("| 사례 | 갈래 | 심리 개념 | 영상 | 채널 | 조회수 합 | 최고 조회수 | 작은 채널 영상 | 대표 영상 (채널) |")
    w("|---|---|---|---|---|---|---|---|---|")
    kind_of_case = cases.groupby("case")["kind_name"].agg(lambda s: "·".join(sorted(set(s))))
    concept_of_case = concept_rows(cases).groupby("case")["concept_one"].agg(
        lambda s: "·".join(pd.Series(s).value_counts().index[:3]))
    for _, r in by_case.head(40).iterrows():
        w(f"| {esc(r['case'])} | {kind_of_case.get(r['case'], '')} | {concept_of_case.get(r['case'], '-')} | {r['videos']} | "
          f"{r['channels']} | {n(r['views_sum'])} | {n(r['max_views'])} | {r['small_videos']} | "
          f"[{esc(r['top_title'])}](https://youtu.be/{r['top_id']}) ({esc(r['top_channel'])}) |")
    w("")

    def table(rows: pd.DataFrame, title: str) -> None:
        w(title)
        w("")
        w("| # | 영상 | 채널 | 구독자 | 조회수 | 구독자 배수 | 하루 조회수 | 좋아요율 | 올린 날 | 갈래 | 사건 | 개념 |")
        w("|---|---|---|---|---|---|---|---|---|---|---|---|")
        for i, (_, r) in enumerate(rows.iterrows(), 1):
            w(f"| {i} | {vid_link(r)} | {esc(r['channel'])} | {n(r['subs'])} | {n(r['views'])} | {r['ratio']:.1f} | "
              f"{n(r['vpd'])} | {r['like_rate'] * 100:.1f}% | {str(r['published'])[:10]} | {r['kind_name']} | "
              f"{esc(r['case'] or '-')} | {esc(r['concept'] or '-')} |")
        w("")

    top = cases.sort_values("views", ascending=False).groupby("channel_id").head(2).head(TOP_SHOW)
    table(top, f"## 4. 조회수 상위 {TOP_SHOW} (채널당 2편)")
    real = cases[cases["kind"].isin(REAL_KINDS)]
    small = real[real["size"] == "작은 채널(≤5만)"].sort_values("views", ascending=False).groupby("channel_id").head(2).head(20)
    table(small, "## 5. 작은 채널(구독자 5만 이하) — 실제 사례 조회수 상위 20 (채널당 2편, 영화·사연 뺌)")
    succ = cases[cases["success"]].sort_values("vpd_subs", ascending=False)
    table(succ, f"## 6. 성공 사례 기준을 넘은 사례 영상 ({len(succ)}개 — 구독자당 하루 조회수 순)")
    rec = real[real["age_days"] <= 365].sort_values("vpd", ascending=False).groupby("channel_id").head(2).head(20)
    table(rec, "## 7. 최근 1년 — 실제 사례 하루 조회수 상위 20 (채널당 2편)")

    w("## 8. 실행 기록")
    w("")
    w(f"- API 호출 {yt.calls}번 · 할당량 {yt.units:,}단위 (이번 실행) · 캐시 사용 {yt.cache_hits}번 · "
      f"{time.time() - t0:.1f}초 · 캐시 `result/incidents/api_cache.json.gz` (다시 돌리면 할당량 0)")
    w(f"- 판정 파일 `result/incidents/labels.tsv` · 전체 표 `incident_cases.csv` · 판정 안 한 후보 `candidates_todo.tsv`")
    w("")
    judg = OUT_DIR / "judgment.md"
    if judg.exists():
        w(judg.read_text(encoding="utf-8").rstrip())
        w("")
    (OUT_DIR / "incident_cases.md").write_text("\n".join(L_), encoding="utf-8")
    L("EXPORT", md=str((OUT_DIR / "incident_cases.md").relative_to(PSY.parent)), cases=len(cases), kinds=len(by_kind),
      named_cases=len(by_case), concepts=len(by_concept), success=len(succ), todo=len(todo))


# ─────────────────────────── main ───────────────────────────
def main(argv: list[str]) -> int:
    setup_logging()
    cmd = argv[1] if len(argv) > 1 else "analyze"
    if cmd not in ("run", "analyze"):
        print(__doc__)
        return 2
    t0 = time.time()
    key = next((os.environ[k].strip() for k in ("PSYCHOLOGY_YOUTUBE_API_KEY", "YOUTUBE_API_KEY_PSYCHOLOGY", "YOUTUBE_API_KEY") if os.environ.get(k, "").strip()), "")
    L("START", tool=f"incident_cases.py {VERSION}", cmd=cmd, as_of=f"{AS_OF:%Y-%m-%d}", seed=SEED,
      key="env:YOUTUBE_API_KEY" if key else "없음", offline=cmd == "analyze")
    yt = YT(key, offline=(cmd == "analyze"))
    rules = load_success_rules()
    L("FEATURE", success_rules=rules, source=str(RULES_TOML.relative_to(PSY.parent)))
    a = load_existing()
    b = load_search(yt)
    yt.save()
    df = pd.concat([x for x in (a, b) if len(x)], ignore_index=True)
    df = validate(df)
    df = classify(df, read_labels())
    df = features(df, rules)
    cases = df[df["is_case"]]
    if len(cases):
        L("SIGNAL", kinds=cases["kind"].value_counts().to_dict(), success=int(cases["success"].sum()),
          small_channel=int((cases["size"] == "작은 채널(≤5만)").sum()),
          views_median=float(cases["views"].median()))
    export(df, yt, rules, t0)
    L("RESULT", cmd=cmd, seconds=round(time.time() - t0, 1), api_units=yt.units)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
