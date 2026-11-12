#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-11-12 — 사용자 지시 "업로드에 필요한 자료를 대본별로 저장소에 올리고 내 컴퓨터에서 자료가 다 생성됐는지 확인 후
#          다 된게 있으면 내가 업로드 버튼 누르면 일주일 후 자동 예약으로 올라가게 해줘" (PC 쪽은 tools/upload_web.py).
#   클라우드(Claude)가 렌더한 완성 영상을 PC 가 받을 수 있게 저장소에 올린다 — 이 환경은 Drive 에 큰 파일을 올릴 수 없음(연결 도구 10MB 한도).
#   · 영상: out/<영상ID>/final_1080p.mp4 → 90MB 조각(final_1080p.mp4.part01 …) → 브랜치 `uploads` 의 <주제>/<영상ID>/ (화질 그대로 — PC 가 이어 붙여 sha256 확인)
#     `uploads` 는 커밋 하나짜리 브랜치로 늘 다시 짬(부모 없음 · 강제 푸시): 아직 안 올린 영상만 남기고, 올린 영상(main 에 youtube.json)은 뺌
#     → 지난 조각은 더는 가리키는 커밋이 없어 저장소가 계속 커지지 않음. main 에는 영상이 들어가지 않음 (CLAUDE.md: 영상 파일은 git 에 넣지 않는다 — main 기준).
#   · 확인값: <주제>/source/<영상ID>/video.json (크기 · sha256 · md5 · 조각 목록 · 브랜치) — main 에 (PC 가 '영상 준비됨'을 이것으로 봄)
#   · check: 업로드 자료(시트 제목·설명란·태그·챕터 · 자막 · 썸네일 · 영상)가 다 있는지 표로
# 사용법:
#   python3 tools/upload_pack.py check stock manspi-jeonmang-2026-11 bandeung-maesu-2026-11
#   python3 tools/upload_pack.py pack  stock manspi-jeonmang-2026-11 bandeung-maesu-2026-11 [--dry-run] [--remote origin]
#     → video.json 을 쓰고 uploads 브랜치를 다시 짜서 강제 푸시 (video.json 은 Claude 가 main 에 커밋)
# 로그: [STAGE] [시각] key=value …   ※ 연구·교육용 도구 — 영상 내용은 투자 권유가 아님.
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent
sys.path.insert(0, str(TOOLS))
import youtube_upload as yu  # noqa: E402

VERSION = "v1.0"
BRANCH = "uploads"
PART = 90 * 1024 * 1024                      # GitHub 파일 하나 100MB 한도 아래
THUMB_RE = re.compile(r"^thumbnail_\d\.(png|jpe?g|webp)$", re.I)


def log(stage: str, **kv) -> None:
    print(f"[{stage}] [{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}] " + " ".join(f"{k}={v}" for k, v in kv.items()), flush=True)


def git(*args, env=None, check=True, capture=True) -> str:
    r = subprocess.run(["git", "-C", str(ROOT), *args], env=env, text=True, capture_output=capture)
    if check and r.returncode != 0:
        raise SystemExit(f"[GIT] ❌ git {' '.join(args[:3])} … 실패: {(r.stderr or '')[:300]}")
    return (r.stdout or "").strip()


def file_hashes(p: Path) -> tuple[str, str]:
    s, m = hashlib.sha256(), hashlib.md5()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(8 << 20), b""):
            s.update(chunk)
            m.update(chunk)
    return s.hexdigest(), m.hexdigest()


def title_options(md: str) -> list[dict]:
    """업로드 시트 1번 '제목' 섹션 → [{n, title, thumb}] — 코드 블록 하나(제목 하나)거나, 표 '| **1** | 제목 | 글자 | `thumbnail_1.jpg` |' 여러 안."""
    m = re.search(r"^##\s*\d+\.\s*[^\n]*제목[^\n]*\n(.*?)(?=^##\s|\Z)", md, re.M | re.S)
    if not m:
        return []
    body = m.group(1)
    c = re.search(r"```[^\n]*\n(.*?)\n```", body, re.S)
    if c and c.group(1).strip():
        return [{"n": 1, "title": c.group(1).strip(), "thumb": 1}]
    out = []
    for row in re.finditer(r"^\|\s*\**(\d)\**\s*\|\s*([^|]+?)\s*\|[^\n]*?thumbnail_(\d)", body, re.M):
        out.append({"n": int(row.group(1)), "title": row.group(2).strip(), "thumb": int(row.group(3))})
    return out


def check_one(topic: str, vid: str) -> dict:
    """업로드 자료 점검 → {항목: (ok, 메모)} + 요약."""
    src = ROOT / topic / "source" / vid
    res: dict[str, tuple[bool, str]] = {}
    md_p = src / "upload.md"
    if not md_p.is_file():
        return {"vid": vid, "items": {"업로드 시트": (False, "upload.md 없음")}, "ready": False}
    md = md_p.read_text("utf-8")
    opts = title_options(md)
    res["제목"] = (bool(opts), f"{len(opts)}안" + (" — PC 화면에서 고름" if len(opts) > 1 else f" · {opts[0]['title'][:40]}" if opts else " — 1번 섹션에 코드 블록이나 안 표가 없음"))
    meta = yu.read_sheet(topic, vid)
    if opts:
        meta["title"] = opts[0]["title"]
    try:
        meta["description"], chapters = yu.recompute_chapters(topic, vid, meta["description"], meta["chapter_spec"])
    except SystemExit as e:
        chapters = None
        res["챕터"] = (False, str(e)[:120])
    else:
        res["챕터"] = (bool(chapters), f"{len(chapters or [])}개" if chapters else "챕터 명령 없음 (3·4번 섹션 --chapters)")
    probs = yu.validate(meta)
    res["설명란·태그"] = (not probs, "; ".join(probs)[:160] if probs else f"설명 {len(meta['description'])}자 · 태그 {len(meta['tags'])}개")
    res["자막"] = ((src / f"{vid}.srt").is_file(), f"{vid}.srt")
    res["대본"] = ((src / f"{vid}.txt").is_file(), f"{vid}.txt")
    th = [p.name for p in (src / "thumbnails").glob("thumbnail_*")] if (src / "thumbnails").is_dir() else []
    th = sorted(n for n in th if THUMB_RE.match(n))
    res["썸네일"] = (bool(th), ", ".join(th) or "thumbnails/thumbnail_N.jpg 없음")
    res["합성 콘텐츠 표시"] = (meta["synthetic"], "예" if meta["synthetic"] else "아니요 (AI 음성이면 '예')")
    vf = ROOT / topic / "out" / vid / "final_1080p.mp4"
    vj = src / "video.json"
    if vj.is_file():
        rec = json.loads(vj.read_text("utf-8"))
        res["영상"] = (True, f"video.json {rec['size'] / 1e6:.0f}MB · 조각 {len(rec['parts'])} · {rec['branch']}")
    else:
        res["영상"] = (vf.is_file(), f"out/{vid}/final_1080p.mp4 {vf.stat().st_size / 1e6:.0f}MB (아직 pack 전)" if vf.is_file() else "완성 영상 없음 — 렌더 먼저")
    res["올린 적 없음"] = (not (src / "youtube.json").is_file(), "youtube.json 없음" if not (src / "youtube.json").is_file() else "이미 올림")
    return {"vid": vid, "items": res, "ready": all(ok for ok, _ in res.values()), "titles": opts}


def cmd_check(topic: str, vids: list[str]) -> int:
    bad = 0
    for vid in vids:
        r = check_one(topic, vid)
        print(f"\n### {topic}/{vid} — {'✅ 준비됨' if r['ready'] else '❌ 부족'}\n| 항목 | 결과 | 메모 |\n|---|---|---|")
        for k, (ok, note) in r["items"].items():
            print(f"| {k} | {'✅' if ok else '❌'} | {note} |")
        bad += 0 if r["ready"] else 1
    log("CHECK", topic=topic, videos=len(vids), not_ready=bad)
    return 1 if bad else 0


def uploaded_on_main(remote: str) -> set[str]:
    """main 에서 youtube.json 이 있는 <주제>/source/<영상ID> → {'<주제>/<영상ID>'}."""
    git("fetch", "-q", remote, "main")
    names = git("ls-tree", "-r", "--name-only", f"{remote}/main").splitlines()
    out = set()
    for n in names:
        m = re.match(r"^([^/]+)/source/([^/]+)/youtube\.json$", n)
        if m:
            out.add(f"{m.group(1)}/{m.group(2)}")
    return out


def cmd_pack(topic: str, vids: list[str], dry: bool, remote: str) -> int:
    t0 = time.time()
    log("START", tool=f"upload_pack.py {VERSION}", topic=topic, videos=",".join(vids), branch=BRANCH, dry_run=dry)
    has_remote = subprocess.run(["git", "-C", str(ROOT), "fetch", "-q", remote, BRANCH], capture_output=True).returncode == 0
    done = uploaded_on_main(remote)
    tmp_index = Path(tempfile.mkdtemp()) / "index"
    env = dict(os.environ, GIT_INDEX_FILE=str(tmp_index))
    if has_remote:
        git("read-tree", f"{remote}/{BRANCH}", env=env)
    else:
        git("read-tree", "--empty", env=env)
    kept = sorted({"/".join(p.split("/")[:2]) for p in git("ls-files", env=env).splitlines() if p.count("/") >= 2})
    for key in kept:                                     # 이미 올린 영상의 조각은 뺌
        if key in done:
            git("rm", "-q", "--cached", "-r", key, env=env)
            log("PRUNE", video=key, why="main 에 youtube.json — 이미 올림")
    for vid in vids:
        vf = ROOT / topic / "out" / vid / "final_1080p.mp4"
        src = ROOT / topic / "source" / vid
        if not vf.is_file():
            raise SystemExit(f"[PACK] ❌ {vid}: 완성 영상 없음 {vf.relative_to(ROOT)} → 먼저 렌더")
        if not src.is_dir():
            raise SystemExit(f"[PACK] ❌ {vid}: 대본 폴더 없음 {src.relative_to(ROOT)}")
        if f"{topic}/{vid}" in done:
            log("PACK", video=vid, skip="main 에 youtube.json — 이미 올림")
            continue
        sha, md5 = file_hashes(vf)
        size = vf.stat().st_size
        git("rm", "-q", "--cached", "-r", "--ignore-unmatch", f"{topic}/{vid}", env=env)
        parts = []
        with open(vf, "rb") as f, tempfile.TemporaryDirectory() as td:
            i = 0
            while True:
                chunk = f.read(PART)
                if not chunk:
                    break
                i += 1
                name = f"final_1080p.mp4.part{i:02d}"
                pp = Path(td) / name
                pp.write_bytes(chunk)
                blob = git("hash-object", "-w", str(pp))
                git("update-index", "--add", "--cacheinfo", f"100644,{blob},{topic}/{vid}/{name}", env=env)
                parts.append({"name": name, "size": len(chunk), "sha256": hashlib.sha256(chunk).hexdigest()})
        rec = {"tool": f"upload_pack.py {VERSION}", "made": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
               "file": "final_1080p.mp4", "size": size, "sha256": sha, "md5": md5, "branch": BRANCH,
               "dir": f"{topic}/{vid}", "parts": parts, "duration_s": yu_duration(vf)}
        man = json.dumps(rec, ensure_ascii=False, indent=1) + "\n"
        mp = Path(tempfile.mkdtemp()) / "video.json"
        mp.write_text(man, "utf-8")
        git("update-index", "--add", "--cacheinfo", f"100644,{git('hash-object', '-w', str(mp))},{topic}/{vid}/video.json", env=env)
        (src / "video.json").write_text(man, "utf-8")
        log("PACK", video=vid, mb=round(size / 1e6, 1), parts=len(parts), sha256=sha[:12], record=str((src / "video.json").relative_to(ROOT)))
    readme = ("# 업로드 대기 영상 (tools/upload_pack.py 가 늘 다시 짜는 커밋 하나짜리 브랜치)\n\n"
              "- 아직 유튜브에 안 올린 완성 영상만 90MB 조각으로 둔다 — PC 의 tools/upload_web.py 가 받아 이어 붙이고 sha256 을 확인한다.\n"
              "- 올린 영상(main 에 youtube.json)은 다음 pack 때 빠지고, 이 브랜치는 부모 없는 새 커밋으로 바뀐다 (강제 푸시).\n"
              "- main 에는 영상이 들어가지 않는다. 확인값은 main 의 <주제>/source/<영상ID>/video.json.\n")
    rp = Path(tempfile.mkdtemp()) / "README.md"
    rp.write_text(readme, "utf-8")
    git("update-index", "--add", "--cacheinfo", f"100644,{git('hash-object', '-w', str(rp))},README.md", env=env)
    tree = git("write-tree", env=env)
    left = sorted({"/".join(p.split("/")[:2]) for p in git("ls-files", env=env).splitlines() if p.count("/") >= 2})
    msg = f"업로드 대기 영상 {len(left)}편 ({', '.join(left)}) — upload_pack.py {VERSION}"
    commit = git("commit-tree", tree, "-m", msg)
    log("TREE", commit=commit[:12], videos=len(left), list=",".join(left) or "-")
    if dry:
        log("DONE", dry_run=True, note="푸시 안 함", sec=round(time.time() - t0, 1))
        return 0
    r = subprocess.run(["git", "-C", str(ROOT), "push", "--force", remote, f"{commit}:refs/heads/{BRANCH}"], text=True, capture_output=True)
    if r.returncode != 0:
        raise SystemExit(f"[PUSH] ❌ uploads 브랜치 푸시 실패: {r.stderr[:300]} → 네트워크면 다시 실행")
    log("DONE", pushed=f"{remote}/{BRANCH}", commit=commit[:12], sec=round(time.time() - t0, 1),
        next="video.json 들을 main 에 커밋 · PC 에서 run_uploader.ps1 -Web")
    return 0


def yu_duration(p: Path):
    try:
        out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)], capture_output=True, text=True).stdout
        return round(float(out.strip()), 2)
    except (ValueError, OSError):
        return None


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="완성 영상·업로드 자료를 PC 업로드 화면이 받을 수 있게 (uploads 브랜치 + video.json)")
    ap.add_argument("cmd", choices=["check", "pack"])
    ap.add_argument("topic")
    ap.add_argument("videos", nargs="+")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--remote", default="origin")
    a = ap.parse_args(argv)
    return cmd_check(a.topic, a.videos) if a.cmd == "check" else cmd_pack(a.topic, a.videos, a.dry_run, a.remote)


if __name__ == "__main__":
    raise SystemExit(main())
