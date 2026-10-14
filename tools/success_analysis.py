#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-14 — 신규: 성공 사례 분석 — AI 가 지시사항을 만들 재료 (사용자 지시: "성공 사례 영상의 정보와 시청자들의
#          니즈(댓글을 통해 영상의 좋은점, 뭐를 더 알고 싶은지, 영상의 아쉬운점이 뭔지 등)를 분석해서 어떤 주제, 어떤 제목, 어떤 썸네일,
#          내용을 어떻게 구성해야하는지 등 조회수가 높게 나오고 구독자가 많이 모일 수 있는 영상을 만드는 거야 … 분석결과를 ai가 보고
#          지시사항을 만들도록 할거고 … 올바른 분석 결과까지만 내도록 수정해").
#          2026-10-14 결과(승인 88개)가 틀어졌던 까닭을 막음: ① 한 채널(경제해적단 45/88)이 숫자를 덮음 → 성공 사례는 채널당 2개,
#          비교 집단은 채널당 최근 5개 ② 성공 기준(180일·구독자 5만 이하·×3·1만·4분)을 승인 영상 전부가 아니라 기준을 넘는 영상에만
#          ③ 광고 의심(좋아요·댓글 거의 없음)·뺀 주제(부동산·코인·땅 매물) 제외 ④ '성공 vs 나머지' 비교 (탐색한 영상 전부 — 할당량 0)
#          ⑤ 대본이 없는 사례는 구성·도입부 근거에서 빼고 표시 ⑥ 댓글은 좋은 점·더 알고 싶은 것·아쉬운 점·경험·구독 기대로 나눔
#          + (사용자 지시: "수요 대비 영상 공급이 별로 없는지도 파악해야해 이외에도 내가 말한 목표를 달성하기 위한 모든 분석 방법을 찾아서 반영해")
#          ⑦ 수요와 공급: 주제 묶음별 수요/공급 지수(최근 90일 하루 조회수 몫 ÷ 영상 수 몫), 검색어별(결과 수 = 공급 추정, 상위 영상 하루 조회수,
#             큰 채널 비율 = 진입 장벽, 작은 채널 성공), YouTube 자동완성(사람들이 찾는 말) 중 최근 영상이 적은 말(+ [공급 확인] 검색 결과),
#             시청자 질문이 많은 주제 ⑧ 구독자: 빨리 크는 작은 채널(개설 24개월 안 — 월 구독자 증가·업로드 빈도·주로 다룬 주제·대표 영상,
#             받을 때마다 남긴 구독자 기록으로 최근 증가) ⑨ 참여율(좋아요·댓글 ÷ 조회수) 성공 vs 나머지 ⑩ 도입부 유형(대본이 있는 사례)
r"""
사용법 (저장소 최상위 또는 PC 실행 폴더 — 주별 분석 tools/weekly_analysis.py 가 끝날 때 저절로 부름):
  python tools/success_analysis.py economic
입력 (할당량 0, 인터넷 안 씀):
  <주제>/result/outliers/  사례 폴더 W_<영상ID>(웹 화면 승인)·01_…(성공 사례 수집)·P01_…(조회수 상위) — metadata.json·description.txt·
                           transcript.json·comments.csv·thumbnail.jpg
  <주제>/result/outliers/.cache/  탐색·검색에서 본 영상 정보·채널 구독자 수 (PC 에만) → 비교 집단
  <주제>/analysis_rules.toml (성공 기준·비교·제외·수요·성장) · keywords.toml (관련어) · tag_rules.toml (TAG_THEMES = 주제 묶음)
  .cache/search_*.json (검색어별 결과·결과 수) · autocomplete.json (자동완성) · supply_*.json ([공급 확인]) · channels.json (개설일·구독자 기록)
출력 (<주제>/result/outliers/ — GitHub 에도 올라감):
  analysis.md          AI 가 읽을 분석 결과 (숫자·원문만 — 해석·규칙 없음)
  analysis.json        같은 내용 (기계용)
  compare.csv          비교 집단 영상 목록 (성공 여부·주제 묶음 — 숫자를 다시 셀 수 있게)
  analysis_thumbs.jpg  성공 사례 썸네일 한 장에 (번호 = 1번 표의 #) · analysis_thumbs_others.jpg (자료를 받았지만 성공 기준 밖)
로그: [STAGE] [시각] key=value (START·CASES·POOL·SUCCESS·COMPARE·COMMENTS·THUMBS·WRITE·DONE)
※ 연구·교육용 분석 도구. 투자 권유가 아니다.
"""
import argparse
import csv
import io
import json
import logging
import math
import re
import statistics
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import outlier_research as orr                                   # noqa: E402  관련어 판정·라이브/외국·챕터·말 속도 (표준 라이브러리만)
from outlier_stats import TITLE_FEATURES                          # noqa: E402  제목 특징 (예전 분석과 같은 규칙)
from weekly_analysis import _published, _write_atomic, clean_description   # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
VERSION = "v1.0"
LOG = logging.getLogger("success")
CASE_DIR_RX = re.compile(r"^(W_|P?\d\d_)")
NON_VIDEO_CACHE = ("search_", "supply_", "uploads_", "channels.json", "autocomplete.json")   # 영상 정보가 아닌 캐시 파일
DEFAULT_RULES = {
    "success": {"MAX_AGE_DAYS": 180, "MAX_SUBS": 50000, "MIN_RATIO": 3.0, "MIN_VIEWS": 10000, "MIN_MINUTES": 4.0, "CASES_PER_CHANNEL": 2},
    "compare": {"MAX_AGE_DAYS": 365, "MAX_SUBS": 50000, "MIN_MINUTES": 4.0, "PER_CHANNEL": 5, "MIN_GROUP": 15, "NOTABLE_DIFF": 0.10},
    "demand": {"RECENT_DAYS": 90, "AUTOCOMPLETE_TOP": 30, "GAP_VERIFY_N": 10},
    "growth": {"NEW_CHANNEL_MONTHS": 24, "MIN_SUBS": 1000, "TOP": 25},
    "exclude": {"OFF_TOPIC": [], "OFF_TOPIC_THEMES": [], "AD_SUSPECT_MIN_VIEWS": 50000, "AD_SUSPECT_MAX_LIKE_RATE": 0.0025, "AD_SUSPECT_MAX_COMMENT_RATE": 0.00005},
}
# 제목 모양 (주제 낱말과 무관한 것 — 주제 낱말은 '제목 낱말' 표가 데이터로 셈)
TITLE_SHAPE = {
    "숫자가 들어감": lambda t: bool(re.search(r"\d", t)),
    "따옴표·괄호로 강조": lambda t: bool(re.search(r"['\"‘’“”「」『』\[\]【】《》]", t)),
    "구분 기호(ㅣ·｜·/)로 나눔": lambda t: bool(re.search(r"[|ㅣ｜/]", t)),
    "말줄임 …·...": lambda t: bool(re.search(r"…|\.\.\.", t)),
    "40자 이상": lambda t: len(t) >= 40,
    "25자 미만": lambda t: len(t) < 25,
}
# 시청자 니즈 (댓글 갈래 — 낱말 규칙이라 거칠다, 한 댓글이 여러 갈래에 들 수 있음). 채널 주인 댓글은 셈에서 뺌
NEED_CATS = {
    "좋은 점 (칭찬·도움·공감)": r"감사|고맙|도움|유익|좋은 ?(영상|정보|내용|말씀|강의|이야기)|최고|공감|잘 ?(들었|봤|보고|배웠|배우)|명쾌|쉽게|이해(가|가 ?잘|됐|돼)|"
                            r"정리(가|를|해)|와닿|울림|감동|힐링|목소리|꿀팁|레전드|대박|좋네|좋아요|좋습니다|좋았|훌륭",
    "더 알고 싶은 것 (질문·요청)": r"궁금|알려 ?주|알고 ?싶|가르쳐 ?주|다뤄 ?주|올려 ?주|해 ?주세요|해 ?주시면|해 ?주실|부탁|추천 ?(해 ?주|좀|부탁)|"
                              r"어떻게 (해야|하면|하나요|하죠|시작)|(나요|까요|가요|는지요|건가요|인가요|을까요|ㄹ까요|죠)\s*\?|\?\s*$",
    "아쉬운 점 (비판·불만·반박)": r"아쉽|아쉬운(?! ?소리)|별로|실망|광고|낚시|어그로|제목(이|과|이랑|만) |뻔한|다 아는|틀린|틀렸|잘못 (알|말|된)|아닌데|아니죠|아닙니다|"
                              r"글쎄|과장|거짓|가짜|기계음|[Aa][Ii] ?(목소리|음성|같|티)|너무 길|지루|결론(이|만|부터)|핵심만|억지|동의 ?(안|못)|헛소리|말도 안|선동",
    "경험 공유 (내 이야기)": r"저도|제가|나도|내가|저희|우리 ?(집|남편|아내|부모|엄마|아빠)|해봤|했었|겪|경험|년째|년 ?차",
    "구독·다음 기대": r"구독(했|하고|합니다|누르|눌렀|박|완료|갑니다|해요|할게|각)|알림 ?설정|팬(이|입니다)|기다려|기대(됩니다|돼요|할게|합니다)|정주행|"
                   r"챙겨 ?(봐|볼)|매일 ?(봐|듣)",
}
PARTICLES = sorted("이 가 은 는 을 를 의 에 에서 으로 로 와 과 도 만 들 들이 들의 들은 들을 이다 입니다 하는 하기 한 할 된 되는".split(), key=len, reverse=True)
STOP = set("이 그 저 것 수 등 및 더 왜 다 또 안 못 잘 꼭 진짜 정말 지금 이제 그냥 바로 모든 모두 절대 무조건 반드시 영상 채널 구독 라이브 오늘 우리 "
           "있는 없는 하는 되는 하면 해서 합니다 입니다 the and for with".split())
# 도입부(대본 첫 20초의 첫 문장) 유형 — 낱말 규칙
HOOK_TYPES = {
    "질문으로 시작": r"\?|까요|나요|인가요|일까|ㄹ까",
    "숫자로 시작": r"\d",
    "내 이야기·사연": r"저는|제가|저희|어느 ?날|살 ?때|년 ?전",
    "경고·단정": r"절대|하지 ?마|반드시|무조건|후회|망하|위험",
    "시청자 부르기": r"여러분|당신|구독자",
}
LEN_BUCKETS = [(4, 8), (8, 15), (15, 25), (25, 40), (40, 10 ** 6)]
SUBS_BUCKETS = [(0, 1000), (1000, 5000), (5000, 20000), (20000, 50001)]


def log(stage, level=logging.INFO, **kv):
    LOG.log(level, "[%s] [%s] %s", stage, datetime.now().isoformat(timespec="seconds"),
            " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) and ' ' in v else v}" for k, v in kv.items()))


# ---------------------------------------------------------------- 규칙·설정
def _toml(p):
    try:
        return orr.tomllib.loads(Path(p).read_text("utf-8")) if Path(p).is_file() else {}
    except (OSError, ValueError) as e:
        log("START", logging.WARNING, file=str(p), note="설정 파일 읽기 실패 — 기본값", error=str(e)[:120])
        return {}


def load_rules(root, topic):
    d = _toml(root / topic / "analysis_rules.toml")
    rules = {k: dict(v) for k, v in DEFAULT_RULES.items()}
    for sec in rules:
        for k, v in (d.get(sec) or {}).items():
            if k in rules[sec]:
                rules[sec][k] = v
    try:
        m = re.search(r"VERSION:\s*(v[\d.]+)", (root / topic / "analysis_rules.toml").read_text("utf-8"))
    except OSError:
        m = None
    rules["version"] = m.group(1) if m else "-"
    rules["file"] = f"{topic}/analysis_rules.toml" if (root / topic / "analysis_rules.toml").is_file() else "(기본값)"
    rules["keywords"] = orr.read_keyword_list(root / topic / "keywords.txt") or []
    return rules


def load_rel(root, topic):
    """관련어 (keywords.toml — 분석기·성공 사례 수집과 같은 파일)."""
    src = {}
    for sec_or_flat in (_toml(root / topic / "keywords.toml"),):
        for k, v in sec_or_flat.items():
            src.update(v if isinstance(v, dict) and k != "KEYWORD_GROUPS" else {k: v})
    return {"strong": [str(t) for t in src.get("RELEVANCE_TERMS") or [] if str(t).strip()],
            "weak": [str(t) for t in src.get("RELEVANCE_WEAK_TERMS") or [] if str(t).strip()],
            "exclude": [str(t) for t in src.get("RELEVANCE_EXCLUDE") or [] if str(t)]}


def load_themes(root, topic):
    d = _toml(root / topic / "tag_rules.toml")
    return {str(k): [str(x) for x in v] for k, v in (d.get("TAG_THEMES") or {}).items()}


def theme_of(title, tags, themes):
    """주제 묶음 하나: 제목에서 맞는 글자가 가장 긴 묶음 (같으면 위쪽) — 제목에 없으면 태그로, 그래도 없으면 '기타'."""
    for text in (str(title or ""), " ".join(map(str, tags or []))):
        low, best, best_len = text.lower(), None, 0
        for name, words in themes.items():
            n = max((len(w) for w in words if w.lower() in low), default=0)
            if n > best_len:
                best, best_len = name, n
        if best:
            return best
    return "기타"


# ---------------------------------------------------------------- 자료 읽기
def _num(x, default=0):
    try:
        return int(x)
    except (TypeError, ValueError):
        return default


def _age_days(published, now):
    return (now - published).total_seconds() / 86400 if published else None


def _base(info, subs, now):
    """영상 정보 → 공통 줄 (배수·나이·길이)."""
    pub = _published(info)
    views = _num(info.get("views", info.get("view_count")))
    age = _age_days(pub, now)
    minutes = info.get("minutes")
    if minutes is None and info.get("duration"):
        minutes = round(float(info["duration"]) / 60, 1)
    return {"id": info.get("id"), "title": str(info.get("title") or ""), "channel": str(info.get("channel") or ""),
            "channel_id": info.get("channel_id") or "", "subs": subs, "views": views,
            "likes": _num(info.get("likes", info.get("like_count"))), "comments_total": _num(info.get("comments_reported", info.get("comment_count"))),
            "published": pub, "age_days": round(age, 1) if age is not None else None, "minutes": float(minutes or 0),
            "ratio": round(views / max(subs, 100), 2) if subs is not None else None,
            "vpd": round(views / max(age or 1, 1), 1), "tags": info.get("tags") or [], "live": info.get("live"), "was_live": info.get("was_live"),
            "audio_lang": info.get("audio_lang") or "", "lang": info.get("lang") or ""}


def load_cache(out):
    """탐색·검색에서 본 영상 정보(.cache/<영상ID>.json)와 채널 구독자 수(.cache/channels.json)."""
    cache = Path(out) / ".cache"
    infos, subs = {}, {}
    load_cache.channels = {}
    if cache.is_dir():
        for f in cache.glob("*.json"):
            if f.name.startswith(NON_VIDEO_CACHE):
                continue
            try:
                i = json.loads(f.read_text("utf-8"))
            except (OSError, ValueError):
                continue
            if isinstance(i, dict) and i.get("id") and "title" in i:
                infos[i["id"]] = i
        try:
            ch = {k: v for k, v in json.loads((cache / "channels.json").read_text("utf-8")).items() if isinstance(v, dict)}
        except (OSError, ValueError):
            ch = {}
        subs = {k: v.get("subs") for k, v in ch.items()}
        load_cache.channels = ch                 # 개설일·영상 수·구독자 기록 (outlier_research v2.1)
    return infos, subs


def load_market_caches(out):
    """검색 캐시(검색어별 결과·결과 수) · 자동완성 · [공급 확인] 결과."""
    cache = Path(out) / ".cache"
    searches, supplies, ac = [], {}, {}
    if cache.is_dir():
        for f in cache.glob("search_*.json"):
            try:
                d = json.loads(f.read_text("utf-8"))
                if d.get("q"):
                    searches.append(d)
            except (OSError, ValueError):
                continue
        for f in cache.glob("supply_*.json"):
            try:
                d = json.loads(f.read_text("utf-8"))
                if d.get("phrase"):
                    supplies[d["phrase"]] = d
            except (OSError, ValueError):
                continue
        try:
            ac = {k: v.get("s") or [] for k, v in json.loads((cache / "autocomplete.json").read_text("utf-8")).items() if isinstance(v, dict)}
        except (OSError, ValueError):
            ac = {}
    return searches, supplies, ac


def load_cases(out, cache_infos, cache_subs, now):
    """사례 폴더 (W_·01_·P01_) → 사례 목록. 같은 영상이 여러 폴더에 있으면 대본이 있는 쪽, 그다음 W_."""
    out = Path(out)
    by_id = {}
    for d in sorted(out.iterdir()) if out.is_dir() else []:
        if not (d.is_dir() and CASE_DIR_RX.match(d.name) and (d / "metadata.json").is_file()):
            continue
        try:
            meta = json.loads((d / "metadata.json").read_text("utf-8"))
        except (OSError, ValueError):
            continue
        vid = meta.get("id")
        if not vid:
            continue
        info = dict(meta)
        ci = cache_infos.get(vid) or {}
        for k_meta, k_cache in (("views", "view_count"), ("likes", "like_count"), ("comments_reported", "comment_count")):
            info[k_meta] = max(_num(meta.get(k_meta)), _num(ci.get(k_cache)))           # 숫자는 늘기만 함 — 더 새 값
        for k in ("live", "was_live", "audio_lang", "lang", "description"):
            if k in ci and k not in info:
                info[k] = ci[k]
        subs = cache_subs.get(meta.get("channel_id")) if cache_subs.get(meta.get("channel_id")) is not None else meta.get("subs")
        c = _base(info, subs, now)
        snips, lang = [], ""
        if (d / "transcript.json").is_file():
            try:
                tj = json.loads((d / "transcript.json").read_text("utf-8"))
                snips, lang = tj.get("snippets") or [], str(tj.get("lang") or "")
                snips = [{"text": str(x.get("text") or ""), "start": float(x.get("start") or 0), "duration": float(x.get("duration") or 0)}
                         for x in snips if isinstance(x, dict)]
            except (OSError, ValueError):
                snips = []
        try:
            desc = (d / "description.txt").read_text("utf-8") if (d / "description.txt").is_file() else str(ci.get("description") or "")
        except OSError:
            desc = ""
        cms = []
        if (d / "comments.csv").is_file():
            with open(d / "comments.csv", encoding="utf-8-sig", newline="") as f:
                for r in csv.DictReader(f):
                    cms.append({"text": str(r.get("text") or ""), "likes": _num(r.get("likes")),
                                "reply": str(r.get("is_reply")) in ("1", "True", "true"),
                                "creator": str(r.get("creator")) in ("1", "True", "true")})
        thumb = d / "thumbnail.jpg"
        c.update(folder=d.name, kind="웹 승인" if d.name.startswith("W_") else ("조회수 상위" if d.name.startswith("P") else "성공 사례 수집"),
                 desc=desc, desc_text=clean_description(desc), chapters=meta.get("chapters") or orr.chapters_from(desc),
                 snips=snips, src=("음성인식" if "음성인식" in lang else "자막") if snips else ("설명" if clean_description(desc) else "없음"),
                 speech=orr.speech_stats(snips) if snips else {}, comments=cms,
                 comments_complete=bool(meta.get("comments_complete")), comments_fetched=len(cms),
                 thumb=(d.name + "/thumbnail.jpg") if thumb.is_file() and thumb.stat().st_size > 0 else None,
                 description=desc)
        old = by_id.get(vid)
        if old is None or (not old["snips"] and (c["snips"] or (c["folder"].startswith("W_") and not old["folder"].startswith("W_")))):
            by_id[vid] = c
    return list(by_id.values())


# ---------------------------------------------------------------- 판정
def flags(x, rules, rel):
    """뺄 까닭 → '' 이면 쓸 수 있음: 라이브·외국 / 주제 밖(관련어 없음) / 뺀 주제(부동산·코인 …) / 광고 의심."""
    ex = rules["exclude"]
    why = orr.exclusion_reason({"title": x["title"], "live": x.get("live"), "was_live": x.get("was_live"),
                                "audio_lang": x.get("audio_lang"), "lang": x.get("lang")})
    if why:
        return why
    hit = next((w for w in ex["OFF_TOPIC"] if w and w in x["title"]), None)
    if hit:
        return f"뺀 주제({hit})"
    if x.get("theme") in ex["OFF_TOPIC_THEMES"]:
        return f"뺀 주제({x['theme']})"
    if not orr.relevant({"title": x["title"], "tags": x.get("tags"), "description": x.get("description") or x.get("desc") or ""}, rel):
        return "주제 밖(관련어 없음)"
    v = x["views"]
    if v >= ex["AD_SUSPECT_MIN_VIEWS"] and x["likes"] / max(v, 1) < ex["AD_SUSPECT_MAX_LIKE_RATE"] \
            and x["comments_total"] / max(v, 1) < ex["AD_SUSPECT_MAX_COMMENT_RATE"]:
        return "광고 의심(좋아요·댓글 거의 없음)"
    return ""


def is_success(x, S, with_age=True):
    return (x["subs"] is not None and x["subs"] <= S["MAX_SUBS"] and x["views"] >= S["MIN_VIEWS"] and (x["ratio"] or 0) >= S["MIN_RATIO"]
            and x["minutes"] >= S["MIN_MINUTES"] and (not with_age or (x["age_days"] is not None and x["age_days"] <= S["MAX_AGE_DAYS"])))


def stem(w):
    for p in PARTICLES:
        if w.endswith(p) and len(w) - len(p) >= 2:
            return w[: -len(p)]
    return w


def title_words(title):
    ws = re.findall(r"[가-힣A-Za-z0-9&]{2,}", str(title or ""))
    return {s for s in (stem(w) for w in ws) if s.lower() not in STOP and not s.isdigit() and len(s) >= 2}


def _rate(rows):
    n, s = len(rows), sum(1 for r in rows if r["success"])
    return {"n": n, "success": s, "rate": round(s / n, 3) if n else None}


def _median(xs):
    xs = [x for x in xs if isinstance(x, (int, float)) and not (isinstance(x, float) and math.isnan(x))]
    return round(statistics.median(xs), 2) if xs else None


def compare_by(rows, pred, C):
    yes = [r for r in rows if pred(r)]
    no = [r for r in rows if not pred(r)]
    a, b = _rate(yes), _rate(no)
    diff = round(a["rate"] - b["rate"], 3) if a["rate"] is not None and b["rate"] is not None else None
    small = a["n"] < C["MIN_GROUP"] or b["n"] < C["MIN_GROUP"]
    return {"with": a, "without": b, "diff": diff, "small_sample": small,
            "notable": bool(diff is not None and not small and abs(diff) >= C["NOTABLE_DIFF"])}


def classify_comment(text):
    return [name for name, rx in NEED_CATS.items() if re.search(rx, text)]


# ---------------------------------------------------------------- 분석
def analyze(topic, name, cases, cache_infos, cache_subs, rules, rel, themes, now, market_caches=((), {}, {})):
    S, C = rules["success"], rules["compare"]
    for c in cases:
        c["theme"] = theme_of(c["title"], c["tags"], themes)
        c["exclude"] = flags(c, rules, rel)
    # 1) 성공 사례 — 자료를 받은 영상 중 기준을 넘고 뺄 까닭이 없는 것, 채널당 CASES_PER_CHANNEL 개 (배수 큰 순)
    passed = [c for c in cases if is_success(c, S)]
    excluded = [c for c in passed if c["exclude"]]
    eligible = sorted((c for c in passed if not c["exclude"]), key=lambda c: -(c["ratio"] or 0))
    per_ch, success, cut = Counter(), [], []
    for c in eligible:
        key = c["channel_id"] or c["channel"]
        if per_ch[key] >= S["CASES_PER_CHANNEL"]:
            cut.append(c)
            continue
        per_ch[key] += 1
        success.append(c)
    for i, c in enumerate(success, 1):
        c["no"] = i
    log("SUCCESS", cases=len(cases), passed=len(passed), excluded=len(excluded), channel_cut=len(cut), success=len(success),
        rule=f"{S['MAX_AGE_DAYS']}일·구독자≤{S['MAX_SUBS']}·×{S['MIN_RATIO']}·{S['MIN_VIEWS']}회·{S['MIN_MINUTES']}분·채널당{S['CASES_PER_CHANNEL']}")
    # 2) 비교 집단 — 탐색에서 본 영상 전부(.cache) + 사례, 같은 조건, 채널당 최근 PER_CHANNEL 개
    pool = {}
    for vid, i in cache_infos.items():
        x = _base({**i, "views": i.get("view_count"), "likes": i.get("like_count"), "comments_reported": i.get("comment_count")},
                  cache_subs.get(i.get("channel_id")), now)
        x["description"] = i.get("description") or ""
        pool[vid] = x
    case_ids = {c["id"] for c in cases}
    for c in cases:
        pool[c["id"]] = {**pool.get(c["id"], {}), **{k: c[k] for k in ("id", "title", "channel", "channel_id", "subs", "views", "likes",
                         "comments_total", "published", "age_days", "minutes", "ratio", "vpd", "tags", "live", "was_live",
                         "audio_lang", "lang")}, "description": c["desc"]}
    rows_all = list(pool.values())
    for x in rows_all:
        x["theme"] = theme_of(x["title"], x["tags"], themes)
        x["exclude"] = flags(x, rules, rel)
        x["success"] = is_success(x, S, with_age=False)
        x["has_case"] = x["id"] in case_ids
        x["in_scope"] = (not x["exclude"] and x["subs"] is not None and x["subs"] <= C["MAX_SUBS"] and x["minutes"] >= C["MIN_MINUTES"]
                         and x["age_days"] is not None and x["age_days"] <= C["MAX_AGE_DAYS"])
    by_ch = defaultdict(list)
    for x in rows_all:
        if x["in_scope"]:
            by_ch[x["channel_id"] or x["channel"]].append(x)
    group, ch_cut = [], 0
    for lst in by_ch.values():
        lst.sort(key=lambda x: x["published"] or datetime.min.replace(tzinfo=timezone.utc), reverse=True)
        group += lst[:C["PER_CHANNEL"]]
        ch_cut += max(0, len(lst) - C["PER_CHANNEL"])
    for x in rows_all:
        x["in_compare"] = False
    for x in group:
        x["in_compare"] = True
    base = _rate(group)
    log("COMPARE", pool=len(rows_all), in_scope=sum(1 for x in rows_all if x["in_scope"]), group=len(group), channel_cut=ch_cut,
        success=base["success"], rate=base["rate"])
    # 자료를 받지 않은 성공 후보 (승인하면 분석에 들어감)
    missing = sorted((x for x in rows_all if not x["has_case"] and not x["exclude"] and is_success(x, S)), key=lambda x: -(x["ratio"] or 0))
    # 3) 주제 묶음
    theme_rows = []
    for th in list(themes) + ["기타"]:
        g = [x for x in group if x["theme"] == th]
        if not g:
            continue
        r = _rate(g)
        theme_rows.append({"theme": th, **r, "ratio_median": _median([x["ratio"] for x in g if x["ratio"] is not None]),
                           "views_median": _median([x["views"] for x in g]), "small_sample": r["n"] < C["MIN_GROUP"],
                           "success_cases": [c["no"] for c in success if c["theme"] == th]})
    theme_rows.sort(key=lambda r: (r["small_sample"], -(r["rate"] or 0)))
    # 4) 제목
    feats = {**{k: (lambda rx: (lambda t: bool(re.search(rx, t))))(rx) for k, rx in TITLE_FEATURES.items()}, **TITLE_SHAPE}
    title_rows = []
    for k, fn in feats.items():
        cmp_ = compare_by(group, lambda x, fn=fn: fn(x["title"]), C)
        share = round(sum(1 for c in success if fn(c["title"])) / len(success), 3) if success else None
        if cmp_["with"]["n"] or share:
            title_rows.append({"feature": k, **cmp_, "success_case_share": share})
    title_rows.sort(key=lambda r: (not r["notable"], -(abs(r["diff"]) if r["diff"] is not None else 0)))
    df = Counter()
    for x in group:
        x["_words"] = title_words(x["title"])
        df.update(x["_words"])
    min_df = max(8, math.ceil(len(group) * 0.03))
    word_rows = []
    for w, n in df.items():
        if n < min_df:
            continue
        cmp_ = compare_by(group, lambda x, w=w: w in x["_words"], C)
        word_rows.append({"word": w, **cmp_})
    word_rows.sort(key=lambda r: -(r["diff"] or 0))
    len_rows = []
    for lo, hi in ((0, 25), (25, 35), (35, 45), (45, 10 ** 6)):
        g = [x for x in group if lo <= len(x["title"]) < hi]
        len_rows.append({"label": f"{lo}~{hi - 1}자" if hi < 10 ** 6 else f"{lo}자 이상", **_rate(g)})
    # 5) 길이·채널 크기
    minutes_rows = []
    for lo, hi in LEN_BUCKETS:
        g = [x for x in group if lo <= x["minutes"] < hi]
        minutes_rows.append({"label": f"{lo}~{hi}분" if hi < 10 ** 6 else f"{lo}분 이상", **_rate(g),
                             "success_cases": sum(1 for c in success if lo <= c["minutes"] < hi)})
    subs_rows = []
    for lo, hi in SUBS_BUCKETS:
        g = [x for x in group if x["subs"] is not None and lo <= x["subs"] < hi]
        subs_rows.append({"label": f"{lo:,}~{hi - 1:,}명", **_rate(g)})
    # 6) 내용 구성 (성공 사례)
    with_tr = [c for c in success if c["snips"]]
    structure = {
        "minutes_median_success": _median([c["minutes"] for c in success]),
        "minutes_median_compare_others": _median([x["minutes"] for x in group if not x["success"]]),
        "chapters_share": round(sum(1 for c in success if c["chapters"]) / len(success), 3) if success else None,
        "chapters_count_median": _median([len(c["chapters"]) for c in success if c["chapters"]]),
        "transcripts": len(with_tr), "text_sources": dict(Counter(c["src"] for c in success)),
        "syl_per_sec_median": _median([c["speech"].get("syl_per_sec") for c in with_tr]),
        "first60_syl_median": _median([c["speech"].get("first60_syl") for c in with_tr]),
    }
    # 7) 시청자 니즈 (성공 사례 댓글 — 채널 주인 댓글 뺌)
    cat_count, cat_likes, quotes = Counter(), Counter(), defaultdict(list)
    n_viewer = 0
    for c in success:
        c["needs"] = Counter()
        c["need_quotes"] = defaultdict(list)
        for m in c["comments"]:
            if m["creator"] or not m["text"].strip():
                continue
            n_viewer += 1
            for cat in classify_comment(m["text"]):
                cat_count[cat] += 1
                cat_likes[cat] += m["likes"]
                c["needs"][cat] += 1
                q = {"no": c["no"], "likes": m["likes"], "reply": m["reply"], "text": re.sub(r"\s+", " ", m["text"]).strip()[:200]}
                quotes[cat].append(q)
                c["need_quotes"][cat].append(q)
    needs = {"viewer_comments": n_viewer,
             "categories": [{"name": k, "count": cat_count[k], "share": round(cat_count[k] / n_viewer, 3) if n_viewer else None,
                             "likes": cat_likes[k]} for k in NEED_CATS],
             "top": {k: sorted((q for q in quotes.get(k, []) if not q["reply"]), key=lambda q: -q["likes"])[:8] for k in NEED_CATS},
             "questions": sorted((q for q in quotes.get("더 알고 싶은 것 (질문·요청)", []) if not q["reply"]), key=lambda q: -q["likes"])[:25],
             "complaints": sorted(quotes.get("아쉬운 점 (비판·불만·반박)", []), key=lambda q: -q["likes"])[:15]}
    log("COMMENTS", success_cases=len(success), viewer_comments=n_viewer,
        cats=",".join(f"{k.split(' ')[0]}:{cat_count[k]}" for k in NEED_CATS))
    # 8) 수요와 공급 · 9) 구독자(채널 성장) · 10) 참여율·도입부
    market = demand_supply(rows_all, cases, group, theme_rows, themes, rules, now, market_caches)
    growth = channel_growth(rows_all, rules, now)
    engagement = {k: {"like_rate": _median([x["likes"] / x["views"] for x in g if x["views"]]),
                      "comment_rate": _median([x["comments_total"] / x["views"] for x in g if x["views"]]), "n": len(g)}
                  for k, g in (("success", [x for x in group if x["success"]]), ("others", [x for x in group if not x["success"]]))}
    hooks = Counter()
    for c in with_tr:
        first = re.split(r"(?<=[.?!])\s|\n", (c["speech"].get("hook20") or "").strip())[0][:120]
        c["hook_first"] = first
        c["hook_types"] = [k for k, rx in HOOK_TYPES.items() if re.search(rx, first)]
        hooks.update(c["hook_types"] or ["그 밖"])
    structure["hook_types"] = dict(hooks)
    # 0) 자료와 한계
    fetched = sum(c["comments_fetched"] for c in success)
    reported = sum(c["comments_total"] for c in success)
    src_all = Counter(c["src"] for c in success)
    limits = []
    no_script = [c["no"] for c in success if c["src"] not in ("자막", "음성인식")]
    if no_script:
        limits.append(f"대본(자막·음성인식)이 없는 성공 사례 {len(no_script)}개 (#{', #'.join(map(str, no_script[:30]))}{' …' if len(no_script) > 30 else ''}) — "
                      f"설명란·챕터만 있음. 도입부·구성·말 속도는 대본이 있는 {len(with_tr)}개로만 셌다 (음성인식이 끝나면 다시 셈)")
    incomplete = [c["no"] for c in success if not c["comments_complete"]]
    if incomplete:
        limits.append(f"댓글을 다 받지 못한 성공 사례 {len(incomplete)}개 (받은 {fetched:,} / 달린 {reported:,}개 — 할당량이 끝나면 다음에 이어 받음)")
    if not group:
        limits.append("비교 집단 없음 — 탐색 캐시(.cache)가 없음 (PC 에서 탐색한 뒤 다시). 주제·제목·길이의 '성공 비율'은 셀 수 없음")
    else:
        limits.append(f"비교 집단 {len(group)}개는 검색(조회수 순)·추가한 채널에서 나와 성공 비율({base['rate']:.0%})이 실제보다 높다 — "
                      "같은 집단 안의 '있음/없음' 차이로만 보라")
    if len(success) < 15:
        limits.append(f"성공 사례가 {len(success)}개뿐 — 성공 사례 안의 비율은 흔들림이 크다 (웹 화면에서 '자료 없는 성공 후보'를 승인하면 늘어남)")
    limits += market["limits"] + growth["limits"]
    limits += ["'구독자가 많이 모이는가'는 YouTube API 로 영상별 구독 증가를 볼 수 없다 — 대신 채널 성장(7번: 개설 뒤 월 구독자·받을 때마다 남긴 기록), "
               "'구독·다음 기대' 댓글, 배수(조회수÷구독자)로 본다",
               "댓글 갈래·제목 특징은 낱말 규칙이라 거칠다 (물음표 반문도 '질문', 한 댓글이 여러 갈래). 원문 인용을 함께 보라",
               "'눈에 띔'은 차이가 크고 표본이 충분하다는 표시일 뿐 원인이 아니다"]
    data = {"tool": f"success_analysis.py {VERSION}", "topic": topic, "name": name, "generated": now.isoformat(timespec="seconds"),
            "rules": {k: v for k, v in rules.items()},
            "sources": {"case_folders": len(cases), "by_kind": dict(Counter(c["kind"] for c in cases)), "pool": len(rows_all),
                        "compare_group": len(group), "compare_success": base["success"], "compare_rate": base["rate"],
                        "compare_channel_cut": ch_cut, "success_passed": len(passed), "success_excluded": [
                            {"id": c["id"], "title": c["title"], "why": c["exclude"]} for c in excluded],
                        "success_channel_cut": [{"id": c["id"], "title": c["title"], "channel": c["channel"]} for c in cut],
                        "success_text_sources": dict(src_all), "success_comments_fetched": fetched, "success_comments_reported": reported,
                        "success_thumbnails": sum(1 for c in success if c["thumb"])},
            "limits": limits,
            "success_cases": [case_view(c) for c in success],
            "missing_success": [{"id": x["id"], "title": x["title"], "channel": x["channel"], "subs": x["subs"], "views": x["views"],
                                 "ratio": x["ratio"], "minutes": x["minutes"], "published": x["published"].date().isoformat() if x["published"] else "",
                                 "theme": x["theme"]} for x in missing[:40]],
            "missing_success_total": len(missing),
            "themes": theme_rows, "title_features": title_rows, "title_words_up": [r for r in word_rows if (r["diff"] or 0) > 0][:15],
            "title_words_down": [r for r in reversed(word_rows) if (r["diff"] or 0) < 0][:10], "title_length": len_rows,
            "minutes": minutes_rows, "subs": subs_rows, "structure": structure, "needs": needs,
            "market": {k: v for k, v in market.items() if k != "limits"}, "growth": {k: v for k, v in growth.items() if k != "limits"},
            "engagement": engagement, "gap_candidates": market["gap_candidates"]}
    return data, success, group, rows_all, cases


def demand_supply(rows_all, cases, group, theme_rows, themes, rules, now, market_caches):
    """수요와 공급 (v1.0): 시장 = 최근 RECENT_DAYS 일·4분 이상·주제 관련·뺀 것 아님 (채널 크기 상관없음 — 공급은 시장 전체).
    수요 = 하루 조회수, 공급 = 영상 수. 지수 = 수요 몫 ÷ 공급 몫 (1 보다 크면 영상 하나가 평균보다 많이 봄 = 공급이 모자라 보임)."""
    D, C, ex = rules["demand"], rules["compare"], rules["exclude"]
    searches, supplies, ac = market_caches

    def norm(t):
        return re.sub(r"\s+", "", str(t)).lower()
    by_id = {x["id"]: x for x in rows_all}
    market = [x for x in rows_all if not x["exclude"] and x["minutes"] >= C["MIN_MINUTES"] and x["age_days"] is not None
              and x["age_days"] <= D["RECENT_DAYS"]]
    tot_v, tot_n = sum(x["vpd"] for x in market) or 1, len(market) or 1
    for x in market:
        x["_words"] = x.get("_words") or title_words(x["title"])
    # 시청자 질문 → 주제 묶음 (사례 전부의 시청자 댓글 중 '더 알고 싶은 것')
    qcat = "더 알고 싶은 것 (질문·요청)"
    q_by_theme, q_quotes = Counter(), defaultdict(list)
    for c in cases:
        for m in c["comments"]:
            if m["creator"] or m["reply"] or not re.search(NEED_CATS[qcat], m["text"]):
                continue
            th = theme_of(m["text"], [], themes)
            if th == "기타" or th in ex["OFF_TOPIC_THEMES"]:
                continue
            q_by_theme[th] += 1
            q_quotes[th].append({"likes": m["likes"], "text": re.sub(r"\s+", " ", m["text"]).strip()[:160], "video": c["title"][:40]})
    rate_by_theme = {r["theme"]: r for r in theme_rows}
    th_rows = []
    for th in list(themes) + ["기타"]:
        g = [x for x in market if x["theme"] == th]
        if th in ex["OFF_TOPIC_THEMES"] or (not g and not q_by_theme.get(th)):
            continue
        vs = sum(x["vpd"] for x in g)
        ds, ss = vs / tot_v, len(g) / tot_n
        r = rate_by_theme.get(th) or {}
        th_rows.append({"theme": th, "videos": len(g), "channels": len({x["channel_id"] for x in g}), "demand_share": round(ds, 3),
                        "supply_share": round(ss, 3), "index": round(ds / ss, 2) if ss else None,
                        "vpd_median": _median([x["vpd"] for x in g]), "small_success_rate": r.get("rate"), "small_n": r.get("n"),
                        "questions": q_by_theme.get(th, 0), "small_sample": len(g) < C["MIN_GROUP"],
                        "top_questions": sorted(q_quotes.get(th, []), key=lambda q: -q["likes"])[:3]})
    th_rows.sort(key=lambda r: (r["small_sample"], -(r["index"] or 0)))
    # 검색어별 (검색 캐시 — 검색어·기간마다, 길이 묶음은 합침)
    kw = defaultdict(lambda: {"ids": [], "total": 0, "total_known": True, "fetched": "", "days": None})
    for d in searches:
        k = (d["q"], d.get("fallback_days"))
        e = kw[k]
        e["ids"] += d.get("ids") or []
        e["days"] = d.get("fallback_days")
        e["fetched"] = max(e["fetched"], str(d.get("fetched") or ""))
        if d.get("total") is None:
            e["total_known"] = False
        else:
            e["total"] += int(d["total"])
    kw_rows = []
    current = {norm(k) for k in market_caches_current(rules)}
    for (q, days), e in kw.items():
        xs = [by_id[i] for i in dict.fromkeys(e["ids"]) if i in by_id]
        if not xs or any(w and w in q for w in ex["OFF_TOPIC"]):
            continue
        ok = [x for x in xs if not x["exclude"]]
        vsum = sum(x["vpd"] for x in ok)
        small_ok = [x for x in ok if x["subs"] is not None and x["subs"] <= C["MAX_SUBS"] and x["minutes"] >= C["MIN_MINUTES"]]
        total = e["total"] if e["total_known"] else None
        kw_rows.append({"q": q, "days": days, "found": len(xs), "recent30": sum(1 for x in ok if (x["age_days"] or 999) <= 30),
                        "total": total, "views_median": _median([x["views"] for x in ok]), "vpd_median": _median([x["vpd"] for x in ok]),
                        "vpd_per_video": round(vsum / total, 1) if total else None,
                        "big_share": round(sum(1 for x in ok if x["subs"] is None or x["subs"] > C["MAX_SUBS"]) / len(ok), 3) if ok else None,
                        "small_n": len(small_ok), "small_success": sum(1 for x in small_ok if x["success"]),
                        "small_hit_share": round(sum(1 for x in small_ok if x["success"]) / len(ok), 3) if ok else None,
                        "current": norm(q) in current, "fetched": e["fetched"][:10]})
    kw_rows.sort(key=lambda r: (not r["current"], -(r["small_hit_share"] or 0), -(r["vpd_median"] or 0)))
    # 자동완성 (사람들이 찾는 말) 중 최근 영상이 적은 말
    phrases = {}
    for seed, sugg in (ac or {}).items():
        n = len(sugg) or 1
        for rank, ph in enumerate(sugg):
            if norm(ph) == norm(seed) or any(w and w in ph for w in ex["OFF_TOPIC"]):
                continue
            e = phrases.setdefault(ph, {"phrase": ph, "score": 0.0, "seeds": []})
            e["score"] += (n - rank) / n
            e["seeds"].append(seed)
    ac_rows = []
    for ph, e in phrases.items():
        words = title_words(ph)
        if not words:
            continue
        pool_n = sum(1 for x in market if words <= x["_words"])
        sup = supplies.get(ph)
        ver = None
        if sup:
            xs = [by_id[i] for i in sup.get("ids") or [] if i in by_id]
            vsum = sum(x["vpd"] for x in xs)
            ver = {"total": sup.get("total"), "days": sup.get("days"), "found": len(xs), "fetched": str(sup.get("fetched") or "")[:10],
                   "views_median": _median([x["views"] for x in xs]), "vpd_median": _median([x["vpd"] for x in xs]),
                   "vpd_per_video": round(vsum / sup["total"], 1) if sup.get("total") else None,
                   "small_share": round(sum(1 for x in xs if x["subs"] is not None and x["subs"] <= C["MAX_SUBS"]) / len(xs), 3) if xs else None,
                   "recent30": sum(1 for x in xs if (x["age_days"] or 999) <= 30)}
        ac_rows.append({"phrase": ph, "score": round(e["score"], 2), "seeds": e["seeds"][:3], "pool_recent": pool_n,
                        "gap": round(e["score"] / (1 + pool_n), 3), "verified": ver})
    ac_rows.sort(key=lambda r: -r["gap"])
    top_ac = ac_rows[:D["AUTOCOMPLETE_TOP"]]
    gap_candidates = [r["phrase"] for r in ac_rows if not r["verified"]][:D["GAP_VERIFY_N"]]
    limits = []
    if not market:
        limits.append("수요·공급: 최근 영상 자료 없음 (PC 에서 탐색한 뒤 다시)")
    else:
        limits.append(f"수요·공급의 '시장'은 탐색·검색에서 본 최근 {D['RECENT_DAYS']}일 영상 {len(market)}개 — 검색이 조회수 순이라 조회수 적은 영상이 덜 잡힌다. "
                      "주제 묶음 사이의 상대 비교(지수)로만 보라")
    if kw_rows and not any(r["total"] for r in kw_rows):
        limits.append("검색어별 결과 수(공급 추정)는 outlier_research v2.1 이후의 검색부터 저장된다 — 그 전 검색은 '–' (7일 캐시가 지나 다시 검색하면 채워짐)")
    if not ac:
        limits.append("자동완성(사람들이 찾는 말) 자료 없음 — 웹 화면에서 '검색어로도 찾기'로 탐색하면 받는다 (할당량 0)")
    elif top_ac and not any(r["verified"] for r in top_ac):
        limits.append("자동완성 말의 '최근 영상 수'는 우리가 본 영상만 셌다 — 실제 공급은 웹 화면 [공급 확인](말 하나에 검색 1번 = 100단위)으로 확인")
    log("MARKET", market=len(market), themes=len(th_rows), keywords=len(kw_rows), autocomplete=len(ac_rows),
        verified=sum(1 for r in ac_rows if r["verified"]), gap_candidates=len(gap_candidates))
    return {"days": D["RECENT_DAYS"], "videos": len(market), "themes": th_rows, "keywords": kw_rows, "keywords_total": len(kw_rows),
            "autocomplete": top_ac, "autocomplete_total": len(ac_rows), "gap_candidates": gap_candidates, "limits": limits}


def market_caches_current(rules):
    """지금 검색어 (keywords.txt) — 검색어별 표에서 예전 검색어와 나눔."""
    return rules.get("keywords") or []


def channel_growth(rows_all, rules, now):
    """빨리 크는 작은 채널 (v1.0): 개설 NEW_CHANNEL_MONTHS 개월 안·구독자 MIN_SUBS 이상 — 월 구독자 증가(구독자 ÷ 개설 뒤 달 수) 순.
    받을 때마다 남긴 구독자 기록(history)이 3일 넘게 벌어져 있으면 최근 하루 증가도."""
    G, C = rules["growth"], rules["compare"]
    chs = getattr(load_cache, "channels", {}) or {}
    vids = defaultdict(list)
    for x in rows_all:
        if not x["exclude"] and x["channel_id"]:
            vids[x["channel_id"]].append(x)
    rows, no_created = [], 0
    for cid, xs in vids.items():
        e = chs.get(cid) or {}
        if not e.get("created"):
            no_created += 1
            continue
        try:
            created = datetime.fromisoformat(str(e["created"]).replace("Z", "+00:00"))
        except ValueError:
            continue
        months = max((now - created).days / 30.44, 1)
        subs = e.get("subs")
        if subs is None:
            continue
        hist = sorted((e.get("history") or {}).items())
        recent = None
        if len(hist) >= 2:
            d0, d1 = datetime.fromisoformat(hist[0][0]), datetime.fromisoformat(hist[-1][0])
            if (d1 - d0).days >= 3:
                recent = round((hist[-1][1] - hist[0][1]) / (d1 - d0).days, 1)
        best = max(xs, key=lambda x: x["vpd"])
        rows.append({"channel_id": cid, "channel": xs[0]["channel"] or e.get("title"), "created": str(e["created"])[:10],
                     "months": round(months, 1), "subs": subs, "videos": e.get("videos"), "subs_per_month": round(subs / months),
                     "uploads_per_month": round((e.get("videos") or 0) / months, 1), "subs_per_day_recent": recent,
                     "themes": [t for t, _ in Counter(x["theme"] for x in xs).most_common(2)], "seen_videos": len(xs),
                     "minutes_median": _median([x["minutes"] for x in xs]),
                     "best": {"id": best["id"], "title": best["title"], "views": best["views"], "vpd": best["vpd"]}})
    fast = sorted((r for r in rows if r["months"] <= G["NEW_CHANNEL_MONTHS"] and r["subs"] >= G["MIN_SUBS"]),
                  key=lambda r: -r["subs_per_month"])[:G["TOP"]]
    limits = []
    if no_created and not rows:
        limits.append("채널 개설일 자료 없음 — outlier_research v2.1 로 다시 탐색하면 채널을 한 번 다시 받는다 (50채널 1단위). 그때부터 '빨리 크는 채널'이 나온다")
    elif no_created:
        limits.append(f"채널 {no_created}곳은 개설일이 아직 없음 (다음 탐색 때 채움)")
    if rows and not any(r["subs_per_day_recent"] is not None for r in rows):
        limits.append("채널의 최근 구독자 증가는 구독자 수를 3일 넘게 사이를 두고 두 번 이상 받아야 나온다 (7일마다 다시 받음)")
    log("GROWTH", channels=len(rows), fast=len(fast), no_created=no_created)
    return {"channels": len(rows), "fast": fast, "limits": limits}


def case_view(c):
    sp = c["speech"] or {}
    return {"no": c["no"], "id": c["id"], "title": c["title"], "channel": c["channel"], "subs": c["subs"], "views": c["views"],
            "ratio": c["ratio"], "views_per_day": c["vpd"], "minutes": c["minutes"], "likes": c["likes"],
            "like_rate": round(c["likes"] / max(c["views"], 1), 4), "published": c["published"].date().isoformat() if c["published"] else "",
            "age_days": c["age_days"], "theme": c["theme"], "folder": c["folder"], "kind": c["kind"], "thumbnail": c["thumb"],
            "text_source": c["src"], "chapters": c["chapters"], "description": c["desc_text"][:400],
            "hook20": sp.get("hook20"), "first60": sp.get("first60"), "outline": sp.get("outline"), "syl_per_sec": sp.get("syl_per_sec"),
            "comments_fetched": c["comments_fetched"], "comments_total": c["comments_total"], "comments_complete": c["comments_complete"],
            "hook_first": c.get("hook_first"), "hook_types": c.get("hook_types"),
            "needs": {k: c["needs"].get(k, 0) for k in NEED_CATS},
            "need_quotes": {k: sorted((q for q in c["need_quotes"].get(k, []) if not q["reply"]), key=lambda q: -q["likes"])[:2]
                            for k in NEED_CATS if c["need_quotes"].get(k)},
            "url": f"https://www.youtube.com/watch?v={c['id']}"}


# ---------------------------------------------------------------- 썸네일 한 장에
def contact_sheet(items, out_path, cols=4, w=320):
    """[(번호, 이미지 경로)] → 한 장 (번호를 왼쪽 위에). Pillow 가 없으면 건너뜀 → 만든 장 수."""
    try:
        from PIL import Image, ImageDraw
    except ImportError:
        log("THUMBS", logging.WARNING, note="Pillow 없음 — 썸네일 한 장 만들기 건너뜀 (사례 폴더의 thumbnail.jpg 는 있음)")
        return 0
    items = [(n, p) for n, p in items if p and Path(p).is_file()]
    if not items:
        return 0
    h = w * 9 // 16
    rows = math.ceil(len(items) / cols)
    sheet = Image.new("RGB", (cols * w, rows * h), (20, 20, 20))
    draw = ImageDraw.Draw(sheet)
    for k, (n, p) in enumerate(items):
        try:
            im = Image.open(p).convert("RGB")
        except Exception:
            continue
        iw, ih = im.size                                        # 4:3 썸네일(hqdefault)의 위아래 검은 띠를 잘라 16:9 로
        target = iw * 9 / 16
        if ih > target:
            top = (ih - target) / 2
            im = im.crop((0, int(top), iw, int(top + target)))
        im = im.resize((w, h))
        x, y = (k % cols) * w, (k // cols) * h
        sheet.paste(im, (x, y))
        draw.rectangle([x, y, x + 34, y + 20], fill=(0, 0, 0))
        draw.text((x + 5, y + 4), f"#{n}", fill=(255, 255, 0))
    sheet.save(out_path, "JPEG", quality=82)
    return len(items)


# ---------------------------------------------------------------- 쓰기
def _pct(x):
    if not isinstance(x, (int, float)):
        return "–"
    return f"{x:.1%}" if 0 < x < 0.1 else f"{x:.0%}"


def _n(x):
    return f"{x:,}" if isinstance(x, int) else (f"{x:,.1f}" if isinstance(x, float) else "–")


def _cell(s, n=60):
    s = re.sub(r"\s+", " ", str(s or "")).strip().replace("|", "∣")
    return s if len(s) <= n else s[: n - 1] + "…"


def _rate_txt(r):
    return f"{r['n']} ({_pct(r['rate'])})" if r["n"] else "0"


def write_md(out, data, success):
    S, C = data["rules"]["success"], data["rules"]["compare"]
    src = data["sources"]
    L = [f"# {data['name']} — 성공 사례 분석 (지시사항 재료)", "",
         f"자동 생성 — `tools/success_analysis.py` {VERSION} ({data['generated'][:16].replace('T', ' ')} UTC), 규칙 `{data['rules']['file']}` "
         f"{data['rules']['version']}. **이 문서는 숫자와 원문만 담는다 — 해석·지시사항은 이것을 읽는 AI 가 만든다.** "
         "주별 추세는 `weekly.md`, 승인한 영상 전부는 `approved.md`. ※ 연구·교육용 — 투자 권유가 아님.", "",
         "## 0. 자료와 한계", "",
         "| 자료 | 수 |", "|---|---|",
         f"| 사례 폴더 (설명·자막·댓글·썸네일을 받은 영상) | {src['case_folders']} ({', '.join(f'{k} {v}' for k, v in src['by_kind'].items()) or '-'}) |",
         f"| **성공 사례** — {S['MAX_AGE_DAYS']}일 안·구독자 {S['MAX_SUBS']:,} 이하·조회수 ≥ 구독자 × {S['MIN_RATIO']:g}·{S['MIN_VIEWS']:,}회 이상·"
         f"{S['MIN_MINUTES']:g}분 이상, 채널당 {S['CASES_PER_CHANNEL']}개 | **{len(success)}** (기준 통과 {src['success_passed']} − 뺀 것 "
         f"{len(src['success_excluded'])} − 채널당 제한 {len(src['success_channel_cut'])}) |",
         f"| 성공 사례의 글 출처 (자막·음성인식·설명·없음) | {' · '.join(f'{k} {v}' for k, v in src['success_text_sources'].items()) or '-'} |",
         f"| 성공 사례 댓글 (받은 / 달린) | {src['success_comments_fetched']:,} / {src['success_comments_reported']:,} |",
         f"| 성공 사례 썸네일 | {src['success_thumbnails']} |",
         f"| 비교 집단 — 탐색에서 본 영상 중 구독자 {C['MAX_SUBS']:,} 이하·{C['MIN_MINUTES']:g}분 이상·{C['MAX_AGE_DAYS']}일 안·주제 관련, "
         f"채널당 최근 {C['PER_CHANNEL']}개 | {src['compare_group']} (성공 {src['compare_success']} = {_pct(src['compare_rate'])}, 채널당 제한으로 뺀 {src['compare_channel_cut']}) |",
         f"| 자료를 받지 않은 성공 후보 (웹 화면에서 승인하면 들어감) | {data['missing_success_total']} |",
         f"| 수요·공급 시장 — 최근 {data['market']['days']}일 영상 (채널 크기 상관없음) | {data['market']['videos']} · 검색어 {data['market']['keywords_total']} · "
         f"자동완성 말 {data['market']['autocomplete_total']} (공급 확인 {sum(1 for r in data['market']['autocomplete'] if r['verified'])}) |",
         f"| 채널 성장 자료 (개설일이 있는 채널) | {data['growth']['channels']} (빨리 크는 작은 채널 {len(data['growth']['fast'])}) |", ""]
    if src["success_excluded"]:
        L.append("성공 기준은 넘었지만 뺀 영상: " + " · ".join(f"{_cell(x['title'], 30)} ({x['why']})" for x in src["success_excluded"][:12]))
        L.append("")
    L += ["**한계**", ""] + [f"- {x}" for x in data["limits"]] + [""]
    # 1. 성공 사례
    L += [f"## 1. 성공 사례 ({len(success)}개 — 배수 큰 순)", "",
          "| # | 썸네일 | 제목 | 채널 | 구독자 | 조회수 | 배수 | 하루 조회수 | 길이 | 업로드 | 주제 묶음 | 글 출처 | 댓글 받은/달린 |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for c in data["success_cases"]:
        img = f'<img src="{c["thumbnail"]}" width="160">' if c["thumbnail"] else "–"
        L.append(f"| {c['no']} | {img} | [{_cell(c['title'], 60)}]({c['url']}) | {_cell(c['channel'], 14)} | {_n(c['subs'])} | {c['views']:,} | "
                 f"{_n(c['ratio'])} | {_n(c['views_per_day'])} | {c['minutes']:g}분 | {c['published']} | {_cell(c['theme'], 14)} | {c['text_source']} | "
                 f"{c['comments_fetched']:,}/{c['comments_total']:,} |")
    if data["missing_success"]:
        L += ["", f"### 자료를 받지 않은 성공 후보 ({data['missing_success_total']}개 중 배수 큰 {len(data['missing_success'])}개 — 웹 화면 탐색 목록에서 승인하면 분석에 들어감)", "",
              "| 제목 | 채널 | 구독자 | 조회수 | 배수 | 길이 | 업로드 | 주제 묶음 |", "|---|---|---|---|---|---|---|---|"]
        for x in data["missing_success"]:
            L.append(f"| [{_cell(x['title'], 60)}](https://www.youtube.com/watch?v={x['id']}) | {_cell(x['channel'], 14)} | {_n(x['subs'])} | "
                     f"{x['views']:,} | {_n(x['ratio'])} | {x['minutes']:g}분 | {x['published']} | {_cell(x['theme'], 14)} |")
    # 2. 주제
    L += ["", "## 2. 주제 — 주제 묶음별 성공 비율 (비교 집단)", "",
          f"주제 묶음 = `tag_rules.toml` TAG_THEMES (제목에서 맞는 글자가 가장 긴 묶음, 없으면 태그). 비교 집단 성공 비율 {_pct(src['compare_rate'])} 과 견주어 본다. "
          f"영상 {C['MIN_GROUP']}개 미만은 '표본 적음'.", "",
          "| 주제 묶음 | 영상 | 성공 | 성공 비율 | 배수 중앙값 | 조회수 중앙값 | 성공 사례 # |", "|---|---|---|---|---|---|---|"]
    for r in data["themes"]:
        L.append(f"| {r['theme']}{' (표본 적음)' if r['small_sample'] else ''} | {r['n']} | {r['success']} | {_pct(r['rate'])} | {_n(r['ratio_median'])} | "
                 f"{_n(r['views_median'])} | {', '.join(map(str, r['success_cases'])) or '-'} |")
    # 3. 수요와 공급
    mk = data["market"]
    L += ["", "## 3. 수요와 공급 — 찾는 사람에 비해 영상이 적은 곳", "",
          f"### 3-1. 주제 묶음별 (최근 {mk['days']}일 영상 {mk['videos']}개 — 채널 크기 상관없음)", "",
          "수요 몫 = 그 묶음 영상들의 하루 조회수 합 ÷ 전체, 공급 몫 = 영상 수 ÷ 전체. **지수 = 수요 몫 ÷ 공급 몫** — 1 보다 크면 영상 하나가 평균보다 "
          "많이 보임(공급이 모자라 보임), 작으면 영상이 넘침. 작은 채널 성공 비율 = 2번 표. 시청자 질문 = 사례 댓글 중 그 묶음 낱말이 든 질문·요청.", "",
          "| 주제 묶음 | 영상(공급) | 채널 | 수요 몫 | 공급 몫 | 지수 | 영상당 하루 조회수 중앙값 | 작은 채널 성공 비율 | 시청자 질문 |",
          "|---|---|---|---|---|---|---|---|---|"]
    for r in mk["themes"]:
        L.append(f"| {r['theme']}{' (표본 적음)' if r['small_sample'] else ''} | {r['videos']} | {r['channels']} | {_pct(r['demand_share'])} | "
                 f"{_pct(r['supply_share'])} | **{_n(r['index'])}** | {_n(r['vpd_median'])} | {_pct(r['small_success_rate'])} | {r['questions']} |")
    L += ["", "### 3-2. 검색어별 (탐색·검색 캐시 — 검색어마다 조회수 순 상위 결과)", "",
          "결과 수 = YouTube 가 알려 준 그 기간 영상 수 추정(공급). 영상당 하루 조회수 = 상위 결과 하루 조회수 합 ÷ 결과 수 (클수록 영상에 비해 찾는 사람이 많음). "
          "큰 채널 비율 = 상위 결과 중 구독자 5만 넘는 채널 (클수록 들어가기 어려움). **작은 채널이 뚫은 비율** = 상위 결과 중 작은 채널(5만 이하)의 "
          "성공 영상(×3·1만) 비율 — 클수록 새 채널도 상위에 들 수 있음. 지금 검색어(keywords.txt)가 먼저, 예전 검색어는 '(예전)'.", "",
          "| 검색어 | 기간(일) | 본 영상 | 결과 수(공급) | 최근 30일 | 조회수 중앙값 | 하루 조회수 중앙값 | 영상당 하루 조회수 | 큰 채널 비율 | 작은 채널이 뚫은 비율 |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    for r in mk["keywords"][:40]:
        L.append(f"| {_cell(r['q'], 24)}{'' if r['current'] else ' (예전)'} | {r['days'] or '–'} | {r['found']} | {_n(r['total'])} | {r['recent30']} | "
                 f"{_n(r['views_median'])} | {_n(r['vpd_median'])} | {_n(r['vpd_per_video'])} | {_pct(r['big_share'])} | "
                 f"{_pct(r['small_hit_share'])} ({r['small_success']}개) |")
    if mk["keywords_total"] > 40:
        L.append(f"| … 나머지 {mk['keywords_total'] - 40}개는 analysis.json |  |  |  |  |  |  |  |  |  |")
    L += ["", "### 3-3. 사람들이 찾는 말 (YouTube 자동완성) 중 최근 영상이 적은 말", "",
          "수요 점수 = 검색어를 넣었을 때 자동완성에 앞쪽에 나올수록·여러 검색어에서 나올수록 큼. 최근 영상 = 우리가 본 최근 영상 중 제목에 그 말의 낱말이 다 든 수. "
          "틈 = 수요 점수 ÷ (1 + 최근 영상). **공급 확인** = 웹 화면 [공급 확인]으로 그 말을 직접 검색한 결과 (최근 90일 결과 수·상위 영상).", "",
          "| 말 | 수요 점수 | 나온 검색어 | 최근 영상(우리가 본) | 틈 | 공급 확인: 결과 수 | 영상당 하루 조회수 | 작은 채널 비율 | 최근 30일 |",
          "|---|---|---|---|---|---|---|---|---|"]
    for r in mk["autocomplete"]:
        v = r["verified"] or {}
        L.append(f"| {_cell(r['phrase'], 30)} | {r['score']} | {_cell(', '.join(r['seeds']), 30)} | {r['pool_recent']} | {r['gap']} | "
                 f"{_n(v.get('total')) if v else '확인 전'} | {_n(v.get('vpd_per_video')) if v else ''} | {_pct(v.get('small_share')) if v else ''} | "
                 f"{v.get('recent30', '') if v else ''} |")
    if not mk["autocomplete"]:
        L.append("| (자동완성 자료 없음 — 웹 화면 탐색 때 받음) |  |  |  |  |  |  |  |  |")
    qs = [r for r in mk["themes"] if r["top_questions"]]
    if qs:
        L += ["", "### 3-4. 주제 묶음별 시청자 질문 (사례 댓글 — 좋아요 순)", ""]
        for r in sorted(qs, key=lambda r: -r["questions"]):
            L.append(f"- **{r['theme']}** ({r['questions']}개): " + " / ".join(f"👍{q['likes']} “{_cell(q['text'], 110)}”" for q in r["top_questions"]))
    # 4. 제목
    L += ["", "## 4. 제목", "", "### 4-1. 제목 특징별 성공 비율 (비교 집단: 있음 vs 없음)", "",
          f"'눈에 띔' = 차이 {C['NOTABLE_DIFF']:.0%}p 이상 · 양쪽 {C['MIN_GROUP']}개 이상 (원인이 아니라 표시). 마지막 열 = 성공 사례 중 그 특징이 있는 비율.", "",
          "| 제목 특징 | 있음 (성공 비율) | 없음 (성공 비율) | 차이 | 표시 | 성공 사례 중 |", "|---|---|---|---|---|---|"]
    for r in data["title_features"]:
        mark = "**눈에 띔**" if r["notable"] else ("표본 적음" if r["small_sample"] else "")
        diff = f"{r['diff'] * 100:+.0f}%p" if r["diff"] is not None else "–"
        L.append(f"| {_cell(r['feature'], 50)} | {_rate_txt(r['with'])} | {_rate_txt(r['without'])} | {diff} | {mark} | {_pct(r['success_case_share'])} |")
    L += ["", "### 4-2. 제목 낱말 (비교 집단 제목에 자주 나온 낱말 — 조사를 거칠게 뗌)", "",
          "| 낱말 | 있음 (성공 비율) | 없음 (성공 비율) | 차이 | 표시 |", "|---|---|---|---|---|"]
    for r in data["title_words_up"] + data["title_words_down"]:
        mark = "**눈에 띔**" if r["notable"] else ("표본 적음" if r["small_sample"] else "")
        L.append(f"| {_cell(r['word'], 20)} | {_rate_txt(r['with'])} | {_rate_txt(r['without'])} | {r['diff'] * 100:+.0f}%p | {mark} |")
    L += ["", "### 4-3. 제목 길이", "", "| 길이 | 영상 (성공 비율) |", "|---|---|"]
    L += [f"| {r['label']} | {_rate_txt(r)} |" for r in data["title_length"]]
    L += ["", "성공 사례 제목 전부는 1번 표 (#순)."]
    # 5. 썸네일
    L += ["", "## 5. 썸네일", "",
          "글자·얼굴·색·구도는 자동으로 뽑지 않는다 — **이미지를 직접 보고** 판단한다 (번호 = 1번 표의 #).", ""]
    if (Path(out) / "analysis_thumbs.jpg").is_file():
        L += ["성공 사례:", "", "![성공 사례 썸네일](analysis_thumbs.jpg)", ""]
    if (Path(out) / "analysis_thumbs_others.jpg").is_file():
        L += ["비교 — 자료를 받았지만 성공 기준 밖 (조회수 큰 순, 번호는 `analysis.json` 의 others 순서):", "", "![비교 썸네일](analysis_thumbs_others.jpg)", ""]
    # 5. 구성
    st = data["structure"]
    L += ["## 6. 길이·내용 구성", "", "### 6-1. 길이별 성공 비율 (비교 집단)", "", "| 길이 | 영상 (성공 비율) | 성공 사례 |", "|---|---|---|"]
    L += [f"| {r['label']} | {_rate_txt(r)} | {r['success_cases']} |" for r in data["minutes"]]
    L += ["", "### 6-2. 채널 크기별 성공 비율 (참고 — 구독자가 적을수록 배수가 커지기 쉬움)", "", "| 구독자 | 영상 (성공 비율) |", "|---|---|"]
    L += [f"| {r['label']} | {_rate_txt(r)} |" for r in data["subs"]]
    L += ["", "### 6-3. 성공 사례의 구성", "",
          f"- 길이 중앙값: 성공 사례 {_n(st['minutes_median_success'])}분 · 비교 집단의 나머지 {_n(st['minutes_median_compare_others'])}분",
          f"- 타임라인(챕터) 있는 성공 사례: {_pct(st['chapters_share'])} (챕터 수 중앙값 {_n(st['chapters_count_median'])})",
          f"- 대본이 있는 성공 사례: {st['transcripts']}개 — 말 속도 중앙값 {_n(st['syl_per_sec_median'])} 음절/초, 첫 1분 음절 중앙값 {_n(st['first60_syl_median'])}"
          + ("" if st["transcripts"] else " (대본이 없어 도입부·흐름은 아직 셀 수 없음)"),
          "- 도입부(첫 20초 첫 문장) 유형: " + (" · ".join(f"{k} {v}" for k, v in (st.get("hook_types") or {}).items()) or "대본 없음 — 아직 셀 수 없음"),
          "- 사례마다의 챕터·도입부(첫 20초)·첫 1분·90초마다 흐름은 9번."]
    eg = data["engagement"]
    L += ["", "### 6-4. 참여율 (비교 집단, 중앙값)", "", "| | 영상 | 좋아요 ÷ 조회수 | 댓글 ÷ 조회수 |", "|---|---|---|---|",
          f"| 성공 | {eg['success']['n']} | {_pct(eg['success']['like_rate'])} | {_pct(eg['success']['comment_rate'])} |",
          f"| 나머지 | {eg['others']['n']} | {_pct(eg['others']['like_rate'])} | {_pct(eg['others']['comment_rate'])} |"]
    # 7. 구독자 — 빨리 크는 채널
    gr = data["growth"]
    L += ["", "## 7. 구독자 — 빨리 크는 작은 채널", "",
          "YouTube API 는 영상별 구독 증가를 주지 않는다 → 채널 단위로 본다. 개설 24개월 안·구독자 1,000 이상 채널을 **월 구독자 증가(구독자 ÷ 개설 뒤 달 수)** 순으로. "
          "최근 하루 증가 = 받을 때마다 남긴 구독자 기록 (3일 넘게 벌어져야 나옴). 주로 다룬 주제 = 우리가 본 그 채널 영상의 주제 묶음.", "",
          "| 채널 | 개설 | 구독자 | 월 구독자 증가 | 최근 하루 증가 | 영상 수 | 월 업로드 | 길이 중앙값 | 주로 다룬 주제 | 대표 영상 (하루 조회수 큰 것) |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    for r in gr["fast"]:
        b = r["best"]
        L.append(f"| {_cell(r['channel'], 16)} | {r['created']} | {r['subs']:,} | {r['subs_per_month']:,} | {_n(r['subs_per_day_recent'])} | {_n(r['videos'])} | "
                 f"{_n(r['uploads_per_month'])} | {_n(r['minutes_median'])}분 | {_cell(', '.join(r['themes']), 24)} | "
                 f"[{_cell(b['title'], 40)}](https://www.youtube.com/watch?v={b['id']}) {b['views']:,}회 |")
    if not gr["fast"]:
        L.append("| (자료 없음 — 한계 참고) |  |  |  |  |  |  |  |  |  |")
    # 6. 니즈
    nd = data["needs"]
    L += ["", f"## 8. 시청자 니즈 (성공 사례 {len(success)}개의 시청자 댓글 {nd['viewer_comments']:,}개 — 채널 주인 댓글 뺌)", "",
          "| 갈래 | 댓글 | 비율 | 좋아요 합 |", "|---|---|---|---|"]
    L += [f"| {r['name']} | {r['count']:,} | {_pct(r['share'])} | {r['likes']:,} |" for r in nd["categories"]]
    for cat, qs in nd["top"].items():
        if qs:
            L += ["", f"### {cat} — 좋아요 많은 댓글", ""] + [f"- 👍{q['likes']:,} [#{q['no']}] “{q['text']}”" for q in qs]
    if nd["questions"]:
        L += ["", "### 더 알고 싶은 것 — 질문·요청 (좋아요 순, 최상위 댓글)", ""] + [f"- 👍{q['likes']:,} [#{q['no']}] “{q['text']}”" for q in nd["questions"]]
    if nd["complaints"]:
        L += ["", "### 아쉬운 점 — 비판·불만 (좋아요 순, 답글 포함)", ""] + [f"- 👍{q['likes']:,} [#{q['no']}]{' (답글)' if q['reply'] else ''} “{q['text']}”"
                                                                       for q in nd["complaints"]]
    # 9. 사례별
    L += ["", "## 9. 사례별 자세히", ""]
    for c in data["success_cases"]:
        L += [f"### {c['no']}. {_cell(c['title'], 90)}", "",
              f"- {c['url']} · {c['channel']} · 구독자 {_n(c['subs'])} · 조회수 {c['views']:,} (×{_n(c['ratio'])}, 하루 {_n(c['views_per_day'])}) · "
              f"좋아요 {c['likes']:,} ({c['like_rate']:.1%}) · {c['minutes']:g}분 · {c['published']} · 주제 묶음 {c['theme']} · 폴더 `{c['folder']}` ({c['kind']})"]
        if c["thumbnail"]:
            L.append(f'- 썸네일: <img src="{c["thumbnail"]}" width="320">')
        if c["chapters"]:
            L.append("- 챕터: " + " · ".join(f"{ch['start'] // 60}:{ch['start'] % 60:02d} {_cell(ch['title'], 30)}" for ch in c["chapters"][:20]))
        if c["description"]:
            L.append(f"- 설명 앞부분: {_cell(c['description'], 300)}")
        if c["text_source"] in ("자막", "음성인식"):
            L.append(f"- 대본 ({c['text_source']}, {_n(c['syl_per_sec'])} 음절/초) 첫 20초: “{_cell(c['hook20'], 300)}”"
                     + (f" — 도입부 유형: {', '.join(c['hook_types'])}" if c.get("hook_types") else ""))
            L.append(f"- 첫 1분: “{_cell(c['first60'], 400)}”")
            if c["outline"]:
                L.append("- 흐름 (90초마다 첫 문장): " + " → ".join(f"{o['t'] // 60}:{o['t'] % 60:02d} {_cell(o['text'], 40)}" for o in c["outline"]))
        else:
            L.append(f"- 대본 없음 ({c['text_source']}) — 음성인식이 끝나면 도입부·흐름이 들어감")
        L.append(f"- 댓글 {c['comments_fetched']:,}/{c['comments_total']:,}{'' if c['comments_complete'] else ' (다 받지 못함)'}: "
                 + " · ".join(f"{k.split(' (')[0]} {v}" for k, v in c["needs"].items()))
        for cat, qs in c["need_quotes"].items():
            for q in qs:
                L.append(f"  - {cat.split(' (')[0]} 👍{q['likes']:,} “{_cell(q['text'], 150)}”")
        L.append("")
    _write_atomic(Path(out) / "analysis.md", "\n".join(L) + "\n")


def write_compare_csv(out, rows):
    cols = ["id", "title", "channel", "subs", "views", "ratio", "minutes", "age_days", "published", "theme", "success", "in_compare", "has_case", "exclude"]
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(cols)
    for x in sorted(rows, key=lambda x: (not x["in_compare"], -(x["ratio"] or 0))):
        w.writerow([x["id"], x["title"], x["channel"], x["subs"], x["views"], x["ratio"], x["minutes"], x["age_days"],
                    x["published"].date().isoformat() if x["published"] else "", x["theme"], x["success"], x["in_compare"], x["has_case"], x["exclude"]])
    _write_atomic(Path(out) / "compare.csv", "﻿" + buf.getvalue())


def run(topic, now=None, root=None):
    root = Path(root or ROOT)
    now = now or datetime.now(timezone.utc)
    out = root / topic / "result" / "outliers"
    cfg = _toml(root / topic / "analyzer_config.toml")
    name = (cfg.get("topic") or {}).get("TOPIC") or cfg.get("TOPIC") or topic
    rules, rel, themes = load_rules(root, topic), load_rel(root, topic), load_themes(root, topic)
    cache_infos, cache_subs = load_cache(out)
    cases = load_cases(out, cache_infos, cache_subs, now)
    log("START", topic=topic, cases=len(cases), cache_videos=len(cache_infos), cache_channels=len(cache_subs), rules=rules["file"],
        themes=len(themes), relevance_terms=len(rel["strong"]), tool=f"success_analysis.py {VERSION}")
    market_caches = load_market_caches(out)
    data, success, group, rows_all, cases = analyze(topic, name, cases, cache_infos, cache_subs, rules, rel, themes, now, market_caches)
    out.mkdir(parents=True, exist_ok=True)
    n1 = contact_sheet([(c["no"], out / c["thumb"]) for c in success if c["thumb"]], out / "analysis_thumbs.jpg")
    per_ch, others = Counter(), []
    for c in sorted((c for c in cases if c["thumb"] and not any(c is s for s in success)), key=lambda c: -c["views"]):
        if per_ch[c["channel_id"] or c["channel"]] < 2 and len(others) < 24:      # 채널당 2개 — 한 채널이 비교 장을 덮지 않게
            per_ch[c["channel_id"] or c["channel"]] += 1
            others.append(c)
    n2 = contact_sheet([(k, out / c["thumb"]) for k, c in enumerate(others, 1)], out / "analysis_thumbs_others.jpg")
    for p, n in ((out / "analysis_thumbs.jpg", n1), (out / "analysis_thumbs_others.jpg", n2)):
        if not n and p.is_file():
            p.unlink()                                               # 지난번 장이 남아 지금 자료와 어긋나지 않게
    data["others"] = [{"k": k, "id": c["id"], "title": c["title"], "views": c["views"], "ratio": c["ratio"], "why_not": c["exclude"] or "성공 기준 밖"}
                      for k, c in enumerate(others, 1)]
    log("THUMBS", success=n1, others=n2)
    write_md(out, data, success)
    _write_atomic(out / "analysis.json", json.dumps(data, ensure_ascii=False, indent=1, default=str))
    write_compare_csv(out, rows_all)                                   # 뺀 영상도 까닭(exclude)과 함께 — 다시 셀 수 있게
    log("WRITE", file=str(out / "analysis.md"), success=len(success), compare=len(group), missing=data["missing_success_total"])
    log("DONE", topic=topic, success=len(success), compare_rate=data["sources"]["compare_rate"],
        text_sources=",".join(f"{k}:{v}" for k, v in data["sources"]["success_text_sources"].items()) or "-")
    return data


def main(argv=None):
    ap = argparse.ArgumentParser(description="성공 사례 분석 — 주제·제목·썸네일·구성·시청자 니즈 (AI 가 지시사항을 만들 재료, 할당량 0)")
    ap.add_argument("topic")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args(argv)
    logging.basicConfig(level=getattr(logging, a.log_level), format="%(message)s", stream=sys.stdout)
    run(a.topic)
    return 0


if __name__ == "__main__":
    sys.exit(main())
