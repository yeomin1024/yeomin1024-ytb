#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-17 — 쇼츠 썸네일(= 첫 문장 화면 그림)에 빈 단색 띠·여백이 있는지 재기.
#          사용자 지시 2026-10-17 "야 넌 이게 비율이 맞는다고 생각해? 검은색 여백있는건 뭔데 다시 수정해" — 1차 그림 4장은
#          프롬프트가 위 13%·아래 34%를 '빈 짙은 남색'으로 두라고 해서 사진이 가운데에만 있고 위·아래·오른쪽이 남색 띠였다
#          (위 12~17% · 아래 39~41% · 오른쪽 14~19%). 규칙: guides/thumbnail_guide.md 12번 '사진이 끝까지'.
#          render.mjs v1.14 가 쇼츠 최종 렌더 전에 부르고, Claude 검수(thumbnail_guide 10번) 때도 쓴다.
r"""
  python3 tools/cover_check.py <그림> [<그림> …]     # 끝 코드: 하나라도 띠가 있으면 1
가장자리에서 안쪽으로 '무늬 없는 줄'(밝기 표준편차 < 6 이고 옆 픽셀 차이 평균 < 1.5)이 몇 % 이어지는지 잰다.
위·아래는 가로줄, 왼쪽·오른쪽은 세로줄. 한 쪽이라도 MAX_BAND(8%)를 넘으면 '여백'.
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image

FLAT_STD = 6.0      # 한 줄의 밝기 표준편차가 이보다 작고
FLAT_DIFF = 1.5     # 이웃 픽셀 밝기 차이 평균이 이보다 작으면 '무늬 없는 줄' (사진은 보통 20+ · 3+, 남색 띠는 1 · 0.3)
MAX_BAND = 0.08     # 한 쪽 띠가 이 비율을 넘으면 여백 (1차 그림은 12~42%, 롱폼 사진 썸네일은 0~7%)


def _run(flags):
    n = 0
    for f in flags:
        if not f:
            break
        n += 1
    return n


def bands(path):
    """→ {'top','bottom','left','right': 비율(0~1)}, (가로, 세로)"""
    a = np.asarray(Image.open(path).convert("L"), dtype=float)
    h, w = a.shape
    rows = (a.std(axis=1) < FLAT_STD) & (np.abs(np.diff(a, axis=1)).mean(axis=1) < FLAT_DIFF)
    cols = (a.std(axis=0) < FLAT_STD) & (np.abs(np.diff(a, axis=0)).mean(axis=0) < FLAT_DIFF)
    return {"top": _run(rows) / h, "bottom": _run(rows[::-1]) / h,
            "left": _run(cols) / w, "right": _run(cols[::-1]) / w}, (w, h)


def check(path):
    b, (w, h) = bands(path)
    bad = {k: v for k, v in b.items() if v > MAX_BAND}
    ratio = w / h
    vertical = abs(ratio - 9 / 16) < 0.01 or abs(ratio - 2 / 3) < 0.01
    print(f"[COVER] file={path} size={w}x{h} ratio={ratio:.4f}({'세로 9:16·2:3' if vertical else '세로 아님'}) "
          + " ".join(f"{k}={v:.1%}" for k, v in b.items())
          + (f" → ❌ 빈 띠: {', '.join(f'{k} {v:.0%}' for k, v in bad.items())} (사진이 화면 끝까지 차야 함 — thumbnail_guide 12번, ChatGPT 로 다시)" if bad else " → ✅ 여백 없음"))
    if not vertical:
        print(f"[COVER] ⚠️ {path}: 세로 9:16(또는 2:3)이 아님 — 쇼츠 화면을 꽉 채우지 못함")
    return not bad and vertical


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    ok = [check(p) for p in argv if Path(p).exists() or print(f"[COVER] ❌ 파일 없음: {p}")]
    return 0 if ok and all(ok) and len(ok) == len(argv) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
