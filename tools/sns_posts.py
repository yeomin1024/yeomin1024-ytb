#!/usr/bin/env python3
# VERSION: v1.0 — 2026-11-03 — 롱폼 편마다 X(트위터)·스레드 글을 만들고 SNS 평가판(stock/topics/SNS평가판.html)을 채움
#   (사용자 지시 2026-11-03 "대본 당 트위터, 스레드 글 작성해서 평가판 만들어봐 항목은 10가지 정도로 확장하고 점수 및 결과는 댓글에 넣는 방식으로").
#   · 원본 = stock/topics/sns/sns_<날짜>.json (편마다 제목·문항 10개 {q, A, B, ans}·결과 유형 3개) — 글은 이 도구가 짬 (손으로 고치지 않음)
#   · X  : 글 하나 = 가중 글자 280 이하 (한글·한자 등은 2, 영문·숫자·기호는 1 — X 셈법) → 첫 글(테스트 소개) + 문항 글 + 댓글(정답·점수 / 결과 유형·링크)
#   · 스레드: 글 하나 = 500자 이하 → 첫 글(소개 + 문항 앞 절반) + 이어 쓰는 글(뒤 절반) + 댓글(정답·점수·결과 유형·링크)
#   · 점검: 글자 수 · 권유·과장 낱말(board_check K8) · 정답 글자가 한쪽으로 몰리지 않게 → 어기면 멈춤(끝 코드 1)
#   · 결과: stock/topics/sns/sns_posts.md (그대로 복사해 올리는 글) · stock/topics/SNS평가판.html (대본 평가판과 같은 틀 — 줄·칸 피드백·판정)
#   연구·교육용 도구 — 투자 권유가 아님.
# 사용: python3 tools/sns_posts.py [원본.json] [--check]
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import board_check as BC              # noqa: E402  K8 권유·과장 낱말
import script_feedback_board as SFB   # noqa: E402  판 틀·build

SRC_DIR = ROOT / "stock/topics/sns"
OUT_MD = SRC_DIR / "sns_posts.md"
OUT_BOARD = ROOT / "stock/topics/SNS평가판.html"
URL_BOARD = "https://claude.ai/artifact/YTmRoWuT9QDCuqfBhoKLJv"
X_MAX, TH_MAX = 280, 500


def log(stage, **kv):
    ts = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    print(f"[{stage}] [{ts}] " + " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) else v}" for k, v in kv.items()))


def xlen(s):
    """X 가중 글자 수 — twitter-text 기본 설정: 이 범위는 1, 나머지(한글·이모지 등)는 2."""
    n = 0
    for ch in s:
        c = ord(ch)
        n += 1 if (c <= 4351 or 8192 <= c <= 8205 or 8208 <= c <= 8223 or 8242 <= c <= 8247) else 2
    return n


def item_text(i, it):
    return f"{i}. {it['q']}\nA. {it['A']}\nB. {it['B']}"


def pack(head, chunks, limit, measure, sep="\n\n"):
    """머리 글 뒤에 문항을 차례로 붙이다가 한도를 넘으면 새 글로."""
    posts, cur = [], head
    for c in chunks:
        cand = (cur + sep + c) if cur else c
        if measure(cand) <= limit:
            cur = cand
        else:
            posts.append(cur)
            cur = c
    if cur:
        posts.append(cur)
    return posts


def make(ep, link):
    items = ep["items"]
    ans = " ".join(f"{i}{it['ans']}" for i, it in enumerate(items, 1))
    score = "맞힌 문제마다 10점 · 90점 이상 통과 · 60~80점 주의 · 50점 이하 불통과"
    t1, t2, t3 = ep["types"]
    chunks = [item_text(i, it) for i, it in enumerate(items, 1)]
    # X — 첫 글은 소개만, 문항은 한도 안에서 묶음, 댓글 둘
    x_head = f"[주식 테스트] {ep['title']}\n\n문제 {len(items)}개 · 당신이라면 A, B 중 무엇을 고를까요?\n답을 적어 두고, 정답과 점수는 댓글에서 확인하세요."
    x_posts = [x_head] + pack("", chunks, X_MAX, xlen)
    x_comments = [f"정답\n{ans}\n\n{score}\n\n몇 점 나왔는지 남겨 주세요.",
                  f"통과: {t1}\n주의: {t2}\n불통과: {t3}\n\n실제 숫자로 푼 해설 ▶ {link}\n※ 투자 권유가 아닌 테스트입니다."]
    # 스레드 — 첫 글에 소개 + 앞 문항, 이어 쓰는 글, 댓글 하나
    th_head = f"[주식 테스트] {ep['title']}\n\n문제 {len(items)}개, 당신이라면 A와 B 중 무엇을 고를지 적어 두세요. 정답과 점수는 댓글에 있습니다."
    th_posts = pack(th_head, chunks, TH_MAX, len)
    th_comments = [f"정답\n{ans}\n\n{score}\n\n통과: {t1}\n주의: {t2}\n불통과: {t3}\n\n실제 숫자로 푼 해설 ▶ {link}\n몇 점 나왔는지 댓글로 남겨 주세요. ※ 투자 권유가 아닌 테스트입니다."]
    return {"x": (x_posts, x_comments), "threads": (th_posts, th_comments), "answers": ans}


def check(ep, out):
    bad = []
    letters = [it["ans"] for it in ep["items"]]
    if len(set(letters)) < 2 or max(letters.count("A"), letters.count("B")) > 7:
        bad.append(f"정답 글자 몰림 {''.join(letters)}")
    for plat, (posts, comms), lim, meas in (("x", out["x"], X_MAX, xlen), ("threads", out["threads"], TH_MAX, len)):
        for k, p in enumerate(posts + comms, 1):
            if meas(p) > lim:
                bad.append(f"{plat} 글 {k} {meas(p)}/{lim} 넘침")
            m = BC.K8.search(p)
            if m:
                bad.append(f"{plat} 글 {k} 권유·과장 낱말 '{m.group(0)}'")
    return bad


def board_entry(ep, plat, posts, comms, ver, meas, lim, ans):
    lines, n = [], 0
    for k, p in enumerate(posts, 1):
        for ln in p.split("\n"):
            if ln.strip():
                n += 1
                lines.append({"n": n, "t": ln, "sec": f"글 {k} ({meas(p)}/{lim})"})
    for k, c in enumerate(comms, 1):
        for ln in c.split("\n"):
            if ln.strip():
                n += 1
                lines.append({"n": n, "t": ln, "sec": f"댓글 {k} ({meas(c)}/{lim})"})
    name = "X 글" if plat == "x" else "스레드 글"
    return {"key": f"e{ep['ep']}-{plat}", "ep": ep["ep"], "label": f"{ep['ep']}편", "kind": "sns", "kindLabel": name,
            "title": ep["title"], "ver": ver, "file": f"stock/topics/sns/sns_posts.md {ep['ep']}편 {name}",
            "fields": [["answers", "정답 (댓글에)", ans, False],
                       ["count", "글 수", f"본문 {len(posts)}개 + 댓글 {len(comms)}개 · {'가중 280' if plat == 'x' else '500자'} 한도", False]],
            "lines": lines}


def main(argv):
    srcs = [Path(a) for a in argv if a.endswith(".json")] or sorted(SRC_DIR.glob("sns_*.json"))[-1:]
    if not srcs:
        log("ERROR", stage="input", next="stock/topics/sns/sns_<날짜>.json 을 먼저 씀")
        return 1
    D = json.loads(srcs[0].read_text("utf-8"))
    md = [f"# 주식 SNS 글 — X(트위터)·스레드 ({srcs[0].name}, {D.get('ver', 'v1')})", "",
          "> 도구 `tools/sns_posts.py` 가 원본 json 에서 만든 글 — 손으로 고치지 않음 (고칠 땐 원본 json → 도구 다시). 올리는 순서: 본문 글을 차례로(스레드는 이어 쓰기) → 댓글은 본문 아래 답글로. ※ 연구·교육용 — 투자 권유 아님.", ""]
    entries, problems = [], []
    for ep in D["episodes"]:
        out = make(ep, D.get("video_link", "(영상 링크)"))
        bad = check(ep, out)
        problems += [f"{ep['ep']}편 {b}" for b in bad]
        md += [f"## {ep['ep']}편 — {ep['title']}", ""]
        for plat, lim, meas in (("x", X_MAX, xlen), ("threads", TH_MAX, len)):
            posts, comms = out[plat]
            md.append(f"### {'X (트위터)' if plat == 'x' else '스레드'} — 본문 {len(posts)}개 · 댓글 {len(comms)}개")
            for k, p in enumerate(posts, 1):
                md += ["", f"**글 {k}** ({meas(p)}/{lim})", "```", p, "```"]
            for k, c in enumerate(comms, 1):
                md += ["", f"**댓글 {k}** ({meas(c)}/{lim})", "```", c, "```"]
            md.append("")
            entries.append(board_entry(ep, plat, posts, comms, D.get("ver", "v1"), meas, lim, out["answers"]))
        log("EP", ep=ep["ep"], x_posts=len(out["x"][0]), x_max=max(xlen(p) for p in out["x"][0] + out["x"][1]),
            threads_posts=len(out["threads"][0]), threads_max=max(len(p) for p in out["threads"][0] + out["threads"][1]),
            answers=out["answers"], problems=len(bad))
    for p in problems:
        log("FAIL", issue=p)
    if problems:
        log("STOP", next="원본 json 을 고친 뒤 다시")
        return 1
    SFB.BOARDS["sns"] = {
        "out": OUT_BOARD, "title": "주식 SNS 평가판", "h1": "주식 SNS 평가판 — X·스레드",
        "intro": lambda: ("롱폼 1~4편마다 X(트위터)·스레드에 올릴 글입니다 — 문제 10개는 본문에, 정답·점수·결과는 댓글에. "
                          "줄을 골라(Shift 로 여러 줄) 또는 칸마다 '피드백'을 남기고, 마음에 들면 <b>통과 (올림)</b>. "
                          "'삭제'로 피드백을 지울 수 있습니다. 연구·교육용 — 투자 권유가 아닙니다."),
        "verdict": {"pass": "통과 (올림)", "hold": "보류"},
        "verdict_hint": "통과하면 그 글을 그대로 올리면 됩니다 (영상 링크는 올린 뒤 채움)",
        "empty": "아직 글이 없습니다.",
    }
    tpl = SFB.TPL.read_text("utf-8")
    page, data = SFB.build("sns", entries, tpl)
    if "--check" not in argv:
        OUT_MD.write_text("\n".join(md) + "\n", "utf-8")
        OUT_BOARD.write_text(page, "utf-8")
    log("DONE", entries=len(entries), lines=sum(len(e["lines"]) for e in entries), md=str(OUT_MD.relative_to(ROOT)),
        board=str(OUT_BOARD.relative_to(ROOT)), bytes=len(data.encode()), wrote="--check" not in argv)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
