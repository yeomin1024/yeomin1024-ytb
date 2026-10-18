#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-10-18 — 외국 영상 승인 뒤: 갈래 2개를 맨 앞에 더함 — '공식 음원(가수·레이블)'(채널 이름이 VEVO·'- Topic' 이거나 제목에
#          Official Video·Lyric Video·Video Oficial·Video Song 등 — 레이블 채널은 구독자 수가 작게 잡혀 작은 채널 성공처럼 보임)·'기존 곡 리믹스'
#          (제목에 slowed·reverb·mashup·lofi version·sped up·8D — 인도·동남아 히트곡을 늦추거나 섞은 것). 둘 다 묶음 '기존 곡' (사용자 방식으로 못 만듦).
#          v1.0 은 이것들이 설명란의 ©·AI 글자로 '만든 곡'에 섞였음 (외국 성공 사례 상위 40개 중 20개 넘게)
# (v1.0 — 2026-10-16 — 신규: 음악 성공 사례의 '곡 출처'(직접·AI로 만든 곡 / 기존 곡 모음 / 커버) 나누기
#          (사용자 지시 2026-10-16 "외국 영상도 포함하고 플레이리스트니까 짧은 영상을 포함안해야하는게 맞어 어떤 음악 영상 올려야 하는지 알려줘봐").
#          사용자 채널 = 작곡 AI 로 만든 곡의 플레이리스트 → 성공 사례 중 '따라 할 수 있는 것'(남의 곡을 모으지 않은 것)만 따로 보려고.
#          분석 도구(tools/success_analysis.py)는 그대로 두고, 그 결과(analysis.json 의 성공 사례)와 사례 폴더 설명란만 읽는 읽기 도구 (할당량 0).)
# ※ 연구·교육용 분석. 저작권·수익 정책 판단은 YouTube 공식 도움말로 따로 확인한다.
"""성공 사례의 곡 출처 나누기 — 설명란·제목 낱말 규칙 (거칠다: 표본을 눈으로 확인하고 쓸 것).

  python3 tools/song_source.py music            # → music/result/outliers/song_source.csv · song_source.md · song_source_thumbs.jpg

갈래 (위에서부터 먼저 맞는 것):
  공식 음원        — (v1.1) 채널 이름이 …VEVO·'… - Topic' 이거나 제목에 Official Video·Official Music Video·Lyric Video·Video Oficial·Video Song·Full Video·Official Audio
  기존 곡 리믹스   — (v1.1) 제목에 slowed·reverb·mashup·lofi version·lo-fi version·sped up·8D audio (남의 히트곡을 늦추거나 섞은 것)
  AI 음악          — 제목·설명에 AI·Suno·인공지능·생성형 (단 'NoAI'·'AI 학습 금지'·'AI 아님' 같은 부정은 뺌)
  커버·리메이크    — 제목에 커버·cover·불러·리메이크
  기존 곡 모음     — 설명의 타임라인 줄 3개 이상 중 절반 넘게 '가수 - 제목' 꼴
  직접 만든 곡     — 설명에 자작곡·직접 작곡·창작곡·오리지널·작곡: ·저작권 표시(©·℗)
  곡 목록만        — 타임라인 3줄 이상인데 가수 표시가 없음 (만든 곡일 수도, 기존 곡일 수도)
  기존 곡으로 보임 — 위에 안 걸리고 제목·설명에 K팝·J팝·팝송·7080·원곡·노래 제목은 댓글 같은 말
  알 수 없음
'만든 곡' = AI 음악 + 직접 만든 곡 · '기존 곡' = 공식 음원 + 기존 곡 리믹스 + 기존 곡 모음 + 기존 곡으로 보임.
로그: [STAGE] [시각] key=value
"""
import csv
import json
import logging
import re
import statistics as st
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

VERSION = "v1.1"
ROOT = Path(__file__).resolve().parent.parent
LOG = logging.getLogger("song_source")

AI_POS = re.compile(r"(?<![A-Za-z])AI(?![A-Za-z])|suno|수노|인공지능|생성형|generative", re.I)
AI_NEG = re.compile(r"no ?ai|ai ?학습|not (made|created) (with|by|using) ai|ai (음악 )?아님|ai 없이|without ai|human[- ]made", re.I)
COVER = re.compile(r"커버|cover|불러|리메이크|remake", re.I)
ORIG = re.compile(r"자작곡|직접 작곡|직접 만든|직접 만들|창작곡|오리지널|original (song|music|composition)|all (music|songs) (is|are|was|were)|"
                  r"composed by|작곡[:：]|작사[:：]|모든 (곡|음악|노래)[은는이가]|저작권[은는]|무단|copyright ©|℗|©", re.I)
EXIST = re.compile(r"kpop|k-pop|케이팝|jpop|j-pop|제이팝|팝송|노래 제목 댓글|곡 제목은 댓글|원곡|가수|아이돌|여돌|남돌|걸그룹|보이그룹|"
                   r"ost 모음|ost모음|드라마 ost|7080|8090|트로트 모음|명곡 모음|히트곡", re.I)
OFFICIAL_TITLE = re.compile(r"official (music |lyric )?video|official audio|official mv|video oficial|lyric video|video song|full video|\(official\)", re.I)
OFFICIAL_CHANNEL = re.compile(r"vevo$|- topic$", re.I)
REMIX = re.compile(r"slowed|reverb|mashup|lo-?fi version|sped up|8d audio", re.I)
TS = re.compile(r"^\s*\[?\(?\d{1,2}:\d{2}(?::\d{2})?\)?\]?\s*[-–.)]?\s*(.+)$")
ARTIST = re.compile(r"\s[-–—|]\s|\s/\s")
MADE = ("AI 음악", "직접 만든 곡")
EXISTING = ("공식 음원", "기존 곡 리믹스", "기존 곡 모음", "기존 곡으로 보임")


def log(stage, level=logging.INFO, **kv):
    LOG.log(level, f"[{stage}] [{datetime.now().isoformat(timespec='seconds')}] " + " ".join(f"{k}={v}" for k, v in kv.items()))


def classify(title, desc, channel=""):
    """→ (갈래, 타임라인 줄 수, 그중 '가수 - 제목' 꼴 수). v1.1: channel(채널 이름)로 공식 음원을 먼저 가름."""
    d = desc[:4000]
    tl = [m.group(1) for m in (TS.match(x) for x in desc.splitlines()) if m]
    art = sum(1 for x in tl if ARTIST.search(x))
    if OFFICIAL_CHANNEL.search((channel or "").strip()) or OFFICIAL_TITLE.search(title):
        return "공식 음원", len(tl), art
    if REMIX.search(title):
        return "기존 곡 리믹스", len(tl), art
    if (AI_POS.search(title) or AI_POS.search(d)) and not AI_NEG.search(title + " " + d):
        return "AI 음악", len(tl), art
    if COVER.search(title):
        return "커버·리메이크", len(tl), art
    if len(tl) >= 3 and art >= max(3, len(tl) * 0.5):
        return "기존 곡 모음", len(tl), art
    if ORIG.search(d):
        return "직접 만든 곡", len(tl), art
    if len(tl) >= 3:
        return "곡 목록만", len(tl), art
    if EXIST.search(title + " " + d):
        return "기존 곡으로 보임", len(tl), art
    return "알 수 없음", len(tl), art


def med(xs, fmt="{:,.0f}"):
    xs = [x for x in xs if x is not None]
    return fmt.format(st.median(xs)) if xs else "–"


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    logging.basicConfig(level=logging.INFO, format="%(message)s", stream=sys.stdout)
    topic = argv[0] if argv else "music"
    out = ROOT / topic / "result" / "outliers"
    try:
        a = json.loads((out / "analysis.json").read_text("utf-8"))
    except (OSError, ValueError) as e:
        log("LOAD", logging.ERROR, file=f"{topic}/result/outliers/analysis.json", error=e,
            next_step=f"python3 tools/cloud_run.py {topic} analyze 를 먼저")
        return 2
    cases = a.get("success_cases") or []
    log("START", tool=f"song_source.py {VERSION}", topic=topic, success_cases=len(cases), analysis_generated=a.get("generated"))
    rows = []
    for c in cases:
        p = out / c["folder"] / "description.txt"
        desc = p.read_text("utf-8", "ignore") if p.is_file() else (c.get("description") or "")
        src, n_tl, n_art = classify(c["title"], desc, c.get("channel") or "")
        rows.append({"no": c["no"], "id": c["id"], "source": src,
                     "group": "만든 곡" if src in MADE else "기존 곡" if src in EXISTING else "커버" if src.startswith("커버") else "모름",
                     "title": c["title"], "channel": c["channel"], "subs": c["subs"], "views": c["views"], "ratio": c["ratio"],
                     "views_per_day": c["views_per_day"], "minutes": c["minutes"], "age_days": c["age_days"], "theme": c["theme"],
                     "format": c["format"], "timeline_lines": n_tl, "artist_lines": n_art, "url": c.get("url")})
    with open(out / "song_source.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else ["no"])
        w.writeheader()
        w.writerows(rows)
    by_src = Counter(r["source"] for r in rows)
    by_grp = Counter(r["group"] for r in rows)
    log("CLASSIFY", **{k.replace(" ", "_"): v for k, v in by_src.items()})

    lines = [f"# 곡 출처별 성공 사례 — {a.get('name') or topic}", "",
             f"자동 생성 — `tools/song_source.py` {VERSION} ({datetime.now().strftime('%Y-%m-%d %H:%M')}) · 입력 `analysis.json` ({a.get('generated')}) 성공 사례 {len(rows)}개 · 할당량 0.",
             "설명란·제목 낱말 규칙이라 거칠다 (도구 머리말의 갈래 규칙). 숫자만 — 해석은 `guides/data_insights.md`.", "",
             "## 1. 갈래별", "", "| 갈래 | 묶음 | 사례 | 조회수 중앙값 | 하루 조회수 중앙값 | 배수 중앙값 | 길이 중앙값(분) | 구독자 중앙값 |", "|---|---|---|---|---|---|---|---|"]
    for s, n in by_src.most_common():
        g = [r for r in rows if r["source"] == s]
        lines.append(f"| {s} | {g[0]['group']} | {n} | {med(r['views'] for r in g)} | {med(r['views_per_day'] for r in g)} | "
                     f"{med((r['ratio'] for r in g), '{:.1f}')} | {med((r['minutes'] for r in g), '{:.0f}')} | {med(r['subs'] for r in g)} |")
    lines += ["", f"묶음: " + " · ".join(f"{k} {v}" for k, v in by_grp.most_common()), "",
              "## 2. '만든 곡'(AI 음악 + 직접 만든 곡) — 주제 묶음별", "",
              "| 주제 묶음 | 사례 | 조회수 중앙값 | 하루 조회수 중앙값 | 길이 중앙값(분) | 예 (조회수 큰 것) |", "|---|---|---|---|---|---|"]
    made = [r for r in rows if r["group"] == "만든 곡"]
    for th, n in Counter(r["theme"] for r in made).most_common():
        g = sorted((r for r in made if r["theme"] == th), key=lambda r: -r["views"])
        ex = " · ".join(f"#{r['no']} {r['title'][:28]} ({r['channel'][:14]}, {r['views']:,})" for r in g[:2])
        lines.append(f"| {th} | {n} | {med(r['views'] for r in g)} | {med(r['views_per_day'] for r in g)} | {med((r['minutes'] for r in g), '{:.0f}')} | {ex} |")
    lines += ["", "## 3. '만든 곡' — 길이", "", "| 길이 | 사례 | 조회수 중앙값 |", "|---|---|---|"]
    for lo, hi, lab in [(4, 15, "4~15분"), (15, 40, "15~40분"), (40, 90, "40~90분"), (90, 180, "90~180분"), (180, 10 ** 6, "180분 이상")]:
        g = [r for r in made if lo <= r["minutes"] < hi]
        lines.append(f"| {lab} | {len(g)} | {med(r['views'] for r in g)} |")
    lines += ["", "## 4. '만든 곡' 조회수 상위 24개 (썸네일 `song_source_thumbs.jpg` 같은 차례)", "",
              "| # | 조회수 | 길이(분) | 구독자 | 주제 묶음 | 갈래 | 제목 | 채널 |", "|---|---|---|---|---|---|---|---|"]
    top = sorted(made, key=lambda r: -r["views"])[:24]
    for r in top:
        lines.append(f"| {r['no']} | {r['views']:,} | {r['minutes']:.0f} | {r['subs']:,} | {r['theme']} | {r['source']} | "
                     f"{r['title'][:60].replace('|', '/')} | {r['channel'][:18]} |")
    (out / "song_source.md").write_text("\n".join(lines) + "\n", "utf-8")
    try:                                                        # 썸네일 한 장 (없어도 표는 씀)
        from PIL import Image, ImageDraw
        W, H = 320, 180
        img = Image.new("RGB", (W * 4, H * 6), "black")
        dr = ImageDraw.Draw(img)
        for i, r in enumerate(top):
            x, y = (i % 4) * W, (i // 4) * H
            p = out / f"W_{r['id']}" / "thumbnail.jpg"
            if p.is_file():
                img.paste(Image.open(p).convert("RGB").resize((W, H)), (x, y))
            dr.rectangle([x, y, x + 40, y + 16], fill="black")
            dr.text((x + 2, y + 2), f"#{r['no']}", fill="yellow")
        img.save(out / "song_source_thumbs.jpg", quality=85)
    except Exception as e:                                      # noqa: BLE001 — 썸네일은 덤
        log("THUMBS", logging.WARNING, error=e, note="표는 그대로 씀")
    log("DONE", made=len(made), existing=by_grp.get("기존 곡", 0), cover=by_grp.get("커버", 0), unknown=by_grp.get("모름", 0),
        files=f"{topic}/result/outliers/song_source.csv·song_source.md·song_source_thumbs.jpg")
    return 0


if __name__ == "__main__":
    sys.exit(main())
