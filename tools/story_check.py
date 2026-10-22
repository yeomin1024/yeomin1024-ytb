#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.2 — 2026-10-22 — 도입 30초 안 (사용자 지시 2026-10-22 "초반 30초로 하고") — 추정 30초 넘으면 문제, 165음절 넘으면 경고.
# (v1.1) — 2026-10-21 — 제목 맨 앞 낱말은 끝 조사를 떼고도 찾음('손절보다' → '손절') · -마무리 3~5문장(시리즈 '다음 화 예고' 한 문장 —
#          story_script v1.2 6번, 사용자 지시 "그리고 시리즈물이라는 것도 고려해").
# (v1.0) — 2026-10-21 — 새로: 이야기형 주식 대본(개미 주인공 1인칭) 점검 — stock/guides/story_script.md v1.0 의 구성·말투 규칙.
#          사용자 지시 2026-10-21 "아래 내용을 지키도록 대본 내용을 만드는 지시사항 파일을 만들어 … 1. 도입부(35초 이내) … 2. 찾은 방법 이야기
#          … 첫 번째는 ~ 요. … 3. 정리 및 마무리 ~ 정리해볼게요. (멘트만하고 화면으로 정리) … 시청해주셔서 감사합니다." ·
#          "한국 시청자 기준이긴 한데 전 세계로 했을 때 큰 문제 없이 넘어갈 수 있도록 해".
#          문장·카드 판정은 tools/srt_tool.py 와 같다(parse_txt·parse_cards·is_label·syllables) — 문장 번호가 오디오·자막과 같음.
"""이야기형 주식 대본 점검 (stock/guides/story_script.md 5번)

  python3 tools/story_check.py stock <영상ID> [--title "<제목>"]      # stock/source/<영상ID>/<영상ID>.txt
  python3 tools/story_check.py --file <대본.txt> [--title "<제목>"]

문제(끝 코드 1): 파트 순서(-도입 → -방법1…N → -정리 → -마무리) · '사연' 라벨 · 도입 추정 30초 넘음 · 첫 문장에 제목 맨 앞 낱말 없음 ·
  방법 파트 첫 문장 '첫 번째는'… 아님 · -정리 끝 문장 '… 정리해볼게요.' 바로 뒤 [장면] 카드 없음 · 카드 문구 49자(공백 제외) 넘음 ·
  마지막 문장이 '시청해주셔서 감사합니다.' 아님 · 쓰지 않는 말(떡상·떡락·가즈아·한강).
  ※ [장면] 카드 문구는 다음 파트 라벨까지 이어진다(srt_tool.parse_txt) → 카드 뒤 다짐·인사는 꼭 새 라벨 -마무리 아래에.
경고: 도입 문장 5~7개·165음절 밖 · 방법 3~5개 밖 · 해요체가 아닌 끝 · 합니다체 많음 · 감탄사 3번 이상 · 60자 넘는 문장 ·
  사다·팔다 꼴 · 카드 줄 수 ≠ 방법 수 · 제목의 금액·%·연도 숫자가 도입에 없음. 개미 낱말(물타기·존버 …)은 처음 나온 문장을 보여 줌 — 뜻을 붙였는지 사람이 봄.
도입 추정 초 = 읽는 음절 ÷ 6.3(진행자 H17 샘플 속도) + 문장 사이 0.45초 — 오디오가 오면 실제 시각으로 다시 본다.
※ 연구·교육용 도구다. 영상 내용은 투자 권유가 아니다.
"""
import argparse
import json
import logging
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import srt_tool  # noqa: E402  (문장·카드·음절 판정을 자막·오디오 도구와 똑같이)

VERSION = "v1.2"
ROOT = Path(__file__).resolve().parents[1]
LOG = logging.getLogger("story_check")

HOST_SYL_PER_SEC = 6.3       # 진행자 H17 샘플 속도 (CLAUDE.md 내레이션 — H04 5.7)
SENT_GAP = 0.45              # 문장 사이 쉼 (tools/tts_narration.py 역할 gap 기본)
INTRO_MAX_SEC = 30.0
INTRO_SYL_MAX = 165
INTRO_SENTS = (5, 7)
METHODS = (3, 5)
CARD_CHARS_MAX = 49          # srt_tool.parse_cards: 글자 ÷ 7 + 1초, 8초에서 잘림 → 49자면 8초
SENT_CHARS_MAX = 60
LAST_SENTENCE = "시청해주셔서 감사합니다."
ORDINALS = ["첫", "두", "세", "네", "다섯"]
POLITE_END = re.compile(r"(요|죠|니다|니까)\s*[.?!…~”\"')]*$")
FORMAL_END = re.compile(r"(습니다|입니다|합니다|됩니다)\s*[.?!]*$")
INTERJ = re.compile(r"(^|\s)(하+|휴+|아+|어휴)\s*…")
BANNED = ["떡상", "떡락", "가즈아", "한강"]
BUY_SELL = re.compile(r"샀|팔았|팔아|사세요|파세요|사야 해|팔아야")
SLANG = ["물타기", "불타기", "몰빵", "존버", "빚투", "반대매매", "리딩방", "테마주", "상폐", "신용"]


def log(stage, level=logging.INFO, **kv):
    LOG.log(level, "[%s] [%s] %s", stage, datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S"),
            " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) and (' ' in v or not v) else v}" for k, v in kv.items()))


def parts_of(path):
    """→ [(라벨, [(문장 번호, 문장), …]), …] — 번호는 srt_tool.parse_txt 순서 (라벨·[장면]·카드 문구 제외)."""
    out, cur, n, in_card = [], None, 0, False
    for raw in Path(path).read_text("utf-8-sig").splitlines():
        line = raw.strip()
        if not line:
            continue
        if srt_tool.is_label(line):
            cur, in_card = (line.lstrip("-").strip(), []), False
            out.append(cur)
            continue
        if line.startswith("[장면]"):
            in_card = True
            continue
        if in_card:
            continue
        n += 1
        if cur is None:
            cur = ("", [])
            out.append(cur)
        cur[1].append((n, line))
    return out


def intro_seconds(sents):
    syl = sum(srt_tool.syllables(s) for _, s in sents)
    return syl, round(syl / HOST_SYL_PER_SEC + SENT_GAP * max(0, len(sents) - 1), 1)


PARTICLES = ("에서는", "으로는", "보다", "까지", "부터", "에서", "으로", "에게", "한테", "처럼", "만큼",
             "은", "는", "이", "가", "을", "를", "에", "의", "도", "만", "로", "와", "과")


def title_head(title):
    """제목 맨 앞 낱말 (쉼표·물음표 등 뗌). 첫 문장에 이 낱말이 그대로 있어야 한다 (story_script.md 2-1 ①)."""
    w = (title or "").strip().split()
    return re.sub(r"[,.?!·…:'\"“”‘’]+$", "", w[0]) if w else ""


def head_in(head, sentence):
    """맨 앞 낱말이 첫 문장에 있나 — 그대로, 또는 끝 조사 하나를 뗀 말(두 글자 이상)로 (v1.1)."""
    if head in sentence:
        return True
    for pt in PARTICLES:
        if head.endswith(pt) and len(head) - len(pt) >= 2 and head[: -len(pt)] in sentence:
            return True
    return False


def check(path, title=None):
    """→ (problems, warnings, info). 사람이 읽는 문장 목록."""
    path = Path(path)
    probs, warns, info = [], [], []
    parts = parts_of(path)
    sents = srt_tool.parse_txt(path)
    cards = srt_tool.parse_cards(path)
    labels = [p[0] for p in parts]
    log("LOAD", file=str(path), sentences=len(sents), parts=len(parts), cards=len(cards), labels="|".join(labels))
    if not sents:
        return ["대본에 문장이 없음"], warns, info

    # ---- 파트 순서
    if any(srt_tool.STORY_WORD in l for l in labels):
        probs.append(f"파트 라벨에 '{srt_tool.STORY_WORD}' — 사연자 목소리 파트로 읽힘 (2번)")
    method_idx = [i for i, l in enumerate(labels) if re.fullmatch(r"방법\s*\d+", l)]
    nums = [int(re.sub(r"\D", "", labels[i])) for i in method_idx]
    order_ok = (labels[:1] == ["도입"] and labels[-2:] == ["정리", "마무리"] and method_idx == list(range(1, len(labels) - 2))
                and nums == list(range(1, len(nums) + 1)))
    if not order_ok:
        probs.append(f"파트 순서가 -도입 → -방법1…N → -정리 → -마무리 가 아님: {labels}")
    n_methods = len(method_idx)
    if not METHODS[0] <= n_methods <= METHODS[1]:
        warns.append(f"방법 {n_methods}개 — 3~5개 (2-2)")
    log("PARTS", order_ok=order_ok, methods=n_methods)

    by_label = {l: s for l, s in parts}

    # ---- 도입
    intro = by_label.get("도입", [])
    if intro:
        syl, sec = intro_seconds(intro)
        log("INTRO", sentences=len(intro), syllables=syl, est_sec=sec, rule=f"<= {INTRO_MAX_SEC}s, syl <= {INTRO_SYL_MAX}")
        if sec > INTRO_MAX_SEC:
            probs.append(f"도입 추정 {sec}초 > {INTRO_MAX_SEC}초 (음절 {syl}, 문장 {len(intro)}) — ① 상황을 줄인다 (2-1)")
        if syl > INTRO_SYL_MAX:
            warns.append(f"도입 {syl}음절 > {INTRO_SYL_MAX}")
        if not INTRO_SENTS[0] <= len(intro) <= INTRO_SENTS[1]:
            warns.append(f"도입 문장 {len(intro)}개 — 5~7개 (2-1)")
        head = title_head(title)
        if not title:
            warns.append("제목을 주지 않아 첫 문장 검사를 건너뜀 (--title)")
        elif not head_in(head, intro[0][1]):
            probs.append(f"첫 문장에 제목 맨 앞 낱말 '{head}' 없음 — 제목을 보고 들어온 사람이 바로 알아보게 (2-1 ①): {intro[0][1]}")
        if title:
            intro_text = " ".join(s for _, s in intro)
            for num in re.findall(r"\d[\d,.]*\s*(?:%|억|만|천|년|배|원)", title):
                num = num.strip().rstrip(",.")
                if num and num not in intro_text:
                    warns.append(f"제목 숫자 '{num}' 가 도입에 없음 (2-1 — 같은 값으로)")
    else:
        probs.append("-도입 파트가 없음")

    # ---- 방법 파트 첫 문장
    for k, i in enumerate(method_idx):
        body = parts[i][1]
        if not body:
            probs.append(f"-{labels[i]} 에 문장이 없음")
            continue
        first = body[0][1]
        want = ORDINALS[k] if k < len(ORDINALS) else None
        ok = bool(want and first.startswith(f"{want} 번째는")) or (k == len(method_idx) - 1 and first.startswith("마지막"))
        if not ok:
            probs.append(f"-{labels[i]} 첫 문장이 '{want} 번째는 ~요.' 꼴이 아님 — 방법을 먼저 (2-2 1): {first}")
        log("METHOD", part=labels[i], sentences=len(body), first=first[:40])

    # ---- 정리 (멘트 한 문장 + 카드) → 마무리
    close = by_label.get("정리", [])
    if close:
        n_ann, last = close[-1]
        if not re.search(r"정리해\s?볼게요[.!]?$", last):
            probs.append(f"-정리 끝 문장이 '… 정리해볼게요.' 가 아님 (2-3 1): {last}")
        if len(close) > 1:
            warns.append(f"-정리 문장 {len(close)}개 — 멘트 한 문장만, 정리는 화면으로 (2-3 1)")
        card = next((c for c in cards if c["after"] == n_ann), None)
        if card is None:
            probs.append(f"'정리해볼게요' (문장 {n_ann}) 바로 뒤에 [장면] 정리 카드가 없음 — 말 없이 화면으로 정리 (2-3 2)")
        else:
            log("CARD", after=n_ann, lines=len(card["lines"]), chars=card["chars"], gap_s=card["seconds"])
            if card["chars"] > CARD_CHARS_MAX:
                probs.append(f"정리 카드 {card['chars']}자 > {CARD_CHARS_MAX}자 (공백 제외 — 쉼이 8초에서 잘림)")
            if n_methods and len(card["lines"]) != n_methods:
                warns.append(f"정리 카드 {len(card['lines'])}줄 ≠ 방법 {n_methods}개 (방법마다 한 줄)")
    else:
        probs.append("-정리 파트가 없음")
    ending = by_label.get("마무리", [])
    if "마무리" in by_label and not 3 <= len(ending) <= 5:
        warns.append(f"-마무리 문장 {len(ending)}개 — 다짐 1~2 + (시리즈) 다음 화 예고 1 + 응원 1 + 끝인사 (2-3 3~5·6번)")
    if "마무리" not in by_label:
        probs.append("-마무리 파트가 없음 — 카드 뒤 문장이 카드 문구로 먹힘 (srt_tool.parse_txt)")
    if sents[-1] != LAST_SENTENCE:
        probs.append(f"마지막 문장이 '{LAST_SENTENCE}' 가 아님: {sents[-1]}")

    # ---- 말투·낱말 (문장 전체)
    formal, interj = [], 0
    for n, s in enumerate(sents, 1):
        if s == LAST_SENTENCE:
            continue
        if FORMAL_END.search(s):
            formal.append(n)
        elif not POLITE_END.search(s):
            warns.append(f"문장 {n} 끝이 해요체가 아님 (1-3): {s}")
        interj += len(INTERJ.findall(s))
        if len(s) > SENT_CHARS_MAX:
            warns.append(f"문장 {n} {len(s)}자 > {SENT_CHARS_MAX} — 둘로 (4-1 번역 1:1): {s[:30]}…")
        for b in BANNED:
            if b in s:
                probs.append(f"문장 {n} 쓰지 않는 말 '{b}' (1-4): {s}")
        if BUY_SELL.search(s):
            warns.append(f"문장 {n} 사다·팔다 꼴 → 매수·매도 (1-4): {s}")
    if len(formal) > 5:
        warns.append(f"합니다체 {len(formal)}문장 (번호 {formal[:10]}…) — 해요체 중심 (1-3)")
    if interj > 2:
        warns.append(f"감탄사 {interj}번 — 영상 하나에 2번 이하 (1-3)")
    for w in SLANG:
        first = next(((n, s) for n, s in enumerate(sents, 1) if w in s), None)
        if first:
            info.append(f"'{w}' 처음 = 문장 {first[0]}: {first[1]} — 그 문장에 뜻을 붙였는지 확인 (1-4)")
    log("TONE", formal=len(formal), interjections=interj, slang_first=len(info))
    return probs, warns, info


def main(argv=None):
    ap = argparse.ArgumentParser(description="이야기형 주식 대본 점검 (stock/guides/story_script.md)")
    ap.add_argument("topic", nargs="?")
    ap.add_argument("video", nargs="?")
    ap.add_argument("--file")
    ap.add_argument("--title")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args(argv)
    logging.basicConfig(level=getattr(logging, a.log_level), format="%(message)s", stream=sys.stderr)
    if a.file:
        path = Path(a.file)
    elif a.topic and a.video:
        path = ROOT / a.topic / "source" / a.video / f"{a.video}.txt"
    else:
        ap.error("<주제> <영상ID> 또는 --file")
    if not path.exists():
        log("LOAD", logging.ERROR, missing=str(path), next="영상ID·경로 확인 (stock/source/<영상ID>/<영상ID>.txt)")
        return 2
    probs, warns, info = check(path, a.title)
    for p in probs:
        print(f"❌ {p}")
    for w in warns:
        print(f"⚠️ {w}")
    for i in info:
        print(f"ℹ️ {i}")
    log("DONE", version=VERSION, problems=len(probs), warnings=len(warns))
    return 1 if probs else 0


if __name__ == "__main__":
    sys.exit(main())
