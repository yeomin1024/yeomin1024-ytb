#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-11-13 — 주제별 통과 기준 <주제>/persona_gate.json (예 crisis: 반론 중 ≤ 3 — 사용자 지시 2026-11-13 "반론은 중 3 이하로 해") ·
#          rejudge 명령(바뀐 기준으로 지난 회차 판정을 다시 셈 — 옛 판정은 pass_before 에 남김). 기준 파일이 없는 주제는 v1.0 과 같음 (중 ≤ 1).
# (이전) v1.0 — 2026-11-12 — 페르소나 반복 검증을 빠뜨리지 못하게 하는 관문 (사용자 지시 "제목,썸네일, 대본 만들때 자꾸 페르소나 반복 검증 빼먹는데
#          빼먹지 말도록 주제별 지시사항 수정해봐"). 절차 = guides/persona_loop.md.
#   단계 3개: title(제목·썸네일 피드 시험 — 대상 + 반론 페르소나) · script_exit(대본 이탈 — 대상 페르소나) · script_rebuttal(대본 반론 — 반론 페르소나)
#   · prompt : 검토자(새 하위 에이전트) 지시문을 만듦 — 회차 번호·검토자 이름·본 글의 sha 를 기록 'pending' 에 적음
#   · add    : 검토자 답(JSON)을 회차로 넣고 통과를 셈 (답이 본 글 = pending sha)
#   · check  : 단계마다 ① 2회차 이상 ② 회차마다 새 검토자 ③ 마지막 회차 통과 ④ 마지막 회차가 본 글 = 지금 글 (고친 뒤 다시 안 봤으면 ❌)
#   tools/board_check.py v1.11 가 script·package 점검 때 이 check 를 부름 → 기록이 없거나 오래되면 ❌ (평가판·대본 판에 못 올림).
#   기록 파일: 편 = <편 폴더>/persona_loop.json (항목 = 영상ID · 쇼츠 = 영상ID-shorts) · 기획안 묶음 = <topics_날짜>.persona.json (항목 = 기획안 id).
#   로그: [STAGE] [시각] key=value … · 연구·교육용 도구 — 투자 권유가 아님.
r"""
  python3 tools/persona_gate.py prompt <주제> title <기록.json> <항목> --plan <package.json | topics.json#B14> [--shorts] --out <지시문.md> [--reviewers R1-P3,R1-K]
  python3 tools/persona_gate.py prompt <주제> script_exit|script_rebuttal <기록.json> <항목> --script <대본.txt> --out <지시문.md> [--persona P3]
  python3 tools/persona_gate.py add    <기록.json> <항목> <단계> <답.json> [<답.json> …] [--fixed "이 회차 뒤 고친 것"]
  python3 tools/persona_gate.py check  <기록.json> <항목> [--script <대본.txt>] [--plan <…>] [--shorts] [--stages title,script_exit,script_rebuttal]
  python3 tools/persona_gate.py status <기록.json>
  python3 tools/persona_gate.py rejudge <기록.json>     # 주제 기준(<주제>/persona_gate.json)이 바뀐 뒤 지난 회차 판정 다시 셈
끝 코드: check 에 ❌ 가 있으면 1.
"""
from __future__ import annotations

import csv
import hashlib
import json
import random
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VERSION = "v1.1"
STAGES = {"title": "제목·썸네일 피드 시험", "script_exit": "대본 이탈 검토 (대상 페르소나)", "script_rebuttal": "대본 반론 검토 (반론 페르소나)"}
RULE = {"min_rounds": 2, "max_rounds": 5, "feed_real": 5, "feed_days": 90, "rebuttal_mid_max": 1}
RULE_KEYS_TOPIC = ("rebuttal_mid_max", "max_rounds")  # 주제 파일로 바꿀 수 있는 값만 (v1.1)


def topic_of(rec: Path) -> str | None:
    """기록 파일 경로의 첫 폴더 = 주제 (예 crisis/source/<편>/persona_loop.json → crisis)."""
    try:
        return Path(rec).resolve().relative_to(ROOT).parts[0]
    except (ValueError, IndexError):
        return None


def rules_for(topic: str | None) -> dict:
    """기본 RULE 에 <주제>/persona_gate.json 의 값을 덮음 — 없거나 깨지면 기본값 (깨지면 알림)."""
    r = dict(RULE)
    f = ROOT / topic / "persona_gate.json" if topic else None
    if f and f.is_file():
        try:
            cfg = json.loads(f.read_text("utf-8"))
        except json.JSONDecodeError as e:
            log("RULE", topic=topic, error=f"{f.name} 읽기 실패 {e} — 기본 기준", next="JSON 꼴을 고칠 것")
            return r
        for k in RULE_KEYS_TOPIC:
            if k in cfg and isinstance(cfg[k], int):
                r[k] = cfg[k]
    return r


def log(tag: str, /, **kv) -> None:
    print(f"[{tag}] [{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}] " + " ".join(f"{k}={v}" for k, v in kv.items()), flush=True)


def sha(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:16]


# ─────────── 글 (검토 대상) ───────────
def script_lines(path: str | Path) -> list[str]:
    """대본의 말·장 줄 (# 주석·빈 줄 뺌) — sha 와 줄 번호의 기준."""
    return [ln.strip() for ln in Path(path).read_text("utf-8").splitlines() if ln.strip() and not ln.lstrip().startswith("#")]


def script_text(path) -> str:
    return "\n".join(script_lines(path))


def load_plan(spec: str) -> dict:
    """--plan <package.json> (편 기획 칸) 또는 <topics_날짜.json>#<id> (기획안 묶음의 한 줄)."""
    p, _, pid = spec.partition("#")
    d = json.loads(Path(p).read_text("utf-8"))
    if pid:
        for pk in d.get("packages", []):
            if pk.get("id") == pid:
                return pk
        raise SystemExit(f"[PLAN] ❌ {p} 에 {pid} 없음")
    return d


def j(v) -> str:
    return " / ".join(v) if isinstance(v, list) else str(v or "")


def title_text(plan: dict, shorts: bool = False) -> str:
    k = ("s_title", "s_thumb_main", "s_thumb_sub") if shorts else ("title", "thumb_main", "thumb_sub")
    return f"제목: {j(plan.get(k[0])).strip()}\n썸네일 문구: {j(plan.get(k[1])).strip()}\n보조 문구: {j(plan.get(k[2])).strip()}"


# ─────────── 페르소나 · 피드 ───────────
def personas(topic: str) -> list[dict]:
    p = ROOT / topic / "result" / "outliers" / "personas.json"
    if not p.is_file():
        return []
    out = []
    for x in json.loads(p.read_text("utf-8")).get("personas", []):
        top = lambda key, n=6: [t for t, *_ in (x.get(key) or [])[:n]]  # noqa: E731
        out.append({"id": x.get("id"), "name": x.get("name", ""), "share": x.get("share"), "age": x.get("age"), "know": x.get("know"),
                    "known": top("known_terms"), "unknown": top("unknown_terms"), "wants": top("want_terms") + top("want_words"),
                    "dislikes": [t for t, *_ in (x.get("dislikes_cat") or [])[:4]] if isinstance(x.get("dislikes_cat"), list) else x.get("dislikes_cat"),
                    "questions": [q if isinstance(q, str) else q.get("text", "") for q in (x.get("top_questions") or [])[:3]]})
    return out


def persona_card(p: dict) -> str:
    def s(v):
        if isinstance(v, dict) and isinstance(v.get("dist"), dict):          # {'dist': {'50대': 101, …}, 'level': '중급'}
            tot = sum(v["dist"].values()) or 1
            txt = " · ".join(f"{k} {round(100 * c / tot)}%" for k, c in sorted(v["dist"].items(), key=lambda x: -x[1])[:3])
            return (f"{v['level']} — " if v.get("level") else "") + txt
        if isinstance(v, list):
            return ", ".join(map(str, v)) or "-"
        return json.dumps(v, ensure_ascii=False) if isinstance(v, dict) else str(v or "-")
    return (f"**{p['id']} {p['name']}** (댓글 몫 {p.get('share')})\n- 나이: {s(p.get('age'))}\n- 지식: {s(p.get('know'))}\n- 이미 아는 말: {s(p['known'])}\n"
            f"- 잘 모르는 말: {s(p['unknown'])}\n- 원하는 것: {s(p['wants'])}\n- 싫어하는 것·떠나는 까닭: {s(p.get('dislikes'))}\n- 실제로 묻는 말: {s(p.get('questions'))}")


def rebuttal_card(topic: str) -> str:
    p = ROOT / topic / "result" / "outliers" / "rebuttal_persona.md"
    if not p.is_file():
        return "(이 주제 반론 페르소나 파일 없음 — 내용의 빈틈(조건·기간·숫자·빠진 비용·현실성·앞뒤 모순·과장)을 찾는 시청자로 읽는다)"
    t = p.read_text("utf-8")
    m = re.search(r"^## 0\..*?(?=^## 1\.)", t, re.M | re.S)
    return (m.group(0) if m else t[:3000]).strip()


def feed_titles(topic: str, n: int, seed: str, shorts: bool) -> list[str]:
    """그 주제 탐색 목록(compare.csv)의 최근 실제 영상 제목 n개 (주제 밖 뺌 · 롱폼 4분 이상 / 쇼츠 1분 안) — seed 로 고정."""
    p = ROOT / topic / "result" / "outliers" / "compare.csv"
    if not p.is_file():
        return []
    rows = [r for r in csv.DictReader(p.open(encoding="utf-8-sig")) if not r.get("exclude")]
    if not rows:
        return []
    last = max(r["published"] for r in rows)
    y, m_, d_ = map(int, last.split("-"))
    import datetime as dt
    lim = (dt.date(y, m_, d_) - dt.timedelta(days=RULE["feed_days"])).isoformat()
    def ok(r):
        try:
            mins = float(r.get("minutes") or 0)
        except ValueError:
            return False
        return r["published"] >= lim and ((mins <= 1.1) if shorts else (mins >= 4))
    pool = sorted({r["title"].strip() for r in rows if ok(r) and re.search(r"[가-힣]", r["title"])})   # 한국어 제목만 (한국어 시청자의 홈 화면)
    rnd = random.Random(seed)
    return rnd.sample(pool, min(n, len(pool)))


# ─────────── 기록 ───────────
def load(rec: Path) -> dict:
    if rec.is_file():
        return json.loads(rec.read_text("utf-8"))
    return {"tool": f"persona_gate.py {VERSION}", "about": "페르소나 반복 검증 기록 — guides/persona_loop.md", "items": {}}


def save(rec: Path, d: dict) -> None:
    d["tool"] = f"persona_gate.py {VERSION}"
    rec.parent.mkdir(parents=True, exist_ok=True)
    rec.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", "utf-8")


def stage_of(d: dict, item: str, stage: str) -> dict:
    return d["items"].setdefault(item, {}).setdefault(stage, {"rounds": []})


def used_reviewers(st: dict) -> set[str]:
    return {r["reviewer"] for rd in st.get("rounds", []) for r in rd.get("reviewers", [])}


# ─────────── 지시문 ───────────
ANSWER_TITLE = """```json
{"reviewer": "<검토자 이름 그대로>", "persona": "<P? 또는 반론>",
 "feed_picks": [<누를 영상 번호 — 누를 차례대로, 많아야 2개, 하나도 안 누르면 []>],
 "feed_why": "<왜 그것을 눌렀나 / 왜 안 눌렀나 한 줄>",
 "candidate_click": true,
 "trust": "믿음 | 의심 | 낚시",
 "stop": "<보고 멈추거나 넘기게 만든 낱말·문구 (없으면 빈칸)>",
 "fix": "<고치면 누를 것 같은 방향 한 줄 (없으면 빈칸)>"}
```"""
ANSWER_EXIT = """```json
{"reviewer": "<검토자 이름 그대로>", "persona": "<P?>",
 "exits": [{"line": <끄고 싶어진 줄 번호>, "why": "<지루함·어려운 말·광고·겁주기·뻔함·관련 없음 등 — 한 줄>"}],
 "hard_words": ["<풀이 없이 나와 모르겠는 말>"],
 "keep_watching": true,
 "best": "<가장 붙잡힌 줄 번호와 까닭 한 줄>"}
```"""
ANSWER_REB = """```json
{"reviewer": "<검토자 이름 그대로>", "persona": "반론",
 "findings": [{"level": "상 | 중 | 하", "k": "K1~K8", "line": <줄 번호>, "text": "<댓글로 달 반박 한 줄>", "fix": "<고칠 방향>"}],
 "answer_clear": true,
 "summary": "<전체 한 줄>"}
```
- 상 = 결론·숫자를 틀리게 만들거나 좋아요 많이 받을 반박 · 중 = 믿음을 깎는 빈틈 · 하 = 말 다듬기."""


def make_prompt(topic: str, stage: str, d: dict, item: str, n: int, reviewers: list[str], body: dict) -> str:
    head = (f"# 페르소나 검토 — {STAGES[stage]} · {item} · {n}회차 (persona_gate.py {VERSION})\n\n"
            f"너는 처음 이 글을 보는 검토자다. 이 대화 밖의 다른 회차 결과는 모른다. 아래 페르소나가 **되어** 솔직하게 답한다 — 칭찬하려 애쓰지 않고, 억지로 흠을 만들지도 않는다.\n"
            f"검토자 이름: {', '.join(reviewers)} (이름마다 따로 답 — 한 사람이면 하나)\n"
            f"답은 아래 JSON 꼴 그대로, 검토자마다 파일 하나로 `{body['answer_dir']}/<검토자 이름>.json` 에 저장하고, 마지막 답에도 그대로 붙인다.\n"
            f"투자 권유가 아닌 연구·교육용 영상의 검토다.\n\n")
    if stage == "title":
        lst = "\n".join(f"{k}. {t}" for k, t in enumerate(body["feed"], 1))
        per = []
        for r in reviewers:
            pid = r.split("-")[-1]
            card = next((persona_card(p) for p in body["personas"] if p["id"] == pid), None)
            per.append(f"### {r}\n" + (card if card else "**반론 페르소나** — 결론보다 빈틈을 먼저 찾는 시청자 (아래 표).\n\n" + body["rebuttal"]))
        return (head + "## 1. 너는 누구인가\n\n" + "\n\n".join(per) +
                ("\n\n## 2. 유튜브 홈 화면 (제목만 보인다고 생각하고 1초 안에 고른다)\n\n" + lst +
                 "\n\n→ 이 화면에서 **누르고 싶은 영상 번호**를 많아야 2개 (`feed_picks`).\n" if body["feed"] else "\n\n(이 주제는 실제 영상 목록이 없어 2번은 건너뜀 — feed_picks 는 [])\n") +
                f"\n## 3. 이 영상 하나를 자세히 (이번엔 제목 + 썸네일 문구를 같이 본다)\n\n```\n{body['text']}\n```\n"
                "→ 누르겠나 (`candidate_click` true/false) · 믿음 / 의심 / 낚시 (`trust`) · 멈추게 한 말 (`stop`) · 고칠 방향 (`fix`).\n\n## 답\n\n" + ANSWER_TITLE + "\n")
    lines = "\n".join(f"{k:>3}  {s}" for k, s in enumerate(body["lines"], 1))
    if stage == "script_exit":
        card = next((persona_card(p) for p in body["personas"] if p["id"] == body["persona"]), None) or "(페르소나 없음)"
        task = ("## 2. 할 일\n영상을 처음부터 보는 시청자로, 줄마다 **여기서 끄고 싶어지나**만 본다 (내레이션은 AI 음성 · 화면엔 숫자·그래프).\n"
                "- 끄고 싶어진 줄 번호와 까닭 (`exits`) — 없으면 [] · 풀이 없이 나와 모르겠는 말 (`hard_words`) · 끝까지 볼 것인가 (`keep_watching`).\n")
        return head + f"## 1. 너는 누구인가\n\n{card}\n\n{task}\n## 3. 대본 (줄 번호 = 말하는 차례 · '-' 로 시작하는 줄은 장 이름)\n\n```\n{lines}\n```\n\n## 답\n\n" + ANSWER_EXIT + "\n"
    task = ("## 2. 할 일\n이 대본을 끝까지 읽고, 댓글로 **반박**을 단다면 무엇을 쓰겠나 — 아래 표의 K1~K8 질문으로. 숫자는 대본 안에서 앞뒤가 맞는지까지만 본다(밖의 자료를 찾지 않음).\n"
            "- 지적마다 `level`(상·중·하) · `k` · `line` · `text` · `fix` · 각 선택의 '옳은 선택'이 상황에 따라 갈리지 않고 분명한가 (`answer_clear`).\n")
    return head + f"## 1. 너는 누구인가\n\n{body['rebuttal']}\n\n{task}\n## 3. 대본\n\n```\n{lines}\n```\n\n## 답\n\n" + ANSWER_REB + "\n"


def cmd_prompt(a: list[str]) -> int:
    topic, stage, rec, item = a[0], a[1], Path(a[2]), a[3]
    if stage not in STAGES:
        raise SystemExit(f"단계는 {list(STAGES)}")
    opt = lambda k: a[a.index(k) + 1] if k in a else None  # noqa: E731
    d = load(rec)
    st = stage_of(d, item, stage)
    n = len(st["rounds"]) + 1
    mx = rules_for(topic_of(rec))["max_rounds"]
    if n > mx:
        log("PROMPT", item=item, stage=stage, note=f"{mx}회차를 넘음 — 남은 지적을 사용자에게 알리고 사용자 결정 (guides/persona_loop.md 4번)")
    used = used_reviewers(st)
    P = personas(topic)
    if stage == "title":
        plan = load_plan(opt("--plan") or "")
        text = title_text(plan, "--shorts" in a)
        tp = plan.get("persona") or (P[0]["id"] if P else "P1")
        reviewers = (opt("--reviewers") or f"T{n}-{tp},T{n}-반론").split(",")
        real = feed_titles(topic, RULE["feed_real"] * 2 - 1, f"{item}-{n}", "--shorts" in a)
        rnd = random.Random(f"{item}-{n}-pos")
        pos = rnd.randrange(len(real) + 1) if real else 0
        title = j(plan.get("s_title" if "--shorts" in a else "title")).strip()
        feed = real[:pos] + [title] + real[pos:] if real else []
        body = {"text": text, "feed": feed, "ours_idx": pos + 1 if real else None, "personas": P, "rebuttal": rebuttal_card(topic)}
        cur = sha(text)
    else:
        sp = opt("--script")
        if not sp:
            raise SystemExit("--script <대본.txt> 가 필요")
        lines = script_lines(sp)
        tp = opt("--persona") or (P[0]["id"] if P else "P1")
        reviewers = (opt("--reviewers") or (f"E{n}-{tp}" if stage == "script_exit" else f"K{n}-반론")).split(",")
        body = {"lines": lines, "persona": tp, "personas": P, "rebuttal": rebuttal_card(topic)}
        cur = sha("\n".join(lines))
        st["path"] = str(Path(sp).resolve().relative_to(ROOT)) if Path(sp).resolve().is_relative_to(ROOT) else sp
    again = [r for r in reviewers if r in used]
    if again:
        raise SystemExit(f"[PROMPT] ❌ 이미 앞 회차에 나온 검토자 이름 {again} — 회차마다 새 검토자 (guides/persona_loop.md 2번)")
    out = Path(opt("--out") or (rec.parent / f"persona_{item}_{stage}_{n}.md"))
    body["answer_dir"] = str(out.parent / f"answers_{item}_{stage}_{n}")
    Path(body["answer_dir"]).mkdir(parents=True, exist_ok=True)
    out.write_text(make_prompt(topic, stage, d, item, n, reviewers, body), "utf-8")
    st["pending"] = {"n": n, "sha": cur, "reviewers": reviewers, "prompt": str(out), "answers": body["answer_dir"], "ours_idx": body.get("ours_idx"),
                     "text": body.get("text"), "at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    save(rec, d)
    log("PROMPT", topic=topic, item=item, stage=stage, round=n, reviewers=",".join(reviewers), sha=cur, out=out,
        feed=len(body.get("feed") or []) if stage == "title" else "-", note="검토자마다 새 하위 에이전트에게 이 파일을 그대로 줌")
    return 0


# ─────────── 판정 ───────────
def judge(stage: str, ans: dict, ours_idx, rule: dict | None = None) -> tuple[bool, list[str]]:
    rule = rule or RULE
    why = []
    if stage == "title":
        picks = ans.get("feed_picks") or []
        if ours_idx and ours_idx not in picks:
            why.append(f"홈 화면에서 안 누름 (고른 것 {picks})")
        if not ans.get("candidate_click"):
            why.append("제목+썸네일을 보고도 안 누름")
        if str(ans.get("trust", "")).strip() == "낚시":
            why.append("낚시로 봄")
        return not why, why + ([f"멈춘 말: {ans['stop']}"] if ans.get("stop") and why else [])
    if stage == "script_exit":
        ex = ans.get("exits") or []
        if ex:
            why.append(f"끄고 싶은 줄 {[e.get('line') for e in ex]}")
        if ans.get("hard_words"):
            why.append(f"모르는 말 {ans['hard_words']}")
        if ans.get("keep_watching") is False:
            why.append("끝까지 안 봄")
        return not why, why
    f = ans.get("findings") or []
    hi = [x for x in f if str(x.get("level", "")).strip().startswith("상")]
    mid = [x for x in f if str(x.get("level", "")).strip().startswith("중")]
    if hi:
        why.append(f"상 {len(hi)} (줄 {[x.get('line') for x in hi]})")
    if len(mid) > rule["rebuttal_mid_max"]:
        why.append(f"중 {len(mid)} > {rule['rebuttal_mid_max']}")
    if ans.get("answer_clear") is False:
        why.append("옳은 선택이 분명하지 않음")
    return not why, why


def cmd_add(a: list[str]) -> int:
    rec, item, stage = Path(a[0]), a[1], a[2]
    files = [x for x in a[3:] if x.endswith(".json")]
    fixed = a[a.index("--fixed") + 1] if "--fixed" in a else ""
    d = load(rec)
    st = stage_of(d, item, stage)
    pend = st.get("pending")
    if not pend:
        raise SystemExit("[ADD] ❌ 먼저 prompt (본 글의 sha 를 남겨야 함)")
    revs = []
    rule = rules_for(topic_of(rec))
    for f in files:
        ans = json.loads(Path(f).read_text("utf-8"))
        ok, why = judge(stage, ans, pend.get("ours_idx"), rule)
        revs.append({**ans, "pass": ok, "why": why})
        log("ADD", item=item, stage=stage, round=pend["n"], reviewer=ans.get("reviewer"), ok=ok, why=";".join(why) or "-")
    names = {r.get("reviewer") for r in revs}
    if stage == "title":
        miss = [r for r in pend["reviewers"] if r not in names]
        if miss:
            raise SystemExit(f"[ADD] ❌ 답이 없는 검토자 {miss} — 대상·반론 둘 다 있어야 함")
    rd = {"n": pend["n"], "at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "sha": pend["sha"], "reviewers": revs,
          "pass": bool(revs) and all(r["pass"] for r in revs), "fixed_after": fixed, "prompt": pend.get("prompt"),
          "rule": {k: rule[k] for k in RULE_KEYS_TOPIC}}
    if pend.get("text"):
        rd["text"] = pend["text"]
    st["rounds"].append(rd)
    st.pop("pending", None)
    save(rec, d)
    log("ROUND", item=item, stage=stage, round=rd["n"], result="통과" if rd["pass"] else "고칠 것", reviewers=len(revs))
    return 0


def problems(rec: Path, item: str, stage: str, cur_sha: str | None) -> list[str]:
    """board_check 가 부름 — [] 면 통과."""
    if not rec.is_file():
        return [f"{STAGES[stage]}: 기록 없음 ({rec.name}) — guides/persona_loop.md 대로 2회차 이상"]
    st = (json.loads(rec.read_text("utf-8")).get("items", {}).get(item) or {}).get(stage) or {}
    rds = st.get("rounds") or []
    out = []
    if len(rds) < RULE["min_rounds"]:
        out.append(f"{STAGES[stage]}: {len(rds)}회차뿐 — {RULE['min_rounds']}회차 이상 (마지막 회차 = 고친 글을 새 검토자가 봄)")
    seen = set()
    for rd in rds:
        for r in rd.get("reviewers", []):
            if r.get("reviewer") in seen:
                out.append(f"{STAGES[stage]}: 검토자 {r.get('reviewer')} 가 두 회차에 — 회차마다 새 검토자")
            seen.add(r.get("reviewer"))
    if rds and not rds[-1].get("pass"):
        out.append(f"{STAGES[stage]}: 마지막 {rds[-1]['n']}회차 통과 못 함 — " + "; ".join(w for r in rds[-1]["reviewers"] for w in r.get("why", []))[:200])
    if rds and cur_sha and rds[-1].get("sha") != cur_sha:
        out.append(f"{STAGES[stage]}: 마지막 회차가 본 글과 지금 글이 다름 (고친 뒤 다시 안 봄) — 새 회차")
    if st.get("pending"):
        out.append(f"{STAGES[stage]}: {st['pending']['n']}회차 지시문만 있고 답이 안 들어옴 (add)")
    return out


def cmd_check(a: list[str]) -> int:
    rec, item = Path(a[0]), a[1]
    opt = lambda k: a[a.index(k) + 1] if k in a else None  # noqa: E731
    stages = (opt("--stages") or "title,script_exit,script_rebuttal").split(",")
    bad = 0
    for stg in stages:
        cur = None
        if stg == "title" and opt("--plan"):
            cur = sha(title_text(load_plan(opt("--plan")), "--shorts" in a))
        elif stg.startswith("script") and opt("--script"):
            cur = sha(script_text(opt("--script")))
        pr = problems(rec, item, stg, cur)
        bad += bool(pr)
        log("CHECK", item=item, stage=stg, result="✅" if not pr else "❌", problems=" | ".join(pr) or "-")
    return 1 if bad else 0


def cmd_status(a: list[str]) -> int:
    d = load(Path(a[0]))
    print(f"| 항목 | 단계 | 회차 | 마지막 | 검토자 |\n|---|---|---|---|---|")
    for item, sts in d.get("items", {}).items():
        for stg, st in sts.items():
            rds = st.get("rounds", [])
            last = rds[-1] if rds else {}
            print(f"| {item} | {stg} | {len(rds)}{' (+대기)' if st.get('pending') else ''} | {'통과' if last.get('pass') else ('고칠 것' if rds else '-')} | "
                  + ", ".join(r.get("reviewer", "?") for rd in rds for r in rd.get("reviewers", [])) + " |")
    return 0


def cmd_rejudge(a: list[str]) -> int:
    """주제 기준이 바뀐 뒤 지난 회차를 다시 셈 (답 JSON 은 그대로 · 옛 판정은 pass_before · 바뀐 회차만 로그)."""
    rec = Path(a[0])
    d = load(rec)
    rule = rules_for(topic_of(rec))
    changed = 0
    for item, sts in d.get("items", {}).items():
        for stg, st in sts.items():
            for rd in st.get("rounds", []):
                old = rd.get("pass")
                for r in rd.get("reviewers", []):
                    ok, why = judge(stg, r, None if stg != "title" else (rd.get("ours_idx") or None), rule)
                    if stg == "title":  # 제목은 기준이 안 바뀜 — 저장된 판정 그대로
                        continue
                    r.setdefault("pass_before", r.get("pass"))
                    r["pass"], r["why"] = ok, why
                if stg != "title":
                    rd["pass"] = bool(rd.get("reviewers")) and all(r["pass"] for r in rd["reviewers"])
                    rd["rule"] = {k: rule[k] for k in RULE_KEYS_TOPIC}
                if rd.get("pass") != old:
                    changed += 1
                    rd.setdefault("pass_before", old)
                    log("REJUDGE", item=item, stage=stg, round=rd["n"], before="통과" if old else "고칠 것",
                        after="통과" if rd["pass"] else "고칠 것", rule=rd.get("rule"))
    save(rec, d)
    log("REJUDGE", rec=rec, topic=topic_of(rec), rebuttal_mid_max=rule["rebuttal_mid_max"], changed_rounds=changed)
    return 0


def main(argv: list[str]) -> int:
    if not argv or argv[0] not in ("prompt", "add", "check", "status", "rejudge"):
        print(__doc__)
        return 2
    return {"prompt": cmd_prompt, "add": cmd_add, "check": cmd_check, "status": cmd_status, "rejudge": cmd_rejudge}[argv[0]](argv[1:])


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
