#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-28 — 최초. 반론에 특화된 시청자 페르소나 — 실제 댓글 중 반박·비판(내용에 대한 반론)만 모아 갈래·좋아요·대표 문장 →
#          대본 검토용 질문 (사용자 지시 2026-10-28 "애매한게 있으면 반론이 들어온다고 명확한걸로 수정해보고 반론에 특화된 페르소나 만들어서
#          대본 피드백하고 다시 수정하고 계속 반복해서 결과 내도록 해"). 같은 꼴: comment_title_ideas.py (후보 → Claude 가 고름 → 정리).
#
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.0 | 2026-10-28 | 최초 — candidates · build | cmd_candidates · cmd_build · main |
#
# 실행:
#   python3 tools/rebuttal_persona.py stock candidates   # <주제>/result/outliers/rebuttal_candidates.tsv (좋아요 순 · 낱말로 어림한 갈래)
#   (Claude 가 후보를 읽고 내용 반론만 갈래를 붙여 rebuttal_picks.tsv — cid · kind(K1~K8) · note)
#   python3 tools/rebuttal_persona.py stock build        # <주제>/result/outliers/rebuttal_persona.md · .json
# 설정: <주제>/rebuttal.toml (갈래·찾을 낱말·검토 질문). 네트워크 없음. 댓글 파일에 작성자 이름·채널 ID 는 넣지 않음 (CLAUDE.md).
# ※ 연구·교육용 — 투자 권유가 아님.
import argparse
import csv
import json
import logging
import re
import sys
import time
import tomllib
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
import comment_types as ct  # noqa: E402  viewer_comments · classify · clean (같은 댓글·같은 유형 규칙)

VERSION = "v1.0"
log = logging.getLogger("rebuttal_persona")


class StageFormatter(logging.Formatter):
    def format(self, record):
        return f"[{getattr(record, 'stage', 'RB')}] [{self.formatTime(record, '%Y-%m-%dT%H:%M:%S')}] {record.getMessage()}"


def out(stage, **kv):
    log.info(" ".join(f"{k}={v}" for k, v in kv.items()), extra={"stage": stage})


def settings(topic):
    p = ROOT / topic / "rebuttal.toml"
    try:
        s = tomllib.loads(p.read_text("utf-8"))
    except (OSError, tomllib.TOMLDecodeError) as e:
        log.error(f"file={p} error={e!r} next_step=설정 파일을 만들거나 고침 (stock/rebuttal.toml 꼴)", extra={"stage": "LOAD"})
        raise SystemExit(1)
    out("LOAD", settings=p.relative_to(ROOT), kinds=len(s["kind"]))
    return s


def paths(topic):
    od = ROOT / topic / "result" / "outliers"
    return od, od / "rebuttal_candidates.tsv", od / "rebuttal_picks.tsv"


def cmd_candidates(topic):
    s = settings(topic)
    c = s["candidates"]
    od, cand_p, _ = paths(topic)
    rows = [r for r in ct.viewer_comments(od) if r["lang_group"] == c["LANG"] and len(r["text"].strip()) >= c["MIN_CHARS"]]
    dis = re.compile(c["DISAGREE"])
    kinds = [(k["code"], re.compile(k["pattern"])) for k in s["kind"]]
    picked, types = [], Counter()
    for r in rows:
        t = ct.classify(r["text"])
        types[t] += 1
        if t in c["SKIP_TYPES"]:
            continue
        guess = [code for code, rx in kinds if rx.search(r["text"])]
        if (t == "C" or guess) and dis.search(r["text"]):
            picked.append({**r, "rule_type": t, "guess": ",".join(guess) or "-"})
    picked.sort(key=lambda r: (-r["likes"], r["cid"]))
    top = picked[:c["TOP"]]
    with cand_p.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["cid", "video_id", "likes", "is_reply", "rule_type", "guess", "text"])
        for r in top:
            w.writerow([r["cid"], r["video_id"], r["likes"], r["reply"], r["rule_type"], r["guess"], ct.clean(r["text"], 240)])
    out("CANDIDATES", topic=topic, comments=len(rows), rule_types=dict(types.most_common()), matched=len(picked), written=len(top),
        file=cand_p.relative_to(ROOT), next_step="Claude 가 읽고 rebuttal_picks.tsv (cid·kind·note) → build")
    return {"comments": len(rows), "matched": len(picked), "written": len(top)}


def cmd_build(topic):
    s = settings(topic)
    od, cand_p, picks_p = paths(topic)
    try:
        cand = {r["cid"]: r for r in csv.DictReader(cand_p.open(encoding="utf-8"), delimiter="\t")}
        picks = list(csv.DictReader(picks_p.open(encoding="utf-8"), delimiter="\t"))
    except OSError as e:
        log.error(f"error={e!r} next_step=candidates 를 먼저, 그다음 Claude 가 rebuttal_picks.tsv", extra={"stage": "LOAD"})
        raise SystemExit(1)
    names = {k["code"]: k for k in s["kind"]}
    bad = [p["cid"] for p in picks if p["cid"] not in cand or p["kind"] not in names]
    if bad:
        log.warning(f"unknown_picks={bad[:5]} n={len(bad)} note=후보에 없는 cid 또는 모르는 갈래 — 뺌", extra={"stage": "CHECK"})
    picks = [p for p in picks if p["cid"] in cand and p["kind"] in names]
    by = defaultdict(list)
    for p in picks:
        by[p["kind"]].append({**cand[p["cid"]], "note": p.get("note", "")})
    total_likes = sum(int(cand[p["cid"]]["likes"]) for p in picks) or 1
    kinds = []
    for code, k in names.items():
        xs = sorted(by.get(code, []), key=lambda r: -int(r["likes"]))
        kinds.append({"code": code, "name": k["name"], "question": k["question"], "n": len(xs), "share": len(xs) / max(len(picks), 1),
                      "likes": sum(int(r["likes"]) for r in xs), "like_share": sum(int(r["likes"]) for r in xs) / total_likes,
                      "examples": [{"likes": int(r["likes"]), "text": r["text"], "note": r["note"]} for r in xs[:4]]})
    kinds.sort(key=lambda k: (-k["likes"], -k["n"]))
    data = {"version": VERSION, "topic": topic, "made": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "candidates": len(cand), "picks": len(picks), "kinds": kinds}
    (od / "rebuttal_persona.json").write_text(json.dumps(data, ensure_ascii=False, indent=1), "utf-8")
    write_md(od / "rebuttal_persona.md", data)
    out("BUILD", topic=topic, picks=len(picks), kinds=" ".join(f"{k['code']}={k['n']}" for k in kinds), file=(od / "rebuttal_persona.md").relative_to(ROOT))
    return data


def write_md(path, d):
    L = [f"# {d['topic']} 반론 페르소나 — 내용에 반박하는 시청자 (실제 댓글에서)", "",
         f"`tools/rebuttal_persona.py {d['version']}` · 만든 때 {d['made']} · 후보 {d['candidates']}개(좋아요 순) 중 Claude 가 **내용에 대한 반론**만 고름 "
         f"{d['picks']}개 (`rebuttal_picks.tsv`) · 설정 `{d['topic']}/rebuttal.toml`. 손으로 고치지 않음.",
         "※ 연구·교육용. 댓글 원문은 작성자 이름 없이.", "",
         "## 0. 한눈에 — 이 페르소나는 누구인가", "",
         "- **누구**: 영상의 결론보다 *빈틈*을 먼저 찾는 시청자. 정치·인물 비난·광고가 아니라 **내용**(조건·기간·숫자·비용·현실성·모순)에 댓글로 반박한다.",
         "- **어떻게 읽나**: 보기마다 '상황에 따라 다르지 않나?' · 숫자마다 '그 기간만 그런 것 아닌가?' · 해설마다 '앞에서 한 말과 다르지 않나?'.",
         "- **떠나는 까닭**: 애매한 정답·고른 기간·빠진 비용·과장 — 반박 댓글이 좋아요를 받으면 다른 시청자의 믿음도 깎인다.", "",
         "| 갈래 | 고른 댓글 | 몫 | 좋아요 | 좋아요 몫 | 대본 검토 질문 |", "|---|---|---|---|---|---|"]
    for k in d["kinds"]:
        L.append(f"| {k['code']} {k['name']} | {k['n']} | {k['share']:.0%} | {k['likes']:,} | {k['like_share']:.0%} | {k['question']} |")
    L += ["", "## 1. 갈래별 대표 댓글 (좋아요 순, 원문)", ""]
    for k in d["kinds"]:
        L.append(f"### {k['code']} {k['name']} — {k['n']}개 · 👍{k['likes']:,}")
        for e in k["examples"]:
            L.append(f"- 👍{e['likes']} \"{e['text']}\"" + (f" — *{e['note']}*" if e["note"] else ""))
        if not k["examples"]:
            L.append("- 근거 없음 (고른 댓글 0)")
        L.append("")
    L += ["## 2. 쓰는 곳", "",
          "- 대본 검토: 이 문서 0번 표의 질문으로 대본을 문장마다 공격 → 상·중·하 → 고침 → 다시 (편 폴더 `대본_반론_검토.md`).",
          "- 반론은 **자료로 답할 수 있는 것**(calc 로 확인)과 **말로 선을 그어야 하는 것**(뺀 조건 밝히기)으로 나눠 고친다 — 자료 없이 반론을 '인정'만 하지 않는다.", "",
          "## 3. 한계", "",
          "- 후보는 낱말 규칙 + 유형 규칙(정확도 약 45%)으로 찾고, 갈래는 한 사람(Claude)이 붙였다 — 갈래 몫은 대강의 크기.",
          "- 반박 댓글은 대개 *다른* 영상(전망·종목 추천)에 달린 것이라, 데이터 테스트 영상에 들어올 반론과 꼭 같지는 않다.",
          "- 좋아요는 그 영상 크기에 따라 다르다 (큰 채널 댓글이 좋아요가 많음)."]
    path.write_text("\n".join(L) + "\n", "utf-8")


def main():
    ap = argparse.ArgumentParser(description="반론 페르소나 (연구·교육용)")
    ap.add_argument("topic")
    ap.add_argument("cmd", choices=["candidates", "build"])
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args()
    h = logging.StreamHandler(sys.stdout)
    h.setFormatter(StageFormatter())
    log.addHandler(h)
    log.setLevel(a.log_level)
    t0 = time.time()
    res = cmd_candidates(a.topic) if a.cmd == "candidates" else cmd_build(a.topic)
    out("DONE", cmd=a.cmd, seconds=f"{time.time() - t0:.1f}", result=len(res) if isinstance(res, dict) else "-")


if __name__ == "__main__":
    main()
