#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-11-12 — 분석 결과 페르소나 파일 꼴 둘을 읽음: 표준 분석기 <주제>/result/outliers/personas.json('personas') ·
#   위기 crisis/result/personas.json('final' — crisis_lab.py, 표준 분석기 전). 사용자 지시 2026-11-12 "재테크는 하지 말고 심리, 위기 주제를 그렇게 만들어".
# (v1.0 — 2026-11-12 — 새로: '살아 있는 페르소나' — 분석 결과로 처음 만들고, 매일 최근 유튜브(영상·댓글)와 뉴스로 고친다. 고칠 때마다 근거·바뀐 것을 짧게 남김.
#   사용자 지시 2026-11-12 "페르소나는 주제와 관련된 최근 유튜브 영상과 최근 트렌드(뉴스 등 외부 정보)들을 수집해서 상황, 생각(호기심, 걱정, 불안),
#   원하는 것 등 세부 설정을 매일 업데이트 해야함 - 페르소나 업데이트 시 아티팩트에 어떤 근거로 어떻게 업데이트 했는지 짧막하게 내역 남기기")
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.1 | 2026-11-12 | crisis 꼴(final) 읽기 · 처지 줄 0% 뺌 | source_personas·who_line_crisis |
# | v1.0 | 2026-11-12 | 최초 | init·status·inputs·apply·feed·selftest |
#
# 파일 (분석기 결과 result/outliers 는 건드리지 않음 — PC 분석이 그 폴더를 덮어도 남게 result/persona/ 에):
#   <주제>/result/persona/live.json     페르소나(처지·상황·호기심·걱정·불안·원하는 것·버릇·원문 댓글) + 바뀐 내역(log)
#   <주제>/result/persona/log.md        바뀐 내역 (새것 위) — 사람이 읽는 꼴
#   <주제>/result/persona/news_<날짜>.json   Claude 가 WebSearch 로 모은 뉴스 [{title, source, date, url, note}] — 손으로 씀
#   <주제>/result/persona/inputs_<날짜>.md   그날 읽을 재료 한 장 (inputs 명령이 만듦 — Claude 는 이것만 읽고 바꿀 것을 정함)
#   <주제>/result/persona/changes_<날짜>.json Claude 가 정한 바꿀 것 (apply 가 검사한 뒤 반영)
# 근거 규칙 (apply 가 막음 — 지어낸 생각을 넣지 않게):
#   · 바꾸는 것마다 basis(근거 한 줄, 80자 안) + src 하나 이상.  src = c:<댓글 원문 12자 이상 — 그대로> · v:<영상 ID> · n:<뉴스 주소> · m:<시장 이름>
#   · 생각(호기심·걱정·불안)·원하는 것·버릇은 시청자 말(c:)이 꼭 하나 — 뉴스·시장(n:·m:)만으로는 '상황'만 바꿈.
#   · c: 는 최근 trend 댓글(comments_<날짜>.jsonl · fresh_comments) 또는 분석 결과 personas.json 원문에 글자 그대로 있어야 함.
#   · 정당·정치인 이름은 넣지 않음 (채널 설명 — 정치 ✗). 칸마다 최대 MAX_ITEMS 개 — 넘으면 오래된 것부터 빼라고 알림.
# 쓰기:
#   python3 tools/persona_live.py init <주제> [--force]        분석 결과(<주제>/result/outliers/personas.json)로 처음 만듦
#   python3 tools/persona_live.py status <주제>                오늘 고쳤는지 · 오래된 칸 · 쓸 수 있는 재료(trend·news 날짜)
#   python3 tools/persona_live.py inputs <주제> [--date D]     그날 재료 한 장 → inputs_<D>.md
#   python3 tools/persona_live.py apply <주제> <changes.json> [--dry-run]
#   python3 tools/persona_live.py feed <주제> [--out <toml>]   피드 시험(tools/feed_sheet.py)용 검토자 설명 (처지 + 원문 댓글만)
#   python3 tools/persona_live.py --selftest
# ※ 연구·교육용 — 투자 권유 아님.
from __future__ import annotations

import argparse
import json
import logging
import re
import sys
import tempfile
import time
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = "v1.1"
LOG = logging.getLogger("persona_live")
TOPIC_RX = re.compile(r"^[a-z][a-z0-9_-]{1,30}$")
VID_RX = re.compile(r"^[0-9A-Za-z_-]{11}$")
FIELDS = {"situation": "상황", "curiosity": "호기심", "worry": "걱정", "anxiety": "불안", "wants": "원하는 것", "habit": "버릇"}
SINGLE = {"situation", "habit"}                  # 글 하나 (나머지는 목록)
NEED_VOICE = {"curiosity", "worry", "anxiety", "wants", "habit"}   # 시청자 말(c:)이 꼭 있어야 하는 칸
MAX_ITEMS = 4                                    # 목록 칸마다 최대 — 넘으면 오래된 것부터 빼게
MAX_TEXT, MAX_BASIS, MIN_QUOTE = 120, 80, 12
STALE_DAYS = 14                                  # 이보다 오래 다시 확인하지 않은 칸은 status 가 '오래됨'
TREND_MAX_AGE = 14                               # c:·v: 근거로 쓰는 trend 파일 — 바꾸는 날부터 이 날수 안
NEWS_MAX_AGE = 7
POLITICS = re.compile(r"대통령|이재명|윤석열|김건희|한동훈|민주당|국민의힘|국힘|좌파|우파|정권|탄핵")


def log(stage: str, level: int = logging.INFO, **kv) -> None:
    ts = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    LOG.log(level, f"[{stage}] [{ts}] " + " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) else v}" for k, v in kv.items()))


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", str(s or "")).strip()


def flat(s: str, n: int) -> str:
    s = norm(s)
    return s if len(s) <= n else s[:n] + "…"


def pdir(root: Path, topic: str) -> Path:
    return root / topic / "result" / "persona"


def read_json(p: Path, default=None):
    try:
        return json.loads(p.read_text("utf-8"))
    except (OSError, ValueError):
        return default


def write_json(p: Path, d) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(p.suffix + ".tmp")
    tmp.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", "utf-8")
    tmp.replace(p)


def check_topic(root: Path, topic: str) -> str:
    if not TOPIC_RX.match(topic) or not (root / topic).is_dir():
        raise SystemExit(f"[ERROR] 주제 폴더가 없음: {topic} — 예: stock · economic · history")
    return topic


# ------------------------------------------------------------------ 재료 읽기
def trend_files(root: Path, topic: str, upto: str, max_age: int = TREND_MAX_AGE) -> list[tuple[str, Path]]:
    """(날짜, trend_<날짜>.json) — upto 날짜부터 max_age 일 안, 새것 먼저."""
    d0 = (date.fromisoformat(upto) - timedelta(days=max_age)).isoformat()
    out = []
    for p in sorted((root / topic / "result" / "trend").glob("trend_*.json"), reverse=True):
        dd = p.stem[6:]
        if d0 <= dd <= upto:
            out.append((dd, p))
    return out


def news_files(root: Path, topic: str, upto: str, max_age: int = NEWS_MAX_AGE) -> list[tuple[str, Path]]:
    d0 = (date.fromisoformat(upto) - timedelta(days=max_age)).isoformat()
    return [(p.stem[5:], p) for p in sorted(pdir(root, topic).glob("news_*.json"), reverse=True) if d0 <= p.stem[5:] <= upto]


def persona_quotes(p: dict, n: int = 6) -> list[dict]:
    """personas.json 한 사람의 원문 — 공감 많은 질문 + 대표 원문 (중복 뺌)."""
    seen, out = set(), []
    for src in (p.get("top_questions") or [], p.get("quotes") or []):
        for q in src:
            t = norm(q.get("text"))
            if t and t not in seen:
                seen.add(t)
                out.append({"text": t, "likes": int(q.get("likes") or 0), "from": "personas.json"})
    out.sort(key=lambda q: -q["likes"])
    return out[:n]


def who_line_crisis(p: dict) -> str:
    """crisis_lab.py 'final' 한 사람 → 처지 줄 (쇼츠 몫·위험 유형·장르 — 숫자만)."""
    bits = []
    if p.get("shorts_share") is not None:
        bits.append(f"쇼츠 댓글 {round(100 * p['shorts_share'])}%")
    dz = [f"{k.replace('_', ' ')} {round(100 * v)}%" for k, v in list((p.get("top_danger") or {}).items())[:3] if round(100 * v) >= 1]
    if dz:
        bits.append("본 위험 유형 " + ", ".join(dz))
    gn = [f"{k} {round(100 * v)}%" for k, v in list((p.get("top_genre") or {}).items())[:2] if round(100 * v) >= 1]
    if gn:
        bits.append("장르 " + ", ".join(gn))
    bits.append(f"근거 댓글 {p.get('n', 0)}개")
    return " · ".join(bits)


def source_personas(root: Path, topic: str) -> tuple[Path | None, str, list[dict]]:
    """분석 결과 페르소나 → (파일, 만든 때, [{key, name, n, who, quotes, texts}]). 표준 분석기 꼴이 먼저, 없으면 crisis 꼴."""
    std = root / topic / "result" / "outliers" / "personas.json"
    pj = read_json(std)
    if pj and pj.get("personas"):
        out = [{"key": p["key"], "name": p["name"], "n": p.get("n", 0), "who": who_line(p), "quotes": persona_quotes(p),
                "texts": [norm(q.get("text")) for q in (p.get("top_questions") or []) + (p.get("quotes") or [])]} for p in pj["personas"]]
        return std, str(pj.get("made", "?")), out
    cr = root / topic / "result" / "personas.json"
    cj = read_json(cr)
    if cj and cj.get("final"):
        out = []
        for p in cj["final"]:
            qs = sorted(({"text": norm(q.get("text")), "likes": int(q.get("likes") or 0), "from": "personas.json"} for q in p.get("quotes") or []), key=lambda q: -q["likes"])
            out.append({"key": p.get("id") or p.get("key"), "name": p["name"], "n": p.get("n", 0), "who": who_line_crisis(p), "quotes": qs[:6],
                        "texts": [q["text"] for q in qs]})
        for sgm in cj.get("segments") or []:                      # 세부 묶음 원문도 근거(c:)로 쓸 수 있게
            if out and sgm.get("quotes"):
                out[0].setdefault("_extra", []).extend(norm(q.get("text")) for q in sgm["quotes"])
        made = ""
        rl = root / topic / "result" / "run_log.txt"
        if rl.is_file():
            m = re.search(r"\d{4}-\d{2}-\d{2}", rl.read_text("utf-8")[:2000])
            made = m.group(0) if m else ""
        return cr, made or "?", out
    return None, "", []


def evidence(root: Path, topic: str, upto: str) -> dict:
    """근거로 쓸 수 있는 것 — 댓글 글(정규화), 영상 ID, 뉴스 주소, 시장 이름."""
    E = {"comments": [], "videos": {}, "news": {}, "market": {}, "trend_dates": [], "news_dates": []}
    for dd, p in trend_files(root, topic, upto):
        t = read_json(p, {}) or {}
        E["trend_dates"].append(dd)
        for k in ("top_long", "top_small", "fresh", "top_short"):
            for v in t.get(k) or []:
                E["videos"].setdefault(v["id"], {"title": v.get("title", ""), "views_per_day": v.get("views_per_day"), "date": dd})
        for m in t.get("market") or []:
            E["market"].setdefault(m["name"], {**m, "date": dd})
        for c in t.get("fresh_comments") or []:
            E["comments"].append(norm(c.get("text")))
        cj = p.with_name(f"comments_{dd}.jsonl")
        if cj.is_file():
            for ln in cj.read_text("utf-8").splitlines():
                try:
                    E["comments"].append(norm(json.loads(ln).get("text")))
                except ValueError:
                    continue
    for pp in source_personas(root, topic)[2]:                # v1.1 표준 분석기 꼴·crisis 꼴 둘 다
        E["comments"].extend(pp["texts"] + pp.get("_extra", []))
    for dd, p in news_files(root, topic, upto):
        E["news_dates"].append(dd)
        for n in read_json(p, []) or []:
            if n.get("url"):
                E["news"].setdefault(n["url"], {**n, "file_date": dd})
    E["_blob"] = "\n".join(E["comments"])
    return E


def check_src(s: str, E: dict, root: Path, topic: str) -> str | None:
    """근거 하나 → 문제 글 (없으면 None)."""
    kind, _, val = s.partition(":")
    val = val.strip()
    if kind == "c":
        q = norm(val.strip("\"'“”‘’"))
        if len(q) < MIN_QUOTE:
            return f"c: 원문이 {MIN_QUOTE}자보다 짧음 — 댓글을 그대로 더 길게"
        return None if q in E["_blob"] else "c: 원문이 최근 trend 댓글·personas.json 에 글자 그대로 없음 (고친 말·요약은 안 됨)"
    if kind == "v":
        if not VID_RX.match(val):
            return "v: 영상 ID 꼴이 아님 (11자)"
        if val in E["videos"] or any((root / topic / "result" / "outliers").glob(f"*_{val}")):
            return None
        return "v: 최근 trend·분석 사례에 없는 영상"
    if kind == "n":
        return None if val in E["news"] else f"n: news_<날짜>.json(최근 {NEWS_MAX_AGE}일)에 없는 주소"
    if kind == "m":
        return None if val in E["market"] else "m: 최근 trend 의 시장 이름이 아님"
    return "근거 꼴은 c:·v:·n:·m: 중 하나"


# ------------------------------------------------------------------ init
def who_line(p: dict) -> str:
    age = (p.get("age") or {}).get("dist") or {}
    ages = sorted(age.items(), key=lambda x: -x[1])[:2]
    know = (p.get("know") or {}).get("level")
    states = [f"{s['name']} {round(100 * s['share'])}%" for s in (p.get("states") or [])[:3] if round(100 * (s.get("share") or 0)) >= 1]
    bits = []
    if ages:
        bits.append("나이 " + "·".join(a for a, _ in ages))
    if know:
        bits.append(f"아는 정도 {know}")
    if states:
        bits.append("댓글로 본 처지 " + ", ".join(states))
    bits.append(f"근거 댓글 {p.get('n', 0)}개")
    return " · ".join(bits)


def cmd_init(root: Path, topic: str, force: bool = False) -> dict:
    out = pdir(root, topic) / "live.json"
    if out.exists() and not force:
        raise SystemExit(f"[ERROR] 이미 있음: {out.relative_to(root)} — 처음부터 다시 만들려면 --force (내역도 지워짐)")
    src, made, src_ps = source_personas(root, topic)
    if not src_ps:
        raise SystemExit(f"[ERROR] 분석 결과 페르소나가 없음: {topic}/result/outliers/personas.json (또는 crisis 꼴 {topic}/result/personas.json) — 먼저 분석·python3 tools/personas.py {topic}")
    today = date.today().isoformat()
    L = {"topic": topic, "tool": f"persona_live.py {VERSION}", "made": today, "updated": "",
         "source_personas": f"{src.relative_to(root).as_posix()} ({made})", "personas": [], "log": []}
    for p in src_ps:
        L["personas"].append({"key": p["key"], "name": p["name"], "n": p["n"], "who": p["who"],
                              "situation": None, "habit": None, "curiosity": [], "worry": [], "anxiety": [], "wants": [],
                              "quotes": p["quotes"]})
    L["log"].append({"date": today, "persona": "*", "field": "*", "op": "init", "before": "", "after": f"{len(L['personas'])}명",
                     "basis": "분석 결과 페르소나(댓글 묶음)로 처음 만듦 — 생각·원하는 것은 첫 업데이트에서", "src": [L["source_personas"]]})
    write_json(out, L)
    write_log_md(root, topic, L)
    log("INIT", topic=topic, personas=len(L["personas"]), source=L["source_personas"], file=str(out.relative_to(root)))
    return L


def load_live(root: Path, topic: str) -> dict:
    L = read_json(pdir(root, topic) / "live.json")
    if not L:
        raise SystemExit(f"[ERROR] 페르소나 파일 없음 — 먼저 python3 tools/persona_live.py init {topic}")
    return L


# ------------------------------------------------------------------ status
def items_of(p: dict, f: str) -> list[dict]:
    v = p.get(f)
    return ([v] if v else []) if f in SINGLE else list(v or [])


def cmd_status(root: Path, topic: str, today: str | None = None) -> dict:
    today = today or date.today().isoformat()
    L = load_live(root, topic)
    stale, empty = [], []
    for p in L["personas"]:
        for f in FIELDS:
            its = items_of(p, f)
            if not its and f != "habit":
                empty.append(f"{p['key']}.{f}")
            for it in its:
                if (date.fromisoformat(today) - date.fromisoformat(it.get("date", today))).days > STALE_DAYS:
                    stale.append(f"{p['key']}.{f}: {flat(it['text'], 30)}")
    tr = trend_files(root, topic, today)
    nw = news_files(root, topic, today)
    res = {"topic": topic, "updated": L.get("updated") or "(아직 없음)", "done_today": L.get("updated") == today,
           "empty": empty, "stale": stale, "trend_latest": tr[0][0] if tr else None, "news_latest": nw[0][0] if nw else None}
    log("STATUS", topic=topic, updated=res["updated"], done_today=res["done_today"], empty=len(empty), stale=len(stale),
        trend_latest=res["trend_latest"] or "-", news_latest=res["news_latest"] or "-")
    if not res["done_today"]:
        steps = []
        if res["trend_latest"] != today:
            steps.append(f"python3 tools/trend_scan.py {topic}")
        if res["news_latest"] != today:
            steps.append(f"WebSearch 뉴스 3~6건 → {topic}/result/persona/news_{today}.json")
        steps += [f"python3 tools/persona_live.py inputs {topic}", f"(바꿀 것 → {topic}/result/persona/changes_{today}.json)",
                  f"python3 tools/persona_live.py apply {topic} {topic}/result/persona/changes_{today}.json",
                  f"python3 tools/analysis_board.py {topic} → 분석 판 다시 올림"]
        log("NEXT", topic=topic, steps=" → ".join(steps))
    return res


# ------------------------------------------------------------------ inputs
def cmd_inputs(root: Path, topic: str, day: str | None = None) -> Path:
    day = day or date.today().isoformat()
    L = load_live(root, topic)
    E = evidence(root, topic, day)
    w = (out := []).append
    w(f"# {topic} — 페르소나 업데이트 재료 ({day})")
    w("")
    w(f"`tools/persona_live.py {VERSION}` · trend {', '.join(E['trend_dates']) or '없음'} · 뉴스 {', '.join(E['news_dates']) or '없음'}. "
      "규칙: 바꾸는 것마다 basis + src (c:원문 그대로 · v:영상 · n:뉴스 주소 · m:시장) · 생각·원하는 것은 c: 꼭 하나 · 정치 이름 ✗.")
    w("")
    w("## 1. 지금 페르소나")
    for p in L["personas"]:
        w(f"### {p['key']} — {p['name']}")
        w(f"- 처지: {p['who']}")
        for f, nm in FIELDS.items():
            its = items_of(p, f)
            w(f"- {nm}: " + (" / ".join(f"{flat(i['text'], 60)} ({i.get('date', '?')})" for i in its) if its else "(비어 있음)"))
    tr = trend_files(root, topic, day)
    if tr:
        t = read_json(tr[0][1], {}) or {}
        w("")
        w(f"## 2. 최근 유튜브 ({tr[0][0]} · 최근 {t.get('days', '?')}일)")
        if t.get("market"):
            w("- 시장: " + " · ".join(f"{m['name']} {m['close']} (1년 최고가 대비 {m['from_high']}%, 5일 {m['d5']}%)" for m in t["market"]))
        w("- 하루 조회수 상위 롱폼:")
        for v in (t.get("top_long") or [])[:12]:
            w(f"  - v:{v['id']} 하루 {v.get('views_per_day')} · {flat(v['title'], 70)}")
        w("- 작은 채널 배수 상위:")
        for v in (t.get("top_small") or [])[:6]:
            w(f"  - v:{v['id']} 구독자 대비 {v.get('ratio')}배 · {flat(v['title'], 70)}")
        w("- 쇼츠 상위:")
        for v in (t.get("top_short") or [])[:6]:
            w(f"  - v:{v['id']} 하루 {v.get('views_per_day')} · {flat(v['title'], 60)}")
        tw = ((t.get("summary") or {}).get("title_words") or [])[:8]
        if tw:
            w("- 제목 낱말: " + " · ".join(f"{x['word']} {x['n']}개" for x in tw if x.get("n")))
        cj = tr[0][1].with_name(f"comments_{tr[0][0]}.jsonl")
        rows = []
        if cj.is_file():
            for ln in cj.read_text("utf-8").splitlines():
                try:
                    rows.append(json.loads(ln))
                except ValueError:
                    continue
        rows += [{"text": c.get("text"), "likes": c.get("likes", 0), "day": c.get("day")} for c in t.get("fresh_comments") or []]
        seen, top = set(), []
        for r in sorted(rows, key=lambda r: -int(r.get("likes") or 0)):
            k = norm(r.get("text"))[:40]
            if k and k not in seen and not POLITICS.search(r.get("text") or ""):
                seen.add(k)
                top.append(r)
            if len(top) >= 40:
                break
        w(f"- 공감 많은 최근 댓글 {len(top)}개 (정치 이름 든 댓글 뺌 — c: 로 쓸 때는 글자 그대로 12자 이상):")
        for r in top:
            w(f"  - ({r.get('likes')}) {flat(r.get('text'), 140)}")
    else:
        w("")
        w(f"## 2. 최근 유튜브 — 없음 → 먼저 `python3 tools/trend_scan.py {topic}`")
    nw = news_files(root, topic, day)
    w("")
    if nw:
        w(f"## 3. 뉴스 ({', '.join(d for d, _ in nw)})")
        for dd, p in nw:
            for n in read_json(p, []) or []:
                w(f"- n:{n.get('url')} · {n.get('date', '?')} {n.get('source', '')} — {flat(n.get('title'), 70)} — {flat(n.get('note'), 90)}")
    else:
        w(f"## 3. 뉴스 — 없음 → WebSearch 로 3~6건 모아 `{topic}/result/persona/news_{day}.json`")
    w("")
    w("## 4. 분석 결과 원문 (personas.json — c: 로 쓸 수 있음)")
    for p in L["personas"]:
        for q in p.get("quotes") or []:
            w(f"- {p['key']} ({q['likes']}) {flat(q['text'], 140)}")
    w("")
    w("## 5. 바꿀 것 꼴 (changes_<날짜>.json)")
    w('```json\n{"date": "' + day + '", "changes": [\n  {"persona": "<key>", "field": "worry", "op": "add", "text": "…(120자 안)", '
      '"basis": "…(80자 안 — 왜 바꾸는지)", "src": ["c:<댓글 원문 그대로>", "n:<뉴스 주소>"]},\n'
      '  {"persona": "<key>", "field": "situation", "op": "set", "text": "…", "basis": "…", "src": ["m:<시장>", "n:<주소>"]},\n'
      '  {"persona": "<key>", "field": "wants", "op": "remove", "index": 0, "basis": "…", "src": ["c:…"]},\n'
      '  {"persona": "<key>", "field": "curiosity", "op": "keep", "index": 1, "basis": "오늘도 같은 물음 — 날짜만 새로", "src": ["c:…"]}\n]}\n```')
    w("op: set(상황·버릇) · add · replace(index) · remove(index) · keep(index — 다시 확인, 날짜만 새로). 목록 칸은 최대 "
      f"{MAX_ITEMS}개. {STALE_DAYS}일 넘게 확인 안 한 칸은 keep 이나 remove.")
    p_out = pdir(root, topic) / f"inputs_{day}.md"
    p_out.parent.mkdir(parents=True, exist_ok=True)
    p_out.write_text("\n".join(out) + "\n", "utf-8")
    log("INPUTS", topic=topic, day=day, trend=E["trend_dates"][:1] or "-", news=len(E["news"]), comments=len(E["comments"]),
        file=str(p_out.relative_to(root)), chars=sum(len(x) for x in out))
    return p_out


# ------------------------------------------------------------------ apply
def validate(L: dict, C: dict, E: dict, root: Path, topic: str) -> list[str]:
    errs = []
    keys = {p["key"]: p for p in L["personas"]}
    day = C.get("date") or ""
    try:
        date.fromisoformat(day)
    except ValueError:
        errs.append(f"date 꼴이 아님: {day!r} (예 2026-11-12)")
    for i, ch in enumerate(C.get("changes") or [], 1):
        at = f"#{i} {ch.get('persona')}.{ch.get('field')} {ch.get('op')}"
        p, f, op = keys.get(ch.get("persona")), ch.get("field"), ch.get("op")
        if not p:
            errs.append(f"{at}: 없는 페르소나 (있는 것: {', '.join(keys)})")
            continue
        if f not in FIELDS:
            errs.append(f"{at}: 칸 이름은 {', '.join(FIELDS)} 중 하나")
            continue
        if op not in ("set", "add", "replace", "remove", "keep"):
            errs.append(f"{at}: op 는 set·add·replace·remove·keep")
            continue
        if (op == "set") != (f in SINGLE) and op in ("set", "add", "replace"):
            errs.append(f"{at}: {FIELDS[f]} 칸은 " + ("set 만" if f in SINGLE else "add·replace·remove·keep"))
        if op in ("set", "add", "replace"):
            t = norm(ch.get("text"))
            if not t:
                errs.append(f"{at}: text 가 비었음")
            elif len(t) > MAX_TEXT:
                errs.append(f"{at}: text {len(t)}자 > {MAX_TEXT}")
            if POLITICS.search(t):
                errs.append(f"{at}: 정당·정치인 이름 ✗ (채널 설명)")
        if op in ("replace", "remove", "keep"):
            its = items_of(p, f)
            idx = ch.get("index", 0 if f in SINGLE else None)
            if not isinstance(idx, int) or not 0 <= idx < len(its):
                errs.append(f"{at}: index {idx} 가 없음 (지금 {len(its)}개)")
        b = norm(ch.get("basis"))
        if not b:
            errs.append(f"{at}: basis(근거 한 줄)가 없음")
        elif len(b) > MAX_BASIS:
            errs.append(f"{at}: basis {len(b)}자 > {MAX_BASIS} — 짧게")
        src = ch.get("src") or []
        if not src:
            errs.append(f"{at}: src(근거)가 없음")
        for s in src:
            e = check_src(str(s), E, root, topic)
            if e:
                errs.append(f"{at}: {e} — {flat(str(s), 50)}")
        if f in NEED_VOICE and op != "remove" and not any(str(s).startswith("c:") for s in src):
            errs.append(f"{at}: {FIELDS[f]} 칸은 시청자 말(c:)이 꼭 하나 — 뉴스·시장만으로는 생각을 지어낼 수 없음")
    return errs


def apply_changes(L: dict, C: dict) -> list[dict]:
    keys = {p["key"]: p for p in L["personas"]}
    day, logs = C["date"], []
    # remove 는 index 가 밀리지 않게 큰 것부터 · 나머지는 적힌 순서대로
    chs = list(C.get("changes") or [])
    rem = sorted([c for c in chs if c["op"] == "remove"], key=lambda c: (c["persona"], c["field"], -c["index"]))
    for ch in [c for c in chs if c["op"] != "remove"] + rem:
        p, f, op = keys[ch["persona"]], ch["field"], ch["op"]
        new = {"text": norm(ch.get("text")), "date": day, "src": list(ch["src"]), "basis": norm(ch["basis"])}
        if f in SINGLE:
            before = (p.get(f) or {}).get("text", "")
            if op == "remove":
                p[f] = None
            elif op == "keep":
                p[f]["date"] = day
                new["text"] = before
            else:
                p[f] = new
        else:
            lst = p.setdefault(f, [])
            if op == "add":
                before = ""
                lst.append(new)
            elif op == "replace":
                before = lst[ch["index"]]["text"]
                lst[ch["index"]] = new
            elif op == "remove":
                before = lst.pop(ch["index"])["text"]
                new["text"] = ""
            else:
                before = lst[ch["index"]]["text"]
                lst[ch["index"]]["date"] = day
                new["text"] = before
        logs.append({"date": day, "persona": p["key"], "field": f, "op": op, "before": before, "after": new["text"],
                     "basis": new["basis"], "src": new["src"]})
    L["log"] = logs + L.get("log", [])
    L["updated"] = day
    L["tool"] = f"persona_live.py {VERSION}"
    return logs


def cmd_apply(root: Path, topic: str, path: str, dry: bool = False) -> dict:
    L = load_live(root, topic)
    C = read_json(Path(path))
    if not C or not isinstance(C.get("changes"), list):
        raise SystemExit(f"[ERROR] 바꿀 것 파일을 못 읽음: {path} — inputs_<날짜>.md 5번 꼴")
    E = evidence(root, topic, C.get("date") or date.today().isoformat())
    log("APPLY", topic=topic, file=path, changes=len(C["changes"]), trend=",".join(E["trend_dates"]) or "-", news=len(E["news"]))
    errs = validate(L, C, E, root, topic)
    if errs:
        for e in errs:
            log("REJECT", logging.WARNING, issue=e)
        log("APPLY", logging.ERROR, topic=topic, rejected=len(errs), applied=0, next="문제 줄을 고친 뒤 다시 apply — 하나라도 틀리면 아무것도 바꾸지 않음")
        return {"ok": False, "errors": errs}
    logs = apply_changes(L, C)
    over = [f"{p['key']}.{f} {len(p[f])}개" for p in L["personas"] for f in FIELDS if f not in SINGLE and len(p.get(f) or []) > MAX_ITEMS]
    for x in logs:
        log("CHANGE", persona=x["persona"], field=FIELDS[x["field"]], op=x["op"], before=flat(x["before"], 40) or "-",
            after=flat(x["after"], 40) or "-", basis=x["basis"], src=len(x["src"]))
    if over:
        log("APPLY", logging.WARNING, over_max=", ".join(over), next=f"칸마다 {MAX_ITEMS}개까지 — 다음 업데이트에서 오래된 것부터 remove")
    if not dry:
        write_json(pdir(root, topic) / "live.json", L)
        write_log_md(root, topic, L)
    log("APPLY", topic=topic, applied=len(logs), dry_run=dry, updated=L["updated"], file=f"{topic}/result/persona/live.json")
    return {"ok": True, "applied": len(logs), "over": over}


def write_log_md(root: Path, topic: str, L: dict) -> None:
    w = (out := []).append
    w(f"# {topic} — 페르소나 바뀐 내역 (새것 위)")
    w("")
    w(f"`tools/persona_live.py {VERSION}` · 지금 페르소나 = `live.json` · 근거 c:댓글 원문 · v:영상 · n:뉴스 · m:시장")
    w("")
    w("| 날짜 | 페르소나 | 칸 | 무엇을 | 근거 |")
    w("|---|---|---|---|---|")
    opn = {"init": "처음 만듦", "set": "고침", "add": "더함", "replace": "바꿈", "remove": "뺌", "keep": "다시 확인"}
    for x in L.get("log", []):
        what = x["after"] if x["op"] in ("set", "add", "replace", "init") else x["before"]
        if x["op"] == "replace":
            what = f"{flat(x['before'], 40)} → {flat(x['after'], 60)}"
        w(f"| {x['date']} | {x['persona']} | {FIELDS.get(x['field'], x['field'])} | {opn.get(x['op'], x['op'])}: {flat(what, 90).replace('|', '/')} | "
          f"{x['basis'].replace('|', '/')} ({len(x['src'])}) |")
    p = pdir(root, topic) / "log.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("\n".join(out) + "\n", "utf-8")


# ------------------------------------------------------------------ feed
def cmd_feed(root: Path, topic: str, out: str | None = None) -> str:
    """tools/feed_sheet.py 검토자 설명 — who = 처지·상황(사실), comments = 원문 댓글만 (내 요약 ✗)."""
    L = load_live(root, topic)
    letters = "ABCDEFGH"
    T = [f"# VERSION: {VERSION} — {date.today()} — tools/persona_live.py feed {topic} 로 만듦 (live.json {L.get('updated') or '-'})",
         "# who = 처지 + 상황(사실) · comments = 원문 댓글만 — 내가 쓴 속생각 요약 줄은 넣지 않음 (feed_sheet 가 막음). 연구·교육용 — 투자 권유 아님.", ""]
    for i, p in enumerate(L["personas"][:len(letters)]):
        cm, seen = [], set()
        for f in ("worry", "anxiety", "curiosity", "wants", "habit"):
            for it in items_of(p, f):
                for s in it.get("src") or []:
                    if s.startswith("c:"):
                        q = norm(s[2:].strip("\"'“”‘’"))
                        if q not in seen:
                            seen.add(q)
                            cm.append(q)
        for q in p.get("quotes") or []:
            if q["text"] not in seen and len(cm) < 8:
                seen.add(q["text"])
                cm.append(q["text"])
        who = [p["who"]] + ([p["situation"]["text"]] if p.get("situation") else [])
        habit = (p.get("habit") or {}).get("text") or "댓글 말투대로 — 자기 처지를 부르는 말에 손이 가고, 남 얘기·훈계에는 식는다고 가정하지 않는다"
        T += [f"[{letters[i]}]", f"name = {json.dumps(p['name'], ensure_ascii=False)}", f"who = {json.dumps(who, ensure_ascii=False)}",
              f"habit = {json.dumps(habit, ensure_ascii=False)}", "comments = [" + ", ".join(json.dumps(flat(c, 160), ensure_ascii=False) for c in cm[:8]) + "]", ""]
    text = "\n".join(T)
    if out:
        Path(out).write_text(text, "utf-8")
        log("FEED", topic=topic, personas=min(len(L["personas"]), len(letters)), file=out)
    else:
        print(text)
    return text


# ------------------------------------------------------------------ selftest
def selftest() -> int:
    ok = True

    def chk(name, cond):
        nonlocal ok
        ok &= bool(cond)
        print(("✅ " if cond else "❌ ") + name)

    with tempfile.TemporaryDirectory() as d:
        R = Path(d)
        (R / "demo" / "result" / "outliers").mkdir(parents=True)
        (R / "demo" / "result" / "trend").mkdir(parents=True)
        (R / "demo" / "result" / "persona").mkdir(parents=True)
        write_json(R / "demo/result/outliers/personas.json", {"made": "2026-11-01", "personas": [
            {"key": "w", "name": "직장인", "n": 10, "age": {"dist": {"40대": 6}}, "know": {"level": "기초"},
             "states": [{"name": "적립식", "share": 0.3}], "top_questions": [{"text": "월급으로 매달 넣는데 지금 멈춰야 하나요?", "likes": 9}], "quotes": []}]})
        today = "2026-11-12"
        write_json(R / "demo/result/trend/trend_2026-11-11.json", {"days": 7, "market": [{"name": "코스피", "close": 1, "from_high": -40, "d5": -3}],
                   "top_long": [{"id": "AAAAAAAAAAA", "title": "폭락장", "views_per_day": 100}], "fresh_comments": []})
        (R / "demo/result/trend/comments_2026-11-11.jsonl").write_text(json.dumps({"text": "계좌 보기가 무서워서 앱을 지웠습니다 정말로요", "likes": 50}, ensure_ascii=False) + "\n", "utf-8")
        write_json(R / "demo/result/persona/news_2026-11-12.json", [{"title": "증시 급락", "source": "x", "date": today, "url": "https://ex.com/a", "note": "n"}])
        L = cmd_init(R, "demo")
        chk("init: 페르소나 1명 · 처지 줄", len(L["personas"]) == 1 and "40대" in L["personas"][0]["who"])
        bad = {"date": today, "changes": [{"persona": "w", "field": "worry", "op": "add", "text": "더 떨어질까 봐", "basis": "뉴스", "src": ["n:https://ex.com/a"]}]}
        (R / "bad.json").write_text(json.dumps(bad, ensure_ascii=False), "utf-8")
        r = cmd_apply(R, "demo", str(R / "bad.json"))
        chk("apply: 걱정 칸을 뉴스만으로 → 거부", not r["ok"] and any("c:" in e for e in r["errors"]))
        fake = {"date": today, "changes": [{"persona": "w", "field": "worry", "op": "add", "text": "x", "basis": "b", "src": ["c:이런 댓글은 어디에도 없습니다 지어낸 말"]}]}
        (R / "fake.json").write_text(json.dumps(fake, ensure_ascii=False), "utf-8")
        chk("apply: 지어낸 원문 → 거부", not cmd_apply(R, "demo", str(R / "fake.json"))["ok"])
        pol = {"date": today, "changes": [{"persona": "w", "field": "situation", "op": "set", "text": "대통령 발언 뒤", "basis": "b", "src": ["m:코스피"]}]}
        (R / "pol.json").write_text(json.dumps(pol, ensure_ascii=False), "utf-8")
        chk("apply: 정치 이름 → 거부", not cmd_apply(R, "demo", str(R / "pol.json"))["ok"])
        good = {"date": today, "changes": [
            {"persona": "w", "field": "situation", "op": "set", "text": "코스피가 1년 최고가보다 40% 아래", "basis": "시장·뉴스", "src": ["m:코스피", "n:https://ex.com/a"]},
            {"persona": "w", "field": "anxiety", "op": "add", "text": "계좌를 보기 무서움", "basis": "공감 50 댓글", "src": ["c:계좌 보기가 무서워서 앱을 지웠습니다"]},
            {"persona": "w", "field": "wants", "op": "add", "text": "적립을 멈출지 정할 기준", "basis": "분석 원문 질문", "src": ["c:월급으로 매달 넣는데 지금 멈춰야 하나요?"]}]}
        (R / "good.json").write_text(json.dumps(good, ensure_ascii=False), "utf-8")
        r = cmd_apply(R, "demo", str(R / "good.json"))
        L2 = load_live(R, "demo")
        chk("apply: 근거 있는 3건 반영 · 내역 3줄 + init", r["ok"] and r["applied"] == 3 and len(L2["log"]) == 4 and L2["updated"] == today)
        rm = {"date": today, "changes": [{"persona": "w", "field": "anxiety", "op": "remove", "index": 0, "basis": "오늘 댓글에 없음", "src": ["m:코스피"]}]}
        (R / "rm.json").write_text(json.dumps(rm, ensure_ascii=False), "utf-8")
        chk("apply: remove 는 c: 없이도 됨", cmd_apply(R, "demo", str(R / "rm.json"))["ok"] and not load_live(R, "demo")["personas"][0]["anxiety"])
        st = cmd_status(R, "demo", today)
        chk("status: 오늘 했음", st["done_today"])
        chk("log.md: 표", "| 날짜 |" in (R / "demo/result/persona/log.md").read_text("utf-8"))
        p_in = cmd_inputs(R, "demo", today)
        chk("inputs: 재료 한 장 (댓글·뉴스)", "계좌 보기가" in p_in.read_text("utf-8") and "n:https://ex.com/a" in p_in.read_text("utf-8"))
        t = cmd_feed(R, "demo", str(R / "feed.toml"))
        chk("feed: 원문 댓글 들어감 · 머릿속 없음", "월급으로 매달" in t and "머릿속" not in t)
        (R / "cr" / "result").mkdir(parents=True)
        write_json(R / "cr/result/personas.json", {"final": [{"id": "F1", "name": "웃으려고 보는 쇼츠 시청자", "n": 448, "shorts_share": 0.96,
                   "top_danger": {"사고_추락·시설": 0.46}, "top_genre": {"유머·장난": 0.45}, "quotes": [{"text": "단체 소송 갈거니까 이미 고객이자 한팀임", "likes": 10}]}], "segments": []})
        Lc = cmd_init(R, "cr")
        chk("init: crisis 꼴(final) 읽음 · 처지 줄", Lc["personas"][0]["key"] == "F1" and "쇼츠 댓글 96%" in Lc["personas"][0]["who"])
        chk("evidence: crisis 원문이 c: 근거", "단체 소송 갈거니까" in evidence(R, "cr", today)["_blob"])
    print("[SELFTEST] " + ("✅ 모두 통과" if ok else "❌ 실패 있음"))
    return 0 if ok else 1


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="살아 있는 페르소나 — 분석 결과로 만들고 매일 최근 유튜브·뉴스로 고침 (근거 검사)")
    ap.add_argument("cmd", nargs="?", choices=["init", "status", "inputs", "apply", "feed"])
    ap.add_argument("topic", nargs="?")
    ap.add_argument("file", nargs="?", help="apply: 바꿀 것 JSON")
    ap.add_argument("--date"); ap.add_argument("--force", action="store_true"); ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--out"); ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args(argv)
    logging.basicConfig(level=getattr(logging, a.log_level), format="%(message)s", stream=sys.stdout)
    if a.selftest:
        return selftest()
    if not a.cmd or not a.topic:
        ap.error("명령과 주제를 주세요 — 예: persona_live.py status stock")
    t = check_topic(ROOT, a.topic)
    t0 = time.perf_counter()
    if a.cmd == "init":
        cmd_init(ROOT, t, a.force)
    elif a.cmd == "status":
        cmd_status(ROOT, t, a.date)
    elif a.cmd == "inputs":
        cmd_inputs(ROOT, t, a.date)
    elif a.cmd == "apply":
        if not a.file:
            ap.error("apply 뒤에 바꿀 것 JSON 경로")
        r = cmd_apply(ROOT, t, a.file, a.dry_run)
        if not r["ok"]:
            return 2
    elif a.cmd == "feed":
        cmd_feed(ROOT, t, a.out)
    log("DONE", cmd=a.cmd, topic=t, seconds=round(time.perf_counter() - t0, 2))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
