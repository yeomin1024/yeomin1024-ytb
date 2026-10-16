#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-10-16 — ① list·approve 가 웹 화면처럼 이미 분석에 쓴 영상(W_·01_·P01_ / 쇼츠 S_)을 뺌 (GET /api/explore 와 같은 규칙 —
#          v1.0 은 목록에 승인한 102개가 섞였고, 그대로 승인하면 이미 받은 자료를 다시 받았음) ② foreign on|off — 웹 화면 [외국 영상도]와 같음
#          (사용자 지시 2026-10-16 "잠깐 주식 주제는 외국 영상도 포함해" — 설정 파일만 고치고 GitHub 에는 Claude 가 git 으로)
# (v1.0 — 2026-10-16 — 신규: 클라우드(Claude Code)에서 웹 화면 없이 분석 돌리기 (사용자 지시 2026-10-16: "이 환경은 이제 저장소에 있는
#          주식 주제 (stock 경로)를 유튜브 분석 코드 실행해서 분석하는 환경이야 한번 해봐" · "아마 분석 코드가 ui로 되어 있을텐데 너가 분석하기
#          쉽도록 수정해도 돼 분석 로직은 변경하지말고"). 웹 화면(tools/web_ui.py)의 작업 함수 — 탐색·승인·채널 기준선·댓글 이어 받기·자동완성·
#          분석 다시·남은 것 이어서·쇼츠 — 를 그대로 부르는 명령줄 껍데기. 분석·추천(체크)·할당량 계산은 web_ui.py 와 같은 코드다.
#          클라우드에서 바꾼 것 (분석 로직 아님):
#          ① 올리기: 기본은 분석기 --push-only(따로 clone) 대신 이 작업 폴더에 남김 → Claude 가 git 으로 main 에 (--push analyzer 면 예전처럼)
#          ② FRESH_START 보호: 클라우드 컨테이너에는 PC 표시(.yt_work/fresh_start_<주제>.txt)가 없어 web_ui·pc_analysis 가 켤 때 git 에 있는
#             승인 결과(W_…)를 .yt_work/old/ 로 옮겨 버림 → 사례 폴더가 이미 있으면 옮기지 않고 표시만 씀
#          ③ 음성인식은 시작하지 않음 (클라우드엔 Whisper·소리 받기 길이 없음 — 남은 수만 보여 줌)
# ※ 연구·교육용 분석 도구. 투자 권유가 아니다.
"""클라우드 분석 실행기 — 웹 화면 없이 같은 작업을 명령으로.

  python3 tools/cloud_run.py stock status                  # 할당량·탐색 목록·승인 수·남은 것
  python3 tools/cloud_run.py stock explore --weeks 26      # [탐색] (검색어마다 4~20분·20분 넘음, 검색 1번 100단위, 캐시 7일~)
  python3 tools/cloud_run.py stock list --unchecked        # 5번 칸 목록 (배수 높은 순, ✔ = 체크(추천))
  python3 tools/cloud_run.py stock check ID … / uncheck ID …
  python3 tools/cloud_run.py stock approve                 # [승인] — 체크한 영상 (ID 를 주면 그 영상만)
  python3 tools/cloud_run.py stock baseline | comments | demand | analyze | resume | startup
  python3 tools/cloud_run.py stock explore --shorts / list --shorts / approve --shorts   # 쇼츠
  python3 tools/cloud_run.py stock foreign on|off          # [외국 영상도] (analyzer_config.toml INCLUDE_FOREIGN)
  python3 tools/cloud_run.py stock wait-reset [--then resume]   # 태평양 자정 +10분까지 기다림 (할당량 초기화)

로그: [STAGE] [시각] key=value (web_ui·outlier_research 와 같은 꼴) — 화면과 .yt_work/cloud_run_<주제>.log
끝 줄: [RESULT] [시각] cmd=… result={JSON}
"""
import argparse
import json
import logging
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import pc_analysis as pc                 # noqa: E402
import web_ui as w                       # noqa: E402

VERSION = "v1.1"
ROOT = pc.ROOT
LOG = logging.getLogger("cloud")
_STEP = {"text": None, "at": 0.0}
STEP_EVERY_S = 5.0                       # 진행 줄은 바뀔 때마다가 아니라 5초에 한 번 (검색·댓글 줄이 수백 개라 — 끝 줄은 늘 남김)


def log(stage, level=logging.INFO, **kv):
    w.log(stage, level, **kv)


# ---------------------------------------------------------------- 준비
def setup_logging(t, level):
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass
    fmt = logging.Formatter("%(message)s")
    root = logging.getLogger()
    root.setLevel(getattr(logging, level))
    (ROOT / ".yt_work").mkdir(exist_ok=True)
    for h in (logging.StreamHandler(sys.stdout), logging.FileHandler(ROOT / ".yt_work" / f"cloud_run_{t}.log", encoding="utf-8")):
        h.setFormatter(fmt)
        root.addHandler(h)


def load_tools():
    """web_ui.main 이 하는 불러오기만 (서버·브라우저·GitHub 동기화·잠금 화면 없이)."""
    import outlier_research as _orr
    import weekly_analysis as _wa
    w.orr, w.wa = _orr, _wa
    try:
        import shorts_analysis as _sh
        w.sh = _sh
    except Exception as e:
        log("START", logging.WARNING, note="쇼츠 분석 도구를 못 불러옴 — 쇼츠 명령만 꺼짐", error=f"{type(e).__name__}: {e}"[:160])


def guard_fresh_start(t):
    """FRESH_START 보호 (v1.0 ②): 사례 폴더(W_·S_·01_·P01_)가 이미 있으면(= git 에서 받은 결과) 옮기지 않고 PC 표시만 씀."""
    want = str(pc._topic_flat(t).get("FRESH_START") or "").strip()
    if not want:
        return
    mark = ROOT / ".yt_work" / f"fresh_start_{t}.txt"
    have = mark.read_text("utf-8").strip() if mark.is_file() else ""
    if have == want:
        return
    od = w.out_dir(t)
    cases = [d for d in od.iterdir() if d.is_dir() and w.CASE_RX.match(d.name)] if od.is_dir() else []
    cases += list(w.shorts_out(t).glob("S_*"))
    if cases:
        mark.parent.mkdir(parents=True, exist_ok=True)
        mark.write_text(want + "\n", "utf-8")
        log("RESET", topic=t, fresh_start=want, cases=len(cases),
            note="git 에 받은 결과가 있어 옮기지 않음 — 표시만 씀 (클라우드 컨테이너에는 PC 표시가 없음)")
    else:
        pc.fresh_start(t)


def progress_step(orig):
    """web_ui.step 을 감싸 진행을 로그로 (화면의 '진행' 칸 대신). 멈춤 검사 등 원래 동작은 그대로."""
    def step(text, done=None, total=None):
        orig(text, done, total)
        now = time.monotonic()
        last = done is not None and total is not None and total and done >= total
        if text != _STEP["text"] and (last or now - _STEP["at"] >= STEP_EVERY_S):
            _STEP.update(text=text, at=now)
            log("STEP", text=text[:120], done=done if done is not None else "-", total=total if total is not None else "-")
    return step


def local_push(t, message):
    """올리기 (v1.0 ①): 결과는 이미 이 작업 폴더(<주제>/result/…)에 있음 → Claude 가 git 으로 main 에. 분석기 clone 올리기는 하지 않음."""
    note = "클라우드: 작업 폴더에 저장 — git 으로 main 에 올릴 것 (커밋 메시지 예: " + message[:80] + ")"
    log("PUSH", topic=t, mode="local", note=note)
    return {"pushed": False, "push_note": note, "materials": "작업 폴더 (git 에 아직 안 올림)"}


def no_whisper(t, why=""):
    n = w.whisper_pending(t, fresh=True)
    log("WHISPER", logging.WARNING, topic=t, pending=n, why=why or "-",
        note="클라우드에서는 음성인식을 시작하지 않음 (Whisper·소리 받기 없음) — PC 웹 화면의 [음성인식 시작]으로")
    return False, f"클라우드 — 음성인식 안 함 (남은 {n}개)"


# ---------------------------------------------------------------- 목록·체크
def explore_file(shorts):
    return "shorts_explore.json" if shorts else "explore.json"


def used(t, shorts):
    """이미 분석에 쓴 영상 — 웹 화면 GET /api/explore 와 같은 규칙 (목록·체크에서 뺌, 승인하면 바로 빠짐)."""
    return w.used_shorts_ids(t) if shorts else w.used_ids(t)


def cmd_list(t, a):
    ex = w._read_json(w.web_dir(t) / explore_file(a.shorts), {})
    rows = ex.get("rows") or []
    if not rows:
        print("탐색 목록이 없습니다 — 먼저 explore" + (" --shorts" if a.shorts else ""))
        return {"rows": 0}
    u = used(t, a.shorts)
    hidden = sum(1 for r in rows if r["id"] in u)
    rows = sorted((r for r in rows if r["id"] not in u), key=w.ratio_key)
    checked = {i for i in ex.get("checked") or [] if i not in u}
    sel = [r for r in rows if (a.checked and r["id"] in checked) or (a.unchecked and r["id"] not in checked)
           or not (a.checked or a.unchecked)]
    print(f"# {t} {'쇼츠 ' if a.shorts else ''}탐색 목록 {ex.get('generated')} · 최근 {ex.get('weeks')}주 · 영상 {len(rows)} · 체크 {len(checked)}"
          f" · 뺀 것 {ex.get('excluded') or {}} · 이미 분석에 쓴 영상 {hidden}개 숨김 · 못 한 검색 {len(ex.get('pending') or [])}")
    print("n | ✔ | 까닭 | 배수 | 조회수 | 구독자 | 분 | 일 | 관련 | 제목 | 채널 | id")
    for n, r in enumerate(sel[: a.limit or None], 1):
        print(" | ".join(str(x) for x in (
            n, "✔" if r["id"] in checked else " ", r.get("reason") or "-", r.get("ratio") if r.get("ratio") is not None else "-",
            f"{r.get('views') or 0:,}", f"{r['subs']:,}" if r.get("subs") is not None else "비공개", r.get("minutes"),
            r.get("age_days"), "O" if r.get("relevant") else "x" + (" 짧음" if r.get("short") else ""),
            (r.get("title") or "")[:60].replace("|", "/"), (r.get("channel") or "")[:20].replace("|", "/"), r["id"])))
    return {"rows": len(rows), "used_hidden": hidden, "shown": min(len(sel), a.limit or len(sel)), "checked": len(checked)}


def cmd_check(t, a, on):
    fn = explore_file(a.shorts)
    ex = w._read_json(w.web_dir(t) / fn, {})
    if not ex:
        raise w.UserError("탐색 목록이 없습니다 — 먼저 explore")
    ok_ids = {r["id"] for r in ex.get("rows") or []}
    bad = [i for i in a.ids if i not in ok_ids]
    cur = list(ex.get("checked") or [])
    if on:
        cur += [i for i in a.ids if i in ok_ids and i not in cur]
    else:
        cur = [i for i in cur if i not in set(a.ids)]
    ex["checked"] = [i for i in cur if i in ok_ids]                       # /api/checked 와 같은 규칙 — 목록에 있는 영상만
    w._write_json(w.web_dir(t) / fn, ex)
    log("CHECK", topic=t, on=on, ids=len(a.ids), not_in_list=",".join(bad) or "-", checked=len(ex["checked"]))
    return {"checked": len(ex["checked"]), "not_in_list": bad}


def cmd_status(t, a):
    ex = w._read_json(w.web_dir(t) / "explore.json", {})
    sx = w._read_json(w.web_dir(t) / "shorts_explore.json", {})
    q = w.quota_view(t)
    od = w.out_dir(t)
    res = {"tool": f"cloud_run.py {VERSION} / web_ui.py {w.VERSION}", "topic": t, "name": w.topic_name(t),
           "include_foreign": w.foreign_ok(t), "key_source": w.orr.load_api_key(t)[1],
           "github_token": "있음" if pc.find_secret("GITHUB_TOKEN", t)[0] else "없음",
           "quota": {k: q.get(k) for k in ("used", "left", "budget", "exhausted", "reset_kst", "searches", "search_blocked", "search_cap", "day")},
           "explore": {"generated": ex.get("generated"), "weeks": ex.get("weeks"), "videos": len(ex.get("rows") or []),
                       "checked": len(ex.get("checked") or []), "pending": len(ex.get("pending") or []),
                       "pending_videos": ex.get("pending_videos"), "excluded": ex.get("excluded")},
           "shorts_explore": {"generated": sx.get("generated"), "videos": len(sx.get("rows") or []), "checked": len(sx.get("checked") or [])},
           "cases": {"W_": len(list(od.glob("W_*/metadata.json"))), "S_": len(list(w.shorts_out(t).glob("S_*/metadata.json")))},
           "cache_files": len(list((od / ".cache").glob("*.json"))) if (od / ".cache").is_dir() else 0,
           "resume_plan": w.resume_plan(t), "whisper_pending": w.whisper_pending(t, fresh=True)}
    until = w.orr.caption_blocked()
    res["caption_block"] = until.astimezone(w.KST).isoformat(timespec="minutes") if until else None
    print(json.dumps(res, ensure_ascii=False, indent=1))
    return {"ok": True}


def cmd_approve(t, a):
    fn = explore_file(a.shorts)
    ex = w._read_json(w.web_dir(t) / fn, {})
    u = used(t, a.shorts)
    ids = [i for i in (list(a.ids) or list(ex.get("checked") or [])) if i not in u]     # 화면처럼 이미 받은 영상은 다시 받지 않음
    log("APPROVE", topic=t, shorts=a.shorts, ids=len(ids), note="체크한 영상 (이미 분석에 쓴 영상은 뺌)" if not a.ids else "준 ID")
    if a.shorts:
        w.need_sh()
        return w.job_shorts_approve(t, ids, False)
    return w.job_approve(t, ids, False)


def cmd_foreign(t, a):
    """[외국 영상도] — /api/foreign 과 같음 (작업 중엔 못 바꿈은 이 명령이 혼자 도므로 해당 없음). GitHub 올리기는 git 으로."""
    if not a.ids or a.ids[0] not in ("on", "off"):
        raise w.UserError("foreign on 또는 foreign off")
    on = a.ids[0] == "on"
    if w.foreign_ok(t) == on:
        return {"include_foreign": on, "message": "이미 " + ("켜져" if on else "꺼져") + " 있습니다"}
    w.set_include_foreign(t, on)
    nf = len(pc.read_keyword_list(w.foreign_keywords_path(t)) or []) if w.foreign_keywords_path(t).is_file() else 0
    log("SETTINGS", topic=t, include_foreign=w.foreign_ok(t), file=f"{t}/analyzer_config.toml", foreign_keywords=nf,
        note="다음 탐색부터 " + ("외국 영상도 — 검색은 언어 지정 없이 새로 (첫 탐색은 캐시 없음)" if on else "외국 영상을 뺌"))
    return {"include_foreign": w.foreign_ok(t), "foreign_keywords": nf}


def cmd_wait_reset(t, a):
    nxt, how = pc.next_quota_reset(datetime.now(timezone.utc), margin_min=w.RESUME_MARGIN_MIN)
    log("WAIT", topic=t, until_kst=nxt.astimezone(w.KST).isoformat(timespec="minutes"), how=how,
        minutes=round((nxt - datetime.now(timezone.utc)).total_seconds() / 60, 1), note="할당량 초기화(태평양 자정) +10분까지 기다림")
    while (left := (nxt - datetime.now(timezone.utc)).total_seconds()) > 0:
        time.sleep(min(60.0, left))
    res = {"waited_until": nxt.isoformat()}
    if a.then == "resume":
        res.update(w.job_resume(t, "할당량 초기화 (클라우드)"))
    return res


# ---------------------------------------------------------------- 명령
def main(argv=None):
    ap = argparse.ArgumentParser(description="클라우드 분석 실행기 — 웹 화면(tools/web_ui.py) 작업을 명령으로")
    ap.add_argument("topic", help="주제 폴더 (예: stock)")
    ap.add_argument("cmd", choices=["status", "explore", "list", "check", "uncheck", "approve", "baseline", "comments", "demand",
                                    "analyze", "resume", "startup", "foreign", "wait-reset"])
    ap.add_argument("ids", nargs="*", help="check·uncheck·approve 할 영상 ID (foreign 은 on|off)")
    ap.add_argument("--weeks", type=int, default=8, help="explore: 최근 몇 주 (웹 화면 기본 8, 1~52)")
    ap.add_argument("--no-keywords", action="store_true", help="explore: 검색어 없이 추가한 채널·영상만")
    ap.add_argument("--shorts", action="store_true", help="쇼츠 (explore·list·check·approve)")
    ap.add_argument("--checked", action="store_true", help="list: 체크한 것만")
    ap.add_argument("--unchecked", action="store_true", help="list: 체크 안 한 것만")
    ap.add_argument("--limit", type=int, default=0, help="list: 몇 줄 (0 = 전부)")
    ap.add_argument("--push", choices=["none", "analyzer"], default="none",
                    help="none(기본) = 작업 폴더에만 (git 으로 직접) · analyzer = 웹 화면처럼 분석기 --push-only")
    ap.add_argument("--then", choices=["none", "resume"], default="none", help="wait-reset 뒤에 할 일")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args(argv)
    t = a.topic
    if not w.TOPIC_RX.match(t) or not (ROOT / t / "analyzer_config.toml").is_file():
        raise SystemExit(f"[START] ❌ 주제 설정 {t}/analyzer_config.toml 이 없음")
    setup_logging(t, a.log_level)
    load_tools()
    w.STATE.update(topic=t, topics=[t])
    w.step = progress_step(w.step)
    w.start_whisper = no_whisper
    if a.push == "none":
        w.push_results = local_push
    guard_fresh_start(t)
    try:
        w.claim_topic(t)                     # 웹 화면과 같은 잠금 — 같은 주제를 두 곳에서 동시에 돌리지 않게
    except w.UserError as e:
        raise SystemExit(f"[START] ❌ {e}")
    weeks = max(1, min(52, a.weeks))
    log("START", tool=f"cloud_run.py {VERSION}", web_ui=w.VERSION, topic=t, cmd=a.cmd, push=a.push, weeks=weeks if a.cmd == "explore" else "-",
        include_foreign=w.foreign_ok(t), key_source=w.orr.load_api_key(t)[1])
    t0 = time.monotonic()
    code = 0
    try:
        if a.cmd == "status":
            res = cmd_status(t, a)
        elif a.cmd == "list":
            res = cmd_list(t, a)
        elif a.cmd in ("check", "uncheck"):
            res = cmd_check(t, a, a.cmd == "check")
        elif a.cmd == "explore":
            if a.shorts:
                w.need_sh()
                res = w.job_shorts_explore(t, weeks, not a.no_keywords)
            else:
                res = w.job_explore(t, weeks, not a.no_keywords)
        elif a.cmd == "approve":
            res = cmd_approve(t, a)
        elif a.cmd == "baseline":
            res = w.job_baseline(t)
            if w.sh is not None:
                res.update(w.job_shorts_baseline(t, quiet=True))
        elif a.cmd == "comments":
            res = w.job_comments(t)
        elif a.cmd == "demand":
            res = w.job_demand(t)
        elif a.cmd == "analyze":
            res = w.job_analyze(t)
        elif a.cmd == "resume":
            res = w.job_resume(t, "클라우드에서 이어서")
        elif a.cmd == "startup":
            res = w.job_startup(t, whisper=False)
        elif a.cmd == "foreign":
            res = cmd_foreign(t, a)
        elif a.cmd == "wait-reset":
            res = cmd_wait_reset(t, a)
        else:
            res = {}
    except w.UserError as e:
        res, code = {"error": str(e)}, 2
        log("JOB", logging.WARNING, topic=t, cmd=a.cmd, error=str(e))
    except w.Cancelled:
        res, code = {"error": "멈춤"}, 130
    finally:
        w.release_topic(t)
    log("RESULT", cmd=a.cmd, seconds=round(time.monotonic() - t0, 1), result=json.dumps(res, ensure_ascii=False, default=str)[:4000])
    return code


if __name__ == "__main__":
    sys.exit(main())
