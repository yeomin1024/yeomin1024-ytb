#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-11-13 — 심리 편 그림 시트 자르기 (만스피 slice.py v1.2 를 바탕으로 — 사람마다 머리카락 색 대신 '머리 폭' 으로 키를 잼)
#   사용자 지시 2026-11-13 "1시간 마다 오디오 확인하고 생긴것 부터 영상 만들어" — 만스피 꼴 영상의 인물 조각.
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.0 | 2026-11-13 | 최초 — 기준·동작 시트(3칸) · 소품(4칸) · 배경 앞 물건(FG) · 키 맞춤(앉은 자세 비율) · 머리 상자 | cut_sheet · props · fg · main |
"""ChatGPT 가 그린 심리 편 시트를 잘라 `psychology/source/<영상ID>/puppet/cut/` 에 조각 + `manifest.json`·`manifest.js` 를 만든다.

- 동작·기준 시트(가로 3칸): 칸마다 사람 하나 → `<시트>-<1..3>.png`
  · 키 맞춤: ChatGPT 가 시트마다 사람 크기를 다르게 그림(같은 사람이 키 629~921px) → 칸마다 '머리 꼭대기(머리 폭이 처음 나오는 줄) ~ 발바닥'
    = 그 자세의 키. 세 칸 가운데 값 ÷ 자세 비율(선 자세 1 · 앉음 0.74 …) = 선 키 → STAND_PX(900px)로 맞춤 (어른·아이 모두 900 —
    아이를 작게 하는 것은 장면 파일의 배율).
  · 기준점(ax, ay) = 칸마다 발바닥 선 · 두 발(또는 의자 다리) 가운데 → 원화를 바꿔 끼워도 몸이 제자리.
  · 머리 상자 pt.head = [가운데 x, 가운데 y, 폭, 높이] (말풍선·숫자가 얼굴을 가리지 않게 장면이 씀).
- 소품 시트(가로 4칸): `<시트>-<1..4>.png` (가운데 기준점).
- 배경 앞 물건 FG-*: 배경 그림의 사각형 안 픽셀을 그대로 잘라 인물 앞에 겹침 (새로 그리지 않음).
로그: [STAGE] [시각] key=value …   실행: python3 psychology/source/puppet_slice.py <영상ID> [--sheet 시트이름]
※ 연구·교육용 영상 소스.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
STAND_PX = 900          # 잘라 낸 조각의 '선 키' (머리 꼭대기 ~ 발바닥, px)
PAD = 10
HEAD_W = 0.11           # 머리 꼭대기 = 칸의 채운 폭이 (그 칸 그림 높이 × 이 값) 이상인 첫 줄 — 위로 든 손·주먹은 이보다 좁음
# 자세 비율 (그 시트의 키 ÷ 선 키) — 앉거나 쪼그린 시트만. 칸마다 다르면 [칸1, 칸2, 칸3]
POSE = {
    "geureut-moa-2026-11": {"G01": 0.74, "G02": [0.74, 0.86, 0.74], "G03": 0.74, "G04": [1.0, 0.62, 1.0]},
    "eomma-gibun-2026-11": {"M01": 0.74},
    "eomma-hasoyeon-2026-11": {"D04": [0.74, 0.74, 0.62]},
    "sangcheo-gonggyeok-2026-11": {},
}
# 배경 앞 물건: 이름 → (배경 파일, [x0, y0, x1, y1] — 배경 1536×864 좌표)
FG = {
    "geureut-moa-2026-11": {"FG-TABLE": ("BG-RESTAURANT.jpg", [0, 656, 1536, 864])},   # 식당 앞 식탁 (먼 쪽 가장자리부터) — 앉은 G 가 식탁 뒤에
    "eomma-gibun-2026-11": {},
    "eomma-hasoyeon-2026-11": {},
    "sangcheo-gonggyeok-2026-11": {},
}


def log(stage: str, **kv):
    print(f"[{stage}] [{time.strftime('%Y-%m-%dT%H:%M:%S')}] " + " ".join(f"{k}={v}" for k, v in kv.items()), flush=True)


def load(path: Path) -> np.ndarray:
    try:
        a = np.array(Image.open(path).convert("RGBA"))
    except OSError as ex:
        raise SystemExit(f"[LOAD] {path} 를 열 수 없음 ({ex}) — ChatGPT 가 올린 파일을 확인 (images_chatgpt.md)")
    if a[2, 2, 3] > 0:                                   # 투명이 아니면 자홍 바탕 → 투명
        r, g, b = (a[:, :, i].astype(int) for i in range(3))
        mag = (r > 200) & (b > 200) & (g < 90)
        a[mag, 3] = 0
        log("LOAD", name=path.name, note="자홍 바탕을 투명으로", magenta_px=int(mag.sum()))
    return a


def save(im: Image.Image, path: Path):
    im.quantize(colors=256, method=Image.Quantize.FASTOCTREE).save(path, optimize=True)


def bbox(mask: np.ndarray):
    ys, xs = np.where(mask)
    return (int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1) if len(xs) else None


def person_of(sheet: str) -> str:
    m = re.match(r"^([A-Z]+)(?:-REF|\d+)$", sheet)
    if not m:
        raise SystemExit(f"[CUT] 시트 이름 꼴이 아님: {sheet} (예: A-REF · A01 · MO02)")
    return m.group(1)


def cell_info(sub: np.ndarray) -> dict:
    al = sub[:, :, 3] > 40
    bb = bbox(al)
    if not bb:
        return {}
    base = bb[3]
    rows = al.sum(1)
    thr = HEAD_W * (bb[3] - bb[1])
    top_rows = np.where(rows >= thr)[0]
    top = int(top_rows.min()) if len(top_rows) else bb[1]
    stand = base - top
    xs = np.where(al[int(base - 0.04 * stand):base])[1]
    ax = float((xs.min() + xs.max()) / 2) if len(xs) else (bb[0] + bb[2]) / 2
    band = al[top:int(top + 0.22 * stand)]
    ys_h, xs_h = np.where(band)
    if len(xs_h):
        hx0, hx1 = float(np.percentile(xs_h, 3)), float(np.percentile(xs_h, 97))
    else:
        hx0, hx1 = float(bb[0]), float(bb[2])
    head = [(hx0 + hx1) / 2, top + 0.11 * stand, hx1 - hx0, 0.22 * stand]
    return dict(al=al, bb=bb, base=base, top=top, stand=stand, ax=ax, head=head)


def cut_sheet(ep: str, path: Path, out: Path, man: dict) -> int:
    name = path.stem
    who = person_of(name)
    a = load(path)
    h, w = a.shape[:2]
    cells = []
    for c in range(3):
        x0, x1 = w * c // 3, w * (c + 1) // 3
        sub = a[:, x0:x1]
        info = cell_info(sub)
        if not info:
            raise SystemExit(f"[CUT] {name} 칸 {c + 1} 이 비어 있음 — 다시 받기")
        info["sub"] = sub
        cells.append(info)
    pose = POSE.get(ep, {}).get(name, 1.0)
    poses = pose if isinstance(pose, list) else [pose] * 3
    stands = [c["stand"] / p for c, p in zip(cells, poses)]
    stand = float(np.median(stands))
    k = STAND_PX / stand
    for i, (c, p) in enumerate(zip(cells, poses), 1):
        bb, sub = c["bb"], c["sub"]
        cx0, cy0 = max(0, bb[0] - PAD), max(0, bb[1] - PAD)
        cx1, cy1 = min(sub.shape[1], bb[2] + PAD), min(sub.shape[0], bb[3] + 4)
        crop = Image.fromarray(sub[cy0:cy1, cx0:cx1])
        if abs(k - 1) > 1e-3:
            crop = crop.resize((round(crop.width * k), round(crop.height * k)), Image.LANCZOS)
        key = f"{name}-{i}"
        save(crop, out / f"{key}.png")
        hd = c["head"]
        man[key] = dict(kind="char", who=who, sheet=name, w=crop.width, h=crop.height,
                        ax=round((c["ax"] - cx0) * k), ay=round((c["base"] - cy0) * k), scale=round(k, 4), pose=p,
                        pt={"head": [round((hd[0] - cx0) * k), round((hd[1] - cy0) * k), round(hd[2] * k), round(hd[3] * k)]})
    log("CUT", sheet=name, who=who, stand_px=[round(s) for s in stands], pose=poses, scale=round(k, 3),
        out_h=[man[f"{name}-{i}"]["h"] for i in (1, 2, 3)])
    spread = (max(stands) - min(stands)) / stand
    if spread > 0.12:
        log("CUT", level="warn", sheet=name, note="칸끼리 키가 12% 넘게 다름 — 자세 비율(POSE) 확인", spread=round(spread, 3))
    return 3


def props(path: Path, out: Path, man: dict, cols: int = 4) -> int:
    name = path.stem
    a = load(path)
    h, w = a.shape[:2]
    n = 0
    for c in range(cols):
        x0, x1 = w * c // cols, w * (c + 1) // cols
        b = bbox(a[:, x0:x1, 3] > 40)
        if not b:
            raise SystemExit(f"[CUT] {name} 칸 {c + 1} 이 비어 있음")
        n += 1
        bx0, by0 = max(0, x0 + b[0] - PAD), max(0, b[1] - PAD)
        bx1, by1 = min(w, x0 + b[2] + PAD), min(h, b[3] + PAD)
        crop = Image.fromarray(a[by0:by1, bx0:bx1])
        key = f"{name}-{n}"
        save(crop, out / f"{key}.png")
        man[key] = dict(kind="prop", w=crop.width, h=crop.height, ax=round(crop.width / 2), ay=round(crop.height / 2))
    log("CUT", sheet=name, items=n)
    return n


def fg(ep: str, pup: Path, out: Path, man: dict) -> None:
    for key, (src, (x0, y0, x1, y1)) in FG.get(ep, {}).items():
        try:
            im = Image.open(pup / src).convert("RGBA")
        except OSError as ex:
            raise SystemExit(f"[FG] {src} 를 열 수 없음 ({ex})")
        crop = im.crop((x0, y0, x1, y1))
        crop.save(out / f"{key}.png", optimize=True)
        k = 1920 / im.width
        man[key] = dict(kind="fg", w=crop.width, h=crop.height, x=round(x0 * k), y=round(y0 * k), sw=round(crop.width * k), sh=round(crop.height * k))
        log("FG", key=key, src=src, box=f"{x0},{y0},{x1},{y1}")


def main() -> int:
    ap = argparse.ArgumentParser(description="심리 편 그림 시트 자르기")
    ap.add_argument("ep", help="영상ID (예: eomma-gibun-2026-11)")
    a = ap.parse_args()
    pup = ROOT / "psychology" / "source" / a.ep / "puppet"
    mot, out = pup / "motion", pup / "cut"
    if not mot.is_dir():
        log("LOAD", level="error", msg=f"{mot} 없음", next="ChatGPT 그림이 main 에 왔는지 확인 (git pull)")
        return 1
    out.mkdir(exist_ok=True)
    man: dict = {}
    t0 = time.time()
    n = 0
    for p in sorted(mot.glob("*.png")):
        if p.stem.startswith("PROPS"):
            n += props(p, out, man)
        else:
            n += cut_sheet(a.ep, p, out, man)
    fg(a.ep, pup, out, man)
    (out / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=0), encoding="utf-8")
    (out / "manifest.js").write_text("window.CUT_MANIFEST = " + json.dumps(man, ensure_ascii=False) + ";\n", encoding="utf-8")
    log("DONE", ep=a.ep, pieces=n, manifest=str((out / "manifest.js").relative_to(ROOT)), seconds=round(time.time() - t0, 1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
