#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-17 — 유튜브 제목이 화면에서 잘리는지 재기 (글자 수가 아니라 화면 폭 — 유튜브는 폭으로 줄이고 '…'으로 자른다).
#          사용자 지시 2026-10-17 "야 올라간 롱폼 영상 제목이 좀 길어서 잘리는데 모바일, PC 둘다 안 잘리도록 해서 제목만 다시 수정해봐"
#          · "제목 수정한거 공통 지시사항에 반영하고 다른 영상 제목도 반영 안된거 있으면 수정해". 규칙: guides/title_guide.md 5-1.
#          폭은 tools/subtitle_widths.json(Noto Sans KR 700 — 실제 유튜브 글꼴보다 조금 굵어 넉넉하게 잼)으로 계산한 어림값이다.
r"""
  python3 tools/title_fit.py "제목 하나" ["제목 둘" …]          # 롱폼 화면들
  python3 tools/title_fit.py --shorts "쇼츠 제목"               # 쇼츠 화면들
  python3 tools/title_fit.py economic                          # 그 주제 업로드 시트(upload.md · shorts/upload.md·shorts.md R1)의 제목 전부
끝 코드: 어느 화면에서든 3줄 이상(= 잘림)이면 1.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import srt_tool  # noqa: E402  (글자 폭 표 — text_px)

ROOT = Path(__file__).resolve().parent.parent
# 화면: (이름, 글자 px, 제목 칸 폭 px, 보이는 줄) — 2026-10-17 어림 (화면·기기마다 조금씩 다름 → 가장 좁은 칸을 넣음)
LONG = [("PC 다음 동영상 (좁은 화면)", 14, 180, 2), ("PC 다음 동영상", 14, 210, 2), ("모바일 홈·검색 (좁은 폰)", 16, 270, 2),
        ("PC 홈", 16, 300, 2), ("PC 검색", 18, 600, 2)]
SHORTS = [("홈 Shorts 칸 (좁은 폰)", 14, 165, 2), ("쇼츠 재생 화면 아래", 15, 300, 2), ("PC 다음 동영상", 14, 180, 2)]


def wrap(title, px, width):
    words, out, cur = title.split(" "), [], ""
    for w in words:
        c = (cur + " " + w).strip()
        if srt_tool.text_px(c, px) > width and cur:
            out.append(cur)
            cur = w
        else:
            cur = c
    out.append(cur)
    return out


def fit(title, shorts=False):
    """→ (모두 들어감?, [(화면, 줄 목록, 보이는 줄)])"""
    rows = [(name, wrap(title, px, w), n) for name, px, w, n in (SHORTS if shorts else LONG)]
    return all(len(ls) <= n for _, ls, n in rows), rows


def report(title, shorts=False):
    ok, rows = fit(title, shorts)
    print(f"[TITLE] {'✅' if ok else '❌ 잘림'} {len(title)}자 {'(쇼츠)' if shorts else '(롱폼)'} {title}")
    for name, ls, n in rows:
        print(f"    {'✅' if len(ls) <= n else '❌'} {name}: {len(ls)}줄 — " + " / ".join(ls))
    return ok


def topic_titles(topic):
    """업로드 시트 1번 제목 (롱폼 upload.md · 쇼츠 shorts/upload.md, 없으면 shorts.md R1)."""
    out = []
    for up in sorted((ROOT / topic / "source").glob("*/upload.md")):
        m = re.search(r"^## 1\. 제목[^\n]*\n.*?```\n(.*?)\n```", up.read_text("utf-8"), re.S | re.M)
        if m:
            out.append((up.parent.name, m.group(1).strip(), False))
        sh = up.parent / "shorts"
        su, sm = sh / "upload.md", sh / "shorts.md"
        if su.exists():
            m = re.search(r"^## 1\. 제목[^\n]*\n.*?```\n(.*?)\n```", su.read_text("utf-8"), re.S | re.M)
            if m:
                out.append((up.parent.name + "-shorts", m.group(1).strip(), True))
        elif sm.exists():
            m = re.search(r"^\| \*\*R1[^|]*\| \*\*(.+?)\*\* \|", sm.read_text("utf-8"), re.M)
            if m:
                out.append((up.parent.name + "-shorts", m.group(1).strip(), True))
    return out


def main(argv):
    shorts = "--shorts" in argv
    args = [a for a in argv if a != "--shorts"]
    if len(args) == 1 and (ROOT / args[0] / "source").is_dir():
        bad = 0
        for vid, title, sh in topic_titles(args[0]):
            print(f"== {vid}")
            bad += not report(title, sh)
        print(f"[TITLE] 잘리는 제목 {bad}개")
        return 1 if bad else 0
    if not args:
        print(__doc__)
        return 2
    return 0 if all([report(t, shorts) for t in args]) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
