#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-11-06 — 최초. 이번 주(탐색 창 안, 올린 지 7일 이상) 한국어 작은 채널 영상의 소재·제목 꼴·댓글 묶음 —
#          제목 후보의 근거 숫자 (사용자 지시 2026-11-06 "분석 코드 돌려서 이번주 성공사례 찾아서 분석 후 조회수가 잘 나올만할 제목 찾되
#          최근 상황에서 소재를 발견해서 지어야해 그리고 너가 그렇게 생각한 근거들도 말하고").
#
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.0 | 2026-11-06 | 최초 — 소재별 성공 비율(themes) · 제목 꼴(titles, content_analysis.TITLE_TYPES 그대로) · 성공 사례 댓글 묶음(comments) | 전부 |
#
# 모집단 = stock/result/web/explore.json 의 탐색 창 안(in_window) · 롱폼 4분 이상 · 주제 관련(relevant) · 한국어 제목 · 푼 추천(dismissed) 뺌 ·
#          구독자 5만 이하 · 올린 지 7일 이상 (성공 판정이 가능한 영상만 — analysis_rules.toml [success] MIN_AGE_DAYS).
# 성공 = analysis_rules.toml [success] 와 같은 기준: 조회수 1만 이상 · 구독자당 하루 조회수 ≥ 0.1 (구독자 100 미만은 100).
# 할당량 0 (받아 둔 탐색 목록·사례 폴더만 읽음). 표본 15개 미만 묶음은 '표본 적음' 표시 — 규칙으로 만들지 않음.
# 실행: python3 -B stock/topics/week_scan.py [--extra-dismiss ID …] [--log-level DEBUG] → stdout (표 3개) · --json <파일>
# ※ 연구·교육용 — 투자 권유가 아님.
import argparse
import collections
import json
import logging
import re
import statistics as st
import sys
from datetime import datetime
from pathlib import Path

VERSION = "v1.0"
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import content_analysis as ca  # noqa: E402  제목 꼴 규칙을 분석 도구와 같게

WEB = ROOT / "stock" / "result" / "web"
CASES = ROOT / "stock" / "result" / "outliers"
MIN_N = 15
THEMES = {
    "중간선거·민주당·트럼프": r"중간\s?선거|민주당|트럼프|블루\s?쓰나미|선거",
    "AI 거품·데이터센터·빅테크": r"AI|인공지능|데이터센터|빅테크|엔비디아|구글|앤트로픽|버블|거품",
    "반도체·삼전닉스": r"반도체|삼성전자|하이닉스|삼전|닉스|HBM|SOX|필라델피아",
    "코스피 폭락·5000 붕괴": r"코스피.*(폭락|급락|붕괴|빠|하락|떡락|위기)|(폭락|급락|붕괴).*코스피|5[,.]?000|5천",
    "나스닥 폭락": r"나스닥.*(폭락|급락|하락|멸망|위험|떡락)|(폭락|급락).*나스닥",
    "폭락·급락 일반": r"폭락|급락|대폭락|하락장|떡락|검은 월요일|붕괴",
    "물린 주식·손절·손실": r"물린|물타기|손절|손실|잃|반토막|마이너스|-\d+%",
    "배당·특별배당·주주환원": r"배당|분배금|주주환원",
    "커버드콜·월배당 ETF": r"커버드콜|월배당|SCHD|QQQI|GPIQ|JEPI",
    "빚투·신용·레버리지": r"빚투|신용|레버리지|청산|SOXL|TQQQ|QLD",
    "외국인 매도": r"외국인",
    "환율": r"환율|달러|엔저",
    "장기투자·적립·S&P500": r"장기\s?투자|적립|S&P\s?500|지수|ETF",
    "은퇴·노후·파이어": r"은퇴|노후|파이어|연금|퇴직",
    "공포·버티기·멘탈": r"공포|버텨|버티|무서|두려|멘탈|후회|패닉",
    "세금·부유세·계좌": r"세금|부유세|억만장자세|ISA|건보료|비과세|계좌",
}
FEATURES = {
    "숫자": r"\d", "물음표": r"\?", "느낌표 !": r"!", "말줄임 ..·…": r"\.\.|…", "따옴표": r"[\"'“”‘’]", "금액(원·억·만·조)": r"\d[\d,.]*\s?(원|억|만|조)",
    "%": r"%", "폭락·급락·붕괴": r"폭락|급락|붕괴|떡락", "실제 계좌·공개": r"계좌|공개|실제", "1인칭 경험": r"제가|저는|내가|나는|내 |저의|했습니다|었습니다",
    "얼마": r"얼마", "이유·왜": r"이유|왜", "'이렇게'": r"이렇게",
}
NEEDS = {
    "손실 고백·멘탈": r"손실|잃|마이너스|-\d+%|반토막|물렸|물려|멘탈|잠이|무섭|공포|힘들",
    "배당·월배당·커버드콜": r"배당|분배금|커버드콜|월배당|SCHD|슈드|QQQI|JEPI|JEPQ",
    "장기·적립·지수": r"장기|적립|S&P|에스앤피|지수|ETF|모아가|존버|버티",
    "버틸까·팔까(매도·손절)": r"팔아|팔까|매도|손절|던져|던질|정리할|탈출",
    "얼마나 더 빠지나·바닥": r"바닥|어디까지|더 빠|반등|지하실|언제까지",
    "은퇴·노후·연금": r"은퇴|노후|연금|퇴직|ISA|IRP",
    "더 살까·물타기(매수)": r"물타|추매|추가\s?매수|더 사|매수할|줍줍|사야|살까|분할",
    "레버리지·빚투": r"레버리지|TQQQ|SOXL|QLD|빚|신용|미수|대출",
    "비판·광고·공포 조장": r"공포\s?조장|광고|리딩|사기|선동|낚시|어그로|구라",
}
QUESTION = r"\?|까요|나요|할까|일까|인가요|어떻게|뭘|어떤"
POLITICS = r"대통령|재명|찢|좌파|우파|민주당|국힘|검찰|정권|정부|윤석열|나라는"

log = logging.getLogger("week_scan")


def L(stage, msg, *a, level=logging.INFO):
    log.log(level, f"[{stage}] [{datetime.now().isoformat(timespec='seconds')}] " + msg, *a)


def load_pool(extra):
    try:
        d = json.loads((WEB / "explore.json").read_text("utf-8"))
        dis = json.loads((WEB / "dismissed.json").read_text("utf-8"))
    except (OSError, ValueError) as e:
        L("DATA", "explore.json·dismissed.json 을 못 읽음 error=%s next=python3 tools/cloud_run.py stock explore 뒤 다시", e, level=logging.ERROR)
        raise
    dis = set(dis if isinstance(dis, list) else dis.keys()) | set(extra)
    ko = lambda s: bool(re.search("[가-힣]", s or ""))  # noqa: E731
    seen, rows = set(), []
    for r in d["rows"]:
        if r["id"] in seen:
            continue
        seen.add(r["id"])
        if (r.get("in_window") and not r.get("short") and r.get("relevant") and (r.get("minutes") or 0) >= 4 and ko(r["title"])
                and r["id"] not in dis and r["subs"] <= 50000 and r["age_days"] >= 7):
            r["success"] = r["views"] >= 10000 and r["views_per_day"] / max(r["subs"], 100) >= 0.1
            rows.append(r)
    ages = [r["age_days"] for r in rows]
    L("DATA", "explore_generated=%s weeks=%s pool=%d success=%d (%.0f%%) age_days=%d~%d dismissed=%d",
      d.get("generated"), d.get("weeks"), len(rows), sum(r["success"] for r in rows), 100 * sum(r["success"] for r in rows) / max(len(rows), 1),
      min(ages, default=0), max(ages, default=0), len(dis))
    return rows


def themes(rows):
    base = sum(r["success"] for r in rows) / max(len(rows), 1)
    out = []
    for k, p in THEMES.items():
        rs = [r for r in rows if re.search(p, r["title"])]
        s = sum(r["success"] for r in rs)
        out.append({"theme": k, "n": len(rs), "success": s, "rate": s / len(rs) if rs else 0, "vs_base_pp": 100 * ((s / len(rs) if rs else 0) - base),
                    "small_sample": len(rs) < MIN_N})
    out.sort(key=lambda x: -x["rate"])
    L("CALC", "themes=%d base_rate=%.1f%% top=%s", len(out), 100 * base, out[0]["theme"] if out else "-")
    return base, out


def titles(rows):
    S = [r for r in rows if r["success"]]
    N = [r for r in rows if not r["success"]]
    def row(name, hit):
        a = sum(hit(r["title"]) for r in S); b = sum(hit(r["title"]) for r in N)
        return {"name": name, "success_share": a / max(len(S), 1), "other_share": b / max(len(N), 1),
                "diff_pp": 100 * (a / max(len(S), 1) - b / max(len(N), 1)), "rate": a / max(a + b, 1), "n": a + b, "small_sample": a + b < MIN_N}
    types = [row(t, lambda s, t=t: t in ca.title_types(s)) for t, _ in ca.TITLE_TYPES]
    feats = [row(k, lambda s, p=p: bool(re.search(p, s))) for k, p in FEATURES.items()]
    lens = {"success_median": st.median(len(r["title"]) for r in S) if S else 0, "other_median": st.median(len(r["title"]) for r in N) if N else 0}
    L("CALC", "title_types=%d features=%d success=%d other=%d len_median=%s", len(types), len(feats), len(S), len(N), lens)
    return types, feats, lens


def comments(rows):
    allc, have, seen = [], 0, set()
    for r in rows:
        if not r["success"]:
            continue
        f = CASES / f"W_{r['id']}" / "comments.jsonl"
        if not f.exists():
            continue
        have += 1
        for line in f.open(encoding="utf-8"):
            c = json.loads(line)
            if c.get("creator") or c.get("parent") or c["id"] in seen:
                continue
            seen.add(c["id"]); c["vtitle"] = r["title"]; allc.append(c)
    cnt, likes = collections.Counter(), collections.Counter()
    for c in allc:
        for k, p in NEEDS.items():
            if re.search(p, c["text"]):
                cnt[k] += 1; likes[k] += c.get("likes") or 0
    nonpol = [c for c in allc if not re.search(POLITICS, c["text"])]
    q = sorted((c for c in nonpol if re.search(QUESTION, c["text"])), key=lambda c: -(c.get("likes") or 0))
    top = sorted(nonpol, key=lambda c: -(c.get("likes") or 0))
    L("CALC", "success_with_comments=%d top_level=%d non_political=%d questions=%d", have, len(allc), len(nonpol), len(q))
    return {"cases": have, "comments": len(allc), "needs": [{"need": k, "n": n, "share": n / max(len(allc), 1), "likes": likes[k]} for k, n in cnt.most_common()],
            "top_questions": [{"likes": c["likes"], "video": c["vtitle"][:40], "text": c["text"][:160]} for c in q[:15]],
            "top_comments": [{"likes": c["likes"], "video": c["vtitle"][:40], "text": c["text"][:160]} for c in top[:15]]}


def show(base, th, types, feats, lens, cm):
    pct = lambda x: f"{100 * x:.0f}%"  # noqa: E731
    print(f"\n## 소재별 성공 비율 (기준 {pct(base)})\n| 소재 | 영상 | 성공 | 성공 비율 | 기준 대비 | 표시 |\n|---|---|---|---|---|---|")
    for t in th:
        print(f"| {t['theme']} | {t['n']} | {t['success']} | {pct(t['rate'])} | {t['vs_base_pp']:+.0f}%p | {'표본 적음' if t['small_sample'] else ''} |")
    for title, rows in (("제목 꼴 (content_analysis.TITLE_TYPES)", types), ("낱말·기호", feats)):
        print(f"\n## {title}\n| 꼴 | 성공 몫 | 그 밖 몫 | 차이 | 그 꼴 성공 비율 (n) | 표시 |\n|---|---|---|---|---|---|")
        for r in sorted(rows, key=lambda r: -r["diff_pp"]):
            print(f"| {r['name']} | {pct(r['success_share'])} | {pct(r['other_share'])} | {r['diff_pp']:+.1f}%p | {pct(r['rate'])} ({r['n']}) | {'표본 적음' if r['small_sample'] else ''} |")
    print(f"\n제목 길이 중앙값: 성공 {lens['success_median']} · 그 밖 {lens['other_median']}")
    print(f"\n## 성공 사례 댓글 묶음 (사례 {cm['cases']} · 댓글 {cm['comments']}, 채널 주인·답글 뺌)\n| 묶음 | 댓글 | 몫 | 좋아요 합 |\n|---|---|---|---|")
    for n in cm["needs"]:
        print(f"| {n['need']} | {n['n']} | {100 * n['share']:.1f}% | {n['likes']:,} |")
    print("\n좋아요 상위 질문 (정치 댓글 뺌)")
    for c in cm["top_questions"]:
        print(f"- 👍{c['likes']} [{c['video']}] {c['text']!r}")


def main(argv=None):
    ap = argparse.ArgumentParser(description="이번 주 소재·제목 꼴·댓글 묶음 (할당량 0, 연구·교육용)")
    ap.add_argument("--extra-dismiss", nargs="*", default=["xzEnoz6ew1M", "VOBcxHQf8X8"], help="모집단에서 더 뺄 영상 ID (기본: 2026-11-06 눈으로 뺀 무당·벽 미장)")
    ap.add_argument("--json", default="", help="결과를 JSON 으로도 저장")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args(argv)
    logging.basicConfig(level=a.log_level, format="%(message)s")
    L("START", "version=%s", VERSION)
    rows = load_pool(a.extra_dismiss)
    base, th = themes(rows)
    types, feats, lens = titles(rows)
    cm = comments(rows)
    show(base, th, types, feats, lens, cm)
    if a.json:
        Path(a.json).write_text(json.dumps({"version": VERSION, "base": base, "themes": th, "title_types": types, "features": feats, "lens": lens,
                                            "comments": cm}, ensure_ascii=False, indent=1), "utf-8")
        L("END", "saved=%s", a.json)


if __name__ == "__main__":
    main()
