#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-11-19 — **페르소나 하나로** (사용자 지시 "아니 페르소나를 따로 만들지 말고 생각, 부가정보 등을 종합해서 하나로 할거야"):
#          묶음(F1~F6)마다 나누지 않고 시청자 한 명(P1)으로 — 투자 욕구 묶음·하나씩 · 아는 정도 · 개념 · 댓글을 쓴 이유 · 자주 하는 말 = 무작위 표본,
#          부가 정보(나이·생애 단계·처지·말한 종목·물렸다고 한 종목)·실제로 묻는 말·좋아함·불만 = 한국어 영상 댓글 전부. personas.json 칸은 그대로(사람 1명).
# (v1.0 — 2026-11-19 — 새로: **투자 욕구 · 아는 정도로 만든 시청자 페르소나** (사용자 지시 2026-11-19 "시청자들이 할 법할 생각을 더 추가해보고
#          그 결과로 주제 탐색이랑 페르소나 바꿔 페르소나 내용은 파일로 보여주고" — 앞서 "페르소나를 만드는 목적은 시청자들이 원하는 공통적인 생각들을
#          정리하기 위해서야 … 누락없이 모든 댓글 … 나이나 처한 상황 … 부가적인 정보는 정리만해" · "댓글을 쓴 사람이 할법한 생각을 유추하라고 … 어느정도까지
#          알고있는지도").
#          · 자료 = tools/viewer_thoughts.py 의 무작위 표본(한국어 영상 댓글 전체에서 2,400개) 추론 결과:
#            invest/*.tsv (투자 욕구 I01~I41 · 묶음 F1~F6) · wants/*.tsv (지식 수준 · 핵심 개념 이해/언급/오해 · 빠진 개념 · 댓글을 쓴 이유 W) ·
#            classify/*.tsv (자주 하는 말 = 생각 목록) · .yt_work rows (부가 정보 — 나이·처지·말한 종목·물린 종목 · 댓글 유형·좋아요).
#          · 페르소나 = 첫째 투자 욕구의 묶음(F1~F6)마다 · 고르는 규칙은 personas.py 와 같음 (댓글 30개 이상 · 몫 8% 이상 · 누적 80% · 2~6명).
#            나이·처지는 묶는 데 쓰지 않고 정리만.
#          · 쓰는 곳이 그대로 돌게 personas.json 칸(id·key·name·share·age·know·known_terms·unknown_terms·want_terms·want_words·top_questions·
#            likes_cat·dislikes_cat·states·quotes·types·groups)을 같은 꼴로 채우고, 새 칸(invest_wants·concepts·reasons·says·stocks·stuck)을 더함.
#          · personas.py build() 가 설정 SOURCE = "thoughts" 이면 이 도구를 부름 (분석이 끝날 때 저절로).
#          ※ 연구·교육용 — 투자 권유가 아님.
"""투자 욕구 · 아는 정도로 만든 시청자 페르소나

  python3 tools/thought_personas.py stock          # → stock/result/outliers/personas.md · personas.json
"""
import gzip
import json
import logging
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comment_types as ct          # noqa: E402
import personas as ps               # noqa: E402  choose · cues · 설정
import viewer_thoughts as vt        # noqa: E402  INVEST · INVEST_FAMILY · CONCEPTS · WANTS · paths · read_tsv · one_line · wilson

VERSION = "v1.1"
ROOT = Path(__file__).resolve().parent.parent
LOG = logging.getLogger("tpersona")
NAMES = {   # 묶음 → 페르소나 이름 (짧게) — 묶음 뜻은 viewer_thoughts.INVEST_FAMILY
    "F1": "앞으로 오를지·내릴지 미리 알고 싶은 투자자",
    "F2": "잃지 않고 꾸준히 불리고 싶은 투자자",
    "F3": "믿을 근거·원칙을 찾는 투자자",
    "F4": "정부·제도가 지켜 주길 바라는 투자자",
    "F5": "물린 손실을 되찾거나 크게 벌고 싶은 투자자",
    "F6": "국장을 떠나려는 투자자",
}
CHANNEL_NOTE = {   # 채널 목적(stock/guides/channel.md — 리스크를 줄이고 천천히 · 타이밍·종목 맞히기 ✗ · 정치 ✗)과의 관계
    "F1": "가장 큰 무리 — 바람(예측·타이밍·종목)은 채널이 답으로 주지 않는 것. 호기심 입구로 쓰고 답은 '맞히기보다 덜 잃는 법'으로 (과거 자료로 그 바람을 시험해 보이는 꼴).",
    "F2": "채널 목적과 가장 가까운 무리 — 장기·적립·배당·비중·노후. 배당·커버드콜 구조를 틀리게 아는 사람이 많음.",
    "F3": "전문가·전망을 믿지 못해 '근거'를 찾는 무리 — 실제 숫자·모든 날 계산·출처를 보여 주는 꼴이 맞음.",
    "F4": "정부·제도·책임자 이야기를 하는 무리 — 채널은 정치를 주제로 삼지 않음(정당·정치인 ✗). 제도 숫자(세금·규칙)만 다룰 수 있음.",
    "F5": "손실 회복·레버리지·빚투 무리 — 위험 관리·레버리지 구조가 가장 많이 빠짐.",
    "F6": "국장을 떠나 미국·부동산·예금으로 옮기려는 무리.",
}
CONCEPT_WORD = {   # 개념 → 대본 검사용 낱말 (persona_review 의 '잘 모르는 말')
    "C01": "금리", "C02": "환율", "C03": "물가", "C04": "국면", "C05": "업황", "C06": "PER", "C07": "실적", "C08": "자산배분", "C09": "분산 투자",
    "C10": "리밸런싱", "C11": "장기 투자", "C12": "적립식", "C13": "ETF", "C14": "레버리지", "C15": "배당락", "C16": "커버드콜", "C17": "절세 계좌",
    "C18": "수급", "C19": "공매도", "C20": "손절", "C21": "손실 회피", "C22": "환헤지", "C23": "주주환원",
}
LEVEL_OLD = {"초보": "초급", "기초": "기초", "중급": "중급", "고급": "상급"}     # 옛 칸 이름 (persona_review 가 '초급'·'기초' 를 봄)
WANT_STOP = set("싶다 알다 원하다 바라다 되다 하다 있다 없다 않다 지금 정말 미리 다시 얼마나 어디 언제 무엇 정하다 갖다 얻다 내다 주다 보다 같다 크다".split())


def log(stage, level=logging.INFO, **kv):
    LOG.log(level, "[%s] [%s] %s", stage, datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), " ".join(f"{k}={v}" for k, v in kv.items()))


def _tsv(path, ncol):
    out = {}
    for f in sorted(Path(path).glob("*.tsv")):
        for i, line in enumerate(f.read_text("utf-8").splitlines()):
            if i == 0 or not line.strip():
                continue
            a = (line.split("\t") + [""] * ncol)[:ncol]
            out[a[0].strip()] = [x.strip() for x in a]
    return out


def load(topic):
    """표본 댓글마다 한 줄: 글·좋아요·부가 정보 + 투자 욕구 + 지식·개념 + 댓글을 쓴 이유 + 자주 하는 말."""
    P = vt.paths(topic)
    rows = [json.loads(l) for l in gzip.open(P["work"] / "rows.jsonl.gz", "rt", encoding="utf-8")]
    ko = [r for r in rows if r["lang"] == "한국어"]
    vids = json.loads((P["work"] / "videos.json").read_text("utf-8"))
    IK = json.loads((P["dir"] / "invest_keys.json").read_text("utf-8"))
    WK = json.loads((P["dir"] / "wants_keys.json").read_text("utf-8"))
    CK = json.loads((P["dir"] / "classify_keys.json").read_text("utf-8"))
    inv, wan, cla = _tsv(P["dir"] / "invest", 5), _tsv(P["dir"] / "wants", 8), _tsv(P["dir"] / "classify", 4)
    w_by_row = {k["row"]: wan.get(k["id"]) for k in WK["keys"]}
    c_by_row = {k["row"]: cla.get(k["id"]) for k in CK["keys"]}
    tl = {k: t for k, _key, t, _g in CK["thoughts"]}
    S = []
    for k in IK["keys"]:
        a = inv.get(k["id"])
        if not a:
            continue
        r = dict(ko[k["row"]])
        c1 = (re.findall(r"I\d\d", a[1].upper()) or ["I00"])[0]
        c2 = (re.findall(r"I\d\d", a[2].upper()) or [""])[0]
        r.update({"i1": c1, "i2": c2 if c2 != c1 else "", "infer": a[3], "conf": a[4][:1], "group": (vids.get(r["vid"]) or {}).get("group", "?")})
        w = w_by_row.get(k["row"])
        if w:
            r["level"] = next((v for kk, v in (("초보", "초보"), ("기초", "기초"), ("중급", "중급"), ("고급", "고급")) if w[6].startswith(kk)), "판단불가")
            r["concepts"] = re.findall(r"(C\d\d)\s*:\s*(이해|언급|오해)", w[4])
            r["gaps"] = sorted(set(re.findall(r"C\d\d", w[5])))
            r["reason"] = (re.findall(r"W\d\d", w[2].upper()) or ["W00"])[0]
        else:
            r.update({"level": "판단불가", "concepts": [], "gaps": [], "reason": "W00"})
        c = c_by_row.get(k["row"])
        r["say"] = tl.get(re.sub(r"[^K0-9]", "", (c[1] if c else "").upper())[:3], "") if c else ""
        S.append(r)
    log("LOAD", topic=topic, sample=len(S), n_ko=IK["n_ko"], with_wants=sum(1 for r in S if r["concepts"] or r["level"] != "판단불가"))
    return S, IK, ko


FAM_ADN = {"F1": "앞날을 미리 알고 싶은", "F2": "잃지 않고 꾸준히 불리고 싶은", "F3": "믿을 근거·원칙을 찾는", "F4": "정부·제도 탓을 하는",
           "F5": "손실을 되찾고 싶은", "F6": "국장을 떠나고 싶은"}
FAM_SHORT = {"F1": "앞날(하락·반등·오를 종목)을 미리 알고 싶고", "F2": "잃지 않고 꾸준히 불리고 싶고", "F3": "믿을 근거·원칙을 찾고",
             "F4": "정부·제도 탓을 하고", "F5": "손실을 되찾거나 크게 벌고 싶고", "F6": "국장을 떠나고 싶고"}


def build(topic, now=None, root=None, write=True):
    """시청자 한 명(P1)으로 — 표본 추론(바람·지식·개념) + 모든 한국어 댓글의 부가 정보."""
    P = vt.paths(topic)
    if not (P["dir"] / "invest_keys.json").is_file():
        log("SKIP", logging.WARNING, topic=topic, note="투자 욕구 추론 결과가 없음", next=f"python3 tools/viewer_thoughts.py {topic} invest → 하위 에이전트 → report")
        return None
    cfg, _ = ps.load_cfg(topic)
    C = ps.compile_cfg(cfg)["한국어"] if cfg else None
    now = now or datetime.now(timezone.utc)
    S, IK, ko = load(topic)
    fam_of = {c: f for f, _, cs in vt.INVEST_FAMILY for c in cs}
    famname = {f: t for f, t, _ in vt.INVEST_FAMILY}
    iname, cname, wname = dict(IK["invest"]), dict(vt.CONCEPTS), dict(vt.WANTS)
    M = [r for r in S if r["i1"] in fam_of]                     # 투자 욕구를 추론할 수 있었던 댓글
    n, ns = len(M), len(S)
    # 투자 욕구 — 묶음(첫째·둘째 중 하나라도) · 하나씩(첫째·둘째)
    fam_any, fam_first, wants = Counter(), Counter(), Counter()
    for r in M:
        fam_first[fam_of[r["i1"]]] += 1
        for f in {fam_of[c] for c in (r["i1"], r["i2"]) if c in fam_of}:
            fam_any[f] += 1
        wants[r["i1"]] += 1
        if r["i2"]:
            wants[r["i2"]] += 1
    ex = defaultdict(list)
    for r in sorted(M, key=lambda r: (r["conf"] != "상", -r["likes"])):
        if r["infer"] not in ("", "-") and len(ex[r["i1"]]) < 2:
            ex[r["i1"]].append({"infer": r["infer"], "text": vt.one_line(r["text"], 120), "likes": r["likes"]})
    # 아는 정도 · 개념 (표본 전부)
    lv = Counter(r["level"] for r in S if r["level"] != "판단불가")
    judged = sum(lv.values())
    cu, cm, cx, cg = Counter(), Counter(), Counter(), Counter()
    for r in S:
        for c, l in r["concepts"]:
            {"이해": cu, "언급": cm, "오해": cx}[l][c] += 1
        for c in r["gaps"]:
            cg[c] += 1
    gap_by_fam = defaultdict(Counter)
    for r in M:
        for c in r["gaps"]:
            gap_by_fam[fam_of[r["i1"]]][c] += 1
    known, unk = Counter(), Counter()
    if C:
        for r in M:
            q = ps.cues(r["text"], C, now)
            for t in q["basic"] + q["adv"]:
                known[t] += 1
            for t in q["unknown"]:
                unk[t] += 1
    for c, k_ in (cx + cg).most_common(8):
        unk[CONCEPT_WORD.get(c, c)] += k_
    want_terms, want_words = Counter(), Counter()
    for r in M:
        for t in (ps.cues(r["infer"] + " " + r["text"], C, now)["basic"] if C else []):
            want_terms[t] += 1
    try:
        import comment_clusters as cc
        for toks in cc.ko_tokens([r["infer"] for r in M if r["infer"] not in ("", "-")]):
            for w in toks:
                if w not in WANT_STOP and len(w) >= 2:
                    want_words[w] += 1
    except Exception as e:
        log("WANT_WORDS", logging.WARNING, error=str(e)[:80], note="want_words 비움")
    # 부가 정보 — 한국어 영상 댓글 전부 (스스로 밝힌 것만)
    ages = Counter((r["age"] // 10) * 10 for r in ko if r.get("age"))
    states = Counter(s_ for r in ko for s_ in (r.get("states") or []))
    stages = Counter(r["stage"] for r in ko if r.get("stage"))
    stocks = Counter(s_ for r in ko for s_ in vt.stocks_of(r["text"], r["type"])[0]) if False else Counter(s_ for r in ko for s_ in (r.get("stocks") or []))
    stuck = Counter()
    for r in ko:
        if r.get("stocks"):
            stuck.update(vt.stocks_of(r["text"], r["type"])[2])
    sts = {x["key"]: x["name"] for x in (cfg or {}).get("states", [])}
    stg = {x["key"]: x["name"] for x in (cfg or {}).get("stages", [])}
    likes, dislikes = Counter(), Counter()
    if C:
        for r in ko:
            if r["type"] == "P":
                likes.update(k_ for k_, rx in C["like"] if rx and rx.search(r["text"]))
            elif r["type"] == "C":
                dislikes.update(k_ for k_, rx in C["dislike"] if rx and rx.search(r["text"]))
    lname = {x["key"]: x["name"] for x in (cfg or {}).get("like", [])}
    dname = {x["key"]: x["name"] for x in (cfg or {}).get("dislike", [])}
    term_rx = C["basic"][0] if C and C.get("basic") else None          # 투자 낱말이 든 질문만 (농담·정치 질문 빼기)
    qs = sorted([r for r in ko if r["type"] == "Q" and not r.get("reply") and (r.get("stocks") or (term_rx and term_rx.search(r["text"])))],
                key=lambda r: -r["likes"])[:8]
    level = max(lv, key=lambda k: lv[k]) if lv else "판단불가"
    fam_rank = [f for f, _ in fam_any.most_common()]
    s1, s2 = [x for x, _ in stocks.most_common(2)] + ["", ""][: max(0, 2 - len(stocks))]
    st1 = sts.get(states.most_common(1)[0][0], "") if states else ""
    lv_txt = LEVEL_OLD.get(level, level)
    if fam_rank[:2] in (["F1", "F3"], ["F3", "F1"]):
        name = f"{s1}·{s2}에 돈이 묶여 앞날을 미리 알고 싶지만, 누구 말을 믿을지 몰라 근거를 찾는 {lv_txt} 지식 개인 투자자"
    else:
        name = f"{s1}·{s2}에 돈이 묶인, {FAM_ADN.get(fam_rank[0], '')} {lv_txt} 지식 개인 투자자"
    one = (f"한국어 영상 시청자 한 명으로 합친 모습 — 가장 큰 바람: " + " · ".join(f"{famname[f].split(' (')[0]} {fam_any[f] / n * 100:.0f}%" for f in fam_rank[:3])
           + f" · 지식 {LEVEL_OLD.get(level, level)} (판단 가능한 댓글의 {lv.get(level, 0) / max(1, judged) * 100:.0f}%) · 가장 많이 빠진 개념: "
           + ", ".join(cname[c].split(' (')[0] for c, _ in cg.most_common(3)) + f" · 가장 많이 밝힌 처지: {st1} · 가장 많이 말한 종목: {s1}·{s2}")
    p = {
        "id": "P1", "key": "ALL", "name": name, "n": n, "share": 1.0, "likes": sum(r["likes"] for r in M), "lang": "한국어", "one_liner": one,
        "families": [{"code": f, "family": famname[f], "any": fam_any[f], "any_share": round(fam_any[f] / n, 3), "first": fam_first[f],
                      "gap_top": [[cname[c].split(" (")[0], k_] for c, k_ in gap_by_fam[f].most_common(3)]} for f in fam_rank],
        "invest_wants": [{"code": c, "want": iname[c], "n": k_, "share": round(k_ / n, 3), "family": fam_of.get(c), "examples": ex.get(c, [])} for c, k_ in wants.most_common(15)],
        "know": {"n": judged, "dist": {LEVEL_OLD[k]: v for k, v in lv.items()}, "level": LEVEL_OLD.get(level, level), "unknown_share": round(1 - judged / ns, 3) if ns else None},
        "concepts": {"understand": [[cname[c], k_] for c, k_ in cu.most_common(8)], "mention": [[cname[c], k_] for c, k_ in cm.most_common(8)],
                     "misunderstand": [[cname[c], k_] for c, k_ in cx.most_common(8)], "missing": [[cname[c], k_] for c, k_ in cg.most_common(8)],
                     "shown_share": round(sum(1 for r in S if r["concepts"]) / ns, 3) if ns else 0},
        "reasons": [[wname.get(c, c), k_] for c, k_ in Counter(r["reason"] for r in S).most_common(8)],
        "says": [[t, k_] for t, k_ in Counter(r["say"] for r in S if r["say"]).most_common(10)],
        "age": {"n": sum(ages.values()), "median_decade": sorted(ages.elements())[sum(ages.values()) // 2] if ages else None,
                "dist": {f"{a}대": v for a, v in sorted(ages.items())}},
        "stages": [[stg.get(k_, k_), v] for k_, v in stages.most_common()],
        "states": [{"key": k_, "name": sts.get(k_, k_), "n": v, "share": round(v / len(ko), 4)} for k_, v in states.most_common(11)],
        "stocks": stocks.most_common(15), "stuck": stuck.most_common(10),
        "known_terms": known.most_common(12), "unknown_terms": unk.most_common(10),
        "want_terms": want_terms.most_common(14), "want_words": want_words.most_common(14),
        "top_questions": [{"text": vt.one_line(r["text"], 200), "likes": r["likes"]} for r in qs],
        "likes_cat": [{"name": lname.get(k_, k_), "n": v} for k_, v in likes.most_common(5)],
        "dislikes_cat": [{"name": dname.get(k_, k_), "n": v} for k_, v in dislikes.most_common(6)],
        "quotes": [{"text": vt.one_line(r["text"], 160), "likes": r["likes"], "age": r.get("age"), "infer": r["infer"], "states": []}
                   for r in sorted(M, key=lambda r: -r["likes"])[:5]],
        "types": dict(Counter(ct.type_name(r["type"]) for r in S).most_common()),
        "groups": dict(Counter(r["group"] for r in S).most_common()),
        "channel_note": " / ".join(f"{f}: {CHANNEL_NOTE[f]}" for f in fam_rank[:4] if f in CHANNEL_NOTE),
    }
    D = {"topic": topic, "tool": f"thought_personas.py {VERSION}", "config_version": (cfg or {}).get("version", "?"), "made": now.strftime("%Y-%m-%dT%H:%M:%SZ"), "source": "thoughts",
         "rules": {"from": "시청자 한 명으로 합침 (사용자 지시 2026-11-19 '페르소나를 따로 만들지 말고 … 종합해서 하나로')"},
         "data": {"n_ko": IK["n_ko"], "sample": ns, "inferable": n, "assigned": n, "side_from": len(ko)},
         "segments": [{"key": f["code"], "n": f["any"], "share": f["any_share"], "cum": None, "chosen": True, "why": "하나로 합침"} for f in p["families"]],
         "personas": [p], "overall": {"want_terms": [], "want_words": [], "shared_wants": []}}
    out = P["out"]
    if write:
        (out / "personas.json").write_text(json.dumps(D, ensure_ascii=False, indent=1), "utf-8")
        (out / "personas.md").write_text(render_md(D), "utf-8")
    log("BUILD", topic=topic, personas=1, name=name, inferable=n, side_from=len(ko), md=out / "personas.md")
    return D


def render_md(D):
    p = D["personas"][0]
    c = p["concepts"]
    L = [f"# {D['topic']} 시청자 페르소나 — 하나로 합친 시청자 (자동)", "",
         f"만든 때 {D['made']} · `tools/{D['tool']}` · 바람·지식·개념 = `tools/viewer_thoughts.py` 무작위 표본 (한국어 영상 댓글 {D['data']['n_ko']:,}개 전체에서 {D['data']['sample']:,}개 · 투자 욕구를 추론할 수 있었던 {D['data']['inferable']:,}개) · 부가 정보·묻는 말 = 한국어 영상 댓글 {D['data']['side_from']:,}개 전부.",
         "사용자 지시 2026-11-19 \"페르소나를 만드는 목적은 시청자들이 원하는 공통적인 생각들을 정리하기 위해서야\" · \"댓글을 쓴 사람이 할법한 생각을 유추하라고 … 어느정도까지 알고있는지도\" · \"페르소나를 따로 만들지 말고 생각, 부가정보 등을 종합해서 하나로 할거야\".",
         "※ 연구·교육용. 댓글에서 어림한 숫자이며 투자 권유가 아니다. 추론은 AI 하위 에이전트가 함 (`stock/result/outliers/thoughts/`).", "",
         f"## P1 {p['name']}", "", p["one_liner"], "",
         "## 1. 투자에서 원하는 것", "", "### 1-1. 바람 묶음 (첫째·둘째 바람 중 하나라도 — 합이 100% 를 넘음)", "",
         "| 묶음 | 몫 (투자 욕구가 보인 댓글 중) | 첫째 바람으로만 | 이 바람에 자주 빠진 개념 |", "|---|---|---|---|"]
    for f in p["families"]:
        L.append(f"| **{f['family']}** | {f['any_share'] * 100:.0f}% ({f['any']}) | {f['first']} | {' · '.join(f'{a} {b}' for a, b in f['gap_top']) or '-'} |")
    L += ["", "### 1-2. 바람 하나씩 (많은 순 · 첫째·둘째)", "", "| 바람 | 몫 | 추론 ← 원래 댓글 |", "|---|---|---|"]
    for w in p["invest_wants"]:
        e = w["examples"][0] if w["examples"] else None
        L.append(f"| {w['want']} ({w['code']}) | {w['share'] * 100:.1f}% | " + (f"\"{e['infer']}\" ← \"{e['text']}\" 👍{e['likes']}".replace("|", "/") if e else "-") + " |")
    L += ["", "## 2. 얼마나 아는지", "",
          f"- **지식 수준**: {p['know']['level']} — " + " · ".join(f"{k} {v}" for k, v in sorted(p["know"]["dist"].items(), key=lambda x: -x[1])) + f" · 판단 불가 {p['know']['unknown_share'] * 100:.0f}% (내용이 너무 짧음)",
          f"- 핵심 개념을 하나라도 드러낸 댓글: {c['shown_share'] * 100:.0f}% (개념은 댓글에 나온 것만 판단 — 안 쓴 개념을 모른다는 뜻은 아님)",
          "- 바르게 씀: " + (" · ".join(f"{a.split(' (')[0]} {b}" for a, b in c["understand"]) or "-"),
          "- 말만 씀 (이해 깊이가 안 보임): " + (" · ".join(f"{a.split(' (')[0]} {b}" for a, b in c["mention"]) or "-"),
          "- **틀리게 앎**: " + (" · ".join(f"{a.split(' (')[0]} {b}" for a, b in c["misunderstand"]) or "-"),
          "- **필요한데 빠짐** (그 바람·판단에 꼭 필요한데 놓친 것): " + (" · ".join(f"{a.split(' (')[0]} {b}" for a, b in c["missing"]) or "-"), "",
          "## 3. 왜 댓글을 쓰고, 무슨 말을 자주 하나", "",
          "- 댓글을 쓴 이유: " + " · ".join(f"{a} {b}" for a, b in p["reasons"]),
          "- 자주 하는 말 (생각 목록): " + " · ".join(f"{a} {b}" for a, b in p["says"]), "",
          "## 4. 부가 정보 — 정리만 (한국어 영상 댓글 전부, 스스로 밝힌 것)", "",
          f"- 밝힌 나이 ({p['age']['n']}명): " + (" · ".join(f"{a} {v}" for a, v in p["age"]["dist"].items()) or "근거 없음"),
          "- 생애 단계: " + " · ".join(f"{a} {b}" for a, b in p["stages"]),
          "- 처지: " + " · ".join(f"{s_['name']} {s_['n']:,}" for s_ in p["states"]),
          "- 말한 종목: " + " · ".join(f"{a} {b:,}" for a, b in p["stocks"]),
          "- **내가 물렸다고 한 종목**: " + " · ".join(f"{a} {b}" for a, b in p["stuck"]),
          "- 좋아하는 것 (칭찬 댓글): " + " · ".join(f"{x['name']} {x['n']:,}" for x in p["likes_cat"]),
          "- 싫어하는 것·떠나는 까닭 (비판 댓글): " + " · ".join(f"{x['name']} {x['n']:,}" for x in p["dislikes_cat"]), "",
          "## 5. 실제로 묻는 말 · 대표 댓글", "", "- 좋아요 많은 질문 (답글 뺌):"]
    for q in p["top_questions"]:
        L.append(f"  - \"{q['text']}\" 👍{q['likes']:,}")
    L.append("- 표본 속 좋아요 많은 댓글 → 추론한 바람:")
    for q in p["quotes"]:
        L.append(f"  - \"{q['text']}\" 👍{q['likes']:,} → {q['infer']}")
    L += ["", "## 6. 주제·제목·대본에 쓸 때", "",
          "- 기획안 `persona` 칸 = P1 (하나) · 핵심은 `want`(1-2 바람 I 번호)와 `gap`(2번 개념 C 번호) — `stock/guides/board_1_topic.md` 2번.",
          "- 채널과의 관계 (`stock/guides/channel.md` — 리스크를 줄이고 천천히 · 맞히기 ✗ · 정치 ✗):"]
    for part in p["channel_note"].split(" / "):
        L.append(f"  - {part}")
    L += ["", "## 7. 한계 — 먼저 읽을 것", "",
          "- 바람·지식·개념은 무작위 표본 2,400개를 AI 하위 에이전트가 추론한 것 — 1~2%대 바람끼리의 순위 차이는 뜻이 작다.",
          "- 부가 정보는 스스로 밝힌 댓글만 (나이는 아주 적음) · 같은 사람의 여러 댓글은 따로 셈.",
          "- 새 댓글이 쌓이면 `viewer_thoughts.py` 단계(묶기 → 이름 → classify·wants·invest) 뒤 이 도구를 다시.", ""]
    return "\n".join(L)


def main(argv=None):
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    a = (argv or sys.argv[1:]) or ["stock"]
    build(a[0])


if __name__ == "__main__":
    main()
