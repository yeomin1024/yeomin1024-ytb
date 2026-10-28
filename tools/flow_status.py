#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-28 — 최초. 새 세션이 문서를 읽지 않고 '분석 → 주제 탐색 → 요약본 → 대본' 어디까지 됐고 다음에 무엇을 돌릴지 한 번에 보게
#          (사용자 지시 2026-10-28 "유튜브 분석에서 요약본까지 생성하는 과정을 토큰 가장 아낄 수 있는 구조로 해서 처음 생성한 세션이 똑같이 진행할 수
#          있도록 지시사항 파일을 만들어" — 지시사항 `stock/guides/quick_flow.md`).
#
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.0 | 2026-10-28 | 최초 — 단계표(결과 파일·앞 단계)·git 시각 비교·편마다 진행 | stamp · step_rows · episode_rows · main |
#
# 실행: python3 tools/flow_status.py stock          (economic · history 도 같은 꼴 — 폴더 구조가 같음)
#       python3 tools/flow_status.py stock --json   (기계용)
# 읽기만 한다 (네트워크·할당량 0 · 파일을 고치지 않음). 시각 = 그 파일의 마지막 커밋 시각 (커밋 안 된 변경이 있으면 파일 수정 시각).
# '다시?' = 앞 단계 결과가 이 단계 결과보다 새것 — 같은 커밋에 함께 올라간 것은 같은 시각이라 '다시?'가 아님.
# ※ 연구·교육용 — 투자 권유가 아님.
import argparse
import glob
import json
import logging
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VERSION = "v1.0"
EXPLORE_MAX_DAYS = 7      # 탐색 캐시가 이보다 오래되면 explore 권함 (검색 캐시 7일~ — stock/README.md '클라우드에서 분석')

# (번호, 이름, 결과 파일(주제 폴더 기준 glob), 앞 단계 입력(glob 목록), 다음에 돌릴 것)
STEPS = [
    (1, "탐색", "cloud_cache/cache.json", [], "python3 tools/cloud_run.py {t} explore --weeks 26 · 이어서 --shorts"),
    (2, "승인·분석", "result/outliers/analysis.md", ["cloud_cache/cache.json"],
     "python3 tools/cloud_run.py {t} list --checked → 주제 밖 uncheck → approve → analyze"),
    (3, "확인 엑셀", "result/outliers/target_check.md", ["result/outliers/analysis.md"], "python3 tools/target_check.py {t}"),
    (4, "페르소나", "result/outliers/personas.md", ["result/outliers/analysis.md"], "python3 tools/personas.py {t}  (analyze 끝에 저절로)"),
    (5, "댓글 유형", "result/outliers/comment_types.md", ["result/outliers/analysis.md"], "python3 tools/comment_types.py {t} report"),
    (6, "댓글 묶음", "result/outliers/comment_clusters.md", ["result/outliers/analysis.md"], "python3 tools/comment_clusters.py {t}"),
    (7, "댓글 니즈", "result/outliers/comment_titles.md", ["result/outliers/analysis.md", "result/outliers/comment_title_picks.tsv"],
     "python3 tools/comment_title_ideas.py {t} candidates → Claude 가 comment_title_picks.tsv → match"),
    (8, "콘텐츠 엑셀", "result/outliers/content_analysis.md", ["result/outliers/analysis.md", "result/outliers/thumb_codes.tsv"],
     "새 성공 사례 썸네일을 thumb_codes.tsv 에 → python3 tools/content_analysis.py {t}"),
    (9, "대본 받을 목록", "result/outliers/transcript_todo.md", ["result/outliers/analysis.md"], "python3 tools/pc_transcribe.py list {t}"),
    (10, "주제 탐색", "topics/주제탐색.md",
     ["result/outliers/personas.md", "result/outliers/comment_titles.md", "guides/channel.md", "topics/평가.txt", "topics/pool/*.json"],
     "python3 tools/topic_ideas.py {t} status  ('갱신 필요'면 material → pool/<날짜>.json → add)"),
    (11, "요약본", "topics/요약본_material.md", ["source/*/요약본_안.json", "topics/요약본_평가.txt", "topics/주제탐색.md"],
     "python3 tools/summary_ideas.py {t} status"),
]


class StageFormatter(logging.Formatter):
    def format(self, record):
        return f"[{getattr(record, 'stage', 'FLOW')}] [{self.formatTime(record, '%Y-%m-%dT%H:%M:%S')}] {record.getMessage()}"


log = logging.getLogger("flow_status")


def out(stage, **kv):
    log.info(" ".join(f"{k}={v}" for k, v in kv.items()), extra={"stage": stage})


def _git(*args):
    try:
        return subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True, timeout=60).stdout
    except (OSError, subprocess.SubprocessError) as e:
        log.warning(f"git={' '.join(args)} error={e!r} next_step=git 이 되는지 확인", extra={"stage": "LOAD"})
        return ""


def stamp(paths, dirty):
    """여러 파일 중 가장 새 시각 (초). 커밋 안 된 변경·새 파일이면 수정 시각. 없으면 None."""
    best = None
    for p in paths:
        rel = str(Path(p).relative_to(ROOT))
        if rel in dirty or not _git("ls-files", rel).strip():
            t = Path(p).stat().st_mtime
        else:
            s = _git("log", "-1", "--format=%ct", "--", rel).strip()
            t = float(s) if s else Path(p).stat().st_mtime
        best = t if best is None else max(best, t)
    return best


def expand(topic, pattern):
    return sorted(glob.glob(str(ROOT / topic / pattern)))


def fmt_t(t):
    return datetime.fromtimestamp(t, tz=timezone.utc).strftime("%m-%d %H:%M") if t else "없음"


def step_rows(topic, dirty, now):
    rows = []
    for no, name, outp, ins, cmd in STEPS:
        files = expand(topic, outp)
        t_out = stamp(files, dirty) if files else None
        t_in = max([x for x in (stamp(expand(topic, g), dirty) for g in ins) if x is not None], default=None)
        if t_out is None:
            state = "없음"
        elif no == 1 and (now - t_out) / 86400 > EXPLORE_MAX_DAYS:
            state = f"오래됨 ({(now - t_out) / 86400:.0f}일)"
        elif t_in is not None and t_in > t_out:
            state = f"다시? (앞 단계가 {(t_in - t_out) / 3600:.1f}시간 새것)"
        else:
            state = "✅"
        rows.append(dict(no=no, step=name, file=f"{topic}/{outp}", updated=fmt_t(t_out), state=state, cmd=cmd.format(t=topic)))
    return rows


def episode_rows(topic):
    eps = []
    for d in sorted((ROOT / topic / "source").glob("*/")):
        has_sum = (d / "요약본.txt").exists()
        if not (has_sum or (d / "요약본_안.json").exists()):
            continue
        txt = (d / "요약본.txt").read_text(encoding="utf-8") if has_sum else ""
        marks = sum(1 for ln in txt.splitlines() if "=>" in ln and not ln.lstrip().startswith("#"))
        script = d / f"{d.name}.txt"
        e = dict(id=d.name, summary="✅" if has_sum else "✗", marks=marks, calc="✅" if (d / "calc" / "calc.py").exists() else "✗",
                 script="✅" if script.exists() else "✗", persona_review="✅" if (d / "persona_review.md").exists() else "✗",
                 audio="✅" if (d / "narration.mp3").exists() else "✗")
        if not script.exists():
            todo = "대본" if e["calc"] == "✅" else "calc → 대본"
            e["next"] = f"사용자 평가(=> 좋음) 또는 안 고름 → {todo}" if marks == 0 else f"고른 안으로 {todo}"
        elif e["persona_review"] == "✗":
            e["next"] = f"python3 tools/persona_review.py {topic} {script.relative_to(ROOT)}"
        elif e["audio"] == "✗":
            e["next"] = "사용자 Kaggle 오디오 (tts_narration.py all --push)"
        elif not (ROOT / "video" / "episodes" / d.name / "index.html").exists():
            e["next"] = "영상 장면 코드 (guides/video_guide.md)"
        else:
            e["next"] = "렌더 점검 → 썸네일 → 업로드 (guides/upload_guide.md)"
        eps.append(e)
    return eps


def main():
    ap = argparse.ArgumentParser(description="분석 → 요약본 → 대본 진행 한눈에 (읽기만)")
    ap.add_argument("topic", nargs="?", default="stock")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--log-level", default="WARNING", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args()
    h = logging.StreamHandler(sys.stderr)
    h.setFormatter(StageFormatter())
    log.addHandler(h)
    log.setLevel(a.log_level)
    t0 = time.time()
    if not (ROOT / a.topic).is_dir():
        log.error(f"topic={a.topic} error=폴더 없음 next_step=주제 이름 확인 (stock·economic·history)", extra={"stage": "LOAD"})
        raise SystemExit(1)
    dirty = {ln[3:].strip().strip('"') for ln in _git("status", "--porcelain").splitlines()}
    now = time.time()
    rows, eps = step_rows(a.topic, dirty, now), episode_rows(a.topic)
    nxt = next((r for r in rows if r["state"] != "✅"), None)
    if a.json:
        print(json.dumps({"version": VERSION, "topic": a.topic, "steps": rows, "episodes": eps, "next": nxt}, ensure_ascii=False, indent=1))
    else:
        print(f"# {a.topic} 진행 — flow_status {VERSION} · {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC (시각 = 마지막 커밋, UTC)")
        for r in rows:
            print(f"{r['no']:>2} {r['step']:<8} {r['updated']:<11} {r['state']:<26} {r['file']}")
        print("\n편 (source/): 요약본 · 평가(=>) · calc · 대본 · 페르소나 검사 · 오디오 → 다음")
        for e in eps:
            print(f"  {e['id']:<26} {e['summary']} · {e['marks']} · {e['calc']} · {e['script']} · {e['persona_review']} · {e['audio']} → {e['next']}")
        print(f"\n다음 단계: {nxt['no']} {nxt['step']} — {nxt['cmd']}" if nxt else "\n다음 단계: 분석~요약본 모두 최신 — 편 줄의 '다음'을 보거나 사용자 평가를 가져온다")
        print("평가판(사용자가 누른 좋음·나쁨)은 이 도구가 못 읽음 → quick_flow.md 3번 (ArtifactData list → import)")
    out("DONE", topic=a.topic, steps=len(rows), episodes=len(eps), next=nxt["no"] if nxt else "-", seconds=f"{time.time() - t0:.1f}")


if __name__ == "__main__":
    main()
