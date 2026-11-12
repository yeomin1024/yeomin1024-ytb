#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-11-12 — 새로 (사용자 지시 2026-11-12 "4가지 대본 만드는 것 까지 해봐 챗지피티한테도 페르소나로 검증해보라고 할거니까 명령 알려주고"):
#          페르소나(<주제>/result/outliers/personas.json — 최근 흐름 포함) + 대본 검토 규칙 + 대본(문장 번호) + 편마다 근거 요약을 한 파일로 →
#          ChatGPT 가 커밋 고정 주소 하나로 끝까지 읽고 페르소나마다 답하게. 편 목록은 <주제>/source/chatgpt_review_list.json.
#          할당량·네트워크 0. ※ 연구·교육용.
"""ChatGPT 페르소나 검증 파일 만들기

  python3 tools/chatgpt_persona_review.py psychology        # → psychology/source/chatgpt_persona_review.md
로그: [STAGE] [시각] key=value (START·EPISODE·WRITE)
"""
import argparse, json, logging, re, sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VERSION = "v1.0"
LOG = logging.getLogger("gptreview")
RULES = [
    "결론을 앞(첫 40초)에 말하고, 대본 전체가 그 결론을 증명하는 순서인가.",
    "**애매한 말 금지** — 무엇을·어떻게 하는지 그 문장에서 알 수 있어야 한다 ('그냥 두면'·'이대로 가면'·'그렇게 하면' ✗). 그 분야 지식이 하나도 없는 50~70대가 한 번 듣고 알아듣는가.",
    "어려운 말은 처음 나올 때 풀어 쓴다 (예: 부모화, 적대적 귀인 편향, 거부 민감성, 메타분석).",
    "연구를 말할 때는 **왜·어떻게 조사했는지**(누구를·몇 명·어떤 방법)를 같이 말한다. 연구가 말하지 않은 것을 연구 결과처럼 말하면 안 된다 (원인·결과 단정 ✗).",
    "일반화·피해자 탓 ✗ — '이런 사람은 다 ~다' · '부모 탓' · '당신 잘못' 같은 말. 진단·치료를 권하는 말투 ✗ (힘들면 상담을 권하는 한 줄은 됨).",
    "정보가 없는 감상 문장 ✗ · 같은 말 되풀이 ✗ · 한 문장 한 뜻 · 조사를 빼지 않음.",
    "진행자 개인 경험을 지어내지 않는다 ('저도 처음엔…' ✗).",
    "마지막 문장은 \"시청해주셔서 감사합니다.\"",
    "제목·썸네일 문구가 약속한 것(예: '3가지')을 대본이 정확히 지키는가 — 시청자 불만 1위가 '제목 낚시'.",
]


def log(stage, **kv):
    LOG.info("[%s] [%s] %s", stage, datetime.now().isoformat(timespec="seconds"), " ".join(f"{k}={v}" for k, v in kv.items()))


def pct(x):
    return f"{x * 100:.0f}%"


def names(xs, k):
    return ", ".join(str(x[0] if isinstance(x, (list, tuple)) else x) for x in (xs or [])[:k]) or "근거 없음"


def build(topic):
    base = ROOT / topic
    d = json.loads((base / "result/outliers/personas.json").read_text("utf-8"))
    eps = json.loads((base / "source/chatgpt_review_list.json").read_text("utf-8"))
    log("START", topic=topic, tool=f"chatgpt_persona_review.py {VERSION}", personas=len(d["personas"]), episodes=len(eps), personas_made=d.get("made"))
    L = [f"# {topic} 대본 {len(eps)}편 — 시청자 페르소나 검증 (ChatGPT 용)", "",
         f"만든 때 {datetime.now().strftime('%Y-%m-%d')} · 저장소 yeomin1024/yeomin1024-ytb · 페르소나 = 실제 유튜브 댓글 {d['data']['comments']:,}개로 만든 시청자 묶음 "
         f"(`{topic}/result/outliers/personas.md`, {d['tool']}, 만든 때 {d['made']}) · 대본 = `{topic}/source/<영상ID>/<영상ID>.txt` · 이 파일 = `tools/chatgpt_persona_review.py {VERSION}`.",
         "※ 연구·교육용 — 진단·치료 영상이 아니다.", "",
         "## 0. 할 일 (ChatGPT 에게)", "",
         f"1. 아래 **1번 페르소나 {len(d['personas'])}명**이 되어, **3번 대본 {len(eps)}편**을 차례로 읽는다. 대본은 진행자 한 사람이 읽는 내레이션이다. 줄 앞 숫자 = 문장 번호, [ ] = 챕터 이름(읽지 않음).",
         "2. 페르소나마다 그 사람의 나이·처지·지식 수준·원하는 것·싫어하는 것으로 판단한다 (내 생각이 아니라 그 사람의 반응).",
         "3. **2번 검토 규칙**을 어긴 문장을 찾는다 — 문장 번호와 까닭.",
         "4. 이 파일 밖의 정보로 대본을 바꾸지 않는다. 다만 '사실이 아닐 수 있다'고 보이면 '사실 확인' 칸에 적는다 (출처는 각 편 '근거 요약').",
         "5. **4번 답 양식** 그대로 답한다. 칭찬보다 고칠 점을 먼저, 구체적으로 (문장 번호 → 원문 → 고친 문장).", "",
         f"## 1. 시청자 페르소나 {len(d['personas'])}명 (몫 = 처지를 스스로 밝힌 댓글 {d['data']['assigned']:,}개 중)", ""]
    for p in d["personas"]:
        t = p.get("trend") or {}
        a = p["age"]
        age = (", ".join(f"{k} {v}명" for k, v in sorted(a["dist"].items(), key=lambda x: -x[1])[:3]) + f" (밝힌 {a['n']}명)") if a["n"] else "밝힌 사람 거의 없음"
        L += [f"### {p['id']} {p['name']} — {pct(p['share'])}" + (f" · 최근 28일 {pct(t['old_share'])} → {pct(t['recent_share'])}" if t.get("recent") else ""),
              f"- 나이: {age}",
              "- 처지 (많은 순): " + (", ".join(f"{s['name']} {pct(s['share'])}" for s in p["states"][:4]) or "근거 없음"),
              f"- 지식 수준: {p['know']['level']} · 이미 아는 말: {names(p['known_terms'], 8)}",
              f"- 원하는 것 (질문 속 낱말): {names(p['want_terms'], 6)} / {names(p['want_words'], 8)}",
              "- 좋아하는 것: " + (", ".join(x["name"] for x in p["likes_cat"][:3]) or "근거 없음") + " · 싫어하는 것: " + (", ".join(x["name"] for x in p["dislikes_cat"][:3]) or "근거 없음"),
              "- 대표 댓글 (작성자 정보 없음): " + " / ".join(f"\"{q['text'][:110]}\"" for q in p["quotes"][:2]), ""]
    b = (d.get("baselines") or [None])[0]
    if b:
        L += ["### 모든 댓글 (참고) — 칭찬·불만 갈래 수", "- 좋아하는 것: " + ", ".join(f"{x['name']} {x['n']}" for x in b["likes_cat"][:5]),
              "- 불만·떠나는 까닭: " + ", ".join(f"{x['name']} {x['n']}" for x in b["dislikes_cat"][:6]), ""]
    tr = d.get("trend") or {}
    if tr.get("rising_words"):
        L += ["### 요즘 흐름 (최근 28일 댓글)", "- 더 나오는 말: " + ", ".join(w["word"] for w in tr["rising_words"][:12]),
              "- 댓글이 몰린 영상: " + " / ".join(v["title"][:40] for v in tr["hot_videos"][:6]), ""]
    L += ["## 2. 검토 규칙 (이 채널 대본 규칙 — 어기면 문장 번호로 적기)", ""] + [f"{i}. {r}" for i, r in enumerate(RULES, 1)] + ["", f"## 3. 대본 {len(eps)}편", ""]
    total = 0
    for e in eps:
        eid = e["id"]
        txt = (base / f"source/{eid}/{eid}.txt").read_text("utf-8").splitlines()
        ev = (base / f"source/{eid}/대본_근거.md").read_text("utf-8")
        src = ev.split("## 1. 사실 문장 ↔ 출처")[1].split("## 2.")[0].strip() if "## 1. 사실 문장 ↔ 출처" in ev else "(근거 파일 없음)"
        L += [f"### {eid} — 「{e['title']}」", "", f"- 썸네일 문구: {e['thumb']}", f"- 대상 페르소나: {e['target']}", "- 근거 요약 (사실 문장 ↔ 출처):", "", src, "", "```"]
        n = 0
        for l in txt:
            if l.startswith("-"):
                L.append(f"      [{l[1:]}]")
            elif l.strip():
                n += 1
                L.append(f"{n:3d}  {l}")
        L += ["```", ""]
        total += n
        log("EPISODE", id=eid, sentences=n, syllables=sum(len(re.findall(r"[가-힣]", l)) for l in txt if not l.startswith("-")))
    L += ["## 4. 답 양식 (이 꼴 그대로)", "", f"### 편마다 ({len(eps)}번 되풀이)", "", "**<영상ID>**", "",
          "| 페르소나 | 제목·썸네일 보고 누를까 (1~5) | 끝까지 볼까 (1~5) | 이해 안 되는 문장 (번호) | 불편하거나 반발할 문장 (번호·까닭) | 더 알고 싶은 것 |",
          "|---|---|---|---|---|---|", "| P1 … | | | | | |", "",
          "| 규칙 (2번) | 어긴 문장 번호 | 원문 | 고친 문장 |", "|---|---|---|---|", "",
          "| 사실 확인이 필요한 문장 | 까닭 |", "|---|---|", "",
          "### 마지막에 한 번", f"- {len(eps)}편 가운데 첫 영상으로 가장 좋은 것 하나와 까닭 (페르소나 반응으로).", f"- {len(eps)}편 모두에 되풀이되는 문제 (있으면).", ""]
    out = base / "source/chatgpt_persona_review.md"
    out.write_text("\n".join(L), "utf-8")
    log("WRITE", file=out.relative_to(ROOT), chars=len("\n".join(L)), sentences=total)


def main(argv=None):
    ap = argparse.ArgumentParser(description="ChatGPT 페르소나 검증 파일")
    ap.add_argument("topic")
    a = ap.parse_args(argv)
    logging.basicConfig(level=logging.INFO, format="%(message)s", stream=sys.stdout)
    build(a.topic)
    return 0


if __name__ == "__main__":
    sys.exit(main())
