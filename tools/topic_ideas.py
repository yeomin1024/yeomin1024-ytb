#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.4 — 2026-10-29 — 평가를 다 한 묶음 갈기·좋음 주제 다시 짜기 (사용자 지시 2026-10-29 "주식 주제 평가판 평가했는데 다시 주제 탐색해봐"):
#          `revise <고침.json>` = 주제 칸을 고침 ({ID: {칸: 새 값, "why": 까닭}} — 평가는 그대로 · 옛 값은 revised 에 · 미리 계산은 지워 다시 계산하게 · lint 통과만) ·
#          `refresh` = 지금 묶음을 모두 평가(또는 작성·뺌)했으면 새 묶음 — 좋음(미리 계산 통과)은 새 묶음에 이어 가고, 나머지 안 쓴 주제는 대기로 · 20개를 못 채우면 아무것도 안 바꿈 ·
#          data_kind 검사 (settings [fields] DATA_KINDS 가 있으면 그 안의 값만 — 주식: 사건 사례·종목 사례를 더함, 지수 전략 백테스트와 나눠 배우게).
#          문서·평가판에 '다시 짬'(뜻이 바뀐 마지막 고침의 까닭 — 좋음을 받은 뒤 다시 짠 주제를 다시 평가할 수 있게).
#          고침: v1.3 에서 평가판 안내 글 기본값(NOTE_PAGE)을 '[분류]' 글로 바꿔 재테크 평가판을 다시 만들면 주식 글이 찍히던 것 → 기본값 되돌리고 주식 settings [page] NOTE_PAGE 로.
#          영향: lint()·pick_batch(carry)·cmd_revise()·cmd_refresh()·revised_why()·render()·render_page()·main().
# (v1.3 — 2026-10-29 — **정답 미리 확인** (사용자 지시 2026-10-29 "그렇게 절차정하고 주제 걸러봐 기존 3개도 확인해서"): `precheck <결과.json> [고친 결론.json]` —
#          주제마다 미리 계산 분류(정답형·차이없음·사실형·계산형·조건부형·미확인)·고친 결론·까닭을 topics.json 에 · settings [precheck] EXCLUDE(미확인)·NO_TEST(조건부형인데
#          테스트형) 는 묶음에서 뺌(나쁨처럼 '남은 것'에서 빠짐 · 새 묶음에 안 뽑힘) · 주제탐색.md 표·자세히·평가판에 분류 · use 할 때 미리 계산이 없거나 빠진 주제면 경고.
#          영향: pre_out()·batch_done()·pick_batch()·finish()·cmd_precheck()·cmd_use()·render()·render_page()·main().)
# (v1.2.2 — 2026-10-28 — 안내 문구를 주제마다 (settings [page] NOTE_DOC · NOTE_PAGE, 없으면 예전 주식 글 그대로) — 역사 주제탐색.md·평가판에
#          '투자 권유가 아님 · 계산(calc/)으로 확정'이 찍혀서. 영향: load_settings()·render()·render_page().)
# (v1.2.1 — 2026-10-28 — '자료에 기간(연도)' 검사를 주제마다 (settings [clarity] YEAR, 없으면 예전 그대로 (19|20)\d\d) — 역사 후보의 1653년·18세기·
#          기원전이 '연도 없음'으로 빠져서 (사용자 지시 2026-10-28 "주식 주제 관련 세션에서 했던것처럼 똑같은 방식으로 … 요약본까지" — history). 영향: lint() 한 줄.)
# (v1.2 — 2026-10-28 — 주제마다 이름·칸 설명 (재테크도 — 사용자 지시 2026-10-28 "주식 주제 관련 세션에서 했던것처럼 똑같은 방식으로 진행해서
#          유튜브 분석부터 요약본까지 만들어봐"): settings.toml [page] NAME · [fields] data·format·market·data_kind 설명 (없으면 주식 글 그대로) ·
#          겹침 대상에 <주제>/source/used_content.md 표(재테크 '이미 만든 대본') · 문서·평가판의 'stock/' 경로를 주제 경로로. 영향: load_settings()·used_entries()·
#          cmd_material()·render()·render_page()·MARKS_HEAD.)
# (v1.1) — 2026-10-28 — material.md 맨 위 '0. 채널 설명' = stock/guides/channel.md 의 '한눈에'(표시 줄 channel:start~end) 그대로 · format 칸 풀이에
#          채널 전달 방식 대응(테스트형 = 테스트·문제 · 실험형 = 비교 시뮬레이션) — 사용자 지시 2026-10-28 "유튜브 채널 설명이니깐 여기에 맞게 영상 만들어야해
#          이 내용 파일 생성해서 참고할수 있게해" · channel_lines() 는 summary_ideas.py 도 씀. 파일이 없으면 WARNING 한 줄 + 재료에 '못 읽음'.
#          · 겹침 검사 고침: 새 꼴 요약본(summary_ideas.py v1.0 — 커밋 622f9ca1)의 [방향] '항목 N: …' 줄과 [N안] 제목 줄을 다시 읽고 '#' 주석 줄은 뺌
#            (그 뒤로 portfolio·timing 편 항목·제목이 겹침 검사에서 빠져 있었음 — material.md 재생성 때 발견).
# (v1.0) — 2026-10-28 — 새로: 주식 주제 탐색 — 분석 결과·페르소나로 주제 20개씩, 좋음·나쁨 평가를 배워 순위에 반영 (사용자 지시 2026-10-28
#          "주제 탐색 파일 생성 — 분석 결과, 페르소나를 토대로 주제 20개씩 생성(이미 작성중, 작성한 주제와 똑같으면 안됨, 모두 작성 시 20개씩 갱신) ·
#          좋다고, 나쁘다고 표시 가능하도록 해서 그걸 학습 후 되도록 좋은 주제로 탐색하도록 · 그리고 애매한 결론이 아닌 명확하게 결론 낼수 있어야 함").
#          · 주제 글(질문·결론·판정 규칙·자료)은 Claude 가 재료(material)를 읽고 후보 모음(pool JSON)으로 쓴다 — 이 도구는 거르고·점수 매기고·뽑고·배운다.
#          · 거르기: ① 애매한 결론 (settings [clarity] VAGUE 말 · 숫자·판정 말 없음 · 판정 규칙에 기준 없음 · 자료에 기간 없음)
#                    ② 이미 쓴·쓰는 주제와 같음 (낱말 닮음 ≥ SIM_MAX — 올린 영상·옛 대본·stock/source/*/요약본 방향·항목 · 앞서 낸 주제)
#          · 점수 = 처음 점수(니즈 좋아요·주제 묶음 성공 비율·페르소나 몫·공급 틈) + 배운 점수(평가한 주제의 갈래별 log 비 + 닮은 좋음/나쁨 주제) — 내역을 문서에.
#          · 묶음: 20개 (같은 주제 묶음 ≤ 4 · 같은 니즈 ≤ 2 · 평가가 쌓이면 아직 평가 없는 갈래에서 3자리). 묶음의 모든 주제가 작성중·작성함·나쁨이면 '갱신 필요'.
#          · 평가 = stock/topics/평가.txt 한 줄 ('T003 좋음 까닭' · 'T007 나쁨') — 사용자가 GitHub 에서 줄을 더하거나, 채팅으로 말하면 Claude 가 mark.
#          결과: stock/topics/주제탐색.md (사람이 읽고 평가) · topics.json (모든 주제·상태). 할당량 0. ※ 연구·교육용 — 투자 권유가 아님.
"""주식 주제 탐색 — 20개씩 · 평가를 배움 · 명확한 결론만

  python3 tools/topic_ideas.py stock material            # 재료 한 장 → stock/topics/material.md (Claude 가 후보를 쓰기 전에 읽음)
  python3 tools/topic_ideas.py stock add <pool.json>     # 후보 모음 → 거르기·점수 → (갱신 때) 새 20개 묶음 → 주제탐색.md
  python3 tools/topic_ideas.py stock mark T003 좋음 "까닭"   # 평가 한 줄 (평가.txt 에 더함) — 나쁨도 같음
  python3 tools/topic_ideas.py stock use T003 <영상ID>    # 이 주제로 쓰기 시작 (작성중) — 요약본에 '주제 ID: T003' 를 적어도 저절로 잡힘
  python3 tools/topic_ideas.py stock done T003           # 다 씀 (작성함)
  python3 tools/topic_ideas.py stock status              # 평가·소스를 다시 읽고 점수·문서 갱신 → '갱신 필요'면 새 후보 모음을 씀
  python3 tools/topic_ideas.py stock import <marks.json> # 평가판 페이지(Artifact db 'marks')에서 누른 평가 → 평가.txt (Claude 가 ArtifactData list 결과를 저장해 넘김)
  python3 tools/topic_ideas.py stock precheck <결과.json> [고친 결론.json]   # v1.3 정답 미리 확인 (stock/topics/precheck/precheck.py 결과) → 분류·고친 결론 · 미확인·조건부 테스트형은 묶음에서 뺌
  python3 tools/topic_ideas.py stock revise <고침.json>   # v1.4 주제 칸 고치기 ({ID: {칸: 값, "why": 까닭}}) — 평가 유지 · 미리 계산은 다시
  python3 tools/topic_ideas.py stock refresh             # v1.4 묶음을 모두 평가했으면 새 20개 — 좋음은 이어 감
로그: [STAGE] [시각] key=value (START·LOAD·USED·CHECK·SCORE·LEARN·BATCH·WRITE·DONE)
"""
import argparse
import json
import logging
import math
import re
import sys
import time
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import personas as pz                  # noqa: E402  kw_tokens (낱말 — 페르소나와 같은 규칙)

try:
    import tomllib
except ModuleNotFoundError:            # Python 3.10
    import tomli as tomllib

VERSION = "v1.4"
ROOT = Path(__file__).resolve().parent.parent
LOG = logging.getLogger("topics")
FIELDS = ("title", "question", "conclusion", "decide", "data", "format", "persona", "theme", "needs", "market", "data_kind")
STATUS = ("이번 묶음", "대기", "작성중", "작성함")
GOOD = re.compile(r"^(좋음|좋아|좋다|good|👍|o|ㅇ|\+)$", re.I)
BAD = re.compile(r"^(나쁨|나빠|별로|bad|👎|x|ㄴ|-)$", re.I)
SYN = {"spy": "s&p500", "s&p": "s&p500", "voo": "s&p500", "s&p500": "s&p500", "에스앤피": "s&p500", "qqq": "나스닥", "나스닥100": "나스닥",
       "매달": "적립", "적립식": "적립", "매월": "적립", "dca": "적립", "tqqq": "레버리지", "qld": "레버리지", "sso": "레버리지",
       "qyld": "커버드콜", "jepq": "커버드콜", "jepi": "커버드콜", "schd": "배당etf", "배당주": "배당", "배당금": "배당"}


def log(stage, _lvl=logging.INFO, **kv):
    LOG.log(_lvl, "[%s] [%s] %s", stage, datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S"),
            " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) and (' ' in v or not v) else v}" for k, v in kv.items()))


def paths(topic, root=None):
    base = Path(root or ROOT) / topic
    t = base / "topics"
    return {"topic": topic, "base": base, "dir": t, "settings": t / "settings.toml", "json": t / "topics.json", "md": t / "주제탐색.md",
            "marks": t / "평가.txt", "material": t / "material.md", "page": t / "평가판.html",
            "out": base / "result" / "outliers", "source": base / "source"}


CHANNEL = Path("guides") / "channel.md"                 # 채널 설명 (사용자 지시 2026-10-28) — 재료 맨 위 0번
CHANNEL_MARK = ("<!-- channel:start -->", "<!-- channel:end -->")


def channel_lines(base):
    """<주제>/guides/channel.md 의 표시 줄 사이('한눈에') → 재료 맨 위 0번 줄들. 없거나 표시 줄이 없으면 WARNING + '못 읽음' 한 줄."""
    p = Path(base) / CHANNEL
    rel = f"{Path(base).name}/{CHANNEL.as_posix()}"
    try:
        body = p.read_text("utf-8").split(CHANNEL_MARK[0], 1)[1].split(CHANNEL_MARK[1], 1)[0].strip("\n")
    except (OSError, IndexError) as e:
        log("LOAD", logging.WARNING, channel=rel, error=type(e).__name__, next=f"{rel} 와 표시 줄 {CHANNEL_MARK[0]} … {CHANNEL_MARK[1]} 를 되살림")
        return [f"## 0. 채널 설명 — ⚠️ 못 읽음 (`{rel}`)", ""]
    log("LOAD", channel=rel, lines=len(body.splitlines()))
    return [f"## 0. 채널 설명 (`{rel}` — 주제·안은 이 목적·전달 방식에 맞게)", "", *body.splitlines(), ""]


# 같은 뜻 다른 말 → 하나로 (닮음 비교 전에 — '목돈 한 번에' = '일시금' · '10% 떨어질 때까지 기다렸다가' = '10% 빠질 때까지 기다렸다')
PHRASES = [(r"한\s?번에|한꺼번에|일시금|목돈\s?한\s?번", "일시금"), (r"나눠\s?(?:서\s?)?(?:사|매수)|분할\s?매수|\d+\s?개월로\s?나눠", "분할매수"),
           (r"떨어지|떨어질|떨어졌|빠지|빠질|빠졌|하락", "하락"), (r"기다리|기다렸|기다린", "기다림"), (r"몰빵|몰아\s?넣|집중\s?투자", "몰빵"),
           (r"적립식|매달\s?(?:사|모으|매수|적립)|매월", "적립"), (r"s\s?&\s?p\s?500|에스앤피|\bspy\b|\bvoo\b", "s&p500"), (r"나스닥\s?100|\bqqq\b", "나스닥")]


def norm_text(text):
    t = str(text or "").lower()
    for rx, rep in PHRASES:
        t = re.sub(rx, f" {rep} ", t)
    return t


def bigrams(text):
    t = re.sub(r"[^가-힣a-z0-9%&]", "", norm_text(text))
    return {t[i:i + 2] for i in range(len(t) - 1)}


def overlap(a, b):
    """글자 두 개씩의 겹침 (작은 쪽 기준) — 표현이 조금 달라도 같은 실험이면 높음 (2026-10-28 맞춤: 같은 주제 0.61~0.89 · 다른 주제 0.33 이하)."""
    return len(a & b) / min(len(a), len(b)) if a and b else 0.0


def toks(text):
    """닮음 비교용 낱말 집합 (조사 떼기 · 티커·같은 뜻 말 하나로)."""
    text = norm_text(text)
    out = set()
    for w in pz.kw_tokens(text or "", "ko", set()):
        w2 = w.lower()
        out.add(SYN.get(w2, w2))
    for w in re.findall(r"[A-Za-z][A-Za-z0-9&]{1,}", text or ""):
        w2 = w.lower()
        out.add(SYN.get(w2, w2))
    return {w for w in out if len(w) >= 2}


def jacc(a, b):
    return len(a & b) / len(a | b) if a and b else 0.0


# ---------------------------------------------------------------- 불러오기
NAMES = {"stock": "주식", "economic": "재테크"}
NAME = "주식"
# 안내 문구 (주제탐색.md 머리 · 평가판) — settings.toml [page] NOTE_DOC · NOTE_PAGE 가 있으면 그것
NOTE_DOC = "※ 연구·교육용 — 투자 권유가 아님. 결론은 **예상**이며 계산(`calc/`)으로 확정한다 — 판정 규칙이 있어 어느 쪽으로 나와도 결론은 하나."
NOTE_PAGE = "※ 연구·교육용 — 투자 권유가 아님. 결론은 계산 전 예상입니다."        # v1.4 되돌림 — 미리 계산 안내는 stock settings [page] NOTE_PAGE (v1.3 에서 기본값을 바꿔 재테크 평가판에도 찍히던 것)
# 후보 칸 설명 (material.md 머리 표) — settings.toml [fields] 가 있으면 그것
FIELD_HELP = {"data": "자료·기간 (실제 미국 주가·지수·재무제표, 2000년 이후 — 연도 필수)",
              "format": "테스트형 = 채널 방식 '테스트'·'문제' (항목 5개 — stock/guides/quick_test.md) · 실험형 = '비교 시뮬레이션' (질문 하나) — 0번",
              "market": "미국 · 한국 · 미국+한국",
              "data_kind": "주가 백테스트 · 재무제표 · 세금·법 · 환율 · 그 밖"}


def load_settings(P):
    """설정 읽기 + 주제 이름·칸 설명을 모듈 전역에 (문서·평가판 글귀)."""
    global NAME, FIELD_HELP, NOTE_DOC, NOTE_PAGE
    d = tomllib.loads(P["settings"].read_text("utf-8"))
    pg = d.get("page") or {}
    NAME = pg.get("NAME") or NAMES.get(P["topic"], P["topic"])
    NOTE_DOC, NOTE_PAGE = pg.get("NOTE_DOC") or NOTE_DOC, pg.get("NOTE_PAGE") or NOTE_PAGE
    FIELD_HELP = {**FIELD_HELP, **(d.get("fields") or {})}
    return d


def load_state(P, topic):
    if P["json"].is_file():
        return json.loads(P["json"].read_text("utf-8"))
    return {"topic": topic, "next_id": 1, "batches": [], "items": {}, "rejected": []}


def save_state(P, S):
    S["updated"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    S["tool"] = f"topic_ideas.py {VERSION}"
    P["json"].write_text(json.dumps(S, ensure_ascii=False, indent=1), "utf-8")


def load_analysis(P):
    """분석 결과 — 페르소나 · 댓글 니즈(제목으로 삼을 만한 댓글) · 주제 묶음 성공 비율 · 성공 사례 제목."""
    out = P["out"]
    pj = json.loads((out / "personas.json").read_text("utf-8")) if (out / "personas.json").is_file() else {"personas": [], "made": "-"}
    cj = json.loads((out / "comment_titles.json").read_text("utf-8")) if (out / "comment_titles.json").is_file() else {"picks": [], "generated": "-"}
    aj = json.loads((out / "analysis.json").read_text("utf-8")) if (out / "analysis.json").is_file() else {"themes": [], "success_cases": [], "generated": "-"}
    personas = {p["key"]: p for p in pj.get("personas") or []}
    needs = {x["pick"]: x for x in cj.get("picks") or []}
    themes = {}
    for t in aj.get("themes") or []:
        m = re.match(r"(\d+)\.", t["theme"])
        themes[m.group(1) if m else t["theme"]] = t
    success = aj.get("success_cases") or []
    success_ko = [dict(c, _toks=toks(c["title"])) for c in success if re.search(r"[가-힣]", c["title"])]   # 한국어 성공 사례만 (외국 제목으로 한국어 규칙 ✗)
    df = Counter(t for c in success_ko for t in c["_toks"])
    n = len(success_ko)
    idf = {t: math.log((n + 1) / (d + 1)) for t, d in df.items()}           # 흔한 말('s&p500'·'주식')은 무게가 작음
    return {"personas": personas, "persona_made": pj.get("made"), "needs": needs, "needs_made": cj.get("generated"), "themes": themes,
            "analysis_made": aj.get("generated"), "success": success, "success_ko": success_ko, "idf": idf, "idf_max": math.log(n + 1) if n else 1.0}


def theme_key(theme):
    m = re.match(r"\s*(\d+)", str(theme or ""))
    return m.group(1) if m else str(theme or "")


def used_entries(P, Z):
    """겹침 검사 대상: 설정의 옛 주제 · 올린 영상 제목 · stock/source/*/요약본 [방향]·[항목] 줄."""
    ents = [{"src": u["id"], "text": u["text"]} for u in Z.get("used") or []]
    up = P["base"] / "uploaded_videos.md"
    if up.is_file():
        for ln in up.read_text("utf-8").splitlines():
            m = re.match(r"\|\s*([a-z0-9\-]+)\s*\|[^|]*\|[^|]*\|[^|]*\|\s*(.+?)\s*\|\s*$", ln)
            if m and re.search(r"[a-z]", m.group(1)) and not m.group(1).endswith("-shorts") and "test" not in m.group(1):
                ents.append({"src": f"올림:{m.group(1)}", "text": m.group(2)})
    uc = P["source"] / "used_content.md"                    # 재테크 '이미 만든 대본' 표: | `영상ID` | 날짜 | 주제 | 결론 | 숫자·사례 |
    if uc.is_file():
        for ln in uc.read_text("utf-8").splitlines():
            m = re.match(r"\|\s*`?([a-z0-9\-]+)`?\s*\|[^|]*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|", ln)
            if m and re.search(r"[a-z]", m.group(1)):
                ents.append({"src": f"만든 대본:{m.group(1)}", "text": f"{m.group(2)} {m.group(3)}"})
    for d in sorted(P["source"].glob("*/")):
        f = d / "요약본.txt"
        if not f.is_file():
            continue
        # 요약본 칸: [방향] 앞 두 줄 · [항목 …]·[사례 …] 줄마다 · [제목 …] 줄마다 · [테스트 내용N] 머리 (첫 편 형식)
        #          + 새 꼴(summary_ideas.py): '#' 주석 줄은 뺌 · [방향] 안 '항목 N: a · b · c' 줄 하나 · [N안 …] 안 '제목 (P1-LT): …' 줄마다
        for blk in re.finditer(r"^\[([^\]]+)\]([^\n]*)\n(.*?)(?=^\[|\Z)", f.read_text("utf-8"), re.M | re.S):
            name, head, body = blk.group(1).strip(), blk.group(2).strip(), blk.group(3)
            lines = [re.sub(r"^\s*(?:[-•]|\d{1,2}\.)\s*", "", ln).strip() for ln in body.splitlines() if not ln.lstrip().startswith("#")]
            lines = [ln for ln in lines if len(ln) >= 6 and not ln.startswith(("뺄", "※")) and not re.match(r"^\|[\s\-|#]*\|?$", ln)]
            if name.startswith("방향"):
                ents.append({"src": f"{d.name}:방향", "text": " ".join(lines[:2])})
                for m in filter(None, (re.match(r"^항목\s?\d*\s?[:：]\s*(.+)$", ln) for ln in lines)):
                    ents.append({"src": f"{d.name}:항목", "text": m.group(1)})     # 줄 하나 그대로 — 짧게 나누면 글자 겹침(작은 쪽 기준)이 부풀어 다른 주제도 '같음'
            elif re.match(r"^\d+안\b", name):
                for m in filter(None, (re.match(r"^제목\s?\(([A-Z]\d+-[LS]T)\)\s?[:：]\s*(.+)$", ln) for ln in lines)):
                    ents.append({"src": f"{d.name}:제목 {m.group(1)}", "text": m.group(2)})
            elif name.startswith(("항목", "사례")):
                ents += [{"src": f"{d.name}:{name.split()[0]}{i}", "text": ln} for i, ln in enumerate(lines, 1)]
            elif name.startswith("제목"):
                ents += [{"src": f"{d.name}:제목{i}", "text": ln} for i, ln in enumerate(lines, 1)]
            elif name.startswith("테스트 내용"):
                ents.append({"src": f"{d.name}:{name}", "text": head})
    for e in ents:
        e["toks"], e["bg"] = toks(e["text"]), bigrams(e["text"])
    return ents


def scan_sources(P, S):
    """요약본에 '주제 ID: T003' 이 있으면 그 주제는 작성중 (폴더 이름을 적음)."""
    hit = 0
    for d in sorted(P["source"].glob("*/")):
        f = d / "요약본.txt"
        if not f.is_file():
            continue
        for m in re.finditer(r"주제\s?ID\s?[:：]\s?(T\d{3,})", f.read_text("utf-8")):
            it = S["items"].get(m.group(1))
            if it and it["status"] in ("이번 묶음", "대기"):
                it["status"], it["folder"] = "작성중", d.name
                hit += 1
    return hit


def read_marks(P):
    """평가.txt — 줄마다 'T003 좋음 까닭' (# 로 시작하면 설명). 같은 주제는 마지막 줄이 이김."""
    marks = {}
    if not P["marks"].is_file():
        return marks
    for ln in P["marks"].read_text("utf-8").splitlines():
        ln = ln.strip()
        if not ln or ln.startswith("#"):
            continue
        ln = re.sub(r"\s+#.*$", "", ln)                      # 줄 끝 '# 평가판 …' 메모
        m = re.match(r"(T\d{3,})\s*[,:]?\s*(\S+)\s*(.*)$", ln)
        if not m:
            continue
        if m.group(2) in ("지움", "취소"):
            marks.pop(m.group(1), None)
            continue
        v = "좋음" if GOOD.match(m.group(2)) else ("나쁨" if BAD.match(m.group(2)) else None)
        if v:
            marks[m.group(1)] = {"rating": v, "why": m.group(3).strip()}
    return marks


# ---------------------------------------------------------------- 거르기
def lint(c, Z, A):
    """명확한 결론인가 + 칸이 다 있는가 → 문제 목록 (없으면 통과)."""
    cl = Z["clarity"]
    bad = []
    for f in FIELDS:
        if (c.get(f) is None) if f == "needs" else not c.get(f):      # needs 는 빈 목록 가능 (이어진 댓글 니즈가 없는 주제 — 처음 점수가 낮아짐)
            bad.append(f"'{f}' 칸 없음")
    con = str(c.get("conclusion") or "")
    v = re.search(cl["VAGUE"], con)
    if v:
        bad.append(f"애매한 결론 ('{v.group(0)}')")
    if con and not re.search(cl["DECISIVE"], con):
        bad.append("결론에 숫자·판정 말 없음")
    if c.get("decide") and not re.search(cl["DECIDE"], str(c["decide"])):
        bad.append("판정 규칙에 기준(비교·문턱) 없음")
    if c.get("data") and not re.search(cl.get("YEAR") or r"(19|20)\d\d", str(c["data"])):     # v1.2.1 주제마다 (역사 = 세기·기원전·세 자리 해)
        bad.append("자료에 기간(연도) 없음")
    if c.get("persona") and c["persona"] not in A["personas"]:
        bad.append(f"페르소나 '{c['persona']}' 없음 (personas.json 키: {', '.join(A['personas'])})")
    for n in c.get("needs") or []:
        if n not in A["needs"]:
            bad.append(f"니즈 '{n}' 없음")
    if c.get("theme") and theme_key(c["theme"]) not in A["themes"]:
        bad.append(f"주제 묶음 '{c['theme']}' 없음")
    kinds = (Z.get("fields") or {}).get("DATA_KINDS")            # v1.4 settings [fields] DATA_KINDS 가 있으면 그 값만
    if kinds and c.get("data_kind") and c["data_kind"] not in kinds:
        bad.append(f"자료 갈래 '{c['data_kind']}' 없음 ({' · '.join(kinds)})")
    return bad


def ctext(c):
    return f"{c.get('title', '')} {c.get('question', '')}"


def nearest(text, ents, Z):
    """가장 닮은 것 — 닮음 = max(낱말 Jaccard ÷ SIM_MAX, 글자 겹침 ÷ OVERLAP_MAX) 로 맞춘 값 (1 이상이면 같은 주제)."""
    tk, bg = toks(text), bigrams(text)
    best = (0.0, None, 0.0, 0.0)
    for e in ents:
        j, o = jacc(tk, e["toks"]), overlap(bg, e["bg"])
        s = max(j / Z["dedupe"]["SIM_MAX"], o / Z["dedupe"]["OVERLAP_MAX"])
        if s > best[0]:
            best = (s, e, j, o)
    return best


# ---------------------------------------------------------------- 점수
def features(it):
    f = [f"페르소나:{it['persona']}", f"형식:{it['format']}", f"주제 묶음:{theme_key(it['theme'])}", f"시장:{it['market']}", f"자료:{it['data_kind']}"]
    f += [f"니즈:{n}" for n in it.get("needs") or []]
    return f


def prior(it, Z, A):
    w = Z["score"]
    likes = [A["needs"][n]["likes"] for n in it.get("needs") or [] if n in A["needs"]]
    max_likes = max([x["likes"] for x in A["needs"].values()] or [1])
    need = math.log1p(max(likes)) / math.log1p(max_likes) if likes else 0.0
    rates = [t["rate"] for t in A["themes"].values()] or [1]
    th = A["themes"].get(theme_key(it["theme"]))
    theme = (th["rate"] / max(rates)) if th and max(rates) else 0.0
    shares = [p["share"] for p in A["personas"].values()] or [1]
    pp = A["personas"].get(it["persona"])
    persona = (pp["share"] / max(shares)) if pp else 0.0
    sup = [A["needs"][n].get("recent_same_country", 0) for n in it.get("needs") or [] if n in A["needs"]]
    gap = 1 - min(1.0, (min(sup) if sup else w["GAP_FULL"] / 2) / w["GAP_FULL"])
    tk = toks(ctext(it))

    def wj(a, b):                     # 무게 준 Jaccard (IDF — 성공 사례 제목에 흔한 말일수록 가벼움, 처음 보는 말 = 가장 무거움)
        wt = lambda t: A["idf"].get(t, A["idf_max"])
        u = sum(wt(t) for t in a | b)
        return sum(wt(t) for t in a & b) / u if u else 0.0
    sims = [(wj(tk, c["_toks"]), c) for c in A["success_ko"]]
    best = max(sims, key=lambda x: x[0]) if sims else (0.0, None)
    succ = min(1.0, best[0] / w["SUCCESS_FULL"])
    it["success_match"] = {"title": best[1]["title"][:80], "sim": round(best[0], 3)} if best[1] else None
    parts = {"니즈": need, "주제 묶음": theme, "페르소나": persona, "공급 틈": gap, "성공 사례": succ}
    total = (w["W_NEED"] * need + w["W_THEME"] * theme + w["W_PERSONA"] * persona + w["W_GAP"] * gap + w["W_SUCCESS"] * succ)
    return total, parts


def learn(S, marks):
    """갈래별 가중치 = log((좋음+1)/(나쁨+1)) — 평가한 주제의 갈래에서."""
    g, b = Counter(), Counter()
    for tid, m in marks.items():
        it = S["items"].get(tid)
        if not it:
            continue
        for f in features(it):
            (g if m["rating"] == "좋음" else b)[f] += 1
    W = {f: math.log((g[f] + 1) / (b[f] + 1)) for f in set(g) | set(b)}
    return W, g, b


def learned_score(it, W, S, marks, Z):
    fs = [W[f] for f in features(it) if f in W]
    feat = sum(fs) / len(fs) if fs else 0.0
    tk = toks(ctext(it))
    sg = max([jacc(tk, toks(ctext(S["items"][t]))) for t, m in marks.items() if m["rating"] == "좋음" and t in S["items"] and t != it["id"]] or [0.0])
    sb = max([jacc(tk, toks(ctext(S["items"][t]))) for t, m in marks.items() if m["rating"] == "나쁨" and t in S["items"] and t != it["id"]] or [0.0])
    w = Z["score"]
    return w["W_LEARN_FEATURE"] * feat + w["W_LEARN_SIMILAR"] * (sg - sb), {"갈래": round(feat, 3), "닮은 좋음": round(sg, 3), "닮은 나쁨": round(sb, 3)}


def score_all(S, Z, A, marks):
    W, g, b = learn(S, marks)
    for it in S["items"].values():
        p, parts = prior(it, Z, A)
        l, lparts = learned_score(it, W, S, marks, Z)
        it["score"] = round(p + l, 4)
        it["score_parts"] = {"처음": round(p, 3), **{k: round(v, 3) for k, v in parts.items()}, "배운": round(l, 3), **lparts}
        it["rating"] = marks.get(it["id"], {}).get("rating")
        it["rating_why"] = marks.get(it["id"], {}).get("why", "")
    return W, g, b


# ---------------------------------------------------------------- 묶음
def current_batch(S):
    return S["batches"][-1] if S["batches"] else None


def pre_out(it):
    """v1.3 미리 계산에서 빠진 주제 (cmd_precheck 가 정함) — 나쁨처럼 '남은 것'·새 묶음에서 뺌."""
    return bool((it.get("precheck") or {}).get("out"))


def batch_done(S):
    b = current_batch(S)
    if not b:
        return True
    left = [t for t in b["ids"] if S["items"][t]["status"] == "이번 묶음" and S["items"][t].get("rating") != "나쁨" and not pre_out(S["items"][t])]
    return not left


def pick_batch(S, Z, W, marks, carry=()):
    """carry (v1.4) = 앞 묶음에서 이어 가는 좋음 주제 — 먼저 넣고 나머지를 탐색 자리·점수 순으로."""
    cfg = Z["batch"]
    pool = [it for it in S["items"].values() if it["status"] == "대기" and it.get("rating") != "나쁨" and not pre_out(it)]
    pool.sort(key=lambda it: -it["score"])
    chosen, per_theme, per_need = [], Counter(), Counter()

    def ok(it):
        if per_theme[theme_key(it["theme"])] >= cfg["MAX_PER_THEME"]:
            return False
        if any(per_need[n] >= cfg["MAX_PER_NEED"] for n in it.get("needs") or []):
            return False
        tk, bg = toks(ctext(it)), bigrams(ctext(it))
        return all(jacc(tk, toks(ctext(c))) < Z["dedupe"]["SIM_MAX_BATCH"] and overlap(bg, bigrams(ctext(c))) < Z["dedupe"]["OVERLAP_MAX_BATCH"]
                   for c in chosen)

    def take(it, why):
        chosen.append(it)
        it["picked_why"] = why
        per_theme[theme_key(it["theme"])] += 1
        for n in it.get("needs") or []:
            per_need[n] += 1

    for it in carry:                                # v1.4 좋음 이어 가기 (묶음 제한은 같이 셈)
        if len(chosen) < cfg["SIZE"] and it not in chosen:
            take(it, "좋음 — 앞 묶음에서 이어 감")
    explore = cfg["EXPLORE"] if len(marks) >= 5 else 0
    if explore:                                     # 아직 평가 없는 갈래 (페르소나·형식·주제 묶음)
        for it in pool:
            if len(chosen) >= explore + len(carry):
                break
            fs = [f for f in features(it)[:3] if f not in W]
            if fs and it not in chosen and ok(it):
                take(it, "탐색 자리 (평가 없는 갈래: " + ", ".join(fs) + ")")
    for it in pool:
        if len(chosen) >= cfg["SIZE"]:
            break
        if it not in chosen and ok(it):
            take(it, "점수 순")
    no = len(S["batches"]) + 1
    for it in chosen:
        it["status"], it["batch"] = "이번 묶음", no
    S["batches"].append({"no": no, "made": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "ids": [it["id"] for it in chosen]})
    log("BATCH", no=no, picked=len(chosen), carried=len(carry), pool=len(pool), explore=explore, themes=json.dumps(dict(per_theme), ensure_ascii=False))
    return chosen


# ---------------------------------------------------------------- 명령
def cmd_add(topic, pool_path, root=None):
    P = paths(topic, root)
    Z, S, A = load_settings(P), load_state(P, topic), load_analysis(P)
    cands = json.loads(Path(pool_path).read_text("utf-8"))
    cands = cands.get("candidates", cands) if isinstance(cands, dict) else cands
    ents = used_entries(P, Z)
    log("LOAD", topic=topic, pool=str(pool_path), candidates=len(cands), used_entries=len(ents), personas=len(A["personas"]), needs=len(A["needs"]))
    def ent(src, text):
        return {"src": src, "text": text, "toks": toks(text), "bg": bigrams(text)}
    earlier = [ent(f"앞서 낸 {t}", ctext(it)) for t, it in S["items"].items()]
    accepted = []
    for c in cands:
        probs = lint(c, Z, A)
        s_used, e_used, j_used, o_used = nearest(ctext(c), ents, Z)
        s_prev, e_prev, j_prev, o_prev = nearest(ctext(c), earlier + [ent(f"이번 모음 {a['id']}", ctext(a)) for a in accepted], Z)
        if s_used >= 1:
            probs.append(f"이미 쓴·쓰는 주제와 같음 ({e_used['src']} · 낱말 {j_used:.2f} · 글자 {o_used:.2f})")
        if s_prev >= 1:
            probs.append(f"앞서 낸 주제와 같음 ({e_prev['src']} · 낱말 {j_prev:.2f} · 글자 {o_prev:.2f})")
        if probs:
            S["rejected"].append({"title": c.get("title"), "why": probs, "pool": str(pool_path), "at": datetime.now(timezone.utc).strftime("%Y-%m-%d")})
            log("CHECK", logging.WARNING, title=c.get("title", "?")[:40], result="뺌", why="; ".join(probs)[:200])
            continue
        tid = f"T{S['next_id']:03d}"
        S["next_id"] += 1
        it = {k: c.get(k) for k in FIELDS}
        it.update({"id": tid, "items": c.get("items") or [], "why": c.get("why", ""), "status": "대기", "pool": str(pool_path),
                   "added": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
                   "nearest_used": {"src": e_used["src"] if e_used else "-", "sim": round(s_used, 3), "words": round(j_used, 3), "chars": round(o_used, 3)}})
        S["items"][tid] = it
        accepted.append(it)
        log("CHECK", id=tid, title=it["title"][:40], result="통과", nearest=it["nearest_used"]["src"], sim=it["nearest_used"]["sim"])
    log("CHECK", topic=topic, accepted=len(accepted), rejected=len(cands) - len(accepted))
    return finish(topic, P, Z, S, A, refresh_ok=True)


def finish(topic, P, Z, S, A, refresh_ok=False):
    hit = scan_sources(P, S)
    marks = read_marks(P)
    W, g, b = score_all(S, Z, A, marks)
    log("LEARN", topic=topic, marks=len(marks), good=sum(1 for m in marks.values() if m["rating"] == "좋음"),
        bad=sum(1 for m in marks.values() if m["rating"] == "나쁨"), features=len(W), from_sources=hit)
    if batch_done(S) and refresh_ok:
        ready = sum(1 for it in S["items"].values() if it["status"] == "대기" and it.get("rating") != "나쁨" and not pre_out(it))
        if ready >= Z["batch"]["SIZE"]:
            pick_batch(S, Z, W, marks)
        else:                                       # 20개를 못 채우면 묶음을 만들지 않음 — 후보를 더 써서 add
            log("BATCH", logging.WARNING, note=f"대기 후보 {ready}개 < {Z['batch']['SIZE']}개 — 새 묶음을 만들지 않음",
                next=f"후보 {Z['batch']['SIZE'] - ready}개 이상을 더 써서 add (material.md 의 '배운 것'을 보고)")
    done = batch_done(S)
    save_state(P, S)
    P["md"].write_text(render(S, Z, A, W, g, b, marks, done), "utf-8")
    P["page"].write_text(render_page(S, A), "utf-8")
    b2 = current_batch(S)
    left = [t for t in (b2["ids"] if b2 else []) if S["items"][t]["status"] == "이번 묶음" and S["items"][t].get("rating") != "나쁨" and not pre_out(S["items"][t])]
    log("WRITE", md=str(P["md"].relative_to(P["base"].parent)), json=str(P["json"].relative_to(P["base"].parent)), page=str(P["page"].relative_to(P["base"].parent)),
        batch=b2["no"] if b2 else 0, left=len(left), refresh_needed=done)
    if done:
        log("DONE", logging.WARNING, note="이번 묶음을 모두 쓰거나 나쁨 — 새 후보 모음을 써서 add (material.md 부터)", next=f"python3 tools/topic_ideas.py {topic} material")
    return S


def cmd_status(topic, root=None):
    P = paths(topic, root)
    return finish(topic, P, load_settings(P), load_state(P, topic), load_analysis(P))


def cmd_mark(topic, tid, rating, why="", root=None):
    P = paths(topic, root)
    v = "좋음" if GOOD.match(rating) else ("나쁨" if BAD.match(rating) else None)
    if not v:
        raise SystemExit("평가는 좋음 · 나쁨 (👍 · 👎)")
    S = load_state(P, topic)
    if tid not in S["items"]:
        raise SystemExit(f"{tid} 없음")
    new = not P["marks"].is_file()
    with open(P["marks"], "a", encoding="utf-8") as f:
        if new:
            f.write(MARKS_HEAD.replace("__NAME__", NAME))
        f.write(f"{tid} {v} {why}".rstrip() + "\n")
    log("LEARN", id=tid, rating=v, why=why or "-", title=S["items"][tid]["title"][:40])
    return cmd_status(topic, root)


def cmd_use(topic, tid, folder, root=None, done=False):
    P = paths(topic, root)
    S = load_state(P, topic)
    if tid not in S["items"]:
        raise SystemExit(f"{tid} 없음")
    it = S["items"][tid]
    pc = it.get("precheck")
    if not done and (not pc or pc.get("out")):                      # v1.3 — 요약본 전에 정답 미리 확인 (stock/topics/README.md)
        log("CHECK", logging.WARNING, id=tid, precheck=(pc or {}).get("class", "없음"),
            note="정답 미리 확인이 없거나 빠진 주제 — 요약본 전에 stock/topics/precheck/precheck.py 로 계산 → precheck 명령",
            next=f"python3 tools/topic_ideas.py {topic} precheck <결과.json>")
    it["status"] = "작성함" if done else "작성중"
    if folder:
        it["folder"] = folder
    save_state(P, S)
    log("BATCH", id=tid, status=it["status"], folder=it.get("folder", "-"))
    return cmd_status(topic, root)


def cmd_precheck(topic, path, fixes=None, root=None):
    """v1.3 정답 미리 확인 결과(precheck.py JSON: results[ID] = {class, answer, why}) + Claude 가 쓴 고친 결론(JSON: {ID: 문장}) → 주제마다 precheck.
    settings [precheck] EXCLUDE 분류 · NO_TEST 분류인데 형식이 테스트형 → out (묶음에서 뺌)."""
    P = paths(topic, root)
    Z, S = load_settings(P), load_state(P, topic)
    cfg = Z.get("precheck") or {}
    excl, notest = set(cfg.get("EXCLUDE", ["미확인"])), set(cfg.get("NO_TEST", ["조건부형"]))
    res = json.loads(Path(path).read_text("utf-8"))
    rs = res.get("results", res)
    fx = json.loads(Path(fixes).read_text("utf-8")) if fixes else {}
    n = Counter()
    for tid, r in rs.items():
        if tid not in S["items"]:
            continue
        it = S["items"][tid]
        cls = r.get("class", "미확인")
        out_ = cls in excl or (cls in notest and it.get("format") == "테스트형")
        it["precheck"] = {"class": cls, "answer": str(r.get("answer", "")), "why": str(r.get("why", "")), "conclusion": fx.get(tid, ""),
                          "out": out_, "out_why": ("자료가 없어 확인 못 함" if cls in excl else "조건에 따라 갈리는데 정답을 맞히는 테스트형") if out_ else "",
                          "file": str(path), "made": res.get("made", ""), "data_last": res.get("data_last", "")}
        n[cls] += 1
        log("CHECK", id=tid, precheck=cls, out=out_, conclusion=(fx.get(tid) or "-")[:60])
    log("CHECK", topic=topic, precheck=json.dumps(dict(n), ensure_ascii=False), out=sum(1 for it in S["items"].values() if pre_out(it)))
    save_state(P, S)
    return finish(topic, P, Z, S, load_analysis(P), refresh_ok=True)


def cmd_revise(topic, path, root=None):
    """v1.4 주제 칸 고치기 — {ID: {칸: 새 값, ..., "why": 까닭}}. 평가는 그대로 (같은 생각을 더 분명히 다시 짠 것) ·
    옛 값은 item['revised'] 에 · 뜻이 바뀌면(질문·결론·판정·자료·형식…) 미리 계산은 precheck_old 로 옮겨 다시 계산하게 (갈래 이름만이면 그대로) ·
    고친 뒤 lint 를 못 넘으면 그 주제는 안 바꿈."""
    P = paths(topic, root)
    Z, S, A = load_settings(P), load_state(P, topic), load_analysis(P)
    fx = json.loads(Path(path).read_text("utf-8"))
    ok_n = 0
    for tid, ch in fx.items():
        if tid not in S["items"]:
            log("CHECK", logging.WARNING, id=tid, result="없는 주제", next_step="topics.json 의 ID 확인")
            continue
        it = S["items"][tid]
        why = str(ch.get("why", ""))
        new = {k: v for k, v in ch.items() if k in FIELDS or k == "items"}
        probs = lint({**{k: it.get(k) for k in FIELDS}, **new}, Z, A)
        if probs:
            log("CHECK", logging.WARNING, id=tid, result="안 바꿈", why="; ".join(probs)[:200])
            continue
        old = {k: it.get(k) for k in new if it.get(k) != new[k]}
        it.update(new)
        it.setdefault("revised", []).append({"at": datetime.now(timezone.utc).strftime("%Y-%m-%d"), "old": old, "why": why, "file": str(path)})
        redo = bool(set(old) - {"data_kind", "theme", "persona", "needs", "market"})     # 갈래 이름만 바꾼 것은 계산을 다시 안 함
        if redo and it.get("precheck"):
            it["precheck_old"] = it.pop("precheck")
        ok_n += 1
        log("CHECK", id=tid, result="고침", fields=",".join(old) or "-", why=why[:80], precheck="다시 계산" if redo else "그대로")
    log("CHECK", topic=topic, revised=ok_n, asked=len(fx))
    save_state(P, S)
    return finish(topic, P, Z, S, A)


def cmd_refresh(topic, root=None):
    """v1.4 묶음 갈기 — 지금 묶음의 모든 주제가 평가(좋음·나쁨)·작성·뺌 중 하나면: 좋음(미리 계산 통과)은 새 묶음에 이어 가고,
    안 쓴 나머지는 대기로 돌린 뒤 점수 순으로 채움. 20개를 못 채우면 아무것도 바꾸지 않고 몇 개가 더 필요한지 적음."""
    P = paths(topic, root)
    Z, S, A = load_settings(P), load_state(P, topic), load_analysis(P)
    scan_sources(P, S)
    marks = read_marks(P)
    W, g, b = score_all(S, Z, A, marks)
    cur = current_batch(S)
    ids = [t for t in (cur["ids"] if cur else []) if S["items"][t]["status"] == "이번 묶음"]
    unrated = [t for t in ids if not S["items"][t].get("rating") and not pre_out(S["items"][t])]
    if unrated:
        log("BATCH", logging.WARNING, note=f"아직 평가 안 한 주제 {len(unrated)}개 — 묶음을 갈지 않음", ids=",".join(unrated))
        return finish(topic, P, Z, S, A)
    carry = [S["items"][t] for t in ids if S["items"][t].get("rating") == "좋음" and not pre_out(S["items"][t])]
    carry.sort(key=lambda it: -it["score"])
    ready = len(carry) + sum(1 for it in S["items"].values() if it["status"] == "대기" and it.get("rating") != "나쁨" and not pre_out(it))
    if ready < Z["batch"]["SIZE"]:
        log("BATCH", logging.WARNING, note=f"쓸 수 있는 주제 {ready}개 < {Z['batch']['SIZE']}개 — 묶음을 갈지 않음",
            next=f"후보 {Z['batch']['SIZE'] - ready}개 이상을 더 써서 add")
        return finish(topic, P, Z, S, A)
    for t in ids:
        S["items"][t]["status"] = "대기"
    log("BATCH", note="묶음 갈기", old=cur["no"] if cur else 0, carried=",".join(it["id"] for it in carry) or "-", ready=ready)
    pick_batch(S, Z, W, marks, carry=carry)
    return finish(topic, P, Z, S, A)


def cmd_import(topic, path, root=None):
    """평가판(Artifact db 'marks' 모음) → 평가.txt. Claude 가 ArtifactData list 결과를 파일로 저장해 넘김.
    문서마다 id(=T003)·rating(좋음|나쁨|빈칸=지움)·why·at. 지금 평가와 다른 것만 한 줄씩 더함 (빈칸 = '지움' 줄)."""
    P = paths(topic, root)
    src = Path(path)
    docs = []
    if src.is_dir():                                   # ArtifactData list … out_dir= → <dir>/marks/<id>.json
        for f in sorted(src.rglob("*.json")):
            d = json.loads(f.read_text("utf-8"))
            docs.append(d if "data" in d else {"id": f.stem, "data": d})
    else:
        txt = src.read_text("utf-8")
        try:
            raw = json.loads(txt)
            docs = raw if isinstance(raw, list) else (raw.get("documents") or raw.get("docs") or raw.get("items") or raw.get("results") or [])
        except json.JSONDecodeError:                   # ArtifactData list 결과를 그대로 붙인 글 — 문서마다 JSON 한 줄
            docs = [json.loads(ln) for ln in txt.splitlines() if ln.strip().startswith("{")]
    cur = read_marks(P)
    S = load_state(P, topic)
    lines, seen = [], 0
    for d in docs:
        body = d.get("data") if isinstance(d.get("data"), dict) else d
        tid = str(d.get("id") or d.get("doc_id") or str(d.get("path", "")).split("/")[-1])
        if not re.match(r"^T\d{3,}$", tid) or tid not in S["items"]:
            continue
        seen += 1
        r = str(body.get("rating") or "")
        why = re.sub(r"\s+", " ", str(body.get("why") or "")).strip()[:120]
        if r in ("좋음", "나쁨") and (cur.get(tid, {}).get("rating") != r or cur.get(tid, {}).get("why", "") != why):
            lines.append(f"{tid} {r} {why}".rstrip() + f"  # 평가판 {str(body.get('at') or '')[:16]}")
        elif not r and tid in cur:
            lines.append(f"{tid} 지움  # 평가판 {str(body.get('at') or '')[:16]}")
    if lines:
        new = not P["marks"].is_file()
        with open(P["marks"], "a", encoding="utf-8") as f:
            if new:
                f.write(MARKS_HEAD.replace("__NAME__", NAME))
            f.write("\n".join(lines) + "\n")
    log("LEARN", topic=topic, source=str(path), page_docs=seen, new_lines=len(lines))
    return cmd_status(topic, root)


MARKS_HEAD = """# __NAME__ 주제 평가 — 줄마다 '주제ID 좋음|나쁨 까닭(선택)'. 예: T003 좋음 댓글 니즈가 커서 / T007 나쁨 너무 어려움
# GitHub 에서 이 파일 끝에 줄을 더하거나, Claude 에게 'T003 좋아, T007 별로'라고 말하면 됨. 같은 주제는 마지막 줄이 이김.
# 평가는 다음 묶음의 순위에 반영된다 (tools/topic_ideas.py — 주제탐색.md 3번 '배운 것').
"""


def cmd_material(topic, root=None):
    P = paths(topic, root)
    Z, S, A = load_settings(P), load_state(P, topic), load_analysis(P)
    scan_sources(P, S)
    marks = read_marks(P)
    W, g, b = score_all(S, Z, A, marks)
    ents = used_entries(P, Z)
    L = [f"# {topic} 주제 후보를 쓰기 전 재료 (자동 — `tools/topic_ideas.py {VERSION}`)", "",
         f"분석 {A['analysis_made']} · 페르소나 {A['persona_made']} · 댓글 니즈 {A['needs_made']}. 후보는 `{topic}/topics/pool/<날짜>.json` 에 쓰고 `add`. ※ 연구·교육용.", "",
         *channel_lines(P["base"]),
         "## 후보 한 개의 칸 (모두 필수 — 빠지면 뺌)", "",
         "| 칸 | 내용 |", "|---|---|",
         "| title | 주제 한 줄 (영상 제목 아님) |", "| question | 시청자가 묻는 것 한 문장 |",
         "| conclusion | **예상 결론 한 문장 — 숫자·판정으로** ('…보다 …가 더 남았다', 'N년 이상이면 손실 0%'). 애매한 말 금지: " + Z["clarity"]["VAGUE"].replace("\\s?", " ").replace("|", "·")[:160] + " |",
         "| decide | 판정 규칙 — 자료가 어느 쪽으로 나와도 결론이 하나로 정해지는 기준 ('A가 B보다 높은 구간이 50% 넘으면 A, 아니면 B') |",
         f"| data | {FIELD_HELP['data']} |",
         f"| format | {FIELD_HELP['format']} |",
         "| persona | personas.json 키: " + ", ".join(f"`{k}` ({p['name']})" for k, p in A["personas"].items()) + " |",
         "| theme | 주제 묶음 번호 (아래 3번 표) |", "| needs | 댓글 니즈 ID 목록 (아래 2번 표) |", f"| market | {FIELD_HELP['market']} |",
         f"| data_kind | {FIELD_HELP['data_kind']} |", "| items | (테스트형) 항목 예 3개 |", "| why | 이 주제를 고른 까닭 한 줄 |", ""]
    L += [f"## 1. 페르소나 ({topic}/result/outliers/personas.md)", "", "| 키 | 이름 | 몫 | 지식 | 가장 흔한 처지 | 원하는 것 (질문 속 용어) | 좋아요 많은 질문 |", "|---|---|---|---|---|---|---|"]
    for k, p in A["personas"].items():
        L.append(f"| `{k}` | {p['name']} | {p['share']:.0%} | {p['know']['level']} | {p['states'][0]['name'] if p['states'] else '-'} | "
                 + " · ".join(f"{t} {n}" for t, n in p["want_terms"][:6]) + " | " + " / ".join(q["text"][:50].replace("|", "/") for q in p["top_questions"][:2]) + " |")
    L += ["", f"## 2. 댓글 니즈 ({topic}/result/outliers/comment_titles.md — 같은 내용 최근 제목이 적을수록 틈)", "", "| ID | 나라 | 니즈 | 👍 | 같은 내용 최근 제목 |", "|---|---|---|---|---|"]
    for k, x in A["needs"].items():
        L.append(f"| {k} | {x['country']} | {x['topic'][:70]} | {x['likes']:,} | {x.get('recent_same_country', '-')} |")
    L += ["", "## 3. 주제 묶음 성공 비율 (analysis.json themes)", "", "| 번호 | 묶음 | 영상 | 성공 | 비율 |", "|---|---|---|---|---|"]
    for k, t in sorted(A["themes"].items(), key=lambda x: -x[1]["rate"]):
        L.append(f"| {k} | {t['theme']} | {t['n']} | {t['success']} | {t['rate']:.0%} |")
    L += ["", "## 4. 성공 사례 제목 (무게 큰 순 20 — 한국어)", ""]
    ko = [c for c in A["success"] if re.search(r"[가-힣]", c["title"])]
    for c in sorted(ko, key=lambda c: -(c.get("weight") or 0))[:20]:
        L.append(f"- {c['title'][:90]} (무게 {c.get('weight', 0):.1f} · {c['theme']})")
    L += ["", f"## 5. 이미 쓴·쓰는 주제 — 같으면 뺌 (낱말 닮음 ≥ {Z['dedupe']['SIM_MAX']} 또는 글자 겹침 ≥ {Z['dedupe']['OVERLAP_MAX']})", ""]
    for e in ents:
        L.append(f"- `{e['src']}` {e['text'][:110]}")
    for t, it in S["items"].items():
        L.append(f"- `앞서 낸 {t}` ({it['status']}{' · ' + it['rating'] if it.get('rating') else ''}) {it['title']}")
    L += ["", "## 6. 배운 것 (평가 " + str(len(marks)) + "개) — 좋은 갈래 쪽으로 더 쓰고, 나쁜 갈래는 줄인다", ""]
    if W:
        for f, w in sorted(W.items(), key=lambda x: -x[1]):
            L.append(f"- {f}: {w:+.2f} (좋음 {g[f]} · 나쁨 {b[f]})")
        for t, m in marks.items():
            if t in S["items"]:
                L.append(f"  - {t} {m['rating']}: {S['items'][t]['title']}" + (f" — {m['why']}" if m["why"] else ""))
    else:
        L.append("- 아직 평가 없음 — 처음 점수(분석 결과)만으로 순위.")
    P["material"].write_text("\n".join(L) + "\n", "utf-8")
    log("WRITE", material=str(P["material"].relative_to(P["base"].parent)), used=len(ents), items=len(S["items"]))


# ---------------------------------------------------------------- 문서
def render(S, Z, A, W, g, b, marks, done):
    B = current_batch(S)
    tp = S.get("topic", "stock")
    L = [f"# {NAME} 주제 탐색 — 분석 결과·페르소나로 20개씩, 평가를 배워 고름 (자동)", "",
         f"`tools/topic_ideas.py {VERSION}` · 갱신 {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M')} UTC · 분석 {A['analysis_made']} · 페르소나 {A['persona_made']} · "
         f"댓글 니즈 {A['needs_made']}. 손으로 고치지 않는다 (주제 글은 `{tp}/topics/pool/`, 평가는 `{tp}/topics/평가.txt`).",
         "사용자 지시 2026-10-28 \"분석 결과, 페르소나를 토대로 주제 20개씩 생성 … 좋다고, 나쁘다고 표시 가능하도록 해서 그걸 학습 후 되도록 좋은 주제로 탐색 … 명확하게 결론\".",
         NOTE_DOC, "",
         "## 평가하는 법", "",
         f"- `{tp}/topics/평가.txt` 끝에 한 줄: `T003 좋음 까닭` · `T007 나쁨 까닭` (까닭은 선택 — 배울 때 참고). GitHub 에서 고치거나, Claude 에게 'T003 좋아, T007 별로'.",
         "- 평가는 순위에 바로 반영되고(3번), 다음 20개를 고를 때 좋은 갈래 쪽으로 뽑는다. **나쁨** 주제는 쓰지 않은 것으로 끝남.",
         "- 쓰기 시작하면 요약본에 `주제 ID: T003` → 작성중. 이번 묶음이 모두 작성중·작성함·나쁨이 되면 **새 20개로 갱신**.", ""]
    if B:
        ids = B["ids"]
        st = Counter(S["items"][t]["status"] for t in ids)
        L += [f"## 1. 이번 묶음 — {B['no']}번째 ({B['made'][:10]}) · {len(ids)}개 · 남은 것 "
              f"{sum(1 for t in ids if S['items'][t]['status'] == '이번 묶음' and S['items'][t].get('rating') != '나쁨')}개"
              + (" · ⚠️ **갱신 필요**" if done else ""), "",
              "- **미리 계산** (v1.3 — `stock/topics/README.md` '정답 미리 확인'): 정답형 · 차이없음 · 사실형 · 계산형 → 요약본 가능 · 조건부형 → 비교·내기의 크기로만 (테스트형 ✗) · 미확인 → 자료 전엔 안 씀. ⛔ = 묶음에서 뺌.", "",
              "| 순위 | ID | 주제 | 결론 (미리 계산 뒤 · 없으면 예상) | 미리 계산 | 대상 | 형식 | 상태 | 평가 | 점수 |", "|---|---|---|---|---|---|---|---|---|---|"]
        rows = sorted((S["items"][t] for t in ids), key=lambda it: -it["score"])
        for i, it in enumerate(rows, 1):
            pp = A["personas"].get(it["persona"], {})
            pc = it.get("precheck") or {}
            L.append(f"| {i} | **{it['id']}** | {it['title']} | {pc.get('conclusion') or it['conclusion']} | {('⛔ ' if pc.get('out') else '') + pc.get('class', '전')} | "
                     f"{pp.get('id', '?')} {pp.get('name', it['persona'])} | {it['format']} | "
                     f"{it['status']}{' (' + it['folder'] + ')' if it.get('folder') else ''} | {('👍' if it.get('rating') == '좋음' else '👎' if it.get('rating') == '나쁨' else '')} | {it['score']:.2f} |")
        L += ["", "## 2. 주제별 자세히", ""]
        for i, it in enumerate(rows, 1):
            pp = A["personas"].get(it["persona"], {})
            th = A["themes"].get(theme_key(it["theme"]), {})
            needs = [A["needs"][n] for n in it.get("needs") or [] if n in A["needs"]]
            sp = it["score_parts"]
            L += [f"### {i}. {it['id']} {it['title']}", "",
                  f"- **질문**: {it['question']}",
                  f"- **결론 (예상)**: {it['conclusion']}",
                  *([f"- **미리 계산 ({it['precheck']['class']}{' · ⛔ 뺌 — ' + it['precheck']['out_why'] if it['precheck'].get('out') else ''})**: "
                     f"{it['precheck'].get('conclusion') or it['precheck']['answer']} — {it['precheck']['why']} (`{it['precheck']['file']}`)"] if it.get("precheck") else
                    ["- **미리 계산**: 아직 — 요약본 전에 `stock/topics/precheck/precheck.py`"]),
                  f"- **판정 규칙**: {it['decide']}",
                  f"- **자료**: {it['data']} · {it['data_kind']} · {it['market']}"]
            if revised_why(it):
                L.append(f"- **다시 짬 (v1.4 revise)**: {revised_why(it)}")
            if it.get("items"):
                L.append("- **항목 예**: " + " / ".join(it["items"]))
            L.append(f"- **대상**: {pp.get('id', '?')} {pp.get('name', it['persona'])} ({pp.get('share', 0):.0%} · 지식 {pp.get('know', {}).get('level', '-')}) · "
                     f"주제 묶음 {th.get('theme', it['theme'])} (성공 {th.get('rate', 0):.0%})")
            if needs:
                L.append("- **댓글 니즈**: " + " · ".join(f"{n['pick']} {n['topic'][:50]} (👍{n['likes']:,} · 같은 내용 최근 제목 {n.get('recent_same_country', '-')})" for n in needs))
            if it.get("why"):
                L.append(f"- **고른 까닭**: {it['why']}")
            nu = it["nearest_used"]
            L.append(f"- **겹침 확인**: 가장 닮은 쓴 주제 `{nu['src']}` — 낱말 {nu.get('words', 0):.2f} (기준 {Z['dedupe']['SIM_MAX']}) · 글자 {nu.get('chars', 0):.2f} "
                     f"(기준 {Z['dedupe']['OVERLAP_MAX']}) → 둘 다 기준 아래 = 다른 주제")
            if it.get("success_match") and it["success_match"]["sim"] > 0:
                L.append(f"- **닮은 성공 사례**: {it['success_match']['title']} (낱말 닮음 {it['success_match']['sim']:.2f})")
            L.append(f"- **점수 {it['score']:.2f}** = 처음 {sp['처음']:.2f} (니즈 {sp['니즈']:.2f} · 묶음 {sp['주제 묶음']:.2f} · 페르소나 {sp['페르소나']:.2f} · 틈 {sp['공급 틈']:.2f} · 성공 사례 {sp['성공 사례']:.2f}) "
                     f"+ 배운 {sp['배운']:+.2f} (갈래 {sp['갈래']:+.2f} · 닮은 좋음 {sp['닮은 좋음']:.2f} · 닮은 나쁨 {sp['닮은 나쁨']:.2f}) · 뽑힌 까닭: {it.get('picked_why', '-')}")
            if it.get("rating"):
                L.append(f"- **평가**: {it['rating']}" + (f" — {it['rating_why']}" if it.get("rating_why") else ""))
            L.append("")
    L += [f"## 3. 배운 것 — 평가 {len(marks)}개", ""]
    if W:
        L += ["| 갈래 | 가중치 | 좋음 | 나쁨 |", "|---|---|---|---|"]
        for f, w in sorted(W.items(), key=lambda x: -x[1]):
            L.append(f"| {f} | {w:+.2f} | {g[f]} | {b[f]} |")
    else:
        L.append("- 아직 평가 없음 — 순위는 처음 점수(분석 결과)만. 평가가 5개 넘으면 다음 묶음부터 '평가 없는 갈래' 탐색 자리 "
                 f"{Z['batch']['EXPLORE']}개가 생긴다.")
    L += ["", "## 4. 점수 매기는 법", "",
          f"- 처음 점수 (0~1) = 니즈 {Z['score']['W_NEED']} × log(이어진 댓글 니즈 👍) + 주제 묶음 {Z['score']['W_THEME']} × 성공 비율 + 페르소나 {Z['score']['W_PERSONA']} × 몫 + "
          f"공급 틈 {Z['score']['W_GAP']} × (1 − 같은 내용 최근 제목 ÷ {Z['score']['GAP_FULL']}) + 성공 사례 {Z['score']['W_SUCCESS']} × (한국어 성공 사례 제목과 가장 큰 낱말 닮음 ÷ {Z['score']['SUCCESS_FULL']}) — 각자 가장 큰 값 = 1.",
          f"- 배운 점수 = {Z['score']['W_LEARN_FEATURE']} × 갈래(페르소나·형식·주제 묶음·시장·자료·니즈)별 log((좋음+1)/(나쁨+1)) 평균 + "
          f"{Z['score']['W_LEARN_SIMILAR']} × (가장 닮은 좋음 주제 닮음 − 가장 닮은 나쁨 주제 닮음).",
          f"- 묶음 고르기: 점수 순 · 같은 주제 묶음 ≤ {Z['batch']['MAX_PER_THEME']} · 같은 니즈 ≤ {Z['batch']['MAX_PER_NEED']} · 후보끼리 닮음 < {Z['dedupe']['SIM_MAX_BATCH']}.",
          f"- 거르기: 결론에 애매한 말·숫자 없음 · 판정 규칙에 기준 없음 · 자료에 기간 없음 · 쓴 주제와 낱말 닮음 ≥ {Z['dedupe']['SIM_MAX']} 또는 글자 겹침 ≥ {Z['dedupe']['OVERLAP_MAX']} → 뺌 (6번).", ""]
    wait = sorted((it for it in S["items"].values() if it["status"] == "대기"), key=lambda it: -it["score"])
    if wait:
        L += [f"## 5. 대기 후보 {len(wait)}개 (이번 묶음에 안 든 것 — 다음 갱신 때 다시 겨룸)", ""]
        for it in wait:
            L.append(f"- {it['id']} {it['title']} — {it['conclusion']} (점수 {it['score']:.2f})")
        L.append("")
    if S["rejected"]:
        L += [f"## 6. 뺀 후보 {len(S['rejected'])}개 (애매한 결론·같은 주제)", ""]
        for r in S["rejected"][-40:]:
            L.append(f"- {r['title']} — {'; '.join(r['why'])}")
        L.append("")
    fin = [it for it in S["items"].values() if it["status"] in ("작성중", "작성함")]
    if fin:
        L += ["## 7. 쓰는·쓴 주제", ""] + [f"- {it['id']} {it['status']} `{it.get('folder', '-')}` {it['title']}" for it in fin] + [""]
    L += ["## 한계", "",
          "- 주제 글은 Claude 가 재료(`material.md`)를 읽고 쓴다 — 도구는 거르고·점수 매기고·뽑는다. 결론은 계산 전 **예상**.",
          "- 겹침은 낱말 닮음이다 — 같은 실험을 다른 말로 쓰면 못 잡을 수 있어 '가장 닮은 쓴 주제'를 함께 보인다.",
          "- 처음 점수는 분석 결과(댓글 니즈·성공 비율·페르소나)에서 — 평가가 적을 때 배운 점수는 흔들린다.", ""]
    return "\n".join(L)


# ---------------------------------------------------------------- 평가판 (Artifact 페이지 — 좋음·나쁨을 눌러 남김)
PAGE = r"""<title>__NAME__ 주제 평가판</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@400;500;700&family=IBM+Plex+Mono:wght@500&display=swap">
<style>
/* 한 줄 목록 — 주제 카드 20장, 위는 평가 셈과 거르기 */
:root{--bg:#f3f5f7;--card:#ffffff;--ink:#17202b;--muted:#5b6876;--line:#d9dfe6;--accent:#1f5f8b;--good:#167a5b;--goodbg:#e3f3ec;--bad:#b4442f;--badbg:#f8e6e1;
--sans:"IBM Plex Sans KR","Apple SD Gothic Neo","Malgun Gothic",system-ui,sans-serif;--mono:"IBM Plex Mono",ui-monospace,Menlo,monospace}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#11161c;--card:#19212a;--ink:#e6ebf0;--muted:#9aa7b4;--line:#2b3641;--accent:#7cb4dc;--good:#5cc79f;--goodbg:#173229;--bad:#ef8c76;--badbg:#3a211b;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#11161c;--card:#19212a;--ink:#e6ebf0;--muted:#9aa7b4;--line:#2b3641;--accent:#7cb4dc;--good:#5cc79f;--goodbg:#173229;--bad:#ef8c76;--badbg:#3a211b;color-scheme:dark}
body{background:var(--bg);color:var(--ink);font-family:var(--sans);font-size:15px;line-height:1.55}
.wrap{max-width:780px;margin:0 auto;padding-block:20px 48px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));display:grid;gap:14px}
header{display:grid;gap:6px}
h1{font-size:1.45rem;margin:0;text-wrap:balance;letter-spacing:-.01em}
.sub{color:var(--muted);font-size:.9rem;margin:0}
.bar{display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.count{font-size:.85rem;color:var(--muted);font-variant-numeric:tabular-nums}
.count b{color:var(--ink);font-family:var(--mono)}
.filt{display:flex;gap:6px;flex-wrap:wrap;margin-left:auto}
.filt button{font:inherit;font-size:.85rem;border:1px solid var(--line);background:var(--card);color:var(--ink);border-radius:999px;padding:4px 12px;cursor:pointer}
.filt button[aria-pressed="true"]{background:var(--ink);color:var(--bg);border-color:var(--ink)}
.note{font-size:.85rem;color:var(--muted);border-left:3px solid var(--line);padding-left:10px;margin:0}
.note.warn{border-color:var(--bad);color:var(--ink)}
ol{list-style:none;margin:0;padding:0;display:grid;gap:12px}
.card{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px 16px;display:grid;gap:8px;min-width:0}
.card.good{border-color:var(--good);box-shadow:inset 4px 0 0 var(--good)}
.card.bad{border-color:var(--bad);box-shadow:inset 4px 0 0 var(--bad)}
.meta{display:flex;flex-wrap:wrap;gap:6px;align-items:center;font-size:.8rem;color:var(--muted)}
.rank{font-family:var(--mono);color:var(--ink)}
.id{font-family:var(--mono);color:var(--accent)}
.chip{border:1px solid var(--line);border-radius:4px;padding:0 6px}
h2{font-size:1.05rem;margin:0;text-wrap:balance}
.concl{margin:0}
.concl span{font-size:.75rem;letter-spacing:.04em;color:var(--muted);margin-right:6px}
details{font-size:.88rem;color:var(--muted)}
details summary{cursor:pointer;color:var(--accent)}
details dl{display:grid;grid-template-columns:auto 1fr;gap:4px 10px;margin:8px 0 0}
details dt{color:var(--ink);font-weight:500}
details dd{margin:0;min-width:0}
.act{display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.act button{font:inherit;font-weight:500;border:1px solid var(--line);background:var(--card);color:var(--ink);border-radius:8px;padding:6px 14px;cursor:pointer;min-width:84px}
.act button.g[aria-pressed="true"]{background:var(--goodbg);border-color:var(--good);color:var(--good)}
.act button.b[aria-pressed="true"]{background:var(--badbg);border-color:var(--bad);color:var(--bad)}
.act input{flex:1 1 180px;min-width:0;font:inherit;font-size:.9rem;border:1px solid var(--line);border-radius:8px;padding:6px 10px;background:var(--bg);color:var(--ink)}
.state{font-size:.8rem;color:var(--muted);min-width:4em}
button:focus-visible,input:focus-visible,summary:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
button:disabled,input:disabled{opacity:.55;cursor:not-allowed}
</style>
<div class="wrap">
<header>
<h1>__NAME__ 주제 평가판</h1>
<p class="sub" id="sub"></p>
<p class="note">좋음·나쁨을 누르면 저장됩니다. 다시 누르면 지워집니다. 까닭은 짧게 (선택). Claude 가 다음에 이 평가를 읽어 배우고, 다음 20개를 고를 때 좋은 쪽으로 뽑습니다. __NOTE__</p>
<p class="note warn" id="offline" hidden>이 화면에서는 저장할 수 없습니다 (로그인이 필요하거나 보기 전용). 평가는 Claude 에게 'T003 좋아, T007 별로'처럼 말하면 됩니다.</p>
<div class="bar"><span class="count" id="count"></span>
<div class="filt" role="group" aria-label="거르기"><button type="button" data-f="all" aria-pressed="true">전체</button><button type="button" data-f="none" aria-pressed="false">평가 안 함</button><button type="button" data-f="good" aria-pressed="false">좋음</button><button type="button" data-f="bad" aria-pressed="false">나쁨</button></div></div>
</header>
<ol id="list"></ol>
</div>
<script id="data" type="application/json">__DATA__</script>
<script>
(function(){
const D=JSON.parse(document.getElementById("data").textContent);
const marks={};            // id -> {rating, why}  (저장소 값 — 처음엔 저장소의 평가.txt 값)
D.items.forEach(it=>{ if(it.rating) marks[it.id]={rating:it.rating,why:it.why||""}; });
let db=null, canWrite=false, filter="all";
const $=s=>document.querySelector(s);
$("#sub").textContent=`${D.batch}번째 묶음 · ${D.made} · 주제 ${D.items.length}개 · 분석 ${D.analysis}`;
function el(tag,attrs,text){const e=document.createElement(tag);for(const k in (attrs||{}))e.setAttribute(k,attrs[k]);if(text!=null)e.textContent=text;return e;}
function counts(){let g=0,b=0;D.items.forEach(it=>{const m=marks[it.id];if(m&&m.rating==="좋음")g++;else if(m&&m.rating==="나쁨")b++;});
  $("#count").innerHTML="";const c=$("#count");c.append("좋음 ");c.append(el("b",{},String(g)));c.append(" · 나쁨 ");c.append(el("b",{},String(b)));c.append(" · 평가 안 함 ");c.append(el("b",{},String(D.items.length-g-b)));}
function render(){
  const L=$("#list"); L.innerHTML="";
  D.items.forEach(it=>{
    const m=marks[it.id]||{}; const r=m.rating||"";
    if(filter==="none"&&r) return; if(filter==="good"&&r!=="좋음") return; if(filter==="bad"&&r!=="나쁨") return;
    const li=el("li",{class:"card"+(r==="좋음"?" good":r==="나쁨"?" bad":""),id:"c-"+it.id});
    const meta=el("div",{class:"meta"});
    meta.append(el("span",{class:"rank"},it.rank+"위"),el("span",{class:"id"},it.id),el("span",{class:"chip"},it.format),el("span",{class:"chip"},it.persona));
    if(it.status!=="이번 묶음") meta.append(el("span",{class:"chip"},it.status));
    li.append(meta, el("h2",{},it.title));
    const c=el("p",{class:"concl"}); c.append(el("span",{},/^\[/.test(it.title)?"결론(계산)":"결론(예상)")); c.append(document.createTextNode(it.conclusion)); li.append(c);
    const d=el("details"); d.append(el("summary",{},"질문 · 판정 규칙 · 자료 · 근거"));
    const dl=el("dl"); [["다시 짬",it.revised],["질문",it.question],["판정 규칙",it.decide],["자료",it.data],["근거",it.basis],["점수",it.score]].forEach(([k,v])=>{if(v){dl.append(el("dt",{},k),el("dd",{},String(v)));}});
    d.append(dl); li.append(d);
    const act=el("div",{class:"act"});
    const gb=el("button",{type:"button",class:"g","aria-pressed":String(r==="좋음"),id:"g-"+it.id},"좋음");
    const bb=el("button",{type:"button",class:"b","aria-pressed":String(r==="나쁨"),id:"b-"+it.id},"나쁨");
    const why=el("input",{type:"text",id:"w-"+it.id,placeholder:"까닭 (선택)",maxlength:"120","aria-label":it.id+" 까닭"}); why.value=m.why||"";
    const st=el("span",{class:"state",id:"s-"+it.id});
    [gb,bb,why].forEach(x=>{ if(!canWrite) x.disabled=true; });
    gb.addEventListener("click",()=>save(it.id, r==="좋음"?"":"좋음", why.value));
    bb.addEventListener("click",()=>save(it.id, r==="나쁨"?"":"나쁨", why.value));
    why.addEventListener("change",()=>{ if(marks[it.id]&&marks[it.id].rating) save(it.id, marks[it.id].rating, why.value); });
    act.append(gb,bb,why,st); li.append(act); L.append(li);
  });
  counts();
}
let busy=Promise.resolve();
function save(id,rating,why){
  if(!db||!canWrite) return;
  const st=document.getElementById("s-"+id); if(st) st.textContent="저장 중…";
  const body={rating:rating,why:(why||"").trim().slice(0,120),at:new Date().toISOString(),batch:D.batch};
  busy=busy.then(()=>db.collection("marks").doc(id).set(body)).then(()=>{
    if(rating) marks[id]={rating:rating,why:body.why}; else delete marks[id];
    render(); const s2=document.getElementById("s-"+id); if(s2) s2.textContent=rating?"저장됨":"지움";
  }).catch(e=>{ const s3=document.getElementById("s-"+id); if(s3) s3.textContent=(e&&e.code==="invalid_argument")?"저장 못 함 (권한)":"저장 못 함 — 다시 눌러 주세요"; });
}
document.querySelectorAll(".filt button").forEach(b=>b.addEventListener("click",()=>{filter=b.dataset.f;document.querySelectorAll(".filt button").forEach(x=>x.setAttribute("aria-pressed",String(x===b)));render();}));
render();
(async()=>{
  try{ db = window.claude && window.claude.use ? await window.claude.use("db") : null; }catch(e){ db=null; }
  if(!db){ $("#offline").hidden=false; return; }
  let user=null; try{ user=await window.claude.use("user"); }catch(e){}
  let cw=null; try{ cw = user ? await user.can("data.write") : null; }catch(e){ cw=null; }
  canWrite = cw!==false;
  if(!canWrite) $("#offline").hidden=false;
  db.collection("marks").onSnapshot(snap=>{
    snap.docs.forEach(doc=>{ const v=doc.data()||{}; if(v.rating) marks[doc.id]={rating:v.rating,why:v.why||""}; else delete marks[doc.id]; });
    render();
  },()=>{});
  render();
})();
})();
</script>
"""


def revised_why(it):
    """v1.4 뜻이 바뀐 마지막 고침의 까닭 (갈래 이름만 바꾼 것은 뺌) — 문서·평가판에 '다시 짬'."""
    for r in reversed(it.get("revised") or []):
        if set(r.get("old") or {}) - {"data_kind", "theme", "persona", "needs", "market"}:
            return f"{r['at']} — {r['why']}"
    return ""


def render_page(S, A):
    """평가판 HTML — 이번 묶음 20개 (점수 순). 저장된 평가(평가.txt)를 처음 값으로 넣고, 페이지에서 누른 것은 db 'marks' 에."""
    B = current_batch(S)
    items = []
    if B:
        rows = sorted((S["items"][t] for t in B["ids"]), key=lambda it: -it["score"])
        for i, it in enumerate(rows, 1):
            pp = A["personas"].get(it["persona"], {})
            needs = [A["needs"][n] for n in it.get("needs") or [] if n in A["needs"]]
            basis = " · ".join([f"{n['pick']} {n['topic'][:40]} 👍{n['likes']:,}" for n in needs] +
                               ([f"닮은 성공 사례: {it['success_match']['title'][:50]}"] if it.get("success_match") and it["success_match"]["sim"] >= 0.08 else []))
            pc = it.get("precheck") or {}
            items.append({"rank": i, "id": it["id"], "title": (f"[{'⛔ ' if pc.get('out') else ''}{pc['class']}] " if pc else "") + it["title"],
                          "conclusion": pc.get("conclusion") or it["conclusion"], "question": it["question"], "decide": it["decide"],
                          "data": it["data"], "format": it["format"], "persona": f"{pp.get('id', '?')} {pp.get('name', it['persona'])}", "status": it["status"],
                          "score": f"{it['score']:.2f}", "basis": basis or it.get("why", ""), "rating": it.get("rating"), "why": it.get("rating_why", ""), "revised": revised_why(it)})
    data = {"batch": B["no"] if B else 0, "made": (B["made"][:10] if B else "-"), "analysis": str(A["analysis_made"])[:10], "items": items}
    js = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    return PAGE.replace("__NAME__", NAME).replace("__NOTE__", NOTE_PAGE).replace("__DATA__", js)


def main(argv=None):
    ap = argparse.ArgumentParser(description="주제 탐색 (주식·재테크) — 20개씩 · 평가를 배움 · 명확한 결론만")
    ap.add_argument("topic")
    ap.add_argument("cmd", choices=["material", "add", "mark", "use", "done", "status", "import", "precheck", "revise", "refresh"])
    ap.add_argument("args", nargs="*")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args(argv)
    logging.basicConfig(level=a.log_level, format="%(message)s", stream=sys.stdout)
    t0 = time.monotonic()
    log("START", topic=a.topic, cmd=a.cmd, tool=f"topic_ideas.py {VERSION}")
    if a.cmd == "material":
        cmd_material(a.topic)
    elif a.cmd == "add":
        cmd_add(a.topic, a.args[0])
    elif a.cmd == "mark":
        cmd_mark(a.topic, a.args[0], a.args[1], " ".join(a.args[2:]))
    elif a.cmd == "import":
        cmd_import(a.topic, a.args[0])
    elif a.cmd == "precheck":
        cmd_precheck(a.topic, a.args[0], a.args[1] if len(a.args) > 1 else None)
    elif a.cmd == "revise":
        cmd_revise(a.topic, a.args[0])
    elif a.cmd == "refresh":
        cmd_refresh(a.topic)
    elif a.cmd in ("use", "done"):
        cmd_use(a.topic, a.args[0], a.args[1] if len(a.args) > 1 else "", done=a.cmd == "done")
    else:
        cmd_status(a.topic)
    log("DONE", topic=a.topic, cmd=a.cmd, seconds=round(time.monotonic() - t0, 2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
