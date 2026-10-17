#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.9 — 2026-10-17 — 자막은 **2줄까지** (사용자 지시 2026-10-17 "그리고 자막은 2줄까지만 표시되도록 해"): 'shorts_cover'(쇼츠 첫 문장 — 썸네일 그림 위)를 3줄 → **글자 42px·2줄**
#          (kit.css #cc.cover — 나머지 자막은 46px 그대로). 2줄에 들어가면 줄바꿈 점수와 상관없이 자막 하나 ('one') — 그림이 자막 하나 동안만.
#          3줄 찾기를 지움. check: 쇼츠 첫 문장이 자막 2개면 문제 (그림이 둘째 자막까지 남음).
# (v1.8 — 2026-10-17 — 쇼츠 첫 문장(썸네일 그림 위 — kit.js K.cover)은 자막 하나에 3줄까지 ('shorts_cover'): 그 문장이 자막 2개로
#          나뉘면 두 번째 자막 동안에도 그림이 남아 '다음 문장으로 넘어가도 썸네일이 보임' (사용자 지시 2026-10-17 "영상에서 첫 문장만 왜 다른 문장
#          넘어가서도 썸네일 이미지가 영상에 뜨면 어떻게 그것도 수정해"). 줄바꿈 뜻 점수를 _break_pen 으로 뗌 (예전 결과 같음).)
# (v1.7 — 2026-10-17 — 한 문장 = 자막 하나 (사용자 지시 2026-10-17 "자막 좀 되도록 한 문장은 한 자막으로 표시되게해 길지 않은 문장도
#          잘라서 자막 띄우잖아 문장이 길면 적당한 곳에 분리하도록 해서 반영해"): 자막 모양(LAYOUTS)을 화면에 굽는 띠 그대로 재서
#          — 롱폼 52px·한 줄 1500px, 세로 쇼츠 46px·816px — 한 줄에 안 들어가면 **같은 자막 안에서 두 줄**(쉼표·절 경계에서 줄바꿈),
#          두 줄로도 안 들어갈 때만 자막 2개로 나눈다. 주식(stock/ — 자막을 굽지 않음)은 예전 한 줄 규칙 그대로(layout 'line').
#          build --reuse 는 같은 문장의 옛 길이(자막 여러 개면 합)를 그대로 쓰고 나눔은 새 규칙으로 다시. check·measure 도 같은 규칙.)
# (v1.6.1 — 2026-10-14 — 문서 경로만 고침: 옛 대본 지시사항이 guides/archive/script_guide_v1.md 로 옮겨짐 (동작 같음))
# (v1.6 — 2026-10-12 — check 사연 길이: 이미 올린 영상(youtube.json 있음)은 SRT가 실제 오디오 시간이므로 음절 추정 대신
#          실측(진행자 첫 문장 시작 ≤ 0:30)으로 판정 — 스튜디오에서 사연을 잘라 낸 영상(tools/studio_trim.py)에 맞춤)
# (v1.5 — 2026-10-12 — check 에 사연 길이 항목: 사연 파트 읽는 음절 85~125(약 20~30초)를 넘으면 ❌ (사용자 지시: 사연은 짧지만 강렬하게))
#          (v1.4: 파트 라벨 판정 수정: '-숫자'(음수 금액)로 시작하는 줄은 문장)
#          (v1.3: 자막 한 줄 1432px, 앞줄·뒷줄 자막, 고지 공백 SRT 안, 문장 번호 기준 내보내기)
#          (v1.2: upload 챕터, v1.1: remotion 내보내기, v1.0: TXT → SRT 생성·검사)
r"""
대본 TXT로 SRT 자막을 만들거나, TXT와 SRT가 지시사항대로 맞는지 검사합니다. (표준 라이브러리만 사용)

  python tools/srt_tool.py check <대본.txt> <자막.srt> [--expect 91/117]       # 문장 / 자막 / SRT–TXT 일치 / 고지 공백 / 사연 길이
  python tools/srt_tool.py build <대본.txt> <새.srt> [--reuse <기존.srt>]       # 대본으로 SRT 만들기 (타이밍은 추정치)
  python tools/srt_tool.py remotion <대본.txt> <자막.srt> video/src/episodes/<영상ID>/subtitles.ts [--audio-seconds 512.3 --audio-file audio/<영상ID>.mp3]
  python tools/srt_tool.py upload <대본.txt> <자막.srt> --chapters "1=사연;15=왜 물타기를 할까"   # 챕터 시간 (문장 번호 기준)
  python tools/srt_tool.py measure <대본.txt>                                   # 문장별 자막 줄·나뉠 문장
  (build·check·measure 의 --layout long|shorts|line — 없으면 경로로: stock/ = line, <영상ID>-shorts.txt = shorts, 그 밖 = long)

자막 규칙 (guides/archive/script_guide_v1.md 5-2 — 새 대본은 guides/script_guide.md 5번, guides/video_guide.md 3-3)
  - 번호: 장면·챕터는 대본 문장 번호(TXT에서 라벨·[장면]·카드 문구를 뺀 줄 순서)로 센다. SRT 번호와 다르다.
  - 한 문장 = 자막 하나 (v1.7): 화면에 굽는 띠의 글자 크기·폭(LAYOUTS)으로 재서 한 줄에 들어가면 한 줄,
    넘으면 같은 자막 안에서 두 줄(줄바꿈 = 쉼표·절 경계·조사 뒤, 두 줄 폭이 비슷하게). 두 줄로도 넘을 때만
    자막 2개(각각 두 줄까지)로 나눠 차례로 보여 준다. 숫자와 단위·날짜·범위는 한 줄에.
    (주식 stock/ 은 자막을 굽지 않으므로 예전 규칙 'line' — 46px 1432px 한 줄, 넘으면 앞줄·뒷줄 자막 2개)
  - 고지 카드: [장면] 바로 앞 문장 뒤에 최소 3.5초 공백을 SRT 안에 둔다. 영상 코드는 자막을 밀지 않고 그 공백에 카드를 보여 준다.
  - 그 밖에는 자막 사이 빈 시간 없음 (첫 자막 앞 2초 이내 여백은 허용 — 내레이션 시작 전 숨)
  - SRT = 영상 시간: 영상의 자막 시간은 SRT 타임코드 그대로다. 업로드용 SRT를 따로 만들지 않는다.
  - build 의 타이밍은 추정치(읽는 음절 ÷ 5.2 + 0.35초 + 쉼표당 0.2초). 내레이션을 녹음하면 video/ 에서
    npm run align-audio 로 오디오에 맞춘다 (오디오는 고치지 않음).
  - --reuse: 글자가 같은 문장은 기존 SRT의 길이(자막이 여러 개였으면 합)를 그대로 쓰고, 나눔·줄바꿈은 지금 규칙으로 다시 정한다.
"""
import argparse
import json
import re
import sys
from pathlib import Path

SYL_PER_SEC = 5.2
PAUSE_SEC = 0.35
COMMA_SEC = 0.2
SENT_MAX = 50
SUB_FONT_PX = 46            # 예전 자막 글자 크기 (layout 'line' — Remotion 시절 video_guide 3-3)
LINE_MAX_PX = 1432          # 예전 자막 한 줄 최대 폭 = 띠 최대 1500px − 좌우 안쪽 여백 34px×2
# v1.7 자막 모양 = 화면에 굽는 띠 (video/render/kit.css #cc · 쇼츠 장면 파일 #cc). width 는 띠 안쪽 폭보다 조금 좁게 (글꼴 반올림 여유)
LAYOUTS = {
    "long":   {"px": 52, "width": 1500, "lines": 2, "desc": "롱폼 1920×1080 — kit.css #cc 52px, 띠 최대 1600 − 안쪽 여백 32×2 = 1536px"},
    "shorts": {"px": 46, "width": 816, "lines": 2, "desc": "세로 쇼츠 — 장면 #cc 46px, 띠 최대 870(안전 구역 x 60~930) − 안쪽 여백 16×2 = 838px"},
    "shorts_cover": {"px": 42, "width": 816, "lines": 2, "one": True,
                     "desc": "세로 쇼츠 첫 문장 (썸네일 그림 위 — v1.9: 글자 42px(kit.css #cc.cover)로 2줄 안에 자막 하나, 그림이 자막 하나 동안만)"},
    "line":   {"px": SUB_FONT_PX, "width": LINE_MAX_PX, "lines": 1, "desc": "예전 한 줄 자막 (주식 stock/ — 자막을 굽지 않음, 문장 시각용)"},
}
CARD_GAP_MIN = 3.5          # 고지 카드 공백 최소 (초)
LEAD_IN_MAX = 2.0           # 첫 자막 앞 여백 허용 (초)
EPS = 0.0015
# 사연 길이 (사용자 지시 2026-10-12, guides/archive/script_guide_v1.md 0-1의 13번 — 사연 파트가 있을 때만): 사연자 실측 4.3~4.6 읽는 음절/초(문장 사이 쉼 포함,
# 주식 4개 영상 tts_narration.json) → 125음절 ≈ 27~29초, 85음절 ≈ 19~20초
STORY_WORD = "사연"         # 파트 라벨에 이 낱말이 있으면 사연 파트 (voices/storyteller.json 의 parts 와 같음)
STORY_SYL_MAX = 125
STORY_SYL_MIN = 85
STORY_RATE = 4.4            # 추정 초 = 읽는 음절 ÷ 이 값
STORY_HOST_MAX = 30.0       # 올린 영상(실측): 진행자 첫 문장이 이 시각(초) 안에 시작

_DIG = "영일이삼사오육칠팔구"
_NATIVE = {1: "한", 2: "두", 3: "세", 4: "네", 5: "다섯", 6: "여섯", 7: "일곱", 8: "여덟", 9: "아홉"}
_NATIVE_TENS = {1: "열", 2: "스물", 3: "서른", 4: "마흔", 5: "쉰", 6: "예순", 7: "일흔", 8: "여든", 9: "아흔"}
_NATIVE_COUNTERS = ("살", "시간", "개", "명", "마리", "군데", "곳")
_LETTERS = {"A": "에이", "B": "비", "C": "씨", "D": "디", "E": "이", "F": "에프", "G": "지", "H": "에이치", "I": "아이",
            "J": "제이", "K": "케이", "L": "엘", "M": "엠", "N": "엔", "O": "오", "P": "피", "Q": "큐", "R": "알", "S": "에스",
            "T": "티", "U": "유", "V": "브이", "W": "더블유", "X": "엑스", "Y": "와이", "Z": "지", "&": "앤"}


def sino(n):
    """한자어 수 읽기 (예: 2025 → 이천이십오, 1500 → 천오백). 1은 단위 앞에서 생략."""
    if n == 0:
        return "영"
    out = []
    for unit_val, unit in ((10 ** 12, "조"), (10 ** 8, "억"), (10 ** 4, "만"), (1, "")):
        chunk, n = divmod(n, unit_val)
        if chunk:
            s = ""
            for v, name in ((1000, "천"), (100, "백"), (10, "십"), (1, "")):
                d, chunk = divmod(chunk, v)
                if d:
                    s += ("" if d == 1 and name else _DIG[d]) + name
            out.append(s + unit)
    return "".join(out)


def native(n):
    t, o = divmod(n, 10)
    return (_NATIVE_TENS.get(t, "") + _NATIVE.get(o, "")) or sino(n)


def spoken(text):
    """읽는 소리로 바꾼 문자열 (음절 수 계산용 — 정확한 맞춤법이 목적이 아님)."""
    s = text
    s = re.sub(r"[A-Za-z&]+", lambda m: "".join(_LETTERS.get(c.upper(), "") for c in m.group()), s)
    s = re.sub(r"-(?=\d)", "마이너스", s)
    s = re.sub(r"\+(?=\d)", "플러스", s)

    def num(m):
        whole, frac, after = m.group(1).replace(",", ""), m.group(2), s_after(m)
        n = int(whole)
        if not frac and 0 < n < 100 and after.startswith(_NATIVE_COUNTERS):
            return native(n)
        r = sino(n)
        if frac:
            r += "점" + "".join(_DIG[int(c)] for c in frac[1:])
        return r

    def s_after(m):
        return m.string[m.end():m.end() + 3]
    s = re.sub(r"(\d[\d,]*)(\.\d+)?", num, s)
    s = s.replace("%", "퍼센트").replace("$", "달러")
    return s


def syllables(text):
    return len(re.findall(r"[가-힣]", spoken(text)))


def duration(text):
    return syllables(text) / SYL_PER_SEC + PAUSE_SEC + COMMA_SEC * text.count(",")




# ----------------------------------------------------------------------------- 글자 폭 (자막 폰트)
_WT = json.loads((Path(__file__).with_name("subtitle_widths.json")).read_text("utf-8"))
_W = {int(k): v for k, v in _WT["widths"].items()}


def layout_of(txt):
    """대본 경로로 자막 모양: stock/ = 'line'(자막을 굽지 않음), <영상ID>-shorts.txt = 'shorts', 그 밖 = 'long'."""
    p = Path(txt).resolve()
    if "stock" in p.parts:
        return "line"
    return "shorts" if p.name.endswith("-shorts.txt") else "long"


def text_px(text, px=SUB_FONT_PX):
    """Noto Sans KR 700 으로 쓴 글자 폭(px, 글자 크기 px). 표: tools/subtitle_widths.json (make_width_table.py)"""
    units = 0
    for ch in text:
        c = ord(ch)
        units += _WT["hangul_syllables"] if 0xAC00 <= c < 0xD7A4 else _W.get(c, _WT["default"])
    return units * px / _WT["units_per_em"]


_CLAUSE_END = re.compile(r"(,|고|고도|서|면|니까|니|며|지만|는데|는데도|듯이|자|자마자|해도|어도|아도|려고|도록)$")   # 절 경계
_PARTICLE_END = re.compile(r"(은|는|이|가|을|를|에|에서|으로|로|도|만|까지)$")                        # 어절 끝 조사 (와·과는 "A와 / B"처럼 짝이 갈려서 뺌)
_ADJ_SHORT = {"많은", "좋은", "작은", "큰", "높은", "낮은", "같은", "다른", "오랜", "어린", "젊은", "늦은", "빠른", "긴", "짧은", "적은", "나쁜", "새"}
_AFTER_NUM = {"이상", "이하", "미만", "정도", "가까이", "넘게", "이내", "사이", "사이인", "전후", "만에", "동안", "안에", "뒤", "후"}
_NO_END_WORDS = {"제", "내", "그", "이", "저", "한", "두", "세", "네", "몇", "새", "왜", "더", "안", "못", "잘", "꼭", "다", "좀", "또"}




_FIXED_NEXT = {"따라", "따른", "대해", "대한", "의해", "의한", "관해", "관한", "비해", "비하면", "위해", "위한", "통해", "통한", "맞춰", "맞춘",
               "합쳐", "합치면", "합해", "합하면"}   # 'X에 따라'·'둘이 합쳐'처럼 붙은 말
_DEP_NOUN = ("법", "적", "데", "뿐", "만큼", "대로", "채", "듯", "척", "덕분", "탓")   # '고치는 법'·'본 적'처럼 꾸밈말 뒤 의존명사


_DEP_NEXT = {"걸", "거", "건", "거예요", "거예요.", "거죠", "거죠.", "걸요", "걸요.", "겁니다", "겁니다.", "거고", "건데", "건데요"}   # 의존명사 '것'의 준말
_NOUN_FALSE = {"혼자", "이자", "배우자", "가입자", "피부양자", "지역가입자", "직장가입자", "수급자", "대상자", "은퇴자", "퇴직자", "투자",
               "부자", "남자", "여자", "소비자", "근로자", "사업자", "순서", "고지서", "신청서", "증명서", "계약서", "최고", "광고", "잔고",
               "화면", "측면"}   # 끝 글자가 절 경계(자·서·고·면)처럼 보이는 명사 — v1.7 새 모양에서는 절 경계로 치지 않음
_AUX_NEXT = ("두", "둔", "둘", "놓", "주", "준", "줄", "드리", "드릴", "드렸", "보", "본", "봤", "버리", "있", "계시", "계신", "싶")      # 보조 용언


def _break_pen(words, i, v17=False):
    """words[i-1] 뒤에서 줄(자막)을 끊을 때의 뜻 점수 (낮을수록 좋음 — 쉼표 −20·절 경계 −12·조사 −5, 덩어리를 가르면 +). 폭 차이는 부르는 쪽이 더함."""
    last = words[i - 1]
    score = 0.0
    if last.endswith(","):
        score -= 20
    elif _CLAUSE_END.search(last):
        score -= 12
    elif _PARTICLE_END.search(last):
        score -= 5
    if last in _NO_END_WORDS or re.fullmatch(r"(것|게|때|수|중|등)(이|을|를|은|는|에|도|만|보다|부터|까지|에서|으로|로|이라는|이라|인|이다|입니다)?[,.]?", words[i]):
        score += 100
    if words[i] in {"한", "할", "난", "된", "될", "온", "간", "산", "본", "준", "탄"} and not (v17 and last.endswith(",")):
        score += 30             # (v1.7 새 모양: 쉼표 뒤 '한 은퇴자'는 새 덩어리라 괜찮음)
    if last in _ADJ_SHORT:
        score += 10             # '많은 / 분들이'처럼 짧은 꾸밈말 뒤는 피함
    if last.endswith(("와", "과")) and len(last) >= 2:
        score += 6              # '진단과 / 치료로'처럼 짝을 가르지 않음
    if re.search(r"[\d천만억]$", last) and re.match(r"^(원|달러|일|월|년|배|명|개|번|살|분|초|주|달|퍼센트|%)", words[i]):
        score += 100            # 숫자와 단위는 한 줄에
    if re.search(r"\d+(월|년)$", last) and re.match(r"^\d", words[i]):
        score += 100            # 날짜는 한 줄에
    if re.search(r"\d\S*(에서|부터|~)$", last) and re.match(r"^\d", words[i]):
        score += 100            # 범위는 한 줄에 (100에서 / 125 X)
    if re.search(r"\d", last) and words[i].rstrip(",.") in _AFTER_NUM:
        score += 100            # 숫자 뒤 '이상·미만·정도·동안'은 한 줄에 (60세 / 이상 X)
    if re.match(r"^[\d-]", words[i]) and not (last.endswith(",") or _CLAUSE_END.search(last) or _PARTICLE_END.search(last)):
        score += 15             # 수량은 앞 명사와 한 줄에 (전단계 / 3,234명 X)
    if v17:                     # v1.7 — 예전 한 줄 규칙('line')의 결과는 그대로 두고 새 모양에만
        nxt = words[i].rstrip(",.")
        if not last.endswith(",") and last.rstrip(".") in _NOUN_FALSE:
            score += 12         # '남편 혼자 / 꺼내면' X — '혼자'는 절 경계가 아님
        if nxt in _FIXED_NEXT and not last.endswith(","):
            score += 30         # '나이에 / 따라' X (쉼표 뒤 '…내서, / 합치면'은 괜찮음)
        if last.endswith("면") and nxt.startswith(("되", "돼", "된", "됩")):
            score += 30         # '고치면 / 되는지' X (~면 되다)
        if words[i] in _DEP_NEXT:
            score += 100        # '손해 본 / 걸' X
        if nxt in {"줄", "줄은", "줄도", "줄을"} and re.search(r"(는|은|던|을|ㄹ)$", last):
            score += 100        # '못 받는 / 줄 알았던' X
        if (re.search(r"(이|가)$", last) and len(nxt) >= 2 and not last.endswith(",") and not re.search(r"\d", nxt)
                and (nxt.endswith(("는", "던")) or (0xAC00 <= ord(nxt[-1]) < 0xD7A4 and (ord(nxt[-1]) - 0xAC00) % 28 == 4))):
            score += 20         # '만기가 / 지난 분이' X (꾸미는 말 안의 주어와 서술어)
        if (len(last) >= 2 and not last.endswith(",") and not re.search(r"\d", last) and 0xAC00 <= ord(last[-1]) < 0xD7A4
                and (ord(last[-1]) - 0xAC00) % 28 in (4, 8) and last[-1] not in "은는만을를" and not _CLAUSE_END.search(last)):
            score += 15         # '만기가 지난 / 분이'·'퇴직연금인 / IRP에' X (받침 ㄴ·ㄹ 꾸밈말 뒤)
        if nxt.startswith("씨"):
            score += 100        # 'B / 씨가' X
        if nxt.startswith(_DEP_NOUN) and len(nxt) <= 4 and re.search(r"(는|은|던|을|할|될|볼|한|본|된)$", last):
            score += 60         # '지금 고치는 / 법까지' X ('는'을 조사로 잘못 봄)
        if (len(nxt) == 1 and 0xAC00 <= ord(nxt) < 0xD7A4 and (ord(nxt) - 0xAC00) % 28 in (4, 8)
                and not last.endswith(",")):
            score += 20         # 받침 ㄴ·ㄹ 한 글자 꾸밈말로 줄 시작 X ('334만 원을 / 낸 김씨는')
        if re.search(r"(고|어|아|여|해|워|와|줘|봐|둬)$", last) and nxt.startswith(_AUX_NEXT) and not last.endswith(","):
            score += 30         # '받고 / 있다는', '넣어 / 두고' X
        if re.search(r"(에서|부터)$", last) and (nxt == "약" or nxt[:1].isdigit()) and re.search(r"\d", " ".join(words[max(0, i - 3):i])):
            score += 100        # '2,100만 원에서 / 약 1,300만 원' X (범위는 한 덩어리)
    return score


def _best_split(text, fits, px, balance=1.0, v17=False):
    """text 를 두 토막 [앞, 뒤]로 — 두 토막 모두 fits() 를 만족하는 곳 중 쉼표·절 경계·조사 뒤를 우선, 두 토막 폭 차이를 줄이고,
    꾸밈 말로 끝내거나 의존명사(것·게·때·수) 앞, 숫자와 단위 사이에서 끊지 않는다. → (점수, [앞, 뒤]) 또는 None.
    balance = 폭 차이의 무게 (예전 'line' 1, 새 모양 0.5 — 줄 길이보다 뜻 덩어리). v17 = 새 모양에만 더하는 규칙
    ('X에 / 따라', '~면 / 되다', '본 / 걸', '받고 / 있다', '넣어 / 두고', '2,100만 원에서 / 약 1,300만'을 피함 — 예전 'line' 결과는 그대로)."""
    words = text.split(" ")
    glyph = px * 42 / 46               # 글자 하나 ≈ 42px (46px 기준)
    best = None
    for i in range(1, len(words)):
        a, b = " ".join(words[:i]), " ".join(words[i:])
        if not fits(a) or not fits(b):
            continue
        score = balance * abs(text_px(a, px) - text_px(b, px)) / glyph + _break_pen(words, i, v17)
        if best is None or score < best[0]:
            best = (score, [a, b])
    return best


WRAP_BAD = 0.0                 # 한 자막 안 줄바꿈 점수가 이보다 나쁘면(쉼표·절 경계·조사 뒤가 아님 — '지금 할 / 일까지') 자막 2개를 본다
SPLIT_GOOD = -8.0              # 그때 자막 2개로 나누는 곳이 이만큼 좋을 때만 (쉼표·절 경계)


def _wrap(text, layout):
    """→ (점수, 줄 목록) 또는 None. 한 줄이면 점수 −100. 줄은 2줄까지 (v1.9 — 3줄 없음)."""
    L = LAYOUTS[layout]
    fits = lambda x: text_px(x, L["px"]) <= L["width"]
    if fits(text):
        return -100.0, [text]
    if L["lines"] < 2:
        return None
    return _best_split(text, fits, L["px"], balance=0.5, v17=True)


def sent_layout(layout, n):
    """문장 n 의 자막 모양: 쇼츠 첫 문장(썸네일 그림 위 — kit.js K.cover)은 'shorts_cover'(42px·2줄, 자막 하나), 그 밖은 그대로 (v1.8 · v1.9)."""
    return "shorts_cover" if layout == "shorts" and n == 1 else layout


def wrap_lines(text, layout="long"):
    """자막 하나의 줄: 한 줄에 들어가면 [text], 아니면 (두 줄 자막이면) 자연스러운 곳에서 [윗줄, 아랫줄]. 안 들어가면 None."""
    w = _wrap(text, layout)
    return w[1] if w else None


def cue_split(text, layout="long"):
    """문장 → 자막 글 목록 (한 자막의 줄은 '\n'). 되도록 자막 하나 (v1.7). 두 줄로도 안 들어가거나, 두 줄로 들어가도
    줄을 바꿀 곳마다 덩어리를 가를 때(WRAP_BAD 보다 나쁨)만 자막 2개 — 그때도 나눈 곳이 쉼표·절 경계(SPLIT_GOOD)일 때만."""
    L = LAYOUTS[layout]
    one = _wrap(text, layout)
    if one and (one[0] <= WRAP_BAD or L.get("one")):        # v1.9 쇼츠 첫 문장('one')은 2줄에 들어가면 늘 자막 하나
        return ["\n".join(one[1])]
    v17 = layout != "line"
    two = _best_split(text, lambda x: _wrap(x, layout) is not None, L["px"], balance=0.5 if v17 else 1.0, v17=v17)
    if two and (one is None or (two[0] <= SPLIT_GOOD and two[0] < one[0])):
        return ["\n".join(wrap_lines(h, layout)) for h in two[1]]
    if one:
        return ["\n".join(one[1])]
    raise SystemExit(f"[SRT] ❌ 자막 2개({L['lines']}줄씩)로도 넘는 문장 → 대본에서 두 문장으로 나누세요 ({layout}): {text}")


def split_px(text):
    """예전 규칙(layout 'line'): 폭 1432px 이하면 [문장], 넘으면 [앞줄, 뒷줄] — 앞줄·뒷줄 자막 2개 (v1.6 과 같은 결과)."""
    return cue_split(text, "line")


# ----------------------------------------------------------------------------- 대본·SRT 읽기
def is_label(line):
    """파트 라벨(-사연 파트, -마무리 등). '-2,500만 원…'처럼 '-' 뒤가 숫자면 음수 금액으로 시작하는 문장이다."""
    return line.startswith("-") and not re.match(r"-\s*[\d.,]", line)


def parse_txt(path):
    """대본에서 자막이 될 문장만 (라벨·[장면]·카드 문구·빈 줄 제외). 이 순서가 '문장 번호'다."""
    out, in_card = [], False
    for raw in Path(path).read_text("utf-8-sig").splitlines():
        line = raw.strip()
        if not line:
            continue
        if is_label(line):
            in_card = False
            continue
        if line.startswith("[장면]"):
            in_card = True
            continue
        if not in_card:
            out.append(line)
    return out


def story_sentences(path):
    """파트 라벨에 '사연'이 든 파트의 문장 (사연자가 읽는 문장 — tts_narration 의 역할 판정과 같은 낱말)."""
    out, part, in_card = [], "", False
    for raw in Path(path).read_text("utf-8-sig").splitlines():
        line = raw.strip()
        if not line:
            continue
        if is_label(line):
            part, in_card = line.lstrip("-").strip(), False
            continue
        if line.startswith("[장면]"):
            in_card = True
            continue
        if not in_card and STORY_WORD in part:
            out.append(line)
    return out


def story_length(path):
    """→ (문장 수, 읽는 음절, 추정 초)."""
    st = story_sentences(path)
    syl = sum(syllables(x) for x in st)
    return len(st), syl, syl / STORY_RATE


def parse_cards(path):
    """[장면] 카드: 제목(같은 줄 '[장면]' 뒤), 문구(다음 라벨 전까지의 줄), 바로 앞 문장 번호, 추정 길이."""
    cards, n, cur = [], 0, None
    for raw in Path(path).read_text("utf-8-sig").splitlines():
        line = raw.strip()
        if not line:
            continue
        if is_label(line):
            cur = None
            continue
        if line.startswith("[장면]"):
            cur = {"after": n, "title": line[len("[장면]"):].strip(), "lines": []}
            cards.append(cur)
            continue
        if cur is not None:
            cur["lines"].append(line)
        else:
            n += 1
    for c in cards:      # build 때 넣는 공백 = 문구 글자 수 ÷ 7 + 1초 (4~8초, 최소 3.5초 규칙보다 김)
        chars = len("".join(c["lines"]).replace(" ", ""))
        c["seconds"] = round(min(8.0, max(4.0, chars / 7 + 1)), 3)
        c["chars"] = chars
    return cards


def _ts(t):
    ms = int(round(t * 1000))
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def _sec(ts):
    h, m, rest = ts.strip().split(":")
    s, ms = rest.split(",")
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000


def parse_srt(path):
    subs = []
    for block in re.split(r"\n\s*\n", Path(path).read_text("utf-8-sig").strip()):
        lines = block.strip().splitlines()
        if len(lines) < 3:
            continue
        a, b = lines[1].split("-->")
        subs.append({"start": _sec(a), "end": _sec(b), "lines": lines[2:], "text": " ".join(x.strip() for x in lines[2:])})
    return subs


def group(subs, sents):
    """SRT 자막들을 대본 문장에 순서대로 묶는다 (앞줄+뒷줄 = 문장). 반환: (문장별 자막 목록, 문제 목록)"""
    out, problems, i = [], [], 0
    for n, sent in enumerate(sents, 1):
        parts, joined = [], ""
        while i < len(subs) and len(joined) < len(sent):
            parts.append(subs[i])
            joined = " ".join(p["text"] for p in parts)
            i += 1
        if joined != sent:
            problems.append(f"문장 {n}: 자막과 대본이 다름 → 대본 '{sent}' / 자막 '{joined}'")
            return out, problems
        out.append({"n": n, "text": sent, "parts": parts, "start": parts[0]["start"], "end": parts[-1]["end"]})
    if i < len(subs):
        problems.append(f"대본에 없는 자막 {len(subs) - i}개가 끝에 남음 (첫 자막: '{subs[i]['text']}')")
    return out, problems


# ----------------------------------------------------------------------------- build
def _split_durs(parts, total):
    syl = [max(1, syllables(p)) + 0.5 * p.count(",") for p in parts]
    return [total * s / sum(syl) for s in syl]


def build(txt, out, reuse=None, layout=None):
    layout = layout or layout_of(txt)
    sents, cards = parse_txt(txt), parse_cards(txt)
    gap_after = {c["after"]: c["seconds"] for c in cards}
    one, pair = {}, {}
    if reuse:                                                         # 글자가 같은 문장 → 옛 길이 (자막 1개 또는 이어진 자막 2개의 합)
        old = parse_srt(reuse)
        for k, s in enumerate(old):
            one.setdefault(s["text"], s["end"] - s["start"])
            if k + 1 < len(old):
                pair.setdefault(s["text"] + " " + old[k + 1]["text"], (s["end"] - s["start"]) + (old[k + 1]["end"] - old[k + 1]["start"]))
    t, blocks, new_n, split_n, two_n = 0.0, [], 0, 0, 0
    for n, sent in enumerate(sents, 1):
        parts = cue_split(sent, sent_layout(layout, n))
        if sent in one:
            total = one[sent]
        elif sent in pair:
            total = pair[sent]
        else:
            total = duration(sent)
            new_n += 1
        durs = _split_durs([p.replace("\n", " ") for p in parts], total)
        split_n += len(parts) > 1
        two_n += sum("\n" in p for p in parts)
        for p, d in zip(parts, durs):
            blocks.append((t, t + d, p))
            t += d
        if n in gap_after:
            t += gap_after[n]
    Path(out).write_text("\n\n".join(f"{i}\n{_ts(a)} --> {_ts(b)}\n{p}" for i, (a, b, p) in enumerate(blocks, 1)) + "\n", "utf-8")
    print(f"[SRT] 저장 {out}: 모양 {layout} / 문장 {len(sents)} / 자막 {len(blocks)} (두 줄 자막 {two_n}개, 자막 2개로 나뉜 문장 {split_n}개, "
          f"새로 계산 {new_n}개), " + ", ".join(f"고지 공백 문장 {c['after']} 뒤 {c['seconds']}초" for c in cards) + f", 길이 {_ts(t)}")


# ----------------------------------------------------------------------------- check
def match_ok(gp):
    return not gp


def check(txt, srt, expect=None, layout=None):
    layout = layout or layout_of(txt)
    L = LAYOUTS[layout]
    sents, subs, cards = parse_txt(txt), parse_srt(srt), parse_cards(txt)
    problems, warnings = [], []
    for n, a in enumerate(sents, 1):
        if len(a) > SENT_MAX:     # 대본 쓸 때의 규칙(script_guide 0번). 자막은 아래 띠 폭으로 판정하므로 경고만
            warnings.append(f"문장 {n}: {len(a)}자 (새 대본은 50자 넘으면 두 문장으로 — 자막은 띠 폭으로 판정)")
    groups, gp = group(subs, sents)
    problems += gp
    cue_sent = {}                                     # v1.8 자막 번호 → 문장 번호 (쇼츠 첫 문장은 42px 모양 — v1.9)
    k0 = 0
    for g in groups:
        for _ in g["parts"]:
            k0 += 1
            cue_sent[k0] = g["n"]
    for k, s in enumerate(subs, 1):
        lay = sent_layout(layout, cue_sent.get(k, 0))
        Lk = LAYOUTS[lay]
        lines = [x.strip() for x in s["lines"]]
        if len(lines) > Lk["lines"]:
            problems.append(f"자막 {k}: {len(lines)}줄 (모양 {lay} — {Lk['lines']}줄까지)")
        for x in lines:
            if text_px(x, Lk["px"]) > Lk["width"] + 0.5:
                problems.append(f"자막 {k}: 한 줄 폭 {text_px(x, Lk['px']):.0f}px > {Lk['width']}px ({Lk['px']}px 글자) — '{x[:20]}…'")
        if len(lines) == 2 and text_px(s["text"], Lk["px"]) <= Lk["width"]:
            problems.append(f"자막 {k}: 한 줄에 들어가는데 두 줄 → 한 줄로")
        if s["end"] <= s["start"]:
            problems.append(f"자막 {k}: 길이 0 이하")
    split_n = two_n = 0
    for g in groups:
        two_n += sum(len(p["lines"]) == 2 for p in g["parts"])
        if len(g["parts"]) > 1:
            split_n += 1
            if len(g["parts"]) > len(cue_split(g["text"], sent_layout(layout, g["n"]))):     # build 와 같은 판단 (줄바꿈이 어색할 때만 자막 2개)
                problems.append(f"문장 {g['n']}: 자막 하나({LAYOUTS[sent_layout(layout, g['n'])]['lines']}줄)에 들어가는데 자막 {len(g['parts'])}개로 나뉨 → 하나로 합치기 (build --reuse)")
            if len(g["parts"]) > 2:
                problems.append(f"문장 {g['n']}: 자막 {len(g['parts'])}개로 나뉨 (2개까지)")
            if LAYOUTS[sent_layout(layout, g["n"])].get("one"):      # v1.9 쇼츠 첫 문장 = 썸네일 그림 — 자막이 바뀌어도 그림이 남음
                problems.append(f"문장 {g['n']}: 쇼츠 첫 문장(썸네일 그림 위)이 자막 {len(g['parts'])}개 → 대본에서 첫 문장을 줄이세요 (42px 2줄 안)")
    card_after = {c["after"]: c for c in cards}
    gaps = []
    if subs and subs[0]["start"] > LEAD_IN_MAX + EPS:
        problems.append(f"첫 자막 앞 여백 {subs[0]['start']:.2f}초 (> {LEAD_IN_MAX}초)")
    for k in range(1, len(subs)):
        gap = subs[k]["start"] - subs[k - 1]["end"]
        if gap < -EPS:
            problems.append(f"자막 {k}–{k + 1}: 겹침 {gap:.3f}초")
        elif gap > EPS:
            gaps.append((k, gap))
    sent_end_idx = {}
    idx = 0
    for g in groups:
        idx += len(g["parts"])
        sent_end_idx[g["n"]] = idx            # 이 문장의 마지막 자막 번호(1부터)
    card_gap_info = []
    for n, c in card_after.items():
        k = sent_end_idx.get(n)
        gap = next((gp_ for kk, gp_ in gaps if kk == k), 0.0) if k else 0.0
        card_gap_info.append((n, gap))
        if gap < CARD_GAP_MIN:
            problems.append(f"고지 공백: 문장 {n} 뒤 {gap:.2f}초 (최소 {CARD_GAP_MIN}초를 SRT 안에)")
    card_ks = {sent_end_idx.get(n) for n in card_after}
    for k, gap in gaps:
        if k not in card_ks:
            problems.append(f"자막 {k}–{k + 1}: 빈 시간 {gap:.3f}초 (고지 카드 자리 말고는 이어 붙임)")
    if expect:
        en, es = expect
        if len(sents) != en:
            problems.append(f"문장 수 {len(sents)} ≠ 기대값 {en}")
        if len(subs) != es:
            problems.append(f"자막 수 {len(subs)} ≠ 기대값 {es}")
    st_n, st_syl, st_sec = story_length(txt)
    story_ok = st_syl <= STORY_SYL_MAX
    measured = None     # 올린 영상은 SRT = 실제 오디오 시간 → 진행자 첫 문장 시작을 잰다 (음절 추정보다 정확)
    if st_n and match_ok(gp) and (Path(txt).parent / "youtube.json").is_file() and st_n < len(groups):
        measured = groups[st_n]["start"]
        story_ok = measured <= STORY_HOST_MAX + EPS
        if not story_ok:
            problems.append(f"사연 길이(올린 영상 실측): 진행자 시작 {measured:.1f}초 > {STORY_HOST_MAX:.0f}초 → "
                            "tools/studio_trim.py 로 스튜디오에서 사연 문장 빼기 (guides/archive/script_guide_v1.md 0-1의 13번)")
    elif st_n and not story_ok:
        problems.append(f"사연 길이: {st_n}문장·읽는 음절 {st_syl} ≈ {st_sec:.0f}초 (> {STORY_SYL_MAX}음절 ≈ 30초) → 5~7문장으로 줄이기 "
                        "(guides/archive/script_guide_v1.md 0-1의 13번, 사용자 지시 2026-10-12)")
    elif st_n and st_syl < STORY_SYL_MIN:
        warnings.append(f"사연 길이: 읽는 음절 {st_syl} ≈ {st_sec:.0f}초 (< {STORY_SYL_MIN}음절 ≈ 20초) — 결과 숫자·결정적 장면이 다 들어갔는지 확인")
    match = not gp
    total = subs[-1]["end"] if subs else 0
    print(f"[SRT] 모양 {layout} / 문장 {len(sents)} / 자막 {len(subs)} (두 줄 자막 {two_n}개, 자막 2개로 나뉜 문장 {split_n}개) / SRT–TXT {'일치 ✅' if match else '불일치 ❌'} / "
          + (" · ".join(f"고지 공백 문장 {n} 뒤 {g:.1f}초 {'✅' if g >= CARD_GAP_MIN else '❌'}" for n, g in card_gap_info) or "고지 카드 없음")
          + f" / 끝 {_ts(total)}"
          + ((f" / 사연 {st_n}문장·{st_syl}음절, 실측 진행자 시작 {measured:.1f}초 {'✅' if story_ok else '❌'}" if measured is not None
              else f" / 사연 {st_n}문장·{st_syl}음절 ≈ {st_sec:.0f}초 {'✅' if story_ok else '❌'}") if st_n else " / 사연 파트 없음"))
    for w in warnings:
        print("  ⚠️", w)
    for p in problems:
        print("  ❌", p)
    print("[SRT] ✅ 이상 없음" if not problems else f"[SRT] 문제 {len(problems)}개")
    return 0 if not problems else 1


def measure(txt, layout=None):
    layout = layout or layout_of(txt)
    L = LAYOUTS[layout]
    sents = parse_txt(txt)
    cues = two = 0
    for n, x in enumerate(sents, 1):
        parts = cue_split(x, sent_layout(layout, n))
        cues += len(parts)
        two += sum("\n" in p for p in parts)
        shown = "  ‖  ".join(p.replace("\n", " / ") for p in parts)
        print(f"{n:3d} {text_px(x, L['px']):6.0f}px {shown}")
    print(f"[SRT] 모양 {layout} ({L['desc']}) / 문장 {len(sents)} → 자막 {cues} (두 줄 자막 {two}개, 자막 2개로 나뉠 문장 {cues - len(sents)}개, "
          f"한 줄 {L['width']}px·{L['px']}px 글자) — '/' = 같은 자막 안 줄바꿈, '‖' = 다음 자막")


# ----------------------------------------------------------------------------- 영상용 내보내기
def export_remotion(txt, srt, out, audio_seconds=None, audio_file=None):
    sents, subs, cards = parse_txt(txt), parse_srt(srt), parse_cards(txt)
    groups, problems = group(subs, sents)
    if problems:
        raise SystemExit("[SRT] ❌ 대본과 자막이 다릅니다 → 먼저 check 로 확인\n  " + "\n  ".join(problems))
    by_n = {g["n"]: g for g in groups}
    card_rows = []
    for c in cards:
        a, b = by_n[c["after"]]["end"], by_n[c["after"] + 1]["start"]
        if b - a < CARD_GAP_MIN:
            raise SystemExit(f"[SRT] ❌ 고지 공백: 문장 {c['after']} 뒤 {b - a:.2f}초 (최소 {CARD_GAP_MIN}초) → SRT를 고치세요 (영상 코드는 자막을 밀지 않음)")
        card_rows.append({"afterSentence": c["after"], "title": c["title"], "lines": c["lines"], "start": round(a, 3), "end": round(b, 3)})
    last = groups[-1]["end"]
    total = max(last + 1.0, float(audio_seconds or 0))          # 영상 길이는 오디오보다 짧게 자르지 않는다
    data = {
        "sentences": [{"n": g["n"], "start": round(g["start"], 3), "end": round(g["end"], 3),
                       "parts": [{"start": round(p["start"], 3), "end": round(p["end"], 3), "text": p["text"]} for p in g["parts"]]}
                      for g in groups],
        "cards": card_rows,
        "audio": {"file": audio_file, "seconds": round(float(audio_seconds), 3)} if audio_file else None,
        "totalSeconds": round(total, 3),
    }
    body = ("// 자동 생성 — python tools/srt_tool.py remotion (직접 고치지 말고 대본·SRT를 고친 뒤 다시 생성)\n"
            "// 타이밍은 SRT 그대로(초) = 영상 시간. 번호는 대본 문장 번호. 고지 카드는 SRT 공백 자리 (코드에서 밀지 않음)\n"
            f"export const SRC = {json.dumps(data, ensure_ascii=False, indent=1)} as const;\n")
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    Path(out).write_text(body, "utf-8")
    print(f"[SRT] 영상용 저장 {out}: 문장 {len(groups)} / 자막 {len(subs)}, 고지 카드 {len(cards)}개 "
          + ", ".join(f"(문장 {c['afterSentence']} 뒤 {c['end'] - c['start']:.1f}초)" for c in card_rows)
          + f", 오디오 {audio_seconds or '없음'}, 영상 길이 {_ts(total)}")


# ----------------------------------------------------------------------------- 업로드 챕터
def _mmss(t):
    t = int(t)  # 챕터 시간은 내림 (자막보다 늦게 시작하지 않게)
    return f"{t // 3600}:{t % 3600 // 60:02d}:{t % 60:02d}" if t >= 3600 else f"{t // 60}:{t % 60:02d}"


def chapters(txt, srt, spec):
    """SRT = 영상 시간이므로 SRT 그대로 업로드하고, 챕터 시간만 문장 번호로 계산한다."""
    sents, subs = parse_txt(txt), parse_srt(srt)
    groups, problems = group(subs, sents)
    if problems:
        raise SystemExit("[SRT] ❌ 대본과 자막이 다릅니다 → 먼저 check 로 확인\n  " + "\n  ".join(problems))
    by_n = {g["n"]: g for g in groups}
    total = groups[-1]["end"] + 1.0
    rows = []
    for part in [p for p in spec.split(";") if p.strip()]:
        n, title = part.split("=", 1)
        g = by_n.get(int(n))
        if g is None:
            raise SystemExit(f"[CHAPTER] ❌ 문장 {n} 없음")
        rows.append((0.0 if int(n) == 1 else g["start"], int(n), title.strip()))
    problems = []
    if rows[0][1] != 1:
        problems.append("첫 챕터는 문장 1(0:00)이어야 함")
    if len(rows) < 3:
        problems.append("챕터는 3개 이상이어야 함")
    for (t0, _, a), (t1, _, b) in zip(rows, rows[1:] + [(total, None, "끝")]):
        if int(t1) - int(t0) < 10:
            problems.append(f"'{a}' 챕터가 10초 미만 ({int(t1) - int(t0)}초)")
        if t1 < t0:
            problems.append(f"'{b}' 시간이 앞 챕터보다 빠름")
    print("[CHAPTER] 설명란에 붙여 넣기 (자막은 이 SRT를 그대로 업로드):")
    for t, n, title in rows:
        print(f"{_mmss(t)} {title}")
    for p in problems:
        print("  ❌", p)
    print("[CHAPTER] ✅ YouTube 챕터 규칙 통과" if not problems else f"[CHAPTER] 문제 {len(problems)}개")
    return 0 if not problems else 1


def main(argv=None):
    ap = argparse.ArgumentParser(description="대본 TXT → SRT 자막 생성·검사 (한 문장 = 자막 하나, 길면 두 줄 — v1.7, 고지 공백 SRT 안)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build", help="TXT로 SRT 만들기")
    b.add_argument("txt")
    b.add_argument("out")
    b.add_argument("--reuse", help="기존 SRT (글자가 같은 문장은 길이를 그대로 사용, 나눔은 지금 규칙)")
    b.add_argument("--layout", choices=sorted(LAYOUTS), help="자막 모양 (없으면 경로로)")
    c = sub.add_parser("check", help="문장 / 자막 / SRT–TXT 일치 / 고지 공백 / 사연 길이(20~30초) 검사")
    c.add_argument("txt")
    c.add_argument("srt")
    c.add_argument("--expect", help="기대값 '문장수/자막수' (예: 91/117)")
    c.add_argument("--layout", choices=sorted(LAYOUTS), help="자막 모양 (없으면 경로로)")
    r = sub.add_parser("remotion", help="영상용 데이터(subtitles.ts) 내보내기")
    r.add_argument("txt")
    r.add_argument("srt")
    r.add_argument("out")
    r.add_argument("--audio-seconds", type=float, help="내레이션 길이(초) — 영상 길이를 이보다 짧게 하지 않음")
    r.add_argument("--audio-file", help="video/public 기준 내레이션 경로 (예: audio/multagi-2026-10.mp3)")
    u = sub.add_parser("upload", help="챕터 시간 계산 (SRT는 그대로 업로드)")
    u.add_argument("txt")
    u.add_argument("srt")
    u.add_argument("--chapters", required=True, help='"문장번호=제목;문장번호=제목" (첫 항목은 1=...)')
    m = sub.add_parser("measure", help="문장별 자막 줄과 나뉠 위치")
    m.add_argument("txt")
    m.add_argument("--layout", choices=sorted(LAYOUTS), help="자막 모양 (없으면 경로로)")
    a = ap.parse_args(argv)
    if a.cmd == "build":
        build(a.txt, a.out, a.reuse, a.layout)
        return 0
    if a.cmd == "remotion":
        export_remotion(a.txt, a.srt, a.out, a.audio_seconds, a.audio_file)
        return 0
    if a.cmd == "upload":
        return chapters(a.txt, a.srt, a.chapters)
    if a.cmd == "measure":
        measure(a.txt, a.layout)
        return 0
    exp = tuple(int(x) for x in a.expect.split("/")) if a.expect else None
    return check(a.txt, a.srt, exp, a.layout)


if __name__ == "__main__":
    sys.exit(main())
