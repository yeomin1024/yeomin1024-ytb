#!/usr/bin/env python3
# VERSION: v1.0 — 2026-10-28 — 최초 (사용자 지시 "그럼 대본 받아야하는 목록 정해서 pc 실행하면 저장소에 올리는 코드 알려줘")
# CHANGELOG
#   v1.0 — 2026-10-28 — list(클라우드: 받을 목록 transcript_todo.csv·.md) · run(PC: 자막 → 음성인식 앞 5분 → 전체,
#          대본 두 파일만 GitHub API 로 한 커밋씩) · selftest(가짜 GitHub). 함수: build_list·write_list·GitHub·run_topic·selftest
"""대본 받기 — 목록은 클라우드에서 정하고, 받기·올리기는 PC 에서.

왜: 클라우드는 YouTube 자막 서버가 막고(IpBlocked·ProxyError) 소리를 받을 수 없어 대본이 주식 723개 중 39개뿐
    (content_analysis.xlsx '대본' 칸이 약함). PC 웹 화면의 음성인식은 켜면 PC 결과로 GitHub 사례 폴더를 통째로 바꿈
    (CLAUDE.md '분석') → 이 도구는 영상마다 대본 두 파일(transcript.json·transcript.txt)만 더하고 다른 파일은 건드리지 않는다.

  클라우드(Claude)  python3 tools/pc_transcribe.py list stock      → stock/result/outliers/transcript_todo.csv · transcript_todo.md
  PC(사용자)        powershell -ExecutionPolicy Bypass -File run_analyzer.ps1 -Transcribe -Folder stock
                    (= .venv\\Scripts\\python.exe tools/pc_transcribe.py run stock · 시험 삼아 몇 개만: … -Transcribe -Folder stock --limit 5)
  시험              python3 tools/pc_transcribe.py selftest      (가짜 GitHub·가짜 저장소 이름 — 진짜로 올리지 않음)

목록 순서 (list): 한국어 영상 먼저 — ① 성공 사례 → ② 성공 쇼츠 → ③ 하루 조회수 상위 → ④ 조회수 상위 → ⑤ 그 밖 승인 롱폼 → ⑥ 그 밖 쇼츠,
    그다음 외국 영상을 같은 순서로 (외국 사례로 한국어 규칙을 만들지 않으므로 — CLAUDE.md). 대본이 끝까지 있으면 뺌, 앞 5분만 있으면 '2차'.

run 이 하는 일 (언어마다 ① 모든 묶음 → ② 모든 묶음 → ③ 모든 묶음, 묶음은 목록 순서대로):
  ① 자막 (youtube-transcript-api, 할당량 0 — outlier_research.transcript 그대로: 요청 사이 1.5~3초, 연속 2번 막히면 6시간 자막 쉼)
  ② 자막이 없거나 막힌 영상 = 음성인식 1차 앞 5분 (소리만 받아 Whisper — 분석기 --whisper-queue 와 같은 함수, 소리 파일은 바로 지움.
     쇼츠는 끝까지) ③ 음성인식 2차 = 1차 영상을 끝까지.
  올리기: GitHub API 로 <주제>/result/outliers/W_<id>/ (쇼츠 shorts/S_<id>/) 의 대본 두 파일만, 20개(또는 10분)마다 한 커밋.
          그 사이 main 이 바뀌었으면 새 main 위에 다시 커밋 (= pull --rebase, 강제 푸시 없음). 다른 경로는 코드가 거부.
  이어서: 다시 실행하면 .yt_work/transcribe_<주제>.json 과 GitHub 에 이미 있는 대본을 보고 남은 것만. Ctrl+C 로 멈추면 받은 것부터 올림.
※ 연구·교육용 분석 자료 — 다른 사람의 영상 파일은 받지도 올리지도 않음 (소리는 음성인식 뒤 바로 지움).
"""
import argparse
import ast
import csv
import importlib.util
import io
import json
import logging
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import types
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VERSION = "v1.0"
LOG = logging.getLogger("transcribe")
TOPIC_RX = re.compile(r"^[a-z][a-z0-9_-]{1,30}$")
VID_RX = re.compile(r"^[0-9A-Za-z_-]{11}$")
LIST_NAME = "transcript_todo"
FIRST_SEC = 300                      # 음성인식 1차 = 앞 5분 (분석기 WHISPER_QUEUE_FIRST_SEC 와 같음 — CLAUDE.md '1차 앞 5분 → 2차 전체')
MAX_ATTEMPTS = 3                     # 같은 영상·같은 단계 시도 한도 (분석기 WHISPER_QUEUE_MAX_ATTEMPTS 와 같음)
PUSH_EVERY = 20                      # 대본 이만큼 모이면 한 커밋
PUSH_EVERY_MIN = 10                  # 또는 이 분마다
COMMIT_MAX_BYTES = 3_000_000         # 한 커밋(트리 요청)에 넣는 글자 양 상한 — 넘으면 나눠 커밋
GROUPS = [("success", "성공 사례"), ("shorts_success", "성공 쇼츠"), ("vpd", "하루 조회수 상위"), ("views", "조회수 상위"),
          ("other", "그 밖 승인"), ("shorts_other", "그 밖 쇼츠")]
GROUP_NAME = dict(GROUPS)
GROUP_RANK = {k: i for i, (k, _) in enumerate(GROUPS)}
CSV_COLS = ["rank", "group", "group_name", "lang", "id", "minutes", "need", "score", "title", "folder"]


def log(stage, level=logging.INFO, **kv):
    LOG.log(level, "[%s] [%s] %s", stage, datetime.now().isoformat(timespec="seconds"),
            " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) and (' ' in v or not v) else v}" for k, v in kv.items()))


def setup_logging(level="INFO", log_file=None):
    root = logging.getLogger()                       # outlier_research 의 'outlier' 로그(자막 막힘 등)도 같은 곳으로
    for h in root.handlers[:]:
        root.removeHandler(h)
    root.setLevel(getattr(logging, str(level).upper(), logging.INFO))
    fmt = logging.Formatter("%(message)s")
    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(fmt)
    root.addHandler(sh)
    if log_file:
        Path(log_file).parent.mkdir(parents=True, exist_ok=True)
        fh = logging.FileHandler(log_file, encoding="utf-8")
        fh.setFormatter(fmt)
        root.addHandler(fh)


def check_topic(topic):
    if not TOPIC_RX.match(topic or ""):
        raise SystemExit(f"[SETUP] ❌ 주제 이름이 이상함: {topic!r} (예: stock)")
    return topic


def allowed_path(topic):
    """올려도 되는 경로 — 이 주제 사례 폴더의 대본 두 파일만 (코드가 다른 경로를 거부)."""
    return re.compile(rf"^{re.escape(topic)}/result/outliers/(?:W_|shorts/S_)[0-9A-Za-z_-]{{11}}/transcript\.(?:json|txt)$")


# ============================================================================ list (클라우드)
def _read_json(p, default=None):
    try:
        return json.loads(Path(p).read_text("utf-8"))
    except (OSError, ValueError):
        return default


def _transcript_state(d):
    """사례 폴더 대본 상태 → 'full'(끝까지 있음 — 뺌) · 'partial'(앞부분만 — 2차) · 'none'."""
    tj = d / "transcript.json"
    if not tj.is_file():
        return "none"
    j = _read_json(tj, {}) or {}
    if j.get("partial_sec"):
        return "partial"
    return "full" if (j.get("snippets") or j.get("no_speech")) else "none"


def build_list(topic, base=ROOT):
    """→ (받을 목록 [dict], 셈 {}) — 성공 사례·하루 조회수 상위·조회수 상위 목록은 analysis.json (분석 결과) 그대로."""
    od = Path(base) / topic / "result" / "outliers"
    a = _read_json(od / "analysis.json", {}) or {}
    sa = _read_json(od / "shorts" / "analysis.json", {}) or {}
    succ = {x["id"]: x for x in a.get("success_cases") or []}
    vpd = {x["id"]: x for x in (a.get("vpd_top") or {}).get("cases") or [] if x["id"] not in succ}
    views = {x["id"]: x for x in (a.get("views_top") or {}).get("cases") or [] if x["id"] not in succ and x["id"] not in vpd}
    s_succ = {x["id"]: x for x in sa.get("success_cases") or []}
    s_excl = {x["id"]: x.get("exclude") for x in sa.get("approved") or [] if x.get("exclude")}
    rows, seen = [], {"full": 0, "excluded": 0, "folders": 0}
    folders = [(d, False) for d in sorted(od.glob("W_*"))] + [(d, True) for d in sorted((od / "shorts").glob("S_*"))]
    for d, short in folders:
        if not d.is_dir() or not VID_RX.match(d.name[2:]):
            continue
        seen["folders"] += 1
        vid = d.name[2:]
        meta = _read_json(d / "metadata.json", {}) or {}
        if short and vid in s_excl:                       # 조회수 부풀림 의심·주제 밖 쇼츠 (shorts 분석 규칙) — 대본 필요 없음
            seen["excluded"] += 1
            continue
        state = _transcript_state(d)
        if state == "full":
            seen["full"] += 1
            continue
        if short:
            grp = "shorts_success" if vid in s_succ else "shorts_other"
        else:
            grp = "success" if vid in succ else "vpd" if vid in vpd else "views" if vid in views else "other"
        src = (s_succ if short else succ).get(vid) or vpd.get(vid) or views.get(vid) or {}
        vpd_v = float(meta.get("views_per_day") or src.get("views_per_day") or 0)
        if grp in ("success", "shorts_success"):
            score, sort2 = f"#{src.get('no')}", float(src.get("no") or 10 ** 6)          # 성공 사례 번호 순
        elif grp == "views":
            score, sort2 = f"조회수 {int(meta.get('views') or src.get('views') or 0)}", -float(meta.get("views") or src.get("views") or 0)
        else:
            score, sort2 = f"하루 {vpd_v:.0f}", -vpd_v
        sec = float(meta.get("seconds") or 0) or float(meta.get("minutes") or src.get("minutes") or 0) * 60
        foreign = bool(meta["foreign"]) if "foreign" in meta else bool(src.get("foreign"))
        rows.append({"group": grp, "group_name": GROUP_NAME[grp], "lang": "외국" if foreign else "한국어", "id": vid,
                     "minutes": round(sec / 60, 1), "need": "2차" if state == "partial" else "전체", "score": score,
                     "title": str(meta.get("title") or src.get("title") or "")[:50].replace("\n", " "),
                     "folder": d.relative_to(Path(base)).as_posix(), "_sort": (1 if foreign else 0, GROUP_RANK[grp], sort2, vid)})
    rows.sort(key=lambda r: r["_sort"])
    for i, r in enumerate(rows, 1):
        r["rank"] = i
        del r["_sort"]
    return rows, seen


def write_list(topic, rows, seen, base=ROOT):
    od = Path(base) / topic / "result" / "outliers"
    with open(od / f"{LIST_NAME}.csv", "w", encoding="utf-8-sig", newline="") as f:      # 엑셀에서 한글이 깨지지 않게 BOM
        w = csv.DictWriter(f, fieldnames=CSV_COLS)
        w.writeheader()
        w.writerows(rows)
    agg = {}
    for r in rows:
        k = (r["lang"], r["group"])
        x = agg.setdefault(k, {"n": 0, "full": 0, "second": 0, "min": 0.0, "first_min": 0.0, "first": r["rank"], "last": r["rank"]})
        x["n"] += 1
        x["full" if r["need"] == "전체" else "second"] += 1
        x["min"] += r["minutes"]
        if r["need"] == "전체":                             # 1차 = 앞 5분 (쇼츠는 끝까지)
            x["first_min"] += r["minutes"] if r["group"].startswith("shorts") else min(r["minutes"], FIRST_SEC / 60)
        x["last"] = r["rank"]
    L = [f"# 대본 받을 목록 — {topic} ({datetime.now():%Y-%m-%d}, tools/pc_transcribe.py {VERSION})", "",
         "※ 숫자만. 순서·영상은 `transcript_todo.csv` (PC 가 이 순서대로 받음). 다시 만들기: `python3 tools/pc_transcribe.py list " + topic + "`", "",
         f"- 사례 폴더 {seen['folders']}개 중 대본이 끝까지 있는 {seen['full']}개 · 뺀 쇼츠(부풀림 의심·주제 밖) {seen['excluded']}개를 빼고 **{len(rows)}개**",
         "- 할 일: '전체' = 대본 없음 (자막 → 없으면 음성인식 앞 5분 → 끝까지) · '2차' = 앞 5분만 있음 (음성인식으로 끝까지)", "",
         "| 순서 | 언어 | 묶음 | 영상 | 전체 | 2차 | 1차 소리(분) | 전체 소리(분) |", "|---|---|---|---:|---:|---:|---:|---:|"]
    for (lang, grp), x in sorted(agg.items(), key=lambda kv: kv[1]["first"]):
        L.append(f"| {x['first']}~{x['last']} | {lang} | {GROUP_NAME[grp]} | {x['n']} | {x['full']} | {x['second']} | {x['first_min']:,.0f} | {x['min']:,.0f} |")
    tot = sum(r["minutes"] for r in rows)
    tot1 = sum(x["first_min"] for x in agg.values())
    L += [f"| | | **합계** | **{len(rows)}** | {sum(1 for r in rows if r['need'] == '전체')} | {sum(1 for r in rows if r['need'] == '2차')} | **{tot1:,.0f}** | **{tot:,.0f}** |", "",
          "- 1차 소리 = 음성인식 1차에 들어가는 소리 (영상마다 앞 5분, 쇼츠는 끝까지 · '2차' 줄은 0) — 자막을 받은 영상은 음성인식을 하지 않으므로 **자막이 모두 막혔을 때의 최대**.",
          "- 걸리는 시간 (최대, 짐작): 소리 1분에 약 1분으로 잡음 (2026-10-14 사용자 PC 기록 '영상 하나 10분 안팎' — Whisper small·CPU) → 한국어 1차 약 "
          f"{sum(x['first_min'] for (lg, _), x in agg.items() if lg == '한국어') / 60:,.0f}시간 · 한국어 전체 약 {sum(x['min'] for (lg, _), x in agg.items() if lg == '한국어') / 60:,.0f}시간. "
          "NVIDIA GPU 가 있으면 몇 배 빠름 (`--model medium` 도 됨).", "",
          "## PC 에서 (사용자)",
          "```",
          f"powershell -ExecutionPolicy Bypass -File run_analyzer.ps1 -Transcribe -Folder {topic}",
          "```",
          "- 차례: 언어마다(한국어 → 외국) ① 자막을 모든 묶음에 (영상 하나 몇 초) → ② 자막이 없거나 막힌 영상만 음성인식 앞 5분 → ③ 끝까지. 묶음은 위 표 순서.",
          "- 20개(또는 10분)마다 대본 파일만 main 에 올림 · 멈췄다 다시 실행하면 이어서 · 끝나면 Claude 에게 \"대본 올렸어\" → 콘텐츠 분석 다시.", ""]
    (od / f"{LIST_NAME}.md").write_text("\n".join(L), "utf-8")
    log("LIST", topic=topic, items=len(rows), need_full=sum(1 for r in rows if r["need"] == "전체"),
        need_second=sum(1 for r in rows if r["need"] == "2차"), audio_min=round(tot), folders=seen["folders"], have_full=seen["full"],
        shorts_excluded=seen["excluded"], csv=f"{topic}/result/outliers/{LIST_NAME}.csv")
    return od / f"{LIST_NAME}.csv"


# ============================================================================ GitHub (PC — 대본 파일만)
class GitHub:
    """GitHub Git Data API — 트리에 대본 파일만 더한 커밋을 main 에 (빠른 감기만, 강제 푸시 없음). 토큰은 머리글로만, 화면에 쓰지 않음."""
    API = "https://api.github.com"

    def __init__(self, repo, branch, token, topic, session=None, dry_run=False, sleep=time.sleep):
        if session is None:
            import requests
            session = requests.Session()
        self.s, self.repo, self.branch, self.dry_run, self.sleep = session, repo, branch, dry_run, sleep
        self.allowed = allowed_path(topic)
        self.h = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28",
                  **({"Authorization": f"Bearer {token}"} if token else {})}    # 토큰 없으면 읽기만 (공개 저장소)

    def req(self, method, path, ok=(200, 201), **kw):
        """네트워크 오류·5xx·속도 제한은 2·4·8·16초 쉬고 다시. 그 밖의 응답(422 등)은 부르는 쪽으로."""
        err = "-"
        for wait in (0, 2, 4, 8, 16):
            if wait:
                self.sleep(wait)
            try:
                r = self.s.request(method, f"{self.API}/repos/{self.repo}{path}", headers=self.h, timeout=60, **kw)
            except Exception as e:                         # 연결 끊김 등
                err = f"{type(e).__name__}: {str(e)[:120]}"
                continue
            if r.status_code in ok:
                return r
            limited = r.status_code == 429 or (r.status_code == 403 and "rate limit" in (r.text or "").lower())
            if r.status_code >= 500 or limited:
                err = f"HTTP {r.status_code}"
                if limited:
                    self.sleep(min(120, int(r.headers.get("Retry-After") or 30)))
                continue
            return r
        raise RuntimeError(f"GitHub {method} {path} 실패 (5번 시도): {err}")

    def _ok(self, r, what):
        if r.status_code not in (200, 201):
            hint = (" → 토큰 권한 확인: Fine-grained 토큰 · 저장소 yeomin1024-ytb · Contents: Read and write (guides/pc_analysis.md)"
                    if r.status_code in (401, 403, 404) else "")
            raise RuntimeError(f"GitHub {what} 실패: HTTP {r.status_code} {(r.text or '')[:200]}{hint}")
        return r.json()

    def head(self):
        return self._ok(self.req("GET", f"/git/ref/heads/{self.branch}"), "브랜치 읽기")["object"]["sha"]

    def read_text(self, path):
        r = self.req("GET", f"/contents/{path}", params={"ref": self.branch}, ok=(200,))
        j = self._ok(r, f"파일 읽기 {path}")
        if j.get("content"):
            import base64
            return base64.b64decode(j["content"]).decode("utf-8-sig")
        if j.get("download_url"):                          # 1MB 넘는 파일 — 받기 주소로
            return self.s.request("GET", j["download_url"], headers=self.h, timeout=60).content.decode("utf-8-sig")
        raise RuntimeError(f"GitHub 파일 내용 없음: {path}")

    def existing_transcripts(self, prefix):
        """GitHub 에 이미 있는 대본(transcript.json) 경로 집합 — prefix(<주제>/result/outliers) 아래만 훑음."""
        tree = self._ok(self.req("GET", f"/git/commits/{self.head()}"), "커밋 읽기")["tree"]["sha"]
        for part in prefix.split("/"):
            ents = self._ok(self.req("GET", f"/git/trees/{tree}"), "트리 읽기")["tree"]
            nxt = next((e for e in ents if e["path"] == part and e["type"] == "tree"), None)
            if nxt is None:
                return set(), False
            tree = nxt["sha"]
        j = self._ok(self.req("GET", f"/git/trees/{tree}", params={"recursive": "1"}), "트리 읽기")
        return {f"{prefix}/{e['path']}" for e in j.get("tree") or [] if e["path"].endswith("/transcript.json")}, bool(j.get("truncated"))

    def commit(self, files, message):
        """files {경로: 글} → 커밋 sha (dry_run 이면 None). main 이 그 사이 바뀌면(422) 새 main 위에 다시 — 최대 5번."""
        bad = [p for p in files if not self.allowed.match(p)]
        if bad:
            raise ValueError(f"대본 파일이 아닌 경로는 올리지 않음: {bad[:3]}")
        if self.dry_run:
            log("PUSH", files=len(files), dry_run=True, first=next(iter(files), "-"))
            return None
        entries = [{"path": p, "mode": "100644", "type": "blob", "content": t} for p, t in sorted(files.items())]
        for attempt in range(1, 6):
            head = self.head()
            base_tree = self._ok(self.req("GET", f"/git/commits/{head}"), "커밋 읽기")["tree"]["sha"]
            tree = self._ok(self.req("POST", "/git/trees", json={"base_tree": base_tree, "tree": entries}), "트리 만들기")["sha"]
            new = self._ok(self.req("POST", "/git/commits", json={"message": message, "tree": tree, "parents": [head]}), "커밋 만들기")["sha"]
            r = self.req("PATCH", f"/git/refs/heads/{self.branch}", json={"sha": new, "force": False})
            if r.status_code in (200, 201):
                return new
            if r.status_code == 422:                       # 빠른 감기가 아님 = 그 사이 다른 커밋 → 새 main 위에 다시 (pull --rebase 와 같음)
                log("PUSH", logging.WARNING, note="main 이 그 사이 바뀜 → 새 main 위에 다시 커밋", attempt=attempt)
                self.sleep(2 ** attempt)
                continue
            self._ok(r, "브랜치 옮기기")
        raise RuntimeError("main 이 계속 바뀌어 5번 모두 실패 — 잠시 뒤 다시 실행 (받은 대본은 .yt_work 에 남아 다음에 올라감)")


# ============================================================================ run (PC)
def analyzer_packages():
    """분석기(youtube_topic_analyzer.py)의 REQUIRED_PACKAGES·OPTIONAL_PACKAGES 를 읽기만 (import 전에 — 패키지 목록이 한 곳에만 있게)."""
    tree = ast.parse((ROOT / "youtube_topic_analyzer.py").read_text("utf-8"))
    req, opt = [], []
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            if node.targets[0].id == "REQUIRED_PACKAGES":
                req = list(ast.literal_eval(node.value))
            elif node.targets[0].id == "OPTIONAL_PACKAGES":
                opt = list(ast.literal_eval(node.value))
    if sys.version_info < (3, 11):
        req.append(("tomli", "tomli>=2.0"))
    return req, opt


def ensure_packages(install=True):
    """필요한 패키지 (분석기와 같은 목록 + faster-whisper). 없으면 pip 으로 설치 · yt-dlp 는 하루 한 번 최신으로 (YouTube 변경 대응)."""
    req, opt = analyzer_packages()
    missing = [pip for mod, pip in req if importlib.util.find_spec(mod) is None]
    optional = [pip for mod, pip in opt if importlib.util.find_spec(mod) is None]      # faster-whisper — 없으면 자막만
    if missing:
        if not install:
            raise SystemExit(f"[SETUP] ❌ 패키지가 없음 → python -m pip install -U {' '.join(missing)}")
        log("SETUP", note="패키지 설치 (처음 한 번, 몇 분)", packages=",".join(missing))
        if subprocess.run([sys.executable, "-m", "pip", "install", "-U", *missing]).returncode != 0:
            raise SystemExit("[SETUP] ❌ 패키지 설치 실패 → 위 오류 확인 (가상환경 .venv 권장 — run_analyzer.ps1 이 만듦)")
    if optional and install:
        log("SETUP", note="음성인식 패키지 설치 (처음 한 번)", packages=",".join(optional))
        if subprocess.run([sys.executable, "-m", "pip", "install", "-U", *optional]).returncode != 0:
            log("SETUP", logging.WARNING, note="faster-whisper 설치 실패 → 자막만 받음 (음성인식은 설치를 고친 뒤 다시 실행)")
    stamp = ROOT / ".yt_work" / "ytdlp_update.stamp"            # 분석기와 같은 표시 파일
    if install and (not stamp.exists() or time.time() - stamp.stat().st_mtime > 86400):
        if subprocess.run([sys.executable, "-m", "pip", "install", "-U", "-q", "yt-dlp[default]"]).returncode == 0:
            stamp.parent.mkdir(parents=True, exist_ok=True)
            stamp.write_text(time.strftime("%Y-%m-%d %H:%M:%S"), "utf-8")
    importlib.invalidate_caches()


def transcript_files(tj):
    """transcript.json 내용 → (json 글, txt 글) — outlier_research(자막)·분석기 대기열(음성인식)과 같은 꼴."""
    snips = tj.get("snippets") or []
    head = f"[앞 {tj['partial_sec'] // 60}분만 — 전체는 2차 음성인식에서]\n" if tj.get("partial_sec") else ""
    return (json.dumps(tj, ensure_ascii=False),
            head + "\n".join(f"[{float(x['start']):7.1f}] {x['text']}" for x in snips))


BLOCK_WORDS = ("Blocked", "429", "TooManyRequests")
ENV_ERRORS = ("faster-whisper 없음", "ffmpeg 없음", "No module named", "ModuleNotFoundError")   # PC 준비 문제 (영상 탓 아님)


def want_caption(st):
    """자막을 (다시) 요청할까: 2번까지 — '자막 없음'은 다시 안 함, 서버가 막았던 것·연결 실패만 다시."""
    if st["caption"] >= 2:
        return False
    return st.get("caption_result") != "whisper" or any(w in (st.get("error") or "") for w in BLOCK_WORDS)


def want_whisper(st):
    """음성인식으로 갈까: 자막이 없거나 막힘 · 연결 실패가 2번 이어진 영상도 (자막 서버만 안 될 수 있음)."""
    return st.get("caption_result") == "whisper" or (st.get("caption_result") == "network" and st["caption"] >= 2)


class Runner:
    """한 주제의 목록을 묶음마다 ①자막 ②음성인식 1차 ③2차 — 받은 대본은 .yt_work 에 모았다가 GitHub 에 (대본 파일만)."""

    def __init__(self, topic, rows, gh, caption, whisper, work, opts, existing=frozenset(), now=time.monotonic):
        self.topic, self.rows, self.gh, self.caption, self.whisper, self.opts, self.now = topic, rows, gh, caption, whisper, opts, now
        self.work = Path(work)
        self.state_p = self.work / f"transcribe_{topic}.json"
        self.pending = self.work / "transcribe" / topic / "pending"
        self.sent = self.work / "transcribe" / topic / "sent"
        st = _read_json(self.state_p, {}) or {}
        self.state = st.get("items") or {}
        self.existing = existing
        self.whisper_off = None                            # 음성인식을 못 쓰게 된 까닭 (패키지 없음·봇 확인 반복)
        self.totals = {"caption": 0, "whisper1": 0, "whisper2": 0, "no_speech": 0, "failed": 0, "network": 0, "skipped_remote": 0,
                       "commits": 0, "files_pushed": 0, "whisper_audio_min": 0.0}
        self.last_push = self.now()

    # ---- 상태·파일
    def save(self):
        self.state_p.parent.mkdir(parents=True, exist_ok=True)
        self.state_p.write_text(json.dumps({"tool": f"pc_transcribe {VERSION}", "items": self.state}, ensure_ascii=False, indent=1), "utf-8")

    def rec(self, vid):
        return self.state.setdefault(vid, {"done": None, "caption": 0, "w1": 0, "w2": 0})

    def stage(self, row, tj):
        tj = {**tj, "by": f"pc_transcribe {VERSION}", "collected": datetime.now().isoformat(timespec="seconds")}
        js, txt = transcript_files(tj)
        for name, body in (("transcript.json", js), ("transcript.txt", txt)):
            p = self.pending / row["folder"] / name
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(body, "utf-8")

    def pending_files(self):
        if not self.pending.is_dir():
            return {}
        return {p.relative_to(self.pending).as_posix(): p.read_text("utf-8") for p in sorted(self.pending.rglob("transcript.*")) if p.is_file()}

    def push(self, why, force=False):
        files = self.pending_files()
        n_vid = len({Path(p).parent.as_posix() for p in files})
        if not files or (not force and n_vid < self.opts.push_every and self.now() - self.last_push < self.opts.push_min * 60):
            return
        if self.opts.no_push or self.gh is None:
            log("PUSH", note="올리지 않고 .yt_work 에 둠 (--no-push 또는 토큰 없음 — 다음에 토큰과 함께 실행하면 먼저 올림)", videos=n_vid,
                folder=self.pending.as_posix())
            self.last_push = self.now()
            return
        chunks, cur, size = [], {}, 0
        for p, t in files.items():                          # 한 커밋이 너무 크지 않게 나눔
            b = len(t.encode("utf-8"))
            if cur and size + b > COMMIT_MAX_BYTES:
                chunks.append(cur)
                cur, size = {}, 0
            cur[p], size = t, size + b
        chunks.append(cur)
        for ch in chunks:
            n = len({Path(p).parent.as_posix() for p in ch})
            sha = self.gh.commit(ch, f"[{self.topic} 대본] {why} — 영상 {n}개 (tools/pc_transcribe.py {VERSION}, PC)")
            if sha is None:                                 # --dry-run: 올리지 않았으니 그대로 둠 (다음 실제 실행이 먼저 올림)
                continue
            for p in ch:                                    # 올린 것은 sent/ 로 (PC 에 사본 — 다시 올리지 않음)
                dst = self.sent / p
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(self.pending / p), str(dst))
            for vid in {Path(p).parent.name[2:] for p in ch}:
                self.rec(vid)["pushed"] = True
            self.totals["commits"] += 1
            self.totals["files_pushed"] += len(ch)
            log("PUSH", videos=n, files=len(ch), commit=sha[:10], why=why)
        self.save()
        self.last_push = self.now()

    # ---- 단계
    def do_caption(self, row):
        r = self.rec(row["id"])
        r["caption"] += 1
        snips, lang, status = self.caption(row["id"], row["lang"] == "외국")
        if snips:
            self.stage(row, {"lang": lang, "snippets": snips})
            r.update(done="caption", error=None)
            self.totals["caption"] += 1
            log("CAPTION", id=row["id"], result="ok", lang=lang, snippets=len(snips), group=row["group_name"])
            return
        kind = "network" if any(w in status for w in ("ProxyError", "ConnectionError", "Timeout", "URLError")) else "whisper"
        if "ModuleNotFoundError" in status:
            raise SystemExit(f"[CAPTION] ❌ 자막 패키지가 없음 ({status[:80]}) → 다시 실행하면 설치함")
        r.update(caption_result=kind, error=status[:160])
        if kind == "network":
            self.totals["network"] += 1
        log("CAPTION", logging.INFO if kind == "whisper" else logging.WARNING, id=row["id"], result="음성인식으로" if kind == "whisper"
            else "연결 실패 — 다음 실행에 다시", status=status[:80])

    def do_whisper(self, row, mode):
        r = self.rec(row["id"])
        key = "w1" if mode == "first" else "w2"
        r[key] += 1
        short = row["folder"].split("/")[-1].startswith("S_")
        max_sec = FIRST_SEC if mode == "first" and not short else None
        t0 = time.perf_counter()
        try:
            snips, src_meta = self.whisper(row["id"], float(row["minutes"]) * 60, max_sec, short, row["lang"] == "외국")
            if not snips and not short:
                raise RuntimeError("음성인식 결과가 비어 있음 (말소리 없음?)")
        except Exception as e:
            r["error"] = f"{type(e).__name__}: {str(e)[:200]}"
            if any(w in r["error"] for w in ENV_ERRORS):    # PC 준비 문제 = 영상 탓이 아님 → 시도 횟수를 쓰지 않고 음성인식만 멈춤
                r[key] -= 1
                self.whisper_off = f"음성인식 준비 안 됨 ({r['error'][:80]}) → 다시 실행하면 설치를 다시 시도 (자막은 계속 받음)"
                return
            self.totals["failed"] += 1
            log("WHISPER", logging.WARNING, id=row["id"], result="실패", pass_=mode, attempt=r[key], error=r["error"][:120],
                next="다음 실행" if r[key] < MAX_ATTEMPTS else "포기 (시도 한도)")
            if "BotCheck" in r["error"] or "봇 확인" in r["error"]:
                self.whisper_off = ("봇 확인이 반복됨 → YouTube 에 로그인한 브라우저에서 cookies.txt 를 내보내 이 폴더에 두고 다시 "
                                    "(분석기가 cookies*.txt 를 저절로 씀 · 비밀값이라 GitHub 에 올리지 않음)")
            return
        partial = bool(max_sec) and float(row["minutes"]) * 60 > max_sec + 5
        tj = {"lang": f"{src_meta.get('language') or '-'}(음성인식)", "snippets": snips, "source": src_meta.get("source")}
        if not snips:
            tj["no_speech"] = True
            self.totals["no_speech"] += 1
        if partial:
            tj["partial_sec"] = max_sec
        self.stage(row, tj)
        r.update(done="whisper_partial" if partial else "whisper", error=None)
        self.totals["whisper1" if mode == "first" else "whisper2"] += 1
        self.totals["whisper_audio_min"] += (max_sec or float(row["minutes"]) * 60) / 60
        log("WHISPER", id=row["id"], result="ok", pass_=mode, partial=partial, snippets=len(snips), group=row["group_name"],
            elapsed_sec=round(time.perf_counter() - t0, 1))

    # ---- 묶음
    def run(self):
        """언어마다(한국어 → 외국) ① 자막을 모든 묶음에 → ② 음성인식 1차(앞 5분)를 모든 묶음에 → ③ 2차(끝까지).
        묶음 순서(성공 사례 먼저)는 목록 순서 그대로 — 도입부·초반이 모든 묶음에서 먼저 모이게 (CLAUDE.md '1차 앞 5분 → 2차 전체')."""
        for r in self.rows:                                 # GitHub 에 이미 있는 대본은 건너뜀 (앞 5분만 있는 '2차' 줄은 빼고)
            st = self.rec(r["id"])
            if r["need"] == "전체" and f"{r['folder']}/transcript.json" in self.existing and not st.get("done"):
                st["done"] = "remote"
                self.totals["skipped_remote"] += 1
        self.save()
        self.push("지난 실행에서 못 올린 대본", force=True)
        for lang in dict.fromkeys(r["lang"] for r in self.rows):
            rows = [r for r in self.rows if r["lang"] == lang]
            todo1 = [r for r in rows if r["need"] == "전체" and not self.rec(r["id"]).get("done") and want_caption(self.rec(r["id"]))]
            log("PASS", lang=lang, step="① 자막", items=len(todo1))
            for r in todo1:                                 # ① 자막 (막혔던 영상은 다음 실행에 한 번 더 — 막힘은 6시간 뒤 풀림)
                self.do_caption(r)
                self.save()
                self.push(f"{lang} 자막")
            self.push(f"{lang} 자막 끝", force=True)
            if self.opts.no_whisper or self.whisper_off:
                continue
            todo2 = [r for r in rows if r["need"] == "전체" and not self.rec(r["id"]).get("done") and want_whisper(self.rec(r["id"]))
                     and self.rec(r["id"])["w1"] < MAX_ATTEMPTS]
            log("PASS", lang=lang, step="② 음성인식 1차 (앞 5분 · 쇼츠는 끝까지)", items=len(todo2),
                audio_min=round(sum(min(r["minutes"], FIRST_SEC / 60) if not r["folder"].split("/")[-1].startswith("S_") else r["minutes"]
                                    for r in todo2)))
            for r in todo2:
                self.do_whisper(r, "first")
                self.save()
                self.push(f"{lang} 음성인식 1차")
                if self.whisper_off:
                    break
            self.push(f"{lang} 음성인식 1차 끝", force=True)
            if self.whisper_off:
                continue
            todo3 = [r for r in rows if (self.rec(r["id"]).get("done") == "whisper_partial" or (r["need"] == "2차" and not self.rec(r["id"]).get("done")))
                     and self.rec(r["id"])["w2"] < MAX_ATTEMPTS]
            log("PASS", lang=lang, step="③ 음성인식 2차 (끝까지)", items=len(todo3), audio_min=round(sum(r["minutes"] for r in todo3)))
            for r in todo3:
                self.do_whisper(r, "full")
                self.save()
                self.push(f"{lang} 음성인식 2차")
                if self.whisper_off:
                    break
            self.push(f"{lang} 음성인식 2차 끝", force=True)
        if self.whisper_off:
            log("WHISPER", logging.WARNING, note="음성인식을 멈춤", why=self.whisper_off)
        return self.totals


def make_deps(topic, opts, keys):
    """PC 의 진짜 자막·음성인식 함수 (분석기·outlier_research 그대로)."""
    sys.path.insert(0, str(ROOT))
    sys.path.insert(0, str(ROOT / "tools"))
    import outlier_research as orx
    import youtube_topic_analyzer as y
    y.setup_logging(opts.log_level, None)
    if keys.get("GITHUB_TOKEN"):
        y.register_secret(keys["GITHUB_TOKEN"])
    cfg = y.collect_config(vars(y))
    cfg_p = ROOT / topic / "analyzer_config.toml"
    if cfg_p.is_file():
        y.apply_config_file(cfg, cfg_p)
    if opts.model:
        cfg["WHISPER_MODEL"] = opts.model
    cfg["WHISPER_CPU_MAX_MINUTES"] = 10 ** 6               # 뒤에서 도니까 길이 제한 없음 (분석기 대기열과 같음)
    work = ROOT / ".yt_work"
    ready = {"auth": False}

    def caption(vid, foreign):
        return orx.transcript(vid, any_lang=foreign)

    def whisper(vid, duration_sec, max_sec, short, foreign):
        if importlib.util.find_spec("faster_whisper") is None:
            raise RuntimeError("faster-whisper 없음 → 다시 실행하면 설치함")
        if not ready["auth"]:
            ctx = types.SimpleNamespace(cfg=cfg, work_dir=work, note=lambda stage, msg, **kv: log(stage, logging.WARNING, note=msg, **kv))
            y.refresh_download_auth(ctx, proxy=keys.get("YTDLP_PROXY", ""))
            ready["auth"] = True
        tmp = work / "tmp" / topic / f"transcribe_{vid}"
        tmp.mkdir(parents=True, exist_ok=True)
        try:
            src = y.ytdlp_download(vid, tmp, cfg, audio_only=True)          # 소리만 (영상 파일은 받지 않음)
            segs, meta = y.transcript_via_whisper(src, cfg, duration_sec, max_sec=max_sec, vad_retry=not short, foreign=foreign)
        finally:
            y.rmtree_force(tmp)                                              # 소리 파일은 남기지 않음
        return [{"text": s["text"], "start": s["start"], "duration": s["duration"]} for s in segs], meta

    return y, caption, whisper, cfg


def read_rows(text):
    rows = list(csv.DictReader(io.StringIO(text.lstrip("﻿"))))
    for r in rows:
        r["rank"] = int(r["rank"])
        r["minutes"] = float(r["minutes"] or 0)
    bad = [r for r in rows if not VID_RX.match(r["id"]) or not re.match(r"^[a-z0-9_-]+/result/outliers/(W_|shorts/S_)", r["folder"])]
    if bad:
        raise SystemExit(f"[LIST] ❌ 목록에 이상한 줄 {len(bad)}개 (예: {bad[0]['id']!r}) — 클라우드에서 list 를 다시 만들어 달라고 하세요")
    return sorted(rows, key=lambda r: r["rank"])


def cmd_run(opts):
    work = ROOT / ".yt_work"
    for topic in opts.topics:
        check_topic(topic)
        setup_logging(opts.log_level, work / f"transcribe_log_{topic}.txt")
        t0 = time.perf_counter()
        ensure_packages(install=not opts.skip_install)
        sys.path.insert(0, str(ROOT))
        import youtube_topic_analyzer as y
        keys = y.load_keys(require_youtube=False, topic_dir=ROOT / topic)     # 값은 가려서 보여 줌
        token = keys.get("GITHUB_TOKEN") or ""
        if not token and not (opts.no_push or opts.dry_run):
            raise SystemExit("[SETUP] ❌ GITHUB_TOKEN 이 없음 → .env 에 넣고 다시 (또는 --no-push 로 PC 에만 받기)")
        y, caption, whisper, cfg = make_deps(topic, opts, keys)
        setup_logging(opts.log_level, work / f"transcribe_log_{topic}.txt")  # 분석기 로그 설정 뒤 다시 (내 로그도 파일로)
        gh = GitHub(opts.repo, opts.branch, token, topic, dry_run=opts.dry_run) if token else None    # 토큰 없음 = PC 에만
        list_path = f"{topic}/result/outliers/{LIST_NAME}.csv"
        if opts.list_file:
            text = Path(opts.list_file).read_text("utf-8-sig")
        elif gh:
            text = gh.read_text(list_path)
        else:
            import requests
            url = f"https://raw.githubusercontent.com/{opts.repo}/{opts.branch}/{list_path}"
            try:
                resp = requests.get(url, timeout=60)
                resp.raise_for_status()
            except Exception as e:
                raise SystemExit(f"[LIST] ❌ 목록을 못 받음: {url} ({type(e).__name__}: {str(e)[:120]}) → 인터넷 연결 확인, "
                                 f"목록이 없으면 Claude 에게 'pc_transcribe list {topic}'") from None
            text = resp.content.decode("utf-8-sig")
        rows = read_rows(text)
        if opts.korean_only:
            rows = [r for r in rows if r["lang"] == "한국어"]
        if opts.groups:
            keep = set(opts.groups.split(","))
            rows = [r for r in rows if r["group"] in keep]
        existing, truncated = (gh.existing_transcripts(f"{topic}/result/outliers") if gh else (set(), False))
        if truncated:
            log("GITHUB", logging.WARNING, note="트리 목록이 잘림 — 이미 있는 대본을 다 못 봄 (목록 기준으로 진행)")
        runner = Runner(topic, rows, gh, caption, whisper, work, opts, existing=frozenset(existing))
        if opts.limit:
            left = [r for r in rows if not runner.rec(r["id"]).get("done")
                    and (r["need"] == "2차" or f"{r['folder']}/transcript.json" not in existing)]   # '2차' 는 앞 5분 대본이 이미 있음
            runner.rows = left[:opts.limit]
        log("RUN", topic=topic, list=len(rows), this_run=len(runner.rows), already_on_github=len(existing), model=cfg["WHISPER_MODEL"],
            first_sec=FIRST_SEC, push_every=opts.push_every, no_whisper=opts.no_whisper, dry_run=opts.dry_run, repo=opts.repo)
        try:
            tot = runner.run()
        except KeyboardInterrupt:
            log("RUN", logging.WARNING, note="Ctrl+C — 받은 대본부터 올리고 끝냄 (다시 실행하면 이어서)")
            runner.push("멈춤 전까지", force=True)
            raise SystemExit(130)
        except Exception as e:
            log("RUN", logging.ERROR, error=f"{type(e).__name__}: {str(e)[:200]}",
                next="받은 대본부터 올리고 멈춤 — 다시 실행하면 이어서, 같은 오류가 또 나면 이 줄을 Claude 에게")
            runner.save()
            runner.push("오류 전까지", force=True)
            raise
        done = sum(1 for r in rows if runner.rec(r["id"]).get("done") in ("caption", "whisper", "remote"))
        left = sum(1 for r in rows if runner.rec(r["id"]).get("done") in (None, "whisper_partial"))
        log("SUMMARY", topic=topic, **{k: (round(v) if isinstance(v, float) else v) for k, v in tot.items()}, list_done=done, list_left=left,
            elapsed_min=round((time.perf_counter() - t0) / 60, 1),
            next="클라우드 Claude 에게 \"대본 올렸어\" → 콘텐츠 분석·성공 사례 분석 다시" if tot["commits"] else "-")
    return 0


def cmd_list(opts):
    setup_logging(opts.log_level)
    for topic in opts.topics:
        t0 = time.perf_counter()
        rows, seen = build_list(check_topic(topic))
        write_list(topic, rows, seen)
        log("LIST", topic=topic, elapsed_sec=round(time.perf_counter() - t0, 2))
    return 0


# ============================================================================ selftest (가짜 GitHub — 진짜로 올리지 않음)
class _Resp:
    def __init__(self, code, body=None, text=""):
        self.status_code, self._b, self.text, self.headers = code, body or {}, text or json.dumps(body or {}), {}
        self.content = self.text.encode("utf-8")

    def json(self):
        return self._b


class _FakeGitHub:
    """Git Data API 흉내: 첫 브랜치 옮기기는 422(그 사이 다른 커밋) → 다시 하면 성공. 받은 트리 항목을 모아 둠."""

    def __init__(self, files=None, existing=()):
        self.head, self.n, self.trees, self.calls, self.refused, self.commits, self.patches = "c0", 0, [], [], 1, [], []
        self.files = files or {}
        self.existing = list(existing)

    def request(self, method, url, headers=None, timeout=None, params=None, json=None):
        path = url.split("/repos/fake-owner/fake-repo", 1)[1]
        self.calls.append((method, path))
        if method == "GET" and path.startswith("/git/ref/heads/"):
            return _Resp(200, {"object": {"sha": self.head}})
        if method == "GET" and path.startswith("/git/commits/"):
            return _Resp(200, {"tree": {"sha": "t-root"}})
        if method == "GET" and path.startswith("/git/trees/"):
            sha = path.rsplit("/", 1)[1]
            nxt = {"t-root": ("demo", "t-demo"), "t-demo": ("result", "t-res"), "t-res": ("outliers", "t-out")}
            if sha in nxt:
                return _Resp(200, {"tree": [{"path": nxt[sha][0], "type": "tree", "sha": nxt[sha][1]}]})
            return _Resp(200, {"tree": [{"path": p, "type": "blob"} for p in self.existing], "truncated": False})
        if method == "GET" and path.startswith("/contents/"):
            import base64
            return _Resp(200, {"content": base64.b64encode(self.files[path[len("/contents/"):]].encode("utf-8")).decode()})
        if method == "POST" and path == "/git/trees":
            self.trees.append(json)
            return _Resp(201, {"sha": f"t{len(self.trees)}"})
        if method == "POST" and path == "/git/commits":
            self.n += 1
            self.commits.append(json)
            return _Resp(201, {"sha": f"c{self.n}"})
        if method == "PATCH":
            self.patches.append(json)
            if self.refused:
                self.refused -= 1
                self.head = "c-other"                      # 다른 세션이 그 사이 올림
                return _Resp(422, {"message": "Update is not a fast forward"})
            self.head = json["sha"]
            return _Resp(200, {"object": {"sha": json["sha"]}})
        return _Resp(404, {"message": "not found"})


def selftest():
    setup_logging("WARNING")
    for k in list(os.environ):                              # CLAUDE.md: 푸시할 수 있는 도구 시험 = 토큰 환경 변수 지우고 가짜 저장소
        if "TOKEN" in k.upper() or k.upper().startswith("GH_"):
            os.environ.pop(k, None)
    ok = True

    def check(name, cond, **kv):
        nonlocal ok
        ok &= bool(cond)
        print(f"[SELFTEST] {'✅' if cond else '❌'} {name}" + (" " + " ".join(f"{k}={v}" for k, v in kv.items()) if kv else ""))

    def case(d, meta, tj=None):
        d.mkdir(parents=True)
        (d / "metadata.json").write_text(json.dumps(meta), "utf-8")
        if tj is not None:
            (d / "transcript.json").write_text(json.dumps(tj), "utf-8")

    with tempfile.TemporaryDirectory() as td:
        base = Path(td)
        od = base / "demo" / "result" / "outliers"
        ids = {k: f"{k:_<11}"[:11] for k in ("succ1", "succ2", "vpd1", "vpd2", "for1", "oth1", "full1", "part1", "shs1", "shx1")}
        case(od / f"W_{ids['succ1']}", {"title": "성공1", "minutes": 12, "views_per_day": 10})
        case(od / f"W_{ids['succ2']}", {"title": "성공2 짧음", "minutes": 3, "views_per_day": 99})
        case(od / f"W_{ids['vpd1']}", {"title": "하루1", "minutes": 20, "views_per_day": 500})
        case(od / f"W_{ids['vpd2']}", {"title": "하루2", "minutes": 20, "views_per_day": 900})
        case(od / f"W_{ids['for1']}", {"title": "foreign", "minutes": 10, "views_per_day": 5000, "foreign": True})
        case(od / f"W_{ids['oth1']}", {"title": "그밖", "minutes": 8, "views_per_day": 1})
        case(od / f"W_{ids['full1']}", {"title": "끝까지", "minutes": 8}, {"lang": "ko", "snippets": [{"text": "a", "start": 0, "duration": 1}]})
        case(od / f"W_{ids['part1']}", {"title": "앞5분", "minutes": 30}, {"lang": "ko(음성인식)", "snippets": [], "partial_sec": 300})
        case(od / "shorts" / f"S_{ids['shs1']}", {"title": "쇼츠", "seconds": 50})
        case(od / "shorts" / f"S_{ids['shx1']}", {"title": "뺀 쇼츠", "seconds": 40})
        (od / "analysis.json").write_text(json.dumps({
            "success_cases": [{"id": ids["succ2"], "no": 1}, {"id": ids["succ1"], "no": 2}, {"id": ids["part1"], "no": 3}],
            "vpd_top": {"cases": [{"id": ids["vpd1"]}, {"id": ids["vpd2"]}, {"id": ids["succ1"]}, {"id": ids["for1"]}]},
            "views_top": {"cases": []}}), "utf-8")
        (od / "shorts" / "analysis.json").write_text(json.dumps({"success_cases": [{"id": ids["shs1"], "no": 1}],
                                                                 "approved": [{"id": ids["shx1"], "exclude": "조회수 부풀림 의심"}]}), "utf-8")
        rows, seen = build_list("demo", base)
        order = [r["id"] for r in rows]
        check("목록 순서: 성공(번호순) → 성공 쇼츠 → 하루 조회수(큰 순) → 그 밖 → 외국",
              order == [ids["succ2"], ids["succ1"], ids["part1"], ids["shs1"], ids["vpd2"], ids["vpd1"], ids["oth1"], ids["for1"]],
              order=",".join(o.rstrip("_") for o in order))
        check("끝까지 있는 대본·뺀 쇼츠는 목록에서 뺌", seen["full"] == 1 and seen["excluded"] == 1 and ids["full1"] not in order)
        check("앞 5분만 있는 대본 = '2차'", next(r for r in rows if r["id"] == ids["part1"])["need"] == "2차")
        csv_p = write_list("demo", rows, seen, base)
        rows2 = read_rows(csv_p.read_text("utf-8-sig"))
        check("목록 csv 읽기 (BOM·숫자)", [r["id"] for r in rows2] == order and rows2[0]["minutes"] == 3.0)

        fake = _FakeGitHub(files={f"demo/result/outliers/{LIST_NAME}.csv": csv_p.read_text("utf-8-sig")},
                           existing=[f"W_{ids['oth1']}/transcript.json"])
        gh = GitHub("fake-owner/fake-repo", "main", "fake-token", "demo", session=fake, sleep=lambda s: None)
        check("GitHub 에서 목록 받기", read_rows(gh.read_text(f"demo/result/outliers/{LIST_NAME}.csv"))[0]["id"] == ids["succ2"])
        ex, tr = gh.existing_transcripts("demo/result/outliers")
        check("GitHub 에 이미 있는 대본 찾기", ex == {f"demo/result/outliers/W_{ids['oth1']}/transcript.json"} and not tr)
        for bad in ("demo/result/outliers/analysis.md", "other/result/outliers/W_aaaaaaaaaaa/transcript.json",
                    "demo/result/outliers/W_aaaaaaaaaaa/comments.csv", "demo/result/outliers/W_../../x/transcript.json"):
            try:
                gh.commit({bad: "x"}, "bad")
                check(f"대본이 아닌 경로는 거부: {bad}", False)
            except ValueError:
                check(f"대본이 아닌 경로는 거부: {bad}", True)

        def caption(vid, foreign):
            if vid == ids["for1"]:
                return [{"text": "hello", "start": 0.4, "duration": 1.0}], "en(자동)", "ok"
            if vid == ids["vpd1"]:
                return [], "-", "ProxyError: connection"
            return [], "-", "IpBlocked: 자막 서버 차단"

        calls = []

        def whisper(vid, dur, max_sec, short, foreign):
            calls.append((vid.rstrip("_"), max_sec, short))
            if vid == ids["shs1"]:
                return [], {"language": "ko", "source": "whisper_small"}       # 말 없는 쇼츠
            if vid == ids["vpd2"]:
                raise RuntimeError("다운로드 실패")
            return [{"text": "말", "start": 0.0, "duration": 1.0}], {"language": "ko", "source": "whisper_small"}

        opts = types.SimpleNamespace(push_every=3, push_min=999, no_push=False, dry_run=False, no_whisper=False)
        work = base / ".yt_work"
        runner = Runner("demo", rows2, gh, caption, whisper, work, opts, existing=frozenset(ex), now=lambda: 0.0)
        tot = runner.run()
        st = runner.state
        check("자막 받음 → 'caption'", st[ids["for1"]]["done"] == "caption")
        check("자막 막힘 → 1차 앞 5분 → 2차 끝까지", ("succ1", 300, False) in calls and ("succ1", None, False) in calls
              and st[ids["succ1"]]["done"] == "whisper")
        check("짧은 영상(3분)은 1차로 끝 (2차 없음)", ("succ2", 300, False) in calls and ("succ2", None, False) not in calls
              and st[ids["succ2"]]["done"] == "whisper")
        check("'2차' 영상은 자막·1차 없이 바로 끝까지", ("part1", None, False) in calls and ("part1", 300, False) not in calls
              and st[ids["part1"]]["done"] == "whisper" and st[ids["part1"]]["caption"] == 0)
        check("쇼츠: 끝까지 한 번 · 말 없음도 끝", ("shs1", None, True) in calls and st[ids["shs1"]]["done"] == "whisper")
        check("연결 실패는 음성인식하지 않고 다음 실행에", st[ids["vpd1"]].get("done") is None and not any(c[0] == "vpd1" for c in calls))
        check("음성인식 실패는 기록하고 다음 영상으로", st[ids["vpd2"]].get("done") is None and st[ids["vpd2"]]["w1"] == 1)
        check("GitHub 에 이미 있으면 건너뜀", st[ids["oth1"]]["done"] == "remote" and not any(c[0] == "oth1" for c in calls))
        ents = {e["path"]: e["content"] for t in fake.trees for e in t["tree"]}
        check("올린 파일 = 대본 두 파일만", ents and all(allowed_path("demo").match(p) for p in ents), files=len(ents))
        check("main 이 그 사이 바뀌면 새 main 위에 다시 (강제 없음)", fake.refused == 0 and fake.commits[1]["parents"] == ["c-other"]
              and fake.head not in ("c0", "c-other") and all(j.get("force") is False for j in fake.patches))
        tj = json.loads(ents[f"demo/result/outliers/W_{ids['succ1']}/transcript.json"])
        check("대본 꼴 (lang·snippets·source — 분석 도구가 읽는 꼴)", tj["lang"] == "ko(음성인식)" and tj["snippets"][0]["text"] == "말"
              and tj.get("source") == "whisper_small" and "partial_sec" not in tj)
        txt = ents[f"demo/result/outliers/W_{ids['for1']}/transcript.txt"]
        check("transcript.txt 꼴 '[    0.4] …'", txt == "[    0.4] hello", txt=txt)
        sj = json.loads(ents[f"demo/result/outliers/shorts/S_{ids['shs1']}/transcript.json"])
        check("말 없는 쇼츠 = no_speech", sj.get("no_speech") is True and sj["snippets"] == [])
        check("올릴 것이 남지 않음", not runner.pending_files() and tot["commits"] >= 2, commits=tot["commits"])
        calls.clear()                                       # 이어서: 같은 상태로 다시 돌리면 끝난 영상은 다시 하지 않음
        runner2 = Runner("demo", rows2, gh, caption, whisper, work, opts, existing=frozenset(ex), now=lambda: 0.0)
        runner2.run()
        check("다시 실행하면 남은 것만 (음성인식 실패 · 연결 실패 2번 → 음성인식)", {c[0] for c in calls} == {"vpd1", "vpd2"}, calls=calls)
        dry = types.SimpleNamespace(**{**vars(opts), "dry_run": True})
        gh_dry = GitHub("fake-owner/fake-repo", "main", "fake-token", "demo", session=_FakeGitHub(), dry_run=True)
        r3 = Runner("demo", [r for r in rows2 if r["id"] == ids["vpd1"]], gh_dry, caption, whisper, base / ".yt_dry", dry, now=lambda: 0.0)
        r3.state[ids["vpd1"]] = {"done": None, "caption": 2, "w1": 0, "w2": 0, "caption_result": "network"}
        r3.run()
        check("--dry-run 은 올리지 않고 남겨 둠 (다음 실제 실행이 올림)", len(r3.pending_files()) == 2 and not r3.state[ids["vpd1"]].get("pushed"))
        def whisper_missing(*a):
            raise RuntimeError("faster-whisper 없음 → 다시 실행하면 설치함")
        r4 = Runner("demo", [r for r in rows2 if r["id"] in (ids["vpd1"], ids["vpd2"])], gh_dry, caption, whisper_missing, base / ".yt_env", dry,
                    now=lambda: 0.0)
        for v in (ids["vpd1"], ids["vpd2"]):
            r4.state[v] = {"done": None, "caption": 2, "w1": 0, "w2": 0, "caption_result": "whisper"}
        r4.run()
        check("음성인식 준비 안 됨 → 시도 횟수를 쓰지 않고 멈춤", r4.whisper_off and r4.state[ids["vpd1"]]["w1"] == 0 and r4.state[ids["vpd2"]]["w1"] == 0)
        check("PC 의 결과 폴더는 건드리지 않음", not (od / f"W_{ids['succ1']}" / "transcript.json").exists())
    print(f"[SELFTEST] {'✅ 모두 통과' if ok else '❌ 실패 있음'}")
    return 0 if ok else 1


def main(argv=None):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")       # Windows 콘솔 한글
    except Exception:
        pass
    ap = argparse.ArgumentParser(description="대본 받기 — list(클라우드) · run(PC, 대본 파일만 올림) · selftest")
    sub = ap.add_subparsers(dest="cmd", required=True)
    pl = sub.add_parser("list", help="받을 목록 만들기 → <주제>/result/outliers/transcript_todo.csv·.md")
    pl.add_argument("topics", nargs="+")
    pr = sub.add_parser("run", help="PC: 목록대로 자막 → 음성인식 → 대본 파일만 GitHub 에")
    pr.add_argument("topics", nargs="+")
    pr.add_argument("--limit", type=int, default=0, help="이번에 할 영상 수 (시험 삼아 --limit 5)")
    pr.add_argument("--korean-only", action="store_true", help="한국어 영상만")
    pr.add_argument("--groups", default="", help="묶음만: " + ",".join(k for k, _ in GROUPS))
    pr.add_argument("--no-whisper", action="store_true", help="자막만 (음성인식 안 함)")
    pr.add_argument("--model", default="", help="Whisper 모델 (기본 = 설정 파일 WHISPER_MODEL, 보통 small · NVIDIA GPU 면 medium)")
    pr.add_argument("--push-every", type=int, default=PUSH_EVERY, help=f"영상 몇 개마다 올릴지 (기본 {PUSH_EVERY})")
    pr.add_argument("--push-min", type=float, default=PUSH_EVERY_MIN, help=f"또는 몇 분마다 (기본 {PUSH_EVERY_MIN})")
    pr.add_argument("--no-push", action="store_true", help="올리지 않고 .yt_work/transcribe/ 에만")
    pr.add_argument("--dry-run", action="store_true", help="올릴 것만 보여 줌")
    pr.add_argument("--list-file", default="", help="GitHub 대신 이 목록 파일")
    pr.add_argument("--repo", default="yeomin1024/yeomin1024-ytb")
    pr.add_argument("--branch", default="main")
    pr.add_argument("--skip-install", action="store_true")
    for p in (pl, pr):
        p.add_argument("--log-level", default="INFO")
    sub.add_parser("selftest", help="가짜 GitHub 로 시험 (진짜로 올리지 않음)")
    opts = ap.parse_args(argv)
    if opts.cmd == "list":
        return cmd_list(opts)
    if opts.cmd == "run":
        return cmd_run(opts)
    return selftest()


if __name__ == "__main__":
    sys.exit(main())
