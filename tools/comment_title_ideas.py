#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-21 — 새로: 제목으로 삼을 만한 댓글 (좋아요 순) + 그 내용의 영상 제목이 이미 있는지. 사용자 지시 2026-10-21 "아니 제목으로
#          삼을 만한 댓글 없냐고 좋아요 수 높은거 찾아보면 나올거 같은데 그리고 그 내용이랑 관련된 내용이 실제 영상 제목으로 있는지도 분석해서 각각 목록
#          알려줘봐". ① candidates: 승인한 영상의 시청자 댓글(답글·채널 주인·도배 꼴·정치 뺌) 중 투자 낱말이 든 '질문·요청'과 '주장·믿음'(백테스트로
#          확인할 만한 말)을 나라(한국·미국 — title_comment_link 와 같은 규칙)별 좋아요 순으로 → candidates.tsv. ② 사람(또는 AI)이 그중 제목감을 골라
#          picks.tsv 에 찾을 말(정규식)과 함께 적음. ③ match: 고른 댓글마다 캐시에 있는 영상 제목(검색·채널 평소 영상 — 탐색에서 본 것 전부) 중
#          찾을 말에 맞는 것 → comment_titles.md·.json. 할당량 0 (유튜브 전체가 아니라 탐색에서 본 영상만 — 결과 0번). ※ 연구·교육용 — 투자 권유가 아님.
"""제목으로 삼을 만한 댓글 + 같은 내용의 영상 제목이 있는지

  python3 tools/comment_title_ideas.py stock candidates     # <주제>/result/outliers/comment_title_candidates.tsv
  (사람·AI 가 고름 → <주제>/result/outliers/comment_title_picks.tsv : pick·country·kind·likes·video_id·comment·topic·match)
  python3 tools/comment_title_ideas.py stock match          # <주제>/result/outliers/comment_titles.md · .json
"""
import argparse
import csv
import json
import logging
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import success_analysis as sa        # noqa: E402
import title_comment_link as tcl     # noqa: E402

VERSION = "v1.0"
ROOT = Path(__file__).resolve().parent.parent
LOG = logging.getLogger("ctitle")
PER_KIND = 150               # 나라·갈래마다 후보 몇 개 (좋아요 순)
MIN_LIKES = 3
RECENT_DAYS = 180            # '최근 영상' = 올린 지 이 날수 안
# 투자 낱말 — 후보 댓글은 이것이 하나는 있어야 (잡담·인사 거르기)
INVEST_KO = (r"주식|투자|매수|매도|수익|손실|손절|익절|물타기|적립|분할|존버|장기|단타|스윙|레버리지|배당|ETF|etf|지수|S&P|에스앤피|나스닥|코스피|코스닥|"
             r"QLD|QQQ|TQQQ|SCHD|JEPQ|SOXL|VOO|SPY|삼성전자|삼전|하이닉스|닉스|반도체|엔비디아|테슬라|팔란티어|연금|ISA|IRP|퇴직|노후|은퇴|현금|예금|적금|"
             r"금리|환율|달러|채권|금값|저점|고점|바닥|폭락|하락장|상승장|리밸런싱|포트폴리오|비중|원금|복리|계좌|세금|양도세|배당세")
INVEST_EN = (r"\b(stocks?|invest\w*|buy\w*|sell\w*|shares?|portfolio|dividends?|etfs?|index|s&p|nasdaq|qqq|tqqq|qld|schd|jepq|jepi|voo|spy|vti|"
             r"401k|ira|roth|retire\w*|cash|bonds?|gold|crash|dip|bear|bull|leverag\w*|dca|dollar[- ]cost|rebalanc\w*|options?|calls?|puts?|"
             r"nvidia|nvda|tesla|tsla|palantir|pltr|amd|market)\b")
# 질문·요청 (영어) — 한국어는 success_analysis.classify_comment 의 '더 알고 싶은 것' 그대로
ASK_EN = (r"(^|\.\s|\n)\s*(how|what|why|when|which|should|would|could|can|is|are|do|does|will|anyone|any)\b[^?]{3,200}\?|"
          r"(please|pls) (make|do|cover|talk|explain)|(can|could|would) you (make|do|cover|explain|talk|compare|analy[sz]e)|"
          r"(do|make) a video (on|about)|i'?d love (to see|a video)|next video")
# 주장·믿음 — 백테스트로 확인할 만한 단정 (투자 낱말과 함께)
CLAIM_KO = (r"답이다|답입니다|정답|진리|무조건|반드시|결국|필승|불패|이긴다|이깁니다|승리|망한다|망합니다|안 ?된다|안 ?됩니다|최고다|최고입니다|"
            r"하면 ?된다|하면 ?됩니다|하면 ?끝|만 ?하면|밖에 ?없|가 ?맞다|가 ?맞습니다|해야 ?한다|해야 ?합니다|하지 ?마|마세요|교훈|깨달")
CLAIM_EN = (r"\b(always|never|only|best|the key|the secret|wins?|works|beats?|outperform\w*|guarantee\w*|no brainer|just buy|keep buying|"
            r"time in the market|don'?t (sell|panic|time)|lesson|learned)\b")


def log(stage, level=logging.INFO, **kv):
    LOG.log(level, "[%s] [%s] %s", stage, datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S"),
            " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) and (' ' in v or not v) else v}" for k, v in kv.items()))


def clean(t, n=400):
    return re.sub(r"\s+", " ", str(t or "")).strip()[:n]


def kind_of(text, country):
    """댓글 → '질문·요청' / '주장·믿음' / None. 정치 댓글·투자 낱말 없는 댓글은 None."""
    if country == "한국":
        if not re.search(INVEST_KO, text):
            return None
        cats = sa.classify_comment(text)
        if sa.CAT_POLITICS in cats:
            return None
        if sa.CAT_ASK in cats:
            return "질문·요청"
        return "주장·믿음" if re.search(CLAIM_KO, text) else None
    if not re.search(INVEST_EN, text, re.I):
        return None
    if re.search(ASK_EN, text, re.I):
        return "질문·요청"
    return "주장·믿음" if re.search(CLAIM_EN, text, re.I) else None


def load(topic, now):
    out = ROOT / topic / "result" / "outliers"
    cache_infos, cache_subs = sa.load_cache(out)
    cases = sa.load_cases(out, cache_infos, cache_subs, now)
    rules, rel, themes = sa.load_rules(ROOT, topic), sa.load_rel(ROOT, topic), sa.load_themes(ROOT, topic)
    for c in cases:                                         # 뺄 까닭 (주제 밖·뺀 주제·광고 의심) — analysis.md 와 같은 규칙
        c["theme"] = sa.theme_of(c["title"], c.get("tags"), themes)
        c["exclude"] = sa.flags(c, rules, rel)
    p = tcl.channels_path(out)
    ch = json.loads(p.read_text("utf-8")) if p.is_file() else {}
    log("LOAD", topic=topic, cases=len(cases), cache_videos=len(cache_infos), channels=len(ch))
    return out, cache_infos, cache_subs, cases, ch


def cmd_candidates(topic, now):
    out, cache_infos, cache_subs, cases, ch = load(topic, now)
    seen_text = Counter()
    for c in cases:                                         # 도배: 같은 글이 영상 3곳 이상 (success_analysis 와 같은 생각)
        for t in {re.sub(r"[^가-힣A-Za-z]", "", m["text"])[-50:] for m in c["comments"] if len(m["text"]) >= 30}:
            seen_text[t] += 1
    rows = defaultdict(list)
    scanned = Counter()
    for c in cases:
        cc = tcl.country_of(c, ch)
        if cc is None or c.get("exclude"):
            continue
        wk = tcl.week_of(c.get("age_days"))
        for m in c["comments"]:
            t = m["text"]
            if m["creator"] or m["reply"] or m["likes"] < MIN_LIKES or not t.strip() or re.search(sa.SPAM_RX, t):
                continue
            if len(t) >= 30 and seen_text[re.sub(r"[^가-힣A-Za-z]", "", t)[-50:]] >= sa.SPAM_MIN_VIDEOS:
                continue
            scanned[cc] += 1
            k = kind_of(t, cc)
            if k:
                rows[(cc, k)].append({"country": cc, "kind": k, "likes": m["likes"], "video_id": c["id"], "video_title": clean(c["title"], 90),
                                      "channel": clean(c["channel"], 30), "published": c["published"].date().isoformat() if c["published"] else "",
                                      "week": f"{wk}주 전" if wk else "4주보다 전", "comment": clean(t)})
    p = out / "comment_title_candidates.tsv"
    fields = ["rank", "country", "kind", "likes", "video_id", "video_title", "channel", "published", "week", "comment"]
    with p.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, delimiter="\t", lineterminator="\n")
        w.writeheader()
        for key in sorted(rows):
            lst = sorted(rows[key], key=lambda r: -r["likes"])
            per_video = Counter()
            k = 0
            for r in lst:
                if per_video[r["video_id"]] >= 5:            # 한 영상이 목록을 덮지 않게 (영상마다 5개까지)
                    continue
                per_video[r["video_id"]] += 1
                k += 1
                w.writerow({"rank": k, **r})
                if k >= PER_KIND:
                    break
    log("CANDIDATES", topic=topic, file=str(p), scanned=dict(scanned), found={f"{a}|{b}": len(v) for (a, b), v in rows.items()}, per_kind=PER_KIND)
    return {k: len(v) for k, v in rows.items()}


def cmd_match(topic, now):
    out, cache_infos, cache_subs, cases, ch = load(topic, now)
    picks_p = out / "comment_title_picks.tsv"
    picks = list(csv.DictReader(picks_p.open(encoding="utf-8"), delimiter="\t"))
    titles = []
    for vid, i in cache_infos.items():
        x = sa._base({**i, "views": i.get("view_count"), "likes": i.get("like_count"), "comments_reported": i.get("comment_count")},
                     cache_subs.get(i.get("channel_id")), now)
        if x["minutes"] < 1 or x.get("live") or x.get("was_live"):
            continue
        titles.append({"id": vid, "title": x["title"], "channel": x["channel"], "subs": x["subs"], "views": x["views"], "vpd": x.get("vpd"),
                       "age_days": x["age_days"], "published": x["published"].date().isoformat() if x["published"] else "",
                       "country": tcl.country_of(x, ch) or "그 밖", "minutes": x["minutes"]})
    res = []
    for pk in picks:
        rx = re.compile(pk["match"], re.I)
        hit = [t for t in titles if t["id"] != pk["video_id"] and rx.search(t["title"])]
        same = [t for t in hit if t["country"] == pk["country"]]
        recent = [t for t in same if t["age_days"] is not None and t["age_days"] <= RECENT_DAYS]
        res.append({**pk, "likes": int(pk["likes"]), "matches": len(hit), "same_country": len(same), "recent_same_country": len(recent),
                    "top": sorted(same, key=lambda t: -(t["views"] or 0))[:4],
                    "newest": max((t["published"] for t in same), default="")})
        log("MATCH", pick=pk["pick"], country=pk["country"], match=pk["match"], titles=len(hit), same_country=len(same), recent=len(recent))
    data = {"tool": f"comment_title_ideas.py {VERSION}", "topic": topic, "generated": now.isoformat(timespec="minutes"),
            "titles_searched": len(titles), "titles_by_country": dict(Counter(t["country"] for t in titles)), "picks": res}
    (out / "comment_titles.json").write_text(json.dumps(data, ensure_ascii=False, indent=1, default=str), "utf-8")
    write_md(out, data)
    log("REPORT", topic=topic, file=str(out / "comment_titles.md"), picks=len(res), titles_searched=len(titles))
    return data


def n(x):
    return "-" if x is None else f"{x:,.0f}"


def cell(s, k=80):
    s = clean(s, 10 ** 4).replace("|", "∣")
    return s if len(s) <= k else s[:k - 1] + "…"


def write_md(out, data):
    L = ["# 제목으로 삼을 만한 댓글 — 그리고 같은 내용의 영상 제목이 이미 있는지", "",
         f"자동 생성 — `tools/comment_title_ideas.py` {VERSION} ({data['generated']} UTC). ※ 연구·교육용 — 투자 권유가 아님.", "",
         "## 0. 자료와 한계 (먼저 읽기)", "",
         "- **댓글** = 승인해 자료를 받은 영상의 시청자 댓글 (답글·채널 주인·도배 꼴·정치 댓글 뺌) 중 투자 낱말이 든 **질문·요청**(시청자가 알고 싶은 것)과 "
         "**주장·믿음**(시청자가 믿는 방법 — 백테스트로 확인할 만한 것). 좋아요 순 후보 `comment_title_candidates.tsv` 에서 제목감을 골라 `comment_title_picks.tsv` 에 적음 (고른 이 = Claude).",
         f"- **같은 내용의 영상 제목** = 탐색에서 본 영상 {data['titles_searched']:,}개(검색 결과 + 채널 평소 영상, 라이브 뺌)의 제목 중 고른 댓글마다 적은 '찾을 말'(정규식)에 맞는 것. "
         "**유튜브 전체가 아니다** — 0개여도 '세상에 없다'가 아니라 '탐색에서 본 것 중엔 없다'. 같은 나라만 셈 (한국 = 한국어 영상 · 미국 = 채널 나라 US 인 영어 영상). "
         f"나라별 제목 수: {', '.join(f'{k} {v:,}' for k, v in data['titles_by_country'].items())}.",
         f"- 최근 = 올린 지 {RECENT_DAYS}일 안. 조회수는 받은 때 값. 댓글 좋아요는 그 영상 크기에 따라 다르다 (큰 채널 댓글이 좋아요가 많음).", "",
         "## 1. 한눈에", "",
         "| # | 나라 | 갈래 | 주제 | 👍 | 같은 내용 제목 (같은 나라) | 그중 최근 180일 | 가장 최근 |", "|---|---|---|---|---|---|---|---|"]
    for p in data["picks"]:
        L.append(f"| {p['pick']} | {p['country']} | {p['kind']} | {cell(p['topic'], 40)} | {p['likes']:,} | {p['same_country']} | {p['recent_same_country']} | {p['newest'] or '-'} |")
    L += ["", "## 2. 댓글과 같은 내용의 영상 제목", ""]
    for p in data["picks"]:
        L += [f"### {p['pick']}. {p['topic']} — {p['country']} · {p['kind']}", "",
              f"- 👍{p['likes']:,} “{cell(p['comment'], 300)}”",
              f"  - 댓글이 달린 영상: [{cell(p['video_title'], 80)}](https://www.youtube.com/watch?v={p['video_id']})",
              f"- 찾을 말: `{p['match']}` → 같은 나라 제목 **{p['same_country']}개** (최근 180일 {p['recent_same_country']}개, 다른 나라 포함 {p['matches']}개)"]
        for t in p["top"]:
            L.append(f"  - [{cell(t['title'], 90)}](https://www.youtube.com/watch?v={t['id']}) — {cell(t['channel'], 24)} · 구독자 {n(t['subs'])} · "
                     f"조회수 {n(t['views'])} · {t['published']}")
        if not p["top"]:
            L.append("  - (탐색에서 본 제목 중엔 없음)")
        L.append("")
    (out / "comment_titles.md").write_text("\n".join(L) + "\n", "utf-8")


def main(argv=None):
    ap = argparse.ArgumentParser(description="제목으로 삼을 만한 댓글 + 같은 내용의 영상 제목 (할당량 0)")
    ap.add_argument("topic")
    ap.add_argument("cmd", choices=["candidates", "match"])
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args(argv)
    logging.basicConfig(level=getattr(logging, a.log_level), format="%(message)s", stream=sys.stderr)
    sa.LOG.setLevel(logging.WARNING)
    now = datetime.now(timezone.utc)
    log("START", topic=a.topic, cmd=a.cmd, tool=f"comment_title_ideas.py {VERSION}")
    res = cmd_candidates(a.topic, now) if a.cmd == "candidates" else cmd_match(a.topic, now)
    log("DONE", cmd=a.cmd, items=len(res) if isinstance(res, dict) else "-")


if __name__ == "__main__":
    main()
