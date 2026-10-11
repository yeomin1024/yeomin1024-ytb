#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-11 — 신규: 완성 영상 음량을 유튜브 기준(-14 LUFS, 트루 피크 -1.5 dBTP 이하)으로 맞춤 (사용자 지시 "음량 맞춰")
r"""
렌더한 완성 영상(final_1080p.mp4)의 소리 크기를 유튜브 기준에 맞춥니다. 영상 스트림은 그대로 복사하고 오디오만 다시 만듭니다.

  python3 tools/loudnorm.py stock/out/molppang-2026-10/final_1080p.mp4   # 파일 하나
  python3 tools/loudnorm.py --all                                         # 모든 <주제>/out/<영상ID>/final_1080p.mp4
  옵션: --target -14 (LUFS) · --tp -1.5 (dBTP) · --dry-run (재기만) · --force (이미 맞아도 다시)

왜: 유튜브는 큰 소리만 -14 LUFS 근처로 줄이고 작은 소리는 키워 주지 않는다. 내레이션 렌더 결과가 약 -20 LUFS라
    다른 영상보다 작게 들렸다 (2026-10-11 측정: bittu -19.7, multagi -20.5, panicsell -19.7, molppang -20.4).

방법 (결정적, 같은 입력이면 같은 결과):
  1. 측정: ffmpeg loudnorm 측정 모드 → 통합 음량 I(LUFS), 트루 피크 TP(dBTP), 음량 범위 LRA
  2. 이미 |I - 목표| ≤ 0.5 이고 TP ≤ 한도면 건너뜀 (--force 아니면). 같은 영상에 두 번 돌려도 안전
  3. 이득 = 목표 - I. 이득을 더한 피크가 한도 안이면 단순 증폭만 (음색·다이내믹 그대로)
     넘으면 증폭 + 피크 리미터(alimiter, 미리 보기 5ms, 지연 보정 → 자막·화면 싱크 그대로). 말소리의 짧은 피크만 누름
  4. 결과 파일을 다시 측정 → 목표에서 0.3 LU 넘게 벗어나거나 TP가 한도를 넘으면 이득·리미터를 고쳐 한 번 더 (최대 3번)
  5. 통과한 파일로 원본을 바꿈 (임시 파일 → 이름 바꾸기). 실패하면 원본은 그대로 두고 종료 코드 1
로그: [LOUDNESS] [시각] key=value ... (측정 전·후 값, 쓴 이득, 리미터 사용 여부, 걸린 시간)
"""
import argparse
import json
import logging
import math
import os
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOL_SKIP = 0.5      # 이미 맞은 것으로 보는 범위 (LU)
TOL_DONE = 0.3      # 처리 뒤 목표와의 허용 차이 (LU)
TP_MARGIN = 0.5     # 리미터는 표본 피크 기준이라 트루 피크(표본 사이 피크)를 위해 한도보다 이만큼 낮게 (dB)
MAX_TRIES = 3

log = logging.getLogger("loudnorm")


def setup_logging(level):
    h = logging.StreamHandler(sys.stdout)
    h.setFormatter(logging.Formatter("[LOUDNESS] [%(asctime)s] %(message)s", "%Y-%m-%dT%H:%M:%SZ"))
    logging.Formatter.converter = time.gmtime
    log.addHandler(h)
    log.setLevel(level)


def kv(**items):
    return " ".join(f"{k}={v}" for k, v in items.items())


def run(cmd):
    p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return p.returncode, p.stdout, p.stderr


def measure(path, target, tp):
    """ffmpeg loudnorm 측정 모드 → {'I','TP','LRA'} (오디오만 읽음)."""
    rc, _, err = run(["ffmpeg", "-hide_banner", "-nostats", "-nostdin", "-i", str(path), "-vn", "-map", "0:a:0",
                      "-af", f"loudnorm=I={target}:TP={tp}:LRA=11:print_format=json", "-f", "null", "-"])
    m = re.search(r"\{[^{}]*\"input_i\"[^{}]*\}", err, re.S)
    if rc != 0 or not m:
        raise RuntimeError(f"측정 실패 rc={rc} file={path} stderr_tail={err.strip()[-300:]!r}")
    d = json.loads(m.group(0))
    return {"I": float(d["input_i"]), "TP": float(d["input_tp"]), "LRA": float(d["input_lra"])}


def audio_info(path):
    rc, out, err = run(["ffprobe", "-v", "error", "-select_streams", "a:0", "-show_entries",
                        "stream=codec_name,sample_rate,channels,bit_rate", "-of", "json", str(path)])
    if rc != 0:
        raise RuntimeError(f"ffprobe 실패 file={path} err={err.strip()[-200:]!r}")
    s = (json.loads(out).get("streams") or [None])[0]
    if not s:
        raise RuntimeError(f"오디오 스트림 없음 file={path}")
    return s


def build_filter(gain_db, limit_dbfs):
    f = [f"volume={gain_db:.2f}dB"]
    if limit_dbfs is not None:
        lim = 10 ** (limit_dbfs / 20)
        # level=false: 자동 보정 끔(이득은 위에서 정함) · latency=true: 미리 보기 지연 보정(A/V 싱크 유지)
        f.append(f"alimiter=limit={lim:.4f}:attack=5:release=50:level=false:latency=true")
    return ",".join(f)


def encode(src, dst, afilter, info):
    br = int(info.get("bit_rate") or 320000)
    br_k = max(192, min(320, round(br / 1000)))
    sr = info.get("sample_rate") or "48000"
    rc, _, err = run(["ffmpeg", "-hide_banner", "-nostats", "-nostdin", "-y", "-i", str(src),
                      "-map", "0:v:0", "-map", "0:a:0", "-c:v", "copy",
                      "-af", afilter, "-c:a", "aac", "-b:a", f"{br_k}k", "-ar", str(sr),
                      "-movflags", "+faststart", str(dst)])
    if rc != 0:
        raise RuntimeError(f"인코딩 실패 file={src} filter={afilter} stderr_tail={err.strip()[-300:]!r}")


def duration(path):
    rc, out, _ = run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)])
    return float(out.strip()) if rc == 0 and out.strip() else float("nan")


def normalize(path, target, tp, dry_run=False, force=False):
    t0 = time.time()
    path = Path(path)
    if not path.is_file():
        raise RuntimeError(f"파일 없음 file={path}")
    info = audio_info(path)
    before = measure(path, target, tp)
    log.info(kv(stage="measure", file=path.relative_to(ROOT) if path.is_relative_to(ROOT) else path,
                I=before["I"], TP=before["TP"], LRA=before["LRA"], target_I=target, target_TP=tp,
                codec=info.get("codec_name"), sr=info.get("sample_rate"), ch=info.get("channels")))
    if not force and abs(before["I"] - target) <= TOL_SKIP and before["TP"] <= tp:
        log.info(kv(stage="skip", reason="이미_기준_안", I=before["I"], TP=before["TP"]))
        return {"file": str(path), "status": "skip", "before": before, "after": before}
    gain = target - before["I"]
    need_limit = before["TP"] + gain > tp
    limit = (tp - TP_MARGIN) if need_limit else None
    log.info(kv(stage="plan", gain_db=f"{gain:+.2f}", peak_after_gain=f"{before['TP'] + gain:+.2f}",
                limiter=("on limit_dbfs=%.2f" % limit) if need_limit else "off"))
    if dry_run:
        return {"file": str(path), "status": "dry-run", "before": before, "gain": gain, "limiter": need_limit}
    tmp = path.with_name(path.stem + ".loudnorm.tmp.mp4")
    after = None
    try:
        for attempt in range(1, MAX_TRIES + 1):
            afilter = build_filter(gain, limit)
            encode(path, tmp, afilter, info)
            after = measure(tmp, target, tp)
            ok_i = abs(after["I"] - target) <= TOL_DONE
            ok_tp = after["TP"] <= tp
            log.info(kv(stage="pass", attempt=attempt, filter=afilter, I=after["I"], TP=after["TP"],
                        LRA=after["LRA"], ok_I=ok_i, ok_TP=ok_tp))
            if ok_i and ok_tp:
                break
            if not ok_tp:   # 트루 피크가 넘으면 리미터를 넘은 만큼 더 낮춤
                limit = (limit if limit is not None else tp - TP_MARGIN) - (after["TP"] - tp) - 0.2
            if not ok_i:    # 리미터가 피크를 누른 만큼 음량이 덜 오름 → 차이만큼 이득 보정
                gain += target - after["I"]
        else:
            raise RuntimeError(f"{MAX_TRIES}번 해도 기준 밖 I={after['I']} TP={after['TP']} → 원본 그대로 둠")
        d0, d1 = duration(path), duration(tmp)
        if not (abs(d0 - d1) < 0.1):
            raise RuntimeError(f"길이가 달라짐 before={d0} after={d1} → 원본 그대로 둠")
        os.replace(tmp, path)
    finally:
        if tmp.exists():
            tmp.unlink()
    log.info(kv(stage="done", I_before=before["I"], I_after=after["I"], TP_before=before["TP"], TP_after=after["TP"],
                LRA_before=before["LRA"], LRA_after=after["LRA"], gain_db=f"{gain:+.2f}",
                limiter="on" if limit is not None else "off", duration_s=f"{d1:.3f}", elapsed_s=f"{time.time() - t0:.1f}"))
    return {"file": str(path), "status": "done", "before": before, "after": after, "gain": gain,
            "limiter": limit is not None}


def main():
    ap = argparse.ArgumentParser(description="완성 영상 음량을 유튜브 기준(-14 LUFS)에 맞춤 (영상 스트림은 그대로)")
    ap.add_argument("files", nargs="*", help="mp4 파일")
    ap.add_argument("--all", action="store_true", help="모든 <주제>/out/<영상ID>/final_1080p.mp4")
    ap.add_argument("--target", type=float, default=-14.0, help="통합 음량 목표 LUFS (기본 -14)")
    ap.add_argument("--tp", type=float, default=-1.5, help="트루 피크 한도 dBTP (기본 -1.5)")
    ap.add_argument("--dry-run", action="store_true", help="재기만 하고 파일은 안 바꿈")
    ap.add_argument("--force", action="store_true", help="이미 기준 안이어도 다시")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args()
    setup_logging(a.log_level)
    files = [Path(f).resolve() for f in a.files]
    if a.all:
        files += sorted(ROOT.glob("*/out/*/final_1080p.mp4"))
    if not files:
        ap.error("파일을 주거나 --all")
    t0, failed = time.time(), []
    for f in files:
        try:
            normalize(f, a.target, a.tp, dry_run=a.dry_run, force=a.force)
        except Exception as e:  # 파일마다 따로: 하나가 실패해도 나머지는 진행
            failed.append(str(f))
            log.error(kv(stage="fail", file=f, error=repr(str(e)),
                         next="ffmpeg 설치·파일 손상 확인 후 다시 실행 (원본은 바뀌지 않음)"))
    log.info(kv(stage="end", files=len(files), failed=len(failed), elapsed_s=f"{time.time() - t0:.1f}"))
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
