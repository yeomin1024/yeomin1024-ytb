#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-11-25 — 새로: 새 분야 갭 탐색 — 조회수는 잘 나오는데 영상은 적은 분야를 지금 주제 밖까지 찾음
#   사용자 지시 2026-11-25 "여기서 다루고 있는 주제 이외에도 조회수 잘나오고 영상은 별로 없을 것 같은 주제 모두 찾아서 해야 돼" →
#   "일단 한국만하고 해외, 한국 둘다 할수 있는 주제면 더 좋아" · "롱폼, 쇼츠 둘다하고 못만드는 분야는 알아서 해 4번은 해도 되고 계속 진행해".
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.0 | 2026-11-25 | 최초 — discover-list · merge · interest-list · trends · supply · report · selftest | 모두 |
"""새 분야 갭 탐색 — 수요(구글 트렌드 유튜브 검색 관심도 + 하루 조회수) ÷ 공급(검색 상위의 최근 영상 수·큰 채널 몫) · 롱폼·쇼츠 따로.

  python3 tools/gap_scan.py new discover-list   # PC 1회차 목록 → new/result/gap/discover.json·.md (분류 25 · 씨앗 관련 검색어 · 자동완성)
  (PC)  powershell -ExecutionPolicy Bypass -File run_analyzer.ps1 -Trends -Folder new --list discover
  python3 tools/gap_scan.py new merge           # 받은 것 → 후보 낱말 candidates.csv·.md ('뺌: 까닭' 표시 — new/gap.toml [[filter]])
  (Claude) new/gap.toml [interest] ANCHOR·WORDS · [global] EN_ANCHOR · [[niche]] 채움
  python3 tools/gap_scan.py new interest-list   # PC 2회차 목록 → interest.json·.md (한국 관심도 + 해외 겸용: 전 세계 관심도·영어 자동완성)
  (PC)  powershell -ExecutionPolicy Bypass -File run_analyzer.ps1 -Trends -Folder new --list interest
  python3 tools/gap_scan.py new trends          # 관심도 (기준 낱말로 묶음끼리 이어 붙임) → demand.md · demand.json.gz
  python3 tools/gap_scan.py new supply          # 유튜브 API (키 = 환경 변수 YOUTUBE_API_KEY — '새 주제 탐색' 환경) · 낱말마다 검색 2번 = 200단위 · 이어서 됨
  python3 tools/gap_scan.py new report          # 갭 표 → gap_scan.md · gap_scan.csv
  python3 tools/gap_scan.py selftest            # 가짜 자료·가짜 API (진짜로 부르지 않음)

로그: [STAGE] [시각] key=value. ※ 연구·교육용 — 트렌드 값은 0~100 상대값, 검색 결과 수는 유튜브 추정치. 다른 채널의 클릭률·시청 지속률은 볼 수 없다.
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import csv
import datetime as dt
import gzip
import json
import logging
import math
import os
import re
import statistics as st
import sys
import time
import tomllib
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = "v1.0"
API = "https://www.googleapis.com/youtube/v3/"
log = logging.getLogger("gap_scan")


def stamp(stage: str, level: int = logging.INFO, **kv) -> None:
    log.log(level, "[%s] [%s] %s", stage, time.strftime("%Y-%m-%dT%H:%M:%S"), " ".join(f"{k}={v}" for k, v in kv.items()))


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip().lower())


def now_utc() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def iso_dur(s: str) -> int:
    m = re.fullmatch(r"P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", s or "")
    if not m:
        return 0
    d, h, mi, se = (int(x or 0) for x in m.groups())
    return d * 86400 + h * 3600 + mi * 60 + se


def fmt(n) -> str:
    if n is None:
        return "—"
    n = float(n)
    return f"{n / 1e4:,.1f}만" if n >= 1e4 else f"{n:,.0f}"


def pct_rank(values: dict) -> dict:
    """값 → 백분위 (0~100, 같은 값은 평균 순위). None 은 None."""
    xs = sorted((v, k) for k, v in values.items() if v is not None)
    out = {k: None for k in values}
    n = len(xs)
    if not n:
        return out
    i = 0
    while i < n:
        j = i
        while j + 1 < n and xs[j + 1][0] == xs[i][0]:
            j += 1
        r = (i + j) / 2
        for t in range(i, j + 1):
            out[xs[t][1]] = 100.0 * r / (n - 1) if n > 1 else 50.0
        i = j + 1
    return out


def mean_ok(xs):
    xs = [x for x in xs if x is not None]
    return sum(xs) / len(xs) if xs else None


# ─────────── 설정 ───────────
class Cfg:
    def __init__(self, topic: str, base: Path | None = None):
        self.topic = topic
        self.dir = (base or ROOT) / topic
        p = self.dir / "gap.toml"
        try:
            self.raw = tomllib.loads(p.read_text("utf-8"))
        except (OSError, tomllib.TOMLDecodeError) as ex:
            raise SystemExit(f"[CONFIG] {p} 를 읽지 못함 ({ex}) — new/gap.toml 참고")
        d = self.raw
        self.geo, self.hl, self.time = d.get("GEO", "KR"), d.get("HL", "ko"), d.get("TIME", "today 12-m")
        dc = d.get("discover", {})
        self.categories = [(int(i), n) for i, n in dc.get("CATEGORIES", [])]
        seeds = []
        if dc.get("SEEDS_FROM_NICHES"):
            try:
                nt = tomllib.loads((self.dir / "niches.toml").read_text("utf-8"))
                seeds += [k for x in nt.get("niche", []) for k in x.get("keywords", [])]
            except (OSError, tomllib.TOMLDecodeError) as ex:
                stamp("CONFIG", logging.WARNING, msg=f"niches.toml 못 읽음 ({ex}) — 씨앗은 SEEDS 만")
        seeds += list(dc.get("SEEDS", []))
        seen, self.seeds = set(), []
        for s in seeds:
            if norm(s) not in seen:
                seen.add(norm(s))
                self.seeds.append(s)
        self.seeds_per_batch = int(dc.get("SEEDS_PER_BATCH", 5))
        self.suffixes = list(dc.get("SUFFIXES", [""]))
        self.filters = [(f["why"], re.compile(f["rx"], re.I)) for f in d.get("filter", [])]
        it = d.get("interest", {})
        self.anchor, self.words = it.get("ANCHOR", ""), list(it.get("WORDS", []))
        gl = d.get("global", {})
        self.en_anchor, self.en_suffixes = gl.get("EN_ANCHOR", ""), list(gl.get("EN_SUFFIXES", [""]))
        sp = d.get("supply", {})
        self.top = int(sp.get("TOP", 100))
        self.recent_days, self.old_days = int(sp.get("RECENT_DAYS", 180)), int(sp.get("OLD_DAYS", 730))
        self.long_sec, self.short_sec, self.big_subs = int(sp.get("LONG_SEC", 240)), int(sp.get("SHORT_SEC", 180)), int(sp.get("BIG_SUBS", 1_000_000))
        self.niches = [{"name": n["name"], "rx": re.compile(n["rx"], re.I), "make": n.get("make", ""), "global": n.get("global", ""), "en": n.get("en", "")}
                       for n in d.get("niche", [])]
        self.out = self.dir / "result" / "gap"
        try:
            rules = tomllib.loads((self.dir / "analysis_rules.toml").read_text("utf-8"))
        except (OSError, tomllib.TOMLDecodeError):
            rules = {}
        self.succ_long = rules.get("success", {})
        self.succ_short = rules.get("shorts", {})
        stamp("CONFIG", topic=topic, file=str(p.relative_to(self.dir.parent)), categories=len(self.categories), seeds=len(self.seeds),
              suffixes=len(self.suffixes), filters=len(self.filters), interest_words=len(self.words), anchor=self.anchor or "(아직)",
              niches=len(self.niches), supply_top=self.top)

    def cant(self, q: str) -> str:
        for why, rx in self.filters:
            if rx.search(q or ""):
                return why
        return ""

    def niche_of(self, q: str) -> str:
        return next((n["name"] for n in self.niches if n["rx"].search(q or "")), "")


def save_gz(c: Cfg, name: str, obj) -> Path:
    c.out.mkdir(parents=True, exist_ok=True)
    p = c.out / name
    with gzip.open(p, "wt", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False)
    return p


def load_gz(c: Cfg, name: str, default=None):
    p = c.out / name
    if not p.exists():
        return default
    with gzip.open(p, "rt", encoding="utf-8") as f:
        return json.load(f)


def trends_url(words, geo, cat=0, time_="today 12-m", hl="ko"):
    q = urllib.parse.quote(",".join(words))
    return (f"https://trends.google.com/trends/explore?date={urllib.parse.quote(time_)}&geo={geo}&gprop=youtube"
            + (f"&cat={cat}" if cat else "") + (f"&q={q}" if words else "") + f"&hl={hl}")


def write_list(c: Cfg, name: str, spec: dict, title: str, lines: list[str]) -> None:
    c.out.mkdir(parents=True, exist_ok=True)
    (c.out / f"{name}.json").write_text(json.dumps(spec, ensure_ascii=False, indent=1), encoding="utf-8")
    kinds = {}
    for b in spec["batches"]:
        kinds[b.get("kind", "timeseries")] = kinds.get(b.get("kind", "timeseries"), 0) + 1
    L = [f"# {title}", "",
         f"> `tools/gap_scan.py {c.topic}` {VERSION} · {time.strftime('%Y-%m-%d %H:%M')} · 묶음 {len(spec['batches'])}개 ({' · '.join(f'{k} {v}' for k, v in kinds.items())})",
         f"> PC: `powershell -ExecutionPolicy Bypass -File run_analyzer.ps1 -Trends -Folder {c.topic} --list {name}` (tools/pc_trends.py v1.2 — 받은 것은 `{spec['out_dir']}/` 에)",
         "> 클라우드는 구글이 막음(trends.google.com HTTP 429 · 이 환경은 자동완성 주소도 프록시 403) → 집 인터넷에서. 다시 실행하면 남은 묶음만.",
         "> PC 가 계속 막히면 아래 주소를 브라우저로 — 화면 아래 '관련 검색어' ⤓(CSV) 또는 '시간 흐름' ⤓ (파일 이름 batch_NNN.csv 로 같은 폴더).", ""]
    (c.out / f"{name}.md").write_text("\n".join(L + lines) + "\n", encoding="utf-8")
    stamp("LIST", name=name, batches=len(spec["batches"]), kinds=kinds, out=f"{c.out.relative_to(c.dir.parent)}/{name}.json")


# ─────────── 1. PC 1회차 목록 ───────────
def cmd_discover_list(c: Cfg, a) -> int:
    batches, lines, n = [{"n": 0, "kind": "categories"}], ["## 분류 번호표 (batch_000)", "", "- 구글 트렌드 분류 전체 (이름·번호·하위 분류)", "", "## 분류만 — 관련 검색어", ""], 1
    for cid, name in c.categories:
        batches.append({"n": n, "kind": "related", "cat": cid, "words": [], "label": name})
        lines.append(f"{n:03d}. {name} (분류 {cid}) — {trends_url([], c.geo, cid, c.time, c.hl)}")
        n += 1
    lines += ["", "## 씨앗 낱말 — 관련 검색어 (5개씩)", ""]
    for i in range(0, len(c.seeds), c.seeds_per_batch):
        ws = c.seeds[i:i + c.seeds_per_batch]
        batches.append({"n": n, "kind": "related", "words": ws, "label": "씨앗"})
        lines.append(f"{n:03d}. {', '.join(ws)} — {trends_url(ws, c.geo, 0, c.time, c.hl)}")
        n += 1
    lines += ["", f"## 씨앗 낱말 — 유튜브 자동완성 (뒤에 붙일 말: {' · '.join(repr(s) for s in c.suffixes)})", ""]
    first = n
    for s in c.seeds:
        batches.append({"n": n, "kind": "suggest", "words": [s], "suffixes": c.suffixes, "hl": c.hl, "gl": c.geo.lower()})
        n += 1
    lines.append(f"{first:03d}~{n - 1:03d}. 씨앗 {len(c.seeds)}개 × {len(c.suffixes)} = 자동완성 {len(c.seeds) * len(c.suffixes)}번 (브라우저로는 못 받음 — PC 만)")
    spec = {"topic": c.topic, "set": "discover", "out_dir": f"{c.topic}/result/gap/discover", "geo": c.geo, "gprop": "youtube", "time": c.time, "hl": c.hl,
            "made": now_utc().isoformat(timespec="seconds"), "next": f"클라우드에서 python3 tools/gap_scan.py {c.topic} merge", "batches": batches}
    write_list(c, "discover", spec, "갭 탐색 PC 1회차 — 분류·씨앗 관련 검색어 + 자동완성 (한국 · 유튜브 검색 · 12개월)", lines)
    trend_n = sum(1 for b in batches if b.get("kind") != "suggest")
    stamp("DISCOVER_LIST", categories=len(c.categories), seeds=len(c.seeds), trends_batches=trend_n, suggest_batches=len(batches) - trend_n,
          est_minutes=round(trend_n * 45 / 60 + sum(len(b.get("words") or []) for b in batches if b.get("kind") == "related") * 6 / 60
                            + len(c.seeds) * len(c.suffixes) * 1.5 / 60))
    return 0


# ─────────── 2. 후보 낱말 ───────────
def read_batches(c: Cfg, folder: str) -> dict[int, object]:
    d = c.out / folder
    out = {}
    for f in sorted(d.glob("batch_*")):
        m = re.fullmatch(r"batch_(\d+)\.(json|csv)", f.name)
        if not m:
            continue
        try:
            out[int(m.group(1))] = json.loads(f.read_text("utf-8")) if m.group(2) == "json" else f.read_text("utf-8-sig")
        except (OSError, ValueError) as ex:
            stamp("LOAD", logging.WARNING, file=f.name, error=str(ex)[:80], next="그 묶음을 PC 에서 --force 로 다시")
    return out


def related_csv(text: str, keyword: str) -> dict:
    """화면 '관련 검색어' ⤓(CSV): 'TOP' 줄 아래 '말,값' … 빈 줄 … 'RISING' 줄 아래 '말,+250%|급증'. → 관련 검색어 JSON 과 같은 꼴."""
    out, cur = {"keyword": keyword, "top": [], "rising": []}, None
    for r in csv.reader(text.splitlines()):
        if not r or not r[0].strip():
            continue
        head = r[0].strip().upper()
        if head in ("TOP", "인기", "인기 검색어") and len(r) == 1:
            cur = "top"
            continue
        if head in ("RISING", "급상승", "급상승 검색어") and len(r) == 1:
            cur = "rising"
            continue
        if cur and len(r) >= 2:
            f = r[1].strip()
            v = 99999 if f.lower() in ("breakout", "급증") else int(re.sub(r"[^\d]", "", f) or 0)
            out[cur].append({"q": r[0].strip(), "v": v, "f": f})
    return out


def cmd_merge(c: Cfg, a) -> int:
    got = read_batches(c, "discover")
    spec = json.loads((c.out / "discover.json").read_text("utf-8")) if (c.out / "discover.json").exists() else {"batches": []}
    want = {b["n"]: b for b in spec["batches"]}
    missing = [n for n in want if n not in got]
    stamp("LOAD", files=len(got), planned=len(want), missing=len(missing), missing_first=missing[:10] or "-")
    cands: dict[str, dict] = {}

    def add(q, src, top_v=None, rising=None):
        k = norm(q)
        if not k or len(k) < 2:
            return
        x = cands.setdefault(k, {"q": q.strip(), "src": set(), "top_v": None, "rising": None, "suggest": 0})
        x["src"].add(src)
        if top_v is not None:
            x["top_v"] = max(x["top_v"] or 0, top_v)
        if rising is not None:
            x["rising"] = rising if x["rising"] is None else max(x["rising"], rising)

    cat_names, by_cat = {}, []
    for n, obj in sorted(got.items()):
        if isinstance(obj, str):                     # 브라우저로 받은 '관련 검색어' CSV (TOP / RISING 두 덩어리) — PC 가 막혔을 때
            b = want.get(n, {})
            obj = {"cat": b.get("cat", 0), "label": b.get("label", ""), "items": [related_csv(obj, ", ".join(b.get("words") or []))]}
        if not isinstance(obj, dict):
            continue
        if n == 0 and "children" in obj:
            def walk(node):
                cat_names[int(node.get("id", 0))] = node.get("name", "")
                for ch in node.get("children") or []:
                    walk(ch)
            walk(obj)
            continue
        if obj.get("kind") == "suggest":
            for q, sugg in (obj.get("results") or {}).items():
                for s in sugg:
                    add(s, "자동완성")
                    cands[norm(s)]["suggest"] += 1 if norm(s) in cands else 0
            continue
        for it in obj.get("items") or []:
            label = (f"분류:{obj.get('label') or cat_names.get(obj.get('cat'), obj.get('cat'))}" if not it.get("keyword") else f"씨앗:{it['keyword']}")
            for y in it.get("top") or []:
                add(y["q"], label, top_v=y.get("v"))
            for y in it.get("rising") or []:
                v = y.get("v")
                add(y["q"], label, rising=(99999 if str(y.get("f", "")).lower() in ("breakout", "급증") else v))
            if not it.get("keyword"):
                by_cat.append((label, it))
    for x in cands.values():
        x["cant"] = c.cant(x["q"])
        x["niche"] = c.niche_of(x["q"])
    rows = sorted(cands.values(), key=lambda x: (bool(x["cant"]), -len(x["src"]), -(x["top_v"] or 0), -(x["rising"] or 0), x["q"]))
    c.out.mkdir(parents=True, exist_ok=True)
    with open(c.out / "candidates.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["query", "sources", "n_sources", "top_value", "rising", "suggest_hits", "cant_make", "niche"])
        for x in rows:
            w.writerow([x["q"], " | ".join(sorted(x["src"])), len(x["src"]), x["top_v"] if x["top_v"] is not None else "",
                        "급증" if x["rising"] == 99999 else (x["rising"] if x["rising"] is not None else ""), x["suggest"], x["cant"], x["niche"]])
    keep = [x for x in rows if not x["cant"]]
    why = {}
    for x in rows:
        if x["cant"]:
            why[x["cant"]] = why.get(x["cant"], 0) + 1
    L = [f"# 갭 탐색 후보 낱말 — PC 1회차 결과 ({time.strftime('%Y-%m-%d %H:%M')})", "",
         f"> `tools/gap_scan.py {c.topic} merge` {VERSION} · 받은 묶음 {len(got)}/{len(want)} (못 받은 것 {len(missing)}) · 후보 {len(rows):,}개 · 뺌 {len(rows) - len(keep):,} · 남음 {len(keep):,}",
         "> '출처' = 그 말이 나온 곳 (분류:… = 그 분류의 관련 검색어 · 씨앗:… = 그 낱말의 관련 검색어 · 자동완성). '인기' = 그 목록 안 0~100 (목록끼리 비교 안 됨) · '급상승' = 오른 % (급증 = 5,000% 넘음).",
         "> 숫자는 아직 관심도가 아님 — 관심도는 PC 2회차(interest) 뒤 `demand.md`. 뺀 것은 지우지 않고 '뺌' 칸에 까닭 (new/gap.toml [[filter]]).", "",
         "## 1. 뺀 까닭 (지금 제작 방식으로 못 만들거나 채널 위험)", "", "| 까닭 | 낱말 수 |", "|---|---|"]
    L += [f"| {k} | {v:,} |" for k, v in sorted(why.items(), key=lambda kv: -kv[1])]
    L += ["", "## 2. 분류별 관련 검색어 (키워드 없이 분류만 — 그 분류에서 유튜브로 많이 찾는 말)", ""]
    for label, it in by_cat:
        L.append(f"- **{label[3:]}** 인기: " + (" · ".join(f"{y['q']}{'✗' if c.cant(y['q']) else ''}" for y in (it.get("top") or [])[:25]) or "—"))
        L.append("  급상승: " + (" · ".join(f"{y['q']}({y.get('f')}){'✗' if c.cant(y['q']) else ''}" for y in (it.get("rising") or [])[:25]) or "—"))
    L += ["", f"## 3. 남은 후보 (출처 많은 순 · 상위 {min(a.top_md, len(keep))}개 — 전체는 candidates.csv)", "", "| # | 낱말 | 출처 수 | 인기 | 급상승 | 출처 |", "|---|---|---|---|---|---|"]
    for i, x in enumerate(keep[: a.top_md], 1):
        L.append(f"| {i} | {x['q']} | {len(x['src'])} | {x['top_v'] if x['top_v'] is not None else ''} | {'급증' if x['rising'] == 99999 else (x['rising'] if x['rising'] is not None else '')} | {' · '.join(sorted(x['src']))[:90]} |")
    (c.out / "candidates.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    stamp("MERGE", candidates=len(rows), excluded=len(rows) - len(keep), kept=len(keep), by_reason=why, out="candidates.csv·candidates.md")
    return 0


# ─────────── 3. PC 2회차 목록 ───────────
def cmd_interest_list(c: Cfg, a) -> int:
    if not c.anchor or not c.words:
        raise SystemExit("[INTEREST] new/gap.toml [interest] ANCHOR·WORDS 가 비었음 — merge 를 읽고 Claude 가 채운다")
    words = [w for w in dict.fromkeys(c.words) if norm(w) != norm(c.anchor)]
    batches, lines, n = [], ["## 한국 관심도 (기준 낱말 + 4개씩)", ""], 1
    for i in range(0, len(words), 4):
        ws = [c.anchor] + words[i:i + 4]
        batches.append({"n": n, "kind": "timeseries", "words": ws, "geo": c.geo, "anchor": c.anchor})
        lines.append(f"{n:03d}. {', '.join(ws[1:])} — {trends_url(ws, c.geo, 0, c.time, c.hl)}")
        n += 1
    en = [x["en"] for x in c.niches if x["en"]]
    en = [w for w in dict.fromkeys(en) if norm(w) != norm(c.en_anchor)]
    if c.en_anchor and en:
        lines += ["", f"## 해외 겸용 — 전 세계 관심도 (기준 「{c.en_anchor}」 + 4개씩 · 나라 없음)", ""]
        for i in range(0, len(en), 4):
            ws = [c.en_anchor] + en[i:i + 4]
            batches.append({"n": n, "kind": "timeseries", "words": ws, "geo": "", "anchor": c.en_anchor})
            lines.append(f"{n:03d}. {', '.join(ws[1:])} — {trends_url(ws, '', 0, c.time, 'en')}")
            n += 1
        lines += ["", "## 해외 겸용 — 영어 자동완성 (미국 · 영어)", ""]
        batches.append({"n": n, "kind": "suggest", "words": en, "suffixes": c.en_suffixes, "hl": "en", "gl": "us"})
        lines.append(f"{n:03d}. 영어 낱말 {len(en)}개 × {len(c.en_suffixes)}")
    spec = {"topic": c.topic, "set": "interest", "out_dir": f"{c.topic}/result/gap/interest", "geo": c.geo, "gprop": "youtube", "time": c.time, "hl": c.hl,
            "anchor": c.anchor, "en_anchor": c.en_anchor, "made": now_utc().isoformat(timespec="seconds"),
            "next": f"클라우드에서 python3 tools/gap_scan.py {c.topic} trends", "batches": batches}
    write_list(c, "interest", spec, f"갭 탐색 PC 2회차 — 관심도 (한국 · 기준 「{c.anchor}」) + 해외 겸용", lines)
    stamp("INTEREST_LIST", words=len(words), kr_batches=math.ceil(len(words) / 4), en_words=len(en), batches=len(batches))
    return 0


# ─────────── 4. 관심도 ───────────
def trend_val(x: str) -> float:
    x = (x or "").strip()
    if x.startswith("<"):
        return 0.5
    try:
        return float(x)
    except ValueError:
        return 0.0


def parse_ts(text: str):
    rows = list(csv.reader(text.splitlines()))
    i = next((k for k, r in enumerate(rows) if r and re.match(r"^(주|Week|월|Month|날짜|Day)", r[0])), None)
    if i is None:
        return None, []
    data = [r for r in rows[i + 1:] if r and re.match(r"\d{4}-\d{2}", r[0])]
    return rows[i], data


def cmd_trends(c: Cfg, a) -> int:
    spec_p = c.out / "interest.json"
    if not spec_p.exists():
        raise SystemExit("[TRENDS] interest.json 없음 — interest-list 먼저")
    spec = json.loads(spec_p.read_text("utf-8"))
    got = read_batches(c, "interest")
    score, en_sugg, redo = {}, {}, []
    for b in spec["batches"]:
        obj = got.get(b["n"])
        if obj is None:
            stamp("TRENDS", logging.WARNING, batch=b["n"], msg="못 받음 — 빠짐", next="PC 에서 같은 명령 (남은 묶음만)")
            continue
        if b.get("kind") == "suggest":
            for q, s in (obj.get("results") or {}).items():
                en_sugg[q] = s
            continue
        hdr, data = parse_ts(obj)
        if not data or len(hdr) != len(b["words"]) + 1:
            stamp("TRENDS", logging.WARNING, batch=b["n"], msg=f"머리 줄·칸 수가 목록과 다름 ({len(hdr or []) - 1} vs {len(b['words'])}) — 빠짐")
            continue
        cols = [[trend_val(r[j + 1]) for r in data] for j in range(len(b["words"]))]
        base = st.mean(cols[0]) or 0.0
        big = max(st.mean(col) for col in cols)
        geo = "전 세계" if b.get("geo") == "" else (b.get("geo") or c.geo)
        stamp("TRENDS", batch=b["n"], geo=geo, weeks=len(data), first=data[0][0], last=data[-1][0], anchor=b["words"][0], anchor_mean=round(base, 1))
        for w, col in zip(b["words"][1:], cols[1:]):
            m = st.mean(col)
            last13, prev13 = col[-13:], col[-26:-13]
            rec = {"geo": geo, "rel": (m / base) if base else None, "recent_rel": (st.mean(last13) / base) if base else None,
                   "trend": (st.mean(last13) / st.mean(prev13)) if prev13 and st.mean(prev13) else None, "mean": m, "peak": max(col),
                   "spike": (max(col) / m) if m else None, "anchor_mean": base, "batch": b["n"],
                   "crushed": base < 10 and m < 5 and big >= 50}       # 같은 묶음에 아주 큰 낱말 → 기준·이 낱말이 다 작아져 거칠음
            if rec["crushed"]:
                redo.append(w)
            score[(geo, w)] = rec
    kr = {w: s for (g, w), s in score.items() if g != "전 세계"}
    ww = {w: s for (g, w), s in score.items() if g == "전 세계"}
    save_gz(c, "demand.json.gz", {"asof": now_utc().isoformat(timespec="seconds"), "anchor": spec.get("anchor"), "en_anchor": spec.get("en_anchor"),
                                  "kr": kr, "world": ww, "en_suggest": en_sugg, "redo": redo})
    L = [f"# 갭 탐색 — 유튜브 검색 관심도 (한국 · 12개월 · 기준 「{spec.get('anchor')}」 = 1.00)", "",
         f"> `tools/gap_scan.py {c.topic} trends` {VERSION} · {time.strftime('%Y-%m-%d %H:%M')} · 묶음 {len(got)}/{len(spec['batches'])} · 값 = 그 낱말 평균 ÷ 같은 묶음 기준 평균.",
         "> '최근 3개월 ÷ 그 전' 1 넘으면 오름 · '꼭짓점 배수' = 최고값 ÷ 평균 (4 넘으면 한때 튐 — 뉴스·계절) · ⚠ = 같은 묶음에 아주 큰 낱말이 있어 값이 거칢 (redo).",
         "> **한계**: 정확히 그 낱말을 친 검색만 — 홈 피드로 퍼지는 분야는 낮게 나옴 (공급 표의 하루 조회수와 같이 봄).", "",
         "| 순위 | 낱말 | 12개월 (기준 대비) | 최근 3개월 | 최근 3개월 ÷ 그 전 | 꼭짓점 배수 | 분야 | 뺌 |", "|---|---|---|---|---|---|---|---|"]
    for i, (w, s) in enumerate(sorted(kr.items(), key=lambda kv: -(kv[1]["rel"] or 0)), 1):
        L.append(f"| {i} | {w}{' ⚠' if s['crushed'] else ''} | {s['rel']:.3f} | {s['recent_rel']:.3f} | {s['trend'] or 0:.2f} | {s['spike'] or 0:.1f} | {c.niche_of(w)} | {c.cant(w)} |")
    if ww:
        L += ["", f"## 해외 겸용 — 전 세계 관심도 (기준 「{spec.get('en_anchor')}」)", "", "| 영어 낱말 | 12개월 (기준 대비) | 최근 3개월 ÷ 그 전 | 영어 자동완성 수 |", "|---|---|---|---|"]
        for w, s in sorted(ww.items(), key=lambda kv: -(kv[1]["rel"] or 0)):
            L.append(f"| {w} | {s['rel']:.3f} | {s['trend'] or 0:.2f} | {len(en_sugg.get(w, []))} |")
    (c.out / "demand.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    stamp("TRENDS", status="done", kr_words=len(kr), world_words=len(ww), crushed=len(redo), redo_first=redo[:8] or "-", out="demand.md")
    return 0


# ─────────── 5. 공급 (유튜브 API) ───────────
class Api:
    COST = {"search": 100}

    def __init__(self, key: str | None = None, opener=None):
        self.key = key if key is not None else os.environ.get("YOUTUBE_API_KEY", "")
        if not self.key:
            raise SystemExit("[API] YOUTUBE_API_KEY 없음 — '새 주제 탐색' 환경 세션에서 (값은 출력하지 않음)")
        self.units, self.open = 0, opener or (lambda url: urllib.request.urlopen(url, timeout=40))

    def get(self, ep: str, **params) -> dict:
        params["key"] = self.key
        cost = self.COST.get(ep, 1)
        url = API + ep + "?" + urllib.parse.urlencode(params)
        for attempt in range(4):
            try:
                with self.open(url) as r:
                    self.units += cost
                    return json.load(r)
            except urllib.error.HTTPError as e:
                self.units += cost
                body = e.read().decode("utf-8", "replace")
                reason = (re.search(r'"reason":\s*"([^"]+)"', body) or [None, "?"])[1]
                if reason in ("quotaExceeded", "dailyLimitExceeded"):
                    raise SystemExit(f"[API] 할당량 끝 ({ep}) — 태평양 자정 +10분(한국 17:10) 뒤 같은 명령 (지금까지 {self.units}단위 · 받은 것은 저장됨)")
                if e.code in (429, 500, 503) and attempt < 3:
                    time.sleep(2 ** attempt * 3)
                    continue
                raise SystemExit(f"[API] {ep} HTTP {e.code} {reason} — 입력 q={params.get('q', '-')} · 다음: 잠시 뒤 다시")
            except (urllib.error.URLError, TimeoutError) as e:
                if attempt < 3:
                    time.sleep(2 ** attempt * 3)
                    continue
                raise SystemExit(f"[API] {ep} 네트워크 실패 ({type(e).__name__}) — 프록시·인터넷 확인 뒤 다시")
        return {}


def check_short(vid: str, opener=None):
    """youtube.com/shorts/<id>: 쇼츠면 200, 아니면 /watch 로 돌려보냄 (분석기 check_is_short 와 같은 판정). 못 열면 None."""
    req = urllib.request.Request(f"https://www.youtube.com/shorts/{vid}", method="HEAD", headers={"User-Agent": "Mozilla/5.0"})

    class NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, *a, **k):
            return None
    try:
        op = opener or urllib.request.build_opener(NoRedirect)
        with op.open(req, timeout=10) as r:
            return r.status == 200
    except urllib.error.HTTPError as e:
        if e.code in (301, 302, 303, 307, 308):
            return False if "/watch" in (e.headers.get("Location") or "") else None
        return None
    except (urllib.error.URLError, TimeoutError, OSError):
        return None


def video_rec(it: dict) -> dict:
    sn, stt, cd = it.get("snippet", {}), it.get("statistics", {}), it.get("contentDetails", {})
    return {"id": it["id"], "title": sn.get("title", ""), "ch_id": sn.get("channelId", ""), "ch": sn.get("channelTitle", ""), "pub": sn.get("publishedAt", ""),
            "views": int(stt.get("viewCount", 0) or 0), "likes": int(stt.get("likeCount", 0) or 0), "comments": int(stt.get("commentCount", 0) or 0),
            "dur": iso_dur(cd.get("duration", "")), "live": sn.get("liveBroadcastContent", "none") != "none"}


def pick_words(c: Cfg, a) -> list[str]:
    if a.words:
        return a.words
    dem = load_gz(c, "demand.json.gz", {}) or {}
    kr = dem.get("kr") or {}
    if not kr:
        raise SystemExit("[SUPPLY] demand.json.gz 없음 — trends 먼저 (또는 --words 로 낱말을 직접)")
    ws = [w for w, s in sorted(kr.items(), key=lambda kv: -(kv[1].get("rel") or 0)) if not c.cant(w)]
    return ws[: a.top or c.top]


def cmd_supply(c: Cfg, a, api: Api | None = None, short_check=check_short) -> int:
    if os.environ.get("YOUTUBE_REFRESH_TOKEN") and not a.allow_upload_env:
        raise SystemExit("[SUPPLY] ❌ 이 환경은 업로드 키(YOUTUBE_REFRESH_TOKEN)가 있는 환경 — 업로드 할당량을 쓰지 않게 멈춤. "
                         "'새 주제 탐색' 환경 세션에서 실행 (정말 이 키로: --allow-upload-env)")
    words = pick_words(c, a)
    api = api or Api()
    cache = load_gz(c, "supply.json.gz", {}) or {}
    q_cache, chans, shorts = cache.get("queries", {}), cache.get("channels", {}), cache.get("is_short", {})
    after = (now_utc() - dt.timedelta(days=c.recent_days)).strftime("%Y-%m-%dT%H:%M:%SZ")
    todo = [w for w in words if w not in q_cache]
    stamp("SUPPLY", words=len(words), cached=len(words) - len(todo), todo=len(todo), est_units=len(todo) * 203, recent_after=after[:10])
    for w in todo:
        rec = {"asof": now_utc().isoformat(timespec="seconds")}
        for key, params in (("rel", dict(order="relevance")),
                            ("short", dict(order="viewCount", publishedAfter=after, videoDuration="short"))):
            j = api.get("search", part="snippet", q=w, type="video", regionCode="KR", relevanceLanguage="ko", maxResults=50, **params)
            ids = [it["id"]["videoId"] for it in j.get("items", []) if it.get("id", {}).get("videoId")]
            vs = api.get("videos", part="snippet,statistics,contentDetails", id=",".join(ids), maxResults=50).get("items", []) if ids else []
            rec[key] = {"total": (j.get("pageInfo") or {}).get("totalResults"), "videos": [video_rec(it) for it in vs]}
        need = sorted({v["ch_id"] for k in ("rel", "short") for v in rec[k]["videos"]} - set(chans))
        for i in range(0, len(need), 50):
            for it in api.get("channels", part="statistics", id=",".join(need[i:i + 50]), maxResults=50).get("items", []):
                s = it.get("statistics", {})
                chans[it["id"]] = {"subs": int(s.get("subscriberCount", 0) or 0), "hidden": bool(s.get("hiddenSubscriberCount"))}
        cand = [v["id"] for k in ("rel", "short") for v in rec[k]["videos"] if v["dur"] <= c.short_sec and v["id"] not in shorts]
        with cf.ThreadPoolExecutor(8) as ex:
            for vid, res in zip(cand, ex.map(short_check, cand)):
                shorts[vid] = res
        q_cache[w] = rec
        stamp("SUPPLY", q=w, rel=len(rec["rel"]["videos"]), short_search=len(rec["short"]["videos"]), total_rel=rec["rel"]["total"],
              shorts_checked=len(cand), shorts_unknown=sum(1 for v in cand if shorts.get(v) is None), units=api.units)
        save_gz(c, "supply.json.gz", {"asof": now_utc().isoformat(timespec="seconds"), "queries": q_cache, "channels": chans, "is_short": shorts})
    stamp("SUPPLY", status="done", words=len(words), units_this_run=api.units, out="supply.json.gz")
    return 0


# ─────────── 6. 갭 표 ───────────
def age_days(pub: str, now: dt.datetime) -> float:
    try:
        return max((now - dt.datetime.fromisoformat(pub.replace("Z", "+00:00"))).total_seconds() / 86400, 0.5)
    except ValueError:
        return float("nan")


def is_short_v(v, shorts, c):
    s = shorts.get(v["id"])
    return (v["dur"] <= 60) if s is None else (bool(s) and v["dur"] <= c.short_sec)


def success_long(v, subs, age, r):
    return (age <= r.get("MAX_AGE_DAYS", 180) and subs <= r.get("MAX_SUBS", 50000) and v["views"] >= r.get("MIN_VIEWS", 10000)
            and v["views"] >= max(subs, 100) * r.get("MIN_RATIO", 3.0) and v["dur"] >= r.get("MIN_MINUTES", 4.0) * 60)


def success_short(v, subs, age, r):
    ad = v["views"] >= r.get("AD_SUSPECT_MIN_VIEWS", 50000) and (v["likes"] / v["views"] if v["views"] else 0) < r.get("AD_SUSPECT_MAX_LIKE_RATE", 0.002)
    return (r.get("MIN_AGE_DAYS", 3) <= age <= r.get("MAX_AGE_DAYS", 180) and subs <= r.get("MAX_SUBS", 50000) and v["views"] >= r.get("MIN_VIEWS", 50000)
            and v["views"] >= max(subs, 100) * r.get("MIN_RATIO", 3.0) and not ad)


def metrics(c: Cfg, w: str, rec: dict, chans: dict, shorts: dict, now: dt.datetime) -> dict:
    def subs(v):
        return (chans.get(v["ch_id"]) or {}).get("subs", 0)
    rel = [v for v in rec["rel"]["videos"] if not v["live"]]
    lv = [v for v in rel if v["dur"] >= c.long_sec]
    for v in lv + rec["short"]["videos"]:
        v["_age"] = age_days(v["pub"], now)
    recent = [v for v in lv if v["_age"] <= c.recent_days]
    base_l = [v for v in recent if v["_age"] >= 7]
    sv = [v for v in rec["short"]["videos"] if not v["live"] and is_short_v(v, shorts, c)]
    m = {"word": w,
         "L_n": len(lv), "L_recent": len(recent), "L_old": sum(1 for v in lv if v["_age"] > c.old_days),
         "L_age_med": st.median([v["_age"] for v in lv]) if lv else None,
         "L_vpd_med": st.median([v["views"] / v["_age"] for v in lv]) if lv else None,
         "L_vpd_recent": st.median([v["views"] / v["_age"] for v in base_l]) if base_l else None,
         "L_succ": sum(1 for v in base_l if success_long(v, subs(v), v["_age"], c.succ_long)), "L_succ_base": len(base_l),
         "L_big": (sum(1 for v in lv if subs(v) >= c.big_subs) / len(lv)) if lv else None,
         "L_channels": len({v["ch_id"] for v in lv}), "total_rel": rec["rel"]["total"],
         "S_n": len(sv), "S_total": rec["short"]["total"],
         "S_vpd_med": st.median([v["views"] / v["_age"] for v in sv]) if sv else None,
         "S_succ": sum(1 for v in sv if success_short(v, subs(v), v["_age"], c.succ_short)), "S_succ_base": sum(1 for v in sv if 3 <= v["_age"] <= c.recent_days),
         "S_big": (sum(1 for v in sv if subs(v) >= c.big_subs) / len(sv)) if sv else None,
         "S_channels": len({v["ch_id"] for v in sv}),
         "top_long": sorted(lv, key=lambda v: -v["views"])[:2], "top_short": sorted(sv, key=lambda v: -v["views"])[:2]}
    m["L_succ_rate"] = m["L_succ"] / m["L_succ_base"] if m["L_succ_base"] else None
    m["S_succ_rate"] = m["S_succ"] / m["S_succ_base"] if m["S_succ_base"] else None
    return m


def score(rows: list[dict], demand: dict) -> None:
    """참고 점수 = (수요 백분위 + (100 − 공급 백분위) + 작은 채널 성공 백분위) ÷ 3 — 롱폼·쇼츠 따로. 줄 세우기용이지 규칙이 아님."""
    ix = {r["word"]: r for r in rows}
    tr = pct_rank({w: (demand.get(w) or {}).get("rel") for w in ix})
    for fmt_, vpd, sup, succ in (("L", "L_vpd_recent", "L_recent", "L_succ_rate"), ("S", "S_vpd_med", "S_n", "S_succ_rate")):
        pv = pct_rank({w: r[vpd] for w, r in ix.items()})
        ps = pct_rank({w: r[sup] for w, r in ix.items()})
        if fmt_ == "S":
            pt = pct_rank({w: (math.log10(r["S_total"]) if r["S_total"] else None) for w, r in ix.items()})
            ps = {w: mean_ok([ps[w], pt[w]]) for w in ix}
        pc = pct_rank({w: r[succ] for w, r in ix.items()})
        for w, r in ix.items():
            d = mean_ok([tr[w], pv[w]])
            r[f"{fmt_}_D"], r[f"{fmt_}_S"], r[f"{fmt_}_C"] = d, ps[w], pc[w]
            r[f"{fmt_}_score"] = mean_ok([d, (100 - ps[w]) if ps[w] is not None else None, pc[w]])


def cmd_report(c: Cfg, a) -> int:
    sup = load_gz(c, "supply.json.gz", {}) or {}
    dem = load_gz(c, "demand.json.gz", {}) or {}
    q, chans, shorts = sup.get("queries", {}), sup.get("channels", {}), sup.get("is_short", {})
    if not q:
        raise SystemExit("[REPORT] supply.json.gz 없음 — supply 먼저")
    now = dt.datetime.fromisoformat(sup.get("asof")) if sup.get("asof") else now_utc()
    kr, world, en_s = dem.get("kr") or {}, dem.get("world") or {}, dem.get("en_suggest") or {}
    rows = [metrics(c, w, rec, chans, shorts, now) for w, rec in q.items()]
    score(rows, kr)
    for r in rows:
        r["niche"], r["cant"] = c.niche_of(r["word"]), c.cant(r["word"])
        d = kr.get(r["word"]) or {}
        r["trend_rel"], r["trend_up"], r["spike"] = d.get("rel"), d.get("trend"), d.get("spike")
    nmeta = {n["name"]: n for n in c.niches}
    c.out.mkdir(parents=True, exist_ok=True)
    cols = ["word", "niche", "cant", "trend_rel", "trend_up", "spike", "L_score", "L_D", "L_S", "L_C", "L_n", "L_recent", "L_old", "L_age_med", "L_vpd_med",
            "L_vpd_recent", "L_succ", "L_succ_base", "L_succ_rate", "L_big", "L_channels", "total_rel", "S_score", "S_D", "S_S", "S_C", "S_n", "S_total",
            "S_vpd_med", "S_succ", "S_succ_base", "S_succ_rate", "S_big", "S_channels"]
    with open(c.out / "gap_scan.csv", "w", encoding="utf-8-sig", newline="") as f:
        wr = csv.writer(f)
        wr.writerow(cols)
        for r in sorted(rows, key=lambda r: -(r["L_score"] or 0)):
            wr.writerow([("" if r[k] is None else (round(r[k], 4) if isinstance(r[k], float) else r[k])) for k in cols])

    def p(x):
        return "—" if x is None else f"{x * 100:.0f}%"

    def s1(x):
        return "—" if x is None else f"{x:.0f}"

    L = [f"# 새 분야 갭 탐색 — 조회수는 잘 나오는데 영상은 적은 낱말 (한국 · 롱폼·쇼츠)", "",
         f"> `tools/gap_scan.py {c.topic} report` {VERSION} · {time.strftime('%Y-%m-%d %H:%M')} · 공급 자료 {sup.get('asof', '?')[:16]} · 낱말 {len(rows)}개 · 숫자만 — 판단은 `new/gap_ideas.md`.", "",
         "## 0. 읽는 법·한계 (먼저)", "",
         f"- **수요(D)** = 백분위 평균(구글 트렌드 12개월 관심도 · 하루 조회수 가운데값). 롱폼 하루 조회수 = 검색 상위 롱폼 중 7~{c.recent_days}일 영상 · 쇼츠 = 최근 {c.recent_days}일 쇼츠.",
         f"- **공급(S)** 롱폼 = 유튜브 검색(관련성 순) 상위 50개 중 4분 이상이면서 최근 {c.recent_days}일 영상 수 — 적으면 '검색해도 새 영상이 잘 안 나옴'. "
         f"쇼츠 = 최근 {c.recent_days}일 조회수 순 3분 이하 검색에서 쇼츠 수 + 검색 결과 수(유튜브 추정치) 백분위 평균.",
         "- **작은 채널(C)** = 성공 비율 (CLAUDE.md 성공 기준 — new/analysis_rules.toml [success]·[shorts]: 180일 안 · 구독자 5만 이하 · 조회수 ≥ 구독자×3 · 롱폼 1만+ / 쇼츠 5만+·좋아요 0.2% 미만 뺌) 백분위.",
         "- **참고 점수** = (D + (100 − S) + C) ÷ 3 — 이 표 안 줄 세우기용 (규칙이 아님). 광고 단가·제작 비용·경쟁 채널의 질은 들어 있지 않음.",
         "- 검색 상위 50개는 '그 낱말을 친 사람이 보는 것' — 분야 전체 영상 수가 아님. 낱말 하나가 분야를 다 대표하지 못함 → 분야 표(3번)와 같이 봄.",
         "- 트렌드는 정확히 그 낱말을 친 검색만 — 홈 피드로 퍼지는 분야(사연·수면 등)는 낮게 나옴. ⚡ = 한때 튄 낱말(꼭짓점 ÷ 평균 4 넘음 — 뉴스·계절).",
         "- 쇼츠 판정 = youtube.com/shorts 주소가 열림 (못 열면 60초 이하만). 구독자 수는 지금 값. 한국어 검색(regionCode KR · relevanceLanguage ko)만.", ""]
    for fmt_, title in (("L", "1. 롱폼 (4분 이상)"), ("S", "2. 쇼츠 (3분 이하)")):
        L += [f"## {title} — 참고 점수 순 (뺀 낱말 제외 · 상위 {a.top_md})", ""]
        if fmt_ == "L":
            L += ["| # | 낱말 | 분야 | 점수 | 관심도 (오름) | 하루 조회수 (최근 영상) | 상위 50 중 롱폼 · 최근 반년 · 2년 넘음 | 작은 채널 성공 | 큰 채널 몫 | 가장 많이 본 영상 |",
                  "|---|---|---|---|---|---|---|---|---|---|"]
        else:
            L += ["| # | 낱말 | 분야 | 점수 | 관심도 (오름) | 하루 조회수 (쇼츠) | 쇼츠 수 · 검색 결과 수 | 작은 채널 성공 | 큰 채널 몫 | 가장 많이 본 쇼츠 |", "|---|---|---|---|---|---|---|---|---|---|"]
        ok = sorted([r for r in rows if not r["cant"] and r[f"{fmt_}_score"] is not None], key=lambda r: -r[f"{fmt_}_score"])
        for i, r in enumerate(ok[: a.top_md], 1):
            tr = "—" if r["trend_rel"] is None else f"{r['trend_rel']:.2f} ({r['trend_up'] or 0:.2f}){' ⚡' if (r['spike'] or 0) > 4 else ''}"
            if fmt_ == "L":
                tv = " / ".join(f"「{v['title'][:28]}」 {fmt(v['views'])}·{v['ch'][:10]}" for v in r["top_long"][:1]) or "—"
                L.append(f"| {i} | {r['word']} | {r['niche'] or '—'} | {s1(r['L_score'])} | {tr} | {fmt(r['L_vpd_recent'])} | {r['L_n']} · {r['L_recent']} · {r['L_old']} | "
                         f"{r['L_succ']}/{r['L_succ_base']} ({p(r['L_succ_rate'])}) | {p(r['L_big'])} | {tv} |")
            else:
                tv = " / ".join(f"「{v['title'][:24]}」 {fmt(v['views'])}·{v['ch'][:10]}" for v in r["top_short"][:1]) or "—"
                L.append(f"| {i} | {r['word']} | {r['niche'] or '—'} | {s1(r['S_score'])} | {tr} | {fmt(r['S_vpd_med'])} | {r['S_n']} · {fmt(r['S_total'])} | "
                         f"{r['S_succ']}/{r['S_succ_base']} ({p(r['S_succ_rate'])}) | {p(r['S_big'])} | {tv} |")
        L.append("")
    by = {}
    for r in rows:
        if r["niche"] and not r["cant"]:
            by.setdefault(r["niche"], []).append(r)
    L += ["## 3. 분야 묶음 (new/gap.toml [[niche]] — 낱말 점수 가운데값 · make·global 은 판단)", "",
          "| 분야 | 낱말 수 | 롱폼 점수 | 쇼츠 점수 | 관심도 합 | 만들기(판단) | 해외 겸용(판단) | 전 세계 관심도 (영어) | 영어 자동완성 | 가장 좋은 낱말 (롱폼 · 쇼츠) |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    for name, rs in sorted(by.items(), key=lambda kv: -(mean_ok([st.median([x["L_score"] for x in kv[1] if x["L_score"] is not None] or [0]),
                                                                  st.median([x["S_score"] for x in kv[1] if x["S_score"] is not None] or [0])]) or 0)):
        n = nmeta.get(name, {})
        ls = [x["L_score"] for x in rs if x["L_score"] is not None]
        ss = [x["S_score"] for x in rs if x["S_score"] is not None]
        en = n.get("en", "")
        wv = (world.get(en) or {}).get("rel")
        es = sum(len(v) for k, v in en_s.items() if norm(k).startswith(norm(en))) if en else 0
        bl = max(rs, key=lambda x: x["L_score"] or 0)["word"]
        bs = max(rs, key=lambda x: x["S_score"] or 0)["word"]
        L.append(f"| {name} | {len(rs)} | {s1(st.median(ls)) if ls else '—'} | {s1(st.median(ss)) if ss else '—'} | {sum(x['trend_rel'] or 0 for x in rs):.2f} | "
                 f"{n.get('make', '') or '—'} | {n.get('global', '') or '—'} | {'—' if wv is None else f'{wv:.2f}'} ({en or '—'}) | {es or '—'} | {bl} · {bs} |")
    ex = [r for r in rows if r["cant"]]
    if ex:
        L += ["", f"## 4. 뺀 낱말 (숫자는 있음 — 못 만들거나 채널 위험) {len(ex)}개", "", " · ".join(f"{r['word']}({r['cant'][:10]})" for r in ex)]
    (c.out / "gap_scan.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    stamp("REPORT", words=len(rows), niches=len(by), excluded=len(ex),
          top_long="·".join(r["word"] for r in sorted([r for r in rows if not r["cant"]], key=lambda r: -(r["L_score"] or 0))[:5]),
          top_short="·".join(r["word"] for r in sorted([r for r in rows if not r["cant"]], key=lambda r: -(r["S_score"] or 0))[:5]), out="gap_scan.md·gap_scan.csv")
    return 0


# ─────────── selftest ───────────
def selftest() -> int:
    import tempfile
    import types
    ok = True

    def check(name, cond, **kv):
        nonlocal ok
        ok &= bool(cond)
        stamp("SELFTEST", result="✅" if cond else "❌", name=name, **kv)

    base = Path(tempfile.mkdtemp(prefix="gap_scan_selftest_"))
    t = base / "demo"
    t.mkdir()
    (t / "niches.toml").write_text('[[niche]]\nname="01. 건강"\nkeywords=["혈당"]\n', "utf-8")
    (t / "analysis_rules.toml").write_text("[success]\nMAX_AGE_DAYS=180\nMAX_SUBS=50000\nMIN_RATIO=3.0\nMIN_VIEWS=10000\nMIN_MINUTES=4.0\n"
                                           "[shorts]\nMAX_SECONDS=180\nMIN_AGE_DAYS=3\nMAX_AGE_DAYS=180\nMAX_SUBS=50000\nMIN_RATIO=3.0\nMIN_VIEWS=50000\n"
                                           "AD_SUSPECT_MIN_VIEWS=50000\nAD_SUSPECT_MAX_LIKE_RATE=0.002\n", "utf-8")
    (t / "gap.toml").write_text('GEO="KR"\n[discover]\nCATEGORIES=[[45,"건강"],[174,"과학"]]\nSEEDS_FROM_NICHES=true\nSEEDS=["공룡","혈당"]\nSEEDS_PER_BATCH=5\n'
                                'SUFFIXES=[""," 이유"]\n[[filter]]\nwhy="노래"\nrx="노래|가사"\n[interest]\nANCHOR=""\nWORDS=[]\n[global]\nEN_ANCHOR=""\n'
                                '[supply]\nTOP=10\n[[niche]]\nname="공룡"\nrx="공룡"\nmake="상"\nglobal="상"\nen="dinosaur"\n', "utf-8")
    c = Cfg("demo", base)
    check("씨앗 = niches.toml + SEEDS (겹침 하나)", c.seeds == ["혈당", "공룡"], seeds=c.seeds)
    a = types.SimpleNamespace(top_md=50, top=0, words=None, allow_upload_env=False)
    cmd_discover_list(c, a)
    spec = json.loads((c.out / "discover.json").read_text("utf-8"))
    kinds = [b.get("kind") for b in spec["batches"]]
    check("1회차 목록 = 분류표 1 · 분류 2 · 씨앗 관련 1 · 자동완성 2 · 폴더 gap/discover",
          kinds == ["categories", "related", "related", "related", "suggest", "suggest"] and spec["out_dir"] == "demo/result/gap/discover", kinds=kinds)
    d = c.out / "discover"
    d.mkdir()
    (d / "batch_000.json").write_text(json.dumps({"id": 0, "name": "모든 카테고리", "children": [{"id": 45, "name": "건강"}]}), "utf-8")
    (d / "batch_001.json").write_text(json.dumps({"cat": 45, "label": "건강", "items": [{"keyword": "", "top": [{"q": "혈당 낮추는 법", "v": 100}, {"q": "노래 가사", "v": 50}],
                                                                                       "rising": [{"q": "저속노화", "v": 99999, "f": "급증"}]}]}), "utf-8")
    (d / "batch_003.json").write_text(json.dumps({"words": ["혈당", "공룡"], "items": [{"keyword": "혈당", "top": [{"q": "혈당 낮추는 법", "v": 80}], "rising": []},
                                                                                     {"keyword": "공룡", "top": [{"q": "공룡 멸종", "v": 100}], "rising": [{"q": "공룡 화석", "v": 250, "f": "+250%"}]}]}), "utf-8")
    (d / "batch_004.json").write_text(json.dumps({"kind": "suggest", "results": {"혈당": ["혈당 낮추는 법", "혈당 스파이크"], "혈당 이유": []}}), "utf-8")
    (d / "batch_002.csv").write_text("카테고리: 과학\n\nTOP\n우주 끝,100\n블랙홀,40\n\nRISING\n우주 끝,급증\n화성 이주,+350%\n", "utf-8")
    cmd_merge(c, a)
    rows = {r["query"]: r for r in csv.DictReader(open(c.out / "candidates.csv", encoding="utf-8-sig"))}
    check("merge — 같은 말은 하나로 (출처 3곳) · 급증 표시 · 못 만드는 말 '뺌'",
          rows.get("혈당 낮추는 법", {}).get("n_sources") == "3" and rows.get("저속노화", {}).get("rising") == "급증" and rows.get("노래 가사", {}).get("cant_make") == "노래",
          n=len(rows))
    check("merge — 브라우저로 받은 관련 검색어 CSV 도 읽음 (분류:과학 · 급증 · +350%)",
          rows.get("우주 끝", {}).get("rising") == "급증" and rows.get("화성 이주", {}).get("rising") == "350" and "분류:과학" in rows.get("블랙홀", {}).get("sources", ""),
          got={k: rows.get(k, {}).get("sources") for k in ("우주 끝", "블랙홀")})
    raw = (t / "gap.toml").read_text("utf-8").replace('ANCHOR=""\nWORDS=[]', 'ANCHOR="공룡"\nWORDS=["혈당","저속노화","공룡 화석","혈당 스파이크","공룡 멸종"]').replace('EN_ANCHOR=""', 'EN_ANCHOR="science"')
    (t / "gap.toml").write_text(raw, "utf-8")
    c = Cfg("demo", base)
    cmd_interest_list(c, a)
    sp2 = json.loads((c.out / "interest.json").read_text("utf-8"))
    ts = [b for b in sp2["batches"] if b["kind"] == "timeseries"]
    check("2회차 목록 — 기준 낱말 + 4개씩 (5개 → 2묶음) · 전 세계 묶음 geo '' · 영어 자동완성",
          len([b for b in ts if b["geo"] == "KR"]) == 2 and ts[0]["words"][0] == "공룡" and any(b["geo"] == "" for b in ts)
          and sp2["batches"][-1]["kind"] == "suggest" and sp2["batches"][-1]["hl"] == "en", n=len(sp2["batches"]))
    idir = c.out / "interest"
    idir.mkdir()
    weeks = [(dt.date(2025, 11, 30) + dt.timedelta(weeks=i)).isoformat() for i in range(52)]

    def csvt(names, cols):
        return "카테고리: 모든 카테고리\n\n주," + ",".join(f"{n}: (대한민국)" for n in names) + "\n" + "\n".join(
            wk + "," + ",".join(str(col[i]) for col in cols) for i, wk in enumerate(weeks)) + "\n"
    (idir / "batch_001.csv").write_text(csvt(ts[0]["words"], [[50] * 52, [100] * 52, [5] * 39 + [15] * 13, ["<1"] * 52, [25] * 52]), "utf-8")
    (idir / "batch_002.csv").write_text(csvt(ts[1]["words"], [[50] * 52, [10] * 52]), "utf-8")
    (idir / "batch_003.csv").write_text(csvt(ts[2]["words"], [[40] * 52, [20] * 52]).replace("(대한민국)", "(전 세계)"), "utf-8")
    (idir / f"batch_{sp2['batches'][-1]['n']:03d}.json").write_text(json.dumps({"kind": "suggest", "results": {"dinosaur": ["dinosaur facts", "dinosaur song"]}}), "utf-8")
    cmd_trends(c, a)
    dem = load_gz(c, "demand.json.gz")
    kr = dem["kr"]
    check("trends — 기준 대비 (혈당 2.0 · '<1' = 0.5 → 0.01 · 오름 3배) · 전 세계 · 영어 자동완성",
          abs(kr["혈당"]["rel"] - 2.0) < 1e-9 and abs(kr["공룡 화석"]["rel"] - 0.01) < 1e-9 and abs(kr["저속노화"]["trend"] - 3.0) < 1e-9
          and abs(dem["world"]["dinosaur"]["rel"] - 0.5) < 1e-9 and dem["en_suggest"]["dinosaur"], kr={k: round(v["rel"], 3) for k, v in kr.items()})
    now = now_utc()

    def iso(days):
        return (now - dt.timedelta(days=days)).strftime("%Y-%m-%dT%H:%M:%SZ")

    import io

    class FakeResp(io.BytesIO):
        def __enter__(self):
            return self

        def __exit__(self, *x):
            return False

    calls = []

    def opener(url):
        qs = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)
        ep = url.split("/v3/")[1].split("?")[0]
        calls.append(ep)
        if ep == "search":
            short = qs.get("videoDuration", [""])[0] == "short"
            word = qs["q"][0]
            ids = [f"{word[:1]}{'S' if short else 'L'}{i:09d}"[:11] for i in range(4)]
            return FakeResp(json.dumps({"pageInfo": {"totalResults": 1000}, "items": [{"id": {"videoId": v}} for v in ids]}).encode())
        if ep == "videos":
            items = []
            for k, v in enumerate(qs["id"][0].split(",")):
                short = v[1] == "S"
                items.append({"id": v, "snippet": {"title": f"t{v}", "channelId": f"C{k}", "channelTitle": "ch", "publishedAt": iso(30 if k < 2 else 900),
                                                   "liveBroadcastContent": "none"},
                              "statistics": {"viewCount": str(300000 if short else 60000), "likeCount": "9000"},
                              "contentDetails": {"duration": "PT45S" if short else "PT12M"}})
            return FakeResp(json.dumps({"items": items}).encode())
        if ep == "channels":
            return FakeResp(json.dumps({"items": [{"id": i, "statistics": {"subscriberCount": "10000" if i == "C0" else "2000000"}} for i in qs["id"][0].split(",")]}).encode())
        return FakeResp(b"{}")
    os.environ.pop("YOUTUBE_REFRESH_TOKEN", None)
    a2 = types.SimpleNamespace(top_md=50, top=3, words=None, allow_upload_env=False)
    cmd_supply(c, a2, api=Api(key="fake", opener=opener), short_check=lambda v: v[1] == "S")
    sup = load_gz(c, "supply.json.gz")
    check("supply — 관심도 상위 3개 (뺀 말 제외) · 낱말마다 검색 2번 · 단위 기록", list(sup["queries"]) == ["혈당", "혈당 스파이크", "공룡 멸종"] and calls.count("search") == 6,
          words=list(sup["queries"]), searches=calls.count("search"))
    n_before = calls.count("search")
    cmd_supply(c, a2, api=Api(key="fake", opener=opener), short_check=lambda v: v[1] == "S")
    check("supply — 다시 실행하면 받은 낱말은 건너뜀 (할당량 0)", calls.count("search") == n_before)
    os.environ["YOUTUBE_REFRESH_TOKEN"] = "fake"
    try:
        cmd_supply(c, a2, api=Api(key="fake", opener=opener))
        check("supply — 업로드 키 환경이면 멈춤", False)
    except SystemExit:
        check("supply — 업로드 키 환경이면 멈춤", True)
    os.environ.pop("YOUTUBE_REFRESH_TOKEN", None)
    cmd_report(c, a)
    gcsv = list(csv.DictReader(open(c.out / "gap_scan.csv", encoding="utf-8-sig")))
    r0 = next(r for r in gcsv if r["word"] == "혈당")
    check("report — 롱폼: 최근 반년 2 · 2년 넘음 2 · 작은 채널 성공 1/2 (C0 구독 1만·조회 6만) · 큰 채널 몫 75% (C1~C3 200만)",
          r0["L_recent"] == "2" and r0["L_old"] == "2" and r0["L_succ"] == "1" and r0["L_succ_base"] == "2" and abs(float(r0["L_big"]) - 0.75) < 1e-9, row={k: r0[k] for k in ("L_n", "L_recent", "L_old", "L_succ", "L_big")})
    check("report — 쇼츠: 4개 중 작은 채널 성공 1 (180일 안 2개만 셈) · 점수 칸 있음",
          r0["S_n"] == "4" and r0["S_succ"] == "1" and r0["S_succ_base"] == "2" and r0["S_score"] != "" and r0["L_score"] != "", row={k: r0[k] for k in ("S_n", "S_succ", "S_succ_base", "S_score")})
    md = (c.out / "gap_scan.md").read_text("utf-8")
    check("report — 표 3개 (롱폼·쇼츠·분야) · 0번 한계 먼저", "## 0. 읽는 법·한계" in md and "## 1. 롱폼" in md and "## 2. 쇼츠" in md and "## 3. 분야 묶음" in md)
    check("백분위 — 같은 값은 같은 순위", pct_rank({"a": 1, "b": 1, "c": 3}) == {"a": 25.0, "b": 25.0, "c": 100.0}, got=pct_rank({"a": 1, "b": 1, "c": 3}))
    stamp("SELFTEST", result="✅ 모두 통과" if ok else "❌ 실패 있음")
    return 0 if ok else 1


CMDS = {"discover-list": cmd_discover_list, "merge": cmd_merge, "interest-list": cmd_interest_list, "trends": cmd_trends, "supply": cmd_supply, "report": cmd_report}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="새 분야 갭 탐색 (수요 ÷ 공급 · 롱폼·쇼츠)")
    ap.add_argument("topic", help="주제 폴더 (new) 또는 selftest")
    ap.add_argument("cmd", nargs="?", choices=list(CMDS))
    ap.add_argument("--top", type=int, default=0, help="supply: 관심도 상위 몇 낱말 (0 = gap.toml [supply] TOP)")
    ap.add_argument("--words", nargs="+", help="supply: 낱말을 직접")
    ap.add_argument("--top-md", type=int, default=120, help="merge·report: .md 표에 몇 줄")
    ap.add_argument("--allow-upload-env", action="store_true", help="supply: 업로드 키 환경에서도 (할당량 주의)")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args(argv)
    logging.basicConfig(level=a.log_level, format="%(message)s")
    if a.topic == "selftest":
        return selftest()
    if not a.cmd:
        ap.error("명령이 필요함 (discover-list · merge · interest-list · trends · supply · report)")
    t0 = time.time()
    c = Cfg(a.topic)
    rc = CMDS[a.cmd](c, a)
    stamp("DONE", topic=a.topic, cmd=a.cmd, seconds=round(time.time() - t0, 1))
    return rc


if __name__ == "__main__":
    sys.exit(main())
