#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.2 — 2026-11-11 — 사용자 지시 "영상 만들 때 캐릭터가 엉뚱한 곳에 있거나 모션 그래픽 요소가 배경이나 이미지들 어울리지 않는 위치에 있거나 어긋나는게 꽤 있는데 그런거 영역을 확실하게 정해서 꼼꼼히 확인해"
#          → 모든 인물 원화에 머리 상자 pt.head(머리카락 꼭대기 ~ 턱, 머리카락 좌우 폭) — 장면 점검(zone-check)이 말풍선·숫자가 얼굴을 가리는지 봄 ·
#          다시 받은 V10 은 던지는 팔이 오른쪽이라 좌우를 뒤집어 자름(MIRROR — 버리는 통이 왼쪽).
# (v1.1 — 2026-11-10 — 사용자 지시 "아니 내말은 원래 방식으로 하되 진짜 애니메이션 처럼 움직이는 효과를 재현하라고 … 더 보충할 이미지가 필요하면 그걸 만들라고"
#          → ChatGPT 움직임용 그림 36장(images_chatgpt_motion.md v1.0 · puppet/motion/)을 더해 자름:
#          · 동작 시트 32장(V01~V17 · E01~E15 — 한 장에 원화 3장): 칸(가로 3등분)마다 잘라 cut/<시트>-<번호>.png
#            - 크기: 머리 꼭대기(머리카락 색)~발바닥 = 서 있는 키 — 세 장의 가운데 값을 그 사람 기준 키(V = V-CALM 1 · E = E-CALM 3)에 맞춤
#              (주먹·도장·서류가 머리 위로 올라가도 키가 흔들리지 않게 — 칸 테두리가 아니라 머리카락으로)
#            - 기준점(ax, ay): 프레임마다 발바닥 선 · 두 발 가운데 (걷기 V05·E07 은 엉덩이 가운데) → 바꿔 끼워도 몸이 제자리
#            - 손에 든 물건 자리(pt): 체(회색 망) · 빈 판(크림) · 저금통(살구) · 저울 접시(금색) · 수정 구슬 · 달력판 · 도장 면 · 입(말풍선 나오는 곳)
#              — 장면 파일이 숫자·말풍선·동전을 그 자리에 붙임 (프레임마다)
#          · 소품 PROPS2(4×1) · FX(4×2) · 배경 앞 물건 FG-*(배경 그림의 있는 픽셀만 잘라 인물 앞에 겹침 — 새로 그리지 않음)
#          v1.0 의 17장 처리는 그대로 (같은 결과).
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.2 | 2026-11-11 | 머리 상자 pt.head (모든 인물 원화) · MIRROR(V10 좌우 뒤집기) | head_box · motion · main |
# | v1.1 | 2026-11-10 | 움직임용 시트 32·소품·FX·앞 물건 · 머리카락 기준 키 · 프레임마다 발 기준점 · 물건 자리 pt | motion · props2 · fg · find_pts |
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
MOT = HERE / "motion"
CHAR = {"V-NIGHT": "V", "V-REACT": "V", "V-CALM": "V",
        "E-HYPE": "E", "E-PUSH": "E", "E-DODGE": "E", "E-CALM": "E", "E-DESK": "E"}
REF = {"V": "V-CALM", "E": "E-CALM"}
STAND = {"V-CALM": 1, "V-NIGHT": 1, "V-REACT": 2, "E-CALM": 3, "E-HYPE": 1, "E-PUSH": 1, "E-DODGE": 1, "E-DESK": 1}   # 똑바로 선 자세 칸 (키 맞춤 기준)
PROPS = {"P-QUOTE": (4, 1), "P-DOCS": (4, 1), "P-MARKS": (4, 1), "P-CHART": (4, 1)}
PAD = 10
# v1.1 움직임 시트: 이름 → (사람, 기준점 방식, 찾을 물건들)
MOTION = {f"V{i:02d}": ("V", "walk" if i == 5 else "feet", []) for i in range(1, 18)}
MOTION.update({f"E{i:02d}": ("E", "walk" if i == 7 else "feet", []) for i in range(1, 16)})
for k, pts in {"V01": ["piggy"], "V02": ["piggy"], "V03": ["coins"], "V08": ["sieve"], "V09": ["sieve"], "V10": ["sieve"], "V11": ["sieve"],
               "V12": ["board"], "E02": ["board"], "E09": ["ball"], "E12": ["stampface"], "E14": ["panL", "panR"]}.items():
    MOTION[k][2].extend(pts)
for k in MOTION:
    if k.startswith("E"):
        MOTION[k][2].append("mouth")
MPROPS = {"PROPS2": (4, 1), "FX": (4, 2)}
MIRROR = {"V10"}                                   # 좌우를 뒤집어 자를 동작 시트 (다시 받은 V10 — 던지는 쪽이 버리는 통 반대라서)
# 배경 앞 물건 (배경 1536×864 좌표의 사각형 — 그 안의 있는 픽셀만): 이름 → (배경 파일, [x0, y0, x1, y1])
FG = {"FG-OFFICE": ("BG-OFFICE.jpg", [0, 661, 1536, 864]),          # 책상 윗면·앞판 (전문가가 책상 뒤에 섬)
      "FG-SIEVE": ("motion/BG-SIEVE0.jpg", [0, 622, 1536, 864]),    # 작업대 윗면·앞판 (시청자가 작업대 뒤에 섬)
      "FG-BIN": ("motion/BG-SIEVE0.jpg", [46, 492, 345, 760]),      # 버리는 통 몸통 (입구 테 아래 — 던진 말이 통 안으로 들어감)
      "FG-BOX": ("motion/BG-SIEVE0.jpg", [1170, 585, 1525, 760]),    # 보관함 앞판 (통과한 말이 상자 안으로)
      "FG-DESK": ("motion/BG-STUDIO0.jpg", [1060, 410, 1536, 700])}  # 스튜디오 책상 (전문가가 책상 뒤에 설 때)


def log(stage: str, **kv):
    print(f"[{stage}] [{time.strftime('%Y-%m-%dT%H:%M:%S')}] " + " ".join(f"{k}={v}" for k, v in kv.items()), flush=True)


def load(name: str, base: Path = HERE) -> np.ndarray:
    path = base / f"{name}.png"
    try:
        a = np.array(Image.open(path).convert("RGBA"))
    except OSError as ex:
        raise SystemExit(f"[LOAD] {path.name} 를 열 수 없음 ({ex}) — ChatGPT 가 올린 파일 확인 (images_chatgpt*.md)")
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


def hair_mask(a: np.ndarray, who: str) -> np.ndarray:
    r, g, b = (a[:, :, i].astype(int) for i in range(3))
    if who == "V":     # 갈색 곱슬머리
        m = (r >= 80) & (r <= 135) & (g >= 50) & (g <= 95) & (b >= 35) & (b <= 80) & (r - b > 25)
    else:              # 짙은 회색 머리
        m = (r >= 50) & (r <= 130) & (g >= 40) & (g <= 120) & (b >= 40) & (b <= 125) & (np.abs(r - b) <= 22) & (np.abs(r - g) <= 25)
    return m & (a[:, :, 3] > 40)


def color_mask(a: np.ndarray, kind: str) -> np.ndarray:
    r, g, b = (a[:, :, i].astype(int) for i in range(3))
    al = a[:, :, 3] > 40
    mx, mn = np.maximum(np.maximum(r, g), b), np.minimum(np.minimum(r, g), b)
    if kind == "sieve":        # 회색 철망
        m = (mx - mn < 20) & (mn > 105) & (mx < 215)
    elif kind == "board":      # 크림색 판·달력 종이
        m = (r > 232) & (g > 212) & (b > 180) & (r - b > 12) & (r - b < 70)
    elif kind == "piggy":      # 살구색 저금통
        m = (r > 225) & (g > 110) & (g < 175) & (b > 85) & (b < 150) & (r - g > 60)
    elif kind == "coins":      # 금화
        m = (r > 215) & (g > 150) & (g < 215) & (b < 90)
    elif kind in ("panL", "panR"):   # 금색 저울
        m = (r > 190) & (g > 135) & (g < 205) & (b < 110)
    elif kind == "ball":       # 수정 구슬 (푸른 회색)
        m = (b > 165) & (b - r > 8) & (b - r < 70) & (g > 150) & (r > 120)
    elif kind == "stampface":  # 도장 면 (크림)
        m = (r > 225) & (g > 200) & (b > 160) & (r - b > 20) & (r - b < 80)
    else:
        raise ValueError(kind)
    return m & al


def pct_box(mask: np.ndarray, lo=3, hi=97):
    ys, xs = np.where(mask)
    if len(xs) < 30:
        return None
    return (float(np.percentile(xs, lo)), float(np.percentile(ys, lo)), float(np.percentile(xs, hi)), float(np.percentile(ys, hi)))


def head_box(sub: np.ndarray, who: str, top: int, base: int):
    """머리 상자 [가운데 x, 가운데 y, 폭, 높이] (원본 칸 좌표) — 머리카락 꼭대기 ~ 턱(키의 32%), 폭은 머리카락 좌우(머리 위 키의 20% 안)."""
    stand = base - top
    hm = hair_mask(sub, who)
    hm[int(top + 0.20 * stand):] = False
    ys, xs = np.where(hm)
    if len(xs) < 20:
        return None
    x0, x1 = float(np.percentile(xs, 2)), float(np.percentile(xs, 98))
    y0, y1 = float(top), float(top + 0.32 * stand)
    return [(x0 + x1) / 2, (y0 + y1) / 2, x1 - x0, y1 - y0]


def find_pts(sub: np.ndarray, who: str, kinds: list[str], top: int, base: int, cx: float) -> dict:
    """칸 하나(원본 좌표)에서 물건 자리 찾기 → {이름: [x, y, w, h]} (원본 칸 좌표)."""
    out = {}
    stand = base - top
    for k in kinds:
        if k == "mouth":       # 입 = 머리 가운데 · 머리 꼭대기에서 키의 17% 아래
            hm = hair_mask(sub, who)
            ys, xs = np.where(hm)
            if len(xs):
                out[k] = [float(np.median(xs)), top + 0.17 * stand, 0, 0]
            continue
        m = color_mask(sub, k)
        if k in ("panL", "panR"):                     # 저울 접시: 가운데 기둥 왼쪽/오른쪽의 가장 아래 금색 덩어리
            xx = np.arange(sub.shape[1])[None, :]
            side = (xx < cx - 0.10 * stand) if k == "panL" else (xx > cx + 0.10 * stand)   # 가운데 기둥·받침은 빼고 양옆만
            mm = m & side
            mm[: int(top + 0.25 * stand)] = False
            ys, xs = np.where(mm)
            if len(xs) < 30:
                continue
            ylo = np.percentile(ys, 70)
            sel = ys >= ylo
            out[k] = [float(np.median(xs[sel])), float(np.median(ys[sel])), float(np.ptp(xs[sel])), float(np.ptp(ys[sel]))]
            continue
        if k in ("board", "stampface"):               # 머리 아래 몸통 쪽만 (셔츠·흰자 빼기 어렵지만 판이 가장 큼)
            m[: int(top + 0.12 * stand)] = False
        b = pct_box(m)
        if b:
            out[k] = [(b[0] + b[2]) / 2, (b[1] + b[3]) / 2, b[2] - b[0], b[3] - b[1]]
    return out


def motion(man: dict, ref_stand: dict) -> int:
    """v1.1 동작 시트 → cut/<시트>-<1..3>.png (같은 배율 · 프레임마다 발 기준점 · 물건 자리)."""
    n = 0
    for name, (who, mode, kinds) in MOTION.items():
        a = load(name, MOT)
        h, w = a.shape[:2]
        cells = []
        for c in range(3):
            x0, x1 = w * c // 3, w * (c + 1) // 3
            sub = a[:, x0:x1]
            al = sub[:, :, 3] > 40
            bb = bbox(al)
            if not bb:
                raise SystemExit(f"[CUT] {name} 칸 {c + 1} 이 비어 있음")
            base = bb[3]
            rows = np.where(hair_mask(sub, who).sum(1) >= 8)[0]
            top = int(rows.min()) if len(rows) else bb[1]
            stand = base - top
            if mode == "walk":                        # 엉덩이 가운데 (키의 52~62%)
                y0, y1 = int(top + 0.52 * stand), int(top + 0.62 * stand)
                xs = np.where(al[y0:y1])[1]
            else:                                     # 두 발 가운데 (맨 아래 4%)
                xs = np.where(al[int(base - 0.04 * stand):base])[1]
            ax = float((xs.min() + xs.max()) / 2) if len(xs) else (bb[0] + bb[2]) / 2
            cells.append(dict(x0=x0, x1=x1, sub=sub, bb=bb, base=base, top=top, stand=stand, ax=ax))
        stand = float(np.median([c["stand"] for c in cells]))
        k = ref_stand[who] / stand
        for i, c in enumerate(cells, 1):
            bb, sub = c["bb"], c["sub"]
            cx0, cy0 = max(0, bb[0] - PAD), max(0, bb[1] - PAD)
            cx1, cy1 = min(sub.shape[1], bb[2] + PAD), min(sub.shape[0], bb[3] + 4)
            pts = find_pts(sub, who, kinds, c["top"], c["base"], c["ax"])
            hb = head_box(sub, who, c["top"], c["base"])
            if hb:
                pts["head"] = hb
            crop = Image.fromarray(sub[cy0:cy1, cx0:cx1])
            ax_src = c["ax"]
            if name in MIRROR:                            # 좌우 뒤집기: 그림·기준점·물건 자리를 함께
                crop = crop.transpose(Image.FLIP_LEFT_RIGHT)
                W0 = cx1 - cx0
                ax_src = cx0 + (W0 - (c["ax"] - cx0))
                pts = {k: [cx0 + (W0 - (v[0] - cx0)), v[1], v[2], v[3]] for k, v in pts.items()}
            if abs(k - 1) > 1e-3:
                crop = crop.resize((round(crop.width * k), round(crop.height * k)), Image.LANCZOS)
            key = f"{name}-{i}"
            save(crop, OUT / f"{key}.png")
            man[key] = dict(kind="char", who=who, w=crop.width, h=crop.height, ax=round((ax_src - cx0) * k), ay=round((c["base"] - cy0) * k),
                            scale=round(k, 4), mirror=name in MIRROR, pt={p: [round((v[0] - cx0) * k), round((v[1] - cy0) * k), round(v[2] * k), round(v[3] * k)] for p, v in pts.items()})
            n += 1
        log("MOTION", sheet=name, who=who, anchor=mode, stand_px=round(stand), scale=round(k, 3), out_h=man[f"{name}-1"]["h"],
            pts=",".join(sorted({p for i in (1, 2, 3) for p in man[f"{name}-{i}"]["pt"]})) or "-")
    return n


def props(man: dict, table: dict, base_dir: Path) -> None:
    for name, (cols, rows) in table.items():
        a = load(name, base_dir)
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


def fg(man: dict) -> None:
    """배경 그림의 사각형 안 픽셀을 그대로 잘라 '앞 물건' 층으로 (1920×1080 무대 좌표 x·y 도 함께)."""
    for key, (src, (x0, y0, x1, y1)) in FG.items():
        try:
            im = Image.open(HERE / src).convert("RGBA")
        except OSError as ex:
            raise SystemExit(f"[FG] {src} 를 열 수 없음 ({ex})")
        crop = im.crop((x0, y0, x1, y1))
        crop.save(OUT / f"{key}.png", optimize=True)
        k = 1920 / im.width
        man[key] = dict(kind="fg", w=crop.width, h=crop.height, x=round(x0 * k), y=round(y0 * k), sw=round(crop.width * k), sh=round(crop.height * k))
        log("FG", key=key, src=src, box=f"{x0},{y0},{x1},{y1}", stage_box=f"{round(x0 * k)},{round(y0 * k)},{round(x1 * k)},{round(y1 * k)}")


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
            cx0_ = s["cells"][c - 1][0]
            sub = s["a"][:, cx0_:s["cells"][c - 1][1]]
            rows = np.where(hair_mask(sub, CHAR[name]).sum(1) >= 8)[0]
            if len(rows):
                hb = head_box(sub, CHAR[name], int(rows.min()), s["base"])
                if hb:
                    man[key]["pt"] = {"head": [round((hb[0] + cx0_ - x0) * k), round((hb[1] - y0) * k), round(hb[2] * k), round(hb[3] * k)]}
        log("CUT", sheet=name, poses=3, scale=round(k, 3), out_h=man[f"{name}-1"]["h"])
    props(man, PROPS, HERE)
    # v1.1 — 기준 키(머리카락 꼭대기 ~ 발바닥)를 같은 방법으로 잼: V-CALM 1번 칸 · E-CALM 3번 칸
    ref_stand = {}
    for who, (sheet, cell) in {"V": ("V-CALM", 1), "E": ("E-CALM", 3)}.items():
        a = sheets[sheet]["a"]
        w = a.shape[1]
        sub = a[:, w * (cell - 1) // 3: w * cell // 3]
        rows = np.where(hair_mask(sub, who).sum(1) >= 8)[0]
        ref_stand[who] = float(bbox(sub[:, :, 3] > 40)[3] - rows.min())
    log("REF", V=round(ref_stand["V"]), E=round(ref_stand["E"]), note="머리카락 꼭대기 ~ 발바닥 (v1.1 시트 크기 맞춤 기준)")
    if MOT.exists():
        nm = motion(man, ref_stand)
        props(man, MPROPS, MOT)
        fg(man)
        log("MOTION", frames=nm)
    (OUT / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (OUT / "manifest.js").write_text("// 자동 생성 — slice.py (장면 파일 video/episodes/manspi-jeonmang-2026-11/index.html 이 읽음)\nwindow.CUT_MANIFEST=" +
                                     json.dumps(man, ensure_ascii=False, separators=(",", ":")) + ";\n", encoding="utf-8")
    total = sum(f.stat().st_size for f in OUT.glob("*.png"))
    log("SUMMARY", cuts=len(man), kb=round(total / 1024), sec=round(time.perf_counter() - t0, 2), out=str(OUT.relative_to(HERE.parents[3])))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
