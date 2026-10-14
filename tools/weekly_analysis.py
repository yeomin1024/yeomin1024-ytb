#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-10-14 — 승인한 영상이 모두 들어가게 (사용자 질문 "분석 결과 다 올라온거야?" — 승인 289개 중 155개가 12주보다
#          오래돼 어느 창에도 없었음): 창을 최대 52주까지(한 주씩), 그보다 오래된 영상이 있으면 마지막에 '전체' 창을 더함
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
성공 사례 기준 = 구독자 5만 이하 · 조회수 1만 이상 · 조회수 ≥ 구독자 × 3 (outlier_research 와 같음, 구독자 100 미만은 100).
로그: [STAGE] [시각] key=value (START·WEEKLY·DONE)
※ 연구·교육용. 투자 권유가 아니다.
"""
import argparse
import csv
import json
import logging
import math
import re
import statistics
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from outlier_stats import COMMENT_CATS, TITLE_FEATURES       # noqa: E402  같은 규칙 (제목 특징·댓글 갈래)

ROOT = Path(__file__).resolve().parent.parent
VERSION = "v1.1"
LOG = logging.getLogger("weekly")
WEB_CASE_RX = re.compile(r"^W_([0-9A-Za-z_-]{11})$")
MAX_SUBS, MIN_RATIO, MIN_VIEWS = 50000, 3.0, 10000
HOOK_SEC = 20
STOPWORDS = set("이 그 저 것 수 등 및 더 왜 다 또 안 못 잘 꼭 진짜 정말 지금 이제 그냥 바로 모든 모두 하는 있는 없는 되는 하면 해서 했다 합니다 입니다 "
                "에서 으로 하고 까지 부터 에게 이런 저런 그런 무조건 반드시 절대 the and for with 영상 채널 구독 라이브".split())


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
        cms = []
        if (d / "comments.csv").is_file():
            with open(d / "comments.csv", encoding="utf-8-sig", newline="") as f:
                cms = [{"text": r.get("text") or "", "likes": int(r.get("likes") or 0), "is_reply": str(r.get("is_reply")) in ("1", "True", "true")}
                       for r in csv.DictReader(f)]
        cases.append({"meta": meta, "snips": snips, "comments": cms, "folder": d.name})
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


def _is_success(m):
    subs, views = m.get("subs"), int(m.get("views") or 0)
    if subs is None or subs > MAX_SUBS or views < MIN_VIEWS:
        return False
    return views / max(subs, 100) >= MIN_RATIO


def _hook(snips, sec=HOOK_SEC):
    return " ".join(s.get("text", "").replace("\n", " ").strip() for s in snips if float(s.get("start") or 0) < sec).strip()


def window_metrics(cases, prev_ids, now):
    """한 창(최근 k주)의 숫자. prev_ids = 바로 앞 창(k-1주)의 영상 → 이번 주에 새로 들어온 영상을 가림."""
    metas = [c["meta"] for c in cases]
    for m in metas:
        p = _published(m)
        m["_age"] = (now - p).total_seconds() / 86400 if p else None
        m["_vpd"] = round(int(m.get("views") or 0) / max(m["_age"] or 1, 1), 1)
        m["_ratio"] = round(int(m.get("views") or 0) / max(m["subs"], 100), 2) if m.get("subs") is not None else None
    n = len(metas)
    feats = Counter()
    toks = Counter()
    for m in metas:
        for k, v in title_features(m.get("title")).items():
            feats[k] += v
        toks.update(set(title_tokens(m.get("title"))))
    with_tr = [c for c in cases if c["snips"]]
    cms = [x for c in cases for x in c["comments"]]
    needs = Counter()
    for x in cms:
        for name, rx in COMMENT_CATS.items():
            if re.search(rx, x["text"]):
                needs[name] += 1
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
        "syl_per_sec_median": _median([c["meta"].get("syl_per_sec") for c in with_tr]),
        "hooks": [{"id": c["meta"]["id"], "title": c["meta"].get("title"), "hook": _hook(c["snips"])[:160]}
                  for c in top if c["snips"]][:3],
        "comments": len(cms),
        "comment_needs": [{"name": k, "count": v, "share": round(v / len(cms), 3)} for k, v in needs.most_common(6)] if cms else [],
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
            "criteria": f"성공 사례 = 구독자 {MAX_SUBS:,} 이하 · 조회수 {MIN_VIEWS:,} 이상 · 조회수 ≥ 구독자 × {MIN_RATIO:g}",
            "windows": windows}


def _pct(x):
    return f"{x:.0%}" if isinstance(x, (int, float)) else "–"


def _num(x):
    return f"{x:,}" if isinstance(x, int) else (f"{x:,.1f}" if isinstance(x, float) else "–")


def write_report(out_dir, rep):
    """weekly.json·weekly.csv·weekly.md 를 out_dir(<주제>/result/outliers/) 에 씀."""
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "weekly.json").write_text(json.dumps(rep, ensure_ascii=False, indent=1), "utf-8")
    cols = ["weeks", "videos", "channels", "new", "views_median", "views_per_day_median", "ratio_median", "success", "minutes_median",
            "title_len_avg", "transcripts", "comments"]
    with open(out_dir / "weekly.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for x in rep["windows"]:
            w.writerow([x["weeks"], x["videos"], x["channels"], len(x["new_this_week"]), x["views_median"], x["views_per_day_median"],
                        x["ratio_median"], x["success"], x["minutes_median"], x["title_len_avg"], x["transcripts"], x["comments"]])
    L = [f"# {rep['name']} — 주별 분석 (최근 1주부터 한 주씩 넓힘)", "",
         f"자동 생성 — `tools/weekly_analysis.py` {VERSION} ({rep['generated'][:16].replace('T', ' ')} UTC). 웹 화면에서 승인해 자료를 받은 영상 "
         f"{rep['cases']}개 (`W_<영상ID>` 폴더). {rep['criteria']}. ※ 연구·교육용 — 투자 권유가 아님.", "",
         "## 한눈에 (누적: 최근 k주 안에 올라온 영상)", "",
         "| 창 | 영상 | 채널 | 이번 주 새로 | 조회수 중앙값 | 하루 조회수 중앙값 | 배수 중앙값 | 성공 사례 | 길이(분) | 제목 글자 | 자막 | 댓글 |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for x in rep["windows"]:
        L.append(f"| {x['label']} | {x['videos']} | {x['channels']} | {len(x['new_this_week'])} | {_num(x['views_median'])} | "
                 f"{_num(x['views_per_day_median'])} | {_num(x['ratio_median'])} | {x['success']} | {_num(x['minutes_median'])} | "
                 f"{_num(x['title_len_avg'])} | {x['transcripts']} | {x['comments']:,} |")
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
        if x["transcripts"]:
            L.append(f"- 자막 {x['transcripts']}개 · 말 속도 중앙값 {_num(x['syl_per_sec_median'])} 음절/초")
            for h in x["hooks"]:
                L.append(f"  - 첫 {HOOK_SEC}초 — {h['title'][:30]}: “{h['hook']}”")
        if x["comment_needs"]:
            L.append(f"- 댓글 {x['comments']:,}개 니즈: " + " · ".join(f"{n['name']} {_pct(n['share'])}" for n in x["comment_needs"]))
        for c in x["top_comments"]:
            L.append(f"  - 👍{c['likes']:,} “{c['text']}”")
        L += ["", "| 상위 영상 (하루 조회수 순) | 채널 | 조회수 | 하루 조회수 | 업로드 |", "|---|---|---|---|---|"]
        for v in x["top_videos"]:
            L.append(f"| [{(v['title'] or '')[:50]}]({v['url']}) | {(v['channel'] or '')[:16]} | {v['views']:,} | {_num(v['views_per_day'])} | {v['published']} |")
    (out_dir / "weekly.md").write_text("\n".join(L) + "\n", "utf-8")
    log("WEEKLY", file=str(out_dir / "weekly.md"), windows=len(rep["windows"]), cases=rep["cases"])


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
    cases = load_cases(out)
    log("START", topic=topic, cases=len(cases), max_weeks=max_weeks, tool=f"weekly_analysis.py {VERSION}")
    rep = build_report(topic, name, cases, now, max_weeks)
    write_report(out, rep)
    log("DONE", topic=topic, windows=len(rep["windows"]), success=rep["windows"][-1]["success"] if rep["windows"] else 0)
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
