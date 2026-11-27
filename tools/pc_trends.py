#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.3.1 — 2026-11-28 — watch 오류 고침 (사용자 PC 2026-11-28 "에러나는데 해결해"): 판 검색어를 못 읽었을 때 경고 로그가 log() 의 첫 인자 이름
#          stage 와 겹쳐 TypeError 로 죽던 것 → step= · --list-file 이 없으면 처음에 찾은 절대 경로와 함께 바로 멈춤 (예전: 경고 뒤 '다음 회차에 다시' — 파일은 안 생김).
# 이전 v1.3 — 2026-11-27 — watch: 제작 판 검색어(GitHub studio/state/trends.json)를 간격마다 읽어 받고 올림 — 사용자 지시 2026-11-27
#          "피시에서는 일정 간격으로 단어 가져와서 결과 업로드, 결과도 볼 수 있음". 결과 폴더 <주제>/result/next_topic/board_<기간>/ (기간 = 간격으로 나눈 날짜·시각),
#          파일 이름에 낱말 묶음 지문(batch_NNN_<6자>.csv|json) — 같은 기간에 검색어를 바꾸면 새 파일. 전체 탐색 = new 주제 폴더(분류만 관련 검색어).
# 이전 v1.2 — 2026-11-25 — 새 분야 갭 탐색용 (사용자 지시 2026-11-25 "여기서 다루고 있는 주제 이외에도 조회수 잘나오고 영상은 별로 없을 것 같은
#          주제 모두 찾아서 해야 돼" · "롱폼, 쇼츠 둘다하고 못만드는 분야는 알아서 해 … 계속 진행해"):
#          ① 묶음 종류 kind — timeseries(지금까지 · CSV) · related(관련 검색어 인기·급상승 — 키워드 없이 분류만도) · categories(분류 번호표) ·
#             suggest(유튜브 자동완성 — 클라우드는 이 환경 프록시가 막아서 집 인터넷에서) → related·categories·suggest 는 JSON
#          ② 목록 파일의 geo·time·gprop·hl 을 씀 (v1.1 은 늘 한국·12개월 — 목록에 다른 나라를 적어도 무시하던 것) · 묶음마다 cat(분류)
#          ③ 목록마다 폴더 out_dir (<주제>/result/(next_topic|gap)/<이름>/batch_NNN.csv|json) — 같은 batch_01 이름이 옛 결과와 겹쳐
#             '이미 있음'으로 건너뛰던 위험을 없앰 · out_dir 이 없는 옛 목록은 그대로 <주제>/result/next_topic/trends/batch_NN.csv
#          ④ 429 가 계속되면 그 주소(트렌드 / 자동완성) 묶음만 그만 — 다른 주소 묶음은 이어서 받음
#          ⑤ --list <이름|경로> (기본 = 옛 경로 <주제>/result/next_topic/trends_batches.json · 이름만 주면 <주제>/result/gap/<이름>.json)
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.3.1 | 2026-11-28 | watch 경고 로그 TypeError(stage 겹침 → step) · --list-file 없으면 경로와 함께 바로 멈춤 · selftest 2개 더 | cmd_watch · selftest |
# | v1.3 | 2026-11-27 | watch(--every 분 · --once) · board_specs · period_of · 지문 파일 이름(hash_names) · selftest 4개 더 | board_specs · period_of · batch_path · allowed_trends · cmd_watch · selftest |
# | v1.2 | 2026-11-25 | kind(related·categories·suggest) · 목록 geo/time/gprop/hl · out_dir · --list · 종류별 쉼 · 429 는 막힌 주소 묶음만 그만(자동완성은 이어서) · selftest 9개 더 | Trends.explore·related·categories·suggest · batch_path · allowed_trends · fetch · run_topic · cmd_run · selftest |
# | v1.1 | 2026-11-25 | ensure_requests (requests 만 설치) · github_token (분석기와 같은 순서로 .env 직접 읽기 — 분석기 import 뺌) · selftest 2개 더 | ensure_requests · github_token · cmd_run · selftest |
# | v1.0 | 2026-11-25 | 최초 — run(묶음 목록 trends_batches.json → 묶음마다 explore → 시간 흐름 위젯 CSV → GitHub) · selftest(가짜 구글·가짜 GitHub) | Trends · run_topic · selftest |
"""구글 트렌드 묶음 받기 — 목록은 클라우드(tools/next_topic.py · tools/gap_scan.py)가 정하고, 받기·올리기는 PC 에서.

왜 PC: 구글 트렌드는 공식 공개 API 가 없고, 화면이 쓰는 내부 주소를 자동으로 부르면 서버(데이터센터) 주소는 첫 요청부터 HTTP 429
       (2026-11-25 클라우드에서 허용 목록에 넣은 뒤 시험 — 화면 주소도 429). 집 인터넷은 사람이 쓰는 주소라 천천히 부르면 대개 받힘.

  PC(사용자)  powershell -ExecutionPolicy Bypass -File run_analyzer.ps1 -Trends -Folder history                  (옛 목록)
              powershell -ExecutionPolicy Bypass -File run_analyzer.ps1 -Trends -Folder new --list discover      (갭 탐색 1회차 · v1.2)
              (= .venv\\Scripts\\python.exe tools/pc_trends.py run <주제> [--list …] · 시험 삼아: … --limit 3 · 받기만: … --no-push)
  시험        python3 tools/pc_trends.py selftest      (가짜 구글·가짜 GitHub — 진짜로 부르거나 올리지 않음)

묶음 종류 (목록 파일 batches[].kind — 없으면 timeseries):
  timeseries  ① 첫 화면(쿠키) → ② /trends/api/explore → 'TIMESERIES' 위젯 → ③ /widgetdata/multiline/csv = 화면 ⤓(CSV) → batch_NNN.csv
  related     ② explore (낱말 1~5개 또는 키워드 없이 분류 cat 만) → 'RELATED_QUERIES' 위젯마다 /widgetdata/relatedsearches → 인기 25·급상승 25 → .json
  categories  /trends/api/explore/pickers/category (분류 번호표 전체) → .json
  suggest     suggestqueries.google.com (ds=yt) — 낱말 × 뒤에 붙일 말(suffixes) 마다 자동완성 최대 10개 → .json
쉬기: 트렌드 묶음 사이 30~60초 (--pause) · 한 묶음 안 관련 검색어 위젯 사이 4~8초 · 자동완성 사이 1~2초 · 429 면 1·2·4분 쉬고 다시,
      그래도 429 면 받은 것까지 올리고 멈춤 (몇 시간 뒤 다시 실행하면 남은 묶음만).
올리기: GitHub API 로 목록이 정한 폴더의 batch 파일만 (다른 경로는 코드가 거부) · 이미 GitHub 에 있는 묶음은 건너뜀 (--force 면 다시).
※ 연구·교육용 — 구글 트렌드 값은 0~100 상대값 (검색 수가 아님).
"""
import argparse
import importlib.util
import json
import logging
import os
import random
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import pc_transcribe as pt  # noqa: E402  GitHub 올리기·로그·주제 이름 검사를 그대로

VERSION = "v1.3.1"
BOARD_STATE = "studio/state/trends.json"   # v1.3 제작 판 검색어 (Claude 가 판 동기화 때 씀)
LOG = logging.getLogger("pc_trends")
TRENDS = "https://trends.google.com"
SUGGEST = "https://suggestqueries.google.com/complete/search"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/124.0 Safari/537.36")
BACKOFF = (60, 120, 240)          # 429 면 이만큼 쉬고 다시 (초)
INNER_PAUSE = 4.0                 # v1.2: 한 묶음 안 관련 검색어 위젯 사이 4~8초
SUGGEST_PAUSE = 1.0               # v1.2: 자동완성 사이 1~2초 (구글 트렌드 주소가 아님)
KINDS = ("timeseries", "related", "categories", "suggest")


def log(stage, level=logging.INFO, **kv):
    LOG.log(level, "[%s] [%s] %s", stage, time.strftime("%Y-%m-%dT%H:%M:%S"), " ".join(f"{k}={v}" for k, v in kv.items()))


def trends_path(topic, n):
    """옛 목록(out_dir 없음)의 경로 — v1.1 과 같음."""
    return f"{topic}/result/next_topic/trends/batch_{n:02d}.csv"


def out_dir_ok(topic, out_dir):
    """목록이 정한 폴더가 이 주제 결과 폴더 안인지 (v1.2) — <주제>/result/next_topic|gap/<영문 소문자·숫자·_>."""
    return bool(re.fullmatch(rf"{re.escape(topic)}/result/(?:next_topic|gap)/[a-z0-9_]+", out_dir or ""))


def batch_path(topic, spec, b):
    """묶음 b 를 올릴 경로. out_dir 이 있으면 <out_dir>/batch_NNN.(csv|json), 없으면 옛 경로."""
    out = (spec or {}).get("out_dir")
    if not out:
        return trends_path(topic, b["n"])
    ext = "csv" if b.get("kind", "timeseries") == "timeseries" else "json"
    if (spec or {}).get("hash_names") and re.fullmatch(r"[0-9a-f]{6}", str(b.get("hash", ""))):      # v1.3 제작 판 묶음 — 낱말 지문
        return f"{out}/batch_{int(b['n']):03d}_{b['hash']}.{ext}"
    return f"{out}/batch_{int(b['n']):03d}.{ext}"


def allowed_trends(topic):
    """올려도 되는 경로 — 이 주제 트렌드 묶음 파일만 (옛 next_topic/trends/batch_NN.csv + v1.2 목록 폴더 batch_NNN.csv|json)."""
    t = re.escape(topic)
    return re.compile(rf"^{t}/result/(?:next_topic/trends/batch_\d{{2}}\.csv|(?:next_topic|gap)/[a-z0-9_]+/batch_\d{{3}}(?:_[0-9a-f]{{6}})?\.(?:csv|json))$")


class Blocked(Exception):
    """구글이 계속 429 — 오늘은 여기까지."""


def keyword_of(req):
    """관련 검색어 위젯 request 에 든 낱말 (키워드 없이 분류만이면 '')."""
    try:
        return req["restriction"]["complexKeywordsRestriction"]["keyword"][0]["value"]
    except (KeyError, IndexError, TypeError):
        return ""


class Trends:
    """구글 트렌드 화면이 부르는 주소를 차례로 (세션 쿠키 유지 · 천천히)."""

    def __init__(self, session, sleep=time.sleep, hl="ko", tz=-540, rnd=random.random):
        self.s, self.sleep, self.hl, self.tz, self.rnd = session, sleep, hl, tz, rnd
        self.s.headers.update({"User-Agent": UA, "Accept-Language": "ko-KR,ko;q=0.9,en;q=0.6"})
        self.warmed = False

    def _get(self, url, **params):
        for i, wait in enumerate((0,) + BACKOFF):
            if wait:
                log("WAIT", level=logging.WARNING, why="HTTP 429 — 구글이 잠시 막음", seconds=wait, try_=i + 1)
                self.sleep(wait)
            r = self.s.get(url, params=params or None, timeout=60)
            if r.status_code == 429:
                continue
            if r.status_code != 200:
                raise RuntimeError(f"HTTP {r.status_code} {url.split('?')[0]} — {(r.text or '')[:120]}")
            return r
        raise Blocked(f"HTTP 429 가 {len(BACKOFF) + 1}번 — 구글이 이 주소를 막음 (몇 시간 뒤 다시, 또는 목록 .md 의 주소를 브라우저로)")

    def warm(self):
        if not self.warmed:
            self._get(f"{TRENDS}/trends/explore", geo="KR", hl=self.hl)      # 쿠키 (NID)
            self.warmed = True

    @staticmethod
    def _json(text):
        """앞에 붙는 )]}' 를 떼고 JSON."""
        i = text.find("{")
        if i < 0:
            raise RuntimeError(f"JSON 아님: {text[:80]!r}")
        return json.loads(text[i:])

    def explore(self, words, cat=0, geo="KR", time_="today 12-m", gprop="youtube"):
        """v1.2: 화면 첫 요청. words 가 비면(또는 [""]) 키워드 없이 분류만 (cat)."""
        self.warm()
        items = [{"keyword": w, "geo": geo, "time": time_} for w in (words or [""])]
        req = {"comparisonItem": items, "category": int(cat or 0), "property": gprop}
        r = self._get(f"{TRENDS}/trends/api/explore", hl=self.hl, tz=self.tz, req=json.dumps(req, ensure_ascii=False))
        return self._json(r.text).get("widgets") or []

    def csv(self, words, cat=0, geo="KR", time_="today 12-m", gprop="youtube"):
        widgets = self.explore(words, cat, geo, time_, gprop)
        ts = next((w for w in widgets if w.get("id") == "TIMESERIES"), None)
        if not ts:
            raise RuntimeError(f"시간 흐름 위젯 없음 (위젯 {[w.get('id') for w in widgets]})")
        r = self._get(f"{TRENDS}/trends/api/widgetdata/multiline/csv", req=json.dumps(ts["request"], ensure_ascii=False),
                      token=ts["token"], tz=self.tz, hl=self.hl)
        text = r.content.decode("utf-8-sig", "replace")
        if not re.search(r"^(주|Week|월|Month|날짜|Day)", text, re.M):
            raise RuntimeError(f"CSV 머리 줄(주,…)이 없음: {text[:120]!r}")
        return text

    def related(self, words, cat=0, geo="KR", time_="today 12-m", gprop="youtube"):
        """v1.2: 관련 검색어 — 낱말(또는 분류)마다 인기(top) 25 · 급상승(rising) 25. value = 인기는 0~100, 급상승은 오른 % (급증 = 'Breakout')."""
        widgets = self.explore(words, cat, geo, time_, gprop)
        rq = [w for w in widgets if str(w.get("id", "")).startswith("RELATED_QUERIES")]
        if not rq:
            raise RuntimeError(f"관련 검색어 위젯 없음 (위젯 {[w.get('id') for w in widgets]})")
        out = []
        for i, w in enumerate(rq):
            if i:
                self.sleep(INNER_PAUSE * (1 + self.rnd()))
            r = self._get(f"{TRENDS}/trends/api/widgetdata/relatedsearches", req=json.dumps(w["request"], ensure_ascii=False),
                          token=w["token"], tz=self.tz, hl=self.hl)
            lists = (self._json(r.text).get("default") or {}).get("rankedList") or []

            def items(k):
                if len(lists) <= k:
                    return []
                return [{"q": x.get("query"), "v": x.get("value"), "f": x.get("formattedValue")} for x in (lists[k].get("rankedKeyword") or [])]

            kw = keyword_of(w.get("request") or {}) or ((words or [""])[i] if i < len(words or [""]) else "")
            out.append({"keyword": kw, "top": items(0), "rising": items(1)})
        return {"cat": int(cat or 0), "geo": geo, "time": time_, "gprop": gprop, "words": list(words or []), "items": out}

    def categories(self):
        """v1.2: 분류 번호표 전체 (이름·id·하위 분류)."""
        self.warm()
        r = self._get(f"{TRENDS}/trends/api/explore/pickers/category", hl=self.hl, tz=self.tz)
        return self._json(r.text)

    def suggest(self, q, hl="ko", gl="kr"):
        """v1.2: 유튜브 자동완성 (검색창에 q 를 치면 뜨는 말, 최대 10개)."""
        r = self._get(SUGGEST, client="firefox", ds="yt", hl=hl, gl=gl, q=q)
        j = json.loads(r.text)
        return [s for s in (j[1] if len(j) > 1 else []) if isinstance(s, str)]


def fetch(tr, b, spec, sleep=time.sleep, rnd=random.random):
    """묶음 하나 받기 → (올릴 글, 로그 칸). 묶음 값이 목록 값보다 먼저 (geo·time·gprop·hl)."""
    kind = b.get("kind", "timeseries")
    if kind not in KINDS:
        raise RuntimeError(f"모르는 묶음 종류 {kind!r} (되는 것: {', '.join(KINDS)})")
    geo = b.get("geo", spec.get("geo", "KR"))
    time_ = b.get("time", spec.get("time", "today 12-m"))
    gprop = b.get("gprop", spec.get("gprop", "youtube"))
    cat = b.get("cat", 0)
    if kind == "timeseries":
        text = tr.csv(b["words"], cat=cat, geo=geo, time_=time_, gprop=gprop)
        return text, {"weeks": sum(1 for ln in text.splitlines() if re.match(r"\d{4}-\d{2}", ln)), "geo": geo or "전 세계"}
    if kind == "related":
        res = tr.related(b.get("words") or [], cat=cat, geo=geo, time_=time_, gprop=gprop)
        res["label"] = b.get("label", "")
        top = sum(len(x["top"]) for x in res["items"])
        rising = [y["q"] for x in res["items"] for y in x["rising"]][:3]
        return json.dumps(res, ensure_ascii=False, indent=1), {"cat": cat, "label": b.get("label", "") or "-", "top": top,
                                                               "rising": sum(len(x["rising"]) for x in res["items"]), "rising_first": "·".join(rising) or "-"}
    if kind == "categories":
        res = tr.categories()
        return json.dumps(res, ensure_ascii=False, indent=1), {"top_level": len(res.get("children") or [])}
    # suggest
    hl, gl = b.get("hl", spec.get("hl", "ko")), b.get("gl", spec.get("gl", "kr"))
    out = {}
    for i, sfx in enumerate(b.get("suffixes") or [""]):
        for w in b.get("words") or []:
            if out:
                sleep(SUGGEST_PAUSE * (1 + rnd()))
            q = (w + sfx).strip()
            out[q] = tr.suggest(q, hl=hl, gl=gl)
    res = {"kind": "suggest", "hl": hl, "gl": gl, "words": b.get("words") or [], "suffixes": b.get("suffixes") or [""], "results": out}
    return json.dumps(res, ensure_ascii=False, indent=1), {"queries": len(out), "with_suggestions": sum(1 for v in out.values() if v), "hl": hl}


def ensure_requests(install=True, run=subprocess.run):
    """PC 가상환경에 requests 가 없으면 그것만 설치 (분석기 전체 패키지는 필요 없음 — v1.1)."""
    if importlib.util.find_spec("requests") is not None:
        return True
    if not install:
        raise SystemExit("[SETUP] ❌ requests 패키지가 없음 → python -m pip install -U requests")
    log("SETUP", note="requests 설치 (처음 한 번, 몇 초)")
    if run([sys.executable, "-m", "pip", "install", "-U", "requests"]).returncode != 0:
        raise SystemExit("[SETUP] ❌ requests 설치 실패 → 위 오류 확인 (가상환경 .venv — run_analyzer.ps1 이 만듦)")
    importlib.invalidate_caches()
    return True


def _env_file(path):
    """KEY=VALUE .env 읽기 (메모장 BOM·따옴표 허용) — 분석기 load_env_file 과 같은 꼴. 값은 출력하지 않음."""
    vals = {}
    try:
        text = Path(path).read_text("utf-8-sig")
    except OSError:
        return vals
    for line in text.splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            vals[k.strip()] = v.strip().strip('"').strip("'")
    return vals


def github_token(topic, root=ROOT, environ=None):
    """GITHUB_TOKEN — 분석기 key_sources 와 같은 순서: <주제>/.env → 환경 변수 GITHUB_TOKEN_<주제> → 맨 위 .env → 환경 변수. → (값, 어디서)."""
    environ = os.environ if environ is None else environ
    tag = re.sub(r"[^0-9A-Za-z가-힣]+", "_", topic).strip("_").upper()
    for name, get in ((f"{topic}/.env", lambda: _env_file(Path(root) / topic / ".env").get("GITHUB_TOKEN", "")),
                      (f"env:GITHUB_TOKEN_{tag}", lambda: environ.get(f"GITHUB_TOKEN_{tag}", "")),
                      (".env", lambda: _env_file(Path(root) / ".env").get("GITHUB_TOKEN", "")),
                      ("env", lambda: environ.get("GITHUB_TOKEN", ""))):
        v = (get() or "").strip()
        if v:
            return v, name
    return "", "-"


def exists_on_github(gh, path):
    r = gh.req("GET", f"/contents/{path}", params={"ref": gh.branch}, ok=(200, 404))
    return r.status_code == 200


def run_topic(topic, batches, tr, gh, work, opts, sleep=time.sleep, rnd=random.random, spec=None):
    """묶음마다 받기 → work 에 저장 → GitHub (gh 가 있으면). 돌려줌: {'got': [...], 'skipped': [...], 'failed': [...], 'blocked': bool}."""
    spec = spec or {}
    out = {"got": [], "skipped": [], "failed": [], "blocked": False, "pushed": 0}
    work.mkdir(parents=True, exist_ok=True)
    todo = []
    for b in batches:
        p = batch_path(topic, spec, b)
        if not opts.force and ((work / Path(p).name).is_file() and not gh or (gh and exists_on_github(gh, p))):
            out["skipped"].append(b["n"])
            continue
        todo.append(b)
    if opts.limit:
        todo = todo[: opts.limit]
    log("RUN", topic=topic, batches=len(batches), this_run=len(todo), skipped=len(out["skipped"]), push=bool(gh),
        pause=f"{opts.pause}~{opts.pause * 2}s", out_dir=spec.get("out_dir") or "next_topic/trends",
        kinds="·".join(f"{k}{sum(1 for b in todo if b.get('kind', 'timeseries') == k)}" for k in KINDS if any(b.get("kind", "timeseries") == k for b in todo)) or "-")
    pending, weight, tried, blocked_hosts = {}, 0.0, 0, set()
    for b in todo:
        kind = b.get("kind", "timeseries")
        host = "suggest" if kind == "suggest" else "trends"   # v1.2: 트렌드가 막혀도 자동완성(다른 주소)은 이어서
        if host in blocked_hosts:
            continue
        if tried:
            if kind == "suggest":                       # 자동완성은 트렌드 주소가 아님 — 짧게
                wait = SUGGEST_PAUSE * (1 + rnd())
            else:
                wait = opts.pause * (1 + rnd())          # 묶음 사이 pause~2×pause 초 (사람처럼 — 고르게 치지 않게)
                log("PAUSE", seconds=round(wait))
            sleep(wait)
        tried += 1
        try:
            text, info = fetch(tr, b, spec, sleep=sleep, rnd=rnd)
        except Blocked as e:
            log("BLOCKED", level=logging.WARNING, batch=b["n"], kind=kind, host=host, why=str(e),
                note="이 주소 묶음은 이번 실행에서 그만 · 다른 주소 묶음은 이어서")
            out["blocked"] = True
            blocked_hosts.add(host)
            continue
        except Exception as e:                          # 한 묶음 실패는 기록하고 다음 묶음
            log("BATCH", level=logging.WARNING, batch=b["n"], kind=kind, words="·".join(b.get("words") or []) or f"cat={b.get('cat', 0)}",
                error=f"{type(e).__name__}: {str(e)[:160]}", next="다시 실행하면 이 묶음만 다시 · 계속 실패면 목록 .md 의 주소를 브라우저로")
            out["failed"].append(b["n"])
            continue
        path = batch_path(topic, spec, b)
        f = work / Path(path).name
        f.write_text(text, encoding="utf-8")
        log("BATCH", batch=b["n"], kind=kind, words="·".join(b.get("words") or []) or "-", **info, saved=f.name)
        out["got"].append(b["n"])
        pending[path] = text
        weight += 0.2 if kind == "suggest" else 1.0     # 자동완성 묶음은 빨리 끝나 5개를 하나로 셈 (커밋 수 줄임)
        if gh and weight >= opts.push_every:
            gh.commit(pending, f"[{topic} 트렌드] 구글 트렌드 묶음 {len(pending)}개 (tools/pc_trends.py {VERSION}, PC)")
            out["pushed"] += len(pending)
            pending, weight = {}, 0.0
    if gh and pending:
        gh.commit(pending, f"[{topic} 트렌드] 구글 트렌드 묶음 {len(pending)}개{' — 막히기 전까지' if out['blocked'] else ''} (tools/pc_trends.py {VERSION}, PC)")
        out["pushed"] += len(pending)
    done_next = spec.get("next") or f"클라우드에서 python3 tools/next_topic.py {topic} trends"
    log("SUMMARY", topic=topic, got=len(out["got"]), skipped=len(out["skipped"]), failed=out["failed"] or "-", blocked=out["blocked"], pushed=out["pushed"],
        next=("몇 시간 뒤 같은 명령 (남은 묶음만) 또는 목록 .md 의 주소를 브라우저로" if out["blocked"] or out["failed"] else done_next))
    return out


def list_path_of(topic, name):
    """--list 값 → GitHub 경로. 비면 옛 경로 · '/' 가 없으면 <주제>/result/gap/<이름>.json · 다른 주제 경로는 거부."""
    if not name:
        return f"{topic}/result/next_topic/trends_batches.json"
    p = name if "/" in name else f"{topic}/result/gap/{name}.json"
    if not re.fullmatch(rf"{re.escape(topic)}/result/(?:next_topic|gap)/[a-z0-9_]+\.json", p):
        raise SystemExit(f"[LIST] ❌ 목록 경로가 이 주제 결과 폴더 밖: {p}")
    return p


def cmd_run(opts):
    work_root = ROOT / ".yt_work"
    for topic in opts.topics:
        pt.check_topic(topic)
        pt.setup_logging(opts.log_level, work_root / f"trends_log_{topic}.txt")
        ensure_requests(install=not opts.skip_install)
        import requests
        token, src = github_token(topic)                                     # 값은 출력하지 않음
        log("KEYS", GITHUB_TOKEN="있음" if token else "(없음)", source=src)
        if not token and not (opts.no_push or opts.dry_run):
            raise SystemExit("[SETUP] ❌ GITHUB_TOKEN 이 없음 → .env 에 넣고 다시 (또는 --no-push 로 PC 에만 받기)")
        gh = None
        if token and not opts.no_push:
            gh = pt.GitHub(opts.repo, opts.branch, token, topic, dry_run=opts.dry_run)
            gh.allowed = allowed_trends(topic)                                # 대본 경로 대신 트렌드 묶음 경로만
        list_path = list_path_of(topic, opts.list)
        if opts.list_file:
            text = Path(opts.list_file).read_text("utf-8-sig")
        elif gh:
            text = gh.read_text(list_path)
        else:
            r = requests.get(f"https://raw.githubusercontent.com/{opts.repo}/{opts.branch}/{list_path}", timeout=60)
            if r.status_code != 200:
                raise SystemExit(f"[LIST] ❌ 묶음 목록을 못 받음 (HTTP {r.status_code}) {list_path} — 클라우드에서 목록을 먼저 만들어 main 에")
            text = r.text
        spec = json.loads(text)
        batches = spec.get("batches") or []
        if not batches:
            raise SystemExit(f"[LIST] ❌ 묶음이 없음 ({list_path}) — 클라우드에서 목록을 다시 만든다")
        if spec.get("out_dir") and not out_dir_ok(topic, spec["out_dir"]):
            raise SystemExit(f"[LIST] ❌ out_dir 이 이 주제 결과 폴더 밖: {spec['out_dir']} (되는 꼴: {topic}/result/gap/<이름>)")
        log("LIST", topic=topic, batches=len(batches), anchor=spec.get("anchor") or "-", geo=spec.get("geo", "KR"), time=spec.get("time", "today 12-m"),
            out_dir=spec.get("out_dir") or "next_topic/trends", made=spec.get("made"), source=opts.list_file or list_path)
        tr = Trends(requests.Session(), hl=spec.get("hl", "ko"))
        work = work_root / "trends" / topic / (Path(list_path).stem if opts.list else "")
        out = run_topic(topic, batches, tr, gh, work, opts, spec=spec)
        if out["blocked"] and not out["got"]:
            return 2
    return 0


# ============================================================================ v1.3 제작 판 — 간격마다 받기
def period_of(every_hours, now=None):
    """간격 → 결과 폴더 기간 이름. 24시간 이상 = 날짜(YYYYMMDD — 며칠 간격이면 그 날수로 내림) · 그 아래 = 날짜_시(간격으로 내림)."""
    import datetime as _dt
    now = now or _dt.datetime.now()
    eh = max(1, int(every_hours or 24))
    if eh >= 24:
        days = eh // 24
        d = _dt.date.fromordinal(now.date().toordinal() // days * days)
        return d.strftime("%Y%m%d")
    return now.strftime("%Y%m%d") + f"_{now.hour // eh * eh:02d}"


def _hash(words, extra=""):
    import hashlib
    return hashlib.sha1(("|".join(words) + "#" + str(extra)).encode("utf-8")).hexdigest()[:6]


def board_specs(state, now=None):
    """studio/state/trends.json → [(주제, 목록 spec)]. 주제마다 시간 흐름(5개씩 — 첫 낱말이 기준, 묶음마다 같이) + 관련 검색어 · 전체 탐색 = 분류만 관련 검색어."""
    out = []
    geo, gprop, time_ = state.get("geo", "KR"), state.get("gprop", "youtube"), state.get("time", "today 3-m")
    for topic, t in (state.get("topics") or {}).items():
        words = [w.strip() for w in (t.get("words") or []) if isinstance(w, str) and w.strip()][:25]
        if not words or not pt.TOPIC_RX.match(topic):
            continue
        anchor, rest = words[0], words[1:]
        groups = [[anchor] + rest[i:i + 4] for i in range(0, len(rest), 4)] or [[anchor]]
        batches = [{"n": i + 1, "kind": "timeseries", "words": g, "hash": _hash(g, time_)} for i, g in enumerate(groups)]
        batches += [{"n": 100 + i + 1, "kind": "related", "words": g, "hash": _hash(g, "rel" + time_)} for i, g in enumerate(groups)]
        out.append((topic, {"topic": topic, "out_dir": f"{topic}/result/next_topic/board_{period_of(t.get('every_hours', 24), now)}",
                            "geo": geo, "gprop": gprop, "time": time_, "hl": "ko", "hash_names": True, "anchor": anchor,
                            "batches": batches, "next": "Claude: python3 tools/studio_board.py build → 제작 판 다시 올림"}))
    ov = state.get("overall") or {}
    cats = [int(c) for c in (ov.get("cats") or []) if str(c).isdigit()]
    if cats and pt.TOPIC_RX.match(ov.get("topic", "new")):
        tm = ov.get("time", "now 7-d")
        out.append((ov.get("topic", "new"), {"topic": ov.get("topic", "new"), "out_dir": f"{ov.get('topic', 'new')}/result/next_topic/board_{period_of(ov.get('every_hours', 24), now)}",
                                             "geo": geo, "gprop": gprop, "time": tm, "hl": "ko", "hash_names": True,
                                             "batches": [{"n": i + 1, "kind": "related", "cat": c, "words": [], "hash": _hash([str(c)], tm)} for i, c in enumerate(cats)],
                                             "next": "Claude: python3 tools/studio_board.py build → 제작 판 다시 올림"}))
    return out


def cmd_watch(opts, sleep=time.sleep):
    """간격마다: GitHub 에서 판 검색어를 읽고 → 이번 기간에 아직 없는 묶음만 받아 올림. --once 면 한 번."""
    if opts.list_file and not Path(opts.list_file).is_file():          # v1.3.1 사람이 둔 파일 — 다음 회차에도 안 생기니 바로 멈춤
        raise SystemExit(f"[SETUP] ❌ 검색어 파일이 없음: {Path(opts.list_file).resolve()} → run_analyzer.ps1 과 같은 폴더({Path.cwd()})에 두고 다시")
    work_root = ROOT / ".yt_work"
    pt.setup_logging(opts.log_level, work_root / "trends_log_board.txt")
    ensure_requests(install=not opts.skip_install)
    import requests
    rounds = 0
    while True:
        rounds += 1
        token, src = github_token("new")
        log("WATCH", round=rounds, GITHUB_TOKEN="있음" if token else "(없음)", source=src, every_min=opts.every, once=opts.once)
        if not token and not (opts.no_push or opts.dry_run):
            raise SystemExit("[SETUP] ❌ GITHUB_TOKEN 이 없음 → 맨 위 .env 에 넣고 다시 (또는 --no-push 로 PC 에만)")
        try:
            if opts.list_file:
                text = Path(opts.list_file).read_text("utf-8-sig")
            else:
                r = requests.get(f"https://raw.githubusercontent.com/{opts.repo}/{opts.branch}/{BOARD_STATE}", timeout=60,
                                 headers={"Authorization": f"token {token}"} if token else {})
                if r.status_code != 200:
                    raise RuntimeError(f"HTTP {r.status_code} — 아직 판 동기화 전이면 Claude 에게 '제작 판 동기화해'")
                text = r.text
            state = json.loads(text)
        except Exception as e:
            log("WATCH", level=logging.WARNING, step="판 검색어 읽기", error=f"{type(e).__name__}: {str(e)[:160]}", next="다음 회차에 다시")
            state = None
        if state:
            specs = board_specs(state)
            log("WATCH", updated=state.get("updated", "-"), lists=len(specs), batches=sum(len(s["batches"]) for _, s in specs))
            tr = Trends(requests.Session(), hl="ko")
            for topic, spec in specs:
                gh = None
                if token and not opts.no_push:
                    gh = pt.GitHub(opts.repo, opts.branch, token, topic, dry_run=opts.dry_run)
                    gh.allowed = allowed_trends(topic)
                if not out_dir_ok(topic, spec["out_dir"]):
                    log("WATCH", level=logging.WARNING, topic=topic, out_dir=spec["out_dir"], note="결과 폴더가 주제 밖 — 건너뜀")
                    continue
                out = run_topic(topic, spec["batches"], tr, gh, work_root / "trends" / topic / Path(spec["out_dir"]).name, opts, spec=spec)
                if out["blocked"]:
                    log("WATCH", level=logging.WARNING, topic=topic, note="구글이 막음(429) — 이번 회차는 여기까지, 다음 회차에 남은 것만")
                    break
        if opts.once:
            return 0
        log("WATCH", next_round_min=opts.every, note="켜 둔 채로 두면 이 간격마다 다시 (멈춤 Ctrl+C) · 같은 기간에 이미 올린 묶음은 건너뜀")
        sleep(opts.every * 60)


# ============================================================================ selftest
def selftest():
    import types
    for k in [k for k in __import__("os").environ if "TOKEN" in k.upper()]:   # CLAUDE.md: 푸시 도구 시험 = 토큰 환경 변수 지우고 가짜 저장소
        __import__("os").environ.pop(k, None)
    pt.setup_logging("INFO")
    ok = True

    def check(name, cond, **kv):
        nonlocal ok
        ok &= bool(cond)
        log("SELFTEST", **{"result": "✅" if cond else "❌", "name": name}, **kv)

    class R:
        def __init__(self, code, text):
            self.status_code, self.text, self.content, self.headers = code, text, text.encode("utf-8"), {}

    class FakeGoogle:
        """첫 화면 → explore → csv · relatedsearches · 분류표 · 자동완성. block 회 만큼 429 를 먼저 돌려줌."""

        def __init__(self, block=0):
            self.headers, self.calls, self.block, self.reqs = {}, [], block, []

        def get(self, url, params=None, timeout=0):
            self.calls.append(url.split("/trends")[-1] if "/trends" in url else "suggest")
            if self.block:
                self.block -= 1
                return R(429, "Too Many Requests")
            if url.endswith("/trends/explore"):
                return R(200, "<html>ok</html>")
            if url.endswith("/api/explore"):
                req = json.loads(params["req"])
                self.reqs.append(req)
                words = [c["keyword"] for c in req["comparisonItem"]]
                wid = [{"id": "TIMESERIES", "token": "tok", "request": {"w": words}}, {"id": "GEO_MAP"}]
                for i, w in enumerate(words):
                    rr = {"restriction": {"complexKeywordsRestriction": {"keyword": [{"type": "BROAD", "value": w}]}}} if w else {"restriction": {}}
                    wid.append({"id": f"RELATED_QUERIES{'_' + str(i) if i else ''}", "token": f"rq{i}", "request": dict(rr, cat=req["category"])})
                return R(200, ")]}'\n" + json.dumps({"widgets": wid}))
            if url.endswith("/multiline/csv"):
                w = json.loads(params["req"])["w"]
                head = "주," + ",".join(f"{x}: (대한민국)" for x in w)
                return R(200, "﻿카테고리: 모든 카테고리\n\n" + head + "\n2025-11-23," + ",".join(["50"] * len(w)) + "\n2025-11-30," + ",".join(["<1"] * len(w)) + "\n")
            if url.endswith("/relatedsearches"):
                kw = keyword_of(json.loads(params["req"])) or "분류"
                return R(200, ")]}',\n" + json.dumps({"default": {"rankedList": [
                    {"rankedKeyword": [{"query": f"{kw} 방법", "value": 100, "formattedValue": "100"}]},
                    {"rankedKeyword": [{"query": f"{kw} 급상승", "value": 250, "formattedValue": "+250%"}]}]}}, ensure_ascii=False))
            if url.endswith("/pickers/category"):
                return R(200, ")]}'\n" + json.dumps({"name": "모든 카테고리", "id": 0, "children": [{"name": "건강", "id": 45}, {"name": "과학", "id": 174}]}, ensure_ascii=False))
            if url == SUGGEST:
                q = params["q"]
                return R(200, json.dumps([q, [f"{q} 이유", f"{q} 방법"]], ensure_ascii=False))
            return R(404, "")

    class FakeGH:
        def __init__(self, existing=(), topic="demo"):
            self.branch, self.allowed, self.commits, self.existing = "main", allowed_trends(topic), [], set(existing)

        def req(self, method, path, params=None, ok=()):
            return R(200 if path.split("/contents/")[-1] in self.existing else 404, "")

        def commit(self, files, message):
            bad = [p for p in files if not self.allowed.match(p)]
            if bad:
                raise ValueError(bad)
            self.commits.append((dict(files), message))
            return "sha"

    base = Path(__import__("tempfile").mkdtemp(prefix="pc_trends_selftest_"))
    batches = [{"n": 1, "words": ["조선", "목욕", "녹봉", "석빙고", "짚신"]}, {"n": 2, "words": ["조선", "족보", "주막", "과거시험", "화장실"]},
               {"n": 3, "words": ["조선", "노비", "기생", "궁녀", "온돌"]}]
    opts = types.SimpleNamespace(force=False, limit=0, pause=1, push_every=2)
    slept = []
    g = FakeGoogle()
    gh = FakeGH(existing={trends_path("demo", 3)})
    out = run_topic("demo", batches, Trends(g, sleep=slept.append), gh, base / "w", opts, sleep=slept.append, rnd=lambda: 0.5)
    check("GitHub 에 이미 있는 묶음은 건너뜀", out["skipped"] == [3] and out["got"] == [1, 2])
    check("묶음 사이 쉼 (pause × 1~2)", slept == [1.5], slept=slept)
    check("첫 화면(쿠키) → explore → csv 차례", g.calls[:3] == ["/explore", "/api/explore", "/api/widgetdata/multiline/csv"], calls=g.calls[:3])
    files = gh.commits[0][0] if gh.commits else {}
    check("올린 파일 = 트렌드 CSV 두 개, 경로 batch_NN.csv (옛 목록 그대로)", sorted(files) == [trends_path("demo", 1), trends_path("demo", 2)])
    check("CSV 꼴 = 화면 ⤓ 와 같음 (주,낱말: (대한민국) · '<1')", "주,조선: (대한민국)" in files.get(trends_path("demo", 1), "") and "<1" in files.get(trends_path("demo", 1), ""))
    try:
        gh.commit({"demo/result/outliers/analysis.md": "x"}, "bad")
        check("트렌드 묶음이 아닌 경로는 거부", False)
    except ValueError:
        check("트렌드 묶음이 아닌 경로는 거부", True)
    slept2 = []
    g2 = FakeGoogle(block=1)
    out2 = run_topic("demo", batches[:1], Trends(g2, sleep=slept2.append), FakeGH(), base / "w2", opts, sleep=slept2.append, rnd=lambda: 0.0)
    check("429 한 번 → 1분 쉬고 다시 → 받음", out2["got"] == [1] and slept2[:1] == [60], slept=slept2)
    slept3 = []
    gh3 = FakeGH()
    out3 = run_topic("demo", batches, Trends(FakeGoogle(block=99), sleep=slept3.append), gh3, base / "w3", opts, sleep=slept3.append)
    check("계속 429 → 1·2·4분 쉰 뒤 멈춤, 올릴 것 없음", out3["blocked"] and not out3["got"] and slept3 == list(BACKOFF) and not gh3.commits, slept=slept3)
    mixed = [{"n": 1, "words": ["a", "b"]}, {"n": 2, "kind": "suggest", "words": ["혈당"]}, {"n": 3, "words": ["c", "d"]}]

    class TrendsOnlyBlocked(FakeGoogle):
        def get(self, url, params=None, timeout=0):
            if "/trends" in url:
                self.calls.append("blocked")
                return R(429, "Too Many Requests")
            return super().get(url, params, timeout)

    slept5, gh5 = [], FakeGH(topic="demo")
    sp5 = {"out_dir": "demo/result/gap/mixed"}
    out5 = run_topic("demo", mixed, Trends(TrendsOnlyBlocked(), sleep=slept5.append), gh5, base / "w5", opts, sleep=slept5.append, rnd=lambda: 0.0, spec=sp5)
    check("v1.2 트렌드가 막혀도 자동완성 묶음은 이어서 받음 (막힌 트렌드 묶음 3 은 시도 안 함)", out5["blocked"] and out5["got"] == [2], got=out5["got"])
    # ── v1.2: 갭 탐색 목록 (out_dir · kind · geo) ──
    spec = {"topic": "demo", "out_dir": "demo/result/gap/discover", "geo": "KR", "time": "today 12-m", "gprop": "youtube",
            "batches": [{"n": 0, "kind": "categories"},
                        {"n": 1, "kind": "related", "cat": 45, "words": [], "label": "건강"},
                        {"n": 2, "kind": "related", "words": ["혈당", "공룡"]},
                        {"n": 3, "kind": "suggest", "words": ["혈당"], "suffixes": ["", " 이유"]},
                        {"n": 4, "kind": "timeseries", "words": ["math", "riddle"], "geo": ""}]}
    g4, slept4, gh4 = FakeGoogle(), [], FakeGH()
    out4 = run_topic("demo", spec["batches"], Trends(g4, sleep=slept4.append, rnd=lambda: 0.0), gh4, base / "w4",
                     types.SimpleNamespace(force=False, limit=0, pause=30, push_every=99), sleep=slept4.append, rnd=lambda: 0.0, spec=spec)
    allf = {k: v for c in gh4.commits for k, v in c[0].items()}
    want = ["demo/result/gap/discover/batch_000.json", "demo/result/gap/discover/batch_001.json", "demo/result/gap/discover/batch_002.json",
            "demo/result/gap/discover/batch_003.json", "demo/result/gap/discover/batch_004.csv"]
    check("v1.2 목록 폴더 · 종류별 확장자 (json·csv) · 다섯 묶음 모두", out4["got"] == [0, 1, 2, 3, 4] and sorted(allf) == want, got=sorted(allf))
    r1 = json.loads(allf.get(want[1], "{}"))
    check("v1.2 키워드 없이 분류만 → 관련 검색어 (cat 45 · 인기·급상승)", g4.reqs[0]["category"] == 45 and g4.reqs[0]["comparisonItem"][0]["keyword"] == ""
          and r1.get("items", [{}])[0].get("top", [{}])[0].get("q") == "분류 방법" and r1.get("label") == "건강", req=g4.reqs[0])
    r2 = json.loads(allf.get(want[2], "{}"))
    check("v1.2 낱말 두 개 → 위젯 두 개 · 낱말 짝이 맞음 · 위젯 사이 4~8초", [x["keyword"] for x in r2.get("items", [])] == ["혈당", "공룡"]
          and r2["items"][1]["rising"][0]["f"] == "+250%" and INNER_PAUSE in slept4, slept=slept4)
    r3 = json.loads(allf.get(want[3], "{}"))
    check("v1.2 자동완성 — 낱말 × 뒤에 붙일 말 · 쉼 1~2초", list(r3.get("results", {})) == ["혈당", "혈당 이유"] and r3["results"]["혈당 이유"][0] == "혈당 이유 이유"
          and SUGGEST_PAUSE in slept4, results=list(r3.get("results", {})))
    check("v1.2 목록의 나라 값을 씀 (묶음 geo '' = 전 세계 · 목록 KR)", g4.reqs[-1]["comparisonItem"][0]["geo"] == "" and g4.reqs[0]["comparisonItem"][0]["geo"] == "KR",
          geos=[r["comparisonItem"][0]["geo"] for r in g4.reqs])
    check("v1.2 경로 검사 — 다른 주제·폴더 밖은 거부", not allowed_trends("demo").match("other/result/gap/discover/batch_001.json")
          and not allowed_trends("demo").match("demo/result/gap/../x/batch_001.json") and not out_dir_ok("demo", "demo/result/outliers")
          and out_dir_ok("demo", "demo/result/gap/interest"))
    check("v1.2 --list 이름 → <주제>/result/gap/<이름>.json · 비면 옛 경로", list_path_of("demo", "discover") == "demo/result/gap/discover.json"
          and list_path_of("demo", "") == "demo/result/next_topic/trends_batches.json")
    try:
        list_path_of("demo", "other/result/gap/x.json")
        check("v1.2 --list 다른 주제 경로는 거부", False)
    except SystemExit:
        check("v1.2 --list 다른 주제 경로는 거부", True)
    kd = base / "keys"                                                      # v1.1: 키 읽기 순서 (가짜 값)
    (kd / "demo").mkdir(parents=True)
    (kd / ".env").write_text("﻿GITHUB_TOKEN='root-fake'\n", "utf-8")
    t1 = github_token("demo", root=kd, environ={"GITHUB_TOKEN": "env-fake"})
    (kd / "demo" / ".env").write_text("# 주석\nGITHUB_TOKEN=topic-fake\n", "utf-8")
    t2 = github_token("demo", root=kd, environ={"GITHUB_TOKEN_DEMO": "tag-fake"})
    t3 = github_token("none", root=base / "empty", environ={})
    check("키 읽기 순서 (주제 .env → GITHUB_TOKEN_<주제> → 맨 위 .env → 환경 변수 · BOM·따옴표)",
          t1 == ("root-fake", ".env") and t2 == ("topic-fake", "demo/.env") and t3 == ("", "-"), got=[t1[1], t2[1], t3[1]])
    calls = []
    check("requests 있으면 설치 안 함", ensure_requests(run=lambda *a, **k: calls.append(a)) and not calls)
    import datetime as _dt                                                   # v1.3 제작 판 watch
    st = {"geo": "KR", "gprop": "youtube", "time": "today 3-m", "topics": {"psychology": {"words": ["심리", "엄마", "말투", "눈치", "허세", "뒷담화"], "every_hours": 24}},
          "overall": {"topic": "new", "cats": [0, 14], "time": "now 7-d", "every_hours": 6}}
    sp = board_specs(st, now=_dt.datetime(2026, 11, 27, 15, 30))
    ps = dict(sp)["psychology"]
    check("v1.3 판 묶음 — 5개씩·첫 낱말이 기준 · 관련 검색어도", [b_["words"] for b_ in ps["batches"] if b_["kind"] == "timeseries"] == [["심리", "엄마", "말투", "눈치", "허세"], ["심리", "뒷담화"]]
          and sum(1 for b_ in ps["batches"] if b_["kind"] == "related") == 2)
    check("v1.3 기간 폴더 (24시간 = 날짜 · 6시간 = 날짜_시)", ps["out_dir"] == "psychology/result/next_topic/board_20261127"
          and dict(sp)["new"]["out_dir"] == "new/result/next_topic/board_20261127_12" and out_dir_ok("psychology", ps["out_dir"]))
    pth = batch_path("psychology", ps, ps["batches"][0])
    check("v1.3 지문 파일 이름이 올리기 허용 경로", re.fullmatch(r"psychology/result/next_topic/board_20261127/batch_001_[0-9a-f]{6}\.csv", pth) is not None
          and bool(allowed_trends("psychology").match(pth)), path=pth)
    check("v1.3 검색어가 바뀌면 지문도 바뀜", _hash(["심리", "엄마"]) != _hash(["심리", "말투"]) and period_of(48, _dt.datetime(2026, 11, 27)) in ("20261126", "20261127"))
    # v1.3.1 watch --list-file: 없으면 경로와 함께 바로 멈춤 · 깨진 파일이면 경고만 (예전엔 경고 로그가 TypeError 로 죽음)
    wopts = types.SimpleNamespace(list_file=str(base / "없는_파일.json"), log_level="INFO", skip_install=True, no_push=True, dry_run=False,
                                  once=True, every=60, repo="fake/fake", branch="main", limit=0, pause=0, push_every=4, force=False)
    try:
        cmd_watch(wopts, sleep=lambda s: None)
        msg = ""
    except SystemExit as e_:
        msg = str(e_)
    check("v1.3.1 watch --list-file 없음 → 찾은 경로와 함께 멈춤", "검색어 파일이 없음" in msg and "없는_파일.json" in msg, got=msg[:80])
    bad = base / "깨진.json"
    bad.write_text("{깨진 json", "utf-8")
    wopts.list_file = str(bad)
    try:
        rc, err = cmd_watch(wopts, sleep=lambda s: None), ""
    except Exception as e_:                                                    # noqa: BLE001 — 시험: 어떤 오류든 실패로
        rc, err = None, f"{type(e_).__name__}: {e_}"
    pt.setup_logging("INFO")                                                   # cmd_watch 가 바꾼 로그 파일 연결을 되돌림
    check("v1.3.1 watch 깨진 검색어 파일 → 경고만 하고 끝남 (TypeError 없음)", rc == 0 and not err, got=rc, error=err[:80] or "-")
    log("SELFTEST", result="✅ 모두 통과" if ok else "❌ 실패 있음")
    return 0 if ok else 1


def main(argv=None):
    ap = argparse.ArgumentParser(description="구글 트렌드 묶음 받기 (PC) → GitHub")
    sub = ap.add_subparsers(dest="cmd", required=True)
    pr = sub.add_parser("run", help="PC: 묶음 받기·올리기")
    pr.add_argument("topics", nargs="+")
    pr.add_argument("--list", default="", help="v1.2: 묶음 목록 — 이름(<주제>/result/gap/<이름>.json) 또는 GitHub 경로 · 비면 <주제>/result/next_topic/trends_batches.json")
    pr.add_argument("--limit", type=int, default=0, help="이번에 받을 묶음 수 (시험 삼아 --limit 3)")
    pr.add_argument("--pause", type=float, default=30, help="트렌드 묶음 사이 쉼 (초) — 실제로는 이 값의 1~2배 (기본 30 → 30~60초)")
    pr.add_argument("--push-every", type=int, default=4, help="묶음 몇 개마다 올릴지 (기본 4 · 자동완성 묶음은 5개를 하나로 셈)")
    pr.add_argument("--force", action="store_true", help="GitHub 에 이미 있는 묶음도 다시 받기")
    pr.add_argument("--no-push", action="store_true", help="올리지 않고 .yt_work/trends/<주제>/ 에만")
    pr.add_argument("--dry-run", action="store_true", help="올릴 것만 보여 줌")
    pr.add_argument("--list-file", default="", help="GitHub 대신 이 묶음 목록 파일")
    pr.add_argument("--repo", default="yeomin1024/yeomin1024-ytb")
    pr.add_argument("--branch", default="main")
    pr.add_argument("--skip-install", action="store_true", help="requests 가 없어도 설치하지 않음")
    pr.add_argument("--log-level", default="INFO")
    pw = sub.add_parser("watch", help="v1.3 PC: 제작 판 검색어를 간격마다 받아 올리기 (studio/state/trends.json)")
    pw.add_argument("--every", type=float, default=60, help="회차 사이 (분, 기본 60) — 같은 기간 결과가 이미 있으면 건너뛰므로 자주 돌려도 구글을 다시 부르지 않음")
    pw.add_argument("--once", action="store_true", help="한 회차만")
    pw.add_argument("--limit", type=int, default=0)
    pw.add_argument("--pause", type=float, default=30)
    pw.add_argument("--push-every", type=int, default=4)
    pw.add_argument("--force", action="store_true")
    pw.add_argument("--no-push", action="store_true")
    pw.add_argument("--dry-run", action="store_true")
    pw.add_argument("--list-file", default="", help="GitHub 대신 이 trends.json")
    pw.add_argument("--repo", default="yeomin1024/yeomin1024-ytb")
    pw.add_argument("--branch", default="main")
    pw.add_argument("--skip-install", action="store_true")
    pw.add_argument("--log-level", default="INFO")
    sub.add_parser("selftest", help="가짜 구글·가짜 GitHub 로 시험")
    a = ap.parse_args(argv)
    if a.cmd == "selftest":
        return selftest()
    if a.cmd == "watch":
        return cmd_watch(a)
    return cmd_run(a)


if __name__ == "__main__":
    sys.exit(main())
