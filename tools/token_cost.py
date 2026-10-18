#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-18 — 최초 작성. 사용자 질문 2026-10-18 "1,3번으로 각각 만들어봐 그리고 하나 만들때 토큰 얼마나 들고 가장 많이
#          드는 부분이 어딘지 알려줘봐": Claude Code 대화 기록(jsonl)의 API 사용량(usage)으로 영상 하나 만드는 데 든 토큰을 단계별로 나눔.
r"""
영상 하나 만드는 데 든 토큰 — 단계별로 나누기

  python3 tools/token_cost.py <대화 기록.jsonl> [다른 기록.jsonl …] [--since 2026-10-18T04:33:00Z] [--top 12]

기록 위치: ~/.claude/projects/<저장소 이름>/<세션>.jsonl (보조 작업자는 <세션>/subagents/agent-*.jsonl). 저장소에 넣지 않음.

세는 법 (API 호출 한 번 = 기록의 assistant 줄 하나, 같은 message.id 는 한 번만):
- 입력 = input + cache_creation(새로 캐시에 씀) + cache_read(캐시에서 다시 읽음). 출력 = output(생각 포함).
- 가중치(입력 1 기준 값의 비율): 새 입력 1 · 캐시 쓰기 1.25 · 캐시 읽기 0.1 · 출력 5 — 요금표의 비율. 금액이 아니라 '무게'.
- 단계 나누기: 호출 i 의 맥락 크기 − 호출 i−1 의 맥락 크기 − 호출 i−1 의 출력 ≈ 그 사이에 들어온 도구 결과 크기.
  그 결과는 뒤의 모든 호출에서 다시 읽히므로 → 그 결과의 단계에 '크기 × 1.25 + 크기 × 0.1 × 남은 호출 수'를 붙인다.
  호출의 출력은 그 호출이 부른 도구(예: 대본 파일 Write)의 단계에 붙인다. 시작 맥락(시스템·지시)은 '시작 맥락'.
로그: [STAGE] 시각 key=value (stderr).
"""
import argparse
import collections
import json
import logging
import re
import sys
import time

VERSION = "v1.0"
W = {"input": 1.0, "write": 1.25, "read": 0.1, "output": 5.0}
LOG = logging.getLogger("token_cost")


def log(stage, **kv):
    LOG.info("[%s] %s %s", stage, time.strftime("%Y-%m-%dT%H:%M:%S"), " ".join(f"{k}={v}" for k, v in kv.items()))


# 단계 이름 — 도구 입력(파일 경로·명령)으로 고름. 위에서부터 처음 맞는 것.
RULES = [
    ("법령 확인", r"law_text|legalize|/law|claude-law"),
    ("니즈·분석 자료", r"comments\.csv|content_research|analysis\.(md|json)|result/outliers|data_insights|shorts_insights|topic_candidates|used_content"),
    ("계산 코드", r"/calc/|calc\.py"),
    ("자막(SRT)", r"srt_tool|\.srt\b"),
    ("제목", r"title_fit|titles\.md"),
    ("요약 문서", r"make_summary|summary\.md"),
    ("쇼츠", r"/shorts/"),
    ("썸네일 프롬프트", r"/thumbnails/"),
    ("업로드 시트", r"upload\.md"),
    ("사실 확인표", r"checklist\.md"),
    ("지시사항 읽기", r"guides/|CLAUDE\.md|pipeline\.md"),
    ("영상 장면 코드", r"video/(episodes|render|prototypes)|kit\.js"),
    ("도구 코드 읽기", r"tools/[\w/]+\.(py|mjs|sh|toml)"),
    ("잘린 큰 결과 다시 읽기", r"tool-results/"),
    ("git", r"\bgit (add|commit|push|pull|log|show|diff|status)"),
]


def stage_of(tool, inp, own):
    # 쓰기는 내용이 아니라 파일 경로로 가름 (README 안에 'guides/' 가 적혀 있어도 README 단계)
    key = [inp.get(k) for k in ("file_path", "command", "pattern", "path", "url", "prompt") if isinstance(inp.get(k), str)]
    s = " ".join(key)[:4000] if key else json.dumps(inp, ensure_ascii=False)[:4000]
    for name, rx in RULES:
        if re.search(rx, s):
            if name in ("자막(SRT)", "쇼츠", "썸네일 프롬프트", "업로드 시트", "사실 확인표", "제목", "계산 코드") and own and own not in s \
                    and tool in ("Read", "Bash", "Grep", "Glob"):
                return "예시 폴더 읽기"        # 다른 영상의 같은 종류 파일을 본보기로 읽음
            return name
    if own and own in s:
        if tool in ("Write", "Edit") and re.search(r"\.txt\b", s):
            return "대본"
        return "README·기타 자기 파일" if tool in ("Write", "Edit") else "자기 파일 다시 읽기"
    if re.search(r"economic/source/", s):
        return "예시 폴더 읽기"
    return f"기타({tool})"


def est_out(content):
    """보이는 출력(글·도구 입력)의 글자 수 → 토큰 추정. 보정 2026-10-18 메인 기록 10개: 한글 0.9자/토큰 · 그 밖 1.6자/토큰 (±10%).
    보조 작업자 기록은 output_tokens 가 스트리밍 시작 값(3~16)만 남아 이걸 씀. 생각(thinking) 토큰은 기록에 없어 빠짐 → 적게 잡힘."""
    ko = other = 0
    for c in content:
        t = c.get("text", "") if c.get("type") == "text" else \
            json.dumps(c.get("input", {}), ensure_ascii=False) if c.get("type") == "tool_use" else c.get("thinking", "") or ""
        k = len(re.findall(r"[가-힣]", t))
        ko += k
        other += len(t) - k
    return ko / 0.9 + other / 1.6


def load(paths, since):
    calls, seen = [], set()
    for p in paths:
        for line in open(p, encoding="utf-8"):
            try:
                d = json.loads(line)
            except ValueError:
                continue
            if since and d.get("timestamp", "") < since:
                continue
            m = d.get("message") or {}
            if d.get("type") == "assistant" and m.get("usage"):
                if m.get("id") in seen:
                    # 한 응답이 블록마다 여러 줄로 기록됨 → 도구 호출은 덧붙이고, 출력 수는 마지막(가장 큰) 값
                    calls[-1]["tools"] += [(c["name"], c.get("input", {})) for c in m.get("content", []) if c.get("type") == "tool_use"]
                    calls[-1]["out"] = max(calls[-1]["out"], m["usage"].get("output_tokens", 0))
                    calls[-1]["est"] += est_out(m.get("content", []))
                    continue
                seen.add(m.get("id"))
                u = m["usage"]
                calls.append(dict(ts=d.get("timestamp", ""), inp=u.get("input_tokens", 0), cw=u.get("cache_creation_input_tokens", 0),
                                  cr=u.get("cache_read_input_tokens", 0), out=u.get("output_tokens", 0),
                                  tools=[(c["name"], c.get("input", {})) for c in m.get("content", []) if c.get("type") == "tool_use"],
                                  est=est_out(m.get("content", []))))
    for c in calls:                                        # 기록된 출력이 추정의 1/3 도 안 되면 추정을 씀
        c["estimated"] = c["out"] < c["est"] / 3
        if c["estimated"]:
            c["out"] = int(c["est"])
    return calls


def analyse(calls, own):
    st = collections.defaultdict(lambda: collections.Counter())
    n = len(calls)
    ctx = [c["inp"] + c["cw"] + c["cr"] for c in calls]
    for i, c in enumerate(calls):
        stages = [stage_of(t, x, own) for t, x in c["tools"]] or ["답·생각(도구 없음)"]
        for s in stages:                                   # 출력은 그 호출이 부른 도구의 단계로
            st[s]["output"] += c["out"] / len(stages)
        added = ctx[0] if i == 0 else max(0, ctx[i] - ctx[i - 1] - calls[i - 1]["out"])
        if i == 0:
            src = ["시작 맥락(시스템·지시)"]
        else:
            src = [stage_of(t, x, own) for t, x in calls[i - 1]["tools"]] or ["답·생각(도구 없음)"]
        later = n - i - 1
        if i and src[0].startswith("기타"):
            LOG.debug("[OTHER] %s tokens=%d %s", calls[i]["ts"], added, json.dumps(calls[i - 1]["tools"], ensure_ascii=False)[:160])
        for s in src:                                      # 들어온 결과는 그 뒤 호출마다 다시 읽힘
            st[s]["added"] += added / len(src)
            st[s]["w"] += added / len(src) * (W["write"] + W["read"] * later)
    for s in st:
        st[s]["w"] += st[s]["output"] * W["output"]
    tot = dict(estimated=sum(c["estimated"] for c in calls), calls=n, input=sum(c["inp"] for c in calls), write=sum(c["cw"] for c in calls), read=sum(c["cr"] for c in calls),
               output=sum(c["out"] for c in calls), peak=max(ctx) if ctx else 0)
    tot["w"] = tot["input"] * W["input"] + tot["write"] * W["write"] + tot["read"] * W["read"] + tot["output"] * W["output"]
    return tot, st


def main(argv=None):
    ap = argparse.ArgumentParser(description="대화 기록 사용량 → 단계별 토큰")
    ap.add_argument("jsonl", nargs="+")
    ap.add_argument("--since", default="", help="이 시각(UTC ISO) 뒤 호출만")
    ap.add_argument("--own", default="", help="이 영상ID — 자기 파일과 예시 폴더를 가름")
    ap.add_argument("--top", type=int, default=14)
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args(argv)
    logging.basicConfig(level=getattr(logging, a.log_level), format="%(message)s", stream=sys.stderr)
    calls = load(a.jsonl, a.since)
    log("LOAD", version=VERSION, files=len(a.jsonl), calls=len(calls), first=calls[0]["ts"] if calls else "-", last=calls[-1]["ts"] if calls else "-")
    if not calls:
        print("호출 없음")
        return 1
    tot, st = analyse(calls, a.own)
    allin = tot["input"] + tot["write"] + tot["read"]
    print(f"API 호출 {tot['calls']}번 · 입력 {allin:,} (새 {tot['input']:,} · 캐시 쓰기 {tot['write']:,} · 캐시 읽기 {tot['read']:,}) · "
          f"출력 {tot['output']:,} · 가장 큰 맥락 {tot['peak']:,}")
    print(f"가중 합계 {tot['w']:,.0f} (입력 1 기준 — 캐시 읽기 0.1·쓰기 1.25·출력 5)")
    if tot["estimated"]:
        print(f"※ 출력 {tot['estimated']}/{tot['calls']}번은 기록에 없어 글자 수로 추정 (생각 토큰 빠짐 — 실제보다 적음)")
    print()
    print("| 단계 | 가중 몫 | 들어온 결과(토큰) | 출력(토큰) |")
    print("|---|---|---|---|")
    sw = sum(c["w"] for c in st.values()) or 1           # 몫은 단계 합으로 나눔 (사용량 합계와 몇 % 다를 수 있음 — 추정)
    for s, c in sorted(st.items(), key=lambda kv: -kv[1]["w"])[: a.top]:
        print(f"| {s} | {c['w'] / sw:.0%} | {c['added']:,.0f} | {c['output']:,.0f} |")
    log("DONE", weighted=f"{tot['w']:.0f}", stage_sum=f"{sw:.0f}", stages=len(st))
    return 0


if __name__ == "__main__":
    sys.exit(main())
