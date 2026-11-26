#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.4 — 2026-11-26 — 도입 예고 말끝 '~봅니다' ⚠ ('~보겠습니다'로 — guides/script_rules.md 1번, 사용자 지시 "따라가 봅니다, 짚어봅니다 이렇게 하기말고 ~보겠습니다")
# 이전 v1.3 — 2026-11-26 — 진행 멘트 점검: '오늘의 ~' ❌ (guides/script_rules.md v1.3 8번 — 사용자 지시 "오늘의 ~ 이런 멘트 넣지마 이건 공통 규칙에 넣고")
# 이전 v1.2 — 2026-11-26 — 맥락을 끊는 멘트 점검(guides/script_rules.md 7번 — 호칭 선언·'끝까지 보시면'·'얻어 가실'·'이 영상에서는' ❌ · 본문의 짧은 '…보겠습니다.' 넘김 ⚠) · 시청자 이득 = 자연스러운 꼴로만 셈 (사용자 지시 "…쓸모없이 맥락만 망치는 멘트는 쓰지 말라고 공통 규칙에 기록하고 대본 수정해")
# 이전 v1.1 — 2026-11-26 — 알고리즘 구조(제목 낱말 → 도입 첫 두 문장 · 챕터 이름 낱말 → 챕터 첫 두 문장) · 익숙한 말(가운뎃점·괄호·슬래시·영어 글자·따옴표 겹침) 점검 — guides/script_rules.md v1.1 5·6번
# 이전 v1.0 — 2026-11-26 — 최초: 대본 공통 규칙(guides/script_rules.md v1.0) 점검 — 도입 30초 · 결론 먼저 ✗ · 썸네일 연결 · 챕터 끝 질문 · 직관적이지 않은 표현
#   사용자 지시 2026-11-26 "대본 도입부 30초 넘기지 말고 썸네일과 연결되고 … 결론부터 말하지 말고 하나씩 챕터를 정해서 알려주고 챕터 넘어갈 때마다 다음 챕터에 대한
#   호기심을 유발하면서 … '보는 때가 다르다' 처럼 직관적이지 못한 표현은 사용하지마 이걸 모든 영상 대본에 적용되는 공통 규칙으로 해서 파일로 기록하고".
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.4 | 2026-11-26 | 도입 '~봅니다' 말끝 ⚠ | main |
# | v1.3 | 2026-11-26 | HOST_FILLER ('오늘의 ~' 진행 멘트 ❌ — 문장 맨 앞 또는 '오늘의 주제·이야기·게임·영상…' · '오늘의 습관'처럼 내용 낱말은 안 걸림) | main |
# | v1.2 | 2026-11-26 | META(맥락 끊는 멘트) · HANDOFF · BENEFIT 자연스러운 꼴 | main |
# | v1.1 | 2026-11-26 | title_words · chapter_words · tts_checks | main |
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

VERSION = "v1.4"
INTRO_MAX_S = 30.0
# 직관적이지 않은 표현 (guides/script_rules.md 3번 표 — 새로 찾으면 여기와 그 표에 같이 더함)
VAGUE = [
    (r"보는\s*때가\s*다르", "'보는 때가 다르다' — 누가 무엇을 보는지 장면으로"),
    (r"(건네는|주는)\s*순간을\s*[,，]?\s*받는\s*(사람|쪽)은\s*그\s*뒤를", "'건네는 순간을, 받는 쪽은 그 뒤를' — 장면으로"),
    (r"손에는\s*.{0,20}마음이\s*들어\s*있", "'…손에는 …마음이 들어 있다' — 비유 대신 '이것이 첫 번째 이유입니다'"),
    (r"(아까움|미안함|부담)[이은]\s*.{0,12}넘어(가|오)", "'아까움이 넘어간다' — 무엇을 누가 하게 되는지 장면으로"),
]
# 진행 멘트 (guides/script_rules.md 8번 — 새로 찾으면 여기와 그 절에 같이 더함)
HOST_FILLER = [
    (r"^\s*오늘의\s|오늘의\s*(주제|이야기|게임|영상|시간|질문|순서|키워드|밸런스)", "'오늘의 ~' 진행 멘트 — 빼고 바로 내용으로 ('오늘은 ~를 보겠습니다'처럼 다룰 내용을 말하는 문장은 됨)"),
]
CONCLUSION_FIRST = r"결론부터|결론을\s*먼저|결론은\s*이렇|답부터\s*말씀"
# 시청자 이득 (1-⑤) — 대놓고 약속하는 꼴('끝까지 보시면'·'얻어 가실')은 셈하지 않고 META 로 ❌
BENEFIT = r"(지키려면|지키는|막으려면|피하려면|확인해야|해야\s*하는지|할\s*수\s*있|알\s*수\s*있|도움이\s*됩니다|챙기|쓸\s*수\s*있)"
# 맥락을 끊는 멘트 (guides/script_rules.md 7번) — 대본 어디서나 ❌
META = [
    (r"끝까지\s*(보시면|봐\s*주시면|시청)", "'끝까지 보시면' — 이득은 다룰 내용 안에 자연스럽게 (1-⑤)"),
    (r"얻어\s*가(실|세요|시)", "'얻어 가실 수 있습니다' — 대놓고 약속 ✗ (1-⑤)"),
    (r"(라고|이라고)\s*부르겠습니다", "호칭 선언 — 처음부터 그 이름으로 · 가명이면 설명란에"),
    (r"(이|오늘|이번)\s*영상에서는", "'이 영상에서는' — 영상 밖 말 · 내용으로 바로"),
]
# 내용 없는 넘김 — 본문에서 '…보겠습니다.'로 끝나는 짧은 문장 (⚠ — 다음 문장에 붙여 말함)
HANDOFF = r"^.{0,24}(보겠습니다|가 보겠습니다|살펴보겠습니다|알아보겠습니다)\.$"


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
        sentences=sum(len(p["sents"]) for p in parts), rule="guides/script_rules.md v1.4")
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
    for k, s in intro["sents"]:
        if re.search(r"(따라가|짚어|살펴|알아|들여다)\s*봅니다\.$", s):
            report("⚠", "도입 예고 말끝", sentence=k, text=s[:60], fix="'~봅니다' → '~보겠습니다' (script_rules.md 1번)")
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
    STOP = {"사람", "이유", "가지", "심리", "그리고", "하는", "있는", "없는", "합니다", "입니다"}
    def words(t: str) -> set[str]:
        return {w for w in re.findall(r"[가-힣]{2,}", t) if w not in STOP}
    def stem_in(w: str, text: str) -> bool:                 # 낱말 앞 2~3글자가 들어 있으면 같은 낱말로 봄 (조사·어미 차이)
        return w in text or (len(w) >= 3 and w[:3] in text) or (len(w) == 2 and w in text)
    # 5. 알고리즘 구조 — 제목 핵심 낱말이 도입 첫 두 문장 안에
    if a.package and Path(a.package).is_file():
        title = json.loads(Path(a.package).read_text("utf-8")).get("title", "")
        first2 = " ".join(s for _, s in intro["sents"][:2])
        tw = sorted(words(title))
        miss = [w for w in tw if not stem_in(w, first2)]
        report("✅" if len(miss) <= max(1, len(tw) // 3) else "⚠", "제목 낱말 → 도입 첫 두 문장", title=title[:40],
               missing=",".join(miss) or "-")
    for p in parts[1:-1]:
        cw = sorted(w for w in words(re.sub(r"^(첫|두|세|네|다섯)\s*번째,?\s*", "", p["name"])))
        first2 = " ".join(s for _, s in p["sents"][:3])
        miss = [w for w in cw if not stem_in(w, first2)]
        if cw and len(miss) > len(cw) // 2:
            report("⚠", "챕터 이름 낱말 → 챕터 첫 문장들", part=p["name"], missing=",".join(miss))
    # 6. 익숙한 말 — TTS 가 어색해지는 기호·꼴
    for k, s in ((k, s) for p in parts for k, s in p["sents"]):
        for pat, why in ((r"·", "가운뎃점 → '와·과'로"), (r"[()（）]", "괄호 → 말로 풀기"), (r"/", "슬래시 → 말로"),
                         (r"[A-Za-z]", "영어 글자 → 한국어로"), (r"'[^']*\"[^\"]*\"[^']*'|\"[^\"]*'[^']*'[^\"]*\"", "따옴표 안 따옴표")):
            if re.search(pat, s):
                report("⚠", "익숙한 말", sentence=k, text=s[:50], fix=why)
    # 챕터 끝 = 다음 챕터로 가는 질문 (마지막 두 챕터 = 마지막 본문·마무리는 뺌 — 마지막 본문은 마무리로 이어지므로 질문 아니어도 됨)
    for i, p in enumerate(parts[1:-2], start=1):
        last = p["sents"][-1][1] if p["sents"] else ""
        ok = last.rstrip().endswith("?")
        report("✅" if ok else "⚠", "챕터 끝 질문", part=p["name"], last=last[:50])
    mid = parts[-2]
    if mid["sents"] and not mid["sents"][-1][1].rstrip().endswith("?"):
        log("CHECK", level="ℹ", what="챕터 끝 질문", part=mid["name"], note="마지막 본문 챕터 — 마무리로 이어지므로 질문 아니어도 됨")
    for k, s in ((k, s) for p in parts for k, s in p["sents"]):
        for pat, why in META:
            if re.search(pat, s):
                report("❌", "맥락을 끊는 멘트", sentence=k, text=s[:60], fix=why)
    for k, s in ((k, s) for p in parts[1:] for k, s in p["sents"]):
        if re.search(HANDOFF, s):
            report("⚠", "내용 없는 넘김", sentence=k, text=s[:60], fix="다음 문장에 붙여 말함 (script_rules.md 7번)")
    for k, s in ((k, s) for p in parts for k, s in p["sents"]):
        for pat, why in VAGUE:
            if re.search(pat, s):
                report("❌", "직관적이지 않은 표현", sentence=k, text=s[:60], fix=why)
        for pat, why in HOST_FILLER:
            if re.search(pat, s):
                report("❌", "진행 멘트", sentence=k, text=s[:60], fix=why)
        if len(s) > 50:
            report("⚠", "긴 문장", sentence=k, chars=len(s), note="50자 넘음 — 자막 2줄 안인지 srt_tool 로")
    last = parts[-1]["sents"][-1][1] if parts[-1]["sents"] else ""
    report("✅" if last == "시청해주셔서 감사합니다." else "❌", "마지막 문장", last=last)
    log("DONE", bad=bad, warn=warn, next="❌ 고친 뒤 다시 · 그다음 guides/persona_loop.md" if bad else "규칙 점검 통과 → 페르소나 반복 검증")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
