#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-11-19 — 새로: **투자 욕구 · 아는 정도로 만든 시청자 페르소나** (사용자 지시 2026-11-19 "시청자들이 할 법할 생각을 더 추가해보고
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

VERSION = "v1.0"
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
    return S, IK


def build(topic, now=None, root=None, write=True):
    P = vt.paths(topic)
    if not (P["dir"] / "invest_keys.json").is_file():
        log("SKIP", logging.WARNING, topic=topic, note="투자 욕구 추론 결과가 없음", next=f"python3 tools/viewer_thoughts.py {topic} invest → 하위 에이전트 → report")
        return None
    cfg, _ = ps.load_cfg(topic)
    C = ps.compile_cfg(cfg)["한국어"] if cfg else None
    now = now or datetime.now(timezone.utc)
    S, IK = load(topic)
    fam_of = {c: f for f, _, cs in vt.INVEST_FAMILY for c in cs}
    iname = dict(IK["invest"])
    cname = dict(vt.CONCEPTS)
    wname = dict(vt.WANTS)
    inferable = [r for r in S if r["i1"] in fam_of]
    seg = Counter(fam_of[r["i1"]] for r in inferable)
    pcfg = dict(ps.DEFAULTS)
    pcfg.update(cfg or {})
    chosen, table = ps.choose(dict(seg), len(inferable), pcfg)
    now_s = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    personas = []
    for i, fam in enumerate(chosen, 1):
        M = [r for r in inferable if fam_of[r["i1"]] == fam]
        n = len(M)
        wants = Counter()
        for r in M:
            wants[r["i1"]] += 1
            if r["i2"]:
                wants[r["i2"]] += 1
        ex = defaultdict(list)
        for r in sorted(M, key=lambda r: (r["conf"] != "상", -r["likes"])):
            if r["infer"] not in ("", "-") and len(ex[r["i1"]]) < 2:
                ex[r["i1"]].append({"infer": r["infer"], "text": vt.one_line(r["text"], 120), "likes": r["likes"]})
        lv = Counter(r["level"] for r in M if r["level"] != "판단불가")
        judged = sum(lv.values())
        cu, cm, cx, cg = Counter(), Counter(), Counter(), Counter()
        for r in M:
            for c, l in r["concepts"]:
                {"이해": cu, "언급": cm, "오해": cx}[l][c] += 1
            for c in r["gaps"]:
                cg[c] += 1
        # 옛 칸 — personas.cues 로 낱말·좋아함·불만 (표본 안에서)
        known, unk, likes, dislikes = Counter(), Counter(), Counter(), Counter()
        if C:
            for r in M:
                q = ps.cues(r["text"], C, now)
                for t in q["basic"] + q["adv"]:
                    known[t] += 1
                for t in q["unknown"]:
                    unk[t] += 1
                for k_ in q["like"]:
                    likes[k_] += 1
                for k_ in q["dislike"]:
                    dislikes[k_] += 1
        for c, k_ in (cx + cg).most_common(6):
            unk[CONCEPT_WORD.get(c, c)] += k_
        want_terms = Counter()
        for r in M:
            for t in (ps.cues(r["infer"] + " " + r["text"], C, now)["basic"] if C else []):
                want_terms[t] += 1
        want_words = Counter()
        try:
            import comment_clusters as cc
            for toks in cc.ko_tokens([r["infer"] for r in M if r["infer"] not in ("", "-")]):
                for w in toks:
                    if w not in WANT_STOP and len(w) >= 2:
                        want_words[w] += 1
        except Exception as e:   # Kiwi 가 없으면 낱말 칸만 비움
            log("WANT_WORDS", logging.WARNING, error=str(e)[:80], note="want_words 비움")
        ages = Counter((r["age"] // 10) * 10 for r in M if r.get("age"))
        states = Counter(s for r in M for s in (r.get("states") or []))
        sts = {s["key"]: s["name"] for s in (cfg or {}).get("states", [])}
        lname = {c["key"]: c["name"] for c in (cfg or {}).get("like", [])}
        dname = {c["key"]: c["name"] for c in (cfg or {}).get("dislike", [])}
        qs = sorted([r for r in M if r["type"] == "Q"], key=lambda r: -r["likes"])[:4]
        level = max(lv, key=lambda k: lv[k]) if lv else "판단불가"
        top3 = [iname[c] for c, _ in wants.most_common(3)]
        gaps3 = [cname[c].split(" (")[0] for c, _ in cg.most_common(3)]
        p = {
            "id": f"P{i}", "key": fam, "name": NAMES.get(fam, fam), "family": dict((f, t) for f, t, _ in vt.INVEST_FAMILY)[fam],
            "n": n, "share": round(n / len(inferable), 4), "likes": sum(r["likes"] for r in M), "lang": "한국어",
            "one_liner": f"{NAMES.get(fam, fam)} · 가장 원하는 것: {', '.join(top3)} · 지식 {level} · 자주 빠진 개념: {', '.join(gaps3) or '근거 없음'}",
            "channel_note": CHANNEL_NOTE.get(fam, ""),
            "invest_wants": [{"code": c, "want": iname[c], "n": k_, "share": round(k_ / n, 3), "examples": ex.get(c, [])} for c, k_ in wants.most_common(8)],
            "know": {"n": judged, "dist": {LEVEL_OLD[k]: v for k, v in lv.items()}, "level": LEVEL_OLD.get(level, level), "unknown_share": round(1 - judged / n, 3) if n else None},
            "concepts": {"understand": [[cname[c], k_] for c, k_ in cu.most_common(6)], "mention": [[cname[c], k_] for c, k_ in cm.most_common(6)],
                         "misunderstand": [[cname[c], k_] for c, k_ in cx.most_common(6)], "missing": [[cname[c], k_] for c, k_ in cg.most_common(6)],
                         "shown_share": round(sum(1 for r in M if r["concepts"]) / n, 3) if n else 0},
            "reasons": [[wname.get(c, c), k_] for c, k_ in Counter(r["reason"] for r in M).most_common(5)],
            "says": [[t, k_] for t, k_ in Counter(r["say"] for r in M if r["say"]).most_common(5)],
            "age": {"n": sum(ages.values()), "median_decade": sorted(ages.elements())[sum(ages.values()) // 2] if ages else None,
                    "dist": {f"{a}대": v for a, v in sorted(ages.items())}},
            "states": [{"key": k_, "name": sts.get(k_, k_), "n": v, "share": round(v / n, 4)} for k_, v in states.most_common(6)],
            "stocks": Counter(s for r in M for s in r["stocks"]).most_common(6),
            "stuck": Counter(s for r in M for s in r["stuck"]).most_common(4),
            "known_terms": known.most_common(10), "unknown_terms": unk.most_common(8),
            "want_terms": want_terms.most_common(12), "want_words": want_words.most_common(12),
            "top_questions": [{"text": vt.one_line(r["text"], 200), "likes": r["likes"]} for r in qs],
            "likes_cat": [{"name": lname.get(k_, k_), "n": v} for k_, v in likes.most_common(4)],
            "dislikes_cat": [{"name": dname.get(k_, k_), "n": v} for k_, v in dislikes.most_common(4)],
            "quotes": [{"text": vt.one_line(r["text"], 160), "likes": r["likes"], "age": r.get("age"), "infer": r["infer"], "states": []}
                       for r in sorted(M, key=lambda r: -r["likes"])[:4]],
            "types": dict(Counter(ct.type_name(r["type"]) for r in M).most_common()),
            "groups": dict(Counter(r["group"] for r in M).most_common()),
        }
        personas.append(p)
    D = {"topic": topic, "tool": f"thought_personas.py {VERSION}", "config_version": (cfg or {}).get("version", "?"), "made": now_s, "source": "thoughts",
         "rules": {"from": "viewer_thoughts 무작위 표본의 투자 욕구 묶음(첫째 욕구)", "MIN_N": pcfg["MIN_N"], "MIN_SHARE": pcfg["MIN_SHARE"], "COVER": pcfg["COVER"],
                   "MIN_PERSONAS": pcfg["MIN_PERSONAS"], "MAX_PERSONAS": pcfg["MAX_PERSONAS"]},
         "data": {"n_ko": IK["n_ko"], "sample": len(S), "inferable": len(inferable), "assigned": len(inferable)},
         "segments": table, "personas": personas,
         "overall": {"want_terms": [], "want_words": [], "shared_wants": [],
                     "families": [{"code": f, "family": t, "n": seg.get(f, 0), "share": round(seg.get(f, 0) / len(inferable), 4)} for f, t, _ in vt.INVEST_FAMILY]}}
    out = P["out"]
    if write:
        (out / "personas.json").write_text(json.dumps(D, ensure_ascii=False, indent=1), "utf-8")
        (out / "personas.md").write_text(render_md(D), "utf-8")
    log("BUILD", topic=topic, personas=[(p["id"], p["key"], p["n"], p["share"]) for p in personas], md=out / "personas.md")
    return D


def render_md(D):
    ps_ = D["personas"]
    L = [f"# {D['topic']} 시청자 페르소나 — 투자에서 원하는 것 · 얼마나 아는지 (자동)", "",
         f"만든 때 {D['made']} · `tools/{D['tool']}` · 자료 = `tools/viewer_thoughts.py` 무작위 표본 (한국어 영상 댓글 {D['data']['n_ko']:,}개 전체에서 {D['data']['sample']:,}개 · 투자 욕구를 추론할 수 있었던 {D['data']['inferable']:,}개).",
         "사용자 지시 2026-11-19 \"페르소나를 만드는 목적은 시청자들이 원하는 공통적인 생각들을 정리하기 위해서야\" · \"댓글을 쓴 사람이 할법한 생각을 유추하라고 … 어느정도까지 알고있는지도\" · \"시청자들이 할 법할 생각을 더 추가해보고 그 결과로 주제 탐색이랑 페르소나 바꿔\".",
         "※ 연구·교육용. 댓글에서 어림한 숫자이며 투자 권유가 아니다. 추론은 AI 하위 에이전트가 함 (`stock/result/outliers/thoughts/`).", "",
         "## 0. 한눈에", "", "| | " + " | ".join(f"**{p['id']} {p['name']}**" for p in ps_) + " |", "|---|" + "---|" * len(ps_)]

    def row(label, f):
        L.append(f"| {label} | " + " | ".join(f(p).replace("|", "/") for p in ps_) + " |")
    row("몫 (투자 욕구가 보인 댓글 중)", lambda p: f"{p['share'] * 100:.0f}% (표본 {p['n']})")
    row("가장 원하는 것", lambda p: " · ".join(f"{w['want']} {w['share'] * 100:.0f}%" for w in p["invest_wants"][:3]))
    row("지식 수준", lambda p: f"**{p['know']['level']}** — " + " · ".join(f"{k} {v}" for k, v in sorted(p["know"]["dist"].items(), key=lambda x: -x[1])) + f" (판단 불가 {p['know']['unknown_share'] * 100:.0f}%)")
    row("개념을 드러낸 댓글", lambda p: f"{p['concepts']['shown_share'] * 100:.0f}%")
    row("말은 쓰는 개념", lambda p: " · ".join(f"{c.split(' (')[0]} {k}" for c, k in (p["concepts"]["understand"] + p["concepts"]["mention"])[:4]) or "-")
    row("틀리게 아는 개념", lambda p: " · ".join(f"{c.split(' (')[0]} {k}" for c, k in p["concepts"]["misunderstand"][:3]) or "-")
    row("필요한데 빠진 개념", lambda p: " · ".join(f"{c.split(' (')[0]} {k}" for c, k in p["concepts"]["missing"][:3]) or "-")
    row("댓글을 쓴 이유", lambda p: " · ".join(f"{c} {k}" for c, k in p["reasons"][:2]))
    row("부가: 밝힌 나이", lambda p: " · ".join(f"{a} {v}" for a, v in p["age"]["dist"].items()) or "근거 없음")
    row("부가: 처지", lambda p: " · ".join(f"{s['name']} {s['n']}" for s in p["states"][:3]) or "근거 없음")
    row("부가: 말한 종목", lambda p: " · ".join(f"{a} {b}" for a, b in p["stocks"][:4]) or "-")
    row("채널과의 관계", lambda p: p["channel_note"])
    L += ["", "## 1. 몇 명인가 — 정한 방법", "",
          "- 표본 댓글마다 **첫째 투자 욕구**의 묶음(F1~F6, `tools/viewer_thoughts.py` 의 `INVEST_FAMILY`)으로 나눔 → 큰 묶음부터 댓글 30개 이상 · 몫 8% 이상 · 누적 80% 에 닿으면 멈춤 · 2~6명 (`personas.py` 와 같은 규칙).",
          "- 나이·처지·종목은 묶는 데 쓰지 않음 (정리만).", "", "| 묶음 | 댓글 | 몫 | 누적 | 결정 |", "|---|---|---|---|---|"]
    fam = {f: t for f, t, _ in vt.INVEST_FAMILY}
    for t in D["segments"]:
        cum = "" if t["cum"] is None else f"{t['cum'] * 100:.0f}%"
        L.append(f"| {t['key']} {fam.get(t['key'], '')[:40]} | {t['n']} | {t['share'] * 100:.0f}% | {cum} | {'✅ 고름' if t['chosen'] else t['why']} |")
    L += ["", "## 2. 페르소나별 자세히", ""]
    for p in ps_:
        L += [f"### {p['id']} {p['name']} — 표본 {p['n']}개 ({p['share'] * 100:.0f}%)", "", p["one_liner"], "",
              f"- **채널과의 관계**: {p['channel_note']}",
              "- **투자에서 원하는 것** (첫째·둘째 욕구, 이 페르소나 안 몫):"]
        for w in p["invest_wants"][:6]:
            L.append(f"  - {w['want']} — {w['n']} ({w['share'] * 100:.0f}%)" + "".join(f"\n    - 추론 \"{e['infer']}\" ← 댓글 \"{e['text']}\" 👍{e['likes']}" for e in w["examples"][:1]))
        c = p["concepts"]
        L += [f"- **지식 수준**: {p['know']['level']} — " + " · ".join(f"{k} {v}" for k, v in p["know"]["dist"].items()) + f" · 판단 불가 {p['know']['unknown_share'] * 100:.0f}%",
              "- **개념** (댓글에 드러난 것만 — 안 쓴 개념을 모른다는 뜻은 아님):",
              "  - 바르게 씀: " + (" · ".join(f"{a} {b}" for a, b in c["understand"]) or "-"),
              "  - 말만 씀: " + (" · ".join(f"{a} {b}" for a, b in c["mention"]) or "-"),
              "  - 틀리게 앎: " + (" · ".join(f"{a} {b}" for a, b in c["misunderstand"]) or "-"),
              "  - 필요한데 빠짐 (그 바람·판단에 꼭 필요한데 놓친 것): " + (" · ".join(f"{a} {b}" for a, b in c["missing"]) or "-"),
              "- **자주 하는 말** (생각 목록): " + (" · ".join(f"{a} {b}" for a, b in p["says"]) or "-"),
              "- **댓글을 쓴 이유**: " + " · ".join(f"{a} {b}" for a, b in p["reasons"]),
              "- **실제로 묻는 말**: " + (" / ".join(f"\"{q['text'][:110]}\" 👍{q['likes']}" for q in p["top_questions"][:3]) or "근거 없음"),
              "- **부가 정보 (정리만)**: 밝힌 나이 " + (" · ".join(f"{a} {v}" for a, v in p["age"]["dist"].items()) or "근거 없음")
              + " | 처지 " + (" · ".join(f"{s['name']} {s['n']}" for s in p["states"]) or "근거 없음")
              + " | 말한 종목 " + (" · ".join(f"{a} {b}" for a, b in p["stocks"]) or "-")
              + " | 물렸다고 한 종목 " + (" · ".join(f"{a} {b}" for a, b in p["stuck"]) or "-"),
              "- **대표 댓글** (좋아요 순 · 원문, 작성자 이름 없음):"]
        for q in p["quotes"][:3]:
            L.append(f"  - \"{q['text']}\" 👍{q['likes']:,} → 추론: {q['infer']}")
        L.append("")
    L += ["## 3. 쓰는 곳", "",
          "- **주제 탐색** (`stock/guides/board_1_topic.md` 2번): 기획안마다 `persona`(P?) + 그 페르소나의 **원하는 것**(투자 욕구) 하나 + **빠진 개념** 하나를 `basis` 에. 채널과의 관계 칸을 지킴 (F1 바람은 입구로만, F4 는 정치 ✗).",
          "- **제목·썸네일 피드 시험** (`tools/persona_gate.py`): 검토자 카드에 원하는 것·아는 정도·빠진 개념이 들어감.",
          "- **대본 피드백** (`tools/persona_review.py`): 원하는 말·잘 모르는 말(빠진·틀린 개념 낱말) 검사.", "",
          "## 4. 한계 — 먼저 읽을 것", "",
          "- 표본 2,400개 · 투자 욕구·지식·개념은 AI 하위 에이전트의 추론. 짧은 댓글은 판단 불가가 많음.",
          "- 개념은 댓글에 나온 것만 — '빠짐'은 그 사람의 바람에 꼭 필요한데 안 보인 것만 셈.",
          "- 같은 사람의 여러 댓글은 따로 셈 · 나이를 밝힌 댓글은 아주 적음 (부가 정보).",
          "- 새 댓글이 쌓이면 `viewer_thoughts.py` 의 build → 이름 → classify·wants·invest(하위 에이전트) → report 뒤 이 도구를 다시 (분석 끝의 저절로 만들기는 지난 표본 결과를 씀).", ""]
    return "\n".join(L)


def main(argv=None):
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    a = (argv or sys.argv[1:]) or ["stock"]
    build(a[0])


if __name__ == "__main__":
    main()
