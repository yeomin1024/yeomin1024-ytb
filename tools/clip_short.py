#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-11-06 — 자막 줄바꿈: 단위 낱말(원·만·%·배·명·개) 앞에서는 끊지 않음 ('2,000만 / 원' — 새 쇼츠 대본 v1.0 문장 15).
# 이전 v1.0 — 2026-11-06 — 사용자 지시 "클립 만들었어 확인해서 최종 영상 보여줘" (주식 쇼츠 애니메이션 bandoche-bunbae-2026-11 —
#          내레이션 없이 AI 클립을 이어 붙이는 꼴, 2026-11-06 "이미지를 영상화해 짧은 영상을 이어 붙이는 식으로"): 대본 전 장면 계획
#          (scene_clips v1.4 timing=clips)으로 세로 쇼츠 한 편을 만든다 — 클립마다 깨끗한 구간(use_from·use_to)·pingpong·화면 시간
#          (show_sec, 짧으면 1.35배까지 늦추고 마지막 장면을 멈춤) → 1080x1920 30fps · 그래프 장면(format=duo_chart)은 장면 80% 아래 붙임 +
#          위 그래프 카드(plan chart — 흐름만, 숫자 축 없음) · 장면마다 자막 한 문장(46px·2줄까지·아래 끝 y 1520 — video_guide 쇼츠 자막 띠) ·
#          무음 오디오 → <주제>/out/<영상ID>/final_1080p.mp4 + qa/still_*.png. 내레이션이 생기면 이 도구 대신 render.mjs + assemble_video.py.
#          (첫 still 점검 뒤 고침 — 모든 그래프 장면을 80% 로 줄이면 인물이 자막 자리로 내려와 S06 우는 얼굴을 자막이 가림 → 줄이기는 클립
#          "scale" 이 있을 때만(S03 — A 가 높이 16% 까지 뜀) · 이름표는 그래프 오른쪽 고정 칸 + 어두운 바탕 (점선·선 위에 겹쳐 읽기 어려웠음))
r"""
  python3 tools/clip_short.py stock bandoche-bunbae-2026-11 --shorts            # → stock/out/bandoche-bunbae-2026-11-shorts/final_1080p.mp4
  python3 tools/clip_short.py stock bandoche-bunbae-2026-11 --shorts --stills   # 장면마다 가운데 한 장만 (영상 없이 배치 점검)
  python3 tools/clip_short.py stock bandoche-bunbae-2026-11 --shorts --dry-run  # 계획·자막 줄바꿈만

plan.json 클립 키: use_from·use_to(초) · loop: "pingpong" · show_sec(화면 시간) · caption(자막 한 문장) · format: "duo_chart"(그래프 장면) ·
  scale(그 장면만 줄여 아래에 붙임 — 인물이 그래프 칸까지 올라오는 클립) · patch: {box: [x, y, w, h], fill: "#FFFFFF", why}
  (완성 화면 좌표 — AI 클립이 지어낸 글자를 덮음: fill 이 있으면 그 색 상자(drawbox — 둘레가 한 색일 때), 없으면 주변 픽셀로 메움(delogo))
plan.json chart: dates{start,end} · baseline{y} · lines[{who,label,points[[x,y]…]}] · segments[{clip, x:[x0,x1]}]
로그: [STAGE] [시각] key=value …   ※ 연구·교육용 영상 제작 도구 (투자 권유 아님)
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
import scene_clips as sc  # noqa: E402

ROOT = sc.ROOT
VERSION = "v1.1"
W, H, FPS = 1080, 1920, 30
MAX_SLOW = sc.MAX_SLOW                       # 1.35 — assemble_video 와 같음
FONT = ROOT / "video" / "public" / "fonts" / "NotoSansKR-700.ttf"
FONT_B = ROOT / "video" / "public" / "fonts" / "NotoSansKR-900.ttf"
# 자막 — video_guide 6번 쇼츠 (#cc left 540 · bottom 400 → 아래 끝 y 1520 · 띠 870 · 46px · 2줄까지)
NO_BREAK_BEFORE = ("원", "만", "%", "배", "명", "개")   # 이 낱말 앞에서는 줄을 바꾸지 않음 (v1.1)
CAP = dict(size=46, max_w=870, bottom=1520, pad_x=18, pad_y=12, line=1.32)
# 그래프 장면 — 위에 그래프 카드 (안전 구역 위 150). 클립 "scale"(<1)이면 장면을 줄여 아래에 붙이고 양옆은 흐린 배경
PANEL = (60, 150, 1020, 580)                 # x0 y0 x1 y1
PLOT = (110, 262, 740, 552)                  # 그래프 선이 그려지는 칸 — 오른쪽 740~1004 는 이름표 칸 (선 끝 오른쪽)
Y_RANGE = (10, 225)                           # plan chart y(처음 돈 100) → 칸 높이
COL = dict(A=(255, 140, 40), A_loss=(235, 60, 60), B=(40, 205, 190), base=(250, 205, 60), text=(255, 255, 255),
           sub=(190, 198, 215), panel=(14, 18, 30, 214), cap_bg=(0, 0, 0, 165))


def log(stage: str, msg: str = "", **kv):
    sc.log(stage, msg, **kv)


def font(size: int, heavy: bool = False) -> ImageFont.FreeTypeFont:
    f = FONT_B if heavy else FONT
    if not f.exists():
        raise SystemExit(f"[FONT] {f} 없음 — 새 컨테이너면 `node video/scripts/get-fonts.mjs` 먼저 (status 4번)")
    return ImageFont.truetype(str(f), size)


# --------------------------------------------------------------------------------------------------
def wrap(text: str, f: ImageFont.FreeTypeFont, max_w: int) -> list[str]:
    """띄어쓰기에서 줄바꿈 — 한 줄에 들어가면 한 줄, 아니면 두 줄의 길이가 비슷하게. 두 줄로도 넘으면 SystemExit (자막 2줄까지)."""
    if f.getlength(text) <= max_w:
        return [text]
    words = text.split(" ")
    best = None
    for i in range(1, len(words)):
        if words[i].startswith(NO_BREAK_BEFORE):                     # '2,000만 / 원' 처럼 단위만 다음 줄로 가지 않게
            continue
        a, b = " ".join(words[:i]), " ".join(words[i:])
        la, lb = f.getlength(a), f.getlength(b)
        if la <= max_w and lb <= max_w and (best is None or abs(la - lb) < best[0]):
            best = (abs(la - lb), [a, b])
    if not best:
        raise SystemExit(f"[CAPTION] 두 줄로도 {max_w}px 를 넘음 — 자막을 줄이기: {text!r}")
    return best[1]


def caption_layer(text: str) -> tuple[Image.Image, list[str]]:
    f = font(CAP["size"])
    lines = wrap(text, f, CAP["max_w"] - 2 * CAP["pad_x"])
    lh = round(CAP["size"] * CAP["line"])
    tw = max(f.getlength(t) for t in lines)
    bw, bh = int(tw + 2 * CAP["pad_x"]), int(lh * len(lines) + 2 * CAP["pad_y"])
    x0, y1 = (W - bw) // 2, CAP["bottom"]
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((x0, y1 - bh, x0 + bw, y1), radius=14, fill=COL["cap_bg"])
    for i, t in enumerate(lines):
        d.text((W // 2, y1 - bh + CAP["pad_y"] + i * lh + lh // 2), t, font=f, fill=COL["text"], anchor="mm",
               stroke_width=2, stroke_fill=(0, 0, 0))
    return im, lines


# --------------------------------------------------------------------------------------------------
def _interp(pts: list[list[float]], x: float) -> float:
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        if x0 <= x <= x1:
            return y0 + (y1 - y0) * (x - x0) / (x1 - x0) if x1 > x0 else y1
    return pts[-1][1]


def _upto(pts: list[list[float]], x: float) -> list[tuple[float, float]]:
    out = [(px, py) for px, py in pts if px < x]
    return out + [(x, _interp(pts, x))]


def _xy(x: float, y: float) -> tuple[float, float]:
    px0, py0, px1, py1 = PLOT
    return px0 + x * (px1 - px0), py1 - (y - Y_RANGE[0]) / (Y_RANGE[1] - Y_RANGE[0]) * (py1 - py0)


def _date(chart: dict, x: float) -> str:
    y0, m0 = map(int, chart["dates"]["start"].split("."))
    y1, m1 = map(int, chart["dates"]["end"].split("."))
    n = round(x * ((y1 - y0) * 12 + (m1 - m0)))
    k = (y0 * 12 + m0 - 1) + n
    return f"{k // 12}.{k % 12 + 1:02d}"


def chart_layer(chart: dict, x: float, fonts: dict) -> Image.Image:
    """그래프 카드 — 시간 x(0~1)까지 선이 자람. 숫자 축·수익률은 쓰지 않음 (plan chart.on_screen)."""
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle(PANEL, radius=28, fill=COL["panel"])
    d.text((PANEL[0] + 36, PANEL[1] + 28), _date(chart, x), font=fonts["date"], fill=COL["text"])
    d.text((PANEL[2] - 36, PANEL[1] + 40), "※ 흐름 예시", font=fonts["small"], fill=COL["sub"], anchor="ra")
    base = chart["baseline"]["y"]
    _, by = _xy(0, base)
    for xx in range(PLOT[0], PLOT[2] + 120, 28):                 # 노란 점선 = 기준(처음 넣은 돈)
        d.line([(xx, by), (min(xx + 14, PLOT[2] + 110), by)], fill=COL["base"], width=4)
    d.text((PLOT[0], by + 8), "처음 돈", font=fonts["small"], fill=COL["base"])
    tips = []
    for ln in chart["lines"]:
        pts = _upto(ln["points"], x)
        who = ln["who"]
        segs = []                                                  # A 는 기준선 아래 구간을 빨강으로
        for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
            if who == "A" and (y0 - base) * (y1 - base) < 0:
                xm = x0 + (x1 - x0) * (base - y0) / (y1 - y0)
                segs += [((x0, y0), (xm, base)), ((xm, base), (x1, y1))]
            else:
                segs.append(((x0, y0), (x1, y1)))
        for (x0, y0), (x1, y1) in segs:
            loss = who == "A" and min(y0, y1) < base - 1e-9 and max(y0, y1) <= base + 1e-9
            c = COL["A_loss"] if loss else COL[who]
            d.line([_xy(x0, y0), _xy(x1, y1)], fill=c, width=9, joint="curve")
        tx, ty = _xy(*pts[-1])
        tc = COL["A_loss"] if who == "A" and pts[-1][1] < base else COL[who]
        d.ellipse((tx - 13, ty - 13, tx + 13, ty + 13), fill=tc, outline=(255, 255, 255), width=4)
        tips.append(dict(who=who, label=f"{who} · {ln['label']}", x=tx, y=ty, c=tc))
    # 이름표 — 선 끝 오른쪽, 두 이름표가 겹치면 위아래로 벌림 (칸 안)
    tips.sort(key=lambda t: t["y"])
    lab_h = 46
    ys = [t["y"] for t in tips]
    if len(ys) == 2 and ys[1] - ys[0] < lab_h:
        mid = (ys[0] + ys[1]) / 2
        ys = [mid - lab_h / 2, mid + lab_h / 2]
    for t, yy in zip(tips, ys):
        yy = min(max(yy, PANEL[1] + 120), PANEL[3] - 34)
        lx = t["x"] + 26
        tw = fonts["label"].getlength(t["label"])
        if lx + tw > PANEL[2] - 14:
            raise SystemExit(f"[CHART] 이름표가 카드 밖 — PLOT 오른쪽 끝을 줄이기: {t['label']}")
        d.rounded_rectangle((lx - 10, yy - 24, lx + tw + 10, yy + 24), radius=12, fill=(10, 12, 20, 235))
        d.text((lx, yy), t["label"], font=fonts["label"], fill=t["c"], anchor="lm")
    return im


# --------------------------------------------------------------------------------------------------
def schedule(plan: dict) -> list[dict]:
    t, out = 0.0, []
    seg = {s["clip"]: s for s in (plan.get("chart") or {}).get("segments", [])}
    for c in plan["clips"]:
        a, b = float(c.get("use_from", 0.0)), float(c["use_to"])
        ping = c.get("loop") == "pingpong"
        src_len = (b - a) * (2 if ping else 1)
        show = float(c["show_sec"])
        slow = min(MAX_SLOW, show / src_len) if show > src_len else 1.0
        hold = max(0.0, show - src_len * slow)
        out.append(dict(name=c["name"], a=a, b=b, ping=ping, src_len=round(src_len, 3), show=show, slow=round(slow, 3),
                        hold=round(hold, 3), t0=round(t, 3), t1=round(t + show, 3), chart=c.get("format") == "duo_chart",
                        scale=float(c.get("scale", 1.0)), patch=c.get("patch"),
                        seg=seg.get(c["name"]), caption=c.get("caption", "")))
        t += show
    return out


def fit_clip(src: Path, s: dict, dst: Path):
    """클립 → 그 장면 길이의 1080x1920 30fps (그래프 장면은 80% 장면 + 흐린 배경)."""
    chain = f"trim=start={s['a']}:end={s['b']},setpts=PTS-STARTPTS"
    pre = f"[0:v]{chain}"
    if s["ping"]:
        pre += ",split[f][r];[r]reverse[rr];[f][rr]concat=n=2:v=1:a=0"
    pre += f",setpts=PTS*{s['slow']},fps={FPS}"
    if s["hold"] > 0:
        pre += f",tpad=stop_mode=clone:stop_duration={s['hold'] + 0.1}"
    pre += f",trim=duration={s['show']},setpts=PTS-STARTPTS"
    cover = f"scale={W}:{round(W * 1280 / 704)}:flags=lanczos,crop={W}:{H}"
    dl = ""
    if s["patch"]:
        x, y, w, h = s["patch"]["box"]
        fill = s["patch"].get("fill")
        dl = (f"drawbox=x={x}:y={y}:w={w}:h={h}:color=0x{fill.lstrip('#')}:t=fill," if fill
              else f"delogo=x={x}:y={y}:w={w}:h={h},")
        log("FIT", "patch", name=s["name"], box=f"{x},{y},{w},{h}", mode="fill " + fill if fill else "delogo",
            why=s["patch"].get("why", ""))
    if s["scale"] < 1.0:
        sw, sh = round(W * s["scale"] / 2) * 2, round(H * s["scale"] / 2) * 2
        g = (f"{pre},{cover},split[bg][fg];[bg]boxblur=24:2,eq=brightness=-0.06[bgb];"
             f"[fg]scale={sw}:{sh}:flags=lanczos[fgs];[bgb][fgs]overlay=x={(W - sw) // 2}:y={H - sh},{dl}format=yuv420p[v]")
    else:
        g = f"{pre},{cover},{dl}format=yuv420p[v]"
    cmd = ["ffmpeg", "-v", "error", "-y", "-i", str(src), "-filter_complex", g, "-map", "[v]", "-an",
           "-c:v", "libx264", "-preset", "fast", "-crf", "14", "-r", str(FPS), str(dst)]
    r = subprocess.run(cmd, capture_output=True, encoding="utf-8", errors="replace")
    if r.returncode:
        raise SystemExit(f"[FIT] ffmpeg 실패 {s['name']}: {r.stderr[-600:]} — 클립 {src} · use_from/use_to 확인")


def overlay_frame(t: float, sched: list[dict], chart: dict | None, caps: dict, fonts: dict, cache: dict) -> bytes:
    s = next((x for x in sched if x["t0"] <= t < x["t1"]), sched[-1])
    key = s["name"]
    if s["chart"] and chart and s["seg"]:
        u = min(1.0, max(0.0, (t - s["t0"]) / s["show"]))
        x0, x1 = s["seg"]["x"]
        im = chart_layer(chart, x0 + (x1 - x0) * u, fonts)
        im.alpha_composite(caps[key])
        return im.tobytes()
    if key not in cache:                                           # 그래프 없는 장면은 자막만 — 장면마다 한 번
        cache[key] = caps[key].tobytes()
    return cache[key]


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="대본 전 클립 쇼츠 합치기 " + VERSION)
    ap.add_argument("topic")
    ap.add_argument("vid")
    ap.add_argument("--shorts", action="store_true")
    ap.add_argument("--stills", action="store_true", help="장면마다 가운데 한 장만")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--crf", type=int, default=18)
    a = ap.parse_args(argv)
    t_start = time.time()
    p = sc.paths(a.topic, a.vid, a.shorts)
    plan = sc.load_plan(p["plan"])
    sched = schedule(plan)
    total = sched[-1]["t1"]
    log("PLAN", "loaded", plan=str(p["plan"].relative_to(ROOT)), clips=len(sched), total_sec=round(total, 2),
        chart_scenes=",".join(s["name"] for s in sched if s["chart"]))
    caps = {}
    for s in sched:
        caps[s["name"]], lines = caption_layer(s["caption"])
        log("FIT", s["name"], use=f"{s['a']}-{s['b']}", pingpong=s["ping"], src_len=s["src_len"], show=s["show"], slow=s["slow"],
            hold=s["hold"], t0=s["t0"], chart=s["chart"], scale=s["scale"], caption_lines=len(lines), caption=" / ".join(lines))
        if s["hold"] > 0.6:
            log("FIT", "WARNING last frame held long — 구간을 늘리거나 show_sec 를 줄이기", name=s["name"], hold=s["hold"])
    if a.dry_run:
        return 0
    out, qa, tmp = p["out"], p["out"] / "qa", p["out"] / "tmp_clip_short"
    qa.mkdir(parents=True, exist_ok=True)
    tmp.mkdir(parents=True, exist_ok=True)
    fonts = dict(date=font(44, True), small=font(36), label=font(38, True))
    chart = plan.get("chart")
    for s in sched:
        src = out / "clips" / f"{s['name']}.mp4"
        if not src.exists():
            raise SystemExit(f"[FIT] 클립 없음 {src} — `python3 tools/scene_clips.py fetch {a.topic} {a.vid}{' --shorts' if a.shorts else ''}`")
        fit_clip(src, s, tmp / f"{s['name']}.mp4")
    log("FIT", "clips fitted", n=len(sched), sec=round(time.time() - t_start, 1))
    lst = tmp / "list.txt"
    lst.write_text("".join(f"file '{(tmp / (s['name'] + '.mp4')).as_posix()}'\n" for s in sched), encoding="utf-8")
    base = tmp / "base.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", str(base)], check=True)
    if a.stills:
        for s in sched:
            t = (s["t0"] + s["t1"]) / 2
            fr = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.3f}", "-i", str(base), "-frames:v", "1", "-f", "rawvideo",
                                 "-pix_fmt", "rgba", "-"], capture_output=True).stdout
            im = Image.frombytes("RGBA", (W, H), fr)
            im.alpha_composite(Image.frombytes("RGBA", (W, H), overlay_frame(t, sched, chart, caps, fonts, {})))
            im.convert("RGB").save(qa / f"still_{s['name']}.png")
        log("STILLS", "wrote", dir=str(qa.relative_to(ROOT)), n=len(sched))
        return 0
    final = out / "final_1080p.mp4"
    n_frames = round(total * FPS)
    cmd = ["ffmpeg", "-v", "error", "-y", "-i", str(base),
           "-f", "rawvideo", "-pix_fmt", "rgba", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
           "-f", "lavfi", "-t", f"{total:.3f}", "-i", "anullsrc=r=48000:cl=stereo",
           "-filter_complex", "[0:v][1:v]overlay=0:0:format=auto,format=yuv420p[v]", "-map", "[v]", "-map", "2:a",
           "-c:v", "libx264", "-preset", "medium", "-crf", str(a.crf), "-r", str(FPS), "-c:a", "aac", "-b:a", "128k",
           "-movflags", "+faststart", "-t", f"{total:.3f}", str(final)]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    cache = {}
    try:
        for i in range(n_frames):
            proc.stdin.write(overlay_frame(i / FPS, sched, chart, caps, fonts, cache))
        proc.stdin.close()
    except BrokenPipeError:
        pass
    err = proc.stderr.read().decode("utf-8", "replace")
    if proc.wait():
        raise SystemExit(f"[RENDER] ffmpeg 실패: {err[-600:]}")
    info = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration,size:stream=codec_type,width,height,r_frame_rate",
                           "-of", "json", str(final)], capture_output=True, encoding="utf-8").stdout
    d = json.loads(info)
    v = next(x for x in d["streams"] if x["codec_type"] == "video")
    log("RENDER", "final", file=str(final.relative_to(ROOT)), size=f"{v['width']}x{v['height']}", fps=v["r_frame_rate"],
        duration_sec=round(float(d["format"]["duration"]), 2), mb=round(int(d["format"]["size"]) / 1e6, 1), frames=n_frames,
        audio="silent (no narration yet)", sec=round(time.time() - t_start, 1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
