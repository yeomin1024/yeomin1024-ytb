#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.2 — 2026-11-28 — recount (의도 낱말 규칙을 바꾼 뒤 저장한 실행을 다시 세어 전후 비교) · '지난 실행' 칸도 지금 규칙으로 다시 셈 — 사용자 지시 2026-11-28 "1~3번 진행해".
# 이전 v1.1 — 2026-11-28 — 지난 실행 뒤 흐른 만큼만 갱신 (검색어마다 마지막 시각 · 시장은 지난 거래일 뒤 · 본 영상은 새 댓글만) — 사용자 지시
#          2026-11-28 "일단 예약 작업은 하지말고 탐색 시 시간체크해서 지난 만큼 업데이트하도록 하고".
# 이전 v1.0.1 — 2026-11-28 — 할당량이 댓글 도중에 끝나도 받은 댓글을 남김 (다른 세션).
# 이전 v1.0 — 2026-11-28 — 최초. 날마다(미국 장 마감 뒤) 주식 시청자 공통 관심 → 주제 후보 재료 — 사용자 지시 2026-11-28
#          "1은 그냥 댓글보면 알 수 있지 않나? 내가 댓글 본것만 봐도 soxl 등 주식 매수 타이밍 예측하는게 많던데 왜 이걸 파악 못해 … 3은 서두를 필요없이
#          최대한 많은 정보를 가지고 정확하게 판단하는게 먼저야 4는 근데 모두야 … 공통점을 찾으면 돼 … 6은 미장 끝나고 업데이트되면 해".
#
# CHANGELOG
#   v1.0 2026-11-28  run · selftest. ① 시장 숫자(tools/market_data.py) + 최근 5거래일 사건 ② 최근 DAYS 일 새 영상 검색(검색어 WORDS) → 영상 정보 →
#                    주식 관련·한국어만 ③ 조회수 ÷ 올린 지 시간 큰 순 TOP_VIDEOS 편 댓글(최근 순·공감 순 한 쪽씩 — 작성자 이름·채널 ID 없음)
#                    ④ 의도(무엇을 하려는지·알고 싶은지) 몫 — 이번 · 전체 성공 사례 댓글과 비교 ⑤ 갈래마다 공감 큰 원문 + Claude 가 읽을 표본.
#                    결과 = <주제>/result/next_topic/daily/<날짜>.md · <날짜>.json.gz · latest.md. 할당량 BUDGET 넘으면 거기서 멈추고 받은 것만.
#   v1.0.1 2026-11-28  fetch_comments — API 가 할당량 끝(SystemExit)을 내면 거기서 멈추고 그때까지 받은 영상 댓글을 돌려줌 (v1.0 은
#                    run() 에서 cms={} 가 되어 받은 댓글을 모두 버렸음 — '받은 것까지만 쓴다'는 설명과 달랐음). 영상마다 진행 줄(DEBUG)·
#                    20편마다 INFO 한 줄 (댓글 단계가 1분 넘게 조용했음).
#   v1.1 2026-11-28  예약 작업 없이 사람이 돌릴 때마다 '지난 실행 뒤 흐른 시간'만큼:
#                    · daily/state.json — 검색어마다 마지막으로 끝까지 찾은 시각(UTC) · 본 영상마다 댓글 받은 시각 · 마지막 시장 거래일 · 지난 결과 파일.
#                    · 검색 기간 = 그 검색어의 마지막 시각 − OVERLAP_HOURS(검색 색인이 늦게 잡는 영상) ~ 지금. 처음이면 DAYS 일. MAX_DAYS 보다 오래면
#                      거기까지만(건너뛴 기간을 로그·문서에). 기간이 CHUNK_DAYS 보다 길면 잘라서 오래된 쪽부터 찾음 (조회수 순 50개가 오래된 영상에만
#                      몰리지 않게) — 할당량이 끊기면 끝까지 찾은 조각까지만 기록해 다음 실행이 거기서 이어 감.
#                    · 댓글 = 처음 보는 영상은 전부, 앞서 본 영상은 그때 뒤에 달린 것만 (두 번 세지 않음).
#                    · 시장 = 지난 실행의 마지막 거래일 뒤 거래일 (★) + 앞 맥락 · 사건은 새 거래일에서만.
#                    · 결과 파일 = <날짜>_<시각>.md (하루에 여러 번 돌려도 안 덮음) · 3번 표에 '지난 실행' 칸.
#                    · v1.0.1 의 '할당량이 도중에 끝나도 받은 댓글 남김'도 같은 거르기(_keep)를 거침.
#                    · ↻ 다시 보기 — 지난 실행에서 댓글 받은 영상 중 올린 지 REVISIT_DAYS 안 · 시간당 조회수 상위 REVISIT_TOP 편은 새 정보를 받아
#                      그 뒤 달린 댓글만 더함 (기간이 좁아져도 며칠 된 인기 영상에 오늘 달리는 댓글 = 지금 관심을 놓치지 않게).
#   v1.2 2026-11-28  · recount <날짜[_시각]> — 저장한 json.gz 의 댓글·비교 댓글을 지금 [intent] 규칙으로 다시 세어 전후 표를 로그에 · json 에
#                      intent_today·intent_base 바꾸고 recount 기록(고치기 전 몫) · md 3~5번만 다시 씀 (0~2번 그대로) · latest.md 가 같은 실행이면 같이.
#                    · '지난 실행' 칸 = 지난 결과의 댓글을 지금 규칙으로 다시 셈 (v1.1 은 그때 규칙으로 센 몫 — 규칙을 바꾸면 비교가 어긋났음).
#                    · 3번 제목에 규칙 판 (daily_topic.toml VERSION) · 3~5번을 intent_lines() 하나로 (write·recount 같이 씀).
#
# 쓰는 법
#   python3 tools/daily_topic.py stock run [--budget 2500] [--words 12] [--top 120]
#   python3 tools/daily_topic.py stock plan        # 할당량 안 쓰고 이번에 찾을 기간·조각·예상 단위만 (읽기만)
#   python3 tools/daily_topic.py stock recount 2026-11-28   # 규칙을 바꾼 뒤 그 실행을 다시 셈 (할당량 안 씀)
#   python3 tools/daily_topic.py selftest
# 연구·교육용 — 투자 조언이 아님. 의도 몫은 낱말 세기 → 판단은 Claude 가 표본 원문을 읽고 (stock/guides/daily_topic.md).
from __future__ import annotations

import argparse
import datetime as dt
import gzip
import json
import logging
import re
import statistics as st
import sys
import time
import tomllib
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import market_data as md          # noqa: E402
import outlier_research as orr    # noqa: E402

VERSION = "v1.2"
ROOT = Path(__file__).resolve().parent.parent
KST = dt.timezone(dt.timedelta(hours=9))
HANGUL = re.compile(r"[가-힣]")
QUESTION = re.compile(r"\?|까요|나요|궁금|알려 ?주|어떻게 해야|뭔가요|인가요|할까|될까")


def log(stage: str, level: int = logging.INFO, **kv) -> None:
    ts = dt.datetime.now(KST).isoformat(timespec="seconds")
    logging.log(level, f"[{stage}] [{ts}] " + " ".join(f"{k}={v}" for k, v in kv.items()))


def load_cfg(folder: str) -> dict:
    p = ROOT / folder / "daily_topic.toml"
    d = tomllib.loads(p.read_text("utf-8"))
    d["_intent"] = [(k, re.compile(v, re.I)) for k, v in (d.get("intent") or {}).items()]
    return d


def iso_dur(s: str) -> int:
    m = re.fullmatch(r"P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", s or "")
    if not m:
        return 0
    d, h, mi, se = (int(x or 0) for x in m.groups())
    return d * 86400 + h * 3600 + mi * 60 + se


UTC = dt.timezone.utc
ISO = "%Y-%m-%dT%H:%M:%SZ"


def iso(t: dt.datetime) -> str:
    return t.astimezone(UTC).strftime(ISO)


def parse_iso(s: str) -> dt.datetime:
    return dt.datetime.fromisoformat(s.replace("Z", "+00:00")).astimezone(UTC)


def state_path(folder: str) -> Path:
    return ROOT / folder / "result/next_topic/daily/state.json"


def load_state(folder: str) -> dict:
    p = state_path(folder)
    if not p.is_file():
        return {"words": {}, "seen": {}, "market_date": "", "last_file": "", "last_run": ""}
    try:
        d = json.loads(p.read_text("utf-8"))
    except json.JSONDecodeError as e:                            # 깨진 기록으로 기간을 잘못 잡지 않게 — 멈추고 알림
        raise SystemExit(f"[STATE] {p} 를 읽지 못함 ({e}) — 파일을 고치거나 지우면 처음처럼 DAYS 일로 찾음")
    for k, v in (("words", {}), ("seen", {}), ("market_date", ""), ("last_file", ""), ("last_run", "")):
        d.setdefault(k, v)
    return d


def save_state(folder: str, stt: dict, keep_days: int = 30) -> None:
    cut = iso(dt.datetime.now(UTC) - dt.timedelta(days=keep_days))
    stt["seen"] = {k: v for k, v in stt["seen"].items() if v >= cut}       # 한 달 지난 영상은 잊음
    p = state_path(folder)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(stt, ensure_ascii=False, indent=1, sort_keys=True) + "\n", "utf-8")


def windows(cfg: dict, stt: dict, words: list[str], now: dt.datetime) -> dict:
    """검색어마다 [시작, 끝] 조각들 (오래된 쪽부터) + 설명. 할당량은 쓰지 않음."""
    S = cfg.get("search") or {}
    days0, maxd = float(S.get("DAYS", 3)), float(S.get("MAX_DAYS", 14))
    ovl, chunk = float(S.get("OVERLAP_HOURS", 6)), float(S.get("CHUNK_DAYS", 3))
    out = {}
    for w in words:
        last = stt["words"].get(w)
        start = parse_iso(last) - dt.timedelta(hours=ovl) if last else now - dt.timedelta(days=days0)
        skipped = ""
        if now - start > dt.timedelta(days=maxd):
            skipped = f"{iso(start)[:16]} ~ {iso(now - dt.timedelta(days=maxd))[:16]}"
            start = now - dt.timedelta(days=maxd)
        parts, a = [], start
        while a < now:
            b = min(a + dt.timedelta(days=chunk), now)
            parts.append((a, b))
            a = b
        out[w] = {"last": last or "", "start": start, "parts": parts, "skipped": skipped,
                  "why": (f"지난 실행 {last[:16]} − 겹침 {ovl:g}시간" if last else f"처음 — 최근 {days0:g}일")}
    return out


# ─────────────────────────────── ① 시장
def market_events(folder: str, since: str = "", n: int = 5) -> dict:
    """지난 실행의 마지막 거래일(since) 뒤 거래일 = 새(★) + 앞 맥락 (모두 합쳐 n 거래일 이상, 20 이하).
    사건(반도체 ±5% · 나스닥 ±3% · 코스피 ±3% · SOXL ±15%)은 새 거래일에서만 (처음이면 최근 n 거래일). + 고점 대비·20일 저점 대비."""
    M = md.load(folder)
    spx = M.get("^GSPC") or {}
    alld = sorted(spx)
    newd = [d for d in alld if d > since] if since else alld[-n:]
    days = alld[-min(max(n, len(newd)), 20):]
    rows, events = [], []
    for d in days:
        r = {"date": d, "new": d in newd}
        for sym in ("^GSPC", "^IXIC", "^SOX", "^VIX", "SOXL", "NVDA"):
            x = (M.get(sym) or {}).get(d)
            r[sym] = x
        rows.append(r)
        if d not in newd:
            continue
        sox, ndq, soxl = ((M.get("^SOX") or {}).get(d) or {}).get("chg"), ((M.get("^IXIC") or {}).get(d) or {}).get("chg"), ((M.get("SOXL") or {}).get(d) or {}).get("chg")
        if sox is not None and abs(sox) >= 5 or ndq is not None and abs(ndq) >= 3 or soxl is not None and abs(soxl) >= 15:
            events.append(f"{d} 미국: 반도체 {sox:+.1f}% · 나스닥 {ndq:+.1f}% · SOXL {soxl:+.1f}%")
    ks = M.get("^KS11") or {}
    for d in sorted(ks):
        if not (d > since if since else d >= (days[0] if days else "")):
            continue
        c = ks[d]["chg"]
        if c is not None and abs(c) >= 3:
            events.append(f"{d} 코스피 {c:+.1f}%")
    state = {}
    for sym in ("^SOX", "^IXIC", "^KS11", "005930.KS", "000660.KS", "SOXL", "NVDA", "TSLA", "^VIX", "KRW=X"):
        x = M.get(sym) or {}
        if not x:
            continue
        ds = sorted(x)
        last = x[ds[-1]]
        low20 = min(x[d]["close"] for d in ds[-20:])
        state[sym] = {"name": md.SYMBOLS[sym][0], "date": ds[-1], "close": last["close"], "chg": last["chg"], "from_high": last["from_high"],
                      "from_low20": round((last["close"] / low20 - 1) * 100, 1)}
    return {"rows": rows, "events": events, "state": state, "new_days": newd[-20:], "last_date": alld[-1] if alld else since}


# ─────────────────────────────── ② 새 영상
def fresh_videos(folder: str, cfg: dict, api, wins: dict, budget: int, done: dict) -> list[dict]:
    """wins = windows() 결과. 조각을 끝까지 찾을 때마다 done[검색어] = 그 조각 끝 (UTC) — 할당량이 끊겨도 받은 곳까지 기록."""
    S = cfg.get("search") or {}
    mx = int(S.get("MAX_RESULTS", 50))
    _, exclude, _, _, rel = orr.load_keywords(folder, 0)
    ids, src = [], {}
    stop = False
    pend = {}                                                   # 끝까지 찾은 조각 — 영상 정보까지 받은 뒤에만 done 에 (중간에 끊기면 다음 실행이 같은 기간부터)
    for w, W in wins.items():
        if W["skipped"]:
            log("SEARCH", logging.WARNING, word=w, note="MAX_DAYS 보다 오래 — 이 기간은 건너뜀", skipped=W["skipped"])
        for a, b in W["parts"]:
            if api.units + 100 > budget:
                log("SEARCH", logging.WARNING, note="할당량 한도 — 남은 조각은 다음 실행이 이어 감", word=w, part=f"{iso(a)[:16]}~{iso(b)[:16]}",
                    units=api.units, budget=budget)
                stop = True
                break
            j = api.get("search", part="snippet", q=w, type="video", publishedAfter=iso(a), publishedBefore=iso(b), order="viewCount",
                        maxResults=mx, regionCode="KR", relevanceLanguage="ko")
            if j.get("_error"):
                log("SEARCH", logging.WARNING, word=w, error=str(j.get("_error"))[:120], next="이 검색어는 다음 실행에 같은 기간부터")
                break
            got = [it["id"]["videoId"] for it in j.get("items", []) if it.get("id", {}).get("videoId")]
            for i in got:
                src.setdefault(i, [])
                if w not in src[i]:
                    src[i].append(w)
                if i not in ids:
                    ids.append(i)
            pend[w] = iso(b)
            log("SEARCH", word=w, part=f"{iso(a)[:16]}~{iso(b)[:16]}", results=len(got), full=len(got) >= mx, new_total=len(ids), units=api.units)
            if len(got) >= mx:
                log("SEARCH", logging.DEBUG, word=w, note="결과가 꽉 참 — 조회수 낮은 영상은 빠졌을 수 있음 (CHUNK_DAYS 를 줄이면 더 촘촘)")
        if stop:
            break
    vids = video_info(folder, api, ids, src)
    done.update(pend)
    log("VIDEOS", searched=len(ids), kept=len(vids), shorts=sum(1 for v in vids if v["short"]), rule="한국어 · 라이브 아님 · 주식 관련어 · 제외 낱말 없음", units=api.units)
    return vids


def video_info(folder: str, api, ids: list[str], src: dict) -> list[dict]:
    """videos.list (50개 1단위) → 한국어·라이브 아님·주식 관련어·제외 낱말 없음만. 시간당 조회수 큰 순."""
    _, exclude, _, _, rel = orr.load_keywords(folder, 0)
    vids = []
    for k in range(0, len(ids), 50):
        j = api.get("videos", part="snippet,statistics,contentDetails,liveStreamingDetails", id=",".join(ids[k:k + 50]), maxResults=50)
        for it in j.get("items", []):
            sn, stt, cd = it["snippet"], it.get("statistics", {}), it.get("contentDetails", {})
            t = sn.get("title", "")
            info = {"title": t, "tags": sn.get("tags") or [], "description": sn.get("description", "")}
            if not HANGUL.search(t) or any(x and x in t for x in exclude) or it.get("liveStreamingDetails") or sn.get("liveBroadcastContent") != "none":
                continue
            if not orr.relevant(info, rel):
                continue
            pub = dt.datetime.fromisoformat(sn["publishedAt"].replace("Z", "+00:00"))
            hrs = max((dt.datetime.now(dt.timezone.utc) - pub).total_seconds() / 3600, 1)
            v = int(stt.get("viewCount", 0) or 0)
            sec = iso_dur(cd.get("duration", ""))
            vids.append({"id": it["id"], "title": t, "channel": sn.get("channelTitle", ""), "published": sn["publishedAt"][:16], "views": v,
                         "likes": int(stt.get("likeCount", 0) or 0), "comments": int(stt.get("commentCount", 0) or 0), "sec": sec, "short": sec <= 180,
                         "vph": round(v / hrs, 1), "words": src.get(it["id"], [])})
    return sorted(vids, key=lambda v: -v["vph"])


def revisit_ids(folder: str, cfg: dict, stt: dict, now: dt.datetime, skip: set) -> list[str]:
    """지난 실행에서 댓글을 받은 영상 중 올린 지 REVISIT_DAYS 안 · 시간당 조회수 큰 순 REVISIT_TOP — 그 뒤 달린 댓글을 더 받으려고.
    (검색 기간은 지난 실행 뒤로 좁아지므로, 며칠 된 영상에 오늘 달리는 댓글 = 지금 관심을 놓치지 않게)"""
    C = cfg.get("comments") or {}
    days, top = float(C.get("REVISIT_DAYS", 3)), int(C.get("REVISIT_TOP", 40))
    f = stt.get("last_file") or ""
    p = ROOT / folder / "result/next_topic/daily" / f
    if not f or not p.is_file() or top <= 0:
        return []
    try:
        with gzip.open(p, "rt", encoding="utf-8") as fh:
            prev = json.load(fh).get("videos") or []
    except (OSError, json.JSONDecodeError) as e:
        log("REVISIT", logging.WARNING, note="지난 결과를 읽지 못함 — 다시 보기 없음", file=f, error=str(e)[:100])
        return []
    cut = iso(now - dt.timedelta(days=days))[:16]
    xs = [v for v in prev if v["id"] in stt["seen"] and v["id"] not in skip and v.get("published", "") >= cut]
    xs.sort(key=lambda v: -float(v.get("vph") or 0))
    log("REVISIT", candidates=len(xs), pick=min(len(xs), top), rule=f"지난 실행에서 댓글 받은 영상 · 올린 지 {days:g}일 안 · 시간당 조회수 큰 순")
    return [v["id"] for v in xs[:top]]


# ─────────────────────────────── ③ 댓글
def fetch_comments(api, vids: list[dict], top: int, budget: int, shorts: bool, seen: dict, fetched: dict) -> dict:
    """처음 보는 영상 = 댓글 전부 · 앞서 본 영상(seen[id] = 그때 시각) = 그 뒤에 달린 것만. fetched[id] = 이번에 받은 시각."""
    out = {}
    cnt = {"old": 0, "cut": 0}
    pick = [v for v in vids if shorts or not v["short"]][:top]

    def _keep(vid: str, got: dict) -> None:
        fetched[vid] = iso(dt.datetime.now(UTC))
        xs = list(got.values())
        if vid in seen:                                         # 두 번 세지 않음 — 지난번 받은 뒤 달린 댓글만
            cnt["old"] += 1
            n0 = len(xs)
            xs = [c for c in xs if c["t"] > seen[vid][:16]]
            cnt["cut"] += n0 - len(xs)
        out[vid] = xs

    for v in pick:
        if v["comments"] == 0:
            continue
        if api.units + 2 > budget:
            log("COMMENTS", logging.WARNING, note="할당량 한도 — 남은 영상 건너뜀", done=len(out), units=api.units)
            break
        got = {}
        for order in ("time", "relevance"):
            try:
                j = api.get("commentThreads", part="snippet", videoId=v["id"], order=order, maxResults=100, textFormat="plainText")
            except SystemExit as e:                            # v1.0.1 할당량 끝 — 이 영상 것까지 남기고 멈춤 (받은 것은 버리지 않음)
                if got:
                    _keep(v["id"], got)
                log("COMMENTS", logging.WARNING, note="API 멈춤 — 받은 것까지만", error=str(e)[:160], done=len(out), units=api.units,
                    next="한국 17시 할당량 초기화 뒤 다시")
                log("COMMENTS", videos=len(out), comments=sum(len(x) for x in out.values()), seen_before=cnt["old"], dropped_old_comments=cnt["cut"], units=api.units)
                return out
            if j.get("_error"):
                log("COMMENTS", logging.DEBUG, video=v["id"], skipped=j["_error"])
                break
            for it in j.get("items", []):
                s = it["snippet"]["topLevelComment"]["snippet"]
                got[it["id"]] = {"id": it["id"], "t": s["publishedAt"][:16], "like": int(s.get("likeCount", 0) or 0), "reply": int(it["snippet"].get("totalReplyCount", 0) or 0),
                                 "text": re.sub(r"\s+", " ", s.get("textDisplay", ""))[:400]}     # 작성자 이름·채널 ID 는 넣지 않음 (CLAUDE.md)
        _keep(v["id"], got)
        log("COMMENTS", logging.INFO if len(out) % 20 == 0 else logging.DEBUG, progress=f"{len(out)}/{len(pick)}", video=v["id"], got=len(out[v["id"]]), units=api.units)
    log("COMMENTS", videos=len(out), comments=sum(len(x) for x in out.values()), seen_before=cnt["old"], dropped_old_comments=cnt["cut"], units=api.units)
    return out


# ─────────────────────────────── ④ 의도
def intent_shares(texts: list[str], intents) -> dict:
    n = len(texts)
    res = {}
    for k, rx in intents:
        m = sum(1 for t in texts if rx.search(t))
        res[k] = {"n": m, "pct": round(m / n * 100, 1) if n else None}
    timing = [k for k, _ in intents][:4]                        # 앞 넷 = 매수 타이밍·바닥·추가 하락·가격 예측
    anyk = sum(1 for t in texts if any(rx.search(t) for k, rx in intents if k in timing))
    res["_timing_any"] = {"n": anyk, "pct": round(anyk / n * 100, 1) if n else None}
    return res


def baseline_texts(folder: str) -> list[str]:
    """비교용 — 성공 사례 승인 자료의 댓글 전부 (답글·영상 주인 뺌)."""
    out = []
    for p in (ROOT / folder / "result/outliers").glob("W_*/comments.jsonl"):
        for ln in p.open(encoding="utf-8"):
            try:
                c = json.loads(ln)
            except json.JSONDecodeError:
                continue
            if not c.get("parent") and not c.get("creator"):
                out.append(str(c.get("text", "")))
    return out


# ─────────────────────────────── 문서
def rules_version(folder: str) -> str:
    m = re.search(r"VERSION:\s*(v[\d.]+)", (ROOT / folder / "daily_topic.toml").read_text("utf-8"))
    return f"daily_topic.toml {m.group(1) if m else '?'}"


def pairs(j: dict) -> list[tuple[dict, dict]]:
    """저장한 실행 → (댓글, 영상) 쌍."""
    vmap = {v["id"]: v for v in j.get("videos") or []}
    return [(c, vmap.get(vid, {"id": vid, "title": ""})) for vid, xs in (j.get("comments") or {}).items() for c in xs]


def prev_intent(folder: str, stt: dict, intents) -> tuple[str, dict]:
    """지난 실행 댓글을 지금 규칙으로 다시 센 몫 (v1.2 — 규칙이 바뀌어도 같은 잣대로 비교). 없으면 빈 것."""
    f = stt.get("last_file") or ""
    p = ROOT / folder / "result/next_topic/daily" / f
    if not f or not p.is_file():
        return "", {}
    try:
        with gzip.open(p, "rt", encoding="utf-8") as fh:
            j = json.load(fh)
    except (OSError, json.JSONDecodeError) as e:
        log("WRITE", logging.WARNING, note="지난 결과를 읽지 못함 — '지난 실행' 칸 비움", file=f, error=str(e)[:100])
        return "", {}
    return j.get("stamp") or j.get("date", ""), intent_shares([c["text"] for c, _ in pairs(j)], intents)


def intent_lines(folder: str, intents, allc: list, now_sh: dict, base_sh: dict, prev_sh: dict, pstamp: str, nbase: int, note: str = "") -> list[str]:
    """결과 문서 3~5번 (write·recount 같이 씀)."""
    L = []
    A = L.append
    A(f"## 3. 시청자가 무엇을 하려는지·알고 싶은지 (이번 기간 댓글 {len(allc):,}개 — 앞서 본 영상은 그 뒤 댓글만 · 비교 = 지난 실행({pstamp or '없음'}) · "
      f"승인 자료(분석 사례) 댓글 전부 {nbase:,}개 · 규칙 {rules_version(folder)} — 모든 칸 같은 규칙)\n")
    if note:
        A(note + "\n")
    A("| 의도 | 이번 | 지난 실행 | 분석 사례 댓글(전체 기간) | 배수 (이번 ÷ 분석 사례) |")
    A("|---|---|---|---|---|")
    rows = [("_timing_any", "**매수 타이밍·바닥·하락·가격 예측 (넷 중 하나라도)**")] + [(k, k) for k, _ in intents]
    pc = lambda x: "–" if x is None else f"{x}%"
    for key, label in rows:
        a, b, c = now_sh[key], base_sh[key], prev_sh.get(key) or {}
        A(f"| {label} | {pc(a['pct'])} ({a['n']:,}) | {pc(c.get('pct'))} | {pc(b['pct'])} | "
          f"{('%.1f배' % (a['pct'] / b['pct'])) if a['pct'] and b['pct'] else '–'} |")
    A("")
    A("## 4. 갈래마다 공감 큰 댓글 (원문 · 작성자 이름 없음)\n")
    for k, rx in intents:
        xs = sorted([(c, v) for c, v in allc if rx.search(c["text"])], key=lambda cv: -cv[0]["like"])[:5]
        if not xs:
            continue
        A(f"**{k}**")
        for c, v in xs:
            A(f"- ({c['like']}) {c['text'][:160]} — 「{v['title'][:30]}」")
        A("")
    A("## 5. 질문만 (공감 순 30)\n")
    qs = sorted([(c, v) for c, v in allc if QUESTION.search(c["text"])], key=lambda cv: -cv[0]["like"])[:30]
    for c, v in qs:
        A(f"- ({c['like']}) {c['text'][:160]} — 「{v['title'][:30]}」")
    A("")
    return L


def write(folder: str, cfg: dict, mk: dict, vids: list[dict], cms: dict, units: int, t0: float, wins: dict, done: dict, stt: dict) -> Path:
    now = dt.datetime.now(KST)
    today, stamp = now.date().isoformat(), now.strftime("%Y-%m-%d_%H%M")
    od = ROOT / folder / "result/next_topic/daily"
    od.mkdir(parents=True, exist_ok=True)
    intents = cfg["_intent"]
    allc = [(c, v) for v in vids for c in cms.get(v["id"], [])]
    texts = [c["text"] for c, _ in allc]
    base = baseline_texts(folder)
    now_sh, base_sh = intent_shares(texts, intents), intent_shares(base, intents)
    pstamp, prev_sh = prev_intent(folder, stt, intents)
    L = []
    A = L.append
    A(f"# 주식 시청자 관심 — {now.strftime('%Y-%m-%d %H:%M')} KST\n")
    A(f"VERSION: `tools/daily_topic.py {VERSION}` 가 만듦 · 판단(주제 후보)은 Claude 가 아래 표본 원문을 읽고 `stock/result/next_topic/next_topic.md` A절에 (`stock/guides/daily_topic.md`).")
    A("※ 연구·교육용 — 투자 조언이 아님. 의도 몫은 낱말 세기(한 댓글이 여러 갈래에 들 수 있음).\n")
    A("## 0. 이번에 갱신한 기간 (지난 실행 뒤 흐른 만큼)\n")
    A(f"- 지난 실행: {stt.get('last_run') or '없음 (처음)'} · 이번: {iso(now)} (UTC) · 지난 결과 `{stt.get('last_file') or '-'}`")
    A(f"- 시장: 지난 마지막 거래일 {stt.get('market_date') or '-'} 뒤 새 거래일 {len(mk.get('new_days') or [])}일 ({', '.join(mk.get('new_days') or []) or '없음 — 그 뒤 미국 장이 열리지 않음'})")
    A("\n| 검색어 | 찾은 기간 (UTC) | 까닭 | 조각 | 끝까지 찾음 |")
    A("|---|---|---|---|---|")
    for w, W in wins.items():
        d = done.get(w)
        A(f"| {w} | {iso(W['start'])[:16]} ~ {(d or '-')[:16]} | {W['why']}{' · 건너뜀 ' + W['skipped'] if W['skipped'] else ''} | {len(W['parts'])} | "
          f"{'✅' if d and d >= iso(W['parts'][-1][1]) else ('⚠️ ' + d[:16] + ' 까지 — 다음 실행이 이어 감' if d else '❌ 못 찾음 — 다음 실행이 같은 기간부터')} |")
    A("")
    A("## 1. 시장 — 미국 거래일 (종가 하루 변화 · ★ = 지난 실행 뒤 새 거래일)\n")
    A("| 날짜 | S&P500 | 나스닥 | 반도체 | VIX | SOXL | 엔비디아 |")
    A("|---|---|---|---|---|---|---|")
    for r in mk["rows"]:
        f = lambda s: "–" if not r.get(s) else (f"{r[s]['close']:.1f}" if s == "^VIX" else f"{r[s]['chg']:+.1f}%" if r[s]["chg"] is not None else "–")
        A(f"| {'★ ' if r.get('new') else ''}{r['date']} | {f('^GSPC')} | {f('^IXIC')} | {f('^SOX')} | {f('^VIX')} | {f('SOXL')} | {f('NVDA')} |")
    A("\n- 새 거래일 사건(반도체 ±5% · 나스닥 ±3% · SOXL ±15% · 코스피 ±3%): " + (" · ".join(mk["events"]) or "없음"))
    A("- 지금: " + " · ".join(f"{s['name']} {s['chg']:+.1f}% (1년 고점 대비 {s['from_high']:.0f}% · 20일 저점 대비 {s['from_low20']:+.0f}%)" for s in mk["state"].values() if s.get("chg") is not None) + "\n")
    A("## 2. 이번 기간 새 영상 — 조회수 ÷ 올린 지 시간 큰 순\n")
    nre = sum(1 for v in vids if v.get("revisit"))
    A(f"검색어 {len(set(w for v in vids for w in v['words']))}개로 찾은 한국어 주식 영상 {len(vids) - nre}편 (쇼츠 {sum(1 for v in vids if v['short'] and not v.get('revisit'))} · 겹침 시간에 앞서 본 영상 {sum(1 for v in vids if v['id'] in stt['seen'] and not v.get('revisit'))})"
      f" + ↻ 다시 본 영상 {nre}편 (지난 실행 영상 중 올린 지 {(cfg.get('comments') or {}).get('REVISIT_DAYS', 3)}일 안 — 그 뒤 댓글만) · 댓글 받은 {len(cms)}편 · 할당량 {units}단위.\n")
    A("| # | 올린 때(UTC) | 제목 | 채널 | 조회수 | 시간당 | 길이 | 댓글 |")
    A("|---|---|---|---|---|---|---|---|")
    for i, v in enumerate(vids[:30], 1):
        A(f"| {i}{' ↻' if v.get('revisit') else ''} | {v['published'][5:]} | [{v['title'][:55].replace('|', '｜')}](https://www.youtube.com/watch?v={v['id']}) | {v['channel'][:12].replace('|', '｜')} | {v['views']:,} | {v['vph']:,.0f} | {'쇼츠' if v['short'] else str(round(v['sec'] / 60)) + '분'} | {v['comments']:,} |")
    A("")
    L += intent_lines(folder, intents, allc, now_sh, base_sh, prev_sh, pstamp, len(base))
    p = od / f"{stamp}.md"
    p.write_text("\n".join(L) + "\n", "utf-8")
    (od / "latest.md").write_text("\n".join(L) + "\n", "utf-8")
    with gzip.open(od / f"{stamp}.json.gz", "wt", encoding="utf-8") as f:
        json.dump({"date": today, "stamp": stamp, "tool": f"daily_topic.py {VERSION}", "market": mk, "videos": vids, "comments": cms,
                   "windows": {w: {"start": iso(W["start"]), "done": done.get(w, ""), "skipped": W["skipped"]} for w, W in wins.items()},
                   "intent_today": now_sh, "intent_base": base_sh, "intent_rules": rules_version(folder)}, f, ensure_ascii=False)
    log("WRITE", md=str(p.relative_to(ROOT)), videos=len(vids), comments=len(texts), timing_any=now_sh["_timing_any"]["pct"], base=base_sh["_timing_any"]["pct"],
        sec=round(time.time() - t0, 1))
    return p


def run(folder: str, budget: int, nwords: int, top: int) -> int:
    t0 = time.time()
    import topic_state
    if folder in topic_state.disabled():
        log("SKIP", folder=folder, note="꺼 둔 주제 (studio/state/topics.json) — 하지 않음")
        return 0
    cfg = load_cfg(folder)
    stt = load_state(folder)
    now = dt.datetime.now(UTC)
    words = list((cfg.get("search") or {}).get("WORDS") or [])[:nwords]
    wins = windows(cfg, stt, words, now)
    log("CONFIG", folder=folder, words=len(words), budget=budget, top=top, intents=len(cfg["_intent"]), last_run=stt["last_run"] or "없음",
        parts=sum(len(W["parts"]) for W in wins.values()), seen_videos=len(stt["seen"]))
    if md.fetch(folder, "1y") != 0:
        log("MARKET", logging.WARNING, note="시장 숫자 받기 실패 — 지난 숫자로 계속", next="네트워크 허용 목록 query1.finance.yahoo.com 확인")
    mk = market_events(folder, stt["market_date"])
    log("MARKET", since=stt["market_date"] or "처음", new_days=len(mk["new_days"]), events=len(mk["events"]), last=mk["last_date"])
    import next_topic as nt
    api = nt.Api()
    done, fetched, vids, cms = {}, {}, [], {}
    try:
        vids = fresh_videos(folder, cfg, api, wins, budget, done)
        rv = revisit_ids(folder, cfg, stt, now, {v["id"] for v in vids})
        old = video_info(folder, api, rv, {}) if rv else []
        for v in old:
            v["revisit"] = True
        shorts = bool((cfg.get("comments") or {}).get("SHORTS", True))
        cms = fetch_comments(api, vids, top, budget, shorts, stt["seen"], fetched)
        cms.update(fetch_comments(api, old, len(old), budget, shorts, stt["seen"], fetched))
        vids = sorted(vids + old, key=lambda v: -v["vph"])
    except SystemExit as e:                                    # 할당량 끝 — 받은 것까지만 쓰고, 끝까지 찾은 조각까지만 기록
        log("API", logging.WARNING, error=str(e)[:160], next="한국 17시 할당량 초기화 뒤 다시 — 다음 실행이 끊긴 곳부터")
    p = write(folder, cfg, mk, vids, cms, api.units, t0, wins, done, stt)
    stt["words"].update(done)
    stt["seen"].update(fetched)
    stt["market_date"] = mk["last_date"] or stt["market_date"]
    stt["last_run"] = iso(now)
    stt["last_file"] = p.with_suffix("").name + ".json.gz"
    save_state(folder, stt)
    log("STATE", file=str(state_path(folder).relative_to(ROOT)), words_done=f"{len(done)}/{len(words)}", market_date=stt["market_date"], seen=len(stt["seen"]))
    return 0


def recount(folder: str, stamp: str) -> int:
    """규칙을 바꾼 뒤 저장한 실행을 다시 셈 — 할당량 안 씀. 전후 표 로그 · json 의도 몫 바꿈(고치기 전 몫은 recount 기록에) · md 3~5번만 다시."""
    t0 = time.time()
    od = ROOT / folder / "result/next_topic/daily"
    jp, mp = od / f"{stamp}.json.gz", od / f"{stamp}.md"
    if not jp.is_file() or not mp.is_file():
        log("RECOUNT", logging.WARNING, note="그 실행 파일이 없음", json=str(jp.relative_to(ROOT)), next="daily/ 의 <날짜>[_시각] 이름으로")
        return 1
    cfg = load_cfg(folder)
    intents = cfg["_intent"]
    with gzip.open(jp, "rt", encoding="utf-8") as fh:
        j = json.load(fh)
    allc = pairs(j)
    base = baseline_texts(folder)
    new_today, new_base = intent_shares([c["text"] for c, _ in allc], intents), intent_shares(base, intents)
    old_today, old_base = j.get("intent_today") or {}, j.get("intent_base") or {}
    olds = sorted(x.name for x in od.glob("*.json.gz") if x.name < jp.name)       # 바로 앞 실행 — 같은 규칙으로
    pstamp, prev_sh = prev_intent(folder, {"last_file": olds[-1] if olds else ""}, intents)
    rv, was = rules_version(folder), j.get("intent_rules") or "daily_topic.toml v1.1 이하"
    log("RECOUNT", file=jp.name, comments=len(allc), base=len(base), rules_before=was, rules_after=rv)
    print(f"\n| 의도 | 이번 전 → 후 | 분석 사례 전 → 후 | 배수 전 → 후 |\n|---|---|---|---|")
    rows = [("_timing_any", "타이밍 넷 중 하나")] + [(k, k) for k, _ in intents]
    # 갈래 이름이 바뀐 것 (v1.2 '원인·이유 (왜)' → '원인·이유 (왜 오르고 내리나)') — 앞부분이 같으면 같은 갈래로 봄
    def old_of(d, k):
        if k in d:
            return d[k]
        for kk, vv in d.items():
            if kk.split(" (")[0] == k.split(" (")[0]:
                return vv
        return {}
    ratio = lambda a, b: f"{a / b:.1f}배" if a and b else "–"
    for key, label in rows:
        oa, ob, na, nb = old_of(old_today, key), old_of(old_base, key), new_today[key], new_base[key]
        print(f"| {label} | {oa.get('pct')}% ({oa.get('n')}) → {na['pct']}% ({na['n']}) | {ob.get('pct')}% → {nb['pct']}% | "
              f"{ratio(oa.get('pct'), ob.get('pct'))} → {ratio(na['pct'], nb['pct'])} |")
    now = dt.datetime.now(KST)
    j.setdefault("recount", []).append({"at": now.isoformat(timespec="seconds"), "rules_before": was, "rules_after": rv,
                                        "before_today": old_today, "before_base": old_base})
    j["intent_today"], j["intent_base"], j["intent_rules"] = new_today, new_base, rv
    with gzip.open(jp, "wt", encoding="utf-8") as fh:
        json.dump(j, fh, ensure_ascii=False)
    md_old = mp.read_text("utf-8")
    cut = md_old.find("\n## 3. ")
    if cut < 0:
        log("RECOUNT", logging.WARNING, note="md 에 3번 절이 없음 — json 만 바꿈", md=mp.name)
        return 1
    ot, nt_ = old_of(old_today, "_timing_any"), new_today["_timing_any"]
    note = (f"> {now.strftime('%Y-%m-%d %H:%M')} KST 다시 셈 (`daily_topic.py recount {stamp}`) — 규칙 {was} → {rv}. "
            f"타이밍 넷 중 하나 {ot.get('pct')}% → {nt_['pct']}% · 고치기 전 몫은 json `recount` 에. 1~2번(시장·영상)은 그대로.")
    md_new = md_old[:cut + 1] + "\n".join(intent_lines(folder, intents, allc, new_today, new_base, prev_sh, pstamp, len(base), note)) + "\n"
    mp.write_text(md_new, "utf-8")
    lt = od / "latest.md"
    if lt.is_file() and lt.read_text("utf-8") == md_old:
        lt.write_text(md_new, "utf-8")
    log("RECOUNT", md=mp.name, latest_updated=lt.is_file() and lt.read_text("utf-8") == md_new, timing_before=ot.get("pct"), timing_after=nt_["pct"],
        sec=round(time.time() - t0, 1))
    return 0


def plan(folder: str, nwords: int, top: int) -> int:
    """할당량 안 쓰고 이번에 찾을 기간·조각·예상 단위 (읽기만)."""
    cfg = load_cfg(folder)
    stt = load_state(folder)
    now = dt.datetime.now(UTC)
    words = list((cfg.get("search") or {}).get("WORDS") or [])[:nwords]
    wins = windows(cfg, stt, words, now)
    parts = sum(len(W["parts"]) for W in wins.values())
    print(f"지난 실행 {stt['last_run'] or '없음'} · 지금 {iso(now)} · 시장 지난 거래일 {stt['market_date'] or '-'}")
    for w, W in wins.items():
        print(f"  {w:10s} {iso(W['start'])[:16]} ~ {iso(now)[:16]}  조각 {len(W['parts'])}  ({W['why']}{' · 건너뜀 ' + W['skipped'] if W['skipped'] else ''})")
    rv = len(revisit_ids(folder, cfg, stt, now, set()))
    est = parts * 100 + 10 + top * 2 + rv * 2 + (rv + 49) // 50
    print(f"↻ 다시 볼 영상 ≤{rv}편 (지난 실행 {stt.get('last_file') or '-'})")
    print(f"예상 할당량 ≈ 검색 {parts}×100 + 영상 정보 ~10 + 댓글 ≤{top}×2 + 다시 보기 ≤{rv}×2 = {est:,}단위 (한도 BUDGET {cfg['comments']['BUDGET']})")
    return 0


def selftest() -> int:
    ok = True

    def check(name, cond):
        nonlocal ok
        print(("PASS " if cond else "FAIL ") + name)
        ok = ok and bool(cond)
    cfg = load_cfg("stock")
    sh = intent_shares(["지금 SOXL 사도 될까요?", "바닥은 아직 멀었다 더 빠진다", "감사합니다"], cfg["_intent"])
    check("의도 — 매수 타이밍·추가 하락·넷 중 하나", sh["매수 타이밍 (살까·언제·들어가)"]["n"] == 1 and sh["추가 하락 예측"]["n"] == 1 and sh["_timing_any"]["n"] == 2)
    check("길이 읽기", iso_dur("PT1H2M3S") == 3723 and iso_dur("PT45S") == 45)
    R = dict(cfg["_intent"])
    neg = {"매도·익절": ["공매도 금지 안 시키냐", "외인매도전환 매도세", "집팔아 주식한 사람", "깔끔하게 정리 잘해 주셔서"],
           "분노·탓": ["일정부분 만회하는 반등"], "바닥·반등 예측": ["이바닥에서 전문가는", "오른다 내린다 하는 인간들 사기", "기회주의 젓문가들", "전세월세떡상"],
           "가격·시점 예측 (숫자·날짜)": ["코스피 200 선물지수로는", "9월29일에 샀네"], "추가 하락 예측": ["외국인 천국 개인 지옥"],
           "계좌·세금": ["계좌 녹아납니다", "깡통계좌"], "종목·상품 고르기 (뭘 살까)": ["OO 추천하고 샀는데 -72%"]}
    pos = {"매도·익절": ["지금 매도할까요", "익절했습니다", "전량 정리했어요"], "분노·탓": ["정부는 뭐하냐", "공매도 세력"],
           "바닥·반등 예측": ["4000이 바닥일지는", "저점 매수", "반등 나옵니다", "다시 오르면"], "가격·시점 예측 (숫자·날짜)": ["4500선 지키면", "내년 1분기", "5만원 간다"],
           "추가 하락 예측": ["더 떨어질 텐데", "하락 지옥"], "계좌·세금": ["ISA 계좌로", "연금저축펀드", "양도세 얼마"]}
    bad = [(k, t) for k, ts in neg.items() for t in ts if R[k].search(t)] + [(k, t) for k, ts in pos.items() for t in ts if not R[k].search(t)]
    check(f"의도 규칙 v1.2 — 거짓 걸림 {sum(len(x) for x in neg.values())}개 안 걸림 · 맞는 말 {sum(len(x) for x in pos.values())}개 걸림" + (f" ✗ {bad}" if bad else ""), not bad)
    check("설정 — 검색어·할당량", len(cfg["search"]["WORDS"]) >= 5 and cfg["comments"]["BUDGET"] > 0)
    now = parse_iso("2026-11-28T12:00:00Z")
    c2 = {"search": {"DAYS": 3, "MAX_DAYS": 14, "OVERLAP_HOURS": 6, "CHUNK_DAYS": 3}}
    st0 = {"words": {"A": "2026-11-27T12:00:00Z", "B": "2026-11-01T00:00:00Z"}, "seen": {}}
    W = windows(c2, st0, ["A", "B", "C"], now)
    check("기간 — 지난 실행 − 겹침 6시간 = 30시간 · 조각 1", iso(W["A"]["start"]) == "2026-11-27T06:00:00Z" and len(W["A"]["parts"]) == 1)
    check("기간 — 처음 = 3일 · 조각 1", iso(W["C"]["start"]) == "2026-11-25T12:00:00Z" and len(W["C"]["parts"]) == 1)
    check("기간 — 14일 넘으면 14일까지 · 건너뜀 기록 · 3일 조각 5개 (오래된 쪽부터)",
          iso(W["B"]["start"]) == "2026-11-14T12:00:00Z" and W["B"]["skipped"] and len(W["B"]["parts"]) == 5 and W["B"]["parts"][0][0] < W["B"]["parts"][-1][0]
          and W["B"]["parts"][-1][1] == now)

    class FakeApi:
        units = 0

        def get(self, ep, **kw):
            self.units += 1
            return {"items": [{"id": "c1", "snippet": {"totalReplyCount": 0, "topLevelComment": {"snippet": {"publishedAt": "2026-11-27T10:00:00Z", "likeCount": 3, "textDisplay": "옛 댓글"}}}},
                              {"id": "c2", "snippet": {"totalReplyCount": 0, "topLevelComment": {"snippet": {"publishedAt": "2026-11-28T10:00:00Z", "likeCount": 1, "textDisplay": "새 댓글 지금 사도 될까"}}}}]}
    vv = [{"id": "v1", "short": False, "comments": 2}, {"id": "v2", "short": False, "comments": 2}]
    fet = {}
    out = fetch_comments(FakeApi(), vv, 10, 999, True, {"v1": "2026-11-28T00:00:00Z"}, fet)
    check("댓글 — 앞서 본 영상은 그 뒤 댓글만 · 처음 보는 영상은 전부 · 받은 시각 기록",
          [c["text"] for c in out["v1"]] == ["새 댓글 지금 사도 될까"] and len(out["v2"]) == 2 and set(fet) == {"v1", "v2"})
    import tempfile as _tf
    with _tf.TemporaryDirectory() as td:
        global ROOT
        r0, ROOT = ROOT, Path(td)
        try:
            s = load_state("x")
            s["seen"] = {"old": "2020-01-01T00:00:00Z", "new": iso(dt.datetime.now(UTC))}
            s["words"] = {"A": "2026-11-28T00:00:00Z"}
            save_state("x", s)
            s2 = load_state("x")
            check("기록 — 저장·읽기 · 한 달 지난 영상 잊음", s2["words"] == {"A": "2026-11-28T00:00:00Z"} and set(s2["seen"]) == {"new"})
            dd = Path(td) / "x/result/next_topic/daily"
            n0 = dt.datetime.now(UTC)
            pv = [{"id": "a", "published": iso(n0 - dt.timedelta(days=1))[:16], "vph": 10}, {"id": "b", "published": iso(n0 - dt.timedelta(days=1))[:16], "vph": 99},
                  {"id": "c", "published": iso(n0 - dt.timedelta(days=5))[:16], "vph": 500}, {"id": "d", "published": iso(n0)[:16], "vph": 50}]
            with gzip.open(dd / "p.json.gz", "wt", encoding="utf-8") as fh:
                json.dump({"videos": pv}, fh)
            st1 = {"last_file": "p.json.gz", "seen": {"a": "x", "b": "x", "c": "x"}}
            rv = revisit_ids("x", {"comments": {"REVISIT_DAYS": 3, "REVISIT_TOP": 5}}, st1, n0, {"a"})
            check("다시 보기 — 댓글 받은 영상만 · 3일 안 · 이번 검색에 든 것 뺌 · 시간당 조회수 순", rv == ["b"])
        finally:
            ROOT = r0

    class FakeApiQuota:                                        # v1.0.1 — 세 번째 부름에서 할당량 끝
        units = 0

        def get(self, ep, **kw):
            self.units += 1
            if self.units >= 3:
                raise SystemExit("[API] 할당량 끝 (시험)")
            return {"items": [{"id": f"c{self.units}", "snippet": {"totalReplyCount": 0, "topLevelComment": {"snippet": {
                "publishedAt": "2026-11-28T00:00:00Z", "likeCount": 1, "textDisplay": "바닥인가요?"}}}}]}
    vv = [{"id": "v1", "short": False, "comments": 5}, {"id": "v2", "short": False, "comments": 5}]
    got = fetch_comments(FakeApiQuota(), vv, 120, 9999, True, {}, {})
    check("할당량이 도중에 끝나도 받은 댓글 남김 (v1.0.1)", list(got) == ["v1"] and len(got["v1"]) == 2)
    print("selftest:", "OK" if ok else "FAIL")
    return 0 if ok else 1


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="날마다 주식 시청자 관심 → 주제 후보 재료")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    ap.add_argument("folder", nargs="?", default="stock")
    ap.add_argument("cmd", nargs="?", default="run", choices=["run", "plan", "recount", "selftest"])
    ap.add_argument("stamp", nargs="?", default="", help="recount — daily/ 의 <날짜>[_시각] (예 2026-11-28)")
    ap.add_argument("--budget", type=int, default=0, help="할당량 한도 (0 = 설정 BUDGET)")
    ap.add_argument("--words", type=int, default=99, help="검색어 몇 개까지")
    ap.add_argument("--top", type=int, default=0, help="댓글 받을 영상 수 (0 = 설정 TOP_VIDEOS)")
    a = ap.parse_args(argv)
    logging.basicConfig(level=getattr(logging, a.log_level), format="%(message)s", stream=sys.stdout)
    if a.folder == "selftest" or a.cmd == "selftest":
        return selftest()
    cfg = load_cfg(a.folder)
    if a.cmd == "recount":
        return recount(a.folder, a.stamp)
    if a.cmd == "plan":
        return plan(a.folder, a.words, a.top or int(cfg["comments"]["TOP_VIDEOS"]))
    return run(a.folder, a.budget or int(cfg["comments"]["BUDGET"]), a.words, a.top or int(cfg["comments"]["TOP_VIDEOS"]))


if __name__ == "__main__":
    raise SystemExit(main())
