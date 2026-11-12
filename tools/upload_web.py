#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-11-12 — 인증 주소를 줄이지 않고 로그에(say=print) · 키가 없을 때와 토큰 만료를 다른 말로 · 화면 다듬음(긴 로그 줄바꿈 ·
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

VERSION = "v1.0"
REPO, MAIN, UPL = "yeomin1024/yeomin1024-ytb", "main", "uploads"
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
        vj = ROOT / topic / "source" / vid / "video.json"
        if vj.is_file():
            rec = json.loads(vj.read_text("utf-8"))
            missing = [x["name"] for x in rec["parts"] if f"{rec['dir']}/{x['name']}" not in upl_paths]
            items["영상"] = [not missing, f"{rec['size'] / 1e6:.0f}MB · 조각 {len(rec['parts'])}개" + (f" — uploads 브랜치에 없음: {', '.join(missing)}" if missing else " ✓ uploads 브랜치")]
        else:
            items["영상"] = [False, "video.json 없음 — Claude 가 tools/upload_pack.py pack 으로 올려야 함"]
        local = ROOT / topic / "out" / vid / "final_1080p.mp4"
        ready.append({"vid": vid, "items": items, "ready": all(v[0] for v in items.values()), "titles": r.get("titles", []),
                      "downloaded": local.is_file()})
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
        JOB.lines.clear()

    def body():
        try:
            with contextlib.redirect_stdout(_Tee()):
                JOB.result = fn(*args) or {}
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


def ensure_auth(topic: str) -> tuple[str, str]:
    """키 확인 → (채널 ID, 이름). 토큰이 없거나 만료(invalid_grant)면 브라우저 인증을 띄워 새 토큰을 <주제>/.env 에 저장하고 다시."""
    apply_env(topic)
    for attempt in (1, 2):
        try:
            token = yu.access_token()
            cid, title = yu.check_channel(topic, token)
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


def apply_title(topic: str, vid: str, n: int) -> str:
    """고른 제목 안을 이 PC 의 upload.md(1번 섹션 코드 블록)와 titles.md(짝 썸네일)에 적음 — GitHub 의 시트는 그대로."""
    src = ROOT / topic / "source" / vid
    md = (src / "upload.md").read_text("utf-8")
    opts = up.title_options(md)
    pick = next((o for o in opts if o["n"] == n), opts[0] if opts else None)
    if not pick:
        raise SystemExit("[SHEET] ❌ 제목 안을 찾지 못함 (upload.md 1번 섹션)")
    if len(opts) > 1:
        m = re.search(r"^(##\s*\d+\.\s*[^\n]*제목[^\n]*\n)", md, re.M)
        md = md[:m.end()] + f"\n```\n{pick['title']}\n```\n" + md[m.end():]
        (src / "upload.md").write_text(md, "utf-8")
    (src / "titles.md").write_text(f"# 고른 제목 (upload_web.py {VERSION})\n- [x] {pick['title']} — 짝 썸네일: thumbnail_{pick['thumb']}\n", "utf-8")
    log("TITLE", video=vid, pick=pick["n"], thumbnail=f"thumbnail_{pick['thumb']}", title=pick["title"][:60].replace(" ", "_"))
    return pick["title"]


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


def do_upload(topic: str, vid: str, n: int, days: int, hhmm: str) -> dict:
    t0 = time.time()
    when = publish_time(days, hhmm)
    log("START", tool=f"upload_web.py {VERSION}", topic=topic, video=vid, publish_kst=when.astimezone(KST).strftime("%Y-%m-%d_%H:%M"))
    cid, ch = ensure_auth(topic)
    lst = list_videos(topic)
    v = next((x for x in lst["videos"] if x["vid"] == vid), None)
    if not v:
        raise SystemExit(f"[UPLOAD] ❌ {vid}: 올릴 목록에 없음 (이미 올렸거나 upload.md 없음)")
    bad = [f"{k}: {note}" for k, (ok, note) in v["items"].items() if not ok]
    if bad:
        raise SystemExit("[UPLOAD] ❌ 자료가 덜 됨 — " + " · ".join(bad))
    title = apply_title(topic, vid, n)
    path = get_video(topic, vid)
    res = yu.run(topic, vid, video=str(path), publish_at=when.strftime("%Y-%m-%dT%H:%M:%SZ"))
    state = ROOT / topic / "source" / vid / "youtube.json"
    pushed = gh_put_new(f"{topic}/source/{vid}/youtube.json", state.read_bytes(),
                        f"유튜브 예약 업로드: {vid} (공개 {when.astimezone(KST):%Y-%m-%d %H:%M} KST, PC upload_web.py {VERSION})") if state.is_file() else "failed:youtube.json 없음"
    log("PUSH", video=vid, result=pushed.replace(" ", "_")[:120], note="youtube.json 이 GitHub 에 있어야 다른 PC·Claude 가 올린 줄 앎" if pushed.startswith("failed") else "-")
    url = (res or {}).get("url", "")
    log("DONE", video=vid, url=url or "-", channel=ch, title=title[:50].replace(" ", "_"), sec=round(time.time() - t0),
        next="공개 전에 스튜디오에서 영상·자막·썸네일 확인 · 2·3안 썸네일은 스튜디오 '테스트 및 비교'")
    return {"ok": True, "url": url, "publishAt": when.isoformat(), "pushed": pushed}


# ─────────── 웹 ───────────
PAGE = r"""<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>유튜브 업로드</title><style>
:root{--bg:#F5F6F8;--card:#fff;--ink:#1B2130;--sub:#5B6475;--line:#E2E5EB;--ok:#16946B;--bad:#D23B2E;--acc:#2F6BFF}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 system-ui,-apple-system,"Malgun Gothic","Apple SD Gothic Neo",sans-serif}
header{padding:18px 24px;background:#151A26;color:#fff}header h1{margin:0;font-size:20px}header p{margin:4px 0 0;color:#B8C0D0;font-size:13px}
.tabs{display:flex;gap:6px;padding:12px 24px;flex-wrap:wrap;background:#fff;border-bottom:1px solid var(--line)}
.tabs button{border:1px solid var(--line);background:#fff;border-radius:999px;padding:6px 14px;cursor:pointer;font-size:14px}
.tabs button.on{background:var(--ink);color:#fff;border-color:var(--ink)}
main{max-width:1100px;margin:0 auto;padding:18px 16px 40px;display:grid;gap:16px}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px 18px}.card h2{margin:0 0 10px;font-size:16px}
.row{display:grid;grid-template-columns:220px 1fr auto;gap:8px;align-items:center;margin:6px 0}
input{width:100%;padding:8px 10px;border:1px solid var(--line);border-radius:8px;font:inherit}
.btn{border:0;border-radius:9px;padding:8px 14px;background:var(--ink);color:#fff;cursor:pointer;font:inherit;white-space:nowrap}
.btn.sec{background:#fff;color:var(--ink);border:1px solid var(--line)}.btn.go{background:var(--acc)}.btn:disabled{opacity:.4;cursor:default}
.muted{color:var(--sub);font-size:13px}.ok{color:var(--ok)}.bad{color:var(--bad)}
table{width:100%;border-collapse:collapse}td,th{border-top:1px solid var(--line);padding:8px 6px;vertical-align:top;text-align:left;font-size:14px}
.chips{display:flex;flex-wrap:wrap;gap:4px}.chip{font-size:12px;border-radius:999px;padding:2px 8px;background:#EEF7F2;color:var(--ok)}.chip.x{background:#FDEEEC;color:var(--bad)}
pre{background:#10141D;color:#D9E1F2;border-radius:10px;padding:12px;max-height:360px;overflow:auto;font-size:12px;white-space:pre-wrap;overflow-wrap:anywhere;word-break:break-all;margin:0}
main>*{min-width:0}
label.t{display:flex;gap:6px;align-items:flex-start;margin:3px 0;font-size:14px;cursor:pointer}label.t input{width:auto;margin-top:4px}
.sched{display:flex;gap:10px;align-items:center;flex-wrap:wrap}.sched input{width:90px}.sched input[type=time]{width:150px}
@media(max-width:700px){.row{grid-template-columns:1fr}}
</style></head><body>
<header><h1>유튜브 업로드 (이 PC 에서만 열림)</h1><p>자료가 다 된 대본만 [업로드] — 비공개로 올리고 정한 날 자동 공개 · 키는 이 PC 의 .env 에만 저장 · 연구·교육용 영상 (투자 권유 아님)</p></header>
<nav class="tabs" id="tabs"></nav>
<main>
<section class="card"><h2>키 설정 — <span id="tname"></span> <span class="muted" id="chan"></span></h2>
<div id="keys"></div>
<div class="row"><span>GITHUB_TOKEN <span class="muted">(모든 주제 공통 · youtube.json 기록)</span></span><input id="k_GITHUB_TOKEN" type="password" placeholder="" autocomplete="off"><span class="muted" id="s_GITHUB_TOKEN"></span></div>
<p style="display:flex;gap:8px;flex-wrap:wrap"><button class="btn" onclick="saveKeys()">저장</button><button class="btn sec" onclick="checkAuth()">키 확인</button><button class="btn sec" onclick="reauth()">다시 인증 (새 토큰)</button></p>
<p class="muted">토큰이 만료되면 [업로드]·[키 확인] 때 브라우저 인증 창이 저절로 열립니다 — 이 주제 채널의 구글 계정으로 로그인하고 체크 칸을 모두 허용하면 새 토큰이 이 주제 .env 에 저장되고 그대로 이어 갑니다. 7일마다 만료되면 Google Cloud 콘솔 → OAuth 동의 화면 → 게시 상태를 '프로덕션'으로.</p>
</section>
<section class="card"><h2>예약</h2><div class="sched">오늘부터 <input id="days" type="number" min="1" max="60" value="7"> 일 뒤 <input id="hhmm" type="time" value="17:00"> (한국 시간) 공개 → <b id="when"></b></div>
<p class="muted">유튜브 할당량: 영상 하나 약 2,050단위 · 하루 10,000 (하루에 4편까지) · 하루는 한국 오후 4~5시에 바뀜</p></section>
<section class="card"><h2>올릴 대본 <button class="btn sec" style="float:right" onclick="loadVideos()">새로 고침</button></h2><div id="videos" class="muted">불러오는 중…</div></section>
<section class="card"><h2>로그 <span class="muted" id="jobname"></span></h2><pre id="log"></pre></section>
</main>
<script>
const TOKEN="__TOKEN__";let TOPIC="";const KEYS=["YOUTUBE_CLIENT_ID","YOUTUBE_CLIENT_SECRET","YOUTUBE_REFRESH_TOKEN"];
const esc=s=>String(s==null?"":s).replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
async function api(p,body){const r=await fetch(p,body?{method:"POST",headers:{"Content-Type":"application/json","X-Upload-Token":TOKEN},body:JSON.stringify(body)}:{headers:{"X-Upload-Token":TOKEN}});return r.json()}
async function boot(){const s=await api("/api/topics");const t=document.getElementById("tabs");t.innerHTML="";s.topics.forEach(n=>{const b=document.createElement("button");b.textContent=n;b.onclick=()=>pick(n);b.id="tab_"+n;t.appendChild(b)});pick(s.topics.includes("stock")?"stock":s.topics[0]);setInterval(pollJob,1500);upd()}
async function pick(n){TOPIC=n;document.querySelectorAll(".tabs button").forEach(b=>b.classList.toggle("on",b.id==="tab_"+n));document.getElementById("tname").textContent=n;await loadKeys();loadVideos()}
async function loadKeys(){const s=await api("/api/env?topic="+encodeURIComponent(TOPIC));document.getElementById("chan").textContent=s.channel?`(채널: ${s.channel.name||""} ${s.channel.channel_id||""})`:"(youtube_channel.json 없음 — 채널 확인 안 함)";
 document.getElementById("keys").innerHTML=KEYS.map(k=>`<div class="row"><span>${k}</span><input id="k_${k}" type="password" autocomplete="off" placeholder="${k==="YOUTUBE_REFRESH_TOKEN"?"비워 두면 [다시 인증]으로 저절로":""}"><span class="muted">${esc(s.status[k]||"없음")}</span></div>`).join("");
 document.getElementById("s_GITHUB_TOKEN").textContent=s.status.GITHUB_TOKEN||"없음"}
async function saveKeys(){const v={};KEYS.concat(["GITHUB_TOKEN"]).forEach(k=>{const x=document.getElementById("k_"+k).value.trim();if(x)v[k]=x});const r=await api("/api/env",{topic:TOPIC,values:v});alert(r.ok?"저장했습니다 ("+r.saved.join(", ")+")":"실패: "+r.error);loadKeys()}
async function checkAuth(){const r=await api("/api/auth",{topic:TOPIC,mode:"check"});if(!r.ok)alert(r.error)}
async function reauth(){const r=await api("/api/auth",{topic:TOPIC,mode:"new"});if(!r.ok)alert(r.error)}
function upd(){const d=+document.getElementById("days").value||7,h=document.getElementById("hhmm").value||"17:00";const t=new Date(Date.now()+d*864e5);const p=n=>String(n).padStart(2,"0");
 const kst=new Date(t.getTime()+(t.getTimezoneOffset()+540)*6e4);document.getElementById("when").textContent=`${kst.getFullYear()}-${p(kst.getMonth()+1)}-${p(kst.getDate())} ${h}`}
document.addEventListener("input",e=>{if(e.target.id==="days"||e.target.id==="hhmm")upd()});
async function loadVideos(){const box=document.getElementById("videos");box.innerHTML="GitHub 에서 자료를 받는 중…";const s=await api("/api/videos?topic="+encodeURIComponent(TOPIC));
 if(s.error){box.innerHTML=`<span class="bad">${esc(s.error)}</span>`;return}
 let h=`<table><tr><th>대본</th><th>제목</th><th>자료</th><th></th></tr>`;
 if(!s.videos.length)h+=`<tr><td colspan="4" class="muted">올릴 대본이 없습니다 (upload.md 가 있고 youtube.json 이 없는 대본)</td></tr>`;
 s.videos.forEach(v=>{const t=v.titles.length>1?v.titles.map((o,i)=>`<label class="t"><input type="radio" name="t_${v.vid}" value="${o.n}" ${i?"":"checked"}> ${o.n}안 ${esc(o.title)} <span class="muted">(thumbnail_${o.thumb})</span></label>`).join(""):esc(v.titles[0]?v.titles[0].title:"(제목 없음)");
  const c=Object.entries(v.items).map(([k,[ok,n]])=>`<span class="chip ${ok?"":"x"}" title="${esc(n)}">${ok?"✓":"✗"} ${esc(k)}</span>`).join("");
  h+=`<tr><td><b>${esc(v.vid)}</b><br><span class="${v.ready?"ok":"bad"}">${v.ready?"준비됨":"부족"}</span>${v.downloaded?'<br><span class="muted">영상 받아 둠</span>':""}</td><td>${t}</td><td><div class="chips">${c}</div></td>
  <td style="white-space:nowrap"><button class="btn sec" onclick="test('${v.vid}')">시험</button> <button class="btn go" ${v.ready?"":"disabled"} onclick="upload('${v.vid}')">업로드</button></td></tr>`});
 h+=`</table>`;const kst=iso=>{if(!iso)return"";const d=new Date(iso);if(isNaN(d))return iso;const k=new Date(d.getTime()+(d.getTimezoneOffset()+540)*6e4),p=n=>String(n).padStart(2,"0");return `${k.getFullYear()}-${p(k.getMonth()+1)}-${p(k.getDate())} ${p(k.getHours())}:${p(k.getMinutes())} 공개`};
 if(s.uploaded.length)h+=`<p class="muted">올린 영상: `+s.uploaded.map(u=>`${esc(u.vid)} ${u.url?`<a href="${esc(u.url)}" target="_blank">열기</a>`:""} ${esc(kst(u.publishAt))}`).join(" · ")+`</p>`;box.innerHTML=h}
async function test(vid){const r=await api("/api/test",{topic:TOPIC,vid});if(!r.ok)alert(r.error)}
async function upload(vid){const sel=document.querySelector(`input[name="t_${vid}"]:checked`);const n=sel?+sel.value:1;const d=+document.getElementById("days").value||7,h=document.getElementById("hhmm").value||"17:00";
 if(!confirm(`${vid}\n${d}일 뒤 ${h} (한국 시간) 공개로 예약 업로드할까요?`))return;const r=await api("/api/upload",{topic:TOPIC,vid,title:n,days:d,hhmm:h});if(!r.ok)alert(r.error)}
let wasBusy=false;async function pollJob(){const s=await api("/api/job");const l=document.getElementById("log");const atEnd=l.scrollTop+l.clientHeight>=l.scrollHeight-20;l.textContent=s.lines.join("\n");if(atEnd)l.scrollTop=l.scrollHeight;
 document.getElementById("jobname").textContent=s.busy?`— ${s.name} 진행 중…`:(s.name?`— ${s.name} ${s.result&&s.result.ok===false?"실패":"끝"}`:"");
 if(wasBusy&&!s.busy){loadKeys();if(s.name.startsWith("업로드"))loadVideos()}wasBusy=s.busy}
boot();
</script></body></html>"""


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
        return True

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
                self.end_headers()
                self.wfile.write(b)
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
            elif u.path == "/api/job":
                self._json({"busy": JOB.busy, "name": JOB.name, "lines": JOB.lines[-400:], "result": JOB.result})
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
        if not re.fullmatch(r"[a-z0-9_-]+", t):
            return self._json({"ok": False, "error": "주제 이름 오류"}, 400)
        p = urllib.parse.urlparse(self.path).path
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
                    os.environ["YOUTUBE_REFRESH_TOKEN"] = "x"          # 일부러 만료처럼 → 브라우저 인증
                    ya_cid = os.environ.get("YOUTUBE_CLIENT_ID")
                    if not ya_cid:
                        raise SystemExit("[AUTH] ❌ YOUTUBE_CLIENT_ID · SECRET 을 먼저 넣고 저장")
                    refresh, missing = ya.issue(os.environ["YOUTUBE_CLIENT_ID"], os.environ["YOUTUBE_CLIENT_SECRET"], say=print)
                    ya.save_env(topic_env_path(topic), {"YOUTUBE_CLIENT_ID": os.environ["YOUTUBE_CLIENT_ID"], "YOUTUBE_CLIENT_SECRET": os.environ["YOUTUBE_CLIENT_SECRET"], "YOUTUBE_REFRESH_TOKEN": refresh})
                    log("AUTH", status="saved", file=f"{topic}/.env", missing_scopes=",".join(missing) or "-")
                    return {"ok": True, "channel": ensure_auth(topic)[1]}
                ok = run_job(f"다시 인증 ({t})", fresh, t)
            else:
                ok = run_job(f"키 확인 ({t})", lambda topic: {"ok": True, "channel": ensure_auth(topic)[1]}, t)
            return self._json({"ok": ok, "error": "" if ok else "다른 작업이 진행 중"})
        if p == "/api/test":
            ok = run_job(f"시험 {d.get('vid')}", do_test, t, str(d.get("vid")))
            return self._json({"ok": ok, "error": "" if ok else "다른 작업이 진행 중"})
        if p == "/api/upload":
            try:
                days, hhmm = int(d.get("days", 7)), str(d.get("hhmm", "17:00"))
                assert 1 <= days <= 60 and re.fullmatch(r"\d{1,2}:\d{2}", hhmm)
            except (ValueError, AssertionError):
                return self._json({"ok": False, "error": "예약 날짜·시각 오류"})
            ok = run_job(f"업로드 {d.get('vid')}", do_upload, t, str(d.get("vid")), int(d.get("title", 1)), days, hhmm)
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
