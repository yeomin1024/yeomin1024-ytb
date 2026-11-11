#!/usr/bin/env python3
# VERSION: v1.0 — 2026-11-11 — 새로: 제목·썸네일 '피드 시험' 시험지를 만든다 (사용자 2026-11-11 "너가 페르소나 입장에서
#   생각했을 때 썸네일 문구, 보조문구, 제목만 봤을 때 썸네일 클릭할 것 같아 안할것 같아?" — 후보끼리만 견주면 '누를까'를 알 수 없었음).
"""피드 시험 시험지 — 이번 주 실제 영상 제목 사이에 우리 제목을 섞어, 어느 게 우리 건지 모르는 새 검토자에게 '뭘 누를지' 묻는다.

쓰는 법 (stock/guides/persona_judge.md 9-7):
  python3 tools/trend_scan.py stock                      # 오늘 판 (없거나 3일 넘었으면 먼저)
  python3 tools/feed_sheet.py stock --title "<제목 1>" --title "<제목 2>" \
      --thumb "큰 글자 1 / 큰 글자 2 | 말풍선 | 꼬리표" --thumb "…" --image "그림 한 줄 설명" --out <scratchpad>/feed
  → home_<페르소나><n>.md (제목마다·페르소나마다 한 장 — 검토자 한 명에게 한 장만) · next.md (그 검토자에게 이어서) · key.json (정답표 — 검토자에게 주지 않음)
  python3 tools/feed_sheet.py --selftest

입력: <주제>/result/trend/trend_<날짜>.json (tools/trend_scan.py) · <주제>/feed_personas.toml (처지 + 원문 댓글만)
한계: 경쟁 영상은 제목·채널·구독자·길이만 (썸네일 그림은 못 넣음) · 검토자는 모델 → 결과는 추정. 연구·교육용 — 투자 권유 아님.
CHANGELOG
- v1.0 2026-11-11 새로 — pick_feed()·market_line()·sheet()·next_sheet() · --selftest
"""
from __future__ import annotations

import argparse
import datetime as dt
import glob
import json
import logging
import os
import random
import sys
import tomllib

VERSION = "v1.0"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log = logging.getLogger("feed_sheet")
MAX_AGE_DAYS = 3          # 이보다 오래된 판이면 경고 (오늘의 경쟁 영상이 아님)
MIX = (5, 2, 3)           # 오늘·어제 올라온 큰 영상 · 그 전 주 큰 영상 · 작은 채널 — 합 10


def stamp() -> str:
    return dt.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")


def subs_text(n: int | None) -> str:
    if not n:
        return "비공개"
    if n >= 10000:
        v = n / 10000
        return f"{v:.0f}만" if v >= 10 else f"{v:.1f}만".replace(".0만", "만")
    return f"{n:,}명"


def age_text(published: str, today: str) -> str:
    d = (dt.date.fromisoformat(today) - dt.date.fromisoformat(published[:10])).days
    return "오늘" if d <= 0 else "어제" if d == 1 else f"{d}일 전"


def pick_feed(trend: dict, videos: dict, n: int, seed: str) -> list[dict]:
    """경쟁 영상 n개 — 채널당 하나 · 쇼츠 뺌 · 순서는 날짜를 씨앗으로 섞음 (같은 날 같은 시험지)."""
    today = trend["date"]
    fresh = [v for v in trend.get("fresh", []) if age_text(v["published"], today) in ("오늘", "어제")]
    older = [v for v in trend.get("top_long", []) if v not in fresh]
    small = trend.get("top_small", [])
    want = [round(n * m / sum(MIX)) for m in MIX]
    want[0] += n - sum(want)
    out, seen_id, seen_ch = [], set(), set()
    for pool, k in zip((fresh, older, small), want):
        took = 0
        for v in pool:
            if took >= k:
                break
            if v["id"] in seen_id or v["channel"] in seen_ch or v.get("kind") == "short":
                continue
            full = videos.get(v["id"], {})
            out.append({"id": v["id"], "title": v["title"].strip(), "channel": v["channel"], "subs": v.get("subs"),
                        "minutes": max(1, int(full.get("seconds", v.get("seconds", 0)) // 60)),
                        "age": age_text(v["published"], today)})
            seen_id.add(v["id"]); seen_ch.add(v["channel"]); took += 1
        log.info("[PICK] [%s] pool_size=%d want=%d took=%d", stamp(), len(pool), k, took)
    if len(out) < max(4, n // 2):
        raise SystemExit(f"[PICK] 경쟁 영상이 {len(out)}개뿐 — trend_scan 을 다시 돌리세요 (python3 tools/trend_scan.py <주제>)")
    random.Random(seed).shuffle(out)
    return out


def market_line(trend: dict) -> str:
    """그날 시장 한 줄 — trend_scan 의 market 숫자 그대로 (내 해석을 붙이지 않음)."""
    bits = []
    for m in trend.get("market", [])[:2]:
        last = ", ".join(f"{d[5:]} {c:+.1f}%" for d, c in m.get("last10", [])[-4:])
        bits.append(f"{m['name']}는 1년 최고가보다 {abs(m['from_high']):.1f}% 아래 (최근 4거래일 {last})")
    return f"- 오늘은 {trend['date']} 밤입니다. " + " · ".join(bits) + "."


def sheet(persona: dict, trend: dict, feed: list[dict], ours: dict, pos: int) -> str:
    rows = feed[:pos - 1] + [ours] + feed[pos - 1:]
    lines = [f"{i}. {r['title']}\n   — {r['channel']} · 구독자 {subs_text(r['subs']) if isinstance(r['subs'], int) else r['subs']} · {r['minutes']}분 · {r['age']}"
             for i, r in enumerate(rows, 1)]
    who = "\n".join(f"- {w}" for w in persona["who"])
    cm = "\n".join(f'  - "{c}"' for c in persona["comments"])
    return f"""당신은 지금부터 아래 사람입니다. 분석가나 마케터가 아니라 **이 사람 본인**으로 답합니다. 도구는 쓰지 말고 바로 답하세요.

## 당신
{who}
{market_line(trend)}
- 요즘 당신 같은 사람들이 유튜브에 쓴 댓글(원문):
{cm}
- 평소 버릇: {persona['habit']}

## 지금 화면
퇴근 뒤 유튜브 앱을 열었더니 홈에 아래 영상 {len(rows)}개가 떠 있습니다. 썸네일의 큰 글자는 제목과 거의 같은 말이라고 치고, 제목·채널·구독자·길이·올린 날만 보고 정합니다. 오늘 밤 볼 수 있는 건 2~3개입니다.

{chr(10).join(lines)}

## 답하는 형식 (이 형식만, 풀어 쓰지 않음)
1) 영상마다 한 줄씩 {len(rows)}줄: `번호 | 누름 / 멈춤만 / 넘김 | 그 순간 머릿속 말 (반말 한마디)`
2) 실제로 누를 순서 1위~3위: 번호와 이유 한 줄씩
3) 절대 안 누를 것 2개: 번호와 이유 한 줄씩

규칙: 평소 버릇 그대로 솔직하게. 작은 채널이라고 봐주지도 깎지도 않습니다. 착하게 답하려 하지 말 것.
"""


def next_sheet(titles: list[str], thumbs: list[str], image: str, ours: dict, pos: int, total: int) -> str:
    t = "\n".join(f"T{i}. {x}" for i, x in enumerate(titles, 1))
    s = "\n".join("S{}. 「{}」 · 말풍선 「{}」 · 꼬리표 「{}」".format(i, *[p.strip() for p in (x.split("|") + ["", ""])[:3]])
                  for i, x in enumerate(thumbs, 1))
    return f"""이어서 하나만 더 — 같은 사람으로 답합니다.

아까 홈 화면의 **{pos}번 영상**({ours['channel']}, 구독자 {ours['subs']}, {ours['minutes']}분)은 아직 제목과 썸네일 글자를 고르는 중입니다. 영상 내용은 어느 쪽이든 같습니다: 얼굴 없이 그래프와 내레이션으로, 과거 주가 기록을 계산해서 보여 줍니다 (전망·종목 추천 없음 · 직접 매매한 기록이 아니라 과거 주가로 계산한 것).
썸네일 그림도 같습니다: {image}

[제목 후보]
{t}

[썸네일 글자 후보] (그림 위 큰 글자 2줄 / 말풍선 / 구석의 작은 꼬리표)
{s}

## 답하는 형식 (이 형식만)
1) 제목마다 한 줄: `T번호 | 누름 / 멈춤만 / 넘김 | 머릿속 말`
2) 썸네일마다 한 줄: `S번호 | 누름 / 멈춤만 / 넘김 | 머릿속 말`
3) 가장 누를 조합 하나(제목 + 썸네일)와, 그 조합이었다면 아까 홈 화면 {total}개 가운데 몇 번째로 눌렀을지 (안 누르면 '안 누름')
4) 거슬리거나 속는 느낌이 드는 낱말 (있으면 · 없으면 '없음')
5) 당신이라면 이렇게 써야 누른다: 제목 하나 · 썸네일 큰 글자 하나 (당신 말투로)
"""


def build(topic: str, titles: list[str], thumbs: list[str], image: str, out: str, date: str | None, pos: int, n: int,
          channel: str, subs: str, minutes: int, who: list[str] | None, root: str = ROOT) -> dict:
    tdir = os.path.join(root, topic, "result", "trend")
    files = sorted(glob.glob(os.path.join(tdir, "trend_*.json")))
    if date:
        files = [f for f in files if f.endswith(f"trend_{date}.json")]
    if not files:
        raise SystemExit(f"[LOAD] {tdir} 에 trend_*.json 없음 — 먼저 python3 tools/trend_scan.py {topic}")
    trend = json.load(open(files[-1], encoding="utf-8"))
    vf = os.path.join(tdir, f"videos_{trend['date']}.json")
    videos = {v["id"]: v for v in json.load(open(vf, encoding="utf-8"))} if os.path.exists(vf) else {}
    age = (dt.date.today() - dt.date.fromisoformat(trend["date"])).days
    log.info("[LOAD] [%s] trend=%s date=%s age_days=%d videos=%d", stamp(), os.path.relpath(files[-1], root), trend["date"], age, len(videos))
    if age > MAX_AGE_DAYS:
        log.warning("[LOAD] [%s] 판이 %d일 전 것 — 오늘의 경쟁 영상이 아님. trend_scan 을 다시 돌리세요.", stamp(), age)
    personas = tomllib.load(open(os.path.join(root, topic, "feed_personas.toml"), "rb"))
    keys = [k for k in personas if isinstance(personas[k], dict) and (not who or k in who)]
    for k in keys:   # 내가 쓴 속마음 요약은 우리 제목과 같은 말이 되어 결과를 부풀린다 — 원문 댓글만
        bad = [w for w in personas[k]["who"] if w.strip().startswith(("머릿속", "속마음"))]
        if bad or len(personas[k]["comments"]) < 4:
            raise SystemExit(f"[CHECK] feed_personas.toml [{k}]: 속마음 요약 줄은 넣지 않고(원문 댓글만), 댓글은 4개 이상 — {bad}")
    if not titles or any(not t.strip() for t in titles):
        raise SystemExit("[CHECK] --title 이 비었음")
    feed = pick_feed(trend, videos, n, seed=trend["date"])
    if not 1 <= pos <= len(feed) + 1:
        raise SystemExit(f"[CHECK] --pos 는 1~{len(feed) + 1}")
    os.makedirs(out, exist_ok=True)
    key = {"tool": f"feed_sheet {VERSION}", "trend": trend["date"], "pos": pos, "feed": [f["id"] for f in feed], "sheets": {}}
    for k in keys:
        for i, t in enumerate(titles, 1):
            ours = {"title": t.strip(), "channel": channel, "subs": subs, "minutes": minutes, "age": "오늘"}
            name = f"home_{k}{i}.md"
            open(os.path.join(out, name), "w", encoding="utf-8").write(sheet(personas[k], trend, feed, ours, pos))
            key["sheets"][name] = {"persona": personas[k]["name"], "title": t.strip()}
    ours = {"channel": channel, "subs": subs, "minutes": minutes}
    if thumbs:
        open(os.path.join(out, "next.md"), "w", encoding="utf-8").write(next_sheet(titles, thumbs, image, ours, pos, len(feed) + 1))
    json.dump(key, open(os.path.join(out, "key.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    log.info("[WRITE] [%s] out=%s sheets=%d personas=%s titles=%d thumbs=%d feed=%d pos=%d", stamp(), out, len(key["sheets"]),
             ",".join(keys), len(titles), len(thumbs), len(feed), pos)
    return key


def selftest() -> None:
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        tdir = os.path.join(tmp, "x", "result", "trend"); os.makedirs(tdir)
        today = dt.date.today().isoformat(); yday = (dt.date.today() - dt.timedelta(days=1)).isoformat()
        old = (dt.date.today() - dt.timedelta(days=5)).isoformat()
        mk = lambda i, d, ch, subs: {"id": f"v{i}", "title": f"제목 {i}", "channel": ch, "subs": subs, "published": d, "seconds": 600 + i}
        trend = {"date": today, "market": [{"name": "코스피", "from_high": -42.5, "last10": [[yday, -6.0], [today, 4.4]]}],
                 "fresh": [mk(i, today if i % 2 else yday, f"큰{i}", 1000000 + i) for i in range(8)] + [mk(0, today, "큰0", 1)],
                 "top_long": [mk(i, old, f"옛{i}", 500000) for i in range(20, 26)],
                 "top_small": [mk(i, old, f"작{i}", 5860 + i) for i in range(40, 46)]}
        json.dump(trend, open(os.path.join(tdir, f"trend_{today}.json"), "w", encoding="utf-8"), ensure_ascii=False)
        open(os.path.join(tmp, "x", "feed_personas.toml"), "w", encoding="utf-8").write(
            '[A]\nname="가"\nwho=["처지"]\nhabit="버릇"\ncomments=["1","2","3","4"]\n[E]\nname="나"\nwho=["처지"]\nhabit="버릇"\ncomments=["1","2","3","4"]\n')
        out = os.path.join(tmp, "out")
        key = build("x", ["우리 제목 하나", "우리 제목 둘"], ["큰 글자 / 둘째 줄 | 말풍선 | 꼬리표"], "그림", out, None, 6, 10, "채널", "1천 명 미만", 8, None, root=tmp)
        assert len(key["sheets"]) == 4 and len(key["feed"]) == 10 and len(set(key["feed"])) == 10, key
        s = open(os.path.join(out, "home_A2.md"), encoding="utf-8").read()
        assert "6. 우리 제목 둘" in s and "11줄" in s and "머릿속:" not in s and "42.5% 아래" in s, s[:400]
        assert s.count(" · 구독자 ") == 11 and "100만" in s and "5,9" in s
        nx = open(os.path.join(out, "next.md"), encoding="utf-8").read()
        assert "T2. 우리 제목 둘" in nx and "S1. 「큰 글자 / 둘째 줄」 · 말풍선 「말풍선」 · 꼬리표 「꼬리표」" in nx and "6번 영상" in nx
        open(os.path.join(tmp, "x", "feed_personas.toml"), "w", encoding="utf-8").write(
            '[A]\nname="가"\nwho=["머릿속: 팔까 버틸까"]\nhabit="버릇"\ncomments=["1","2","3","4"]\n')
        try:
            build("x", ["제목"], [], "", out, None, 6, 10, "채널", "1천", 8, None, root=tmp); raise AssertionError("요약 줄이 통과함")
        except SystemExit:
            pass
        assert subs_text(1240000) == "124만" and subs_text(31800) == "3.2만" and subs_text(5860) == "5,860명"
    print("[SELFTEST] ok — pick_feed(채널당 하나·섞기) · 우리 제목 자리 · 속마음 요약 줄 막기 · next.md · 구독자 표기")


def main() -> None:
    ap = argparse.ArgumentParser(description="피드 시험 시험지 (제목·썸네일 '누를까')")
    ap.add_argument("topic", nargs="?")
    ap.add_argument("--title", action="append", default=[], help="우리 제목 후보 (여러 번) — 홈 화면에는 시험지마다 하나")
    ap.add_argument("--thumb", action="append", default=[], help="'큰 글자 1 / 큰 글자 2 | 말풍선 | 꼬리표' (여러 번) — next.md")
    ap.add_argument("--image", default="(그림 설명)", help="썸네일 그림 한 줄 설명")
    ap.add_argument("--out", help="시험지 폴더 (scratchpad — 저장소에 넣지 않음)")
    ap.add_argument("--date", help="trend 날짜 (기본 가장 새 것)")
    ap.add_argument("--pos", type=int, default=6, help="우리 영상 자리 (모든 시험지 같은 자리)")
    ap.add_argument("--n", type=int, default=10, help="경쟁 영상 수")
    ap.add_argument("--channel", default="STOCK LAB"); ap.add_argument("--subs", default="1천 명 미만"); ap.add_argument("--minutes", type=int, default=8)
    ap.add_argument("--personas", help="쉼표로 (기본 전부) — 예 A,E")
    ap.add_argument("--selftest", action="store_true"); ap.add_argument("--log", default="INFO")
    a = ap.parse_args()
    logging.basicConfig(level=getattr(logging, a.log.upper(), logging.INFO), format="%(message)s")
    if a.selftest:
        return selftest()
    if not a.topic or not a.out:
        ap.error("topic 과 --out 이 필요합니다")
    t0 = dt.datetime.now()
    build(a.topic, a.title, a.thumb, a.image, a.out, a.date, a.pos, a.n, a.channel, a.subs, a.minutes, a.personas.split(",") if a.personas else None)
    log.info("[DONE] [%s] seconds=%.2f — 시험지 한 장을 새 검토자 한 명에게 (같은 사람에게 두 제목을 보이지 않음) · key.json 은 주지 않음", stamp(), (dt.datetime.now() - t0).total_seconds())


if __name__ == "__main__":
    main()
