#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.7.1 — 2026-10-17 — SIMPLE_TEXT_RULES 예·검사 기호에 비교·수식 기호(> < = +) — 사용자 지시 2026-10-17 "<, >, =, vs, +, - 등등 비교나 간단한 수식 관련된 기호 문구도 사용하는 게 좋을 것 같아 다시 수정해봐".
# (v1.7.0 — 2026-10-17 — 글자 종류 셋: 없음 · 한글(TEXT_RULES) · **영어 낱말·숫자·기호(SIMPLE_TEXT_RULES — 주식)** — thumbnail_N.md 의 '| 글자 | **영어…' 줄로 알아봄.
#          ChatGPT 규칙 4·6 이 '한글 획'이 아니라 '철자·기호(−·%·$·×·→) 한 글자씩'을 보게. 사용자 지시 2026-10-17 "문구 없으니까 너무 허전하네 buy, sell 같은
#          정말 간단해서 모두 알만한 영어 문구는 써도 돼" · "숫자나 기호 같은 문구도 써도 돼".)
# (v1.6.0 — 2026-10-16 — 쇼츠 썸네일도: 영상ID `<영상ID>-shorts` = `<주제>/source/<영상ID>/shorts/thumbnails/` 의 thumbnail_1 하나
#          (쇼츠는 '테스트 및 비교'가 없어 한 장). --chatgpt-all 이 롱폼 다음에 쇼츠를 모으고, 장마다 크기 줄(롱폼 가로 16:9 · 쇼츠 세로 9:16)을 적음.
#          사용자 지시 2026-10-16 "쇼츠 영상 썸네일 이미지 프롬프트 만들어서 영상 처음에만 그걸 포함 시키고 … 이미지 프롬프트 4개 다 만들도록 하고".)
# (v1.5.0 — 2026-10-16 — --chatgpt-all <주제>: 그 주제 모든 영상의 남은 썸네일을 한 파일(<주제>/thumbnails_chatgpt.md)에 모아
#          ChatGPT 가 메시지 한 번으로 차례로 만들고 장마다 **저장 경로**(`<주제>/source/<영상ID>/thumbnails/thumbnail_N.png`)에 올리게 한다
#          (못 쓰면 경로를 붙여 순서대로 보여 주고 Claude 대화에 붙이게). 영상별 chatgpt.md 도 그림 위에 저장 경로를 적게 함.
#          사용자 지시 2026-10-16 "모든 썸네일은 chatgpt가 프롬프트 읽고 만들어서 맞는 경로에 업로드 해줘야하는데 뭐라고 해야하는지 알려줘 지시사항 변경 필요하면 변경하고".)
# (v1.4.4 — 2026-10-16 — chatgpt.md 규칙 4: '따옴표 안 한글만' → '따옴표 안 글자(한글, 그리고 프롬프트가 적은 영문 — 예: ISA)만'.
#          ISA 영상 썸네일 문구에 영문 'ISA'가 있어 '한글만'이라는 규칙과 어긋났음 (사용자 지시 2026-10-16 "영상 4개 완성하기 위해 뭐가 필요한지 확인하고 없으면 만들어").)
# (v1.4.3 — 2026-10-15 — 글자 없는 썸네일: thumbnail_N.md 표에 '| 글자 | 없음' 이 있으면 chatgpt.md 규칙을 '글자·숫자 하나도 없이,
#          가짜 글자가 없는지 확대해 보기'로 바꿈 (사용자 지시 2026-10-15 "주식 주제는 전세계 사람들 대상 … 썸네일도 문구 달지 말고 이미지로만").)
# (v1.4.2 — 2026-10-15 — 사용자 지시 "썸네일 chatgpt가 안올렸대잖아 올리도록 지시사항 반영해": ChatGPT 가 저장소에 못 쓰면(이 계정은 읽기만)
#          그림을 'Claude 대화에 붙여 넣으라'고 안내 → Claude 가 검수해 올린다 (기본 길). 모든 시안에 이미지가 있으면 '만들 것 없음' 파일을 쓴다)
#          (v1.4.1 — 2026-10-15 — 사용자 지시 "chatgpt가 저장소 경로에 업로드하라고": chatgpt.md 에 저장소 올리기 단계(GitHub 앱 커밋, 안 되면 업로드 링크),
#          이미 이미지가 있는 시안은 빼고 남은 것만, 한글 획 확대 확인 (1차: 입체 '건보료' 획 틀림))
#          (v1.4.0 — 2026-10-15 — 사용자 지시 "한번에 3개 다 읽어서 만들라고 하면 되잖아": --chatgpt 주제 영상ID → thumbnails/chatgpt.md
#          (ChatGPT가 주소 하나로 읽고 썸네일 3장을 차례로 만드는 지시 + 시안별 문구표·[A] 프롬프트, thumbnail_N.md 에서 만들어 어긋나지 않게))
#          (v1.3.3 — 2026-10-12 — 오디오 줄: 스튜디오에서 잘라 낸 영상(youtube.json studioTrim)은 '원본 렌더 오디오 + 스튜디오 컷'으로 표시하고
#          'Kaggle에서 다시'를 안내하지 않음, 이미 올린 영상도 다시 만들라고 하지 않음 (tts_narration 은 올린 영상을 건드리지 않음)
#          (v1.3.2: 상태표 썸네일 줄: 프롬프트 파일 개수를 실제로 셈 (없는데 '3개 ✅'로 나오던 오류))
#          (v1.3.1: 오디오 없음 안내 문구: Kaggle 셀 하나(all --push)가 대본 폴더에 올림)
#          (v1.3: 사용자 지시: 요약에서 스토리보드 빼기 (상태 줄·4번 절 삭제, 영상 코드 상태로 대체),
#          내레이션 역할(사연자·진행자, voices/*.json) 표시, 오디오가 지금 대본으로 만든 것인지(tts_narration.json) 표시
#          (v1.2: 파트 라벨 판정을 srt_tool.is_label과 같게; v1.1: 예약 공개 시각 표시; v1.0: 영상별 summary.md, --thumb-todo, 표준 라이브러리만))
r"""
영상 하나의 결과물을 한 문서로 모읍니다: 상태 → 제목 3개 → 썸네일 3개 → 업로드 정보 → 대본(파트마다 사연자·진행자 표시).
스토리보드는 넣지 않는다 (사용자 지시 2026-10-10).

  python tools/make_summary.py stock bittu-2026-10      # → stock/source/bittu-2026-10/summary.md
  python tools/make_summary.py --all                    # 모든 주제 폴더의 source/<영상ID>/ (upload.md가 있는 것)
  python tools/make_summary.py --thumb-todo stock       # 이미지가 아직 없는 썸네일의 [A] 프롬프트 모음 → stock/thumbnail_todo.md
  python tools/make_summary.py --chatgpt economic eunte-kkeonaeseugi-2026-10   # ChatGPT가 읽고 3장을 만드는 파일 → source/<영상ID>/thumbnails/chatgpt.md
  python tools/make_summary.py --chatgpt-all economic   # (v1.5.0) 그 주제 모든 영상의 남은 썸네일 → <주제>/thumbnails_chatgpt.md (메시지 한 번, 장마다 저장 경로)

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
SHORTS = "-shorts"                                              # v1.6.0 쇼츠 영상ID 끝


def thumb_folder(topic, vid, root=None):
    """롱폼 → source/<영상ID>/thumbnails · 쇼츠(<영상ID>-shorts) → source/<영상ID>/shorts/thumbnails (v1.6.0)."""
    root = root or ROOT
    if vid.endswith(SHORTS):
        return root / topic / "source" / vid[: -len(SHORTS)] / "shorts" / "thumbnails"
    return root / topic / "source" / vid / "thumbnails"


def thumb_slots(vid):
    """시안 번호: 롱폼 1~3 (본안 + 실험안 2 — 스튜디오 '테스트 및 비교') · 쇼츠 1 (쇼츠는 비교 시험이 없음)."""
    return (1,) if vid.endswith(SHORTS) else (1, 2, 3)


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
        trim = (yt or {}).get("studioTrim")
        if diff and trim:   # 올린 영상을 스튜디오에서 잘라 냄 → 대본·SRT 는 잘라 낸 영상 기준, 오디오는 원본 렌더 기록
            audio_note = (f" · 원본 렌더 오디오 (사연 문장 {len(trim.get('dropSentences', []))}개를 스튜디오 컷으로 뺌 — "
                          f"`studio_trim.md`, 다시 만들지 않음)")
        elif diff and yt:
            audio_note = f" · ⚠️ 대본이 올린 영상과 다름 (바뀐 문장 {diff[0]}번 등 {len(diff)}개) — 올린 영상은 오디오를 다시 만들지 않음"
        else:
            audio_note = " · 지금 대본과 같음" if not diff else f" · ⚠️ 옛 대본으로 만든 오디오 (바뀐 문장 {diff[0]}번 등 {len(diff)}개) → Kaggle에서 다시"
    else:
        audio_note = " · 대본과 같은지 정보 없음(직접 녹음)" if audio else ""
    has_code = (ROOT / "video" / "src" / "episodes" / vid).is_dir()
    imgs = [i for i in (1, 2, 3) if any((src / "thumbnails" / f"thumbnail_{i}{e}").exists() for e in IMG_EXTS)]
    prompts = [i for i in (1, 2, 3) if (src / "thumbnails" / f"thumbnail_{i}.md").exists()]
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
        ("썸네일", (f"프롬프트 3개 ✅ · 이미지 {len(imgs)}/3" + (" (이미지 AI로 만들어 `thumbnails/thumbnail_N.png`에 저장)" if len(imgs) < 3 else ""))
         if len(prompts) == 3 else f"❌ 프롬프트 {len(prompts)}/3 (`thumbnails/thumbnail_N.md`)"),
        ("업로드 시트", "✅ 설명란·태그·고정 댓글·챕터" if upload_md else "❌ 없음"),
        ("내레이션 역할", (role_ranges(txt, roles) + " (`voices/*.json`)") if roles and txt.exists() else "voices/ 없음"),
        ("오디오", f"✅ {audio.name}{audio_note}" if audio else
         f"⏳ 없음 → Kaggle 셀 하나(`tts_narration.py all --push`)가 `source/{vid}/narration.mp3`로 올리면 영상 제작 시작"),
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


REPO = "yeomin1024/yeomin1024-ytb"
RAW_BASE = f"https://raw.githubusercontent.com/{REPO}/main"   # 공개 저장소 — ChatGPT가 이 주소로 파일을 연다
UPLOAD_BASE = f"https://github.com/{REPO}/upload/main"        # GitHub 웹 '파일 올리기' 화면 (폴더 지정)

CHATGPT_RULES = """## ChatGPT에게 — 이 파일을 읽으면 할 일
1. 아래 썸네일 {n}개({names})를 **차례로 모두** 만든다. 질문하지 말고, 한 장을 만든 뒤 멈추지 말고 다음 장으로 넘어간다.
2. 각 장은 그 칸의 **프롬프트(``` 안)를 한 글자도 바꾸지 않고 그대로** 쓴다. 장마다 서로 다른 그림이다 — 앞 장의 인물·구도·색을 이어 쓰지 않는다.
{rule3}{rule4}5. 사람은 실존 인물이나 유명인을 닮지 않은 가상 인물이다.
{rule6}7. 그림마다 바로 위에 그 장의 저장 경로 `{folder}/thumbnail_N.png`를 한 줄 적어 어느 시안인지 알려 준다 (그림 안에는 쓰지 않는다).
8. **다 만들면 저장소에 넣는다.**
   - 올릴 곳: 저장소 `{repo}` main 브랜치의 `{folder}/` 폴더, 파일 이름 `thumbnail_N.png` (N = 시안 번호).
   - GitHub 에 쓸 수 있으면(쓰기 권한이 있는 GitHub 앱) 그 폴더에 커밋한다. 커밋 메시지: `[썸네일] {vid} thumbnail_N 이미지`
   - **쓸 수 없으면 (이 계정의 ChatGPT 는 GitHub 를 읽기만 함 — 2026-10-15 확인)** 묻지 말고 아래처럼 끝낸다:
     1. 만든 그림을 thumbnail 번호 순서로 다시 한 번씩 보여 준다 (그림마다 위에 저장 경로 `{folder}/thumbnail_N.png`).
     2. 마지막에 이 문장을 그대로 쓴다: **"이 그림 {n}장을 Claude 대화창에 그대로 붙여 넣어 주세요. Claude가 검수한 뒤 저장소({folder}/thumbnail_N)에 올립니다."**
     3. 그 아래 줄에 직접 올리는 길도 적는다: "직접 올리려면: 그림을 thumbnail_N.png 이름으로 내려받아 {upload} 에 끌어다 놓고 Commit changes"
"""


SIZE_WIDE = "3. 크기는 가로형 16:9 (1280×720). 16:9가 안 되면 가장 넓은 가로형으로 만들고, 글자와 얼굴은 가운데에 두고 위아래 가장자리 8%는 비운다.\n"
SIZE_TALL = ("3. 크기는 **세로형 9:16 (1080×1920)** — 쇼츠 썸네일이자 쇼츠 첫 화면이다. 9:16이 안 되면 세로 2:3으로 만들고(가운데를 9:16으로 잘라 씀), "
             "글자와 얼굴은 가운데에 두고 양옆 가장자리 8%는 비운다.\n")
SIZE_MIXED = ("3. 크기는 **장마다 '크기' 줄대로**: 롱폼 썸네일 = 가로형 16:9 (1280×720 — 안 되면 가장 넓은 가로형, 글자와 얼굴은 가운데, 위아래 8% 비움) · "
              "**쇼츠 썸네일(영상 ID 끝이 `-shorts`) = 세로형 9:16 (1080×1920)** — 안 되면 세로 2:3, 글자와 얼굴은 가운데, 양옆 8% 비움.\n")


def size_rule(vids):
    """v1.6.0 규칙 3: 롱폼만 = 가로, 쇼츠만 = 세로, 섞이면 장마다 '크기' 줄."""
    kinds = {v.endswith(SHORTS) for v in vids}
    return SIZE_MIXED if len(kinds) > 1 else (SIZE_TALL if kinds == {True} else SIZE_WIDE)


TEXT_RULES = ("4. 그림 속 글자는 프롬프트의 따옴표 안 글자만(한글, 그리고 프롬프트가 적은 영문 — 예: ISA), 글자·띄어쓰기 그대로 쓴다. 다른 글자·숫자·로고·워터마크는 넣지 않는다.\n",
              "6. 한 장을 만들 때마다 그 칸의 '문구' 표와 그림 속 한글을 한 글자씩 맞춰 본다. 크게 확대해서 받침과 모음 획(예: '료'의 ㄹ, '보'의 ㅗ)이 빠지거나 가려지지 않았는지도 본다. 다르면 그림은 그대로 두고 글자만 고쳐 다시 만든다.\n")
SIMPLE_TEXT_RULES = ("4. 그림 속 글자는 프롬프트가 따옴표로 적은 **영어 낱말·숫자·기호·티커만** (예: BUY, TAX, QQQ, −15%, $100,000, 1×, →, ?, 그리고 비교·수식 기호 >, <, =, +, vs) — 철자·기호·띄어쓰기 그대로, 납작하고 굵은 글씨. "
                     "다른 글자·숫자·로고·워터마크는 넣지 않는다 (동전·상자·화면에도). 한국어·문장은 쓰지 않는다 (전 세계 시청자용).\n",
                     "6. 한 장을 만들 때마다 그 칸의 '문구' 표와 그림 속 글자를 **한 글자씩** 맞춰 본다 — 마이너스 '−'·'%'·'$'·쉼표·소수점·'×'·'→'·'>'·'<'·'='·'+'·'?' 가 빠지거나 바뀌거나 방향이 뒤집히지 않았는지(특히 '>' 와 '<'), "
                     "표에 없는 가짜 글자·숫자가 생기지 않았는지 크게 확대해서 본다. 다르면 그림은 그대로 두고 글자만 고쳐 다시 만든다.\n")
NO_TEXT_RULES = ("4. **그림 속에 글자·숫자·기호·로고·워터마크를 하나도 넣지 않는다** — 전 세계 시청자용이라 그림만으로 뜻을 전한다. 지폐·화면·간판·그래프 눈금에도 글자나 숫자가 없어야 한다.\n",
                 "6. 한 장을 만들 때마다 그림을 크게 확대해 **글자처럼 보이는 것**(가짜 글자, 숫자, 지폐 무늬 속 숫자, 화면 속 글)이 없는지 본다. 있으면 그 부분만 지운 그림으로 다시 만든다.\n")


def text_mode(md):
    """v1.7.0: thumbnail_N.md '| 글자 |' 줄 → 'none'(글자 없음 — v1.4.3) · 'simple'(영어 낱말·숫자·기호 — 주식 2026-10-17) · 'ko'(한글 문구)."""
    m = re.search(r"^\|\s*글자\s*\|\s*\**\s*(\S+)", md, re.M)
    if m and m.group(1).startswith("없음"):
        return "none"
    if m and m.group(1).startswith("영어"):
        return "simple"
    return "ko"


def rules_for(modes):
    """v1.7.0: 모두 없음 → NO_TEXT · 한글이 하나도 없고 영어가 있음 → SIMPLE_TEXT · 그 밖 → TEXT(한글)."""
    modes = set(modes)
    if modes == {"none"}:
        return NO_TEXT_RULES
    if "ko" not in modes:
        return SIMPLE_TEXT_RULES
    return TEXT_RULES


def pending_thumbnails(topic, vid, root=ROOT):
    """이미지가 아직 없는 시안 → [(번호, 제목 줄, [A] 프롬프트, 문구표, 글자 없음)] (thumbnail_N.md 가 있는 것만)."""
    folder = thumb_folder(topic, vid, root)
    items = []
    for i in thumb_slots(vid):
        md_path = folder / f"thumbnail_{i}.md"
        if not md_path.exists():
            print(f"[CHATGPT] level=warn missing={md_path.relative_to(root)}")
            continue
        img = next((p for p in (folder / f"thumbnail_{i}{e}" for e in IMG_EXTS) if p.exists()), None)
        if img:   # 이미 만든 시안은 빼고 남은 것만 ChatGPT에 맡긴다
            print(f"[CHATGPT] skip=thumbnail_{i} reason=이미지_있음 file={img.name}")
            continue
        md = md_path.read_text("utf-8")
        a = re.search(r"## \[A\][^\n]*\n```\n(.*?)\n```", md, re.S)
        words = re.search(r"## 문구[^\n]*\n(.*?)(?=\n## )", md, re.S)
        if not a:
            raise SystemExit(f"[CHATGPT] level=error file={md_path.name} reason=[A] 프롬프트 칸 없음 — '## [A] …' 아래 ``` 블록 필요")
        mode = text_mode(md)                                                                # v1.7.0 없음·한글·영어(숫자·기호)
        items.append((i, md.splitlines()[0].lstrip("# ").strip(), a.group(1), "" if mode == "none" else (words.group(1).strip() if words else ""), mode))
    return items


def chatgpt_file(topic, vid, root=ROOT):
    """thumbnail_1~3.md 의 문구표·[A] 프롬프트를 모아 ChatGPT가 주소 하나로 읽고 3장을 만드는 파일을 쓴다 (원본은 고치지 않음)."""
    folder = thumb_folder(topic, vid, root)
    items = pending_thumbnails(topic, vid, root)
    rel = folder.relative_to(root).as_posix()
    if not items:
        if not any((folder / f"thumbnail_{i}.md").exists() for i in thumb_slots(vid)):
            raise SystemExit(f"[CHATGPT] level=error folder={rel} reason=thumbnail_N.md 없음 — 프롬프트 파일을 먼저 (guides/thumbnail_guide.md 8번)")
        done = folder / "chatgpt.md"   # 모든 시안에 이미지가 있다 → 예전 지시가 남지 않게 '만들 것 없음'으로 바꿔 둔다
        done.write_text(f"# {vid} 썸네일 — ChatGPT용\n\n모든 썸네일 이미지가 저장소에 있다 ({rel}/thumbnail_{'1' if vid.endswith(SHORTS) else '1~3'}). **만들 것 없음.**\n\n"
                        f"이 파일을 읽은 AI는 그림을 만들지 말고 '만들 썸네일이 없습니다'라고만 답한다.\n\n"
                        f"자동 생성 — `python tools/make_summary.py --chatgpt {topic} {vid}` ({dt.datetime.now().strftime('%Y-%m-%d %H:%M')})\n", "utf-8")
        print(f"[CHATGPT] topic={topic} video={vid} thumbnails=0 note=모든_시안에_이미지_있음 file={done.relative_to(root)}")
        return done
    out = [f"# {vid} 썸네일 {len(items)}장 — ChatGPT용 (읽고 그대로 만들고 저장소에 올리기)", "",
           f"자동 생성 — `python tools/make_summary.py --chatgpt {topic} {vid}` ({dt.datetime.now().strftime('%Y-%m-%d %H:%M')}). "
           f"이 파일은 고치지 말고 `thumbnail_N.md`를 고친 뒤 다시 만든다.", "",
           f"이 파일 주소: {RAW_BASE}/{rel}/chatgpt.md", "",
           CHATGPT_RULES.format(n=len(items), names=", ".join(f"thumbnail_{i}" for i, *_ in items), repo=REPO,
                                folder=rel, vid=vid, upload=f"{UPLOAD_BASE}/{rel}", rule3=size_rule([vid]),
                                rule4=rules_for(x[4] for x in items)[0],
                                rule6=rules_for(x[4] for x in items)[1])]
    for i, head, prompt, words, _mode in items:
        out += [f"## thumbnail_{i} — {head.split('—', 1)[-1].strip()}", ""]
        if words:
            out += ["문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):", "", words, ""]
        out += ["프롬프트:", "", "```", prompt, "```", ""]
    path = folder / "chatgpt.md"
    path.write_text("\n".join(out), "utf-8")
    print(f"[CHATGPT] topic={topic} video={vid} thumbnails={len(items)} file={path.relative_to(root)} url={RAW_BASE}/{rel}/chatgpt.md")
    return path


CHATGPT_ALL_RULES = """## ChatGPT에게 — 이 파일을 읽으면 할 일
1. 아래 썸네일 {n}장({videos}개 영상)을 **1번부터 차례로 모두** 만든다. 질문하지 말고, 한 장을 만든 뒤 멈추지 말고 다음 장으로 넘어간다.
   - 이미지 한도 때문에 멈추면 사용자가 `계속`이라고 보낸다 → 아직 안 만든 번호부터 이어서 만든다.
2. 각 장은 그 칸의 **프롬프트(``` 안)를 한 글자도 바꾸지 않고 그대로** 쓴다. 장마다 서로 다른 그림이다 — 앞 장의 인물·구도·색을 이어 쓰지 않는다.
{rule3}{rule4}5. 사람은 실존 인물이나 유명인을 닮지 않은 가상 인물이다.
{rule6}7. **그림마다 바로 위에 그 장의 번호와 저장 경로를 한 줄 적는다** (예: `3. {example}`). 그림 안에는 쓰지 않는다.
8. **다 만들면 저장소에 넣는다 — 장마다 적힌 저장 경로 그대로.**
   - 저장소 `{repo}` main 브랜치. 파일 이름·폴더는 그 장의 '저장 경로'와 한 글자도 다르지 않게 (`thumbnail_N.png`).
   - GitHub 에 쓸 수 있으면(쓰기 권한이 있는 GitHub 앱) 장마다 그 경로에 커밋한다. 커밋 메시지: `[썸네일] <영상ID> thumbnail_N 이미지`
   - **쓸 수 없으면 (이 계정의 ChatGPT 는 GitHub 를 읽기만 함 — 2026-10-15 확인)** 묻지 말고 아래처럼 끝낸다:
     1. 만든 그림을 이 파일의 번호 순서(1번부터)대로 다시 한 번씩 보여 준다 (그림마다 위에 번호와 저장 경로).
     2. 마지막에 이 문장을 그대로 쓴다: **"이 그림 {n}장을 이 순서대로 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 각 저장 경로에 올립니다."**
     3. 그 아래에 직접 올리는 길도 적는다: "직접 올리려면: 그림을 thumbnail_N.png 이름으로 내려받아 폴더마다 아래 링크에 끌어다 놓고 Commit changes" + 아래 '폴더별 올리기 링크' 목록
"""


def chatgpt_all(topic, root=ROOT):
    """v1.5.0: 주제의 모든 영상에서 이미지가 없는 시안을 모아 <주제>/thumbnails_chatgpt.md 하나로 (영상 ID 순 → 시안 번호 순).
    ChatGPT 는 메시지 한 번으로 차례로 만들고 장마다 저장 경로에 올린다 (못 쓰면 경로를 붙여 보여 주고 Claude 대화에 붙이게)."""
    groups = []
    src = root / topic / "source"
    found = [(f.parent.name, f) for f in src.glob("*/thumbnails")] + [(f.parent.parent.name + SHORTS, f) for f in src.glob("*/shorts/thumbnails")]
    for vid, folder in sorted(found, key=lambda x: (x[0].endswith(SHORTS), x[0])):   # v1.6.0 롱폼 먼저, 그다음 쇼츠
        if not any((folder / f"thumbnail_{i}.md").exists() for i in thumb_slots(vid)):
            continue
        items = pending_thumbnails(topic, vid, root)
        if items:
            groups.append((vid, folder.relative_to(root).as_posix(), items))
    path = root / topic / "thumbnails_chatgpt.md"
    stamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    gen = f"자동 생성 — `python tools/make_summary.py --chatgpt-all {topic}` ({stamp})"
    if not groups:
        path.write_text(f"# {topic} 썸네일 — ChatGPT용 (모든 영상)\n\n모든 썸네일 이미지가 저장소에 있다. **만들 것 없음.**\n\n"
                        f"이 파일을 읽은 AI는 그림을 만들지 말고 '만들 썸네일이 없습니다'라고만 답한다.\n\n{gen}\n", "utf-8")
        print(f"[CHATGPT-ALL] topic={topic} thumbnails=0 note=모든_시안에_이미지_있음 file={path.relative_to(root)}")
        return path
    flat = [(vid, rel, it) for vid, rel, items in groups for it in items]
    rules = rules_for(it[4] for _, _, it in flat)
    first_vid, first_rel, first_it = flat[min(2, len(flat) - 1)]
    out = [f"# {topic} 썸네일 {len(flat)}장 — ChatGPT용 (모든 영상 · 읽고 그대로 만들고 각 저장 경로에 올리기)", "",
           f"{gen}. 이 파일은 고치지 말고 영상마다 `thumbnail_N.md`를 고친 뒤 다시 만든다.", "",
           f"이 파일 주소: {RAW_BASE}/{topic}/thumbnails_chatgpt.md", "",
           "| 영상 | 만들 시안 | 저장 폴더 |", "|---|---|---|"]
    out += [f"| {vid} | {', '.join(f'thumbnail_{it[0]}' for it in items)} | `{rel}/` |" for vid, rel, items in groups]
    out += ["", CHATGPT_ALL_RULES.format(n=len(flat), videos=len(groups), repo=REPO, example=f"{first_rel}/thumbnail_{first_it[0]}.png",
                                          rule3=size_rule([g[0] for g in groups]), rule4=rules[0], rule6=rules[1]),
            "## 폴더별 올리기 링크 (ChatGPT가 못 올릴 때 사람이 쓰는 길)", ""]
    out += [f"- {vid}: {UPLOAD_BASE}/{rel}" for vid, rel, _ in groups]
    out.append("")
    for k, (vid, rel, (i, head, prompt, words, _mode)) in enumerate(flat, 1):
        out += [f"## {k}. {vid} · thumbnail_{i} — {head.split('—', 1)[-1].strip()}", "",
                f"**저장 경로: `{rel}/thumbnail_{i}.png`**", "",
                "크기: **세로 9:16 (1080×1920) — 쇼츠**" if vid.endswith(SHORTS) else "크기: 가로 16:9 (1280×720) — 롱폼", ""]
        if words:
            out += ["문구 (그림 속 글자는 이것과 한 글자도 다르면 안 됨):", "", words, ""]
        out += ["프롬프트:", "", "```", prompt, "```", ""]
    path.write_text("\n".join(out), "utf-8")
    print(f"[CHATGPT-ALL] topic={topic} videos={len(groups)} thumbnails={len(flat)} file={path.relative_to(root)} url={RAW_BASE}/{topic}/thumbnails_chatgpt.md")
    return path


def main(argv=None):
    ap = argparse.ArgumentParser(description="영상별 한눈에 보기 문서(summary.md) 만들기")
    ap.add_argument("topic", nargs="?")
    ap.add_argument("video_id", nargs="?")
    ap.add_argument("--all", action="store_true", help="upload.md가 있는 모든 영상 (보류 주제 제외)")
    ap.add_argument("--thumb-todo", metavar="주제폴더", help="이미지가 없는 썸네일 프롬프트 모음 만들기")
    ap.add_argument("--chatgpt", nargs=2, metavar=("주제폴더", "영상ID"), help="ChatGPT가 읽고 썸네일 3장을 만드는 thumbnails/chatgpt.md 만들기")
    ap.add_argument("--chatgpt-all", metavar="주제폴더", help="(v1.5.0) 그 주제 모든 영상의 남은 썸네일 → <주제>/thumbnails_chatgpt.md")
    a = ap.parse_args(argv)
    if a.chatgpt_all:
        chatgpt_all(a.chatgpt_all)
    elif a.chatgpt:
        chatgpt_file(*a.chatgpt)
    elif a.thumb_todo:
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
