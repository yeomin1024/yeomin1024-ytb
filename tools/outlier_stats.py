#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-12 — 신규: tools/outlier_research.py 결과로 data_insights 의 숫자를 다시 계산 (재현용, 해석 없음)
#          ① 제목·길이·채널 크기별 성공 비율 (candidates.csv — 구독자 5만 이하·365일 안·4분 이상·주제 낱말이 든 롱폼)
#          ② 성공 사례 댓글을 낱말 규칙으로 나눈 시청자 니즈 (사례 폴더의 comments.csv, 한 댓글이 여러 갈래에 들 수 있음)
r"""
사용법 (저장소 최상위):
  python3 tools/outlier_stats.py stock                       # 둘 다 (자료가 있는 것만)
  python3 tools/outlier_stats.py stock --skip-ranks 1,7,11,13,15   # 댓글 분류에서 뺄 사례 순위 (주제 밖·광고 의심)
  python3 tools/outlier_stats.py stock --group "실패=2,3,5,6,10,17,19,20" --group "해봄·제도=4,8,9,12,14,16,18"

성공 = 조회수 1만 이상 그리고 조회수 ≥ 구독자 × 3 (outlier_research 기준과 같음, 구독자 100 미만은 100으로).
댓글 분류는 낱말 규칙이라 거칠다: '질문'은 물음표·'~나요'를 세므로 반문도 들어가고, AI 를 다룬 영상에서는 'AI' 가 비판으로 잘못 셀 수 있다.
로그: [STAGE] [시각] key=value
※ 연구·교육용. 투자 권유가 아니다.
"""
import argparse
import csv
import glob
import json
import logging
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VERSION = "v1.0"
LOG = logging.getLogger("outlier_stats")

# 주식 주제 낱말 (제목에 하나라도 있어야 비교 집단에 넣음)
TOPIC_RE = {"stock": r"주식|주가|증시|코스피|코스닥|나스닥|ETF|etf|S&P|에스앤피|배당|빚투|신용|미수|반대매매|물타기|손절|종목|개미|레버리지|리딩방|투자|퇴직금|노후자금|연금|ISA|isa|삼성전자|하이닉스|반도체"}
TOPIC_RE["stock_backup"] = TOPIC_RE["stock"]   # 옛 주식 폴더 (2026-10-12 백업)
MONEY = r"\d[\d,\.]*\s*(?:억|천만|만\s*원|만원|천\s*만|백만|원)"
TITLE_FEATURES = {
    "금액(억·만원)": MONEY,
    "두 금액(반전)": rf"{MONEY}.*?{MONEY}",
    "물음표 ?": r"\?",
    "느낌표 !": r"!",
    "패턴형(공통점·특징·이유·N가지·착각·과정)": r"공통점|특징|이유|\d\s*가지|착각|과정|패턴",
    "공통점": r"공통점|공통적",
    "이유": r"이유",
    "N가지": r"\d\s*가지",
    "과정·벌어진 일·결말·결국": r"과정|벌어진 일|결말|결국",
    "손실 낱말(망하·날린·잃은·반토막)": r"망하|망한|망했|날린|날려|잃은|잃고|잃는|반토막",
    "노후·퇴직금·은퇴·50~70대": r"노후|퇴직금|은퇴|[5-7]0대|예순|환갑",
    "사연·오디오북·실화·고백": r"사연|오디오북|실화|고백",
    "직접·해보니·N년 기록": r"직접|해보니|해봤|만들어봤|\d+\s*년\s*(?:투자|굴|동안|차)|후기",
    "vs 비교": r"\bvs\b|VS|대\s",
    "S&P500·ETF·지수·나스닥": r"S&P|ETF|etf|지수|나스닥",
    "빚투·신용·미수·레버리지·대출": r"빚투|신용|미수|레버리지|대출|빚",
    "AI": r"AI|ai|인공지능",
    "코스피·폭락·급락·하락장": r"코스피|폭락|급락|하락장",
}
COMMENT_CATS = {
    "경험(내 얘기·나도 잃음)": r"저도|제가|나도|내가|내 ?얘기|내 ?이야기|제 ?얘기|제 ?이야기|난가|뜨끔|물렸|물려|잃었|날렸|날린|마이너스|-\d+|손절했|반토막|깡통|빚투했|해봤|경험",
    "원칙·정답(시청자가 스스로 씀)": r"해야|하지 ?마|말아라|마세요|정답|답이|답은|원칙|장기 ?투자|여유 ?자금|여윳돈|분산|적립|지수|S&P|슨피|ETF|etf|욕심|버티|존버|손절 ?(잘|해야|라인)|기준",
    "질문": r"\?|나요|까요|궁금|어떻게 해야|어떻게 하",
    "칭찬·감사": r"감사|고맙|좋은 ?(영상|정보|내용)|도움|최고|공감|잘 ?(들었|보고|배우)|유익|뼈때|뼈 ?때|명언|울림|감동",
    "비판(가짜·AI·뻔함)": r"거짓|소설|가짜|실화 ?아니|AI|ai|에이아이|뻔한|다 아는|광고|강의팔이|짜집기|올드|똑같",
    "도덕적 비난(도박·본인 책임)": r"도박|책임|구제|탕감|한심|역겹|자업자득|본인 ?(몫|탓)|노름",
    "2026 시장(폭락·불장·서킷)": r"폭락|불장|서킷|사이드카|삼전|닉스|하이닉스|코스피|국장|7월",
    "빚·신용·미수": r"빚|신용|미수|대출|레버",
    "요청": r"다음 ?(영상|편)|부탁|해 ?주세요|알려 ?주|올려 ?주",
}


def log(stage, level=logging.INFO, **kv):
    LOG.log(level, "[%s] [%s] %s", stage, datetime.now().isoformat(timespec="seconds"),
            " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) and ' ' in v else v}" for k, v in kv.items()))


def rate(group):
    n = len(group)
    s = sum(r["ok"] for r in group)
    return f"{s}/{n}({s / n:.0%})" if n else "0/0"


def title_stats(topic, max_subs=50000, max_age=365, min_min=4.0):
    p = ROOT / topic / "result" / "outliers" / "candidates.csv"
    if not p.is_file():
        log("TITLE", logging.WARNING, topic=topic, note="candidates.csv 없음 — outlier_research.py 를 먼저 (API 검색)", file=str(p.relative_to(ROOT)))
        return None
    rel = re.compile(TOPIC_RE.get(topic, r"."))
    pop = []
    for r in csv.DictReader(open(p, encoding="utf-8-sig")):
        try:
            subs, views, age, mins = int(r["subs"]), int(r["views"]), int(r["age_days"]), float(r["minutes"])
        except (TypeError, ValueError):
            continue
        if subs > max_subs or age > max_age or mins < min_min or not rel.search(r["title"] or ""):
            continue
        r.update(subs=subs, views=views, mins=mins, ok=views >= 10000 and views >= 3 * max(subs, 100))
        pop.append(r)
    if not pop:
        log("TITLE", logging.WARNING, topic=topic, note="비교 집단 0개")
        return None
    log("TITLE", topic=topic, population=len(pop), success=sum(r["ok"] for r in pop), rate=f"{sum(r['ok'] for r in pop) / len(pop):.3f}",
        rule=f"구독자≤{max_subs}·{max_age}일 안·{min_min}분 이상·주제 낱말")
    print(f"\n## 제목 요소 (비교 집단 {len(pop)}개, 성공 {rate(pop)})\n\n| 요소 | 있음 | 없음 |\n|---|---|---|")
    for k, pat in TITLE_FEATURES.items():
        has = [r for r in pop if re.search(pat, r["title"])]
        no = [r for r in pop if not re.search(pat, r["title"])]
        print(f"| {k} | {rate(has)} | {rate(no)} |")
    for name, key, edges in (("제목 길이(공백 포함 글자)", lambda r: len(r["title"]), (0, 30, 40, 50, 66, 10**6)),
                             ("영상 길이(분)", lambda r: r["mins"], (4, 8, 12, 20, 40, 10**6)),
                             ("구독자", lambda r: r["subs"], (0, 1000, 5000, 20000, max_subs + 1))):
        print(f"\n| {name} | 성공 |\n|---|---|")
        for lo, hi in zip(edges, edges[1:]):
            g = [r for r in pop if lo <= key(r) < hi]
            if g:
                print(f"| {lo}~{hi - 1 if hi < 10**6 else ''} | {rate(g)} |")
    return pop


def comment_needs(topic, skip, groups):
    cases = sorted(glob.glob(str(ROOT / topic / "result" / "outliers" / "[0-9][0-9]_*")))
    if not cases:
        log("COMMENTS", logging.WARNING, topic=topic, note="사례 폴더 없음 (git 에 올라가지 않음 — outlier_research.py 를 다시)")
        return None

    def count(ranks):
        tot = {k: [0, 0] for k in COMMENT_CATS}
        n = likes = 0
        for d in cases:
            m = json.load(open(Path(d) / "metadata.json", encoding="utf-8"))
            if (ranks is None and m["rank"] in skip) or (ranks is not None and m["rank"] not in ranks):
                continue
            for c in csv.DictReader(open(Path(d) / "comments.csv", encoding="utf-8-sig")):
                t, lk = c["text"], int(c["likes"] or 0)
                n += 1
                likes += lk
                for k, pat in COMMENT_CATS.items():
                    if re.search(pat, t):
                        tot[k][0] += 1
                        tot[k][1] += lk
        return n, likes, tot

    for name, ranks in [("전체 (뺀 사례: " + ",".join(map(str, sorted(skip))) + ")", None)] + list(groups.items()):
        n, likes, tot = count(ranks)
        log("COMMENTS", topic=topic, group=name, comments=n, likes=likes)
        if not n:
            continue
        print(f"\n## 댓글 — {name}: {n}개 · 좋아요 {likes:,}\n\n| 갈래 | 댓글 | 좋아요 |\n|---|---|---|")
        for k, (c, lk) in sorted(tot.items(), key=lambda x: -x[1][1]):
            print(f"| {k} | {c} ({c / n:.0%}) | {lk:,} ({lk / max(likes, 1):.0%}) |")
    return True


def main():
    ap = argparse.ArgumentParser(description="outlier_research 결과로 제목 요소·댓글 니즈 숫자 다시 계산 (해석 없음)")
    ap.add_argument("topic")
    ap.add_argument("--skip-ranks", default="", help="댓글 분류에서 뺄 사례 순위 (쉼표)")
    ap.add_argument("--group", action="append", default=[], help='이름=순위,순위… (예: "실패=2,3,5")')
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args()
    logging.basicConfig(level=getattr(logging, a.log_level), format="%(message)s", stream=sys.stderr)
    skip = {int(x) for x in a.skip_ranks.split(",") if x.strip()}
    groups = {}
    for g in a.group:
        name, _, ranks = g.partition("=")
        groups[name] = {int(x) for x in ranks.split(",") if x.strip()}
    log("START", topic=a.topic, tool=f"outlier_stats.py {VERSION}", skip=",".join(map(str, sorted(skip))) or "-", groups=len(groups))
    title_stats(a.topic)
    comment_needs(a.topic, skip, groups)


if __name__ == "__main__":
    main()
