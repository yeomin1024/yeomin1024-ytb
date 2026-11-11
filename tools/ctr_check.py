#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-11-11 — report: 검토자 여러 명 평균 · 페르소나 몫 무게 평균 · 영상마다 판정(✅) (6회차 뒤 — 검토자 한 명 점수가 ±1 흔들려서, 무게는 personas.md 몫).
# (v1.0 — 2026-11-11 — 새로 (사용자 지시 2026-11-11 "4가지 주제 골라서 제목, 썸네일 문구, 보조문구 만들어봐 그리고 페르소나로
#          썸네일 클릭율 잘나오는지 계속 검증해야해 잘나올 때까지 진행하고 최종 알려줘 영상 1개당 3개 만들면 돼").)
# CHANGELOG
#   v1.1 — 2026-11-11 — wavg·judge · report 판정 줄 (pass_rule weights 가 있으면 무게 평균)
#   v1.0 — 2026-11-11 — check(안마다 규칙·숫자 점검) · panel(페르소나 패널 지시문 만들기) · report(회차 표) · 함수: load_frames·check_variant·panel_prompt·report
"""제목·썸네일 안 점검 — 숫자(그 주제 탐색 목록) + 페르소나 패널(Claude 하위 에이전트가 읽는 지시문) — 클릭률을 '미리 걸러 보는' 도구.

  python3 tools/ctr_check.py history check  <안.json>      # 안마다: 제목 2줄·길이·피할 말·썸네일 줄 길이·꼬리표 규칙 + 제목 꼴의 성공 비율 차이
  python3 tools/ctr_check.py history panel  <안.json> <n>  # n 회차 페르소나 패널 지시문 → <안 폴더>/panel_<n>_prompt.md (Claude 가 새 하위 에이전트에게 줌)
  python3 tools/ctr_check.py history report <안.json>      # 회차마다 패널 점수(안.json 'rounds' — Claude 가 패널 답을 넣음) → <안>.md

안.json: {"topic","made","videos":[{"id","theme","supply_rx","variants":[{"v":"A","title","thumb_main":["1줄","2줄"],"thumb_sub":["꼬리표"…],"image"}]}],
          "rounds":[{"n":1,"scores":{"<id>-<v>":{"P1":7,"P2":6,"P3":8,"flags":["…"],"feed":{"P1":2,…}}}}]}
제목 꼴 숫자 = <주제>/result/web/explore.json 의 주제 관련 롱폼 중 구독자 5만 이하 · 올린 지 7~182일 · 주제 밖(analysis_rules [exclude] OFF_TOPIC) 뺌 —
  성공 = 구독자당 하루 조회수 ≥ [success] MIN_VPD_SUBS. 꼴마다 성공 비율 − 전체 비율(%p). 표본이 15개보다 적은 꼴은 '표본 적음'.
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
VERSION = "v1.1"
LOG = logging.getLogger("ctr")
MAIN_LINE_MAX = 14          # 썸네일 주요 문구 줄마다 띄어쓰기 빼고 (summary_ideas.lint_answer 와 같음)
MIN_N = 15                  # 이보다 적은 꼴은 '표본 적음'
# 제목 꼴 (정규식) — 역사·심리 탐색에서 쓴 꼴 그대로 (history/source/next_video_2026-11-11.md 2번 표)
FRAMES = {
    "사극·교과서 대비": r"사극|교과서|드라마에서",
    "어떻게 ~했을까": r"어떻게.{0,20}(을까|았나|었나|했나)",
    "왜 ~했을까": r"왜.{0,25}(을까|나\?|는가|았나|었나)",
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
    ok = lambda r: (r.get("views_per_day") or 0) / max(100, r.get("subs") or 0) >= S["min_vpd"]  # noqa: E731
    base = sum(map(ok, rows)) / max(1, len(rows))
    F = {}
    for k, rx in FRAMES.items():
        g = [r for r in rows if re.search(rx, r["title"])]
        F[k] = {"n": len(g), "rate": (sum(map(ok, g)) / len(g)) if g else None}
    log("FRAMES", topic=topic, explore=d.get("generated"), pool=len(rows), base=f"{100*base:.0f}%")
    return d, base, F


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
            v["check"] = {"problems": probs, "frames": lifts, "data_score": sum(l for _, l, n in lifts if n >= MIN_N)}
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
    L += ["", "## 답 (JSON 하나만, 다른 글 없이)",
          '{"scores": {"<영상ID>-<안>": {"P1": 1~10, "P2": 1~10, "P3": 1~10, "flags": ["헷갈림·과장·사실 의심 등 — 없으면 빈 칸"], "why": "한 줄"}}, '
          '"best": {"<영상ID>": "A|B|C"}, "fix": {"<영상ID>-<안>": "점수를 올릴 고침 한 줄 (제목·썸네일 문구·꼬리표·그림 중)"}}']
    out = Path(path).resolve().with_name(f"panel_{n}_prompt.md")
    out.write_text("\n".join(L) + "\n", "utf-8")
    log("PANEL", round=n, prompt=str(out.relative_to(ROOT)), personas=len(cards), feed=len(feed))
    return out


def wavg(s, w):
    """페르소나 몫 무게 평균 (무게가 없으면 같은 무게)."""
    w = w or {"P1": 1, "P2": 1, "P3": 1}
    return round(sum(s[p] * w[p] for p in ("P1", "P2", "P3")) / sum(w[p] for p in ("P1", "P2", "P3")), 2)


def judge(P, r, rule):
    """회차 판정 — 영상마다 가장 좋은 안(무게 평균) · 통과 여부. 기준은 안.json 'pass_rule'."""
    w = rule.get("weights")
    out = {}
    for vdo in P["videos"]:
        keys = [k for k in (r.get("scores") or {}) if k.startswith(vdo["id"] + "-")]
        if not keys:
            continue
        sc = {k: wavg(r["scores"][k], w) for k in keys}
        best = max(sc, key=sc.get)
        b = r["scores"][best]
        if w:
            ok = sc[best] >= rule["best_wavg"] and min(b["P1"], b["P2"]) >= rule["best_min_P1P2"] and all(sc[k] >= rule["others_wavg"] for k in keys)
        else:
            ok = sc[best] >= rule["best_avg"] and min(b[p] for p in ("P1", "P2", "P3")) >= rule["best_min"] and all(sc[k] >= rule["all_avg"] for k in keys)
        out[vdo["id"]] = {"best": best, "score": sc[best], "ok": ok, "all": sc}
    return out


def cmd_report(topic, path):
    P = json.loads(Path(path).read_text("utf-8"))
    rule = P.get("pass_rule") or {"best_avg": 7.5, "best_min": 6.5, "all_avg": 6.0}
    w = rule.get("weights")
    if w:
        rtxt = (f"통과 기준: 영상마다 가장 좋은 안의 페르소나 몫 무게 평균 ≥ {rule['best_wavg']} (무게 {w}) · 그 안의 P1·P2 ≥ {rule['best_min_P1P2']} · "
                f"나머지 두 안 무게 평균 ≥ {rule['others_wavg']} — {rule.get('note', '')}")
    else:
        rtxt = f"통과 기준: 영상마다 가장 좋은 안 평균 ≥ {rule['best_avg']} · 그 안의 페르소나마다 ≥ {rule['best_min']} · 세 안 모두 평균 ≥ {rule['all_avg']}"
    L = [f"# 제목·썸네일 안 — 점검·페르소나 패널 ({topic})", "",
         f"자동 생성 — `tools/ctr_check.py {VERSION}` · 안 파일 `{Path(path).name}` · ⚠️ 패널은 시뮬레이션 — 진짜 클릭률은 스튜디오 '테스트 및 비교'.", "", rtxt, ""]
    for r in P.get("rounds") or []:
        J = judge(P, r, rule)
        L += [f"## {r['n']}회차 — {r.get('reviewer', '')}", "",
              "판정: " + " · ".join(f"{vid} {j['best']} {j['score']} {'✅' if j['ok'] else '—'}" for vid, j in J.items()), "",
              "| 안 | 제목 | 썸네일 | 꼬리표 | P1 | P2 | P3 | 무게 평균 | flags |", "|---|---|---|---|---|---|---|---|---|"]
        for vdo in P["videos"]:
            for v in vdo["variants"]:
                k = f"{vdo['id']}-{v['v']}"
                s = (r.get("scores") or {}).get(k)
                snap = (r.get("snapshot") or {}).get(k) or v
                if not s:
                    continue
                L.append(f"| {k} | {snap['title']} | {' / '.join(snap['thumb_main'])} | {' · '.join(snap.get('thumb_sub') or [])} | {s['P1']} | {s['P2']} | {s['P3']} | {wavg(s, w)} | {' · '.join(s.get('flags') or []) or '-'} |")
        L.append("")
        log("ROUND", n=r["n"], verdict=" ".join(f"{vid}:{j['best']}={j['score']}{'✅' if j['ok'] else '✗'}" for vid, j in J.items()))
    Path(path).resolve().with_suffix(".md").write_text("\n".join(L), "utf-8")
    log("WRITE", md=str(Path(path).resolve().with_suffix(".md").relative_to(ROOT)))
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
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
