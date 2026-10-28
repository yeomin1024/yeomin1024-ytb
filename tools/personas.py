#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-28 — 새로: 시청자 페르소나를 분석 대상 최근 영상의 댓글에서 만든다 (사용자 지시 2026-10-28
#          "시청자 페르소나 파일 생성하도록 해 — 분석 대상 최근 영상 유튜브 댓글을 보고 시청자 유형 파악, 많이 겹치는 유형 탐색해서 생성,
#          몇명 생성하여 적절한지 정해야함, 댓글 분석 결과가 곧 페르소나 … 연령, 처한 상황, 지식 수준, 기존 알고 있는 내용, 원하는 내용 등 …
#          페르소나 기반으로 주제 탐색 및 요약본, 최종 대본 피드백에 사용 … 분석 결과에 따라 업데이트도 돼야함").
#          · 자료: 승인한 롱폼 영상(W_·01_·P01_) 중 올린 지 RECENT_DAYS 안 · 주제 언어(LANGS) · (음악) 영상 제목 거르기 — 시청자 댓글 전부.
#          · 댓글마다 단서: 자기 나이(밝힌 것만) · 생애 단계/듣는 때(stage) · 처지(state) · 지식(초급 말·용어·정정) · 유형(comment_types 규칙)
#            · 원하는 것(질문·요청 댓글의 낱말·용어) · 좋아함/불만(칭찬·비판 댓글의 갈래). 처지 단서는 자기 이야기일 때만 (저는·제가… 또는 경험·질문 댓글).
#          · 묶음 = stage 하나 (강한 단서 > 밝힌 나이 > 그 밖 단서). 페르소나 수 = 큰 묶음부터 MIN_SHARE 이상만, 누적 COVER 까지,
#            MIN_PERSONAS ~ MAX_PERSONAS — 계산표를 문서에 남김.
#          · 결과: <주제>/result/outliers/personas.md (사람·AI 가 읽음) · personas.json (tools/persona_review.py 가 읽음).
#          · 분석이 끝날 때 저절로 다시 만듦 (weekly_analysis v1.5 → success_analysis 뒤). 할당량 0.
#          설정: <주제>/personas.toml (낱말 사전·묶음·처지·용어 — 주제마다). ※ 연구·교육용 — 투자 권유가 아님.
#          첫 실행 감사(무작위 댓글을 Claude 가 읽음)로 고친 것: 나이는 끝말(입니다·인데…)·앞말(저는·저희 부부는…)이 있을 때만 + 나이 앞에 남을 가리키는
#          말(아들이·사람이·평균)이 있으면 뺌 (재테크 27/40 → 36/40) · 엄격 모드 AGE_STRICT (역사 — 역사 인물 나이 6/12 → 약 15/20) · 처지는 단서 근처
#          (앞 40자·뒤 25자)에 자기 말이 있을 때만 · '모르는 말' = 그 말 바로 뒤에 '뭔가요·무슨 뜻' · 강의 미끼 댓글(단톡방·자료 부탁)은 '원하는 것'에서 뺌
#          · 언어마다 따로 SPLIT_LANG (음악) · '모든 댓글 (참고)' 칸 (칭찬·불만 갈래는 여기서 숫자가 큼) · 용어 사전을 정규식 하나로 (속도).
"""시청자 페르소나 — 분석 대상 최근 영상의 댓글에서

  python3 tools/personas.py stock                 # <주제>/result/outliers/personas.md · personas.json
  python3 tools/personas.py stock audit age       # 단서(age · stage:<키> · state:<키> · know:beginner · know:advanced)에 걸린 댓글 무작위 40개
                                                  #   → 사람이 읽고 정확도를 셈 (사전을 고칠 때)
로그: [STAGE] [시각] key=value (START·DATA·CUES·SEGMENT·PERSONA·BASELINE·WRITE·DONE)
"""
import argparse
import json
import logging
import math
import random
import re
import statistics
import sys
import time
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comment_types as ct            # noqa: E402  iter_videos · lang_group · classify (댓글 유형 — 같은 규칙)

try:
    import tomllib
except ModuleNotFoundError:           # Python 3.10
    import tomli as tomllib

VERSION = "v1.0"
ROOT = Path(__file__).resolve().parent.parent
LOG = logging.getLogger("persona")
SEED = 20261028
LANG_CODE = {"한국어": "ko", "영어": "en"}
DEFAULTS = {"RECENT_DAYS": 180, "LANGS": ["한국어"], "MIN_SHARE": 0.08, "COVER": 0.80, "MIN_PERSONAS": 2, "MAX_PERSONAS": 6,
            "MIN_N": 30, "NEED_SELF": True, "VIDEO_TITLE_RX": "", "SPLIT_LANG": False, "WANT_SKIP": "", "AGE_STRICT": False, "AGE_SKIP_BEFORE": "", "TOP_WANTS": 12, "TOP_TERMS": 10, "QUOTES": 4}
GROUPS = ("성공 사례", "하루 조회수 상위", "그 밖의 승인 영상")


def log(stage, _lvl=logging.INFO, **kv):
    LOG.log(_lvl, "[%s] [%s] %s", stage, datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S"),
            " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) and (' ' in v or not v) else v}" for k, v in kv.items()))


# ---------------------------------------------------------------- 공통 낱말 (주제 설정이 없을 때도 쓰는 것)
SELF = {"ko": r"(?<![가-힣])(저는|제가|저도|저희|전\s|나는|내가|나도|난\s|제\s|내\s|우리\s?(집|애|아이|남편|아내|와이프|부모|엄마|아빠|부부))",
        "en": r"\b(I|I'm|I am|I've|I was|my|me|mine)\b"}
# 자기 나이 — 끝말(입니다·인데…)이나 앞말(저는·저희 부부는…)로 자기 나이일 때만 (v1.0 감사: 끝말 없이 '1960년생 이후는'·'65세 남자치고'·
#   '50대 부부 기준'까지 세면 40개 중 27개만 맞음 → 끝말·앞말을 꼭 요구)
_KO_END = r"(?:입니다|이에요|예요|에요|이고|이구요|이지만|인데|인대|이라(?![고는면도])|라서|이며|임(?![가-힣])|이네요|이자|로서|가\s?된|에\s?접어|이랍니다|랍니다|이요(?![가-힣]))"
_KO_NOUN = (r"(?:\s?(?:직장인|주부|가장|아줌마|아저씨|아재|할머니|할아버지|남자|여자|남성|여성|맘|엄마|아빠|싱글|미혼|기혼|은퇴자|퇴직자|자영업자?|초보|"
            r"직딩|회사원|공무원|교사|대학생|학생|취준생|청년|노인|주린이|개미|투자자|흙수저|직장맘|워킹맘|부부|아들|딸|노총각|노처녀|백수|돌싱))?")
_KO_SELF = r"(?<![가-힣])(?:저는|전|나는|난|저도|나도|저희\s?(?:부부|집)?(?:는|도)?|우리\s?부부(?:는|도)?|제\s?나이(?:는|가)?|내\s?나이(?:는|가)?|현재\s?나이(?:는|가)?)"
_KO_WHEN = r"(?:\s*(?:이제|올해|벌써|현재|지금|곧|만))?"
_KO_NOT = r"(?!\s*(?:까지|부터|이후|이상|넘|되면|이면|에\s|였으면|라면|이라면|쯤|때|를|을|바라|앞두|향해))"   # '저는 60세까지 일할 줄'·'저도 50대였으면' — 지금 나이가 아님
_KO_END_STRICT = r"(?:입니다|이에요|예요|에요|임(?![가-힣])|이랍니다|랍니다)"
# 엄격 (설정 AGE_STRICT — 역사처럼 댓글 속 나이가 대개 역사 인물의 나이일 때): '저는·제 나이·난' 앞말이 있거나, '…입니다·…예요·…임'으로 끝나는 자기소개만
AGE_STRICT = {
    "ko": (r"(?<!님 )(?<![\d가-힣제])(?P<dec>[1-9])0\s?대\s*(?:초반|중반|후반|초|중|말)?" + _KO_NOUN + r"\s*" + _KO_END_STRICT +
           r"|" + _KO_SELF + _KO_WHEN + r"\s*(?P<dec2>[1-9])0\s?대(?!\s*(?:왕|임금|대통령|손|후손|째))" + _KO_NOT +
           r"|" + _KO_SELF + _KO_WHEN + r"\s*(?P<yrs>\d\d)\s*(?:살|세(?!기))" + _KO_NOT +
           r"|(?<!님 )(?<!\d)(?P<yrs2>\d\d)\s*(?:살|세(?!기))" + _KO_NOUN + r"\s*" + _KO_END_STRICT +
           r"|(?<![\d])(?P<by4>19[3-9]\d|200\d)\s*년생" + _KO_NOUN + r"\s*" + _KO_END_STRICT +
           r"|(?<![\d])(?P<by2>[3-9]\d|0\d)\s*년생" + _KO_NOUN + r"\s*" + _KO_END_STRICT +
           r"|" + _KO_SELF + r".{0,4}?(?<![\d])(?P<by5>19[3-9]\d|200\d|[3-9]\d|0\d)\s*년생"),
}
AGE = {
    "ko": (r"(?<!님 )(?<![\d가-힣제])(?P<dec>[1-9])0\s?대\s*(?:초반|중반|후반|초|중|말)?" + _KO_NOUN + r"\s*" + _KO_END +
           r"|(?<![\d가-힣제])(?P<dec3>[1-9])0\s?대\s*(?:초반|중반|후반)?도\s.{0,15}(?:나요|까요|되나|될까)"
           r"|" + _KO_SELF + _KO_WHEN + r"\s*(?P<dec2>[1-9])0\s?대(?!\s*(?:왕|임금|대통령|손|후손|째))" + _KO_NOT +
           r"|" + _KO_SELF + _KO_WHEN + r"\s*(?P<yrs>\d\d)\s*(?:살|세(?!기))" + _KO_NOT +
           r"|(?<!님 )(?<!\d)(?P<yrs2>\d\d)\s*(?:살|세(?!기))" + _KO_NOUN + r"\s*" + _KO_END +
           r"|(?<![\d])(?P<by4>19[3-9]\d|200\d)\s*년생" + _KO_NOUN + r"\s*" + _KO_END +
           r"|(?<![\d])(?P<by2>[3-9]\d|0\d)\s*년생" + _KO_NOUN + r"\s*" + _KO_END +
           r"|" + _KO_SELF + r".{0,4}?(?<![\d])(?P<by5>19[3-9]\d|200\d|[3-9]\d|0\d)\s*년생"),
    "en": (r"\bI(?:'m| am)\s+(?P<yrs>[1-9]\d)\b(?!\s*(?:%|min|minutes|hours?|hrs|days?|times|x\b))|\bI(?:'m| am)\s+in\s+my\s+(?P<dec>[1-9])0s\b"
           r"|\bas\s+an?\s+(?P<yrs2>[1-9]\d)[- ]?(?:yo|year[- ]old)\b|\b(?P<yrs3>[1-9]\d)\s*(?:yo|y/o|years?[- ]old)\s+(?:here|man|woman|guy|girl|male|female|student|mom|dad|grandma|grandpa)\b"),
}
# 나이 앞 10자에 남을 가리키는 말이 있으면 그 사람 나이 ('작은아들이 32살인데요'·'받는 사람이 63세 인데')
OTHER_BEFORE = {"ko": re.compile(r"(아들|딸|남편|신랑|아내|와이프|마누라|엄마|아빠|부모님?|어머니|아버지|어머님|아버님|시모|시부|장모|장인|친구|지인|동생|형님|누나|언니|오빠|"
                                 r"이모|고모|삼촌|외삼촌|할머니|할아버지|시어머니|시아버지|형|오빠|누나|언니|애기|강아지|고양이|댕댕이|냥이|반려견|반려묘|"
                                 r"님|분|씨|사람|애|아이|손주|조카|선배|후배|사장|대표|교수|박사|며느리|사위|자식|자녀|부인|와이프|남친|여친|평균|평균\s?나이|수명|사망|기준)\s?(이|가|은|는|도|께서|의)?\s?$"),
                "en": re.compile(r"\b(my|his|her|their)\s+(son|daughter|wife|husband|mom|mother|dad|father|friend|brother|sister|kid|kids|grandma|grandpa)\s*(is|was)?\s*$", re.I)}
OTHER_NEAR = re.compile(r"평균|수명|사망|즉위|당시|그때\s?나이|나이에|살\s?때|세\s?때")   # 나이 앞 30자 — 통계·남의 생애 (앵커 없음)
BEGINNER = {"ko": r"초보|주린이|입문|처음\s?(시작|해|들|알|접)|잘\s?몰라|모르겠|몰랐|무슨\s?(뜻|말)|뭔가요|뭐예요|뭐에요|뭔지|이해가\s?(안|잘\s?안)|헷갈|어렵(네|다|고|습|더)|쉽게\s?(설명|알려)",
            "en": r"\b(beginner|newbie|new to|first time|don'?t understand|confus\w+|what does .{1,25} mean|what is an?)\b"}
CORRECT = {"ko": r"정정|틀렸|틀린\s?(내용|부분|정보)|사실과\s?다르|잘못\s?(알|말씀|나온)|오류가?\s?있|아닙니다\.?\s|고증\s?(오류|틀)",
           "en": r"\b(correction|incorrect|that'?s wrong|actually,|not true|inaccurate)\b"}
ASK_TERM = {"ko": r"뭔가요|뭐예요|뭐에요|뭔지|무슨\s?뜻|뜻이|란\s?뭐|이란\s?뭐|이\s?뭐|가\s?뭐|모르|몰라|궁금",
            "en": r"\bwhat(?:'s| is| are| does)\b|\bmeaning\b|\bexplain\b"}
STOP_KO = set("""그리고 그런데 그래서 그러면 그럼 하지만 근데 혹시 정말 진짜 너무 아주 매우 조금 많이 그냥 이제 지금 요즘 오늘 내일 어제 항상 계속 다시 이미
이거 저거 그거 이것 저것 그것 여기 저기 거기 이런 저런 그런 어떤 무슨 어느 어떻게 왜 언제 어디 얼마 얼마나 몇 누구 무엇 뭐 뭘 뭔가 무엇을
영상 유튜브 댓글 구독 좋아요 감사 감사합니다 고맙습니다 선생님 대표님 박사님 교수님 작가님 님 분 분들 사람 사람들 우리 저희 제가 저는 나는 내가 저도
질문 궁금 궁금합니다 궁금해요 부탁 부탁드립니다 알려 알려주세요 해주세요 주세요 있나요 없나요 되나요 하나요 할까요 인가요 건가요 나요 까요 가요
있는 없는 하는 되는 같은 다른 이번 다음 정도 경우 때문 생각 이야기 얘기 말씀 내용 부분 문제 방법 이유 하면 해야 해서 하고 하는데 인데 있고 없고
그게 이게 저게 거의 바로 먼저 가장 제일 혹은 또는 및 등 것 거 수 때 중 좀 더 덜 안 못 잘 꼭 또 다 한 두 세 네
초반 중반 후반 대초반 대중반 대후반 년생 나이 올해 작년 내년 좋아 좋은 좋겠 같아 같습니다 보고 보니 봤는데 들어 들었
답변 하나 앞으로 앞으 있게 필요 조금씩 그동안 동안 이후 이전 지금까지 현재 계속해서 정도로""".split())
# 강의·자료 미끼 댓글 ('단톡방 입장했습니다 자료 부탁드려요') — 나이는 세되 '원하는 것'에서는 뺌 (재테크 v1.0 첫 결과: 낱말 1~5위가 단톡방·자료·신청·입장·무료자료)
WANT_SKIP = r"단톡방|톡방|오픈\s?채팅|카톡방|무료\s?자료|자료\s?(좀\s?)?(부탁|받|신청|주세요|요청)|전자책|책자|수강\s?신청|입장\s?(했|완료|합니다)|링크\s?(좀|부탁)|\bpdf\b"
STOP_EN = set("""the a an and or but so if then than that this these those it its it's is are was were be been being have has had do does did
to of in on at for from with by about as into over after before up down out just very really so too also not no yes
i i'm im me my mine you your yours we our they their he she him her his them what which who whom how why when where
can could would should will shall may might must there here more most some any all each every one two three
song songs music video videos playlist channel thank thanks please like love good great nice best amazing beautiful
know get got make made go going come came see look want need feel listen listening watch watching""".split())
PARTICLES = sorted(("은 는 이 가 을 를 에 의 도 로 으로 에서 에게 께 한테 까지 부터 와 과 랑 이랑 이나 나 요 이요 인가요 나요 까요 가요 는지 인지 할까요 하나요 "
                    "하면 해야 하는 한 할 한데 인데 이고 이며 이면 이라 이라고 라고 하고 에는 에도 으로도 로도 보다 처럼 만 만큼 이랑은 과는 와는 들 들이 들은 들을 "
                    "입니다 이에요 예요 에요 이죠 죠 같은 같아요 같은데 해요 했어요 합니다 하세요 하시나요 하셨나요 했나요 될까요 되나요 있나요 없나요 인가 일까").split(),
                   key=len, reverse=True)
# 낱말 끝이 움직씨·그림씨 꼴이면 뺌 ('있나'·'싶어'·'할수'·'입니다'·'대인데' — v1.0 첫 결과의 '원하는 것' 낱말 윗자리를 차지함). 이름씨만 남기려는 어림.
VERB_END = re.compile(r"(습니다|입니다|합니다|됩니다|세요|해요|어요|아요|에요|예요|네요|군요|는데|인데|은데|던데|지만|어서|아서|해서|하고|하면|으면|려고|려면|"
                      r"싶어|싶은|싶다|싶습|을수|할수|볼수|될수|갈수|살수|할까|될까|있나|없나|있을|없을|있는|없는|있어|없어|했는|했어|했다|한다|된다|하는|되는|받는|받고|사는|가능|"
                      r"드려|드립|주세|주시|해주|하세|나요|까요|가요|던가|는지|인지|시면|주면|드네|하네|보고|겠|였|었|았|했|됐|히)$|^(안녕|감사|부탁|혹시|정말|진짜)")
TOK = re.compile(r"[가-힣]{2,}|[A-Za-z][A-Za-z0-9&+.\-]{1,}|[0-9]{2,4}[A-Za-z]+")


def kw_tokens(text, code, stop):
    out = []
    for tok in TOK.findall(text or ""):
        t = tok
        if code == "ko" and re.match(r"[가-힣]", t):
            for p in PARTICLES:
                if t.endswith(p) and len(t) - len(p) >= 2:
                    t = t[:-len(p)]
                    break
            if len(t) < 2 or t in STOP_KO or t in stop or VERB_END.search(t) or re.search(r"\d", t):
                continue
        else:
            t = t.strip(".-")
            t = t if (code == "ko" and t.isupper()) else t.lower()     # 한국어 댓글 속 ISA·ETF 는 그대로
            if len(t) < 3 or t.lower() in STOP_EN or t in stop or t.isdigit():
                continue
        out.append(t)
    return out


# ---------------------------------------------------------------- 설정
def load_cfg(topic, root=None):
    p = Path(root or ROOT) / topic / "personas.toml"
    if not p.is_file():
        return None, p
    d = tomllib.loads(p.read_text("utf-8"))
    cfg = dict(DEFAULTS)
    cfg.update(d.get("personas") or {})
    cfg["stages"] = d.get("stage") or []
    cfg["states"] = d.get("state") or []
    cfg["know"] = d.get("know") or {}
    cfg["like"] = d.get("like") or []
    cfg["dislike"] = d.get("dislike") or []
    cfg["stop"] = set((d.get("personas") or {}).get("STOP") or [])
    cfg["version"] = (d.get("personas") or {}).get("VERSION") or "?"
    k = cfg["know"]
    cfg["_terms"] = {re.sub(r"\s", "", t).lower() for key in ("basic", "advanced", "basic_en", "advanced_en") for t in (k.get(key) or [])}
    return cfg, p


def rxc(p):
    return re.compile(p, re.I | re.S) if p else None


def compile_cfg(cfg):
    """언어마다 정규식 (설정 + 공통)."""
    C = {}
    for lg in cfg["LANGS"]:
        code = LANG_CODE.get(lg, "en")
        k = cfg["know"]
        terms_basic = [t for t in (k.get("basic") or [])]
        terms_adv = [t for t in (k.get("advanced") or [])]
        if code == "en":
            terms_basic += k.get("basic_en") or []
            terms_adv += k.get("advanced_en") or []
        def terms_rx(ts):
            """용어 여럿을 정규식 하나로 (v1.0: 용어마다 정규식 하나 → 댓글 19만 개에 60초. 하나로 묶어 한 번만 훑음).
            찾은 글자 → 사전 표기 (대소문자·띄어쓰기 무시)."""
            if not ts:
                return None, {}
            alts = [(r"(?<![A-Za-z])" + re.escape(t).replace(r"\ ", r"\s?") + r"(?![A-Za-z])") if re.match(r"[A-Za-z0-9]", t)
                    else re.escape(t).replace(r"\ ", r"\s?") for t in sorted(set(ts), key=len, reverse=True)]
            return re.compile("|".join(alts), re.I), {re.sub(r"\s", "", t).lower(): t for t in ts}
        C[lg] = {
            "code": code,
            "self": rxc(SELF[code]), "age": rxc((AGE_STRICT if cfg.get("AGE_STRICT") else AGE).get(code) or AGE[code]),
            "age_skip": rxc(cfg.get("AGE_SKIP_BEFORE") or ""),
            "beginner": rxc((k.get(f"beginner_{code}") or "") + ("|" if k.get(f"beginner_{code}") else "") + BEGINNER[code]),
            "correct": rxc(CORRECT[code]), "ask_term": rxc(ASK_TERM[code]),
            "want_skip": rxc(WANT_SKIP + (("|" + cfg["WANT_SKIP"]) if cfg.get("WANT_SKIP") else "")),
            "stages": [(s["key"], rxc(s.get(code) or ""), bool(s.get("strong")), bool(s.get("self", cfg["NEED_SELF"]))) for s in cfg["stages"]],
            "states": [(s["key"], rxc(s.get(code) or ""), bool(s.get("self", cfg["NEED_SELF"]))) for s in cfg["states"]],
            "basic": terms_rx(terms_basic), "advanced": terms_rx(terms_adv),
            "like": [(c["key"], rxc(c.get(code) or "")) for c in cfg["like"]],
            "dislike": [(c["key"], rxc(c.get(code) or "")) for c in cfg["dislike"]],
        }
    return C


# ---------------------------------------------------------------- 자료
def video_rows(topic, cfg, now, root=None):
    out = Path(root or ROOT) / topic / "result" / "outliers"
    an = json.loads((out / "analysis.json").read_text("utf-8")) if (out / "analysis.json").is_file() else {}
    success_ids = {c["id"] for c in an.get("success_cases") or []}
    vpd_ids = {c["id"] for c in (an.get("vpd_top") or {}).get("cases") or []}
    title_rx = rxc(cfg.get("VIDEO_TITLE_RX") or "")
    skipped = Counter()
    for d, meta, info, cms in ct.iter_videos(out):
        try:
            age = (now - datetime.fromisoformat(str(meta.get("published_at") or meta.get("published"))[:10]).replace(tzinfo=timezone.utc)).days
        except ValueError:
            skipped["날짜 없음"] += 1
            continue
        if age > cfg["RECENT_DAYS"]:
            skipped[f"{cfg['RECENT_DAYS']}일보다 오래"] += 1
            continue
        lg = ct.lang_group(meta, info)
        if lg not in cfg["LANGS"]:
            skipped[f"언어 {lg}"] += 1
            continue
        if title_rx and not title_rx.search(meta.get("title") or ""):
            skipped["제목 거르기"] += 1
            continue
        vid = meta.get("id")
        grp = GROUPS[0] if vid in success_ids else (GROUPS[1] if vid in vpd_ids else GROUPS[2])
        yield {"id": vid, "title": meta.get("title") or "", "lg": lg, "group": grp, "age_days": age}, cms
    video_rows.skipped = skipped


def age_of(m, now):
    g = m.groupdict()
    for k in ("dec", "dec2", "dec3"):
        if g.get(k):
            return int(g[k]) * 10
    for k in ("yrs", "yrs2", "yrs3", "yrs4"):
        if g.get(k):
            return min(90, (int(g[k]) // 10) * 10)
    if g.get("by4"):
        return max(10, min(90, ((now.year - int(g["by4"])) // 10) * 10))
    if g.get("by5") and len(g["by5"]) == 4:
        return max(10, min(90, ((now.year - int(g["by5"])) // 10) * 10))
    if g.get("by2") or g.get("by5"):
        y = int(g.get("by2") or g["by5"])
        y = 2000 + y if y <= now.year % 100 else 1900 + y
        return max(10, min(90, ((now.year - y) // 10) * 10))
    return None


def cues(text, C, now):
    """댓글 하나 → 단서 묶음."""
    typ = ct.classify(text)
    selfish = bool(C["self"].search(text)) or typ in ("E", "Q")
    short_self = typ in ("E", "Q") and len(text) <= 100       # 짧은 경험·질문 댓글 = 주어가 빠져도 자기 이야기

    def hit(r, need):
        """단서가 자기 이야기인가: 짧은 경험·질문 댓글이거나, 단서 앞 40자·뒤 25자 안에 '저는·제가·우리 부부…' (v1.0 감사 — 댓글 어딘가에
        '저는'만 있어도 세면 '생활비 빠듯' 15개 중 5개만 맞음: 남의 이야기·일반론이 섞임)."""
        if not r:
            return False
        if not need:
            return bool(r.search(text))
        for m in r.finditer(text):
            if short_self or C["self"].search(text[max(0, m.start() - 40): m.end() + 25]):
                return True
        return False
    age = None
    for a in C["age"].finditer(text):
        before30 = text[max(0, a.start() - 30): a.start()]
        if OTHER_BEFORE[C["code"]].search(text[max(0, a.start() - 10): a.start()]) or OTHER_NEAR.search(before30) \
                or (C["age_skip"] and C["age_skip"].search(before30)):
            continue
        age = age_of(a, now)
        break
    st = [k for k, r, strong, need in C["stages"] if hit(r, need)]
    strong = [k for k, r, s2, need in C["stages"] if s2 and k in st]
    sts = [k for k, r, need in C["states"] if hit(r, need)]
    def found(pair):
        r, canon = pair
        if not r:
            return []
        return sorted({canon.get(re.sub(r"\s", "", m.group(0)).lower(), m.group(0)) for m in r.finditer(text)})
    adv = found(C["advanced"])
    basic = [t for t in found(C["basic"]) if t not in adv]
    beg = bool(C["beginner"].search(text))
    cor = bool(C["correct"].search(text)) and bool(adv or basic)
    know = "초급" if beg else ("상급" if (len(adv) >= 2 or cor) else ("중급" if adv else ("기초" if basic else None)))
    asks_term = bool(C["ask_term"].search(text)) and (typ == "Q" or beg)
    unknown = [t for t in basic + adv if _unk_rx(t, C["code"]).search(text)] if asks_term else []   # 그 낱말 바로 뒤에 '뭔가요·무슨 뜻·모르
    like = [k for k, r in C["like"] if r and r.search(text)] if typ == "P" else []
    dislike = [k for k, r in C["dislike"] if r and r.search(text)] if typ == "C" else []
    return {"type": typ, "promo": bool(C["want_skip"].search(text)), "self": selfish, "age": age, "stages": st, "strong": strong, "states": sts, "basic": basic, "adv": adv,
            "know": know, "asks_term": asks_term, "unknown": unknown, "like": like, "dislike": dislike}


_UNK = {}


def _unk_rx(t, code):
    """'ISA가 뭔가요'·'IRP란 무엇'·'what is an ETF' — 그 말을 모른다는 질문 (v1.0 첫 결과: 질문 댓글에 든 말을 모두 '모르는 말'로 세니
    '주식 160'처럼 아는 말이 맨 위에 옴 → 낱말 바로 뒤·앞의 뜻 묻는 말만)."""
    k = (t, code)
    if k not in _UNK:
        e = re.escape(t).replace(r"\ ", r"\s?")
        if code == "ko":
            _UNK[k] = re.compile(e + r"(?:이|가|은|는|이란|란|라는\s?게|이라는\s?게)?\s?(?:뭔가요|뭐예요|뭐에요|뭔지|뭐죠|뭐지|뭐야|무엇|무슨\s?뜻|뜻이|뜻을|"
                                 r"어떤\s?(거|건|것)|모르|몰라|헷갈|이해가\s?안)", re.I)
        else:
            _UNK[k] = re.compile(r"what(?:'s| is| are| does)\s+(?:a |an |the )?" + e + r"|" + e + r".{0,12}\bmean", re.I)
    return _UNK[k]


def stage_of(c, cfg):
    """묶음 하나: 강한 단서 > 밝힌 나이(나이 범위가 있는 묶음) > 그 밖 단서 (설정 순서)."""
    if c["strong"]:
        return c["strong"][0]
    if c["age"] is not None:
        for s in cfg["stages"]:
            r = s.get("age")
            if r and r[0] <= c["age"] <= r[1]:
                return s["key"]
    return c["stages"][0] if c["stages"] else None


# ---------------------------------------------------------------- 만들기
def collect(topic, cfg, now, root=None):
    C = compile_cfg(cfg)
    rows, vids = [], []
    for v, cms in video_rows(topic, cfg, now, root):
        vids.append(v)
        Cl = C[v["lg"]]
        for m in cms:
            t = str(m.get("text") or "")
            if m.get("creator") or not t.strip():
                continue
            c = cues(t, Cl, now)
            c.update({"text": ct.clean(t, 400), "likes": int(m.get("likes") or 0), "vid": v["id"], "group": v["group"], "lg": v["lg"], "code": Cl["code"]})
            c["stage"] = stage_of(c, cfg)
            if c["stage"] and cfg["SPLIT_LANG"]:
                c["stage"] = f"{c['stage']}@{v['lg']}"     # 언어마다 따로 (외국 댓글과 한국어 댓글을 한 페르소나로 섞지 않음)
            rows.append(c)
    return rows, vids, getattr(video_rows, "skipped", Counter())


def choose(seg_counts, n_assigned, cfg):
    """페르소나 수 정하기 — 큰 묶음부터: MIN_N 이상 · 몫 MIN_SHARE 이상(최소 수를 채우기 전엔 무시) · 누적 COVER 에 닿으면 멈춤 · MAX 까지."""
    table, chosen, cum = [], [], 0.0
    for key, n in sorted(seg_counts.items(), key=lambda x: -x[1]):
        share = n / n_assigned if n_assigned else 0
        why = ""
        if len(chosen) >= cfg["MAX_PERSONAS"]:
            why = f"최대 {cfg['MAX_PERSONAS']}명"
        elif n < cfg["MIN_N"]:
            why = f"댓글 {cfg['MIN_N']}개 미만"
        elif cum >= cfg["COVER"] and len(chosen) >= cfg["MIN_PERSONAS"]:
            why = f"앞 묶음들이 이미 {cum:.0%} 덮음 (기준 {cfg['COVER']:.0%})"
        elif share < cfg["MIN_SHARE"] and len(chosen) >= cfg["MIN_PERSONAS"]:
            why = f"몫 {share:.1%} < {cfg['MIN_SHARE']:.0%}"
        if not why:
            chosen.append(key)
            cum += share
        table.append({"key": key, "n": n, "share": share, "cum": cum if key in chosen else None, "chosen": key in chosen, "why": why or "고름"})
    return chosen, table


def top(counter, k):
    return [(x, n) for x, n in counter.most_common(k)]


def quote(t, n=130):
    t = re.sub(r"@\S+\s*", "", t).strip()
    return (t[:n] + "…") if len(t) > n else t


def profile(key, rs, cfg, stage_def, state_names, like_names, dislike_names):
    n = len(rs)
    ages = [r["age"] for r in rs if r["age"] is not None]
    age_c = Counter(ages)
    states = Counter(s for r in rs for s in set(r["states"]))
    combos = Counter(tuple(sorted(set(r["states"]))[:2]) for r in rs if len(set(r["states"])) >= 2)
    know = Counter(r["know"] for r in rs if r["know"])
    nk = sum(know.values())
    level = None
    if nk:
        beg, mid, hi = know["초급"] / nk, know["중급"] / nk, know["상급"] / nk
        # 가장 흔한 꼴: 초급 표현 30% 이상 → 초급 · 고급 용어(중급+상급) 40% 이상 → 중급(상급 25% 이상이면 상급) · 그 밖 → 기초
        level = "초급" if beg >= 0.3 else ("상급" if hi >= 0.25 else ("중급" if mid + hi >= 0.4 else "기초"))
    known = Counter(t for r in rs if r["type"] != "Q" and r["know"] != "초급" for t in set(r["basic"] + r["adv"]))
    unknown = Counter(t for r in rs for t in set(r["unknown"]))
    q = [r for r in rs if r["type"] == "Q" and not r["promo"]]
    want_terms = Counter(t for r in q for t in set(r["basic"] + r["adv"]))
    stop = cfg["stop"]
    want_kw = Counter(w for r in q for w in set(kw_tokens(r["text"], r["code"], stop)) if w.lower() not in cfg["_terms"])   # 용어는 위 칸에서 셈
    types = Counter(r["type"] for r in rs)
    likes = Counter(k for r in rs for k in r["like"])
    dislikes = Counter(k for r in rs for k in r["dislike"])
    groups = Counter(r["group"] for r in rs)
    qs = sorted(q, key=lambda r: -r["likes"])
    seen, top_q = set(), []
    for r in qs:
        k2 = r["text"][:40]
        if k2 in seen or len(r["text"]) < 12:
            continue
        seen.add(k2)
        top_q.append({"text": quote(r["text"]), "likes": r["likes"]})
        if len(top_q) >= 6:
            break
    rep = sorted([r for r in rs if r["type"] in ("E", "Q") and (r["age"] is not None or r["states"])], key=lambda r: -r["likes"])
    seen, reps = set(), []
    for r in rep:
        k2 = r["text"][:40]
        if k2 in seen or len(r["text"]) < 15:
            continue
        seen.add(k2)
        reps.append({"text": quote(r["text"]), "likes": r["likes"], "age": r["age"], "states": [state_names.get(s, s) for s in r["states"]]})
        if len(reps) >= cfg["QUOTES"]:
            break
    med = None
    if ages:
        med = int(statistics.median(ages))
    return {
        "key": key, "name": stage_def.get("name", key), "n": n, "likes": sum(r["likes"] for r in rs),
        "age": {"n": len(ages), "median_decade": med, "dist": {f"{a}대": c for a, c in sorted(age_c.items())}},
        "states": [{"key": k, "name": state_names.get(k, k), "n": c, "share": round(c / n, 4)} for k, c in states.most_common(6)],
        "combos": [{"states": [state_names.get(s, s) for s in k], "n": c} for k, c in combos.most_common(4)],
        "know": {"n": nk, "dist": dict(know), "level": level},
        "known_terms": top(known, cfg["TOP_TERMS"]), "unknown_terms": top(unknown, 8),
        "want_terms": top(want_terms, cfg["TOP_WANTS"]), "want_words": top(want_kw, cfg["TOP_WANTS"]), "top_questions": top_q,
        "questions": len(q), "types": {ct.type_name(k): c for k, c in types.most_common()},
        "likes_cat": [{"name": like_names.get(k, k), "n": c} for k, c in likes.most_common(5)],
        "dislikes_cat": [{"name": dislike_names.get(k, k), "n": c} for k, c in dislikes.most_common(5)],
        "groups": dict(groups), "quotes": reps,
    }


def build(topic, now=None, root=None, write=True):
    t0 = time.monotonic()
    now = now or datetime.now(timezone.utc)
    if now.tzinfo is None:                     # 부르는 쪽이 시간대 없는 시각을 넘겨도 (weekly_analysis·web_ui)
        now = now.replace(tzinfo=timezone.utc)
    cfg, cp = load_cfg(topic, root)
    if cfg is None:
        log("START", logging.WARNING, topic=topic, note="personas.toml 없음 — 페르소나를 만들지 않음", next=f"{topic}/personas.toml 을 만듦")
        return None
    log("START", topic=topic, tool=f"personas.py {VERSION}", config=str(cp.relative_to(Path(root or ROOT))), config_version=cfg["version"],
        recent_days=cfg["RECENT_DAYS"], langs=",".join(cfg["LANGS"]), title_filter=bool(cfg.get("VIDEO_TITLE_RX")))
    rows, vids, skipped = collect(topic, cfg, now, root)
    n = len(rows)
    log("DATA", topic=topic, videos=len(vids), comments=n, skipped=json.dumps(dict(skipped), ensure_ascii=False),
        by_group=json.dumps(dict(Counter(v["group"] for v in vids)), ensure_ascii=False))
    if not n:
        log("DONE", logging.WARNING, topic=topic, note="댓글 없음 — 만들지 않음")
        return None
    any_cue = sum(1 for r in rows if r["age"] is not None or r["stages"] or r["states"])
    n_age = sum(1 for r in rows if r["age"] is not None)
    assigned = [r for r in rows if r["stage"]]
    log("CUES", topic=topic, any_cue=any_cue, age=n_age, assigned=len(assigned), know=sum(1 for r in rows if r["know"]),
        questions=sum(1 for r in rows if r["type"] == "Q"), promo_skipped=sum(1 for r in rows if r["type"] == "Q" and r["promo"]))
    seg = Counter(r["stage"] for r in assigned)
    if cfg["SPLIT_LANG"]:
        chosen, table = [], []
        for lg in cfg["LANGS"]:
            sub = {k: v for k, v in seg.items() if k.endswith("@" + lg)}
            c2, t2 = choose(sub, sum(sub.values()), cfg)
            chosen += c2
            table += [dict(t, lang=lg) for t in t2]
    else:
        chosen, table = choose(seg, len(assigned), cfg)
    stage_def = {s["key"]: s for s in cfg["stages"]}
    base = lambda k: k.split("@")[0]
    lang_of = lambda k: k.split("@")[1] if "@" in k else ""
    seg_total = Counter()
    for k, v in seg.items():
        seg_total[lang_of(k)] += v
    state_names = {s["key"]: s.get("name", s["key"]) for s in cfg["states"]}
    like_names = {s["key"]: s.get("name", s["key"]) for s in cfg["like"]}
    dislike_names = {s["key"]: s.get("name", s["key"]) for s in cfg["dislike"]}
    for t in table:
        t["name"] = stage_def.get(base(t["key"]), {}).get("name", t["key"]) + (f" · {lang_of(t['key'])}" if lang_of(t["key"]) else "")
    log("SEGMENT", topic=topic, segments=len(seg), chosen=",".join(chosen), cover=f"{sum(seg[k] for k in chosen) / max(1, len(assigned)):.3f}")
    by = defaultdict(list)
    for r in assigned:
        by[r["stage"]].append(r)
    personas = []
    for i, k in enumerate(chosen, 1):
        p = profile(k, by[k], cfg, stage_def.get(base(k), {}), state_names, like_names, dislike_names)
        p["id"] = f"P{i}"
        p["lang"] = lang_of(k)
        if p["lang"]:
            p["name"] += f" · {p['lang']}"
        p["share"] = round(p["n"] / (seg_total[p["lang"]] or len(assigned)), 4)    # 언어를 나누면 그 언어 안의 몫
        personas.append(p)
        log("PERSONA", topic=topic, id=p["id"], key=k, n=p["n"], age_n=p["age"]["n"], age_median=p["age"]["median_decade"],
            level=p["know"]["level"], top_state=(p["states"][0]["name"] if p["states"] else "-"),
            top_want=(p["want_terms"][0][0] if p["want_terms"] else (p["want_words"][0][0] if p["want_words"] else "-")))
    # 모든 댓글 (참고 칸) — 페르소나에 안 든 다수의 지식·원하는 것·좋아함·불만 (칭찬·비판 갈래는 여기서 숫자가 큼)
    baselines = []
    for lg in (cfg["LANGS"] if cfg["SPLIT_LANG"] else [None]):
        rs = [r for r in rows if lg is None or r["lg"] == lg]
        if not rs:
            continue
        b = profile("all", rs, cfg, {"name": "모든 댓글 (참고)" + (f" · {lg}" if lg else "")}, state_names, like_names, dislike_names)
        b.update({"id": "전체", "lang": lg or "", "share": 1.0, "quotes": [], "top_questions": b["top_questions"][:3]})
        baselines.append(b)
        log("BASELINE", topic=topic, lang=lg or "-", comments=len(rs), level=b["know"]["level"],
            top_like=(b["likes_cat"][0]["name"] if b["likes_cat"] else "-"), top_dislike=(b["dislikes_cat"][0]["name"] if b["dislikes_cat"] else "-"))
    # 전체 원하는 것 (페르소나에 안 든 댓글도 — 주제 탐색용)
    allq = [r for r in rows if r["type"] == "Q" and not r["promo"]]

    def wants(qs, ps):
        o = {"want_terms": top(Counter(t for r in qs for t in set(r["basic"] + r["adv"])), 15),
             "want_words": top(Counter(w for r in qs for w in set(kw_tokens(r["text"], r["code"], cfg["stop"])) if w.lower() not in cfg["_terms"]), 15)}
        shared = Counter(t for p in ps for t, _ in (p["want_terms"][:8] + p["want_words"][:8]))
        o["shared_wants"] = [t for t, c in shared.most_common() if c >= 2]     # 두 페르소나 이상이 함께 묻는 것
        return o
    if cfg["SPLIT_LANG"]:
        overall = {"by_lang": {lg: wants([r for r in allq if r["lg"] == lg], [p for p in personas if p["lang"] == lg]) for lg in cfg["LANGS"]}}
    else:
        overall = wants(allq, personas)
    data = {"topic": topic, "tool": f"personas.py {VERSION}", "config_version": cfg["version"], "made": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "rules": {k: cfg[k] for k in ("RECENT_DAYS", "LANGS", "MIN_SHARE", "COVER", "MIN_PERSONAS", "MAX_PERSONAS", "MIN_N", "NEED_SELF", "VIDEO_TITLE_RX", "SPLIT_LANG", "AGE_STRICT")},
            "data": {"videos": len(vids), "by_group": dict(Counter(v["group"] for v in vids)), "by_lang": dict(Counter(v["lg"] for v in vids)),
                     "comments": n, "any_cue": any_cue, "age": n_age, "assigned": len(assigned), "skipped": dict(skipped),
                     "questions": len(allq), "promo_skipped": sum(1 for r in rows if r["type"] == "Q" and r["promo"])},
            "segments": table, "personas": personas, "baselines": baselines, "overall": overall,
            "stage_defs": [{"key": s["key"], "name": s.get("name", s["key"]), "age": s.get("age"), "strong": bool(s.get("strong"))} for s in cfg["stages"]]}
    if write:
        out = Path(root or ROOT) / topic / "result" / "outliers"
        (out / "personas.json").write_text(json.dumps(data, ensure_ascii=False, indent=1), "utf-8")
        (out / "personas.md").write_text(render_md(data), "utf-8")
        log("WRITE", topic=topic, md=f"{topic}/result/outliers/personas.md", json=f"{topic}/result/outliers/personas.json", personas=len(personas))
    log("DONE", topic=topic, personas=len(personas), seconds=round(time.monotonic() - t0, 1))
    return data


# ---------------------------------------------------------------- 문서
def pct(x):
    return f"{x * 100:.0f}%" if x >= 0.095 else f"{x * 100:.1f}%"


def join(items, k=6, fmt=lambda x: f"{x[0]} {x[1]}"):
    items = list(items)[:k]
    return " · ".join(fmt(x) for x in items) if items else "근거 없음"


def age_line(p):
    a = p["age"]
    if not a["n"]:
        return "근거 없음 (나이를 밝힌 댓글 0)"
    dist = sorted(a["dist"].items(), key=lambda x: -x[1])
    main = dist[0]
    s = f"{main[0]} {main[1] / a['n']:.0%}"
    if len(dist) > 1:
        s += " · " + " · ".join(f"{k} {v / a['n']:.0%}" for k, v in dist[1:3])
    s += f" (밝힌 {a['n']}명)"
    if a["n"] < 10:
        s += " ⚠️ 적음"
    return s


def know_line(p):
    k = p["know"]
    if not k["n"]:
        return "근거 없음"
    d = k["dist"]
    parts = [f"{x} {d.get(x, 0) / k['n']:.0%}" for x in ("초급", "기초", "중급", "상급") if d.get(x)]
    return f"**{k['level']}** — " + " · ".join(parts) + f" (단서 {k['n']})"


def one_liner(p, defs):
    a = p["age"]
    parts = [p["name"]]
    if a["n"] >= 10 and a["median_decade"]:
        parts.append(f"밝힌 나이 가운데값 {a['median_decade']}대")
    if p["states"]:
        parts.append(f"가장 흔한 처지 '{p['states'][0]['name']}'")
    lv = {"초급": "기초부터 묻는", "기초": "기본 낱말은 아는", "중급": "용어를 꽤 쓰는", "상급": "전문 용어로 따지는"}.get(p["know"]["level"], "")
    if lv:
        parts.append(f"{lv} 시청자")
    wants = ", ".join(dict.fromkeys(t for t, _ in (p["want_terms"][:3] + p["want_words"][:3])))
    if wants:
        parts.append(f"가장 많이 묻는 것: {wants}")
    return " · ".join(parts) + "."


def render_md(D):
    P = D["personas"]
    d = D["data"]
    L = [f"# {D['topic']} 시청자 페르소나 — 분석 대상 최근 영상의 댓글에서 (자동)", "",
         f"만든 때 {D['made']} · `tools/{D['tool'].replace(' ', ' ')}` · 설정 `{D['topic']}/personas.toml` {D['config_version']} · "
         f"분석(analyze)이 끝날 때마다 저절로 다시 만듦 — 손으로 고치지 않는다 (사전은 `personas.toml` 에서).",
         "사용자 지시 2026-10-28 \"시청자 페르소나 파일 생성하도록 해 … 댓글 분석 결과가 곧 페르소나 … 주제 탐색 및 요약본, 최종 대본 피드백에 사용 … 분석 결과에 따라 업데이트\".",
         "※ 연구·교육용. 댓글에서 센 숫자이며 투자 권유가 아니다.", ""]
    # 0. 한눈에
    L += ["## 0. 한눈에 — 페르소나 " + f"{len(P)}명", "",
          f"자료: 올린 지 {D['rules']['RECENT_DAYS']}일 안 승인 영상 {d['videos']}개 ({', '.join(f'{k} {v}' for k, v in d['by_lang'].items())}) · 시청자 댓글 {d['comments']:,}개 → "
          f"자기 단서(나이·처지)가 있는 댓글 {d['any_cue']:,}개 ({pct(d['any_cue'] / d['comments'])}) · 묶음에 든 댓글 {d['assigned']:,}개 · 나이를 밝힌 댓글 {d['age']:,}개.", ""]
    if P:
        cols = P + D.get("baselines", [])
        head = "| | " + " | ".join(f"**{p['id']} {p['name']}**" if p["id"] != "전체" else f"*{p['name']}*" for p in cols) + " |"
        L += [head, "|---|" + "---|" * len(cols)]
        def row(label, f):
            L.append(f"| {label} | " + " | ".join(str(f(p)).replace("|", "/") for p in cols) + " |")
        row("몫 (묶음에 든 댓글 중)", lambda p: f"{pct(p['share'])} (댓글 {p['n']:,})" if p["id"] != "전체" else f"댓글 {p['n']:,}")
        row("연령 (밝힌 사람)", age_line)
        row("처한 상황 (많은 순)", lambda p: join(p["states"], 3, lambda s: f"{s['name']} {pct(s['share'])}"))
        row("지식 수준", know_line)
        row("이미 아는 말", lambda p: join(p["known_terms"], 6, lambda x: x[0]))
        row("잘 모르는 말 (물어봄)", lambda p: join(p["unknown_terms"], 5, lambda x: f"{x[0]} {x[1]}"))
        row("원하는 것 (질문 속 용어)", lambda p: join(p["want_terms"], 6))
        row("원하는 것 (질문 낱말)", lambda p: join(p["want_words"], 6))
        row("좋아하는 것", lambda p: join(p["likes_cat"], 3, lambda x: f"{x['name']} {x['n']}"))
        row("불만·떠나는 까닭", lambda p: join(p["dislikes_cat"], 3, lambda x: f"{x['name']} {x['n']}"))
        row("한 줄 소개", lambda p: one_liner(p, D["stage_defs"]))
    L.append("")
    # 1. 몇 명
    r = D["rules"]
    L += ["## 1. 몇 명인가 — 정한 방법", "",
          f"- 댓글마다 묶음 하나 (설정의 `[[stage]]` 순서): ① 강한 단서(예: 은퇴했·연금 받는 중) ② 밝힌 나이가 든 나이 범위 ③ 그 밖 단서. "
          f"처지 단서는 {'자기 이야기일 때만 (저는·제가… 또는 경험·질문 댓글)' if r['NEED_SELF'] else '모든 댓글에서 (듣는 때처럼 스스로 말하는 단서)'}.",
          f"- 큰 묶음부터 고름: 댓글 {r['MIN_N']}개 이상 · 몫 {r['MIN_SHARE']:.0%} 이상 · 누적 {r['COVER']:.0%} 에 닿으면 멈춤 · {r['MIN_PERSONAS']}~{r['MAX_PERSONAS']}명"
          + (" — **언어마다 따로** (몫·누적도 그 언어 안에서. 외국 댓글로 한국어 페르소나를 만들지 않음)." if r.get("SPLIT_LANG") else "."),
          "- 그래서 페르소나 수는 댓글이 정한다 — 분석이 바뀌면 수도 바뀐다.", "",
          "| 묶음 | 댓글 | 몫 | 누적 | 결정 |", "|---|---|---|---|---|"]
    for t in D["segments"]:
        L.append(f"| {t['name']} | {t['n']:,} | {pct(t['share'])} | {pct(t['cum']) if t['cum'] is not None else ''} | {'✅ ' if t['chosen'] else ''}{t['why']} |")
    L.append("")
    # 2. 자세히
    L += ["## 2. 페르소나별 자세히", ""]
    for p in P:
        L += [f"### {p['id']} {p['name']} — 댓글 {p['n']:,}개 ({pct(p['share'])})", "", f"{one_liner(p, D['stage_defs'])}", ""]
        L.append(f"- **연령**: {age_line(p)} — 분포 " + (" · ".join(f"{k} {v}" for k, v in p["age"]["dist"].items()) or "없음"))
        L.append("- **처한 상황**: " + join(p["states"], 6, lambda s: f"{s['name']} {s['n']:,} ({pct(s['share'])})"))
        if p["combos"]:
            L.append("  - 함께 나온 처지 (겹치는 유형): " + " · ".join(f"{' + '.join(c['states'])} {c['n']}" for c in p["combos"]))
        L.append(f"- **지식 수준**: {know_line(p)}")
        L.append("- **이미 아는 말** (질문·초급 아닌 댓글에서 쓴 말): " + join(p["known_terms"], 10))
        L.append("- **잘 모르는 말** ('…가 뭔가요·무슨 뜻'처럼 그 말의 뜻을 물은 댓글): " + join(p["unknown_terms"], 8))
        L.append(f"- **원하는 것** — 질문·요청 {p['questions']:,}개: 용어 " + join(p["want_terms"], 10) + " / 낱말 " + join(p["want_words"], 10))
        if p["top_questions"]:
            L.append("  - 좋아요 많은 질문: " + " · ".join(f"\"{q['text']}\" 👍{q['likes']}" for q in p["top_questions"][:5]))
        L.append("- **좋아하는 것** (칭찬 댓글 갈래): " + join(p["likes_cat"], 5, lambda x: f"{x['name']} {x['n']}"))
        L.append("- **불만·떠나는 까닭** (비판 댓글 갈래): " + join(p["dislikes_cat"], 5, lambda x: f"{x['name']} {x['n']}"))
        L.append("- **댓글 유형**: " + " · ".join(f"{k} {v / p['n']:.0%}" for k, v in list(p["types"].items())[:5]))
        L.append("- **어느 영상에서**: " + " · ".join(f"{k} {v:,}" for k, v in p["groups"].items()))
        if p["quotes"]:
            L.append("- **대표 댓글** (원문 — 작성자 이름 없음):")
            for q in p["quotes"]:
                tag = (f"{q['age']}대 · " if q["age"] else "") + ", ".join(q["states"])
                L.append(f"  - \"{q['text']}\" 👍{q['likes']}" + (f" ({tag})" if tag else ""))
        L.append("")
    # 3. 쓰는 법
    O = D["overall"].get("by_lang") or {"": D["overall"]}
    shared = [t for o in O.values() for t in o["shared_wants"][:8]]
    L += ["## 3. 이 문서를 쓰는 곳 (주제 탐색 · 요약본 · 최종 대본 피드백)", "",
          "- **주제 탐색** (`guides/topic_guide.md`): 후보마다 '대상 페르소나 + 그 페르소나의 원하는 것(위 질문 용어·낱말·좋아요 많은 질문)'을 적는다. "
          "두 페르소나 이상이 함께 묻는 것 = 넓은 주제" + (f": **{', '.join(shared[:10])}**" if shared else "") + ".",
          "- **요약본**: 맨 위 [페르소나] 칸 — 대상 P 번호 · 그가 원하는 것 중 이 영상이 답하는 것 · 지식 수준에 맞출 것(잘 모르는 말은 풀어 말함) · 불만(길다·광고 등)을 피할 것.",
          f"- **최종 대본 피드백**: `python3 tools/persona_review.py {D['topic']} <대본.txt>` → 페르소나마다 원하는 것을 다뤘는지 · 잘 모르는 말이 설명 없이 나오는지 · 불만 갈래에 걸리는지 → 요약본·대본을 고친다."]
    for lg, o in O.items():
        L.append(f"- 전체 질문{f' ({lg})' if lg else ''} (페르소나에 안 든 댓글 포함): 용어 " + join(o["want_terms"], 12) + " / 낱말 " + join(o["want_words"], 12))
    L.append("")
    # 4. 한계
    L += ["## 4. 한계 — 먼저 읽을 것", "",
          f"- 나이·처지는 **스스로 밝힌 댓글만** ({pct(d['any_cue'] / d['comments'])}). 밝히지 않는 다수가 같은 분포라는 보장은 없다 — 연령 칸은 '밝힌 사람' 기준.",
          "- 같은 사람이 여러 댓글을 달면 여러 번 센다 (작성자 정보는 저장하지 않음).",
          "- 단서는 낱말 규칙(정규식)이다 — 정확도는 `python3 tools/personas.py <주제> audit <단서>` 로 무작위 댓글을 읽어 확인한다 (설정 머리에 확인한 정확도).",
          "- 지식 수준은 쓴 용어·초보 표현·정정 댓글로 어림한 것 — 쓰지 않은 사람의 지식은 모른다.",
          "- 외국 댓글로 한국어 규칙을 만들지 않는다 (설정 LANGS 밖 언어는 뺌)." + (f" 뺀 영상: {', '.join(f'{k} {v}' for k, v in d['skipped'].items())}." if d["skipped"] else ""), ""]
    return "\n".join(L)


# ---------------------------------------------------------------- 점검 (사람이 읽음)
def audit(topic, what, n=40, now=None, root=None):
    now = now or datetime.now(timezone.utc)
    cfg, _ = load_cfg(topic, root)
    rows, _, _ = collect(topic, cfg, now, root)
    kind, _, key = what.partition(":")
    if kind == "age":
        hit = [r for r in rows if r["age"] is not None]
    elif kind == "stage":
        hit = [r for r in rows if key in r["stages"] or r["stage"] == key]
    elif kind == "state":
        hit = [r for r in rows if key in r["states"]]
    elif kind == "know":
        hit = [r for r in rows if (key == "beginner" and r["know"] == "초급") or (key == "advanced" and r["know"] == "상급")]
    else:
        raise SystemExit("단서: age · stage:<키> · state:<키> · know:beginner · know:advanced")
    random.seed(SEED)
    pick = random.sample(hit, min(n, len(hit)))
    print(f"[AUDIT] topic={topic} cue={what} hits={len(hit)} shown={len(pick)} — 맞으면 o, 틀리면 x 로 세어 정확도를 personas.toml 머리에 적는다")
    for i, r in enumerate(pick, 1):
        tag = f"{r['age']}대" if r["age"] else ""
        print(f"{i:02d}. [{tag} {r['stage'] or '-'} {','.join(r['states'])}] {quote(r['text'], 160)}")
    return len(hit)


def main(argv=None):
    ap = argparse.ArgumentParser(description="시청자 페르소나 — 분석 대상 최근 영상의 댓글에서")
    ap.add_argument("topic")
    ap.add_argument("cmd", nargs="?", default="build", choices=["build", "audit"])
    ap.add_argument("cue", nargs="?", default="age")
    ap.add_argument("--n", type=int, default=40)
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args(argv)
    logging.basicConfig(level=a.log_level, format="%(message)s", stream=sys.stdout)
    if a.cmd == "audit":
        audit(a.topic, a.cue, a.n)
        return 0
    return 0 if build(a.topic) else 1


if __name__ == "__main__":
    sys.exit(main())
