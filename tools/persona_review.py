#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-28 — 새로: 대본을 시청자 페르소나(tools/personas.py 결과)로 검사 (사용자 지시 2026-10-28 "페르소나 기반으로 주제 탐색 및
#          요약본, 최종 대본 피드백에 사용"). 페르소나마다 ① 원하는 것(질문 속 용어·낱말)을 대본이 다루는지 ② 그 페르소나가 모르는 말·고급 용어가
#          풀이 없이 처음 나오는지(문장 번호) ③ 한 문장에 고급 용어 2개 이상(초급·기초 페르소나) ④ 불만 갈래(길다·반복·광고·겁주기)에 걸리는 곳.
#          결과: 대본 폴더의 persona_review.md (사람·AI 가 읽고 요약본·대본을 고침). 숫자·법이 맞는지는 보지 않는다 (script_guide 3번이 따로).
#          ※ 연구·교육용 — 투자 권유가 아님.
"""대본 × 시청자 페르소나 검사

  python3 tools/persona_review.py economic economic/source/isa-mangi-2026-10/isa-mangi-2026-10.txt
  python3 tools/persona_review.py stock stock/source/simri-test-2026-10/simri-test-2026-10.txt --out -    # 화면에만
문장 번호 = 빈 줄과 '-'로 시작하는 줄(챕터 이름)을 빼고 위에서부터 1, 2, 3… (viewer_review.md 와 같음)
로그: [STAGE] [시각] key=value (START·LOAD·CHECK·WRITE·DONE)
"""
import argparse
import json
import logging
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import personas as pz                  # noqa: E402  load_cfg (용어 사전) · kw_tokens

VERSION = "v1.0"
ROOT = Path(__file__).resolve().parent.parent
LOG = logging.getLogger("preview")
SENT_MAX = 50                          # srt_tool SENT_MAX 와 같음 (50자 넘으면 나눔)
SYL_PER_SEC = 6.3                      # 진행자 H17 샘플 속도 (CLAUDE.md) — 길이 어림
EXPLAIN = re.compile(r"(이)?란\s|(이)?라는\s|(이)?라고\s?(하는|부르)|즉[, ]|쉽게\s?말해|다시\s?말해|말하자면|뜻(입니다|이에요|이죠)|말합니다|가리킵니다|부릅니다|"
                     r"뜻하는|라는\s?뜻|이라는\s?말|\(.{2,20}\)")
EXPLAIN_NEXT = re.compile(r"^(이건|이것은|이게|그건|즉|쉽게\s?말해|다시\s?말해|말하자면|[가-힣A-Za-z]{1,8}(은|는)\s.{0,20}(돈|제도|계좌|세금|말|것|뜻))")
AD = re.compile(r"구독|좋아요|알림\s?설정|댓글\s?(남겨|달아)|링크|광고")
SCARE = re.compile(r"큰일|폭망|망합니다|망해요|무조건|절대로|당장|위험합니다|후회합니다|날립니다|폭탄")


def log(stage, _lvl=logging.INFO, **kv):
    LOG.log(_lvl, "[%s] [%s] %s", stage, datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S"),
            " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) and (' ' in v or not v) else v}" for k, v in kv.items()))


def sentences(text):
    out = []
    for ln in text.splitlines():
        t = ln.strip()
        if not t or t.startswith("-"):
            continue
        out.append(t)
    return out


def norm(s):
    return re.sub(r"\s", "", s).lower()


def term_hits(sent, terms):
    """문장 안 용어 (띄어쓰기·대소문자 무시, 영어 낱말은 경계)."""
    ns = norm(sent)
    got = []
    for t in terms:
        nt = norm(t)
        if re.match(r"[a-z0-9]", nt):
            if re.search(r"(?<![a-z])" + re.escape(nt) + r"(?![a-z])", ns):
                got.append(t)
        elif nt in ns:
            got.append(t)
    return got


def jaccard(a, b):
    a, b = set(a), set(b)
    return len(a & b) / len(a | b) if a and b else 0.0


def review(topic, script, root=None):
    t0 = time.monotonic()
    root = Path(root or ROOT)
    pj = root / topic / "result" / "outliers" / "personas.json"
    if not pj.is_file():
        log("LOAD", logging.WARNING, topic=topic, note="personas.json 없음", next=f"python3 tools/personas.py {topic}")
        return None
    P = json.loads(pj.read_text("utf-8"))
    cfg, _ = pz.load_cfg(topic, root)
    k = (cfg or {}).get("know") or {}
    adv_terms = list(dict.fromkeys((k.get("advanced") or []) + (k.get("advanced_en") or [])))
    sents = sentences(Path(script).read_text("utf-8"))
    syl = sum(len(re.sub(r"[^가-힣A-Za-z0-9]", "", s)) for s in sents)
    log("START", topic=topic, tool=f"persona_review.py {VERSION}", script=str(script), sentences=len(sents),
        personas=len(P["personas"]), personas_made=P["made"], est_minutes=round(syl / SYL_PER_SEC / 60, 1))
    # 대본 전체에서: 고급 용어 첫 등장 + 풀이 여부
    first = {}
    for i, s in enumerate(sents, 1):
        for t in term_hits(s, adv_terms):
            if t in first:
                continue
            nxt = sents[i] if i < len(sents) else ""
            et = re.escape(t)
            appos = re.search(r"[가-힣A-Za-z]{2,}인\s?" + et, s, re.I) or re.search(et + r"\s?인\s?[가-힣A-Za-z]{2,}", s, re.I)   # '개인형 퇴직연금인 IRP'
            first[t] = {"n": i, "sent": s, "explained": bool(EXPLAIN.search(s) or EXPLAIN_NEXT.search(nxt) or appos)}
    dense = [(i, s, term_hits(s, adv_terms)) for i, s in enumerate(sents, 1)]
    dense = [(i, s, h) for i, s, h in dense if len(h) >= 2]
    long_s = [(i, s, len(s)) for i, s in enumerate(sents, 1) if len(s) > SENT_MAX]
    toks = [pz.kw_tokens(s, "ko", set()) for s in sents]
    repeats = []
    for i in range(len(sents)):
        for j in range(max(0, i - 40), i):
            if len(toks[i]) >= 4 and jaccard(toks[i], toks[j]) >= 0.7:
                repeats.append((j + 1, i + 1, sents[i]))
                break
    ads = [(i, s) for i, s in enumerate(sents, 1) if AD.search(s)]
    scares = [(i, s) for i, s in enumerate(sents, 1) if SCARE.search(s)]
    log("CHECK", topic=topic, adv_terms_used=len(first), unexplained=sum(1 for v in first.values() if not v["explained"]),
        dense=len(dense), long=len(long_s), repeats=len(repeats), ads=len(ads), scares=len(scares))
    rows = []
    for p in P["personas"]:
        # 원하는 것 = 질문 속 용어(사전) + 질문 낱말 중 2번 이상 나온 것 (한 번뿐인 낱말은 잡음이 많음 — 페르소나 질문은 수십 개)
        wants = [t for t, _ in p["want_terms"][:8]] + [w for w, c in p["want_words"][:8] if c >= 2]
        wants = list(dict.fromkeys(wants))
        covered = [w for w in wants if term_hits(" ".join(sents), [w])]
        unknown = [t for t, c in p["unknown_terms"]]                    # 이 페르소나가 '…가 뭔가요'로 물어본 말
        low = p["know"]["level"] in ("초급", "기초")
        # 이 페르소나에게 풀이가 필요한 말: 그가 물어본 말 + (초급·기초면) 고급 용어 전부
        need = {t: v for t, v in first.items() if (t in unknown or low) and not v["explained"]}
        need.update({t: {"n": i, "sent": s, "explained": False} for i, s in enumerate(sents, 1) for t in term_hits(s, unknown)
                     if t not in first and t not in need and not EXPLAIN.search(s)})
        dis = [d["name"] for d in p["dislikes_cat"]]
        rows.append({"p": p, "wants": wants, "covered": covered, "need": sorted(need.items(), key=lambda x: x[1]["n"]), "low": low, "dis": dis})
        log("CHECK", topic=topic, persona=p["id"], wants=len(wants), covered=len(covered), need_explain=len(need), level=p["know"]["level"])
    base = (P.get("baselines") or [{}])[0]
    return {"topic": topic, "script": str(script), "P": P, "sents": sents, "est_min": syl / SYL_PER_SEC / 60, "first": first, "dense": dense,
            "long": long_s, "repeats": repeats, "ads": ads, "scares": scares, "rows": rows, "base": base, "seconds": time.monotonic() - t0}


def short(s, n=70):
    return s if len(s) <= n else s[:n] + "…"


def render(R):
    P = R["P"]
    L = [f"# 페르소나 검사 — `{R['script']}`", "",
         f"`tools/persona_review.py {VERSION}` · 페르소나 `{R['topic']}/result/outliers/personas.md` ({P['made']} · {len(P['personas'])}명) · "
         f"문장 {len(R['sents'])}개 · 길이 어림 {R['est_min']:.1f}분 (H17 {SYL_PER_SEC}음절/초).",
         "이 검사는 **알아듣기·원하는 것**만 본다. 숫자·법이 맞는지는 `guides/script_guide.md` 3번이 따로. ※ 연구·교육용.", ""]
    L += ["## 0. 한눈에", "", "| 페르소나 | 지식 | 원하는 것 다룸 | 풀이 없이 나온 말 | 이 페르소나의 불만 갈래 |", "|---|---|---|---|---|"]
    for r in R["rows"]:
        p = r["p"]
        L.append(f"| {p['id']} {p['name']} | {p['know']['level'] or '근거 없음'} | {len(r['covered'])}/{len(r['wants'])} | {len(r['need'])} | "
                 f"{' · '.join(r['dis'][:3]) or '근거 없음'} |")
    b = R["base"]
    if b:
        L.append(f"| *모든 댓글* | {b['know']['level']} | | | {' · '.join(d['name'] for d in b['dislikes_cat'][:4]) or '근거 없음'} |")
    L += ["", "## 1. 페르소나별", ""]
    for r in R["rows"]:
        p = r["p"]
        L += [f"### {p['id']} {p['name']}", ""]
        miss = [w for w in r["wants"] if w not in r["covered"]]
        L.append(f"- **원하는 것 — 다룸**: {', '.join(r['covered']) or '없음'}")
        L.append(f"- **원하는 것 — 안 다룸**: {', '.join(miss) or '없음'} (이 영상 주제와 맞는 것만 더한다 — 억지로 넣지 않음)")
        if r["need"]:
            L.append(f"- **풀이 없이 처음 나온 말** ({'초급·기초 — 고급 용어 모두' if r['low'] else '이 페르소나가 물어본 말만'}):")
            for t, v in r["need"][:12]:
                L.append(f"  - 문장 {v['n']} `{t}` — \"{short(v['sent'])}\"")
        else:
            L.append("- **풀이 없이 처음 나온 말**: 없음")
        if r["low"] and R["dense"]:
            L.append("- **한 문장에 고급 용어 2개 이상** (초급·기초에게 무거움): " + " · ".join(f"문장 {i} ({', '.join(h)})" for i, s, h in R["dense"][:8]))
        L.append("")
    L += ["## 2. 불만 갈래에 걸리는 곳 (모든 페르소나 공통)", ""]
    L.append(f"- **길다** — {SENT_MAX}자 넘는 문장 {len(R['long'])}개" + (": " + " · ".join(f"문장 {i} ({n}자)" for i, s, n in R["long"][:10]) if R["long"] else ""))
    L.append(f"- **반복** — 앞 40문장 안의 문장과 낱말 70% 이상 같은 문장 {len(R['repeats'])}개" +
             (": " + " · ".join(f"문장 {b2}≈{a2}" for a2, b2, s in R["repeats"][:10]) if R["repeats"] else ""))
    L.append(f"- **광고·구독 유도** — {len(R['ads'])}문장" + (": " + " · ".join(f"문장 {i}" for i, s in R["ads"][:10]) if R["ads"] else ""))
    L.append(f"- **겁주기 말** — {len(R['scares'])}문장" + (": " + " · ".join(f"문장 {i} \"{short(s, 30)}\"" for i, s in R["scares"][:8]) if R["scares"] else ""))
    L += ["", "## 3. 고칠 때", "",
          "- 풀이 없이 나온 말: 처음 나오는 문장이나 바로 다음 문장에 '쉽게 말해 …'·'…란 …입니다' 한 마디 (이미 아는 페르소나에게 길지 않게).",
          "- 원하는 것 안 다룸: 요약본 [페르소나] 칸에 이 영상이 답하는 것만 적고, 다루지 않는 것은 다음 주제 후보로 (`guides/topic_guide.md`).",
          "- 길다·반복: `guides/script_guide.md` 피드백 19(짧게). 반복은 결론 되짚기면 그대로 둔다 (마무리 요약은 반복이 아님).", ""]
    return "\n".join(L)


def main(argv=None):
    ap = argparse.ArgumentParser(description="대본 × 시청자 페르소나 검사")
    ap.add_argument("topic")
    ap.add_argument("script")
    ap.add_argument("--out", default="", help="결과 파일 (기본: 대본 폴더의 persona_review.md · '-' = 화면에만)")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args(argv)
    logging.basicConfig(level=a.log_level, format="%(message)s", stream=sys.stderr)
    R = review(a.topic, a.script)
    if not R:
        return 1
    md = render(R)
    if a.out == "-":
        print(md)
    else:
        out = Path(a.out) if a.out else Path(a.script).parent / "persona_review.md"
        out.write_text(md, "utf-8")
        log("WRITE", topic=a.topic, out=str(out))
    log("DONE", topic=a.topic, seconds=round(R["seconds"], 2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
