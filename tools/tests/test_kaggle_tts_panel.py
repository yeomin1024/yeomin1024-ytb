# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-10-24 — kaggle_tts_panel v1.1 (대본 고르기) 시험 더함: 주제를 고르면 대본 체크 상자, 고른 대본만 --ids,
#          하나도 안 고르면 주제 전체(--ids 없음), 대본 수에 쇼츠도 셈, 롱폼 바로 뒤 짝 쇼츠, CLI --ids 검사.
# (v1.0) — 2026-10-15 — tools/kaggle_tts_panel.py v1.0 시험 (가짜 위젯·가짜 저장소 — GPU·네트워크·GitHub 올리기 없음)
r"""
  python3 -m unittest tools.tests.test_kaggle_tts_panel -v     (저장소 최상위에서)

- 범위 목록: 대본(<주제>/source/<영상ID>/<영상ID>.txt · <영상ID>/shorts/<영상ID>-shorts.txt)이 있는 폴더만, 대본 수
- 명령: 전체 = --topics 없음, 주제 하나 = --topics 주제, 고른 대본 = --ids
- 버튼: 기본값이 '전체', 주제를 고르면 대본 체크 상자, [오디오 만들기]·[목록만 보기]가 고른 범위·대본으로 실행하고 실행 중에는 잠금
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
        self._obs = []
    def on_click(self, fn):
        self._click = fn
    def click(self):
        self._click(self)
    def observe(self, fn, names=None):
        self._obs.append(fn)
    def set(self, value):                      # 사용자가 누른 것처럼 값 바꾸고 알림
        self.value = value
        for fn in self._obs:
            fn({"new": value})
    def __enter__(self):
        return self
    def __exit__(self, *a):
        return False


def fake_modules(shown):
    W = types.ModuleType("ipywidgets")
    for name in ("ToggleButtons", "Button", "Output", "HTML", "Checkbox", "HBox", "Layout"):
        setattr(W, name, type(name, (FakeWidget,), {}))
    W.VBox = lambda children=(), **k: FakeWidget(children=children)
    disp = types.ModuleType("IPython.display")
    disp.display = lambda x: shown.append(x)
    ip = types.ModuleType("IPython"); ip.display = disp
    return {"ipywidgets": W, "IPython": ip, "IPython.display": disp}


def make_repo(r):
    for vid in ("a-1", "b-2"):
        (r / "economic" / "source" / vid / "shorts").mkdir(parents=True)
        (r / "economic" / "source" / vid / f"{vid}.txt").write_text("x")
    (r / "economic" / "source" / "a-1" / "shorts" / "a-1-shorts.txt").write_text("x")
    (r / "economic" / "source" / "b-2" / "note.txt").write_text("x")                     # 이름이 달라 대본 아님
    (r / "economic" / "source" / "b-2" / "shorts" / "other-shorts.txt").write_text("x")  # 폴더 이름과 달라 대본 아님
    (r / "guides").mkdir(); (r / ".git" / "source").mkdir(parents=True)


class PanelTest(unittest.TestCase):
    def test_topics_count_long_and_shorts(self):
        with tempfile.TemporaryDirectory() as td:
            r = Path(td); make_repo(r)
            self.assertEqual(kp.topics(r), [("economic", 3)])
            self.assertEqual([(v, k) for v, k, _ in kp.script_files(r / "economic")],
                             [("a-1", "롱폼"), ("a-1-shorts", "쇼츠"), ("b-2", "롱폼")])   # 롱폼 바로 뒤 짝 쇼츠

    def test_scripts_outside_repo_have_unknown_status(self):
        with tempfile.TemporaryDirectory() as td:
            r = Path(td); make_repo(r)
            rows = kp.scripts("economic", r)
            self.assertEqual([x["status"] for x in rows], ["?", "?", "?"])
            self.assertIn("a-1-shorts · 쇼츠", rows[1]["label"])

    def test_command_scope_and_ids(self):
        self.assertNotIn("--topics", kp.command(kp.ALL, ("--push",)))
        cmd = kp.command("economic", ("--push",))
        self.assertEqual(cmd[-2:], ["--topics", "economic"])
        self.assertIn("all", cmd); self.assertIn("--push", cmd); self.assertNotIn("--ids", cmd)
        cmd = kp.command("economic", ("--push",), ids=["a-1", "a-1-shorts"])
        self.assertEqual(cmd[-4:], ["--topics", "economic", "--ids", "a-1,a-1-shorts"])

    def test_click_runs_selected_scope_and_scripts(self):
        shown, calls = [], []
        rows = [{"id": "a-1", "kind": "롱폼", "status": "todo", "label": "a-1 · 롱폼 · 오디오 없음 → 만듦"},
                {"id": "a-1-shorts", "kind": "쇼츠", "status": "stale", "label": "a-1-shorts · 쇼츠 · 옛 대본 → 다시 만듦"}]
        with mock.patch.dict(sys.modules, fake_modules(shown)), \
                mock.patch.object(kp, "topics", return_value=[("economic", 2)]), \
                mock.patch.object(kp, "scripts", return_value=rows):
            def fake_run(scope, extra, write=print, ids=None):
                note, pick, box, row, out = shown[0].children
                calls.append((scope, tuple(extra), ids, pick.disabled, all(cb.disabled for cb in box.children[1:])))
                return 0
            with mock.patch.object(kp, "run", side_effect=fake_run):
                kp.panel(extra=("--push",))
                note, pick, box, row, out = shown[0].children
                self.assertEqual(pick.value, kp.ALL)                     # 기본 = 전체
                self.assertEqual([v for _, v in pick.options], [kp.ALL, "economic"])
                self.assertEqual(len(box.children), 1)                   # 전체면 안내 글만
                go, dry = row.children
                go.click()                                              # 기본(전체)로 만들기
                pick.set("economic")                                    # 주제를 고르면 대본 체크 상자
                self.assertEqual([cb.description for cb in box.children[1:]], [r["label"] for r in rows])
                dry.click()                                             # 아무것도 안 고름 = 주제 전체
                box.children[2].value = True; go.click()                # 쇼츠 하나만
                self.assertFalse(pick.disabled)                          # 끝나면 다시 풀림
                self.assertFalse(box.children[2].disabled)
                pick.set(kp.ALL); go.click()                            # 다시 전체 — 고른 대본은 버림
        self.assertEqual(calls, [(kp.ALL, ("--push",), None, True, True),
                                 ("economic", ("--dry-run",), None, True, True),
                                 ("economic", ("--push",), ["a-1-shorts"], True, True),
                                 (kp.ALL, ("--push",), None, True, True)])

    def test_cli_rejects_unknown_ids(self):
        with mock.patch.object(kp, "run") as run:
            self.assertEqual(kp.main(["--topic", "test", "--ids", "no-such-video"]), 2)
            run.assert_not_called()


if __name__ == "__main__":
    unittest.main()
