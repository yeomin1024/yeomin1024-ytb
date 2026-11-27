#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-11-27 — 최초: 제작 판 (심리·위기 분석 판 두 개를 하나로 — 사용자 지시 2026-11-27
#          "지금 아티팩트가 심리, 위기 2개 있는데 하나로 통합하고 아래 내용을 모두 만족하도록 수정해").
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
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
  trends    <주제> | overall          {words:[…], cats:[…], every_hours, at}
  skills    (자동 id)                 {name, url, memo, createdAt, at}
  uploads   <주제>__<영상ID>          {checks:{항목: bool}, reupload, note, at}
  channels  (자동 id)                 {topic, input, memo, status, reply, createdAt}   — 옛 분석 판의 고정 채널 넣기
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

VERSION = "v1.0"
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
THUMB_W, REF_W = 360, 220  # 판에 넣는 작은 썸네일 폭 (px)

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
def small_jpeg(src: Path, dst: Path, width: int) -> str | None:
    try:
        from PIL import Image
    except ImportError:
        return None
    try:
        dst.parent.mkdir(parents=True, exist_ok=True)
        if not dst.is_file() or dst.stat().st_mtime < src.stat().st_mtime:
            with Image.open(src) as im:
                im = im.convert("RGB")
                h = max(1, round(im.height * width / im.width))
                im.resize((width, h), Image.LANCZOS).save(dst, "JPEG", quality=72, optimize=True)
        return dst.name
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


def refs_psychology(topic: str, tc: dict, img_dir: Path) -> dict:
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
            img = None
            src = ROOT / topic / "result/outliers" / f"W_{vid}" / "thumbnail.jpg"
            if src.is_file():
                nm = small_jpeg(src, img_dir / f"ref_{vid}.jpg", REF_W)
                img = f"img/{topic}/{nm}" if nm else None
            c = succ_ids[vid]
            thumbs.append({"id": f"{topic}.thumb.{vid}", "vid": vid, "text": row.get("main_text", ""), "sub": row.get("sub_text", ""),
                           "image": row.get("image", ""), "face": row.get("face", ""), "img": img, "title": c["title"],
                           "views": c.get("views"), "ratio": c.get("ratio")})
    up = [{"word": w["word"], "rate": w["with"]["rate"], "n": w["with"]["n"], "diff": w["diff"]} for w in a.get("title_words_up", [])]
    down = [{"word": w["word"], "rate": w["with"]["rate"], "n": w["with"]["n"], "diff": w["diff"]} for w in a.get("title_words_down", [])]
    feats = [{"word": f["feature"], "rate": f["with"]["rate"], "n": f["with"]["n"], "diff": f["diff"]} for f in a.get("title_features", [])[:10]]
    return {"titles": titles, "thumbs": thumbs, "words_up": up, "words_down": down, "features": feats,
            "freq": words_of([t["text"] for t in titles]), "source": f"{topic}/result/outliers/analysis.json ({a.get('generated', '?')})",
            "thumb_source": rel(codes) if codes and codes.is_file() else ""}


def refs_videos_csv(topic: str, tc: dict, img_dir: Path) -> dict:
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
    dirs = sorted((d for d in base.glob("board_*") if d.is_dir()), key=lambda d: d.name) if base.is_dir() else []
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
            nm = small_jpeg(p, img_dir / f"{vid}_{p.stem}.jpg", THUMB_W) if img_dir else None
            if nm or img_dir is None:
                thumbs.append({"name": p.name, "img": f"img/{topic}/{nm}" if nm else None})
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
    return ep


def episodes(topic: str, T, img_dir: Path | None, upl_paths: set) -> list[dict]:
    out = []
    sdir = ROOT / topic / "source"
    for d in sorted(p for p in sdir.iterdir() if p.is_dir()) if sdir.is_dir() else []:
        if not VID_RE.fullmatch(d.name):
            continue
        files = {p.name for p in d.iterdir()}
        if not ({f"{d.name}.txt", "package.json", "upload.md"} & files):
            continue
        try:
            out.append(episode(topic, d, d.name, T, img_dir, upl_paths))
        except Exception as e:
            log("EPISODE", logging.WARNING, topic=topic, video=d.name, error=f"{type(e).__name__}: {str(e)[:160]}", next="그 편 폴더 확인")
            continue
        sh = d / "shorts"
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
    return out


def legacy(path: str) -> dict:
    j = read_json(ROOT / path, {}) if path else {}
    j = j or {}
    return {k: j.get(k) for k in ("personas", "log", "videos", "news", "market", "transcript", "made", "note", "stale_days", "today")} | {"from": (j.get("_from") or {}).get("artifact", "")}


def topic_data(topic: str, cfg: dict, out: Path, T, upl_paths: set) -> dict:
    tc = cfg["topic"][topic]
    img_dir = out / "img" / topic
    explore = [x for x in (doc_entry(p) for p in tc.get("EXPLORE", [])) if x]
    rdir = ROOT / tc.get("RELATED_DIR", "")
    related = [x for x in (doc_entry(rel(p)) for p in sorted(rdir.glob("*.md"))) if x] if tc.get("RELATED_DIR") and rdir.is_dir() else []
    refs = refs_psychology(topic, tc, img_dir) if tc.get("SUCCESS") == "analysis_json" else refs_videos_csv(topic, tc, img_dir)
    eps = episodes(topic, T, img_dir, upl_paths)
    d = {"topic": topic, "name": tc.get("NAME", topic), "note": tc.get("NOTE", ""), "explore": explore, "related": related,
         "refs": refs, "episodes": eps, "legacy": legacy(tc.get("LEGACY", "")), "trends": trends_results(topic),
         "default_words": tc.get("WORDS", [])}
    log("TOPIC", topic=topic, explore=len(explore), related=len(related), ref_titles=len(refs["titles"]), ref_thumbs=len(refs["thumbs"]),
        episodes=len(eps), personas=len(d["legacy"].get("personas") or []), trends_period=d["trends"].get("period") or "-")
    return d


def channels_data() -> dict:
    p = STUDIO / "channels" / "channels.json"
    j = read_json(p, None)
    return j or {"made": None, "channels": [], "note": "아직 없음 — python3 tools/channel_stats.py (YOUTUBE_API_KEY 가 있는 세션)"}


def build(out: Path, topics: list[str] | None = None) -> int:
    t0 = time.time()
    cfg = load_cfg()
    topics = topics or cfg["TOPICS"]
    commit = git("rev-parse", "--short=9", "HEAD")
    fetched = subprocess.run(["git", "-C", str(ROOT), "fetch", "-q", "origin", "uploads"], capture_output=True).returncode == 0
    upl = set(git("ls-tree", "-r", "--name-only", "origin/uploads").splitlines()) if fetched else set()
    log("START", tool=f"studio_board.py {VERSION}", commit=commit, topics=",".join(topics), uploads_branch="ok" if fetched else "못 받음",
        note="읽기만 — 저장소에 쓰지 않음 (판 파일은 studio/build/)")
    T = tts_mod()
    out.mkdir(parents=True, exist_ok=True)
    (out / "data").mkdir(exist_ok=True)
    files = {}
    for t in topics:
        d = topic_data(t, cfg, out, T, upl)
        body = json.dumps(d, ensure_ascii=False, separators=(",", ":"))
        (out / "data" / f"{t}.json").write_text(body, "utf-8")
        files[f"data/{t}.json"] = str(out / "data" / f"{t}.json")
    ov = cfg["trends"].get("overall", {})
    common = {"rules": read_json(RULES_PATH, {}), "channels": channels_data(), "overall_trends": trends_results(ov.get("TOPIC", "new")),
              "trends_defaults": {"every_hours": cfg["trends"].get("EVERY_HOURS", 24), "geo": cfg["trends"].get("GEO", "KR"),
                                  "gprop": cfg["trends"].get("GPROP", "youtube"), "time": cfg["trends"].get("TIME", "today 3-m"),
                                  "overall": {"topic": ov.get("TOPIC", "new"), "cats": ov.get("CATS", [0]), "time": ov.get("TIME", "now 7-d")},
                                  "words": {t: cfg["topic"][t].get("WORDS", []) for t in topics}},
              "state": {k: read_json(STATE / f"{k}.json", None) for k in ("trends", "tts_queue", "gates", "reupload", "skills")},
              "synced_at": (read_json(STATE / "board_db.json", {}) or {}).get("synced_at")}
    body = json.dumps(common, ensure_ascii=False, separators=(",", ":"))
    (out / "data" / "common.json").write_text(body, "utf-8")
    files["data/common.json"] = str(out / "data" / "common.json")
    for p in sorted((out / "img").rglob("*.jpg")):
        files[p.relative_to(out).as_posix()] = str(p)
    meta = {"tool": f"studio_board.py {VERSION}", "made": dt.datetime.now(KST).strftime("%Y-%m-%d %H:%M"), "commit": commit,
            "topics": [{"key": t, "name": cfg["topic"][t].get("NAME", t)} for t in topics], "stages": STAGES, "stage_ko": STAGE_KO,
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
    for topic in cfg["TOPICS"]:
        eps = episodes(topic, T, None, set())
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


def sync(dump: Path) -> int:
    t0 = time.time()
    cfg = load_cfg()
    cols = load_dump(dump)
    now = dt.datetime.now(KST).isoformat(timespec="seconds")
    log("SYNC", dump=rel(dump), collections=",".join(f"{k}:{len(v)}" for k, v in sorted(cols.items())) or "-")
    STATE.mkdir(parents=True, exist_ok=True)
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
    for t in cfg["TOPICS"]:
        d = tr.get(t) or {}
        words = [w.strip() for w in (d.get("words") or cfg["topic"][t].get("WORDS", [])) if isinstance(w, str) and w.strip()][:25]
        trends["topics"][t] = {"words": words, "every_hours": int(d.get("every_hours") or tcfg.get("EVERY_HOURS", 24)),
                               "from": "board" if d else "studio.toml"}
    (STATE / "trends.json").write_text(json.dumps(trends, ensure_ascii=False, indent=1) + "\n", "utf-8")
    # 음성 생성 줄 (Kaggle 셀의 tts_narration.py all 이 이것만 만듦)
    q = []
    for d in cols.get("tts", []):
        key = f"{d.get('topic')}/{d.get('ep')}"
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
                                                       "topics": cfg["TOPICS"], "items": q}, ensure_ascii=False, indent=1) + "\n", "utf-8")
    # 다시 올리기 · 스킬
    re_up = [{"topic": d["id"].split("__")[0], "id": d["id"].split("__", 1)[1], "at": d.get("at", ""), "note": d.get("note", "")}
             for d in cols.get("uploads", []) if d.get("reupload") and "__" in d.get("id", "")]
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
    check("doc id 꼴", bool(DOC_ID_RE.fullmatch("psychology__jakku-juneun-2026-11-25__title")))
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
