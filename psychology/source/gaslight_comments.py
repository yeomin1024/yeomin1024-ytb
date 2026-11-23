#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0.1 — 2026-11-23 — 고침: '시어머니·시모'가 '어머니'에도 걸려 시댁 댓글이 부모로도 세어지던 것 (relation_of —
#          시댁 낱말을 먼저 지운 뒤 나머지 관계를 찾음 · 시험 test_relation_order_and_tactics 가 잡음)
# (이전) v1.0.0 — 2026-11-23 — 신규: 심리 영상 댓글에서 '나도 모르게 가스라이팅 당했다' 경험 세기
#          (사용자 지시 2026-11-23 "그러니까 1번 심리가 초래한 실제 사례들을 찾아보라고 사람들이 모르고 있지만
#           그게 가스라이팅이 어느 순간 된거지 그런거")
"""
gaslight_comments.py — 심리 분석 승인 영상(psychology/result/outliers/W_*/comments.csv) 댓글에서
'가스라이팅'을 말한 댓글을 모아 ① 누구에게(관계) ② 나중에 알아챘나(깨달음) ③ 처음엔 잘해 줬나(평범한 시작)
④ 어떤 수법(죄책감·고립·돈·효도·무시·비교)을 셈 → result/incidents/gaslight_comments.md

흐름: LOAD(댓글 csv · 영상 metadata) → VALIDATE(빈 글·같은 댓글 id) → FEATURE(정규식 낱말 묶음) → METRICS → EXPORT
한계: 낱말이 나왔다고 그 사람이 가해자라는 뜻은 아님(대강의 크기) · 댓글을 단 영상이 '가스라이팅' 영상에 몰려 있음 ·
      작성자 이름·@아이디는 지우고 인용 · 할당량 0 (받아 둔 댓글만)
실행: python3 psychology/source/gaslight_comments.py      (LOG_LEVEL=DEBUG 로 묶음별 예시)
"""
from __future__ import annotations

import csv
import json
import logging
import os
import re
import sys
import time
from collections import Counter
from datetime import datetime
from pathlib import Path

VERSION = "v1.0.1"
HERE = Path(__file__).resolve().parent
PSY = HERE.parent
CASES = PSY / "result" / "outliers"
OUT = PSY / "result" / "incidents" / "gaslight_comments.md"
QUOTE_N = 25            # 인용할 깨달음 댓글 수 (공감 순)
QUOTE_LEN = 220

GAS = re.compile(r"가스\s?라이팅|가스라이터|가스라이트")
REALIZE = re.compile(r"몰랐|몰랐던|모르고 ?(?:살|지내|있)|이제야|이제서야|깨달|알고 ?보니|지나고 ?보니|돌이켜 ?보니|생각해 ?보니|"
                     r"그게 가스라이팅|그것도 가스라이팅|이게 가스라이팅|가스라이팅이었|가스라이팅이였|가스라이팅인 ?줄|당한 ?줄|"
                     r"당하고 ?있었|당했었|당했던|나중에 ?알")
RELATION = {   # 관계 낱말 (앞이 우선 — 시댁 낱말이 '어머니'보다 먼저 잡히게)
    "시댁": r"시어머니|시모|시댁|시부모|시누|시아버지|시가",
    "부모": r"엄마|어머니|어머님|아빠|아버지|부모|친정|모친|부친",
    "배우자": r"남편|아내|와이프|배우자|신랑",
    "연인": r"남친|여친|남자 ?친구|여자 ?친구|전남친|전여친|애인|연애|사귀",
    "형제": r"언니|오빠|누나|형이|형은|형한테|동생|자매|형제",
    "친구·지인": r"친구|지인|동창|절친",
    "직장·학교": r"상사|직장|회사|팀장|사장|부장|과장|동료|선배|교수|선생님|학원",
    "종교": r"교회|목사|종교|사이비|스님|교주|신도",
}
START_KIND = re.compile(r"(?:처음엔|처음에는|처음에|첨엔|첨에|초반엔|초반에)[^.!?\n]{0,40}?"
                        r"(?:잘해|친절|챙겨|다정|상냥|걱정|도와|위로|칭찬|친한 ?척|좋은 ?사람|착한)")
TACTICS = {
    "죄책감": r"죄책감|미안하게|미안해야|나쁜 ?(?:년|놈|사람|딸|아들|며느리)|탓을|탓으로|내 탓|네 탓|니 탓",
    "고립": r"고립|못 ?만나게|연락(?:을)? ?끊|이간질|갈라놓|친구를 ?끊|혼자 ?만들",
    "돈": r"돈을?|재산|빚|대출|용돈|빌려",
    "효도·도리": r"효도|효녀|효자|도리|천륜|은혜|키워 ?줬|키워준",
    "무시·깎아내림": r"무시|깎아내|자존감 ?(?:도둑|바닥|낮)|등신|바보 ?취급|한심",
    "비교": r"비교|누구는|남의 집",
    "통제·감시": r"통제|감시|간섭|허락|위치|검사|보고하",
}
HANDLE = re.compile(r"@[\w가-힣.\-]+")

log = logging.getLogger("gaslight_comments")


def L(stage: str, level: int = logging.INFO, **kv) -> None:
    msg = " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if not isinstance(v, str) or ' ' in v else v}"
                   for k, v in kv.items())
    log.log(level, msg, extra={"stage": stage})


class F(logging.Formatter):
    def format(self, r):
        lv = "" if r.levelno == logging.INFO else f" level={r.levelname}"
        return f"[{getattr(r, 'stage', 'MAIN')}] [{datetime.now():%Y-%m-%dT%H:%M:%S}]{lv} {r.getMessage()}"


def load() -> tuple[list[dict], dict]:
    rows, meta = [], {}
    for d in sorted(CASES.glob("W_*")):
        vid = d.name[2:]
        m = d / "metadata.json"
        if m.exists():
            try:
                j = json.loads(m.read_text(encoding="utf-8"))
                meta[vid] = {"title": j.get("title", ""), "views": j.get("view_count") or j.get("views")}
            except json.JSONDecodeError:
                L("LOAD", logging.WARNING, file=str(m), error="metadata json", next_step="그 사례 폴더 다시 받기")
        c = d / "comments.csv"
        if not c.exists():
            continue
        with open(c, encoding="utf-8-sig") as fh:
            for r in csv.DictReader(fh):
                rows.append({"vid": vid, "id": r.get("id"), "likes": int(r.get("likes") or 0),
                             "is_reply": r.get("is_reply") == "True", "creator": r.get("creator") == "True",
                             "published": r.get("published", ""), "text": r.get("text") or ""})
    L("LOAD", source="psychology/result/outliers/W_*/comments.csv", videos=len(meta), comments=len(rows),
      date_range=f"{min((r['published'] for r in rows if r['published']), default='-')[:10]}~"
                 f"{max((r['published'] for r in rows if r['published']), default='-')[:10]}")
    return rows, meta


def validate(rows: list[dict]) -> list[dict]:
    seen, out, empty, dup, creator = set(), [], 0, 0, 0
    for r in rows:
        if not r["text"].strip():
            empty += 1
            continue
        if r["id"] in seen:
            dup += 1
            continue
        if r["creator"]:
            creator += 1          # 영상 주인 댓글은 경험담이 아님
            continue
        seen.add(r["id"])
        out.append(r)
    L("VALIDATE", rows_in=len(rows), drop_empty=empty, drop_duplicate_id=dup, drop_creator=creator, rows_out=len(out))
    return out


def relation_of(text: str) -> list[str]:
    """v1.0.1: 시댁 낱말(시어머니 등)을 먼저 지운 뒤 나머지를 찾음 — '어머니'로 부모가 또 잡히지 않게."""
    out = []
    if re.search(RELATION["시댁"], text):
        out.append("시댁")
        text = re.sub(RELATION["시댁"], " ", text)
    out += [k for k, p in RELATION.items() if k != "시댁" and re.search(p, text)]
    return out


def features(rows: list[dict]) -> list[dict]:
    g = []
    for r in rows:
        t = r["text"]
        if not GAS.search(t):
            continue
        r = dict(r)
        r["realize"] = bool(REALIZE.search(t))
        r["rel"] = relation_of(t)
        r["start_kind"] = bool(START_KIND.search(t))
        r["tactics"] = [k for k, p in TACTICS.items() if re.search(p, t)]
        g.append(r)
    L("FEATURE", rule="GAS in text", gas_comments=len(g), realize=sum(r["realize"] for r in g),
      start_kind=sum(r["start_kind"] for r in g), videos=len({r["vid"] for r in g}))
    return g


def clean(t: str) -> str:
    return HANDLE.sub("@…", t.replace("\n", " ").replace("|", "／")).strip()[:QUOTE_LEN]


def export(g: list[dict], meta: dict, total: int, t0: float) -> None:
    rel_all, rel_real, tac_all, tac_real = Counter(), Counter(), Counter(), Counter()
    for r in g:
        rel_all.update(r["rel"] or ["(관계 낱말 없음)"])
        tac_all.update(r["tactics"])
        if r["realize"]:
            rel_real.update(r["rel"] or ["(관계 낱말 없음)"])
            tac_real.update(r["tactics"])
    vids = Counter(r["vid"] for r in g)
    real = [r for r in g if r["realize"]]
    w = []
    w.append("# 심리 영상 댓글 — '나도 모르게 가스라이팅 당했다' 경험")
    w.append("")
    w.append(f"VERSION: {VERSION} — 도구 `psychology/source/gaslight_comments.py` · 사용자 지시 2026-11-23 \"그러니까 1번 심리가 "
             "초래한 실제 사례들을 찾아보라고 사람들이 모르고 있지만 그게 가스라이팅이 어느 순간 된거지 그런거\"")
    w.append("")
    w.append("## 0. 읽는 법·한계")
    w.append(f"- 자료: 심리 분석 승인 영상 {len(meta)}개의 받아 둔 댓글 {total:,}개(답글 포함, 영상 주인 댓글 뺌) 중 "
             f"'가스라이팅'이 들어간 {len(g):,}개 · 그 영상 {len(vids)}개.")
    w.append("- **깨달음** = '몰랐다·이제야·알고 보니·그게 가스라이팅이었다·당한 줄' 같은 말이 같이 나온 댓글.")
    w.append("- **관계** = 댓글에 나온 관계 낱말 (한 댓글에 여럿이면 각각 셈). 낱말이 나왔다고 그 사람이 가해자라는 뜻은 아님 — 대강의 크기.")
    w.append("- 인용은 작성자 이름·@아이디를 지움. 숫자·원문만, 해석은 `incident_cases.md` 9번·`source/gaslighting_cases.md`.")
    w.append("")
    w.append("## 1. 누구에게 — 관계 낱말")
    w.append("")
    w.append("| 관계 | 가스라이팅 댓글 | 그중 깨달음 댓글 |")
    w.append("|---|---|---|")
    for k, v in rel_all.most_common():
        w.append(f"| {k} | {v} | {rel_real.get(k, 0)} |")
    w.append("")
    w.append(f"- 깨달음 댓글 {len(real)}개 · 그중 '처음엔 잘해 줬다' 꼴(처음엔 + 잘해·친절·챙겨·걱정·칭찬…) "
             f"{sum(r['start_kind'] for r in real)}개 (가스라이팅 댓글 전체로는 {sum(r['start_kind'] for r in g)}개)")
    w.append("")
    w.append("## 2. 어떤 수법 — 같이 나온 낱말")
    w.append("")
    w.append("| 수법 | 가스라이팅 댓글 | 그중 깨달음 댓글 |")
    w.append("|---|---|---|")
    for k, v in tac_all.most_common():
        w.append(f"| {k} | {v} | {tac_real.get(k, 0)} |")
    w.append("")
    w.append("## 3. 댓글이 많이 달린 영상 (가스라이팅 댓글 수)")
    w.append("")
    w.append("| 영상 | 가스라이팅 댓글 | 깨달음 |")
    w.append("|---|---|---|")
    for v, c in vids.most_common(10):
        t = meta.get(v, {}).get("title", v)
        w.append(f"| [{clean(t)[:70]}](https://youtu.be/{v}) | {c} | {sum(1 for r in real if r['vid'] == v)} |")
    w.append("")
    w.append(f"## 4. 깨달음 댓글 — 공감 순 {QUOTE_N}개 (원문, 이름·@아이디 지움)")
    w.append("")
    w.append("| 공감 | 관계 | 처음엔 잘해 줌 | 수법 | 댓글 |")
    w.append("|---|---|---|---|---|")
    for r in sorted(real, key=lambda r: -r["likes"])[:QUOTE_N]:
        w.append(f"| {r['likes']} | {'·'.join(r['rel']) or '-'} | {'예' if r['start_kind'] else ''} | "
                 f"{'·'.join(r['tactics']) or '-'} | {clean(r['text'])} |")
    w.append("")
    w.append(f"_실행 {time.time() - t0:.1f}초 · 할당량 0_")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(w) + "\n", encoding="utf-8")
    L("EXPORT", md=str(OUT.relative_to(PSY.parent)), relations=dict(rel_all.most_common()),
      realize_relations=dict(rel_real.most_common()), tactics=dict(tac_all.most_common()))


def main() -> int:
    h = logging.StreamHandler(sys.stdout)
    h.setFormatter(F())
    log.handlers[:] = [h]
    log.setLevel(os.environ.get("LOG_LEVEL", "INFO").upper())
    t0 = time.time()
    L("START", tool=f"gaslight_comments.py {VERSION}", quota=0)
    rows, meta = load()
    if not rows:
        L("LOAD", logging.WARNING, error="댓글 0개", next_step="git pull 로 psychology/result/outliers/W_* 받기")
        return 1
    ok = validate(rows)
    g = features(ok)
    export(g, meta, len(ok), t0)
    L("RESULT", seconds=round(time.time() - t0, 2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
