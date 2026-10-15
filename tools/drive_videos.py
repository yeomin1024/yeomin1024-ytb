#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-15 — 사용자 지시 "압축본 올린거 삭제하고 구글 드라이브 내 드라이브에 youtube 폴더에 주제 (예: economic)맞는 폴더에
#          원본 영상 올리고 pc에서 영상 및 환경설정을 받아서 업로드 하는 코드 만들어서 올리는 걸로 하자": 완성 영상 원본을
#          Google Drive '내 드라이브/youtube/<주제>/<영상ID>.mp4' 에 올리고(클라우드 — Claude), 찾아서 받는다(PC — tools/pc_upload.py).
r"""
완성 영상 원본 ↔ Google Drive '내 드라이브/youtube/<주제>/<영상ID>.mp4'. 표준 라이브러리만 씁니다.

  python tools/drive_videos.py upload economic eunte-kkeonaeseugi-2026-10   # out/<영상ID>/final_1080p.mp4 → Drive (같은 내용이면 건너뜀)
  python tools/drive_videos.py upload economic --all                        # out/ 에 완성 영상이 있는 영상 전부
  python tools/drive_videos.py list economic                                # Drive 의 youtube/economic 영상 목록
  python tools/drive_videos.py download economic <영상ID> --dest 파일.mp4    # 받기 (md5 확인)
  python tools/drive_videos.py check                                        # 키에 Drive 권한이 있는지만 확인

키 (환경 변수 — 유튜브 업로드와 같은 OAuth): YOUTUBE_CLIENT_ID · YOUTUBE_CLIENT_SECRET · YOUTUBE_REFRESH_TOKEN
  ※ 리프레시 토큰에 Drive 권한(https://www.googleapis.com/auth/drive)이 있어야 한다 → tools/youtube_auth.py v1.2 로 한 번 다시 발급,
    같은 Google Cloud 프로젝트에서 'Google Drive API' 사용 설정 (guides/pipeline.md '처음 한 번 할 일' B).
  ※ 사용자가 직접 만든 '내 드라이브/youtube/economic' 폴더도 써야 해서 drive.file(앱이 만든 파일만)이 아니라 drive 권한이다.
기록: 올리면 <주제>/source/<영상ID>/drive.json (파일 ID·크기·md5·올린 시각) — PC 가 받은 파일을 이 md5 로 확인한다.
PC 의 'Google Drive 데스크톱' 폴더(G:\내 드라이브\youtube\… 등)가 있으면 받지 않고 그 파일을 바로 쓴다 (local_video, 환경 변수 DRIVE_DIR).
※ 연구·교육용 도구다. 영상 내용은 투자·세무·보험 상담이나 권유가 아니다.
"""
import argparse
import datetime as dt
import hashlib
import json
import os
import re
import string
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent
sys.path.insert(0, str(TOOLS))
import youtube_upload as yu  # noqa: E402

VERSION = "v1.0"
API = "https://www.googleapis.com/drive/v3"
UPLOAD_API = "https://www.googleapis.com/upload/drive/v3"
FOLDER = "application/vnd.google-apps.folder"
TOP = "youtube"                     # 내 드라이브/youtube/<주제>/
CHUNK = 8 * 1024 * 1024             # 256KB 의 배수
FIELDS = "id,name,size,md5Checksum,modifiedTime,appProperties,parents"
SCOPE_HINT = ("키에 Google Drive 권한이 없음 → PC 에서 python tools/youtube_auth.py (v1.2, Drive 권한 포함) 를 한 번 다시 실행해 새 "
              "YOUTUBE_REFRESH_TOKEN 을 받고, 클라우드 환경 변수와 PC .env 를 바꾸기. 같은 프로젝트에서 'Google Drive API' 사용 설정 "
              "(guides/pipeline.md '처음 한 번 할 일' B)")


def log(stage, **kv):
    yu.log(stage, **kv)


class DriveError(RuntimeError):
    pass


def call(method, url, token, data=None, headers=None):
    """youtube_upload.request 와 같은 재시도 — 권한·API 꺼짐은 알아보기 쉬운 오류로."""
    try:
        return yu.request(method, url, token, data=data, headers=headers)
    except RuntimeError as e:
        msg = str(e)
        if "insufficient" in msg.lower() or "ACCESS_TOKEN_SCOPE_INSUFFICIENT" in msg:
            raise DriveError(SCOPE_HINT) from None
        if "accessNotConfigured" in msg or "SERVICE_DISABLED" in msg:
            raise DriveError("이 Google Cloud 프로젝트에서 'Google Drive API' 가 꺼져 있음 → 콘솔 → API 및 서비스 → 라이브러리 → Google Drive API → 사용") from None
        raise


def q_str(s):
    return "'" + s.replace("\\", "\\\\").replace("'", "\\'") + "'"


def search(token, q, fields=FIELDS):
    url = f"{API}/files?" + urllib.parse.urlencode({"q": q, "fields": f"files({fields})", "spaces": "drive", "pageSize": 100,
                                                     "orderBy": "modifiedTime desc"})
    return call("GET", url, token)[2].get("files", [])


def find_folder(token, name, parent):
    hits = search(token, f"name = {q_str(name)} and mimeType = '{FOLDER}' and {q_str(parent)} in parents and trashed = false", "id,name")
    return hits[0]["id"] if hits else None


def topic_folder(token, topic, create=False):
    """내 드라이브/youtube/<주제> 폴더 ID (없으면 create 일 때 만든다, 아니면 None)."""
    ids = []
    parent = "root"
    for name in (TOP, topic):
        fid = find_folder(token, name, parent)
        if not fid:
            if not create:
                return None
            _, _, r = call("POST", f"{API}/files?fields=id", token, data=json.dumps({"name": name, "mimeType": FOLDER, "parents": [parent]}).encode(),
                           headers={"Content-Type": "application/json; charset=UTF-8"})
            fid = r["id"]
            log("DRIVE", created_folder="/".join([TOP, topic][: len(ids) + 1]), id=fid)
        ids.append(fid)
        parent = fid
    return parent


def find_video(token, topic, vid, folder=None):
    folder = folder or topic_folder(token, topic)
    if not folder:
        return None
    hits = search(token, f"name = {q_str(vid + '.mp4')} and {q_str(folder)} in parents and trashed = false")
    return hits[0] if hits else None


def list_videos(token, topic):
    folder = topic_folder(token, topic)
    if not folder:
        return []
    return [f for f in search(token, f"{q_str(folder)} in parents and trashed = false and mimeType != '{FOLDER}'") if f["name"].endswith(".mp4")]


def md5(path):
    h = hashlib.md5()
    with Path(path).open("rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def _resumable(token, method, url, meta, path):
    size = path.stat().st_size
    _, headers, _ = call(method, url, token, data=json.dumps(meta).encode(),
                         headers={"Content-Type": "application/json; charset=UTF-8", "X-Upload-Content-Type": "video/mp4",
                                  "X-Upload-Content-Length": str(size)})
    session = headers.get("Location") or headers.get("location")
    if not session:
        raise DriveError("Drive 업로드 세션 주소(Location)를 받지 못함")
    sent, t0 = 0, time.time()
    with path.open("rb") as f:
        while sent < size:
            f.seek(sent)
            chunk = f.read(CHUNK)
            end = sent + len(chunk) - 1
            status, h, resp = call("PUT", session, token, data=chunk,
                                   headers={"Content-Length": str(len(chunk)), "Content-Range": f"bytes {sent}-{end}/{size}"})
            if status in (200, 201):
                log("DRIVE", upload="100%", seconds=f"{time.time() - t0:.0f}", mb=f"{size / 1e6:.1f}")
                return resp
            rng = h.get("Range") or h.get("range")
            sent = int(rng.split("-")[1]) + 1 if rng else end + 1
            log("DRIVE", upload=f"{sent * 100 // size}%")
    raise DriveError("업로드가 끝났는데 파일 정보를 받지 못함")


def upload(topic, vid, src=None, token=None):
    """out/<영상ID>/final_1080p.mp4 → 내 드라이브/youtube/<주제>/<영상ID>.mp4 (있으면 같은 파일을 새 내용으로, md5 가 같으면 건너뜀)
    → <주제>/source/<영상ID>/drive.json 기록."""
    src = Path(src) if src else ROOT / topic / "out" / vid / "final_1080p.mp4"
    if not src.is_file():
        raise SystemExit(f"[DRIVE] ❌ 영상 없음: {src} → 먼저 렌더 (node video/render/render.mjs video {topic} {vid})")
    token = token or yu.access_token()
    local_md5, size = md5(src), src.stat().st_size
    folder = topic_folder(token, topic, create=True)
    old = find_video(token, topic, vid, folder)
    props = {"video_id": vid, "topic": topic, "tool": f"drive_videos {VERSION}"}
    if old and old.get("md5Checksum") == local_md5:
        log("DRIVE", video=vid, action="skip", reason="같은 내용이 이미 있음", file_id=old["id"])
        res = old
    elif old:
        log("DRIVE", video=vid, action="replace", file_id=old["id"], old_md5=old.get("md5Checksum"), new_md5=local_md5)
        res = _resumable(token, "PATCH", f"{UPLOAD_API}/files/{old['id']}?uploadType=resumable&fields={FIELDS}", {"appProperties": props}, src)
    else:
        log("DRIVE", video=vid, action="upload", folder=f"{TOP}/{topic}", mb=f"{size / 1e6:.1f}")
        res = _resumable(token, "POST", f"{UPLOAD_API}/files?uploadType=resumable&fields={FIELDS}",
                         {"name": f"{vid}.mp4", "parents": [folder], "mimeType": "video/mp4", "appProperties": props}, src)
    if res.get("md5Checksum") and res["md5Checksum"] != local_md5:
        raise DriveError(f"Drive md5 {res['md5Checksum']} ≠ 로컬 {local_md5} — 다시 올리기")
    rec = {"tool": f"drive_videos.py {VERSION}", "uploadedAt": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
           "path": f"내 드라이브/{TOP}/{topic}/{vid}.mp4", "fileId": res["id"], "size": size, "md5": local_md5,
           "url": f"https://drive.google.com/file/d/{res['id']}/view", "source": str(src.relative_to(ROOT)) if src.is_relative_to(ROOT) else str(src)}
    dst = ROOT / topic / "source" / vid / "drive.json"
    if dst.parent.is_dir():
        dst.write_text(json.dumps(rec, ensure_ascii=False, indent=1) + "\n", "utf-8")
    log("DRIVE", video=vid, done=True, file_id=res["id"], md5=local_md5, record=str(dst.relative_to(ROOT)) if dst.parent.is_dir() else "-")
    return rec


def download(file, dest, token=None):
    """Drive 파일 → dest (이미 같은 md5 면 건너뜀). 받은 뒤 md5 확인. → dest"""
    dest = Path(dest)
    want = file.get("md5Checksum")
    if dest.is_file() and want and md5(dest) == want:
        log("DRIVE", download="skip", reason="같은 파일이 이미 있음", dest=str(dest))
        return dest
    token = token or yu.access_token()
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_suffix(dest.suffix + ".part")
    req = urllib.request.Request(f"{API}/files/{file['id']}?alt=media", headers={"Authorization": f"Bearer {token}"})
    h, got, t0 = hashlib.md5(), 0, time.time()
    try:
        with urllib.request.urlopen(req, timeout=600) as r, tmp.open("wb") as f:
            while True:
                b = r.read(CHUNK)
                if not b:
                    break
                f.write(b)
                h.update(b)
                got += len(b)
    except urllib.error.HTTPError as e:
        tmp.unlink(missing_ok=True)
        body = e.read().decode(errors="replace")[:300]
        if e.code == 403 and "insufficient" in body.lower():
            raise DriveError(SCOPE_HINT) from None
        raise DriveError(f"Drive 받기 실패 HTTP {e.code}: {body}") from None
    if want and h.hexdigest() != want:
        tmp.unlink(missing_ok=True)
        raise DriveError(f"받은 파일 md5 {h.hexdigest()} ≠ Drive {want} — 다시 실행")
    tmp.replace(dest)
    log("DRIVE", download="ok", dest=str(dest), mb=f"{got / 1e6:.1f}", seconds=f"{time.time() - t0:.0f}", md5=h.hexdigest())
    return dest


# ----------------------------------------------------------------------------- PC 의 'Google Drive 데스크톱' 폴더
def local_roots():
    """'youtube' 폴더 후보: 환경 변수 DRIVE_DIR(내 드라이브 또는 그 안의 youtube 폴더) → 윈도 드라이브 문자 X:\\내 드라이브 · X:\\My Drive
    → macOS ~/Library/CloudStorage/GoogleDrive-*/내 드라이브. 있는 것만."""
    cands = []
    d = os.environ.get("DRIVE_DIR", "").strip().strip('"')
    if d:
        p = Path(d)
        cands += [p, p / TOP] if p.name.lower() != TOP else [p]
    if os.name == "nt":
        for letter in string.ascii_uppercase[3:]:
            for my in ("내 드라이브", "My Drive"):
                cands.append(Path(f"{letter}:\\") / my / TOP)
    for base in Path.home().glob("Library/CloudStorage/GoogleDrive-*"):
        for my in ("내 드라이브", "My Drive"):
            cands.append(base / my / TOP)
    seen, out = set(), []
    for c in cands:
        try:
            if c.name.lower() == TOP and c.is_dir() and str(c) not in seen:
                seen.add(str(c))
                out.append(c)
        except OSError:
            continue
    return out


def local_video(topic, vid):
    for r in local_roots():
        p = r / topic / f"{vid}.mp4"
        if p.is_file():
            return p
    return None


def main(argv=None):
    ap = argparse.ArgumentParser(description="완성 영상 원본 ↔ Google Drive 내 드라이브/youtube/<주제>/")
    sub = ap.add_subparsers(dest="cmd", required=True)
    u = sub.add_parser("upload", help="out/<영상ID>/final_1080p.mp4 → Drive")
    u.add_argument("topic")
    u.add_argument("video_id", nargs="?")
    u.add_argument("--all", action="store_true")
    li = sub.add_parser("list", help="Drive 영상 목록")
    li.add_argument("topic")
    d = sub.add_parser("download", help="Drive → 파일")
    d.add_argument("topic")
    d.add_argument("video_id")
    d.add_argument("--dest", required=True)
    sub.add_parser("check", help="키에 Drive 권한이 있는지")
    a = ap.parse_args(argv)
    log("START", tool=f"drive_videos.py {VERSION}", cmd=a.cmd)
    try:
        if a.cmd == "upload":
            ids = sorted(p.parent.name for p in (ROOT / a.topic / "out").glob("*/final_1080p.mp4")) if a.all else [a.video_id]
            if not ids or ids == [None]:
                ap.error("영상 ID 또는 --all")
            token = yu.access_token()
            for vid in ids:
                upload(a.topic, vid, token=token)
        elif a.cmd == "list":
            files = list_videos(yu.access_token(), a.topic)
            for f in files:
                print(f"{f['name']}\t{int(f.get('size', 0)) / 1e6:.1f}MB\t{f.get('modifiedTime', '')}\t{f['id']}")
            log("LIST", topic=a.topic, videos=len(files))
        elif a.cmd == "download":
            token = yu.access_token()
            f = find_video(token, a.topic, a.video_id)
            if not f:
                raise SystemExit(f"[DRIVE] ❌ Drive 에 없음: 내 드라이브/{TOP}/{a.topic}/{a.video_id}.mp4")
            download(f, a.dest, token)
        else:
            token = yu.access_token()
            search(token, "trashed = false and 'root' in parents", "id")
            log("CHECK", drive="ok", note="키로 Drive 를 읽을 수 있음")
    except DriveError as e:
        raise SystemExit(f"[DRIVE] ❌ {e}")


if __name__ == "__main__":
    main()
