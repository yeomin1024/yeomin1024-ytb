#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-11-16 — 바깥에서 만든 내레이션(사용자가 올린 mp3)을 대본 문장에 맞춤 — 짧은 쉼(-30dB·0.04초)까지 말 덩어리로 나누고,
#          덩어리를 차례대로 묶어 문장마다 ① 길이 ÷ (음절 × 평균 속도) ② 음절 봉우리 수(소리 크기 봉우리 — 음절 수 어림) ÷ 음절이
#          1 에 가깝고 ③ 경계 쉼이 길수록 낫게 (동적 계획법). 길이만 보던 첫 시도는 쉼 없이 이어 읽은 문장 경계(AI 안경 쇼츠 10·11번)를 못 찾았음. 결과 = render.mjs sync 가 읽는
#          tts_narration.json(문장 시작·끝) + <영상ID>.srt(한 문장 = 자막 하나, srt_tool.cue_split). 음성 인식 없이 길이만 보므로
#          덩어리 수 < 문장 수이거나 맞춤 오차가 크면 경고 — 그때는 사람 귀로 확인.
#          사용자 지시 2026-11-16 "음성은 이걸로 하고 … 다 되면 영상 만들어" (AI 안경 쇼츠 — Kaggle TTS 대신 올린 음성).
"""
  python3 tools/external_audio_align.py <주제> <영상ID> <음성.mp3> [--noise -40] [--min-sil 0.12] [--dry-run]
    → <대본 폴더>/narration.mp3 (복사) · tts_narration.json · <영상ID>.srt
  대본 폴더: 롱폼 <주제>/source/<영상ID>/ · 쇼츠(<영상ID>-shorts) <주제>/source/<영상ID 앞부분>/shorts/ (tts_narration.py 와 같음)
로그: [STAGE] [시각] key=value … · 연구·교육용 도구.
"""
from __future__ import annotations

import argparse
import json
import math
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import srt_tool  # noqa: E402
import tts_narration as tn  # noqa: E402  (read_script·script_sha — 대본 해시를 TTS 도구와 같게)

VERSION = "v1.0"


def log(stage, **kv):
    print(f"[{stage}] [{time.strftime('%Y-%m-%dT%H:%M:%S')}] " + " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) and ' ' in v else v}" for k, v in kv.items()), flush=True)


def die(stage, msg, nxt):
    log(stage, level="error", error=msg, next=nxt)
    raise SystemExit(1)


def probe(path: Path) -> float:
    try:
        out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
                             capture_output=True, text=True, check=True).stdout.strip()
        return float(out)
    except (subprocess.CalledProcessError, ValueError) as e:
        die("LOAD", f"ffprobe 실패 {e}", "음성 파일이 mp3/wav 인지 확인")


def chunks(path: Path, noise: float, min_sil: float, dur: float):
    """ffmpeg silencedetect → 말 덩어리 [(시작, 끝, 뒤 쉼 길이)] (앞뒤 무음 뺌)."""
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(path), "-af", f"silencedetect=noise={noise}dB:d={min_sil}", "-f", "null", "-"],
                       capture_output=True, text=True)
    st = [float(x) for x in re.findall(r"silence_start: ([0-9.]+)", r.stderr)]
    en = [float(x) for x in re.findall(r"silence_end: ([0-9.]+)", r.stderr)]
    sil = list(zip(st, en + [dur] * (len(st) - len(en))))
    out, cur = [], 0.0
    for a, b in sil:
        if a - cur > 0.03:
            out.append((cur, a, b - a))
        cur = b
    if dur - cur > 0.03:
        out.append((cur, dur, 0.0))
    return out


def peaks(path: Path):
    """음절 봉우리 시각 — 10ms 창 소리 크기(dB)를 50ms 로 고른 뒤, ±80ms 안 최고이고 -35dB 넘고 양옆 150ms 골보다 3dB 높은 점."""
    import numpy as np
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), "-ac", "1", "-ar", "16000", "-f", "s16le", "-"], capture_output=True, check=True).stdout
    x = np.frombuffer(raw, dtype=np.int16).astype(float) / 32768
    hop, win = 160, 400
    n = max(0, (len(x) - win) // hop)
    fr = np.sqrt(np.array([np.mean(x[i * hop:i * hop + win] ** 2) for i in range(n)]) + 1e-9)
    s = np.convolve(20 * np.log10(fr), np.ones(5) / 5, "same")
    return [i * hop / 16000 for i in range(16, len(s) - 16)
            if s[i] == s[i - 8:i + 9].max() and s[i] > -35 and s[i] - min(s[i - 15:i].min(), s[i + 1:i + 16].min()) > 3]


def align(ch, syl, pk):
    """덩어리 ch 를 차례대로 len(syl) 묶음으로. 비용 = Σ [log(길이/기대 길이)² + log((봉우리+1)/(기대 봉우리+1))² − 0.6×min(경계 쉼, 0.6)]
    · 기대 길이 = 음절 × (전체 말 길이 ÷ 전체 음절) · 기대 봉우리 = 음절 × (전체 봉우리 ÷ 전체 음절)."""
    n, m = len(ch), len(syl)
    if n < m:
        return None
    rate = (ch[-1][1] - ch[0][0]) / sum(syl)
    pr = len(pk) / sum(syl)
    cnt = lambda a, b: sum(a <= p <= b for p in pk)  # noqa: E731
    INF = float("inf")
    best = [[INF] * (n + 1) for _ in range(m + 1)]
    prev = [[-1] * (n + 1) for _ in range(m + 1)]
    best[0][0] = 0.0
    for i in range(1, m + 1):
        for j in range(i, n - (m - i) + 1):           # 문장 i 가 덩어리 j 에서 끝남
            for k in range(i - 1, j):                 # 문장 i 가 덩어리 k+1 에서 시작
                if best[i - 1][k] == INF:
                    continue
                a, b = ch[k][0], ch[j - 1][1]
                gap = ch[j - 1][2] if j < n else 0.6
                dr = math.log((b - a) / (syl[i - 1] * rate))
                prr = math.log((cnt(a, b) + 1) / (syl[i - 1] * pr + 1))
                c = best[i - 1][k] + dr * dr + prr * prr - 0.6 * min(gap, 0.6)
                if c < best[i][j]:
                    best[i][j], prev[i][j] = c, k
    if best[m][n] == INF:
        return None
    cuts, j = [], n
    for i in range(m, 0, -1):
        k = prev[i][j]
        cuts.append((k, j))
        j = k
    cuts.reverse()
    return [(ch[k][0], ch[j - 1][1]) for k, j in cuts], rate, best[m][n], pr, cnt


def ts(t):
    h, r = divmod(t, 3600)
    mnt, s = divmod(r, 60)
    return f"{int(h):02d}:{int(mnt):02d}:{int(s):02d},{int(round((s - int(s)) * 1000)):03d}"


def main():
    ap = argparse.ArgumentParser(description="바깥 내레이션 → 문장 시각(tts_narration.json)·자막(SRT)")
    ap.add_argument("topic")
    ap.add_argument("vid")
    ap.add_argument("audio")
    ap.add_argument("--noise", type=float, default=-30.0, help="쉼으로 볼 크기 dB (기본 -30)")
    ap.add_argument("--min-sil", type=float, default=0.04, help="쉼으로 볼 최소 길이 초 (기본 0.04)")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    src = tn.src_dir(a.topic, a.vid)
    txt = src / f"{a.vid}.txt"
    if not txt.is_file():
        die("LOAD", f"대본 없음 {txt.relative_to(ROOT)}", "대본 폴더·영상ID 확인")
    audio = Path(a.audio)
    if not audio.is_file():
        die("LOAD", f"음성 없음 {audio}", "경로 확인")
    rows, cards = tn.read_script(txt)
    sents = [t for t, _ in rows]
    syl = [max(1, srt_tool.syllables(t)) for t in sents]
    dur = probe(audio)
    log("LOAD", tool=f"external_audio_align.py {VERSION}", script=str(txt.relative_to(ROOT)), sentences=len(sents), syllables=sum(syl), audio=audio.name, audio_s=round(dur, 2))
    ch = chunks(audio, a.noise, a.min_sil, dur)
    log("CHUNK", chunks=len(ch), noise_db=a.noise, min_sil_s=a.min_sil, first=f"{ch[0][0]:.2f}" if ch else "-", last=f"{ch[-1][1]:.2f}" if ch else "-")
    pk = peaks(audio)
    log("PEAKS", peaks=len(pk), per_syl=f"{len(pk) / sum(syl):.2f}")
    res = align(ch, syl, pk)
    if not res:
        die("ALIGN", f"말 덩어리 {len(ch)}개 < 문장 {len(sents)}개", "--min-sil 을 0.03 처럼 줄이거나 --noise 를 -28 로 올려 다시")
    spans, rate, cost, pr, cnt = res
    worst = 0.0
    items = []
    for n, ((s, e), t, sy, (_, part)) in enumerate(zip(spans, sents, syl, rows), 1):
        ratio = (e - s) / (sy * rate)
        pratio = (cnt(s, e) + 1) / (sy * pr + 1)
        worst = max(worst, abs(math.log(ratio)), abs(math.log(pratio)))
        items.append({"n": n, "part": part, "text": t, "start": round(s, 3), "end": round(e, 3), "role": "host"})
        log("ALIGN", n=n, start=f"{s:.2f}", end=f"{e:.2f}", sec=f"{e - s:.2f}", syl=sy, ratio=f"{ratio:.2f}", peak_ratio=f"{pratio:.2f}", text=t[:24])
    log("ALIGN", rate_syl_per_s=f"{1 / rate:.2f}", cost=f"{cost:.3f}", worst_ratio=f"{math.exp(worst):.2f}",
        verdict="✅" if math.exp(worst) < 1.45 else "⚠️ 귀로 확인 — 어떤 문장이 길이와 크게 어긋남")
    layout = srt_tool.layout_of(txt)
    blocks = []
    for it in items:
        parts = srt_tool.cue_split(it["text"], layout)
        w = [max(1, srt_tool.syllables(p.replace("\n", " "))) for p in parts]
        t0, tot = it["start"], it["end"] - it["start"]
        for p, wi in zip(parts, w):
            d = tot * wi / sum(w)
            blocks.append((t0, t0 + d, p))
            t0 += d
    srt = "\n\n".join(f"{i}\n{ts(s)} --> {ts(e)}\n{p}" for i, (s, e, p) in enumerate(blocks, 1)) + "\n"
    meta = {"tool": f"external_audio_align.py {VERSION}", "created": time.strftime("%Y-%m-%dT%H:%M:%S"), "topic": a.topic, "id": a.vid,
            "script": str(txt.relative_to(ROOT)), "script_sha1": tn.script_sha(rows, cards), "sentences": len(items), "seconds": round(dur, 2),
            "engine": "external", "source_audio": audio.name, "items": items,
            "note": "사용자가 올린 음성 — 쉼 자리로 문장 시각을 맞춤 (음성 인식 아님)"}
    if a.dry_run:
        log("WRITE", dry_run=True, subs=len(blocks))
        return 0
    dst = src / "narration.mp3"
    if audio.resolve() != dst.resolve():
        shutil.copyfile(audio, dst)
    (src / "tts_narration.json").write_text(json.dumps(meta, ensure_ascii=False, indent=1) + "\n", "utf-8")
    (src / f"{a.vid}.srt").write_text(srt, "utf-8")
    log("WRITE", narration=str(dst.relative_to(ROOT)), meta="tts_narration.json", srt=f"{a.vid}.srt", subs=len(blocks),
        next=f"node video/render/render.mjs sync {a.topic} {a.vid}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
