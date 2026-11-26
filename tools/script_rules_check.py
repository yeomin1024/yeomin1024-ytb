#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-11-26 — 최초: 대본 공통 규칙(guides/script_rules.md v1.0) 점검 — 도입 30초 · 결론 먼저 ✗ · 썸네일 연결 · 챕터 끝 질문 · 직관적이지 않은 표현
#   사용자 지시 2026-11-26 "대본 도입부 30초 넘기지 말고 썸네일과 연결되고 … 결론부터 말하지 말고 하나씩 챕터를 정해서 알려주고 챕터 넘어갈 때마다 다음 챕터에 대한
#   호기심을 유발하면서 … '보는 때가 다르다' 처럼 직관적이지 못한 표현은 사용하지마 이걸 모든 영상 대본에 적용되는 공통 규칙으로 해서 파일로 기록하고".
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.0 | 2026-11-26 | 최초 | parse · intro_checks · chapter_checks · phrase_checks · main |
"""대본 공통 규칙 점검 (읽기만 — 파일을 고치지 않음).

대본 꼴: '-챕터 이름' 줄로 챕터를 나누고, 그 밑에 한 줄에 한 문장 ('#' 줄은 주석). 첫 챕터 = 도입, 마지막 챕터 = 마무리.
  python3 tools/script_rules_check.py <대본.txt> [--package <package.json>] [--srt <대본.srt>] [--rate 6.3] [--pause 0.35]
결과: [CHECK] 줄 + 끝에 ❌·⚠ 수. ❌ 가 있으면 끝 코드 1. ※ 연구·교육용 도구.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

VERSION = "v1.0"
INTRO_MAX_S = 30.0
# 직관적이지 않은 표현 (guides/script_rules.md 3번 표 — 새로 찾으면 여기와 그 표에 같이 더함)
VAGUE = [
    (r"보는\s*때가\s*다르", "'보는 때가 다르다' — 누가 무엇을 보는지 장면으로"),
    (r"(건네는|주는)\s*순간을\s*[,，]?\s*받는\s*(사람|쪽)은\s*그\s*뒤를", "'건네는 순간을, 받는 쪽은 그 뒤를' — 장면으로"),
    (r"손에는\s*.{0,20}마음이\s*들어\s*있", "'…손에는 …마음이 들어 있다' — 비유 대신 '이것이 첫 번째 이유입니다'"),
    (r"(아까움|미안함|부담)[이은]\s*.{0,12}넘어(가|오)", "'아까움이 넘어간다' — 무엇을 누가 하게 되는지 장면으로"),
]
CONCLUSION_FIRST = r"결론부터|결론을\s*먼저|결론은\s*이렇|답부터\s*말씀"
BENEFIT = r"(끝까지\s*보시면|알면|아시면|얻어\s*가|할\s*수\s*있습니다|도움이\s*됩니다|챙기실\s*수|피하실\s*수)"


def log(stage: str, **kv) -> None:
    now = dt.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    print(f"[{stage}] [{now}] " + " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) and (' ' in v or not v) else v}"
                                          for k, v in kv.items()), flush=True)


def parse(path: Path) -> list[dict]:
    parts, cur = [], None
    n = 0
    for ln in path.read_text("utf-8").splitlines():
        if ln.startswith("#") or not ln.strip():
            continue
        if ln.startswith("-"):
            cur = {"name": ln[1:].strip(), "sents": []}
            parts.append(cur)
            continue
        if cur is None:
            cur = {"name": "(이름 없음)", "sents": []}
            parts.append(cur)
        n += 1
        cur["sents"].append((n, ln.strip()))
    return parts


def syllables(s: str) -> float:
    """말소리 길이 어림: 한글 1 · 숫자 한 자리 1.3(읽으면 길어짐) · 영문 0.5."""
    return sum(1 for ch in s if "가" <= ch <= "힣") + 1.3 * sum(ch.isdigit() for ch in s) + 0.5 * sum(ch.isascii() and ch.isalpha() for ch in s)


def srt_end_of(srt: Path, k: int) -> float | None:
    blocks = [b for b in re.split(r"\n\s*\n", srt.read_text("utf-8-sig").strip()) if b.strip()]
    for b in blocks:
        ln = b.splitlines()
        if ln and ln[0].strip() == str(k) and len(ln) > 1 and "-->" in ln[1]:
            h, m, rest = ln[1].split("-->")[1].strip().split(":")
            s, ms = rest.split(",")
            return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000
    return None


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="대본 공통 규칙 점검 (guides/script_rules.md)")
    ap.add_argument("script")
    ap.add_argument("--package", help="편 package.json (썸네일 문구와 도입 연결 확인)")
    ap.add_argument("--srt", help="실제 음성에 맞춘 SRT (도입 실제 초)")
    ap.add_argument("--rate", type=float, default=6.3, help="음절/초 (H17 샘플 6.3)")
    ap.add_argument("--pause", type=float, default=0.35, help="문장 사이 쉼(초)")
    a = ap.parse_args(argv)
    path = Path(a.script)
    parts = parse(path)
    bad, warn = 0, 0

    def report(level: str, what: str, **kv):
        nonlocal bad, warn
        if level == "❌":
            bad += 1
        elif level == "⚠":
            warn += 1
        log("CHECK", level=level, what=what, **kv)

    log("START", tool=f"script_rules_check.py {VERSION}", script=str(path), parts=len(parts),
        sentences=sum(len(p["sents"]) for p in parts), rule="guides/script_rules.md v1.0")
    if len(parts) < 3:
        report("❌", "챕터", why="'-챕터 이름' 줄이 3개 미만 — 도입 · 챕터 · 마무리로 나눔")
        return 1
    intro = parts[0]
    text = " ".join(s for _, s in intro["sents"])
    syl = syllables(text)
    est = syl / a.rate + a.pause * max(0, len(intro["sents"]) - 1)
    real = srt_end_of(Path(a.srt), intro["sents"][-1][0]) if a.srt and Path(a.srt).is_file() else None
    secs = real if real is not None else est
    report("❌" if secs > INTRO_MAX_S else "✅", "도입 길이", part=intro["name"], sentences=len(intro["sents"]), syllables=round(syl),
           seconds=round(secs, 1), source="SRT 실제" if real is not None else f"어림({a.rate}음절/초+쉼)", limit=INTRO_MAX_S)
    if re.search(CONCLUSION_FIRST, text):
        report("❌", "결론 먼저", why="도입에 '결론부터' 류 — 답은 그 챕터에서 처음")
    report("✅" if "?" in text else "❌", "도입 호기심 질문", found="?" in text)
    report("✅" if re.search(BENEFIT, text) else "⚠", "도입 시청자 이득 문장", found=bool(re.search(BENEFIT, text)))
    if a.package and Path(a.package).is_file():
        pkg = json.loads(Path(a.package).read_text("utf-8"))
        subs = pkg.get("thumb_subs") or pkg.get("thumb_sub") or []
        subs = [subs] if isinstance(subs, str) else list(subs)
        thumb = " ".join(list(pkg.get("thumb_main") or []) + subs)
        words = {w for w in re.findall(r"[가-힣A-Za-z0-9]{2,}", re.sub(r"[~…'\"]", " ", thumb))}
        first = intro["sents"][0][1]
        hit_first = sorted(w for w in words if w in first)
        hit_intro = sorted(w for w in words if w in text)
        report("✅" if hit_first else ("⚠" if hit_intro else "❌"), "썸네일 연결", first_sentence_words=",".join(hit_first) or "-",
               intro_words=",".join(hit_intro) or "-", thumb=thumb[:60])
    # 챕터 끝 = 다음 챕터로 가는 질문 (마지막 두 챕터 = 마지막 본문·마무리는 뺌 — 마지막 본문은 마무리로 이어지므로 질문 아니어도 됨)
    for i, p in enumerate(parts[1:-2], start=1):
        last = p["sents"][-1][1] if p["sents"] else ""
        ok = last.rstrip().endswith("?")
        report("✅" if ok else "⚠", "챕터 끝 질문", part=p["name"], last=last[:50])
    mid = parts[-2]
    if mid["sents"] and not mid["sents"][-1][1].rstrip().endswith("?"):
        log("CHECK", level="ℹ", what="챕터 끝 질문", part=mid["name"], note="마지막 본문 챕터 — 마무리로 이어지므로 질문 아니어도 됨")
    for k, s in ((k, s) for p in parts for k, s in p["sents"]):
        for pat, why in VAGUE:
            if re.search(pat, s):
                report("❌", "직관적이지 않은 표현", sentence=k, text=s[:60], fix=why)
        if len(s) > 50:
            report("⚠", "긴 문장", sentence=k, chars=len(s), note="50자 넘음 — 자막 2줄 안인지 srt_tool 로")
    last = parts[-1]["sents"][-1][1] if parts[-1]["sents"] else ""
    report("✅" if last == "시청해주셔서 감사합니다." else "❌", "마지막 문장", last=last)
    log("DONE", bad=bad, warn=warn, next="❌ 고친 뒤 다시 · 그다음 guides/persona_loop.md" if bad else "규칙 점검 통과 → 페르소나 반복 검증")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
