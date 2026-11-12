# VERSION: v1.0 — 2026-11-12 — 위기 상황 제목·썸네일 패널 답 모아 판정 (tools/ctr_check.py 의 'title+trust' 판정을 이 주제 데이터로)
"""python3 crisis/code/ctr_report.py crisis/source/ctr/ctr_2026-11-12.json <n> crisis/source/ctr/answers/r<n>_*.json

- 클릭 = 페르소나 4명 점수의 가중 평균 (무게 = 최종 페르소나 댓글 몫, pass_rule.weights), 검토자 평균.
- 패널 타당성: 실제 성공(HIT) 앵커 평균 − 덜 된(MISS) 앵커 평균 ≥ panel_valid_gap 이면 클릭도 판정에 씀.
  아니면 클릭은 참고만 (역사 패널도 거꾸로 매겼음 — tools/ctr_check.py v1.4 'title+trust').
- 편마다: 본안 = trust ≥ trust_best_min 인 안 중 data_score 가 가장 큰 안 (패널이 타당하면 클릭 ≥ HIT 평균도).
  나머지 두 안 trust ≥ trust_others_min. 본안 data_score ≥ data_mid.
- 결과: 같은 폴더 ctr_report.md + json rounds 에 회차 저장.
로그: [STAGE] [시각] key=value
※ 페르소나 패널은 시뮬레이션 — 진짜 클릭률은 스튜디오 '테스트 및 비교'로만 안다. 나쁜 안을 먼저 거르는 데만 쓴다. 연구·교육용.
"""
import json
import logging
import sys
from datetime import datetime
from pathlib import Path
from statistics import mean, pstdev

logging.basicConfig(level=logging.INFO, format="%(message)s")
LOG = logging.getLogger("ctr_report")


def L(stage, **kv):
    LOG.info(f"[{stage}] [{datetime.now():%Y-%m-%dT%H:%M:%S}] " + " ".join(f"{k}={v}" for k, v in kv.items()))


def main(argv):
    path, n, answers = Path(argv[1]), int(argv[2]), [Path(a) for a in argv[3:]]
    d = json.loads(path.read_text())
    rule = d["pass_rule"]
    w = rule["weights"]                     # F1~F4 → P1~P4
    wv = [w["F1"], w["F2"], w["F3"], w["F4"]]
    A = [json.loads(a.read_text()) for a in answers]
    L("LOAD", file=path.name, round=n, reviewers=len(A), ids=len(A[0]["scores"]) if A else 0)
    items = {c["id"]: dict(c, src="ours") for c in d["candidates"]} | {a["id"]: dict(a, src="anchor") for a in d["anchors"]}
    res = {}
    for i, it in items.items():
        clicks, trusts, flags = [], [], []
        for a in A:
            s = a["scores"].get(i)
            if not s:
                L("LOAD", level="WARN", missing=i, reviewer=a.get("reviewer"))
                continue
            p = [s["P1"], s["P2"], s["P3"], s["P4"]]
            clicks.append(sum(x * y for x, y in zip(p, wv)) / sum(wv))
            trusts.append(s["trust"])
            flags += [f"{a.get('reviewer')}: {f}" for f in s.get("flags", [])]
        res[i] = dict(click=round(mean(clicks), 2), click_sd=round(pstdev(clicks), 2), trust=round(mean(trusts), 2),
                      p=[round(mean(a["scores"][i][k] for a in A if i in a["scores"]), 2) for k in ("P1", "P2", "P3", "P4")],
                      flags=flags)
    H = mean(res[a["id"]]["click"] for a in d["anchors"] if a["kind"] == "HIT")
    M = mean(res[a["id"]]["click"] for a in d["anchors"] if a["kind"] == "MISS")
    valid = H - M >= rule["panel_valid_gap"]
    L("SIGNAL", hit_click=round(H, 2), miss_click=round(M, 2), gap=round(H - M, 2), need=rule["panel_valid_gap"], panel_click_valid=valid)
    verdict = {}
    for g in sorted({c["group"] for c in d["candidates"]}):
        vs = [c for c in d["candidates"] if c["group"] == g]
        ok_best = [c for c in vs if res[c["id"]]["trust"] >= rule["trust_best_min"] and (not valid or res[c["id"]]["click"] >= H)]
        best = max(ok_best, key=lambda c: (c["data_score"], res[c["id"]]["trust"])) if ok_best else None
        others = [c for c in vs if best is None or c["id"] != best["id"]]
        checks = {
            "본안 있음 (trust≥%.0f%s)" % (rule["trust_best_min"], ", 클릭≥HIT" if valid else ""): best is not None,
            "본안 제목 점수 ≥ %.2f" % rule["data_mid"]: best is not None and best["data_score"] >= rule["data_mid"],
            "나머지 두 안 trust ≥ %.0f" % rule["trust_others_min"]: all(res[c["id"]]["trust"] >= rule["trust_others_min"] for c in others),
        }
        verdict[g] = dict(best=best["id"] if best else None, ok=all(checks.values()), checks=checks)
        L("DECISION", group=g, best=verdict[g]["best"], ok=verdict[g]["ok"],
          fail=[k for k, x in checks.items() if not x] or "-")
    d["rounds"] = [r for r in d.get("rounds", []) if r["n"] != n] + [dict(n=n, reviewers=[a.get("reviewer") for a in A], H=round(H, 2), M=round(M, 2),
                                                                         panel_click_valid=valid, scores=res, verdict=verdict)]
    path.write_text(json.dumps(d, ensure_ascii=False, indent=1))
    out = [f"# 위기 상황 — 제목·썸네일 패널 {n}회차 (ctr_report.py v1.0, {datetime.now():%Y-%m-%d})", "",
           f"- 검토자 {len(A)}명 (서로 모름, 지시문 `panel_{n}_prompt.md` 만 읽음) · 클릭 = P1~P4 가중 평균 (무게 {wv})",
           f"- 제목 점수 = 제목 형식+위험 유형 (5겹 교차 AUC 0.744, seed 42) — `ctr_2026-11-12.json` validate",
           f"- **패널 타당성:** 실제 성공 앵커 클릭 {H:.2f} vs 덜 된 앵커 {M:.2f} (차이 {H - M:+.2f}, 기준 +{rule['panel_valid_gap']}) → "
           + ("클릭도 판정에 씀" if valid else "**클릭은 참고만** (패널이 실제 성공을 가려내지 못함)"), "",
           "| ID | 제목 | 썸네일 큰 글 | 제목 점수 | 클릭(참고) | P1 웃음 | P2 감정 | P3 전문 | P4 판정 | 믿음 |", "|---|---|---|---|---|---|---|---|---|---|"]
    for i in sorted(items, key=lambda k: (items[k]["src"] != "ours", k)):
        it, r = items[i], res[i]
        tag = f" ({it['kind']})" if it["src"] == "anchor" else ""
        out.append(f"| {i}{tag} | {it['title'][:40]} | {' / '.join(it['thumb_main'])} | {it['data_score']} | {r['click']} ±{r['click_sd']} | "
                   + " | ".join(str(x) for x in r["p"]) + f" | {r['trust']} |")
    out += ["", "## 편마다 판정", ""]
    for g, v in verdict.items():
        out.append(f"- **{g}** 본안 {v['best'] or '없음'} — " + ("✅" if v["ok"] else "❌") + " · " + " · ".join(f"{k} {'✅' if x else '❌'}" for k, x in v["checks"].items()))
    out += ["", "## 검토자 메모 (우리 안만)", ""]
    for c in d["candidates"]:
        out.append(f"- **{c['id']}** " + " / ".join(res[c["id"]]["flags"][:6]))
    (path.parent / "ctr_report.md").write_text("\n".join(out) + "\n")
    L("EXPORT", file=str(path.parent / "ctr_report.md"), groups=len(verdict), all_ok=all(v["ok"] for v in verdict.values()))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
