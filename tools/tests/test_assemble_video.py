# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-10-21 — use_from·use_to(클립 안 구간만)·loop pingpong · 뒤가 코드 화면이면 TAIL 만큼 더 (test_tail)(앞으로 → 거꾸로) 맞추기·그래프 + 진짜 ffmpeg 로 그 부분 그래프 돌려 프레임 수 확인.
# 이전 v1.0 — 2026-10-19 — tools/assemble_video.py v1.0 시험 (클립 맞추기: 자르기·늦추기 1.35배·마지막 장면 멈춤 · ffmpeg 그래프 · 각색 안내 그림)
# (가짜 길이만 씀 — 실제 합치기는 쇼츠 자리 표시 클립으로 따로 돌려 봄: assemble_video.py --placeholders)
r"""
  python3 -m unittest tools.tests.test_assemble_video -v     (저장소 최상위에서)
"""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import assemble_video as av  # noqa: E402

WINS = [dict(name="L01", a=1, b=1, t0=0.0, t1=3.0, frames=89), dict(name="L02", a=3, b=3, t0=10.0, t1=14.0, frames=97),
        dict(name="L03", a=5, b=5, t0=20.0, t1=27.0, frames=121)]
DUR = {"L01": 3.708, "L02": 3.2, "L03": 5.04}


class TestAssemble(unittest.TestCase):
    def setUp(self):
        self.real_probe = av.probe
        av.probe = lambda p: dict(duration=DUR[Path(p).stem])

    def tearDown(self):
        av.probe = self.real_probe

    def test_fit(self):
        fits = {f["name"]: f for f in av.fit_plan(WINS, {k: Path(f"{k}.mp4") for k in DUR}, tail=0.0)}
        self.assertEqual((fits["L01"]["slow"], fits["L01"]["hold"], fits["L01"]["cut"]), (1.0, 0.0, 0.708))   # 길면 자름
        self.assertAlmostEqual(fits["L02"]["slow"], 4.0 / 3.2, places=4)                                      # 짧으면 늦춤 (1.25배)
        self.assertEqual(fits["L02"]["hold"], 0.0)
        self.assertEqual(fits["L03"]["slow"], av.sc.MAX_SLOW)                                                 # 1.35배까지만
        self.assertAlmostEqual(fits["L03"]["hold"], 7.0 - 5.04 * av.sc.MAX_SLOW, places=3)                    # 나머지는 멈춤

    def test_graph(self):
        fits = av.fit_plan(WINS, {k: Path(f"{k}.mp4") for k in DUR}, tail=0.0)
        g = av.build_graph(fits, (1920, 1080), dict(a=0.3, b=19.0), None)
        self.assertIn("[1:v]scale=1920:1080:force_original_aspect_ratio=increase:flags=lanczos,crop=1920:1080", g)
        self.assertIn("setpts=(PTS-STARTPTS)*1.2500", g)
        self.assertIn("tpad=stop_mode=clone", g)                       # L03 만
        self.assertEqual(g.count("tpad="), 1)
        self.assertIn("setpts=PTS-STARTPTS+10.000/TB", g)
        self.assertIn("enable='between(t,9.999,14.001)'", g)
        self.assertIn("[4:v]setpts=PTS-STARTPTS,format=rgba[ov]", g)  # 자막·이름표 PNG = 클립 다음 입력
        self.assertIn("[5:v]format=rgba", g)                           # 각색 안내
        self.assertTrue(g.rstrip().endswith("[vout]"))
        p = av.build_graph(fits, (1920, 1080), None, (60.0, 90.0))
        self.assertIn("trim=start=60.000:end=90.000", p)
        self.assertNotIn("[nt]", p)

    def test_span_pingpong(self):
        opts = {"L03": {"use_to": 1.3, "loop": "pingpong"}, "L01": {"use_from": 1.0, "use_to": 3.0},
                "L02": {"use_from": 1.2, "loop": "pingpong"}}
        fits = {f["name"]: f for f in av.fit_plan(WINS, {k: Path(f"{k}.mp4") for k in DUR}, opts, tail=0.0)}
        d = 2 * 1.3 - 1 / av.sc.MODEL_FPS
        self.assertEqual((fits["L03"]["span"], fits["L03"]["pingpong"], fits["L03"]["slow"]), ((0.0, 1.3), True, av.sc.MAX_SLOW))
        self.assertAlmostEqual(fits["L03"]["hold"], 7.0 - d * av.sc.MAX_SLOW, places=3)
        self.assertEqual(fits["L01"]["span"], (1.0, 3.0))
        self.assertEqual(fits["L01"]["slow"], av.sc.MAX_SLOW)                                                # 2.0초 → 3.0초는 1.35배까지
        self.assertEqual(fits["L02"]["span"], (1.2, 3.2))                                                    # 끝 = 클립 길이
        self.assertAlmostEqual(fits["L02"]["slow"], 4.0 / (2 * 2.0 - 1 / av.sc.MODEL_FPS), places=3)
        g = av.build_graph(list(fits.values()), (1920, 1080), None, None)
        self.assertIn("[3:v]trim=start=0.000:end=1.300,setpts=PTS-STARTPTS,split[pa3][pb3]", g)
        self.assertIn("[pb3]reverse,trim=start_frame=1,setpts=PTS-STARTPTS[pr3]", g)
        self.assertIn("[pp3]scale=1920:1080", g)
        self.assertIn("[1:v]trim=start=1.000:end=3.000,setpts=PTS-STARTPTS[pp1]", g)
        plain = av.build_graph(av.fit_plan(WINS, {k: Path(f"{k}.mp4") for k in DUR}, tail=0.0), (1920, 1080), None, None)
        self.assertNotIn("[pp", plain)                                                                       # 옵션 없으면 예전 그래프
        for bad in ({"L01": {"loop": "bounce"}}, {"L01": {"use_from": 3.0, "use_to": 2.0}}, {"L01": {"use_from": 9.0}}):
            with self.assertRaises(SystemExit):
                av.fit_plan(WINS, {k: Path(f"{k}.mp4") for k in DUR}, bad, tail=0.0)

    def test_tail(self):
        wins = [dict(WINS[0]), dict(WINS[1], t0=3.0, t1=6.0), dict(WINS[2])]           # L01 바로 뒤에 L02 → L01 은 늘리지 않음
        fits = {f["name"]: f for f in av.fit_plan(wins, {k: Path(f"{k}.mp4") for k in DUR})}
        self.assertEqual((fits["L01"]["t1"], fits["L01"]["tail"]), (3.0, 0.0))
        self.assertEqual((fits["L02"]["t1"], fits["L02"]["t1_plan"], fits["L02"]["tail"]), (6.15, 6.0, av.TAIL))
        self.assertEqual(fits["L02"]["slow"], 1.0)                                         # 3.2초 클립이 3.15초를 덮음
        g = av.build_graph(list(fits.values()), (1920, 1080), None, None)
        self.assertIn("enable='between(t,2.999,6.151)'", g)                              # 보이는 끝도 늘어남
        self.assertIn("trim=duration=3.150", g)

    def test_pingpong_ffmpeg(self):
        """진짜 ffmpeg: 24fps 2초 → 앞 1초 pingpong = 24 + 23 프레임."""
        import shutil
        import subprocess
        if not shutil.which("ffmpeg"):
            self.skipTest("ffmpeg 없음")
        with tempfile.TemporaryDirectory() as d:
            src, dst = Path(d) / "c.mp4", Path(d) / "o.mp4"
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", "testsrc2=s=128x72:r=24:d=2", "-pix_fmt", "yuv420p",
                            str(src)], check=True)
            g = ("[0:v]trim=duration=1.000,setpts=PTS-STARTPTS,split[a][b];[b]reverse,trim=start_frame=1,setpts=PTS-STARTPTS[r];"
                 "[a][r]concat=n=2:v=1:a=0[v]")
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(src), "-filter_complex", g, "-map", "[v]", str(dst)], check=True)
            n = subprocess.run(["ffprobe", "-v", "error", "-count_frames", "-select_streams", "v:0", "-show_entries",
                                "stream=nb_read_frames", "-of", "csv=p=0", str(dst)], capture_output=True, text=True).stdout.strip()
            self.assertEqual(int(n), 24 + 23)

    def test_notice_png(self):
        from PIL import Image
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "n.png"
            av.notice_png("기사 사례를 바탕으로 각색한 가상 사례", (1920, 1080), f, portrait=False)
            with Image.open(f) as im:
                x0, y0, x1, y1 = im.getbbox()
                self.assertEqual((im.mode, im.size), ("RGBA", (1920, 1080)))
                self.assertGreater(x0, 960)          # 오른쪽 위
                self.assertLessEqual(x1, 1920 - 96 + 1)
                self.assertLess(y1, 140)


if __name__ == "__main__":
    unittest.main()
