#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-11-28 — 최초. 날마다(미국 장 마감 뒤) 주식 시청자 공통 관심 → 주제 후보 재료 — 사용자 지시 2026-11-28
#          "1은 그냥 댓글보면 알 수 있지 않나? 내가 댓글 본것만 봐도 soxl 등 주식 매수 타이밍 예측하는게 많던데 왜 이걸 파악 못해 … 3은 서두를 필요없이
#          최대한 많은 정보를 가지고 정확하게 판단하는게 먼저야 4는 근데 모두야 … 공통점을 찾으면 돼 … 6은 미장 끝나고 업데이트되면 해".
#
# CHANGELOG
#   v1.0 2026-11-28  run · selftest. ① 시장 숫자(tools/market_data.py) + 최근 5거래일 사건 ② 최근 DAYS 일 새 영상 검색(검색어 WORDS) → 영상 정보 →
#                    주식 관련·한국어만 ③ 조회수 ÷ 올린 지 시간 큰 순 TOP_VIDEOS 편 댓글(최근 순·공감 순 한 쪽씩 — 작성자 이름·채널 ID 없음)
#                    ④ 의도(무엇을 하려는지·알고 싶은지) 몫 — 이번 · 전체 성공 사례 댓글과 비교 ⑤ 갈래마다 공감 큰 원문 + Claude 가 읽을 표본.
#                    결과 = <주제>/result/next_topic/daily/<날짜>.md · <날짜>.json.gz · latest.md. 할당량 BUDGET 넘으면 거기서 멈추고 받은 것만.
#
# 쓰는 법
#   python3 tools/daily_topic.py stock run [--budget 2500] [--words 12] [--top 120]
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

VERSION = "v1.0"
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


# ─────────────────────────────── ① 시장
def market_events(folder: str, n: int = 5) -> dict:
    """최근 n 거래일 표 + 사건 (반도체 ±5% · 나스닥 ±3% · 코스피 ±3% · SOXL ±15%) + 고점 대비·20일 저점 대비."""
    M = md.load(folder)
    spx = M.get("^GSPC") or {}
    days = sorted(spx)[-n:]
    rows, events = [], []
    for d in days:
        r = {"date": d}
        for sym in ("^GSPC", "^IXIC", "^SOX", "^VIX", "SOXL", "NVDA"):
            x = (M.get(sym) or {}).get(d)
            r[sym] = x
        rows.append(r)
        sox, ndq, soxl = ((M.get("^SOX") or {}).get(d) or {}).get("chg"), ((M.get("^IXIC") or {}).get(d) or {}).get("chg"), ((M.get("SOXL") or {}).get(d) or {}).get("chg")
        if sox is not None and abs(sox) >= 5 or ndq is not None and abs(ndq) >= 3 or soxl is not None and abs(soxl) >= 15:
            events.append(f"{d} 미국: 반도체 {sox:+.1f}% · 나스닥 {ndq:+.1f}% · SOXL {soxl:+.1f}%")
    ks = M.get("^KS11") or {}
    for d in sorted(ks)[-n:]:
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
    return {"rows": rows, "events": events, "state": state}


# ─────────────────────────────── ② 새 영상
def fresh_videos(folder: str, cfg: dict, api, words: list[str], budget: int) -> list[dict]:
    S = cfg.get("search") or {}
    days, mx = int(S.get("DAYS", 3)), int(S.get("MAX_RESULTS", 50))
    after = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=days)).strftime("%Y-%m-%dT%H:%M:%SZ")
    _, exclude, _, _, rel = orr.load_keywords(folder, 0)
    ids, src = [], {}
    for w in words:
        if api.units + 100 > budget:
            log("SEARCH", logging.WARNING, note="할당량 한도 — 남은 검색어 건너뜀", word=w, units=api.units, budget=budget)
            break
        j = api.get("search", part="snippet", q=w, type="video", publishedAfter=after, order="viewCount", maxResults=mx,
                    regionCode="KR", relevanceLanguage="ko")
        got = [it["id"]["videoId"] for it in j.get("items", []) if it.get("id", {}).get("videoId")]
        for i in got:
            src.setdefault(i, []).append(w)
            if i not in ids:
                ids.append(i)
        log("SEARCH", word=w, results=len(got), new_total=len(ids), units=api.units)
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
    log("VIDEOS", searched=len(ids), kept=len(vids), shorts=sum(1 for v in vids if v["short"]), rule="한국어 · 라이브 아님 · 주식 관련어 · 제외 낱말 없음", units=api.units)
    return sorted(vids, key=lambda v: -v["vph"])


# ─────────────────────────────── ③ 댓글
def fetch_comments(api, vids: list[dict], top: int, budget: int, shorts: bool) -> dict:
    out = {}
    pick = [v for v in vids if shorts or not v["short"]][:top]
    for v in pick:
        if v["comments"] == 0:
            continue
        if api.units + 2 > budget:
            log("COMMENTS", logging.WARNING, note="할당량 한도 — 남은 영상 건너뜀", done=len(out), units=api.units)
            break
        got = {}
        for order in ("time", "relevance"):
            j = api.get("commentThreads", part="snippet", videoId=v["id"], order=order, maxResults=100, textFormat="plainText")
            if j.get("_error"):
                break
            for it in j.get("items", []):
                s = it["snippet"]["topLevelComment"]["snippet"]
                got[it["id"]] = {"t": s["publishedAt"][:16], "like": int(s.get("likeCount", 0) or 0), "reply": int(it["snippet"].get("totalReplyCount", 0) or 0),
                                 "text": re.sub(r"\s+", " ", s.get("textDisplay", ""))[:400]}     # 작성자 이름·채널 ID 는 넣지 않음 (CLAUDE.md)
        out[v["id"]] = list(got.values())
    log("COMMENTS", videos=len(out), comments=sum(len(x) for x in out.values()), units=api.units)
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
def write(folder: str, cfg: dict, mk: dict, vids: list[dict], cms: dict, units: int, t0: float) -> Path:
    today = dt.datetime.now(KST).date().isoformat()
    od = ROOT / folder / "result/next_topic/daily"
    od.mkdir(parents=True, exist_ok=True)
    intents = cfg["_intent"]
    allc = [(c, v) for v in vids for c in cms.get(v["id"], [])]
    texts = [c["text"] for c, _ in allc]
    base = baseline_texts(folder)
    now_sh, base_sh = intent_shares(texts, intents), intent_shares(base, intents)
    L = []
    A = L.append
    A(f"# 오늘의 주식 시청자 관심 — {today} (미국 장 마감 뒤)\n")
    A(f"VERSION: `tools/daily_topic.py {VERSION}` 가 만듦 · 판단(주제 후보)은 Claude 가 아래 표본 원문을 읽고 `stock/result/next_topic/next_topic.md` A절에 (`stock/guides/daily_topic.md`).")
    A("※ 연구·교육용 — 투자 조언이 아님. 의도 몫은 낱말 세기(한 댓글이 여러 갈래에 들 수 있음).\n")
    A("## 1. 시장 — 최근 5거래일 (미국 · 종가 하루 변화)\n")
    A("| 날짜 | S&P500 | 나스닥 | 반도체 | VIX | SOXL | 엔비디아 |")
    A("|---|---|---|---|---|---|---|")
    for r in mk["rows"]:
        f = lambda s: "–" if not r.get(s) else (f"{r[s]['close']:.1f}" if s == "^VIX" else f"{r[s]['chg']:+.1f}%" if r[s]["chg"] is not None else "–")
        A(f"| {r['date']} | {f('^GSPC')} | {f('^IXIC')} | {f('^SOX')} | {f('^VIX')} | {f('SOXL')} | {f('NVDA')} |")
    A("\n- 사건(반도체 ±5% · 나스닥 ±3% · SOXL ±15% · 코스피 ±3%): " + (" · ".join(mk["events"]) or "없음"))
    A("- 지금: " + " · ".join(f"{s['name']} {s['chg']:+.1f}% (1년 고점 대비 {s['from_high']:.0f}% · 20일 저점 대비 {s['from_low20']:+.0f}%)" for s in mk["state"].values() if s.get("chg") is not None) + "\n")
    A(f"## 2. 최근 {(cfg.get('search') or {}).get('DAYS', 3)}일 새 영상 — 조회수 ÷ 올린 지 시간 큰 순\n")
    A(f"검색어 {len(set(w for v in vids for w in v['words']))}개로 찾은 한국어 주식 영상 {len(vids)}편 (쇼츠 {sum(1 for v in vids if v['short'])}) · 댓글 받은 {len(cms)}편 · 할당량 {units}단위.\n")
    A("| # | 올린 때(UTC) | 제목 | 채널 | 조회수 | 시간당 | 길이 | 댓글 |")
    A("|---|---|---|---|---|---|---|---|")
    for i, v in enumerate(vids[:30], 1):
        A(f"| {i} | {v['published'][5:]} | [{v['title'][:55].replace('|', '｜')}](https://www.youtube.com/watch?v={v['id']}) | {v['channel'][:12].replace('|', '｜')} | {v['views']:,} | {v['vph']:,.0f} | {'쇼츠' if v['short'] else str(round(v['sec'] / 60)) + '분'} | {v['comments']:,} |")
    A("")
    A(f"## 3. 시청자가 무엇을 하려는지·알고 싶은지 (댓글 {len(texts):,}개 · 비교 = 승인 자료(분석 사례) 댓글 전부 {len(base):,}개 · 전체 기간)\n")
    A("| 의도 | 오늘 | 분석 사례 댓글(전체 기간) | 배수 |")
    A("|---|---|---|---|")
    rows = [("**매수 타이밍·바닥·하락·가격 예측 (넷 중 하나라도)**", now_sh["_timing_any"], base_sh["_timing_any"])] + [(k, now_sh[k], base_sh[k]) for k, _ in intents]
    for k, a, b in rows:
        A(f"| {k} | {a['pct']}% ({a['n']:,}) | {b['pct']}% | {('%.1f배' % (a['pct'] / b['pct'])) if a['pct'] and b['pct'] else '–'} |")
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
    p = od / f"{today}.md"
    p.write_text("\n".join(L) + "\n", "utf-8")
    (od / "latest.md").write_text("\n".join(L) + "\n", "utf-8")
    with gzip.open(od / f"{today}.json.gz", "wt", encoding="utf-8") as f:
        json.dump({"date": today, "tool": f"daily_topic.py {VERSION}", "market": mk, "videos": vids, "comments": cms,
                   "intent_today": now_sh, "intent_base": base_sh}, f, ensure_ascii=False)
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
    log("CONFIG", folder=folder, words=len((cfg.get("search") or {}).get("WORDS") or []), budget=budget, top=top, intents=len(cfg["_intent"]))
    if md.fetch(folder, "1y") != 0:
        log("MARKET", logging.WARNING, note="시장 숫자 받기 실패 — 지난 숫자로 계속", next="네트워크 허용 목록 query1.finance.yahoo.com 확인")
    mk = market_events(folder)
    log("MARKET", events=len(mk["events"]), last=mk["rows"][-1]["date"] if mk["rows"] else "-")
    import next_topic as nt
    api = nt.Api()
    words = list((cfg.get("search") or {}).get("WORDS") or [])[:nwords]
    try:
        vids = fresh_videos(folder, cfg, api, words, budget)
        cms = fetch_comments(api, vids, top, budget, bool((cfg.get("comments") or {}).get("SHORTS", True)))
    except SystemExit as e:                                    # 할당량 끝 — 받은 것까지만 쓰고 알림
        log("API", logging.WARNING, error=str(e)[:160], next="한국 17시 할당량 초기화 뒤 다시")
        vids, cms = locals().get("vids", []), locals().get("cms", {})
    write(folder, cfg, mk, vids, cms, api.units, t0)
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
    check("설정 — 검색어·할당량", len(cfg["search"]["WORDS"]) >= 5 and cfg["comments"]["BUDGET"] > 0)
    print("selftest:", "OK" if ok else "FAIL")
    return 0 if ok else 1


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="날마다 주식 시청자 관심 → 주제 후보 재료")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    ap.add_argument("folder", nargs="?", default="stock")
    ap.add_argument("cmd", nargs="?", default="run", choices=["run", "selftest"])
    ap.add_argument("--budget", type=int, default=0, help="할당량 한도 (0 = 설정 BUDGET)")
    ap.add_argument("--words", type=int, default=99, help="검색어 몇 개까지")
    ap.add_argument("--top", type=int, default=0, help="댓글 받을 영상 수 (0 = 설정 TOP_VIDEOS)")
    a = ap.parse_args(argv)
    logging.basicConfig(level=getattr(logging, a.log_level), format="%(message)s", stream=sys.stdout)
    if a.folder == "selftest" or a.cmd == "selftest":
        return selftest()
    cfg = load_cfg(a.folder)
    return run(a.folder, a.budget or int(cfg["comments"]["BUDGET"]), a.words, a.top or int(cfg["comments"]["TOP_VIDEOS"]))


if __name__ == "__main__":
    raise SystemExit(main())
