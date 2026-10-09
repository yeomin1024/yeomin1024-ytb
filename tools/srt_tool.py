#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.2 — 2026-10-09 — upload 명령 추가: 고지 카드만큼 민 업로드용 SRT + 자막 번호로 YouTube 챕터 시간 계산 (v1.1: remotion 내보내기, v1.0: TXT → SRT 생성·검사)
r"""
대본 TXT로 SRT 자막을 만들거나, TXT와 SRT가 지시사항대로 맞는지 검사합니다. (표준 라이브러리만 사용)

  python tools/srt_tool.py check stock/source/multagi-2026-10/multagi-2026-10.txt stock/source/multagi-2026-10/multagi-2026-10.srt
  python tools/srt_tool.py build <대본.txt> <새.srt> --reuse <기존.srt>
  python tools/srt_tool.py remotion <대본.txt> <자막.srt> video/src/episodes/<영상ID>/subtitles.ts   # 영상 지시사항 6-3
  python tools/srt_tool.py upload <대본.txt> <자막.srt> <업로드용.srt> --chapters "1=사연;15=왜 물타기를 할까"   # 업로드 지시사항

build 규칙 (guides/script_guide.md 5-2)
  - 자막 1개 = 대본 1문장(한 줄). 파트 라벨(-사연 파트 등), [장면] 줄과 그 뒤 카드 문구(다음 라벨 전까지)는 뺌
  - --reuse 로 기존 SRT를 주면, 글자가 똑같은 문장은 기존 줄바꿈·길이를 그대로 씀 (사람이 다듬은 것 보존)
  - 새 문장 길이 = 읽는 음절 수 ÷ 5.2 + 0.35초 + 쉼표당 0.2초 (숫자·영문은 읽는 소리로 셈: 8천만=팔천만, S&P=에스앤피)
  - 22자(공백 포함) 이하는 1줄, 넘으면 쉼표·절 경계(~고, ~서, ~면, ~니까, ~며, ~지만, ~는데)를 우선해 2줄
  - 자막 사이 빈 시간 없음, 0초부터 시작
check: 문장 수·순서 일치, 50자 초과 문장, 줄 수 규칙, 빈 시간, 총 길이를 출력하고 문제가 있으면 종료 코드 1
upload: 영상에는 고지 카드가 끼어 있어 카드 뒤 자막이 카드 길이만큼 늦게 나온다. 그만큼 민 SRT를 저장하고,
        --chapters 의 "자막번호=챕터 제목"을 영상 시간(M:SS, 내림)으로 바꿔 출력한다.
        YouTube 챕터 규칙 검사: 첫 챕터 0:00, 3개 이상, 각 10초 이상, 시간 순서
"""
import argparse
import re
import sys
from pathlib import Path

SYL_PER_SEC = 5.2
PAUSE_SEC = 0.35
COMMA_SEC = 0.2
LINE_MAX = 22
SENT_MAX = 50

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


_CLAUSE_END = re.compile(r"(,|고|서|면|니까|니|며|지만|는데|듯이|자|자마자|해도|어도|아도|려고|도록)$")   # 절 경계
_PARTICLE_END = re.compile(r"(은|는|이|가|을|를|에|에서|으로|로|도|만|까지|와|과)$")                  # 어절 끝 조사
_NO_END_WORDS = {"제", "내", "그", "이", "저", "한", "두", "세", "네", "몇", "새", "왜", "더", "안", "못", "잘", "꼭", "다", "좀", "또"}


def wrap(text):
    """22자 이하는 1줄. 넘으면 두 줄 — 절 경계·조사 뒤를 우선하고, 두 줄 길이 차이를 줄이고,
    '제·왜·그' 같은 꾸밈 말로 줄을 끝내거나 의존명사(것·게·때·수) 앞에서 끊지 않는다."""
    if len(text) <= LINE_MAX:
        return [text]
    words = text.split(" ")
    best = None
    for i in range(1, len(words)):
        a, b = " ".join(words[:i]), " ".join(words[i:])
        last = words[i - 1]
        score = abs(len(a) - len(b))
        if last.endswith(","):
            score -= 20             # 쉼표 뒤가 1순위
        elif _CLAUSE_END.search(last):
            score -= 12
        elif _PARTICLE_END.search(last):
            score -= 5
        if last in _NO_END_WORDS or re.fullmatch(r"(것|게|때|수|중|등)(이|을|를|은|는|에|도|만|보다|부터|까지|에서|으로|로|이라는|이라|인|이다|입니다)?[,.]?", words[i]):
            score += 100            # 의존명사(것·게·때·수) 앞에서 끊지 않음
        if words[i] in {"한", "할", "난", "된", "될", "온", "간", "산", "본", "준", "탄"}:
            score += 30             # '물타기를 / 한 5월'처럼 꾸밈말이 다음 줄 맨 앞에 오는 것 피함
        if len(last) <= 2 and last.endswith(("은", "운", "던")):
            score += 10             # '많은 / 분들이'처럼 짧은 꾸밈말 뒤는 피함
        if re.search(r"[\d천만억]$", last) and re.match(r"^(원|달러|일|월|년|배|명|개|번|살|분|초|주|달|퍼센트|%)", words[i]):
            score += 100            # 숫자와 단위는 한 줄에 (예: 5천만 / 원 X)
        if re.search(r"\d+(월|년)$", last) and re.match(r"^\d", words[i]):
            score += 100            # 날짜는 한 줄에 (예: 5월 / 9일 X)
        if best is None or score < best[0]:
            best = (score, [a, b])
    return best[1]


def parse_txt(path):
    """대본에서 자막이 될 문장만 (라벨·[장면]·카드 문구·빈 줄 제외)."""
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


def build(txt, out, reuse=None):
    sents = parse_txt(txt)
    old = {s["text"]: s for s in parse_srt(reuse)} if reuse else {}
    t, blocks, new_n = 0.0, [], 0
    for i, sent in enumerate(sents, 1):
        if sent in old:
            o = old[sent]
            lines, dur = o["lines"], o["end"] - o["start"]
        else:
            lines, dur = wrap(sent), duration(sent)
            new_n += 1
        blocks.append(f"{i}\n{_ts(t)} --> {_ts(t + dur)}\n" + "\n".join(lines))
        t += dur
    Path(out).write_text("\n\n".join(blocks) + "\n", "utf-8")
    print(f"[SRT] 저장 {out}: 자막 {len(sents)}개 (새로 계산 {new_n}개, 기존 재사용 {len(sents) - new_n}개), 길이 {_ts(t)}")


def check(txt, srt):
    sents, subs, problems = parse_txt(txt), parse_srt(srt), []
    if len(sents) != len(subs):
        problems.append(f"문장 수 {len(sents)} ≠ 자막 수 {len(subs)}")
    for i, (a, s) in enumerate(zip(sents, subs), 1):
        if a != s["text"]:
            problems.append(f"자막 {i}: 대본과 다름 → 대본 '{a}' / 자막 '{s['text']}'")
    for i, a in enumerate(sents, 1):
        if len(a) > SENT_MAX:
            problems.append(f"문장 {i}: {len(a)}자 (50자 넘음 → 두 문장으로)")
    prev = 0.0
    for i, s in enumerate(subs, 1):
        want = 1 if len(s["text"]) <= LINE_MAX else 2
        if len(s["lines"]) != want:
            problems.append(f"자막 {i}: {len(s['text'])}자인데 {len(s['lines'])}줄 (규칙: {want}줄)")
        if abs(s["start"] - prev) > 0.0015:
            problems.append(f"자막 {i}: 앞 자막과 빈 시간/겹침 {s['start'] - prev:+.3f}초")
        if s["end"] <= s["start"]:
            problems.append(f"자막 {i}: 길이 0 이하")
        prev = s["end"]
    total_syl = sum(syllables(a) for a in sents)
    print(f"[SRT] 자막 {len(subs)}개 · 길이 {_ts(prev)} (고지 카드 제외) · 읽는 음절 약 {total_syl} "
          f"(= {total_syl / SYL_PER_SEC / 60:.1f}분 @{SYL_PER_SEC}음절/초)")
    for p in problems:
        print("  ❌", p)
    print("[SRT] ✅ 이상 없음" if not problems else f"[SRT] 문제 {len(problems)}개")
    return 0 if not problems else 1


def parse_cards(path):
    """[장면] 카드: 제목(같은 줄 '[장면]' 뒤), 문구(다음 라벨 전까지의 줄), 바로 앞 자막 문장 번호."""
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
    for c in cards:      # 카드 길이 = 문구 글자 수 ÷ 7 + 1초 (최소 4, 최대 8) — guides/video_guide.md 2번
        chars = len("".join(c["lines"]).replace(" ", ""))
        c["seconds"] = round(min(8.0, max(4.0, chars / 7 + 1)), 3)
        c["chars"] = chars
    return cards


def export_remotion(txt, srt, out):
    import json
    subs, cards = parse_srt(srt), parse_cards(txt)
    if [s["text"] for s in subs] != parse_txt(txt):
        raise SystemExit("[SRT] ❌ 대본과 자막이 다릅니다 → 먼저 check 로 확인")
    total = subs[-1]["end"] + sum(c["seconds"] for c in cards) + 1.0
    data = {
        "subtitles": [{"n": i, "start": round(s["start"], 3), "end": round(s["end"], 3), "lines": s["lines"]}
                      for i, s in enumerate(subs, 1)],
        "cards": [{"afterSub": c["after"], "title": c["title"], "lines": c["lines"], "seconds": c["seconds"]} for c in cards],
        "totalSeconds": round(total, 3),
    }
    body = ("// 자동 생성 — python tools/srt_tool.py remotion (직접 고치지 말고 대본·SRT를 고친 뒤 다시 생성)\n"
            "// 타이밍은 SRT 기준(초). 고지 카드 뒤 자막은 카드 길이만큼 뒤로 밀림 (timeline.ts)\n"
            f"export const SRC = {json.dumps(data, ensure_ascii=False, indent=1)} as const;\n")
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    Path(out).write_text(body, "utf-8")
    print(f"[SRT] 영상용 저장 {out}: 자막 {len(subs)}개, 고지 카드 {len(cards)}개 "
          + ", ".join(f"(자막 {c['after']} 뒤, {c['chars']}자 → {c['seconds']}초)" for c in cards)
          + f", 전체 길이 {_ts(total)} (마지막 자막 끝 + 카드 + 여유 1초)")


def video_times(txt, srt):
    """영상 시간축: 카드 뒤 자막을 카드 길이만큼 민 (start, end) 목록과 전체 길이 (export_remotion·timeline.ts와 같은 계산)"""
    subs, cards = parse_srt(srt), parse_cards(txt)
    if [s["text"] for s in subs] != parse_txt(txt):
        raise SystemExit("[SRT] ❌ 대본과 자막이 다릅니다 → 먼저 check 로 확인")
    shift, out = 0.0, []
    for i, s in enumerate(subs, 1):
        out.append({**s, "n": i, "vstart": s["start"] + shift, "vend": s["end"] + shift})
        shift += sum(c["seconds"] for c in cards if c["after"] == i)
    total = subs[-1]["end"] + sum(c["seconds"] for c in cards) + 1.0
    return out, cards, total


def _mmss(t):
    t = int(t)  # 챕터 시간은 내림 (자막보다 늦게 시작하지 않게)
    return f"{t // 3600}:{t % 3600 // 60:02d}:{t % 60:02d}" if t >= 3600 else f"{t // 60}:{t % 60:02d}"


def export_upload(txt, srt, out, chapters=None):
    subs, cards, total = video_times(txt, srt)
    blocks = [f"{s['n']}\n{_ts(s['vstart'])} --> {_ts(s['vend'])}\n" + "\n".join(s["lines"]) for s in subs]
    Path(out).write_text("\n\n".join(blocks) + "\n", "utf-8")
    print(f"[SRT] 업로드용 저장 {out}: 자막 {len(subs)}개, 고지 카드 {len(cards)}개만큼 밀림 "
          + ", ".join(f"(자막 {c['after']} 뒤 +{c['seconds']}초)" for c in cards) + f", 영상 길이 {_ts(total)}")
    if not chapters:
        return 0
    by_n = {s["n"]: s for s in subs}
    rows = []
    for part in [p for p in chapters.split(";") if p.strip()]:
        n, title = part.split("=", 1)
        s = by_n.get(int(n))
        if s is None:
            raise SystemExit(f"[CHAPTER] ❌ 자막 {n} 없음")
        rows.append((0.0 if int(n) == 1 else s["vstart"], int(n), title.strip()))
    problems = []
    if rows[0][0] != 0.0:
        problems.append("첫 챕터는 자막 1(0:00)이어야 함")
    if len(rows) < 3:
        problems.append("챕터는 3개 이상이어야 함")
    for (t0, n0, a), (t1, n1, b) in zip(rows, rows[1:] + [(total, None, "끝")]):
        if int(t1) - int(t0) < 10:
            problems.append(f"'{a}' 챕터가 10초 미만 ({int(t1) - int(t0)}초)")
        if t1 < t0:
            problems.append(f"'{b}' 시간이 앞 챕터보다 빠름")
    print("[CHAPTER] 설명란에 붙여 넣기:")
    for t, n, title in rows:
        print(f"{_mmss(t)} {title}")
    for p in problems:
        print("  ❌", p)
    print("[CHAPTER] ✅ YouTube 챕터 규칙 통과" if not problems else f"[CHAPTER] 문제 {len(problems)}개")
    return 0 if not problems else 1


def main(argv=None):
    ap = argparse.ArgumentParser(description="대본 TXT → SRT 자막 생성·검사")
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build", help="TXT로 SRT 만들기")
    b.add_argument("txt")
    b.add_argument("out")
    b.add_argument("--reuse", help="기존 SRT (글자가 같은 문장은 줄바꿈·길이를 그대로 사용)")
    c = sub.add_parser("check", help="TXT와 SRT가 규칙대로 맞는지 검사")
    c.add_argument("txt")
    c.add_argument("srt")
    r = sub.add_parser("remotion", help="영상용 자막·고지 카드 데이터(subtitles.ts) 내보내기")
    r.add_argument("txt")
    r.add_argument("srt")
    r.add_argument("out")
    u = sub.add_parser("upload", help="업로드용 SRT(고지 카드만큼 밈) 저장 + 챕터 시간 계산")
    u.add_argument("txt")
    u.add_argument("srt")
    u.add_argument("out")
    u.add_argument("--chapters", help='"자막번호=제목;자막번호=제목" (첫 항목은 1=...)')
    a = ap.parse_args(argv)
    if a.cmd == "upload":
        return export_upload(a.txt, a.srt, a.out, a.chapters)
    if a.cmd == "remotion":
        export_remotion(a.txt, a.srt, a.out)
        return 0
    if a.cmd == "build":
        build(a.txt, a.out, a.reuse)
        return 0
    return check(a.txt, a.srt)


if __name__ == "__main__":
    sys.exit(main())
