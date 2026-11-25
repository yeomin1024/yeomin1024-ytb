#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-11-25 — 새로: 트렌드 낱말 근거표 (사용자 지시 2026-11-25 "역사 주제에서 한 것 처럼 재테크 하위 주제(경제, 주식 등등) 키워드들을 모두 찾아서 트렌드 코드 실행 명령 알려줘").
#   <주제>/next_topic.toml [trends] WORDS 마다 — 우리 분석 자료(compare.csv 제목)에 몇 번 나왔나 · 실제 영상 태그(tag_candidates.csv)로 몇 개 영상에 붙었나.
#   자료 주제를 여러 개 줄 수 있음 (재테크 = economic + stock). 결과 = <주제>/result/next_topic/keywords.md
#   실행: python3 tools/trend_keywords.py economic --from economic stock
#   ※ 연구·교육용. 숫자는 우리가 탐색에서 본 영상 안의 횟수 (검색 수가 아님 — 관심도는 구글 트렌드로).
import argparse, csv, re, time, tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def log(stage, **kv):
    print(f"[{stage}] [{time.strftime('%Y-%m-%dT%H:%M:%S')}] " + " ".join(f"{k}={v}" for k, v in kv.items()), flush=True)


def norm(s):
    return re.sub(r"\s", "", (s or "").lower())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("topic")
    ap.add_argument("--from", dest="src", nargs="+", default=None, help="제목·태그를 읽을 주제 폴더 (기본 = topic)")
    a = ap.parse_args()
    cfg = tomllib.loads((ROOT / a.topic / "next_topic.toml").read_text("utf-8"))
    words, anchor = cfg["trends"]["WORDS"], cfg["trends"]["ANCHOR"]
    titles, tags, nvid = [], {}, 0
    for t in a.src or [a.topic]:
        cp = ROOT / t / "result/outliers/compare.csv"
        if cp.exists():
            rows = list(csv.DictReader(open(cp, encoding="utf-8-sig")))
            titles += [norm(r["title"]) for r in rows]
            nvid += len(rows)
        tp = ROOT / t / "tag_candidates.csv"
        if tp.exists():
            for r in csv.DictReader(open(tp, encoding="utf-8-sig")):
                tags[norm(r["tag"])] = tags.get(norm(r["tag"]), 0) + int(r["videos"] or 0)
    log("LOAD", topic=a.topic, src=a.src or [a.topic], titles=len(titles), tags=len(tags), words=len(words))
    batches = [[anchor] + words[i:i + 4] for i in range(0, len(words), 4)]
    L = [f"# 트렌드 낱말 근거 — {cfg.get('name', a.topic)} ({time.strftime('%Y-%m-%d')})", "",
         f"> `tools/trend_keywords.py` v1.0 · 설정 `{a.topic}/next_topic.toml` [trends] · 자료 = {', '.join(a.src or [a.topic])} 탐색 영상 {nvid:,}개 제목 · 실제 영상 태그.",
         "> '제목' = 그 낱말이 든 제목 수 · '태그' = 그 태그가 붙은 영상 수 (우리가 본 영상 안 — 검색 수 아님). 관심도 순위는 구글 트렌드 받은 뒤 `trends.md`.", "",
         f"기준 낱말 「{anchor}」 — 제목 {sum(1 for x in titles if norm(anchor) in x):,} · 태그 {tags.get(norm(anchor), 0):,}", "",
         "| 묶음 | 낱말 | 제목 | 태그 |", "|---|---|---|---|"]
    for i, b in enumerate(batches, 1):
        for w in b[1:]:
            L.append(f"| {i:02d} | {w} | {sum(1 for x in titles if norm(w) in x):,} | {tags.get(norm(w), 0):,} |")
    out = ROOT / a.topic / "result/next_topic/keywords.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    log("DONE", out=out.relative_to(ROOT), batches=len(batches))


if __name__ == "__main__":
    main()
