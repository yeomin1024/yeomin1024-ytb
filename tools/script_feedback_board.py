#!/usr/bin/env python3
# VERSION: v2.7 — 2026-11-12 — 역사·심리·위기도 (TOPICS 에 없으면 <주제>/topics/ 기본 경로 — 판 파일·db 는 주제마다 따로) · 쇼츠 'independent': true = 롱폼과 별개 쇼츠
#   (짝 롱폼 검사 안 함 — 사용자 지시 2026-11-12 "쇼츠는 꼭 롱폼 내용과 연결될 필요없이 별개로 생성하면 됨" · "재테크는 하지 말고 심리, 위기 주제를 그렇게 만들어").
# (v2.6 — 2026-11-03 — `--only long|short` — 한 세션에 판 하나 (사용자 지시 "새 세션 3개에서 … 세션당 평가판 하나야") — 다른 판 파일은 건드리지 않음.)
# (v2.5 — 2026-11-02 — 주식 쇼츠안 v7 (SHORT_VER).
# (v2.4 — 2026-11-02 — 주식 쇼츠안 v6 (SHORT_VER — 쇼츠 판 피드백 8건).
# (v2.3 — 2026-11-02 — 주제 인자 (재테크도 — 사용자 지시 2026-11-02 "지시사항 수정됐으니 stock/guides/quick_board.md 대로 평가판 구성해"):
#   주제마다 판 파일·주소·이름 (TOPICS) — 재테크는 옛 편 표(롱폼대본·쇼츠안 md) 없이 script_board.json 'extra'·shorts_board.json 'items' 만.
#   틀은 주식 틀 그대로 (stock/topics/board/script_board.template.html — 글은 자리표로 채움). 주제를 빼면 stock (옛 명령 그대로).
# (v2.2 — 2026-11-02 — 쇼츠 판에서 '전달 내용·방식' 칸을 뺌 — 쇼츠는 대본으로 평가 (사용자 지시 "쇼츠 평가판에 전달내용 빼고 대본써서 하는걸로 하자") · 대본 줄이 없는 쇼츠는 판에 올리지 않음.)
# (v2.1 — 2026-11-02 — 쇼츠 판에 '점검 결과' 칸(쇼츠안 md 의 '- 점검:' 줄 · 새 편은 기획안 check_shorts 의 ❌·⚠) · 1편 대본 v11.
# (v2.0 — 2026-11-02 — 판을 둘로 나눔: 대본 평가판(2단계 · 롱폼만) · 쇼츠 평가판(3단계 · 롱폼이 통과한 편의 쇼츠만)
#   (사용자 지시 2026-11-02 "주제 탐색 평가판 -> 대본 평가판 -> 쇼츠 평가판 이렇게 3단계로 나누자 다시 수정해줘").
#   · 틀 하나 stock/topics/board/script_board.template.html → 판 둘 (자리표 {{TITLE}}·{{H1}}·{{INTRO}} · DATA.board = 판 이름·판정 글·빈 판 글)
#   · 대본 평가판 = 롱폼대본_2026-10-31.md 표의 1~4편 + script_board.json 'extra'(주제 평가판에서 통과한 주제의 롱폼)
#   · 쇼츠 평가판 = shorts_board.json 'items' — 대본 평가판에서 그 편 롱폼이 '통과 (쇼츠로)'(db verdicts/<long_key>.verdict == pass)인 것만
#     Claude 가 한 줄씩 더함 (stock/guides/quick_board.md). 칸 = 쇼츠 제목·썸네일 문구·보조 문구·전달 내용·방식 + 대본 줄.
#   · 판정(통과·보류)과 피드백은 아티팩트 db(verdicts·feedback) — 판마다 db 가 따로 (주소가 다르므로).
# (v1.2 — 2026-11-02 — 1편 대본 v10 · 주제 평가판에서 통과한 주제의 대본(script_board.json 'extra')도 판에.
# (v1.1 — 2026-11-02 — 롱폼 판을 편마다 (1편 대본 v9 · 2~4편 v8 — 피드백판 1편 반영).
# (v1.0 — 2026-11-02 — 주식 1~4편 롱폼·쇼츠 대본을 피드백판의 SCRIPTS 칸에 채움
#   (사용자 지시 2026-11-02 "그 1~4편 롱폼, 쇼츠 각각 대본 별로 피드백 남길 수 있도록 아티팩트로 만들어볼래? 대본의 여러 줄을 선택해서 각각 피드백 달 수 있도록").
#   · 대본 파일의 '-○○' 줄은 장 이름, 나머지 빈 줄 아닌 줄 = 문장 (번호 = 오디오·자막 문장 번호와 같음)
#   · 대본이 바뀌면 이 도구를 다시 돌리고 같은 주소로 다시 올림 — 저장된 피드백(db)은 그대로 (피드백의 ver 칸으로 어느 판에 단 것인지 구분).
#   연구·교육용 도구 — 투자 권유가 아님.
# 사용: python3 tools/script_feedback_board.py [주제] [--only long|short] [--check] [--items <쇼츠 목록.json>]   (주제 = stock 기본 · economic · --only = 그 판만 씀)
#   --check = 파일을 쓰지 않고 셈만 · --items = 쇼츠 목록을 다른 파일로 (시험용 — 판 파일은 쓰지 않음)
import html as H
import json
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TPL = ROOT / "stock/topics/board/script_board.template.html"
OUT_LONG = ROOT / "stock/topics/대본피드백판.html"
OUT_SHORT = ROOT / "stock/topics/쇼츠평가판.html"
LONG_INDEX = ROOT / "stock/topics/롱폼대본_2026-10-31.md"
SHORTS_MD = ROOT / "stock/topics/쇼츠안_2026-10-30.md"
EXTRA = ROOT / "stock/topics/board/script_board.json"
SHORTS_ITEMS = ROOT / "stock/topics/board/shorts_board.json"
LONG_VER = {1: "대본 v17", 2: "대본 v18", 3: "대본 v18", 4: "대본 v18"}   # 3편 v18 = 문장 2 「3천4백만」 → 「3천1백만」 (박씨 ④ 1년 현금 대기 — 문장 79 와 맞춤, longform_ep3 v1.1) · 2편 v18 = 문장 84 「지수에 넣어 둔 2천만 원」 → 「지수에 넣어 둔 돈」 (그날 값 1,897만 원 — 계산과 맞춤) · 4편 v18 = 문장 25 45% → 58% (계산 버그 — longform_ep4 v1.1) · 2~4편 v17 = 말머리 편마다 다르게 · 3편 1편과 같은 문장 고침 (quick_board 규칙 43)
# 이전: 1편 v17·2~4편 v16 = 질문 뒤 '선택해 보세요.' · '3, 2, 1.' (quick_board 규칙 41) · 2~4편 v15 = 판 피드백 5건(질문 구체 행동·하락·역전·지표 결론, quick_board 규칙 36~39) · 1편 v16 = 판 피드백 2건(규칙 34·35) · v15·v14 = 1편 피드백 11건을 모든 편에 (2026-11-04, quick_board 규칙 26~33) · v14·v13 = 질문형 선택 + 바로 정답·해설 · v13·v12 = \'A번,\'
SHORT_VER = "v7"                                                       # 쇼츠안_2026-10-30.md 의 판
URL = {
    "topic": "https://claude.ai/artifact/Rawg2U7g3tEdSvEu5skTDN",
    "long": "https://claude.ai/artifact/7UQobTs4TU45V4GCMqWCZz",
    "short": "https://claude.ai/artifact/Mjfwm81meE2vyHH71UqAt2",
}
# v2.2 주제마다 (stock 은 위 상수 그대로)
TOPICS = {
    "economic": {
        "OUT_LONG": ROOT / "economic/topics/대본평가판.html", "OUT_SHORT": ROOT / "economic/topics/쇼츠평가판.html",
        "LONG_INDEX": None, "SHORTS_MD": None,
        "EXTRA": ROOT / "economic/topics/board/script_board.json", "SHORTS_ITEMS": ROOT / "economic/topics/board/shorts_board.json",
        "LONG_VER": {}, "NAME": "재테크", "NOTE": "정보 제공용 — 세무·법률 상담이 아닙니다.",
        "URL": {"topic": "", "long": "", "short": ""},     # economic/topics/board/urls.json 에서 채움 (판을 처음 올린 뒤)
    },
}
DEFAULT_TOPICS = {    # v2.7 TOPICS 에 없는 주제 — 이름·안내 줄만 (경로는 <주제>/topics/ 기본)
    "history": ("역사", "사실은 사료·연구로 확인합니다."),
    "psychology": ("심리", "연구·교육용 — 의료·심리 상담이 아닙니다."),
    "crisis": ("위기", "안전 수칙은 공식 지침(소방청·경찰청·국민재난안전포털)으로 확인합니다."),
}
TOPIC, NAME, NOTE = "stock", "주식", "연구·교육용 — 투자 권유가 아닙니다."
BEGIN, END = "/*SCRIPTS:BEGIN*/", "/*SCRIPTS:END*/"
NO_VALUE = "(아직 없음 — 이 판의 피드백으로 만듦)"


def log(stage, **kv):
    ts = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    print(f"[{stage}] [{ts}] " + " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) else v}" for k, v in kv.items()))


def fail(**kv):
    log("ERROR", **kv)
    sys.exit(1)


def read_lines(path):
    """대본 파일 → 문장 목록. '-' 로 시작하는 줄 = 장 이름, 빈 줄은 건너뜀."""
    sec, lines = None, []
    for raw in path.read_text(encoding="utf-8").splitlines():
        t = raw.strip()
        if not t:
            continue
        if t.startswith("-"):
            sec = t[1:].strip()
            continue
        lines.append({"n": len(lines) + 1, "t": t, "sec": sec})
    return lines


# ---------------- 2단계 대본 평가판 (롱폼) ----------------
def longform():
    out = []
    if LONG_INDEX is None:                     # v2.2 옛 편 표가 없는 주제 (재테크) — extra 만
        rows = []
    else:
        rows = re.findall(r"^\|\s*([1-4])\s*\|\s*([^|]+?)\s*\|\s*`([^`]+\.txt)`", LONG_INDEX.read_text(encoding="utf-8"), re.M)
    if LONG_INDEX is not None and len(rows) != 4:
        fail(stage="longform_index", found=len(rows), file=str(LONG_INDEX.relative_to(ROOT)), next="표 꼴(| 편 | 제목 | `대본` |)이 바뀌었는지 확인")
    for ep, title, rel in rows:
        lines = read_lines(ROOT / rel)
        out.append({"key": f"e{ep}-long", "ep": int(ep), "label": f"{ep}편", "kind": "long", "title": title.strip(),
                    "ver": LONG_VER[int(ep)], "file": rel, "lines": lines})
        log("LOAD", board="long", script=f"e{ep}-long", file=rel, sentences=len(lines), sections=len({l["sec"] for l in lines}))
    if EXTRA.exists():
        for e in json.loads(EXTRA.read_text("utf-8")).get("extra", []):
            if e.get("kind", "long") != "long":
                log("WARN", board="long", script=e.get("key"), issue="쇼츠는 대본 평가판이 아니라 shorts_board.json 에", next="그 줄을 shorts_board.json items 로 옮김")
                continue
            lines = read_lines(ROOT / e["file"])
            out.append(dict(e, kind="long", lines=lines))
            log("LOAD", board="long", script=e["key"], file=e["file"], sentences=len(lines), from_topic=e.get("label", ""))
    return out


# ---------------- 3단계 쇼츠 평가판 ----------------
def shorts_md():
    """쇼츠안_2026-10-30.md → {편: {title, bullets{}, lines[]}} + 맨 위 공통 줄(틀 등)."""
    eps, common, cur = {}, {}, None
    for raw in SHORTS_MD.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^##\s*([1-4])편\s*—\s*(.+?)\s*$", raw)
        if m:
            title = re.sub(r"\s*\((Claude )?안\)\s*$", "", m.group(2)).strip()
            cur = eps.setdefault(int(m.group(1)), {"title": title, "bullets": {}, "lines": []})
            continue
        if raw.startswith("## "):
            cur = None
            continue
        b = re.match(r"^-\s*([^:：]+?)\s*[:：]\s*(.+)$", raw)
        if b:
            key = re.sub(r"\s*\([^)]*\)", "", b.group(1)).strip()
            val = b.group(2).replace("**", "").replace("`", "").strip()   # 판은 글만 보임 — 마크다운 표시는 뺌
            (cur["bullets"] if cur is not None else common).setdefault(key, val)
            continue
        r = re.match(r"^\|\s*(\d+)\s*\|\s*([^|]*?)\s*\|\s*(.+?)\s*\|\s*$", raw)
        if cur is not None and r:
            cur["lines"].append({"n": int(r.group(1)), "role": r.group(2), "t": r.group(3), "sec": None})
    for ep, e in eps.items():
        nums = [l["n"] for l in e["lines"]]
        if nums != list(range(1, len(nums) + 1)):
            log("WARN", board="short", ep=ep, issue="쇼츠 줄 번호가 1부터 이어지지 않음", nums=str(nums))
    return eps, common


def _thumb(v):
    """'윗줄 / 아랫줄 (사용자 문구)' → ['윗줄', '아랫줄']"""
    if not v:
        return NO_VALUE
    v = re.sub(r"\s*\((사용자|Claude)[^)]*\)\s*$", "", v).strip()
    return [x.strip() for x in v.split(" / ")] if " / " in v else v


def shortform(items_path):
    if not items_path.exists():
        log("WARN", board="short", issue="쇼츠 목록 파일 없음", file=str(items_path))
        return []
    items = json.loads(items_path.read_text("utf-8")).get("items", [])
    md = common = None
    out = []
    for it in items:
        if it.get("from") == "md":
            if md is None:
                md, common = shorts_md()
            ep = int(it["md_ep"])
            if ep not in md:
                fail(stage="shorts_md", ep=ep, file=str(SHORTS_MD.relative_to(ROOT)), next="'## N편 — 제목' 머리가 있는지 확인")
            e, b = md[ep], md[ep]["bullets"]
            fields = [["s_title", "쇼츠 제목", e["title"], True],
                      ["s_thumb_main", "쇼츠 썸네일 문구", _thumb(b.get("썸네일 문구")), True],
                      ["s_thumb_sub", "쇼츠 썸네일 보조 문구", b.get("썸네일 보조 문구") or b.get("보조 문구") or NO_VALUE, False]]   # v2.2 전달 내용 칸 없음 — 대본으로 평가
            if b.get("점검"):
                fields.append(["s_check", "점검 결과 (Claude — 일반·반론 페르소나 규칙)", b["점검"], False])
            out.append({"key": it["key"], "ep": ep, "label": it.get("label", f"{ep}편"), "kind": "short", "title": e["title"],
                        "ver": it.get("ver", SHORT_VER), "file": f"{SHORTS_MD.relative_to(ROOT)} {ep}편", "long_key": it.get("long_key", f"e{ep}-long"),
                        "fields": fields, "lines": e["lines"]})
        elif it.get("from") == "file":
            src, pid = it["fields_from"].split("#")
            pk = next((p for p in json.loads((ROOT / src).read_text("utf-8"))["packages"] if p["id"] == pid), None)
            if pk is None:
                fail(stage="shorts_fields", key=it["key"], fields_from=it["fields_from"], next="기획안 id 확인")
            if not (pk.get("check_shorts") or {}).get("pass"):
                log("SKIP", board="short", key=it["key"], why="쇼츠 기획안 점검 안 함·❌", next=f"python3 tools/board_check.py package {TOPIC} {src} --stage shorts --write")
                continue
            fields = [["s_title", "쇼츠 제목", pk.get("s_title") or NO_VALUE, True],
                      ["s_thumb_main", "쇼츠 썸네일 문구", pk.get("s_thumb_main") or NO_VALUE, True],
                      ["s_thumb_sub", "쇼츠 썸네일 보조 문구", pk.get("s_thumb_sub") or NO_VALUE, False]]   # v2.2 전달 내용 칸 없음
            ck = pk.get("check_shorts") or {}
            notes = [f"❌ {x}" for x in ck.get("fail", [])] + [f"⚠ {x}" for x in ck.get("warn", [])]
            fields.append(["s_check", "점검 결과 (Claude — 일반·반론 페르소나 규칙)", " · ".join(notes) or "❌·⚠ 없음", False])
            out.append({"key": it["key"], "ep": it.get("ep", pid), "label": it.get("label", pid), "kind": "short",
                        "title": pk.get("s_title", ""), "ver": it.get("ver", "v1"), "file": it["file"],
                        "long_key": "" if it.get("independent") else it.get("long_key", f"{pid}-long"),      # v2.7 별개 쇼츠
                        "fields": fields, "lines": read_lines(ROOT / it["file"])})
        else:
            fail(stage="shorts_items", key=it.get("key"), issue="from 은 md 또는 file", file=str(items_path))
        s = out[-1]
        if not s["lines"]:
            out.pop()
            log("SKIP", board="short", key=it["key"], why="쇼츠 대본 줄이 없음 — 쇼츠는 대본으로 평가", next="쇼츠 대본을 쓴 뒤 다시")
            continue
        log("LOAD", board="short", script=s["key"], long_key=s["long_key"], lines=len(s["lines"]), fields=len(s["fields"]))
    return out


# ---------------- 판 만들기 ----------------
def links(here):
    names = [("topic", "1단계 주제 평가판"), ("long", "2단계 대본 평가판"), ("short", "3단계 쇼츠 평가판")]
    return " → ".join(f"<b>{H.escape(n)}</b>" if k == here or not URL.get(k) else f'<a href="{URL[k]}" target="_blank" rel="noopener">{H.escape(n)}</a>' for k, n in names)


BOARDS = {
    "long": {
        "out": OUT_LONG, "title": "주식 대본 평가판", "h1": "주식 대본 평가판 — 롱폼",
        "intro": lambda: links("long") + ". 롱폼 대본에서 피드백할 줄을 눌러 고르고(Shift 로 여러 줄) 의견을 남기세요. '삭제'로 지울 수 있습니다. "
                 "대본이 마음에 들면 <b>통과 (쇼츠로)</b>를 누르세요 — Claude 가 그 편의 쇼츠를 쇼츠 평가판에 올립니다. "
                 "여기 올라온 대본은 모두 일반·반론 페르소나 점검을 거쳤습니다. 연구·교육용 — 투자 권유가 아닙니다.",
        "verdict": {"pass": "통과 (쇼츠로)", "hold": "보류"},
        "verdict_hint": "통과하면 이 편의 쇼츠가 쇼츠 평가판에 올라갑니다",
        "empty": "아직 올라온 롱폼 대본이 없습니다. 주제 평가판에서 통과한 주제의 대본이 여기에 올라옵니다.",
    },
    "short": {
        "out": OUT_SHORT, "title": "주식 쇼츠 평가판", "h1": "주식 쇼츠 평가판",
        "intro": lambda: links("short") + ". 롱폼 대본이 통과한 편의 쇼츠만 올라옵니다. 쇼츠 제목·썸네일 문구·보조 문구 칸마다 '피드백'을 누르거나, "
                 "대본 줄을 골라 의견을 남기세요. '삭제'로 지울 수 있습니다. 마음에 들면 <b>통과 (영상으로)</b> — Claude 가 오디오·영상 단계로 넘깁니다. "
                 "연구·교육용 — 투자 권유가 아닙니다.",
        "verdict": {"pass": "통과 (영상으로)", "hold": "보류"},
        "verdict_hint": "통과하면 오디오·영상 만들기로 넘어갑니다",
        "empty": "아직 롱폼 대본이 통과한 편이 없습니다. 대본 평가판에서 '통과 (쇼츠로)'를 누르면 Claude 가 그 편의 쇼츠를 여기에 올립니다.",
    },
}


def build(kind, scripts, tpl):
    c = BOARDS[kind]
    board = {k: c[k] for k in ("h1", "verdict", "verdict_hint", "empty")}
    page = tpl.replace("{{TITLE}}", c["title"]).replace("{{H1}}", H.escape(c["h1"])).replace("{{INTRO}}", c["intro"]())
    a, b = page.find(BEGIN), page.find(END)
    if a < 0 or b < a:
        fail(stage="inject", file=str(TPL.relative_to(ROOT)), next="SCRIPTS:BEGIN/END 표시를 되살림")
    data = json.dumps({"board": board, "scripts": scripts}, ensure_ascii=False, separators=(",", ":"))
    left = re.findall(r"\{\{[A-Z_]+\}\}", page)
    if left:
        fail(stage="inject", board=kind, left=str(sorted(set(left))), next="틀의 자리표 이름 확인")
    return page[: a + len(BEGIN)] + data + page[b:], data


def set_topic(topic):
    """v2.2: 주제마다 판 파일·주소·이름. stock 은 맨 위 상수 그대로."""
    global TOPIC, NAME, NOTE, OUT_LONG, OUT_SHORT, LONG_INDEX, SHORTS_MD, EXTRA, SHORTS_ITEMS, LONG_VER, URL
    if topic == "stock":
        return
    if topic not in TOPICS and topic in DEFAULT_TOPICS and (ROOT / topic).is_dir():      # v2.7
        nm, nt = DEFAULT_TOPICS[topic]
        TOPICS[topic] = {"OUT_LONG": ROOT / topic / "topics/대본평가판.html", "OUT_SHORT": ROOT / topic / "topics/쇼츠평가판.html",
                         "LONG_INDEX": None, "SHORTS_MD": None, "EXTRA": ROOT / topic / "topics/board/script_board.json",
                         "SHORTS_ITEMS": ROOT / topic / "topics/board/shorts_board.json", "LONG_VER": {}, "NAME": nm, "NOTE": nt,
                         "URL": {"topic": "", "long": "", "short": ""}}
    if topic not in TOPICS:
        fail(stage="topic", topic=topic, next="TOPICS 또는 DEFAULT_TOPICS 에 주제를 더함")
    c = TOPICS[topic]
    TOPIC, NAME, NOTE = topic, c["NAME"], c["NOTE"]
    OUT_LONG, OUT_SHORT, LONG_INDEX, SHORTS_MD = c["OUT_LONG"], c["OUT_SHORT"], c["LONG_INDEX"], c["SHORTS_MD"]
    EXTRA, SHORTS_ITEMS, LONG_VER = c["EXTRA"], c["SHORTS_ITEMS"], c["LONG_VER"]
    URL = dict(c["URL"])
    up = ROOT / topic / "topics/board/urls.json"
    if up.exists():
        URL.update(json.loads(up.read_text("utf-8")))
    for k, b in BOARDS.items():
        b["out"] = OUT_LONG if k == "long" else OUT_SHORT
        b["title"] = b["title"].replace("주식", NAME)
        b["h1"] = b["h1"].replace("주식", NAME)
        intro = b["intro"]
        b["intro"] = (lambda f=intro: f().replace("연구·교육용 — 투자 권유가 아닙니다.", NOTE))
    log("TOPIC", topic=topic, out_long=str(OUT_LONG.relative_to(ROOT)), out_short=str(OUT_SHORT.relative_to(ROOT)), urls=",".join(k for k, v in URL.items() if v))


def main(argv):
    topic = next((a for i, a in enumerate(argv) if not a.startswith("-") and (i == 0 or argv[i - 1] not in ("--items", "--only"))), "stock")
    only = argv[argv.index("--only") + 1] if "--only" in argv else None      # v2.6 long | short — 세션마다 자기 판 하나만 씀
    if only not in (None, "long", "short"):
        log("ERROR", stage="args", only=only, next="--only long 또는 --only short")
        sys.exit(1)
    set_topic(topic)
    check = "--check" in argv
    items = Path(argv[argv.index("--items") + 1]).resolve() if "--items" in argv else SHORTS_ITEMS
    if items != SHORTS_ITEMS:
        check = True   # 시험 목록으로는 판 파일을 쓰지 않음
    tpl = TPL.read_text(encoding="utf-8")
    sets = {"long": longform(), "short": shortform(items)}
    long_keys = {s["key"] for s in sets["long"]}
    for s in sets["short"]:
        if s["long_key"] and s["long_key"] not in long_keys:            # v2.7 별개 쇼츠(long_key "")는 짝 검사 안 함
            log("WARN", board="short", script=s["key"], issue="짝 롱폼이 대본 평가판에 없음", long_key=s["long_key"])
    for kind, scripts in sets.items():
        if only and kind != only:
            continue
        page, data = build(kind, scripts, tpl)
        out = BOARDS[kind]["out"]
        old = out.read_text(encoding="utf-8") if out.exists() else ""
        log("DATA", board=kind, scripts=len(scripts), lines=sum(len(s["lines"]) for s in scripts),
            fields=sum(len(s.get("fields", [])) for s in scripts), bytes=len(data.encode("utf-8")),
            shorts_url_filled="{{SHORTS_URL}}" not in page)
        if not check:
            out.parent.mkdir(parents=True, exist_ok=True)          # v2.7 새 주제는 topics/ 가 없을 수 있음
            out.write_text(page, encoding="utf-8")
        log("DONE", board=kind, wrote=not check, file=str(out.relative_to(ROOT)), changed=page != old)
    return sets


if __name__ == "__main__":
    main(sys.argv[1:])
