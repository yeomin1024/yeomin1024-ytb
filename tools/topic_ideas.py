#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.6.2 — 2026-10-29 — **카드에 영상 형식(문제형·테스트형)** (사용자 지시 2026-10-29 "1번 평가판은 사실형으로 하지 말고 문제나 테스트형으로 좀 해봐 왜 다 사실형이야"):
#          평가판 카드의 칩이 정답 미리 확인 분류(사실형 = 정답이 지난 실제 숫자)를 보여 줘 영상 형식으로 읽혔음 → 기획안 `form`(문제·테스트·비교 — 판 번호를 안 올리는 칸,
#          EXTRA_KEYS)을 카드 칩으로 · 분류는 평가판에서 빼고 영상기획안.md 에만. 영향: EXTRA_KEYS·lint_stage()·stage_update()·stage_page_item()·render_plans()·PAGE_STAGE.
# (v1.6.1 — 2026-10-29 — **이전에 좋음을 준 것은 1단계를 건너뜀** (사용자 지시 2026-10-29 "아니 내가 이전에 좋다고 한것들은 2번에 넣어야지 다시해봐"):
#          주제 평가(평가.txt — 예전 평가판 'marks')·기존 편 평가(기존편_평가.txt)가 좋음이고 1단계 평가가 아직 하나도 없으면 1단계 통과로 봄 (carried · 1단계 평가판에는 안 보이고
#          '건너뜀' 줄로만 · 2단계로) — 1단계를 직접 평가하면 그 평가가 이김. 영향: stage_status(carried)·stage_rows()·render_stage_page()·log_stages()·stage_cell()·selftest_stages()·PAGE_STAGE.)
# (v1.6 — 2026-10-29 — **단계 평가판 세 장** (사용자 지시 2026-10-29 "1번. 제목, 전달하고자 하는 내용 / 2번. 썸네일 문구, 보조문구, 대본 도입부(요약) /
#          3번. 대본 내용(요약) 각각 3가지 평가판을 만들어봐 그럼 평가할게 통과한건 2번부터 다시 만들면 돼 3번은 2번에서 통과된것만 만드는거야"):
#          기획안 칸을 세 단계로 (STAGE_KEYS 1 = title·message(전달하고자 하는 내용) · 2 = thumb_main·thumb_sub·intro · 3 = items·explain) · 단계마다 판 번호
#          (package v·base — 그 단계 칸이 바뀌면 +1, base = 만들 때의 앞 단계 판) · 앞 단계를 모두 좋음으로 통과하고 이 단계 내용을 그 판에 맞춰 만든 것만 그 단계 평가판에 ·
#          평가 = 단계평가.txt ('1단계 T043 v1 좋음 까닭' — 판마다) · `import-stage <단계> <marks>` (Artifact db 모음 s1·s2·s3) · 1단계 좋음은 평가.txt 에도 좋음 (주제 학습) ·
#          `package` 는 준 칸만 합침 (예전엔 통째로 바꿈) · 기존 편(EP_)도 같은 길 (판 번호는 재구성_안.json 에) · settings [stages] URLS 가 있으면 평가판 세 장
#          (평가판.html · 평가판_2단계.html · 평가판_3단계.html), 없으면 v1.5 평가판 그대로 (재테크·역사) · `selftest` = 단계 판정 시험.
#          영향: lint_stage()·lint_package()·stage_update()·pkg_ver()·stage_status()·read_stage_marks()·stage_rows()·read_docs()·cmd_package()·cmd_import()·cmd_import_stage()·
#          load_episodes()·render_stage_page()·render_plans()·finish()·selftest_stages()·main()·PAGE_STAGE.)
# (v1.5 — 2026-10-29 — **평가판 = 영상 기획안** (사용자 지시 2026-10-29 "저 평가판을 진짜 영상 만든다고 생각하고 제목, 썸네일 문구, 썸네일 보조 문구, 도입부,
#          내용만(항목 및 정답, 해설 내용 간단하게) 표시되도록 해봐 기존 3건(재무제표, 매수 시기, 포트폴리오)도 … 다시 구성해봐"): `package <기획안.json>`
#          ({"packages": {ID: {title, thumb_main[2], thumb_sub, intro[], items[{q,a}], explain[]}}} — 검사 lint_package) · 평가판 카드는 기획안만 (썸네일 모양 · 도입부 ·
#          항목과 정답 · 해설) · settings [page] EPISODES = 기존 편 폴더 → <편>/재구성_안.json 을 '기존 편' 칸으로 (평가 문서 id EP_<편> → import 가 기존편_평가.txt 에) ·
#          기획안 모음 문서 영상기획안.md. 영향: lint_package()·cmd_package()·render_page()·render_plans()·cmd_import()·read_ep_marks()·finish()·main()·PAGE.)
# (v1.4.1 — 2026-10-29 — pick_batch: 주제 묶음·니즈 제한 때문에 20개를 못 채우면 제한을 풀고 점수 순으로 채움 (겹침 검사는 그대로 · 로그 WARNING) —
#          3회차 묶음이 14개로 끝나서 (좋음이 투자 심리·종목 고르기 묶음에 몰림). 사용자 지시 2026-10-29 "평가판 반영했으니 주제 다시 탐색하고 …".)
# (v1.4 — 2026-10-29 — 평가를 다 한 묶음 갈기·좋음 주제 다시 짜기 (사용자 지시 2026-10-29 "주식 주제 평가판 평가했는데 다시 주제 탐색해봐"):
#          `revise <고침.json>` = 주제 칸을 고침 ({ID: {칸: 새 값, "why": 까닭}} — 평가는 그대로 · 옛 값은 revised 에 · 미리 계산은 지워 다시 계산하게 · lint 통과만) ·
#          `refresh` = 지금 묶음을 모두 평가(또는 작성·뺌)했으면 새 묶음 — 좋음(미리 계산 통과)은 새 묶음에 이어 가고, 나머지 안 쓴 주제는 대기로 · 20개를 못 채우면 아무것도 안 바꿈 ·
#          data_kind 검사 (settings [fields] DATA_KINDS 가 있으면 그 안의 값만 — 주식: 사건 사례·종목 사례를 더함, 지수 전략 백테스트와 나눠 배우게).
#          문서·평가판에 '다시 짬'(뜻이 바뀐 마지막 고침의 까닭 — 좋음을 받은 뒤 다시 짠 주제를 다시 평가할 수 있게).
#          고침: v1.3 에서 평가판 안내 글 기본값(NOTE_PAGE)을 '[분류]' 글로 바꿔 재테크 평가판을 다시 만들면 주식 글이 찍히던 것 → 기본값 되돌리고 주식 settings [page] NOTE_PAGE 로.
#          영향: lint()·pick_batch(carry)·cmd_revise()·cmd_refresh()·revised_why()·render()·render_page()·main().)
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
  python3 tools/topic_ideas.py stock package <기획안.json> # v1.5 주제마다 영상 기획안(제목·썸네일 문구·보조·도입부·항목과 정답·해설) → 평가판 카드
                                                         #  v1.6 준 칸만 합치고, 바뀐 단계의 판 번호를 올림 ({ID: {칸: 값, "why": 까닭}} · ID 는 T… 또는 EP_<편>)
  python3 tools/topic_ideas.py stock import-stage 1 <marks.json>   # v1.6 단계 평가판(db 모음 s1·s2·s3)에서 누른 평가 → 단계평가.txt
  python3 tools/topic_ideas.py stock selftest            # v1.6 단계 판정 시험 (파일을 안 건드림)
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

VERSION = "v1.6.2"
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
    filled = 0
    if len(chosen) < cfg["SIZE"]:                   # v1.4.1 주제 묶음·니즈 제한 때문에 못 채우면 — 제한을 풀고 점수 순 (같은 묶음 안 겹침 검사는 그대로)
        for it in pool:
            if len(chosen) >= cfg["SIZE"]:
                break
            tk, bg = toks(ctext(it)), bigrams(ctext(it))
            if it not in chosen and all(jacc(tk, toks(ctext(c))) < Z["dedupe"]["SIM_MAX_BATCH"] and overlap(bg, bigrams(ctext(c))) < Z["dedupe"]["OVERLAP_MAX_BATCH"] for c in chosen):
                take(it, "점수 순 (주제 묶음·니즈 제한을 풀어 채움)")
                filled += 1
        if filled:
            log("BATCH", logging.WARNING, note=f"제한 안에서 {len(chosen) - filled}개뿐 — 제한을 풀어 {filled}개 더 채움", limits=f"MAX_PER_THEME={cfg['MAX_PER_THEME']} MAX_PER_NEED={cfg['MAX_PER_NEED']}")
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
    P_PAGE[0], Z_PAGE[0] = P, Z
    if Z.get("stages"):                             # v1.6 단계 평가판 세 장 (settings [stages])
        rows = stage_rows(S, P, Z)
        for n, name in STAGE_PAGES.items():
            (P["dir"] / name).write_text(render_stage_page(S, P, Z, n, rows), "utf-8")
        log_stages(rows)
    else:
        P["page"].write_text(render_page(S, A), "utf-8")
    (P["md"].parent / "영상기획안.md").write_text(render_plans(S, P, Z), "utf-8")
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


PKG_KEYS = ("title", "thumb_main", "thumb_sub", "intro", "items", "explain")
# v1.6 단계 — 1 제목·전달하고자 하는 내용 → 2 썸네일 문구·보조 문구·도입부(요약) → 3 대본 내용(요약: 항목과 정답·해설)
STAGE_KEYS = {1: ("title", "message"), 2: ("thumb_main", "thumb_sub", "intro"), 3: ("items", "explain")}
STAGE_NAME = {1: "제목 · 전달하고자 하는 내용", 2: "썸네일 문구 · 보조 문구 · 도입부", 3: "대본 내용"}
# v1.6.2 판 번호를 안 올리는 칸 — form = 영상 형식 (채널 설명 stock/guides/channel.md: 문제 '내 실력은' · 테스트 '나는 어떨까' · 비교 시뮬레이션)
EXTRA_KEYS = ("form",)
FORMS = {"문제": "문제형", "테스트": "테스트형", "비교": "비교형"}


def lint_stage(pk, s):
    """v1.6 한 단계 칸 검사 (문제 목록, 없으면 통과)."""
    bad = [f"'{k}' 칸 없음" for k in STAGE_KEYS[s] if not pk.get(k)]
    if bad:
        return bad
    if s == 1:
        if len(pk["title"]) > 60:
            bad.append(f"제목 {len(pk['title'])}자 > 60")
        msg = pk["message"]
        if not (isinstance(msg, list) and 1 <= len(msg) <= 3 and all(isinstance(x, str) and x.strip() for x in msg)):
            bad.append("전달하고자 하는 내용은 1~3문장 (목록)")
        elif sum(len(x) for x in msg) > 240:
            bad.append(f"전달하고자 하는 내용 {sum(len(x) for x in msg)}자 > 240")
    elif s == 2:
        if not (isinstance(pk["thumb_main"], list) and len(pk["thumb_main"]) == 2 and all(pk["thumb_main"])):
            bad.append("썸네일 문구는 2줄 (목록 2개)")
        elif max(len(x) for x in pk["thumb_main"]) > 14:
            bad.append("썸네일 문구 한 줄이 14자 넘음")
        if len(pk["thumb_sub"]) > 16:
            bad.append(f"보조 문구 {len(pk['thumb_sub'])}자 > 16")
        if not 2 <= len(pk["intro"]) <= 6:
            bad.append(f"도입부 {len(pk['intro'])}문장 (2~6)")
    else:
        if not 3 <= len(pk["items"]) <= 6 or not all(x.get("q") and x.get("a") for x in pk["items"]):
            bad.append("항목 3~6개 · 항목마다 q(질문)·a(정답)")
        if not 1 <= len(pk["explain"]) <= 3:
            bad.append("해설 1~3문장")
    return bad


def lint_package(pk):
    """v1.5 영상 기획안 검사 — 칸이 다 있고 길이가 맞는지 (문제 목록, 없으면 통과). v1.6: 단계 검사(2·3)를 그대로 씀 · 전달 내용은 묻지 않음."""
    bad = [f"'{k}' 칸 없음" for k in PKG_KEYS if not pk.get(k)]
    if bad:
        return bad
    if len(pk["title"]) > 60:
        bad.append(f"제목 {len(pk['title'])}자 > 60")
    return bad + lint_stage(pk, 2) + lint_stage(pk, 3)


def pkg_ver(pk):
    """v1.6 단계마다 판 번호 (0 = 이 단계 내용을 아직 안 만듦 · 예전 기획안의 칸은 초안) · base = 만들 때의 앞 단계 판."""
    v, b = (pk or {}).get("v") or {}, (pk or {}).get("base") or {}
    return {s: int(v.get(str(s), 0)) for s in (1, 2, 3)}, {s: int(b.get(str(s), 0)) for s in (2, 3)}


def lint_extra(pk):
    """v1.6.2 판 번호를 안 올리는 칸 검사."""
    return [f"form '{pk['form']}' — {'·'.join(FORMS)} 중 하나"] if "form" in pk and pk["form"] not in FORMS else []


def stage_update(pk, entry, why="", at=None):
    """v1.6 준 칸만 합침 → (새 기획안, 바뀐 단계 목록, 문제). 한 단계라도 검사를 못 넘으면 아무것도 안 바꿈.
    그 단계 칸이 바뀌었거나 아직 판이 0 이면 판 +1 · base[s] = 앞 단계의 (새) 판 · 옛 값은 history 에."""
    at = at or datetime.now(timezone.utc).strftime("%Y-%m-%d")
    pk = dict(pk or {})
    v, b = pkg_ver(pk)
    hist, changed = list(pk.get("history") or []), []
    for s in (1, 2, 3):
        keys = [k for k in STAGE_KEYS[s] if k in entry]
        if not keys:
            continue
        new = {**pk, **{k: entry[k] for k in keys}}
        probs = lint_stage(new, s)
        if probs:
            return None, [], [f"{s}단계: {x}" for x in probs]
        if any(pk.get(k) != entry[k] for k in keys) or v[s] == 0:
            v[s] += 1
            if s >= 2:
                b[s] = v[s - 1]
            hist.append({"stage": s, "v": v[s], "at": at, "why": why, "old": {k: pk[k] for k in keys if k in pk and pk[k] != entry[k]}})
            changed.append(s)
        pk = new
    ex = {k: entry[k] for k in EXTRA_KEYS if k in entry}       # v1.6.2 형식 — 판 번호는 그대로 (내용이 아니라 꼬리표)
    if ex:
        probs = lint_extra({**pk, **ex})
        if probs:
            return None, [], probs
        old = {k: pk[k] for k in ex if k in pk and pk[k] != ex[k]}
        if old or any(k not in pk for k in ex):
            hist.append({"stage": 0, "v": 0, "at": at, "why": why, "old": old, "set": ex})
        pk.update(ex)
    pk["v"], pk["base"], pk["history"] = {str(s): v[s] for s in v}, {str(s): b[s] for s in b}, hist
    return pk, changed, []


def stage_marks_path(P):
    return P["dir"] / "단계평가.txt"


STAGE_MARKS_HEAD = """# 단계 평가 — 줄마다 '<단계>단계 <ID> v<판> 좋음|나쁨 까닭(선택)'. 예: 1단계 T043 v1 좋음 / 2단계 EP_timing-test-2026-10 v1 나쁨 도입이 길다
# 평가판 세 장(1단계 제목·전달 내용 → 2단계 썸네일 문구·보조 문구·도입부 → 3단계 대본 내용)에서 누른 것을 Claude 가 import-stage 로 옮김 — 채팅으로 말해도 됨.
# 같은 단계·ID·판은 마지막 줄이 이김 · 좋음 = 다음 단계로 · 나쁨 = 그 단계 내용만 까닭을 반영해 새 판(v+1)으로 (tools/topic_ideas.py v1.6).
"""


def read_stage_marks(P):
    """v1.6 단계평가.txt → {(단계, ID): {판: {rating, why, note}}} (같은 단계·ID·판은 마지막 줄이 이김 · '지움' 은 그 판 평가를 지움)."""
    out = defaultdict(dict)
    f = stage_marks_path(P)
    if f.is_file():
        for ln in f.read_text("utf-8").splitlines():
            m = re.match(r"^([123])단계\s+(\S+)\s+v(\d+)\s+(좋음|나쁨|지움)\s*(.*?)(?:\s+#\s*(.*))?$", ln.strip())
            if not m:
                continue
            key, ver = (int(m.group(1)), m.group(2)), int(m.group(3))
            if m.group(4) == "지움":
                out[key].pop(ver, None)
            else:
                out[key][ver] = {"rating": m.group(4), "why": m.group(5).strip(), "note": (m.group(6) or "").strip()}
    return out


def stage_status(pk, sm, iid, carried=None):
    """v1.6 단계마다 {v, ready(이 판 내용이 지금 앞 단계 판에 맞춰 있음), open(앞 단계를 모두 좋음 + ready → 이 단계 평가판에), rating·why(이 판 평가),
    prev(앞 판의 마지막 평가), todo('만들 차례'·'다시 만들 차례'·None), carried}. 앞 단계 판이 바뀌면 base 가 어긋나 ready=False (= 다시 만들 차례).
    v1.6.1 carried = {"why": …} (이전 주제 평가 좋음) — 1단계 평가가 한 판도 없으면 1단계 좋음으로 봄 (직접 평가가 있으면 그것이 이김)."""
    v, b = pkg_ver(pk)
    out, passed = {}, True
    for s in (1, 2, 3):
        ready = v[s] >= 1 and (s == 1 or b[s] == v[s - 1])
        m = sm.get((s, iid), {})
        cur = m.get(v[s]) if ready else None
        carry = s == 1 and ready and carried is not None and not m
        if carry:
            cur = {"rating": "좋음", "why": carried.get("why", "")}
        pv = max((k for k in m if k < v[s] or not ready), default=None)
        todo = None
        if passed and not ready:
            todo = "만들 차례"
        elif passed and cur and cur["rating"] == "나쁨":
            todo = "다시 만들 차례"
        out[s] = {"v": v[s], "ready": ready, "open": passed and ready, "rating": cur["rating"] if cur else None, "why": cur["why"] if cur else "",
                  "prev": ({"v": pv, "rating": m[pv]["rating"], "why": m[pv]["why"]} if pv is not None else None), "todo": todo, "carried": carry}
        passed = passed and ready and bool(cur) and cur["rating"] == "좋음"
    return out


def last_fix(pk, s):
    """v1.6 이 단계 지금 판을 만든 까닭 (판 2 이상일 때만 — 첫 판은 빈칸)."""
    v, _ = pkg_ver(pk)
    for h in reversed((pk or {}).get("history") or []):
        if h.get("stage") == s and h.get("v") == v[s] and v[s] >= 2:
            return h.get("why", "")
    return ""


def ep_file(P, ep):
    return P["base"] / "source" / ep / "재구성_안.json"     # P["base"] = <주제>/


def cmd_package(topic, path, root=None):
    """v1.5 영상 기획안 넣기 — {"packages": {ID: {...}}} · 평가는 그대로.
    v1.6: 준 칸만 합침 (stage_update — 바뀐 단계의 판 +1 · 검사를 못 넘으면 그 ID 는 안 바꿈) · ID 가 EP_<편> 이면 <편>/재구성_안.json 에."""
    P = paths(topic, root)
    Z, S, A = load_settings(P), load_state(P, topic), load_analysis(P)
    pk = json.loads(Path(path).read_text("utf-8"))
    pk = pk.get("packages", pk)
    ok_n = 0
    for tid, v in pk.items():
        why = v.get("why", "")
        if tid.startswith("EP_"):
            f = ep_file(P, tid[3:])
            if not f.is_file():
                log("CHECK", logging.WARNING, id=tid, result="없는 기존 편", file=str(f))
                continue
            d = json.loads(f.read_text("utf-8"))
            new, changed, probs = stage_update(d, v, why)
            if probs:
                log("CHECK", logging.WARNING, id=tid, result="기획안 안 넣음", why="; ".join(probs))
                continue
            f.write_text(json.dumps(new, ensure_ascii=False, indent=1) + "\n", "utf-8")
        else:
            if tid not in S["items"]:
                log("CHECK", logging.WARNING, id=tid, result="없는 주제")
                continue
            new, changed, probs = stage_update(S["items"][tid].get("package"), v, why)
            if probs:
                log("CHECK", logging.WARNING, id=tid, result="기획안 안 넣음", why="; ".join(probs))
                continue
            new.update({"file": str(path), "made": datetime.now(timezone.utc).strftime("%Y-%m-%d")})
            S["items"][tid]["package"] = new
        ok_n += 1
        vv, bb = pkg_ver(new)
        log("CHECK", id=tid, result="기획안", title=new.get("title", "")[:40], stages_changed=",".join(map(str, changed)) or "-",
            v=f"{vv[1]}/{vv[2]}/{vv[3]}", base=f"{bb[2]}/{bb[3]}", why=why[:60] or "-")
    log("CHECK", topic=topic, packages=ok_n, asked=len(pk))
    save_state(P, S)
    return finish(topic, P, Z, S, A)


def ep_marks_path(P):
    return P["md"].parent / "기존편_평가.txt"            # <주제>/topics/


def read_ep_marks(P):
    """v1.5 기존 편 기획안 평가 — 'EP_<편> 좋음|나쁨 까닭' (마지막 줄이 이김)."""
    out = {}
    f = ep_marks_path(P)
    if f.is_file():
        for ln in f.read_text("utf-8").splitlines():
            m = re.match(r"^(EP_\S+)\s+(좋음|나쁨|지움)\s*(.*?)(\s+#.*)?$", ln.strip())
            if m:
                if m.group(2) == "지움":
                    out.pop(m.group(1), None)
                else:
                    out[m.group(1)] = {"rating": m.group(2), "why": m.group(3).strip()}
    return out


def load_episodes(P, Z):
    """settings [page] EPISODES — <주제>/source/<편>/재구성_안.json (없으면 건너뜀). v1.6: full = 파일 전체 (전달 내용·판 번호)."""
    eps, em = [], read_ep_marks(P)
    for ep in (Z.get("page") or {}).get("EPISODES") or []:
        f = ep_file(P, ep)
        if not f.is_file():
            log("LOAD", logging.WARNING, episode=ep, note="재구성_안.json 없음")
            continue
        d = json.loads(f.read_text("utf-8"))
        probs = lint_package(d)
        if probs:
            log("CHECK", logging.WARNING, episode=ep, why="; ".join(probs))
            continue
        eid = "EP_" + ep
        eps.append({"id": eid, "label": d.get("label", ep), "pkg": {k: d[k] for k in PKG_KEYS}, "changed": d.get("changed", ""), "full": d,
                    "rating": em.get(eid, {}).get("rating"), "why": em.get(eid, {}).get("why", "")})
    return eps


def read_docs(path):
    """평가판 db 모음을 ArtifactData list 로 받은 결과 → 문서 목록 [{id, data}] (폴더 · JSON · 한 줄에 문서 하나인 글 모두)."""
    src = Path(path)
    docs = []
    if src.is_dir():                                   # ArtifactData list … out_dir= → <dir>/<모음>/<id>.json
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
    out = []
    for d in docs:
        body = d.get("data") if isinstance(d.get("data"), dict) else d
        out.append((str(d.get("id") or d.get("doc_id") or str(d.get("path", "")).split("/")[-1]), body))
    return out


def cmd_import(topic, path, root=None):
    """평가판(Artifact db 'marks' 모음) → 평가.txt. Claude 가 ArtifactData list 결과를 파일로 저장해 넘김.
    문서마다 id(=T003)·rating(좋음|나쁨|빈칸=지움)·why·at. 지금 평가와 다른 것만 한 줄씩 더함 (빈칸 = '지움' 줄)."""
    P = paths(topic, root)
    cur = read_marks(P)
    S = load_state(P, topic)
    lines, seen, ep_lines = [], 0, []
    for tid, body in read_docs(path):
        if tid.startswith("EP_"):                      # v1.5 기존 편 기획안 평가 → 기존편_평가.txt
            r = str(body.get("rating") or "")
            why = re.sub(r"\s+", " ", str(body.get("why") or "")).strip()[:120]
            cur_ep = read_ep_marks(P)
            if r in ("좋음", "나쁨") and (cur_ep.get(tid, {}).get("rating") != r or cur_ep.get(tid, {}).get("why", "") != why):
                ep_lines.append(f"{tid} {r} {why}".rstrip() + f"  # 평가판 {str(body.get('at') or '')[:16]}")
            elif not r and tid in cur_ep:
                ep_lines.append(f"{tid} 지움  # 평가판 {str(body.get('at') or '')[:16]}")
            continue
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
    if ep_lines:
        f = ep_marks_path(P)
        new = not f.is_file()
        with open(f, "a", encoding="utf-8") as fh:
            if new:
                fh.write("# 기존 편 다시 짠 안(평가판 '기존 편' 칸) 평가 — 'EP_<편> 좋음|나쁨 까닭' · 같은 편은 마지막 줄이 이김 (topic_ideas.py v1.5)\n")
            fh.write("\n".join(ep_lines) + "\n")
    log("LEARN", topic=topic, source=str(path), page_docs=seen, new_lines=len(lines), episode_lines=len(ep_lines))
    return cmd_status(topic, root)


def stage_rows(S, P, Z):
    """v1.6 이번 묶음(점수 순) + 기존 편 — 단계 상태와 함께 (단계 평가판·영상기획안·로그가 같이 씀)."""
    sm = read_stage_marks(P)
    B = current_batch(S)
    rows = []
    if B:
        for i, it in enumerate(sorted((S["items"][t] for t in B["ids"]), key=lambda it: -it["score"]), 1):
            pk = it.get("package") or {}
            rows.append({"id": it["id"], "rank": i, "kind": "topic", "label": it["id"], "pkg": pk, "cls": (it.get("precheck") or {}).get("class", ""),
                         "carried": (it.get("picked_why") or "").startswith("좋음"), "status": it["status"],
                         "st": stage_status(pk, sm, it["id"], {"why": it.get("rating_why", "")} if it.get("rating") == "좋음" else None)})
    for e in load_episodes(P, Z):                   # v1.6.1 기존 편: 기존편_평가.txt 좋음 → 1단계 건너뜀
        rows.append({"id": e["id"], "rank": None, "kind": "episode", "label": e["label"], "pkg": e["full"], "cls": "", "carried": False,
                     "status": "", "st": stage_status(e["full"], sm, e["id"], {"why": e["why"]} if e["rating"] == "좋음" else None)})
    return rows


def cmd_import_stage(topic, n, path, root=None):
    """v1.6 단계 평가판(db 모음 s1·s2·s3) → 단계평가.txt. 문서마다 id·rating·why·v(평가한 판)·at. 지금 기록과 다른 것만 한 줄씩 (빈칸 = '지움').
    1단계 좋음(T…)은 평가.txt 에도 좋음 (주제 학습 — 이미 좋음이면 안 씀). 나쁨은 옮기지 않음 — 제목·전달 내용을 다시 만들 차례라서
    (까닭이 주제 자체가 나쁘다는 뜻이면 Claude 가 `mark T… 나쁨`)."""
    P = paths(topic, root)
    Z, S = load_settings(P), load_state(P, topic)
    n = int(n)
    sm = read_stage_marks(P)
    rows = {r["id"]: r for r in stage_rows(S, P, Z)}
    lines, good_topics, seen, skipped = [], [], 0, 0
    for iid, body in read_docs(path):
        if iid not in rows:
            skipped += 1
            log("LEARN", logging.WARNING, step=n, id=iid, note="이번 묶음·기존 편에 없음 — 건너뜀")
            continue
        try:
            v = int(body.get("v") or 0)
        except (TypeError, ValueError):
            v = 0
        if v < 1:
            skipped += 1
            log("LEARN", logging.WARNING, step=n, id=iid, note="판 번호(v) 없음 — 건너뜀")
            continue
        seen += 1
        r = str(body.get("rating") or "")
        why = re.sub(r"\s+", " ", str(body.get("why") or "")).strip()[:120]
        at = str(body.get("at") or "")[:16]
        cur = sm.get((n, iid), {}).get(v)
        if r in ("좋음", "나쁨") and (not cur or cur["rating"] != r or cur["why"] != why):
            lines.append(f"{n}단계 {iid} v{v} {r} {why}".rstrip() + f"  # 평가판 {at}")
        elif not r and cur:
            lines.append(f"{n}단계 {iid} v{v} 지움  # 평가판 {at}")
        if v != rows[iid]["st"][n]["v"]:
            log("LEARN", logging.WARNING, step=n, id=iid, rated_v=v, now_v=rows[iid]["st"][n]["v"], note="앞 판 평가 — 기록만 (지금 판의 통과는 아님)")
        if n == 1 and r == "좋음" and iid.startswith("T") and v == rows[iid]["st"][1]["v"]:
            good_topics.append((iid, why))
    f = stage_marks_path(P)
    if lines:
        new = not f.is_file()
        with open(f, "a", encoding="utf-8") as fh:
            if new:
                fh.write(STAGE_MARKS_HEAD)
            fh.write("\n".join(lines) + "\n")
    marks = read_marks(P)
    tl = [f"{t} 좋음 1단계 통과{(' — ' + w) if w else ''}  # 단계 평가판" for t, w in good_topics if marks.get(t, {}).get("rating") != "좋음"]
    if tl:
        new = not P["marks"].is_file()
        with open(P["marks"], "a", encoding="utf-8") as fh:
            if new:
                fh.write(MARKS_HEAD.replace("__NAME__", NAME))
            fh.write("\n".join(tl) + "\n")
    log("LEARN", topic=topic, step=n, source=str(path), docs=seen, skipped=skipped, new_lines=len(lines), topic_good_lines=len(tl))
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
/* v1.5 영상 기획안 카드 — 썸네일 모양(문구 2줄 + 보조 말풍선) · 도입부 · 항목과 정답 · 해설 */
.thumb{position:relative;aspect-ratio:16/9;max-width:420px;width:100%;border-radius:8px;background:#0f141a;color:#fff;display:flex;flex-direction:column;justify-content:flex-end;padding:12px 14px;box-sizing:border-box;overflow:hidden}
.thumb .l1,.thumb .l2{font-weight:700;line-height:1.15;font-size:clamp(1.15rem,5vw,1.7rem);letter-spacing:-.02em;overflow-wrap:anywhere}
.thumb .l2{color:#ffd54a}
.thumb .bub{position:absolute;top:10px;right:10px;max-width:60%;background:#fff;color:#111;border-radius:12px;padding:2px 10px;font-size:.82rem;font-weight:500}
.thumb .tag{position:absolute;top:10px;left:12px;font-size:.7rem;color:#9fb0c0;letter-spacing:.05em}
.lab{font-size:.75rem;letter-spacing:.04em;color:var(--muted);margin:2px 0 0}
.intro{margin:0;font-size:.95rem}
.qa{list-style:decimal;padding-left:1.4em;margin:0;display:grid;gap:6px}
.qa li{padding-left:2px}
.qa .q{display:block}
.qa .a{display:block;color:var(--good);font-weight:500}
.qa .a::before{content:"정답 · ";color:var(--muted);font-weight:400}
.exp{margin:0;font-size:.92rem;border-left:3px solid var(--accent);padding-left:10px}
h2.sec{font-size:1.15rem;margin:18px 0 0}
.chg{font-size:.82rem;color:var(--muted);margin:0}
button:disabled,input:disabled{opacity:.55;cursor:not-allowed}
</style>
<div class="wrap">
<header>
<h1>__NAME__ 주제 평가판</h1>
<p class="sub" id="sub"></p>
<p class="note">주제마다 실제 영상처럼 제목 · 썸네일 문구 · 보조 문구 · 도입부 · 내용(항목과 정답 · 해설)만 보입니다. 좋음·나쁨을 누르면 저장되고, 다시 누르면 지워집니다. 까닭은 짧게 (선택). Claude 가 다음에 이 평가를 읽어 배우고, 다음 20개를 고를 때 좋은 쪽으로 뽑습니다. __NOTE__</p>
<p class="note warn" id="offline" hidden>이 화면에서는 저장할 수 없습니다 (로그인이 필요하거나 보기 전용). 평가는 Claude 에게 'T003 좋아, T007 별로'처럼 말하면 됩니다.</p>
<div class="bar"><span class="count" id="count"></span>
<div class="filt" role="group" aria-label="거르기"><button type="button" data-f="all" aria-pressed="true">전체</button><button type="button" data-f="none" aria-pressed="false">평가 안 함</button><button type="button" data-f="good" aria-pressed="false">좋음</button><button type="button" data-f="bad" aria-pressed="false">나쁨</button></div></div>
</header>
<ol id="list"></ol>
<section id="epsec" hidden><h2 class="sec">기존 3편 — 리스크를 줄이며 안정적으로 번 쪽을 정답으로 다시 짠 안</h2><ol id="eps"></ol></section>
</div>
<script id="data" type="application/json">__DATA__</script>
<script>
(function(){
const D=JSON.parse(document.getElementById("data").textContent);
const marks={};            // id -> {rating, why}  (저장소 값 — 처음엔 저장소의 평가.txt 값)
D.items.forEach(it=>{ if(it.rating) marks[it.id]={rating:it.rating,why:it.why||""}; });
(D.episodes||[]).forEach(it=>{ if(it.rating) marks[it.id]={rating:it.rating,why:it.why||""}; });
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
    meta.append(el("span",{class:"rank"},it.rank+"위"),el("span",{class:"id"},it.id));
    if(!it.pkg){ meta.append(el("span",{class:"chip"},it.format),el("span",{class:"chip"},it.persona)); }
    if(it.carried) meta.append(el("span",{class:"chip"},"앞 묶음 좋음"));
    if(it.status!=="이번 묶음") meta.append(el("span",{class:"chip"},it.status));
    if(it.pkg){ plan(li, it.pkg); }
    else{
    li.append(el("h2",{},it.title));
    const c=el("p",{class:"concl"}); c.append(el("span",{},/^\[/.test(it.title)?"결론(계산)":"결론(예상)")); c.append(document.createTextNode(it.conclusion)); li.append(c);
    const d=el("details"); d.append(el("summary",{},"질문 · 판정 규칙 · 자료 · 근거"));
    const dl=el("dl"); [["다시 짬",it.revised],["질문",it.question],["판정 규칙",it.decide],["자료",it.data],["근거",it.basis],["점수",it.score]].forEach(([k,v])=>{if(v){dl.append(el("dt",{},k),el("dd",{},String(v)));}});
    d.append(dl); li.append(d);
    }
    li.append(actions(it.id, r, m)); L.append(li);
  });
  const E=$("#eps"); E.innerHTML=""; const eps=D.episodes||[];
  $("#epsec").hidden=!eps.length;
  eps.forEach(ep=>{
    const m=marks[ep.id]||{}; const r=m.rating||"";
    const li=el("li",{class:"card"+(r==="좋음"?" good":r==="나쁨"?" bad":""),id:"c-"+ep.id});
    const meta=el("div",{class:"meta"}); meta.append(el("span",{class:"id"},ep.label)); li.append(meta);
    plan(li, ep.pkg);
    if(ep.changed) li.append(el("p",{class:"chg"},"바뀐 것 · "+ep.changed));
    li.append(actions(ep.id, r, m)); E.append(li);
  });
  counts();
}
function plan(li, p){
  li.append(el("h2",{},p.title));
  const t=el("div",{class:"thumb",role:"img","aria-label":"썸네일 문구 "+p.thumb_main.join(" ")+" · 보조 "+p.thumb_sub});
  t.append(el("span",{class:"tag"},"썸네일"), el("span",{class:"bub"},p.thumb_sub), el("span",{class:"l1"},p.thumb_main[0]), el("span",{class:"l2"},p.thumb_main[1]));
  li.append(t);
  li.append(el("p",{class:"lab"},"도입부"), el("p",{class:"intro"},p.intro.join(" ")));
  li.append(el("p",{class:"lab"},"내용 — 항목과 정답"));
  const ol=el("ol",{class:"qa"}); p.items.forEach(x=>{const q=el("li"); q.append(el("span",{class:"q"},x.q), el("span",{class:"a"},x.a)); ol.append(q);}); li.append(ol);
  const e=el("p",{class:"exp"}); e.append(el("span",{class:"lab"},"해설  ")); e.append(document.createTextNode(p.explain.join(" "))); li.append(e);
}
function actions(id, r, m){
    const act=el("div",{class:"act"});
    const it={id:id};
    const gb=el("button",{type:"button",class:"g","aria-pressed":String(r==="좋음"),id:"g-"+it.id},"좋음");
    const bb=el("button",{type:"button",class:"b","aria-pressed":String(r==="나쁨"),id:"b-"+it.id},"나쁨");
    const why=el("input",{type:"text",id:"w-"+it.id,placeholder:"까닭 (선택)",maxlength:"120","aria-label":it.id+" 까닭"}); why.value=m.why||"";
    const st=el("span",{class:"state",id:"s-"+it.id});
    [gb,bb,why].forEach(x=>{ if(!canWrite) x.disabled=true; });
    gb.addEventListener("click",()=>save(it.id, r==="좋음"?"":"좋음", why.value));
    bb.addEventListener("click",()=>save(it.id, r==="나쁨"?"":"나쁨", why.value));
    why.addEventListener("change",()=>{ if(marks[it.id]&&marks[it.id].rating) save(it.id, marks[it.id].rating, why.value); });
    act.append(gb,bb,why,st);
    return act;
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


PAGE_STAGE = r"""<title>__NAME__ 영상 __STAGE__단계 평가판</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@400;500;700&family=IBM+Plex+Mono:wght@500&display=swap">
<style>
/* v1.6 단계 평가판 — 위 단계 표시(1·2·3) · 카드 = 이 단계 칸만 (앞 단계 칸은 회색 맥락) · 좋음 = 다음 단계로 */
:root{--bg:#f3f5f7;--card:#ffffff;--ink:#17202b;--muted:#5b6876;--line:#d9dfe6;--accent:#1f5f8b;--good:#167a5b;--goodbg:#e3f3ec;--bad:#b4442f;--badbg:#f8e6e1;--well:#eef1f4;
--sans:"IBM Plex Sans KR","Apple SD Gothic Neo","Malgun Gothic",system-ui,sans-serif;--mono:"IBM Plex Mono",ui-monospace,Menlo,monospace}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#11161c;--card:#19212a;--ink:#e6ebf0;--muted:#9aa7b4;--line:#2b3641;--accent:#7cb4dc;--good:#5cc79f;--goodbg:#173229;--bad:#ef8c76;--badbg:#3a211b;--well:#141b22;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#11161c;--card:#19212a;--ink:#e6ebf0;--muted:#9aa7b4;--line:#2b3641;--accent:#7cb4dc;--good:#5cc79f;--goodbg:#173229;--bad:#ef8c76;--badbg:#3a211b;--well:#141b22;color-scheme:dark}
body{background:var(--bg);color:var(--ink);font-family:var(--sans);font-size:15px;line-height:1.55}
.wrap{max-width:780px;margin:0 auto;padding-block:20px 48px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));display:grid;gap:14px}
header{display:grid;gap:8px}
nav.steps{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:6px}
nav.steps>a,nav.steps>span{display:grid;gap:1px;align-content:start;padding:7px 10px;border:1px solid var(--line);border-radius:8px;background:var(--card);color:var(--ink);text-decoration:none;font-size:.8rem;line-height:1.3;min-width:0}
nav.steps .n{font-family:var(--mono);font-size:.72rem;color:var(--muted)}
nav.steps .t{overflow-wrap:anywhere}
nav.steps>[aria-current="page"]{border-color:var(--accent);box-shadow:inset 0 -3px 0 var(--accent)}
nav.steps>a:hover{border-color:var(--accent)}
h1{font-size:1.4rem;margin:4px 0 0;text-wrap:balance;letter-spacing:-.01em}
.sub{color:var(--muted);font-size:.9rem;margin:0;font-variant-numeric:tabular-nums}
.bar{display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.count{font-size:.85rem;color:var(--muted);font-variant-numeric:tabular-nums}
.count b{color:var(--ink);font-family:var(--mono)}
.filt{display:flex;gap:6px;flex-wrap:wrap;margin-left:auto}
.filt button{font:inherit;font-size:.85rem;border:1px solid var(--line);background:var(--card);color:var(--ink);border-radius:999px;padding:4px 12px;cursor:pointer}
.filt button[aria-pressed="true"]{background:var(--ink);color:var(--bg);border-color:var(--ink)}
.note{font-size:.85rem;color:var(--muted);border-left:3px solid var(--line);padding-left:10px;margin:0}
.note.warn{border-color:var(--bad);color:var(--ink)}
ol.list{list-style:none;margin:0;padding:0;display:grid;gap:12px}
.card{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px 16px;display:grid;gap:8px;min-width:0}
.card.good{border-color:var(--good);box-shadow:inset 4px 0 0 var(--good)}
.card.bad{border-color:var(--bad);box-shadow:inset 4px 0 0 var(--bad)}
.meta{display:flex;flex-wrap:wrap;gap:6px;align-items:center;font-size:.8rem;color:var(--muted)}
.rank{font-family:var(--mono);color:var(--ink)}
.id{font-family:var(--mono);color:var(--accent)}
.chip{border:1px solid var(--line);border-radius:4px;padding:0 6px}
.chip.v{font-family:var(--mono)}
.chip.form{border-color:var(--accent);color:var(--accent);font-weight:500}
h2{font-size:1.08rem;margin:0;text-wrap:balance}
.lab{font-size:.75rem;letter-spacing:.04em;color:var(--muted);margin:2px 0 0}
.msg{margin:0;font-size:.97rem}
.ctx{background:var(--well);border-radius:8px;padding:8px 11px;display:grid;gap:3px;font-size:.86rem;color:var(--muted);min-width:0}
.ctx b{color:var(--ink);font-weight:500}
.ctx p{margin:0}
.thumb{position:relative;aspect-ratio:16/9;max-width:420px;width:100%;border-radius:8px;background:#0f141a;color:#fff;display:flex;flex-direction:column;justify-content:flex-end;padding:12px 14px;box-sizing:border-box;overflow:hidden}
.thumb .l1,.thumb .l2{font-weight:700;line-height:1.15;font-size:clamp(1.15rem,5vw,1.7rem);letter-spacing:-.02em;overflow-wrap:anywhere}
.thumb .l2{color:#ffd54a}
.thumb .bub{position:absolute;top:10px;right:10px;max-width:60%;background:#fff;color:#111;border-radius:12px;padding:2px 10px;font-size:.82rem;font-weight:500}
.thumb .tag{position:absolute;top:10px;left:12px;font-size:.7rem;color:#9fb0c0;letter-spacing:.05em}
.intro{margin:0;font-size:.95rem}
.qa{list-style:decimal;padding-left:1.4em;margin:0;display:grid;gap:6px}
.qa .q{display:block}
.qa .a{display:block;color:var(--good);font-weight:500}
.qa .a::before{content:"정답 · ";color:var(--muted);font-weight:400}
.exp{margin:0;font-size:.92rem;border-left:3px solid var(--accent);padding-left:10px}
.hist{font-size:.82rem;color:var(--muted);margin:0}
.hist b{font-weight:500;color:var(--ink)}
.act{display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.act button{font:inherit;font-weight:500;border:1px solid var(--line);background:var(--card);color:var(--ink);border-radius:8px;padding:6px 14px;cursor:pointer;min-width:84px}
.act button.g[aria-pressed="true"]{background:var(--goodbg);border-color:var(--good);color:var(--good)}
.act button.b[aria-pressed="true"]{background:var(--badbg);border-color:var(--bad);color:var(--bad)}
.act input{flex:1 1 180px;min-width:0;font:inherit;font-size:.9rem;border:1px solid var(--line);border-radius:8px;padding:6px 10px;background:var(--bg);color:var(--ink)}
.state{font-size:.8rem;color:var(--muted);min-width:4em}
h2.sec{font-size:1.1rem;margin:14px 0 0}
.empty{background:var(--card);border:1px dashed var(--line);border-radius:10px;padding:22px 18px;display:grid;gap:8px}
.empty h2{font-size:1.1rem}
.empty p{margin:0;color:var(--muted)}
.empty a{color:var(--accent);font-weight:500}
.empty .steps{margin:0;padding-left:1.3em;color:var(--muted);font-size:.9rem;display:grid;gap:2px}
[hidden]{display:none!important}
button:disabled,input:disabled{opacity:.55;cursor:not-allowed}
button:focus-visible,input:focus-visible,a:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
</style>
<div class="wrap">
<header>
<nav class="steps" id="steps" aria-label="평가 단계"></nav>
<h1 id="h1"></h1>
<p class="sub" id="sub"></p>
<p class="note" id="how"></p>
<p class="note" id="skip" hidden></p>
<p class="note warn" id="offline" hidden></p>
<div class="bar" id="bar"><span class="count" id="count"></span>
<div class="filt" role="group" aria-label="거르기"><button type="button" data-f="all" aria-pressed="true">전체</button><button type="button" data-f="none" aria-pressed="false">평가 안 함</button><button type="button" data-f="good" aria-pressed="false">좋음</button><button type="button" data-f="bad" aria-pressed="false">나쁨</button></div></div>
</header>
<section id="emptysec" hidden></section>
<section id="topsec" hidden><h2 class="sec" id="toph"></h2><ol class="list" id="list"></ol></section>
<section id="epsec" hidden><h2 class="sec">기존 편 — 리스크를 줄이며 안정적으로 번 쪽을 정답으로 다시 짠 안</h2><ol class="list" id="eps"></ol></section>
</div>
<script id="data" type="application/json">__DATA__</script>
<script>
(function(){
const D=JSON.parse(document.getElementById("data").textContent);
const N=D.stage, COL="s"+N;
const ALL=D.items.concat(D.episodes);
const byId={}; ALL.forEach(it=>{byId[it.id]=it;});
const marks={}, prevs={};      // 이 판 평가 · 앞 판의 마지막 평가 (처음엔 저장소의 단계평가.txt 값)
ALL.forEach(it=>{ if(it.rating) marks[it.id]={rating:it.rating,why:it.why||""}; if(it.prev) prevs[it.id]=it.prev; });
let db=null, canWrite=false, filter="all";
const $=s=>document.querySelector(s);
function el(tag,attrs,text){const e=document.createElement(tag);for(const k in (attrs||{}))e.setAttribute(k,attrs[k]);if(text!=null)e.textContent=text;return e;}
// 위 단계 표시 — 지금 단계는 aria-current, 다른 단계는 주소가 있으면 링크
const steps=$("#steps");
[1,2,3].forEach(s=>{
  const u=D.urls[s-1]; const cur=s===N;
  const a=(cur||!u)?el("span",cur?{"aria-current":"page"}:{}):el("a",{href:u,target:"_blank",rel:"noopener"});
  a.append(el("span",{class:"n"},s+"단계"+(D.counts[s]!=null?" · "+D.counts[s]+"개":"")), el("span",{class:"t"},D.names[s]));
  steps.append(a);
});
$("#h1").textContent=`${D.name} 영상 ${N}단계 평가판`;
$("#sub").textContent = N===1 ? `${D.batch}번째 묶음 · ${D.made} · 새 주제 ${D.items.length}개`+(D.episodes.length?` + 기존 편 ${D.episodes.length}개`:"")+((D.skipped||[]).length?` · 건너뜀 ${D.skipped.length}개`:"")
  : `${N-1}단계 통과 ${D.passed_prev}개 · 이 단계에 올린 것 ${ALL.length}개${D.waiting?" · 만드는 중 "+D.waiting+"개":""} · ${D.made}`;
const HOW={1:"주제마다 제목과, 이 영상으로 전달하고자 하는 내용만 보입니다. 좋음 = 2단계(썸네일 문구 · 보조 문구 · 도입부)를 그 제목에 맞춰 다시 만들어 2단계 평가판에 올립니다. 나쁨 = 까닭을 반영해 제목 · 전달 내용을 다시 만들어 여기에 새 판(v2)으로 올립니다.",
 2:"1단계에서 좋음을 받은 주제만 — 회색 칸의 제목 · 전달 내용에 맞춘 썸네일 문구 · 보조 문구 · 대본 도입부(요약)입니다. 좋음 = 3단계(대본 내용)를 만들어 올립니다. 나쁨 = 이 단계 내용만 다시 만듭니다.",
 3:"2단계에서 좋음을 받은 주제만 — 대본 내용(요약: 항목과 정답 · 해설)입니다. 좋음 = 이 내용으로 대본을 씁니다. 나쁨 = 이 단계 내용만 다시 만듭니다."};
$("#how").textContent=HOW[N]+" 다시 누르면 지워집니다. 까닭은 짧게 (선택). "+D.note;
if(D.skipped&&D.skipped.length){ const k=$("#skip"); k.hidden=false; k.textContent=`이전 평가판에서 좋음을 준 ${D.skipped.length}개는 1단계를 건너뛰고 2단계로 갔습니다 — `+D.skipped.map(x=>x.label).join(" · ")+". 제목 · 전달 내용은 2단계 카드 위 회색 칸에 함께 보입니다."; }
function counts(){let g=0,b=0;ALL.forEach(it=>{const m=marks[it.id];if(m&&m.rating==="좋음")g++;else if(m&&m.rating==="나쁨")b++;});
  const c=$("#count"); c.textContent=""; c.append("좋음 ",el("b",{},String(g))," · 나쁨 ",el("b",{},String(b))," · 평가 안 함 ",el("b",{},String(ALL.length-g-b)));}
function emptyState(){
  const E=$("#emptysec"); E.hidden=false; E.textContent="";
  const box=el("div",{class:"empty"});
  box.append(el("h2",{},"아직 평가할 것이 없습니다"));
  box.append(el("p",{},`${N-1}단계에서 좋음을 받은 주제만 이 판에 올라옵니다.`+(D.waiting?` 지금 ${D.waiting}개가 통과해 Claude 가 이 단계 내용을 만드는 중입니다.`:` 지금 ${N-1}단계 통과는 ${D.passed_prev}개입니다.`)));
  const ol=el("ol",{class:"steps"});
  ol.append(el("li",{},`${N-1}단계 평가판에서 좋음 · 나쁨을 누릅니다.`), el("li",{},"Claude 에게 '평가했어'라고 말하면, 좋음을 받은 주제의 이 단계 내용을 만들어 여기에 올립니다."));
  box.append(ol);
  const u=D.urls[N-2]; if(u){ const a=el("a",{href:u,target:"_blank",rel:"noopener"},`${N-1}단계 평가판 열기`); const p=el("p"); p.append(a); box.append(p); }
  E.append(box); $("#bar").hidden=true;
}
function ctx(it){
  const c=el("div",{class:"ctx"});
  const t=el("p"); t.append(el("b",{},"제목 "), document.createTextNode(it.title)); c.append(t);
  const m=el("p"); m.append(el("b",{},"전달 내용 "), document.createTextNode(it.message.join(" "))); c.append(m);
  if(N===3){ const th=el("p"); th.append(el("b",{},"썸네일 "), document.createTextNode(it.thumb_main.join(" / ")+" · "+it.thumb_sub)); c.append(th); }
  return c;
}
function thumb(it){
  const t=el("div",{class:"thumb",role:"img","aria-label":"썸네일 문구 "+it.thumb_main.join(" ")+" · 보조 "+it.thumb_sub});
  t.append(el("span",{class:"tag"},"썸네일"), el("span",{class:"bub"},it.thumb_sub), el("span",{class:"l1"},it.thumb_main[0]), el("span",{class:"l2"},it.thumb_main[1]));
  return t;
}
function card(it){
  const m=marks[it.id]||{}; const r=m.rating||"";
  if(filter==="none"&&r) return null; if(filter==="good"&&r!=="좋음") return null; if(filter==="bad"&&r!=="나쁨") return null;
  const li=el("li",{class:"card"+(r==="좋음"?" good":r==="나쁨"?" bad":""),id:"c-"+it.id});
  const meta=el("div",{class:"meta"});
  if(it.rank) meta.append(el("span",{class:"rank"},it.rank+"위"));
  meta.append(el("span",{class:"id"},it.label), el("span",{class:"chip v"},"v"+it.v));
  if(it.form) meta.append(el("span",{class:"chip form"},it.form));
  if(it.carried) meta.append(el("span",{class:"chip"},"앞 묶음 좋음"));
  li.append(meta);
  if(N===1){ li.append(el("h2",{},it.title), el("p",{class:"lab"},"전달하고자 하는 내용"), el("p",{class:"msg"},it.message.join(" "))); }
  else li.append(ctx(it));
  if(N===2){ li.append(el("p",{class:"lab"},"썸네일 문구 · 보조 문구"), thumb(it), el("p",{class:"lab"},"대본 도입부 (요약)"), el("p",{class:"intro"},it.intro.join(" "))); }
  if(N===3){
    li.append(el("p",{class:"lab"},"대본 내용 (요약) — 항목과 정답"));
    const ol=el("ol",{class:"qa"}); it.items.forEach(x=>{const q=el("li"); q.append(el("span",{class:"q"},x.q), el("span",{class:"a"},x.a)); ol.append(q);}); li.append(ol);
    const e=el("p",{class:"exp"}); e.append(el("span",{class:"lab"},"해설  ")); e.append(document.createTextNode(it.explain.join(" "))); li.append(e);
  }
  const pv=prevs[it.id];
  if(pv){ const h=el("p",{class:"hist"}); h.append(el("b",{},`이전 판 v${pv.v} · ${pv.rating}`), document.createTextNode((pv.why?" — "+pv.why:"")+(it.fixed?` → 고친 것: ${it.fixed}`:""))); li.append(h); }
  else if(it.fixed){ li.append(el("p",{class:"hist"},"고친 것 · "+it.fixed)); }
  li.append(actions(it, r, m));
  return li;
}
function actions(it, r, m){
  const act=el("div",{class:"act"});
  const gb=el("button",{type:"button",class:"g","aria-pressed":String(r==="좋음")},"좋음");
  const bb=el("button",{type:"button",class:"b","aria-pressed":String(r==="나쁨")},"나쁨");
  const why=el("input",{type:"text",placeholder:"까닭 (선택)",maxlength:"120","aria-label":it.label+" 까닭"}); why.value=m.why||"";
  const st=el("span",{class:"state",id:"s-"+it.id});
  [gb,bb,why].forEach(x=>{ if(!canWrite) x.disabled=true; });
  gb.addEventListener("click",()=>save(it, r==="좋음"?"":"좋음", why.value));
  bb.addEventListener("click",()=>save(it, r==="나쁨"?"":"나쁨", why.value));
  why.addEventListener("change",()=>{ if(marks[it.id]&&marks[it.id].rating) save(it, marks[it.id].rating, why.value); });
  act.append(gb,bb,why,st);
  return act;
}
function render(){
  if(!ALL.length){ emptyState(); return; }
  const tops=D.items, eps=D.episodes;
  $("#topsec").hidden=!tops.length; $("#epsec").hidden=!eps.length;
  $("#toph").textContent = N===1 ? `새 주제 ${tops.length}개 (점수 순)` : `새 주제 ${tops.length}개`;
  const L=$("#list"); L.textContent=""; tops.forEach(it=>{const c=card(it); if(c) L.append(c);});
  const E=$("#eps"); E.textContent=""; eps.forEach(it=>{const c=card(it); if(c) E.append(c);});
  counts();
}
let busy=Promise.resolve();
function save(it,rating,why){
  if(!db||!canWrite) return;
  const st=document.getElementById("s-"+it.id); if(st) st.textContent="저장 중…";
  const body={rating:rating,why:(why||"").trim().slice(0,120),at:new Date().toISOString(),v:it.v,batch:D.batch};
  busy=busy.then(()=>db.collection(COL).doc(it.id).set(body)).then(()=>{
    if(rating) marks[it.id]={rating:rating,why:body.why}; else delete marks[it.id];
    render(); const s2=document.getElementById("s-"+it.id); if(s2) s2.textContent=rating?"저장됨":"지움";
  }).catch(e=>{ const s3=document.getElementById("s-"+it.id); if(s3) s3.textContent=(e&&(e.code==="not_granted"||e.code==="permission_denied"))?"저장 못 함 (권한)":"저장 못 함 — 다시 눌러 주세요"; });
}
document.querySelectorAll(".filt button").forEach(b=>b.addEventListener("click",()=>{filter=b.dataset.f;document.querySelectorAll(".filt button").forEach(x=>x.setAttribute("aria-pressed",String(x===b)));render();}));
$("#offline").textContent=`이 화면에서는 저장할 수 없습니다 (로그인이 필요하거나 보기 전용). 평가는 Claude 에게 '${N}단계 T043 좋아, T047 별로'처럼 말하면 됩니다.`;
render();
if(!ALL.length) return;
(async()=>{
  try{ db = window.claude && window.claude.use ? await window.claude.use("db") : null; }catch(e){ db=null; }
  if(!db){ $("#offline").hidden=false; return; }
  let user=null; try{ user=await window.claude.use("user"); }catch(e){}
  let cw=null; try{ cw = user ? await user.can("data.write") : null; }catch(e){ cw=null; }
  canWrite = cw!==false;
  if(!canWrite) $("#offline").hidden=false;
  db.collection(COL).onSnapshot(snap=>{
    snap.docs.forEach(doc=>{
      const v=doc.data()||{}; const it=byId[doc.id]; if(!it) return; const dv=Number(v.v)||0;
      if(dv===it.v){ if(v.rating) marks[doc.id]={rating:v.rating,why:v.why||""}; else delete marks[doc.id]; }
      else if(dv<it.v && v.rating && (!prevs[doc.id]||prevs[doc.id].v<=dv)){ prevs[doc.id]={v:dv,rating:v.rating,why:v.why||""}; }
    });
    render();
  },()=>{});
  render();
})();
})();
</script>
"""


STAGE_PAGES = {1: "평가판.html", 2: "평가판_2단계.html", 3: "평가판_3단계.html"}


def stage_page_item(r, n):
    """v1.6 단계 평가판 카드 한 장 — 이 단계까지의 칸 (앞 단계 칸은 회색 맥락) · 지금 판 · 이 판 평가 · 앞 판 평가 · 고친 까닭."""
    pk, x = r["pkg"], r["st"][n]
    keys = [k for s in range(1, n + 1) for k in STAGE_KEYS[s]]
    return {"id": r["id"], "rank": r["rank"] if n == 1 else None, "label": r["label"], "form": FORMS.get(pk.get("form"), ""), "carried": r["carried"] and n == 1,
            "v": x["v"], "rating": x["rating"], "why": x["why"], "prev": x["prev"], "fixed": last_fix(pk, n), **{k: pk[k] for k in keys}}


def render_stage_page(S, P, Z, n, rows):
    """v1.6 단계 n 평가판 HTML — 앞 단계를 모두 좋음으로 통과하고 이 단계 내용을 그 판에 맞춰 만든 것만 (rows = stage_rows)."""
    B = current_batch(S)
    urls = list((Z.get("stages") or {}).get("URLS") or ["", "", ""]) + ["", "", ""]
    open_ = [r for r in rows if r["st"][n]["open"] and not (n == 1 and r["st"][1]["carried"])]
    skipped = [{"id": r["id"], "label": r["label"].split(" (")[0]} for r in rows if r["st"][1]["carried"]] if n == 1 else []
    data = {"skipped": skipped, "stage": n, "name": NAME, "names": STAGE_NAME, "urls": urls[:3], "note": NOTE_PAGE, "batch": B["no"] if B else 0,
            "made": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
            "counts": {s: sum(1 for r in rows if r["st"][s]["open"] and not (s == 1 and r["st"][1]["carried"])) for s in (1, 2, 3)},
            "passed_prev": sum(1 for r in rows if n > 1 and r["st"][n - 1]["open"] and r["st"][n - 1]["rating"] == "좋음"),
            "waiting": sum(1 for r in rows if n > 1 and r["st"][n]["todo"] == "만들 차례"),
            "items": [{**stage_page_item(r, n), **({"rank": i} if n == 1 else {})} for i, r in enumerate((r for r in open_ if r["kind"] == "topic"), 1)],
            "episodes": [stage_page_item(r, n) for r in open_ if r["kind"] == "episode"]}
    js = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    return PAGE_STAGE.replace("__NAME__", NAME).replace("__STAGE__", str(n)).replace("__DATA__", js)


def log_stages(rows):
    """v1.6 단계마다 올린 수·좋음·나쁨 · Claude 가 할 일 (만들 차례 = 앞 단계 통과인데 이 단계 내용이 그 판에 맞춰 없음 · 다시 만들 차례 = 이 판 나쁨)."""
    for s in (1, 2, 3):
        op = [r for r in rows if r["st"][s]["open"]]
        todo = [f"{r['id']}" for r in rows if r["st"][s]["todo"] == "만들 차례"]
        redo = [f"{r['id']}" for r in rows if r["st"][s]["todo"] == "다시 만들 차례"]
        log("STAGE", step=s, shown=len(op), carried=sum(1 for r in op if r["st"][s]["carried"]), good=sum(1 for r in op if r["st"][s]["rating"] == "좋음"), bad=sum(1 for r in op if r["st"][s]["rating"] == "나쁨"),
            unrated=sum(1 for r in op if not r["st"][s]["rating"]), make=",".join(todo) or "-", remake=",".join(redo) or "-")


def revised_why(it):
    """v1.4 뜻이 바뀐 마지막 고침의 까닭 (갈래 이름만 바꾼 것은 뺌) — 문서·평가판에 '다시 짬'."""
    for r in reversed(it.get("revised") or []):
        if set(r.get("old") or {}) - {"data_kind", "theme", "persona", "needs", "market"}:
            return f"{r['at']} — {r['why']}"
    return ""


P_PAGE, Z_PAGE = [None], [None]           # v1.5 finish() 가 넣음 (기존 편 칸을 읽으려고)


def stage_cell(x):
    """v1.6 영상기획안.md 단계 표 한 칸."""
    if x.get("carried"):
        return f"v{x['v']} 좋음 (이전 평가)"
    if x["rating"]:
        return f"v{x['v']} {x['rating']}"
    if x["open"]:
        return f"v{x['v']} 평가 전"
    if x["todo"]:
        return x["todo"]
    return "—" if not x["v"] else f"v{x['v']} 초안"


def render_plans(S, P, Z):
    """v1.5 영상기획안.md — 이번 묶음 기획안 + 기존 편 다시 짠 안 (사람이 읽는 모음). v1.6: 맨 위 단계 평가 표 · 전달하고자 하는 내용."""
    B = current_batch(S)
    st = Z.get("stages") or {}
    urls = list(st.get("URLS") or [(Z.get("page") or {}).get("URL", "")])
    L = [f"# {NAME} 영상 기획안 — {B['no'] if B else 0}번째 묶음", "",
         f"(자동 — `tools/topic_ideas.py {VERSION}` · 기획안 `package` · 평가판 {' · '.join(u for u in urls if u)}) ※ 연구·교육용 — 투자 권유가 아님.", ""]
    if st:
        rows = stage_rows(S, P, Z)
        L += ["## 단계 평가", "", "1단계 제목·전달 내용 → 2단계 썸네일 문구·보조 문구·도입부 → 3단계 대본 내용. 앞 단계에서 좋음을 받은 것만 다음 단계로 (`단계평가.txt`). "
              "'초안' = 예전 기획안의 칸 (앞 단계를 통과하면 다시 만듦).", "",
              "| ID | 1단계 | 2단계 | 3단계 |", "|---|---|---|---|"]
        L += [f"| {r['label']} | " + " | ".join(stage_cell(r["st"][s]) for s in (1, 2, 3)) + " |" for r in rows] + [""]
    def block(head, pk, extra=""):
        out = [f"## {head}", "", f"- **제목**: {pk['title']}"] + ([f"- **형식**: {FORMS[pk['form']]}"] if pk.get("form") in FORMS else []) + (
               [f"- **전달하고자 하는 내용**: {' '.join(pk['message'])}"] if pk.get("message") else []) + [
               f"- **썸네일 문구**: {' / '.join(pk['thumb_main'])}", f"- **썸네일 보조 문구**: {pk['thumb_sub']}",
               f"- **도입부**: {' '.join(pk['intro'])}", "- **내용**:"]
        out += [f"  {i}. {x['q']} → **{x['a']}**" for i, x in enumerate(pk["items"], 1)]
        out += [f"- **해설**: {' '.join(pk['explain'])}"] + ([f"- {extra}"] if extra else []) + [""]
        return out
    if B:
        for t in B["ids"]:
            it = S["items"][t]
            if it.get("package"):
                pc = it.get("precheck") or {}
                L += block(f"{t} — {it['title']}", it["package"], f"정답 미리 확인: {pc.get('class', '-')} (정답의 근거 종류 — 영상 형식이 아님) · 주제 평가: {it.get('rating') or '-'}")
    eps = load_episodes(P, Z)
    if eps:
        L += ["# 기존 편 — 리스크 기준으로 다시 짠 안", ""]
        for e in eps:
            L += block(e["label"], e["full"], f"바뀐 것: {e['changed']}")
    return "\n".join(L) + "\n"


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
                          "score": f"{it['score']:.2f}", "basis": basis or it.get("why", ""), "rating": it.get("rating"), "why": it.get("rating_why", ""), "revised": revised_why(it),
                          "pkg": {k: it["package"][k] for k in PKG_KEYS} if all((it.get("package") or {}).get(k) for k in PKG_KEYS) else None,
                          "carried": (it.get("picked_why") or "").startswith("좋음")})
    data = {"batch": B["no"] if B else 0, "made": (B["made"][:10] if B else "-"), "analysis": str(A["analysis_made"])[:10], "items": items,
            "episodes": load_episodes(P_PAGE[0], Z_PAGE[0]) if P_PAGE[0] else []}
    js = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    return PAGE.replace("__NAME__", NAME).replace("__NOTE__", NOTE_PAGE).replace("__DATA__", js)


def selftest_stages():
    """v1.6 단계 판정 시험 — 파일을 안 건드림. 통과하면 0, 아니면 1 (로그 TEST)."""
    base = {"title": "제목", "thumb_main": ["가", "나"], "thumb_sub": "보조", "intro": ["하나.", "둘."], "items": [{"q": "q", "a": "a"}] * 3, "explain": ["해설."]}
    ok = []
    pk, ch, pr = stage_update(base, {"message": ["전달."]}, "첫 판")
    ok.append(("전달 내용만 넣으면 1단계 v1 · 2·3단계는 초안 v0", not pr and ch == [1] and pkg_ver(pk)[0] == {1: 1, 2: 0, 3: 0}))
    st = stage_status(pk, {}, "T1")
    ok.append(("평가 전: 1단계만 보임", st[1]["open"] and not st[2]["open"] and not st[3]["open"] and st[1]["todo"] is None))
    sm = {(1, "T1"): {1: {"rating": "좋음", "why": ""}}}
    st = stage_status(pk, sm, "T1")
    ok.append(("1단계 좋음 → 2단계 '만들 차례' (초안은 안 보임)", st[2]["todo"] == "만들 차례" and not st[2]["open"]))
    pk2, ch, _ = stage_update(pk, {"thumb_main": ["가", "나"], "thumb_sub": "보조", "intro": ["하나.", "둘."]}, "1단계 통과 뒤")
    st = stage_status(pk2, sm, "T1")
    ok.append(("같은 값이라도 판 0 이면 v1 로 만듦 → 2단계 보임 (base = 1단계 v1)", ch == [2] and st[2]["open"] and pkg_ver(pk2)[1][2] == 1))
    sm[(2, "T1")] = {1: {"rating": "나쁨", "why": "도입이 김"}}
    st = stage_status(pk2, sm, "T1")
    ok.append(("2단계 나쁨 → '다시 만들 차례' · 3단계 안 보임", st[2]["todo"] == "다시 만들 차례" and not st[3]["open"]))
    pk3, ch, _ = stage_update(pk2, {"intro": ["짧게.", "둘."]}, "도입이 김 → 줄임")
    st = stage_status(pk3, sm, "T1")
    ok.append(("고치면 2단계 v2 · 앞 판 평가는 prev · 고친 까닭", ch == [2] and st[2]["v"] == 2 and st[2]["prev"]["rating"] == "나쁨" and last_fix(pk3, 2) == "도입이 김 → 줄임"))
    pk4, ch, _ = stage_update(pk3, {"title": "새 제목"}, "제목 고침")
    st = stage_status(pk4, sm, "T1")
    ok.append(("1단계를 고치면 1단계 v2 평가 전 · 2단계는 안 보임", st[1]["v"] == 2 and st[1]["open"] and not st[1]["rating"] and not st[2]["open"]))
    sm[(1, "T1")][2] = {"rating": "좋음", "why": ""}
    st = stage_status(pk4, sm, "T1")
    ok.append(("1단계 v2 좋음 → 2단계는 base 어긋남 = '만들 차례'", st[2]["todo"] == "만들 차례" and not st[2]["ready"]))
    _, _, pr = stage_update(pk4, {"thumb_main": ["너무너무너무너무 긴 썸네일 한 줄", "나"]})
    ok.append(("검사 실패면 안 바꿈", bool(pr)))
    _, _, pr = stage_update(base, {"message": []})
    ok.append(("빈 전달 내용은 실패", bool(pr)))
    pk5, ch, pr = stage_update(pk2, {"form": "문제"}, "형식")
    ok.append(("v1.6.2 형식(form)은 판 번호를 안 올림", not pr and ch == [] and pkg_ver(pk5) == pkg_ver(pk2) and pk5["form"] == "문제"))
    _, _, pr = stage_update(pk2, {"form": "사실"})
    ok.append(("v1.6.2 형식은 문제·테스트·비교만", bool(pr)))
    st = stage_status(pk, {}, "T2", {"why": "예전 좋음"})
    ok.append(("v1.6.1 이전 평가 좋음 → 1단계 좋음(carried) · 2단계 '만들 차례'", st[1]["carried"] and st[1]["rating"] == "좋음" and st[2]["todo"] == "만들 차례"))
    st = stage_status(pk, {(1, "T2"): {1: {"rating": "나쁨", "why": "제목"}}}, "T2", {"why": "예전 좋음"})
    ok.append(("v1.6.1 1단계를 직접 평가하면 그것이 이김", not st[1]["carried"] and st[1]["todo"] == "다시 만들 차례"))
    for name, good in ok:
        log("TEST", logging.INFO if good else logging.ERROR, check=name, result="통과" if good else "실패")
    bad = sum(1 for _, g in ok if not g)
    log("TEST", checks=len(ok), failed=bad)
    return 1 if bad else 0


def main(argv=None):
    ap = argparse.ArgumentParser(description="주제 탐색 (주식·재테크) — 20개씩 · 평가를 배움 · 명확한 결론만")
    ap.add_argument("topic")
    ap.add_argument("cmd", choices=["material", "add", "mark", "use", "done", "status", "import", "precheck", "revise", "refresh", "package", "import-stage", "selftest"])
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
    elif a.cmd == "package":
        cmd_package(a.topic, a.args[0])
    elif a.cmd == "import-stage":
        cmd_import_stage(a.topic, a.args[0], a.args[1])
    elif a.cmd == "selftest":
        rc = selftest_stages()
        log("DONE", topic=a.topic, cmd=a.cmd, seconds=round(time.monotonic() - t0, 2))
        return rc
    elif a.cmd in ("use", "done"):
        cmd_use(a.topic, a.args[0], a.args[1] if len(a.args) > 1 else "", done=a.cmd == "done")
    else:
        cmd_status(a.topic)
    log("DONE", topic=a.topic, cmd=a.cmd, seconds=round(time.monotonic() - t0, 2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
