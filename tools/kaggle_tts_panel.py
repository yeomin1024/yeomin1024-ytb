#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-10-24 — 사용자 지시 "오디오 코드 경로 선택하면 대본도 선택할 수 있게 수정해": 주제를 고르면 그 주제의
#          대본(롱폼·쇼츠) 체크 상자가 나오고, 고른 대본만 all --ids 로 만든다 (하나도 안 고르면 그 주제 전체 — 예전과 같음).
#          대본마다 지금 상태(오디오 없음 → 만듦 · 옛 대본 → 다시 만듦 · 있음/업로드함/NO_TTS → 건너뜀)를 tts_narration 규칙 그대로 보여 줌.
#          대본 수에 쇼츠도 셈(all 이 쇼츠도 만들므로). 안내 글의 진행자 목소리는 voices/host.json 의 고른 목소리(picked.id)로.
# (v1.0) — 2026-10-15 — 사용자 지시 "오디오를 생성할 경로를 전체 경로 또는 economic 같은 단일 주제 경로를 버튼으로
#          선택할수 있게해 디폴트는 전체야": Kaggle 노트북에 범위 버튼(전체 · 주제 폴더) + [▶ 오디오 만들기] 버튼
r"""
Kaggle 노트북 셀(guides/tts_guide.md 3번)에서 오디오를 만들 범위를 버튼으로 고른다. 기본은 '전체'.

  import sys; sys.path.insert(0, "/kaggle/working/yeomin1024-ytb/tools")
  import importlib, kaggle_tts_panel; importlib.reload(kaggle_tts_panel).panel()

  - 범위 버튼: 전체(모든 주제 폴더) · economic · …  (대본 <주제>/source/<영상ID>/<영상ID>.txt ·
                <영상ID>/shorts/<영상ID>-shorts.txt 가 있는 폴더만, 대본 수 표시)
  - 대본 고르기 (v1.1): 주제를 누르면 그 주제의 대본 체크 상자가 나온다 — 하나도 안 고르면 주제 전체, 고르면 그 대본만
  - [▶ 오디오 만들기]: python tools/tts_narration.py all --push                       (전체)
                       python tools/tts_narration.py all --push --topics 주제            (주제 하나)
                       python tools/tts_narration.py all --push --topics 주제 --ids 영상ID,… (고른 대본만)
  - [목록만 보기]: 같은 범위로 all --dry-run (모델을 불러오지 않고 무엇을 만들지)
  - 로그는 버튼 아래 칸과 /kaggle/working/tts_panel.log 에 함께 남는다 (탭을 닫아도 파일에 남음)

위젯이 없는 곳(터미널)에서는 버튼 대신:
  python tools/kaggle_tts_panel.py                    # 전체
  python tools/kaggle_tts_panel.py --topic economic   # 주제 하나
  python tools/kaggle_tts_panel.py --topic test --ids myeonse-hwangeup-2026-10,myeonse-hwangeup-2026-10-shorts   # 고른 대본만
  python tools/kaggle_tts_panel.py --list             # 범위 목록만
  python tools/kaggle_tts_panel.py --topic test --list   # 그 주제의 대본과 상태
※ 연구·교육용 도구다. 영상 내용은 투자 권유가 아니다.
"""
import argparse
import json
import shlex
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ALL = "전체"
LOG_FILE = Path("/kaggle/working/tts_panel.log") if Path("/kaggle/working").is_dir() else ROOT / "output" / "tts_panel.log"
SHORTS_SUFFIX = "-shorts"
# tts_narration.repo_status 상태 → (지금 상태, all 이 할 일)
STATUS = {"todo": ("오디오 없음", "만듦"), "stale": ("옛 대본으로 만든 오디오", "다시 만듦"),
          "has_audio": ("오디오 있음", "건너뜀"), "uploaded": ("업로드함", "건너뜀"), "no_tts": ("NO_TTS", "건너뜀")}


def script_files(topic_dir):
    """주제 폴더 하나의 대본 → [(영상ID, 롱폼|쇼츠, TXT)] — tts_narration.script_entries 와 같은 규칙, 롱폼 바로 뒤에 짝 쇼츠."""
    src = Path(topic_dir) / "source"
    out = [(t.stem, "롱폼", t) for t in src.glob("*/*.txt") if t.stem == t.parent.name]
    out += [(t.stem, "쇼츠", t) for t in src.glob("*/shorts/*.txt") if t.stem == t.parents[1].name + SHORTS_SUFFIX]
    return sorted(out, key=lambda x: (x[0][:-len(SHORTS_SUFFIX)] if x[1] == "쇼츠" else x[0], x[1] != "롱폼"))


def topics(root=ROOT):
    """대본이 있는 주제 폴더 → [(이름, 대본 수)]. 대본 수 = 롱폼 + 쇼츠 (all 이 둘 다 만듦, v1.1)."""
    out = []
    for d in sorted(p for p in root.iterdir() if p.is_dir() and not p.name.startswith(".")):
        if (d / "source").is_dir():
            n = len(script_files(d))
            if n:
                out.append((d.name, n))
    return out


def _status_reader(root):
    """저장소 상태를 읽는 함수 (tts_narration 규칙 그대로) — 저장소가 아니거나 불러오지 못하면 None (상태 '?')."""
    if Path(root).resolve() != ROOT:
        return None
    try:
        sys.path.insert(0, str(ROOT / "tools"))
        import tts_narration as T
    except Exception as e:                     # numpy 등이 없는 곳 — 목록만 보여 줌
        print(f"[PANEL] level=warning stage=status error={e} note=대본 상태 없이 목록만")
        return None

    def read(topic, vid, txt):
        try:
            rows, cards = T.read_script(txt)
            return T.repo_status(topic, vid, rows, cards)[0]
        except Exception as e:
            print(f"[PANEL] level=warning stage=status video={vid} error={e}")
            return "?"
    return read


def scripts(topic, root=ROOT):
    """주제 하나의 대본 목록 → [{id, kind, status, label}] — 체크 상자 이름표에 지금 상태와 all 이 할 일."""
    read = _status_reader(root)
    out = []
    for vid, kind, txt in script_files(Path(root) / topic):
        st = read(topic, vid, txt) if read else "?"
        now, todo = STATUS.get(st, ("상태 모름", "all 이 판단"))
        out.append({"id": vid, "kind": kind, "status": st, "label": f"{vid} · {kind} · {now} → {todo}"})
    return out


def host_voice(root=ROOT):
    """안내 글에 쓸 진행자 목소리 이름 (voices/host.json 의 picked.id, 없으면 '진행자')."""
    try:
        return json.loads((Path(root) / "voices" / "host.json").read_text("utf-8"))["picked"]["id"]
    except Exception:
        return "진행자"


def command(scope, extra=(), ids=None):
    """범위 → tts_narration.py all 명령 (전체면 --topics 없음, 고른 대본이 있으면 --ids)."""
    cmd = [sys.executable, str(ROOT / "tools" / "tts_narration.py"), "all", *extra]
    if scope and scope != ALL:
        cmd += ["--topics", scope]
    if ids:
        cmd += ["--ids", ",".join(ids)]
    return cmd


def run(scope, extra=("--push",), write=print, ids=None):
    """명령을 돌리며 한 줄씩 write 로 넘기고 로그 파일에도 남긴다 → 종료 코드."""
    cmd = command(scope, extra, ids)
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    with LOG_FILE.open("a", encoding="utf-8") as lf:
        def emit(line):
            write(line)
            lf.write(line + "\n")
            lf.flush()
        emit(f"[PANEL] {time.strftime('%Y-%m-%d %H:%M:%S')} scope={scope or ALL} ids={','.join(ids) if ids else '(주제 전체)'} cmd={' '.join(shlex.quote(c) for c in cmd[1:])} log={LOG_FILE}")
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
    picks = []                                 # [(영상ID, 체크 상자)] — 지금 고른 주제의 대본
    pick = W.ToggleButtons(options=[(f"{ALL} (대본 {total}개)", ALL)] + [(f"{t} (대본 {n}개)", t) for t, n in ts],
                           value=ALL, style={"button_width": "auto"}, tooltips=["모든 주제 폴더"] + [f"{t}/source/ 만" for t, _ in ts])
    go = W.Button(description="오디오 만들기", button_style="success", icon="play", layout=W.Layout(width="200px"))
    dry = W.Button(description="목록만 보기", icon="list", layout=W.Layout(width="140px"))
    out = W.Output(layout=W.Layout(border="1px solid #cfd6e2", max_height="520px", overflow="auto", padding="6px"))
    note = W.HTML("<b>오디오를 만들 범위</b> — 기본은 <b>전체</b>(모든 주제). 주제 하나만 만들려면 그 버튼을 누른 뒤 "
                  "<b>오디오 만들기</b>. 주제를 누르면 <b>그 주제의 대본</b>이 나온다 — 하나도 안 고르면 주제 전체, 고르면 고른 대본만. "
                  f"진행자 목소리({host_voice()}) 하나로 읽고, 영상마다 대본 폴더에 올린다.")
    box = W.VBox(children=[])

    def fill(topic):
        """주제가 바뀌면 대본 체크 상자를 다시 (전체면 안내 글만)."""
        picks.clear()
        if topic == ALL:
            box.children = [W.HTML("<i>주제를 고르면 그 주제의 대본을 고를 수 있다 (전체는 모든 대본).</i>")]
            return
        rows = scripts(topic)
        for r in rows:
            picks.append((r["id"], W.Checkbox(value=False, description=r["label"], indent=False, layout=W.Layout(width="auto"))))
        box.children = [W.HTML(f"<b>{topic} 대본 {len(rows)}개</b> — 하나도 안 고르면 이 주제 전체, 고르면 고른 대본만 "
                               "('건너뜀'은 골라도 all 이 만들지 않음)")] + [cb for _, cb in picks]

    pick.observe(lambda ch: fill(ch["new"]), names="value")
    fill(pick.value)

    def start(extra_args):
        def handler(_):
            ws = [pick, go, dry] + [cb for _, cb in picks]
            for w in ws:
                w.disabled = True
            try:
                with out:
                    run(pick.value, extra_args, write=print, ids=[v for v, cb in picks if cb.value] or None)
            finally:
                for w in ws:
                    w.disabled = False
        return handler

    go.on_click(start(extra))
    dry.on_click(start(("--dry-run",)))
    display(W.VBox(children=[note, pick, box, W.HBox(children=[go, dry]), out]))
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description="오디오를 만들 범위(전체 / 주제 하나)를 골라 tts_narration.py all 실행 — 버튼이 없는 곳용")
    ap.add_argument("--topic", default=ALL, help=f"주제 폴더 하나 (기본: {ALL})")
    ap.add_argument("--ids", default=None, help="이 대본만 (영상ID 쉼표로 — 쇼츠는 <영상ID>-shorts). 없으면 주제 전체")
    ap.add_argument("--list", action="store_true", help="범위 목록만 (--topic 과 함께면 그 주제의 대본과 상태)")
    ap.add_argument("--dry-run", action="store_true", help="무엇을 만들지 목록만 (all --dry-run)")
    a = ap.parse_args(argv)
    ts = topics()
    if a.topic != ALL and a.topic not in {t for t, _ in ts}:
        print(f"[PANEL] level=error topic={a.topic} reason=대본이 있는 주제 폴더가 아님 next=--list 로 확인 ({', '.join(t for t, _ in ts)})")
        return 2
    if a.list:
        if a.topic == ALL:
            print(f"[PANEL] scopes={ALL}," + ",".join(f"{t}({n})" for t, n in ts))
        else:
            for r in scripts(a.topic):
                print(f"[PANEL] topic={a.topic} script={r['id']} kind={r['kind']} status={r['status']} label=\"{r['label']}\"")
        return 0
    ids = [v.strip() for v in (a.ids or "").split(",") if v.strip()]
    if ids:
        known = {vid for t, _ in ts if a.topic in (ALL, t) for vid, _, _ in script_files(ROOT / t)}
        bad = [v for v in ids if v not in known]
        if bad:
            print(f"[PANEL] level=error ids={','.join(bad)} reason=이 범위에 없는 대본 next=--topic <주제> --list 로 확인")
            return 2
    return run(a.topic, ("--dry-run",) if a.dry_run else ("--push",), ids=ids or None)


if __name__ == "__main__":
    sys.exit(main())
