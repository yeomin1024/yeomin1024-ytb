#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.2 — 2026-10-13 — 여러 주제를 동시에(병렬로) (사용자 지시: "동시에 병렬로 다른 주제 분석도 가능하도록 해야해 그럼 검색어 설정 파일,
#          키설정 파일도 여러개 있어야 겠지"): `pc_analysis.py economic health` → 패키지 준비를 한 번 하고 주제마다 따로 프로세스를 띄움
#          (화면 줄 앞에 [주제], 주제마다 잠금·로그·진행 파일·할당량 대기). 검색어는 <주제>/keywords.toml, 키는 <주제>/.env
#          (없으면 맨 위 .env) — 같은 키를 쓰는 주제끼리 하루 할당량을 나눔(성공 사례·분석기 QUOTA_BUDGET 모두 ÷ 주제 수).
#          ⚠️ 할당량을 늘리려고 프로젝트를 여러 개 만드는 것은 YouTube API 정책 위반('sharding') — 기본은 키 하나를 나눠 씀
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
        --outlier-quota 4000 --per-group 2 --top 20 --popular 20   성공 사례·조회수 상위 수집 (분석기가 도는 날: 분석기 QUOTA_BUDGET 과 합쳐 10,000 이하)
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
import importlib.util
import json
import logging
import os
import re
import subprocess
import sys
import threading
import time
from datetime import date, datetime, time as dtime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VERSION = "v1.2"
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
            "deep": st.get("deep", 0), "popular": st.get("popular", 0), "comments_total": st.get("comments_total", 0),
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
            "quota_used": (ri.get("youtube_api") or {}).get("used")}


def analyzer_done_recently(folder, days=7):
    """앞 회차(이 실행 또는 --once 로 부른 예전 실행)에서 분석기가 이월 검색어 없이 끝났으면 그 시각 (days 일 안), 아니면 None."""
    p = ROOT / ".yt_work" / f"pc_progress_{folder}.json"
    try:
        t = datetime.fromisoformat(json.loads(p.read_text("utf-8")).get("analyzer_done_kst") or "")
    except (OSError, ValueError, TypeError):
        return None
    return t if datetime.now(KST) - t <= timedelta(days=days) else None


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
        if codes.get("analyzer") != 0 or not a.get("fresh"):
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


def one_round(folder, opts, k, runner=run_child):
    """한 회차: 성공 사례 → 분석기 → 진행 상태 → 푸시. → (complete, info)."""
    cfg_p, out_dir, outl_dir = read_paths(folder)
    log_file = ROOT / ".yt_work" / f"pc_analysis_{folder}.log"
    log_file.parent.mkdir(parents=True, exist_ok=True)
    started = datetime.now(timezone.utc)
    py = sys.executable
    codes, o, a = {}, {}, {}
    done_at = None if (opts.rerun_analyzer or opts.skip_analyzer) else analyzer_done_recently(folder)
    skip_an = opts.skip_analyzer or done_at is not None
    quota = opts.daily_quota if skip_an else opts.outlier_quota
    log("ROUND", round=k, folder=folder, started=started.astimezone(KST).isoformat(timespec="minutes"),
        analyzer="건너뜀 (" + (done_at.isoformat(timespec="minutes") + " 에 끝남)" if done_at else "--skip-analyzer)") if skip_an else "돌림",
        outlier_quota=quota)
    if not opts.skip_outliers:
        cmd = [py, "tools/outlier_research.py", folder, "--per-group", str(opts.per_group), "--top", str(opts.top),
               "--popular", str(opts.popular), "--quota", str(quota)]
        codes["outlier"] = 0 if opts.dry_run else runner(cmd, "OUTLIER", log_file)
        if opts.dry_run:
            log("OUTLIER", dry_run=True, cmd=" ".join(cmd[1:]))
        o = outlier_summary(outl_dir / "status.json")
        log("OUTLIER", **{key: v for key, v in o.items() if key != "updated"})
    if not skip_an:
        cmd = [py, "youtube_topic_analyzer.py", "--config", str(cfg_p.relative_to(ROOT)), "--no-push", "--no-open"] + \
            (["--skip-install"] if opts.child else [])     # 여러 주제를 동시에: 패키지 준비는 부모가 한 번
        share = getattr(opts, "quota_share", 1) or 1
        if share > 1:                                       # 같은 키를 쓰는 주제끼리 분석기 할당량도 나눔
            cmd += ["--quota-budget", str(analyzer_budget(cfg_p) // share)]
        codes["analyzer"] = 0 if opts.dry_run else runner(cmd, "ANALYZER", log_file)
        if opts.dry_run:
            log("ANALYZER", dry_run=True, cmd=" ".join(cmd[1:]))
        a = analyzer_summary(out_dir / "run_info.json", started)
        log("ANALYZER", **{key: v for key, v in a.items() if key != "deferred_examples"},
            examples=",".join(a.get("deferred_examples") or []) or "-")
    complete, left = round_verdict(o, a, codes, opts, skip_an) if not opts.dry_run else (True, [])
    if not skip_an and codes.get("analyzer") == 0 and a.get("fresh") and not a.get("deferred"):
        done_at = datetime.now(KST)                           # 분석기 끝 → 다음 회차부터 건너뛰고 할당량을 댓글에
    reset_utc, how = next_quota_reset(datetime.now(timezone.utc), opts.margin_min)
    info = {"tool": f"pc_analysis.py {VERSION}", "folder": folder, "round": k, "started_kst": started.astimezone(KST).isoformat(timespec="minutes"),
            "finished_kst": datetime.now(KST).isoformat(timespec="minutes"), "exit_codes": codes, "outliers": o, "analyzer": a,
            "complete": complete, "left": left, "analyzer_skipped": skip_an,
            "analyzer_done_kst": done_at.isoformat(timespec="minutes") if done_at else None,
            "next_round_kst": None if complete else reset_utc.astimezone(KST).isoformat(timespec="minutes"),
            "note": "연구·교육용. 할당량 초기화 = 태평양 자정 (한국 오후 4시, 미국 표준시 기간엔 5시)"}
    targets = [ROOT / ".yt_work" / f"pc_progress_{folder}.json"]
    if (out_dir / "README.md").is_file():
        targets.append(out_dir / "pc_progress.json")         # GitHub <주제>/result/pc_progress.json 으로 올라감
    if not opts.dry_run:
        write_progress(targets, info)
    if not opts.no_push and not opts.dry_run:
        if (out_dir / "README.md").is_file() and env_has("GITHUB_TOKEN", folder):
            codes["push"] = runner([py, "youtube_topic_analyzer.py", "--config", str(cfg_p.relative_to(ROOT)), "--push-only"]
                                   + (["--skip-install"] if opts.child else []), "PUSH", log_file)
        else:
            log("PUSH", logging.WARNING, note="푸시 건너뜀", reason="분석기 결과 없음" if not (out_dir / "README.md").is_file() else "GITHUB_TOKEN 없음 (.env)",
                hint="결과는 PC 에 있음 — 토큰을 넣고 python youtube_topic_analyzer.py --config "
                     f"{cfg_p.relative_to(ROOT).as_posix()} --push-only")
    log("ROUND", round=k, complete=complete, left=" / ".join(left) or "-", next_round=info["next_round_kst"] or "-", reset_calc=how)
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
            complete, info = one_round(folder, opts, k, runner)
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
FORWARD_FLAGS = ("once", "dry_run", "skip_outliers", "skip_analyzer", "no_push", "force", "rerun_analyzer")
FORWARD_VALUES = ("max_rounds", "per_group", "top", "popular", "margin_min", "log_level")


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
            if stage == "OUTLIER":
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
                                     popular=20, daily_quota=9500, rerun_analyzer=False, child=False, log_level="INFO", quota_share=1)
        global ensure_packages
        real_ensure, ensure_packages = ensure_packages, (lambda dry: True)
        try:
            code = run(opts, fake_runner, lambda: clock["t"], fake_sleep)
        finally:
            ensure_packages = real_ensure
        check("2회차에 끝남 (exit 0)", code == 0 and calls.count("OUTLIER") == 2, calls=",".join(calls))
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
            if stage == "OUTLIER":
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
        check("분석기 끝난 뒤 회차는 분석기 건너뜀·할당량 9500·--popular 전달", code == 0 and stages == ["OUTLIER", "ANALYZER", "PUSH", "OUTLIER", "PUSH"]
              and q2[q2.index("--quota") + 1] == "9500" and "--popular" in q2, stages=",".join(stages))
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
    ap.add_argument("--outlier-quota", type=int, default=4000, help="성공 사례 수집 할당량 (분석기 QUOTA_BUDGET 과 합쳐 10,000 이하)")
    ap.add_argument("--per-group", type=int, default=2)
    ap.add_argument("--top", type=int, default=20)
    ap.add_argument("--popular", type=int, default=20, help="구독자 수 상관없이 조회수 상위 영상 수 (댓글 전부)")
    ap.add_argument("--daily-quota", type=int, default=9500, help="분석기가 이미 끝난 날 성공 사례·조회수 상위에 쓰는 할당량")
    ap.add_argument("--rerun-analyzer", action="store_true", help="분석기가 끝났어도 이번에 다시 돌림")
    ap.add_argument("--skip-outliers", action="store_true")
    ap.add_argument("--skip-analyzer", action="store_true")
    ap.add_argument("--no-push", action="store_true")
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
