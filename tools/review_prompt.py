#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-17 — 최초. 시청자 페르소나 + 대본 전부(문장 번호)를 ChatGPT 가 한 번에 읽을 파일 하나로 묶는다.
#          사용자 지시 2026-10-17 "이 영상의 시청자층을 잘 표현할 수 있는 페르소나를 알려주고 이 대본들을 읽고 피드백 해줄 수 있도록
#          뭐라고 말해야 되는지 알랴줘봐". 페르소나·요청 글 = <주제>/guides/viewer_review.md 의 <!-- REVIEW:BEGIN --> 뒤.
#          문장 번호 = tools/srt_tool.py parse_txt 순서 (SRT·checklist.md·장면 파일과 같음). 결과 = <주제>/script_review_chatgpt.md.
"""python3 tools/review_prompt.py stock [영상ID ...]   # 영상ID 를 빼면 <주제>/source/ 아래 README.md 와 대본(.txt)이 있는 폴더 전부"""
import argparse
import logging
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import srt_tool  # noqa: E402

RAW = "https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/main"
MARK = "<!-- REVIEW:BEGIN -->"
log = logging.getLogger("review_prompt")


def numbered(txt):
    """대본 → ['-파트', 's1 문장', …] — 번호는 srt_tool.parse_txt 와 같은 순서 ([장면] 카드 문구는 읽지 않으므로 뺌)."""
    out, n, card = [], 0, False
    for raw in Path(txt).read_text("utf-8-sig").splitlines():
        line = raw.strip()
        if not line:
            continue
        if srt_tool.is_label(line):
            card = False
            out.append(line)
            continue
        if line.startswith("[장면]"):
            card = True
            continue
        if card:
            continue
        n += 1
        out.append(f"s{n} {line}")
    want = srt_tool.parse_txt(txt)
    got = [x.split(" ", 1)[1] for x in out if re.match(r"s\d+ ", x)]
    if got != want:
        raise SystemExit(f"[REVIEW] 문장 판정이 srt_tool 과 다름: {txt}")
    return out, n


def title_of(src):
    """제목 R1 (titles.md 표의 굵은 제목) — 없으면 빈 글."""
    f = src / "titles.md"
    if not f.exists():
        return ""
    m = re.search(r"\|\s*\*\*R1[^|]*\*\*\s*\|\s*\*\*(.+?)\*\*\s*\|", f.read_text("utf-8"))
    return m.group(1) if m else ""


def order_of(src):
    """README 첫 줄의 '(주식 N번)' → N (없으면 1 — 1번 영상 README 에는 번호가 없음)."""
    m = re.search(r"\(\S+ (\d+)번\)", (src / "README.md").read_text("utf-8").splitlines()[0])
    return int(m.group(1)) if m else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("topic")
    ap.add_argument("ids", nargs="*")
    ap.add_argument("-v", "--verbose", action="store_true")
    a = ap.parse_args()
    logging.basicConfig(level=logging.DEBUG if a.verbose else logging.INFO, format="[%(name)s] %(message)s")
    top = ROOT / a.topic
    pf = top / "guides" / "viewer_review.md"
    if not pf.exists():
        raise SystemExit(f"[REVIEW] 페르소나 파일 없음: {pf.relative_to(ROOT)} — 먼저 만든다")
    body = pf.read_text("utf-8")
    if MARK not in body:
        raise SystemExit(f"[REVIEW] {pf.name} 에 {MARK} 줄이 없음")
    ver = re.search(r"^버전: (v[\d.]+)", body, re.M)
    ids = a.ids or sorted((p.name for p in (top / "source").iterdir()
                           if p.is_dir() and not p.name.startswith("_") and (p / f"{p.name}.txt").exists() and (p / "README.md").exists()),
                          key=lambda v: (order_of(top / "source" / v), v))
    parts, total = [], 0
    for i, vid in enumerate(ids, 1):
        src = top / "source" / vid
        lines, n = numbered(src / f"{vid}.txt")
        total += n
        log.info(f"video={vid} sentences={n} title={title_of(src)!r}")
        parts.append("\n".join([
            f"## 대본 {i}. `{vid}` — {n}문장",
            f"- 제목: {title_of(src) or '(없음)'}",
            f"- 화면 설명: {RAW}/{a.topic}/source/{vid}/README.md (3번)",
            "", "```", *lines, "```", ""]))
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    head = [
        f"# 대본 피드백 요청 — {a.topic} ({len(ids)}편, {total}문장)",
        "",
        f"만든 때: {now} · `tools/review_prompt.py` v1.0 · 페르소나 `{a.topic}/guides/viewer_review.md` {ver.group(1) if ver else ''} · "
        "대본이 바뀌면 다시 만든다 (`python3 tools/review_prompt.py " + a.topic + "`).",
        "",
        "**이 파일을 끝까지 읽고, 아래 1번의 시청자 4명이 되어 대본을 하나씩 읽은 뒤 3번 방법대로 피드백해 주세요.** ※ 연구·교육용 영상 — 투자 권유 아님.",
        "",
    ]
    out = top / "script_review_chatgpt.md"
    out.write_text("\n".join(head) + "\n" + body.split(MARK, 1)[1].strip() + "\n\n---\n\n" + "\n".join(parts), "utf-8")
    log.info(f"wrote={out.relative_to(ROOT)} videos={len(ids)} sentences={total} url={RAW}/{a.topic}/script_review_chatgpt.md")


if __name__ == "__main__":
    main()
