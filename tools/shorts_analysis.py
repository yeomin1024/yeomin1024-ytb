#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.3 — 2026-10-28 — 사용자 지시 2026-10-28 "1은 그렇게하고 최근에 조회수가 높을수록 더 많이 반영되도록 해야해 3은 할당량 남으면
#          진행하도록 해 나머지는 너가 추천하는 방향으로 하고" (값은 주제 analysis_rules.toml — 없으면 예전대로, success_analysis v1.6 과 같은 규칙):
#          · 성공 쇼츠: [shorts] MIN_VPD_SUBS > 0 = 구독자당 하루 조회수 ≥ 그 값 (orr.success_core) · 점수 큰 순 · WEIGHT "score" = 성공 쇼츠 몫(가중)
#            (쇼츠마다 무게 = 1 + log2(점수 ÷ 기준) — sa.case_weight, 주제·형식·제목 특징의 성공 쇼츠 몫).
#          · 하루 조회수 = 받은 때 조회수 ÷ 받은 때까지 날수 (orr.views_per_day).
#          · 1-4번 하루 조회수 상위 쇼츠 ([shorts_vpd_top] — 최근 MAX_AGE_DAYS 안, 롱폼 1-3번과 같은 꼴) · 1-5번 조회수 상위 쇼츠 ([shorts_views_top] —
#            기간 없는 쇼츠 검색 포함, 올린 날짜 상관없이). 둘 다 채널당 2개 + 그 묶음 니즈. 기간 없는 검색 캐시는 비교 집단·시장에 안 섞음.
# (v1.2.1 — 2026-10-18 — 뺀 쇼츠 까닭의 앞말을 주제마다 ([shorts_exclude] LABEL, 없으면 예전 그대로 '돈 이야기 아님') — 역사 쇼츠를 빼면
#          '돈 이야기 아님 — 드라마·영화 장면'으로 적혀 뜻이 틀려서 (history/analysis_rules.toml v1.4 LABEL = '역사 아님'). 빼는 규칙·숫자는 그대로
# (v1.2 — 2026-10-15 — 외국 영상 켜고 끄기 (사용자 지시: "주식은 외국 영상도 다 분석할 건데 확인해봐 on/off 기능(default off) 있는지
#          확인하고 없으면 추가해"): 주제 설정 INCLUDE_FOREIGN(기본 꺼짐)을 켜면 외국 쇼츠도 성공·비교·같은 채널 기준선에 넣음 (success_analysis v1.4
#          규칙을 그대로 씀) · 쇼츠마다 foreign 표시 · 첫 3초 음절·말 속도(한글 음절)는 한국어 쇼츠만으로 셈 · 한계 글)
# (v1.1 — 2026-10-15 — 돈 이야기가 아닌 쇼츠 빼기 · 채널 유형 '모름' 빼고 셈 · 정보 요청이 아닌 댓글 거름 (사용자 지시: "고쳐서 다시 분석해보자"
#          — 2026-10-15 결과 검토: 성공 쇼츠 103개 중 40여 개가 연예·예능 클립·운세·명언·정치·'노후차' 같은 다른 뜻이라 주제·형식 통계가 흐려짐):
#          ① [shorts_exclude] (주제마다 analysis_rules.toml — 코드 기본값 없음) 갈래별 정규식: where = text(제목·설명 앞 300자·채널 이름 — 영상 태그는
#             안 봄: '명언'·'이재명' 태그가 붙은 주식 쇼츠까지 빠져서) 또는 title(제목만). keep_if_money = true 면 제목(해시태그 포함)에 돈 낱말
#             (MONEY_RX)이 있으면 빼지 않음 — '투자 원칙 10가지 #명언' 은 남김. [shorts_exclude_videos] = 눈으로 보고 뺀 쇼츠(까닭과 함께).
#             성공·비교 집단·시장(수요와 공급)·같은 채널 기준선에서 모두 뺌, 까닭은 '돈 이야기 아님 — <갈래>' 로 0번에 수
#          ② 10번 채널 유형 — 채널 쇼츠 수를 모르는 채널(평소 쇼츠를 안 받은 채널 = 거의 성공 아닌 채널)은 비율에서 빼고 수만 적음
#          ③ 11번 '더 알고 싶은 것' — [shorts_needs] NOT_INFO_RX(띠·년생·재물복·로또·영입·노래·팬 …)가 든 댓글은 질문·요청에서 뺌
# (v1.0 — 2026-10-15 — 신규: 쇼츠 분석 (사용자 지시: "깃허브 저장소에 유튜브 분석기 있지? 거기에 쇼츠 분석 기능도 추가해 목적은
#          사람들의 니즈를 충족해주는 쇼츠를 만들어서 최대한 조회수를 높이기 위한 쇼츠를 만들기 위해 분석하는거야 전력을 다해서 해봐").
#          롱폼 분석(tools/success_analysis.py → analysis.md)과 같은 원칙 — AI 가 쇼츠 지시사항을 만들 재료, 숫자·원문만(해석·규칙 없음):
#          ① 성공 쇼츠 = 웹 화면 [쇼츠]에서 승인해 자료를 받은 쇼츠 중 기준(analysis_rules.toml [shorts] — 올린 지 3~180일·구독자 5만 이하·
#             조회수 5만 이상·조회수 ≥ 구독자×3·3분 이하 세로) — 채널당 2개. 근거: 2026-10-15 compare.csv 의 작은 채널 쇼츠 777개 중
#             조회수 중앙값 2,287·상위 10% 55,631, '5만·×3' 은 3.5%
#          ② 같은 채널 기준선 — 채널 쇼츠 목록(UUSH)의 평소 쇼츠 조회수 중앙값 대비 × · 같은 채널 잘된 쇼츠 vs 평소 쇼츠 (채널 크기·구독층을 뺀 비교)
#          ③ 비교 집단(탐색에서 본 쇼츠 — 채널당 최근 5개)의 주제·형식·제목·해시태그·길이(초)·올린 요일·시각·채널 유형별 성공 비율
#          ④ 수요와 공급 (최근 90일 쇼츠 시장: 주제 지수·검색어별·자동완성 말 중 쇼츠가 적은 말)
#          ⑤ 대본으로: 첫 3초(첫 말까지 걸린 시간·3초 안 음절·첫 줄 유형) · 말 속도 · 말이 차지한 비율 · 끝 문장(구독·댓글·풀영상 안내·질문·
#             끝맺음 없이 끝남) · 말 없는 쇼츠 · 설명란의 롱폼 연결
#          ⑥ 시청자 니즈 (성공 쇼츠 댓글 — 롱폼과 같은 갈래 + '더 자세히·긴 영상 요청')
#          ※ 쇼츠 조회수는 2025-03-31 부터 '재생·다시 재생 횟수'(시청 시간 하한 없음) — 시청 지속률·스와이프 비율은 API 로 볼 수 없다 (한계에 적음))
r"""
사용법 (저장소 최상위 또는 PC 실행 폴더 — 웹 화면이 쇼츠 승인·다시 분석 때, 분석기 음성인식 대기열이 쇼츠 하나 끝날 때마다 저절로 부름):
  python tools/shorts_analysis.py economic                 # 할당량 0 (같은 채널 평소 쇼츠 표지 그림만 받음 — --no-thumbs 로 끔)
입력:
  <주제>/result/outliers/shorts/S_<영상ID>/   웹 화면 [쇼츠] 승인 — metadata.json·description.txt·transcript.json·comments.csv·thumbnail.jpg
  <주제>/result/outliers/.cache/shorts/       쇼츠 탐색에서 본 영상 정보(<영상ID>.json — 화면비 포함)·쇼츠 검색(search_*.json)·
                                              채널 쇼츠 목록(uploads_<채널ID>.json — UUSH, total = 채널 쇼츠 수)   ← PC 에만
  <주제>/result/outliers/.cache/channels.json (구독자·개설일·영상 수 — 롱폼과 함께) · autocomplete.json (사람들이 찾는 말)
  <주제>/analysis_rules.toml [shorts]·[shorts_compare]·[shorts_baseline]·[shorts_format] (없으면 아래 기본값) · [exclude]·[demand]·[growth]
  <주제>/keywords.toml (관련어) · tag_rules.toml (TAG_THEMES = 주제 묶음)
출력 (<주제>/result/outliers/shorts/ — GitHub 에도 올라감):
  analysis.md (AI 가 읽을 분석 — 숫자·원문만) · analysis.json · compare.csv (비교 집단 — 다시 셀 수 있게) · approved.md (받은 쇼츠 전부)
  cases_NN.md (성공 쇼츠 사례별 — 대본 전문·첫 3초·끝 문장·댓글) · thumbs_NN.jpg (성공 쇼츠 표지) · thumbs_pairs_NN.jpg (같은 채널 짝)
로그: [STAGE] [시각] key=value (START·CASES·POOL·SUCCESS·COMPARE·BASELINE·MARKET·SPEECH·COMMENTS·THUMBS·WRITE·DONE)
※ 연구·교육용 분석 도구. 투자 권유가 아니다.
"""
import argparse
import csv
import io
import json
import logging
import math
import re
import statistics
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import outlier_research as orr                                     # noqa: E402  쇼츠 판별·해시태그·라이브/외국·관련어
import success_analysis as sa                                      # noqa: E402  주제 묶음·뺄 까닭·댓글 갈래·제목 낱말·비교 (롱폼과 같은 규칙)
from outlier_stats import TITLE_FEATURES                            # noqa: E402
from weekly_analysis import _published, _write_atomic, clean_description   # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
VERSION = "v1.3"
LOG = logging.getLogger("shorts")
KST = timezone(timedelta(hours=9))
SHORTS_DIR = "shorts"
SHORTS_CASE_RX = re.compile(r"^S_([0-9A-Za-z_-]{11})$")
NON_VIDEO_CACHE = ("search_", "supply_", "uploads_", "channels.json", "autocomplete.json")
DEFAULT_RULES = {
    # 성공 쇼츠 — 근거: 2026-10-15 economic compare.csv 의 작은 채널(구독자 5만 이하) 쇼츠 777개 (채널 업로드 목록 — 검색 치우침 없음):
    # 조회수 중앙값 2,287 · 상위 25% 6,511 · 상위 10% 55,631 · 배수 중앙값 0.28 · 상위 10% 3.99 → '5만 이상·×3 이상' = 27개(3.5%)
    # 조회수 부풀림 의심(쇼츠) — 근거: 2026-10-15 실제 쇼츠 검색 '연금' 33개: 6초짜리 7개가 조회수 73만~279만인데 좋아요 0.03~0.06%, 나머지 26개는 0.28~11%.
    # 광고로 조회수를 샀거나, 6초짜리 한 장 정보 쇼츠가 반복 재생돼(2025-03-31 부터 다시 재생도 조회수) 사람 수보다 조회수가 훨씬 많은 것 — API 로는 어느 쪽인지 모름.
    # 롱폼 규칙(좋아요 0.25% 미만 '그리고' 댓글 0.005% 미만)은 그중 하나를 댓글 0.0049% 로 겨우 걸렀음 → 쇼츠는 좋아요만으로 (좋아요 0 = 숨김 → 모름)
    "shorts": {"MAX_SECONDS": 180, "MIN_AGE_DAYS": 3, "MAX_AGE_DAYS": 180, "MAX_SUBS": 50000, "MIN_RATIO": 3.0, "MIN_VIEWS": 50000,
               "CASES_PER_CHANNEL": 2, "AD_SUSPECT_MIN_VIEWS": 50000, "AD_SUSPECT_MAX_LIKE_RATE": 0.002,
               "MIN_VPD_SUBS": 0, "WEIGHT": ""},          # v1.3: MIN_VPD_SUBS > 0 = 구독자당 하루 조회수 · WEIGHT "vpd" = 가중 성공 비율
    "shorts_vpd_top": {"TOP_PCT": 0, "MAX_AGE_DAYS": 0, "CASES_PER_CHANNEL": 2, "MIN_POOL": 30},    # v1.3: 1-4번 하루 조회수 상위 (0 = 끔)
    "shorts_views_top": {"TOP_PCT": 0, "CASES_PER_CHANNEL": 2, "MIN_POOL": 30},                     # v1.3: 1-5번 조회수 상위 (0 = 끔)
    "shorts_compare": {"MIN_AGE_DAYS": 3, "MAX_AGE_DAYS": 180, "MAX_SUBS": 50000, "PER_CHANNEL": 5, "MIN_GROUP": 15, "NOTABLE_DIFF": 0.10,
                       "RECENT_DAYS": 90},
    "shorts_baseline": {"MIN_VIDEOS": 5, "MIN_AGE_DAYS": 3, "MAX_AGE_DAYS": 180, "HIT": 3.0, "NORMAL_LO": 0.5, "NORMAL_HI": 1.5,
                        "PER_CHANNEL": 5, "PAIRS": 20},
}
# 쇼츠 형식 — 제목·채널 이름·태그(없으면 설명 앞 150자) 낱말, 위에서부터 먼저 맞는 것 하나 (analysis_rules.toml [shorts_format] 이 덮어씀).
# 원인이 아니라 '어떤 모양의 쇼츠인가' 묶음 (대본이 없어도 내용 구성을 가늠하려고)
DEFAULT_FORMATS = {
    "클립·발췌 (방송·인터뷰·강연 일부)": r"출처|풀\s?영상|풀\s?버전|원본|본편|인터뷰|방송|강연|강의|클립|발췌|하이라이트|편집본|토크|대담|ft\.|feat",
    "사연·상황극": r"사연|상황극|참교육|드라마|실화|며느리|시어머니|시댁|콩트|역할극",
    "브이로그·직접 해본 것": r"브이로그|vlog|일상|후기|해봤|해보니|가계부|살림|(월급|수익|계좌|자산) ?공개|언박싱",
    "제도 변화·소식": r"속보|뉴스|발표|바뀝|바뀐|달라지|달라진|개편|시행|부터|확정|인상|인하|신설|폐지",
    "정보 요약 (N가지·순서·방법)": r"\d\s*가지|순서|방법|하는\s?법|꿀팁|정리|총정리|체크|핵심|모르면|알아야|필수|공식",
    "숫자·비교 (얼마·순위·vs)": r"얼마|\bvs\b|VS|비교|순위|TOP|top|연봉|월급|수입|가격|원가|차이",
}
FORMAT_OTHER = "그 밖"
# 첫 줄(첫 3초) 유형 — 낱말 규칙 (한 쇼츠가 여러 유형에 들 수 있음)
HOOK_TYPES = {
    "질문으로 시작": r"\?|까요|나요|인가요|일까|을까|뭘까|왜일까|아세요|알아요",
    "숫자·금액으로 시작": r"\d|억|천만|만\s?원",
    "단정·경고 먼저": r"절대|하지\s?마|반드시|무조건|후회|망하|위험|큰일|손해|정답|결론|당장",
    "반전·의외": r"사실|알고\s?보니|의외|놀랍|충격|믿기|몰랐|아무도|진짜\s?이유|착각",
    "시청자 부르기": r"여러분|당신|구독자|님들|너(는|도|희)|이거\s?보는",
    "내 이야기·사연": r"(?<![가-힣])(저는|제가|저희|나는|내가)|어느\s?날|살\s?때|년\s?전",
}
ENDING_TYPES = {
    "구독·좋아요 부탁": r"구독|좋아요|알림",
    "댓글 유도": r"댓글",
    "저장·공유": r"저장|공유",
    "풀영상·다음 편 안내": r"풀\s?영상|풀\s?버전|전체\s?영상|본편|자세한|자세히|다음\s?(편|영상)|2탄|고정\s?댓글|링크|프로필",
    "질문으로 끝": r"\?|까요|나요|가요|을까|ㄹ까",
}
SENT_END_RX = re.compile(r"(다|요|죠|까|니다|세요|네|군|지|라|자|래|야|어|아)\s*[.!?…~]*\s*$")
DESC_LONG_LINK_RX = re.compile(r"youtu\.be/|youtube\.com/(watch|live)|풀\s?영상|전체\s?영상|본편|원본\s?영상|full\s?ver", re.I)
CAT_MORE = "더 자세히·긴 영상 요청 (풀영상·2탄·자세히)"
MORE_RX = r"풀\s?영상|전체\s?영상|본편|원본|자세히|자세한|길게|롱폼|긴\s?영상|2탄|다음\s?편|후속|더\s?(알려|설명|자세)"
SEC_BUCKETS = [(0, 15), (15, 30), (30, 45), (45, 60), (60, 90), (90, 181)]
TAG_BUCKETS = [(0, 1, "해시태그 없음"), (1, 3, "1~2개"), (3, 6, "3~5개"), (6, 10 ** 6, "6개 이상")]
WEEKDAYS = "월화수목금토일"
HOUR_BUCKETS = [(0, 6, "0~5시"), (6, 9, "6~8시"), (9, 12, "9~11시"), (12, 15, "12~14시"), (15, 18, "15~17시"), (18, 21, "18~20시"), (21, 24, "21~23시")]
CHANNEL_TYPES = [(0.9, "쇼츠만 (90% 이상)"), (0.5, "쇼츠 위주 (50~90%)"), (0.0, "롱폼 위주 (쇼츠 50% 미만)")]
QUOTES_PER_CASE = 2


def log(stage, level=logging.INFO, **kv):
    LOG.log(level, "[%s] [%s] %s", stage, datetime.now().isoformat(timespec="seconds"),
            " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) and ' ' in v else v}" for k, v in kv.items()))


# ---------------------------------------------------------------- 규칙·경로
def shorts_out(root, topic):
    return Path(root) / topic / "result" / "outliers" / SHORTS_DIR


def shorts_cache(root, topic):
    return Path(root) / topic / "result" / "outliers" / ".cache" / SHORTS_DIR


def load_rules(root, topic):
    """롱폼 규칙(success_analysis — 뺄 주제·광고 의심·자동완성 제외어·채널 성장) + 쇼츠 규칙 ([shorts]·[shorts_compare]·[shorts_baseline]·[shorts_format])."""
    rules = sa.load_rules(root, topic)
    d = sa._toml(Path(root) / topic / "analysis_rules.toml")
    for sec, dflt in DEFAULT_RULES.items():
        r = dict(dflt)
        for k, v in (d.get(sec) or {}).items():
            if k in r:
                r[k] = v
        rules[sec] = r
    fm = {str(k): str(v) for k, v in (d.get("shorts_format") or {}).items() if isinstance(v, str)}
    rules["shorts_format"] = fm or dict(DEFAULT_FORMATS)
    for k, rx in list(rules["shorts_format"].items()):
        try:
            re.compile(rx)
        except re.error as e:
            log("START", logging.WARNING, note=f"[shorts_format] '{k}' 정규식 오류 — 뺌", error=str(e)[:80])
            rules["shorts_format"].pop(k)
    rules["shorts_defaults"] = not any(d.get(s) for s in DEFAULT_RULES)
    rules["shorts_exclude"] = load_exclude(d)
    na = d.get("shorts_needs") or {}
    rules["shorts_needs"] = {"NOT_INFO_RX": _compile(na.get("NOT_INFO_RX"), "[shorts_needs] NOT_INFO_RX")}
    return rules


def _compile(rx, label):
    if not rx:
        return None
    try:
        return re.compile(str(rx), re.I)
    except re.error as e:
        log("START", logging.WARNING, note=f"{label} 정규식 오류 — 쓰지 않음", error=str(e)[:80])
        return None


def load_exclude(d):
    """v1.1 [shorts_exclude] (+ [shorts_exclude_videos]) → {"money": rx, "kinds": [{name, rx, where, keep_if_money}], "videos": {id: 까닭}}.
    주제마다 analysis_rules.toml 에만 있음 (코드 기본값 없음 — 사용자 지시 '설정도 다 따로')."""
    ex = d.get("shorts_exclude") or {}
    kinds = []
    for k in ex.get("kind") or []:
        if not isinstance(k, dict) or not k.get("name"):
            continue
        rx = _compile(k.get("rx"), f"[shorts_exclude] '{k.get('name')}'")
        if rx:
            kinds.append({"name": str(k["name"]), "rx": rx, "where": "title" if k.get("where") == "title" else "text",
                          "keep_if_money": bool(k.get("keep_if_money"))})
    videos = {str(k): str(v) for k, v in (d.get("shorts_exclude_videos") or {}).items()}
    return {"money": _compile(ex.get("MONEY_RX"), "[shorts_exclude] MONEY_RX"), "kinds": kinds, "videos": videos,
            "label": str(ex.get("LABEL") or OFF_KIND)}     # v1.2.1 까닭 앞말 (역사 = '역사 아님')


HASHTAG_RX = re.compile(r"#\S+")
OFF_KIND = "돈 이야기 아님"


def off_kind(x, rules):
    """v1.1: 돈 이야기가 아닌 쇼츠 → '돈 이야기 아님 — <갈래>(<맞은 말>)' 또는 ''. 찾는 곳: text = 제목·설명 앞 300자·채널 이름 (영상 태그는 안 봄),
    title = 제목만(해시태그 뺌). keep_if_money 갈래는 제목(해시태그 포함)에 돈 낱말이 있으면 빼지 않음. 눈으로 본 목록([shorts_exclude_videos])이 먼저."""
    E = rules.get("shorts_exclude") or {}
    why = (E.get("videos") or {}).get(x.get("id"))
    if why:
        return f"{E.get('label') or OFF_KIND} — {why.split('—')[0].strip()}(눈으로 봄: {why})"
    title = str(x.get("title") or "")
    text = " | ".join([title, str(x.get("description") or "")[:300], str(x.get("channel") or "")])
    plain = HASHTAG_RX.sub(" ", title)
    for k in E.get("kinds") or []:
        m = k["rx"].search(plain if k["where"] == "title" else text)        # title = 해시태그 뺀 제목 ('#이재명' 붙은 증시 방송 클립은 남김)
        if not m:
            continue
        if k["keep_if_money"] and E.get("money") and E["money"].search(title):     # 해시태그 포함 ('… #복리 #투자' 는 돈 이야기)
            continue
        return f"{E.get('label') or OFF_KIND} — {k['name']}({m.group(0).strip()})"
    return ""


def format_of(x, formats):
    head = " | ".join([str(x.get("title") or ""), str(x.get("channel") or ""), " ".join(map(str, x.get("tags") or []))])
    for text in (head, str(x.get("description") or "")[:150]):
        for name, rx in formats.items():
            if re.search(rx, text, re.I):
                return name
    return FORMAT_OTHER


# ---------------------------------------------------------------- 자료 읽기
def load_shorts_cache(cache):
    """쇼츠 캐시 → (영상 정보 {id: info}, 채널 쇼츠 목록 {채널ID: {"ids","total"}}, 쇼츠 검색 [캐시])."""
    infos, uploads, searches = {}, {}, []
    cache = Path(cache)
    for f in (cache.glob("*.json") if cache.is_dir() else []):
        try:
            d = json.loads(f.read_text("utf-8"))
        except (OSError, ValueError):
            continue
        if f.name.startswith("uploads_"):
            uploads[d.get("channel") or f.stem[len("uploads_"):]] = {"ids": d.get("ids") or [], "total": d.get("total"),
                                                                    "fetched": str(d.get("fetched") or "")[:10]}
        elif f.name.startswith("search_"):
            if d.get("q") and not sa.is_alltime_search(d):      # v1.3: 기간 없는 검색은 1-5번에만 (sa.load_alltime_ids)
                searches.append(d)
        elif not f.name.startswith(NON_VIDEO_CACHE) and isinstance(d, dict) and d.get("id") and "title" in d:
            infos[d["id"]] = d
    return infos, uploads, searches


def load_main_cache(out):
    """롱폼과 함께 쓰는 캐시: 채널 정보(channels.json — 구독자·개설일·영상 수)·자동완성."""
    cache = Path(out) / ".cache"
    try:
        ch = {k: v for k, v in json.loads((cache / "channels.json").read_text("utf-8")).items() if isinstance(v, dict)}
    except (OSError, ValueError):
        ch = {}
    try:
        ac = {k: v.get("s") or [] for k, v in json.loads((cache / "autocomplete.json").read_text("utf-8")).items() if isinstance(v, dict)}
    except (OSError, ValueError):
        ac = {}
    return ch, ac


def _num(x, default=0):
    try:
        return int(x)
    except (TypeError, ValueError):
        return default


def row_of(info, subs, now, known=()):
    """영상 정보 → 쇼츠 줄 (배수·나이·초·쇼츠 판별·해시태그·한국 시각)."""
    pub = _published(info)
    views = _num(info.get("views", info.get("view_count")))
    age = (now - pub).total_seconds() / 86400 if pub else None
    sec = info.get("seconds") or info.get("duration") or round(float(info.get("minutes") or 0) * 60)
    sh, basis = orr.is_short({**info, "duration": sec}, known)
    kst = pub.astimezone(KST) if pub else None
    desc = str(info.get("description") or "")
    return {"id": info.get("id"), "title": str(info.get("title") or ""), "channel": str(info.get("channel") or ""),
            "channel_id": info.get("channel_id") or "", "subs": subs, "views": views,
            "likes": _num(info.get("likes", info.get("like_count"))),
            "comments_total": _num(info.get("comments_reported", info.get("comment_count"))),
            "published": pub, "age_days": round(age, 1) if age is not None else None, "seconds": int(sec or 0),
            "minutes": round((sec or 0) / 60, 2), "ratio": round(views / max(subs, 100), 2) if subs is not None else None,
            "vpd": orr.views_per_day(views, pub, info.get("fetched"), now), "tags": info.get("tags") or [], "description": desc,   # v1.3
            "live": info.get("live"), "was_live": info.get("was_live"), "audio_lang": info.get("audio_lang") or "", "lang": info.get("lang") or "",
            "foreign": orr.is_foreign({"title": info.get("title"), "audio_lang": info.get("audio_lang"), "lang": info.get("lang")}),   # v1.2
            "is_short": sh, "short_basis": basis, "hashtags": orr.hashtags(info.get("title"), desc),
            "weekday": WEEKDAYS[kst.weekday()] if kst else "", "hour": kst.hour if kst else None,
            "long_link": bool(DESC_LONG_LINK_RX.search(desc))}


def _union_len(spans):
    tot, cur_s, cur_e = 0.0, None, None
    for s, e in sorted(spans):
        if cur_e is None or s > cur_e:
            if cur_e is not None:
                tot += cur_e - cur_s
            cur_s, cur_e = s, e
        else:
            cur_e = max(cur_e, e)
    return tot + ((cur_e - cur_s) if cur_e is not None else 0.0)


def speech_features(snips, seconds):
    """대본 조각 → 쇼츠 말 특징: 첫 말까지 걸린 초·3초 안 음절(나눠 셈)·첫 줄·끝 줄·말 속도(말하는 구간)·말이 차지한 비율(구간 합집합 ÷ 길이)
    ·첫 줄 유형·끝 줄 유형·끝맺음 없이 끝남. 자동 자막은 문장 부호가 없어 '줄' = 자막 조각 (8자 미만이면 다음 조각과 합침)."""
    if not snips:
        return {}
    snips = sorted(snips, key=lambda x: x["start"])
    H = orr.HANGUL
    syl = sum(len(H.findall(s["text"])) for s in snips)
    end = max(s["start"] + s["duration"] for s in snips)
    span = max(1e-6, end - snips[0]["start"])
    syl3 = 0.0
    for s in snips:
        a, b = s["start"], s["start"] + max(s["duration"], 0.01)
        ov = max(0.0, min(b, 3.0) - max(a, 0.0))
        if ov > 0:
            syl3 += len(H.findall(s["text"])) * ov / (b - a)
    first, k = "", 0
    while k < len(snips) and len(first) < 8:
        first = (first + " " + snips[k]["text"]).strip()
        k += 1
    last, k = "", len(snips) - 1
    while k >= 0 and len(last) < 8:
        last = (snips[k]["text"] + " " + last).strip()
        k -= 1
    first, last = re.sub(r"\s+", " ", first)[:120], re.sub(r"\s+", " ", last)[:120]
    first3 = " ".join(s["text"] for s in snips if s["start"] < 3.0)
    cov = _union_len([(s["start"], s["start"] + max(s["duration"], 0)) for s in snips]) / max(seconds or span, 1)
    head = first + " " + first3
    return {"syl": syl, "syl_per_sec": round(syl / span, 2), "first_speech_sec": round(snips[0]["start"], 2),
            "syl_first3": round(syl3, 1), "first_line": first, "first3": re.sub(r"\s+", " ", first3)[:160], "last_line": last,
            "coverage": round(min(cov, 1.0), 2), "lines": len(snips),
            "hook_types": [k for k, rx in HOOK_TYPES.items() if re.search(rx, head)],
            "ending_types": [k for k, rx in ENDING_TYPES.items() if re.search(rx, last)],
            "ends_open": not SENT_END_RX.search(last), "text": re.sub(r"\s+", " ", " ".join(s["text"] for s in snips)).strip()}


def load_cases(sdir, infos, subs_map, now, known):
    """쇼츠 사례 폴더 S_<영상ID> → 사례 목록 (숫자는 캐시가 더 새것이면 그것 — 늘기만 함)."""
    cases = []
    for d in sorted(Path(sdir).iterdir()) if Path(sdir).is_dir() else []:
        if not (d.is_dir() and SHORTS_CASE_RX.match(d.name) and (d / "metadata.json").is_file()):
            continue
        try:
            meta = json.loads((d / "metadata.json").read_text("utf-8"))
        except (OSError, ValueError):
            continue
        vid = meta.get("id") or SHORTS_CASE_RX.match(d.name).group(1)
        info = dict(meta)
        ci = infos.get(vid) or {}
        for k_meta, k_cache in (("views", "view_count"), ("likes", "like_count"), ("comments_reported", "comment_count")):
            info[k_meta] = max(_num(meta.get(k_meta)), _num(ci.get(k_cache)))
        for k in ("live", "was_live", "audio_lang", "lang", "embed_w", "embed_h", "duration", "published"):
            if k in ci and info.get(k) in (None, ""):
                info[k] = ci[k]
        info["seconds"] = meta.get("seconds") or ci.get("duration") or round(float(meta.get("minutes") or 0) * 60)
        info["fetched"] = orr.latest_fetch((_num(meta.get("views")), meta.get("collected")), (_num(ci.get("view_count")), ci.get("fetched")))   # v1.3
        try:
            desc = (d / "description.txt").read_text("utf-8") if (d / "description.txt").is_file() else str(ci.get("description") or "")
        except OSError:
            desc = ""
        info["description"] = desc
        cid = meta.get("channel_id")
        subs = subs_map.get(cid) if subs_map.get(cid) is not None else meta.get("subs")
        c = row_of(info, subs, now, known)
        snips, lang, no_speech = [], "", False
        if (d / "transcript.json").is_file():
            try:
                tj = json.loads((d / "transcript.json").read_text("utf-8"))
                lang, no_speech = str(tj.get("lang") or ""), bool(tj.get("no_speech"))
                snips = [{"text": str(x.get("text") or ""), "start": float(x.get("start") or 0), "duration": float(x.get("duration") or 0)}
                         for x in tj.get("snippets") or [] if isinstance(x, dict)]
            except (OSError, ValueError):
                snips = []
        cms = []
        if (d / "comments.csv").is_file():
            with open(d / "comments.csv", encoding="utf-8-sig", newline="") as f:
                for r in csv.DictReader(f):
                    cms.append({"text": str(r.get("text") or ""), "likes": _num(r.get("likes")),
                                "reply": str(r.get("is_reply")) in ("1", "True", "true"),
                                "creator": str(r.get("creator")) in ("1", "True", "true")})
        thumb = d / "thumbnail.jpg"
        dtext = clean_description(desc)
        c.update(folder=d.name, snips=snips, lang=lang, no_speech=no_speech,
                 src=("음성인식" if "음성인식" in lang else "자막") if snips else ("말 없음(음성인식)" if no_speech else ("설명" if dtext else "없음")),
                 speech=speech_features(snips, c["seconds"]) if snips else {}, comments=cms, desc_text=dtext,
                 comments_complete=bool(meta.get("comments_complete")), comments_fetched=len(cms),
                 cover=meta.get("cover") or "", thumb=(f"{d.name}/thumbnail.jpg" if thumb.is_file() and thumb.stat().st_size > 0 else None),
                 approved=meta.get("approved") or "", transcript_status=meta.get("transcript_status") or "")
        cases.append(c)
    return cases


# ---------------------------------------------------------------- 판정·비교
def is_success(x, S, with_age=True):
    """v1.3: orr.success_core (구독자당 하루 조회수 또는 배수 · 작은 채널 · 조회수 · 나이) + 쇼츠 길이."""
    return x["is_short"] and 0 < x["seconds"] <= S["MAX_SECONDS"] and orr.success_core(x, S, with_age)


INFLATED = "조회수 부풀림 의심"          # 광고 또는 반복 재생 — 성공·비교·같은 채널 기준선에서 뺌 (5-2 번에 따로 숫자)
TINY_SECONDS = 15                     # 5-2 번 '아주 짧은 쇼츠' (한 장 정보·반복 재생형?) 기준


def ad_suspect(x, S):
    """쇼츠 조회수 부풀림 의심 (광고 또는 반복 재생): 조회수 AD_SUSPECT_MIN_VIEWS 이상인데 좋아요 비율이 AD_SUSPECT_MAX_LIKE_RATE 미만
    (좋아요 0 은 숨김일 수 있어 모름 → 아님). 이름은 규칙 키(AD_SUSPECT_*)를 따름."""
    v, lk = x.get("views") or 0, x.get("likes") or 0
    return v >= S["AD_SUSPECT_MIN_VIEWS"] and 0 < lk / v < S["AD_SUSPECT_MAX_LIKE_RATE"]


def flags(x, rules, rel):
    """뺄 까닭 (롱폼과 같은 규칙: 라이브·외국·뺀 주제·주제 밖·광고 의심) + 쇼츠가 아님 + 쇼츠 광고 의심(좋아요만)."""
    if not x["is_short"]:
        return f"쇼츠 아님({x['short_basis']})"
    why = sa.flags(x, rules, rel)
    if (not why or why.startswith("광고 의심")) and ad_suspect(x, rules["shorts"]):     # 롱폼 광고 규칙에 걸린 것도 쇼츠 이름으로 (5-2번에 모이게)
        why = f"{INFLATED}(좋아요 {rules['shorts']['AD_SUSPECT_MAX_LIKE_RATE']:.1%} 미만 — 광고 또는 반복 재생)"
    elif why.startswith("광고 의심"):
        why = f"{INFLATED}(좋아요·댓글 거의 없음 — 광고 또는 반복 재생)"
    return why or off_kind(x, rules)


def _median(xs):
    return sa._median(xs)


def _share(xs, pred):
    xs = list(xs)
    return round(sum(1 for x in xs if pred(x)) / len(xs), 3) if xs else None


def bucket_rows(group, success, key, buckets, C):
    out = []
    for lo, hi, label in buckets:
        g = [x for x in group if key(x) is not None and lo <= key(x) < hi]
        r = sa._rate(g)
        out.append({"label": label, **r, "small_sample": r["n"] < C["MIN_GROUP"], "vpd_median": _median([x["vpd"] for x in g]),
                    "success_cases": [c["no"] for c in success if key(c) is not None and lo <= key(c) < hi]})
    return out


def title_feature_fns():
    feats = {**{k: (lambda rx: (lambda t: bool(re.search(rx, t))))(rx) for k, rx in TITLE_FEATURES.items()}, **sa.TITLE_SHAPE}
    feats["'#shorts' 표시"] = lambda t: bool(orr.SHORTS_TAG_RX.search(t))
    return feats


def channel_type(share):
    if share is None:
        return "모름 (채널 쇼츠 수 없음)"
    for lo, name in CHANNEL_TYPES:
        if share >= lo:
            return name
    return CHANNEL_TYPES[-1][1]


# ---------------------------------------------------------------- 분석
def top_group(kind, cases, pool, T, success, rules, others=None):
    """v1.3: 쇼츠 '하루 조회수 상위'(kind='vpd', 1-4번) · '조회수 상위'(kind='views', 1-5번) 묶음 — 모집단(검색에서 찾은 주제 관련 쇼츠, 뺄 까닭 없는 것)
    안에서 상위 TOP_PCT% 경계(orr.top_pct_threshold) → 자료를 받은 쇼츠 중 넘는 것, 구독자 상관없이, 채널당 CASES_PER_CHANNEL 개 (큰 순).
    vpd 는 MAX_AGE_DAYS(>0) 안만 ('최근 트렌드'). TOP_PCT 0 = 끔. others = 다른 묶음 번호(1-5번 표의 V# 칸). → (요약 dict, 묶음 목록)"""
    key = "vpd" if kind == "vpd" else "views"
    pct, max_age = float(T.get("TOP_PCT") or 0), float(T.get("MAX_AGE_DAYS") or 0)
    recent = (lambda x: x.get("age_days") is not None and x["age_days"] <= max_age) if max_age > 0 else (lambda x: True)
    pool = [x for x in pool if x.get(key) is not None and recent(x)]
    ages = [x["age_days"] for x in pool if x.get("age_days") is not None]
    res = {"kind": kind, "pct": pct, "threshold": None, "pool": len(pool), "min_pool": T.get("MIN_POOL", 30), "per_channel": T.get("CASES_PER_CHANNEL", 2),
           "max_age_days": max_age, "oldest_days": round(max(ages)) if ages else None, "older_than_year": sum(1 for a in ages if a > 365),
           "cases": [], "passed": 0, "excluded": [], "channel_cut": 0, "missing_total": 0, "missing": []}
    if pct <= 0:
        return res, []
    thr = orr.top_pct_threshold([x[key] for x in pool], pct) if len(pool) >= res["min_pool"] else None
    res["threshold"] = thr
    if thr is None:
        log("TOP_GROUP", logging.WARNING, kind=kind, pool=len(pool), min_pool=res["min_pool"], note="묶음 없음 — 검색 쇼츠가 적음")
        return res, []
    passed = [c for c in cases if c["is_short"] and (c[key] or 0) >= thr and recent(c)]
    per_ch, group, cut = Counter(), [], 0
    for c in sorted((c for c in passed if not c["exclude"]), key=lambda c: -(c[key] or 0)):
        ck = c["channel_id"] or c["channel"]
        if per_ch[ck] >= res["per_channel"]:
            cut += 1
            continue
        per_ch[ck] += 1
        group.append(c)
    nkey = "vno" if kind == "vpd" else "tno"
    for i, c in enumerate(group, 1):
        c[nkey] = i
    success_no = {c["id"]: c["no"] for c in success}
    case_ids = {c["id"] for c in cases}
    miss = sorted((x for x in pool if x[key] >= thr and x["id"] not in case_ids), key=lambda x: -x[key])
    res.update(passed=len(passed), channel_cut=cut, missing_total=len(miss),
               excluded=[{"id": c["id"], "title": c["title"], "why": c["exclude"]} for c in passed if c["exclude"]],
               big_channels=sum(1 for c in group if c["subs"] is None or c["subs"] > rules["shorts"]["MAX_SUBS"]),
               in_success=sum(1 for c in group if c["id"] in success_no),
               older_than_year_cases=sum(1 for c in group if c["age_days"] is not None and c["age_days"] > 365),
               comments_fetched=sum(c["comments_fetched"] for c in group), comments_total=sum(c["comments_total"] for c in group),
               cases=[{nkey: c[nkey], "id": c["id"], "title": c["title"], "channel": c["channel"], "subs": c["subs"], "views": c["views"],
                       "views_per_day": c["vpd"], "ratio": c["ratio"], "age_days": c["age_days"], "seconds": c["seconds"],
                       "published": c["published"].date().isoformat() if c["published"] else "", "theme": c["theme"], "format": c["format"],
                       "text_source": c["src"], "success_no": success_no.get(c["id"]), "url": f"https://www.youtube.com/shorts/{c['id']}",
                       **({"vno": (others or {}).get(c["id"])} if kind != "vpd" else {})} for c in group],      # vpd 는 nkey 가 곧 vno — 덮지 않게
               missing=[{"id": x["id"], "title": x["title"], "channel": x["channel"], "subs": x["subs"], "views": x["views"], "views_per_day": x["vpd"],
                         "seconds": x["seconds"], "published": x["published"].date().isoformat() if x["published"] else "", "theme": x["theme"]}
                        for x in miss[:30]])
    log("TOP_GROUP", kind=kind, pool=len(pool), pct=pct, threshold=round(thr, 1), oldest_days=res["oldest_days"], passed=len(passed),
        channel_cut=cut, group=len(group), in_success=res["in_success"], missing=len(miss))
    return res, group


def analyze(topic, name, cases, infos, uploads, searches, channels, ac, rules, rel, themes, now, alltime_ids=()):
    S, C = rules["shorts"], rules["shorts_compare"]
    weighted = str(S.get("WEIGHT") or "") == "score"              # v1.3: 성공 쇼츠 몫(가중)
    formats = rules["shorts_format"]
    subs_map = {k: v.get("subs") for k, v in channels.items()}
    for c in cases:
        c["theme"] = sa.theme_of(c["title"], c["tags"], themes)
        c["format"] = format_of(c, formats)
        c["exclude"] = flags(c, rules, rel)
    # 1) 성공 쇼츠 (자료를 받은 것 중) — 채널당 CASES_PER_CHANNEL 개 (배수 큰 순)
    passed = [c for c in cases if is_success(c, S)]
    excluded = [c for c in passed if c["exclude"]]
    eligible = sorted((c for c in passed if not c["exclude"]), key=lambda c: -(orr.success_metric(c, S) or 0))   # v1.3: 점수 큰 순
    per_ch, success, cut = Counter(), [], []
    for c in eligible:
        key = c["channel_id"] or c["channel"]
        if per_ch[key] >= S["CASES_PER_CHANNEL"]:
            cut.append(c)
            continue
        per_ch[key] += 1
        success.append(c)
    for i, c in enumerate(success, 1):
        c["no"] = i
        c["weight"] = sa.case_weight(c, S)                        # v1.3
    others = [c for c in cases if not any(c is s for s in success)]
    log("SUCCESS", cases=len(cases), passed=len(passed), excluded=len(excluded), channel_cut=len(cut), success=len(success),
        weight="score" if weighted else "-", rule=f"{S['MIN_AGE_DAYS']}~{S['MAX_AGE_DAYS']}일·구독자≤{S['MAX_SUBS']}·" + (f"구독자당 하루 조회수≥{S['MIN_VPD_SUBS']}" if float(S.get('MIN_VPD_SUBS') or 0) > 0 else f"×{S['MIN_RATIO']}") + f"·{S['MIN_VIEWS']}회·{S['MAX_SECONDS']}초 이하 세로·채널당{S['CASES_PER_CHANNEL']}")
    # 2) 비교 집단 — 쇼츠 탐색에서 본 영상 전부 + 사례 (채널당 최근 PER_CHANNEL 개)
    known = {i for u in uploads.values() for i in u["ids"]}
    pool = {}
    for vid, i in infos.items():
        x = row_of(i, subs_map.get(i.get("channel_id")), now, known)
        pool[vid] = x
    case_ids = {c["id"] for c in cases}
    for c in cases:
        pool[c["id"]] = c
    rows_all = list(pool.values())
    searched = {i for d in searches for i in (d.get("ids") or [])}
    for x in rows_all:
        if x["id"] not in case_ids:
            x["theme"] = sa.theme_of(x["title"], x["tags"], themes)
            x["format"] = format_of(x, formats)
            x["exclude"] = flags(x, rules, rel)
        x["success"] = is_success(x, S, with_age=False)
        x["has_case"] = x["id"] in case_ids
        x["in_scope"] = (not x["exclude"] and x["subs"] is not None and x["subs"] <= C["MAX_SUBS"]
                         and x["age_days"] is not None and C["MIN_AGE_DAYS"] <= x["age_days"] <= C["MAX_AGE_DAYS"])
        sh_total = (uploads.get(x["channel_id"]) or {}).get("total")
        vids = (channels.get(x["channel_id"]) or {}).get("videos")
        x["shorts_share"] = round(min(1.0, sh_total / vids), 2) if isinstance(sh_total, int) and vids else None
        x["channel_type"] = channel_type(x["shorts_share"])
    not_short = Counter(x["short_basis"] for x in rows_all if not x["is_short"])
    why_out = Counter(re.sub(r"\(.*", "", x["exclude"]) for x in rows_all if x["is_short"] and x["exclude"])     # 쇼츠인데 뺀 까닭
    by_ch = defaultdict(list)
    for x in rows_all:
        if x["in_scope"]:
            by_ch[x["channel_id"] or x["channel"]].append(x)
    group, ch_cut = [], 0
    for lst in by_ch.values():
        lst.sort(key=lambda x: x["published"] or datetime.min.replace(tzinfo=timezone.utc), reverse=True)
        group += lst[:C["PER_CHANNEL"]]
        ch_cut += max(0, len(lst) - C["PER_CHANNEL"])
    for x in rows_all:
        x["in_compare"] = False
    for x in group:
        x["in_compare"] = True
    base = sa._rate(group)
    from_uploads = sum(1 for x in group if x["id"] in known and x["id"] not in searched)
    log("COMPARE", pool=len(rows_all), shorts=sum(1 for x in rows_all if x["is_short"]), not_short=sum(not_short.values()),
        in_scope=sum(1 for x in rows_all if x["in_scope"]), group=len(group), channel_cut=ch_cut, success=base["success"], rate=base["rate"],
        from_channel_lists=from_uploads)
    # 자료를 받지 않은 성공 후보 (채널마다 남은 자리만큼)
    slots = Counter({k: S["CASES_PER_CHANNEL"] - v for k, v in per_ch.items()})
    missing, miss_ch, missing_full = [], Counter(), 0
    for x in sorted((x for x in rows_all if not x["has_case"] and not x["exclude"] and is_success(x, S)), key=lambda x: -(orr.success_metric(x, S) or 0)):
        key = x["channel_id"] or x["channel"]
        room = slots[key] if key in per_ch else S["CASES_PER_CHANNEL"]
        if miss_ch[key] >= room:
            missing_full += 1
            continue
        miss_ch[key] += 1
        missing.append(x)
    # 1-4·1-5) 하루 조회수 상위 · 조회수 상위 쇼츠 (v1.3 — 구독자 상관없이, 성공 쇼츠와 따로)
    sw = set(searched)
    vtop, vgroup = top_group("vpd", cases, [x for x in rows_all if x["id"] in sw and x["is_short"] and not x["exclude"]], rules["shorts_vpd_top"], success, rules)
    ttop, tgroup = top_group("views", cases, [x for x in rows_all if x["id"] in (sw | set(alltime_ids)) and x["is_short"] and not x["exclude"]],
                             rules["shorts_views_top"], success, rules, others={c["id"]: c.get("vno") for c in vgroup})
    for top_, grp_, pre in ((vtop, vgroup, "V"), (ttop, tgroup, "T")):
        if grp_:
            top_["needs"], st_ = sa.comment_needs(grp_, lambda c, pre=pre: f"{pre}{c[pre.lower() + 'no']}")
            log("COMMENTS", group=pre, cases=len(grp_), viewer_comments=st_["viewer"], spam_excluded=st_["spam"], requests=st_["requests"])
    # 3) 주제 묶음·형식
    def group_rows(keyname, names):
        out_ = []
        for nm in names:
            g = [x for x in group if x[keyname] == nm]
            sc_ = [c["no"] for c in success if c[keyname] == nm]
            if not g and not sc_:
                continue
            r = sa._rate(g)
            out_.append({keyname: nm, **r, "small_sample": r["n"] < C["MIN_GROUP"], "views_median": _median([x["views"] for x in g]),
                         "vpd_median": _median([x["vpd"] for x in g]), "success_cases": sc_,
                         "success_share": round(len(sc_) / len(success), 3) if success else None,
                         "w_success_share": sa.wshare(success, lambda c, nm=nm: c[keyname] == nm) if weighted else None})     # v1.3
        out_.sort(key=lambda r: (r["small_sample"], -(r["rate"] or 0)))
        return out_
    theme_rows = group_rows("theme", list(themes) + ["기타"])
    format_rows = group_rows("format", list(formats) + [FORMAT_OTHER])
    # 4) 제목·해시태그
    title_rows = []
    for k, fn in title_feature_fns().items():
        cmp_ = sa.compare_by(group, lambda x, fn=fn: fn(x["title"]), C)
        share = _share(success, lambda c, fn=fn: fn(c["title"])) if success else None
        if cmp_["with"]["n"] or share:
            title_rows.append({"feature": k, **cmp_, "success_case_share": share,
                               "w_success_case_share": sa.wshare(success, lambda c, fn=fn: fn(c["title"])) if weighted else None})   # v1.3
    title_rows.sort(key=lambda r: (not r["notable"], -(abs(r["diff"]) if r["diff"] is not None else 0)))
    df = Counter()
    for x in group:
        x["_words"] = sa.title_words(x["title"])
        df.update(x["_words"])
    min_df = max(6, math.ceil(len(group) * 0.03))
    word_rows = [{"word": w, **sa.compare_by(group, lambda x, w=w: w in x["_words"], C)} for w, n in df.items() if n >= min_df]
    word_rows.sort(key=lambda r: -(r["diff"] or 0))
    len_rows = bucket_rows(group, success, lambda x: len(x["title"]), [(0, 20, "20자 미만"), (20, 30, "20~29자"), (30, 40, "30~39자"),
                                                                          (40, 10 ** 6, "40자 이상")], C)
    tag_rows = bucket_rows(group, success, lambda x: len(x["hashtags"]), TAG_BUCKETS, C)
    tag_df, tag_succ = Counter(), Counter()
    for x in group:
        tag_df.update(set(x["hashtags"]))
    for c in success:
        tag_succ.update(set(c["hashtags"]))
    top_tags = [{"tag": t, "compare_n": n, **sa._rate([x for x in group if t in x["hashtags"]]), "success_cases": tag_succ.get(t, 0)}
                for t, n in tag_df.most_common(25)]
    # 5) 길이 (초)
    sec_rows = bucket_rows(group, success, lambda x: x["seconds"], [(lo, hi, f"{lo}~{hi - 1}초" if hi <= 180 else f"{lo}~180초")
                                                                    for lo, hi in SEC_BUCKETS], C)
    # 9) 올린 요일·시각 (한국 시간)
    wd_rows = bucket_rows(group, success, lambda x: WEEKDAYS.index(x["weekday"]) if x["weekday"] else None,
                          [(k, k + 1, f"{d}요일") for k, d in enumerate(WEEKDAYS)], C)
    hour_rows = bucket_rows(group, success, lambda x: x["hour"], HOUR_BUCKETS, C)
    # 8) 참여율
    def per1k(xs):
        xs = [x for x in xs if x is not None]
        return round(statistics.median(xs) * 1000, 2) if xs else None
    engagement = {k: {"likes_per_1k": per1k([x["likes"] / x["views"] for x in g if x["views"]]),
                      "comments_per_1k": per1k([x["comments_total"] / x["views"] for x in g if x["views"]]),
                      "vpd_median": _median([x["vpd"] for x in g]), "seconds_median": _median([x["seconds"] for x in g]), "n": len(g)}
                  for k, g in (("success", [x for x in group if x["success"]]), ("others", [x for x in group if not x["success"]]),
                               ("success_cases", success))}
    # 10) 채널 유형·빨리 크는 쇼츠 채널
    ctype_rows = []
    ctype_unknown = sum(1 for x in group if x["channel_type"].startswith("모름"))       # v1.1: 비율에서 뺌 (평소 쇼츠를 안 받은 채널 = 거의 성공 아닌 채널)
    for nm in [n for _, n in CHANNEL_TYPES]:
        g = [x for x in group if x["channel_type"] == nm]
        sc_ = [c["no"] for c in success if (pool.get(c["id"]) or c).get("channel_type") == nm]
        if g or sc_:
            r = sa._rate(g)
            ctype_rows.append({"type": nm, **r, "channels": len({x["channel_id"] for x in g}), "small_sample": r["n"] < C["MIN_GROUP"],
                               "success_cases": sc_})
    growth = shorts_growth(rows_all, channels, uploads, rules, now, rel)
    # 1-2) 같은 채널 기준선
    baseline = channel_baseline(cases, success, infos, uploads, subs_map, rules, themes, rel, now, known)
    # 3) 수요와 공급
    market = demand_supply(rows_all, cases, searches, ac, themes, rules, now)
    # 6·7) 말 (자료를 받은 쇼츠 — 성공 vs 나머지)
    speech = speech_compare(success, others)
    # 5-2) 아주 짧은 쇼츠 (TINY_SECONDS 초 미만 — 한 장 정보·반복 재생형?) — 주제 관련 쇼츠 전부 (부풀림 의심 포함, 그 밖에 뺀 것은 뺌)
    base_ok = [x for x in rows_all if x["is_short"] and (not x["exclude"] or x["exclude"].startswith(INFLATED))]
    tiny = {}
    for k, g in (("tiny", [x for x in base_ok if 0 < x["seconds"] < TINY_SECONDS]), ("rest", [x for x in base_ok if x["seconds"] >= TINY_SECONDS])):
        tiny[k] = {"n": len(g), "inflated": sum(1 for x in g if x["exclude"]), "channels": len({x["channel_id"] for x in g}),
                   "views_median": _median([x["views"] for x in g]), "likes_per_1k": _median([1000 * x["likes"] / x["views"] for x in g if x["views"]]),
                   "seconds_median": _median([x["seconds"] for x in g])}
    tiny["examples"] = [{"id": x["id"], "title": x["title"], "channel": x["channel"], "seconds": x["seconds"], "views": x["views"], "subs": x["subs"],
                         "likes_per_1k": round(1000 * x["likes"] / max(x["views"], 1), 2), "inflated": bool(x["exclude"])}
                        for x in sorted((x for x in base_ok if 0 < x["seconds"] < TINY_SECONDS), key=lambda x: -x["views"])[:12]]
    # 11) 시청자 니즈
    needs = comment_needs(success, rules)
    fetched = sum(c["comments_fetched"] for c in success)
    reported = sum(c["comments_total"] for c in success)
    limits = []
    no_script = [c["no"] for c in success if not c["snips"]]
    if no_script:
        limits.append(f"대본(자막·음성인식)이 없는 성공 쇼츠 {len(no_script)}개 (#{', #'.join(map(str, no_script[:30]))}{' …' if len(no_script) > 30 else ''}) — "
                      "첫 3초·말 속도·끝 문장은 대본이 있는 쇼츠로만 셌다 (음성인식은 쇼츠부터 — 끝나면 다시 셈). '말 없음'은 음성인식 결과가 없는 쇼츠(음악·화면 글자만)")
    incomplete = [c["no"] for c in success if not c["comments_complete"]]
    if incomplete:
        limits.append(f"댓글을 다 받지 못한 성공 쇼츠 {len(incomplete)}개 (받은 {fetched:,} / 달린 {reported:,}개 — 할당량이 끝나면 다음에 이어 받음)")
    if not group:
        limits.append("쇼츠 비교 집단 없음 — 쇼츠 탐색 캐시(.cache/shorts)가 없음 (PC 웹 화면에서 [쇼츠]로 탐색한 뒤 다시). 성공 비율은 셀 수 없음")
    else:
        limits.append(f"비교 집단 {len(group)}개 = 쇼츠 검색(조회수 순 — 잘된 쇼츠 쪽으로 치우침)" +
                      (f"·채널 쇼츠 목록 {from_uploads}개 (치우침 없음)" if from_uploads else "") +
                      f" 에서 올린 지 {C['MIN_AGE_DAYS']}~{C['MAX_AGE_DAYS']}일·구독자 {C['MAX_SUBS']:,} 이하, 성공 비율 {base['rate']:.0%} — "
                      "실제 시장 비율이 아니다. '있음/없음' 차이로만 보고, '무엇이 먹혔나'는 1-2번(같은 채널 안)을 먼저 보라")
    if len(success) < 15:
        limits.append(f"성공 쇼츠가 {len(success)}개뿐 — 성공 쇼츠 안의 비율은 흔들림이 크다 (웹 화면 [쇼츠] 목록에서 성공 후보를 승인하면 늘어남)")
    if why_out:
        ads = [x for x in rows_all if x["is_short"] and x["exclude"].startswith(("광고 의심", INFLATED))]
        limits.append("쇼츠인데 성공·비교에서 뺀 것: " + ", ".join(f"{k} {v}개" for k, v in why_out.most_common())
                      + (f" — 조회수 부풀림·광고 의심 {len(ads)}개의 길이 중앙값 {_median([x['seconds'] for x in ads])}초·조회수 중앙값 "
                         f"{_median([x['views'] for x in ads]):,.0f}회. 조회수는 많은데 좋아요가 거의 없음 = 광고로 조회수를 샀거나 아주 짧은 쇼츠가 반복 재생됨 "
                         "(어느 쪽인지 API 로는 모름 — 5-2번에 따로). 조회수 순 검색 위쪽을 덮는다 (2026-10-15 '연금' 검색: 6초짜리 7개)" if ads else ""))
    if not_short:
        limits.append("쇼츠 판별: 3분 이하 + 세로·정사각(화면비 = API embed 크기) — 쇼츠가 아니라서 뺀 것: "
                      + ", ".join(f"{k} {v}개" for k, v in not_short.most_common()) + ". 화면비를 모르는 예전 캐시는 '#shorts' 표시·60초 이하로 추정")
    if rules.get("include_foreign"):                              # v1.2: 외국 영상을 넣는 주제
        n_foreign = [c["no"] for c in success if c.get("foreign")]
        limits.append(f"외국 영상을 넣음 (주제 설정 INCLUDE_FOREIGN = true) — 성공 쇼츠 중 외국 쇼츠 {len(n_foreign)}개"
                      + (f" (#{', #'.join(map(str, n_foreign[:30]))})" if n_foreign else "") +
                      ". 첫 3초 음절·말 속도(한글 음절)는 한국어 쇼츠만으로 셌고, 제목·댓글 낱말 규칙은 한국어 기준이라 외국 쇼츠에는 거의 걸리지 않는다")
    limits += baseline["limits"] + market["limits"] + growth["limits"] + speech["limits"]
    limits += ["쇼츠 조회수는 2025-03-31 부터 '재생·다시 재생 횟수'(시청 시간 하한 없음)다 — 그 전 쇼츠와 숫자를 바로 비교하지 말 것. "
               "쇼츠의 핵심 신호(피드에서 '본 비율 vs 넘긴 비율'·평균 시청 비율·다시 재생)는 YouTube API 로 볼 수 없다 — 대신 조회수·배수·같은 채널 대비·"
               "참여율(좋아요·댓글 ÷ 조회수)·대본의 첫 3초·끝 문장을 본다",
               "형식·첫 줄·끝 줄 유형·댓글 갈래는 낱말 규칙이라 거칠다 (한 쇼츠가 여러 유형에 들 수 있음). 자동 자막은 문장 부호가 없어 '줄' = 자막 조각. 원문을 함께 보라",
               "화면 글자(자막 띠·제목 카드)·음악·편집 속도는 영상을 받지 않으므로 셀 수 없다 — 표지 그림(thumbs_NN.jpg)과 대본으로만 가늠한다",
               "'눈에 띔'은 차이가 크고 표본이 충분하다는 표시일 뿐 원인이 아니다"]
    data = {"tool": f"shorts_analysis.py {VERSION}", "topic": topic, "name": name, "generated": now.isoformat(timespec="seconds"),
            "rules": {k: rules[k] for k in ("shorts", "shorts_compare", "shorts_baseline", "shorts_format", "growth", "version", "file",
                                            "shorts_defaults", "shorts_vpd_top", "shorts_views_top")},
            "sources": {"case_folders": len(cases), "pool": len(rows_all), "pool_shorts": sum(1 for x in rows_all if x["is_short"]),
                        "not_short": dict(not_short), "excluded_shorts": dict(why_out), "compare_group": len(group), "compare_success": base["success"],
                        "compare_rate": base["rate"], "compare_channel_cut": ch_cut, "compare_from_channel_lists": from_uploads,
                        "success_passed": len(passed),
                        "success_excluded": [{"id": c["id"], "title": c["title"], "why": c["exclude"]} for c in excluded],
                        "success_channel_cut": [{"id": c["id"], "title": c["title"], "channel": c["channel"]} for c in cut],
                        "text_sources": dict(Counter(c["src"] for c in cases)), "success_text_sources": dict(Counter(c["src"] for c in success)),
                        "success_comments_fetched": fetched, "success_comments_reported": reported,
                        "searches": len(searches), "channel_lists": len(uploads), "covers": dict(Counter(c["cover"] or "-" for c in cases))},
            "limits": limits,
            "success_cases": [case_view(c) for c in success],
            "missing_success": [{"id": x["id"], "title": x["title"], "channel": x["channel"], "subs": x["subs"], "views": x["views"],
                                 "ratio": x["ratio"], "seconds": x["seconds"], "published": x["published"].date().isoformat() if x["published"] else "",
                                 "theme": x["theme"]} for x in missing[:40]],
            "missing_success_total": len(missing), "missing_success_channel_full": missing_full,
            "vpd_top": vtop, "views_top": ttop,
            "themes": theme_rows, "formats": format_rows, "title_features": title_rows,
            "title_words_up": [r for r in word_rows if (r["diff"] or 0) > 0][:15],
            "title_words_down": [r for r in reversed(word_rows) if (r["diff"] or 0) < 0][:10], "title_length": len_rows,
            "hashtag_count": tag_rows, "hashtags_top": top_tags, "seconds": sec_rows, "weekdays": wd_rows, "hours": hour_rows,
            "engagement": engagement, "tiny": tiny, "channel_types": ctype_rows, "channel_types_unknown": ctype_unknown, "growth": {k: v for k, v in growth.items() if k != "limits"},
            "baseline": {k: v for k, v in baseline.items() if k != "limits"}, "market": {k: v for k, v in market.items() if k != "limits"},
            "speech": {k: v for k, v in speech.items() if k != "limits"}, "needs": needs,
            "long_link_share": {"success": _share(success, lambda c: c["long_link"]), "others": _share(others, lambda c: c["long_link"]),
                                "compare_success": _share([x for x in group if x["success"]], lambda x: x["long_link"]),
                                "compare_others": _share([x for x in group if not x["success"]], lambda x: x["long_link"])},
            "approved": [approved_view(c) for c in sorted(cases, key=lambda c: c["published"] or datetime.min.replace(tzinfo=timezone.utc),
                                                           reverse=True)]}
    return data, success, group, rows_all, cases


def shorts_growth(rows_all, channels, uploads, rules, now, rel):
    """빨리 크는 쇼츠 채널: 개설 NEW_CHANNEL_MONTHS 개월 안·구독자 MIN_SUBS~MAX_SUBS·쇼츠 몫 50% 이상(채널 쇼츠 수 ÷ 영상 수) — 월 구독자 증가 순."""
    G = rules["growth"]
    vids = defaultdict(list)
    no_terms = not (rel.get("strong") or rel.get("weak"))          # 관련어가 없는 주제는 모든 쇼츠를 주제 관련으로
    for x in rows_all:
        if x["is_short"] and not x["exclude"] and x["channel_id"] and (no_terms or sa.title_relevant(x["title"], rel)):
            vids[x["channel_id"]].append(x)
    rows, no_created = [], 0
    for cid, xs in vids.items():
        e = channels.get(cid) or {}
        if not e.get("created"):
            no_created += 1
            continue
        try:
            created = datetime.fromisoformat(str(e["created"]).replace("Z", "+00:00"))
        except ValueError:
            continue
        months = max((now - created).days / 30.44, 1)
        subs = e.get("subs")
        sh_total = (uploads.get(cid) or {}).get("total")
        share = round(min(1.0, sh_total / e["videos"]), 2) if isinstance(sh_total, int) and e.get("videos") else None
        if subs is None:
            continue
        best = max(xs, key=lambda x: x["vpd"])
        rows.append({"channel_id": cid, "channel": xs[0]["channel"] or e.get("title"), "created": str(e["created"])[:10], "months": round(months, 1),
                     "subs": subs, "videos": e.get("videos"), "shorts_total": sh_total, "shorts_share": share,
                     "subs_per_month": round(subs / months), "uploads_per_month": round((e.get("videos") or 0) / months, 1),
                     "seen_shorts": len(xs), "seconds_median": _median([x["seconds"] for x in xs]),
                     "themes": [t for t, _ in Counter(x["theme"] for x in xs).most_common(2)],
                     "best": {"id": best["id"], "title": best["title"], "views": best["views"], "vpd": best["vpd"]}})
    fast = sorted((r for r in rows if r["months"] <= G["NEW_CHANNEL_MONTHS"] and G["MIN_SUBS"] <= r["subs"] <= G["MAX_SUBS"]
                   and (r["shorts_share"] is None or r["shorts_share"] >= 0.5)), key=lambda r: -r["subs_per_month"])[:G["TOP"]]
    limits = []
    if vids and not rows:
        limits.append("쇼츠 채널의 개설일 자료 없음 — 웹 화면 [쇼츠] 탐색이 채널 정보를 받으면 '빨리 크는 쇼츠 채널'이 나온다")
    if rows and not any(r["shorts_share"] is not None for r in rows):
        limits.append("채널 쇼츠 몫(쇼츠 수 ÷ 영상 수)은 채널 쇼츠 목록(UUSH)을 받은 채널만 — 쇼츠 승인 때 받음 (채널 하나 약 2단위)")
    log("GROWTH", channels=len(rows), fast=len(fast), no_created=no_created)
    return {"channels": len(rows), "fast": fast, "limits": limits}


def channel_baseline(cases, success, infos, uploads, subs_map, rules, themes, rel, now, known):
    """같은 채널 안 비교: 채널 쇼츠 목록(UUSH — 쇼츠만)의 올린 지 MIN_AGE~MAX_AGE 일 쇼츠 조회수 중앙값 대비 × ·
    채널마다 잘된 쇼츠(×HIT 이상) vs 평소 쇼츠(×NORMAL_LO~HI) — 채널당 PER_CHANNEL 개씩 · 성공 쇼츠와 같은 채널 평소 쇼츠 짝."""
    B = rules["shorts_baseline"]
    formats = rules["shorts_format"]
    chan_rows = {}
    for cid, u in uploads.items():
        rows = []
        for vid in dict.fromkeys(u["ids"]):
            i = infos.get(vid)
            if not i or (i.get("channel_id") and i["channel_id"] != cid):
                continue
            x = row_of(i, subs_map.get(cid), now, known)
            if not x["is_short"] or x["live"] or x["was_live"] or x["age_days"] is None or not (B["MIN_AGE_DAYS"] <= x["age_days"] <= B["MAX_AGE_DAYS"]):
                continue
            if ad_suspect(x, rules["shorts"]):            # 조회수 부풀림 의심(광고·반복 재생)은 채널 평소에도 넣지 않음 — 조회수가 사람 수가 아님
                continue
            x["theme"] = sa.theme_of(x["title"], x["tags"], themes)
            x["format"] = format_of(x, formats)
            ex_ = rules["exclude"]
            x["off"] = bool(orr.exclusion_reason(x, rules.get("include_foreign", False)) or any(w and w in x["title"] for w in ex_["OFF_TOPIC"]) or x["theme"] in ex_["OFF_TOPIC_THEMES"]
                            or off_kind(x, rules))                  # v1.1: 돈 이야기가 아닌 쇼츠는 잘된/평소 비교에서 뺌
            rows.append(x)
        if rows:
            chan_rows[cid] = rows
    for c in cases:
        others = [x for x in chan_rows.get(c["channel_id"]) or [] if x["id"] != c["id"]]
        c["channel_ratio"], c["channel_median"], c["channel_n"], c["normal_pairs"] = None, None, len(others), []
        if len(others) >= B["MIN_VIDEOS"]:
            med = statistics.median([x["views"] for x in others])
            c["channel_median"] = round(med)
            c["channel_ratio"] = round(c["views"] / max(med, 1), 1)
            c["normal_pairs"] = sorted([x for x in others if not x["off"]] or others,
                                       key=lambda x: abs(math.log((x["views"] + 1) / (med + 1))))[:2]
    hits, normal, n_ch = [], [], 0
    for cid, rows in chan_rows.items():
        if len(rows) < B["MIN_VIDEOS"] + 1:
            continue
        n_ch += 1
        med = statistics.median([x["views"] for x in rows])
        h = sorted((x for x in rows if not x["off"] and x["views"] >= B["HIT"] * med), key=lambda x: -x["views"])[:B["PER_CHANNEL"]]
        nm = sorted((x for x in rows if not x["off"] and B["NORMAL_LO"] * med <= x["views"] <= B["NORMAL_HI"] * med),
                    key=lambda x: -(x["published"].timestamp() if x["published"] else 0))[:B["PER_CHANNEL"]]
        for x in h + nm:
            x["channel_median"] = round(med)
            x["channel_ratio"] = round(x["views"] / max(med, 1), 1)
        hits += h
        normal += nm
    feats = []
    for k, fn in title_feature_fns().items():
        a, b = _share(hits, lambda x, fn=fn: fn(x["title"])), _share(normal, lambda x, fn=fn: fn(x["title"]))
        if (a or 0) or (b or 0):
            feats.append({"feature": k, "hits": a, "normal": b, "diff": round(a - b, 3) if a is not None and b is not None else None})
    feats.sort(key=lambda r: -abs(r["diff"] or 0))

    def shares(key):
        names = sorted({x[key] for x in hits + normal})
        rows_ = [{"name": n, "hits": _share(hits, lambda x, n=n: x[key] == n), "normal": _share(normal, lambda x, n=n: x[key] == n)} for n in names]
        for r in rows_:
            r["diff"] = round((r["hits"] or 0) - (r["normal"] or 0), 3)
        return sorted(rows_, key=lambda r: -abs(r["diff"]))
    covered = sum(1 for c in success if c.get("channel_ratio") is not None)
    pairs = [{"no": c["no"], "id": c["id"], "title": c["title"], "views": c["views"], "channel_ratio": c["channel_ratio"], "thumb": c["thumb"],
              "normal": [{"id": x["id"], "title": x["title"], "views": x["views"], "thumb": None} for x in c["normal_pairs"]]}
             for c in success if c.get("normal_pairs")][:B["PAIRS"]]
    limits = []
    if not uploads:
        limits.append("같은 채널 기준선 없음 — 채널 쇼츠 목록(UUSH)이 아직 없음 (웹 화면 [쇼츠] 승인·켤 때 받음 — 채널 하나 약 2단위)")
    elif success and covered < len(success):
        limits.append(f"같은 채널 기준선: 성공 쇼츠 {covered}/{len(success)}개만 '채널 평소 쇼츠 대비'가 있음 (채널 쇼츠가 {B['MIN_VIDEOS']}개 넘게 있어야 셈)")
    log("BASELINE", channels=len(chan_rows), compared_channels=n_ch, hits=len(hits), normal=len(normal), success_covered=covered)
    return {"channels": len(chan_rows), "compared_channels": n_ch, "hits": len(hits), "normal": len(normal), "success_covered": covered,
            "title_features": feats, "themes": shares("theme"), "formats": shares("format"),
            "seconds_median": {"hits": _median([x["seconds"] for x in hits]), "normal": _median([x["seconds"] for x in normal])},
            "hashtags_median": {"hits": _median([len(x["hashtags"]) for x in hits]), "normal": _median([len(x["hashtags"]) for x in normal])},
            "title_len_median": {"hits": _median([len(x["title"]) for x in hits]), "normal": _median([len(x["title"]) for x in normal])},
            "hit_examples": [{"id": x["id"], "title": x["title"], "channel": x["channel"], "views": x["views"], "channel_ratio": x["channel_ratio"],
                              "seconds": x["seconds"]} for x in sorted(hits, key=lambda x: -(x["channel_ratio"] or 0))[:25]],
            "normal_examples": [{"id": x["id"], "title": x["title"], "channel": x["channel"], "views": x["views"], "channel_ratio": x["channel_ratio"],
                                 "seconds": x["seconds"]} for x in normal[:15]],
            "pairs": pairs, "limits": limits}


def demand_supply(rows_all, cases, searches, ac, themes, rules, now):
    """쇼츠 수요와 공급: 시장 = 쇼츠 검색으로 찾은 최근 RECENT_DAYS 일 쇼츠 (채널 크기 상관없음). 수요 = 하루 조회수, 공급 = 쇼츠 수.
    지수 = 수요 몫 ÷ 공급 몫 (1 보다 크면 쇼츠 하나가 평균보다 많이 봄 = 공급이 모자라 보임)."""
    C, D, ex = rules["shorts_compare"], rules["demand"], rules["exclude"]
    by_id = {x["id"]: x for x in rows_all}
    searched = {i for d in searches for i in (d.get("ids") or [])}
    market = [x for x in rows_all if x["id"] in searched and x["is_short"] and not x["exclude"] and x["age_days"] is not None
              and x["age_days"] <= C["RECENT_DAYS"]]
    tot_v, tot_n = sum(x["vpd"] for x in market) or 1, len(market) or 1

    def norm(t):
        return re.sub(r"\s+", "", str(t)).lower()
    for x in market:
        x["_norm"] = norm(x["title"])
    th_rows = []
    for th in list(themes) + ["기타"]:
        g = [x for x in market if x["theme"] == th]
        if not g or th in ex["OFF_TOPIC_THEMES"]:
            continue
        ds, ss = sum(x["vpd"] for x in g) / tot_v, len(g) / tot_n
        th_rows.append({"theme": th, "videos": len(g), "channels": len({x["channel_id"] for x in g}), "demand_share": round(ds, 3),
                        "supply_share": round(ss, 3), "index": round(ds / ss, 2) if ss else None, "vpd_median": _median([x["vpd"] for x in g]),
                        "small_sample": len(g) < C["MIN_GROUP"]})
    th_rows.sort(key=lambda r: (r["small_sample"], -(r["index"] or 0)))
    kw = defaultdict(lambda: {"ids": [], "total": None, "fetched": ""})
    for d in searches:
        e = kw[d["q"]]
        e["ids"] += d.get("ids") or []
        e["total"] = d.get("total") if d.get("total") is not None else e["total"]
        e["fetched"] = max(e["fetched"], str(d.get("fetched") or ""))
    current = {norm(k) for k in rules.get("keywords") or []}
    kw_rows = []
    for q, e in kw.items():
        xs = [by_id[i] for i in dict.fromkeys(e["ids"]) if i in by_id]
        if not xs or any(w and w in q for w in ex["OFF_TOPIC"]):
            continue
        sh = [x for x in xs if x["is_short"]]
        ok = [x for x in sh if not x["exclude"]]
        small = [x for x in ok if x["subs"] is not None and x["subs"] <= C["MAX_SUBS"]]
        kw_rows.append({"q": q, "found": len(xs), "shorts": len(sh), "shorts_share": round(len(sh) / len(xs), 3), "total": e["total"],
                        "recent30": sum(1 for x in ok if (x["age_days"] or 999) <= 30), "views_median": _median([x["views"] for x in ok]),
                        "vpd_median": _median([x["vpd"] for x in ok]),
                        "big_share": round(sum(1 for x in ok if x["subs"] is None or x["subs"] > C["MAX_SUBS"]) / len(ok), 3) if ok else None,
                        "small_n": len(small), "small_success": sum(1 for x in small if x["success"]),
                        "small_hit_share": round(sum(1 for x in small if x["success"]) / len(ok), 3) if ok else None,
                        "current": norm(q) in current, "fetched": e["fetched"][:10]})
    kw_rows.sort(key=lambda r: (not r["current"], -(r["small_hit_share"] or 0), -(r["vpd_median"] or 0)))
    phrases, ac_excluded = {}, Counter()
    ch_names = {norm(x["channel"]) for x in rows_all if len(norm(x["channel"])) >= 3}
    for seed, sugg in (ac or {}).items():
        n = len(sugg) or 1
        for rank, ph in enumerate(sugg):
            if norm(ph) == norm(seed):
                continue
            why = ("뺀 주제" if any(w and w in ph for w in ex["OFF_TOPIC"]) else
                   "실시간·전망 등" if any(w and w.lower() in ph.lower() for w in D["AC_EXCLUDE"]) else
                   "채널 이름" if norm(ph) in ch_names or any(len(cn) >= 5 and norm(ph).startswith(cn) for cn in ch_names) else "")
            if why:
                ac_excluded[why] += 1
                continue
            e = phrases.setdefault(ph, {"phrase": ph, "score": 0.0, "seeds": []})
            e["score"] += (n - rank) / n
            e["seeds"].append(seed)
    ac_rows = []
    for ph, e in phrases.items():
        toks = [t for t in re.split(r"\s+", ph.lower()) if t]
        if not toks:
            continue
        hit = [x for x in market if all(t in x["_norm"] for t in toks)]
        ac_rows.append({"phrase": ph, "score": round(e["score"], 2), "seeds": e["seeds"][:3], "shorts_recent": len(hit),
                        "vpd_median": _median([x["vpd"] for x in hit]), "gap": round(e["score"] / (1 + len(hit)), 3)})
    ac_rows.sort(key=lambda r: -r["gap"])
    limits = []
    if not market:
        limits.append("쇼츠 수요·공급: 최근 쇼츠 자료 없음 (웹 화면 [쇼츠]에서 '검색어로도 찾기'로 탐색한 뒤 다시)")
    else:
        limits.append(f"쇼츠 수요·공급의 '시장'은 쇼츠 검색(조회수 순)에서 본 최근 {C['RECENT_DAYS']}일 쇼츠 {len(market)}개 — 조회수 적은 쇼츠가 덜 잡힌다. "
                      "주제 묶음 사이의 상대 비교(지수)로만 보라. 검색어별 '결과 수'는 4분 미만 전체(가로 영상 포함) 추정이다")
    if not ac:
        limits.append("자동완성(사람들이 찾는 말) 자료 없음 — 웹 화면을 켜면 받는다 (할당량 0)")
    log("MARKET", market=len(market), searched=len(searched), themes=len(th_rows), keywords=len(kw_rows), autocomplete=len(ac_rows),
        ac_excluded=",".join(f"{k}:{v}" for k, v in ac_excluded.items()) or "-")
    return {"days": C["RECENT_DAYS"], "videos": len(market), "themes": th_rows, "keywords": kw_rows,
            "autocomplete": ac_rows[:D["AUTOCOMPLETE_TOP"]], "autocomplete_total": len(ac_rows), "autocomplete_excluded": dict(ac_excluded),
            "limits": limits}


def speech_compare(success, others):
    """자료를 받은 쇼츠의 말 — 성공 쇼츠 vs 나머지 받은 쇼츠 (대본이 있는 것만, '말 없음'은 따로 셈)."""
    def stats(cs):
        t = [c for c in cs if c["snips"]]
        sp = [c["speech"] for c in t]
        sp_ko = [c["speech"] for c in t if not c.get("foreign")]     # v1.2: 음절(한글) 수는 한국어 쇼츠만
        return {"n": len(cs), "with_script": len(t), "no_speech": sum(1 for c in cs if c["no_speech"]),
                "no_speech_share": _share(cs, lambda c: c["no_speech"]) if cs else None,
                "first_speech_sec": _median([s["first_speech_sec"] for s in sp]), "syl_first3": _median([s["syl_first3"] for s in sp_ko]),
                "syl_per_sec": _median([s["syl_per_sec"] for s in sp_ko]), "coverage": _median([s["coverage"] for s in sp]),
                "lines": _median([s["lines"] for s in sp]), "seconds": _median([c["seconds"] for c in cs]),
                "hook_types": {k: _share(sp, lambda s, k=k: k in s["hook_types"]) for k in HOOK_TYPES},
                "hook_none": _share(sp, lambda s: not s["hook_types"]),
                "ending_types": {k: _share(sp, lambda s, k=k: k in s["ending_types"]) for k in ENDING_TYPES},
                "ending_none": _share(sp, lambda s: not s["ending_types"]), "ends_open": _share(sp, lambda s: s["ends_open"])}
    a, b = stats(success), stats(others)
    limits = []
    if a["with_script"] < 10:
        limits.append(f"말 비교(6·7번)는 대본이 있는 성공 쇼츠 {a['with_script']}개 · 나머지 {b['with_script']}개로 셌다 — 표본이 작다")
    log("SPEECH", success=a["n"], success_script=a["with_script"], others=b["n"], others_script=b["with_script"],
        no_speech=a["no_speech"] + b["no_speech"])
    return {"success": a, "others": b, "limits": limits}


def comment_needs(success, rules=None):
    """성공 쇼츠 댓글 — 롱폼과 같은 갈래(success_analysis.classify_comment) + '더 자세히·긴 영상 요청'. 채널 주인·도배 댓글 뺌.
    v1.1: [shorts_needs] NOT_INFO_RX(띠·년생·재물복·로또·영입·노래·팬 …)가 든 댓글은 '더 알고 싶은 것'(질문·요청)에서 뺌 — 정보 요청이 아님."""
    not_info = ((rules or {}).get("shorts_needs") or {}).get("NOT_INFO_RX")
    n_not_info = 0
    def spam_key(t):
        k = re.sub(r"[^가-힣A-Za-z]", "", t)
        return k[-50:] if len(k) >= 30 else None
    seen = defaultdict(set)
    for c in success:
        for m in c["comments"]:
            k = None if m["creator"] else spam_key(m["text"])
            if k:
                seen[k].add(c["id"])
    spam_keys = {k for k, v in seen.items() if len(v) >= sa.SPAM_MIN_VIDEOS}
    cats = list(sa.NEED_CATS) + [CAT_MORE]
    cat_count, cat_likes, quotes, requests_q = Counter(), Counter(), defaultdict(list), []
    n_viewer = n_spam = 0
    for c in success:
        c["needs"] = Counter()
        c["need_quotes"] = defaultdict(list)
        for m in c["comments"]:
            if m["creator"] or not m["text"].strip():
                continue
            if re.search(sa.SPAM_RX, m["text"]) or spam_key(m["text"]) in spam_keys:
                n_spam += 1
                continue
            n_viewer += 1
            found = sa.classify_comment(m["text"]) + ([CAT_MORE] if re.search(MORE_RX, m["text"]) else [])
            if sa.CAT_ASK in found and not_info and not_info.search(m["text"]):
                found.remove(sa.CAT_ASK)
                n_not_info += 1
            for cat in found:
                cat_count[cat] += 1
                cat_likes[cat] += m["likes"]
                c["needs"][cat] += 1
                q = {"no": c["no"], "likes": m["likes"], "reply": m["reply"], "text": re.sub(r"\s+", " ", m["text"]).strip()[:200]}
                quotes[cat].append(q)
                c["need_quotes"][cat].append(q)
                if cat == sa.CAT_ASK and re.search(sa.EXPLICIT_ASK, m["text"]):
                    requests_q.append(q)
    req_ids = {id(q) for q in requests_q}
    log("COMMENTS", success=len(success), viewer_comments=n_viewer, spam_excluded=n_spam, requests=len(requests_q), not_info_asks=n_not_info,
        more=cat_count[CAT_MORE])
    return {"viewer_comments": n_viewer, "spam_excluded": n_spam, "requests_total": len(requests_q), "not_info_asks": n_not_info,
            "requests": sa.top_quotes(requests_q, 40),
            "categories": [{"name": k, "count": cat_count[k], "share": round(cat_count[k] / n_viewer, 3) if n_viewer else None,
                            "likes": cat_likes[k]} for k in cats],
            "top": {k: sa.top_quotes(quotes.get(k, []), 8) for k in cats},
            "questions": sa.top_quotes([q for q in quotes.get(sa.CAT_ASK, []) if id(q) not in req_ids], 20),
            "complaints": sa.top_quotes(quotes.get(sa.CAT_BAD, []), 15, replies=True)}


def case_view(c):
    sp = c["speech"] or {}
    return {"no": c["no"], "id": c["id"], "title": c["title"], "channel": c["channel"], "channel_id": c["channel_id"], "subs": c["subs"],
            "views": c["views"], "ratio": c["ratio"], "views_per_day": c["vpd"], "seconds": c["seconds"], "likes": c["likes"],
            "likes_per_1k": round(1000 * c["likes"] / max(c["views"], 1), 2), "comments_per_1k": round(1000 * c["comments_total"] / max(c["views"], 1), 3),
            "published": c["published"].astimezone(KST).isoformat(timespec="minutes") if c["published"] else "", "age_days": c["age_days"],
            "weekday": c["weekday"], "hour": c["hour"], "theme": c["theme"], "format": c["format"], "folder": c["folder"],
            "thumbnail": c["thumb"], "cover": c["cover"], "text_source": c["src"], "hashtags": c["hashtags"], "long_link": c["long_link"],
            "description": c["desc_text"][:300], "first_line": sp.get("first_line"), "first3": sp.get("first3"), "last_line": sp.get("last_line"),
            "first_speech_sec": sp.get("first_speech_sec"), "syl_first3": sp.get("syl_first3"), "syl_per_sec": sp.get("syl_per_sec"),
            "coverage": sp.get("coverage"), "hook_types": sp.get("hook_types"), "ending_types": sp.get("ending_types"), "ends_open": sp.get("ends_open"),
            "text": (sp.get("text") or "")[:1500], "channel_ratio": c.get("channel_ratio"), "channel_median": c.get("channel_median"),
            "channel_n": c.get("channel_n"), "short_basis": c["short_basis"],
            "normal_pairs": [{"id": x["id"], "title": x["title"], "views": x["views"]} for x in c.get("normal_pairs") or []],
            "comments_fetched": c["comments_fetched"], "comments_total": c["comments_total"], "comments_complete": c["comments_complete"],
            "needs": {k: c["needs"].get(k, 0) for k in list(sa.NEED_CATS) + [CAT_MORE]},
            "need_quotes": {k: sa.top_quotes(v, 2, per_case=2) for k, v in c["need_quotes"].items() if v},
            "url": f"https://www.youtube.com/shorts/{c['id']}"}


def approved_view(c):
    return {"id": c["id"], "title": c["title"], "channel": c["channel"], "subs": c["subs"], "views": c["views"], "ratio": c["ratio"],
            "seconds": c["seconds"], "published": c["published"].date().isoformat() if c["published"] else "", "success_no": c.get("no"),
            "exclude": c["exclude"], "text_source": c["src"], "comments": c["comments_fetched"], "comments_complete": c["comments_complete"],
            "channel_ratio": c.get("channel_ratio"), "folder": c["folder"], "thumb": c["thumb"], "short_basis": c["short_basis"]}


# ---------------------------------------------------------------- 표지 그림 한 장에 (세로 9:16 칸)
def contact_sheet_v(items, out_path, cols=6, w=180):
    """[(번호, 그림 경로)] → 한 장 (세로 칸). 4:3·16:9 표지는 가운데를 9:16 으로 잘라 넣음 (쇼츠 hqdefault 는 세로 화면 양옆이 검은 띠)."""
    try:
        from PIL import Image, ImageDraw
    except ImportError:
        log("THUMBS", logging.WARNING, note="Pillow 없음 — 표지 한 장 만들기 건너뜀 (사례 폴더의 thumbnail.jpg 는 있음)")
        return 0
    items = [(n, p if p and Path(p).is_file() else None) for n, p in items]
    if not any(p for _, p in items):
        return 0
    h = w * 16 // 9
    rows = math.ceil(len(items) / cols)
    sheet = Image.new("RGB", (cols * w, rows * h), (20, 20, 20))
    draw = ImageDraw.Draw(sheet)
    for k, (n, p) in enumerate(items):
        if not p:
            continue
        try:
            im = Image.open(p).convert("RGB")
        except Exception:
            continue
        iw, ih = im.size
        if iw * 16 > ih * 9:                        # 가로가 넓음 → 가운데 9:16
            cw = ih * 9 / 16
            im = im.crop((int((iw - cw) / 2), 0, int((iw + cw) / 2), ih))
        else:
            chh = iw * 16 / 9
            im = im.crop((0, int((ih - chh) / 2), iw, int((ih + chh) / 2)))
        im = im.resize((w, h))
        x, y = (k % cols) * w, (k // cols) * h
        sheet.paste(im, (x, y))
        label = f"#{n}" if isinstance(n, int) else str(n)
        draw.rectangle([x, y, x + 8 + 7 * len(label), y + 20], fill=(0, 0, 0))
        draw.text((x + 5, y + 4), label, fill=(255, 255, 0))
    sheet.save(out_path, "JPEG", quality=82)
    return sum(1 for _, p in items if p)


def paged_v(items, out, prefix, per=24, cols=6):
    out = Path(out)
    pages = []
    for k in range(0, len(items), per):
        chunk = items[k:k + per]
        name = f"{prefix}_{k // per + 1:02d}.jpg"
        if contact_sheet_v(chunk, out / name, cols=cols):
            pages.append((name, chunk[0][0], chunk[-1][0]))
    keep = {n for n, _, _ in pages}
    for f in out.glob(f"{prefix}_*.jpg"):
        if f.name not in keep:
            f.unlink()
    return pages


def fetch_pair_covers(cache, pairs, limit=40):
    """같은 채널 평소 쇼츠의 표지 (PC — 그림 1장씩, 할당량 0). .cache/shorts/thumbs/<영상ID>.jpg → pairs 의 thumb 에 상대 경로."""
    d = Path(cache) / "thumbs"
    d.mkdir(parents=True, exist_ok=True)
    got = 0
    for pr in pairs:
        for x in pr["normal"]:
            f = d / f"{x['id']}.jpg"
            if f.is_file() and f.stat().st_size > 0:
                x["thumb"] = str(f)
                continue
            if got >= limit:
                continue
            if orr.shorts_cover(x["id"], f, timeout=10):
                x["thumb"] = str(f)
                got += 1
    return got


# ---------------------------------------------------------------- 쓰기
_pct, _n, _cell, _rate_txt = sa._pct, sa._n, sa._cell, sa._rate_txt


def _sec(x):
    return f"{x:.0f}초" if isinstance(x, (int, float)) else "–"


def _cmp_line(r):
    return (f"| {_rate_txt(r['with'])} | {_rate_txt(r['without'])} | {('+' if (r['diff'] or 0) > 0 else '') + _pct(r['diff']) if r['diff'] is not None else '–'}"
            f"{' ⚑' if r['notable'] else ''}{' (표본 적음)' if r['small_sample'] else ''} |")


def write_md(out, data, success):
    S, C, B = data["rules"]["shorts"], data["rules"]["shorts_compare"], data["rules"]["shorts_baseline"]
    src = data["sources"]
    L = [f"# 쇼츠 분석 — {data['name']} (`{data['topic']}`)", "",
         f"만든 시각 {data['generated']} UTC · `{data['tool']}` · 규칙 `{data['rules']['file']}` {data['rules']['version']}"
         + (" (쇼츠 규칙은 기본값 — tools/shorts_analysis.py)" if data["rules"].get("shorts_defaults") else ""),
         "", "> **AI 가 쇼츠 지시사항을 만들 재료** — 숫자와 원문만 있고 해석·규칙은 없다. 0번 '한계'를 먼저 읽고, 표본이 작은 차이·대본 없는 사례로 규칙을 만들지 않는다.",
         "> 롱폼 분석은 `../analysis.md` (같은 시청자 — 롱폼 댓글 요청은 거기 8-1). ※ 연구·교육용 — 투자 권유가 아님.", ""]
    L += ["## 0. 자료와 한계", "",
          f"- 받은 쇼츠(사례 폴더 `S_<영상ID>`) {src['case_folders']}개 · 쇼츠 탐색에서 본 영상 {src['pool']:,}개 (그중 쇼츠 {src['pool_shorts']:,}) · "
          f"쇼츠 검색 {src['searches']}개 · 채널 쇼츠 목록 {src['channel_lists']}곳",
          f"- 비교 집단 {src['compare_group']:,}개 (성공 {src['compare_success']}, {_pct(src['compare_rate'])}) — 채널당 최근 {C['PER_CHANNEL']}개 (잘린 {src['compare_channel_cut']})",
          "- 글 출처 (받은 쇼츠 전부): " + (" · ".join(f"{k} {v}" for k, v in src["text_sources"].items()) or "–")
          + " · 표지: " + (" · ".join(f"{'못 받음' if k == '-' else k} {v}" for k, v in src["covers"].items()) or "–"), ""]
    L += [f"- {x}" for x in data["limits"]] + [""]
    # 1
    L += [f"## 1. 성공 쇼츠 {len(success)}개", "",
          f"기준: 받은 쇼츠 중 올린 지 {S['MIN_AGE_DAYS']}~{S['MAX_AGE_DAYS']}일 · 구독자 {S['MAX_SUBS']:,} 이하 · 조회수 {S['MIN_VIEWS']:,} 이상 · "
          + (f"**구독자당 하루 조회수 ≥ {S['MIN_VPD_SUBS']:g}** (하루 조회수 = 받은 때 조회수 ÷ 받은 때까지 날수, ÷ 구독자)" if float(S.get("MIN_VPD_SUBS") or 0) > 0
             else f"조회수 ≥ 구독자 × {S['MIN_RATIO']}") +
          f" · {S['MAX_SECONDS']}초 이하 세로·정사각 · 채널당 {S['CASES_PER_CHANNEL']}개 ({'구독자당 하루 조회수' if float(S.get('MIN_VPD_SUBS') or 0) > 0 else '배수'} 큰 순). "
          f"통과 {src['success_passed']} − 뺀 것 {len(src['success_excluded'])} − 채널당 제한 {len(src['success_channel_cut'])}", "",
          "| # | 제목 | 채널 | 구독자 | 조회수 | 배수 | 채널 평소 쇼츠 대비 | 하루 조회수 | 길이 | 좋아요/1천 | 올린 때(한국) | 주제 | 형식 | 글 출처 | 첫 줄(첫 3초) |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for c in data["success_cases"]:
        L.append(f"| {c['no']} | [{_cell(c['title'], 50)}]({c['url']}) | {_cell(c['channel'], 16)} | {_n(c['subs'])} | {_n(c['views'])} | ×{c['ratio']} | "
                 f"{('×' + str(c['channel_ratio'])) if c['channel_ratio'] is not None else '–'} | {_n(c['views_per_day'])} | {c['seconds']}초 | "
                 f"{c['likes_per_1k']} | {c['weekday']} {c['hour'] if c['hour'] is not None else ''}시 | {_cell(c['theme'], 12)} | {_cell(c['format'], 12)} | "
                 f"{c['text_source']} | {_cell(c['first_line'] or '', 40)} |")
    if data["sources"]["success_excluded"]:
        L += ["", "기준은 넘었지만 뺀 것: " + "; ".join(f"{_cell(x['title'], 30)} ({x['why']})" for x in data["sources"]["success_excluded"][:20])]
    bl = data["baseline"]
    L += ["", f"### 1-2. 같은 채널 기준선 (채널 쇼츠 목록 {bl['channels']}곳 — 채널 크기·구독층이 같은 쇼츠끼리)", "",
          f"성공 쇼츠 {bl['success_covered']}/{len(success)}개에 '채널 평소 쇼츠 대비'(그 채널의 올린 지 {B['MIN_AGE_DAYS']}~{B['MAX_AGE_DAYS']}일 쇼츠 조회수 중앙값, 쇼츠 {B['MIN_VIDEOS']}개 넘을 때). "
          f"채널 {bl['compared_channels']}곳의 잘된 쇼츠(중앙값 ×{B['HIT']} 이상) {bl['hits']}개 vs 평소 쇼츠(×{B['NORMAL_LO']}~{B['NORMAL_HI']}) {bl['normal']}개 — 채널당 {B['PER_CHANNEL']}개씩", "",
          f"- 길이 중앙값: 잘된 {_sec(bl['seconds_median']['hits'])} · 평소 {_sec(bl['seconds_median']['normal'])} · 제목 글자 중앙값: 잘된 {_n(bl['title_len_median']['hits'])} · 평소 {_n(bl['title_len_median']['normal'])}"
          f" · 해시태그 수 중앙값: 잘된 {_n(bl['hashtags_median']['hits'])} · 평소 {_n(bl['hashtags_median']['normal'])}", "",
          "| 제목 특징 | 잘된 쇼츠 | 평소 쇼츠 | 차이 |", "|---|---|---|---|"]
    L += [f"| {r['feature']} | {_pct(r['hits'])} | {_pct(r['normal'])} | {_pct(r['diff'])} |" for r in bl["title_features"][:14]]
    L += ["", "| 주제 묶음 | 잘된 | 평소 | 차이 |", "|---|---|---|---|"] + [f"| {r['name']} | {_pct(r['hits'])} | {_pct(r['normal'])} | {_pct(r['diff'])} |" for r in bl["themes"][:10]]
    L += ["", "| 형식 | 잘된 | 평소 | 차이 |", "|---|---|---|---|"] + [f"| {r['name']} | {_pct(r['hits'])} | {_pct(r['normal'])} | {_pct(r['diff'])} |" for r in bl["formats"]]
    if bl["hit_examples"]:
        L += ["", "같은 채널에서 잘된 쇼츠 (채널 평소 대비 큰 순):", ""] + [
            f"- ×{x['channel_ratio']} · {_n(x['views'])}회 · {x['seconds']}초 · {_cell(x['channel'], 16)} — {_cell(x['title'], 70)} (https://www.youtube.com/shorts/{x['id']})"
            for x in bl["hit_examples"][:20]]
    if data.get("pair_pages"):
        L += ["", "성공 쇼츠와 같은 채널 평소 쇼츠 짝 (표지): " + ", ".join(f"[`{n}`]({n}) (#{a}~)" for n, a, _ in data["pair_pages"])]
    if data["missing_success"]:
        L += ["", f"### 1-3. 자료를 받지 않은 성공 후보 {data['missing_success_total']}개 (웹 화면 [쇼츠] 목록에서 승인하면 분석에 들어감 — 채널 자리가 찬 것 {data['missing_success_channel_full']}개는 뺌)", "",
              "| 제목 | 채널 | 구독자 | 조회수 | 배수 | 길이 | 올린 날 | 주제 |", "|---|---|---|---|---|---|---|---|"]
        L += [f"| [{_cell(x['title'], 50)}](https://www.youtube.com/shorts/{x['id']}) | {_cell(x['channel'], 16)} | {_n(x['subs'])} | {_n(x['views'])} | ×{x['ratio']} | "
              f"{x['seconds']}초 | {x['published']} | {_cell(x['theme'], 14)} |" for x in data["missing_success"][:20]]
    # 1-4·1-5 (v1.3)
    for top_, title_, pre, kname in ((data.get("vpd_top") or {}, "1-4. 하루 조회수 상위 쇼츠 — 구독자 상관없이 (최근 트렌드)", "V", "하루 조회수"),
                                     (data.get("views_top") or {}, "1-5. 조회수 상위 쇼츠 — 올린 날짜·구독자 상관없이 (최근 트렌드에 비슷한 과거 사례)", "T", "조회수")):
        if top_.get("threshold") is None:
            continue
        nk = pre.lower() + "no"
        L += ["", f"## {title_} ({len(top_['cases'])}개, {kname} 큰 순)", "",
              "경계 = 검색에서 찾은 주제 관련 쇼츠" + (f"(최근 {top_['max_age_days']:g}일 안)" if top_.get("max_age_days") else "(기간 없는 검색 포함)") +
              f" {top_['pool']:,}개(가장 오래된 {top_['oldest_days']}일) 중 {kname} 상위 {top_['pct']:g}% (**{_n(round(top_['threshold']))}{'회/일' if pre == 'V' else '회'} 이상**). "
              f"자료를 받은 쇼츠 중 넘은 것, 채널당 {top_['per_channel']}개 ({pre}# 번호) · 큰 채널 {top_['big_channels']}개 · 성공 쇼츠에도 든 것 {top_['in_success']}개 · "
              f"1년 넘은 것 {top_['older_than_year_cases']}개 · 기준 통과 {top_['passed']} − 뺀 것 {len(top_['excluded'])} − 채널당 제한 {top_['channel_cut']}.", "",
              f"| {pre}# | 제목 | 채널 | 구독자 | 조회수 | 하루 조회수 | 올린 지 | 길이 | 주제 | 형식 | 글 출처 | 성공 # |" + (" V# |" if pre == "T" else ""),
              "|---|---|---|---|---|---|---|---|---|---|---|---|" + ("---|" if pre == "T" else "")]
        for c in top_["cases"]:
            L.append(f"| {pre}{c[nk]} | [{_cell(c['title'], 50)}]({c['url']}) | {_cell(c['channel'], 16)} | {_n(c['subs'])} | {_n(c['views'])} | "
                     f"{_n(c['views_per_day'])} | {_n(c['age_days'])}일 | {c['seconds']}초 | {_cell(c['theme'], 12)} | {_cell(c['format'], 12)} | {c['text_source']} | "
                     f"{('#' + str(c['success_no'])) if c['success_no'] else ''} |" + ((f" {('V' + str(c['vno'])) if c.get('vno') else ''} |") if pre == "T" else ""))
        if top_["missing"]:
            L += ["", f"자료를 받지 않은 후보 {top_['missing_total']}개 중 {kname} 큰 {min(len(top_['missing']), 15)}개 (웹 화면 [쇼츠] 목록에서 승인하면 들어감):", ""] + [
                f"- {_n(x['views'])}회 · 하루 {_n(x['views_per_day'])}회 · {x['seconds']}초 · {x['published']} · {_cell(x['channel'], 16)} — {_cell(x['title'], 60)} "
                f"(https://www.youtube.com/shorts/{x['id']})" for x in top_["missing"][:15]]
        nd = top_.get("needs")
        if nd:
            L += ["", f"이 묶음의 시청자 니즈 (시청자 댓글 {nd['viewer_comments']:,}개 — 롱폼 8번과 같은 규칙):", "", "| 갈래 | 댓글 | 비율 | 좋아요 합 |", "|---|---|---|---|"]
            L += [f"| {r['name']} | {r['count']:,} | {_pct(r['share'])} | {r['likes']:,} |" for r in nd["categories"]]
            if nd.get("uncategorized"):
                u = nd["uncategorized"]
                L.append(f"| **어느 갈래에도 안 듦** | {u['count']:,} | {_pct(u['share'])} | {u['likes']:,} |")
    # 2
    L += ["", "## 2. 주제 묶음 · 형식 (비교 집단 성공 비율 · 성공 쇼츠 몫)", "", "| 주제 묶음 | 비교 집단 (성공 비율) | 조회수 중앙값 | 하루 조회수 중앙값 | 성공 쇼츠 몫 | 성공 쇼츠 # |", "|---|---|---|---|---|---|"]
    L += [f"| {r['theme']} | {_rate_txt(r)}{' (표본 적음)' if r['small_sample'] else ''} | {_n(r['views_median'])} | {_n(r['vpd_median'])} | "
          f"{sa._share_txt(r.get('success_share'), r.get('w_success_share'))} | {', '.join(map(str, r['success_cases'][:15])) or '–'} |" for r in data["themes"]]
    L += ["", "| 형식 | 비교 집단 (성공 비율) | 하루 조회수 중앙값 | 성공 쇼츠 몫 | 성공 쇼츠 # |", "|---|---|---|---|---|"]
    L += [f"| {r['format']} | {_rate_txt(r)}{' (표본 적음)' if r['small_sample'] else ''} | {_n(r['vpd_median'])} | {sa._share_txt(r['success_share'], r.get('w_success_share'))} | "
          f"{', '.join(map(str, r['success_cases'][:15])) or '–'} |" for r in data["formats"]]
    # 3
    mk = data["market"]
    L += ["", f"## 3. 수요와 공급 (최근 {mk['days']}일 쇼츠 {mk['videos']}개 — 쇼츠 검색으로 찾은 것, 채널 크기 상관없음)", "",
          "지수 = 하루 조회수 몫 ÷ 쇼츠 수 몫 (1 보다 크면 쇼츠 하나가 평균보다 많이 봄 = 공급이 모자라 보임)", "",
          "| 주제 묶음 | 쇼츠 | 채널 | 수요 몫 | 공급 몫 | 지수 | 하루 조회수 중앙값 |", "|---|---|---|---|---|---|---|"]
    L += [f"| {r['theme']} | {r['videos']} | {r['channels']} | {_pct(r['demand_share'])} | {_pct(r['supply_share'])} | **{r['index']}**"
          f"{' (표본 적음)' if r['small_sample'] else ''} | {_n(r['vpd_median'])} |" for r in mk["themes"]]
    L += ["", "검색어별 (쇼츠 검색 — videoDuration=short, 조회수 순 50개):", "",
          "| 검색어 | 찾음 | 그중 쇼츠 | 결과 수(4분 미만 추정) | 최근 30일 | 조회수 중앙값 | 하루 조회수 중앙값 | 큰 채널 몫 | 작은 채널 성공 | 지금 검색어 |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    L += [f"| {_cell(r['q'], 20)} | {r['found']} | {r['shorts']} ({_pct(r['shorts_share'])}) | {_n(r['total'])} | {r['recent30']} | {_n(r['views_median'])} | "
          f"{_n(r['vpd_median'])} | {_pct(r['big_share'])} | {r['small_success']}/{r['small_n']} | {'○' if r['current'] else ''} |" for r in mk["keywords"][:50]]
    L += ["", f"사람들이 찾는 말(YouTube 자동완성) 중 최근 쇼츠가 적은 말 — 틈 = 자동완성 점수 ÷ (1 + 최근 쇼츠 수), 전체 {mk['autocomplete_total']}개 중 위 {len(mk['autocomplete'])}개"
          + (" · 뺀 것: " + ", ".join(f"{k} {v}" for k, v in mk["autocomplete_excluded"].items()) if mk["autocomplete_excluded"] else ""), "",
          "| 말 | 자동완성 점수 | 씨앗 검색어 | 최근 쇼츠 | 하루 조회수 중앙값 | 틈 |", "|---|---|---|---|---|---|"]
    L += [f"| {_cell(r['phrase'], 30)} | {r['score']} | {_cell(', '.join(r['seeds']), 30)} | {r['shorts_recent']} | {_n(r['vpd_median'])} | {r['gap']} |"
          for r in mk["autocomplete"]]
    # 4
    L += ["", "## 4. 제목 · 해시태그 (비교 집단)", "", "| 제목 특징 | 있음 (성공 비율) | 없음 | 차이 | 성공 쇼츠 몫 |", "|---|---|---|---|---|"]
    L += [f"| {r['feature']} " + _cmp_line(r)[:-1] + f"| {sa._share_txt(r['success_case_share'], r.get('w_success_case_share'))} |" for r in data["title_features"]]
    if data["title_words_up"]:
        L += ["", "성공 비율이 높은 제목 낱말: " + ", ".join(f"{r['word']} ({_rate_txt(r['with'])} vs {_pct(r['without']['rate'])}{' ⚑' if r['notable'] else ''})"
                                                for r in data["title_words_up"])]
    if data["title_words_down"]:
        L += ["", "성공 비율이 낮은 제목 낱말: " + ", ".join(f"{r['word']} ({_rate_txt(r['with'])} vs {_pct(r['without']['rate'])})" for r in data["title_words_down"])]
    L += ["", "| 제목 길이 | 비교 집단 (성공 비율) | 하루 조회수 중앙값 | 성공 쇼츠 # |", "|---|---|---|---|"]
    L += [f"| {r['label']} | {_rate_txt(r)} | {_n(r['vpd_median'])} | {', '.join(map(str, r['success_cases'][:15])) or '–'} |" for r in data["title_length"]]
    L += ["", "| 해시태그 수 (제목+설명) | 비교 집단 (성공 비율) | 하루 조회수 중앙값 | 성공 쇼츠 # |", "|---|---|---|---|"]
    L += [f"| {r['label']} | {_rate_txt(r)} | {_n(r['vpd_median'])} | {', '.join(map(str, r['success_cases'][:15])) or '–'} |" for r in data["hashtag_count"]]
    if data["hashtags_top"]:
        L += ["", "많이 쓴 해시태그 (비교 집단 쇼츠 수 · 그 쇼츠의 성공 비율 · 성공 쇼츠 수): " +
              ", ".join(f"#{r['tag']} {r['compare_n']} ({_pct(r['rate'])}·{r['success_cases']})" for r in data["hashtags_top"])]
    # 5
    L += ["", "## 5. 길이 (초)", "", f"- 중앙값: 성공 쇼츠 {_sec(data['engagement']['success_cases']['seconds_median'])} · 비교 집단 성공 {_sec(data['engagement']['success']['seconds_median'])} · "
          f"나머지 {_sec(data['engagement']['others']['seconds_median'])}", "", "| 길이 | 비교 집단 (성공 비율) | 하루 조회수 중앙값 | 성공 쇼츠 # |", "|---|---|---|---|"]
    L += [f"| {r['label']} | {_rate_txt(r)}{' (표본 적음)' if r['small_sample'] else ''} | {_n(r['vpd_median'])} | {', '.join(map(str, r['success_cases'][:15])) or '–'} |"
          for r in data["seconds"]]
    tn = data["tiny"]
    L += ["", f"### 5-2. 아주 짧은 쇼츠 ({TINY_SECONDS}초 미만 — 한 장 정보·반복 재생형?) — 주제 관련 쇼츠 전부 (조회수 부풀림 의심 포함)", "",
          "조회수는 2025-03-31 부터 다시 재생도 셈 → 아주 짧은 쇼츠는 한 사람이 여러 번 셀 수 있다. 광고로 산 조회수와 API 로 가를 수 없다", "",
          "| 묶음 | 쇼츠 | 그중 부풀림 의심 | 채널 | 조회수 중앙값 | 좋아요/1천 | 길이 중앙값 |", "|---|---|---|---|---|---|---|"]
    for k, nm in (("tiny", f"{TINY_SECONDS}초 미만"), ("rest", f"{TINY_SECONDS}초 이상")):
        r = tn[k]
        L.append(f"| {nm} | {r['n']} | {r['inflated']} | {r['channels']} | {_n(r['views_median'])} | {_n(r['likes_per_1k'])} | {_sec(r['seconds_median'])} |")
    if tn["examples"]:
        L += ["", f"{TINY_SECONDS}초 미만 쇼츠 (조회수 순):", ""] + [
            f"- {x['seconds']}초 · {_n(x['views'])}회 · 좋아요/1천 {x['likes_per_1k']} · 구독자 {_n(x['subs'])} · {_cell(x['channel'], 16)}"
            f"{' · 부풀림 의심' if x['inflated'] else ''} — {_cell(x['title'], 70)} (https://www.youtube.com/shorts/{x['id']})" for x in tn["examples"]]
    # 6·7
    sp = data["speech"]
    a, b = sp["success"], sp["others"]
    L += ["", "## 6. 첫 3초 · 7. 말과 끝맺음 (자료를 받은 쇼츠 — 대본이 있는 것)", "",
          f"성공 쇼츠 {a['n']}개 (대본 {a['with_script']} · 말 없음 {a['no_speech']}) vs 나머지 받은 쇼츠 {b['n']}개 (대본 {b['with_script']} · 말 없음 {b['no_speech']}) — 중앙값·몫", "",
          "| 항목 | 성공 쇼츠 | 나머지 받은 쇼츠 |", "|---|---|---|",
          f"| 첫 말까지 걸린 시간 | {a['first_speech_sec'] if a['first_speech_sec'] is not None else '–'}초 | {b['first_speech_sec'] if b['first_speech_sec'] is not None else '–'}초 |",
          f"| 첫 3초 안 음절 | {_n(a['syl_first3'])} | {_n(b['syl_first3'])} |",
          f"| 말 속도 (음절/초, 말하는 구간) | {_n(a['syl_per_sec'])} | {_n(b['syl_per_sec'])} |",
          f"| 말이 차지한 비율 | {_pct(a['coverage'])} | {_pct(b['coverage'])} |",
          f"| 자막 줄 수 | {_n(a['lines'])} | {_n(b['lines'])} |",
          f"| 말 없는 쇼츠 (음악·화면 글자만) | {_pct(a['no_speech_share'])} | {_pct(b['no_speech_share'])} |"]
    L += [f"| 첫 줄: {k} | {_pct(a['hook_types'].get(k))} | {_pct(b['hook_types'].get(k))} |" for k in HOOK_TYPES]
    L += [f"| 첫 줄: 위 유형 없음 | {_pct(a['hook_none'])} | {_pct(b['hook_none'])} |"]
    L += [f"| 끝 줄: {k} | {_pct(a['ending_types'].get(k))} | {_pct(b['ending_types'].get(k))} |" for k in ENDING_TYPES]
    L += [f"| 끝 줄: 위 유형 없음 | {_pct(a['ending_none'])} | {_pct(b['ending_none'])} |",
          f"| 끝 줄이 문장 끝맺음(다·요·까…) 없이 끝남 | {_pct(a['ends_open'])} | {_pct(b['ends_open'])} |"]
    ll = data["long_link_share"]
    L += ["", f"- 설명란에 롱폼·풀영상 연결(유튜브 영상 주소·'풀영상'·'본편'): 성공 쇼츠 {_pct(ll['success'])} · 나머지 받은 쇼츠 {_pct(ll['others'])} · "
          f"비교 집단 성공 {_pct(ll['compare_success'])} · 나머지 {_pct(ll['compare_others'])}", "", "성공 쇼츠의 첫 줄·끝 줄 (원문):", ""]
    for c in data["success_cases"]:
        if c["first_line"]:
            L.append(f"- #{c['no']} ({c['seconds']}초, 첫 말 {c['first_speech_sec']}초) 첫: “{_cell(c['first_line'], 80)}” → 끝: “{_cell(c['last_line'], 80)}”"
                     + (f" [{', '.join(c['hook_types'] or [])}]" if c["hook_types"] else ""))
    # 8
    e = data["engagement"]
    L += ["", "## 8. 참여율 (조회수 1,000회당 — 중앙값)", "", "| 묶음 | 수 | 좋아요/1천 | 댓글/1천 | 하루 조회수 |", "|---|---|---|---|---|",
          f"| 비교 집단 성공 | {e['success']['n']} | {e['success']['likes_per_1k']} | {e['success']['comments_per_1k']} | {_n(e['success']['vpd_median'])} |",
          f"| 비교 집단 나머지 | {e['others']['n']} | {e['others']['likes_per_1k']} | {e['others']['comments_per_1k']} | {_n(e['others']['vpd_median'])} |",
          f"| 성공 쇼츠 (받은 것) | {e['success_cases']['n']} | {e['success_cases']['likes_per_1k']} | {e['success_cases']['comments_per_1k']} | {_n(e['success_cases']['vpd_median'])} |"]
    # 9
    L += ["", "## 9. 올린 요일 · 시각 (한국 시간 — 비교 집단, 표본이 작으면 흔들림)", "", "| 요일 | 비교 집단 (성공 비율) | 성공 쇼츠 # |", "|---|---|---|"]
    L += [f"| {r['label']} | {_rate_txt(r)}{' (표본 적음)' if r['small_sample'] else ''} | {', '.join(map(str, r['success_cases'][:12])) or '–'} |" for r in data["weekdays"]]
    L += ["", "| 시각 | 비교 집단 (성공 비율) | 성공 쇼츠 # |", "|---|---|---|"]
    L += [f"| {r['label']} | {_rate_txt(r)}{' (표본 적음)' if r['small_sample'] else ''} | {', '.join(map(str, r['success_cases'][:12])) or '–'} |" for r in data["hours"]]
    # 10
    L += ["", "## 10. 채널 유형 · 빨리 크는 쇼츠 채널", "", "채널 유형 = 채널 쇼츠 수(UUSH 목록) ÷ 채널 영상 수. "
          f"채널 쇼츠 수를 모르는 비교 집단 쇼츠 {data.get('channel_types_unknown', 0):,}개는 비율에서 뺐다 (평소 쇼츠는 승인한 쇼츠의 채널만 받으므로 "
          "모르는 채널은 거의 다 성공이 아님 — 넣으면 '쇼츠만 하는 채널'이 잘 되는 것처럼 보임). 아래도 승인한 쇼츠의 채널 쪽으로 치우쳐 있다", "",
          "| 채널 유형 | 비교 집단 (성공 비율) | 채널 | 성공 쇼츠 # |", "|---|---|---|---|"]
    L += [f"| {r['type']} | {_rate_txt(r)}{' (표본 적음)' if r['small_sample'] else ''} | {r['channels']} | {', '.join(map(str, r['success_cases'][:12])) or '–'} |"
          for r in data["channel_types"]]
    g = data["growth"]
    if g["fast"]:
        L += ["", f"빨리 크는 쇼츠 채널 (개설 {data['rules']['growth']['NEW_CHANNEL_MONTHS']}개월 안·구독자 {data['rules']['growth']['MIN_SUBS']:,}~"
              f"{data['rules']['growth']['MAX_SUBS']:,}·쇼츠 몫 50% 이상 — 월 구독자 증가 순, {g['channels']}곳 중):", "",
              "| 채널 | 개설 | 구독자 | 월 구독자 증가 | 영상 수 | 쇼츠 몫 | 본 쇼츠 길이 중앙값 | 주로 다룬 주제 | 대표 쇼츠 |", "|---|---|---|---|---|---|---|---|---|"]
        L += [f"| {_cell(r['channel'], 18)} | {r['created']} | {_n(r['subs'])} | {_n(r['subs_per_month'])} | {_n(r['videos'])} | {_pct(r['shorts_share'])} | "
              f"{_sec(r['seconds_median'])} | {_cell(', '.join(r['themes']), 24)} | [{_cell(r['best']['title'], 30)}](https://www.youtube.com/shorts/{r['best']['id']}) {_n(r['best']['views'])}회 |"
              for r in g["fast"]]
    # 11
    nd = data["needs"]
    L += ["", f"## 11. 시청자 니즈 (성공 쇼츠 댓글 — 시청자 댓글 {nd['viewer_comments']:,}개, 도배 {nd['spam_excluded']}개 뺌, 채널 주인 댓글 뺌, 정보 요청이 아닌 부탁(띠·로또·노래 등) {nd.get('not_info_asks', 0)}개는 질문·요청에서 뺌)", "",
          "| 갈래 | 댓글 | 몫 | 좋아요 합 |", "|---|---|---|---|"]
    L += [f"| {r['name']} | {r['count']:,} | {_pct(r['share'])} | {r['likes']:,} |" for r in nd["categories"]]
    L += ["", f"### 11-1. 요청 — '다뤄 주세요·알려 주세요' {nd['requests_total']}개 (다음 쇼츠·롱폼 주제 후보)", ""]
    L += [f"- #{q['no']} 👍{q['likes']} “{_cell(q['text'], 160)}”" for q in nd["requests"]] or ["- (없음)"]
    L += ["", f"### 11-2. {CAT_MORE}", ""] + ([f"- #{q['no']} 👍{q['likes']} “{_cell(q['text'], 160)}”" for q in nd["top"].get(CAT_MORE, [])] or ["- (없음)"])
    L += ["", "### 11-3. 물음표 질문", ""] + ([f"- #{q['no']} 👍{q['likes']} “{_cell(q['text'], 160)}”" for q in nd["questions"]] or ["- (없음)"])
    L += ["", "### 11-4. 아쉬운 점 — 영상", ""] + ([f"- #{q['no']} 👍{q['likes']} “{_cell(q['text'], 160)}”" for q in nd["complaints"]] or ["- (없음)"])
    for k in (sa.CAT_GOOD, sa.CAT_EXP, sa.CAT_SUB):
        L += ["", f"### 11-x. {k}", ""] + ([f"- #{q['no']} 👍{q['likes']} “{_cell(q['text'], 140)}”" for q in nd["top"].get(k, [])] or ["- (없음)"])
    # 12
    L += ["", "## 12. 사례별 · 표지", ""]
    if data.get("case_pages"):
        L += ["사례별 (대본 전문·첫 3초·끝 줄·설명·댓글): " + ", ".join(f"[`{n}`]({n}) (#{a}~#{z})" for n, a, z in data["case_pages"])]
    if data.get("thumb_pages"):
        L += ["", "성공 쇼츠 표지 (번호 = 1번 표의 #): " + ", ".join(f"[`{n}`]({n}) (#{a}~#{z})" for n, a, z in data["thumb_pages"])]
    L += ["", "받은 쇼츠 전부 (업로드 최근 순·글 출처·댓글): [`approved.md`](approved.md) · 비교 집단 숫자: [`compare.csv`](compare.csv)", ""]
    _write_atomic(Path(out) / "analysis.md", "\n".join(L) + "\n")


def write_cases_pages(out, data, per=15):
    pages = []
    cs = data["success_cases"]
    for k in range(0, len(cs), per):
        chunk = cs[k:k + per]
        name = f"cases_{k // per + 1:02d}.md"
        L = [f"# 성공 쇼츠 사례별 #{chunk[0]['no']}~#{chunk[-1]['no']} — {data['name']}", "", "숫자·원문만 (해석 없음). ※ 연구·교육용.", ""]
        for c in chunk:
            L += [f"## #{c['no']}. {_cell(c['title'], 90)}", "",
                  f"- {c['url']} · {c['channel']} · 구독자 {_n(c['subs'])} · 조회수 {_n(c['views'])} (×{c['ratio']}"
                  + (f" · 채널 평소 쇼츠 대비 ×{c['channel_ratio']}" if c["channel_ratio"] is not None else "") + f") · 하루 {_n(c['views_per_day'])}회 · "
                  f"{c['seconds']}초 · 올린 때 {c['published'][:16].replace('T', ' ')} ({c['weekday']}) · 좋아요/1천 {c['likes_per_1k']} · 댓글/1천 {c['comments_per_1k']}",
                  f"- 주제 {c['theme']} · 형식 {c['format']} · 글 출처 {c['text_source']} · 쇼츠 판별 {c['short_basis']} · 해시태그 "
                  + (" ".join("#" + h for h in c["hashtags"]) or "없음") + (" · 설명란에 롱폼 연결" if c["long_link"] else ""),
                  f"- 설명: {_cell(c['description'], 300) or '(없음)'}"]
            if c["first_line"]:
                L += [f"- 첫 말 {c['first_speech_sec']}초 · 첫 3초 음절 {c['syl_first3']} · 말 속도 {c['syl_per_sec']} 음절/초 · 말이 차지한 비율 {_pct(c['coverage'])}",
                      f"- 첫 3초: “{_cell(c['first3'], 160)}” · 첫 줄 유형: {', '.join(c['hook_types'] or []) or '–'}",
                      f"- 끝 줄: “{_cell(c['last_line'], 160)}” · 끝 줄 유형: {', '.join(c['ending_types'] or []) or '–'}{' · 끝맺음 없이 끝남' if c['ends_open'] else ''}",
                      "", "대본 전문:", "", "> " + (_cell(c["text"], 1500) or "(없음)")]
            if c["normal_pairs"]:
                L += ["", "같은 채널 평소 쇼츠: " + "; ".join(f"{_cell(x['title'], 50)} ({_n(x['views'])}회)" for x in c["normal_pairs"])]
            if c["need_quotes"]:
                L += ["", f"댓글 (받은 {c['comments_fetched']:,} / 달린 {c['comments_total']:,}):"]
                for cat, qs in c["need_quotes"].items():
                    L += [f"- {cat.split(' (')[0]}: " + " / ".join(f"👍{q['likes']} “{_cell(q['text'], 120)}”" for q in qs)]
            L.append("")
        _write_atomic(Path(out) / name, "\n".join(L) + "\n")
        pages.append((name, chunk[0]["no"], chunk[-1]["no"]))
    keep = {n for n, _, _ in pages}
    for f in Path(out).glob("cases_*.md"):
        if f.name not in keep:
            f.unlink()
    return pages


def write_approved(out, data):
    L = [f"# 받은 쇼츠 전부 — {data['name']} ({len(data['approved'])}개, 업로드 최근 순)", "",
         "웹 화면 [쇼츠]에서 승인해 자료(설명·자막·표지·댓글 전부)를 받은 쇼츠. 폴더 `S_<영상ID>` 에 원문. ※ 연구·교육용.", "",
         "| 올린 날 | 제목 | 채널 | 구독자 | 조회수 | 배수 | 채널 평소 대비 | 길이 | 성공 # | 뺀 까닭 | 글 출처 | 댓글 | 폴더 |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in data["approved"]:
        L.append(f"| {r['published']} | [{_cell(r['title'], 44)}](https://www.youtube.com/shorts/{r['id']}) | {_cell(r['channel'], 14)} | {_n(r['subs'])} | "
                 f"{_n(r['views'])} | {('×' + str(r['ratio'])) if r['ratio'] is not None else '–'} | {('×' + str(r['channel_ratio'])) if r['channel_ratio'] is not None else '–'} | "
                 f"{r['seconds']}초 | {r['success_no'] or ''} | {_cell(r['exclude'], 20)} | {r['text_source']} | {r['comments']:,}{'' if r['comments_complete'] else ' (덜 받음)'} | "
                 f"[`{r['folder']}`]({r['folder']}) |")
    _write_atomic(Path(out) / "approved.md", "\n".join(L) + "\n")


def write_compare_csv(out, rows):
    fields = ["id", "title", "channel", "subs", "views", "ratio", "seconds", "age_days", "published", "weekday", "hour", "theme", "format",
              "hashtags", "is_short", "short_basis", "channel_type", "success", "in_compare", "has_case", "exclude"]
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=fields, extrasaction="ignore")
    w.writeheader()
    for x in sorted(rows, key=lambda x: (not x.get("in_compare"), -(x.get("views") or 0))):
        w.writerow({**x, "published": x["published"].date().isoformat() if x.get("published") else "", "hashtags": " ".join(x.get("hashtags") or [])})
    _write_atomic(Path(out) / "compare.csv", "﻿" + buf.getvalue())


# ---------------------------------------------------------------- 실행
def run(topic, now=None, root=None, fetch_thumbs=True):
    root = Path(root or ROOT)
    now = now or datetime.now(timezone.utc)
    out_all = root / topic / "result" / "outliers"
    sdir, cache = shorts_out(root, topic), shorts_cache(root, topic)
    cfg = sa._toml(root / topic / "analyzer_config.toml")
    name = (cfg.get("topic") or {}).get("TOPIC") or cfg.get("TOPIC") or topic
    rules, rel, themes = load_rules(root, topic), sa.load_rel(root, topic), sa.load_themes(root, topic)
    infos, uploads, searches = load_shorts_cache(cache)
    channels, ac = load_main_cache(out_all)
    subs_map = {k: v.get("subs") for k, v in channels.items()}
    known = {i for u in uploads.values() for i in u["ids"]}
    cases = load_cases(sdir, infos, subs_map, now, known)
    log("START", topic=topic, cases=len(cases), cache_videos=len(infos), channel_lists=len(uploads), searches=len(searches),
        channels=len(channels), rules=rules["file"], shorts_rules="기본값" if rules["shorts_defaults"] else "파일", tool=f"shorts_analysis.py {VERSION}")
    if not cases and not infos:
        log("DONE", topic=topic, note="쇼츠 자료 없음 — 웹 화면 [쇼츠]에서 탐색·승인한 뒤 다시 (아무것도 쓰지 않음)")
        return None
    alltime = sa.load_alltime_ids(cache, dur="short") - {i for d in searches for i in (d.get("ids") or [])}     # v1.3
    data, success, group, rows_all, cases = analyze(topic, name, cases, infos, uploads, searches, channels, ac, rules, rel, themes, now, alltime_ids=alltime)
    sdir.mkdir(parents=True, exist_ok=True)
    data["thumb_pages"] = paged_v([(c["no"], sdir / c["thumb"] if c["thumb"] else None) for c in success], sdir, "thumbs")
    if fetch_thumbs and data["baseline"]["pairs"]:
        fetch_pair_covers(cache, data["baseline"]["pairs"])
    items = []
    for pr in data["baseline"]["pairs"]:
        items += [(pr["no"], sdir / pr["thumb"] if pr["thumb"] else None)] + \
                 [(f"#{pr['no']}-{'ab'[k]}", Path(x["thumb"]) if x.get("thumb") else None) for k, x in enumerate((pr["normal"] + [{}, {}])[:2])]
    data["pair_pages"] = paged_v(items, sdir, "thumbs_pairs", per=30, cols=6)
    for pr in data["baseline"]["pairs"]:                                       # PC 경로는 json 에 남기지 않음
        for x in pr["normal"]:
            x["thumb"] = bool(x.get("thumb"))
    data["case_pages"] = write_cases_pages(sdir, data)
    log("THUMBS", success=sum(1 for c in success if c["thumb"]), pages=len(data["thumb_pages"]), pair_pages=len(data["pair_pages"]))
    write_md(sdir, data, success)
    write_approved(sdir, data)
    _write_atomic(sdir / "analysis.json", json.dumps(data, ensure_ascii=False, indent=1, default=str))
    write_compare_csv(sdir, rows_all)
    log("WRITE", file=str(sdir / "analysis.md"), success=len(success), compare=len(group), missing=data["missing_success_total"],
        case_pages=len(data["case_pages"]))
    log("DONE", topic=topic, success=len(success), compare_rate=data["sources"]["compare_rate"],
        text_sources=",".join(f"{k}:{v}" for k, v in data["sources"]["text_sources"].items()) or "-")
    return data


def main(argv=None):
    ap = argparse.ArgumentParser(description="쇼츠 분석 — 성공 쇼츠·같은 채널 기준선·주제·길이·첫 3초·끝 문장·시청자 니즈 (AI 가 쇼츠 지시사항을 만들 재료, 할당량 0)")
    ap.add_argument("topic")
    ap.add_argument("--no-thumbs", action="store_true", help="같은 채널 평소 쇼츠 표지 그림을 받지 않음")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args(argv)
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass
    logging.basicConfig(level=getattr(logging, a.log_level), format="%(message)s", stream=sys.stdout)
    run(a.topic, fetch_thumbs=not a.no_thumbs)
    return 0


if __name__ == "__main__":
    sys.exit(main())
