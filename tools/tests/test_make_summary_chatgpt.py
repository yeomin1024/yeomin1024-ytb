# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-15 — tools/make_summary.py v1.4.0 --chatgpt 시험 (임시 폴더의 가짜 thumbnail_N.md 만 씀 — 네트워크 없음)
r"""
  python3 -m unittest tools.tests.test_make_summary_chatgpt -v     (저장소 최상위에서)

- thumbnail_1~3.md 의 문구표·[A] 프롬프트가 chatgpt.md 에 글자 그대로 들어가는지 ([B]·검수 칸은 안 들어감)
- 'ChatGPT에게' 지시(차례로 모두·그대로·16:9·한글 그대로)와 공개 주소가 들어가는지
- [A] 칸이 없으면 멈추는지
"""
import io
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(TOOLS))
import make_summary as ms  # noqa: E402


def thumb_md(i, a_text="PROMPT", with_a=True):
    a = f"## [A] 완성형 프롬프트\n```\n{a_text} {i} \"세금\"\n```\n\n" if with_a else ""
    return (f"# vid 썸네일 {i} — 시안 {i}\n\n버전: v1\n\n| 항목 | 값 |\n|---|---|\n| 시험하는 가설 | h{i} |\n\n"
            f"## 문구 (그대로 사용)\n| 자리 | 문구 | 색 |\n|---|---|---|\n| 하단 1줄 | 줄{i} | 노랑 |\n\n"
            f"{a}## [B] 글자 없는 프롬프트\n```\nNO_TEXT_{i}\n```\n\n## 검수\n- [ ] CHECK_{i}\n")


class ChatgptFileTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.folder = self.root / "economic" / "source" / "vid" / "thumbnails"
        self.folder.mkdir(parents=True)

    def tearDown(self):
        self.tmp.cleanup()

    def run_tool(self):
        with redirect_stdout(io.StringIO()) as buf:
            path = ms.chatgpt_file("economic", "vid", root=self.root)
        return path.read_text("utf-8"), buf.getvalue()

    def test_three_prompts_verbatim_in_order(self):
        for i in (1, 2, 3):
            (self.folder / f"thumbnail_{i}.md").write_text(thumb_md(i), "utf-8")
        text, log = self.run_tool()
        for i in (1, 2, 3):
            self.assertIn(f'PROMPT {i} "세금"', text)
            self.assertIn(f"| 하단 1줄 | 줄{i} | 노랑 |", text)
            self.assertNotIn(f"NO_TEXT_{i}", text)   # [B] 는 넣지 않음
            self.assertNotIn(f"CHECK_{i}", text)     # 검수 칸도 넣지 않음
        self.assertLess(text.index("## thumbnail_1"), text.index("## thumbnail_2"))
        self.assertLess(text.index("## thumbnail_2"), text.index("## thumbnail_3"))
        self.assertIn("thumbnail_1부터 차례로 모두", text)
        self.assertIn("가로형 16:9", text)
        self.assertIn("글자·띄어쓰기 그대로", text)
        self.assertIn(f"{ms.RAW_BASE}/economic/source/vid/thumbnails/chatgpt.md", text)
        self.assertIn("[CHATGPT] topic=economic video=vid thumbnails=3", log)

    def test_missing_a_block_stops(self):
        (self.folder / "thumbnail_1.md").write_text(thumb_md(1, with_a=False), "utf-8")
        with redirect_stdout(io.StringIO()), self.assertRaises(SystemExit):
            ms.chatgpt_file("economic", "vid", root=self.root)

    def test_no_files_stops(self):
        with redirect_stdout(io.StringIO()), self.assertRaises(SystemExit):
            ms.chatgpt_file("economic", "vid", root=self.root)


if __name__ == "__main__":
    unittest.main()
