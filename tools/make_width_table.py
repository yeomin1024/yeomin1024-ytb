#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-10 — 자막 폰트(Noto Sans KR 700)의 글자 폭 표를 만든다 (srt_tool.py 의 1432px 한 줄 판정용)
"""
  pip install fonttools
  python tools/make_width_table.py video/public/fonts/NotoSansKR-700.ttf tools/subtitle_widths.json

- 한글 음절(가~힣)은 이 폰트에서 모두 같은 폭(920/1000)이라 하나로 적고, 기본 폭(1000)과 다른 글자만 표에 넣는다.
- 자막 폰트를 바꾸면 이 표를 다시 만든다. (영상 자막: 46px Noto Sans KR 700 — guides/video_guide.md 3-3)
"""
import json
import sys
from collections import Counter

from fontTools.ttLib import TTFont

font = TTFont(sys.argv[1])
cmap, hmtx, upm = font.getBestCmap(), font["hmtx"], font["head"].unitsPerEm
hangul = Counter(hmtx[cmap[c]][0] for c in range(0xAC00, 0xD7A4) if c in cmap).most_common(1)[0][0]
default = Counter(hmtx[g][0] for c, g in cmap.items() if not (0xAC00 <= c < 0xD7A4)).most_common(1)[0][0]
widths = {str(c): hmtx[g][0] for c, g in sorted(cmap.items())
          if not (0xAC00 <= c < 0xD7A4) and hmtx[g][0] != default}
out = {"font": sys.argv[1].replace("\\", "/").split("/")[-1], "units_per_em": upm, "default": default,
       "hangul_syllables": hangul, "widths": widths}
with open(sys.argv[2], "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, separators=(",", ":"))
print(f"[WIDTH] {sys.argv[2]}: 기본 {default}, 한글 {hangul}, 예외 {len(widths)}개 (단위 {upm})")
