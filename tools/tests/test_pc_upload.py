# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-15 — tools/pc_upload.py v1.0 · tools/drive_videos.py v1.0 · youtube_upload.py v1.5(썸네일 Pillow) 시험
#          (가짜 GitHub·Drive·유튜브 — 네트워크·진짜 GitHub 쓰기 없음)
r"""
  python3 -m unittest tools.tests.test_pc_upload -v     (저장소 최상위에서)

1) .env 읽기: 이미 있는 환경 변수는 그대로
2) 준비된 영상 고르기·설정 받기(썸네일은 thumbnail_N 이미지만)
3) 전체 흐름: Drive 데스크톱 폴더 영상은 그대로 쓰고 지우지 않음 · Drive API 로 받은 영상은 올린 뒤 지움 ·
   예약 시각 = --at + --gap · youtube.json 을 GitHub 에 새 파일로 · 할당량 초과면 멈춤
4) Drive 올리기: 폴더 찾기 → 이어 올리기 → drive.json · 같은 md5 면 건너뜀
5) ffmpeg 없는 PC: 썸네일을 Pillow 로 1280×720 JPG
"""
import datetime as dt
import hashlib
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(TOOLS))
import drive_videos as dv  # noqa: E402
import pc_upload as pu  # noqa: E402
import youtube_upload as yu  # noqa: E402

KEYS = ("YOUTUBE_CLIENT_ID", "YOUTUBE_CLIENT_SECRET", "YOUTUBE_REFRESH_TOKEN", "GITHUB_TOKEN", "DRIVE_DIR")


class FakeGitHub:
    def __init__(self, files, token="t"):
        self.files, self.token, self.puts = dict(files), token, []

    def list(self, path):
        path = path.rstrip("/") + "/"
        seen = {}
        for p in self.files:
            if p.startswith(path):
                head = p[len(path):].split("/")[0]
                seen[head] = "dir" if "/" in p[len(path):] else "file"
        return [{"name": k, "type": v, "path": path + k} for k, v in sorted(seen.items())]

    def raw(self, path):
        return self.files.get(path)

    def put_new(self, path, content, message):
        if path in self.files:
            return "exists"
        self.files[path] = content
        self.puts.append((path, message))
        return "created"


def sheet(vid):
    return f"""# {vid}
## 1. 제목
```
제목 {vid}
```
## 2. 설명란
```
첫 줄
■ 챕터
0:00 하나
```
## 3. 챕터
```
python tools/srt_tool.py upload a b --chapters "1=하나"
```
## 4. 태그
```
가, 나
```
| 변경되거나 합성된 콘텐츠 | 예 |
""".encode()


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.gh_cls = pu.GitHub
        self.saved = (pu.ROOT, yu.ROOT, dv.ROOT, yu.run, yu.check_auth, yu.access_token, dv.local_video, dv.find_video, dv.download,
                      {k: os.environ.get(k) for k in KEYS})
        pu.ROOT = yu.ROOT = dv.ROOT = self.root
        for k in KEYS:
            os.environ.pop(k, None)

    def tearDown(self):
        (pu.ROOT, yu.ROOT, dv.ROOT, yu.run, yu.check_auth, yu.access_token, dv.local_video, dv.find_video, dv.download, env) = self.saved
        pu.GitHub = self.gh_cls
        for k, v in env.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v
        self.tmp.cleanup()


class PcUploadTest(Base):
    def gh(self):
        f = {}
        for vid in ("a-2026-10", "b-2026-10", "c-2026-10"):
            f[f"economic/source/{vid}/upload.md"] = sheet(vid)
            f[f"economic/source/{vid}/{vid}.txt"] = b"x"
            f[f"economic/source/{vid}/{vid}.srt"] = b"x"
        f["economic/source/a-2026-10/thumbnails/thumbnail_1.webp"] = b"img"
        f["economic/source/a-2026-10/thumbnails/thumbnail_1.md"] = b"prompt"     # 이미지 아님 → 받지 않음
        f["economic/source/b-2026-10/youtube.json"] = b"{}"                       # 이미 올림
        f["economic/source/d-2026-10/d-2026-10.txt"] = b"x"                      # 시트 없음 → 대상 아님
        return FakeGitHub(f)

    def test_load_env(self):
        p = self.root / ".env"
        p.write_text("# 주석\nYOUTUBE_CLIENT_ID='abc'\nYOUTUBE_REFRESH_TOKEN=\nGITHUB_TOKEN=tok\n", "utf-8")
        os.environ["GITHUB_TOKEN"] = "keep"
        got = pu.load_env(p)
        self.assertEqual(os.environ["YOUTUBE_CLIENT_ID"], "abc")
        self.assertEqual(os.environ["GITHUB_TOKEN"], "keep")             # 이미 있던 값은 그대로
        self.assertNotIn("YOUTUBE_REFRESH_TOKEN", os.environ)             # 빈 값은 넣지 않음
        self.assertEqual(got, ["YOUTUBE_CLIENT_ID"])

    def test_candidates_and_settings(self):
        gh = self.gh()
        ready, skipped = pu.find_candidates(gh, "economic")
        self.assertEqual([v for v, _ in ready], ["a-2026-10", "c-2026-10"])
        self.assertEqual(skipped, [("b-2026-10", "이미 올림 (youtube.json)")])
        pu.fetch_settings(gh, "economic", "a-2026-10", ready[0][1])
        d = self.root / "economic/source/a-2026-10"
        self.assertTrue((d / "upload.md").is_file() and (d / "thumbnails/thumbnail_1.webp").is_file())
        self.assertFalse((d / "thumbnails/thumbnail_1.md").exists())

    def test_full_flow(self):
        gh = self.gh()
        pu.GitHub = lambda *a, **k: gh
        local = self.root / "gdrive/youtube/economic/a-2026-10.mp4"
        local.parent.mkdir(parents=True)
        local.write_bytes(b"local video")
        dv.local_video = lambda topic, vid: local if vid == "a-2026-10" else None
        yu.access_token = lambda: "tok"
        dv.find_video = lambda token, topic, vid, folder=None: {"id": "F" + vid, "size": "11", "md5Checksum": "m"}
        got = []

        def fake_download(f, dest, token=None):
            Path(dest).parent.mkdir(parents=True, exist_ok=True)
            Path(dest).write_bytes(b"drive video")
            return Path(dest)
        dv.download = fake_download

        def fake_run(topic, vid, dry_run=False, video=None, publish_at=None, **kw):
            got.append((vid, Path(video).read_bytes(), publish_at))
            (self.root / topic / "source" / vid / "youtube.json").write_text(json.dumps({"videoId": "Y" + vid}), "utf-8")
            return {"url": f"https://youtu.be/Y{vid}"}
        yu.run, yu.check_auth = fake_run, lambda: None
        for k in ("YOUTUBE_CLIENT_ID", "YOUTUBE_CLIENT_SECRET", "YOUTUBE_REFRESH_TOKEN"):
            os.environ[k] = "x"
        at = (dt.datetime.now(dt.timezone(dt.timedelta(hours=9))) + dt.timedelta(hours=3)).replace(second=0, microsecond=0)
        with redirect_stdout(io.StringIO()) as out:
            code = pu.main(["--at", at.strftime("%Y-%m-%d %H:%M"), "--gap", "24h"])
        self.assertEqual(code, 0, out.getvalue()[-800:])
        self.assertEqual([(v, b) for v, b, _ in got], [("a-2026-10", b"local video"), ("c-2026-10", b"drive video")])
        t1 = dt.datetime.strptime(got[0][2], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=dt.timezone.utc)
        t2 = dt.datetime.strptime(got[1][2], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=dt.timezone.utc)
        self.assertEqual(t1, at.astimezone(dt.timezone.utc))
        self.assertEqual(t2 - t1, dt.timedelta(hours=24))
        self.assertEqual([p for p, _ in gh.puts], ["economic/source/a-2026-10/youtube.json", "economic/source/c-2026-10/youtube.json"])
        self.assertTrue(local.is_file())                                              # Drive 데스크톱 폴더 원본은 그대로
        self.assertFalse((self.root / "economic/out/c-2026-10/final_1080p.mp4").exists())   # 받은 사본은 지움
        self.assertIn("| c-2026-10 | uploaded | https://youtu.be/Yc-2026-10 |", out.getvalue())

    def test_quota_stop_and_missing_video(self):
        gh = self.gh()
        pu.GitHub = lambda *a, **k: gh
        dv.local_video = lambda topic, vid: None
        yu.access_token = lambda: "tok"
        dv.find_video = lambda token, topic, vid, folder=None: None if vid == "a-2026-10" else {"id": "F", "md5Checksum": "m"}
        dv.download = lambda f, dest, token=None: (Path(dest).parent.mkdir(parents=True, exist_ok=True), Path(dest).write_bytes(b"v"), Path(dest))[2]
        calls = []

        def boom(topic, vid, **kw):
            calls.append(vid)
            raise RuntimeError('HTTP 403 upload: {"reason": "quotaExceeded"}')
        yu.run, yu.check_auth = boom, lambda: None
        for k in ("YOUTUBE_CLIENT_ID", "YOUTUBE_CLIENT_SECRET", "YOUTUBE_REFRESH_TOKEN"):
            os.environ[k] = "x"
        gh.files["economic/source/e-2026-10/upload.md"] = sheet("e-2026-10")
        gh.files["economic/source/e-2026-10/e-2026-10.txt"] = b"x"
        gh.files["economic/source/e-2026-10/e-2026-10.srt"] = b"x"
        with redirect_stdout(io.StringIO()) as out:
            code = pu.main([])
        text = out.getvalue()
        self.assertEqual(code, 1)
        self.assertIn("| a-2026-10 | no_video |", text)       # Drive 에 영상 없음
        self.assertIn("| c-2026-10 | failed |", text)
        self.assertIn("| e-2026-10 | not_run |", text)         # 할당량 초과 뒤 멈춤
        self.assertEqual(calls, ["c-2026-10"])
        self.assertEqual(gh.puts, [])


class DriveTest(Base):
    def test_upload_new_then_skip(self):
        src = self.root / "economic/out/v-2026-10/final_1080p.mp4"
        src.parent.mkdir(parents=True)
        src.write_bytes(b"0123456789" * 1000)
        (self.root / "economic/source/v-2026-10").mkdir(parents=True)
        want = hashlib.md5(src.read_bytes()).hexdigest()
        state = {"files": []}
        log = []

        def fake_call(method, url, token, data=None, headers=None):
            log.append((method, url.split("?")[0]))
            if method == "GET" and "/drive/v3/files" in url:
                q = url.split("q=")[1]
                if "folder" in q:
                    return 200, {}, {"files": [{"id": "FOLDER", "name": "x"}]}
                return 200, {}, {"files": state["files"]}
            if method == "POST":
                meta = json.loads(data)
                self.assertEqual(meta["name"], "v-2026-10.mp4")
                self.assertEqual(meta["parents"], ["FOLDER"])
                return 200, {"Location": "https://upload/session"}, {}
            if method == "PUT":
                f = {"id": "NEW", "name": "v-2026-10.mp4", "md5Checksum": want, "size": str(src.stat().st_size)}
                state["files"] = [f]
                return 200, {}, f
            raise AssertionError((method, url))
        old = dv.call
        dv.call = fake_call
        try:
            with redirect_stdout(io.StringIO()):
                rec = dv.upload("economic", "v-2026-10", token="tok")
                rec2 = dv.upload("economic", "v-2026-10", token="tok")
        finally:
            dv.call = old
        self.assertEqual(rec["fileId"], "NEW")
        self.assertEqual(rec["md5"], want)
        self.assertEqual(rec["path"], "내 드라이브/youtube/economic/v-2026-10.mp4")
        saved = json.loads((self.root / "economic/source/v-2026-10/drive.json").read_text("utf-8"))
        self.assertEqual(saved["fileId"], "NEW")
        self.assertEqual(rec2["fileId"], "NEW")
        self.assertEqual(sum(1 for m, _ in log if m == "PUT"), 1)            # 두 번째는 같은 md5 라 건너뜀

    def test_local_roots_drive_dir(self):
        d = self.root / "My Drive" / "youtube" / "economic"
        d.mkdir(parents=True)
        (d / "v-2026-10.mp4").write_bytes(b"x")
        os.environ["DRIVE_DIR"] = str(self.root / "My Drive")
        self.assertEqual(dv.local_video("economic", "v-2026-10"), d / "v-2026-10.mp4")
        self.assertIsNone(dv.local_video("economic", "w-2026-10"))


class ThumbnailTest(Base):
    def test_pillow_when_no_ffmpeg(self):
        try:
            from PIL import Image
        except ImportError:
            self.skipTest("Pillow 없음")
        img = self.root / "thumbnail_1.webp"
        Image.new("RGB", (1672, 941), (200, 30, 30)).save(img, "WEBP")
        real = subprocess.run

        def no_ffmpeg(cmd, *a, **k):
            if cmd and cmd[0] in ("ffprobe", "ffmpeg"):
                raise FileNotFoundError(cmd[0])
            return real(cmd, *a, **k)
        subprocess.run = no_ffmpeg
        try:
            with redirect_stdout(io.StringIO()):
                out = yu.prepare_thumbnail(img, self.root / "out")
        finally:
            subprocess.run = real
        self.assertEqual(out.suffix, ".jpg")
        with Image.open(out) as im:
            self.assertEqual(im.size, (1280, 720))
        self.assertLessEqual(out.stat().st_size, yu.THUMB_MAX)


if __name__ == "__main__":
    unittest.main()
