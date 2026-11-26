#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.10 — 2026-11-26 — jakku 둘째 줄 '심리학적 이유 3가지' → '거절해도 또 주는 이유' (영상 제작 공통 규칙 3번 — 제목과 이어지는 시청자 장면 · 답 숨김 · package.json thumb_main 과 맞춤 · '숨겨진' 은 페르소나 title 4·5회차가 탓하는 말로 읽음)
# 이전 VERSION: v1.9 — 2026-11-25 — jakku-juneun-2026-11-25 (같은 낱말 3안 — 본안 말풍선 둘 · 실험 1 말풍선 없음 · 실험 2 강조 색 바꿈 + 노란 말풍선) — 사용자 지시 "이미지, 음성 확인해서 영상 만들어"
# 이전 v1.8 — 2026-11-24 — adhd-ab-2026-11 그림을 화면 끝까지 (아래 어두운 띠 뺌 — 두 칸을 따로 잘라 좌우로) · 문구는 그림 위 · 말풍선은 썸네일 좌표 — 사용자 지시 "썸네일 문구부분은 왜 이미지 영역이 아니야 이미지 꽉채워서 문구넣어야지"
# (v1.7) — 2026-11-24 — adhd-ab-2026-11 사용자 제목·문구 3안 + A 말풍선 「진작 할걸~」 한 줄(작게) — 사용자 지시 "제목1 … 제목3 … 이렇게 가고 썸네일 각각 만들어 그리고 글씨 크기 좀 줄여서 한줄에 진작 할걸~ 로 고쳐"
# 이전 v1.6 — 2026-11-24 — adhd-ab-2026-11 A 말풍선 「진작 할걸」 (사용자 지시 "진작 할걸 이렇게 바꾸고")
# 이전 v1.5 — 2026-11-24 — adhd-ab-2026-11 실험 문구·A 말풍선을 성공 사례 썸네일 분석(thumb_text_patterns.md)으로 — 사용자 지시 "실험형 썸네일 문구 성공 사례 분석해서 한거야? 분석해서 만들고 이유를 아니까를 진작에 할걸(예시) 이런식으로 고쳐봐"
# 이전 v1.4 — 2026-11-24 — 편마다 3안을 따로 (variants: 안마다 문구 2줄·말풍선 여러 개) — 사용자 지시 "둘다 말풍선 넣고 두번재 줄 괄호 제거해 그리고 나머지 2개는 실험형으로 너가 문구를 만드는 거야"
# 이전 v1.3 — 2026-11-24 — adhd-ab-2026-11 (일상툰 · 그림 아래 어두운 띠 y 74% 부터): 편마다 글 상자(l1·l2)·꼬리 방향·설명 줄을 따로 — 사용자 지시 "1번으로 하고 썸네일 만들어봐"
# 이전 v1.2 — 2026-11-13 — 말풍선 꼬리가 말하는 사람(말풍선 왼쪽 아래) 쪽으로 기울게 (tail right · 18%)
# 이전 v1.1 — 2026-11-13 — 말풍선을 머리 옆 빈 곳 끝까지 넓히고 줄을 나눠 글자를 키움 (40~46px → 크게 · 낱말 그대로)
# 이전 v1.0 — 2026-11-13 — 심리 네 편 롱폼 썸네일 3안 설정 (만스피처럼 그림 = ChatGPT TH-CHAR · 문구 = 코드 thumb.mjs)
#   사용자 지시 2026-11-13 "썸네일 만스피처럼 문구 코드로 얹어서 만들어".
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.10 | 2026-11-26 | jakku 둘째 줄 문구 (제목 축약) | EP |
# | v1.9 | 2026-11-25 | variants 셋째 칸 opts {bubbles: W·Y·none} · same_words(실험안도 본안 낱말 그대로 — package.json thumb_tests 없을 때) · 편마다 why(설명 줄의 사용자 지시) — jakku-juneun-2026-11-25 | EP · build_variants |
# | v1.8 | 2026-11-24 | 편마다 images(crop·box)·bg 덮어쓰기 · bubbles_px(썸네일 좌표 그대로) — adhd-ab-2026-11 TH-CHAR 아래 26% 어두운 띠를 빼고 왼쪽 칸(A)·오른쪽 칸(B)을 따로 잘라 1280×720 을 채움 | EP · bubble · build_variants |
# | v1.7 | 2026-11-24 | adhd-ab-2026-11 3안 = 사용자 제목·문구 1~3 · A 말풍선 한 줄 (낮은 상자 → 글씨 작게) | EP |
# | v1.6 | 2026-11-24 | adhd-ab-2026-11 A 말풍선 「진작 할걸」 (사용자 문구) | EP |
# | v1.5 | 2026-11-24 | adhd-ab-2026-11 실험 1·2 = 성공 사례 갈래(특징+숫자 · 이유형) · A 말풍선 = 인물 속마음 「진작 검사받을걸!」 | EP |
# | v1.4 | 2026-11-24 | variants (안마다 문구·말풍선 여러 개) — package.json thumb_tests 와 글자 대조 | build |
# | v1.3 | 2026-11-24 | 편마다 l1·l2 글 상자 · tail·tailPos · note (adhd-ab-2026-11) | EP · bubble · build |
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
    # v1.8 — 그림 아래 26%(y 640/864 부터)가 어두운 빈 띠 → 문구가 그림 밖에 놓였음 (사용자 지적 2026-11-24).
    #   그림 칸(y 0~640)만 쓴다: 640 높이로 16:9 를 채우면 폭 1138 < A·B 가 걸친 폭(x 130~1340) → 칸마다 따로 잘라 좌우에 붙임.
    #   왼쪽 = A 칸 x 112~679 (A 팔꿈치 x≈130 · 모니터 x 490~672 까지) · 오른쪽 = B 칸 x 969~1536 (스탠드·B·낙서 구름·창문) · 가운데 4px 틈 = 원래 칸 나눔 선.
    #   배율 720/640 = 1.125 — 썸네일 x = (그림 x − 112)×1.125 (왼쪽) · 642 + (그림 x − 969)×1.125 (오른쪽), y = 그림 y×1.125.
    "adhd-ab-2026-11": {
        "bg": "#24212b",
        "images": [{"src": "../images/TH-CHAR.jpg", "crop": [112, 0, 567, 640], "box": [0, 0, 638, 720]},
                   {"src": "../images/TH-CHAR.jpg", "crop": [969, 0, 567, 640], "box": [642, 0, 638, 720]}],
        "l1": [36, 524, 1208, 94], "l2": [36, 616, 1000, 100],
        # 말풍선 = 썸네일 좌표 (bubbles_px) — A: 머리(x 76~313 · y 124~371)·반짝 표시(x 256~324) 오른쪽, 모니터(y 236~) 위 사무실 벽
        #   B: 머리(x 761~964 · y 180~405)·낙서 구름(x 806~919) 오른쪽 창문 (사람·스탠드·구름을 가리지 않음)
        "bubbles_px": True,
        "bubbles": [[[344, 40, 266, 92], "진작 할걸~", "right", 0.18], [[984, 28, 276, 168], "내가 게을러서\n그래…", "right", 0.16]],
        "variants": [
            ("1안 — 사용자 제목1·문구1", [[["나도 ", "W"], ["ADHD", "Y"], ["인가? 고민했던 두 사람", "W"]], [["30년 삶의 질이 ", "W"], ["정반대", "Y"], ["가 된 이유", "W"]]]),
            ("2안 — 사용자 제목2·문구2", [[["나도 ", "W"], ["ADHD", "Y"], ["인가? 했던 고민", "W"]], [["30년 삶의 질을 ", "W"], ["바꾼 이유", "Y"]]]),
            ("3안 — 사용자 제목3·문구3", [[["나도 ", "W"], ["ADHD", "Y"], ["인가? 했던 고민", "W"]], [["그냥 넘겼다가 ", "W"], ["30년을 자책한", "R"], [" 이유", "W"]]]),
        ],
        "note": "1~3안 = 사용자 제목·문구 (2026-11-24) · 말풍선 = 인물 속마음 A 「진작 할걸~」(사용자 문구, 한 줄)·B 「내가 게을러서 그래…」(대본 46번) — persona_loop title 단계는 1안 · v1.8 그림을 화면 끝까지 (문구는 그림 위)",
        "_": "A 머리 오른쪽 사무실 벽(모니터 위) · B 머리 오른쪽 창문 — 썸네일 좌표, 사람·스탠드·낙서 구름을 가리지 않음",
    },
    "jakku-juneun-2026-11-25": {
        # TH-CHAR = 화면 끝까지 그린 복도 (빈 띠 없음) — 자르지 않음. 문구는 그림 위 아래쪽 (L1·L2 기본 상자)
        # 말풍선 = 썸네일 좌표: G(주는 사람) 머리 x 308~488 · y 117~288, 반짝 표시 x 496~546 → 그 오른쪽 창문(하늘)
        #   R(받는 사람) 머리 x 850~1012 · y 79~250 → 그 오른쪽 열린 문틀 · 두 말풍선 모두 꼬리는 왼쪽(말하는 사람) 쪽으로
        "bubbles_px": True,
        "bubbles": [[[566, 30, 262, 146], "너 주려고\n챙겼지~", "right", 0.18], [[1030, 26, 234, 146], "마음은\n고마운데…", "right", 0.16]],
        "same_words": True,
        "variants": [
            ("본안 — 말풍선 둘", [[["필요 없다는데 ", "W"], ["자꾸 주는", "Y"], [" 사람", "W"]], [["거절해도 ", "W"], ["또 주는 이유", "Y"]]], {"bubbles": "W"}),
            ("실험 1 — 보조 문구 없음", [[["필요 없다는데 ", "W"], ["자꾸 주는", "Y"], [" 사람", "W"]], [["거절해도 ", "W"], ["또 주는 이유", "Y"]]], {"bubbles": "none"}),
            ("실험 2 — 강조 색 바꿈 · 노란 말풍선", [[["필요 없다는데", "R"], [" 자꾸 주는 사람", "W"]], [["거절해도 또 주는 이유", "Y"]]], {"bubbles": "Y"}),
        ],
        "why": "2026-11-25 — 사용자 지시 \"이미지, 음성 확인해서 영상 만들어\"",
        "note": "문구 = package.json thumb_main·thumb_subs (v1.10 제목 '…사람의 심리 3가지' · 문구 '거절해도 또 주는 이유' — persona_loop title 4·5회차 지적 반영, 6회차로 다시 봄) · 실험안은 같은 낱말(thumb_tests_note) · 빨강 = 나쁜 상황('필요 없다는데')",
        "_": "G 머리·반짝 표시 오른쪽 창문(하늘) · R 머리 오른쪽 열린 문틀 — 썸네일 좌표, 두 사람 얼굴·손·봉지를 가리지 않음",
    },
}


def log(stage: str, **kv):
    print(f"[{stage}] [{time.strftime('%Y-%m-%dT%H:%M:%S')}] " + " ".join(f"{k}={v}" for k, v in kv.items()), flush=True)


def lines(box, frags):
    return {"kind": "lines", "box": box, "align": "left", "valign": "bottom", "lineHeight": 1.05, "stroke": 16, "lines": [frags]}


def bubble(rect, text, bg, tail="right", tail_pos=0.18, px=False):
    x, y, w, h = (round(v) if px else round(v * K) for v in rect)          # v1.8 px=True → 썸네일 좌표 그대로
    return {"kind": "bubble", "x": x, "y": y, "w": w, "h": h, "bg": bg, "color": "K", "text": text, "tail": tail, "tailPos": tail_pos, "tailLen": 54,
            "fill": [0.9, 0.74], "_": "보조 문구 — 머리 옆 빈 곳 (사람을 가리지 않음 · 꼬리는 평평한 아래쪽 18% · tail right = 왼쪽(말하는 사람 쪽)으로 기욺)"}


def build_variants(ep: str, spec: dict, pkg: dict) -> list[Path]:
    """v1.4 편마다 3안 (안마다 문구 2줄 · 말풍선 여러 개) — package.json thumb_main(본안)·thumb_tests(실험)·thumb_subs 와 글자 대조."""
    want = [pkg["thumb_main"]] + [t["main"] for t in pkg.get("thumb_tests", [])]
    if spec.get("same_words") and not pkg.get("thumb_tests"):           # v1.9 실험안도 본안 낱말 그대로 (색·말풍선만 다름)
        want = [pkg["thumb_main"]] * len(spec["variants"])
    got = [["".join(t for t, _ in ln) for ln in v[1]] for v in spec["variants"]]
    if got != want:
        raise SystemExit(f"[THUMB] {ep} 문구가 package.json 과 다름: {got} ≠ {want} — 문구를 바꾸면 persona_loop title 단계부터")
    if [b[1].replace("\n", " ") for b in spec["bubbles"]] != pkg.get("thumb_subs", []):
        raise SystemExit(f"[THUMB] {ep} 말풍선이 package.json thumb_subs 와 다름")
    out_dir = ROOT / "psychology" / "source" / ep / "thumbnails"
    out_dir.mkdir(exist_ok=True)
    base = {"size": [1280, 720], "shade": [0.56, 0.9], "images": [{"src": "../images/TH-CHAR.jpg", "box": [0, 0, 1280, 720]}]}
    if "images" in spec:                                    # v1.8 편마다 그림 자르기 (어두운 빈 띠 빼고 화면 끝까지)
        base.update(images=spec["images"], bg=spec.get("bg", "#000"))
    l1, l2 = spec.get("l1", L1), spec.get("l2", L2)
    px = spec.get("bubbles_px", False)
    paths = []
    for i, v in enumerate(spec["variants"], 1):
        name, main = v[0], v[1]
        vo = v[2] if len(v) > 2 else {"bubbles": "W"}                      # v1.9 안마다 말풍선 색 · none = 말풍선 없음
        d = dict(base)
        why = spec.get("why", "2026-11-24 — 사용자 지시 \"둘다 말풍선 넣고 두번재 줄 괄호 제거해 그리고 나머지 2개는 실험형으로 너가 문구를 만드는 거야\"")
        d["_설명"] = (f"{name} ({why}) — "
                     f"짝 제목 「{pkg['title']}」 · {spec.get('note', '')} · 그림 = images/TH-CHAR.jpg"
                     f"{' (자르기 ' + ' + '.join(str(im['crop']) for im in spec['images']) + ')' if 'images' in spec else ''} · 말풍선 자리: {spec['_']}")
        d["out"] = f"thumbnail_{i}.jpg"
        bubs = [] if vo["bubbles"] == "none" else [bubble(r, t, vo["bubbles"], tl, tp, px) for r, t, tl, tp in spec["bubbles"]]
        d["blocks"] = [lines(l1, main[0]), lines(l2, main[1])] + bubs
        p = out_dir / f"thumbnail_{i}.json"
        p.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
        paths.append(p)
    log("JSON", ep=ep, files=len(paths), variants=len(spec["variants"]))
    return paths


def build(ep: str, spec: dict, pkg: dict) -> list[Path]:
    if "variants" in spec:                                  # v1.4
        return build_variants(ep, spec, pkg)
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
    l1, l2 = spec.get("l1", L1), spec.get("l2", L2)                       # v1.3 편마다 글 상자
    tl = (spec.get("tail", "right"), spec.get("tailPos", 0.18))
    variants = [
        ("본안", [lines(l1, spec["main"][0]), lines(l2, spec["main"][1]), bubble(spec["bubble"], spec["btext"], "W", *tl)]),
        ("실험 1 — 보조 문구 없음", [lines(l1, spec["main"][0]), lines(l2, spec["main"][1])]),
        ("실험 2 — 강조 색 바꿈 · 노란 말풍선", [lines(l1, spec["alt"][0]), lines(l2, spec["alt"][1]), bubble(spec["bubble"], spec["btext"], "Y", *tl)]),
    ]
    paths = []
    for i, (name, blocks) in enumerate(variants, 1):
        d = dict(base)
        note = spec.get("note", "문구 = package.json (페르소나 관문 title 통과 — 글자 그대로)")
        d["_설명"] = (f"{name} (2026-11-13 — 사용자 지시 \"썸네일 만스피처럼 문구 코드로 얹어서 만들어\") — 짝 제목 「{pkg['title']}」 · "
                     f"{note} · 그림 = images/TH-CHAR.jpg (ChatGPT, 글자 없음) · 말풍선 자리: {spec['_']}")
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
