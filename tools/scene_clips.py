#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.2 — 2026-10-19 — ChatGPT GitHub 앱이 약 768KB 를 넘는 파일을 잘라 올림 (썸네일 PNG 4장이 786,444바이트에서 깨짐): 규칙 8 =
#          JPEG(.jpg) 700KB 이하로 바꿔 올리고 올린 크기 확인 · 그림 확장자 기본 .jpg · check 가 끝까지 읽히는지 확인 (깨진 그림 = 문제).
# 이전 v1.1 — 2026-10-19 — ChatGPT 가 GitHub 에 바로 올림 (사용자 지시 "chatgpt 깃허브 업로드 가능하다고 다시 수정해서 알려주고"): 규칙 8 =
#          장마다 저장 경로에 커밋(대화에 붙이기는 실패한 장만) · 그림 확장자 = 올린 그대로 .png (plan image_ext) — videogen.json·check·add-image.
# 이전 v1.0 — 2026-10-19 — 사용자 지시 "영상은 설명이 복잡하고 어려울 때는 클로드 코드로 렌더링 하고 그렇지 않은 부분은
#          친숙한 애니메이션 이미지 생성 프롬프트와 그걸 기반으로 짧은 영상 만들어주는 프롬프트 각각 생성해서 영상 만드는걸로
#          하자 롱폼,숏폼 둘다 아까 짧게 짧게 시작이미지로 영상 만들었던 코드로 만들거니까 … 영상을 이어 붙이는건 … 너가 하는거야":
#          장면 계획 하나(scenes/plan.json)에서 ① ChatGPT 그림 프롬프트 파일 ② Kaggle videogen 설정 ③ 사람이 보는 계획 표를
#          만들고, 그림·클립을 점검하고, GitHub Release 의 클립을 받는다. 이어 붙이기·자막은 tools/assemble_video.py.
r"""
  python3 tools/scene_clips.py build economic gungmin-sigi-2026-10 [--shorts]     # plan.json → chatgpt.md · videogen.json · plan.md
  python3 tools/scene_clips.py check economic gungmin-sigi-2026-10 [--shorts]     # 문장 범위·장 시작·길이 · 있는 그림·클립
  python3 tools/scene_clips.py add-image economic gungmin-sigi-2026-10 L01 그림.png [--shorts]   # 대화에 붙인 그림 → scenes/L01.jpg
  python3 tools/scene_clips.py fetch economic gungmin-sigi-2026-10 [--shorts]     # Release → <주제>/out/<영상ID>/clips/ (sha256 확인)

장면 계획 (scenes/plan.json — 사람이 고치는 파일):
  clips[] = {name, sentences:[처음, 끝], chars:[인물 id], place, ko(한 줄 요약), image(그림 프롬프트, 영어), motion(움직임, 영어)}
  inherit = 다른 plan.json 경로 (쇼츠가 롱폼의 그림체·인물·장소를 그대로 씀)
시각: 영상 장면 파일의 EP(오디오에 맞춘 것) > tts_narration.json(TTS 가 붙인 시각) > EP(추정). 클립 하나가 덮는 구간 =
  첫 문장 시작 - lead ~ 다음 문장 시작 - lead (다음 문장이 장 시작이면 장 카드가 뜨는 1초 전까지). 장 시작 문장은 AI 클립 금지
  (장 카드는 코드 화면). 클립 길이 = 구간 + margin_sec (최대 max_sec — 5B 한 번 121프레임 = 5.04초).
로그: [STAGE] [시각] key=value …   ※ 연구·교육용 영상 제작 도구 (투자 권유 아님)
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO = "yeomin1024/yeomin1024-ytb"
VERSION = "v1.2"
# 생성 해상도(5B 는 32 배수) · 최종 해상도 · 비율 — videogen v1.4.0 은 가운데를 잘라 생성 해상도에 맞춤
SIZES = {"landscape": dict(gen=(1280, 704), final=(1920, 1080), ratio="16:9", chatgpt="1536×864"),
         "portrait": dict(gen=(704, 1280), final=(1080, 1920), ratio="9:16", chatgpt="864×1536")}
MODEL = "wan2.2-5b-fast"
MODEL_FPS = 24
MODEL_MAX_FRAMES = 121                       # FastWan 5B 한 번 (24fps 5.04초) — 넘으면 창 이어붙이기(느림)
MAX_SLOW = 1.35                              # 합칠 때 클립을 늦추는 한도 (넘으면 마지막 장면을 멈춤) — assemble_video 와 같음
CARD_LEAD = 1.0                              # kit.js K.chapters: 장 카드는 그 장 첫 문장 1초 전부터
# FastWan(CFG 없음)에서는 쓰이지 않지만 CFG 모델로 바꿀 때를 위해: Wan 기본 부정 프롬프트에서 '风格·作品·画作·画面'(그림체를
# 사진 쪽으로 미는 말)을 빼고 글자·워터마크·얼굴 변형·사진풍을 더함
NEGATIVE = ("色调艳丽，过曝，静态，细节模糊不清，字幕，文字，水印，整体发灰，最差质量，低质量，JPEG压缩残留，丑陋的，残缺的，"
            "多余的手指，画得不好的手部，画得不好的脸部，畸形的，毁容的，形态畸形的肢体，手指融合，静止不动的画面，杂乱的背景，"
            "三条腿，背景人很多，倒着走，人脸变形，照片写实")


def log(stage: str, msg: str = "", **kv):
    parts = " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) and (' ' in v or not v) else v}"
                     for k, v in kv.items())
    print(f"[{stage}] [{time.strftime('%Y-%m-%dT%H:%M:%S')}] {msg} {parts}".rstrip(), flush=True)


# --------------------------------------------------------------------------------------------------
def paths(topic: str, vid: str, shorts: bool) -> dict:
    folder = ROOT / topic / "source" / vid
    base = folder / "shorts" if shorts else folder
    ep_id = f"{vid}-shorts" if shorts else vid
    return dict(folder=folder, scenes=base / "scenes", plan=base / "scenes" / "plan.json", timing=base / "tts_narration.json",
                episode=ROOT / "video" / "episodes" / ep_id / "index.html", out=ROOT / topic / "out" / ep_id, ep_id=ep_id)


def load_plan(path: Path) -> dict:
    plan = json.loads(path.read_text(encoding="utf-8"))
    if plan.get("inherit"):
        parent = json.loads((ROOT / plan["inherit"]).read_text(encoding="utf-8"))
        for k in ("style", "characters", "places"):
            plan.setdefault(k, parent.get(k))
    for k in ("video", "orientation", "release_tag", "image_dir", "clips", "style", "characters"):
        if not plan.get(k):
            raise SystemExit(f"[PLAN] {path} 에 '{k}' 가 없음")
    if plan["orientation"] not in SIZES:
        raise SystemExit(f"[PLAN] orientation={plan['orientation']!r} — landscape | portrait")
    return plan


def read_ep(html: Path) -> dict | None:
    if not html.exists():
        return None
    m = re.search(r"/\*EP-DATA:BEGIN\*/window\.EP=(.*?);/\*EP-DATA:END\*/", html.read_text(encoding="utf-8"), re.S)
    return json.loads(m.group(1)) if m else None


def load_timing(p: dict) -> tuple[list[dict], str]:
    """문장 시각 [{n, start, end, part}] 과 출처."""
    ep = read_ep(p["episode"])
    if ep and ep.get("sent") and not ep.get("estimated"):
        return ep["sent"], f"episode EP (audio-synced {ep.get('synced', '')})"
    if p["timing"].exists():
        d = json.loads(p["timing"].read_text(encoding="utf-8"))
        return [dict(n=i["n"], start=i["start"], end=i["end"], part=i["part"], text=i["text"]) for i in d["items"]], \
            f"{p['timing'].relative_to(ROOT)} (TTS)"
    if ep and ep.get("sent"):
        return ep["sent"], "episode EP (ESTIMATED — no audio yet)"
    raise SystemExit(f"[TIMING] 문장 시각이 없음: {p['episode']} · {p['timing']}")


def chapter_starts(sents: list[dict]) -> set[int]:
    return {s["n"] for i, s in enumerate(sents) if i and s["part"] != sents[i - 1]["part"]}


def windows(plan: dict, sents: list[dict]) -> list[dict]:
    """클립마다 덮는 구간 [t0, t1] · 필요한 길이 · 생성 길이(sec). 겹침·범위·장 시작은 check_plan 이 본다."""
    by_n = {s["n"]: s for s in sents}
    starts = chapter_starts(sents)
    first, lead = sents[0]["n"], plan.get("lead", 0.15)
    out = []
    for c in plan["clips"]:
        a, b = c["sentences"]
        if a not in by_n or b not in by_n:
            raise SystemExit(f"[PLAN] {c['name']} 문장 {a}~{b} 가 대본에 없음 (1~{sents[-1]['n']})")
        t0 = 0.0 if a == first else by_n[a]["start"] - lead
        nxt = by_n.get(b + 1)
        if nxt is None:
            t1 = by_n[b]["end"] + 0.3
        elif b + 1 in starts:
            t1 = nxt["start"] - CARD_LEAD
        else:
            t1 = nxt["start"] - lead
        need = round(t1 - t0, 3)
        sec = plan.get("fixed_sec") or min(plan.get("max_sec", 5.0), round(need + plan.get("margin_sec", 0.5), 2))
        frames = max(1, round(sec * MODEL_FPS)) // 4 * 4 + 1
        out.append(dict(name=c["name"], a=a, b=b, t0=round(t0, 3), t1=round(t1, 3), need=need, sec=sec, frames=frames,
                        clip_sec=round(frames / MODEL_FPS, 3), slow=round(max(1.0, need / (frames / MODEL_FPS)), 3)))
    return out


def check_plan(plan: dict, sents: list[dict], wins: list[dict]) -> list[str]:
    problems = []
    names = [c["name"] for c in plan["clips"]]
    for n in sorted({x for x in names if names.count(x) > 1}):
        problems.append(f"이름이 겹침: {n}")
    for c in plan["clips"]:
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,63}", c["name"]):
            problems.append(f"{c['name']}: 이름은 영문·숫자·_-. (파일 이름)")
        for k in ("image", "motion", "ko"):
            if not str(c.get(k, "")).strip():
                problems.append(f"{c['name']}: '{k}' 가 비어 있음")
        unknown = [x for x in c.get("chars", []) if x not in {ch["id"] for ch in plan["characters"]}]
        if unknown:
            problems.append(f"{c['name']}: 모르는 인물 {unknown}")
        if c.get("place") and c["place"] not in {pl["id"] for pl in plan.get("places") or []}:
            problems.append(f"{c['name']}: 모르는 장소 {c['place']!r}")
    starts = chapter_starts(sents)
    covered = {}
    for w in wins:
        if w["a"] > w["b"]:
            problems.append(f"{w['name']}: 문장 범위 {w['a']}~{w['b']} 거꾸로")
        for n in range(w["a"], w["b"] + 1):
            if n in covered:
                problems.append(f"문장 {n}: {covered[n]} 와 {w['name']} 가 겹침")
            covered[n] = w["name"]
            if n in starts:
                problems.append(f"{w['name']}: 문장 {n} 은 장 시작 — 장 카드는 코드 화면 (AI 클립 금지)")
        for n in plan.get("cover_sentences", []):
            if w["a"] <= n <= w["b"]:
                problems.append(f"{w['name']}: 문장 {n} 은 썸네일 그림(K.cover) 자리")
        if w["need"] <= 0:
            problems.append(f"{w['name']}: 구간 길이 {w['need']}초")
        if w["frames"] > MODEL_MAX_FRAMES:
            problems.append(f"{w['name']}: {w['frames']}프레임 > {MODEL_MAX_FRAMES} (5B 한 번 한도) — max_sec 확인")
    return problems


# --------------------------------------------------------------------------------------------------
def _people(plan: dict, ids: list[str]) -> list[dict]:
    by = {c["id"]: c for c in plan["characters"]}
    return [by[i] for i in ids if i in by]


def _place(plan: dict, pid: str | None) -> dict | None:
    return next((pl for pl in plan.get("places") or [] if pl["id"] == pid), None) if pid else None


def frame_rules(plan: dict) -> str:
    s = SIZES[plan["orientation"]]
    if plan["orientation"] == "landscape":
        return (f"Format: 16:9 landscape ({s['chatgpt']}, or the widest landscape size). Keep faces and key objects in the "
                "central area and away from the top and bottom 10% (the picture will be cropped to 16:9). Keep the bottom "
                "20% simple and calm with no faces or key objects (subtitles go there).")
    return (f"Format: 9:16 vertical ({s['chatgpt']}, or the tallest vertical size). Keep faces between 12% and 60% of the "
            "height and away from the left and right 10% (the picture will be cropped to 9:16). Keep the bottom 35% simple "
            "and calm with no faces or key objects (subtitles and the app's buttons go there).")


NO_TEXT = ("Absolutely no text, letters, numbers, symbols, logos or watermarks anywhere in the picture — papers, forms, "
           "bankbooks, calculators, screens and signs show only blank areas or abstract gray lines.")


def image_prompt(plan: dict, clip: dict) -> str:
    lines = [plan["style"]["image"], frame_rules(plan)]
    people = _people(plan, clip.get("chars", []))
    if people:
        lines.append("Characters (draw them exactly like this, same face, hair and clothes in every picture):")
        lines += [f"- {p['en']}" for p in people]
    pl = _place(plan, clip.get("place"))
    if pl:
        lines.append(f"Place: {pl['en']}")
    lines += [f"Scene: {clip['image']}", NO_TEXT]
    return "\n".join(lines)


def sheet_prompt(plan: dict) -> str:
    people = "\n".join(f"- {c['en']}" for c in plan["characters"])
    return "\n".join([plan["style"]["image"],
                      "A character reference sheet: these characters standing side by side in a row, full body, front "
                      "view, neutral friendly expressions, plain light background, evenly lit:", people,
                      "16:9 landscape. " + NO_TEXT + " Do not write names or labels."])


def motion_prompt(plan: dict, clip: dict) -> str:
    return f"{clip['motion'].rstrip()} {plan['style']['motion']}".strip()


def image_ext(plan: dict) -> str:
    """장면 그림 확장자 (v1.2 — ChatGPT 가 JPEG 700KB 이하로 바꿔 올림: GitHub 앱이 약 768KB 를 넘는 파일을 잘라 올리므로)."""
    return plan.get("image_ext", ".jpg")


def videogen_settings(plan: dict, wins: list[dict]) -> dict:
    gw, gh = SIZES[plan["orientation"]]["gen"]
    by = {w["name"]: w for w in wins}
    return dict(
        model=MODEL, width=gw, height=gh, seed=42, concat=False, upscaler="lanczos",
        prompt=plan["style"]["motion"], negative_prompt=NEGATIVE, release_tag=plan["release_tag"],
        start_images=[dict(image=f"{plan['image_dir']}/{c['name']}{image_ext(plan)}", name=c["name"], sec=by[c["name"]]["sec"],
                           prompt=motion_prompt(plan, c)) for c in plan["clips"]])


def _quote(sents: list[dict], a: int, b: int) -> str:
    by = {s["n"]: s for s in sents}
    return " ".join(by[n].get("text", "") for n in range(a, b + 1)).strip()


def chatgpt_md(plan: dict, sents: list[dict], plan_rel: str, stamp: str, shorts: bool) -> str:
    n = len(plan["clips"])
    s = SIZES[plan["orientation"]]
    vid = plan["video"]
    me = f"{plan['image_dir']}/chatgpt.md"
    out = [f"# {vid} 장면 그림 {n}장 — ChatGPT용 (읽고 1번부터 차례로 모두 만들기)", "",
           f"자동 생성 — `python3 tools/scene_clips.py build` {VERSION} ({stamp}). 이 파일은 고치지 말고 `{plan_rel}` 을 "
           "고친 뒤 다시 만든다.", "",
           f"이 파일 주소(최신): https://raw.githubusercontent.com/{REPO}/main/{me}", "",
           "쓰임: 영상에서 **사연 장면**마다 이 그림을 첫 장면으로 짧은 움직이는 클립(약 2~5초)을 만든다 (Kaggle videogen). "
           "숫자·계산 설명은 Claude 가 코드로 그린 화면이라 여기 없다.", "",
           "## ChatGPT에게 — 이 파일을 읽으면 할 일",
           "0. **이 주소를 지금 새로 열어 그 내용만 쓴다.** 답의 첫 줄에 이 파일 맨 위 '자동 생성' 줄의 시각을 그대로 적는다."
           + (" 이 파일은 같은 영상 롱폼 그림을 만든 **같은 대화에서 이어서** 만든다 (인물을 같게)." if shorts else ""),
           ("1. 먼저 **0번 인물 설정표** 한 장을 만든다 (영상에는 쓰지 않음 — 모든 장면의 얼굴·머리·옷을 맞추는 기준)."
            if not shorts else "1. 롱폼에서 만든 인물 설정표의 인물과 **똑같은 얼굴·머리·옷**으로 그린다 (설정표는 다시 만들지 않음)."),
           f"2. 그다음 **1번부터 {n}번까지 차례로 모두** 만든다. 질문하지 말고, 한 장을 만든 뒤 멈추지 말고 다음 장으로 넘어간다.",
           "   - 이미지 한도 때문에 멈추면 사용자가 `계속`이라고 보낸다 → 아직 안 만든 번호부터 이어서 만든다.",
           "3. 각 장은 그 칸의 **프롬프트(``` 안)를 그대로** 쓴다. 모든 장이 **같은 그림체·같은 인물**이다 (프롬프트마다 그림체와 그 장의 "
           "인물 설명이 들어 있음 — 장마다 다른 얼굴·옷으로 바꾸지 않는다).",
           f"4. 크기: **{s['ratio']} {'가로' if plan['orientation'] == 'landscape' else '세로'}** ({s['chatgpt']} — 안 되면 "
           f"가장 {'넓은 가로형' if plan['orientation'] == 'landscape' else '긴 세로형'}). 얼굴과 중요한 물건은 프롬프트의 "
           "'Format' 줄대로 (잘리는 가장자리·자막 자리를 피함).",
           "5. **그림 속 글자·숫자·기호·로고·워터마크는 하나도 없다.** 서류·통장·계산기·화면·간판은 빈칸이나 회색 줄만.",
           "6. 사람은 실존 인물이나 유명인을 닮지 않은 가상 인물이다. 표정·몸짓은 프롬프트에 적힌 그대로 (감정이 작은 화면에서도 보이게).",
           "7. **그림마다 바로 위에 그 장의 번호와 저장 경로를 한 줄 적는다** (예: `1. " + f"{plan['image_dir']}/"
           f"{plan['clips'][0]['name']}{image_ext(plan)}`). 그림 안에는 쓰지 않는다.",
           "8. **다 만들면 저장소에 넣는다 — 장마다 적힌 저장 경로 그대로.**",
           f"   - 저장소 `{REPO}` main 브랜치. **GitHub 앱으로 장마다 그 경로에 커밋한다** — 이 계정의 ChatGPT 는 저장소에 파일을 "
           f"올릴 수 있다 (2026-10-19 사용자 확인). 커밋 메시지 `[장면] {vid} <이름> 그림`. 파일 이름·폴더는 저장 경로와 한 글자도 다르지 "
           "않게. 다 올리면 올린 파일 경로와 커밋 링크를 목록으로 적는다 (Claude 가 그 목록으로 검수).",
           "   - **올리기 전에 JPEG(.jpg)로 바꿔 700KB 이하로 만든다** — 파이썬(PIL)으로 RGB·크기 그대로·품질 90부터 5씩 낮춰 700KB "
           "아래가 될 때까지 저장. GitHub 앱은 약 768KB 를 넘는 파일을 **잘라** 올려 그림이 깨진다 (2026-10-19 썸네일 PNG 4장이 "
           "786,444바이트에서 잘려 열리지 않음). 올린 뒤 GitHub 에 있는 그 파일의 크기(바이트)가 내 파일과 같은지 확인하고, 다르면 다시 올린다.",
           "   - **올리기가 실패한 장만** (권한·연결 오류) 묻지 말고: 그 그림을 번호 순서대로 다시 보여 주고(그림마다 위에 번호와 저장 "
           "경로), 마지막에 이 문장을 그대로 쓴다: **\"올리지 못한 그림을 이 순서대로 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 "
           "뒤 각 저장 경로에 올립니다.\"**", "",
           "## 그림체 (모든 장 공통 — 프롬프트에 이미 들어 있음)", "", plan["style"]["image"], "",
           "## 인물", ""]
    out += [f"- **{c['name']}** — {c['en']}" for c in plan["characters"]]
    if plan.get("places"):
        out += ["", "## 장소", ""] + [f"- **{p['name']}** — {p['en']}" for p in plan["places"]]
    if not shorts:
        out += ["", f"## 0. 인물 설정표 (영상에는 안 씀)", "",
                f"**저장 경로: `{plan['image_dir']}/characters{image_ext(plan)}`**", "", "```", sheet_prompt(plan), "```"]
    for i, c in enumerate(plan["clips"], 1):
        a, b = c["sentences"]
        rng = f"문장 {a}" if a == b else f"문장 {a}~{b}"
        out += ["", f"## {i}. {c['name']} — {c['ko']}", "",
                f"**저장 경로: `{plan['image_dir']}/{c['name']}{image_ext(plan)}`**", "",
                f"내레이션 ({rng}): 「{_quote(sents, a, b)}」", "", "```", image_prompt(plan, c), "```"]
    return "\n".join(out) + "\n"


def plan_md(plan: dict, sents: list[dict], wins: list[dict], src: str, stamp: str) -> str:
    by = {w["name"]: w for w in wins}
    ai = {n: w["name"] for w in wins for n in range(w["a"], w["b"] + 1)}
    starts = chapter_starts(sents)
    total = sents[-1]["end"]
    ai_sec = sum(w["need"] for w in wins)
    out = [f"# {plan['video']} 장면 계획 — AI 클립 {len(wins)}개 + 코드 화면", "",
           f"자동 생성 — `python3 tools/scene_clips.py build` {VERSION} ({stamp}) · 원본 `scenes/plan.json` · 시각 출처: {src}", "",
           f"- {plan.get('version', '')}",
           f"- AI 클립 구간 합계 {ai_sec:.1f}초 / 영상 {total:.1f}초 ({ai_sec / total * 100:.0f}%) · 생성 {SIZES[plan['orientation']]['gen'][0]}x"
           f"{SIZES[plan['orientation']]['gen'][1]} → 합칠 때 {SIZES[plan['orientation']]['final'][0]}x{SIZES[plan['orientation']]['final'][1]}",
           f"- 클립 길이 = 구간 + {plan.get('margin_sec', 0.5)}초 (최대 {plan.get('max_sec', 5.0)}초)"
           + (f" · 쇼츠는 모두 {plan['fixed_sec']}초 (오디오 전 — 남는 만큼 자름)" if plan.get("fixed_sec") else "")
           + f". 클립이 구간보다 짧으면 합칠 때 {MAX_SLOW}배까지 늦추고, 그래도 모자라면 마지막 장면을 멈춤.",
           "- 장 시작 문장(장 카드)·숫자·법·계산·정리는 코드 화면 (`video/episodes/<영상ID>/index.html`).", "",
           "| 문장 | 시작 | 화면 | 장면 | 구간(초) | 클립(초) |", "|---|---|---|---|---|---|"]
    clip_by = {c["name"]: c for c in plan["clips"]}
    for s in sents:
        n = s["n"]
        if n in ai:
            w = by[ai[n]]
            if n != w["a"]:
                continue
            rng = f"{w['a']}" if w["a"] == w["b"] else f"{w['a']}~{w['b']}"
            slow = f" (×{w['slow']:.2f} 늦춤)" if w["slow"] > 1.0 else ""
            out.append(f"| {rng} | {w['t0']:.2f} | **AI {w['name']}** | {clip_by[w['name']]['ko']} | {w['need']:.2f} | "
                       f"{w['clip_sec']:.2f}{slow} |")
        else:
            tag = " (장 시작)" if n in starts else (" (썸네일 그림)" if n in plan.get("cover_sentences", []) else "")
            out.append(f"| {n} | {s['start']:.2f} | 코드{tag} | {s.get('text', '')[:34]} | | |")
    return "\n".join(out) + "\n"


# --------------------------------------------------------------------------------------------------
def cmd_build(a) -> int:
    p = paths(a.topic, a.vid, a.shorts)
    plan = load_plan(p["plan"])
    sents, src = load_timing(p)
    wins = windows(plan, sents)
    problems = check_plan(plan, sents, wins)
    log("PLAN", "loaded", plan=str(p["plan"].relative_to(ROOT)), clips=len(wins), sentences=len(sents), timing=src)
    for pr in problems:
        log("PLAN", "PROBLEM " + pr)
    if problems:
        return 1
    stamp = time.strftime("%Y-%m-%d %H:%M")
    plan_rel = str(p["plan"].relative_to(ROOT))
    files = {p["scenes"] / "chatgpt.md": chatgpt_md(plan, sents, plan_rel, stamp, a.shorts),
             p["scenes"] / "videogen.json": json.dumps(videogen_settings(plan, wins), ensure_ascii=False, indent=2) + "\n",
             p["scenes"] / "plan.md": plan_md(plan, sents, wins, src, stamp)}
    for path, text in files.items():
        path.write_text(text, encoding="utf-8")
        log("BUILD", "wrote", file=str(path.relative_to(ROOT)), bytes=len(text.encode("utf-8")))
    for w in wins:
        log("CLIP", w["name"], sentences=f"{w['a']}-{w['b']}", t0=w["t0"], t1=w["t1"], need=w["need"], sec=w["sec"],
            frames=w["frames"], slow=w["slow"])
    slow = [w for w in wins if w["slow"] > 1.0]
    log("SUMMARY", "clips", n=len(wins), gen_sec=round(sum(w["clip_sec"] for w in wins), 1),
        ai_cover_sec=round(sum(w["need"] for w in wins), 1), slowed=len(slow),
        frozen=sum(1 for w in wins if w["slow"] > MAX_SLOW))
    return 0


def image_ok(path: Path) -> bool:
    """끝까지 읽히는 그림인지 (v1.2 — 잘려 올라간 PNG 는 열리기는 해도 load 에서 깨짐)."""
    from PIL import Image
    try:
        with Image.open(path) as im:
            im.load()
        return True
    except Exception:
        return False


def _image_file(p: dict, name: str, broken: list | None = None) -> Path | None:
    """<이름>.(jpg|png|jpeg|webp) 가운데 끝까지 읽히는 첫 파일. 깨진 파일은 broken 에 넣고 없는 것으로."""
    for ext in (".jpg", ".png", ".jpeg", ".webp"):
        f = p["scenes"] / f"{name}{ext}"
        if f.exists():
            if image_ok(f):
                return f
            if broken is not None:
                broken.append(f)
    return None


def crop_pct(w: int, h: int, orientation: str) -> float:
    tw, th = SIZES[orientation]["gen"]
    scale = max(tw / w, th / h)
    return round((1 - (tw * th) / (max(tw, round(w * scale)) * max(th, round(h * scale)))) * 100, 1)


def cmd_check(a) -> int:
    from PIL import Image
    p = paths(a.topic, a.vid, a.shorts)
    plan = load_plan(p["plan"])
    sents, src = load_timing(p)
    wins = windows(plan, sents)
    problems = check_plan(plan, sents, wins)
    have, missing, broken = 0, [], []
    for w in wins:
        f = _image_file(p, w["name"], broken)
        if not f:
            missing.append(w["name"])
            continue
        have += 1
        with Image.open(f) as im:
            cut = crop_pct(*im.size, plan["orientation"])
            log("IMAGE", w["name"], file=str(f.relative_to(ROOT)), size=f"{im.size[0]}x{im.size[1]}", cropped_pct=cut)
            if f.suffix != image_ext(plan):
                problems.append(f"{w['name']}: {f.name} — videogen.json 은 {image_ext(plan)} 를 가리킴 (add-image 로 바꾸기)")
            if cut > 20:
                problems.append(f"{w['name']}: 비율이 많이 달라 {cut}% 잘림 — {SIZES[plan['orientation']]['ratio']} 로 다시")
            if max(im.size) < 1024:
                problems.append(f"{w['name']}: 그림이 작음 {im.size}")
    for f in broken:
        problems.append(f"{f.name}: 끝까지 읽히지 않음 ({f.stat().st_size:,}바이트 — 잘려 올라감) → JPEG 700KB 이하로 다시 올리기")
    man = p["out"] / "clips" / "clips_manifest.json"
    clips = {}
    if man.exists():
        clips = {c["name"]: c for c in json.loads(man.read_text(encoding="utf-8"))["clips"]}
        for w in wins:
            c = clips.get(w["name"])
            if not c:
                continue
            d = c.get("duration_sec") or 0
            slow = w["need"] / d if d else 99
            if slow > MAX_SLOW:
                log("CLIP", "shorter than its window — last frame will be held", name=w["name"], need=w["need"],
                    clip_sec=d, hold_sec=round(w["need"] - d * MAX_SLOW, 2))
    log("SUMMARY", "check", timing=src, clips=len(wins), images=have, images_missing=len(missing),
        fetched_clips=sum(1 for w in wins if w["name"] in clips), problems=len(problems))
    if missing:
        log("SUMMARY", "images missing", names=",".join(missing))
    for pr in problems:
        log("CHECK", "PROBLEM " + pr)
    return 1 if problems else 0


def cmd_add_image(a) -> int:
    from PIL import Image
    p = paths(a.topic, a.vid, a.shorts)
    plan = load_plan(p["plan"])
    if a.name not in {c["name"] for c in plan["clips"]} and a.name != "characters":
        raise SystemExit(f"[IMAGE] {a.name} 은 계획에 없는 이름")
    src = Path(a.file)
    with Image.open(src) as im:
        im = im.convert("RGB")
        w, h = im.size
        if max(w, h) > 1920:
            k = 1920 / max(w, h)
            im = im.resize((round(w * k), round(h * k)), Image.LANCZOS)
        ext = image_ext(plan)
        dst = p["scenes"] / f"{a.name}{ext}"
        im.save(dst, **({"quality": 92, "optimize": True} if ext == ".jpg" else {"optimize": True}))
    for old in (p["scenes"] / f"{a.name}{e}" for e in (".png", ".jpg", ".jpeg", ".webp") if e != dst.suffix):
        if old.exists():
            old.unlink()
    log("IMAGE", "saved", name=a.name, src=str(src), orig=f"{w}x{h}", file=str(dst.relative_to(ROOT)),
        size=f"{im.size[0]}x{im.size[1]}", kb=round(dst.stat().st_size / 1024), cropped_pct=crop_pct(w, h, plan["orientation"]))
    return 0


def _get(url: str, tries: int = 4) -> bytes:
    err = None
    for k in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "scene_clips"}), timeout=120) as r:
                return r.read()
        except Exception as e:  # 네트워크 오류: 2·4·8초 쉬고 다시
            err = e
            log("FETCH", "retry", url=url[-90:], attempt=k + 1, error=repr(e)[:160])
            time.sleep(2 ** (k + 1))
    raise RuntimeError(f"받기 실패 {url}: {err!r} — Release 가 있는지(Kaggle 로그 [RELEASE] done) 확인")


def cmd_fetch(a) -> int:
    p = paths(a.topic, a.vid, a.shorts)
    plan = load_plan(p["plan"])
    base = f"https://github.com/{REPO}/releases/download/{plan['release_tag']}"
    t0 = time.perf_counter()
    man = json.loads(_get(f"{base}/clips_manifest.json"))
    out = p["out"] / "clips"
    out.mkdir(parents=True, exist_ok=True)
    got, bad, total = 0, [], 0
    for c in man["clips"]:
        dst = out / c["file"]
        if dst.exists() and hashlib.sha256(dst.read_bytes()).hexdigest() == c["sha256"]:
            got += 1
            continue
        data = _get(c.get("release_url") or f"{base}/{c['file']}")
        if hashlib.sha256(data).hexdigest() != c["sha256"]:
            bad.append(c["name"])
            log("FETCH", "sha256 mismatch — skipped", name=c["name"])
            continue
        dst.write_bytes(data)
        got += 1
        total += len(data)
        log("FETCH", "clip", name=c["name"], mb=round(len(data) / 1e6, 2), duration_sec=c.get("duration_sec"),
            size=f"{c.get('width')}x{c.get('height')}")
    (out / "clips_manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=2), encoding="utf-8")
    want = {c["name"] for c in plan["clips"]}
    have = {c["name"] for c in man["clips"]} - set(bad)
    log("SUMMARY", "fetch", tag=plan["release_tag"], clips=got, mb=round(total / 1e6, 1), sec=round(time.perf_counter() - t0, 1),
        missing=",".join(sorted(want - have)) or "none", extra=",".join(sorted(have - want)) or "none", bad=len(bad))
    return 1 if bad or (want - have) else 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="장면 클립 계획·프롬프트·받기 " + VERSION)
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("build", "check", "fetch", "add-image"):
        s = sub.add_parser(name)
        s.add_argument("topic")
        s.add_argument("vid")
        if name == "add-image":
            s.add_argument("name")
            s.add_argument("file")
        s.add_argument("--shorts", action="store_true")
    a = ap.parse_args(argv)
    return {"build": cmd_build, "check": cmd_check, "fetch": cmd_fetch, "add-image": cmd_add_image}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
