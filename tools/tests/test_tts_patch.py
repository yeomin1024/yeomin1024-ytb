# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-15 — tools/tts_narration.py v1.8 '부분 다시 만들기' 시험 (가짜 소리 --fake, 임시 폴더에 저장소 일부를 복사 — 네트워크·GitHub 없음)
r"""
  python3 -m unittest tools.tests.test_tts_patch -v     (저장소 최상위에서, ffmpeg 필요)

1) 처음 만들기(--fake) → 결과를 대본 폴더에 넣음(올리기 흉내)
2) 마지막 문장 글만 바꿈 → build 가 그 문장만 만들어 끼우는지: 앞 문장 시각 그대로, 앞부분 소리 거의 같음, 메타 patches·보고 절
3) 바뀐 문장이 20% 넘음 / --full → 전부 다시
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
import wave
from pathlib import Path

import numpy as np

REPO = Path(__file__).resolve().parent.parent.parent
VID = "patchtest-2026-10"
SCRIPT = """-도입
같은 돈인데 세금이 다릅니다.
두 사람의 차이는 순서입니다.
결론부터 말씀드리겠습니다.
-원칙
첫 번째 원칙은, 기준은 한 사람씩이라는 것입니다.
두 번째 원칙은, 꺼낼 때 세금을 낸다는 것입니다.
세 번째 원칙은, 첫해부터 연금으로 받는다는 것입니다.
-정리
오늘 내 통장부터 확인해 보세요.
끝까지 봐 주셔서 감사합니다.
"""


def ffmpeg():
    return shutil.which("ffmpeg")


def decode(path, sr=24000):
    r = subprocess.run([ffmpeg(), "-hide_banner", "-loglevel", "error", "-i", str(path), "-f", "s16le", "-ac", "1", "-ar", str(sr), "-"],
                       capture_output=True, check=True)
    return np.frombuffer(r.stdout, dtype="<i2").astype(np.float32) / 32767.0


@unittest.skipUnless(ffmpeg(), "ffmpeg 없음")
class TtsPatchTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name) / "repo"
        shutil.copytree(REPO / "tools", self.root / "tools", ignore=shutil.ignore_patterns("tests", "__pycache__"))
        (self.root / "voices" / "ref").mkdir(parents=True)
        for f in ("host.json", "storyteller.json"):
            shutil.copy2(REPO / "voices" / f, self.root / "voices" / f)
        for f in (REPO / "voices" / "ref").iterdir():
            shutil.copy2(f, self.root / "voices" / "ref" / f.name)
        self.src = self.root / "economic" / "source" / VID
        self.src.mkdir(parents=True)
        self.txt = self.src / f"{VID}.txt"
        self.txt.write_text(SCRIPT, encoding="utf-8")
        self.out = Path(self.tmp.name) / "out"
        self.env = {k: v for k, v in os.environ.items() if k not in ("GITHUB_TOKEN", "GH_TOKEN")}   # 시험은 절대 올리지 않음

    def tearDown(self):
        self.tmp.cleanup()

    def run_tool(self, *extra):
        r = subprocess.run([sys.executable, str(self.root / "tools" / "tts_narration.py"), "build", "economic", VID, "--fake",
                            "--out-dir", str(self.out), *extra], capture_output=True, text=True, env=self.env, cwd=self.root)
        self.assertEqual(r.returncode, 0, r.stdout[-3000:] + r.stderr[-3000:])
        return r.stdout

    def publish(self):
        """올리기 흉내: OUT/upload/… 의 세 파일을 대본 폴더로."""
        up = self.out / "upload" / "economic" / "source" / VID
        for f in ("narration.mp3", "tts_narration.json", "tts_report.md"):
            shutil.copy2(up / f, self.src / f)
        return json.loads((self.src / "tts_narration.json").read_text("utf-8"))

    def test_patch_last_sentence(self):
        log1 = self.run_tool()
        self.assertIn('mode="전부 만들기"', log1)
        base = self.publish()
        old_audio = decode(self.src / "narration.mp3")
        # 마지막 문장 글만 바꿈 (사용자 지시 2026-10-15 끝인사)
        self.txt.write_text(SCRIPT.replace("끝까지 봐 주셔서 감사합니다.", "시청해주셔서 감사합니다."), encoding="utf-8")
        log2 = self.run_tool()
        self.assertIn('mode="바뀐 문장만"', log2)
        self.assertIn("patched=8", log2)
        new = self.publish()
        n = len(base["items"])
        self.assertEqual(new["sentences"], n)
        self.assertEqual(new["items"][-1]["text"], "시청해주셔서 감사합니다.")
        for a, b in zip(base["items"][:-1], new["items"][:-1]):   # 앞 문장 시각은 그대로
            self.assertEqual((a["start"], a["end"]), (b["start"], b["end"]))
        self.assertEqual(new["patches"][-1]["sentences"], [8])
        self.assertEqual(new["patches"][-1]["texts"]["8"]["old"], "끝까지 봐 주셔서 감사합니다.")
        self.assertNotEqual(new["script_sha1"], base["script_sha1"])
        # 앞부분 소리: 다시 압축한 차이만 (상관 0.99 이상)
        new_audio = decode(self.src / "narration.mp3")
        cut = int(base["items"][-2]["end"] * 24000)
        c = np.corrcoef(old_audio[:cut], new_audio[:cut])[0, 1]
        self.assertGreater(c, 0.99)
        # 길이 = 앞부분 + 새 마지막 문장 + 끝 쉼
        tail = base["gaps"]["tail"]
        self.assertAlmostEqual(new["seconds"], new["items"][-1]["end"] + tail, delta=0.02)
        rep = (self.src / "tts_report.md").read_text("utf-8")
        self.assertIn("## 부분 다시 만들기", rep)
        self.assertIn("부분 다시 만듦", rep)
        # 저장소가 지금 대본과 같으면 다음 실행은 '바뀐 문장 없음' → 전부(=has_audio 는 all 이 건너뜀)
        r = subprocess.run([sys.executable, str(self.root / "tools" / "tts_narration.py"), "check", "economic", VID, "--fake"],
                           capture_output=True, text=True, env=self.env, cwd=self.root)
        self.assertEqual(r.returncode, 0, r.stdout[-2000:])

    def test_full_when_many_changed_or_flag(self):
        self.run_tool()
        self.publish()
        many = SCRIPT.replace("같은 돈인데", "같은 금액인데").replace("두 사람의 차이는", "두 사람이 다른 것은")
        self.txt.write_text(many, encoding="utf-8")   # 8문장 중 2개 > 20%(1개)
        log = self.run_tool()
        self.assertIn('mode="전부 만들기"', log)
        self.assertIn("바뀐 문장 2개 > 1개", log)
        self.publish()
        self.txt.write_text(many.replace("끝까지 봐 주셔서 감사합니다.", "시청해주셔서 감사합니다."), encoding="utf-8")
        log = self.run_tool("--full")
        self.assertIn('mode="전부 만들기"', log)
        self.assertIn("--full", log)

    def test_full_when_sentence_count_changes(self):
        self.run_tool()
        self.publish()
        self.txt.write_text(SCRIPT + "다음 영상에서 뵙겠습니다.\n", encoding="utf-8")
        log = self.run_tool()
        self.assertIn("문장 수가 다름 (8 → 9)", log)


if __name__ == "__main__":
    unittest.main()
