#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.10 — 2026-10-14 — 음성인식 기록 요약(whisper_summary)이 2차(전체) 기록('<영상ID>#full' — 분석기 v2.10.0)을 영상으로 세지 않게
# (v1.9 — 2026-10-14 — 성공 사례 분석 도구(tools/success_analysis.py)·규칙(<주제>/analysis_rules.toml)도 GitHub 최신으로 받는 목록에
#          (SYNC_CODE·SYNC_CONFIG — 사용자 지시: "… 올바른 분석 결과까지만 내도록 수정해"))
# (v1.8 — 2026-10-14 — 웹 화면(tools/web_ui.py·tools/weekly_analysis.py)도 회차마다 GitHub 최신으로 받는 코드 목록에 (SYNC_CODE).
#          자동 실행은 이제 run_analyzer.ps1 -Auto (기본은 웹 화면). 자막 서버 차단(IpBlocked)은 '네트워크 때문에 못 받은 자막'으로
#          세지 않음 — tools/outlier_research.py v1.9 가 음성인식으로 보냄 (예전: 그 때문에 끝나지 않고 매일 같은 자막을 다시 요청))
# (v1.7 — 2026-10-13 — 내가 고친 검색어가 바로 쓰이게 (사용자 지시: "내가 검색어 변경했는데 안되네 해결해봐" · "걍 검색어 내가
#          수정해도 돌아가게 하면 안돼? 꼭 그룹을 지정해야하나 검색어만 넣어도 되잖아"):
#          ① 회차마다 GitHub 에서 설정·검색어를 받음 (sync_from_github): <주제>/keywords.txt·keywords.toml·analyzer_config.toml·
#             tag_rules.toml — PC 파일이 지난번에 받은 그대로면 GitHub 새 판으로 바꿈(.bak), PC 에서 고쳤고 GitHub 은 그대로면 PC 것을 지킴.
#             VERSION 을 올리지 않아도 됨. 코드·실행기(run_analyzer.ps1·.sh)도 GitHub 최신으로 (이 파일 자신은 다음 실행부터).
#             예전: 실행기가 '없을 때만'(v2.2)·'VERSION 이 높을 때만'(v2.3) 받고, 며칠 도는 동안 다시 보지 않아 GitHub 수정이 안 왔음
#          ② 검색어 목록 keywords.txt (한 줄에 하나, 그룹 없음) — 할당량 계산·지문도 이것으로
#          ③ 검색어가 바뀌면 분석기를 다시 돌림 (예전: 분석기가 끝나면 7일 동안 건너뜀 → 새 검색어가 분석기에 안 쓰임)
#          ④ --tag-keywords 기본 0 — 내가 적은 검색어만 검색 (지운 검색어가 '잘된 영상 태그'로 되살아나지 않게))
# (v1.6 — 2026-10-13 — pip 이 없는 가상환경 고침 (사용자 PC 오류: ".venv\Scripts\python.exe: No module named pip" → 패키지 설치 실패):
#          ensure_pip() — pip 이 없으면 ① python -m ensurepip --upgrade --default-pip ② 안 되면 공식 get-pip.py(bootstrap.pypa.io)
#          로 설치한 뒤 패키지를 설치. 가상환경을 만들다 끊기면(첫 실행 중단 등) python.exe 만 있고 pip 이 없는 .venv 가 남는다)
# (v1.5 — 2026-10-13 — 검색어 전부 (사용자 지시: "그냥 검색어를 재테크 관련 태그로 찾아서 다 그걸로 탐색해봐"):
#          ① --per-group 0(기본) = keywords.toml 의 검색어 전부를 성공 사례 수집에 (검색어는 tools/tag_keywords.py 가 태그로 채움)
#             자동 할당량(outlier_need)도 검색어 전부로 계산 (같은 검색어는 한 번)
#          ② ⚠️ 분석기 최소 할당량 300 → ANALYZER_MIN_UNITS 1,000: 검색어 40개면 첫날 성공 사례 검색(약 9,000단위)이 하루 몫을 거의 다 써서
#             분석기에 수백 단위만 남는데, 그걸로 돌리면 검색 0~1개짜리 빈 결과만 만들고 오래 걸림 → 다음 회차(할당량 초기화 뒤)로 미룸)
# (v1.4 — 2026-10-13 — 빠른 것 먼저 올리고 음성인식은 뒤에서 하나씩 (사용자 지시: "일단 영상 자체는 받지말고 자막, 썸네일, 댓글 등
#          빨리 받을 수 있는 것들만 다 받으면 분석결과를 먼저 올리도록 하고 오래걸리는 음성인식은 계속 진행해서 하나가 끝나면 바로 올리고
#          그다음거 진행하는 식으로" · "태그도 검색어에 포함하도록 해서 탐색"): 회차 순서 = ① 성공 사례(자막·썸네일·댓글·태그 검색어)
#          → ② 바로 올림(성공 사례 결과 먼저, 분석기가 도는 회차만) → ③ 분석기(--no-video --defer-whisper: 영상 파일 안 받음·음성인식 미룸)
#          → ④ 보충 → ⑤ 올림 → ⑥ 음성인식 대기열(youtube_topic_analyzer.py --whisper-queue: 하나 끝날 때마다 바로 올림).
#          --tag-keywords 5 (자동 할당량에 태그 검색 포함), --no-whisper)
# (v1.3 — 2026-10-13 — 남는 할당량을 버리지 않기 (사용자 지시: "너무 오래 걸리는데 댓글 전체 받아서 그런거야? … 좋은 해결 방법"):
#          ① 오늘(태평양 날짜) 쓴 단위를 주제마다 적어 둠 (.yt_work/quota_<주제>.json — 도구가 보고한 사용량의 합)
#          ② 분석기 다음에 '보충' 단계: 오늘 남은 할당량(10,000 ÷ 같은 키 주제 수 − 200)으로 성공 사례 수집을 한 번 더 →
#             검색은 캐시라 남은 단위가 거의 다 댓글에 감. 예전엔 고정 배분(4,000/6,000) 때문에 몇백 단위 댓글 때문에 하루를 더 기다렸음
#          ③ 오늘 이미 쓴 양을 빼고 도구에 할당량을 줌 (--once 를 하루 두 번 돌려도 넘지 않게), 분석기 사용량을 잘못 읽던 것 고침(quota_used)
#          ④ 진행 상태에 ready(인기 댓글까지 받아 분석 시작 가능)·오늘 쓴 단위
#          ⑤ 성공 사례 할당량을 검색 수로 계산 (--outlier-quota 0 = 자동, 기본): 예전 고정 4,000은 검색 40번(4,000)+여유 150 이
#             안 들어가 검색 2번이 늘 다음 날로 밀렸음 → 이제 첫날 검색·인기 댓글까지 끝나 첫날 분석 시작 가능(ready), 분석기는 나머지)
# (v1.2 — 2026-10-13 — 여러 주제를 동시에(병렬로) (사용자 지시: "동시에 병렬로 다른 주제 분석도 가능하도록 해야해 그럼 검색어 설정 파일,
#          키설정 파일도 여러개 있어야 겠지"): `pc_analysis.py economic health` → 패키지 준비를 한 번 하고 주제마다 따로 프로세스를 띄움
#          (화면 줄 앞에 [주제], 주제마다 잠금·로그·진행 파일·할당량 대기). 검색어는 <주제>/keywords.toml, 키는 <주제>/.env
#          (없으면 맨 위 .env) — 같은 키를 쓰는 주제끼리 하루 할당량을 나눔(성공 사례·분석기 QUOTA_BUDGET 모두 ÷ 주제 수).
#          ⚠️ 할당량을 늘리려고 프로젝트를 여러 개 만드는 것은 YouTube API 정책 위반('sharding') — 기본은 키 하나를 나눠 씀)
# (v1.1 — 2026-10-13 — 댓글 전부·조회수 상위 (사용자 지시: "비공개로 돌릴테니까 전부 다 업로드되게 하고 댓글은 전부 받도록 수정해
#          그리고 구독자 수 상관없이 조회수 많이 나온 영상 댓글은 전부 받아야해"):
#          ① 성공 사례 수집에 --popular(조회수 상위, 기본 20)를 넘김 — 댓글은 outlier_research v1.3 기본값(전부)
#          ② 분석기가 이미 끝났으면(이월 검색어 0, 7일 안) 다음 회차부터 분석기를 건너뛰고 하루 할당량(--daily-quota 9500)을
#             성공 사례·조회수 상위 댓글에 씀 (.yt_work/pc_progress_<주제>.json 의 analyzer_done_kst — --once 로 매일 불러도 같음)
#          ③ 기본 최대 회차 7 → 10 (댓글 전부는 며칠 걸릴 수 있음))
# (v1.0 — 2026-10-13 — 신규 (사용자 지시: "분석기 코드 pc에서 돌릴 수 있도록 수정하고 … api 할당량이 초기화된 시간이 되면
#          다시 자동으로 분석결과를 확인 못한 부분부터 새로 추가로 만들도록"):
#          PC 에서 한 주제(기본 economic)를 끝까지 분석한다. 한 '회차' =
#            ① tools/outlier_research.py (작은 채널 성공 사례 — 자막·썸네일·댓글, 할당량 약 4,000)
#            ② youtube_topic_analyzer.py --no-push (주제 전체 분석, 할당량 QUOTA_BUDGET)
#            ③ 진행 상태 pc_progress.json 을 결과 폴더에 쓰고 youtube_topic_analyzer.py --push-only (GitHub, 성공 사례 요약 포함)
#          할당량 때문에 못 한 일이 남으면(성공 사례 status.json complete=false · 분석기 run_info.json 의 이월 검색어 ·
#          네트워크 때문에 못 받은 자막) 다음 할당량 초기화(태평양 자정 + 10분 = 한국 오후 4:10, 겨울 5:10)까지 기다렸다가
#          다음 회차를 돈다. 두 도구 모두 받은 검색·영상 정보·자막을 캐시하므로 다음 회차는 '못 한 부분만' 새로 받는다.)
r"""
사용법 (PC 실행 폴더 = run_analyzer.ps1 / run_analyzer.sh 가 있는 폴더):
  python tools/pc_analysis.py economic              # 끝날 때까지 (못 한 일이 남으면 할당량 초기화 시각까지 기다렸다가 이어서)
  python tools/pc_analysis.py economic health       # 여러 주제를 동시에 (주제마다 <주제>/keywords.toml·<주제>/.env)
  python tools/pc_analysis.py economic --once       # 한 회차만 (작업 스케줄러가 매일 부를 때). 남은 일이 있으면 종료 코드 3
  python tools/pc_analysis.py economic --dry-run    # 실행할 명령·다음 초기화 시각만 보여 줌
  옵션: --max-rounds 10      최대 회차 (하루 1회차 → 최대 10일)
        --outlier-quota 0 --per-group 0 --top 20 --popular 20   성공 사례·조회수 상위 수집 (할당량 0 = 자동: 검색 수로 계산, 분석기는 오늘 남은 만큼.
                             --per-group 0 = 검색어 전부)
        --daily-quota 9500   분석기가 이미 끝난 날 성공 사례·조회수 상위(주로 댓글 전부)에 쓰는 할당량
        --rerun-analyzer     분석기가 끝났어도 이번에 다시 돌림
        --skip-outliers / --skip-analyzer / --no-push
        --margin-min 10      초기화 뒤 몇 분 더 기다릴지
        --self-test          오프라인 점검 (초기화 시각 계산·회차 판단·이어서 돌리기 흐름)
결과: PC  output/<주제>/result/ (분석기) · <주제>/result/outliers/ (성공 사례) · .yt_work/pc_analysis_<주제>.log (이 도구 로그)
      GitHub <주제>/result/ (분석기 결과 + outliers/ 의 csv·md·json + pc_progress.json). 다른 채널의 자막·댓글 원문·썸네일은 올리지 않음.
로그: [STAGE] [시각] key=value (START·SETUP·OUTLIER·ANALYZER·PUSH·ROUND·WAIT·DONE)
비밀값(.env 의 YOUTUBE_API_KEY·GITHUB_TOKEN)은 읽기만 하고 출력하지 않는다.
※ 연구·교육용 분석 도구. 투자 조언이 아니다.
"""
import argparse
import hashlib
import importlib.util
import json
import logging
import os
import re
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import date, datetime, time as dtime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VERSION = "v1.10"
LOG = logging.getLogger("pc_analysis")
KST = timezone(timedelta(hours=9))
LOCK_STALE_MIN = 30          # 잠금 파일이 이 시간 넘게 갱신되지 않으면 이전 실행이 죽은 것으로 봄
HEARTBEAT_SEC = 300
SLEEP_CHUNK_SEC = 600        # 기다리는 동안 10분마다 벽시계로 다시 계산 (PC 절전에서 깨어나도 맞게)


def log(stage, level=logging.INFO, **kv):
    LOG.log(level, "[%s] [%s] %s", stage, datetime.now(KST).isoformat(timespec="seconds"),
            " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) and ' ' in v else v}" for k, v in kv.items()))


# ---------------------------------------------------------------- 할당량 초기화 시각 (태평양 자정)
def _nth_sunday(year, month, n):
    d = date(year, month, 1)
    d += timedelta(days=(6 - d.weekday()) % 7)        # 첫 일요일
    return d + timedelta(weeks=n - 1)


def _pacific_offset_fallback(utc_dt):
    """tzdata 가 없을 때: 미국 서머타임 규칙 (3월 둘째 일요일 02:00 PST ~ 11월 첫 일요일 02:00 PDT). → UTC 와의 차 (시간)."""
    y = utc_dt.year
    start = datetime.combine(_nth_sunday(y, 3, 2), dtime(10, 0), tzinfo=timezone.utc)    # 02:00 PST = 10:00 UTC
    end = datetime.combine(_nth_sunday(y, 11, 1), dtime(9, 0), tzinfo=timezone.utc)      # 02:00 PDT = 09:00 UTC
    return -7 if start <= utc_dt < end else -8


def next_quota_reset(now_utc, margin_min=10, use_zoneinfo=True):
    """YouTube Data API 일일 할당량이 초기화되는 다음 태평양 자정(+margin) → (UTC 시각, 계산 방법)."""
    try:
        if not use_zoneinfo:
            raise LookupError("규칙 계산 점검")
        from zoneinfo import ZoneInfo
        la = ZoneInfo("America/Los_Angeles")
        local = now_utc.astimezone(la)
        nxt = datetime.combine(local.date() + timedelta(days=1), dtime(0, 0), tzinfo=la)
        return nxt.astimezone(timezone.utc) + timedelta(minutes=margin_min), "zoneinfo"
    except Exception:
        off = _pacific_offset_fallback(now_utc)
        local = now_utc + timedelta(hours=off)
        midnight_local = datetime.combine(local.date() + timedelta(days=1), dtime(0, 0))
        cand = (midnight_local - timedelta(hours=off)).replace(tzinfo=timezone.utc)
        off2 = _pacific_offset_fallback(cand)                      # 서머타임이 바뀌는 날
        if off2 != off:
            cand = (midnight_local - timedelta(hours=off2)).replace(tzinfo=timezone.utc)
        return cand + timedelta(minutes=margin_min), "rule"


DAILY_LIMIT = 10000          # YouTube Data API 하루 할당량 (프로젝트마다)
DAILY_MARGIN = 200           # 남겨 두는 단위 (다른 곳에서 조금 쓸 때·계산 차이)
ANALYZER_MIN_UNITS = 1000    # ⚠️ 분석기를 돌릴 최소 단위 (v1.5: 300 → 1,000 — 모자라면 할당량 초기화 뒤 다음 회차에)


def pacific_day(now_utc):
    """할당량이 세는 날짜 (태평양 시간)."""
    try:
        from zoneinfo import ZoneInfo
        return now_utc.astimezone(ZoneInfo("America/Los_Angeles")).date().isoformat()
    except Exception:
        return (now_utc + timedelta(hours=_pacific_offset_fallback(now_utc))).date().isoformat()


class Ledger:
    """오늘(태평양 날짜) 이 주제가 쓴 YouTube API 단위 — 도구가 보고한 사용량(status.json·run_info.json)을 더함.
    날짜가 바뀌면 0부터. 다른 곳(클라우드 등)에서 같은 키로 쓴 양은 모름 → 그때는 도구가 하루 한도 오류로 멈추고 다음 날 이어서."""

    def __init__(self, folder, now_fn=lambda: datetime.now(timezone.utc)):
        self.p, self.now_fn = ROOT / ".yt_work" / f"quota_{folder}.json", now_fn

    def _load(self):
        day = pacific_day(self.now_fn())
        try:
            d = json.loads(self.p.read_text("utf-8"))
        except (OSError, ValueError):
            d = {}
        return d if d.get("day") == day else {"day": day, "used": 0, "runs": []}

    def used(self):
        return self._load()["used"]

    def add(self, units, what):
        d = self._load()
        d["used"] += int(units or 0)
        d["runs"].append({"what": what, "units": int(units or 0), "kst": datetime.now(KST).isoformat(timespec="minutes")})
        self.p.parent.mkdir(parents=True, exist_ok=True)
        self.p.write_text(json.dumps(d, ensure_ascii=False, indent=1), "utf-8")
        return d["used"]


def _fresh(updated, started_utc):
    try:
        return datetime.fromisoformat(str(updated)) >= started_utc
    except (TypeError, ValueError):
        return False


# ---------------------------------------------------------------- 설정·환경
def _toml():
    try:
        import tomllib
    except ModuleNotFoundError:
        import tomli as tomllib
    return tomllib


def read_paths(folder):
    """분석기 설정에서 결과 위치 → (설정 파일, 분석기 결과 폴더 output/<PROJECT_FOLDER>/<RESULT_FOLDER>, 성공 사례 폴더)."""
    cfg_p = ROOT / folder / "analyzer_config.toml"
    out_dir, proj, res = "output", folder, "result"
    if cfg_p.is_file():
        try:
            flat = {}
            for k, v in _toml().loads(cfg_p.read_text("utf-8")).items():
                flat.update(v if isinstance(v, dict) and k != "KEYWORD_GROUPS" else {k: v})
            out_dir, proj, res = flat.get("OUTPUT_DIR", out_dir), flat.get("PROJECT_FOLDER", proj), flat.get("RESULT_FOLDER", res)
        except Exception as e:
            log("SETUP", logging.WARNING, note="설정 파일을 읽지 못해 기본 위치 사용", error=str(e)[:150])
    base = Path(out_dir).expanduser()
    base = base if base.is_absolute() else ROOT / base
    return cfg_p, base / proj / res, ROOT / folder / "result" / "outliers"


ENV_TEMPLATE = """# YouTube 분석 비밀 키 파일 — 절대 GitHub 에 올리거나 공유하지 마세요
# '=' 뒤에 값을 붙여넣고 저장 (따옴표 필요 없음). 자세히: guides/pc_analysis.md

# [필수] YouTube Data API v3 키 (Google Cloud 콘솔 → API 및 서비스 → 사용자 인증 정보 → API 키)
YOUTUBE_API_KEY=

# [권장] GitHub 토큰 (Fine-grained, 저장소 yeomin1024-ytb, Contents: Read and write) — 비우면 결과는 PC 에만
GITHUB_TOKEN=
"""


def _env_file_value(path, name):
    if not path.is_file():
        return ""
    m = re.search(rf"^[ \t]*{name}[ \t]*=[ \t]*['\"]?([^'\"\s]+)", path.read_text("utf-8-sig", errors="replace"), re.M)
    return m.group(1) if m else ""


def find_secret(name, folder=None):
    """키를 찾는 곳 (분석기 v2.6.0·성공 사례 v1.4 와 같은 순서): <주제>/.env → 환경 변수 <이름>_<주제> → 맨 위 .env → 환경 변수 <이름>.
    → (값, 어디서). 값은 출력하지 않는다."""
    if folder:
        v = _env_file_value(ROOT / folder / ".env", name)
        if v:
            return v, f"{folder}/.env"
        tag = re.sub(r"[^0-9A-Za-z가-힣]+", "_", str(folder)).strip("_").upper()
        v = os.environ.get(f"{name}_{tag}", "").strip()
        if v:
            return v, f"env:{name}_{tag}"
    v = _env_file_value(ROOT / ".env", name)
    if v:
        return v, ".env"
    v = os.environ.get(name, "").strip()
    return (v, f"env:{name}") if v else ("", "-")


def env_has(name, folder=None):
    return bool(find_secret(name, folder)[0])


TOPIC_ENV_TEMPLATE = """# 이 주제({folder})만 쓰는 키 — 보통은 비워 둠 (맨 위 폴더의 .env 키를 여러 주제가 나눠 씀). 절대 GitHub 에 올리거나 공유하지 마세요
# ⚠️ 할당량을 늘리려고 Google Cloud 프로젝트를 주제마다 새로 만드는 것은 YouTube API 개발자 정책 위반입니다('sharding' —
#    키 회수·계정 정지 위험). 여기에는 정말 다른 용도·다른 사람의 프로젝트 키만 넣으세요. 할당량이 더 필요하면 '할당량 증가 신청'.
# 자세히: guides/pc_analysis.md "여러 주제를 동시에"
YOUTUBE_API_KEY=

# (보통 비움 — 맨 위 .env 의 토큰을 씀)
GITHUB_TOKEN=
"""


def ensure_topic_env(folder):
    """<주제>/.env 틀 (없을 때만) — 주제별 키 파일이 어디 있는지 보이게."""
    p = ROOT / folder / ".env"
    if (ROOT / folder).is_dir() and not p.exists():
        p.write_text(TOPIC_ENV_TEMPLATE.format(folder=folder), "utf-8")
        log("SETUP", folder=folder, note="주제별 키 파일 틀을 만듦 (비우면 맨 위 .env 키)", file=f"{folder}/.env")


KEYWORD_LIST_FILE = "keywords.txt"      # 검색어만 한 줄에 하나씩 (v1.7) — 있으면 keywords.toml 의 KEYWORD_GROUPS 대신


def read_keyword_list(path):
    """keywords.txt → 검색어 목록 (분석기 v2.8.0·성공 사례 v1.8 과 같은 규칙: 한 줄에 하나, '#' 줄·빈 줄 무시, 같은 검색어는 한 번,
    UTF-8 — 안 되면 cp949). 파일이 없으면 None."""
    path = Path(path)
    if not path.is_file():
        return None
    raw = path.read_bytes()
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError:
        text = raw.decode("cp949", errors="replace")
    out, seen = [], set()
    for line in text.splitlines():
        k = line.strip().rstrip(",").strip().strip('"').strip("'").strip()
        if k and not k.startswith("#") and "".join(k.split()).lower() not in seen:
            seen.add("".join(k.split()).lower())
            out.append(k)
    return out


def keyword_list(folder, per_group=0):
    """이 주제가 검색할 검색어 (정규화: 띄어쓰기 없앰·소문자, 순서 그대로, 같은 것은 한 번). keywords.txt 가 있으면 그것(per_group 무시),
    없으면 keywords.toml 의 KEYWORD_GROUPS(그룹마다 앞 per_group 개 — 0 이하면 전부) + EXTRA_KEYWORDS. 못 읽으면 None."""
    flat = read_keyword_list(ROOT / folder / KEYWORD_LIST_FILE)
    extra = []
    try:
        d = _toml().loads((ROOT / folder / "keywords.toml").read_text("utf-8"))
        groups = d.get("KEYWORD_GROUPS") or {}
        extra = [str(k) for k in d.get("EXTRA_KEYWORDS") or []]
    except Exception:
        if not flat:
            return None
        groups = {}
    raw = flat if flat else [k for v in groups.values() for k in (v if per_group <= 0 else v[:per_group])]
    out = []
    for k in list(raw) + extra:
        n = "".join(str(k).split()).lower()
        if n and n not in out:
            out.append(n)
    return out


def keywords_fingerprint(folder):
    """검색어 목록의 지문 (분석기가 어떤 검색어로 끝났는지 기억 → 검색어가 바뀌면 분석기를 다시 돌림). 못 읽으면 None."""
    kws = keyword_list(folder)
    return hashlib.sha256("\n".join(sorted(kws)).encode("utf-8")).hexdigest()[:16] if kws else None


def outlier_need(folder, per_group, top, popular, tag_keywords=0):
    """성공 사례 수집이 하루에 끝나려면 필요한 단위: 검색(검색어 수 × 길이 2 × 100 — keywords.txt, 없으면 그룹마다 앞 per_group 개·0 이하면
    전부) + 검색 여유 150 + 영상 정보·구독자 약 100 + 인기 댓글(사례마다 1). 같은 검색어(띄어쓰기·대소문자만 다름)는 한 번. 못 읽으면 4,400."""
    try:
        uniq = keyword_list(folder, per_group) or []
        searches = len(uniq) * 2
        if not searches:
            return 4400
        return (searches + tag_keywords * 2) * 100 + 150 + 100 + top + popular      # 태그 검색어도 길이 2 × 100
    except Exception:
        return 4400


def whisper_summary(folder):
    """음성인식 대기열 기록(.yt_work/whisper_<주제>.json) → 끝남·실패(다시 할 것)·포기."""
    tag = re.sub(r"[^0-9A-Za-z가-힣]+", "_", str(folder)).strip("_") or "topic"
    try:
        st = json.loads((ROOT / ".yt_work" / f"whisper_{tag}.json").read_text("utf-8"))
    except (OSError, ValueError):
        st = {}
    st = {k: v for k, v in st.items() if "#" not in k}      # v1.10: '<영상ID>#full' = 2차(전체) 기록 — 영상 수는 1차 기준으로 셈
    return {"done": sum(1 for v in st.values() if v.get("done")),
            "retry": sum(1 for v in st.values() if not v.get("done") and v.get("attempts", 0) < 3),
            "given_up": sum(1 for v in st.values() if not v.get("done") and v.get("attempts", 0) >= 3)}


def analyzer_budget(cfg_p):
    """설정 파일의 QUOTA_BUDGET (없으면 분석기 기본 9000)."""
    try:
        for k, v in _toml().loads(cfg_p.read_text("utf-8")).items():
            if k == "QUOTA_BUDGET":
                return int(v)
            if isinstance(v, dict) and "QUOTA_BUDGET" in v:
                return int(v["QUOTA_BUDGET"])
    except Exception:
        pass
    return 9000


GET_PIP_URL = "https://bootstrap.pypa.io/get-pip.py"   # pip 공식 설치 스크립트 (ensurepip 이 없을 때만)


def ensure_pip(py=None, runner=subprocess.run):
    """pip 이 없으면 설치 → (ok, how). how: 있음 / ensurepip / get-pip.py / 실패 까닭.
    가상환경(.venv)을 만들다 끊기면 python.exe 만 있고 pip 이 없다 (사용자 PC 2026-10-13: 'No module named pip')."""
    py = py or sys.executable

    def has():
        return runner([py, "-m", "pip", "--version"], capture_output=True, text=True).returncode == 0
    if has():
        return True, "있음"
    log("SETUP", logging.WARNING, note="이 Python 에 pip 이 없음 → ensurepip 로 설치", python=py)
    r = runner([py, "-m", "ensurepip", "--upgrade", "--default-pip"], capture_output=True, text=True)
    if r.returncode == 0 and has():
        log("SETUP", note="pip 설치됨", how="ensurepip")
        return True, "ensurepip"
    err = (r.stderr or r.stdout or "").strip().splitlines()[-1:] or ["?"]
    log("SETUP", logging.WARNING, note="ensurepip 실패 → 공식 get-pip.py 로", error=err[0][:200])
    tmp = ROOT / ".yt_work" / "get-pip.py"
    try:
        import urllib.request
        tmp.parent.mkdir(parents=True, exist_ok=True)
        with urllib.request.urlopen(GET_PIP_URL, timeout=60) as resp:
            tmp.write_bytes(resp.read())
        r = runner([py, str(tmp), "--no-warn-script-location"], capture_output=True, text=True)
        if r.returncode == 0 and has():
            log("SETUP", note="pip 설치됨", how="get-pip.py")
            return True, "get-pip.py"
        why = ((r.stderr or r.stdout or "").strip().splitlines()[-1:] or ["?"])[0][:200]
    except Exception as e:
        why = f"{type(e).__name__}: {e}"[:200]
    finally:
        tmp.unlink(missing_ok=True)
    log("SETUP", logging.ERROR, note="pip 을 설치하지 못함", error=why,
        next_step="실행 폴더의 .venv 폴더를 지우고 run_analyzer 를 다시 실행 (가상환경을 새로 만듦). 그래도 안 되면 python.org 에서 "
                  "Python 을 다시 설치(설치 화면 'pip' 체크)")
    return False, why


def ensure_packages(dry):
    """성공 사례 수집에 필요한 것 (분석기 패키지는 분석기가 처음 실행 때 스스로 설치)."""
    need = []
    if importlib.util.find_spec("youtube_transcript_api") is None:
        need.append("youtube-transcript-api>=1.2")
    if sys.version_info < (3, 11) and importlib.util.find_spec("tomli") is None:
        need.append("tomli>=2.0")
    try:
        from zoneinfo import ZoneInfo
        ZoneInfo("America/Los_Angeles")
    except Exception:
        need.append("tzdata")       # Windows 는 시간대 자료가 없음 (없어도 규칙으로 계산하지만 정확하게)
    if not need:
        return True
    log("SETUP", packages=",".join(need), note="필요한 패키지 설치")
    if dry:
        return True
    if not ensure_pip()[0]:                      # v1.6: pip 이 없는 .venv (만들다 끊긴 경우) → ensurepip / get-pip.py
        return False
    r = subprocess.run([sys.executable, "-m", "pip", "install", "-U", "-q", *need])
    if r.returncode != 0:
        log("SETUP", logging.ERROR, note="패키지 설치 실패 — 위 pip 오류 확인", next_step=f"python -m pip install {' '.join(need)}")
    return r.returncode == 0


class Lock:
    """같은 주제를 두 번 동시에 돌리지 않게 (작업 스케줄러 + 손으로 실행). 5분마다 갱신, 30분 넘게 멈춘 잠금은 무시."""

    def __init__(self, folder):
        self.p = ROOT / ".yt_work" / f"pc_analysis_{folder}.lock"
        self._stop = threading.Event()

    def acquire(self, force=False):
        self.p.parent.mkdir(parents=True, exist_ok=True)
        if self.p.is_file() and not force:
            age_min = (time.time() - self.p.stat().st_mtime) / 60
            if age_min < LOCK_STALE_MIN:
                log("START", logging.ERROR, note="같은 주제 분석이 이미 돌고 있음 — 끝나길 기다리거나, 확실히 멈춘 것이면 --force",
                    lock=str(self.p.relative_to(ROOT)), updated_min_ago=round(age_min, 1))
                return False
        self.p.write_text(json.dumps({"pid": os.getpid(), "started": datetime.now(KST).isoformat(timespec="seconds")}), "utf-8")
        threading.Thread(target=self._beat, daemon=True).start()
        return True

    def _beat(self):
        while not self._stop.wait(HEARTBEAT_SEC):
            try:
                os.utime(self.p, None)
            except OSError:
                pass

    def release(self):
        self._stop.set()
        try:
            self.p.unlink()
        except OSError:
            pass


# ---------------------------------------------------------------- 하위 도구 실행
def run_child(cmd, stage, log_file):
    """하위 도구를 실행하고 출력을 화면·로그 파일에 그대로 (UTF-8). → 종료 코드."""
    env = {**os.environ, "PYTHONIOENCODING": "utf-8", "PYTHONUTF8": "1"}
    log(stage, cmd=" ".join(str(c) if " " not in str(c) else f'"{c}"' for c in cmd[1:]))
    t0 = time.time()
    try:
        p = subprocess.Popen(cmd, cwd=ROOT, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    except OSError as e:
        log(stage, logging.ERROR, error=f"{type(e).__name__}: {e}", next_step="Python 경로·파일이 있는지 확인")
        return 1
    with open(log_file, "a", encoding="utf-8") as lf:
        for raw in p.stdout:
            line = raw.decode("utf-8", errors="replace").rstrip("\r\n")
            print(line, flush=True)
            lf.write(line + "\n")
    code = p.wait()
    log(stage, exit_code=code, minutes=round((time.time() - t0) / 60, 1))
    return code


def outlier_summary(status_p):
    """성공 사례 status.json → 회차 판단용 요약."""
    if not status_p.is_file():
        return {"found": False, "complete": False}
    st = json.loads(status_p.read_text("utf-8"))
    pend = st.get("pending", {})
    retry_tr = [t["id"] for t in st.get("transcript_missing", []) if t.get("retry_elsewhere")]
    return {"found": True, "complete": bool(st.get("complete")), "quota_stop": st.get("quota_stop"),
            "pending_searches": len(pend.get("searches", [])), "pending_videos": pend.get("videos", 0),
            "pending_channels": pend.get("channels", 0), "pending_comments": len(pend.get("comments", [])),
            "ready": bool(st.get("ready")), "deep": st.get("deep", 0), "popular": st.get("popular", 0), "comments_total": st.get("comments_total", 0),
            "comments_complete": st.get("comments_complete"), "cases": st.get("cases"), "quota_used": st.get("quota_used"),
            "transcripts_ok": st.get("transcripts_ok", 0), "retry_transcripts": len(retry_tr),
            "thumbnails_missing": len(st.get("thumbnail_missing", [])), "updated": st.get("updated")}


def analyzer_summary(run_info_p, started_utc):
    """분석기 run_info.json → 이번 회차에 만든 것인지·이월 검색어."""
    if not run_info_p.is_file():
        return {"found": False, "deferred": None}
    ri = json.loads(run_info_p.read_text("utf-8"))
    fin = ri.get("finished_at_utc")
    try:
        fresh = datetime.fromisoformat(fin) >= started_utc
    except (TypeError, ValueError):
        fresh = False
    kw = ri.get("keywords") or {}
    return {"found": True, "fresh": fresh, "run_id": ri.get("run_id"), "searched": kw.get("searched"),
            "deferred": len(kw.get("deferred") or []), "deferred_examples": (kw.get("deferred") or [])[:5],
            "quota_used": (ri.get("youtube_api") or {}).get("quota_used")}      # v1.3: 'used' 로 잘못 읽던 것


# ---------------------------------------------------------------- GitHub 에서 고친 설정·검색어를 PC 로 (v1.7)
SYNC_CONFIG = ("keywords.txt", "keywords.toml", "analyzer_config.toml", "tag_rules.toml", "analysis_rules.toml")   # <주제>/ 아래 — PC 에서 고친 것은 지킴
SYNC_CODE = ("youtube_topic_analyzer.py", "tools/outlier_research.py", "tools/outlier_stats.py", "tools/tag_keywords.py",
             "tools/pc_analysis.py", "tools/web_ui.py", "tools/weekly_analysis.py", "tools/success_analysis.py",
             "run_analyzer.ps1", "run_analyzer.sh")   # 언제나 GitHub 최신


def repo_of(folder):
    """설정 파일의 GITHUB_REPO·GITHUB_BRANCH (없으면 yeomin1024/yeomin1024-ytb · main)."""
    repo, branch = "yeomin1024/yeomin1024-ytb", "main"
    try:
        flat = {}
        for k, v in _toml().loads((ROOT / folder / "analyzer_config.toml").read_text("utf-8")).items():
            flat.update(v if isinstance(v, dict) and k != "KEYWORD_GROUPS" else {k: v})
        repo, branch = str(flat.get("GITHUB_REPO") or repo), str(flat.get("GITHUB_BRANCH") or branch)
    except Exception:
        pass
    return repo, branch


def fetch_repo_file(rel, repo, branch, token):
    """GitHub 에 있는 파일 원본 (토큰이 있으면 API — 비공개 저장소도 됨, 없으면 공개 주소). 없으면 None, 그 밖의 실패는 예외.
    환경 변수 RAW_BASE 가 있으면 그 주소 (실행기 시험용과 같음). 토큰은 머리글로만 — 로그에 쓰지 않음."""
    q = urllib.parse.quote(rel)
    if os.environ.get("RAW_BASE"):
        url, headers = f"{os.environ['RAW_BASE'].rstrip('/')}/{q}", {}
    elif token:
        url = f"https://api.github.com/repos/{repo}/contents/{q}?ref={urllib.parse.quote(branch)}"
        headers = {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github.raw", "X-GitHub-Api-Version": "2022-11-28"}
    else:
        url, headers = f"https://raw.githubusercontent.com/{repo}/{branch}/{q}", {}
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=30) as r:
            return r.read()
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


def _write_atomic(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".sync")
    tmp.write_bytes(data)
    os.replace(tmp, path)          # 새 파일로 바꿔 끼움 — 돌고 있는 bash 실행기도 예전 파일을 끝까지 읽음


def sync_from_github(folder, code=False, dry=False, fetch=None):
    """GitHub 에서 고친 설정·검색어가 PC 에 오게 (사용자: "내가 검색어 변경했는데 안되네"). 회차마다 부름. → {경로: 결과}
    설정(<주제>/keywords.txt·keywords.toml·analyzer_config.toml·tag_rules.toml):
      PC 에 없음 → 받음 / 같음 → 그대로 / PC 파일이 지난번에 받은 그대로(또는 처음) → GitHub 것으로 바꿈 (PC 것은 .bak)
      / PC 에서 고쳤고 GitHub 은 지난번 그대로 → PC 것을 지킴. 받은 내용의 지문은 .yt_work/config_sync.json.
    code=True 면 코드·실행기도 GitHub 최신으로 (지금 도는 pc_analysis.py 는 다음 실행부터). 저장소 작업 폴더(.git)에서는 안 함."""
    if (ROOT / ".git").exists():
        return {"-": "git 작업 폴더 — 건너뜀"}
    repo, branch = repo_of(folder)
    token = find_secret("GITHUB_TOKEN", folder)[0]
    fetch = fetch or (lambda rel: fetch_repo_file(rel, repo, branch, token))
    state_p = ROOT / ".yt_work" / "config_sync.json"
    try:
        state = json.loads(state_p.read_text("utf-8"))
    except (OSError, ValueError):
        state = {}
    files = [(f"{folder}/{n}", "config") for n in SYNC_CONFIG] + ([(c, "code") for c in SYNC_CODE] if code else [])
    res = {}
    for rel, kind in files:
        try:
            remote = fetch(rel)
        except Exception as e:
            res[rel] = f"받기 실패 ({type(e).__name__})"
            continue
        if not remote or not remote.strip():
            res[rel] = "GitHub 에 없음"
            continue
        p = ROOT / rel
        local = p.read_bytes() if p.is_file() else None
        h = hashlib.sha256(remote).hexdigest()
        if local == remote:
            res[rel] = "같음"
        elif kind == "config" and local is not None and state.get(rel) == h:
            res[rel] = "PC 에서 고친 것 지킴"                        # GitHub 은 지난번에 받은 그대로
        else:
            res[rel] = "새로 받음" if local is None else "GitHub 새 판으로 바꿈"
            if not dry:
                try:
                    if kind == "config" and local is not None:
                        _write_atomic(p.with_name(p.name + ".bak"), local)
                    _write_atomic(p, remote)
                except OSError as e:
                    res[rel] = f"바꾸기 실패 ({e.__class__.__name__}) — 다음 회차에 다시"
                    continue
        if not dry:
            state[rel] = h
    if not dry:
        state_p.parent.mkdir(parents=True, exist_ok=True)
        state_p.write_text(json.dumps(state, ensure_ascii=False, indent=1), "utf-8")
    changed = {k: v for k, v in res.items() if v not in ("같음", "GitHub 에 없음")}
    for rel, v in changed.items():
        log("SYNC", logging.WARNING if "실패" in v else logging.INFO, file=rel, result=v,
            note=("지금 도는 이 도구는 다음 실행부터 새 코드" if rel == "tools/pc_analysis.py" and "바꿈" in v else
                  "예전 파일은 .bak" if v == "GitHub 새 판으로 바꿈" and not rel.endswith((".py", ".ps1", ".sh")) else None) or "-")
    log("SYNC", folder=folder, repo=repo, branch=branch, files=len(files), changed=sum(1 for v in changed.values() if "바꿈" in v or v == "새로 받음"),
        kept_pc=sum(1 for v in changed.values() if v == "PC 에서 고친 것 지킴"), failed=sum(1 for v in changed.values() if "실패" in v),
        dry_run=dry)
    return res


def analyzer_done_recently(folder, days=7):
    """앞 회차(이 실행 또는 --once 로 부른 예전 실행)에서 분석기가 이월 검색어 없이 끝났으면 그 시각 (days 일 안), 아니면 None.
    v1.7: 그때의 검색어 지문이 지금과 다르면(검색어를 고쳤으면) None → 분석기를 다시 돌림 (받은 검색은 캐시라 바뀐 검색어만 새로)."""
    p = ROOT / ".yt_work" / f"pc_progress_{folder}.json"
    try:
        prog = json.loads(p.read_text("utf-8"))
        t = datetime.fromisoformat(prog.get("analyzer_done_kst") or "")
    except (OSError, ValueError, TypeError):
        return None
    if datetime.now(KST) - t > timedelta(days=days):
        return None
    now_fp = keywords_fingerprint(folder)
    if prog.get("analyzer_keywords") != now_fp:
        log("ROUND", note="검색어가 바뀌어 분석기를 다시 돌림 (받은 검색은 캐시 — 바뀐 검색어만 새로)", folder=folder,
            before=prog.get("analyzer_keywords") or "-", now=now_fp or "-")
        return None
    return t


def round_verdict(o, a, codes, opts, skip_analyzer=None):
    """이번 회차로 끝났는가 → (complete, 남은 일 목록)."""
    skip_analyzer = opts.skip_analyzer if skip_analyzer is None else skip_analyzer
    left = []
    if not opts.skip_outliers:
        if codes.get("outlier") not in (0, 3):
            left.append(f"성공 사례 수집 오류 (종료 코드 {codes.get('outlier')})")
        if not o.get("complete"):
            left.append(f"성공 사례·조회수 상위: 남은 검색 {o.get('pending_searches', '?')}·영상 정보 {o.get('pending_videos', '?')}·"
                        f"구독자 {o.get('pending_channels', '?')}·댓글 받는 중인 영상 {o.get('pending_comments', '?')}")
        if o.get("retry_transcripts"):
            left.append(f"성공 사례: 네트워크 때문에 못 받은 자막 {o['retry_transcripts']}개")
    if not skip_analyzer:
        if codes.get("analyzer") == "quota":
            left.append("분석기: 오늘 할당량을 다 써서 다음 회차에")
        elif codes.get("analyzer") != 0 or not a.get("fresh"):
            left.append(f"분석기 실패 또는 결과 없음 (종료 코드 {codes.get('analyzer')})")
        elif a.get("deferred"):
            left.append(f"분석기: 이월된 검색어 {a['deferred']}개")
    return not left, left


def write_progress(path_list, info):
    for p in path_list:
        try:
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(json.dumps(info, ensure_ascii=False, indent=1), "utf-8")
        except OSError as e:
            log("ROUND", logging.WARNING, note="진행 상태 파일을 못 씀", file=str(p), error=str(e)[:120])


def one_round(folder, opts, k, runner=run_child, now_fn=lambda: datetime.now(timezone.utc)):
    """한 회차: 성공 사례 → 분석기 → 보충(남은 할당량으로 댓글) → 진행 상태 → 푸시. → (complete, info)."""
    cfg_p, out_dir, outl_dir = read_paths(folder)
    log_file = ROOT / ".yt_work" / f"pc_analysis_{folder}.log"
    log_file.parent.mkdir(parents=True, exist_ok=True)
    started = datetime.now(timezone.utc)
    py = sys.executable
    codes, o, a = {}, {}, {}
    done_at = None if (opts.rerun_analyzer or opts.skip_analyzer) else analyzer_done_recently(folder)
    skip_an = opts.skip_analyzer or done_at is not None
    quota = opts.daily_quota if skip_an else (opts.outlier_quota or outlier_need(folder, opts.per_group, opts.top, opts.popular,
                                                                                    opts.tag_keywords))
    share = getattr(opts, "quota_share", 1) or 1
    budget = DAILY_LIMIT // share - DAILY_MARGIN                # 이 주제가 오늘 쓸 수 있는 단위 (같은 키 주제 수로 나눔)
    ledger = Ledger(folder, now_fn)

    def left_today():
        return budget - ledger.used()
    log("ROUND", round=k, folder=folder, started=started.astimezone(KST).isoformat(timespec="minutes"),
        analyzer="건너뜀 (" + (done_at.isoformat(timespec="minutes") + " 에 끝남)" if done_at else "--skip-analyzer)") if skip_an else "돌림",
        outlier_quota=quota, today_budget=budget, today_used=ledger.used())

    def outlier_pass(q, stage):
        cmd = [py, "tools/outlier_research.py", folder, "--per-group", str(opts.per_group), "--top", str(opts.top),
               "--popular", str(opts.popular), "--tag-keywords", str(opts.tag_keywords), "--quota", str(q)]
        if opts.dry_run:
            log(stage, dry_run=True, cmd=" ".join(cmd[1:]))
            return 0, outlier_summary(outl_dir / "status.json")
        t0 = datetime.now(timezone.utc)
        code = runner(cmd, stage, log_file)
        res = outlier_summary(outl_dir / "status.json")
        if _fresh(res.get("updated"), t0):
            log(stage, today_used=ledger.add(res.get("quota_used"), stage.lower()), units=res.get("quota_used"))
        log(stage, **{key: v for key, v in res.items() if key != "updated"})
        return code, res
    def push(stage, why):
        has = (out_dir / "README.md").is_file() or (outl_dir / "summary.md").is_file()
        if opts.no_push or opts.dry_run:
            if opts.dry_run:
                log(stage, dry_run=True, note=why)
            return None
        if has and env_has("GITHUB_TOKEN", folder):
            log(stage, note=why)
            return runner([py, "youtube_topic_analyzer.py", "--config", str(cfg_p.relative_to(ROOT)), "--push-only"]
                          + (["--skip-install"] if opts.child else []), stage, log_file)
        log(stage, logging.WARNING, note="푸시 건너뜀", reason="올릴 결과 없음" if not has else "GITHUB_TOKEN 없음 (.env)",
            hint="결과는 PC 에 있음 — 토큰을 넣고 python youtube_topic_analyzer.py --config "
                 f"{cfg_p.relative_to(ROOT).as_posix()} --push-only")
        return None
    ran = []                                              # 이번 회차에 실제로 돈 도구 (아무것도 안 돌았으면 올리지 않음)
    if not opts.skip_outliers:
        q = min(quota, left_today())
        if q < 100 and not opts.dry_run:
            log("OUTLIER", logging.WARNING, note="오늘 이 주제 할당량을 다 씀 → 다음 회차에", today_used=ledger.used(), budget=budget)
            codes["outlier"], o = 3, outlier_summary(outl_dir / "status.json")
        else:
            codes["outlier"], o = outlier_pass(q, "OUTLIER")
            ran.append("outlier")
            if not skip_an:                               # 분석기는 오래 걸리니 성공 사례 결과(자막·댓글·받은 자료 표)부터 올림
                codes["push_first"] = push("PUSH_FIRST", "성공 사례 결과 먼저 올림 (분석기 전)")
    if not skip_an:
        cmd = [py, "youtube_topic_analyzer.py", "--config", str(cfg_p.relative_to(ROOT)), "--no-push", "--no-open",
               "--no-video", "--defer-whisper"] + (["--skip-install"] if opts.child else [])   # 영상 안 받음·음성인식은 ⑥에서 (v1.4)
        cfg_budget = analyzer_budget(cfg_p)
        an_q = min(cfg_budget // share, left_today())       # 같은 키 주제끼리 나누고, 오늘 이미 쓴 양을 뺌
        if an_q < ANALYZER_MIN_UNITS and not opts.dry_run:      # v1.5: 300 → 1,000 (빈 결과 대신 다음 회차)
            log("ANALYZER", logging.WARNING, note="오늘 이 주제 할당량을 다 씀 → 분석기는 다음 회차에", today_used=ledger.used(), budget=budget)
            codes["analyzer"], a = "quota", {"found": False, "deferred": None}
        else:
            if an_q != cfg_budget:
                cmd += ["--quota-budget", str(an_q)]
            ran.append("analyzer")
            codes["analyzer"] = 0 if opts.dry_run else runner(cmd, "ANALYZER", log_file)
            if opts.dry_run:
                log("ANALYZER", dry_run=True, cmd=" ".join(cmd[1:]))
            a = analyzer_summary(out_dir / "run_info.json", started)
            if a.get("fresh") and not opts.dry_run:
                ledger.add(a.get("quota_used"), "analyzer")
            log("ANALYZER", **{key: v for key, v in a.items() if key != "deferred_examples"},
                examples=",".join(a.get("deferred_examples") or []) or "-", today_used=ledger.used())
    # 보충: 남은 일이 있고 오늘 할당량이 남았으면 한 번 더 (검색은 캐시 → 남은 단위가 댓글·남은 검색에)
    if not opts.skip_outliers and o and not o.get("complete") and codes.get("outlier") in (0, 3) and not opts.dry_run:
        q2 = left_today()
        if q2 >= 100:
            log("TOPUP", note="오늘 남은 할당량으로 성공 사례·조회수 상위 보충 (주로 댓글)", quota=q2)
            codes["topup"], o = outlier_pass(q2, "TOPUP")
            ran.append("topup")
            codes["outlier"] = codes["topup"]
        else:
            log("TOPUP", note="오늘 남은 할당량 없음 → 다음 회차", left=q2)
    complete, left = round_verdict(o, a, codes, opts, skip_an) if not opts.dry_run else (True, [])
    if not skip_an and codes.get("analyzer") == 0 and a.get("fresh") and not a.get("deferred"):
        done_at = datetime.now(KST)                           # 분석기 끝 → 다음 회차부터 건너뛰고 할당량을 댓글에
    reset_utc, how = next_quota_reset(datetime.now(timezone.utc), opts.margin_min)
    info = {"tool": f"pc_analysis.py {VERSION}", "folder": folder, "round": k, "started_kst": started.astimezone(KST).isoformat(timespec="minutes"),
            "finished_kst": datetime.now(KST).isoformat(timespec="minutes"), "exit_codes": codes, "outliers": o, "analyzer": a,
            "complete": complete, "ready": bool(o.get("ready")) if o else None, "left": left, "analyzer_skipped": skip_an,
            "quota_today": {"pacific_day": pacific_day(now_fn()), "used": ledger.used(), "budget": budget},
            "analyzer_done_kst": done_at.isoformat(timespec="minutes") if done_at else None,
            "analyzer_keywords": keywords_fingerprint(folder) if done_at else None,      # v1.7: 이 검색어로 끝남 (바뀌면 다시)
            "next_round_kst": None if complete else reset_utc.astimezone(KST).isoformat(timespec="minutes"),
            "note": "연구·교육용. 할당량 초기화 = 태평양 자정 (한국 오후 4시, 미국 표준시 기간엔 5시)"}
    targets = [ROOT / ".yt_work" / f"pc_progress_{folder}.json"]
    if (out_dir / "README.md").is_file():
        targets.append(out_dir / "pc_progress.json")         # GitHub <주제>/result/pc_progress.json 으로 올라감
    if not opts.dry_run:
        write_progress(targets, info)
    codes["push"] = push("PUSH", "이번 회차 결과 올림") if ran or opts.dry_run else None
    # ⑥ 음성인식 대기열: 자막 없는 영상을 하나씩 (할당량 0) — 하나 끝날 때마다 바로 올림 (분석기 --whisper-queue)
    if not opts.no_whisper:
        wcmd = [py, "youtube_topic_analyzer.py", "--config", str(cfg_p.relative_to(ROOT)), "--whisper-queue"] + \
            (["--skip-install"] if opts.child else []) + (["--no-push"] if opts.no_push else [])
        if opts.dry_run:
            log("WHISPER", dry_run=True, cmd=" ".join(wcmd[1:]))
        else:
            codes["whisper"] = runner(wcmd, "WHISPER", log_file)
            info["whisper"] = whisper_summary(folder)
            info["exit_codes"] = codes
            write_progress([ROOT / ".yt_work" / f"pc_progress_{folder}.json"], info)
            log("WHISPER", **info["whisper"])
    log("ROUND", round=k, complete=complete, ready=info["ready"], today_used=ledger.used(), budget=budget, left=" / ".join(left) or "-",
        next_round=info["next_round_kst"] or "-", reset_calc=how)
    return complete, info


def wait_until(target_utc, now_fn=lambda: datetime.now(timezone.utc), sleep_fn=time.sleep):
    """벽시계 기준으로 기다림 (10분마다 다시 계산 — 절전에서 깨어나도 늦지 않게). 30분마다 남은 시간 로그."""
    last_log = None
    while True:
        left = (target_utc - now_fn()).total_seconds()
        if left <= 0:
            return
        if last_log is None or last_log - left >= 1800:
            log("WAIT", until_kst=target_utc.astimezone(KST).isoformat(timespec="minutes"), hours_left=round(left / 3600, 2),
                note="PC 를 켜 두세요 (절전이면 깨어난 뒤 바로 이어서)")
            last_log = left
        sleep_fn(min(SLEEP_CHUNK_SEC, left))


def run(opts, runner=run_child, now_fn=lambda: datetime.now(timezone.utc), sleep_fn=time.sleep):
    folder = opts.folder
    if not (ROOT / folder / "analyzer_config.toml").is_file():
        log("START", logging.ERROR, note="주제 폴더의 설정 파일이 없음", expected=f"{folder}/analyzer_config.toml",
            next_step="run_analyzer.ps1 / run_analyzer.sh 로 받거나 --folder 확인")
        return 1
    if not opts.dry_run:
        ensure_topic_env(folder)
    if not env_has("YOUTUBE_API_KEY", folder) and not opts.dry_run:
        env_p = ROOT / ".env"
        if not env_p.exists():
            env_p.write_text(ENV_TEMPLATE, "utf-8")
        log("START", logging.ERROR, note="YOUTUBE_API_KEY 없음 — .env(또는 이 주제의 .env)를 메모장으로 열어 키를 넣고 저장한 뒤 다시 실행",
            env_file=f".env 또는 {folder}/.env", guide="guides/pc_analysis.md")
        return 1
    if not opts.child and not ensure_packages(opts.dry_run):
        return 1
    lock = Lock(folder)
    if not opts.dry_run and not lock.acquire(opts.force):
        return 2
    try:
        for k in range(1, opts.max_rounds + 1):
            if not getattr(opts, "no_sync", False):            # v1.7: 회차마다 GitHub 에서 고친 설정·검색어(·코드)를 받음
                try:
                    sync_from_github(folder, code=not opts.child, dry=opts.dry_run)
                except Exception as e:
                    log("SYNC", logging.WARNING, note="GitHub 에서 설정을 받지 못함 — PC 에 있는 파일로 계속", error=f"{type(e).__name__}: {e}"[:200])
            complete, info = one_round(folder, opts, k, runner, now_fn)
            if complete:
                log("DONE", folder=folder, rounds=k, note="못 한 일 없음 — 끝" if not opts.dry_run else "dry-run")
                return 0
            if opts.once:
                log("DONE", folder=folder, rounds=k, complete=False, next_round=info["next_round_kst"],
                    note="--once: 남은 일은 다음 실행 때 (작업 스케줄러가 매일 부르면 자동)")
                return 3
            if k == opts.max_rounds:
                break
            reset_utc, _ = next_quota_reset(now_fn(), opts.margin_min)
            wait_until(reset_utc, now_fn, sleep_fn)
        log("DONE", logging.WARNING, folder=folder, rounds=opts.max_rounds, complete=False,
            note="최대 회차까지 돌았지만 남은 일이 있음 — 로그 확인", log=f".yt_work/pc_analysis_{folder}.log")
        return 3
    except KeyboardInterrupt:
        log("DONE", logging.WARNING, note="사용자가 멈춤 (Ctrl+C) — 받은 것은 캐시에 남아 다시 실행하면 이어서")
        return 130
    finally:
        if not opts.dry_run:
            lock.release()


# ---------------------------------------------------------------- 여러 주제를 동시에
FORWARD_FLAGS = ("once", "dry_run", "skip_outliers", "skip_analyzer", "no_push", "force", "rerun_analyzer", "no_whisper", "no_sync")
FORWARD_VALUES = ("max_rounds", "per_group", "top", "popular", "tag_keywords", "margin_min", "log_level")


def child_cmd(opts, folder, quota_div=1):
    """주제 하나를 돌리는 자식 프로세스 명령 (같은 키를 쓰는 주제 수 quota_div 로 성공 사례 할당량을 나눔)."""
    cmd = [sys.executable, "tools/pc_analysis.py", folder, "--child", "--quota-share", str(quota_div),
           "--outlier-quota", str(opts.outlier_quota // quota_div), "--daily-quota", str(opts.daily_quota // quota_div)]
    for f in FORWARD_FLAGS:
        if getattr(opts, f, False):
            cmd.append("--" + f.replace("_", "-"))
    for f in FORWARD_VALUES:
        cmd += ["--" + f.replace("_", "-"), str(getattr(opts, f))]
    return cmd


def spawn_prefixed(cmd, prefix, lock):
    """자식 프로세스를 띄우고 출력 줄 앞에 [주제] 를 붙여 화면에. → Popen (끝나기를 기다리는 쪽은 부모)."""
    env = {**os.environ, "PYTHONIOENCODING": "utf-8", "PYTHONUTF8": "1"}
    p = subprocess.Popen(cmd, cwd=ROOT, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    def pump():
        for raw in p.stdout:
            line = raw.decode("utf-8", errors="replace").rstrip("\r\n")
            with lock:
                print(f"[{prefix}] {line}", flush=True)
    threading.Thread(target=pump, daemon=True).start()
    return p


def run_parallel(opts, folders, spawn=None, setup=None):
    """주제 여러 개를 동시에: 패키지 준비 한 번 → 주제마다 자식 프로세스 (잠금·로그·진행 파일·대기는 주제마다 따로).
    → 종료 코드 (1 오류가 하나라도 / 3 남은 일 / 2 이미 도는 주제 / 0 모두 끝)."""
    import hashlib
    ok_folders = []
    for f in dict.fromkeys(folders):
        if (ROOT / f / "analyzer_config.toml").is_file():
            ok_folders.append(f)
        else:
            log("START", logging.ERROR, folder=f, note="설정 파일이 없어 이 주제는 건너뜀", expected=f"{f}/analyzer_config.toml",
                next_step="Claude 에게 '<주제> 검색어 만들어줘' 또는 python youtube_topic_analyzer.py --topic <주제> --folder <폴더> --init-config")
    if not ok_folders:
        return 1
    groups = {}                                       # 키(지문)별 주제 — 같은 키면 하루 할당량을 나눠 씀
    for f in ok_folders:
        if not opts.dry_run:
            ensure_topic_env(f)
        key, src = find_secret("YOUTUBE_API_KEY", f)
        fp = hashlib.sha256(key.encode()).hexdigest()[:8] if key else "none"
        groups.setdefault(fp, []).append(f)
        log("START", folder=f, key_source=src, key_id=fp, github_token="있음" if env_has("GITHUB_TOKEN", f) else "없음")
    div = {}
    for fp, fs in groups.items():
        for f in fs:
            div[f] = len(fs)
        if fp != "none" and len(fs) > 1:
            log("START", folders=",".join(fs), note=f"같은 YouTube 키를 {len(fs)}개 주제가 나눠 씀 → 하루 10,000단위를 주제마다 1/{len(fs)} "
                "(성공 사례·분석기 할당량 모두 나눔, 남은 일은 다음 날 이어서). 할당량이 더 필요하면 할당량 증가 신청 — 프로젝트를 늘리는 것은 정책 위반")
    if setup is None:
        def setup():
            if not ensure_packages(opts.dry_run):
                return False
            if opts.dry_run:
                return True
            return subprocess.run([sys.executable, "youtube_topic_analyzer.py", "--setup-only"], cwd=ROOT).returncode == 0
    if not setup():
        log("SETUP", logging.ERROR, note="패키지 준비 실패 — 위 오류 확인", next_step="python youtube_topic_analyzer.py --setup-only")
        return 1
    lock = threading.Lock()
    spawn = spawn or spawn_prefixed
    procs = {}
    for f in ok_folders:
        cmd = child_cmd(opts, f, div[f])
        log("START", folder=f, cmd=" ".join(cmd[1:]))
        procs[f] = spawn(cmd, f, lock)
    try:
        codes = {f: p.wait() for f, p in procs.items()}
    except KeyboardInterrupt:
        for p in procs.values():
            p.terminate()
        log("DONE", logging.WARNING, note="사용자가 멈춤 (Ctrl+C) — 주제마다 받은 것은 캐시에 남아 다시 실행하면 이어서")
        return 130
    for f, c in codes.items():
        log("DONE", folder=f, exit_code=c, meaning={0: "끝", 3: "남은 일 있음(다음 실행이 이어서)", 2: "이미 도는 중"}.get(c, "오류 — 로그 확인"),
            log=f".yt_work/pc_analysis_{f}.log")
    vals = list(codes.values()) + ([1] if len(ok_folders) < len(dict.fromkeys(folders)) else [])
    if any(c not in (0, 2, 3) for c in vals):
        return 1
    return 3 if 3 in vals else (2 if 2 in vals else 0)


# ---------------------------------------------------------------- 오프라인 점검
def self_test():
    ok = True

    def check(name, cond, **kv):
        nonlocal ok
        ok &= bool(cond)
        log("SELFTEST", logging.INFO if cond else logging.ERROR, check=name, result="PASS" if cond else "FAIL", **kv)

    u = lambda *a: datetime(*a, tzinfo=timezone.utc)
    cases = [(u(2026, 10, 13, 6, 30), u(2026, 10, 13, 7, 10)),     # 한국 15:30 → 16:10 (서머타임)
             (u(2026, 10, 13, 7, 30), u(2026, 10, 14, 7, 10)),     # 한국 16:30 (이미 지남) → 다음 날 16:10
             (u(2026, 12, 1, 3, 0), u(2026, 12, 1, 8, 10)),        # 겨울: 한국 12:00 → 17:10
             (u(2026, 11, 1, 6, 0), u(2026, 11, 1, 7, 10)),        # 10/31 23:00 PDT → 11/1 00:00 PDT (서머타임 끝나는 날 자정)
             (u(2026, 11, 1, 8, 0), u(2026, 11, 2, 8, 10)),        # 11/1 01:00 PDT → 11/2 00:00 PST (그날 02:00 에 표준시로)
             (u(2026, 3, 8, 7, 0), u(2026, 3, 8, 8, 10)),          # 3/7 23:00 PST → 3/8 00:00 PST
             (u(2026, 3, 8, 9, 0), u(2026, 3, 9, 7, 10))]          # 3/8 01:00 PST → 3/9 00:00 PDT (그날 02:00 에 서머타임)
    for now, want in cases:
        for zi in (True, False):
            got, how = next_quota_reset(now, 10, use_zoneinfo=zi)
            check(f"초기화 시각 {now:%m-%d %H:%M}Z ({'zoneinfo' if zi else '규칙'})", got == want, got=got.isoformat(),
                  want=want.isoformat(), how=how)
    import tempfile
    import types
    global ROOT
    old_root = ROOT
    tmp = Path(tempfile.mkdtemp())
    ROOT = tmp
    try:
        (tmp / "t").mkdir()
        (tmp / "t" / "analyzer_config.toml").write_text('[topic]\nPROJECT_FOLDER = "t"\n', "utf-8")
        (tmp / ".env").write_text("YOUTUBE_API_KEY=x\nGITHUB_TOKEN=y\n", "utf-8")
        cfg_p, out_dir, outl = read_paths("t")
        calls, day = [], {"n": 0}

        def fake_runner(cmd, stage, log_file):          # 1일째: 할당량이 모자라 남음, 2일째: 끝
            calls.append(stage)
            if stage in ("OUTLIER", "TOPUP"):
                outl.mkdir(parents=True, exist_ok=True)
                done = day["n"] >= 1
                (outl / "status.json").write_text(json.dumps({"complete": done, "quota_stop": None if done else "run_budget",
                                                              "pending": {"searches": [] if done else ["a (medium)"], "videos": 0,
                                                                          "channels": 0, "comments": []},
                                                              "deep": 5, "transcripts_ok": 5, "transcript_missing": []}), "utf-8")
                return 0 if done else 3
            if stage == "ANALYZER":
                out_dir.mkdir(parents=True, exist_ok=True)
                (out_dir / "README.md").write_text("x", "utf-8")
                (out_dir / "run_info.json").write_text(json.dumps({
                    "finished_at_utc": datetime.now(timezone.utc).isoformat(), "run_id": f"r{day['n']}",
                    "keywords": {"searched": 40 if day["n"] == 0 else 50, "deferred": [] if day["n"] >= 1 else ["k1", "k2"]}}), "utf-8")
                return 0
            if stage == "PUSH":
                day["n"] += 1                            # 회차 끝 → 다음 날
                return 0
            return 1
        clock = {"t": u(2026, 10, 13, 6, 30)}
        slept = []

        def fake_sleep(s):
            slept.append(s)
            clock["t"] += timedelta(seconds=s)
        opts = types.SimpleNamespace(folder="t", once=False, dry_run=False, max_rounds=3, per_group=2, top=20, outlier_quota=4000,
                                     skip_outliers=False, skip_analyzer=False, no_push=False, margin_min=10, force=False,
                                     popular=20, daily_quota=9500, rerun_analyzer=False, child=False, log_level="INFO", quota_share=1,
                                     tag_keywords=5, no_whisper=False, no_sync=True)     # 시험은 GitHub 에 묻지 않음
        global ensure_packages
        real_ensure, ensure_packages = ensure_packages, (lambda dry: True)
        try:
            code = run(opts, fake_runner, lambda: clock["t"], fake_sleep)
        finally:
            ensure_packages = real_ensure
        check("2회차에 끝남 (exit 0)·1회차에 남은 할당량으로 보충", code == 0 and calls.count("OUTLIER") == 2 and calls[:3] == ["OUTLIER", "ANALYZER", "TOPUP"],
              calls=",".join(calls))
        check("1회차 뒤 초기화 시각까지 기다림 (16:10 KST)", clock["t"] >= u(2026, 10, 13, 7, 10) and sum(slept) > 0,
              waited_h=round(sum(slept) / 3600, 2))
        prog = json.loads((out_dir / "pc_progress.json").read_text("utf-8"))
        check("pc_progress.json (결과 폴더) complete", prog["complete"] is True and prog["round"] == 2)
        check("잠금 파일 정리", not (tmp / ".yt_work" / "pc_analysis_t.lock").exists())
        # --once: 남은 일이 있으면 3
        day["n"], calls[:] = 0, []
        (tmp / ".yt_work" / "pc_progress_t.json").unlink()     # 앞 시나리오의 '분석기 끝남' 기록 지움
        opts.once = True
        ensure_packages = lambda dry: True
        try:
            code = run(opts, fake_runner, lambda: clock["t"], fake_sleep)
        finally:
            ensure_packages = real_ensure
        prog = json.loads((tmp / ".yt_work" / "pc_progress_t.json").read_text("utf-8"))
        check("--once 남은 일 → exit 3·다음 회차 시각", code == 3 and prog["complete"] is False and prog["next_round_kst"]
              and any("이월된 검색어 2개" in x for x in prog["left"]), left=" / ".join(prog["left"]))
        # 잠금: 다른 실행이 돌고 있으면 2
        lk = Lock("t")
        lk.acquire()
        opts.once = False
        ensure_packages = lambda dry: True
        try:
            code = run(opts, fake_runner, lambda: clock["t"], fake_sleep)
        finally:
            ensure_packages = real_ensure
            lk.release()
        check("이미 돌고 있으면 exit 2", code == 2)
        # v1.1: 분석기는 1회차에 끝, 댓글이 남음 → 2회차는 분석기를 건너뛰고 하루 할당량(9500)을 댓글에
        (tmp / ".yt_work" / "pc_progress_t.json").unlink()
        cmds = []

        def fake_runner2(cmd, stage, log_file):
            cmds.append((stage, cmd))
            if stage in ("OUTLIER", "TOPUP"):
                big = "9500" in cmd
                (outl / "status.json").write_text(json.dumps({"complete": big, "quota_stop": None if big else "run_budget",
                                                              "pending": {"searches": [], "videos": 0, "channels": 0,
                                                                          "comments": [] if big else ["v1", "v2"]},
                                                              "deep": 20, "popular": 20, "transcript_missing": []}), "utf-8")
                return 0 if big else 3
            if stage == "ANALYZER":
                (out_dir / "run_info.json").write_text(json.dumps({"finished_at_utc": datetime.now(timezone.utc).isoformat(),
                                                                   "keywords": {"searched": 50, "deferred": []}}), "utf-8")
                return 0
            return 0
        ensure_packages = lambda dry: True
        try:
            code = run(opts, fake_runner2, lambda: clock["t"], fake_sleep)
        finally:
            ensure_packages = real_ensure
        stages = [st for st, _ in cmds]
        q2 = [c for st, c in cmds if st == "OUTLIER"][-1]
        # v1.2: 여러 주제를 동시에 — 같은 키를 쓰는 주제끼리 할당량 나눔, 설정 없는 주제는 건너뜀, 종료 코드 모으기
        for f, key in (("p1", "AIzaSAME"), ("p2", "AIzaSAME"), ("p3", "AIzaOTHER")):
            (tmp / f).mkdir()
            (tmp / f / "analyzer_config.toml").write_text(f'[topic]\nPROJECT_FOLDER = "{f}"\n', "utf-8")
            (tmp / f / ".env").write_text(f"YOUTUBE_API_KEY={key}\n", "utf-8")
        spawned = {}

        class FakeP:
            def __init__(self, code):
                self.code = code

            def wait(self):
                return self.code

            def terminate(self):
                pass

        def fake_spawn(cmd, prefix, lk):
            spawned[prefix] = cmd
            return FakeP({"p1": 0, "p2": 3, "p3": 0}[prefix])
        pcode = run_parallel(opts, ["p1", "p2", "p3", "nope"], spawn=fake_spawn, setup=lambda: True)
        q = {f: int(c[c.index("--outlier-quota") + 1]) for f, c in spawned.items()}
        check("여러 주제 동시에: 같은 키는 할당량 나눔·다른 키는 그대로·자식 --child", q == {"p1": 2000, "p2": 2000, "p3": 4000}
              and all("--child" in c for c in spawned.values()) and pcode == 1, quotas=q, exit_code=pcode)
        pcode2 = run_parallel(opts, ["p1", "p2", "p3"], spawn=fake_spawn, setup=lambda: True)
        check("여러 주제 동시에: 남은 일 있는 주제가 있으면 exit 3", pcode2 == 3)
        check("같은 키 주제는 --quota-share 2, 다른 키는 1", spawned["p1"][spawned["p1"].index("--quota-share") + 1] == "2"
              and spawned["p3"][spawned["p3"].index("--quota-share") + 1] == "1")
        (tmp / "p1" / "analyzer_config.toml").write_text('[topic]\nPROJECT_FOLDER = "p1"\n[advanced]\nQUOTA_BUDGET = 6000\n', "utf-8")
        check("설정의 QUOTA_BUDGET 읽기", analyzer_budget(tmp / "p1" / "analyzer_config.toml") == 6000
              and analyzer_budget(tmp / "p3" / "analyzer_config.toml") == 9000)
        check("분석기 끝난 뒤 회차는 분석기 건너뜀·할당량 9500·--popular 전달", code == 0
              and stages == ["OUTLIER", "PUSH_FIRST", "ANALYZER", "TOPUP", "PUSH", "WHISPER", "OUTLIER", "PUSH", "WHISPER"]
              and q2[q2.index("--quota") + 1] == "9500" and "--popular" in q2, stages=",".join(stages))
        # v1.3: 오늘 쓴 양 장부 — 성공 사례 3,900 + 분석기 5,700 보고 → 보충은 남은 200(=10,000-200-9,600)만, 다 쓰면 보충 안 함
        (tmp / ".yt_work" / "pc_progress_t.json").unlink(missing_ok=True)
        (tmp / ".yt_work" / "quota_t.json").unlink(missing_ok=True)
        cmds3 = []

        def fake_runner3(cmd, stage, log_file):
            cmds3.append((stage, cmd))
            now_iso = datetime.now(timezone.utc).isoformat()
            if stage in ("OUTLIER", "TOPUP"):
                qa = int(cmd[cmd.index("--quota") + 1])
                (outl / "status.json").write_text(json.dumps({"complete": False, "ready": True, "updated": now_iso,
                                                              "quota_used": min(qa, 3900 if stage == "OUTLIER" else qa),
                                                              "pending": {"searches": [], "videos": 0, "channels": 0, "comments": ["v1"]},
                                                              "transcript_missing": []}), "utf-8")
                return 3
            if stage == "ANALYZER":
                (out_dir / "run_info.json").write_text(json.dumps({"finished_at_utc": now_iso, "keywords": {"searched": 50, "deferred": ["k"]},
                                                                   "youtube_api": {"quota_used": 5700}}), "utf-8")
                return 0
            return 0
        opts.once = True
        ensure_packages = lambda dry: True
        try:
            run(opts, fake_runner3, lambda: clock["t"], fake_sleep)
            topup = [c for st_, c in cmds3 if st_ == "TOPUP"]
            led = json.loads((tmp / ".yt_work" / "quota_t.json").read_text("utf-8"))
            check("보충 = 오늘 남은 할당량 (9,800 − 3,900 − 5,700 = 200)", len(topup) == 1 and topup[0][topup[0].index("--quota") + 1] == "200"
                  and led["used"] == 9800, used=led["used"])
            cmds3.clear()
            run(opts, fake_runner3, lambda: clock["t"], fake_sleep)          # 같은 날 또: 이미 다 씀 → 도구를 돌리지 않음
            check("같은 날 다시 실행하면 이미 쓴 양을 빼고 (다 썼으면 안 돌림·안 올림, 음성인식만)", [st_ for st_, _ in cmds3] == ["WHISPER"],
                  stages=",".join(st_ for st_, _ in cmds3))
        finally:
            ensure_packages = real_ensure
            opts.once = False
        (tmp / "t" / "keywords.toml").write_text('[KEYWORD_GROUPS]\n"a" = ["1","2","3"]\n"b" = ["4"]\n', "utf-8")
        check("성공 사례 자동 할당량 = 검색 (2+1)×2×100 + 250 + 사례 40", outlier_need("t", 2, 20, 20) == 600 + 250 + 40
              and outlier_need("nope", 2, 20, 20) == 4400, need=outlier_need("t", 2, 20, 20))
        # v1.4: 성공 사례 결과가 있으면 분석기 전에 먼저 올림, 분석기는 --no-video --defer-whisper, 끝에 음성인식 대기열
        (tmp / ".yt_work" / "quota_t.json").unlink(missing_ok=True)
        (tmp / ".yt_work" / "pc_progress_t.json").unlink(missing_ok=True)
        (outl / "summary.md").write_text("x", "utf-8")
        cmds4 = []
        opts.once = True
        ensure_packages = lambda dry: True
        try:
            run(opts, lambda cmd, stage, lf: cmds4.append((stage, cmd)) or (3 if stage == "OUTLIER" else 0), lambda: clock["t"], fake_sleep)
        finally:
            ensure_packages = real_ensure
            opts.once = False
        st4 = [x for x, _ in cmds4]
        an4 = next(c for x, c in cmds4 if x == "ANALYZER")
        ou4 = next(c for x, c in cmds4 if x == "OUTLIER")
        check("결과 먼저: OUTLIER → PUSH_FIRST → ANALYZER(--no-video --defer-whisper) → … → PUSH → WHISPER",
              st4[:3] == ["OUTLIER", "PUSH_FIRST", "ANALYZER"] and st4[-2:] == ["PUSH", "WHISPER"] and "--no-video" in an4
              and "--defer-whisper" in an4 and ou4[ou4.index("--tag-keywords") + 1] == "5", stages=",".join(st4))
        check("자동 할당량에 태그 검색 포함 (+5×2×100)", outlier_need("t", 2, 20, 20, 5) == 600 + 1000 + 250 + 40)
        (tmp / "t" / "keywords.toml").write_text('[KEYWORD_GROUPS]\n"a" = ["1","2","3"]\n"b" = ["4", "1 "]\n', "utf-8")
        check("v1.5 --per-group 0 = 검색어 전부 (같은 검색어 한 번): 4개 × 2 × 100 + 250 + 40", outlier_need("t", 0, 20, 20) == 800 + 250 + 40,
              need=outlier_need("t", 0, 20, 20))
        check("분석기 사용량 읽기 (quota_used)", analyzer_summary(out_dir / "run_info.json", u(2000, 1, 1)).get("quota_used") == 5700)
        # v1.6: pip 이 없는 .venv → ensurepip (가짜 실행기: pip 은 ensurepip 뒤에만 있음)
        pip_state, calls_p = {"has": False}, []

        def fake_pip(cmd, **kw):
            calls_p.append(cmd[2] if len(cmd) > 2 else cmd[-1])
            if cmd[1:3] == ["-m", "ensurepip"]:
                pip_state["has"] = True
                return subprocess.CompletedProcess(cmd, 0, "", "")
            return subprocess.CompletedProcess(cmd, 0 if pip_state["has"] else 1, "", "" if pip_state["has"] else "No module named pip")
        r1 = ensure_pip("py", fake_pip)
        r2 = ensure_pip("py", fake_pip)
        check("v1.6 pip 이 없으면 ensurepip 로 설치, 있으면 그대로", r1 == (True, "ensurepip") and r2 == (True, "있음")
              and calls_p == ["pip", "ensurepip", "pip", "pip"], calls=",".join(calls_p))
        # v1.7: keywords.txt (한 줄에 하나) 가 있으면 그것이 검색어 — 그룹·per_group 무시
        (tmp / "t" / "keywords.txt").write_text("# 내 검색어\n재테크\n주식 투자\n\n주식투자\nETF\n", "utf-8")
        check("v1.7 keywords.txt = 검색어 (주석·빈 줄·같은 검색어 무시, 그룹 무시): 3개 × 2 × 100 + 250 + 40",
              keyword_list("t", 2) == ["재테크", "주식투자", "etf"] and outlier_need("t", 2, 20, 20) == 600 + 250 + 40,
              kws=",".join(keyword_list("t", 2) or []), need=outlier_need("t", 2, 20, 20))
        # v1.7: 검색어가 바뀌면 분석기를 다시 (지문)
        fp1 = keywords_fingerprint("t")
        prog_p = tmp / ".yt_work" / "pc_progress_t.json"
        prog_p.write_text(json.dumps({"analyzer_done_kst": datetime.now(KST).isoformat(), "analyzer_keywords": fp1}), "utf-8")
        same = analyzer_done_recently("t")
        (tmp / "t" / "keywords.txt").write_text("재테크\n주식투자\n", "utf-8")       # ETF 를 지움
        changed = analyzer_done_recently("t")
        prog_p.unlink()
        check("v1.7 검색어가 그대로면 분석기 건너뜀, 바뀌면 다시 돌림", same is not None and changed is None and keywords_fingerprint("t") != fp1)
        # v1.7: GitHub 에서 고친 설정·검색어를 PC 로 (지난번에 받은 지문으로 PC 수정과 GitHub 수정을 가림)
        gh = {"t/keywords.txt": b"A\nB\n", "t/keywords.toml": None, "t/analyzer_config.toml": None, "t/tag_rules.toml": None,
              "tools/outlier_research.py": b"print(2)\n"}
        fetch = lambda rel: gh.get(rel)
        (tmp / "t" / "keywords.txt").write_text("OLD\n", "utf-8")                       # 처음 (기록 없음) — 사용자 PC 상황
        r_a = sync_from_github("t", fetch=fetch)["t/keywords.txt"]
        txt_a, bak_a = (tmp / "t" / "keywords.txt").read_bytes(), (tmp / "t" / "keywords.txt.bak").read_bytes()
        r_b = sync_from_github("t", fetch=fetch)["t/keywords.txt"]                          # 같음
        (tmp / "t" / "keywords.txt").write_bytes(b"A\nB\nPC\n")                          # PC 에서 고침, GitHub 은 그대로
        r_c = sync_from_github("t", fetch=fetch)["t/keywords.txt"]
        txt_c = (tmp / "t" / "keywords.txt").read_bytes()
        gh["t/keywords.txt"] = b"A\nC\n"                                                    # GitHub 에서 고침
        r_d = sync_from_github("t", fetch=fetch)["t/keywords.txt"]
        txt_d = (tmp / "t" / "keywords.txt").read_bytes()
        (tmp / "tools").mkdir(exist_ok=True)
        (tmp / "tools" / "outlier_research.py").write_text("print(1)\n", "utf-8")
        r_e = sync_from_github("t", code=True, fetch=fetch)
        (tmp / ".git").mkdir()
        r_f = sync_from_github("t", fetch=fetch)
        (tmp / ".git").rmdir()
        check("v1.7 GitHub 수정 → PC: 처음·다르면 GitHub 것(.bak) / 같음 / PC 에서 고친 것 지킴 / GitHub 이 또 바뀌면 GitHub 것 / 코드는 늘 최신 / git 폴더는 안 함",
              r_a == "GitHub 새 판으로 바꿈" and txt_a == b"A\nB\n" and bak_a == b"OLD\n" and r_b == "같음"
              and r_c == "PC 에서 고친 것 지킴" and txt_c == b"A\nB\nPC\n" and r_d == "GitHub 새 판으로 바꿈" and txt_d == b"A\nC\n"
              and r_e["tools/outlier_research.py"] == "GitHub 새 판으로 바꿈" and (tmp / "tools" / "outlier_research.py").read_bytes() == b"print(2)\n"
              and not (tmp / "tools" / "outlier_research.py.bak").exists() and r_e["t/keywords.toml"] == "GitHub 에 없음" and "-" in r_f,
              a=r_a, b=r_b, c=r_c, d=r_d)
    finally:
        ROOT = old_root
        import shutil
        shutil.rmtree(tmp, ignore_errors=True)
    log("SELFTEST", result="ALL PASS" if ok else "FAIL")
    return 0 if ok else 1


def main(argv=None):
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass
    ap = argparse.ArgumentParser(description="PC 분석 실행기 — 성공 사례 + 주제 분석, 할당량이 초기화되면 남은 부분부터 자동으로 이어서")
    ap.add_argument("folders", nargs="*", default=["economic"], help="주제 폴더 (기본 economic). 여러 개면 동시에 (예: economic health)")
    ap.add_argument("--child", action="store_true", help=argparse.SUPPRESS)      # 여러 주제를 동시에 돌릴 때 부모가 붙임
    ap.add_argument("--quota-share", type=int, default=1, help=argparse.SUPPRESS)  # 같은 키를 쓰는 주제 수 (분석기 할당량 나눔)
    ap.add_argument("--once", action="store_true", help="한 회차만 (작업 스케줄러용). 남은 일이 있으면 종료 코드 3")
    ap.add_argument("--dry-run", action="store_true", help="실행할 명령과 다음 초기화 시각만")
    ap.add_argument("--max-rounds", type=int, default=10)
    ap.add_argument("--outlier-quota", type=int, default=0,
                    help="성공 사례 수집 할당량 (0 = 자동: 검색 수 × 100 + 여유 — 첫날 검색·인기 댓글까지 끝나게, 분석기는 나머지)")
    ap.add_argument("--per-group", type=int, default=0, help="검색어 그룹마다 성공 사례 검색에 쓸 수 (0 = 전부, 기본)")
    ap.add_argument("--top", type=int, default=20)
    ap.add_argument("--popular", type=int, default=20, help="구독자 수 상관없이 조회수 상위 영상 수 (댓글 전부)")
    ap.add_argument("--daily-quota", type=int, default=9500, help="분석기가 이미 끝난 날 성공 사례·조회수 상위에 쓰는 할당량")
    ap.add_argument("--rerun-analyzer", action="store_true", help="분석기가 끝났어도 이번에 다시 돌림")
    ap.add_argument("--tag-keywords", type=int, default=0, help="잘된 영상의 태그에서 더 고를 검색어 수 (기본 0 = 내가 적은 검색어만)")
    ap.add_argument("--no-whisper", action="store_true", help="음성인식 대기열을 돌리지 않음")
    ap.add_argument("--skip-outliers", action="store_true")
    ap.add_argument("--skip-analyzer", action="store_true")
    ap.add_argument("--no-push", action="store_true")
    ap.add_argument("--no-sync", action="store_true", help="회차마다 GitHub 에서 설정·검색어·코드를 받지 않음 (PC 파일만)")
    ap.add_argument("--margin-min", type=int, default=10)
    ap.add_argument("--force", action="store_true", help="잠금 파일이 있어도 실행 (이전 실행이 확실히 멈췄을 때)")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    opts = ap.parse_args(argv)
    logging.basicConfig(level=getattr(logging, opts.log_level), format="%(message)s", stream=sys.stdout)
    if opts.self_test:
        return self_test()
    reset_utc, how = next_quota_reset(datetime.now(timezone.utc), opts.margin_min)
    folders = [f for x in opts.folders for f in str(x).split(",") if f.strip()]
    if len(folders) > 1:
        log("START", tool=f"pc_analysis.py {VERSION}", mode="parallel", folders=",".join(folders), once=opts.once, dry_run=opts.dry_run,
            next_quota_reset_kst=reset_utc.astimezone(KST).isoformat(timespec="minutes"))
        return run_parallel(opts, folders)
    opts.folder = folders[0]
    log("START", tool=f"pc_analysis.py {VERSION}", folder=opts.folder, child=opts.child, once=opts.once, dry_run=opts.dry_run, max_rounds=opts.max_rounds,
        outlier_quota=opts.outlier_quota, daily_quota=opts.daily_quota, per_group=opts.per_group, top=opts.top, popular=opts.popular,
        python=sys.version.split()[0],
        next_quota_reset_kst=reset_utc.astimezone(KST).isoformat(timespec="minutes"), reset_calc=how,
        youtube_key=find_secret("YOUTUBE_API_KEY", opts.folder)[1], github_token="있음" if env_has("GITHUB_TOKEN", opts.folder) else "없음")
    return run(opts)


if __name__ == "__main__":
    sys.exit(main())
