#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-11-05 — 내레이션 이상한 소리·발음 확인 후보 찾기 (사용자 지시 2026-11-05 "2편 음성 확인해서 발음 이상하거나 이상한 소리나는 부분 찾아봐").
#   이 클라우드 환경에서는 음성 인식 모델(Whisper·Vosk)을 받을 수 없어(호스트 막힘) '무엇을 말했는지'는 못 듣는다 → 소리 모양으로 찾고, 발음은 '틀리기 쉬운 낱말' 목록 + 들을 조각으로.
#   검사 (문장마다, narration.mp3 + tts_narration.json 의 문장 시각):
#     ONSET  첫 낱말 앞 웅얼거림 — 말소리 시작 뒤 300ms 안에 깊은 끊김(-58dB 아래 30ms 넘게)이 있는데, 그 자리에 글자상 끊길 까닭(파열음·받침 닫힘·쉼표)이 없음
#            (1편 문장 8 「당신에게는」 앞 0.2초 — guides/tts_guide.md 5-4 와 같은 꼴)
#     TAIL   마지막 낱말 뒤 다시 나는 소리 — 강한 말소리가 끝난 뒤 -52dB 아래 60ms 넘게 쉬었다가 -40dB 넘게 40ms 넘게 다시 올라옴
#     GAP    문장 안 긴 끊김 — 말소리 사이 -55dB 아래 0.7초 넘게 (쉼표 쉼은 0.5초 안팎) ('|' 끊어 읽기 문장은 뺌)
#     CLICK  딸깍 — 조용한 곳(앞뒤 5ms 세기 -40dB 아래)에서 표본 하나가 크게 튐 / 문장 이음매 첫·끝 표본이 0 에서 멂
#     RATE   말 빠르기 — 읽는 글(사전 적용) 음절(숫자·영문 어림) ÷ 말소리 길이가 같은 영상 가운데값의 ±28% 밖 (빠지거나 덧붙은 소리 의심)
#     REPORT tts_report.md 확인 칸이 ✅ 가 아니고 '속도·크기 맞춤·나눠 만듦'만도 아닌 문장
#     WORD   발음 확인 — 영어·숫자·기호가 든 낱말 (사전으로 바꾼 소리도 함께 적음)
#   출력: <대본 폴더>/audio_check.md (표 + 시각) · 들을 조각 <주제>/out/<영상ID>/audio_check_clips.mp3 (후보마다 앞뒤 0.6초, 사이에 삐 소리 — git 에 넣지 않음).
# 사용: python3 tools/audio_check.py stock daebi-test-2026-11   (쇼츠는 daebi-test-2026-11-shorts)
# ※ 연구·교육용 도구 — 투자 권유 아님.
import argparse
import json
import logging
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent
sys.path.insert(0, str(TOOLS))
import tts_narration as T  # noqa: E402  (사전·읽는 글 규칙을 TTS 와 똑같이)

SR = 24000
HOP = 0.01
logging.basicConfig(level=logging.INFO, format="%(message)s")


def log(stage, **kv):
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    logging.info(f"[{stage}] [{ts}] " + " ".join(f"{k}={v}" for k, v in kv.items()))


def src_dir(topic, vid):
    if vid.endswith("-shorts"):
        return ROOT / topic / "source" / vid[: -len("-shorts")] / "shorts"
    return ROOT / topic / "source" / vid


def load_audio(p):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(p), "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.int16).astype(np.float64) / 32768.0


def env_db(a):
    h = int(SR * HOP); n = len(a) // h
    if n == 0:
        return np.array([-180.0])
    x = a[: n * h].reshape(n, h)
    return 20 * np.log10(np.sqrt((x ** 2).mean(axis=1)) + 1e-9)


# ---- 한글 음절 → 끊길 까닭이 있는 자리 (파열·파찰음 첫소리, 닫히는 받침, 쉼표·띄어쓰기 뒤 파열음)
STOP_ONSET = {0, 1, 3, 4, 7, 8, 12, 13, 14, 15, 16, 17}          # ㄱㄲㄷㄸㅂㅃㅈㅉㅊㅋㅌㅍ
STOP_CODA = {1, 2, 3, 7, 9, 17, 18, 19, 20, 22, 23, 24, 25, 26}    # ㄱㄲㄳㄷㄺㅂㅄㅅㅆㅈㅊㅋㅌㅍ
FRIC_CODA = {19, 20}                                               # ㅅㅆ


def syl_count(s):
    """말 빠르기용 음절 수 어림 — 한글 음절 + 숫자 한 자 1.3 + 영문 한 자 1.2 (사전으로 안 바뀐 숫자·영문을 모델이 읽는 몫)."""
    return sum(1 for ch in s if "가" <= ch <= "힣") + 1.3 * sum(ch.isdigit() for ch in s) + 1.2 * sum(ch.isascii() and ch.isalpha() for ch in s)


def syllables(s):
    """읽는 글 → [(음절, 앞에 쉼표 있음)] (한글만)."""
    out, comma = [], False
    for ch in s:
        if "가" <= ch <= "힣":
            out.append((ch, comma)); comma = False
        elif ch in ",.?!|":
            comma = True
    return out


def closure_after(sy, i):
    """i 번째 음절 뒤에 끊길 까닭이 있나."""
    if i + 1 >= len(sy):
        return True
    c = ord(sy[i][0]) - 0xAC00; n = ord(sy[i + 1][0]) - 0xAC00
    jong = c % 28; cho_next = n // 588
    if sy[i + 1][1]:
        return True
    if cho_next in STOP_ONSET:
        return True
    if jong in STOP_CODA - FRIC_CODA:
        return True                                  # 파열·파찰 받침은 뒤가 ㅇ 이어도(이어 읽어도) 닫힘이 남음 — 같은→가튼·앞으로→아프로
    return jong in FRIC_CODA and cho_next != 11     # ㅅ·ㅆ 받침은 뒤가 ㅇ 이면 이어 읽혀 안 닫힘


def check_sentence(it, seg, spoken, rate_med):
    """한 문장 검사 → [(검사, 시각(초, 절대), 설명)]."""
    out = []
    e = env_db(seg)
    if len(e) < 5:
        return out
    t0 = it["start"]
    on = next((i for i, v in enumerate(e) if v > -40), None)
    voiced = np.where(e > -45)[0]
    if on is None or len(voiced) == 0:
        return [("GAP", t0, "말소리가 거의 없음")]
    last = voiced[-1]
    sy = syllables(spoken)
    split = "|" in spoken
    # ONSET
    if not split and sy:
        run = 0
        for i in range(on + 3, min(on + 30, len(e))):
            run = run + 1 if e[i] < -58 else 0
            if run >= 3:
                gap_t = (i - 2 - on) * HOP
                dur = max(0.3, (last - on) * HOP)
                per = dur / len(sy)
                k = int(gap_t / per)                     # 끊김 앞에 읽혔어야 할 음절 수
                ok = any(closure_after(sy, j) for j in range(max(0, k - 1), min(len(sy), k + 1)))
                if not ok:
                    out.append(("ONSET", round(t0 + on * HOP, 3),
                                f"시작 {gap_t:.2f}초 뒤 깊은 끊김 — 앞 음절 약 {k}개 '{''.join(s for s, _ in sy[:max(1, k)])}' 뒤에 끊길 까닭 없음"))
                break
    # TAIL — 강한 말소리(95% 값 -12dB 안)가 끝난 뒤 -52dB 아래로 60ms 넘게 내려갔다가 -40dB 넘게 40ms 넘게 다시 올라옴
    strong = np.where(e > np.percentile(e[on:last + 1], 95) - 12)[0]
    main_end = strong[-1] if len(strong) else last
    low_run, dipped = 0, False
    for i in range(main_end + 1, len(e) - 3):
        low_run = low_run + 1 if e[i] < -52 else 0
        if low_run >= 6:
            dipped = True
        elif dipped and all(e[i:i + 4] > -40):
            if len(sy) >= 2 and closure_after(sy, len(sy) - 2):
                break                                    # 마지막 음절 앞이 닫히는 자리(났죠·겠습니까) — 다시 나는 소리는 마지막 음절
            out.append(("TAIL", round(t0 + i * HOP, 3), f"마지막 낱말이 끝난 뒤({(i - main_end) * HOP:.2f}초) 다시 나는 소리"))
            break
    # GAP
    if not split:
        run, st = 0, None
        for i in range(on, last):
            if e[i] < -55:
                run += 1; st = st if st is not None else i
            else:
                if run * HOP >= 0.7:
                    out.append(("GAP", round(t0 + st * HOP, 3), f"문장 안 {run * HOP:.2f}초 끊김"))
                run, st = 0, None
    # CLICK (조용한 곳의 튐)
    d = np.abs(np.diff(seg))
    w = int(SR * 0.005)
    for idx in np.where(d > 0.25)[0][:50]:
        lo, hi = max(0, idx - w), min(len(seg), idx + w)
        around = np.concatenate([seg[lo:max(lo, idx - 2)], seg[min(hi, idx + 3):hi]])
        if len(around) and 20 * np.log10(np.sqrt((around ** 2).mean()) + 1e-9) < -40:
            out.append(("CLICK", round(t0 + idx / SR, 3), f"조용한 곳 튐 {d[idx]:.2f}"))
            break
    for edge, val in (("시작", seg[0]), ("끝", seg[-1])):
        if abs(val) > 0.02:
            out.append(("CLICK", round(t0 if edge == "시작" else it["end"], 3), f"이음매 {edge} 표본 {val:+.3f}"))
    # RATE
    if not split and len(sy) >= 6 and rate_med:
        rate = syl_count(spoken) / max(0.2, (last - on) * HOP)
        if abs(rate / rate_med - 1) > 0.28:
            out.append(("RATE", round(t0 + on * HOP, 3), f"{rate:.1f} 음절/초 (가운데값 {rate_med:.1f}) — 빠지거나 덧붙은 소리 의심"))
    return out


def report_flags(src):
    """tts_report.md 확인 칸 — ✅·맞춤·나눠 만듦 말고 다른 말이 있는 문장."""
    p = src / "tts_report.md"
    flags = {}
    if not p.exists():
        return flags
    for ln in p.read_text("utf-8").splitlines():
        m = re.match(r"\|\s*(\d+)\s*\|.*\|\s*([^|]*)\|\s*$", ln)
        if not m:
            continue
        note = m.group(2).strip()
        rest = [x.strip() for x in note.split("·") if x.strip() and not x.strip().startswith(("✅", "속도 맞춤", "크기 맞춤", "나눠 만듦"))]
        if rest:
            flags[int(m.group(1))] = " · ".join(rest)
    return flags


WORD_RE = re.compile(r"[^\s,.?!]*[A-Za-z0-9%&$][^\s,.?!]*")


def main(argv=None):
    ap = argparse.ArgumentParser(description="내레이션 이상한 소리·발음 확인 후보")
    ap.add_argument("topic"); ap.add_argument("video_id")
    ap.add_argument("--no-clips", action="store_true")
    ap.add_argument("--audio", help="다른 오디오 파일로 검사 (시험용 — 보고 파일은 쓰지 않음)")
    a = ap.parse_args(argv)
    src = src_dir(a.topic, a.video_id)
    meta = json.loads((src / "tts_narration.json").read_text("utf-8"))
    narr = Path(a.audio) if a.audio else src / "narration.mp3"
    log("INPUT", video=a.video_id, audio=narr, sentences=len(meta["items"]), tool_audio=meta.get("tool"))
    lex = T.load_lexicon([ROOT / a.topic / "tts_lexicon.tsv"] + ([src.parent / "tts_lexicon.tsv"] if a.video_id.endswith("-shorts") else []) + [src / "tts_lexicon.tsv"])
    audio = load_audio(narr)
    items = meta["items"]
    spoken = {it["n"]: T.tts_text(it["text"], lex) for it in items}
    # 말 빠르기 가운데값
    rates = []
    for it in items:
        sy = syllables(spoken[it["n"]])
        seg = audio[int(it["start"] * SR): int(it["end"] * SR)]
        e = env_db(seg); v = np.where(e > -45)[0]
        if len(sy) >= 6 and len(v) and "|" not in spoken[it["n"]]:
            rates.append(syl_count(spoken[it["n"]]) / max(0.2, (v[-1] - v[0]) * HOP))
    rate_med = float(np.median(rates)) if rates else None
    found = []
    for it in items:
        seg = audio[int(it["start"] * SR): int(it["end"] * SR)]
        for kind, t, why in check_sentence(it, seg, spoken[it["n"]], rate_med):
            found.append((it["n"], kind, t, why))
    for n, why in report_flags(src).items():
        it = next(x for x in items if x["n"] == n)
        found.append((n, "REPORT", it["start"], why))
    words = []
    for it in items:
        for w in WORD_RE.findall(it["text"]):
            sp = T.tts_text(w, lex)
            words.append((it["n"], it["start"], w, sp if sp != w else ""))
    found.sort(key=lambda x: x[2])
    by_kind = {}
    for f in found:
        by_kind[f[1]] = by_kind.get(f[1], 0) + 1
    log("CHECK", candidates=len(found), **by_kind, words=len(words), rate_median=round(rate_med or 0, 2))
    # 들을 조각
    clips_path = None
    if found and not a.no_clips and not a.audio:
        out_dir = ROOT / a.topic / "out" / a.video_id; out_dir.mkdir(parents=True, exist_ok=True)
        clips_path = out_dir / "audio_check_clips.mp3"
        beep = np.sin(2 * np.pi * 1000 * np.arange(int(SR * 0.15)) / SR) * 0.15
        sil = np.zeros(int(SR * 0.35))
        parts = []
        for n, kind, t, why in found:
            it = next(x for x in items if x["n"] == n)
            lo = max(0, int((min(t, it["start"]) - 0.6) * SR)); hi = min(len(audio), int((max(t + 0.8, it["end"]) + 0.3) * SR)) if kind in ("REPORT", "RATE") else min(len(audio), int((t + 1.2) * SR))
            parts += [beep, sil, audio[lo:hi], sil]
        pcm = (np.clip(np.concatenate(parts), -1, 1) * 32767).astype(np.int16).tobytes()
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "s16le", "-ar", str(SR), "-ac", "1", "-i", "-", "-b:a", "96k", str(clips_path)], input=pcm, check=True)
        log("CLIPS", file=clips_path.relative_to(ROOT), clips=len(found))
    # 보고
    def mmss(t):
        return f"{int(t // 60)}:{t % 60:04.1f}"
    md = [f"# 내레이션 확인 후보 — {a.video_id}", "",
          f"> `tools/audio_check.py` v1.0 · {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M')} UTC · 오디오 `{narr}` ({meta.get('tool')}) · 문장 {len(items)}개 · 말 빠르기 가운데값 {rate_med:.1f} 음절/초",
          "> 이 환경은 음성 인식 모델을 받을 수 없어 **무엇을 말했는지는 듣지 못함** — 소리 모양으로 찾은 후보 + 틀리기 쉬운 낱말. 들을 조각 `" + (str(clips_path.relative_to(ROOT)) if clips_path else "없음") + "` (후보 순서대로, 삐 소리로 나눔). 연구·교육용.", "",
          "## 1. 소리 후보", "", "| # | 시각 | 문장 | 검사 | 설명 | 문장 |", "|---|---|---|---|---|---|"]
    for k, (n, kind, t, why) in enumerate(found, 1):
        it = next(x for x in items if x["n"] == n)
        md.append(f"| {k} | {mmss(t)} | {n} | {kind} | {why} | {it['text'][:40]} |")
    if not found:
        md.append("| - | - | - | - | 후보 없음 | - |")
    md += ["", "## 2. 발음 확인 낱말 (영어·숫자·기호 — 귀로 확인)", "", "| 시각 | 문장 | 낱말 | 사전으로 바꾼 소리 |", "|---|---|---|---|"]
    md += [f"| {mmss(t)} | {n} | {w} | {sp or '(그대로 — 모델이 읽음)'} |" for n, t, w, sp in words]
    if not a.audio:
        (src / "audio_check.md").write_text("\n".join(md) + "\n", "utf-8")
        log("DONE", report=(src / "audio_check.md").relative_to(ROOT))
    for n, kind, t, why in found:
        print(f"  {mmss(t)}  문장 {n:>3}  {kind:<6} {why}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
