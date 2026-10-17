#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-18 — 세 칸(band) 쇼츠 썸네일의 '문구 칸'과 '사진 칸'을 그대로 잘라 아래로 옮긴다 (새로 그리지 않음 — 픽셀만 옮김).
#          ChatGPT 가 문구를 높이 12~14% 부터 그려 4:5 로 잘리는 선(15%) 위에 걸쳤을 때 쓴다. 사용자 지시 2026-10-18 "썸네일 다시 생성했으니
#          다시 확인해봐" 검수 때 4장 모두 글자가 12.1~14.3% 부터라 고침 (그 전 사용자 지시 2026-10-17 "PC나 모바일에서 볼 때 위 아래 영역이
#          좀 짤릴 수 있는데 그러면 안돼"). 칸 찾기는 tools/cover_check.py v1.1 band 와 같은 규칙.
r"""
  python3 tools/cover_shift.py <원본 그림> <새 그림> [--text-top 0.165] [--gap 0.02]
문구 위 끝 = 높이 text-top, 문구 아래 ~ 사진 위 틈 = gap. 사진 아래 끝이 85% 를 넘으면 멈춤 (4:5 로 잘림).
원본은 thumbnails/original/ 에 두고 새 그림을 thumbnail_1.png 로 (검수 기록에 적는다).
"""
import argparse
import sys
from pathlib import Path

import numpy as np
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cover_check as cc  # noqa: E402


def _runs(flags):
    out, s = [], None
    for i, f in enumerate(flags):
        if f and s is None:
            s = i
        elif not f and s is not None:
            out.append((s, i)); s = None
    if s is not None:
        out.append((s, len(flags)))
    return out


def panels(a):
    """→ (사진 칸 위, 아래, 문구 위, 아래) 픽셀 줄 — cover_check.check_band 와 같은 판정"""
    h, w = a.shape
    e = max(2, int(w * cc.EDGE))
    side = lambda s: (s.mean(axis=1) > cc.DARK) | (s.std(axis=1) > 8)
    nb = (a >= cc.BLACK).mean(axis=1)
    photo = (nb > 0.85) | ((nb > 0.5) & (side(a[:, :e]) | side(a[:, -e:])))
    merged = []
    for s, t in _runs(photo):
        if merged and s - merged[-1][1] <= h * 0.01:
            merged[-1] = (merged[-1][0], t)
        else:
            merged.append((s, t))
    if not merged:
        raise SystemExit("[SHIFT] level=error reason=사진 칸 없음 (세 칸 그림이 아님 — cover_check.py 로 먼저)")
    ps, pe = max(merged, key=lambda r: r[1] - r[0])
    tr = np.where((a[:ps] > cc.INK).mean(axis=1) > 0.003)[0]
    if len(tr) == 0:
        raise SystemExit("[SHIFT] level=error reason=위 칸에 글자 없음")
    return ps, pe, int(tr.min()), int(tr.max()) + 1


def shift(src, dst, text_top=0.165, gap=0.02):
    im = Image.open(src).convert("RGB")
    a = np.asarray(im.convert("L"), dtype=float)
    h, w = a.shape
    ps, pe, ts, te = panels(a)
    m = int(h * 0.004)                                   # 외곽선 끝까지
    ts0, te0 = max(0, ts - m), min(ps, te + m)
    new_ts0 = int(round(h * text_top)) - (ts - ts0)
    new_ps = new_ts0 + (te0 - ts0) - (te0 - te) + int(round(h * gap))
    if (new_ps + pe - ps) / h > cc.SAFE_BOT:
        raise SystemExit(f"[SHIFT] level=error reason=옮기면 사진 아래 끝이 {(new_ps + pe - ps) / h:.0%} — 85% 를 넘음 (ChatGPT 로 다시)")
    out = Image.new("RGB", (w, h), (0, 0, 0))
    out.paste(im.crop((0, ts0, w, te0)), (0, new_ts0))
    out.paste(im.crop((0, ps, w, pe)), (0, new_ps))
    out.save(dst)
    print(f"[SHIFT] src={src} dst={dst} 글자 {ts / h:.1%}~{te / h:.1%} → {text_top:.1%}~{(text_top * h + te - ts) / h:.1%} · "
          f"사진 {ps / h:.1%}~{pe / h:.1%} → {new_ps / h:.1%}~{(new_ps + pe - ps) / h:.1%}")
    return dst


def main(argv=None):
    ap = argparse.ArgumentParser(description="세 칸 쇼츠 썸네일의 문구·사진 칸을 아래로 옮기기 (4:5 안전 구역)")
    ap.add_argument("src"); ap.add_argument("dst")
    ap.add_argument("--text-top", type=float, default=0.165)
    ap.add_argument("--gap", type=float, default=0.02)
    o = ap.parse_args(argv)
    shift(o.src, o.dst, o.text_top, o.gap)
    return 0 if cc.check_band(o.dst) else 1


if __name__ == "__main__":
    sys.exit(main())
