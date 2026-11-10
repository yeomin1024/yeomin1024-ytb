#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-11-10 — 사용자 지시 "이미지 만들었으니 영상 만들어봐": ChatGPT 시트(images_chatgpt.md v1.0 — 한 장에 같은 사람 연속 동작 3개 ·
#          소품 4개)를 칸마다 잘라 cut/<이름>-<번호>.png 로 (있는 픽셀만 자르고 크기만 바꿈 — 새로 그리지 않음).
#          bandoche-bunbae-2026-11/puppet/slice.py v1.1 과 같은 방법:
#          · 인물 시트: 칸(가로 3등분) 내용 폭 × [시트 안 가장 높은 머리 위 − 여백, 발바닥 선] — 기준점 = 칸 가운데 · 발 선
#          · 크기 맞춤: 시트마다 '서 있는 자세'의 키를 그 사람 기준 키(V = V-CALM 1 · E = E-CALM 3)에 맞춤 — 서 있는 자세가 첫 칸이 아닌 시트는 STAND 로 칸 번호
#          · 소품: 칸마다 내용 테두리로 · 저장은 256색 (투명 유지)
#          · 투명이 아닌 시트(자홍 #FF00FF 바탕)는 자홍을 투명으로 바꿔 읽음
#          · cut/manifest.json · manifest.js: 이름마다 크기·기준점·배율 — 장면 파일(video/episodes/manspi-jeonmang-2026-11/index.html)이 읽음
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.0 | 2026-11-10 | 최초 | load · main |
# 실행: python3 stock/source/manspi-jeonmang-2026-11/puppet/slice.py      로그: [STAGE] [시각] key=value …
from __future__ import annotations

import json
import time
from pathlib import Path

import numpy as np
from PIL import Image

HERE = Path(__file__).resolve().parent
OUT = HERE / "cut"
CHAR = {"V-NIGHT": "V", "V-REACT": "V", "V-CALM": "V",
        "E-HYPE": "E", "E-PUSH": "E", "E-DODGE": "E", "E-CALM": "E", "E-DESK": "E"}
REF = {"V": "V-CALM", "E": "E-CALM"}
STAND = {"V-CALM": 1, "V-NIGHT": 1, "V-REACT": 2, "E-CALM": 3, "E-HYPE": 1, "E-PUSH": 1, "E-DODGE": 1, "E-DESK": 1}   # 똑바로 선 자세 칸 (키 맞춤 기준)
PROPS = {"P-QUOTE": (4, 1), "P-DOCS": (4, 1), "P-MARKS": (4, 1), "P-CHART": (4, 1)}
PAD = 10


def log(stage: str, **kv):
    print(f"[{stage}] [{time.strftime('%Y-%m-%dT%H:%M:%S')}] " + " ".join(f"{k}={v}" for k, v in kv.items()), flush=True)


def load(name: str) -> np.ndarray:
    path = HERE / f"{name}.png"
    try:
        a = np.array(Image.open(path).convert("RGBA"))
    except OSError as ex:
        raise SystemExit(f"[LOAD] {path.name} 를 열 수 없음 ({ex}) — ChatGPT 가 올린 파일 확인 (images_chatgpt.md)")
    if a[2, 2, 3] > 0:                                   # 투명이 아니면 자홍 바탕 → 투명
        r, g, b = (a[:, :, i].astype(int) for i in range(3))
        mag = (r > 200) & (b > 200) & (g < 90)
        a[mag, 3] = 0
        log("LOAD", name=name, note="자홍 바탕을 투명으로", magenta_px=int(mag.sum()))
    return a


def save(im: Image.Image, path: Path):
    """256색 PNG (투명 유지) — 평면 2D 그림이라 차이가 거의 없음."""
    im.quantize(colors=256, method=Image.Quantize.FASTOCTREE).save(path, optimize=True)


def bbox(mask: np.ndarray):
    ys, xs = np.where(mask)
    return (int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1) if len(xs) else None


def main() -> int:
    t0 = time.perf_counter()
    OUT.mkdir(exist_ok=True)
    man = {}
    sheets = {}
    for name in CHAR:
        a = load(name)
        h, w = a.shape[:2]
        cells = []
        for c in range(3):
            x0, x1 = w * c // 3, w * (c + 1) // 3
            b = bbox(a[:, x0:x1, 3] > 40)
            if not b:
                raise SystemExit(f"[CUT] {name} 칸 {c + 1} 이 비어 있음")
            cells.append((x0, x1, b))
        base = max(b[3] for _, _, b in cells)
        top = min(b[1] for _, _, b in cells)
        si = STAND[name] - 1
        stand = base - cells[si][2][1]
        sheets[name] = dict(a=a, cells=cells, base=base, top=top, stand=stand)
        log("SHEET", name=name, size=f"{w}x{h}", base_y=base, top_y=top, stand_pose=STAND[name], stand_height=stand)
    scale = {name: sheets[REF[ch]]["stand"] / sheets[name]["stand"] for name, ch in CHAR.items()}
    for name, s in sheets.items():
        k = scale[name]
        for c, (x0, x1, b) in enumerate(s["cells"], 1):
            y0 = max(0, s["top"] - PAD)
            y1 = min(s["a"].shape[0], s["base"] + 4)
            cx = (x0 + x1) / 2
            x0, x1 = max(x0, x0 + b[0] - PAD), min(x1, x0 + b[2] + PAD)
            crop = Image.fromarray(s["a"][y0:y1, x0:x1])
            if abs(k - 1) > 1e-3:
                crop = crop.resize((round(crop.width * k), round(crop.height * k)), Image.LANCZOS)
            key = f"{name}-{c}"
            save(crop, OUT / f"{key}.png")
            man[key] = dict(kind="char", who=CHAR[name], w=crop.width, h=crop.height, ax=round((cx - x0) * k), ay=round((s["base"] - y0) * k), scale=round(k, 4))
        log("CUT", sheet=name, poses=3, scale=round(k, 3), out_h=man[f"{name}-1"]["h"])
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
    (OUT / "manifest.js").write_text("// 자동 생성 — slice.py (장면 파일 video/episodes/manspi-jeonmang-2026-11/index.html 이 읽음)\nwindow.CUT_MANIFEST=" +
                                     json.dumps(man, ensure_ascii=False, separators=(",", ":")) + ";\n", encoding="utf-8")
    total = sum(f.stat().st_size for f in OUT.glob("*.png"))
    log("SUMMARY", cuts=len(man), kb=round(total / 1024), sec=round(time.perf_counter() - t0, 2), out=str(OUT.relative_to(HERE.parents[3])))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
