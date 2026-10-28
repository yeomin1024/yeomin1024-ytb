#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-28 — 새로: 분석 대상 세 묶음 확인 엑셀. 사용자 지시 2026-10-28 "아래 처럼 분석하고 있는지 확인하고 내가 확인할 수 있는
#          엑셀 파일 생성해 / 분석 대상(롱폼, 쇼츠 종합) — 구독자에 비해 업로드 대비 조회수가 높은 영상 (성공 사례) · 구독자 상관 없이 업로드 대비
#          조회수가 높은 영상 (최근 트렌드) · 업로드 기간 상관없이 조회수가 높은 영상 (최근 트렌드에 비슷한 과거 사례)".
#          · 분석 코드(success_analysis·shorts_analysis 의 analyze — 파일을 쓰지 않음)를 그대로 불러 같은 모집단·같은 규칙으로 셈 → 묶음마다
#            '기준 통과 / 자료 받음(승인) / 분석 묶음에 듦' 과 빠진 점. 지금 분석에 없는 묶음(쇼츠 하루 조회수 상위·조회수 상위)도 같은 꼴(상위 N%)로
#            세어 '분석 묶음 없음' 으로 보임 — 분석 결과(analysis.md)는 바꾸지 않음.
#          · 엑셀: 안내 · 확인 결과 · 모집단 · ①성공 사례 · ②최근 트렌드 · ③조회수 상위 · 겹침 · 전체 목록 (롱폼·쇼츠 한 표, '형식' 칸). 할당량 0.
#          ※ 연구·교육용 — 투자 권유가 아님.
"""분석 대상 세 묶음 확인 — 롱폼·쇼츠 종합 엑셀

  python3 tools/target_check.py stock            # stock/result/outliers/target_check.xlsx (+ .md 요약)
  python3 tools/target_check.py stock --pct 10   # ②·③ 상위 몇 % (기본 = analysis_rules.toml [vpd_top] TOP_PCT)
"""
import argparse
import json
import logging
import sys
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import outlier_research as orr        # noqa: E402  top_pct_threshold (웹 화면 추천·분석 1-3번과 같은 경계)
import shorts_analysis as sha         # noqa: E402
import success_analysis as sa         # noqa: E402

VERSION = "v1.0"
ROOT = Path(__file__).resolve().parent.parent
LOG = logging.getLogger("tchk")
G1, G2, G3 = "① 성공 사례", "② 최근 트렌드", "③ 조회수 상위"
LONG, SHORT = "롱폼", "쇼츠"


def log(stage, level=logging.INFO, **kv):
    LOG.log(level, "[%s] [%s] %s", stage, datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S"),
            " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) and (' ' in v or not v) else v}" for k, v in kv.items()))


# ---------------------------------------------------------------- 자료 (분석 코드 그대로 — 파일은 쓰지 않음)
def load_long(topic, now):
    out = ROOT / topic / "result" / "outliers"
    rules, rel, themes = sa.load_rules(ROOT, topic), sa.load_rel(ROOT, topic), sa.load_themes(ROOT, topic)
    cache_infos, cache_subs = sa.load_cache(out)
    cases = sa.load_cases(out, cache_infos, cache_subs, now)
    mc = sa.load_market_caches(out)
    data, success, _group, rows_all, cases = sa.analyze(topic, topic, cases, cache_infos, cache_subs, rules, rel, themes, now, mc, sa.load_uploads(out))
    searched = {i for d in (mc[0] or ()) for i in (d.get("ids") or [])}
    return {"rules": rules, "data": data, "success": success, "rows": rows_all, "cases": cases, "searched": searched,
            "fetched": {k: v.get("fetched") for k, v in cache_infos.items()}}


def load_shorts(topic, now):
    out_all = ROOT / topic / "result" / "outliers"
    sdir, cache = sha.shorts_out(ROOT, topic), sha.shorts_cache(ROOT, topic)
    rules, rel, themes = sha.load_rules(ROOT, topic), sa.load_rel(ROOT, topic), sa.load_themes(ROOT, topic)
    infos, uploads, searches = sha.load_shorts_cache(cache)
    if not infos:
        return None
    channels, ac = sha.load_main_cache(out_all)
    subs_map = {k: v.get("subs") for k, v in channels.items()}
    known = {i for u in uploads.values() for i in u["ids"]}
    cases = sha.load_cases(sdir, infos, subs_map, now, known)
    data, success, _group, rows_all, cases = sha.analyze(topic, topic, cases, infos, uploads, searches, channels, ac, rules, rel, themes, now)
    searched = {i for d in searches for i in (d.get("ids") or [])}
    return {"rules": rules, "data": data, "success": success, "rows": rows_all, "cases": cases, "searched": searched,
            "fetched": {k: v.get("fetched") for k, v in infos.items()}}


def parse_dt(s):
    try:
        d = datetime.fromisoformat(str(s).replace("Z", "+00:00"))
        return d if d.tzinfo else d.replace(tzinfo=timezone.utc)
    except (TypeError, ValueError):
        return None


def vpd_at_fetch(x, fetched):
    """하루 조회수(받은 때) = 받은 때 조회수 ÷ 올린 날부터 받은 때까지 날수 (최소 1일). 분석 코드의 하루 조회수는 ÷ 오늘까지 날수."""
    f, pub = parse_dt(fetched), x.get("published")
    if not (f and pub):
        return None
    return round(x["views"] / max((f - pub).total_seconds() / 86400, 1.0), 1)


def explore_meta(topic):
    """탐색 목록(웹 화면·cloud_run explore)의 검색 기간·추천 까닭."""
    res = {}
    for fmt, name in ((LONG, "explore.json"), (SHORT, "shorts_explore.json")):
        p = ROOT / topic / "result" / "web" / name
        d = json.loads(p.read_text("utf-8")) if p.is_file() else {}
        res[fmt] = {"weeks": d.get("weeks"), "generated": d.get("generated"),
                    "reason": {r["id"]: r.get("reason") or "" for r in d.get("rows") or []}}
    return res


# ---------------------------------------------------------------- 묶음
def build(long, shorts, pct, meta):
    """두 형식 → 영상 줄 (묶음 표시·분석 상태) + 묶음 요약."""
    rows, summary = [], {}
    for fmt, src in ((LONG, long), (SHORT, shorts)):
        if not src:
            summary[fmt] = None
            continue
        R, data = src["rules"], src["data"]
        S = R["success"] if fmt == LONG else R["shorts"]
        is_success = sa.is_success if fmt == LONG else sha.is_success
        min_min = R["vpd_top"]["MIN_MINUTES"] if fmt == LONG else 0
        # 모집단 = 검색에서 찾은 주제 관련 영상 중 뺄 까닭 없는 것 (롱폼 = 분석 1-3번 vpool 과 같음 · 쇼츠 = 쇼츠인 것)
        pool = [x for x in src["rows"] if x["id"] in src["searched"] and not x["exclude"] and x.get("vpd") is not None
                and (x["minutes"] >= min_min if fmt == LONG else x.get("is_short"))]
        pool_ids = {x["id"] for x in pool}
        thr_vpd = orr.top_pct_threshold([x["vpd"] for x in pool], pct)
        thr_views = orr.top_pct_threshold([x["views"] for x in pool], pct)
        success_no = {c["id"]: c["no"] for c in src["success"]}
        vtop = data.get("vpd_top") or {}
        vno = {c["id"]: c["vno"] for c in vtop.get("cases") or []} if fmt == LONG else {}
        if fmt == LONG and vtop.get("threshold") is not None and thr_vpd is not None and abs(vtop["threshold"] - thr_vpd) > 0.5 and pct == R["vpd_top"]["TOP_PCT"]:
            log("GROUP", logging.WARNING, fmt=fmt, note="② 경계가 분석 결과와 다름", analysis=vtop["threshold"], here=thr_vpd)
        case_ids = {c["id"] for c in src["cases"]}
        reason = meta[fmt]["reason"]
        seen = set()
        for x in src["rows"]:
            g1 = (not x["exclude"]) and is_success(x, S)
            in_pool = x["id"] in pool_ids
            g2 = in_pool and thr_vpd is not None and x["vpd"] >= thr_vpd
            g3 = in_pool and thr_views is not None and x["views"] >= thr_views
            if not (in_pool or g1 or x["id"] in case_ids) or x["id"] in seen:
                continue
            seen.add(x["id"])
            has = x["id"] in case_ids
            st1 = (f"분석 #{success_no[x['id']]}" if x["id"] in success_no else ("자료 받음 · 채널당 {}개 넘어 묶음 밖".format(S["CASES_PER_CHANNEL"]) if has else "자료 안 받음")) if g1 else ""
            if fmt == LONG:
                st2 = (f"분석 V{vno[x['id']]}" if x["id"] in vno else ("자료 받음 · 채널당 {}개 넘어 묶음 밖".format(R["vpd_top"]["CASES_PER_CHANNEL"]) if has else "자료 안 받음")) if g2 else ""
            else:
                st2 = ("분석 묶음 없음 · 자료 받음" if has else "분석 묶음 없음 · 자료 안 받음") if g2 else ""
            st3 = ("분석 묶음 없음 · 자료 받음" if has else "분석 묶음 없음 · 자료 안 받음") if g3 else ""
            pub = x.get("published")
            subs = x.get("subs")
            fetched = src["fetched"].get(x["id"])
            vf = vpd_at_fetch(x, fetched)
            rows.append({"형식": fmt, "제목": x["title"], "링크": f"https://www.youtube.com/watch?v={x['id']}", "채널": x["channel"],
                         "구독자": subs, "조회수": x["views"], "올린 날": pub.date().isoformat() if pub else "",
                         "지난 날수": round(x["age_days"]) if x.get("age_days") is not None else None,
                         "하루 조회수": x["vpd"], "하루 조회수(받은 때)": vf, "받은 날": (parse_dt(fetched).date().isoformat() if parse_dt(fetched) else ""),
                         "배수(조회수÷구독자)": x.get("ratio"),
                         "구독자당 하루 조회수": round(x["vpd"] / max(subs, 100), 3) if subs is not None and x.get("vpd") is not None else None,
                         "길이(분)": round(x["minutes"], 1), "외국": "외국" if x.get("foreign") else "", "주제 묶음": x.get("theme") or "",
                         "어디서 봄": "검색" if x["id"] in src["searched"] else ("승인 자료" if has else "채널 평소 영상"),
                         "모집단(검색)": "○" if in_pool else "", "자료 받음": "○" if has else "",
                         G1: "○" if g1 else "", f"{G1} 분석": st1, G2: "○" if g2 else "", f"{G2} 분석": st2, G3: "○" if g3 else "", f"{G3} 분석": st3,
                         "탐색 추천 까닭": reason.get(x["id"], ""), "뺀 까닭": x.get("exclude") or "", "_id": x["id"]})
        mine = [r for r in rows if r["형식"] == fmt]
        ages = [x["age_days"] for x in pool if x.get("age_days") is not None]
        # 하루 조회수를 오늘까지 날수로 나눌 때 얼마나 낮아지나 (올린 지 30일 안 영상 — 받은 뒤 날이 지날수록 낮게 셈)
        young = [r for r in mine if r["모집단(검색)"] and r["하루 조회수(받은 때)"] and r["지난 날수"] is not None and r["지난 날수"] <= 30]
        shrink = sorted(r["하루 조회수"] / r["하루 조회수(받은 때)"] for r in young if r["하루 조회수(받은 때)"])
        thr_fetch = orr.top_pct_threshold([r["하루 조회수(받은 때)"] for r in mine if r["모집단(검색)"] and r["하루 조회수(받은 때)"]], pct)
        g2_fetch = {r["_id"] for r in mine if r["모집단(검색)"] and thr_fetch is not None and (r["하루 조회수(받은 때)"] or 0) >= thr_fetch}
        g2_now = {r["_id"] for r in mine if r[G2]}
        summary[fmt] = {
            "weeks": meta[fmt]["weeks"], "generated": meta[fmt]["generated"], "pool": len(pool), "rows": len(src["rows"]),
            "oldest": round(max(ages)) if ages else None, "older_180": sum(1 for a in ages if a > 180), "older_365": sum(1 for a in ages if a > 365),
            "thr_vpd": thr_vpd, "thr_views": thr_views, "pct": pct, "cases": len(case_ids),
            "rule1": (f"{S.get('MIN_AGE_DAYS', 0)}~{S['MAX_AGE_DAYS']}일 · 구독자 ≤ {S['MAX_SUBS']:,} · 조회수 ≥ 구독자 × {S['MIN_RATIO']:g} · 조회수 ≥ {S['MIN_VIEWS']:,}"
                      + (f" · {S['MIN_MINUTES']:g}분 이상" if fmt == LONG else f" · {S['MAX_SECONDS']}초 이하 세로") + f" · 채널당 {S['CASES_PER_CHANNEL']}개"),
            **{f"{g}_{k}": v for g, col in ((G1, G1), (G2, G2), (G3, G3)) for k, v in (
                ("pass", sum(1 for r in mine if r[col])), ("has", sum(1 for r in mine if r[col] and r["자료 받음"])),
                ("in", sum(1 for r in mine if r[f"{col} 분석"].startswith("분석 #") or r[f"{col} 분석"].startswith("분석 V"))))},
            "vpd_top_analysis": vtop if fmt == LONG else None,
            "g1_search": sum(1 for r in mine if r[G1] and r["어디서 봄"] != "채널 평소 영상"), "g1_uploads": sum(1 for r in mine if r[G1] and r["어디서 봄"] == "채널 평소 영상"),
            "last_fetch": max((r["받은 날"] for r in mine if r["받은 날"]), default=""),
            "young": len(young), "shrink_median": round(shrink[len(shrink) // 2], 2) if shrink else None,
            "thr_fetch": thr_fetch, "g2_fetch_only": len(g2_fetch - g2_now), "g2_now_only": len(g2_now - g2_fetch),
        }
        log("GROUP", fmt=fmt, pool=len(pool), oldest_days=summary[fmt]["oldest"], thr_vpd=thr_vpd, thr_views=thr_views,
            g1=f"{summary[fmt][G1 + '_pass']}/{summary[fmt][G1 + '_has']}/{summary[fmt][G1 + '_in']}",
            g2=f"{summary[fmt][G2 + '_pass']}/{summary[fmt][G2 + '_has']}/{summary[fmt][G2 + '_in']}",
            g3=f"{summary[fmt][G3 + '_pass']}/{summary[fmt][G3 + '_has']}/{summary[fmt][G3 + '_in']}", note="통과/자료 받음/분석 묶음",
            g1_from_uploads=summary[fmt]["g1_uploads"], last_fetch=summary[fmt]["last_fetch"], young30=summary[fmt]["young"],
            vpd_now_vs_fetch_median=summary[fmt]["shrink_median"], thr_fetch=thr_fetch,
            g2_changes=f"+{summary[fmt]['g2_fetch_only']}/-{summary[fmt]['g2_now_only']}")
    return rows, summary


def check_rows(summary, long_rules):
    """확인 결과 — 사용자 기준 × 형식 6줄."""
    out = []
    want = {G1: "구독자에 비해 업로드 대비 조회수가 높은 영상", G2: "구독자 상관없이 업로드 대비 조회수가 높은 영상", G3: "업로드 기간 상관없이 조회수가 높은 영상"}
    for g in (G1, G2, G3):
        for fmt in (LONG, SHORT):
            s = summary.get(fmt)
            if not s:
                out.append({"분석 대상": g, "형식": fmt, "사용자 기준": want[g], "판정": "❌ 자료 없음"})
                continue
            p, h, i = s[f"{g}_pass"], s[f"{g}_has"], s[f"{g}_in"]
            if g == G1:
                rule, where = s["rule1"], ("analysis.md 1번" if fmt == LONG else "shorts/analysis.md 1번")
                verdict = "⚠️ 들어감 · 기준 한 곳 다름"
                gap = ("'업로드 대비' 를 날수로 나누지 않음 — 지금은 조회수 ÷ 구독자 (180일 안이면 10일 된 영상과 170일 된 영상을 같은 잣대로 봄). "
                       "말씀대로라면 '구독자당 하루 조회수' (하루 조회수 ÷ 구독자) — 엑셀에 그 칸을 넣어 둠. 기준을 바꾸면 CLAUDE.md 지시사항 근거(성공 사례)도 바뀌어 사용자 결정 필요. "
                       f"기준 통과 {p}개 = 검색·승인 자료 {s['g1_search']} + 채널 평소 영상(같은 채널 기준선으로만 본 것) {s['g1_uploads']} — 자료를 안 받은 {p - h}개는 분석에 없음.")
                fix = "기준을 바꿀지 결정 (할당량 0 — 다시 분석만)"
            elif g == G2 and fmt == LONG:
                rule = f"검색에서 찾은 주제 관련 롱폼(4분 이상) 안 하루 조회수 상위 {s['pct']:g}% (경계 {s['thr_vpd']:,.0f}회/일) · 채널당 {long_rules['vpd_top']['CASES_PER_CHANNEL']}개"
                where, verdict = "analysis.md 1-3번 (성공 사례와 따로)", "✅ 들어감"
                gap = ((f"기준 통과 {p}개 중 자료를 안 받은 {p - h}개는 분석에 없음 (탐색 추천 목록에는 있음 — 승인하면 들어감). " if p - h else "")
                       + f"⚠️ 하루 조회수 = 받은 때 조회수 ÷ 오늘까지 날수 — 마지막으로 받은 날 {s['last_fetch']}, 올린 지 30일 안 영상은 받은 때 기준보다 "
                       f"중앙값 ×{s['shrink_median']} 로 낮게 셈 → 받은 때 기준이면 이 묶음에 +{s['g2_fetch_only']}개·-{s['g2_now_only']}개 (탐색을 다시 돌리면 새로 받음).")
                fix = "남은 추천 승인 (댓글 받기 — 영상당 몇 단위)" if p - h else ""
            elif g == G2:
                rule = f"(분석에는 없음) 여기서 같은 꼴로 셈: 검색에서 찾은 주제 관련 쇼츠 안 하루 조회수 상위 {s['pct']:g}% (경계 {s['thr_vpd']:,.0f}회/일)"
                where, verdict = "없음 — 탐색 추천도 없음 (쇼츠 추천 = 성공 쇼츠·조회수 상위 20)", "❌ 빠짐"
                gap = (f"쇼츠에는 하루 조회수 상위 묶음이 없음. 기준 통과 {p}개 중 다른 까닭으로 자료를 받은 것 {h}개. "
                       f"(쇼츠 자료를 마지막으로 받은 날 {s['last_fetch']} — 오늘까지 날수로 나눠 30일 안 쇼츠는 중앙값 ×{s['shrink_median']})")
                fix = "쇼츠 추천·분석에 롱폼과 같은 규칙 더하기 (코드 — 할당량 0) + 추천 승인 (댓글 받기)"
            else:
                rule = (f"(분석에는 없음) 여기서 셈: 모집단 안 조회수 상위 {s['pct']:g}% (경계 {s['thr_views']:,.0f}회). "
                        f"탐색 추천 '조회수 상위' = 조회수 상위 20개만 (분석 묶음은 아님)")
                where, verdict = "없음 — 승인하면 '그 밖의 승인 영상' 으로만 섞임", "❌ 빠짐 (기간도 막힘)"
                gap = (f"검색이 최근 {s['weeks']}주로 막혀 있음 (YouTube 검색 publishedAfter) — 모집단에서 가장 오래된 영상 {s['oldest']}일 · "
                       f"1년 넘은 영상 {s['older_365']}개 → '기간 상관없는 과거 사례' 를 찾지 못함. 따로 묶는 분석도 없음.")
                fix = ("기간 없는 검색(검색어마다 조회수 순 — 롱폼·쇼츠 검색어 수 × 100단위) + 따로 묶는 분석 (코드). "
                       "할당량이 하루 10,000 을 넘을 수 있음 — 사용자 결정")
            out.append({"분석 대상": g, "형식": fmt, "사용자 기준": want[g], "지금 규칙": rule, "기준 통과 (모집단·자료 안)": p, "자료 받음 (승인)": h,
                        "분석 묶음에 듦": i if not (g == G2 and fmt == SHORT) and g != G3 else 0, "분석 결과 위치": where, "판정": verdict,
                        "다른 점·빠진 것": gap, "고치려면": fix})
    return out


def pool_rows(summary):
    out = []
    for fmt in (LONG, SHORT):
        s = summary.get(fmt)
        if not s:
            continue
        out.append({"형식": fmt, "검색 기간(주)": s["weeks"], "탐색 목록 만든 때": s["generated"], "모집단(검색·주제 관련·뺄 까닭 없음)": s["pool"],
                    "분석에 쓴 영상 전부(채널 평소 영상 포함)": s["rows"], "자료 받은 영상(승인)": s["cases"], "모집단에서 가장 오래된 영상(일)": s["oldest"],
                    "180일 넘은 영상": s["older_180"], "1년 넘은 영상": s["older_365"], f"② 경계 하루 조회수(상위 {s['pct']:g}%)": s["thr_vpd"],
                    f"③ 경계 조회수(상위 {s['pct']:g}%)": s["thr_views"]})
    return out


def overlap_rows(rows):
    out = []
    for fmt in (LONG, SHORT):
        mine = [r for r in rows if r["형식"] == fmt]
        if not mine:
            continue
        c = Counter((bool(r[G1]), bool(r[G2]), bool(r[G3])) for r in mine)
        for (a, b, d), n in sorted(c.items(), key=lambda kv: -kv[1]):
            if not (a or b or d):
                continue
            out.append({"형식": fmt, G1: "○" if a else "", G2: "○" if b else "", G3: "○" if d else "", "영상 수": n})
    return out


# ---------------------------------------------------------------- 엑셀
FMT_INT = ("구독자", "조회수", "하루 조회수", "지난 날수", "기준 통과 (모집단·자료 안)", "자료 받음 (승인)", "분석 묶음에 듦", "영상 수", "180일 넘은 영상",
           "1년 넘은 영상", "자료 받은 영상(승인)", "모집단(검색·주제 관련·뺄 까닭 없음)", "분석에 쓴 영상 전부(채널 평소 영상 포함)", "모집단에서 가장 오래된 영상(일)")


def write_xlsx(path, sheets, guide):
    import pandas as pd
    from openpyxl.styles import Alignment, Font, PatternFill
    from openpyxl.utils import get_column_letter
    with pd.ExcelWriter(path, engine="openpyxl") as xw:
        pd.DataFrame({"안내": guide}).to_excel(xw, sheet_name="안내", index=False)
        for name, rows in sheets:
            pd.DataFrame(rows).to_excel(xw, sheet_name=name, index=False)
        wb = xw.book
        fill, wrap = PatternFill("solid", fgColor="DDEBF7"), Alignment(wrap_text=True, vertical="top")
        for ws in wb.worksheets:
            ws.freeze_panes = "A2"
            if ws.max_row > 1 and ws.title != "안내":
                ws.auto_filter.ref = ws.dimensions
            for cell in ws[1]:
                cell.font, cell.fill, cell.alignment = Font(bold=True), fill, wrap
            for col in range(1, ws.max_column + 1):
                name = str(ws.cell(row=1, column=col).value or "")
                wide = name in ("안내", "제목", "지금 규칙", "다른 점·빠진 것", "고치려면", "사용자 기준", "분석 결과 위치") or name.endswith(" 분석")
                ws.column_dimensions[get_column_letter(col)].width = (70 if name in ("안내", "다른 점·빠진 것", "지금 규칙") else 45 if wide else
                                                                      max(9, min(22, len(name) * 2 + 2)))
                fmt = ("#,##0" if name in FMT_INT or name.startswith("② 경계") or name.startswith("③ 경계") else
                       "0.00" if name == "배수(조회수÷구독자)" else "0.000" if name == "구독자당 하루 조회수" else None)
                if not (fmt or wide or name == "링크"):
                    continue
                for (c,) in ws.iter_rows(min_row=2, min_col=col, max_col=col):
                    if fmt:
                        c.number_format = fmt
                    if wide:
                        c.alignment = wrap
                    if name == "링크" and c.value:
                        c.hyperlink, c.font = c.value, Font(color="0563C1", underline="single")
    log("XLSX", file=str(path), sheets=len(sheets) + 1, kb=round(path.stat().st_size / 1024))


def write_md(path, checks, pools, now):
    L = [f"# 분석 대상 세 묶음 확인 (`tools/target_check.py` {VERSION} · {now.date().isoformat()}) — 자세한 영상 목록은 `target_check.xlsx`", "",
         "※ 연구·교육용 — 투자 권유가 아님. 숫자 = 기준 통과 / 자료 받음(승인) / 분석 묶음에 듦.", "",
         "| 분석 대상 | 형식 | 판정 | 통과 / 자료 / 분석 | 다른 점·빠진 것 |", "|---|---|---|---|---|"]
    for r in checks:
        L.append(f"| {r['분석 대상']} | {r['형식']} | {r['판정']} | {r.get('기준 통과 (모집단·자료 안)', '-')} / {r.get('자료 받음 (승인)', '-')} / "
                 f"{r.get('분석 묶음에 듦', '-')} | {str(r.get('다른 점·빠진 것', '')).replace('|', '∣')} |")
    L += ["", "| 형식 | 검색 기간 | 모집단 | 가장 오래된 영상 | ② 경계 하루 조회수 | ③ 경계 조회수 |", "|---|---|---|---|---|---|"]
    for p in pools:
        k2 = next(k for k in p if k.startswith("② 경계"))
        k3 = next(k for k in p if k.startswith("③ 경계"))
        L.append(f"| {p['형식']} | {p['검색 기간(주)']}주 | {p['모집단(검색·주제 관련·뺄 까닭 없음)']:,} | {p['모집단에서 가장 오래된 영상(일)']}일 | "
                 f"{p[k2] or 0:,.0f} | {p[k3] or 0:,.0f} |")
    path.write_text("\n".join(L) + "\n", "utf-8")


def run(topic, pct=None, now=None, out_path=None):
    now = now or datetime.now(timezone.utc)
    t0 = time.time()
    long = load_long(topic, now)
    shorts = load_shorts(topic, now)
    pct = pct if pct is not None else long["rules"]["vpd_top"]["TOP_PCT"]
    meta = explore_meta(topic)
    log("LOAD", topic=topic, long_rows=len(long["rows"]), long_cases=len(long["cases"]), shorts_rows=len(shorts["rows"]) if shorts else 0,
        shorts_cases=len(shorts["cases"]) if shorts else 0, long_weeks=meta[LONG]["weeks"], shorts_weeks=meta[SHORT]["weeks"], pct=pct,
        seconds=round(time.time() - t0, 1))
    rows, summary = build(long, shorts, pct, meta)
    checks, pools = check_rows(summary, long["rules"]), pool_rows(summary)
    order = {LONG: 0, SHORT: 1}
    def pick(col, key):
        return [{k: v for k, v in r.items() if k != "_id"} for r in sorted((r for r in rows if r[col]), key=lambda r: (order[r["형식"]], -(r[key] or 0)))]
    sheets = [("확인 결과", checks), ("모집단", pools),
              ("① 성공 사례", pick(G1, "배수(조회수÷구독자)")), ("② 최근 트렌드", pick(G2, "하루 조회수")), ("③ 조회수 상위", pick(G3, "조회수")),
              ("겹침", overlap_rows(rows)),
              ("전체 목록", [{k: v for k, v in r.items() if k != "_id"} for r in sorted(rows, key=lambda r: (order[r["형식"]], -(r["하루 조회수"] or 0)))])]
    out = ROOT / topic / "result" / "outliers"
    out_path = Path(out_path) if out_path else out / "target_check.xlsx"
    guide = [
        f"자동 생성 — tools/target_check.py {VERSION} ({now.isoformat(timespec='minutes')}). 연구·교육용 — 투자 권유가 아님. 할당량 0 (받아 둔 자료만).",
        "사용자 지시 (2026-10-28): 분석 대상(롱폼·쇼츠 종합) ① 구독자에 비해 업로드 대비 조회수가 높은 영상(성공 사례) ② 구독자 상관없이 업로드 대비 조회수가 높은 영상"
        "(최근 트렌드) ③ 업로드 기간 상관없이 조회수가 높은 영상(최근 트렌드에 비슷한 과거 사례) — 이렇게 분석하고 있는지 확인.",
        "셈하는 법: 분석 코드(success_analysis·shorts_analysis)를 그대로 불러 같은 모집단·같은 규칙으로 셈 — 분석 결과 파일은 바꾸지 않음.",
        "모집단 = 탐색 검색에서 찾은 주제 관련 영상 중 뺄 까닭(라이브·주제 밖·광고 의심·쇼츠 부풀림 의심 등)이 없는 것. 롱폼은 4분 이상, 쇼츠는 쇼츠인 것.",
        "① = 지금 성공 사례 규칙 그대로 (확인 결과 시트 '지금 규칙'). ② = 하루 조회수(조회수 ÷ 올린 지 날수) 상위 N% — 롱폼은 분석 1-3번과 같음, "
        "쇼츠는 분석에 없어 같은 꼴로 여기서 셈. ③ = 조회수 상위 N% (분석에 없어 여기서 셈).",
        "'○' = 기준 통과. '… 분석' 칸: '분석 #n' = analysis.md 성공 사례 n번 · '분석 V n' = 1-3번 하루 조회수 상위 n번 · '자료 받음 · 채널당 2개 넘어 묶음 밖' · "
        "'자료 안 받음' (승인하지 않아 설명·댓글이 없음) · '분석 묶음 없음' (그런 묶음이 분석에 없음).",
        "구독자당 하루 조회수 = 하루 조회수 ÷ 구독자(100 미만은 100) — ① 의 '업로드 대비' 를 날수로 나눈 잣대 (지금 성공 사례 규칙은 이것이 아니라 조회수 ÷ 구독자).",
        "하루 조회수 = 분석 코드와 같이 받은 때 조회수 ÷ 오늘까지 날수 (그래서 오늘 다시 세면 analysis.md 를 만든 날과 숫자가 조금 다름). 하루 조회수(받은 때) = ÷ 받은 날까지 날수 — "
        "자료를 받은 지 오래된 최근 영상은 앞의 값이 낮게 나옴 (확인 결과 ② 롱폼 줄). 어디서 봄 = 검색 · 승인 자료 · 채널 평소 영상(같은 채널 기준선으로 받은 최근 영상).",
        "탐색 추천 까닭 = 탐색 목록이 체크해 둔 까닭 (성공 사례 · 하루 조회수 상위 · 조회수 상위(상위 20) · 성공 쇼츠).",
        "한계: 조회수·구독자는 받은 때 값. 검색은 YouTube 검색 결과(조회수 순·검색어마다 최대 50개)라 모든 영상이 아님. 검색 기간 밖(모집단 시트)은 볼 수 없음.",
        f"다시 만들기: python3 tools/target_check.py {topic}" + (f" --pct {pct:g}" if pct != long["rules"]["vpd_top"]["TOP_PCT"] else ""),
    ]
    write_xlsx(out_path, sheets, guide)
    write_md(out_path.with_suffix(".md"), checks, pools, now)
    log("DONE", seconds=round(time.time() - t0, 1), xlsx=str(out_path), rows=len(rows),
        verdict=" | ".join(f"{r['분석 대상'][:1]}{r['형식']}={r['판정']}" for r in checks))
    return {"xlsx": str(out_path), "checks": checks, "pools": pools, "rows": len(rows)}


def main(argv=None):
    ap = argparse.ArgumentParser(description="분석 대상 세 묶음(성공 사례·최근 트렌드·조회수 상위) 확인 엑셀 — 롱폼·쇼츠 종합 (할당량 0)")
    ap.add_argument("topic")
    ap.add_argument("--pct", type=float, default=None, help="②·③ 상위 몇 %% (기본 = analysis_rules.toml [vpd_top] TOP_PCT)")
    ap.add_argument("--out", default="", help="엑셀 경로 (기본 <주제>/result/outliers/target_check.xlsx)")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args(argv)
    logging.basicConfig(level=getattr(logging, a.log_level), format="%(message)s", stream=sys.stderr)
    log("START", topic=a.topic, pct=a.pct if a.pct is not None else "기본", tool=f"target_check.py {VERSION}")
    run(a.topic, pct=a.pct, out_path=a.out or None)


if __name__ == "__main__":
    main()
