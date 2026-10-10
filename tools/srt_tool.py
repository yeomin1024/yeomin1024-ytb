#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.3 — 2026-10-10 — 자막 한 줄 규칙(46px 폭 1432px), 긴 문장은 앞줄·뒷줄 자막 2개, 고지 공백을 SRT 안에, 문장 번호 기준 내보내기
#          (v1.2: upload 챕터, v1.1: remotion 내보내기, v1.0: TXT → SRT 생성·검사)
r"""
대본 TXT로 SRT 자막을 만들거나, TXT와 SRT가 지시사항대로 맞는지 검사합니다. (표준 라이브러리만 사용)

  python tools/srt_tool.py check <대본.txt> <자막.srt> [--expect 91/117]       # 문장 / 자막 / SRT–TXT 일치 / 고지 공백
  python tools/srt_tool.py build <대본.txt> <새.srt> [--reuse <기존.srt>]       # 대본으로 SRT 만들기 (타이밍은 추정치)
  python tools/srt_tool.py remotion <대본.txt> <자막.srt> video/src/episodes/<영상ID>/subtitles.ts [--audio-seconds 512.3 --audio-file audio/<영상ID>.mp3]
  python tools/srt_tool.py upload <대본.txt> <자막.srt> --chapters "1=사연;15=왜 물타기를 할까"   # 챕터 시간 (문장 번호 기준)
  python tools/srt_tool.py measure <대본.txt>                                   # 문장별 자막 폭(px)과 나뉠 문장

자막 규칙 (guides/script_guide.md 5-2, guides/video_guide.md 3-3)
  - 번호: 장면·챕터는 대본 문장 번호(TXT에서 라벨·[장면]·카드 문구를 뺀 줄 순서)로 센다. SRT 번호와 다르다.
  - 자막 한 줄: 자막은 늘 한 줄. 문장 폭(46px Noto Sans KR 700)이 1432px 이하면 문장 전체가 자막 1개,
    넘으면 앞줄·뒷줄 자막 2개로 나눠 차례로 보여 준다. (나뉜 문장: 문장 수 < 자막 수)
  - 고지 카드: [장면] 바로 앞 문장 뒤에 최소 3.5초 공백을 SRT 안에 둔다. 영상 코드는 자막을 밀지 않고 그 공백에 카드를 보여 준다.
  - 그 밖에는 자막 사이 빈 시간 없음 (첫 자막 앞 2초 이내 여백은 허용 — 내레이션 시작 전 숨)
  - SRT = 영상 시간: 영상의 자막 시간은 SRT 타임코드 그대로다. 업로드용 SRT를 따로 만들지 않는다.
  - build 의 타이밍은 추정치(읽는 음절 ÷ 5.2 + 0.35초 + 쉼표당 0.2초). 내레이션을 녹음하면 video/ 에서
    npm run align-audio 로 오디오에 맞춘다 (오디오는 고치지 않음).
  - --reuse: 글자가 같은 문장은 기존 SRT의 길이·나눈 위치(앞줄/뒷줄, 또는 옛 두 줄 자막의 줄바꿈)를 그대로 쓴다.
"""
import argparse
import json
import re
import sys
from pathlib import Path

SYL_PER_SEC = 5.2
PAUSE_SEC = 0.35
COMMA_SEC = 0.2
SENT_MAX = 50
SUB_FONT_PX = 46            # 영상 자막 글자 크기 (video_guide 3-3)
LINE_MAX_PX = 1432          # 자막 한 줄 최대 폭 = 띠 최대 1500px − 좌우 안쪽 여백 34px×2
CARD_GAP_MIN = 3.5          # 고지 카드 공백 최소 (초)
LEAD_IN_MAX = 2.0           # 첫 자막 앞 여백 허용 (초)
EPS = 0.0015

_DIG = "영일이삼사오육칠팔구"
_NATIVE = {1: "한", 2: "두", 3: "세", 4: "네", 5: "다섯", 6: "여섯", 7: "일곱", 8: "여덟", 9: "아홉"}
_NATIVE_TENS = {1: "열", 2: "스물", 3: "서른", 4: "마흔", 5: "쉰", 6: "예순", 7: "일흔", 8: "여든", 9: "아흔"}
_NATIVE_COUNTERS = ("살", "시간", "개", "명", "마리", "군데", "곳")
_LETTERS = {"A": "에이", "B": "비", "C": "씨", "D": "디", "E": "이", "F": "에프", "G": "지", "H": "에이치", "I": "아이",
            "J": "제이", "K": "케이", "L": "엘", "M": "엠", "N": "엔", "O": "오", "P": "피", "Q": "큐", "R": "알", "S": "에스",
            "T": "티", "U": "유", "V": "브이", "W": "더블유", "X": "엑스", "Y": "와이", "Z": "지", "&": "앤"}


def sino(n):
    """한자어 수 읽기 (예: 2025 → 이천이십오, 1500 → 천오백). 1은 단위 앞에서 생략."""
    if n == 0:
        return "영"
    out = []
    for unit_val, unit in ((10 ** 12, "조"), (10 ** 8, "억"), (10 ** 4, "만"), (1, "")):
        chunk, n = divmod(n, unit_val)
        if chunk:
            s = ""
            for v, name in ((1000, "천"), (100, "백"), (10, "십"), (1, "")):
                d, chunk = divmod(chunk, v)
                if d:
                    s += ("" if d == 1 and name else _DIG[d]) + name
            out.append(s + unit)
    return "".join(out)


def native(n):
    t, o = divmod(n, 10)
    return (_NATIVE_TENS.get(t, "") + _NATIVE.get(o, "")) or sino(n)


def spoken(text):
    """읽는 소리로 바꾼 문자열 (음절 수 계산용 — 정확한 맞춤법이 목적이 아님)."""
    s = text
    s = re.sub(r"[A-Za-z&]+", lambda m: "".join(_LETTERS.get(c.upper(), "") for c in m.group()), s)
    s = re.sub(r"-(?=\d)", "마이너스", s)
    s = re.sub(r"\+(?=\d)", "플러스", s)

    def num(m):
        whole, frac, after = m.group(1).replace(",", ""), m.group(2), s_after(m)
        n = int(whole)
        if not frac and 0 < n < 100 and after.startswith(_NATIVE_COUNTERS):
            return native(n)
        r = sino(n)
        if frac:
            r += "점" + "".join(_DIG[int(c)] for c in frac[1:])
        return r

    def s_after(m):
        return m.string[m.end():m.end() + 3]
    s = re.sub(r"(\d[\d,]*)(\.\d+)?", num, s)
    s = s.replace("%", "퍼센트").replace("$", "달러")
    return s


def syllables(text):
    return len(re.findall(r"[가-힣]", spoken(text)))


def duration(text):
    return syllables(text) / SYL_PER_SEC + PAUSE_SEC + COMMA_SEC * text.count(",")




# ----------------------------------------------------------------------------- 글자 폭 (자막 폰트)
_WT = json.loads((Path(__file__).with_name("subtitle_widths.json")).read_text("utf-8"))
_W = {int(k): v for k, v in _WT["widths"].items()}


def text_px(text, px=SUB_FONT_PX):
    """자막 폰트(46px Noto Sans KR 700)로 쓴 글자 폭(px). 표: tools/subtitle_widths.json (make_width_table.py)"""
    units = 0
    for ch in text:
        c = ord(ch)
        units += _WT["hangul_syllables"] if 0xAC00 <= c < 0xD7A4 else _W.get(c, _WT["default"])
    return units * px / _WT["units_per_em"]


_CLAUSE_END = re.compile(r"(,|고|서|면|니까|니|며|지만|는데|듯이|자|자마자|해도|어도|아도|려고|도록)$")   # 절 경계
_PARTICLE_END = re.compile(r"(은|는|이|가|을|를|에|에서|으로|로|도|만|까지|와|과)$")                  # 어절 끝 조사
_NO_END_WORDS = {"제", "내", "그", "이", "저", "한", "두", "세", "네", "몇", "새", "왜", "더", "안", "못", "잘", "꼭", "다", "좀", "또"}




def split_px(text):
    """폭 1432px 이하면 [문장]. 넘으면 [앞줄, 뒷줄] — 두 줄 모두 1432px 이하, 쉼표·절 경계·조사 뒤를 우선,
    두 줄 폭 차이를 줄이고, 꾸밈 말로 줄을 끝내거나 의존명사(것·게·때·수) 앞, 숫자와 단위 사이에서 끊지 않는다."""
    if text_px(text) <= LINE_MAX_PX:
        return [text]
    words = text.split(" ")
    best = None
    for i in range(1, len(words)):
        a, b = " ".join(words[:i]), " ".join(words[i:])
        if text_px(a) > LINE_MAX_PX or text_px(b) > LINE_MAX_PX:
            continue
        last = words[i - 1]
        score = abs(text_px(a) - text_px(b)) / 42      # 글자 하나 ≈ 42px
        if last.endswith(","):
            score -= 20
        elif _CLAUSE_END.search(last):
            score -= 12
        elif _PARTICLE_END.search(last):
            score -= 5
        if last in _NO_END_WORDS or re.fullmatch(r"(것|게|때|수|중|등)(이|을|를|은|는|에|도|만|보다|부터|까지|에서|으로|로|이라는|이라|인|이다|입니다)?[,.]?", words[i]):
            score += 100
        if words[i] in {"한", "할", "난", "된", "될", "온", "간", "산", "본", "준", "탄"}:
            score += 30
        if len(last) <= 2 and last.endswith(("은", "운", "던")):
            score += 10
        if re.search(r"[\d천만억]$", last) and re.match(r"^(원|달러|일|월|년|배|명|개|번|살|분|초|주|달|퍼센트|%)", words[i]):
            score += 100
        if re.search(r"\d+(월|년)$", last) and re.match(r"^\d", words[i]):
            score += 100
        if best is None or score < best[0]:
            best = (score, [a, b])
    if best is None:
        raise SystemExit(f"[SRT] ❌ 두 줄로도 1432px을 넘는 문장 → 대본에서 두 문장으로 나누세요: {text}")
    return best[1]


# ----------------------------------------------------------------------------- 대본·SRT 읽기
def parse_txt(path):
    """대본에서 자막이 될 문장만 (라벨·[장면]·카드 문구·빈 줄 제외). 이 순서가 '문장 번호'다."""
    out, in_card = [], False
    for raw in Path(path).read_text("utf-8-sig").splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("-"):
            in_card = False
            continue
        if line.startswith("[장면]"):
            in_card = True
            continue
        if not in_card:
            out.append(line)
    return out


def parse_cards(path):
    """[장면] 카드: 제목(같은 줄 '[장면]' 뒤), 문구(다음 라벨 전까지의 줄), 바로 앞 문장 번호, 추정 길이."""
    cards, n, cur = [], 0, None
    for raw in Path(path).read_text("utf-8-sig").splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("-"):
            cur = None
            continue
        if line.startswith("[장면]"):
            cur = {"after": n, "title": line[len("[장면]"):].strip(), "lines": []}
            cards.append(cur)
            continue
        if cur is not None:
            cur["lines"].append(line)
        else:
            n += 1
    for c in cards:      # build 때 넣는 공백 = 문구 글자 수 ÷ 7 + 1초 (4~8초, 최소 3.5초 규칙보다 김)
        chars = len("".join(c["lines"]).replace(" ", ""))
        c["seconds"] = round(min(8.0, max(4.0, chars / 7 + 1)), 3)
        c["chars"] = chars
    return cards


def _ts(t):
    ms = int(round(t * 1000))
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def _sec(ts):
    h, m, rest = ts.strip().split(":")
    s, ms = rest.split(",")
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000


def parse_srt(path):
    subs = []
    for block in re.split(r"\n\s*\n", Path(path).read_text("utf-8-sig").strip()):
        lines = block.strip().splitlines()
        if len(lines) < 3:
            continue
        a, b = lines[1].split("-->")
        subs.append({"start": _sec(a), "end": _sec(b), "lines": lines[2:], "text": " ".join(x.strip() for x in lines[2:])})
    return subs


def group(subs, sents):
    """SRT 자막들을 대본 문장에 순서대로 묶는다 (앞줄+뒷줄 = 문장). 반환: (문장별 자막 목록, 문제 목록)"""
    out, problems, i = [], [], 0
    for n, sent in enumerate(sents, 1):
        parts, joined = [], ""
        while i < len(subs) and len(joined) < len(sent):
            parts.append(subs[i])
            joined = " ".join(p["text"] for p in parts)
            i += 1
        if joined != sent:
            problems.append(f"문장 {n}: 자막과 대본이 다름 → 대본 '{sent}' / 자막 '{joined}'")
            return out, problems
        out.append({"n": n, "text": sent, "parts": parts, "start": parts[0]["start"], "end": parts[-1]["end"]})
    if i < len(subs):
        problems.append(f"대본에 없는 자막 {len(subs) - i}개가 끝에 남음 (첫 자막: '{subs[i]['text']}')")
    return out, problems


# ----------------------------------------------------------------------------- build
def _split_durs(parts, total):
    syl = [max(1, syllables(p)) + 0.5 * p.count(",") for p in parts]
    return [total * s / sum(syl) for s in syl]


def build(txt, out, reuse=None):
    sents, cards = parse_txt(txt), parse_cards(txt)
    gap_after = {c["after"]: c["seconds"] for c in cards}
    one, pair = {}, {}
    if reuse:
        old = parse_srt(reuse)
        for k, s in enumerate(old):
            one.setdefault(s["text"], s)
            if k + 1 < len(old):
                pair.setdefault(s["text"] + " " + old[k + 1]["text"], (s, old[k + 1]))
    t, blocks, new_n, split_n = 0.0, [], 0, 0
    for n, sent in enumerate(sents, 1):
        if sent in pair and text_px(sent) > LINE_MAX_PX:            # 새 형식 기존 SRT: 앞줄·뒷줄 그대로
            a, b = pair[sent]
            parts, durs = [a["text"], b["text"]], [a["end"] - a["start"], b["end"] - b["start"]]
        elif sent in one:                                             # 글자가 같은 문장: 기존 길이·줄바꿈
            o = one[sent]
            total = o["end"] - o["start"]
            if text_px(sent) <= LINE_MAX_PX:
                parts = [sent]
            elif len(o["lines"]) == 2 and all(text_px(x) <= LINE_MAX_PX for x in o["lines"]):
                parts = [x.strip() for x in o["lines"]]               # 옛 두 줄 자막의 줄바꿈 = 앞줄/뒷줄
            else:
                parts = split_px(sent)
            durs = _split_durs(parts, total)
        else:
            parts = split_px(sent)
            durs = _split_durs(parts, duration(sent))
            new_n += 1
        split_n += len(parts) > 1
        for p, d in zip(parts, durs):
            blocks.append((t, t + d, p))
            t += d
        if n in gap_after:
            t += gap_after[n]
    Path(out).write_text("\n\n".join(f"{i}\n{_ts(a)} --> {_ts(b)}\n{p}" for i, (a, b, p) in enumerate(blocks, 1)) + "\n", "utf-8")
    print(f"[SRT] 저장 {out}: 문장 {len(sents)} / 자막 {len(blocks)} (나뉜 문장 {split_n}개, 새로 계산 {new_n}개), "
          + ", ".join(f"고지 공백 문장 {c['after']} 뒤 {c['seconds']}초" for c in cards) + f", 길이 {_ts(t)}")


# ----------------------------------------------------------------------------- check
def check(txt, srt, expect=None):
    sents, subs, cards = parse_txt(txt), parse_srt(srt), parse_cards(txt)
    problems, warnings = [], []
    for n, a in enumerate(sents, 1):
        if len(a) > SENT_MAX:     # 대본 쓸 때의 규칙(script_guide 0번). 자막 기준은 아래 1432px이라 경고만
            warnings.append(f"문장 {n}: {len(a)}자 (새 대본은 50자 넘으면 두 문장으로 — 자막은 앞줄·뒷줄 폭으로 판정)")
    groups, gp = group(subs, sents)
    problems += gp
    for k, s in enumerate(subs, 1):
        if len(s["lines"]) != 1:
            problems.append(f"자막 {k}: {len(s['lines'])}줄 (자막은 한 줄 — 넘치면 앞줄·뒷줄 자막 2개로)")
        if text_px(s["text"]) > LINE_MAX_PX + 0.5:
            problems.append(f"자막 {k}: 폭 {text_px(s['text']):.0f}px > {LINE_MAX_PX}px")
        if s["end"] <= s["start"]:
            problems.append(f"자막 {k}: 길이 0 이하")
    split_n = 0
    for g in groups:
        if len(g["parts"]) > 1:
            split_n += 1
            if text_px(g["text"]) <= LINE_MAX_PX:
                problems.append(f"문장 {g['n']}: 폭 {text_px(g['text']):.0f}px ≤ {LINE_MAX_PX}px인데 나뉨 → 한 줄로 합치기")
            if len(g["parts"]) > 2:
                problems.append(f"문장 {g['n']}: 자막 {len(g['parts'])}개로 나뉨 (앞줄·뒷줄 2개까지)")
    card_after = {c["after"]: c for c in cards}
    gaps = []
    if subs and subs[0]["start"] > LEAD_IN_MAX + EPS:
        problems.append(f"첫 자막 앞 여백 {subs[0]['start']:.2f}초 (> {LEAD_IN_MAX}초)")
    for k in range(1, len(subs)):
        gap = subs[k]["start"] - subs[k - 1]["end"]
        if gap < -EPS:
            problems.append(f"자막 {k}–{k + 1}: 겹침 {gap:.3f}초")
        elif gap > EPS:
            gaps.append((k, gap))
    sent_end_idx = {}
    idx = 0
    for g in groups:
        idx += len(g["parts"])
        sent_end_idx[g["n"]] = idx            # 이 문장의 마지막 자막 번호(1부터)
    card_gap_info = []
    for n, c in card_after.items():
        k = sent_end_idx.get(n)
        gap = next((gp_ for kk, gp_ in gaps if kk == k), 0.0) if k else 0.0
        card_gap_info.append((n, gap))
        if gap < CARD_GAP_MIN:
            problems.append(f"고지 공백: 문장 {n} 뒤 {gap:.2f}초 (최소 {CARD_GAP_MIN}초를 SRT 안에)")
    card_ks = {sent_end_idx.get(n) for n in card_after}
    for k, gap in gaps:
        if k not in card_ks:
            problems.append(f"자막 {k}–{k + 1}: 빈 시간 {gap:.3f}초 (고지 카드 자리 말고는 이어 붙임)")
    if expect:
        en, es = expect
        if len(sents) != en:
            problems.append(f"문장 수 {len(sents)} ≠ 기대값 {en}")
        if len(subs) != es:
            problems.append(f"자막 수 {len(subs)} ≠ 기대값 {es}")
    match = not gp
    total = subs[-1]["end"] if subs else 0
    print(f"[SRT] 문장 {len(sents)} / 자막 {len(subs)} (나뉜 문장 {split_n}개) / SRT–TXT {'일치 ✅' if match else '불일치 ❌'} / "
          + (" · ".join(f"고지 공백 문장 {n} 뒤 {g:.1f}초 {'✅' if g >= CARD_GAP_MIN else '❌'}" for n, g in card_gap_info) or "고지 카드 없음")
          + f" / 끝 {_ts(total)}")
    for w in warnings:
        print("  ⚠️", w)
    for p in problems:
        print("  ❌", p)
    print("[SRT] ✅ 이상 없음" if not problems else f"[SRT] 문제 {len(problems)}개")
    return 0 if not problems else 1


def measure(txt):
    sents = parse_txt(txt)
    split = 0
    for n, s in enumerate(sents, 1):
        parts = split_px(s)
        split += len(parts) > 1
        print(f"{n:3d} {text_px(s):6.0f}px {'→ ' + ' / '.join(parts) if len(parts) > 1 else s}")
    print(f"[SRT] 문장 {len(sents)} → 자막 {len(sents) + split} (나뉠 문장 {split}개, 기준 {LINE_MAX_PX}px)")


# ----------------------------------------------------------------------------- 영상용 내보내기
def export_remotion(txt, srt, out, audio_seconds=None, audio_file=None):
    sents, subs, cards = parse_txt(txt), parse_srt(srt), parse_cards(txt)
    groups, problems = group(subs, sents)
    if problems:
        raise SystemExit("[SRT] ❌ 대본과 자막이 다릅니다 → 먼저 check 로 확인\n  " + "\n  ".join(problems))
    by_n = {g["n"]: g for g in groups}
    card_rows = []
    for c in cards:
        a, b = by_n[c["after"]]["end"], by_n[c["after"] + 1]["start"]
        if b - a < CARD_GAP_MIN:
            raise SystemExit(f"[SRT] ❌ 고지 공백: 문장 {c['after']} 뒤 {b - a:.2f}초 (최소 {CARD_GAP_MIN}초) → SRT를 고치세요 (영상 코드는 자막을 밀지 않음)")
        card_rows.append({"afterSentence": c["after"], "title": c["title"], "lines": c["lines"], "start": round(a, 3), "end": round(b, 3)})
    last = groups[-1]["end"]
    total = max(last + 1.0, float(audio_seconds or 0))          # 영상 길이는 오디오보다 짧게 자르지 않는다
    data = {
        "sentences": [{"n": g["n"], "start": round(g["start"], 3), "end": round(g["end"], 3),
                       "parts": [{"start": round(p["start"], 3), "end": round(p["end"], 3), "text": p["text"]} for p in g["parts"]]}
                      for g in groups],
        "cards": card_rows,
        "audio": {"file": audio_file, "seconds": round(float(audio_seconds), 3)} if audio_file else None,
        "totalSeconds": round(total, 3),
    }
    body = ("// 자동 생성 — python tools/srt_tool.py remotion (직접 고치지 말고 대본·SRT를 고친 뒤 다시 생성)\n"
            "// 타이밍은 SRT 그대로(초) = 영상 시간. 번호는 대본 문장 번호. 고지 카드는 SRT 공백 자리 (코드에서 밀지 않음)\n"
            f"export const SRC = {json.dumps(data, ensure_ascii=False, indent=1)} as const;\n")
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    Path(out).write_text(body, "utf-8")
    print(f"[SRT] 영상용 저장 {out}: 문장 {len(groups)} / 자막 {len(subs)}, 고지 카드 {len(cards)}개 "
          + ", ".join(f"(문장 {c['afterSentence']} 뒤 {c['end'] - c['start']:.1f}초)" for c in card_rows)
          + f", 오디오 {audio_seconds or '없음'}, 영상 길이 {_ts(total)}")


# ----------------------------------------------------------------------------- 업로드 챕터
def _mmss(t):
    t = int(t)  # 챕터 시간은 내림 (자막보다 늦게 시작하지 않게)
    return f"{t // 3600}:{t % 3600 // 60:02d}:{t % 60:02d}" if t >= 3600 else f"{t // 60}:{t % 60:02d}"


def chapters(txt, srt, spec):
    """SRT = 영상 시간이므로 SRT 그대로 업로드하고, 챕터 시간만 문장 번호로 계산한다."""
    sents, subs = parse_txt(txt), parse_srt(srt)
    groups, problems = group(subs, sents)
    if problems:
        raise SystemExit("[SRT] ❌ 대본과 자막이 다릅니다 → 먼저 check 로 확인\n  " + "\n  ".join(problems))
    by_n = {g["n"]: g for g in groups}
    total = groups[-1]["end"] + 1.0
    rows = []
    for part in [p for p in spec.split(";") if p.strip()]:
        n, title = part.split("=", 1)
        g = by_n.get(int(n))
        if g is None:
            raise SystemExit(f"[CHAPTER] ❌ 문장 {n} 없음")
        rows.append((0.0 if int(n) == 1 else g["start"], int(n), title.strip()))
    problems = []
    if rows[0][1] != 1:
        problems.append("첫 챕터는 문장 1(0:00)이어야 함")
    if len(rows) < 3:
        problems.append("챕터는 3개 이상이어야 함")
    for (t0, _, a), (t1, _, b) in zip(rows, rows[1:] + [(total, None, "끝")]):
        if int(t1) - int(t0) < 10:
            problems.append(f"'{a}' 챕터가 10초 미만 ({int(t1) - int(t0)}초)")
        if t1 < t0:
            problems.append(f"'{b}' 시간이 앞 챕터보다 빠름")
    print("[CHAPTER] 설명란에 붙여 넣기 (자막은 이 SRT를 그대로 업로드):")
    for t, n, title in rows:
        print(f"{_mmss(t)} {title}")
    for p in problems:
        print("  ❌", p)
    print("[CHAPTER] ✅ YouTube 챕터 규칙 통과" if not problems else f"[CHAPTER] 문제 {len(problems)}개")
    return 0 if not problems else 1


def main(argv=None):
    ap = argparse.ArgumentParser(description="대본 TXT → SRT 자막 생성·검사 (자막 한 줄 1432px, 고지 공백 SRT 안)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build", help="TXT로 SRT 만들기")
    b.add_argument("txt")
    b.add_argument("out")
    b.add_argument("--reuse", help="기존 SRT (글자가 같은 문장은 길이·나눈 위치를 그대로 사용)")
    c = sub.add_parser("check", help="문장 / 자막 / SRT–TXT 일치 / 고지 공백 검사")
    c.add_argument("txt")
    c.add_argument("srt")
    c.add_argument("--expect", help="기대값 '문장수/자막수' (예: 91/117)")
    r = sub.add_parser("remotion", help="영상용 데이터(subtitles.ts) 내보내기")
    r.add_argument("txt")
    r.add_argument("srt")
    r.add_argument("out")
    r.add_argument("--audio-seconds", type=float, help="내레이션 길이(초) — 영상 길이를 이보다 짧게 하지 않음")
    r.add_argument("--audio-file", help="video/public 기준 내레이션 경로 (예: audio/multagi-2026-10.mp3)")
    u = sub.add_parser("upload", help="챕터 시간 계산 (SRT는 그대로 업로드)")
    u.add_argument("txt")
    u.add_argument("srt")
    u.add_argument("--chapters", required=True, help='"문장번호=제목;문장번호=제목" (첫 항목은 1=...)')
    m = sub.add_parser("measure", help="문장별 자막 폭과 나뉠 위치")
    m.add_argument("txt")
    a = ap.parse_args(argv)
    if a.cmd == "build":
        build(a.txt, a.out, a.reuse)
        return 0
    if a.cmd == "remotion":
        export_remotion(a.txt, a.srt, a.out, a.audio_seconds, a.audio_file)
        return 0
    if a.cmd == "upload":
        return chapters(a.txt, a.srt, a.chapters)
    if a.cmd == "measure":
        measure(a.txt)
        return 0
    exp = tuple(int(x) for x in a.expect.split("/")) if a.expect else None
    return check(a.txt, a.srt, exp)


if __name__ == "__main__":
    sys.exit(main())
