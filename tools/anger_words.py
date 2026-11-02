#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-11-02 — 최초. 시청자가 '누구에게·어떻게' 화를 내는지 댓글 갈래별 수·좋아요 배수 + 제목 꼴별 성공 몫을 센다 (읽기만).
#          사용자 지시 2026-11-02 "아니 제목좀 더 자극적으로 해봐 댓글보면 나라가 일을 안한다 도둑놈이다 이렇게 말하던데 좀 참고해보라고".
#          설정 <주제>/anger_words.toml · 결과 <주제>/result/outliers/anger_words.md (+ 로그). 근거로 쓰는 곳: economic/guides/channel.md 3번.
r"""
  python3 tools/anger_words.py economic            # 셈 → anger_words.md
  python3 tools/anger_words.py economic --top 5    # 갈래마다 좋아요 상위 댓글 수 (기본 5)
같은 댓글 id 는 한 번만(파일에 겹쳐 적힌 줄이 있음) · 채널 주인 댓글 뺌 · 좋아요 배수 = 갈래 위 댓글 평균 ÷ 전체 위 댓글 평균.
댓글 원문은 앞 90자만 · 작성자 이름·채널 ID 는 적지 않음 (CLAUDE.md). ※ 정보 제공용 — 세무·법률 상담이 아님.
"""
import csv
import glob
import json
import logging
import re
import statistics as st
import sys
import time
import tomllib
from pathlib import Path

VERSION = "v1.0"
ROOT = Path(__file__).resolve().parent.parent
log = logging.getLogger("anger_words")


def stamp():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def main(argv):
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    topic = next((a for a in argv if not a.startswith("-") and not a.isdigit()), None)
    if not topic:
        print(__doc__)
        return 2
    top_n = int(argv[argv.index("--top") + 1]) if "--top" in argv else 5
    R = ROOT / topic / "result" / "outliers"
    cfg_path = ROOT / topic / "anger_words.toml"
    try:
        cfg = tomllib.load(open(cfg_path, "rb"))
    except (OSError, tomllib.TOMLDecodeError) as e:
        log.error(f"[LOAD] [{stamp()}] stage=config file=\"{cfg_path}\" error=\"{e}\" next=\"설정 파일을 만들거나 고치세요\"")
        return 1
    log.info(f"[START] [{stamp()}] tool=\"anger_words.py {VERSION}\" topic=\"{topic}\" config=\"{cfg_path.relative_to(ROOT)}\"")

    # 비교 집단 (제목·성공)
    succ, title, in_cmp = {}, {}, {}
    try:
        for r in csv.DictReader(open(R / "compare.csv", encoding="utf-8-sig")):
            succ[r["id"]] = r["success"] == "True"
            title[r["id"]] = r["title"]
            in_cmp[r["id"]] = r["in_compare"] == "True"
    except OSError as e:
        log.error(f"[LOAD] [{stamp()}] stage=compare file=\"{R / 'compare.csv'}\" error=\"{e}\" next=\"cloud_run.py {topic} analyze 먼저\"")
        return 1

    # 댓글 (id 로 중복 제거)
    seen, rows, files = set(), [], sorted(glob.glob(str(R / "W_*" / "comments.jsonl")))
    dup = 0
    for f in files:
        vid = Path(f).parent.name[2:]
        for line in open(f, encoding="utf-8"):
            try:
                c = json.loads(line)
            except json.JSONDecodeError:
                continue
            if c.get("creator"):
                continue
            if c["id"] in seen:
                dup += 1
                continue
            seen.add(c["id"])
            rows.append((vid, c.get("parent") is None, int(c.get("likes") or 0), c.get("text", "")))
    top_all = [r[2] for r in rows if r[1]]
    if not top_all:
        log.error(f"[LOAD] [{stamp()}] stage=comments files={len(files)} error=\"댓글 없음\" next=\"cloud_run.py {topic} comments\"")
        return 1
    base = st.mean(top_all)
    log.info(f"[LOAD] [{stamp()}] videos={len(files)} comments={len(rows)} top_level={len(top_all)} duplicates_skipped={dup} base_like_mean={base:.2f}")

    sub = cfg.get("comments", {})
    out = [f"# 분노 댓글·제목 셈 — {topic}", "",
           f"`tools/anger_words.py` {VERSION} · {stamp()} · 설정 `{cfg_path.relative_to(ROOT)}` (정규식은 거기에). 숫자만 — 해석은 `{topic}/guides/channel.md` 3번.",
           "※ 정보 제공용 — 세무·법률 상담이 아님. 댓글 원문은 앞 90자만, 작성자 정보 없음.", "",
           f"- 대상: 분석 영상 {len(files)}개 · 시청자 댓글 {len(rows):,} (위 댓글 {len(top_all):,}) · 겹쳐 적힌 줄 {dup:,} 뺌",
           f"- 기준: 위 댓글 좋아요 평균 **{base:.1f}** · 좋아요 10개 넘는 몫 {sum(x >= 10 for x in top_all) / len(top_all) * 100:.1f}%", "",
           "## 1. 댓글 갈래 — 누구에게·어떻게 화내나", "",
           "| 갈래 | 댓글 | 위 댓글 | 영상 | 좋아요 평균 | **배수** | 10개 넘는 몫 | 성공 사례 영상 위 댓글 |",
           "|---|---|---|---|---|---|---|---|"]
    tops = []
    for g in cfg.get("group", []):
        pat = g["pattern"]
        for k, v in sub.items():  # {STATE}·{TAKE} 자리만 바꿈 (정규식 {0,12} 는 그대로)
            pat = pat.replace("{" + k + "}", v)
        rx = re.compile(pat)
        hit = [r for r in rows if rx.search(r[3])]
        top = [r for r in hit if r[1]]
        L = [r[2] for r in top]
        mean = st.mean(L) if L else 0.0
        share = sum(x >= 10 for x in L) / len(L) * 100 if L else 0.0
        sc = sum(succ.get(r[0], False) for r in top)
        out.append(f"| {g['code']} {g['name']} | {len(hit):,} | {len(top):,} | {len({r[0] for r in hit})} | {mean:.1f} | **×{mean / base:.2f}** | {share:.1f}% | {sc} |")
        log.info(f"[GROUP] [{stamp()}] code={g['code']} hits={len(hit)} top_level={len(top)} like_mean={mean:.2f} ratio={mean / base:.2f}")
        tops.append((g, sorted(top, key=lambda r: -r[2])[:top_n]))
    out += ["", "## 2. 갈래마다 좋아요 상위 댓글 (앞 90자)", ""]
    for g, tp in tops:
        out.append(f"**{g['code']} {g['name']}**")
        for r in tp:
            t = re.sub(r"\s+", " ", r[3])[:90]
            out.append(f"- 👍{r[2]:,} — {t} · 〔{title.get(r[0], '?')[:30]}〕")
        out.append("")

    ids = [i for i in title if in_cmp.get(i)]
    b = sum(succ[i] for i in ids) / len(ids) * 100 if ids else 0
    out += ["## 3. 제목 꼴 — 비교 집단 성공 몫", "", f"비교 집단 {len(ids):,}개 · 성공 몫 **{b:.1f}%** (15개 미만은 표본 적음)", "",
            "| 꼴 | 제목 | 성공 | 성공 몫 | 배수 | 표본 |", "|---|---|---|---|---|---|"]
    for k, p in cfg.get("titles", {}).items():
        rx = re.compile(p)
        h = [i for i in ids if rx.search(title[i])]
        s = sum(succ[i] for i in h)
        sh = s / len(h) * 100 if h else 0
        out.append(f"| {k} | {len(h)} | {s} | {sh:.1f}% | ×{sh / b:.2f} | {'적음' if len(h) < 15 else '됨'} |" if b else f"| {k} | {len(h)} | {s} | - | - | - |")
        log.info(f"[TITLE] [{stamp()}] form=\"{k}\" n={len(h)} success={s} share={sh:.1f} base={b:.1f}")
    dst = R / "anger_words.md"
    dst.write_text("\n".join(out) + "\n", encoding="utf-8")
    log.info(f"[DONE] [{stamp()}] wrote=\"{dst.relative_to(ROOT)}\" groups={len(cfg.get('group', []))} title_forms={len(cfg.get('titles', {}))}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
