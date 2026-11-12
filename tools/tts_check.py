#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-11-12 — 새로: 대본을 TTS(Qwen3-TTS)에 넣기 전 '이상하게 읽힐 꼴' 검사 + 숫자 읽는 소리 사전 줄 만들기
#   사용자 지시 2026-11-12 "오디오가 이상하게 생성되지 않도록 최대한 모델에게 익숙한 형식으로 생성, 특히 숫자 주의".
#   근거 = guides/tts_guide.md 5-1(알파벳+쉼표·해라체·서수 쉼표·분수) · 5-2(55음절 넘는 문장·짧은 문장) · 주식 편 사전(tts_lexicon.tsv — 소수는 모두 사전에 읽는 소리로).
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.0 | 2026-11-12 | 최초 | sino·reading·check_line·check_script·write_lexicon·selftest |
#
# 읽는 것: 대본 .txt (tools/srt_tool.py 와 같은 규칙 — '-' 로 시작하는 줄 = 장 이름, [장면] 뒤 카드 문구는 읽지 않음)
#         사전: <주제>/tts_lexicon.tsv · <대본 폴더>/tts_lexicon.tsv (쇼츠 폴더면 롱폼 폴더 것도) — tts_narration.py 와 같은 순서·같은 '긴 것부터 바꿈'.
# 검사 (사전을 먼저 적용한 뒤 남은 꼴만):
#   ❌ 소수(42.5%·1.5배·3.7년) · 천 단위 쉼표 숫자(5,239) · 숫자 범위 물결(3~5) · 기호(/ × ± → ≈ ≥ ≤ = < >) · 문장 머리 알파벳+쉼표(A, …) · 숫자 분수(4분의 1)
#   ⚠ 사전에 없는 영어 낱말 · 55음절 넘는 문장 · 6음절 안 문장 · 해라체 끝(…했다.) · 서수 쉼표 나열(일곱, 여덟 번째) · 괄호 · 단위 없는 큰 숫자(25000)
# 쓰기:
#   python3 tools/tts_check.py <대본.txt> [--topic <주제>] [--write-lexicon] [--out <md>]
#     --write-lexicon = 소수·분수·쉼표 숫자의 읽는 소리 줄을 <대본 폴더>/tts_lexicon.tsv 끝에 더함 (있는 줄은 그대로) → 다시 검사
#   python3 tools/tts_check.py --selftest
# 끝 코드: ❌ 가 있으면 1. ※ 연구·교육용 — 투자 권유 아님.
from __future__ import annotations

import argparse
import json
import logging
import re
import sys
import tempfile
import time
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = "v1.0"
LOG = logging.getLogger("tts_check")
LONG_SYL, SHORT_SYL = 55, 6
DIG = "영일이삼사오육칠팔구"
UNIT_WORD = {"%p": "퍼센트포인트", "%": "퍼센트", "배": "배", "년": "년", "개월": "개월", "달": "달", "원": "원", "일": "일", "시간": "시간",
             "분": "분", "초": "초", "명": "명", "번": "번", "점": "점", "주": "주", "살": "살", "세": "세", "호": "호", "km": "킬로미터", "kg": "킬로그램"}
UNIT_RX = "|".join(sorted(map(re.escape, UNIT_WORD), key=len, reverse=True))
DECIMAL = re.compile(rf"(?<![\d.])(\d+\.\d+)\s?({UNIT_RX})?")
COMMA_NUM = re.compile(rf"(?<![\d,])(\d{{1,3}}(?:,\d{{3}})+)(?![\d,])\s?({UNIT_RX})?")
RANGE = re.compile(r"\d\s*[~∼〜]\s*\d")
SYMBOL = re.compile(r"[/×±→≈≥≤=<>]")
LETTER_COMMA = re.compile(r"(?:^|[\s\"'“‘(])[A-Za-z],")
FRACTION = re.compile(r"(\d+)\s?분의\s?(\d+)")
ENGLISH = re.compile(r"[A-Za-z][A-Za-z&.+\-]*")
BIG_INT = re.compile(r"(?<![\d,.])(\d{5,})(?![\d,.])")
ORD_COMMA = re.compile(r"(첫|두|세|네|다섯|여섯|일곱|여덟|아홉|열)(?: 번째)?, ?(두|세|네|다섯|여섯|일곱|여덟|아홉|열) 번째")
HAERA = re.compile(r"(?<!니)(?<!습)다[.!]?$")
SYL = re.compile(r"[가-힣0-9]")


def log(stage: str, level: int = logging.INFO, **kv) -> None:
    ts = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    LOG.log(level, f"[{stage}] [{ts}] " + " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) else v}" for k, v in kv.items()))


# ------------------------------------------------------------------ 읽는 소리 (한자어 수)
def sino(n: int) -> str:
    """정수 → 한자어 읽기 (일십·일백·일천·일만의 '일'은 뺌 — 사전 꼴 '십오', '백삼십칠', '만')."""
    if n == 0:
        return "영"
    out, big = [], ["", "만", "억", "조", "경"]
    k = 0
    while n > 0:
        n, chunk = divmod(n, 10000)
        if chunk:
            s = ""
            for i, u in ((3, "천"), (2, "백"), (1, "십"), (0, "")):
                d = (chunk // 10 ** i) % 10
                if d:
                    s += ("" if d == 1 and u else DIG[d]) + u
            if k == 1 and s == "일":
                s = ""                                    # 10000 → '만' (일만 ✗)
            out.append(s + big[k])
        k += 1
    return " ".join(reversed(out)).replace("  ", " ").strip()


def reading(num: str, unit: str | None = None) -> str:
    """'42.5' '%' → '사십이 점 오 퍼센트' · '5,239' → '오천이백삼십구' · 소수 자리는 한 자씩 (0 → 영)."""
    num = num.replace(",", "")
    if "." in num:
        a, b = num.split(".", 1)
        s = f"{sino(int(a))} 점 " + " ".join(DIG[int(c)] for c in b)
    else:
        s = sino(int(num))
    return s + (f" {UNIT_WORD[unit]}" if unit else "")


# ------------------------------------------------------------------ 대본·사전
def is_label(line: str) -> bool:
    return line.startswith("-") and not re.match(r"^-\s?\d", line)      # '-800만' 같은 음수 문장은 장 이름이 아님


def read_lines(path: Path) -> list[tuple[int, str]]:
    """(문장 번호, 문장) — srt_tool.parse_txt 와 같은 판정이면 그것을 씀 (가능하면 같은 함수)."""
    try:
        sys.path.insert(0, str(ROOT / "tools"))
        import srt_tool  # noqa: E402
        return list(enumerate(srt_tool.parse_txt(str(path)), 1))
    except Exception as e:  # noqa: BLE001 — srt_tool 을 못 쓰면 같은 규칙의 작은 판정으로
        log("INPUT", logging.WARNING, note="srt_tool.parse_txt 를 못 써 작은 판정으로", error=repr(e)[:120])
    rows, in_card = [], False
    for raw in path.read_text("utf-8-sig").splitlines():
        line = raw.strip()
        if not line:
            continue
        if is_label(line):
            in_card = False
            continue
        if line.startswith("[장면]"):
            in_card = True
            continue
        if not in_card:
            rows.append(line)
    return list(enumerate(rows, 1))


def lexicon_paths(path: Path, topic: str | None) -> list[Path]:
    ps = []
    if topic:
        ps.append(ROOT / topic / "tts_lexicon.tsv")
    if path.parent.name == "shorts":
        ps.append(path.parent.parent / "tts_lexicon.tsv")
    ps.append(path.parent / "tts_lexicon.tsv")
    return ps


def load_lexicon(paths: list[Path]) -> list[tuple[str, str]]:
    pairs = []
    for p in paths:
        if p.is_file():
            for ln in p.read_text("utf-8-sig").splitlines():
                if ln.strip() and not ln.lstrip().startswith("#") and "\t" in ln:
                    a, b = ln.split("\t", 1)
                    pairs.append((a.strip(), b.strip()))
    return sorted(pairs, key=lambda x: -len(x[0]))


def apply_lex(text: str, lex: list[tuple[str, str]]) -> str:
    for a, b in lex:
        text = text.replace(a, b)
    text = re.sub(r"(?<![\w.])-(?=\d)", "마이너스 ", text)                 # tts_narration.tts_text 와 같음
    return re.sub(r"(?<![\w.])\+(?=\d)", "플러스 ", text)


# ------------------------------------------------------------------ 검사
def check_line(no: int, raw: str, lex: list[tuple[str, str]]) -> tuple[list[dict], list[tuple[str, str]]]:
    """→ (문제 [{no, level, kind, what, fix}], 사전에 더할 줄 [(원문, 읽는 소리)])"""
    s = apply_lex(raw, lex)
    out, add = [], []

    def hit(level, kind, what, fix):
        out.append({"no": no, "level": level, "kind": kind, "what": what, "fix": fix, "text": raw})

    for m in DECIMAL.finditer(s):
        src = m.group(0).strip()
        r = reading(m.group(1), m.group(2))
        hit("❌", "소수", src, f"사전: {src}<TAB>{r}")
        add.append((src, r))
    for m in COMMA_NUM.finditer(s):
        src = m.group(0).strip()
        r = reading(m.group(1), m.group(2))
        hit("❌", "쉼표 숫자", src, f"사전: {src}<TAB>{r} (또는 대본을 '5천2백' 꼴로)")
        add.append((src, r))
    for m in FRACTION.finditer(s):
        src = m.group(0)
        r = f"{sino(int(m.group(1)))}분의 {sino(int(m.group(2)))}"
        hit("❌", "분수", src, f"사전: {src}<TAB>{r}")
        add.append((src, r))
    if RANGE.search(s):
        hit("❌", "범위 물결", RANGE.search(s).group(0), "대본을 'A에서 B' 또는 'A부터 B까지'로")
    for m in SYMBOL.finditer(s):
        hit("❌", "기호", m.group(0), "기호를 말로 ('/' → '당'·'또는' · '→' → 문장으로 · '×' → '곱하기'·'배')")
    if LETTER_COMMA.search(s):
        hit("❌", "알파벳+쉼표", LETTER_COMMA.search(s).group(0).strip(), "'A번, …' 꼴 + 사전 'A번<TAB>에이 번' (tts_guide 5-1)")
    eng = sorted({m.group(0) for m in ENGLISH.finditer(s)})
    if eng:
        hit("⚠", "영어 낱말", ", ".join(eng[:6]), "사전에 읽는 소리 (예 'ETF<TAB>이티에프') — 모델이 영어로 읽거나 목소리가 바뀜")
    syl = len(SYL.findall(s))
    if syl > LONG_SYL:
        hit("⚠", "긴 문장", f"{syl}음절", f"{LONG_SYL}음절 넘음 — 쉼표에서 자동으로 나뉘지만(tts_narration v1.17) 두 문장으로 나누면 더 안전")
    elif syl < SHORT_SYL and not re.search(r"\|", s):
        hit("⚠", "짧은 문장", f"{syl}음절", "6음절 안 — 탈락이 잦은 꼴 (8번까지 다시 만듦). 앞뒤 문장과 합칠 수 있으면 합침")
    if HAERA.search(raw.strip()) and not raw.strip().endswith(("까.", "까?")):
        hit("⚠", "해라체", raw.strip()[-8:], "내레이션은 합니다체 — '…했다.' → '…했습니다.' (tts_guide 5-1)")
    if ORD_COMMA.search(s):
        hit("⚠", "서수 쉼표", ORD_COMMA.search(s).group(0), "'일곱 번째와 여덟 번째' 꼴로 (tts_guide 5-1)")
    if "(" in s or ")" in s:
        hit("⚠", "괄호", "( )", "괄호 속 말은 문장으로 풀거나 뺌 (읽지 않거나 끊겨 읽힘)")
    for m in BIG_INT.finditer(s):
        if not re.match(r"(19|20)\d\d$", m.group(1)):
            hit("⚠", "큰 숫자", m.group(1), f"'{reading(m.group(1))}' — 대본을 '2만 5천' 꼴로 쓰면 더 익숙함")
    return out, add


def check_script(path: Path, topic: str | None = None) -> dict:
    lex_paths = lexicon_paths(path, topic)
    lex = load_lexicon(lex_paths)
    issues, adds = [], []
    lines = read_lines(path)
    for no, line in lines:
        iss, add = check_line(no, line, lex)
        issues += iss
        adds += add
    uniq, seen = [], set()
    for a in adds:
        if a[0] not in seen:
            seen.add(a[0])
            uniq.append(a)
    return {"file": str(path), "sentences": len(lines), "lexicon": [str(p) for p in lex_paths if p.is_file()], "lexicon_entries": len(lex),
            "issues": issues, "fail": sum(i["level"] == "❌" for i in issues), "warn": sum(i["level"] == "⚠" for i in issues), "lexicon_add": uniq}


def write_lexicon(path: Path, adds: list[tuple[str, str]]) -> int:
    p = path.parent / "tts_lexicon.tsv"
    old = p.read_text("utf-8-sig") if p.is_file() else "# 읽는 소리 사전 (tools/tts_narration.py — TTS 에 넣는 글에만, 대본·자막은 그대로). 원문<TAB>읽는 소리\n"
    have = {ln.split("\t", 1)[0].strip() for ln in old.splitlines() if "\t" in ln and not ln.lstrip().startswith("#")}
    new = [(a, b) for a, b in adds if a not in have]
    if not new:
        return 0
    head = f"# (tools/tts_check.py {VERSION} — {date.today()} — {path.name}: {' · '.join(a for a, _ in new[:12])}{' …' if len(new) > 12 else ''})"
    text = old.rstrip("\n") + "\n" + head + "\n" + "\n".join(f"{a}\t{b}" for a, b in new) + "\n"
    p.write_text(text, "utf-8")
    return len(new)


def render(R: dict) -> str:
    w = (L := []).append
    w(f"# TTS 꼴 검사 — {Path(R['file']).name} ({date.today()})")
    w("")
    w(f"`tools/tts_check.py {VERSION}` · 문장 {R['sentences']}개 · 사전 {R['lexicon_entries']}줄 ({', '.join(Path(p).as_posix().split('/')[-2] + '/' + Path(p).name for p in R['lexicon']) or '없음'}) · "
      f"❌ {R['fail']} · ⚠ {R['warn']}")
    w("")
    if not R["issues"]:
        w("✅ 고칠 꼴 없음")
    else:
        w("| 문장 | 판정 | 꼴 | 무엇 | 고치는 법 | 문장 글 |")
        w("|---:|---|---|---|---|---|")
        for i in R["issues"]:
            w(f"| {i['no']} | {i['level']} | {i['kind']} | {i['what'].replace('|', '/')} | {i['fix'].replace('|', '/')} | {i['text'][:50].replace('|', '/')} |")
    return "\n".join(L) + "\n"


def selftest() -> int:
    ok = True

    def chk(name, cond):
        nonlocal ok
        ok &= bool(cond)
        print(("✅ " if cond else "❌ ") + name)

    chk("읽기: 42.5% → 사십이 점 오 퍼센트", reading("42.5", "%") == "사십이 점 오 퍼센트")
    chk("읽기: 0.75%p → 영 점 칠 오 퍼센트포인트", reading("0.75", "%p") == "영 점 칠 오 퍼센트포인트")
    chk("읽기: 15.0% → 십오 점 영 퍼센트", reading("15.0", "%") == "십오 점 영 퍼센트")
    chk("읽기: 137 · 2026 · 10000 · 52390", (sino(137), sino(2026), sino(10000), sino(52390)) == ("백삼십칠", "이천이십육", "만", "오만 이천삼백구십"))
    chk("읽기: 5,239 → 오천이백삼십구", reading("5,239") == "오천이백삼십구")
    lex = [("S&P 500", "에스앤피 오백"), ("42.5%", "사십이 점 오 퍼센트")]
    iss, add = check_line(1, "코스피는 최고가보다 42.5% 아래이고, S&P 500 은 3.7년 걸렸습니다.", lex)
    kinds = [i["kind"] for i in iss]
    chk("검사: 사전에 있는 소수는 통과 · 없는 3.7년만 ❌", kinds.count("소수") == 1 and add == [("3.7년", "삼 점 칠 년")])
    chk("검사: 사전에 있는 영어(S&P 500)는 경고 없음", "영어 낱말" not in kinds)
    iss, _ = check_line(2, "A, 바로 매도합니다.", [])
    chk("검사: 'A,' → ❌", any(i["kind"] == "알파벳+쉼표" for i in iss))
    iss, _ = check_line(3, "3~5년 동안 1/3 을 팔았다.", [])
    k = {i["kind"] for i in iss}
    chk("검사: 범위·기호·해라체", {"범위 물결", "기호", "해라체"} <= k)
    iss, _ = check_line(4, "−800만 원이 아니라 -800만 원입니다.", [])
    chk("검사: 음수 부호는 마이너스로 읽음 (오류 아님)", not any(i["level"] == "❌" for i in iss))
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "ep.txt"
        p.write_text("-도입\n반등 83번 중 56번이 저점을 깼습니다.\n본전까지 3.7년이 걸렸습니다.\n[장면]\n카드 1.5배\n-끝\n시청해주셔서 감사합니다.\n", "utf-8")
        R = check_script(p)
        chk("대본: 장 이름·카드 문구는 문장 아님 (3문장)", R["sentences"] == 3)
        n = write_lexicon(p, R["lexicon_add"])
        R2 = check_script(p)
        chk("사전 더하기 뒤 ❌ 0", n == 1 and R2["fail"] == 0)
    print("[SELFTEST] " + ("✅ 모두 통과" if ok else "❌ 실패 있음"))
    return 0 if ok else 1


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="대본 TTS 꼴 검사 + 숫자 읽는 소리 사전")
    ap.add_argument("script", nargs="?"); ap.add_argument("--topic"); ap.add_argument("--write-lexicon", action="store_true")
    ap.add_argument("--out"); ap.add_argument("--selftest", action="store_true"); ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args(argv)
    logging.basicConfig(level=getattr(logging, a.log_level), format="%(message)s", stream=sys.stdout)
    if a.selftest:
        return selftest()
    if not a.script or not Path(a.script).is_file():
        ap.error("대본 .txt 경로를 주세요")
    t0 = time.perf_counter()
    p = Path(a.script).resolve()
    topic = a.topic or (p.relative_to(ROOT).parts[0] if ROOT in p.parents else None)
    R = check_script(p, topic)
    log("CHECK", file=p.name, sentences=R["sentences"], lexicon=R["lexicon_entries"], fail=R["fail"], warn=R["warn"], lexicon_add=len(R["lexicon_add"]))
    if a.write_lexicon and R["lexicon_add"]:
        n = write_lexicon(p, R["lexicon_add"])
        log("LEXICON", file=str((p.parent / "tts_lexicon.tsv").relative_to(ROOT)) if ROOT in p.parents else str(p.parent / "tts_lexicon.tsv"), added=n,
            first=", ".join(f"{x}={y}" for x, y in R["lexicon_add"][:4]))
        R = check_script(p, topic)
        log("CHECK", after="사전 더한 뒤", fail=R["fail"], warn=R["warn"])
    md = render(R)
    if a.out:
        Path(a.out).write_text(md, "utf-8")
    else:
        print(md)
    log("DONE", file=p.name, fail=R["fail"], warn=R["warn"], seconds=round(time.perf_counter() - t0, 2))
    return 1 if R["fail"] else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
