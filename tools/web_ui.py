#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.5 — 2026-10-15 — 할당량 표시·주제별 창·초기화 뒤 자동으로 이어서 (사용자 지시: "유튜브 분석 코드를 최대한 api 사용량 덜쓰는
#          방법(단어 줄이는 방법 말고) 찾아서 수정해보고 웹 ui에 사용량 얼마나 남았는지 표시하고 그리고 분석기 여러개 열어서 각자 다른 주제로
#          탐색해도 되지? 그리고 economic 같은 주제 경로를 선택할 수 있게해서 각각 주제별로 탐색할 수 있게 수정해 그리고 사용량 초기화되면
#          자동으로 다시 분석 마저 하는거지? 그렇게 되야해"):
#          ① 남은 할당량: 화면 위에 '남은 N / 9,800 · 초기화 한국 시간 MM-DD HH:MM (n시간 뒤)' — 같은 키를 쓰는 모든 창·주제·자동 실행을
#             합친 키 장부(tools/pc_analysis.py KeyLedger, 요청마다 적음). 자세히: 주제별·작업별 사용량, 열린 다른 창
#          ② 주제 고르기: 화면 위 주제 목록 = 설정 파일이 있는 모든 주제 폴더(경로 표시) + [새 주제] (폴더·이름·검색어 → 설정 파일 3개)
#          ③ 창 여러 개: 창(프로세스)마다 주제 하나를 잠금(.yt_work/web_<주제>.lock — OS 잠금) — 같은 주제를 두 창이 동시에 쓰지 않게,
#             다른 주제는 동시에. 같은 주제 창이 이미 있으면 그 창 주소를 열고 끝. `web_ui.py economic health` 처럼 주제를 여러 개 주면
#             주제마다 창을 하나씩 띄움 (포트 자동). 음성인식은 PC 에서 한 번에 하나 (분석기 v2.10.1 — 다른 주제는 기다렸다가)
#          ④ 초기화 뒤 자동으로 이어서: 태평양 자정(+10분)이 되면 할당량 때문에 남은 것(탐색 검색·영상 정보, 못 받은 댓글, 채널 기준선)을
#             저절로 이어서 하고 다시 분석·올림 (job_resume). 켤 때도 남은 탐색이 있으면 이어서. 다시 탐색해도 내가 체크한 것은 그대로
#          ⑤ 할당량 아끼기 (outlier_research v2.2): 적응형 검색 캐시(안 바뀌는 검색은 7→14→21일), 채널 목록은 새 영상만, 오래된 영상 정보는
#             길게, 한 쪽짜리 댓글은 인기 댓글 쪽 건너뜀 — 탐색 로그에 검색마다 캐시 시간·단계·새로 보인 영상
# (v1.4 — 2026-10-14 — 분석 결과로 '무엇이 먹혔나'를 가릴 수 있게 (사용자 지시: "결과 올라갔는데 문제가 부분 수정하고
#          분석결과로 내가 말한 거 할수 있는지 판단해 개선 필요하면 더 개선하고"):
#          ① 같은 채널 기준선 (job_baseline): 켤 때·승인 때 사례 채널(구독자 5만 이하) 최근 영상 50개(업로드 목록 + 영상 정보 —
#             채널 하나 약 2단위, 7일 캐시)를 받음 → 분석이 '채널 평소 대비 ×'·같은 채널 잘된 영상 vs 평소 영상을 셈
#             (⚠️ 할당량: 처음 한 번 채널 141곳이면 약 280단위)
#          ② 음성인식 2단계 표시 (분석기 v2.10.0 — 1차 앞 5분 → 2차 전체): 차수 이름·차수마다 n/전체, 남은 수에 2차 남은 영상도
#          ③ 분석 요약 칸에 같은 채널 기준선 (성공 사례 몇 개에 '채널 평소 대비'가 있나)
# (v1.3 — 2026-10-14 — 성공 사례 분석(analysis.md)이 맞게 나오게 (사용자 지시: "성공 사례 영상의 정보와 시청자들의 니즈 …
#          어떤 주제, 어떤 제목, 어떤 썸네일, 내용을 어떻게 구성해야하는지 … 올바른 분석 결과까지만 내도록 수정해"):
#          ① 켤 때 코드도 GitHub 최신으로 받은 뒤 도구를 불러옴 (새 도구 tools/success_analysis.py 가 PC 에 오게 — 실행기 목록에 없던 파일)
#          ② 못 받은 댓글 이어 받기 (job_comments — 승인 영상 W_ 중 comments_complete=False: 2026-10-14 88개 중 55개가 할당량이 끝나 0개였고
#             예전엔 다시 받을 길이 없었음) — 켤 때 저절로, [못 받은 댓글 이어 받기] 단추
#          ③ 분석 결과 칸 위에 성공 사례 분석 요약 (성공 사례 수·글 출처·한계·자료 없는 성공 후보 → [성공 후보 체크] 단추)
#          ④ 수요와 공급 (사용자 지시: "수요 대비 영상 공급이 별로 없는지도 파악해야해 …"): [탐색] 때 검색어마다 YouTube 자동완성(사람들이 찾는 말)도
#             받음 (할당량 0, 7일 캐시) · [공급 확인] = 수요는 있는데 영상이 적어 보이는 말 N개를 직접 검색(말 하나 100단위) → 다시 분석·올림)
# (v1.2.1 — 2026-10-14 — 공개 저장소에도 자료(사례 폴더)를 다 올림 (사용자 지시 "그냥 공개에서 다 올리도록 해" — 분석기 v2.9.3): 승인 결과 안내를
#          분석기 로그의 full=True/False 로 읽음 (예전: private=True/False — 공개면 늘 'PC 에만'으로 보였을 것))
# (v1.2 — 2026-10-14 — 결과 먼저 올리고 음성인식은 뒤에서 (사용자 지시: "아니 음성인식이랑 별개로 분석결과 낼 수 있잖아 자막도
#          다운 시도했는데 안되면영상 설명으로 대체해서 그냥 분석결과랑 자료 다 올려 그 다음 음성인식하라고 수정해"):
#          ① [승인] = 자료 받기(설명·자막 시도·썸네일·댓글 전부) → 주별 분석(자막을 못 받은 영상은 영상 설명으로 대신 —
#             weekly_analysis v1.2, 승인 영상 표 approved.md) → **바로 GitHub 에 올림** → 작업 끝. (예전 v1.1: 음성인식 대기열이
#             다 끝나야 — 289개면 2~3일 — 올렸음)
#          ② 음성인식은 그 뒤에 '뒤에서' 따로 (화면 위 '음성인식' 표시: n/전체·지금 영상, [음성인식 시작]·[멈춤]) — 하나 끝날 때마다
#             대본을 넣어 주별 분석을 다시 만들고 바로 올림 (분석기 --whisper-queue). 도는 동안에도 탐색·승인을 할 수 있음.
#             승인을 더 하면 지금 대기열이 끝난 뒤 새 영상도 이어서
#          ③ 화면을 켜면: 승인한 영상이 있으면 주별 분석을 다시 만들어 올리고(새 코드의 설명 대체·표), 자막 없는 영상이 남았으면
#             음성인식을 뒤에서 시작 (--no-whisper 로 끔)
#          ④ [다시 분석]도 다시 만든 뒤 올림
#          ※ 사례 폴더(W_ — 다른 사람의 설명·자막·댓글·썸네일 원문)는 저장소가 비공개일 때만 올라감 (CLAUDE.md) — 공개면 화면에 안내)
# (v1.1.1 — 2026-10-14 — 분석 결과 안내 글만: 오래된 영상은 '창 밖' → 마지막 '전체' 창에 (weekly_analysis v1.1))
# (v1.1 — 2026-10-14 — 목록 고침 (사용자 지시: "영상이나 채널 여러 개 넣을 수 있게 하고 체크된거랑 안된거 따로 목록 분리해서
#          보여주고 이미 분석에 사용한 영상이면 목록에서 제외해 그리고 라이브 방송, 외국 영상은 탐색 대상에서 제외 그리고 목록을 배수가
#          가장 높은순으로 정렬해"): ① 직접 추가 칸에 여러 개 (한 줄에 하나 — 띄어쓰기·쉼표로 나눠도 됨) ② 목록을 '체크한 영상'과
#          '체크 안 한 영상' 두 표로 (체크하면 위 표로 옮겨 감) ③ 이미 분석에 쓴 영상(승인한 W_·성공 사례 01_·조회수 상위 P01_·_old·
#          분석기 성공사례)은 목록에서 뺌 ④ 라이브 방송·외국 영상은 탐색에서 뺌 (tools/outlier_research.py v2.0 exclusion_reason —
#          주소로 직접 넣은 영상만 남기고 표시) ⑤ 목록은 배수(조회수÷구독자) 높은 순 (구독자 비공개는 맨 뒤)
# (v1.0 — 2026-10-14 — 신규: 분석기 웹 화면 (사용자 지시: "이거 분석기 웹 ui 형식으로 만들어 실행하면 바로 웹 ui가 나와서 env, 검색어
#          수정할 수 있게하고 탐색 버튼 누르면 탐색 대상 영상 목록이 나오지만 체크 표시만 해놓고 내가 승인 버튼을 눌러야 관련 자료를 받아서
#          분석하는걸로 해 그리고 내가 영상 url이나 채널을 추가하면 탐색 대상에 추가하도록 하고(채널을 추가하면 그 채널에 올려진 영상 다
#          탐색하는거야) 목록은 최근에 업로드 된 순으로 하고 1주 전, 2주 전, 3주 전 1주씩 늘리면서 분석 결과 내보도록 해"):
#          ① 실행하면 브라우저에 화면이 뜸 (이 PC 안에서만 — 127.0.0.1, 요청마다 무작위 열쇠 확인)
#          ② 키(.env 의 YOUTUBE_API_KEY·GITHUB_TOKEN — 끝 4자리만 보임)·검색어(<주제>/keywords.txt, GitHub 에도 저장 가능) 고치기
#          ③ 직접 추가: 영상 주소 → 그 영상, 채널 주소·@이름 → 그 채널에 올라온 영상 전부 (<주제>/targets.json)
#          ④ [탐색] → 검색어(최근 N주·조회수 순·4~20분·20분 넘음) + 추가한 채널·영상 → 목록 (최근 업로드 순). 추천(성공 사례·조회수 상위·
#             추가한 것)은 체크만 해 둠 — 자료는 아직 안 받음
#          ⑤ [승인] → 체크한 영상만 설명·자막·썸네일·댓글 전부를 받고(<주제>/result/outliers/W_<영상ID>/) 주별 분석
#             (tools/weekly_analysis.py — 최근 1주·2주·3주 … 한 주씩 넓힘) → 자막을 못 받은 영상은 음성인식 대기열 → 다시 분석 → GitHub))
r"""
사용법 (PC 실행 폴더 — run_analyzer.ps1 이 기본으로 띄움):
  python tools/web_ui.py                    # economic (설정 파일이 있는 주제 폴더가 여럿이면 화면에서 고름)
  python tools/web_ui.py economic --port 8765 --no-browser
  python tools/web_ui.py economic health    # 주제마다 창 하나씩 (같은 키의 할당량은 함께 셈 — 화면 위 '남은 할당량')
  옵션: --port 8765 (쓰는 중이면 다음 번호) · --no-browser (주소만 보여 줌) · --no-sync (GitHub 에서 설정·검색어를 받지 않음)
        --no-whisper (켤 때 음성인식을 뒤에서 시작하지 않음 — 화면의 [음성인식 시작]으로)
순서: [승인] → 자료 받기 → 같은 채널 기준선(채널 평소 영상) → 주별·성공 사례 분석(자막 없으면 설명으로) → GitHub 에 올림
      → (뒤에서) 음성인식 — 성공 사례부터 1차(앞 5분) → 2차(전체), 하나 끝날 때마다 다시 분석, 15분마다·차수 끝에 올림
할당량: 탐색 = 검색어 1개마다 검색 2번(200단위, 7일 캐시) + 채널 영상 목록 50개에 1단위 + 영상 정보 50개에 1단위.
        승인 = 영상마다 댓글 100개에 1단위 (+ 답글). 같은 채널 기준선(켤 때·승인 때) = 채널 하나 약 2단위 (7일 캐시).
        오늘 쓴 양: 키 장부 .yt_work/quota_key_<키 지문>.json (같은 키의 모든 창·주제·자동 실행) + 주제 장부 .yt_work/quota_<주제>.json.
        할당량이 끝나 남은 것은 태평양 자정(한국 오후 4~5시) +10분에 저절로 이어서 (창을 켜 둔 동안 · 켤 때도).
로그: [STAGE] [시각] key=value — 화면의 '진행' 칸과 .yt_work/web_ui.log
비밀값(키·토큰)은 화면·로그에 끝 4자리만. ※ 연구·교육용 분석 도구. 투자 권유가 아니다.
"""
import argparse
import base64
import collections
import hashlib
import json
import logging
import os
import re
import secrets
import subprocess
import sys
import threading
import time
import types
import urllib.error
import urllib.parse
import urllib.request
import webbrowser
from datetime import datetime, timedelta, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import pc_analysis as pc                 # noqa: E402  할당량 장부·키 찾기·GitHub 동기화·패키지 준비

ROOT = pc.ROOT
VERSION = "v1.5"
LOG = logging.getLogger("web")
KST = timezone(timedelta(hours=9))
TOKEN = secrets.token_urlsafe(18)        # 화면이 요청마다 보내는 열쇠 (다른 사이트가 이 PC 의 화면을 조작하지 못하게)
MIN_SEC = 240                            # 롱폼 기준 (4분) — 그보다 짧으면 '짧은 영상'
POPULAR_N = 20                           # 검색 결과 중 조회수 상위 몇 개를 추천(체크)할지
orr = None                               # tools/outlier_research.py (패키지 준비 뒤 불러옴)
wa = None                                # tools/weekly_analysis.py
STATE = {"topic": None, "topics": [], "port": None}
WINDOW = {"lock": None, "topic": None}     # v1.5: 이 창이 잠근 주제 (OS 잠금 — 창이 꺼지면 풀림)
RESUME = {"next": None, "last": None, "last_result": None, "status": "idle", "note": ""}   # v1.5: 초기화 뒤 자동으로 이어서
RESUME_MARGIN_MIN = 10                   # 태평양 자정 + 이 분 뒤에 이어서 (Google 쪽 초기화가 조금 늦을 때)
RESUME_JOB_WAIT_H = 6                    # 그때 다른 작업이 도는 중이면 끝나길 기다리는 최대 시간
TOPIC_RX = re.compile(r"^[a-z][a-z0-9_-]{1,30}$")
JOB = {"name": None, "status": "idle", "step": "", "done": 0, "total": 0, "started": None, "finished": None, "error": None,
       "result": None, "cancel": False, "log": collections.deque(maxlen=500), "proc": None}
JOB_LOCK = threading.Lock()
# 음성인식 (v1.2) — 작업(JOB)과 따로 뒤에서: 탐색·승인을 하는 동안에도 돎. 분석기 --whisper-queue 를 돌리고 출력 줄로 진행을 읽음
WHISPER = {"status": "idle", "topic": None, "proc": None, "started": None, "finished": None, "current": "", "done": 0, "failed": 0,
           "total": 0, "pass": "", "rerun": False, "stop": False, "last_exit": None, "note": "", "log": collections.deque(maxlen=300)}
WHISPER_LOCK = threading.Lock()
WHISPER_LINE_RX = re.compile(r"\[(?:INFO|WARNING)\] (\d+)/(\d+) (시작|끝|실패|올림|올리기 실패)(.*)$")
WHISPER_ITEMS_RX = re.compile(r"음성인식 대기열 items=(\d+)(?:.*?pass_=(\"[^\"]*\"|\S+))?")   # 분석기 v2.10.0 — 차수(1차 앞 5분·2차 전체)마다 한 줄
WHISPER_MAX_ATTEMPTS = 3                 # 분석기 WHISPER_QUEUE_MAX_ATTEMPTS 와 같게 (그만큼 실패한 영상은 '남은 것'에서 뺌)
SKIP_TRANSCRIPT = ("건너뜀", "확인 안 함")
NETWORK_FAIL_WORDS = ("ProxyError", "ConnectionError", "Timeout", "URLError")     # 분석기 대기열과 같은 기준 (연결 자체 실패는 뺌)
_PENDING_CACHE = {"t": None, "at": 0.0, "n": 0}


def log(stage, level=logging.INFO, **kv):
    LOG.log(level, "[%s] [%s] %s", stage, datetime.now().isoformat(timespec="seconds"),
            " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) and ' ' in v else v}" for k, v in kv.items()))


class _JobLogHandler(logging.Handler):
    """도구들의 로그 줄을 화면의 '진행' 칸으로."""

    def emit(self, record):
        try:
            JOB["log"].append(self.format(record))
        except Exception:
            pass


class UserError(Exception):
    """사용자에게 그대로 보여 줄 오류 (키 없음 등)."""


class Cancelled(Exception):
    pass


# ---------------------------------------------------------------- 경로·파일
def topic_dir(t):
    return ROOT / t


def out_dir(t):
    return ROOT / t / "result" / "outliers"


def web_dir(t):
    d = ROOT / t / "result" / "web"           # 탐색 목록 등 PC 에만 (GitHub 에 올리지 않음)
    d.mkdir(parents=True, exist_ok=True)
    return d


def _read_json(p, default):
    try:
        return json.loads(Path(p).read_text("utf-8"))
    except (OSError, ValueError):
        return default


def _write_json(p, data):
    p = Path(p)
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_name(p.name + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=1), "utf-8")
    os.replace(tmp, p)


def find_topics():
    return sorted(p.parent.name for p in ROOT.glob("*/analyzer_config.toml") if not p.parent.name.startswith("."))


def topic_name(t):
    try:
        flat = {}
        for k, v in pc._toml().loads((ROOT / t / "analyzer_config.toml").read_text("utf-8")).items():
            flat.update(v if isinstance(v, dict) and k != "KEYWORD_GROUPS" else {k: v})
        return str(flat.get("TOPIC") or t)
    except Exception:
        return t


# ---------------------------------------------------------------- 키 (.env)
ENV_NAMES = ("YOUTUBE_API_KEY", "GITHUB_TOKEN")


def mask(v):
    return f"…{v[-4:]} ({len(v)}자)" if v else ""


def env_view(t):
    out = {}
    for n in ENV_NAMES:
        v, src = pc.find_secret(n, t)
        out[n] = {"set": bool(v), "tail": mask(v), "source": src if v else "-"}
    return out


def set_env_value(path, name, value):
    """.env 의 name= 줄을 바꾸거나 더함 (다른 줄·메모는 그대로). 값은 로그에 쓰지 않음."""
    path = Path(path)
    lines = path.read_text("utf-8-sig").splitlines() if path.is_file() else []
    rx = re.compile(rf"^[ \t]*{name}[ \t]*=")
    for i, line in enumerate(lines):
        if rx.match(line):
            lines[i] = f"{name}={value}"
            break
    else:
        lines.append(f"{name}={value}")
    path.write_text("\n".join(lines) + "\n", "utf-8")


# ---------------------------------------------------------------- 검색어·직접 추가
def keywords_path(t):
    return ROOT / t / pc.KEYWORD_LIST_FILE


def targets_path(t):
    return ROOT / t / "targets.json"


def load_targets(t):
    d = _read_json(targets_path(t), {})
    return {"channels": list(d.get("channels") or []), "videos": list(d.get("videos") or [])}


def github_put(t, rel, data, message):
    """GitHub 에 파일 하나 저장 (contents API — 토큰 필요). → (ok, 설명)."""
    token = pc.find_secret("GITHUB_TOKEN", t)[0]
    if not token:
        return False, "GITHUB_TOKEN 없음 — PC 에만 저장"
    repo, branch = pc.repo_of(t)
    url = f"https://api.github.com/repos/{repo}/contents/{urllib.parse.quote(rel)}"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
    sha = None
    try:
        with urllib.request.urlopen(urllib.request.Request(f"{url}?ref={urllib.parse.quote(branch)}", headers=headers), timeout=30) as r:
            sha = json.loads(r.read().decode("utf-8")).get("sha")
    except urllib.error.HTTPError as e:
        if e.code != 404:
            return False, f"GitHub 읽기 실패 HTTP {e.code}"
    except Exception as e:
        return False, f"GitHub 연결 실패 ({type(e).__name__})"
    body = {"message": message, "content": base64.b64encode(data).decode("ascii"), "branch": branch}
    if sha:
        body["sha"] = sha
    req = urllib.request.Request(url, data=json.dumps(body).encode("utf-8"), headers={**headers, "Content-Type": "application/json"}, method="PUT")
    try:
        with urllib.request.urlopen(req, timeout=30):
            pass
    except urllib.error.HTTPError as e:
        return False, f"GitHub 저장 실패 HTTP {e.code}" + (" — 토큰의 Contents 권한이 Read and write 인지 확인" if e.code in (403, 404) else "")
    except Exception as e:
        return False, f"GitHub 연결 실패 ({type(e).__name__})"
    sync_p = ROOT / ".yt_work" / "config_sync.json"            # 자동 실행의 동기화가 'GitHub 과 같음'으로 보게
    st = _read_json(sync_p, {})
    st[rel] = hashlib.sha256(data).hexdigest()
    _write_json(sync_p, st)
    return True, f"GitHub 에도 저장 ({repo}/{rel})"


def key_ledger(t):
    """이 주제가 쓰는 YouTube 키의 장부 (같은 키 = 모든 창·주제가 함께, v1.5). 키가 없으면 None."""
    key = orr.load_api_key(t)[0]
    return pc.KeyLedger(key) if key else None


def make_api(t, what="web"):
    """v1.5: 남은 양 = 키 장부(같은 키의 다른 창·주제·자동 실행 포함). 요청마다 키 장부에 먼저 적고(orr.Api ledger=) 실패하면 돌려줌."""
    key, src = orr.load_api_key(t)
    if not key:
        raise UserError("YouTube API 키가 없습니다 — 화면 위 '1. 키 설정'에서 넣고 저장하세요")
    kl = pc.KeyLedger(key)
    left = kl.left()
    if left < 1:
        q = kl.snapshot()
        raise UserError(f"오늘 할당량을 다 썼습니다 (이 키로 {q['used']:,}단위" + (" · Google 이 하루 한도라고 답함" if q["exhausted"] else "")
                        + f") — 한국 시간 {q['reset_kst']} 초기화 +{RESUME_MARGIN_MIN}분 뒤 남은 것은 저절로 이어서 합니다 (이 창을 켜 두면)")
    return orr.Api(key, left, ledger=kl, what=what, topic=t), pc.Ledger(t), src


def record_use(t, api, ledger, what):
    """작업이 끝날 때 (v1.5): 주제 장부(자동 실행이 주제 몫을 셀 때 봄)에 적음 — 키 장부는 요청마다 이미 적었으므로 기록 한 줄만."""
    ledger.add(api.used, what, forward=False)
    if api.used and getattr(api, "ledger", None) is not None:
        api.ledger.note_run(what, t, api.used)
    if api.used:
        log("QUOTA", topic=t, what=what, units=api.used, calls=",".join(f"{k}:{v}" for k, v in sorted(api.calls.items())) or "-",
            left=api.ledger.left() if getattr(api, "ledger", None) is not None else "-")


def quota_view(t):
    """화면 위 할당량 (v1.5): 같은 키의 오늘 사용·남은 양·다음 초기화(한국 시간)·주제별·작업별."""
    kl = key_ledger(t)
    budget = pc.DAILY_LIMIT - pc.DAILY_MARGIN
    if not kl:
        reset, _ = pc.next_quota_reset(datetime.now(timezone.utc), margin_min=0)
        return {"key": None, "used": 0, "left": None, "budget": budget, "exhausted": False, "by_topic": {}, "by_what": {},
                "reset_kst": reset.astimezone(KST).strftime("%m-%d %H:%M"), "topic_used": pc.Ledger(t).used(),
                "day": pc.pacific_day(datetime.now(timezone.utc))}
    q = kl.snapshot()
    q.update(budget=budget, topic_used=int((q.get("by_topic") or {}).get(t, 0)))
    return q


# ---------------------------------------------------------------- 창 여러 개 (v1.5): 창마다 주제 하나를 잠금
def _window_tag(t):
    return re.sub(r"[^0-9A-Za-z_-]+", "_", str(t)) or "topic"


def _window_paths(t):
    base = ROOT / ".yt_work" / f"web_{_window_tag(t)}"
    return base.with_suffix(".lock"), base.with_suffix(".json")


def topic_window(t):
    """다른 창이 이 주제를 쓰는 중이면 그 창 정보 {url, pid, since}, 아니면 None (잠금을 잠깐 잡아 보고 바로 놓음)."""
    lock_p, info_p = _window_paths(t)
    if WINDOW["topic"] == t:
        return None
    if not lock_p.is_file():
        return None
    f = pc.os_lock(lock_p, 0)
    if f is not None:                 # 아무도 안 잡고 있음 (예전 창이 꺼짐)
        pc.os_unlock(f)
        return None
    return _read_json(info_p, {}) or {"url": "", "pid": None}


def claim_topic(t):
    """이 창이 주제 t 를 씀 — 다른 창이 쓰는 중이면 UserError (그 창 주소와 함께). 예전 주제의 잠금은 놓음."""
    if WINDOW["topic"] == t and WINDOW["lock"] is not None:
        return
    lock_p, info_p = _window_paths(t)
    f = pc.os_lock(lock_p, 0)
    if f is None:
        other = _read_json(info_p, {})
        raise UserError(f"'{t}' 주제는 다른 분석기 창이 쓰는 중입니다 — {other.get('url') or '그 창'} (한 주제는 창 하나에서만, 다른 주제는 동시에 돼요)")
    old_lock, old_t = WINDOW["lock"], WINDOW["topic"]
    WINDOW.update(lock=f, topic=t)
    _write_json(info_p, {"topic": t, "url": f"http://127.0.0.1:{STATE['port']}/" if STATE.get("port") else "", "pid": os.getpid(),
                         "since": datetime.now(KST).isoformat(timespec="seconds")})
    if old_lock is not None:
        pc.os_unlock(old_lock)
        try:
            _window_paths(old_t)[1].unlink()
        except OSError:
            pass
    log("WINDOW", topic=t, port=STATE.get("port"), note="이 창이 이 주제를 씀 (다른 창은 다른 주제만)")


def release_topic():
    if WINDOW["lock"] is not None:
        pc.os_unlock(WINDOW["lock"])
        try:
            _window_paths(WINDOW["topic"])[1].unlink()
        except OSError:
            pass
        WINDOW.update(lock=None, topic=None)


def open_windows():
    """열린 분석기 창 전부 (이 창 포함) → [{topic, url, me}] (v1.5)."""
    out = []
    for t in find_topics():
        if t == WINDOW["topic"]:
            out.append({"topic": t, "url": f"http://127.0.0.1:{STATE['port']}/", "me": True})
            continue
        w = topic_window(t)
        if w is not None:
            out.append({"topic": t, "url": w.get("url") or "", "me": False})
    return out


def create_topic(folder, name, keywords_text, push=False):
    """새 주제 폴더 (v1.5): <폴더>/analyzer_config.toml(economic 틀에서 주제 이름·폴더만 바꿈)·keywords.txt·keywords.toml(관련어 비움)
    ·analysis_rules.toml(economic 것 복사). 관련어가 비어 있으면 모든 검색 결과를 주제 관련으로 봄 → Claude 에게 '<주제> 검색어 만들어줘'로 다듬기."""
    folder = str(folder or "").strip()
    name = str(name or "").strip() or folder
    if not TOPIC_RX.match(folder):
        raise UserError("폴더 이름은 영어 소문자로 시작하고 영어 소문자·숫자·-·_ 만 (2~31자) — 예: health, side-job")
    d = ROOT / folder
    if (d / "analyzer_config.toml").is_file():
        raise UserError(f"'{folder}' 주제 폴더가 이미 있습니다 — 위 주제 목록에서 고르세요")
    if any(c in name for c in '"\\\n') or len(name) > 40:
        raise UserError("주제 이름은 40자 이하, 따옴표·역슬래시 없이")
    tpl_p = ROOT / "economic" / "analyzer_config.toml"
    if tpl_p.is_file():
        cfg = tpl_p.read_text("utf-8")
        cfg = re.sub(r'(?m)^TOPIC\s*=\s*"[^"]*"', f'TOPIC = "{name}"', cfg)
        cfg = re.sub(r'(?m)^PROJECT_FOLDER\s*=\s*"[^"]*"', f'PROJECT_FOLDER = "{folder}"', cfg)
    else:
        cfg = (f'[topic]\nTOPIC = "{name}"\nPROJECT_FOLDER = "{folder}"\nRESULT_FOLDER = "result"\n\n[github]\nGITHUB_REPO = "yeomin1024/yeomin1024-ytb"\n'
               f'GITHUB_BRANCH = "main"\n\n[search]\nREGION_CODE = "KR"\nLANGUAGE = "ko"\n\n[keywords]\nKEYWORD_MODE = "curated"\nKEYWORDS_FILE = "keywords.toml"\n')
    cfg = f"# {name} — 웹 화면에서 새로 만든 주제 ({datetime.now(KST).strftime('%Y-%m-%d')}, web_ui {VERSION}, 틀: economic)\n" + cfg
    kws = [k.strip() for k in str(keywords_text or "").splitlines() if k.strip() and not k.strip().startswith("#")]
    files = {
        "analyzer_config.toml": cfg,
        "keywords.txt": f"# {name} 검색어 — 한 줄에 하나 (# 은 메모)\n" + "".join(k + "\n" for k in kws),
        "keywords.toml": (f"# {name} — 관련어(주제와 관련된 영상 가리기)·제외어. 비어 있으면 모든 검색 결과를 주제 관련으로 봄\n"
                          "EXTRA_KEYWORDS = []\nEXCLUDE_KEYWORDS = []\n\n[KEYWORD_GROUPS]\n\n[relevance]\n"
                          "RELEVANCE_TERMS = []\nRELEVANCE_WEAK_TERMS = []\nRELEVANCE_EXCLUDE = []\n"),
    }
    rules = ROOT / "economic" / "analysis_rules.toml"
    if rules.is_file():
        files["analysis_rules.toml"] = rules.read_text("utf-8")
    d.mkdir(parents=True, exist_ok=True)
    for fn, text in files.items():
        (d / fn).write_text(text, "utf-8")
    notes = [f"PC 에 만듦 ({folder}/ — {', '.join(files)})"]
    if push:
        for fn, text in files.items():
            ok, note = github_put(folder, f"{folder}/{fn}", text.encode("utf-8"), f"[{name}] 새 주제 (웹 화면) — {fn}")
            if not ok:
                notes.append(note)
                break
        else:
            notes.append("GitHub 에도 저장")
    log("TOPIC", folder=folder, name=name, keywords=len(kws), note=" · ".join(notes))
    return {"folder": folder, "name": name, "keywords": len(kws), "message": " · ".join(notes)}


def add_target(t, text):
    kind, val = orr.parse_target(text)
    if not kind:
        raise UserError(val)
    tg = load_targets(t)
    now = datetime.now(KST).isoformat(timespec="minutes")
    if kind == "video":
        if any(v["id"] == val for v in tg["videos"]):
            return {"kind": "video", "id": val, "note": "이미 있음"}
        entry = {"id": val, "title": "", "added": now}
        try:
            api, ledger, _ = make_api(t, "web_add")
        except UserError as e:                       # 키가 없거나 할당량이 없어도 추가는 됨 — 제목은 탐색 때
            api, entry["note"] = None, f"제목은 탐색 때 ({e})"
        if api:
            try:
                items = api.videos([val])
            except Exception as e:
                items, entry["note"] = None, f"제목은 탐색 때 ({type(e).__name__})"
            finally:
                record_use(t, api, ledger, "web_add")
            if items == []:
                raise UserError(f"영상을 찾지 못했습니다 (지워졌거나 비공개): {val}")
            if items:
                entry["title"] = items[0]["snippet"].get("title", "")
                entry["channel"] = items[0]["snippet"].get("channelTitle", "")
        tg["videos"].append(entry)
        _write_json(targets_path(t), tg)
        log("TARGET", kind="video", id=val, title=entry.get("title", ""))
        return {"kind": "video", **entry}
    api, ledger, _ = make_api(t, "web_add")
    try:
        ch = orr.resolve_channel(api, kind, val)
    finally:
        record_use(t, api, ledger, "web_add")
    if not ch:
        raise UserError(f"채널을 찾지 못했습니다: {val}")
    if any(c["id"] == ch["id"] for c in tg["channels"]):
        return {"kind": "channel", **ch, "note": "이미 있음"}
    ch["added"] = now
    tg["channels"].append(ch)
    _write_json(targets_path(t), tg)
    log("TARGET", kind="channel", id=ch["id"], title=ch["title"], videos=ch["videos"])
    return {"kind": "channel", **ch}


def add_targets(t, text):
    """여러 개를 한 번에 (한 줄에 하나 — 띄어쓰기·쉼표로 나눠도 됨). → [{input, ok, kind, id, title, note|error}] (v1.1)."""
    items = [x for x in re.split(r"[\s,]+", str(text or "")) if x.strip()]
    if not items:
        raise UserError("빈 칸 — 영상 주소나 채널 주소를 넣으세요")
    out = []
    for x in items[:200]:
        try:
            out.append({"input": x, "ok": True, **add_target(t, x)})
        except UserError as e:
            out.append({"input": x, "ok": False, "error": str(e)})
        except Exception as e:
            out.append({"input": x, "ok": False, "error": f"{type(e).__name__}: {e}"[:160]})
    return out


CASE_RX = re.compile(r"^(?:W_|P?\d\d_)([0-9A-Za-z_-]{11})$")


def used_ids(t):
    """이미 분석에 쓴 영상 (v1.1 — 목록에서 뺌): 웹 화면에서 승인한 W_·성공 사례 01_·조회수 상위 P01_ (빠진 것 _old/ 도) +
    분석기 성공사례(output/…/success_cases). → {영상ID}"""
    ids = set()
    od = out_dir(t)
    for base in (od, od / "_old"):
        if base.is_dir():
            for d in base.iterdir():
                m = CASE_RX.match(d.name)
                if m and d.is_dir() and (d / "metadata.json").is_file():
                    ids.add(m.group(1))
    try:
        sc = pc.read_paths(t)[1] / "success_cases"
        for d in (sc.iterdir() if sc.is_dir() else []):
            vid = _read_json(d / "metadata.json", {}).get("video_id")
            if vid:
                ids.add(vid)
    except Exception:
        pass
    return ids


def remove_target(t, kind, tid):
    tg = load_targets(t)
    key = "channels" if kind == "channel" else "videos"
    tg[key] = [x for x in tg[key] if x["id"] != tid]
    _write_json(targets_path(t), tg)
    return tg


# ---------------------------------------------------------------- 작업 (한 번에 하나, 뒤에서)
def job_view():
    return {k: (list(v)[-200:] if k == "log" else v) for k, v in JOB.items() if k not in ("proc", "cancel")}


def start_job(name, fn, *args):
    with JOB_LOCK:
        if JOB["status"] == "running":
            return False, f"'{JOB['name']}' 작업이 아직 도는 중입니다 — 끝난 뒤 다시"
        JOB.update(name=name, status="running", step="시작", done=0, total=0, started=datetime.now(KST).isoformat(timespec="seconds"),
                   finished=None, error=None, result=None, cancel=False, proc=None)
        JOB["log"].clear()

    def runner():
        try:
            JOB["result"] = fn(*args)
            JOB["status"] = "done"
        except Cancelled:
            JOB["status"] = "cancelled"
            log("JOB", logging.WARNING, name=name, note="사용자가 멈춤 — 받은 것은 캐시·폴더에 남음")
        except UserError as e:
            JOB.update(status="error", error=str(e))
            log("JOB", logging.WARNING, name=name, error=str(e))
        except Exception as e:
            JOB.update(status="error", error=f"{type(e).__name__}: {e}"[:300])
            LOG.exception("[JOB] %s 실패", name)
        finally:
            JOB["finished"] = datetime.now(KST).isoformat(timespec="seconds")
            JOB["proc"] = None
    threading.Thread(target=runner, daemon=True, name=f"job-{name}").start()
    return True, "시작"


def step(text, done=None, total=None):
    if JOB["cancel"]:
        raise Cancelled()
    JOB["step"] = text
    if done is not None:
        JOB["done"] = done
    if total is not None:
        JOB["total"] = total


def run_subprocess(cmd, label, capture=None):
    """도구를 따로 돌리고 출력 줄을 '진행' 칸으로 (멈춤을 누르면 끝냄). capture(목록)가 있으면 출력 줄을 거기에도. → 종료 코드."""
    env = {**os.environ, "PYTHONIOENCODING": "utf-8", "PYTHONUTF8": "1"}
    log("JOB", step=label, cmd=" ".join(str(c) for c in cmd[1:]))
    p = subprocess.Popen(cmd, cwd=ROOT, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    JOB["proc"] = p
    for raw in p.stdout:
        line = raw.decode("utf-8", errors="replace").rstrip()
        JOB["log"].append(line)
        if capture is not None:
            capture.append(line)
        if JOB["cancel"]:
            p.terminate()
    code = p.wait()
    JOB["proc"] = None
    if JOB["cancel"]:
        raise Cancelled()
    return code


# ---------------------------------------------------------------- 탐색
def estimate(t, weeks, use_keywords):
    """탐색하면 쓸 검색 할당량 (캐시는 0). → {searches, cached, units, channels}."""
    cache = out_dir(t) / ".cache"
    kws = orr.load_keywords(t, 0)[0] if use_keywords else []
    total = cached = 0
    for _, q in kws:
        for dur in ("medium", "long"):
            total += 1
            cached += orr.search_is_cached(cache, q, dur, weeks * 7)
    tg = load_targets(t)
    ch_units = sum(max(1, -(-int(c.get("videos") or 50) // 50)) * 2 for c in tg["channels"])   # 목록 + 영상 정보
    q = quota_view(t)
    return {"keywords": len(kws), "searches": total, "cached": cached, "units": (total - cached) * 100 + ch_units + 20,
            "channels": len(tg["channels"]), "videos": len(tg["videos"]), "left": q.get("left"), "reset_kst": q.get("reset_kst")}


def ratio_key(r):
    """배수 높은 순 (구독자 비공개 = 배수 없음은 맨 뒤), 같으면 조회수 많은 순."""
    return (r.get("ratio") is None, -(r.get("ratio") or 0), -(r.get("views") or 0))


def _is_success(r):
    return r["subs"] is not None and r["subs"] <= 50000 and r["views"] >= 10000 and (r["ratio"] or 0) >= 3


def preselect(rows):
    """추천 = 체크만 해 둠: 직접 추가한 영상 · 추가한 채널의 최근 N주 롱폼 · 검색 결과 중 성공 사례(작은 채널)·조회수 상위(주제 관련, 최근 N주 롱폼)."""
    reasons = {}
    searched = [r for r in rows if r["in_window"] and not r["short"] and r["relevant"] and any(s.startswith("검색:") for s in r["sources"])]
    searched_ids = {r["id"] for r in searched}
    for r in sorted(searched, key=lambda r: -r["views"])[:POPULAR_N]:
        reasons[r["id"]] = "조회수 상위"
    for r in rows:
        if "주소" in r["sources"]:
            reasons[r["id"]] = "추가한 영상"
        elif any(s.startswith("채널:") for s in r["sources"]) and r["in_window"] and not r["short"]:
            reasons[r["id"]] = "추가한 채널"
        elif r["id"] in searched_ids and _is_success(r):
            reasons[r["id"]] = "성공 사례"
    return reasons


def job_explore(t, weeks, use_keywords):
    api, ledger, src = make_api(t, "web_explore")
    out = out_dir(t)
    cache = out / ".cache"
    cache.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc)
    days = weeks * 7
    since = (now - timedelta(days=days)).strftime("%Y-%m-%dT00:00:00Z")
    kws, exclude, _, _, rel = orr.load_keywords(t, 0)
    kws = kws if use_keywords else []
    tg = load_targets(t)
    if not kws and not tg["channels"] and not tg["videos"]:
        raise UserError("탐색할 것이 없습니다 — 검색어를 넣거나 영상·채널을 추가하세요")
    found, pending = {}, []
    searched_new = 0
    state = orr.new_state()
    infos = []
    total = len(kws) * 2 + len(tg["channels"]) + 2
    n = 0
    log("EXPLORE", topic=t, weeks=weeks, keywords=len(kws), channels=len(tg["channels"]), videos=len(tg["videos"]), key_source=src,
        quota_left=api.quota)
    try:
        for g, q in kws:
            for dur in ("medium", "long"):
                n += 1
                step(f"검색 {q} ({'4~20분' if dur == 'medium' else '20분 넘음'})", n, total)
                ttl = {}
                try:
                    ids, hit = orr.cached_search(api, cache, q, since, dur, days, orr.SEARCH_TTL_HOURS, False, info=ttl)
                except orr.QuotaStop:
                    pending.append(f"{q} ({dur})")
                    continue
                for vid in ids:
                    found.setdefault(vid, []).append(f"검색:{q}")
                searched_new += not hit
                log("SEARCH", query=q, dur=dur, results=len(ids), cached=hit, quota_used=api.used,
                    **{k: v for k, v in ttl.items() if v is not None})       # v1.5: 적응형 캐시 시간(ttl_h)·단계·새로 보인 영상
        for ch in tg["channels"]:
            n += 1
            step(f"채널 {ch.get('title') or ch['id']} 영상 목록", n, total)
            try:
                ids = orr.channel_uploads(api, cache, ch)
            except orr.QuotaStop:
                pending.append(f"채널 {ch.get('title')}")
                continue
            for vid in ids:
                found.setdefault(vid, []).append(f"채널:{ch.get('title') or ch['id']}")
        for v in tg["videos"]:
            found.setdefault(v["id"], []).append("주소")
        if kws:                                   # v1.3: 수요 — 사람들이 찾는 말 (YouTube 자동완성, 할당량 0, 7일 캐시)
            ac_fail = ac_new = 0
            for k, (g, q) in enumerate(kws, 1):
                step(f"자동완성(사람들이 찾는 말) {k}/{len(kws)} — {q} (할당량 0)", n, total)
                try:
                    _, hit = orr.fetch_autocomplete(q, cache)
                    if not hit:
                        ac_new += 1
                        time.sleep(0.2)
                except Exception as e:
                    ac_fail += 1
                    if ac_fail == 3:
                        log("AUTOCOMPLETE", logging.WARNING, note="자동완성 연결 실패가 이어짐 — 이번엔 그만 (분석은 자동완성 없이)", error=f"{type(e).__name__}"[:60])
                        break
            log("AUTOCOMPLETE", keywords=len(kws), new=ac_new, failed=ac_fail, note="수요 자료 (할당량 0)")
        step(f"영상 {len(found):,}개 정보·구독자 수", n + 1, total)
        infos = orr.fetch_video_infos(api, cache, list(found), state)
        subs = orr.fetch_channel_subs(api, cache, {i["channel_id"] for i in infos}, state)
    finally:
        record_use(t, api, ledger, "web_explore")
    for i in infos:
        i["subs"] = (subs.get(i["channel_id"]) or {}).get("subs")
    info_by_id = {i["id"]: i for i in infos}
    url_ids = {v["id"] for v in tg["videos"]}                     # 주소로 직접 넣은 영상은 라이브·외국이어도 남김 (표시만)
    excluded = collections.Counter(orr.exclusion_reason(i) for i in infos if i["id"] not in url_ids)
    excluded.pop(None, None)
    rows = []
    for r in orr.build_rows(infos, found, now, keep=url_ids):
        srcs = list(dict.fromkeys(found.get(r["id"], [])))
        if "주소" not in srcs and any(w in (r["title"] or "") for w in exclude):
            continue
        r.update(sources=srcs, published_at=str(info_by_id[r["id"]].get("published") or ""),
                 relevant=orr.relevant(info_by_id[r["id"]], rel), short=r["minutes"] * 60 < MIN_SEC,
                 in_window=r["age_days"] is not None and r["age_days"] <= days,
                 downloaded=(out / f"W_{r['id']}" / "metadata.json").is_file())
        r["success"] = _is_success(r)
        rows.append(r)
    reasons = preselect(rows)
    for r in rows:
        r["reason"] = reasons.get(r["id"], "")
    rows.sort(key=ratio_key)                                         # 배수 높은 순 (v1.1)
    prev = _read_json(web_dir(t) / "explore.json", {})               # v1.5: 다시 탐색해도(자동 이어서 포함) 전에 있던 영상은 내가 체크한 그대로
    prev_rows, prev_checked = {r["id"] for r in prev.get("rows") or []}, set(prev.get("checked") or [])
    checked = [r["id"] for r in rows if (r["id"] in prev_checked if r["id"] in prev_rows else bool(r["reason"]))]
    data = {"topic": t, "generated": datetime.now(KST).isoformat(timespec="seconds"), "weeks": weeks, "use_keywords": use_keywords,
            "rows": rows, "checked": checked, "pending": pending, "quota_used": api.used,
            "pending_videos": state["pending_videos"], "pending_channels": state["pending_channels"],
            "searched_new": searched_new, "excluded": dict(excluded)}
    _write_json(web_dir(t) / "explore.json", data)
    log("EXPLORE", topic=t, videos=len(rows), checked=len(data["checked"]), kept_checks=len(prev_rows & {r["id"] for r in rows}),
        pending=len(pending), pending_videos=state["pending_videos"], searched_new=searched_new, quota_used=api.used,
        excluded=",".join(f"{k}:{v}" for k, v in excluded.items()) or "-", note="체크만 해 둠 — [승인]을 눌러야 자료를 받음")
    step("끝", total, total)
    return {"videos": len(rows), "checked": len(data["checked"]), "pending": pending, "pending_videos": state["pending_videos"],
            "quota_used": api.used}


# ---------------------------------------------------------------- 승인 → 자료 받기 → 주별 분석 → 음성인식 → 다시 분석 → GitHub
def job_approve(t, ids, auto_whisper=True):
    ex = _read_json(web_dir(t) / "explore.json", {})
    by_id = {r["id"]: r for r in ex.get("rows") or []}
    ids = [i for i in dict.fromkeys(ids) if i in by_id]
    if not ids:
        raise UserError("승인할 영상이 없습니다 — 목록에서 체크하세요 (탐색을 먼저)")
    api, ledger, _ = make_api(t, "web_approve")
    out = out_dir(t)
    cache = out / ".cache"
    a = types.SimpleNamespace(refresh=False, no_transcript=False, offline=False, comments=0, replies=True)
    state = orr.new_state()
    got = []
    log("APPROVE", topic=t, videos=len(ids), note="설명·자막·썸네일·댓글 전부 받음")
    try:
        for n, vid in enumerate(ids, 1):
            step(f"자료 받기 {n}/{len(ids)} — {by_id[vid]['title'][:40]}", n - 1, len(ids))
            info = _read_json(cache / f"{vid}.json", None)
            if not info:
                log("APPROVE", logging.WARNING, id=vid, note="영상 정보 캐시 없음 — 탐색을 다시")
                continue
            d = out / f"W_{vid}"
            row = {k: v for k, v in by_id[vid].items() if k not in ("sources", "reason", "downloaded", "in_window", "relevant", "short", "success")}
            row.update(rank=f"W{n}", set="web", folder=d.name, sources=by_id[vid]["sources"], url=f"https://www.youtube.com/watch?v={vid}")
            meta, cms = orr.deep_case(d, row, info, a, api, "web", {}, state)
            cms, cst = orr.comments_step(d, meta, a, api, "web", {}, state, full=True)
            n_rep = sum(1 for c in cms if c.get("parent"))
            meta.update(comments_fetched=len(cms), comments_top_level=len(cms) - n_rep, comments_replies=n_rep,
                        comments_by_creator=sum(1 for c in cms if c.get("creator")), comments_complete=cst["complete"],
                        comments_disabled=cst.get("disabled", False), approved=datetime.now(KST).isoformat(timespec="minutes"))
            (d / "metadata.json").write_text(json.dumps(meta, ensure_ascii=False, indent=1), "utf-8")
            got.append(meta)
            log("APPROVE", n=f"{n}/{len(ids)}", id=vid, transcript=meta["transcript_status"] if meta["transcript_status"] != "ok" else meta["transcript_lang"],
                comments=len(cms), comments_complete=cst["complete"], quota_used=api.used)
    finally:
        record_use(t, api, ledger, "web_approve")
    appr = _read_json(web_dir(t) / "approved.json", {"approved": []})
    appr["approved"] = list(dict.fromkeys(appr["approved"] + [m["id"] for m in got]))
    _write_json(web_dir(t) / "approved.json", appr)
    missing = [m["id"] for m in got if m["transcript_status"] != "ok"]
    base = job_baseline(t, quiet=True)          # v1.4: 같은 채널 기준선 — 새로 승인한 영상의 채널 최근 영상 (채널 하나 약 2단위)
    # v1.2: 음성인식을 기다리지 않음 — 자막을 못 받은 영상은 설명으로 대신 분석하고 바로 올림, 음성인식은 그 뒤에 뒤에서
    step(f"주별 분석 (자막 못 받은 {len(missing)}개는 영상 설명으로 대신)", len(ids), len(ids))
    rep = wa.run(t)
    got_ids = {m["id"] for m in got}
    src = collections.Counter(c["src"] for c in wa.load_cases(out) if c["meta"].get("id") in got_ids)
    res = {"videos": len(got), "transcripts_ok": len(got) - len(missing), "description_fallback": src.get("설명", 0),
           "no_text": src.get("없음", 0), "whisper_needed": len(missing), "quota_used": api.used,
           "pending_comments": len(state["pending_comments"]), "windows": len(rep["windows"]), **base}
    res.update(push_results(t, f"웹 화면 승인 {len(got)}개 — 자료·주별 분석 (자막 못 받은 {len(missing)}개는 설명으로, 음성인식은 뒤에서)"))
    if missing and auto_whisper:
        res["whisper"] = start_whisper(t, f"승인한 영상 중 자막을 못 받은 {len(missing)}개")[1]
    elif missing:
        res["whisper"] = "자동 음성인식 끔 — 화면의 [음성인식 시작]으로"
    log("APPROVE", topic=t, **{k: v for k, v in res.items()})
    step("끝 — " + ("결과를 GitHub 에 올렸습니다" if res.get("pushed") else res.get("push_note") or "PC 에 저장")
         + (" · 음성인식은 뒤에서 (화면 위 '음성인식')" if missing and auto_whisper else ""))
    return res


def push_results(t, message):
    """분석 결과와 자료(사례 폴더 — 공개 저장소에도, 분석기 v2.9.3)를 바로 GitHub 에 (분석기 --push-only, 다른 올리기와 차례로 — 분석기 v2.9.2 잠금).
    → {pushed, push_exit, push_note, materials}"""
    if not pc.find_secret("GITHUB_TOKEN", t)[0]:
        note = "GITHUB_TOKEN 없음 — 결과는 PC 에만 (화면 위 '1. 키 설정'에서 넣으면 다음부터 올라감)"
        log("PUSH", logging.WARNING, topic=t, note=note)
        return {"pushed": False, "push_note": note}
    step("GitHub 에 올리기 (분석 결과·자료)")
    lines = []                          # 진행 칸(최근 500줄)과 따로 — 승인이 많아 진행 칸이 차 있어도 올리기 출력을 읽게
    code = run_subprocess([sys.executable, "youtube_topic_analyzer.py", "--config", f"{t}/analyzer_config.toml", "--push-only",
                           "--push-message", message], "GitHub", capture=lines)
    out = "\n".join(lines)
    if re.search(r"\bfull=True\b", out):
        materials = "올림 — 사례 폴더(설명·자막·댓글 전부·썸네일)까지" + (" (공개 저장소)" if re.search(r"\bprivate=False\b", out) else "")
    elif re.search(r"\bfull=False\b", out) or "요약 파일만" in out:
        materials = "PC 에만 — 분석기 설정 UPLOAD_CASES_TO_PUBLIC_REPO 가 꺼져 있고 저장소가 공개라 사례 폴더는 올리지 않음"
    else:
        materials = "확인 못 함 (진행 칸의 GitHub 줄 참고)"
    no_change = "변경 사항 없음" in out
    note = ("바뀐 것 없음 (이미 올라가 있음)" if code == 0 and no_change else "GitHub 에 올림" if code == 0
            else f"올리기 실패 (종료 코드 {code}) — 진행 칸의 GitHub 줄 확인, [다시 분석]을 누르면 다시 올림")
    log("PUSH", logging.INFO if code == 0 else logging.WARNING, topic=t, exit=code, note=note, materials=materials)
    return {"pushed": code == 0, "push_exit": code, "push_note": note, "materials": materials}


def job_analyze(t):
    step("주별 분석·성공 사례 분석 (자막 없으면 설명으로)")
    rep = wa.run(t)
    res = {"windows": len(rep["windows"]), "cases": rep["cases"], "text_sources": rep.get("text_sources")}
    if rep["cases"]:
        res.update(push_results(t, f"웹 화면 주별 분석 다시 (승인 {rep['cases']}개)"))
    step("끝 — " + (res.get("push_note") or "승인한 영상 없음"))
    return res


def job_comments(t, quiet=False):
    """못 받은 댓글 이어 받기 (v1.3): 승인 영상(W_) 중 댓글을 다 받지 못한 것 — 받은 쪽 다음부터 (comments_state.json),
    할당량이 끝나면 멈추고 다음에 이어서. quiet=True(켤 때)면 키·할당량이 없을 때 오류 대신 건너뜀."""
    todo = []
    for d in sorted(out_dir(t).glob("W_*")):
        m = _read_json(d / "metadata.json", None)
        if m and m.get("id") and not m.get("comments_complete") and not m.get("comments_disabled"):
            todo.append((d, m))
    if not todo:
        return {"comments_todo": 0}
    try:
        api, ledger, _ = make_api(t, "web_comments")
    except UserError as e:
        if not quiet:
            raise
        log("COMMENTS", logging.WARNING, topic=t, todo=len(todo), note=f"못 받은 댓글 이어 받기 건너뜀 — {e}")
        return {"comments_todo": len(todo), "comments_skipped": str(e)}
    a = types.SimpleNamespace(refresh=False, no_transcript=False, offline=False, comments=0, replies=True)
    state = orr.new_state()
    done = got = 0
    log("COMMENTS", topic=t, todo=len(todo), quota_left=api.quota, note="못 받은 댓글 이어 받기")
    try:
        for n, (d, m) in enumerate(todo, 1):
            step(f"못 받은 댓글 이어 받기 {n}/{len(todo)} — {str(m.get('title') or '')[:40]}", n - 1, len(todo))
            cms, cst = orr.comments_step(d, m, a, api, "web", {}, state, full=True)
            n_rep = sum(1 for c in cms if c.get("parent"))
            m.update(comments_fetched=len(cms), comments_top_level=len(cms) - n_rep, comments_replies=n_rep,
                     comments_by_creator=sum(1 for c in cms if c.get("creator")), comments_complete=cst["complete"],
                     comments_disabled=cst.get("disabled", False))
            _write_json(d / "metadata.json", m)
            done += bool(cst["complete"])
            got += len(cms)
            if state["quota_stop"]:
                log("COMMENTS", logging.WARNING, topic=t, note="할당량이 끝나 멈춤 — 다음에 이어서", done=done, left=len(todo) - n)
                break
    finally:
        record_use(t, api, ledger, "web_comments")
    log("COMMENTS", topic=t, todo=len(todo), completed=done, comments=got, quota_used=api.used)
    return {"comments_todo": len(todo), "comments_completed": done, "comments_quota_used": api.used,
            "comments_quota_stop": state["quota_stop"]}


def job_supply(t, n=None):
    """[공급 확인] (v1.3): 분석의 '수요는 있는데 영상이 적어 보이는 말'(analysis.json gap_candidates) n개를 직접 검색 —
    최근 90일·길이 상관없이 조회수 순 (말 하나 = 검색 1번 100단위 + 영상 정보) → 다시 분석·올림."""
    a = _read_json(out_dir(t) / "analysis.json", {})
    words = list(a.get("gap_candidates") or [])
    days = int(((a.get("rules") or {}).get("demand") or {}).get("RECENT_DAYS") or 90)
    if n:
        words = words[:n]
    if not words:
        raise UserError("확인할 말이 없습니다 — 먼저 '검색어로도 찾기'로 탐색해 자동완성(수요)을 받고 다시 분석하세요")
    api, ledger, _ = make_api(t, "web_supply")
    cache = out_dir(t) / ".cache"
    state = orr.new_state()
    done = []
    log("SUPPLY", topic=t, words=len(words), days=days, quota_left=api.quota, note="말 하나 = 검색 1번 100단위")
    try:
        for k, w in enumerate(words, 1):
            step(f"공급 확인 {k}/{len(words)} — '{w}' 최근 {days}일 검색", k - 1, len(words))
            try:
                r = orr.search_supply(api, cache, w, days, state)
            except orr.QuotaStop as e:
                log("SUPPLY", logging.WARNING, note=f"할당량이 끝나 멈춤 — {e}", done=len(done))
                break
            done.append(w)
            log("SUPPLY", word=w, total=r.get("total"), found=len(r.get("ids") or []), cached=r.get("cached"))
    finally:
        record_use(t, api, ledger, "web_supply")
    res = {"supply_checked": len(done), "supply_quota_used": api.used}
    res.update(job_analyze(t))
    return res


BASELINE_VIDEOS = 50                     # 채널마다 최근 영상 몇 개로 '평소'를 셈 (업로드 목록 1단위 + 영상 정보 1단위)
BASELINE_TTL_H = 168                     # 채널 업로드 목록 캐시 7일 (영상 정보는 outlier_research 캐시 24시간)


def job_baseline(t, quiet=False):
    """같은 채널 기준선 (v1.4): 사례(W_·01_·P01_) 채널 중 구독자 ≤ 비교 기준(analysis_rules [compare] MAX_SUBS)인 곳의 최근 영상
    BASELINE_VIDEOS 개 (업로드 목록 + 영상 정보 — 채널 하나 약 2단위, 7일 캐시) → .cache/uploads_<채널ID>.json · .cache/<영상ID>.json
    → 분석(success_analysis 1-2번)이 '채널 평소 대비 ×'와 같은 채널 잘된 영상 vs 평소 영상을 셈. 성공 사례 채널부터, 할당량이 끝나면 멈춤."""
    plan = baseline_plan(t)
    cache, todo, fresh, need, meta_need = plan["cache"], plan["todo"], plan["fresh"], plan["need"], plan["meta_need"]
    res = {"baseline_channels": len(todo), "baseline_cached": len(fresh), "channel_meta_missing": len(meta_need)}
    if not need and not meta_need:
        log("BASELINE", topic=t, channels=len(todo), cached=len(fresh), note="채널 평소 영상·채널 정보 — 모두 캐시")
        return res
    return _baseline_fetch(t, quiet, cache, todo, fresh, need, meta_need, res)


def baseline_plan(t):
    """같은 채널 기준선에서 받을 것 (v1.5: job_baseline 에서 떼어 냄 — 자동 이어서(resume_plan)도 셈). 할당량 0."""
    od = out_dir(t)
    cache = od / ".cache"
    succ = {c.get("id"): c.get("no") or 999 for c in (_read_json(od / "analysis.json", {}).get("success_cases") or [])}
    max_subs = 50000
    try:
        rp = topic_dir(t) / "analysis_rules.toml"
        if rp.is_file():
            max_subs = int(orr.tomllib.loads(rp.read_text("utf-8")).get("compare", {}).get("MAX_SUBS", max_subs))
    except Exception as e:                  # 규칙 파일이 깨져도 기본값으로
        log("BASELINE", logging.WARNING, note=f"analysis_rules.toml 못 읽음 — 구독자 {max_subs} 이하로 — {type(e).__name__}")
    chans = {}
    for d in (od.iterdir() if od.is_dir() else []):
        if not (CASE_RX.match(d.name) and d.is_dir()):
            continue
        m = _read_json(d / "metadata.json", None)
        cid = (m or {}).get("channel_id") or ""
        if not (cid.startswith("UC") and len(cid) == 24):
            continue
        subs = m.get("subs")
        if subs is not None and subs > max_subs:
            continue
        rank = min(succ.get(m.get("id"), 999), chans.get(cid, {}).get("rank", 999))
        chans[cid] = {"id": cid, "uploads": "UU" + cid[2:], "title": m.get("channel") or cid, "rank": rank}
    todo = sorted(chans.values(), key=lambda c: (c["rank"], c["title"]))
    fresh = [c for c in todo if orr._fresh(cache / f"uploads_{c['id']}.json", BASELINE_TTL_H, False)]
    need = [c for c in todo if c not in fresh]
    # 채널 개설일·영상 수 (analysis.md 7번 '빨리 크는 작은 채널') — 탐색에서 본 영상의 채널 중 개설일이 없거나 7일 지난 것 (50채널에 1단위)
    pool = _pool_channels(t)
    try:
        known = _read_json(cache / "channels.json", {})
    except Exception:
        known = {}
    meta_need = sorted(c for c in pool if not (isinstance(known.get(c), dict) and "created" in known[c]))
    return {"cache": cache, "todo": todo, "fresh": fresh, "need": need, "meta_need": meta_need}


def _baseline_fetch(t, quiet, cache, todo, fresh, need, meta_need, res):
    try:
        api, ledger, _ = make_api(t, "web_baseline")
    except UserError as e:
        if not quiet:
            raise
        log("BASELINE", logging.WARNING, topic=t, todo=len(need), note=f"채널 평소 영상 받기 건너뜀 — {e}")
        return {**res, "baseline_skipped": str(e)}
    state = orr.new_state()
    got = 0
    log("BASELINE", topic=t, channels=len(todo), cached=len(fresh), todo=len(need), channel_meta=len(meta_need), quota_left=api.quota,
        note=f"채널 평소 영상 (최근 {BASELINE_VIDEOS}개) — 채널 하나 약 2단위, 성공 사례 채널부터 · 채널 개설일은 50채널에 1단위")
    try:
        if meta_need:
            step(f"채널 정보(개설일·영상 수) {len(meta_need)}곳 — 50곳에 1단위", 0, max(len(need), 1))
            orr.fetch_channel_subs(api, cache, set(meta_need), state)
            res["channel_meta_fetched"] = len(meta_need) - state["pending_channels"]
        for n, c in enumerate(need, 1):
            step(f"채널 평소 영상 {n}/{len(need)} — {c['title'][:30]}", n - 1, len(need))
            try:
                ids = orr.channel_uploads(api, cache, c, ttl_h=BASELINE_TTL_H, max_videos=BASELINE_VIDEOS)
                orr.fetch_video_infos(api, cache, ids[:BASELINE_VIDEOS], state)
            except orr.QuotaStop as e:
                log("BASELINE", logging.WARNING, topic=t, note=f"할당량이 끝나 멈춤 — 다음에 이어서 ({e})", done=got, left=len(need) - n + 1)
                state["quota_stop"] = state["quota_stop"] or getattr(e, "kind", "quota")
                break
            except (RuntimeError, urllib.error.URLError, OSError, ValueError, KeyError) as e:   # 채널이 지워졌거나 비공개 등 — 그 채널만
                log("BASELINE", logging.WARNING, channel=c["title"], id=c["id"], error=f"{type(e).__name__}: {e}"[:160],
                    note="이 채널만 건너뜀")
                continue
            got += 1
            if state["quota_stop"]:
                log("BASELINE", logging.WARNING, topic=t, note="할당량이 끝나 멈춤 — 다음에 이어서", done=got, left=len(need) - n)
                break
    finally:
        record_use(t, api, ledger, "web_baseline")
    log("BASELINE", topic=t, fetched=got, todo=len(need), quota_used=api.used)
    return {**res, "baseline_fetched": got, "baseline_quota_used": api.used, "baseline_quota_stop": state["quota_stop"]}


def _pool_channels(t):
    """탐색에서 본 영상(.cache/<영상ID>.json)의 채널 ID 전부 (v1.4 — 채널 개설일을 받을 대상)."""
    cache = out_dir(t) / ".cache"
    ids = set()
    for f in (cache.glob("*.json") if cache.is_dir() else []):
        if f.name.startswith(("search_", "supply_", "uploads_")) or f.name in ("channels.json", "autocomplete.json"):
            continue
        cid = (_read_json(f, {}) or {}).get("channel_id")
        if isinstance(cid, str) and cid.startswith("UC"):
            ids.add(cid)
    return ids


def job_demand(t, quiet=True):
    """수요 자료 (v1.4): 검색어(keywords.txt)마다 YouTube 자동완성 — 할당량 0, 7일 캐시. 켤 때 저절로 (예전엔 '검색어로도 찾기' 탐색 때만 받아
    탐색을 안 하면 analysis.md 3-3 이 비었음). 연결 실패가 3번 이어지면 그만."""
    qs = pc.read_keyword_list(keywords_path(t)) or []
    cache = out_dir(t) / ".cache"
    cache.mkdir(parents=True, exist_ok=True)
    new = fail = 0
    for k, q in enumerate(qs, 1):
        step(f"자동완성(사람들이 찾는 말) {k}/{len(qs)} — {q} (할당량 0)", k - 1, len(qs))
        try:
            _, hit = orr.fetch_autocomplete(q, cache)
            if not hit:
                new += 1
                time.sleep(0.2)
        except Exception as e:
            fail += 1
            if fail >= 3:
                log("AUTOCOMPLETE", logging.WARNING, note="자동완성 연결 실패가 이어짐 — 이번엔 그만 (분석은 자동완성 없이)", error=type(e).__name__)
                break
    log("AUTOCOMPLETE", topic=t, keywords=len(qs), new=new, failed=fail, note="수요 자료 (할당량 0, 켤 때)")
    return {"autocomplete_keywords": len(qs), "autocomplete_new": new, "autocomplete_failed": fail}


def job_comments_then_analyze(t):
    res = job_comments(t)
    res.update(job_analyze(t))
    return res


def job_startup(t, whisper=True):
    """화면을 켤 때 (v1.2·v1.3·v1.4): 못 받은 댓글 이어 받기 → 채널 평소 영상(같은 채널 기준선)·채널 개설일 → 자동완성(수요, 할당량 0)
    → 승인한 영상이 있으면 분석(주별·성공 사례)을 다시 만들어 올림
    → 자막 없는 영상이 남았으면 음성인식을 뒤에서."""
    res = job_comments(t, quiet=True)
    res.update(job_baseline(t, quiet=True))
    res.update(job_demand(t))
    res.update(_resume_explore(t, "켤 때"))         # v1.5: 할당량 때문에 남은 탐색(검색·영상 정보)이 있으면 이어서
    if any(out_dir(t).glob("W_*/metadata.json")):
        res.update(job_analyze(t))
    n = whisper_pending(t, fresh=True)
    res["whisper_pending"] = n
    if n and whisper:
        res["whisper"] = start_whisper(t, f"켤 때 남은 {n}개")[1]
    step("끝 — " + (res.get("push_note") or "올릴 결과 없음") + (f" · 음성인식 {n}개 남음" if n else ""))
    return res


# ---------------------------------------------------------------- 할당량 초기화 뒤 자동으로 이어서 (v1.5)
def resume_plan(t):
    """할당량 때문에 남은 것 (할당량 0으로 셈): 탐색의 못 한 검색·채널·영상 정보 · 못 받은 댓글 · 같은 채널 기준선."""
    ex = _read_json(web_dir(t) / "explore.json", {})
    pend = list(ex.get("pending") or [])
    pv = int(ex.get("pending_videos") or 0) + int(ex.get("pending_channels") or 0)
    comments = 0
    for d in sorted(out_dir(t).glob("W_*")):
        m = _read_json(d / "metadata.json", None)
        if m and m.get("id") and not m.get("comments_complete") and not m.get("comments_disabled"):
            comments += 1
    try:
        bp = baseline_plan(t)
        base = len(bp["need"]) + (1 if bp["meta_need"] else 0)
    except Exception as e:                  # 계획을 못 세워도 다른 것은 이어서
        log("RESUME", logging.WARNING, topic=t, note=f"채널 기준선 계획 실패 — {type(e).__name__}")
        base = 0
    plan = {"explore_searches": len(pend), "explore_videos": pv, "explore_weeks": ex.get("weeks"),
            "explore_keywords": ex.get("use_keywords", True), "comments": comments, "baseline": base}
    plan["any"] = bool(pend or pv or comments or base)
    return plan


def _resume_explore(t, why):
    ex = _read_json(web_dir(t) / "explore.json", {})
    if not (ex.get("pending") or ex.get("pending_videos") or ex.get("pending_channels")):
        return {}
    kl = key_ledger(t)
    need = 100 + orr.SEARCH_RESERVE if ex.get("pending") else 1
    if not kl or kl.left() < need:
        log("RESUME", topic=t, why=why, note="남은 탐색이 있지만 할당량이 모자람 — 다음 초기화 뒤에", left=kl.left() if kl else "-")
        return {"explore_resume": "할당량 모자람 — 다음 초기화 뒤"}
    log("RESUME", topic=t, why=why, pending=len(ex.get("pending") or []), pending_videos=ex.get("pending_videos") or 0,
        note="할당량 때문에 남은 탐색을 이어서 (캐시된 검색은 0단위, 체크는 그대로)")
    r = job_explore(t, int(ex.get("weeks") or 8), bool(ex.get("use_keywords", True)))
    return {"explore_resumed": True, "explore_pending_after": len(r.get("pending") or []), "explore_quota_used": r.get("quota_used")}


def job_resume(t, why="할당량 초기화"):
    """남은 것 이어서 (v1.5 — 사용자 지시 "사용량 초기화되면 자동으로 다시 분석 마저 하는거지? 그렇게 되야해"):
    못 받은 댓글 → 같은 채널 기준선 → 남은 탐색 → 분석 다시·GitHub. 각 단계는 할당량이 끝나면 멈추고 다음 초기화 때 또 이어서."""
    plan = resume_plan(t)
    log("RESUME", topic=t, why=why, **{k: v for k, v in plan.items() if k != "any"})
    res = {"plan": plan}
    res.update(job_comments(t, quiet=True))
    res.update(job_baseline(t, quiet=True))
    res.update(_resume_explore(t, why))
    if any(out_dir(t).glob("W_*/metadata.json")) and (plan["comments"] or plan["baseline"]):
        res.update(job_analyze(t))           # 댓글·기준선이 바뀌었으면 분석을 다시 만들어 올림
    after = resume_plan(t)
    res["left_after"] = {k: v for k, v in after.items() if k != "any"}
    RESUME.update(last=datetime.now(KST).isoformat(timespec="minutes"), last_result=res["left_after"])
    step("끝 — " + ("남은 것 없음" if not after["any"] else "아직 남은 것은 다음 초기화 뒤에 또 이어서"))
    return res


def _resume_loop():
    """태평양 자정 + RESUME_MARGIN_MIN 분마다 남은 것을 저절로 이어서 (이 창이 켜져 있는 동안). PC 가 잠들었다 깨도 벽시계로 다시 셈."""
    while True:
        try:
            nxt, how = pc.next_quota_reset(datetime.now(timezone.utc), margin_min=RESUME_MARGIN_MIN)
            RESUME.update(next=nxt.astimezone(KST).isoformat(timespec="minutes"), status="waiting")
            while True:
                left_s = (nxt - datetime.now(timezone.utc)).total_seconds()
                if left_s <= 0:
                    break
                time.sleep(min(60.0, left_s))
            t = STATE["topic"]
            plan = resume_plan(t)
            if not plan["any"]:
                RESUME.update(last=datetime.now(KST).isoformat(timespec="minutes"), last_result={}, note="초기화 — 남은 것 없음")
                log("RESUME", topic=t, note="할당량 초기화 — 이어서 할 것 없음")
                time.sleep(90)
                continue
            RESUME.update(status="waiting_job")
            waited = 0
            while JOB["status"] == "running" and waited < RESUME_JOB_WAIT_H * 3600:
                time.sleep(30)
                waited += 30
            ok, msg = start_job("할당량 초기화 — 남은 것 이어서", job_resume, t, "할당량 초기화")
            RESUME.update(status="started" if ok else "skipped", note=msg)
            log("RESUME", topic=t, started=ok, note=msg, waited_min=waited // 60)
            time.sleep(90)                   # 같은 초기화로 두 번 돌지 않게
        except Exception as e:               # 이어서 하기가 죽지 않게 — 기록하고 다음 초기화에
            LOG.exception("[RESUME] 실패")
            RESUME.update(status="error", note=f"{type(e).__name__}: {e}"[:200])
            time.sleep(300)


# ---------------------------------------------------------------- 음성인식 (뒤에서, v1.2)
def whisper_pending(t, fresh=False):
    """음성인식이 남은 영상 수 — 분석기 대기열과 같은 기준 (W_·01_·P01_ 중 대본 없음·자막 서버 차단·자막 없음 + 앞부분만 한 대본(2차);
    건너뜀·연결 실패·시도 한도를 넘은 것은 뺌). 화면이 자주 물어서 15초 동안은 지난 값."""
    now = time.monotonic()
    if not fresh and _PENDING_CACHE["t"] == t and now - _PENDING_CACHE["at"] < 15:
        return _PENDING_CACHE["n"]
    tag = re.sub(r"[^0-9A-Za-z가-힣]+", "_", str(t)).strip("_") or "topic"
    tried = _read_json(ROOT / ".yt_work" / f"whisper_{tag}.json", {})
    n = 0
    od = out_dir(t)
    for d in (od.iterdir() if od.is_dir() else []):
        m = CASE_RX.match(d.name)
        if not (m and d.is_dir() and (d / "metadata.json").is_file()):
            continue
        if (d / "transcript.json").is_file():     # v1.4: 앞부분만 한 대본(partial_sec — 분석기 v2.10.0 1차)은 2차(전체)가 남음
            if _read_json(d / "transcript.json", {}).get("partial_sec"):
                rec = tried.get(m.group(1) + "#full") or {}
                n += not (rec.get("done") or rec.get("attempts", 0) >= WHISPER_MAX_ATTEMPTS)
            continue
        st = str(_read_json(d / "metadata.json", {}).get("transcript_status") or "")
        if st == "ok" or st.startswith(SKIP_TRANSCRIPT) or any(w in st for w in NETWORK_FAIL_WORDS):
            continue
        rec = tried.get(m.group(1)) or {}
        if rec.get("done") or rec.get("attempts", 0) >= WHISPER_MAX_ATTEMPTS:
            continue
        n += 1
    _PENDING_CACHE.update(t=t, at=now, n=n)
    return n


def whisper_view():
    w = {k: (list(v)[-120:] if k == "log" else v) for k, v in WHISPER.items() if k not in ("proc", "stop")}
    t = WHISPER["topic"] or STATE["topic"]
    try:
        w["pending"] = whisper_pending(t) if t else 0
    except Exception:
        w["pending"] = None
    return w


def start_whisper(t, why=""):
    """음성인식을 뒤에서 시작. 이미 도는 중이면 '끝나면 다시'만 표시 (새로 승인한 영상도 이어서). → (시작했나, 설명)."""
    with WHISPER_LOCK:
        if WHISPER["status"] in ("running", "stopping"):
            WHISPER["rerun"] = True
            return False, "음성인식이 이미 도는 중 — 지금 대기열이 끝나면 새 영상도 이어서"
        WHISPER.update(status="running", topic=t, started=datetime.now(KST).isoformat(timespec="seconds"), finished=None, current="",
                       done=0, failed=0, total=0, rerun=False, stop=False, last_exit=None, note=why, proc=None, **{"pass": ""})
        WHISPER["log"].clear()
    log("WHISPER", topic=t, note=f"뒤에서 시작 — {why}" if why else "뒤에서 시작")
    threading.Thread(target=_whisper_loop, args=(t,), daemon=True, name="whisper").start()
    return True, "음성인식을 뒤에서 시작 — 성공 사례부터 1차(앞 5분) → 2차(전체), 하나 끝날 때마다 분석을 다시 만들고 15분마다·차수 끝에 올림"


def stop_whisper():
    with WHISPER_LOCK:
        if WHISPER["status"] != "running":
            return False
        WHISPER.update(stop=True, status="stopping", rerun=False)
        p = WHISPER.get("proc")
    if p:
        p.terminate()
    log("WHISPER", logging.WARNING, note="사용자가 멈춤 — 끝난 영상의 대본은 남음, 하던 영상은 다음에 처음부터")
    return True


def _whisper_loop(t):
    try:
        while True:
            has_token = bool(pc.find_secret("GITHUB_TOKEN", t)[0])
            cmd = [sys.executable, "youtube_topic_analyzer.py", "--config", f"{t}/analyzer_config.toml", "--whisper-queue"] + \
                  ([] if has_token else ["--no-push"])
            WHISPER.update(done=0, failed=0, total=0, current="", **{"pass": ""})
            code = _whisper_run(cmd)
            WHISPER["last_exit"] = code
            _PENDING_CACHE["at"] = 0.0
            with WHISPER_LOCK:
                again = WHISPER["rerun"] and not WHISPER["stop"]
                WHISPER["rerun"] = False
            if not again:
                break
            log("WHISPER", topic=t, note="새로 승인한 영상도 이어서")
    except Exception as e:
        WHISPER["note"] = f"오류: {type(e).__name__}: {e}"[:200]
        LOG.exception("[WHISPER] 실패")
    finally:
        with WHISPER_LOCK:
            stopped = WHISPER["stop"]
            WHISPER.update(status="stopped" if stopped else "idle", finished=datetime.now(KST).isoformat(timespec="seconds"), proc=None,
                           current="")
        log("WHISPER", topic=t, done=WHISPER["done"], failed=WHISPER["failed"], exit=WHISPER["last_exit"],
            note="멈춤" if stopped else "대기열 끝")


def _whisper_run(cmd):
    env = {**os.environ, "PYTHONIOENCODING": "utf-8", "PYTHONUTF8": "1"}
    log("WHISPER", cmd=" ".join(str(c) for c in cmd[1:]))
    p = subprocess.Popen(cmd, cwd=ROOT, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    WHISPER["proc"] = p
    for raw in p.stdout:
        line = raw.decode("utf-8", errors="replace").rstrip()
        WHISPER["log"].append(line)
        m = WHISPER_ITEMS_RX.search(line)
        if m:                           # 차수가 바뀌면 n/전체를 새로 셈 (v1.4 — 분석기 v2.10.0: 1차 앞 5분 → 2차 전체)
            WHISPER.update(total=int(m.group(1)), done=0, failed=0, current="")
            WHISPER["pass"] = (m.group(2) or "").strip('"')
        m = WHISPER_LINE_RX.search(line)
        if m:
            n, total, what, rest = int(m.group(1)), int(m.group(2)), m.group(3), m.group(4)
            WHISPER["total"] = total
            if what == "시작":
                title = re.search(r'title=("([^"]*)"|\S+)', rest)
                WHISPER["current"] = f"{n}/{total} " + ((title.group(2) if title.group(2) is not None else title.group(1)) if title else "")
            elif what == "끝":
                WHISPER["done"] += 1
                _PENDING_CACHE["at"] = 0.0
            elif what == "실패":
                WHISPER["failed"] += 1
        if "이미 도는 중" in line:
            WHISPER["note"] = "다른 창(자동 실행)에서 음성인식이 이미 도는 중 — 그쪽이 하나씩 올림"
        if WHISPER["stop"]:
            p.terminate()
    code = p.wait()
    WHISPER["proc"] = None
    return code


# ---------------------------------------------------------------- 화면 상태
def state_view(t):
    ex = _read_json(web_dir(t) / "explore.json", {})
    kp = keywords_path(t)
    text = kp.read_text("utf-8-sig") if kp.is_file() else ""
    until = orr.caption_blocked()
    STATE["topics"] = sorted(set(find_topics()) | {t}, key=lambda x: (x != "economic", x))     # v1.5: 새로 만든 주제 폴더도
    wins = open_windows()
    return {"version": VERSION, "topic": t, "name": topic_name(t), "topics": STATE["topics"], "env": env_view(t),
            "topic_names": {x: topic_name(x) for x in STATE["topics"]}, "windows": wins, "port": STATE.get("port"),
            "resume": {**{k: v for k, v in RESUME.items()}, "plan": resume_plan(t)},
            "keywords_text": text, "keywords_count": len(pc.read_keyword_list(kp) or []), "targets": load_targets(t),
            "explore": {"generated": ex.get("generated"), "weeks": ex.get("weeks"), "videos": len(ex.get("rows") or []),
                        "checked": len(ex.get("checked") or []), "pending": ex.get("pending") or []},
            "quota": quota_view(t),
            "caption_block": until.astimezone(KST).strftime("%m-%d %H:%M") if until else None,
            "approved": len(_read_json(web_dir(t) / "approved.json", {"approved": []})["approved"]),
            "job": job_view()}


PAGE = None      # 아래 HTML (파일 끝)


class Handler(BaseHTTPRequestHandler):
    server_version = "AnalyzerUI/" + VERSION

    def log_message(self, fmt, *args):          # 접속 기록은 남기지 않음 (화면이 1초마다 묻기 때문)
        pass

    def _send(self, code, body, ctype="application/json; charset=utf-8"):
        data = body if isinstance(body, bytes) else json.dumps(body, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(data)

    def _host_ok(self):
        host = (self.headers.get("Host") or "").split(":")[0]
        return host in ("127.0.0.1", "localhost")

    def _authorized(self):
        return self._host_ok() and secrets.compare_digest(self.headers.get("X-Token") or "", TOKEN)

    def do_GET(self):
        if not self._host_ok():
            return self._send(403, {"error": "이 PC 에서만 열 수 있습니다"})
        u = urllib.parse.urlparse(self.path)
        if u.path in ("/", "/index.html"):
            return self._send(200, PAGE.replace("{{TOKEN}}", TOKEN).encode("utf-8"), "text/html; charset=utf-8")
        if u.path == "/favicon.ico":                         # 브라우저가 저절로 묻는 아이콘 — 없음 (403 오류로 보이지 않게)
            self.send_response(204)
            self.end_headers()
            return
        if not self._authorized():
            return self._send(403, {"error": "열쇠가 맞지 않음 — 화면을 새로 고침"})
        t = STATE["topic"]
        q = urllib.parse.parse_qs(u.query)
        try:
            if u.path == "/api/state":
                return self._send(200, state_view(t))
            if u.path == "/api/job":                                   # v1.5: 남은 할당량·자동 이어서도 (화면이 1~3초마다 물음)
                return self._send(200, {**job_view(), "whisper": whisper_view(), "quota": quota_view(t),
                                        "resume": {k: v for k, v in RESUME.items()}})
            if u.path == "/api/explore":
                ex = _read_json(web_dir(t) / "explore.json", {})
                used = used_ids(t)                                     # 이미 분석에 쓴 영상은 뺌 (승인하면 바로 빠짐)
                rows = sorted((r for r in ex.get("rows") or [] if r["id"] not in used), key=ratio_key)
                return self._send(200, {"rows": rows, "checked": [i for i in ex.get("checked") or [] if i not in used],
                                        "generated": ex.get("generated"), "weeks": ex.get("weeks"), "excluded": ex.get("excluded") or {},
                                        "used_hidden": sum(1 for r in ex.get("rows") or [] if r["id"] in used)})
            if u.path == "/api/estimate":
                weeks = max(1, min(52, int((q.get("weeks") or ["8"])[0])))
                return self._send(200, estimate(t, weeks, (q.get("kw") or ["1"])[0] == "1"))
            if u.path == "/api/report":
                return self._send(200, _read_json(out_dir(t) / "weekly.json", {}))
            if u.path == "/api/analysis":                      # v1.3: 성공 사례 분석 요약 (전문은 analysis.md)
                a = _read_json(out_dir(t) / "analysis.json", {})
                return self._send(200, {k: a.get(k) for k in ("generated", "sources", "limits", "missing_success_total", "tool", "gap_candidates")}
                                  | {"success": len(a.get("success_cases") or []),
                                     "missing_ids": [x["id"] for x in a.get("missing_success") or []],
                                     "needs": [(c["name"], c["count"]) for c in (a.get("needs") or {}).get("categories") or []],
                                     "market_themes": [(r["theme"], r["index"], r["videos"]) for r in (a.get("market") or {}).get("themes") or []
                                                       if not r.get("small_sample")][:6],
                                     "gaps": [(r["phrase"], r["pool_recent"], (r.get("verified") or {}).get("total"))
                                              for r in ((a.get("market") or {}).get("autocomplete") or [])[:8]],
                                     "fast_channels": len((a.get("growth") or {}).get("fast") or []),
                                     "baseline": {k: (a.get("baseline") or {}).get(k) for k in ("success_covered", "channels", "hits", "normal")},
                                     "formats": [(r["format"].split(" (")[0], r.get("success_share"), r.get("market_index")) for r in a.get("formats") or []],
                                     "requests": (a.get("needs") or {}).get("requests_total")})
        except UserError as e:
            return self._send(400, {"error": str(e)})
        except Exception as e:
            LOG.exception("GET %s", u.path)
            return self._send(500, {"error": f"{type(e).__name__}: {e}"[:300]})
        return self._send(404, {"error": "없는 주소"})

    def do_POST(self):
        if not self._authorized():
            return self._send(403, {"error": "열쇠가 맞지 않음 — 화면을 새로 고침"})
        n = int(self.headers.get("Content-Length") or 0)
        if n > 2_000_000:
            return self._send(413, {"error": "너무 큼"})
        try:
            body = json.loads(self.rfile.read(n).decode("utf-8") or "{}")
        except ValueError:
            return self._send(400, {"error": "JSON 이 아님"})
        t = STATE["topic"]
        path = urllib.parse.urlparse(self.path).path
        try:
            if path == "/api/topic":                                   # v1.5: 창마다 주제 하나 (다른 창이 쓰는 주제는 못 고름)
                nt = str(body.get("topic") or "")
                if nt not in find_topics():
                    raise UserError("없는 주제 폴더 (<폴더>/analyzer_config.toml 이 있어야 함)")
                if nt != t:
                    if JOB["status"] == "running":
                        raise UserError(f"'{JOB['name']}' 작업이 도는 중 — 끝난 뒤(또는 [멈춤] 뒤)에 주제를 바꾸세요. 동시에 하려면 [새 창으로 열기]")
                    if WHISPER["status"] in ("running", "stopping"):
                        raise UserError("음성인식이 도는 중 — 멈춘 뒤 주제를 바꾸세요. 동시에 하려면 [새 창으로 열기]")
                    claim_topic(nt)
                    STATE["topic"] = nt
                    log("TOPIC", topic=nt, note="이 창의 주제를 바꿈")
                return self._send(200, state_view(STATE["topic"]))
            if path == "/api/topic/new":                               # v1.5: 새 주제 폴더
                r = create_topic(body.get("folder"), body.get("name"), body.get("keywords"), bool(body.get("push")))
                return self._send(200, r)
            if path == "/api/window/new":                              # v1.5: 다른 주제를 새 창(다른 포트)으로 — 동시에 탐색
                nt = str(body.get("topic") or "")
                if nt not in find_topics():
                    raise UserError("없는 주제 폴더")
                w = topic_window(nt) if nt != t else {"url": f"http://127.0.0.1:{STATE['port']}/"}
                if w is not None:
                    return self._send(200, {"ok": False, "url": w.get("url"), "message": "이미 열린 창이 있습니다"})
                spawn_windows([nt])
                return self._send(200, {"ok": True, "message": f"'{nt}' 새 창을 띄웠습니다 — 브라우저 탭이 하나 더 열립니다 (몇 초)"})
            if path == "/api/resume":                                  # v1.5: [지금 이어서] — 초기화를 기다리지 않고 남은 것을 이어서
                ok, msg = start_job("남은 것 이어서", job_resume, t, "화면에서")
                return self._send(200 if ok else 409, {"ok": ok, "message": msg})
            if path == "/api/env":
                changed = []
                for name in ENV_NAMES:
                    v = str(body.get(name) or "").strip().strip('"').strip("'")
                    if not v:
                        continue
                    if re.search(r"\s", v):
                        raise UserError(f"{name}: 값에 띄어쓰기·줄바꿈이 있으면 안 됩니다")
                    src = pc.find_secret(name, t)[1]             # 지금 쓰는 파일에 저장 (주제 .env 가 먼저 읽히므로)
                    set_env_value(ROOT / t / ".env" if src == f"{t}/.env" else ROOT / ".env", name, v)
                    os.environ.pop(name, None)                   # 예전 환경 변수보다 .env 를 쓰게
                    changed.append(name)
                log("ENV", changed=",".join(changed) or "-", note="값은 로그에 쓰지 않음")
                return self._send(200, {"changed": changed, "env": env_view(t)})
            if path == "/api/keywords":
                text = str(body.get("text") or "")
                data = (text.replace("\r\n", "\n").rstrip("\n") + "\n").encode("utf-8")
                kp = keywords_path(t)
                kp.write_bytes(data)
                kws = pc.read_keyword_list(kp) or []
                msg = f"PC 에 저장 ({len(kws)}개)"
                if body.get("push"):
                    ok, note = github_put(t, f"{t}/{pc.KEYWORD_LIST_FILE}", data, f"[{topic_name(t)}] 검색어 고침 (웹 화면, {len(kws)}개)")
                    msg += " · " + note
                log("KEYWORDS", topic=t, keywords=len(kws), note=msg)
                return self._send(200, {"count": len(kws), "message": msg})
            if path == "/api/targets/add":
                return self._send(200, {"results": add_targets(t, body.get("text")), "targets": load_targets(t)})
            if path == "/api/targets/remove":
                return self._send(200, {"targets": remove_target(t, body.get("kind"), body.get("id"))})
            if path == "/api/checked":
                ex = _read_json(web_dir(t) / "explore.json", {})
                if ex:
                    ok_ids = {r["id"] for r in ex.get("rows") or []}
                    ex["checked"] = [i for i in body.get("ids") or [] if i in ok_ids]
                    _write_json(web_dir(t) / "explore.json", ex)
                return self._send(200, {"checked": len(ex.get("checked") or [])})
            if path == "/api/explore":
                weeks = max(1, min(52, int(body.get("weeks") or 8)))
                ok, msg = start_job("탐색", job_explore, t, weeks, bool(body.get("keywords", True)))
                return self._send(200 if ok else 409, {"ok": ok, "message": msg})
            if path == "/api/approve":
                ok, msg = start_job("승인 — 자료 받고 분석", job_approve, t, list(body.get("ids") or []), bool(body.get("whisper", True)))
                return self._send(200 if ok else 409, {"ok": ok, "message": msg})
            if path == "/api/analyze":
                ok, msg = start_job("주별 분석", job_analyze, t)
                return self._send(200 if ok else 409, {"ok": ok, "message": msg})
            if path == "/api/supply":
                n = max(1, min(30, int(body.get("n") or 10)))
                ok, msg = start_job("공급 확인 — 수요는 있는데 영상이 적어 보이는 말", job_supply, t, n)
                return self._send(200 if ok else 409, {"ok": ok, "message": msg})
            if path == "/api/comments":
                ok, msg = start_job("못 받은 댓글 이어 받기", job_comments_then_analyze, t)
                return self._send(200 if ok else 409, {"ok": ok, "message": msg})
            if path == "/api/whisper":
                ok, msg = start_whisper(t, "화면에서 [음성인식 시작]")
                return self._send(200, {"ok": ok, "message": msg})
            if path == "/api/whisper/stop":
                return self._send(200, {"ok": stop_whisper()})
            if path == "/api/cancel":
                JOB["cancel"] = True
                p = JOB.get("proc")
                if p:
                    p.terminate()
                return self._send(200, {"ok": True})
        except UserError as e:
            return self._send(400, {"error": str(e)})
        except Exception as e:
            LOG.exception("POST %s", path)
            return self._send(500, {"error": f"{type(e).__name__}: {e}"[:300]})
        return self._send(404, {"error": "없는 주소"})


CHILDREN = []          # v1.5: 이 창이 띄운 다른 주제 창 (이 창을 끄면 같이 끔)
SPAWN_OPTS = {"flags": []}


def spawn_windows(topics):
    """다른 주제를 새 창(프로세스·포트)으로 (v1.5). 출력은 .yt_work/web_ui_<주제>.log. 같은 키의 할당량은 키 장부로 함께 셈."""
    for t in topics:
        logp = ROOT / ".yt_work" / f"web_ui_{_window_tag(t)}.log"
        cmd = [sys.executable, str(Path(__file__).resolve()), t, "--port", str((STATE.get("port") or 8765) + 1), "--no-sync",
               "--skip-install", "--log-file", str(logp)] + SPAWN_OPTS["flags"]
        env = {**os.environ, "PYTHONIOENCODING": "utf-8", "PYTHONUTF8": "1"}
        err = open(logp.with_suffix(".err.log"), "a", encoding="utf-8")
        CHILDREN.append(subprocess.Popen(cmd, cwd=ROOT, env=env, stdout=subprocess.DEVNULL, stderr=err))
        log("WINDOW", topic=t, note="이 주제는 새 창(다른 포트)으로 — 브라우저 탭이 하나 더 열림", log_file=str(logp.relative_to(ROOT)))


def serve(port, host="127.0.0.1"):
    for p in range(port, port + 20):
        try:
            return ThreadingHTTPServer((host, p), Handler), p
        except OSError:
            continue
    raise SystemExit(f"[START] ❌ {port}~{port + 19} 번 포트를 모두 쓰는 중 — --port 로 다른 번호")


def main(argv=None):
    global orr, wa
    ap = argparse.ArgumentParser(description="분석기 웹 화면 — 키·검색어 고치기, 탐색 → 체크 → 승인 → 자료 받기·주별 분석")
    ap.add_argument("topics", nargs="*", help="주제 폴더 (없으면 설정 파일이 있는 폴더 — economic 먼저)")
    ap.add_argument("--port", type=int, default=8765)
    ap.add_argument("--no-browser", action="store_true")
    ap.add_argument("--no-sync", action="store_true", help="GitHub 에서 설정·검색어를 받지 않음")
    ap.add_argument("--skip-install", action="store_true")
    ap.add_argument("--no-whisper", action="store_true", help="켤 때 음성인식을 뒤에서 시작하지 않음 (화면의 [음성인식 시작]으로)")
    ap.add_argument("--no-startup", action="store_true", help="켤 때 주별 분석 다시 만들기·올리기를 하지 않음")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    ap.add_argument("--log-file", default="", help=argparse.SUPPRESS)          # v1.5: 다른 주제 창(spawn_windows)이 따로 쓰는 기록 파일
    ap.add_argument("--no-resume", action="store_true", help="할당량 초기화 뒤 남은 것을 저절로 이어서 하지 않음")
    a = ap.parse_args(argv)
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass
    fmt = logging.Formatter("%(message)s")
    root_log = logging.getLogger()
    root_log.setLevel(getattr(logging, a.log_level))
    for h in (logging.StreamHandler(sys.stdout), _JobLogHandler()):
        h.setFormatter(fmt)
        root_log.addHandler(h)
    (ROOT / ".yt_work").mkdir(exist_ok=True)
    fh = logging.FileHandler(Path(a.log_file) if a.log_file else ROOT / ".yt_work" / "web_ui.log", encoding="utf-8")
    fh.setFormatter(fmt)
    root_log.addHandler(fh)
    topics = a.topics or find_topics()
    if not topics:
        raise SystemExit("[START] ❌ 주제 폴더(<폴더>/analyzer_config.toml)가 없음 — run_analyzer.ps1 로 받거나 폴더 이름 확인")
    if "economic" in topics:
        topics = ["economic"] + [x for x in topics if x != "economic"]
    STATE.update(topic=topics[0], topics=topics)
    SPAWN_OPTS["flags"] = ["--log-level", a.log_level] + [f for f, on in (("--no-browser", a.no_browser), ("--no-whisper", a.no_whisper),
                                                                           ("--no-startup", a.no_startup), ("--no-resume", a.no_resume)) if on]
    # v1.5: 창마다 주제 하나 — 같은 주제가 이미 다른 창에 열려 있으면 그 창을 열고 끝 (같은 주제를 두 창이 동시에 쓰지 않게)
    free = [t for t in topics if topic_window(t) is None]
    if not free:
        other = topic_window(topics[0]) or {}
        url = other.get("url") or ""
        log("START", topics=",".join(topics), note="이 주제는 이미 다른 분석기 창에 열려 있음 — 그 창을 씀", url=url or "-")
        print(f"\n  ▶ '{topics[0]}' 분석기 화면은 이미 열려 있습니다: {url or '(다른 창)'}\n    다른 주제를 동시에 하려면: run_analyzer.ps1 -Folder <주제>\n", flush=True)
        if url and not a.no_browser:
            webbrowser.open(url)
        return 0
    if not a.skip_install and not pc.ensure_packages(False):
        raise SystemExit("[START] ❌ 패키지 설치 실패 — 위 오류 확인")
    if not a.no_sync:                         # v1.3: 코드도 — 실행기 목록에 없는 새 도구(tools/success_analysis.py)가 PC 에 오게 (불러오기 전에)
        for k, t in enumerate(topics):
            try:
                res = pc.sync_from_github(t, code=(k == 0))
                got = [r for r, v in res.items() if v in ("새로 받음", "GitHub 새 판으로 바꿈")]
                log("SYNC", topic=t, updated=",".join(got) or "-", note="GitHub 최신 설정·코드 (이 화면 자신은 다음 실행부터)")
            except Exception as e:
                log("SYNC", logging.WARNING, topic=t, note="GitHub 에서 설정·코드를 받지 못함 — PC 파일로", error=f"{type(e).__name__}"[:80])
    import outlier_research as _orr
    import weekly_analysis as _wa
    orr, wa = _orr, _wa
    srv, port = serve(a.port)
    STATE["port"] = port
    mine = None
    for t in free:                            # v1.5: 이 창의 주제 (잠금) — 켜는 사이 다른 창이 먼저 잡았으면 다음 주제
        try:
            claim_topic(t)
            mine = t
            break
        except UserError as e:
            log("START", logging.WARNING, topic=t, note=str(e))
    if mine is None:
        srv.server_close()
        print("\n  ▶ 고른 주제가 모두 다른 창에 열려 있습니다 — 그 창을 쓰세요\n", flush=True)
        return 0
    STATE["topic"] = mine
    url = f"http://127.0.0.1:{port}/"
    log("START", url=url, topics=",".join(topics), tool=f"web_ui.py {VERSION}",
        note="이 창을 닫으면 화면도 꺼집니다 (Ctrl+C 로 끝냄)")
    print(f"\n  ▶ 분석기 화면: {url}\n    (브라우저가 안 열리면 위 주소를 복사해 여세요. 끝내려면 이 창에서 Ctrl+C)\n", flush=True)
    if not a.no_browser:
        threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    if not a.no_startup:                      # v1.2: 승인한 영상 결과를 새로 만들어 올리고, 남은 음성인식은 뒤에서
        start_job("켤 때 — 분석 결과 올리기", job_startup, STATE["topic"], not a.no_whisper)
    if not a.no_resume:                       # v1.5: 할당량 초기화(태평양 자정 +10분) 뒤 남은 것을 저절로 이어서
        threading.Thread(target=_resume_loop, daemon=True, name="resume").start()
        log("RESUME", topic=STATE["topic"], next_kst=pc.next_quota_reset(datetime.now(timezone.utc), RESUME_MARGIN_MIN)[0].astimezone(KST)
            .strftime("%m-%d %H:%M"), note="할당량이 끝나 남은 것은 초기화 뒤 저절로 이어서 (이 창을 켜 둔 동안)")
    if a.topics and len(a.topics) > 1:        # v1.5: 주제를 여러 개 주면 나머지 주제는 창을 하나씩 (동시에 탐색)
        spawn_windows([t for t in free if t != mine])
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        log("DONE", note="화면을 끔")
    finally:
        srv.server_close()
        release_topic()
        for c in CHILDREN:                    # 이 창이 띄운 다른 주제 창도 끔
            if c.poll() is None:
                c.terminate()
        for holder in (WHISPER, JOB):          # 음성인식·올리기도 같이 끝냄 (하던 영상은 다음에 처음부터)
            p = holder.get("proc")
            if p and p.poll() is None:
                p.terminate()
    return 0


PAGE = r"""<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="t" content="{{TOKEN}}"><title>분석기</title>
<style>
:root{--bg:#f7f7f5;--card:#fff;--fg:#1d1d1f;--mut:#6b6b70;--line:#e3e3e0;--acc:#2563eb;--acc2:#1d4ed8;--ok:#15803d;--warn:#b45309;--bad:#b91c1c;--chip:#eef2ff;--row:#fafaf9}
@media (prefers-color-scheme:dark){:root{--bg:#111113;--card:#1a1a1d;--fg:#ececee;--mut:#a0a0a8;--line:#2c2c31;--acc:#5b8cff;--acc2:#7aa2ff;--ok:#4ade80;--warn:#fbbf24;--bad:#f87171;--chip:#1e2540;--row:#161618}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:14px/1.5 -apple-system,"Segoe UI","Malgun Gothic","Apple SD Gothic Neo",sans-serif}
header{position:sticky;top:0;z-index:5;background:var(--card);border-bottom:1px solid var(--line);padding:10px 16px;display:flex;gap:14px;align-items:center;flex-wrap:wrap}
header h1{font-size:17px;margin:0}header .pill{font-size:12px;color:var(--mut);background:var(--bg);border:1px solid var(--line);border-radius:99px;padding:2px 10px}
main{max-width:1280px;margin:0 auto;padding:16px;display:grid;gap:14px}main>*,.two>*{min-width:0}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px 16px}
.card h2{font-size:15px;margin:0 0 10px}.card h2 small{font-weight:400;color:var(--mut);margin-left:6px}
.row{display:flex;gap:8px;align-items:center;flex-wrap:wrap}.grow{flex:1;min-width:200px}
input[type=text],input[type=password],input[type=number],textarea,select{font:inherit;color:var(--fg);background:var(--bg);border:1px solid var(--line);border-radius:8px;padding:7px 10px}
textarea{width:100%;min-height:180px;font-family:ui-monospace,Consolas,monospace;font-size:13px}
button{font:inherit;border:1px solid var(--line);background:var(--bg);color:var(--fg);border-radius:8px;padding:7px 14px;cursor:pointer}
button.pri{background:var(--acc);border-color:var(--acc);color:#fff;font-weight:600}button.pri:hover{background:var(--acc2)}
button:disabled{opacity:.5;cursor:not-allowed}.mut{color:var(--mut)}.ok{color:var(--ok)}.warn{color:var(--warn)}.bad{color:var(--bad)}
.two{display:grid;grid-template-columns:1fr 1fr;gap:14px}@media (max-width:860px){.two{grid-template-columns:1fr}}
.chip{display:inline-flex;gap:6px;align-items:center;background:var(--chip);border-radius:99px;padding:3px 6px 3px 10px;margin:3px 4px 0 0;font-size:13px}
.chip button{padding:0 7px;border:0;background:transparent;color:var(--mut)}
.tablewrap{overflow:auto;max-height:620px;border:1px solid var(--line);border-radius:8px}
table{border-collapse:collapse;width:100%;font-size:13px}th,td{padding:6px 8px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top;white-space:nowrap}
th{position:sticky;top:0;background:var(--card);z-index:1;font-weight:600}td.t{white-space:normal;min-width:260px}tr.on{background:var(--row)}
td.n,th.n{text-align:right;font-variant-numeric:tabular-nums}a{color:var(--acc)}
.tag{font-size:11px;border-radius:6px;padding:1px 6px;background:var(--bg);border:1px solid var(--line);margin-right:3px}
.tag.s{border-color:var(--ok);color:var(--ok)}.tag.d{border-color:var(--acc);color:var(--acc)}
.bar{height:6px;background:var(--line);border-radius:9px;overflow:hidden}.bar i{display:block;height:100%;background:var(--acc);width:0}
pre{background:var(--bg);border:1px solid var(--line);border-radius:8px;padding:10px;max-height:260px;overflow:auto;font-size:12px;white-space:pre-wrap;margin:8px 0 0}
details{border:1px solid var(--line);border-radius:8px;padding:8px 12px;margin-top:8px}summary{cursor:pointer;font-weight:600}
.msg{min-height:20px;font-size:13px}h3.sub{font-size:14px;margin:14px 0 6px}.tag.x{border-color:var(--warn);color:var(--warn)}.k{display:grid;grid-template-columns:150px 1fr;gap:8px;align-items:center;margin-bottom:8px}
@media (max-width:600px){.k{grid-template-columns:1fr}}
</style></head><body>
<header><h1 id="title">분석기</h1><select id="topic" title="주제 폴더 — 창 하나에 주제 하나 (다른 주제는 새 창으로 동시에)"></select>
<span class="pill" id="quota">할당량 …</span><span class="pill" id="caption">자막 서버 …</span><span class="pill" id="wPill">음성인식 …</span><span class="pill" id="ver"></span></header>
<main>
<section class="card"><h2>0. 주제 · 할당량 <small>창 하나에 주제 하나 — 다른 주제는 새 창으로 동시에 탐색 · 할당량은 같은 키를 쓰는 모든 창·주제가 함께</small></h2>
 <div class="row"><b id="qBig">할당량 …</b><span class="mut" id="qReset"></span></div>
 <div class="bar" style="margin-top:6px"><i id="qBar"></i></div>
 <div class="mut" id="qBy" style="margin-top:6px"></div>
 <div class="row" style="margin-top:6px"><span class="grow mut" id="resumeInfo"></span><button id="resumeNow" title="초기화를 기다리지 않고 남은 탐색·댓글·채널 기준선을 지금 이어서 (남은 할당량만큼)">지금 이어서</button></div>
 <div class="mut" id="winInfo" style="margin-top:4px"></div>
 <details><summary>다른 주제를 새 창으로 · 새 주제 만들기</summary>
  <div class="row" style="margin-top:8px"><select id="winTopic"></select><button id="winOpen">새 창으로 열기</button><span class="msg" id="winMsg"></span></div>
  <h3 class="sub">새 주제 만들기 <small class="mut">— economic 설정을 틀로 <code>&lt;폴더&gt;/analyzer_config.toml · keywords.txt · keywords.toml</code></small></h3>
  <div class="k"><label for="ntFolder">폴더 이름 (영어 소문자)</label><input type="text" id="ntFolder" placeholder="예: health"></div>
  <div class="k"><label for="ntName">주제 이름</label><input type="text" id="ntName" placeholder="예: 건강"></div>
  <div class="k"><label for="ntKw">검색어 (한 줄에 하나)</label><textarea id="ntKw" style="min-height:90px"></textarea></div>
  <div class="row"><button class="pri" id="ntMake">주제 폴더 만들기</button><label><input type="checkbox" id="ntPush" checked> GitHub 에도 저장</label><span class="msg" id="ntMsg"></span></div>
  <div class="mut">관련어(주제와 관련된 영상 가리기)는 비어 있게 만들어집니다 — 비어 있으면 모든 검색 결과를 주제 관련으로 봅니다. 다듬으려면 Claude 에게 '&lt;주제&gt; 검색어 만들어줘'.</div>
 </details>
</section>
<div class="two">
 <section class="card"><h2>1. 키 설정 <small>.env — 끝 4자리만 보입니다</small></h2>
  <div class="k"><label for="ytkey">YouTube API 키</label><div><input type="password" id="ytkey" class="grow" style="width:100%" placeholder="바꿀 때만 붙여넣기" autocomplete="off"><div class="mut" id="ytkey_now"></div></div></div>
  <div class="k"><label for="ghtok">GitHub 토큰</label><div><input type="password" id="ghtok" style="width:100%" placeholder="바꿀 때만 붙여넣기" autocomplete="off"><div class="mut" id="ghtok_now"></div></div></div>
  <div class="row"><button class="pri" id="saveEnv">키 저장</button><span class="msg" id="envMsg"></span></div>
 </section>
 <section class="card"><h2>2. 검색어 <small>한 줄에 하나 · # 은 메모</small></h2>
  <textarea id="kw" spellcheck="false"></textarea>
  <div class="row" style="margin-top:8px"><button class="pri" id="saveKw">검색어 저장</button>
   <label><input type="checkbox" id="kwPush" checked> GitHub 에도 저장</label><span class="mut" id="kwCount"></span><span class="msg" id="kwMsg"></span></div>
 </section>
</div>
<section class="card"><h2>3. 직접 추가 <small>영상 주소 → 그 영상 · 채널 주소나 @이름 → 그 채널에 올라온 영상 전부 · 여러 개는 한 줄에 하나</small></h2>
 <div class="row" style="align-items:flex-start"><textarea id="tgIn" class="grow" style="min-height:70px" placeholder="https://www.youtube.com/watch?v=…&#10;https://www.youtube.com/@채널이름&#10;(여러 개를 한 번에 붙여넣어도 됩니다)"></textarea><button class="pri" id="tgAdd">추가</button></div>
 <div class="msg" id="tgMsg"></div>
 <div id="tgList" style="margin-top:6px"></div>
</section>
<section class="card"><h2>4. 탐색 <small>목록만 만듭니다 — 자료는 승인한 영상만 받습니다</small></h2>
 <div class="row">최근 <input type="number" id="weeks" min="1" max="52" value="8" style="width:70px"> 주
  <label><input type="checkbox" id="useKw" checked> 검색어로도 찾기</label>
  <span class="mut" id="est"></span><button class="pri" id="explore">탐색</button></div>
</section>
<section class="card" id="listCard"><h2>5. 탐색 목록 <small id="listInfo">배수 높은 순 · 추천은 체크해 둠</small></h2>
 <div class="row" style="margin-bottom:8px"><input type="text" id="flt" class="grow" placeholder="제목·채널 거르기">
  <label><input type="checkbox" id="fShort"> 짧은 영상(4분 미만)도</label><label><input type="checkbox" id="fRel" checked> 주제 관련만</label>
  <button id="chkAll">보이는 것 모두 체크</button><button id="chkNone">모두 해제</button><button id="chkRec">추천만</button></div>
 <h3 class="sub">✅ 체크한 영상 <span id="onCount"></span> <small class="mut">— 승인하면 이 영상들의 자료를 받습니다</small></h3>
 <div class="tablewrap"><table><thead><tr><th></th><th>업로드</th><th>제목</th><th>채널</th><th class="n">구독자</th><th class="n">조회수</th><th class="n">배수 ▼</th><th class="n">하루 조회수</th><th class="n">길이</th><th>추천 · 출처</th></tr></thead><tbody id="rowsOn"><tr><td colspan="10" class="mut">탐색을 누르면 여기에 나옵니다</td></tr></tbody></table></div>
 <h3 class="sub">☐ 체크 안 한 영상 <span id="offCount"></span></h3>
 <div class="tablewrap"><table><thead><tr><th></th><th>업로드</th><th>제목</th><th>채널</th><th class="n">구독자</th><th class="n">조회수</th><th class="n">배수 ▼</th><th class="n">하루 조회수</th><th class="n">길이</th><th>추천 · 출처</th></tr></thead><tbody id="rowsOff"><tr><td colspan="10" class="mut">—</td></tr></tbody></table></div>
 <div class="row" style="margin-top:10px"><button class="pri" id="approve">승인 — 자료 받고 분석해서 바로 올리기</button><label><input type="checkbox" id="autoW" checked> 그다음 자막 못 받은 영상 음성인식 (뒤에서)</label><span class="mut" id="chkInfo"></span></div>
 <div class="mut" style="margin-top:6px">순서: 자료(설명·자막·썸네일·댓글) 받기 → 채널 평소 영상(같은 채널 기준선, 채널 하나 약 2단위) → 분석 (자막을 못 받은 영상은 영상 설명으로 대신) → GitHub 에 바로 올림 → 음성인식은 뒤에서 (성공 사례부터 앞 5분 → 전체)</div>
</section>
<section class="card"><h2>진행 <small id="jobName"></small></h2>
 <div class="row"><span id="jobStep" class="grow">쉬는 중</span><button id="cancel" disabled>멈춤</button><button id="reanalyze" title="주별 분석·성공 사례 분석을 다시 만들어 GitHub 에 올림">다시 분석·올리기</button><button id="comments" title="할당량이 끝나 다 받지 못한 댓글을 이어 받고 다시 분석">못 받은 댓글 이어 받기</button></div>
 <div class="msg" id="jobRes"></div>
 <div class="bar" style="margin-top:8px"><i id="jobBar"></i></div><pre id="jobLog"></pre>
</section>
<section class="card"><h2>음성인식 <small>뒤에서 하나씩 · 성공 사례부터 1차(앞 5분) → 2차(전체) · 끝날 때마다 분석을 다시 만들고 15분마다·차수 끝에 올림 · 도는 동안에도 탐색·승인 가능</small></h2>
 <div class="row"><span id="wStep" class="grow">쉬는 중</span><button id="wStart">음성인식 시작</button><button id="wStop" disabled>멈춤</button></div>
 <div class="bar" style="margin-top:8px"><i id="wBar"></i></div>
 <details><summary>음성인식 기록</summary><pre id="wLog"></pre></details>
</section>
<section class="card"><h2>6. 분석 결과 <small>성공 사례 분석 analysis.md (지시사항 재료) · 주별 추세 weekly.md</small></h2>
 <div id="analysis" class="mut" style="margin-bottom:12px"></div>
 <h3 class="sub">주별 추세 <small class="mut">— 승인한 영상 전부 (최근 1주부터 한 주씩 넓힘, 누적)</small></h3>
 <div id="report" class="mut">승인한 영상이 생기면 여기에 나옵니다</div></section>
</main>
<script>
const T=document.querySelector('meta[name=t]').content;let ROWS=[],CHECK=new Set(),REC=new Set(),busy=false,lastJob=null,waitDone=false,lastWDone=null,TOPICS={names:{},windows:[]},PLAN=null;
const $=id=>document.getElementById(id);const esc=s=>String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const num=x=>x==null?'–':(typeof x==='number'?x.toLocaleString('ko-KR',{maximumFractionDigits:1}):x);
async function api(p,b){const r=await fetch(p,{method:b?'POST':'GET',headers:{'X-Token':T,'Content-Type':'application/json'},body:b?JSON.stringify(b):undefined});
 const j=await r.json().catch(()=>({error:'응답 오류'}));if(!r.ok)throw new Error(j.error||j.message||r.status);return j}
function say(id,t,cls){const e=$(id);e.textContent=t;e.className='msg '+(cls||'')}
async function loadState(){const s=await api('/api/state');$('title').textContent=s.name+' 분석기';$('ver').textContent='web_ui '+s.version;
 renderTopics(s);PLAN=s.resume&&s.resume.plan;renderQuota(s.quota);renderResume(s.resume);
 $('caption').textContent=s.caption_block?`자막 서버 차단 — ${s.caption_block}까지 쉬는 중 (음성인식으로)`:'자막 서버 정상';$('caption').className='pill '+(s.caption_block?'warn':'');
 const e=s.env;$('ytkey_now').innerHTML=e.YOUTUBE_API_KEY.set?`<span class=ok>설정됨</span> ${esc(e.YOUTUBE_API_KEY.tail)} · ${esc(e.YOUTUBE_API_KEY.source)}`:'<span class=bad>없음</span> — 넣어야 탐색할 수 있습니다';
 $('ghtok_now').innerHTML=e.GITHUB_TOKEN.set?`<span class=ok>설정됨</span> ${esc(e.GITHUB_TOKEN.tail)} · ${esc(e.GITHUB_TOKEN.source)}`:'없음 — 결과는 PC 에만 저장';
 if(document.activeElement!==$('kw'))$('kw').value=s.keywords_text;$('kwCount').textContent=`검색어 ${s.keywords_count}개`;
 renderTargets(s.targets);showJob(s.job);estimate();return s}
function hm(m){return m>=60?`${Math.floor(m/60)}시간 ${m%60}분`:`${m}분`}
function renderQuota(q){if(!q)return;
 if(q.key===null){$('quota').textContent='할당량 — 키 없음';$('quota').className='pill warn';$('qBig').textContent='YouTube API 키를 넣으면 남은 할당량이 보입니다';$('qBy').textContent='';return}
 const pct=Math.min(100,Math.round(100*q.used/Math.max(1,q.budget)));
 $('quota').textContent=`남은 할당량 ${num(q.left)} / ${num(q.budget)} · 초기화 ${q.reset_kst} (${hm(q.reset_in_min)} 뒤)`;
 $('quota').className='pill '+(q.left<=0?'bad':q.left<1000?'warn':'ok');
 $('qBig').textContent=q.exhausted?`오늘 할당량 끝 — Google 이 하루 한도라고 답함 (장부상 쓴 양 ${num(q.used)})`:`남은 ${num(q.left)}단위 · 오늘 쓴 ${num(q.used)} / ${num(q.budget)}`;
 $('qReset').textContent=` · 하루 ${num(q.limit)} − 여유 ${num(q.margin)} · 초기화 한국 시간 ${q.reset_kst} (${hm(q.reset_in_min)} 뒤)`;
 $('qBar').style.width=pct+'%';$('qBar').style.background=q.left<=0?'var(--bad)':q.left<1000?'var(--warn)':'var(--acc)';
 const bt=Object.entries(q.by_topic||{}).filter(x=>x[1]).map(([k,v])=>`${esc(k)} ${num(v)}`).join(' · ');
 const bw=Object.entries(q.by_what||{}).filter(x=>x[1]).sort((a,b)=>b[1]-a[1]).slice(0,6).map(([k,v])=>`${esc(k)} ${num(v)}`).join(' · ');
 $('qBy').innerHTML=`주제별 ${bt||'—'} · 작업별 ${bw||'—'} <span class=mut>(같은 키를 쓰는 이 PC 의 모든 창·자동 실행 합계 — 다른 PC·클라우드에서 쓴 양은 모름, 그때는 Google 의 한도 답으로 멈춤)</span>`}
function renderResume(r){if(!r)return;const p=PLAN||{};
 const parts=[p.explore_searches?`검색 ${p.explore_searches}개`:'',p.explore_videos?`영상 정보 ${p.explore_videos}개`:'',p.comments?`댓글 못 받은 영상 ${p.comments}개`:'',p.baseline?`채널 기준선 ${p.baseline}곳`:''].filter(Boolean);
 const nx=r.next?`다음 자동 이어서: 한국 시간 ${r.next.slice(5,16).replace('T',' ')}`:'자동 이어서 꺼짐 (--no-resume)';
 $('resumeInfo').textContent=(parts.length?`할당량 때문에 남은 것: ${parts.join(' · ')} → ${nx}`:`남은 것 없음 · ${nx}`)+(r.status==='waiting_job'?' · 지금 작업이 끝나길 기다리는 중':'')+(r.last?` · 지난번 ${r.last.slice(5,16).replace('T',' ')}`:'')}
function renderTopics(s){TOPICS={names:s.topic_names||{},windows:s.windows||[]};
 const other=Object.fromEntries(TOPICS.windows.filter(w=>!w.me).map(w=>[w.topic,w.url]));
 $('topic').innerHTML=s.topics.map(t=>`<option value="${esc(t)}" ${t===s.topic?'selected':''}>${esc(t)}/ · ${esc(TOPICS.names[t]||t)}${other[t]?' (다른 창에 열림)':''}</option>`).join('');
 const rest=s.topics.filter(t=>t!==s.topic);
 $('winTopic').innerHTML=rest.length?rest.map(t=>`<option value="${esc(t)}">${esc(t)}/ · ${esc(TOPICS.names[t]||t)}${other[t]?' (이미 열림 — 그 창으로)':''}</option>`).join(''):'<option value="">다른 주제 없음 — 아래에서 만들기</option>';
 $('winInfo').innerHTML='열린 창: '+TOPICS.windows.map(w=>w.me?`<b>${esc(w.topic)}</b> (이 창)`:`<a href="${esc(w.url)}" target=_blank rel=noopener>${esc(w.topic)}</a>`).join(' · ')}
function renderTargets(tg){const c=tg.channels.map(x=>`<span class=chip>📺 ${esc(x.title||x.id)} <span class=mut>영상 ${num(x.videos)}개</span><button data-k=channel data-id="${esc(x.id)}" title="빼기">✕</button></span>`);
 const v=tg.videos.map(x=>`<span class=chip>▶ ${esc((x.title||x.id).slice(0,40))}<button data-k=video data-id="${esc(x.id)}" title="빼기">✕</button></span>`);
 $('tgList').innerHTML=(c.concat(v).join(''))||'<span class=mut>추가한 영상·채널 없음</span>';
 $('tgList').querySelectorAll('button').forEach(b=>b.onclick=async()=>{const r=await api('/api/targets/remove',{kind:b.dataset.k,id:b.dataset.id});renderTargets(r.targets);estimate()})}
let estT;function estimate(){clearTimeout(estT);estT=setTimeout(async()=>{try{const e=await api(`/api/estimate?weeks=${$('weeks').value}&kw=${$('useKw').checked?1:0}`);
 $('est').textContent=`검색 ${e.searches}번 (캐시 ${e.cached}) + 채널 ${e.channels}·영상 ${e.videos} → 약 ${num(e.units)}단위`+(e.left!=null?` · 오늘 남은 ${num(e.left)}`+(e.units>e.left?' (모자라는 만큼은 초기화 뒤 저절로 이어서)':''):'')}catch(x){$('est').textContent=x.message}},250)}
async function loadRows(){const d=await api('/api/explore');ROWS=d.rows;CHECK=new Set(d.checked);REC=new Set(ROWS.filter(r=>r.reason).map(r=>r.id));
 const ex=Object.entries(d.excluded||{}).map(([k,v])=>`${k} ${v}개`);if(d.used_hidden)ex.unshift(`이미 분석에 쓴 영상 ${d.used_hidden}개`);
 $('listInfo').textContent=(d.generated?`배수 높은 순 · ${d.generated.slice(0,16).replace('T',' ')} 탐색 (최근 ${d.weeks}주) · 영상 ${ROWS.length.toLocaleString()}개 · 추천은 체크해 둠`:'배수 높은 순 · 추천은 체크해 둠')+(ex.length?` · 뺀 것: ${ex.join(', ')}`:'');renderRows()}
function byRatio(a){return a.sort((x,y)=>((y.ratio??-1)-(x.ratio??-1))||(y.views-x.views))}
function visible(){const f=$('flt').value.trim().toLowerCase();return ROWS.filter(r=>(r.sources.includes('주소')||(($('fShort').checked||!r.short)&&(!$('fRel').checked||r.relevant)))
 &&(!f||(r.title+' '+r.channel).toLowerCase().includes(f)))}
function rowHtml(r){const src=r.sources.map(s=>s.startsWith('검색:')?'🔎'+s.slice(3):s.startsWith('채널:')?'📺'+s.slice(3):'▶ 추가').slice(0,3).join(' ');
  return `<tr class="${CHECK.has(r.id)?'on':''}"><td><input type=checkbox data-id="${r.id}" ${CHECK.has(r.id)?'checked':''}></td><td>${esc(r.published)}<div class=mut>${r.age_days}일 전</div></td>
  <td class=t><a href="${r.url}" target=_blank rel=noopener>${esc(r.title)}</a></td><td>${esc(r.channel)}</td><td class=n>${r.subs==null?'비공개':num(r.subs)}</td><td class=n>${num(r.views)}</td>
  <td class=n>${r.ratio==null?'–':num(r.ratio)}</td><td class=n>${num(r.views_per_day)}</td><td class=n>${num(r.minutes)}분</td>
  <td>${r.reason?`<span class="tag ${r.reason==='성공 사례'?'s':''}">${esc(r.reason)}</span>`:''}${r.flag?`<span class="tag x">${esc(r.flag)}</span>`:''}<span class=mut>${esc(src)}</span></td></tr>`}
function fill(id,list,empty){$(id).innerHTML=list.length?list.slice(0,3000).map(rowHtml).join('')+(list.length>3000?`<tr><td colspan=10 class=mut>앞 3,000개만 보입니다 — 거르기를 쓰세요 (전체 ${list.length.toLocaleString()}개)</td></tr>`:''):`<tr><td colspan=10 class=mut>${empty}</td></tr>`}
function renderRows(){if(!ROWS.length){$('rowsOn').innerHTML='<tr><td colspan=10 class=mut>탐색을 누르면 여기에 나옵니다</td></tr>';$('rowsOff').innerHTML='<tr><td colspan=10 class=mut>—</td></tr>';$('onCount').textContent='';$('offCount').textContent='';updChk();return}
 const vs=visible(),on=byRatio(vs.filter(r=>CHECK.has(r.id))),off=byRatio(vs.filter(r=>!CHECK.has(r.id)));
 fill('rowsOn',on,'체크한 영상 없음 — 아래 표에서 체크하세요');fill('rowsOff',off,'체크 안 한 영상 없음');
 $('onCount').textContent=`${on.length.toLocaleString()}개`;$('offCount').textContent=`${off.length.toLocaleString()}개`;
 document.querySelectorAll('#rowsOn input[type=checkbox],#rowsOff input[type=checkbox]').forEach(c=>c.onchange=()=>{c.checked?CHECK.add(c.dataset.id):CHECK.delete(c.dataset.id);renderRows();saveChk()});updChk()}
function updChk(){$('chkInfo').textContent=`체크 ${CHECK.size.toLocaleString()}개 / 목록 ${ROWS.length.toLocaleString()}개`;$('approve').disabled=busy||!CHECK.size}
let chkT;function saveChk(){clearTimeout(chkT);chkT=setTimeout(()=>api('/api/checked',{ids:[...CHECK]}).catch(()=>{}),700)}
function showJob(j){if(j.quota)renderQuota(j.quota);if(j.resume)renderResume(j.resume);busy=j.status==='running';$('jobName').textContent=j.name?`${j.name} — ${({running:'도는 중',done:'끝',error:'오류',cancelled:'멈춤',idle:''})[j.status]||j.status}`:'';
 $('jobStep').innerHTML=j.status==='error'?`<span class=bad>${esc(j.error)}</span>`:esc(j.step||'쉬는 중');
 $('jobBar').style.width=j.total?Math.round(100*j.done/j.total)+'%':(busy?'15%':'0');$('cancel').disabled=!busy;
 ['explore','reanalyze','comments','resumeNow'].forEach(id=>$(id).disabled=busy);updChk();
 const r=j.result||{};$('jobRes').innerHTML=j.status==='done'&&(r.push_note||r.materials||r.whisper)?[r.push_note?`GitHub: ${esc(r.push_note)}`:'',
  r.description_fallback!=null?`자막 ${r.transcripts_ok}개 · 설명으로 대신 ${r.description_fallback}개${r.no_text?` · 글 없음 ${r.no_text}개`:''}`:'',
  r.materials?`<span class="${String(r.materials).startsWith('PC')?'warn':'ok'}">자료(사례 폴더): ${esc(r.materials)}</span>`:'',r.whisper?`음성인식: ${esc(r.whisper)}`:''].filter(Boolean).join('<br>'):'';
 const L=$('jobLog'),atEnd=L.scrollTop+L.clientHeight>=L.scrollHeight-20;L.textContent=(j.log||[]).join('\n');if(atEnd)L.scrollTop=L.scrollHeight;
 if(j.whisper)showWhisper(j.whisper);
 if((lastJob==='running'||waitDone)&&j.status!=='running'){waitDone=false;loadState();loadRows().then(loadAnalysis);loadReport()}lastJob=j.status}
function showWhisper(w){const run=w.status==='running'||w.status==='stopping';const left=w.pending==null?'':` · 남은 ${num(w.pending)}개`;
 $('wPill').textContent=run?`음성인식${w.pass?' '+w.pass:''} ${w.done}/${w.total||'…'}${w.failed?` (실패 ${w.failed})`:''}`:`음성인식 쉬는 중${left}`;$('wPill').className='pill '+(run?'ok':'');
 $('wStep').innerHTML=run?`${w.status==='stopping'?'멈추는 중… ':''}${esc(w.current||'준비 중 (소리 받기·모델 불러오기)')} <span class=mut>${w.pass?esc(w.pass)+' — ':''}끝 ${w.done} · 실패 ${w.failed} / 이번 대기열 ${w.total||'…'}${left}${w.rerun?' · 끝나면 새로 승인한 영상도':''}</span>`
  :`${w.status==='stopped'?'멈춤':'쉬는 중'}${left}${w.finished?` <span class=mut>(마지막 ${esc(w.finished.slice(5,16).replace('T',' '))} — 끝 ${w.done} · 실패 ${w.failed})</span>`:''}${w.note?` <span class=mut>${esc(w.note)}</span>`:''}`;
 $('wBar').style.width=w.total?Math.round(100*(w.done+w.failed)/w.total)+'%':(run?'5%':'0');$('wStart').disabled=run;$('wStop').disabled=!run||w.status==='stopping';
 const L=$('wLog'),atEnd=L.scrollTop+L.clientHeight>=L.scrollHeight-20;L.textContent=(w.log||[]).join('\n');if(atEnd)L.scrollTop=L.scrollHeight;
 if(lastWDone!==null&&w.done!==lastWDone){loadReport();loadAnalysis()}lastWDone=w.done}
async function poll(){try{showJob(await api('/api/job'))}catch(e){}setTimeout(poll,busy?1000:3000)}
function pct(x){return x==null?'–':Math.round(x*100)+'%'}
let MISSING=[];
async function loadAnalysis(){let a;try{a=await api('/api/analysis')}catch(e){return}
 if(!a.generated){$('analysis').innerHTML='<span class=mut>성공 사례 분석은 승인한 영상이 생기면 만들어집니다 (analysis.md)</span>';return}
 const s=a.sources||{},ts=Object.entries(s.success_text_sources||{}).map(([k,v])=>`${k} ${v}`).join(' · ')||'-';MISSING=a.missing_ids||[];
 const inList=MISSING.filter(id=>ROWS.some(r=>r.id===id)).length;
 $('analysis').innerHTML=`<div><b>성공 사례 ${a.success}개</b> <span class=mut>(${esc(a.generated.slice(0,16).replace('T',' '))} UTC · 기준 통과 ${s.success_passed} − 뺀 것 ${(s.success_excluded||[]).length} − 채널당 제한 ${(s.success_channel_cut||[]).length})</span>
  · 글 출처 ${esc(ts)} · 댓글 ${num(s.success_comments_fetched)}/${num(s.success_comments_reported)} · 비교 집단 ${num(s.compare_group)}개 (성공 ${pct(s.compare_rate)})</div>
  <div>시청자 니즈: ${(a.needs||[]).map(([n,c])=>esc(n.split(' (')[0])+' '+num(c)).join(' · ')}${a.requests!=null?` <span class=mut>(그중 '다뤄 주세요·알려 주세요' 요청 ${num(a.requests)}개 — analysis.md 8-1)</span>`:''}</div>
  <div>형식(성공 사례 몫·시장 지수): ${(a.formats||[]).map(([f,sh,ix])=>esc(f)+' '+pct(sh)+(ix!=null?' · '+num(ix):'')).join(' / ')||'<span class=mut>자료 없음</span>'}</div>
  <div>수요/공급 지수 (1보다 크면 영상이 모자라 보임): ${(a.market_themes||[]).map(([t,i,v])=>esc(t)+' <b>'+num(i)+'</b>').join(' · ')||'<span class=mut>자료 없음</span>'}</div>
  <div>찾는데 영상이 적어 보이는 말: ${(a.gaps||[]).map(([p,n,tot])=>esc(p)+` <span class=mut>(본 영상 ${n}${tot!=null?` · 결과 ${num(tot)}`:''})</span>`).join(', ')||'<span class=mut>자동완성 자료 없음 — 검색어로 탐색하면 받음</span>'}
   ${(a.gap_candidates||[]).length?`<button id="supply">공급 확인 ${(a.gap_candidates||[]).length}개 (≈${(a.gap_candidates||[]).length*100+20}단위)</button>`:''}</div>
  <div>같은 채널 기준선: 성공 사례 ${num((a.baseline||{}).success_covered)}/${num(a.success)}개에 '채널 평소 대비' · 잘된 영상 ${num((a.baseline||{}).hits)} vs 평소 영상 ${num((a.baseline||{}).normal)} <span class=mut>(채널 평소 영상은 켤 때·승인 때 받음, analysis.md 1-2번)</span></div>
  <div>빨리 크는 작은 채널: ${num(a.fast_channels)}곳 <span class=mut>(analysis.md 7번)</span></div>
  ${a.missing_success_total?`<div class=warn style="margin-top:4px">자료를 받지 않은 성공 후보 ${a.missing_success_total}개 — 승인하면 분석에 들어갑니다 <button id="chkMissing" ${inList?'':'disabled'}>성공 후보 체크 (지금 목록에 ${inList}개)</button></div>`:''}
  <details><summary>한계 ${(a.limits||[]).length}개</summary><ul>${(a.limits||[]).map(x=>`<li>${esc(x)}</li>`).join('')}</ul></details>
  <div class=mut>전문(주제·제목·썸네일·구성·니즈·사례별): GitHub 의 economic/result/outliers/analysis.md</div>`;
 const sb=$('supply');if(sb)sb.onclick=()=>{const n=(a.gap_candidates||[]).length;if(!confirm(`수요는 있는데 영상이 적어 보이는 말 ${n}개를 직접 검색합니다 (최근 90일).\n말 하나 = 검색 1번 100단위 → 약 ${n*100+20}단위`))return;startJob('/api/supply',{n})};
 const b=$('chkMissing');if(b)b.onclick=()=>{MISSING.forEach(id=>{if(ROWS.some(r=>r.id===id))CHECK.add(id)});renderRows();saveChk();$('listCard').scrollIntoView({behavior:'smooth'})}}
function srcTxt(w){const s=w.text_sources;return s?`${s['자막']||0}·${s['음성인식']||0}·${s['설명']||0}`:num(w.transcripts)}
async function loadReport(){const r=await api('/api/report');if(!r.windows){$('report').innerHTML='<span class=mut>승인한 영상이 생기면 여기에 나옵니다</span>';return}
 const ts=r.text_sources||{};let h=`<div class=mut>${esc(r.generated.slice(0,16).replace('T',' '))} UTC · 승인 영상 ${r.cases}개 (글 출처: 자막 ${ts['자막']||0} · 음성인식 ${ts['음성인식']||0} · 설명으로 대신 ${ts['설명']||0} · 없음 ${ts['없음']||0}) · 승인 영상 표는 approved.md · ${esc(r.criteria)}${r.older_than_windows?` · ${r.max_weeks}주보다 오래된 영상 ${r.older_than_windows}개는 마지막 '전체' 창에`:''}</div>
 <div class=tablewrap style="margin-top:8px"><table><thead><tr><th>창</th><th class=n>영상</th><th class=n>채널</th><th class=n>이번 주 새로</th><th class=n>조회수 중앙값</th><th class=n>하루 조회수</th><th class=n>배수</th><th class=n>성공 사례</th><th class=n>길이(분)</th><th class=n>제목 글자</th><th class=n title="분석에 쓴 글: 자막 · 음성인식 · 설명(자막을 못 받아 대신)">글 출처 자막·음성·설명</th><th class=n>댓글</th></tr></thead><tbody>`;
 h+=r.windows.map(w=>`<tr><td>${esc(w.label)}</td><td class=n>${w.videos}</td><td class=n>${w.channels}</td><td class=n>${w.new_this_week.length}</td><td class=n>${num(w.views_median)}</td><td class=n>${num(w.views_per_day_median)}</td><td class=n>${num(w.ratio_median)}</td><td class=n>${w.success}</td><td class=n>${num(w.minutes_median)}</td><td class=n>${num(w.title_len_avg)}</td><td class=n>${srcTxt(w)}</td><td class=n>${num(w.comments)}</td></tr>`).join('')+'</tbody></table></div>';
 h+=r.windows.filter(w=>w.videos).map(w=>`<details><summary>${esc(w.label)} — 영상 ${w.videos}개 (이번 주 새로 ${w.new_this_week.length})</summary>
  ${w.title_features.length?`<p><b>제목 특징</b> ${w.title_features.slice(0,6).map(f=>esc(f.name)+' '+pct(f.share)).join(' · ')}</p>`:''}
  ${w.title_words.length?`<p><b>자주 쓴 낱말</b> ${w.title_words.map(x=>esc(x.word)+'('+x.count+')').join(', ')}</p>`:''}
  ${w.content_words&&w.content_words.length?`<p><b>내용에 자주 나온 낱말</b> <span class=mut>(자막·음성인식, 없으면 설명)</span> ${w.content_words.map(x=>esc(x.word)+'('+x.count+')').join(', ')}</p>`:''}
  ${w.hooks.length?`<p><b>도입부</b> <span class=mut>(자막·음성인식은 첫 20초${w.transcripts?` · 말 속도 ${num(w.syl_per_sec_median)} 음절/초`:''}, 없으면 설명 앞부분)</span></p><ul>${w.hooks.map(x=>`<li><span class="tag ${x.src==='설명'?'x':'d'}">${esc(x.src||'자막')}</span>${esc(x.title.slice(0,30))}: “${esc(x.hook)}”</li>`).join('')}</ul>`:''}
  ${w.comment_needs.length?`<p><b>댓글 ${num(w.comments)}개 니즈</b> ${w.comment_needs.map(n=>esc(n.name)+' '+pct(n.share)).join(' · ')}</p><ul>${w.top_comments.map(c=>`<li>👍${num(c.likes)} “${esc(c.text)}”</li>`).join('')}</ul>`:''}
  <p><b>상위 영상</b> (하루 조회수 순)</p><ol>${w.top_videos.map(v=>`<li><a href="${v.url}" target=_blank rel=noopener>${esc(v.title)}</a> <span class=mut>${esc(v.channel)} · ${num(v.views)}회 · 하루 ${num(v.views_per_day)} · ${v.published}</span></li>`).join('')}</ol></details>`).join('');
 $('report').innerHTML=h}
$('topic').onchange=async()=>{const nt=$('topic').value;const w=TOPICS.windows.find(x=>x.topic===nt&&!x.me);
 if(w){window.open(w.url,'_blank');await loadState();return}
 try{await api('/api/topic',{topic:nt});await loadState();await loadRows();await loadReport();await loadAnalysis()}catch(e){alert(e.message);await loadState()}};
$('winOpen').onclick=async()=>{const nt=$('winTopic').value;if(!nt)return;try{const r=await api('/api/window/new',{topic:nt});
 if(!r.ok&&r.url)window.open(r.url,'_blank');say('winMsg',r.message,r.ok?'ok':'');setTimeout(loadState,5000)}catch(e){say('winMsg',e.message,'bad')}};
$('ntMake').onclick=async()=>{try{const r=await api('/api/topic/new',{folder:$('ntFolder').value.trim(),name:$('ntName').value.trim(),keywords:$('ntKw').value,push:$('ntPush').checked});
 say('ntMsg',r.message+' — 위 주제 목록에서 고르거나 [새 창으로 열기]','ok');$('ntFolder').value='';$('ntName').value='';$('ntKw').value='';await loadState()}catch(e){say('ntMsg',e.message,'bad')}};
$('resumeNow').onclick=()=>startJob('/api/resume',{});
$('saveEnv').onclick=async()=>{try{const r=await api('/api/env',{YOUTUBE_API_KEY:$('ytkey').value,GITHUB_TOKEN:$('ghtok').value});$('ytkey').value='';$('ghtok').value='';
 say('envMsg',r.changed.length?`저장함: ${r.changed.join(', ')}`:'바뀐 것 없음 (넣은 칸만 저장)','ok');loadState()}catch(e){say('envMsg',e.message,'bad')}};
$('saveKw').onclick=async()=>{try{const r=await api('/api/keywords',{text:$('kw').value,push:$('kwPush').checked});say('kwMsg',r.message,'ok');$('kwCount').textContent=`검색어 ${r.count}개`;estimate()}catch(e){say('kwMsg',e.message,'bad')}};
$('tgAdd').onclick=async()=>{const v=$('tgIn').value.trim();if(!v)return;say('tgMsg','확인 중…');try{const r=await api('/api/targets/add',{text:v});
 const ok=r.results.filter(x=>x.ok),bad=r.results.filter(x=>!x.ok);
 $('tgMsg').innerHTML=ok.map(x=>`<span class=ok>✓ ${x.kind==='channel'?`채널 ${esc(x.title)} (영상 ${num(x.videos)}개)`:`영상 ${esc(x.title||x.id)}`}${x.note?' — '+esc(x.note):''}</span>`).concat(
  bad.map(x=>`<span class=bad>✕ ${esc(x.input.slice(0,60))} — ${esc(x.error)}</span>`)).join('<br>');$('tgMsg').className='msg';
 $('tgIn').value=bad.map(x=>x.input).join('\n');renderTargets(r.targets);estimate()}catch(e){say('tgMsg',e.message,'bad')}};
$('tgIn').onkeydown=e=>{if(e.key==='Enter'&&(e.ctrlKey||e.metaKey))$('tgAdd').click()};
$('weeks').oninput=estimate;$('useKw').onchange=estimate;
async function startJob(p,b){try{waitDone=true;await api(p,b);busy=true;showJob(await api('/api/job'))}catch(e){waitDone=false;alert(e.message)}}
$('explore').onclick=()=>startJob('/api/explore',{weeks:+$('weeks').value,keywords:$('useKw').checked});
$('approve').onclick=async()=>{const ids=ROWS.filter(r=>CHECK.has(r.id)).map(r=>r.id);if(!ids.length)return;
 if(!confirm(`체크한 영상 ${ids.length}개의 설명·자막·썸네일·댓글 전부를 받고 → 주별 분석 → GitHub 에 바로 올립니다.\n자막을 못 받은 영상은 영상 설명으로 대신 분석하고, 음성인식은 그다음 뒤에서 합니다.\n(댓글 100개에 할당량 1단위)`))return;
 startJob('/api/approve',{ids,whisper:$('autoW').checked})};
$('cancel').onclick=()=>api('/api/cancel',{});$('reanalyze').onclick=()=>startJob('/api/analyze',{});$('comments').onclick=()=>startJob('/api/comments',{});
$('wStart').onclick=async()=>{try{const r=await api('/api/whisper',{});if(!r.ok)alert(r.message);showJob(await api('/api/job'))}catch(e){alert(e.message)}};
$('wStop').onclick=async()=>{if(!confirm('음성인식을 멈출까요? (끝난 영상의 대본은 남고, 하던 영상은 다음에 처음부터)'))return;await api('/api/whisper/stop',{});showJob(await api('/api/job'))};
['flt','fShort','fRel'].forEach(id=>$(id).addEventListener('input',renderRows));
$('chkAll').onclick=()=>{visible().forEach(r=>CHECK.add(r.id));renderRows();saveChk()};$('chkNone').onclick=()=>{CHECK.clear();renderRows();saveChk()};
$('chkRec').onclick=()=>{CHECK=new Set(REC);renderRows();saveChk()};
loadState().then(()=>{loadRows().then(loadAnalysis);loadReport()}).catch(e=>document.body.insertAdjacentHTML('afterbegin',`<p class=bad style="padding:16px">${esc(e.message)}</p>`));poll();
</script></body></html>
"""


if __name__ == "__main__":
    sys.exit(main())
