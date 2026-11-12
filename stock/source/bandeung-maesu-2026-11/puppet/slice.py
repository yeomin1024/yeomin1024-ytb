#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-11-12 — 반등 편 롱폼 만화 조각 — 사용자 지시 "오디오 만들었으니 반등 영상 만들어봐" → "만스피처럼 만화 인물"
#   만스피 편 slice.py v1.2 의 함수를 그대로 씀(load·hair_mask·head_box·find_pts·motion·props) — 같은 V 기준 키(만스피 V-CALM 1번 칸)로 잘라
#   반등 편 새 동작(V18~V26)과 만스피 편 V 조각을 한 장면에서 섞어도 키·발 자리가 같게.
#   · 동작 시트 V18~V26 (images_chatgpt_long.md 6~14번) → cut/V18-1.png … (프레임마다 발 기준점 · V25 걷기는 엉덩이 가운데)
#   · 소품 PROPS-B(4×1) · 건물 BLDG(4×1, 밑변 기준) · 객차 TRAIN(1×1)
#   · 배경 앞 물건 FG-*: 배경 그림의 있는 픽셀만 (보관실 책상 앞판 · 편의점 탁자 · 승강장 기둥) — 배경이 오면 자리를 재서 FG 표를 채움
#   · 아직 안 온 그림은 건너뜀(로그) — 장면 파일은 없는 조각을 같은 뜻의 만스피 조각으로 잠깐 바꿔 그림(FALLBACK, 렌더 전 0 이어야 함)
#   쓰기: cut/manifest.json · cut/manifest.js (window.CUT_MANIFEST_B)
# 실행: python3 stock/source/bandeung-maesu-2026-11/puppet/slice.py      로그: [STAGE] [시각] key=value …
# 연구·교육용 — 투자 권유 아님.
from __future__ import annotations

import importlib.util
import json
import time
from pathlib import Path

import numpy as np
from PIL import Image

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUT = HERE / "cut"
MOT = HERE / "motion"
MS_PATH = ROOT / "stock/source/manspi-jeonmang-2026-11/puppet/slice.py"

spec = importlib.util.spec_from_file_location("manspi_slice", MS_PATH)
ms = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ms)

SHEETS = {f"V{i}": ("V", "walk" if i == 25 else "feet", []) for i in range(18, 27)}   # V18~V26
PROPS_B = {"PROPS-B": (4, 1), "BLDG": (4, 1), "TRAIN": (1, 1)}
BOTTOM = {"BLDG"}                                    # 밑변 기준 (땅에 선 건물)
# 배경 앞 물건 (배경 1536×864 좌표) — 다각형 안의 있는 픽셀만 (다각형 밖은 투명): 이름 → (배경 파일, [다각형, …])
#   보관실: 책상 윗면·앞판(y 700~) + 왼쪽·오른쪽 책 더미 (그림에서 잰 윤곽 — 인물이 책상 뒤에 서면 책이 몸 앞에)
FG = {"FG-ARCHIVE": ("BG-ARCHIVE.jpg", [
    [(0, 700), (1536, 700), (1536, 864), (0, 864)],
    [(0, 648), (20, 645), (150, 633), (250, 640), (263, 655), (262, 692), (290, 698), (300, 712), (300, 790), (0, 790)],
    [(1236, 702), (1258, 690), (1260, 650), (1290, 637), (1370, 629), (1440, 634), (1525, 646), (1536, 646), (1536, 790), (1236, 790)]])}
# 좌우를 뒤집은 원화를 하나 더 (V23 1·2번 칸이 같은 쪽 손이라 — 왼손 ↔ 오른손 고민이 보이게): 원래 → 새 이름
MIRROR_COPY = {"V23-1": "V23-4"}


def log(stage: str, **kv):
    print(f"[{stage}] [{time.strftime('%Y-%m-%dT%H:%M:%S')}] " + " ".join(f"{k}={v}" for k, v in kv.items()), flush=True)


def ref_stand_v() -> float:
    """만스피 V-CALM 1번 칸의 머리카락 꼭대기 ~ 발바닥 (만스피 slice.py v1.1 과 같은 방법)."""
    a = ms.load("V-CALM")
    w = a.shape[1]
    sub = a[:, 0: w // 3]
    rows = np.where(ms.hair_mask(sub, "V").sum(1) >= 8)[0]
    return float(ms.bbox(sub[:, :, 3] > 40)[3] - rows.min())


def fg(man: dict) -> None:
    from PIL import ImageDraw
    for key, (src, polys) in FG.items():
        p = HERE / src
        if not p.exists():
            log("FG", key=key, skip=f"{src} 없음")
            continue
        im = Image.open(p).convert("RGBA")
        mask = Image.new("L", im.size, 0)
        dr = ImageDraw.Draw(mask)
        for poly in polys:
            dr.polygon(poly, fill=255)
        im.putalpha(mask)
        x0, y0 = min(x for poly in polys for x, _ in poly), min(y for poly in polys for _, y in poly)
        x1, y1 = max(x for poly in polys for x, _ in poly), max(y for poly in polys for _, y in poly)
        crop = im.crop((x0, y0, x1, y1))
        crop.save(OUT / f"{key}.png", optimize=True)
        k = 1920 / im.width
        man[key] = dict(kind="fg", w=crop.width, h=crop.height, x=round(x0 * k), y=round(y0 * k), sw=round(crop.width * k), sh=round(crop.height * k))
        log("FG", key=key, src=src, polys=len(polys), box=f"{x0},{y0},{x1},{y1}")


def mirror_copies(man: dict) -> None:
    for a, b in MIRROR_COPY.items():
        if a not in man:
            continue
        im = Image.open(OUT / f"{a}.png").transpose(Image.FLIP_LEFT_RIGHT)
        ms.save(im.convert("RGBA"), OUT / f"{b}.png")
        m = dict(man[a]); w = m["w"]
        m["ax"] = w - m["ax"]; m["mirror"] = True
        m["pt"] = {k: [w - v[0], v[1], v[2], v[3]] for k, v in m.get("pt", {}).items()}
        man[b] = m
        log("MIRROR", src=a, out=b)


def main() -> int:
    t0 = time.perf_counter()
    OUT.mkdir(exist_ok=True)
    ms.OUT, ms.MOT, ms.MIRROR = OUT, MOT, set()
    have = {k: v for k, v in SHEETS.items() if (MOT / f"{k}.png").exists()}
    miss = sorted(set(SHEETS) - set(have))
    log("INPUT", sheets=len(have), missing=",".join(miss) or "-", props=",".join(k for k in PROPS_B if (MOT / f"{k}.png").exists()) or "-")
    man: dict = {}
    ref = {"V": ref_stand_v()}
    log("REF", V=round(ref["V"]), note="만스피 V-CALM 1번 칸 — 두 편의 V 조각이 같은 키")
    if have:
        ms.MOTION = have
        n = ms.motion(man, ref)
        log("MOTION", frames=n)
    props = {k: v for k, v in PROPS_B.items() if (MOT / f"{k}.png").exists()}
    if props:
        ms.props(man, props, MOT)
        for k in list(man):
            if k.split("-")[0] in BOTTOM:
                man[k]["ay"] = man[k]["h"]
    mirror_copies(man)
    fg(man)
    (OUT / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (OUT / "manifest.js").write_text("// 자동 생성 — stock/source/bandeung-maesu-2026-11/puppet/slice.py (장면 파일 video/episodes/bandeung-maesu-2026-11/index.html 이 읽음)\n"
                                     "window.CUT_MANIFEST_B=" + json.dumps(man, ensure_ascii=False, separators=(",", ":")) + ";\n", encoding="utf-8")
    total = sum(f.stat().st_size for f in OUT.glob("*.png"))
    log("SUMMARY", cuts=len(man), kb=round(total / 1024), sec=round(time.perf_counter() - t0, 2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
