#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-15 — 사용자 지시 "영상 만들었으면 각 영상 압축해서 저장소에 올리고 실행하면 해당 영상 유튜브에 자동 예약으로
#          1시간 후 업로드하는 colab 코드": 완성 영상(<주제>/out/<영상ID>/final_1080p.mp4, git 에 없음)을 줄여 저장소에 넣을 압축본
#          <주제>/source/<영상ID>/final_1080p.mp4 + 기록 final_1080p.json 을 만든다. Colab 업로드 셀이 이 파일을 올린다.
r"""
완성 영상을 저장소에 넣을 크기로 줄입니다 (화질은 눈으로 같게, 음량은 유튜브 기준 그대로).

  python tools/compress_video.py economic eunte-kkeonaeseugi-2026-10        # 영상 하나
  python tools/compress_video.py economic --all                             # out/ 에 완성 영상이 있는 영상 전부
  python tools/compress_video.py economic eunte-kkeonaeseugi-2026-10 --crf 21 --no-ssim

방법 (2026-10-15 시험: 은퇴 꺼내 쓰기 60초 구간)
  - 영상: H.264 CRF 23 · preset medium · tune animation (평평한 색 그림에 맞춤) — 원본(CRF 18 fast) 대비 SSIM 0.9993, 크기 -31%
  - 소리: AAC 96 kbps 단일 채널 48 kHz — 원본 169 kbps 와 음량 같음 (-14.3 LUFS, 트루 피크 -1.7 dBTP)
  - 확인: 길이 차이 0.1초 이하 · 음량 -15~-13 LUFS · 트루 피크 -1.5 dBTP 이하 (넘으면 소리는 원본 그대로 복사해 다시) ·
          SSIM 0.995 이상(아니면 경고) · 파일 95MB 이하 (GitHub 한 파일 100MB 한도, 50MB 넘으면 경고)
  - 기록: final_1080p.json (원본·압축본 크기·해시, 설정, SSIM, 음량, 만든 시각)
※ 연구·교육용 도구다. 영상 내용은 투자·세무 권유가 아니다.
"""
import argparse
import datetime as dt
import hashlib
import json
import logging
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VERSION = "v1.0"
CRF, PRESET, TUNE, AUDIO_BR = 23, "medium", "animation", "96k"
I_RANGE, TP_MAX, SSIM_MIN = (-15.0, -13.0), -1.5, 0.995
MB_WARN, MB_MAX = 50, 95
LOG = logging.getLogger("compress")


def log(stage, level=logging.INFO, **kv):
    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    LOG.log(level, f"[{stage}] [{now}] " + " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) and ' ' in v else v}"
                                                  for k, v in kv.items()))


def sh(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"{cmd[0]} 실패 ({r.returncode}): {r.stderr.strip()[-400:]}")
    return r


def probe(path):
    out = json.loads(sh(["ffprobe", "-v", "error", "-show_entries", "stream=codec_type,codec_name,width,height,bit_rate,sample_rate,channels",
                         "-show_entries", "format=duration,size", "-of", "json", str(path)]).stdout)
    v = next((s for s in out["streams"] if s["codec_type"] == "video"), {})
    a = next((s for s in out["streams"] if s["codec_type"] == "audio"), {})
    return {"duration": float(out["format"]["duration"]), "mb": int(out["format"]["size"]) / 1e6, "video": v.get("codec_name"),
            "size": f"{v.get('width')}x{v.get('height')}", "audio": a.get("codec_name"), "sr": a.get("sample_rate"), "ch": a.get("channels")}


def loudness(path):
    """→ (I LUFS, TP dBTP) — ffmpeg loudnorm 측정 (tools/loudnorm.py 와 같은 필터)."""
    err = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(path), "-vn", "-af", "loudnorm=I=-14:TP=-1.5:print_format=json",
                          "-f", "null", "-"], capture_output=True, text=True).stderr
    m = re.search(r"\{[^{}]*\"input_i\"[^{}]*\}", err, re.S)
    if not m:
        raise RuntimeError("음량 측정 실패")
    j = json.loads(m.group(0))
    return float(j["input_i"]), float(j["input_tp"])


def ssim(a, b):
    err = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(a), "-i", str(b), "-lavfi", "[0:v][1:v]ssim", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    m = re.search(r"All:([0-9.]+)", err)
    return float(m.group(1)) if m else None


def sha256(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def encode(src, dst, crf, audio_copy):
    cmd = ["ffmpeg", "-y", "-v", "error", "-i", str(src), "-map", "0:v:0", "-map", "0:a:0",
           "-c:v", "libx264", "-preset", PRESET, "-tune", TUNE, "-crf", str(crf), "-pix_fmt", "yuv420p", "-profile:v", "high"]
    cmd += ["-c:a", "copy"] if audio_copy else ["-c:a", "aac", "-b:a", AUDIO_BR, "-ac", "1", "-ar", "48000"]
    sh(cmd + ["-movflags", "+faststart", str(dst)])


def compress(topic, vid, crf=CRF, check_ssim=True):
    src = ROOT / topic / "out" / vid / "final_1080p.mp4"
    dst_dir = ROOT / topic / "source" / vid
    dst, meta_p = dst_dir / "final_1080p.mp4", dst_dir / "final_1080p.json"
    if not src.is_file():
        raise SystemExit(f"[INPUT] ❌ 완성 영상 없음: {src.relative_to(ROOT)} → 먼저 렌더 (node video/render/render.mjs video {topic} {vid})")
    if not dst_dir.is_dir():
        raise SystemExit(f"[INPUT] ❌ 대본 폴더 없음: {dst_dir.relative_to(ROOT)}")
    p0 = probe(src)
    src_sha = sha256(src)
    if meta_p.is_file() and dst.is_file():
        old = json.loads(meta_p.read_text("utf-8"))
        if old.get("source_sha256") == src_sha and old.get("crf") == crf and old.get("tool") == VERSION:
            log("SKIP", video=vid, reason="같은 원본·설정으로 이미 압축함", out=str(dst.relative_to(ROOT)), mb=round(dst.stat().st_size / 1e6, 1))
            return old
    log("INPUT", video=vid, src=str(src.relative_to(ROOT)), mb=round(p0["mb"], 1), seconds=round(p0["duration"], 2), video_codec=p0["video"],
        size=p0["size"], audio=f"{p0['audio']} {p0['sr']}Hz ch={p0['ch']}")
    i0, tp0 = loudness(src)
    t0 = time.time()
    tmp = dst.with_suffix(".tmp.mp4")
    audio_copy = False
    encode(src, tmp, crf, audio_copy)
    i1, tp1 = loudness(tmp)
    if not (I_RANGE[0] <= i1 <= I_RANGE[1]) or tp1 > TP_MAX:
        log("AUDIO", logging.WARNING, video=vid, I=i1, TP=tp1, note=f"AAC {AUDIO_BR} 로 줄였더니 음량 기준 밖 → 소리는 원본 그대로 복사해 다시")
        audio_copy = True
        encode(src, tmp, crf, audio_copy)
        i1, tp1 = loudness(tmp)
    p1 = probe(tmp)
    problems = []
    if abs(p1["duration"] - p0["duration"]) > 0.1:
        problems.append(f"길이가 다름 {p0['duration']:.2f} → {p1['duration']:.2f}초")
    if p1["mb"] > MB_MAX:
        problems.append(f"{p1['mb']:.1f}MB > {MB_MAX}MB (GitHub 한 파일 100MB 한도) → --crf 를 올려 다시")
    if not (I_RANGE[0] <= i1 <= I_RANGE[1]) or tp1 > TP_MAX:
        problems.append(f"음량 기준 밖 I={i1} TP={tp1} → 원본 렌더의 tools/loudnorm.py 결과 확인")
    s = ssim(tmp, src) if check_ssim else None
    if problems:
        tmp.unlink(missing_ok=True)
        for p in problems:
            log("CHECK", logging.ERROR, video=vid, problem=p)
        raise SystemExit(f"[CHECK] ❌ {vid}: 문제 {len(problems)}개 — 압축본을 저장하지 않음")
    if s is not None and s < SSIM_MIN:
        log("CHECK", logging.WARNING, video=vid, ssim=s, note=f"SSIM < {SSIM_MIN} — 화질이 눈에 띄게 떨어질 수 있음, --crf 를 낮춰 다시 고려")
    if p1["mb"] > MB_WARN:
        log("CHECK", logging.WARNING, video=vid, mb=round(p1["mb"], 1), note=f"{MB_WARN}MB 넘음 — GitHub 경고(올라가긴 함)")
    tmp.replace(dst)
    meta = {"tool": VERSION, "created": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"), "video": vid, "topic": topic,
            "source": str(src.relative_to(ROOT)), "source_mb": round(p0["mb"], 2), "source_sha256": src_sha,
            "file": dst.name, "mb": round(p1["mb"], 2), "sha256": sha256(dst), "seconds": round(p1["duration"], 3),
            "crf": crf, "preset": PRESET, "tune": TUNE, "audio": "copy" if audio_copy else f"aac {AUDIO_BR} mono 48kHz",
            "ssim": s, "loudness_before": {"I": i0, "TP": tp0}, "loudness_after": {"I": i1, "TP": tp1},
            "elapsed_s": round(time.time() - t0, 1)}
    meta_p.write_text(json.dumps(meta, ensure_ascii=False, indent=1) + "\n", "utf-8")
    log("DONE", video=vid, out=str(dst.relative_to(ROOT)), mb_before=round(p0["mb"], 1), mb_after=round(p1["mb"], 1),
        saved=f"{(1 - p1['mb'] / p0['mb']):.0%}", ssim=s if s is not None else "-", I=i1, TP=tp1, audio=meta["audio"], elapsed_s=meta["elapsed_s"])
    return meta


def main(argv=None):
    ap = argparse.ArgumentParser(description="완성 영상 → 저장소에 넣을 압축본 (<주제>/source/<영상ID>/final_1080p.mp4)")
    ap.add_argument("topic")
    ap.add_argument("video_id", nargs="?")
    ap.add_argument("--all", action="store_true", help="<주제>/out/*/final_1080p.mp4 가 있는 영상 전부")
    ap.add_argument("--crf", type=int, default=CRF, help=f"영상 화질 (낮을수록 좋고 큼, 기본 {CRF})")
    ap.add_argument("--no-ssim", action="store_true", help="SSIM 비교를 건너뜀 (빠르게)")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args(argv)
    logging.basicConfig(level=getattr(logging, a.log_level), format="%(message)s", stream=sys.stdout)
    log("START", tool=f"compress_video.py {VERSION}", topic=a.topic, crf=a.crf, preset=PRESET, tune=TUNE, audio=AUDIO_BR)
    if a.all:
        ids = sorted(p.parent.name for p in (ROOT / a.topic / "out").glob("*/final_1080p.mp4"))
    elif a.video_id:
        ids = [a.video_id]
    else:
        ap.error("영상 ID 또는 --all")
    failed = []
    for vid in ids:
        try:
            compress(a.topic, vid, a.crf, not a.no_ssim)
        except (SystemExit, RuntimeError) as e:
            failed.append(vid)
            log("FAIL", logging.ERROR, video=vid, error=str(e)[:300], next="위 [CHECK] 로그 확인 뒤 같은 명령")
    log("SUMMARY", videos=len(ids), failed=",".join(failed) or "-")
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
