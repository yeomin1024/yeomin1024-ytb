#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.2 — 2026-10-15 — tools/ 로 옮기고 주제 폴더·묶음 낱말을 인자로 (guides/thumbnail_guide.md v3.0 2단계)
#          (v1.1: 저장소 상대 경로, 2-1 표(중앙값·P(성공>기준 밖)·성공 안 순위상관) 계산 / v1.0: 이미지 수치)
r"""썸네일 이미지 수치 — 승인 영상 썸네일(성공 / 기준 밖)의 밝기·채도·색 비율·글자 띠 추정과 비교 표.
연구·교육용. 색 판정은 HSV 범위 규칙(근사).

  python3 tools/thumbnail_metrics.py economic --group 노후,절세 --out <저장 폴더>
    읽기: <주제>/result/outliers/{analysis.json, compare.csv, approved.csv, */thumbnail.jpg}
    쓰기: <저장 폴더>/thumbs.json (기본: .yt_work/thumbnail_metrics/<주제>/ — git 밖)
    로그 [STATS]: 전체·묶음별 중앙값, P(성공>기준 밖)(Mann-Whitney AUC), 성공 안에서 배수와 스피어만 순위상관
"""
import argparse, csv, json, sys, logging, time
from pathlib import Path
import numpy as np
from PIL import Image
logging.basicConfig(level=logging.INFO, format="%(message)s")
def log(stage, **kv): logging.info("[%s] %s %s", stage, time.strftime("%H:%M:%S"), " ".join(f"{k}={v}" for k, v in kv.items()))
ROOT = Path(__file__).resolve().parent.parent  # 저장소 맨 위
ap = argparse.ArgumentParser(description="썸네일 이미지 수치 (성공 vs 기준 밖)")
ap.add_argument("topic", help="주제 폴더 (예: economic)")
ap.add_argument("--group", default="노후,절세", help="따로 볼 주제 묶음 낱말, 쉼표로 (analysis.json theme 에 든 말)")
ap.add_argument("--out", help="thumbs.json 저장 폴더")
args = ap.parse_args()
O = ROOT / args.topic / "result" / "outliers"
OUT = Path(args.out) if args.out else ROOT / ".yt_work" / "thumbnail_metrics" / args.topic
OUT.mkdir(parents=True, exist_ok=True)
if not (O / "analysis.json").is_file():
    sys.exit(f"[LOAD] level=error stage=분석결과 file={O / 'analysis.json'} reason=없음 — 다음: PC 분석(guides/pc_analysis.md)을 먼저 돌려 결과를 올린다")
a = json.load(open(O / "analysis.json", encoding="utf-8"))
succ = {c["id"]: c for c in a["success_cases"]}
theme = {r["id"]: r["theme"] for r in csv.DictReader(open(O / "compare.csv", encoding="utf-8-sig"))}
rows = []
for r in csv.DictReader(open(O / "approved.csv", encoding="utf-8-sig")):
    f = O / r["folder"] / "thumbnail.jpg"
    if not f.is_file():
        log("SKIP", level="warn", id=r["id"], reason="no thumbnail"); continue
    c = succ.get(r["id"])
    rows.append(dict(id=r["id"], folder=r["folder"], success=bool(c), no=c["no"] if c else "", theme=(c or {}).get("theme") or theme.get(r["id"], ""),
                     ratio=float(r["ratio"] or 0), title=r["title"], path=str(f)))
log("LOAD", thumbs=len(rows), success=sum(r["success"] for r in rows))
def metrics(path):
    im = Image.open(path).convert("RGB").resize((320, 180))
    x = np.asarray(im).astype(np.float32) / 255.0
    r, g, b = x[..., 0], x[..., 1], x[..., 2]
    mx, mn = x.max(-1), x.min(-1)
    v = mx; s = np.where(mx > 0, (mx - mn) / np.maximum(mx, 1e-6), 0)
    # hue
    rc = (mx - r) / np.maximum(mx - mn, 1e-6); gc = (mx - g) / np.maximum(mx - mn, 1e-6); bc = (mx - b) / np.maximum(mx - mn, 1e-6)
    h = np.where(r == mx, bc - gc, np.where(g == mx, 2 + rc - bc, 4 + gc - rc)); h = (h / 6.0) % 1.0 * 360
    sat = (s > 0.45) & (v > 0.45)
    cls = dict(
        yellow=sat & (h >= 40) & (h < 70), red=sat & ((h < 15) | (h >= 340)), orange=sat & (h >= 15) & (h < 40),
        green=sat & (h >= 70) & (h < 170), blue=sat & (h >= 190) & (h < 260),
        white=(v > 0.88) & (s < 0.15), black=(v < 0.15))
    gray = 0.299 * r + 0.587 * g + 0.114 * b
    # 글자 띠 추정: 가로 경계(밝기 차)가 많고 흰/노랑 픽셀이 많은 가로 띠 — 위 1/3, 가운데, 아래 1/3
    gx = np.abs(np.diff(gray, axis=1)); edge = gx > 0.25
    bands = {"top": slice(0, 60), "mid": slice(60, 120), "bottom": slice(120, 180)}
    ed = {k: float(edge[s_].mean()) for k, s_ in bands.items()}
    return dict(brightness=float(v.mean()), saturation=float(s.mean()), contrast=float(gray.std()),
                **{f"c_{k}": float(m.mean()) for k, m in cls.items()}, **{f"edge_{k}": e for k, e in ed.items()})
for r in rows:
    try:
        r.update(metrics(r["path"]))
    except Exception as e:
        log("METRIC", level="warn", id=r["id"], error=e)
for r in rows:
    r["path"] = str(Path(r["path"]).relative_to(ROOT))
json.dump(rows, open(OUT / "thumbs.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
log("SAVE", out=OUT / "thumbs.json", rows=len(rows))


# 2-1 표: 성공 vs 기준 밖 중앙값, P(성공>기준 밖)(= Mann-Whitney AUC), 성공 안에서 배수와 스피어만 순위상관
def auc(a, b):
    a, b = np.asarray(a), np.asarray(b)
    return float(((a[:, None] > b[None, :]).sum() + 0.5 * (a[:, None] == b[None, :]).sum()) / (len(a) * len(b)))
def spearman(x, y):
    rx, ry = np.argsort(np.argsort(x)), np.argsort(np.argsort(y))
    return float(np.corrcoef(rx, ry)[0, 1])
GROUP = tuple(w for w in args.group.split(",") if w)
for label, subset in (("전체", rows), ("·".join(GROUP), [r for r in rows if any(k in r["theme"] for k in GROUP)])):
    s_ = [r for r in subset if r["success"] and "brightness" in r]; o_ = [r for r in subset if not r["success"] and "brightness" in r]
    log("STATS", group=label, success=len(s_), other=len(o_))
    for k in ("brightness", "saturation", "c_white", "c_yellow", "c_red", "c_black"):
        a_, b_ = [r[k] for r in s_], [r[k] for r in o_]
        log("STATS", group=label, metric=k, succ_median=round(float(np.median(a_)), 3), other_median=round(float(np.median(b_)), 3),
            p_succ_gt_other=round(auc(a_, b_), 2), rho_ratio_in_success=round(spearman(a_, [r["ratio"] for r in s_]), 2))
