#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-10-21 — 사용자 지시 "클립 돌렸으니 확인해서 영상 만들어봐": 클립을 직접 보니 L05 가 1.45초부터 사람이 겹쳐
#          보이며 녹아내림(그 밖에 8개도 중간·끝에 겹침) → 장면 계획(plan.json) 클립 옵션 `use_from`·`use_to`(클립 안 깨끗한 구간만,
#          초) · `loop: "pingpong"`(그 구간을 앞으로 갔다 되돌아오게 — 작게 움직이는 장면에서 멈춤 대신) · [FIT] 로그에 쓴 구간·pingpong ·
#          클립 뒤가 코드 화면이면 클립을 TAIL(0.15초) 더 보여 줌 — 바탕은 다음 문장 0.15초 전에 장면을 바꾸기 시작해, 클립에 가려 한 번도
#          안 보인 카드가 사라지는 4프레임이 번쩍였음 (쇼츠 S10 → 11번 문장).
# 이전 v1.0 — 2026-10-19 — 사용자 지시 "영상은 설명이 복잡하고 어려울 때는 클로드 코드로 렌더링 하고 그렇지 않은 부분은 친숙한
#          애니메이션 이미지 … 짧은 영상 만들어주는 프롬프트 … 영상을 이어 붙이는건 그 코드에서 하는게 아니라 너가 하는거야 최종으로
#          영상에 합치는거니까": 코드 화면 바탕 영상 + AI 장면 클립(videogen v1.4.0) + 구운 자막·장 이름표(코드 화면과 같은 모양) +
#          각색 안내 + 내레이션 → final_1080p.mp4 → 음량 맞춤(tools/loudnorm.py) → 점검용 장면 모음.
r"""
순서 (저장소 최상위에서):
  node video/render/render.mjs video   economic gungmin-sigi-2026-10 --base     # 코드 화면 바탕 → out/<영상ID>/base_1080p.mp4
  node video/render/render.mjs overlay economic gungmin-sigi-2026-10            # 자막·장 이름표 투명 PNG → out/<영상ID>/overlay/
  python3 tools/scene_clips.py fetch   economic gungmin-sigi-2026-10            # Release 의 AI 클립 → out/<영상ID>/clips/
  python3 tools/assemble_video.py      economic gungmin-sigi-2026-10 [--shorts] # → out/<영상ID>/final_1080p.mp4 + qa/

옵션: --placeholders (AI 클립 대신 이름이 적힌 시험 클립 — 오디오·클립 전 흐름 시험) · --preview 60,90 (그 구간만, 음량 맞춤 없음)
      --crf 18 · --dry-run (계획·ffmpeg 그래프만) · --allow-stale (바탕·자막 PNG 가 장면 파일보다 오래돼도)

클립 맞추기 (scene_clips.windows 구간 [t0, t1] — 첫 문장 시작 - 0.15초 ~ 다음 문장 시작 - 0.15초, 다음이 장 시작이면 장 카드 1초 전):
  클립이 길면 앞에서부터 자름 · 짧으면 1.35배까지 늦춤 · 그래도 짧으면 마지막 장면을 멈춤 · 생성 크기(1280x704) → 1920x1080 은
  (v1.1) plan.json 클립에 "use_from": 2.3·"use_to": 1.3 = 클립 안 그 구간만 (겹침·녹아내림을 뺌) · "loop": "pingpong" = 그 구간을 앞으로 →
  거꾸로 이어서 씀 ·
  키운 뒤 가운데 자르기(Lanczos) · 24fps → 30fps.
로그: [STAGE] [시각] key=value …   ※ 연구·교육용 영상 제작 도구 (연금 상담·투자 권유 아님)
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import scene_clips as sc  # noqa: E402

ROOT = sc.ROOT
VERSION = "v1.1"
FPS = 30
TAIL = 0.15   # 클립 뒤가 코드 화면일 때 더 보여 줄 시간 (바탕의 장면 바꿈이 끝날 때까지)
FONT = ROOT / "video" / "public" / "fonts" / "NotoSansKR-700.ttf"


def log(stage: str, msg: str = "", **kv):
    sc.log(stage, msg, **kv)


def probe(path: Path) -> dict:
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration:stream=codec_type,width,height,r_frame_rate",
                        "-of", "json", str(path)], capture_output=True, encoding="utf-8", errors="replace")
    if r.returncode:
        raise SystemExit(f"[PROBE] 읽기 실패 {path}: {r.stderr[-300:]}")
    d = json.loads(r.stdout)
    v = next((s for s in d.get("streams", []) if s.get("codec_type") == "video"), {})
    num, den = (v.get("r_frame_rate") or "0/1").split("/")
    return dict(duration=float(d.get("format", {}).get("duration") or 0), width=v.get("width"), height=v.get("height"),
                fps=round(float(num) / float(den or 1), 3) if float(den or 1) else None,
                audio=any(s.get("codec_type") == "audio" for s in d.get("streams", [])))


def run(cmd: list, stage: str, hint: str) -> None:
    t0 = time.perf_counter()
    r = subprocess.run(cmd, capture_output=True, encoding="utf-8", errors="replace")
    if r.returncode:
        for line in r.stderr.strip().splitlines()[-12:]:
            log(stage, "  | " + line[:300])
        raise SystemExit(f"[{stage}] 실패 (rc={r.returncode}) — {hint}")
    log(stage, "ok", sec=round(time.perf_counter() - t0, 1))


# --------------------------------------------------------------------------------------------------
def fit_plan(wins: list[dict], clips: dict[str, Path], opts: dict[str, dict] | None = None, tail: float = TAIL) -> list[dict]:
    """클립마다 늦춤 배수·멈춤 길이. 늦춤은 sc.MAX_SLOW 까지. opts = plan 클립(이름별) — use_from·use_to·loop.
    바로 뒤에 다른 클립이 없으면 보이는 끝 t1 을 tail 만큼 늘림 (t1_plan = 원래 끝)."""
    out = []
    t0s = [w["t0"] for w in wins]
    for w in wins:
        ext = 0.0 if any(abs(x - w["t1"]) < 0.02 for x in t0s) else tail
        w = dict(w, t1=round(w["t1"] + ext, 3), t1_plan=w["t1"], tail=ext)
        o = (opts or {}).get(w["name"], {})
        raw = probe(clips[w["name"]])["duration"]
        a = float(o.get("use_from", 0.0))
        b = min(raw, float(o.get("use_to", raw)))
        if not 0 <= a < b:
            raise SystemExit(f"[FIT] {w['name']}: 쓸 구간이 없음 use_from={a} use_to={b} (클립 {raw:.2f}초)")
        pingpong = o.get("loop") == "pingpong"
        if o.get("loop") not in (None, "pingpong"):
            raise SystemExit(f"[FIT] {w['name']}: loop 는 \"pingpong\" 만 ({o['loop']})")
        span = (round(a, 3), round(b, 3)) if ("use_from" in o or "use_to" in o) else None
        d = b - a
        if pingpong:
            d = 2 * d - 1 / sc.MODEL_FPS          # 되돌아올 때 맨 끝 장면은 한 번만
        need = w["t1"] - w["t0"]
        slow = 1.0 if d >= need else min(sc.MAX_SLOW, need / d)
        hold = max(0.0, need - d * slow)
        out.append(dict(w, file=clips[w["name"]], clip_dur=round(raw, 3), span=span, pingpong=pingpong, slow=round(slow, 4),
                        hold=round(hold, 3), cut=round(max(0.0, d - need), 3)))
    return out


def notice_png(text: str, size: tuple[int, int], dst: Path, portrait: bool) -> None:
    """각색 안내 한 줄 (오른쪽 위 — 장 이름표와 같은 높이·모양, 36px)."""
    from PIL import Image, ImageDraw, ImageFont
    W, H = size
    img = Image.new("RGBA", size, (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype(str(FONT), 36)
    l, t, r, b = d.textbbox((0, 0), text, font=font)
    pw, ph = r - l + 56, 36 + 32
    x1, y0 = (W - 96, 60) if not portrait else (W // 2 + pw // 2, 160)
    x0, y1 = x1 - pw, y0 + ph
    d.rounded_rectangle((x0, y0, x1, y1), radius=ph // 2, fill=(5, 9, 18, 158), outline=(255, 255, 255, 46), width=2)
    d.text((x0 + 28 - l, y0 + (ph - (b - t)) / 2 - t), text, font=font, fill=(244, 246, 250, 255))
    img.save(dst)


def make_placeholders(wins: list[dict], gen: tuple[int, int], dst: Path) -> dict[str, Path]:
    """AI 클립 대신 움직이는 시험 무늬 + 이름 (생성 크기·24fps·계획한 길이) — 흐름 시험용."""
    dst.mkdir(parents=True, exist_ok=True)
    out = {}
    for w in wins:
        f = dst / f"{w['name']}.mp4"
        dur = w["frames"] / sc.MODEL_FPS
        txt = f"{w['name']}  s{w['a']}" + ("" if w["a"] == w["b"] else f"-{w['b']}")
        vf = (f"drawtext=fontfile={FONT}:text='{txt}':fontsize=110:fontcolor=white:borderw=6:bordercolor=black:"
              f"x=(w-tw)/2:y=(h-th)/2-40,drawtext=fontfile={FONT}:text='%{{pts\\:hms}}':fontsize=48:fontcolor=yellow:"
              f"x=(w-tw)/2:y=(h/2)+80")
        run(["ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", f"testsrc2=s={gen[0]}x{gen[1]}:r={sc.MODEL_FPS}:d={dur:.4f}",
             "-vf", vf, "-c:v", "libx264", "-preset", "veryfast", "-crf", "23", "-pix_fmt", "yuv420p", str(f)],
            "PLACEHOLDER", "ffmpeg drawtext·글꼴 확인")
        out[w["name"]] = f
    log("PLACEHOLDER", "made", clips=len(out), dir=str(dst.relative_to(ROOT)))
    return out


def build_graph(fits: list[dict], size: tuple[int, int], notice: dict | None, preview: tuple[float, float] | None) -> str:
    W, H = size
    lines = [f"[0:v]setpts=PTS-STARTPTS,fps={FPS},format=yuv420p[v0]"]
    for i, f in enumerate(fits, 1):
        need = f["t1"] - f["t0"]
        src = f"[{i}:v]"
        if f.get("span") or f.get("pingpong"):
            cut = f"trim=start={f['span'][0]:.3f}:end={f['span'][1]:.3f}," if f.get("span") else ""
            if f.get("pingpong"):
                lines.append(f"[{i}:v]{cut}setpts=PTS-STARTPTS,split[pa{i}][pb{i}]")
                lines.append(f"[pb{i}]reverse,trim=start_frame=1,setpts=PTS-STARTPTS[pr{i}]")
                lines.append(f"[pa{i}][pr{i}]concat=n=2:v=1:a=0[pp{i}]")
            else:
                lines.append(f"[{i}:v]{cut}setpts=PTS-STARTPTS[pp{i}]")
            src = f"[pp{i}]"
        chain = (f"{src}scale={W}:{H}:force_original_aspect_ratio=increase:flags=lanczos,crop={W}:{H},setsar=1,"
                 f"setpts=(PTS-STARTPTS)*{f['slow']:.4f},fps={FPS}")
        if f["hold"] > 0:
            chain += f",tpad=stop_mode=clone:stop_duration={f['hold'] + 0.1:.3f}"
        chain += f",trim=duration={need:.3f},setpts=PTS-STARTPTS+{f['t0']:.3f}/TB,format=yuv420p[c{i}]"
        lines.append(chain)
        lines.append(f"[v{i - 1}][c{i}]overlay=0:0:eof_action=pass:repeatlast=0:"
                     f"enable='between(t,{f['t0'] - 0.001:.3f},{f['t1'] + 0.001:.3f})'[v{i}]")
    n = len(fits)
    k = n + 1
    lines.append(f"[{k}:v]setpts=PTS-STARTPTS,format=rgba[ov]")
    lines.append(f"[v{n}][ov]overlay=0:0:eof_action=repeat:format=auto[vs]")
    last = "vs"
    if notice:
        lines.append(f"[{k + 1}:v]format=rgba,setpts=PTS-STARTPTS[nt]")
        lines.append(f"[vs][nt]overlay=0:0:eof_action=pass:enable='between(t,{notice['a']:.3f},{notice['b']:.3f})'[vn]")
        last = "vn"
    tail = f"[{last}]format=yuv420p"
    if preview:
        tail += f",trim=start={preview[0]:.3f}:end={preview[1]:.3f},setpts=PTS-STARTPTS"
    lines.append(tail + "[vout]")
    return ";\n".join(lines)


def qa_sheet(final: Path, fits: list[dict], qa_dir: Path, size: tuple[int, int], offset: float = 0.0) -> Path:
    """클립마다 들어가기 직전·가운데·끝난 직후 장면 → 모음 그림 (Claude 가 직접 봄)."""
    from PIL import Image, ImageDraw, ImageFont
    qa_dir.mkdir(parents=True, exist_ok=True)
    for old in qa_dir.glob("*.jpg"):
        old.unlink()
    W, H = size
    tw = 384 if W > H else 216
    th = round(tw * H / W)
    font = ImageFont.truetype(str(FONT), 22)
    rows = []
    for f in fits:
        ts = [f["t0"] - 0.2, (f["t0"] + f["t1"]) / 2, f["t1"] + 0.2]
        frames = []
        for j, t in enumerate(ts):
            t -= offset
            if t < 0:
                t = 0.0
            p = qa_dir / f"{f['name']}_{j}.jpg"
            subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", f"{t:.3f}", "-i", str(final), "-frames:v", "1",
                            "-vf", f"scale={tw}:{th}", "-q:v", "4", str(p)], check=False)
            frames.append(p if p.exists() else None)
        rows.append((f, frames))
    cols = 3
    sheet = Image.new("RGB", (cols * tw + 260, max(1, len(rows)) * (th + 8)), (20, 20, 24))
    d = ImageDraw.Draw(sheet)
    for r, (f, frames) in enumerate(rows):
        y = r * (th + 8)
        d.text((8, y + 8), f"{f['name']} s{f['a']}", font=font, fill=(255, 214, 0))
        d.text((8, y + 40), f"{f['t0']:.1f}–{f['t1']:.1f}s", font=font, fill=(230, 230, 230))
        d.text((8, y + 72), f"x{f['slow']:.2f} hold {f['hold']:.2f}", font=font, fill=(180, 180, 180))
        for c, p in enumerate(frames):
            if p:
                with Image.open(p) as im:
                    sheet.paste(im, (260 + c * tw, y))
    out = qa_dir / "contact_sheet.jpg"
    sheet.save(out, quality=85)
    return out


# --------------------------------------------------------------------------------------------------
def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="코드 화면 + AI 장면 클립 합치기 " + VERSION)
    ap.add_argument("topic")
    ap.add_argument("vid")
    ap.add_argument("--shorts", action="store_true")
    ap.add_argument("--placeholders", action="store_true")
    ap.add_argument("--preview")
    ap.add_argument("--crf", type=int, default=18)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--allow-stale", action="store_true")
    ap.add_argument("--estimated-preview", action="store_true", help="오디오 전 추정 시각으로 (소리 없음, 최종본 아님)")
    a = ap.parse_args(argv)
    t_start = time.perf_counter()

    p = sc.paths(a.topic, a.vid, a.shorts)
    plan = sc.load_plan(p["plan"])
    ep = sc.read_ep(p["episode"])
    if not ep:
        raise SystemExit(f"[INPUT] 장면 파일이 없음: {p['episode']}")
    if ep.get("estimated") and not a.estimated_preview:
        raise SystemExit(f"[INPUT] 장면 파일이 추정 시각 — 오디오가 오면 node video/render/render.mjs sync {a.topic} {p['ep_id']}")
    sents = ep["sent"]
    wins = sc.windows(plan, sents)
    problems = sc.check_plan(plan, sents, wins)
    if problems:
        for pr in problems:
            log("PLAN", "PROBLEM " + pr)
        return 1
    size = sc.SIZES[plan["orientation"]]["final"]
    out_dir = p["out"]
    base = out_dir / "base_1080p.mp4"
    ov_dir = out_dir / "overlay"
    narration = p["timing"].parent / "narration.mp3"
    log("INPUT", "episode", video=p["ep_id"], sentences=len(sents), duration=ep["duration"], synced=ep.get("synced", ""),
        clips_planned=len(wins), size=f"{size[0]}x{size[1]}", tool=f"assemble_video.py {VERSION}")

    missing = [str(x.relative_to(ROOT)) for x in (base, ov_dir / "list.ffconcat") if not x.exists()]
    if not a.estimated_preview and not narration.exists():
        missing.append(str(narration.relative_to(ROOT)))
    if missing:
        log("INPUT", "missing", files=",".join(missing),
            next_step=f"node video/render/render.mjs video {a.topic} {p['ep_id']} --base · overlay {a.topic} {p['ep_id']}")
        return 1
    page_mtime = p["episode"].stat().st_mtime
    stale = [x.name for x in (base, ov_dir / "overlay.json") if x.stat().st_mtime < page_mtime]
    if stale:
        log("INPUT", "older than the scene file (re-render?)", files=",".join(stale))
        if not a.allow_stale:
            return 1
    bi = probe(base)
    if abs(bi["duration"] - ep["duration"]) > 0.2 or (bi["width"], bi["height"]) != size:
        log("INPUT", "base video does not match the episode", base_sec=bi["duration"], ep_sec=ep["duration"],
            base_size=f"{bi['width']}x{bi['height']}")
        if not a.allow_stale:
            return 1
    ovj = json.loads((ov_dir / "overlay.json").read_text(encoding="utf-8"))
    log("INPUT", "base", sec=round(bi["duration"], 2), fps=bi["fps"], audio=bi["audio"])
    log("INPUT", "overlay", states=len(ovj["states"]), subs=ovj["subs"], chip=ovj["chip"], subtitles=ovj["subtitles"])

    if a.placeholders:
        clips = make_placeholders(wins, sc.SIZES[plan["orientation"]]["gen"], out_dir / "clips_placeholder")
    else:
        cdir = out_dir / "clips"
        clips = {w["name"]: cdir / f"{w['name']}.mp4" for w in wins}
        absent = [n for n, f in clips.items() if not f.exists()]
        if absent:
            log("INPUT", "AI clips missing", names=",".join(absent),
                next_step=f"python3 tools/scene_clips.py fetch {a.topic} {a.vid}{' --shorts' if a.shorts else ''} (or --placeholders)")
            return 1
    fits = fit_plan(wins, clips, {c["name"]: c for c in plan["clips"]})
    for f in fits:
        log("FIT", f["name"], sentences=f"{f['a']}-{f['b']}", t0=f["t0"], t1=f["t1"], tail=f["tail"], need=round(f["t1"] - f["t0"], 3),
            clip=f["clip_dur"], used=f"{f['span'][0]}-{f['span'][1]}" if f["span"] else "all", pingpong=f["pingpong"], slow=f["slow"], hold=f["hold"], cut=f["cut"])
    held = [f["name"] for f in fits if f["hold"] > 0.05]
    if held:
        log("FIT", "last frame held (clip too short even at max slow-down)", names=",".join(held))

    notice = None
    if plan.get("notice"):
        nt = plan["notice"]
        by = {s["n"]: s for s in sents}
        notice = dict(text=nt["text"], a=by[nt.get("from_sentence", 1)]["start"], b=by[nt["until_sentence"]]["end"])
        notice_png(notice["text"], size, out_dir / "notice.png", plan["orientation"] == "portrait")
        log("NOTICE", "caption", text=notice["text"], a=notice["a"], b=notice["b"])

    preview = tuple(map(float, a.preview.split(","))) if a.preview else None
    graph = build_graph(fits, size, notice, preview)
    gfile = out_dir / "assemble_graph.txt"
    gfile.write_text(graph, encoding="utf-8")
    final = out_dir / ("final_1080p.mp4" if not preview else f"preview_assembled_{preview[0]:g}-{preview[1]:g}.mp4")
    if a.placeholders and not preview:
        final = out_dir / "placeholder_assembled.mp4"
    cmd = ["ffmpeg", "-y", "-v", "error", "-i", str(base)]
    for f in fits:
        cmd += ["-i", str(f["file"])]
    cmd += ["-f", "concat", "-safe", "0", "-i", str(ov_dir / "list.ffconcat")]
    if notice:
        cmd += ["-loop", "1", "-framerate", str(FPS), "-t", f"{notice['b'] + 0.5:.3f}", "-i", str(out_dir / "notice.png")]
    audio_idx = None
    if narration.exists() and not a.estimated_preview:
        audio_idx = len(fits) + 2 + (1 if notice else 0)
        cmd += (["-ss", f"{preview[0]:.3f}"] if preview else []) + ["-i", str(narration)]   # 미리보기면 소리도 그 구간부터
    cmd += ["-filter_complex_script", str(gfile), "-map", "[vout]"]
    if audio_idx is not None:
        cmd += ["-map", f"{audio_idx}:a", "-c:a", "aac", "-b:a", "192k"]
    dur = (preview[1] - preview[0]) if preview else ep["duration"]
    cmd += ["-c:v", "libx264", "-preset", "medium", "-crf", str(a.crf), "-pix_fmt", "yuv420p", "-r", str(FPS),
            "-t", f"{dur:.3f}", "-movflags", "+faststart", str(final)]
    log("ASSEMBLE", "plan", inputs=len(fits) + 2 + (1 if notice else 0) + (1 if audio_idx is not None else 0),
        graph=str(gfile.relative_to(ROOT)), out=str(final.relative_to(ROOT)), sec=round(dur, 2), crf=a.crf)
    if a.dry_run:
        print(" ".join(cmd))
        return 0
    run(cmd, "ASSEMBLE", f"그래프 {gfile.relative_to(ROOT)} · 입력 파일 확인")
    fi = probe(final)
    log("ASSEMBLE", "final", file=str(final.relative_to(ROOT)), sec=round(fi["duration"], 2), size=f"{fi['width']}x{fi['height']}",
        fps=fi["fps"], audio=fi["audio"], mb=round(final.stat().st_size / 1e6, 1))
    if not preview and not a.placeholders and audio_idx is not None:
        r = subprocess.run([sys.executable, str(ROOT / "tools" / "loudnorm.py"), str(final)])
        if r.returncode:
            log("LOUDNORM", "FAILED — the assembled file is kept", next_step=f"python3 tools/loudnorm.py {final.relative_to(ROOT)}")
            return 1
    sheet = qa_sheet(final, [f for f in fits if not preview or preview[0] <= f["t0"] < preview[1]], out_dir / "qa", size,
                     offset=preview[0] if preview else 0.0)
    log("QA", "contact sheet (look at it)", file=str(sheet.relative_to(ROOT)))
    log("SUMMARY", "assembled", out=str(final.relative_to(ROOT)), clips=len(fits), slowed=sum(1 for f in fits if f["slow"] > 1),
        held=len(held), sec=round(time.perf_counter() - t_start, 1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
