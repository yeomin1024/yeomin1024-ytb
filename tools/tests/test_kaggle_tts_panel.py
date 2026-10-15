# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-15 — tools/kaggle_tts_panel.py v1.0 시험 (가짜 위젯·가짜 저장소 — GPU·네트워크·GitHub 올리기 없음)
r"""
  python3 -m unittest tools.tests.test_kaggle_tts_panel -v     (저장소 최상위에서)

- 범위 목록: 대본(<주제>/source/<영상ID>/<영상ID>.txt)이 있는 폴더만, 대본 수
- 명령: 전체 = --topics 없음, 주제 하나 = --topics 주제
- 버튼: 기본값이 '전체', [오디오 만들기]·[목록만 보기]가 고른 범위로 실행하고 실행 중에는 버튼을 잠금
"""
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest import mock

TOOLS = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(TOOLS))
import kaggle_tts_panel as kp  # noqa: E402


class FakeWidget:
    def __init__(self, *a, **k):
        self.__dict__.update(k)
        self.disabled = False
        self._click = None
    def on_click(self, fn):
        self._click = fn
    def click(self):
        self._click(self)
    def __enter__(self):
        return self
    def __exit__(self, *a):
        return False


def fake_modules(shown):
    W = types.ModuleType("ipywidgets")
    for name in ("ToggleButtons", "Button", "Output", "HTML", "VBox", "HBox", "Layout"):
        setattr(W, name, type(name, (FakeWidget,), {}))
    W.VBox = lambda children, **k: shown.append(children) or FakeWidget()
    disp = types.ModuleType("IPython.display")
    disp.display = lambda x: None
    ip = types.ModuleType("IPython"); ip.display = disp
    return {"ipywidgets": W, "IPython": ip, "IPython.display": disp}


class PanelTest(unittest.TestCase):
    def test_topics_only_folders_with_scripts(self):
        with tempfile.TemporaryDirectory() as td:
            r = Path(td)
            (r / "economic" / "source" / "a-1").mkdir(parents=True); (r / "economic" / "source" / "a-1" / "a-1.txt").write_text("x")
            (r / "economic" / "source" / "b-1").mkdir(parents=True); (r / "economic" / "source" / "b-1" / "note.txt").write_text("x")  # 이름이 달라 대본 아님
            (r / "guides").mkdir(); (r / ".git" / "source").mkdir(parents=True)
            self.assertEqual(kp.topics(r), [("economic", 1)])

    def test_command_scope(self):
        self.assertNotIn("--topics", kp.command(kp.ALL, ("--push",)))
        cmd = kp.command("economic", ("--push",))
        self.assertEqual(cmd[-2:], ["--topics", "economic"])
        self.assertIn("all", cmd); self.assertIn("--push", cmd)

    def test_click_runs_selected_scope(self):
        shown, calls = [], []
        mods = fake_modules(shown)
        mods["ipywidgets"].HBox = lambda children, **k: FakeWidget(children=children)
        with mock.patch.dict(sys.modules, mods), mock.patch.object(kp, "topics", return_value=[("economic", 4)]):
            def fake_run(scope, extra, write=print):
                note, pick, row, out = shown[0]
                calls.append((scope, tuple(extra), pick.disabled))      # 실행 중에는 버튼이 잠김
                return 0
            with mock.patch.object(kp, "run", side_effect=fake_run):
                kp.panel(extra=("--push",))
                note, pick, row, out = shown[0]
                self.assertEqual(pick.value, kp.ALL)                     # 기본 = 전체
                self.assertEqual([v for _, v in pick.options], [kp.ALL, "economic"])
                go, dry = row.children
                go.click()                                              # 기본(전체)로 만들기
                pick.value = "economic"; dry.click()                    # economic 목록만
                self.assertFalse(pick.disabled)                          # 끝나면 다시 풀림
        self.assertEqual(calls, [(kp.ALL, ("--push",), True), ("economic", ("--dry-run",), True)])


if __name__ == "__main__":
    unittest.main()
