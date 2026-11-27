#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0.0 — 2026-11-27 — 새로 (사용자 지시 2026-11-27 "그냥 겨울철 꿀팁들 조사해서 주제 정하자 탐색해서 주제 여러개 알려줘봐" · 같은 날 "이 채널은 쇼츠만 운영할거야").
#   겨울 꿀팁 갈래(SUBTOPICS)마다 **쇼츠** 시장을 잰다 — 이 채널이 쇼츠만 하므로 롱폼 탐색(explore)과 따로.
#   갈래마다 유튜브 검색 1번(videoDuration=short · 최근 365일 · 조회수 순 · 한국 · 한국어 = 100단위, 캐시는 outlier_research 와 같은 곳·같은 규칙)
#   → 영상 정보·채널 구독자 → 3분 이하 · 라이브 아님 · 제목에 갈래 핵심 낱말이 든 쇼츠만 →
#     영상 수 · 조회수 가운데값·상위 25% · 100만+ 개수(⚠ 이미 많이 본 내용) · 작은 채널 성공(analysis_rules.toml [shorts] 기준 그대로:
#     3~180일 · 구독자 5만 이하 · 조회수 5만 이상 · 구독자당 하루 조회수 ≥ 0.1) · 최근 30일 공급 · 자동완성(할당량 0).
#   숫자만 낸다 — 판단(추천 순서)은 Claude 가 shopping/result/next_topic/winter_topics.md 에.
#   한계: 검색은 조회수 순 상위 50개라 잘된 쪽으로 치우침 (갈래끼리 견주는 데만) · 핵심 낱말은 제목 규칙이라 거침.
# ※ 연구·교육용 — 구매 권유가 아니다.
"""겨울 꿀팁 쇼츠 시장 — python3 shopping/source/winter_tips.py [--quota 2200] [--refresh] | --selftest"""
import argparse
import json
import logging
import re
import statistics
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import outlier_research as orr  # noqa: E402

VERSION = "v1.0.0"
TOPIC = "shopping"
LOG = logging.getLogger("winter_tips")

# 갈래 = (이름, 검색어, 제목 핵심 낱말 정규식, 자동완성 낱말, 이어지는 물건(쿠팡 후보 — Claude 판단 칸의 재료))
SUBTOPICS = [
    ("난방비 절약", "난방비 절약 꿀팁", "난방비|난방|보일러", "난방비 절약", "문풍지·뽁뽁이·방한커튼·탄소매트"),
    ("외풍 차단", "외풍 차단 꿀팁", "외풍|웃풍|뽁뽁이|문풍지|단열|틈새", "외풍 차단", "문풍지·뽁뽁이·방한커튼·틈막이"),
    ("결로·곰팡이", "결로 곰팡이 방지", "결로|곰팡이|물방울", "결로 방지", "결로방지 시트·제습제·창문 물기 제거기"),
    ("수도 동파", "수도 동파 방지", "동파|얼었|얼어|보온재", "수도 동파 방지", "수도 보온재·동파 방지 열선"),
    ("정전기", "정전기 없애는 법", "정전기", "정전기 방지", "정전기 방지 스프레이·섬유유연제·가습기"),
    ("실내 건조·습도", "겨울 실내 건조 습도", "건조|습도|가습", "실내 습도", "가습기·습도계·젖은 수건 걸이"),
    ("가습기 청소", "가습기 청소 꿀팁", "가습기", "가습기 청소", "가습기 세척 솔·구연산"),
    ("겨울 빨래 건조", "겨울 빨래 건조 꿀팁", "빨래|건조대|건조기", "겨울 빨래", "빨래 건조대·제습기·건조기 시트"),
    ("패딩 세탁", "패딩 세탁 꿀팁", "패딩|다운", "패딩 세탁", "패딩 전용 세제·세탁망·테니스공"),
    ("니트 보풀", "니트 보풀 제거", "보풀|니트", "보풀 제거", "보풀 제거기·니트 세탁망"),
    ("전기장판·매트", "전기장판 전기세", "전기장판|전기요|온수매트|탄소매트|카본매트|매트", "전기장판", "탄소매트·전기요·온수매트"),
    ("손발 보온", "겨울 보온 꿀팁", "보온|핫팩|손난로|수면양말|발이 시|손이 시", "핫팩", "핫팩·손난로·수면양말·발열 내의"),
    ("귤·과일 보관", "귤 보관법", "귤|보관", "귤 보관", "과일 보관 용기·신문지(무료)"),
    ("김장", "김장 꿀팁", "김장|절임|배추", "김장 꿀팁", "김장 매트·김장 봉투·고무장갑"),
    ("겨울 환기", "겨울 환기 방법", "환기", "겨울 환기", "창문 환기 팬(조심 — 효과 말)"),
    ("보일러 사용법", "보일러 외출 모드", "보일러|외출", "보일러 외출", "보일러 온도 조절기(스마트)"),
    ("빙판길·미끄럼", "빙판길 미끄럼 방지", "빙판|미끄|아이젠", "빙판길", "신발 아이젠·미끄럼 방지 패드"),
    ("겨울 이불", "겨울 이불 세탁", "이불|극세사|차렵", "겨울 이불", "극세사 이불·이불 압축팩"),
    ("겨울 피부 건조", "겨울 피부 건조 꿀팁", "피부|보습|건조", "겨울 피부", "보습 크림(⚠ 효능 말 ✗)"),
    ("겨울철 꿀팁 전반", "겨울철 꿀팁", "겨울", "겨울철 꿀팁", "갈래마다 다름"),
]
SHORTS = {"MAX_SECONDS": 180, "MIN_AGE_DAYS": 3, "MAX_AGE_DAYS": 180, "MAX_SUBS": 50000, "MIN_VIEWS": 50000, "MIN_VPD_SUBS": 0.1}
WINDOW_DAYS = 365
RECENT_DAYS = 30


def log(stage, level=logging.INFO, **kv):
    LOG.log(level, "[%s] [%s] %s", stage, datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S"),
            " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) and ' ' in v else v}" for k, v in kv.items()))


def age_days(published, now):
    try:
        return (now - datetime.fromisoformat(str(published).replace("Z", "+00:00"))).total_seconds() / 86400
    except (TypeError, ValueError):
        return None


def measure(infos, subs, core_rx, now, rules=SHORTS):
    """한 갈래의 숫자 (할당량 0 — 받아 둔 영상 정보만)."""
    rx = re.compile(core_rx, re.I)
    rows = []
    for i in infos:
        if i.get("live") or i.get("was_live"):
            continue
        if not i.get("duration") or i["duration"] > rules["MAX_SECONDS"]:
            continue
        if not rx.search(i.get("title") or ""):
            continue
        ad = age_days(i.get("published"), now)
        if ad is None or ad > WINDOW_DAYS:
            continue
        s = (subs.get(i.get("channel_id")) or {}).get("subs")
        v = int(i.get("view_count") or 0)
        vpd = v / max(ad, 1)
        ok = (rules["MIN_AGE_DAYS"] <= ad <= rules["MAX_AGE_DAYS"] and s is not None and s <= rules["MAX_SUBS"]
              and v >= rules["MIN_VIEWS"] and vpd / max(s, 100) >= rules["MIN_VPD_SUBS"])
        rows.append({"id": i["id"], "title": i.get("title"), "channel": i.get("channel"), "subs": s, "views": v, "age": round(ad, 1),
                     "vpd": round(vpd), "small_win": ok, "recent": ad <= RECENT_DAYS,
                     "winter": datetime.fromisoformat(str(i["published"]).replace("Z", "+00:00")).month in (11, 12, 1, 2)})
    views = sorted(r["views"] for r in rows)
    out = {"n": len(rows), "median": int(statistics.median(views)) if views else 0,
           "p75": views[int(len(views) * 0.75)] if views else 0, "max": views[-1] if views else 0,
           "over_1m": sum(1 for v in views if v >= 1_000_000), "over_100k": sum(1 for v in views if v >= 100_000),
           "small_wins": sum(1 for r in rows if r["small_win"]), "recent_n": sum(1 for r in rows if r["recent"]),
           "recent_median": int(statistics.median([r["views"] for r in rows if r["recent"]])) if any(r["recent"] for r in rows) else 0,
           "winter_share": round(sum(r["views"] for r in rows if r["winter"]) / max(sum(views), 1), 2)}
    out["examples"] = sorted([r for r in rows if r["small_win"]], key=lambda r: -r["views"])[:3] or sorted(rows, key=lambda r: -r["views"])[:2]
    return out


def selftest():
    now = datetime(2026, 11, 27, tzinfo=timezone.utc)
    infos = [
        {"id": "a", "title": "난방비 절약 꿀팁", "channel_id": "c1", "duration": 40, "published": "2026-11-20T00:00:00Z", "view_count": 200000},
        {"id": "b", "title": "난방비 아끼는 법", "channel_id": "c2", "duration": 50, "published": "2026-01-10T00:00:00Z", "view_count": 2_000_000},
        {"id": "c", "title": "난방 롱폼", "channel_id": "c1", "duration": 600, "published": "2026-11-20T00:00:00Z", "view_count": 9},
        {"id": "d", "title": "귤 보관", "channel_id": "c1", "duration": 30, "published": "2026-11-20T00:00:00Z", "view_count": 9},
        {"id": "e", "title": "보일러 라이브", "channel_id": "c1", "duration": 30, "published": "2026-11-20T00:00:00Z", "view_count": 9, "live": True},
    ]
    subs = {"c1": {"subs": 1000}, "c2": {"subs": 900000}}
    m = measure(infos, subs, "난방비|난방|보일러", now)
    assert m["n"] == 2 and m["small_wins"] == 1 and m["over_1m"] == 1 and m["recent_n"] == 1, m
    assert m["winter_share"] == 1.0, "11월·1월 영상"
    print("[SELFTEST] ok — n", m["n"], "작은 채널 성공", m["small_wins"], "100만+", m["over_1m"])


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quota", type=int, default=2200)
    ap.add_argument("--refresh", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args(argv)
    logging.basicConfig(level=a.log_level, format="%(message)s", stream=sys.stdout)
    if a.selftest:
        selftest()
        return 0
    t0 = datetime.now(timezone.utc)
    key, src = orr.load_api_key(TOPIC)
    if not key:
        log("START", logging.ERROR, error="YOUTUBE_API_KEY 없음", next="환경 변수 YOUTUBE_API_KEY 를 넣고 다시")
        return 1
    cache = ROOT / TOPIC / "result" / "outliers" / ".cache"
    cache.mkdir(parents=True, exist_ok=True)
    api, state = orr.Api(key, a.quota), orr.new_state()
    since = (t0 - timedelta(days=WINDOW_DAYS)).strftime("%Y-%m-%dT%H:%M:%SZ")
    log("START", tool=f"winter_tips.py {VERSION}", subtopics=len(SUBTOPICS), window_days=WINDOW_DAYS, dur="short", quota=a.quota, key_source=src,
        rule="쇼츠 성공 = 3~180일·구독자≤5만·조회수≥5만·구독자당 하루 조회수≥0.1 (analysis_rules [shorts])")
    results = []
    for name, q, core, ac_word, items in SUBTOPICS:
        try:
            ids, cached = orr.cached_search(api, cache, q, since, "short", WINDOW_DAYS, orr.SEARCH_TTL_HOURS, a.refresh)
        except orr.QuotaStop as e:
            log("SEARCH", logging.WARNING, subtopic=name, stop=str(e), next="할당량 초기화(한국 17:00) 뒤 다시 — 받은 갈래는 캐시로 0단위")
            break
        infos = orr.fetch_video_infos(api, cache, ids, state)
        subs = orr.fetch_channel_subs(api, cache, list({i.get("channel_id") for i in infos if i.get("channel_id")}), state)
        try:
            ac, _ = orr.fetch_autocomplete(ac_word, cache)
        except Exception as e:  # noqa: BLE001 — 자동완성은 보조 (실패해도 갈래 숫자는 냄)
            log("AUTOCOMPLETE", logging.WARNING, word=ac_word, error=repr(e)[:120])
            ac = []
        m = measure(infos, subs, core, t0)
        m.update(name=name, q=q, items=items, autocomplete=ac[:8], cached=cached)
        results.append(m)
        log("SUBTOPIC", name=name, n=m["n"], median=m["median"], small_wins=m["small_wins"], over_1m=m["over_1m"], recent_n=m["recent_n"],
            winter_share=m["winter_share"], cached=cached, quota_used=api.used)
    out_dir = ROOT / TOPIC / "result" / "next_topic"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "winter_tips.json").write_text(json.dumps({"version": VERSION, "asof": t0.isoformat(timespec="seconds"), "rules": SHORTS,
                                                           "window_days": WINDOW_DAYS, "results": results}, ensure_ascii=False, indent=1), "utf-8")
    L = [f"# 겨울 꿀팁 쇼츠 시장 — 갈래별 숫자 (`shopping/source/winter_tips.py` {VERSION})", "",
         f"만든 때 {t0.strftime('%Y-%m-%d %H:%M')}Z · 갈래 {len(results)}개 × 쇼츠 검색 1번(최근 {WINDOW_DAYS}일·조회수 순 50개) · 할당량 {api.used}단위 · "
         "제목에 갈래 핵심 낱말이 든 3분 이하 쇼츠만 · **숫자만 — 판단은 `winter_topics.md`**", "",
         "> 작은 채널 성공 = `analysis_rules.toml` [shorts] 기준 그대로 (3~180일 · 구독자 5만 이하 · 조회수 5만 이상 · 구독자당 하루 조회수 0.1 이상). "
         "100만+ = 시청자가 이미 많이 본 내용(⚠ 겹침). 최근 30일 = 지금 올라오는 양(공급). 겨울 몫 = 11~2월에 올린 쇼츠가 가진 조회수 몫. "
         "검색 순위 상위 50개라 잘된 쪽으로 치우침 — 갈래끼리 견주는 데만.", "",
         "| 갈래 | 쇼츠 수 | 조회수 가운데값 | 상위 25% | 100만+ | 작은 채널 성공 | 최근 30일 (가운데값) | 겨울 몫 | 자동완성 |",
         "|---|---|---|---|---|---|---|---|---|"]
    for m in sorted(results, key=lambda m: (-m["small_wins"], -m["median"])):
        L.append(f"| **{m['name']}** | {m['n']} | {m['median']:,} | {m['p75']:,} | {m['over_1m']} | {m['small_wins']} | {m['recent_n']} ({m['recent_median']:,}) | "
                 f"{m['winter_share']:.0%} | {' · '.join(m['autocomplete'][:4]) or '—'} |")
    L += ["", "## 갈래마다 — 작은 채널 성공 쇼츠 (없으면 가장 많이 본 쇼츠)", ""]
    for m in sorted(results, key=lambda m: (-m["small_wins"], -m["median"])):
        ex = " / ".join(f"[{(r['title'] or '')[:40]}](https://youtube.com/shorts/{r['id']}) {r['views']:,}회·구독자 {r['subs'] if r['subs'] is not None else '?':,}" if isinstance(r['subs'], int)
                        else f"[{(r['title'] or '')[:40]}](https://youtube.com/shorts/{r['id']}) {r['views']:,}회" for r in m["examples"])
        L.append(f"- **{m['name']}** (검색어 '{m['q']}' · 이어지는 물건: {m['items']}) — {ex or '근거 없음'}")
    (out_dir / "winter_tips.md").write_text("\n".join(L) + "\n", "utf-8")
    log("DONE", out="shopping/result/next_topic/winter_tips.md", subtopics=len(results), quota_used=api.used,
        seconds=round((datetime.now(timezone.utc) - t0).total_seconds(), 1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
