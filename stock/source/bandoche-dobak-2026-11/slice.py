#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-11-14 — 젠슨 황 리스크 편 실사 조각 자르기 (사용자 지시 2026-11-14 "그럼 영상 만들어봐 카메라 워크 신경쓰면서 만스피 영상 처럼").
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.0 | 2026-11-14 | 최초 — 3칸 시트는 칸마다 같은 자르기 상자(세 장 겹침 그대로) · 소품 4×2 는 칸마다 가장 큰 덩어리만 | sheet3 · props · main |
"""ChatGPT 실사 시트(WebP 투명)를 잘라 `puppet/cut/` 에 PNG 조각 + manifest.json·manifest.js (video/render/psy_anim.js 가 읽는 꼴).

- 3칸 시트(Y-REF · Y01 · Y02 · H01): 세 칸을 같은 칸 안 좌표 상자(세 칸 채운 곳의 합)로 자름 → 원화를 바꿔 끼워도 ChatGPT 가 찍은 자리 그대로
  (심리 편 puppet_slice 는 칸마다 키를 다시 맞췄지만, 실사 연속 사진은 이미 같은 크기라 맞추지 않음 — 맞추면 오히려 흔들림).
  기준점 ax = 상자 가운데 · ay = 상자 아래 끝 (의자 바퀴 · 손목 끝). pt.head = 위쪽 15% 상자 (말풍선을 쓰지 않아도 엔진이 요구함).
- 소품(PROPS 4×2): 칸마다 '가장 긴 채운 열 묶음 × 행 묶음' = 가장 큰 덩어리 → ChatGPT 가 남긴 작은 조각(HBM·휴대전화 칸)을 버림.
로그: [STAGE] [시각] key=value   실행: python3 stock/source/bandoche-dobak-2026-11/slice.py
※ 연구·교육용 영상 소스.
"""
from __future__ import annotations

import json
import time
from pathlib import Path

import numpy as np
from PIL import Image

HERE = Path(__file__).resolve().parent
MOT = HERE / "puppet" / "motion"
OUT = HERE / "puppet" / "cut"
PAD = 8
ALPHA = 40


def log(stage: str, **kv):
    print(f"[{stage}] [{time.strftime('%Y-%m-%dT%H:%M:%S')}] " + " ".join(f"{k}={v}" for k, v in kv.items()), flush=True)


def runs(v: np.ndarray):
    """True 가 이어진 구간 [(시작, 끝)] (끝 포함)."""
    out, s = [], None
    for i, x in enumerate(v):
        if x and s is None:
            s = i
        if not x and s is not None:
            out.append((s, i - 1)); s = None
    if s is not None:
        out.append((s, len(v) - 1))
    return out


def sheet3(name: str, man: dict) -> int:
    im = Image.open(MOT / f"{name}.webp").convert("RGBA")
    a = np.array(im)
    h, w = a.shape[:2]
    cw = w // 3
    boxes = []
    for c in range(3):
        m = a[:, c * cw:(c + 1) * cw, 3] > ALPHA
        ys, xs = np.where(m)
        boxes.append((int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max())))
    x0 = max(0, min(b[0] for b in boxes) - PAD); y0 = max(0, min(b[1] for b in boxes) - PAD)
    x1 = min(cw - 1, max(b[2] for b in boxes) + PAD); y1 = min(h - 1, max(b[3] for b in boxes) + PAD)
    W, H = x1 - x0 + 1, y1 - y0 + 1
    for c in range(3):
        crop = im.crop((c * cw + x0, y0, c * cw + x1 + 1, y1 + 1))
        key = f"{name}-{c + 1}"
        crop.save(OUT / f"{key}.png", optimize=True)
        bx = boxes[c]
        man[key] = {"who": name.split("-")[0][:1], "w": W, "h": H, "ax": round(W / 2), "ay": H - PAD,
                    "pt": {"head": [round((bx[0] + bx[2]) / 2 - x0), round(bx[1] - y0 + H * 0.08), round(W * 0.3), round(H * 0.16)]}}
    log("CUT", sheet=name, box=[int(x0), int(y0), int(x1), int(y1)], size=f"{W}x{H}")
    return 3


def props(name: str, man: dict, cols: int = 4, rows: int = 2) -> int:
    im = Image.open(MOT / f"{name}.webp").convert("RGBA")
    a = np.array(im)
    h, w = a.shape[:2]
    cw, ch = w // cols, h // rows
    n = 0
    for r in range(rows):
        for c in range(cols):
            sub = a[r * ch:(r + 1) * ch, c * cw:(c + 1) * cw, 3] > ALPHA
            cr = max(runs(sub.any(axis=0)), key=lambda p: p[1] - p[0])      # 가장 넓은 열 묶음
            cr = (int(cr[0]), int(cr[1]))
            sub2 = sub[:, cr[0]:cr[1] + 1]
            rr = max(runs(sub2.any(axis=1)), key=lambda p: p[1] - p[0])     # 그 안에서 가장 높은 행 묶음
            rr = (int(rr[0]), int(rr[1]))
            x0, x1 = c * cw + max(0, cr[0] - PAD), c * cw + min(cw - 1, cr[1] + PAD)
            y0, y1 = r * ch + max(0, rr[0] - PAD), r * ch + min(ch - 1, rr[1] + PAD)
            crop = Image.fromarray(a[y0:y1 + 1, x0:x1 + 1].copy())
            key = f"{name}-{r * cols + c + 1}"
            crop.save(OUT / f"{key}.png", optimize=True)
            man[key] = {"who": "P", "w": crop.width, "h": crop.height, "ax": crop.width // 2, "ay": crop.height // 2,
                        "pt": {"head": [crop.width // 2, crop.height // 2, crop.width // 2, crop.height // 2]}}
            n += 1
    log("CUT", sheet=name, pieces=n)
    return n


def main() -> int:
    t0 = time.time()
    OUT.mkdir(parents=True, exist_ok=True)
    man: dict = {}
    n = 0
    for s in ("Y-REF", "Y01", "Y02", "H01"):
        n += sheet3(s, man)
    n += props("PROPS", man)
    (OUT / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
    (OUT / "manifest.js").write_text("window.CUT_MANIFEST = " + json.dumps(man, ensure_ascii=False) + ";\n", encoding="utf-8")
    log("DONE", pieces=n, out=str(OUT.relative_to(HERE.parents[2])), seconds=round(time.time() - t0, 1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
