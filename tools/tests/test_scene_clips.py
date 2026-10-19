# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-19 — tools/scene_clips.py v1.0 시험 (구간 계산 · 장 시작·겹침·썸네일 자리 검사 · 프롬프트 · videogen 설정)
# (가짜 계획·시각만 씀 — 파일·네트워크 없음)
r"""
  python3 -m unittest tools.tests.test_scene_clips -v     (저장소 최상위에서)
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import scene_clips as sc  # noqa: E402

SENTS = [dict(n=1, start=0.3, end=2.9, part="A", text="하나."), dict(n=2, start=3.4, end=6.0, part="A", text="둘."),
         dict(n=3, start=6.5, end=9.0, part="A", text="셋."), dict(n=4, start=10.0, end=12.0, part="B", text="넷."),
         dict(n=5, start=12.5, end=20.0, part="B", text="다섯.")]
STYLE = dict(image="2D style.", motion="Smooth motion.")
CHARS = [dict(id="kim", name="김 씨", en="Mr. Kim — navy shirt.")]


def plan(clips, **kw):
    return dict(dict(video="v", orientation="landscape", release_tag="clips-v", image_dir="x/scenes", style=STYLE,
                     characters=CHARS, places=[dict(id="home", name="집", en="Home.")], clips=clips), **kw)


def clip(name, a, b, **kw):
    return dict(dict(name=name, sentences=[a, b], chars=["kim"], place="home", ko="장면", image="Scene.", motion="Moves."), **kw)


class TestSceneClips(unittest.TestCase):
    def test_windows(self):
        w = {x["name"]: x for x in sc.windows(plan([clip("A1", 1, 1), clip("A2", 3, 3), clip("A3", 5, 5)]), SENTS)}
        self.assertEqual((w["A1"]["t0"], w["A1"]["t1"]), (0.0, 3.25))          # 첫 문장은 0초부터, 다음 문장 시작 - lead
        self.assertEqual((w["A2"]["t0"], w["A2"]["t1"]), (6.35, 9.0))          # 다음 문장(4)이 장 시작 → 카드 1초 전까지
        self.assertEqual((w["A3"]["t0"], w["A3"]["t1"]), (12.35, 20.3))        # 마지막 문장: 끝 + 0.3
        self.assertEqual(w["A1"]["sec"], 3.75)                                 # 구간 + 0.5
        self.assertEqual(w["A3"]["sec"], 5.0)                                  # 최대 5초
        self.assertEqual(w["A3"]["frames"], 121)
        self.assertAlmostEqual(w["A3"]["slow"], 7.95 / (121 / 24), places=3)   # 구간 7.95초 > 5.04초 → 늦춤(그래도 모자라면 멈춤)
        self.assertTrue(all(x["frames"] % 4 == 1 for x in w.values()))
        fixed = sc.windows(plan([clip("S", 2, 2)], fixed_sec=5.0), SENTS)[0]
        self.assertEqual((fixed["sec"], fixed["frames"]), (5.0, 121))

    def test_check_plan(self):
        p = plan([clip("A1", 1, 2), clip("A2", 2, 2), clip("A3", 4, 4), clip("A4", 3, 3, chars=["nobody"], motion="")],
                 cover_sentences=[1])
        probs = "\n".join(sc.check_plan(p, SENTS, sc.windows(p, SENTS)))
        self.assertIn("문장 2: A1 와 A2 가 겹침", probs)
        self.assertIn("A3: 문장 4 은 장 시작", probs)
        self.assertIn("A1: 문장 1 은 썸네일 그림", probs)
        self.assertIn("A4: 모르는 인물", probs)
        self.assertIn("A4: 'motion' 가 비어 있음", probs)
        ok = plan([clip("A1", 2, 3)])
        self.assertEqual(sc.check_plan(ok, SENTS, sc.windows(ok, SENTS)), [])

    def test_prompts_and_settings(self):
        p = plan([clip("A1", 1, 1)])
        img = sc.image_prompt(p, p["clips"][0])
        for needle in ("2D style.", "16:9 landscape", "Mr. Kim — navy shirt.", "Place: Home.", "Scene: Scene.", "no text"):
            self.assertIn(needle, img)
        self.assertIn("9:16 vertical", sc.image_prompt(dict(p, orientation="portrait"), p["clips"][0]))
        v = sc.videogen_settings(p, sc.windows(p, SENTS))
        self.assertEqual((v["model"], v["width"], v["height"], v["concat"], v["release_tag"]),
                         ("wan2.2-5b-fast", 1280, 704, False, "clips-v"))
        self.assertEqual(v["start_images"][0], dict(image="x/scenes/A1.jpg", name="A1", sec=3.75,
                                                    prompt="Moves. Smooth motion."))
        md = sc.chatgpt_md(p, SENTS, "x/scenes/plan.json", "2026-10-19 00:00", shorts=False)
        self.assertIn("0. 인물 설정표", md)
        self.assertIn("x/scenes/A1.png", md)
        self.assertIn("「하나.」", md)
        self.assertNotIn("0. 인물 설정표", sc.chatgpt_md(p, SENTS, "x", "t", shorts=True))

    def test_crop(self):
        self.assertEqual(sc.crop_pct(1536, 1024, "landscape"), 17.5)   # ChatGPT 3:2 → 1280x704(1.82:1) 위아래 잘림
        self.assertEqual(sc.crop_pct(1024, 1536, "portrait"), 17.5)
        self.assertLess(sc.crop_pct(1536, 864, "landscape"), 3)   # 16:9 그림 → 1280x704 는 2.2% (거의 그대로)


if __name__ == "__main__":
    unittest.main()
