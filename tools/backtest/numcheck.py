# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-10-17 — about(): 대본에서 말하는 어림 금액 '약 56만 달러' · '약 9만 6천 달러' (단위 하나 — 정확한 값은 화면에).
#          사용자가 붙인 페르소나 피드백 2026-10-17 4번 "한국식 만 단위 금액이 해외 자동 번역에 취약 … '56만 4,469달러', '1,730만 6,585달러'처럼
#          두 단위가 섞인 표현" (stock/guides/README.md 5번).
# v1.0 — 2026-10-16 — 최초. 주식 대본 숫자 검사 공통 부품 (주식 2·3·4번 — 사용자 지시 2026-10-16 "같은 방식으로 필요한 소스 생성해서 3개 영상 미리보기
#          영상 만들어봐"). 1번 영상 check_numbers.py v3.0 의 방법 그대로: 문장마다 결과 파일에서 글자를 다시 만들어 그 문장에 그대로 있는지 + 조건 검사 +
#          대본의 모든 숫자가 검사표에 있는지 → checklist.md (stock/guides/concept.md 2번 '숫자는 코드 출력만').
"""사용:
    from backtest import numcheck as nc
    C = nc.Checker(txt_path)
    n = C.S("문장에 든 글자")             # 그 글자가 든 문장 번호 (하나여야 함)
    C.need(n, nc.won(95647), "근거")     # '9만 5,647달러' 가 그 문장에 있어야 함
    C.need_any(n, nc.pcts(-0.2099), "근거")
    C.cond(n, 조건, "근거", "글자")       # 조건이 참 + (글자가 있으면) 그 글자가 문장에 있어야 함
    sys.exit(C.report(out_md, title))
"""
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import srt_tool  # noqa: E402

NATIVE = {1: "한", 2: "두", 3: "세", 4: "네", 5: "다섯", 6: "여섯", 7: "일곱", 8: "여덟", 9: "아홉", 10: "열"}


def rint(x):
    """반올림 (0.5 는 올림 — 대본·장면과 같음)."""
    import math
    return int(math.floor(float(x) + 0.5))


def comma(v):
    return f"{v:,}"


def won(x, thousand=False):
    """달러 금액 → 대본 글자: 95647 → '9만 5,647달러' · 100945 → '10만 945달러' · 200000 → '20만 달러' · 9461 → '9,461달러'.
    thousand=True: 25000 → '2만 5천 달러' (딱 떨어지는 문턱)."""
    v = rint(x)
    if v < 10_000:
        return f"{comma(v)}달러"
    man, rest = divmod(v, 10_000)
    if rest == 0:
        return f"{man}만 달러"
    if thousand and rest % 1000 == 0:
        return f"{man}만 {rest // 1000}천 달러"
    return f"{man}만 {comma(rest)}달러"


def about(x):
    """대본에서 말하는 어림 금액 (단위 하나, '만 + 쉼표 숫자'를 섞지 않음):
    9461 → '9,461달러' (1만 미만은 그대로) · 95647 → '약 9만 6천 달러' (천 단위 반올림) · 564469 → '약 56만 달러' (만 단위 반올림) ·
    17306585 → '약 1,731만 달러'."""
    v = rint(x)
    if v < 10_000:
        return f"{comma(v)}달러"
    if v < 100_000:
        man, th = divmod(rint(v / 1000), 10)
        return f"약 {man}만 {th}천 달러" if th else f"약 {man}만 달러"
    return f"약 {comma(rint(v / 10_000))}만 달러"


def times(x, d=2):
    """배수 글자: 3.1614 → '3.16배'."""
    return f"{x:.{d}f}배"


def pct(x, d=1):
    return f"{abs(x) * 100:.{d}f}%"


def pcts(x, d=1):
    """허용 글자 목록: '21.0%' 와 끝이 .0 이면 '21%' 도."""
    a = pct(x, d)
    out = [a]
    if a.endswith(".0%"):
        out.append(a[:-3] + "%")
    return out


def ym(d):
    y, m, _ = d.split("-")
    return f"{int(y)}년 {int(m)}월"


def md(d):
    _, m, dd = d.split("-")
    return f"{int(m)}월 {int(dd)}일"


def ymd(d):
    y, m, dd = d.split("-")
    return f"{int(y)}년 {int(m)}월 {int(dd)}일"


def days(a, b):
    return (date.fromisoformat(b) - date.fromisoformat(a)).days


class Checker:
    def __init__(self, txt):
        self.txt = Path(txt)
        self.sent = srt_tool.parse_txt(self.txt)
        self.checks = []            # (문장 번호, [허용 글자], 근거, 조건 결과 또는 None)

    def S(self, anchor):
        hits = [i + 1 for i, s in enumerate(self.sent) if anchor in s]
        if len(hits) != 1:
            raise SystemExit(f"[CHECK] 문장 찾기 '{anchor}' → {len(hits)}개 {hits} (하나여야 함)")
        return hits[0]

    def need(self, n, text, why):
        self.checks.append((n, [text], why, None))

    def need_any(self, n, texts, why):
        self.checks.append((n, list(texts), why, None))

    def cond(self, n, ok, why, token=""):
        self.checks.append((n, [token], why, bool(ok)))

    def report(self, out_md, title, source):
        rows, bad = [], 0
        covered = {}
        for n, texts, why, ok in self.checks:
            s = self.sent[n - 1]
            hit_t = next((t for t in texts if t and t in s), None)
            if ok is None:
                hit = hit_t is not None
            else:
                hit = ok and (not texts[0] or texts[0] in s)
            bad += not hit
            shown = " / ".join(f"`{t}`" for t in texts if t) or "—"
            rows.append(f"| {n} | {s} | {shown} | {why} | {'✅' if hit else '❌'} |")
            for t in ([hit_t] if hit_t else texts):
                covered.setdefault(n, set()).update(x.rstrip(",.") for x in re.findall(r"\d[\d,.]*", t or ""))
        nums_bad = []
        for n, s in enumerate(self.sent, 1):
            for tok in re.findall(r"\d[\d,.]*", s):
                tok = tok.rstrip(",.")
                if tok not in covered.get(n, set()):
                    nums_bad.append(f"문장 {n}: '{tok}' — {s}")
        L = [f"# {title}", "", f"- 대본 `{self.txt.name}` {len(self.sent)}문장 · 결과 {source}",
             f"- 검사 {len(self.checks)}개 · 맞음 {len(self.checks) - bad} · 틀림 {bad} · 검사표에 없는 숫자 {len(nums_bad)}", "",
             "| 문장 | 대본 | 찾는 글자 | 근거 | 결과 |", "|---:|---|---|---|---|"] + rows
        if nums_bad:
            L += ["", "## 검사표에 없는 숫자", ""] + [f"- {x}" for x in nums_bad]
        Path(out_md).write_text("\n".join(L) + "\n", "utf-8")
        print(f"[CHECK] sentences={len(self.sent)} numbers={len(self.checks)} ok={len(self.checks) - bad} bad={bad} uncovered={len(nums_bad)} → {out_md}")
        for n, texts, why, ok in self.checks:
            s = self.sent[n - 1]
            if not (any(t and t in s for t in texts) if ok is None else (ok and (not texts[0] or texts[0] in s))):
                print(f"  ❌ 문장 {n}: {texts} ({why}) — {s}")
        for x in nums_bad[:60]:
            print("  ⚠️ 검사표에 없음:", x)
        return 1 if (bad or nums_bad) else 0
