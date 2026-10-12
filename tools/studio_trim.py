#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-12 — 사용자 지시("패닉셀 영상 오디오 편집은 되는것 같은데 사연 부분을 줄일려고 하는데 자를 부분좀
#          알려줘봐 그리고 대본 파일도 수정해봐"): 이미 올린 영상을 유튜브 스튜디오 편집기(자르기 및 컷 → 새 컷)로 줄일 때
#          자를 시각을 계산(소리가 잘리지 않고, 빼는 문장의 화면 자막이 번쩍이지 않게)하고, 대본·SRT·챕터를 잘라 낸 영상에 맞춘다
"""
이미 올린 영상의 문장 일부를 유튜브 스튜디오에서 잘라 낼 때 쓰는 도구. 연구·교육용 — 투자 권유 아님.

왜 필요한가
  올린 영상은 오디오를 바꿀 수 없지만, 스튜디오 → 편집기 → '자르기 및 컷' → '새 컷'으로 가운데 구간을 빼면
  URL·조회수·댓글이 그대로다. 자막·장면은 영상 화면에 박혀 있으므로 자르는 시각이 중요하다.
    X(컷 시작) = 앞 문장 소리가 끝난 뒤, 빼는 첫 문장의 화면(자막·장면)이 바뀌기 전
    Y(컷 끝)   = 뒤 문장의 화면이 바뀐 뒤, 그 문장 소리가 시작되기 전
  스튜디오 시간 입력 단위(--step, 기본 0.1초)로 이 창 안에 들어가는 값을 고른다. 창 안에 단위 값이 없으면
  소리를 자르지 않는 쪽(빼는 문장 화면이 몇 프레임 보임)을 고르고 그 프레임 수를 보고한다.
  화면이 바뀌는 프레임 = round(SRT 시작 × fps) — 영상 코드(video/src/components/timeline.ts)와 같은 계산.
  소리 시작·끝 = 영상(없으면 narration.mp3) 오디오를 10ms 창으로 읽어 -40 dBFS 를 넘는 첫·마지막 지점.

사용
  python tools/studio_trim.py plan  stock panicsell-2026-10 --drop 2-8,10,12,14,16
  python tools/studio_trim.py plan  stock panicsell-2026-10 --drop 2-8,10,12,14,16 --preview /tmp/p.mp4 --preview-until 110
  python tools/studio_trim.py apply stock panicsell-2026-10 --drop 2-8,10,12,14,16
    apply = 대본(.txt)에서 뺀 문장 삭제, SRT 를 잘라 낸 영상 시간으로, upload.md 챕터 명령(문장 번호)·설명란 챕터,
            youtube.json(chapters·chaptersBeforeTrim·studioTrim), <영상ID>/studio_trim.md(스튜디오 작업 순서) 작성.
    narration.mp3·tts_narration.json·영상 코드(video/src/episodes/<ID>)는 원본 렌더 기록이라 그대로 둔다.
"""
import argparse
import json
import logging
import math
import re
import subprocess
import sys
import tempfile
import wave
from datetime import datetime
from pathlib import Path

import numpy as np

VERSION = "v1.0"
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
import srt_tool  # noqa: E402  — 대본 문장 번호·SRT 묶기 (같은 규칙)

THR_DB = -40.0       # 소리 판정 (10ms 창 최대값)
WIN = 0.010
MIN_TAIL = 0.12      # 앞 문장 소리 끝 뒤 최소 여유 (X)
GUARD = 0.002        # 뒤 문장 소리 시작(1ms 단위로 다시 잰 값) 전 최소 여유 (Y)
GAP_OK = (0.3, 0.8)  # 컷 뒤 남는 문장 사이 쉼 (원래 0.45초)
SR = 48000

logging.basicConfig(level=logging.INFO, format="%(message)s")
LOG = logging.getLogger("studio_trim")


def log(stage, level=logging.INFO, **kv):
    parts = []
    for k, v in kv.items():
        s = v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)
        parts.append(f'{k}="{s}"' if isinstance(v, str) and (" " in s or not s) else f"{k}={s}")
    LOG.log(level, f"[{stage}] [{datetime.now().isoformat(timespec='seconds')}] " + " ".join(parts))


def die(stage, msg, hint=""):
    log(stage, logging.ERROR, error=msg, next=hint or "-")
    raise SystemExit(1)


# ----------------------------------------------------------------------------- 입력
def parse_drop(spec):
    out = set()
    for part in [p.strip() for p in spec.split(",") if p.strip()]:
        a, _, b = part.partition("-")
        lo, hi = int(a), int(b or a)
        if hi < lo:
            die("INPUT", f"범위가 거꾸로: {part}")
        out.update(range(lo, hi + 1))
    return sorted(out)


def runs(nums):
    """[2,3,4,10,12] → [(2,4),(10,10),(12,12)]"""
    out = []
    for n in nums:
        if out and n == out[-1][1] + 1:
            out[-1] = (out[-1][0], n)
        else:
            out.append((n, n))
    return out


def paths(topic, vid):
    src = ROOT / topic / "source" / vid
    return {"src": src, "txt": src / f"{vid}.txt", "srt": src / f"{vid}.srt", "yt": src / "youtube.json",
            "upload": src / "upload.md", "sheet": src / "studio_trim.md", "narr": src / "narration.mp3",
            "video": ROOT / topic / "out" / vid / "final_1080p.mp4"}


def load_sentences(p):
    sents, subs = srt_tool.parse_txt(p["txt"]), srt_tool.parse_srt(p["srt"])
    groups, problems = srt_tool.group(subs, sents)
    if problems:
        die("LOAD", "대본과 SRT가 다름: " + problems[0], "python tools/srt_tool.py check 로 확인")
    return groups, subs


def probe_fps(video):
    try:
        out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=r_frame_rate",
                              "-of", "csv=p=0", str(video)], capture_output=True, text=True, timeout=60).stdout.strip()
        a, b = out.split("/")
        return float(a) / float(b)
    except Exception as e:  # noqa: BLE001 — fps 를 못 읽으면 영상 코드 기본값
        log("LOAD", logging.WARNING, fps_probe=f"실패 {e}", fallback=30)
        return 30.0


def load_audio(path, until):
    """→ (샘플, 10ms 창 최대값 dBFS 배열). ffmpeg 로 앞부분만 읽는다."""
    with tempfile.TemporaryDirectory() as d:
        wav = Path(d) / "a.wav"
        cmd = ["ffmpeg", "-v", "error", "-y", "-i", str(path), "-t", f"{until:.3f}", "-ac", "1", "-ar", str(SR), str(wav)]
        try:
            subprocess.run(cmd, check=True, capture_output=True, text=True, timeout=600)
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
            die("AUDIO", f"오디오를 읽지 못함 {path}: {getattr(e, 'stderr', e)}", "ffmpeg 설치·파일 경로 확인")
        with wave.open(str(wav)) as w:
            x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768
    hop = int(SR * WIN)
    n = len(x) // hop
    pk = np.abs(x[: n * hop]).reshape(n, hop).max(axis=1)
    return x, 20 * np.log10(np.maximum(pk, 1e-6))


def refine(x, t0, t1, first):
    """[t0, t1) 안에서 -40 dBFS 를 넘는 첫(first) 또는 마지막 샘플 시각 — 10ms 창 경계를 1샘플 단위로 다듬는다."""
    a, b = max(0, int(t0 * SR)), min(int(t1 * SR), len(x))
    idx = np.nonzero(np.abs(x[a:b]) > 10 ** (THR_DB / 20))[0]
    if not len(idx):
        return None
    return (a + (idx[0] if first else idx[-1] + 1)) / SR


def gap_at(db, t, span=0.8, min_len=0.15):
    """화면이 바뀌는 시각 t 근처의 문장 사이 무음 → (앞 문장 소리 끝, 뒤 문장 소리 시작). 문장 사이 쉼(0.45초)은
    문장 안 쉼보다 길고 t(= 뒤 문장 시작)에 붙어 있으므로, 끝이 t 에 가장 가까운 0.15초 이상 무음을 고른다."""
    a, b = max(0, int((t - span) / WIN)), min(int((t + span) / WIN), len(db))
    quiet = db[a:b] <= THR_DB
    best, i = None, 0
    while i < len(quiet):
        if quiet[i]:
            j = i
            while j < len(quiet) and quiet[j]:
                j += 1
            s, e = (a + i) * WIN, (a + j) * WIN
            if e - s >= min_len and (best is None or abs(e - t) < abs(best[1] - t)):
                best = (s, e)
            i = j
        else:
            i += 1
    return best


# ----------------------------------------------------------------------------- 계산
def plan_cuts(groups, drop, fps, wav, db, step):
    by_n = {g["n"]: g for g in groups}
    last = groups[-1]["n"]
    sw = lambda n: round(by_n[n]["start"] * fps) / fps          # noqa: E731 — 화면이 바뀌는 시각
    fl = lambda t: math.floor(t / step + 1e-9) * step          # noqa: E731
    ce = lambda t: math.ceil(t / step - 1e-9) * step           # noqa: E731
    cuts = []
    for a, b in runs(drop):
        if a == 1 or b == last:
            die("PLAN", f"문장 {a}–{b}: 처음·마지막 문장을 빼는 컷은 이 도구가 다루지 않음 (스튜디오 '자르기'로 앞뒤를 직접)")
        prev, nxt = a - 1, b + 1
        ga, gn = gap_at(db, sw(a)), gap_at(db, sw(nxt))
        if ga is None or gn is None:
            die("PLAN", f"문장 {prev}–{a} 또는 {b}–{nxt} 사이 무음을 찾지 못함", "영상·오디오 파일이 이 SRT로 만든 것인지 확인")
        end_prev = refine(wav, ga[0] - WIN, ga[0] + WIN, first=False) or ga[0]
        end_drop = refine(wav, gn[0] - WIN, gn[0] + WIN, first=False) or gn[0]
        on_next = refine(wav, gn[1] - WIN, gn[1] + WIN, first=True) or gn[1]
        x_lo, x_hi = end_prev + MIN_TAIL, sw(a)
        y_lo, y_hi = sw(nxt), on_next - GUARD
        x = fl(x_hi)
        if x < x_lo:
            die("PLAN", f"문장 {prev} 뒤에 {step}초 단위로 자를 자리가 없음 (창 {x_lo:.3f}~{x_hi:.3f})", "--step 0.01")
        y, flash = ce(y_lo), 0
        if y > y_hi:                       # 창 안에 단위 값이 없음 → 소리를 자르지 않는 쪽 (빼는 문장 화면이 잠깐)
            y = fl(y_lo)
            flash = round((y_lo - y) * fps)
            if y < end_drop + 0.05:
                die("PLAN", f"문장 {nxt} 앞: 빼는 문장 소리가 남음 (Y {y:.2f} < {end_drop:.3f})", "--step 0.01")
        clip = max(0.0, y - on_next)
        gap = (x - end_prev) + max(0.0, on_next - y)
        cuts.append({"drop": [a, b], "prev": prev, "next": nxt, "x": round(x, 3), "y": round(y, 3),
                     "len": round(y - x, 3), "gap": round(gap, 3), "flash_frames": flash, "clip_ms": round(clip * 1000),
                     "x_window": [round(x_lo, 3), round(x_hi, 3)], "y_window": [round(y_lo, 3), round(y_hi, 3)],
                     "texts": [by_n[n]["text"] for n in range(a, b + 1)]})
        lvl = logging.WARNING if flash or clip or not (GAP_OK[0] <= gap <= GAP_OK[1]) else logging.INFO
        log("CUT", lvl, drop=f"{a}-{b}" if a != b else str(a), start=mmss(x), end=mmss(y), seconds=round(y - x, 2),
            gap_s=round(gap, 2), flash_frames=flash, clip_ms=round(clip * 1000),
            x_window=f"{x_lo:.3f}~{x_hi:.3f}", y_window=f"{y_lo:.3f}~{y_hi:.3f}")
    return cuts


def remap(t, cuts):
    """원본 시각 → 잘라 낸 영상 시각. 컷 안의 시각은 컷 시작으로."""
    shift = 0.0
    for c in cuts:
        if t >= c["y"]:
            shift += c["len"]
        elif t > c["x"]:
            return round(c["x"] - shift, 3)
    return round(t - shift, 3)


def mmss(t):
    t = max(0.0, t)
    m, s = divmod(t, 60)
    return f"{int(m)}:{s:04.1f}"


# ----------------------------------------------------------------------------- 적용
def rewrite_txt(p, drop):
    lines = p["txt"].read_text("utf-8-sig").splitlines()
    out, n, in_card, removed = [], 0, False, []
    for raw in lines:
        line = raw.strip()
        if line and srt_tool.is_label(line):
            in_card = False
        elif line.startswith("[장면]"):
            in_card = True
        elif line and not in_card:
            n += 1
            if n in drop:
                removed.append((n, line))
                continue
        out.append(raw)
    p["txt"].write_text("\n".join(out) + "\n", "utf-8")
    return removed


def rewrite_srt(p, groups, drop, cuts):
    keep = [g for g in groups if g["n"] not in drop]
    cues = []
    for g in keep:
        for part in g["parts"]:
            cues.append([remap(part["start"], cuts), remap(part["end"], cuts), part["text"]])
    for i in range(len(cues) - 1):          # 컷 양쪽 자막은 이어 붙인다 (원래 이어져 있던 것만)
        if 0 < cues[i + 1][0] - cues[i][1] < 0.2:
            cues[i][1] = cues[i + 1][0]
    body = "\n".join(f"{k}\n{srt_tool._ts(a)} --> {srt_tool._ts(b)}\n{t}\n" for k, (a, b, t) in enumerate(cues, 1))
    p["srt"].write_text(body, "utf-8")
    return len(keep), len(cues)


def renumber_spec(spec, drop):
    out = []
    for part in [x for x in spec.split(";") if x.strip()]:
        n, title = part.split("=", 1)
        n = int(n)
        if n in drop:
            die("CHAPTER", f"챕터 문장 {n}을 빼게 됨 ('{title}')", "--drop 을 바꾸거나 upload.md 3번 챕터를 먼저 고치기")
        out.append(f"{n - sum(1 for d in drop if d < n)}={title}")
    return ";".join(out)


def rewrite_upload(p, drop, today):
    md = p["upload"].read_text("utf-8")
    m = re.search(r'--chapters\s+"([^"]+)"', md)
    if not m:
        die("CHAPTER", "upload.md 3번에 --chapters 명령 없음")
    spec_old, spec_new = m.group(1), renumber_spec(m.group(1), drop)
    md = md.replace(spec_old, spec_new)
    out = subprocess.run([sys.executable, str(ROOT / "tools" / "srt_tool.py"), "upload", str(p["txt"]), str(p["srt"]),
                          "--chapters", spec_new], capture_output=True, text=True)
    lines = [x for x in out.stdout.splitlines() if re.match(r"^\d+:\d\d(:\d\d)? ", x)]
    if out.returncode != 0 or "✅" not in out.stdout or not lines:
        die("CHAPTER", "챕터 규칙 실패: " + out.stdout[-400:], "upload.md 3번 챕터 확인")
    md = re.sub(r"(■ 챕터\n)((?:\d+:\d\d(?::\d\d)? [^\n]*\n?)+)", lambda mm: mm.group(1) + "\n".join(lines) + "\n", md, count=1)
    note = (f"- {today} 스튜디오 컷(`tools/studio_trim.py` {VERSION}, 문장 {','.join(map(str, drop))} 뺌) 뒤 다시 계산: "
            f"챕터 {len(lines)}개, \"✅ YouTube 챕터 규칙 통과\". 위 2번 설명란 챕터를 이 값으로 바꿨다 → 스튜디오 설명란에도 붙여 넣기")
    md = re.sub(r"(## 3\. 챕터 다시 계산하기[^\n]*\n\n```\n[^\n]*\n```\n)", lambda mm: mm.group(1) + note + "\n", md, count=1)
    p["upload"].write_text(md, "utf-8")
    log("CHAPTER", status="ok", chapters=len(lines), spec_renumbered=spec_new != spec_old)
    return lines


def write_sheet(p, vid, rec, cuts, removed, keep_story, chapters, total_cut, dur_old, args):
    L = [f"# 스튜디오에서 사연 줄이기 — {vid}", "",
         f"> 자동 생성: `tools/studio_trim.py` {VERSION} · {datetime.now():%Y-%m-%d %H:%M} · 연구·교육용, 투자 권유 아님.",
         f"> 영상: [{rec.get('videoId')}]({rec.get('url')}) · [스튜디오 편집기]({rec.get('studio', '').replace('/edit', '/editor')})",
         "> 올린 영상의 오디오는 바꿀 수 없어서, 이미 있는 문장을 빼는 방식으로 줄인다. URL·조회수·댓글은 그대로.",
         "> ⚠️ 저장한 편집은 '원본으로 되돌리기'가 안 된다(2025년 6월부터). 저장 전에 미리보기로 꼭 들어 본다.", "",
         "## 1. 스튜디오에서 할 일", "",
         "1. 스튜디오 → 콘텐츠 → 이 영상 → **편집기** → **자르기 및 컷**",
         f"2. 아래 컷 {len(cuts)}개를 **뒤에서부터** 하나씩: **새 컷** → 시작·끝 시간 입력 → ✓ (뒤에서부터 하면 앞 컷의 시간이 밀리지 않는다)",
         "3. **미리보기**로 컷마다 앞뒤 2초를 들어 본다 → **저장**",
         "4. 처리가 끝나면(길이가 바뀜) **세부정보 → 설명란**의 '■ 챕터' 줄을 아래 3번으로 바꾼다", "",
         "## 2. 자를 구간 (원본 영상 시간)", "",
         f"스튜디오 입력 단위 {args.step}초 기준. '허용 범위' 안이면 어느 값이어도 된다(소리 안 잘림·빼는 문장 화면 안 보임).", "",
         "| 컷 | 시작 | 끝 | 빼는 길이 | 빼는 문장 | 허용 범위 (시작 / 끝) | 확인할 점 |", "|---|---|---|---|---|---|---|"]
    for k, c in reversed(list(enumerate(cuts, 1))):
        a, b = c["drop"]
        note = []
        if c["flash_frames"]:
            note.append(f"끝 시각이 단위에 안 맞아 빼는 문장 화면이 {c['flash_frames']}프레임 보임 — 0.01초 입력이 되면 "
                        f"{c['y_window'][0] + 0.01:.2f}")
        if c["clip_ms"]:
            note.append(f"다음 문장 첫소리 {c['clip_ms']}ms 잘림")
        note.append(f"남는 쉼 {c['gap']:.2f}초")
        L.append(f"| {k} | **{mmss(c['x'])}** | **{mmss(c['y'])}** | {c['len']:.1f}초 | {a}" + (f"–{b}" if b != a else "")
                 + f" | {c['x_window'][0]:.2f}~{c['x_window'][1]:.2f} / {c['y_window'][0]:.2f}~{c['y_window'][1]:.2f} | "
                 + "; ".join(note) + " |")
    L += ["", f"빼는 길이 합계 **{total_cut:.1f}초** → 영상 {mmss(dur_old)} → 약 {mmss(dur_old - total_cut)}", "",
          "### 남는 사연 (잘라 낸 영상)", ""]
    L += [f"{i}. {t}" for i, t in enumerate(keep_story, 1)]
    L += ["", "### 빼는 문장", ""]
    L += [f"- 문장 {n}: {t}" for n, t in removed]
    L += ["", "## 3. 설명란 챕터 (잘라 낸 뒤 — 이 줄들로 교체)", "", "```"] + chapters + ["```", "",
          "## 4. 저장소에서 바뀐 것", "",
          "- 대본(.txt)·SRT·`upload.md`(설명란 챕터·3번 명령의 문장 번호)·`youtube.json`(chapters, 옛 값은 chaptersBeforeTrim)은 "
          "**잘라 낸 영상 기준**이다.",
          "- `narration.mp3`·`tts_narration.json`·영상 코드(`video/src/episodes/" + vid + "/`)는 원본 렌더 기록이라 그대로 둔다 "
          "(다시 렌더하지 않는다 — 원본 대본은 git 기록).", ""]
    p["sheet"].write_text("\n".join(L), "utf-8")


def preview(video, cuts, until, out):
    keep, t = [], 0.0
    for c in cuts:
        keep.append((t, c["x"]))
        t = c["y"]
    keep.append((t, until))
    keep = [(a, min(b, until)) for a, b in keep if a < until]
    fc, cat = [], ""
    for i, (a, b) in enumerate(keep):
        fc.append(f"[0:v]trim={a:.3f}:{b:.3f},setpts=PTS-STARTPTS,scale=1280:-2[v{i}]")
        fc.append(f"[0:a]atrim={a:.3f}:{b:.3f},asetpts=PTS-STARTPTS[a{i}]")
        cat += f"[v{i}][a{i}]"
    fc.append(f"{cat}concat=n={len(keep)}:v=1:a=1[v][a]")
    cmd = ["ffmpeg", "-v", "error", "-y", "-i", str(video), "-filter_complex", ";".join(fc), "-map", "[v]", "-map", "[a]",
           "-c:v", "libx264", "-preset", "veryfast", "-crf", "26", "-c:a", "aac", "-b:a", "128k", str(out)]
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True, timeout=900)
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        die("PREVIEW", f"미리보기 실패: {getattr(e, 'stderr', e)}", "ffmpeg·영상 경로 확인")
    log("PREVIEW", file=str(out), segments=len(keep), seconds=round(sum(b - a for a, b in keep), 2), source_until=until)


# ----------------------------------------------------------------------------- 명령
def main(argv=None):
    ap = argparse.ArgumentParser(description="올린 영상을 유튜브 스튜디오에서 잘라 낼 시각 계산·대본 맞추기 (연구·교육용)")
    ap.add_argument("cmd", choices=["plan", "apply"])
    ap.add_argument("topic")
    ap.add_argument("vid")
    ap.add_argument("--drop", required=True, help="뺄 문장 번호 (지금 대본 기준) 예: 2-8,10,12")
    ap.add_argument("--step", type=float, default=0.1, help="스튜디오 시간 입력 단위(초)")
    ap.add_argument("--video", help="원본 영상 (기본 <주제>/out/<ID>/final_1080p.mp4, 없으면 narration.mp3 로 소리만)")
    ap.add_argument("--fps", type=float, help="영상이 없을 때 fps (기본 30)")
    ap.add_argument("--preview", help="잘라 낸 모습 미리보기 mp4 경로 (영상 필요)")
    ap.add_argument("--preview-until", type=float, default=120.0, help="미리보기를 원본 몇 초까지")
    ap.add_argument("--force", action="store_true", help="이미 apply 한 영상에 다시")
    args = ap.parse_args(argv)

    p = paths(args.topic, args.vid)
    for k in ("txt", "srt", "yt"):
        if not p[k].is_file():
            die("LOAD", f"{p[k]} 없음", "올린 영상(youtube.json 있음)에만 쓰는 도구")
    rec = json.loads(p["yt"].read_text("utf-8"))
    if args.cmd == "apply" and rec.get("studioTrim") and not args.force:
        die("LOAD", "이미 apply 함 (youtube.json studioTrim) — 지금 대본 번호가 바뀌어 있음", "되돌리려면 git, 그래도 하려면 --force")
    video = Path(args.video) if args.video else p["video"]
    audio = video if video.is_file() else p["narr"]
    if not audio.is_file():
        die("LOAD", f"영상·오디오 없음: {video}, {p['narr']}")
    fps = args.fps or (probe_fps(video) if video.is_file() else 30.0)
    groups, subs = load_sentences(p)
    drop = parse_drop(args.drop)
    bad = [n for n in drop if n < 1 or n > len(groups)]
    if bad:
        die("INPUT", f"없는 문장 번호 {bad} (문장 {len(groups)}개)")
    log("LOAD", tool=f"studio_trim.py {VERSION}", video=args.vid, sentences=len(groups), subs=len(subs), fps=round(fps, 3),
        audio=str(audio.relative_to(ROOT) if audio.is_relative_to(ROOT) else audio), drop=",".join(map(str, drop)),
        step=args.step, note="연구·교육용 — 투자 권유 아님")
    until = max(g["start"] for g in groups if g["n"] <= max(drop) + 1) + 2.0
    wav, db = load_audio(audio, max(until, args.preview_until if args.preview else 0))
    cuts = plan_cuts(groups, drop, fps, wav, db, args.step)
    total_cut = sum(c["len"] for c in cuts)

    story = srt_tool.story_sentences(p["txt"])
    st_n = len(story)
    keep_story = [g["text"] for g in groups if g["n"] <= st_n and g["n"] not in drop]
    host_first = next((g for g in groups if g["n"] > st_n and g["n"] not in drop), None)
    host_at = remap(round(host_first["start"] * fps) / fps, cuts) if host_first else None
    syl = sum(srt_tool.syllables(t) for t in keep_story)
    dur_old = subs[-1]["end"]
    log("STORY", before=f"{st_n}문장 {groups[st_n - 1]['end'] if st_n else 0:.1f}초", after_sentences=len(keep_story),
        after_syllables=syl, host_starts=mmss(host_at) if host_at is not None else "-", removed_s=round(total_cut, 2),
        video_before=mmss(dur_old), video_after=mmss(dur_old - total_cut))
    if host_at is not None and host_at > 30.0:
        log("STORY", logging.WARNING, note=f"진행자 시작 {mmss(host_at)} > 0:30 (script_guide 0-1의 13번)")

    if args.preview:
        if not video.is_file():
            die("PREVIEW", f"영상 없음 {video}", "집 PC 또는 렌더한 환경에서")
        preview(video, cuts, args.preview_until, Path(args.preview))

    if args.cmd == "plan":
        log("NEXT", note="확인 뒤 같은 인수로 apply → 대본·SRT·챕터·youtube.json·studio_trim.md")
        return 0

    today = datetime.now().strftime("%Y-%m-%d")
    removed = rewrite_txt(p, set(drop))
    n_sent, n_cue = rewrite_srt(p, groups, set(drop), cuts)
    log("APPLY", txt=str(p["txt"].relative_to(ROOT)), removed=len(removed), srt=str(p["srt"].relative_to(ROOT)),
        sentences=n_sent, subs=n_cue)
    chapters = rewrite_upload(p, drop, today)
    rec["chaptersBeforeTrim"] = rec.get("chaptersBeforeTrim") or rec.get("chapters")
    rec["chapters"] = chapters
    rec["studioTrim"] = {"date": today, "tool": f"studio_trim.py {VERSION}", "dropSentences": drop, "step": args.step,
                         "cuts": [{"start": mmss(c["x"]), "end": mmss(c["y"]), "startSec": c["x"], "endSec": c["y"],
                                   "drop": c["drop"], "flashFrames": c["flash_frames"], "clipMs": c["clip_ms"]} for c in cuts],
                         "removedSeconds": round(total_cut, 2), "hostStartsAt": mmss(host_at) if host_at else None,
                         "status": "스튜디오에서 적용할 것 (studio_trim.md) — 적용 뒤 설명란 챕터 교체"}
    p["yt"].write_text(json.dumps(rec, ensure_ascii=False, indent=2) + "\n", "utf-8")
    write_sheet(p, args.vid, rec, cuts, removed, keep_story, chapters, total_cut, dur_old, args)
    log("APPLY", youtube_json="chapters·chaptersBeforeTrim·studioTrim", sheet=str(p["sheet"].relative_to(ROOT)))
    rc = srt_tool.check(p["txt"], p["srt"], (n_sent, n_cue))
    log("NEXT", note=f"{p['sheet'].relative_to(ROOT)} 순서대로 스튜디오에서 컷 {len(cuts)}개 → 설명란 챕터 교체", check_rc=rc)
    return rc


if __name__ == "__main__":
    sys.exit(main())
