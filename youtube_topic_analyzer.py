#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v2.0.0 — 2026-10-09 — 내 PC(Windows/Mac/Linux)에서 실행하는 단일 스크립트로 전환 (.env 키 · 패키지 자동 설치)
r"""
YouTube 주제 분석기 — 구독자 0명 채널이 조회수를 가장 잘 받을 영상 찾기
(연구·교육용 분석 도구입니다. 투자 조언이 아니며, 통계는 상관관계일 뿐 인과관계를 보장하지 않습니다.)

[처음 한 번]
  1) Python 3.10 이상 설치  (Windows: python.org 설치 화면에서 'Add python.exe to PATH' 체크)
  2) Git 설치 (결과를 GitHub에 올릴 때 필요)  https://git-scm.com/downloads
  3) 이 파일이 있는 폴더에서 터미널(Windows: PowerShell / Mac: 터미널) 열고:
       python -m venv .venv
       Windows:  .venv\Scripts\activate        Mac/Linux:  source .venv/bin/activate
       python youtube_topic_analyzer.py
     → 처음 실행하면 같은 폴더에 .env 파일이 생깁니다. 메모장으로 열어 키를 넣고 저장한 뒤 다시 실행하세요.
     → 필요한 패키지는 자동으로 설치됩니다 (AUTO_INSTALL_PACKAGES).

[실행 예]
  python youtube_topic_analyzer.py                                  # 아래 [설정] 그대로 실행
  python youtube_topic_analyzer.py --topic 부동산 --folder realestate # 주제·저장 폴더만 바꿔서 실행
  python youtube_topic_analyzer.py --no-push --cases 3              # GitHub 푸시 없이, 성공사례 3개만
  python youtube_topic_analyzer.py --help                           # 전체 옵션

[결과]
  PC:      <이 폴더>/output/<PROJECT_FOLDER>/<RESULT_FOLDER>/  — README.md(리포트), analysis.xlsx, charts/, data/,
           success_cases/(대본·영상·썸네일), run_info.json, run_log.txt
  GitHub:  <GITHUB_REPO> 저장소의 <PROJECT_FOLDER>/<RESULT_FOLDER>/  (상위 폴더가 없으면 자동 생성)
"""

# =====================================================================================================
# [설정 1] 🔑 키 — 이 파일이 아니라 같은 폴더의 `.env` 파일에 넣습니다 (처음 실행 시 자동 생성, GitHub에 올라가지 않음)
#   YOUTUBE_API_KEY=...   (필수)
#   GITHUB_TOKEN=...      (권장 — 없으면 GitHub 푸시만 건너뜀)
#   YTDLP_PROXY=...       (선택 — 보통 필요 없음)
# =====================================================================================================
ENV_FILE = ".env"

# =====================================================================================================
# [설정 2] ⚙️ 분석 설정 — 필요하면 값만 바꾸세요 (명령줄 옵션 --topic, --folder 등이 있으면 그 값이 우선)
# =====================================================================================================
# ---- 주제 & 저장 위치 ----
TOPIC = "주식"                               # 분석 주제 (다른 주제로 변경 가능)
PROJECT_FOLDER = "stock"                     # 결과 상위 폴더 (PC·GitHub에 없으면 자동 생성)
RESULT_FOLDER = "result"                     # 결과 하위 폴더 → <PROJECT_FOLDER>/<RESULT_FOLDER>/
GITHUB_REPO = "yeomin1024/yeomin1024-ytb"    # 결과를 푸시할 저장소
GITHUB_BRANCH = "main"                       # 푸시할 브랜치 (없으면 생성)
OUTPUT_DIR = "output"                        # PC 결과 저장 위치 (이 스크립트 폴더 기준 상대경로 또는 절대경로)

EXTRA_KEYWORDS = []     # 직접 추가할 검색 키워드. 예: ["미국 주식", "배당주", "ETF 추천"]
EXCLUDE_KEYWORDS = []   # 자동완성에서 제외할 단어(특정 채널명 등). 예: ["주식단테"]

# ---- 수집 범위 ----
REGION_CODE = "KR"              # 검색 지역
LANGUAGE = "ko"                 # 검색/자막 언어
ANALYSIS_DAYS = 365             # 성과 분석 대상: 최근 N일 내 업로드 영상
MAX_SEARCH_KEYWORDS = 20        # YouTube 검색할 키워드 수 (키워드당 검색 1회 = 100유닛 × 정렬 수)
SEARCH_ORDERS = ["relevance", "viewCount"]  # relevance=실제 검색 결과 화면(경쟁), viewCount=기간 내 조회수 상위
RELEVANCE_USE_DATE_FILTER = False  # False: 관련도 검색은 기간 제한 없이 '실제 검색화면' 그대로 수집
PAGES_PER_QUERY = 1             # 검색 1페이지 = 50개
QUOTA_BUDGET = 9000             # 이번 실행에서 쓸 최대 쿼터 (일일 한도 10,000)
AUTOCOMPLETE_EXPAND = True      # 자동완성 확장(ㄱ~ㅎ, 가~하, a~z, 수식어) — 쿼터 0
AUTOCOMPLETE_DEPTH2_N = 15      # 상위 자동완성어를 한 번 더 확장할 개수
REQUIRE_TOPIC_IN_KEYWORD = True # 자동완성어에 주제어가 포함된 것만 사용

# ---- 성과 지표 기준 ----
MATURE_AGE_DAYS = 14            # 업로드 후 N일 이상 지난 영상만 '성과' 분석 (조회수 누적 미완료 편향 방지)
BASELINE_UPLOADS = 50           # 채널 평균 계산에 쓰는 최근 업로드 수 (1페이지=50개=1유닛)
BASELINE_MIN_N = 5              # 채널 기준선 최소 표본
MAX_BASELINE_CHANNELS = 700     # 기준선을 계산할 최대 채널 수 (채널당 약 2유닛)
OUTLIER_MIN = 3.0               # 채널 중앙값 대비 N배 이상 → 아웃라이어(성공)
MIN_SUCCESS_VIEWS = 10_000      # 성공으로 인정할 최소 조회수
SMALL_CHANNEL_MAX_SUBS = 10_000 # 소규모 채널 기준 (구독자 수 미만)
BIG_CHANNEL_MIN_SUBS = 100_000  # 대형 채널 기준
SERP_TOP_N = 20                 # 키워드 경쟁도 계산에 쓰는 검색 상위 N개
FRESH_DAYS = 90                 # '최신 영상' 기준 (검색 상위에 최신 영상이 많으면 신규 진입 여지↑)
SHORTS_HTTP_CHECK = True        # 61~180초 영상의 쇼츠 여부를 youtube.com/shorts/ 로 확인 (쿼터 0)
FETCH_COMMENTS_TOP_N = 30       # 시청자 질문 분석용 댓글 수집 영상 수 (영상당 1유닛)

# ---- 성공사례 (대본 + 영상 파일) ----
SUCCESS_CASE_COUNT = 8          # 저장할 성공사례 영상 수
SUCCESS_SMALL_CHANNEL_SHARE = 0.5   # 성공사례 중 소규모 채널 최소 비율 (0명 채널에 가장 참고가 됨)
SUCCESS_LONGFORM_SHARE = 0.5        # 성공사례 중 롱폼 최소 비율 (대본 분석 가치↑)
MAX_CASES_PER_CHANNEL = 1       # 한 채널에서 최대 몇 개까지 (다양성)
DOWNLOAD_VIDEOS = True          # 영상 파일 다운로드
VIDEO_MAX_HEIGHT = 480          # 다운로드 해상도 상한 (용량 절약)
VIDEO_MAX_MB = 49               # 파일당 최대 용량 — 초과 시 ffmpeg 재인코딩 (GitHub 50MB 경고/100MB 차단)
ALLOW_VIDEO_UPLOAD_TO_PUBLIC_REPO = False  # ⚠️ 공개 저장소에 타인 영상 업로드 허용 여부 (저작권 위험) — False면 영상은 PC에만 저장
USE_WHISPER_FALLBACK = True     # 자막이 없으면 Whisper 음성인식으로 대본 생성 (faster-whisper 자동 설치)
WHISPER_MODEL = "small"         # tiny/base/small/medium/large-v3 (NVIDIA GPU 있으면 medium 권장)
WHISPER_CPU_MAX_MINUTES = 15    # GPU 없이 실행 시 이 길이(분)를 넘는 영상은 Whisper 생략 (GPU면 제한 없음)

# ---- YouTube 봇 확인('Sign in to confirm you're not a bot') 대응 — 가정용 인터넷이면 보통 필요 없음 ----
YTDLP_COOKIES_FILE = ""         # cookies.txt 경로. 비워두면 이 폴더의 cookies*.txt 를 자동으로 사용
COOKIES_FROM_BROWSER = ""       # 또는 브라우저 로그인 쿠키 사용: "firefox" 권장 (크롬은 실행 중이면 실패할 수 있음)
YTDLP_CLIENT_FALLBACK = True    # 봇 확인 시 다른 YouTube 클라이언트(tv_simply → tv → web_embedded → mweb)로 재시도
YTDLP_MAX_BOT_BLOCKS = 2        # 연속 N개 영상이 모두 막히면 이번 실행의 다운로드 중단

# ---- 저장 / 푸시 ----
PUSH_TO_GITHUB = True
CLEAN_OLD_RESULTS = True        # 푸시 전 GitHub의 기존 <PROJECT_FOLDER>/<RESULT_FOLDER> 내용을 교체 (이전 버전은 git 기록에 남음)
OPEN_RESULT_FOLDER = True       # 끝나면 결과 폴더 열기
MAKE_RESULT_ZIP = False         # 결과를 zip 파일로도 저장

# ---- 실행 환경 ----
AUTO_INSTALL_PACKAGES = True    # 필요한 파이썬 패키지 자동 설치 (pip)
UPDATE_YTDLP_DAILY = True       # yt-dlp를 하루 1번 최신으로 업데이트 (YouTube 변경 대응)
CACHE_TTL_HOURS = 24            # API 응답 캐시 유효시간 — 같은 날 재실행 시 쿼터를 거의 쓰지 않음
RANDOM_SEED = 42                # 클러스터링 등 재현성용 시드
LOG_LEVEL = "INFO"              # DEBUG / INFO / WARNING
RUN_SELF_TEST = True            # 시작 시 오프라인 자가진단 (2~3초)


# =====================================================================================================
# 이하 코드는 수정할 필요가 없습니다.
# =====================================================================================================
# VERSION: v2.0.0 — 2026-10-09 — 실행 준비: 콘솔 UTF-8, Python 버전 확인, 패키지 자동 설치, yt-dlp 일일 업데이트 (표준 라이브러리만 사용)
import importlib.util as _ilu
import os as _os
import subprocess as _sp
import sys as _sys
import time as _time
from pathlib import Path as _Path

REQUIRED_PACKAGES = [  # (import 이름, pip 이름)
    ("numpy", "numpy"), ("pandas", "pandas"), ("requests", "requests"), ("matplotlib", "matplotlib"),
    ("sklearn", "scikit-learn"), ("scipy", "scipy"), ("openpyxl", "openpyxl"),
    ("yt_dlp", "yt-dlp[default]"),                         # 영상/자막 다운로드 (yt-dlp-ejs 포함)
    ("youtube_transcript_api", "youtube-transcript-api>=1.2"),
    ("kiwipiepy", "kiwipiepy"),                            # 한국어 형태소 분석
    ("imageio_ffmpeg", "imageio-ffmpeg"),                  # ffmpeg 바이너리 (따로 설치 불필요)
    ("deno", "deno"),                                      # yt-dlp가 YouTube에서 요구하는 JavaScript 런타임
]
OPTIONAL_PACKAGES = [("faster_whisper", "faster-whisper")]   # USE_WHISPER_FALLBACK=True 일 때만


ENV_TEMPLATE = """# YouTube 주제 분석기 — 비밀 키 파일
# ⚠️ 이 파일은 절대 GitHub에 올리거나 공유하지 마세요 (.gitignore에 등록되어 있음)
# '=' 뒤에 값을 붙여넣고 저장하세요. 따옴표는 필요 없습니다.

# [필수] YouTube Data API v3 키
#   https://console.cloud.google.com/ → 프로젝트 만들기 → API 및 서비스 → 라이브러리 → "YouTube Data API v3" 사용
#   → 사용자 인증 정보 → API 키 만들기
YOUTUBE_API_KEY=

# [권장] GitHub 토큰 — 비워두면 결과는 PC에만 저장되고 GitHub 푸시는 건너뜁니다
#   GitHub → Settings → Developer settings → Fine-grained tokens → Generate new token
#   → Repository access: yeomin1024-ytb 선택 → Permissions: Contents = Read and write
GITHUB_TOKEN=

# [선택] 프록시 (보통 필요 없음). 예: http://user:pass@host:port
YTDLP_PROXY=
"""


def _setup_console():
    """Windows 콘솔/리다이렉트에서도 한글·이모지가 깨지거나 오류 나지 않도록 UTF-8로 출력."""
    for stream in (_sys.stdout, _sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass


def _pip_install(pkgs, quiet=False):
    cmd = [_sys.executable, "-m", "pip", "install", "-U", *(["-q"] if quiet else []), *pkgs]
    print(f"[SETUP] {' '.join(cmd[2:])}", flush=True)
    return _sp.run(cmd).returncode == 0


def bootstrap(skip_install=False):
    _setup_console()
    if _sys.version_info < (3, 10):
        print(f"[SETUP] ❌ Python 3.10 이상이 필요합니다 (현재 {_sys.version.split()[0]}) → https://www.python.org/downloads/")
        _sys.exit(1)
    base = _Path(__file__).resolve().parent
    env_path = base / ENV_FILE
    if not env_path.exists():           # 설치(수 분)보다 먼저 만들어 두면 설치되는 동안 키를 입력할 수 있음
        env_path.write_text(ENV_TEMPLATE, "utf-8")
        print(f"[SETUP] 📝 키 파일을 만들었습니다: {env_path}\n"
              f"[SETUP]    메모장 등으로 열어 YOUTUBE_API_KEY(필수), GITHUB_TOKEN(권장)을 입력·저장하세요.", flush=True)
    missing = [pip for mod, pip in REQUIRED_PACKAGES if _ilu.find_spec(mod) is None]
    optional = [pip for mod, pip in OPTIONAL_PACKAGES if USE_WHISPER_FALLBACK and _ilu.find_spec(mod) is None]
    if missing:
        if skip_install or not AUTO_INSTALL_PACKAGES:
            print(f"[SETUP] ❌ 필요한 패키지가 없습니다 → 다음 명령으로 설치 후 다시 실행하세요:\n"
                  f'        python -m pip install -U {" ".join(chr(34) + p + chr(34) for p in missing)}')
            _sys.exit(1)
        print(f"[SETUP] 필요한 패키지 설치 중 (최초 1회, 수 분 소요): {missing}", flush=True)
        if not _pip_install(missing):
            print("[SETUP] ❌ 패키지 설치 실패 → 위 오류 확인. 가상환경(.venv) 사용을 권장합니다:\n"
                  "        python -m venv .venv  →  (Windows) .venv\\Scripts\\activate  /  (Mac) source .venv/bin/activate")
            _sys.exit(1)
    failed_stamp = base / ".yt_work" / "whisper_install_failed.stamp"
    recently_failed = failed_stamp.exists() and _time.time() - failed_stamp.stat().st_mtime < 86400
    if optional and not skip_install and AUTO_INSTALL_PACKAGES and not recently_failed:
        print(f"[SETUP] 선택 패키지 설치 (자막 없는 영상 음성인식용): {optional}", flush=True)
        if not _pip_install(optional):
            failed_stamp.parent.mkdir(parents=True, exist_ok=True)
            failed_stamp.write_text(_time.strftime("%Y-%m-%d %H:%M:%S"), "utf-8")   # 24시간 동안 재시도 안 함
            print("[SETUP] ⚠️ faster-whisper 설치 실패 → 음성인식 없이 진행합니다 (자막이 있는 영상은 영향 없음)")
    # yt-dlp는 YouTube 변경에 맞춰 자주 업데이트됨 → 하루 1번 최신화
    stamp = base / ".yt_work" / "ytdlp_update.stamp"
    if (UPDATE_YTDLP_DAILY and AUTO_INSTALL_PACKAGES and not skip_install and "yt-dlp[default]" not in missing
            and (not stamp.exists() or _time.time() - stamp.stat().st_mtime > 86400)):
        if _pip_install(["yt-dlp[default]"], quiet=True):
            stamp.parent.mkdir(parents=True, exist_ok=True)
            stamp.write_text(_time.strftime("%Y-%m-%d %H:%M:%S"), "utf-8")
    import importlib
    importlib.invalidate_caches()


if __name__ == "__main__":
    bootstrap(skip_install="--skip-install" in _sys.argv)


# =====================================================================================================
# 🧰 [모듈] 공통 유틸 (로깅·캐시·타이머·경로)
# =====================================================================================================
# VERSION: v2.0.0 — 2026-10-09 — 내 PC 실행: 스크립트 폴더 기준 경로·Windows 안전 삭제·cookies.txt 자동 인식 (공통 유틸: 로깅·캐시·타이머)
import os, sys, re, glob, json, time, math, html, stat, base64, random, shutil, hashlib, logging, platform, tempfile, threading, subprocess, unicodedata
import datetime as dt
from pathlib import Path
from collections import Counter, deque
from concurrent.futures import ThreadPoolExecutor
from contextlib import contextmanager
from dataclasses import dataclass, field

import numpy as np
import pandas as pd
import requests

NOTEBOOK_VERSION = "v2.0.0"
KST = dt.timezone(dt.timedelta(hours=9))
UTC = dt.timezone.utc
IS_WINDOWS = os.name == "nt"
try:
    BASE_DIR = Path(__file__).resolve().parent          # 이 스크립트가 있는 폴더 (.env / output / 캐시 기준)
except NameError:                                       # (대화형 실행 등 __file__ 이 없을 때)
    BASE_DIR = Path.cwd()
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/128.0 Safari/537.36")
LOGGER = logging.getLogger("yt_topic_analyzer")


# ----------------------------------------------------------------------------- 로깅
class _SecretMasker(logging.Filter):
    """로그에 API 키/토큰이 절대 찍히지 않도록 마스킹."""
    secrets = set()

    def filter(self, record):
        msg = record.getMessage()
        for s in self.secrets:
            if s and len(s) >= 8:
                msg = msg.replace(s, "***")
        record.msg, record.args = msg, ()
        return True


class _StageFormatter(logging.Formatter):
    """형식: [STAGE] [YYYY-MM-DD HH:MM:SS KST] [LEVEL] message key=value ..."""

    def format(self, record):
        stage = getattr(record, "stage", "GENERAL")
        ts = dt.datetime.now(KST).strftime("%Y-%m-%d %H:%M:%S")
        return f"[{stage}] [{ts}] [{record.levelname}] {record.getMessage()}"


def register_secret(value):
    if value:
        _SecretMasker.secrets.add(value)


def mask_secrets(text):
    for s in _SecretMasker.secrets:
        if s and len(s) >= 8:
            text = text.replace(s, "***")
    return text


def setup_logging(level="INFO", log_file=None):
    for h in LOGGER.handlers[:]:
        h.close()
        LOGGER.removeHandler(h)
    LOGGER.filters.clear()
    LOGGER.setLevel(getattr(logging, str(level).upper(), logging.INFO))
    LOGGER.propagate = False
    LOGGER.addFilter(_SecretMasker())
    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(_StageFormatter())
    LOGGER.addHandler(sh)
    if log_file:
        Path(log_file).parent.mkdir(parents=True, exist_ok=True)
        fh = logging.FileHandler(log_file, encoding="utf-8")
        fh.setFormatter(_StageFormatter())
        LOGGER.addHandler(fh)


def _fmt_val(v):
    if isinstance(v, (float, np.floating)):
        return f"{float(v):.4g}" if np.isfinite(v) else "nan"
    if isinstance(v, (list, tuple, set, pd.Index, np.ndarray)):
        v = list(v)
        body = ",".join(str(x) for x in v[:12]) + (f",…(+{len(v) - 12})" if len(v) > 12 else "")
        return f"[{body}]"
    if isinstance(v, dict):
        return json.dumps(v, ensure_ascii=False, default=str)[:300]
    s = str(v)
    if len(s) > 200:
        s = s[:200] + "…"
    return f'"{s}"' if (" " in s or not s) else s


def log(stage, msg="", level="INFO", **kv):
    lvl = getattr(logging, level.upper(), logging.INFO) if isinstance(level, str) else level
    if not LOGGER.isEnabledFor(lvl):
        return
    kvs = " ".join(f"{k}={_fmt_val(v)}" for k, v in kv.items())
    LOGGER.log(lvl, f"{msg} {kvs}".strip(), extra={"stage": stage})


@contextmanager
def stage_timer(ctx, stage):
    """단계별 시작/종료/소요시간 로깅 + ctx.timings 기록."""
    t0 = time.perf_counter()
    log(stage, "▶ 시작")
    try:
        yield
    except Exception as e:
        ctx.timings[stage] = round(time.perf_counter() - t0, 2)
        log(stage, "✖ 실패", level="ERROR", error=f"{type(e).__name__}: {e}", elapsed_sec=ctx.timings[stage])
        raise
    ctx.timings[stage] = round(time.perf_counter() - t0, 2)
    log(stage, "■ 완료", elapsed_sec=ctx.timings[stage])


# ----------------------------------------------------------------------------- 캐시
class JsonCache:
    """요청 파라미터 해시 → JSON 파일. 재실행 시 YouTube 쿼터/네트워크 절약."""

    def __init__(self, root, ttl_hours=24):
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)
        self.ttl = float(ttl_hours) * 3600
        self.hits, self.misses = Counter(), Counter()
        self._lock = threading.Lock()

    def _path(self, ns, key):
        h = hashlib.sha1(key.encode("utf-8")).hexdigest()
        return self.root / ns / h[:2] / f"{h}.json"

    def get(self, ns, key):
        p = self._path(ns, key)
        if p.exists() and (self.ttl <= 0 or time.time() - p.stat().st_mtime <= self.ttl):
            try:
                val = json.loads(p.read_text("utf-8"))
                with self._lock:
                    self.hits[ns] += 1
                return val
            except (json.JSONDecodeError, OSError):
                pass
        with self._lock:
            self.misses[ns] += 1
        return None

    def set(self, ns, key, value):
        p = self._path(ns, key)
        p.parent.mkdir(parents=True, exist_ok=True)
        tmp = p.with_suffix(f".tmp{threading.get_ident()}")
        try:
            tmp.write_text(json.dumps(value, ensure_ascii=False), "utf-8")
            os.replace(tmp, p)
        except OSError:          # (Windows) 다른 스레드가 같은 파일을 쓰는 중이면 캐시 저장만 생략
            tmp.unlink(missing_ok=True)


# ----------------------------------------------------------------------------- 실행 컨텍스트
@dataclass
class RunContext:
    cfg: dict
    run_id: str
    started_at: dt.datetime            # UTC aware
    work_dir: Path
    out_dir: Path                      # <output_root>/<PROJECT_FOLDER>/<RESULT_FOLDER>
    cache: JsonCache
    output_root: Path = None           # OUTPUT_DIR (기본: <스크립트 폴더>/output)
    yt: object = None
    timings: dict = field(default_factory=dict)
    data: dict = field(default_factory=dict)
    notes: list = field(default_factory=list)  # 리포트에 표시할 경고/한계

    def note(self, stage, msg, level="WARNING", **kv):
        log(stage, msg, level=level, **kv)
        self.notes.append(f"[{stage}] {msg}" + (" " + " ".join(f"{k}={_fmt_val(v)}" for k, v in kv.items()) if kv else ""))


CONFIG_KEYS = [
    "TOPIC", "PROJECT_FOLDER", "RESULT_FOLDER", "GITHUB_REPO", "GITHUB_BRANCH", "EXTRA_KEYWORDS", "EXCLUDE_KEYWORDS",
    "REGION_CODE", "LANGUAGE", "ANALYSIS_DAYS", "MAX_SEARCH_KEYWORDS", "SEARCH_ORDERS", "RELEVANCE_USE_DATE_FILTER",
    "PAGES_PER_QUERY", "QUOTA_BUDGET", "AUTOCOMPLETE_EXPAND", "AUTOCOMPLETE_DEPTH2_N", "REQUIRE_TOPIC_IN_KEYWORD",
    "MATURE_AGE_DAYS", "BASELINE_UPLOADS", "BASELINE_MIN_N", "MAX_BASELINE_CHANNELS", "OUTLIER_MIN", "MIN_SUCCESS_VIEWS",
    "SMALL_CHANNEL_MAX_SUBS", "BIG_CHANNEL_MIN_SUBS", "SERP_TOP_N", "FRESH_DAYS", "SHORTS_HTTP_CHECK",
    "FETCH_COMMENTS_TOP_N", "SUCCESS_CASE_COUNT", "SUCCESS_SMALL_CHANNEL_SHARE", "SUCCESS_LONGFORM_SHARE",
    "MAX_CASES_PER_CHANNEL", "DOWNLOAD_VIDEOS", "VIDEO_MAX_HEIGHT", "VIDEO_MAX_MB", "ALLOW_VIDEO_UPLOAD_TO_PUBLIC_REPO",
    "USE_WHISPER_FALLBACK", "WHISPER_MODEL", "WHISPER_CPU_MAX_MINUTES", "YTDLP_COOKIES_FILE",
    "COOKIES_FROM_BROWSER", "YTDLP_CLIENT_FALLBACK", "YTDLP_MAX_BOT_BLOCKS",
    "PUSH_TO_GITHUB", "CLEAN_OLD_RESULTS", "OUTPUT_DIR", "OPEN_RESULT_FOLDER", "MAKE_RESULT_ZIP",
    "AUTO_INSTALL_PACKAGES", "UPDATE_YTDLP_DAILY", "CACHE_TTL_HOURS", "RANDOM_SEED", "LOG_LEVEL", "RUN_SELF_TEST",
]
# 위험/비용 관련 설정: 기본값과 다르면 WARNING으로 명시적으로 기록
RISK_DEFAULTS = {"QUOTA_BUDGET": 9000, "SUCCESS_CASE_COUNT": 8, "DOWNLOAD_VIDEOS": True, "VIDEO_MAX_MB": 49,
                 "ALLOW_VIDEO_UPLOAD_TO_PUBLIC_REPO": False, "CLEAN_OLD_RESULTS": True, "MAX_BASELINE_CHANNELS": 700}


def collect_config(namespace):
    missing = [k for k in CONFIG_KEYS if k not in namespace]
    if missing:
        raise RuntimeError(f"설정 변수가 없습니다: {missing} → 스크립트 상단 [설정] 영역을 확인하세요.")
    return {k: namespace[k] for k in CONFIG_KEYS}


def sanitize_folder(name, label):
    name = str(name).strip().strip("/").replace("\\", "/")
    parts = [p for p in name.split("/") if p]
    if not parts or any(p in (".", "..") for p in parts) or any(re.search(r'[<>:"|?*\x00-\x1f]', p) for p in parts):
        raise ValueError(f"{label} 폴더명이 올바르지 않습니다: {name!r} (예: 'stock')")
    return "/".join(parts)


def find_ffmpeg():
    """시스템 ffmpeg → imageio-ffmpeg 내장 바이너리 순서로 탐색 (PC에 ffmpeg를 따로 설치하지 않아도 됨)."""
    p = shutil.which("ffmpeg")
    if p:
        return p
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        return None


AUTH_COOKIE_NAMES = {"SID", "__Secure-1PSID", "__Secure-3PSID", "LOGIN_INFO", "SAPISID", "__Secure-3PAPISID"}


def find_cookie_files():
    """이 스크립트 폴더의 cookies*.txt 자동 탐색 (봇 확인 대응용, 선택)."""
    return sorted(str(p) for p in BASE_DIR.glob("*cookie*.txt"))


def inspect_cookies(path):
    """cookies.txt(Netscape 형식) 점검 — 쿠키 '이름'만 확인하고 값은 절대 기록하지 않음."""
    rows = []
    with open(path, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            if line.startswith("#HttpOnly_"):
                line = line[len("#HttpOnly_"):]
            elif line.startswith("#") or not line.strip():
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) >= 7:
                rows.append((parts[0], parts[4], parts[5]))     # domain, expiry, name
    yt = [r for r in rows if r[0].endswith(("youtube.com", "google.com"))]
    now = time.time()
    auth = sorted({n for _, _, n in yt if n in AUTH_COOKIE_NAMES})
    expired = sorted({n for _, e, n in yt if n in AUTH_COOKIE_NAMES and e.isdigit() and 0 < int(e) < now})
    return {"cookie_lines": len(rows), "youtube_google_cookies": len(yt), "auth_cookies": auth, "expired_auth": expired}


def prepare_cookies(cfg, work):
    """쿠키 파일 준비: YTDLP_COOKIES_FILE → 스크립트 폴더의 cookies*.txt 자동 탐색.
    원본 보호를 위해 작업폴더로 복사해서 사용 (yt-dlp가 종료 시 쿠키 파일을 다시 씀)."""
    dst = Path(work) / "cookies.txt"
    src, source = str(cfg.get("YTDLP_COOKIES_FILE") or "").strip(), "file"
    if src and not os.path.isabs(src):
        src = str(BASE_DIR / src)
    if not src:
        found = find_cookie_files()
        if found:
            src, source = found[0], "auto"
    if not src:
        return "", "none"
    if not os.path.exists(src):
        log("AUTH", "YTDLP_COOKIES_FILE 경로가 없음 → 쿠키 없이 진행", level="WARNING", path=src)
        return "", "missing"
    if os.path.abspath(src) != os.path.abspath(dst):
        shutil.copy(src, dst)
    try:
        os.chmod(dst, 0o600)
    except OSError:
        pass
    return str(dst), f"{source}:{Path(src).name}"


def rmtree_force(path):
    """폴더 삭제 (Windows에서 git 읽기전용 파일 때문에 실패하는 문제 대응)."""
    def _fix(func, p, _exc):
        try:
            os.chmod(p, stat.S_IWRITE)
            func(p)
        except Exception:
            pass
    if Path(path).exists():
        if sys.version_info >= (3, 12):
            shutil.rmtree(path, onexc=_fix)
        else:
            shutil.rmtree(path, onerror=_fix)


def close_log_files():
    """Windows는 열린 로그 파일이 있으면 폴더를 지울 수 없으므로 먼저 닫음."""
    for h in LOGGER.handlers[:]:
        if isinstance(h, logging.FileHandler):
            h.close()
            LOGGER.removeHandler(h)


def init_run(cfg, youtube_api_key, github_token):
    cfg = dict(cfg)
    if not youtube_api_key:     # 뒤 단계까지 가지 않고 즉시 멈춤
        raise ValueError("YOUTUBE_API_KEY 없음 → 스크립트 폴더의 .env 파일에 YOUTUBE_API_KEY=... 입력 후 다시 실행")
    if not str(cfg["TOPIC"]).strip():
        raise ValueError("TOPIC이 비어 있습니다.")
    cfg["TOPIC"] = str(cfg["TOPIC"]).strip()
    cfg["PROJECT_FOLDER"] = sanitize_folder(cfg["PROJECT_FOLDER"], "PROJECT_FOLDER")
    cfg["RESULT_FOLDER"] = sanitize_folder(cfg["RESULT_FOLDER"], "RESULT_FOLDER")
    work = BASE_DIR / ".yt_work"                         # 캐시·임시파일·git 작업폴더 (재실행 시 캐시 재사용)
    output_root = Path(cfg["OUTPUT_DIR"]).expanduser()
    if not output_root.is_absolute():
        output_root = BASE_DIR / output_root
    out_dir = output_root / cfg["PROJECT_FOLDER"] / cfg["RESULT_FOLDER"]
    work.mkdir(parents=True, exist_ok=True)
    close_log_files()
    if out_dir.exists():
        rmtree_force(out_dir)           # 결과 폴더는 매 실행 새로 생성 (이전 결과는 GitHub 기록에 남음, 캐시는 유지)
    out_dir.mkdir(parents=True, exist_ok=True)
    setup_logging(cfg["LOG_LEVEL"], out_dir / "run_log.txt")
    register_secret(youtube_api_key)
    register_secret(github_token)
    if github_token:
        register_secret(base64.b64encode(f"x-access-token:{github_token}".encode()).decode())
    random.seed(cfg["RANDOM_SEED"])
    np.random.seed(cfg["RANDOM_SEED"])
    started = dt.datetime.now(UTC)
    run_id = started.astimezone(KST).strftime("%Y%m%d_%H%M%S")
    ctx = RunContext(cfg=cfg, run_id=run_id, started_at=started, work_dir=work, out_dir=out_dir,
                     cache=JsonCache(work / "cache", cfg["CACHE_TTL_HOURS"]), output_root=output_root)
    log("INIT", "실행 시작", version=NOTEBOOK_VERSION, run_id=run_id, os=platform.platform(), out_dir=str(out_dir),
        work_dir=str(work), python=sys.version.split()[0], pandas=pd.__version__, numpy=np.__version__,
        ffmpeg=find_ffmpeg(), git=shutil.which("git"))
    log("INIT", "설정", **{k: v for k, v in cfg.items()})
    for k, default in RISK_DEFAULTS.items():
        if cfg[k] != default:
            ctx.note("INIT", "⚠️ 위험/비용 관련 설정이 기본값과 다릅니다", key=k, default=default, current=cfg[k])
    log("INIT", "재현성 시드 고정", random_seed=cfg["RANDOM_SEED"])
    return ctx


# ----------------------------------------------------------------------------- 공통 유틸
def chunks(seq, n):
    seq = list(seq)
    for i in range(0, len(seq), n):
        yield seq[i:i + n]


def slugify(text, maxlen=40):
    text = unicodedata.normalize("NFKC", str(text))
    text = re.sub(r"[^0-9A-Za-z가-힣]+", "_", text).strip("_")
    return (text[:maxlen].rstrip("_")) or "untitled"


def normalize_kw(s):
    return re.sub(r"\s+", "", unicodedata.normalize("NFKC", str(s)).lower())


def pct_rank(s):
    """0~1 백분위 순위 (NaN 유지). 서로 다른 단위의 지표를 합산할 때 사용."""
    return pd.Series(s, dtype="float64").rank(pct=True, method="average")


def parse_iso_duration(series):
    """ISO8601 기간(PT1H2M3S, P1DT2H) → 초 (벡터화)."""
    s = pd.Series(series, dtype="object").fillna("").astype(str)
    p = s.str.extract(r"^P(?:(?P<d>\d+)D)?(?:T(?:(?P<h>\d+)H)?(?:(?P<m>\d+)M)?(?:(?P<s>\d+(?:\.\d+)?)S)?)?$")
    p = p.apply(pd.to_numeric, errors="coerce")
    sec = p["d"].fillna(0) * 86400 + p["h"].fillna(0) * 3600 + p["m"].fillna(0) * 60 + p["s"].fillna(0)
    valid = s.str.match(r"^P(?=\d|T\d)")
    return sec.where(valid, np.nan)


def fmt_int(x):
    try:
        return "-" if x is None or (isinstance(x, float) and not np.isfinite(x)) else f"{int(round(float(x))):,}"
    except (TypeError, ValueError):
        return "-"


def fmt_num(x, digits=1, suffix=""):
    try:
        x = float(x)
        return "-" if not np.isfinite(x) else f"{x:,.{digits}f}{suffix}"
    except (TypeError, ValueError):
        return "-"


def fmt_pct(x, digits=1):
    return fmt_num(float(x) * 100 if x is not None else np.nan, digits, "%")


def fmt_compact(x):
    try:
        x = float(x)
    except (TypeError, ValueError):
        return "-"
    if not np.isfinite(x):
        return "-"
    for unit, div in (("억", 1e8), ("만", 1e4), ("천", 1e3)):
        if abs(x) >= div:
            v = x / div
            return f"{v:,.0f}{unit}" if abs(v) >= 100 or float(v).is_integer() else f"{v:,.1f}{unit}"
    return f"{x:,.0f}"


def to_jsonable(x):
    """numpy/pandas 타입·NaN·Timestamp → JSON 직렬화 가능한 값."""
    if isinstance(x, str) or x is None:
        return x
    if isinstance(x, dict):
        return {str(k): to_jsonable(v) for k, v in x.items()}
    if isinstance(x, (list, tuple, set, np.ndarray, pd.Index)):
        return [to_jsonable(v) for v in x]
    if isinstance(x, (pd.Timestamp, dt.datetime, dt.date)):
        return None if pd.isna(x) else x.isoformat()
    if isinstance(x, (bool, np.bool_)):
        return bool(x)
    if isinstance(x, (int, np.integer)):
        return int(x)
    if isinstance(x, (float, np.floating)):
        return float(x) if np.isfinite(x) else None
    try:
        if pd.isna(x):
            return None
    except (TypeError, ValueError):
        pass
    return str(x)


def video_url(vid):
    return f"https://www.youtube.com/watch?v={vid}"


def md_escape(s):
    return str(s).replace("|", "\\|").replace("\n", " ").replace("[", "［").replace("]", "］")


def http_get(session, url, stage, retries=3, timeout=20, **kw):
    """외부 HTTP 호출 공통: 재시도 + 명확한 오류 로그 (조용히 실패하지 않음)."""
    last = None
    for attempt in range(1, retries + 1):
        try:
            r = session.get(url, timeout=timeout, **kw)
            if r.status_code == 429 or r.status_code >= 500:
                last = f"HTTP {r.status_code}"
                time.sleep(2 ** attempt)
                continue
            return r
        except requests.RequestException as e:
            last = f"{type(e).__name__}: {e}"
            time.sleep(2 ** attempt)
    log(stage, "HTTP 요청 실패", level="WARNING", url=url[:120], error=last, next_step="네트워크/차단 여부 확인 후 재실행")
    return None


# =====================================================================================================
# 🧰 [모듈] YouTube Data API 클라이언트
# =====================================================================================================
# VERSION: v2.0.0 — 2026-10-09 — 안내 문구 PC(.env) 기준으로 수정 (YouTube Data API 클라이언트 + 쿼터 추적)
class QuotaExceededError(RuntimeError):
    pass


class YouTubeAPIError(RuntimeError):
    def __init__(self, endpoint, status, reason, message, fatal=False):
        self.endpoint, self.status, self.reason, self.fatal = endpoint, status, reason, fatal
        super().__init__(f"{endpoint} HTTP {status} reason={reason} message={message}")


_API_HINTS = {
    "keyInvalid": "YOUTUBE_API_KEY 값이 올바르지 않습니다 → .env 파일의 값을 확인하세요.",
    "API_KEY_INVALID": "YOUTUBE_API_KEY 값이 올바르지 않습니다 → .env 파일의 값을 확인하세요.",
    "badRequest": "요청 형식 오류 또는 잘못된 API 키입니다 → 키/설정값 확인.",
    "accessNotConfigured": "Google Cloud Console에서 'YouTube Data API v3'를 사용 설정하세요.",
    "SERVICE_DISABLED": "Google Cloud Console에서 'YouTube Data API v3'를 사용 설정하세요.",
    "API_KEY_SERVICE_BLOCKED": "API 키 제한 설정에서 YouTube Data API v3 허용 여부를 확인하세요.",
    "ipRefererBlocked": "API 키의 IP/리퍼러 제한을 해제하거나 내 PC의 공인 IP를 허용하세요.",
    "forbidden": "접근 권한이 없습니다 (비공개 영상/채널 등).",
    "quotaExceeded": "일일 쿼터 소진 → 한국시간 오후 4~5시(태평양 자정) 리셋 후 재실행. 캐시 덕분에 이미 받은 데이터는 다시 쿼터를 쓰지 않습니다.",
}
_FATAL_REASONS = {"keyInvalid", "API_KEY_INVALID", "accessNotConfigured", "SERVICE_DISABLED", "API_KEY_SERVICE_BLOCKED", "ipRefererBlocked"}
_QUOTA_REASONS = {"quotaExceeded", "dailyLimitExceeded"}
_RETRY_REASONS = {"rateLimitExceeded", "userRateLimitExceeded", "backendError", "internalError"}


class YouTubeClient:
    BASE_URL = "https://www.googleapis.com/youtube/v3/"
    COST = {"search": 100, "videos": 1, "channels": 1, "playlistItems": 1, "commentThreads": 1}

    def __init__(self, api_key, cache, budget):
        if not api_key:
            raise ValueError("YOUTUBE_API_KEY가 없습니다 → .env 파일에 YOUTUBE_API_KEY=... 입력 후 다시 실행")
        self.api_key, self.cache, self.budget = api_key, cache, int(budget)
        self.used = 0
        self.calls, self.cache_hits, self.errors = Counter(), Counter(), Counter()
        self._lock = threading.Lock()
        self._local = threading.local()
        register_secret(api_key)

    # -- 내부 ------------------------------------------------------------------
    def _session(self):
        if not hasattr(self._local, "s"):
            self._local.s = requests.Session()
        return self._local.s

    def remaining(self):
        return self.budget - self.used

    def can_afford(self, endpoint, n=1):
        return self.used + self.COST[endpoint] * n <= self.budget

    def _reserve(self, cost):
        with self._lock:
            if self.used + cost > self.budget:
                raise QuotaExceededError(f"쿼터 예산 초과 예정: used={self.used} cost={cost} budget={self.budget}")
            self.used += cost

    def _refund(self, cost):
        with self._lock:
            self.used -= cost

    @staticmethod
    def _parse_error(r):
        try:
            err = r.json().get("error", {})
            errs = err.get("errors") or [{}]
            reason = errs[0].get("reason") or err.get("status") or "unknown"
            for d in err.get("details", []) or []:     # 신형 오류 포맷 (SERVICE_DISABLED 등)
                if d.get("reason"):
                    reason = d["reason"]
            return reason, err.get("message", "")[:300]
        except ValueError:
            return "unparsable", r.text[:300]

    def _request(self, endpoint, params, use_cache=True):
        cache_key = endpoint + "?" + json.dumps(params, sort_keys=True, ensure_ascii=False)
        if use_cache:
            hit = self.cache.get("yt_api", cache_key)
            if hit is not None:
                with self._lock:
                    self.cache_hits[endpoint] += 1
                return hit
        cost = self.COST.get(endpoint, 1)
        last = None
        for attempt in range(1, 5):
            self._reserve(cost)   # 오류 응답도 쿼터를 소모하므로 응답을 받으면 비용 확정
            try:
                r = self._session().get(self.BASE_URL + endpoint, params={**params, "key": self.api_key}, timeout=30)
            except requests.RequestException as e:
                self._refund(cost)
                last = f"{type(e).__name__}"
                log("API", "네트워크 오류 → 재시도", level="WARNING", endpoint=endpoint, attempt=attempt, error=last)
                time.sleep(2 ** attempt)
                continue
            with self._lock:
                self.calls[endpoint] += 1
            if r.status_code == 200:
                data = r.json()
                if use_cache:
                    self.cache.set("yt_api", cache_key, data)
                return data
            reason, message = self._parse_error(r)
            with self._lock:
                self.errors[f"{endpoint}:{r.status_code}:{reason}"] += 1
            if reason in _QUOTA_REASONS:
                log("API", "❌ YouTube 일일 쿼터 소진", level="ERROR", endpoint=endpoint, hint=_API_HINTS["quotaExceeded"])
                raise QuotaExceededError(message)
            if reason in _RETRY_REASONS or r.status_code >= 500:
                last = f"{r.status_code}:{reason}"
                log("API", "일시 오류 → 재시도", level="WARNING", endpoint=endpoint, attempt=attempt, reason=reason)
                time.sleep(2 ** attempt)
                continue
            fatal = reason in _FATAL_REASONS or (r.status_code == 400 and "API key" in message)
            if fatal:
                log("API", "❌ 치명적 API 오류", level="ERROR", endpoint=endpoint, status=r.status_code, reason=reason,
                    message=message, hint=_API_HINTS.get(reason, _API_HINTS["badRequest"]))
            raise YouTubeAPIError(endpoint, r.status_code, reason, message, fatal=fatal)
        raise YouTubeAPIError(endpoint, -1, "retries_exhausted", str(last))

    # -- 엔드포인트 ----------------------------------------------------------------
    def search(self, q, order, published_after=None, max_pages=1, region=None, lang=None):
        items, total, token = [], None, None
        for _ in range(max_pages):
            params = {"part": "snippet", "q": q, "type": "video", "order": order, "maxResults": 50,
                      "regionCode": region, "relevanceLanguage": lang, "publishedAfter": published_after,
                      "pageToken": token}
            params = {k: v for k, v in params.items() if v}
            data = self._request("search", params)
            total = data.get("pageInfo", {}).get("totalResults", total)
            for it in data.get("items", []):
                vid = (it.get("id") or {}).get("videoId")
                if vid:
                    items.append({"video_id": vid, "channel_id": it.get("snippet", {}).get("channelId")})
            token = data.get("nextPageToken")
            if not token:
                break
        return items, total

    def _batched(self, endpoint, part, ids):
        """50개씩 묶어 병렬 요청 (1묶음 = 1유닛). 순서는 의미 없음."""
        groups = list(chunks(sorted(set(ids)), 50))

        def one(chunk):
            return self._request(endpoint, {"part": part, "id": ",".join(chunk), "maxResults": 50}).get("items", [])
        if len(groups) <= 2:
            return [it for g in groups for it in one(g)]
        with ThreadPoolExecutor(max_workers=8) as ex:
            return [it for res in ex.map(one, groups) for it in res]

    def videos(self, ids):
        return self._batched("videos", "snippet,contentDetails,statistics,liveStreamingDetails", ids)

    def channels(self, ids):
        return self._batched("channels", "snippet,statistics,contentDetails", ids)

    def playlist_video_ids(self, playlist_id, max_items=50):
        ids, token = [], None
        while len(ids) < max_items:
            params = {"part": "contentDetails", "playlistId": playlist_id, "maxResults": min(50, max_items - len(ids))}
            if token:
                params["pageToken"] = token
            data = self._request("playlistItems", params)
            ids += [it["contentDetails"]["videoId"] for it in data.get("items", []) if it.get("contentDetails")]
            token = data.get("nextPageToken")
            if not token:
                break
        return ids[:max_items]

    def comment_threads(self, video_id, max_results=100, order="relevance"):
        data = self._request("commentThreads", {"part": "snippet", "videoId": video_id, "maxResults": max_results,
                                                "order": order, "textFormat": "plainText"})
        rows = []
        for it in data.get("items", []):
            top = it.get("snippet", {}).get("topLevelComment", {}).get("snippet", {})
            rows.append({"video_id": video_id, "comment": top.get("textDisplay", ""), "likes": top.get("likeCount", 0),
                         "published_at": top.get("publishedAt"), "replies": it.get("snippet", {}).get("totalReplyCount", 0)})
        return rows

    def summary(self):
        return {"quota_used": self.used, "quota_budget": self.budget, "calls": dict(self.calls),
                "cache_hits": dict(self.cache_hits), "errors": dict(self.errors)}


def flatten_video(item):
    sn, st = item.get("snippet", {}), item.get("statistics", {})
    cd, ls = item.get("contentDetails", {}), item.get("liveStreamingDetails") or {}
    th = sn.get("thumbnails", {})
    thumb = next((th[k]["url"] for k in ("maxres", "standard", "high", "medium", "default") if k in th), None)
    return {
        "video_id": item.get("id"), "title": sn.get("title", ""), "description": sn.get("description", ""),
        "channel_id": sn.get("channelId"), "channel_title": sn.get("channelTitle", ""),
        "published_at": sn.get("publishedAt"), "tags": sn.get("tags") or [], "category_id": sn.get("categoryId"),
        "default_audio_language": sn.get("defaultAudioLanguage"),
        "live_broadcast_content": sn.get("liveBroadcastContent", "none"), "duration_iso": cd.get("duration"),
        "definition": cd.get("definition"), "has_caption": cd.get("caption") == "true",
        "views": st.get("viewCount"), "likes": st.get("likeCount"), "comments": st.get("commentCount"),
        "was_live": bool(ls.get("actualStartTime")), "thumbnail_url": thumb,
    }


def flatten_channel(item):
    sn, st, cd = item.get("snippet", {}), item.get("statistics", {}), item.get("contentDetails", {})
    hidden = bool(st.get("hiddenSubscriberCount"))
    return {
        "channel_id": item.get("id"), "channel_title_ch": sn.get("title", ""), "channel_handle": sn.get("customUrl"),
        "channel_published_at": sn.get("publishedAt"), "channel_country": sn.get("country"),
        "subscribers": None if hidden else st.get("subscriberCount"), "subs_hidden": hidden,
        "channel_views": st.get("viewCount"), "channel_video_count": st.get("videoCount"),
        "uploads_playlist": (cd.get("relatedPlaylists") or {}).get("uploads"),
    }


# =====================================================================================================
# 🧰 [모듈] Stage 1 — 키워드 발굴
# =====================================================================================================
# VERSION: v2.0.0 — 2026-10-09 — 로직 변경 없음(v1.0.0 유지) (라이브러리 3/10: Stage 1 키워드 발굴 — YouTube 자동완성, 쿼터 0)
HANGUL_CHOSEONG = list("ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎ")
HANGUL_SYLLABLES = list("가나다라마바사아자차카타파하")
ALPHABET = list("abcdefghijklmnopqrstuvwxyz")
# 주제와 무관하게 '검색 의도'를 넓혀주는 범용 수식어 (주제에 맞게 자유롭게 수정 가능)
KEYWORD_MODIFIERS = ["추천", "초보", "방법", "하는법", "전망", "공부", "이유", "후기", "꿀팁", "총정리", "기초", "입문",
                     "비교", "순위", "실수", "수익", "현실", "장단점", "주의", "뉴스", "분석", "쇼츠", "{year}"]
KEYWORD_PREFIXES = ["초보", "요즘", "{year}", "직장인", "20대", "30대", "40대", "50대", "왜", "어떻게", "무조건"]


def parse_autocomplete(text):
    """client=firefox → 순수 JSON, client=youtube → JSONP. 둘 다 처리."""
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        m = re.search(r"\((\[.*\])\)\s*;?\s*$", text, re.S)
        if not m:
            return []
        data = json.loads(m.group(1))
    if not isinstance(data, list) or len(data) < 2 or not isinstance(data[1], list):
        return []
    out = [(s[0] if isinstance(s, list) and s else s) for s in data[1]]
    return [x.strip() for x in out if isinstance(x, str) and x.strip()]


def fetch_autocomplete(query, hl, gl, cache, session):
    key = f"{hl}|{gl}|{query}"
    hit = cache.get("autocomplete", key)
    if hit is not None:
        return hit
    r = http_get(session, "https://suggestqueries.google.com/complete/search", "KEYWORD",
                 params={"client": "firefox", "ds": "yt", "hl": hl, "gl": gl, "q": query},
                 headers={"User-Agent": UA}, timeout=10)
    if r is None or r.status_code != 200:
        raise RuntimeError(f"autocomplete 실패 query={query} status={getattr(r, 'status_code', None)}")
    try:
        text = r.content.decode("utf-8")
    except UnicodeDecodeError:
        text = r.content.decode("cp949", errors="replace")
    sugg = parse_autocomplete(text)
    cache.set("autocomplete", key, sugg)
    return sugg


def _bigram_jaccard(a, b):
    A = {a[i:i + 2] for i in range(len(a) - 1)} or {a}
    B = {b[i:i + 2] for i in range(len(b) - 1)} or {b}
    return len(A & B) / len(A | B)


def stage1_keyword_discovery(ctx):
    cfg = ctx.cfg
    topic, year = cfg["TOPIC"], str(ctx.started_at.astimezone(KST).year)
    hl, gl = cfg["LANGUAGE"], cfg["REGION_CODE"].lower()
    queries = [topic]
    if cfg["AUTOCOMPLETE_EXPAND"]:
        queries += [f"{topic} {c}" for c in HANGUL_CHOSEONG + HANGUL_SYLLABLES + ALPHABET]
        queries += [f"{topic} {m.format(year=year)}" for m in KEYWORD_MODIFIERS]
        queries += [f"{p.format(year=year)} {topic}" for p in KEYWORD_PREFIXES]
    queries = list(dict.fromkeys(queries))
    log("KEYWORD", "자동완성 수집 시작", seed=topic, n_queries=len(queries), hl=hl, gl=gl)

    session = requests.Session()
    rows, failed = [], []

    def _run(qs, depth):
        def task(q):
            try:
                return q, fetch_autocomplete(q, hl, gl, ctx.cache, session), None
            except Exception as e:  # 개별 실패는 기록 후 계속
                return q, [], repr(e)
        with ThreadPoolExecutor(max_workers=6) as ex:
            for q, sugg, err in ex.map(task, qs):
                if err:
                    failed.append(q)
                for rank, s in enumerate(sugg):
                    rows.append({"query": q, "depth": depth, "suggestion": s, "rank": rank})

    _run(queries, 1)
    # depth-2: 1차 상위 자동완성어를 다시 확장 → 롱테일 검색어
    if cfg["AUTOCOMPLETE_DEPTH2_N"] > 0 and rows:
        tmp = pd.DataFrame(rows)
        tmp["w"] = 1.0 / (1 + tmp["rank"])
        top = tmp.groupby("suggestion")["w"].sum().sort_values(ascending=False).index
        depth2 = [s for s in top if s not in queries][: cfg["AUTOCOMPLETE_DEPTH2_N"]]
        _run(depth2, 2)
    if failed:
        ctx.note("KEYWORD", "일부 자동완성 요청 실패 (나머지로 계속 진행)", n_failed=len(failed), examples=failed[:5])
    if not rows:
        ctx.note("KEYWORD", "자동완성 결과가 없습니다 → 주제어 + EXTRA_KEYWORDS만으로 검색합니다", level="ERROR")
        raw = pd.DataFrame(columns=["query", "depth", "suggestion", "rank"])
    else:
        raw = pd.DataFrame(rows)

    # 집계: 순위가 높을수록, 여러 질의에서 반복 등장할수록 수요가 큰 검색어로 간주
    raw["norm"] = raw["suggestion"].map(normalize_kw)
    raw["w"] = np.where(raw["depth"] == 1, 1.0, 0.5) / (1 + raw["rank"])
    t_norm = normalize_kw(topic)
    if raw.empty:
        agg = pd.DataFrame(columns=["norm", "keyword", "ac_score", "ac_hits", "best_rank", "contains_topic"])
    else:
        agg = (raw.groupby("norm")
                  .agg(keyword=("suggestion", lambda s: s.value_counts().index[0]), ac_score=("w", "sum"),
                       ac_hits=("query", "nunique"), best_rank=("rank", "min"))
                  .reset_index())
        agg["contains_topic"] = agg["norm"].str.contains(re.escape(t_norm), regex=True)
    n_before = len(agg)
    if cfg["REQUIRE_TOPIC_IN_KEYWORD"]:
        agg = agg[agg["contains_topic"]]
    excl = [normalize_kw(x) for x in cfg["EXCLUDE_KEYWORDS"] if str(x).strip()]
    if excl:
        agg = agg[~agg["norm"].apply(lambda n: any(e in n for e in excl))]
    agg = agg.sort_values("ac_score", ascending=False).reset_index(drop=True)
    agg["ac_rank"] = np.arange(1, len(agg) + 1)
    log("KEYWORD", "자동완성 집계", raw_rows=len(raw), unique_suggestions=n_before, after_filter=len(agg),
        require_topic=cfg["REQUIRE_TOPIC_IN_KEYWORD"], excluded=excl)
    for _, r in agg.head(20).iterrows():
        log("KEYWORD", "상위 검색어", level="DEBUG", rank=int(r.ac_rank), keyword=r.keyword, ac_score=r.ac_score, hits=int(r.ac_hits))
    log("KEYWORD", "상위 자동완성 Top10", top10=list(agg["keyword"].head(10)))

    # 검색 키워드 선정: 주제어 → 직접 추가 키워드 → 자동완성 상위 (유사 중복 제거)
    selected, sel_norm = [], []

    def _add(kw, force=False):
        n = normalize_kw(kw)
        if not n or n in sel_norm:
            return
        if not force and any(_bigram_jaccard(n, s) >= 0.8 for s in sel_norm):
            return
        selected.append(kw.strip())
        sel_norm.append(n)

    _add(topic, force=True)
    for kw in cfg["EXTRA_KEYWORDS"]:
        _add(kw, force=True)
    for kw in agg["keyword"]:
        if len(selected) >= cfg["MAX_SEARCH_KEYWORDS"]:
            break
        _add(kw)
    log("KEYWORD", "검색 키워드 선정", n=len(selected), keywords=selected)
    ctx.data["autocomplete_raw"] = raw.drop(columns=["w"])
    ctx.data["keywords_ac"] = agg
    ctx.data["search_keywords"] = selected
    return selected


# =====================================================================================================
# 🧰 [모듈] Stage 2 — 데이터 수집
# =====================================================================================================
# VERSION: v2.0.0 — 2026-10-09 — 로직 변경 없음(v1.0.0 유지) (라이브러리 4/10: Stage 2 데이터 수집 — 검색·영상·채널·채널 기준선)
def plan_quota(ctx, keywords):
    """검색 전에 예상 쿼터를 계산하고, 예산 초과 시 키워드 수를 줄인다 (변경 전/후를 로그로 남김)."""
    cfg, yt = ctx.cfg, ctx.yt
    per_kw = len(cfg["SEARCH_ORDERS"]) * cfg["PAGES_PER_QUERY"] * YouTubeClient.COST["search"]
    est_videos = int(len(keywords) * len(cfg["SEARCH_ORDERS"]) * cfg["PAGES_PER_QUERY"] * 50 * 0.7)
    est_channels = min(cfg["MAX_BASELINE_CHANNELS"], int(est_videos * 0.5))
    reserve = (math.ceil(est_videos / 50) + math.ceil(est_channels / 50)          # videos + channels
               + 2 * est_channels + cfg["FETCH_COMMENTS_TOP_N"] + 30)               # 기준선(채널당 ~2) + 댓글 + 여유
    planned = per_kw * len(keywords) + reserve
    log("COLLECT", "쿼터 계획", keywords=len(keywords), search_cost=per_kw * len(keywords), reserve=reserve,
        planned_total=planned, budget=yt.budget, already_used=yt.used)
    if planned > yt.remaining():
        max_kw = max(1, int((yt.remaining() - reserve) // per_kw))
        if max_kw < len(keywords):
            ctx.note("COLLECT", "쿼터 예산 부족 → 검색 키워드 수 축소", before=len(keywords), after=max_kw,
                     budget=yt.budget, hint="QUOTA_BUDGET을 늘리거나 MAX_SEARCH_KEYWORDS를 줄이세요")
            keywords = keywords[:max_kw]
    return keywords


def collect_search(ctx, keywords):
    cfg, yt = ctx.cfg, ctx.yt
    day0 = ctx.started_at.replace(hour=0, minute=0, second=0, microsecond=0)  # 날짜 단위로 고정 → 같은 날 재실행 시 캐시 적중
    window_start = (day0 - dt.timedelta(days=cfg["ANALYSIS_DAYS"])).strftime("%Y-%m-%dT%H:%M:%SZ")
    rows, stop = [], False
    for i, kw in enumerate(keywords, 1):
        counts = {}
        for order in cfg["SEARCH_ORDERS"]:
            pa = None if (order == "relevance" and not cfg["RELEVANCE_USE_DATE_FILTER"]) else window_start
            try:
                items, total = yt.search(kw, order, pa, cfg["PAGES_PER_QUERY"], cfg["REGION_CODE"], cfg["LANGUAGE"])
            except QuotaExceededError as e:
                ctx.note("COLLECT", "쿼터 소진/예산 도달 → 검색 중단 (수집된 데이터로 계속)", keyword=kw, error=str(e)[:150])
                stop = True
                break
            except YouTubeAPIError as e:
                if e.fatal:
                    raise
                log("COLLECT", "검색 실패 (건너뜀)", level="WARNING", keyword=kw, order=order, error=str(e)[:200])
                continue
            counts[order] = len(items)
            for rank, it in enumerate(items, 1):
                rows.append({"keyword": kw, "order": order, "rank": rank, "video_id": it["video_id"],
                             "channel_id": it["channel_id"], "total_results": total, "published_after": pa})
        log("COLLECT", f"검색 {i}/{len(keywords)}", keyword=kw, results=counts, quota_used=yt.used)
        if stop:
            break
    search_df = pd.DataFrame(rows, columns=["keyword", "order", "rank", "video_id", "channel_id", "total_results", "published_after"])
    if search_df.empty:
        raise RuntimeError("검색 결과가 0건입니다 → API 키/쿼터/키워드를 확인하세요.")
    log("COLLECT", "검색 결과 요약", rows=len(search_df), unique_videos=search_df.video_id.nunique(),
        unique_channels=search_df.channel_id.nunique(), dup_ratio=1 - search_df.video_id.nunique() / len(search_df),
        window_start=window_start)
    return search_df


def collect_channel_baselines(ctx, channels, videos_raw):
    """채널별 최근 업로드 N개의 조회수 → 아웃라이어 배수의 분모(채널 기준선)."""
    cfg, yt = ctx.cfg, ctx.yt
    stats = videos_raw.assign(v=pd.to_numeric(videos_raw["views"], errors="coerce")).groupby("channel_id")["v"].agg(["size", "max"])
    ch = channels.join(stats, on="channel_id").sort_values(["size", "max"], ascending=False)
    cap = min(len(ch), cfg["MAX_BASELINE_CHANNELS"])
    affordable = max(0, (yt.remaining() - cfg["FETCH_COMMENTS_TOP_N"] - 10) // 2)
    if affordable < cap:
        ctx.note("COLLECT", "쿼터 부족 → 기준선 계산 채널 수 축소", before=cap, after=affordable)
        cap = int(affordable)
    if cap < len(ch):
        log("COLLECT", "기준선 대상 채널 제한", total_channels=len(ch), used=cap, rule="데이터셋 내 영상 수·최대 조회수 순")
    ch = ch.head(cap)
    pl = ch["uploads_playlist"].fillna(ch["channel_id"].str.replace(r"^UC", "UU", regex=True))
    pairs, failed = [], Counter()

    def task(args):
        cid, pid = args
        try:
            return cid, yt.playlist_video_ids(pid, cfg["BASELINE_UPLOADS"]), None
        except QuotaExceededError:
            return cid, [], "quota"
        except YouTubeAPIError as e:
            return cid, [], e.reason
    with ThreadPoolExecutor(max_workers=8) as ex:
        for cid, ids, err in ex.map(task, zip(ch["channel_id"], pl)):
            if err:
                failed[err] += 1
            pairs += [(cid, v) for v in ids]
    if failed:
        log("COLLECT", "일부 채널 업로드 목록 실패", level="WARNING", failures=dict(failed))
    base = pd.DataFrame(pairs, columns=["channel_id", "video_id"]).drop_duplicates()
    known = set(videos_raw["video_id"])
    need = [v for v in base["video_id"].unique() if v not in known]   # 이미 받은 영상은 재요청하지 않음
    extra = []
    try:
        extra = [flatten_video(x) for x in yt.videos(need)] if need else []
    except QuotaExceededError as e:
        ctx.note("COLLECT", "쿼터 소진 → 일부 기준선 영상 상세 누락", error=str(e)[:150])
    cols = ["video_id", "views", "published_at", "duration_iso", "was_live", "live_broadcast_content"]
    detail = pd.concat([videos_raw[cols], pd.DataFrame(extra, columns=list(flatten_video({}).keys()))[cols]], ignore_index=True)
    detail = detail.drop_duplicates("video_id")
    base = base.merge(detail, on="video_id", how="inner")
    log("COLLECT", "채널 기준선 수집", channels=ch.shape[0], baseline_videos=len(base), fetched_new=len(extra), quota_used=yt.used)
    return base


def stage2_collect(ctx, keywords):
    yt = ctx.yt
    keywords = plan_quota(ctx, keywords)
    search_df = collect_search(ctx, keywords)

    vids = search_df["video_id"].unique()
    videos_raw = pd.DataFrame([flatten_video(x) for x in yt.videos(vids)])
    missing = set(vids) - set(videos_raw.get("video_id", []))
    log("COLLECT", "영상 상세 수집", requested=len(vids), received=len(videos_raw), missing=len(missing),
        note="missing=삭제/비공개 영상", quota_used=yt.used)
    if videos_raw.empty:
        raise RuntimeError("영상 상세 정보가 0건입니다.")

    channels = pd.DataFrame([flatten_channel(x) for x in yt.channels(videos_raw["channel_id"].dropna().unique())])
    log("COLLECT", "채널 상세 수집", channels=len(channels), hidden_subs=int(channels["subs_hidden"].sum()), quota_used=yt.used)

    baseline = collect_channel_baselines(ctx, channels, videos_raw)
    ctx.data.update(search_df=search_df, videos_raw=videos_raw, channels_raw=channels, baseline_raw=baseline,
                    collected_at=dt.datetime.now(UTC))
    log("COLLECT", "API 사용 요약", **yt.summary())
    return search_df, videos_raw, channels, baseline


# =====================================================================================================
# 🧰 [모듈] Stage 3 — 검증·피처·아웃라이어
# =====================================================================================================
# VERSION: v2.0.0 — 2026-10-09 — 로직 변경 없음(v1.0.0 유지) (라이브러리 5/10: Stage 3 데이터 검증 + 피처 + 아웃라이어 배수)
# 제목 후킹 단어 그룹 (주제와 무관한 범용 표현 — 필요하면 수정/추가)
HOOK_WORD_GROUPS = {
    "hook_urgency":   ["지금", "당장", "긴급", "속보", "오늘", "마지막", "곧", "서둘"],
    "hook_fear":      ["폭락", "하락", "위기", "경고", "손실", "조심", "주의", "절대", "위험", "붕괴", "최악", "망하", "실수"],
    "hook_greed":     ["급등", "상승", "수익", "대박", "부자", "기회", "폭등", "떡상", "벌었", "돈 버는", "월급"],
    "hook_curiosity": ["이유", "비밀", "진짜", "사실", "정체", "결국", "몰랐", "아무도", "숨겨진", "충격", "반전"],
    "hook_beginner":  ["초보", "기초", "방법", "하는법", "하는 법", "정리", "가이드", "입문", "쉽게", "공부", "처음"],
    "hook_list":      ["TOP", "Top", "top", "순위", "BEST", "베스트", "추천", "랭킹"],
    "hook_story":     ["후기", "인증", "경험", "브이로그", "vlog", "VLOG", "실전", "직접", "솔직"],
}
TITLE_FEATURE_REGEX = {
    "has_number":       r"\d",
    "has_question":     r"[?？]",
    "has_exclaim":      r"[!！]",
    "has_bracket":      r"[\[\]【】「」『』〈〉<>()]",
    "has_year":         r"20[2-3]\d",
    "has_money_or_pct": r"\d\s*(?:%|퍼센트|원|만원|억|조|배|달러|\$)|%",
    "has_ellipsis":     r"…|\.\.\.",
    "has_quote":        r"[\"'“”‘’]",
    "has_hashtag":      r"#",
    "has_caps_word":    r"\b[A-Z]{2,}\b",
    "has_emoji":        r"[\U0001F300-\U0001FAFF☀-➿]",
}
FEATURE_LABELS = {
    "has_number": "숫자 포함", "has_question": "물음표(질문형)", "has_exclaim": "느낌표", "has_bracket": "괄호/대괄호",
    "has_year": "연도 표기", "has_money_or_pct": "금액·% 표기", "has_ellipsis": "말줄임(…)", "has_quote": "따옴표(인용)",
    "has_hashtag": "해시태그", "has_caps_word": "영문 대문자 단어", "has_emoji": "이모지",
    "hook_urgency": "긴급성(지금·당장·속보)", "hook_fear": "공포/경고(폭락·위기·절대)", "hook_greed": "수익/욕망(급등·수익·부자)",
    "hook_curiosity": "호기심(이유·진짜·결국)", "hook_beginner": "초보/방법(초보·기초·정리)", "hook_list": "리스트/순위(TOP·순위·추천)",
    "hook_story": "경험담(후기·실전·직접)",
}
CHANNEL_SIZE_BINS = [-1, 999, 9_999, 99_999, 999_999, np.inf]
CHANNEL_SIZE_LABELS = ["1천 미만", "1천~1만", "1만~10만", "10만~100만", "100만+"]
DURATION_BINS = [0, 60, 180, 300, 480, 720, 1200, 1800, 3600, np.inf]
DURATION_LABELS = ["~1분", "1~3분", "3~5분", "5~8분", "8~12분", "12~20분", "20~30분", "30~60분", "60분+"]
HOUR_BINS = [-1, 5, 8, 11, 14, 17, 20, 23]
HOUR_LABELS = ["00~05시", "06~08시", "09~11시", "12~14시", "15~17시", "18~20시", "21~23시"]
WEEKDAY_LABELS = ["월", "화", "수", "목", "금", "토", "일"]


def check_is_short(video_id, session):
    """youtube.com/shorts/<id>: 쇼츠면 200, 아니면 /watch 로 리다이렉트."""
    try:
        r = session.head(f"https://www.youtube.com/shorts/{video_id}", allow_redirects=False, timeout=10,
                         headers={"User-Agent": UA})
    except requests.RequestException:
        return None
    if r.status_code == 200:
        return True
    if r.status_code in (301, 302, 303, 307, 308):
        loc = r.headers.get("Location", "")
        return False if "/watch" in loc else None   # consent 페이지 등은 판단 보류
    return None


def classify_format(df, ctx):
    """format: shorts / long / live. 61~180초는 HTTP 확인(가능 시) → 실패 시 #shorts 표기로 판단."""
    cfg = ctx.cfg
    dur = df["duration_sec"]
    fmt = pd.Series("long", index=df.index, dtype="object")
    fmt[dur <= 60] = "shorts"
    ambiguous = (dur > 60) & (dur <= 180) & ~df["was_live"]
    text = (df["title"].fillna("") + " " + df["description"].fillna("").str[:500] + " " +
            df["tags"].map(lambda t: " ".join(t) if isinstance(t, list) else ""))
    has_tag = text.str.contains(r"#?shorts?\b", case=False, regex=True)
    method = Counter({"duration<=60": int((dur <= 60).sum())})
    checked = {}
    if cfg["SHORTS_HTTP_CHECK"] and ambiguous.any():
        ids = df.loc[ambiguous, "video_id"].tolist()
        cached = {v: ctx.cache.get("is_short", v) for v in ids}
        todo = [v for v, c in cached.items() if c is None]
        sess = requests.Session()
        with ThreadPoolExecutor(max_workers=8) as ex:
            for v, res in zip(todo, ex.map(lambda v: check_is_short(v, sess), todo)):
                if res is not None:
                    ctx.cache.set("is_short", v, {"short": res})
                    cached[v] = {"short": res}
        checked = {v: c["short"] for v, c in cached.items() if c is not None}
    for idx in df.index[ambiguous]:
        vid = df.at[idx, "video_id"]
        if vid in checked:
            fmt[idx] = "shorts" if checked[vid] else "long"
            method["http_check"] += 1
        else:
            fmt[idx] = "shorts" if has_tag[idx] else "long"
            method["hashtag_heuristic"] += 1
    fmt[df["was_live"]] = "live"
    log("FEATURE", "포맷 분류", method=dict(method), counts=fmt.value_counts().to_dict())
    return fmt


def validate_videos(df, ctx, stage="VALIDATE"):
    """입력 데이터 검증: 중복·결측·범위 이상·미래 날짜 등 → 로그 + valid_perf 플래그."""
    n0 = len(df)
    dups = int(df["video_id"].duplicated().sum())
    df = df.drop_duplicates("video_id").copy()
    checks = {
        "duplicated_video_id": dups,
        "views_missing": int(df["views"].isna().sum()),
        "views_negative": int((df["views"] < 0).sum()),
        "likes_gt_views": int((df["likes"] > df["views"]).sum()),
        "published_missing": int(df["published_at"].isna().sum()),
        "published_in_future": int((df["age_days"] < 0).sum()),
        "live_or_upcoming": int(df["live_broadcast_content"].isin(["live", "upcoming"]).sum()),
        "duration_missing_or_zero": int((df["duration_sec"].isna() | (df["duration_sec"] <= 0)).sum()),
        "channel_info_missing": int(df["subscribers"].isna().sum() - df["subs_hidden"].fillna(False).astype(bool).sum()),
        "subscribers_hidden": int(df["subs_hidden"].fillna(False).astype(bool).sum()),
        "likes_hidden": int(df["likes"].isna().sum()),
    }
    df["valid_perf"] = (df["views"].notna() & (df["views"] >= 0) & df["published_at"].notna() & (df["age_days"] >= 0)
                        & ~df["live_broadcast_content"].isin(["live", "upcoming"]) & (df["duration_sec"] > 0))
    level = "WARNING" if any(v for k, v in checks.items() if k not in ("subscribers_hidden", "likes_hidden", "duplicated_video_id")) else "INFO"
    log(stage, "데이터 검증 결과", level=level, rows_in=n0, rows_out=len(df), valid_perf=int(df["valid_perf"].sum()), **checks)
    if df["published_at"].notna().any():
        log(stage, "업로드일 범위", min=str(df["published_at"].min())[:10], max=str(df["published_at"].max())[:10])
    return df


def build_video_frame(ctx):
    cfg, d = ctx.cfg, ctx.data
    collected_at = pd.Timestamp(d["collected_at"])
    v = d["videos_raw"].copy()
    ch = d["channels_raw"].copy()
    for c in ("views", "likes", "comments"):
        v[c] = pd.to_numeric(v[c], errors="coerce")
    for c in ("subscribers", "channel_views", "channel_video_count"):
        ch[c] = pd.to_numeric(ch[c], errors="coerce")
    v["published_at"] = pd.to_datetime(v["published_at"], utc=True, errors="coerce")
    ch["channel_published_at"] = pd.to_datetime(ch["channel_published_at"], utc=True, errors="coerce")
    v = v.merge(ch, on="channel_id", how="left")
    v["duration_sec"] = parse_iso_duration(v["duration_iso"])
    v["age_days"] = (collected_at - v["published_at"]).dt.total_seconds() / 86400
    v["channel_age_days"] = (collected_at - v["channel_published_at"]).dt.total_seconds() / 86400
    v["was_live"] = v["was_live"].fillna(False).astype(bool)
    v = validate_videos(v, ctx)

    # ---- 성과 지표 (모두 수집 시점 t에서 관측 가능한 값만 사용 → 미래 정보 누수 없음) ----
    v["views_per_day"] = v["views"] / v["age_days"].clip(lower=1)
    v["views_per_sub"] = v["views"] / v["subscribers"].where(v["subscribers"] > 0)
    v["like_rate"] = v["likes"] / v["views"].where(v["views"] > 0)
    v["comment_rate"] = v["comments"] / v["views"].where(v["views"] > 0)
    v["fmt"] = classify_format(v, ctx)
    pub = v["published_at"].dt.tz_convert("Asia/Seoul")
    v["publish_weekday"] = pub.dt.dayofweek
    v["publish_hour"] = pub.dt.hour
    v["weekday_label"] = v["publish_weekday"].map(dict(enumerate(WEEKDAY_LABELS)))
    v["hour_bucket"] = pd.cut(v["publish_hour"], HOUR_BINS, labels=HOUR_LABELS)
    v["channel_size"] = pd.cut(v["subscribers"], CHANNEL_SIZE_BINS, labels=CHANNEL_SIZE_LABELS)
    v["is_small_channel"] = (v["subscribers"] < cfg["SMALL_CHANNEL_MAX_SUBS"]).fillna(False)
    v["is_big_channel"] = (v["subscribers"] >= cfg["BIG_CHANNEL_MIN_SUBS"]).fillna(False)
    v["duration_bucket"] = pd.cut(v["duration_sec"], DURATION_BINS, labels=DURATION_LABELS)
    v["is_mature"] = v["age_days"] >= cfg["MATURE_AGE_DAYS"]
    v["in_window"] = v["age_days"] <= cfg["ANALYSIS_DAYS"]

    # ---- 제목 피처 (벡터화) ----
    t = v["title"].fillna("")
    v["title_len"] = t.str.len()
    for name, rx in TITLE_FEATURE_REGEX.items():
        v[name] = t.str.contains(rx, regex=True)
    for name, words in HOOK_WORD_GROUPS.items():
        v[name] = t.str.contains("|".join(re.escape(w) for w in words), regex=True)

    v = compute_outlier_scores(v, ctx)
    v["is_success"] = (v["valid_perf"] & v["is_mature"] & v["in_window"] & (v["views"] >= cfg["MIN_SUCCESS_VIEWS"])
                       & (v["outlier_score"] >= cfg["OUTLIER_MIN"])).fillna(False)
    v["small_success"] = v["is_success"] & v["is_small_channel"]
    v["video_url"] = v["video_id"].map(video_url)

    perf = v[v["valid_perf"] & v["is_mature"] & v["in_window"]].copy()
    ctx.data["videos"], ctx.data["perf"] = v, perf
    log("FEATURE", "성과 분석 대상 확정 (분석 분할)", all_videos=len(v), perf_videos=len(perf),
        rule=f"valid & age>={cfg['MATURE_AGE_DAYS']}d & age<={cfg['ANALYSIS_DAYS']}d",
        perf_published_min=str(perf["published_at"].min())[:10], perf_published_max=str(perf["published_at"].max())[:10],
        recent_unmatured=int((v["valid_perf"] & ~v["is_mature"]).sum()), out_of_window=int((v["valid_perf"] & ~v["in_window"]).sum()))
    log("FEATURE", "성공(아웃라이어) 판정", success=int(perf["is_success"].sum()),
        success_rate=float(perf["is_success"].mean()) if len(perf) else np.nan,
        small_channel_success=int(perf["small_success"].sum()), rule=f"views>={cfg['MIN_SUCCESS_VIEWS']} & outlier>={cfg['OUTLIER_MIN']}")
    return v


def compute_outlier_scores(v, ctx):
    """outlier_score = 영상 조회수 / 같은 채널 최근 업로드 조회수 중앙값.
    - 대상 영상 자신은 기준선에서 제외(leave-one-out) → 자기 자신이 평균을 끌어올리는 편향 방지
    - 쇼츠형(≤180초)/롱폼/라이브를 따로 비교 (조회수 체계가 달라서)
    - 기준선은 업로드 후 MATURE_AGE_DAYS 이상 지난 영상만 사용 (조회수 누적 미완료 편향 방지)"""
    cfg = ctx.cfg
    b = ctx.data["baseline_raw"].copy()
    b["views"] = pd.to_numeric(b["views"], errors="coerce")
    b["published_at"] = pd.to_datetime(b["published_at"], utc=True, errors="coerce")
    b["age_days"] = (pd.Timestamp(ctx.data["collected_at"]) - b["published_at"]).dt.total_seconds() / 86400
    b["dur"] = parse_iso_duration(b["duration_iso"])
    b = b[b["views"].notna() & (b["age_days"] >= cfg["MATURE_AGE_DAYS"]) & (b["dur"] > 0)
          & ~b["live_broadcast_content"].isin(["live", "upcoming"])]
    b["grp"] = np.where(b["was_live"].fillna(False).astype(bool), "live", np.where(b["dur"] <= 180, "short", "long"))
    v["dur_grp"] = np.where(v["was_live"], "live", np.where(v["duration_sec"] <= 180, "short", "long"))

    by_grp = {k: (g["video_id"].to_numpy(), g["views"].to_numpy(float)) for k, g in b.groupby(["channel_id", "grp"])}
    by_ch = {k: (g["video_id"].to_numpy(), g["views"].to_numpy(float)) for k, g in b.groupby("channel_id")}
    base_views, base_kind, base_n = [], [], []
    min_n = cfg["BASELINE_MIN_N"]
    for vid, cid, grp in zip(v["video_id"], v["channel_id"], v["dur_grp"]):
        val, kind, n = np.nan, "insufficient", 0
        for key, source, label in (((cid, grp), by_grp, "same_format"), (cid, by_ch, "all_formats")):
            if key in source:
                ids, views = source[key]
                sample = views[ids != vid]
                if len(sample) >= min_n:
                    val, kind, n = float(np.median(sample)), label, len(sample)
                    break
        base_views.append(val)
        base_kind.append(kind)
        base_n.append(n)
    v["baseline_views"] = base_views
    v["baseline_kind"] = base_kind
    v["baseline_n"] = base_n
    v["outlier_score"] = v["views"] / v["baseline_views"].where(v["baseline_views"] > 0)
    kinds = Counter(base_kind)
    log("FEATURE", "아웃라이어 배수 계산", baseline_videos=len(b), kinds=dict(kinds),
        median_outlier=float(v["outlier_score"].median()), p90_outlier=float(v["outlier_score"].quantile(0.9)))
    if kinds.get("insufficient", 0) > 0.3 * len(v):
        ctx.note("FEATURE", "기준선 부족 영상 비율이 높음 → 아웃라이어 지표 신뢰도 낮음",
                 insufficient=kinds["insufficient"], total=len(v), hint="MAX_BASELINE_CHANNELS/쿼터 증가 고려")

    # 채널 업로드 빈도 (주당 업로드 수) — 성공한 소규모 채널의 업로드 습관 파악용
    raw = ctx.data["baseline_raw"].copy()
    raw["published_at"] = pd.to_datetime(raw["published_at"], utc=True, errors="coerce")
    g = raw.groupby("channel_id")["published_at"].agg(["min", "max", "size"])
    span_w = ((g["max"] - g["min"]).dt.total_seconds() / (86400 * 7)).clip(lower=1)
    ctx.data["channel_upload_freq"] = (g["size"] / span_w).rename("uploads_per_week")
    v = v.join(ctx.data["channel_upload_freq"], on="channel_id")
    return v


def stage3_features(ctx):
    v = build_video_frame(ctx)
    return v


# =====================================================================================================
# 🧰 [모듈] Stage 4 — 분석
# =====================================================================================================
# VERSION: v2.0.0 — 2026-10-09 — 로직 변경 없음(v1.0.0 유지) (라이브러리 6/10: Stage 4 분석 — 키워드 기회·제목 패턴·포맷·타이밍·클러스터·댓글)
# 키워드 기회점수 가중치 (합=1.0). 각 지표를 키워드 간 백분위(0~1)로 바꾼 뒤 가중합 → 0~100점
KEYWORD_SCORE_WEIGHTS = {
    "demand_vpd": 0.25,       # 수요: 검색 상위 영상의 일평균 조회수 중앙값
    "ac_score": 0.15,         # 검색 수요: 자동완성 노출 점수
    "small_win_share": 0.20,  # 진입 가능성: 검색 상위에 '소규모 채널 + 1만회 이상' 영상 비율
    "median_outlier": 0.15,   # 떡상 가능성: 해당 키워드 영상의 아웃라이어 배수 중앙값
    "fresh_share": 0.10,      # 신선도: 검색 상위 중 최근 FRESH_DAYS일 영상 비율 (새 영상이 노출될 여지)
    "low_competition": 0.15,  # 경쟁 강도(역수): 검색 상위 채널 구독자 중앙값이 낮을수록 높음
}
MIN_GROUP_N = 8          # 그룹 비교 최소 표본
MIN_TOKEN_SUPPORT = 8    # 단어 분석 최소 등장 영상 수
TOKEN_STOPWORDS = {"영상", "채널", "구독", "좋아요", "알림", "SHORTS", "SHORT", "쇼츠", "LIVE", "라이브", "오늘의", "이번"}
QUESTION_RX = r"[?？]|궁금|어떻게|알려\s*주|추천\s*(?:해|좀|부탁)|뭐가|무엇|언제|어디|왜\s|어떤|가능할까|될까요|인가요|나요"


def _mwu_p(a, b):
    try:
        from scipy.stats import mannwhitneyu
        return float(mannwhitneyu(a, b, alternative="two-sided").pvalue)
    except Exception:
        return np.nan


def bh_fdr(pvals):
    """Benjamini-Hochberg 다중비교 보정 q값 (여러 제목 요소를 동시에 검정하므로 우연한 '유의'를 줄임)."""
    p = np.asarray(pvals, dtype=float)
    q = np.full_like(p, np.nan)
    idx = np.where(~np.isnan(p))[0]
    if len(idx) == 0:
        return q
    order = idx[np.argsort(p[idx])]
    m, prev = len(order), 1.0
    for rank in range(m, 0, -1):
        i = order[rank - 1]
        prev = min(prev, p[i] * m / rank)
        q[i] = prev
    return q


def group_perf(df, by, min_n=1):
    if df.empty:
        return pd.DataFrame()
    g = df.groupby(by, observed=True, dropna=True)
    out = g.agg(n=("video_id", "size"), median_views=("views", "median"), median_vpd=("views_per_day", "median"),
                median_outlier=("outlier_score", "median"), success_rate=("is_success", "mean"),
                small_success_rate=("small_success", "mean"), median_views_per_sub=("views_per_sub", "median"))
    out["reliable"] = out["n"] >= min_n
    return out.reset_index()


# ----------------------------------------------------------------------------- 키워드 기회
def analyze_keywords(ctx):
    cfg, d = ctx.cfg, ctx.data
    v = d["videos"].set_index("video_id")
    cols = ["views", "views_per_day", "subscribers", "age_days", "outlier_score", "is_success", "is_small_channel",
            "fmt", "is_mature", "in_window", "valid_perf", "title", "channel_title", "duration_sec"]
    s = d["search_df"].join(v[cols], on="video_id", rsuffix="_v")
    s = s[s["valid_perf"].fillna(False).astype(bool)]
    ac = d["keywords_ac"].set_index("norm")["ac_score"] if not d["keywords_ac"].empty else pd.Series(dtype=float)
    rows = []
    for kw, g in s.groupby("keyword", sort=False):
        rel = g[(g["order"] == "relevance") & (g["rank"] <= cfg["SERP_TOP_N"])]
        uniq = g.drop_duplicates("video_id")
        perfv = uniq[uniq["is_mature"] & uniq["in_window"]]
        top10 = rel.nsmallest(10, "rank")
        fmt_perf = perfv.groupby("fmt")["outlier_score"].agg(["median", "size"])
        fmt_perf = fmt_perf[fmt_perf["size"] >= 5]
        best = perfv.sort_values("outlier_score", ascending=False)
        rows.append({
            "keyword": kw, "serp_n": len(rel),
            "demand_vpd": rel["views_per_day"].median(), "serp_median_views": rel["views"].median(),
            "competition_subs": rel["subscribers"].median(),
            "big_share": (rel["subscribers"] >= cfg["BIG_CHANNEL_MIN_SUBS"]).mean() if len(rel) else np.nan,
            "small_share": (rel["subscribers"] < cfg["SMALL_CHANNEL_MAX_SUBS"]).mean() if len(rel) else np.nan,
            "small_win_share": ((rel["subscribers"] < cfg["SMALL_CHANNEL_MAX_SUBS"]) & (rel["views"] >= cfg["MIN_SUCCESS_VIEWS"])).mean() if len(rel) else np.nan,
            "fresh_share": (rel["age_days"] <= cfg["FRESH_DAYS"]).mean() if len(rel) else np.nan,
            "shorts_share_serp": (rel["fmt"] == "shorts").mean() if len(rel) else np.nan,
            "top_channel_share": top10["channel_id"].value_counts(normalize=True).max() if len(top10) else np.nan,
            "n_videos": len(uniq), "n_perf": len(perfv), "median_outlier": perfv["outlier_score"].median(),
            "success_rate": perfv["is_success"].mean() if len(perfv) else np.nan, "n_success": int(perfv["is_success"].sum()),
            "best_format": fmt_perf["median"].idxmax() if len(fmt_perf) else None,
            "total_results": g["total_results"].max(),
            "ac_score": ac.get(normalize_kw(kw), 0.0),
            "example_ids": list(best["video_id"].head(10)),
            "small_example_ids": list(best.loc[best["is_small_channel"].astype(bool) & (best["views"] >= cfg["MIN_SUCCESS_VIEWS"]), "video_id"].head(3)),
        })
    k = pd.DataFrame(rows)
    if k.empty:
        return k
    # 상위 10개 중 절반 이상이 한 채널 → 채널명 검색(내비게이션 검색) → 기회 분석에서 제외
    k["navigational"] = k["top_channel_share"] >= 0.5
    pool = ~k["navigational"]
    comp = {}
    imputed = Counter()
    for m in KEYWORD_SCORE_WEIGHTS:
        src = "competition_subs" if m == "low_competition" else m
        r = pd.Series(np.nan, index=k.index)
        r[pool] = pct_rank(k.loc[pool, src])
        if m == "low_competition":
            r[pool] = 1 - r[pool]
        imputed[m] = int(r[pool].isna().sum())
        comp[m] = r.fillna(0.5)     # 결측은 중립값(0.5)으로 — 개수는 로그로 남김
        k[f"score_{m}"] = comp[m].round(3)
    k["opportunity"] = (sum(KEYWORD_SCORE_WEIGHTS[m] * comp[m] for m in KEYWORD_SCORE_WEIGHTS) * 100).round(1)
    k.loc[~pool, "opportunity"] = np.nan
    k = k.sort_values("opportunity", ascending=False, na_position="last").reset_index(drop=True)
    log("ANALYSIS", "키워드 기회점수", keywords=len(k), navigational_excluded=int((~pool).sum()),
        weights=KEYWORD_SCORE_WEIGHTS, imputed_neutral=dict(imputed),
        top5=[f"{r.keyword}:{r.opportunity}" for r in k.head(5).itertuples()])
    return k


# ----------------------------------------------------------------------------- 제목 패턴
def analyze_title_features(perf):
    feats = list(TITLE_FEATURE_REGEX) + list(HOOK_WORD_GROUPS)
    segments = {"전체": perf, "롱폼": perf[perf["fmt"] == "long"], "쇼츠": perf[perf["fmt"] == "shorts"]}
    rows = []
    for seg, d in segments.items():
        d = d[d["outlier_score"].notna()]
        for f in feats:
            a, b = d[d[f]], d[~d[f]]
            if len(a) < MIN_GROUP_N or len(b) < MIN_GROUP_N:
                continue
            ma, mb = a["outlier_score"].median(), b["outlier_score"].median()
            rows.append({"segment": seg, "feature": f, "label": FEATURE_LABELS.get(f, f), "n_with": len(a), "n_without": len(b),
                         "median_outlier_with": ma, "median_outlier_without": mb, "lift": ma / mb if mb else np.nan,
                         "success_rate_with": a["is_success"].mean(), "success_rate_without": b["is_success"].mean(),
                         "median_vpd_with": a["views_per_day"].median(), "median_vpd_without": b["views_per_day"].median(),
                         "p_value": _mwu_p(np.log1p(a["outlier_score"]), np.log1p(b["outlier_score"]))})
    out = pd.DataFrame(rows)
    if not out.empty:
        out["q_value"] = np.nan
        for seg in out["segment"].unique():
            m = out["segment"] == seg
            out.loc[m, "q_value"] = bh_fdr(out.loc[m, "p_value"])
        out["significant"] = (out["q_value"] < 0.05) & (out["n_with"] >= MIN_GROUP_N * 2)
        out = out.sort_values(["segment", "lift"], ascending=[True, False]).reset_index(drop=True)
        top = out[(out["segment"] == "전체")].head(5)
        log("ANALYSIS", "제목 피처 효과 (전체, lift 상위)", top=[f"{r.label}:{r.lift:.2f}x(q={r.q_value:.3f})" for r in top.itertuples()], correction="Benjamini-Hochberg FDR")
    return out


def get_tokenizer():
    try:
        from kiwipiepy import Kiwi
        kiwi = Kiwi()

        def tok(texts):
            out = []
            for res in kiwi.tokenize(list(texts)):
                toks = []
                for t in res:
                    if t.tag in ("NNG", "NNP") and len(t.form) >= 2:
                        toks.append(t.form)
                    elif t.tag == "SL" and len(t.form) >= 2:
                        toks.append(t.form.upper())
                out.append(toks)
            return out
        return tok, "kiwipiepy"
    except Exception as e:
        log("ANALYSIS", "kiwipiepy 사용 불가 → 정규식 토크나이저 사용", level="WARNING", error=type(e).__name__)
        particles = re.compile(r"(으로|에서|에게|까지|부터|은|는|이|가|을|를|의|에|로|도|만|과|와)$")

        def tok(texts):
            out = []
            for t in texts:
                ws = re.findall(r"[가-힣]{2,}|[A-Za-z]{2,}", str(t))
                ws = [w.upper() if w.isascii() else (particles.sub("", w) if len(w) > 2 else w) for w in ws]
                out.append([w for w in ws if len(w) >= 2])
            return out
        return tok, "regex"


def analyze_tokens(perf, tokens):
    rows = [(vid, tk) for vid, toks in zip(perf["video_id"], tokens) for tk in set(toks) if tk not in TOKEN_STOPWORDS]
    if not rows:
        return pd.DataFrame()
    ex = pd.DataFrame(rows, columns=["video_id", "token"]).merge(
        perf[["video_id", "outlier_score", "views_per_day", "is_success", "small_success"]], on="video_id")
    n_total, n_succ = len(perf), max(int(perf["is_success"].sum()), 1)
    overall = perf["outlier_score"].median()
    t = ex.groupby("token").agg(n=("video_id", "nunique"), median_outlier=("outlier_score", "median"),
                                median_vpd=("views_per_day", "median"), success_n=("is_success", "sum"),
                                small_success_n=("small_success", "sum"))
    t = t[t["n"] >= MIN_TOKEN_SUPPORT].copy()
    t["success_rate"] = t["success_n"] / t["n"]
    t["outlier_lift"] = t["median_outlier"] / overall if overall else np.nan
    t["success_overrep"] = (t["success_n"] / n_succ) / (t["n"] / n_total)   # 성공 영상에서 과대표집된 정도
    t = t.sort_values(["success_overrep", "outlier_lift"], ascending=False).reset_index()
    return t


def analyze_tags(perf):
    ex = perf[["video_id", "tags", "outlier_score", "is_success"]].explode("tags").dropna(subset=["tags"])
    if ex.empty:
        return pd.DataFrame()
    ex["tag"] = ex["tags"].astype(str).str.strip().str.lower()
    n_total, n_succ = len(perf), max(int(perf["is_success"].sum()), 1)
    t = ex.groupby("tag").agg(n=("video_id", "nunique"), median_outlier=("outlier_score", "median"), success_n=("is_success", "sum"))
    t = t[t["n"] >= MIN_TOKEN_SUPPORT].copy()
    t["success_rate"] = t["success_n"] / t["n"]
    t["success_overrep"] = (t["success_n"] / n_succ) / (t["n"] / n_total)
    return t.sort_values(["success_overrep", "n"], ascending=False).reset_index()


# ----------------------------------------------------------------------------- 하위 주제 클러스터
def cluster_titles(perf, tokens, cfg):
    try:
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.cluster import KMeans
        from sklearn.metrics import silhouette_score
    except ImportError:
        log("ANALYSIS", "scikit-learn 없음 → 클러스터 분석 생략", level="WARNING")
        return pd.DataFrame(), None
    docs = [[t for t in toks if t not in TOKEN_STOPWORDS] for toks in tokens]
    keep = [i for i, dd in enumerate(docs) if dd]
    if len(keep) < 40:
        log("ANALYSIS", "클러스터링 표본 부족 → 생략", level="WARNING", n=len(keep))
        return pd.DataFrame(), None
    vec = TfidfVectorizer(analyzer=lambda x: x, min_df=3, max_df=0.5)
    X = vec.fit_transform([docs[i] for i in keep])
    terms = np.array(vec.get_feature_names_out())
    seed = cfg["RANDOM_SEED"]
    k_max = int(min(12, max(3, len(keep) // 15)))
    scores = {}
    for k in range(3, k_max + 1):
        km = KMeans(n_clusters=k, n_init=10, random_state=seed).fit(X)
        scores[k] = silhouette_score(X, km.labels_, metric="cosine", sample_size=min(2000, X.shape[0]), random_state=seed)
    best_k = max(scores, key=scores.get)
    km = KMeans(n_clusters=best_k, n_init=10, random_state=seed).fit(X)
    log("ANALYSIS", "제목 클러스터링", n_docs=len(keep), vocab=len(terms), silhouette={k: round(s, 3) for k, s in scores.items()},
        best_k=best_k, seed=seed)
    labels = pd.Series(-1, index=perf.index)
    labels.iloc[keep] = km.labels_
    sub = perf.assign(cluster=labels.values)
    sub = sub[sub["cluster"] >= 0]
    rows = []
    for c, g in sub.groupby("cluster"):
        center = km.cluster_centers_[c]
        top_terms = list(terms[np.argsort(center)[::-1][:6]])
        ex = g.sort_values("outlier_score", ascending=False).head(3)
        rows.append({"cluster": int(c), "top_terms": ", ".join(top_terms), "n": len(g),
                     "median_outlier": g["outlier_score"].median(), "median_vpd": g["views_per_day"].median(),
                     "success_rate": g["is_success"].mean(), "small_success_rate": g["small_success"].mean(),
                     "shorts_share": (g["fmt"] == "shorts").mean(),
                     "example_titles": " / ".join(ex["title"].str[:40]), "example_ids": list(ex["video_id"])})
    cl = pd.DataFrame(rows)
    rel = cl["n"] >= 10
    cl["cluster_opportunity"] = np.nan
    cl.loc[rel, "cluster_opportunity"] = ((0.4 * pct_rank(cl.loc[rel, "median_outlier"]) + 0.3 * pct_rank(cl.loc[rel, "small_success_rate"])
                                           + 0.3 * pct_rank(cl.loc[rel, "median_vpd"])) * 100).round(1)
    return cl.sort_values("cluster_opportunity", ascending=False, na_position="last").reset_index(drop=True), sub[["video_id", "cluster"]]


# ----------------------------------------------------------------------------- 댓글(시청자 질문)
def collect_audience_comments(ctx, perf):
    cfg, yt = ctx.cfg, ctx.yt
    n = cfg["FETCH_COMMENTS_TOP_N"]
    if n <= 0 or perf.empty:
        return pd.DataFrame()
    top = perf.sort_values(["is_success", "outlier_score"], ascending=False).head(n)
    rows, fails = [], Counter()
    for vid in top["video_id"]:
        try:
            rows += yt.comment_threads(vid, 100)
        except QuotaExceededError:
            ctx.note("ANALYSIS", "쿼터 소진 → 댓글 수집 중단")
            break
        except YouTubeAPIError as e:
            fails[e.reason] += 1          # commentsDisabled 등은 정상적인 실패
    c = pd.DataFrame(rows, columns=["video_id", "comment", "likes", "published_at", "replies"])
    if not c.empty:
        c["is_question"] = c["comment"].str.contains(QUESTION_RX, regex=True)
    log("ANALYSIS", "댓글 수집", videos=len(top), comments=len(c), questions=int(c.get("is_question", pd.Series(dtype=bool)).sum()),
        failures=dict(fails), quota_used=yt.used)
    return c


# ----------------------------------------------------------------------------- 실행
def stage4_analysis(ctx):
    cfg, d = ctx.cfg, ctx.data
    perf, v = d["perf"], d["videos"]
    if perf.empty:
        raise RuntimeError("성과 분석 대상 영상이 0개입니다 → ANALYSIS_DAYS/MATURE_AGE_DAYS 설정 확인")
    res = {}
    res["keywords"] = analyze_keywords(ctx)
    res["title_features"] = analyze_title_features(perf)
    tl = perf.assign(title_len_bucket=pd.cut(perf["title_len"], [0, 20, 30, 40, 50, 60, 200],
                                             labels=["~20자", "21~30자", "31~40자", "41~50자", "51~60자", "61자+"]))
    res["title_length"] = group_perf(tl, "title_len_bucket", MIN_GROUP_N)
    tok_fn, tok_name = get_tokenizer()
    t0 = time.perf_counter()
    tokens = tok_fn(perf["title"].fillna(""))
    log("ANALYSIS", "제목 토큰화", tokenizer=tok_name, titles=len(tokens), elapsed_sec=round(time.perf_counter() - t0, 2))
    res["tokens"] = analyze_tokens(perf, tokens)
    res["tags"] = analyze_tags(perf)
    res["format"] = group_perf(perf, "fmt", MIN_GROUP_N)
    res["duration"] = group_perf(perf[perf["fmt"] == "long"], "duration_bucket", MIN_GROUP_N)
    res["weekday"] = group_perf(perf, "weekday_label", MIN_GROUP_N)
    res["hour"] = group_perf(perf, "hour_bucket", MIN_GROUP_N)
    hm = perf.pivot_table(index="weekday_label", columns="hour_bucket", values="is_success", aggfunc="mean", observed=False)
    hn = perf.pivot_table(index="weekday_label", columns="hour_bucket", values="video_id", aggfunc="count", observed=False)
    res["timing_heatmap"] = hm.where(hn >= 5).reindex(WEEKDAY_LABELS)
    res["timing_counts"] = hn.reindex(WEEKDAY_LABELS)
    res["channel_size"] = group_perf(perf, "channel_size", MIN_GROUP_N)
    res["clusters"], d["cluster_map"] = cluster_titles(perf, tokens, cfg)
    corr_cols = ["like_rate", "comment_rate", "title_len", "duration_sec", "subscribers", "channel_age_days", "uploads_per_week"]
    cc = perf[corr_cols + ["outlier_score"]].copy()
    cc["outlier_score"] = np.log1p(cc["outlier_score"])
    res["correlations"] = cc.corr(method="spearman")["outlier_score"].drop("outlier_score").rename("spearman_vs_log_outlier").reset_index()
    log("ANALYSIS", "스피어만 상관 (vs log 아웃라이어)", **{r["index"]: r["spearman_vs_log_outlier"] for _, r in res["correlations"].iterrows()})

    res["recent_hot"] = (v[v["valid_perf"] & ~v["is_mature"]].sort_values("views_per_day", ascending=False).head(20))
    res["new_channel_wins"] = (perf[perf["is_success"] & (perf["channel_age_days"] <= 365)]
                               .sort_values("outlier_score", ascending=False).head(20))
    succ_small = perf[perf["small_success"]]
    res["small_channel_upload_freq"] = float(succ_small.drop_duplicates("channel_id")["uploads_per_week"].median()) if len(succ_small) else np.nan
    res["comments"] = collect_audience_comments(ctx, perf)
    if not res["comments"].empty and res["comments"]["is_question"].any():
        q = res["comments"][res["comments"]["is_question"]]
        qt = [t for toks in tok_fn(q["comment"].str[:300]) for t in set(toks) if t not in TOKEN_STOPWORDS]
        res["question_terms"] = pd.Series(Counter(qt)).sort_values(ascending=False).head(40).rename("count").reset_index().rename(columns={"index": "term"})
    else:
        res["question_terms"] = pd.DataFrame(columns=["term", "count"])
    for key in ("format", "duration", "channel_size"):
        if not res[key].empty:
            log("ANALYSIS", f"그룹 성과: {key}", rows=res[key].assign(
                s=lambda x: x.iloc[:, 0].astype(str) + ":n=" + x["n"].astype(str) + ",sr=" + (x["success_rate"] * 100).round(1).astype(str) + "%")["s"].tolist())
    d["analysis"] = res
    return res


# =====================================================================================================
# 🧰 [모듈] Stage 5 — 차트
# =====================================================================================================
# VERSION: v2.0.0 — 2026-10-09 — PC용: 항상 파일 저장(Agg), Windows/Mac/Linux 한글 폰트 탐색 + 나눔고딕 자동 다운로드 (Stage 5 차트)
import matplotlib
matplotlib.use("Agg")      # 화면 없이 PNG 파일로 저장
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.colors import LinearSegmentedColormap

# 색상: 단일 시리즈는 blue 1색, 2개 시리즈는 blue/orange (색각이상 검증 통과 조합), 증감은 blue↔red
C = {"surface": "#fcfcfb", "ink": "#0b0b0b", "ink2": "#52514e", "muted": "#898781", "grid": "#e1e0d9",
     "axis": "#c3c2b7", "blue": "#2a78d6", "orange": "#eb6834", "red": "#e34948", "gray": "#c3c2b7"}
SEQ_BLUE = LinearSegmentedColormap.from_list("seq_blue", ["#cde2fb", "#86b6ef", "#3987e5", "#256abf", "#184f95", "#0d366b"])


FONT_CANDIDATES = [
    "C:/Windows/Fonts/malgun.ttf",                                   # Windows: 맑은 고딕
    "/Library/Fonts/AppleGothic.ttf", "/System/Library/Fonts/Supplemental/AppleGothic.ttf",  # macOS
    "/usr/share/fonts/truetype/nanum/NanumGothic.ttf",               # Linux (fonts-nanum)
    "/System/Library/Fonts/AppleSDGothicNeo.ttc",                    # macOS (ttc)
]
FONT_URLS = ["https://raw.githubusercontent.com/google/fonts/main/ofl/nanumgothic/NanumGothic-Regular.ttf",
             "https://cdn.jsdelivr.net/gh/google/fonts@main/ofl/nanumgothic/NanumGothic-Regular.ttf"]


def _korean_font_candidates(work_dir):
    downloaded = Path(work_dir) / "fonts" / "NanumGothic-Regular.ttf"
    yield from (p for p in FONT_CANDIDATES + [str(downloaded)] if os.path.exists(p))
    yield from (p for p in fm.findSystemFonts()
                if re.search(r"malgun|Nanum|NotoSansKR|NotoSansCJK|Noto Sans CJK|AppleGothic|AppleSDGothic|wqy-zenhei", p, re.I))
    downloaded.parent.mkdir(parents=True, exist_ok=True)              # 마지막 수단: 나눔고딕 다운로드
    for u in FONT_URLS:
        r = http_get(requests.Session(), u, "CHART", retries=2, timeout=30)
        if r is not None and r.status_code == 200 and len(r.content) > 100_000:
            downloaded.write_bytes(r.content)
            yield str(downloaded)
            return


def setup_chart_style(work_dir="."):
    font_name = None
    for path in _korean_font_candidates(work_dir):
        try:
            fm.fontManager.addfont(path)
            font_name = fm.FontProperties(fname=path).get_name()
            plt.rcParams["font.family"] = font_name
            log("CHART", "한글 폰트", font=font_name, path=path)
            break
        except Exception as e:
            log("CHART", "폰트 등록 실패 → 다음 후보", level="DEBUG", path=path, error=type(e).__name__)
    if not font_name:
        log("CHART", "한글 폰트를 찾지 못함 → 차트의 한글이 깨질 수 있음", level="WARNING")
    plt.rcParams.update({
        "axes.unicode_minus": False, "figure.facecolor": C["surface"], "axes.facecolor": C["surface"],
        "savefig.facecolor": C["surface"], "axes.edgecolor": C["axis"], "axes.labelcolor": C["ink2"],
        "xtick.color": C["muted"], "ytick.color": C["muted"], "text.color": C["ink"], "axes.titlecolor": C["ink"],
        "axes.grid": True, "grid.color": C["grid"], "grid.linewidth": 0.8, "axes.axisbelow": True,
        "axes.spines.top": False, "axes.spines.right": False, "axes.titlesize": 13, "axes.titleweight": "bold",
        "axes.titlelocation": "left", "font.size": 10,
    })
    return font_name


def _save(fig, ctx, name, charts):
    path = ctx.out_dir / "charts" / name
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)
    charts[name] = f"charts/{name}"
    log("CHART", "저장", file=name)


FMT_KO = {"long": "롱폼", "shorts": "쇼츠", "live": "라이브"}


def _plain_log_axis(ax, which="both"):
    from matplotlib.ticker import FuncFormatter
    f = FuncFormatter(lambda x, _: fmt_compact(x))
    if which in ("x", "both"):
        ax.xaxis.set_major_formatter(f)
        ax.xaxis.set_minor_formatter(FuncFormatter(lambda x, _: ""))
    if which in ("y", "both"):
        ax.yaxis.set_major_formatter(f)
        ax.yaxis.set_minor_formatter(FuncFormatter(lambda x, _: ""))


def _hbar(ax, labels, values, color, fmt=lambda x: f"{x:.1f}", xlabel=""):
    y = np.arange(len(labels))[::-1]
    ax.barh(y, values, height=0.6, color=color)
    ax.set_yticks(y, labels)
    ax.grid(axis="y", visible=False)
    xmax = np.nanmax(values) if len(values) else 1
    for yi, val in zip(y, values):
        if np.isfinite(val):
            ax.text(val + xmax * 0.01, yi, fmt(val), va="center", fontsize=9, color=C["ink2"])
    ax.set_xlim(0, xmax * 1.15 if xmax > 0 else 1)
    ax.set_xlabel(xlabel)


def stage5_charts(ctx):
    setup_chart_style(ctx.work_dir)
    res, perf, cfg = ctx.data["analysis"], ctx.data["perf"], ctx.cfg
    charts = {}

    def safe(name, fn):
        try:
            fn(name)
        except Exception as e:
            log("CHART", "차트 생성 실패 (건너뜀)", level="WARNING", chart=name, error=f"{type(e).__name__}: {e}")
            plt.close("all")

    def c_keywords(name):
        k = res["keywords"].dropna(subset=["opportunity"]).head(15)
        if k.empty:
            return
        fig, ax = plt.subplots(figsize=(9, 0.42 * len(k) + 1.4))
        _hbar(ax, k["keyword"], k["opportunity"].to_numpy(float), C["blue"], xlabel="기회점수 (0~100)")
        ax.set_title(f"'{cfg['TOPIC']}' 키워드 기회점수 Top {len(k)}")
        _save(fig, ctx, name, charts)

    def c_demand(name):
        k = res["keywords"].dropna(subset=["demand_vpd", "competition_subs"])
        k = k[(k["demand_vpd"] > 0) & (k["competition_subs"] > 0)]
        if len(k) < 3:
            return
        fig, ax = plt.subplots(figsize=(9, 6))
        nav = k["navigational"].astype(bool)
        size = 40 + 260 * (k["ac_score"] / max(k["ac_score"].max(), 1e-9))
        ax.scatter(k.loc[~nav, "competition_subs"], k.loc[~nav, "demand_vpd"], s=size[~nav], color=C["blue"],
                   edgecolor=C["surface"], linewidth=2, label="일반 키워드", zorder=3)
        if nav.any():
            ax.scatter(k.loc[nav, "competition_subs"], k.loc[nav, "demand_vpd"], s=size[nav], color=C["gray"],
                       edgecolor=C["surface"], linewidth=2, label="채널명 검색(제외)", zorder=2)
        ax.set_xscale("log")
        ax.set_yscale("log")
        for r in k[~nav].nlargest(10, "opportunity").itertuples():
            ax.annotate(r.keyword, (r.competition_subs, r.demand_vpd), xytext=(6, 4), textcoords="offset points", fontsize=9, color=C["ink2"])
        ax.set_xlabel("경쟁 강도: 검색 상위 채널 구독자 중앙값 (로그)")
        ax.set_ylabel("수요: 검색 상위 영상 일평균 조회수 중앙값 (로그)")
        ax.set_title("수요 vs 경쟁 — 왼쪽 위(수요↑·경쟁↓)가 기회 (원 크기=자동완성 수요)")
        _plain_log_axis(ax)
        if nav.any():
            ax.legend(frameon=False, loc="lower right")
        _save(fig, ctx, name, charts)

    def c_views_subs(name):
        d = perf.dropna(subset=["subscribers", "views"])
        d = d[(d["subscribers"] > 0) & (d["views"] > 0)]
        if len(d) < 10:
            return
        fig, ax = plt.subplots(figsize=(9, 6))
        ok = d["is_success"].astype(bool)
        ax.scatter(d.loc[~ok, "subscribers"], d.loc[~ok, "views"], s=14, color=C["blue"], alpha=0.35, label="일반 영상", linewidths=0)
        ax.scatter(d.loc[ok, "subscribers"], d.loc[ok, "views"], s=26, color=C["orange"], edgecolor=C["surface"], linewidth=1,
                   label=f"성공(채널 평균 {cfg['OUTLIER_MIN']:.0f}배↑ & {fmt_compact(cfg['MIN_SUCCESS_VIEWS'])}회↑)")
        ax.set_xscale("log")
        ax.set_yscale("log")
        lo, hi = max(d["subscribers"].min(), 1), d["subscribers"].max()
        xs = np.logspace(np.log10(lo), np.log10(hi), 50)
        for mult in (1, 10):
            ax.plot(xs, xs * mult, color=C["muted"], linewidth=1)
            ax.annotate(f"조회수 = 구독자×{mult}", (xs[-1], xs[-1] * mult), fontsize=8, color=C["muted"], ha="right", va="bottom")
        ax.axvline(cfg["SMALL_CHANNEL_MAX_SUBS"], color=C["axis"], linewidth=1)
        ax.set_xlabel("채널 구독자 수 (로그)")
        ax.set_ylabel("영상 조회수 (로그)")
        ax.set_title("구독자 대비 조회수 — 세로선 왼쪽 = 소규모 채널")
        _plain_log_axis(ax)
        ax.legend(frameon=False, loc="upper left")
        _save(fig, ctx, name, charts)

    def c_group(name, key, title, label_col):
        g = res[key]
        if g is None or g.empty:
            return
        g = g[g["n"] >= 1]
        fig, axes = plt.subplots(1, 3, figsize=(13, 0.42 * len(g) + 1.8), sharey=True)
        labels = [f"{FMT_KO.get(a, a)} (n={n})" for a, n in zip(g[label_col].astype(str), g["n"])]
        _hbar(axes[0], labels, g["median_outlier"].to_numpy(float), C["blue"], lambda x: f"{x:.2f}배", "채널 평균 대비 배수(중앙값)")
        _hbar(axes[1], labels, (g["success_rate"] * 100).to_numpy(float), C["blue"], lambda x: f"{x:.1f}%", "성공 비율(%)")
        _hbar(axes[2], labels, g["median_vpd"].to_numpy(float), C["blue"], fmt_compact, "일평균 조회수(중앙값)")
        fig.suptitle(title, x=0.01, ha="left", fontsize=13, fontweight="bold")
        _save(fig, ctx, name, charts)

    def c_title_lift(name):
        t = res["title_features"]
        if t.empty:
            return
        t = t[t["segment"] == "전체"].sort_values("lift")
        fig, ax = plt.subplots(figsize=(9, 0.38 * len(t) + 1.6))
        vals = np.log2(t["lift"].to_numpy(float))
        colors = [C["blue"] if x >= 0 else C["red"] for x in vals]
        y = np.arange(len(t))
        ax.barh(y, vals, height=0.6, color=colors)
        ax.set_yticks(y, [f"{l}{' *' if s else ''} (n={n})" for l, s, n in zip(t["label"], t["significant"], t["n_with"])])
        ax.axvline(0, color=C["axis"], linewidth=1)
        ax.grid(axis="y", visible=False)
        for yi, x, lift in zip(y, vals, t["lift"]):
            ax.text(x + (0.03 if x >= 0 else -0.03), yi, f"{lift:.2f}배", va="center", ha="left" if x >= 0 else "right", fontsize=9, color=C["ink2"])
        lim = max(np.abs(vals).max() * 1.35, 0.5)
        ax.set_xlim(-lim, lim)
        ax.set_xlabel("효과 (log2 배수: 오른쪽=해당 요소가 있을 때 아웃라이어 배수↑)   * = 다중비교 보정 후 유의(q<0.05)")
        ax.set_title("제목 요소별 효과 (포함 vs 미포함, 아웃라이어 배수 중앙값 비)")
        _save(fig, ctx, name, charts)

    def c_timing(name):
        hm = res["timing_heatmap"]
        if hm is None or hm.dropna(how="all").empty:
            return
        fig, ax = plt.subplots(figsize=(10, 4.6))
        data = (hm * 100).to_numpy(float)
        im = ax.imshow(np.ma.masked_invalid(data), cmap=SEQ_BLUE, aspect="auto")
        ax.set_xticks(range(hm.shape[1]), [str(c) for c in hm.columns])
        ax.set_yticks(range(hm.shape[0]), list(hm.index))
        ax.grid(False)
        vmax = np.nanmax(data) if np.isfinite(data).any() else 1
        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                if np.isfinite(data[i, j]):
                    ax.text(j, i, f"{data[i, j]:.0f}%", ha="center", va="center", fontsize=8,
                            color="white" if data[i, j] > vmax * 0.6 else C["ink"])
        cb = fig.colorbar(im, ax=ax, fraction=0.03)
        cb.set_label("성공 비율(%)")
        ax.set_title("업로드 요일×시간(KST)별 성공 비율 — 빈칸=표본 5개 미만")
        _save(fig, ctx, name, charts)

    def c_tokens(name):
        t = res["tokens"]
        if t is None or t.empty:
            return
        t = t[t["success_n"] >= 2].head(20)
        if t.empty:
            return
        fig, ax = plt.subplots(figsize=(9, 0.38 * len(t) + 1.4))
        _hbar(ax, [f"{a} (n={n})" for a, n in zip(t["token"], t["n"])], t["success_overrep"].to_numpy(float), C["blue"],
              lambda x: f"{x:.2f}배", "성공 영상에서의 과대표집 배수 (1=평균)")
        ax.axvline(1, color=C["axis"], linewidth=1)
        ax.set_title("성공 영상 제목에 유독 많이 등장하는 단어 Top 20")
        _save(fig, ctx, name, charts)

    def c_clusters(name):
        cl = res["clusters"]
        if cl is None or cl.empty:
            return
        cl = cl.dropna(subset=["cluster_opportunity"]).head(12)
        if cl.empty:
            return
        fig, ax = plt.subplots(figsize=(10, 0.45 * len(cl) + 1.4))
        _hbar(ax, [f"{t[:28]} (n={n})" for t, n in zip(cl["top_terms"], cl["n"])], cl["cluster_opportunity"].to_numpy(float),
              C["blue"], xlabel="하위 주제 기회점수 (0~100)")
        ax.set_title("하위 주제(제목 클러스터)별 기회점수")
        _save(fig, ctx, name, charts)

    safe("01_keyword_opportunity.png", c_keywords)
    safe("02_demand_vs_competition.png", c_demand)
    safe("03_views_vs_subscribers.png", c_views_subs)
    safe("04_format_performance.png", lambda n: c_group(n, "format", "포맷별 성과 (쇼츠 / 롱폼 / 라이브)", "fmt"))
    safe("05_duration_performance.png", lambda n: c_group(n, "duration", "롱폼 길이별 성과", "duration_bucket"))
    safe("06_title_feature_lift.png", c_title_lift)
    safe("07_publish_timing_heatmap.png", c_timing)
    safe("08_channel_size_performance.png", lambda n: c_group(n, "channel_size", "채널 규모별 성과 — 작은 채널도 터질 수 있나?", "channel_size"))
    safe("09_success_tokens.png", c_tokens)
    safe("10_subtopic_clusters.png", c_clusters)
    safe("11_title_length.png", lambda n: c_group(n, "title_length", "제목 길이별 성과", "title_len_bucket"))
    ctx.data["charts"] = charts
    log("CHART", "차트 생성 요약", n=len(charts), files=list(charts))
    return charts


# =====================================================================================================
# 🧰 [모듈] Stage 6 — 성공사례(대본·영상)
# =====================================================================================================
# VERSION: v2.0.0 — 2026-10-09 — PC용: 쿠키 파일/브라우저 쿠키, Windows 안전 처리(인코딩·파일 교체·삭제), PC용 스크립트 생성 제거 (Stage 6 성공사례)
VIDEO_EXTS = {".mp4", ".mkv", ".webm", ".mov", ".m4a", ".mp3", ".opus"}
SUCCESS_SCORE_WEIGHTS = {"outlier": 0.40, "views": 0.35, "views_per_sub": 0.25}


def select_success_cases(perf, cfg):
    """성공사례 선정: 종합점수(아웃라이어·조회수·구독자대비조회수 백분위 가중합) + 다양성 제약.
    제약: 소규모 채널 최소 비율, 롱폼 최소 비율, 채널당 최대 개수."""
    N = cfg["SUCCESS_CASE_COUNT"]
    cand = perf[(perf["views"] >= cfg["MIN_SUCCESS_VIEWS"]) & perf["outlier_score"].notna()].copy()
    if cand.empty or N <= 0:
        return cand.head(0)
    vps = np.log1p(cand["views_per_sub"].fillna(cand["views_per_sub"].median()))
    cand["case_score"] = (100 * (SUCCESS_SCORE_WEIGHTS["outlier"] * pct_rank(np.log1p(cand["outlier_score"]))
                                 + SUCCESS_SCORE_WEIGHTS["views"] * pct_rank(np.log1p(cand["views"]))
                                 + SUCCESS_SCORE_WEIGHTS["views_per_sub"] * pct_rank(vps))).round(1)
    strong = cand[cand["outlier_score"] >= cfg["OUTLIER_MIN"]].sort_values("case_score", ascending=False)
    weak = cand[cand["outlier_score"] < cfg["OUTLIER_MIN"]].sort_values("case_score", ascending=False)
    if len(strong) < N:
        log("SUCCESS", "아웃라이어 기준 충족 영상이 부족 → 종합점수 상위로 보충", level="WARNING", strong=len(strong), need=N)
    pool = pd.concat([strong, weak])
    picks, reasons, per_ch = [], {}, Counter()

    def take(mask, quota, reason):
        for idx in pool.index[mask.loc[pool.index]]:
            if quota is not None and sum(mask.loc[i] for i in picks) >= quota:
                return
            if len(picks) >= N:
                return
            cid = pool.at[idx, "channel_id"]
            if idx in picks or per_ch[cid] >= cfg["MAX_CASES_PER_CHANNEL"]:
                continue
            picks.append(idx)
            reasons[idx] = reason
            per_ch[cid] += 1

    take(pool["is_small_channel"].astype(bool), math.ceil(N * cfg["SUCCESS_SMALL_CHANNEL_SHARE"]), "소규모 채널 쿼터")
    take(pool["fmt"] == "long", math.ceil(N * cfg["SUCCESS_LONGFORM_SHARE"]), "롱폼 쿼터")
    take(pd.Series(True, index=pool.index), None, "종합점수 상위")
    sel = pool.loc[picks].assign(selection_reason=[reasons[i] for i in picks]).sort_values("case_score", ascending=False)
    log("SUCCESS", "성공사례 선정", n=len(sel), candidates=len(cand), strong=len(strong), weights=SUCCESS_SCORE_WEIGHTS,
        small_channel=int(sel["is_small_channel"].sum()), longform=int((sel["fmt"] == "long").sum()),
        channels=sel["channel_id"].nunique())
    for r in sel.itertuples():
        log("SUCCESS", "선정", level="DEBUG", video_id=r.video_id, score=r.case_score, outlier=r.outlier_score,
            views=r.views, subs=r.subscribers, reason=r.selection_reason)
    return sel


# ----------------------------------------------------------------------------- yt-dlp
BOT_CHECK_RX = re.compile(r"confirm you.?re not a bot|Sign in to confirm|LOGIN_REQUIRED", re.I)
# 일시적인 오류(간헐적 403·응답 추출 실패·5xx·타임아웃) → 잠시 후 같은 클라이언트로 재시도
TRANSIENT_RX = re.compile(r"Failed to extract any player response|HTTP Error (403|429|5\d\d)|timed out|Connection reset|"
                          r"Remote end closed|IncompleteRead|Temporary failure", re.I)
TRANSIENT_WAITS = (3, 8)
# 봇 확인에 걸리면 순서대로 다른 YouTube 클라이언트로 재시도 ("default" = yt-dlp 기본 선택)
YT_CLIENT_FALLBACKS = [("default",), ("tv_simply",), ("tv",), ("web_embedded",), ("mweb",)]
# 다운로드 인증/상태 (프록시는 비밀값이므로 cfg/run_info에 넣지 않고 여기만 보관)
DL_STATE = {"proxy": "", "cookiefile": "", "client": None, "bot_streak": 0, "bot_total": 0, "disabled": False,
            "client_hits": Counter(), "last_blocked": None}


class BotCheckError(RuntimeError):
    """YouTube 'Sign in to confirm you're not a bot' — IP 평판(데이터센터·VPN·과도한 요청) 기반 차단."""


class _YtdlpLogger:
    def __init__(self):
        self.errors = []

    def debug(self, msg):
        if not msg.startswith("[debug]"):
            log("DOWNLOAD", "yt-dlp", level="DEBUG", detail=msg[:200])

    def info(self, msg):
        self.debug(msg)

    def warning(self, msg):
        log("DOWNLOAD", "yt-dlp 경고", level="DEBUG", detail=msg[:300])

    def error(self, msg):
        self.errors.append(msg)
        # 봇 확인 오류는 클라이언트 재시도 과정에서 반복되므로 요약 로그(run_ytdlp)로만 남김
        log("DOWNLOAD", "yt-dlp 오류", level="DEBUG" if BOT_CHECK_RX.search(msg) else "WARNING", detail=msg[:300])


_JS_RUNTIMES = {}


def _js_runtimes():
    """yt-dlp용 JS 런타임 탐색 (deno → node). 한 번만 찾고 재사용."""
    if "v" not in _JS_RUNTIMES:
        js = {}
        deno = shutil.which("deno")
        if not deno:
            try:
                from deno import find_deno_bin
                deno = find_deno_bin()
            except Exception:
                deno = None
        if deno:
            js["deno"] = {"path": deno}
        if shutil.which("node"):
            js["node"] = {"path": shutil.which("node")}
        _JS_RUNTIMES["v"] = js
    return dict(_JS_RUNTIMES["v"])


def ytdlp_base_opts(cfg):
    opts = {"quiet": True, "no_warnings": True, "noprogress": True, "noplaylist": True, "retries": 5,
            "fragment_retries": 5, "socket_timeout": 30, "concurrent_fragment_downloads": 4, "logger": _YtdlpLogger()}
    js = _js_runtimes()
    if js:
        opts["js_runtimes"] = js
    ff = find_ffmpeg()
    if ff:
        opts["ffmpeg_location"] = ff        # 영상+음성 병합용 (시스템 ffmpeg가 없으면 imageio-ffmpeg 사용)
    if DL_STATE["cookiefile"] and os.path.exists(DL_STATE["cookiefile"]):
        opts["cookiefile"] = DL_STATE["cookiefile"]
    elif cfg.get("COOKIES_FROM_BROWSER"):
        opts["cookiesfrombrowser"] = (str(cfg["COOKIES_FROM_BROWSER"]).strip().lower(),)
    if DL_STATE["proxy"]:
        opts["proxy"] = DL_STATE["proxy"]
    return opts


def run_ytdlp(cfg, extra_opts, fn, video_id):
    """yt-dlp 실행 래퍼.
    - 봇 확인 오류 → 다른 player_client로 재시도, 성공한 클라이언트는 이후 영상에 우선 사용
    - 연속 YTDLP_MAX_BOT_BLOCKS개 영상이 모든 클라이언트에서 막히면 이후 yt-dlp 시도 중단 (시간 낭비·IP 평판 악화 방지)"""
    from yt_dlp import YoutubeDL
    if DL_STATE["disabled"]:
        raise BotCheckError("봇 확인 차단이 반복되어 이번 실행에서는 yt-dlp 시도를 중단함")
    if not cfg["YTDLP_CLIENT_FALLBACK"]:
        order = [("default",)]
    elif DL_STATE["client"]:
        order = [DL_STATE["client"]] + [c for c in YT_CLIENT_FALLBACKS if c != DL_STATE["client"]]
    else:
        order = list(YT_CLIENT_FALLBACKS)
    tried = []
    for client in order:
        opts = {**ytdlp_base_opts(cfg), **extra_opts}
        if client != ("default",):
            opts["extractor_args"] = {"youtube": {"player_client": list(client)}}
        result, err = None, None
        for wait in (0, *TRANSIENT_WAITS):
            if wait:
                log("DOWNLOAD", "일시 오류 → 재시도", level="INFO", video_id=video_id, client="+".join(client),
                    wait_sec=wait, error=str(err)[:120])
                time.sleep(wait)
            try:
                with YoutubeDL(opts) as ydl:
                    result, err = fn(ydl), None
                break
            except Exception as e:
                err = e
                if BOT_CHECK_RX.search(str(e)) or not TRANSIENT_RX.search(str(e)):
                    break
        if err is not None:
            if BOT_CHECK_RX.search(str(err)):
                tried.append("+".join(client))
                continue
            raise err
        if client != DL_STATE["client"]:
            log("DOWNLOAD", "yt-dlp 클라이언트 선택", video_id=video_id, client="+".join(client),
                after_bot_check=tried or None)
        DL_STATE.update(client=client, bot_streak=0, last_blocked=None)
        DL_STATE["client_hits"]["+".join(client)] += 1
        return result
    if DL_STATE["last_blocked"] != video_id:   # 같은 영상의 영상/자막/음성 시도는 1회로 집계 (연속 '영상' 기준)
        DL_STATE["bot_streak"] += 1
        DL_STATE["bot_total"] += 1
        DL_STATE["last_blocked"] = video_id
    log("DOWNLOAD", "YouTube 봇 확인 차단 (모든 클라이언트 실패)", level="WARNING", video_id=video_id, clients=tried,
        cookies=bool(DL_STATE["cookiefile"]), proxy=bool(DL_STATE["proxy"]), streak=DL_STATE["bot_streak"])
    if DL_STATE["bot_streak"] >= cfg["YTDLP_MAX_BOT_BLOCKS"]:
        DL_STATE["disabled"] = True
        log("DOWNLOAD", "❌ 봇 확인 차단이 연속 발생 → 이번 실행의 yt-dlp 다운로드 중단", level="ERROR",
            fix=("(1) VPN을 끄고 잠시 후 다시 실행 "
                 "(2) 쿠키 사용: 시크릿 창에서 YouTube 로그인 → youtube.com/robots.txt 이동 → "
                 "'Get cookies.txt LOCALLY' 확장으로 cookies.txt 저장 → 시크릿 창 닫기 → 이 스크립트 폴더에 cookies.txt 두기 "
                 "(또는 설정 COOKIES_FROM_BROWSER='firefox') → 다시 실행 (API 응답은 캐시되어 쿼터를 거의 안 씀)"))
    raise BotCheckError(f"봇 확인 차단 (시도한 클라이언트: {', '.join(tried)})")


def refresh_download_auth(ctx, proxy=""):
    """Stage 6 직전에 호출: 쿠키(파일/브라우저)·프록시 준비 + 봇 확인 상태 초기화."""
    path, source = prepare_cookies(ctx.cfg, ctx.work_dir)
    if not path and ctx.cfg.get("COOKIES_FROM_BROWSER"):
        source = f"browser:{ctx.cfg['COOKIES_FROM_BROWSER']}"
    DL_STATE.update(cookiefile=path, proxy=(proxy or "").strip(), client=None, bot_streak=0, bot_total=0, disabled=False,
                    last_blocked=None)
    DL_STATE["client_hits"].clear()
    register_secret(DL_STATE["proxy"])
    info = inspect_cookies(path) if path else {}
    log("AUTH", "다운로드 인증 준비", cookies=source, proxy=bool(DL_STATE["proxy"]), **info)
    if path and not info.get("auth_cookies"):
        ctx.note("AUTH", "쿠키에 로그인 쿠키(SID/__Secure-3PSID/LOGIN_INFO 등)가 없음 → 봇 확인을 통과하지 못할 수 있음",
                 hint="YouTube에 로그인한 상태에서 cookies.txt를 다시 내보내세요")
    if info.get("expired_auth"):
        ctx.note("AUTH", "로그인 쿠키가 만료됨 → cookies.txt를 다시 내보내세요", expired=info["expired_auth"])
    return {"cookies": source, "proxy": bool(DL_STATE["proxy"]), **info}


def ytdlp_download(video_id, out_dir, cfg, audio_only=False):
    h = cfg["VIDEO_MAX_HEIGHT"]
    name = "audio" if audio_only else "video"
    extra = {"outtmpl": str(Path(out_dir) / f"{name}.%(ext)s"), "merge_output_format": "mp4",
             "format": ("ba[ext=m4a]/ba/b" if audio_only else
                        f"bv*[height<={h}][ext=mp4]+ba[ext=m4a]/b[height<={h}][ext=mp4]/bv*[height<={h}]+ba/b[height<={h}]/wv*+ba/w")}
    run_ytdlp(cfg, extra, lambda ydl: ydl.extract_info(video_url(video_id), download=True), video_id)
    files = [p for p in Path(out_dir).glob(f"{name}.*") if p.suffix.lower() in VIDEO_EXTS]
    if not files:
        raise RuntimeError("다운로드 파일 없음")
    return max(files, key=lambda p: p.stat().st_size)


def media_duration(path):
    """실제 파일 길이(초): ffprobe → (없으면) ffmpeg -i 출력 파싱. 실패 시 None → 메타데이터 길이 사용."""
    if shutil.which("ffprobe"):
        r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
                           capture_output=True, text=True, encoding="utf-8", errors="replace")
        try:
            return float(r.stdout.strip())
        except ValueError:
            pass
    ff = find_ffmpeg()
    if ff:
        r = subprocess.run([ff, "-hide_banner", "-i", str(path)], capture_output=True, text=True, encoding="utf-8", errors="replace")
        m = re.search(r"Duration:\s*(\d+):(\d+):(\d+(?:\.\d+)?)", r.stderr)
        if m:
            return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3))
    return None


def ensure_max_size(path, max_mb, duration_sec):
    """파일이 max_mb 초과 시 ffmpeg로 목표 비트레이트 재인코딩 (H.264/AAC mp4)."""
    path = Path(path)
    size = path.stat().st_size / 1e6
    if size <= max_mb and path.suffix.lower() == ".mp4":
        return path, "original", size
    ff = find_ffmpeg()
    if not ff:
        return path, ("original" if size <= max_mb else "too_large"), size
    out = path.with_name("video_resized.mp4")

    def _finish(how):
        new = out.stat().st_size / 1e6
        path.unlink()
        final = path.with_suffix(".mp4")
        os.replace(out, final)              # Windows에서도 덮어쓰기 가능한 교체
        return final, how, new

    if size <= max_mb:      # 크기는 괜찮고 컨테이너만 mp4가 아닌 경우 → 무손실 리먹스 (실패 시 원본 유지)
        r = subprocess.run([ff, "-y", "-loglevel", "error", "-i", str(path), "-c", "copy", "-movflags", "+faststart", str(out)],
                           capture_output=True, text=True, encoding="utf-8", errors="replace")
        return _finish("remux") if r.returncode == 0 and out.exists() else (path, "original", size)
    dur = max(media_duration(path) or float(duration_sec or 0), 1.0)
    factor = 1.0
    for attempt in (1, 2):
        total_kbps = max_mb * 8000 * 0.92 / dur * factor
        a_kbps = 64 if total_kbps > 400 else 48
        v_kbps = max(int(total_kbps - a_kbps), 60)
        height = 480 if v_kbps >= 500 else (360 if v_kbps >= 220 else 240)
        cmd = [ff, "-y", "-loglevel", "error", "-i", str(path), "-c:v", "libx264", "-preset", "veryfast",
               "-b:v", f"{v_kbps}k", "-maxrate", f"{int(v_kbps * 1.2)}k", "-bufsize", f"{v_kbps * 2}k",
               "-vf", f"scale=-2:'min({height},ih)'", "-c:a", "aac", "-b:a", f"{a_kbps}k", "-ac", "1",
               "-movflags", "+faststart", str(out)]
        t0 = time.perf_counter()
        r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
        if r.returncode != 0 or not out.exists():
            log("DOWNLOAD", "ffmpeg 실패", level="WARNING", stderr=r.stderr[-300:])
            break
        new = out.stat().st_size / 1e6
        log("DOWNLOAD", "영상 용량 조정(재인코딩)", attempt=attempt, before_mb=round(size, 1), after_mb=round(new, 1),
            v_kbps=v_kbps, height=height, elapsed_sec=round(time.perf_counter() - t0, 1))
        if new <= max_mb:
            return _finish("transcoded")
        factor *= 0.8 * max_mb / new
    out.unlink(missing_ok=True)
    return path, "too_large", size


# ----------------------------------------------------------------------------- 대본(자막)
def _ts(x):
    p = x.replace(",", ".").split(":")
    p = [float(v) for v in p]
    return p[0] * 3600 + p[1] * 60 + p[2] if len(p) == 3 else p[0] * 60 + p[1]


def parse_vtt(text):
    """WebVTT → [{start, duration, text}]. 유튜브 자동자막의 '롤링 중복 줄' 제거."""
    segs, recent = [], deque(maxlen=4)
    for block in re.split(r"\n\s*\n", text.replace("\r", "")):
        lines = [l for l in block.strip().split("\n") if l.strip()]
        ti = next((i for i, l in enumerate(lines) if "-->" in l), None)
        if ti is None:
            continue
        a, b = lines[ti].split("-->")
        try:
            start, end = _ts(a.strip()), _ts(b.strip().split(" ")[0])
        except (ValueError, IndexError):
            continue
        for raw in lines[ti + 1:]:
            t = html.unescape(re.sub(r"<[^>]+>", "", raw)).strip()
            if t and t not in recent:
                segs.append({"start": round(start, 2), "duration": round(max(end - start, 0), 2), "text": t})
                recent.append(t)
    return segs


def transcript_via_api(video_id, langs, retries=2):
    """youtube-transcript-api: 수동 자막(langs 순) → 자동 자막(langs 순) → 아무 트랙. 차단(RequestBlocked) 시 1회 재시도."""
    from youtube_transcript_api import YouTubeTranscriptApi, RequestBlocked
    proxy_cfg = None
    if DL_STATE["proxy"]:
        from youtube_transcript_api.proxies import GenericProxyConfig
        proxy_cfg = GenericProxyConfig(http_url=DL_STATE["proxy"], https_url=DL_STATE["proxy"])
    for attempt in range(1, retries + 1):
        try:
            tl = YouTubeTranscriptApi(proxy_config=proxy_cfg).list(video_id)
            break
        except RequestBlocked:
            if attempt == retries:
                raise
            time.sleep(4 * attempt)
    t = None
    for finder in (tl.find_manually_created_transcript, tl.find_generated_transcript):
        try:
            t = finder(langs)
            break
        except Exception:
            continue
    if t is None:
        t = next(iter(tl), None)
    if t is None:
        raise RuntimeError("자막 트랙 없음")
    segs = [{"start": round(s.start, 2), "duration": round(s.duration, 2), "text": s.text.replace("\n", " ").strip()}
            for s in t.fetch()]
    return segs, {"source": "youtube_transcript_api", "language": t.language_code, "auto_generated": t.is_generated}


def transcript_via_ytdlp(video_id, langs, tmp_dir, cfg):
    """yt-dlp로 자막 트랙 목록 확인 후 '하나만' 내려받기.
    우선순위: 수동 자막(langs) → 원어 자동자막(*-orig) → 번역 자동자막(langs). 번역 트랙은 429 차단이 잦아 마지막."""
    def fetch(ydl):
        info = ydl.extract_info(video_url(video_id), download=False)
        subs, autos = info.get("subtitles") or {}, info.get("automatic_captions") or {}
        orig = [k for k in autos if k.endswith("-orig")]
        choice = next(((l, subs[l], False) for l in langs if l in subs), None)
        choice = choice or next(((k, autos[k], True) for k in orig), None)
        choice = choice or next(((l, autos[l], True) for l in langs if l in autos), None)
        if choice is None:
            raise RuntimeError(f"자막 트랙 없음 (manual={sorted(subs)[:5]}, auto={len(autos)})")
        lang, fmts, auto = choice
        vtt = next((x for x in fmts if x.get("ext") == "vtt"), None)
        if vtt is None:
            raise RuntimeError(f"vtt 형식 없음 lang={lang}")
        for attempt in (1, 2):
            try:
                return ydl.urlopen(vtt["url"]).read().decode("utf-8", "replace"), lang, auto
            except Exception as e:
                if attempt == 2:
                    raise RuntimeError(f"자막 다운로드 실패 lang={lang}: {type(e).__name__}: {str(e)[:120]}")
                time.sleep(5)

    text, lang, auto = run_ytdlp(cfg, {"skip_download": True}, fetch, video_id)
    segs = parse_vtt(text)
    if not segs:
        raise RuntimeError("자막 파싱 결과 비어 있음")
    return segs, {"source": "yt_dlp_subtitles", "language": lang.replace("-orig", ""), "auto_generated": auto}


_WHISPER = {}


def transcript_via_whisper(media_path, cfg, duration_sec):
    from faster_whisper import WhisperModel
    try:
        import ctranslate2
        cuda = ctranslate2.get_cuda_device_count() > 0
    except Exception:
        cuda = False
    if _WHISPER.get("gpu_failed"):
        cuda = False
    if not cuda and duration_sec and duration_sec / 60 > cfg["WHISPER_CPU_MAX_MINUTES"]:
        raise RuntimeError(f"GPU 없이 {duration_sec / 60:.0f}분 영상은 Whisper 생략 (Accelerator=GPU 권장)")
    ff = find_ffmpeg()
    if not ff:
        raise RuntimeError("ffmpeg 없음 → pip install imageio-ffmpeg 후 다시 실행")
    t0 = time.perf_counter()
    # 오디오는 ffmpeg로 직접 디코딩(16kHz mono) → PyAV 버전 호환성 문제 회피
    pcm = subprocess.run([ff, "-nostdin", "-loglevel", "error", "-i", str(media_path), "-f", "s16le", "-ac", "1",
                          "-ar", "16000", "-"], capture_output=True, check=True).stdout
    audio = np.frombuffer(pcm, np.int16).astype(np.float32) / 32768.0

    def _model(use_cuda):
        key = (cfg["WHISPER_MODEL"], use_cuda)
        if key not in _WHISPER:
            t1 = time.perf_counter()
            # GPU: compute_type="auto" (T4=float16, P100처럼 float16 미지원 GPU는 자동으로 다른 정밀도 선택)
            _WHISPER[key] = WhisperModel(cfg["WHISPER_MODEL"], device="cuda" if use_cuda else "cpu",
                                         compute_type="auto" if use_cuda else "int8")
            log("TRANSCRIPT", "Whisper 모델 로드", model=cfg["WHISPER_MODEL"], device="cuda" if use_cuda else "cpu",
                elapsed_sec=round(time.perf_counter() - t1, 1))
        return _WHISPER[key]

    def _run(use_cuda):
        for vad in (True, False):   # VAD가 음악/배경음 위주 구간을 전부 걸러내면 VAD 없이 재시도
            segments, info = _model(use_cuda).transcribe(audio, language=cfg["LANGUAGE"] or None, vad_filter=vad, beam_size=5)
            segs = [{"start": round(s.start, 2), "duration": round(s.end - s.start, 2), "text": s.text.strip()} for s in segments]
            if segs:
                break
        return segs, info, vad

    try:
        segs, info, vad = _run(cuda)
    except Exception as e:
        if not cuda:
            raise
        # PC의 CUDA/cuDNN 버전이 ctranslate2와 안 맞는 경우 등 → CPU로 재시도
        _WHISPER["gpu_failed"] = True
        log("TRANSCRIPT", "Whisper GPU 실행 실패 → CPU로 재시도", level="WARNING", error=f"{type(e).__name__}: {str(e)[:150]}")
        if duration_sec and duration_sec / 60 > cfg["WHISPER_CPU_MAX_MINUTES"]:
            raise RuntimeError(f"GPU 실패 + CPU로 {duration_sec / 60:.0f}분 영상은 Whisper 생략")
        segs, info, vad = _run(False)
    log("TRANSCRIPT", "Whisper 음성인식 완료", segments=len(segs), vad_filter=vad, audio_sec=round(len(audio) / 16000),
        elapsed_sec=round(time.perf_counter() - t0, 1))
    return segs, {"source": f"whisper_{cfg['WHISPER_MODEL']}", "language": info.language, "auto_generated": True}


def _mmss(sec):
    sec = int(sec)
    return f"{sec // 3600:d}:{sec % 3600 // 60:02d}:{sec % 60:02d}" if sec >= 3600 else f"{sec // 60:02d}:{sec % 60:02d}"


def write_transcript(case_dir, segs, meta, row):
    header = (f"# {row['title']}\n# {video_url(row['video_id'])}\n# 채널: {row['channel_title']} · 조회수 {fmt_int(row['views'])}"
              f" · 업로드 {str(row['published_at'])[:10]}\n# 대본 출처: {meta['source']} · 언어: {meta['language']}"
              f" · 자동생성: {meta['auto_generated']}\n\n")
    paras, cur, last_start = [], [], 0.0
    for s in segs:
        if cur and (s["start"] - last_start >= 45 or sum(len(x) for x in cur) > 350):
            paras.append(" ".join(cur))
            cur, last_start = [], s["start"]
        cur.append(s["text"])
    if cur:
        paras.append(" ".join(cur))
    (case_dir / "transcript.txt").write_text(header + "\n\n".join(paras) + "\n", "utf-8")
    (case_dir / "transcript_timestamped.txt").write_text(
        header + "\n".join(f"[{_mmss(s['start'])}] {s['text']}" for s in segs) + "\n", "utf-8")
    (case_dir / "transcript.json").write_text(json.dumps({"meta": meta, "segments": segs}, ensure_ascii=False, indent=1), "utf-8")


def transcript_stats(segs, duration_sec, fmt):
    text = " ".join(s["text"] for s in segs)
    chars = len(re.sub(r"\s+", "", text))
    hook_sec = 5 if fmt == "shorts" else 30
    hook = " ".join(s["text"] for s in segs if s["start"] < hook_sec)
    return {"transcript_chars": chars, "chars_per_min": round(chars / max(duration_sec / 60, 1e-9), 1) if duration_sec else None,
            "hook_seconds": hook_sec, "hook_text": hook[:400]}


# ----------------------------------------------------------------------------- 케이스 처리
def process_success_case(ctx, row, idx, comments):
    cfg = ctx.cfg
    vid = row["video_id"]
    case_dir = ctx.out_dir / "success_cases" / f"{idx:02d}_{slugify(row['title'], 30)}_{vid}"
    case_dir.mkdir(parents=True, exist_ok=True)
    tmp = ctx.work_dir / "tmp" / vid
    tmp.mkdir(parents=True, exist_ok=True)
    status = {"video_id": vid, "case_dir": case_dir.relative_to(ctx.out_dir).as_posix()}
    t0 = time.perf_counter()

    # 1) 썸네일
    r = http_get(requests.Session(), row["thumbnail_url"], "SUCCESS", retries=2) if row.get("thumbnail_url") else None
    if r is not None and r.status_code == 200:
        (case_dir / "thumbnail.jpg").write_bytes(r.content)
        status["thumbnail"] = "ok"
    else:
        status["thumbnail"] = "failed"

    # 2) 영상
    media = None
    if cfg["DOWNLOAD_VIDEOS"]:
        try:
            p = ytdlp_download(vid, case_dir, cfg)
            p, how, mb = ensure_max_size(p, cfg["VIDEO_MAX_MB"], row["duration_sec"])
            media = p
            status.update(video=how, video_file=p.name, video_mb=round(mb, 1))
        except BotCheckError as e:
            status.update(video="blocked(bot_check)", video_error=str(e)[:200])
        except Exception as e:
            status.update(video="failed", video_error=f"{type(e).__name__}: {str(e)[:200]}")
            log("SUCCESS", "영상 다운로드 실패", level="WARNING", video_id=vid, error=status["video_error"],
                next_step="yt-dlp 업데이트(pip install -U \"yt-dlp[default]\") 후 다시 실행")
    else:
        status["video"] = "skipped(DOWNLOAD_VIDEOS=False)"

    # 3) 대본: 자막 API → yt-dlp 자막 → Whisper 순서로 시도
    langs = [cfg["LANGUAGE"], "ko", "en"]
    langs = list(dict.fromkeys(l for l in langs if l))
    segs, meta, errors = None, None, {}
    for name, fn in (("api", lambda: transcript_via_api(vid, langs)),
                     ("ytdlp", lambda: transcript_via_ytdlp(vid, langs, tmp, cfg))):
        try:
            segs, meta = fn()
            break
        except Exception as e:
            errors[name] = f"{type(e).__name__}: {str(e)[:150]}"
    if segs is None and cfg["USE_WHISPER_FALLBACK"]:
        try:
            src = media
            if src is None or src.suffix.lower() not in VIDEO_EXTS:
                src = ytdlp_download(vid, tmp, cfg, audio_only=True)
            segs, meta = transcript_via_whisper(src, cfg, row["duration_sec"])
        except Exception as e:
            errors["whisper"] = f"{type(e).__name__}: {str(e)[:150]}"
    if segs:
        write_transcript(case_dir, segs, meta, row)
        status.update(transcript=meta["source"], transcript_lang=meta["language"], **transcript_stats(segs, row["duration_sec"], row["fmt"]))
    else:
        status["transcript"] = "failed"
        log("SUCCESS", "대본 확보 실패", level="WARNING", video_id=vid, errors=errors,
            next_step="봇 확인 차단이면 cookies.txt를 스크립트 폴더에 두고 다시 실행 / 자막 없는 영상은 USE_WHISPER_FALLBACK")
    if errors:
        status["transcript_errors"] = errors

    # 4) 댓글
    if comments is not None and not comments.empty:
        cm = comments[comments["video_id"] == vid]
        if not cm.empty:
            cm.sort_values("likes", ascending=False).to_csv(case_dir / "comments.csv", index=False, encoding="utf-8-sig")
            status["comments"] = len(cm)

    # 5) 메타데이터
    keep = ["video_id", "title", "channel_title", "channel_id", "published_at", "views", "likes", "comments", "subscribers",
            "duration_sec", "fmt", "outlier_score", "baseline_views", "baseline_kind", "views_per_day", "views_per_sub",
            "like_rate", "comment_rate", "case_score", "selection_reason", "tags", "description", "video_url"]
    meta_out = {k: to_jsonable(row[k]) for k in keep if k in row}
    meta_out["download_status"] = status
    (case_dir / "metadata.json").write_text(json.dumps(meta_out, ensure_ascii=False, indent=2), "utf-8")
    rmtree_force(tmp)
    status["elapsed_sec"] = round(time.perf_counter() - t0, 1)
    log("SUCCESS", f"사례 {idx:02d} 처리", video_id=vid, thumbnail=status["thumbnail"], video=status.get("video"),
        video_mb=status.get("video_mb"), transcript=status.get("transcript"), elapsed_sec=status["elapsed_sec"])
    return status


def stage6_success_cases(ctx):
    cfg, d = ctx.cfg, ctx.data
    sel = select_success_cases(d["perf"], cfg)
    d["success_cases"] = sel
    rmtree_force(ctx.out_dir / "success_cases")   # 재실행 시 이전 결과 정리
    statuses = []
    comments = d["analysis"].get("comments") if "analysis" in d else None
    for i, (_, row) in enumerate(sel.iterrows(), 1):
        try:
            statuses.append(process_success_case(ctx, row, i, comments))
        except Exception as e:      # 한 사례 실패가 전체를 멈추지 않도록
            log("SUCCESS", "사례 처리 중 예외 (건너뜀)", level="ERROR", video_id=row["video_id"], error=f"{type(e).__name__}: {e}")
            statuses.append({"video_id": row["video_id"], "error": str(e)[:200]})
    st = pd.DataFrame(statuses)
    d["success_status"], d["success_status_list"] = st, statuses
    if not st.empty:
        log("SUCCESS", "성공사례 처리 요약", cases=len(st),
            video_ok=int(st.get("video", pd.Series(dtype=str)).isin(["original", "transcoded", "remux"]).sum()),
            transcript_ok=int((st.get("transcript", pd.Series(dtype=str)).fillna("failed") != "failed").sum()),
            transcript_sources=st.get("transcript", pd.Series(dtype=str)).value_counts().to_dict())
        if (st.get("transcript", pd.Series(dtype=str)).fillna("failed") == "failed").all():
            ctx.note("SUCCESS", "모든 대본 수집 실패 — YouTube 차단(봇 확인) 또는 네트워크 문제일 수 있음",
                     hint="VPN 끄기 / cookies.txt를 스크립트 폴더에 두고 다시 실행")
    if DL_STATE["bot_total"]:
        ctx.note("SUCCESS", "YouTube 봇 확인(Sign in to confirm you're not a bot)으로 일부/전체 다운로드 차단",
                 blocked_videos=DL_STATE["bot_total"], cookies=bool(DL_STATE["cookiefile"]),
                 fix="VPN 끄기 / cookies.txt를 스크립트 폴더에 두거나 COOKIES_FROM_BROWSER 설정 후 다시 실행")
    log("SUCCESS", "yt-dlp 클라이언트 사용 현황", hits=dict(DL_STATE["client_hits"]), bot_blocked=DL_STATE["bot_total"],
        stopped=DL_STATE["disabled"])
    return st


# =====================================================================================================
# 🧰 [모듈] Stage 7 — 리포트
# =====================================================================================================
# VERSION: v2.0.0 — 2026-10-09 — PC용: 실행 환경 표기(OS), PC용 스크립트 안내 제거 (Stage 7 추천 생성 + 리포트/엑셀/CSV/run_info)
# 데이터에서 효과가 확인된 제목 요소 → 제목 템플릿 (참고용 예시. 과장·수익 보장 표현은 피하세요)
TITLE_TEMPLATES = {
    "has_number":       ["{kw} 초보가 꼭 알아야 할 {n}가지", "{kw} 핵심 {n}가지만 기억하세요"],
    "has_question":     ["{kw}, 지금 시작해도 될까?", "{kw} 왜 대부분 실패할까?"],
    "has_exclaim":      ["{kw} 이것만은 꼭 알고 시작하세요!"],
    "has_bracket":      ["[{kw}] 10분 만에 핵심 정리", "{kw} 완벽 정리 (초보 필수)"],
    "has_year":         ["{year} {kw} 총정리", "{year} 하반기 {kw} 체크리스트"],
    "has_money_or_pct": ["{kw} 100만 원으로 시작한다면?", "{kw} 수수료 0.1% 차이가 만드는 결과"],
    "has_ellipsis":     ["{kw}… 결국 이게 답이었습니다"],
    "has_quote":        ["\"{kw}\" 이렇게 하면 망합니다"],
    "hook_urgency":     ["지금 {kw} 꼭 확인해야 하는 이유", "{kw} 오늘 반드시 체크할 것"],
    "hook_fear":        ["{kw} 절대 하면 안 되는 실수 {n}가지", "{kw} 이것 모르면 손해봅니다"],
    "hook_greed":       ["{kw} 현실적으로 수익 내는 방법", "{kw} 기회는 이렇게 옵니다"],
    "hook_curiosity":   ["{kw}의 진짜 이유 (아무도 말 안 해주는 것)", "{kw} 결국 이렇게 됩니다"],
    "hook_beginner":    ["{kw} 완전 초보 가이드 — 이것만 보세요", "{kw} 기초부터 쉽게 정리"],
    "hook_list":        ["{kw} TOP {n} 순위 정리", "{kw} 추천 BEST {n}"],
    "hook_story":       ["{kw} 직접 해본 솔직 후기", "{kw} 1년 해보고 깨달은 것"],
}
DEFAULT_TEMPLATE_FEATURES = ["hook_beginner", "has_number", "has_question"]


def md_table(df, cols, headers=None, fmts=None, max_rows=None):
    """tabulate 없이 마크다운 표 생성."""
    if df is None or len(df) == 0:
        return "_데이터 없음_\n"
    headers = headers or cols
    fmts = fmts or {}
    d = df.head(max_rows) if max_rows else df
    lines = ["| " + " | ".join(headers) + " |", "|" + "---|" * len(cols)]
    for _, r in d.iterrows():
        cells = []
        for c in cols:
            v = r.get(c)
            cells.append(fmts[c](v) if c in fmts else md_escape("" if v is None or (isinstance(v, float) and not np.isfinite(v)) else v))
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines) + "\n"


def link(title, vid, n=45):
    t = md_escape(str(title))
    return f"[{t[:n]}{'…' if len(t) > n else ''}]({video_url(vid)})"


def pick_template_features(tf):
    if tf is None or tf.empty:
        return DEFAULT_TEMPLATE_FEATURES, "기본값(데이터 부족)"
    t = tf[(tf["segment"] == "전체") & (tf["lift"] >= 1.1) & tf["feature"].isin(TITLE_TEMPLATES)]
    t = t.sort_values(["significant", "lift"], ascending=False)
    feats = list(t["feature"].head(4))
    if len(feats) < 2:
        feats += [f for f in DEFAULT_TEMPLATE_FEATURES if f not in feats][: 3 - len(feats)]
        return feats, "데이터 기반 + 기본값 보충"
    return feats, "데이터 기반 (lift≥1.1)"


def build_recommendations(ctx):
    d = ctx.data
    res = d["analysis"]
    year = ctx.started_at.astimezone(KST).year
    feats, feat_src = pick_template_features(res["title_features"])
    fmt_tbl = res["format"].set_index("fmt") if not res["format"].empty else pd.DataFrame()
    rel_fmt = fmt_tbl[fmt_tbl["reliable"]] if not fmt_tbl.empty else fmt_tbl
    overall_best_fmt = rel_fmt["median_outlier"].idxmax() if len(rel_fmt) else "long"
    dur = res["duration"]
    dur_rel = dur[dur["reliable"]] if not dur.empty else dur
    best_dur = (dur_rel.sort_values(["success_rate", "median_outlier"], ascending=False)["duration_bucket"].astype(str).head(2).tolist()
                if len(dur_rel) else [])
    v = d["videos"].set_index("video_id")
    recs, used = [], set()
    for i, r in enumerate(res["keywords"].dropna(subset=["opportunity"]).head(8).itertuples()):
        kw = r.keyword
        n = [3, 5, 7][i % 3]
        titles = [TITLE_TEMPLATES[f][(i + j) % len(TITLE_TEMPLATES[f])].format(kw=kw, n=n, year=year)
                  for j, f in enumerate(feats[(i % len(feats)):] + feats[:(i % len(feats))])][:3]
        fmt = r.best_format or overall_best_fmt
        # 참고 영상: 다른 아이디어와 겹치지 않게 2개 + 소규모 채널 성공 예시 1개(있으면)
        refs = [vid for vid in r.example_ids if vid in v.index and vid not in used][:2]
        small = [vid for vid in r.small_example_ids if vid in v.index and vid not in used and vid not in refs][:1]
        refs = refs + small if small else [vid for vid in r.example_ids if vid in v.index and vid not in used][:3]
        used.update(refs)
        recs.append({"rank": i + 1, "keyword": kw, "opportunity": r.opportunity, "format": fmt, "durations": best_dur,
                     "titles": titles, "refs": refs, "demand_vpd": r.demand_vpd, "small_win_share": r.small_win_share,
                     "fresh_share": r.fresh_share, "competition_subs": r.competition_subs, "median_outlier": r.median_outlier,
                     "n_success": r.n_success, "shorts_share_serp": r.shorts_share_serp})
    log("REPORT", "추천 아이디어 생성", n=len(recs), template_features=feats, source=feat_src, best_format=overall_best_fmt, best_durations=best_dur)
    return recs, feats, feat_src, overall_best_fmt, best_dur


def build_upload_plan(recs, best_fmt):
    plan = []
    for r in recs:
        plan.append({"형식": "롱폼" if r["format"] != "shorts" else "쇼츠", "키워드": r["keyword"], "제목 예시": r["titles"][0],
                     "근거": f"기회점수 {r['opportunity']:.0f}"})
        plan.append({"형식": "쇼츠" if r["format"] != "shorts" else "롱폼", "키워드": r["keyword"],
                     "제목 예시": r["titles"][1] if len(r["titles"]) > 1 else r["titles"][0],
                     "근거": "같은 키워드를 다른 포맷으로 재활용 (제작비↓, 검색·쇼츠 피드 동시 공략)"})
    return plan[:10]


def _df_for_excel(df):
    df = df.copy()
    for c in df.columns:
        if isinstance(df[c].dtype, pd.DatetimeTZDtype):
            df[c] = df[c].dt.tz_convert("Asia/Seoul").dt.tz_localize(None)
        elif df[c].dtype == object or str(df[c].dtype) in ("string", "str"):
            df[c] = df[c].map(lambda x: ", ".join(map(str, x)) if isinstance(x, (list, tuple, np.ndarray))
                              else (re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", x)[:3000] if isinstance(x, str) else x))
        elif isinstance(df[c].dtype, pd.CategoricalDtype):
            df[c] = df[c].astype(str)
    return df


def write_tables(ctx):
    d, res = ctx.data, ctx.data["analysis"]
    data_dir = ctx.out_dir / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    vcols = ["video_id", "title", "channel_title", "channel_id", "published_at", "fmt", "duration_sec", "views", "likes", "comments",
             "subscribers", "channel_size", "age_days", "views_per_day", "views_per_sub", "outlier_score", "baseline_views",
             "baseline_kind", "is_success", "is_small_channel", "is_mature", "in_window", "like_rate", "comment_rate",
             "weekday_label", "publish_hour", "title_len", "uploads_per_week", "tags", "video_url"]
    tables = {
        "videos": d["videos"][[c for c in vcols if c in d["videos"].columns]].sort_values("outlier_score", ascending=False),
        "keyword_opportunity": res["keywords"],
        "autocomplete_keywords": d["keywords_ac"],
        "title_features": res["title_features"],
        "title_tokens": res["tokens"],
        "title_length": res["title_length"],
        "format": res["format"],
        "duration": res["duration"],
        "weekday": res["weekday"],
        "hour": res["hour"],
        "channel_size": res["channel_size"],
        "clusters": res["clusters"],
        "tags": res["tags"],
        "correlations": res["correlations"],
        "recent_hot": res["recent_hot"][[c for c in vcols if c in res["recent_hot"].columns]],
        "new_channel_wins": res["new_channel_wins"][[c for c in vcols if c in res["new_channel_wins"].columns]],
        "success_cases": d.get("success_cases", pd.DataFrame()).drop(columns=["description"], errors="ignore"),
        "success_download_status": d.get("success_status", pd.DataFrame()),
        "audience_comments": res["comments"],
        "question_terms": res["question_terms"],
        "search_results": d["search_df"],
    }
    for name, t in tables.items():
        if t is not None and len(t):
            _df_for_excel(t).to_csv(data_dir / f"{name}.csv", index=False, encoding="utf-8-sig")
    try:
        with pd.ExcelWriter(ctx.out_dir / "analysis.xlsx", engine="openpyxl") as xw:
            for name, t in tables.items():
                if t is not None and len(t):
                    _df_for_excel(t).head(100_000).to_excel(xw, sheet_name=name[:31], index=False)
        log("REPORT", "엑셀 저장", file="analysis.xlsx", sheets=[n for n, t in tables.items() if t is not None and len(t)])
    except Exception as e:
        log("REPORT", "엑셀 저장 실패 (CSV는 저장됨)", level="WARNING", error=f"{type(e).__name__}: {e}")
    log("REPORT", "CSV 저장", dir="data/", files=len(list(data_dir.glob("*.csv"))))


def write_report(ctx):
    cfg, d = ctx.cfg, ctx.data
    res, perf, v = d["analysis"], d["perf"], d["videos"]
    charts = d.get("charts", {})
    recs, feats, feat_src, best_fmt, best_dur = build_recommendations(ctx)
    plan = build_upload_plan(recs, best_fmt)
    d["recommendations"] = recs
    topic = cfg["TOPIC"]
    now_kst = dt.datetime.now(KST).strftime("%Y-%m-%d %H:%M")
    fmt_name = {"long": "롱폼", "shorts": "쇼츠", "live": "라이브"}
    yt_sum = ctx.yt.summary() if ctx.yt else {}
    vv = v.set_index("video_id")

    def img(name, alt):
        return f"![{alt}]({charts[name]})\n" if name in charts else ""

    L = []
    L.append(f"# 📊 YouTube '{topic}' 주제 분석 리포트\n")
    L.append(f"> 생성 {now_kst} KST · 노트북 {NOTEBOOK_VERSION} · 실행ID `{ctx.run_id}` · 지역 {cfg['REGION_CODE']} / 언어 {cfg['LANGUAGE']}  \n"
             f"> ⚠️ 연구·교육용 분석 결과입니다. **투자 조언이 아니며**, 통계는 상관관계일 뿐 인과관계를 보장하지 않습니다.\n")

    # ---- 0. 요약
    small_sr = perf.loc[perf["is_small_channel"], "is_success"].mean()
    big_sr = perf.loc[perf["is_big_channel"], "is_success"].mean()
    ft = res["format"].set_index("fmt") if not res["format"].empty else pd.DataFrame()
    L.append("## 0. 한눈에 보기 (TL;DR)\n")
    L.append(f"- **분석 데이터**: 영상 {len(v):,}개 수집 → 성과 분석 {len(perf):,}개 "
             f"(업로드 {str(perf['published_at'].min())[:10]} ~ {str(perf['published_at'].max())[:10]}, 업로드 후 {cfg['MATURE_AGE_DAYS']}일 이상 경과), "
             f"채널 {v['channel_id'].nunique():,}개, 검색 키워드 {d['search_df']['keyword'].nunique()}개, 자동완성 검색어 {len(d['keywords_ac']):,}개")
    L.append(f"- **성공(아웃라이어) 기준**: 조회수 {fmt_int(cfg['MIN_SUCCESS_VIEWS'])}회 이상 **그리고** 같은 채널 최근 영상 중앙값의 {cfg['OUTLIER_MIN']:.0f}배 이상 "
             f"→ {int(perf['is_success'].sum()):,}개 ({fmt_pct(perf['is_success'].mean())})")
    if recs:
        L.append("- 🎯 **기회가 가장 큰 키워드**: " + ", ".join(f"`{r['keyword']}`({r['opportunity']:.0f}점)" for r in recs[:5]))
    if len(ft):
        L.append("- 🎬 **포맷별 성공 비율**: " + " · ".join(f"{fmt_name.get(i, i)} {fmt_pct(r.success_rate)} (배수 중앙값 {fmt_num(r.median_outlier, 2)}배, n={r.n})"
                                                     for i, r in ft.iterrows()) + f" → 추천: **{fmt_name.get(best_fmt, best_fmt)}** 중심")
    if best_dur:
        L.append(f"- ⏱️ **롱폼 추천 길이**: {', '.join(best_dur)} (성공 비율 상위 구간)")
    tf = res["title_features"]
    if not tf.empty:
        pos = tf[(tf["segment"] == "전체") & (tf["lift"] > 1)].head(4)
        neg = tf[(tf["segment"] == "전체") & (tf["lift"] < 1)].sort_values("lift").head(3)
        L.append("- 🏷️ **효과 있는 제목 요소**: " + (", ".join(f"{r.label} {r.lift:.2f}배{'*' if r.significant else ''}" for r in pos.itertuples()) or "뚜렷한 요소 없음")
                 + ("  /  역효과: " + ", ".join(f"{r.label} {r.lift:.2f}배" for r in neg.itertuples()) if len(neg) else "") + "  (*=다중비교 보정 후 유의, q<0.05)")
    L.append(f"- 🌱 **작은 채널도 터지나?**: 소규모(<{fmt_compact(cfg['SMALL_CHANNEL_MAX_SUBS'])}) 채널 영상의 성공 비율 {fmt_pct(small_sr)} "
             f"vs 대형(≥{fmt_compact(cfg['BIG_CHANNEL_MIN_SUBS'])}) {fmt_pct(big_sr)}. "
             + (f"성공한 소규모 채널의 업로드 빈도 중앙값: 주 {fmt_num(res['small_channel_upload_freq'], 1)}회"
                if np.isfinite(res["small_channel_upload_freq"]) else "이번 데이터에는 소규모 채널 성공 사례가 없습니다 → 롱테일 키워드/쇼츠로 진입 전략 필요"))
    if not res["weekday"].empty:
        w = res["weekday"][res["weekday"]["reliable"]].sort_values("success_rate", ascending=False).head(2)
        h = res["hour"][res["hour"]["reliable"]].sort_values("success_rate", ascending=False).head(2)
        L.append(f"- 🕒 **업로드 타이밍(참고)**: 성공 비율 높은 요일 {', '.join(w['weekday_label'].astype(str))} / 시간대 {', '.join(h['hour_bucket'].astype(str))} (KST)")
    L.append(f"- 💸 **API 쿼터 사용**: {yt_sum.get('quota_used', 0):,} / 예산 {yt_sum.get('quota_budget', 0):,} (일일 한도 10,000)\n")

    # ---- 1. 추천 아이디어
    L.append("## 1. 🎬 추천 영상 아이디어 (데이터 기반)\n")
    L.append(f"제목 예시는 이번 데이터에서 효과가 확인된 제목 요소({', '.join(FEATURE_LABELS.get(f, f) for f in feats)}; {feat_src})를 조합한 **템플릿 예시**입니다. "
             "그대로 쓰기보다 참고 영상의 실제 제목·썸네일·도입부(대본)를 함께 보고 다듬으세요.\n")
    for r in recs:
        L.append(f"### {r['rank']}. `{md_escape(r['keyword'])}` — 기회점수 **{r['opportunity']:.0f}**/100\n")
        L.append(f"- 근거: 검색 상위 {cfg['SERP_TOP_N']}개 영상 일평균 조회수 중앙값 **{fmt_compact(r['demand_vpd'])}회**, "
                 f"소규모 채널 진입 성공 비율 **{fmt_pct(r['small_win_share'])}**, 최근 {cfg['FRESH_DAYS']}일 영상 비율 {fmt_pct(r['fresh_share'])}, "
                 f"경쟁 채널 구독자 중앙값 {fmt_compact(r['competition_subs'])}명, 아웃라이어 배수 중앙값 {fmt_num(r['median_outlier'], 2)}배, 성공 영상 {r['n_success']}개")
        L.append(f"- 추천 포맷: **{fmt_name.get(r['format'], r['format'])}**" + (f" · 롱폼이면 {', '.join(r['durations'])}" if r['durations'] and r['format'] != 'shorts' else "")
                 + f" · 검색 상위 중 쇼츠 비율 {fmt_pct(r['shorts_share_serp'])}")
        L.append("- 제목 예시: " + " / ".join(f"「{t}」" for t in r["titles"]))
        if r["refs"]:
            L.append("- 참고할 성공 영상:")
            for vid in r["refs"]:
                x = vv.loc[vid]
                L.append(f"  - {link(x['title'], vid)} — 조회수 {fmt_compact(x['views'])}, 구독자 {fmt_compact(x['subscribers'])}, "
                         f"채널 평균의 {fmt_num(x['outlier_score'], 1)}배, {fmt_name.get(x['fmt'], x['fmt'])}")
        L.append("")
    if plan:
        L.append("### 🗓️ 첫 10개 영상 업로드 플랜 (제안)\n")
        L.append(md_table(pd.DataFrame(plan).reset_index().assign(index=lambda x: x["index"] + 1),
                          ["index", "형식", "키워드", "제목 예시", "근거"], ["#", "형식", "키워드", "제목 예시", "근거"]))
    cl = res["clusters"]
    if cl is not None and not cl.empty:
        L.append("### 🧩 하위 주제(제목 클러스터)별 기회\n")
        L.append(img("10_subtopic_clusters.png", "클러스터"))
        L.append(md_table(cl, ["cluster_opportunity", "top_terms", "n", "median_outlier", "success_rate", "small_success_rate", "shorts_share", "example_titles"],
                          ["기회점수", "핵심 단어", "영상 수", "배수 중앙값", "성공 비율", "소규모채널 성공", "쇼츠 비율", "예시 제목"],
                          {"cluster_opportunity": lambda x: fmt_num(x, 0), "n": fmt_int, "median_outlier": lambda x: fmt_num(x, 2),
                           "success_rate": fmt_pct, "small_success_rate": fmt_pct, "shorts_share": fmt_pct,
                           "example_titles": lambda x: md_escape(x)[:90]}, 12))

    # ---- 2. 키워드
    L.append("## 2. 🔑 키워드 기회 분석\n")
    L.append("기회점수 = 수요 25% + 자동완성 15% + 소규모채널 진입 20% + 아웃라이어 15% + 신선도 10% + 경쟁(역) 15% (키워드 간 백분위 기준). "
             "검색 상위 10개 중 절반 이상이 한 채널인 키워드(채널명 검색)는 제외했습니다.\n")
    L.append(img("01_keyword_opportunity.png", "키워드 기회점수") + img("02_demand_vs_competition.png", "수요 vs 경쟁"))
    L.append(md_table(res["keywords"], ["keyword", "opportunity", "demand_vpd", "ac_score", "small_win_share", "fresh_share", "competition_subs", "median_outlier", "n_success", "best_format", "navigational"],
                      ["키워드", "기회점수", "일평균 조회수(중앙)", "자동완성", "소규모 진입", "최신 비율", "경쟁 구독자(중앙)", "배수(중앙)", "성공 수", "추천 포맷", "채널명검색"],
                      {"opportunity": lambda x: fmt_num(x, 0), "demand_vpd": fmt_compact, "ac_score": lambda x: fmt_num(x, 2),
                       "small_win_share": fmt_pct, "fresh_share": fmt_pct, "competition_subs": fmt_compact,
                       "median_outlier": lambda x: fmt_num(x, 2), "n_success": fmt_int,
                       "best_format": lambda x: fmt_name.get(x, "-") if isinstance(x, str) else "-",
                       "navigational": lambda x: "예" if x else ""}, 30))
    L.append("<details><summary>자동완성 상위 검색어 50개 (실제 사람들이 검색하는 말)</summary>\n\n" +
             md_table(d["keywords_ac"], ["ac_rank", "keyword", "ac_score", "ac_hits"], ["순위", "검색어", "점수", "등장 질의 수"],
                      {"ac_score": lambda x: fmt_num(x, 2), "ac_hits": fmt_int}, 50) + "\n</details>\n")

    # ---- 3. 제목
    L.append("## 3. 🏷️ 제목 패턴 분석\n")
    L.append(img("06_title_feature_lift.png", "제목 요소 효과") + img("09_success_tokens.png", "성공 단어") + img("11_title_length.png", "제목 길이"))
    if not tf.empty:
        L.append(md_table(tf[tf["segment"] == "전체"], ["label", "n_with", "median_outlier_with", "median_outlier_without", "lift", "success_rate_with", "success_rate_without", "p_value", "q_value"],
                          ["제목 요소", "해당 영상 수", "배수(있음)", "배수(없음)", "효과(배)", "성공률(있음)", "성공률(없음)", "p값", "q값(보정)"],
                          {"n_with": fmt_int, "median_outlier_with": lambda x: fmt_num(x, 2), "median_outlier_without": lambda x: fmt_num(x, 2),
                           "lift": lambda x: fmt_num(x, 2), "success_rate_with": fmt_pct, "success_rate_without": fmt_pct, "p_value": lambda x: fmt_num(x, 3),
                           "q_value": lambda x: fmt_num(x, 3)}))
        L.append("<details><summary>롱폼/쇼츠 따로 본 제목 요소 효과</summary>\n\n" +
                 md_table(tf[tf["segment"] != "전체"], ["segment", "label", "n_with", "lift", "success_rate_with", "p_value"],
                          ["구분", "제목 요소", "영상 수", "효과(배)", "성공률(있음)", "p값"],
                          {"n_with": fmt_int, "lift": lambda x: fmt_num(x, 2), "success_rate_with": fmt_pct, "p_value": lambda x: fmt_num(x, 3)}) + "\n</details>\n")
    if res["tokens"] is not None and not res["tokens"].empty:
        L.append("**성공 영상 제목에 유독 많이 나오는 단어** (과대표집 배수 = 성공 영상 내 비중 ÷ 전체 비중)\n")
        L.append(md_table(res["tokens"], ["token", "n", "success_n", "success_overrep", "median_outlier", "median_vpd"],
                          ["단어", "영상 수", "성공 수", "과대표집", "배수(중앙)", "일평균 조회수"],
                          {"n": fmt_int, "success_n": fmt_int, "success_overrep": lambda x: fmt_num(x, 2),
                           "median_outlier": lambda x: fmt_num(x, 2), "median_vpd": fmt_compact}, 25))

    # ---- 4. 포맷/길이
    L.append("## 4. 🎞️ 포맷 · 길이\n")
    L.append("> 쇼츠 조회수는 2025년 3월부터 '재생 시작/반복'마다 집계되어 롱폼 조회수와 직접 비교할 수 없습니다. "
             "그래서 **같은 채널·같은 포맷 대비 배수(아웃라이어)** 와 성공 비율로 비교합니다.\n")
    L.append(img("04_format_performance.png", "포맷") + img("05_duration_performance.png", "길이"))
    perf_fmts = {"n": fmt_int, "median_views": fmt_compact, "median_vpd": fmt_compact, "median_outlier": lambda x: fmt_num(x, 2),
                 "success_rate": fmt_pct, "small_success_rate": fmt_pct}
    perf_cols = ["n", "median_views", "median_vpd", "median_outlier", "success_rate", "small_success_rate"]
    perf_hdr = ["영상 수", "조회수(중앙)", "일평균(중앙)", "배수(중앙)", "성공 비율", "소규모채널 성공"]
    L.append(md_table(res["format"].assign(fmt=lambda x: x["fmt"].map(lambda f: fmt_name.get(f, f))), ["fmt"] + perf_cols, ["포맷"] + perf_hdr, perf_fmts))
    L.append(md_table(res["duration"], ["duration_bucket"] + perf_cols, ["롱폼 길이"] + perf_hdr, perf_fmts))

    # ---- 5. 타이밍
    L.append("## 5. 🕒 업로드 타이밍 (참고용 — 효과가 작고 혼란변수가 많음)\n")
    L.append(img("07_publish_timing_heatmap.png", "타이밍"))
    L.append(md_table(res["weekday"].set_index("weekday_label").reindex(WEEKDAY_LABELS).dropna(subset=["n"]).reset_index(),
                      ["weekday_label"] + perf_cols, ["요일"] + perf_hdr, perf_fmts))
    L.append(md_table(res["hour"], ["hour_bucket"] + perf_cols, ["시간대(KST)"] + perf_hdr, perf_fmts))

    # ---- 6. 채널 규모
    L.append("## 6. 🌱 채널 규모별 분석 — 0명 채널에게 가장 중요한 부분\n")
    L.append(img("08_channel_size_performance.png", "채널 규모") + img("03_views_vs_subscribers.png", "구독자 대비 조회수"))
    L.append(md_table(res["channel_size"], ["channel_size"] + perf_cols, ["구독자 규모"] + perf_hdr, perf_fmts))
    nw = res["new_channel_wins"]
    L.append(f"**개설 1년 이내 채널의 성공 영상** ({len(nw)}개) — 신생 채널이 실제로 터진 사례\n")
    L.append(md_table(nw.assign(t=[link(t, i) for t, i in zip(nw["title"], nw["video_id"])]) if len(nw) else nw,
                      ["t", "channel_title", "subscribers", "views", "outlier_score", "fmt", "channel_age_days"],
                      ["영상", "채널", "구독자", "조회수", "배수", "포맷", "채널 나이(일)"],
                      {"t": lambda x: x, "subscribers": fmt_compact, "views": fmt_compact, "outlier_score": lambda x: fmt_num(x, 1),
                       "fmt": lambda x: fmt_name.get(x, x), "channel_age_days": fmt_int}, 15))

    # ---- 7. 최근 급상승
    rh = res["recent_hot"]
    L.append(f"## 7. 🔥 최근 {cfg['MATURE_AGE_DAYS']}일 이내 급상승 영상 (아직 성과 집계 전 — 트렌드 참고)\n")
    L.append(md_table(rh.assign(t=[link(t, i) for t, i in zip(rh["title"], rh["video_id"])]) if len(rh) else rh,
                      ["t", "channel_title", "subscribers", "views", "views_per_day", "age_days", "fmt"],
                      ["영상", "채널", "구독자", "조회수", "일평균", "경과일", "포맷"],
                      {"t": lambda x: x, "subscribers": fmt_compact, "views": fmt_compact, "views_per_day": fmt_compact,
                       "age_days": lambda x: fmt_num(x, 1), "fmt": lambda x: fmt_name.get(x, x)}, 15))

    # ---- 8. 성공사례
    sc = d.get("success_cases", pd.DataFrame())
    st_map = {s["video_id"]: s for s in d.get("success_status_list", [])}
    L.append("## 8. 🏆 성공사례 — 대본 · 영상 · 썸네일\n")
    L.append(f"선정 기준: 종합점수(아웃라이어 40% + 조회수 35% + 구독자 대비 조회수 25%) 상위, 소규모 채널 ≥{cfg['SUCCESS_SMALL_CHANNEL_SHARE']:.0%}, "
             f"롱폼 ≥{cfg['SUCCESS_LONGFORM_SHARE']:.0%}, 채널당 최대 {cfg['MAX_CASES_PER_CHANNEL']}개. 각 폴더에 `transcript.txt`(대본), "
             "`transcript_timestamped.txt`, `video.mp4`, `thumbnail.jpg`, `metadata.json`, `comments.csv` 가 있습니다.\n")
    if len(sc):
        for i, r in enumerate(sc.itertuples(), 1):
            s = st_map.get(r.video_id, {})
            folder = s.get("case_dir", "")
            L.append(f"### {i}. {link(r.title, r.video_id, 70)}\n")
            L.append(f"- 채널 **{md_escape(r.channel_title)}** (구독자 {fmt_compact(r.subscribers)}) · 조회수 **{fmt_compact(r.views)}** · "
                     f"채널 평균의 **{fmt_num(r.outlier_score, 1)}배** · {fmt_name.get(r.fmt, r.fmt)} {_mmss(r.duration_sec or 0)} · "
                     f"업로드 {str(r.published_at)[:10]} · 선정: {r.selection_reason} (점수 {r.case_score:.0f})")
            if folder:
                thumb = f"{folder}/thumbnail.jpg"
                L.append(f"- 📁 [`{folder}/`]({folder}/) · 대본: {s.get('transcript', '-')} · 영상: {s.get('video', '-')}"
                         + (f" ({s.get('video_mb')}MB)" if s.get('video_mb') else "")
                         + (f" · 말 속도 {s.get('chars_per_min')}자/분" if s.get('chars_per_min') else ""))
                if s.get("thumbnail") == "ok":
                    L.append(f"\n  <img src=\"{thumb}\" width=\"320\">\n")
            if s.get("hook_text"):
                L.append(f"- 🎣 **첫 {s.get('hook_seconds')}초 도입부**: \"{md_escape(s['hook_text'][:300])}\"")
            L.append("")
    else:
        L.append("_선정된 성공사례가 없습니다 (기준을 낮추거나 데이터 범위를 넓혀보세요)._\n")

    # ---- 9. 시청자 질문
    cm = res["comments"]
    L.append("## 9. 💬 시청자 질문 (성공 영상 댓글에서 추출) — 다음 영상 주제 후보\n")
    if cm is not None and not cm.empty and cm["is_question"].any():
        q = cm[cm["is_question"]].sort_values("likes", ascending=False).head(20).copy()
        q["comment"] = q["comment"].str.replace(r"\s+", " ", regex=True).str[:140]
        q["src"] = [link(vv.loc[x, "title"] if x in vv.index else x, x, 25) for x in q["video_id"]]
        L.append("질문 댓글에 많이 나오는 단어: " + ", ".join(f"`{t}`({c})" for t, c in res["question_terms"].head(20).itertuples(index=False)) + "\n")
        L.append(md_table(q, ["comment", "likes", "src"], ["질문 댓글", "좋아요", "영상"], {"likes": fmt_int, "src": lambda x: x}))
    else:
        L.append("_수집된 질문 댓글이 없습니다._\n")

    # ---- 10. 태그 / 상관
    if res["tags"] is not None and not res["tags"].empty:
        L.append("## 10. 🔖 태그 분석 (성공 영상에서 과대표집된 태그)\n")
        L.append(md_table(res["tags"], ["tag", "n", "success_n", "success_overrep", "median_outlier"], ["태그", "영상 수", "성공 수", "과대표집", "배수(중앙)"],
                          {"n": fmt_int, "success_n": fmt_int, "success_overrep": lambda x: fmt_num(x, 2), "median_outlier": lambda x: fmt_num(x, 2)}, 20))
    L.append("**아웃라이어 배수와의 순위상관(스피어만)** — 절댓값 0.1 미만은 사실상 무관\n")
    L.append(md_table(res["correlations"], ["index", "spearman_vs_log_outlier"], ["지표", "상관계수"], {"spearman_vs_log_outlier": lambda x: fmt_num(x, 3)}))

    # ---- 11. 체크리스트
    L.append("## 11. ✅ 0명 채널 실행 체크리스트\n")
    L.append("1. **검색형 키워드로 시작**: 위 기회점수 상위 키워드는 '검색 → 유입'이 가능한 주제입니다. 구독자가 없을 때는 추천 피드보다 검색 유입이 먼저 열립니다.")
    L.append("2. **제목 = 검색어 + 검증된 제목 요소**: 키워드를 제목 앞쪽에 넣고, 3장의 효과 요소를 1~2개만 조합하세요 (과장은 시청 지속률을 떨어뜨립니다).")
    L.append("3. **첫 30초(쇼츠는 첫 3~5초)**: 8장 성공사례의 '도입부'를 비교해 공통 구조(질문 제기 → 결론 예고 → 근거)를 따라 해보세요.")
    L.append("4. **롱폼 1개 → 쇼츠 2~3개 재가공**: 같은 주제를 두 포맷으로 내보내 제작 효율과 노출 채널을 동시에 늘립니다.")
    freq = res["small_channel_upload_freq"]
    L.append("5. **업로드 빈도**: " + (f"성공한 소규모 채널의 업로드 빈도 중앙값은 주 {fmt_num(freq, 1)}회입니다. " if np.isfinite(freq) else "")
             + "꾸준함이 우선입니다 (최소 주 1~2회 롱폼 + 쇼츠).")
    L.append("6. **댓글 질문을 다음 영상으로**: 9장의 질문이 바로 수요가 검증된 다음 주제입니다.")
    L.append("7. **주식/금융 주제 주의**: 특정 종목 매수·매도 권유, 수익 보장 표현은 피하고 '투자 권유 아님' 고지를 넣으세요. "
             "유료 리딩방·1:1 종목 추천처럼 대가를 받고 투자 판단을 조언하면 자본시장법상 유사투자자문업 신고 대상이 될 수 있습니다 (사업화 전 확인 필요).")
    L.append("8. **2~4주마다 재분석**: 트렌드는 빠르게 바뀝니다. 이 노트북을 다시 실행해 키워드 순위 변화를 확인하세요.\n")

    # ---- 12. 방법론
    L.append("## 12. 📐 방법론 · 한계 · 재현 정보\n")
    L.append(f"- **아웃라이어 배수** = 영상 조회수 ÷ 같은 채널 최근 업로드 {cfg['BASELINE_UPLOADS']}개(업로드 {cfg['MATURE_AGE_DAYS']}일 이상 경과, 같은 포맷 우선, 해당 영상 제외)의 조회수 중앙값. "
             "구독자 수와 무관하게 '주제·제목·썸네일의 힘'을 보는 지표입니다.")
    L.append(f"- **분석 분할**: 성과 분석은 업로드 후 {cfg['MATURE_AGE_DAYS']}일 이상 ~ {cfg['ANALYSIS_DAYS']}일 이내 영상만 사용 "
             f"({str(perf['published_at'].min())[:10]} ~ {str(perf['published_at'].max())[:10]}). 그보다 최근 영상은 7장(급상승)에서만 참고.")
    L.append("- **미래 정보 누수 방지**: 모든 지표는 수집 시점에 관측 가능한 값만 사용하며, 기준선에서 대상 영상 자신을 제외했습니다.")
    L.append("- **한계**: ① search.list 결과는 YouTube가 고른 표본이며 개인화되지 않은 결과입니다. ② 오래된 영상일수록 조회수가 누적되어 배수가 커질 수 있습니다 "
             "(채널 최근 업로드가 짧은 기간에 몰린 경우). ③ 썸네일·시청 지속률·CTR 등 핵심 내부 지표는 API로 볼 수 없습니다. "
             "④ 제목 요소 효과는 상관관계이며 주제·채널 특성과 섞여 있습니다. ⑤ 쇼츠 판별은 길이 + youtube.com/shorts 응답으로 추정합니다.")
    L.append(f"- **재현성**: 랜덤 시드 {cfg['RANDOM_SEED']}, 캐시 TTL {cfg['CACHE_TTL_HOURS']}시간, API 호출 {yt_sum.get('calls', {})}, 캐시 적중 {yt_sum.get('cache_hits', {})}")
    L.append("- **저작권**: 성공사례 대본·영상은 개인 학습·분석용입니다. 재업로드·재배포하지 마세요. 공개 저장소에는 영상 파일을 올리지 않는 것이 기본값입니다.")
    if ctx.notes:
        L.append("\n**이번 실행의 경고/주의 사항**\n")
        L += [f"- {md_escape(n)}" for n in ctx.notes]
    L.append("\n## 13. 📁 파일 목록\n")
    L.append("- `README.md` (이 리포트) · `analysis.xlsx` (모든 표) · `data/*.csv` · `charts/*.png` · `success_cases/` · `run_info.json` · `run_log.txt`")
    (ctx.out_dir / "README.md").write_text("\n".join(L) + "\n", "utf-8")
    log("REPORT", "리포트 저장", file="README.md", lines=len(L), recommendations=len(recs))


def write_run_info(ctx):
    d = ctx.data
    perf = d.get("perf", pd.DataFrame())
    info = {
        "notebook_version": NOTEBOOK_VERSION, "run_id": ctx.run_id, "started_at_utc": ctx.started_at.isoformat(),
        "finished_at_utc": dt.datetime.now(UTC).isoformat(), "config": ctx.cfg,
        "youtube_api": ctx.yt.summary() if ctx.yt else None,
        "cache": {"hits": dict(ctx.cache.hits), "misses": dict(ctx.cache.misses)},
        "timings_sec": ctx.timings, "notes": ctx.notes,
        "data_ranges": {
            "videos_total": int(len(d.get("videos", []))), "perf_videos": int(len(perf)),
            "perf_published_min": str(perf["published_at"].min()) if len(perf) else None,
            "perf_published_max": str(perf["published_at"].max()) if len(perf) else None,
            "collected_at": str(d.get("collected_at")),
        },
        "scoring": {"keyword_weights": KEYWORD_SCORE_WEIGHTS, "success_case_weights": SUCCESS_SCORE_WEIGHTS},
        "environment": {"python": sys.version.split()[0], "pandas": pd.__version__, "numpy": np.__version__, "os": platform.platform()},
        "disclaimer": "연구·교육용 분석 결과이며 투자 조언이 아닙니다.",
    }
    (ctx.out_dir / "run_info.json").write_text(json.dumps(to_jsonable(info), ensure_ascii=False, indent=2), "utf-8")
    log("REPORT", "run_info.json 저장")


def stage7_report(ctx):
    write_tables(ctx)
    write_report(ctx)
    write_run_info(ctx)
    files = [p for p in ctx.out_dir.rglob("*") if p.is_file()]
    log("REPORT", "출력 요약", files=len(files), total_mb=round(sum(p.stat().st_size for p in files) / 1e6, 1), out_dir=str(ctx.out_dir))


# =====================================================================================================
# 🧰 [모듈] Stage 8 — GitHub 푸시 + 결과 정리
# =====================================================================================================
# VERSION: v2.0.0 — 2026-10-09 — PC용: git 미설치 감지, Windows 긴 경로/인코딩/자격증명 팝업 방지, Kaggle 출력 → 결과 폴더 열기 (Stage 8)
GITHUB_MAX_FILE_MB = 95      # GitHub는 100MB 초과 파일을 거부


def github_api(path, token, method="GET", **kw):
    r = requests.request(method, f"https://api.github.com{path}", timeout=30,
                         headers={"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json",
                                  "X-GitHub-Api-Version": "2022-11-28"}, **kw)
    return r


def run_git(args, cwd, auth_b64=None, check=True, timeout=900):
    # core.longpaths: Windows 260자 경로 제한 회피 / quotepath: 한글 파일명 그대로 / credential.helper 비움: 로그인 팝업 방지
    cmd = ["git", "-c", "core.longpaths=true", "-c", "core.quotepath=false", "-c", "credential.helper="]
    if auth_b64:   # 토큰을 URL/설정 파일에 남기지 않고 요청 헤더로만 전달
        cmd += ["-c", f"http.https://github.com/.extraheader=AUTHORIZATION: basic {auth_b64}"]
    cmd += args
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=timeout,
                       env={**os.environ, "GIT_TERMINAL_PROMPT": "0", "GCM_INTERACTIVE": "never"})
    out = mask_secrets((r.stdout or "") + (r.stderr or ""))
    if check and r.returncode != 0:
        raise RuntimeError(f"git {args[0]} 실패 (code={r.returncode}): {out[-800:]}")
    return r.returncode, out


def _copy_results(ctx, target, allow_videos):
    """로컬 결과 → 저장소 경로 복사. 영상 정책/용량 제한으로 제외된 파일 목록 반환."""
    skipped = []
    for src in ctx.out_dir.rglob("*"):
        if not src.is_file():
            continue
        rel = src.relative_to(ctx.out_dir)
        mb = src.stat().st_size / 1e6
        if src.suffix.lower() in VIDEO_EXTS and not allow_videos:
            skipped.append((rel.as_posix(), round(mb, 1), "public_repo_video_policy"))
            continue
        if mb > GITHUB_MAX_FILE_MB:
            skipped.append((rel.as_posix(), round(mb, 1), "over_100MB_limit"))
            continue
        dst = target / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
    for rel, mb, why in skipped:   # 빠진 영상 자리에 안내 파일
        note = (target / rel).parent / "VIDEO_NOT_IN_GITHUB.txt"
        note.parent.mkdir(parents=True, exist_ok=True)
        note.write_text(f"{Path(rel).name} ({mb}MB) 은 GitHub에 올리지 않았습니다. 사유: {why}\n"
                        f"- public_repo_video_policy: 공개 저장소에 타인 영상 업로드 방지 (저장소를 private으로 바꾸면 자동 업로드)\n"
                        f"- 영상 위치: 분석을 실행한 PC의 {ctx.out_dir / rel}\n",
                        "utf-8")
    return skipped


def stage8_push_github(ctx, token):
    cfg = ctx.cfg
    result = {"pushed": False}
    ctx.data["github_push"] = result
    if not cfg["PUSH_TO_GITHUB"]:
        log("GITHUB", "PUSH_TO_GITHUB=False → 건너뜀")
        return result
    if not token:
        ctx.note("GITHUB", "GitHub 토큰 없음 → 푸시 건너뜀 (결과는 PC에만 저장됨)",
                 hint=".env 파일에 GITHUB_TOKEN=... 입력 후 다시 실행")
        return result
    if not shutil.which("git"):
        ctx.note("GITHUB", "Git이 설치되어 있지 않아 푸시 건너뜀 (결과는 PC에만 저장됨)",
                 hint="https://git-scm.com/downloads 에서 Git 설치 후 다시 실행")
        return result
    repo, branch = cfg["GITHUB_REPO"].strip(), cfg["GITHUB_BRANCH"].strip()
    r = github_api(f"/repos/{repo}", token)
    if r.status_code == 401:
        raise RuntimeError("GitHub 토큰이 유효하지 않습니다 (401) → 토큰 재발급/확인")
    if r.status_code == 404:
        raise RuntimeError(f"저장소 {repo} 를 찾을 수 없거나 토큰에 접근 권한이 없습니다 (404) → Fine-grained 토큰의 저장소 선택 확인")
    r.raise_for_status()
    meta = r.json()
    private = bool(meta.get("private"))
    perms = meta.get("permissions") or {}
    if perms and not perms.get("push"):
        raise RuntimeError("토큰에 쓰기 권한이 없습니다 → Contents: Read and write 권한 필요")
    allow_videos = private or cfg["ALLOW_VIDEO_UPLOAD_TO_PUBLIC_REPO"]
    log("GITHUB", "저장소 확인", repo=repo, branch=branch, private=private, default_branch=meta.get("default_branch"), allow_videos=allow_videos)
    if not private and not cfg["ALLOW_VIDEO_UPLOAD_TO_PUBLIC_REPO"]:
        ctx.note("GITHUB", "공개(public) 저장소 → 성공사례 영상 파일은 GitHub에 올리지 않음 (대본·썸네일·메타데이터는 업로드)",
                 hint="저장소를 private으로 변경하면 영상도 함께 업로드됩니다", videos_kept_in=str(ctx.out_dir))
    if not private and cfg["ALLOW_VIDEO_UPLOAD_TO_PUBLIC_REPO"]:
        ctx.note("GITHUB", "⚠️ ALLOW_VIDEO_UPLOAD_TO_PUBLIC_REPO=True → 타인 영상이 공개 저장소에 업로드됩니다 (저작권 침해 위험)", level="WARNING")

    u = github_api("/user", token)
    login, uid = (u.json().get("login"), u.json().get("id")) if u.status_code == 200 else ("yt-analyzer", 0)
    author = ["-c", f"user.name={login}", "-c", f"user.email={uid}+{login}@users.noreply.github.com"]
    auth = base64.b64encode(f"x-access-token:{token}".encode()).decode()
    register_secret(auth)
    branch_exists = github_api(f"/repos/{repo}/branches/{branch}", token).status_code == 200
    rel_path = f"{cfg['PROJECT_FOLDER']}/{cfg['RESULT_FOLDER']}"
    url = f"https://github.com/{repo}.git"

    for round_ in (1, 2):   # 동시 수정으로 push가 거부되면 새로 clone해서 1회 재시도
        clone = ctx.work_dir / "_github_clone"
        rmtree_force(clone)
        if branch_exists:
            run_git(["clone", "--depth", "1", "--branch", branch, "--single-branch", url, str(clone)], ctx.work_dir, auth)
        else:
            run_git(["clone", "--depth", "1", url, str(clone)], ctx.work_dir, auth)
            run_git(["checkout", "-b", branch], clone)
            log("GITHUB", "브랜치가 없어 새로 생성", branch=branch)
        project_dir = clone / cfg["PROJECT_FOLDER"]
        if not project_dir.exists():
            log("GITHUB", "상위 폴더가 없어 새로 생성", folder=cfg["PROJECT_FOLDER"])
        target = clone / rel_path
        if target.exists() and cfg["CLEAN_OLD_RESULTS"]:
            rmtree_force(target)
            log("GITHUB", "기존 결과 폴더 교체 (이전 버전은 git 기록에 보존)", path=rel_path)
        target.mkdir(parents=True, exist_ok=True)
        skipped = _copy_results(ctx, target, allow_videos)
        run_git(["add", "-A", "--", rel_path], clone)
        _, status = run_git(["status", "--porcelain", "--", rel_path], clone)
        if not status.strip():
            log("GITHUB", "변경 사항 없음 → 커밋 생략")
            result.update(pushed=False, reason="no_changes")
            return result
        msg = f"[{cfg['TOPIC']}] YouTube 분석 결과 {ctx.run_id} ({NOTEBOOK_VERSION})"
        run_git(author + ["commit", "-q", "-m", msg], clone)
        pushed, out = False, ""
        for attempt, wait in enumerate((0, 2, 4, 8, 16), 1):
            time.sleep(wait)
            code, out = run_git(["push", "origin", f"HEAD:refs/heads/{branch}"], clone, auth, check=False)
            if code == 0:
                pushed = True
                break
            if "non-fast-forward" in out or "fetch first" in out or "rejected" in out:
                break
            log("GITHUB", "push 실패 → 재시도", level="WARNING", attempt=attempt, error=out[-200:])
        if pushed:
            break
        if round_ == 1 and ("non-fast-forward" in out or "fetch first" in out or "rejected" in out):
            log("GITHUB", "원격에 새 커밋이 있어 거부됨 → 새로 clone 후 재시도", level="WARNING")
            branch_exists = True
            continue
        raise RuntimeError(f"git push 실패: {out[-500:]}")
    _, sha = run_git(["rev-parse", "HEAD"], clone)
    files = [p for p in target.rglob("*") if p.is_file()]
    web = f"https://github.com/{repo}/tree/{branch}/{rel_path}"
    result.update(pushed=True, commit=sha.strip()[:12], url=web, files=len(files), skipped=skipped,
                  total_mb=round(sum(p.stat().st_size for p in files) / 1e6, 1), allow_videos=allow_videos)
    log("GITHUB", "✅ 푸시 완료", commit=result["commit"], files=result["files"], total_mb=result["total_mb"],
        skipped=len(skipped), url=web)
    if skipped:
        log("GITHUB", "GitHub에서 제외된 파일", level="WARNING", files=[f"{p}({mb}MB,{why})" for p, mb, why in skipped])
    rmtree_force(clone)
    return result


def open_path(path):
    """결과 폴더/리포트를 OS 기본 프로그램으로 열기 (Windows 탐색기 / macOS Finder / Linux 파일관리자)."""
    try:
        if IS_WINDOWS:
            os.startfile(str(path))                    # noqa: (Windows 전용)
        elif sys.platform == "darwin":
            subprocess.Popen(["open", str(path)])
        elif shutil.which("xdg-open"):
            subprocess.Popen(["xdg-open", str(path)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as e:
        log("OUTPUT", "폴더 열기 실패 (직접 여세요)", level="DEBUG", path=str(path), error=type(e).__name__)


def stage8_finish(ctx):
    """PC 결과 정리: 용량 요약, (선택) zip, (선택) 결과 폴더 열기."""
    cfg = ctx.cfg
    files = [p for p in ctx.out_dir.rglob("*") if p.is_file()]
    total_mb = round(sum(p.stat().st_size for p in files) / 1e6, 1)
    videos = [p for p in files if p.suffix.lower() in VIDEO_EXTS]
    result = {"out_dir": str(ctx.out_dir), "files": len(files), "total_mb": total_mb, "videos": len(videos), "zip": None}
    if cfg["MAKE_RESULT_ZIP"]:
        t0 = time.perf_counter()
        rel = f"{cfg['PROJECT_FOLDER']}/{cfg['RESULT_FOLDER']}"
        base = ctx.output_root / f"{rel.replace('/', '_')}_{ctx.run_id}"
        result["zip"] = shutil.make_archive(str(base), "zip", root_dir=str(ctx.output_root), base_dir=rel)
        log("OUTPUT", "결과 zip 생성", zip=result["zip"], zip_mb=round(os.path.getsize(result["zip"]) / 1e6, 1),
            elapsed_sec=round(time.perf_counter() - t0, 1))
    push = ctx.data.get("github_push", {})
    held_back = [s for s in push.get("skipped", []) if s[2] == "public_repo_video_policy"]
    if videos and (held_back or not push.get("pushed")):
        ctx.note("OUTPUT", "성공사례 영상 파일은 이 PC에만 저장되어 있습니다", level="INFO", videos=len(videos),
                 path=str(ctx.out_dir / "success_cases"))
    log("OUTPUT", "✅ 결과 정리", **{k: v for k, v in result.items() if k != "zip"})
    ctx.data["finish"] = result
    if cfg["OPEN_RESULT_FOLDER"]:
        open_path(ctx.out_dir)
    return result


# =====================================================================================================
# 🧰 [모듈] 자가진단(오프라인 테스트)
# =====================================================================================================
# VERSION: v2.0.0 — 2026-10-09 — 임시폴더를 OS 기본 위치로 변경 (v1.2.0: 쿠키 점검·봇 확인 재시도/중단 테스트) (자가진단: 네트워크/API 없이 핵심 로직 검증)
def make_synthetic_dataset(seed=7, n_channels=40, per_channel=12):
    """알려진 패턴을 심은 가짜 데이터: '숫자 포함 제목'은 조회수 3배, 소규모 채널 일부도 터짐."""
    rng = np.random.default_rng(seed)
    now = pd.Timestamp("2026-10-01T00:00:00Z")
    vids, chans, base = [], [], []
    for c in range(n_channels):
        cid = f"UC{c:022d}"
        subs = int(10 ** rng.uniform(2.5, 6))
        chans.append({"channel_id": cid, "channel_title_ch": f"채널{c}", "channel_handle": None,
                      "channel_published_at": (now - pd.Timedelta(days=int(rng.uniform(100, 3000)))).isoformat(),
                      "channel_country": "KR", "subscribers": subs, "subs_hidden": False, "channel_views": subs * 50,
                      "channel_video_count": 100, "uploads_playlist": "UU" + cid[2:]})
        typical = subs * 0.3 + 300
        for j in range(per_channel):
            vid = f"v{c:03d}_{j:03d}x"[:11]
            has_num = j % 2 == 0
            views = typical * rng.lognormal(0, 0.3) * (3.0 if has_num else 1.0)
            dur = 40 if j % 4 == 3 else int(rng.uniform(300, 1500))
            age = int(rng.uniform(20, 300))
            title = f"{'5가지 ' if has_num else ''}주식 {'초보' if j % 3 == 0 else '전망'} 이야기 {['삼성전자', 'ETF', '배당주'][j % 3]}"
            row = {"video_id": vid, "title": title, "description": "", "channel_id": cid, "channel_title": f"채널{c}",
                   "published_at": (now - pd.Timedelta(days=age)).isoformat(), "tags": ["주식", "투자"], "category_id": "27",
                   "default_audio_language": "ko", "live_broadcast_content": "none", "duration_iso": f"PT{dur // 60}M{dur % 60}S",
                   "definition": "hd", "has_caption": False, "views": str(int(views)), "likes": str(int(views * 0.02)),
                   "comments": str(int(views * 0.002)), "was_live": False, "thumbnail_url": None}
            vids.append(row)
            base.append({"channel_id": cid, **{k: row[k] for k in ["video_id", "views", "published_at", "duration_iso", "was_live", "live_broadcast_content"]}})
    search = []
    for k, kw in enumerate(["주식", "주식 초보", "주식 전망"]):
        sample = rng.choice(len(vids), 30, replace=False)
        for rank, i in enumerate(sample, 1):
            for order in ("relevance", "viewCount"):
                search.append({"keyword": kw, "order": order, "rank": rank, "video_id": vids[i]["video_id"],
                               "channel_id": vids[i]["channel_id"], "total_results": 1000, "published_after": None})
    ac = pd.DataFrame({"norm": ["주식", "주식초보", "주식전망"], "keyword": ["주식", "주식 초보", "주식 전망"],
                       "ac_score": [3.0, 2.0, 1.0], "ac_hits": [10, 5, 3], "best_rank": [0, 1, 2], "contains_topic": True, "ac_rank": [1, 2, 3]})
    return pd.DataFrame(vids), pd.DataFrame(chans), pd.DataFrame(base), pd.DataFrame(search), ac, now


def run_self_test(cfg):
    t0 = time.perf_counter()
    results = []

    def check(name, cond, **kv):
        results.append((name, bool(cond)))
        log("SELFTEST", f"{'✅' if cond else '❌'} {name}", level="INFO" if cond else "ERROR", **kv)

    d = parse_iso_duration(["PT1H2M3S", "PT45S", "P1DT0S", "PT0S", None, "P0D"]).tolist()
    check("ISO8601 길이 파싱", d[:4] == [3723, 45, 86400, 0] and np.isnan(d[4]) and d[5] == 0, parsed=d)
    js = '["주식",["주식","주식 초보","주식 전망"],[],{}]'
    jp = 'window.google.ac.h(["주식",[["주식 기초",0,[512]],["주식 공부",0,[512]]],{"k":1}])'
    check("자동완성 파싱 (JSON/JSONP)", parse_autocomplete(js) == ["주식", "주식 초보", "주식 전망"]
          and parse_autocomplete(jp) == ["주식 기초", "주식 공부"])
    vtt = ("WEBVTT\n\n00:00:00.000 --> 00:00:02.000\n안녕하세요\n\n00:00:02.000 --> 00:00:04.000\n안녕하세요\n오늘은 <c>주식</c>\n\n"
           "00:00:04.000 --> 00:00:06.000\n오늘은 주식\n이야기입니다\n")
    segs = parse_vtt(vtt)
    check("VTT 자막 파싱 + 롤링 중복 제거", [s["text"] for s in segs] == ["안녕하세요", "오늘은 주식", "이야기입니다"], texts=[s["text"] for s in segs])
    q = bh_fdr([0.01, 0.04, 0.03, np.nan])
    check("다중비교 보정(BH-FDR)", np.allclose(q[:3], [0.03, 0.04, 0.04]) and np.isnan(q[3]), q=list(np.round(q, 4)))
    check("키워드 정규화/폴더 검증", normalize_kw(" 주식  시작 ") == "주식시작" and sanitize_folder("/stock/", "t") == "stock")

    vr, ch, base, search, ac, now = make_synthetic_dataset(cfg["RANDOM_SEED"])
    tcfg = {**cfg, "SHORTS_HTTP_CHECK": False, "MATURE_AGE_DAYS": 14, "ANALYSIS_DAYS": 365, "MIN_SUCCESS_VIEWS": 100,
            "OUTLIER_MIN": 1.8, "FETCH_COMMENTS_TOP_N": 0, "SUCCESS_CASE_COUNT": 6, "MAX_CASES_PER_CHANNEL": 1}
    tctx = RunContext(cfg=tcfg, run_id="selftest", started_at=now.to_pydatetime(), work_dir=Path("."), out_dir=Path("."),
                      cache=JsonCache(Path(tempfile.gettempdir()) / "yt_selftest_cache", 0))
    tctx.data.update(videos_raw=vr, channels_raw=ch, baseline_raw=base, search_df=search, keywords_ac=ac, collected_at=now)
    prev = LOGGER.level
    LOGGER.setLevel(logging.WARNING)   # 자가진단 내부 로그는 숨김
    try:
        v = build_video_frame(tctx)
        perf = tctx.data["perf"]
        tf = analyze_title_features(perf)
        kw = analyze_keywords(tctx)
        sel = select_success_cases(perf, tcfg)
    finally:
        LOGGER.setLevel(prev)
    lift = tf.query("segment=='전체' and feature=='has_number'")["lift"]
    check("아웃라이어: 숫자 제목(심어둔 3배 효과) 탐지", len(lift) and 2.0 < float(lift.iloc[0]) < 4.5, lift=float(lift.iloc[0]) if len(lift) else None)
    check("아웃라이어: 기준선 leave-one-out", (v["baseline_kind"] != "insufficient").mean() > 0.9, ok_ratio=(v["baseline_kind"] != "insufficient").mean())
    check("포맷 분류 (≤60초=쇼츠)", set(v.loc[v["duration_sec"] <= 60, "fmt"]) == {"shorts"})
    check("키워드 기회점수 0~100", kw["opportunity"].dropna().between(0, 100).all() and len(kw) == 3, scores=kw["opportunity"].tolist())
    check("성공사례: 채널당 1개 + 개수", sel["channel_id"].is_unique and len(sel) == 6, n=len(sel))
    # 쿠키 점검: 값은 읽지 않고 이름·만료만 확인
    import types
    tmpd = Path(tempfile.mkdtemp())
    ck = tmpd / "c.txt"
    ck.write_text("# Netscape HTTP Cookie File\n.youtube.com\tTRUE\t/\tTRUE\t4102444800\t__Secure-3PSID\tx\n"
                  "#HttpOnly_.youtube.com\tTRUE\t/\tTRUE\t1000\tLOGIN_INFO\ty\n.youtube.com\tTRUE\t/\tFALSE\t0\tPREF\tz\n", "utf-8")
    ci = inspect_cookies(ck)
    check("쿠키 점검(로그인 쿠키·만료 탐지)", ci["auth_cookies"] == ["LOGIN_INFO", "__Secure-3PSID"] and ci["expired_auth"] == ["LOGIN_INFO"], info=ci)

    # 봇 확인 대응: 기본 클라이언트가 막히면 tv로 재시도 → 이후 tv 우선, 전부 막히면 연속 N회 후 중단
    class _FakeYDL:
        mode = "tv_ok"

        def __init__(self, opts):
            self.client = tuple((opts.get("extractor_args") or {}).get("youtube", {}).get("player_client", ["default"]))

        def __enter__(self):
            return self

        def __exit__(self, *a):
            return False

        def go(self):
            if _FakeYDL.mode == "flaky":
                _FakeYDL.calls += 1
                if _FakeYDL.calls == 1:
                    raise RuntimeError("ERROR: [youtube] x: Failed to extract any player response")
                return "ok"
            if _FakeYDL.mode == "tv_ok" and self.client == ("tv",):
                return "ok"
            raise RuntimeError("ERROR: [youtube] x: Sign in to confirm you’re not a bot.")
    saved_mod, saved_state = sys.modules.get("yt_dlp"), dict(DL_STATE)
    sys.modules["yt_dlp"] = types.SimpleNamespace(YoutubeDL=_FakeYDL)
    try:
        DL_STATE.update(client=None, bot_streak=0, bot_total=0, disabled=False, client_hits=Counter(), cookiefile="", proxy="",
                        last_blocked=None)
        bcfg = {**cfg, "YTDLP_CLIENT_FALLBACK": True, "YTDLP_MAX_BOT_BLOCKS": 2}
        r1 = run_ytdlp(bcfg, {}, lambda y: y.go(), "t1")
        remembered = DL_STATE["client"]
        _FakeYDL.mode = "all_blocked"
        errs = []
        for vid in ("t2", "t2", "t3", "t4"):        # t2 두 번(영상+자막) = 영상 1개로 집계
            try:
                run_ytdlp(bcfg, {}, lambda y: y.go(), vid)
            except BotCheckError as e:
                errs.append(str(e)[:20])
        check("봇 확인: 클라이언트 재시도 + 연속 차단 시 중단", r1 == "ok" and remembered == ("tv",) and len(errs) == 4
              and DL_STATE["disabled"] and DL_STATE["bot_total"] == 2, remembered=remembered, bot_total=DL_STATE["bot_total"])
        # 일시 오류(간헐적 응답 추출 실패)는 같은 클라이언트로 재시도해서 성공
        global TRANSIENT_WAITS
        saved_waits, TRANSIENT_WAITS = TRANSIENT_WAITS, (0.01, 0.01)
        DL_STATE.update(client=None, bot_streak=0, bot_total=0, disabled=False, last_blocked=None)
        _FakeYDL.mode, _FakeYDL.calls = "flaky", 0
        r2 = run_ytdlp(bcfg, {}, lambda y: y.go(), "t5")
        TRANSIENT_WAITS = saved_waits
        check("일시 오류 자동 재시도", r2 == "ok" and _FakeYDL.calls == 2, calls=_FakeYDL.calls)
    finally:
        if saved_mod is not None:
            sys.modules["yt_dlp"] = saved_mod
        else:
            sys.modules.pop("yt_dlp", None)
        DL_STATE.clear()
        DL_STATE.update(saved_state)
        rmtree_force(tmpd)
    passed = sum(ok for _, ok in results)
    log("SELFTEST", "자가진단 완료", passed=f"{passed}/{len(results)}", elapsed_sec=round(time.perf_counter() - t0, 2))
    if passed != len(results):
        raise AssertionError(f"자가진단 실패: {[n for n, ok in results if not ok]} → 코드/패키지 버전을 확인하세요")
    return results


# =====================================================================================================
# VERSION: v2.0.0 — 2026-10-09 — 실행부: .env 키 읽기, 명령줄 옵션, 단계별 실행·요약 (노트북 실행 셀 대체)
# =====================================================================================================
import argparse

def load_env_file(path):
    """KEY=VALUE 형식 .env 읽기 (메모장 BOM/따옴표 허용). 값은 출력하지 않음."""
    values = {}
    for line in Path(path).read_text("utf-8-sig").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        values[k.strip()] = v.strip().strip('"').strip("'")
    return values


def _mask(v):
    return f"{v[:4]}…{v[-4:]} (len={len(v)})" if len(v) >= 10 else ("(없음)" if not v else "***")


def load_keys():
    """키 우선순위: .env 파일 → 환경변수. .env가 없으면 템플릿을 만들고 종료."""
    env_path = BASE_DIR / ENV_FILE
    if not env_path.exists():
        env_path.write_text(ENV_TEMPLATE, "utf-8")
        print(f"[KEYS] 📝 키 파일을 만들었습니다: {env_path}\n"
              f"[KEYS]    메모장 등으로 열어 YOUTUBE_API_KEY(필수), GITHUB_TOKEN(권장)을 입력·저장한 뒤 다시 실행하세요.")
        sys.exit(1)
    vals = load_env_file(env_path)
    keys = {}
    for k in ("YOUTUBE_API_KEY", "GITHUB_TOKEN", "YTDLP_PROXY"):
        v, src = vals.get(k, ""), ".env"
        if not v and os.environ.get(k, "").strip():
            v, src = os.environ[k].strip(), "env"
        keys[k] = v
        print(f"[KEYS] {k}={_mask(v) if k != 'YTDLP_PROXY' else ('있음' if v else '(없음)')} source={src if v else '-'}")
    if not keys["YOUTUBE_API_KEY"]:
        print(f"[KEYS] ❌ YOUTUBE_API_KEY 가 비어 있습니다 → {env_path} 에 입력 후 다시 실행하세요.")
        sys.exit(1)
    if not keys["YOUTUBE_API_KEY"].startswith("AIza"):
        print("[KEYS] ⚠️ YouTube API 키는 보통 'AIza'로 시작합니다. 값을 다시 확인하세요.")
    if not keys["GITHUB_TOKEN"]:
        print("[KEYS] ⚠️ GITHUB_TOKEN 이 없습니다 → 결과는 PC에만 저장되고 GitHub 푸시는 건너뜁니다.")
    return keys


def parse_args(argv=None):
    p = argparse.ArgumentParser(description="YouTube 주제 분석기 — 0명 채널이 조회수를 가장 잘 받을 영상 찾기")
    p.add_argument("--topic", help=f"분석 주제 (기본: {TOPIC})")
    p.add_argument("--folder", help=f"결과 상위 폴더 PROJECT_FOLDER (기본: {PROJECT_FOLDER})")
    p.add_argument("--result-folder", help=f"결과 하위 폴더 RESULT_FOLDER (기본: {RESULT_FOLDER})")
    p.add_argument("--keywords", type=int, help=f"검색 키워드 수 (기본: {MAX_SEARCH_KEYWORDS})")
    p.add_argument("--cases", type=int, help=f"성공사례 수 (기본: {SUCCESS_CASE_COUNT})")
    p.add_argument("--no-video", action="store_true", help="성공사례 영상 파일은 받지 않음 (대본·썸네일만)")
    p.add_argument("--no-push", action="store_true", help="GitHub 푸시 안 함")
    p.add_argument("--no-open", action="store_true", help="끝나고 결과 폴더 열지 않음")
    p.add_argument("--log-level", choices=["DEBUG", "INFO", "WARNING"], help="로그 상세도")
    p.add_argument("--skip-install", action="store_true", help="패키지 자동 설치/업데이트 안 함")
    return p.parse_args(argv)


def apply_cli(cfg, args):
    """명령줄 옵션으로 설정 덮어쓰기 — 바뀐 값은 로그에 남김."""
    changes = {}
    for opt, key, val in (("topic", "TOPIC", args.topic), ("folder", "PROJECT_FOLDER", args.folder),
                          ("result_folder", "RESULT_FOLDER", args.result_folder),
                          ("keywords", "MAX_SEARCH_KEYWORDS", args.keywords), ("cases", "SUCCESS_CASE_COUNT", args.cases),
                          ("log_level", "LOG_LEVEL", args.log_level)):
        if val is not None:
            changes[key] = (cfg[key], val)
            cfg[key] = val
    for flag, key, val in ((args.no_video, "DOWNLOAD_VIDEOS", False), (args.no_push, "PUSH_TO_GITHUB", False),
                           (args.no_open, "OPEN_RESULT_FOLDER", False)):
        if flag:
            changes[key] = (cfg[key], val)
            cfg[key] = val
    return changes


def main(argv=None):
    args = parse_args(argv)
    keys = load_keys()
    cfg = collect_config(globals())
    changes = apply_cli(cfg, args)
    ctx = init_run(cfg, keys["YOUTUBE_API_KEY"], keys["GITHUB_TOKEN"])
    if changes:
        log("INIT", "명령줄 옵션으로 변경된 설정", **{k: f"{a} → {b}" for k, (a, b) in changes.items()})
    if ctx.cfg["TOPIC"] != "주식" and ctx.cfg["PROJECT_FOLDER"] == "stock":
        ctx.note("INIT", "주제를 바꿨는데 저장 폴더는 'stock' 그대로입니다 → 기존 주식 결과를 덮어씁니다",
                 hint="--folder 로 다른 폴더명을 지정하세요 (예: --topic 부동산 --folder realestate)")
    try:
        if ctx.cfg["RUN_SELF_TEST"]:
            with stage_timer(ctx, "SELFTEST"):
                run_self_test(ctx.cfg)
        with stage_timer(ctx, "KEYWORD"):
            keywords = stage1_keyword_discovery(ctx)
        ctx.yt = YouTubeClient(keys["YOUTUBE_API_KEY"], ctx.cache, ctx.cfg["QUOTA_BUDGET"])
        with stage_timer(ctx, "COLLECT"):
            stage2_collect(ctx, keywords)
        with stage_timer(ctx, "FEATURE"):
            stage3_features(ctx)
        with stage_timer(ctx, "ANALYSIS"):
            stage4_analysis(ctx)
        with stage_timer(ctx, "CHART"):
            stage5_charts(ctx)
        refresh_download_auth(ctx, proxy=keys["YTDLP_PROXY"])
        with stage_timer(ctx, "SUCCESS"):
            stage6_success_cases(ctx)
        with stage_timer(ctx, "REPORT"):
            stage7_report(ctx)
        try:            # 푸시 실패(토큰 오류·네트워크 등)는 PC 결과에 영향이 없으므로 계속 진행
            with stage_timer(ctx, "GITHUB"):
                stage8_push_github(ctx, keys["GITHUB_TOKEN"])
        except Exception as e:
            ctx.note("GITHUB", "GitHub 푸시 실패 — 결과는 PC에 저장되어 있습니다", level="ERROR",
                     error=f"{type(e).__name__}: {str(e)[:200]}", hint="토큰 권한(Contents: Read and write)·네트워크 확인 후 다시 실행")
        with stage_timer(ctx, "OUTPUT"):
            stage8_finish(ctx)
    except KeyboardInterrupt:
        log("SUMMARY", "사용자가 중단했습니다 (Ctrl+C). API 응답은 캐시되어 다시 실행하면 이어서 빠르게 진행됩니다.", level="WARNING")
        return 130
    except Exception as e:
        log("SUMMARY", "❌ 실행 실패 — 위 로그의 원인과 next_step/hint를 확인하세요", level="ERROR",
            error=f"{type(e).__name__}: {str(e)[:300]}", log_file=str(ctx.out_dir / "run_log.txt"))
        if ctx.cfg["LOG_LEVEL"] == "DEBUG":
            import traceback
            traceback.print_exc()
        return 1
    p = ctx.data.get("github_push", {})
    log("SUMMARY", "실행 요약", version=NOTEBOOK_VERSION, run_id=ctx.run_id, topic=ctx.cfg["TOPIC"],
        quota_used=ctx.yt.used if ctx.yt else 0, timings_sec=ctx.timings, notes=len(ctx.notes))
    log("SUMMARY", "결과 위치", report=str(ctx.out_dir / "README.md"), github=p.get("url", "(푸시 안 함)"), commit=p.get("commit"))
    for r in ctx.data.get("recommendations", [])[:5]:
        log("SUMMARY", f"추천 #{r['rank']}", keyword=r["keyword"], opportunity=r["opportunity"], format=r["format"], title=r["titles"][0])
    for n in ctx.notes:
        log("SUMMARY", "주의", level="WARNING", note=n)
    return 0


if __name__ == "__main__":
    sys.exit(main())
