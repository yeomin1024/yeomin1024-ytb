#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-14 — 최초 작성 (사용자 지시 "지금까지 했던 주제 탐색, 제목 생성, 대본 생성을 어떻게 했는지와 피드백을 반영해서
#          각각 지시사항 파일을 만들고"): 2026-10-14 대화에서 임시 스크립트로 한 분석(시청자 나이·질문 묶음, 제목 형식·낱말·맨 앞 말,
#          성공 대본 말투·전개 장치, 댓글 칭찬·불만, 새 대본 측정)을 명령 하나로 모음. 지시사항: guides/topic_guide.md · title_guide.md · script_guide.md
"""
콘텐츠 연구 — 분석 결과(PC 가 올린 `<주제>/result/outliers/`)로 주제·제목·대본 지시사항의 숫자를 다시 낸다. 할당량 0, 네트워크 없음.

  python3 tools/content_research.py audience economic      # 댓글에서 밝힌 나이 → 주요 시청자층
  python3 tools/content_research.py needs economic         # 질문·요청 댓글 → 묶음별 개수·좋아요·영상 수 + 원문
  python3 tools/content_research.py titles economic        # 제목 형식·낱말·맨 앞 말 → 성공 비율(비교 집단·좁힌 주제·같은 채널) + 검색 수요
  python3 tools/content_research.py style economic         # 성공 사례 대본(음성인식 앞 5분) → 말투·문장 길이·시점·전개 장치
  python3 tools/content_research.py feedback economic      # 성공 사례 댓글 → 내용·전달에 대한 칭찬·불만 + 원문
  python3 tools/content_research.py measure <대본.txt> [--compare <옛 대본.txt>]   # 새 대본을 성공 사례와 같은 규칙으로 잼
  python3 tools/content_research.py all economic --out /tmp/research.md            # 위 다섯 개를 한 파일로

자료
  - analysis.json · compare.csv · W_*/transcript.json · <사례 폴더>/comments.csv (tools/success_analysis.py 결과)
  - 주제별 낱말 규칙: `<주제>/research_rules.toml` (예: economic/research_rules.toml). 없으면 묶음 분석은 건너뛴다.

해석 주의 (지시사항에 그대로 옮김)
  - 성공 = 180일 안·구독자 5만 이하·조회수 ≥ 구독자×3·1만 회 이상·4분 이상 (analysis_rules.toml). 비교 집단은 조회수 순 검색이라 성공 비율이 높게 나온다.
  - '같은 채널'은 compare.csv 로 근사한 기준선(채널 중앙값×3↑ = 잘된 영상, ×0.5~1.5 = 평소 영상, 채널마다 5개)이다.
  - 표본 15개 미만은 '표본 적음'으로 표시한다. 차이를 규칙으로 만들 때는 비교 집단·같은 채널이 같은 방향인지 본다.
  - 대본 지표는 음성인식 '앞 5분'만 있다(1차). '많이 쓰인다'이지 '그래서 잘됐다'는 아니다.
  - 정규식 분류는 엉뚱하게 걸린 댓글이 섞인다 → 원문을 함께 보고 판단한다.

로그: `[STAGE] 시각 key=value …` (stderr, --log-level DEBUG/INFO/WARNING). 표는 stdout.
연구·교육용 도구다. 투자·세무 권유가 아니다.
"""
import argparse
import collections
import csv
import json
import logging
import re
import statistics
import sys
import time
from pathlib import Path

try:
    import tomllib
except ImportError:  # pragma: no cover - 3.11 미만
    tomllib = None

VERSION = "v1.0"
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

LOG = logging.getLogger("content_research")


def log(stage, level=logging.INFO, **kv):
    LOG.log(level, "[%s] %s %s", stage, time.strftime("%Y-%m-%dT%H:%M:%S"), " ".join(f"{k}={v}" for k, v in kv.items()))


# ----------------------------------------------------------------------------- 자료 읽기
class Data:
    """한 주제의 분석 결과. 없는 파일은 친절한 메시지와 함께 멈춘다."""

    def __init__(self, topic):
        self.topic = topic
        self.out = ROOT / topic / "result" / "outliers"
        path = self.out / "analysis.json"
        if not path.is_file():
            raise SystemExit(f"[LOAD] ❌ {path} 없음 → PC 분석(guides/pc_analysis.md)을 먼저 돌려 주세요")
        try:
            self.a = json.load(open(path, encoding="utf-8"))
        except Exception as e:  # noqa: BLE001
            raise SystemExit(f"[LOAD] ❌ {path} 읽기 실패: {e} → 파일이 잘렸으면 PC 에서 다시 올려 주세요")
        self.cases = self.a.get("success_cases") or []
        self.rules = load_rules(topic)
        log("LOAD", topic=topic, generated=self.a.get("generated"), success_cases=len(self.cases), rules=bool(self.rules))
        self._comments = None
        self._compare = None

    # 성공 사례 댓글 (채널 주인·도배 제외)
    def comments(self):
        if self._comments is not None:
            return self._comments
        import success_analysis as sa
        rows, missing = [], 0
        for c in self.cases:
            f = self.out / c["folder"] / "comments.csv"
            if not f.is_file():
                missing += 1
                continue
            for r in csv.DictReader(open(f, encoding="utf-8-sig")):
                if str(r.get("creator")) in ("True", "1", "true"):
                    continue
                t = re.sub(r"\s+", " ", r.get("text") or "").strip()
                if not t or re.search(sa.SPAM_RX, t):
                    continue
                rows.append(dict(no=c["no"], theme=c.get("theme") or "", fmt=c.get("format") or "", likes=int(r.get("likes") or 0), t=t))
        if missing:
            log("LOAD", logging.WARNING, comments_missing_cases=missing)
        log("LOAD", comments=len(rows), cases_with_comments=len(self.cases) - missing)
        self._comments = rows
        return rows

    # 비교 집단 + 같은 채널 근사
    def compare(self):
        if self._compare is not None:
            return self._compare
        f = self.out / "compare.csv"
        if not f.is_file():
            raise SystemExit(f"[LOAD] ❌ {f} 없음 → success_analysis.py v1.2 이상이 만든다 (PC 주별 분석)")
        rows = list(csv.DictReader(open(f, encoding="utf-8-sig")))
        bad = 0
        for r in rows:
            try:
                r["views"] = int(float(r["views"] or 0))
                r["age"] = float(r["age_days"] or -1)
                r["min"] = float(r["minutes"] or 0)
            except ValueError:
                bad += 1
                r["views"], r["age"], r["min"] = 0, -1, 0
            r["ok"] = r["success"] == "True"
            r["t"] = re.sub(r"^[\s\"'“‘\[\(【「『]+", "", r["title"])
        group = [r for r in rows if r["in_compare"] == "True"]
        narrow_names = set(self.rules.get("NARROW_THEMES", []))
        narrow = [r for r in group if r["theme"] in narrow_names]
        by = collections.defaultdict(list)
        for r in rows:
            if r["exclude"].startswith("라이브") or r["min"] < 4 or not (7 <= r["age"] <= 365):
                continue
            by[r["channel"]].append(r)
        hits, normal, nch = [], [], 0
        for rs in by.values():
            if len(rs) < 6:
                continue
            nch += 1
            med = statistics.median(x["views"] for x in rs)
            hits += sorted((x for x in rs if not x["exclude"] and x["views"] >= 3 * med), key=lambda x: -x["views"])[:5]
            normal += sorted((x for x in rs if not x["exclude"] and 0.5 * med <= x["views"] <= 1.5 * med), key=lambda x: x["age"])[:5]
        if bad:
            log("LOAD", logging.WARNING, compare_bad_rows=bad)
        log("LOAD", compare_rows=len(rows), group=len(group), group_success=sum(r["ok"] for r in group),
            narrow=len(narrow), channels=nch, hits=len(hits), normal=len(normal))
        self._compare = dict(group=group, narrow=narrow, hits=hits, normal=normal, channels=nch)
        return self._compare


def load_rules(topic):
    f = ROOT / topic / "research_rules.toml"
    if not f.is_file():
        log("RULES", logging.WARNING, missing=f, note="묶음·낱말 분석 건너뜀 — economic/research_rules.toml 을 본떠 만드세요")
        return {}
    if tomllib is None:
        raise SystemExit("[RULES] ❌ Python 3.11 이상이 필요합니다 (tomllib)")
    try:
        return tomllib.loads(f.read_text("utf-8"))
    except Exception as e:  # noqa: BLE001
        raise SystemExit(f"[RULES] ❌ {f} 읽기 실패: {e}")


pct = lambda v: "  -" if v is None else f"{v * 100:3.0f}%"


def rate(rows, fn):
    w = [x for x in rows if fn(x)]
    wo = [x for x in rows if not fn(x)]
    f = lambda s: (sum(x["ok"] for x in s) / len(s)) if s else None
    return len(w), f(w), f(wo)


def md(text):
    """마크다운 표 칸 안의 '|' 를 이스케이프."""
    return str(text).replace("|", "\\|")


def compare_line(cmp, name, fn, show_examples=0):
    name = md(name)
    n, a, b = rate(cmp["group"], fn)
    m, c, d = rate(cmp["narrow"], fn)
    hk = sum(1 for x in cmp["hits"] if fn(x))
    nk = sum(1 for x in cmp["normal"] if fn(x))
    h = hk / len(cmp["hits"]) if cmp["hits"] else None
    nm = nk / len(cmp["normal"]) if cmp["normal"] else None
    diff = "  -" if a is None or b is None else f"{(a - b) * 100:+3.0f}"
    hd = "  -" if h is None or nm is None else f"{(h - nm) * 100:+3.0f}"
    flag = "표본적음" if n < 15 else ""
    print(f"| {name} | {n} | {pct(a)} | {pct(b)} | {diff} | {flag} | {m} | {pct(c)} | {pct(d)} | {pct(h)} ({hk}) | {pct(nm)} ({nk}) | {hd} |")
    if show_examples:
        ex = sorted((x for x in cmp["group"] if fn(x) and x["ok"]), key=lambda x: -float(x["ratio"] or 0))[:show_examples]
        for x in ex:
            print(f"|  ↳ 성공 예: {md(x['title'][:70])} ({x['views']:,}회·×{float(x['ratio'] or 0):.1f}) | | | | | | | | | | | |")


def compare_header(first="항목"):
    print(f"| {first} | 비교 n | 있음 성공 | 없음 성공 | 차이 | | 좁힌 주제 n | 있음 | 없음 | 같은 채널 잘된 | 평소 | 차이 |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|")


# ----------------------------------------------------------------------------- 1. 시청자층
AGE_RX = re.compile(r"(?<!\d)([2-8])0\s*대|(?<!\d)([2-8]\d)\s*(?:세|살)")


def cmd_audience(d):
    rows = d.comments()
    ages = collections.Counter()
    for x in rows:
        m = AGE_RX.search(x["t"])
        if m:
            dec = m.group(1) or m.group(2)[0]
            ages[dec + "0대"] += 1
    tot = sum(ages.values())
    print(f"\n## 시청자층 — 댓글에서 밝힌 나이 ({tot}개 / 댓글 {len(rows):,}개)\n")
    if not tot:
        print("- 나이를 밝힌 댓글이 없다 → 근거 없음")
        return
    print("| " + " | ".join(sorted(ages)) + " | 50대 이상 |")
    print("|" + "---|" * (len(ages) + 1))
    over50 = sum(v for k, v in ages.items() if k[0] in "5678")
    print("| " + " | ".join(f"{ages[k]} ({ages[k] / tot:.0%})" for k in sorted(ages)) + f" | {over50 / tot:.0%} |")
    log("AUDIENCE", age_mentions=tot, over50=f"{over50 / tot:.2f}")


# ----------------------------------------------------------------------------- 2. 시청자 니즈 (질문 묶음)
def cmd_needs(d, top=6):
    import success_analysis as sa
    rules = d.rules
    clusters = rules.get("NEED_CLUSTERS") or {}
    if not clusters:
        print("\n## 질문 묶음 — research_rules.toml 의 NEED_CLUSTERS 가 없어 건너뜀")
        return
    rows = d.comments()
    want = [x for x in rows if sa.CAT_ASK in sa.classify_comment(x["t"]) or re.search(r"궁금", x["t"])]
    core_rx = re.compile(rules.get("CORE_CONTEXT") or r"$^")
    prefix = rules.get("CORE_THEME_PREFIX") or "\0"
    core = [x for x in want if x["theme"].startswith(prefix) or core_rx.search(x["t"])]
    print(f"\n## 시청자가 원하는 정보 — 질문·요청·'궁금' 댓글 {len(want):,}개 중 핵심 시청자 질문 {len(core)}개\n")
    print(f"- 핵심 시청자 = 주제 묶음 '{prefix}…' 영상에 달렸거나, `{rules.get('CORE_CONTEXT')}` 가 든 질문. 한 질문이 여러 묶음에 들 수 있다.\n")
    res = []
    for k, rx in clusters.items():
        hits = [x for x in core if re.search(rx, x["t"])]
        res.append((k, hits))
    print("| 묶음 | 질문 | 👍 합 | 영상 |")
    print("|---|---|---|---|")
    for k, hits in sorted(res, key=lambda r: -len(r[1])):
        print(f"| {k} | {len(hits)} | {sum(h['likes'] for h in hits)} | {len({h['no'] for h in hits})} |")
    for name, members in (rules.get("NEED_UNIONS") or {}).items():
        rx = re.compile("|".join(clusters[m] for m in members if m in clusters))
        u = [x for x in core if rx.search(x["t"])]
        print(f"| **{name}** (합집합) | **{len(u)}** | {sum(x['likes'] for x in u)} | {len({x['no'] for x in u})} |")
        log("NEEDS", union=name, questions=len(u), likes=sum(x["likes"] for x in u))
    for k, hits in sorted(res, key=lambda r: -len(r[1])):
        if not hits:
            continue
        print(f"\n### {k} — 좋아요 많은 원문")
        for h in sorted(hits, key=lambda h: -h["likes"])[:top]:
            print(f"- 👍{h['likes']} #{h['no']} {h['t'][:160]}")
    log("NEEDS", want=len(want), core=len(core), clusters=len(clusters))


# ----------------------------------------------------------------------------- 3. 제목
TITLE_FORMS = {
    "경고① 모르면·놓치면·안 하면": r"모르면|모르고|모른다면|놓치면|안 ?하면|않으면|안 ?받으면",
    "경고② 폭탄·날벼락·손해·함정": r"폭탄|날벼락|손해|함정|토해|뜯기|떼인|벌금|세금 ?폭탄",
    "경고③ 하지 마세요·절대 (금지)": r"하지 ?마|마세요|말아야|말라|절대",
    "경고④ 후회·큰일·위험·주의": r"후회|큰일|위험|주의|조심|실수|망",
    "해결① 방법·하는 법·비법·전략·팁": r"방법|하는 ?법|받는 ?법|버는 ?법|모으는 ?법|만드는 ?법|비법|노하우|전략|꿀팁|팁",
    "해결② 이렇게·이것만·만 하면": r"이렇게|이것만|이것부터|이거 ?하나|만 ?하면|만 ?알면|만 ?지키면",
    "해결③ 순서·공식·로드맵·단계·총정리": r"순서|공식|로드맵|단계|체크리스트|총정리|완벽 ?정리",
    "해결④ 덜 내는·아끼는·줄이는": r"덜 ?내|아끼|아낄|줄이|줄여|안 ?내|0원|절약|절세",
    "해결⑤ ~하세요 (권유·명령)": r"하세요|받으세요|보세요|넣으세요|꺼내세요|챙기세요|드세요|하십시오|해라|하라\b",
    "결과① 월·매달 N만 원": r"(월|매달|매월|한 ?달)\s*\d[\d,]*\s*만\s*원?",
    "결과② N억·N천만 원 (목돈)": r"\d[\d,.]*\s*억|\d\s*천\s*만",
    "질문① 물음표·~일까·~나요": r"\?|일까|할까|될까|나요|까요|인가",
    "호기심① 진짜·사실·몰랐던·비밀": r"진짜|사실은|사실 |아무도|몰랐던|비밀|안 ?알려|의외|정체|진실",
    "호기심② 이유·때문": r"이유|때문",
    "호기심③ 지시어 이것·이렇게·이 OO": r"이것|이거|이렇게|이때|이걸|(?<![가-힣])이 ?(순서|방법|돈|통장|계좌|선|한 ?가지|숫자|차이|습관|실수|사람|정도|금액)",
    "대상① 50~70대·은퇴자·부부·~라면": r"[5-8]0대|[5-8]\d\s*세|은퇴자|은퇴 ?후|부부|라면|이라면|분들",
    "사연① 했더니·해보니·후기·실화·N년": r"했더니|해보니|해봤|후기|실화|사연|\d+\s*년\s*(?:동안|째|차|만에)",
    "비교① vs·차이·보다": r"\bvs\b|VS|차이|보다 ",
    "목록① N가지·N개·TOP": r"\d\s*가지|\d\s*개\b|TOP|top|베스트",
    "감정① 충격·경악·소름·난리": r"충격|경악|소름|대박|미쳤|난리|발칵|역대급",
    "모양① 두 부분 (ㅣ·|·/·— 로 나눔)": r"[|ㅣ｜/∣]|\s[-—–]\s",
    "모양② 끝이 ~니다·~요": r"(니다|어요|아요|해요|세요|네요|죠)[.!]*\s*$|(니다|어요|아요|해요|세요|네요|죠)[.!]*\s*[|ㅣ｜/∣]",
}
TITLE_COMBOS = {
    "조합A 경고(①②) + 해결(①~④)": (r"모르면|모르고|모른다면|놓치면|안 ?하면|않으면|안 ?받으면|폭탄|날벼락|손해|함정|토해|뜯기|떼인|벌금",
                                  r"방법|하는 ?법|비법|노하우|전략|팁|이렇게|이것만|만 ?하면|순서|공식|로드맵|단계|총정리|덜 ?내|아끼|줄이|절약|절세"),
    "조합D 결과 금액(월·억) + 해결": (r"(월|매달|매월)\s*\d[\d,]*\s*만|\d[\d,.]*\s*억|\d\s*천\s*만",
                                  r"방법|하는 ?법|비법|노하우|전략|팁|이렇게|이것만|만 ?하면|순서|공식|로드맵|단계|총정리|덜 ?내|아끼|줄이|절약|절세"),
    "조합E 대상(50~70대·은퇴·부부) + 결과 금액": (r"[5-8]0대|[5-8]\d\s*세|은퇴자|은퇴 ?후|부부|라면|이라면|분들",
                                         r"(월|매달|매월)\s*\d[\d,]*\s*만|\d[\d,.]*\s*억|\d\s*천\s*만"),
    "월 N만 원 + 손해·덜·날림": (r"(월|매달|매월)\s*\d[\d,]*\s*만", r"손해|날|덜|빠져|깎"),
    "손해 낱말 + 금액(만·억)": (r"손해|날벼락|폭탄|날려|날린", r"\d[\d,]*\s*(만|억)"),
}


def cmd_titles(d):
    cmp = d.compare()
    T = lambda rx: (lambda x: bool(re.search(rx, x["title"])))
    print(f"\n## 제목 — 비교 집단 {len(cmp['group'])}개(성공 {sum(x['ok'] for x in cmp['group'])}) · 좁힌 주제 {len(cmp['narrow'])}개"
          f"(성공 {sum(x['ok'] for x in cmp['narrow'])}) · 같은 채널 잘된 {len(cmp['hits'])} / 평소 {len(cmp['normal'])} ({cmp['channels']}개 채널)\n")
    print("### 형식 (문장 구조)\n")
    compare_header("형식")
    for k, rx in TITLE_FORMS.items():
        compare_line(cmp, k, T(rx))
    for k, (a, b) in TITLE_COMBOS.items():
        compare_line(cmp, k, (lambda a, b: lambda x: bool(re.search(a, x["title"])) and bool(re.search(b, x["title"])))(a, b), show_examples=2)
    print("\n### 길이 (글자)\n")
    compare_header("길이")
    for lo, hi in ((0, 30), (30, 45), (45, 60), (60, 200)):
        compare_line(cmp, f"{lo}~{hi - 1}자", (lambda lo, hi: lambda x: lo <= len(x["title"]) < hi)(lo, hi))
    words = d.rules.get("TITLE_WORDS") or {}
    if words:
        print("\n### 낱말 (주제 규칙 TITLE_WORDS)\n")
        compare_header("낱말")
        for k, rx in words.items():
            compare_line(cmp, k, T(rx))
    leads = d.rules.get("TITLE_LEADS") or {}
    if leads:
        print("\n### 맨 앞(첫 12자)에 오는 말\n")
        compare_header("맨 앞 말")
        for k, rx in leads.items():
            compare_line(cmp, k, (lambda rx: lambda x: bool(re.search(rx, x["t"][:12])))(rx))
    search = d.rules.get("SEARCH") or {}
    mk = d.a.get("market") or {}
    kw = {k["q"]: k for k in mk.get("keywords") or []}
    if search.get("KEYWORD_PROBE") and kw:
        print("\n### 검색 수요 — 검색어 표 (analysis.md 3-2)\n")
        print("| 검색어 | 영상당 하루 조회수 | 작은 채널이 뚫은 비율 | 작은 채널 성공 | 결과 수 | 최근 30일 |")
        print("|---|---|---|---|---|---|")
        for q in search["KEYWORD_PROBE"]:
            x = kw.get(q)
            if not x:
                print(f"| {q} | (검색어 표에 없음) | | | | |")
                continue
            print(f"| {q} | {x.get('vpd_per_video')} | {x.get('small_hit_share')} | {x.get('small_success')} | {x.get('total')} | {x.get('recent30')} |")
    ac = mk.get("autocomplete") or []
    if search.get("AUTOCOMPLETE_FILTER") and ac:
        rx = re.compile(search["AUTOCOMPLETE_FILTER"])
        sel = sorted((x for x in ac if rx.search(x["phrase"])), key=lambda x: -x["score"])[:25]
        print("\n### 자동완성 말 (수요 점수 순, 우리가 본 최근 영상이 적으면 '틈')\n")
        print("| 말 | 수요 점수 | 최근 영상 | 틈 |")
        print("|---|---|---|---|")
        for x in sel:
            print(f"| {md(x['phrase'])} | {x['score']} | {x['pool_recent']} | {x['gap']} |")
    log("TITLES", forms=len(TITLE_FORMS), words=len(words), leads=len(leads))


# ----------------------------------------------------------------------------- 4. 대본 말투·장치
HAN = re.compile(r"[가-힣]")
# 합니다체: '~니다/~니까/~십시오'로 끝남 (2026-10-14 대화의 임시 스크립트는 'ㅂ니다'를 글자 그대로 찾아 '씁니다·갑니다'를 놓쳤음 → 고침)
END_FORMAL = re.compile(r"(니다|니까|십시오)[.?!…]*$")
END_POLITE = re.compile(r"(요|죠|세요|에요|예요|네요|거든요|잖아요|래요|군요|구요)[.?!…]*$")
END_Q = re.compile(r"(\?|까요|나요|가요|죠\?|니까\?|ㄹ까|을까|일까)[.?!…]*$")
TIMING = {"인사(안녕하세요)": r"안녕하세요", "약속(오늘은·알려드리·끝까지)": r"오늘은|오늘 (이 )?영상|알려 ?드리|말씀드리|끝까지",
          "구독·좋아요 요청": r"구독|좋아요|알림"}
# (시간 창 초, 정규식) — 성공 사례는 앞 5분 대본만 있어 창이 300초를 넘지 않는다
DEVICES = {
    "대상 부르기·조건 (첫 30초: ~계시다면·~라면·~분들)": (30, r"계시다면|하신다면|이시라면|라면|분들|분이라면|하시는 분"),
    "숫자로 시작 (첫 15초)": (15, r"\d|만 ?원|억"),
    "질문으로 시작 (첫 15초)": (15, r"\?|까요|나요|십니까|습니까"),
    "장면·이야기로 시작 (첫 15초)": (15, r"아침|저녁|어제|그날|여보|엄마|아버지|지인|친구|\d+시|갔습니다|했습니다"),
    "진행자 속마음 (솔직히·제 생각)": (300, r"솔직히|제 생각|저는 이|개인적으로|저도 처음"),
    "결론·답 먼저 (앞 2분)": (120, r"결론부터|정답|한마디로|먼저 답|답부터|핵심부터"),
    "시청자 스스로 확인 질문": (300, r"(있으셨|계세요|받고 계|하셨나요|있으신가요|계신가요|아시나요|보셨나요)"),
    "예상 반론 짚기": (300, r"하시는 분(들)?(이|도)? (계실|많|있)|생각하시(죠|겠|는)|라고 하시|하실 겁니다|하실 거예요"),
    "비유 (처럼·마치·라고 보시면)": (300, r"처럼|마치|비유|같은 거예요|라고 보시면"),
    "중간 정리 (정리하면·한 줄·핵심은·한마디로)": (300, r"정리하면|정리하자면|한 줄|핵심은|요약하면|한마디로"),
    "같이 계산 (저랑·같이 보시)": (300, r"저랑|같이 (보|계산|살펴|정리)|함께 (보|계산|살펴)"),
    "기준 날짜 밝힘 (20NN년 … 기준)": (300, r"20\d\d ?년.{0,15}기준|기준으로|올해 기준|현재 기준"),
    "끝까지 보라는 약속": (300, r"끝까지"),
    "어르신 호칭 (어머님·아버님·어르신·부모님)": (300, r"어머님|아버님|어르신|부모님"),
}


def _sentences(snips, limit=300):
    buf, out, st = "", [], None
    for s in snips:
        if s["start"] > limit:
            break
        t = (s.get("text") or "").strip()
        if not t:
            continue
        if st is None:
            st = s["start"]
        buf = (buf + " " + t).strip()
        if re.search(r"[.?!…]$|(다|요|죠|까|니다)$", buf):
            out.append((st, buf))
            buf, st = "", None
    if buf:
        out.append((st, buf))
    return out


def style_rows(d):
    cases = {c["folder"]: c for c in d.cases}
    rows, skipped = [], 0
    for f in sorted(d.out.glob("W_*/transcript.json")):
        folder = f.parent.name
        c = cases.get(folder)
        try:
            j = json.load(open(f, encoding="utf-8"))
        except Exception as e:  # noqa: BLE001
            log("STYLE", logging.WARNING, unreadable=folder, error=e)
            skipped += 1
            continue
        sn = j.get("snippets") or []
        if not sn:
            skipped += 1
            continue
        dur = min(300, sn[-1]["start"] + sn[-1].get("duration", 0))
        if dur < 120:
            skipped += 1
            continue
        ss = _sentences(sn)
        texts = [t for _, t in ss]
        lens = [len(HAN.findall(t)) for t in texts if HAN.search(t)]
        if not texts or not lens:
            skipped += 1
            continue
        n = len(texts)
        r = dict(folder=folder, success=bool(c), theme=(c or {}).get("theme") or "", format=(c or {}).get("format") or "", dur=dur,
                 sylps=sum(lens) / dur, len_med=statistics.median(lens),
                 short=sum(1 for x in lens if x <= 12) / len(lens), long=sum(1 for x in lens if x >= 35) / len(lens),
                 formal=sum(1 for t in texts if END_FORMAL.search(t)) / n, polite=sum(1 for t in texts if END_POLITE.search(t)) / n,
                 q=sum(1 for t in texts if END_Q.search(t)) / n)
        for k, rx in TIMING.items():
            r[k] = next((st for st, t in ss if re.search(rx, t)), None)
        for k, (sec, rx) in DEVICES.items():
            r["dev:" + k] = bool(re.search(rx, " ".join(s["text"] for s in sn if s["start"] <= sec)))
        rows.append(r)
    log("STYLE", transcripts=len(rows), skipped=skipped)
    return rows


def cmd_style(d):
    rows = [r for r in style_rows(d) if r["success"]]
    pre = d.rules.get("STYLE_THEME_PREFIX") or ""
    groups = {"성공 사례 전체": rows}
    if pre:
        groups[f"주제 묶음 {pre}…"] = [r for r in rows if r["theme"].startswith(pre)]
    groups["정보·해설 형식"] = [r for r in rows if r["format"].startswith("정보·해설")]
    if pre:
        groups[f"{pre}… × 정보·해설"] = [r for r in rows if r["theme"].startswith(pre) and r["format"].startswith("정보·해설")]
    print(f"\n## 성공 사례 대본 — 음성인식 앞 5분, {len(rows)}개 (중앙값)\n")
    print("| 묶음 | 수 | 말 속도(음절/초) | 문장 길이 | 짧은 문장(≤12) | 긴 문장(≥35) | 합니다체 | 해요체 | 질문 |")
    print("|---|---|---|---|---|---|---|---|---|")
    for g, rs in groups.items():
        if not rs:
            continue
        med = lambda k: statistics.median(x[k] for x in rs)
        print(f"| {g} | {len(rs)} | {med('sylps'):.1f} | {med('len_med'):.0f} | {med('short'):.0%} | {med('long'):.0%} | {med('formal'):.0%} | {med('polite'):.0%} | {med('q'):.0%} |")
    print("\n### 시점 (앞 5분 안에 나온 영상 수, 시점 중앙값)\n")
    print("| 묶음 | " + " | ".join(TIMING) + " |")
    print("|---|" + "---|" * len(TIMING))
    for g, rs in groups.items():
        if not rs:
            continue
        cells = []
        for k in TIMING:
            ts = [x[k] for x in rs if x[k] is not None]
            cells.append(f"{len(ts)}/{len(rs)}" + (f", {statistics.median(ts):.0f}초" if ts else ""))
        print(f"| {g} | " + " | ".join(cells) + " |")
    print("\n### 전개 장치 (쓰는 영상 수)\n")
    print("| 장치 | " + " | ".join(groups) + " |")
    print("|---|" + "---|" * len(groups))
    for k in DEVICES:
        cells = []
        for rs in groups.values():
            n = sum(1 for r in rs if r["dev:" + k])
            cells.append(f"{n}/{len(rs)} ({n / len(rs):.0%})" if rs else "-")
        print(f"| {k} | " + " | ".join(cells) + " |")


# ----------------------------------------------------------------------------- 5. 댓글 피드백
FEEDBACK = {
    "칭찬: 현실적·공감": r"현실적|현실을|공감|와닿|와 닿|내 ?얘기|제 ?얘기|위로",
    "칭찬: 도움·실천": r"도움(이|되|돼|됐|많이)|유익|꿀팁|실천|바로 (해|하|신청|확인)|당장",
    "칭찬: 숫자·계산·구체적": r"숫자|계산|구체적|데이터|수치|시뮬|표로|정확히 (알|계산)",
    "칭찬: 정리·핵심": r"정리(가|를)? ?(잘|해 ?주)|핵심(만|을|이)|요점|깔끔",
    "칭찬: 쉽게 이해·설명": r"이해(가|하기)? ?(쉽|잘|쏙)|쉽게 (설명|알려|이해)|귀에 (쏙|잘)|명쾌|설명(을|이)? ?(잘|쉽|좋)|머리에 쏙",
    "칭찬: 목소리·말투": r"목소리(가|도)? ?(좋|편|따뜻|차분|멋)|말투(가)? ?(좋|편)|차분|듣기 ?(좋|편)|발음(이)? ?(좋|정확)",
    "불만: 틀림·부정확": r"틀린|틀렸|잘못 (된|알|설명)|오류|정정|사실과 달|사실이 아|확인 (좀|하고)",
    "불만: 길다·반복·지루": r"너무 ?길|길어서|길다|지루|반복|늘어지|핵심만|요점만|결론만|요약 ?좀|빨리 (말|본론)",
    "불만: 뻔함·일반론": r"뻔한|다 아는|원론|당연한 (얘기|소리|말)|누가 몰라",
    "불만: 광고·낚시·제목": r"광고(가|가 ?너무|많|티|충)|낚시|어그로|(제목|썸네일)(이|과|이랑)? ?(낚|과장|다르|달라)",
    "불만: AI 목소리 (이 영상 내레이션)": r"([Aa][Ii]|에이아이) ?(목소리|음성|내레이션|나레이션|더빙|성우)|기계음|기계 ?(목소리|같은 ?목소리)|로봇 ?(목소리|같)|합성 ?음성|TTS|tts|목소리가 ?(어색|부자연|기계)",
    "불만: 말 빠르기·소리": r"말이 ?(빠르|너무 빨)|너무 빨라|느려|소리가 ?(작|커)|배경 ?(음악|소리)",
    "불만: 60대 어르신·노인 취급": r"(어르신|노인)(이라|취급|소리|이라고)|노인 ?취급|늙은이 ?취급|60대(가|는|를)? ?(무슨|어르신|노인)",
}
FEEDBACK_EXCLUDE = {"불만: AI 목소리 (이 영상 내레이션)": r"AI ?(투자|주식|관련|산업|반도체|버블|시대|일자리|로봇주)|로봇 ?(주|산업|관련)"}


def cmd_feedback(d, top=4):
    import success_analysis as sa
    rows = d.comments()
    pre = d.rules.get("STYLE_THEME_PREFIX") or ""

    def hits_of(rs, k, rx):
        out = []
        for x in rs:
            if not re.search(rx, x["t"]):
                continue
            if k.startswith("불만") and re.search(sa.PRAISE_NEG, x["t"]):
                continue
            ex = FEEDBACK_EXCLUDE.get(k)
            if ex and re.search(ex, x["t"]):
                continue
            out.append(x)
        return out
    groups = {"성공 사례 전체": rows}
    if pre:
        groups[f"주제 묶음 {pre}…"] = [x for x in rows if x["theme"].startswith(pre)]
    print(f"\n## 댓글 피드백 — 성공 사례 {len(d.cases)}개, 댓글 {len(rows):,}개 (정규식 분류: 엉뚱한 댓글이 섞임 → 원문 확인)\n")
    print("| 갈래 | " + " | ".join(f"{g} (댓글·👍·영상)" for g in groups) + " |")
    print("|---|" + "---|" * len(groups))
    for k, rx in FEEDBACK.items():
        cells = []
        for rs in groups.values():
            h = hits_of(rs, k, rx)
            cells.append(f"{len(h)} · 👍{sum(x['likes'] for x in h):,} · {len({x['no'] for x in h})}")
        print(f"| {k} | " + " | ".join(cells) + " |")
    for k, rx in FEEDBACK.items():
        h = sorted(hits_of(rows, k, rx), key=lambda x: -x["likes"])
        seen, out = set(), []
        for x in h:
            if x["no"] in seen:
                continue
            seen.add(x["no"])
            out.append(x)
            if len(out) >= top:
                break
        print(f"\n### {k} — 좋아요 많은 원문 (영상마다 1개)")
        for x in out:
            print(f"- 👍{x['likes']} #{x['no']} {x['t'][:150]}")
    log("FEEDBACK", comments=len(rows), categories=len(FEEDBACK))


# ----------------------------------------------------------------------------- 6. 새 대본 측정
def script_sentences(path):
    """대본 문장 (파트 라벨 '-…', '[챕터…]', '[장면]' 카드 문구 제외). 한 줄에 두 문장이면 나눠 센다."""
    sents, in_card = [], False
    for raw in Path(path).read_text("utf-8-sig").splitlines():
        line = raw.strip()
        if not line:
            continue
        if (line.startswith("-") and not re.match(r"-\s*[\d.,]", line)) or line.startswith("[챕터"):
            in_card = False
            continue
        if line.startswith("[장면]"):
            in_card = True
            continue
        if in_card:
            continue
        sents += [x.strip() for x in re.split(r"(?<=[.?!])\s+", line) if x.strip()]
    return sents


def measure(path, rate_sps=5.1):
    import srt_tool
    sents = script_sentences(path)
    if not sents:
        raise SystemExit(f"[MEASURE] ❌ {path} 에 문장이 없음")
    lens = [len(HAN.findall(x)) for x in sents]          # 성공 사례 문장 길이와 같은 규칙(한글 글자)
    spk = [srt_tool.syllables(x) for x in sents]          # 읽는 음절(숫자·영문을 소리로)
    est = sum(srt_tool.duration(x) for x in sents)        # srt_tool 추정(문장 쉼 포함)
    t, timed = 0.0, []
    for x, n in zip(sents, spk):
        timed.append((t, x))
        t += n / rate_sps
    upto = lambda sec: " ".join(x for st, x in timed if st <= sec)
    r = dict(path=str(path), sent=len(sents), syl=sum(spk), minutes=sum(spk) / rate_sps / 60, srt_minutes=est / 60,
             len_med=statistics.median(lens), short=sum(1 for n in lens if n <= 12) / len(lens), long=sum(1 for n in lens if n >= 35) / len(lens),
             formal=sum(1 for x in sents if END_FORMAL.search(x)) / len(sents), polite=sum(1 for x in sents if END_POLITE.search(x)) / len(sents),
             q=sum(1 for x in sents if END_Q.search(x)) / len(sents),
             over50=[i + 1 for i, x in enumerate(sents) if len(x) > 50])
    r["first"] = {name: next((round(st) for st, x in timed if re.search(rx, x)), None)
                  for name, rx in (("결론 먼저", r"결론부터"), ("첫 질문", r"\?"), ("끝까지 약속", r"끝까지"), ("기준 날짜", r"20\d\d ?년"))}
    r["devices"] = {k: bool(re.search(rx, upto(sec))) for k, (sec, rx) in DEVICES.items()}
    r["devices_any_time"] = {k: bool(re.search(rx, " ".join(sents))) for k, (sec, rx) in DEVICES.items()}
    return r


def cmd_measure(paths, rate_sps):
    print(f"\n## 대본 측정 — 말 속도 {rate_sps}음절/초 가정 (성공 사례 중앙값), 문장 길이는 한글 글자 수\n")
    rs = [measure(p, rate_sps) for p in paths]
    print("| 대본 | 문장 | 읽는 음절 | 길이(분) | srt_tool 추정(분) | 문장 길이 | 짧은 | 긴 | 합니다체 | 해요체 | 질문 | 50자 넘는 문장 |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for r in rs:
        print(f"| {Path(r['path']).name} | {r['sent']} | {r['syl']:,} | {r['minutes']:.1f} | {r['srt_minutes']:.1f} | {r['len_med']:.0f} | {r['short']:.0%} | {r['long']:.0%} | "
              f"{r['formal']:.0%} | {r['polite']:.0%} | {r['q']:.0%} | {len(r['over50'])} |")
    for r in rs:
        print(f"\n### {Path(r['path']).name} — 처음 나오는 시점(초): " + ", ".join(f"{k} {v}" for k, v in r["first"].items()))
        print("| 장치 (성공 사례와 같은 시간 창) | 창 안 | 대본 어디든 |")
        print("|---|---|---|")
        for k in DEVICES:
            print(f"| {k} | {'O' if r['devices'][k] else '-'} | {'O' if r['devices_any_time'][k] else '-'} |")
        log("MEASURE", script=Path(r["path"]).name, sentences=r["sent"], syllables=r["syl"], minutes=f"{r['minutes']:.2f}",
            srt_minutes=f"{r['srt_minutes']:.2f}", formal=f"{r['formal']:.2f}", polite=f"{r['polite']:.2f}")
    return rs


# ----------------------------------------------------------------------------- 실행
def main(argv=None):
    ap = argparse.ArgumentParser(description="콘텐츠 연구 — 분석 결과로 주제·제목·대본 지시사항의 숫자를 다시 냄 (연구·교육용)")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("audience", "needs", "titles", "style", "feedback", "all"):
        p = sub.add_parser(name)
        p.add_argument("topic", help="주제 폴더 (예: economic)")
        if name == "all":
            p.add_argument("--out", help="결과 마크다운 파일 (없으면 화면)")
    p = sub.add_parser("measure")
    p.add_argument("script", help="대본 txt (파트 라벨 '-…' 또는 '[챕터]' 형식)")
    p.add_argument("--compare", action="append", default=[], help="같이 잴 대본 (여러 번 가능)")
    p.add_argument("--rate", type=float, default=5.1, help="말 속도 음절/초 (기본: 재테크 성공 사례 중앙값 5.1)")
    a = ap.parse_args(argv)
    logging.basicConfig(level=getattr(logging, a.log_level), format="%(message)s", stream=sys.stderr)
    t0 = time.time()
    log("START", version=VERSION, cmd=a.cmd)
    if a.cmd == "measure":
        cmd_measure(a.compare + [a.script], a.rate)
    else:
        d = Data(a.topic)
        run = {"audience": [cmd_audience], "needs": [cmd_needs], "titles": [cmd_titles], "style": [cmd_style], "feedback": [cmd_feedback],
               "all": [cmd_audience, cmd_needs, cmd_titles, cmd_style, cmd_feedback]}[a.cmd]
        out_f = None
        if getattr(a, "out", None):
            out_f = open(a.out, "w", encoding="utf-8")
            sys.stdout = out_f
            print(f"# 콘텐츠 연구 — {a.topic} (tools/content_research.py {VERSION}, 분석 결과 {d.a.get('generated')})\n")
        try:
            for fn in run:
                fn(d)
        finally:
            if out_f:
                sys.stdout = sys.__stdout__
                out_f.close()
                log("SAVE", out=a.out)
    log("DONE", seconds=f"{time.time() - t0:.1f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
