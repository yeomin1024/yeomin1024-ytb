#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.11 — 2026-11-12 — **페르소나 반복 검증 관문** (사용자 지시 "제목,썸네일, 대본 만들때 자꾸 페르소나 반복 검증 빼먹는데 빼먹지 말도록 주제별 지시사항 수정해봐"):
#          script → 같은 폴더 persona_loop.json 의 script_exit·script_rebuttal (+ 편 기획 칸 package.json 이 있으면 title · upload.md 제목 = package.json 제목) ·
#          package → <기획안>.persona.json 의 title — tools/persona_gate.py 규칙(2회차 이상 · 회차마다 새 검토자 · 마지막 통과 · 본 글 = 지금 글)을 못 넘으면 ❌. guides/persona_loop.md.
# (v1.10) — 2026-11-04 — 정답 줄 말머리를 편마다 다르게 읽음(ANS_RE) · K10 새로: 같은 묶음 다른 편과 똑같은 문장 ❌ · 같은 말머리 ⚠ · 글 겹침 15% ⚠ (유튜브 '진정성 없는 콘텐츠' 막기 — 사용자 지시 "2~4편 1은 최대한 형식을 유지하면서 다르게 할 수 있는 부분은 다르게해 3은 수정하고 2는 영상 만들 때 최대한 피하도록 해" · "그리고 정책에 위반되지 않게 지시사항에도 반영하고").
# (v1.9) — 2026-11-04 — K9 새로: 질문 두 줄 뒤 '선택해 보세요.' → '3, 2, 1.' → '이때는 …옳은 선택입니다.' (사용자 지시 2026-11-04 "매수 하시겠습니까? 선택 항목 다음에 선택해보세요. 멘트 추가하고 3, 2, 1 카운트 후에 정답 얘기하도록수정해 다른 대본도 그렇게 하고" — quick_board 규칙 41) · K7 은 그 두 줄을 건너뛰고 보기를 찾음.
# (v1.8) — 2026-11-04 — K6·K7 질문형 선택(바로 정답·해설)도 읽음 (아래 줄).
# (v1.7) — 2026-11-03 — 기획안 `user_fields`(사용자가 준 칸) 의 제목 2줄 넘침은 ❌ 대신 ⚠ — 사용자 문구는 한 글자도 안 바꾸므로 판에서 빠지지 않게 (주제 판 피드백 2026-11-03 E2·E3 제목).
# (v1.6 — 2026-11-02 — 주식 쇼츠 공통 끝 멘트가 「다른 테스트가 궁금하다면 구독하고 채널에서 확인하세요.」 로 바뀜 (사용자 지시 "…로 변경해 모두") — 주식 규칙의 SHORT_END 만 바꿈 (재테크 규칙 그대로).
# (v1.5 — 2026-11-02 — 주제마다 규칙 파일 <주제>/board_rules.toml (없으면 주식 규칙 그대로): 채널 목적 밖(OFF)·조건(COND)·쇼츠 끝 멘트·
#   칸 이름 · 꼭 있어야 할 칸(REQUIRE — 재테크 complaint) · 사람·정당 탓(NO_TARGET) · 비속어(PROFANITY) · 제목·쇼츠 제목에서 피할 말 — 재테크 평가판
#   (사용자 지시 2026-11-02 "지시사항 수정됐으니 stock/guides/quick_board.md 대로 평가판 구성해"). 영향: rules()·check_package()·check_script()·main().
# (v1.4 — 2026-11-02 — 쇼츠 칸에서 '전달 내용·방식'(s_message) 뺌 (사용자 지시 "쇼츠 평가판에 전달내용 빼고 대본써서 하는걸로 하자") — 공통 끝 멘트는 쇼츠 대본 점검(script --kind short)에서 마지막 줄로 봄.)
# v1.8 — 2026-11-04 — 질문형 선택('여기서 당신은 …하시겠습니까?' / '아니면 …?' → '이때는 …옳은 선택입니다.' → 해설) — K6·K7 이 새 꼴도 읽음 (quick_board 규칙 25).
# (v1.3 — 2026-11-02 — K7(해설 정답 ↔ 보기) 이 새 보기 꼴 'A, …' 도 읽음 (전엔 'A번, …' 만 — 새 꼴에선 늘 '없음'으로 지나감).
# (v1.2 — 2026-11-02 — 저장소 밖 파일(시험·임시 대본)도 점검 — 결과 파일 경로를 저장소 기준으로 못 바꾸면 그대로 씀 (전엔 ValueError 로 멈춤) ·
#   광고 점검에서 --allow 문장과 쇼츠 공통 끝 멘트(「다른 테스트가 궁금하다면 구독하고 채널에서 확인하세요.」 — 사용자가 정한 줄, 2026-11-02 바뀜)는 뺌.
# (v1.1 — 2026-11-02 — 3단계 판(주제 → 대본 → 쇼츠)에 맞춤: package --stage topic|shorts (판마다 그 칸만) · script --kind short (해설·설명란 점검 뺌).
# (v1.0 — 2026-11-02 — 평가판에 처음 올리기 전 점검 (일반 페르소나 + 반론 페르소나) — 토큰을 쓰지 않는 규칙 점검
#   사용자 지시 2026-11-02 "처음 평가판에 올라가기 전에는 일반, 반론 페르소나로 점검은 거쳐야해 토큰 최대한 아끼는 방식으로 하고".
#   · 일반 페르소나 = stock/result/outliers/personas.json (tools/persona_review.py 의 review — 풀이 없는 어려운 말·50자 넘는 문장·광고·겁주기 + 페르소나가 원하는 말)
#   · 반론 페르소나 = stock/result/outliers/rebuttal_persona.md 0번 표의 K1~K8 질문을 규칙으로 (낱말·꼴·숫자 대조) — 규칙이 못 보는 것은 '사람 확인' 줄로 남김
#   · 결과: 통과(✅) · 고칠 것(❌ — 고친 뒤 다시) · 사람 확인(⚠ — Claude 가 그 줄만 읽고 판단) → 판의 카드에 '점검' 칸으로 붙음
#   연구·교육용 도구 — 투자 권유가 아님.
r"""
  python3 tools/board_check.py script  stock <대본.txt> [--kind long|short] [--calc <json>] [--upload <upload.md>] [--allow "<사용자 문장 일부>" …]
  python3 tools/board_check.py package stock <기획안.json> [--stage topic|shorts] [--write]   # topic → 주제 평가판(롱폼 칸) · shorts → 쇼츠 평가판(쇼츠 칸)
끝 코드: ❌ 가 하나라도 있으면 1.
"""
import contextlib
import io
import json
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
VERSION = "v1.11"
SENT_MAX = 50

# K8 권유·과장 — 사용자가 정한 제목 꼴('절대 통과 못하는')은 뺌
SHORT_END = "구독하고 채널에서 확인하세요"   # 쇼츠 공통 끝 멘트 (stock/topics/쇼츠안_2026-10-30.md 머리 — 사용자가 정한 줄)
K8 = re.compile(r"무조건|반드시|100\s?%\s?(수익|보장)|확실히 (번|오른)|(?<!절대 통과 )절대(?! 통과)|사세요|파세요|매수하세요|매도하세요|추천 ?종목|수익 보장|대박|떡상|인생 역전")
# K2 결과론·앞으로도
K2 = re.compile(r"앞으로도 (반드시|꼭|계속)|항상 (오른|이긴)|늘 (오른|이긴)|영원히")
# 채널 목적 밖 (stock/guides/channel.md 1번 — 단타·타이밍·종목/업종 맞히기·'더 벌었나')
OFF = re.compile(r"단타|스캘핑|급등주 찾|종목 맞히|업종 맞히|수익률 대결|누가 더 벌|타이밍 맞히|바닥 맞히")
COND = re.compile(r"년|달|개월|쓸 일|급할 때|비상금|은퇴|월급|목돈|나이|기간|조건|계좌의|비중")


SERIES_OK = {"선택해 보세요.", "3, 2, 1.", "그럼 모두 성공 투자 하시기 바랍니다.", "시청해주셔서 감사합니다."}   # v1.10 시리즈 표시 — 편마다 같아도 됨
OPENER_RES = {"질문": r"^(.{0,12}?)당신은 .+\?$", "정답": r"^(\S+(?: \S+)?는) .+것이 옳은 선택입니다\.$", "결론": r"^(\S+) 옳은 선택은 ", "날짜": r"^(\S+) \d{4}년 \d{1,2}월 \d{1,2}일[,은이]"}


def series_overlap(path, sents):
    """v1.10: 같은 묶음(폴더 이름 끝 '-<꼴>-YYYY-MM' 이 같은 다른 대본)과 비교 — 같은 문장(시리즈 표시 빼고) ❌ ·
    같은 말머리(질문·정답·결론·날짜) ⚠ · 5글자 조각 겹침 15% 넘으면 ⚠. (사용자 지시 2026-11-04 '정책에 위반되지 않게')"""
    p = Path(path).resolve()
    m = re.search(r"(-[a-z]+-\d{4}-\d{2})$", p.parent.name)
    if not m or p.stem != p.parent.name:
        return [], []
    sibs = [q / f"{q.name}.txt" for q in sorted(p.parent.parent.glob(f"*{m.group(1)}")) if q != p.parent and (q / f"{q.name}.txt").is_file()]
    if not sibs:
        return [], []
    norm = lambda t: re.sub(r"\s+", "", t)
    grams = lambda ts: {norm(t)[i:i + 5] for t in ts for i in range(max(0, len(norm(t)) - 4))}
    def openers(ss):
        out = {}
        for k, rx in OPENER_RES.items():
            for i, t in enumerate(ss):
                if k == "질문" and not (i + 1 < len(ss) and ss[i + 1].startswith("아니면 ")):   # 선택 질문만 (결과 질문 '이 테스트에서 당신은' 은 뺌)
                    continue
                mm = re.match(rx, t)
                if mm and mm.group(1).strip():
                    out.setdefault(k, set()).add(mm.group(1).strip())
        return out
    mine = [t for t in sents if t not in SERIES_OK]
    myop, g0 = openers(sents), grams(mine)
    fails, warns = [], []
    for q in sibs:
        other = [l.strip() for l in q.read_text("utf-8").splitlines() if l.strip() and not l.startswith("-")]
        same = sorted(set(mine) & set(other))
        if same:
            fails.append(f"반론 K10 시리즈 겹침: {q.parent.name} 와 똑같은 문장 {len(same)}개 {same[:3]} — 편마다 다르게 (규칙 43)")
        op = openers(other)
        dup = {k: sorted(myop.get(k, set()) & op.get(k, set())) for k in OPENER_RES}
        dup = {k: v for k, v in dup.items() if v}
        if dup:
            warns.append(f"반론 K10 말머리가 {q.parent.name} 와 같음 {dup} — 편마다 다른 말머리로 (규칙 43)")
        g1 = grams([t for t in other if t not in SERIES_OK])
        jac = len(g0 & g1) / max(1, len(g0 | g1))
        if jac > 0.15:
            warns.append(f"반론 K10 글 겹침 {jac:.0%} ({q.parent.name}) — 15% 넘음")
    return fails, warns


def log(stage, **kv):
    ts = time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime())
    print(f"[{stage}] [{ts}] " + " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) else v}" for k, v in kv.items()))


def rules(topic):
    """v1.4: <주제>/board_rules.toml — 없으면 주식 규칙(위 상수) 그대로."""
    p = ROOT / topic / "board_rules.toml"
    R = {"OFF": OFF, "COND": COND, "SHORT_END": SHORT_END, "PURPOSE": "채널 목적(덜 잃기·장기)", "COND_LABEL": "반론 K1 조건(돈 쓸 때·기간·비중)을 보기에 못 박았나",
         "VERIFY_LABEL": "반론 K3 다른 기간·다른 하락장으로 확인할 길", "BASIS_LABEL": "분석 근거(data_insights 5-1)", "REQUIRE": [], "NO_TARGET": None,
         "PROFANITY": None, "TITLE_BANNED": None, "SHORTS_TITLE_BANNED": None, "FIELD_NAMES": {}, "SHORT_END_PKG": None}
    if p.is_file():
        import tomllib
        d = tomllib.loads(p.read_text("utf-8"))
        for k in ("OFF", "COND", "NO_TARGET", "PROFANITY", "TITLE_BANNED", "SHORTS_TITLE_BANNED"):
            if d.get(k):
                R[k] = re.compile(d[k])
        for k in ("SHORT_END", "PURPOSE", "COND_LABEL", "VERIFY_LABEL", "BASIS_LABEL"):
            if d.get(k):
                R[k] = d[k]
        R["SHORT_END_PKG"] = d.get("SHORT_END") or None
        R["REQUIRE"] = d.get("REQUIRE") or []
        R["FIELD_NAMES"] = d.get("FIELD_NAMES") or {}
    return R


def numbers_in_calc(path):
    """계산 JSON 안의 모든 숫자(문자열 '+12.3%' 꼴 포함) → 절댓값 집합."""
    vals = set()

    def walk(x):
        if isinstance(x, dict):
            for v in x.values():
                walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)
        elif isinstance(x, (int, float)) and not isinstance(x, bool):
            vals.add(abs(float(x)))
        elif isinstance(x, str):
            for m in re.findall(r"[-+−]?\d+(?:\.\d+)?", x):
                vals.add(abs(float(m.replace("−", "-"))))
    walk(json.loads(Path(path).read_text("utf-8")))
    return vals


def pct_ok(n, vals):
    """대본의 정수 퍼센트 n 이 계산 값(퍼센트·비율)을 반올림·버림한 값인가."""
    for v in vals:
        for x in (v, v * 100):
            if round(x) == n or int(x) == n or (n % 10 == 0 and abs(x - n) < 3):
                return True
    return False


def check_script(topic, script, calc=None, upload=None, allow=(), kind="long"):
    import persona_review as PR
    with contextlib.redirect_stdout(io.StringIO()):
        R = PR.review(topic, script)
    sents = R["sents"]
    fails, warns, oks = [], [], []
    # ── 일반 페르소나
    un = [(t, v["n"]) for t, v in R["first"].items() if not v["explained"]]
    if un:
        fails.append(f"일반: 풀이 없는 어려운 말 {un}")
    longs = [(i, n) for i, s, n in R["long"] if not any(a in s for a in allow)]
    (fails if longs else oks).append(f"일반: 50자 넘는 문장 {longs or '없음 (사용자 문장은 뺌)'}")
    # 사용자가 정한 문장(--allow)과 쇼츠 공통 끝 멘트(쇼츠안 머리 — 사용자 지시)는 광고로 세지 않음
    RL = rules(topic)
    ads = [(i, x) for i, x in R["ads"] if not any(a in x for a in allow) and not (kind == "short" and RL["SHORT_END"] in x)]
    if ads or R["scares"]:
        fails.append(f"일반: 광고 {[i for i, _ in ads]} · 겁주기 {[i for i, _ in R['scares']]}")
    elif R["ads"]:
        oks.append(f"일반: 광고 없음 (사용자 문장·쇼츠 공통 끝 멘트 {len(R['ads'])}개는 뺌)")
    oks.append(f"일반: 약 {R['est_min']:.1f}분 · 페르소나마다 원하는 말 " + ", ".join(f"{r['p']['id']} {len(r['covered'])}/{len(r['wants'])}" for r in R["rows"]))
    # ── 반론 K8·K2
    k8 = [(i, s) for i, s in enumerate(sents, 1) if K8.search(s) and not any(a in s for a in allow)]
    (fails if k8 else oks).append(f"반론 K8 권유·과장: {k8 or '없음'}")
    k2 = [(i, s) for i, s in enumerate(sents, 1) if K2.search(s)]
    (fails if k2 else oks).append(f"반론 K2 결과론: {k2 or '없음'}")
    for lab, rx in (("사람·정당 탓", RL["NO_TARGET"]), ("비속어", RL["PROFANITY"])):     # v1.4 주제 규칙 (재테크)
        if rx:
            hit = [(i, s[:40]) for i, s in enumerate(sents, 1) if rx.search(s)]
            (fails if hit else oks).append(f"채널 선 — {lab}: {hit or '없음'}")
    if kind == "short":                                   # 쇼츠: 해설·보기·설명란이 없음 → K6·K7·K2/K4 설명란 점검 뺌
        end = RL["SHORT_END"]                          # v1.5 주제마다 (주식 '구독하고 채널에서 확인하세요' · 재테크 '아래 영상에서 확인하세요')
        (oks if any(end in x for x in sents[-2:]) else fails).append(f"쇼츠 공통 끝 멘트(마지막 줄 「…{end}.」): " + ("있음" if any(end in x for x in sents[-2:]) else "없음"))
        if calc:
            vals = numbers_in_calc(calc)
            loose = [(i, m.group(0)) for i, s in enumerate(sents, 1) for m in re.finditer(r"(\d+(?:\.\d+)?)\s?%", s) if float(m.group(1)) == int(float(m.group(1))) and not pct_ok(int(float(m.group(1))), vals)]
            (warns if loose else oks).append(f"반론 K5 계산 출력에 없는 % (사람 확인): {loose or '없음'}")
        else:
            warns.append("반론 K5: --calc 없음 — 숫자 대조 못 함")
        return fails, warns, oks
    COUNT_LINES = ("선택해 보세요.", "3, 2, 1.")             # v1.9 질문과 정답 사이 (규칙 41)
    ANS_RE = r"^.+것이 옳은 선택입니다\.$"                    # v1.10 정답 줄 (말머리 '이때는'·'이럴 때는'·'이 국면에서는' … 편마다)
    # ── K6 지키기 어려움 인정 — 해설마다 '물론 …' 반론 줄
    heads = [i for i, s in enumerate(sents) if re.match(r"(첫|두|세|네|다섯) 번째 선택의 정답은", s)
             or re.match(ANS_RE, s)]                               # v1.8 질문형 선택 → 바로 정답·해설 · v1.10 말머리는 편마다 다름
    miss = []
    for k, h in enumerate(heads):
        end = heads[k + 1] if k + 1 < len(heads) else len(sents)
        if not any(s.startswith("물론") for s in sents[h:end]):
            miss.append(k + 1)
    (fails if miss else oks).append(f"반론 K6 '물론…하지만' 없는 해설: {miss or '없음'} (해설 {len(heads)}개)")
    # ── K7 모순 — 해설 '정답은 X, …' 이 보기 X 와 같은 말인가
    opts = {}
    q = 0
    for s in sents:
        if re.match(r"여기서 .+ 번째 선택입니다", s):
            q += 1
        m = re.match(r"([AB])번?, (.+)", s)   # 보기 꼴 'A, …'(2026-11-02 사용자 지시) · 옛 'A번, …' 둘 다
        if m and q:
            opts[(q, m.group(1))] = m.group(2)
    bad7, letters = [], []
    words = lambda t: set(re.findall(r"[가-힣A-Za-z0-9%]{2,}", t))
    for k, h in enumerate(heads):
        if re.match(ANS_RE, sents[h]) and h >= 2:            # v1.8 질문형: 바로 앞 두 줄 '(말머리) 당신은 …?' / '아니면 …?' 가 보기
            j = h                                              # v1.9 그 사이 '선택해 보세요.' · '3, 2, 1.' (규칙 41) 은 건너뜀
            while j > 2 and sents[j - 1] in COUNT_LINES:
                j -= 1
            qa, qb = re.match(r"^.{0,12}?당신은 (.+)\?$", sents[j - 2]), re.match(r"아니면 (.+)\?$", sents[j - 1])   # v1.10 말머리 편마다
            if not (qa and qb):
                bad7.append((k + 1, "?", "질문 두 줄이 정답 바로 앞에 없음"))
                continue
            w = words(re.sub(r"^\S+(?: \S+)?(?:는|에는|서는) ", "", sents[h]).replace("옳은 선택입니다", ""))
            sa, sb = len(w & words(qa.group(1))), len(w & words(qb.group(1)))
            letters.append("A" if sa > sb else "B")
            if max(sa, sb) == 0 or sa == sb:
                bad7.append((k + 1, "?", "정답 말이 어느 보기와 같은지 모름"))
            continue
        m = re.search(r"정답은 ([AB])번?, (.+)", sents[h])
        if not m:
            continue
        letters.append(m.group(1))
        o = opts.get((k + 1, m.group(1)), "")
        a = set(re.findall(r"[가-힣A-Za-z0-9%]{2,}", o)); b = set(re.findall(r"[가-힣A-Za-z0-9%]{2,}", m.group(2)))
        if a and len(a & b) / len(a) < 0.25:
            bad7.append((k + 1, m.group(1), o))
    (warns if bad7 else oks).append(f"반론 K7 해설 정답 ↔ 보기 말이 다름(사람 확인): {bad7 or '없음'} · 정답 글자 {''.join(letters)}")
    # ── K9 (v1.9) 질문 뒤 '선택해 보세요.' → '3, 2, 1.' → 정답 (quick_board 규칙 41 — 사용자 지시 2026-11-04)
    qheads = [h for h in heads if re.match(ANS_RE, sents[h])]
    miss9 = [k + 1 for k, h in enumerate(qheads) if h < 2 or tuple(sents[h - 2:h]) != COUNT_LINES]
    if qheads:
        (fails if miss9 else oks).append(f"반론 K9 질문 뒤 '선택해 보세요.' · '3, 2, 1.' 없음: {miss9 or '없음'} (선택 {len(qheads)}개)")
    if letters and len(set(letters)) == 1:
        fails.append("반론 K7: 정답이 모두 같은 글자 — 섞어야 함")
    # ── K10 (v1.10) 시리즈 겹침 — 유튜브 '진정성 없는 콘텐츠'(틀로 찍어 거의 같은 영상) 막기 (quick_board 규칙 43)
    k10f, k10w = series_overlap(script, sents) if kind == "long" else ([], [])
    fails += k10f; warns += k10w
    if not (k10f or k10w):
        oks.append("반론 K10 시리즈 겹침: 다른 편과 같은 문장·같은 말머리 없음 (시리즈 표시 문장 제외)")
    # ── K5 숫자 — 대본 퍼센트가 계산 출력에 있는가
    if calc:
        vals = numbers_in_calc(calc)
        loose = []
        for i, s in enumerate(sents, 1):
            for m in re.finditer(r"(\d+(?:\.\d+)?)\s?%", s):
                n = float(m.group(1))
                if n == int(n) and not pct_ok(int(n), vals):
                    loose.append((i, m.group(0)))
        (warns if loose else oks).append(f"반론 K5 계산 출력에 없는 % (사람 확인 — 연구 인용·규칙 숫자일 수 있음): {loose or '없음'}")
    else:
        warns.append("반론 K5: --calc 없음 — 숫자 대조 못 함")
    # ── K2·K4 한계·뺀 비용 — 설명란(업로드 시트)에
    if upload:
        u = Path(upload).read_text("utf-8")
        need = {"K2 과거 자료 한계": r"과거.*(보장|같다는)", "K4 뺀 비용(세금·수수료·환율)": r"(세금|수수료).*(뺐|빼)|환율.*(뺐|빼)"}
        for k, pat in need.items():
            (oks if re.search(pat, u) else fails).append(f"반론 {k}: 설명란 {'있음' if re.search(pat, u) else '없음'}")
    else:
        warns.append("반론 K2·K4: --upload 없음 — 설명란 확인 못 함")
    # ── K1·K3 — 규칙으로 못 봄 → 날짜 있는 사례 목록만
    dated = [(i, s) for i, s in enumerate(sents, 1) if re.search(r"20\d\d년 \d+월 \d+일", s)]
    warns.append(f"반론 K1·K3 (사람 확인 — 조건이 먼저 못 박혔나 · 다른 기간이면 뒤집히나: calc 노트·precheck): 날짜 사례 {len(dated)}개 {[i for i, _ in dated]}")
    return fails, warns, oks


FIELDS_TOPIC = [("message", "전달 내용"), ("approach", "전달 방식"), ("title", "제목"), ("thumb_main", "썸네일 문구"), ("thumb_sub", "썸네일 보조 문구")]
FIELDS_SHORTS = [("s_title", "쇼츠 제목"), ("s_thumb_main", "쇼츠 썸네일 문구"), ("s_thumb_sub", "쇼츠 썸네일 보조 문구")]   # v1.4 전달 내용 칸 없음 — 쇼츠는 대본(script --kind short)으로 점검


def txt(v):
    return " / ".join(v) if isinstance(v, list) else str(v or "")


def check_package(topic, pk, personas, adv, stage="topic"):
    import title_fit as TF
    RL = rules(topic)
    fails, warns, oks = [], [], []
    FIELDS = FIELDS_TOPIC if stage == "topic" else FIELDS_SHORTS
    if stage == "topic":
        FIELDS = [(k, RL["FIELD_NAMES"].get(k, k)) for k in RL["REQUIRE"]] + FIELDS      # v1.4 꼭 있어야 할 칸 (재테크 complaint)
    miss = [lab for k, lab in FIELDS if not txt(pk.get(k)).strip()]
    if miss:
        fails.append(f"빈 칸: {miss}")
    allt = " ".join(txt(pk.get(k)) for k, _ in FIELDS)
    # 일반 페르소나 — 원하는 말 · 어려운 말 · 길이
    hit = {p["id"]: [w for w in p["wants"] if w.lower() in allt.lower()] for p in personas}
    best = max(hit.items(), key=lambda x: len(x[1]))
    (oks if best[1] else warns).append(f"일반: 페르소나 원하는 말 — " + " · ".join(f"{k} {len(v)}" for k, v in hit.items()) + (f" (가장 가까운 {best[0]}: {best[1][:5]})" if best[1] else " — 아무도 안 걸림(사람 확인)"))
    hard = [t for t in adv if t in allt]
    (warns if hard else oks).append(f"일반: 어려운 말 {hard or '없음'} (대본에서 풀이 필요)")
    tm = txt(pk.get("thumb_main" if stage == "topic" else "s_thumb_main")).replace(" / ", "")
    (warns if len(tm) > 26 else oks).append(f"일반: 썸네일 주요 문구 {len(tm)}자 (성공 중앙값 22 — 26 넘으면 줄임)")
    for key, sh in ((("title", False),) if stage == "topic" else (("s_title", True),)):
        t = txt(pk.get(key))
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            ok = TF.report(t, sh) if t else False
        user = key in (pk.get("user_fields") or [])      # v1.7 사용자가 준 문구 — 고치지 않으므로 ⚠ (사람 확인)로만
        (oks if ok else (warns if user else fails)).append(f"일반: {'쇼츠 ' if sh else ''}제목 화면 2줄 안 {'✅' if ok else ('⚠ 잘림 — 사용자 제목이라 그대로' if user else '❌ 잘림')} ({len(t)}자)")
        bx = RL["SHORTS_TITLE_BANNED" if sh else "TITLE_BANNED"]
        if bx:
            mb = bx.search(t)
            (fails if mb else oks).append(f"일반: {'쇼츠 ' if sh else ''}제목에서 피할 말 {'❌ ' + mb.group(0) if mb else '없음'}")
    # 반론
    k8 = [k for k, _ in FIELDS if K8.search(txt(pk.get(k)))]
    (fails if k8 else oks).append(f"반론 K8 권유·과장 낱말: {k8 or '없음'}")
    k2 = [k for k, _ in FIELDS if K2.search(txt(pk.get(k)))]
    (fails if k2 else oks).append(f"반론 K2 결과론 낱말: {k2 or '없음'}")
    off = RL["OFF"].search(allt)
    (fails if off else oks).append(f"{RL['PURPOSE']}: {'❌ ' + off.group(0) if off else '맞음'}")
    for lab, rx in (("사람·정당 탓", RL["NO_TARGET"]), ("비속어", RL["PROFANITY"])):     # v1.4 주제 규칙 (재테크 채널 선)
        if rx:
            m = rx.search(allt)
            (fails if m else oks).append(f"채널 선 — {lab}: {'❌ ' + m.group(0) if m else '없음'}")
    nums = [k for k, _ in FIELDS if k not in ("message", "approach", "s_message") and re.search(r"\d", txt(pk.get(k)))]
    (warns if nums and not pk.get("calc") else oks).append(f"반론 K5 숫자 칸 {nums or '없음'} · 계산 근거 {'있음' if pk.get('calc') else '없음 — 숫자는 대본 계산 때 확인'}")
    if stage == "topic":
        (oks if RL["COND"].search(txt(pk.get("approach"))) else warns).append(f"{RL['COND_LABEL']}: " + ("있음" if RL["COND"].search(txt(pk.get("approach"))) else "안 보임(사람 확인)"))
        (oks if txt(pk.get("verify")).strip() else fails).append(f"{RL['VERIFY_LABEL']}: {txt(pk.get('verify')) or '없음'}")
        (oks if txt(pk.get("basis")).strip() else warns).append(f"{RL['BASIS_LABEL']}: " + ("있음" if txt(pk.get("basis")).strip() else "없음"))
    return fails, warns, oks


import persona_gate as PG  # noqa: E402  (v1.11)


def gate_script(path, upload=None, short=False):
    """(v1.11) 대본 → 같은 폴더 persona_loop.json — 이탈·반론 반복 검증 · 편 기획 칸 package.json 이 있으면 제목·썸네일 피드 시험과 upload.md 제목 일치."""
    sp = Path(path).resolve()
    rec, item = sp.parent / "persona_loop.json", sp.stem
    cur = PG.sha(PG.script_text(sp))
    fails, oks = [], []
    for stg in ("script_exit", "script_rebuttal"):
        pr = PG.problems(rec, item, stg, cur)
        (fails.extend(f"페르소나 반복 검증 ❌ {x}" for x in pr)) if pr else oks.append(f"페르소나 반복 검증: {PG.STAGES[stg]} 통과 (persona_gate)")
    plan = sp.parent / "package.json"
    if plan.is_file():
        pk = json.loads(plan.read_text("utf-8"))
        pr = PG.problems(rec, item, "title", PG.sha(PG.title_text(pk, short)))
        (fails.extend(f"페르소나 반복 검증 ❌ {x}" for x in pr)) if pr else oks.append("페르소나 반복 검증: 제목·썸네일 피드 시험 통과 (persona_gate)")
        if upload and Path(upload).is_file() and not short:
            m = re.search(r"^##\s*\d+\.\s*[^\n]*제목[^\n]*\n(.*?)(?=^##\s|\Z)", Path(upload).read_text("utf-8"), re.M | re.S)
            c = re.search(r"```[^\n]*\n(.*?)\n```", m.group(1), re.S) if m else None
            ut = c.group(1).strip() if c else ""
            (oks if ut == txt(pk.get("title")).strip() else fails).append(f"업로드 시트 제목 = package.json 제목: {'같음' if ut == txt(pk.get('title')).strip() else '❌ 다름 — 바꿨으면 package.json 도 바꾸고 피드 시험 다시'}")
    else:
        oks.append("페르소나 반복 검증: package.json 없음 — 제목·썸네일 피드 시험은 기획안 묶음(<기획안>.persona.json)에서 확인")
    return fails, oks


def main(argv):
    if len(argv) < 3 or argv[0] not in ("script", "package"):
        print(__doc__)
        return 2
    mode, topic, path = argv[0], argv[1], argv[2]
    opt = lambda k: argv[argv.index(k) + 1] if k in argv else None  # noqa: E731
    allow = [argv[i + 1] for i, a in enumerate(argv) if a == "--allow"]
    log("START", tool=f"board_check.py {VERSION}", mode=mode, topic=topic, path=path)
    if mode == "script":
        f, w, o = check_script(topic, path, opt("--calc"), opt("--upload"), allow, opt("--kind") or "long")
        gf, go = gate_script(path, opt("--upload"), (opt("--kind") or "long") == "short")      # v1.11 페르소나 반복 검증
        f, o = f + gf, o + go
        out = Path(path).resolve().with_name("board_check.md" if (opt("--kind") or "long") == "long" else "board_check_shorts.md")
        md = [f"# 평가판 전 점검 — {Path(path).name} ({time.strftime('%Y-%m-%d')}, board_check.py {VERSION})", "", f"결과: {'❌ 고칠 것 ' + str(len(f)) if f else '✅ 통과'} · ⚠ 사람 확인 {len(w)}", ""]
        md += [f"- ❌ {x}" for x in f] + [f"- ⚠ {x}" for x in w] + [f"- ✅ {x}" for x in o]
        out.write_text("\n".join(md) + "\n", "utf-8")
        log("DONE", fails=len(f), warns=len(w), out=(str(out.relative_to(ROOT)) if out.is_relative_to(ROOT) else str(out)))
        for x in f + w:
            print("   ", x[:300])
        return 1 if f else 0
    import personas as pz
    P = json.loads((ROOT / topic / "result" / "outliers" / "personas.json").read_text("utf-8"))
    personas = [{"id": p["id"], "wants": [t for t, _ in p["want_terms"][:8]] + [w for w, c in p["want_words"][:8] if c >= 2]} for p in P["personas"]]
    with contextlib.redirect_stdout(io.StringIO()):
        cfg, _ = pz.load_cfg(topic, ROOT)
    k = (cfg or {}).get("know") or {}
    adv = list(dict.fromkeys((k.get("advanced") or []) + (k.get("advanced_en") or [])))
    D = json.loads(Path(path).read_text("utf-8"))
    bad = 0
    stage = opt("--stage") or "topic"
    rec = Path(path).with_suffix(".persona.json")                                                   # v1.11 기획안 묶음의 피드 시험 기록
    for pk in D["packages"]:
        f, w, o = check_package(topic, pk, personas, adv, stage)
        if not pk.get("existing"):                                                                   # 이미 대본이 있는 옛 편(E1~)은 그 편 폴더에서
            item = pk.get("id", "") + ("-shorts" if stage == "shorts" else "")
            pr = PG.problems(rec, item, "title", PG.sha(PG.title_text(pk, stage == "shorts")))
            f, o = (f + [f"페르소나 반복 검증 ❌ {x}" for x in pr]) if pr else f, (o if pr else o + ["페르소나 반복 검증: 제목·썸네일 피드 시험 통과 (persona_gate)"])
        pk["check" if stage == "topic" else "check_shorts"] = {"tool": f"board_check.py {VERSION}", "at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "pass": not f,
                       "fail": f, "warn": w, "ok": o}
        bad += bool(f)
        log("CHECK", id=pk.get("id"), result="통과" if not f else "고칠 것", fails=len(f), warns=len(w))
        for x in f + w:
            print("   ", x[:240])
    if "--write" in argv:
        Path(path).write_text(json.dumps(D, ensure_ascii=False, indent=1) + "\n", "utf-8")
    log("DONE", packages=len(D["packages"]), fail=bad, wrote="--write" in argv)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
