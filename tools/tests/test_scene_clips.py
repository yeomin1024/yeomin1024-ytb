# -*- coding: utf-8 -*-
# VERSION: v1.4 — 2026-11-06 — scene_clips v1.4.0: 대본 전 plan(timing=clips — 클립마다 sec) · 클립 format 줄 · negative_prompt ·
#          sheet_note · inherit 없는 쇼츠도 설정표 (TestClipsMode · test_prompts_and_settings 마지막 줄).
# (v1.3 — 2026-10-21 — scene_clips v1.3.0: plan 클립 seed → videogen.json 항목 seed (없으면 키 없음) · ghost (선명도 떨어짐 찾기 —
#          숫자 시험 + 진짜 ffmpeg 로 1초부터 흐려지는 클립).
# (v1.2 — 2026-10-19 — scene_clips v1.2: 그림 .jpg 기본 · JPEG 700KB 규칙 · 깨진 그림 검사 (test_image_ok).
# (v1.1 — 2026-10-19 — scene_clips v1.1: ChatGPT 가 저장소에 올림(규칙 8) · 그림 확장자 .png 기본 (image_ext).
# (v1.0 — 2026-10-19 — tools/scene_clips.py v1.0 시험 (구간 계산 · 장 시작·겹침·썸네일 자리 검사 · 프롬프트 · videogen 설정)
# (가짜 계획·시각만 씀 — 파일·네트워크 없음))
r"""
  python3 -m unittest tools.tests.test_scene_clips -v     (저장소 최상위에서)
"""
import sys
import tempfile
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
        self.assertIn("x/scenes/A1.jpg", md)
        self.assertIn("JPEG(.jpg)로 바꿔 700KB 이하", md)                           # v1.2 — GitHub 앱이 768KB 넘는 파일을 자름
        self.assertIn("ChatGPT 는 저장소에 파일을 올릴 수 있다", md)                # v1.1 — 올리기가 기본
        self.assertNotIn("읽기만", md)
        self.assertEqual(sc.videogen_settings(dict(p, image_ext=".png"), sc.windows(p, SENTS))["start_images"][0]["image"],
                         "x/scenes/A1.png")
        ps = plan([dict(clip("A1", 1, 1), seed="1046")])                               # v1.3 — 그 클립만 다른 seed
        self.assertEqual(sc.videogen_settings(ps, sc.windows(ps, SENTS))["start_images"][0]["seed"], 1046)
        self.assertNotIn("seed", v["start_images"][0])
        self.assertIn("「하나.」", md)
        self.assertNotIn("0. 인물 설정표", sc.chatgpt_md(dict(p, inherit="x/plan.json"), SENTS, "x", "t", shorts=True))
        self.assertIn("0. 인물 설정표", sc.chatgpt_md(p, SENTS, "x", "t", shorts=True))   # v1.4 — 물려받지 않은 쇼츠(단독 편)

    def test_ghost_scan(self):                                       # v1.3 — 쓰는 구간 안 선명도 떨어짐
        s = [50.0] * 6 + [100.0] * 30 + [70.0] * 12 + [100.0] * 12   # 24fps: 1.5~2.0초 겹침
        r = sc.ghost_scan(s, 0.0, 2.5)
        self.assertEqual((r["first_drop_sec"], r["min_rel"]), (1.5, 0.7))
        self.assertIsNone(sc.ghost_scan(s, 0.0, 1.4)["first_drop_sec"])   # 그 앞만 쓰면 괜찮음
        self.assertIsNone(sc.ghost_scan(s, 2.0, 2.5)["first_drop_sec"])   # 그 뒤만 써도
        self.assertIsNone(sc.ghost_scan([10.0] * 5 + [100.0] * 20, 0.0, 1.0)["first_drop_sec"])   # 첫 0.25초(덜 선명)는 안 봄

    def test_sharpness_ffmpeg(self):
        import shutil
        import subprocess
        if not shutil.which("ffmpeg"):
            self.skipTest("ffmpeg 없음")
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "c.mp4"
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", "testsrc2=s=320x176:r=24:d=2",
                            "-vf", "boxblur=6:enable='gte(t,1)'", "-pix_fmt", "yuv420p", str(f)], check=True)
            r = sc.ghost_scan(sc.sharpness(f, 320, 176), 0.0, 2.0)
            self.assertAlmostEqual(r["first_drop_sec"], 1.0, delta=0.05)
            self.assertLess(r["min_rel"], 0.5)

    def test_image_ok(self):                                         # v1.2 — 잘려 올라간 PNG 는 깨진 것
        import io, tempfile
        from PIL import Image
        with tempfile.TemporaryDirectory() as d:
            good, bad = Path(d) / "a.jpg", Path(d) / "b.png"
            Image.new("RGB", (32, 32), (10, 200, 90)).save(good)
            buf = io.BytesIO()
            Image.frombytes("RGB", (64, 64), bytes((i * 7) % 256 for i in range(64 * 64 * 3))).save(buf, format="PNG")
            bad.write_bytes(buf.getvalue()[: len(buf.getvalue()) // 2])
            self.assertTrue(sc.image_ok(good))
            self.assertFalse(sc.image_ok(bad))
            broken = []
            self.assertIsNone(sc._image_file({"scenes": Path(d)}, "b", broken))
            self.assertEqual([f.name for f in broken], ["b.png"])

    def test_crop(self):
        self.assertEqual(sc.crop_pct(1536, 1024, "landscape"), 17.5)   # ChatGPT 3:2 → 1280x704(1.82:1) 위아래 잘림
        self.assertEqual(sc.crop_pct(1024, 1536, "portrait"), 17.5)
        self.assertLess(sc.crop_pct(1536, 864, "landscape"), 3)   # 16:9 그림 → 1280x704 는 2.2% (거의 그대로)



# ---- v1.4 대본 전 장면 계획 (timing=clips) ----
def clips_plan(**kw) -> dict:
    plan = dict(video="t", orientation="portrait", timing="clips", release_tag="clips-t", image_dir="x/scenes",
                style=dict(image="STYLE-IMG", motion="STYLE-MOTION"),
                characters=[dict(id="A", name="a", en="A — hyper"), dict(id="B", name="b", en="B — calm")],
                places=[dict(id="p", name="p", en="PLACE")],
                formats=dict(duo="Format: TOP-40-EMPTY"),
                clips=[dict(name="S01", chars=["A"], place="p", sec=5.0, ko="하나", image="IMG1", motion="MOVE1"),
                       dict(name="S02", chars=["A", "B"], place="p", format="duo", sec=3.0, ko="둘", image="IMG2", motion="MOVE2"),
                       dict(name="S03", chars=["B"], ko="셋", image="IMG3", motion="MOVE3")])
    plan.update(kw)
    return plan


class TestClipsMode(unittest.TestCase):
    def test_windows_by_sec(self):
        wins = sc.windows(clips_plan(), [])
        self.assertEqual([w["frames"] for w in wins], [121, 73, 121])      # 5.0초 · 3.0초 · sec 없음 → max_sec 5.0
        self.assertEqual([w["t0"] for w in wins], [0.0, 5.042, 8.084])     # 차례로 이어 놓음
        self.assertTrue(all(w["slow"] == 1.0 for w in wins))

    def test_check_problems(self):
        plan = clips_plan()
        self.assertEqual(sc.check_plan(plan, [], sc.windows(plan, [])), [])
        plan["clips"][0]["sec"] = 6.0                                      # 145 프레임 > 121
        plan["clips"][1]["format"] = "nope"
        plan["clips"][2]["sentences"] = [1, 2]
        probs = sc.check_plan(plan, [], sc.windows(plan, []))
        self.assertTrue(any("S01" in p and "145" in p for p in probs), probs)
        self.assertTrue(any("S02" in p and "format" in p for p in probs), probs)
        self.assertTrue(any("S03" in p and "sentences" in p for p in probs), probs)

    def test_prompts_and_settings(self):
        plan = clips_plan(negative_prompt="NEG", sheet_note="EXPRESSIONS-ROW")
        self.assertIn("Format: TOP-40-EMPTY", sc.image_prompt(plan, plan["clips"][1]))
        self.assertIn("9:16 vertical", sc.image_prompt(plan, plan["clips"][0]))     # format 없음 → 기본 줄
        md = sc.chatgpt_md(plan, [], "x/scenes/plan.json", "stamp", shorts=True)
        self.assertIn("0. 인물 설정표", md)                                  # inherit 없음 → 쇼츠 단독도 설정표
        self.assertIn("EXPRESSIONS-ROW", md)
        self.assertNotIn("내레이션 (", md)
        self.assertIn("클립 약 3초의 첫 장면 · 구도 `duo`", md)
        vg = sc.videogen_settings(plan, sc.windows(plan, []))
        self.assertEqual((vg["width"], vg["height"], vg["negative_prompt"]), (704, 1280, "NEG"))
        self.assertEqual([i["sec"] for i in vg["start_images"]], [5.0, 3.0, 5.0])
        self.assertTrue(vg["start_images"][1]["prompt"].startswith("MOVE2 STYLE-MOTION"))
        self.assertIn("대본 전", sc.plan_md(plan, [], sc.windows(plan, []), "src", "stamp"))

    def test_script_plan_unchanged(self):
        """대본 plan(timing 없음)은 v1.3 과 같은 길 — 문장 시각으로 구간, 기본 부정 프롬프트, inherit 있으면 설정표 없음."""
        plan = clips_plan(timing=None, inherit="some/plan.json")
        del plan["timing"]
        for i, c in enumerate(plan["clips"]):
            c.pop("sec", None)
            c.pop("format", None)
            c["sentences"] = [i + 1, i + 1]
        sents = [dict(n=n, start=(n - 1) * 4.0, end=(n - 1) * 4.0 + 3.5, part="p1", text=f"문장{n}") for n in (1, 2, 3)]
        wins = sc.windows(plan, sents)
        self.assertEqual([w["t0"] for w in wins], [0.0, 3.85, 7.85])        # 첫 문장 0 · 나머지 시작 - lead 0.15
        self.assertEqual(sc.check_plan(plan, sents, wins), [])
        self.assertEqual(sc.videogen_settings(plan, wins)["negative_prompt"], sc.NEGATIVE)
        md = sc.chatgpt_md(plan, sents, "x/scenes/plan.json", "stamp", shorts=True)
        self.assertNotIn("0. 인물 설정표", md)                               # inherit 있는 쇼츠 — 예전처럼 없음
        self.assertIn("내레이션 (문장 1): 「문장1」", md)


if __name__ == "__main__":
    unittest.main()
