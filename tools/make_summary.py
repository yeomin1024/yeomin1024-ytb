#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.3 — 2026-10-10 — 사용자 지시: 요약에서 스토리보드 빼기 (상태 줄·4번 절 삭제, 영상 코드 상태로 대체),
#          내레이션 역할(사연자·진행자, voices/*.json) 표시, 오디오가 지금 대본으로 만든 것인지(tts_narration.json) 표시
#          (v1.2: 파트 라벨 판정을 srt_tool.is_label과 같게; v1.1: 예약 공개 시각 표시; v1.0: 영상별 summary.md, --thumb-todo, 표준 라이브러리만)
r"""
영상 하나의 결과물을 한 문서로 모읍니다: 상태 → 제목 3개 → 썸네일 3개 → 업로드 정보 → 대본(파트마다 사연자·진행자 표시).
스토리보드는 넣지 않는다 (사용자 지시 2026-10-10).

  python tools/make_summary.py stock bittu-2026-10      # → stock/source/bittu-2026-10/summary.md
  python tools/make_summary.py --all                    # 모든 주제 폴더의 source/<영상ID>/ (upload.md가 있는 것)
  python tools/make_summary.py --thumb-todo stock       # 이미지가 아직 없는 썸네일의 [A] 프롬프트 모음 → stock/thumbnail_todo.md

읽는 파일: source/<영상ID>/{titles.md, thumbnails/thumbnail_1~3.md·이미지, upload.md, <영상ID>.txt·.srt, README.md, youtube.json,
          narration.*, tts_narration.json}, out/<영상ID>/final_1080p.mp4, voices/*.json, video/src/episodes/<영상ID>/
원본 파일을 고치지 않는다. 내용을 바꾸려면 원본을 고치고 다시 실행한다.
"""
import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import srt_tool  # noqa: E402  (문장 파싱·SRT 묶음 재사용)

AUDIO_EXTS = (".mp3", ".wav", ".m4a")
VOICES_DIR = ROOT / "voices"     # 내레이션 역할 설정 (tools/tts_narration.py 와 같은 파일·같은 규칙)
IMG_EXTS = (".png", ".jpg", ".jpeg", ".webp")


def section_code(md, word):
    m = re.search(rf"^##\s*\d+\.\s*[^\n]*{word}[^\n]*\n(.*?)(?=^##\s|\Z)", md, re.M | re.S)
    if not m:
        return None
    c = re.search(r"```[^\n]*\n(.*?)\n```", m.group(1), re.S)
    return c.group(1) if c else None


def kst(iso):
    t = dt.datetime.fromisoformat(iso.replace("Z", "+00:00")).astimezone(dt.timezone(dt.timedelta(hours=9)))
    return t.strftime("%Y-%m-%d %H:%M")


def mmss(t):
    return f"{int(t // 60)}:{int(t % 60):02d}"


def voice_roles():
    """voices/*.json → [(역할, 이름, 파트 낱말)]. 낱말이 맞는 역할이 먼저, 없으면 "*" 역할 (tts_narration.role_of 와 같은 규칙)."""
    roles = []
    for p in sorted(VOICES_DIR.glob("*.json")):
        try:
            d = json.loads(p.read_text("utf-8-sig"))
        except json.JSONDecodeError:
            continue
        roles.append((p.stem, d.get("name", p.stem), d.get("parts", ["*"])))
    return sorted(roles, key=lambda r: ("*" in r[2], r[0]))


def role_name(label, roles):
    for _, name, parts in roles:
        if any(k != "*" and k in label for k in parts):
            return name
    return next((name for _, name, parts in roles if "*" in parts), "")


def role_ranges(txt_path, roles):
    """역할별 문장 범위 → '사연자 1–16 · 진행자 17–88'."""
    spans, n, label, in_card = {}, 0, "", False
    for raw in txt_path.read_text("utf-8").splitlines():
        line = raw.strip()
        if not line:
            in_card = False
            continue
        if srt_tool.is_label(line):
            label, in_card = line.lstrip("-").strip(), False
            continue
        if line.startswith("[장면]"):
            in_card = True
            continue
        if in_card:
            continue
        n += 1
        spans.setdefault(role_name(label, roles), []).append(n)
    return " · ".join(f"{k} {v[0]}–{v[-1]}" if v[-1] - v[0] + 1 == len(v) else f"{k} {len(v)}문장" for k, v in spans.items())


def script_block(txt_path, roles=()):
    """대본을 파트별로, 문장 번호를 붙여 보여 준다 (번호 = 대본 문장 번호). 파트 제목 옆에 읽는 역할(사연자·진행자)."""
    out, n, in_card = [], 0, False
    for raw in txt_path.read_text("utf-8").splitlines():
        line = raw.strip()
        if not line:
            in_card = False
            continue
        if srt_tool.is_label(line):
            label = line.lstrip('-').strip()
            who = role_name(label, roles) if roles else ""
            out.append(f"\n**{label}**" + (f" — 🎙 {who}" if who else "") + "\n")
            in_card = False
            continue
        if line.startswith("[장면]"):
            out.append(f"\n> 🟨 {line} (화면 고지 카드 — 자막·내레이션 아님)")
            in_card = True
            continue
        if in_card:
            out.append(f"> {line}")
            continue
        n += 1
        out.append(f"{n}. {line}")
    return "\n".join(out).strip() + "\n"


def thumb_section(src, vid, adopted_n):
    rows = []
    for i in (1, 2, 3):
        md_path = src / "thumbnails" / f"thumbnail_{i}.md"
        if not md_path.exists():
            rows.append(f"### 썸네일 {i}\n(프롬프트 파일 없음)\n")
            continue
        md = md_path.read_text("utf-8")
        head = md.splitlines()[0].lstrip("# ").strip()
        hyp = re.search(r"\|\s*시험하는 가설\s*\|\s*(.+?)\s*\|", md)
        words = re.search(r"## 문구[^\n]*\n(.*?)(?=\n## )", md, re.S)
        prompt = re.search(r"## \[A\][^\n]*\n```\n(.*?)\n```", md, re.S)
        img = next((p for p in (src / "thumbnails" / f"thumbnail_{i}{e}" for e in IMG_EXTS) if p.exists()), None)
        part = [f"### 썸네일 {i}{' ✅ 기본(채택 제목의 짝)' if i == adopted_n else ''} — {head.split('—')[-1].strip()}"]
        part.append(f"![thumbnail_{i}](thumbnails/{img.name})" if img else
                    f"🖼️ 이미지 없음 → 이미지 AI에 `thumbnails/thumbnail_{i}.md`의 [A] 프롬프트를 넣어 만든 뒤 "
                    f"`thumbnails/thumbnail_{i}.png`로 저장")
        if hyp:
            part.append(f"- 가설: {hyp.group(1)}")
        if words:
            part.append(words.group(1).strip())
        if prompt:
            part.append(f"<details><summary>[A] 완성형 프롬프트</summary>\n\n```\n{prompt.group(1)}\n```\n</details>")
        rows.append("\n\n".join(part) + "\n")
    return "\n".join(rows)


def build(topic, vid):
    src = ROOT / topic / "source" / vid
    out_dir = ROOT / topic / "out" / vid
    txt, srt = src / f"{vid}.txt", src / f"{vid}.srt"
    upload_md = (src / "upload.md").read_text("utf-8") if (src / "upload.md").exists() else ""
    titles_md = (src / "titles.md").read_text("utf-8") if (src / "titles.md").exists() else ""

    # ── 상태 ──
    sents = srt_tool.parse_txt(str(txt)) if txt.exists() else []
    subs = srt_tool.parse_srt(str(srt)) if srt.exists() else []
    groups, problems = srt_tool.group(subs, sents) if sents and subs else ([], ["SRT 없음"])
    length = mmss(groups[-1]["end"]) if groups else "?"
    audio = next((p for p in (src / f"narration{e}" for e in AUDIO_EXTS) if p.exists()), None)
    yt = json.loads((src / "youtube.json").read_text("utf-8")) if (src / "youtube.json").exists() else None
    roles = voice_roles()
    meta_p = src / "tts_narration.json"
    tts = json.loads(meta_p.read_text("utf-8")) if meta_p.exists() else None
    if audio and tts:   # 오디오가 지금 대본으로 만든 것인지 (문장 글 비교 — tts_narration.py check 와 같은 뜻)
        old = [i["text"] for i in tts.get("items", [])]
        diff = [i + 1 for i in range(max(len(old), len(sents))) if i >= len(old) or i >= len(sents) or old[i] != sents[i]]
        audio_note = " · 지금 대본과 같음" if not diff else f" · ⚠️ 옛 대본으로 만든 오디오 (바뀐 문장 {diff[0]}번 등 {len(diff)}개) → Kaggle에서 다시"
    else:
        audio_note = " · 대본과 같은지 정보 없음(직접 녹음)" if audio else ""
    has_code = (ROOT / "video" / "src" / "episodes" / vid).is_dir()
    imgs = [i for i in (1, 2, 3) if any((src / "thumbnails" / f"thumbnail_{i}{e}").exists() for e in IMG_EXTS)]
    adopted = re.search(r"\[x\]\s*\*\*(T\d)[^\n]*?\*\*\s*(.+?)\s*`", titles_md)
    pair = re.search(r"\[x\].*짝 썸네일:\s*thumbnail_(\d)", titles_md)
    adopted_n = int(pair.group(1)) if pair else 1
    title = (section_code(upload_md, "제목") or "").strip()
    rendered = (out_dir / "final_1080p.mp4").exists()
    status = [
        ("대본·SRT", f"✅ 문장 {len(sents)} / 자막 {len(subs)}, 길이 {length} "
                    f"({'오디오에 맞춤' if audio and (src / f'{vid}.srt').stat().st_mtime >= audio.stat().st_mtime else 'SRT 추정'})"
         if not problems else f"⚠️ {problems[0]}"),
        ("제목 3개", f"✅ 채택 {adopted.group(1)}" if adopted else ("✅" if titles_md else "❌ 없음")),
        ("썸네일", f"프롬프트 3개 ✅ · 이미지 {len(imgs)}/3" + (" (이미지 AI로 만들어 `thumbnails/thumbnail_N.png`에 저장)" if len(imgs) < 3 else "")),
        ("업로드 시트", "✅ 설명란·태그·고정 댓글·챕터" if upload_md else "❌ 없음"),
        ("내레이션 역할", (role_ranges(txt, roles) + " (`voices/*.json`)") if roles and txt.exists() else "voices/ 없음"),
        ("오디오", f"✅ {audio.name}{audio_note}" if audio else
         f"⏳ 없음 → Kaggle에서 `tts_narration.py all`로 만들어 `source/{vid}/narration.mp3`에 올리면 영상 제작 시작"),
        ("영상 코드", f"✅ `video/src/episodes/{vid}/`" if has_code else "⏳ 오디오가 생기면 Claude가 만든다 (승인 없이 바로 렌더)"),
        ("렌더", "✅ final_1080p.mp4" if rendered else "⏳ 오디오 뒤"),
        ("유튜브", (f"✅ 비공개 업로드 [{yt['videoId']}]({yt['studio']}) ({yt['uploadedAt'][:10]})"
                   + (f" · 예약 공개 {kst(yt['publishAt'])} (한국 시간)" if yt.get("publishAt") else "")) if yt
         else "⏳ 렌더 뒤 비공개 업로드 + 렌더 완료 1시간 뒤 예약 공개"),
    ]

    md = [f"# {vid} 한눈에 보기", "",
          f"자동 생성 — `python tools/make_summary.py {topic} {vid}` ({dt.datetime.now().strftime('%Y-%m-%d %H:%M')}). "
          "이 파일은 고치지 말고 원본(대본·titles.md·thumbnails/·upload.md)을 고친 뒤 다시 만든다.", ""]
    if title:
        md += [f"> **{title}**", ""]
    md += ["## 0. 상태", "", "| 단계 | 상태 |", "|---|---|"] + [f"| {a} | {b} |" for a, b in status] + [""]
    md += ["## 1. 제목 3개 (`titles.md`)", ""]
    md += [l for l in titles_md.splitlines() if re.match(r"^- \[[ x]\] \*\*T\d", l)] or ["(없음)"]
    md += ["", "## 2. 썸네일 3개 (`thumbnails/`)", "", "썸네일은 프롬프트 파일이 산출물이다. 이미지는 이미지 AI가 프롬프트로 만든다.", "",
           thumb_section(src, vid, adopted_n)]
    desc = section_code(upload_md, "설명란")
    tags = section_code(upload_md, "태그")
    pin = section_code(upload_md, "고정 댓글")
    md += ["## 3. 업로드 정보 (`upload.md`)", ""]
    md += ["**설명란**", "", "```", desc or "(없음)", "```", "", f"**태그**: {tags or '(없음)'}", "", "**고정 댓글**", "", "```", pin or "(없음)", "```", ""]
    md += ["## 4. 대본 (번호 = 대본 문장 번호, 🎙 = 읽는 목소리)", "", script_block(txt, roles) if txt.exists() else "(없음)", ""]
    md += ["## 5. 검산·출처", "", "사연 검산표와 모든 숫자의 출처: [`README.md`](README.md)", ""]
    path = src / "summary.md"
    path.write_text("\n".join(md), "utf-8")
    print(f"[SUMMARY] [{dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}] video={vid} "
          f"file={path.relative_to(ROOT)} sentences={len(sents)} subtitles={len(subs)} episode_code={'있음' if has_code else '없음'} "
          f"thumb_images={len(imgs)} audio={'있음' if audio else '없음'} youtube={'있음' if yt else '없음'}")
    return path


def on_hold(topic):
    """주제 README 앞부분에 '⏸ … 보류'가 있으면 보류 주제 (사용자 지시 2026-10-10, tts_narration.topic_on_hold 와 같은 규칙)."""
    p = ROOT / topic / "README.md"
    head = p.read_text("utf-8").splitlines()[:30] if p.exists() else []
    return any("⏸" in ln and "보류" in ln for ln in head)


def thumb_todo(topic):
    """이미지가 아직 없는 썸네일의 [A] 프롬프트와 저장 경로를 한 파일에 모은다 (이미지 AI에 차례로 넣기 좋게)."""
    items = []
    for md_path in sorted((ROOT / topic / "source").glob("*/thumbnails/thumbnail_*.md")):
        folder, n = md_path.parent, md_path.stem.split("_")[-1]
        if any((folder / f"thumbnail_{n}{e}").exists() for e in IMG_EXTS):
            continue
        md = md_path.read_text("utf-8")
        a = re.search(r"## \[A\][^\n]*\n```\n(.*?)\n```", md, re.S)
        b = re.search(r"## \[B\][^\n]*\n```\n(.*?)\n```", md, re.S)
        words = re.search(r"## 문구[^\n]*\n(.*?)(?=\n## )", md, re.S)
        vid = folder.parent.name
        items.append((vid, n, md.splitlines()[0].lstrip("# ").strip(), a, b, words))
    out = [f"# {topic} 썸네일 만들 목록 (이미지 없는 것)", "",
           f"자동 생성 — `python tools/make_summary.py --thumb-todo {topic}` ({dt.datetime.now().strftime('%Y-%m-%d %H:%M')})",
           "", "1. [A] 프롬프트를 이미지 AI에 넣는다. 한글이 틀리면 [B]로 만들고 문구표대로 글자를 얹는다.",
           "2. 이미지를 아래 '저장 위치'로 GitHub에 올린다 (크기는 업로드 때 1280×720으로 자동 변환).", "",
           f"남은 썸네일: {len(items)}개", ""]
    for vid, n, head, a, b, words in items:
        out += [f"## {vid} · thumbnail_{n} — {head.split('—')[-1].strip()}", "",
                f"저장 위치: `{topic}/source/{vid}/thumbnails/thumbnail_{n}.png`", ""]
        if words:
            out += [words.group(1).strip(), ""]
        if a:
            out += ["[A] 완성형 프롬프트", "", "```", a.group(1), "```", ""]
        if b:
            out += ["<details><summary>[B] 글자 없는 프롬프트</summary>", "", "```", b.group(1), "```", "</details>", ""]
    path = ROOT / topic / "thumbnail_todo.md"
    path.write_text("\n".join(out), "utf-8")
    print(f"[THUMB-TODO] topic={topic} remaining={len(items)} file={path.relative_to(ROOT)}")


def main(argv=None):
    ap = argparse.ArgumentParser(description="영상별 한눈에 보기 문서(summary.md) 만들기")
    ap.add_argument("topic", nargs="?")
    ap.add_argument("video_id", nargs="?")
    ap.add_argument("--all", action="store_true", help="upload.md가 있는 모든 영상 (보류 주제 제외)")
    ap.add_argument("--thumb-todo", metavar="주제폴더", help="이미지가 없는 썸네일 프롬프트 모음 만들기")
    a = ap.parse_args(argv)
    if a.thumb_todo:
        thumb_todo(a.thumb_todo)
    elif a.all:
        for up in sorted(ROOT.glob("*/source/*/upload.md")):
            if on_hold(up.parts[-4]):
                print(f"[SUMMARY] skip video={up.parts[-2]} reason=주제_보류(⏸ README)")
                continue
            build(up.parts[-4], up.parts[-2])
    elif a.topic and a.video_id:
        build(a.topic, a.video_id)
    else:
        ap.error("주제 폴더와 영상 ID, 또는 --all")


if __name__ == "__main__":
    main()
