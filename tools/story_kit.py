#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.8 — 2026-10-24 — 화면에 투자 영어 허용 (사용자 지시 "국기를 할 필요는 없잖아 그냥 KOSPI, S&P500 이거 달면 되는데 … 다 알만한건 넣어도 돼"):
#          허용 목록 stock/story/screen_words.txt → SPEC.allowWords · 장면 표의 영어가 목록 밖이면 멈춤 · 화면 이름표 title= · K5 글자 칩 'TEXT
#          (밑줄 = 띄어쓰기) · LIST 화면 ('n:+글자; n:!글자') · PIE cap= · 그림 chip·briefcase·school · 썸네일 문구도 목록 낱말은 됨.
# (v1.7) — 2026-10-24 — props 명령: 공통 설명 소품 목록(뜻·쓴 화·그림 있음·후보)을 낱말로 찾음 — 새 화는 있는 소품부터 다시 씀
#          (사용자 지시 "소품 요소를 좀 되도록 다른 주식 관련 영상에서 재사용할 수 있도록 공통된 걸 만들도록 해봐 …").
# (v1.6) — 2026-10-23 — ① 정리 부분 뺌 (사용자 지시 "그냥 정리 부분은 빼자"): 장면 표의 '정리' 줄·K6 정리 카드 없음 (쓰면 문제).
#          ② 설명 소품 그림 (사용자 지시 "설명에 필요한 이미지 요소들은 왜 생성안해?"): 인형 칸에 '*이름' = 무대 위 종이 소품
#          (ChatGPT 그림 stock/story/puppet/props/<이름>.png — 목록 = props_chatgpt.md 표). 소품은 화면 없는 장면이나 BIG 과만 (화면 칸과 겹침).
# (v1.5) — 2026-10-23 — 영어도 없음 (사용자 지시 "야 영어 문구도 넣지마"): 썸네일 문구 = 숫자·기호만(글자면 멈춤 · 1~2줄 · 꼬리표 '#N') · BIG icon=.
# (v1.4) — 2026-10-23 — 화면·썸네일에 한국어 없음 (사용자 지시 "외국인 대상으로도 할거니까 그것도 고려해 영상에 한글 문구 사용하지 말고
#          최대한 이해 잘되도록"): K6 = 줄마다 그림(쉼표·화살표) · PIE 원그래프 · K5 화살표 칸 · K4 icon= · BIG 여러 낱말 · 새 그림 6개 ·
#          썸네일 문구는 쉬운 영어·숫자·기호(한글이면 멈춤) · K6 방법 이름 대체(v1.3)는 뺌.
# (v1.3) — 2026-10-23 — scenes: 정리 카드 줄이 숫자뿐이면 화면 K6 에 제작안의 '방법N · 이름'을 보여 줌 (1화 — 사용자 지시 "일단 1화만 영상 필요 소스 생성해봐").
# (v1.2) — 2026-10-23 — check 에 앞 화와 겹침 검사 (사용자 지시 "70% 잃었다는건 처음 시리즈에서만 말하고 다른데서는 다른 경험으로
#          이야기해야지 중복되면 안돼 다른 내용도 마찬가지야 이전 시리즈에서 썻던 내용들은 똑같이 사용하면 안돼") — dup_check.
# (v1.1) — 2026-10-23 — scenes: 제작안의 '- 도입 통과:' 줄 → SPEC.introOk (사용자가 통과시킨 도입 — render check 도입 35초에서 경고로).
#          사용자 지시 2026-10-23 "도입은 그냥 통과시켜 … 도입 마지노선 35초로해".
# (v1.0) — 2026-10-23 — 새로: '개미 재기 일지'(주식 이야기형) 단계 도구 하나 — 주제 탐색 → 요약본 → 영상 소스 → 영상을 토큰을 가장 덜 쓰게.
#          사용자 지시 2026-10-23 "주제 탐색 -> 요약본 만들기 -> 대본, 썸네일 프롬프트 등 영상 소스 -> 영상 만들기 과정을 토큰을 가장 덜 사용하는 구조로
#          만들어봐 저번에 그렇게 했었으니 참고해서 설계해봐" (재테크 quick_script·quick_package 본보기). 지시사항 stock/guides/quick_story.md.
#          원칙: 긴 파일 대신 이 도구의 짧은 출력을 읽는다 · 썸네일 프롬프트·장면 파일은 손으로 쓰지 않고 만든다 · 출력은 한 화면 안.
#          ※ 연구·교육용 — 투자 권유가 아님.
"""개미 재기 일지 — 단계 도구 (출력은 짧게)

  A 주제   python3 tools/story_kit.py topics [--n 15]
  숫자     python3 tools/story_kit.py nums [키 …]            # stock/story/calc/results.json 한 줄씩 (키 일부로 거름)
  근거     python3 tools/story_kit.py facts [낱말 …] [--url] [--unused]  # facts.md — --unused = 아직 안 쓴 근거만
  B 요약본 python3 tools/story_kit.py new <화> <영상ID> "<전달 내용>"
  C 검사   python3 tools/story_kit.py check <영상ID>         # 제작안 길이·story_check·제목 2줄 — 문제 줄만
  C 내보내기 python3 tools/story_kit.py export <영상ID> --thumb "줄1/줄2" --pose PHONE [--big "−70%"] [--bg HOME-NIGHT]
                                                          # 오디오 대본 · 쇼츠 대본 · 썸네일 프롬프트 3+1장 · 장면 표 초안
  소품     python3 tools/story_kit.py props [낱말 …]           # 공통 설명 소품 목록 (뜻·쓴 화·그림 있음) — 있는 것부터 다시 씀
  D 장면   python3 tools/story_kit.py scenes <영상ID> [--shorts] [--draft] [--force]   # 장면 표 → video/episodes/<영상ID>/index.html
"""
import argparse
import csv
import io
import json
import logging
import re
import subprocess
import sys
import time
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "stock" / "story" / "calc"))
import srt_tool  # noqa: E402

VERSION = "v1.8"
LOG = logging.getLogger("story_kit")
STORY = ROOT / "stock" / "story"
SOURCE = ROOT / "stock" / "source"
RESULTS = STORY / "calc" / "results.json"
FACTS = STORY / "facts.md"
SERIES = STORY / "series.md"
CANDIDATES = ROOT / "stock" / "result" / "outliers" / "comment_title_candidates.tsv"
CHATGPT = STORY / "protagonist_chatgpt.md"
PROPS_FILE = STORY / "puppet" / "props_chatgpt.md"             # v1.6 소품 목록 (표의 저장 경로) — ChatGPT 가 그린다
SCREEN_WORDS = STORY / "screen_words.txt"                      # v1.8 화면에 써도 되는 투자 영어
PROP_RX = re.compile(r"`stock/story/puppet/props/([A-Z0-9]+(?:-[A-Z0-9]+)*)\.png`")
ID_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*-20\d\d-\d\d$")
SYL, GAP = 6.3, 0.45                                   # 진행자 H17 (story_check 와 같음)

STORY_WORDS = ["손절", "포기", "원금", "본전", "복구", "회복", "물타기", "몰빵", "빚", "신용", "반대매매", "레버리지", "멘탈", "조급",
               "욕심", "포모", "FOMO", "존버", "손실", "잃", "파이어", "은퇴", "노후", "공부", "리딩방", "테마", "초보", "개미", "후회", "버티",
               "적립", "장기", "계좌", "마이너스"]
POLITICS = re.compile(r"특검|의원|대통령|정부|정권|민주당|국힘|국민의힘|좌파|우파|탄핵|윤석열|이재명|문재인|호남|영남|빨갱|수꼴|시장개입")
POSES = ["BONSEOK", "WALK", "PHONE", "DESPAIR", "RESOLVE", "STUDY", "BACK", "SMILE", "CROWD"]
BGS = ["HOME-NIGHT", "OFFICE", "STREET-DAWN", "BOARD", "PAPER"]
SCREENS = ["K1", "K2", "K3", "K4", "K5", "BIG", "PIE", "LIST"]           # v1.6 K6 정리 카드 없음
ICONS = ["basket", "drop", "debt", "swap", "x3", "hourglass", "calendar", "phone", "book", "up", "down", "bell", "lock", "globe", "coin", "house",
         "kr", "us", "pct", "fx", "people", "chart", "chip", "briefcase", "school"]   # v1.8 반도체·회사·학원                   # v1.4 국기·금리 %·환율 ₩⇄$·사람들·막대

# 문장 → 표정 (위에서부터 처음 맞는 것) — 장면 표 초안용. 사람이 고친다.
POSE_RULES = [
    ("SMILE", r"응원|바랄게요|힘내|함께 해|감사합니다"),
    ("CROWD", r"남들|단톡방|인증|다 번다|다 벌|포모|FOMO|동료"),
    ("PHONE", r"문자|계좌를|앱을|확인했|빠져나|반대매매|담보"),
    ("DESPAIR", r"잃|손해|날렸|날려|폭락|무너|막막|두렵|걱정|불안|미안|말도 못|모르고|떨어"),
    ("RESOLVE", r"하기로|할 거예요|정했|지키|마음먹|다짐|결심|멈추"),
    ("STUDY", r"공부|복기|찾아|알아보|기록|일지|적어|계산|백테스트|확인해 보"),
    ("BACK", r"깨달|알게 됐|문득|생각이 들|그때"),
    ("WALK", r"출근|퇴근|정류장|새벽|걸어"),
]
BG_RULES = [("BOARD", r"코스피|코스닥|지수|전광판|시장 전체|S&P"), ("OFFICE", r"회사|동료|사무실|점심|공장"),
            ("STREET-DAWN", r"새벽|출근|정류장|버스"), ("HOME-NIGHT", r"아내|딸|집|밤|거실|화장실")]
FIRST = re.compile(r"(?:^|[\s,])(저는|저도|저처럼|저만|저한테|제가|제 |내 |나는|저 )")
NEG = re.compile(r"잃|손해|손실|날렸|날려|떨어|하락|폭락|빠져|반토막|−|마이너스")
POS = re.compile(r"올랐|오르|수익|벌|회복|되찾|늘어|불어")
POSE_EN = {
    "BONSEOK": "standing and facing the viewer, gentle faint smile",
    "WALK": "walking in side view, calm tired face",
    "PHONE": "holding a smartphone and staring at its screen, having just realized he lost the money — knitted eyebrows, eyes wide with dismay, mouth slightly open, shoulders slumped (a defeated, frustrated face, not a frozen surprised face)",
    "DESPAIR": "sitting slumped on the floor with one hand on his forehead and head bowed, eyes shut tight, deeply frustrated and defeated after the loss",
    "RESOLVE": "standing straight with fists clenched at his chest, determined eyes and a firmly closed mouth",
    "STUDY": "sitting at a small desk with an open notebook and a pen, focused serious eyes",
    "BACK": "seen from behind at three-quarter view, looking up at a big blank board, his side face showing quiet realization",
    "SMILE": "raising one hand in a cheering wave with a bright warm smile",
    "CROWD": "(not used alone in thumbnails)",
}
BG_EN = {
    "HOME-NIGHT": "a small Korean apartment living room at night — sofa, low table, a window with distant apartment lights, deep indigo tones",
    "OFFICE": "a production-control office in an auto-parts factory by day — two desks, blank monitors, factory roofs through the window",
    "STREET-DAWN": "an apartment-complex bus stop at dawn — a streetlight and an empty bench, soft blue-gold sky",
    "BOARD": "a financial-district street at night with a huge blank navy electronic board",
    "PAPER": "a plain warm cream paper stage backdrop",
}


def log(stage, level=logging.INFO, **kv):
    LOG.log(level, "[%s] %s %s", stage, time.strftime("%Y-%m-%dT%H:%M:%S"), " ".join(f"{k}={v}" for k, v in kv.items()))


def fail(stage, msg, hint=""):
    log(stage, logging.ERROR, error=msg, next=hint or "-")
    raise SystemExit(1)


def src(vid):
    if not ID_RE.match(vid):
        fail("ARGS", f"영상ID 꼴이 아님: {vid}", "영문 소문자·하이픈 <로마자>-<연>-<월> (예: pogi-sonjeol-2026-10)")
    return SOURCE / vid


def meta(vid):
    p = src(vid) / "story.json"
    return json.loads(p.read_text("utf-8")) if p.exists() else {}


# ---------------------------------------------------------------- A 주제 탐색
def cmd_topics(a):
    print(f"[TOPICS] story_kit {VERSION} — 쓴 주제 · 만드는 중 · 이야기 낱말 댓글 (좋아요 순)")
    for line in SERIES.read_text("utf-8").splitlines():
        if re.match(r"^\| \d+ \| `", line):
            c = [x.strip() for x in line.strip().strip("|").split("|")]
            print(f"  {c[0]}화 {c[1]} · 실수: {c[4][:46]} · 다음: {c[5][:34]}")
    metas = [(json.loads(p.read_text("utf-8")), p) for p in SOURCE.glob("*/story.json")]
    for m, p in sorted(metas, key=lambda x: (x[0].get("ep") or 0, x[0]["id"])):          # 화 순서
        have = [n for n, f in (("요약본", "요약본.md"), ("제작안", f"{m['id']}_제작안.txt"), ("대본", f"{m['id']}.txt"),
                               ("오디오", "narration.mp3")) if (p.parent / f).exists()]
        print(f"  [만드는 중] {m.get('ep')}화 {m['id']} — {m.get('message', '')[:40]} · 있음: {'·'.join(have) or '없음'}")
    if not CANDIDATES.exists():
        print(f"  (댓글 후보 없음 — python3 tools/comment_title_ideas.py stock candidates)")
        return 0
    rows = list(csv.DictReader(CANDIDATES.open(encoding="utf-8"), delimiter="\t"))
    kr = [r for r in rows if r.get("country") == "한국" and any(w in r.get("comment", "") for w in STORY_WORDS)
          and not POLITICS.search(r.get("comment", ""))]          # 정치 댓글은 뺌 (CLAUDE.md 분석 규칙)
    kr.sort(key=lambda r: -int(r.get("likes") or 0))
    seen, shown = set(), 0
    print(f"[COMMENTS] 한국 후보 {sum(r.get('country') == '한국' for r in rows)}개 중 이야기 낱말 {len(kr)}개 — 위 {a.n}개 (comment_title_candidates.tsv)")
    for r in kr:
        key = r["comment"][:30]
        if key in seen:
            continue
        seen.add(key)
        c = re.sub(r"\s+", " ", r["comment"]).strip()
        print(f"  👍{int(r['likes']):>5} {r['kind'][:2]} {c[:84]}{'…' if len(c) > 84 else ''} ‹{r['video_title'][:22]}›")
        shown += 1
        if shown >= a.n:
            break
    cnt = {w: sum(w in r["comment"] for r in kr) for w in STORY_WORDS}
    print("[WORDS] " + " · ".join(f"{w} {n}" for w, n in sorted(cnt.items(), key=lambda x: -x[1])[:10] if n))
    return 0


# ---------------------------------------------------------------- 숫자 · 근거
def flat(x, p=""):
    if isinstance(x, dict):
        for k, v in x.items():
            yield from flat(v, f"{p}.{k}" if p else str(k))
    elif isinstance(x, list):
        if all(not isinstance(v, (dict, list)) for v in x):
            yield p, ", ".join(map(str, x))
        else:
            for i, v in enumerate(x):
                yield from flat(v, f"{p}[{i}]")
    else:
        yield p, x


def cmd_nums(a):
    d = json.loads(RESULTS.read_text("utf-8"))
    print(f"[NUMS] results.json {d.get('version')} made={d.get('made')} · {d.get('assumptions', '')[:70]}")
    if not a.keys:
        for k, v in d.items():
            if isinstance(v, (dict, list)):
                print(f"  {k} ({sum(1 for _ in flat(v))}개)")
        print("  → python3 tools/story_kit.py nums <키 일부> (예: nums lev3 dca)")
        return 0
    out = [(k, v) for k, v in flat(d) if any(q.lower() in k.lower() for q in a.keys)]
    for k, v in out[:80]:
        print(f"  {k} = {str(v)[:110]}")
    if len(out) > 80:
        print(f"  … {len(out) - 80}줄 더 (키를 좁혀서)")
    if not out:
        print("  (맞는 키 없음 — 새 계산은 stock/story/calc/series_calc.py 에 함수 하나 더하고 다시 실행)")
    return 0


def cmd_facts(a):
    lines = [l for l in FACTS.read_text("utf-8").splitlines() if l.startswith("- [")]
    hit = [l for l in lines if all(w.lower() in l.lower() for w in a.words)]
    if a.unused:                                              # v1.2 아직 어느 화에서도 안 쓴 근거만
        hit = [l for l in hit if "쓴 화" not in l]
    print(f"[FACTS] facts.md {len(lines)}줄 중 {len(hit)}줄 — {' '.join(a.words) or '(전부)'}")
    for l in hit:
        print("  " + (l if a.url else re.sub(r"\s*https?://\S+", "", l)))
    if not hit:
        print("  (없음 — 웹에서 찾으면 facts.md 에 같은 꼴로 한 줄 더한다)")
    return 0


# ---------------------------------------------------------------- B 요약본 틀
SUMMARY_TMPL = """# {ep}화 요약본 — {vid}
<!-- story_kit new {ver} {date} · 지난 화에서 정한 것: {prev} · 텍스트로 핵심만 — 사용자가 고친 뒤 C 단계(제작안) -->

전달 내용: {message}

## 롱폼 제목
1.
2.
3.

## 도입
- (첫 멘트 — 제목 맨 앞 낱말 + 결과 숫자 하나)
- (그 나이대가 실제로 하는 걱정 — 회사·아이·노후·가족에게 말 못 함)
- (그래서 무엇을 하기로 했는지)

## 문제 상황 → 해결 방법
1. (해결 방법 한 줄)
- 문제: (많은 개미가 … → 저도)
- 좋은 안:
- 근거:
  -
2.
- 문제:
- 좋은 안:
- 근거:
  -
3.
- 문제:
- 좋은 안:
- 근거:
  -

## 쇼츠 제목
1.
2.
3.

## 쇼츠 대본
- 첫 문장:
-
- 질문: … → 아래 영상에서.
"""


def prev_rule(ep):
    card = (STORY / "card.md").read_text("utf-8")
    m = re.search(rf"^- {ep - 1}화: (.*)$", card, re.M)
    return m.group(1)[:120] if m else "(없음)"


def cmd_new(a):
    d = src(a.vid)
    p = d / "요약본.md"
    if p.exists() and not a.force:
        fail("NEW", f"이미 있음: {p.relative_to(ROOT)}", "고치려면 그 파일을 Edit · 새로 만들려면 --force")
    d.mkdir(parents=True, exist_ok=True)
    m = dict(id=a.vid, ep=a.ep, message=a.message, made=time.strftime("%Y-%m-%d"), kit=VERSION)
    (d / "story.json").write_text(json.dumps(m, ensure_ascii=False, indent=1) + "\n", "utf-8")
    p.write_text(SUMMARY_TMPL.format(ep=a.ep, vid=a.vid, ver=VERSION, date=m["made"], prev=prev_rule(a.ep), message=a.message), "utf-8")
    log("NEW", file=p.relative_to(ROOT), meta=(d / "story.json").relative_to(ROOT))
    print(f"[NEW] {p.relative_to(ROOT)} · 지난 화에서 정한 것: {prev_rule(a.ep)[:60]}")
    return 0


# ---------------------------------------------------------------- C 제작안 검사·내보내기
def plan_path(vid):
    p = src(vid) / f"{vid}_제작안.txt"
    if not p.exists():
        fail("PLAN", f"제작안 없음: {p.relative_to(ROOT)}", "quick_story.md C-1 꼴로 한 번에 쓴다")
    return p


def section(text, head):
    """'■ <head>' 절의 줄들 (다음 '■ ' 전까지)."""
    m = re.search(rf"^■ {re.escape(head)}[^\n]*\n(.*?)(?=^■ |\Z)", text, re.S | re.M)
    return [l.rstrip() for l in m.group(1).splitlines()] if m else []


def shorts_lines(text):
    return [l.strip() for l in section(text, "쇼츠 대본") if l.strip() and not l.strip().startswith(("(", "#"))]


def numbered(lines):
    return [re.sub(r"^\s*(R?\d+)\.\s*", "", l).split("  (")[0].strip() for l in lines if re.match(r"^\s*R?\d+\.\s*\S", l)]


def est(sents):
    return sum(srt_tool.syllables(s) for s in sents) / SYL + GAP * max(0, len(sents) - 1)


def run_plan(plan, extra):
    import plan_tool
    buf = io.StringIO()
    with redirect_stdout(buf):
        code = plan_tool.main([str(plan)] + extra)
    return code, buf.getvalue().splitlines()


def title_check(title, shorts=False):
    r = subprocess.run([sys.executable, str(ROOT / "tools" / "title_fit.py")] + (["--shorts"] if shorts else []) + [title],
                       capture_output=True, text=True)
    out = [l for l in (r.stdout + r.stderr).splitlines() if l.startswith("[TITLE]") or "❌" in l]
    return r.returncode, out


NUM_RX = re.compile(r"\d[\d,.]*\s*(?:억(?:\s*\d+\s*천)?(?:만)?\s*원?|천만\s*원|만\s*원|%|퍼센트|배|조|명|번|개월|년)")


def ep_sentences(vid):
    """→ (화, 도입 문장들, 모든 문장들 — 대본 + 쇼츠). 제작안이 없으면 None."""
    pp = src(vid) / f"{vid}_제작안.txt"
    if not pp.exists():
        return None
    import plan_tool
    text = pp.read_text("utf-8")
    scenes, _ = plan_tool.parse(text.split("\n"))
    intro = [x for sc in scenes if sc["part"] == "도입" for x in sc["sentences"]]
    every = [x for sc in scenes for x in sc["sentences"]] + shorts_lines(text)
    return meta(vid).get("ep"), intro, every


def nums_in(sentences):
    out = {}
    for x in sentences:
        for m in NUM_RX.finditer(x):
            t = re.sub(r"\s+", "", m.group(0))
            if re.fullmatch(r"(19|20)\d\d년", t) or len(t) < 3:          # 연도·'8번' 같은 짧은 것은 뺌
                continue
            out.setdefault(t, x)
    return out


def norm(x):
    return re.sub(r"[\s,.?!·'\"‘’“”…]", "", x)


def dup_check(vid):
    """v1.2 앞 화와 겹침 (사용자 지시 2026-10-23 "70% 잃었다는건 처음 시리즈에서만 말하고 다른데서는 다른 경험으로 … 이전 시리즈에서
    썼던 내용들은 똑같이 사용하면 안돼"): 앞 화 도입(그 화의 핵심 경험)의 숫자를 다시 쓰면 문제 · 거의 같은 문장(0.85 이상)이면 문제 ·
    그 밖의 같은 숫자는 경고(사람이 본다)."""
    import difflib
    me = ep_sentences(vid)
    if not me or not isinstance(me[0], int):
        return [], []
    ep, _, mine = me
    probs, warns = [], []
    my_nums = nums_in(mine)
    for p_ in sorted(SOURCE.glob("*/story.json")):
        other = json.loads(p_.read_text("utf-8"))
        if not isinstance(other.get("ep"), int) or other["ep"] >= ep or other["id"] == vid:
            continue
        got = ep_sentences(other["id"])
        if not got:
            continue
        oep, ointro, oall = got
        core, rest = nums_in(ointro), nums_in(oall)
        for t, x in my_nums.items():
            if t in core:
                probs.append(f"{oep}화 핵심 경험(도입)의 숫자 '{t}' 를 다시 씀 — 이 화의 경험으로 바꾼다: {x[:50]}")
            elif t in rest:
                warns.append(f"{oep}화에 나온 숫자 '{t}' — 같은 사례·근거면 바꾼다: {x[:50]}")
        on = [norm(y) for y in oall if len(norm(y)) >= 12]
        for x in mine:
            nx = norm(x)
            if len(nx) < 12:
                continue
            best = max((difflib.SequenceMatcher(None, nx, y).ratio() for y in on), default=0)
            if best >= 0.85:
                probs.append(f"{oep}화와 거의 같은 문장 ({best:.2f}): {x[:50]}")
    return probs, warns


def cmd_check(a):
    plan = plan_path(a.vid)
    code, out = run_plan(plan, ["--write"])
    parts = []
    for l in out:
        if l.startswith("[PART]"):
            m = re.match(r"\[PART\] (\S+): .*? (\d+:\d\d~\d+:\d\d)", l)
            if m:
                parts.append(f"{m.group(1)} {m.group(2)}")
        elif not l.startswith("[WRITE]"):
            print(l)
    print("[PARTS] " + " · ".join(parts))
    text = plan.read_text("utf-8")
    bad = code
    titles = numbered(section(text, "제목"))
    if titles:
        c, o = title_check(titles[0])
        bad |= c
        print("\n".join(o))
    st = numbered(section(text, "쇼츠 제목"))
    if st:
        c, o = title_check(st[0], shorts=True)
        bad |= c
        print("\n".join(o))
    sl = shorts_lines(text)
    if sl:
        t = est(sl)
        flag = "✅" if 48 <= t <= 58 else "⚠️"
        print(f"[SHORTS] {flag} 문장 {len(sl)} · 추정 {t:.0f}초 (목표 50~55초) · 첫 문장 {len(sl[0])}자")
    dp, dw = dup_check(a.vid)
    for x in dp:
        print(f"❌ {x}")
    for x in dw:
        print(f"⚠️ {x}")
    print(f"[DUP] 앞 화와 겹침 problems={len(dp)} warnings={len(dw)}")
    bad |= 1 if dp else 0
    log("CHECK", plan=plan.name, problems=bad)
    return 1 if bad else 0


def thumb_prompt(n, ep, lines, pose, big, bg, vertical=False, close=False):
    raw = CHATGPT.read_text("utf-8")
    style = re.search(r"^STYLE: .*$", raw, re.M).group(0)
    style = style.replace(" No text, letters, numbers, logos or watermarks anywhere.", "")
    char = re.search(r"^CHARACTER .*$", raw, re.M).group(0)
    bad = [w for l in lines for w in bad_words(l)]
    if bad:                                                  # v1.8 한국어 없음 · 영어는 투자자라면 다 아는 말(screen_words.txt)만
        fail("THUMB", f"썸네일 문구에 허용 목록 밖 글자: {bad}", f"숫자·기호 + {SCREEN_WORDS.relative_to(ROOT)} 낱말만 (사용자 지시 2026-10-24)")
    cols = ["muted-red #E0302A" if re.search(r"[−-]\s?\d", l) else "bright yellow #FFD400" for l in lines]   # 손해 숫자 빨강 · 그 밖 노랑
    text = " ".join(f'line {i + 1} "{l}" in {c}' for i, (l, c) in enumerate(zip(lines, cols)))
    size = "vertical 9:16 (1080×1920), the picture fills the whole frame to every edge — no empty bands" if vertical else "landscape 16:9 (1280×720)"
    frame = ("a close-up of his head and shoulders filling about 70% of the height" if close
             else "his whole upper body large, about 60% of the picture height")
    place = "in the middle, the text above him in the upper third" if vertical else "on the left half, facing slightly right"
    num = f' One big number "{big}" in red with a cream paper outline in the upper right, about 22% of the height.' if big and not close and big not in " ".join(lines) else ""
    return "\n".join([
        f"# 썸네일 {n} — {'쇼츠' if vertical else '롱폼'} ({'본안' if n == 1 and not vertical else '실험안' if not vertical else '쇼츠'})",
        f"자세 {pose} · 배경 {bg} · 문구 {' / '.join(lines)}{' · 큰 숫자 ' + big if big and not close else ''} · 만든 도구 story_kit {VERSION}",
        "", "## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)", "```",
        style, char,
        f"SCENE: a paper puppet theater stage; the backdrop is {BG_EN[bg]}. Gu Bonseok puppet {POSE_EN[pose]}, {place}, {frame}.",
        f"TEXT: exactly these characters and nothing more — numbers, symbols and well-known stock-market words only (no Korean, no other words), very large bold rounded letters with a thick dark navy outline, "
        f"{('one line' if len(lines) == 1 else 'two lines') + (' in the upper part' if vertical else ' across the bottom, 60–90% of the width')}: {text}. Nothing else written except the tag.{num}",
        f'TAG: a small rounded navy tag "#{ep}" with yellow characters in the top-left corner.',
        f"FORMAT: {size}. Save as JPEG (.jpg) under 700 KB.",
        "```", ""])


def cmd_export(a):
    d, plan = src(a.vid), plan_path(a.vid)
    m = meta(a.vid)
    ep = m.get("ep", "?")
    text = plan.read_text("utf-8")
    script = d / f"{a.vid}.txt"
    code, out = run_plan(plan, [])                            # 검사 먼저 — 문제가 있으면 아무것도 쓰지 않음
    print("\n".join(l for l in out if l.startswith(("[PLAN]", "❌", "[CHECK]"))))
    if code:
        fail("EXPORT", "story_check 문제가 남음", f"python3 tools/story_kit.py check {a.vid}")
    run_plan(plan, ["--script-out", str(script)])
    sl = shorts_lines(text)
    if sl:
        (d / "shorts").mkdir(exist_ok=True)
        (d / "shorts" / f"{a.vid}-shorts.txt").write_text("-쇼츠\n" + "\n".join(sl) + "\n", "utf-8")
        print(f"[SHORTS] shorts/{a.vid}-shorts.txt 문장 {len(sl)}")
    lines = [x.strip() for x in a.thumb.split("/")][:2]
    alt = {"PHONE": "DESPAIR", "DESPAIR": "PHONE"}.get(a.pose, "DESPAIR")
    (d / "thumbnails").mkdir(exist_ok=True)
    for n, (pose, close) in enumerate([(a.pose, False), (alt, False), (a.pose, True)], 1):
        (d / "thumbnails" / f"thumbnail_{n}.md").write_text(thumb_prompt(n, ep, lines, pose, a.big, a.bg, close=close), "utf-8")
    if sl:
        (d / "shorts" / "thumbnails").mkdir(exist_ok=True)
        (d / "shorts" / "thumbnails" / "thumbnail_1.md").write_text(thumb_prompt(1, ep, lines, a.pose, a.big, a.bg, vertical=True), "utf-8")
    print(f"[THUMB] thumbnails/thumbnail_1~3.md (본안 {a.pose} · 실험 {alt} · 실험 얼굴 크게){' · shorts/thumbnails/thumbnail_1.md' if sl else ''}")
    for shorts in ([False, True] if sl else [False]):
        sp = scenes_path(a.vid, shorts)
        if not sp.exists():
            sp.write_text(draft(a.vid, shorts), "utf-8")
            print(f"[SCENES] 초안 {sp.relative_to(ROOT)} — 고칠 줄만 Edit")
    log("EXPORT", vid=a.vid, script=script.relative_to(ROOT))
    return 0


# ---------------------------------------------------------------- D 장면 표 → index.html
def scenes_path(vid, shorts):
    return src(vid) / ("shorts/scenes.txt" if shorts else "scenes.txt")


def script_path(vid, shorts):
    return src(vid) / (f"shorts/{vid}-shorts.txt" if shorts else f"{vid}.txt")


def parts_of(path):
    """→ [(파트 이름, 문장 번호)] — srt_tool.parse_txt 와 같은 번호."""
    out, part, in_card, n = [], "", False, 0
    for raw in path.read_text("utf-8-sig").splitlines():
        line = raw.strip()
        if not line:
            continue
        if srt_tool.is_label(line):
            part, in_card = line.lstrip("-").strip(), False
            continue
        if line.startswith("[장면]"):
            in_card = True
            continue
        if not in_card:
            n += 1
            out.append((part, n, line))
    return out


def first_match(rules, text, default):
    for k, rx in rules:
        if re.search(rx, text):
            return k
    return default


AMOUNT_RX = [
    ("won", re.compile(r"(\d+(?:\.\d+)?)\s*억(?:\s*(\d+)\s*천)?(?:\s*(\d+)\s*백)?\s*만?\s*원")),
    ("won", re.compile(r"(\d+)\s*천(?:\s*(\d+)\s*백)?\s*만\s*원")),
    ("won", re.compile(r"(\d[\d,]*)\s*만\s*원")),
    ("pct", re.compile(r"(\d+(?:\.\d+)?)\s*(?:%|퍼센트)")),
    ("x", re.compile(r"(\d+(?:\.\d+)?)\s*배")),
]


def amount(s):
    """문장 속 맨 앞 금액·%·배 → 화면 글자 (숫자·기호만). 예: '2억 5천만 원' → ₩250,000,000 · '34%'(떨어짐) → −34%."""
    best = None
    for i, (kind, rx) in enumerate(AMOUNT_RX):
        m = rx.search(s)
        if m and (best is None or m.start() < best[0].start()):
            best = (m, kind, i)
    if not best:
        return None
    m, kind, i = best
    g = [x for x in m.groups()]
    if kind == "won":
        if i == 0:
            v = float(g[0]) * 1e8 + int(g[1] or 0) * 1e7 + int(g[2] or 0) * 1e6
        elif i == 1:
            v = int(g[0]) * 1e7 + int(g[1] or 0) * 1e6
        else:
            v = int(g[0].replace(",", "")) * 1e4
        return f"₩{int(v):,}"
    if kind == "pct":
        sign = "−" if NEG.search(s) else "+" if POS.search(s) else ""
        return f"{sign}{g[0]}%"
    return f"×{g[0]}"


PART_POSE = {"도입": "BONSEOK", "마무리": "RESOLVE"}
PART_BG = {"도입": "HOME-NIGHT", "쇼츠": "HOME-NIGHT", "마무리": "STREET-DAWN"}
METHOD_BG = ["OFFICE", "HOME-NIGHT", "STREET-DAWN", "OFFICE", "HOME-NIGHT"]


def part_default(part, table, method_list, k):
    for key, v in table.items():
        if part.startswith(key):
            return v
    return method_list[k % len(method_list)] if isinstance(method_list, list) else method_list


def draft(vid, shorts):
    """대본 → 장면 표 초안 (표정·배경·큰 숫자는 낱말 규칙 — 사람이 고친다).
    장면 = 같은 파트 안에서 표정이 같은 문장 3개까지 · 숫자는 장면마다 하나 · 표정 낱말이 없는 문장은 앞 표정을 이어 감."""
    sp = script_path(vid, shorts)
    if not sp.exists():
        fail("DRAFT", f"대본 없음: {sp.relative_to(ROOT)}", f"python3 tools/story_kit.py export {vid} …")
    rows = parts_of(sp)
    out = [f"# 장면 표 — {vid}{'-shorts' if shorts else ''} · story_kit {VERSION} 초안 {time.strftime('%Y-%m-%d')} · 한 줄 = 장면 하나",
           "# 문장 | 배경 | 인형(+*소품) | 화면    (문법: stock/guides/quick_story.md D-2 · 고친 뒤 python3 tools/story_kit.py scenes " + vid + (" --shorts)" if shorts else ")"),
           ""]
    groups, cur, methods = [], None, []
    for part, n, line in rows:
        if part.startswith("방법") and part not in methods:
            methods.append(part)
        new_part = cur is None or cur["part"] != part
        hit = first_match(POSE_RULES, line, None)
        if hit in ("DESPAIR", "PHONE") and not (part.startswith(("도입", "쇼츠")) or FIRST.search(line)):
            hit = None                                        # 시장 이야기('코스피가 떨어져')는 주인공 표정을 바꾸지 않음
        if hit in ("DESPAIR", "PHONE") and part.startswith("마무리"):
            hit = "RESOLVE"
        pose = hit or (PART_POSE.get(part[:3], None) if new_part else cur["pose"]) or ("STUDY" if part.startswith("방법") else "BONSEOK")
        big = amount(line)
        if new_part or pose != cur["pose"] or len(cur["n"]) >= 3 or (big and cur["big"]):
            cur = dict(part=part, pose=pose, n=[], text=[], big=None, mi=len(methods) - 1)
            groups.append(cur)
        cur["n"].append(n)
        cur["text"].append(line)
        cur["big"] = cur["big"] or (big, line) if big else cur["big"]
    for g in groups:
        txt = " ".join(g["text"])
        bg = part_default(g["part"], PART_BG, METHOD_BG, max(0, g["mi"]))
        if re.search(BG_RULES[0][1], txt) and g["big"]:
            bg = "BOARD"
        scr = ""
        if g["big"]:
            val, line = g["big"]
            col = "R" if NEG.search(line) else "G" if POS.search(line) else "Y"
            scr = f"BIG {val} {col}"
        pose = g["pose"]
        side = "@L" if scr and not shorts else ""                # 롱폼은 화면이 오른쪽 → 인형 왼쪽 · 쇼츠는 화면이 위
        pup = f"{pose}{side}" if pose != "CROWD" else (f"CROWD{side}" if scr else "PHONE@L+CROWD@R")
        rng = f"{g['n'][0]}" if len(g["n"]) == 1 else f"{g['n'][0]}-{g['n'][-1]}"
        out.append(f"{rng} | {bg} | {pup}" + (f" | {scr}" if scr else ""))
    return "\n".join(out) + "\n"


SCREEN_RX = re.compile(r"^(K[1-5]|BIG|PIE|LIST)\b\s*(.*)$")


def icon_items(tok):
    """'!kr>+us' → [{k:kr,m:!},{arrow},{k:us,m:+}] — '>' = 화살표 칸, '!' 빨간 × · '+' 청록 ✓ (v1.4)."""
    out = []
    for j, part in enumerate(tok.split(">")):
        if j:
            out.append(dict(arrow=True))
        if not part:                                             # v1.8 띄어 쓴 '>' 하나 = 화살표만
            continue
        mk = part[0] if part[:1] in ("!", "+") else ""
        k = part.lstrip("!+")
        if k.startswith("'"):                                    # v1.8 글자 칩 'S&P_500 (밑줄 = 띄어쓰기) — 허용 목록 낱말만
            out.append(dict(t=k[1:].replace("_", " "), m=mk))
            continue
        if k not in ICONS:
            raise ValueError(f"아이콘 없음: {k} (있는 것: {', '.join(ICONS)})")
        out.append(dict(k=k, m=mk))
    return out


def parse_screen(s):
    m = SCREEN_RX.match(s.strip())
    if not m:
        raise ValueError(f"화면 꼴 아님: {s!r} (K1~K5·BIG·PIE — v1.6 K6 정리 카드 없음)")
    typ, rest = m.group(1), m.group(2).strip()
    at_m = re.search(r"\s*@(\d+)(?::(\S+))?\s*$", rest)
    when = None
    if at_m:
        when = [int(at_m.group(1)), at_m.group(2)]
        rest = rest[:at_m.start()].strip()
    o = dict(type=typ)
    tm = re.search(r"(?:^|\s)title=(\S+)", rest)                  # v1.8 화면 위 이름표 (밑줄 = 띄어쓰기)
    if tm:
        o["title"] = tm.group(1).replace("_", " ")
        rest = (rest[:tm.start()] + " " + rest[tm.end():]).strip()
    if typ == "K1":
        f, t = rest.split(">")
        o.update({"from": f.strip(), "to": t.strip()})
    elif typ == "K2":
        ys = [y.strip() for y in rest.split(",") if y.strip()]
        o.update(years=[y.lstrip("*") for y in ys], hl=[y.lstrip("*") for y in ys if y.startswith("*")])
    elif typ == "K3":
        kv = dict(re.findall(r"(\w+)=(\S+)", rest))
        vals = re.sub(r"\s*\w+=\S+", "", rest).strip()
        o.update(values=[float(v) for v in vals.split(",")], base=float(kv["base"]) if "base" in kv else None,
                 labels=kv["lab"].split(",") if "lab" in kv else [], end=kv.get("end"))
    elif typ == "K4":
        items = []
        for tok in rest.split():
            if tok.startswith("icon="):                          # v1.4 단위를 그림으로 (예: icon=hourglass = 기간)
                o["icon"] = icon_items(tok[5:])[0]["k"]
                continue
            p = tok.split(":")
            items.append(dict(lab=p[0], val=p[1], c=p[2] if len(p) > 2 else None))
        o.update(items=items)
    elif typ == "K5":
        icons = []
        for tok in rest.split():
            icons += icon_items(tok)                             # v1.4 'kr>us' = 국기 → 국기
        o.update(icons=icons)
    elif typ == "PIE":                                           # v1.4 원그래프: PIE <몫 %> [색] [label=50%+] [icon=people]
        kv = dict(re.findall(r"(\w+)=(\S+)", rest))
        bare = re.sub(r"\s*\w+=\S+", "", rest).split()
        o.update(value=float(bare[0]), c=bare[1] if len(bare) > 1 else "R", label=kv.get("label"))
        if "cap" in kv:                                          # v1.8 원그래프 아래 짧은 글 (밑줄 = 띄어쓰기)
            o["cap"] = kv["cap"].replace("_", " ")
        if "icon" in kv:
            o["icon"] = icon_items(kv["icon"])[0]["k"]
    elif typ == "LIST":                                          # v1.8 'n:+글자; n:!글자' — 줄마다 ✓/✗, 문장 n 에 나타남
        items = []
        for part in [x.strip() for x in rest.split(";") if x.strip()]:
            im = re.match(r"^(?:(\d+)(?::(\S+?))?:)?([!+])?(.+)$", part)
            it = dict(t=im.group(4).strip(), m=im.group(3) or "+")
            if im.group(1):
                it["at"] = [int(im.group(1)), im.group(2)]
            items.append(it)
        if not items:
            raise ValueError("LIST = 'n:+글자; n:!글자' (줄 하나 이상)")
        o.update(items=items)
    elif typ == "BIG":
        p = rest.split()
        for tok in [x for x in p if x.startswith("icon=")]:     # v1.5 무엇의 숫자인지 그림 (예: icon=kr — 'KOSPI' 글자 대신)
            o["icon"] = icon_items(tok[5:])[0]["k"]
            p.remove(tok)
        c = p.pop() if len(p) > 1 and p[-1] in ("R", "G", "Y", "W") else "W"
        o.update(text=" ".join(p), c=c)                          # v1.4 여러 낱말 (예: BIG 3× −76.7% R)
    if when:
        o["at"] = when
    return o


def screen_words():
    """화면에 써도 되는 영어 (대문자 set) — stock/story/screen_words.txt."""
    if not SCREEN_WORDS.exists():
        return set()
    return {l.strip().upper() for l in SCREEN_WORDS.read_text("utf-8").splitlines() if l.strip() and not l.startswith("#")}


def bad_words(text, allow=None):
    """글자 속 한국어(→ '한국어') 또는 허용 목록 밖 영어 낱말 목록 (render.mjs v1.25 와 같은 판정 — '%p' 는 뺌)."""
    if re.search(r"[가-힣ぁ-んァ-ン一-龥]", text or ""):
        return ["한국어"]
    allow = screen_words() if allow is None else allow
    return [w for w in re.findall(r"[A-Za-z][A-Za-z&-]*", (text or "").replace("%p", "%")) if w.upper() not in allow]


def screen_texts(o):
    """화면 하나의 글자들 (낱말 검사용)."""
    out = [o.get("title", ""), o.get("text", ""), o.get("label") or "", o.get("cap", ""), o.get("end") or ""]
    out += [x.get("t", "") for x in o.get("icons", [])] + [x["t"] for x in o.get("items", []) if "t" in x]
    out += [x.get("lab", "") + " " + x.get("val", "") for x in o.get("items", []) if "lab" in x]
    out += o.get("labels", []) + o.get("years", [])
    return [t for t in out if t]


def props_catalog():
    """→ 소품 이름 목록 (stock/story/puppet/props_chatgpt.md 표의 저장 경로 순서). 파일이 없으면 빈 목록."""
    if not PROPS_FILE.exists():
        return []
    seen = []
    for name in PROP_RX.findall(PROPS_FILE.read_text("utf-8")):
        if name not in seen:
            seen.append(name)
    return seen


PROP_ROW = re.compile(r"^\| (\d+) \| `stock/story/puppet/props/([A-Z0-9-]+)\.png` \| ([^|]*)\| ([^|]*)\| ([^|]*)\|")
PROP_CAND = re.compile(r"^- 후보 ([A-Z0-9-]+) — (.*)$")


def cmd_props(a):
    """공통 설명 소품 목록 — 이름 · 뜻 · 쓴 화 · 그림 있음(✅)/만들 것(⬜)/후보(…). 낱말을 주면 뜻·이야기 예에 든 것만."""
    if not PROPS_FILE.exists():
        fail("PROPS", f"목록 없음: {PROPS_FILE.relative_to(ROOT)}")
    rows, cand = [], []
    for line in PROPS_FILE.read_text("utf-8").splitlines():
        m = PROP_ROW.match(line)
        if m:
            rows.append((m.group(2), m.group(3).strip(), m.group(4).strip(), m.group(5).strip()))
            continue
        c = PROP_CAND.match(line)
        if c:
            cand.append((c.group(1), c.group(2).strip()))
    words = [w for w in a.words if w]
    hit = lambda *txt: not words or any(w in " ".join(txt) for w in words)
    n = 0
    for name, mean, ex, ep in rows:
        if hit(name, mean, ex):
            have = (STORY / "puppet" / "props" / f"{name}.png").exists()
            print(f"{'✅' if have else '⬜'} *{name:<12} {mean} — 예: {ex} · {ep}")
            n += 1
    for name, mean in cand:
        if hit(name, mean):
            print(f"… {name:<13} (후보 — 쓰려면 props_chatgpt.md 표로 옮겨 프롬프트를 씀) {mean}")
            n += 1
    if not n:
        print(f"맞는 소품 없음 — 새로 만들면 {PROPS_FILE.relative_to(ROOT)} 표 끝에 (일반적인 뜻으로, 화 전용이면 '전용')")
    log("PROPS", shown=n, total=len(rows), candidates=len(cand), words=" ".join(words))
    return 0


def parse_puppets(s, catalog=None):
    """인형 칸 → [{pose…} | {prop…}] — v1.6 '*이름' = 소품 (예: 13:몰빵:*ONE-BASKET@R>rise)."""
    out = []
    for tok in re.split(r"\s*[+;]\s*", s.strip()):
        if not tok:
            continue
        pm = re.match(r"^(?:(\d+)(?::(\S+?))?:)?\*([A-Z0-9]+(?:-[A-Z0-9]+)*)(?:@([LCR]))?(?:>(rise|pop))?$", tok)
        if pm:
            cat = props_catalog() if catalog is None else catalog
            if pm.group(3) not in cat:
                raise ValueError(f"소품 없음: {pm.group(3)} — {PROPS_FILE.relative_to(ROOT)} 표에 먼저 더함 (있는 것: {', '.join(cat) or '없음'})")
            p = dict(prop=pm.group(3), pos=pm.group(4), move=pm.group(5) or "pop")
            if pm.group(1):
                p["at"] = [int(pm.group(1)), pm.group(2)]
            out.append(p)
            continue
        m = re.match(r"^(?:(\d+)(?::(\S+?))?:)?([A-Z]+)(?:@([LCR]))?(?:>(in|walk|rise|pop))?(!)?$", tok)
        if not m or m.group(3) not in POSES:
            raise ValueError(f"인형 꼴 아님: {tok!r} (POSE[@L|C|R][>in|walk|rise|pop][!] · 자세 {', '.join(POSES)} · 장면 안에서 바뀜 = '<문장>:POSE' · 소품 = '*이름[@L|C|R]')")
        p = dict(pose=m.group(3), pos=m.group(4) or "C", move=m.group(5) or "in", flip=bool(m.group(6)))
        if m.group(1):
            p["at"] = [int(m.group(1)), m.group(2)]
        out.append(p)
    return out


def compile_scenes(vid, shorts):
    sp, scp = scenes_path(vid, shorts), script_path(vid, shorts)
    rows = parts_of(scp)
    nmax = len(rows)
    catalog = props_catalog()
    allow = screen_words()
    scenes, errs, prev = [], [], None
    for i, raw in enumerate(sp.read_text("utf-8").splitlines(), 1):
        line = raw.split("#", 1)[0].strip() if not raw.lstrip().startswith("#") else ""
        if not line:
            continue
        c = [x.strip() for x in line.split("|")] + ["", "", ""]
        try:
            if c[0] == "정리":
                raise ValueError("'정리' 줄(정리 카드)은 쓰지 않음 — 정리 부분은 뺌 (v1.6, 사용자 지시 2026-10-23)")
            m = re.match(r"^(\d+)(?:-(\d+))?$", c[0])
            if not m:
                raise ValueError(f"문장 칸 꼴 아님: {c[0]!r} (n · n-m)")
            a_, b_ = int(m.group(1)), int(m.group(2) or m.group(1))
            if not (1 <= a_ <= b_ <= nmax):
                raise ValueError(f"문장 번호 범위 밖: {c[0]} (1~{nmax})")
            sc = dict(a=a_, b=b_)
            sc["bg"] = c[1] or (prev or {}).get("bg") or "PAPER"
            if sc["bg"] not in BGS:
                raise ValueError(f"배경 없음: {sc['bg']} ({', '.join(BGS)})")
            cast = parse_puppets(c[2], catalog) if c[2] else []
            sc["puppets"] = [p for p in cast if "pose" in p]
            props = [p for p in cast if "prop" in p]
            for p in props:                                    # v1.6 소품 자리: 롱폼 오른쪽(R) · 쇼츠 위 가운데(C)
                p["pos"] = p["pos"] or ("C" if shorts else "R")
            if props:
                sc["props"] = props
            if c[3]:
                sc["screen"] = parse_screen(c[3])
                bad = [w for t in screen_texts(sc["screen"]) for w in bad_words(t, allow)]
                if bad:
                    raise ValueError(f"화면 글자가 허용 목록 밖: {', '.join(sorted(set(bad)))} — 한국어는 쓰지 않고, 영어는 {SCREEN_WORDS.relative_to(ROOT)} 낱말만 (투자자라면 다 아는 말)")
                if props and sc["screen"]["type"] != "BIG":
                    raise ValueError(f"소품은 화면 없는 장면이나 BIG 과만 ({sc['screen']['type']} 칸과 겹침 — 장면을 나눔)")
                for p in sc["puppets"]:                       # 화면이 있으면 인형은 왼쪽 (롱폼) — 자리를 적었으면 그대로
                    if p["pos"] == "C" and not shorts and "@" not in c[2]:
                        p["pos"] = "L"
            if prev:                                           # 앞 장면과 같은 배경·자세·자리 → 들어오는 움직임 없이 이어짐
                same = {(p["pose"], p["pos"]) for p in prev.get("puppets", []) if "at" not in p}
                for p in sc["puppets"]:
                    if "at" not in p and (p["pose"], p["pos"]) in same and prev["bg"] == sc["bg"]:
                        p["cont"] = True
                same_p = {(p["prop"], p["pos"]) for p in prev.get("props", []) if "at" not in p}
                for p in sc.get("props", []):                 # 같은 소품이 같은 자리에 이어지면 튀어나오지 않음
                    if "at" not in p and (p["prop"], p["pos"]) in same_p and prev["bg"] == sc["bg"]:
                        p["cont"] = True
            scenes.append(sc)
            prev = sc
        except (ValueError, KeyError, IndexError) as e:
            errs.append(f"{sp.name}:{i}: {e}")
    if shorts and any(p.get("pos") != "C" for s in scenes for p in s.get("props", [])):
        errs.append("쇼츠 소품은 위 가운데(@C)만 — 인형이 아래 가운데")
    covered = sorted({n for s in scenes if "a" in s for n in range(s["a"], s["b"] + 1)})
    missing = [n for n in range(1, nmax + 1) if n not in covered]
    if scenes and scenes[0].get("a") != 1:
        errs.append("첫 장면이 문장 1 부터가 아님")
    order = [s["a"] for s in scenes if "a" in s]
    if order != sorted(order):
        errs.append("장면 순서가 문장 순서와 다름")
    return scenes, errs, missing, nmax, rows


PAGE = """<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
{metas}<title>{vid}</title>
<!-- 자동 생성 — tools/story_kit.py scenes {ver} ({made}) · 원본 장면 표 stock/source/{rel} · 무대 video/render/story.js.
     손으로 고치지 않는다 (장면 표를 고치고 다시 생성 — 데이터 칸 EP-DATA 는 그대로 둠). 연구·교육용 영상 — 투자 권유 아님. -->
<link rel="stylesheet" href="../../render/kit.css">
<link rel="stylesheet" href="../../render/story.css">
{vcss}</head>
<body>
<div id="wrap"><div id="stage"></div></div>
<div id="ctrl"></div>
<div id="now"></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.min.js"></script>
<script id="ep-data">{epdata}</script>
<script src="../../render/kit.js"></script>
<script src="../../render/puppet.js"></script>
<script src="../../render/story.js"></script>
<script>
Story.build({spec});
</script>
</body>
</html>
"""
VCSS = """<style>
#wrap{max-width:420px;margin:0 auto;aspect-ratio:9/16}
body.render #wrap{width:1080px;height:1920px;max-width:none;margin:0}
#stage{width:1080px;height:1920px;background:#000}
</style>
"""


def cmd_scenes(a):
    sp = scenes_path(a.vid, a.shorts)
    if a.draft or not sp.exists():
        if sp.exists() and not a.force:
            fail("SCENES", f"이미 있음: {sp.relative_to(ROOT)}", "고칠 줄만 Edit · 초안을 다시 만들려면 --draft --force")
        sp.parent.mkdir(parents=True, exist_ok=True)
        sp.write_text(draft(a.vid, a.shorts), "utf-8")
        print(f"[DRAFT] {sp.relative_to(ROOT)}")
        if a.draft:
            return 0
    scenes, errs, missing, nmax, rows = compile_scenes(a.vid, a.shorts)
    for e in errs:
        print(f"❌ {e}")
    if missing:
        print(f"⚠️ 장면 표에 없는 문장 {len(missing)}개: {missing[:12]}{' …' if len(missing) > 12 else ''} (앞 장면이 이어짐)")
    if errs:
        log("SCENES", logging.ERROR, problems=len(errs))
        return 1
    m = meta(a.vid)
    ep = m.get("ep")
    parts = []
    for part, _, _ in rows:
        if part not in parts:
            parts.append(part)
    test_from = next((p for p in parts if p.startswith("방법")), None)
    page_id = a.vid + ("-shorts" if a.shorts else "")
    plan = src(a.vid) / f"{a.vid}_제작안.txt"
    intro_ok = plan.exists() and any(l.strip().startswith("- 도입 통과:") for l in plan.read_text("utf-8").splitlines())
    used = []
    for s in scenes:
        for p in s.get("props", []):
            if p["prop"] not in used:
                used.append(p["prop"])
    spec = dict(dir="../../../stock/story/puppet/", ep=ep, introOk=intro_ok, next=(ep + 1) if isinstance(ep, int) and not a.shorts else None,
                vertical=a.shorts, cover=a.shorts, testFrom=None if a.shorts else test_from,
                props={k: f"props/{k}.png" for k in used}, allowWords=sorted(screen_words()), scenes=scenes)
    out = ROOT / "video" / "episodes" / page_id / "index.html"
    epdata = "/*EP-DATA:BEGIN*//*EP-DATA:END*/"
    if out.exists():
        mm = re.search(r"/\*EP-DATA:BEGIN\*/[\s\S]*?/\*EP-DATA:END\*/", out.read_text("utf-8"))
        if mm:
            epdata = mm.group(0)
    metas = ('<meta name="video-size" content="1080x1920">\n<meta name="video-safe" content="150 60 1320 60">\n'
             '<meta name="end-hold" content="2.5">\n') if a.shorts else ""
    html = PAGE.format(metas=metas, vid=page_id, ver=VERSION, made=time.strftime("%Y-%m-%d %H:%M"),
                       rel=sp.relative_to(SOURCE).as_posix(), vcss=VCSS if a.shorts else "", epdata=epdata,
                       spec=json.dumps(spec, ensure_ascii=False, separators=(",", ":")))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, "utf-8")
    kinds = {}
    for s in scenes:
        k = (s.get("screen") or {}).get("type", "무대")
        kinds[k] = kinds.get(k, 0) + 1
    have = [k for k in used if (STORY / "puppet" / "props" / f"{k}.png").exists()]
    print(f"[SCENES] {out.relative_to(ROOT)} · 장면 {len(scenes)} (문장 {nmax}) · " + " ".join(f"{k} {v}" for k, v in kinds.items())
          + f" · 소품 {len(used)}종 (그림 있음 {len(have)}) · testFrom={spec['testFrom']} · {len(html) // 1024}KB")
    if len(have) < len(used):
        print(f"[PROPS] 그림 아직 없음 {len(used) - len(have)}개 (임시 그림으로 그림): {', '.join(k for k in used if k not in have)} "
              f"→ ChatGPT {PROPS_FILE.relative_to(ROOT)}")
    synced = "EP=" in epdata and '"estimated":true' not in epdata
    print(f"[NEXT] node video/render/render.mjs sync stock {page_id}{'' if synced else ' --estimate'} && node video/render/render.mjs check stock {page_id}")
    log("SCENES", page=out.relative_to(ROOT), scenes=len(scenes))
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description="개미 재기 일지 단계 도구")
    ap.add_argument("--log-level", default="WARNING", choices=["DEBUG", "INFO", "WARNING"])
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("topics"); p.add_argument("--n", type=int, default=15)
    p = sub.add_parser("nums"); p.add_argument("keys", nargs="*")
    p = sub.add_parser("facts"); p.add_argument("words", nargs="*"); p.add_argument("--url", action="store_true"); p.add_argument("--unused", action="store_true")
    p = sub.add_parser("new"); p.add_argument("ep", type=int); p.add_argument("vid"); p.add_argument("message"); p.add_argument("--force", action="store_true")
    p = sub.add_parser("check"); p.add_argument("vid")
    p = sub.add_parser("export"); p.add_argument("vid"); p.add_argument("--thumb", required=True, help='썸네일 문구 1~2줄 "줄1/줄2" — 숫자·기호만 (영어·한국어 없음)')
    p.add_argument("--pose", default="PHONE", choices=[x for x in POSES if x != "CROWD"]); p.add_argument("--big", default="")
    p.add_argument("--bg", default="HOME-NIGHT", choices=BGS)
    p = sub.add_parser("props"); p.add_argument("words", nargs="*")
    p = sub.add_parser("scenes"); p.add_argument("vid"); p.add_argument("--shorts", action="store_true")
    p.add_argument("--draft", action="store_true"); p.add_argument("--force", action="store_true")
    a = ap.parse_args(argv)
    logging.basicConfig(level=getattr(logging, a.log_level), format="%(message)s", stream=sys.stderr)
    return {"topics": cmd_topics, "nums": cmd_nums, "facts": cmd_facts, "new": cmd_new, "check": cmd_check,
            "export": cmd_export, "props": cmd_props, "scenes": cmd_scenes}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
