#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.5.2 — 2026-10-28 — 주석만: 페르소나 설정이 있는 주제 = 주식·재테크 (재테크 되살림 — 사용자 지시 "주식 주제 관련 세션에서 했던것처럼 똑같은 방식으로 진행해서 유튜브 분석부터 요약본까지 만들어봐").
# (v1.5.1 — 2026-10-28 — 페르소나는 설정(<주제>/personas.toml)이 있는 주제만 — 지금 주식만 (사용자 지시 "아니 주식 쪽만 하면돼"). 코드 그대로(설정이 없으면 personas.build 가 '만들지 않음'만 남김).
# (v1.5 — 2026-10-28 — 끝날 때 시청자 페르소나(tools/personas.py → personas.md·.json)도 다시 만듦 (사용자 지시 2026-10-28
#          "시청자 페르소나 … 분석 결과에 따라 업데이트도 돼야함"). 실패해도 주별·성공 사례 분석은 저장됨. 그 밖 그대로.)
# (v1.4 — 2026-10-28 — 성공 판정·하루 조회수를 분석(success_analysis v1.6)과 같게: 주제 analysis_rules.toml [success] 를 읽어
#          orr.success_core (MIN_VPD_SUBS > 0 = 구독자당 하루 조회수, 아니면 배수 — 주별 창은 예전처럼 나이 제한 없이) · 하루 조회수 = 받은 때
#          (metadata collected)까지 날수로 (orr.views_per_day). 사용자 지시 2026-10-28 "1은 그렇게하고 … 나머지는 너가 추천하는 방향으로 하고".
# (v1.3.1 — 2026-10-22 — 주마다 '댓글 N개 니즈' 줄에 '어느 갈래에도 안 듦 x%' (갈래 비율만 보이고 나머지 약 59% 가 안 보였음 — 사용자 지시 2026-10-21
#          "… 모든 댓글 유형 나눠서 통계내서 분석하고 있는가 맞아? 일부분 밖에 없는거 같은데"). 모든 댓글 유형은 comment_types.md. 갈래 규칙은 그대로
# (v1.3 — 2026-10-14 — 끝날 때 성공 사례 분석(tools/success_analysis.py → analysis.md — AI 가 지시사항을 만들 재료)도 다시 만듦
#          (사용자 지시: "… 어떤 주제, 어떤 제목, 어떤 썸네일, 내용을 어떻게 구성해야하는지 … 올바른 분석 결과까지만 내도록 수정해").
#          weekly.md 머리에 '이 표는 승인 영상 전부의 추세 — 성공 사례 분석은 analysis.md' 안내 (한 채널 쏠림 보정은 analysis.md 에만))
# (v1.2.1 — 2026-10-14 — 안내 글만: approved.md 의 '사례 폴더는 비공개일 때만' → 공개 저장소에도 올라감 (사용자 지시 "그냥 공개에서 다 올리도록 해"))
# (v1.2 — 2026-10-14 — 자막을 못 받은 영상은 영상 설명으로 대신 분석 (사용자 지시: "음성인식이랑 별개로 분석결과 낼 수 있잖아
#          자막도 다운 시도했는데 안되면 영상 설명으로 대체해서 그냥 분석결과랑 자료 다 올려 그 다음 음성인식하라고 수정해"):
#          ① 영상마다 '글 출처' = 자막 → 음성인식 → 설명(description.txt — 링크·#태그·시각·구독/문의/투자 권유 문구 줄은 뺌) → 없음
#          ② 창마다 글 출처 수(자막·음성인식·설명), 도입부(자막·음성인식은 첫 20초, 없으면 설명 앞부분 — 출처 표시),
#             내용에 자주 나온 낱말(자막·음성인식, 없으면 설명), 타임라인(챕터) 있는 영상 비율
#          ③ approved.md·approved.csv — 승인한 영상 전부 (업로드 날짜 최근 순: 제목·채널·구독자·조회수·배수·글 출처·댓글·썸네일·폴더)
#          ④ 파일은 임시 파일에 쓰고 바꿔치기 (웹 화면과 음성인식이 동시에 다시 만들어도 반쪽 파일이 안 생기게))
# (v1.1 — 2026-10-14 — 승인한 영상이 모두 들어가게 (사용자 질문 "분석 결과 다 올라온거야?" — 승인 289개 중 155개가 12주보다
#          오래돼 어느 창에도 없었음): 창을 최대 52주까지(한 주씩), 그보다 오래된 영상이 있으면 마지막에 '전체' 창을 더함)
# (v1.0 — 2026-10-14 — 신규 (사용자 지시: "목록은 최근에 업로드 된 순으로 하고 1주 전, 2주 전, 3주 전 1주씩 늘리면서 분석 결과 내보도록"):
#          웹 화면(tools/web_ui.py)에서 승인해 자료를 받은 영상(<주제>/result/outliers/W_<영상ID>/)을 업로드 날짜로 묶어
#          '최근 1주 · 최근 2주 · 최근 3주 …' 처럼 한 주씩 넓히며 같은 숫자를 낸다 (누적 창). 창마다:
#          영상·채널 수, 그 주에 새로 들어온 영상, 조회수·하루 조회수·배수(조회수÷구독자) 중앙값, 성공 사례 수, 길이,
#          제목 특징(금액·물음표·N가지 … — tools/outlier_stats.py 와 같은 규칙)·자주 쓴 낱말, 자막(말 속도·첫 20초), 댓글 니즈·인기 댓글, 상위 영상
#          → weekly.md (GitHub 에서 바로 보이는 표) · weekly.json (웹 화면) · weekly.csv)
r"""
사용법 (저장소 최상위 또는 PC 실행 폴더):
  python tools/weekly_analysis.py economic                 # W_ 사례로 weekly.md·json·csv 다시 만듦 (API 요청 없음)
  python tools/weekly_analysis.py economic --max-weeks 26  # 창을 최대 26주까지 (기본 52, 더 오래된 영상은 마지막 '전체' 창)
결과: <주제>/result/outliers/weekly.md·json·csv (주별) · approved.md·csv (승인한 영상 전부 — 글 출처: 자막·음성인식·설명)
글 출처: 자막을 못 받은 영상은 영상 설명으로 대신 분석하고, 음성인식 대본이 생기면 다음 실행부터 그것을 씀.
성공 사례 기준 = 구독자 5만 이하 · 조회수 1만 이상 · 조회수 ≥ 구독자 × 3 (outlier_research 와 같음, 구독자 100 미만은 100).
로그: [STAGE] [시각] key=value (START·WEEKLY·DONE)
※ 연구·교육용. 투자 권유가 아니다.
"""
import argparse
import csv
import json
import logging
import math
import os
import re
import statistics
import sys
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from outlier_stats import COMMENT_CATS, TITLE_FEATURES       # noqa: E402  같은 규칙 (제목 특징·댓글 갈래)
import outlier_research as orr                                # noqa: E402  v1.4: success_core·views_per_day (분석과 같은 규칙)

ROOT = Path(__file__).resolve().parent.parent
VERSION = "v1.5.2"
LOG = logging.getLogger("weekly")
WEB_CASE_RX = re.compile(r"^W_([0-9A-Za-z_-]{11})$")
MAX_SUBS, MIN_RATIO, MIN_VIEWS = 50000, 3.0, 10000
SUCCESS_RULES = {"MAX_AGE_DAYS": 180, "MAX_SUBS": MAX_SUBS, "MIN_RATIO": MIN_RATIO, "MIN_VIEWS": MIN_VIEWS, "MIN_AGE_DAYS": 0, "MIN_VPD_SUBS": 0}   # v1.4: run() 이 주제 [success] 로 덮음
HOOK_SEC = 20
STOPWORDS = set("이 그 저 것 수 등 및 더 왜 다 또 안 못 잘 꼭 진짜 정말 지금 이제 그냥 바로 모든 모두 하는 있는 없는 되는 하면 해서 했다 합니다 입니다 "
                "에서 으로 하고 까지 부터 에게 이런 저런 그런 무조건 반드시 절대 the and for with 영상 채널 구독 라이브".split())
TEXT_SOURCES = ("자막", "음성인식", "설명", "없음")            # 글 출처 (v1.2) — 앞일수록 좋음
DESC_DROP_RX = re.compile(r"https?://|www\.|@|#|\b\d{1,2}:\d{2}\b|구독|좋아요|알림|문의|메일|협찬|광고|제휴|협업|비즈니스|"
                          r"권유|책임|투자 판단|참고용|무단|저작권|인스타|블로그|카카오|오픈채팅|텔레그램|후원|멤버십|링크|출처")
DESC_HOOK_CHARS = 160


def clean_description(desc):
    """영상 설명 → 내용 줄만 (링크·#태그·@·타임라인 시각·구독/문의/광고/투자 권유·책임 문구 줄은 뺌). 분석용 글 (v1.2)."""
    keep = []
    for line in str(desc or "").splitlines():
        line = line.strip(" \t-–—•·*▶►✅✔️📌👉=~|")
        if len(line) < 4 or DESC_DROP_RX.search(line) or not re.search(r"[가-힣A-Za-z]", line):
            continue
        keep.append(line)
    return " ".join(keep).strip()


def log(stage, level=logging.INFO, **kv):
    LOG.log(level, "[%s] [%s] %s", stage, datetime.now().isoformat(timespec="seconds"),
            " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) and ' ' in v else v}" for k, v in kv.items()))


def _published(meta):
    """업로드 시각 (UTC). 'YYYY-MM-DD' 또는 ISO 시각 둘 다. 모르면 None."""
    s = str(meta.get("published_at") or meta.get("published") or "").strip()      # 웹 화면 사례는 시각까지 (published_at)
    if not s:
        return None
    try:
        d = datetime.fromisoformat(s.replace("Z", "+00:00")) if "T" in s else datetime.fromisoformat(s[:10])
    except ValueError:
        return None
    return d if d.tzinfo else d.replace(tzinfo=timezone.utc)


def load_cases(out_dir):
    """W_<영상ID> 폴더 → 사례 목록 [{meta, transcript 조각, 댓글}] (메타데이터가 없는 폴더는 건너뜀)."""
    cases = []
    out_dir = Path(out_dir)
    if not out_dir.is_dir():
        return cases
    for d in sorted(out_dir.iterdir()):
        if not (d.is_dir() and WEB_CASE_RX.match(d.name) and (d / "metadata.json").is_file()):
            continue
        try:
            meta = json.loads((d / "metadata.json").read_text("utf-8"))
        except ValueError:
            continue
        snips = []
        if (d / "transcript.json").is_file():
            try:
                snips = json.loads((d / "transcript.json").read_text("utf-8")).get("snippets") or []
            except ValueError:
                snips = []
        lang = ""
        if snips:
            try:
                lang = str(json.loads((d / "transcript.json").read_text("utf-8")).get("lang") or "")
            except ValueError:
                lang = ""
        cms = []
        if (d / "comments.csv").is_file():
            with open(d / "comments.csv", encoding="utf-8-sig", newline="") as f:
                cms = [{"text": r.get("text") or "", "likes": int(r.get("likes") or 0), "is_reply": str(r.get("is_reply")) in ("1", "True", "true")}
                       for r in csv.DictReader(f)]
        try:
            desc = (d / "description.txt").read_text("utf-8") if (d / "description.txt").is_file() else ""
        except OSError:
            desc = ""
        desc_text = clean_description(desc)
        src = ("음성인식" if "음성인식" in lang else "자막") if snips else ("설명" if desc_text else "없음")     # v1.2: 자막 없으면 설명으로
        text = " ".join(str(x.get("text") or "").replace("\n", " ") for x in snips) if snips else desc_text
        cases.append({"meta": meta, "snips": snips, "comments": cms, "folder": d.name, "src": src, "text": text,
                      "desc_text": desc_text, "has_thumb": (d / "thumbnail.jpg").is_file() and (d / "thumbnail.jpg").stat().st_size > 0})
    return cases


def title_features(title):
    t = str(title or "")
    return {name: bool(re.search(rx, t)) for name, rx in TITLE_FEATURES.items()}


def title_tokens(title):
    """제목 낱말 (한글·영숫자 2자 이상, 흔한 낱말 뺌). 조사를 떼지는 않음 — 거친 셈."""
    return [w for w in re.findall(r"[가-힣A-Za-z0-9&]{2,}", str(title or "")) if w.lower() not in STOPWORDS and not w.isdigit()]


def _median(xs):
    xs = [x for x in xs if isinstance(x, (int, float)) and not (isinstance(x, float) and math.isnan(x))]
    return round(statistics.median(xs), 2) if xs else None


def _vpd(m, now=None):
    """v1.4: 하루 조회수 = 조회수 ÷ 올린 날부터 받은 때(metadata collected)까지 날수."""
    return orr.views_per_day(int(m.get("views") or 0), _published(m), m.get("collected"), now)


def _is_success(m):
    """v1.4: 분석과 같은 규칙 (orr.success_core — 주별 창은 나이 제한 없이, 예전과 같음)."""
    subs, views = m.get("subs"), int(m.get("views") or 0)
    x = {"subs": subs, "views": views, "vpd": m.get("_vpd") if m.get("_vpd") is not None else _vpd(m),
         "ratio": round(views / max(subs, 100), 2) if subs is not None else None, "age_days": m.get("_age")}
    return orr.success_core(x, SUCCESS_RULES, with_age=False)


def _hook(snips, sec=HOOK_SEC):
    return " ".join(s.get("text", "").replace("\n", " ").strip() for s in snips if float(s.get("start") or 0) < sec).strip()


def case_hook(c):
    """도입부 (v1.2): 자막·음성인식은 첫 20초, 없으면 설명 앞부분. → (출처, 글) 또는 (None, "")."""
    if c.get("snips"):
        return c.get("src") or "자막", _hook(c["snips"])[:DESC_HOOK_CHARS]
    if c.get("desc_text"):
        return "설명", c["desc_text"][:DESC_HOOK_CHARS]
    return None, ""


def window_metrics(cases, prev_ids, now):
    """한 창(최근 k주)의 숫자. prev_ids = 바로 앞 창(k-1주)의 영상 → 이번 주에 새로 들어온 영상을 가림."""
    metas = [c["meta"] for c in cases]
    for m in metas:
        p = _published(m)
        m["_age"] = (now - p).total_seconds() / 86400 if p else None
        m["_vpd"] = _vpd(m, now)
        m["_ratio"] = round(int(m.get("views") or 0) / max(m["subs"], 100), 2) if m.get("subs") is not None else None
    n = len(metas)
    feats = Counter()
    toks = Counter()
    for m in metas:
        for k, v in title_features(m.get("title")).items():
            feats[k] += v
        toks.update(set(title_tokens(m.get("title"))))
    with_tr = [c for c in cases if c["snips"]]
    srcs = Counter(c.get("src") or ("자막" if c["snips"] else "없음") for c in cases)
    words = Counter()
    for c in cases:                                    # 내용 낱말: 자막·음성인식, 없으면 설명 (영상마다 한 번씩 셈)
        words.update(set(title_tokens(c.get("text") or "")))
    cms = [x for c in cases for x in c["comments"]]
    needs = Counter()
    none = 0
    for x in cms:
        hit = False
        for name, rx in COMMENT_CATS.items():
            if re.search(rx, x["text"]):
                needs[name] += 1
                hit = True
        none += 0 if hit else 1                           # v1.3.1: 어느 갈래에도 안 듦
    top = sorted(cases, key=lambda c: -c["meta"]["_vpd"])
    return {
        "videos": n,
        "channels": len({m.get("channel_id") or m.get("channel") for m in metas}),
        "new_this_week": [{"id": m["id"], "title": m.get("title"), "published": str(m.get("published") or "")[:10]}
                          for m in metas if m["id"] not in prev_ids],
        "views_median": _median([int(m.get("views") or 0) for m in metas]),
        "views_per_day_median": _median([m["_vpd"] for m in metas]),
        "ratio_median": _median([m["_ratio"] for m in metas if m["_ratio"] is not None]),
        "success": sum(1 for m in metas if _is_success(m)),
        "minutes_median": _median([float(m.get("minutes") or 0) for m in metas]),
        "title_len_avg": round(sum(len(str(m.get("title") or "")) for m in metas) / n, 1) if n else None,
        "title_features": [{"name": k, "count": v, "share": round(v / n, 3)} for k, v in feats.most_common() if v] if n else [],
        "title_words": [{"word": w, "count": c} for w, c in toks.most_common(10) if c >= 2],
        "transcripts": len(with_tr),
        "text_sources": {k: srcs.get(k, 0) for k in TEXT_SOURCES},
        "content_words": [{"word": w, "count": c} for w, c in words.most_common(12) if c >= 2],
        "chapters_share": round(sum(1 for m in metas if m.get("chapters")) / n, 3) if n else None,
        "syl_per_sec_median": _median([c["meta"].get("syl_per_sec") for c in with_tr]),
        "hooks": [{"id": c["meta"]["id"], "title": c["meta"].get("title"), "src": h[0], "hook": h[1]}
                  for c in top for h in [case_hook(c)] if h[0]][:3],
        "comments": len(cms),
        "comment_needs": [{"name": k, "count": v, "share": round(v / len(cms), 3)} for k, v in needs.most_common(6)] if cms else [],
        "comment_uncategorized": round(none / len(cms), 3) if cms else None,
        "top_comments": [{"text": x["text"][:120], "likes": x["likes"]} for x in sorted(cms, key=lambda x: -x["likes"]) if not x["is_reply"]][:3],
        "top_videos": [{"id": c["meta"]["id"], "title": c["meta"].get("title"), "channel": c["meta"].get("channel"),
                        "views": int(c["meta"].get("views") or 0), "views_per_day": c["meta"]["_vpd"],
                        "published": str(c["meta"].get("published") or "")[:10], "url": f"https://www.youtube.com/watch?v={c['meta']['id']}"}
                       for c in top[:5]],
    }


def build_report(topic, name, cases, now=None, max_weeks=52):
    """승인한 영상 → 창 목록 (최근 1주, 2주, … — 가장 오래된 영상이 들어갈 때까지, 최대 max_weeks).
    그보다 오래된 영상이 있으면 마지막에 '전체' 창 (v1.1 — 승인한 영상이 빠지지 않게)."""
    now = now or datetime.now(timezone.utc)
    dated = [c for c in cases if _published(c["meta"])]
    ages = [(now - _published(c["meta"])).total_seconds() / 86400 for c in dated]
    k_max = max(1, min(max_weeks, math.ceil(max(ages) / 7) if ages else 1))
    windows, prev = [], set()
    for k in range(1, k_max + 1):
        sub = [c for c, a in zip(dated, ages) if a <= 7 * k]
        w = {"weeks": k, "label": f"최근 {k}주", **window_metrics(sub, prev, now)}
        windows.append(w)
        prev = {c["meta"]["id"] for c in sub}
    older = sum(1 for a in ages if a > 7 * k_max)                 # max_weeks 보다 오래된 영상 → '전체' 창에만
    if older:
        windows.append({"weeks": None, "label": f"전체 ({k_max}주보다 오래된 {older}개 포함)", **window_metrics(dated, prev, now)})
    return {"tool": f"weekly_analysis.py {VERSION}", "topic": topic, "name": name, "generated": now.isoformat(timespec="seconds"),
            "cases": len(cases), "dated": len(dated), "older_than_windows": older, "max_weeks": max_weeks,
            "text_sources": {k: sum(1 for c in cases if c.get("src") == k) for k in TEXT_SOURCES},
            "criteria": f"성공 사례 = 구독자 {SUCCESS_RULES['MAX_SUBS']:,} 이하 · 조회수 {SUCCESS_RULES['MIN_VIEWS']:,} 이상 · "
                        + (f"구독자당 하루 조회수 ≥ {SUCCESS_RULES['MIN_VPD_SUBS']:g} (하루 조회수 ÷ 구독자)" if float(SUCCESS_RULES.get("MIN_VPD_SUBS") or 0) > 0
                           else f"조회수 ≥ 구독자 × {SUCCESS_RULES['MIN_RATIO']:g}"),
            "windows": windows}


def _pct(x):
    return f"{x:.0%}" if isinstance(x, (int, float)) else "–"


def _num(x):
    return f"{x:,}" if isinstance(x, int) else (f"{x:,.1f}" if isinstance(x, float) else "–")


def _write_atomic(path, text, encoding="utf-8"):
    """임시 파일에 쓰고 바꿔치기 (v1.2 — 웹 화면과 음성인식이 동시에 써도 반쪽 파일이 안 생기게). Windows 에서 다른 쪽이
    잠깐 열고 있으면 몇 번 다시."""
    path = Path(path)
    tmp = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    tmp.write_text(text, encoding)
    for i in range(10):
        try:
            os.replace(tmp, path)
            return
        except PermissionError:
            time.sleep(0.3 * (i + 1))
    os.replace(tmp, path)


def _csv_text(rows):
    import io
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    for r in rows:
        w.writerow(r)
    return "\ufeff" + buf.getvalue()


def approved_rows(cases, now=None):
    """승인한 영상 전부 (업로드 최근 순) → 표 줄 (v1.2)."""
    now = now or datetime.now(timezone.utc)
    out = []
    for c in cases:
        m = c["meta"]
        p = _published(m)
        views, subs = int(m.get("views") or 0), m.get("subs")
        out.append({"published": p.date().isoformat() if p else "", "_ts": p.timestamp() if p else 0, "id": m.get("id"),
                    "title": m.get("title") or "", "channel": m.get("channel") or "", "subs": subs, "views": views,
                    "ratio": round(views / max(subs, 100), 2) if subs is not None else None,
                    "views_per_day": _vpd(m, now), "minutes": m.get("minutes"), "src": c.get("src") or "",
                    "transcript_status": m.get("transcript_status") or "", "comments": len(c["comments"]),
                    "thumbnail": bool(c.get("has_thumb")), "folder": c["folder"], "approved": m.get("approved") or "",
                    "success": _is_success(m), "url": f"https://www.youtube.com/watch?v={m.get('id')}"})
    out.sort(key=lambda r: -r["_ts"])
    return out


def write_approved(out_dir, rep, rows):
    """approved.md·approved.csv — 승인한 영상 전부와 글 출처 (v1.2)."""
    out_dir = Path(out_dir)
    cols = ["published", "id", "title", "channel", "subs", "views", "ratio", "views_per_day", "minutes", "src", "transcript_status",
            "comments", "thumbnail", "success", "folder", "approved", "url"]
    _write_atomic(out_dir / "approved.csv", _csv_text([cols] + [[r[k] for k in cols] for r in rows]))
    srcs = Counter(r["src"] for r in rows)
    L = [f"# {rep['name']} — 승인한 영상 {len(rows)}개 (업로드 최근 순)", "",
         f"자동 생성 — `tools/weekly_analysis.py` {VERSION} ({rep['generated'][:16].replace('T', ' ')} UTC). "
         "글 출처 = 분석에 쓴 글: 자막 → 음성인식 → **설명**(자막을 못 받아 영상 설명으로 대신 분석, 음성인식 대본이 생기면 바뀜) → 없음. "
         "사례 폴더(`W_<영상ID>` — 설명·자막·댓글 전부·썸네일)도 GitHub 에 올라감 (폴더 열에서 바로). "
         "※ 연구·교육용 — 투자 권유가 아님.", "",
         "글 출처: " + " · ".join(f"{k} {srcs.get(k, 0)}개" for k in TEXT_SOURCES), "",
         "| 업로드 | 제목 | 채널 | 구독자 | 조회수 | 배수 | 하루 조회수 | 길이(분) | 글 출처 | 댓글 | 썸네일 | 폴더 |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        title = (r["title"] or "")[:50].replace("|", "∣")
        channel = (r["channel"] or "")[:16].replace("|", "∣")
        subs = "비공개" if r["subs"] is None else f"{r['subs']:,}"
        star = " ⭐" if r["success"] else ""
        L.append(f"| {r['published']} | [{title}]({r['url']}){star} | {channel} | {subs} | {r['views']:,} | {_num(r['ratio'])} | "
                 f"{_num(r['views_per_day'])} | {_num(r['minutes'])} | {r['src']} | {r['comments']:,} | {'✓' if r['thumbnail'] else '✗'} | `{r['folder']}` |")
    L += ["", "⭐ = 성공 사례 (" + rep["criteria"] + ")"]
    _write_atomic(out_dir / "approved.md", "\n".join(L) + "\n")


def write_report(out_dir, rep, cases=None):
    """weekly.json·weekly.csv·weekly.md (+ approved.md·csv) 를 out_dir(<주제>/result/outliers/) 에 씀."""
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    _write_atomic(out_dir / "weekly.json", json.dumps(rep, ensure_ascii=False, indent=1))
    cols = ["weeks", "videos", "channels", "new", "views_median", "views_per_day_median", "ratio_median", "success", "minutes_median",
            "title_len_avg", "transcripts", "text_caption", "text_speech", "text_description", "text_none", "comments"]
    rows = [cols]
    for x in rep["windows"]:
        ts = x.get("text_sources") or {}
        rows.append([x["weeks"], x["videos"], x["channels"], len(x["new_this_week"]), x["views_median"], x["views_per_day_median"],
                     x["ratio_median"], x["success"], x["minutes_median"], x["title_len_avg"], x["transcripts"],
                     ts.get("자막", 0), ts.get("음성인식", 0), ts.get("설명", 0), ts.get("없음", 0), x["comments"]])
    _write_atomic(out_dir / "weekly.csv", _csv_text(rows))
    L = [f"# {rep['name']} — 주별 분석 (최근 1주부터 한 주씩 넓힘)", "",
         f"자동 생성 — `tools/weekly_analysis.py` {VERSION} ({rep['generated'][:16].replace('T', ' ')} UTC). 웹 화면에서 승인해 자료를 받은 영상 "
         f"{rep['cases']}개 (`W_<영상ID>` 폴더). {rep['criteria']}. ※ 연구·교육용 — 투자 권유가 아님.", "",
         "> 이 표는 승인한 영상 **전부**의 주별 추세다 (한 채널을 통째로 추가하면 그 채널 쪽으로 쏠림). 성공 사례만 골라 주제·제목·썸네일·구성·"
         "시청자 니즈를 비교한 분석은 **`analysis.md`** (지시사항 재료).", "",
         "## 한눈에 (누적: 최근 k주 안에 올라온 영상)", "",
         "| 창 | 영상 | 채널 | 이번 주 새로 | 조회수 중앙값 | 하루 조회수 중앙값 | 배수 중앙값 | 성공 사례 | 길이(분) | 제목 글자 | 글 출처 자막·음성·설명 | 댓글 |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for x in rep["windows"]:
        ts = x.get("text_sources") or {}
        L.append(f"| {x['label']} | {x['videos']} | {x['channels']} | {len(x['new_this_week'])} | {_num(x['views_median'])} | "
                 f"{_num(x['views_per_day_median'])} | {_num(x['ratio_median'])} | {x['success']} | {_num(x['minutes_median'])} | "
                 f"{_num(x['title_len_avg'])} | {ts.get('자막', 0)}·{ts.get('음성인식', 0)}·{ts.get('설명', 0)} | {x['comments']:,} |")
    for x in rep["windows"]:
        L += ["", f"## {x['label']}", ""]
        if not x["videos"]:
            L.append("이 기간에 올라온 승인 영상 없음.")
            continue
        if x["new_this_week"]:
            L.append(f"- 이번 주에 새로 들어온 영상 {len(x['new_this_week'])}개: "
                     + " · ".join(f"{v['title'][:30]}({v['published']})" for v in x["new_this_week"][:6])
                     + (" …" if len(x["new_this_week"]) > 6 else ""))
        if x["title_features"]:
            L.append("- 제목 특징: " + " · ".join(f"{f['name']} {_pct(f['share'])}" for f in x["title_features"][:6]))
        if x["title_words"]:
            L.append("- 자주 쓴 제목 낱말: " + ", ".join(f"{w['word']}({w['count']})" for w in x["title_words"]))
        ts = x.get("text_sources") or {}
        L.append(f"- 글 출처: 자막 {ts.get('자막', 0)} · 음성인식 {ts.get('음성인식', 0)} · 설명으로 대신 {ts.get('설명', 0)} · 없음 {ts.get('없음', 0)}"
                 + (f" · 말 속도 중앙값 {_num(x['syl_per_sec_median'])} 음절/초 (자막·음성인식)" if x["transcripts"] else "")
                 + (f" · 타임라인 있는 영상 {_pct(x.get('chapters_share'))}" if x.get("chapters_share") is not None else ""))
        if x.get("content_words"):
            L.append("- 내용에 자주 나온 낱말 (자막·음성인식, 없으면 설명): " + ", ".join(f"{w['word']}({w['count']})" for w in x["content_words"]))
        for h in x["hooks"]:
            where = f"첫 {HOOK_SEC}초({h['src']})" if h.get("src") in ("자막", "음성인식") else "설명 앞부분"
            L.append(f"  - {where} — {h['title'][:30]}: “{h['hook']}”")
        if x["comment_needs"]:
            L.append(f"- 댓글 {x['comments']:,}개 니즈: " + " · ".join(f"{n['name']} {_pct(n['share'])}" for n in x["comment_needs"])
                     + (f" · **어느 갈래에도 안 듦 {_pct(x['comment_uncategorized'])}** (모든 댓글 유형은 `comment_types.md`)" if x.get("comment_uncategorized") is not None else ""))
        for c in x["top_comments"]:
            L.append(f"  - 👍{c['likes']:,} “{c['text']}”")
        L += ["", "| 상위 영상 (하루 조회수 순) | 채널 | 조회수 | 하루 조회수 | 업로드 |", "|---|---|---|---|---|"]
        for v in x["top_videos"]:
            L.append(f"| [{(v['title'] or '')[:50]}]({v['url']}) | {(v['channel'] or '')[:16]} | {v['views']:,} | {_num(v['views_per_day'])} | {v['published']} |")
    _write_atomic(out_dir / "weekly.md", "\n".join(L) + "\n")
    if cases is not None:
        write_approved(out_dir, rep, approved_rows(cases, datetime.fromisoformat(rep["generated"])))
    last = rep["windows"][-1].get("text_sources") if rep["windows"] else {}
    log("WEEKLY", file=str(out_dir / "weekly.md"), windows=len(rep["windows"]), cases=rep["cases"],
        text_sources=",".join(f"{k}:{v}" for k, v in (last or {}).items()) or "-", approved_list=cases is not None)


def run(topic, max_weeks=52, now=None, root=None):
    root = Path(root or ROOT)
    out = root / topic / "result" / "outliers"
    name = topic
    try:
        import tomllib
    except ModuleNotFoundError:      # Python 3.10
        import tomli as tomllib
    try:
        cfg = tomllib.loads((root / topic / "analyzer_config.toml").read_text("utf-8"))
        name = (cfg.get("topic") or {}).get("TOPIC") or cfg.get("TOPIC") or topic
    except (OSError, ValueError):
        pass
    try:                                       # v1.4: 성공 규칙 = 주제 analysis_rules.toml [success] (분석과 같음)
        d = tomllib.loads((root / topic / "analysis_rules.toml").read_text("utf-8")) if (root / topic / "analysis_rules.toml").is_file() else {}
        SUCCESS_RULES.update({k: v for k, v in (d.get("success") or {}).items() if k in SUCCESS_RULES})
    except (OSError, ValueError) as e:
        log("START", logging.WARNING, note=f"analysis_rules.toml [success] 못 읽음 — 기본 규칙 — {type(e).__name__}")
    cases = load_cases(out)
    log("START", topic=topic, cases=len(cases), max_weeks=max_weeks, tool=f"weekly_analysis.py {VERSION}",
        success_rule="구독자당 하루 조회수" if float(SUCCESS_RULES.get("MIN_VPD_SUBS") or 0) > 0 else "배수")
    rep = build_report(topic, name, cases, now, max_weeks)
    write_report(out, rep, cases)
    try:                                       # v1.3: 성공 사례 분석 (analysis.md) — 실패해도 주별 분석은 저장됨
        import success_analysis
        success_analysis.run(topic, now=now, root=root)
    except Exception as e:
        log("WEEKLY", logging.WARNING, note="성공 사례 분석(analysis.md) 실패 — 주별 분석은 저장됨", error=f"{type(e).__name__}: {e}"[:300])
    try:                                       # v1.5: 시청자 페르소나 (personas.md·.json) — 설정이 있는 주제만(지금 주식·재테크), 승인 영상 댓글이 바뀌면 같이 바뀜
        import personas
        personas.build(topic, now=now, root=root)
    except Exception as e:
        log("WEEKLY", logging.WARNING, note="시청자 페르소나(personas.md) 실패 — 주별·성공 사례 분석은 저장됨",
            error=f"{type(e).__name__}: {e}"[:300], next=f"python3 tools/personas.py {topic} 로 다시")
    log("DONE", topic=topic, windows=len(rep["windows"]), success=rep["windows"][-1]["success"] if rep["windows"] else 0,
        text_sources=",".join(f"{k}:{v}" for k, v in rep["text_sources"].items()))
    return rep


def main(argv=None):
    ap = argparse.ArgumentParser(description="웹 화면에서 승인한 영상의 주별 분석 (최근 1주·2주·3주 …)")
    ap.add_argument("topic")
    ap.add_argument("--max-weeks", type=int, default=52, help="한 주씩 넓힐 최대 주 수 (더 오래된 영상은 마지막 '전체' 창)")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args(argv)
    logging.basicConfig(level=getattr(logging, a.log_level), format="%(message)s", stream=sys.stdout)
    run(a.topic, a.max_weeks)
    return 0


if __name__ == "__main__":
    sys.exit(main())
