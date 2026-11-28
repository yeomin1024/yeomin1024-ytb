#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.7.1 — 2026-11-28 — 지금은 주식만 (사용자 지시 2026-11-28 "야 내말 못들었냐 지금은 주식 주제만 하라고 계속 진행해"): studio.toml [topic.<판 주제>] SHOW_FOLDERS = 판에 보이는 폴더
#          (재테크 = stock 만 — 성공 사례 제목·탐색 문서·단계 결과) · 성공 사례 목록은 SUCCESS_FOLDERS 가 있는 판 주제만 만듦 (다른 주제는 건드리지 않음). 함수 topic_data.
# (v1.7) — 2026-11-28 — 주제 탐색 ① 성공 사례 목록 = 주제(합친 폴더 포함)의 compare.csv 에서 <폴더>/analysis_rules.toml [success] 기준을 모두 넘는 영상 전부
#          (자료 받은 사례 = analysis.json success_cases 표시·자세히) · 미국주식 낱말(next_topic.toml FOCUS)·한국어 표시 — 사용자 지시 2026-11-28
#          "맨처음 단계를 성공 사례 찾는거부터 해봐 그리고 모든 성공사례 정보 목록을 볼 수 있게해봐" · "그 일단 주식만 보이게 하고 검색에 사용한 단어 목록도 같이
#          보여줘" — studio.toml [topic.<판 주제>] SUCCESS_FOLDERS (재테크 = stock 만) · 검색어 목록 = <폴더>/keywords.txt(+ 외국 영상을 켠 주제는
#          keywords_foreign.txt) 갈래별 + tag_candidates 태그 쓴 채널·영상 수. 함수 success_rules · success_rows · search_words · topic_data.
# (v1.6) — 2026-11-28 — 주제 탐색 단계별 결과: next_topic_data.md 를 절(## 2·3·4·5·6)마다 잘라 ②·③·④·① 단계 결과 칸에 (전에는 ④에 통째로) —
#          사용자 지시 2026-11-28 "단계별 분석 다시해서 주제 탐색 결과 내봐". 함수 split_sections · step_docs.
# (v1.5) — 2026-11-28 — 판에서 숨긴 편 studio.toml [topic.<폴더>] HIDE (예전 편 — 판·gates.json 에서 뺌, 저장소 폴더·올린 기록은 그대로) —
#          사용자 지시 2026-11-28 "재테크 쪽에 예전 영상들 있는데 다 삭제해" (고름: 판에서만 빼기). 함수 episodes · topic_data · effective_gates · selftest.
# (v1.4) — 2026-11-28 — 주제 합치기 studio.toml MERGE (주식 → 재테크: 판 주제 하나에 두 폴더의 편·탐색 문서·성공 사례 — 편은 제 폴더 이름 그대로라
#          gates·음성·업로드 도구는 그대로 읽음 · 판 주제를 끄면 합친 폴더도 꺼짐) · 규칙 단계별 결과 = 주제마다 step_docs (주제 탐색 ①~⑤ 단계의 결과 문서 —
#          result/next_topic/suggest·recent·big·overlap·report·next_topic.md) · 최신 트렌드(trend) 주제. 사용자 지시 2026-11-28 "주식 관련 내용은 재테크에 포함시켜
#          그리고 규칙을 단계로 나누고 그 단계에 대한 결과를 각각 표시하도록 해 … 최신 트렌드 주제 추가해". 함수 board_topics · folders_of · off_folders · step_docs ·
#          topic_data · build · effective_gates · sync · selftest.
# (v1.3) — 2026-11-28 — 판 v1.3 구글 트렌드 (사용자 지시 2026-11-28 "주제 탐색에 구글 트렌드 부분을 넣어 단어는 8개씩하고 줄마다 단어 입력 후 링크 생성 버튼을
#          누르면 … 구글 트렌드 링크 생성해 그리고 csv 파일 업로드 할 수 있도록 해 모든 파일이 업로드 되면 완료로 표시하고"): sync 가 db trend_rows(줄마다 단어 8개) →
#          studio/state/trends.json 주제마다 groups(판 링크와 같은 묶음 — 5개까지 한 링크, 6~8개면 첫 단어를 둘 다에) · rows · csv 완료 수 · 주제마다 기간·대상 ·
#          db trend_csv(판에서 올린 CSV) → <주제>/result/next_topic/board_csv/r<줄>_p<링크>.csv + index.json (지금 줄 단어와 다른 옛 CSV 는 빼고 경고) ·
#          trends_results 는 날짜 폴더 board_<YYYYMMDD…> 만 (board_csv 제외). 함수 trend_groups · sync_trend_csv · sync · trends_results · selftest.
# (v1.2) — 2026-11-27 — 재업로드 요청 시각 = db uploads reupload_at ([재업로드] 누른 때 — 다른 체크를 바꿔도 다시 요청되지 않게) · 사용자 지시 2026-11-27 "아티팩트에서 업로드 준비 완료 체크된 것만 올릴대본에 표시하도록 해, 그리고 재업로드 버튼도 추가해". 함수 sync.
# (v1.1) — 2026-11-27 — 주제 모두(studio.toml TOPICS 10개 — 사용자 지시 "주식 이런 주제는 왜 없어? 누락된거 추가하고") · 주제 켜기·끄기
#          (판 db topics → studio/state/topics.json · 꺼 둔 주제는 판 자료를 만들지 않음 · 동기화 결과에서 뺌 — "비활성화하면 아티팩트에서 보이지 않고 에이전트가
#          보지도 않도록") · 그림은 파일 대신 자료 안 data URI (아티팩트 한 번에 255개 파일 한도) · 주제 칸 자동 찾기(analysis.json·thumb_codes·related) ·
#          common.json 에 주제별 편 요약(단계 계산용 — 주제 자료는 고를 때 받음).
# (v1.0) — 2026-11-27 — 최초: 제작 판 (심리·위기 분석 판 두 개를 하나로 — 사용자 지시 2026-11-27
#          "지금 아티팩트가 심리, 위기 2개 있는데 하나로 통합하고 아래 내용을 모두 만족하도록 수정해").
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.7 | 2026-11-28 | ① 성공 사례 전체 목록 (기준 다시 적용 · 자료 받은 사례 자세히) | success_rules · success_rows · topic_data |
# | v1.6 | 2026-11-28 | next_topic_data.md 절마다 단계 결과로 | split_sections · step_docs |
# | v1.5 | 2026-11-28 | 판에서 숨긴 편 HIDE | episodes · topic_data · effective_gates · selftest |
# | v1.4 | 2026-11-28 | 주제 합치기 MERGE · 단계별 결과 문서 step_docs · trend 주제 | board_topics · folders_of · off_folders · step_docs · topic_data · build · effective_gates · sync · selftest |
# | v1.3 | 2026-11-28 | 판 구글 트렌드 줄·CSV → trends.json groups · board_csv/ | trend_groups · sync_trend_csv · sync · trends_results · selftest |
# | v1.2 | 2026-11-27 | 재업로드 요청 시각 reupload_at | sync |
# | v1.1 | 2026-11-27 | 주제 10개 · 주제 켜기·끄기(topics.json) · data URI 그림 · 칸 자동 찾기 · 편 요약 | small_jpeg · refs_analysis · topic_cfg · build · sync · effective_gates · selftest |
# | v1.0 | 2026-11-27 | 최초 — build(저장소 → 판 자료·작은 썸네일·페이지) · sync(판 db 내려받은 것 → studio/state/*.json·rules.json) · selftest | 모두 |
"""제작 판 자료 만들기 · 판 입력을 저장소에 반영하기.

  python3 tools/studio_board.py build                 # → studio/build/index.html + data/*.json + img/… (Artifact 로 올릴 파일 목록 files.json)
  python3 tools/studio_board.py sync <db 내려받은 폴더>  # ArtifactData list out_dir 로 받은 판 db → studio/state/*.json · studio/rules.json
  python3 tools/studio_board.py selftest

단계(통과 체크가 된 편만 다음 단계로): 주제 → 제목 → 썸네일 → 대본 → 음성 → 코드 테스트 → 영상 → 업로드.
판 db 컬렉션 (페이지가 씀 · Claude 가 ArtifactData 로 읽음):
  gates     <주제>__<영상ID>__<단계>   {topic, ep, stage, pass, note, at}
  episodes  (자동 id)                 {topic, title, memo, createdAt}         — 판에서 더한 주제 후보 (편 id = 'cand-<doc id>')
  rules     <규칙 id>                 {stage, scope, text, deleted, at}        — scope = common | <주제>
  refs      <주제>.<title|thumb>.<id> {topic, kind, text, sub, note, deleted, at}
  feedback  (자동 id)                 {topic, ep, stage, line, text, status(new|done), reply, createdAt, at}
  tts       <주제>__<영상ID>          {topic, ep, make, full, redo:[문장 번호], at}
  trends    <주제> | overall          {time, gprop, every_hours, at} · overall {cats:[…], every_hours}   (v1.3 단어는 trend_rows 로 — 옛 words 는 줄이 없을 때만)
  trend_rows <주제>.r<…>              {topic, n, words:[8개까지], deleted, at}                — v1.3 구글 트렌드 줄 (링크 = trend_groups)
  trend_csv  <줄 id>.p<1|2>           {topic, row, n, part, q:[링크 단어], time, gprop, file, text, uploadedAt, at} — v1.3 판에서 올린 CSV
  skills    (자동 id)                 {name, url, memo, createdAt, at}
  uploads   <주제>__<영상ID>          {checks:{항목: bool}, reupload, note, at}
  channels  (자동 id)                 {topic, input, memo, status, reply, createdAt}   — 옛 분석 판의 고정 채널 넣기
  topics    <주제>                    {enabled, at}                            — v1.1 주제 켜기·끄기 (sync → studio/state/topics.json)
연구·교육용 도구 — 투자·의료 조언이 아니다.
"""
import argparse
import csv
import datetime as dt
import gzip
import hashlib
import html
import json
import logging
import re
import subprocess
import sys
import time
import tomllib
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent
sys.path.insert(0, str(TOOLS))

VERSION = "v1.7.1"
import topic_state  # noqa: E402  v1.1 꺼 둔 주제
KST = dt.timezone(dt.timedelta(hours=9))
STUDIO = ROOT / "studio"
STATE = STUDIO / "state"
CFG_PATH = STUDIO / "studio.toml"
RULES_PATH = STUDIO / "rules.json"
TEMPLATE = STUDIO / "board_template.html"
STAGES = ["topic", "title", "thumb", "script", "voice", "codetest", "video", "upload"]
STAGE_KO = {"topic": "주제", "title": "제목", "thumb": "썸네일", "script": "대본", "voice": "음성", "codetest": "코드 테스트",
            "video": "영상", "upload": "업로드"}
VID_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*-\d{4}-\d{2}(?:-\d{2})?")
DOC_ID_RE = re.compile(r"[A-Za-z0-9_\-.~:@+]{1,200}")
MAX_DOC_KB = 160          # 탐색 결과 문서 하나를 판에 넣는 한도 (넘으면 앞부분만 + 원문 경로)
THUMB_W, REF_W = 320, 180  # 판에 넣는 작은 썸네일 폭 (px) — v1.1 자료 안 data URI

LOG = logging.getLogger("studio_board")


def log(stage: str, level=logging.INFO, **kv) -> None:
    LOG.log(level, "[%s] [%s] %s", stage, dt.datetime.now(KST).strftime("%Y-%m-%dT%H:%M:%S"),
            " ".join(f"{k}={v}" for k, v in kv.items()))


def rel(p: Path) -> str:
    try:
        return str(Path(p).resolve().relative_to(ROOT))
    except ValueError:
        return str(p)


def git(*args: str) -> str:
    r = subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else ""


def load_cfg() -> dict:
    return tomllib.loads(CFG_PATH.read_text("utf-8"))


# ─────────────────────────────── v1.4 주제 합치기 (studio.toml MERGE = { 폴더 = "판 주제" })
def board_topics(cfg: dict) -> list[str]:
    """판에 단추로 보이는 주제 = TOPICS 에서 다른 주제 안으로 합친 폴더를 뺀 것."""
    m = cfg.get("MERGE") or {}
    return [t for t in cfg["TOPICS"] if t not in m]


def folders_of(cfg: dict, topic: str) -> list[str]:
    """판 주제 하나가 보여 주는 저장소 폴더들 (자기 + 합친 폴더)."""
    return [topic] + [c for c, p in (cfg.get("MERGE") or {}).items() if p == topic and c in cfg["TOPICS"]]


def off_folders(cfg: dict, off: set[str]) -> set[str]:
    """판에서 끈 주제 → 그 안에 합친 폴더도 꺼짐."""
    return set(off) | {c for c, p in (cfg.get("MERGE") or {}).items() if p in off}


STEP_DOCS = {                                                   # v1.4 주제 탐색 단계마다 결과 문서 (guides/topic_guide.md 1-0 · tools/next_topic.py)
    "t1": ["result/next_topic/suggest.md", "result/next_topic/keywords.md", "result/next_topic/trends.md", "result/next_topic/trends/*.md"],
    "t2": ["result/next_topic/recent*.md"],
    "t3": ["result/next_topic/big*.md"],
    "t4": ["result/next_topic/overlap*.md", "result/next_topic/report*.md"],
    "t5": ["result/next_topic/next_topic.md"],
}


SECTION_STEP = {"1": "t1", "2": "t2", "3": "t3", "4": "t4", "5": "t4", "6": "t1"}   # next_topic.py report 절 번호 → 단계


def split_sections(path: str) -> dict:
    """v1.6 next_topic_data.md → {단계: [doc]} — '## N.' 절마다 (머리말 한계 줄은 절마다 앞에)."""
    p = ROOT / path
    if not p.is_file():
        return {}
    raw = p.read_text("utf-8", errors="replace")
    head, parts, cur = [], [], None
    for ln in raw.splitlines():
        m = re.match(r"^##\s+(\d+)\.", ln)
        if m:
            cur = [m.group(1), [ln]]
            parts.append(cur)
        elif cur:
            cur[1].append(ln)
        elif ln.startswith(">"):
            head.append(ln)
    mtime = git("log", "-1", "--format=%cs", "--", path) or dt.date.fromtimestamp(p.stat().st_mtime).isoformat()
    out = {}
    for n, lines in parts:
        k = SECTION_STEP.get(n)
        if not k:
            continue
        md = "\n".join(head[-1:] + [""] + lines)
        out.setdefault(k, []).append({"path": path, "title": lines[0].lstrip("# ").strip()[:120], "date": mtime, "html": md_to_html(md), "cut": False})
    return out


def step_docs(folders: list[str], explore: list[dict]) -> dict:
    out = {}
    for k, pats in STEP_DOCS.items():
        L = []
        for f in folders:
            for pat in pats:
                for q in sorted((ROOT / f).glob(pat)):
                    if q.is_file() and not q.name.endswith("_batches.md"):
                        x = doc_entry(rel(q))
                        if x and all(y["path"] != x["path"] for y in L):
                            L.append(x)
        out[k] = L
    for f in folders:                                          # v1.6 자료 파일은 절마다 그 단계에
        for k, L in split_sections(f"{f}/result/next_topic/next_topic_data.md").items():
            out[k] = out.get(k, []) + L
    out["t5"] = out["t5"] + [x for x in explore if all(y["path"] != x["path"] for y in out["t5"])]   # 판단 = next_topic.md + studio.toml EXPLORE
    return out


def read_json(p: Path, default=None):
    try:
        if str(p).endswith(".gz"):
            return json.loads(gzip.decompress(p.read_bytes()).decode("utf-8"))
        return json.loads(p.read_text("utf-8"))
    except (OSError, json.JSONDecodeError):
        return default


# ─────────────────────────────── 마크다운 → HTML (판 안에서 결과 문서를 읽게 — 작은 변환기)
def _inline(s: str) -> str:
    out, i = [], 0
    for m in re.finditer(r"`([^`]+)`", s):
        out.append(_inline_plain(s[i:m.start()]))
        out.append("<code>" + html.escape(m.group(1)) + "</code>")
        i = m.end()
    out.append(_inline_plain(s[i:]))
    return "".join(out)


def _inline_plain(s: str) -> str:
    s = html.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)

    def link(m):
        text, url = m.group(1), html.unescape(m.group(2))
        if url.startswith("https://"):
            return f'<a href="{html.escape(url)}" target="_blank" rel="noopener">{text}</a>'
        return f"{text} <span class=\"mdpath\">({html.escape(url)})</span>"
    s = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, s)
    return s


def md_to_html(md: str) -> str:
    lines = md.replace("\r\n", "\n").split("\n")
    out, i, n = [], 0, len(lines)
    while i < n:
        ln = lines[i]
        if ln.startswith("```"):
            j = i + 1
            buf = []
            while j < n and not lines[j].startswith("```"):
                buf.append(lines[j])
                j += 1
            out.append("<pre><code>" + html.escape("\n".join(buf)) + "</code></pre>")
            i = j + 1
            continue
        m = re.match(r"(#{1,6})\s+(.*)", ln)
        if m:
            lv = min(len(m.group(1)) + 2, 6)            # 판 안에서는 h3 부터
            out.append(f"<h{lv}>{_inline(m.group(2))}</h{lv}>")
            i += 1
            continue
        if ln.strip().startswith("|") and i + 1 < n and re.match(r"^\s*\|?\s*:?-{2,}", lines[i + 1]):
            head = [c.strip() for c in ln.strip().strip("|").split("|")]
            rows = []
            j = i + 2
            while j < n and lines[j].strip().startswith("|"):
                rows.append([c.strip() for c in lines[j].strip().strip("|").split("|")])
                j += 1
            t = "<div class=\"tablebox\"><table><thead><tr>" + "".join(f"<th>{_inline(c)}</th>" for c in head) + "</tr></thead><tbody>"
            t += "".join("<tr>" + "".join(f"<td>{_inline(c)}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table></div>"
            out.append(t)
            i = j
            continue
        if ln.startswith(">"):
            buf = []
            while i < n and lines[i].startswith(">"):
                buf.append(lines[i].lstrip(">").strip())
                i += 1
            out.append("<blockquote>" + "<br>".join(_inline(x) for x in buf) + "</blockquote>")
            continue
        if re.match(r"\s*([-*]|\d+\.)\s+", ln):
            tag = "ol" if re.match(r"\s*\d+\.\s+", ln) else "ul"
            buf = []
            while i < n and re.match(r"\s*([-*]|\d+\.)\s+", lines[i]):
                buf.append(re.sub(r"^\s*([-*]|\d+\.)\s+", "", lines[i]))
                i += 1
            out.append(f"<{tag}>" + "".join(f"<li>{_inline(x)}</li>" for x in buf) + f"</{tag}>")
            continue
        if not ln.strip():
            i += 1
            continue
        buf = []
        while i < n and lines[i].strip() and not re.match(r"(#{1,6}\s|```|>|\s*([-*]|\d+\.)\s+|\s*\|)", lines[i]):
            buf.append(lines[i].strip())
            i += 1
        if not buf:                                       # 위 꼴 어디에도 안 맞는 줄 (예: '|' 하나로 시작하는 표 아닌 줄)
            buf.append(lines[i].strip())
            i += 1
        out.append("<p>" + "<br>".join(_inline(x) for x in buf) + "</p>")
    return "\n".join(out)


def doc_entry(path: str) -> dict | None:
    p = ROOT / path
    if not p.is_file():
        return None
    raw = p.read_text("utf-8", errors="replace")
    cut = len(raw.encode()) > MAX_DOC_KB * 1024
    if cut:
        raw = raw.encode()[: MAX_DOC_KB * 1024].decode("utf-8", errors="ignore") + "\n\n…(판에는 앞부분만 — 원문은 저장소 파일)"
    first = next((ln.lstrip("# ").strip() for ln in raw.splitlines() if ln.startswith("#")), p.name)
    mtime = git("log", "-1", "--format=%cs", "--", path) or dt.date.fromtimestamp(p.stat().st_mtime).isoformat()
    return {"path": path, "title": first[:120], "date": mtime, "html": md_to_html(raw), "cut": cut}


# ─────────────────────────────── 작은 썸네일 (판 안에서 보이게 — 다른 주소 그림은 판이 못 불러옴)
def small_jpeg(src: Path, width: int) -> str | None:
    """작은 JPEG → data URI (v1.1 — 파일 수 한도 없이 자료 안에)."""
    try:
        from PIL import Image
    except ImportError:
        return None
    try:
        import base64
        import io
        with Image.open(src) as im:
            im = im.convert("RGB")
            h = max(1, round(im.height * width / im.width))
            buf = io.BytesIO()
            im.resize((width, h), Image.LANCZOS).save(buf, "JPEG", quality=62, optimize=True)
        return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()
    except Exception as e:                                  # 그림 하나가 깨져도 판은 만든다
        log("IMG", logging.WARNING, src=rel(src), error=f"{type(e).__name__}: {str(e)[:120]}")
        return None


# ─────────────────────────────── 참고 자료 (분석 성공 사례 — 제목·썸네일 문구)
STOP = set("의 가 이 은 는 을 를 에 에서 와 과 도 로 으로 만 한 하는 하고 하면 그 이런 저런 더 수 것 거 등 및 vs | - · … ? ! , .".split())


def words_of(titles: list[str], top: int = 40) -> list[dict]:
    """제목 낱말 세기 (조사는 거칠게 뗌) — 2편 넘게 나온 낱말만."""
    cnt: dict[str, int] = {}
    for t in titles:
        seen = set()
        for w in re.findall(r"[가-힣A-Za-z0-9]+", t):
            w2 = re.sub(r"(으로|에서|에게|까지|부터|처럼|이라|라는|하는|했던|하면|은|는|이|가|을|를|의|에|도|만|로|와|과)$", "", w) or w
            if len(w2) < 2 or w2 in STOP or w2 in seen:
                continue
            seen.add(w2)
            cnt[w2] = cnt.get(w2, 0) + 1
    return [{"word": w, "n": c} for w, c in sorted(cnt.items(), key=lambda x: (-x[1], x[0])) if c >= 2][:top]


def refs_analysis(topic: str, tc: dict, img_dir) -> dict:
    """표준 분석기 결과 analysis.json 성공 사례 → 제목·썸네일 문구 참고 자료 (v1.1 — 모든 주제)."""
    a = read_json(ROOT / topic / "result/outliers/analysis.json", {}) or {}
    titles = []
    for c in a.get("success_cases", []):
        titles.append({"id": f"{topic}.title.{c['id']}", "vid": c["id"], "text": c["title"], "channel": c.get("channel", ""),
                       "subs": c.get("subs"), "views": c.get("views"), "ratio": c.get("ratio"), "published": c.get("published", ""),
                       "format": c.get("format", ""), "shorts": False})
    thumbs = []
    codes = ROOT / tc.get("THUMB_CODES", "") if tc.get("THUMB_CODES") else None
    succ_ids = {c["id"]: c for c in a.get("success_cases", [])}
    if codes and codes.is_file():
        for row in csv.DictReader((ln for ln in codes.read_text("utf-8").splitlines() if not ln.startswith("#")), delimiter="\t"):
            vid = row.get("id", "")
            if vid not in succ_ids:
                continue                                     # 지금 성공 사례만 (예전 성공 사례 줄은 뺌)
            c = succ_ids[vid]
            src = ROOT / topic / "result/outliers" / (c.get("thumbnail") or f"W_{vid}/thumbnail.jpg")
            img = small_jpeg(src, REF_W) if src.is_file() else None
            thumbs.append({"id": f"{topic}.thumb.{vid}", "vid": vid, "text": row.get("main_text", ""), "sub": row.get("sub_text", ""),
                           "image": row.get("image", ""), "face": row.get("face", ""), "img": img, "title": c["title"],
                           "views": c.get("views"), "ratio": c.get("ratio")})
    up = [{"word": w["word"], "rate": w["with"]["rate"], "n": w["with"]["n"], "diff": w["diff"]} for w in a.get("title_words_up", [])]
    down = [{"word": w["word"], "rate": w["with"]["rate"], "n": w["with"]["n"], "diff": w["diff"]} for w in a.get("title_words_down", [])]
    feats = [{"word": f["feature"], "rate": f["with"]["rate"], "n": f["with"]["n"], "diff": f["diff"]} for f in a.get("title_features", [])[:10]]
    return {"titles": titles, "thumbs": thumbs, "words_up": up, "words_down": down, "features": feats,
            "freq": words_of([t["text"] for t in titles]), "source": f"{topic}/result/outliers/analysis.json ({a.get('generated', '?')})",
            "thumb_source": rel(codes) if codes and codes.is_file() else ""}


def refs_videos_csv(topic: str, tc: dict, img_dir) -> dict:
    p = ROOT / topic / "result/videos.csv"
    titles = []
    if p.is_file():
        for r in csv.DictReader(p.open(encoding="utf-8-sig")):
            if r.get("group") != "성공 사례":
                continue
            titles.append({"id": f"{topic}.title.{r['video_id']}", "vid": r["video_id"], "text": r["title"], "channel": r.get("channel", ""),
                           "subs": int(float(r["subs"] or 0)), "views": int(float(r["views"] or 0)),
                           "ratio": round(float(r["views_per_sub"] or 0), 2), "published": (r.get("published") or "")[:10],
                           "format": r.get("genre", ""), "shorts": r.get("is_shorts") == "True"})
    titles.sort(key=lambda x: (x["shorts"], -(x["views"] or 0)))
    return {"titles": titles, "thumbs": [], "words_up": [], "words_down": [], "features": [],
            "freq": words_of([t["text"] for t in titles]), "source": rel(p) if p.is_file() else "",
            "thumb_source": "", "thumb_note": "이 주제 분석은 성공 사례 썸네일 문구를 분류하지 않음 (독립 1차 분석) — 판에서 직접 더할 수 있음"}


# ─────────────────────────────── 트렌드 결과 (PC 가 올린 board_<날짜> 폴더)
def parse_trends_csv(text: str) -> dict:
    lines = [ln for ln in text.splitlines() if ln.strip()]
    hi = next((i for i, ln in enumerate(lines) if re.match(r"^(주|Week|일|Day|월|Month|시간|Time)\b", ln)), None)
    if hi is None:
        return {}
    head = next(csv.reader([lines[hi]]))
    words = [re.sub(r":\s*\(.*\)$", "", h).strip() for h in head[1:]]
    series = {w: [] for w in words}
    dates = []
    for row in csv.reader(lines[hi + 1:]):
        if len(row) < 2:
            continue
        dates.append(row[0])
        for w, v in zip(words, row[1:]):
            series[w].append(int(v) if v.strip().isdigit() else 0)
    out = []
    for w in words:
        s = series[w]
        if not s:
            continue
        last, prev = s[-4:], s[-8:-4]
        avg = sum(s) / len(s)
        out.append({"word": w, "avg": round(avg, 1), "last4": round(sum(last) / len(last), 1),
                    "change": (round(sum(last) / len(last) / (sum(prev) / len(prev)), 2) if prev and sum(prev) else None),
                    "series": s[-26:]})
    return {"dates": [dates[0], dates[-1]] if dates else [], "words": out}


def trends_results(topic: str) -> dict:
    base = ROOT / topic / "result/next_topic"
    dirs = sorted((d for d in base.glob("board_[0-9]*") if d.is_dir()), key=lambda d: d.name) if base.is_dir() else []   # v1.3 PC 날짜 폴더만 (board_csv = 판에서 올린 CSV)
    if not dirs:
        return {"period": None, "dirs": [], "timeseries": [], "related": []}
    d = dirs[-1]
    ts, rl = [], []
    for f in sorted(d.glob("batch_*")):
        if f.suffix == ".csv":
            r = parse_trends_csv(f.read_text("utf-8", errors="replace"))
            if r:
                ts.append({"file": f.name, **r})
        elif f.suffix == ".json":
            j = read_json(f, {}) or {}
            for it in j.get("items", []):
                rl.append({"file": f.name, "cat": j.get("cat", 0), "keyword": it.get("keyword", ""), "time": j.get("time", ""),
                           "top": [x.get("q") for x in it.get("top", [])][:15], "rising": [[x.get("q"), x.get("f")] for x in it.get("rising", [])][:15]})
    when = git("log", "-1", "--format=%cI", "--", rel(d)) or ""
    return {"period": d.name.replace("board_", ""), "dir": rel(d), "pushed": when, "dirs": [x.name for x in dirs[-6:]],
            "timeseries": ts, "related": rl}


# ─────────────────────────────── 편 (주제 후보 → 업로드)
def tts_mod():
    try:
        import tts_narration as T
        return T
    except Exception as e:                                   # 무거운 꾸러미가 없어도 판은 만든다 (문장 번호는 같은 규칙으로 따로)
        log("TTS", logging.WARNING, note="tts_narration 을 못 불러옴 — 대본 줄은 간단 읽기", error=f"{type(e).__name__}: {str(e)[:100]}")
        return None


def read_lines_simple(txt: Path) -> list[tuple[str, str]]:
    rows, part = [], ""
    for ln in txt.read_text("utf-8").splitlines():
        s = ln.strip()
        if not s or s.startswith("#"):
            continue
        if s.startswith("-"):
            part = s[1:].strip()
            continue
        rows.append((s, part))
    return rows


def persona_rounds(src: Path, vid: str) -> dict:
    j = read_json(src / "persona_loop.json", {}) or {}
    it = (j.get("items") or {}).get(vid) or {}
    return {k: len((v or {}).get("rounds", [])) for k, v in it.items() if isinstance(v, dict)}


def upload_history(src: Path) -> list[dict]:
    out = []
    for p in sorted(src.glob("youtube*.json")):
        j = read_json(p, {}) or {}
        if p.name == "youtube_history.json":
            for h in j.get("history", []):
                out.append({"file": p.name, "videoId": h.get("videoId", ""), "url": h.get("url", ""), "uploadedAt": h.get("uploadedAt", ""),
                            "publishAt": h.get("publishAt", ""), "title": h.get("title", ""), "replacedAt": h.get("replacedAt", ""), "current": False})
            continue
        if not j.get("videoId"):
            continue
        out.append({"file": p.name, "videoId": j.get("videoId", ""), "url": j.get("url", ""), "uploadedAt": j.get("uploadedAt", ""),
                    "publishAt": j.get("publishAt", ""), "title": j.get("title", ""), "channel": j.get("channel", ""),
                    "current": p.name == "youtube.json"})
    out.sort(key=lambda x: x.get("uploadedAt") or "", reverse=True)
    return out


def episode(topic: str, src: Path, vid: str, T, img_dir: Path | None, upl_paths: set, shorts_of: str | None = None) -> dict:
    """편 하나 → 판 자료. shorts_of = 짝 롱폼 영상ID (쇼츠면). img_dir=None 이면 가볍게 (sync 의 단계 계산용 — 그림·업로드 자료 없이)."""
    base = src.parent if shorts_of else src            # 쇼츠는 source/<롱폼>/shorts/
    txt = src / f"{vid}.txt"
    pkg = read_json(base / "package.json", {}) or {}
    ep: dict = {"topic": topic, "id": vid, "kind": "shorts" if shorts_of else "long", "parent": shorts_of, "dir": rel(src)}
    if shorts_of:
        ep["title"] = pkg.get("s_title") or ""
        tm, ts_ = pkg.get("s_thumb_main") or [], pkg.get("s_thumb_sub") or ""
    else:
        ep["title"] = pkg.get("title") or ""
        tm, ts_ = pkg.get("thumb_main") or [], pkg.get("thumb_sub") or ""
    ep["thumb_main"] = tm if isinstance(tm, list) else [tm]
    ep["thumb_sub"] = ts_ if isinstance(ts_, list) else ([ts_] if ts_ else [])
    if not ep["title"] and not shorts_of and (base / "요약본.txt").is_file():          # v1.1 요약본만 있는 편 — 첫 줄을 이름으로
        first = next((ln.lstrip("-* ").strip() for ln in (base / "요약본.txt").read_text("utf-8").splitlines()
                      if ln.strip() and not ln.lstrip().startswith(("#", "["))), "")             # [방향] 아래 첫 줄
        ep["summary_title"] = first[:80]
    ep["title_why"] = (pkg.get("title_why") or "")[:900]
    ep["experiments"] = pkg.get("experiments") or []
    alts = []
    for k in ("title_alt", "title_v1", "title_r3", "title_r4", "title_r5"):
        v = pkg.get(k)
        if isinstance(v, str) and v and v != ep["title"]:
            alts.append({"key": k, "title": v})
    tmd = base / "titles.md"
    if tmd.is_file() and not shorts_of:
        for m in re.finditer(r"^\|\s*(?:\*\*)?([A-Z가-힣]?\d+|본안|실험\s*\d)(?:\*\*)?\s*\|\s*([^|]{6,90}?)\s*\|", tmd.read_text("utf-8"), re.M):
            t = m.group(2).strip().strip("`「」")
            if t and t != ep["title"] and not set(t) <= set("-: "):
                alts.append({"key": f"titles.md {m.group(1)}", "title": t})
    ep["title_alts"] = alts[:8]
    ep["persona"] = persona_rounds(base, vid)
    # 썸네일 (작게)
    thumbs = []
    tdir = src / "thumbnails"
    if tdir.is_dir():
        for p in sorted(tdir.glob("thumbnail_*")):
            if p.suffix.lower() not in (".jpg", ".jpeg", ".png") or "_upload" in p.stem:
                continue
            uri = small_jpeg(p, THUMB_W) if img_dir else None
            if uri or img_dir is None:
                thumbs.append({"name": p.name, "img": uri})
    ep["thumbs"] = thumbs
    # 대본 줄 · 음성 상태
    lines, audio = [], {"status": "none", "note": "대본 없음"}
    if txt.is_file():
        if T:
            rows, cards = T.read_script(txt)
            st, note = T.repo_status(topic, vid, rows, cards)
        else:
            rows, st, note = read_lines_simple(txt), "unknown", "tts_narration 없음"
        meta = read_json(src / "tts_narration.json", {}) or {}
        old = {it.get("n"): it.get("text") for it in meta.get("items", [])}
        for i, (t, part) in enumerate(rows, 1):
            lines.append({"n": i, "part": part, "text": t, "changed": bool(old) and old.get(i) != t})
        audio = {"status": st, "note": note, "created": meta.get("created", ""), "seconds": meta.get("seconds"),
                 "queue_stamp": meta.get("queue_stamp", ""), "tool": meta.get("tool", "")}
        syl = sum(len(re.findall(r"[가-힣0-9]", t)) for t, _ in rows)
        ep["est"] = round(syl / 6.3 + 0.35 * len(rows))
    ep["lines"] = lines
    ep["audio"] = audio
    # 영상
    scene = ROOT / "video/episodes" / vid / "index.html"
    vj = read_json(src / "video.json", None)
    rmd = src / "render.md"
    ep["video"] = {"scene": scene.is_file(), "scene_path": rel(scene) if scene.is_file() else "", "render_md": rmd.is_file(),
                   "packed": bool(vj), "mb": round(vj["size"] / 1e6) if vj else None, "duration_s": (vj or {}).get("duration_s"),
                   "on_branch": bool(vj) and all(f"{vj['dir']}/{x['name']}" in upl_paths for x in vj.get("parts", []))}
    # 업로드
    ep["upload"] = None
    ep["history"] = upload_history(src)
    if (src / "upload.md").is_file() and img_dir is not None:
        try:
            import upload_preview as upv
            rec, _ = upv.record(topic, vid, upl_paths, None, make_video=False)
            ep["upload"] = {k: rec.get(k) for k in ("status", "title", "title_chars", "title_opts", "description", "chapters", "tags",
                                                     "tags_chars", "settings", "pinned", "experiments", "problems", "items", "ready", "youtube")}
            ep["upload"]["thumbs"] = [{"n": t["n"], "name": t["name"], "main": t["main"], "role": t["role"],
                                       "img": next((x["img"] for x in thumbs if x["name"] == t["name"]), None)} for t in rec.get("thumbs", [])]
            sc = rec.get("script") or {}
            ep["upload"]["script_stale"] = sc.get("stale")
        except Exception as e:
            ep["upload"] = {"status": "error", "problems": [f"업로드 자료를 못 읽음: {type(e).__name__}: {str(e)[:160]}"]}
            log("UPLOAD", logging.WARNING, topic=topic, video=vid, error=f"{type(e).__name__}: {str(e)[:120]}")
    # v1.1 제목이 package.json 에 없던 옛 편 (재테크·주식·시험 채널) — 업로드 시트 → 올린 기록 → titles.md 첫 안
    if not ep["title"]:
        cur = next((h for h in ep["history"] if h.get("current")), None)
        ep["title"] = ((ep["upload"] or {}).get("title") or (cur or {}).get("title") or (ep["title_alts"][0]["title"] if ep["title_alts"] else "")) or ""
        if ep["title"]:
            ep["title_from"] = "업로드 시트" if (ep["upload"] or {}).get("title") else ("올린 기록" if cur else "titles.md")
    # 저장소 기준 단계 (판에서 체크하기 전 기본값 — 판의 체크가 늘 이김)
    pr = ep["persona"]
    has_audio = audio["status"] in ("has_audio", "uploaded")
    ep["repo_gates"] = {
        "topic": True,
        "title": bool(ep["title"]) and (pr.get("title", 0) >= 1 or bool(ep["history"])),
        "thumb": bool(thumbs),
        "script": bool(lines) and (pr.get("script_exit", 0) >= 1 or pr.get("script_rebuttal", 0) >= 1 or has_audio),
        "voice": has_audio,
        "codetest": scene.is_file(),
        "video": bool(vj),
        "upload": any(h["current"] for h in ep["history"]),
    }
    later = False                                              # v1.1 음성·장면·영상·업로드가 이미 있으면 앞 단계도 지난 것 (옛 편은 순서가 달랐음)
    for s_ in reversed(STAGES):                                #      대본 검증 기록만으로는 앞(썸네일)을 채우지 않음 — 썸네일이 실제로 빠진 편이 있음
        later = later or (ep["repo_gates"][s_] and s_ in ("voice", "codetest", "video", "upload"))
        ep["repo_gates"][s_] = ep["repo_gates"][s_] or later
    return ep


def episodes(topic: str, T, img_dir: Path | None, upl_paths: set, hide: set | None = None) -> list[dict]:
    out = []
    sdir = ROOT / topic / "source"
    hidden = 0
    for d in sorted(p for p in sdir.iterdir() if p.is_dir()) if sdir.is_dir() else []:
        if not VID_RE.fullmatch(d.name):
            continue
        if hide and d.name in hide:                               # v1.5 판에서 숨긴 예전 편 (짝 쇼츠도)
            hidden += 1
            continue
        files = {p.name for p in d.iterdir()}
        sh = d / "shorts"
        has_long = bool({f"{d.name}.txt", "package.json", "upload.md", "요약본.txt", "titles.md"} & files)     # v1.1 요약본 단계 편도 (역사)
        has_short = (sh / f"{d.name}-shorts.txt").is_file() or (sh / "upload.md").is_file()
        if not (has_long or has_short):
            continue
        if has_long:
            try:
                out.append(episode(topic, d, d.name, T, img_dir, upl_paths))
            except Exception as e:
                log("EPISODE", logging.WARNING, topic=topic, video=d.name, error=f"{type(e).__name__}: {str(e)[:160]}", next="그 편 폴더 확인")
                continue
        if (sh / f"{d.name}-shorts.txt").is_file() or (sh / "upload.md").is_file():
            try:
                out.append(episode(topic, sh, d.name + "-shorts", T, img_dir, upl_paths, shorts_of=d.name))
            except Exception as e:
                log("EPISODE", logging.WARNING, topic=topic, video=d.name + "-shorts", error=f"{type(e).__name__}: {str(e)[:160]}")
    def key(e):
        base = e.get("parent") or e["id"]
        m = re.search(r"(\d{4}-\d{2}(?:-\d{2})?)$", base)
        return (m.group(1) if m else "", base, e["kind"] != "long")
    out.sort(key=key, reverse=False)
    out.sort(key=lambda e: key(e)[0], reverse=True)          # 최근 편 먼저 (같은 날짜 안은 이름순 · 롱폼 뒤 짝 쇼츠)
    if hidden:
        log("EPISODES", topic=topic, shown=len(out), hidden=hidden, note="studio.toml HIDE — 판·gates 에서 뺌 (폴더는 그대로)")
    return out


def legacy(path: str) -> dict:
    j = read_json(ROOT / path, {}) if path else {}
    j = j or {}
    return {k: j.get(k) for k in ("personas", "log", "videos", "news", "market", "transcript", "made", "note", "stale_days", "today")} | {"from": (j.get("_from") or {}).get("artifact", "")}


def topic_cfg(cfg: dict, topic: str) -> dict:
    """[topic.<이름>] + 빈 칸은 저장소에서 찾음 (v1.1)."""
    tc = dict((cfg.get("topic") or {}).get(topic) or {})
    tc.setdefault("NAME", topic)
    if not tc.get("SUCCESS"):
        tc["SUCCESS"] = "analysis_json" if (ROOT / topic / "result/outliers/analysis.json").is_file() else ""
    if not tc.get("THUMB_CODES") and (ROOT / topic / "result/outliers/thumb_codes.tsv").is_file():
        tc["THUMB_CODES"] = f"{topic}/result/outliers/thumb_codes.tsv"
    if not tc.get("RELATED_DIR") and (ROOT / topic / "result/related").is_dir():
        tc["RELATED_DIR"] = f"{topic}/result/related"
    return tc


def empty_refs(topic: str) -> dict:
    return {"titles": [], "thumbs": [], "words_up": [], "words_down": [], "features": [], "freq": [], "source": "",
            "thumb_source": "", "thumb_note": f"{topic} 은(는) 성공 사례 분석 결과가 없음 — 판에서 직접 더할 수 있음"}


# ─────────────────────────────── v1.7 ① 성공 사례 — 기준을 넘는 영상 전부
SUCCESS_DEFAULT = {"MIN_AGE_DAYS": 7, "MAX_AGE_DAYS": 180, "MAX_SUBS": 50000, "MIN_VPD_SUBS": 0.1, "MIN_RATIO": 3.0, "MIN_VIEWS": 10000, "MIN_MINUTES": 4.0,
                   "CASES_PER_CHANNEL": 2}
HANGUL_RE = re.compile(r"[가-힣]")


def success_rules(folder: str) -> dict:
    p = ROOT / folder / "analysis_rules.toml"
    try:
        r = (tomllib.loads(p.read_text("utf-8")).get("success") or {}) if p.is_file() else {}
    except tomllib.TOMLDecodeError:
        r = {}
    return {k: r.get(k, v) for k, v in SUCCESS_DEFAULT.items()} | {"from": rel(p) if p.is_file() else "기본값"}


def _focus_of(folders: list[str]):
    for f in folders:
        p = ROOT / f / "next_topic.toml"
        if p.is_file():
            try:
                fx = (tomllib.loads(p.read_text("utf-8")).get("filter") or {}).get("FOCUS")
            except tomllib.TOMLDecodeError:
                fx = None
            if fx:
                return re.compile(fx, re.I), rel(p)
    return None, ""


def success_rows(folder: str, focus, refs: dict) -> tuple[list[dict], dict]:
    """compare.csv 에서 [success] 기준을 모두 넘는 영상 (뺀 것·라이브 제외) · 자료 받은 사례(analysis.json)는 자세히. 반환 (줄, 셈)."""
    R = success_rules(folder)
    p = ROOT / folder / "result/outliers/compare.csv"
    cases = {}
    aj = read_json(ROOT / folder / "result/outliers/analysis.json", {}) or {}
    for c in aj.get("success_cases") or []:
        needs = c.get("needs") or {}                            # {댓글 갈래: 수}
        top = sorted(((k, v) for k, v in needs.items() if v), key=lambda kv: -kv[1])[:4] if isinstance(needs, dict) else []
        cases[c.get("id")] = {"fmt": c.get("format", ""), "like": c.get("like_rate"), "cm": c.get("comments_total"),
                              "hook": str(c.get("hook20") or "")[:220], "needs": [f"{k.split(' — ')[0].split(' (')[0]} {v}" for k, v in top],
                              "src": c.get("text_source", "")}
    rows, n_all = [], 0
    if p.is_file():
        rd = csv.DictReader(p.open(encoding="utf-8-sig"))
        if "id" in (rd.fieldnames or []):
            for r in rd:
                n_all += 1
                if r.get("exclude"):
                    continue
                try:
                    a, sb, v, m = float(r["age_days"] or 0), float(r["subs"] or 0), float(r["views"] or 0), float(r["minutes"] or 0)
                except ValueError:
                    continue
                vs = v / max(a, 1) / max(sb, 100)
                ok_ratio = vs >= R["MIN_VPD_SUBS"] if R["MIN_VPD_SUBS"] else v >= sb * R["MIN_RATIO"]
                if not (R["MIN_AGE_DAYS"] <= a <= R["MAX_AGE_DAYS"] and sb <= R["MAX_SUBS"] and v >= R["MIN_VIEWS"] and m >= R["MIN_MINUTES"] and ok_ratio):
                    continue
                t = r["title"]
                row = {"id": r["id"], "t": t, "ch": r.get("channel", ""), "s": int(sb), "v": int(v), "vs": round(vs, 3), "a": round(a), "p": r.get("published", "")[:10],
                       "m": round(m, 1), "th": r.get("theme", ""), "f": folder, "ko": bool(HANGUL_RE.search(t)), "us": bool(focus.search(t)) if focus else None}
                if r["id"] in cases:
                    row["x"] = cases[r["id"]]
                rows.append(row)
    if not rows and refs.get("titles"):                          # 독립 분석(위기) — 분석이 고른 성공 사례 그대로
        for r in refs["titles"]:
            t = r.get("text", "")
            rows.append({"id": r.get("vid", ""), "t": t, "ch": r.get("channel", ""), "s": r.get("subs"), "v": r.get("views"), "vs": None, "a": None,
                         "p": r.get("published", ""), "m": None, "th": r.get("format", ""), "f": folder, "ko": bool(HANGUL_RE.search(t)),
                         "us": bool(focus.search(t)) if focus else None, "x": {"fmt": r.get("format", ""), "shorts": r.get("shorts")}})
        R = R | {"from": refs.get("source", "") + " (독립 분석 — 분석이 고른 성공 사례)"}
    cnt = {"rows": len(rows), "cases": sum(1 for x in rows if x.get("x")), "compare": n_all, "rules": R,
           "asof": git("log", "-1", "--format=%cs", "--", rel(p)) if p.is_file() else ""}
    return rows, cnt


def search_words(folder: str) -> dict:
    """v1.7 성공 사례를 찾은 검색어 — keywords.txt '# ── 갈래 ──' 묶음 그대로 + 태그 쓴 채널·영상 수 (tag_candidates.csv)."""
    def parse(p: Path) -> list[dict]:
        groups, cur = [], None
        if not p.is_file():
            return groups
        for ln in p.read_text("utf-8").splitlines():
            t = ln.strip()
            m = re.match(r"^#\s*──\s*(.+?)\s*──", t)
            if m:
                cur = {"name": m.group(1), "words": []}
                groups.append(cur)
            elif t and not t.startswith("#"):
                if cur is None:
                    cur = {"name": "", "words": []}
                    groups.append(cur)
                cur["words"].append(t)
        return [g for g in groups if g["words"]]
    cnt = {}
    for name in ("tag_candidates.csv", "tag_candidates_foreign.csv"):
        q = ROOT / folder / name
        if q.is_file():
            for r in csv.DictReader(q.open(encoding="utf-8-sig")):
                cnt[re.sub(r"\s+", "", (r.get("tag") or "")).lower()] = (r.get("channels"), r.get("videos"))
    def tag(gs):
        for g in gs:
            g["words"] = [{"w": w, "ch": (cnt.get(re.sub(r"\s+", "", w).lower()) or (None, None))[0], "v": (cnt.get(re.sub(r"\s+", "", w).lower()) or (None, None))[1]} for w in g["words"]]
        return gs
    foreign = False
    cfgp = ROOT / folder / "analyzer_config.toml"
    if cfgp.is_file():
        try:
            foreign = bool((tomllib.loads(cfgp.read_text("utf-8")).get("search") or {}).get("INCLUDE_FOREIGN"))
        except tomllib.TOMLDecodeError:
            pass
    ko = tag(parse(ROOT / folder / "keywords.txt"))
    fo = tag(parse(ROOT / folder / "keywords_foreign.txt")) if foreign else []
    return {"ko": ko, "foreign": fo, "src": rel(ROOT / folder / "keywords.txt"), "foreign_src": rel(ROOT / folder / "keywords_foreign.txt") if foreign else "",
            "n": sum(len(g["words"]) for g in ko), "n_foreign": sum(len(g["words"]) for g in fo)}


def _refs_of(f: str, tc: dict, img_dir) -> dict:
    return (refs_analysis(f, tc, img_dir) if tc.get("SUCCESS") == "analysis_json" else
            refs_videos_csv(f, tc, img_dir) if tc.get("SUCCESS") == "videos_csv" else empty_refs(f))


def topic_data(topic: str, cfg: dict, out: Path, T, upl_paths: set) -> dict:
    tc = topic_cfg(cfg, topic)
    img_dir = out                                              # v1.1 그림은 data URI (img_dir 는 '가볍게 아님' 표시로만)
    folders = folders_of(cfg, topic)                           # v1.4 재테크 = economic + stock
    explore, related, eps = [], [], []
    refs = None
    focus, focus_src = _focus_of(folders)                      # v1.7 성공 사례 '미국주식' 표시
    succ, succ_cnt, words = [], {}, {}
    shown = [x for x in (tc.get("SHOW_FOLDERS") or folders) if x in folders]        # v1.7.1 판에 보이는 폴더 (재테크 = 주식만)
    for f in [x for x in (tc.get("SUCCESS_FOLDERS") or []) if x in folders]:        # v1.7 성공 사례 목록 — SUCCESS_FOLDERS 가 있는 판 주제만 (지금 주식)
        tf = topic_cfg(cfg, f)
        rr, cc = success_rows(f, focus, _refs_of(f, tf, img_dir) if tf.get("SUCCESS") == "videos_csv" else {})
        seen = {x["id"] for x in succ}
        succ += [x for x in rr if x["id"] not in seen]         # 두 폴더에 같은 영상이면 한 번만
        succ_cnt[f] = cc
        words[f] = search_words(f)
    for f in shown:                                            # 판 자료 (편·탐색 문서·성공 사례 제목) — 보이는 폴더만
        tf = topic_cfg(cfg, f)
        explore += [x for x in (doc_entry(p) for p in tf.get("EXPLORE", [])) if x]
        rdir = ROOT / tf.get("RELATED_DIR", "")
        related += [x for x in (doc_entry(rel(p)) for p in sorted(rdir.glob("*.md"))) if x] if tf.get("RELATED_DIR") and rdir.is_dir() else []
        r = _refs_of(f, tf, img_dir)
        if refs is None:
            refs = r
        else:                                                  # 합친 폴더의 성공 사례는 뒤에 이어 붙임 (낱말 표는 앞 주제 것 — 없으면 합친 폴더 것)
            refs["titles"] += r["titles"]
            refs["thumbs"] += r["thumbs"]
            for k in ("words_up", "words_down", "features"):
                refs[k] = refs[k] or r[k]
            refs["freq"] = words_of([t["text"] for t in refs["titles"]])
            refs["source"] = " · ".join(x for x in (refs.get("source"), r.get("source")) if x)
            refs["thumb_source"] = " · ".join(x for x in (refs.get("thumb_source"), r.get("thumb_source")) if x)
        eps += episodes(f, T, img_dir, upl_paths, set(tf.get("HIDE", [])))
    d = {"topic": topic, "name": tc.get("NAME", topic), "note": tc.get("NOTE", ""), "folders": folders, "explore": explore, "related": related,
         "refs": refs, "episodes": eps, "legacy": legacy(tc.get("LEGACY", "")), "trends": trends_results(topic),
         "step_docs": step_docs(shown, explore), "default_words": tc.get("WORDS", []), "shown_folders": shown,
         "success": {"rows": sorted(succ, key=lambda x: -(x.get("vs") or 0)), "by_folder": succ_cnt, "focus": focus_src, "words": words}}
    if succ_cnt:
        log("SUCCESS", topic=topic, rows=len(succ), cases=sum(1 for x in succ if x.get("x")), us=sum(1 for x in succ if x.get("us")),
            by_folder=",".join(f"{k}:{v['rows']}" for k, v in succ_cnt.items()), focus=focus_src or "-")
    log("TOPIC", topic=topic, folders="+".join(folders), explore=len(explore), related=len(related), ref_titles=len(refs["titles"]), ref_thumbs=len(refs["thumbs"]),
        episodes=len(eps), step_docs=",".join(f"{k}:{len(v)}" for k, v in d["step_docs"].items()),
        personas=len(d["legacy"].get("personas") or []), trends_period=d["trends"].get("period") or "-")
    return d


def channels_data() -> dict:
    p = STUDIO / "channels" / "channels.json"
    j = read_json(p, None)
    return j or {"made": None, "channels": [], "note": "아직 없음 — python3 tools/channel_stats.py (YOUTUBE_API_KEY 가 있는 세션)"}


def build(out: Path, topics: list[str] | None = None) -> int:
    t0 = time.time()
    cfg = load_cfg()
    every = board_topics(cfg)                                      # v1.4 합친 폴더(주식)는 판 주제(재테크) 안에
    off = topic_state.disabled()
    topics = [t for t in (topics or every) if t not in off]           # v1.1 꺼 둔 주제는 판 자료를 만들지 않음
    if off:
        log("TOPIC", disabled=",".join(sorted(off)), note="꺼 둔 주제 — 판 자료를 만들지 않음 (판 '주제 켜기·끄기'에서 켜면 다음 build 에)")
    commit = git("rev-parse", "--short=9", "HEAD")
    fetched = subprocess.run(["git", "-C", str(ROOT), "fetch", "-q", "origin", "uploads"], capture_output=True).returncode == 0
    upl = set(git("ls-tree", "-r", "--name-only", "origin/uploads").splitlines()) if fetched else set()
    log("START", tool=f"studio_board.py {VERSION}", commit=commit, topics=",".join(topics), uploads_branch="ok" if fetched else "못 받음",
        note="읽기만 — 저장소에 쓰지 않음 (판 파일은 studio/build/)")
    T = tts_mod()
    out.mkdir(parents=True, exist_ok=True)
    (out / "data").mkdir(exist_ok=True)
    for old in (out / "data").glob("*.json"):                        # v1.1 꺼 둔 주제의 옛 자료가 남지 않게
        old.unlink()
    files = {}
    summary, topic_trends = {}, {}
    for t in topics:
        d = topic_data(t, cfg, out, T, upl)
        topic_trends[t] = d["trends"]
        summary[t] = [{"id": e["id"], "title": e.get("title") or e.get("summary_title", ""), "kind": e["kind"], "parent": e.get("parent"), "repo_gates": e["repo_gates"],
                       "history": [{"videoId": h.get("videoId"), "current": h.get("current")} for h in e.get("history", [])]} for e in d["episodes"]]
        body = json.dumps(d, ensure_ascii=False, separators=(",", ":"))
        (out / "data" / f"{t}.json").write_text(body, "utf-8")
        files[f"data/{t}.json"] = str(out / "data" / f"{t}.json")
    ov = cfg["trends"].get("overall", {})
    common = {"rules": read_json(RULES_PATH, {}), "channels": channels_data(), "overall_trends": trends_results(ov.get("TOPIC", "new")),
              "trends_defaults": {"every_hours": cfg["trends"].get("EVERY_HOURS", 24), "geo": cfg["trends"].get("GEO", "KR"),
                                  "gprop": cfg["trends"].get("GPROP", "youtube"), "time": cfg["trends"].get("TIME", "today 3-m"),
                                  "overall": {"topic": ov.get("TOPIC", "new"), "cats": ov.get("CATS", [0]), "time": ov.get("TIME", "now 7-d")},
                                  "words": {t: topic_cfg(cfg, t).get("WORDS", []) for t in topics}},
              "state": {k: read_json(STATE / f"{k}.json", None) for k in ("trends", "tts_queue", "gates", "reupload", "skills", "topics")},
              "summary": summary, "topic_trends": topic_trends,
              "synced_at": (read_json(STATE / "board_db.json", {}) or {}).get("synced_at")}
    body = json.dumps(common, ensure_ascii=False, separators=(",", ":"))
    (out / "data" / "common.json").write_text(body, "utf-8")
    files["data/common.json"] = str(out / "data" / "common.json")
    meta = {"tool": f"studio_board.py {VERSION}", "made": dt.datetime.now(KST).strftime("%Y-%m-%d %H:%M"), "commit": commit,
            "topics": [{"key": t, "name": topic_cfg(cfg, t).get("NAME", t), "built": t in topics, "repo_off": t in off} for t in every],
            "merge": dict(cfg.get("MERGE") or {}), "names": {t: topic_cfg(cfg, t).get("NAME", t) for t in cfg["TOPICS"]},
            "stages": STAGES, "stage_ko": STAGE_KO,
            "artifact": cfg.get("ARTIFACT", ""), "synced_at": common["synced_at"]}
    page = TEMPLATE.read_text("utf-8")
    if "/*BOARD:BEGIN*/null/*BOARD:END*/" not in page:
        raise SystemExit("[BUILD] ❌ 틀(studio/board_template.html)에 /*BOARD:BEGIN*/null/*BOARD:END*/ 자리가 없음")
    page = page.replace("/*BOARD:BEGIN*/null/*BOARD:END*/", "/*BOARD:BEGIN*/" + json.dumps(meta, ensure_ascii=False).replace("<", "\\u003c") + "/*BOARD:END*/")
    (out / "index.html").write_text(page, "utf-8")
    (out / "files.json").write_text(json.dumps(files, ensure_ascii=False, indent=1) + "\n", "utf-8")
    mb = sum(Path(p).stat().st_size for p in files.values()) / 1e6
    log("DONE", files=len(files), mb=round(mb, 2), page_kb=round((out / "index.html").stat().st_size / 1024), sec=round(time.time() - t0, 1),
        next=f"Artifact 도구: file_path={rel(out / 'index.html')} · files = {rel(out / 'files.json')} 의 표")
    return 0


# ─────────────────────────────── sync — 판 db → 저장소
def load_dump(dump: Path) -> dict:
    """ArtifactData list out_dir 로 받은 폴더 → {컬렉션: [{id, version, ...data}]}. 문서 파일 꼴 두 가지(자료만 · id/version/data)를 다 받음."""
    cols: dict[str, list] = {}
    for f in sorted(dump.rglob("*.json")):
        coll = f.parent.relative_to(dump).as_posix()
        j = read_json(f, None)
        if not isinstance(j, dict):
            continue
        if "data" in j and isinstance(j["data"], dict) and ("version" in j or "id" in j):
            doc = dict(j["data"], id=j.get("id") or f.stem, version=j.get("version"))
        else:
            doc = dict(j, id=j.get("id") or f.stem)
        cols.setdefault(coll, []).append(doc)
    return cols


def effective_gates(cfg: dict, cols: dict) -> dict:
    """편마다 단계 통과 = 판 체크(있으면) · 없으면 저장소 기준. 판에서 더한 후보(episodes)는 판 체크만."""
    T = tts_mod()
    db = {(g.get("topic"), g.get("ep"), g.get("stage")): g for g in cols.get("gates", [])}
    out = {}
    for topic in [t for t in cfg["TOPICS"] if t not in off_folders(cfg, board_disabled(cfg, cols))]:     # v1.1 꺼 둔 주제는 뺌 · v1.4 합친 폴더 포함
        eps = episodes(topic, T, None, set(), set(topic_cfg(cfg, topic).get("HIDE", [])))   # v1.5 숨긴 편은 단계 목록에서도 뺌
        cands = [{"id": "cand-" + c["id"], "repo_gates": {}} for c in cols.get("episodes", []) if c.get("topic") == topic and not c.get("deleted")]
        for e in eps + cands:
            row, ok_prev = {}, True
            for s in STAGES:
                g = db.get((topic, e["id"], s))
                passed = bool(g["pass"]) if g and g.get("pass") is not None else bool(e["repo_gates"].get(s))
                row[s] = {"pass": passed and ok_prev, "own": passed, "by": "board" if g and g.get("pass") is not None else "repo",
                          "at": (g or {}).get("at", "")}
                ok_prev = ok_prev and passed
            out[f"{topic}/{e['id']}"] = row
    return out


def apply_rules(cols: dict, now: str) -> list[str]:
    rules = read_json(RULES_PATH, {}) or {}
    st = rules.setdefault("stages", {})
    msgs = []
    for r in cols.get("rules", []):
        stage, scope, rid = r.get("stage"), r.get("scope") or "common", r.get("id")
        if stage not in st and stage not in ("trends", "topic", "title", "thumb", "script", "voice", "video", "upload"):
            msgs.append(f"⚠ 규칙 {rid}: 모르는 단계 {stage} — 건너뜀")
            continue
        lst = st.setdefault(stage, {}).setdefault(scope, [])
        cur = next((x for x in lst if x["id"] == rid), None)
        if r.get("deleted"):
            if cur:
                lst.remove(cur)
                msgs.append(f"규칙 뺌 {rid} ({stage}/{scope}) — 근거 문서 {cur.get('src', '?')} 에서도 뺄 것")
            continue
        text = (r.get("text") or "").strip()
        if not text:
            continue
        if cur and cur["text"] != text:
            msgs.append(f"규칙 고침 {rid} ({stage}/{scope}): 「{cur['text'][:50]}…」 → 「{text[:50]}…」 — 근거 문서 {cur.get('src', '?')} 도 고칠 것")
            cur["text"], cur["edited"] = text, now
        elif not cur:
            lst.append({"id": rid, "text": text, "src": f"제작 판 ({now[:10]})", "edited": now})
            msgs.append(f"규칙 더함 {rid} ({stage}/{scope}): 「{text[:60]}」 — 맞는 지시사항 문서에도 더할 것")
    if msgs:
        rules["version"] = re.sub(r"^v(\d+)\.(\d+)", lambda m: f"v{m.group(1)}.{int(m.group(2)) + 1}", rules.get("version", "v1.0")).split(" — ")[0] + \
            f" — {now[:10]} — 제작 판에서 고친 규칙 반영 (studio_board.py sync)"
        RULES_PATH.write_text(json.dumps(rules, ensure_ascii=False, indent=1) + "\n", "utf-8")
    return msgs


def trend_groups(words: list) -> list[list[str]]:
    """판 trendParts 와 같은 규칙 — 구글 트렌드는 한 번에 5개까지: 5개 이하 = 한 링크 · 6~8개 = [앞 5개] + [첫 단어 + 나머지] (첫 단어로 크기를 맞춤)."""
    seen, W = set(), []
    for w in words or []:
        w = str(w or "").strip()
        k = re.sub(r"\s+", "", w).lower()
        if w and k not in seen:
            seen.add(k)
            W.append(w)
    W = W[:8]
    if not W:
        return []
    return [W] if len(W) <= 5 else [W[:5], [W[0]] + W[5:]]


def _normset(ws) -> str:
    return "|".join(sorted(re.sub(r"\s+", "", str(w)).lower() for w in ws))


def sync_trend_csv(topic: str, rows: list, csv_docs: list, opt: dict, now: str, base: Path | None = None) -> dict:
    """판에서 올린 CSV → <주제>/result/next_topic/board_csv/ (지금 줄·기간·대상과 같은 것만). 반환 {need, have, done, dir}. base = 시험용 폴더."""
    out = (base or ROOT / topic / "result/next_topic") / "board_csv"
    by_id = {d.get("id"): d for d in csv_docs}
    need, files, index = 0, {}, []
    for r in rows:
        for i, q in enumerate(trend_groups(r.get("words")), 1):
            need += 1
            d = by_id.get(f"{r['id']}.p{i}")
            if not d:
                continue
            if _normset(d.get("q") or []) != _normset(q) or (d.get("time") or "") != opt["time"] or (d.get("gprop") if d.get("gprop") is not None else "youtube") != opt["gprop"]:
                log("TREND_CSV", logging.WARNING, topic=topic, row=r.get("n"), part=i, note="CSV 가 지금 줄 단어·기간과 다름 — 빼고 판에서 다시 올리기", csv_q="·".join(d.get("q") or []), now_q="·".join(q))
                continue
            text = str(d.get("text") or "")
            if not parse_trends_csv(text):
                log("TREND_CSV", logging.WARNING, topic=topic, row=r.get("n"), part=i, note="CSV 를 읽지 못함 — 뺌", file=d.get("file", ""))
                continue
            name = f"r{int(r.get('n') or 0):02d}_p{i}.csv"
            files[name] = text if text.endswith(chr(10)) else text + chr(10)
            index.append({"file": name, "row": r.get("n"), "part": i, "q": q, "time": opt["time"], "gprop": opt["gprop"], "uploaded_file": d.get("file", ""),
                          "uploadedAt": d.get("uploadedAt", "")})
    if files or out.is_dir():
        out.mkdir(parents=True, exist_ok=True)
        for f in out.glob("r*_p*.csv"):                                  # 이 도구가 만든 이름만 지움 (줄을 지웠거나 단어를 바꾼 옛 CSV)
            if f.name not in files:
                f.unlink()
        for name, text in files.items():
            (out / name).write_text(text, "utf-8")
        (out / "index.json").write_text(json.dumps({"updated": now, "about": "제작 판 주제 탐색 › 구글 트렌드에서 올린 CSV (값은 같은 파일 안 낱말끼리만 비교 0~100)",
                                                    "geo": "KR", "time": opt["time"], "gprop": opt["gprop"], "need": need, "have": len(files), "files": index},
                                                   ensure_ascii=False, indent=1) + "\n", "utf-8")
    log("TREND_CSV", topic=topic, rows=len(rows), need=need, have=len(files), done=bool(need and len(files) == need), dir=rel(out))
    return {"need": need, "have": len(files), "done": bool(need and len(files) == need), "dir": rel(out)}


def board_disabled(cfg: dict, cols: dict) -> set[str]:
    """판 db topics (doc id = 주제, enabled) → 꺼 둔 주제. 문서가 없는 주제는 켜짐."""
    return {d["id"] for d in cols.get("topics", []) if d.get("id") in cfg["TOPICS"] and d.get("enabled") is False}


def sync(dump: Path) -> int:
    t0 = time.time()
    cfg = load_cfg()
    cols = load_dump(dump)
    now = dt.datetime.now(KST).isoformat(timespec="seconds")
    log("SYNC", dump=rel(dump), collections=",".join(f"{k}:{len(v)}" for k, v in sorted(cols.items())) or "-")
    STATE.mkdir(parents=True, exist_ok=True)
    off = off_folders(cfg, {t for t in board_disabled(cfg, cols) if t in board_topics(cfg)})   # v1.1 주제 켜기·끄기 → 모든 도구·세션이 읽는 파일 · v1.4 합친 폴더는 판 주제를 따름
    was = topic_state.disabled()
    (STATE / "topics.json").write_text(json.dumps({"updated": now, "about": "제작 판 '주제 켜기·끄기' — disabled 주제는 판에 안 보이고 Claude·도구가 읽지도 작업하지도 않음 (tools/topic_state.py)",
                                                   "disabled": sorted(off), "enabled": [t for t in cfg["TOPICS"] if t not in off]},
                                                  ensure_ascii=False, indent=1) + "\n", "utf-8")
    if off != was:
        log("TOPICS", disabled=",".join(sorted(off)) or "-", turned_off=",".join(sorted(off - was)) or "-", turned_on=",".join(sorted(was - off)) or "-")
    (STATE / "board_db.json").write_text(json.dumps({"synced_at": now, "tool": f"studio_board.py {VERSION}", "collections": cols},
                                                    ensure_ascii=False, indent=1) + "\n", "utf-8")
    # 단계 통과
    gates = effective_gates(cfg, cols)
    (STATE / "gates.json").write_text(json.dumps({"updated": now, "stages": STAGES, "items": gates}, ensure_ascii=False, indent=1) + "\n", "utf-8")
    # 트렌드 검색어 (PC pc_trends.py watch 가 GitHub 에서 읽음)
    tr = {d["id"]: d for d in cols.get("trends", [])}
    tcfg = cfg["trends"]
    ov = tcfg.get("overall", {})
    trends = {"updated": now, "geo": tcfg.get("GEO", "KR"), "gprop": tcfg.get("GPROP", "youtube"), "time": tcfg.get("TIME", "today 3-m"),
              "topics": {}, "overall": {"topic": ov.get("TOPIC", "new"), "cats": (tr.get("overall") or {}).get("cats") or ov.get("CATS", [0]),
                                        "time": ov.get("TIME", "now 7-d"),
                                        "every_hours": int((tr.get("overall") or {}).get("every_hours") or tcfg.get("EVERY_HOURS", 24))}}
    all_rows = [r for r in cols.get("trend_rows", []) if r.get("id")]
    for t in [x for x in board_topics(cfg) if x not in off]:          # v1.4 판 주제마다 (합친 폴더 단어는 그 판 주제 줄에)
        d = tr.get(t) or {}
        opt = {"time": d.get("time") or tcfg.get("TIME", "today 3-m"), "gprop": d.get("gprop") if d.get("gprop") is not None else tcfg.get("GPROP", "youtube")}
        rows = sorted([r for r in all_rows if r.get("topic") == t and not r.get("deleted")], key=lambda r: r.get("n") or 0)
        if any(r.get("topic") == t for r in all_rows):                   # v1.3 판 줄이 있으면 그 링크 묶음 그대로
            groups = [g for r in rows for g in trend_groups(r.get("words"))]
            words = list(dict.fromkeys(w for g in groups for w in g))
            src = "board_rows"
        else:
            words = [w.strip() for w in (d.get("words") or topic_cfg(cfg, t).get("WORDS", [])) if isinstance(w, str) and w.strip()][:25]
            rows8 = [words[:8]] + [[words[0]] + words[8:][i:i + 7] for i in range(0, len(words[8:]), 7)] if words else []   # 판 기본 줄과 같은 꼴 (8개씩 · 둘째 줄부터 첫 단어로 시작)
            groups = [g for r8 in rows8 for g in trend_groups(r8)]
            src = "board" if d else "studio.toml"
        csvst = sync_trend_csv(t, rows, [c for c in cols.get("trend_csv", []) if c.get("topic") == t], opt, now) if rows else {"need": 0, "have": 0, "done": False}
        trends["topics"][t] = {"words": words, "groups": groups, "rows": [{"n": r.get("n"), "words": r.get("words") or []} for r in rows],
                               "time": opt["time"], "gprop": opt["gprop"], "every_hours": int(d.get("every_hours") or tcfg.get("EVERY_HOURS", 24)),
                               "csv": csvst, "from": src}
        log("TRENDS", topic=t, source=src, links=len(groups), words="·".join(words) or "-", time=opt["time"], gprop=opt["gprop"] or "web",
            csv=f"{csvst['have']}/{csvst['need']}", done=csvst["done"])
    (STATE / "trends.json").write_text(json.dumps(trends, ensure_ascii=False, indent=1) + "\n", "utf-8")
    # 음성 생성 줄 (Kaggle 셀의 tts_narration.py all 이 이것만 만듦)
    q = []
    for d in cols.get("tts", []):
        key = f"{d.get('topic')}/{d.get('ep')}"
        if d.get("topic") in off:
            continue
        redo = sorted({int(x) for x in (d.get("redo") or []) if str(x).isdigit()})
        if not (d.get("make") or redo):
            continue
        g = gates.get(key, {})
        if not g.get("script", {}).get("pass"):
            log("TTS", logging.WARNING, item=key, note="대본 단계 통과 전 — 음성 줄에 넣지 않음")
            continue
        q.append({"topic": d.get("topic"), "id": d.get("ep"), "stamp": str(d.get("at") or d.get("version") or now), "full": bool(d.get("full")),
                  "redo": redo})
    (STATE / "tts_queue.json").write_text(json.dumps({"updated": now, "about": "제작 판에서 '음성 생성'·줄 '재생성'을 체크한 것 — tools/tts_narration.py all 이 판 주제(topics)는 이것만 만듦 · 판 밖 주제는 예전처럼 (--all-pending 이면 모두 예전처럼)",
                                                       "topics": [t for t in cfg["TOPICS"] if t not in off], "items": q}, ensure_ascii=False, indent=1) + "\n", "utf-8")
    # 다시 올리기 · 스킬
    re_up = [{"topic": d["id"].split("__")[0], "id": d["id"].split("__", 1)[1], "at": d.get("reupload_at") or d.get("at", ""), "note": d.get("note", "")}   # v1.2 [재업로드] 누른 때
             for d in cols.get("uploads", []) if d.get("reupload") and "__" in d.get("id", "") and d["id"].split("__")[0] not in off]
    (STATE / "reupload.json").write_text(json.dumps({"updated": now, "items": re_up}, ensure_ascii=False, indent=1) + "\n", "utf-8")
    skills = [{"name": d.get("name", ""), "url": d.get("url", ""), "memo": d.get("memo", "")} for d in cols.get("skills", []) if d.get("url")]
    (STATE / "skills.json").write_text(json.dumps({"updated": now, "skills": skills}, ensure_ascii=False, indent=1) + "\n", "utf-8")
    msgs = apply_rules(cols, now)
    fb_new = [f for f in cols.get("feedback", []) if f.get("status", "new") == "new"]
    log("SYNC", gates=len(gates), trends_topics=len(trends["topics"]), tts_queue=len(q), reupload=len(re_up), skills=len(skills),
        rule_changes=len(msgs), feedback_new=len(fb_new), sec=round(time.time() - t0, 1))
    for m in msgs:
        log("RULES", note=m)
    for f in fb_new:
        log("FEEDBACK", id=f.get("id"), topic=f.get("topic"), ep=f.get("ep"), stage=f.get("stage"), line=f.get("line") or "-",
            text=str(f.get("text", ""))[:80].replace(" ", "_"))
    for x in q:
        log("TTS_QUEUE", topic=x["topic"], video=x["id"], full=x["full"], redo=",".join(map(str, x["redo"])) or "-", stamp=x["stamp"])
    log("NEXT", note="① 피드백 반영 → 판 db feedback status=done·reply ② 규칙 고침은 근거 문서에도 ③ git commit·push (main) ④ build → 같은 주소로 발행")
    return 0


# ─────────────────────────────── selftest
def selftest() -> int:
    ok = True

    def check(name, cond):
        nonlocal ok
        print(("PASS " if cond else "FAIL ") + name)
        ok = ok and cond
    h = md_to_html("# 제목\n\n| a | b |\n|---|---|\n| 1 | **2** |\n\n- 하나\n- 둘\n\n```\nx<y\n```\n> 인용\n문단 [링크](https://x.y) [로컬](a/b.md)")
    check("md 표", "<table>" in h and "<strong>2</strong>" in h)
    check("md 목록·코드", "<ul><li>하나</li>" in h and "x&lt;y" in h)
    check("md 링크 https 만", 'href="https://x.y"' in h and 'href="a/b.md"' not in h)
    csvt = "카테고리: 모든 카테고리\n\n주,심리: (대한민국),엄마: (대한민국)\n" + "\n".join(f"2025-0{1 + i // 4}-0{1 + i % 4},{50 + i},{i}" for i in range(9))
    r = parse_trends_csv(csvt)
    check("트렌드 CSV 낱말", [w["word"] for w in r["words"]] == ["심리", "엄마"])
    check("트렌드 바뀜 배수", r["words"][0]["change"] is not None and r["words"][0]["change"] > 1)
    check("제목 낱말 세기", words_of(["엄마 기분 살피던 사람", "엄마 하소연 받아 주는 사람"])[0]["word"] in ("엄마", "사람"))
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        d = Path(td)
        (d / "gates").mkdir()
        (d / "gates" / "psychology__x-2026-11__title.json").write_text(json.dumps({"id": "psychology__x-2026-11__title", "version": 3,
                                                                                    "data": {"topic": "psychology", "ep": "x-2026-11", "stage": "title", "pass": True}}), "utf-8")
        (d / "tts").mkdir()
        (d / "tts" / "a.json").write_text(json.dumps({"topic": "psychology", "ep": "y", "make": True}), "utf-8")
        c = load_dump(d)
        check("db 내려받기 두 꼴", c["gates"][0]["pass"] is True and c["gates"][0]["version"] == 3 and c["tts"][0]["id"] == "a")
    check("단계 순서", STAGES.index("codetest") == STAGES.index("voice") + 1 and STAGES[-1] == "upload")
    cfg = {"TOPICS": ["psychology", "stock"], "topic": {}}
    check("v1.1 꺼 둔 주제 = enabled false 문서만", board_disabled(cfg, {"topics": [{"id": "stock", "enabled": False}, {"id": "psychology", "enabled": True}, {"id": "zzz", "enabled": False}]}) == {"stock"})
    check("v1.1 topic_state 글 읽기", topic_state.disabled(text='{"disabled": ["stock"]}') == {"stock"} and topic_state.disabled(text="깨진") == set())
    check("v1.1 칸 자동 찾기 (심리 = analysis.json · thumb_codes)", topic_cfg(load_cfg(), "psychology")["SUCCESS"] == "analysis_json"
          and topic_cfg(load_cfg(), "psychology").get("THUMB_CODES", "").endswith("thumb_codes.tsv") and topic_cfg(load_cfg(), "crisis")["SUCCESS"] == "videos_csv")
    check("doc id 꼴", bool(DOC_ID_RE.fullmatch("psychology__jakku-juneun-2026-11-25__title")))
    mc = {"TOPICS": ["economic", "stock", "crisis"], "MERGE": {"stock": "economic"}, "topic": {}}
    check("v1.4 합치기 — 판 주제 · 폴더 · 끄면 합친 폴더도", board_topics(mc) == ["economic", "crisis"] and folders_of(mc, "economic") == ["economic", "stock"]
          and off_folders(mc, {"economic"}) == {"economic", "stock"} and off_folders(mc, {"crisis"}) == {"crisis"})
    sw = search_words("stock")
    check("v1.7 검색어 목록 = keywords.txt 갈래 + 태그 수 (주식 40 · 외국 15)", sw["n"] >= 30 and sw["ko"][0]["name"] and sw["ko"][0]["words"][0]["w"]
          and any(w["ch"] for g in sw["ko"] for w in g["words"]) and (sw["n_foreign"] > 0) == bool(sw["foreign_src"]))
    rs, cs = success_rows("stock", re.compile("나스닥|s&p", re.I), {})
    check("v1.7 성공 사례 = 기준을 모두 넘는 영상 (구독자 5만 이하 · 7~180일 · 조회수 1만+ · 4분+ · 구독자당 하루 0.1+)",
          bool(rs) and all(r["s"] <= 50000 and 7 <= r["a"] <= 180 and r["v"] >= 10000 and r["m"] >= 4 and r["vs"] >= 0.1 for r in rs) and cs["cases"] <= len(rs))
    check("v1.5 숨긴 편 = studio.toml HIDE 폴더 이름 (있는 폴더만)", all((ROOT / f / "source" / x).is_dir() for f in ("economic", "stock") for x in topic_cfg(load_cfg(), f).get("HIDE", [])))
    check("v1.4 studio.toml 주식 → 재테크 · trend 주제", (load_cfg().get("MERGE") or {}).get("stock") == "economic" and "trend" in load_cfg()["TOPICS"])
    W8 = ["자기계발", "갓생", "동기부여", "미라클모닝", "루틴", "자기관리", "습관", "독서"]
    check("v1.3 트렌드 링크 묶음 8개 = 5 + (첫 단어 + 3)", trend_groups(W8) == [W8[:5], ["자기계발", "자기관리", "습관", "독서"]])
    check("v1.3 트렌드 링크 묶음 5개 이하 = 하나 · 겹친 단어 뺌", trend_groups(["a", "b", "a ", " A"]) == [["a", "b"]] and trend_groups([]) == [])
    with tempfile.TemporaryDirectory() as td:
        base = Path(td)
        rows = [{"id": "selfdev.r1", "n": 1, "words": W8}]
        csv1 = "카테고리: 모든 카테고리\n\n일,자기계발: (대한민국),갓생: (대한민국),동기부여: (대한민국),미라클모닝: (대한민국),루틴: (대한민국)\n2026-09-01,50,10,20,5,30\n2026-09-02,55,12,21,4,33\n"
        docs = [{"id": "selfdev.r1.p1", "q": W8[:5], "time": "today 3-m", "gprop": "youtube", "text": csv1, "file": "multiTimeline.csv"},
                {"id": "selfdev.r1.p2", "q": ["자기계발", "습관"], "time": "today 3-m", "gprop": "youtube", "text": csv1}]     # 옛 단어 — 빼야 함
        (base / "board_csv").mkdir()
        (base / "board_csv" / "r09_p1.csv").write_text("old", "utf-8")
        st = sync_trend_csv("selfdev", rows, docs, {"time": "today 3-m", "gprop": "youtube"}, "2026-11-28T00:00:00+09:00", base=base)
        names = sorted(f.name for f in (base / "board_csv").iterdir())
        check("v1.3 판 CSV 옮기기 — 같은 것만 · 옛 파일 지움 · 완료 수", st["need"] == 2 and st["have"] == 1 and not st["done"] and names == ["index.json", "r01_p1.csv"])
        st2 = sync_trend_csv("selfdev", rows, docs, {"time": "today 12-m", "gprop": "youtube"}, "2026-11-28T00:00:00+09:00", base=base)
        check("v1.3 기간이 바뀌면 CSV 다시", st2["have"] == 0)
    print("selftest:", "OK" if ok else "FAIL")
    return 0 if ok else 1


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="제작 판 — build · sync · selftest")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build")
    b.add_argument("--out", default=str(STUDIO / "build"))
    b.add_argument("--topics", default="", help="쉼표로 (기본 = studio.toml TOPICS)")
    s = sub.add_parser("sync")
    s.add_argument("dump", help="ArtifactData list out_dir 로 받은 폴더")
    sub.add_parser("selftest")
    a = ap.parse_args(argv)
    logging.basicConfig(level=getattr(logging, a.log_level), format="%(message)s", stream=sys.stdout)
    if a.cmd == "build":
        return build(Path(a.out), [t for t in a.topics.split(",") if t] or None)
    if a.cmd == "sync":
        return sync(Path(a.dump))
    return selftest()


if __name__ == "__main__":
    raise SystemExit(main())
