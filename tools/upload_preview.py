#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.3 — 2026-11-27 — 대상 주제에 upload_topics.txt (업로드만 하는 주제, 예 crisis) — upload_web v1.7 과 같은 규칙. 함수 topics.
# 이전 v1.2 — 2026-11-26 — 대본 전체(챕터별) + 음성·자막이 이 대본으로 만들어졌는지(대본 문장이 지금 SRT 에 있는지) — 사용자 지시 "자꾸 주는 사람 영상 전반적으로 규칙 만족하도록 수정해서 아티팩트에 올려"
# 이전 v1.1 — 2026-11-25 — 영상: 업로드 대기 편은 미리보기용 낮은 화질 영상(14MB 아래 — 아티팩트 파일 하나 15MB 한도)을 같이 올려 재생 + 원본 GitHub 링크 ·
#          올린 편은 유튜브 링크 — 사용자 지시 "영상 재생 안되면 링크 첨부라도 해봐"
# 이전 v1.0 — 2026-11-25 — 업로드 미리보기 아티팩트 자료 만들기 (PC 업로드 화면 tools/upload_web.py v1.6 의 [미리보기] · 썸네일 내려받기를 claude.ai 아티팩트로)
#   사용자 지시 2026-11-25 "아티팩트 만들어서 저번에 만들었던 미리보기, 썸네일 다운로드 기능을 거기에 넣어봐".
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.3 | 2026-11-27 | upload_topics.txt 도 대상 (업로드만 하는 주제) | topics |
# | v1.2 | 2026-11-26 | script_of(대본 txt → 챕터·문장·예상 길이 · SRT 와 비교해 음성이 옛 대본인지 stale) · record 에 script·script_text | script_of · record |
# | v1.1 | 2026-11-25 | preview_video(원본 = out/ mp4 또는 uploads 브랜치 조각 → sha256 확인 → ffmpeg 360p 안팎 · 크기 맞춰 비트레이트 · 원본 sha 로 캐시) · links(원본 GitHub 받기 · uploads 폴더) · --no-video | preview_video · source_mp4 · record · build |
# | v1.0 | 2026-11-25 | 최초 — 업로드 시트(upload.md)가 있는 롱폼·쇼츠마다 미리보기 자료(제목·설명란(챕터 다시 계산)·태그·설정·자막 앞부분·고정 댓글·실험안·썸네일·자료 점검) → data.json + 아티팩트에 같이 올릴 파일 목록 files.json | build · record · main |
"""업로드 미리보기 아티팩트의 자료를 만든다 (읽기만 — 저장소·유튜브에 아무것도 올리지 않음).

- 대상: topics.txt 의 주제 + youtube_channel.json 이 있는 폴더 (upload_web.topics 와 같은 규칙) 안의
  <주제>/source/<영상ID>/upload.md (롱폼) · <주제>/source/<영상ID>/shorts/upload.md (쇼츠 '<영상ID>-shorts').
- 업로드 대기(main 에 youtube.json 없음) = 자료 점검(tools/upload_pack.check_one 과 같은 규칙 — 영상은 video.json + uploads 브랜치 조각)
  + 미리보기 · 올린 영상(youtube.json 있음) = 유튜브 주소·공개 시각 + 썸네일(실험안은 스튜디오 '테스트 및 비교'에 직접 넣을 것).
- 미리보기 내용은 upload_web.preview 와 같음 (설명란 챕터 = 지금 SRT 로 다시 계산 · 설정 표 · 자막 처음 6개 · 고정 댓글).
  영상 (v1.1): 업로드 대기 편 = 미리보기용 낮은 화질 mp4(14MB 아래 — 아티팩트 파일 하나 한도 15MB) + 원본 1080p GitHub 링크(uploads 브랜치 — 공개 저장소) ·
  올린 편 = 유튜브 링크. 원본은 out/<영상ID>/final_1080p.mp4(크기·sha256 이 video.json 과 같을 때) 또는 uploads 브랜치 조각을 이어 붙여 sha256 확인.
- 출력: <out>/data.json (한 줄에 영상 하나) · <out>/files.json (아티팩트 published 경로 → 저장소 파일 — Artifact 도구 files 에 그대로)
실행: python3 tools/upload_preview.py [--out .yt_work/upload_preview] [--status waiting|uploaded|all] [--no-video]
로그: [STAGE] [시각] key=value …  ※ 연구·교육용 도구.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
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

VERSION = "v1.3"
KST = dt.timezone(dt.timedelta(hours=9))
TOPIC_KO = {"economic": "재테크", "stock": "주식", "psychology": "심리", "music": "음악", "history": "역사", "test": "시험 채널",
            "crisis": "위기", "math": "수학", "new": "새 분야"}
MAX_PUBLISH_MB = 60          # 아티팩트 한 번 올리기 64MB 아래
PREVIEW_MAX_MB = 14.0        # 미리보기 영상 (아티팩트 파일 하나 15MB 한도 아래)
AUDIO_KBPS = 48              # 내레이션 한 채널이라 48k 면 충분
REPO = uw.REPO


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
    for fname in ("topics.txt", "upload_topics.txt"):      # v1.3 upload_topics.txt = 업로드만 하는 주제 (upload_web v1.7 과 같음)
        p = ROOT / fname
        for ln in (p.read_text("utf-8").splitlines() if p.is_file() else []):
            ln = ln.strip()
            if ln and not ln.startswith("#") and re.fullmatch(r"[a-z0-9_-]+", ln) and ln not in names:
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


def sha256_of(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def source_mp4(topic: str, vid: str, v: dict, upl_paths: set[str], work: Path) -> Path | None:
    """원본 완성 영상: out/<영상ID>/final_1080p.mp4 (크기·sha256 이 video.json 과 같을 때) → 아니면 uploads 브랜치 조각을 이어 붙여 sha256 확인."""
    local = ROOT / topic / "out" / vid / "final_1080p.mp4"
    if local.is_file() and local.stat().st_size == v["size"] and sha256_of(local) == v["sha256"]:
        log("SOURCE", video=vid, source="out/ (sha256 같음)", mb=round(v["size"] / 1e6, 1))
        return local
    if any(f"{v['dir']}/{x['name']}" not in upl_paths for x in v["parts"]):
        log("SOURCE", level="warn", video=vid, why="uploads 브랜치에 조각이 다 없음 — 미리보기 영상 못 만듦", next="upload_pack.py pack")
        return None
    dst = work / f"{vid}.src.mp4"
    with open(dst, "wb") as f:
        for x in v["parts"]:
            r = subprocess.run(["git", "-C", str(ROOT), "cat-file", "blob", f"origin/{up.BRANCH}:{v['dir']}/{x['name']}"], capture_output=True)
            if r.returncode != 0:
                log("SOURCE", level="error", video=vid, part=x["name"], error=r.stderr.decode()[:160], next="git fetch origin uploads")
                return None
            f.write(r.stdout)
    if sha256_of(dst) != v["sha256"]:
        log("SOURCE", level="error", video=vid, why="이어 붙인 영상의 sha256 이 video.json 과 다름 — 미리보기 영상 안 만듦", next="upload_pack.py pack 다시")
        dst.unlink(missing_ok=True)
        return None
    log("SOURCE", video=vid, source=f"uploads 브랜치 조각 {len(v['parts'])}개 (sha256 같음)", mb=round(v["size"] / 1e6, 1))
    return dst


def preview_video(topic: str, vid: str, v: dict, upl_paths: set[str], out: Path) -> dict | None:
    """미리보기용 낮은 화질 mp4 (PREVIEW_MAX_MB 아래). 원본 sha256 이 같으면 지난번 것을 다시 씀 (다시 인코딩하지 않음)."""
    work = out / "video" / topic
    work.mkdir(parents=True, exist_ok=True)
    cache = work / f"{vid}.{v['sha256'][:12]}.mp4"
    pub = f"video/{topic}/{vid}.mp4"
    if cache.is_file() and cache.stat().st_size <= PREVIEW_MAX_MB * 1e6:
        log("PREVIEW", video=vid, cache="hit", mb=round(cache.stat().st_size / 1e6, 1))
        return {"path": pub, "src": cache, "mb": round(cache.stat().st_size / 1e6, 1), "res": cache.name}
    for old in work.glob(f"{vid}.*.mp4"):                    # 원본이 바뀐 지난 미리보기는 지움 (.yt_work 안 — 저장소 밖)
        old.unlink()
    src = source_mp4(topic, vid, v, upl_paths, work)
    if not src:
        return None
    pr = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height:format=duration",
                         "-of", "json", str(src)], capture_output=True, text=True)
    try:
        info = json.loads(pr.stdout)
        w, h = info["streams"][0]["width"], info["streams"][0]["height"]
        dur = float(info["format"]["duration"])
    except (KeyError, IndexError, ValueError, json.JSONDecodeError) as e:
        log("PREVIEW", level="error", video=vid, stage="ffprobe", error=str(e)[:120], next="원본 영상 확인")
        return None
    total = PREVIEW_MAX_MB * 0.93 * 8000 / dur                # kbit/s (MB = 1e6 바이트) — 7% 여유
    vb = int(min(900, total - AUDIO_KBPS - 6))
    t0 = time.time()
    for attempt in range(3):
        side = 480 if vb >= 600 else 360 if vb >= 150 else 240
        scale = f"scale=-2:{side}" if w >= h else f"scale={side}:-2"   # 세로 쇼츠는 가로를 맞춤
        tmp = cache.with_suffix(".tmp.mp4")
        cmd = ["ffmpeg", "-y", "-v", "error", "-i", str(src), "-vf", scale, "-c:v", "libx264", "-preset", "medium", "-profile:v", "main",
               "-pix_fmt", "yuv420p", "-b:v", f"{vb}k", "-maxrate", f"{int(vb * 1.5)}k", "-bufsize", f"{vb * 2}k",
               "-c:a", "aac", "-b:a", f"{AUDIO_KBPS}k", "-ac", "1", "-movflags", "+faststart", str(tmp)]
        try:
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=1800)
        except subprocess.TimeoutExpired:
            log("PREVIEW", level="error", video=vid, stage="ffmpeg", error="30분 넘음", next="--no-video 로 링크만")
            return None
        if r.returncode != 0:
            log("PREVIEW", level="error", video=vid, stage="ffmpeg", error=r.stderr[-200:], next="ffmpeg 설치·원본 확인")
            return None
        mb = tmp.stat().st_size / 1e6
        log("PREVIEW", video=vid, attempt=attempt + 1, side=f"{side}p", video_kbps=vb, audio_kbps=AUDIO_KBPS, mb=round(mb, 2), limit_mb=PREVIEW_MAX_MB)
        if mb <= PREVIEW_MAX_MB:
            tmp.replace(cache)
            break
        vb = int(vb * PREVIEW_MAX_MB / mb * 0.92)            # 넘으면 비율대로 줄여 다시
    else:
        log("PREVIEW", level="error", video=vid, why=f"세 번 해도 {PREVIEW_MAX_MB}MB 넘음 — 링크만", next="PREVIEW_MAX_MB 확인")
        return None
    if src.name.endswith(".src.mp4"):
        src.unlink(missing_ok=True)                          # 이어 붙인 원본은 남기지 않음 (용량)
    log("PREVIEW", video=vid, cache="new", mb=round(cache.stat().st_size / 1e6, 1), sec=round(time.time() - t0, 1))
    return {"path": pub, "src": cache, "mb": round(cache.stat().st_size / 1e6, 1), "res": f"{side}p"}


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


def _norm(t: str) -> str:
    return re.sub(r"[\W_]+", "", t)


def script_of(src: Path, vid: str) -> dict | None:
    """(v1.2) 대본 <영상ID>.txt → 챕터별 문장 · 예상 길이(H17 6.3음절/초 + 쉼 0.35초) · 음성 비교.
    stale = 대본 문장 가운데 지금 SRT(= 지금 음성의 자막) 글에 없는 문장 수 — 0 이 아니면 음성·영상이 아직 옛 대본."""
    p = src / f"{vid}.txt"
    if not p.is_file():
        return None
    parts, cur = [], None
    for ln in p.read_text("utf-8").splitlines():
        ln = ln.strip()
        if not ln:
            continue
        if ln.startswith("-"):
            cur = {"name": ln[1:].strip(), "lines": []}
            parts.append(cur)
        else:
            if cur is None:
                cur = {"name": "", "lines": []}
                parts.append(cur)
            cur["lines"].append(ln)
    sents = [x for pt in parts for x in pt["lines"]]
    syl = sum(len(re.findall(r"[가-힣0-9]", x)) for x in sents)
    est = syl / 6.3 + 0.35 * len(sents)
    srt = src / f"{vid}.srt"
    stale, first = None, []
    if srt.is_file():
        body = []
        for b in re.split(r"\r?\n\r?\n", srt.read_text("utf-8-sig").strip()):
            ln = b.strip().splitlines()
            if len(ln) >= 3 and "-->" in ln[1]:
                body.append(" ".join(ln[2:]))
        allt = _norm(" ".join(body))
        miss = [x for x in sents if _norm(x) not in allt]
        stale, first = len(miss), miss[:3]
    rec = {"file": str(p.relative_to(ROOT)), "parts": parts, "sentences": len(sents), "est": f"{int(est // 60)}분 {int(est % 60):02d}초",
           "stale": stale, "stale_first": first}
    text = "\n\n".join((f"[{pt['name']}]\n" if pt["name"] else "") + "\n".join(pt["lines"]) for pt in parts)
    log("SCRIPT", vid=vid, sentences=len(sents), est=rec["est"], stale=stale)
    return {"script": rec, "script_text": text}


def record(topic: str, vid: str, upl_paths: set[str], out: Path | None = None, make_video: bool = True) -> tuple[dict, dict]:
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
    rec.update(script_of(src, vid) or {"script": None, "script_text": ""})           # v1.2 대본 전체 · 음성 비교
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
        rec["video"] = {"mb": round(v["size"] / 1e6), "parts": len(v["parts"]), "on_branch": not missing, "duration_s": v.get("duration_s"),
                        "folder": f"https://github.com/{REPO}/tree/{up.BRANCH}/{v['dir']}",                          # v1.1 원본 링크 (공개 저장소)
                        "raw": f"https://github.com/{REPO}/raw/{up.BRANCH}/{v['dir']}/{v['parts'][0]['name']}" if len(v["parts"]) == 1 else ""}
    else:
        rec["video"] = None
    rec["preview"] = None
    if status == "waiting" and rec["video"] and rec["video"]["on_branch"] and make_video and out is not None:   # v1.1 미리보기 영상
        pv = preview_video(topic, vid, v, upl_paths, out)
        if pv:
            files[pv["path"]] = str(pv["src"].relative_to(ROOT)) if pv["src"].resolve().is_relative_to(ROOT) else str(pv["src"])
            rec["preview"] = {"path": pv["path"], "mb": pv["mb"], "res": pv["res"]}
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


def build(out: Path, which: str, make_video: bool = True) -> int:
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
                rec, f = record(topic, vid, upl, out, make_video and which != "uploaded")
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
    keep = {t["path"] for r in vids for t in r["thumbs"]} | {r["preview"]["path"] for r in vids if r.get("preview")}
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
        preview_videos=sum(1 for r in vids if r.get("preview")),
        files=len(files), mb=round(mb, 1), data_kb=round(len(body.encode()) / 1024), failed=",".join(fails) or "-",
        out=str(out), sec=round(time.time() - t0, 1), next="Artifact 도구 files = files.json · file_path = tools/upload_preview/index.html")
    if mb > MAX_PUBLISH_MB:
        log("WARN", mb=round(mb, 1), limit=MAX_PUBLISH_MB, next="--status waiting 으로 줄이거나 두 번에 나눠 올림")
    return 1 if fails else 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="업로드 미리보기 아티팩트 자료 (data.json · files.json)")
    ap.add_argument("--out", default=str(ROOT / ".yt_work" / "upload_preview"))
    ap.add_argument("--status", choices=("waiting", "uploaded", "all"), default="all")
    ap.add_argument("--no-video", action="store_true", help="미리보기 영상을 만들지 않음 (원본·유튜브 링크만)")
    a = ap.parse_args(argv)
    return build(Path(a.out).resolve(), a.status, not a.no_video)


if __name__ == "__main__":
    sys.exit(main())
