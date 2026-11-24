#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-11-24 — 신규: 내레이션 문장마다 시작·끝 가장자리 정리 (시각은 그대로)
#   사용자 지시 2026-11-24 "음성 끝이나 시작에 이상한 음성이 잘려서 들어가는데 너가 문장별로 시작, 끝 부분을 딱 잘라서 그런일 없도록 해".
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.0 | 2026-11-24 | 최초 — 말 시작 앞·말 끝 뒤 무음 + 짧은 코사인 경사, 끝이 소리 나는 채로 잘린 문장은 60ms 페이드 | plan · apply · main |
"""문장마다 '말소리 앞'과 '말소리 뒤'를 정리한다 — tts_narration.json 의 문장 시각(start·end)은 바꾸지 않는다.

까닭: tts_narration.py 는 문장 파일 앞뒤 무음을 자를 때 60ms 여유(TRIM_PAD)를 남기고, 속도 맞춤(atempo)도 한다.
  그래서 ① 말 시작 앞 여유에 숨·잡음 조각이 남거나 ② 말끝이 아직 소리 나는 채로 잘려(예: -30dB 에서 바로 -84dB) '뚝' 끊긴
  조각이 들린다 (adhd-ab-2026-11 문장 42 「…양복인데도요.」 끝).
하는 일 (5ms 구간 RMS dB):
  - 시작: 문장 구간 안에서 처음으로 ON_DB(-45dB)를 넘는 곳 = 말 시작. 그보다 PRE(15ms) 앞까지 무음, 그 15ms 는 0→1 코사인 경사.
  - 끝: 마지막으로 ON_DB 를 넘는 곳 = 말 끝.
      · 말 끝이 문장 구간 끝에서 ABRUPT(15ms) 안이면 '소리 난 채로 잘림' → 구간 끝 FADE_ABRUPT(60ms) 동안 1→0 코사인.
      · 아니면 말 끝 + POST(10ms) 부터 FADE(30ms) 동안 1→0, 그 뒤 무음.
  - 문장 사이·맨 앞·맨 뒤는 원래 무음이라 0 으로 둔다.
  - 말소리 자체(ON_DB 를 넘는 곳)는 건드리지 않는다 — 바뀌는 것은 가장자리의 작은 소리와 끝 경사뿐.
결과: 원본을 덮어쓰기 전 같은 시각인지(상호상관 지연 0) 확인 · 바뀐 문장 표 `<대본 폴더>/edge_clean.md`.
실행: python3 tools/edge_clean.py <주제> <영상ID> [--dry-run] [--log-level DEBUG]
※ 연구·교육용 영상 도구.
"""
from __future__ import annotations

import argparse
import json
import logging
import subprocess
import sys
import time
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
SR = 24000
HOP = 0.005          # 5ms 구간
ON_DB = -45.0        # 이 위 = 말소리 (tts_narration SIL_DB 와 같음)
PRE = 0.015          # 말 시작 앞 경사
POST = 0.010         # 말 끝 뒤 그대로 두는 여유
FADE = 0.030         # 말 끝 뒤 경사
ABRUPT = 0.015       # 말 끝이 구간 끝에서 이 안이면 '잘림'
FADE_ABRUPT = 0.060  # 잘린 끝의 경사
log = logging.getLogger("edge_clean")


def stamp(stage: str, **kv) -> None:
    log.info("[%s] [%s] %s", stage, time.strftime("%Y-%m-%dT%H:%M:%S"), " ".join(f"{k}={v}" for k, v in kv.items()))


def decode(path: Path) -> np.ndarray:
    try:
        raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                             capture_output=True, check=True).stdout
    except (OSError, subprocess.CalledProcessError) as ex:
        raise SystemExit(f"[LOAD] {path} 를 읽지 못함 ({ex}) — ffmpeg·파일 확인")
    return np.frombuffer(raw, dtype=np.float32).copy()


def frame_db(a: np.ndarray) -> np.ndarray:
    h = int(HOP * SR)
    n = len(a) // h
    return 20 * np.log10(np.sqrt(np.mean(a[: n * h].reshape(n, h) ** 2, axis=1) + 1e-12))


def ramp(n: int, up: bool) -> np.ndarray:
    x = 0.5 - 0.5 * np.cos(np.linspace(0, np.pi, max(1, n)))
    return x if up else x[::-1]


def plan(a: np.ndarray, items: list[dict]) -> tuple[np.ndarray, list[dict]]:
    """문장마다 이득 곡선(0~1)과 바뀐 내용 — 이득 곡선 밖(문장 사이)은 0."""
    db = frame_db(a)
    g = np.zeros(len(a), dtype=np.float32)
    rows = []
    for it in items:
        s, e = int(it["start"] * SR), min(len(a), int(it["end"] * SR))
        f0, f1 = int(it["start"] / HOP), min(len(db), int(it["end"] / HOP))
        loud = np.where(db[f0:f1] > ON_DB)[0]
        if loud.size == 0:
            log.warning("[PLAN] 문장 %s 에 말소리가 없음 — 건드리지 않음", it["n"])
            g[s:e] = 1
            continue
        on = int((f0 + loud[0]) * HOP * SR)
        off = int((f0 + loud[-1] + 1) * HOP * SR)
        a0 = max(s, on - int(PRE * SR))
        g[a0:on] = ramp(on - a0, True)
        abrupt = (e - off) <= int(ABRUPT * SR)
        if abrupt:
            b0 = e - int(FADE_ABRUPT * SR)
            g[on:b0] = 1
            g[b0:e] = ramp(e - b0, False)
            end_note = f"잘린 끝 → 끝 {FADE_ABRUPT * 1000:.0f}ms 페이드"
        else:
            b0 = min(e, off + int(POST * SR))
            b1 = min(e, b0 + int(FADE * SR))
            g[on:b0] = 1
            g[b0:b1] = ramp(b1 - b0, False)
            end_note = f"말끝 뒤 {(e - b1) / SR * 1000:.0f}ms 무음"
        pre_ms = (a0 - s) / SR * 1000
        pre_max = float(db[f0:max(f0 + 1, int(a0 / SR / HOP))].max()) if a0 > s else -120.0
        post_max = float(db[min(len(db) - 1, int(off / SR / HOP)) + 2:f1].max()) if f1 > int(off / SR / HOP) + 2 else -120.0
        rows.append({"n": it["n"], "pre_ms": round(pre_ms), "pre_max_db": round(pre_max, 1), "abrupt": abrupt,
                     "post_max_db": round(post_max, 1), "end": end_note, "text": it["text"]})
    return g, rows


def encode(a: np.ndarray, out: Path) -> None:
    try:
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-",
                        "-c:a", "libmp3lame", "-b:a", "160k", str(out)], input=a.astype(np.float32).tobytes(), check=True)
    except (OSError, subprocess.CalledProcessError) as ex:
        raise SystemExit(f"[WRITE] mp3 를 쓰지 못함 ({ex}) — ffmpeg libmp3lame 확인")


def lag(x: np.ndarray, y: np.ndarray, win: int = 2400) -> int:
    """y 가 x 보다 몇 표본 늦는지 (±win 안) — 다시 인코딩해도 시각이 그대로인지 확인."""
    n = min(len(x), len(y), SR * 60)
    c = np.correlate(y[win:n - win], x[:n], mode="valid")
    return int(np.argmax(c)) - win


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="내레이션 문장마다 시작·끝 가장자리 정리 (시각 그대로)")
    ap.add_argument("topic")
    ap.add_argument("video_id")
    ap.add_argument("--dry-run", action="store_true", help="덮어쓰지 않고 표만")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args(argv)
    logging.basicConfig(level=a.log_level, format="%(message)s")
    src = ROOT / a.topic / "source" / a.video_id
    audio, meta_p = src / "narration.mp3", src / "tts_narration.json"
    if not audio.is_file() or not meta_p.is_file():
        stamp("LOAD", level="error", msg="narration.mp3 또는 tts_narration.json 없음", path=src.relative_to(ROOT),
              next="Kaggle 셀로 오디오를 먼저 만든다")
        return 1
    meta = json.loads(meta_p.read_text("utf-8"))
    x = decode(audio)
    stamp("LOAD", audio=audio.relative_to(ROOT), sec=round(len(x) / SR, 2), sentences=len(meta["items"]))
    g, rows = plan(x, meta["items"])
    y = x * g
    changed = float(np.abs(y - x).max())
    speech = g > 0.999
    stamp("PLAN", abrupt=sum(r["abrupt"] for r in rows), muted_s=round(float((g == 0).sum()) / SR, 2),
          max_change=round(changed, 4), speech_kept=round(float(speech.mean()) * 100, 1))
    for r in rows:
        log.debug("[PLAN] n=%s pre_ms=%s pre_max_db=%s abrupt=%s end=%s", r["n"], r["pre_ms"], r["pre_max_db"], r["abrupt"], r["end"])
    lines = [f"# 내레이션 가장자리 정리 — {a.video_id}", "",
             f"> `tools/edge_clean.py` v1.0 · {time.strftime('%Y-%m-%d %H:%M')} · 사용자 지시 \"음성 끝이나 시작에 이상한 음성이 잘려서 들어가는데 너가 문장별로 시작, 끝 부분을 딱 잘라서 그런일 없도록 해\"",
             f"> 말소리 = 5ms RMS {ON_DB:.0f}dB 위 (건드리지 않음) · 시작 앞 {PRE * 1000:.0f}ms 경사 · 끝 뒤 {POST * 1000:.0f}ms 여유 + {FADE * 1000:.0f}ms 경사 · 소리 난 채로 잘린 끝은 {FADE_ABRUPT * 1000:.0f}ms 페이드 · 문장 시각(SRT·장면)은 그대로",
             "", "| 문장 | 시작 앞 무음 처리(ms) | 그 안 최대 dB | 끝 | 끝 뒤 최대 dB | 문장 |", "|---|---|---|---|---|---|"]
    for r in rows:
        lines.append(f"| {r['n']} | {r['pre_ms']} | {r['pre_max_db']} | {'⚠️ ' if r['abrupt'] else ''}{r['end']} | {r['post_max_db']} | {r['text'][:28]} |")
    if a.dry_run:
        print("\n".join(lines[:12]))
        stamp("DONE", dry_run=True)
        return 0
    tmp = src / "narration.edge_tmp.mp3"
    encode(y, tmp)
    z = decode(tmp)
    d = lag(y, z)
    if abs(d) > 2 or abs(len(z) - len(y)) > SR * 0.05:
        tmp.unlink(missing_ok=True)
        stamp("CHECK", level="error", lag_samples=d, len_in=len(y), len_out=len(z), next="인코딩 지연 — 덮어쓰지 않음")
        return 1
    tmp.replace(audio)
    (src / "edge_clean.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    stamp("DONE", audio=audio.relative_to(ROOT), lag_samples=d, report=(src / "edge_clean.md").relative_to(ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
