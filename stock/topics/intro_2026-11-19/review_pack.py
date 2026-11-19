#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-11-19 — 후보 수를 파일에서 셈 (v1.0 은 '4안'·'6안'을 글로 박아 2회차에 수가 틀림).
# (v1.0 — 2026-11-19 — 제목(사용자)·썸네일 4안·도입 6안을 한 번에 검토하는 지시문 (guides/persona_loop.md 세 단계를 후보 비교용으로 묶음 — 회차마다 새 검토자 2명: P1 · 반론).
#   피드 = compare.csv 최근 90일 한국어 4분 이상 제목 9개(무작위 · 씨앗 = 회차) + 우리 제목 1개 — 어느 것이 우리 것인지 알리지 않음.
#   페르소나 카드 = persona_gate.py v1.2 가 만든 카드 그대로 (stock/topics/loss_alt_2026-11-19/review/r5_exit.md · r5_rebut.md 의 '1. 너는 누구인가').
#   실행: python3 stock/topics/intro_2026-11-19/review_pack.py <회차> <도입 파일> <썸네일 json>
import csv, json, random, re, sys, time
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
TITLE = "삼성전자, 하이닉스 폭락 후 코스피 주가 이걸 보면 전망이 보일 겁니다"


def card(path, start, stop):
    s = Path(path).read_text(encoding="utf-8")
    a, b = s.index(start), s.index(stop)
    return s[a:b].strip()


def intros(path):
    out, cur = {}, None
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        m = re.match(r"^\[(\w) (.+)\]$", line)
        if m:
            cur = m.group(1); out[cur] = []
            continue
        out[cur].append(line)
    return out


def main(rnd, intro_file, thumb_file):
    rnd = int(rnd)
    rows = [r for r in csv.DictReader(open(ROOT / "stock/result/outliers/compare.csv", encoding="utf-8-sig"))]
    cut = str(date(2026, 11, 19) - timedelta(days=90))
    pool = [r["title"] for r in rows if r["published"] >= cut and re.search("[가-힣]", r["title"]) and float(r["minutes"] or 0) >= 4 and r["title"] != TITLE]
    rng = random.Random(20261119 + rnd)
    feed = rng.sample(pool, 9)
    pos = rng.randrange(10)
    feed.insert(pos, TITLE)
    th = json.loads(Path(thumb_file).read_text(encoding="utf-8"))
    it = intros(intro_file)
    base = ROOT / "stock/topics/loss_alt_2026-11-19/review"
    p1 = card(base / "r5_exit.md", "## 1. 너는 누구인가", "## 2. 할 일")
    k = card(base / "r5_rebut.md", "## 0. 한눈에", "## 2. 할 일")
    feed_md = "\n".join(f"{i + 1}. {t}" for i, t in enumerate(feed))
    th_md = "\n".join(f"- **{x['id']}** 주요 문구: 「{x['main'][0]} / {x['main'][1]}」 · 보조 문구: 「{x['sub']}」 · 그림: {x['image']}" for x in th)
    it_md = "\n\n".join(f"**도입 {key}**\n" + "\n".join(f"{key}{j + 1}. {l}" for j, l in enumerate(v)) for key, v in it.items())
    common = f"""
## 3. 홈 화면 (유튜브 홈에 뜬 영상 10개 — 제목만)
{feed_md}

## 4. 썸네일 후보 (3번 화면의 {pos + 1}번 영상 썸네일 — 같은 제목에 썸네일만 다른 {len(th)}안)
{th_md}

## 5. 도입 후보 (그 영상을 눌렀을 때 첫 25~30초 — {len(it)}안, 하나만 쓰임 · 진행자 한 명의 AI 음성 · 화면엔 숫자·그래프)
{it_md}
"""
    out_dir = f"stock/topics/intro_2026-11-19/review/answers_r{rnd}"
    p1_task = f"""# 페르소나 검토 — 제목·썸네일·도입 후보 비교 (대상 페르소나) · {rnd}회차 (review_pack.py v1.0)

너는 처음 이 화면을 보는 검토자다. 다른 회차 결과는 모른다. 아래 페르소나가 **되어** 솔직하게 답한다 — 칭찬하려 애쓰지 않고, 억지로 흠을 만들지도 않는다.
검토자 이름: E{rnd}-P1 · 답은 아래 JSON 꼴 그대로 `{out_dir}/E{rnd}-P1.json` 에 저장하고, 마지막 답에도 붙인다. 투자 권유가 아닌 연구·교육용 영상의 검토다.

{p1}

## 2. 할 일
1. 3번 홈 화면에서 **가장 먼저 누를 영상 하나**와 까닭, 그리고 {pos + 1}번을 누르겠는가 (누른다/안 누른다 + 까닭).
2. 4번 썸네일 {len(th)}안을 누르고 싶은 순서로 — 안마다 한 줄 까닭. 제목+썸네일이 '낚시'(내용보다 과장)로 느껴지는 안이 있으면 표시.
3. 5번 도입 {len(it)}안을 **하나씩 따로** 처음부터 듣는다고 생각하고: 끄고 싶어진 줄(예 'C3')과 까닭 · 풀이 없이 모르는 말 · 30초 뒤 계속 볼 것인가 · 제목·썸네일에서 기대한 것과 맞는가.
4. 마지막에 가장 계속 보고 싶은 도입 하나와 까닭.
{common}
## 답 (JSON)
```json
{{"reviewer": "E{rnd}-P1", "first_click": {{"no": 0, "why": ""}}, "click_ours": {{"click": true, "why": ""}},
 "thumb_rank": [{{"id": "T?", "why": "", "bait": false}}],
 "intros": {{"A": {{"exit_line": null, "why": "", "hard_words": [], "keep_watching": true, "matches_promise": true}}}},
 "best_intro": {{"id": "", "why": ""}}}}
```
"""
    k_task = f"""# 페르소나 검토 — 제목·썸네일·도입 후보 반론 (반론 페르소나) · {rnd}회차 (review_pack.py v1.0)

너는 처음 이 화면을 보는 검토자다. 다른 회차 결과는 모른다. 아래 페르소나가 **되어** 솔직하게 답한다.
검토자 이름: K{rnd}-반론 · 답은 아래 JSON 꼴 그대로 `{out_dir}/K{rnd}-반론.json` 에 저장하고, 마지막 답에도 붙인다. 투자 권유가 아닌 연구·교육용 영상의 검토다.

{k}

## 2. 할 일
1. 3번 홈 화면에서 {pos + 1}번을 누르겠는가 (누른다/안 누른다 + 까닭) — 제목이 내용보다 과장(낚시)인가.
2. 4번 썸네일 {len(th)}안마다 반박 댓글감(K1~K8 · 상·중·하).
3. 5번 도입 {len(it)}안마다 반박 댓글감(K1~K8 · 상·중·하 · 줄 번호 예 'B4'). 숫자는 도입 안에서 앞뒤가 맞는지까지만 본다(밖의 자료를 찾지 않음). '전망을 맞힌다'고 약속하거나 한쪽 행동을 권하는 말로 들리는 줄은 꼭 짚는다.
4. 반박이 가장 적게 달릴 도입·썸네일 하나씩과 까닭.
{common}
## 답 (JSON)
```json
{{"reviewer": "K{rnd}-반론", "click_ours": {{"click": true, "why": "", "bait": false}},
 "thumbs": {{"T1": [{{"level": "중", "k": "K8", "text": "", "fix": ""}}]}},
 "intros": {{"A": [{{"level": "중", "k": "K5", "line": "A2", "text": "", "fix": ""}}]}},
 "least_rebuttal": {{"intro": "", "thumb": "", "why": ""}}}}
```
"""
    rv = HERE / "review"; rv.mkdir(exist_ok=True)
    (rv / f"r{rnd}_P1.md").write_text(p1_task, "utf-8")
    (rv / f"r{rnd}_K.md").write_text(k_task, "utf-8")
    (ROOT / out_dir).mkdir(parents=True, exist_ok=True)
    print(f"[PACK] [{time.strftime('%Y-%m-%dT%H:%M:%S')}] round={rnd} ours_at={pos + 1} intros={list(it)} thumbs={[x['id'] for x in th]} out={rv}/r{rnd}_*.md")


if __name__ == "__main__":
    main(*sys.argv[1:4])
