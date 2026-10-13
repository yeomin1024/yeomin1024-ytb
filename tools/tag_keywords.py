#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-13 — 신규 (사용자 지시: "그냥 검색어를 재테크 관련 태그로 찾아서 다 그걸로 탐색해봐"):
#          검색어를 사람이 정하지 않고, 실제 영상들이 쓰는 태그에서 고른다.
#          ① <주제>/tag_rules.toml 의 TAG_SEEDS 로 검색 (tools/outlier_research.py 와 같은 캐시 — 최근 365일·조회수 순·4~20분·20분 넘음)
#          ② 지금까지 받은 영상 정보(캐시) 중 주제 관련 영상(keywords.toml 관련어)의 태그를 모음
#          ③ TAG_EXCLUDE(경제 등)를 빼고, 채널 MIN_CHANNELS 곳 이상이 쓴 태그를 채널 수 순으로 MAX_TAGS 개
#          ④ TAG_THEMES 로 묶어 표(<주제>/tag_candidates.md·.csv — keywords.toml 옆. result/ 는 PC 푸시가 통째로 바꾸므로 거기 두지 않음)를 쓰고, --write-keywords 면 keywords.toml 의
#             [KEYWORD_GROUPS] 를 그 태그로 다시 씀 (관련어 등 나머지는 그대로) → 분석기·성공 사례 수집이 모두 태그로 탐색
r"""
사용법 (저장소 최상위 또는 PC 실행 폴더):
  python tools/tag_keywords.py economic                       # 씨앗 검색 + 태그 표만 (keywords.toml 은 그대로)
  python tools/tag_keywords.py economic --write-keywords      # 표 + keywords.toml 의 검색어를 태그로 바꿈
  python tools/tag_keywords.py economic --no-seed-search      # 검색 없이 이미 받은 영상의 태그로만 (할당량 0)
  옵션: --max-tags 40 --min-channels 5 (tag_rules.toml 값 대신), --quota 1000 (씨앗 검색 한도)
할당량: 씨앗 1개 = 검색 2번 = 200단위 (+ 영상 정보 50개에 1단위). 이미 받은 검색은 7일 동안 캐시(0단위).
로그: [STAGE] [시각] key=value (START·SEED·TAGS·WRITE·DONE)
※ 연구·교육용. 투자 권유가 아니다.
"""
import argparse
import csv
import json
import logging
import re
import sys
import types
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import outlier_research as orr          # noqa: E402  같은 캐시·같은 관련어 규칙을 씀

ROOT = orr.ROOT
VERSION = "v1.0"
LOG = logging.getLogger("tag_keywords")


def log(stage, level=logging.INFO, **kv):
    LOG.log(level, "[%s] [%s] %s", stage, datetime.now().isoformat(timespec="seconds"),
            " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) and ' ' in v else v}" for k, v in kv.items()))


def load_rules(topic):
    p = ROOT / topic / "tag_rules.toml"
    if not p.is_file():
        raise SystemExit(f"[START] ❌ {p} 없음 — 태그 규칙 파일을 먼저 만드세요 (예: economic/tag_rules.toml)")
    d = orr.tomllib.loads(p.read_text("utf-8"))
    return {"seeds": list(d.get("TAG_SEEDS") or []), "min_channels": int(d.get("MIN_CHANNELS") or 5),
            "max_tags": int(d.get("MAX_TAGS") or 40), "exclude": [str(x) for x in d.get("TAG_EXCLUDE") or []],
            "keep": [orr._norm(x) for x in d.get("TAG_KEEP") or []],
            "themes": {str(k): [str(x) for x in v] for k, v in (d.get("TAG_THEMES") or {}).items()}, "path": p}


def cached_infos(out):
    """성공 사례 캐시(out/.cache)에 있는 영상 정보 전부 (검색·채널 캐시 파일은 빼고)."""
    infos = []
    for f in sorted((out / ".cache").glob("*.json")):
        if f.name.startswith("search_") or f.name == "channels.json":
            continue
        try:
            infos.append(json.loads(f.read_text("utf-8")))
        except ValueError:
            continue
    return infos


def tag_stats(infos, rel):
    """주제 관련 영상의 태그 → {태그(대표 표기): {videos, channels, views}}. 대소문자·띄어쓰기만 다른 태그는 하나로."""
    stats, label = {}, {}
    for i in infos:
        if not orr.relevant(i, rel):
            continue
        for t in {str(x).strip().lstrip("#") for x in (i.get("tags") or [])}:
            if not t:
                continue
            key = orr._norm(t)
            label.setdefault(key, {})
            label[key][t] = label[key].get(t, 0) + 1
            s = stats.setdefault(key, {"videos": 0, "channels": set(), "views": 0})
            s["videos"] += 1
            s["channels"].add(i.get("channel_id"))
            s["views"] += int(i.get("view_count") or 0)
    out = {}
    for key, s in stats.items():
        name = max(label[key].items(), key=lambda kv: kv[1])[0]          # 가장 많이 쓰인 표기
        out[name] = {"videos": s["videos"], "channels": len(s["channels"]), "views": s["views"]}
    return out


def theme_of(tag, themes):
    """맞는 글자가 가장 긴 묶음 (같으면 위쪽 묶음). 예: 연금저축펀드 → '연금저축'(4글자)이 든 노후·연금, 부동산투자 → 부동산."""
    low, best, best_len = tag.lower(), "기타 재테크", 0
    for name, words in themes.items():
        n = max((len(w) for w in words if w.lower() in low), default=0)
        if n > best_len:
            best, best_len = name, n
    return best


def choose(stats, rules, max_tags, min_channels):
    """→ (고른 태그 [(태그, 통계, 묶음)], 표 행 전부). 빼는 까닭도 남김."""
    rows = []
    for t, s in sorted(stats.items(), key=lambda kv: (-kv[1]["channels"], -kv[1]["videos"], kv[0])):
        why = ""
        keep = any(k in orr._norm(t) for k in rules["keep"])                  # TAG_KEEP: 빼는 말이 들어 있어도 씀
        if not keep and any(x.lower() in t.lower() for x in rules["exclude"]):
            why = "빼는 말 (TAG_EXCLUDE)"
        elif not (2 <= len(t) <= 20):
            why = "길이"
        elif s["channels"] < min_channels:
            why = f"채널 {min_channels}곳 미만"
        rows.append({"tag": t, **s, "theme": theme_of(t, rules["themes"]), "why": why})
    picked = [r for r in rows if not r["why"]][:max_tags]
    picked_set = {r["tag"] for r in picked}
    for r in rows:
        if not r["why"] and r["tag"] not in picked_set:
            r["why"] = f"상위 {max_tags}개 밖"
    return picked, rows


def write_table(dst, topic_name, picked, rows, n_videos, n_relevant, seeds, args):
    """dst = <주제> 폴더 (keywords.toml·tag_rules.toml 옆) → tag_candidates.md (GitHub 에서 바로 보이는 표) + tag_candidates.csv."""
    L = [f"# {topic_name} — 태그로 고른 검색어", "",
         f"자동 생성 — `tools/tag_keywords.py` {VERSION} ({datetime.now().strftime('%Y-%m-%d %H:%M')}). "
         f"영상 {n_videos:,}개 중 주제 관련 {n_relevant:,}개의 태그 · 씨앗 검색: {', '.join(seeds) or '없음'}", "",
         f"규칙: 채널 {args.min_channels}곳 이상이 쓴 태그 · 빼는 말 제외 · 채널 수 순 {args.max_tags}개 → "
         f"{'`keywords.toml` 검색어로 씀' if args.write_keywords else '표만 (keywords.toml 은 그대로 — --write-keywords 로 바꿈)'}", "",
         "| # | 태그 | 채널 수 | 영상 수 | 묶음 | 검색어로 씀 |", "|---|---|---|---|---|---|"]
    rank = {r["tag"]: k for k, r in enumerate(picked, 1)}
    for r in rows[:200]:
        L.append(f"| {rank.get(r['tag'], '')} | {r['tag']} | {r['channels']} | {r['videos']} | {r['theme']} | "
                 f"{'✅' if r['tag'] in rank else '– ' + r['why']} |")
    (dst / "tag_candidates.md").write_text("\n".join(L) + "\n", "utf-8")
    with open(dst / "tag_candidates.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=["rank", "tag", "channels", "videos", "views", "theme", "why"])
        w.writeheader()
        for r in rows:
            w.writerow({"rank": rank.get(r["tag"], ""), **{k: r[k] for k in ("tag", "channels", "videos", "views", "theme", "why")}})


def rewrite_keyword_groups(kw_path, picked, note):
    """keywords.toml 의 [KEYWORD_GROUPS] 블록만 태그 묶음으로 다시 씀 (다른 줄은 그대로). 쓴 뒤 TOML 로 다시 읽어 검사."""
    text = kw_path.read_text("utf-8")
    head = re.compile(r"^\[KEYWORD_GROUPS\][ \t]*(#.*)?$", re.M).search(text)    # 표 머리 줄만 (주석 속 글자는 아님)
    if not head:
        raise SystemExit(f"[WRITE] ❌ {kw_path} 에 [KEYWORD_GROUPS] 줄이 없음 — 파일을 확인하세요")
    start = head.start()
    nxt = re.compile(r"^\[", re.M).search(text, head.end())
    end = nxt.start() if nxt else len(text)
    groups = {}
    for r in picked:
        groups.setdefault(r["theme"], []).append(r["tag"])
    order = sorted(groups, key=lambda g: (g == "기타 재테크", [int(x) for x in re.findall(r"^\d+", g)] or [99], g))
    block = ["[KEYWORD_GROUPS]", f"# {note}"]
    names = {}
    for k, g in enumerate(order, 1):                       # 빈 묶음을 건너뛴 번호를 1부터 차례로 다시 (예: 9. 코인 → 7. 코인)
        names[g] = f"{k}. {re.sub(r'^\d+\.\s*', '', g)}"
        block.append(f"{json.dumps(names[g], ensure_ascii=False)} = [")
        block += [f"  {json.dumps(t, ensure_ascii=False)}," for t in groups[g]]
        block.append("]")
    new = text[:start] + "\n".join(block) + "\n\n" + text[end:]
    before, after = orr.tomllib.loads(text), orr.tomllib.loads(new)     # 형식 검사 (깨지면 쓰지 않음)
    want = {names[g]: groups[g] for g in order}
    if after.get("KEYWORD_GROUPS") != want or set(after) != set(before) or \
            any(after[k] != before[k] for k in before if k != "KEYWORD_GROUPS"):
        raise SystemExit(f"[WRITE] ❌ {kw_path} 을 다시 쓰면 검색어 말고 다른 설정이 바뀜 — 쓰지 않음 (파일 모양을 확인하세요)")
    kw_path.write_text(new, "utf-8")
    return {names[g]: len(groups[g]) for g in order}


def main(argv=None):
    ap = argparse.ArgumentParser(description="실제 영상 태그에서 검색어 고르기 (재테크 등) — 표 + keywords.toml 검색어 다시 쓰기")
    ap.add_argument("topic")
    ap.add_argument("--write-keywords", action="store_true", help="keywords.toml 의 [KEYWORD_GROUPS] 를 고른 태그로 바꿈")
    ap.add_argument("--no-seed-search", action="store_true", help="씨앗 검색 없이 이미 받은 영상의 태그로만 (할당량 0)")
    ap.add_argument("--max-tags", type=int, help="검색어로 쓸 태그 수 (tag_rules.toml MAX_TAGS 대신)")
    ap.add_argument("--min-channels", type=int, help="이만큼 다른 채널이 쓴 태그만 (MIN_CHANNELS 대신)")
    ap.add_argument("--quota", type=int, default=1000, help="씨앗 검색 할당량 한도")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    args = ap.parse_args(argv)
    logging.basicConfig(level=getattr(logging, args.log_level), format="%(message)s", stream=sys.stdout)
    orr.logging.getLogger("outlier").setLevel(getattr(logging, args.log_level))
    rules = load_rules(args.topic)
    args.max_tags = args.max_tags or rules["max_tags"]
    args.min_channels = args.min_channels or rules["min_channels"]
    out = ROOT / args.topic / "result" / "outliers"
    (out / ".cache").mkdir(parents=True, exist_ok=True)
    _, exclude, topic_name, kw_file, rel = orr.load_keywords(args.topic, 0)
    log("START", topic=args.topic, name=topic_name, seeds=",".join(rules["seeds"]), max_tags=args.max_tags,
        min_channels=args.min_channels, write_keywords=args.write_keywords, tool=f"tag_keywords.py {VERSION}")
    used = 0
    if rules["seeds"] and not args.no_seed_search:
        key, src = orr.load_api_key(args.topic)
        if not key:
            raise SystemExit("[SEED] ❌ YOUTUBE_API_KEY 없음 — 키를 넣거나 --no-seed-search")
        api = orr.Api(key, args.quota)
        a = types.SimpleNamespace(fallback_days=365, long=True, search_ttl_hours=orr.SEARCH_TTL_HOURS, refresh=False)
        state = orr.new_state()
        orr.collect_api(args.topic, a, api, [("씨앗", s) for s in rules["seeds"]], exclude, out, state)
        used = api.used
        log("SEED", searches_new=state["searched"], searches_cached=state["search_cached"], pending=len(state["pending_searches"]),
            quota_used=used, key_source=src)
    infos = cached_infos(out)
    n_rel = sum(1 for i in infos if orr.relevant(i, rel))
    stats = tag_stats(infos, rel)
    picked, rows = choose(stats, rules, args.max_tags, args.min_channels)
    log("TAGS", videos=len(infos), relevant=n_rel, distinct_tags=len(stats), picked=len(picked),
        top=",".join(r["tag"] for r in picked[:15]))
    write_table(ROOT / args.topic, topic_name, picked, rows, len(infos), n_rel, rules["seeds"], args)
    if args.write_keywords and picked:
        note = (f"태그에서 고른 검색어 {len(picked)}개 — tools/tag_keywords.py {VERSION} {datetime.now().strftime('%Y-%m-%d')} "
                f"(관련 영상 {n_rel:,}개·채널 {args.min_channels}곳 이상·표: tag_candidates.md). 손으로 고쳐도 됨")
        groups = rewrite_keyword_groups(kw_file, picked, note)
        log("WRITE", file=str(kw_file.relative_to(ROOT)), groups=len(groups), keywords=sum(groups.values()),
            themes=",".join(f"{g}:{n}" for g, n in groups.items()))
    log("DONE", topic=args.topic, picked=len(picked), quota_used=used, table=str((ROOT / args.topic / "tag_candidates.md").relative_to(ROOT)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
