#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-11-25 — PC 오류 "ModuleNotFoundError: No module named 'requests'" 고침 (사용자 보고): 분석기(numpy·pandas·matplotlib …)를 키 읽기용으로 불러오지 않고 .env 를 직접 읽음 · requests 만 없으면 설치.
# (v1.0 — 2026-11-25 — 새로: 구글 트렌드(유튜브 검색·한국·최근 12개월) 묶음 CSV 를 PC(집 인터넷)에서 받아 GitHub 에
#   사용자 지시 2026-11-25 "트렌드 사이트는 왜 막히는거야 안 막히고 돌리는 방법 없어? 내가 코드를 실행한다던가" →)
#   클라우드는 허용 목록에 넣어도 구글이 첫 요청부터 HTTP 429 (데이터센터 주소) — 2026-11-25 시험. 집 인터넷 주소는 사람이 쓰는 주소라 대개 받힘.
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.1 | 2026-11-25 | ensure_requests (requests 만 설치) · github_token (분석기와 같은 순서로 .env 직접 읽기 — 분석기 import 뺌) · selftest 2개 더 | ensure_requests · github_token · cmd_run · selftest |
# | v1.0 | 2026-11-25 | 최초 — run(묶음 목록 trends_batches.json → 묶음마다 explore → 시간 흐름 위젯 CSV → GitHub) · selftest(가짜 구글·가짜 GitHub) | Trends · run_topic · selftest |
"""구글 트렌드 묶음 받기 — 목록은 클라우드(tools/next_topic.py <주제> report|batches)가 정하고, 받기·올리기는 PC 에서.

왜 PC: 구글 트렌드는 공식 공개 API 가 없고, 화면이 쓰는 내부 주소를 자동으로 부르면 서버(데이터센터) 주소는 첫 요청부터 HTTP 429
       (2026-11-25 클라우드에서 허용 목록에 넣은 뒤 시험 — 화면 주소도 429). 집 인터넷은 사람이 쓰는 주소라 천천히 부르면 대개 받힘.

  PC(사용자)  powershell -ExecutionPolicy Bypass -File run_analyzer.ps1 -Trends -Folder history
              (= .venv\\Scripts\\python.exe tools/pc_trends.py run history · 시험 삼아 한 묶음만: … --limit 1 · 받기만: … --no-push)
  시험        python3 tools/pc_trends.py selftest      (가짜 구글·가짜 GitHub — 진짜로 부르거나 올리지 않음)

하는 일 (묶음마다, 목록 순서대로):
  ① trends.google.com 첫 화면 (쿠키) → ② /trends/api/explore (그 묶음 낱말 5개 · 한국 · 최근 12개월 · 유튜브 검색) → 'TIMESERIES' 위젯 token
  → ③ /trends/api/widgetdata/multiline/csv = 화면의 ⤓(CSV) 단추와 같은 파일 → batch_NN.csv
  쉬기: 묶음 사이 30~60초 (--pause) · 429 면 1·2·4분 쉬고 다시, 그래도 429 면 받은 것까지 올리고 멈춤 (몇 시간 뒤 다시 실행하면 남은 묶음만).
  올리기: GitHub API 로 <주제>/result/next_topic/trends/batch_NN.csv 만 (다른 경로는 코드가 거부) · 이미 GitHub 에 있는 묶음은 건너뜀 (--force 면 다시).
그다음 클라우드에서: python3 tools/next_topic.py <주제> trends → trends.md (기준 낱말로 묶음끼리 이어 붙인 관심도 순위)
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

VERSION = "v1.1"
LOG = logging.getLogger("pc_trends")
TRENDS = "https://trends.google.com"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/124.0 Safari/537.36")
BACKOFF = (60, 120, 240)          # 429 면 이만큼 쉬고 다시 (초)


def log(stage, level=logging.INFO, **kv):
    LOG.log(level, "[%s] [%s] %s", stage, time.strftime("%Y-%m-%dT%H:%M:%S"), " ".join(f"{k}={v}" for k, v in kv.items()))


def trends_path(topic, n):
    return f"{topic}/result/next_topic/trends/batch_{n:02d}.csv"


def allowed_trends(topic):
    """올려도 되는 경로 — 이 주제 트렌드 묶음 CSV 만."""
    return re.compile(rf"^{re.escape(topic)}/result/next_topic/trends/batch_\d{{2}}\.csv$")


class Blocked(Exception):
    """구글이 계속 429 — 오늘은 여기까지."""


class Trends:
    """구글 트렌드 화면이 부르는 주소를 차례로 (세션 쿠키 유지 · 천천히)."""

    def __init__(self, session, sleep=time.sleep, hl="ko", tz=-540):
        self.s, self.sleep, self.hl, self.tz = session, sleep, hl, tz
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
        raise Blocked(f"HTTP 429 가 {len(BACKOFF) + 1}번 — 구글이 이 주소를 막음 (몇 시간 뒤 다시, 또는 trends_batches.md 주소를 브라우저로)")

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

    def csv(self, words, geo="KR", time_="today 12-m", gprop="youtube"):
        self.warm()
        req = {"comparisonItem": [{"keyword": w, "geo": geo, "time": time_} for w in words], "category": 0, "property": gprop}
        r = self._get(f"{TRENDS}/trends/api/explore", hl=self.hl, tz=self.tz, req=json.dumps(req, ensure_ascii=False))
        widgets = self._json(r.text).get("widgets") or []
        ts = next((w for w in widgets if w.get("id") == "TIMESERIES"), None)
        if not ts:
            raise RuntimeError(f"시간 흐름 위젯 없음 (위젯 {[w.get('id') for w in widgets]})")
        r = self._get(f"{TRENDS}/trends/api/widgetdata/multiline/csv", req=json.dumps(ts["request"], ensure_ascii=False),
                      token=ts["token"], tz=self.tz, hl=self.hl)
        text = r.content.decode("utf-8-sig", "replace")
        if not re.search(r"^(주|Week|월|Month|날짜|Day)", text, re.M):
            raise RuntimeError(f"CSV 머리 줄(주,…)이 없음: {text[:120]!r}")
        return text


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


def run_topic(topic, batches, tr, gh, work, opts, sleep=time.sleep, rnd=random.random):
    """묶음마다 받기 → work 에 저장 → GitHub (gh 가 있으면). 돌려줌: {'got': [...], 'skipped': [...], 'failed': [...], 'blocked': bool}."""
    out = {"got": [], "skipped": [], "failed": [], "blocked": False, "pushed": 0}
    work.mkdir(parents=True, exist_ok=True)
    todo = []
    for b in batches:
        p = trends_path(topic, b["n"])
        if not opts.force and ((work / Path(p).name).is_file() and not gh or (gh and exists_on_github(gh, p))):
            out["skipped"].append(b["n"])
            continue
        todo.append(b)
    if opts.limit:
        todo = todo[: opts.limit]
    log("RUN", topic=topic, batches=len(batches), this_run=len(todo), skipped=len(out["skipped"]), push=bool(gh), pause=f"{opts.pause}~{opts.pause * 2}s")
    pending = {}
    for i, b in enumerate(todo):
        if i:
            wait = opts.pause * (1 + rnd())          # 묶음 사이 pause~2×pause 초 (사람처럼 — 고르게 치지 않게)
            log("PAUSE", seconds=round(wait))
            sleep(wait)
        try:
            text = tr.csv(b["words"])
        except Blocked as e:
            log("BLOCKED", level=logging.WARNING, batch=b["n"], why=str(e))
            out["blocked"] = True
            break
        except Exception as e:                          # 한 묶음 실패는 기록하고 다음 묶음
            log("BATCH", level=logging.WARNING, batch=b["n"], words="·".join(b["words"]), error=f"{type(e).__name__}: {str(e)[:160]}")
            out["failed"].append(b["n"])
            continue
        f = work / Path(trends_path(topic, b["n"])).name
        f.write_text(text, encoding="utf-8")
        rows = sum(1 for ln in text.splitlines() if re.match(r"\d{4}-\d{2}", ln))
        log("BATCH", batch=b["n"], words="·".join(b["words"]), weeks=rows, saved=str(f.relative_to(work.parent.parent)) if work.parent.parent in f.parents else str(f))
        out["got"].append(b["n"])
        pending[trends_path(topic, b["n"])] = text
        if gh and len(pending) >= opts.push_every:
            gh.commit(pending, f"[{topic} 트렌드] 구글 트렌드 묶음 {len(pending)}개 (tools/pc_trends.py {VERSION}, PC)")
            out["pushed"] += len(pending)
            pending = {}
    if gh and pending:
        gh.commit(pending, f"[{topic} 트렌드] 구글 트렌드 묶음 {len(pending)}개{' — 막히기 전까지' if out['blocked'] else ''} (tools/pc_trends.py {VERSION}, PC)")
        out["pushed"] += len(pending)
    log("SUMMARY", topic=topic, got=len(out["got"]), skipped=len(out["skipped"]), failed=out["failed"] or "-", blocked=out["blocked"], pushed=out["pushed"],
        next=("몇 시간 뒤 같은 명령 (남은 묶음만) 또는 trends_batches.md 주소를 브라우저로" if out["blocked"] or out["failed"]
              else f"클라우드에서 python3 tools/next_topic.py {topic} trends"))
    return out


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
            gh.allowed = allowed_trends(topic)                                # 대본 경로 대신 트렌드 CSV 경로만
        list_path = f"{topic}/result/next_topic/trends_batches.json"
        if opts.list_file:
            text = Path(opts.list_file).read_text("utf-8-sig")
        elif gh:
            text = gh.read_text(list_path)
        else:
            r = requests.get(f"https://raw.githubusercontent.com/{opts.repo}/{opts.branch}/{list_path}", timeout=60)
            if r.status_code != 200:
                raise SystemExit(f"[LIST] ❌ 묶음 목록을 못 받음 (HTTP {r.status_code}) — 클라우드에서 next_topic.py {topic} report 를 먼저")
            text = r.text
        spec = json.loads(text)
        batches = spec.get("batches") or []
        if not batches:
            raise SystemExit(f"[LIST] ❌ 묶음이 없음 — 클라우드에서 {topic}/next_topic.toml [trends] WORDS 를 채우고 next_topic.py {topic} batches")
        log("LIST", topic=topic, batches=len(batches), anchor=spec.get("anchor"), made=spec.get("made"), source=opts.list_file or list_path)
        tr = Trends(requests.Session())
        out = run_topic(topic, batches, tr, gh, work_root / "trends" / topic, opts)
        if out["blocked"] and not out["got"]:
            return 2
    return 0


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
        """첫 화면 → explore → csv. block 회 만큼 429 를 먼저 돌려줌."""

        def __init__(self, block=0):
            self.headers, self.calls, self.block = {}, [], block

        def get(self, url, params=None, timeout=0):
            self.calls.append(url.split("/trends")[-1])
            if self.block:
                self.block -= 1
                return R(429, "Too Many Requests")
            if url.endswith("/trends/explore"):
                return R(200, "<html>ok</html>")
            if url.endswith("/api/explore"):
                req = json.loads(params["req"])
                words = [c["keyword"] for c in req["comparisonItem"]]
                return R(200, ")]}'\n" + json.dumps({"widgets": [{"id": "TIMESERIES", "token": "tok", "request": {"w": words}}, {"id": "GEO_MAP"}]}))
            if url.endswith("/multiline/csv"):
                w = json.loads(params["req"])["w"]
                head = "주," + ",".join(f"{x}: (대한민국)" for x in w)
                return R(200, "﻿카테고리: 모든 카테고리\n\n" + head + "\n2025-11-23," + ",".join(["50"] * len(w)) + "\n2025-11-30," + ",".join(["<1"] * len(w)) + "\n")
            return R(404, "")

    class FakeGH:
        def __init__(self, existing=()):
            self.branch, self.allowed, self.commits, self.existing = "main", allowed_trends("demo"), [], set(existing)

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
    check("올린 파일 = 트렌드 CSV 두 개, 경로 batch_NN.csv", sorted(files) == [trends_path("demo", 1), trends_path("demo", 2)])
    check("CSV 꼴 = 화면 ⤓ 와 같음 (주,낱말: (대한민국) · '<1')", "주,조선: (대한민국)" in files.get(trends_path("demo", 1), "") and "<1" in files.get(trends_path("demo", 1), ""))
    try:
        gh.commit({"demo/result/outliers/analysis.md": "x"}, "bad")
        check("트렌드 CSV 가 아닌 경로는 거부", False)
    except ValueError:
        check("트렌드 CSV 가 아닌 경로는 거부", True)
    slept2 = []
    g2 = FakeGoogle(block=1)
    out2 = run_topic("demo", batches[:1], Trends(g2, sleep=slept2.append), FakeGH(), base / "w2", opts, sleep=slept2.append, rnd=lambda: 0.0)
    check("429 한 번 → 1분 쉬고 다시 → 받음", out2["got"] == [1] and slept2[:1] == [60], slept=slept2)
    slept3 = []
    gh3 = FakeGH()
    out3 = run_topic("demo", batches, Trends(FakeGoogle(block=99), sleep=slept3.append), gh3, base / "w3", opts, sleep=slept3.append)
    check("계속 429 → 1·2·4분 쉰 뒤 멈춤, 올릴 것 없음", out3["blocked"] and not out3["got"] and slept3 == list(BACKOFF) and not gh3.commits, slept=slept3)
    kd = base / "keys"                                                      # v1.1: 키 읽기 순서 (가짜 값)
    (kd / "demo").mkdir(parents=True)
    (kd / ".env").write_text("\ufeffGITHUB_TOKEN='root-fake'\n", "utf-8")
    t1 = github_token("demo", root=kd, environ={"GITHUB_TOKEN": "env-fake"})
    (kd / "demo" / ".env").write_text("# 주석\nGITHUB_TOKEN=topic-fake\n", "utf-8")
    t2 = github_token("demo", root=kd, environ={"GITHUB_TOKEN_DEMO": "tag-fake"})
    t3 = github_token("none", root=base / "empty", environ={})
    check("키 읽기 순서 (주제 .env → GITHUB_TOKEN_<주제> → 맨 위 .env → 환경 변수 · BOM·따옴표)",
          t1 == ("root-fake", ".env") and t2 == ("topic-fake", "demo/.env") and t3 == ("", "-"), got=[t1[1], t2[1], t3[1]])
    calls = []
    check("requests 있으면 설치 안 함", ensure_requests(run=lambda *a, **k: calls.append(a)) and not calls)
    log("SELFTEST", result="✅ 모두 통과" if ok else "❌ 실패 있음")
    return 0 if ok else 1


def main(argv=None):
    ap = argparse.ArgumentParser(description="구글 트렌드 묶음 CSV 받기 (PC) → GitHub")
    sub = ap.add_subparsers(dest="cmd", required=True)
    pr = sub.add_parser("run", help="PC: 묶음 받기·올리기")
    pr.add_argument("topics", nargs="+")
    pr.add_argument("--limit", type=int, default=0, help="이번에 받을 묶음 수 (시험 삼아 --limit 1)")
    pr.add_argument("--pause", type=float, default=30, help="묶음 사이 쉼 (초) — 실제로는 이 값의 1~2배 (기본 30 → 30~60초)")
    pr.add_argument("--push-every", type=int, default=4, help="묶음 몇 개마다 올릴지 (기본 4)")
    pr.add_argument("--force", action="store_true", help="GitHub 에 이미 있는 묶음도 다시 받기")
    pr.add_argument("--no-push", action="store_true", help="올리지 않고 .yt_work/trends/<주제>/ 에만")
    pr.add_argument("--dry-run", action="store_true", help="올릴 것만 보여 줌")
    pr.add_argument("--list-file", default="", help="GitHub 대신 이 묶음 목록 파일 (trends_batches.json)")
    pr.add_argument("--repo", default="yeomin1024/yeomin1024-ytb")
    pr.add_argument("--branch", default="main")
    pr.add_argument("--skip-install", action="store_true", help="requests 가 없어도 설치하지 않음")
    pr.add_argument("--log-level", default="INFO")
    sub.add_parser("selftest", help="가짜 구글·가짜 GitHub 로 시험")
    a = ap.parse_args(argv)
    if a.cmd == "selftest":
        return selftest()
    return cmd_run(a)


if __name__ == "__main__":
    sys.exit(main())
