#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-11-27 — 최초: 꺼 둔 주제 (제작 판 '주제 켜기·끄기' → studio/state/topics.json) — 사용자 지시 2026-11-27
#          "주제 비활성화도 할 수 있도록 해 비활성화하면 아티팩트에서 보이지 않고 에이전트가 보지도 않도록 하는거야".
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.0 | 2026-11-27 | 최초 — disabled · is_disabled · guard · filter | 모두 |
"""꺼 둔 주제 읽기 — 여러 도구가 같이 씀 (tts_narration · kaggle_tts_panel · upload_preview · upload_web · channel_stats · cloud_run · next_topic · studio_board).

  python3 tools/topic_state.py            # 꺼 둔 주제 목록
  python3 tools/topic_state.py psychology # 그 주제가 꺼져 있으면 종료 코드 3

파일 studio/state/topics.json = {"updated": …, "disabled": ["stock", …]} — Claude 가 '제작 판 동기화' 때 씀. 파일이 없으면 모두 켜짐.
꺼 둔 주제는 Claude·도구가 읽지도 작업하지도 않는다 (사용자가 판에서 다시 켤 때까지). 연구·교육용.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE_FILE = ROOT / "studio" / "state" / "topics.json"


def disabled(root: Path | None = None, text: str | None = None) -> set[str]:
    """꺼 둔 주제 이름들. text 를 주면 그 글(GitHub 에서 받은 파일 내용)을 읽음."""
    try:
        j = json.loads(text) if text is not None else json.loads(((root or ROOT) / "studio" / "state" / "topics.json").read_text("utf-8"))
    except (OSError, json.JSONDecodeError, TypeError):
        return set()
    return {str(t) for t in (j.get("disabled") or []) if isinstance(t, str)}


def is_disabled(topic: str, root: Path | None = None) -> bool:
    return topic in disabled(root)


def filter_topics(names, root: Path | None = None) -> list[str]:
    off = disabled(root)
    return [n for n in names if n not in off]


def guard(topic: str, tool: str = "", force: bool = False) -> None:
    """꺼 둔 주제면 멈춤 (force 면 경고만)."""
    if topic and is_disabled(topic):
        msg = (f"[TOPIC] ⏸ '{topic}' 은(는) 제작 판에서 꺼 둔 주제 (studio/state/topics.json) — {tool or '이 도구'} 가 읽지도 작업하지도 않음. "
               f"다시 쓰려면 사용자가 판 '공통 › 주제 켜기·끄기'에서 켜고 Claude 가 동기화")
        if force:
            print(msg + " · --force 라 계속", file=sys.stderr)
            return
        raise SystemExit(msg)


if __name__ == "__main__":
    off = disabled()
    if len(sys.argv) > 1:
        print(f"[TOPIC] topic={sys.argv[1]} disabled={sys.argv[1] in off}")
        raise SystemExit(3 if sys.argv[1] in off else 0)
    print(f"[TOPIC] disabled={','.join(sorted(off)) or '-'} file={STATE_FILE.relative_to(ROOT)}")
