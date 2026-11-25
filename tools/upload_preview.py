#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-11-25 — 업로드 미리보기 아티팩트 자료 만들기 (PC 업로드 화면 tools/upload_web.py v1.6 의 [미리보기] · 썸네일 내려받기를 claude.ai 아티팩트로)
#   사용자 지시 2026-11-25 "아티팩트 만들어서 저번에 만들었던 미리보기, 썸네일 다운로드 기능을 거기에 넣어봐".
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.0 | 2026-11-25 | 최초 — 업로드 시트(upload.md)가 있는 롱폼·쇼츠마다 미리보기 자료(제목·설명란(챕터 다시 계산)·태그·설정·자막 앞부분·고정 댓글·실험안·썸네일·자료 점검) → data.json + 아티팩트에 같이 올릴 파일 목록 files.json | build · record · main |
"""업로드 미리보기 아티팩트의 자료를 만든다 (읽기만 — 저장소·유튜브에 아무것도 올리지 않음).

- 대상: topics.txt 의 주제 + youtube_channel.json 이 있는 폴더 (upload_web.topics 와 같은 규칙) 안의
  <주제>/source/<영상ID>/upload.md (롱폼) · <주제>/source/<영상ID>/shorts/upload.md (쇼츠 '<영상ID>-shorts').
- 업로드 대기(main 에 youtube.json 없음) = 자료 점검(tools/upload_pack.check_one 과 같은 규칙 — 영상은 video.json + uploads 브랜치 조각)
  + 미리보기 · 올린 영상(youtube.json 있음) = 유튜브 주소·공개 시각 + 썸네일(실험안은 스튜디오 '테스트 및 비교'에 직접 넣을 것).
- 미리보기 내용은 upload_web.preview 와 같음 (설명란 챕터 = 지금 SRT 로 다시 계산 · 설정 표 · 자막 처음 6개 · 고정 댓글).
  영상 재생은 넣지 않음 (완성 영상은 수십 MB — 아티팩트 파일 하나 한도 15MB, 영상은 PC 업로드 화면에서).
- 출력: <out>/data.json (한 줄에 영상 하나) · <out>/files.json (아티팩트 published 경로 → 저장소 파일 — Artifact 도구 files 에 그대로)
실행: python3 tools/upload_preview.py [--out .yt_work/upload_preview] [--status waiting|uploaded|all]
로그: [STAGE] [시각] key=value …  ※ 연구·교육용 도구.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
import sys
import time
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent
sys.path.insert(0, str(TOOLS))
import youtube_upload as yu  # noqa: E402
import upload_pack as up  # noqa: E402
import upload_web as uw  # noqa: E402   (experiments · srt_cues · cell — 함수만 씀, 서버는 켜지 않음)

VERSION = "v1.0"
KST = dt.timezone(dt.timedelta(hours=9))
TOPIC_KO = {"economic": "재테크", "stock": "주식", "psychology": "심리", "music": "음악", "history": "역사", "test": "시험 채널",
            "crisis": "위기", "math": "수학", "new": "새 분야"}
MAX_PUBLISH_MB = 60          # 아티팩트 한 번 올리기 64MB 아래


def log(stage: str, **kv) -> None:
    now = dt.datetime.now(KST).strftime("%Y-%m-%dT%H:%M:%S%z")
    print(f"[{stage}] [{now}] " + " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) and (' ' in v or not v) else v}"
                                          for k, v in kv.items()), flush=True)


def git(*args: str) -> str:
    r = subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else ""


def topics() -> list[str]:
    """upload_web.topics 와 같은 규칙 — 단 GitHub 대신 이 체크아웃(main 을 받아 둔 것)에서."""
    names = []
    p = ROOT / "topics.txt"
    for ln in (p.read_text("utf-8").splitlines() if p.is_file() else []):
        ln = ln.strip()
        if ln and not ln.startswith("#") and re.fullmatch(r"[a-z0-9_-]+", ln):
            names.append(ln)
    for q in sorted(ROOT.glob("*/youtube_channel.json")):
        if q.parent.name not in names:
            names.append(q.parent.name)
    return names


def sheets(topic: str) -> list[str]:
    out = []
    for p in sorted((ROOT / topic / "source").glob("*/upload.md")):
        out.append(p.parent.name)
    for p in sorted((ROOT / topic / "source").glob("*/shorts/upload.md")):
        out.append(p.parent.parent.name + "-shorts")
    return out


def thumb_size(p: Path) -> tuple[int, int]:
    try:
        from PIL import Image
        with Image.open(p) as im:
            return im.size
    except Exception as e:                                  # 그림을 못 읽으면 가로 16:9 로 봄 (경고만)
        log("THUMB", level="warn", file=str(p.relative_to(ROOT)), error=str(e)[:80], fallback="1280x720")
        return 1280, 720


def settings_of(md: str, meta: dict) -> dict:
    """upload_web.preview 의 설정 표와 같은 값."""
    cell = uw.cell
    return {"공개": "비공개로 올린 뒤 예약 공개",
            "카테고리": f"교육 (categoryId {yu.CATEGORY_EDUCATION} — 도구가 늘 이 값)" + ("" if cell(md, "카테고리") in ("교육", "-") else f" · 시트: {cell(md, '카테고리')}"),
            "시청자층": "아동용 아님 (도구가 늘 이 값)" + ("" if cell(md, "시청자층") in ("아동용 아님", "-") else f" · 시트: {cell(md, '시청자층')}"),
            "기본 언어": meta["default_language"],
            "변경되거나 합성된 콘텐츠": "예" if meta["synthetic"] else "아니요",
            "자막 올리기": ("예 — " + ("한국어 + 언어별" if meta["caption_mode"] == "all" else "한국어")) if meta["captions"] else "아니요",
            "언어별 제목·설명": ", ".join(meta["localizations"]) or "없음"}


def record(topic: str, vid: str, upl_paths: set[str]) -> tuple[dict, dict]:
    """영상 하나 → (미리보기 자료, 아티팩트 파일 {published: 저장소 경로})."""
    src = yu.src_dir(topic, vid)
    md = (src / "upload.md").read_text("utf-8")
    yt = src / "youtube.json"
    status = "uploaded" if yt.is_file() else "waiting"
    rec: dict = {"key": f"{topic}--{vid}", "topic": topic, "topic_ko": TOPIC_KO.get(topic, topic), "vid": vid,
                 "shorts": yu.is_shorts(vid), "status": status, "problems": []}
    files: dict = {}
    # 제목·설명란·태그 (시트 1·2·4번) — 챕터는 지금 SRT 로 다시 계산
    try:
        meta = yu.read_sheet(topic, vid)
    except SystemExit as e:
        rec["problems"].append(str(e)[:200])
        meta = {"title": "", "description": "", "tags": [], "chapter_spec": None, "synthetic": True, "default_language": "ko",
                "captions": True, "caption_mode": "ko", "localizations": {}}
    opts = up.title_options(md)
    if opts:
        meta["title"] = opts[0]["title"]
    chapters = []
    try:
        desc, ch = yu.recompute_chapters(topic, vid, meta["description"], meta["chapter_spec"])
        chapters = ch or []
    except SystemExit as e:
        desc = meta["description"]
        if status == "waiting":
            rec["problems"].append(str(e).splitlines()[0][:200])
    rec.update(title=meta["title"], title_chars=len(meta["title"]), title_opts=len(opts), description=desc, chapters=chapters,
               tags=meta["tags"], tags_chars=yu.tags_length(meta["tags"]), settings=settings_of(md, meta),
               srt=uw.srt_cues(src / f"{vid}.srt"), pinned=(yu._section_code(md, "고정 댓글") or "").strip(),
               experiments=uw.experiments(md))
    if status == "waiting":
        rec["problems"] += yu.validate(dict(meta, description=desc))
    # 썸네일 (본안 = titles.md 채택 짝 · 없으면 1)
    main_n = yu.paired_thumbnail(topic, vid)
    thumbs = []
    tdir = src / "thumbnails"
    names = sorted(p.name for p in tdir.glob("thumbnail_*") if up.THUMB_RE.match(p.name)) if tdir.is_dir() else []
    for nm in names:
        k = int(re.search(r"thumbnail_(\d)", nm).group(1))
        ex = next((e for e in rec["experiments"] if e["thumb"] == k), None)
        pub = f"thumbs/{topic}/{vid}/{nm}"
        p = tdir / nm
        w, h = thumb_size(p)
        thumbs.append({"n": k, "name": nm, "path": pub, "main": k == main_n, "w": w, "h": h, "kb": round(p.stat().st_size / 1024),
                       "role": "본안 — API 로 올림" if k == main_n else ("실험안 — 스튜디오 '테스트 및 비교'" + (f" · 짝 제목: {ex['title']}" if ex else ""))})
        files[pub] = str(p.relative_to(ROOT))
    rec["thumbs"] = thumbs
    # 영상 · 자료 점검
    vj = src / "video.json"
    if vj.is_file():
        v = json.loads(vj.read_text("utf-8"))
        missing = [x["name"] for x in v["parts"] if f"{v['dir']}/{x['name']}" not in upl_paths]
        rec["video"] = {"mb": round(v["size"] / 1e6), "parts": len(v["parts"]), "on_branch": not missing, "duration_s": v.get("duration_s")}
    else:
        rec["video"] = None
    if status == "waiting":
        r = up.check_one(topic, vid)
        items = {k: list(x) for k, x in r["items"].items()}
        if rec["video"]:
            items["영상"] = [rec["video"]["on_branch"], f"{rec['video']['mb']}MB · 조각 {rec['video']['parts']}개" +
                           (" ✓ uploads 브랜치" if rec["video"]["on_branch"] else " — uploads 브랜치에 조각 없음")]
        else:
            items["영상"] = [False, "video.json 없음 — Claude 가 렌더 뒤 tools/upload_pack.py pack"]
        items["올린 적 없음"] = [True, "main 에 업로드 기록 없음"]
        rec["items"] = [[k, bool(x[0]), str(x[1])] for k, x in items.items()]
        rec["ready"] = all(x[1] for x in rec["items"]) and not rec["problems"]
    else:
        st = json.loads(yt.read_text("utf-8"))
        url = st.get("url", "")
        rec["youtube"] = {"url": url if url.startswith("https://") else "", "publishAt": st.get("publishAt", ""), "title": st.get("title", "")}
        rec["ready"] = None
    return rec, files


def build(out: Path, which: str) -> int:
    t0 = time.time()
    commit = git("rev-parse", "--short=9", "HEAD")
    fetched = subprocess.run(["git", "-C", str(ROOT), "fetch", "-q", "origin", up.BRANCH], capture_output=True).returncode == 0
    upl = set(git("ls-tree", "-r", "--name-only", f"origin/{up.BRANCH}").splitlines()) if fetched else set()
    log("START", tool=f"upload_preview.py {VERSION}", commit=commit, uploads_branch="ok" if fetched else "못 받음 (영상 칸 ✗ 로 보임)",
        uploads_files=len(upl), status=which, note="읽기만 — 아무것도 올리지 않음")
    vids, files, fails = [], {}, []
    for topic in topics():
        for vid in sheets(topic):
            try:
                rec, f = record(topic, vid, upl)
            except Exception as e:                           # 한 편이 깨져도 나머지는 만듦 (로그에 남김)
                fails.append(f"{topic}/{vid}")
                log("FAIL", stage="record", topic=topic, video=vid, error=f"{type(e).__name__}: {str(e)[:160]}", next="그 편 upload.md 확인")
                continue
            if which != "all" and rec["status"] != which:
                continue
            vids.append(rec)
            files.update(f)
            log("VIDEO", topic=topic, video=vid, status=rec["status"], ready=rec["ready"], thumbs=len(rec["thumbs"]),
                chapters=len(rec["chapters"]), problems=len(rec["problems"]))
    waiting = sorted((r for r in vids if r["status"] == "waiting"), key=lambda r: (not r["ready"], r["topic"], r["vid"]))   # 준비된 것 먼저
    uploaded = [r for r in vids if r["status"] == "uploaded" and r["thumbs"]]          # 올린 영상은 썸네일 받기용 — 썸네일 없는 것은 뺌
    skipped = sum(1 for r in vids if r["status"] == "uploaded" and not r["thumbs"])
    uploaded.sort(key=lambda r: (r["youtube"]["publishAt"] or ""), reverse=True)        # 올린 영상은 최근 공개 먼저
    vids = waiting + uploaded
    keep = {t["path"] for r in vids for t in r["thumbs"]}
    files = {k: v for k, v in files.items() if k in keep}
    if skipped:
        log("SKIP", uploaded_without_thumbs=skipped, why="올린 영상인데 썸네일이 없음 — 받을 것이 없어 뺌")
    out.mkdir(parents=True, exist_ok=True)
    meta = {"tool": f"upload_preview.py {VERSION}", "built": dt.datetime.now(KST).strftime("%Y-%m-%d %H:%M"), "commit": commit,
            "uploads_branch": fetched, "default_days": 7, "default_hhmm": "17:00"}
    body = '{"meta": ' + json.dumps(meta, ensure_ascii=False) + ',\n"videos": [\n' + ",\n".join(json.dumps(r, ensure_ascii=False) for r in vids) + "\n]}\n"
    (out / "data.json").write_text(body, "utf-8")
    files["data.json"] = str((out / "data.json").relative_to(ROOT)) if (out / "data.json").resolve().is_relative_to(ROOT) else str(out / "data.json")
    (out / "files.json").write_text(json.dumps(files, ensure_ascii=False, indent=1) + "\n", "utf-8")
    mb = sum((ROOT / p).stat().st_size if not Path(p).is_absolute() else Path(p).stat().st_size for p in files.values()) / 1e6
    log("DONE", videos=len(vids), waiting=len(waiting), ready=sum(1 for r in waiting if r["ready"]), uploaded=len(uploaded),
        files=len(files), mb=round(mb, 1), data_kb=round(len(body.encode()) / 1024), failed=",".join(fails) or "-",
        out=str(out), sec=round(time.time() - t0, 1), next="Artifact 도구 files = files.json · file_path = tools/upload_preview/index.html")
    if mb > MAX_PUBLISH_MB:
        log("WARN", mb=round(mb, 1), limit=MAX_PUBLISH_MB, next="--status waiting 으로 줄이거나 두 번에 나눠 올림")
    return 1 if fails else 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="업로드 미리보기 아티팩트 자료 (data.json · files.json)")
    ap.add_argument("--out", default=str(ROOT / ".yt_work" / "upload_preview"))
    ap.add_argument("--status", choices=("waiting", "uploaded", "all"), default="all")
    a = ap.parse_args(argv)
    return build(Path(a.out).resolve(), a.status)


if __name__ == "__main__":
    sys.exit(main())
