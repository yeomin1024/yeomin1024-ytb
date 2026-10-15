#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-15 — 사용자 지시 "오디오를 생성할 경로를 전체 경로 또는 economic 같은 단일 주제 경로를 버튼으로
#          선택할수 있게해 디폴트는 전체야": Kaggle 노트북에 범위 버튼(전체 · 주제 폴더) + [▶ 오디오 만들기] 버튼
r"""
Kaggle 노트북 셀(guides/tts_guide.md 3번)에서 오디오를 만들 범위를 버튼으로 고른다. 기본은 '전체'.

  import sys; sys.path.insert(0, "/kaggle/working/yeomin1024-ytb/tools")
  import importlib, kaggle_tts_panel; importlib.reload(kaggle_tts_panel).panel()

  - 범위 버튼: 전체(모든 주제 폴더) · economic · …  (대본 <주제>/source/<영상ID>/<영상ID>.txt 가 있는 폴더만, 대본 수 표시)
  - [▶ 오디오 만들기]: python tools/tts_narration.py all --push            (전체)
                       python tools/tts_narration.py all --push --topics 주제 (주제 하나)
  - [목록만 보기]: 같은 범위로 all --dry-run (모델을 불러오지 않고 무엇을 만들지)
  - 로그는 버튼 아래 칸과 /kaggle/working/tts_panel.log 에 함께 남는다 (탭을 닫아도 파일에 남음)

위젯이 없는 곳(터미널)에서는 버튼 대신:
  python tools/kaggle_tts_panel.py                    # 전체
  python tools/kaggle_tts_panel.py --topic economic   # 주제 하나
  python tools/kaggle_tts_panel.py --list             # 범위 목록만
※ 연구·교육용 도구다. 영상 내용은 투자 권유가 아니다.
"""
import argparse
import shlex
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ALL = "전체"
LOG_FILE = Path("/kaggle/working/tts_panel.log") if Path("/kaggle/working").is_dir() else ROOT / "output" / "tts_panel.log"


def topics(root=ROOT):
    """대본이 있는 주제 폴더 → [(이름, 대본 수)]. 대본 = <주제>/source/<영상ID>/<영상ID>.txt (tts_narration.discover 와 같은 규칙)."""
    out = []
    for d in sorted(p for p in root.iterdir() if p.is_dir() and not p.name.startswith(".")):
        src = d / "source"
        if src.is_dir():
            n = sum(1 for t in src.glob("*/*.txt") if t.stem == t.parent.name)
            if n:
                out.append((d.name, n))
    return out


def command(scope, extra=()):
    """범위 → tts_narration.py all 명령 (전체면 --topics 없음)."""
    cmd = [sys.executable, str(ROOT / "tools" / "tts_narration.py"), "all", *extra]
    if scope and scope != ALL:
        cmd += ["--topics", scope]
    return cmd


def run(scope, extra=("--push",), write=print):
    """명령을 돌리며 한 줄씩 write 로 넘기고 로그 파일에도 남긴다 → 종료 코드."""
    cmd = command(scope, extra)
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    with LOG_FILE.open("a", encoding="utf-8") as lf:
        def emit(line):
            write(line)
            lf.write(line + "\n")
            lf.flush()
        emit(f"[PANEL] {time.strftime('%Y-%m-%d %H:%M:%S')} scope={scope or ALL} cmd={' '.join(shlex.quote(c) for c in cmd[1:])} log={LOG_FILE}")
        try:
            p = subprocess.Popen(cmd, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
        except OSError as e:
            emit(f"[PANEL] level=error stage=start error={e} next=저장소 경로·파이썬 확인 ({ROOT})")
            return 1
        for line in p.stdout:
            emit(line.rstrip("\n"))
        rc = p.wait()
        emit(f"[PANEL] done scope={scope or ALL} exit={rc} minutes={(time.time() - t0) / 60:.1f}"
             + ("" if rc == 0 else " next=위 [ERROR] 줄 확인 뒤 같은 버튼을 다시 (이미 올라간 영상은 건너뜀)"))
    return rc


def panel(extra=("--push",)):
    """Kaggle·Jupyter: 범위 버튼(기본 전체) + 만들기·목록 버튼. ipywidgets 가 없으면 기본(전체)으로 바로 실행."""
    try:
        import ipywidgets as W
        from IPython.display import display
    except ImportError:
        print("[PANEL] ipywidgets 없음 → 버튼 없이 기본 범위(전체)로 바로 실행")
        return run(ALL, extra)
    ts = topics()
    total = sum(n for _, n in ts)
    pick = W.ToggleButtons(options=[(f"{ALL} (대본 {total}개)", ALL)] + [(f"{t} (대본 {n}개)", t) for t, n in ts],
                           value=ALL, style={"button_width": "auto"}, tooltips=["모든 주제 폴더"] + [f"{t}/source/ 만" for t, _ in ts])
    go = W.Button(description="오디오 만들기", button_style="success", icon="play", layout=W.Layout(width="200px"))
    dry = W.Button(description="목록만 보기", icon="list", layout=W.Layout(width="140px"))
    out = W.Output(layout=W.Layout(border="1px solid #cfd6e2", max_height="520px", overflow="auto", padding="6px"))
    note = W.HTML("<b>오디오를 만들 범위</b> — 기본은 <b>전체</b>(모든 주제). 주제 하나만 만들려면 그 버튼을 누른 뒤 "
                  "<b>오디오 만들기</b>. 진행자 목소리(H04) 하나로 읽고, 영상마다 대본 폴더에 올린다.")

    def start(extra_args):
        def handler(_):
            for w in (pick, go, dry):
                w.disabled = True
            try:
                with out:
                    run(pick.value, extra_args, write=print)
            finally:
                for w in (pick, go, dry):
                    w.disabled = False
        return handler

    go.on_click(start(extra))
    dry.on_click(start(("--dry-run",)))
    display(W.VBox([note, pick, W.HBox([go, dry]), out]))
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description="오디오를 만들 범위(전체 / 주제 하나)를 골라 tts_narration.py all 실행 — 버튼이 없는 곳용")
    ap.add_argument("--topic", default=ALL, help=f"주제 폴더 하나 (기본: {ALL})")
    ap.add_argument("--list", action="store_true", help="범위 목록만")
    ap.add_argument("--dry-run", action="store_true", help="무엇을 만들지 목록만 (all --dry-run)")
    a = ap.parse_args(argv)
    ts = topics()
    if a.list:
        print(f"[PANEL] scopes={ALL}," + ",".join(f"{t}({n})" for t, n in ts))
        return 0
    if a.topic != ALL and a.topic not in {t for t, _ in ts}:
        print(f"[PANEL] level=error topic={a.topic} reason=대본이 있는 주제 폴더가 아님 next=--list 로 확인 ({', '.join(t for t, _ in ts)})")
        return 2
    return run(a.topic, ("--dry-run",) if a.dry_run else ("--push",))


if __name__ == "__main__":
    sys.exit(main())
