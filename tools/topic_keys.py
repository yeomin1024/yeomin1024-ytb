#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-11-27 — 새 주제 두 개의 키 이름: 최신 트렌드 = trend (TREND_…) · 자기계발 = selfdev (SELFDEV_…) — 사용자 지시 2026-11-27
#          "최신 트렌드, 자기계발 주제도 만들거니까 변수명 만들어봐" (폴더는 주제를 만들 때 이 이름으로). 함수 TOPICS·UPLOADS.
# (v1.0) — 2026-11-27 — 최초: 주제 접두사 환경 변수 (사용자 지시 2026-11-27 "주제별 접두사를 변수명에 붙여서 구분되도록해 내가 넣어야될 변수명 다 알려줘").
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.1 | 2026-11-27 | 새 주제 trend · selfdev | TOPICS · UPLOADS |
# | v1.0 | 2026-11-27 | 최초 — tag · get · apply · names · 표 출력 | 모두 |
"""주제별 키 — 환경 변수 이름 앞에 주제 접두사 (예: PSYCHOLOGY_YOUTUBE_API_KEY).

  python3 tools/topic_keys.py            # 주제마다 넣을 변수 이름 + 지금 이 세션에 들어 있는지 (값은 출력하지 않음)
  python3 tools/topic_keys.py stock      # 그 주제만

도구는 시작할 때 한 번 apply(주제) → 그 주제의 키를 이 프로세스의 기본 이름(YOUTUBE_API_KEY 등)으로 씀.
찾는 순서 (앞이 먼저): 환경 변수 <주제>_<이름> (v1.0 새 꼴) → <이름>_<주제> (옛 꼴 — 분석기 v2.6.0) → <이름> (공통).
PC 는 <주제>/.env 파일(업로드·분석 화면의 키 칸)이 이미 주제별이라 접두사 없이 그대로.
⚠️ 키는 시작할 때 하나로 정해지고, 오류(할당량 초과 등)가 나도 다른 키로 바꾸지 않는다 — 여러 프로젝트로 할당량을 이어 쓰는 것은
YouTube API 정책 위반(할당량 우회). 할당량이 더 필요하면 할당량 증가 신청. 값은 출력하지 않는다.
"""
import os
import re
import sys

NAMES = ("YOUTUBE_API_KEY", "YOUTUBE_CLIENT_ID", "YOUTUBE_CLIENT_SECRET", "YOUTUBE_REFRESH_TOKEN", "GITHUB_TOKEN")
TOPICS = ("psychology", "crisis", "economic", "stock", "history", "shopping", "music", "test", "new", "math", "trend", "selfdev")
UPLOADS = {"psychology", "crisis", "economic", "stock", "shopping", "music", "test", "trend", "selfdev"}   # 채널에 올리는 주제 (업로드 키 3개)


def tag(topic: str) -> str:
    """주제 폴더 → 접두사 (economic → ECONOMIC) — 분석기 folder_tag 와 같은 규칙."""
    return re.sub(r"[^0-9A-Za-z가-힣]+", "_", str(topic)).strip("_").upper()


def get(name: str, topic: str | None = None, environ=None) -> tuple[str, str]:
    """→ (값, 어디서). 없으면 ("", "-")."""
    env = os.environ if environ is None else environ
    if topic:
        t = tag(topic)
        for k in (f"{t}_{name}", f"{name}_{t}"):
            v = (env.get(k) or "").strip()
            if v:
                return v, f"env:{k}"
    v = (env.get(name) or "").strip()
    return (v, f"env:{name}") if v else ("", "-")


def apply(topic: str | None, names=NAMES, environ=None, say=None) -> dict:
    """그 주제 키가 있으면 이 프로세스의 기본 이름에 넣음 (한 번 — 오류가 나도 바꾸지 않음). → {이름: 어디서}."""
    env = os.environ if environ is None else environ
    used = {}
    if not topic:
        return used
    for n in names:
        v, src = get(n, topic, env)
        if v and src != f"env:{n}":
            env[n] = v
        used[n] = src
    picked = {n: s for n, s in used.items() if s != "-"}
    if say is not None and picked:
        say(f"[KEYS] topic={topic} " + " ".join(f"{n}={s}" for n, s in picked.items()) + " (값은 출력하지 않음)")
    return used


def main(argv=None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    topics = argv or list(TOPICS)
    print("| 주제 | 넣을 변수 이름 | 지금 이 세션 |")
    print("|---|---|---|")
    for t in topics:
        for n in NAMES:
            if n.startswith("YOUTUBE_CLIENT") or n == "YOUTUBE_REFRESH_TOKEN":
                if t not in UPLOADS:
                    continue
            if n == "GITHUB_TOKEN":
                continue                                   # GitHub 토큰은 모든 주제 공통 하나 (GITHUB_TOKEN)
            _, src = get(n, t)
            print(f"| {t} | `{tag(t)}_{n}` | {'있음 (' + src + ')' if src != '-' else '없음'} |")
    print("\n공통: `GITHUB_TOKEN` 하나 (주제별로 나누려면 `<주제>_GITHUB_TOKEN`). 값은 출력하지 않음.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
