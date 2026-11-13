#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.2 — 2026-11-13 — 말풍선 꼬리가 말하는 사람(말풍선 왼쪽 아래) 쪽으로 기울게 (tail right · 18%)
# 이전 v1.1 — 2026-11-13 — 말풍선을 머리 옆 빈 곳 끝까지 넓히고 줄을 나눠 글자를 키움 (40~46px → 크게 · 낱말 그대로)
# 이전 v1.0 — 2026-11-13 — 심리 네 편 롱폼 썸네일 3안 설정 (만스피처럼 그림 = ChatGPT TH-CHAR · 문구 = 코드 thumb.mjs)
#   사용자 지시 2026-11-13 "썸네일 만스피처럼 문구 코드로 얹어서 만들어".
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.2 | 2026-11-13 | 꼬리 방향 = 말하는 사람 쪽 | bubble |
# | v1.1 | 2026-11-13 | 말풍선 자리 넓힘 · 줄 나눔 (글자 그대로) · fill 0.9/0.74 | EP · bubble |
# | v1.0 | 2026-11-13 | 최초 — 편마다 thumbnail_1~3.json (본안 · 실험 1 보조 문구 없음 · 실험 2 강조 색·노란 말풍선) | build · main |
"""psychology/source/<영상ID>/thumbnails/thumbnail_{1,2,3}.json 을 쓰고 `node video/render/thumb.mjs` 로 jpg 를 만든다.

- 문구 = 그 편 package.json 의 thumb_main(2줄)·thumb_sub (페르소나 관문 title 단계 통과 — 글자는 바꾸지 않음).
- 1 = 본안: 아래 2줄 + 보조 문구 흰 말풍선(머리 옆 빈 곳 — 사람을 가리지 않음, thumbnail_guide 13-5).
- 2 = 실험 1: 아래 2줄만 (보조 문구가 클릭에 도움이 되는지 — 스튜디오 '테스트 및 비교').
- 3 = 실험 2: 같은 낱말 · 강조 색을 바꿈 + 노란 말풍선.
- 규칙: 2줄째는 오른쪽 아래 18% 칸을 비움(영상 길이 표시) · 나쁜 상황 빨강 · 중요 노랑 · 말풍선 꼬리는 평평한 아래쪽(13-6).
실행: python3 psychology/source/thumbs_build.py [--only <영상ID>] [--no-render]
※ 연구·교육용 영상 소스.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
K = 1280 / 1536            # 그림(1536×864) → 썸네일(1280×720)
L1 = [36, 452, 1208, 120]   # 1줄 상자
L2 = [36, 576, 1000, 124]   # 2줄 상자 — 오른쪽 끝 1036 < 1280 × 0.82 (영상 길이 표시 칸 비움)

# 편마다: 1줄·2줄 색 조각(본안 · 실험 2) · 말풍선(그림 좌표 [x, y, w, h] — 머리 옆 빈 곳, 눈으로 잼) · 글(두 줄 "\n")
EP = {
    "geureut-moa-2026-11": {
        "main": [[["식당 ", "W"], ["그릇", "Y"], [" 모아 두는 사람", "W"]], [["의외의 속마음", "Y"]]],
        "alt": [[["식당 그릇 모아 두는 사람", "W"]], [["의외의 ", "W"], ["속마음", "Y"]]],
        "bubble": [706, 17, 307, 294], "btext": "안 치우면\n거슬려서요",
        "_": "G 머리(그림 x 13~25% · y 13~41%)와 직원 머리(x 67~82%) 사이 벽",
    },
    "eomma-gibun-2026-11": {
        "main": [[["엄마 눈치", "Y"], [" 보며 자란 아이", "W"]], [["커서도 남을 수 있는 ", "W"], ["5가지", "Y"]]],
        "alt": [[["엄마 눈치 보며 자란 아이", "W"]], [["커서도 ", "W"], ["남을 수 있는", "R"], [" 5가지", "Y"]]],
        "bubble": [1106, 26, 399, 363], "btext": "내가\n참으면\n되지...",
        "_": "어른 A 머리(x 50~71% · y 2~37%) 오른쪽 사무실 창",
    },
    "eomma-hasoyeon-2026-11": {
        "main": [[["엄마 하소연", "Y"], [" 다 받아 주면", "W"]], [["딸 혼자 ", "W"], ["지칩니다", "R"]]],
        "alt": [[["엄마 하소연 다 받아 주면", "W"]], [["딸 혼자 지칩니다", "R"]]],
        "bubble": [937, 26, 553, 363], "btext": "나 아니면\n들어 줄 사람이\n없잖아...",
        "_": "딸 D 머리(x 38~58% · y 9~41%) 오른쪽 가게 차양·가로등",
    },
    "sangcheo-gonggyeok-2026-11": {
        "main": [[["상처받은", "Y"], [" 사람이", "W"]], [["오히려 ", "W"], ["공격적", "R"], ["이 되는 이유", "W"]]],
        "alt": [[["상처받은 사람이", "W"]], [["오히려 공격적이 되는 이유", "Y"]]],
        "bubble": [1106, 26, 399, 300], "btext": "왜,\n안 어울려?",
        "_": "R 머리(x 50~71% · y 4~39%) 오른쪽 선반·냉장고",
    },
}


def log(stage: str, **kv):
    print(f"[{stage}] [{time.strftime('%Y-%m-%dT%H:%M:%S')}] " + " ".join(f"{k}={v}" for k, v in kv.items()), flush=True)


def lines(box, frags):
    return {"kind": "lines", "box": box, "align": "left", "valign": "bottom", "lineHeight": 1.05, "stroke": 16, "lines": [frags]}


def bubble(rect, text, bg):
    x, y, w, h = (round(v * K) for v in rect)
    return {"kind": "bubble", "x": x, "y": y, "w": w, "h": h, "bg": bg, "color": "K", "text": text, "tail": "right", "tailPos": 0.18, "tailLen": 54,
            "fill": [0.9, 0.74], "_": "보조 문구 — 머리 옆 빈 곳 (사람을 가리지 않음 · 꼬리는 평평한 아래쪽 18% · tail right = 왼쪽(말하는 사람 쪽)으로 기욺)"}


def build(ep: str, spec: dict, pkg: dict) -> list[Path]:
    # 문구가 package.json 과 같은지 (글자는 바꾸지 않음 — 페르소나 관문 통과 문구)
    joined = ["".join(t for t, _ in ln) for ln in spec["main"]]
    if joined != pkg["thumb_main"]:
        raise SystemExit(f"[THUMB] {ep} 주요 문구가 package.json 과 다름: {joined} ≠ {pkg['thumb_main']} — 문구를 바꾸면 persona_loop title 단계부터")
    if ["".join(t for t, _ in ln) for ln in spec["alt"]] != pkg["thumb_main"]:
        raise SystemExit(f"[THUMB] {ep} 실험 2 문구가 package.json 과 다름")
    if spec["btext"].replace("\n", " ") != pkg["thumb_sub"].strip('"').replace("  ", " "):   # 줄바꿈만 다름 (글자 그대로)
        raise SystemExit(f"[THUMB] {ep} 보조 문구가 package.json 과 다름: {spec['btext']!r} ≠ {pkg['thumb_sub']!r}")
    out_dir = ROOT / "psychology" / "source" / ep / "thumbnails"
    out_dir.mkdir(exist_ok=True)
    base = {"size": [1280, 720], "shade": [0.56, 0.9], "images": [{"src": "../images/TH-CHAR.jpg", "box": [0, 0, 1280, 720]}]}
    variants = [
        ("본안", [lines(L1, spec["main"][0]), lines(L2, spec["main"][1]), bubble(spec["bubble"], spec["btext"], "W")]),
        ("실험 1 — 보조 문구 없음", [lines(L1, spec["main"][0]), lines(L2, spec["main"][1])]),
        ("실험 2 — 강조 색 바꿈 · 노란 말풍선", [lines(L1, spec["alt"][0]), lines(L2, spec["alt"][1]), bubble(spec["bubble"], spec["btext"], "Y")]),
    ]
    paths = []
    for i, (name, blocks) in enumerate(variants, 1):
        d = dict(base)
        d["_설명"] = (f"{name} (2026-11-13 — 사용자 지시 \"썸네일 만스피처럼 문구 코드로 얹어서 만들어\") — 짝 제목 「{pkg['title']}」 · "
                     f"문구 = package.json (페르소나 관문 title 통과 — 글자 그대로) · 그림 = images/TH-CHAR.jpg (ChatGPT, 글자 없음) · 말풍선 자리: {spec['_']}")
        d["out"] = f"thumbnail_{i}.jpg"
        d["blocks"] = blocks
        p = out_dir / f"thumbnail_{i}.json"
        p.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
        paths.append(p)
    log("JSON", ep=ep, files=len(paths))
    return paths


def main() -> int:
    ap = argparse.ArgumentParser(description="심리 썸네일 3안 설정 + 렌더")
    ap.add_argument("--only")
    ap.add_argument("--no-render", action="store_true")
    a = ap.parse_args()
    allp = []
    for ep, spec in EP.items():
        if a.only and ep != a.only:
            continue
        pkg = json.loads((ROOT / "psychology" / "source" / ep / "package.json").read_text(encoding="utf-8"))
        allp += build(ep, spec, pkg)
    if a.no_render:
        return 0
    try:
        r = subprocess.run(["node", str(ROOT / "video/render/thumb.mjs"), *map(str, allp)], cwd=ROOT, capture_output=True, text=True, timeout=600)
    except (OSError, subprocess.TimeoutExpired) as ex:
        log("RENDER", level="error", msg=str(ex), next="cd video/render && npm ci · node video/scripts/get-fonts.mjs")
        return 1
    print(r.stdout[-3000:], r.stderr[-2000:], sep="\n")
    return r.returncode


if __name__ == "__main__":
    sys.exit(main())
