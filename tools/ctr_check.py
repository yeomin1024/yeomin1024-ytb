#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.5 — 2026-11-12 — 성공 = 구독자당 하루 조회수 ≥ MIN_VPD_SUBS 그리고 조회수 ≥ [success] MIN_VIEWS (사용자 지시 2026-11-12 "조회수가 구독자수 대비가 높아도 조회수 별로 안나오면 성공사례에서 빼야해" — 성공 사례와 같은 잣대).
# (v1.4 — 2026-11-11 — validate: 제목 꼴 점수를 실제 성공으로 검증(5겹 교차 AUC · 앵커 빼고 배운 점수로 실제 성공·덜 된 영상 가름) · 판정 mode "title+trust" = 클릭은 검증된 제목 점수로, 페르소나는 믿음·고증 거름으로 (10회차 — 패널 v2 도 H 6.16 < M 6.75, 페르소나 클릭 점수는 두 판 모두 실제 결과를 못 가림).)
# (v1.3 — 2026-11-11 — 패널 v2: 페르소나마다 1초 첫인상 클릭(P1~P3) + 본 뒤 믿음(trust) 따로 · 앵커 8편 · 판정은 패널이 성공 영상을 가릴 때만 (9회차 — v1 패널은 성공 H 4.65 < 덜 됨 M 5.48 로 거꾸로 매김: 낚시·AI 그림을 깎는 품질 심사였음).
# (v1.2 — 2026-11-11 — 보정 앵커: 실제 성공·덜 된 영상을 패널에 몰래 섞어(K-n) 같은 회차 점수로 기준을 맞춤 · add 명령(검토자 답 평균) (8회차 뒤 — 6.2~6.8 에서 멈춰 7.0 이 실제 성공 영상보다 높은 막대인지 확인).)
# (v1.1 — 2026-11-11 — report: 검토자 여러 명 평균 · 페르소나 몫 무게 평균 · 영상마다 판정(✅) (6회차 뒤 — 검토자 한 명 점수가 ±1 흔들려서, 무게는 personas.md 몫).)
# (v1.0 — 2026-11-11 — 새로 (사용자 지시 2026-11-11 "4가지 주제 골라서 제목, 썸네일 문구, 보조문구 만들어봐 그리고 페르소나로
#          썸네일 클릭율 잘나오는지 계속 검증해야해 잘나올 때까지 진행하고 최종 알려줘 영상 1개당 3개 만들면 돼").)
# CHANGELOG
#   v1.5 — 2026-11-12 — settings min_views · load_frames·pool_rows 성공 판정에 조회수 하한
#   v1.4 — 2026-11-11 — FRAMES 왜: 임진왜란·왜구 등 뺌 · cmd_check data_score = title_model lift(있으면) · cmd_validate(title_model) · judge mode "title+trust" · add 스냅숏에 data_score · report 제목 점수 칸·검증 줄
#   v1.3 — 2026-11-11 — panel_prompt v2(pass_rule.panel_version=2 — click·trust) · cmd_add trust 평균 · judge v2(가름 폭 min_gap · 믿음 하한) · report 믿음 칸
#   v1.2 — 2026-11-11 — anchors(panel 에 K-n 으로 섞음 · report 에 성공 H·덜 된 M 평균) · judge 보정 기준(pass_rule.calibrated) · add(검토자 답 파일 → rounds)
#   v1.1 — 2026-11-11 — wavg·judge · report 판정 줄 (pass_rule weights 가 있으면 무게 평균)
#   v1.0 — 2026-11-11 — check(안마다 규칙·숫자 점검) · panel(페르소나 패널 지시문 만들기) · report(회차 표) · 함수: load_frames·check_variant·panel_prompt·report
"""제목·썸네일 안 점검 — 숫자(그 주제 탐색 목록) + 페르소나 패널(Claude 하위 에이전트가 읽는 지시문) — 클릭률을 '미리 걸러 보는' 도구.

  python3 tools/ctr_check.py history check  <안.json>      # 안마다: 제목 2줄·길이·피할 말·썸네일 줄 길이·꼬리표 규칙 + 제목 꼴의 성공 비율 차이
  python3 tools/ctr_check.py history panel  <안.json> <n>  # n 회차 페르소나 패널 지시문 → <안 폴더>/panel_<n>_prompt.md (Claude 가 새 하위 에이전트에게 줌)
  python3 tools/ctr_check.py history add    <안.json> <n> <답1.json> …  # 검토자 답(JSON) 평균 → 안.json rounds (스냅숏 = 지금 안)
  python3 tools/ctr_check.py history validate <안.json>    # 제목 꼴 점수 검증: 5겹 교차 AUC(seed 42) + 앵커(실제 성공·덜 됨)를 빼고 배운 점수로 가름 → 안.json title_model
  python3 tools/ctr_check.py history report <안.json>      # 회차마다 패널 점수(안.json 'rounds' — Claude 가 패널 답을 넣음) → <안>.md

안.json: {"topic","made","videos":[{"id","theme","supply_rx","variants":[{"v":"A","title","thumb_main":["1줄","2줄"],"thumb_sub":["꼬리표"…],"image"}]}],
          "rounds":[{"n":1,"scores":{"<id>-<v>":{"P1":7,"P2":6,"P3":8,"flags":["…"],"feed":{"P1":2,…}}}}]}
제목 꼴 숫자 = <주제>/result/web/explore.json 의 주제 관련 롱폼 중 구독자 5만 이하 · 올린 지 7~182일 · 주제 밖(analysis_rules [exclude] OFF_TOPIC) 뺌 —
  성공 = 구독자당 하루 조회수 ≥ [success] MIN_VPD_SUBS 그리고 조회수 ≥ [success] MIN_VIEWS (v1.5). 꼴마다 성공 비율 − 전체 비율(%p). 표본이 15개보다 적은 꼴은 '표본 적음'.
보정 앵커 (안.json 'anchors'): 실제 영상(성공 hit · 덜 된 miss)의 제목·썸네일 문구·그림을 '다른 편 후보 K-n'으로 섞어 — 패널이 실제 성공 영상에
  주는 점수(H)·덜 된 영상 점수(M)를 같은 회차에서 잰다. pass_rule.calibrated 이면: 가장 좋은 안 ≥ H · 나머지 두 안 ≥ (H+M)/2 · 그리고 H − M ≥ min_gap (가르지 못하면 패널 무효).
패널 v2 (pass_rule.panel_version=2): 페르소나마다 클릭(폰 홈 피드 1~2초 첫인상 — P1~P3) + 안마다 믿음(trust — 본 뒤 '낚였다·고증 틀렸다'가 없을지).
  v1 은 하나의 점수에 둘을 섞어 실제 성공 영상(자극적 말·사진 같은 얼굴)을 가장 낮게 매김 → 판정은 클릭으로, 믿음은 하한(trust_min)으로.
판정 mode "title+trust" (10회차부터): 페르소나 클릭 점수는 v1·v2 모두 앵커를 거꾸로 매겨(9·10회차) 판정에 쓰지 않음 →
  클릭 = 검증된 제목 점수(data_score ≥ 실제 성공 앵커 가운데 가장 낮은 점수 hit_min) · 믿음 = 페르소나 trust ≥ trust_min(나머지 trust_min_others) · 나머지 두 안 data_score ≥ (성공 평균+덜 됨 평균)/2.
⚠️ 페르소나 패널은 시뮬레이션이다 — 진짜 클릭률은 유튜브 스튜디오 '테스트 및 비교'(썸네일 3장)로만 안다. 이 도구는 나쁜 안을 먼저 거르는 데만 쓴다.
※ 연구·교육용.
"""
import json
import logging
import re
import sys
import tomllib
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import title_fit  # noqa: E402  모바일·PC 목록 2줄

ROOT = Path(__file__).resolve().parent.parent
VERSION = "v1.5"
LOG = logging.getLogger("ctr")
MAIN_LINE_MAX = 14          # 썸네일 주요 문구 줄마다 띄어쓰기 빼고 (summary_ideas.lint_answer 와 같음)
MIN_N = 15                  # 이보다 적은 꼴은 '표본 적음'
# 제목 꼴 (정규식) — 역사·심리 탐색에서 쓴 꼴 그대로 (history/source/next_video_2026-11-11.md 2번 표)
FRAMES = {
    "사극·교과서 대비": r"사극|교과서|드라마에서",
    "어떻게 ~했을까": r"어떻게.{0,20}(을까|았나|었나|했나)",
    # '왜' = 묻는 말만 — 임진왜란·왜구·왜군·왜인·왜장 의 '왜' 는 뺌 (v1.4 — 앞 판은 '임진왜란 … 싸웠을까' 를 '왜 ~했을까' 로 셈)
    "왜 ~했을까": r"(?:^|[\s,.!?'\"“‘(])왜(?![란구군인놈적선장성])\s?.{0,25}(을까|나\?|는가|았나|었나|했나|일까)",
    "이유": r"이유",
    "물음표": r"\?",
    "숫자": r"\d",
    "'~없던' (보일러·냉장고 없던)": r"없던|없었던",
    "기록 근거 (실록·일기·법전)": r"실록|기록|일기|사료|문헌|경국대전",
    "비교 (vs·보다)": r"\bvs\b|VS|보다\s",
    "충격·소름·경악": r"충격|소름|경악",
    "진실·숨겨진·비밀": r"진실|숨겨진|비밀",
    "만약 ~했다면": r"만약|(았|었|였|했|웠|졌|났|갔|왔|넜|겼|됐)다면",
    "열어 봤다·단면": r"3D|열어\s?(봤|보)|단면",
}


def rel(p):
    """저장소 안이면 저장소 기준 경로, 밖이면 그대로 (시험용 사본)."""
    p = Path(p).resolve()
    return str(p.relative_to(ROOT)) if p.is_relative_to(ROOT) else str(p)


def log(stage, level=logging.INFO, **kv):
    LOG.log(level, "[%s] [%s] %s", stage, datetime.now().isoformat(timespec="seconds"),
            " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) and (' ' in v or not v) else v}" for k, v in kv.items()))


def settings(topic):
    """주제 규칙: 성공 기준·주제 밖 낱말 (analysis_rules) · 피할 말·꼬리표 규칙 (topics/settings.toml [summary])."""
    ar = tomllib.loads((ROOT / topic / "analysis_rules.toml").read_text("utf-8"))
    st = {}
    p = ROOT / topic / "topics" / "settings.toml"
    if p.is_file():
        st = tomllib.loads(p.read_text("utf-8")).get("summary") or {}
    return {"min_vpd": float(ar.get("success", {}).get("MIN_VPD_SUBS") or 0.1),
            "min_views": int(ar.get("success", {}).get("MIN_VIEWS") or 0),   # v1.5: 성공 = 구독자당 하루 조회수 + 조회수 하한 (성공 사례와 같은 잣대)
            "off": ar.get("exclude", {}).get("OFF_TOPIC") or [],
            "title_banned": st.get("TITLE_BANNED") or "", "banned": st.get("BANNED") or "",
            "sub_items": int(st.get("SUB_ITEMS") or 2), "sub_max": int(st.get("SUB_ITEM_MAX") or 6)}


def load_frames(topic, S):
    """제목 꼴마다 성공 비율 차이 — 작은 채널·7~182일·주제 관련 롱폼."""
    p = ROOT / topic / "result" / "web" / "explore.json"
    try:
        d = json.loads(p.read_text("utf-8"))
    except OSError as e:
        log("LOAD", logging.ERROR, file=str(p), error=e, next_step=f"python3 tools/cloud_run.py {topic} explore 먼저")
        raise
    off = re.compile("|".join(re.escape(w) for w in S["off"])) if S["off"] else None
    rows = [r for r in d["rows"] if r.get("relevant") and not r.get("short") and (r.get("minutes") or 0) >= 4
            and (r.get("subs") or 0) <= 50000 and 7 <= (r.get("age_days") or 0) <= 182
            and not (off and off.search(r["title"] + " " + (r.get("channel") or "")))]
    ok = lambda r: ((r.get("views_per_day") or 0) / max(100, r.get("subs") or 0) >= S["min_vpd"]  # noqa: E731
                    and (r.get("views") or 0) >= S["min_views"])
    base = sum(map(ok, rows)) / max(1, len(rows))
    F = {}
    for k, rx in FRAMES.items():
        g = [r for r in rows if re.search(rx, r["title"])]
        F[k] = {"n": len(g), "rate": (sum(map(ok, g)) / len(g)) if g else None}
    log("FRAMES", topic=topic, explore=d.get("generated"), pool=len(rows), base=f"{100*base:.0f}%")
    return d, base, F


def pool_rows(topic, S):
    """load_frames 와 같은 비교 무리 (작은 채널·7~182일·주제 관련 롱폼) + 성공 판정 함수."""
    d = json.loads((ROOT / topic / "result" / "web" / "explore.json").read_text("utf-8"))
    off = re.compile("|".join(re.escape(w) for w in S["off"])) if S["off"] else None
    rows = [r for r in d["rows"] if r.get("relevant") and not r.get("short") and (r.get("minutes") or 0) >= 4
            and (r.get("subs") or 0) <= 50000 and 7 <= (r.get("age_days") or 0) <= 182
            and not (off and off.search(r["title"] + " " + (r.get("channel") or "")))]
    ok = lambda r: ((r.get("views_per_day") or 0) / max(100, r.get("subs") or 0) >= S["min_vpd"]  # noqa: E731
                    and (r.get("views") or 0) >= S["min_views"])
    return d, rows, ok


def frame_score(title, lift):
    """제목 꼴 점수 = 제목에 든 꼴마다 (성공 비율 − 전체 비율)%p 합 (표본 MIN_N 이상만 — cmd_check data_score 와 같은 셈)."""
    return round(sum(l for k, l in lift.items() if l is not None and re.search(FRAMES[k], title)))


def learn_lift(rows, ok):
    base = sum(map(ok, rows)) / max(1, len(rows))
    lift = {}
    for k, rx in FRAMES.items():
        g = [r for r in rows if re.search(rx, r["title"])]
        lift[k] = 100 * (sum(map(ok, g)) / len(g) - base) if len(g) >= MIN_N else None
    return lift


def cmd_validate(topic, path, seed=42, folds=5):
    """제목 꼴 점수가 실제 성공을 맞히는지 — (1) 5겹 교차 AUC (2) 앵커(실제 성공·덜 된 영상)를 빼고 배운 점수로 앵커를 가르는지."""
    import random
    S = settings(topic)
    d, rows, ok = pool_rows(topic, S)
    P = json.loads(Path(path).read_text("utf-8"))
    aid = {a["id"] for a in P.get("anchors") or []}
    pool = [r for r in rows if r["id"] not in aid]

    def auc(sc, yy):
        pos = [a for a, t in zip(sc, yy) if t]
        neg = [a for a, t in zip(sc, yy) if not t]
        return sum((p > n) + 0.5 * (p == n) for p in pos for n in neg) / max(1, len(pos) * len(neg))
    idx = list(range(len(pool)))
    random.Random(seed).shuffle(idx)
    aucs = []
    for f in range(folds):
        test = set(idx[f::folds])
        lift = learn_lift([pool[i] for i in idx if i not in test], ok)
        te = sorted(test)
        aucs.append(round(auc([frame_score(pool[i]["title"], lift) for i in te], [ok(pool[i]) for i in te]), 3))
    lift = learn_lift(pool, ok)
    an = {a["k"]: {"kind": a["kind"], "score": frame_score(a["title"], lift)} for a in P.get("anchors") or []}
    hits = [x["score"] for x in an.values() if x["kind"] == "hit"]
    miss = [x["score"] for x in an.values() if x["kind"] == "miss"]
    tm = {"made": datetime.now().strftime("%Y-%m-%d %H:%M"), "explore": d.get("generated"), "pool": len(pool), "seed": seed, "folds": folds,
          "success_rate": round(sum(map(ok, pool)) / max(1, len(pool)), 3), "auc_folds": aucs, "auc_mean": round(sum(aucs) / len(aucs), 3),
          "anchors": an, "hit_min": min(hits) if hits else None, "hit_mean": round(sum(hits) / len(hits), 1) if hits else None,
          "miss_max": max(miss) if miss else None, "miss_mean": round(sum(miss) / len(miss), 1) if miss else None,
          "separates": bool(hits and miss and min(hits) > max(miss)), "lift": {k: None if v is None else round(v) for k, v in lift.items()}}
    P["title_model"] = tm
    Path(path).write_text(json.dumps(P, ensure_ascii=False, indent=1), "utf-8")
    log("VALIDATE", pool=len(pool), auc=tm["auc_mean"], folds=aucs, hit_min=tm["hit_min"], hit_mean=tm["hit_mean"],
        miss_max=tm["miss_max"], miss_mean=tm["miss_mean"], separates=tm["separates"],
        anchors=" ".join(f"{k}:{x['kind']}={x['score']}" for k, x in an.items()))
    return 0


def check_variant(vid, v, S, base, F, explore):
    probs, lifts = [], []
    t = v["title"]
    if not title_fit.fit(t)[0]:
        probs.append("제목이 어떤 화면에서 3줄")
    if len(t) > 60:
        probs.append("제목 60자 넘음")
    for rx, what in ((S["title_banned"], "제목·썸네일 피할 말"), (S["banned"], "쓰지 않는 말")):
        if rx:
            for txt in [t] + list(v.get("thumb_main") or []):
                m = re.search(rx, txt)
                if m:
                    probs.append(f"{what} '{m.group(0)}'")
    lines = v.get("thumb_main") or []
    if len(lines) != 2 or any(len(x.replace(" ", "")) > MAIN_LINE_MAX for x in lines):
        probs.append(f"썸네일 주요 문구는 2줄 · 줄마다 띄어쓰기 빼고 {MAIN_LINE_MAX}자 이하")
    subs = v.get("thumb_sub") or []
    if len(subs) > S["sub_items"] or any(len(x.replace(" ", "")) > S["sub_max"] for x in subs):
        probs.append(f"보조 꼬리표는 {S['sub_items']}개 이하 · 각 {S['sub_max']}자 이하")
    thumb_txt = " ".join(lines)
    if re.search(FRAMES["진실·숨겨진·비밀"], thumb_txt):
        probs.append("썸네일에 '진실·숨겨진·비밀' (제목 꼴 숫자가 가장 낮은 무리)")
    for k, rx in FRAMES.items():
        if re.search(rx, t) and F[k]["rate"] is not None:
            lift = 100 * (F[k]["rate"] - base)
            lifts.append((k, round(lift), F[k]["n"]))
    return probs, lifts


def cmd_check(topic, path):
    S = settings(topic)
    explore, base, F = load_frames(topic, S)
    P = json.loads(Path(path).read_text("utf-8"))
    titles = [r["title"] for r in explore["rows"]]
    bad = 0
    for vdo in P["videos"]:
        sup = [x for x in titles if re.search(vdo["supply_rx"], x)] if vdo.get("supply_rx") else []
        log("VIDEO", id=vdo["id"], theme=vdo["theme"], same_topic_titles=len(sup))
        for v in vdo["variants"]:
            probs, lifts = check_variant(vdo["id"], v, S, base, F, explore)
            tm_lift = (P.get("title_model") or {}).get("lift")
            if tm_lift:  # 보이는 꼴 숫자도 판정에 쓰는 숫자(앵커 빼고 배움)로 — 두 숫자가 달라 헷갈리지 않게
                lifts = [(k, tm_lift[k], n) for k, _, n in lifts if tm_lift.get(k) is not None] + [(k, 0, n) for k, _, n in lifts if tm_lift.get(k) is None]
            ds = frame_score(v["title"], tm_lift) if tm_lift else sum(l for _, l, n in lifts if n >= MIN_N)
            v["check"] = {"problems": probs, "frames": lifts, "data_score": ds, "data_score_from": "title_model (앵커 빼고 배움)" if tm_lift else "전체"}
            bad += bool(probs)
            log("CHECK", id=f"{vdo['id']}-{v['v']}", data_score=v["check"]["data_score"],
                frames=" · ".join(f"{k} {l:+d}%p({n})" for k, l, n in lifts) or "-", result="✅" if not probs else " / ".join(probs))
    P["frames"] = {"base": round(100 * base), "explore": explore.get("generated"),
                   "table": {k: {"n": f["n"], "lift": None if f["rate"] is None else round(100 * (f["rate"] - base))} for k, f in F.items()}}
    Path(path).write_text(json.dumps(P, ensure_ascii=False, indent=1), "utf-8")
    log("DONE", cmd="check", problems=bad)
    return 1 if bad else 0


def panel_prompt(topic, path, n):
    """페르소나 패널 지시문 — 새 하위 에이전트가 앞 회차를 모르게 (안 글·피드·페르소나만)."""
    P = json.loads(Path(path).read_text("utf-8"))
    pj = json.loads((ROOT / topic / "result" / "outliers" / "personas.json").read_text("utf-8"))
    cards = []
    names = lambda xs, k="name": " · ".join(f"{x[k]}" for x in (xs or [])[:3]) or "근거 없음"  # noqa: E731
    for p in pj.get("personas") or []:
        age = p.get("age") or {}
        ages = " · ".join(f"{k} {v}" for k, v in sorted((age.get("dist") or {}).items(), key=lambda kv: -kv[1])[:3]) or "밝힌 사람 적음"
        terms = " · ".join(t for t, _ in (p.get("known_terms") or [])[:6])
        cards.append(f"- **{p.get('id')} {p.get('name')}** — 댓글 묶음 몫 {round(100 * float(p.get('share') or 0))}% · 밝힌 나이 {ages} · "
                     f"보는 때 {names(p.get('states'))} · 아는 말 {terms} · 좋아함 {names(p.get('likes_cat'))} · 싫어함 {names(p.get('dislikes_cat'))}")
    ov = next((b for b in pj.get("baselines") or [] if b.get("key") == "all"), {})
    if ov.get("dislikes_cat"):
        cards.append(f"- (모든 댓글 {ov.get('n'):,}개) 좋아함 많은 순: {' · '.join(str(x['name']) + ' ' + str(x['n']) for x in (ov.get('likes_cat') or [])[:4])} · "
                     f"싫어함 많은 순: {' · '.join(str(x['name']) + ' ' + str(x['n']) for x in ov['dislikes_cat'][:4])}")
    feed = P.get("feed") or []
    if (P.get("pass_rule") or {}).get("panel_version") == 2:
        return panel_prompt_v2(P, path, n, cards, feed)
    L = [f"# 썸네일·제목 클릭 패널 — {n}회차 (자동 — `tools/ctr_check.py {VERSION}`)", "",
         "너는 유튜브 홈 화면을 넘기는 시청자 셋을 차례로 연기한다. 아래 '페르소나'는 실제 댓글로 만든 시청자다. 각 페르소나가 되어 **홈 피드**(경쟁 영상 + 우리 안이 섞여 있음)를 볼 때, "
         "우리 안마다 누를 가능성을 1~10 으로 매겨라 (10 = 피드에서 가장 먼저 누름 · 7 = 경쟁 영상 사이에서도 누름 · 5 = 시간이 나면 · 3 이하 = 지나침).",
         "규칙: 칭찬하려고 높게 주지 말 것 — 경쟁 영상과 견줘서. 낚시·과장·뜻이 헷갈리는 말·사실이 의심되는 말·AI 같은 느낌은 깎고 flags 에 적어라 (이 시청자들이 가장 싫어하는 것 = 고증 오류·광고·낚시·AI 그림). "
         "그림은 글로 적힌 장면을 상상해서 본다.", "", "## 페르소나", *cards, "",
         "## 홈 피드 — 경쟁 영상 (최근 30일 실제 영상 제목)", *[f"- {x}" for x in feed], "",
         "## 우리 안 (영상마다 A·B·C — 같은 영상의 썸네일·제목 시험안)"]
    for vdo in P["videos"]:
        L.append(f"### {vdo['id']} — {vdo['theme']}")
        for v in vdo["variants"]:
            L.append(f"- **{vdo['id']}-{v['v']}** 제목 「{v['title']}」 · 썸네일 아래 2줄 「{v['thumb_main'][0]} / {v['thumb_main'][1]}」 · "
                     f"그림 속 꼬리표 「{' · '.join(v.get('thumb_sub') or []) or '-'}」 · 그림 = {v.get('image')}")
    if P.get("anchors"):
        L.append("### K — 다른 생활사 편 후보 (편마다 주제가 다름 — 서로 견주지 말고 하나씩 같은 잣대로)")
        for a in P["anchors"]:
            L.append(f"- **{a['k']}** 제목 「{a['title']}」 · 썸네일 문구 「{' / '.join(a['thumb_main'])}」 · "
                     f"그림 속 작은 글 「{' · '.join(a.get('thumb_sub') or []) or '-'}」 · 그림 = {a.get('image')}")
    L += ["", "## 답 (JSON 하나만, 다른 글 없이)",
          '{"scores": {"<영상ID>-<안>": {"P1": 1~10, "P2": 1~10, "P3": 1~10, "flags": ["헷갈림·과장·사실 의심 등 — 없으면 빈 칸"], "why": "한 줄"}}, '
          '"best": {"<영상ID>": "A|B|C"} (K 는 빼고), "fix": {"<영상ID>-<안>": "점수를 올릴 고침 한 줄 (제목·썸네일 문구·꼬리표·그림 중)"}}']
    out = Path(path).resolve().with_name(f"panel_{n}_prompt.md")
    out.write_text("\n".join(L) + "\n", "utf-8")
    log("PANEL", round=n, prompt=rel(out), personas=len(cards), feed=len(feed), anchors=len(P.get("anchors") or []))
    return out


def item_lines(P):
    L = ["## 후보 (편마다 A·B·C = 같은 영상의 썸네일·제목 시험안 · K = 다른 편 후보 — 모두 같은 잣대로 하나씩)"]
    for vdo in P["videos"]:
        L.append(f"### {vdo['id']} — {vdo['theme']}")
        for v in vdo["variants"]:
            L.append(f"- **{vdo['id']}-{v['v']}** 제목 「{v['title']}」 · 썸네일 문구 「{' / '.join(v['thumb_main'])}」 · "
                     f"그림 속 작은 글 「{' · '.join(v.get('thumb_sub') or []) or '-'}」 · 그림 = {v.get('image')}")
    if P.get("anchors"):
        L.append("### K — 다른 생활사 편 후보 (편마다 주제가 다름)")
        for a in P["anchors"]:
            L.append(f"- **{a['k']}** 제목 「{a['title']}」 · 썸네일 문구 「{' / '.join(a['thumb_main'])}」 · "
                     f"그림 속 작은 글 「{' · '.join(a.get('thumb_sub') or []) or '-'}」 · 그림 = {a.get('image')}")
    return L


def panel_prompt_v2(P, path, n, cards, feed):
    """패널 v2 — 클릭(1~2초 첫인상)과 믿음(본 뒤)을 나눠 받음. v1 은 둘을 섞어 실제 성공 영상을 가장 낮게 매겼음 (9회차)."""
    L = [f"# 썸네일·제목 클릭 패널 v2 — {n}회차 (자동 — `tools/ctr_check.py {VERSION}`)", "",
         "너는 유튜브 홈 화면을 넘기는 시청자 셋을 차례로 연기한다. 아래 '페르소나'는 실제 댓글로 만든 시청자다.",
         "점수는 두 가지를 **따로** 매긴다.",
         "1. **클릭 (P1·P2·P3, 1~10)** — 그 페르소나가 폰 홈 피드를 엄지로 넘기다 이 썸네일·제목을 **1~2초** 볼 때 손가락이 멈추고 누르는가. "
         "실제 클릭률을 맞히는 것이 목적이다: 사람은 피드에서 제목·문구를 다 읽지 않고 큰 글자·얼굴·장면·궁금증 한 조각에 반응한다. "
         "댓글에서 낚시·과장을 욕하는 사람도 그 썸네일을 먼저 누르는 일이 흔하다. 맞춤법·고증·출처는 누른 **뒤에야** 따지므로 클릭 점수에 섞지 마라. "
         "네 취향(좋은 영상인가)이 아니라 그 사람의 엄지가 멈추는가만. 10 = 피드에서 가장 먼저 누름 · 7 = 경쟁 영상 사이에서도 누름 · 5 = 시간이 나면 · 3 이하 = 지나침.",
         "2. **믿음 (trust, 1~10, 후보마다 하나)** — 누르고 끝까지 본 뒤 이 시청자들이 '낚였다·고증이 틀렸다·AI 같다'고 느끼지 않을 가능성 "
         "(제목·썸네일의 약속이 사실로 지켜질 듯한가 — 이 시청자들이 가장 싫어하는 것 = 고증 오류·광고·낚시·AI 그림). 문제가 보이면 flags 에 적어라.",
         "그림은 글로 적힌 장면을 상상해서 본다.", "", "## 페르소나", *cards, "",
         "## 홈 피드 — 경쟁 영상 (최근 30일 실제 영상 제목)", *[f"- {x}" for x in feed], "", *item_lines(P), "",
         "## 답 (JSON 하나만, 다른 글 없이)",
         '{"scores": {"<후보ID>": {"P1": 1~10, "P2": 1~10, "P3": 1~10, "trust": 1~10, "flags": ["헷갈림·과장·사실 의심 등 — 없으면 빈 칸"], "why": "한 줄"}}, '
         '"best": {"<영상ID>": "A|B|C"} (K 는 빼고), "fix": {"<영상ID>-<안>": "클릭을 올리되 믿음을 깎지 않는 고침 한 줄 (제목·썸네일 문구·꼬리표·그림 중)"}}']
    out = Path(path).resolve().with_name(f"panel_{n}_prompt.md")
    out.write_text("\n".join(L) + "\n", "utf-8")
    log("PANEL", version=2, round=n, prompt=rel(out), personas=len(cards), feed=len(feed), anchors=len(P.get("anchors") or []))
    return out


def wavg(s, w):
    """페르소나 몫 무게 평균 (무게가 없으면 같은 무게)."""
    w = w or {"P1": 1, "P2": 1, "P3": 1}
    return round(sum(s[p] * w[p] for p in ("P1", "P2", "P3")) / sum(w[p] for p in ("P1", "P2", "P3")), 2)


def anchor_level(P, r, w):
    """같은 회차 보정 앵커 점수 — H = 실제 성공 영상 무게 평균의 평균, M = 덜 된 영상. 앵커가 없으면 None."""
    sc = r.get("scores") or {}
    hit = [wavg(sc[a["k"]], w) for a in P.get("anchors") or [] if a["kind"] == "hit" and a["k"] in sc]
    miss = [wavg(sc[a["k"]], w) for a in P.get("anchors") or [] if a["kind"] == "miss" and a["k"] in sc]
    if not hit or not miss:
        return None
    return round(sum(hit) / len(hit), 2), round(sum(miss) / len(miss), 2)


def judge(P, r, rule):
    """회차 판정 — 영상마다 가장 좋은 안(무게 평균) · 통과 여부. 기준은 안.json 'pass_rule' (calibrated 면 같은 회차 앵커 H·M)."""
    w = rule.get("weights")
    HM = anchor_level(P, r, w) if rule.get("calibrated") else None
    tm = P.get("title_model") or {}
    title_mode = rule.get("mode") == "title+trust" and r["n"] >= rule.get("mode_from", 0) and tm.get("hit_min") is not None
    out = {}
    for vdo in P["videos"]:
        keys = [k for k in (r.get("scores") or {}) if k.startswith(vdo["id"] + "-")]
        if not keys:
            continue
        sc = {k: wavg(r["scores"][k], w) for k in keys}
        best = max(sc, key=sc.get)
        b = r["scores"][best]
        if title_mode:
            # 제목 점수는 늘 지금 title_model 로 스냅숏 제목에서 다시 셈 (회차마다 같은 잣대 — 스냅숏에 적힌 값은 그때 기록)
            ds = {k: frame_score(((r.get("snapshot") or {}).get(k) or {}).get("title", ""), tm["lift"]) for k in keys}
            mid = (tm["hit_mean"] + tm["miss_mean"]) / 2
            tr = lambda k: r["scores"][k].get("trust") or 0  # noqa: E731
            # 본안 = 믿음 하한을 넘는 안 가운데 제목 점수가 가장 높은 안 (같으면 클릭 참고 점수) — 믿음이 낮은 안은 본안이 되지 않음
            cand = [k for k in keys if tr(k) >= rule["trust_min"]] or keys
            best = max(cand, key=lambda k: (ds[k], sc[k]))
            ok = (ds[best] >= tm["hit_min"] and tr(best) >= rule["trust_min"]
                  and all(ds[k] >= mid and tr(k) >= rule["trust_min_others"] for k in keys if k != best))
            out[vdo["id"]] = {"best": best, "score": f"제목 {ds[best]} · 믿음 {tr(best)} · 클릭(참고) {sc[best]}", "ok": ok, "all": sc, "ds": ds}
            continue
        if HM:
            H, M = HM
            gap = rule.get("min_gap", 0)
            tmin = rule.get("trust_min")
            tr_ok = tmin is None or all((r["scores"][k].get("trust") or 0) >= (tmin if k == best else rule.get("trust_min_others", tmin)) for k in keys)
            ok = (H - M) >= gap and H > M and sc[best] >= H and all(sc[k] >= round((H + M) / 2, 2) for k in keys) and tr_ok
        elif w:
            ok = sc[best] >= rule["best_wavg"] and min(b["P1"], b["P2"]) >= rule["best_min_P1P2"] and all(sc[k] >= rule["others_wavg"] for k in keys)
        else:
            ok = sc[best] >= rule["best_avg"] and min(b[p] for p in ("P1", "P2", "P3")) >= rule["best_min"] and all(sc[k] >= rule["all_avg"] for k in keys)
        out[vdo["id"]] = {"best": best, "score": sc[best], "ok": ok, "all": sc}
    return out


def cmd_report(topic, path):
    P = json.loads(Path(path).read_text("utf-8"))
    rule = P.get("pass_rule") or {"best_avg": 7.5, "best_min": 6.5, "all_avg": 6.0}
    w = rule.get("weights")
    if rule.get("calibrated"):
        rtxt = (f"통과 기준 (보정 — {rule.get('calibrated_from', '')}): 영상마다 가장 좋은 안 ≥ 같은 회차 실제 성공 영상 점수 H · 나머지 두 안 ≥ (H+M)/2 · 패널이 H > M 을 가려야 함 (무게 {w}). "
                f"참고 — 보정 전 기준: 가장 좋은 안 ≥ {rule.get('best_wavg')} · P1·P2 ≥ {rule.get('best_min_P1P2')} · 나머지 ≥ {rule.get('others_wavg')}")
    elif w:
        rtxt = (f"통과 기준: 영상마다 가장 좋은 안의 페르소나 몫 무게 평균 ≥ {rule['best_wavg']} (무게 {w}) · 그 안의 P1·P2 ≥ {rule['best_min_P1P2']} · "
                f"나머지 두 안 무게 평균 ≥ {rule['others_wavg']} — {rule.get('note', '')}")
    else:
        rtxt = f"통과 기준: 영상마다 가장 좋은 안 평균 ≥ {rule['best_avg']} · 그 안의 페르소나마다 ≥ {rule['best_min']} · 세 안 모두 평균 ≥ {rule['all_avg']}"
    if rule.get("mode") == "title+trust":
        rtxt = (f"통과 기준 ({rule.get('mode_from')}회차부터 — {rule.get('mode_note', '')}): 영상마다 가장 좋은 안의 제목 점수 ≥ 실제 성공 앵커 가운데 가장 낮은 점수 · 그 안의 믿음 ≥ {rule['trust_min']} · "
                f"나머지 두 안 제목 점수 ≥ (성공 평균 + 덜 됨 평균)/2 · 믿음 ≥ {rule['trust_min_others']}. 페르소나 클릭 점수는 참고만. 앞 회차 기준: " + rtxt)
    tm = P.get("title_model") or {}
    L = [f"# 제목·썸네일 안 — 점검·페르소나 패널 ({topic})", "",
         f"자동 생성 — `tools/ctr_check.py {VERSION}` · 안 파일 `{Path(path).name}` · ⚠️ 패널은 시뮬레이션 — 진짜 클릭률은 스튜디오 '테스트 및 비교'.", "", rtxt, ""]
    if tm:
        L += [f"제목 점수 검증 (`validate` {tm['made']} · 탐색 {tm['explore']}): 비교 무리 {tm['pool']}편 (성공 {round(100 * tm['success_rate'])}%) · "
              f"5겹 교차 AUC {tm['auc_mean']} ({' · '.join(map(str, tm['auc_folds']))}, seed {tm['seed']}) — 0.5 = 동전 던지기, 약하지만 맞힘 · "
              f"앵커(빼고 배움): 성공 {' · '.join(str(x['score']) for x in tm['anchors'].values() if x['kind'] == 'hit')} (가장 낮음 {tm['hit_min']}) · "
              f"덜 됨 {' · '.join(str(x['score']) for x in tm['anchors'].values() if x['kind'] == 'miss')} (가장 높음 {tm['miss_max']}) · 가름 {'✅' if tm['separates'] else '❌'}", ""]
    for r in P.get("rounds") or []:
        J = judge(P, r, rule)
        L += [f"## {r['n']}회차 — {r.get('reviewer', '')}", "",
              "판정: " + " · ".join(f"{vid} {j['best']} {j['score']} {'✅' if j['ok'] else '—'}" for vid, j in J.items()), "",
              "| 안 | 제목 | 썸네일 | 꼬리표 | 제목 점수 | P1 | P2 | P3 | 무게 평균 | 믿음 | flags |", "|---|---|---|---|---|---|---|---|---|---|---|"]
        for vdo in P["videos"]:
            for v in vdo["variants"]:
                k = f"{vdo['id']}-{v['v']}"
                s = (r.get("scores") or {}).get(k)
                snap = (r.get("snapshot") or {}).get(k) or v
                if not s:
                    continue
                L.append(f"| {k} | {snap['title']} | {' / '.join(snap['thumb_main'])} | {' · '.join(snap.get('thumb_sub') or [])} | {frame_score(snap['title'], tm['lift']) if tm.get('lift') else snap.get('data_score', '-')} | {s['P1']} | {s['P2']} | {s['P3']} | {wavg(s, w)} | {s.get('trust', '-')} | {' · '.join(s.get('flags') or []) or '-'} |")
        if any(a["k"] in (r.get("scores") or {}) for a in P.get("anchors") or []):
            HM = anchor_level(P, r, w)
            gap = rule.get("min_gap", 0)
            L += ["", f"보정 앵커 (실제 영상 — 패널은 모름): 성공 H = {HM[0]} · 덜 된 M = {HM[1]} · 가름 {'✅ H − M ≥ ' + str(gap) if HM[0] - HM[1] >= gap and HM[0] > HM[1] else '❌ 못 가름 (이 회차 판정 무효)'} · 나머지 안 기준 (H+M)/2 = {round((HM[0] + HM[1]) / 2, 2)}", "",
                  "| 앵커 | 실제 | 제목 | 썸네일 문구 | P1 | P2 | P3 | 무게 평균 | 믿음 |", "|---|---|---|---|---|---|---|---|---|"]
            for a in P["anchors"]:
                s = r["scores"].get(a["k"])
                if s:
                    L.append(f"| {a['k']} | {'성공' if a['kind'] == 'hit' else '덜 됨'} (배수 {a['ratio']} · 구독자 {a['subs']:,}) | {a['title']} | {' / '.join(a['thumb_main'])} | {s['P1']} | {s['P2']} | {s['P3']} | {wavg(s, w)} | {s.get('trust', '-')} |")
        L.append("")
        log("ROUND", n=r["n"], anchors=anchor_level(P, r, w), verdict=" ".join(f"{vid}:{j['best']}={j['score']}{'✅' if j['ok'] else '✗'}" for vid, j in J.items()))
    Path(path).resolve().with_suffix(".md").write_text("\n".join(L), "utf-8")
    log("WRITE", md=rel(Path(path).resolve().with_suffix(".md")))
    return 0


def cmd_add(topic, path, n, answers):
    """검토자 답(JSON 파일들) 평균 → 안.json rounds[n] (스냅숏 = 지금 안 · 앵커 포함 · flags 는 모두 모음)."""
    P = json.loads(Path(path).read_text("utf-8"))
    R = []
    for a in answers:
        try:
            R.append(json.loads(Path(a).read_text("utf-8")))
        except (OSError, ValueError) as e:
            log("ADD", logging.ERROR, file=a, error=e, next_step="검토자 답이 JSON 하나인지 확인")
            return 1
    keys = [f"{v['id']}-{x['v']}" for v in P["videos"] for x in v["variants"]] + [a["k"] for a in P.get("anchors") or []]
    scores = {}
    for k in keys:
        raw = [[r["scores"][k][p] for p in ("P1", "P2", "P3")] for r in R if k in r.get("scores", {})]
        if len(raw) != len(R):
            log("ADD", logging.WARNING, key=k, answered=len(raw), reviewers=len(R), note="답이 빠진 검토자가 있음")
        if not raw:
            continue
        fl = []
        for r in R:
            for f in (r["scores"].get(k) or {}).get("flags") or []:
                if f not in fl:
                    fl.append(f)
        scores[k] = {**{p: round(sum(x[i] for x in raw) / len(raw), 2) for i, p in enumerate(("P1", "P2", "P3"))}, "raw": raw, "flags": fl}
        tr = [r["scores"][k]["trust"] for r in R if "trust" in (r["scores"].get(k) or {})]
        if tr:
            scores[k]["trust"] = round(sum(tr) / len(tr), 2)
            scores[k]["raw_trust"] = tr
    snap = {f"{v['id']}-{x['v']}": {**{kk: x[kk] for kk in ("title", "thumb_main", "thumb_sub", "image") if kk in x},
                                    "data_score": (x.get("check") or {}).get("data_score")} for v in P["videos"] for x in v["variants"]}
    P["rounds"] = [r for r in P.get("rounds") or [] if r["n"] != n] + [{
        "n": n, "reviewer": f"새 하위 에이전트 {len(R)}명 평균 (" + " · ".join(Path(a).stem for a in answers) + ")",
        "scores": scores, "snapshot": snap, "fix": [r.get("fix") or {} for r in R]}]
    Path(path).write_text(json.dumps(P, ensure_ascii=False, indent=1), "utf-8")
    log("ADD", round=n, reviewers=len(R), keys=len(scores))
    return 0


def main(argv):
    logging.basicConfig(level=logging.INFO, format="%(message)s", stream=sys.stdout)
    if len(argv) < 3:
        print(__doc__)
        return 2
    topic, cmd, path = argv[0], argv[1], argv[2]
    log("START", tool=f"ctr_check.py {VERSION}", topic=topic, cmd=cmd, file=path)
    if cmd == "check":
        return cmd_check(topic, path)
    if cmd == "panel":
        panel_prompt(topic, path, int(argv[3]) if len(argv) > 3 else 1)
        return 0
    if cmd == "report":
        return cmd_report(topic, path)
    if cmd == "validate":
        return cmd_validate(topic, path)
    if cmd == "add" and len(argv) > 4:
        return cmd_add(topic, path, int(argv[3]), argv[4:])
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
