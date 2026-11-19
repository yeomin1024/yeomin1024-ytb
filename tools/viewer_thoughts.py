#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-11-19 — 새로 (같은 날 classify 단계 더함 — 묶음 이름을 물려받은 댓글이 독립 확인 23% 만 맞아, 몫은 무작위 표본 2,400개를 직접 분류해 어림): 시청자 '공통 생각' 순위 (사용자 지시 2026-11-19 "페르소나를 만드는 목적은 시청자들이 원하는 공통적인
#          생각들을 정리하기 위해서야 그러니까 일단 누락없이 모든 댓글을 참고해야해 댓글들을 통해 가장 겹치는 생각들을 많은 순으로 정리해봐 나이나
#          처한 상황(어떤 주식에 물려있다)과 같은 여러가지 부가적인 정보는 정리만해").
#          · 자료: 승인한 영상 폴더(W_·01_·P01_) 전부의 시청자 댓글 전부 (날짜·언어로 거르지 않음 — 채널 주인 댓글·빈 댓글만 뺌, 답글 포함).
#            personas.py 는 '올린 지 180일 · 한국어 · 나이나 생애 단계를 밝힌 댓글'만 묶어 530개(0.3%)만 썼다 → 이 도구는 모든 댓글에 생각 하나.
#          · 묶기: 언어 묶음(한국어 영상·영어 영상·그 밖) × 댓글 유형(comment_types — 질문·경험·의견·칭찬·비판·정치 …)마다
#            comment_clusters.cluster_lang (Kiwi 낱말 → TF-IDF → SVD → MiniBatchKMeans, 씨앗 고정) → 작은 묶음 수백 개.
#          · 이름 붙이기: 묶음마다 표본 10개(한가운데 4 · 무작위 4 · 좋아요 2)를 Claude(하위 에이전트)가 읽고 '시청자의 생각' 한 문장 + 맞는 표본 수
#            (labels/*.tsv) → 같은 생각끼리 하나로(canon.tsv) → 댓글 수 많은 순.
#          · 부가 정보(정리만): 밝힌 나이 · 생애 단계 · 처지(personas.toml 의 state) · 지식 수준 · 말한 종목 · 물린 종목(종목 이름 옆에 물렸·손실·평단…)
#            — 전체 표 + 생각마다 많은 것 몇 개. 묶는 기준으로는 쓰지 않음.
#          할당량 0. ※ 연구·교육용 — 투자 권유가 아님.
"""시청자 공통 생각 — 모든 댓글을 생각별로 묶어 많은 순으로

  python3 tools/viewer_thoughts.py stock build          # 묶기 → .yt_work/thoughts/stock/rows.jsonl.gz · <주제>/result/outliers/thoughts/clusters.json · label_todo/*.md
  (하위 에이전트가 label_todo/<묶음>.md 를 읽고 labels/<묶음>.tsv 를 씀 → Claude 가 canon.tsv 로 같은 생각을 합침)
  python3 tools/viewer_thoughts.py stock report         # labels + canon → <주제>/result/outliers/viewer_thoughts.md · .json
"""
import argparse
import gzip
import json
import logging
import random
import re
import sys
import time
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comment_clusters as cc          # noqa: E402  cluster_lang (같은 묶기)
import comment_types as ct             # noqa: E402  iter_videos · lang_group · classify · TYPES
import personas as ps                  # noqa: E402  cues (나이·생애 단계·처지·지식) — 부가 정보만

VERSION = "v1.0"
ROOT = Path(__file__).resolve().parent.parent
LOG = logging.getLogger("vthought")
SEED = 20261119
K_TOTAL = {"한국어": 300, "영어": 110, "그 밖 언어": 35}     # 언어마다 작은 묶음 수 (유형마다 댓글 몫대로 나눔)
SPLIT = 0.2                      # 한 묶음이 그 (언어 × 유형) 댓글의 이 몫을 넘을 때만 다시 나눔 (0.03 이면 유형마다 50개 넘는 묶음을 다 나눠 2,033개가 됨)
SAMPLE = {"center": 4, "random": 4, "liked": 2}
SAMPLE_CHARS = 160
BATCH = {"한국어": 45, "영어": 60, "그 밖 언어": 40}       # 하위 에이전트 한 명이 읽는 묶음 수

# 종목 사전 (부가 정보 — 말한 종목·물린 종목). 이름 → 정규식. 한국어 댓글에서 자주 쓰는 줄임말 포함.
STOCKS = {
    "삼성전자": r"삼성\s?전자|삼전(?![가-힣]{0,1}(?:자|략|체))|삼성\s?(?:주식|주)",
    "SK하이닉스": r"(?:sk\s?)?하이닉스|(?<![가-힣])닉스(?![가-힣])|삼닉|삼전닉스",
    "현대차": r"현대\s?차|현대\s?자동차", "기아": r"(?<![가-힣])기아(?:차)?(?![가-힣])",
    "LG에너지솔루션": r"엔솔|lg\s?에너지|엘지\s?에너지", "에코프로": r"에코프로", "셀트리온": r"셀트리온",
    "카카오": r"카카오(?!톡|뱅크)|(?<![가-힣])카카오뱅크", "네이버": r"네이버", "한화에어로스페이스": r"한화\s?에어로",
    "두산에너빌리티": r"두산\s?에너빌|두에빌", "삼성바이오로직스": r"삼성\s?바이오|삼바(?![가-힣])", "포스코": r"포스코",
    "한미반도체": r"한미\s?반도체", "알테오젠": r"알테오젠", "HD현대·조선주": r"hd\s?현대|현대\s?중공업|한화\s?오션|조선주",
    "방산주": r"방산주|lig\s?넥스원|현대\s?로템", "2차전지": r"2\s?차\s?전지|이차\s?전지",
    "테슬라": r"테슬라|tesla|tsla", "엔비디아": r"엔비디아|엔비|nvidia|nvda", "애플": r"(?<![가-힣])애플|apple|aapl",
    "마이크로소프트": r"마이크로소프트|마소(?![가-힣])|msft", "구글·알파벳": r"구글|알파벳|googl?", "아마존": r"아마존|amazon|amzn",
    "메타": r"(?<![가-힣a-z])메타(?![버포인])|(?<![a-z])meta(?![a-z])", "팔란티어": r"팔란티어|pltr", "브로드컴": r"브로드컴|avgo",
    "AMD": r"(?<![a-z])amd(?![a-z])", "인텔": r"인텔|intel", "마이크론": r"마이크론|micron", "아이온큐": r"아이온큐|ionq",
    "넷플릭스": r"넷플릭스|nflx", "코인베이스": r"코인베이스",
    "QQQ·나스닥100 ETF": r"(?<![a-z])qqqm?(?![a-z])|나스닥\s?100", "S&P 500 ETF": r"(?<![a-z])(?:spy|voo|ivv|splg)(?![a-z])|s&p\s?500|에스앤피",
    "SCHD": r"schd|슈드", "JEPI·JEPQ": r"jepi|jepq", "TQQQ": r"tqqq", "SOXL": r"soxl", "QLD·SSO": r"(?<![a-z])(?:qld|sso)(?![a-z])",
    "커버드콜 ETF": r"커버드\s?콜", "비트코인": r"비트\s?코인|비코(?![가-힣])|bitcoin|btc", "금": r"(?<![가-힣])금\s?(?:etf|투자|사|값|시세)|골드",
}
LOSS = re.compile(r"물렸|물려\s?(?:있|서|요)|물린|손실\s?(?:중|이|봤|입|이에)|손해\s?(?:봤|보고|중)|마이너스|평단|반토막|-\s?\d{1,2}\s?%|파란\s?불|"
                  r"손절|구조대|탈출|본전|원금\s?(?:회복|손실)", re.I)
STOCK_RX = {k: re.compile(v, re.I) for k, v in STOCKS.items()}


def log(stage, level=logging.INFO, **kv):
    LOG.log(level, "[%s] [%s] %s", stage, datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            " ".join(f"{k}={v}" for k, v in kv.items()))


def one_line(t, n=SAMPLE_CHARS):
    t = re.sub(r"\s+", " ", str(t)).strip()
    return t if len(t) <= n else t[: n - 1] + "…"


SELF_KO = re.compile(ps.SELF["ko"], re.I)


def stocks_of(text, typ=None):
    """말한 종목 · 물림 이야기에 나온 종목(종목 이름 앞뒤 25자 안에 물렸·손실·평단·반토막 …) · 내가 물린 종목(그중 그 손실 낱말 앞 30자·뒤 20자에
    저는·제가… 가 있거나, 100자 이하 경험·질문 댓글). v1.0 표본 감사(12개): 이름 옆 손실 낱말만으로는 '개미들이 다 물려 있다'·'물린 분들 위로송' 같은
    남 이야기가 섞여 자기 이야기는 3개쯤 → '내가 물린'은 자기 단서를 더 요구."""
    said, talk, mine = [], [], []
    short_self = typ in ("E", "Q") and len(text) <= 100
    for k, r in STOCK_RX.items():
        for m in r.finditer(text):
            if k not in said:
                said.append(k)
            w0, w1 = max(0, m.start() - 25), m.end() + 25
            lm = LOSS.search(text, w0, w1)
            if not lm:
                continue
            if k not in talk:
                talk.append(k)
            if k not in mine and (short_self or SELF_KO.search(text[max(0, lm.start() - 30): lm.end() + 20])):
                mine.append(k)
    return said, talk, mine


def paths(topic):
    out = ROOT / topic / "result" / "outliers"
    return {"out": out, "dir": out / "thoughts", "todo": out / "thoughts" / "label_todo", "labels": out / "thoughts" / "labels",
            "canon": out / "thoughts" / "canon.tsv", "clusters": out / "thoughts" / "clusters.json",
            "work": ROOT / ".yt_work" / "thoughts" / topic, "md": out / "viewer_thoughts.md", "json": out / "viewer_thoughts.json"}


# ---------------------------------------------------------------- 묶기
def load_rows(topic):
    P = paths(topic)
    an = json.loads((P["out"] / "analysis.json").read_text("utf-8")) if (P["out"] / "analysis.json").is_file() else {}
    succ = {c["id"] for c in an.get("success_cases") or []}
    vpd = {c["id"] for c in (an.get("vpd_top") or {}).get("cases") or []}
    rows, vids = [], {}
    for d, meta, info, cms in ct.iter_videos(P["out"]):
        vid = meta.get("id")
        lg = ct.lang_group(meta, info)
        vids[vid] = {"title": meta.get("title") or "", "channel": meta.get("channel") or "", "lang": lg,
                     "group": "성공 사례" if vid in succ else ("하루 조회수 상위" if vid in vpd else "그 밖의 승인 영상"),
                     "published": (meta.get("published_at") or meta.get("published") or "")[:10]}
        for m in cms:
            if m["creator"] or not cc.ZW.sub("", m["text"]).strip():
                continue
            rows.append({"vid": vid, "cid": m["cid"], "text": m["text"], "likes": m["likes"], "reply": m["reply"], "lang": lg,
                         "published": (m.get("published") or "")[:10]})
    log("LOAD", topic=topic, videos=len(vids), comments=len(rows), by_lang=dict(Counter(r["lang"] for r in rows)),
        replies=sum(r["reply"] for r in rows), note="승인 영상 전부 · 날짜·언어로 거르지 않음 · 채널 주인·빈 댓글만 뺌")
    return rows, vids


def features(rows, topic):
    """유형(모든 댓글) + 부가 정보 (한국어: 나이·생애 단계·처지·지식 — personas.cues · 모든 언어: 종목)."""
    t0 = time.time()
    cfg, _ = ps.load_cfg(topic)
    C = ps.compile_cfg(cfg) if cfg else {}
    now = datetime.now(timezone.utc)
    for r in rows:
        r["type"] = ct.classify(r["text"])
        r["stocks"], r["stuck_talk"], r["stuck"] = stocks_of(r["text"], r["type"])
        if r["lang"] == "한국어" and "한국어" in C:
            c = ps.cues(r["text"], C["한국어"], now)
            r["age"] = c["age"]
            r["stage"] = ps.stage_of(c, cfg)
            r["states"] = c["states"]
            r["know"] = c["know"]
        else:
            r["age"] = r["stage"] = r["know"] = None
            r["states"] = []
    log("FEATURES", comments=len(rows), types=dict(Counter(r["type"] for r in rows).most_common()), with_age=sum(r["age"] is not None for r in rows),
        with_stage=sum(bool(r["stage"]) for r in rows), with_state=sum(bool(r["states"]) for r in rows), with_stock=sum(bool(r["stocks"]) for r in rows),
        with_stuck_talk=sum(bool(r["stuck_talk"]) for r in rows), with_stuck_self=sum(bool(r["stuck"]) for r in rows), seconds=round(time.time() - t0, 1))


def build(topic, k_total=None):
    k_total = k_total or K_TOTAL
    P = paths(topic)
    rows, vids = load_rows(topic)
    features(rows, topic)
    rng = random.Random(SEED)
    clusters = []
    for lang in ("한국어", "영어", "그 밖 언어"):
        L = [i for i, r in enumerate(rows) if r["lang"] == lang]
        if not L:
            continue
        by_type = defaultdict(list)
        for i in L:
            by_type[rows[i]["type"]].append(i)
        for typ, idx in sorted(by_type.items(), key=lambda x: -len(x[1])):
            k = max(2, round(k_total[lang] * len(idx) / len(L)))
            sub = [rows[i] for i in idx]
            labels, sim, info = cc.cluster_lang(lang, sub, k, SPLIT, seed=SEED)
            groups = defaultdict(list)
            for j, lab in enumerate(labels):
                groups[int(lab)].append(j)
            for lab, js in sorted(groups.items()):
                cid = f"{ {'한국어': 'KO', '영어': 'EN', '그 밖 언어': 'OT'}[lang]}-{typ}-{lab:03d}"
                for j in js:
                    rows[idx[j]]["cluster"] = cid
                    rows[idx[j]]["sim"] = round(float(sim[j]), 4)
                central = sorted(js, key=lambda j: -sim[j])[: SAMPLE["center"]]
                rest = [j for j in js if j not in central]
                rnd = rng.sample(rest, min(SAMPLE["random"], len(rest)))
                liked = [j for j in sorted(js, key=lambda j: -sub[j]["likes"]) if j not in central and j not in rnd][: SAMPLE["liked"]]
                samp = [{"why": w, "likes": sub[j]["likes"], "text": one_line(sub[j]["text"])} for w, grp in (("가운데", central), ("무작위", rnd), ("좋아요", liked)) for j in grp]
                clusters.append({"id": cid, "lang": lang, "type": typ, "type_name": ct.type_name(typ), "n": len(js),
                                 "likes": int(sum(sub[j]["likes"] for j in js)), "videos": len({sub[j]["vid"] for j in js}),
                                 "terms": (info.get(lab) or {}).get("terms") or [], "samples": samp})
            log("TYPE", lang=lang, type=typ, comments=len(idx), k=k, clusters=len(groups))
    P["work"].mkdir(parents=True, exist_ok=True)
    with gzip.open(P["work"] / "rows.jsonl.gz", "wt", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps({k: r.get(k) for k in ("vid", "cid", "text", "likes", "reply", "lang", "published", "type", "cluster", "sim", "stocks", "stuck_talk", "stuck",
                                                      "age", "stage", "states", "know")}, ensure_ascii=False) + "\n")
    (P["work"] / "videos.json").write_text(json.dumps(vids, ensure_ascii=False), "utf-8")
    P["dir"].mkdir(parents=True, exist_ok=True)
    meta = {"topic": topic, "tool": f"viewer_thoughts.py {VERSION}", "made": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "seed": SEED,
            "k_total": k_total, "split": SPLIT, "comments": len(rows), "videos": len(vids), "clusters": clusters}
    P["clusters"].write_text(json.dumps(meta, ensure_ascii=False, indent=1), "utf-8")
    write_todo(topic, clusters)
    log("BUILD", comments=len(rows), clusters=len(clusters), work=P["work"] / "rows.jsonl.gz", clusters_file=P["clusters"])


TODO_HEAD = """# 댓글 묶음에 '시청자의 생각' 이름 붙이기 — {batch} ({n}묶음)

너는 처음 이 글을 보는 검토자다. 아래는 주식 유튜브 영상들의 시청자 댓글을 낱말이 비슷한 것끼리 기계로 묶은 작은 묶음들이다.
묶음마다 표본 댓글 최대 10개(가운데 4 · 무작위 4 · 좋아요 2)가 있다. 표본을 다 읽고, 그 묶음 댓글들이 **공통으로 말하는 시청자의 생각**을 정한다.

규칙
- 생각 = 시청자 입장의 한 문장 (예: "지금 팔아야 할지 버텨야 할지 모르겠다" · "장기 적립이 결국 이긴다" · "정부·금융당국이 개미를 지키지 않는다" ·
  "커버드콜 ETF가 괜찮은지 알고 싶다" · "영상이 쉽고 도움이 됐다"). 낱말 나열이나 '○○에 대한 댓글' ✗ — 무엇을 생각·원하는지.
- 묶음 번호가 정한 유형(질문·경험·의견…)은 기계가 붙인 것이라 틀릴 수 있다 — 표본이 실제로 말하는 것으로 정한다.
- 표본 10개 중 그 생각과 맞는 것이 몇 개인지 `맞음` 칸에 숫자로. 생각이 둘로 갈리면 많은 쪽을 쓰고 `메모`에 다른 쪽을 적는다 (예: "반대: 3개는 '지금이 기회'").
- 내용이 거의 없으면(이모지·ㅋㅋ·출석) "반응만 (뜻 없음)" · 광고·도배면 "광고·도배" · 다른 언어면 한국어로 옮겨 쓴다.
- 갈래(하나 고름): 질문·궁금증 / 투자 원칙·교훈 / 시장·종목 전망 / 내 경험·처지 / 불안·후회·고통 / 정부·제도·정치 / 영상·출연자 칭찬 / 영상·출연자 비판 / 정보·요약 보충 / 반응·농담 / 광고·도배
- 다른 파일은 읽지 않는다. 답은 아래 꼴의 TSV 로 `{out}` 에 저장한다 (머리줄 그대로, 묶음마다 한 줄, 탭으로 나눔, 칸 안에 탭·줄바꿈 ✗):

```
묶음\t생각\t갈래\t맞음\t메모
```

"""


def write_todo(topic, clusters):
    P = paths(topic)
    P["todo"].mkdir(parents=True, exist_ok=True)
    P["labels"].mkdir(parents=True, exist_ok=True)
    for f in P["todo"].glob("*.md"):
        f.unlink()
    n_files = 0
    for lang, code in (("한국어", "KO"), ("영어", "EN"), ("그 밖 언어", "OT")):
        L = [c for c in clusters if c["lang"] == lang]
        for b in range(0, len(L), BATCH[lang]):
            part = L[b: b + BATCH[lang]]
            name = f"{code}_{b // BATCH[lang] + 1:02d}"
            out = P["labels"] / f"{name}.tsv"
            lines = [TODO_HEAD.format(batch=name, n=len(part), out=out.relative_to(ROOT))]
            for c in part:
                lines.append(f"## {c['id']} — 기계 유형 {c['type_name']} · 댓글 {c['n']:,}개 · 좋아요 {c['likes']:,} · 많은 낱말 {', '.join(c['terms'][:6]) or '-'}")
                for s in c["samples"]:
                    lines.append(f"- ({s['why']} 👍{s['likes']}) {s['text']}")
                lines.append("")
            (P["todo"] / f"{name}.md").write_text("\n".join(lines), "utf-8")
            n_files += 1
    log("TODO", files=n_files, dir=P["todo"])


# ---------------------------------------------------------------- 보고
def read_tsv(p):
    out = []
    for i, line in enumerate(Path(p).read_text("utf-8").splitlines()):
        if i == 0 or not line.strip():
            continue
        parts = line.split("\t")
        out.append(parts + [""] * (5 - len(parts)))
    return out


def report(topic):
    P = paths(topic)
    meta = json.loads(P["clusters"].read_text("utf-8"))
    cl = {c["id"]: c for c in meta["clusters"]}
    lab = {}
    for f in sorted(P["labels"].glob("*.tsv")):
        for cid, thought, kind, ok, memo in (r[:5] for r in read_tsv(f)):
            cid = cid.strip()
            if cid in cl:
                try:
                    okn = max(0, min(int(re.sub(r"[^\d]", "", ok) or 0), len(cl[cid]["samples"])))
                except ValueError:
                    okn = 0
                lab[cid] = {"thought": thought.strip(), "kind": kind.strip(), "ok": okn, "memo": memo.strip()}
    missing = [c for c in cl if c not in lab]
    canon = {}
    if P["canon"].is_file():
        for r in read_tsv(P["canon"]):
            canon[r[0].strip()] = {"key": r[1].strip(), "thought": r[2].strip(), "kind": r[3].strip()}
    rows = [json.loads(l) for l in gzip.open(P["work"] / "rows.jsonl.gz", "rt", encoding="utf-8")]
    for r in rows:                      # 종목은 글에서 다시 셈 (stocks_of 를 고쳐도 build 를 다시 돌리지 않게 — 묶음은 종목을 쓰지 않음)
        r["stocks"], r["stuck_talk"], r["stuck"] = stocks_of(r["text"], r["type"])
    vids = json.loads((P["work"] / "videos.json").read_text("utf-8"))
    log("REPORT_IN", clusters=len(cl), labeled=len(lab), missing=len(missing), canon=len(canon), comments=len(rows))
    T = {}
    for r in rows:
        cid = r.get("cluster")
        c = canon.get(cid) or ({"key": lab[cid]["thought"], "thought": lab[cid]["thought"], "kind": lab[cid]["kind"]} if cid in lab else
                               {"key": "(이름 없음)", "thought": "(이름 안 붙은 묶음)", "kind": "-"})
        key = (r["lang"], c["key"])
        t = T.setdefault(key, {"lang": r["lang"], "key": c["key"], "thought": c["thought"], "kind": c["kind"], "n": 0, "likes": 0, "clusters": set(), "rows": []})
        t["n"] += 1
        t["likes"] += r["likes"]
        t["clusters"].add(cid)
        t["rows"].append(r)
    total = Counter(r["lang"] for r in rows)
    res = []
    for (lang, key), t in T.items():
        rs = t["rows"]
        # 맞음 몫 = 묶음 크기로 가중한 표본 맞음 비율 (그 생각에 든 댓글 중 정말 그 생각인 몫의 어림)
        okw = sum(cl[c]["n"] * (lab[c]["ok"] / max(1, len(cl[c]["samples"]))) for c in t["clusters"] if c in lab)
        nw = sum(cl[c]["n"] for c in t["clusters"] if c in lab)
        # 예시 댓글은 표본이 잘 맞은 묶음(맞음 7/10 이상 → 없으면 5 이상)의 한가운데 쪽 60% 안에서 — 섞인 묶음 가장자리의 딴 이야기가 뽑히지 않게
        pool = next((p for p in ([r for r in rs if lab.get(r.get("cluster"), {}).get("ok", 0) >= k] for k in (7, 5)) if p), rs)
        sims = sorted(r.get("sim") or 0 for r in pool)
        cut = sims[int(len(sims) * 0.4)] if sims else 0
        top_liked = sorted([r for r in pool if (r.get("sim") or 0) >= cut] or pool, key=lambda r: -r["likes"])[:3]
        central = sorted(pool, key=lambda r: -(r.get("sim") or 0))[:3]
        ages = Counter((r["age"] // 10) * 10 for r in rs if r.get("age"))
        est = okw + (t["n"] - nw)          # 이름 안 붙은 묶음은 그대로
        res.append({
            "lang": lang, "key": key, "thought": t["thought"], "kind": t["kind"], "n": t["n"], "share": t["n"] / total[lang], "likes": t["likes"],
            "est": round(est), "est_share": est / total[lang],
            "clusters": sorted(t["clusters"]), "precision": round(okw / nw, 2) if nw else None,
            "videos": len({r["vid"] for r in rs}), "types": Counter(ct.type_name(r["type"]) for r in rs).most_common(3),
            "ages": sorted(ages.items()), "age_n": sum(ages.values()),
            "stages": Counter(r["stage"] for r in rs if r.get("stage")).most_common(3),
            "states": Counter(s for r in rs for s in (r.get("states") or [])).most_common(3),
            "stocks": Counter(s for r in rs for s in r["stocks"]).most_common(5),
            "stuck": Counter(s for r in rs for s in r["stuck"]).most_common(5),
            "stuck_talk": Counter(s for r in rs for s in r["stuck_talk"]).most_common(5),
            "know": Counter(r["know"] for r in rs if r.get("know")).most_common(),
            "groups": Counter(vids.get(r["vid"], {}).get("group", "?") for r in rs).most_common(),
            "examples_central": [{"likes": r["likes"], "text": one_line(r["text"], 140)} for r in central],
            "examples_liked": [{"likes": r["likes"], "text": one_line(r["text"], 140)} for r in top_liked],
        })
    res.sort(key=lambda x: (x["lang"] != "한국어", x["lang"], -x["est"], -x["n"]))     # 순위 = 추정 댓글 수 (섞인 묶음을 덜 셈)
    V = verify_read(P)
    for x in res:
        v = V.get(x["key"])
        if v:
            n = sum(v.values())
            x["checked"] = {"n": n, "yes": v["맞음"], "part": v["부분"], "no": v["아님"], "yes_share": round(v["맞음"] / n, 2), "part_share": round(v["부분"] / n, 2)}
    side = side_info(rows)
    ko_rows = [r for r in rows if r["lang"] == "한국어"]
    SM = classify_read(P, ko_rows)
    sample = None
    if SM and SM["n"]:
        cl_by_key = {x["key"]: x for x in res if x["lang"] == "한국어"}
        for x in SM["rows"]:
            mem = x.pop("members")
            x["examples"] = [{"likes": r["likes"], "text": one_line(r["text"], 150)} for r in sorted(mem, key=lambda r: -r["likes"])[:3]]
            x["cluster_est"] = (cl_by_key.get(x["key"]) or {}).get("est")
            x["videos"] = len({r["vid"] for r in mem})
            x["stocks"] = Counter(s for r in mem for s in r["stocks"]).most_common(4)
            x["stuck"] = Counter(s for r in mem for s in r["stuck"]).most_common(3)
            x["states"] = Counter(s for r in mem for s in (r.get("states") or [])).most_common(3)
            x["ages"] = sorted(Counter((r["age"] // 10) * 10 for r in mem if r.get("age")).items())
            x["types"] = Counter(ct.type_name(r["type"]) for r in mem).most_common(2)
        sample = {"n": SM["n"], "planned": SM["planned"], "n_ko": SM["n_ko"], "rows": SM["rows"], "other_memos": SM["other_memos"]}
        log("SAMPLE", classified=SM["n"], planned=SM["planned"], k00=sum(x["k"] for x in SM["rows"] if x["code"] == "K00"),
            top=[(x["thought"][:24], x["k"]) for x in SM["rows"][:5]])
    D = {"sample": sample, "topic": topic, "tool": f"viewer_thoughts.py {VERSION}", "made": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
         "comments": len(rows), "by_lang": dict(total), "videos": len(vids), "clusters": len(cl), "labeled": len(lab), "missing": missing,
         "thoughts": res, "side": side}
    P["json"].write_text(json.dumps(D, ensure_ascii=False, indent=1, default=list), "utf-8")
    write_md(P["md"], D, stage_names(topic))
    log("REPORT", thoughts=len(res), md=P["md"], json=P["json"],
        top_ko=[(x["thought"][:30], x["n"]) for x in res if x["lang"] == "한국어"][:5])


VERIFY_N = 12          # 생각마다 무작위 댓글 수
VERIFY_TOP = 25        # 한국어 상위 몇 개 생각을 따로 확인하나 ('반응만' 은 뺌)


def verify_todo(topic):
    """독립 확인: 한국어 상위 생각마다 무작위 댓글 12개 → 새 검토자가 '그 생각인가' 맞음·부분·아님 (묶음 이름을 붙인 사람과 다른 사람)."""
    P = paths(topic)
    D = json.loads(P["json"].read_text("utf-8"))
    rows = [json.loads(l) for l in gzip.open(P["work"] / "rows.jsonl.gz", "rt", encoding="utf-8")]
    canon = {r[0].strip(): r[1].strip() for r in read_tsv(P["canon"])} if P["canon"].is_file() else {}
    by = defaultdict(list)
    for r in rows:
        if r["lang"] == "한국어":
            by[canon.get(r.get("cluster"), r.get("cluster"))].append(r)
    rng = random.Random(SEED + 1)
    ko = [t for t in D["thoughts"] if t["lang"] == "한국어" and not t["thought"].startswith("반응만")][:VERIFY_TOP]
    out = P["dir"] / "verify.tsv"
    L = ["# 독립 확인 — 댓글이 그 '생각'을 말하는가", "",
         "너는 처음 이 글을 보는 검토자다. 아래 생각마다 무작위로 뽑은 주식 유튜브 시청자 댓글 12개가 있다.",
         "댓글마다 그 생각을 말하는지 판정한다: **맞음**(그 생각이 댓글의 주된 내용) · **부분**(그 생각과 닿지만 주된 내용은 아님) · **아님**(다른 이야기).",
         f"다른 파일은 읽지 않는다. 답은 TSV 로 `{out.relative_to(ROOT)}` 에 저장 (머리줄 `생각\t댓글\t판정`, 줄마다 생각 번호·댓글 번호·판정 — 모든 댓글 빠짐없이).", ""]
    for i, t in enumerate(ko, 1):
        rs = by.get(t["key"]) or []
        samp = rng.sample(rs, min(VERIFY_N, len(rs)))
        L.append(f"## T{i:02d} — {t['thought']}")
        for j, r in enumerate(samp, 1):
            L.append(f"- C{j:02d}: {one_line(r['text'], 200)}")
        L.append("")
    (P["dir"] / "verify_todo.md").write_text("\n".join(L), "utf-8")
    meta = [{"t": f"T{i:02d}", "key": t["key"]} for i, t in enumerate(ko, 1)]
    (P["dir"] / "verify_keys.json").write_text(json.dumps(meta, ensure_ascii=False, indent=1), "utf-8")
    log("VERIFY_TODO", thoughts=len(ko), per_thought=VERIFY_N, file=P["dir"] / "verify_todo.md", answer=out)


def verify_read(P):
    """verify.tsv → 생각 키마다 (맞음, 부분, 아님)."""
    f, k = P["dir"] / "verify.tsv", P["dir"] / "verify_keys.json"
    if not (f.is_file() and k.is_file()):
        return {}
    keys = {m["t"]: m["key"] for m in json.loads(k.read_text("utf-8"))}
    res = defaultdict(Counter)
    for r in read_tsv(f):
        t, verdict = r[0].strip(), r[2].strip()
        if t in keys:
            res[keys[t]]["맞음" if verdict.startswith("맞") else ("부분" if verdict.startswith("부") else "아님")] += 1
    return res


CLASSIFY_N = 2400       # 한국어 댓글 무작위 표본 (모든 한국어 댓글에서 고르게)
CLASSIFY_BATCH = 300


def thought_list(topic, lang="한국어"):
    """canon.tsv 의 생각 목록 (그 언어) → [(번호, 키, 생각, 갈래)]."""
    P = paths(topic)
    seen, out = set(), []
    pre = {"한국어": "KO", "영어": "EN", "그 밖 언어": "OT"}[lang]
    for r in read_tsv(P["canon"]):
        cid, key, th, kind = (x.strip() for x in r[:4])
        if cid.startswith(pre) and key not in seen:
            seen.add(key)
            out.append((key, th, kind))
    out.sort(key=lambda x: (x[2], x[1]))
    return [(f"K{i:02d}", k, t, g) for i, (k, t, g) in enumerate(out, 1)]


def classify_todo(topic):
    """정확한 몫: 한국어 댓글 전체에서 무작위 CLASSIFY_N 개 → 새 검토자가 댓글마다 생각 목록에서 직접 고름 (묶음을 거치지 않음).
    v1.0 독립 확인에서 '묶음 이름을 물려받은 댓글' 이 그 생각과 맞는 게 무작위 300개 중 69개(23%) · 부분 80개뿐이라 — 묶음은 생각 목록을 찾는 데만 쓰고
    몫은 무작위 표본으로 어림 (95% 범위와 함께)."""
    P = paths(topic)
    rows = [json.loads(l) for l in gzip.open(P["work"] / "rows.jsonl.gz", "rt", encoding="utf-8")]
    ko = [r for r in rows if r["lang"] == "한국어"]
    rng = random.Random(SEED + 2)
    samp = rng.sample(range(len(ko)), min(CLASSIFY_N, len(ko)))
    TL = thought_list(topic)
    d = P["dir"] / "classify_todo"
    d.mkdir(parents=True, exist_ok=True)
    (P["dir"] / "classify").mkdir(parents=True, exist_ok=True)
    for f in d.glob("*.md"):
        f.unlink()
    lst = "\n".join(f"- {k}: {t} ({g})" for k, _, t, g in TL)
    keys = []
    for b in range(0, len(samp), CLASSIFY_BATCH):
        part = samp[b: b + CLASSIFY_BATCH]
        name = f"C{b // CLASSIFY_BATCH + 1:02d}"
        out = P["dir"] / "classify" / f"{name}.tsv"
        L = [f"# 댓글마다 시청자의 생각 고르기 — {name} (댓글 {len(part)}개)", "",
             "너는 처음 이 글을 보는 검토자다. 아래 주식 유튜브 시청자 댓글마다, 그 댓글이 **주로 말하는 생각**을 생각 목록에서 하나 고른다.",
             "- 생각이 둘이면 `생각2` 칸에 하나 더 (없으면 비움). 목록에 맞는 게 없으면 `K00` 을 쓰고 `메모`에 그 생각을 한 문장으로 짧게.",
             "- 이모지·ㅋㅋ·출석·짧은 맞장구처럼 뜻이 거의 없으면 '반응만' 번호. 답글(@이름…)은 그 답글이 말하는 생각으로.",
             f"- 다른 파일은 읽지 않는다. 답은 TSV 로 `{out.relative_to(ROOT)}` 에 저장 — 머리줄 `댓글\t생각1\t생각2\t메모`, 댓글마다 한 줄, 빠짐없이.", "",
             "## 생각 목록", "", lst, "- K00: 목록에 없음 (메모에 한 문장)", "", "## 댓글", ""]
        for j, i in enumerate(part, 1):
            cid = f"{name}-{j:03d}"
            keys.append({"id": cid, "row": i, "cid": ko[i]["cid"]})
            L.append(f"- {cid}: {one_line(ko[i]['text'], 220)}")
        (d / f"{name}.md").write_text("\n".join(L), "utf-8")
    (P["dir"] / "classify_keys.json").write_text(json.dumps({"thoughts": TL, "keys": keys, "n_ko": len(ko), "seed": SEED + 2}, ensure_ascii=False), "utf-8")
    log("CLASSIFY_TODO", sample=len(samp), of=len(ko), files=len(list(d.glob('*.md'))), thoughts=len(TL), dir=d)


def wilson(k, n, z=1.96):
    if not n:
        return (0.0, 0.0)
    p = k / n
    den = 1 + z * z / n
    c = (p + z * z / (2 * n)) / den
    h = z * ((p * (1 - p) / n + z * z / (4 * n * n)) ** 0.5) / den
    return (max(0.0, c - h), min(1.0, c + h))


def classify_read(P, rows_ko):
    """classify/*.tsv → 생각 키마다 표본 수·몫·95% 범위 + 그 표본 댓글."""
    kf = P["dir"] / "classify_keys.json"
    if not kf.is_file():
        return None
    K = json.loads(kf.read_text("utf-8"))
    code2key = {k: key for k, key, t, g in K["thoughts"]}
    meta = {k: (t, g) for k, key, t, g in K["thoughts"]}
    idmap = {x["id"]: x["row"] for x in K["keys"]}
    got, prim, sec, other = {}, Counter(), Counter(), []
    for f in sorted((P["dir"] / "classify").glob("*.tsv")):
        for r in read_tsv(f):
            cid = r[0].strip()
            if cid not in idmap:
                continue
            c1 = re.sub(r"[^K0-9]", "", r[1].strip().upper())[:3]
            c2 = re.sub(r"[^K0-9]", "", r[2].strip().upper())[:3]
            got[cid] = (c1, c2, r[3].strip())
    n = len(got)
    members = defaultdict(list)
    for cid, (c1, c2, memo) in got.items():
        prim[c1] += 1
        members[c1].append(rows_ko[idmap[cid]])
        if c2 and c2 != c1:
            sec[c2] += 1
        if c1 == "K00":
            other.append(memo)
    res = []
    for code in list(meta) + ["K00"]:
        k = prim.get(code, 0)
        lo, hi = wilson(k, n)
        t, g = meta.get(code, ("목록에 없음 (메모)", "-"))
        res.append({"code": code, "key": code2key.get(code, "K00"), "thought": t, "kind": g, "k": k, "share": k / n if n else 0, "lo": lo, "hi": hi,
                    "also": sec.get(code, 0), "est": round(k / n * K["n_ko"]) if n else 0, "members": members.get(code, [])})
    res.sort(key=lambda x: -x["k"])
    return {"n": n, "planned": len(idmap), "n_ko": K["n_ko"], "rows": res, "other_memos": other}


def stage_names(topic):
    cfg, _ = ps.load_cfg(topic)
    if not cfg:
        return {}, {}
    return {s["key"]: s["name"] for s in cfg["stages"]}, {s["key"]: s["name"] for s in cfg["states"]}


def side_info(rows):
    ko = [r for r in rows if r["lang"] == "한국어"]
    ages = Counter((r["age"] // 10) * 10 for r in ko if r.get("age"))
    return {"ko_comments": len(ko), "age_n": sum(ages.values()), "ages": sorted(ages.items()),
            "stages": Counter(r["stage"] for r in ko if r.get("stage")).most_common(),
            "states": Counter(s for r in ko for s in (r.get("states") or [])).most_common(),
            "know": Counter(r["know"] for r in ko if r.get("know")).most_common(),
            "stocks": Counter(s for r in ko for s in r["stocks"]).most_common(25),
            "stuck": Counter(s for r in ko for s in r["stuck"]).most_common(20), "stuck_n": sum(bool(r["stuck"]) for r in ko),
            "stuck_talk": Counter(s for r in ko for s in r["stuck_talk"]).most_common(20), "stuck_talk_n": sum(bool(r["stuck_talk"]) for r in ko),
            "stocks_all_langs": Counter(s for r in rows for s in r["stocks"]).most_common(15)}


def pc(x):
    return f"{x * 100:.1f}%" if x >= 0.001 else f"{x * 100:.2f}%"


def write_md(path, D, names):
    stg, sts = names
    S = D["side"]
    L = [f"# {D['topic']} 시청자 공통 생각 — 모든 댓글에서, 많은 순", "",
         f"만든 때 {D['made']} · `tools/{D['tool']}` · 승인 영상 {D['videos']}개의 시청자 댓글 **{D['comments']:,}개 전부** "
         f"(한국어 영상 {D['by_lang'].get('한국어', 0):,} · 영어 영상 {D['by_lang'].get('영어', 0):,} · 그 밖 {D['by_lang'].get('그 밖 언어', 0):,} — 날짜·언어로 거르지 않음, 채널 주인·빈 댓글만 뺌, 답글 포함).",
         "사용자 지시 2026-11-19 \"페르소나를 만드는 목적은 시청자들이 원하는 공통적인 생각들을 정리하기 위해서야 … 누락없이 모든 댓글 … 가장 겹치는 생각들을 많은 순으로 … 나이나 처한 상황(어떤 주식에 물려있다)과 같은 여러가지 부가적인 정보는 정리만해\".",
         "※ 연구·교육용 — 댓글에서 센 숫자이며 투자 권유가 아님.", "",
         "## 0. 어떻게 셌나 (먼저 읽을 것)", "",
         f"- 모든 댓글 → 언어 묶음 × 댓글 유형마다 낱말이 비슷한 것끼리 작은 묶음 {D['clusters']}개 (Kiwi 낱말 → TF-IDF → SVD → KMeans, 씨앗 고정 — `comment_clusters.cluster_lang` 와 같은 방법).",
         f"- 묶음마다 표본 10개를 Claude(하위 에이전트)가 읽고 '시청자의 생각' 한 문장을 붙임 ({D['labeled']}개) → 같은 생각끼리 합침(`thoughts/canon.tsv`) → 댓글 수 순.",
         "- **댓글 하나 = 생각 하나** (그 댓글이 든 묶음의 생각). 한 댓글에 생각이 둘이면 많이 쓴 낱말 쪽으로 감.",
         "- **맞음** = 그 생각에 든 묶음들의 표본 중 정말 그 생각인 몫 (묶음 크기로 가중). **추정 댓글 수** = 묶음마다 댓글 수 × 맞음 을 더한 것 — 섞인 묶음을 덜 셈. **순위는 추정 댓글 수로**.",
         "- **독립 확인** = 이름을 붙인 사람과 다른 검토자가 그 생각에 든 댓글 무작위 12개를 읽고 맞음·부분·아님 (`thoughts/verify.tsv` — 한국어 상위 25개, '반응만' 뺌).",
         "- 부가 정보(나이·생애 단계·처지·지식·종목)는 **묶는 데 쓰지 않고 정리만** — 스스로 밝힌 댓글에서만 셈 (한국어 댓글만 · 종목은 모든 언어).",
         ""]
    if D["missing"]:
        L += [f"- ⚠ 이름이 안 붙은 묶음 {len(D['missing'])}개 — '(이름 안 붙은 묶음)' 줄로 셈.", ""]
    ko = [t for t in D["thoughts"] if t["lang"] == "한국어"]
    SMP = D.get("sample")
    if SMP:
        n = SMP["n"]
        L[L.index("## 0. 어떻게 셌나 (먼저 읽을 것)") + 2:L.index("## 0. 어떻게 셌나 (먼저 읽을 것)") + 2] = [
            f"- **순위(1·2번) = 무작위 표본으로 어림**: 한국어 영상 댓글 {SMP['n_ko']:,}개 전체에서 무작위 {n:,}개를 뽑아, 새 검토자(하위 에이전트 8명)가 댓글마다 아래 생각 목록에서 **직접** 하나(둘이면 둘째도) 고름 (`thoughts/classify/*.tsv`). "
            f"몫 = 표본 중 그 생각인 댓글의 몫 · 95% 범위(윌슨) · 전체 어림 = 몫 × {SMP['n_ko']:,}.",
            "- **생각 목록은 모든 댓글에서**: 아래 묶음 방법으로 모든 댓글(한 개도 빼지 않음)을 작은 묶음 수백 개로 나눠 묶음마다 이름을 붙이고 합친 것 — 목록에 없는 생각은 검토자가 K00 + 한 문장으로 적어 5번에 모음.",
            "- 왜 두 단계인가: 처음엔 댓글마다 '그 댓글이 든 묶음의 이름'을 물려줬는데, 독립 확인(다른 검토자 · 상위 25개 생각 × 무작위 12개)에서 **맞음 69 · 부분 80 · 아님 151 / 300** 이었다 — 낱말이 비슷한 묶음은 생각이 섞여 있어서. 그래서 묶음은 '생각 목록 찾기'에만 쓰고, 몫은 직접 고른 무작위 표본으로 어림한다. 묶음으로 센 수는 부록 A (참고).",
            "", "**묶음 방법** (생각 목록을 찾는 데 쓴 것 — 부록 A·4번 숫자의 바탕):"]
        L += ["## 1. 한국어 영상 댓글 — 공통 생각 순위 (무작위 표본 · 많은 순)", "",
              f"표본 {n:,}개 (계획 {SMP['planned']:,}) · 한국어 댓글 전체 {SMP['n_ko']:,}개", "",
              "| 순위 | 생각 | 갈래 | 표본 수 | 몫 (95% 범위) | 전체 어림 | 둘째 생각으로도 | 표본 속 좋아요 많은 댓글 |", "|---|---|---|---|---|---|---|---|"]
        rank = 0
        for x in SMP["rows"]:
            if not x["k"] and not x["also"]:
                continue
            rank += 1
            ex = x["examples"][0] if x["examples"] else {"likes": 0, "text": ""}
            L.append(f"| {rank} | **{x['thought']}** | {x['kind']} | {x['k']} | {x['share'] * 100:.1f}% ({x['lo'] * 100:.1f}~{x['hi'] * 100:.1f}%) | 약 {x['est']:,} | {x['also']} | 👍{ex['likes']:,} {ex['text'].replace('|', '/')} |")
        kinds = Counter()
        for x in SMP["rows"]:
            kinds[x["kind"] if x["code"] != "K00" else "목록에 없음"] += x["k"]
        L += ["", "### 1-1. 갈래로 묶으면 (표본 몫)", "", "| 갈래 | 표본 수 | 몫 (95% 범위) |", "|---|---|---|"]
        for k_, v_ in kinds.most_common():
            lo_, hi_ = wilson(v_, n)
            L.append(f"| {k_} | {v_} | {v_ / n * 100:.1f}% ({lo_ * 100:.1f}~{hi_ * 100:.1f}%) |")
        L += ["", "## 2. 생각마다 — 표본 속 댓글과 부가 정보 (표본 15개 이상)", ""]
        rank = 0
        for x in SMP["rows"]:
            if x["k"] < 15:
                continue
            rank += 1
            L.append(f"### {rank}. {x['thought']} — 표본 {x['k']} ({x['share'] * 100:.1f}%, 95% {x['lo'] * 100:.1f}~{x['hi'] * 100:.1f}%) · 전체 어림 약 {x['est']:,}개")
            L.append(f"- 갈래 {x['kind']} · 둘째 생각으로도 {x['also']}개 · 표본이 나온 영상 {x['videos']}개 · 기계 유형 " + " · ".join(f"{a} {b}" for a, b in x["types"]))
            L.append("- 표본 속 댓글 (좋아요 순): " + " / ".join(f"\"{e['text']}\" 👍{e['likes']:,}" for e in x["examples"]))
            side = []
            if x["ages"]:
                side.append("밝힌 나이 " + " · ".join(f"{a}대 {b}" for a, b in x["ages"]))
            if x["states"]:
                side.append("처지 " + " · ".join(f"{sts.get(a, a)} {b}" for a, b in x["states"]))
            if x["stocks"]:
                side.append("말한 종목 " + " · ".join(f"{a} {b}" for a, b in x["stocks"]))
            if x["stuck"]:
                side.append("내가 물렸다고 한 종목 " + " · ".join(f"{a} {b}" for a, b in x["stuck"]))
            L.append("- 부가 정보 (표본 안): " + (" | ".join(side) if side else "밝힌 것 없음"))
            L.append("")
        L += ["## 부록 A. 묶음으로 센 수 (참고 — 독립 확인 맞음 23% · 부분 27%라 몫으로 쓰지 않음)", ""]
    L += ["## 1. 한국어 영상 댓글 — 공통 생각 순위" if not SMP else "", "",
          "| 순위 | 생각 | 갈래 | 추정 댓글 수 (몫) | 묶인 댓글 수 | 맞음 | 독립 확인 (무작위 12개) | 좋아요 합 | 영상 수 | 좋아요 많은 댓글 |", "|---|---|---|---|---|---|---|---|---|---|"]
    for i, t in enumerate(ko, 1):
        ex = t["examples_liked"][0] if t["examples_liked"] else {"likes": 0, "text": ""}
        prec = f"{t['precision']:.0%}" if t["precision"] is not None else "-"
        ck = t.get("checked")
        cks = f"맞음 {ck['yes']} · 부분 {ck['part']} · 아님 {ck['no']}" if ck else "-"
        L.append(f"| {i} | **{t['thought']}** | {t['kind']} | {t['est']:,} ({pc(t['est_share'])}) | {t['n']:,} | {prec} | {cks} | {t['likes']:,} | {t['videos']} | 👍{ex['likes']:,} {ex['text'].replace('|', '/')} |")
    L += ["", "## 2. 생각마다 — 대표 댓글과 부가 정보 (상위 40)" if not SMP else "", ""]
    for i, t in enumerate(ko[:40] if not SMP else [], 1):
        L.append(f"### {i}. {t['thought']} — 추정 {t['est']:,}개 ({pc(t['est_share'])}) · 묶인 댓글 {t['n']:,} · 맞음 {t['precision']:.0%}" if t["precision"] is not None else f"### {i}. {t['thought']} — 댓글 {t['n']:,}개")
        L.append(f"- 갈래 {t['kind']} · 기계 유형 " + " · ".join(f"{a} {b:,}" for a, b in t["types"]) + f" · 영상 {t['videos']}개 · 묶음 {len(t['clusters'])}개")
        L.append("- 대표 댓글 (묶음 가운데): " + " / ".join(f"\"{e['text']}\" 👍{e['likes']}" for e in t["examples_central"]))
        L.append("- 좋아요 많은 댓글: " + " / ".join(f"\"{e['text']}\" 👍{e['likes']:,}" for e in t["examples_liked"]))
        side = []
        if t["age_n"]:
            side.append("밝힌 나이 " + " · ".join(f"{a}대 {b}" for a, b in t["ages"]) + f" (명 {t['age_n']})")
        if t["stages"]:
            side.append("생애 단계 " + " · ".join(f"{stg.get(a, a)} {b}" for a, b in t["stages"]))
        if t["states"]:
            side.append("처지 " + " · ".join(f"{sts.get(a, a)} {b}" for a, b in t["states"]))
        if t["stocks"]:
            side.append("말한 종목 " + " · ".join(f"{a} {b}" for a, b in t["stocks"]))
        if t["stuck"]:
            side.append("내가 물렸다고 한 종목 " + " · ".join(f"{a} {b}" for a, b in t["stuck"]))
        elif t["stuck_talk"]:
            side.append("물림·손실 이야기에 나온 종목 " + " · ".join(f"{a} {b}" for a, b in t["stuck_talk"]))
        L.append("- 부가 정보: " + (" | ".join(side) if side else "밝힌 것 없음"))
        L.append("")
    L += ["## 3. 부가 정보 — 정리만 (한국어 영상 댓글, 스스로 밝힌 것)", "",
          f"- 밝힌 나이 ({S['age_n']:,}명 · 한국어 댓글의 {pc(S['age_n'] / max(1, S['ko_comments']))}): " + " · ".join(f"{a}대 {b:,}" for a, b in S["ages"]),
          "- 생애 단계: " + " · ".join(f"{stg.get(a, a)} {b:,}" for a, b in S["stages"]),
          "- 처지: " + " · ".join(f"{sts.get(a, a)} {b:,}" for a, b in S["states"]),
          "- 지식 단서: " + " · ".join(f"{a} {b:,}" for a, b in S["know"]),
          "- 말한 종목 (많은 순): " + " · ".join(f"{a} {b:,}" for a, b in S["stocks"]),
          f"- **내가 물렸다고 한 종목** ({S['stuck_n']:,}개 댓글 — 종목 이름 앞뒤 25자에 물렸·손실·평단·반토막·손절 … + 그 옆에 저는·제가… 또는 짧은 경험·질문 댓글): " + " · ".join(f"{a} {b:,}" for a, b in S["stuck"]),
          f"- 물림·손실 이야기에 나온 종목 ({S['stuck_talk_n']:,}개 댓글 — 남 이야기·일반론 포함): " + " · ".join(f"{a} {b:,}" for a, b in S["stuck_talk"]),
          "- 모든 언어에서 말한 종목: " + " · ".join(f"{a} {b:,}" for a, b in S["stocks_all_langs"]), ""]
    for lang in ("영어", "그 밖 언어"):
        F = [t for t in D["thoughts"] if t["lang"] == lang]
        if not F:
            continue
        L += [f"## 4. {lang} 영상 댓글 — 공통 생각 (묶음으로 센 참고 순위 · 우리 채널은 한국어라 1번과 섞지 않음 · 표본 확인 안 함)", "",
              "| 순위 | 생각 | 갈래 | 추정 댓글 수 (몫) | 묶인 댓글 수 | 맞음 | 좋아요 많은 댓글 |", "|---|---|---|---|---|---|---|"]
        for i, t in enumerate(F[:30], 1):
            ex = t["examples_liked"][0] if t["examples_liked"] else {"likes": 0, "text": ""}
            prec = f"{t['precision']:.0%}" if t["precision"] is not None else "-"
            L.append(f"| {i} | {t['thought']} | {t['kind']} | {t['est']:,} ({pc(t['est_share'])}) | {t['n']:,} | {prec} | 👍{ex['likes']:,} {ex['text'].replace('|', '/')} |")
        L.append("")
    if SMP and SMP["other_memos"]:
        L += [f"## 5. 목록에 없던 생각 (표본에서 K00 — {len(SMP['other_memos'])}개, 검토자 메모 그대로)", ""]
        for m_ in sorted(Counter(SMP["other_memos"]).items(), key=lambda x: -x[1]):
            L.append(f"- {m_[0]}" + (f" ×{m_[1]}" if m_[1] > 1 else ""))
        L.append("")
    L += ["## 6. 한계", "",
          "- 1·2번 몫은 무작위 표본 어림 — 95% 범위를 같이 볼 것 (표본 15개 미만인 생각은 순위 차이에 큰 뜻이 없음). 검토자 판단은 AI 하위 에이전트.",
          "- 묶음은 '같은 낱말을 쓴 댓글'이다 — 뜻이 같아도 낱말이 다르면 다른 묶음에 갈 수 있고, 그래서 같은 생각을 canon.tsv 로 합쳤다.",
          "- 생각 이름은 묶음마다 표본 10개로 정했다 — 맞음 칸이 그 어림의 정확도. 댓글 하나에 생각 하나만 셈.",
          "- 같은 사람이 여러 댓글을 달면 여러 번 센다 (작성자 정보는 저장하지 않음). 많이 단 영상(댓글 수천 개)의 주제가 크게 잡힌다 — 영상 수 칸을 같이 볼 것.",
          "- 댓글이 더해지면 묶음이 바뀌므로 build → 이름 붙이기 → report 를 다시 한다.", ""]
    Path(path).write_text("\n".join(L), "utf-8")


def main(argv=None):
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    ap = argparse.ArgumentParser(description="시청자 공통 생각 — 모든 댓글")
    ap.add_argument("topic")
    ap.add_argument("cmd", choices=["build", "report", "verify", "classify"])
    a = ap.parse_args(argv)
    t0 = time.time()
    if a.cmd == "build":
        build(a.topic)
    elif a.cmd == "verify":
        verify_todo(a.topic)
    elif a.cmd == "classify":
        classify_todo(a.topic)
    else:
        report(a.topic)
    log("DONE", cmd=a.cmd, seconds=round(time.time() - t0, 1))


if __name__ == "__main__":
    main()
