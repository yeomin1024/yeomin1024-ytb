#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-11-23 — 제목 꼴 세기 추가: 기준 통과(83) vs 같은 낱말이 든 기준 미달(같은 조건 — 7~180일·5만 이하·4분 이상·주제 관련) 영상의 꼴 몫 (`patterns`).
# (v1.0 — 2026-11-23 — 제목에 삼성전자·SK하이닉스·코스피가 든 성공 사례 조사 (사용자 지시 "삼성전자, SK하이닉스, 코스피를 제목에 포함한 성공 사례 영상 조사해봐").
#   자료 = stock/result/outliers/compare.csv (탐색에서 본 영상 전부 · 2026-11-18 받음) + analysis.json (공식 성공 사례 108).
#   성공 기준 = stock/analysis_rules.toml [success] 그대로 (7~180일 · 구독자 5만 이하 · 구독자당 하루 조회수 ≥ 0.1 · 조회수 1만 이상 · 4분 이상 · 조회수 ≥ 구독자×3)
#     · 공식 108 은 채널당 2개 · 자료 받은 것만 — 여기서는 채널 제한 없이 기준을 넘은 영상 전부도 셈 ('기준 통과').
#   낱말: 삼성전자 = 삼성전자·삼전·(바이오·SDI·생명 등이 아닌) 삼성 · 하이닉스 = 하이닉스·하닉·닉스(피닉스 뺌)·Hynix · 코스피 = 코스피·KOSPI · '삼전닉스' = 삼전+하닉 둘 다.
#   비교 = 비교 집단(compare in_compare — 5만 이하·4분·365일·주제 관련·채널당 5) 안에서 낱말이 든 제목의 성공 비율 vs 안 든 제목.
#   로그: [STAGE] [시각] key=value · 실행: python3 stock/topics/title_research_2026-11-23/kw_success.py
#   ※ 연구·교육용. 조회수 순 검색이라 잘된 영상 쪽으로 치우침 — 비율은 같은 집단 안 비교로만.
import csv, json, re, time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "stock/result/outliers"
HERE = Path(__file__).resolve().parent
SAM = re.compile(r"삼성전자|삼전|삼성(?!\s?(바이오|SDI|생명|물산|중공업|화재|증권|전기|카드|E&A|에스디에스|SDS|biologics))|Samsung", re.I)
HYN = re.compile(r"하이닉스|하닉|(?<!피)닉스|hynix", re.I)
KOS = re.compile(r"코스피|kospi", re.I)


def log(stage, **kv):
    print(f"[{stage}] [{time.strftime('%Y-%m-%dT%H:%M:%S')}] " + " ".join(f"{k}={v}" for k, v in kv.items()), flush=True)


def f(x):
    try: return float(x)
    except Exception: return 0.0


def tags(t):
    return ("S" if SAM.search(t) else "") + ("H" if HYN.search(t) else "") + ("K" if KOS.search(t) else "")


def passes(r):
    s, a, v = f(r["subs"]), f(r["age_days"]), f(r["views"])
    return (r["exclude"] == "" and 0 < s <= 50000 and 7 <= a <= 180 and v >= 10000 and f(r["minutes"]) >= 4
            and v / max(1.0, a) / s >= 0.1 and v >= 3 * s)


def main():
    rows = list(csv.DictReader(open(OUT / "compare.csv", encoding="utf-8-sig")))
    an = json.load(open(OUT / "analysis.json", encoding="utf-8"))
    official = {c["id"]: c for c in an["success_cases"]}
    log("LOAD", explored=len(rows), official=len(official))
    out = {"official": [], "criteria": [], "rates": {}}
    for r in rows:
        t = tags(r["title"])
        if not t:
            continue
        if not passes(r) and r["id"] not in official:
            continue
        a = max(1.0, f(r["age_days"]))
        item = {"id": r["id"], "tags": t, "title": r["title"], "channel": r["channel"], "subs": int(f(r["subs"])), "views": int(f(r["views"])),
                "ratio": round(f(r["ratio"]), 1), "vpd_subs": round(f(r["views"]) / a / max(1, f(r["subs"])), 2), "vpd": int(f(r["views"]) / a),
                "minutes": round(f(r["minutes"]), 1), "published": r["published"], "theme": r["theme"], "official": r["id"] in official,
                "has_case": r["has_case"] == "True", "korean": bool(re.search("[가-힣]", r["title"]))}
        out["criteria"].append(item)
        if item["official"]:
            out["official"].append(item)
    out["criteria"].sort(key=lambda x: -x["vpd_subs"])
    # 비교 집단 안 성공 비율
    comp = [r for r in rows if r["in_compare"] == "True"]
    def rate(sel):
        n = len(sel); s = sum(r["success"] == "True" and passes(r) for r in sel)
        return {"n": n, "success": s, "pct": round(100 * s / n, 1) if n else None}
    out["rates"]["all"] = rate(comp)
    for name, fn in (("삼성전자", lambda t: "S" in t), ("하이닉스", lambda t: "H" in t), ("코스피", lambda t: "K" in t),
                     ("셋 중 하나라도", lambda t: bool(t)), ("둘 이상", lambda t: len(t) >= 2), ("셋 다", lambda t: t == "SHK"), ("셋 다 없음", lambda t: not t)):
        out["rates"][name] = rate([r for r in comp if fn(tags(r["title"]))])
    PAT = {"물음표": r"\?", "결정 질문(팔아야·사도·버틸·바닥·끝인가)": r"팔아야|팔면|사도 될|살까|버틸|바닥|끝인가|끝났|어디까지",
           "이유·까닭": r"이유|왜 ", "지수·가격 숫자(천·만·P·피)": r"\d[\d,]*\s?(P|피|선|만|원)|\d천|\d만", "퍼센트·배수": r"\d+(\.\d+)?\s?%|\d+배",
           "큰 금액(조)": r"\d+조", "폭락·급락·붕괴": r"폭락|급락|붕괴|추락|무너", "사람·전문가(출연·대표·이름 따옴표)": r"출연|대표|연구원|센터장|회장|전문가|차장|이광수|존리|문남중",
           "숨긴 말(이것·이렇게·이때·이 가격·진짜)": r"'이|‘이|\"이것|진짜|숨겨|숨기", "외국인·수급": r"외국인|외인|수급", "목록 숫자(N가지)": r"\d\s?가지", "따옴표 인용": r"[\"“”'‘’]"}
    def share(sel):
        return {k: round(100 * sum(bool(re.search(v, x)) for x in sel) / len(sel), 1) if sel else None for k, v in PAT.items()}
    ok_titles = [x["title"] for x in out["criteria"]]
    fail = [r["title"] for r in rows if tags(r["title"]) and not passes(r) and r["exclude"] == "" and 0 < f(r["subs"]) <= 50000
            and 7 <= f(r["age_days"]) <= 180 and f(r["minutes"]) >= 4]
    out["patterns"] = {"pass_n": len(ok_titles), "fail_n": len(fail), "pass": share(ok_titles), "fail": share(fail)}
    for k in PAT:
        log("PATTERN", name=k, pass_pct=out["patterns"]["pass"][k], fail_pct=out["patterns"]["fail"][k])
    combo = {}
    for it in out["criteria"]:
        combo[it["tags"]] = combo.get(it["tags"], 0) + 1
    out["combo_criteria"] = combo
    out["combo_official"] = {k: sum(1 for x in out["official"] if x["tags"] == k) for k in combo}
    log("RESULT", criteria=len(out["criteria"]), official=len(out["official"]), combo=combo)
    for k, v in out["rates"].items():
        log("RATE", group=k, **v)
    (HERE / "kw_success.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), "utf-8")
    log("DONE", out=HERE / "kw_success.json")


if __name__ == "__main__":
    main()
