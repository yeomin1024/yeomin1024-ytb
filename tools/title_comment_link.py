#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-21 — 새로: 제목·썸네일 문구 vs 관심 많은 댓글(좋아요 순)의 관계 — 나라(한국·미국) × 올린 주(1~4주 전) × 묶음
#          (조회수 잘 나온 영상 · 성공 사례 · 그 밖의 승인 영상). 사용자 지시 2026-10-21 "조회수 잘 나온 영상, 성공 사례 영상의 제목 및 썸네일
#          문구와 관심 많은 댓글의 상관성 비교해서 국가별(한국, 미국)로와 최신 주별(1주전~4주전)별로 알려줘봐".
#          · '조회수 잘 나온 영상' = 그 나라·그 주에 올라온 검색 영상(주제 관련·4분 이상·뺄 까닭 없음) 안 하루 조회수 상위 TOP_PCT% — 주마다 따로
#            (analysis.md 1-3번의 한 경계는 막 올라온 영상이 거의 다 차지해 3~4주 전이 비어서). 성공 사례 = analysis.json success_cases 그대로.
#          · 나라: 한국 = 한국어 영상(lang·audio_lang ko) · 미국 = 채널 나라 US(채널이 적어 둔 것 — outlier_research v2.6.1 이 받음)인 영어 영상.
#          · 썸네일 문구 = <주제>/result/outliers/thumb_text.tsv (사람·AI 가 그림을 보고 옮겨 적음 — 이 환경의 OCR 은 꾸민 글자를 거의 못 읽음).
#          숫자만 쓴다 — 해석·지시사항은 읽는 AI 가. 할당량: countries 만 (채널 50곳에 1단위). ※ 연구·교육용 — 투자 권유가 아님.
"""제목·썸네일 문구 vs 관심 많은 댓글 — 나라 × 주 × 묶음

  python3 tools/title_comment_link.py stock countries   # 채널 나라 받기 (대상 칸 채널 중 나라를 모르는 것, 50곳에 1단위)
  python3 tools/title_comment_link.py stock targets     # 칸마다 대상 영상 · 썸네일 문구가 없는 영상 목록과 모음 그림 (.yt_work/)
  python3 tools/title_comment_link.py stock report      # <주제>/result/outliers/title_comment.md · .json
"""
import argparse
import csv
import json
import logging
import math
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import outlier_research as orr       # noqa: E402
import success_analysis as sa        # noqa: E402

VERSION = "v1.0"
ROOT = Path(__file__).resolve().parent.parent
LOG = logging.getLogger("tclink")
WEEKS = 4                    # 1주 전 = 올린 지 0~6일 … 4주 전 = 21~27일
TOP_PCT = 10                 # 칸(나라·주) 안 하루 조회수 상위 %
MIN_CELL_POOL = 20           # 칸 모집단이 이보다 적으면 상위 %를 잡지 않음 (표에 '모집단 적음')
TOP_COMMENTS = 20            # 영상마다 좋아요 많은 시청자 댓글 (답글 뺌)
MIN_COMMENT_LIKES = 1
COUNTRIES = ("한국", "미국")
GROUPS = ("조회수 잘 나온 영상", "성공 사례", "그 밖의 승인 영상")
EXAMPLES_PER_CELL = 3
# 영어 낱말 거르기 (success_analysis.STOP 에 더해) — 뜻 없는 말·제목 꾸밈말
STOP_EN = set("""a an the and or but if so of to in on at by for from with as is are was were be been being it its this that these those
there here what which who whom whose how why when where will would can could should shall may might must do does did done have has had
not no yes all any some every each more most very just now then than also into out up down over under after before about again still
ever never you your yours we our ours i me my mine he him his she her they them their it's i'm don't can't won't isn't aren't vs
new next one two three four five ten get got make made take takes see watch here's why's what's let's""".split())
# 주제 갈래 — 한국어·영어 함께 (제목·썸네일·댓글에 같은 규칙). 낱말 규칙이라 거칠다.
THEMES = {
    "폭락·급락·공포": r"폭락|급락|하락|붕괴|공포|패닉|투매|반토막|서킷|검은 ?(월|화|수|목|금)요일|crash|dip|sell-?off|panic|fear|plung|collaps|bear market|bloodbath|meltdown|tank",
    "매수·기회·바닥": r"매수|사야|살 ?때|담아|줍줍|저점|바닥|기회|반등|buy|buying|bought|opportunit|bottom|gift|on sale|discount|rebound|bounce",
    "매도·현금·손절": r"매도|팔아|팔까|현금|손절|익절|sell(?!-?off)|selling|sold|cash|exit|take profit",
    "AI·반도체·빅테크": r"(?<![A-Za-z])AI(?![A-Za-z])|인공지능|반도체|삼성전자|삼전|하이닉스|닉스|엔비디아|팔란티어|테슬라|nvidia|nvda|semiconductor|chip|palantir|tesla|big tech|magnificent",
    "ETF·지수·배당": r"ETF|S&P|나스닥|지수|배당|QQQ|SPY|VOO|SCHD|커버드콜|dividend|index|nasdaq|covered call",
    "정치·정책·정부": r"이재명|윤석열|대통령|정부|정권|민주당|국힘|국민의힘|정책|국회|선거|특검|trump|biden|harris|congress|government|election|midterm|tariff|policy|white house|fed\b|powell",
    "연금·노후": r"국민연금|연금|노후|은퇴|pension|retire|401\s?k|\bira\b|social security",
    "코스피·국장": r"코스피|코스닥|국장|한국 ?증시|국내 ?증시|kospi",
    "미국 증시·미장": r"미국 ?증시|미장|미국 ?주식|뉴욕 ?증시|wall street|dow|s&p 500|us stock|american stock",
    "질문(?로 끝남)": r"\?\s*$",
}
NUM_RX = re.compile(r"\d[\d,.]*\s*(%|퍼센트|배|억|조|만|천|원|달러|\$|년|개월|주|일|x|×|k|m|b)?", re.I)


def log(stage, level=logging.INFO, **kv):
    LOG.log(level, "[%s] [%s] %s", stage, datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S"),
            " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) and (' ' in v or not v) else v}" for k, v in kv.items()))


def setup_logging(level="INFO"):
    logging.basicConfig(level=getattr(logging, level), format="%(message)s", stream=sys.stderr)
    sa.LOG.setLevel(logging.WARNING)            # 분석 본체 로그는 경고만 (이 도구 로그가 묻히지 않게)


# ---------------------------------------------------------------- 낱말
def words_of(text):
    """제목·썸네일 문구 → 낱말 집합. 한국어 = success_analysis.title_words (조사 떼기·STOP), 영어 = 소문자·STOP_EN·끝 s 떼기."""
    out = set()
    for w in sa.title_words(text):
        if re.fullmatch(r"[A-Za-z&]+", w):
            lw = w.lower()
            if lw in STOP_EN or len(lw) < 3:
                continue
            out.add(lw[:-1] if lw.endswith("s") and len(lw) > 3 and not lw.endswith("ss") else lw)
        else:
            out.add(w)
    return out


def word_rx(w):
    """댓글에서 그 낱말 찾기: 영어 = 낱말 경계·대소문자 무시·끝 s 허용, 한국어 = 그대로 들어 있음 (조사·어미가 붙어도)."""
    if re.fullmatch(r"[a-z&]+", w):
        return re.compile(r"(?<![a-z])" + re.escape(w) + r"s?(?![a-z])", re.I)
    return re.compile(re.escape(w))


def themes_of(text):
    t = str(text or "")
    return {name for name, rx in THEMES.items() if re.search(rx, t, re.I | re.M)}


# ---------------------------------------------------------------- 자료
def week_of(age_days):
    if age_days is None or age_days < 0:
        return None
    k = int(age_days // 7) + 1
    return k if k <= WEEKS else None


def country_of(x, ch):
    lang = str(x.get("lang") or "") + " " + str(x.get("audio_lang") or "")
    if re.search(r"(^|\s)ko", lang):
        return "한국"
    c = (ch.get(x.get("channel_id")) or {}).get("country") if isinstance(ch.get(x.get("channel_id")), dict) else None
    langs = [str(v) for v in (x.get("lang"), x.get("audio_lang")) if v]
    if c == "US" and (not langs or any(v.startswith("en") for v in langs)):     # 미국 채널의 영어 영상 (중국어 등은 뺌)
        return "미국"
    return None


def load_pool(topic, now):
    """success_analysis 와 같은 규칙으로 모집단(검색으로 찾은 영상 전부 + 사례)을 만듦 — analyze() 를 그대로 돌려 rows_all·사례·성공 사례를 받음."""
    out = ROOT / topic / "result" / "outliers"
    rules, rel, themes = sa.load_rules(ROOT, topic), sa.load_rel(ROOT, topic), sa.load_themes(ROOT, topic)
    cache_infos, cache_subs = sa.load_cache(out)
    cases = sa.load_cases(out, cache_infos, cache_subs, now)
    mc = sa.load_market_caches(out)
    data, success, group, rows_all, cases = sa.analyze(topic, topic, cases, cache_infos, cache_subs, rules, rel, themes, now, mc, sa.load_uploads(out))
    searched = {i for d in (mc[0] or ()) for i in (d.get("ids") or [])}
    log("LOAD", topic=topic, cache_videos=len(cache_infos), cases=len(cases), success=len(success), searched=len(searched),
        tool=f"success_analysis {sa.VERSION}")
    return out, rules, rows_all, cases, success, searched


def channels_path(out):
    return out / ".cache" / "channels.json"


def build_cells(topic, now, quiet=False):
    """칸 (나라, 주) 마다: 모집단 · 하루 조회수 경계 · 묶음별 영상(자료 받은 것) · 받지 않은 '조회수 잘 나온' 후보."""
    out, rules, rows_all, cases, success, searched = load_pool(topic, now)
    ch = json.loads(channels_path(out).read_text("utf-8")) if channels_path(out).is_file() else {}
    case_by_id = {c["id"]: c for c in cases}
    success_ids = {c["id"] for c in success}
    pool = defaultdict(list)
    unknown = Counter()
    for x in rows_all:
        if x["id"] not in searched or x["exclude"] or x["minutes"] < sa.DEFAULT_RULES["vpd_top"]["MIN_MINUTES"] or x.get("vpd") is None:
            continue
        wk = week_of(x["age_days"])
        if wk is None:
            continue
        cc = country_of(x, ch)
        if cc is None:
            unknown["나라 모름(채널 나라 없음·다른 나라)" if not (ch.get(x.get("channel_id")) or {}).get("country") else "다른 나라"] += 1
            continue
        pool[(cc, wk)].append(x)
    cells = {}
    for cc in COUNTRIES:
        for wk in range(1, WEEKS + 1):
            P = pool.get((cc, wk), [])
            thr = orr.top_pct_threshold([x["vpd"] for x in P], TOP_PCT) if len(P) >= MIN_CELL_POOL else None
            top_ids = {x["id"] for x in P if thr is not None and x["vpd"] >= thr}
            members = {g: [] for g in GROUPS}
            for c in cases:                                  # 자료를 받은 사례 — 그 칸에 드는 것
                if c["exclude"] or c["minutes"] < sa.DEFAULT_RULES["vpd_top"]["MIN_MINUTES"]:
                    continue
                if week_of(c["age_days"]) != wk or country_of(c, ch) != cc:
                    continue
                g = "성공 사례" if c["id"] in success_ids else "조회수 잘 나온 영상" if c["id"] in top_ids else "그 밖의 승인 영상"
                if c["id"] in success_ids and c["id"] in top_ids:
                    members["조회수 잘 나온 영상"].append(c)      # 둘 다면 두 묶음에 모두 (표에 겹침 수)
                members[g].append(c)
            missing = sorted((x for x in P if x["id"] in top_ids and x["id"] not in case_by_id), key=lambda x: -x["vpd"])
            cells[(cc, wk)] = {"pool": len(P), "threshold": thr, "top": len(top_ids), "members": members, "missing": missing,
                               "overlap": len(top_ids & success_ids & set(case_by_id))}
            if not quiet:
                log("CELL", country=cc, week=wk, pool=len(P), threshold=round(thr, 1) if thr else "-", top=len(top_ids),
                    top_with_data=len(members["조회수 잘 나온 영상"]), top_missing=len(missing), success=len(members["성공 사례"]),
                    other=len(members["그 밖의 승인 영상"]))
    log("POOL", unknown=dict(unknown), note="한국 = 한국어 영상, 미국 = 채널 나라 US (채널이 나라를 적지 않았으면 '나라 모름')")
    return out, ch, cells, unknown


# ---------------------------------------------------------------- countries
def cmd_countries(topic, now):
    """대상 기간(최근 WEEKS 주) 검색 영상·사례의 채널 중 나라를 모르는 것만 channels.list (50곳 1단위 — snippet.country)."""
    import cloud_run as cr
    import web_ui as w
    cr.load_tools()
    out, rules, rows_all, cases, success, searched = load_pool(topic, now)
    p = channels_path(out)
    ch = json.loads(p.read_text("utf-8")) if p.is_file() else {}
    want = sorted({x.get("channel_id") for x in list(rows_all) + list(cases)
                   if x.get("channel_id") and week_of(x.get("age_days")) is not None and not re.search(r"ko", str(x.get("lang") or "") + str(x.get("audio_lang") or ""))
                   and "country" not in (ch.get(x["channel_id"]) or {})})
    log("COUNTRY", topic=topic, channels_without_country=len(want), est_units=math.ceil(len(want) / 50))
    if not want:
        return {"fetched": 0}
    api, ledger, _ = w.make_api(topic, "title_comment_countries")
    got = 0
    try:
        for i in range(0, len(want), 50):
            api.channels(want[i:i + 50])
            for cid in want[i:i + 50]:
                meta = api.channel_meta.get(cid)
                ent = ch.get(cid) if isinstance(ch.get(cid), dict) else {}
                ent["country"] = (meta or {}).get("country")         # None = 채널이 나라를 적지 않음 (또는 채널 없음)
                ent["country_fetched"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
                ch[cid] = ent
                got += 1
    finally:
        w.record_use(topic, api, ledger, "title_comment_countries")
        p.write_text(json.dumps(ch, ensure_ascii=False), "utf-8")
    cnt = Counter((ch.get(c) or {}).get("country") for c in want)
    log("COUNTRY", topic=topic, fetched=got, units=api.used, countries=dict(cnt.most_common(12)))
    return {"fetched": got, "units": api.used}


# ---------------------------------------------------------------- targets
def thumb_text_path(out):
    return out / "thumb_text.tsv"


def load_thumb_text(out):
    p = thumb_text_path(out)
    res = {}
    if p.is_file():
        for row in csv.DictReader(p.open(encoding="utf-8"), delimiter="\t"):
            res[row["id"]] = {"text": (row.get("text") or "").strip(), "reader": row.get("reader") or ""}
    return res


def cmd_targets(topic, now, sheet_dir):
    out, ch, cells, unknown = build_cells(topic, now)
    tt = load_thumb_text(out)
    need = []
    for (cc, wk), cell in cells.items():
        for g in ("조회수 잘 나온 영상", "성공 사례"):
            for c in cell["members"][g]:
                if c["id"] not in tt and c["id"] not in {n["id"] for n in need}:
                    need.append({"id": c["id"], "country": cc, "week": wk, "group": g, "title": c["title"], "thumb": c.get("thumb") or ""})
    sheet_dir = Path(sheet_dir)
    sheet_dir.mkdir(parents=True, exist_ok=True)
    (sheet_dir / "thumb_need.json").write_text(json.dumps(need, ensure_ascii=False, indent=1), "utf-8")
    # 모음 그림 — 9장씩 3열, 원래 크기(480) 그대로 16:9 부분만 (위아래 검은 띠 뺌), 칸 위에 번호
    from PIL import Image, ImageDraw
    per, cols, wpx = 9, 3, 480
    sheets = []
    for k in range(0, len(need), per):
        part = need[k:k + per]
        hpx = wpx * 9 // 16
        im = Image.new("RGB", (cols * wpx, math.ceil(len(part) / cols) * (hpx + 24)), "white")
        dr = ImageDraw.Draw(im)
        for j, n in enumerate(part):
            x0, y0 = (j % cols) * wpx, (j // cols) * (hpx + 24)
            f = out / f"W_{n['id']}" / "thumbnail.jpg"
            if f.is_file():
                src = Image.open(f).convert("RGB").resize((wpx, wpx * 3 // 4))
                im.paste(src.crop((0, (wpx * 3 // 4 - hpx) // 2, wpx, (wpx * 3 // 4 - hpx) // 2 + hpx)), (x0, y0 + 24))
            dr.text((x0 + 6, y0 + 5), f"{k + j + 1}. {n['id']}", fill="black")
        sp = sheet_dir / f"thumb_sheet_{k // per + 1:02d}.jpg"
        im.save(sp, quality=88)
        sheets.append(str(sp))
    log("TARGETS", topic=topic, need_thumb_text=len(need), sheets=len(sheets), have_thumb_text=len(tt), dir=str(sheet_dir))
    return {"need": len(need), "sheets": len(sheets)}


# ---------------------------------------------------------------- report
def top_comments(c, k=TOP_COMMENTS):
    """좋아요 많은 시청자 댓글 k 개 (채널 주인·답글·도배 꼴 뺌)."""
    cs = [m for m in c["comments"] if not m["creator"] and not m["reply"] and m["text"].strip() and m["likes"] >= MIN_COMMENT_LIKES
          and not re.search(sa.SPAM_RX, m["text"])]
    return sorted(cs, key=lambda m: -m["likes"])[:k]


def share(comments, pred):
    return sum(1 for m in comments if pred(m["text"])) / len(comments) if comments else None


def mean(xs):
    xs = [x for x in xs if x is not None]
    return sum(xs) / len(xs) if xs else None


def video_row(c, tt):
    tc = top_comments(c)
    tw = words_of(c["title"])
    th = (tt.get(c["id"]) or {}).get("text")
    hw = words_of(th) if th else set()
    rxs = {w: word_rx(w) for w in tw | hw}
    return {"c": c, "comments": tc, "tw": tw, "hw": hw, "th": th, "rx": rxs,
            "title_themes": themes_of(c["title"]), "thumb_themes": themes_of(th) if th else set(),
            "echo_title": share(tc, lambda t: any(rxs[w].search(t) for w in tw)) if tw else None,
            "echo_thumb": share(tc, lambda t: any(rxs[w].search(t) for w in hw)) if hw else None,
            "title_has_num": bool(NUM_RX.search(c["title"])), "thumb_text": th}


def baseline_echo(v, others, key):
    """우연 겹침: v 의 댓글에 '같은 나라 다른 영상'의 제목(썸네일) 낱말이 나오는 비율의 평균."""
    if not v["comments"]:
        return None
    vals = []
    for u in others:
        ws = u[key]
        if u is v or not ws:
            continue
        rx = [word_rx(w) for w in ws]
        vals.append(share(v["comments"], lambda t: any(r.search(t) for r in rx)))
    return mean(vals)


def cmd_report(topic, now, md_only=False):
    out, ch, cells, unknown = build_cells(topic, now)
    tt = load_thumb_text(out)
    rows = {}           # (cc, wk, g) → [video_row]
    by_country = defaultdict(list)
    vrows = {}          # 영상 하나 = video_row 하나 (잘 나온 영상이면서 성공 사례인 영상이 두 번 세이지 않게 — 묶음끼리 같은 것을 씀)
    for (cc, wk), cell in cells.items():
        for g in GROUPS:
            for c in cell["members"][g]:
                if c["id"] not in vrows:
                    vrows[c["id"]] = video_row(c, tt)
            rows[(cc, wk, g)] = [vrows[c["id"]] for c in cell["members"][g]]
            by_country[cc] += rows[(cc, wk, g)]
    # 우연 겹침 기준: 같은 나라 다른 영상 최대 60개 (하루 조회수 순으로 고정 — 다시 돌려도 같은 값)
    for cc, vs in by_country.items():
        ref = sorted({id(v): v for v in vs}.values(), key=lambda v: -(v["c"].get("vpd") or 0))[:60]
        for v in vs:
            if "base_title" not in v:
                v["base_title"] = baseline_echo(v, ref, "tw")
                v["base_thumb"] = baseline_echo(v, ref, "hw")
    data = {"tool": f"title_comment_link.py {VERSION}", "topic": topic, "generated": now.isoformat(timespec="minutes"),
            "rules": {"weeks": WEEKS, "top_pct": TOP_PCT, "min_cell_pool": MIN_CELL_POOL, "top_comments": TOP_COMMENTS,
                      "min_comment_likes": MIN_COMMENT_LIKES, "themes": THEMES},
            "unknown_country": dict(unknown), "cells": [], "themes": {}, "words": {}, "examples": {}, "kr_needs": {}}
    for (cc, wk), cell in sorted(cells.items(), key=lambda kv: (COUNTRIES.index(kv[0][0]), kv[0][1])):
        for g in GROUPS:
            vs = rows[(cc, wk, g)]
            data["cells"].append({
                "country": cc, "week": wk, "group": g, "pool": cell["pool"], "threshold": cell["threshold"], "top": cell["top"],
                "missing": len(cell["missing"]) if g == GROUPS[0] else None, "overlap_success": cell["overlap"] if g == GROUPS[0] else None,
                "videos": len(vs), "comments": sum(len(v["comments"]) for v in vs),
                "thumb_text": sum(1 for v in vs if v["th"]),
                "echo_title": mean(v["echo_title"] for v in vs), "base_title": mean(v["base_title"] for v in vs if v["echo_title"] is not None),
                "echo_thumb": mean(v["echo_thumb"] for v in vs), "base_thumb": mean(v["base_thumb"] for v in vs if v["echo_thumb"] is not None),
                "title_num": mean(1.0 if v["title_has_num"] else 0.0 for v in vs),
                "title_q": mean(1.0 if "질문(?로 끝남)" in v["title_themes"] else 0.0 for v in vs)})
    # 주제 갈래: 나라·묶음(잘 나온+성공 합침 / 그 밖)·주 → 제목(또는 썸네일)에 그 갈래가 있을 때 vs 없을 때 좋아요 많은 댓글의 언급률
    for cc in COUNTRIES:
        for wk in list(range(1, WEEKS + 1)) + [0]:
            vs = [v for (c2, w2, g), L in rows.items() if c2 == cc and (wk == 0 or w2 == wk) and g != GROUPS[2] for v in L]
            vs = list({id(v): v for v in vs}.values())
            res = {}
            for name, rx in THEMES.items():
                if name == "질문(?로 끝남)":
                    continue
                has = [v for v in vs if name in (v["title_themes"] | v["thumb_themes"]) and v["comments"]]
                no = [v for v in vs if name not in (v["title_themes"] | v["thumb_themes"]) and v["comments"]]
                f = lambda v: share(v["comments"], lambda t: re.search(rx, t, re.I) is not None)
                res[name] = {"with_n": len(has), "with_share": mean(f(v) for v in has), "without_n": len(no), "without_share": mean(f(v) for v in no),
                             "title_share": len(has) / len(vs) if vs else None}
            data["themes"][f"{cc}|{wk}"] = res
    # 낱말: 칸(나라·주, 잘 나온+성공)마다 제목·썸네일 낱말 중 '자기 댓글에 나온 비율 − 같은 나라 다른 영상 댓글에 나온 비율'이 큰 것
    for cc in COUNTRIES:
        allv = list({id(v): v for v in by_country[cc]}.values())
        for wk in range(1, WEEKS + 1):
            vs = list({id(v): v for g in GROUPS[:2] for v in rows[(cc, wk, g)]}.values())
            stat = defaultdict(lambda: {"videos": 0, "own": [], "src": Counter()})
            for v in vs:
                if not v["comments"]:
                    continue
                for w in v["tw"] | v["hw"]:
                    s = stat[w]
                    s["videos"] += 1
                    s["own"].append(share(v["comments"], v["rx"][w].search))
                    s["src"]["제목" if w in v["tw"] else "썸네일"] += 1
                    if w in v["tw"] and w in v["hw"]:
                        s["src"]["둘 다"] += 1
            lst = []
            for w, s in stat.items():
                if s["videos"] < 2:
                    continue
                rx = word_rx(w)
                other = [share(u["comments"], rx.search) for u in allv if u["comments"] and w not in (u["tw"] | u["hw"])]
                own, base = mean(s["own"]), mean(other)
                lst.append({"word": w, "videos": s["videos"], "own": own, "base": base, "lift": (own or 0) - (base or 0),
                            "where": "·".join(k for k in ("제목", "썸네일") if s["src"][k])})
            data["words"][f"{cc}|{wk}"] = sorted(lst, key=lambda x: -x["lift"])[:10]
            # 사례: 그 칸 잘 나온+성공 중 제목 메아리(자기 − 우연)가 큰 것
            ex = sorted((v for v in vs if v["echo_title"] is not None), key=lambda v: -((v["echo_title"] or 0) - (v["base_title"] or 0)))[:EXAMPLES_PER_CELL]
            data["examples"][f"{cc}|{wk}"] = [{
                "id": v["c"]["id"], "title": v["c"]["title"], "thumb_text": v["th"], "channel": v["c"]["channel"], "subs": v["c"]["subs"],
                "views": v["c"]["views"], "vpd": v["c"].get("vpd"), "success": v["c"]["id"] in {x["c"]["id"] for x in rows[(cc, wk, GROUPS[1])]},
                "echo_title": v["echo_title"], "base_title": v["base_title"], "echo_thumb": v["echo_thumb"],
                "comments": [{"likes": m["likes"], "text": re.sub(r"\s+", " ", m["text"]).strip()[:160]} for m in v["comments"][:3]]} for v in ex]
    # 한국: 좋아요 많은 댓글의 갈래 (success_analysis 와 같은 낱말 규칙 — 한국어만)
    for wk in range(1, WEEKS + 1):
        for g in GROUPS:
            vs = rows[("한국", wk, g)]
            cs = [m for v in vs for m in v["comments"]]
            cnt = Counter(cat for m in cs for cat in sa.classify_comment(m["text"]))
            data["kr_needs"][f"{wk}|{g}"] = {"comments": len(cs), **{k: (cnt[k] / len(cs) if cs else None) for k in sa.NEED_CATS}}
    data["missing"] = {f"{cc}|{wk}": [{"id": x["id"], "title": x["title"], "channel": x["channel"], "subs": x["subs"], "vpd": x["vpd"]}
                                     for x in cell["missing"]] for (cc, wk), cell in cells.items()}
    write_md(out, data, now)
    if not md_only:
        (out / "title_comment.json").write_text(json.dumps(data, ensure_ascii=False, indent=1, default=str), "utf-8")
    log("REPORT", topic=topic, file=str(out / "title_comment.md"), cells=len(data["cells"]),
        videos=sum(c["videos"] for c in data["cells"]), comments=sum(c["comments"] for c in data["cells"]),
        thumb_text=sum(c["thumb_text"] for c in data["cells"]))
    return data


# ---------------------------------------------------------------- 쓰기
def pct(x):
    return "-" if x is None else f"{x * 100:.0f}%"


def pp(a, b):
    return "-" if a is None or b is None else f"{(a - b) * 100:+.0f}%p"


def n(x):
    return "-" if x is None else f"{x:,.0f}"


def cell_txt(s, k=70):
    s = re.sub(r"\s+", " ", str(s or "")).replace("|", "∣")
    return s if len(s) <= k else s[:k - 1] + "…"


def week_label(wk, now):
    from datetime import timedelta
    a, b = (now - timedelta(days=7 * wk - 1)).date(), (now - timedelta(days=7 * (wk - 1))).date()
    return f"{wk}주 전 ({a.strftime('%m-%d')}~{b.strftime('%m-%d')})"


def write_md(out, data, now):
    L = [f"# 제목·썸네일 문구 vs 관심 많은 댓글 — 나라 × 주", "",
         f"자동 생성 — `tools/title_comment_link.py` {VERSION} ({data['generated']} UTC). **숫자와 원문만** — 해석·지시사항은 읽는 AI 가. "
         "※ 연구·교육용 — 투자 권유가 아님.", "",
         "## 0. 자료와 한계 (먼저 읽기)", "",
         f"- **칸** = 나라(한국 = 한국어 영상 · 미국 = 채널 나라 US 인 영어 영상) × 올린 주(1주 전 = 올린 지 0~6일 … {WEEKS}주 전 = {WEEKS * 7 - 7}~{WEEKS * 7 - 1}일). "
         "채널 나라는 채널이 스스로 적은 값이라, 다른 나라 사람이 US 로 적은 채널(예: 인도 투자 유튜버 Akshat Shrivastava·Raj Shamani)도 미국에 든다.",
         f"- **조회수 잘 나온 영상** = 그 칸의 검색 영상(주제 관련·4분 이상·뺄 까닭 없음) 안 하루 조회수 상위 {TOP_PCT}% — **주마다 따로** 잡음 "
         "(`analysis.md` 1-3번의 한 경계는 막 올라온 영상이 거의 다 차지함). 칸 모집단이 "
         f"{MIN_CELL_POOL}개 미만이면 잡지 않음. 자료(댓글)를 받은 것만 셈 — 받지 않은 수는 표의 '못 받음'.",
         "- **성공 사례** = `analysis.md` 1번 그대로 (구독자 5만 이하 · 조회수 ≥ 구독자×3 · 180일 · 4분). 둘 다인 영상은 두 묶음에 모두. "
         "**그 밖의 승인 영상** = 같은 칸에서 자료를 받았지만 두 묶음이 아닌 것 (비교용).",
         f"- **관심 많은 댓글** = 영상마다 좋아요 많은 시청자 댓글 {TOP_COMMENTS}개 (채널 주인·답글·도배 꼴·좋아요 {MIN_COMMENT_LIKES} 미만 뺌).",
         "- **메아리** = 그 댓글 중 제목(썸네일) 낱말이 하나라도 나온 비율. **우연** = 같은 댓글에 같은 나라 다른 영상(하루 조회수 큰 60개)의 "
         "제목(썸네일) 낱말이 나온 비율의 평균 — '주식·코스피'처럼 어디나 나오는 말 몫. **메아리 − 우연** 이 제목과 댓글이 이어진 정도.",
         "- **주제 갈래**는 한국어·영어 낱말 규칙(아래 4번 위)이라 거칠다. 한국 댓글 갈래(6번)는 `success_analysis` 의 한국어 규칙 그대로 — 미국 댓글엔 못 씀.",
         "- **썸네일 문구**는 `thumb_text.tsv` — 그림을 보고 옮겨 적은 것(읽은 이 칸 참고). 이 환경의 OCR(tesseract)은 꾸민 글자를 거의 못 읽어서 쓰지 않음.",
         "- 영상 수가 적은 칸(특히 3·4주 전·미국)은 숫자가 크게 흔들린다 — 영상 10개 미만 칸으로 규칙을 만들지 않는다. "
         "외국(미국) 사례의 제목·댓글 낱말 통계로 한국어 규칙을 만들지 않는다 (CLAUDE.md).",
         f"- 나라를 정하지 못해 뺀 검색 영상: {', '.join(f'{k} {v:,}' for k, v in data['unknown_country'].items()) or '없음'}.", "",
         "## 1. 한눈에 — 칸마다 묶음별", "",
         "| 나라 | 주 | 묶음 | 영상 | 댓글 | 썸네일 문구 | 제목 메아리 | 우연 | 차이 | 썸네일 메아리 | 우연 | 차이 | 제목에 숫자 | 제목이 ?로 끝남 | 칸 모집단·경계(하루 조회수)·못 받음 |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for c in data["cells"]:
        extra = (f"{c['pool']:,} · {n(c['threshold'])}회 이상 · {c['missing']}" if c["group"] == GROUPS[0] and c["threshold"] is not None
                 else (f"{c['pool']:,} · 모집단 적음" if c["group"] == GROUPS[0] else ""))
        L.append(f"| {c['country']} | {c['week']} | {c['group']} | {c['videos']} | {c['comments']:,} | {c['thumb_text']} | {pct(c['echo_title'])} | "
                 f"{pct(c['base_title'])} | {pp(c['echo_title'], c['base_title'])} | {pct(c['echo_thumb'])} | {pct(c['base_thumb'])} | "
                 f"{pp(c['echo_thumb'], c['base_thumb'])} | {pct(c['title_num'])} | {pct(c['title_q'])} | {extra} |")
    L += ["", "## 2. 주제 갈래 — 제목·썸네일에 그 갈래가 있을 때 vs 없을 때, 관심 많은 댓글이 그 갈래를 말한 비율 (잘 나온 + 성공 사례, 4주 합침)", "",
          "| 나라 | 갈래 | 제목·썸네일에 있는 영상 | 그 댓글이 말한 비율 | 없는 영상 | 그 댓글이 말한 비율 | 차이 |", "|---|---|---|---|---|---|---|"]
    for cc in COUNTRIES:
        for name, r in data["themes"][f"{cc}|0"].items():
            L.append(f"| {cc} | {name} | {r['with_n']} | {pct(r['with_share'])} | {r['without_n']} | {pct(r['without_share'])} | {pp(r['with_share'], r['without_share'])} |")
    L += ["", "### 2-1. 주마다 — 제목·썸네일에 그 갈래가 든 영상 비율 / 그때 댓글이 말한 비율 (없을 때 비율)", ""]
    names = [k for k in THEMES if k != "질문(?로 끝남)"]
    for cc in COUNTRIES:
        L += [f"**{cc}**", "", "| 갈래 | " + " | ".join(week_label(wk, now) for wk in range(1, WEEKS + 1)) + " |",
              "|---|" + "---|" * WEEKS]
        for name in names:
            cells_txt = []
            for wk in range(1, WEEKS + 1):
                r = data["themes"][f"{cc}|{wk}"][name]
                cells_txt.append(f"{pct(r['title_share'])} · {pct(r['with_share'])} ({pct(r['without_share'])})" if r["with_n"] or r["without_n"] else "-")
            L.append(f"| {name} | " + " | ".join(cells_txt) + " |")
        L.append("")
    L += ["## 3. 낱말 — 댓글이 가장 따라 한 제목·썸네일 낱말 (잘 나온 + 성공 사례, 영상 2개 이상에 쓴 낱말)", "",
          "자기 댓글 = 그 낱말을 제목·썸네일에 쓴 영상의 관심 많은 댓글 중 그 낱말이 나온 비율. 다른 영상 = 같은 나라에서 그 낱말을 안 쓴 영상의 댓글 중 나온 비율.", ""]
    for cc in COUNTRIES:
        for wk in range(1, WEEKS + 1):
            ws = data["words"].get(f"{cc}|{wk}") or []
            L += [f"**{cc} · {week_label(wk, now)}**", ""]
            if not ws:
                L += ["(영상 2개 이상에 쓴 낱말 없음)", ""]
                continue
            L += ["| 낱말 | 어디 | 영상 | 자기 댓글 | 다른 영상 댓글 | 차이 |", "|---|---|---|---|---|---|"]
            for x in ws:
                L.append(f"| {x['word']} | {x['where']} | {x['videos']} | {pct(x['own'])} | {pct(x['base'])} | {pp(x['own'], x['base'])} |")
            L.append("")
    L += ["## 4. 사례 — 칸마다 제목 메아리(메아리 − 우연)가 큰 영상과 좋아요 많은 댓글 3개", ""]
    for cc in COUNTRIES:
        for wk in range(1, WEEKS + 1):
            ex = data["examples"].get(f"{cc}|{wk}") or []
            if not ex:
                continue
            L += [f"**{cc} · {week_label(wk, now)}**", ""]
            for e in ex:
                L.append(f"- [{cell_txt(e['title'], 90)}](https://www.youtube.com/watch?v={e['id']}) — {cell_txt(e['channel'], 24)} · 구독자 {n(e['subs'])} · "
                         f"조회수 {n(e['views'])} · 하루 {n(e['vpd'])}{' · 성공 사례' if e['success'] else ''} · 제목 메아리 {pct(e['echo_title'])} (우연 {pct(e['base_title'])})"
                         + (f" · 썸네일 「{cell_txt(e['thumb_text'], 60)}」 메아리 {pct(e['echo_thumb'])}" if e["thumb_text"] else " · 썸네일 문구 없음·안 읽음"))
                for m in e["comments"]:
                    L.append(f"  - 👍{m['likes']:,} “{cell_txt(m['text'], 150)}”")
            L.append("")
    L += ["## 5. 한국 — 관심 많은 댓글의 갈래 (`success_analysis` 한국어 규칙, 한 댓글이 여러 갈래에 들 수 있음)", "",
          "| 주 | 묶음 | 댓글 | " + " | ".join(k.split(" (")[0] for k in sa.NEED_CATS) + " |", "|---|---|---|" + "---|" * len(sa.NEED_CATS)]
    for wk in range(1, WEEKS + 1):
        for g in GROUPS:
            r = data["kr_needs"][f"{wk}|{g}"]
            L.append(f"| {wk} | {g} | {r['comments']:,} | " + " | ".join(pct(r[k]) for k in sa.NEED_CATS) + " |")
    L += ["", "## 6. 자료를 받지 않은 '조회수 잘 나온 영상' (승인하면 들어감)", ""]
    for key, xs in data["missing"].items():
        if xs:
            L.append(f"- {key.replace('|', ' · ')}주 전: " + " · ".join(f"[{cell_txt(x['title'], 40)}](https://www.youtube.com/watch?v={x['id']}) (하루 {n(x['vpd'])})" for x in xs[:8])
                     + (f" … 모두 {len(xs)}개" if len(xs) > 8 else ""))
    if not any(data["missing"].values()):
        L.append("없음")
    (out / "title_comment.md").write_text("\n".join(L) + "\n", "utf-8")


def main(argv=None):
    ap = argparse.ArgumentParser(description="제목·썸네일 문구 vs 관심 많은 댓글 — 나라 × 주 (할당량: countries 만)")
    ap.add_argument("topic")
    ap.add_argument("cmd", choices=["countries", "targets", "report"])
    ap.add_argument("--sheet-dir", default=str(ROOT / ".yt_work" / "thumb_sheets"), help="targets: 썸네일 모음 그림을 둘 곳")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args(argv)
    setup_logging(a.log_level)
    now = datetime.now(timezone.utc)
    log("START", topic=a.topic, cmd=a.cmd, tool=f"title_comment_link.py {VERSION}")
    if a.cmd == "countries":
        res = cmd_countries(a.topic, now)
    elif a.cmd == "targets":
        res = cmd_targets(a.topic, now, a.sheet_dir)
    else:
        d = cmd_report(a.topic, now)
        res = {"cells": len(d["cells"])}
    log("DONE", **{k: v for k, v in res.items()})


if __name__ == "__main__":
    main()
