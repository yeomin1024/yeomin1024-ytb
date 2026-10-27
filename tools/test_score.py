#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-10-27 — 점수 단계를 편마다 고를 수 있게 (check_rules(levels=…)) — 재무제표 편이 5항목 × 0·10·20점
#          (사용자 지시 "5개 정도만 찾고 재무지표를 상세하게 분석하는 걸로 해"). 기본값 0·5·10 은 그대로라 10항목 편은 바뀌지 않음.
# (v1.0 — 2026-10-27 — 최초. 주식 테스트형 영상(stock/guides/quick_test.md)의 점수 규칙을 편마다 다시 쓰지 않게 공용으로.
#          첫 편 stock/source/simri-test-2026-10/calc/calc.py v1.6 의 grade·letters_for·규칙 검사·가상 응시를 그대로 옮김
#          (첫 편 코드는 그대로 둠). 사용자 지시 2026-10-27: "토큰은 가장 아낄 수 있도록 구조를 잡고 해".)
#
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.1 | 2026-10-27 | levels 인자 (기본 0·5·10) · 등급 구간 글을 단계 폭으로 | check_rules |
# | v1.0 | 2026-10-27 | 최초 (첫 편 calc v1.6 에서 옮김) | grade · letters_for · check_rules · run_virtual |
#
# 쓰는 법 (편의 calc/calc.py 에서):
#   sys.path.insert(0, str(ROOT / "tools")); import test_score as ts
#   QUESTIONS = [(번호, 짧은 이름, 과락 문항인가, {"A": 0, "B": 10, "C": 5}), …]   # 요약본 [항목N] 보기 순서와 같게
#   ts.check_rules(QUESTIONS, out, log) · ts.run_virtual(QUESTIONS, VIRTUAL, out)
# 등급 (quick_test.md 4번): 과락 문항에서 0점 → 총점과 상관없이 불통과 · 70점 이상 통과 · 40~65 주의 · 35 이하 불통과.
# ※ 연구·교육용 — 투자 권유가 아님.
import itertools
from collections import Counter

VERSION = "v1.1"
LEVELS = (0, 5, 10)
PASS_MIN = 70       # 통과: 과락 없이 70점 이상
CAUTION_MIN = 40    # 주의: 40~65점 · 불통과: 35점 이하


def letters_for(questions, levels):
    """점수 줄(예: [10, 10, 5, …]) → 그 점수가 나오는 보기 글자 줄 (가상 응시를 글자로 보이려고)."""
    return "".join({p: a for a, p in key.items()}[lv] for (_, _, _, key), lv in zip(questions, levels))


def grade(questions, answers):
    """answers: 'ABC…' 10글자 → (총점, 등급, 과락 문항 목록)."""
    if len(answers) != len(questions) or any(a not in "ABC" for a in answers):
        raise ValueError(f"답은 A/B/C {len(questions)}개여야 함: {answers!r}")
    pts = [key[a] for (_, _, _, key), a in zip(questions, answers)]
    total = sum(pts)
    fails = [q for (q, _, cut, _), p in zip(questions, pts) if cut and p == 0]
    if fails:
        return total, "불통과(과락)", fails
    if total >= PASS_MIN:
        return total, "통과", fails
    if total >= CAUTION_MIN:
        return total, "주의", fails
    return total, "불통과", fails


def check_rules(questions, out, log, levels=LEVELS):
    """항목마다 levels(기본 0·5·10) 가 하나씩인지 · 최고점 자리가 섞였는지 · 모든 경우(3^N)의 등급 분포. 문제 수를 돌려준다."""
    step = levels[1] - levels[0]
    best = "".join(max(k, key=k.get) for *_, k in questions)
    out("RULE", questions=len(questions), levels=levels, max_total=len(questions) * max(levels),
        pass_min=PASS_MIN, caution=f"{CAUTION_MIN}~{PASS_MIN - step}", fail=f"0~{CAUTION_MIN - step}",
        cut_questions=[q for q, _, c, _ in questions if c], best_letter=best,
        zero_letter="".join(min(k, key=k.get) for *_, k in questions))
    problems = 0
    if len(questions) * max(levels) != 100:
        problems += 1
        log.warning(f"max_total={len(questions) * max(levels)} problem=만점이 100 이 아니라 통과 {PASS_MIN}·주의 {CAUTION_MIN} 기준이 맞지 않음", extra={"stage": "RULE"})
    for q, name, _, key in questions:
        if sorted(key.values()) != list(levels):
            problems += 1
            log.warning(f"q={q} name={name} key={key} problem=점수 {levels} 가 하나씩이 아님", extra={"stage": "RULE"})
    spread = Counter(best)
    if max(spread.values()) > len(questions) // 2:  # 한 글자가 절반을 넘으면 '늘 B' 같은 찍기가 통함
        problems += 1
        log.warning(f"best_letter={best} spread={dict(spread)} problem=10점 자리가 한 글자에 몰림", extra={"stage": "RULE"})
    # 모든 경우를 채점해 등급이 빈틈·겹침 없이 나뉘는지 본다. '아무렇게나 고르면'의 비율은 사람의 분포가 아니다.
    bands = Counter(grade(questions, "".join(c))[1] for c in itertools.product("ABC", repeat=len(questions)))
    n = sum(bands.values())
    out("CHECK", combos=n, problems=problems, **{k: f"{v} ({v / n * 100:.1f}%)" for k, v in sorted(bands.items())})
    return problems


def run_virtual(questions, virtual, out):
    """virtual: [(이름, [점수 N개]), …] — 규칙이 뜻대로 움직이는지 보는 예 (실제 사람 아님)."""
    for name, levels in virtual:
        ans = letters_for(questions, levels)
        t, g, fails = grade(questions, ans)
        out("VIRTUAL", name=name.replace(" ", "_"), answers=ans, total=t, grade=g, cut_fail=fails or "-")
