#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-11-12 — 새로: 제목 후보가 유튜브에 이미 있는 영상과 같거나 비슷한지, 같은 내용이 너무 흔한지 검사
#   사용자 지시 2026-11-12 "유튜브 이미 올라와 있거나 중복되거나 비슷한 내용이 많으면 안됨".
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.0 | 2026-11-12 | 최초 | corpus·live_titles·score·judge·render·selftest |
#
# 견주는 제목 (할당량 0 — 저장소에 있는 것):
#   ① <주제>/result/web/explore.json·shorts_explore.json (탐색 목록 — 검색으로 찾은 영상 전부) ② <주제>/result/outliers/*/metadata.json (받은 사례)
#   ③ <주제>/result/trend/videos_<날짜>.json (최근 훑기) ④ 우리 영상 <주제>/source/*/youtube.json (같은 채널 안 중복)
#   --live 면 ⑤ 유튜브 검색 1번(100단위 — 후보 낱말로, 기간 없이 관련도 순 50개) + 영상 정보 1단위. 키 = 환경 변수 YOUTUBE_API_KEY (값은 출력하지 않음).
# 셈 (글자 바탕 — 뜻이 같아도 말이 다르면 못 잡음: 남는 판단은 Claude 가 표의 비슷한 제목을 읽고):
#   · 글자 두 개씩(띄어쓰기·부호·따옴표 뺌) 겹침 — jac = 자카드, cont = 짧은 쪽 기준 포함률
#   · 핵심 낱말(2자 이상, 흔한 말 뺌)·숫자 겹침 — 같은 내용 = 후보 핵심 낱말의 KEY_SHARE 이상 + 2개 이상이 같은 제목
#   판정: ❌ 같은 제목(jac ≥ SAME_JAC 또는 cont ≥ SAME_CONT) · ❌ 우리 채널 영상과 비슷(jac ≥ OWN_JAC) · ❌ 같은 내용 CROWD_MAX 개 이상(최근 CROWD_DAYS 일)
#         ⚠ 비슷한 제목(jac ≥ NEAR_JAC) · ⚠ 같은 내용 CROWD_WARN 개 이상 · ✅ 그 밖.  (값은 아래 상수 — 처음 값, 쓰면서 맞춤)
# 쓰기:
#   python3 tools/title_dupe.py <주제> --title "후보 1" --title "후보 2" [--shorts] [--live] [--out <md>]
#   python3 tools/title_dupe.py --selftest
# ※ 연구·교육용 — 투자 권유 아님.
from __future__ import annotations

import argparse
import glob
import json
import logging
import os
import re
import sys
import tempfile
import time
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = "v1.0"
LOG = logging.getLogger("title_dupe")
SAME_JAC, SAME_CONT, NEAR_JAC, OWN_JAC = 0.55, 0.80, 0.33, 0.40
KEY_SHARE, CROWD_DAYS, CROWD_MAX, CROWD_WARN = 0.6, 180, 6, 3
STOP = set("영상 이유 방법 진짜 정말 지금 이제 그냥 무조건 절대 모두 가장 제일 하는 있는 없는 이것 그것 우리 여러분 사람 사람들 경우 결국 이렇게 그렇게 "
           "합니다 했다 한다 하면 해도 하고 해서 입니다 있다 없다 된다 됩니다 하세요 보세요 꼭 다시 계속 바로 오늘 내일 이번 정리 총정리 완벽 "
           "shorts 쇼츠 feat ep".split())
HANGUL_TOKEN = re.compile(r"[가-힣A-Za-z]{2,}|\d+(?:[.,]\d+)?%?")
JOSA = re.compile(r"(은|는|이|가|을|를|에|에서|의|도|로|으로|와|과|만|까지|부터|보다|처럼|이나|나|요|죠|다)$")
LOG_FMT = "%(message)s"


def log(stage: str, level: int = logging.INFO, **kv) -> None:
    ts = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    LOG.log(level, f"[{stage}] [{ts}] " + " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) else v}" for k, v in kv.items()))


def squash(t: str) -> str:
    t = re.sub(r"#\S+", " ", str(t or ""))
    return re.sub(r"[^0-9A-Za-z가-힣%]", "", t).lower()


def bigrams(t: str) -> set[str]:
    s = squash(t)
    return {s[i:i + 2] for i in range(len(s) - 1)} if len(s) > 1 else {s} if s else set()


def keys(t: str) -> set[str]:
    out = set()
    for w in HANGUL_TOKEN.findall(re.sub(r"#\S+", " ", str(t or ""))):
        w = w.lower()
        if not w[0].isdigit():
            w2 = JOSA.sub("", w) if len(w) > 2 else w
            w = w2 if len(w2) >= 2 else w
        if w not in STOP and len(w) >= 2:
            out.add(w)
    return out


def score(a: str, b: str) -> dict:
    A, B = bigrams(a), bigrams(b)
    inter = len(A & B)
    jac = inter / len(A | B) if A | B else 0.0
    cont = inter / min(len(A), len(B)) if A and B else 0.0
    ka, kb = keys(a), keys(b)
    shared = ka & kb
    return {"jac": round(jac, 3), "cont": round(cont, 3), "shared": sorted(shared), "key_share": round(len(shared) / len(ka), 2) if ka else 0.0}


# ------------------------------------------------------------------ 견줄 제목
def corpus(root: Path, topic: str, shorts: bool = False) -> list[dict]:
    seen, out = set(), []

    def add(vid, title, src, published="", views=None, channel=""):
        if not title or (vid and vid in seen):
            return
        if vid:
            seen.add(vid)
        out.append({"id": vid or "", "title": str(title), "src": src, "published": str(published or "")[:10], "views": views, "channel": channel})

    web = root / topic / "result" / "web"
    for fn in (["shorts_explore.json", "explore.json"] if shorts else ["explore.json", "shorts_explore.json"]):
        d = read_json(web / fn, {}) or {}
        for r in d.get("rows") or []:
            add(r.get("id"), r.get("title"), "탐색", r.get("published"), r.get("views"), r.get("channel", ""))
    for p in glob.glob(str(root / topic / "result" / "outliers" / "**" / "metadata.json"), recursive=True):
        m = read_json(Path(p), {}) or {}
        vid = m.get("video_id") or m.get("id") or Path(p).parent.name.split("_", 1)[-1]
        add(vid, m.get("title"), "사례", m.get("published"), m.get("views"), m.get("channel", ""))
    for p in sorted((root / topic / "result" / "trend").glob("videos_*.json"), reverse=True)[:5]:
        for r in read_json(p, []) or []:
            add(r.get("id"), r.get("title"), "최근", r.get("published"), r.get("views"), r.get("channel", ""))
    for p in glob.glob(str(root / topic / "source" / "**" / "youtube.json"), recursive=True):
        y = read_json(Path(p), {}) or {}
        add(y.get("videoId"), y.get("title"), "우리 채널", str(y.get("publishAt") or y.get("uploadedAt") or ""), None, y.get("channel", ""))
    return out


def read_json(p: Path, default=None):
    try:
        return json.loads(p.read_text("utf-8"))
    except (OSError, ValueError):
        return default


def live_titles(topic: str, title: str, quota: int = 300) -> list[dict]:
    """유튜브 검색 1번(100단위) — 후보의 핵심 낱말로, 기간 없이 관련도 순 50개 + 영상 정보 1단위."""
    sys.path.insert(0, str(ROOT / "tools"))
    import outlier_research as orr  # noqa: E402
    import pc_analysis as pc        # noqa: E402
    key = os.environ.get("YOUTUBE_API_KEY")
    if not key:
        log("LIVE", logging.ERROR, missing="YOUTUBE_API_KEY", next="키를 환경 변수에 넣거나 --live 없이 (저장소 제목만)")
        return []
    api = orr.Api(key, quota, ledger=pc.KeyLedger(key), what="title_dupe", topic=topic)
    q = " ".join(sorted(keys(title), key=len, reverse=True)[:5]) or title
    try:
        d = api.get("search", part="snippet", q=q, type="video", order="relevance", regionCode="KR", relevanceLanguage="ko", maxResults=50)
    except Exception as e:  # noqa: BLE001 (할당량·네트워크)
        log("LIVE", logging.WARNING, query=q, error=repr(e)[:140], next="할당량이면 태평양 자정 뒤 다시 — 저장소 제목만으로 판정")
        return []
    ids = [it["id"]["videoId"] for it in d.get("items", []) if it.get("id", {}).get("videoId")]
    stats = {}
    if ids:
        for it in api.videos(ids[:50]):
            stats[it["id"]] = int((it.get("statistics") or {}).get("viewCount", 0) or 0)
    out = [{"id": it["id"]["videoId"], "title": it["snippet"].get("title", ""), "src": "유튜브 검색", "published": it["snippet"].get("publishedAt", "")[:10],
            "views": stats.get(it["id"]["videoId"]), "channel": it["snippet"].get("channelTitle", "")}
           for it in d.get("items", []) if it.get("id", {}).get("videoId")]
    log("LIVE", query=q, results=len(out), units=api.used)
    return out


# ------------------------------------------------------------------ 판정
def judge(title: str, rows: list[dict], today: str | None = None) -> dict:
    today = today or date.today().isoformat()
    d0 = (date.fromisoformat(today) - timedelta(days=CROWD_DAYS)).isoformat()
    scored = []
    for r in rows:
        s = score(title, r["title"])
        if s["jac"] >= 0.12 or len(s["shared"]) >= 2:
            scored.append({**r, **s})
    scored.sort(key=lambda r: (-r["jac"], -len(r["shared"])))
    ka = keys(title)
    crowd = [r for r in scored if len(r["shared"]) >= 2 and r["key_share"] >= KEY_SHARE and (not r["published"] or r["published"] >= d0)]
    fails, warns = [], []
    same = [r for r in scored if r["jac"] >= SAME_JAC or r["cont"] >= SAME_CONT]
    own = [r for r in scored if r["src"] == "우리 채널" and r["jac"] >= OWN_JAC]
    near = [r for r in scored if NEAR_JAC <= r["jac"] < SAME_JAC and r["cont"] < SAME_CONT]
    if same:
        fails.append(f"같은 제목 {len(same)}개 — 「{same[0]['title'][:50]}」 (jac {same[0]['jac']} · cont {same[0]['cont']})")
    if own:
        fails.append(f"우리 채널 영상과 비슷 — 「{own[0]['title'][:50]}」 (jac {own[0]['jac']})")
    if len(crowd) >= CROWD_MAX:
        fails.append(f"같은 내용(핵심 낱말 {round(KEY_SHARE * 100)}% 이상 같음) 최근 {CROWD_DAYS}일 {len(crowd)}개 ≥ {CROWD_MAX}")
    elif len(crowd) >= CROWD_WARN:
        warns.append(f"같은 내용 최근 {CROWD_DAYS}일 {len(crowd)}개 (≥ {CROWD_WARN}) — 표를 읽고 우리만의 결과·물음인지 확인")
    if near:
        warns.append(f"비슷한 제목 {len(near)}개 — 가장 가까운 「{near[0]['title'][:50]}」 (jac {near[0]['jac']})")
    verdict = "❌" if fails else "⚠" if warns else "✅"
    return {"title": title, "verdict": verdict, "fails": fails, "warns": warns, "keys": sorted(ka), "crowd": len(crowd), "top": scored[:12],
            "crowd_rows": crowd[:8], "compared": len(rows)}


def render(topic: str, results: list[dict], live: bool) -> str:
    w = (L := []).append
    w(f"# 제목 중복 검사 — {topic} ({date.today()})")
    w("")
    w(f"`tools/title_dupe.py {VERSION}` · 견준 제목 {results[0]['compared'] if results else 0}개 (탐색·사례·최근 훑기·우리 채널{' + 유튜브 검색' if live else ''}) · "
      f"기준: 같은 제목 jac ≥ {SAME_JAC} 또는 cont ≥ {SAME_CONT} · 비슷 jac ≥ {NEAR_JAC} · 같은 내용 = 핵심 낱말 {round(KEY_SHARE * 100)}% 이상 같음, 최근 {CROWD_DAYS}일 {CROWD_MAX}개 이상 ❌")
    w("")
    w("※ 글자 바탕 셈 — 말만 다르고 뜻이 같은 제목은 못 잡는다. 표의 비슷한 제목을 읽고 '이미 있는 내용인가'를 한 줄로 판단해 적는다.")
    for r in results:
        w("")
        w(f"## {r['verdict']} {r['title']}")
        w(f"- 핵심 낱말: {', '.join(r['keys']) or '-'} · 같은 내용 {r['crowd']}개")
        for x in r["fails"]:
            w(f"- ❌ {x}")
        for x in r["warns"]:
            w(f"- ⚠ {x}")
        if r["top"]:
            w("")
            w("| jac | cont | 같은 낱말 | 출처 | 올린 날 | 조회수 | 제목 |")
            w("|---:|---:|---|---|---|---:|---|")
            for t in r["top"]:
                v = f"{int(float(t['views'])):,}" if t.get("views") not in (None, "") else "—"
                w(f"| {t['jac']} | {t['cont']} | {', '.join(t['shared'][:5])} | {t['src']} | {t['published'] or '—'} | {v} | {t['title'][:70].replace('|', '/')} |")
    return "\n".join(L) + "\n"


def selftest() -> int:
    ok = True

    def chk(name, cond):
        nonlocal ok
        ok &= bool(cond)
        print(("✅ " if cond else "❌ ") + name)

    today = "2026-11-12"
    rows = [{"id": "a", "title": "반등에 팔까 버틸까? 급반등 셋 중 둘은 저점을 또 깼다", "src": "탐색", "published": "2026-11-01", "views": 1, "channel": ""},
            {"id": "b", "title": "연금저축 세금 16.5% 피하는 법", "src": "탐색", "published": "2026-10-01", "views": 1, "channel": ""}]
    r = judge("반등에 팔까 버틸까? 급반등 셋 중 둘은 저점을 또 깼다", rows, today)
    chk("같은 제목 → ❌", r["verdict"] == "❌" and r["fails"])
    r = judge("조선 백성은 겨울을 어떻게 났을까", rows, today)
    chk("다른 내용 → ✅", r["verdict"] == "✅")
    crowd = [{"id": str(i), "title": f"연금저축 세금 16.5% 함정 {i}번째", "src": "탐색", "published": "2026-10-20", "views": 1, "channel": ""} for i in range(7)]
    r = judge("연금저축 세금 16.5% 아무도 안 알려준 함정", crowd, today)
    chk("같은 내용 7개 → ❌ (흔함)", r["verdict"] == "❌" and any("같은 내용" in f for f in r["fails"]))
    own = [{"id": "o", "title": "주식 투자 실패하는 사람들은 절대 통과 못하는 테스트", "src": "우리 채널", "published": "2026-11-05", "views": None, "channel": ""}]
    r = judge("주식 투자 실패하는 사람은 통과 못하는 테스트 2탄", own, today)
    chk("우리 채널과 비슷 → ❌", r["verdict"] == "❌")
    chk("낱말: 조사 뗌", "연금저축" in keys("연금저축은 왜") and "세금" in keys("세금을"))
    with tempfile.TemporaryDirectory() as d:
        R = Path(d)
        (R / "demo/result/web").mkdir(parents=True)
        (R / "demo/result/web/explore.json").write_text(json.dumps({"rows": rows}, ensure_ascii=False), "utf-8")
        chk("corpus: 탐색 목록 읽음", len(corpus(R, "demo")) == 2)
    print("[SELFTEST] " + ("✅ 모두 통과" if ok else "❌ 실패 있음"))
    return 0 if ok else 1


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="제목 후보 중복·비슷·흔한 내용 검사")
    ap.add_argument("topic", nargs="?"); ap.add_argument("--title", action="append", default=[])
    ap.add_argument("--shorts", action="store_true", help="쇼츠 탐색 목록을 먼저"); ap.add_argument("--live", action="store_true", help="유튜브 검색 1번씩 (100단위)")
    ap.add_argument("--out"); ap.add_argument("--selftest", action="store_true"); ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args(argv)
    logging.basicConfig(level=getattr(logging, a.log_level), format=LOG_FMT, stream=sys.stdout)
    if a.selftest:
        return selftest()
    if not a.topic or not (ROOT / a.topic).is_dir() or not a.title:
        ap.error("주제와 --title 을 주세요 — 예: title_dupe.py stock --title \"…\"")
    t0 = time.perf_counter()
    base = corpus(ROOT, a.topic, a.shorts)
    log("CORPUS", topic=a.topic, titles=len(base), by_src=json.dumps({s: sum(r["src"] == s for r in base) for s in ("탐색", "사례", "최근", "우리 채널")}, ensure_ascii=False))
    results = []
    for t in a.title:
        rows = base + (live_titles(a.topic, t) if a.live else [])
        r = judge(t, rows)
        results.append(r)
        log("JUDGE", title=t[:60], verdict=r["verdict"], fails=len(r["fails"]), warns=len(r["warns"]), crowd=r["crowd"],
            nearest=(r["top"][0]["title"][:40] if r["top"] else "-"), nearest_jac=(r["top"][0]["jac"] if r["top"] else 0))
    md = render(a.topic, results, a.live)
    if a.out:
        Path(a.out).write_text(md, "utf-8")
        log("DONE", file=a.out, titles=len(results), fails=sum(r["verdict"] == "❌" for r in results), seconds=round(time.perf_counter() - t0, 2))
    else:
        print(md)
    return 1 if any(r["verdict"] == "❌" for r in results) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
