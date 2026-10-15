#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-15 — 사용자 지시 "영상 만들었으면 각 영상 압축해서 저장소에 올리고 실행하면 해당 영상 유튜브에 자동 예약으로
#          1시간 후 업로드하는 colab 코드 전체 하나로 알려줘": Colab 셀 하나(guides/upload_guide.md 11번)가 부르는 일괄 업로드.
#          저장소의 압축본(source/<영상ID>/final_1080p.mp4)을 비공개로 올리고 '실행 시각 + 1시간'에 예약 공개 → 영상마다
#          youtube.json 을 main 에 올림 (다시 실행해도 같은 영상을 두 번 올리지 않음).
r"""
Colab(또는 터미널)에서 준비된 영상을 유튜브에 올리고 예약 공개합니다. 업로드 한 건은 tools/youtube_upload.py 가 합니다.

  python tools/colab_youtube.py                       # 준비된 영상 전부 → 비공개 업로드 + 지금부터 1시간 뒤 공개 → youtube.json 을 main 에
  python tools/colab_youtube.py --dry-run             # 올리지 않고 무엇을 올릴지·시트 검사만 (키 없어도 됨)
  python tools/colab_youtube.py --ids isa-mangi-2026-10 --delay 2h
  python tools/colab_youtube.py --gap 24h             # 첫 영상 1시간 뒤, 다음 영상은 24시간씩 뒤에 (하루에 하나씩 공개)
  python tools/colab_youtube.py --no-push             # youtube.json 을 GitHub 에 올리지 않음 (같은 Colab 세션 안에서만 중복 방지)

준비된 영상 = <주제>/source/<영상ID>/upload.md 가 있고, 영상 파일(out/ 원본 또는 source/ 압축본 final_1080p.mp4)이 있고,
             youtube.json 이 없는 영상 (tools/youtube_upload.find_video).
필요한 환경 변수 (Colab 보안 비밀 → 셀이 넣음, 값은 출력하지 않음):
  YOUTUBE_CLIENT_ID · YOUTUBE_CLIENT_SECRET · YOUTUBE_REFRESH_TOKEN   ← 업로드 (tools/youtube_auth.py 로 한 번 발급)
  GITHUB_TOKEN (+ 셀의 GIT_CONFIG_* 머리글)                            ← youtube.json 을 main 에 올리기·비공개 저장소 받기
할당량: 영상 하나 약 2,050단위 (업로드 1,600 + 자막 400 + 썸네일 50), 하루 10,000 → 하루 최대 4개. 넘으면 멈추고, 다음 날 같은 셀을 다시.
⚠️ Google 감사를 받지 않은 API 프로젝트로 올린 영상은 비공개로 잠겨 예약 공개가 되지 않을 수 있다 (guides/pipeline.md '업로드 주의').
※ 연구·교육용 도구다. 영상 내용은 투자·세무·보험 상담이나 권유가 아니다.
"""
import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent
sys.path.insert(0, str(TOOLS))
import youtube_upload as yu  # noqa: E402

VERSION = "v1.0"
UNITS_PER_VIDEO = 1600 + 400 + 50
DAILY_UNITS = 10_000
KST = dt.timezone(dt.timedelta(hours=9))
PUSH_TRIES = 4
STOP_WORDS = ("quotaExceeded", "uploadLimitExceeded", "dailyLimitExceeded", "rateLimitExceeded")


def log(stage, **kv):
    yu.log(stage, **kv)


def parse_span(s):
    """'1h' · '90m' · '24h' → timedelta."""
    m = re.fullmatch(r"(\d+(?:\.\d+)?)([hm])", (s or "").strip())
    if not m:
        raise SystemExit(f"[START] ❌ 시간 형식 오류: {s!r} (예: 1h, 90m)")
    v = float(m.group(1))
    return dt.timedelta(hours=v) if m.group(2) == "h" else dt.timedelta(minutes=v)


def find_ready(topics=None, ids=None):
    """준비된 영상 [(주제, 영상ID, 영상 파일)] 과 건너뛴 영상 [(영상ID, 이유)]."""
    ready, skipped = [], []
    for sheet in sorted(ROOT.glob("*/source/*/upload.md")):
        src = sheet.parent
        topic, vid = src.parent.parent.name, src.name
        if (topics and topic not in topics) or (ids and vid not in ids):
            continue
        if (src / "youtube.json").exists():
            skipped.append((vid, "이미 올림 (youtube.json)"))
            continue
        video = yu.find_video(topic, vid)
        if not video.exists():
            skipped.append((vid, "영상 파일 없음 (렌더 → tools/compress_video.py)"))
            continue
        ready.append((topic, vid, video))
    return ready, skipped


def git(*args, check=True):
    r = subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True)
    if check and r.returncode != 0:
        raise RuntimeError(f"git {args[0]} 실패: {r.stderr.strip()[-300:]}")
    return r


def push_state(topic, vid, publish_kst):
    """youtube.json 하나만 커밋 → pull --rebase → push origin HEAD:main (최대 4번). → 성공 여부."""
    path = f"{topic}/source/{vid}/youtube.json"
    git("add", "--", path)
    if git("diff", "--cached", "--quiet", check=False).returncode == 0:
        log("PUSH", video=vid, note="바뀐 것 없음")
        return True
    git("-c", "user.name=colab-uploader", "-c", "user.email=yeomin1024@users.noreply.github.com",
        "commit", "-q", "-m", f"유튜브 예약 업로드: {vid} (공개 {publish_kst} KST, Colab colab_youtube.py {VERSION})", "--", path)
    for k in range(PUSH_TRIES):
        git("pull", "-q", "--rebase", "origin", "main", check=False)
        r = git("push", "-q", "origin", "HEAD:main", check=False)
        if r.returncode == 0:
            log("PUSH", video=vid, file=path, ok=True)
            return True
        wait = 2 ** (k + 1)
        log("PUSH", video=vid, ok=False, retry_in_s=wait, error=r.stderr.strip()[-160:].replace(" ", "_"))
        time.sleep(wait)
    return False


def main(argv=None):
    ap = argparse.ArgumentParser(description="준비된 영상을 유튜브에 비공개로 올리고 예약 공개 (Colab 셀 하나)")
    ap.add_argument("--topics", default=None, help="이 주제 폴더만 (예: economic)")
    ap.add_argument("--ids", default=None, help="이 영상만 (쉼표로)")
    ap.add_argument("--delay", default="1h", help="예약 공개: 실행 시각 + 이 시간 (기본 1h, 5분 이상)")
    ap.add_argument("--gap", default="0m", help="영상이 여러 개일 때 공개 간격 (기본 0 = 모두 같은 시각, 예: 24h)")
    ap.add_argument("--max", type=int, default=4, help=f"이번에 올릴 최대 영상 수 (기본 4 — 하루 할당량 {DAILY_UNITS:,} ÷ 약 {UNITS_PER_VIDEO:,})")
    ap.add_argument("--dry-run", action="store_true", help="올리지 않고 확인만")
    ap.add_argument("--no-push", action="store_true", help="youtube.json 을 GitHub 에 올리지 않음")
    a = ap.parse_args(argv)
    t0 = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)
    log("START", tool=f"colab_youtube.py {VERSION}", dry_run=a.dry_run, delay=a.delay, gap=a.gap, max=a.max,
        note="연구·교육용 — 투자·세무·보험 상담 아님")
    topics = {t.strip() for t in a.topics.split(",")} if a.topics else None
    ids = {t.strip() for t in a.ids.split(",")} if a.ids else None
    ready, skipped = find_ready(topics, ids)
    for vid, why in skipped:
        log("PLAN", video=vid, action="skip", why=why.replace(" ", "_"))
    todo = ready[: a.max]
    for topic, vid, video in ready[a.max:]:
        log("PLAN", video=vid, action="later", why=f"--max_{a.max}_넘음_(다음에_같은_셀)")
    if not todo:
        log("DONE", uploaded=0, note="올릴 영상 없음 — 모두 올렸거나 영상 파일이 없음")
        return 0
    delay, gap = parse_span(a.delay), parse_span(a.gap)
    plan = []
    for i, (topic, vid, video) in enumerate(todo):
        when = t0 + delay + gap * i
        plan.append((topic, vid, video, when.strftime("%Y-%m-%dT%H:%M:%SZ"), when.astimezone(KST).strftime("%Y-%m-%d %H:%M")))
        log("PLAN", video=vid, action="upload", file=str(video.relative_to(ROOT)), mb=round(video.stat().st_size / 1e6, 1),
            publish_at_kst=plan[-1][4].replace(" ", "_"))
    log("PLAN", videos=len(plan), est_units=len(plan) * UNITS_PER_VIDEO, daily_units=DAILY_UNITS,
        note="감사_전_API_프로젝트면_비공개로_잠겨_공개되지_않을_수_있음(pipeline.md)")
    if not a.dry_run:
        missing = [k for k in ("YOUTUBE_CLIENT_ID", "YOUTUBE_CLIENT_SECRET", "YOUTUBE_REFRESH_TOKEN") if not os.environ.get(k, "").strip()]
        if missing:
            raise SystemExit(f"[AUTH] ❌ 환경 변수 없음: {', '.join(missing)} → Colab 왼쪽 🔑(보안 비밀)에 넣고 '노트북 액세스'를 켠 뒤 셀 다시 실행")
        yu.check_auth()
    push = not a.dry_run and not a.no_push
    if push and not os.environ.get("GITHUB_TOKEN", "").strip():
        log("PUSH", note="GITHUB_TOKEN 없음 → youtube.json 을 올리지 않음 (같은 세션 안에서만 중복 방지)")
        push = False
    results, stopped = [], None
    for topic, vid, video, when_z, when_kst in plan:
        if stopped:
            results.append((vid, "not_run", "-", when_kst))
            continue
        log("VIDEO", video=vid, publish_at_kst=when_kst.replace(" ", "_"))
        try:
            res = yu.run(topic, vid, dry_run=a.dry_run, video=str(video), publish_at=None if a.dry_run else when_z)
        except SystemExit as e:              # 시트 검사 실패 등 — 이 영상만 건너뜀
            log("VIDEO", video=vid, ok=False, error=str(e)[:200].replace(" ", "_"))
            results.append((vid, "failed", "-", when_kst))
            continue
        except Exception as e:               # HTTP 오류 — 할당량이면 모두 멈춤
            msg = str(e)
            log("VIDEO", video=vid, ok=False, error=msg[:240].replace(" ", "_"))
            results.append((vid, "failed", "-", when_kst))
            if any(w in msg for w in STOP_WORDS):
                stopped = "할당량"
                log("STOP", reason="유튜브 할당량 초과 — 남은 영상은 내일(태평양 자정 뒤) 같은 셀을 다시")
            continue
        if a.dry_run:
            results.append((vid, "dry-run", "-", when_kst))
            continue
        url = (res or {}).get("url", "-")
        pushed = push_state(topic, vid, when_kst) if push else False
        results.append((vid, "uploaded" + ("" if pushed or not push else " (push 실패 — git push 를 다시)"), url, when_kst))
    print("\n| 영상 | 결과 | 유튜브 | 공개 (한국 시간) |\n|---|---|---|---|")
    for vid, st, url, when in results:
        print(f"| {vid} | {st} | {url} | {when} |")
    up = sum(1 for r in results if r[1].startswith("uploaded"))
    log("DONE", uploaded=up, failed=sum(1 for r in results if r[1] == "failed"), not_run=sum(1 for r in results if r[1] == "not_run"),
        next="예약 시각 전에 스튜디오에서 영상·자막·썸네일 확인" if up else "-")
    return 1 if any(r[1] in ("failed", "not_run") for r in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
