#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0.1 — 2026-11-13 — 토큰 실패 로그가 log() 의 stage 인자와 겹쳐 TypeError 로 죽던 것 고침 (stage= → step=). 동작 그대로.
# (v1.0 — 2026-11-10 — 새로: YouTube Reporting API 의 도달범위 보고서(썸네일 노출 수·노출 클릭률)를 받아 영상별로 모음.)
#   사용자 지시 2026-11-10 "노출수랑 클릭률은 조회가 안돼?" → "reporting api 허용했으니 참고하고 …".
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.0.1 | 2026-11-13 | 토큰 실패 로그 TypeError 고침 | token |
# | v1.0 | 2026-11-10 | 최초 — list(작업·보고서 수) · fetch(새 보고서 받아 영상별 합계 `<주제>/result/channel/reach.md`·`.json`) · --selftest | jobs·reports·summarize·main |
#
# 왜: 통계 API(v2)는 노출·클릭률을 주지 않는다 (2026-11-10 열 가지 조합 모두 '지원하지 않는 질의'). Reporting API 는 '작업'을 만들어 두면 날마다 CSV 보고서를 만들어 준다
#     (보고서 종류 channel_reach_basic_a1 · channel_reach_combined_a1 — 작업은 2026-11-10 에 만듦 · 첫 보고서는 만든 뒤 하루 이틀, 지난 30일 치 포함).
# 쓰기:
#   python3 tools/yt_reach.py stock list             # 작업과 보고서 수 (읽기만)
#   python3 tools/yt_reach.py stock fetch            # 보고서를 받아 영상별 노출·클릭 합계 → stock/result/channel/reach.md · reach.json (원본 CSV 는 git 밖 .yt_work/reach/)
#   python3 tools/yt_reach.py --selftest             # 합계 계산 검사 (네트워크 없음)
# 키: 환경 변수 YOUTUBE_CLIENT_ID · YOUTUBE_CLIENT_SECRET · YOUTUBE_REFRESH_TOKEN (값은 출력하지 않음). 채널이 `<주제>/youtube_channel.json` 과 다르면 멈춤.
# 열 이름은 보고서 머리줄에서 찾는다 ('impressions' 가 든 열 = 노출 · 'ctr' 가 든 열 = 클릭률) — 클릭 수 = 노출 × 클릭률 을 날·영상마다 구해 더한 뒤 다시 나눔(클릭률을 그냥 평균하지 않음).
# ※ 연구·교육용 도구. 조회(views)·참여 조회(engagedViews)와 섞지 않는다 — 이 도구는 노출·클릭률만.
from __future__ import annotations

import csv
import gzip
import io
import json
import logging
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

VERSION = "v1.0.1"
ROOT = Path(__file__).resolve().parents[1]
API = "https://youtubereporting.googleapis.com/v1/"
TYPES = ("channel_reach_basic_a1", "channel_reach_combined_a1")

logging.basicConfig(level=os.environ.get("LOG_LEVEL", "INFO"), format="%(message)s", stream=sys.stdout)


def log(stage: str, level: int = logging.INFO, **kv) -> None:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    logging.log(level, f"[{stage}] [{ts}] " + " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, (str, dict, list)) else v}" for k, v in kv.items()))


def token() -> str:
    need = ("YOUTUBE_CLIENT_ID", "YOUTUBE_CLIENT_SECRET", "YOUTUBE_REFRESH_TOKEN")
    miss = [k for k in need if not os.environ.get(k)]
    if miss:
        log("FAIL", logging.ERROR, stage="auth", missing=miss, next="환경 변수에 키를 넣는다 (guides/upload_guide.md)")
        raise SystemExit(2)
    body = urllib.parse.urlencode({"client_id": os.environ[need[0]].strip(), "client_secret": os.environ[need[1]].strip(),
                                   "refresh_token": os.environ[need[2]].strip(), "grant_type": "refresh_token"}).encode()
    try:
        with urllib.request.urlopen(urllib.request.Request("https://oauth2.googleapis.com/token", data=body), timeout=40) as r:
            return json.load(r)["access_token"]
    except urllib.error.HTTPError as e:
        log("FAIL", logging.ERROR, step="auth", http=e.code, next="키가 만료됐는지 tools/youtube_upload.py --check-auth 로 확인")
        raise SystemExit(2)


def get(url: str, tok: str, raw: bool = False, **q):
    u = url + ("?" + urllib.parse.urlencode(q) if q else "")
    last = None
    for wait in (0, 2, 4, 8):
        time.sleep(wait)
        try:
            with urllib.request.urlopen(urllib.request.Request(u, headers={"Authorization": "Bearer " + tok}), timeout=90) as r:
                data = r.read()
            return data if raw else json.loads(data)
        except urllib.error.HTTPError as e:
            last = f"HTTP {e.code} {e.read().decode(errors='replace')[:200]}"
            if e.code in (400, 401, 403, 404):
                break
        except Exception as e:  # noqa: BLE001
            last = repr(e)[:200]
    log("FAIL", logging.ERROR, stage="api", url=url.split("?")[0], err=last, next="403 이면 Google Cloud 에서 YouTube Reporting API 를 켰는지 확인")
    raise SystemExit(3)


def check_channel(topic: str, tok: str) -> str:
    want = json.loads((ROOT / topic / "youtube_channel.json").read_text(encoding="utf-8"))["channel_id"]
    got = get("https://www.googleapis.com/youtube/v3/channels", tok, part="id", mine="true")["items"][0]["id"]
    if want != got:
        log("FAIL", logging.ERROR, stage="channel", issue="키의 채널이 이 주제 채널과 다름", next=f"{topic}/youtube_channel.json 과 환경 키를 확인")
        raise SystemExit(4)
    return got


def jobs(tok: str) -> list[dict]:
    js = [j for j in get(API + "jobs", tok).get("jobs", []) if j.get("reportTypeId") in TYPES]
    for j in js:
        j["reports"] = get(API + f"jobs/{j['id']}/reports", tok).get("reports", [])
        log("JOB", type=j["reportTypeId"], created=j.get("createTime", "")[:10], reports=len(j["reports"]),
            newest=max((r.get("endTime", "")[:10] for r in j["reports"]), default="-"))
    if not js:
        log("JOB", logging.WARNING, issue="도달범위 작업이 없음", next="Reporting API jobs.create 로 channel_reach_basic_a1 작업을 만든다 (2026-11-10 에 만든 것이 지워졌는지 확인)")
    return js


def summarize(rows: list[dict]) -> dict:
    """영상별 노출·클릭 합계. 클릭 = 노출 × 클릭률 (줄마다) → 합 → 다시 나눔. 값이 비었거나 음수인 줄은 세고 뺌."""
    if not rows:
        return {"videos": {}, "bad_rows": 0, "rows": 0, "cols": {}}
    head = list(rows[0].keys())
    imp = next((c for c in head if "impressions" in c and "ctr" not in c and "rate" not in c), None)
    ctr = next((c for c in head if "impressions" in c and ("ctr" in c or "rate" in c)), None)
    vid = next((c for c in head if c == "video_id"), None)
    if not (imp and vid):
        log("FAIL", logging.ERROR, stage="parse", head=head, next="보고서 머리줄에 video_id·impressions 열이 있는지 확인 (보고서 종류가 바뀌었을 수 있음)")
        raise SystemExit(5)
    agg, bad, seen = defaultdict(lambda: {"impressions": 0.0, "clicks": 0.0, "days": set()}), 0, set()
    for r in rows:
        try:
            n = float(r[imp]); c = float(r[ctr]) if ctr and r.get(ctr) not in (None, "") else 0.0
        except (TypeError, ValueError):
            bad += 1; continue
        if n < 0 or not (0 <= c <= 1.0001):
            bad += 1; continue
        key = tuple(r.get(k) for k in head if k not in (imp, ctr))        # 같은 줄이 두 보고서에 있으면 한 번만
        if key in seen:
            continue
        seen.add(key)
        a = agg[r[vid]]
        a["impressions"] += n; a["clicks"] += n * c; a["days"].add(r.get("date"))
    out = {v: {"impressions": int(round(a["impressions"])), "clicks": round(a["clicks"], 1), "ctr": round(a["clicks"] / a["impressions"], 4) if a["impressions"] else None,
               "days": len(a["days"])} for v, a in agg.items()}
    return {"videos": dict(sorted(out.items(), key=lambda kv: -kv[1]["impressions"])), "bad_rows": bad, "rows": len(rows), "cols": {"impressions": imp, "ctr": ctr}}


def fetch(topic: str, tok: str) -> int:
    js = jobs(tok)
    work = ROOT / topic / ".yt_work" / "reach"
    work.mkdir(parents=True, exist_ok=True)
    rows, n_new = [], 0
    for j in (x for x in js if x["reportTypeId"] == "channel_reach_basic_a1"):
        for r in j["reports"]:
            f = work / f"{r['id']}.csv"
            if not f.exists():                                                  # 이미 받은 보고서는 다시 받지 않음
                data = get(r["downloadUrl"], tok, raw=True)
                if data[:2] == b"\x1f\x8b":
                    data = gzip.decompress(data)
                f.write_bytes(data); n_new += 1
            rows += list(csv.DictReader(io.StringIO(f.read_text(encoding="utf-8"))))
    log("FETCH", reports_new=n_new, rows=len(rows), cache=str(work.relative_to(ROOT)))
    if not rows:
        log("FETCH", logging.WARNING, issue="보고서가 아직 없음", next="작업을 만든 뒤 하루 이틀 뒤 다시 (지난 30일 치가 함께 나옴)")
        return 0
    S = summarize(rows)
    if S["bad_rows"]:
        log("DATA", logging.WARNING, issue="빈 값·범위 밖 줄", n=S["bad_rows"], action="뺌")
    out = ROOT / topic / "result" / "channel"
    out.mkdir(parents=True, exist_ok=True)
    made = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    (out / "reach.json").write_text(json.dumps({"tool": f"yt_reach.py {VERSION}", "made": made, **S}, ensure_ascii=False, indent=1), encoding="utf-8")
    L = [f"# {topic} 채널 — 썸네일 노출·클릭률 (YouTube Reporting API 도달범위 보고서)", "",
         f"`tools/yt_reach.py {VERSION}` · {made} · 줄 {S['rows']:,}개 · 영상 {len(S['videos'])}개. 클릭 = 노출 × 클릭률을 날마다 구해 더함. ※ 조회·참여 조회와 다른 숫자.", "",
         "| 영상 ID | 노출 | 클릭 | 클릭률 | 날 수 |", "|---|---|---|---|---|"]
    L += [f"| {v} | {a['impressions']:,} | {a['clicks']:,} | {a['ctr']:.2%} | {a['days']} |" if a["ctr"] is not None else f"| {v} | 0 | 0 | — | {a['days']} |" for v, a in S["videos"].items()]
    (out / "reach.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    log("WRITE", md=str((out / "reach.md").relative_to(ROOT)), videos=len(S["videos"]))
    return 0


def selftest() -> int:
    rows = [{"date": "20261101", "video_id": "a", "video_thumbnail_impressions": "100", "video_thumbnail_impressions_ctr": "0.05"},
            {"date": "20261102", "video_id": "a", "video_thumbnail_impressions": "300", "video_thumbnail_impressions_ctr": "0.01"},
            {"date": "20261102", "video_id": "a", "video_thumbnail_impressions": "300", "video_thumbnail_impressions_ctr": "0.01"},   # 같은 줄 — 한 번만
            {"date": "20261101", "video_id": "b", "video_thumbnail_impressions": "", "video_thumbnail_impressions_ctr": "0.5"},        # 빈 값 — 뺌
            {"date": "20261101", "video_id": "b", "video_thumbnail_impressions": "10", "video_thumbnail_impressions_ctr": "0"}]
    S = summarize(rows)
    assert S["videos"]["a"] == {"impressions": 400, "clicks": 8.0, "ctr": 0.02, "days": 2}, S       # (100×0.05 + 300×0.01) ÷ 400 = 2% (클릭률 평균 3% 가 아님)
    assert S["videos"]["b"] == {"impressions": 10, "clicks": 0.0, "ctr": 0.0, "days": 1} and S["bad_rows"] == 1 and list(S["videos"]) == ["a", "b"], S
    assert summarize([])["rows"] == 0
    print("[SELFTEST] ok — summarize(가중 클릭률·중복 줄·빈 값)")
    return 0


def main(argv: list[str]) -> int:
    if "--selftest" in argv:
        return selftest()
    if len(argv) < 2 or argv[1] not in ("list", "fetch"):
        print(__doc__ or "쓰기: python3 tools/yt_reach.py <주제> list|fetch  ·  --selftest"); return 1
    topic, cmd = argv[0], argv[1]
    t0 = time.time()
    tok = token()
    check_channel(topic, tok)
    log("START", tool=f"yt_reach.py {VERSION}", topic=topic, cmd=cmd)
    rc = (len(jobs(tok)) == 0) if cmd == "list" else fetch(topic, tok)
    log("DONE", sec=round(time.time() - t0, 1))
    return int(rc)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
