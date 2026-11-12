#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.4 — 2026-11-12 — ① '올린 적 없음' 칸 = main 기준 (main 에 youtube.json 이 없으면 ✅ — 이 PC 의 옛 youtube.json 때문에 ✗ 로 막히던 것 고침;
#          옛 기록은 v1.3 대로 업로드 때 youtube_old_<시각>.json 으로 옮김) ② 화면에서 채널 이름을 뺌 (영상 줄·키 칸 — 채널 확인은 ID 로만, 다를 때 묻는 창은 그대로).
#          사용자 지시 2026-11-12 "채널이름 빼 자꾸 영상 올린적 없음 엑스로 되어 있어서 업로드 안되잖아 수정해".
# (v1.3 — 2026-11-12 — 다시 올리기: main 에 youtube.json 이 없어 목록에 다시 나온 대본인데 이 PC 에 옛 youtube.json 이 남아 있으면
#          youtube_upload.run 이 '이미 업로드됨'으로 건너뛰고 그 옛 기록을 main 에 다시 올렸음 → 업로드 전에 이 PC 의 옛 기록을
#          youtube_old_<시각>.json 으로 옮김 (지우지 않음 · 로그 REUPLOAD). 사용자 지시 2026-11-12 "만스피 대본 잘못 올라갔는데 다시 업로드 목록에 생기도록 해줘".)
# (v1.2 — 2026-11-12 — 사용자 지시 "주식 채널명이 다르다고 업로드 실패했는데 그건 내가 채널명이 변경해서 그래 그러니까 달라도 업로드 할껀지
#          물어보고 하도록 하고 업로드 미리보기 기능도 넣어 그리고 … 3안 중 사이트에서 나한테 선택하게 하지말고 너가 가장 괜찮은걸로 하나 정해":
#   · 채널 확인 = 채널 ID(UC…) 비교 (이름만 바꾼 채널은 ID 가 같아 그대로 통과). ID 가 다르면 멈추지 않고 화면에 두 채널(이름 · ID)을 보여 주고 물음 →
#     [이 채널에 올림] (그 ID 만 이번 업로드에 허용 — youtube_upload.ALLOW_CHANNEL) · '다음부터 이 채널로 기억'(GitHub <주제>/youtube_channel.json 갱신) ·
#     [다른 채널로 다시 인증] (계정 고르기 창 — youtube_auth v1.4).
#   · [미리보기]: 올라갈 그대로 — 썸네일(본안 + 실험안) · 휴대전화 목록 모양 · 제목 · 설명란(챕터 시각을 다시 계산한 것) · 태그 · 공개 시각 · 설정 ·
#     자막 앞부분 · 고정 댓글 · 영상(받아 둔 경우 재생 — 아니면 [영상 받기]) · 자료 점검 결과. 이 PC 의 파일만 보여 줌(/media — 화면 토큰 필요).
#   · 제목 고르기 칸을 뺌 — 업로드 시트 1번의 본안 하나만 올림(Claude 가 정함), 실험안은 미리보기에 '스튜디오 테스트 및 비교용'으로만.)
# (v1.1 — 2026-11-12 — 인증 주소를 줄이지 않고 로그에(say=print) · 키가 없을 때와 토큰 만료를 다른 말로 · 화면 다듬음(긴 로그 줄바꿈 ·
#          제목 고르기 줄 · 시각 칸 너비 · 올린 영상 공개 시각을 KST 로)
# (v1.0 — 2026-11-12 — 사용자 지시 "업로드에 필요한 자료를 대본별로 저장소에 올리고 내 컴퓨터에서 자료가 다 생성됏는지 확인 후 다 된게 있으면
#          내가 업로드 버튼 누르면 일주일 후 자동 예약으로 올라가게 해줘 토큰 만료되면 알아서 인증 코드 돌려서 설정 넣어주도록 하고
#          필요한 환경변수 값들 넣을 수 있는 웹 사이트 코드 만들어줘 주제별로 가능하도록 해줘".)
#   PC 에서 켜는 업로드 화면 (이 PC 에서만 — 127.0.0.1). 실행기: run_uploader.ps1 -Web (또는 python tools/upload_web.py)
#   · 주제 탭(topics.txt + youtube_channel.json 이 있는 폴더) · 탭마다 키 칸 → <주제>/.env (YOUTUBE_CLIENT_ID · SECRET · REFRESH_TOKEN), 공통 GITHUB_TOKEN → .env
#     화면에는 값을 다시 보여 주지 않음(설정됨 · 끝 4자리만).
#   · 영상 목록 = GitHub main 의 <주제>/source/<영상ID>/upload.md 가 있고 youtube.json 이 없는 대본 → 자료 점검(제목 · 챕터 · 설명란·태그 · 자막 · 대본 ·
#     썸네일 · 합성 콘텐츠 표시 · 영상 video.json + uploads 브랜치 조각) — tools/upload_pack.py check 와 같은 규칙.
#   · [업로드] → 키 확인(만료면 브라우저 인증을 저절로 띄워 새 토큰을 <주제>/.env 에 저장하고 이어 감 — tools/youtube_auth.py issue) → 채널 확인 →
#     영상 조각을 받아 이어 붙이고 sha256 확인 → 비공개 업로드 + 예약 공개(기본 7일 뒤 17:00 KST — 화면에서 바꿈) → youtube.json 을 GitHub main 에.
#   · [시험] → 올리지 않고: 키·채널 · 시트 · 조각 있는지.
# 로그: [STAGE] [시각] key=value … (화면 아래 로그 칸에도) · ※ 연구·교육용 도구 — 영상 내용은 투자 권유가 아님.
from __future__ import annotations

import argparse
import base64
import contextlib
import datetime as dt
import hashlib
import html
import http.server
import io
import json
import os
import re
import secrets
import socket
import sys
import threading
import time
import traceback
import urllib.error
import urllib.parse
import urllib.request
import webbrowser
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent
sys.path.insert(0, str(TOOLS))
import youtube_auth as ya  # noqa: E402
import youtube_upload as yu  # noqa: E402
import upload_pack as up  # noqa: E402

VERSION = "v1.4"
REPO, MAIN, UPL = "yeomin1024/yeomin1024-ytb", "main", "uploads"
LAST_KEY_CHANNEL: dict[str, dict] = {}     # v1.2 주제 → 마지막으로 '다르다'고 나온 키의 채널 {channel_id, name} ('기억'은 이 값만 씀 — 화면이 보낸 ID 를 믿지 않음)


class ChannelMismatch(Exception):
    """v1.2 키의 채널 ID 가 <주제>/youtube_channel.json 과 다름 → 화면이 사용자에게 물음 (멈추지만 실패로 끝내지 않음)."""

    def __init__(self, info: dict):
        super().__init__(f"채널이 다름: 키 {info['key_channel']} · 기록 {info['expected']}")
        self.info = info
YT_KEYS = ("YOUTUBE_CLIENT_ID", "YOUTUBE_CLIENT_SECRET", "YOUTUBE_REFRESH_TOKEN")
KST = dt.timezone(dt.timedelta(hours=9))
WANT_FILES = ("upload.md", "titles.md", "video.json")      # + <영상ID>.txt · <영상ID>.srt · thumbnails/thumbnail_N.*
STATE = {"repo": REPO, "token": secrets.token_urlsafe(24)}


def log(stage: str, **kv) -> None:
    print(f"[{stage}] [{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}] " + " ".join(f"{k}={v}" for k, v in kv.items()), flush=True)


# ─────────── .env (값은 출력하지 않음) ───────────
def read_env(p: Path) -> dict:
    out = {}
    if p.is_file():
        for ln in p.read_text("utf-8-sig").splitlines():
            m = re.match(r"^\s*([A-Z][A-Z0-9_]*)\s*=\s*['\"]?([^'\"\r\n]*?)['\"]?\s*$", ln)
            if m and not ln.lstrip().startswith("#"):
                out[m.group(1)] = m.group(2).strip()
    return out


def mask(v: str) -> str:
    return f"설정됨 ····{v[-4:]}" if v and len(v) > 8 else ("설정됨" if v else "")


def topic_env_path(topic: str) -> Path:
    return ROOT / topic / ".env"


def apply_env(topic: str) -> dict:
    """주제의 키를 os.environ 에 (주제 .env 먼저, 없으면 공통 .env). → 어디서 온 값인지 {키: 'topic'|'root'|''}."""
    te, re_ = read_env(topic_env_path(topic)), read_env(ROOT / ".env")
    src = {}
    for k in YT_KEYS:
        v = te.get(k) or re_.get(k) or ""
        os.environ[k] = v
        src[k] = "topic" if te.get(k) else ("root" if re_.get(k) else "")
    return src


# ─────────── GitHub (읽기는 토큰 없이도 — 공개 저장소) ───────────
def gh_token() -> str:
    """공통 .env 의 GITHUB_TOKEN (없으면 환경 변수) — 주제 키를 바꾸지 않고 읽음 (작업 중 다른 탭을 눌러도 섞이지 않게)."""
    return (read_env(ROOT / ".env").get("GITHUB_TOKEN") or os.environ.get("GITHUB_TOKEN", "")).strip()


def gh_req(url: str, data=None, method=None, accept="application/vnd.github+json", timeout=60):
    h = {"Accept": accept, "X-GitHub-Api-Version": "2022-11-28", "User-Agent": "upload-web"}
    tok = gh_token()
    if tok and "api.github.com" in url:
        h["Authorization"] = f"Bearer {tok}"
    req = urllib.request.Request(url, data=data, method=method, headers=h)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read()


def gh_tree(branch: str) -> set[str]:
    st, body = gh_req(f"https://api.github.com/repos/{STATE['repo']}/git/trees/{branch}?recursive=1")
    if st == 404:
        return set()
    if st != 200:
        raise RuntimeError(f"GitHub 목록 실패 ({branch}): HTTP {st} {body[:160]!r} — 비공개 저장소면 GITHUB_TOKEN 확인 · 1시간 60번 한도면 GITHUB_TOKEN 넣기")
    j = json.loads(body)
    if j.get("truncated"):
        log("GITHUB", warning="목록이 잘림 (파일이 너무 많음) — 일부 대본이 안 보일 수 있음")
    return {e["path"] for e in j.get("tree", []) if e.get("type") == "blob"}


def gh_raw(branch: str, path: str, timeout=600) -> bytes | None:
    if gh_token():
        st, body = gh_req(f"https://api.github.com/repos/{STATE['repo']}/contents/{urllib.parse.quote(path)}?ref={branch}",
                          accept="application/vnd.github.raw", timeout=timeout)
    else:
        st, body = gh_req(f"https://raw.githubusercontent.com/{STATE['repo']}/{branch}/{urllib.parse.quote(path)}", timeout=timeout)
    if st == 404:
        return None
    if st != 200:
        raise RuntimeError(f"GitHub 받기 실패 {branch}:{path} HTTP {st}")
    return body


def gh_put_update(path: str, content: bytes, message: str) -> str:
    """(v1.2) 있는 파일을 바꿈 (sha 를 읽어 PUT). → 'updated' · 'created' · 'failed:…'."""
    if not gh_token():
        return "failed:GITHUB_TOKEN 없음"
    url = f"https://api.github.com/repos/{STATE['repo']}/contents/{urllib.parse.quote(path)}"
    st, body = gh_req(f"{url}?ref={MAIN}")
    payload = {"message": message, "content": base64.b64encode(content).decode(), "branch": MAIN}
    if st == 200:
        payload["sha"] = json.loads(body)["sha"]
    elif st != 404:
        return f"failed:HTTP {st} (읽기)"
    st, body = gh_req(url, data=json.dumps(payload).encode(), method="PUT")
    if st in (200, 201):
        return "updated" if "sha" in payload else "created"
    return f"failed:HTTP {st} {body[:160].decode(errors='replace')}"


def gh_put_new(path: str, content: bytes, message: str) -> str:
    if not gh_token():
        return "failed:GITHUB_TOKEN 없음"
    data = json.dumps({"message": message, "content": base64.b64encode(content).decode(), "branch": MAIN}).encode()
    st, body = gh_req(f"https://api.github.com/repos/{STATE['repo']}/contents/{urllib.parse.quote(path)}", data=data, method="PUT")
    if st in (200, 201):
        return "created"
    if st == 422 and b"sha" in body:
        return "exists"
    return f"failed:HTTP {st} {body[:160].decode(errors='replace')}"


def topics() -> list[str]:
    names = []
    try:
        txt = (gh_raw(MAIN, "topics.txt") or b"").decode("utf-8")
    except RuntimeError:
        txt = (ROOT / "topics.txt").read_text("utf-8") if (ROOT / "topics.txt").is_file() else ""
    for ln in txt.splitlines():
        ln = ln.strip()
        if ln and not ln.startswith("#") and re.fullmatch(r"[a-z0-9_-]+", ln):
            names.append(ln)
    for p in sorted(ROOT.glob("*/youtube_channel.json")):
        if p.parent.name not in names:
            names.append(p.parent.name)
    return names


def channel_of(topic: str) -> dict:
    try:
        body = gh_raw(MAIN, f"{topic}/youtube_channel.json")
        if body:
            (ROOT / topic).mkdir(exist_ok=True)
            (ROOT / topic / "youtube_channel.json").write_bytes(body)
            return json.loads(body)
    except (RuntimeError, json.JSONDecodeError):
        pass
    p = ROOT / topic / "youtube_channel.json"
    return json.loads(p.read_text("utf-8")) if p.is_file() else {}


# ─────────── 영상 목록 · 자료 점검 ───────────
def fetch_settings(topic: str, vid: str, main_paths: set[str]) -> None:
    """업로드에 쓰는 파일만 GitHub main → 이 PC 의 <주제>/source/<영상ID>/ (youtube.json 은 받지 않음)."""
    base = f"{topic}/source/{vid}/"
    dst = ROOT / topic / "source" / vid
    names = list(WANT_FILES) + [f"{vid}.txt", f"{vid}.srt"]
    names += [p[len(base):] for p in main_paths if p.startswith(base + "thumbnails/") and up.THUMB_RE.match(p.rsplit("/", 1)[-1])]
    for n in names:
        if base + n in main_paths:
            body = gh_raw(MAIN, base + n)
            if body is not None:
                (dst / n).parent.mkdir(parents=True, exist_ok=True)
                (dst / n).write_bytes(body)


def list_videos(topic: str) -> dict:
    main_paths = gh_tree(MAIN)
    upl_paths = gh_tree(UPL)
    vids = sorted({m.group(1) for p in main_paths for m in [re.match(rf"^{re.escape(topic)}/source/([^/]+)/upload\.md$", p)] if m})
    ready, done = [], []
    for vid in vids:
        base = f"{topic}/source/{vid}/"
        if base + "youtube.json" in main_paths:
            try:
                st = json.loads(gh_raw(MAIN, base + "youtube.json") or b"{}")
            except (RuntimeError, json.JSONDecodeError):
                st = {}
            done.append({"vid": vid, "url": st.get("url", ""), "publishAt": st.get("publishAt", ""), "title": st.get("title", "")})
            continue
        fetch_settings(topic, vid, main_paths)
        r = up.check_one(topic, vid)
        items = {k: list(v) for k, v in r["items"].items()}
        stale = (ROOT / topic / "source" / vid / "youtube.json").is_file()      # v1.4 기준은 main (위에서 main 에 youtube.json 없음을 확인함)
        items["올린 적 없음"] = [True, "main 에 업로드 기록 없음" + (" — 이 PC 의 옛 기록은 업로드 때 youtube_old_… 로 옮김" if stale else "")]
        vj = ROOT / topic / "source" / vid / "video.json"
        if vj.is_file():
            rec = json.loads(vj.read_text("utf-8"))
            missing = [x["name"] for x in rec["parts"] if f"{rec['dir']}/{x['name']}" not in upl_paths]
            items["영상"] = [not missing, f"{rec['size'] / 1e6:.0f}MB · 조각 {len(rec['parts'])}개" + (f" — uploads 브랜치에 없음: {', '.join(missing)}" if missing else " ✓ uploads 브랜치")]
        else:
            items["영상"] = [False, "video.json 없음 — Claude 가 tools/upload_pack.py pack 으로 올려야 함"]
        local = ROOT / topic / "out" / vid / "final_1080p.mp4"
        md = (ROOT / topic / "source" / vid / "upload.md").read_text("utf-8")
        ready.append({"vid": vid, "items": items, "ready": all(v[0] for v in items.values()), "titles": r.get("titles", []),
                      "experiments": len(experiments(md)), "downloaded": local.is_file()})
    log("LIST", topic=topic, scripts=len(vids), ready=sum(1 for v in ready if v["ready"]), waiting=len(ready), uploaded=len(done))
    return {"videos": ready, "uploaded": done}


# ─────────── 작업 (한 번에 하나) ───────────
class Job:
    def __init__(self):
        self.lock = threading.Lock()
        self.lines: list[str] = []
        self.busy = False
        self.name = ""
        self.result: dict = {}
        self.seq = 0                       # v1.2 작업 번호 — 화면이 같은 결과(채널 질문)를 두 번 띄우지 않게

    def say(self, s: str) -> None:
        for ln in str(s).splitlines():
            if not re.search(r"(refresh_token|client_secret|access_token)\s*[=:]", ln, re.I):   # 값이 섞인 줄은 버림
                self.lines.append(ln)
        del self.lines[:-800]


JOB = Job()


class _Tee(io.TextIOBase):
    def write(self, s):
        if s.strip():
            JOB.say(s.rstrip("\n"))
        sys.__stdout__.write(s)
        return len(s)


def run_job(name: str, fn, *args) -> bool:
    with JOB.lock:
        if JOB.busy:
            return False
        JOB.busy, JOB.name, JOB.result = True, name, {}
        JOB.seq += 1
        JOB.lines.clear()

    def body():
        try:
            with contextlib.redirect_stdout(_Tee()):
                JOB.result = fn(*args) or {}
        except ChannelMismatch as e:             # v1.2 멈추고 화면에서 물음
            JOB.say(f"⚠️ 키의 채널 = {e.info['key_channel']['name']} ({e.info['key_channel']['channel_id']}) · "
                    f"{e.info['topic']} 채널 기록 = {e.info['expected']['name']} ({e.info['expected']['channel_id']}) — 화면에서 올릴지 고르세요 (아직 올리지 않음)")
            JOB.result = {"ok": False, "need": "channel", **e.info}
        except SystemExit as e:
            JOB.say(f"❌ {e}")
            JOB.result = {"ok": False, "error": str(e)[:400]}
        except Exception as e:   # noqa: BLE001 — 화면에 까닭을 보여 줌
            JOB.say(f"❌ {e}")
            JOB.say(traceback.format_exc()[-800:])
            JOB.result = {"ok": False, "error": str(e)[:400]}
        finally:
            JOB.busy = False

    threading.Thread(target=body, daemon=True).start()
    return True


def channel_gate(topic: str, cid: str, title: str, allow: str = "") -> None:
    """(v1.2) 키의 채널 ID 와 <주제>/youtube_channel.json 비교 — 같으면 통과 · 다르면 allow(사용자가 확인한 ID)일 때만 통과, 아니면 ChannelMismatch."""
    want = yu.expected_channel(topic)
    if want is None:
        log("CHANNEL", status="unchecked", topic=topic, channel=title, channel_id=cid, note=f"{topic}/youtube_channel.json 없음")
        return
    if cid == want["channel_id"]:
        nm = "" if title == want.get("name") else f"이름만 다름 (기록 '{want.get('name', '')}' → 지금 '{title}') — ID 가 같아 그대로 올림"
        log("CHANNEL", status="ok", topic=topic, channel=title, channel_id=cid, note=nm or "-")
        return
    if allow and allow == cid:
        yu.ALLOW_CHANNEL.add(cid)
        log("CHANNEL", status="override", topic=topic, channel=title, channel_id=cid, expected=want.get("name", "?"),
            expected_id=want["channel_id"], note="사용자가 '이 채널에 올림'을 확인함")
        return
    LAST_KEY_CHANNEL[topic] = {"channel_id": cid, "name": title}
    log("CHANNEL", status="different", topic=topic, channel=title, channel_id=cid, expected=want.get("name", "?"), expected_id=want["channel_id"],
        note="채널 ID 가 다름 — 이름만 바꾼 채널이면 ID 는 같음 → 다른 채널(브랜드 계정)로 인증했을 수 있음 · 화면에서 물음")
    raise ChannelMismatch({"topic": topic, "key_channel": {"channel_id": cid, "name": title},
                           "expected": {"channel_id": want["channel_id"], "name": want.get("name", "")}})


def remember_channel(topic: str) -> str:
    """(v1.2) 마지막으로 '다르다'고 나온 키의 채널을 이 주제의 채널로 기록 — GitHub main <주제>/youtube_channel.json (다른 PC·Claude 도 같은 기준)."""
    kc = LAST_KEY_CHANNEL.get(topic)
    if not kc:
        raise SystemExit("[CHANNEL] ❌ 기억할 채널이 없음 — 먼저 [키 확인]")
    old = yu.expected_channel(topic) or {}
    rec = {"channel_id": kc["channel_id"], "name": kc["name"],
           "note": f"{dt.date.today()} PC 업로드 화면에서 사용자가 이 채널로 바꿈 (전: {old.get('name', '?')} {old.get('channel_id', '?')}) · "
                   f"upload_web.py {VERSION} — 키의 채널 ID 가 이것과 다르면 화면이 올릴지 물음",
           "previous": {"channel_id": old.get("channel_id", ""), "name": old.get("name", ""), "note": old.get("note", "")}}
    body = (json.dumps(rec, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    res = gh_put_update(f"{topic}/youtube_channel.json", body, f"[{topic}] 업로드 채널 기록을 {kc['name']} ({kc['channel_id']}) 로 (PC upload_web.py {VERSION})")
    if res.startswith("failed"):
        raise SystemExit(f"[CHANNEL] ❌ GitHub 기록 실패({res}) — 기억하지 못함 (공통 GITHUB_TOKEN 이 있어야 함). 이번 업로드만 하려면 '기억' 없이 [이 채널에 올림]")
    (ROOT / topic / "youtube_channel.json").write_bytes(body)
    log("CHANNEL", status="remembered", topic=topic, channel=kc["name"], channel_id=kc["channel_id"], github=res)
    return res


def ensure_auth(topic: str, allow: str = "") -> tuple[str, str]:
    """키 확인 → (채널 ID, 이름). 토큰이 없거나 만료(invalid_grant)면 브라우저 인증을 띄워 새 토큰을 <주제>/.env 에 저장하고 다시.
    v1.2: 채널이 다르면 ChannelMismatch (allow = 사용자가 확인한 채널 ID 면 통과)."""
    apply_env(topic)
    for attempt in (1, 2):
        try:
            token = yu.access_token()
            cid, title = yu.mine_channel(token)
            channel_gate(topic, cid, title, allow)
            log("AUTH", status="ok", topic=topic, channel=title)
            return cid, title
        except SystemExit as e:
            msg = str(e)
            expired = "invalid_grant" in msg or "YOUTUBE_REFRESH_TOKEN" in msg or "토큰 갱신 실패 (400)" in msg
            if attempt == 2 or not expired:
                raise
            if not (os.environ.get("YOUTUBE_CLIENT_ID") and os.environ.get("YOUTUBE_CLIENT_SECRET")):
                had = bool(os.environ.get("YOUTUBE_REFRESH_TOKEN"))
                raise SystemExit("[AUTH] ❌ " + ("토큰이 만료됐는데 " if had else "이 주제의 키가 없음 — ") +
                                 "YOUTUBE_CLIENT_ID · YOUTUBE_CLIENT_SECRET 이 없어 인증할 수 없음 → 위 키 칸에 넣고 [저장] (토큰은 [업로드]·[다시 인증] 때 저절로)")
            log("AUTH", status="expired", topic=topic, action="브라우저 인증을 띄움 — 이 주제 채널의 구글 계정으로 로그인 · 체크 칸 모두 허용")
            try:
                refresh, missing = ya.issue(os.environ["YOUTUBE_CLIENT_ID"], os.environ["YOUTUBE_CLIENT_SECRET"], say=print)
            except ya.AuthError as ae:
                raise SystemExit(f"[AUTH] ❌ {ae}") from None
            ya.save_env(topic_env_path(topic), {"YOUTUBE_CLIENT_ID": os.environ["YOUTUBE_CLIENT_ID"],
                                                "YOUTUBE_CLIENT_SECRET": os.environ["YOUTUBE_CLIENT_SECRET"], "YOUTUBE_REFRESH_TOKEN": refresh})
            os.environ["YOUTUBE_REFRESH_TOKEN"] = refresh
            log("AUTH", status="saved", file=f"{topic}/.env", missing_scopes=",".join(missing) or "-",
                note="새 토큰 저장 — OAuth 동의 화면이 '테스트'면 7일 뒤 또 만료되니 '프로덕션'으로")
    raise SystemExit("[AUTH] ❌ 인증 실패")


def publish_time(days: int, hhmm: str) -> dt.datetime:
    h, m = (int(x) for x in hhmm.split(":"))
    now = dt.datetime.now(KST)
    t = (now + dt.timedelta(days=days)).replace(hour=h, minute=m, second=0, microsecond=0)
    if t < now + dt.timedelta(minutes=15):
        raise SystemExit(f"[SCHEDULE] ❌ 공개 시각 {t:%Y-%m-%d %H:%M} 이 지금보다 15분 이상 뒤가 아님")
    return t.astimezone(dt.timezone.utc)


def get_video(topic: str, vid: str) -> Path:
    """uploads 브랜치 조각 → <주제>/out/<영상ID>/final_1080p.mp4 (이미 있고 sha256 이 같으면 그대로). 받은 뒤 sha256 확인."""
    rec = json.loads((ROOT / topic / "source" / vid / "video.json").read_text("utf-8"))
    dest = ROOT / topic / "out" / vid / "final_1080p.mp4"
    if dest.is_file() and dest.stat().st_size == rec["size"] and up.file_hashes(dest)[0] == rec["sha256"]:
        log("VIDEO", video=vid, source="이미 받음", mb=round(rec["size"] / 1e6, 1))
        return dest
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_suffix(".part")
    h = hashlib.sha256()
    with open(tmp, "wb") as f:
        for i, part in enumerate(rec["parts"], 1):
            body = gh_raw(rec["branch"], f"{rec['dir']}/{part['name']}", timeout=1800)
            if body is None:
                raise SystemExit(f"[VIDEO] ❌ 조각 없음 {rec['branch']}:{rec['dir']}/{part['name']} → Claude 에게 upload_pack.py pack 다시")
            if hashlib.sha256(body).hexdigest() != part["sha256"]:
                raise SystemExit(f"[VIDEO] ❌ 조각 {part['name']} 내용이 기록과 다름 → 다시 받기")
            f.write(body)
            h.update(body)
            log("VIDEO", video=vid, part=f"{i}/{len(rec['parts'])}", mb=round(len(body) / 1e6, 1))
    if h.hexdigest() != rec["sha256"]:
        tmp.unlink(missing_ok=True)
        raise SystemExit("[VIDEO] ❌ 이어 붙인 영상의 sha256 이 기록과 다름 → 다시 받기")
    tmp.replace(dest)
    log("VIDEO", video=vid, source=f"GitHub {rec['branch']} 브랜치", mb=round(rec["size"] / 1e6, 1), sha256=rec["sha256"][:12])
    return dest


def experiments(md: str) -> list[dict]:
    """(v1.2) 업로드 시트 '## 1-1. 실험안 …' 표 → [{name, title, thumb}] — 스튜디오 '테스트 및 비교'용 (API 로 올리지 않음)."""
    m = re.search(r"^##\s*1-1\.[^\n]*\n(.*?)(?=^##\s|\Z)", md, re.M | re.S)
    if not m:
        return []
    out = []
    for row in re.finditer(r"^\|\s*([^|]*실험[^|]*?)\s*\|\s*([^|]+?)\s*\|[^\n]*?thumbnail_(\d)", m.group(1), re.M):
        out.append({"name": row.group(1).strip(), "title": row.group(2).strip(), "thumb": int(row.group(3))})
    return out


def srt_cues(p: Path, n: int = 6) -> dict:
    """(v1.2) SRT 앞 n 개 + 개수 + 끝 시각."""
    if not p.is_file():
        return {"count": 0, "first": [], "end": ""}
    blocks = [b for b in re.split(r"\r?\n\r?\n", p.read_text("utf-8-sig").strip()) if b.strip()]
    first, end = [], ""
    for b in blocks:
        ln = b.strip().splitlines()
        if len(ln) >= 3 and "-->" in ln[1]:
            end = ln[1].split("-->")[1].strip()
            if len(first) < n:
                first.append({"t": ln[1].split("-->")[0].strip()[:8], "text": " ".join(ln[2:])})
    return {"count": len(blocks), "first": first, "end": end[:8]}


def cell(md: str, name: str, default: str = "-") -> str:
    """(v1.2) 업로드 설정 표 '| <name> | <값> |' 의 값 칸 전체 (굵게 ** 와 괄호 설명 빼고) — 미리보기용."""
    m = re.search(rf"^\|\s*{re.escape(name)}\s*\|\s*([^|\n]+?)\s*\|", md, re.M)
    if not m:
        return default
    v = re.sub(r"\*\*", "", m.group(1)).strip()
    return re.sub(r"\s*\([^)]*\)\s*$", "", v).strip() or default


def media_url(topic: str, vid: str, what: str) -> str:
    return f"/media/{topic}/{vid}/{what}?k={STATE['token']}"


def preview(topic: str, vid: str) -> dict:
    """(v1.2) 올라갈 그대로 — 이 PC 에 받아 둔 시트·자막·썸네일·영상(GitHub 에서 [새로 고침] 때 받은 것)으로."""
    src = ROOT / topic / "source" / vid
    if not (src / "upload.md").is_file():
        raise SystemExit(f"[PREVIEW] ❌ {vid}: 업로드 시트가 이 PC 에 없음 → [새로 고침]")
    md = (src / "upload.md").read_text("utf-8")
    meta = yu.read_sheet(topic, vid)
    chap_err = ""
    try:
        desc, chapters = yu.recompute_chapters(topic, vid, meta["description"], meta["chapter_spec"])
    except SystemExit as e:
        desc, chapters, chap_err = meta["description"], [], str(e)[:200]
    problems = yu.validate(dict(meta, description=desc)) + ([chap_err] if chap_err else [])
    main_n = yu.paired_thumbnail(topic, vid)
    exps = experiments(md)
    names = sorted(p.name for p in (src / "thumbnails").glob("thumbnail_*") if up.THUMB_RE.match(p.name)) if (src / "thumbnails").is_dir() else []
    thumbs = []
    for nm in names:
        k = int(re.search(r"thumbnail_(\d)", nm).group(1))
        ex = next((e for e in exps if e["thumb"] == k), None)
        thumbs.append({"n": k, "name": nm, "url": media_url(topic, vid, f"thumb/{nm}"), "main": k == main_n,
                       "role": "본안 — API 로 올림" if k == main_n else ("실험안 — 스튜디오 '테스트 및 비교'" + (f" · 짝 제목: {ex['title']}" if ex else ""))})
    rec = json.loads((src / "video.json").read_text("utf-8")) if (src / "video.json").is_file() else {}
    local = ROOT / topic / "out" / vid / "final_1080p.mp4"
    have = bool(rec) and local.is_file() and local.stat().st_size == rec.get("size")
    want = yu.expected_channel(topic) or {}
    pinned = (yu._section_code(md, "고정 댓글") or "").strip()
    out = {"vid": vid, "title": meta["title"], "title_chars": len(meta["title"]), "description": desc, "chapters": chapters or [],
           "tags": meta["tags"], "tags_chars": yu.tags_length(meta["tags"]), "problems": problems,
           "thumbs": thumbs, "experiments": exps, "channel": want,
           "settings": {"공개": "비공개로 올린 뒤 예약 공개",
                        "카테고리": f"교육 (categoryId {yu.CATEGORY_EDUCATION} — 도구가 늘 이 값)" + ("" if cell(md, "카테고리") in ("교육", "-") else f" · 시트: {cell(md, '카테고리')}"),
                        "시청자층": "아동용 아님 (도구가 늘 이 값)" + ("" if cell(md, "시청자층") in ("아동용 아님", "-") else f" · 시트: {cell(md, '시청자층')}"),
                        "기본 언어": meta["default_language"],
                        "변경되거나 합성된 콘텐츠": "예" if meta["synthetic"] else "아니요",
                        "자막 올리기": ("예 — " + ("한국어 + 언어별" if meta["caption_mode"] == "all" else "한국어")) if meta["captions"] else "아니요",
                        "언어별 제목·설명": ", ".join(meta["localizations"]) or "없음"},
           "srt": srt_cues(src / f"{vid}.srt"), "pinned": pinned,
           "video": {"have": have, "url": media_url(topic, vid, "video") if have else "", "mb": round(rec.get("size", 0) / 1e6),
                     "parts": len(rec.get("parts", [])), "note": "" if rec else "video.json 없음"}}
    log("PREVIEW", topic=topic, video=vid, title_chars=out["title_chars"], chapters=len(out["chapters"]), tags=len(out["tags"]),
        thumbs=len(thumbs), main_thumb=f"thumbnail_{main_n}", video_local=have, problems=len(problems))
    return out


def do_test(topic: str, vid: str) -> dict:
    cid, ch = ensure_auth(topic)
    lst = list_videos(topic)
    v = next((x for x in lst["videos"] if x["vid"] == vid), None)
    if not v:
        raise SystemExit(f"[TEST] ❌ {vid}: 올릴 목록에 없음 (이미 올렸거나 upload.md 없음)")
    bad = [f"{k}: {note}" for k, (ok, note) in v["items"].items() if not ok]
    for k, (ok, note) in v["items"].items():
        log("TEST", item=k.replace(" ", "_"), ok=ok, note=str(note).replace(" ", "_")[:100])
    log("TEST", video=vid, channel=ch, result="통과 — [업로드]를 눌러도 됨" if not bad else f"부족 {len(bad)}개")
    return {"ok": not bad, "problems": bad, "channel": ch}


def do_upload(topic: str, vid: str, days: int, hhmm: str, allow: str = "", remember: bool = False) -> dict:
    t0 = time.time()
    when = publish_time(days, hhmm)
    log("START", tool=f"upload_web.py {VERSION}", topic=topic, video=vid, publish_kst=when.astimezone(KST).strftime("%Y-%m-%d_%H:%M"),
        allow_channel=allow or "-", remember=remember)
    cid, ch = ensure_auth(topic, allow)
    if remember and allow and cid == allow:
        remember_channel(topic)
    lst = list_videos(topic)
    v = next((x for x in lst["videos"] if x["vid"] == vid), None)
    if not v:
        raise SystemExit(f"[UPLOAD] ❌ {vid}: 올릴 목록에 없음 (이미 올렸거나 upload.md 없음)")
    bad = [f"{k}: {note}" for k, (ok, note) in v["items"].items() if not ok]
    if bad:
        raise SystemExit("[UPLOAD] ❌ 자료가 덜 됨 — " + " · ".join(bad))
    title = yu.read_sheet(topic, vid)["title"]
    log("TITLE", video=vid, title=title[:60].replace(" ", "_"), thumbnail=f"thumbnail_{yu.paired_thumbnail(topic, vid)}", note="업로드 시트 1번 본안 (실험안은 스튜디오)")
    path = get_video(topic, vid)
    stale = ROOT / topic / "source" / vid / "youtube.json"
    if stale.is_file():                                   # v1.3 main 에는 없음(목록에 있으니) = 이 PC 에만 남은 옛 기록 → 옮기고 새로 올림
        old_rec = json.loads(stale.read_text("utf-8") or "{}")
        moved = stale.with_name(f"youtube_old_{dt.datetime.now(dt.timezone.utc):%Y%m%d%H%M%S}.json")
        stale.rename(moved)
        log("REUPLOAD", video=vid, old_video_id=old_rec.get("videoId", "-"), moved_to=moved.name,
            note="main 에 youtube.json 이 없어 새로 올림 — 옛 영상은 스튜디오에서 지우지 않으면 그대로 남음 (예약 공개면 그 시각에 공개됨)")
    res = yu.run(topic, vid, video=str(path), publish_at=when.strftime("%Y-%m-%dT%H:%M:%SZ"))
    state = ROOT / topic / "source" / vid / "youtube.json"
    pushed = gh_put_new(f"{topic}/source/{vid}/youtube.json", state.read_bytes(),
                        f"유튜브 예약 업로드: {vid} (공개 {when.astimezone(KST):%Y-%m-%d %H:%M} KST, PC upload_web.py {VERSION})") if state.is_file() else "failed:youtube.json 없음"
    log("PUSH", video=vid, result=pushed.replace(" ", "_")[:120], note="youtube.json 이 GitHub 에 있어야 다른 PC·Claude 가 올린 줄 앎" if pushed.startswith("failed") else "-")
    url = (res or {}).get("url", "")
    log("DONE", video=vid, url=url or "-", channel=ch, title=title[:50].replace(" ", "_"), sec=round(time.time() - t0),
        next="공개 전에 스튜디오에서 영상·자막·썸네일 확인 · 실험안 썸네일은 공개 뒤 스튜디오 '테스트 및 비교'")
    return {"ok": True, "url": url, "publishAt": when.isoformat(), "pushed": pushed}


# ─────────── 웹 ───────────
PAGE = r"""<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>유튜브 업로드</title><style>
:root{--bg:#F5F6F8;--card:#fff;--ink:#1B2130;--sub:#5B6475;--line:#E2E5EB;--ok:#16946B;--bad:#D23B2E;--acc:#2F6BFF;--warn:#B26A00}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 system-ui,-apple-system,"Malgun Gothic","Apple SD Gothic Neo",sans-serif}
header{padding:18px 24px;background:#151A26;color:#fff}header h1{margin:0;font-size:20px}header p{margin:4px 0 0;color:#B8C0D0;font-size:13px}
.tabs{display:flex;gap:6px;padding:12px 24px;flex-wrap:wrap;background:#fff;border-bottom:1px solid var(--line)}
.tabs button{border:1px solid var(--line);background:#fff;border-radius:999px;padding:6px 14px;cursor:pointer;font-size:14px}
.tabs button.on{background:var(--ink);color:#fff;border-color:var(--ink)}
main{max-width:1100px;margin:0 auto;padding:18px 16px 40px;display:grid;gap:16px}main>*{min-width:0}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px 18px}.card h2{margin:0 0 10px;font-size:16px}
.row{display:grid;grid-template-columns:220px 1fr auto;gap:8px;align-items:center;margin:6px 0}
input{width:100%;padding:8px 10px;border:1px solid var(--line);border-radius:8px;font:inherit}
.btn{border:0;border-radius:9px;padding:8px 14px;background:var(--ink);color:#fff;cursor:pointer;font:inherit;white-space:nowrap}
.btn.sec{background:#fff;color:var(--ink);border:1px solid var(--line)}.btn.go{background:var(--acc)}.btn:disabled{opacity:.4;cursor:default}
.muted{color:var(--sub);font-size:13px}.ok{color:var(--ok)}.bad{color:var(--bad)}
table{width:100%;border-collapse:collapse}td,th{border-top:1px solid var(--line);padding:8px 6px;vertical-align:top;text-align:left;font-size:14px}
.chips{display:flex;flex-wrap:wrap;gap:4px}.chip{font-size:12px;border-radius:999px;padding:2px 8px;background:#EEF7F2;color:var(--ok)}.chip.x{background:#FDEEEC;color:var(--bad)}.chip.n{background:#EEF1F6;color:var(--sub)}
pre{background:#10141D;color:#D9E1F2;border-radius:10px;padding:12px;max-height:360px;overflow:auto;font-size:12px;white-space:pre-wrap;overflow-wrap:anywhere;word-break:break-all;margin:0}
.sched{display:flex;gap:10px;align-items:center;flex-wrap:wrap}.sched input{width:90px}.sched input[type=time]{width:150px}
.ov{position:fixed;inset:0;background:rgba(10,14,22,.62);display:none;align-items:flex-start;justify-content:center;overflow:auto;z-index:10;padding:24px 12px}.ov.on{display:flex}
.dlg{background:#fff;border-radius:16px;max-width:1080px;width:100%;padding:18px 20px;position:relative}.dlg.sm{max-width:620px}
.dlg h2{margin:0 0 8px;font-size:18px}.cls{position:absolute;right:14px;top:10px;background:none;border:0;font-size:24px;cursor:pointer;color:var(--sub)}
.pv{display:grid;grid-template-columns:minmax(0,1.45fr) minmax(0,1fr);gap:18px}@media(max-width:860px){.pv{grid-template-columns:1fr}.row{grid-template-columns:1fr}}
.player{width:100%;aspect-ratio:16/9;background:#000;border-radius:12px;overflow:hidden;display:flex;align-items:center;justify-content:center;position:relative}
.player video,.player img{width:100%;height:100%;object-fit:contain;display:block}
.player .over{position:absolute;inset:auto 0 0 0;padding:10px;background:linear-gradient(transparent,rgba(0,0,0,.75));color:#fff;font-size:13px;display:flex;gap:8px;align-items:center;flex-wrap:wrap}
.wtitle{font-size:19px;font-weight:700;margin:12px 0 4px;line-height:1.35}
.desc{background:#F2F3F5;border-radius:12px;padding:12px 14px;white-space:pre-wrap;overflow-wrap:anywhere;font-size:14px;margin-top:8px}
.desc a{color:#065FD4;text-decoration:none;cursor:pointer}
.phone{width:100%;max-width:380px;background:#0F0F0F;color:#F1F1F1;border-radius:16px;padding:10px 10px 14px}
.phone .th{position:relative}.phone .th img{width:100%;aspect-ratio:16/9;object-fit:cover;border-radius:10px;display:block}
.phone .dur{position:absolute;right:6px;bottom:6px;background:rgba(0,0,0,.8);color:#fff;font-size:12px;border-radius:4px;padding:1px 4px}
.phone .meta{display:flex;gap:10px;margin-top:10px}.phone .av{width:36px;height:36px;border-radius:50%;background:#3A3F4B;flex:none}
.phone .t2{font-size:15px;line-height:1.38;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;font-family:Roboto,"Malgun Gothic","Apple SD Gothic Neo",sans-serif}
.phone .s{color:#AAAAAA;font-size:12px;margin-top:3px}
.thumbs{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px}.thumbs figure{margin:0}.thumbs img{width:100%;border-radius:8px;display:block;border:3px solid transparent}
.thumbs figure.main img{border-color:var(--acc)}.thumbs figcaption{font-size:12px;color:var(--sub);margin-top:3px}
.kv td{font-size:13px;padding:5px 6px}.kv td:first-child{color:var(--sub);width:42%}
.probs{background:#FDEEEC;color:var(--bad);border-radius:10px;padding:10px 12px;font-size:14px;margin:8px 0}
h4{margin:14px 0 6px;font-size:14px}.cue{font-size:13px;margin:2px 0}.cue b{color:var(--sub);font-weight:500;margin-right:6px}
.foot{display:flex;gap:8px;justify-content:flex-end;flex-wrap:wrap;margin-top:16px;border-top:1px solid var(--line);padding-top:12px}
.chbox{display:grid;grid-template-columns:auto 1fr;gap:4px 12px;background:#F7F8FA;border-radius:10px;padding:10px 12px;margin:10px 0;font-size:14px}
label.ck{display:flex;gap:8px;align-items:flex-start;font-size:14px;margin:8px 0}label.ck input{width:auto;margin-top:4px}
</style></head><body>
<header><h1>유튜브 업로드 (이 PC 에서만 열림)</h1><p>자료가 다 된 대본만 [미리보기] → [업로드] — 비공개로 올리고 정한 날 자동 공개 · 키는 이 PC 의 .env 에만 저장 · 연구·교육용 영상 (투자 권유 아님)</p></header>
<nav class="tabs" id="tabs"></nav>
<main>
<section class="card"><h2>키 설정 — <span id="tname"></span> <span class="muted" id="chan"></span></h2>
<div id="keys"></div>
<div class="row"><span>GITHUB_TOKEN <span class="muted">(모든 주제 공통 · youtube.json 기록)</span></span><input id="k_GITHUB_TOKEN" type="password" placeholder="" autocomplete="off"><span class="muted" id="s_GITHUB_TOKEN"></span></div>
<p style="display:flex;gap:8px;flex-wrap:wrap"><button class="btn" onclick="saveKeys()">저장</button><button class="btn sec" onclick="checkAuth()">키 확인</button><button class="btn sec" onclick="reauth()">다시 인증 (계정·채널 다시 고르기)</button></p>
<p class="muted">토큰이 만료되면 [업로드]·[키 확인] 때 브라우저 인증 창이 저절로 열립니다 — 이 주제 채널의 구글 계정(채널)을 고르고 체크 칸을 모두 허용하면 새 토큰이 이 주제 .env 에 저장되고 그대로 이어 갑니다. 키의 채널이 기록과 다르면 올리기 전에 물어봅니다. 7일마다 만료되면 Google Cloud 콘솔 → OAuth 동의 화면 → 게시 상태를 '프로덕션'으로.</p>
</section>
<section class="card"><h2>예약</h2><div class="sched">오늘부터 <input id="days" type="number" min="1" max="60" value="7"> 일 뒤 <input id="hhmm" type="time" value="17:00"> (한국 시간) 공개 → <b id="when"></b></div>
<p class="muted">유튜브 할당량: 영상 하나 약 2,050단위 · 하루 10,000 (하루에 4편까지) · 하루는 한국 오후 4~5시에 바뀜</p></section>
<section class="card"><h2>올릴 대본 <button class="btn sec" style="float:right" onclick="loadVideos()">새로 고침</button></h2><div id="videos" class="muted">불러오는 중…</div></section>
<section class="card"><h2>로그 <span class="muted" id="jobname"></span></h2><pre id="log"></pre></section>
</main>
<div class="ov" id="pvov" onclick="if(event.target===this)closePv()"><div class="dlg" id="pv"></div></div>
<div class="ov" id="chov"><div class="dlg sm" id="ch"></div></div>
<script>
const TOKEN="__TOKEN__";let TOPIC="",PENDING=null,HANDLED=0,PVVID="",VIDS={};const KEYS=["YOUTUBE_CLIENT_ID","YOUTUBE_CLIENT_SECRET","YOUTUBE_REFRESH_TOKEN"];
const esc=s=>String(s==null?"":s).replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
async function api(p,body){const r=await fetch(p,body?{method:"POST",headers:{"Content-Type":"application/json","X-Upload-Token":TOKEN},body:JSON.stringify(body)}:{headers:{"X-Upload-Token":TOKEN}});return r.json()}
async function boot(){const s=await api("/api/topics");const t=document.getElementById("tabs");t.innerHTML="";s.topics.forEach(n=>{const b=document.createElement("button");b.textContent=n;b.onclick=()=>pick(n);b.id="tab_"+n;t.appendChild(b)});pick(s.topics.includes("stock")?"stock":s.topics[0]);setInterval(pollJob,1500);upd()}
async function pick(n){TOPIC=n;document.querySelectorAll(".tabs button").forEach(b=>b.classList.toggle("on",b.id==="tab_"+n));document.getElementById("tname").textContent=n;await loadKeys();loadVideos()}
async function loadKeys(){const s=await api("/api/env?topic="+encodeURIComponent(TOPIC));document.getElementById("chan").textContent=s.channel&&s.channel.channel_id?`(채널 기록 ID: ${s.channel.channel_id})`:"(youtube_channel.json 없음 — 채널 확인 안 함)";
 document.getElementById("keys").innerHTML=KEYS.map(k=>`<div class="row"><span>${k}</span><input id="k_${k}" type="password" autocomplete="off" placeholder="${k==="YOUTUBE_REFRESH_TOKEN"?"비워 두면 [다시 인증]으로 저절로":""}"><span class="muted">${esc(s.status[k]||"없음")}</span></div>`).join("");
 document.getElementById("s_GITHUB_TOKEN").textContent=s.status.GITHUB_TOKEN||"없음"}
async function saveKeys(){const v={};KEYS.concat(["GITHUB_TOKEN"]).forEach(k=>{const x=document.getElementById("k_"+k).value.trim();if(x)v[k]=x});const r=await api("/api/env",{topic:TOPIC,values:v});alert(r.ok?"저장했습니다 ("+r.saved.join(", ")+")":"실패: "+r.error);loadKeys()}
async function checkAuth(){PENDING=null;const r=await api("/api/auth",{topic:TOPIC,mode:"check"});if(!r.ok)alert(r.error)}
async function reauth(){const r=await api("/api/auth",{topic:TOPIC,mode:"new"});if(!r.ok)alert(r.error)}
function sched(){const d=+document.getElementById("days").value||7,h=document.getElementById("hhmm").value||"17:00";const t=new Date(Date.now()+d*864e5);const p=n=>String(n).padStart(2,"0");
 const k=new Date(t.getTime()+(t.getTimezoneOffset()+540)*6e4);return{d,h,label:`${k.getFullYear()}-${p(k.getMonth()+1)}-${p(k.getDate())} ${h}`}}
function upd(){document.getElementById("when").textContent=sched().label}
document.addEventListener("input",e=>{if(e.target.id==="days"||e.target.id==="hhmm")upd()});
async function loadVideos(){const box=document.getElementById("videos");box.innerHTML="GitHub 에서 자료를 받는 중…";const s=await api("/api/videos?topic="+encodeURIComponent(TOPIC));
 if(s.error){box.innerHTML=`<span class="bad">${esc(s.error)}</span>`;return}
 VIDS={};let h=`<table><tr><th>대본</th><th>올라갈 제목 (본안)</th><th>자료</th><th></th></tr>`;
 if(!s.videos.length)h+=`<tr><td colspan="4" class="muted">올릴 대본이 없습니다 (upload.md 가 있고 youtube.json 이 없는 대본)</td></tr>`;
 s.videos.forEach(v=>{VIDS[v.vid]=v;const t=v.titles[0]?esc(v.titles[0].title):'<span class="bad">(제목 없음)</span>';
  const ex=v.experiments?`<br><span class="muted">실험안 ${v.experiments}개 — 공개 뒤 스튜디오 '테스트 및 비교'</span>`:"";
  const c=Object.entries(v.items).map(([k,[ok,n]])=>`<span class="chip ${ok?"":"x"}" title="${esc(n)}">${ok?"✓":"✗"} ${esc(k)}</span>`).join("");
  h+=`<tr><td><b>${esc(v.vid)}</b><br><span class="${v.ready?"ok":"bad"}">${v.ready?"준비됨":"부족"}</span>${v.downloaded?'<br><span class="muted">영상 받아 둠</span>':""}</td><td>${t}${ex}</td><td><div class="chips">${c}</div></td>
  <td style="white-space:nowrap"><button class="btn sec" onclick="openPv('${esc(v.vid)}')">미리보기</button> <button class="btn sec" onclick="test('${esc(v.vid)}')">시험</button> <button class="btn go" ${v.ready?"":"disabled"} onclick="upload('${esc(v.vid)}')">업로드</button></td></tr>`});
 h+=`</table>`;const kst=iso=>{if(!iso)return"";const d=new Date(iso);if(isNaN(d))return iso;const k=new Date(d.getTime()+(d.getTimezoneOffset()+540)*6e4),p=n=>String(n).padStart(2,"0");return `${k.getFullYear()}-${p(k.getMonth()+1)}-${p(k.getDate())} ${p(k.getHours())}:${p(k.getMinutes())} 공개`};
 if(s.uploaded.length)h+=`<p class="muted">올린 영상: `+s.uploaded.map(u=>`${esc(u.vid)} ${u.url?`<a href="${esc(u.url)}" target="_blank">열기</a>`:""} ${esc(kst(u.publishAt))}`).join(" · ")+`</p>`;box.innerHTML=h}
async function test(vid){PENDING=null;const r=await api("/api/test",{topic:TOPIC,vid});if(!r.ok)alert(r.error)}
async function upload(vid,allow,remember){const s=sched();const v=VIDS[vid]||{};const title=v.titles&&v.titles[0]?v.titles[0].title:"";
 if(!allow&&!confirm(`${vid}\n제목: ${title}\n썸네일: 본안(thumbnail_1 — 시트의 짝)\n${s.label} (한국 시간) 공개로 예약 업로드할까요?\n그때까지는 비공개입니다.`))return;
 PENDING={vid,d:s.d,h:s.h};const r=await api("/api/upload",{topic:TOPIC,vid,days:s.d,hhmm:s.h,allow_channel:allow||"",remember:!!remember});if(!r.ok)alert(r.error)}
function closePv(){document.getElementById("pvov").classList.remove("on");const v=document.querySelector("#pv video");if(v)v.pause();PVVID=""}
function tsLinks(t){return esc(t).split("\n").map(l=>{const m=l.match(/^(\d+:)?\d+:\d\d/);if(!m)return l;const p=m[0].split(":").map(Number);const sec=p.length===3?p[0]*3600+p[1]*60+p[2]:p[0]*60+p[1];return `<a onclick="seek(${sec})">${m[0]}</a>`+l.slice(m[0].length)}).join("\n")}
function seek(s){const v=document.querySelector("#pv video");if(v){v.currentTime=s;v.play()}}
async function openPv(vid){PVVID=vid;const ov=document.getElementById("pvov"),box=document.getElementById("pv");box.innerHTML='<button class="cls" onclick="closePv()" title="닫기">×</button><p class="muted">미리보기를 만드는 중…</p>';ov.classList.add("on");
 const r=await api("/api/preview?topic="+encodeURIComponent(TOPIC)+"&vid="+encodeURIComponent(vid));if(r.ok===false||r.error){box.innerHTML=`<button class="cls" onclick="closePv()" title="닫기">×</button><p class="bad">${esc(r.error)}</p>`;return}
 const s=sched(),main=r.thumbs.find(t=>t.main)||r.thumbs[0]||{},ready=(VIDS[vid]||{}).ready;const dur=r.srt.end?r.srt.end.replace(/^00:/,"").replace(/^0/,""):"";
 const player=r.video.have?`<video controls preload="metadata" poster="${esc(main.url||"")}" src="${esc(r.video.url)}"></video>`:`<img src="${esc(main.url||"")}" alt=""><div class="over">영상은 아직 이 PC 에 없음 (${r.video.mb}MB · 조각 ${r.video.parts}) <button class="btn sec" onclick="fetchVideo('${esc(vid)}')">영상 받기 (미리보기용)</button></div>`;
 const probs=r.problems.length?`<div class="probs"><b>올리기 전에 고칠 것</b><br>${r.problems.map(esc).join("<br>")}</div>`:"";
 const exps=r.experiments.length?`<h4>실험안 (API 로 올리지 않음 — 공개 뒤 스튜디오 '테스트 및 비교')</h4>`+r.experiments.map(e=>`<div class="cue"><b>${esc(e.name)}</b>${esc(e.title)} <span class="muted">· thumbnail_${e.thumb}</span></div>`).join(""):"";
 box.innerHTML=`<button class="cls" onclick="closePv()" title="닫기">×</button><h2>미리보기 — ${esc(vid)}</h2><p class="muted" style="margin:0 0 10px">이 PC 에 받아 둔 업로드 시트·자막·썸네일 그대로 · 공개 <b>${esc(s.label)}</b> (한국 시간) · 그때까지 비공개</p>${probs}
 <div class="pv"><div><div class="player">${player}</div>
  <div class="wtitle">${esc(r.title)}</div><div class="muted">제목 ${r.title_chars}자</div>
  <div class="desc">${tsLinks(r.description)}</div>
  <h4>태그 ${r.tags.length}개 · ${r.tags_chars}자 / 500</h4><div class="chips">${r.tags.map(t=>`<span class="chip n">${esc(t)}</span>`).join("")}</div>
  ${r.pinned?`<h4>고정 댓글 (스튜디오에서 직접 — API 로 안 올림)</h4><div class="desc">${esc(r.pinned)}</div>`:""}</div>
 <div><h4 style="margin-top:0">휴대전화 홈 화면 (대략 — 줄 바꿈은 기기마다 조금 다름)</h4><div class="phone"><div class="th"><img src="${esc(main.url||"")}" alt="">${dur?`<span class="dur" id="pvdur">≈${esc(dur)}</span>`:""}</div>
  <div class="meta"><div class="av"></div><div><div class="t2">${esc(r.title)}</div><div class="s">${esc(r.channel.name||"")} · 조회수 0회 · 예약 ${esc(s.label)}</div></div></div></div>
  <h4>썸네일</h4><div class="thumbs">${r.thumbs.map(t=>`<figure class="${t.main?"main":""}"><img src="${esc(t.url)}" alt=""><figcaption>${esc(t.name)} · ${esc(t.role)}</figcaption></figure>`).join("")}</div>${exps}
  <h4>설정</h4><table class="kv">${Object.entries(r.settings).map(([k,v])=>`<tr><td>${esc(k)}</td><td>${esc(v)}</td></tr>`).join("")}<tr><td>챕터</td><td>${r.chapters.length}개 (시각은 자막에서 다시 계산)</td></tr></table>
  <h4>자막 — 처음 ${r.srt.first.length}개 / 모두 ${r.srt.count}개 · 끝 ${esc(r.srt.end)}</h4>${r.srt.first.map(c=>`<div class="cue"><b>${esc(c.t)}</b>${esc(c.text)}</div>`).join("")}</div></div>
 <div class="foot"><button class="btn sec" onclick="closePv()">닫기</button><button class="btn go" ${ready&&!r.problems.length?"":"disabled"} onclick="closePv();upload('${esc(vid)}')">이대로 업로드 (${esc(s.label)} 공개)</button></div>`
 const vv=document.querySelector('#pv video');if(vv)vv.addEventListener('loadedmetadata',()=>{const d=document.getElementById('pvdur');if(d)d.textContent=fmtDur(vv.duration)})}
function fmtDur(t){t=Math.round(t);const h=Math.floor(t/3600),m=Math.floor(t%3600/60),x=t%60,p=n=>String(n).padStart(2,'0');return h?`${h}:${p(m)}:${p(x)}`:`${m}:${p(x)}`}
async function fetchVideo(vid){const r=await api("/api/fetch_video",{topic:TOPIC,vid});if(!r.ok)alert(r.error)}
function showChannel(res){const o=document.getElementById("chov"),b=document.getElementById("ch"),up=!!PENDING;
 b.innerHTML=`<h2>키의 채널이 ${esc(res.topic)} 채널 기록과 다릅니다</h2>
 <div class="chbox"><span class="muted">지금 키의 채널</span><b>${esc(res.key_channel.name)} <span class="muted">${esc(res.key_channel.channel_id)}</span></b>
 <span class="muted">${esc(res.topic)} 채널 기록</span><b>${esc(res.expected.name)} <span class="muted">${esc(res.expected.channel_id)}</span></b></div>
 <p style="font-size:14px">채널 <b>이름만</b> 바꾼 경우에는 채널 ID 가 그대로라 이 창이 뜨지 않습니다. <b>ID 가 다르면 다른 채널</b>로 인증했을 수 있어요 (같은 구글 계정 안의 다른 채널·브랜드 계정 포함). 유튜브 스튜디오 → 설정 → 채널 → 고급 설정에서 채널 ID 를 확인하세요.</p>
 <label class="ck"><input type="checkbox" id="chrem"> 다음부터 이 채널을 ${esc(res.topic)} 채널로 기억 (GitHub 의 ${esc(res.topic)}/youtube_channel.json 을 바꿈 — 다른 PC·Claude 도 이 채널 기준)</label>
 <div class="foot"><button class="btn sec" onclick="closeCh()">취소</button><button class="btn sec" onclick="closeCh();reauth()">다른 채널로 다시 인증</button>
 ${up?`<button class="btn go" onclick="chGo('${esc(res.key_channel.channel_id)}')">이 채널에 올림</button>`:`<button class="btn go" onclick="chRemember()">이 채널로 기억</button>`}</div>`;o.classList.add("on")}
function closeCh(){document.getElementById("chov").classList.remove("on")}
async function chGo(cid){const rem=document.getElementById("chrem").checked;closeCh();const p=PENDING;if(!p)return;document.getElementById("days").value=p.d;document.getElementById("hhmm").value=p.h;upd();await upload(p.vid,cid,rem)}
async function chRemember(){const r=await api("/api/channel",{topic:TOPIC,mode:"remember"});closeCh();alert(r.ok?"기억했습니다 — "+r.result:"실패: "+r.error);loadKeys()}
let wasBusy=false;async function pollJob(){const s=await api("/api/job");const l=document.getElementById("log");const atEnd=l.scrollTop+l.clientHeight>=l.scrollHeight-20;l.textContent=s.lines.join("\n");if(atEnd)l.scrollTop=l.scrollHeight;
 const need=s.result&&s.result.need==="channel";
 document.getElementById("jobname").textContent=s.busy?`— ${s.name} 진행 중…`:(s.name?`— ${s.name} ${need?"멈춤 (채널 확인)":(s.result&&s.result.ok===false?"실패":"끝")}`:"");
 if(!s.busy&&need&&s.seq!==HANDLED){HANDLED=s.seq;showChannel(s.result)}
 if(wasBusy&&!s.busy){loadKeys();if(s.name.startsWith("업로드")&&!need){PENDING=null;loadVideos()}if(s.name.startsWith("영상 받기")&&PVVID)openPv(PVVID)}wasBusy=s.busy}
boot();
</script></body></html>"""


VID_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,80}")
TOPIC_RE = re.compile(r"[a-z0-9_-]+")
CID_RE = re.compile(r"UC[A-Za-z0-9_-]{22}")


class Handler(http.server.BaseHTTPRequestHandler):
    def log_message(self, *_):
        pass

    def _json(self, obj, code=200):
        b = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(b)

    def _guard(self) -> bool:
        host = (self.headers.get("Host") or "").split(":")[0]
        if host not in ("127.0.0.1", "localhost"):
            self._json({"ok": False, "error": "이 PC 에서만 열 수 있음"}, 403)
            return False
        if self.path.startswith("/api/") and self.headers.get("X-Upload-Token") != STATE["token"]:
            self._json({"ok": False, "error": "화면을 새로 고침하세요 (토큰 다름)"}, 403)
            return False
        if self.path.startswith("/media/"):
            q = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            if q.get("k", [""])[0] != STATE["token"]:
                self._json({"ok": False, "error": "화면을 새로 고침하세요 (토큰 다름)"}, 403)
                return False
        return True

    def _send_file(self, path: Path, ctype: str) -> None:
        """(v1.2) 이 PC 의 파일 — 영상은 Range(이어 보기·건너뛰기)."""
        size = path.stat().st_size
        start, end, code = 0, size - 1, 200
        m = re.match(r"bytes=(\d*)-(\d*)$", (self.headers.get("Range") or "").strip())
        if m and (m.group(1) or m.group(2)):
            if m.group(1):
                start, end = int(m.group(1)), (int(m.group(2)) if m.group(2) else size - 1)
            else:
                start = max(0, size - int(m.group(2)))
            end = min(end, size - 1)
            if start > end:
                self.send_response(416)
                self.send_header("Content-Range", f"bytes */{size}")
                self.end_headers()
                return
            code = 206
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Accept-Ranges", "bytes")
        self.send_header("Content-Length", str(end - start + 1))
        self.send_header("Cache-Control", "no-store")
        if code == 206:
            self.send_header("Content-Range", f"bytes {start}-{end}/{size}")
        self.end_headers()
        try:
            with open(path, "rb") as f:
                f.seek(start)
                left = end - start + 1
                while left > 0:
                    chunk = f.read(min(1 << 20, left))
                    if not chunk:
                        break
                    self.wfile.write(chunk)
                    left -= len(chunk)
        except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError):
            pass

    def _media(self, parts: list[str]) -> None:
        """/media/<주제>/<영상ID>/thumb/<thumbnail_N.jpg> · /media/<주제>/<영상ID>/video — 정해진 자리의 파일만."""
        if len(parts) < 3 or not TOPIC_RE.fullmatch(parts[0]) or not VID_RE.fullmatch(parts[1]) or ".." in parts[1]:
            return self._json({"error": "없음"}, 404)
        topic, vid, what = parts[0], parts[1], parts[2]
        if what == "thumb" and len(parts) == 4 and up.THUMB_RE.match(parts[3]) and "/" not in parts[3]:
            p = ROOT / topic / "source" / vid / "thumbnails" / parts[3]
            ctype = {"jpg": "image/jpeg", "jpeg": "image/jpeg", "png": "image/png", "webp": "image/webp"}.get(p.suffix.lower().lstrip("."), "application/octet-stream")
        elif what == "video" and len(parts) == 3:
            p, ctype = ROOT / topic / "out" / vid / "final_1080p.mp4", "video/mp4"
        else:
            return self._json({"error": "없음"}, 404)
        if not p.is_file():
            return self._json({"error": "파일 없음"}, 404)
        self._send_file(p, ctype)

    def do_GET(self):
        if not self._guard():
            return
        u = urllib.parse.urlparse(self.path)
        q = {k: v[0] for k, v in urllib.parse.parse_qs(u.query).items()}
        try:
            if u.path == "/":
                b = PAGE.replace("__TOKEN__", STATE["token"]).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Cache-Control", "no-store")
                self.end_headers()
                self.wfile.write(b)
            elif u.path.startswith("/media/"):
                self._media([urllib.parse.unquote(x) for x in u.path[len("/media/"):].split("/")])
            elif u.path == "/api/topics":
                self._json({"topics": topics()})
            elif u.path == "/api/env":
                t = q["topic"]
                te, re_ = read_env(topic_env_path(t)), read_env(ROOT / ".env")
                st = {k: (mask(te[k]) + " (이 주제)") if te.get(k) else ((mask(re_[k]) + " (공통 .env)") if re_.get(k) else "없음") for k in YT_KEYS}
                st["GITHUB_TOKEN"] = mask(te.get("GITHUB_TOKEN") or re_.get("GITHUB_TOKEN") or "") or "없음"
                self._json({"status": st, "channel": channel_of(t)})
            elif u.path == "/api/videos":
                if JOB.busy:
                    self._json({"error": f"'{JOB.name}' 진행 중 — 끝나면 저절로 새로 고침"})
                else:
                    self._json(list_videos(q["topic"]))
            elif u.path == "/api/preview":
                t, vid = q.get("topic", ""), q.get("vid", "")
                if not TOPIC_RE.fullmatch(t) or not VID_RE.fullmatch(vid):
                    return self._json({"ok": False, "error": "주제·영상 이름 오류"})
                try:
                    with contextlib.redirect_stdout(_Tee()):
                        self._json(preview(t, vid))
                except SystemExit as e:
                    self._json({"ok": False, "error": str(e)[:400]})
            elif u.path == "/api/job":
                self._json({"busy": JOB.busy, "name": JOB.name, "seq": JOB.seq, "lines": JOB.lines[-400:], "result": JOB.result})
            else:
                self._json({"error": "없음"}, 404)
        except Exception as e:   # noqa: BLE001
            self._json({"ok": False, "error": str(e)[:400]}, 200)

    def do_POST(self):
        if not self._guard():
            return
        n = int(self.headers.get("Content-Length") or 0)
        try:
            d = json.loads(self.rfile.read(n) or b"{}")
        except json.JSONDecodeError:
            return self._json({"ok": False, "error": "JSON 오류"}, 400)
        t = str(d.get("topic", ""))
        if not TOPIC_RE.fullmatch(t):
            return self._json({"ok": False, "error": "주제 이름 오류"}, 400)
        vid = str(d.get("vid", ""))
        p = urllib.parse.urlparse(self.path).path
        if p in ("/api/test", "/api/upload", "/api/fetch_video") and not VID_RE.fullmatch(vid):
            return self._json({"ok": False, "error": "영상 이름 오류"}, 400)
        if p == "/api/env":
            vals = {k: str(v).strip() for k, v in (d.get("values") or {}).items() if k in YT_KEYS + ("GITHUB_TOKEN",) and str(v).strip()}
            if any(re.search(r"\s", v) for v in vals.values()):
                return self._json({"ok": False, "error": "값에 빈칸이 있음"})
            gh = {k: vals.pop(k) for k in list(vals) if k == "GITHUB_TOKEN"}
            if vals:
                (ROOT / t).mkdir(exist_ok=True)
                ya.save_env(topic_env_path(t), vals)
            if gh:
                ya.save_env(ROOT / ".env", gh)
            log("ENV", topic=t, saved=",".join(list(vals) + list(gh)) or "-")
            return self._json({"ok": True, "saved": list(vals) + list(gh)})
        if p == "/api/auth":
            if d.get("mode") == "new":
                def fresh(topic):
                    apply_env(topic)
                    if not (os.environ.get("YOUTUBE_CLIENT_ID") and os.environ.get("YOUTUBE_CLIENT_SECRET")):
                        raise SystemExit("[AUTH] ❌ YOUTUBE_CLIENT_ID · SECRET 을 먼저 넣고 저장")
                    log("AUTH", status="new", topic=topic, action="브라우저 인증 — 계정 고르기 창에서 이 주제 채널(브랜드 계정)을 고름")
                    refresh, missing = ya.issue(os.environ["YOUTUBE_CLIENT_ID"], os.environ["YOUTUBE_CLIENT_SECRET"], say=print)
                    ya.save_env(topic_env_path(topic), {"YOUTUBE_CLIENT_ID": os.environ["YOUTUBE_CLIENT_ID"], "YOUTUBE_CLIENT_SECRET": os.environ["YOUTUBE_CLIENT_SECRET"], "YOUTUBE_REFRESH_TOKEN": refresh})
                    os.environ["YOUTUBE_REFRESH_TOKEN"] = refresh
                    log("AUTH", status="saved", file=f"{topic}/.env", missing_scopes=",".join(missing) or "-")
                    return {"ok": True, "channel": ensure_auth(topic)[1]}
                ok = run_job(f"다시 인증 ({t})", fresh, t)
            else:
                ok = run_job(f"키 확인 ({t})", lambda topic: {"ok": True, "channel": ensure_auth(topic)[1]}, t)
            return self._json({"ok": ok, "error": "" if ok else "다른 작업이 진행 중"})
        if p == "/api/channel":
            if d.get("mode") != "remember":
                return self._json({"ok": False, "error": "모드 오류"})
            try:
                with contextlib.redirect_stdout(_Tee()):
                    return self._json({"ok": True, "result": remember_channel(t)})
            except SystemExit as e:
                return self._json({"ok": False, "error": str(e)[:400]})
        if p == "/api/test":
            ok = run_job(f"시험 {vid}", do_test, t, vid)
            return self._json({"ok": ok, "error": "" if ok else "다른 작업이 진행 중"})
        if p == "/api/fetch_video":
            ok = run_job(f"영상 받기 {vid}", lambda topic, v: (get_video(topic, v), {"ok": True})[1], t, vid)
            return self._json({"ok": ok, "error": "" if ok else "다른 작업이 진행 중"})
        if p == "/api/upload":
            try:
                days, hhmm = int(d.get("days", 7)), str(d.get("hhmm", "17:00"))
                assert 1 <= days <= 60 and re.fullmatch(r"\d{1,2}:\d{2}", hhmm)
            except (ValueError, AssertionError):
                return self._json({"ok": False, "error": "예약 날짜·시각 오류"})
            allow = str(d.get("allow_channel") or "")
            if allow and not CID_RE.fullmatch(allow):
                return self._json({"ok": False, "error": "채널 ID 오류"})
            if allow and LAST_KEY_CHANNEL.get(t, {}).get("channel_id") != allow:
                return self._json({"ok": False, "error": "확인한 채널이 마지막 키 확인 결과와 다름 — [키 확인]부터 다시"})
            ok = run_job(f"업로드 {vid}", do_upload, t, vid, days, hhmm, allow, bool(d.get("remember")))
            return self._json({"ok": ok, "error": "" if ok else "다른 작업이 진행 중"})
        return self._json({"ok": False, "error": "없음"}, 404)


def free_port(want: int) -> int:
    with socket.socket() as s:
        try:
            s.bind(("127.0.0.1", want))
            return want
        except OSError:
            s.bind(("127.0.0.1", 0))
            return s.getsockname()[1]


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="PC 업로드 화면 (주제별 키 · 자료 점검 · 일주일 뒤 예약 업로드)")
    ap.add_argument("--port", type=int, default=8770)
    ap.add_argument("--no-browser", action="store_true")
    ap.add_argument("--repo", default=os.environ.get("GITHUB_REPO", REPO), help="자료를 읽을 GitHub 저장소 (owner/name)")
    a = ap.parse_args(argv)
    STATE["repo"] = a.repo
    port = free_port(a.port)
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", port), Handler)
    url = f"http://127.0.0.1:{port}/"
    log("START", tool=f"upload_web.py {VERSION}", url=url, repo=a.repo, note="이 창을 닫으면 화면도 꺼짐 · 연구·교육용")
    if not a.no_browser:
        threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        log("STOP", note="끝")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
