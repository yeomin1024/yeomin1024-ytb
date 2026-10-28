#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.2 — 2026-10-28 — 주제 인자 (재테크도 — 사용자 지시 2026-10-28 "주식 주제 관련 세션에서 했던것처럼 똑같은 방식으로 진행해서 유튜브 분석부터
#          요약본까지 만들어봐"): 편 목록·쓰지 않는 말·쇼츠 제목에서 뺄 말·평가판 이름 = <주제>/topics/settings.toml [summary] (없으면 주식 기본값 그대로).
#          제목·썸네일 문구에서 피할 말 TITLE_BANNED · 썸네일 보조 = 꼬리표 낱말(SUB_ITEMS·SUB_ITEM_MAX).
#          주제를 빼면 stock (옛 명령 그대로 됨). 영향: configure()·paths()·ep_paths()·lint_answer()·PAGE·write_material()·main().
# (v1.1) — 2026-10-28 — 요약본_material.md 맨 위 '0. 채널 설명' (stock/guides/channel.md '한눈에' — topic_ideas.channel_lines) — 사용자 지시 2026-10-28
#          "유튜브 채널 설명이니깐 여기에 맞게 영상 만들어야해 이 내용 파일 생성해서 참고할수 있게해".
# (v1.0) — 2026-10-28 — 새로: 주식 편 요약본 = 핵심 방향 + 안 5개 (롱폼·쇼츠 제목·썸네일 주요·보조 문구·대본 진행), 좋음·나쁨을 배워 다음 안으로
#          (사용자 지시 2026-10-28 "요약본 파일을 생성해야해 … 주제 탐색 후 어떻게 할건지 핵심 방향만 작성, 그리고 출처는 주석으로 달고 지시사항이나 출처 등
#          영상 외 자료는 쓰지 말것, 또한 각각 5개씩 생성 후 좋다고, 나쁘다고 표시 가능하도록 해서 그걸 학습 후 좋은 안으로 생성하도록 · 1. 롱폼 제목·썸네일
#          주요 문구, 보조 문구·대본 진행 방식 및 내용 2. 쇼츠 같음" + "대본 완성된 1개 빼고 3개만").
#          · 안 글은 Claude 가 <편 폴더>/요약본_안.json 에 쓴다 (칸마다 글 + 갈래 꼬리표) — 이 도구는 검사하고·요약본.txt 를 만들고·평가를 배운다.
#          · 요약본.txt 본문 = 영상 내용만 ([방향] + [N안]). 출처·평가·검사 = '#' 주석 줄.
#          · 평가 = stock/topics/요약본_평가.txt ('F2-LT 좋음 까닭' · 'F2 나쁨' = 안 전체) ← 요약본 줄 끝 '=> 좋음' · 평가판 페이지(import) · 채팅(mark).
#          · 배우기 = 칸 종류마다 꼬리표의 log((좋음+1)/(나쁨+1)) + 닮은 좋음/나쁨 글 → 안 점수 · [추천 조합] (칸마다 가장 좋은 글).
#          ※ 연구·교육용 — 투자 권유가 아님.
"""편 요약본 — 핵심 방향 + 안 5개 · 좋음·나쁨을 배움 (주식·재테크)

  python3 tools/summary_ideas.py [주제] status                 # 요약본 줄 끝 '=> 좋음' 가져오기 → 점수 → 편마다 요약본.txt · 평가판 · material 다시
  python3 tools/summary_ideas.py [주제] mark F2-LT 좋음 "까닭"   # 칸 하나 (F2 = 안 전체)
  python3 tools/summary_ideas.py [주제] import <marks 파일>      # 평가판(Artifact db 'marks') → 평가 파일
  python3 tools/summary_ideas.py [주제] add <영상ID> <round.json> # 새 안 5개 (다음 회차) — 검사 → 요약본 다시
  주제 = stock(기본) · economic — 편 목록은 <주제>/topics/settings.toml [summary] EPISODES (글자 = 안 ID 머리)
칸: LT 롱폼 제목 · LM 롱폼 썸네일 주요 · LS 롱폼 썸네일 보조 · LF 롱폼 대본 진행 · ST/SM/SS/SF 쇼츠 같음
로그: [STAGE] [시각] key=value (START·LOAD·SYNC·CHECK·LEARN·WRITE·DONE)
"""
import argparse
import json
import logging
import math
import re
import sys
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import title_fit                       # noqa: E402  제목이 모든 화면에서 2줄 안인가
import topic_ideas as ti               # noqa: E402  toks · jacc · GOOD · BAD (같은 낱말 규칙)

VERSION = "v1.2"
ROOT = Path(__file__).resolve().parent.parent
LOG = logging.getLogger("summary")
COMMANDS = ("status", "mark", "import", "add")
# 주제별 설정 — <주제>/topics/settings.toml [summary] 가 있으면 그것 (configure)
DEFAULTS = {"stock": {"NAME": "주식",
                      "EPISODES": {"F": "jaemu-test-2026-10", "P": "portfolio-test-2026-10", "M": "timing-test-2026-10"},   # 대본이 끝난 simri-test 는 뺌 (사용자 지시)
                      "BANNED": r"물타기|빚투|국장|미장|개미|존버|떡상|떡락|실패한",      # quick_test 7·8번 (외국 시청자 자동 번역 · '실패할')
                      "TITLE_BANNED": "", "SHORTS_TITLE_BANNED": "", "SUB_ITEMS": 0, "SUB_ITEM_MAX": 0}}
TOPIC = "stock"
NAME = DEFAULTS["stock"]["NAME"]
EPISODES = dict(DEFAULTS["stock"]["EPISODES"])
SHORTS_TITLE_BANNED = None
TITLE_BANNED = None
SUB_ITEMS, SUB_ITEM_MAX = 0, 0
ELEMS = [("LT", "롱폼", "제목"), ("LM", "롱폼", "썸네일 주요"), ("LS", "롱폼", "썸네일 보조"), ("LF", "롱폼", "대본"),
         ("ST", "쇼츠", "제목"), ("SM", "쇼츠", "썸네일 주요"), ("SS", "쇼츠", "썸네일 보조"), ("SF", "쇼츠", "대본")]
ENAME = {c: f"{a} {b}" for c, a, b in ELEMS}
BANNED = re.compile(DEFAULTS["stock"]["BANNED"])
MARKS_HEAD = """# __NAME__ 편 요약본 안 평가 — 줄마다 '안ID 좋음|나쁨 까닭(선택)'. 칸 하나는 'F2-LT 좋음', 안 전체는 'F2 나쁨'. 'F2-LT 지움' = 취소.
# 칸: LT 롱폼 제목 · LM 롱폼 썸네일 주요 · LS 롱폼 썸네일 보조 · LF 롱폼 대본 · ST 쇼츠 제목 · SM 쇼츠 썸네일 주요 · SS 쇼츠 썸네일 보조 · SF 쇼츠 대본
# 요약본.txt 줄 끝에 '=> 좋음' 을 적어도 되고 (다음 status 때 여기로 옮김), Claude 에게 말해도 된다. 같은 칸은 마지막 줄이 이김.
"""


def log(stage, _lvl=logging.INFO, **kv):
    LOG.log(_lvl, "[%s] [%s] %s", stage, datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S"),
            " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) and (' ' in v or not v) else v}" for k, v in kv.items()))


def configure(topic="stock", root=None):
    """주제 설정 읽기 — <주제>/topics/settings.toml [summary] (없으면 DEFAULTS). 모듈 전역(EPISODES·BANNED·ID_RX …)을 바꿈."""
    global TOPIC, NAME, EPISODES, BANNED, TITLE_BANNED, SHORTS_TITLE_BANNED, SUB_ITEMS, SUB_ITEM_MAX, ID_RX
    cfg = dict(DEFAULTS.get(topic) or {})
    st = Path(root or ROOT) / topic / "topics" / "settings.toml"
    if st.is_file():
        cfg.update(ti.tomllib.loads(st.read_text("utf-8")).get("summary") or {})
    if not cfg.get("EPISODES"):
        raise SystemExit(f"{topic}: 편 목록 없음 — {st} 에 [summary] EPISODES = {{F = \"<영상ID>\"}}")
    TOPIC, NAME = topic, cfg.get("NAME") or topic
    EPISODES = dict(cfg["EPISODES"])
    BANNED = re.compile(cfg.get("BANNED") or r"(?!x)x")
    SHORTS_TITLE_BANNED = re.compile(cfg["SHORTS_TITLE_BANNED"]) if cfg.get("SHORTS_TITLE_BANNED") else None
    TITLE_BANNED = re.compile(cfg["TITLE_BANNED"]) if cfg.get("TITLE_BANNED") else None
    SUB_ITEMS, SUB_ITEM_MAX = int(cfg.get("SUB_ITEMS") or 0), int(cfg.get("SUB_ITEM_MAX") or 0)
    letters = "".join(sorted(EPISODES))
    ID_RX = re.compile(rf"^([{letters}]\d+)(?:-(LT|LM|LS|LF|ST|SM|SS|SF))?$")
    log("LOAD", topic=topic, episodes=" ".join(f"{k}={v}" for k, v in EPISODES.items()), settings=str(st.relative_to(Path(root or ROOT))) if st.is_file() else "-")


def paths(root=None):
    base = Path(root or ROOT) / TOPIC
    return {"base": base, "marks": base / "topics" / "요약본_평가.txt", "page": base / "topics" / "요약본_평가판.html",
            "material": base / "topics" / "요약본_material.md", "settings": base / "topics" / "settings.toml"}


def ep_paths(vid, root=None):
    d = Path(root or ROOT) / TOPIC / "source" / vid
    return d, d / "요약본_안.json", d / "요약본.txt"


def load_ep(vid, root=None):
    d, j, _ = ep_paths(vid, root)
    return json.loads(j.read_text("utf-8"))


def save_ep(vid, E, root=None):
    _, j, _ = ep_paths(vid, root)
    j.write_text(json.dumps(E, ensure_ascii=False, indent=1), "utf-8")


def sha(t):
    import hashlib
    return hashlib.sha1(t.encode("utf-8")).hexdigest()[:16]


def norm_render(t):
    """비교용: 줄 끝 '=> 좋음…' 평가 표시와 끝 빈 줄을 뺀 글 (평가만 적은 파일은 '고치지 않음'으로 봄)."""
    return "\n".join(re.sub(r"\s*=>\s*(좋음|좋아|나쁨|별로|👍|👎).*$", "", ln).rstrip() for ln in t.splitlines()).strip()


def text_of(el):
    t = el.get("text")
    return " ".join(t) if isinstance(t, list) else str(t or "")


# ---------------------------------------------------------------- 평가
ID_RX = re.compile(r"^([FPM]\d+)(?:-(LT|LM|LS|LF|ST|SM|SS|SF))?$")


def read_marks(P):
    marks = {}
    if not P["marks"].is_file():
        return marks
    for ln in P["marks"].read_text("utf-8").splitlines():
        ln = re.sub(r"\s+#.*$", "", ln.strip())
        if not ln or ln.startswith("#"):
            continue
        m = re.match(r"(\S+)\s+(\S+)\s*(.*)$", ln)
        if not m or not ID_RX.match(m.group(1)):
            continue
        if m.group(2) in ("지움", "취소"):
            marks.pop(m.group(1), None)
            continue
        v = "좋음" if ti.GOOD.match(m.group(2)) or m.group(2) in ("좋아요",) else ("나쁨" if ti.BAD.match(m.group(2)) else None)
        if v:
            marks[m.group(1)] = {"rating": v, "why": m.group(3).strip()}
    return marks


def append_marks(P, lines):
    if not lines:
        return
    new = not P["marks"].is_file()
    with open(P["marks"], "a", encoding="utf-8") as f:
        if new:
            f.write(MARKS_HEAD.replace("__NAME__", NAME))
        f.write("\n".join(lines) + "\n")


def element_rating(marks, aid, code):
    """칸 평가 — 칸에 따로 있으면 그것, 없으면 안 전체 평가."""
    return marks.get(f"{aid}-{code}") or marks.get(aid)


def sync_file_marks(P, root=None):
    """요약본.txt 줄 끝 '=> 좋음 까닭' → 평가 파일 (렌더한 글에는 '=>' 가 없음 — 사용자가 적은 것만)."""
    lines = []
    for code, vid in EPISODES.items():
        _, _, txt = ep_paths(vid, root)
        if not txt.is_file():
            continue
        for ln in txt.read_text("utf-8").splitlines():
            m = re.search(r"=>\s*(좋음|좋아|나쁨|별로|👍|👎)\s*(.*)$", ln)
            if not m:
                continue
            letters = "".join(sorted(EPISODES))
            idm = re.search(rf"\(([{letters}]\d+-(?:LT|LM|LS|LF|ST|SM|SS|SF))\)", ln) or re.search(rf"\[\d+안 ([{letters}]\d+)\]", ln)
            if idm:
                v = "좋음" if m.group(1) in ("좋음", "좋아", "👍") else "나쁨"
                lines.append(f"{idm.group(1)} {v} {m.group(2).strip()}".rstrip() + "  # 요약본에 적음")
    append_marks(P, lines)
    log("SYNC", from_file=len(lines))
    return len(lines)


# ---------------------------------------------------------------- 검사
def lint_answer(a):
    probs = []
    for code, kind, name in ELEMS:
        el = a.get(code)
        if not el or not text_of(el):
            probs.append(f"{code} 없음")
            continue
        t = text_of(el)
        b = BANNED.search(t)
        if b:
            probs.append(f"{code} 쓰지 않는 말 '{b.group(0)}'")
        tb = TITLE_BANNED.search(t) if TITLE_BANNED and code in ("LT", "ST", "LM", "SM") else None
        if tb:
            probs.append(f"{code} 제목·썸네일 문구에서 피할 말 '{tb.group(0)}'")
        if code in ("LT", "ST"):
            ok, _ = title_fit.fit(t, shorts=(code == "ST"))
            if not ok:
                probs.append(f"{code} 제목이 어떤 화면에서 3줄 (title_fit)")
            if len(t) > 60:
                probs.append(f"{code} 60자 넘음")
            if code == "ST" and SHORTS_TITLE_BANNED and SHORTS_TITLE_BANNED.search(t):
                probs.append(f"{code} 쇼츠 제목에서 빼는 말 '{SHORTS_TITLE_BANNED.search(t).group(0)}'")
        if code in ("LM", "SM"):
            ls = [x.strip() for x in t.split("/")]
            if len(ls) > 2 or any(len(x.replace(" ", "")) > 14 for x in ls):
                probs.append(f"{code} 썸네일 주요 문구는 2줄 · 줄마다 띄어쓰기 빼고 14자 이하")
        if code in ("LS", "SS") and SUB_ITEMS:                    # 보조 = 그림 속 꼬리표 낱말 (재테크 — 'A / B', 2개 이하·각 SUB_ITEM_MAX 자)
            ws = [x.strip() for x in t.split("/") if x.strip()]
            if len(ws) > SUB_ITEMS or any(len(x.replace(" ", "")) > SUB_ITEM_MAX for x in ws):
                probs.append(f"{code} 썸네일 보조(꼬리표)는 {SUB_ITEMS}개 이하 · 각 {SUB_ITEM_MAX}자 이하")
        elif code in ("LS", "SS") and len(t.replace(" ", "")) > 16:
            probs.append(f"{code} 썸네일 보조 문구 16자 넘음")
        if code in ("LF", "SF"):
            steps = el["text"] if isinstance(el.get("text"), list) else []
            if len(steps) < (4 if code == "LF" else 3):
                probs.append(f"{code} 대본 단계가 적음 ({len(steps)})")
        if not el.get("tags"):
            probs.append(f"{code} 꼬리표 없음 (배우기에 필요)")
    return probs


# ---------------------------------------------------------------- 배우기
def all_answers(root=None):
    out = []
    for code, vid in EPISODES.items():
        _, j, _ = ep_paths(vid, root)
        if not j.is_file():
            continue
        E = json.loads(j.read_text("utf-8"))
        for r in E["rounds"]:
            for a in r["answers"]:
                out.append((vid, r["no"], a))
    return out


def learn(marks, root=None):
    g, b = Counter(), Counter()
    rated = {"좋음": {}, "나쁨": {}}
    for vid, rno, a in all_answers(root):
        for code, _, _ in ELEMS:
            m = element_rating(marks, a["id"], code)
            el = a.get(code)
            if not m or not el:
                continue
            for t in el.get("tags") or []:
                (g if m["rating"] == "좋음" else b)[f"{code}:{t}"] += 1
            rated[m["rating"]].setdefault(code, []).append(ti.toks(text_of(el)))
    W = {f: math.log((g[f] + 1) / (b[f] + 1)) for f in set(g) | set(b)}
    return W, g, b, rated


def el_score(code, el, W, rated):
    ws = [W[f"{code}:{t}"] for t in el.get("tags") or [] if f"{code}:{t}" in W]
    feat = sum(ws) / len(ws) if ws else 0.0
    tk = ti.toks(text_of(el))
    sg = max([ti.jacc(tk, x) for x in rated["좋음"].get(code, [])] or [0.0])
    sb = max([ti.jacc(tk, x) for x in rated["나쁨"].get(code, [])] or [0.0])
    return round(0.5 * feat + 0.5 * (sg - sb), 3)


def best_combo(E, marks, W, rated):
    """칸마다: 좋음 받은 글 중 점수 큰 것 → 없으면 나쁨이 아닌 글 중 점수 큰 것 (모든 회차)."""
    combo = {}
    for code, _, _ in ELEMS:
        cands = []
        for r in E["rounds"]:
            for a in r["answers"]:
                el = a.get(code)
                if not el:
                    continue
                m = element_rating(marks, a["id"], code)
                if m and m["rating"] == "나쁨":
                    continue
                cands.append(((1 if m and m["rating"] == "좋음" else 0), el_score(code, el, W, rated), a["id"], el))
        if cands:
            cands.sort(key=lambda x: (-x[0], -x[1]))
            combo[code] = cands[0]
    return combo


# ---------------------------------------------------------------- 요약본
def render_summary(E, marks, W, rated):
    R = E["rounds"][-1]
    L = [f"# VERSION: {E['version']} — {E['version_note']}",
         "# '#' 로 시작하는 줄 = 주석 (출처·평가·검사 — 영상에 안 들어감). 평가: 칸 줄 끝에 '=> 좋음' 또는 '=> 나쁨 까닭' · 안 전체는 [N안] 줄 끝에.",
         f"# 이 파일은 tools/summary_ideas.py 가 {E['file']} 에서 만든다 (안 글은 그 JSON 에서 고침). ※ 연구·교육용 — 투자 권유가 아님.", "",
         "[방향]"]
    for d in E["direction"]:
        L.append(f"- {d['text']}")
        L += [f"# {n}" for n in d.get("notes") or []]
    L.append("")
    ranked = sorted(R["answers"], key=lambda a: -sum(el_score(c, a[c], W, rated) for c, _, _ in ELEMS if a.get(c)))
    rank = {a["id"]: i for i, a in enumerate(ranked, 1)}
    for i, a in enumerate(R["answers"], 1):
        am = marks.get(a["id"])
        L.append(f"[{i}안 {a['id']}] {a['label']}")
        if am:
            L.append(f"# 평가 (안 전체): {am['rating']}" + (f" — {am['why']}" if am["why"] else ""))
        for kind in ("롱폼", "쇼츠"):
            L.append(kind)
            for code, k2, name in ELEMS:
                if k2 != kind:
                    continue
                el = a[code]
                if isinstance(el.get("text"), list):
                    L.append(f"- {name} ({a['id']}-{code}):")
                    L += [f"  {n}) {s}" for n, s in enumerate(el["text"], 1)]
                else:
                    L.append(f"- {name} ({a['id']}-{code}): {el['text']}")
                m = marks.get(f"{a['id']}-{code}")
                if m:
                    L.append(f"# 평가: {m['rating']}" + (f" — {m['why']}" if m["why"] else ""))
        L += [f"# {n}" for n in a.get("notes") or []]
        probs = lint_answer(a)
        L.append(f"# 검사: {'✅ 이상 없음' if not probs else '❌ ' + ' · '.join(probs)} · 배운 점수 순위 {rank[a['id']]}/{len(R['answers'])}")
        L.append("")
    combo = best_combo(E, marks, W, rated)
    if any(element_rating(marks, a["id"], c) for r in E["rounds"] for a in r["answers"] for c, _, _ in ELEMS):
        L.append("[추천 조합 — 평가에서]")
        for code, kind, name in ELEMS:
            if code in combo:
                good, sc, aid, el = combo[code]
                txt = " → ".join(el["text"]) if isinstance(el.get("text"), list) else el["text"]
                L.append(f"- {kind} {name}: {txt}")
                L.append(f"# ← {aid}{' (좋음)' if good else ''} · 점수 {sc:+.2f}")
        L.append("")
    return "\n".join(L)


# ---------------------------------------------------------------- 평가판 (Artifact)
PAGE = r"""<title>__NAME__ 요약본 평가판</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@400;500;700&family=IBM+Plex+Mono:wght@500&display=swap">
<style>
/* 편 탭 하나씩 — 안 카드 5장, 칸마다 좋음·나쁨 */
:root{--bg:#f3f5f7;--card:#ffffff;--ink:#17202b;--muted:#5b6876;--line:#d9dfe6;--accent:#1f5f8b;--good:#167a5b;--goodbg:#e3f3ec;--bad:#b4442f;--badbg:#f8e6e1;
--sans:"IBM Plex Sans KR","Apple SD Gothic Neo","Malgun Gothic",system-ui,sans-serif;--mono:"IBM Plex Mono",ui-monospace,Menlo,monospace}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#11161c;--card:#19212a;--ink:#e6ebf0;--muted:#9aa7b4;--line:#2b3641;--accent:#7cb4dc;--good:#5cc79f;--goodbg:#173229;--bad:#ef8c76;--badbg:#3a211b;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#11161c;--card:#19212a;--ink:#e6ebf0;--muted:#9aa7b4;--line:#2b3641;--accent:#7cb4dc;--good:#5cc79f;--goodbg:#173229;--bad:#ef8c76;--badbg:#3a211b;color-scheme:dark}
body{background:var(--bg);color:var(--ink);font-family:var(--sans);font-size:15px;line-height:1.55}
.wrap{max-width:820px;margin:0 auto;padding-block:20px 48px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));display:grid;gap:14px}
h1{font-size:1.45rem;margin:0;text-wrap:balance}
.note{font-size:.85rem;color:var(--muted);border-left:3px solid var(--line);padding-left:10px;margin:0}
.note.warn{border-color:var(--bad);color:var(--ink)}
.tabs{display:flex;gap:6px;flex-wrap:wrap}
.tabs button{font:inherit;font-size:.9rem;border:1px solid var(--line);background:var(--card);color:var(--ink);border-radius:999px;padding:5px 14px;cursor:pointer}
.tabs button[aria-pressed="true"]{background:var(--ink);color:var(--bg);border-color:var(--ink)}
.dir{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:12px 16px;margin:0;display:grid;gap:4px;font-size:.92rem}
.dir li{margin-left:1em}
.ans{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px 16px;display:grid;grid-template-columns:minmax(0,1fr);gap:10px;min-width:0}
.ah{display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.ah h2{font-size:1.05rem;margin:0}
.id{font-family:var(--mono);color:var(--accent);font-size:.85rem}
.kind{font-size:.78rem;letter-spacing:.06em;color:var(--muted);margin-top:4px}
.row{display:grid;grid-template-columns:5.5em minmax(0,1fr);gap:4px 10px;align-items:start;border-top:1px solid var(--line);padding-top:8px}
.row.good{background:linear-gradient(90deg,var(--goodbg),transparent 60%)}
.row.bad{background:linear-gradient(90deg,var(--badbg),transparent 60%)}
.lab{font-size:.82rem;color:var(--muted)}
.val{min-width:0}
.val ol{margin:0;padding-left:1.2em}
.mk{display:flex;gap:6px;flex-wrap:wrap;align-items:center;min-width:0}
.row .mk{grid-column:2}
.val{overflow-wrap:anywhere}
button.g,button.b{font:inherit;font-size:.82rem;font-weight:500;border:1px solid var(--line);background:var(--card);color:var(--ink);border-radius:7px;padding:3px 10px;cursor:pointer}
button.g[aria-pressed="true"]{background:var(--goodbg);border-color:var(--good);color:var(--good)}
button.b[aria-pressed="true"]{background:var(--badbg);border-color:var(--bad);color:var(--bad)}
.mk input{flex:1 1 140px;min-width:0;font:inherit;font-size:.82rem;border:1px solid var(--line);border-radius:7px;padding:3px 8px;background:var(--bg);color:var(--ink)}
.st{font-size:.75rem;color:var(--muted)}
button:focus-visible,input:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
button:disabled,input:disabled{opacity:.55;cursor:not-allowed}
</style>
<div class="wrap">
<h1>__NAME__ 요약본 평가판</h1>
<p class="note" id="sub"></p>
<p class="note">안 전체나 칸 하나에 좋음·나쁨을 누르면 저장됩니다. 다시 누르면 지워집니다. Claude 가 다음에 이 평가를 배워 다음 안을 쓰고, 칸마다 좋은 글을 모아 추천 조합을 만듭니다. ※ 연구·교육용 — 투자 권유가 아님.</p>
<p class="note warn" id="offline" hidden>이 화면에서는 저장할 수 없습니다. 평가는 Claude 에게 'F2 제목 좋아'처럼 말하거나 요약본 줄 끝에 '=> 좋음'을 적으면 됩니다.</p>
<div class="tabs" id="tabs" role="group" aria-label="편"></div>
<ul class="dir" id="dir"></ul>
<div id="list" style="display:grid;gap:12px"></div>
</div>
<script id="data" type="application/json">__DATA__</script>
<script>
(function(){
const D=JSON.parse(document.getElementById("data").textContent);
const marks=Object.assign({},D.marks||{});
let db=null, canWrite=false, cur=D.episodes[0].code;
const $=s=>document.querySelector(s);
function el(tag,attrs,text){const e=document.createElement(tag);for(const k in (attrs||{}))e.setAttribute(k,attrs[k]);if(text!=null)e.textContent=text;return e;}
$("#sub").textContent=`${D.made} · 편 ${D.episodes.length}개 · 편마다 안 5개`;
function tabs(){const T=$("#tabs");T.innerHTML="";D.episodes.forEach(e=>{const b=el("button",{type:"button","aria-pressed":String(e.code===cur)},e.name);b.addEventListener("click",()=>{cur=e.code;render();});T.append(b);});}
function markRow(id,label){
  const m=marks[id]||{}; const r=m.rating||"";
  const box=el("div",{class:"mk"});
  const g=el("button",{type:"button",class:"g","aria-pressed":String(r==="좋음"),id:"g-"+id},"좋음");
  const b=el("button",{type:"button",class:"b","aria-pressed":String(r==="나쁨"),id:"b-"+id},"나쁨");
  const w=el("input",{type:"text",id:"w-"+id,placeholder:"까닭 (선택)",maxlength:"120","aria-label":label+" 까닭"}); w.value=m.why||"";
  const s=el("span",{class:"st",id:"s-"+id});
  [g,b,w].forEach(x=>{if(!canWrite)x.disabled=true;});
  g.addEventListener("click",()=>save(id,r==="좋음"?"":"좋음",w.value));
  b.addEventListener("click",()=>save(id,r==="나쁨"?"":"나쁨",w.value));
  w.addEventListener("change",()=>{if(marks[id]&&marks[id].rating)save(id,marks[id].rating,w.value);});
  box.append(g,b,w,s); return box;
}
function render(){
  tabs();
  const E=D.episodes.find(e=>e.code===cur);
  const dir=$("#dir"); dir.innerHTML=""; E.direction.forEach(t=>dir.append(el("li",{},t)));
  const L=$("#list"); L.innerHTML="";
  E.answers.forEach((a,i)=>{
    const card=el("section",{class:"ans",id:"a-"+a.id});
    const h=el("div",{class:"ah"}); h.append(el("h2",{},`${i+1}안 · ${a.label}`),el("span",{class:"id"},a.id)); card.append(h);
    card.append(markRow(a.id,a.id+" 안 전체"));
    ["롱폼","쇼츠"].forEach(kind=>{
      card.append(el("div",{class:"kind"},kind));
      a.els.filter(x=>x.kind===kind).forEach(x=>{
        const r=(marks[x.id]||marks[a.id]||{}).rating||"";
        const row=el("div",{class:"row"+(r==="좋음"?" good":r==="나쁨"?" bad":"")});
        row.append(el("div",{class:"lab"},x.name));
        const v=el("div",{class:"val"});
        if(Array.isArray(x.text)){const ol=el("ol");x.text.forEach(t=>ol.append(el("li",{},t)));v.append(ol);} else v.textContent=x.text;
        row.append(v, markRow(x.id,x.id)); card.append(row);
      });
    });
    L.append(card);
  });
}
let busy=Promise.resolve();
function save(id,rating,why){
  if(!db||!canWrite)return;
  const st=document.getElementById("s-"+id); if(st) st.textContent="저장 중…";
  const body={rating:rating,why:(why||"").trim().slice(0,120),at:new Date().toISOString()};
  busy=busy.then(()=>db.collection("marks").doc(id).set(body)).then(()=>{
    if(rating) marks[id]={rating:rating,why:body.why}; else delete marks[id];
    render(); const s2=document.getElementById("s-"+id); if(s2) s2.textContent=rating?"저장됨":"지움";
  }).catch(e=>{const s3=document.getElementById("s-"+id); if(s3) s3.textContent=(e&&e.code==="invalid_argument")?"저장 못 함 (권한)":"저장 못 함 — 다시 눌러 주세요";});
}
render();
(async()=>{
  try{ db = window.claude && window.claude.use ? await window.claude.use("db") : null; }catch(e){ db=null; }
  if(!db){ $("#offline").hidden=false; return; }
  let user=null; try{ user=await window.claude.use("user"); }catch(e){}
  let cw=null; try{ cw = user ? await user.can("data.write") : null; }catch(e){ cw=null; }
  canWrite = cw!==false; if(!canWrite) $("#offline").hidden=false;
  db.collection("marks").onSnapshot(snap=>{
    snap.docs.forEach(doc=>{const v=doc.data()||{}; if(v.rating) marks[doc.id]={rating:v.rating,why:v.why||""}; else delete marks[doc.id];});
    render();
  },()=>{});
  render();
})();
})();
</script>
"""


def render_page(eps, marks):
    data = {"made": datetime.now(timezone.utc).strftime("%Y-%m-%d"), "marks": marks, "episodes": []}
    for code, vid, E in eps:
        R = E["rounds"][-1]
        answers = []
        for a in R["answers"]:
            els = [{"id": f"{a['id']}-{c}", "kind": k, "name": n, "text": a[c]["text"]} for c, k, n in ELEMS if a.get(c)]
            answers.append({"id": a["id"], "label": a["label"], "els": els})
        data["episodes"].append({"code": code, "name": E["name"], "direction": [d["text"] for d in E["direction"]], "answers": answers})
    return PAGE.replace("__NAME__", NAME).replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))


# ---------------------------------------------------------------- 명령
def cmd_status(root=None):
    P = paths(root)
    sync_file_marks(P, root)
    marks = read_marks(P)
    W, g, b, rated = learn(marks, root)
    log("LEARN", marks=len(marks), good=sum(1 for m in marks.values() if m["rating"] == "좋음"),
        bad=sum(1 for m in marks.values() if m["rating"] == "나쁨"), features=len(W))
    eps = []
    for code, vid in EPISODES.items():
        _, j, txt = ep_paths(vid, root)
        if not j.is_file():
            log("LOAD", logging.WARNING, episode=vid, note="요약본_안.json 없음")
            continue
        E = json.loads(j.read_text("utf-8"))
        eps.append((code, vid, E))
        bad = {a["id"]: lint_answer(a) for a in E["rounds"][-1]["answers"]}
        for aid, pr in bad.items():
            log("CHECK", logging.WARNING if pr else logging.INFO, episode=vid, answer=aid, result="✅" if not pr else "; ".join(pr))
        out = render_summary(E, marks, W, rated) + "\n"
        if txt.is_file() and E.get("_rendered_sha"):
            if sha(norm_render(txt.read_text("utf-8"))) != E["_rendered_sha"]:           # 사용자가 요약본 글을 고침 → 덮기 전에 따로 저장 (Claude 가 JSON 에 옮김)
                keep = txt.with_name(f"요약본.사용자수정-{datetime.now(timezone.utc).strftime('%Y%m%d-%H%M')}.txt")
                keep.write_text(txt.read_text("utf-8"), "utf-8")
                log("SYNC", logging.WARNING, episode=vid, note="요약본.txt 를 사용자가 고침 — 덮기 전에 따로 저장", saved=keep.name,
                    next="고친 글을 요약본_안.json 에 옮긴 뒤 status")
        txt.write_text(out, "utf-8")
        E["_rendered_sha"] = sha(norm_render(out))
        save_ep(vid, E, root)
        log("WRITE", summary=str(txt.relative_to(Path(root or ROOT))), answers=len(E["rounds"][-1]["answers"]), round=E["rounds"][-1]["no"])
    P["page"].write_text(render_page(eps, marks), "utf-8")
    write_material(P, eps, marks, W, g, b, rated)
    log("WRITE", page=str(P["page"].relative_to(Path(root or ROOT))), material=str(P["material"].relative_to(Path(root or ROOT))))


def write_material(P, eps, marks, W, g, b, rated):
    """다음 회차 안을 쓰기 전에 Claude 가 읽는 한 장 — 배운 꼬리표 · 좋음/나쁨 글 · 칸별 추천."""
    L = [f"# {NAME} 편 요약본 안 — 다음 회차를 쓰기 전 재료 (자동 — `tools/summary_ideas.py {VERSION}`)", "",
         f"평가 {len(marks)}개. 다음 회차 = 좋음 칸은 그대로 두거나 같은 꼬리표로 변주 · 나쁨 꼬리표는 쓰지 않음 · 평가 없는 꼬리표로 1~2안은 새로 시험. ※ 연구·교육용.", "",
         *ti.channel_lines(P["base"]),
         "## 1. 배운 꼬리표 (칸:꼬리표 — 가중치 · 좋음 · 나쁨)", ""]
    for f, w in sorted(W.items(), key=lambda x: -x[1]):
        L.append(f"- {f}: {w:+.2f} (좋음 {g[f]} · 나쁨 {b[f]})")
    if not W:
        L.append("- 아직 평가 없음.")
    L += ["", "## 2. 평가한 글", ""]
    for code, vid, E in eps:
        for r in E["rounds"]:
            for a in r["answers"]:
                for c, k, n in ELEMS:
                    m = element_rating(marks, a["id"], c)
                    if m:
                        L.append(f"- {m['rating']} {a['id']}-{c} ({k} {n}): {text_of(a[c])[:120]}" + (f" — {m['why']}" if m["why"] else ""))
    L += ["", "## 3. 편마다 칸별 추천 (좋음 > 점수)", ""]
    for code, vid, E in eps:
        L.append(f"### {E['name']} `{vid}`")
        for c, (gd, sc, aid, el) in best_combo(E, marks, W, rated).items():
            L.append(f"- {ENAME[c]}: {text_of(el)[:120]} ← {aid}{' 좋음' if gd else ''} {sc:+.2f}")
        L.append("")
    P["material"].write_text("\n".join(L) + "\n", "utf-8")


def cmd_mark(aid, rating, why="", root=None):
    if not ID_RX.match(aid):
        raise SystemExit(f"ID 는 F2 · F2-LT 꼴 (편 글자: {' · '.join(f'{k} {v}' for k, v in EPISODES.items())})")
    v = "좋음" if ti.GOOD.match(rating) or rating == "좋아요" else ("나쁨" if ti.BAD.match(rating) else None)
    if not v:
        raise SystemExit("평가는 좋음 · 나쁨")
    append_marks(paths(root), [f"{aid} {v} {why}".rstrip()])
    log("LEARN", id=aid, rating=v, why=why or "-")
    cmd_status(root)


def cmd_import(path, root=None):
    P = paths(root)
    src = Path(path)
    txt = src.read_text("utf-8")
    try:
        raw = json.loads(txt)
        docs = raw if isinstance(raw, list) else (raw.get("documents") or raw.get("docs") or [])
    except json.JSONDecodeError:
        docs = [json.loads(ln) for ln in txt.splitlines() if ln.strip().startswith("{")]
    cur = read_marks(P)
    lines = []
    for d in docs:
        body = d.get("data") if isinstance(d.get("data"), dict) else d
        did = str(d.get("id") or "")
        if not ID_RX.match(did):
            continue
        r = str(body.get("rating") or "")
        why = re.sub(r"\s+", " ", str(body.get("why") or "")).strip()[:120]
        if r in ("좋음", "나쁨") and (cur.get(did, {}).get("rating") != r or cur.get(did, {}).get("why", "") != why):
            lines.append(f"{did} {r} {why}".rstrip() + f"  # 평가판 {str(body.get('at') or '')[:16]}")
        elif not r and did in cur:
            lines.append(f"{did} 지움  # 평가판 {str(body.get('at') or '')[:16]}")
    append_marks(P, lines)
    log("SYNC", source=str(path), page_docs=len(docs), new_lines=len(lines))
    cmd_status(root)


def cmd_add(vid, path, root=None):
    """새 회차 안 5개 — {"version", "version_note", "answers": [...]} (ID 는 그 편 글자 + 이어지는 번호)."""
    E = load_ep(vid, root)
    new = json.loads(Path(path).read_text("utf-8"))
    for a in new["answers"]:
        pr = lint_answer(a)
        log("CHECK", logging.WARNING if pr else logging.INFO, answer=a.get("id"), result="✅" if not pr else "; ".join(pr))
    E["rounds"].append({"no": len(E["rounds"]) + 1, "made": datetime.now(timezone.utc).strftime("%Y-%m-%d"), "answers": new["answers"]})
    E["version"], E["version_note"] = new.get("version", E["version"]), new.get("version_note", E["version_note"])
    save_ep(vid, E, root)
    cmd_status(root)


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    topic = "stock"
    if argv and argv[0] not in COMMANDS and not argv[0].startswith("-"):      # 첫 인자가 명령이 아니면 주제 (옛 명령 = stock)
        topic = argv.pop(0)
    ap = argparse.ArgumentParser(description="편 요약본 — 핵심 방향 + 안 5개 · 좋음·나쁨을 배움 (앞에 주제: stock 기본 · economic)")
    ap.add_argument("cmd", choices=list(COMMANDS))
    ap.add_argument("args", nargs="*")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args(argv)
    logging.basicConfig(level=a.log_level, format="%(message)s", stream=sys.stdout)
    t0 = time.monotonic()
    log("START", cmd=a.cmd, topic=topic, tool=f"summary_ideas.py {VERSION}")
    configure(topic)
    if a.cmd == "status":
        cmd_status()
    elif a.cmd == "mark":
        cmd_mark(a.args[0], a.args[1], " ".join(a.args[2:]))
    elif a.cmd == "import":
        cmd_import(a.args[0])
    else:
        cmd_add(a.args[0], a.args[1])
    log("DONE", cmd=a.cmd, seconds=round(time.monotonic() - t0, 2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
