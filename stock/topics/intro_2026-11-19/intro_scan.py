#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-11-19 — 받은 대본의 앞 30초 모으기·세기 (사용자 지시 "분석 자료에 있는 대본에 30초 도입 부분 있지? 분석해서 썸네일, 제목 클릭 후 도입에서 이탈되지 않도록 내용 여러 개 만들어봐").
#   자료 = stock/result/outliers/W_<id>/transcript.json (자막·음성인식) + compare.csv (성공 여부·조회수·구독자).
#   묶음 = 성공 사례(compare success) · 하루 조회수 상위 10% (조회수 ÷ 올린 지 날수, 대본 있는 영상 안에서) · 그 밖.
#   관련 = 제목에 삼성·하이닉스·코스피·폭락·하락·급락·전망·반도체 중 하나.
#   센 것 (앞 30초): 첫 문장 꼴(숫자·질문·인사·지금 상황) · 제목 낱말이 30초 안에 나온 몫 · 숫자 수 · 질문 수 · 약속 말('알려 드리'·'보여 드리'·'끝까지'·'마지막') · 시청자 부르기('여러분'·'당신'·'~하신 분').
#   로그: [STAGE] [시각] key=value · 실행: python3 stock/topics/intro_2026-11-19/intro_scan.py
#   ※ 연구·교육용. 유튜브 시청 지속 자료는 없음 — '이탈 안 됨'의 근거는 성공 여부(조회수 ÷ 구독자)뿐. 음성인식 글자는 틀린 낱말이 섞임.
import csv, json, re, statistics, time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "stock/result/outliers"
HERE = Path(__file__).resolve().parent
REL = re.compile(r"삼성|하이닉스|하닉|코스피|폭락|하락|급락|전망|반도체|삼전")
NUM = re.compile(r"\d")
PROMISE = re.compile(r"알려\s?드리|보여\s?드리|정리해\s?드리|끝까지|마지막|오늘 영상|이 영상")
CALL = re.compile(r"여러분|당신|하신 분|계신 분|분들")


def log(stage, **kv):
    print(f"[{stage}] [{time.strftime('%Y-%m-%dT%H:%M:%S')}] " + " ".join(f"{k}={v}" for k, v in kv.items()), flush=True)


def first_kind(s):
    s = s.strip()
    if re.match(r"^(안녕|여러분 안녕|반갑)", s): return "인사"
    if "?" in s[:80] or re.search(r"(까요|나요|ㄹ까|습니까|인가요)", s[:80]): return "질문"
    if NUM.search(s[:40]): return "숫자"
    if re.search(r"(지금|오늘|요즘|최근|어제)", s[:30]): return "지금 상황"
    return "그 밖"


def main():
    rows = {r["id"]: r for r in csv.DictReader(open(OUT / "compare.csv", encoding="utf-8-sig"))}
    vids = []
    for p in sorted(OUT.glob("W_*/transcript.json")):
        vid = p.parent.name[2:]
        meta = rows.get(vid)
        if not meta:
            continue
        j = json.load(open(p, encoding="utf-8"))
        sn = j.get("snippets", [])
        text30 = " ".join(x["text"] for x in sn if x["start"] < 30).strip()
        if not text30:
            continue
        title = meta["title"]
        tw = [w for w in re.findall(r"[가-힣A-Za-z0-9]{2,}", title) if not w.startswith("#")]
        hit = sum(1 for w in set(tw) if w in text30) / max(1, len(set(tw)))
        age = max(1.0, float(meta["age_days"] or 1))
        vids.append({"id": vid, "title": title, "channel": meta["channel"], "subs": int(float(meta["subs"] or 0)), "views": int(float(meta["views"] or 0)),
                     "ratio": float(meta["ratio"] or 0), "vpd": round(float(meta["views"] or 0) / age), "success": meta["success"] == "True",
                     "lang": j.get("lang", ""), "relevant": bool(REL.search(title)), "intro": text30, "first": sn[0]["text"] if sn else "",
                     "kind": first_kind(sn[0]["text"] if sn else ""), "title_word_share": round(hit * 100), "nums": len(re.findall(r"\d+(?:[.,]\d+)?", text30)),
                     "questions": len(re.findall(r"\?|까요|나요|습니까", text30)), "promise": bool(PROMISE.search(text30)), "call": bool(CALL.search(text30)),
                     "chars": len(re.sub(r"\s", "", text30))})
    log("LOAD", transcripts=len(vids), success=sum(v["success"] for v in vids), relevant=sum(v["relevant"] for v in vids))
    cut = sorted(v["vpd"] for v in vids)[int(len(vids) * 0.9)] if vids else 0
    for v in vids:
        v["group"] = "성공 사례" if v["success"] else ("하루 조회수 상위" if v["vpd"] >= cut else "그 밖")

    def stats(g):
        if not g: return {}
        kinds = {}
        for v in g: kinds[v["kind"]] = kinds.get(v["kind"], 0) + 1
        return {"n": len(g), "first_kind": kinds, "title_word_share_median": statistics.median(v["title_word_share"] for v in g),
                "nums_median": statistics.median(v["nums"] for v in g), "questions_median": statistics.median(v["questions"] for v in g),
                "promise_pct": round(100 * sum(v["promise"] for v in g) / len(g)), "call_pct": round(100 * sum(v["call"] for v in g) / len(g)),
                "chars_median": statistics.median(v["chars"] for v in g)}
    res = {"vpd_cut": cut, "groups": {k: stats([v for v in vids if v["group"] == k]) for k in ("성공 사례", "하루 조회수 상위", "그 밖")},
           "relevant": {k: stats([v for v in vids if v["group"] == k and v["relevant"]]) for k in ("성공 사례", "하루 조회수 상위", "그 밖")}}
    for k, s in res["groups"].items(): log("GROUP", group=k, **{x: y for x, y in s.items() if x != "first_kind"}, kinds=s.get("first_kind"))
    (HERE / "intro_scan.json").write_text(json.dumps({"summary": res, "videos": vids}, ensure_ascii=False, indent=1), "utf-8")
    md = ["# 앞 30초 모음 — 주식 (대본 있는 영상)", "", f"자동 생성 — intro_scan.py v1.0 ({time.strftime('%Y-%m-%d %H:%M')}). ※ 시청 지속 자료 없음 · 음성인식 글자 틀림 섞임 · 연구·교육용.", ""]
    for g in ("성공 사례", "하루 조회수 상위", "그 밖"):
        sel = sorted([v for v in vids if v["group"] == g and v["relevant"]], key=lambda v: -v["ratio"])
        md += [f"## {g} — 관련 주제 {len(sel)}개", ""]
        for v in sel:
            md += [f"### {v['title']}", f"- 조회수 {v['views']:,} · 구독자 {v['subs']:,} · 배수 {v['ratio']} · 하루 {v['vpd']:,} · 첫 문장 꼴 {v['kind']} · 제목 낱말 {v['title_word_share']}% · 숫자 {v['nums']} · 질문 {v['questions']} · {v['lang']}",
                   "", "> " + v["intro"], ""]
    (HERE / "intro_30s.md").write_text("\n".join(md), "utf-8")
    log("DONE", out=HERE / "intro_30s.md", vpd_cut=cut)


if __name__ == "__main__":
    main()
