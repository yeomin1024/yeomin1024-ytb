#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-10 — 완성 영상을 유튜브에 비공개로 업로드 (제목·설명란·태그·카테고리·자막·썸네일 1개), 표준 라이브러리만
r"""
업로드 시트(upload.md)대로 완성 영상을 유튜브에 **비공개**로 올립니다. (guides/pipeline.md 4단계, guides/upload_guide.md 9번)

  python tools/youtube_upload.py stock bittu-2026-10 --dry-run     # 올리지 않고 읽은 값·파일·규칙만 확인
  python tools/youtube_upload.py stock bittu-2026-10               # 비공개 업로드 → source/<영상ID>/youtube.json 기록
  python tools/youtube_upload.py --check-auth                      # 키로 채널 이름만 확인 (업로드 안 함)

필요한 환경변수 (클라우드 환경 설정 — 값은 출력·커밋하지 않음):
  YOUTUBE_CLIENT_ID, YOUTUBE_CLIENT_SECRET, YOUTUBE_REFRESH_TOKEN   ← tools/youtube_auth.py 로 한 번 발급

읽는 파일 (<주제폴더>/ 기준):
  source/<영상ID>/upload.md          1번 제목 · 2번 설명란 · 3번 챕터 명령(--chapters) · 4번 태그 (각 섹션의 첫 코드 블록)
  source/<영상ID>/<영상ID>.txt·.srt  챕터를 지금 SRT(= 영상 시간)로 다시 계산해 설명란 "■ 챕터"를 바꿔 넣음
  out/<영상ID>/final_1080p.mp4       올릴 영상
  out/<영상ID>/thumbnails/thumbnail_1.png (또는 .jpg)   기본 썸네일 (채택 제목의 짝). 2MB 이하

API로 할 수 없는 것 (스튜디오에서 직접): 썸네일 "테스트 및 비교"(3개), 최종 화면, 공개 전환.
  ⚠️ Google 감사를 받지 않은 API 프로젝트로 올린 영상은 비공개로 잠긴다 → guides/pipeline.md "업로드 주의"
"""
import argparse
import datetime as dt
import hashlib
import json
import mimetypes
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKEN_URL = "https://oauth2.googleapis.com/token"
API = "https://www.googleapis.com/youtube/v3"
UPLOAD_API = "https://www.googleapis.com/upload/youtube/v3"
CATEGORY_EDUCATION = "27"
CHUNK = 8 * 1024 * 1024
THUMB_MAX = 2 * 1024 * 1024
MAX_TITLE, MAX_DESC, MAX_TAGS = 100, 5000, 500


def log(stage, **kv):
    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print(f"[{stage}] [{now}] " + " ".join(f"{k}={v}" for k, v in kv.items()), flush=True)


# ----------------------------------------------------------------------------- upload.md 읽기
def _section_code(md, heading_word):
    """'## N. <heading_word>…' 섹션의 첫 코드 블록 내용."""
    m = re.search(rf"^##\s*\d+\.\s*[^\n]*{heading_word}[^\n]*\n(.*?)(?=^##\s|\Z)", md, re.M | re.S)
    if not m:
        return None
    c = re.search(r"```[^\n]*\n(.*?)\n```", m.group(1), re.S)
    return c.group(1) if c else None


def read_sheet(topic, vid):
    src = ROOT / topic / "source" / vid
    md = (src / "upload.md").read_text("utf-8")
    title = (_section_code(md, "제목") or "").strip()
    desc = _section_code(md, "설명란") or ""
    tags_raw = _section_code(md, "태그") or ""
    cmd = _section_code(md, "챕터") or ""
    spec = re.search(r'--chapters\s+"([^"]+)"', cmd)
    tags = [t.strip() for t in tags_raw.replace("\n", ",").split(",") if t.strip()]
    return {"title": title, "description": desc, "tags": tags, "chapter_spec": spec.group(1) if spec else None}


def recompute_chapters(topic, vid, desc, spec):
    """지금 SRT(= 영상 시간)로 챕터를 다시 계산해 설명란 '■ 챕터' 줄을 바꾼다 (align-audio 뒤 시간이 바뀌므로)."""
    if not spec:
        log("CHAPTER", status="skip", reason="upload.md 3번에 --chapters 명령 없음 → 설명란 챕터 그대로")
        return desc, None
    src = ROOT / topic / "source" / vid
    out = subprocess.run([sys.executable, str(ROOT / "tools" / "srt_tool.py"), "upload", str(src / f"{vid}.txt"),
                          str(src / f"{vid}.srt"), "--chapters", spec], capture_output=True, text=True)
    lines = [l for l in out.stdout.splitlines() if re.match(r"^\d+:\d\d(:\d\d)? ", l)]
    ok = "✅" in out.stdout and out.returncode == 0
    if not ok or not lines:
        raise SystemExit(f"[CHAPTER] ❌ 챕터 규칙 실패 → srt_tool.py upload 출력 확인\n{out.stdout[-800:]}{out.stderr[-400:]}")
    m = re.search(r"(■ 챕터\n)((?:\d+:\d\d(?::\d\d)? [^\n]*\n?)+)", desc)
    if not m:
        raise SystemExit("[CHAPTER] ❌ 설명란에 '■ 챕터' 줄 묶음이 없습니다 (upload.md 2번)")
    old = [l for l in m.group(2).splitlines() if l.strip()]
    new_desc = desc[:m.start(2)] + "\n".join(lines) + "\n" + desc[m.end(2):]
    changed = sum(a != b for a, b in zip(old, lines)) + abs(len(old) - len(lines))
    log("CHAPTER", status="ok", chapters=len(lines), changed_lines=changed)
    return new_desc, lines


def tags_length(tags):
    # YouTube는 공백이 든 태그를 따옴표로 감싸 센다 (+2), 태그 사이 쉼표 포함
    return sum(len(t) + (2 if " " in t else 0) for t in tags) + max(0, len(tags) - 1)


def validate(meta):
    problems = []
    if not meta["title"]:
        problems.append("제목 없음 (upload.md 1번 코드 블록)")
    if len(meta["title"]) > MAX_TITLE:
        problems.append(f"제목 {len(meta['title'])}자 > {MAX_TITLE}")
    if len(meta["description"]) > MAX_DESC:
        problems.append(f"설명란 {len(meta['description'])}자 > {MAX_DESC}")
    for field in ("title", "description"):
        if re.search(r"[<>]", meta[field]):
            problems.append(f"{field}에 < > 문자 (유튜브가 거부)")
    if tags_length(meta["tags"]) > MAX_TAGS:
        problems.append(f"태그 {tags_length(meta['tags'])}자 > {MAX_TAGS}")
    return problems


# ----------------------------------------------------------------------------- OAuth · HTTP
def access_token():
    need = ("YOUTUBE_CLIENT_ID", "YOUTUBE_CLIENT_SECRET", "YOUTUBE_REFRESH_TOKEN")
    missing = [k for k in need if not os.environ.get(k, "").strip()]
    if missing:
        raise SystemExit(f"[AUTH] ❌ 환경변수 없음: {', '.join(missing)} → guides/pipeline.md '처음 한 번 할 일' 2번 (tools/youtube_auth.py)")
    body = urllib.parse.urlencode({"client_id": os.environ["YOUTUBE_CLIENT_ID"].strip(),
                                   "client_secret": os.environ["YOUTUBE_CLIENT_SECRET"].strip(),
                                   "refresh_token": os.environ["YOUTUBE_REFRESH_TOKEN"].strip(),
                                   "grant_type": "refresh_token"}).encode()
    try:
        with urllib.request.urlopen(urllib.request.Request(TOKEN_URL, data=body), timeout=30) as r:
            return json.load(r)["access_token"]
    except urllib.error.HTTPError as e:
        detail = e.read().decode(errors="replace")[:300]
        hint = " → 토큰이 만료·취소됨. OAuth 동의 화면이 '테스트' 상태면 7일마다 만료되니 '프로덕션'으로 바꾸고 youtube_auth.py 다시 실행" \
            if "invalid_grant" in detail else ""
        raise SystemExit(f"[AUTH] ❌ 토큰 갱신 실패 ({e.code}): {detail}{hint}")


def request(method, url, token, data=None, headers=None, retries=4):
    headers = {"Authorization": f"Bearer {token}", **(headers or {})}
    for attempt in range(retries + 1):
        req = urllib.request.Request(url, data=data, method=method, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=600) as r:
                raw = r.read()
                return r.status, dict(r.headers), (json.loads(raw) if raw else {})
        except urllib.error.HTTPError as e:
            raw = e.read()
            if e.code == 308:                       # 이어 올리기: 아직 덜 받음
                return 308, dict(e.headers), {}
            if e.code in (500, 502, 503, 504) and attempt < retries:
                wait = 2 ** (attempt + 1)
                log("HTTP", status=e.code, retry_in_s=wait, url=url.split("?")[0])
                time.sleep(wait)
                continue
            raise RuntimeError(f"HTTP {e.code} {url.split('?')[0]}: {raw.decode(errors='replace')[:500]}")
        except urllib.error.URLError as e:
            if attempt < retries:
                wait = 2 ** (attempt + 1)
                log("HTTP", error=str(e.reason)[:80], retry_in_s=wait)
                time.sleep(wait)
                continue
            raise


def upload_video(token, path, meta, privacy):
    body = {"snippet": {"title": meta["title"], "description": meta["description"], "tags": meta["tags"],
                        "categoryId": CATEGORY_EDUCATION, "defaultLanguage": "ko", "defaultAudioLanguage": "ko"},
            "status": {"privacyStatus": privacy, "selfDeclaredMadeForKids": False, "embeddable": True}}
    size = path.stat().st_size
    status, headers, _ = request("POST", f"{UPLOAD_API}/videos?uploadType=resumable&part=snippet,status", token,
                                 data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json; charset=UTF-8",
                                          "X-Upload-Content-Type": "video/mp4", "X-Upload-Content-Length": str(size)})
    session = headers.get("Location") or headers.get("location")
    if not session:
        raise RuntimeError("업로드 세션 주소(Location)를 받지 못함")
    sent = 0
    t0 = time.time()
    with path.open("rb") as f:
        while sent < size:
            f.seek(sent)
            chunk = f.read(CHUNK)
            end = sent + len(chunk) - 1
            status, headers, resp = request("PUT", session, token, data=chunk,
                                            headers={"Content-Length": str(len(chunk)),
                                                     "Content-Range": f"bytes {sent}-{end}/{size}"})
            if status in (200, 201):
                log("UPLOAD", progress="100%", seconds=f"{time.time() - t0:.0f}")
                return resp["id"]
            rng = headers.get("Range") or headers.get("range")
            sent = int(rng.split("-")[1]) + 1 if rng else end + 1
            log("UPLOAD", progress=f"{sent * 100 // size}%", sent_mb=f"{sent / 1e6:.0f}", total_mb=f"{size / 1e6:.0f}")
    raise RuntimeError("업로드가 끝났는데 영상 ID를 받지 못함")


def upload_captions(token, video_id, srt_path):
    boundary = uuid.uuid4().hex
    meta = json.dumps({"snippet": {"videoId": video_id, "language": "ko", "name": "한국어", "isDraft": False}})
    body = (f"--{boundary}\r\nContent-Type: application/json; charset=UTF-8\r\n\r\n{meta}\r\n"
            f"--{boundary}\r\nContent-Type: application/octet-stream\r\n\r\n").encode() + srt_path.read_bytes() + \
           f"\r\n--{boundary}--\r\n".encode()
    _, _, resp = request("POST", f"{UPLOAD_API}/captions?uploadType=multipart&part=snippet", token, data=body,
                         headers={"Content-Type": f"multipart/related; boundary={boundary}"})
    return resp.get("id")


def upload_thumbnail(token, video_id, img):
    ctype = mimetypes.guess_type(img.name)[0] or "image/png"
    request("POST", f"{UPLOAD_API}/thumbnails/set?videoId={video_id}&uploadType=media", token,
            data=img.read_bytes(), headers={"Content-Type": ctype})


def check_auth():
    token = access_token()
    _, _, resp = request("GET", f"{API}/channels?part=snippet&mine=true", token)
    items = resp.get("items", [])
    if not items:
        raise SystemExit("[AUTH] ❌ 이 계정에 유튜브 채널이 없습니다")
    log("AUTH", status="ok", channel=items[0]["snippet"]["title"], channel_id=items[0]["id"])


def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


# ----------------------------------------------------------------------------- 실행
def run(topic, vid, dry_run=False, privacy="private", force=False, no_captions=False, no_thumbnail=False, video=None):
    src = ROOT / topic / "source" / vid
    out = ROOT / topic / "out" / vid
    state_path = src / "youtube.json"
    if state_path.exists() and not force:
        st = json.loads(state_path.read_text("utf-8"))
        log("SKIP", video=vid, reason="이미 업로드됨", youtube_id=st.get("videoId"), hint="--force 로 다시 올림")
        return st
    video_path = Path(video) if video else out / "final_1080p.mp4"
    srt_path = src / f"{vid}.srt"
    thumbs = [p for p in (out / "thumbnails" / "thumbnail_1.png", out / "thumbnails" / "thumbnail_1.jpg") if p.exists()]
    meta = read_sheet(topic, vid)
    meta["description"], chapter_lines = recompute_chapters(topic, vid, meta["description"], meta["chapter_spec"])
    problems = validate(meta)
    log("SHEET", video=vid, title_chars=len(meta["title"]), desc_chars=len(meta["description"]),
        tags=len(meta["tags"]), tags_chars=tags_length(meta["tags"]))
    log("FILES", video_file=f"{video_path.relative_to(ROOT) if video_path.is_relative_to(ROOT) else video_path}"
        f"({'있음' if video_path.exists() else '없음'})", srt="있음" if srt_path.exists() else "없음",
        thumbnail=thumbs[0].name if thumbs else "없음")
    if not video_path.exists():
        problems.append(f"영상 파일 없음: {video_path} → 먼저 렌더 (guides/pipeline.md 4단계)")
    if thumbs and thumbs[0].stat().st_size > THUMB_MAX:
        problems.append(f"썸네일 {thumbs[0].stat().st_size / 1e6:.1f}MB > 2MB → JPG로 다시 저장")
    for p in problems:
        log("CHECK", problem=p)
    if dry_run:
        print(f"\n제목: {meta['title']}\n태그: {', '.join(meta['tags'])}\n--- 설명란 ---\n{meta['description']}\n---")
        log("DRY-RUN", result="문제 없음" if not problems else f"문제 {len(problems)}개", uploaded="안 함")
        return None
    if problems:
        raise SystemExit(f"[CHECK] ❌ 문제 {len(problems)}개 → 고친 뒤 다시 실행 (업로드 안 함)")

    token = access_token()
    log("UPLOAD", video=vid, privacy=privacy, size_mb=f"{video_path.stat().st_size / 1e6:.1f}")
    video_id = upload_video(token, video_path, meta, privacy)
    log("UPLOAD", status="ok", youtube_id=video_id, url=f"https://youtu.be/{video_id}")
    result = {"videoId": video_id, "url": f"https://youtu.be/{video_id}",
              "studio": f"https://studio.youtube.com/video/{video_id}/edit", "privacy": privacy,
              "uploadedAt": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
              "title": meta["title"], "videoFile": str(video_path.name), "videoSha256": sha256(video_path),
              "chapters": chapter_lines, "captions": None, "thumbnail": None, "warnings": []}
    if not no_captions and srt_path.exists():
        try:
            result["captions"] = upload_captions(token, video_id, srt_path)
            log("CAPTIONS", status="ok", file=srt_path.name)
        except Exception as e:                                   # 자막 실패해도 영상은 이미 올라감
            result["warnings"].append(f"자막 실패: {e}")
            log("CAPTIONS", status="fail", error=str(e)[:200], next="스튜디오 → 자막에서 SRT 직접 업로드")
    if not no_thumbnail and thumbs:
        try:
            upload_thumbnail(token, video_id, thumbs[0])
            result["thumbnail"] = thumbs[0].name
            log("THUMBNAIL", status="ok", file=thumbs[0].name)
        except Exception as e:
            result["warnings"].append(f"썸네일 실패: {e}")
            log("THUMBNAIL", status="fail", error=str(e)[:200],
                next="채널 전화번호 인증(youtube.com/verify) 후 스튜디오에서 직접 등록")
    state_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", "utf-8")
    log("DONE", video=vid, state=str(state_path.relative_to(ROOT)), studio=result["studio"])
    return result


def main(argv=None):
    ap = argparse.ArgumentParser(description="완성 영상을 유튜브에 비공개 업로드 (upload.md 기준)")
    ap.add_argument("topic", nargs="?", help="주제 폴더 (예: stock)")
    ap.add_argument("video_id", nargs="?", help="영상 ID (예: bittu-2026-10)")
    ap.add_argument("--dry-run", action="store_true", help="올리지 않고 확인만")
    ap.add_argument("--check-auth", action="store_true", help="키로 채널 이름만 확인")
    ap.add_argument("--privacy", default="private", choices=["private", "unlisted", "public"])
    ap.add_argument("--force", action="store_true", help="youtube.json이 있어도 다시 올림")
    ap.add_argument("--video", help="영상 파일 경로 (기본: <주제>/out/<영상ID>/final_1080p.mp4)")
    ap.add_argument("--no-captions", action="store_true")
    ap.add_argument("--no-thumbnail", action="store_true")
    a = ap.parse_args(argv)
    if a.check_auth:
        return check_auth()
    if not a.topic or not a.video_id:
        ap.error("주제 폴더와 영상 ID가 필요합니다 (예: stock bittu-2026-10)")
    if a.privacy != "private":
        log("WARN", privacy=a.privacy, note="지시사항 기본은 비공개(private)")
    run(a.topic, a.video_id, a.dry_run, a.privacy, a.force, a.no_captions, a.no_thumbnail, a.video)


if __name__ == "__main__":
    main()
