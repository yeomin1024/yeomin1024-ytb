# VERSION: v1.2.1 — 2026-11-27 — 키: CRISIS_YOUTUBE_API_KEY → YOUTUBE_API_KEY_CRISIS → YOUTUBE_API_KEY 순서 (주제 접두사 — 사용자 지시 2026-11-27 "주제별 접두사를 변수명에 붙여서 구분되도록해"). 시작할 때 한 번 정함.
# (이전) VERSION: v1.2.0 — 2026-11-23 — '겨울' 낱말 묶음 · 채널 크기별 숫자 · 본 영상 전부 목록 (사용자 지시 2026-11-23 "겨울 러닝이 가장 많다고?
#          니가 본 영상들 구독자 수랑 조회수 모두 알려줘봐"): ① 제목에 겨울 낱말(WINTER_WORDS)·겨울+위험 묶음 — v1.1.0 의 '편 소재' 묶음은
#          겨울이 아니라 10월 마라톤 사망 뉴스였음을 드러내려고 ② 구독자 5만 이하 영상 조회수 중앙값 · 구독자 100만+ 채널이 가져간 조회수 몫
#          ③ topic_demand_all.md — 남긴 영상 전부(구독자·조회수·배수) + 뺀 영상과 까닭. 수집·기존 숫자는 그대로 (캐시, 할당량 0)
# (이전) v1.1.0 — 2026-11-23 — 분류 오탐 고침 + '편 소재 낱말' 묶음 추가 (v1.0.0 결과를 Claude 가 읽고 발견):
#          ① 주제 밖 낱말 EXCLUDE — '런닝맨'(예능)이 러닝으로 들어옴 ② 위험·안전 낱말에서 '죽'(우후죽순·죽전)·'실화'(실화냐=정말?) 뺌,
#             '죽음|죽었|죽을|죽는'으로 좁힘 ③ 주제마다 그 편이 다룰 위험만 고르는 focus 묶음 (캠핑 = 일산화탄소·가스 중독만)
#          — 수집·성공 기준·검색어는 그대로 (캐시로 다시 셈, 할당량 0)
# (이전) v1.0.0 — 2026-11-23 — 신규: 주제 후보별 유튜브 수요 비교
#          (사용자 지시 2026-11-23 "그럼 각각 관련된 단어로 검색해서 관련 영상을 사람들이 많이봤는지 분석해봐" —
#           후보 = 겨울 러닝 · 캠핑·차박 일산화탄소 · 초겨울 산행, 비교 기준 = 지금 채널 1위 소재 엘리베이터)
"""
topic_demand.py — 주제 후보마다 관련 검색어로 유튜브를 찾아 '사람들이 많이 봤나'를 비교

흐름
  1. LOAD     : 검색어마다 search(order=viewCount, regionCode=KR, relevanceLanguage=ko, publishedAfter=AS_OF-365일) 50개
                → videos·channels 통계. 응답은 crisis/cache/ 에 저장 (crisis_lab 과 같은 캐시 — 재실행 시 할당량 0)
  2. VALIDATE : 통계 빠짐 · 숨긴 구독자 · 3일 미만 · 한글 없는 제목 · 미래 날짜 (뺀 수를 로그로)
  3. FILTER   : 주제 낱말(TOPICS[*]["words"])이 제목·태그·설명 앞 300자에 없으면 '주제 밖' → 뺌 (뺀 수·예시 로그)
  4. FEATURE  : 쇼츠(≤180초)/롱폼 · 위험·안전 낱말(SAFETY) 여부 · 겨울(11~2월)에 올렸나
  5. METRICS  : 주제 × (전체 · 위험/안전 영상) — 영상·채널 수, 조회수 중앙값(채널당 최대 3편으로 자른 뒤)·상위 25%,
                10만·100만 넘은 영상, 하루 조회수 중앙값, 작은 채널 성공 사례 (CLAUDE.md 기준 — 아래 SUCCESS)
  6. EXPORT   : crisis/result/demand/topic_demand.md · topic_demand_videos.csv · topic_demand_queries.csv

읽는 법 (한계)
  - search(order=viewCount)는 '그 검색어로 조회수 높은 순 50개'라 전체 시장이 아니라 위쪽 꼬리만 본다.
    주제끼리 같은 방법으로 쟀으니 '비교'는 되지만 절대 크기로 읽으면 안 됨.
  - 기간 365일 = 겨울 한 번(2025-11-23 ~ 2026-02)이 들어감. 겨울 주제는 180일 기준만 보면 철이 안 맞아 작게 나옴
    → 성공 사례를 180일(CLAUDE.md 표준)과 365일(계절 반영) 두 가지로 함께 적음.

실행:  python3 crisis/code/topic_demand.py run        # 수집+분석 (캐시 있으면 API 호출 안 함)
       python3 crisis/code/topic_demand.py analyze    # 캐시만으로 분석 (할당량 0)
       LOG_LEVEL=DEBUG python3 crisis/code/topic_demand.py analyze   # 주제 밖으로 뺀 영상 제목까지
주의: 연구·기획용 도구. 영상 속 안전 수칙은 소방청·행안부 등 공식 지침으로 따로 확인할 것.
"""
from __future__ import annotations

import logging
import re
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import crisis_lab as cl  # noqa: E402  — YT(캐시 우선 API)·로깅·길이 변환을 그대로 씀 (같은 캐시·같은 로그 꼴)

VERSION = "v1.2.1"
SEED = 0  # 무작위 요소 없음 — 재현성 기록용

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "result" / "demand"
AS_OF = datetime(2026, 11, 23, tzinfo=timezone.utc)   # 기준일 고정 (재실행해도 '며칠 지났나'가 같음)
WINDOW_DAYS = 365
MIN_AGE_DAYS = 3
SHORTS_MAX_SEC = 180
PER_CHANNEL = 3          # 중앙값 계산 때 한 채널은 조회수 상위 3편까지 (한 채널이 결과를 덮지 않게)
TOP_SHOW = 8             # 주제마다 보여 줄 조회수 상위 영상 (채널당 2편)
RECENT_DAYS = 60         # '요즘 올라오는 양' — 최근 60일 안에 올린 영상 수
WINTER_MONTHS = (11, 12, 1, 2)

# 성공 사례 — CLAUDE.md '분석' 기준 (180일·구독자 5만 이하·조회수 ≥ 구독자×3·4분 이상·조회수 1만 / 쇼츠 5만)
SUCCESS = {
    "long": {"MIN_AGE": 7, "MAX_SUBS": 50_000, "MIN_RATIO": 3.0, "MIN_VIEWS": 10_000, "MIN_SEC": 240},
    "short": {"MIN_AGE": 3, "MAX_SUBS": 50_000, "MIN_RATIO": 3.0, "MIN_VIEWS": 50_000},
}
SUCCESS_WINDOWS = (180, 365)   # 180 = 표준, 365 = 지난 겨울까지 (계절 반영 — 표준이 아님을 표에 적음)

TOPICS = {
    "winter_run": {
        "name": "겨울 러닝",
        "queries": ["겨울 러닝", "겨울 달리기", "러닝 심정지", "마라톤 사망", "러닝 사고", "러닝 위험"],
        "words": r"러닝|런닝|달리기|마라톤|조깅|러너|하프|풀코스|트레일러닝|러닝크루|10km|10킬로",
        "exclude": r"런닝맨|running ?man",   # v1.1.0: 예능 '런닝맨'
        "focus": r"심정지|돌연사|쓰러|사망|숨져|숨진|심장|저체온|빙판|한파|영하|추위",   # 그 편의 위험: 추위 속 심장·저체온·빙판
    },
    "camping_co": {
        "name": "캠핑·차박 일산화탄소",
        "queries": ["캠핑 일산화탄소", "차박 일산화탄소", "텐트 난로", "동계 캠핑 난로", "캠핑 사고", "일산화탄소 중독"],
        "words": r"캠핑|차박|텐트|야영|캠퍼|글램핑|캠핑카|동계캠핑|백패킹",
        "exclude": r"(?!)",
        "focus": r"일산화탄소|가스 ?중독|중독|질식",
    },
    "winter_hike": {
        "name": "초겨울 산행",
        "queries": ["겨울 산행", "겨울 등산", "등산 사고", "산악 사고", "등산 조난", "등산 추락"],
        "words": r"등산|산행|산악|하산|등반|조난|아이젠|등산로|등산객|설악산|한라산|북한산|지리산|국립공원|트레킹|산에서|능선",
        "exclude": r"(?!)",
        "focus": r"조난|추락|실족|저체온|동사|동상|빙판|아이젠|미끄러|고립|일몰|해 ?지|사고|사망|숨져|숨진",
    },
    "baseline_elevator": {
        "name": "(기준) 엘리베이터",
        "queries": ["엘리베이터 갇혔을 때", "엘리베이터 사고"],
        "words": r"엘리베이터|엘레베이터|엘베|승강기",
        "exclude": r"(?!)",
        "focus": r"갇|추락|멈|사고|사망",
    },
}
# v1.1.0: '죽'(우후죽순·죽전·죽인다=최고) · '실화'(실화냐=정말?) 오탐 → 뺌
SAFETY = (r"사고|사망|숨져|숨진|죽음|죽었|죽을|죽는|위험|주의|조심|심정지|돌연사|쓰러|중독|조난|추락|실족|저체온|동상|빙판|부상|"
          r"구조|119|응급|절대|하지\s?마|금지|안전|생존|참사|비극|경고|목숨")
# v1.2.0: 제목에 겨울·추위 낱말 — '겨울' 주제 수요를 따로 보려고
WINTER_WORDS = r"겨울|추위|추운|한파|영하|쌀쌀|빙판|설산|동계|눈길|첫눈|저체온|동상|패딩"
SMALL_SUBS = 50_000      # 작은 채널 (성공 기준과 같은 선)
BIG_SUBS = 1_000_000     # 큰 채널 (방송사 뉴스 등)
HANGUL = re.compile(r"[가-힣]")
L = cl.L


# ─────────────────────────── 1. LOAD ───────────────────────────
def load(yt: cl.YT) -> tuple[pd.DataFrame, pd.DataFrame]:
    """검색어마다 50개 → (topic, query, video_id) 행 + 영상·채널 통계."""
    t0 = time.time()
    after = (AS_OF - timedelta(days=WINDOW_DAYS)).strftime("%Y-%m-%dT%H:%M:%SZ")
    hits = []
    for tk, t in TOPICS.items():
        for q in t["queries"]:
            data = yt.get("search", part="snippet", q=q, type="video", order="viewCount", maxResults=50,
                          regionCode="KR", relevanceLanguage="ko", publishedAfter=after)
            if data is None:
                L("LOAD", logging.WARNING, topic=tk, query=q, error="no_response",
                  next_step="할당량·키 확인 뒤 run 다시 (받은 검색어는 캐시에 남음)")
                continue
            ids = [it["id"]["videoId"] for it in data.get("items", []) if it.get("id", {}).get("videoId")]
            hits += [(tk, q, v) for v in ids]
            L("LOAD", logging.DEBUG, topic=tk, query=q, found=len(ids))
    if not hits:
        raise RuntimeError("검색 결과 0건 — 캐시도 없고 API도 실패. YOUTUBE_API_KEY·할당량 확인 후 run 다시")
    hit_df = pd.DataFrame(hits, columns=["topic", "query", "video_id"])
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
                         "duration_sec": cl.iso_duration_sec(cd.get("duration"))})
    vdf = pd.DataFrame(rows)
    chans = sorted(vdf["channel_id"].dropna().unique())
    crow = []
    for i in range(0, len(chans), 50):
        data = yt.get("channels", part="statistics", id=",".join(chans[i:i + 50]), maxResults=50)
        for it in (data or {}).get("items", []):
            st = it.get("statistics", {})
            crow.append({"channel_id": it["id"], "subs": None if st.get("hiddenSubscriberCount") else st.get("subscriberCount")})
    vdf = vdf.merge(pd.DataFrame(crow, columns=["channel_id", "subs"]), on="channel_id", how="left")
    # 같은 영상이 한 주제의 검색어 여러 개에 걸리면 검색어를 합쳐 한 줄로 (주제가 다르면 주제마다 한 줄)
    q_by = hit_df.groupby(["topic", "video_id"])["query"].agg(lambda s: "|".join(sorted(set(s)))).reset_index()
    df = q_by.merge(vdf, on="video_id", how="inner")
    L("LOAD", source="YouTube Data API v3 search(order=viewCount,KR,ko)", queries=int(hit_df["query"].nunique()),
      search_hits=len(hit_df), unique_videos=len(vdf), topic_rows=len(df), channels=len(chans),
      date_range=f"{after[:10]}~{AS_OF:%Y-%m-%d}", api_calls=yt.calls, units=yt.units, cache_hits=yt.cache_hits,
      sec=round(time.time() - t0, 2))
    return df, hit_df


# ─────────────────────────── 2. VALIDATE ───────────────────────────
def validate(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    for c in ["views", "likes", "comments", "subs", "duration_sec"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    df["published"] = pd.to_datetime(df["published"], utc=True, errors="coerce")
    df["age_days"] = (AS_OF - df["published"]).dt.total_seconds() / 86400
    dup = int(df.duplicated(["topic", "video_id"]).sum())
    anomalies = {"duplicate_topic_video": dup,
                 "missing_views": int(df["views"].isna().sum()),
                 "hidden_or_missing_subs": int(df["subs"].isna().sum()),
                 "missing_duration": int(df["duration_sec"].isna().sum()),
                 "future_published": int((df["age_days"] < 0).sum()),
                 f"too_new(<{MIN_AGE_DAYS}d)": int((df["age_days"] < MIN_AGE_DAYS).sum()),
                 "older_than_window": int((df["age_days"] > WINDOW_DAYS + 1).sum()),
                 "non_korean_title": int((~df["title"].str.contains(HANGUL)).sum()),
                 "negative_counts": int((df[["views", "likes", "comments"]] < 0).any(axis=1).sum())}
    df = df.drop_duplicates(["topic", "video_id"])
    keep = (df["views"].notna() & df["published"].notna() & df["duration_sec"].notna()
            & df["age_days"].between(MIN_AGE_DAYS, WINDOW_DAYS + 1) & df["title"].str.contains(HANGUL))
    out = df[keep].copy()
    L("VALIDATE", logging.WARNING if sum(anomalies.values()) else logging.INFO, rows_in=len(df) + dup,
      rows_out=len(out), anomalies=anomalies,
      note="숨긴 구독자 채널은 성공 판정에서만 빠짐 (조회수 통계에는 들어감)")
    return out


# ─────────────────────────── 3. FILTER ───────────────────────────
def on_topic(df: pd.DataFrame) -> pd.DataFrame:
    """주제 낱말이 제목·태그·설명 앞 300자 어디에도 없으면 주제 밖 (검색이 끌어온 딴 영상)."""
    text = df["title"].fillna("") + " " + df["tags"].fillna("").str.replace("|", " ") + " " + df["description"].fillna("")
    words = df["topic"].map({k: v["words"] for k, v in TOPICS.items()})
    excl = df["topic"].map({k: v["exclude"] for k, v in TOPICS.items()})
    mask = pd.Series([bool(re.search(w, s, re.I)) and not re.search(x, s, re.I)
                      for w, x, s in zip(words, excl, text)], index=df.index)
    for tk in TOPICS:
        m = df["topic"] == tk
        dropped = df[m & ~mask]
        L("FILTER", topic=tk, rows_in=int(m.sum()), kept=int((m & mask).sum()), dropped_off_topic=len(dropped),
          examples=dropped.nlargest(3, "views")["title"].str.slice(0, 40).tolist())
        for _, r in dropped.iterrows():
            L("FILTER", logging.DEBUG, topic=tk, drop=r["title"][:60], views=int(r["views"]))
    return df[mask].copy()


# ─────────────────────────── 4. FEATURE ───────────────────────────
def features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["format"] = np.where(df["duration_sec"] <= SHORTS_MAX_SEC, "쇼츠", "롱폼")
    df["safety"] = df["title"].str.contains(SAFETY, regex=True)          # 제목에 위험·안전 낱말
    focus = df["topic"].map({k: v["focus"] for k, v in TOPICS.items()})  # v1.1.0: 그 편이 다룰 위험 낱말 (제목)
    df["focus"] = [bool(re.search(f, t)) for f, t in zip(focus, df["title"])]
    df["winter_title"] = df["title"].str.contains(WINTER_WORDS, regex=True)   # v1.2.0
    df["winter_upload"] = df["published"].dt.month.isin(WINTER_MONTHS)
    df["vpd"] = df["views"] / df["age_days"].clip(lower=1)                # 하루 조회수 = 조회수 ÷ 올린 지 날수
    df["ratio"] = df["views"] / df["subs"].clip(lower=1)                     # 구독자 대비 (숨김이면 NaN, 0명은 1명으로)
    for w in SUCCESS_WINDOWS:
        df[f"success_{w}"] = success_mask(df, w)
    L("FEATURE", shorts_rule=f"duration<={SHORTS_MAX_SEC}s", safety_regex_words=SAFETY.count("|") + 1,
      winter_months=list(WINTER_MONTHS), by_topic={tk: {"rows": int((df["topic"] == tk).sum()),
                                                        "shorts": int(((df["topic"] == tk) & (df["format"] == "쇼츠")).sum()),
                                                        "safety": int(((df["topic"] == tk) & df["safety"]).sum()),
                                                        "focus": int(((df["topic"] == tk) & df["focus"]).sum())}
                                                   for tk in TOPICS})
    return df


def success_mask(df: pd.DataFrame, window: int) -> pd.Series:
    """CLAUDE.md 성공 기준. 롱폼 4분 미만(181~239초)은 롱폼 성공 대상이 아님."""
    lo, sh = SUCCESS["long"], SUCCESS["short"]
    is_short = df["duration_sec"] <= SHORTS_MAX_SEC
    base = df["subs"].notna() & (df["subs"] <= lo["MAX_SUBS"]) & (df["views"] >= lo["MIN_RATIO"] * df["subs"])
    long_ok = (~is_short & (df["duration_sec"] >= lo["MIN_SEC"]) & df["age_days"].between(lo["MIN_AGE"], window)
               & (df["views"] >= lo["MIN_VIEWS"]))
    short_ok = is_short & df["age_days"].between(sh["MIN_AGE"], window) & (df["views"] >= sh["MIN_VIEWS"])
    return base & (long_ok | short_ok)


# ─────────────────────────── 5. METRICS ───────────────────────────
def cap_channel(d: pd.DataFrame, n: int = PER_CHANNEL) -> pd.DataFrame:
    return d.sort_values("views", ascending=False).groupby("channel_id", sort=False).head(n)


def metrics(d: pd.DataFrame) -> dict:
    if d.empty:
        return {"n": 0}
    c = cap_channel(d)
    return {
        "n": len(d), "channels": int(d["channel_id"].nunique()),
        "shorts_share": float((d["format"] == "쇼츠").mean()),
        "med_views": float(c["views"].median()), "p75_views": float(c["views"].quantile(0.75)),
        "med_vpd": float(c["vpd"].median()),
        "n_100k": int((d["views"] >= 100_000).sum()), "n_1m": int((d["views"] >= 1_000_000).sum()),
        "total_views": float(d["views"].sum()),
        "succ_180": int(d["success_180"].sum()), "succ_365": int(d["success_365"].sum()),
        "succ_channels_365": int(d.loc[d["success_365"], "channel_id"].nunique()),
        "recent_n": int((d["age_days"] <= RECENT_DAYS).sum()),
        # v1.2.0: 채널 크기 — 큰 채널(방송사) 몫이 크면 '많이 봤다'가 작은 채널에도 해당하는지 따로 봐야 함
        "n_small": int((d["subs"] <= SMALL_SUBS).sum()),
        "med_views_small": float(cap_channel(d[d["subs"] <= SMALL_SUBS])["views"].median()) if (d["subs"] <= SMALL_SUBS).any() else np.nan,
        "n_big": int((d["subs"] >= BIG_SUBS).sum()),
        "big_view_share": float(d.loc[d["subs"] >= BIG_SUBS, "views"].sum() / d["views"].sum()) if d["views"].sum() else np.nan,
        "winter_view_share": float(d.loc[d["winter_upload"], "views"].sum() / d["views"].sum()) if d["views"].sum() else np.nan,
        "winter_upload_share": float(d["winter_upload"].mean()),
        "med_views_long": float(cap_channel(d[d["format"] == "롱폼"])["views"].median()) if (d["format"] == "롱폼").any() else np.nan,
        "med_views_short": float(cap_channel(d[d["format"] == "쇼츠"])["views"].median()) if (d["format"] == "쇼츠").any() else np.nan,
    }


def summarize(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for tk, t in TOPICS.items():
        d = df[df["topic"] == tk]
        for part, sub in (("전체", d), ("위험·안전 제목", d[d["safety"]]), ("편 소재 낱말", d[d["focus"]]),
                          ("제목에 겨울 낱말", d[d["winter_title"]]), ("겨울 + 위험 제목", d[d["winter_title"] & d["safety"]])):
            m = metrics(sub)
            rows.append({"topic": tk, "name": t["name"], "part": part, **m})
            L("METRICS", topic=tk, part=part, **{k: (round(v, 3) if isinstance(v, float) else v) for k, v in m.items()})
    out = pd.DataFrame(rows)
    # v1.2.0: 빈 묶음(n=0) 줄 때문에 개수 칸이 실수(130.0)로 바뀌지 않게 정수형으로
    for c in ("n", "channels", "n_100k", "n_1m", "succ_180", "succ_365", "succ_channels_365", "recent_n", "n_small", "n_big"):
        if c in out:
            out[c] = out[c].astype("Int64")
    return out


def query_table(df: pd.DataFrame, hit_df: pd.DataFrame) -> pd.DataFrame:
    """검색어마다: 검색 결과 수 · 주제 안 영상 · 조회수 중앙값 · 1위 영상."""
    rows = []
    for (tk, q), h in hit_df.groupby(["topic", "query"], sort=False):
        d = df[(df["topic"] == tk) & df["query"].str.split("|").apply(lambda qs: q in qs)]
        top = d.nlargest(1, "views")
        rows.append({"topic": tk, "query": q, "search_hits": len(h), "on_topic": len(d),
                     "med_views": float(cap_channel(d)["views"].median()) if len(d) else np.nan,
                     "n_100k": int((d["views"] >= 100_000).sum()),
                     "top_title": top["title"].iloc[0] if len(top) else "", "top_views": float(top["views"].iloc[0]) if len(top) else np.nan})
    qt = pd.DataFrame(rows)
    L("METRICS", query_table_rows=len(qt), weakest=qt.nsmallest(3, "med_views")[["query", "med_views"]].values.tolist())
    return qt


# ─────────────────────────── 6. EXPORT ───────────────────────────
def n(x) -> str:
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return "-"
    x = float(x)
    if x >= 10_000:
        return f"{x / 10_000:.1f}만"
    return f"{x:,.0f}"


def pct(x) -> str:
    return "-" if x is None or (isinstance(x, float) and np.isnan(x)) else f"{x * 100:.0f}%"


def md_escape(s: str) -> str:
    return str(s).replace("|", "/").replace("\n", " ")


def export(df: pd.DataFrame, summ: pd.DataFrame, qt: pd.DataFrame, yt: cl.YT, t0: float) -> Path:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    cols = ["topic", "query", "video_id", "title", "channel", "subs", "views", "vpd", "ratio", "format", "safety", "focus",
            "published", "age_days", "duration_sec", "winter_upload", "success_180", "success_365"]
    df.sort_values(["topic", "views"], ascending=[True, False])[cols].to_csv(OUT_DIR / "topic_demand_videos.csv", index=False)
    qt.to_csv(OUT_DIR / "topic_demand_queries.csv", index=False)

    L_ = [f"# 주제 후보 유튜브 수요 비교 ({VERSION}, 기준일 {AS_OF:%Y-%m-%d})", "",
          "> 숫자는 코드 출력(`crisis/code/topic_demand.py`). 검색어마다 '조회수 높은 순 50개'(한국·한국어, 최근 365일)만 봄 → "
          "시장 전체가 아니라 위쪽 꼬리. 주제끼리 같은 방법이라 **비교**로만 읽기.",
          f"> 중앙값은 한 채널 최대 {PER_CHANNEL}편으로 자른 뒤. 성공 사례 = CLAUDE.md 기준(구독자 5만 이하·조회수 ≥ 구독자×3·"
          "롱폼 4분 이상 1만 / 쇼츠 5만). 180일 = 표준, 365일 = 지난 겨울 포함(계절 주제라 함께 적음 — 표준 아님).",
          "> 묶음: 전체 = 주제 낱말이 든 영상 · 위험·안전 제목 = 제목에 사고·위험·주의 같은 낱말 · "
          "편 소재 낱말 = 그 편이 다룰 위험만 (아래 5번에 낱말).", "",
          "## 1. 주제별 한눈에", "",
          "| 주제 | 묶음 | 영상 | 채널 | 조회수 중앙값 | 상위 25% | 하루 조회수 중앙값 | 10만+ | 100만+ | 작은 채널 성공 180일 | 365일 (채널) | 쇼츠 비율 | 최근 60일 올림 | 겨울에 올린 영상 조회수 몫 |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for _, r in summ.iterrows():
        if r["n"] == 0:
            L_.append(f"| {r['name']} | {r['part']} | 0 | | | | | | | | | | | |")
            continue
        L_.append(f"| {r['name']} | {r['part']} | {r['n']} | {r['channels']} | {n(r['med_views'])} | {n(r['p75_views'])} | "
                  f"{n(r['med_vpd'])} | {r['n_100k']} | {r['n_1m']} | {r['succ_180']} | {r['succ_365']} ({r['succ_channels_365']}) | "
                  f"{pct(r['shorts_share'])} | {r['recent_n']} | {pct(r['winter_view_share'])} |")
    L_ += ["", f"## 1-1. 채널 크기별 (v1.2.0) — 작은 채널 = 구독자 {SMALL_SUBS:,} 이하 · 큰 채널 = {BIG_SUBS:,} 이상", "",
           "| 주제 | 묶음 | 영상 | 작은 채널 영상 | 작은 채널 조회수 중앙값 | 큰 채널 영상 | 큰 채널이 가져간 조회수 몫 |", "|---|---|---|---|---|---|---|"]
    for _, r in summ.iterrows():
        if r["n"]:
            L_.append(f"| {r['name']} | {r['part']} | {r['n']} | {r['n_small']} | {n(r['med_views_small'])} | {r['n_big']} | {pct(r['big_view_share'])} |")
    L_ += ["", "## 2. 쇼츠 · 롱폼 조회수 중앙값 (전체 묶음)", "", "| 주제 | 롱폼 | 쇼츠 |", "|---|---|---|"]
    for _, r in summ[summ["part"] == "전체"].iterrows():
        L_.append(f"| {r['name']} | {n(r.get('med_views_long'))} | {n(r.get('med_views_short'))} |")

    L_ += ["", "## 3. 검색어별", "", "| 주제 | 검색어 | 검색 결과 | 주제 안 | 조회수 중앙값 | 10만+ | 1위 영상 (조회수) |", "|---|---|---|---|---|---|---|"]
    for _, r in qt.iterrows():
        L_.append(f"| {TOPICS[r['topic']]['name']} | {r['query']} | {r['search_hits']} | {r['on_topic']} | {n(r['med_views'])} | "
                  f"{r['n_100k']} | {md_escape(r['top_title'])[:45]} ({n(r['top_views'])}) |")

    L_ += ["", f"## 4. 주제별 조회수 상위 영상 (채널당 2편, 상위 {TOP_SHOW})", ""]
    for tk, t in TOPICS.items():
        d = df[df["topic"] == tk].sort_values("views", ascending=False).groupby("channel_id", sort=False).head(2).head(TOP_SHOW)
        L_ += [f"### {t['name']}", "", "| 조회수 | 구독자 | 형식 | 올린 날 | 위험·안전 | 편 소재 | 제목 | 채널 |",
               "|---|---|---|---|---|---|---|---|"]
        for _, r in d.iterrows():
            L_.append(f"| {n(r['views'])} | {n(r['subs'])} | {r['format']} | {r['published']:%Y-%m-%d} | {'○' if r['safety'] else ''} | "
                      f"{'○' if r['focus'] else ''} | {md_escape(r['title'])[:50]} | {md_escape(r['channel'])[:20]} |")
        f = df[(df["topic"] == tk) & df["focus"]].sort_values("views", ascending=False).groupby("channel_id", sort=False).head(2).head(5)
        if len(f):
            L_ += ["", "편 소재 낱말이 든 영상 조회수 상위 5 (채널당 2편):", ""]
            for _, r in f.iterrows():
                L_.append(f"- {n(r['views'])} — {md_escape(r['title'])[:55]} · 구독자 {n(r['subs'])} · {r['format']} · {r['published']:%Y-%m-%d}")
        s = df[(df["topic"] == tk) & df["success_365"]].sort_values("ratio", ascending=False).head(5)
        if len(s):
            L_ += ["", "작은 채널 성공 사례 (365일, 구독자 대비 높은 순):", ""]
            for _, r in s.iterrows():
                L_.append(f"- {md_escape(r['title'])[:55]} — 구독자 {n(r['subs'])} · 조회수 {n(r['views'])} (×{r['ratio']:.1f}) · "
                          f"{r['format']} · {r['published']:%Y-%m-%d}{' · 180일 밖' if r['age_days'] > 180 else ''}")
        L_.append("")
    L_ += ["## 5. 실행 기록", "",
           f"- 검색어 {sum(len(t['queries']) for t in TOPICS.values())}개 · API 호출 {yt.calls} · 할당량 {yt.units}단위 · 캐시 사용 {yt.cache_hits} · "
           f"걸린 시간 {time.time() - t0:.1f}초", f"- 위험·안전 낱말 (제목): `{SAFETY}`",
           "- 주제 낱말: " + " · ".join(f"{t['name']} `{t['words']}`" for t in TOPICS.values()),
           "- 주제 밖 낱말: " + " · ".join(f"{t['name']} `{t['exclude']}`" for t in TOPICS.values() if t["exclude"] != "(?!)"),
           "- 편 소재 낱말 (제목): " + " · ".join(f"{t['name']} `{t['focus']}`" for t in TOPICS.values()),
           f"- 겨울 낱말 (제목, v1.2.0): `{WINTER_WORDS}`",
           "- 본 영상 전부(구독자·조회수)와 뺀 영상: `topic_demand_all.md`",
           "- ※ 연구·기획용. 영상 속 안전 수칙은 공식 지침(소방청·행안부·국립공원공단)으로 따로 확인."]
    out = OUT_DIR / "topic_demand.md"
    out.write_text("\n".join(L_) + "\n", encoding="utf-8")
    L("EXPORT", files=[str(p.relative_to(ROOT)) for p in sorted(OUT_DIR.glob("topic_demand*"))], sec=round(time.time() - t0, 2))
    return out


def drop_table(raw: pd.DataFrame, val: pd.DataFrame, kept: pd.DataFrame) -> pd.DataFrame:
    """v1.2.0: 받았지만 분석에서 뺀 영상과 까닭 (검증 → 주제 필터 순)."""
    bad = raw.loc[~raw.index.isin(val.index)].copy()
    age = (AS_OF - pd.to_datetime(bad["published"], utc=True, errors="coerce")).dt.total_seconds() / 86400
    bad["reason"] = np.select([~bad["title"].fillna("").str.contains(HANGUL), age < MIN_AGE_DAYS],
                              ["한글 없는 제목 (외국 영상)", f"올린 지 {MIN_AGE_DAYS}일 미만"], "통계 빠짐")
    off = val.loc[~val.index.isin(kept.index)].copy()
    off["reason"] = "주제 밖 (주제 낱말 없음 / 주제 밖 낱말)"
    out = pd.concat([bad, off])
    for c in ("views", "subs"):
        out[c] = pd.to_numeric(out[c], errors="coerce")
    L("EXPORT", dropped_total=len(out), by_reason=out["reason"].value_counts().to_dict())
    return out


def export_all(df: pd.DataFrame, dropped: pd.DataFrame) -> Path:
    """v1.2.0: 본 영상 전부 — 주제마다 조회수 순, 구독자·조회수·구독자 대비·묶음 표시. 끝에 뺀 영상과 까닭."""
    L_ = [f"# 주제 후보 — 본 영상 전부 ({VERSION}, 기준일 {AS_OF:%Y-%m-%d})", "",
          "> `crisis/code/topic_demand.py` 출력. 검색어마다 조회수 높은 순 50개(한국·한국어, 최근 365일)를 받아 검증·주제 필터를 지난 영상 전부.",
          "> 표시: 위험 = 제목에 위험·안전 낱말 · 소재 = 그 편이 다룰 위험 낱말 · 겨울 = 제목에 겨울 낱말 · 성공 = 작은 채널 성공 사례(365일).",
          f"> 구독자 대비 = 조회수 ÷ 구독자. 큰 채널(구독자 {BIG_SUBS:,} 이상)은 채널 칸에 ★.", ""]
    for tk, t in TOPICS.items():
        d = df[df["topic"] == tk].sort_values("views", ascending=False)
        L_ += [f"## {t['name']} — {len(d)}편 (작은 채널 {int((d['subs'] <= SMALL_SUBS).sum())} · 큰 채널 {int((d['subs'] >= BIG_SUBS).sum())})", "",
               "| # | 조회수 | 구독자 | 구독자 대비 | 형식 | 올린 날 | 위험 | 소재 | 겨울 | 성공 | 제목 | 채널 | 검색어 |",
               "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
        for i, (_, r) in enumerate(d.iterrows(), 1):
            ratio = "-" if pd.isna(r["ratio"]) else f"×{r['ratio']:.1f}" if r["ratio"] < 100 else f"×{r['ratio']:,.0f}"
            star = "★ " if r["subs"] >= BIG_SUBS else ""
            subs = "숨김" if pd.isna(r["subs"]) else f"{int(r['subs']):,}"
            L_.append(f"| {i} | {int(r['views']):,} | {subs} | {ratio} | "
                      f"{r['format']} | {r['published']:%Y-%m-%d} | {'○' if r['safety'] else ''} | {'○' if r['focus'] else ''} | "
                      f"{'○' if r['winter_title'] else ''} | {'○' if r['success_365'] else ''} | {md_escape(r['title'])[:60]} | "
                      f"{star}{md_escape(r['channel'])[:20]} | {md_escape(r['query'])} |")
        L_.append("")
    L_ += [f"## 뺀 영상 — {len(dropped)}편", "", "| 주제 | 까닭 | 조회수 | 구독자 | 제목 | 채널 |", "|---|---|---|---|---|---|"]
    for _, r in dropped.sort_values(["topic", "reason", "views"], ascending=[True, True, False]).iterrows():
        subs = "숨김" if pd.isna(r["subs"]) else f"{int(r['subs']):,}"
        views = "-" if pd.isna(r["views"]) else f"{int(r['views']):,}"
        L_.append(f"| {TOPICS[r['topic']]['name']} | {r['reason']} | {views} | {subs} | {md_escape(r['title'])[:60]} | {md_escape(r['channel'])[:20]} |")
    out = OUT_DIR / "topic_demand_all.md"
    out.write_text("\n".join(L_) + "\n", encoding="utf-8")
    L("EXPORT", all_list=str(out.relative_to(ROOT)), rows=len(df), dropped=len(dropped))
    return out


def main(argv: list[str]) -> int:
    cl.setup_logging()
    mode = argv[1] if len(argv) > 1 else "analyze"
    if mode not in ("run", "analyze"):
        print(__doc__)
        return 2
    t0 = time.time()
    import os
    yt = cl.YT(key=next((os.environ[k].strip() for k in ("CRISIS_YOUTUBE_API_KEY", "YOUTUBE_API_KEY_CRISIS", "YOUTUBE_API_KEY") if os.environ.get(k, "").strip()), ""), offline=(mode == "analyze"))
    L("LOAD", version=VERSION, mode=mode, as_of=f"{AS_OF:%Y-%m-%d}", window_days=WINDOW_DAYS, seed=SEED,
      key_present=bool(yt.key), cache_dir=str(cl.CACHE_DIR.relative_to(ROOT.parent)))
    try:
        df, hit_df = load(yt)
    except RuntimeError as e:
        L("LOAD", logging.ERROR, error=str(e), next_step="run 으로 다시 (analyze 는 캐시만 읽음)")
        return 1
    raw = df
    val = validate(raw)
    df = features(on_topic(val))
    dropped = drop_table(raw, val, df)   # v1.2.0
    summ = summarize(df)
    qt = query_table(df, hit_df)
    out = export(df, summ, qt, yt, t0)
    export_all(df, dropped)              # v1.2.0
    L("EXPORT", report=str(out.relative_to(ROOT.parent)), units=yt.units, quota_dead=yt.quota_dead)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
