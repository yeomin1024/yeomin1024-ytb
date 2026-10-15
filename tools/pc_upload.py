#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-15 — 사용자 지시 "압축본 올린거 삭제하고 구글 드라이브 내 드라이브에 youtube 폴더에 주제 (예: economic)맞는 폴더에
#          원본 영상 올리고 pc에서 영상 및 환경설정을 받아서 업로드 하는 코드 만들어서 올리는 걸로 하자 자동 예약 기능도 있어야해":
#          PC 에서 GitHub 의 업로드 설정(upload.md·자막·썸네일)과 Google Drive 의 원본 영상을 받아 유튜브에 비공개로 올리고
#          예약 공개(기본: 실행 시각 + 1시간)를 건 뒤 youtube.json 을 GitHub 에 기록한다. 실행기: run_uploader.ps1
r"""
PC 업로더 — 보통은 run_uploader.ps1 이 부른다 (guides/upload_guide.md 11번).

  python tools/pc_upload.py                          # economic 의 준비된 영상 전부 → 비공개 업로드 + 지금부터 1시간 뒤 공개
  python tools/pc_upload.py --dry-run                # 올리지 않고: GitHub 설정·Drive 영상·시트 검사·예약 시각만
  python tools/pc_upload.py --ids isa-mangi-2026-10 --delay 3h
  python tools/pc_upload.py --gap 24h                # 첫 영상 1시간 뒤, 다음 영상부터 24시간씩 (하루에 하나씩 공개)
  python tools/pc_upload.py --at "2026-10-16 18:00"  # 첫 영상 공개 시각을 직접 (한국 시간), 다음 영상은 --gap 만큼 뒤

준비된 영상 = GitHub <주제>/source/<영상ID>/ 에 upload.md 가 있고 youtube.json 이 없는 영상
  + Google Drive '내 드라이브/youtube/<주제>/<영상ID>.mp4' (Claude 가 렌더 뒤 tools/drive_videos.py 로 올림, 또는 사용자가 직접 넣음).
  PC 에 'Google Drive 데스크톱'이 있으면 그 폴더의 파일을 바로 쓰고, 없으면 Drive API 로 <주제>/out/<영상ID>/final_1080p.mp4 에 받는다
  (올린 뒤 지움, --keep-video 면 둠). GitHub 의 drive.json md5 와 다르면 경고.
받는 설정 (GitHub → 이 폴더의 <주제>/source/<영상ID>/): upload.md · <영상ID>.txt · <영상ID>.srt · titles.md · drive.json · thumbnails/thumbnail_N.*
키 (.env, 맨 위 또는 <주제>/.env — run_uploader.ps1 이 틀을 만듦): YOUTUBE_CLIENT_ID · YOUTUBE_CLIENT_SECRET · YOUTUBE_REFRESH_TOKEN
  (Drive API 로 받으려면 토큰에 Drive 권한 — tools/youtube_auth.py v1.2) · GITHUB_TOKEN (youtube.json 기록 — Contents 쓰기, 없으면 이 PC 에만 남김)
할당량: 영상 하나 약 2,050단위, 하루 10,000 → 하루 최대 4개 (--max 4). 넘으면 멈추고, 다음 날 다시 실행하면 남은 영상부터.
⚠️ Google 감사를 받지 않은 API 프로젝트로 올린 영상은 비공개로 잠겨 예약 공개가 안 될 수 있다 (guides/pipeline.md '업로드 주의').
※ 연구·교육용 도구다. 영상 내용은 투자·세무·보험 상담이나 권유가 아니다.
"""
import argparse
import base64
import datetime as dt
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent
sys.path.insert(0, str(TOOLS))
import drive_videos as dv  # noqa: E402
import youtube_upload as yu  # noqa: E402

VERSION = "v1.0"
REPO, BRANCH = "yeomin1024/yeomin1024-ytb", "main"
UNITS_PER_VIDEO = 1600 + 400 + 50
DAILY_UNITS = 10_000
KST = dt.timezone(dt.timedelta(hours=9))
STOP_WORDS = ("quotaExceeded", "uploadLimitExceeded", "dailyLimitExceeded", "rateLimitExceeded")
THUMB_RE = re.compile(r"^thumbnail_\d\.(png|jpe?g|webp)$", re.I)
KEYS = ("YOUTUBE_CLIENT_ID", "YOUTUBE_CLIENT_SECRET", "YOUTUBE_REFRESH_TOKEN")


def log(stage, **kv):
    yu.log(stage, **{k: (str(v).replace(" ", "_") if isinstance(v, str) else v) for k, v in kv.items()})


def load_env(*paths):
    """.env 의 KEY=VALUE → os.environ (이미 값이 있는 환경 변수는 그대로). 값은 출력하지 않는다. → 읽은 키 이름들"""
    got = []
    for p in paths:
        p = Path(p)
        if not p.is_file():
            continue
        for ln in p.read_text("utf-8-sig").splitlines():
            m = re.match(r"^\s*([A-Z][A-Z0-9_]*)\s*=\s*['\"]?([^'\"\s]*)", ln)
            if m and m.group(2) and not os.environ.get(m.group(1), "").strip():
                os.environ[m.group(1)] = m.group(2)
                got.append(m.group(1))
    return got


def parse_span(s):
    m = re.fullmatch(r"(\d+(?:\.\d+)?)([hm])", (s or "").strip())
    if not m:
        raise SystemExit(f"[START] ❌ 시간 형식 오류: {s!r} (예: 1h, 90m, 24h)")
    v = float(m.group(1))
    return dt.timedelta(hours=v) if m.group(2) == "h" else dt.timedelta(minutes=v)


def parse_at(s):
    """'2026-10-16 18:00' (한국 시간) 또는 ISO 8601 → UTC datetime."""
    s = s.strip()
    try:
        t = dt.datetime.fromisoformat(s.replace("Z", "+00:00"))
    except ValueError:
        raise SystemExit(f"[START] ❌ --at 형식 오류: {s!r} (예: 2026-10-16 18:00 — 한국 시간)") from None
    return (t if t.tzinfo else t.replace(tzinfo=KST)).astimezone(dt.timezone.utc)


class GitHub:
    """GitHub Contents API (비공개 저장소도 — 토큰은 머리글로만, 출력하지 않음)."""

    def __init__(self, repo=REPO, branch=BRANCH, token=""):
        self.repo, self.branch, self.token = repo, branch, token

    def _req(self, method, path, data=None, accept="application/vnd.github+json"):
        url = f"https://api.github.com/repos/{self.repo}/contents/{urllib.parse.quote(path)}"
        if method == "GET":
            url += f"?ref={self.branch}"
        h = {"Accept": accept, "X-GitHub-Api-Version": "2022-11-28", "User-Agent": "pc-upload"}
        if self.token:
            h["Authorization"] = f"Bearer {self.token}"
        req = urllib.request.Request(url, data=data, method=method, headers=h)
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.status, r.read()
        except urllib.error.HTTPError as e:
            return e.code, e.read()

    def list(self, path):
        st, body = self._req("GET", path)
        if st == 404:
            return []
        if st != 200:
            raise RuntimeError(f"GitHub 목록 실패 {path}: HTTP {st} {body[:200]!r} → 비공개 저장소면 .env 의 GITHUB_TOKEN 확인")
        return json.loads(body)

    def raw(self, path):
        st, body = self._req("GET", path, accept="application/vnd.github.raw")
        if st == 404:
            return None
        if st != 200:
            raise RuntimeError(f"GitHub 받기 실패 {path}: HTTP {st}")
        return body

    def put_new(self, path, content, message):
        """새 파일 만들기. 이미 있으면 건드리지 않음. → 'created' · 'exists' · 'failed:<이유>'"""
        if not self.token:
            return "failed:GITHUB_TOKEN 없음"
        data = json.dumps({"message": message, "content": base64.b64encode(content).decode(), "branch": self.branch}).encode()
        st, body = self._req("PUT", path, data=data)
        if st in (200, 201):
            return "created"
        if st == 422 and b"sha" in body:
            return "exists"
        return f"failed:HTTP {st} {body[:160].decode(errors='replace')}"


def find_candidates(gh, topic, ids=None):
    """GitHub 의 <주제>/source/* 중 upload.md 가 있고 youtube.json 이 없는 영상 → [(영상ID, 목록)], [(영상ID, 건너뛴 이유)]"""
    ready, skipped = [], []
    for e in sorted(gh.list(f"{topic}/source"), key=lambda x: x["name"]):
        if e.get("type") != "dir" or (ids and e["name"] not in ids):
            continue
        vid = e["name"]
        listing = gh.list(f"{topic}/source/{vid}")
        names = {x["name"] for x in listing}
        if "upload.md" not in names:
            continue                                    # 업로드 시트가 없는 대본 폴더 (아직 영상 전)
        if "youtube.json" in names or (ROOT / topic / "source" / vid / "youtube.json").exists():
            skipped.append((vid, "이미 올림 (youtube.json)"))
            continue
        ready.append((vid, listing))
    return ready, skipped


def fetch_settings(gh, topic, vid, listing):
    """업로드에 쓰는 파일만 GitHub → 이 폴더 (youtube.json 은 건드리지 않음). → 받은 파일 수"""
    dst = ROOT / topic / "source" / vid
    names = {x["name"]: x for x in listing}
    want = ["upload.md", f"{vid}.txt", f"{vid}.srt", "titles.md", "drive.json"]
    n = 0
    for name in want:
        if name in names:
            body = gh.raw(f"{topic}/source/{vid}/{name}")
            if body is not None:
                (dst / name).parent.mkdir(parents=True, exist_ok=True)
                (dst / name).write_bytes(body)
                n += 1
    if "thumbnails" in names:
        for t in gh.list(f"{topic}/source/{vid}/thumbnails"):
            if t.get("type") == "file" and THUMB_RE.match(t["name"]):
                body = gh.raw(f"{topic}/source/{vid}/thumbnails/{t['name']}")
                if body is not None:
                    (dst / "thumbnails").mkdir(parents=True, exist_ok=True)
                    (dst / "thumbnails" / t["name"]).write_bytes(body)
                    n += 1
    for need in ("upload.md", f"{vid}.txt", f"{vid}.srt"):
        if not (dst / need).is_file():
            raise SystemExit(f"[SETTINGS] ❌ {vid}: {need} 를 받지 못함")
    log("SETTINGS", video=vid, files=n, dst=str(dst.relative_to(ROOT)))
    return n


def locate_video(topic, vid, dry_run, token_fn):
    """→ (출처, 경로 또는 None, 메모). 출처: local(Drive 데스크톱 폴더) · drive(받음) · missing · unknown(dry-run 에서 키 없음)"""
    p = dv.local_video(topic, vid)
    if p:
        return "local", p, f"Google Drive 데스크톱 폴더 {p}"
    try:
        token = token_fn()
    except SystemExit as e:
        if dry_run:
            return "unknown", None, f"Drive 확인 못 함 (키 없음: {str(e)[:80]})"
        raise
    try:
        f = dv.find_video(token, topic, vid)
    except dv.DriveError as e:
        if dry_run:
            return "unknown", None, f"Drive 확인 못 함 ({str(e)[:90]})"
        raise
    if not f:
        return "missing", None, f"Drive 에 없음: 내 드라이브/{dv.TOP}/{topic}/{vid}.mp4"
    if dry_run:
        return "drive", None, f"Drive 에 있음 {int(f.get('size', 0)) / 1e6:.1f}MB (dry-run 이라 받지 않음)"
    dest = ROOT / topic / "out" / vid / "final_1080p.mp4"
    dv.download(f, dest, token)
    return "drive", dest, f"Drive 에서 받음 {dest.stat().st_size / 1e6:.1f}MB"


def check_md5(topic, vid, path):
    rec = ROOT / topic / "source" / vid / "drive.json"
    if not (rec.is_file() and path):
        return
    want = json.loads(rec.read_text("utf-8")).get("md5")
    got = dv.md5(path)
    if want and want != got:
        log("CHECK", video=vid, warning="Drive 영상이 drive.json 기록과 다름 (다시 렌더했거나 손으로 바꿈) — 그대로 올림", want=want, got=got)


def check_sheet(topic, vid):
    """dry-run: 업로드 시트만 검사 (제목·설명란·태그 길이, 챕터 다시 계산). → 문제 목록"""
    meta = yu.read_sheet(topic, vid)
    meta["description"], chapters = yu.recompute_chapters(topic, vid, meta["description"], meta["chapter_spec"])
    problems = yu.validate(meta)
    thumb = yu.find_thumbnail(topic, vid, yu.paired_thumbnail(topic, vid))
    log("SHEET", video=vid, title=meta["title"][:60], title_chars=len(meta["title"]), desc_chars=len(meta["description"]),
        tags=len(meta["tags"]), chapters=len(chapters or []), synthetic="예" if meta["synthetic"] else "아니요",
        thumbnail=thumb.name if thumb else "없음", problems=";".join(problems) or "-")
    return problems


def main(argv=None):
    ap = argparse.ArgumentParser(description="PC 업로더: GitHub 설정 + Drive 원본 → 유튜브 비공개 업로드 + 예약 공개")
    ap.add_argument("--topic", default="economic")
    ap.add_argument("--ids", default=None, help="이 영상만 (쉼표로)")
    ap.add_argument("--delay", default="1h", help="예약 공개 = 실행 시각 + 이 시간 (기본 1h, 5분 이상)")
    ap.add_argument("--at", default=None, help="첫 영상 공개 시각 (한국 시간, 예: '2026-10-16 18:00') — 주면 --delay 대신")
    ap.add_argument("--gap", default="0m", help="영상이 여러 개일 때 공개 간격 (기본 0 = 같은 시각, 예: 24h)")
    ap.add_argument("--max", type=int, default=4, help="이번에 올릴 최대 영상 수 (기본 4 — 하루 할당량)")
    ap.add_argument("--dry-run", action="store_true", help="올리지 않고 확인만")
    ap.add_argument("--keep-video", action="store_true", help="Drive 에서 받은 영상을 올린 뒤에도 남김")
    ap.add_argument("--repo", default=os.environ.get("GITHUB_REPO", REPO))
    ap.add_argument("--branch", default=BRANCH)
    a = ap.parse_args(argv)
    keys = load_env(ROOT / ".env", ROOT / a.topic / ".env")
    t0 = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)
    log("START", tool=f"pc_upload.py {VERSION}", topic=a.topic, dry_run=a.dry_run, delay=a.delay, at=a.at or "-", gap=a.gap,
        max=a.max, env_keys=",".join(sorted(set(keys))) or "-", note="연구·교육용 — 투자·세무·보험 상담 아님")
    gh = GitHub(a.repo, a.branch, os.environ.get("GITHUB_TOKEN", "").strip())
    ids = {x.strip() for x in a.ids.split(",")} if a.ids else None
    ready, skipped = find_candidates(gh, a.topic, ids)
    for vid, why in skipped:
        log("PLAN", video=vid, action="skip", why=why)
    first = parse_at(a.at) if a.at else t0 + parse_span(a.delay)
    gap = parse_span(a.gap)
    if first < t0 + dt.timedelta(minutes=10):
        raise SystemExit(f"[START] ❌ 첫 공개 시각 {first.astimezone(KST):%Y-%m-%d %H:%M} 이 지금보다 10분 이상 뒤가 아님")
    todo = ready[: a.max]
    for vid, _ in ready[a.max:]:
        log("PLAN", video=vid, action="later", why=f"--max {a.max} 넘음 — 다음 실행에")
    if not todo:
        log("DONE", uploaded=0, note="올릴 영상 없음 — 모두 올렸거나 업로드 시트가 없음")
        return 0
    if not a.dry_run:
        missing = [k for k in KEYS if not os.environ.get(k, "").strip()]
        if missing:
            raise SystemExit(f"[AUTH] ❌ .env 에 없음: {', '.join(missing)} → run_uploader.ps1 -Auth (또는 guides/upload_guide.md 11번)")
        yu.check_auth()
    if not gh.token and not a.dry_run:
        log("PUSH", note="GITHUB_TOKEN 없음 → youtube.json 은 이 PC 에만 (다른 PC·Claude 는 올린 줄 모름)")
    token_cache = {}

    def token_fn():
        if "t" not in token_cache:
            token_cache["t"] = yu.access_token()
        return token_cache["t"]

    results, stopped = [], False
    for i, (vid, listing) in enumerate(todo):
        when = first + gap * i
        when_z, when_kst = when.strftime("%Y-%m-%dT%H:%M:%SZ"), when.astimezone(KST).strftime("%Y-%m-%d %H:%M")
        if stopped:
            results.append((vid, "not_run", "-", when_kst))
            continue
        log("VIDEO", video=vid, publish_at_kst=when_kst)
        try:
            fetch_settings(gh, a.topic, vid, listing)
            src, path, note = locate_video(a.topic, vid, a.dry_run, token_fn)
            log("VIDEO", video=vid, source=src, note=note)
            if src == "missing":
                results.append((vid, "no_video", "-", when_kst))
                continue
            check_md5(a.topic, vid, path)
            if a.dry_run:
                problems = check_sheet(a.topic, vid)
                results.append((vid, f"dry-run ({src}{', 시트 문제 ' + str(len(problems)) if problems else ''})", "-", when_kst))
                continue
            res = yu.run(a.topic, vid, video=str(path), publish_at=when_z)
        except SystemExit as e:
            log("VIDEO", video=vid, ok=False, error=str(e)[:240])
            results.append((vid, "failed", "-", when_kst))
            continue
        except Exception as e:
            msg = str(e)
            log("VIDEO", video=vid, ok=False, error=msg[:240])
            results.append((vid, "failed", "-", when_kst))
            if any(w in msg for w in STOP_WORDS):
                stopped = True
                log("STOP", reason="유튜브 할당량 초과 — 남은 영상은 내일(한국 오후 4~5시 뒤) 다시 실행")
            continue
        state = ROOT / a.topic / "source" / vid / "youtube.json"
        pushed = gh.put_new(f"{a.topic}/source/{vid}/youtube.json", state.read_bytes(),
                            f"유튜브 예약 업로드: {vid} (공개 {when_kst} KST, PC pc_upload.py {VERSION})") if state.is_file() else "failed:youtube.json 없음"
        log("PUSH", video=vid, result=pushed)
        if src == "drive" and path and not a.keep_video:
            Path(path).unlink(missing_ok=True)
            log("CLEAN", video=vid, removed=str(Path(path).relative_to(ROOT)), note="Drive 원본은 그대로")
        results.append((vid, "uploaded" + ("" if pushed in ("created", "exists") else f" (GitHub 기록 실패: {pushed[7:60]})"),
                        (res or {}).get("url", "-"), when_kst))
    print("\n| 영상 | 결과 | 유튜브 | 공개 (한국 시간) |\n|---|---|---|---|")
    for vid, st, url, when in results:
        print(f"| {vid} | {st} | {url} | {when} |")
    up = sum(1 for r in results if r[1].startswith("uploaded"))
    bad = [r for r in results if r[1] in ("failed", "not_run", "no_video")]
    log("DONE", uploaded=up, failed=sum(1 for r in results if r[1] == "failed"), no_video=sum(1 for r in results if r[1] == "no_video"),
        not_run=sum(1 for r in results if r[1] == "not_run"), next="예약 시각 전에 스튜디오에서 영상·자막·썸네일 확인" if up else "-")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
