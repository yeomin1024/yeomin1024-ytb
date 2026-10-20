#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.2 — 2026-10-20 — band: 사진 위 경계의 섞인 줄(높이 0.5% 안, JPEG 경계)을 글자로 세지 않음 — 글자와 사진 사이 틈을 0% 로 잘못 재던 것
#          (test/ 일본 축제 쇼츠 첫 장면 그림: 실제 틈 약 4% 인데 691번째 줄 하나 때문에 ❌). 다른 검사는 그대로.
# (v1.1) — 2026-10-17 — **배치 두 가지**: 'band'(세 칸 — 위 검정 + 문구 2줄 · 가운데 사진 칸 · 아래 검정) 검사 추가.
#          사용자 지시 2026-10-17 "이미지 외 영역은 검은 배경으로 하고 문구는 두 줄로해서 최대 크기로 맞춰 너가 보내준 ISA 만기 쇼츠
#          문구 위치 좀 어긋나 있는데 저렇게 하면 안돼 그리고 PC나 모바일에서 볼 때 위 아래 영역이 좀 짤릴 수 있는데 그러면 안돼"
#          → band 는 ① 사진 칸이 가로 끝까지·높이 약 36~72% ② 위·아래 칸이 검정 ③ 글자·사진이 높이 15~85%(4:5 로 잘리는 선) 안
#          ④ 글자가 사진에 붙지 않음 ⑤ 줄마다 가운데(어긋남 없음) ⑥ 긴 줄이 너비 80% 이상(최대 크기)을 잰다.
#          배치는 그림 옆 thumbnail_1.md 의 'COVER_LAYOUT: band' 로 저절로 고름 (없으면 'full' — 예전 v1.0 검사, 주식 쇼츠).
# (v1.0 — 2026-10-17 — 쇼츠 썸네일(= 첫 문장 화면 그림)에 빈 단색 띠·여백이 있는지 재기 ('full' 배치). 사용자 지시 2026-10-17
#          "야 넌 이게 비율이 맞는다고 생각해? 검은색 여백있는건 뭔데 다시 수정해" — 1차 그림 4장은 위·아래·오른쪽이 빈 남색 띠였다.)
#          render.mjs 가 쇼츠 최종 렌더 전에 부르고, youtube_upload.py 가 쇼츠 썸네일을 올리기 전에 부르고, Claude 검수(thumbnail_guide 10번) 때도 쓴다.
r"""
  python3 tools/cover_check.py <그림> [<그림> …]                # 배치는 그림 옆 thumbnail_1.md 의 COVER_LAYOUT 로 (없으면 full)
  python3 tools/cover_check.py --layout band <그림> [<그림> …]  # 배치를 직접
끝 코드: 하나라도 ❌ 이면 1.
full : 가장자리에서 안쪽으로 '무늬 없는 줄'(밝기 표준편차 < 6, 옆 픽셀 차이 평균 < 1.5)이 한 쪽이라도 8% 넘게 이어지면 '여백'.
band : 위 칸(검정 + 문구 2줄) · 가운데 사진 칸(가로 끝까지) · 아래 칸(검정, 빈 칸). 글자·사진은 높이 15~85% 안 (일부 피드가 4:5 로 잘라 위아래 약 15%씩 안 보임).
"""
import re
import sys
from pathlib import Path

import numpy as np
from PIL import Image

FLAT_STD = 6.0      # 한 줄의 밝기 표준편차가 이보다 작고
FLAT_DIFF = 1.5     # 이웃 픽셀 밝기 차이 평균이 이보다 작으면 '무늬 없는 줄' (사진은 보통 20+ · 3+, 남색 띠는 1 · 0.3)
MAX_BAND = 0.08     # full: 한 쪽 띠가 이 비율을 넘으면 여백 (1차 그림은 12~42%, 롱폼 사진 썸네일은 0~7%)

# band (v1.1) — 높이·너비 비율. 프롬프트(economic/source/*/shorts/thumbnails/thumbnail_1.md v3.0)와 같은 숫자
SAFE_TOP, SAFE_BOT = 0.15, 0.85          # 4:5 로 잘리는 선 (1920 중 가운데 1350 → 위아래 14.8%)
PANEL_TOP = (0.28, 0.44)                 # 사진 칸 위 경계가 이 사이 (프롬프트 36%)
PANEL_BOT = (0.64, 0.80)                 # 사진 칸 아래 경계가 이 사이 (프롬프트 72%)
DARK = 30                                # 검정 칸: 밝기 평균이 이보다 작음
INK = 70                                 # 글자 픽셀: 밝기가 이보다 큼 (검정 위 흰·노랑·빨강 글자)
EDGE = 0.02                              # 사진 줄 판정에 쓰는 왼쪽·오른쪽 가장자리 폭
BLACK = 20                               # 이보다 어두우면 '검정' 픽셀
MIN_GAP = 0.015                          # 글자 아래 ~ 사진 위 최소 틈
MAX_OFF = 0.03                           # 줄 가운데가 화면 가운데에서 벗어나도 되는 폭 (너비 비율)
MIN_TEXT_W = 0.80                        # 가장 긴 줄 너비 (최대 크기)


def _run(flags):
    n = 0
    for f in flags:
        if not f:
            break
        n += 1
    return n


def _runs(flags):
    """True 가 이어진 구간들 → [(시작, 끝+1)]"""
    out, s = [], None
    for i, f in enumerate(flags):
        if f and s is None:
            s = i
        elif not f and s is not None:
            out.append((s, i)); s = None
    if s is not None:
        out.append((s, len(flags)))
    return out


def bands(path):
    """→ {'top','bottom','left','right': 비율(0~1)}, (가로, 세로)"""
    a = np.asarray(Image.open(path).convert("L"), dtype=float)
    h, w = a.shape
    rows = (a.std(axis=1) < FLAT_STD) & (np.abs(np.diff(a, axis=1)).mean(axis=1) < FLAT_DIFF)
    cols = (a.std(axis=0) < FLAT_STD) & (np.abs(np.diff(a, axis=0)).mean(axis=0) < FLAT_DIFF)
    return {"top": _run(rows) / h, "bottom": _run(rows[::-1]) / h,
            "left": _run(cols) / w, "right": _run(cols[::-1]) / w}, (w, h)


def layout_of(path):
    """그림 옆 thumbnail_1.md(또는 같은 이름 .md)에 'COVER_LAYOUT: band' 가 있으면 band, 아니면 full."""
    p = Path(path)
    for md in (p.with_suffix(".md"), p.parent / "thumbnail_1.md"):
        try:
            if md.exists() and re.search(r"COVER_LAYOUT:\s*band", md.read_text("utf-8")):
                return "band"
        except OSError:
            pass
    return "full"


def _vertical(w, h):
    ratio = w / h
    return ratio, abs(ratio - 9 / 16) < 0.01 or abs(ratio - 2 / 3) < 0.01


def check_full(path):
    b, (w, h) = bands(path)
    bad = {k: v for k, v in b.items() if v > MAX_BAND}
    ratio, vertical = _vertical(w, h)
    print(f"[COVER] layout=full file={path} size={w}x{h} ratio={ratio:.4f}({'세로 9:16·2:3' if vertical else '세로 아님'}) "
          + " ".join(f"{k}={v:.1%}" for k, v in b.items())
          + (f" → ❌ 빈 띠: {', '.join(f'{k} {v:.0%}' for k, v in bad.items())} (사진이 화면 끝까지 차야 함 — thumbnail_guide 12번, ChatGPT 로 다시)" if bad else " → ✅ 여백 없음"))
    if not vertical:
        print(f"[COVER] ⚠️ {path}: 세로 9:16(또는 2:3)이 아님 — 쇼츠 화면을 꽉 채우지 못함")
    return not bad and vertical


def check_band(path):
    """(v1.1) 세 칸 배치 검사 → True/False. 문제마다 한 줄씩 이유를 찍는다."""
    a = np.asarray(Image.open(path).convert("L"), dtype=float)
    h, w0 = a.shape
    ratio, vertical = _vertical(w0, h)
    probs, notes = [], []
    if abs(ratio - 2 / 3) < 0.01:                     # 2:3 → 가운데 9:16 으로 잘라 씀: 잘리는 양옆에 글자가 있으면 안 됨
        cw = int(round(h * 9 / 16)); x0 = (w0 - cw) // 2
        side = np.concatenate([a[: int(h * 0.36), :x0], a[: int(h * 0.36), x0 + cw:]], axis=1)
        if (side > INK).mean() > 0.002:
            probs.append("2:3 그림 — 9:16 으로 잘리는 양옆에 글자가 있음")
        a = a[:, x0:x0 + cw]
        notes.append("2:3 → 가운데 9:16 으로 잘라 잼")
    h, w = a.shape
    e = max(2, int(w * EDGE))
    lft, rgt = a[:, :e], a[:, -e:]
    side_on = lambda s: (s.mean(axis=1) > DARK) | (s.std(axis=1) > 8)
    # 사진 줄 = 검정 아닌 픽셀이 85% 넘는 줄, 또는 50% 넘고 가장자리 한쪽에 그림이 있는 줄
    # (글자 줄은 글자 사이·양옆 가장자리가 검정 — 사진이 가장자리만 어두우면 85% 쪽으로 잡힘)
    nb = (a >= BLACK).mean(axis=1)
    photo = (nb > 0.85) | ((nb > 0.5) & (side_on(lft) | side_on(rgt)))
    # 1% 안의 끊김은 메움 (사진 가장자리가 잠깐 어두운 곳)
    runs = _runs(photo)
    merged = []
    for s, t in runs:
        if merged and s - merged[-1][1] <= h * 0.01:
            merged[-1] = (merged[-1][0], t)
        else:
            merged.append((s, t))
    if not merged:
        print(f"[COVER] layout=band file={path} → ❌ 사진 칸이 없음 (가로 끝까지 찬 사진 줄이 없음)")
        return False
    ps, pe = max(merged, key=lambda r: r[1] - r[0])
    pt, pb = ps / h, pe / h
    if not (PANEL_TOP[0] <= pt <= PANEL_TOP[1]):
        probs.append(f"사진 칸 위 경계 {pt:.0%} (프롬프트 36% — {PANEL_TOP[0]:.0%}~{PANEL_TOP[1]:.0%} 이어야)")
    if not (PANEL_BOT[0] <= pb <= PANEL_BOT[1]):
        probs.append(f"사진 칸 아래 경계 {pb:.0%} (프롬프트 72% — {PANEL_BOT[0]:.0%}~{PANEL_BOT[1]:.0%} 이어야)")
    if pb > SAFE_BOT:
        probs.append(f"사진이 높이 {pb:.0%} 까지 — 85% 아래는 4:5 로 잘릴 수 있음")
    # 위 칸: 검정 + 글자
    # v1.2 사진 위 경계에 붙은 '섞인 줄'(JPEG 경계 — 검정과 사진이 반쯤 섞여 사진 줄 기준 85%에 못 미치는 줄)은 글자로 세지 않음.
    #      높이 0.5% 안에서 사진 쪽으로 이어진 줄만 (2026-10-20 test 쇼츠 그림: 691번째 줄 하나 때문에 틈 4% 가 0% 로 재짐)
    k = 0
    while k < max(1, int(h * 0.005)) and ps - k - 1 >= 0 and nb[ps - k - 1] > 0.05:
        k += 1
    top = a[:ps - k]
    ink = top > INK
    tr = np.where(ink.mean(axis=1) > 0.003)[0]
    if len(tr) == 0:
        probs.append("위 칸에 글자가 없음")
        tt = tb = tx0 = tx1 = 0.0; lines = []
    else:
        tt, tb = tr.min() / h, (tr.max() + 1) / h
        tc = np.where(ink.mean(axis=0) > 0.002)[0]
        tx0, tx1 = tc.min() / w, (tc.max() + 1) / w
        if np.median(top[~ink]) > DARK:
            probs.append(f"위 칸 바탕이 검정이 아님 (밝기 중앙값 {np.median(top[~ink]):.0f})")
        if tt < SAFE_TOP - 0.005:
            probs.append(f"글자가 높이 {tt:.1%} 부터 — 15% 위는 4:5 로 잘릴 수 있음")
        if pt - tb < MIN_GAP:
            probs.append(f"글자와 사진 사이 틈 {max(0.0, pt - tb):.1%} — 글자가 사진에 붙거나 겹침 (1.5% 이상)")
        if tx1 - tx0 < MIN_TEXT_W:
            probs.append(f"가장 긴 줄 너비 {tx1 - tx0:.0%} — 최대 크기가 아님 ({MIN_TEXT_W:.0%} 이상, 프롬프트 4~96%)")
        # 줄 나누기: 글자 줄 사이 빈 줄(잉크 없음)로
        lines = [(s, t) for s, t in _runs(ink.mean(axis=1) > 0.003) if (t - s) > h * 0.012]
        for i, (s, t) in enumerate(lines):
            c = np.where(ink[s:t].mean(axis=0) > 0.004)[0]
            if len(c) == 0:
                continue
            mid = (c.min() + c.max() + 1) / 2 / w
            if abs(mid - 0.5) > MAX_OFF:
                probs.append(f"{i + 1}줄 가운데가 {mid:.0%} — 화면 가운데(50%)에서 벗어남 (줄이 어긋남)")
        if len(lines) != 2:
            notes.append(f"글자 줄 {len(lines)}개로 보임 (문구는 2줄 — 외곽선이 붙으면 1개로 셀 수 있음, 눈으로 확인)")
    # 아래 칸: 검정, 빈 칸
    bot = a[pe:]
    if len(bot):
        if np.median(bot) > DARK or (bot > INK).mean() > 0.003:
            probs.append(f"아래 칸이 빈 검정이 아님 (밝기 중앙값 {np.median(bot):.0f}, 밝은 픽셀 {(bot > INK).mean():.1%})")
    if not vertical:
        probs.append("세로 9:16(또는 2:3)이 아님")
    ok = not probs
    print(f"[COVER] layout=band file={path} size={w0}x{a.shape[0]} ratio={ratio:.4f} 사진칸={pt:.0%}~{pb:.0%} "
          f"글자=높이 {tt:.1%}~{tb:.1%}·너비 {tx0:.0%}~{tx1:.0%} 줄={len(lines)}"
          + (" → ✅ 세 칸 배치 (위·아래 검정, 글자·사진이 높이 15~85% 안, 줄 가운데)" if ok else " → ❌ " + " · ".join(probs) + " (thumbnail_guide 12번 — ChatGPT 로 다시)"))
    for n in notes:
        print(f"[COVER] ℹ️ {n}")
    return ok


def check(path, layout=None):
    layout = layout or layout_of(path)
    return check_band(path) if layout == "band" else check_full(path)


def main(argv):
    layout = None
    if argv[:1] == ["--layout"] and len(argv) > 1:
        layout, argv = argv[1], argv[2:]
    if not argv:
        print(__doc__)
        return 2
    ok = [check(p, layout) for p in argv if Path(p).exists() or print(f"[COVER] ❌ 파일 없음: {p}")]
    return 0 if ok and all(ok) and len(ok) == len(argv) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
