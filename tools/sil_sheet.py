#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-11-26 — 실루엣 시트(흰 바탕 · 검은 실루엣 · 칸마다 한 동작) → 투명 실루엣 프레임 띠 + 장면 파일이 읽는 목록(have.js).
#   사용자 지시 2026-11-26 "지금 영상이 고정 이미지만 나오잖아 검은색 실루엣이 움직이는 효과 내도록 따로 여러 상태 이미지 생성해야지 …"
#   요청 파일 crisis/source/hallasan-simjeongji-2026-11/images_chatgpt_states.md (SIL-01~11 · MED-S-STATES · PLT-01~08).
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.0 | 2026-11-26 | 최초 — 흰 바탕 → 투명 · 칸 자르기 · 몸통 가운데·발바닥 맞춤 · MED 칸 자르기 · have.js | load_alpha · cut_cells · build_strip · main |
"""실루엣 시트를 영상 부품으로 바꾼다 (원본 그림은 고치지 않음).

  python3 tools/sil_sheet.py <주제> <영상ID> [--src <그림 폴더>] [--out <출력 폴더>] [--check]
    · 그림 폴더 기본 = <주제>/source/<영상ID>/images  · 출력 기본 = video/episodes/<영상ID>/sprites
    · 출력: <이름>.png (프레임을 가로로 이은 띠, 투명 바탕 · 검은 실루엣) · MED-S-STATES_<k>.jpg (칸별) · have.js (장면 파일이 읽음)
    · 그림이 하나도 없어도 have.js 를 만든다 (장면 파일은 없는 것을 옛 사진으로 대신 보여 줌).
    · --check: 쓰지 않고 칸 검사만 (칸 밖으로 나간 그림·빈 칸·크기가 크게 다른 칸 → WARN).
결과: [STAGE] [시각] key=value … 줄. ※ 연구·교육용 영상 제작 도구.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path

import numpy as np
from PIL import Image

VERSION = "v1.0"
ROOT = Path(__file__).resolve().parent.parent
# 시트 이름 → (칸 가로 수, 칸 세로 수) — 요청 파일의 GRID 와 같게
SHEETS = {
    "SIL-01-KIM-WALK": (3, 2), "SIL-02-KIM-STATES": (3, 2), "SIL-03-KIM-WALK-BACK": (3, 2),
    "SIL-04-COMP-WALK": (2, 2), "SIL-05-COMP-STATES": (2, 2), "SIL-06-RESCUER": (3, 2),
    "SIL-07-STRETCHER": (2, 2), "SIL-08-SIGNS": (3, 2), "SIL-09-SLOPE": (3, 2),
    "SIL-10-CPR": (2, 2), "SIL-11-PREP": (3, 2),
}
MED = {"MED-S-STATES": (3, 2)}
PLATES = ["PLT-01-TRAIL-SIDE", "PLT-02-ENTRANCE-SIDE", "PLT-03-SEARCH-SIDE", "PLT-04-SLOPE-UP",
          "PLT-05-SLOPE-DOWN", "PLT-06-CLEARING", "PLT-07-CLINIC", "PLT-08-LIVING"]
WHITE, BLACK = 232, 40          # 이 밝기 위는 투명, 아래는 불투명 (사이는 부드러운 가장자리)
PAD = 12                        # 프레임 둘레 여백 (px)


def log(stage: str, **kv) -> None:
    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print(f"[{stage}] [{now}] " + " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) and (' ' in v or not v) else v}"
                                          for k, v in kv.items()), flush=True)


def load_alpha(path: Path) -> np.ndarray:
    """흰 바탕 · 검은 실루엣 JPEG → 불투명도 0~1 (검을수록 1)."""
    g = np.asarray(Image.open(path).convert("L"), dtype=np.float32)
    return np.clip((WHITE - g) / (WHITE - BLACK), 0.0, 1.0)


def cut_cells(a: np.ndarray, cols: int, rows: int, name: str) -> list[dict]:
    """칸마다 그림의 테두리 상자 · 몸통 가운데(위 45% 의 무게 중심) · 발바닥 줄을 찾는다."""
    H, W = a.shape
    cw, ch = W / cols, H / rows
    cells = []
    for r in range(rows):
        for c in range(cols):
            x0, y0, x1, y1 = round(c * cw), round(r * ch), round((c + 1) * cw), round((r + 1) * ch)
            sub = a[y0:y1, x0:x1]
            m = sub > 0.16
            k = len(cells) + 1
            if m.sum() < 200:
                log("WARN", sheet=name, cell=k, why="빈 칸 — 그림이 없음")
                cells.append(None)
                continue
            ys, xs = np.nonzero(m)
            bx0, bx1, by0, by1 = xs.min(), xs.max() + 1, ys.min(), ys.max() + 1
            edge = [bx0 <= 1, by0 <= 1, bx1 >= sub.shape[1] - 1, by1 >= sub.shape[0] - 1]
            if any(edge):
                log("WARN", sheet=name, cell=k, why="그림이 칸 가장자리에 닿음 — 옆 칸과 겹쳤을 수 있음", edge=edge)
            top = m[by0:by0 + max(1, int((by1 - by0) * 0.45))]
            tys, txs = np.nonzero(top)
            cx = float(txs.mean()) if len(txs) else (bx0 + bx1) / 2
            cells.append({"k": k, "img": sub[by0:by1, bx0:bx1], "cx": cx - bx0, "w": int(bx1 - bx0), "h": int(by1 - by0)})
    hs = [c["h"] for c in cells if c]
    if hs:
        med = float(np.median(hs))
        for c in cells:
            if c and abs(c["h"] - med) / med > 0.28:
                log("WARN", sheet=name, cell=c["k"], why="다른 칸과 키가 크게 다름 (앉음·누움 칸이면 정상)", h=c["h"], median=round(med))
    return cells


def build_strip(cells: list[dict]) -> tuple[Image.Image, dict]:
    """프레임을 같은 크기로 맞춰 가로로 잇는다 — 몸통 가운데를 프레임 가운데에, 발바닥을 프레임 아래(PAD 위)에."""
    ok = [c for c in cells if c]
    left = max(c["cx"] for c in ok)
    right = max(c["w"] - c["cx"] for c in ok)
    fw = int(np.ceil(2 * max(left, right))) + 2 * PAD
    fh = max(c["h"] for c in ok) + 2 * PAD
    strip = np.zeros((fh, fw * len(cells)), dtype=np.float32)
    for i, c in enumerate(cells):
        if not c:
            continue
        ox = i * fw + int(round(fw / 2 - c["cx"]))
        oy = fh - PAD - c["h"]
        strip[oy:oy + c["h"], ox:ox + c["w"]] = np.maximum(strip[oy:oy + c["h"], ox:ox + c["w"]], c["img"])
    rgba = np.zeros((fh, strip.shape[1], 4), dtype=np.uint8)
    rgba[..., 3] = (strip * 255).round().astype(np.uint8)          # 색은 검정 그대로, 불투명도만
    return Image.fromarray(rgba, "RGBA"), {"n": len(cells), "fw": fw, "fh": fh, "feet": fh - PAD,
                                           "empty": [i + 1 for i, c in enumerate(cells) if not c]}


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("topic"); ap.add_argument("vid")
    ap.add_argument("--src"); ap.add_argument("--out"); ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    src = Path(a.src) if a.src else ROOT / a.topic / "source" / a.vid / "images"
    out = Path(a.out) if a.out else ROOT / "video" / "episodes" / a.vid / "sprites"
    log("START", tool=f"sil_sheet.py {VERSION}", src=str(src), out=str(out), check=a.check)
    have = {"version": VERSION, "made": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "sheets": {}, "med": {}, "plates": []}
    if not a.check:
        out.mkdir(parents=True, exist_ok=True)
    for name, (cols, rows) in SHEETS.items():
        p = src / f"{name}.jpg"
        if not p.is_file():
            log("SKIP", sheet=name, why="그림 없음 — 장면 파일은 옛 사진으로 대신")
            continue
        alpha = load_alpha(p)
        cells = cut_cells(alpha, cols, rows, name)
        if not any(cells):
            continue
        img, meta = build_strip(cells)
        meta["file"] = f"sprites/{name}.png"
        have["sheets"][name] = meta
        if not a.check:
            img.save(out / f"{name}.png", optimize=True)
        log("SHEET", sheet=name, grid=f"{cols}x{rows}", frames=meta["n"], frame=f"{meta['fw']}x{meta['fh']}", empty=meta["empty"] or "-")
    for name, (cols, rows) in MED.items():
        p = src / f"{name}.jpg"
        if not p.is_file():
            log("SKIP", sheet=name, why="그림 없음")
            continue
        im = Image.open(p).convert("RGB")
        W, H = im.size
        files = []
        for r in range(rows):
            for c in range(cols):
                k = r * cols + c + 1
                cell = im.crop((round(c * W / cols), round(r * H / rows), round((c + 1) * W / cols), round((r + 1) * H / rows)))
                f = f"sprites/{name}_{k}.jpg"
                if not a.check:
                    cell.save(out / f"{name}_{k}.jpg", quality=92)
                files.append(f)
        have["med"][name] = files
        log("MED", sheet=name, cells=len(files))
    for name in PLATES:
        if (src / f"{name}.jpg").is_file():
            have["plates"].append(name)
    log("PLATES", have=len(have["plates"]), names=",".join(have["plates"]) or "-")
    if not a.check:
        (out / "have.js").write_text("/* tools/sil_sheet.py 가 만듦 — 손으로 고치지 않음 */\nwindow.SPRITES = "
                                     + json.dumps(have, ensure_ascii=False) + ";\n", "utf-8")
    log("DONE", sheets=len(have["sheets"]), med=len(have["med"]), plates=len(have["plates"]),
        next="장면 파일을 다시 렌더 (node video/render/render.mjs video <주제> <영상ID>)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
