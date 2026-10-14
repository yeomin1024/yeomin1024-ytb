#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-14 — 신규: 분석기 웹 화면 (사용자 지시: "이거 분석기 웹 ui 형식으로 만들어 실행하면 바로 웹 ui가 나와서 env, 검색어
#          수정할 수 있게하고 탐색 버튼 누르면 탐색 대상 영상 목록이 나오지만 체크 표시만 해놓고 내가 승인 버튼을 눌러야 관련 자료를 받아서
#          분석하는걸로 해 그리고 내가 영상 url이나 채널을 추가하면 탐색 대상에 추가하도록 하고(채널을 추가하면 그 채널에 올려진 영상 다
#          탐색하는거야) 목록은 최근에 업로드 된 순으로 하고 1주 전, 2주 전, 3주 전 1주씩 늘리면서 분석 결과 내보도록 해"):
#          ① 실행하면 브라우저에 화면이 뜸 (이 PC 안에서만 — 127.0.0.1, 요청마다 무작위 열쇠 확인)
#          ② 키(.env 의 YOUTUBE_API_KEY·GITHUB_TOKEN — 끝 4자리만 보임)·검색어(<주제>/keywords.txt, GitHub 에도 저장 가능) 고치기
#          ③ 직접 추가: 영상 주소 → 그 영상, 채널 주소·@이름 → 그 채널에 올라온 영상 전부 (<주제>/targets.json)
#          ④ [탐색] → 검색어(최근 N주·조회수 순·4~20분·20분 넘음) + 추가한 채널·영상 → 목록 (최근 업로드 순). 추천(성공 사례·조회수 상위·
#             추가한 것)은 체크만 해 둠 — 자료는 아직 안 받음
#          ⑤ [승인] → 체크한 영상만 설명·자막·썸네일·댓글 전부를 받고(<주제>/result/outliers/W_<영상ID>/) 주별 분석
#             (tools/weekly_analysis.py — 최근 1주·2주·3주 … 한 주씩 넓힘) → 자막을 못 받은 영상은 음성인식 대기열 → 다시 분석 → GitHub
r"""
사용법 (PC 실행 폴더 — run_analyzer.ps1 이 기본으로 띄움):
  python tools/web_ui.py                    # economic (설정 파일이 있는 주제 폴더가 여럿이면 화면에서 고름)
  python tools/web_ui.py economic --port 8765 --no-browser
  옵션: --port 8765 (쓰는 중이면 다음 번호) · --no-browser (주소만 보여 줌) · --no-sync (GitHub 에서 설정·검색어를 받지 않음)
할당량: 탐색 = 검색어 1개마다 검색 2번(200단위, 7일 캐시) + 채널 영상 목록 50개에 1단위 + 영상 정보 50개에 1단위.
        승인 = 영상마다 댓글 100개에 1단위 (+ 답글). 오늘 쓴 양은 .yt_work/quota_<주제>.json (자동 실행과 같은 장부).
로그: [STAGE] [시각] key=value — 화면의 '진행' 칸과 .yt_work/web_ui.log
비밀값(키·토큰)은 화면·로그에 끝 4자리만. ※ 연구·교육용 분석 도구. 투자 권유가 아니다.
"""
import argparse
import base64
import collections
import hashlib
import json
import logging
import os
import re
import secrets
import subprocess
import sys
import threading
import time
import types
import urllib.error
import urllib.parse
import urllib.request
import webbrowser
from datetime import datetime, timedelta, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import pc_analysis as pc                 # noqa: E402  할당량 장부·키 찾기·GitHub 동기화·패키지 준비

ROOT = pc.ROOT
VERSION = "v1.0"
LOG = logging.getLogger("web")
KST = timezone(timedelta(hours=9))
TOKEN = secrets.token_urlsafe(18)        # 화면이 요청마다 보내는 열쇠 (다른 사이트가 이 PC 의 화면을 조작하지 못하게)
MIN_SEC = 240                            # 롱폼 기준 (4분) — 그보다 짧으면 '짧은 영상'
POPULAR_N = 20                           # 검색 결과 중 조회수 상위 몇 개를 추천(체크)할지
orr = None                               # tools/outlier_research.py (패키지 준비 뒤 불러옴)
wa = None                                # tools/weekly_analysis.py
STATE = {"topic": None, "topics": [], "port": None}
JOB = {"name": None, "status": "idle", "step": "", "done": 0, "total": 0, "started": None, "finished": None, "error": None,
       "result": None, "cancel": False, "log": collections.deque(maxlen=500), "proc": None}
JOB_LOCK = threading.Lock()


def log(stage, level=logging.INFO, **kv):
    LOG.log(level, "[%s] [%s] %s", stage, datetime.now().isoformat(timespec="seconds"),
            " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) and ' ' in v else v}" for k, v in kv.items()))


class _JobLogHandler(logging.Handler):
    """도구들의 로그 줄을 화면의 '진행' 칸으로."""

    def emit(self, record):
        try:
            JOB["log"].append(self.format(record))
        except Exception:
            pass


class UserError(Exception):
    """사용자에게 그대로 보여 줄 오류 (키 없음 등)."""


class Cancelled(Exception):
    pass


# ---------------------------------------------------------------- 경로·파일
def topic_dir(t):
    return ROOT / t


def out_dir(t):
    return ROOT / t / "result" / "outliers"


def web_dir(t):
    d = ROOT / t / "result" / "web"           # 탐색 목록 등 PC 에만 (GitHub 에 올리지 않음)
    d.mkdir(parents=True, exist_ok=True)
    return d


def _read_json(p, default):
    try:
        return json.loads(Path(p).read_text("utf-8"))
    except (OSError, ValueError):
        return default


def _write_json(p, data):
    p = Path(p)
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_name(p.name + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=1), "utf-8")
    os.replace(tmp, p)


def find_topics():
    return sorted(p.parent.name for p in ROOT.glob("*/analyzer_config.toml") if not p.parent.name.startswith("."))


def topic_name(t):
    try:
        flat = {}
        for k, v in pc._toml().loads((ROOT / t / "analyzer_config.toml").read_text("utf-8")).items():
            flat.update(v if isinstance(v, dict) and k != "KEYWORD_GROUPS" else {k: v})
        return str(flat.get("TOPIC") or t)
    except Exception:
        return t


# ---------------------------------------------------------------- 키 (.env)
ENV_NAMES = ("YOUTUBE_API_KEY", "GITHUB_TOKEN")


def mask(v):
    return f"…{v[-4:]} ({len(v)}자)" if v else ""


def env_view(t):
    out = {}
    for n in ENV_NAMES:
        v, src = pc.find_secret(n, t)
        out[n] = {"set": bool(v), "tail": mask(v), "source": src if v else "-"}
    return out


def set_env_value(path, name, value):
    """.env 의 name= 줄을 바꾸거나 더함 (다른 줄·메모는 그대로). 값은 로그에 쓰지 않음."""
    path = Path(path)
    lines = path.read_text("utf-8-sig").splitlines() if path.is_file() else []
    rx = re.compile(rf"^[ \t]*{name}[ \t]*=")
    for i, line in enumerate(lines):
        if rx.match(line):
            lines[i] = f"{name}={value}"
            break
    else:
        lines.append(f"{name}={value}")
    path.write_text("\n".join(lines) + "\n", "utf-8")


# ---------------------------------------------------------------- 검색어·직접 추가
def keywords_path(t):
    return ROOT / t / pc.KEYWORD_LIST_FILE


def targets_path(t):
    return ROOT / t / "targets.json"


def load_targets(t):
    d = _read_json(targets_path(t), {})
    return {"channels": list(d.get("channels") or []), "videos": list(d.get("videos") or [])}


def github_put(t, rel, data, message):
    """GitHub 에 파일 하나 저장 (contents API — 토큰 필요). → (ok, 설명)."""
    token = pc.find_secret("GITHUB_TOKEN", t)[0]
    if not token:
        return False, "GITHUB_TOKEN 없음 — PC 에만 저장"
    repo, branch = pc.repo_of(t)
    url = f"https://api.github.com/repos/{repo}/contents/{urllib.parse.quote(rel)}"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
    sha = None
    try:
        with urllib.request.urlopen(urllib.request.Request(f"{url}?ref={urllib.parse.quote(branch)}", headers=headers), timeout=30) as r:
            sha = json.loads(r.read().decode("utf-8")).get("sha")
    except urllib.error.HTTPError as e:
        if e.code != 404:
            return False, f"GitHub 읽기 실패 HTTP {e.code}"
    except Exception as e:
        return False, f"GitHub 연결 실패 ({type(e).__name__})"
    body = {"message": message, "content": base64.b64encode(data).decode("ascii"), "branch": branch}
    if sha:
        body["sha"] = sha
    req = urllib.request.Request(url, data=json.dumps(body).encode("utf-8"), headers={**headers, "Content-Type": "application/json"}, method="PUT")
    try:
        with urllib.request.urlopen(req, timeout=30):
            pass
    except urllib.error.HTTPError as e:
        return False, f"GitHub 저장 실패 HTTP {e.code}" + (" — 토큰의 Contents 권한이 Read and write 인지 확인" if e.code in (403, 404) else "")
    except Exception as e:
        return False, f"GitHub 연결 실패 ({type(e).__name__})"
    sync_p = ROOT / ".yt_work" / "config_sync.json"            # 자동 실행의 동기화가 'GitHub 과 같음'으로 보게
    st = _read_json(sync_p, {})
    st[rel] = hashlib.sha256(data).hexdigest()
    _write_json(sync_p, st)
    return True, f"GitHub 에도 저장 ({repo}/{rel})"


def make_api(t):
    key, src = orr.load_api_key(t)
    if not key:
        raise UserError("YouTube API 키가 없습니다 — 화면 위 '1. 키 설정'에서 넣고 저장하세요")
    ledger = pc.Ledger(t)
    left = pc.DAILY_LIMIT - pc.DAILY_MARGIN - ledger.used()
    if left < 1:
        raise UserError(f"오늘 할당량을 다 썼습니다 ({ledger.used():,}단위) — 한국 시간 오후 4~5시(태평양 자정) 뒤에 다시")
    return orr.Api(key, left), ledger, src


def add_target(t, text):
    kind, val = orr.parse_target(text)
    if not kind:
        raise UserError(val)
    tg = load_targets(t)
    now = datetime.now(KST).isoformat(timespec="minutes")
    if kind == "video":
        if any(v["id"] == val for v in tg["videos"]):
            return {"kind": "video", "id": val, "note": "이미 있음"}
        entry = {"id": val, "title": "", "added": now}
        try:
            api, ledger, _ = make_api(t)
        except UserError as e:                       # 키가 없거나 할당량이 없어도 추가는 됨 — 제목은 탐색 때
            api, entry["note"] = None, f"제목은 탐색 때 ({e})"
        if api:
            try:
                items = api.videos([val])
            except Exception as e:
                items, entry["note"] = None, f"제목은 탐색 때 ({type(e).__name__})"
            finally:
                ledger.add(api.used, "web_add")
            if items == []:
                raise UserError(f"영상을 찾지 못했습니다 (지워졌거나 비공개): {val}")
            if items:
                entry["title"] = items[0]["snippet"].get("title", "")
                entry["channel"] = items[0]["snippet"].get("channelTitle", "")
        tg["videos"].append(entry)
        _write_json(targets_path(t), tg)
        log("TARGET", kind="video", id=val, title=entry.get("title", ""))
        return {"kind": "video", **entry}
    api, ledger, _ = make_api(t)
    ch = orr.resolve_channel(api, kind, val)
    ledger.add(api.used, "web_add")
    if not ch:
        raise UserError(f"채널을 찾지 못했습니다: {val}")
    if any(c["id"] == ch["id"] for c in tg["channels"]):
        return {"kind": "channel", **ch, "note": "이미 있음"}
    ch["added"] = now
    tg["channels"].append(ch)
    _write_json(targets_path(t), tg)
    log("TARGET", kind="channel", id=ch["id"], title=ch["title"], videos=ch["videos"])
    return {"kind": "channel", **ch}


def remove_target(t, kind, tid):
    tg = load_targets(t)
    key = "channels" if kind == "channel" else "videos"
    tg[key] = [x for x in tg[key] if x["id"] != tid]
    _write_json(targets_path(t), tg)
    return tg


# ---------------------------------------------------------------- 작업 (한 번에 하나, 뒤에서)
def job_view():
    return {k: (list(v)[-200:] if k == "log" else v) for k, v in JOB.items() if k not in ("proc", "cancel")}


def start_job(name, fn, *args):
    with JOB_LOCK:
        if JOB["status"] == "running":
            return False, f"'{JOB['name']}' 작업이 아직 도는 중입니다 — 끝난 뒤 다시"
        JOB.update(name=name, status="running", step="시작", done=0, total=0, started=datetime.now(KST).isoformat(timespec="seconds"),
                   finished=None, error=None, result=None, cancel=False, proc=None)
        JOB["log"].clear()

    def runner():
        try:
            JOB["result"] = fn(*args)
            JOB["status"] = "done"
        except Cancelled:
            JOB["status"] = "cancelled"
            log("JOB", logging.WARNING, name=name, note="사용자가 멈춤 — 받은 것은 캐시·폴더에 남음")
        except UserError as e:
            JOB.update(status="error", error=str(e))
            log("JOB", logging.WARNING, name=name, error=str(e))
        except Exception as e:
            JOB.update(status="error", error=f"{type(e).__name__}: {e}"[:300])
            LOG.exception("[JOB] %s 실패", name)
        finally:
            JOB["finished"] = datetime.now(KST).isoformat(timespec="seconds")
            JOB["proc"] = None
    threading.Thread(target=runner, daemon=True, name=f"job-{name}").start()
    return True, "시작"


def step(text, done=None, total=None):
    if JOB["cancel"]:
        raise Cancelled()
    JOB["step"] = text
    if done is not None:
        JOB["done"] = done
    if total is not None:
        JOB["total"] = total


def run_subprocess(cmd, label):
    """도구를 따로 돌리고 출력 줄을 '진행' 칸으로 (멈춤을 누르면 끝냄). → 종료 코드."""
    env = {**os.environ, "PYTHONIOENCODING": "utf-8", "PYTHONUTF8": "1"}
    log("JOB", step=label, cmd=" ".join(str(c) for c in cmd[1:]))
    p = subprocess.Popen(cmd, cwd=ROOT, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    JOB["proc"] = p
    for raw in p.stdout:
        JOB["log"].append(raw.decode("utf-8", errors="replace").rstrip())
        if JOB["cancel"]:
            p.terminate()
    code = p.wait()
    JOB["proc"] = None
    if JOB["cancel"]:
        raise Cancelled()
    return code


# ---------------------------------------------------------------- 탐색
def estimate(t, weeks, use_keywords):
    """탐색하면 쓸 검색 할당량 (캐시는 0). → {searches, cached, units, channels}."""
    cache = out_dir(t) / ".cache"
    kws = orr.load_keywords(t, 0)[0] if use_keywords else []
    total = cached = 0
    for _, q in kws:
        for dur in ("medium", "long"):
            total += 1
            cached += orr.search_is_cached(cache, q, dur, weeks * 7)
    tg = load_targets(t)
    ch_units = sum(max(1, -(-int(c.get("videos") or 50) // 50)) * 2 for c in tg["channels"])   # 목록 + 영상 정보
    return {"keywords": len(kws), "searches": total, "cached": cached, "units": (total - cached) * 100 + ch_units + 20,
            "channels": len(tg["channels"]), "videos": len(tg["videos"])}


def _is_success(r):
    return r["subs"] is not None and r["subs"] <= 50000 and r["views"] >= 10000 and (r["ratio"] or 0) >= 3


def preselect(rows):
    """추천 = 체크만 해 둠: 직접 추가한 영상 · 추가한 채널의 최근 N주 롱폼 · 검색 결과 중 성공 사례(작은 채널)·조회수 상위(주제 관련, 최근 N주 롱폼)."""
    reasons = {}
    searched = [r for r in rows if r["in_window"] and not r["short"] and r["relevant"] and any(s.startswith("검색:") for s in r["sources"])]
    searched_ids = {r["id"] for r in searched}
    for r in sorted(searched, key=lambda r: -r["views"])[:POPULAR_N]:
        reasons[r["id"]] = "조회수 상위"
    for r in rows:
        if "주소" in r["sources"]:
            reasons[r["id"]] = "추가한 영상"
        elif any(s.startswith("채널:") for s in r["sources"]) and r["in_window"] and not r["short"]:
            reasons[r["id"]] = "추가한 채널"
        elif r["id"] in searched_ids and _is_success(r):
            reasons[r["id"]] = "성공 사례"
    return reasons


def job_explore(t, weeks, use_keywords):
    api, ledger, src = make_api(t)
    out = out_dir(t)
    cache = out / ".cache"
    cache.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc)
    days = weeks * 7
    since = (now - timedelta(days=days)).strftime("%Y-%m-%dT00:00:00Z")
    kws, exclude, _, _, rel = orr.load_keywords(t, 0)
    kws = kws if use_keywords else []
    tg = load_targets(t)
    if not kws and not tg["channels"] and not tg["videos"]:
        raise UserError("탐색할 것이 없습니다 — 검색어를 넣거나 영상·채널을 추가하세요")
    found, pending = {}, []
    total = len(kws) * 2 + len(tg["channels"]) + 2
    n = 0
    log("EXPLORE", topic=t, weeks=weeks, keywords=len(kws), channels=len(tg["channels"]), videos=len(tg["videos"]), key_source=src,
        quota_left=api.quota)
    try:
        for g, q in kws:
            for dur in ("medium", "long"):
                n += 1
                step(f"검색 {q} ({'4~20분' if dur == 'medium' else '20분 넘음'})", n, total)
                try:
                    ids, hit = orr.cached_search(api, cache, q, since, dur, days, orr.SEARCH_TTL_HOURS, False)
                except orr.QuotaStop:
                    pending.append(f"{q} ({dur})")
                    continue
                for vid in ids:
                    found.setdefault(vid, []).append(f"검색:{q}")
                log("SEARCH", query=q, dur=dur, results=len(ids), cached=hit, quota_used=api.used)
        for ch in tg["channels"]:
            n += 1
            step(f"채널 {ch.get('title') or ch['id']} 영상 목록", n, total)
            try:
                ids = orr.channel_uploads(api, cache, ch)
            except orr.QuotaStop:
                pending.append(f"채널 {ch.get('title')}")
                continue
            for vid in ids:
                found.setdefault(vid, []).append(f"채널:{ch.get('title') or ch['id']}")
        for v in tg["videos"]:
            found.setdefault(v["id"], []).append("주소")
        step(f"영상 {len(found):,}개 정보·구독자 수", n + 1, total)
        state = orr.new_state()
        infos = orr.fetch_video_infos(api, cache, list(found), state)
        subs = orr.fetch_channel_subs(api, cache, {i["channel_id"] for i in infos}, state)
    finally:
        ledger.add(api.used, "web_explore")
    for i in infos:
        i["subs"] = (subs.get(i["channel_id"]) or {}).get("subs")
    info_by_id = {i["id"]: i for i in infos}
    rows = []
    for r in orr.build_rows(infos, found, now):
        srcs = list(dict.fromkeys(found.get(r["id"], [])))
        if "주소" not in srcs and any(w in (r["title"] or "") for w in exclude):
            continue
        r.update(sources=srcs, published_at=str(info_by_id[r["id"]].get("published") or ""),
                 relevant=orr.relevant(info_by_id[r["id"]], rel), short=r["minutes"] * 60 < MIN_SEC,
                 in_window=r["age_days"] is not None and r["age_days"] <= days,
                 downloaded=(out / f"W_{r['id']}" / "metadata.json").is_file())
        r["success"] = _is_success(r)
        rows.append(r)
    reasons = preselect(rows)
    for r in rows:
        r["reason"] = reasons.get(r["id"], "")
    rows.sort(key=lambda r: r["published_at"], reverse=True)          # 최근 업로드 순
    data = {"topic": t, "generated": datetime.now(KST).isoformat(timespec="seconds"), "weeks": weeks, "use_keywords": use_keywords,
            "rows": rows, "checked": [r["id"] for r in rows if r["reason"]], "pending": pending, "quota_used": api.used}
    _write_json(web_dir(t) / "explore.json", data)
    log("EXPLORE", topic=t, videos=len(rows), checked=len(data["checked"]), pending=len(pending), quota_used=api.used,
        note="체크만 해 둠 — [승인]을 눌러야 자료를 받음")
    step("끝", total, total)
    return {"videos": len(rows), "checked": len(data["checked"]), "pending": pending, "quota_used": api.used}


# ---------------------------------------------------------------- 승인 → 자료 받기 → 주별 분석 → 음성인식 → 다시 분석 → GitHub
def job_approve(t, ids, auto_whisper=True):
    ex = _read_json(web_dir(t) / "explore.json", {})
    by_id = {r["id"]: r for r in ex.get("rows") or []}
    ids = [i for i in dict.fromkeys(ids) if i in by_id]
    if not ids:
        raise UserError("승인할 영상이 없습니다 — 목록에서 체크하세요 (탐색을 먼저)")
    api, ledger, _ = make_api(t)
    out = out_dir(t)
    cache = out / ".cache"
    a = types.SimpleNamespace(refresh=False, no_transcript=False, offline=False, comments=0, replies=True)
    state = orr.new_state()
    got = []
    log("APPROVE", topic=t, videos=len(ids), note="설명·자막·썸네일·댓글 전부 받음")
    try:
        for n, vid in enumerate(ids, 1):
            step(f"자료 받기 {n}/{len(ids)} — {by_id[vid]['title'][:40]}", n - 1, len(ids))
            info = _read_json(cache / f"{vid}.json", None)
            if not info:
                log("APPROVE", logging.WARNING, id=vid, note="영상 정보 캐시 없음 — 탐색을 다시")
                continue
            d = out / f"W_{vid}"
            row = {k: v for k, v in by_id[vid].items() if k not in ("sources", "reason", "downloaded", "in_window", "relevant", "short", "success")}
            row.update(rank=f"W{n}", set="web", folder=d.name, sources=by_id[vid]["sources"], url=f"https://www.youtube.com/watch?v={vid}")
            meta, cms = orr.deep_case(d, row, info, a, api, "web", {}, state)
            cms, cst = orr.comments_step(d, meta, a, api, "web", {}, state, full=True)
            n_rep = sum(1 for c in cms if c.get("parent"))
            meta.update(comments_fetched=len(cms), comments_top_level=len(cms) - n_rep, comments_replies=n_rep,
                        comments_by_creator=sum(1 for c in cms if c.get("creator")), comments_complete=cst["complete"],
                        comments_disabled=cst.get("disabled", False), approved=datetime.now(KST).isoformat(timespec="minutes"))
            (d / "metadata.json").write_text(json.dumps(meta, ensure_ascii=False, indent=1), "utf-8")
            got.append(meta)
            log("APPROVE", n=f"{n}/{len(ids)}", id=vid, transcript=meta["transcript_status"] if meta["transcript_status"] != "ok" else meta["transcript_lang"],
                comments=len(cms), comments_complete=cst["complete"], quota_used=api.used)
    finally:
        ledger.add(api.used, "web_approve")
    appr = _read_json(web_dir(t) / "approved.json", {"approved": []})
    appr["approved"] = list(dict.fromkeys(appr["approved"] + [m["id"] for m in got]))
    _write_json(web_dir(t) / "approved.json", appr)
    step("주별 분석", len(ids), len(ids))
    rep = wa.run(t)
    missing = [m["id"] for m in got if m["transcript_status"] != "ok"]
    res = {"videos": len(got), "transcripts_ok": len(got) - len(missing), "whisper_needed": len(missing), "quota_used": api.used,
           "pending_comments": len(state["pending_comments"]), "windows": len(rep["windows"])}
    has_token = bool(pc.find_secret("GITHUB_TOKEN", t)[0])
    if missing and auto_whisper:
        step(f"음성인식 {len(missing)}개 (자막을 못 받은 영상 — 하나씩, 오래 걸림)", 0, len(missing))
        code = run_subprocess([sys.executable, "youtube_topic_analyzer.py", "--config", f"{t}/analyzer_config.toml", "--whisper-queue"]
                              + ([] if has_token else ["--no-push"]), "음성인식")
        res["whisper_exit"] = code
        step("주별 분석 (음성인식 대본 넣어서)")
        rep = wa.run(t)
        res["transcripts_ok"] = sum(1 for c in wa.load_cases(out) if c["snips"] and c["meta"]["id"] in {m["id"] for m in got})
    if has_token:
        step("GitHub 에 올리기")
        res["push_exit"] = run_subprocess([sys.executable, "youtube_topic_analyzer.py", "--config", f"{t}/analyzer_config.toml",
                                           "--push-only"], "GitHub")
    log("APPROVE", topic=t, **{k: v for k, v in res.items()})
    step("끝")
    return res


def job_analyze(t):
    step("주별 분석")
    rep = wa.run(t)
    return {"windows": len(rep["windows"]), "cases": rep["cases"]}


def job_whisper(t):
    step("음성인식 대기열")
    has_token = bool(pc.find_secret("GITHUB_TOKEN", t)[0])
    code = run_subprocess([sys.executable, "youtube_topic_analyzer.py", "--config", f"{t}/analyzer_config.toml", "--whisper-queue"]
                          + ([] if has_token else ["--no-push"]), "음성인식")
    step("주별 분석")
    wa.run(t)
    return {"exit": code}


# ---------------------------------------------------------------- 화면 상태
def state_view(t):
    ex = _read_json(web_dir(t) / "explore.json", {})
    kp = keywords_path(t)
    text = kp.read_text("utf-8-sig") if kp.is_file() else ""
    until = orr.caption_blocked()
    ledger = pc.Ledger(t)
    return {"version": VERSION, "topic": t, "name": topic_name(t), "topics": STATE["topics"], "env": env_view(t),
            "keywords_text": text, "keywords_count": len(pc.read_keyword_list(kp) or []), "targets": load_targets(t),
            "explore": {"generated": ex.get("generated"), "weeks": ex.get("weeks"), "videos": len(ex.get("rows") or []),
                        "checked": len(ex.get("checked") or []), "pending": ex.get("pending") or []},
            "quota": {"used": ledger.used(), "budget": pc.DAILY_LIMIT - pc.DAILY_MARGIN, "day": pc.pacific_day(datetime.now(timezone.utc))},
            "caption_block": until.astimezone(KST).strftime("%m-%d %H:%M") if until else None,
            "approved": len(_read_json(web_dir(t) / "approved.json", {"approved": []})["approved"]),
            "job": job_view()}


PAGE = None      # 아래 HTML (파일 끝)


class Handler(BaseHTTPRequestHandler):
    server_version = "AnalyzerUI/" + VERSION

    def log_message(self, fmt, *args):          # 접속 기록은 남기지 않음 (화면이 1초마다 묻기 때문)
        pass

    def _send(self, code, body, ctype="application/json; charset=utf-8"):
        data = body if isinstance(body, bytes) else json.dumps(body, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(data)

    def _host_ok(self):
        host = (self.headers.get("Host") or "").split(":")[0]
        return host in ("127.0.0.1", "localhost")

    def _authorized(self):
        return self._host_ok() and secrets.compare_digest(self.headers.get("X-Token") or "", TOKEN)

    def do_GET(self):
        if not self._host_ok():
            return self._send(403, {"error": "이 PC 에서만 열 수 있습니다"})
        u = urllib.parse.urlparse(self.path)
        if u.path in ("/", "/index.html"):
            return self._send(200, PAGE.replace("{{TOKEN}}", TOKEN).encode("utf-8"), "text/html; charset=utf-8")
        if u.path == "/favicon.ico":                         # 브라우저가 저절로 묻는 아이콘 — 없음 (403 오류로 보이지 않게)
            self.send_response(204)
            self.end_headers()
            return
        if not self._authorized():
            return self._send(403, {"error": "열쇠가 맞지 않음 — 화면을 새로 고침"})
        t = STATE["topic"]
        q = urllib.parse.parse_qs(u.query)
        try:
            if u.path == "/api/state":
                return self._send(200, state_view(t))
            if u.path == "/api/job":
                return self._send(200, job_view())
            if u.path == "/api/explore":
                ex = _read_json(web_dir(t) / "explore.json", {})
                return self._send(200, {"rows": ex.get("rows") or [], "checked": ex.get("checked") or [], "generated": ex.get("generated"),
                                        "weeks": ex.get("weeks")})
            if u.path == "/api/estimate":
                weeks = max(1, min(52, int((q.get("weeks") or ["8"])[0])))
                return self._send(200, estimate(t, weeks, (q.get("kw") or ["1"])[0] == "1"))
            if u.path == "/api/report":
                return self._send(200, _read_json(out_dir(t) / "weekly.json", {}))
        except UserError as e:
            return self._send(400, {"error": str(e)})
        except Exception as e:
            LOG.exception("GET %s", u.path)
            return self._send(500, {"error": f"{type(e).__name__}: {e}"[:300]})
        return self._send(404, {"error": "없는 주소"})

    def do_POST(self):
        if not self._authorized():
            return self._send(403, {"error": "열쇠가 맞지 않음 — 화면을 새로 고침"})
        n = int(self.headers.get("Content-Length") or 0)
        if n > 2_000_000:
            return self._send(413, {"error": "너무 큼"})
        try:
            body = json.loads(self.rfile.read(n).decode("utf-8") or "{}")
        except ValueError:
            return self._send(400, {"error": "JSON 이 아님"})
        t = STATE["topic"]
        path = urllib.parse.urlparse(self.path).path
        try:
            if path == "/api/topic":
                if body.get("topic") not in STATE["topics"]:
                    raise UserError("없는 주제 폴더")
                STATE["topic"] = body["topic"]
                return self._send(200, state_view(STATE["topic"]))
            if path == "/api/env":
                changed = []
                for name in ENV_NAMES:
                    v = str(body.get(name) or "").strip().strip('"').strip("'")
                    if not v:
                        continue
                    if re.search(r"\s", v):
                        raise UserError(f"{name}: 값에 띄어쓰기·줄바꿈이 있으면 안 됩니다")
                    src = pc.find_secret(name, t)[1]             # 지금 쓰는 파일에 저장 (주제 .env 가 먼저 읽히므로)
                    set_env_value(ROOT / t / ".env" if src == f"{t}/.env" else ROOT / ".env", name, v)
                    os.environ.pop(name, None)                   # 예전 환경 변수보다 .env 를 쓰게
                    changed.append(name)
                log("ENV", changed=",".join(changed) or "-", note="값은 로그에 쓰지 않음")
                return self._send(200, {"changed": changed, "env": env_view(t)})
            if path == "/api/keywords":
                text = str(body.get("text") or "")
                data = (text.replace("\r\n", "\n").rstrip("\n") + "\n").encode("utf-8")
                kp = keywords_path(t)
                kp.write_bytes(data)
                kws = pc.read_keyword_list(kp) or []
                msg = f"PC 에 저장 ({len(kws)}개)"
                if body.get("push"):
                    ok, note = github_put(t, f"{t}/{pc.KEYWORD_LIST_FILE}", data, f"[{topic_name(t)}] 검색어 고침 (웹 화면, {len(kws)}개)")
                    msg += " · " + note
                log("KEYWORDS", topic=t, keywords=len(kws), note=msg)
                return self._send(200, {"count": len(kws), "message": msg})
            if path == "/api/targets/add":
                return self._send(200, {"added": add_target(t, body.get("text")), "targets": load_targets(t)})
            if path == "/api/targets/remove":
                return self._send(200, {"targets": remove_target(t, body.get("kind"), body.get("id"))})
            if path == "/api/checked":
                ex = _read_json(web_dir(t) / "explore.json", {})
                if ex:
                    ok_ids = {r["id"] for r in ex.get("rows") or []}
                    ex["checked"] = [i for i in body.get("ids") or [] if i in ok_ids]
                    _write_json(web_dir(t) / "explore.json", ex)
                return self._send(200, {"checked": len(ex.get("checked") or [])})
            if path == "/api/explore":
                weeks = max(1, min(52, int(body.get("weeks") or 8)))
                ok, msg = start_job("탐색", job_explore, t, weeks, bool(body.get("keywords", True)))
                return self._send(200 if ok else 409, {"ok": ok, "message": msg})
            if path == "/api/approve":
                ok, msg = start_job("승인 — 자료 받고 분석", job_approve, t, list(body.get("ids") or []), bool(body.get("whisper", True)))
                return self._send(200 if ok else 409, {"ok": ok, "message": msg})
            if path == "/api/analyze":
                ok, msg = start_job("주별 분석", job_analyze, t)
                return self._send(200 if ok else 409, {"ok": ok, "message": msg})
            if path == "/api/whisper":
                ok, msg = start_job("음성인식", job_whisper, t)
                return self._send(200 if ok else 409, {"ok": ok, "message": msg})
            if path == "/api/cancel":
                JOB["cancel"] = True
                p = JOB.get("proc")
                if p:
                    p.terminate()
                return self._send(200, {"ok": True})
        except UserError as e:
            return self._send(400, {"error": str(e)})
        except Exception as e:
            LOG.exception("POST %s", path)
            return self._send(500, {"error": f"{type(e).__name__}: {e}"[:300]})
        return self._send(404, {"error": "없는 주소"})


def serve(port, host="127.0.0.1"):
    for p in range(port, port + 20):
        try:
            return ThreadingHTTPServer((host, p), Handler), p
        except OSError:
            continue
    raise SystemExit(f"[START] ❌ {port}~{port + 19} 번 포트를 모두 쓰는 중 — --port 로 다른 번호")


def main(argv=None):
    global orr, wa
    ap = argparse.ArgumentParser(description="분석기 웹 화면 — 키·검색어 고치기, 탐색 → 체크 → 승인 → 자료 받기·주별 분석")
    ap.add_argument("topics", nargs="*", help="주제 폴더 (없으면 설정 파일이 있는 폴더 — economic 먼저)")
    ap.add_argument("--port", type=int, default=8765)
    ap.add_argument("--no-browser", action="store_true")
    ap.add_argument("--no-sync", action="store_true", help="GitHub 에서 설정·검색어를 받지 않음")
    ap.add_argument("--skip-install", action="store_true")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args(argv)
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass
    fmt = logging.Formatter("%(message)s")
    root_log = logging.getLogger()
    root_log.setLevel(getattr(logging, a.log_level))
    for h in (logging.StreamHandler(sys.stdout), _JobLogHandler()):
        h.setFormatter(fmt)
        root_log.addHandler(h)
    (ROOT / ".yt_work").mkdir(exist_ok=True)
    fh = logging.FileHandler(ROOT / ".yt_work" / "web_ui.log", encoding="utf-8")
    fh.setFormatter(fmt)
    root_log.addHandler(fh)
    topics = a.topics or find_topics()
    if not topics:
        raise SystemExit("[START] ❌ 주제 폴더(<폴더>/analyzer_config.toml)가 없음 — run_analyzer.ps1 로 받거나 폴더 이름 확인")
    if "economic" in topics:
        topics = ["economic"] + [x for x in topics if x != "economic"]
    STATE.update(topic=topics[0], topics=topics)
    if not a.skip_install and not pc.ensure_packages(False):
        raise SystemExit("[START] ❌ 패키지 설치 실패 — 위 오류 확인")
    import outlier_research as _orr
    import weekly_analysis as _wa
    orr, wa = _orr, _wa
    if not a.no_sync:
        for t in topics:
            try:
                pc.sync_from_github(t, code=False)
            except Exception as e:
                log("SYNC", logging.WARNING, topic=t, note="GitHub 에서 설정을 받지 못함 — PC 파일로", error=f"{type(e).__name__}"[:80])
    srv, port = serve(a.port)
    STATE["port"] = port
    url = f"http://127.0.0.1:{port}/"
    log("START", url=url, topics=",".join(topics), tool=f"web_ui.py {VERSION}",
        note="이 창을 닫으면 화면도 꺼집니다 (Ctrl+C 로 끝냄)")
    print(f"\n  ▶ 분석기 화면: {url}\n    (브라우저가 안 열리면 위 주소를 복사해 여세요. 끝내려면 이 창에서 Ctrl+C)\n", flush=True)
    if not a.no_browser:
        threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        log("DONE", note="화면을 끔")
    finally:
        srv.server_close()
    return 0


PAGE = r"""<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="t" content="{{TOKEN}}"><title>분석기</title>
<style>
:root{--bg:#f7f7f5;--card:#fff;--fg:#1d1d1f;--mut:#6b6b70;--line:#e3e3e0;--acc:#2563eb;--acc2:#1d4ed8;--ok:#15803d;--warn:#b45309;--bad:#b91c1c;--chip:#eef2ff;--row:#fafaf9}
@media (prefers-color-scheme:dark){:root{--bg:#111113;--card:#1a1a1d;--fg:#ececee;--mut:#a0a0a8;--line:#2c2c31;--acc:#5b8cff;--acc2:#7aa2ff;--ok:#4ade80;--warn:#fbbf24;--bad:#f87171;--chip:#1e2540;--row:#161618}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:14px/1.5 -apple-system,"Segoe UI","Malgun Gothic","Apple SD Gothic Neo",sans-serif}
header{position:sticky;top:0;z-index:5;background:var(--card);border-bottom:1px solid var(--line);padding:10px 16px;display:flex;gap:14px;align-items:center;flex-wrap:wrap}
header h1{font-size:17px;margin:0}header .pill{font-size:12px;color:var(--mut);background:var(--bg);border:1px solid var(--line);border-radius:99px;padding:2px 10px}
main{max-width:1280px;margin:0 auto;padding:16px;display:grid;gap:14px}main>*,.two>*{min-width:0}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px 16px}
.card h2{font-size:15px;margin:0 0 10px}.card h2 small{font-weight:400;color:var(--mut);margin-left:6px}
.row{display:flex;gap:8px;align-items:center;flex-wrap:wrap}.grow{flex:1;min-width:200px}
input[type=text],input[type=password],input[type=number],textarea,select{font:inherit;color:var(--fg);background:var(--bg);border:1px solid var(--line);border-radius:8px;padding:7px 10px}
textarea{width:100%;min-height:180px;font-family:ui-monospace,Consolas,monospace;font-size:13px}
button{font:inherit;border:1px solid var(--line);background:var(--bg);color:var(--fg);border-radius:8px;padding:7px 14px;cursor:pointer}
button.pri{background:var(--acc);border-color:var(--acc);color:#fff;font-weight:600}button.pri:hover{background:var(--acc2)}
button:disabled{opacity:.5;cursor:not-allowed}.mut{color:var(--mut)}.ok{color:var(--ok)}.warn{color:var(--warn)}.bad{color:var(--bad)}
.two{display:grid;grid-template-columns:1fr 1fr;gap:14px}@media (max-width:860px){.two{grid-template-columns:1fr}}
.chip{display:inline-flex;gap:6px;align-items:center;background:var(--chip);border-radius:99px;padding:3px 6px 3px 10px;margin:3px 4px 0 0;font-size:13px}
.chip button{padding:0 7px;border:0;background:transparent;color:var(--mut)}
.tablewrap{overflow:auto;max-height:620px;border:1px solid var(--line);border-radius:8px}
table{border-collapse:collapse;width:100%;font-size:13px}th,td{padding:6px 8px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top;white-space:nowrap}
th{position:sticky;top:0;background:var(--card);z-index:1;font-weight:600}td.t{white-space:normal;min-width:260px}tr.on{background:var(--row)}
td.n,th.n{text-align:right;font-variant-numeric:tabular-nums}a{color:var(--acc)}
.tag{font-size:11px;border-radius:6px;padding:1px 6px;background:var(--bg);border:1px solid var(--line);margin-right:3px}
.tag.s{border-color:var(--ok);color:var(--ok)}.tag.d{border-color:var(--acc);color:var(--acc)}
.bar{height:6px;background:var(--line);border-radius:9px;overflow:hidden}.bar i{display:block;height:100%;background:var(--acc);width:0}
pre{background:var(--bg);border:1px solid var(--line);border-radius:8px;padding:10px;max-height:260px;overflow:auto;font-size:12px;white-space:pre-wrap;margin:8px 0 0}
details{border:1px solid var(--line);border-radius:8px;padding:8px 12px;margin-top:8px}summary{cursor:pointer;font-weight:600}
.msg{min-height:20px;font-size:13px}.k{display:grid;grid-template-columns:150px 1fr;gap:8px;align-items:center;margin-bottom:8px}
@media (max-width:600px){.k{grid-template-columns:1fr}}
</style></head><body>
<header><h1 id="title">분석기</h1><select id="topic" title="주제 폴더"></select>
<span class="pill" id="quota">할당량 …</span><span class="pill" id="caption">자막 서버 …</span><span class="pill" id="ver"></span></header>
<main>
<div class="two">
 <section class="card"><h2>1. 키 설정 <small>.env — 끝 4자리만 보입니다</small></h2>
  <div class="k"><label for="ytkey">YouTube API 키</label><div><input type="password" id="ytkey" class="grow" style="width:100%" placeholder="바꿀 때만 붙여넣기" autocomplete="off"><div class="mut" id="ytkey_now"></div></div></div>
  <div class="k"><label for="ghtok">GitHub 토큰</label><div><input type="password" id="ghtok" style="width:100%" placeholder="바꿀 때만 붙여넣기" autocomplete="off"><div class="mut" id="ghtok_now"></div></div></div>
  <div class="row"><button class="pri" id="saveEnv">키 저장</button><span class="msg" id="envMsg"></span></div>
 </section>
 <section class="card"><h2>2. 검색어 <small>한 줄에 하나 · # 은 메모</small></h2>
  <textarea id="kw" spellcheck="false"></textarea>
  <div class="row" style="margin-top:8px"><button class="pri" id="saveKw">검색어 저장</button>
   <label><input type="checkbox" id="kwPush" checked> GitHub 에도 저장</label><span class="mut" id="kwCount"></span><span class="msg" id="kwMsg"></span></div>
 </section>
</div>
<section class="card"><h2>3. 직접 추가 <small>영상 주소 → 그 영상 · 채널 주소나 @이름 → 그 채널에 올라온 영상 전부</small></h2>
 <div class="row"><input type="text" id="tgIn" class="grow" placeholder="https://www.youtube.com/watch?v=…  또는  https://www.youtube.com/@채널이름"><button class="pri" id="tgAdd">추가</button><span class="msg" id="tgMsg"></span></div>
 <div id="tgList" style="margin-top:6px"></div>
</section>
<section class="card"><h2>4. 탐색 <small>목록만 만듭니다 — 자료는 승인한 영상만 받습니다</small></h2>
 <div class="row">최근 <input type="number" id="weeks" min="1" max="52" value="8" style="width:70px"> 주
  <label><input type="checkbox" id="useKw" checked> 검색어로도 찾기</label>
  <span class="mut" id="est"></span><button class="pri" id="explore">탐색</button></div>
</section>
<section class="card" id="listCard"><h2>5. 탐색 목록 <small id="listInfo">최근 업로드 순 · 추천은 체크해 둠</small></h2>
 <div class="row" style="margin-bottom:8px"><input type="text" id="flt" class="grow" placeholder="제목·채널 거르기">
  <label><input type="checkbox" id="fShort"> 짧은 영상(4분 미만)도</label><label><input type="checkbox" id="fRel" checked> 주제 관련만</label>
  <label><input type="checkbox" id="fChk"> 체크한 것만</label>
  <button id="chkAll">보이는 것 모두 체크</button><button id="chkNone">모두 해제</button><button id="chkRec">추천만</button></div>
 <div class="tablewrap"><table><thead><tr><th></th><th>업로드</th><th>제목</th><th>채널</th><th class="n">구독자</th><th class="n">조회수</th><th class="n">배수</th><th class="n">하루 조회수</th><th class="n">길이</th><th>추천 · 출처</th></tr></thead><tbody id="rows"><tr><td colspan="10" class="mut">탐색을 누르면 여기에 나옵니다</td></tr></tbody></table></div>
 <div class="row" style="margin-top:10px"><button class="pri" id="approve">승인 — 체크한 영상 자료 받고 분석</button><label><input type="checkbox" id="autoW" checked> 자막 없는 영상은 음성인식까지</label><span class="mut" id="chkInfo"></span></div>
</section>
<section class="card"><h2>진행 <small id="jobName"></small></h2>
 <div class="row"><span id="jobStep" class="grow">쉬는 중</span><button id="cancel" disabled>멈춤</button><button id="reanalyze">다시 분석</button><button id="whisper">음성인식 대기열</button></div>
 <div class="bar" style="margin-top:8px"><i id="jobBar"></i></div><pre id="jobLog"></pre>
</section>
<section class="card"><h2>6. 분석 결과 <small>최근 1주부터 한 주씩 넓힘 (누적) · weekly.md 로도 저장</small></h2><div id="report" class="mut">승인한 영상이 생기면 여기에 나옵니다</div></section>
</main>
<script>
const T=document.querySelector('meta[name=t]').content;let ROWS=[],CHECK=new Set(),REC=new Set(),busy=false,lastJob=null,waitDone=false;
const $=id=>document.getElementById(id);const esc=s=>String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const num=x=>x==null?'–':(typeof x==='number'?x.toLocaleString('ko-KR',{maximumFractionDigits:1}):x);
async function api(p,b){const r=await fetch(p,{method:b?'POST':'GET',headers:{'X-Token':T,'Content-Type':'application/json'},body:b?JSON.stringify(b):undefined});
 const j=await r.json().catch(()=>({error:'응답 오류'}));if(!r.ok)throw new Error(j.error||j.message||r.status);return j}
function say(id,t,cls){const e=$(id);e.textContent=t;e.className='msg '+(cls||'')}
async function loadState(){const s=await api('/api/state');$('title').textContent=s.name+' 분석기';$('ver').textContent='web_ui '+s.version;
 $('topic').innerHTML=s.topics.map(t=>`<option ${t===s.topic?'selected':''}>${esc(t)}</option>`).join('');
 $('quota').textContent=`오늘 할당량 ${num(s.quota.used)} / ${num(s.quota.budget)}`;
 $('caption').textContent=s.caption_block?`자막 서버 차단 — ${s.caption_block}까지 쉬는 중 (음성인식으로)`:'자막 서버 정상';$('caption').className='pill '+(s.caption_block?'warn':'');
 const e=s.env;$('ytkey_now').innerHTML=e.YOUTUBE_API_KEY.set?`<span class=ok>설정됨</span> ${esc(e.YOUTUBE_API_KEY.tail)} · ${esc(e.YOUTUBE_API_KEY.source)}`:'<span class=bad>없음</span> — 넣어야 탐색할 수 있습니다';
 $('ghtok_now').innerHTML=e.GITHUB_TOKEN.set?`<span class=ok>설정됨</span> ${esc(e.GITHUB_TOKEN.tail)} · ${esc(e.GITHUB_TOKEN.source)}`:'없음 — 결과는 PC 에만 저장';
 if(document.activeElement!==$('kw'))$('kw').value=s.keywords_text;$('kwCount').textContent=`검색어 ${s.keywords_count}개`;
 renderTargets(s.targets);showJob(s.job);estimate();return s}
function renderTargets(tg){const c=tg.channels.map(x=>`<span class=chip>📺 ${esc(x.title||x.id)} <span class=mut>영상 ${num(x.videos)}개</span><button data-k=channel data-id="${esc(x.id)}" title="빼기">✕</button></span>`);
 const v=tg.videos.map(x=>`<span class=chip>▶ ${esc((x.title||x.id).slice(0,40))}<button data-k=video data-id="${esc(x.id)}" title="빼기">✕</button></span>`);
 $('tgList').innerHTML=(c.concat(v).join(''))||'<span class=mut>추가한 영상·채널 없음</span>';
 $('tgList').querySelectorAll('button').forEach(b=>b.onclick=async()=>{const r=await api('/api/targets/remove',{kind:b.dataset.k,id:b.dataset.id});renderTargets(r.targets);estimate()})}
let estT;function estimate(){clearTimeout(estT);estT=setTimeout(async()=>{try{const e=await api(`/api/estimate?weeks=${$('weeks').value}&kw=${$('useKw').checked?1:0}`);
 $('est').textContent=`검색 ${e.searches}번 (캐시 ${e.cached}) + 채널 ${e.channels}·영상 ${e.videos} → 약 ${num(e.units)}단위`}catch(x){$('est').textContent=x.message}},250)}
async function loadRows(){const d=await api('/api/explore');ROWS=d.rows;CHECK=new Set(d.checked);REC=new Set(ROWS.filter(r=>r.reason).map(r=>r.id));
 $('listInfo').textContent=d.generated?`최근 업로드 순 · ${d.generated.slice(0,16).replace('T',' ')} 탐색 (최근 ${d.weeks}주) · 영상 ${ROWS.length.toLocaleString()}개 · 추천은 체크해 둠`:'최근 업로드 순 · 추천은 체크해 둠';renderRows()}
function visible(){const f=$('flt').value.trim().toLowerCase();return ROWS.filter(r=>(r.sources.includes('주소')||(($('fShort').checked||!r.short)&&(!$('fRel').checked||r.relevant)))
 &&(!$('fChk').checked||CHECK.has(r.id))&&(!f||(r.title+' '+r.channel).toLowerCase().includes(f)))}
function renderRows(){const vs=visible();if(!ROWS.length){$('rows').innerHTML='<tr><td colspan=10 class=mut>탐색을 누르면 여기에 나옵니다</td></tr>';updChk();return}
 $('rows').innerHTML=vs.slice(0,3000).map(r=>{const src=r.sources.map(s=>s.startsWith('검색:')?'🔎'+s.slice(3):s.startsWith('채널:')?'📺'+s.slice(3):'▶ 추가').slice(0,3).join(' ');
  return `<tr class="${CHECK.has(r.id)?'on':''}"><td><input type=checkbox data-id="${r.id}" ${CHECK.has(r.id)?'checked':''}></td><td>${esc(r.published)}<div class=mut>${r.age_days}일 전</div></td>
  <td class=t><a href="${r.url}" target=_blank rel=noopener>${esc(r.title)}</a></td><td>${esc(r.channel)}</td><td class=n>${r.subs==null?'비공개':num(r.subs)}</td><td class=n>${num(r.views)}</td>
  <td class=n>${r.ratio==null?'–':num(r.ratio)}</td><td class=n>${num(r.views_per_day)}</td><td class=n>${num(r.minutes)}분</td>
  <td>${r.reason?`<span class="tag ${r.reason==='성공 사례'?'s':''}">${esc(r.reason)}</span>`:''}${r.downloaded?'<span class="tag d">받음</span>':''}<span class=mut>${esc(src)}</span></td></tr>`}).join('')
  +(vs.length>3000?`<tr><td colspan=10 class=mut>앞 3,000개만 보입니다 — 거르기를 쓰세요 (전체 ${vs.length.toLocaleString()}개)</td></tr>`:'');
 $('rows').querySelectorAll('input[type=checkbox]').forEach(c=>c.onchange=()=>{c.checked?CHECK.add(c.dataset.id):CHECK.delete(c.dataset.id);c.closest('tr').className=c.checked?'on':'';updChk();saveChk()});updChk()}
function updChk(){$('chkInfo').textContent=`체크 ${CHECK.size.toLocaleString()}개 / 목록 ${ROWS.length.toLocaleString()}개`;$('approve').disabled=busy||!CHECK.size}
let chkT;function saveChk(){clearTimeout(chkT);chkT=setTimeout(()=>api('/api/checked',{ids:[...CHECK]}).catch(()=>{}),700)}
function showJob(j){busy=j.status==='running';$('jobName').textContent=j.name?`${j.name} — ${({running:'도는 중',done:'끝',error:'오류',cancelled:'멈춤',idle:''})[j.status]||j.status}`:'';
 $('jobStep').innerHTML=j.status==='error'?`<span class=bad>${esc(j.error)}</span>`:esc(j.step||'쉬는 중');
 $('jobBar').style.width=j.total?Math.round(100*j.done/j.total)+'%':(busy?'15%':'0');$('cancel').disabled=!busy;
 ['explore','reanalyze','whisper'].forEach(id=>$(id).disabled=busy);updChk();
 const L=$('jobLog'),atEnd=L.scrollTop+L.clientHeight>=L.scrollHeight-20;L.textContent=(j.log||[]).join('\n');if(atEnd)L.scrollTop=L.scrollHeight;
 if((lastJob==='running'||waitDone)&&j.status!=='running'){waitDone=false;loadState();loadRows();loadReport()}lastJob=j.status}
async function poll(){try{showJob(await api('/api/job'))}catch(e){}setTimeout(poll,busy?1000:4000)}
function pct(x){return x==null?'–':Math.round(x*100)+'%'}
async function loadReport(){const r=await api('/api/report');if(!r.windows){$('report').innerHTML='<span class=mut>승인한 영상이 생기면 여기에 나옵니다</span>';return}
 let h=`<div class=mut>${esc(r.generated.slice(0,16).replace('T',' '))} UTC · 승인 영상 ${r.cases}개 · ${esc(r.criteria)}${r.older_than_windows?` · ${r.max_weeks}주보다 오래된 영상 ${r.older_than_windows}개는 창 밖`:''}</div>
 <div class=tablewrap style="margin-top:8px"><table><thead><tr><th>창</th><th class=n>영상</th><th class=n>채널</th><th class=n>이번 주 새로</th><th class=n>조회수 중앙값</th><th class=n>하루 조회수</th><th class=n>배수</th><th class=n>성공 사례</th><th class=n>길이(분)</th><th class=n>제목 글자</th><th class=n>자막</th><th class=n>댓글</th></tr></thead><tbody>`;
 h+=r.windows.map(w=>`<tr><td>${esc(w.label)}</td><td class=n>${w.videos}</td><td class=n>${w.channels}</td><td class=n>${w.new_this_week.length}</td><td class=n>${num(w.views_median)}</td><td class=n>${num(w.views_per_day_median)}</td><td class=n>${num(w.ratio_median)}</td><td class=n>${w.success}</td><td class=n>${num(w.minutes_median)}</td><td class=n>${num(w.title_len_avg)}</td><td class=n>${w.transcripts}</td><td class=n>${num(w.comments)}</td></tr>`).join('')+'</tbody></table></div>';
 h+=r.windows.filter(w=>w.videos).map(w=>`<details><summary>${esc(w.label)} — 영상 ${w.videos}개 (이번 주 새로 ${w.new_this_week.length})</summary>
  ${w.title_features.length?`<p><b>제목 특징</b> ${w.title_features.slice(0,6).map(f=>esc(f.name)+' '+pct(f.share)).join(' · ')}</p>`:''}
  ${w.title_words.length?`<p><b>자주 쓴 낱말</b> ${w.title_words.map(x=>esc(x.word)+'('+x.count+')').join(', ')}</p>`:''}
  ${w.hooks.length?`<p><b>첫 20초</b> (말 속도 ${num(w.syl_per_sec_median)} 음절/초)</p><ul>${w.hooks.map(x=>`<li>${esc(x.title.slice(0,30))}: “${esc(x.hook)}”</li>`).join('')}</ul>`:''}
  ${w.comment_needs.length?`<p><b>댓글 ${num(w.comments)}개 니즈</b> ${w.comment_needs.map(n=>esc(n.name)+' '+pct(n.share)).join(' · ')}</p><ul>${w.top_comments.map(c=>`<li>👍${num(c.likes)} “${esc(c.text)}”</li>`).join('')}</ul>`:''}
  <p><b>상위 영상</b> (하루 조회수 순)</p><ol>${w.top_videos.map(v=>`<li><a href="${v.url}" target=_blank rel=noopener>${esc(v.title)}</a> <span class=mut>${esc(v.channel)} · ${num(v.views)}회 · 하루 ${num(v.views_per_day)} · ${v.published}</span></li>`).join('')}</ol></details>`).join('');
 $('report').innerHTML=h}
$('topic').onchange=async()=>{await api('/api/topic',{topic:$('topic').value});await loadState();await loadRows();await loadReport()};
$('saveEnv').onclick=async()=>{try{const r=await api('/api/env',{YOUTUBE_API_KEY:$('ytkey').value,GITHUB_TOKEN:$('ghtok').value});$('ytkey').value='';$('ghtok').value='';
 say('envMsg',r.changed.length?`저장함: ${r.changed.join(', ')}`:'바뀐 것 없음 (넣은 칸만 저장)','ok');loadState()}catch(e){say('envMsg',e.message,'bad')}};
$('saveKw').onclick=async()=>{try{const r=await api('/api/keywords',{text:$('kw').value,push:$('kwPush').checked});say('kwMsg',r.message,'ok');$('kwCount').textContent=`검색어 ${r.count}개`;estimate()}catch(e){say('kwMsg',e.message,'bad')}};
$('tgAdd').onclick=async()=>{const v=$('tgIn').value.trim();if(!v)return;say('tgMsg','확인 중…');try{const r=await api('/api/targets/add',{text:v});
 say('tgMsg',(r.added.kind==='channel'?`채널 추가: ${r.added.title} (영상 ${num(r.added.videos)}개)`:`영상 추가: ${r.added.title||r.added.id}`)+(r.added.note?' — '+r.added.note:''),'ok');$('tgIn').value='';renderTargets(r.targets);estimate()}catch(e){say('tgMsg',e.message,'bad')}};
$('tgIn').onkeydown=e=>{if(e.key==='Enter')$('tgAdd').click()};
$('weeks').oninput=estimate;$('useKw').onchange=estimate;
async function startJob(p,b){try{waitDone=true;await api(p,b);busy=true;showJob(await api('/api/job'))}catch(e){waitDone=false;alert(e.message)}}
$('explore').onclick=()=>startJob('/api/explore',{weeks:+$('weeks').value,keywords:$('useKw').checked});
$('approve').onclick=async()=>{const ids=ROWS.filter(r=>CHECK.has(r.id)).map(r=>r.id);if(!ids.length)return;
 if(!confirm(`체크한 영상 ${ids.length}개의 설명·자막·썸네일·댓글 전부를 받고 분석합니다.\n(댓글 100개에 할당량 1단위)`))return;
 startJob('/api/approve',{ids,whisper:$('autoW').checked})};
$('cancel').onclick=()=>api('/api/cancel',{});$('reanalyze').onclick=()=>startJob('/api/analyze',{});$('whisper').onclick=()=>startJob('/api/whisper',{});
['flt','fShort','fRel','fChk'].forEach(id=>$(id).addEventListener('input',renderRows));
$('chkAll').onclick=()=>{visible().forEach(r=>CHECK.add(r.id));renderRows();saveChk()};$('chkNone').onclick=()=>{CHECK.clear();renderRows();saveChk()};
$('chkRec').onclick=()=>{CHECK=new Set(REC);renderRows();saveChk()};
loadState().then(()=>{loadRows();loadReport()}).catch(e=>document.body.insertAdjacentHTML('afterbegin',`<p class=bad style="padding:16px">${esc(e.message)}</p>`));poll();
</script></body></html>
"""


if __name__ == "__main__":
    sys.exit(main())
