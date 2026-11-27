#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v0.1.1 — 2026-11-27 — 살 마음 댓글을 '그 댓글이 나온 영상 수'로 (한 영상은 5개까지만 셈) + 광고·도배 댓글 뺌.
#   까닭 (audit): v0.1.0 은 공동구매 영상 하나가 찜기 댓글 170개 중 158개, 틴트 브랜드 영상 하나가 립 118개 중 115개를 채웠고, '명품 가방 최상급 제작' 도배가 가방 대표 댓글이었음.
# (v0.1.0 — 2026-11-27 — 새로 (사용자 지시 2026-11-27 "아니 나는 어떤 쿠팡 아이템을 선정해야되는지 모르겠어 어떻게 할까? 자동화도 가능해?")
#   상품 고르기 자동화 1단계 = 유튜브 수요 쪽 (할당량 0 — 이미 받은 탐색 목록·승인 자료만 읽음).
#   물건 이름 사전(ITEMS, 갈래 8개)을 제목·태그·댓글에서 찾아 물건마다:
#     ① 영상 수 · 최근 90일 영상의 하루 조회수 합(지금 수요) · 조회수 가운데값 · 성공 사례 수 (탐색 목록 shopping/result/web/explore.json)
#     ② 살 마음 댓글 수 = 그 물건 이름 + '어디서·제품명·링크·브랜드·사고 싶·샀' 이 함께 든 시청자 댓글 (승인 자료 W_*/comments.jsonl)
#     ③ 다이소 몫 = 그 물건 영상 중 제목에 '다이소'가 든 비율 (높으면 쿠팡 수수료가 안 나올 수 있음 → '다이소 vs 쿠팡' 비교로)
#     ④ 조심 = 효능 광고 규제 갈래(화장품 기능·건강기능식품·의료기기 비슷한 것) — 영상에서 효능 말 ✗
#   점수 = 0.5 × 지금 수요 순위 백분위 + 0.3 × 살 마음 댓글 백분위 + 0.2 × 성공 사례 백분위 (⚖️ 판단 — 가중은 첫 판, 쿠팡 쪽 자료가 붙으면 다시 정함)
#   결과: shopping/result/items/item_scan.md · .csv
#   2단계(쿠팡 쪽 — 가격·리뷰 수·별점·로켓배송·파트너스 링크)는 쿠팡 파트너스 오픈 API 키가 있어야 함 (shopping/guides/item_select.md).
# ※ 연구·교육용 — 구매 권유가 아니다.
"""물건 후보 찾기 — python3 shopping/source/item_scan.py [--recent-days 90] [--log-level INFO]

  시험: python3 shopping/source/item_scan.py --selftest
"""
import argparse
import csv
import json
import logging
import re
import statistics
import sys
from datetime import datetime, timezone
from pathlib import Path

VERSION = "v0.1.1"
ROOT = Path(__file__).resolve().parents[2]
TOPIC = ROOT / "shopping"
LOG = logging.getLogger("item_scan")

# 물건 이름 사전 — 표기 여럿은 '|' (정규식). 갈래는 4050 여성이 쿠팡에서 많이 사는 쪽 (guides/channel.md 1번).
# ⚖️ 판단: 뜻이 둘인 말은 앞뒤 말로 좁힘 (쿠션 = 화장품 쿠션만, 가방 = 그대로).
ITEMS = {
    "주방": {
        "에어프라이어": "에어\\s?프라이어", "채칼": "채칼", "스텐팬": "스텐\\s?팬|스테인리스\\s?팬|스텐\\s?프라이팬", "프라이팬": "프라이팬|후라이팬",
        "냄비": "냄비", "밀폐용기": "밀폐\\s?용기|보관\\s?용기|반찬\\s?통|유리\\s?용기", "도마": "도마", "칼": "식칼|주방\\s?칼|과도",
        "수세미": "수세미", "행주": "행주", "고무장갑": "고무\\s?장갑", "식기건조대": "식기\\s?건조대|설거지\\s?건조대", "전자레인지 용기": "전자레인지\\s?(용기|찜기)|찜기",
        "텀블러": "텀블러|보온병", "그릇": "그릇|접시|식기", "믹서기": "믹서기|블렌더|초퍼", "전기포트": "전기\\s?포트|커피\\s?포트", "밥솥": "밥솥",
        "김장 용품": "김장\\s?(매트|봉투|용품)|절임\\s?배추", "랩·지퍼백": "지퍼\\s?백|위생\\s?(봉투|백)|랩\\b",
    },
    "청소·세탁": {
        "물걸레 청소기": "물걸레|스팀\\s?청소기", "무선 청소기": "무선\\s?청소기|청소기", "로봇청소기": "로봇\\s?청소기", "세제": "세제|섬유\\s?유연제",
        "곰팡이 제거제": "곰팡이|락스", "청소포": "청소포|부직포", "빨래 건조대": "빨래\\s?건조대|건조대", "건조기": "건조기", "세탁망": "세탁망",
        "욕실 청소": "욕실\\s?(청소|솔)|변기\\s?(솔|청소)|화장실\\s?청소", "먼지떨이": "먼지\\s?떨이|정전기\\s?(청소|먼지)",
    },
    "수납·정리": {
        "수납함": "수납\\s?(함|박스|바구니|용품)|정리\\s?(함|박스|바구니)", "옷걸이": "옷걸이|논슬립\\s?옷걸이", "행거": "행거", "선반": "선반|스탠드\\s?선반",
        "압축팩": "압축\\s?(팩|봉투)", "서랍장": "서랍장|서랍\\s?정리", "냉장고 정리": "냉장고\\s?(정리|수납)", "신발장 정리": "신발\\s?(정리|수납)",
    },
    "생활·겨울": {
        "가습기": "가습기", "전기요": "전기\\s?요|전기\\s?장판|온수\\s?매트|탄소\\s?매트", "난방 용품": "난방|뽁뽁이|문풍지|외풍", "전기히터": "히터|온풍기",
        "이불": "이불|극세사|차렵", "수면 양말": "수면\\s?양말", "손난로": "손\\s?난로|핫팩", "슬리퍼": "슬리퍼|실내화", "우산": "우산", "캐리어": "캐리어|여행\\s?가방",
    },
    "4050 패션": {
        "경량패딩": "경량\\s?패딩", "패딩": "패딩|다운\\s?점퍼", "니트": "니트|스웨터", "청바지": "청바지|데님", "슬랙스": "슬랙스|정장\\s?바지",
        "운동화": "운동화|스니커즈", "로퍼": "로퍼|구두", "가방": "가방|백팩|숄더\\s?백|토트\\s?백", "스카프": "스카프|머플러|목도리", "코트": "코트",
        "가디건": "가디건", "레깅스": "레깅스", "기모 바지": "기모\\s?(바지|팬츠)|융털", "내복·발열내의": "내복|발열\\s?내의|히트텍",
    },
    "4050 뷰티": {
        "쿠션": "쿠션\\s?(팩트|파운데이션)?(?=.{0,6}(화장|피부|커버|메이크업))|쿠션\\s?팩트", "선크림": "선크림|썬크림|선블록", "수분크림": "수분\\s?크림|보습\\s?크림",
        "레티놀": "레티놀", "앰플·세럼": "앰플|세럼|에센스", "클렌징": "클렌징|클렌저|폼클", "샴푸": "샴푸", "헤어 드라이기": "드라이기|고데기|헤어\\s?드라이",
        "바디로션": "바디\\s?로션|바디\\s?크림", "립": "립스틱|틴트|립밤", "마스크팩": "마스크\\s?팩|시트\\s?마스크",
    },
    "식품·장보기": {
        "밀키트": "밀키트", "냉동식품": "냉동\\s?(식품|만두|볶음밥)", "간식": "간식|과자|디저트", "커피": "커피|캡슐", "견과류": "견과",
    },
    "건강·생활 보조": {
        "안마기": "안마기|마사지기|마사지\\s?건", "체중계": "체중계|인바디", "혈압계": "혈압계", "영양제": "영양제|비타민|유산균|오메가",
    },
}
# 효능 광고 규제 갈래 — 영상에서 효능(주름 개선·탈모 완화·혈압·관절·면역 등) 말 ✗ (guides/channel.md 3번 7)
CAUTION = {"레티놀", "앰플·세럼", "샴푸", "선크림", "영양제", "혈압계", "안마기", "곰팡이 제거제"}
CAUTION_NOTE = {"레티놀": "기능성 화장품 효능", "앰플·세럼": "기능성 화장품 효능", "샴푸": "탈모 완화 = 기능성",
                "선크림": "자외선 차단 = 기능성", "영양제": "건강기능식품", "혈압계": "의료기기", "안마기": "의료기기 비슷한 효능 말",
                "곰팡이 제거제": "생활화학제품 안전 표시"}
INTENT = re.compile(r"어디서|어디\s?꺼|어디\s?제품|제품명|모델명|브랜드|링크|구매\s?(처|링크)|사고\s?싶|살까|샀|사서|구입|주문|장바구니")
DAISO = re.compile(r"다이소")
SPAM = re.compile(r"https?://|www\.|카톡|카카오톡|텔레그램|문의\s?(주세요|하세요|환영)|제작합니다|최상급|레플|이미테이션|도매\s?문의")
PER_VIDEO_CAP = 5   # v0.1.1: 한 영상에서 물건마다 살 마음 댓글을 이만큼까지만 셈


def log(stage, level=logging.INFO, **kv):
    LOG.log(level, "[%s] [%s] %s", stage, datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S"),
            " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) and ' ' in v else v}" for k, v in kv.items()))


def compile_items():
    out = []
    for cat, d in ITEMS.items():
        for name, rx in d.items():
            out.append((cat, name, re.compile(rx, re.I)))
    return out


def pct_rank(values):
    """값 → 0~1 백분위 (같은 값은 같은 순위, 0 은 0)."""
    s = sorted(set(v for v in values if v > 0))
    pos = {v: (i + 1) / len(s) for i, v in enumerate(s)} if s else {}
    return [pos.get(v, 0.0) for v in values]


def scan(explore_rows, comment_iter, recent_days=90):
    items = compile_items()
    stat = {name: {"cat": cat, "videos": 0, "recent_videos": 0, "recent_vpd": 0.0, "views": [], "success": 0, "daiso": 0,
                   "intent": 0, "intent_raw": 0, "intent_videos": set(), "per_video": {}, "intent_likes": 0, "example": "", "example_vpd": -1.0, "quote": "", "quote_likes": -1}
            for cat, name, _ in items}
    rows = [r for r in explore_rows if r.get("relevant") and not r.get("short") and (r.get("minutes") or 0) >= 4]
    for r in rows:
        text = f"{r.get('title', '')} {r.get('tags', '') if isinstance(r.get('tags'), str) else ' '.join(r.get('tags') or [])}"
        for cat, name, rx in items:
            if not rx.search(text):
                continue
            s = stat[name]
            s["videos"] += 1
            s["views"].append(int(r.get("views") or 0))
            if r.get("reason") == "성공 사례" or r.get("success"):
                s["success"] += 1
            if DAISO.search(r.get("title", "")):
                s["daiso"] += 1
            if (r.get("age_days") or 9999) <= recent_days:
                s["recent_videos"] += 1
                s["recent_vpd"] += float(r.get("views_per_day") or 0)
                if float(r.get("views_per_day") or 0) > s["example_vpd"]:
                    s["example_vpd"], s["example"] = float(r.get("views_per_day") or 0), f"{r.get('title', '')[:60]} ({r.get('url', '')})"
    n_comments = n_intent = n_spam = 0
    for c in comment_iter:
        n_comments += 1
        t = c.get("text") or ""
        if c.get("creator") or not INTENT.search(t):
            continue
        if SPAM.search(t):
            n_spam += 1
            continue
        n_intent += 1
        vid = c.get("video") or "?"
        for cat, name, rx in items:
            if rx.search(t):
                s = stat[name]
                s["intent_raw"] += 1
                s["per_video"][vid] = s["per_video"].get(vid, 0) + 1
                if s["per_video"][vid] > PER_VIDEO_CAP:
                    continue
                s["intent"] += 1
                s["intent_videos"].add(vid)
                s["intent_likes"] += int(c.get("likes") or 0)
                if int(c.get("likes") or 0) > s["quote_likes"]:
                    s["quote_likes"], s["quote"] = int(c.get("likes") or 0), re.sub(r"\s+", " ", t)[:80]
    names = list(stat)
    d_rank = pct_rank([stat[n]["recent_vpd"] for n in names])
    i_rank = pct_rank([len(stat[n]["intent_videos"]) for n in names])   # v0.1.1: 영상 수
    s_rank = pct_rank([stat[n]["success"] for n in names])
    for n, a, b, c in zip(names, d_rank, i_rank, s_rank):
        stat[n]["score"] = round(100 * (0.5 * a + 0.3 * b + 0.2 * c), 1)
        stat[n]["median_views"] = int(statistics.median(stat[n]["views"])) if stat[n]["views"] else 0
        stat[n]["daiso_share"] = (stat[n]["daiso"] / stat[n]["videos"]) if stat[n]["videos"] else 0.0
        stat[n]["caution"] = CAUTION_NOTE.get(n, "") if n in CAUTION else ""
        stat[n]["intent_vids"] = len(stat[n]["intent_videos"])
        stat[n]["top_share"] = (max(stat[n]["per_video"].values()) / stat[n]["intent_raw"]) if stat[n]["intent_raw"] else 0.0
    meta = {"rows": len(rows), "comments": n_comments, "intent_comments": n_intent, "spam": n_spam, "recent_days": recent_days, "items": len(names)}
    return stat, meta


def iter_comments(outliers):
    for f in sorted(outliers.glob("W_*/comments.jsonl")):
        vid = f.parent.name[2:]
        with f.open(encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if line:
                    try:
                        c = json.loads(line)
                    except ValueError:
                        continue
                    c.setdefault("video", vid)
                    yield c


def write(stat, meta, out_dir):
    out_dir.mkdir(parents=True, exist_ok=True)
    order = sorted(stat, key=lambda n: (-stat[n]["score"], -stat[n]["recent_vpd"]))
    with (out_dir / "item_scan.csv").open("w", encoding="utf-8-sig", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["순위", "갈래", "물건", "점수", "최근 영상", "최근 하루 조회수 합", "영상(1년)", "조회수 가운데값", "성공 사례", "살 마음 댓글 영상 수", "살 마음 댓글(영상당 5개까지)", "살 마음 댓글(전부)", "한 영상 몫", "다이소 몫", "조심", "가장 많이 본 최근 영상", "살 마음 댓글 예"])
        for i, n in enumerate(order, 1):
            s = stat[n]
            w.writerow([i, s["cat"], n, s["score"], s["recent_videos"], round(s["recent_vpd"]), s["videos"], s["median_views"], s["success"],
                        s["intent_vids"], s["intent"], s["intent_raw"], f"{s['top_share']:.0%}", f"{s['daiso_share']:.0%}", s["caution"], s["example"], s["quote"]])
    L = [f"# 물건 후보 — 유튜브 수요 쪽 (`shopping/source/item_scan.py` {VERSION})", "",
         f"만든 때 {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M')}Z · 할당량 0 (이미 받은 자료만) · 탐색 목록 관련 롱폼 {meta['rows']:,}개 · "
         f"승인 영상 시청자 댓글 {meta['comments']:,}개 중 살 마음 낱말이 든 {meta['intent_comments']:,}개 (광고·도배 {meta['spam']:,}개 뺌) · 물건 사전 {meta['items']}개",
         "", "**읽는 법** — 점수 = 0.5 × 최근 {0}일 하루 조회수 합 순위 + 0.3 × 살 마음 댓글이 나온 영상 수 순위 + 0.2 × 성공 사례 순위 (백분위, 100 점 만점 — ⚖️ 첫 판 가중). "
         "숫자는 검색 순위로 모은 목록이라 잘된 쪽으로 치우침 — 물건끼리 견주는 데만 쓴다. **다이소 몫**이 높으면 다이소 물건 영상이 대부분 → 쿠팡 수수료가 안 나올 수 있어 '다이소 vs 쿠팡' 비교로. "
         "**조심** = 효능 광고 규제 갈래 (영상에서 효능 말 ✗). 이 표는 후보일 뿐 — 쿠팡 쪽(가격·리뷰·로켓배송)은 2단계에서.".format(meta["recent_days"]), "",
         "| # | 물건 | 갈래 | 점수 | 최근 영상 · 하루 조회수 합 | 성공 사례 | 살 마음 댓글 (영상 수 · 댓글) | 다이소 몫 | 조심 |", "|---|---|---|---|---|---|---|---|---|"]
    for i, n in enumerate(order[:40], 1):
        s = stat[n]
        if s["videos"] == 0 and s["intent"] == 0:
            continue
        L.append(f"| {i} | **{n}** | {s['cat']} | {s['score']} | {s['recent_videos']} · {s['recent_vpd']:,.0f} | {s['success']} | {s['intent_vids']} · {s['intent']} | "
                 f"{s['daiso_share']:.0%} | {s['caution'] or '–'} |")
    L += ["", "## 물건마다 — 가장 많이 본 최근 영상 · 살 마음 댓글 (상위 15)", ""]
    for n in order[:15]:
        s = stat[n]
        L.append(f"- **{n}** — 영상: {s['example'] or '근거 없음'} · 댓글(👍{max(s['quote_likes'], 0)}): \"{s['quote'] or '근거 없음'}\"")
    zero = [n for n in order if stat[n]["videos"] == 0 and stat[n]["intent"] == 0]
    if zero:
        L += ["", f"자료에 한 번도 안 나온 물건 ({len(zero)}): " + " · ".join(zero)]
    (out_dir / "item_scan.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    return order


def selftest():
    rows = [{"relevant": True, "short": False, "minutes": 8, "title": "다이소 채칼 사지 마세요", "views": 200000, "views_per_day": 5000, "age_days": 30, "reason": "성공 사례", "url": "u1"},
            {"relevant": True, "short": False, "minutes": 9, "title": "에어프라이어 vs 오븐", "views": 100000, "views_per_day": 1000, "age_days": 200, "reason": "", "url": "u2"},
            {"relevant": False, "short": False, "minutes": 9, "title": "채칼 노래", "views": 9, "views_per_day": 9, "age_days": 1, "url": "u3"}]
    comments = [{"text": "그 채칼 어디서 사요?", "likes": 3}, {"text": "채칼 좋네요", "likes": 9}, {"text": "에어프라이어 제품명 알려주세요", "likes": 1, "creator": True}]
    stat, meta = scan(rows, iter(comments), recent_days=90)
    assert stat["채칼"]["videos"] == 1 and stat["채칼"]["success"] == 1 and stat["채칼"]["daiso_share"] == 1.0, stat["채칼"]
    assert stat["채칼"]["intent"] == 1, "살 마음 낱말 없는 댓글·관련 없는 영상은 세지 않음"
    many = [{"text": f"채칼 어디서 사요 {i}", "video": "V1"} for i in range(9)] + [{"text": "채칼 링크 http://spam", "video": "V2"}]
    st2, m2 = scan(rows, iter(many))
    assert st2["채칼"]["intent"] == PER_VIDEO_CAP and st2["채칼"]["intent_vids"] == 1 and m2["spam"] == 1, (st2["채칼"]["intent"], m2)
    assert stat["에어프라이어"]["recent_videos"] == 0 and stat["에어프라이어"]["intent"] == 0, "90일 밖·채널 주인 댓글은 뺌"
    assert stat["채칼"]["score"] > stat["에어프라이어"]["score"]
    print("[SELFTEST] ok — 채칼 점수", stat["채칼"]["score"], "> 에어프라이어", stat["에어프라이어"]["score"])


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--recent-days", type=int, default=90)
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    logging.basicConfig(level=a.log_level, format="%(message)s")
    if a.selftest:
        selftest()
        return 0
    t0 = datetime.now(timezone.utc)
    ex = TOPIC / "result" / "web" / "explore.json"
    try:
        rows = json.loads(ex.read_text("utf-8"))["rows"]
    except (OSError, ValueError, KeyError) as e:
        log("LOAD", logging.ERROR, file=str(ex), error=repr(e), next="python3 tools/cloud_run.py shopping explore --weeks 26 를 먼저")
        return 1
    log("LOAD", file=str(ex.relative_to(ROOT)), rows=len(rows), tool=f"item_scan.py {VERSION}")
    stat, meta = scan(rows, iter_comments(TOPIC / "result" / "outliers"), recent_days=a.recent_days)
    log("SCAN", **meta, weights="demand0.5/intent0.3/success0.2")
    order = write(stat, meta, TOPIC / "result" / "items")
    log("TOP", items=",".join(f"{n}:{stat[n]['score']}" for n in order[:10]))
    log("DONE", out="shopping/result/items/item_scan.md", seconds=round((datetime.now(timezone.utc) - t0).total_seconds(), 1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
