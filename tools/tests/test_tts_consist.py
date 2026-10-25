# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-25 — tools/tts_narration.py v1.16 '고르기' 시험 (사용자 지시 2026-10-25 "오디오가 자꾸 소리가 갑자기 작아지고
#          목소리도 아예 달라지는 부분이 있는데 좀 일정하게 되도록 고쳐봐"): 사람 목소리 비슷한 합성음(배음 + 포먼트)으로
#          1) 보통 문장은 걸리지 않음 2) 끝 흐림·문장 중간 목소리 바뀜·작은 문장은 걸림 3) level_even 이 크기를 맞추고 흐린 끝을 올림
#          4) consist_pass 가 걸린 문장을 새 시드로 다시 만들고, 더 나쁘면 원래 것을 두고 다음 실행에선 되풀이하지 않음.
#          임시 폴더만 씀 — 모델·네트워크·GitHub 없음.
"""python3 -m unittest tools.tests.test_tts_consist -v     (저장소 최상위에서)"""
import json
import sys
import tempfile
import types
import unittest
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import tts_narration as tn  # noqa: E402

SR = 24000
NORMAL = (550, 1500, 2600)      # 보통 목소리의 포먼트(Hz)
OTHER = (320, 2300, 3300)       # 다른 목소리(모양이 다름)


def voice(dur, seed, f0=118.0, formants=NORMAL, amp=0.08):
    """배음(f0 의 배수, 7kHz 까지) × 포먼트 봉우리 + 음절 떨림(초당 5번) — 말소리 비슷한 소리."""
    rng = np.random.default_rng(seed)
    t = np.arange(int(dur * SR)) / SR
    f = f0 * (1 + 0.03 * np.sin(2 * np.pi * 0.7 * t + rng.uniform(0, 6)))
    ph = 2 * np.pi * np.cumsum(f) / SR
    y = np.zeros_like(t)
    for k in range(1, int(7000 / f0)):
        hz = k * f0
        a = sum(np.exp(-0.5 * ((hz - fm) / 180) ** 2) for fm in formants) + 0.02
        y += a / k ** 0.5 * np.sin(k * ph + rng.uniform(0, 6))
    env = 0.55 + 0.45 * np.abs(np.sin(np.pi * 5 * t + rng.uniform(0, 3)))
    y = y * env
    y = y / (np.sqrt(np.mean(y ** 2)) + 1e-12) * amp
    return y.astype(np.float32) * (1 + 0.05 * rng.standard_normal())


def faded(dur, seed, tail=1.4, drop_db=16):
    x = voice(dur, seed)
    n = int(tail * SR)
    x[-n:] *= 10 ** (-drop_db / 20)
    return x


def timbre_change(dur, seed, mid=1.6):
    x = voice(dur, seed)
    a, b = int((dur - mid) / 2 * SR), int((dur + mid) / 2 * SR)
    x[a:b] = voice(dur, seed + 99, formants=OTHER)[a:b]
    return x


def center_of(n=14):
    return tn.voice_center([tn.voice_print(voice(3.5 + 0.3 * (i % 4), i), SR) for i in range(n)])


class VoicePrint(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.c = center_of()

    def test_center_built(self):
        self.assertIsNotNone(self.c)
        self.assertGreaterEqual(self.c["n"], tn.CONSIST_MIN)
        self.assertGreaterEqual(self.c["shape_tol"], tn.SHAPE_TOL_FLOOR)
        self.assertGreaterEqual(self.c["win_tol"], tn.WIN_SHAPE_FLOOR)

    def test_too_few_sentences(self):
        self.assertIsNone(tn.voice_center([tn.voice_print(voice(3, i), SR) for i in range(tn.CONSIST_MIN - 1)]))

    def test_normal_not_flagged(self):
        for s in range(100, 110):
            iss, dev, m = tn.consist_issues(tn.voice_print(voice(4.0, s), SR), self.c)
            self.assertEqual(iss, [], (s, m))
            self.assertEqual(dev, 0.0)

    def test_fade_flagged(self):
        iss, dev, m = tn.consist_issues(tn.voice_print(faded(4.5, 7), SR), self.c)
        self.assertTrue(any(i.startswith("끝 흐림") for i in iss), (iss, m))
        self.assertGreater(m["fade_s"], 1.0)
        self.assertGreater(dev, 0)

    def test_timbre_change_flagged(self):
        iss, dev, m = tn.consist_issues(tn.voice_print(timbre_change(5.0, 8), SR), self.c)
        self.assertTrue(any(i.startswith("문장 중간") for i in iss), (iss, m))

    def test_whole_other_voice_flagged(self):
        iss, _, m = tn.consist_issues(tn.voice_print(voice(4.0, 9, formants=OTHER), SR), self.c)
        self.assertTrue(any(i.startswith("목소리 모양") for i in iss), (iss, m))

    def test_quiet_sentence_flagged(self):
        iss, _, m = tn.consist_issues(tn.voice_print(voice(4.0, 10) * 10 ** (-7 / 20), SR), self.c)
        self.assertTrue(any(i.startswith("크기 ") for i in iss), (iss, m))
        self.assertAlmostEqual(m["level_dev"], -7, delta=1.5)

    def test_patch_center_skips_level(self):
        """부분 다시 만들기 기준(level None): 크기는 보지 않고, 끝 흐림은 문장 자기 크기로 본다."""
        c = dict(self.c, level=None)
        iss, _, _ = tn.consist_issues(tn.voice_print(voice(4.0, 11) * 0.3, SR), c)
        self.assertEqual(iss, [])
        iss, _, _ = tn.consist_issues(tn.voice_print(faded(4.5, 12), SR), c)
        self.assertTrue(any(i.startswith("끝 흐림") for i in iss), iss)


class LevelEven(unittest.TestCase):
    def test_levels_matched_and_tail_lifted(self):
        clips = [voice(3.5, i, amp=0.08 * 10 ** (d / 20)) for i, d in enumerate([0, 1, -1, 0, -5, 2, 0])]
        clips.append(faded(4.5, 50))
        before = [tn.voiced_rms_db(x, SR) for x in clips]
        out, adj = tn.level_even(clips, ["host"] * len(clips), SR)
        after = [tn.voiced_rms_db(x, SR) for x in out]
        self.assertGreater(np.ptp(before[:7]), 6)
        self.assertLess(np.ptp(after[:7]), 1.5, after)       # 보통 문장 크기 차이 1.5dB 안
        self.assertGreater(adj[4][0], 4)                       # -5dB 문장은 올림
        self.assertGreater(adj[7][1], 4)                       # 흐린 끝은 ride 로 올림
        tail = lambda x: tn.voiced_rms_db(x[-int(1.2 * SR):], SR) - tn.voiced_rms_db(x[:int(2.5 * SR)], SR)
        self.assertLess(tail(clips[7]), -14)
        self.assertGreater(tail(out[7]), -11)                  # 16dB 작던 끝이 6dB 가까이 올라감
        self.assertLess(adj[0][1], 1.0)                        # 보통 문장은 거의 그대로
        pk = max(float(np.max(np.abs(x))) for x in clips)
        self.assertLessEqual(max(float(np.max(np.abs(x))) for x in out), pk * 1.0001)   # 올려도 최고점은 그대로

    def test_ride_keeps_silence(self):
        x = np.concatenate([voice(2, 1), np.zeros(SR, np.float32), voice(2, 2)])
        y, r = tn.ride(x, SR)
        self.assertTrue(np.all(y[2 * SR + 2400: 3 * SR - 2400] == 0))   # 무음은 무음 그대로
        self.assertLess(r, 1.0)


class StubEngine:
    """시드 차례대로 정해 둔 소리를 낸다 (make_sentence 의 생성기 자리)."""

    def __init__(self, plan):
        self.plan, self.calls = plan, 0

    def synth(self, text, spec, seed, max_new):
        self.calls += 1
        return self.plan(self.calls, seed), SR

    def describe(self, spec):
        return {"engine": "stub", "model": "stub", "language": "-", "dtype": "-", "gen": {}}


TEXT = "가나다라마바사아자차카타파하가나다라마바"      # 20음절 → 4초면 5음절/초 (속도 검사 통과)


def run_pass(engine, cache, n_bad=3):
    """문장 12개(그중 n_bad 번은 끝 흐림)를 캐시에 만들고 consist_pass 를 돌린다."""
    args = types.SimpleNamespace(max_tries=2, no_consist=False)
    items, metas = [], {}
    for n in range(1, 13):
        spec = {"engine": "clone", "seed": 1000 + n, "instruct": "", "ref_f0": 118.0, "f0_tol": 0.3, "ref_sha": "x"}
        it = {"n": n, "role": "host", "tts": f"{TEXT}{n}", "spec": spec, "syl": 20}
        items.append(it)
        x = faded(4.0, n) if n == n_bad else voice(4.0, n)
        key = tn.cache_key(engine, it["tts"], spec)
        tn.write_wav(cache / f"{key}.wav", x, SR)
        meta = {"key": key, "ok": True, "issues": [], "warns": [], "tried": [1], "dur": 4.0}
        (cache / f"{key}.json").write_text(json.dumps(meta), "utf-8")
        metas[n] = dict(meta, wav=str(cache / f"{key}.wav"))
    return tn.consist_pass(engine, cache, items, metas, args, "test"), items


class ConsistPass(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.cache = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_redo_fixes(self):
        eng = StubEngine(lambda k, seed: np.concatenate([np.zeros(2400, np.float32), voice(4.0, 500 + k), np.zeros(2400, np.float32)]))
        metas, _ = run_pass(eng, self.cache)
        self.assertEqual(eng.calls, 1)                          # 걸린 문장(3번) 하나만, 첫 시도에 통과
        self.assertTrue(metas[3]["ok"], metas[3]["issues"])
        self.assertEqual(metas[3]["tried"], [1, 2])             # 전에 쓴 시도 다음 시드로
        self.assertNotIn("consist_kept", metas[3])

    def test_worse_redo_keeps_original_once(self):
        eng = StubEngine(lambda k, seed: faded(4.0, 600 + k, tail=2.5, drop_db=20))
        metas, items = run_pass(eng, self.cache)
        self.assertEqual(eng.calls, 2)                          # max_tries 2 번 모두 더 나쁨
        self.assertFalse(metas[3]["ok"])
        self.assertTrue(metas[3]["consist_kept"])
        self.assertTrue(any(i.startswith("끝 흐림") for i in metas[3]["issues"]))
        x, _ = tn.read_wav(metas[3]["wav"])
        self.assertAlmostEqual(len(x) / SR, 4.0, delta=0.01)   # 원래 파일 되돌림
        meta_disk = json.loads(Path(metas[3]["wav"]).with_suffix(".json").read_text("utf-8"))
        self.assertTrue(meta_disk["consist_kept"])
        self.assertEqual(meta_disk["tried"], [1, 2, 3])
        # 다음 실행: 캐시 메타에 consist_kept → 같은 시도를 되풀이하지 않음
        args = types.SimpleNamespace(max_tries=2, no_consist=False)
        metas2 = {it["n"]: dict(json.loads((self.cache / f"{tn.cache_key(eng, it['tts'], it['spec'])}.json").read_text("utf-8")),
                                wav=str(self.cache / f"{tn.cache_key(eng, it['tts'], it['spec'])}.wav")) for it in items}
        tn.consist_pass(eng, self.cache, items, metas2, args, "test")
        self.assertEqual(eng.calls, 2)

    def test_no_consist_flag(self):
        eng = StubEngine(lambda k, seed: voice(4.0, k))
        args = types.SimpleNamespace(no_consist=True)
        self.assertEqual(tn.consist_pass(eng, self.cache, [], {1: {}}, args, "test"), {1: {}})
        self.assertEqual(eng.calls, 0)


if __name__ == "__main__":
    unittest.main()
