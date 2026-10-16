# -*- coding: utf-8 -*-
# VERSION: v1.4 — 2026-10-16 — make_summary v1.5.0 --chatgpt-all (주제 모든 영상 한 파일, 장마다 저장 경로) · 영상별 파일 그림 위 저장 경로 시험.
# (v1.3 — 2026-10-15 — v1.4.3 글자 없는 썸네일('| 글자 | 없음') 규칙 시험 추가.)
# (v1.2 — 2026-10-15 — tools/make_summary.py v1.4.2 --chatgpt 시험 (못 쓰면 Claude 대화에 붙이라는 안내, 모두 만들었을 때 '만들 것 없음')
# (v1.1 — 2026-10-15 — v1.4.1: 올리기 단계·이미지 있는 시안 빼기))
# (v1.0 — 2026-10-15 — v1.4.0 --chatgpt 시험)
# (임시 폴더의 가짜 thumbnail_N.md 만 씀 — 네트워크 없음)
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
        self.assertIn("thumbnail_1, thumbnail_2, thumbnail_3)를 **차례로 모두**", text)
        self.assertIn(f"{ms.UPLOAD_BASE}/economic/source/vid/thumbnails", text)   # 올리기 링크
        self.assertIn("thumbnail_N.png", text)
        self.assertIn("Claude 대화창에 그대로 붙여 넣어 주세요", text)   # ChatGPT 가 못 올릴 때 기본 길
        self.assertIn("가로형 16:9", text)
        self.assertIn("글자·띄어쓰기 그대로", text)
        self.assertIn(f"{ms.RAW_BASE}/economic/source/vid/thumbnails/chatgpt.md", text)
        self.assertIn("[CHATGPT] topic=economic video=vid thumbnails=3", log)

    def test_skips_thumbnails_with_images(self):
        for i in (1, 2, 3):
            (self.folder / f"thumbnail_{i}.md").write_text(thumb_md(i), "utf-8")
        (self.folder / "thumbnail_1.webp").write_bytes(b"img")
        text, log = self.run_tool()
        self.assertNotIn("## thumbnail_1", text)
        self.assertIn("## thumbnail_2", text)
        self.assertIn("thumbnail_2, thumbnail_3)를", text)
        self.assertIn("skip=thumbnail_1", log)

    def test_all_images_present_writes_done_notice(self):
        for i in (1, 2, 3):
            (self.folder / f"thumbnail_{i}.md").write_text(thumb_md(i), "utf-8")
            (self.folder / f"thumbnail_{i}.png").write_bytes(b"img")
        text, log = self.run_tool()
        self.assertIn("만들 것 없음", text)
        self.assertNotIn("PROMPT", text)
        self.assertIn("thumbnails=0", log)

    def test_missing_a_block_stops(self):
        (self.folder / "thumbnail_1.md").write_text(thumb_md(1, with_a=False), "utf-8")
        with redirect_stdout(io.StringIO()), self.assertRaises(SystemExit):
            ms.chatgpt_file("economic", "vid", root=self.root)

    def test_no_files_stops(self):
        with redirect_stdout(io.StringIO()), self.assertRaises(SystemExit):
            ms.chatgpt_file("economic", "vid", root=self.root)

    def test_no_text_rules(self):                       # v1.4.3 — 주식(전 세계 대상) 글자 없는 썸네일
        for i in (1, 2, 3):
            md = thumb_md(i).replace("| 시험하는 가설 | h", "| 글자 | **없음** (그림만) |\n| 시험하는 가설 | h")
            (self.folder / f"thumbnail_{i}.md").write_text(md, "utf-8")
        text, _ = self.run_tool()
        self.assertIn("글자·숫자·기호·로고·워터마크를 하나도 넣지 않는다", text)
        self.assertIn("글자처럼 보이는 것", text)
        self.assertNotIn("받침과 모음 획", text)
        self.assertNotIn("문구 (그림 속 한글", text)            # 문구표를 넣지 않음
        for n in ("4.", "5.", "6.", "7."):                      # 규칙 번호 차례
            self.assertIn("\n" + n, text)
        self.assertLess(text.index("\n4."), text.index("\n5."))
        self.assertLess(text.index("\n5."), text.index("\n6."))


    def test_label_has_save_path(self):                 # v1.5.0 — 그림 위에 저장 경로
        for i in (1, 2, 3):
            (self.folder / f"thumbnail_{i}.md").write_text(thumb_md(i), "utf-8")
        text, _ = self.run_tool()
        self.assertIn("저장 경로 `economic/source/vid/thumbnails/thumbnail_N.png`", text)


class ChatgptAllTest(unittest.TestCase):                # v1.5.0 --chatgpt-all
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        for vid in ("b-vid", "a-vid"):
            f = self.root / "economic" / "source" / vid / "thumbnails"
            f.mkdir(parents=True)
            for i in (1, 2, 3):
                (f / f"thumbnail_{i}.md").write_text(thumb_md(i, a_text=f"PROMPT_{vid}"), "utf-8")
        (self.root / "economic" / "source" / "a-vid" / "thumbnails" / "thumbnail_2.png").write_bytes(b"img")
        (self.root / "economic" / "source" / "no-thumbs").mkdir(parents=True)          # 썸네일 폴더 없는 영상은 무시

    def tearDown(self):
        self.tmp.cleanup()

    def run_all(self):
        with redirect_stdout(io.StringIO()) as buf:
            path = ms.chatgpt_all("economic", root=self.root)
        return path, path.read_text("utf-8"), buf.getvalue()

    def test_collects_pending_in_order_with_paths(self):
        path, text, log = self.run_all()
        self.assertEqual(path, self.root / "economic" / "thumbnails_chatgpt.md")
        heads = [l for l in text.splitlines() if l.startswith("## ") and " · thumbnail_" in l]
        self.assertEqual([h.split(" — ")[0] for h in heads],
                         ["## 1. a-vid · thumbnail_1", "## 2. a-vid · thumbnail_3",
                          "## 3. b-vid · thumbnail_1", "## 4. b-vid · thumbnail_2", "## 5. b-vid · thumbnail_3"])
        self.assertIn("**저장 경로: `economic/source/a-vid/thumbnails/thumbnail_3.png`**", text)
        self.assertNotIn("a-vid/thumbnails/thumbnail_2.png`**", text)                    # 이미지 있는 시안은 뺌
        self.assertIn('PROMPT_b-vid 2 "세금"', text)
        self.assertIn("썸네일 5장(2개 영상)을 **1번부터 차례로 모두**", text)
        self.assertIn("이 그림 5장을 이 순서대로 Claude 대화창에 붙여 넣어 주세요", text)
        self.assertIn(f"{ms.UPLOAD_BASE}/economic/source/b-vid/thumbnails", text)
        self.assertIn(f"{ms.RAW_BASE}/economic/thumbnails_chatgpt.md", text)
        self.assertIn("[CHATGPT-ALL] topic=economic videos=2 thumbnails=5", log)

    def test_all_done_notice(self):
        for vid in ("a-vid", "b-vid"):
            for i in (1, 2, 3):
                (self.root / "economic" / "source" / vid / "thumbnails" / f"thumbnail_{i}.webp").write_bytes(b"img")
        _, text, log = self.run_all()
        self.assertIn("만들 것 없음", text)
        self.assertNotIn("PROMPT", text)
        self.assertIn("thumbnails=0", log)


if __name__ == "__main__":
    unittest.main()
