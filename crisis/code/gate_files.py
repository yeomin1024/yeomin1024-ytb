# VERSION: v1.2 — 2026-11-12 — 나이 단서가 20개 미만이면 분포 대신 '단서 부족' 글로 (v1.1 에서 P4 나이가 '10대 100%'(단서 1개)로 찍혀 검토자가 10대로 읽음)
# (이전) v1.1 — 2026-11-12 — 혐오·국적 탓 댓글을 반론 갈래·질문 예시에서 뺌 (v1.0 결과에 "경찰이 중국인 아님?"이 K3 예시로 들어감)
# (이전) v1.0 — 2026-11-12 — 위기 상황 독립 분석 결과 → tools/persona_gate.py 가 읽는 꼴 (crisis/result/outliers/)
"""python3 crisis/code/gate_files.py

guides/persona_loop.md 의 반복 검증 도구(tools/persona_gate.py)는 <주제>/result/outliers/ 아래
personas.json · rebuttal_persona.md · compare.csv 를 읽는다. 위기 상황은 표준 분석기가 아니라
crisis_lab.py 결과라 그 꼴로 옮긴다 (숫자·댓글은 crisis_lab 캐시·결과 그대로, 지어내지 않음).

- personas.json      : 최종 페르소나 F1~F4 → id P1~P4 (도구가 'P' 번호를 씀). 실제로 묻는 말 = 그 묶음 댓글 중 물음표가 있는 좋아요 상위.
- rebuttal_persona.md: 반박·정정 댓글을 낱말 규칙으로 K1~K5 갈래 → 갈래마다 몫·좋아요 상위 원문 (작성자 이름 없음).
- compare.csv        : 분석 영상 (주제 안) 제목·올린 날·길이(분) — 피드 시험의 '실제 영상 제목'.
로그: [STAGE] [시각] key=value · 연구·교육용.
"""
import csv
import json
import logging
import re
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import crisis_lab as cl  # noqa: E402

VERSION = "v1.2"
# 사람·국적·지역 탓 댓글은 반론도 질문도 아님 → 갈래·예시에서 뺌 (crisis/guides/channel.md 3번) — v1.1
HATE = r"중국|중국인|조선족|짱깨|무비자|불법체류|외국인|이민자|짱꼴라|신안|밀양|전라도|홍어|경상도|제주도가 더|제주도는 우리나라"
OUT = cl.ROOT / "result" / "outliers"
REBUTTAL = {  # 갈래: (이름, 규칙) — 영상 내용에 맞서는 댓글만
    "K1": ("조건·예외가 빠졌다", r"한정|에서나|경우에만|잔잔한|파도|물살|계곡|바다에서는|상황마다|케바케"),
    "K2": ("한국 현실·사실과 다르다", r"한국에서는|한국은|우리나라는|사례는|단 ?한 ?건|실제로는|현실은"),
    "K3": ("그 방법은 틀렸거나 더 위험하다", r"오히려|더 위험|그러면 안|틀린 정보|틀렸|잘못된|잘못 알려|하면 안 됨|하면 안됨"),  # v1.1: '아님·아닙니다' 는 너무 넓어 뺌
    "K4": ("과장·낚시·AI 티", r"과장|낚시|어그로|AI|에이아이|구라|조작|연출|주작"),
    "K5": ("돈·법·제도 현실을 모른다", r"소송|변호사|보상|배상|처벌|합의|보험|법이"),
}


def L(stage, **kv):
    logging.getLogger("gate").info(f"[{stage}] [{datetime.now():%Y-%m-%dT%H:%M:%S}] " + " ".join(f"{k}={v}" for k, v in kv.items()))


AGE_GUESS = {"F1": "알 수 없음 (쇼츠 웃음 댓글 — 젊은 층으로 보이나 근거 없음)", "F2": "알 수 없음 (어른 — 참사·책임을 말함)",
             "F3": "알 수 없음 (어른 — 현직·경험을 말함)", "F4": "알 수 없음 (어른 — 자녀·가족 이야기가 섞임, 부모 단서 포함)"}


def age_text(f: dict) -> str:
    n = sum((f.get("age_hint") or {}).values())
    if n >= 20:
        return {"dist": f["age_hint"], "level": "나이는 댓글 간접 단서"}
    return f"{AGE_GUESS[f['id']]} — 나이 단서 {n}개뿐이라 나이로 읽지 말 것"


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    cl.setup_logging()
    cl.log.setLevel(logging.ERROR)
    yt = cl.YT(key=None, offline=True)
    vdf = cl.label_success(cl.features(cl.validate(cl.load_videos(yt))))
    cdf = cl.segment(cl.load_comments(yt, vdf))
    hate = cdf["text"].str.contains(HATE, regex=True)
    L("FILTER", hate_comments=int(hate.sum()), kept=int((~hate).sum()))
    cdf = cdf[~hate]
    OUT.mkdir(parents=True, exist_ok=True)

    # personas.json
    fin = json.loads((cl.RESULT_DIR / "personas.json").read_text())["final"]
    segs = {p["key"]: p for p in json.loads((cl.RESULT_DIR / "personas.json").read_text())["segments"]}
    know = {"F1": "안전 지식 없이 재미로 봄 (쇼츠 댓글 96%)", "F2": "사고 뉴스를 챙겨 봄 — 안전 지식은 보통",
            "F3": "현직·경험자·수영 강사 등 — 틀린 정보를 바로잡음", "F4": "보통 — '나라면' 판정 (부모 단서 포함)"}
    dislike = {"F1": ["훈계·긴 설명", "뻔한 말"], "F2": ["참사를 가볍게·자극적으로 다룸", "피해자 탓", "책임 회피"],
               "F3": ["조건 빠진 수칙", "틀린 정보", "근거 없는 숫자"], "F4": ["어려운 말", "할 일이 없는 영상"]}
    out = []
    for i, f in enumerate(fin, 1):
        m = cdf[[f"s_{k}" for k in cl.PERSONA_GROUPS[f["id"]][1]]].sum(axis=1) > 0
        sub = cdf[m]
        q = sub[sub["text"].str.contains(r"\?", regex=True) & sub["text"].str.len().between(10, 120)].nlargest(3, "likes")["text"].tolist()
        words = []
        for k in f["from"]:
            words += segs.get(k, {}).get("top_words", [])[:4]
        out.append({"id": f"P{i}", "name": f["name"], "share": f"{f['share'] * 100:.0f}%",
                    "age": age_text(f),
                    "know": know[f["id"]], "known_terms": [[w] for w in words[:6]], "unknown_terms": [],
                    "want_terms": [[k] for k in list(f["top_danger"])[:2]], "want_words": [],
                    "dislikes_cat": [[d] for d in dislike[f["id"]]], "top_questions": [x.replace("\n", " ") for x in q],
                    "from": f["from"], "like_share": f["like_share"], "top_video_like_share": f["top_video_like_share"]})
    (OUT / "personas.json").write_text(json.dumps({"made": f"crisis gate_files.py {VERSION}", "source": "crisis/result/personas.json final F1~F4 → P1~P4",
                                                    "personas": out}, ensure_ascii=False, indent=1))
    L("PERSONA", personas=len(out), ids=[p["id"] for p in out])

    # rebuttal_persona.md
    lines = ["# 위기 상황 — 반론 페르소나 (crisis/code/gate_files.py v1.1)", "",
             f"댓글 {len(cdf):,}개 중 영상 내용에 맞서는 댓글을 낱말 규칙으로 갈래 지음 (작성자 이름 없음).", "",
             "## 0. 반론 페르소나 — 결론보다 빈틈을 먼저 찾는 시청자", "",
             "안전 영상 밑에 \"○○ 한정\", \"한국은 달라\", \"그러면 오히려 위험\"을 다는 사람. 좋아요가 많이 붙는다.", "",
             "| 갈래 | 묻는 것 | 댓글 수 | 좋아요 많은 원문 |", "|---|---|---|---|"]
    tot = 0
    for k, (name, pat) in REBUTTAL.items():
        m = cdf["text"].str.contains(pat, regex=True)
        tot += int(m.sum())
        ex = cdf[m & cdf["text"].str.len().between(10, 110)].nlargest(2, "likes")["text"].str.replace("\n", " ").tolist()
        lines.append(f"| {k} | {name} | {int(m.sum())} | " + " / ".join(f"「{e}」" for e in ex) + " |")
        L("REBUTTAL", k=k, n=int(m.sum()))
    lines += ["", "- 참사·사고 영상은 **피해자·생존자·구조하던 사람 탓**으로 들리는 말에 반박이 몰린다 (항공 영상 댓글 좋아요 91%가 국내 참사 댓글).", "",
              "## 1. 원문 더 보기", "", "`crisis/result/personas.md` 세부 묶음 fact_checker·pro·justice 대표 댓글."]
    (OUT / "rebuttal_persona.md").write_text("\n".join(lines) + "\n")

    # compare.csv
    with (OUT / "compare.csv").open("w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["title", "published", "minutes", "views", "subs", "success", "exclude"])
        w.writeheader()
        for r in vdf.itertuples():
            w.writerow({"title": r.title, "published": r.published.strftime("%Y-%m-%d"), "minutes": round(r.duration_sec / 60, 2),
                        "views": int(r.views), "subs": int(r.subs) if r.subs == r.subs else "", "success": int(r.success), "exclude": ""})
    L("EXPORT", dir=str(OUT.relative_to(cl.ROOT.parent)), compare_rows=len(vdf), rebuttal_comments=tot)
    return 0


if __name__ == "__main__":
    sys.exit(main())
