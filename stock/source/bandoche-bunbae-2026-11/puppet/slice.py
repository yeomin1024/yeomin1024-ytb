#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-11-06 — 인물 칸을 내용 폭으로 잘라 냄 (기준점 x = 칸 가운데 그대로 — ax 가 그림 가운데가 아닐 수 있음): 칸 전체 폭이면 배치 점검에서
#          두 인물 상자가 겹치고 화면 밖으로 나감 (layout-check 78 문제 중 다수).
# 이전 v1.0 — 2026-11-06 — 사용자 지시 "그림 올렸으니 영상 만들어서 보여줘": ChatGPT 시트(images_chatgpt.md v1.2 — 한 장에 같은 사람 연속 동작 3개 ·
#          소품 4·8개)를 칸마다 잘라 cut/<이름>-<번호>.png 로 (있는 픽셀만 자르고 크기만 바꿈 — 새로 그리지 않음).
#          · 인물 시트: 칸(가로 3등분) 전체 폭 × [시트 안 가장 높은 머리 위 − 여백, 발바닥 선] — 같은 시트의 자세는 같은 크기·같은 발 선(아래 가운데가 기준점)
#          · 크기 맞춤: 시트마다 첫 자세(서 있음)의 키를 그 사람 기준 키(A = A-HAPPY 1 · B = B-CALM 1)에 맞춤 — 서 있는 첫 자세가 없는 A-RUIN 은
#            SCALE_FIX 1.07 (Claude 가 A-HAPPY 1 옆에 1.0·1.07·1.166 을 놓고 머리 크기로 봄 — 다른 A 시트 가운데값 1.166 은 11% 커 보였음)
#            · 얼굴 시트·소품은 맞추지 않음 (그림 그대로 잘라 테두리만 줄임) · 저장은 256색 (투명 유지 — 6.2MB → 줄임)
#          · cut/manifest.json: 이름마다 크기·기준점(발 선 가운데)·배율 — 장면 파일이 읽음
# 실행: python3 stock/source/bandoche-bunbae-2026-11/puppet/slice.py      로그: [STAGE] [시각] key=value …
from __future__ import annotations

import json
import time
from pathlib import Path

import numpy as np
from PIL import Image

HERE = Path(__file__).resolve().parent
OUT = HERE / "cut"
CHAR = {"A-HAPPY": "A", "A-BUY": "A", "A-MOCK": "A", "A-PANIC": "A", "A-RUIN": "A",
        "B-CALM": "B", "B-REACT": "B", "B-WIN": "B"}
REF = {"A": "A-HAPPY", "B": "B-CALM"}
NO_STANDING = {"A-RUIN"}                         # 첫 자세가 서 있지 않음 (다리 풀림)
SCALE_FIX = {"A-RUIN": 1.07}                     # 머리 크기로 눈으로 맞춘 배율 (위 주석)
PROPS = {"A-FACE": (3, 1), "B-FACE": (3, 1), "P-AI": (4, 1), "P-SECTOR": (4, 2), "P-FX": (4, 1)}
PAD = 10


def log(stage: str, **kv):
    print(f"[{stage}] [{time.strftime('%Y-%m-%dT%H:%M:%S')}] " + " ".join(f"{k}={v}" for k, v in kv.items()), flush=True)


def load(name: str) -> np.ndarray:
    im = Image.open(HERE / f"{name}.png").convert("RGBA")
    a = np.array(im)
    if a[2, 2, 3] > 0:
        raise SystemExit(f"[LOAD] {name}.png 가 투명이 아님 — 자홍 바탕이면 먼저 빼야 함 (이 시트는 투명이어야)")
    return a


def save(im: Image.Image, path: Path):
    """256색 PNG (투명 유지) — 평면 2D 그림이라 차이가 거의 없음."""
    im.quantize(colors=256, method=Image.Quantize.FASTOCTREE).save(path, optimize=True)


def bbox(mask: np.ndarray):
    ys, xs = np.where(mask)
    return (int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1) if len(xs) else None


def main() -> int:
    OUT.mkdir(exist_ok=True)
    man = {}
    # ---- 인물 시트: 칸마다 자르고 시트 배율 구하기 ----
    sheets = {}
    for name in CHAR:
        a = load(name)
        h, w = a.shape[:2]
        cells = []
        for c in range(3):
            x0, x1 = w * c // 3, w * (c + 1) // 3
            b = bbox(a[:, x0:x1, 3] > 40)
            cells.append((x0, x1, b))
        base = max(b[3] for _, _, b in cells)                       # 발바닥 선 (가장 낮은 발)
        top = min(b[1] for _, _, b in cells)
        stand = base - cells[0][2][1]                               # 첫 자세 키
        sheets[name] = dict(a=a, cells=cells, base=base, top=top, stand=stand)
        log("SHEET", name=name, size=f"{w}x{h}", base_y=base, top_y=top, first_pose_height=stand)
    scale = {}
    for name, ch in CHAR.items():
        if name in NO_STANDING:
            continue
        scale[name] = sheets[REF[ch]]["stand"] / sheets[name]["stand"]
    for name in NO_STANDING:
        if name in SCALE_FIX:
            scale[name] = SCALE_FIX[name]
            log("SCALE", name=name, note="SCALE_FIX — 머리 크기로 맞춤", scale=scale[name])
            continue
        others = [scale[n] for n, ch in CHAR.items() if ch == CHAR[name] and n in scale and n != REF[CHAR[name]]]
        scale[name] = float(np.median(others)) if others else 1.0
        log("SCALE", name=name, note="첫 자세가 서 있지 않음 — 같은 사람 다른 시트 배율의 가운데값", scale=round(scale[name], 3))
    for name, s in sheets.items():
        k = scale[name]
        for c, (x0, x1, b) in enumerate(s["cells"], 1):
            y0 = max(0, s["top"] - PAD)
            y1 = min(s["a"].shape[0], s["base"] + 4)
            cx = (x0 + x1) / 2                                          # 기준점 x = 칸 가운데 (시트 안 자세끼리 같은 자리)
            x0, x1 = max(x0, x0 + b[0] - PAD), min(x1, x0 + b[2] + PAD)  # v1.1 내용 폭으로 (투명 여백 뺌)
            crop = Image.fromarray(s["a"][y0:y1, x0:x1])
            if abs(k - 1) > 1e-3:
                crop = crop.resize((round(crop.width * k), round(crop.height * k)), Image.LANCZOS)
            key = f"{name}-{c}"
            save(crop, OUT / f"{key}.png")
            # 기준점 = 칸 가운데 · 발바닥 선 (잘린 그림 안 좌표, 배율 뒤)
            man[key] = dict(kind="char", who=CHAR[name], w=crop.width, h=crop.height, ax=round((cx - x0) * k), ay=round((s["base"] - y0) * k),
                            scale=round(k, 4))
        log("CUT", sheet=name, poses=3, scale=round(k, 3), out_h=man[f"{name}-1"]["h"])
    # ---- 얼굴·소품: 칸마다 내용 테두리로 ----
    for name, (cols, rows) in PROPS.items():
        a = load(name)
        h, w = a.shape[:2]
        n = 0
        for r in range(rows):
            for c in range(cols):
                x0, x1, y0, y1 = w * c // cols, w * (c + 1) // cols, h * r // rows, h * (r + 1) // rows
                b = bbox(a[y0:y1, x0:x1, 3] > 40)
                if not b:
                    raise SystemExit(f"[CUT] {name} 칸 {r},{c} 이 비어 있음")
                n += 1
                bx0, by0 = max(0, x0 + b[0] - PAD), max(0, y0 + b[1] - PAD)
                bx1, by1 = min(w, x0 + b[2] + PAD), min(h, y0 + b[3] + PAD)
                crop = Image.fromarray(a[by0:by1, bx0:bx1])
                key = f"{name}-{n}"
                save(crop, OUT / f"{key}.png")
                man[key] = dict(kind="prop", w=crop.width, h=crop.height, ax=round(crop.width / 2), ay=round(crop.height / 2))
        log("CUT", sheet=name, items=n)
    (OUT / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (OUT / "manifest.js").write_text("// 자동 생성 — slice.py (장면 파일 video/episodes/bandoche-bunbae-2026-11-shorts/index.html 이 읽음)\nwindow.CUT_MANIFEST=" +
                                     json.dumps(man, ensure_ascii=False, separators=(",", ":")) + ";\n", encoding="utf-8")
    total = sum(f.stat().st_size for f in OUT.glob("*.png"))
    log("SUMMARY", cuts=len(man), kb=round(total / 1024), out=str(OUT.relative_to(HERE.parents[3])))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
