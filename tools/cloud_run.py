#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.6 — 2026-10-28 — explore --alltime-only: 보통 검색은 받아 둔 결과 그대로(캐시가 지났어도 0단위) 쓰고 ③ 기간 없는 검색만
#          (할당량이 orr.ALLTIME_RESERVE 넘게 남을 때만 — web_ui v2.5). 사용자 지시 2026-10-28 "3은 할당량 남으면 진행하도록 해".
# (v1.5.1 — 2026-10-21 — '-' 로 시작하는 영상 ID(예: -Fl1y9riPs4)를 check·uncheck·approve 에 주면 argparse 가 옵션으로 읽어 멈추던 것
#          (exit 2 — 132개 승인이 시작도 못 함) → 11자 영상 ID 꼴이면서 아는 옵션이 아닌 낱말은 ID 로 읽음. `--` 를 앞에 둬도 됨. 다른 동작 그대로
# (v1.5 — 2026-10-21 — 푼 추천 기억: uncheck 한 영상을 <주제>/result/web/dismissed.json(쇼츠 shorts_dismissed.json — 캐시 묶음에 함께)에 남기고
#          explore 뒤에 다시 풂 (check 하면 목록에서 지움). 웹 화면 탐색은 바로 앞 목록의 체크만 기억해, 1주 ↔ 26주처럼 기간을 바꾸면 예전에 푼
#          영화·정치 영상이 다시 체크됐음 (2026-10-21 — 사용자 지시 "주제 탐색 시 … 업로드 기간 대비 조회수가 높은 영상은 모두 분석 대상에 넣어" 작업 중))
# (v1.4 — 2026-10-20 — 캐시 묶음 나누기: cache.tgz 가 45MB 를 넘으면 cache.tgz.001·.002 … 로 나눠 씀 (GitHub 은 파일 하나 50MB 넘으면 경고,
#          100MB 넘으면 푸시 거부 — 음악 캐시가 채널 기준선 1,038곳·쇼츠 탐색 뒤 56.8MB). 45MB 이하면 예전처럼 cache.tgz 하나 (다른 주제는 그대로).
#          cache-load 는 둘 다 읽음 (cache.json 'parts' 가 있으면 조각을 이어 붙여 풂). 묶음 안 내용·풀 곳은 그대로.
# (v1.3 — 2026-10-16 — captions: 승인한 영상 중 대본이 없는 것의 자막만 다시 (할당량 0, 사용자 지시 2026-10-16 "일단 음성인식은 보류하고
#          시간되면 이어서 진행해"). 웹 화면은 승인한 영상을 목록에서 숨겨 자막을 다시 시도할 길이 음성인식뿐인데, 승인 185개 중 78개는 PC 에
#          자막 도구가 없어(ModuleNotFoundError) 시도조차 못 했고 59개는 연결 실패(유튜브 로봇 확인 → www.google.com/sorry 로 넘김 — 막힌 주소)
#          였음. 같은 outlier_research.transcript() (요청 사이 1.5~3초·연속 2번 막히면 6시간 쉼)로 받고, 받으면 deep_case 와 같은
#          파일(transcript.json·transcript.txt)과 metadata 칸(transcript_lang·transcript_status·말 속도 등 speech_stats)만 고침. 자막 서버 차단
#          (IpBlocked·RequestBlocked·429)은 규칙대로 음성인식 몫이라 다시 요청하지 않음. 쉬기가 시작되면 멈추고 남은 것은 상태를 그대로 둠)
# (v1.2 — 2026-10-16 — 탐색 캐시를 저장소에 (사용자 지시 2026-10-16 "저장소에 올려"): 클라우드 컨테이너가 새로 뜨면 .cache(검색 결과·영상 정보·
#          채널 목록 — 주식 탐색 한 바퀴 ≈ 11,000단위)가 사라져 검색을 다시 해야 했음 → <주제>/cloud_cache/cache.tgz (+ cache.json 목록)
#          · 켤 때 .cache 가 비어 있으면 저절로 풂 · 할당량을 쓰는 명령(explore·approve·baseline·comments·demand·resume·startup·wait-reset)과
#          check·uncheck 뒤에 저절로 묶음 · cache-save / cache-load 명령. result/ 밖에 두는 까닭: PC 분석기 올리기(_copy_local_outliers full)가
#          저장소의 result/outliers 를 PC 것과 똑같이 덮어씀. 썸네일 캐시(.cache/thumbs)는 i.ytimg.com 에서 할당량 0 으로 다시 받으므로 뺌
# (v1.1 — 2026-10-16 — ① list·approve 가 웹 화면처럼 이미 분석에 쓴 영상(W_·01_·P01_ / 쇼츠 S_)을 뺌 (GET /api/explore 와 같은 규칙 —
#          v1.0 은 목록에 승인한 102개가 섞였고, 그대로 승인하면 이미 받은 자료를 다시 받았음) ② foreign on|off — 웹 화면 [외국 영상도]와 같음
#          (사용자 지시 2026-10-16 "잠깐 주식 주제는 외국 영상도 포함해" — 설정 파일만 고치고 GitHub 에는 Claude 가 git 으로)
# (v1.0 — 2026-10-16 — 신규: 클라우드(Claude Code)에서 웹 화면 없이 분석 돌리기 (사용자 지시 2026-10-16: "이 환경은 이제 저장소에 있는
#          주식 주제 (stock 경로)를 유튜브 분석 코드 실행해서 분석하는 환경이야 한번 해봐" · "아마 분석 코드가 ui로 되어 있을텐데 너가 분석하기
#          쉽도록 수정해도 돼 분석 로직은 변경하지말고"). 웹 화면(tools/web_ui.py)의 작업 함수 — 탐색·승인·채널 기준선·댓글 이어 받기·자동완성·
#          분석 다시·남은 것 이어서·쇼츠 — 를 그대로 부르는 명령줄 껍데기. 분석·추천(체크)·할당량 계산은 web_ui.py 와 같은 코드다.
#          클라우드에서 바꾼 것 (분석 로직 아님):
#          ① 올리기: 기본은 분석기 --push-only(따로 clone) 대신 이 작업 폴더에 남김 → Claude 가 git 으로 main 에 (--push analyzer 면 예전처럼)
#          ② FRESH_START 보호: 클라우드 컨테이너에는 PC 표시(.yt_work/fresh_start_<주제>.txt)가 없어 web_ui·pc_analysis 가 켤 때 git 에 있는
#             승인 결과(W_…)를 .yt_work/old/ 로 옮겨 버림 → 사례 폴더가 이미 있으면 옮기지 않고 표시만 씀
#          ③ 음성인식은 시작하지 않음 (클라우드엔 Whisper·소리 받기 길이 없음 — 남은 수만 보여 줌)
# ※ 연구·교육용 분석 도구. 투자 권유가 아니다.
"""클라우드 분석 실행기 — 웹 화면 없이 같은 작업을 명령으로.

  python3 tools/cloud_run.py stock status                  # 할당량·탐색 목록·승인 수·남은 것
  python3 tools/cloud_run.py stock explore --weeks 26      # [탐색] (검색어마다 4~20분·20분 넘음, 검색 1번 100단위, 캐시 7일~)
  python3 tools/cloud_run.py stock list --unchecked        # 5번 칸 목록 (배수 높은 순, ✔ = 체크(추천))
  python3 tools/cloud_run.py stock check ID … / uncheck ID …
  python3 tools/cloud_run.py stock approve                 # [승인] — 체크한 영상 (ID 를 주면 그 영상만)
  python3 tools/cloud_run.py stock baseline | comments | demand | analyze | resume | startup
  python3 tools/cloud_run.py stock explore --shorts / list --shorts / approve --shorts   # 쇼츠
  python3 tools/cloud_run.py stock captions [--limit N]     # 대본 없는 승인 영상의 자막만 다시 (할당량 0 — 연결 실패·시도 못 한 것만)
  python3 tools/cloud_run.py stock cache-save | cache-load  # 탐색 캐시 ↔ <주제>/cloud_cache/cache.tgz (보통은 저절로)
  python3 tools/cloud_run.py stock foreign on|off          # [외국 영상도] (analyzer_config.toml INCLUDE_FOREIGN)
  python3 tools/cloud_run.py stock wait-reset [--then resume]   # 태평양 자정 +10분까지 기다림 (할당량 초기화)

로그: [STAGE] [시각] key=value (web_ui·outlier_research 와 같은 꼴) — 화면과 .yt_work/cloud_run_<주제>.log
끝 줄: [RESULT] [시각] cmd=… result={JSON}
"""
import argparse
import hashlib
import io
import json
import logging
import os
import re
import sys
import tarfile
import time
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import pc_analysis as pc                 # noqa: E402
import web_ui as w                       # noqa: E402

VERSION = "v1.6"
VIDEO_ID_RX = re.compile(r"-[0-9A-Za-z_-]{10}")   # v1.5.1: '-' 로 시작하는 11자 영상 ID (argparse 가 옵션으로 읽지 않게)
ROOT = pc.ROOT
LOG = logging.getLogger("cloud")
_STEP = {"text": None, "at": 0.0}
CACHE_DIR = "cloud_cache"               # v1.2: <주제>/cloud_cache/cache.tgz — result/ 밖 (PC 올리기가 result/outliers 를 PC 것으로 덮어씀)
CACHE_SKIP = ("thumbs",)               # .cache/thumbs — 할당량 0 으로 다시 받음
CACHE_PART_BYTES = 45_000_000           # v1.4: 묶음이 이보다 크면 cache.tgz.001·.002 … 로 나눔 (GitHub 파일 경고 50MB·거부 100MB)
CACHE_SAVE_AFTER = ("explore", "approve", "baseline", "comments", "demand", "resume", "startup", "wait-reset", "check", "uncheck")
STEP_EVERY_S = 5.0                       # 진행 줄은 바뀔 때마다가 아니라 5초에 한 번 (검색·댓글 줄이 수백 개라 — 끝 줄은 늘 남김)


def log(stage, level=logging.INFO, **kv):
    w.log(stage, level, **kv)


# ---------------------------------------------------------------- 준비
def setup_logging(t, level):
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass
    fmt = logging.Formatter("%(message)s")
    root = logging.getLogger()
    root.setLevel(getattr(logging, level))
    (ROOT / ".yt_work").mkdir(exist_ok=True)
    for h in (logging.StreamHandler(sys.stdout), logging.FileHandler(ROOT / ".yt_work" / f"cloud_run_{t}.log", encoding="utf-8")):
        h.setFormatter(fmt)
        root.addHandler(h)


def load_tools():
    """web_ui.main 이 하는 불러오기만 (서버·브라우저·GitHub 동기화·잠금 화면 없이)."""
    import outlier_research as _orr
    import weekly_analysis as _wa
    w.orr, w.wa = _orr, _wa
    try:
        import shorts_analysis as _sh
        w.sh = _sh
    except Exception as e:
        log("START", logging.WARNING, note="쇼츠 분석 도구를 못 불러옴 — 쇼츠 명령만 꺼짐", error=f"{type(e).__name__}: {e}"[:160])


def guard_fresh_start(t):
    """FRESH_START 보호 (v1.0 ②): 사례 폴더(W_·S_·01_·P01_)가 이미 있으면(= git 에서 받은 결과) 옮기지 않고 PC 표시만 씀."""
    want = str(pc._topic_flat(t).get("FRESH_START") or "").strip()
    if not want:
        return
    mark = ROOT / ".yt_work" / f"fresh_start_{t}.txt"
    have = mark.read_text("utf-8").strip() if mark.is_file() else ""
    if have == want:
        return
    od = w.out_dir(t)
    cases = [d for d in od.iterdir() if d.is_dir() and w.CASE_RX.match(d.name)] if od.is_dir() else []
    cases += list(w.shorts_out(t).glob("S_*"))
    if cases:
        mark.parent.mkdir(parents=True, exist_ok=True)
        mark.write_text(want + "\n", "utf-8")
        log("RESET", topic=t, fresh_start=want, cases=len(cases),
            note="git 에 받은 결과가 있어 옮기지 않음 — 표시만 씀 (클라우드 컨테이너에는 PC 표시가 없음)")
    else:
        pc.fresh_start(t)


def progress_step(orig):
    """web_ui.step 을 감싸 진행을 로그로 (화면의 '진행' 칸 대신). 멈춤 검사 등 원래 동작은 그대로."""
    def step(text, done=None, total=None):
        orig(text, done, total)
        now = time.monotonic()
        last = done is not None and total is not None and total and done >= total
        if text != _STEP["text"] and (last or now - _STEP["at"] >= STEP_EVERY_S):
            _STEP.update(text=text, at=now)
            log("STEP", text=text[:120], done=done if done is not None else "-", total=total if total is not None else "-")
    return step


def local_push(t, message):
    """올리기 (v1.0 ①): 결과는 이미 이 작업 폴더(<주제>/result/…)에 있음 → Claude 가 git 으로 main 에. 분석기 clone 올리기는 하지 않음."""
    note = "클라우드: 작업 폴더에 저장 — git 으로 main 에 올릴 것 (커밋 메시지 예: " + message[:80] + ")"
    log("PUSH", topic=t, mode="local", note=note)
    return {"pushed": False, "push_note": note, "materials": "작업 폴더 (git 에 아직 안 올림)"}


def no_whisper(t, why=""):
    n = w.whisper_pending(t, fresh=True)
    log("WHISPER", logging.WARNING, topic=t, pending=n, why=why or "-",
        note="클라우드에서는 음성인식을 시작하지 않음 (Whisper·소리 받기 없음) — PC 웹 화면의 [음성인식 시작]으로")
    return False, f"클라우드 — 음성인식 안 함 (남은 {n}개)"


# ---------------------------------------------------------------- 탐색 캐시 ↔ 저장소 (v1.2)
def cache_sources(t):
    """(PC 폴더, 묶음 안 이름) — 탐색 캐시(검색·영상 정보·채널·업로드 목록·자동완성·공급 확인·쇼츠)와 탐색 목록·체크·승인 목록."""
    return [(w.out_dir(t) / ".cache", "result/outliers/.cache"), (ROOT / t / "result" / "web", "result/web")]


def cache_kind(name, rel):
    """목록(cache.json)에 적을 갈래: web/… · .cache 의 하위 폴더 · search_/uploads_/supply_ · 영상 정보(이름 11자) · 그 밖 파일 이름."""
    if name.endswith("web"):
        return "web"
    if len(rel.parts) > 1:
        return rel.parts[0]
    stem = rel.stem
    for pre in ("search_", "uploads_", "supply_"):
        if stem.startswith(pre):
            return pre.rstrip("_")
    return "video" if len(stem) == 11 else rel.name


def cache_paths(t):
    d = ROOT / t / CACHE_DIR
    return d / "cache.tgz", d / "cache.json"


def cache_parts(arc):
    """v1.4: 나눠 쓴 조각 cache.tgz.001, .002 … (이름 순 = 이어 붙일 순서)."""
    return sorted(arc.parent.glob(arc.name + ".[0-9][0-9][0-9]"))


def _write_atomic(path, data):
    tmp = path.with_name(path.name + f".{os.getpid()}.tmp")
    tmp.write_bytes(data)
    os.replace(tmp, path)


def cache_save(t, why=""):
    arc, man = cache_paths(t)
    files, kinds = [], {}
    for base, name in cache_sources(t):
        for f in sorted(base.rglob("*")) if base.is_dir() else []:
            rel = f.relative_to(base)
            if not f.is_file() or ".tmp" in f.name or (name.endswith(".cache") and rel.parts[0] in CACHE_SKIP):
                continue
            files.append((f, f"{name}/{rel.as_posix()}"))
            k = cache_kind(name, rel)
            kinds[k] = kinds.get(k, 0) + 1
    if not files:
        log("CACHE", logging.WARNING, topic=t, note="묶을 캐시 없음 — 건너뜀")
        return {"cache_saved": False}
    arc.parent.mkdir(parents=True, exist_ok=True)
    tmp = arc.with_name(arc.name + f".{os.getpid()}.tmp")
    with tarfile.open(tmp, "w:gz", compresslevel=9) as tf:
        for f, name in files:
            tf.add(f, arcname=name, recursive=False)
    data = tmp.read_bytes()
    old_parts = cache_parts(arc)
    if len(data) > CACHE_PART_BYTES:            # v1.4: 큰 묶음은 조각으로 (조각마다 새로 쓴 뒤 남은 예전 조각·cache.tgz 를 지움)
        parts = [arc.with_name(f"{arc.name}.{i + 1:03d}") for i in range((len(data) + CACHE_PART_BYTES - 1) // CACHE_PART_BYTES)]
        for i, part in enumerate(parts):
            _write_atomic(part, data[i * CACHE_PART_BYTES:(i + 1) * CACHE_PART_BYTES])
        tmp.unlink()
        for old in old_parts + [arc]:
            if old not in parts and old.exists():
                old.unlink()
    else:
        parts = []
        os.replace(tmp, arc)
        for old in old_parts:
            old.unlink()
    info = {"tool": f"cloud_run.py {VERSION}", "topic": t, "saved": datetime.now(w.KST).isoformat(timespec="seconds"), "why": why,
            "files": len(files), "bytes_raw": sum(f.stat().st_size for f, _ in files), "bytes_tgz": len(data),
            "sha256": hashlib.sha256(data).hexdigest(), "parts": [part.name for part in parts], "kinds": dict(sorted(kinds.items()))}
    w._write_json(man, info)
    saved = arc.relative_to(ROOT).as_posix() + (f" ({len(parts)}조각 .001~.{len(parts):03d})" if parts else "")
    log("CACHE", topic=t, saved=saved, files=len(files), mb_raw=round(info["bytes_raw"] / 1e6, 1),
        mb_tgz=round(len(data) / 1e6, 2), parts=len(parts), why=why or "-", note="git 으로 main 에 올리면 새 컨테이너도 이어서 씀")
    return {"cache_saved": True, "cache_files": len(files), "cache_mb": round(len(data) / 1e6, 2), "cache_parts": len(parts)}


def cache_load(t, force=False):
    """새 컨테이너: .cache 가 비어 있으면 저장소의 묶음을 풂 (force 면 덮어씀). 묶음 안 이름은 cache_sources 두 곳만 받음."""
    arc, man = cache_paths(t)
    parts = cache_parts(arc)
    if not arc.is_file() and not parts:
        return {"cache_loaded": False, "why": "묶음 없음"}
    have = sum(1 for _ in (w.out_dir(t) / ".cache").glob("*.json")) if (w.out_dir(t) / ".cache").is_dir() else 0
    if have and not force:
        return {"cache_loaded": False, "why": f"이미 캐시 {have}개"}
    info = w._read_json(man, {})
    use_parts = bool(parts) and (bool(info.get("parts")) or not arc.is_file())     # v1.4: 목록이 조각이라 하거나 cache.tgz 가 없으면 조각
    data = b"".join(part.read_bytes() for part in parts) if use_parts else arc.read_bytes()
    if info.get("sha256") and hashlib.sha256(data).hexdigest() != info["sha256"]:
        log("CACHE", logging.WARNING, topic=t, note="묶음 sha256 이 목록(cache.json)과 다름 — 그래도 풂 (목록이 예전 것일 수 있음)")
    allowed = tuple(name + "/" for _, name in cache_sources(t))
    n = 0
    with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as tf:
        members = [m for m in tf.getmembers() if m.isfile() and m.name.startswith(allowed) and ".." not in m.name.split("/")]
        tf.extractall(ROOT / t, members=members, filter="data")
        n = len(members)
    log("CACHE", topic=t, loaded=arc.relative_to(ROOT).as_posix() + (f" ({len(parts)}조각)" if use_parts else ""), files=n, saved=info.get("saved") or "-", force=force,
        note="저장소의 탐색 캐시를 풂 — 받은 검색·영상 정보는 할당량 0 으로 다시 씀")
    return {"cache_loaded": True, "cache_files": n, "cache_saved_at": info.get("saved")}


# ---------------------------------------------------------------- 목록·체크
def explore_file(shorts):
    return "shorts_explore.json" if shorts else "explore.json"


def used(t, shorts):
    """이미 분석에 쓴 영상 — 웹 화면 GET /api/explore 와 같은 규칙 (목록·체크에서 뺌, 승인하면 바로 빠짐)."""
    return w.used_shorts_ids(t) if shorts else w.used_ids(t)


def cmd_list(t, a):
    ex = w._read_json(w.web_dir(t) / explore_file(a.shorts), {})
    rows = ex.get("rows") or []
    if not rows:
        print("탐색 목록이 없습니다 — 먼저 explore" + (" --shorts" if a.shorts else ""))
        return {"rows": 0}
    u = used(t, a.shorts)
    hidden = sum(1 for r in rows if r["id"] in u)
    rows = sorted((r for r in rows if r["id"] not in u), key=w.ratio_key)
    checked = {i for i in ex.get("checked") or [] if i not in u}
    sel = [r for r in rows if (a.checked and r["id"] in checked) or (a.unchecked and r["id"] not in checked)
           or not (a.checked or a.unchecked)]
    print(f"# {t} {'쇼츠 ' if a.shorts else ''}탐색 목록 {ex.get('generated')} · 최근 {ex.get('weeks')}주 · 영상 {len(rows)} · 체크 {len(checked)}"
          f" · 뺀 것 {ex.get('excluded') or {}} · 이미 분석에 쓴 영상 {hidden}개 숨김 · 못 한 검색 {len(ex.get('pending') or [])}")
    print("n | ✔ | 까닭 | 배수 | 조회수 | 구독자 | 분 | 일 | 관련 | 제목 | 채널 | id")
    for n, r in enumerate(sel[: a.limit or None], 1):
        print(" | ".join(str(x) for x in (
            n, "✔" if r["id"] in checked else " ", r.get("reason") or "-", r.get("ratio") if r.get("ratio") is not None else "-",
            f"{r.get('views') or 0:,}", f"{r['subs']:,}" if r.get("subs") is not None else "비공개", r.get("minutes"),
            r.get("age_days"), "O" if r.get("relevant") else "x" + (" 짧음" if r.get("short") else ""),
            (r.get("title") or "")[:60].replace("|", "/"), (r.get("channel") or "")[:20].replace("|", "/"), r["id"])))
    return {"rows": len(rows), "used_hidden": hidden, "shown": min(len(sel), a.limit or len(sel)), "checked": len(checked)}


def dismissed_path(t, shorts):
    """v1.5: 내가 푼 추천 (기간을 바꿔 다시 탐색해도 다시 체크되지 않게) — result/web 이라 캐시 묶음에 함께 올라감."""
    return w.web_dir(t) / ("shorts_dismissed.json" if shorts else "dismissed.json")


def apply_dismissed(t, shorts):
    """v1.5: explore 뒤 — 탐색 목록의 체크에서 내가 예전에 푼 영상을 다시 뺌. → 뺀 수"""
    dis = set((w._read_json(dismissed_path(t, shorts), {}) or {}).get("ids") or [])
    fn = explore_file(shorts)
    ex = w._read_json(w.web_dir(t) / fn, {})
    if not dis or not ex:
        return 0
    before = list(ex.get("checked") or [])
    ex["checked"] = [i for i in before if i not in dis]
    n = len(before) - len(ex["checked"])
    if n:
        w._write_json(w.web_dir(t) / fn, ex)
    log("CHECK", topic=t, shorts=shorts, dismissed_known=len(dis), unchecked_again=n, note="예전에 푼 추천은 다시 탐색해도 풂 (dismissed.json)")
    return n


def cmd_check(t, a, on):
    fn = explore_file(a.shorts)
    ex = w._read_json(w.web_dir(t) / fn, {})
    if not ex:
        raise w.UserError("탐색 목록이 없습니다 — 먼저 explore")
    ok_ids = {r["id"] for r in ex.get("rows") or []}
    bad = [i for i in a.ids if i not in ok_ids]
    cur = list(ex.get("checked") or [])
    if on:
        cur += [i for i in a.ids if i in ok_ids and i not in cur]
    else:
        cur = [i for i in cur if i not in set(a.ids)]
    ex["checked"] = [i for i in cur if i in ok_ids]                       # /api/checked 와 같은 규칙 — 목록에 있는 영상만
    w._write_json(w.web_dir(t) / fn, ex)
    dp = dismissed_path(t, a.shorts)                                      # v1.5: 푼 추천 기억 (check 하면 지움)
    dis = list(dict.fromkeys((w._read_json(dp, {}) or {}).get("ids") or []))
    dis = [i for i in dis if i not in set(a.ids)] + ([] if on else [i for i in a.ids if w.re.fullmatch(r"[0-9A-Za-z_-]{11}", i)])   # 지금 목록에 없어도 기억
    w._write_json(dp, {"ids": dis, "updated": datetime.now(w.KST).isoformat(timespec="seconds")})
    log("CHECK", topic=t, on=on, ids=len(a.ids), not_in_list=",".join(bad) or "-", checked=len(ex["checked"]))
    return {"checked": len(ex["checked"]), "not_in_list": bad}


def cmd_status(t, a):
    ex = w._read_json(w.web_dir(t) / "explore.json", {})
    sx = w._read_json(w.web_dir(t) / "shorts_explore.json", {})
    q = w.quota_view(t)
    od = w.out_dir(t)
    res = {"tool": f"cloud_run.py {VERSION} / web_ui.py {w.VERSION}", "topic": t, "name": w.topic_name(t),
           "include_foreign": w.foreign_ok(t), "key_source": w.orr.load_api_key(t)[1],
           "github_token": "있음" if pc.find_secret("GITHUB_TOKEN", t)[0] else "없음",
           "quota": {k: q.get(k) for k in ("used", "left", "budget", "exhausted", "reset_kst", "searches", "search_blocked", "search_cap", "day")},
           "explore": {"generated": ex.get("generated"), "weeks": ex.get("weeks"), "videos": len(ex.get("rows") or []),
                       "checked": len(ex.get("checked") or []), "pending": len(ex.get("pending") or []),
                       "pending_videos": ex.get("pending_videos"), "excluded": ex.get("excluded")},
           "shorts_explore": {"generated": sx.get("generated"), "videos": len(sx.get("rows") or []), "checked": len(sx.get("checked") or [])},
           "cases": {"W_": len(list(od.glob("W_*/metadata.json"))), "S_": len(list(w.shorts_out(t).glob("S_*/metadata.json")))},
           "cache_files": len(list((od / ".cache").glob("*.json"))) if (od / ".cache").is_dir() else 0,
           "resume_plan": w.resume_plan(t), "whisper_pending": w.whisper_pending(t, fresh=True)}
    until = w.orr.caption_blocked()
    res["caption_block"] = until.astimezone(w.KST).isoformat(timespec="minutes") if until else None
    print(json.dumps(res, ensure_ascii=False, indent=1))
    return {"ok": True}


def cmd_approve(t, a):
    fn = explore_file(a.shorts)
    ex = w._read_json(w.web_dir(t) / fn, {})
    u = used(t, a.shorts)
    ids = [i for i in (list(a.ids) or list(ex.get("checked") or [])) if i not in u]     # 화면처럼 이미 받은 영상은 다시 받지 않음
    log("APPROVE", topic=t, shorts=a.shorts, ids=len(ids), note="체크한 영상 (이미 분석에 쓴 영상은 뺌)" if not a.ids else "준 ID")
    if a.shorts:
        w.need_sh()
        return w.job_shorts_approve(t, ids, False)
    return w.job_approve(t, ids, False)


def cmd_foreign(t, a):
    """[외국 영상도] — /api/foreign 과 같음 (작업 중엔 못 바꿈은 이 명령이 혼자 도므로 해당 없음). GitHub 올리기는 git 으로."""
    if not a.ids or a.ids[0] not in ("on", "off"):
        raise w.UserError("foreign on 또는 foreign off")
    on = a.ids[0] == "on"
    if w.foreign_ok(t) == on:
        return {"include_foreign": on, "message": "이미 " + ("켜져" if on else "꺼져") + " 있습니다"}
    w.set_include_foreign(t, on)
    nf = len(pc.read_keyword_list(w.foreign_keywords_path(t)) or []) if w.foreign_keywords_path(t).is_file() else 0
    log("SETTINGS", topic=t, include_foreign=w.foreign_ok(t), file=f"{t}/analyzer_config.toml", foreign_keywords=nf,
        note="다음 탐색부터 " + ("외국 영상도 — 검색은 언어 지정 없이 새로 (첫 탐색은 캐시 없음)" if on else "외국 영상을 뺌"))
    return {"include_foreign": w.foreign_ok(t), "foreign_keywords": nf}


CAPTION_NEVER_TRIED = ("ModuleNotFoundError",)   # v1.3: 자막 도구가 없어 요청조차 안 한 것 (PC 2026-10-14~15 승인분)


def caption_retry_ok(st):
    """다시 요청해도 되는 자막 상태: 연결 실패(orr.is_network_failure)·시도 못 함. 자막 서버 차단은 아님 (음성인식 몫 — CLAUDE.md)."""
    st = str(st or "")
    return not w.orr.is_caption_block(st) and (w.orr.is_network_failure(st) or any(x in st for x in CAPTION_NEVER_TRIED))


def cmd_captions(t, a):
    todo = []
    for d in sorted(w.out_dir(t).glob("W_*")) + sorted(w.shorts_out(t).glob("S_*")):
        m = w._read_json(d / "metadata.json", None)
        if m and m.get("id") and not (d / "transcript.json").is_file() and caption_retry_ok(m.get("transcript_status")):
            todo.append((d, m))
    if a.limit:
        todo = todo[: a.limit]
    log("CAPTIONS", topic=t, todo=len(todo), note="자막만 다시 (할당량 0) — 연결 실패·시도 못 한 것만, 자막 서버 차단은 음성인식 몫이라 건너뜀")
    got, block, fail = [], 0, 0
    for n, (d, m) in enumerate(todo, 1):
        if w.orr.caption_blocked():
            log("CAPTIONS", logging.WARNING, topic=t, note="자막 요청 쉬는 중 (연속으로 막힘) — 멈춤, 남은 것은 상태 그대로 (다음에 다시)", left=len(todo) - n + 1)
            break
        w.step(f"자막 {n}/{len(todo)} — {str(m.get('title') or '')[:40]}", n - 1, len(todo))
        snips, lang, st = w.orr.transcript(m["id"], any_lang=bool(m.get("foreign")))
        if not snips and w.orr.caption_blocked() and "쉼" in str(st):        # 요청하기 전에 쉬기가 시작됨 — 기록하지 않음
            log("CAPTIONS", logging.WARNING, topic=t, note="자막 요청 쉬기 시작 — 멈춤", left=len(todo) - n + 1)
            break
        if snips:                                                           # deep_case 와 같은 파일
            (d / "transcript.json").write_text(json.dumps({"lang": lang, "snippets": snips}, ensure_ascii=False), "utf-8")
            (d / "transcript.txt").write_text("\n".join(f"[{x['start']:7.1f}] {x['text']}" for x in snips), "utf-8")
            m.update(transcript_lang=lang, transcript_status=st, **w.orr.speech_stats(snips))
            got.append(m["id"])
        else:
            m.update(transcript_lang=lang, transcript_status=st)
            block += w.orr.is_caption_block(st)
            fail += not w.orr.is_caption_block(st)
        m["transcript_retried"] = datetime.now(w.KST).isoformat(timespec="minutes")
        w._write_json(d / "metadata.json", m)
        log("CAPTIONS", n=f"{n}/{len(todo)}", id=m["id"], result=lang if snips else str(st)[:90])
    res = {"captions_todo": len(todo), "captions_got": len(got), "captions_blocked": block, "captions_failed": fail}
    log("CAPTIONS", topic=t, **res, note="받은 영상은 다음 analyze 부터 글 출처 '자막'")
    return res


def cmd_wait_reset(t, a):
    nxt, how = pc.next_quota_reset(datetime.now(timezone.utc), margin_min=w.RESUME_MARGIN_MIN)
    log("WAIT", topic=t, until_kst=nxt.astimezone(w.KST).isoformat(timespec="minutes"), how=how,
        minutes=round((nxt - datetime.now(timezone.utc)).total_seconds() / 60, 1), note="할당량 초기화(태평양 자정) +10분까지 기다림")
    while (left := (nxt - datetime.now(timezone.utc)).total_seconds()) > 0:
        time.sleep(min(60.0, left))
    res = {"waited_until": nxt.isoformat()}
    if a.then == "resume":
        res.update(w.job_resume(t, "할당량 초기화 (클라우드)"))
    return res


# ---------------------------------------------------------------- 명령
def parse_args(argv=None):
    ap = argparse.ArgumentParser(description="클라우드 분석 실행기 — 웹 화면(tools/web_ui.py) 작업을 명령으로")
    ap.add_argument("topic", help="주제 폴더 (예: stock)")
    ap.add_argument("cmd", choices=["status", "explore", "list", "check", "uncheck", "approve", "baseline", "comments", "demand",
                                    "analyze", "resume", "startup", "foreign", "wait-reset", "cache-save", "cache-load", "captions"])
    ap.add_argument("ids", nargs="*", help="check·uncheck·approve 할 영상 ID (foreign 은 on|off)")
    ap.add_argument("--weeks", type=int, default=8, help="explore: 최근 몇 주 (웹 화면 기본 8, 1~52)")
    ap.add_argument("--no-keywords", action="store_true", help="explore: 검색어 없이 추가한 채널·영상만")
    ap.add_argument("--alltime-only", action="store_true", help="explore: 보통 검색은 받아 둔 결과 그대로, 기간 없는 검색(③)만 — 할당량이 남을 때만")
    ap.add_argument("--shorts", action="store_true", help="쇼츠 (explore·list·check·approve)")
    ap.add_argument("--checked", action="store_true", help="list: 체크한 것만")
    ap.add_argument("--unchecked", action="store_true", help="list: 체크 안 한 것만")
    ap.add_argument("--limit", type=int, default=0, help="list: 몇 줄 · captions: 몇 개 (0 = 전부)")
    ap.add_argument("--push", choices=["none", "analyzer"], default="none",
                    help="none(기본) = 작업 폴더에만 (git 으로 직접) · analyzer = 웹 화면처럼 분석기 --push-only")
    ap.add_argument("--then", choices=["none", "resume"], default="none", help="wait-reset 뒤에 할 일")
    ap.add_argument("--force", action="store_true", help="cache-load: 있는 캐시를 덮어씀")
    ap.add_argument("--no-cache-save", action="store_true", help="명령 뒤에 캐시를 묶지 않음")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    argv = list(sys.argv[1:] if argv is None else argv)
    opts = {o for act in ap._actions for o in act.option_strings}
    argv = [("\x00" + x if x not in opts and VIDEO_ID_RX.fullmatch(x) else x) for x in argv]   # v1.5.1: '-' 로 시작하는 영상 ID
    a = ap.parse_args(argv)
    a.ids = [x.lstrip("\x00") for x in a.ids]
    return a


def main(argv=None):
    a = parse_args(argv)
    t = a.topic
    if not w.TOPIC_RX.match(t) or not (ROOT / t / "analyzer_config.toml").is_file():
        raise SystemExit(f"[START] ❌ 주제 설정 {t}/analyzer_config.toml 이 없음")
    setup_logging(t, a.log_level)
    load_tools()
    w.STATE.update(topic=t, topics=[t])
    w.step = progress_step(w.step)
    w.start_whisper = no_whisper
    if a.push == "none":
        w.push_results = local_push
    guard_fresh_start(t)
    try:
        w.claim_topic(t)                     # 웹 화면과 같은 잠금 — 같은 주제를 두 곳에서 동시에 돌리지 않게
    except w.UserError as e:
        raise SystemExit(f"[START] ❌ {e}")
    weeks = max(1, min(52, a.weeks))
    if a.cmd != "cache-load":
        try:
            cache_load(t)                    # v1.2: 새 컨테이너면 저장소의 탐색 캐시부터
        except (OSError, tarfile.TarError, ValueError) as e:
            log("CACHE", logging.WARNING, topic=t, note="캐시 묶음 풀기 실패 — 캐시 없이 계속 (탐색이 새로 검색함)", error=f"{type(e).__name__}: {e}"[:160])
    log("START", tool=f"cloud_run.py {VERSION}", web_ui=w.VERSION, topic=t, cmd=a.cmd, push=a.push, weeks=weeks if a.cmd == "explore" else "-",
        include_foreign=w.foreign_ok(t), key_source=w.orr.load_api_key(t)[1])
    t0 = time.monotonic()
    code = 0
    try:
        if a.cmd == "status":
            res = cmd_status(t, a)
        elif a.cmd == "list":
            res = cmd_list(t, a)
        elif a.cmd in ("check", "uncheck"):
            res = cmd_check(t, a, a.cmd == "check")
        elif a.cmd == "explore":
            if a.shorts:
                w.need_sh()
                res = w.job_shorts_explore(t, weeks, not a.no_keywords, alltime_only=a.alltime_only)
            else:
                res = w.job_explore(t, weeks, not a.no_keywords, alltime_only=a.alltime_only)
            res["unchecked_again"] = apply_dismissed(t, a.shorts)          # v1.5
        elif a.cmd == "approve":
            res = cmd_approve(t, a)
        elif a.cmd == "baseline":
            res = w.job_baseline(t)
            if w.sh is not None:
                res.update(w.job_shorts_baseline(t, quiet=True))
        elif a.cmd == "comments":
            res = w.job_comments(t)
        elif a.cmd == "demand":
            res = w.job_demand(t)
        elif a.cmd == "analyze":
            res = w.job_analyze(t)
        elif a.cmd == "resume":
            res = w.job_resume(t, "클라우드에서 이어서")
        elif a.cmd == "startup":
            res = w.job_startup(t, whisper=False)
        elif a.cmd == "foreign":
            res = cmd_foreign(t, a)
        elif a.cmd == "captions":
            res = cmd_captions(t, a)
        elif a.cmd == "cache-save":
            res = cache_save(t, "손으로")
        elif a.cmd == "cache-load":
            res = cache_load(t, force=a.force)
        elif a.cmd == "wait-reset":
            res = cmd_wait_reset(t, a)
        else:
            res = {}
    except w.UserError as e:
        res, code = {"error": str(e)}, 2
        log("JOB", logging.WARNING, topic=t, cmd=a.cmd, error=str(e))
    except w.Cancelled:
        res, code = {"error": "멈춤"}, 130
    finally:
        if a.cmd in CACHE_SAVE_AFTER and not a.no_cache_save:
            try:
                res_c = cache_save(t, a.cmd)
                if isinstance(locals().get("res"), dict):
                    res.update(res_c)
            except (OSError, tarfile.TarError) as e:
                log("CACHE", logging.WARNING, topic=t, note="캐시 묶기 실패 — 결과는 그대로", error=f"{type(e).__name__}: {e}"[:160])
        w.release_topic(t)
    log("RESULT", cmd=a.cmd, seconds=round(time.monotonic() - t0, 1), result=json.dumps(res, ensure_ascii=False, default=str)[:4000])
    return code


if __name__ == "__main__":
    sys.exit(main())
