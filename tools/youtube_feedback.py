#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-11 — 최초 작성 (사용자 지시: "올린 영상의 통계 자료로 피드백할 수 있는 자료를 만들어 저장소에 올리는 코드")
#          올린 영상(youtube.json)마다 공개 지표·시청 지속·유입 경로·일별 조회·댓글을 모아 stats/<날짜>.json(원자료)과
#          feedback.md(대본 문장·챕터에 맞춘 자료)를 만들고, 주제별 모음 <주제>/feedback.md, --push 로 main에 올림. 표준 라이브러리만
r"""
유튜브에 올린 영상의 통계를 모아 **피드백용 자료**를 만듭니다. 해석(분석)은 하지 않고, 숫자를 대본 문장·챕터에 맞춰 정리만 합니다.

  python tools/youtube_feedback.py --check                     # 키·권한으로 무엇을 받을 수 있는지만 확인 (통계는 받지 않음)
  python tools/youtube_feedback.py stock                       # stock 주제에서 올린 영상(youtube.json 있음) 전부
  python tools/youtube_feedback.py stock bittu-2026-10         # 영상 하나
  python tools/youtube_feedback.py --all --push                # 모든 주제 → 결과 파일만 main에 커밋·푸시
  옵션: --refresh (오늘 받은 자료가 있어도 다시 받음) · --comments 20 (댓글 수, 0이면 안 받음) · --dry-run (파일·푸시 없이 확인만)
        --log-level DEBUG|INFO|WARNING

만드는 파일 (<주제폴더>/ 기준, 자동 생성이라 직접 고치지 않음):
  source/<영상ID>/stats/<YYYY-MM-DD>.json   그날(한국 날짜) 받은 원자료. 같은 날 다시 실행하면 API를 부르지 않고 이 파일을 다시 씀
  source/<영상ID>/feedback.md               영상 하나의 피드백 자료: 핵심 지표 · 수집일별 추이 · 시청 지속(빠진 구간 → 그때 대본 문장·챕터)
                                            · 챕터별 유지율 · 유입 경로 · 일별 조회 · 댓글(작성자 이름은 저장하지 않음)
  feedback.md                               주제의 영상들을 한 표로 (영상마다 가장 최근 원자료)

받는 자료와 필요한 키 (클라우드 환경 변수 — 값은 출력·커밋하지 않음):
  공개 지표(조회수·좋아요·댓글 수·공개 상태·길이)  YouTube Data API v3 — OAuth(youtube / youtube.readonly / youtube.force-ssl)면 비공개 영상도,
                                                  없으면 YOUTUBE_API_KEY 로 공개 영상만
  상세 분석(시청 시간·평균 시청 비율·시청 지속 곡선·유입 경로·일별·구독 증감)
                                                  YouTube Analytics API v2 — OAuth 권한 yt-analytics.readonly 필요.
                                                  ① Google Cloud(업로드용 프로젝트)에서 "YouTube Analytics API" 사용 설정
                                                  ② 내 PC에서 tools/youtube_auth.py(v1.1)를 다시 실행 → 동의 화면의 권한 체크 칸을 **모두** 체크
                                                  ③ 새 YOUTUBE_REFRESH_TOKEN 을 환경 설정에 넣고 새 세션
  댓글                                            YOUTUBE_API_KEY(공개 영상) 또는 OAuth
  이 도구가 받지 않는 것: 노출수·노출 클릭률(CTR), 썸네일·제목 테스트 결과 → 스튜디오 → 분석 → 도달범위

주의: 저장소가 공개라서 올린 통계·댓글 내용은 누구나 볼 수 있다. 날짜는 Analytics API 기준(미국 태평양 시간)이고, 분석 숫자는 보통 1~3일 늦게 들어온다.
연구·교육용 자료이며 투자 권유가 아니다.
"""
import argparse
import json
import logging
import math
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

try:
    from zoneinfo import ZoneInfo
    PT = ZoneInfo("America/Los_Angeles")
except Exception:                                   # tzdata 가 없는 환경: 태평양 표준시 고정 (날짜가 하루 어긋날 수 있음 — 로그로 알림)
    PT = timezone(timedelta(hours=-8))

sys.path.insert(0, str(Path(__file__).resolve().parent))
import srt_tool  # noqa: E402  — 대본 문장·SRT 시간 (같은 문장 번호 규칙)

VERSION = "v1.0"
ROOT = Path(__file__).resolve().parent.parent
KST = timezone(timedelta(hours=9))
TOKEN_URL = "https://oauth2.googleapis.com/token"
DATA_API = "https://www.googleapis.com/youtube/v3"
ANALYTICS_API = "https://youtubeanalytics.googleapis.com/v2/reports"
SCOPE = "https://www.googleapis.com/auth/"
DATA_SCOPES = {SCOPE + s for s in ("youtube", "youtube.readonly", "youtube.force-ssl", "youtubepartner")}
ANALYTICS_SCOPES = {SCOPE + s for s in ("yt-analytics.readonly", "yt-analytics-monetary.readonly", "youtube",
                                        "youtube.readonly", "youtubepartner")}
TOTAL_METRICS = ("views,estimatedMinutesWatched,averageViewDuration,averageViewPercentage,likes,comments,shares,"
                 "subscribersGained,subscribersLost")
DAILY_DAYS = 14          # feedback.md 일별 표에 보이는 날 수 (원자료에는 전부)
TOP_DROPS, TOP_RISES = 5, 3
PUSH_TRIES = 4
TRAFFIC_KO = {
    "YT_SEARCH": "유튜브 검색", "RELATED_VIDEO": "추천 동영상", "SUGGESTED": "추천 동영상", "BROWSE": "탐색(홈·구독 피드)",
    "SUBSCRIBER": "구독 피드", "NOTIFICATION": "알림", "CHANNEL": "채널 페이지", "PLAYLIST": "재생목록",
    "YT_PLAYLIST_PAGE": "재생목록 페이지", "EXT_URL": "외부", "NO_LINK_OTHER": "직접·알 수 없음", "NO_LINK_EMBEDDED": "삽입 재생",
    "SHORTS": "쇼츠 피드", "YT_OTHER_PAGE": "기타 유튜브", "END_SCREEN": "최종 화면", "ANNOTATION": "카드·주석",
    "CAMPAIGN_CARD": "캠페인 카드", "HASHTAGS": "해시태그", "ADVERTISING": "광고", "LIVE_REDIRECT": "라이브 리디렉션",
    "PRODUCT_PAGE": "제품 페이지", "SOUND_PAGE": "사운드 페이지", "VIDEO_REMIXES": "리믹스", "YT_CHANNEL": "채널 페이지",
}

LOG = logging.getLogger("feedback")


# ----------------------------------------------------------------------------- 로그
def _fmt(v):
    if isinstance(v, float):
        return f"{v:.3f}".rstrip("0").rstrip(".") if math.isfinite(v) else str(v)
    s = str(v)
    return f'"{s}"' if (" " in s or not s) else s


def log(stage, level=logging.INFO, **kv):
    """[STAGE] [TIMESTAMP] key=value ... (공통 로그 형식)"""
    LOG.log(level, "[%s] [%s] %s", stage, datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            " ".join(f"{k}={_fmt(v)}" for k, v in kv.items()))


def rel(p, root=ROOT):
    try:
        return str(Path(p).resolve().relative_to(Path(root).resolve()))
    except ValueError:
        return str(p)


# ----------------------------------------------------------------------------- 작은 계산
def parse_iso_duration(s):
    """'PT7M38S' · 'PT1H2M3S' · 'P0D' → 초. 읽을 수 없으면 None."""
    m = re.fullmatch(r"P(?:(\d+)D)?(?:T(?:(\d+)H)?(?:(\d+)M)?(?:(\d+(?:\.\d+)?)S)?)?", s or "")
    if not m:
        return None
    d, h, mi, se = (float(x) if x else 0.0 for x in m.groups())
    return d * 86400 + h * 3600 + mi * 60 + se


def table(resp):
    """Analytics 응답(columnHeaders + rows) → [{열 이름: 값}]. 행이 없으면 []."""
    names = [c["name"] for c in resp.get("columnHeaders", [])]
    return [dict(zip(names, row)) for row in resp.get("rows") or []]


def mmss(t):
    t = int(round(t or 0))
    return f"{t // 3600}:{t % 3600 // 60:02d}:{t % 60:02d}" if t >= 3600 else f"{t // 60}:{t % 60:02d}"


def num(v, digits=0):
    if v is None:
        return "—"
    return f"{v:,.{digits}f}" if isinstance(v, float) and digits else f"{int(round(v)):,}"


def pct(v, digits=1):
    return "—" if v is None else f"{v * 100:.{digits}f}%"


def fixed(v, digits=1, unit=""):
    """이미 계산된 값 → '12.3%' 같은 글자 (None 이면 —)."""
    return "—" if v is None else f"{v:.{digits}f}{unit}"


def per_k(part, views):
    return None if part is None or not views else part * 1000 / views


def interp(points, t):
    """시간 t의 남은 시청자 비율 (points: t 오름차순, 선형 보간, 범위 밖은 끝값)."""
    if not points:
        return None
    if t <= points[0]["t"]:
        return points[0]["w"]
    for a, b in zip(points, points[1:]):
        if a["t"] <= t <= b["t"]:
            return a["w"] if b["t"] == a["t"] else a["w"] + (b["w"] - a["w"]) * (t - a["t"]) / (b["t"] - a["t"])
    return points[-1]["w"]


def retention_points(rows, duration):
    """elapsedVideoTimeRatio 행 → [{r, t(초), w(남은 비율), rel(비슷한 길이 영상 대비 0~1)}] (r 오름차순)."""
    pts = [{"r": float(x["elapsedVideoTimeRatio"]), "w": float(x["audienceWatchRatio"]),
            "rel": None if x.get("relativeRetentionPerformance") is None else float(x["relativeRetentionPerformance"])}
           for x in rows]
    pts.sort(key=lambda p: p["r"])
    for p in pts:
        p["t"] = p["r"] * duration
    return pts


def checkpoints(points, duration):
    out = []
    for label, t in (("0:30", 30), ("1:00", 60), ("25%", duration * .25), ("50%", duration * .5), ("75%", duration * .75),
                     ("끝", points[-1]["t"] if points else duration)):
        if t <= duration:
            near = min(points, key=lambda p: abs(p["t"] - t)) if points else None
            out.append({"label": label, "t": t, "w": interp(points, t), "rel": near["rel"] if near else None})
    return out


def moves(points, k, falling=True):
    """이웃한 두 점 사이 변화가 가장 큰 구간 k개 (falling: 가장 많이 빠진 구간, 아니면 가장 많이 오른 구간)."""
    steps = [{"t0": a["t"], "t1": b["t"], "w0": a["w"], "w1": b["w"], "d": b["w"] - a["w"]} for a, b in zip(points, points[1:])]
    steps = [s for s in steps if (s["d"] < 0 if falling else s["d"] > 0)]
    steps.sort(key=lambda s: s["d"] if falling else -s["d"])
    return steps[:k]


def chapter_rows(points, chapters, duration):
    out = []
    for i, (t0, title) in enumerate(chapters):
        t1 = chapters[i + 1][0] if i + 1 < len(chapters) else duration
        w0, w1 = interp(points, t0), interp(points, t1)
        loss = None if w0 is None or w1 is None else (w0 - w1) * 100
        mins = (t1 - t0) / 60
        out.append({"title": title, "t0": t0, "t1": t1, "w0": w0, "w1": w1, "loss_pp": loss,
                    "loss_pp_per_min": None if loss is None or mins <= 0 else loss / mins})
    return out


def chapter_at(chapters, t):
    cur = chapters[0][1] if chapters else "—"
    for t0, title in chapters:
        if t0 <= t:
            cur = title
    return cur


def sentences_between(timeline, t0, t1):
    return [s for s in timeline if s["start"] < t1 and s["end"] > t0]


def clip(text, n=60):
    text = " ".join(str(text).split())
    return text if len(text) <= n else text[:n - 1] + "…"


def md_cell(text):
    return str(text).replace("|", "｜").replace("\n", " ")


# ----------------------------------------------------------------------------- 저장소 읽기
def uploaded_videos(root, topic=None, vid=None):
    """youtube.json 이 있는 영상 → [(주제, 영상ID, youtube.json 내용)]."""
    out = []
    for p in sorted(Path(root).glob("*/source/*/youtube.json")):
        t, v = p.parent.parent.parent.name, p.parent.name
        if (topic and t != topic) or (vid and v != vid):
            continue
        out.append((t, v, json.loads(p.read_text("utf-8"))))
    return out


def sentence_parts(txt):
    """srt_tool.parse_txt 와 같은 순서로 문장마다 파트 라벨 (예: '사연 파트')."""
    out, label, in_card = [], "", False
    for raw in Path(txt).read_text("utf-8-sig").splitlines():
        line = raw.strip()
        if not line:
            continue
        if srt_tool.is_label(line):
            label, in_card = line.lstrip("-").strip(), False
            continue
        if line.startswith("[장면]"):
            in_card = True
            continue
        if not in_card:
            out.append(label)
    return out


def load_timeline(root, topic, vid):
    """대본 문장 → 영상 시간 (SRT = 영상 시간). [{n, part, text, start, end}]. 맞지 않으면 [] (경고 로그)."""
    src = Path(root) / topic / "source" / vid
    txt, srt = src / f"{vid}.txt", src / f"{vid}.srt"
    if not txt.is_file() or not srt.is_file():
        log("TIMELINE", logging.WARNING, video=vid, note="대본 TXT·SRT 없음 → 시청 지속을 문장에 맞추지 않음")
        return []
    sents, subs = srt_tool.parse_txt(txt), srt_tool.parse_srt(srt)
    groups, problems = srt_tool.group(subs, sents)
    parts = sentence_parts(txt)
    if problems or len(parts) != len(groups):
        log("TIMELINE", logging.WARNING, video=vid, problems=len(problems), parts=len(parts), groups=len(groups),
            note="대본과 SRT가 다름 → 시청 지속을 문장에 맞추지 않음 (srt_tool.py check 로 확인)")
        return []
    tl = [{"n": g["n"], "part": p, "text": g["text"], "start": g["start"], "end": g["end"]} for g, p in zip(groups, parts)]
    log("TIMELINE", video=vid, sentences=len(tl), end_s=tl[-1]["end"] if tl else 0)
    return tl


def parse_chapters(rec):
    """youtube.json 의 chapters ['0:00 제목', '1:37 …'] → [(초, 제목)]."""
    out = []
    for line in rec.get("chapters") or []:
        m = re.match(r"^(\d+):(\d\d)(?::(\d\d))?\s+(.*)$", line.strip())
        if m:
            a, b, c = int(m.group(1)), int(m.group(2)), m.group(3)
            out.append((a * 3600 + b * 60 + int(c) if c else a * 60 + b, m.group(4)))
    return out


def load_history(stats_dir):
    out = []
    for p in sorted(Path(stats_dir).glob("*.json")):
        try:
            out.append(json.loads(p.read_text("utf-8")))
        except ValueError:
            log("HISTORY", logging.WARNING, file=p.name, note="읽을 수 없는 원자료 — 건너뜀")
    return out


# ----------------------------------------------------------------------------- API
class ApiError(Exception):
    def __init__(self, code, reason, message):
        super().__init__(f"HTTP {code} {reason}: {message}")
        self.code, self.reason, self.message = code, reason, message


def http_json(url, params=None, token=None, data=None, retries=4):
    """GET(또는 data가 있으면 POST) → JSON. 5xx·네트워크 오류는 2·4·8·16초 뒤 다시. 키·토큰은 로그에 남기지 않는다."""
    full = url + ("?" + urllib.parse.urlencode(params) if params else "")
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(urllib.request.Request(full, data=data, headers=headers), timeout=60) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            body = e.read().decode(errors="replace")
            try:
                err = json.loads(body).get("error", {})
                if isinstance(err, str):                      # 토큰 엔드포인트: {"error": "invalid_grant", ...}
                    reason, msg = err, json.loads(body).get("error_description", "")
                else:
                    reason, msg = ((err.get("errors") or [{}])[0].get("reason", "")), err.get("message", "")
            except ValueError:
                reason, msg = "", body[:200]
            if e.code in (500, 502, 503, 504) and attempt < retries:
                log("HTTP", logging.WARNING, status=e.code, retry_in_s=2 ** (attempt + 1), url=url)
                time.sleep(2 ** (attempt + 1))
                continue
            raise ApiError(e.code, reason, msg[:300]) from None
        except urllib.error.URLError as e:
            if attempt < retries:
                log("HTTP", logging.WARNING, error=str(e.reason)[:80], retry_in_s=2 ** (attempt + 1), url=url)
                time.sleep(2 ** (attempt + 1))
                continue
            raise ApiError(0, "network", str(e.reason)[:300]) from None


class Live:
    """실제 YouTube API. plan: 무엇을 어떤 키로 받는지 (data: oauth|api_key|none, analytics: bool, comments: api_key|oauth|none)."""

    def __init__(self, api_key="", token=None, scopes=(), auth_note=""):
        self.api_key, self.token, self.scopes, self.auth_note = api_key, token, set(scopes), auth_note
        oauth_data = bool(token and self.scopes & DATA_SCOPES)
        self.plan = {"data": "oauth" if oauth_data else ("api_key" if api_key else "none"),
                     "analytics": bool(token and self.scopes & ANALYTICS_SCOPES),
                     "comments": "api_key" if api_key else ("oauth" if oauth_data else "none")}

    @classmethod
    def from_env(cls, env=None):
        env = env or os.environ
        api_key = env.get("YOUTUBE_API_KEY", "").strip()
        need = ("YOUTUBE_CLIENT_ID", "YOUTUBE_CLIENT_SECRET", "YOUTUBE_REFRESH_TOKEN")
        missing = [k for k in need if not env.get(k, "").strip()]
        if missing:
            return cls(api_key, None, (), f"OAuth 환경변수 없음: {','.join(missing)}")
        body = urllib.parse.urlencode({"client_id": env["YOUTUBE_CLIENT_ID"].strip(),
                                       "client_secret": env["YOUTUBE_CLIENT_SECRET"].strip(),
                                       "refresh_token": env["YOUTUBE_REFRESH_TOKEN"].strip(),
                                       "grant_type": "refresh_token"}).encode()
        try:
            tok = http_json(TOKEN_URL, data=body, retries=2)
        except ApiError as e:
            hint = " → 토큰 만료·취소: youtube_auth.py 다시" if e.reason == "invalid_grant" else ""
            return cls(api_key, None, (), f"OAuth 토큰 갱신 실패 ({e.code} {e.reason}){hint}")
        return cls(api_key, tok.get("access_token"), (tok.get("scope") or "").split(), "ok")

    def _auth(self, kind):
        return ({"key": self.api_key}, None) if kind == "api_key" else ({}, self.token)

    def videos(self, ids):
        extra, token = self._auth(self.plan["data"])
        resp = http_json(f"{DATA_API}/videos", {"part": "snippet,statistics,status,contentDetails", "id": ",".join(ids),
                                                "maxResults": 50, **extra}, token)
        return resp.get("items", [])

    def report(self, params):
        return http_json(ANALYTICS_API, {"ids": "channel==MINE", **params}, self.token)

    def comments(self, video_id, n):
        extra, token = self._auth(self.plan["comments"])
        resp = http_json(f"{DATA_API}/commentThreads", {"part": "snippet", "videoId": video_id, "order": "relevance",
                                                        "maxResults": max(1, min(100, n)), "textFormat": "plainText",
                                                        **extra}, token)
        return resp.get("items", [])


# ----------------------------------------------------------------------------- 모으기
def analytics_period(rec, now):
    """공개일(태평양 시간 날짜) ~ 오늘(태평양 시간). Analytics API 날짜는 태평양 시간 기준."""
    base = rec.get("publishAt") or rec.get("uploadedAt")
    start = datetime.fromisoformat(base.replace("Z", "+00:00")).astimezone(PT).date() if base else now.astimezone(PT).date()
    end = now.astimezone(PT).date()
    return str(min(start, end)), str(end)


def collect(src, topic, vid, rec, now, n_comments=20):
    """API에서 영상 하나의 원자료를 모은다 (각 부분은 따로 실패할 수 있음 — 실패는 sources·warnings 에 남김)."""
    yid = rec["videoId"]
    snap = {"tool": f"youtube_feedback.py {VERSION}", "collected_at": now.isoformat(timespec="seconds"),
            "collected_kst": now.astimezone(KST).strftime("%Y-%m-%d %H:%M"),
            "video": {"topic": topic, "id": vid, "youtubeId": yid, "title": rec.get("title"), "publishAt": rec.get("publishAt"),
                      "uploadedAt": rec.get("uploadedAt")},
            "sources": {}, "public": None, "analytics": None, "comments": None, "warnings": []}
    W = snap["warnings"]

    # 1) 공개 지표 (Data API)
    if src.plan["data"] == "none":
        snap["sources"]["data"] = "키 없음 (YOUTUBE_API_KEY 또는 OAuth youtube 권한)"
    else:
        try:
            items = src.videos([yid])
            snap["sources"]["data"] = src.plan["data"]
            if not items:
                W.append("Data API에서 영상이 보이지 않음 — API 키는 공개 영상만 본다 (아직 비공개이거나 비공개 잠김)")
            else:
                it = items[0]
                st, stt, cd = it.get("statistics", {}), it.get("status", {}), it.get("contentDetails", {})
                snap["public"] = {"privacyStatus": stt.get("privacyStatus"), "publishAt": stt.get("publishAt"),
                                  "publishedAt": it.get("snippet", {}).get("publishedAt"),
                                  "duration_s": parse_iso_duration(cd.get("duration")),
                                  "viewCount": _int(st.get("viewCount")), "likeCount": _int(st.get("likeCount")),
                                  "commentCount": _int(st.get("commentCount"))}
                pa = rec.get("publishAt")
                if pa and stt.get("privacyStatus") == "private" and datetime.fromisoformat(pa.replace("Z", "+00:00")) < now:
                    W.append("예약 공개 시각이 지났는데 아직 비공개 — 감사 전 API 프로젝트의 비공개 잠김일 수 있음 → 스튜디오 확인 "
                             "(guides/pipeline.md 4단계 '업로드 주의')")
        except ApiError as e:
            snap["sources"]["data"] = f"실패: {e}"
    log("COLLECT", video=vid, part="public", source=snap["sources"]["data"],
        views=(snap["public"] or {}).get("viewCount", "—"), status=(snap["public"] or {}).get("privacyStatus", "—"))

    # 2) 상세 분석 (Analytics API)
    if not src.plan["analytics"]:
        snap["sources"]["analytics"] = ("권한 없음 — OAuth 에 yt-analytics.readonly 가 없음 → Google Cloud 'YouTube Analytics API' 사용 설정 + "
                                        "tools/youtube_auth.py 다시 실행(권한 모두 체크) → 새 YOUTUBE_REFRESH_TOKEN")
    else:
        start, end = analytics_period(rec, now)
        A = {"period": {"start": start, "end": end, "timezone": "America/Los_Angeles"}}
        base = {"startDate": start, "endDate": end, "filters": f"video=={yid}"}
        queries = {"totals": {"metrics": TOTAL_METRICS},
                   "daily": {"metrics": "views,estimatedMinutesWatched,averageViewDuration", "dimensions": "day", "sort": "day"},
                   "retention": {"metrics": "audienceWatchRatio,relativeRetentionPerformance", "dimensions": "elapsedVideoTimeRatio"},
                   "traffic": {"metrics": "views,estimatedMinutesWatched", "dimensions": "insightTrafficSourceType", "sort": "-views"}}
        errors = []
        for key, q in queries.items():
            try:
                rows = table(src.report({**base, **q}))
                A[key] = (rows[0] if rows else None) if key == "totals" else rows
            except ApiError as e:
                A[key] = None
                errors.append(f"{key}: {e}")
        snap["analytics"] = A
        snap["sources"]["analytics"] = "ok" if not errors else "일부 실패: " + " / ".join(errors)
        if not errors and not A.get("totals") and not A.get("retention"):
            W.append("상세 분석에 아직 숫자가 없음 — 보통 공개 뒤 1~3일 걸린다")
        log("COLLECT", video=vid, part="analytics", period=f"{start}~{end}", totals="있음" if A.get("totals") else "없음",
            retention_points=len(A.get("retention") or []), traffic_rows=len(A.get("traffic") or []),
            daily_rows=len(A.get("daily") or []), errors=len(errors))

    # 3) 댓글 (작성자 이름은 저장하지 않음 — 저장소가 공개)
    if n_comments <= 0:
        snap["sources"]["comments"] = "건너뜀 (--comments 0)"
    elif src.plan["comments"] == "none":
        snap["sources"]["comments"] = "키 없음"
    else:
        try:
            items = src.comments(yid, n_comments)
            snap["comments"] = [{"text": clip(c["snippet"]["topLevelComment"]["snippet"].get("textDisplay", ""), 300),
                                 "likes": _int(c["snippet"]["topLevelComment"]["snippet"].get("likeCount")),
                                 "replies": _int(c["snippet"].get("totalReplyCount")),
                                 "publishedAt": c["snippet"]["topLevelComment"]["snippet"].get("publishedAt")}
                                for c in items[:n_comments]]
            snap["sources"]["comments"] = src.plan["comments"]
        except ApiError as e:
            snap["sources"]["comments"] = f"실패: {e}"
        log("COLLECT", video=vid, part="comments", source=snap["sources"]["comments"][:60],
            count=len(snap["comments"] or []))
    for w in W:
        log("CHECK", logging.WARNING, video=vid, warning=w)
    return snap


def _int(v):
    try:
        return int(v)
    except (TypeError, ValueError):
        return None


# ----------------------------------------------------------------------------- 문서 만들기
def video_duration(snap, timeline):
    d = (snap.get("public") or {}).get("duration_s")
    tl_end = timeline[-1]["end"] + 1.0 if timeline else None
    return d or tl_end, (d, tl_end)


def summarize(snap, timeline, chapters):
    """원자료 → 표에 쓸 값 (feedback.md 와 주제 모음이 같이 쓴다). 해석 없이 계산만."""
    dur, (api_d, tl_d) = video_duration(snap, timeline)
    A = snap.get("analytics") or {}
    T = A.get("totals") or {}
    P = snap.get("public") or {}
    pts = retention_points(A.get("retention") or [], dur) if dur and A.get("retention") else []
    chaps = chapter_rows(pts, chapters, dur) if pts and chapters else []
    traffic = A.get("traffic") or []
    tv = sum(r.get("views") or 0 for r in traffic)
    views = T.get("views") if T else P.get("viewCount")
    pub = snap["video"].get("publishAt") or snap["video"].get("uploadedAt")
    days = None
    if pub:
        days = (datetime.fromisoformat(snap["collected_at"]) - datetime.fromisoformat(pub.replace("Z", "+00:00"))).total_seconds() / 86400
    worst = max((c for c in chaps if c["loss_pp_per_min"] is not None), key=lambda c: c["loss_pp_per_min"], default=None)
    return {"duration": dur, "duration_api": api_d, "duration_srt": tl_d, "totals": T, "public": P, "points": pts,
            "chapters": chaps, "traffic": traffic, "traffic_views": tv, "views": views, "days": days,
            "top_traffic": (TRAFFIC_KO.get(traffic[0]["insightTrafficSourceType"], traffic[0]["insightTrafficSourceType"])
                            if traffic else None),
            "worst_chapter": worst}


def render_feedback(snap, timeline, chapters, history):
    v, S = snap["video"], summarize(snap, timeline, chapters)
    T, P, A = S["totals"], S["public"], snap.get("analytics") or {}
    yid = v["youtubeId"]
    L = [f"# 피드백 자료 — {v.get('title') or v['id']}", "",
         f"> 자동 생성: `tools/youtube_feedback.py` {VERSION} · 수집 {snap['collected_kst']} (한국 시간). 직접 고치지 않는다 — 다시 실행하면 덮어쓴다.",
         "> 숫자를 대본 문장·챕터에 맞춰 정리한 자료이고 해석은 담지 않는다. 연구·교육용이며 투자 권유가 아니다.", ""]
    pub = v.get("publishAt")
    pub_txt = (datetime.fromisoformat(pub.replace("Z", "+00:00")).astimezone(KST).strftime("%Y-%m-%d %H:%M") + " (한국 시간) 예약"
               if pub else "예약 없음")
    period = A.get("period") or {}
    L += ["| 항목 | 값 |", "|---|---|",
          f"| 영상 | `{v['id']}` · [{yid}](https://youtu.be/{yid}) · [스튜디오](https://studio.youtube.com/video/{yid}/analytics) |",
          f"| 공개 | {pub_txt} · 지금 상태 {P.get('privacyStatus') or '모름'}"
          + (f" · 공개 뒤 {S['days']:.1f}일" if S["days"] is not None and S["days"] >= 0 else "") + " |",
          f"| 영상 길이 | {mmss(S['duration']) if S['duration'] else '—'} |",
          f"| 받은 자료 | 공개 지표: {snap['sources'].get('data', '—')} · 상세 분석: {snap['sources'].get('analytics', '—')}"
          + (f" ({period.get('start')} ~ {period.get('end')}, 날짜는 미국 태평양 시간)" if period else "")
          + f" · 댓글: {snap['sources'].get('comments', '—')} |", ""]
    warns = list(snap.get("warnings") or [])
    if S["duration_api"] and S["duration_srt"] and abs(S["duration_api"] - S["duration_srt"]) > 3:
        warns.append(f"영상 길이(API {mmss(S['duration_api'])})와 자막 끝({mmss(S['duration_srt'])})이 3초 넘게 다름 — 문장 위치가 조금 어긋날 수 있음")
    if not timeline:
        warns.append("대본·SRT를 읽지 못해 시청 지속을 문장에 맞추지 못함")
    if warns:
        L += ["## 주의", ""] + [f"- ⚠️ {md_cell(w)}" for w in warns] + [""]

    # 1. 핵심 지표
    L += ["## 1. 핵심 지표", ""]
    if T or P:
        views = S["views"]
        dur = S["duration"]
        avd = T.get("averageViewDuration")
        subs_net = None if not T else (T.get("subscribersGained") or 0) - (T.get("subscribersLost") or 0)
        rows = [("조회수", num(views), "상세 분석" if T else "공개 지표"),
                ("시청 시간", f"{num(T.get('estimatedMinutesWatched') / 60, 1)}시간" if T.get("estimatedMinutesWatched") is not None else "—", ""),
                ("평균 시청 시간", mmss(avd) if avd is not None else "—", f"영상 길이의 {pct(avd / dur)}" if avd is not None and dur else ""),
                ("평균 시청 비율", f"{T['averageViewPercentage']:.1f}%" if T.get("averageViewPercentage") is not None else "—", "YouTube 계산값"),
                ("좋아요", num(T.get("likes") if T else P.get("likeCount")), f"천 회당 {num(per_k(T.get('likes') if T else P.get('likeCount'), views), 1)}"),
                ("댓글", num(T.get("comments") if T else P.get("commentCount")), f"천 회당 {num(per_k(T.get('comments') if T else P.get('commentCount'), views), 1)}"),
                ("공유", num(T.get("shares")), f"천 회당 {num(per_k(T.get('shares'), views), 1)}" if T else ""),
                ("구독자", f"+{num(T.get('subscribersGained'))} / −{num(T.get('subscribersLost'))}" if T else "—",
                 f"순증 천 회당 {num(per_k(subs_net, views), 2)}" if T else "")]
        L += ["| 지표 | 값 | 참고 |", "|---|---|---|"] + [f"| {a} | {b} | {c} |" for a, b, c in rows]
        if T and P.get("viewCount") is not None:
            L += ["", f"공개 지표(Data API, 수집 시각 기준): 조회수 {num(P.get('viewCount'))} · 좋아요 {num(P.get('likeCount'))} · 댓글 {num(P.get('commentCount'))}"
                  " — 상세 분석은 하루 이상 늦게 집계되어 다를 수 있다."]
    else:
        L += ["자료 없음 (위 '받은 자료' 참고)."]
    L += [""]

    # 2. 수집일별 추이
    L += ["## 2. 수집일별 추이", "", "| 수집 (한국 시간) | 공개 뒤 | 조회수 | 평균 시청 비율 | 좋아요 | 댓글 |", "|---|---|---|---|---|---|"]
    for h in sorted(history + ([snap] if snap not in history else []), key=lambda s: s["collected_at"]):
        hs = summarize(h, [], [])
        ht, hp = hs["totals"], hs["public"]
        L.append(f"| {h['collected_kst']} | {fixed(hs['days'], 1, '일')} | {num(hs['views'])} | "
                 f"{fixed(ht.get('averageViewPercentage'), 1, '%')} | "
                 f"{num(ht.get('likes') if ht else hp.get('likeCount'))} | {num(ht.get('comments') if ht else hp.get('commentCount'))} |")
    L += [""]

    # 3. 시청 지속
    pts = S["points"]
    L += ["## 3. 시청 지속 (audience retention)", ""]
    if not pts:
        L += ["자료 없음 (상세 분석 권한이 없거나 아직 집계 전).", ""]
    else:
        L += ["남은 시청자 = 그 시점까지 보고 있는 비율(다시 본 경우 100%를 넘을 수 있음). 비슷한 길이 영상 대비 = 0.5가 중간, 1에 가까울수록 높음.", "",
              "| 시점 | 영상 시간 | 남은 시청자 | 비슷한 길이 영상 대비 | 챕터 |", "|---|---|---|---|---|"]
        for c in checkpoints(pts, S["duration"]):
            L.append(f"| {c['label']} | {mmss(c['t'])} | {pct(c['w'])} | {fixed(c['rel'], 2)} | "
                     f"{md_cell(chapter_at(chapters, c['t']))} |")
        for title, k, falling in (("3-1. 가장 많이 빠진 구간", TOP_DROPS, True), ("3-2. 다시 보거나 건너뛰어 온 구간 (오른 곳)", TOP_RISES, False)):
            L += ["", f"### {title}", "", "| # | 구간 | 변화 | 챕터 | 그때 대본 (문장 번호 · 파트) |", "|---|---|---|---|---|"]
            mv = moves(pts, k, falling)
            for i, m in enumerate(mv, 1):
                ss = sentences_between(timeline, m["t0"], m["t1"])
                said = " / ".join(f"{s['n']}. {clip(s['text'])} ({s['part']})" for s in ss) or "(자막 없음 — 고지 카드·앞뒤 여백)"
                L.append(f"| {i} | {mmss(m['t0'])}–{mmss(m['t1'])} | {m['d'] * 100:+.1f}%p ({pct(m['w0'])} → {pct(m['w1'])}) | "
                         f"{md_cell(chapter_at(chapters, m['t0']))} | {md_cell(said)} |")
            if not mv:
                L.append("| — | 없음 | | | |")
        L += ["", "### 3-3. 챕터별 유지", ""]
        if S["chapters"]:
            L += ["| 챕터 | 시작 | 길이 | 시작 때 | 끝날 때 | 빠진 정도 | 1분당 |", "|---|---|---|---|---|---|---|"]
            for c in S["chapters"]:
                L.append(f"| {md_cell(c['title'])} | {mmss(c['t0'])} | {mmss(c['t1'] - c['t0'])} | {pct(c['w0'])} | {pct(c['w1'])} | "
                         f"{fixed(c['loss_pp'], 1, '%p')} | "
                         f"{fixed(c['loss_pp_per_min'], 1, '%p')} |")
        else:
            L += ["챕터 정보 없음 (youtube.json 의 chapters)."]
    L += [""]

    # 4. 유입 경로
    L += ["## 4. 유입 경로", ""]
    if S["traffic"]:
        L += ["| 경로 | 조회수 | 비율 | 시청 시간(분) |", "|---|---|---|---|"]
        for r in S["traffic"]:
            src = r.get("insightTrafficSourceType")
            L.append(f"| {TRAFFIC_KO.get(src, src)} (`{src}`) | {num(r.get('views'))} | "
                     f"{pct((r.get('views') or 0) / S['traffic_views']) if S['traffic_views'] else '—'} | {num(r.get('estimatedMinutesWatched'))} |")
    else:
        L += ["자료 없음."]
    L += [""]

    # 5. 일별
    daily = A.get("daily") or []
    L += [f"## 5. 일별 조회 (처음 {DAILY_DAYS}일, 날짜는 미국 태평양 시간)", ""]
    if daily:
        L += ["| 날짜 | 조회수 | 시청 시간(분) | 평균 시청 시간 |", "|---|---|---|---|"]
        L += [f"| {d.get('day')} | {num(d.get('views'))} | {num(d.get('estimatedMinutesWatched'))} | {mmss(d.get('averageViewDuration'))} |"
              for d in daily[:DAILY_DAYS]]
    else:
        L += ["자료 없음."]
    L += [""]

    # 6. 댓글
    cm = snap.get("comments")
    L += [f"## 6. 댓글 (관련성 순 상위 {len(cm or [])}개, 작성자 이름은 저장하지 않음)", ""]
    if cm:
        L += ["| # | 좋아요 | 답글 | 내용 |", "|---|---|---|---|"]
        L += [f"| {i} | {num(c.get('likes'))} | {num(c.get('replies'))} | {md_cell(clip(c.get('text', ''), 200))} |" for i, c in enumerate(cm, 1)]
    else:
        L += ["자료 없음."]
    L += ["", "## 이 자료에 없는 것 (스튜디오에서 확인)", "",
          "- 노출수·노출 클릭률(CTR), 썸네일·제목 '테스트 및 비교' 결과 → 스튜디오 → 분석 → 도달범위", ""]
    return "\n".join(L)


def render_overview(topic, entries):
    """entries: [(영상ID, 최신 원자료, timeline, chapters)] → 주제 모음 표."""
    L = [f"# {topic} — 올린 영상 피드백 모음", "",
         f"> 자동 생성: `tools/youtube_feedback.py` {VERSION}. 영상마다 가장 최근에 받은 원자료 기준. 영상별 자세한 자료는 `source/<영상ID>/feedback.md`.",
         "> 해석은 담지 않는다. 연구·교육용이며 투자 권유가 아니다.", "",
         "| 영상 | 제목 | 공개 (한국 시간) | 수집 | 공개 뒤 | 조회수 | 평균 시청 비율 | 평균 시청 시간 | 좋아요/천 회 | 구독 순증 | 가장 많은 유입 | 1분당 가장 많이 빠진 챕터 |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for vid, snap, tl, ch in sorted(entries, key=lambda e: e[1]["video"].get("publishAt") or "", reverse=True):
        S = summarize(snap, tl, ch)
        T, P = S["totals"], S["public"]
        pub = snap["video"].get("publishAt")
        likes = T.get("likes") if T else P.get("likeCount")
        net = None if not T else (T.get("subscribersGained") or 0) - (T.get("subscribersLost") or 0)
        wc = S["worst_chapter"]
        wc_txt = f"{md_cell(wc['title'])} ({fixed(wc['loss_pp_per_min'], 1, '%p')})" if wc else "—"
        pub_txt = datetime.fromisoformat(pub.replace("Z", "+00:00")).astimezone(KST).strftime("%m-%d %H:%M") if pub else "—"
        avd = T.get("averageViewDuration")
        L.append(f"| [{vid}](source/{vid}/feedback.md) | {md_cell(clip(snap['video'].get('title') or '', 40))} | {pub_txt} | "
                 f"{snap['collected_kst']} | {fixed(S['days'], 1, '일')} | {num(S['views'])} | "
                 f"{fixed(T.get('averageViewPercentage'), 1, '%')} | {mmss(avd) if avd is not None else '—'} | "
                 f"{num(per_k(likes, S['views']), 1)} | {'—' if net is None else f'{net:+d}'} | {S['top_traffic'] or '—'} | {wc_txt} |")
    return "\n".join(L) + "\n"


# ----------------------------------------------------------------------------- 올리기
def git_push(root, paths, message, tries=PUSH_TRIES, sleep=time.sleep):
    """paths 만 커밋 → pull --rebase → push origin HEAD:main (실패하면 2·4·8·16초 뒤 다시). → 성공 여부."""
    def git(*a):
        r = subprocess.run(["git", "-C", str(root), *a], capture_output=True, text=True)
        return r.returncode, (r.stdout + r.stderr).strip()

    rels = [rel(p, root) for p in paths]
    rc, out = git("add", "--", *rels)
    if rc != 0:
        log("PUSH", logging.ERROR, step="add", error=" ".join(out.split())[:300])
        return False
    rc, _ = git("diff", "--cached", "--quiet", "--", *rels)
    if rc == 0:
        log("PUSH", note="바뀐 결과 없음 — 커밋하지 않음 (못 올린 커밋이 있으면 올림)")
    else:
        rc, out = git("commit", "-q", "-m", message, "--", *rels)
        if rc != 0:
            log("PUSH", logging.ERROR, step="commit", error=" ".join(out.split())[:300])
            return False
    for attempt in range(1, tries + 1):
        rc, out = git("pull", "-q", "--rebase", "--autostash", "origin", "main")
        if rc == 0:
            rc, out = git("push", "-q", "origin", "HEAD:main")
            if rc == 0:
                _, head = git("rev-parse", "--short", "HEAD")
                log("PUSH", status="ok", commit=head, files=len(rels), branch="main")
                return True
        wait = 2 ** attempt
        log("PUSH", logging.WARNING, attempt=attempt, error=" ".join(out.split())[:200], retry_in_s=wait if attempt < tries else 0)
        if attempt < tries:
            sleep(wait)
    log("PUSH", logging.ERROR, note="올리기 실패 — 결과 파일은 저장소에 그대로 있음. 'git push origin HEAD:main' 으로 다시")
    return False


# ----------------------------------------------------------------------------- 실행
def run(root, topic=None, vid=None, refresh=False, n_comments=20, dry_run=False, push=False, source_factory=None, now=None):
    """→ 쓴 파일 목록. source_factory: API 객체를 만드는 함수 (시험에서 가짜로 바꿈). 오늘 원자료가 있으면 부르지 않는다."""
    root = Path(root)
    now = now or datetime.now(timezone.utc)
    today = now.astimezone(KST).strftime("%Y-%m-%d")
    targets = uploaded_videos(root, topic, vid)
    log("SCAN", topic=topic or "전체", video=vid or "전체", uploaded=len(targets), today_kst=today, refresh=refresh, dry_run=dry_run)
    src, written, touched, done = None, [], set(), []
    for t, v, rec in targets:
        pa = rec.get("publishAt")
        if pa and datetime.fromisoformat(pa.replace("Z", "+00:00")) > now:
            log("SKIP", video=v, reason="아직 공개 전", publish_at_kst=datetime.fromisoformat(pa.replace("Z", "+00:00")).astimezone(KST).strftime("%Y-%m-%d %H:%M"))
            continue
        d = root / t / "source" / v
        snap_path = d / "stats" / f"{today}.json"
        if snap_path.is_file() and not refresh:
            snap = json.loads(snap_path.read_text("utf-8"))
            log("CACHE", video=v, file=rel(snap_path, root), note="오늘 받은 원자료를 씀 (API 안 부름, 다시 받으려면 --refresh)")
        else:
            if src is None:
                src = (source_factory or Live.from_env)()
                log("SOURCE", plan=",".join(f"{k}={v_}" for k, v_ in src.plan.items()), auth=getattr(src, "auth_note", "-"))
            snap = collect(src, t, v, rec, now, n_comments)
            if not dry_run:
                snap_path.parent.mkdir(parents=True, exist_ok=True)
                snap_path.write_text(json.dumps(snap, ensure_ascii=False, indent=2) + "\n", "utf-8")
                written.append(snap_path)
        timeline, chapters = load_timeline(root, t, v), parse_chapters(rec)
        history = [h for h in load_history(d / "stats") if h.get("collected_at") != snap.get("collected_at")]
        md = render_feedback(snap, timeline, chapters, history)
        S = summarize(snap, timeline, chapters)
        log("FEEDBACK", video=v, views=S["views"] if S["views"] is not None else "—", retention_points=len(S["points"]),
            chapters=len(S["chapters"]), traffic_rows=len(S["traffic"]), comments=len(snap.get("comments") or []),
            md_lines=md.count("\n") + 1, written="안 함(--dry-run)" if dry_run else rel(d / "feedback.md", root))
        if not dry_run:
            (d / "feedback.md").write_text(md, "utf-8")
            written.append(d / "feedback.md")
        touched.add(t)
        done.append(v)

    for t in sorted(touched):                      # 주제 모음: 올린 영상마다 가장 최근 원자료
        entries = []
        for _, v, rec in uploaded_videos(root, t):
            hist = load_history(root / t / "source" / v / "stats")
            if hist:
                latest = max(hist, key=lambda s: s["collected_at"])
                entries.append((v, latest, load_timeline(root, t, v), parse_chapters(rec)))
        if entries and not dry_run:
            p = root / t / "feedback.md"
            p.write_text(render_overview(t, entries), "utf-8")
            written.append(p)
            log("OVERVIEW", topic=t, videos=len(entries), file=rel(p, root))

    log("DONE", files=len(written), push=push and not dry_run)
    if push and written and not dry_run:
        msg = (f"피드백 자료: {', '.join(done)} (youtube_feedback {VERSION}, 수집 {today} KST)\n\n"
               "자동 생성 — 영상마다 stats/<날짜>.json · feedback.md, 주제별 feedback.md. 연구·교육용, 투자 권유 아님.")
        if not git_push(root, written, msg):
            raise SystemExit(1)
    return written


def check(src, root=ROOT):
    """키·권한으로 무엇을 받을 수 있는지 (통계는 받지 않음). API 키는 videos.list(part=id) 한 번으로 동작만 본다."""
    names = sorted(s.replace(SCOPE, "") for s in src.scopes)
    log("CHECK", api_key="있음" if src.api_key else "없음", oauth=src.auth_note, scopes=",".join(names) or "—")
    log("CHECK", data={"oauth": "OAuth(비공개 영상도)", "api_key": "API 키(공개 영상만)", "none": "불가"}[src.plan["data"]],
        analytics="가능" if src.plan["analytics"] else "불가 → yt-analytics.readonly 권한 필요 (YouTube Analytics API 사용 설정 + youtube_auth.py v1.1 다시)",
        comments={"oauth": "OAuth", "api_key": "API 키", "none": "불가"}[src.plan["comments"]])
    vids = uploaded_videos(root)
    if src.api_key and vids:
        try:
            resp = http_json(f"{DATA_API}/videos", {"part": "id", "id": vids[0][2]["videoId"], "key": src.api_key})
            log("CHECK", api_key_call="ok", probe_video=vids[0][1], visible=len(resp.get("items", [])),
                note="visible=0 이면 아직 비공개(또는 잠김) — API 키는 공개 영상만 봄")
        except ApiError as e:
            log("CHECK", logging.ERROR, api_key_call="실패", error=str(e)[:200])
    return src.plan


def main(argv=None):
    ap = argparse.ArgumentParser(description="올린 영상의 통계로 피드백 자료 만들기 (해석 없음)")
    ap.add_argument("topic", nargs="?", help="주제 폴더 (예: stock). 없으면 --all")
    ap.add_argument("video_id", nargs="?", help="영상 ID (예: bittu-2026-10)")
    ap.add_argument("--all", action="store_true", help="모든 주제")
    ap.add_argument("--check", action="store_true", help="키·권한만 확인 (통계는 받지 않음)")
    ap.add_argument("--refresh", action="store_true", help="오늘 받은 원자료가 있어도 다시 받음")
    ap.add_argument("--comments", type=int, default=20, help="받을 댓글 수 (0이면 안 받음, 최대 100)")
    ap.add_argument("--dry-run", action="store_true", help="파일을 쓰지 않고 푸시도 하지 않음")
    ap.add_argument("--push", action="store_true", help="결과 파일만 main에 커밋·푸시")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args(argv)
    logging.basicConfig(level=a.log_level, format="%(message)s", stream=sys.stdout)
    if a.check:
        check(Live.from_env())
        return 0
    if not a.topic and not a.all:
        ap.error("주제 폴더(예: stock) 또는 --all 이 필요합니다")
    run(ROOT, None if a.all else a.topic, a.video_id, a.refresh, a.comments, a.dry_run, a.push)
    return 0


if __name__ == "__main__":
    sys.exit(main())
