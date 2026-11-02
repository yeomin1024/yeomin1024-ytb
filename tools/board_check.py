#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-11-02 — 3단계 판(주제 → 대본 → 쇼츠)에 맞춤: package --stage topic|shorts (판마다 그 칸만) · script --kind short (해설·설명란 점검 뺌).
# (v1.0 — 2026-11-02 — 평가판에 처음 올리기 전 점검 (일반 페르소나 + 반론 페르소나) — 토큰을 쓰지 않는 규칙 점검
#   사용자 지시 2026-11-02 "처음 평가판에 올라가기 전에는 일반, 반론 페르소나로 점검은 거쳐야해 토큰 최대한 아끼는 방식으로 하고".
#   · 일반 페르소나 = stock/result/outliers/personas.json (tools/persona_review.py 의 review — 풀이 없는 어려운 말·50자 넘는 문장·광고·겁주기 + 페르소나가 원하는 말)
#   · 반론 페르소나 = stock/result/outliers/rebuttal_persona.md 0번 표의 K1~K8 질문을 규칙으로 (낱말·꼴·숫자 대조) — 규칙이 못 보는 것은 '사람 확인' 줄로 남김
#   · 결과: 통과(✅) · 고칠 것(❌ — 고친 뒤 다시) · 사람 확인(⚠ — Claude 가 그 줄만 읽고 판단) → 판의 카드에 '점검' 칸으로 붙음
#   연구·교육용 도구 — 투자 권유가 아님.
r"""
  python3 tools/board_check.py script  stock <대본.txt> [--kind long|short] [--calc <json>] [--upload <upload.md>] [--allow "<사용자 문장 일부>" …]
  python3 tools/board_check.py package stock <기획안.json> [--stage topic|shorts] [--write]   # topic → 주제 평가판(롱폼 칸) · shorts → 쇼츠 평가판(쇼츠 칸)
끝 코드: ❌ 가 하나라도 있으면 1.
"""
import contextlib
import io
import json
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
VERSION = "v1.1"
SENT_MAX = 50

# K8 권유·과장 — 사용자가 정한 제목 꼴('절대 통과 못하는')은 뺌
K8 = re.compile(r"무조건|반드시|100\s?%\s?(수익|보장)|확실히 (번|오른)|(?<!절대 통과 )절대(?! 통과)|사세요|파세요|매수하세요|매도하세요|추천 ?종목|수익 보장|대박|떡상|인생 역전")
# K2 결과론·앞으로도
K2 = re.compile(r"앞으로도 (반드시|꼭|계속)|항상 (오른|이긴)|늘 (오른|이긴)|영원히")
# 채널 목적 밖 (stock/guides/channel.md 1번 — 단타·타이밍·종목/업종 맞히기·'더 벌었나')
OFF = re.compile(r"단타|스캘핑|급등주 찾|종목 맞히|업종 맞히|수익률 대결|누가 더 벌|타이밍 맞히|바닥 맞히")
COND = re.compile(r"년|달|개월|쓸 일|급할 때|비상금|은퇴|월급|목돈|나이|기간|조건|계좌의|비중")


def log(stage, **kv):
    ts = time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime())
    print(f"[{stage}] [{ts}] " + " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) else v}" for k, v in kv.items()))


def numbers_in_calc(path):
    """계산 JSON 안의 모든 숫자(문자열 '+12.3%' 꼴 포함) → 절댓값 집합."""
    vals = set()

    def walk(x):
        if isinstance(x, dict):
            for v in x.values():
                walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)
        elif isinstance(x, (int, float)) and not isinstance(x, bool):
            vals.add(abs(float(x)))
        elif isinstance(x, str):
            for m in re.findall(r"[-+−]?\d+(?:\.\d+)?", x):
                vals.add(abs(float(m.replace("−", "-"))))
    walk(json.loads(Path(path).read_text("utf-8")))
    return vals


def pct_ok(n, vals):
    """대본의 정수 퍼센트 n 이 계산 값(퍼센트·비율)을 반올림·버림한 값인가."""
    for v in vals:
        for x in (v, v * 100):
            if round(x) == n or int(x) == n or (n % 10 == 0 and abs(x - n) < 3):
                return True
    return False


def check_script(topic, script, calc=None, upload=None, allow=(), kind="long"):
    import persona_review as PR
    with contextlib.redirect_stdout(io.StringIO()):
        R = PR.review(topic, script)
    sents = R["sents"]
    fails, warns, oks = [], [], []
    # ── 일반 페르소나
    un = [(t, v["n"]) for t, v in R["first"].items() if not v["explained"]]
    if un:
        fails.append(f"일반: 풀이 없는 어려운 말 {un}")
    longs = [(i, n) for i, s, n in R["long"] if not any(a in s for a in allow)]
    (fails if longs else oks).append(f"일반: 50자 넘는 문장 {longs or '없음 (사용자 문장은 뺌)'}")
    if R["ads"] or R["scares"]:
        fails.append(f"일반: 광고 {len(R['ads'])} · 겁주기 {len(R['scares'])}")
    oks.append(f"일반: 약 {R['est_min']:.1f}분 · 페르소나마다 원하는 말 " + ", ".join(f"{r['p']['id']} {len(r['covered'])}/{len(r['wants'])}" for r in R["rows"]))
    # ── 반론 K8·K2
    k8 = [(i, s) for i, s in enumerate(sents, 1) if K8.search(s) and not any(a in s for a in allow)]
    (fails if k8 else oks).append(f"반론 K8 권유·과장: {k8 or '없음'}")
    k2 = [(i, s) for i, s in enumerate(sents, 1) if K2.search(s)]
    (fails if k2 else oks).append(f"반론 K2 결과론: {k2 or '없음'}")
    if kind == "short":                                   # 쇼츠: 해설·보기·설명란이 없음 → K6·K7·K2/K4 설명란 점검 뺌
        if calc:
            vals = numbers_in_calc(calc)
            loose = [(i, m.group(0)) for i, s in enumerate(sents, 1) for m in re.finditer(r"(\d+(?:\.\d+)?)\s?%", s) if float(m.group(1)) == int(float(m.group(1))) and not pct_ok(int(float(m.group(1))), vals)]
            (warns if loose else oks).append(f"반론 K5 계산 출력에 없는 % (사람 확인): {loose or '없음'}")
        else:
            warns.append("반론 K5: --calc 없음 — 숫자 대조 못 함")
        return fails, warns, oks
    # ── K6 지키기 어려움 인정 — 해설마다 '물론 …' 반론 줄
    heads = [i for i, s in enumerate(sents) if re.match(r"(첫|두|세|네|다섯) 번째 선택의 정답은", s)]
    miss = []
    for k, h in enumerate(heads):
        end = heads[k + 1] if k + 1 < len(heads) else len(sents)
        if not any(s.startswith("물론") for s in sents[h:end]):
            miss.append(k + 1)
    (fails if miss else oks).append(f"반론 K6 '물론…하지만' 없는 해설: {miss or '없음'} (해설 {len(heads)}개)")
    # ── K7 모순 — 해설 '정답은 X, …' 이 보기 X 와 같은 말인가
    opts = {}
    q = 0
    for s in sents:
        if re.match(r"여기서 .+ 번째 선택입니다", s):
            q += 1
        m = re.match(r"([AB])번, (.+)", s)
        if m and q:
            opts[(q, m.group(1))] = m.group(2)
    bad7, letters = [], []
    for k, h in enumerate(heads):
        m = re.search(r"정답은 ([AB]), (.+)", sents[h])
        if not m:
            continue
        letters.append(m.group(1))
        o = opts.get((k + 1, m.group(1)), "")
        a = set(re.findall(r"[가-힣A-Za-z0-9%]{2,}", o)); b = set(re.findall(r"[가-힣A-Za-z0-9%]{2,}", m.group(2)))
        if a and len(a & b) / len(a) < 0.25:
            bad7.append((k + 1, m.group(1), o))
    (warns if bad7 else oks).append(f"반론 K7 해설 정답 ↔ 보기 말이 다름(사람 확인): {bad7 or '없음'} · 정답 글자 {''.join(letters)}")
    if letters and len(set(letters)) == 1:
        fails.append("반론 K7: 정답이 모두 같은 글자 — 섞어야 함")
    # ── K5 숫자 — 대본 퍼센트가 계산 출력에 있는가
    if calc:
        vals = numbers_in_calc(calc)
        loose = []
        for i, s in enumerate(sents, 1):
            for m in re.finditer(r"(\d+(?:\.\d+)?)\s?%", s):
                n = float(m.group(1))
                if n == int(n) and not pct_ok(int(n), vals):
                    loose.append((i, m.group(0)))
        (warns if loose else oks).append(f"반론 K5 계산 출력에 없는 % (사람 확인 — 연구 인용·규칙 숫자일 수 있음): {loose or '없음'}")
    else:
        warns.append("반론 K5: --calc 없음 — 숫자 대조 못 함")
    # ── K2·K4 한계·뺀 비용 — 설명란(업로드 시트)에
    if upload:
        u = Path(upload).read_text("utf-8")
        need = {"K2 과거 자료 한계": r"과거.*(보장|같다는)", "K4 뺀 비용(세금·수수료·환율)": r"(세금|수수료).*(뺐|빼)|환율.*(뺐|빼)"}
        for k, pat in need.items():
            (oks if re.search(pat, u) else fails).append(f"반론 {k}: 설명란 {'있음' if re.search(pat, u) else '없음'}")
    else:
        warns.append("반론 K2·K4: --upload 없음 — 설명란 확인 못 함")
    # ── K1·K3 — 규칙으로 못 봄 → 날짜 있는 사례 목록만
    dated = [(i, s) for i, s in enumerate(sents, 1) if re.search(r"20\d\d년 \d+월 \d+일", s)]
    warns.append(f"반론 K1·K3 (사람 확인 — 조건이 먼저 못 박혔나 · 다른 기간이면 뒤집히나: calc 노트·precheck): 날짜 사례 {len(dated)}개 {[i for i, _ in dated]}")
    return fails, warns, oks


FIELDS_TOPIC = [("message", "전달 내용"), ("approach", "전달 방식"), ("title", "제목"), ("thumb_main", "썸네일 문구"), ("thumb_sub", "썸네일 보조 문구")]
FIELDS_SHORTS = [("s_title", "쇼츠 제목"), ("s_thumb_main", "쇼츠 썸네일 문구"), ("s_thumb_sub", "쇼츠 썸네일 보조 문구"), ("s_message", "쇼츠 전달 내용·방식")]


def txt(v):
    return " / ".join(v) if isinstance(v, list) else str(v or "")


def check_package(topic, pk, personas, adv, stage="topic"):
    import title_fit as TF
    fails, warns, oks = [], [], []
    FIELDS = FIELDS_TOPIC if stage == "topic" else FIELDS_SHORTS
    miss = [lab for k, lab in FIELDS if not txt(pk.get(k)).strip()]
    if miss:
        fails.append(f"빈 칸: {miss}")
    allt = " ".join(txt(pk.get(k)) for k, _ in FIELDS)
    # 일반 페르소나 — 원하는 말 · 어려운 말 · 길이
    hit = {p["id"]: [w for w in p["wants"] if w.lower() in allt.lower()] for p in personas}
    best = max(hit.items(), key=lambda x: len(x[1]))
    (oks if best[1] else warns).append(f"일반: 페르소나 원하는 말 — " + " · ".join(f"{k} {len(v)}" for k, v in hit.items()) + (f" (가장 가까운 {best[0]}: {best[1][:5]})" if best[1] else " — 아무도 안 걸림(사람 확인)"))
    hard = [t for t in adv if t in allt]
    (warns if hard else oks).append(f"일반: 어려운 말 {hard or '없음'} (대본에서 풀이 필요)")
    tm = txt(pk.get("thumb_main" if stage == "topic" else "s_thumb_main")).replace(" / ", "")
    (warns if len(tm) > 26 else oks).append(f"일반: 썸네일 주요 문구 {len(tm)}자 (성공 중앙값 22 — 26 넘으면 줄임)")
    for key, sh in ((("title", False),) if stage == "topic" else (("s_title", True),)):
        t = txt(pk.get(key))
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            ok = TF.report(t, sh) if t else False
        (oks if ok else fails).append(f"일반: {'쇼츠 ' if sh else ''}제목 화면 2줄 안 {'✅' if ok else '❌ 잘림'} ({len(t)}자)")
    # 반론
    k8 = [k for k, _ in FIELDS if K8.search(txt(pk.get(k)))]
    (fails if k8 else oks).append(f"반론 K8 권유·과장 낱말: {k8 or '없음'}")
    k2 = [k for k, _ in FIELDS if K2.search(txt(pk.get(k)))]
    (fails if k2 else oks).append(f"반론 K2 결과론 낱말: {k2 or '없음'}")
    off = OFF.search(allt)
    (fails if off else oks).append(f"채널 목적(덜 잃기·장기): {'❌ ' + off.group(0) if off else '맞음'}")
    nums = [k for k, _ in FIELDS if k not in ("message", "approach", "s_message") and re.search(r"\d", txt(pk.get(k)))]
    (warns if nums and not pk.get("calc") else oks).append(f"반론 K5 숫자 칸 {nums or '없음'} · 계산 근거 {'있음' if pk.get('calc') else '없음 — 숫자는 대본 계산 때 확인'}")
    if stage == "topic":
        (oks if COND.search(txt(pk.get("approach"))) else warns).append("반론 K1 조건(돈 쓸 때·기간·비중)을 보기에 못 박았나: " + ("있음" if COND.search(txt(pk.get("approach"))) else "안 보임(사람 확인)"))
        (oks if txt(pk.get("verify")).strip() else fails).append(f"반론 K3 다른 기간·다른 하락장으로 확인할 길: {txt(pk.get('verify')) or '없음'}")
        (oks if txt(pk.get("basis")).strip() else warns).append("분석 근거(data_insights 5-1): " + ("있음" if txt(pk.get("basis")).strip() else "없음"))
    else:
        (oks if "구독하고 확인하세요" in txt(pk.get("s_message")) or "공통 끝 멘트" in txt(pk.get("s_message")) else warns).append("쇼츠 공통 끝 멘트: " + ("있음" if "끝 멘트" in txt(pk.get("s_message")) or "구독하고" in txt(pk.get("s_message")) else "안 보임"))
    return fails, warns, oks


def main(argv):
    if len(argv) < 3 or argv[0] not in ("script", "package"):
        print(__doc__)
        return 2
    mode, topic, path = argv[0], argv[1], argv[2]
    opt = lambda k: argv[argv.index(k) + 1] if k in argv else None  # noqa: E731
    allow = [argv[i + 1] for i, a in enumerate(argv) if a == "--allow"]
    log("START", tool=f"board_check.py {VERSION}", mode=mode, topic=topic, path=path)
    if mode == "script":
        f, w, o = check_script(topic, path, opt("--calc"), opt("--upload"), allow, opt("--kind") or "long")
        out = Path(path).resolve().with_name("board_check.md" if (opt("--kind") or "long") == "long" else "board_check_shorts.md")
        md = [f"# 평가판 전 점검 — {Path(path).name} ({time.strftime('%Y-%m-%d')}, board_check.py {VERSION})", "", f"결과: {'❌ 고칠 것 ' + str(len(f)) if f else '✅ 통과'} · ⚠ 사람 확인 {len(w)}", ""]
        md += [f"- ❌ {x}" for x in f] + [f"- ⚠ {x}" for x in w] + [f"- ✅ {x}" for x in o]
        out.write_text("\n".join(md) + "\n", "utf-8")
        log("DONE", fails=len(f), warns=len(w), out=str(out.relative_to(ROOT)))
        for x in f + w:
            print("   ", x[:300])
        return 1 if f else 0
    import personas as pz
    P = json.loads((ROOT / topic / "result" / "outliers" / "personas.json").read_text("utf-8"))
    personas = [{"id": p["id"], "wants": [t for t, _ in p["want_terms"][:8]] + [w for w, c in p["want_words"][:8] if c >= 2]} for p in P["personas"]]
    with contextlib.redirect_stdout(io.StringIO()):
        cfg, _ = pz.load_cfg(topic, ROOT)
    k = (cfg or {}).get("know") or {}
    adv = list(dict.fromkeys((k.get("advanced") or []) + (k.get("advanced_en") or [])))
    D = json.loads(Path(path).read_text("utf-8"))
    bad = 0
    stage = opt("--stage") or "topic"
    for pk in D["packages"]:
        f, w, o = check_package(topic, pk, personas, adv, stage)
        pk["check" if stage == "topic" else "check_shorts"] = {"tool": f"board_check.py {VERSION}", "at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "pass": not f,
                       "fail": f, "warn": w, "ok": o}
        bad += bool(f)
        log("CHECK", id=pk.get("id"), result="통과" if not f else "고칠 것", fails=len(f), warns=len(w))
        for x in f + w:
            print("   ", x[:240])
    if "--write" in argv:
        Path(path).write_text(json.dumps(D, ensure_ascii=False, indent=1) + "\n", "utf-8")
    log("DONE", packages=len(D["packages"]), fail=bad, wrote="--write" in argv)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
