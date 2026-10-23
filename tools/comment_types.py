#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0.1 — 2026-10-23 — iter_videos 댓글에 published(댓글 단 때) 칸을 더함 (comment_clusters.py --by comment 가 comments.csv 를 두 번 읽지 않게). 그 밖 그대로.
# v1.0 — 2026-10-22 — 새로: 모든 댓글에 유형 하나 (사용자 지시 2026-10-21 "너 분석 영상들의 모든 댓글 유형 나눠서 통계내서 분석하고 있는가
#          맞아? 일부분 밖에 없는거 같은데" → 확인해 보니 analysis.md 8번은 성공 사례 댓글(전체의 약 10%)만, 그중 87%는 어느 갈래에도 안 들었고
#          표에 그 줄이 없었음 · weekly.md 는 59%가 안 듦. 사용자가 고친 방법 "A+b로 해" = A 표본을 사람(Claude)이 직접 분류해 실제 분포 추정
#          + B 그 표본에 맞춰 규칙을 고쳐 댓글 전부에 적용, 남는 것은 '그 밖'으로 드러냄).
#          ① sample: 시청자 댓글(채널 주인 뺌) 전부에서 언어 묶음별 무작위 표본 (씨앗 고정) → comment_type_sample.tsv (절반 '조정' · 절반 '시험').
#          ② 사람이 comment_type_labels.tsv 에 유형을 붙임. ③ evaluate: 규칙 vs 사람 — 규칙은 '조정' 절반만 보고 고치고 정확도는 '시험' 절반으로.
#          ④ report: 댓글 전부에 규칙 → comment_types.md·.json (규칙 몫 · 표본 추정과 95% 범위 · 표본으로 보정한 추정). 할당량 0.
#          ※ 연구·교육용 — 투자 권유가 아님.
"""모든 댓글에 유형 하나 — 표본(사람) + 규칙(전부)

  python3 tools/comment_types.py stock sample      # <주제>/result/outliers/comment_type_sample.tsv (씨앗 고정 — 다시 돌려도 같음)
  (사람이 <주제>/result/outliers/comment_type_labels.tsv 에 sid·type 을 적음 — 유형 정의는 아래 TYPES)
  python3 tools/comment_types.py stock evaluate    # 규칙 vs 사람 (조정·시험 절반 따로)
  python3 tools/comment_types.py stock report      # <주제>/result/outliers/comment_types.md · .json
"""
import argparse
import csv
import json
import logging
import math
import random
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import success_analysis as sa        # noqa: E402  한국어 갈래 낱말(정치·요청·반문·도배)을 이어 씀

VERSION = "v1.0.1"
ROOT = Path(__file__).resolve().parent.parent
LOG = logging.getLogger("ctype")
SEED = 20261022
SAMPLE_SIZES = {"한국어": 600, "영어": 400, "그 밖 언어": 100}
# 유형 — 댓글 하나 = 유형 하나 (주된 뜻). 애매하면 이 순서로 앞의 것: 광고 > 정치 > 질문 > 비판 > 경험 > 의견 > 정보 > 칭찬 > 반응
TYPES = {
    "Q": ("질문·요청", "답을 원해 묻거나(종목·방법·영상 내용) 다뤄 달라고 요청. 따지는 반문('말이 되나요?')은 비판·의견으로"),
    "E": ("경험·내 상황", "자기 매수·매도·손익·보유 종목·처지(나이·은퇴·계좌)를 주로 말함"),
    "O": ("투자 의견·전망·원칙", "시장·종목 전망, 투자 방법에 대한 주장·조언·교훈 (자기 이야기가 주가 아님)"),
    "I": ("정보·요약 보충", "타임라인·요약·사실·숫자·출처 보충, 내용 정정"),
    "P": ("칭찬·감사·응원", "영상·출연자·채널에 대한 좋은 말, 감사, 응원·축하"),
    "C": ("비판·반박·불만", "영상·출연자·채널·내용에 대한 비판, 반박, 낚시·광고·말 바꾸기 지적, 출연자 조롱"),
    "G": ("정치·사회", "정부·정치인·정당·정책·국민연금 운용·사회에 대한 의견 (투자와 엮여도 주된 대상이 정치·정책이면 여기)"),
    "R": ("단순 반응·농담", "감탄·웃음·밈·짧은 맞장구·다른 댓글에 대한 반응 (뜻 있는 내용이 거의 없음)"),
    "S": ("광고·도배·무관", "홍보·리딩방·링크·같은 글 도배, 영상·투자와 무관한 말"),
}
OTHER = "X"                                   # 규칙에 안 걸림 ('그 밖') — 사람 표본에는 없음
TYPE_ORDER = list(TYPES) + [OTHER]


def type_name(code):
    return TYPES[code][0] if code in TYPES else "그 밖 (규칙에 안 걸림)"


def log(stage, level=logging.INFO, **kv):
    LOG.log(level, "[%s] [%s] %s", stage, datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S"),
            " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) and (' ' in v or not v) else v}" for k, v in kv.items()))


def clean(t, n=500):
    return re.sub(r"\s+", " ", str(t or "")).strip()[:n]


# ---------------------------------------------------------------- 자료
def lang_group(meta, info):
    langs = " ".join(str(x or "") for x in (meta.get("video_lang"), (info or {}).get("lang"), (info or {}).get("audio_lang")))
    if re.search(r"(^|\s)ko", langs):
        return "한국어"
    if re.search(r"(^|\s)en", langs):
        return "영어"
    return "그 밖 언어"


def iter_videos(out):
    """승인한 영상 폴더(W_·01_·P01_) → (meta, info, 댓글 목록). 댓글 = comments.csv 그대로 (id 포함)."""
    for d in sorted(Path(out).iterdir()):
        if not (d.is_dir() and re.match(r"^(W_|P?\d\d_)", d.name) and (d / "metadata.json").is_file()):
            continue
        meta = json.loads((d / "metadata.json").read_text("utf-8"))
        ip = Path(out) / ".cache" / f"{meta.get('id')}.json"
        info = json.loads(ip.read_text("utf-8")) if ip.is_file() else {}
        cms = []
        if (d / "comments.csv").is_file():
            with open(d / "comments.csv", encoding="utf-8-sig", newline="") as f:
                for r in csv.DictReader(f):
                    cms.append({"cid": r.get("id") or "", "text": str(r.get("text") or ""), "likes": int(float(r.get("likes") or 0)),
                                "reply": str(r.get("is_reply")) in ("1", "True", "true"), "creator": str(r.get("creator")) in ("1", "True", "true"),
                                "published": r.get("published") or ""})
        yield d, meta, info, cms


def viewer_comments(out):
    """시청자 댓글 전부 (채널 주인·빈 댓글 뺌) — 영상 정보와 함께."""
    rows = []
    for d, meta, info, cms in iter_videos(out):
        lg = lang_group(meta, info)
        for m in cms:
            if m["creator"] or not m["text"].strip():
                continue
            rows.append({**m, "video_id": meta.get("id"), "lang_group": lg})
    return rows


# ---------------------------------------------------------------- 표본
def sample_path(out):
    return Path(out) / "comment_type_sample.tsv"


def labels_path(out):
    return Path(out) / "comment_type_labels.tsv"


def cmd_sample(topic):
    out = ROOT / topic / "result" / "outliers"
    rows = viewer_comments(out)
    pop = Counter(r["lang_group"] for r in rows)
    rng = random.Random(SEED)
    picked = []
    for lg, n in SAMPLE_SIZES.items():
        pool = sorted((r for r in rows if r["lang_group"] == lg), key=lambda r: (r["video_id"], r["cid"]))   # 순서 고정 → 씨앗이 같으면 같은 표본
        picked += [(lg, r) for r in rng.sample(pool, min(n, len(pool)))]
    p = sample_path(out)
    with p.open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["sid", "half", "lang_group", "video_id", "comment_id", "is_reply", "likes", "text"])
        for k, (lg, r) in enumerate(picked, 1):
            w.writerow([f"s{k:04d}", "조정" if k % 2 else "시험", lg, r["video_id"], r["cid"], r["reply"], r["likes"], clean(r["text"])])
    log("SAMPLE", topic=topic, file=str(p), seed=SEED, population=dict(pop), sample={lg: min(n, pop[lg]) for lg, n in SAMPLE_SIZES.items()},
        population_total=len(rows), note="절반(홀수 번호)=조정 — 규칙을 고칠 때만 봄, 절반(짝수)=시험 — 정확도만 잼")
    return {"sample": len(picked), "population": len(rows)}


def load_sample(out):
    s = {r["sid"]: r for r in csv.DictReader(sample_path(out).open(encoding="utf-8"), delimiter="\t")}
    lab = {}
    if labels_path(out).is_file():
        for r in csv.DictReader(labels_path(out).open(encoding="utf-8"), delimiter="\t"):
            if r["type"] not in TYPES:
                raise SystemExit(f"[LABEL] ❌ 모르는 유형 {r['type']!r} (sid {r['sid']}) — {', '.join(TYPES)}")
            lab[r["sid"]] = r["type"]
    return s, lab


# ---------------------------------------------------------------- 규칙 (B) — '조정' 절반(550개)만 보고 만듦 (조정 정확도 66.5%)
# 2026-10-22 고정 — 그 뒤 '시험' 절반을 사람이 분류해 정확도를 잼 (규칙을 시험 절반에 맞춰 고치지 않음). 한국어 낱말은 success_analysis 규칙을 이어 씀.
RULES_VERSION = "v1"
F = re.I | re.S
def rx(p): return re.compile(p, F)
SPAM = rx(sa.SPAM_RX + r"|whats ?app|telegram|\bCFP\b|financial (advis|plann)|portfolio'?s? (is )?up|p0rtfolio|(his|her) (guidance|approach|strategy|service)|"
          r"teach me|get across to|(who|what) is the (person|name)|username|verified ✅|\+\d{8,}|[\U0001D400-\U0001D7FF]{3,}|"
          r"\b(question|ques|qus)\s*(no\.?)?\s*\d|\bans(wer)?\s*\d|\bq\s*\d\b|quiz|응모|이벤트 ?참여|출석|출첵|출책|"
          r"SPACX|SPCX|grokvortex|from us\$|minimum profit|liquidated on a scalp|i wish i saw this")
POL = rx(sa.NEED_CATS[sa.CAT_POLITICS] + r"|특검|이죄명|죄명|찢|재명|윤석|문재|이재|정은경|민주당|더불어|국힘|좌빨|빨갱|좌파|우파|공산|사회주의|탄핵|하야|청와대|장관|국회|국회의원|"
         r"정권|정부|나라를|나라가|나라 ?망|국가 ?부채|국민연금.{0,15}(특검|책임|처벌|손|날|운용|농단|조사|개입|원칙|리밸|관계자|수장|골빈)|연기금|금감원|금융위|"
         r"세금|과세|공매도 ?금지|상법|선거|지지율|정책|관세|매국|반국가|경로당|유승민|김재원|주진우|대한민국|국민청원|기자회견|외교|무보수|정치|감옥|구속|처벌|탈조선|호남|전라도|집어넣|책임질|"
         r"\b(trump|biden|harris|democrat|dems|republican|gop|government|govt|congress|president|election|midterm|tariff|bailout|taxpayers?|politician|"
         r"communis\w*|socialis\w*|nirmala|sebi|modi|bjp|anti ?national|ltcg|fm|politicians?|public money|regime|corrupt\w*|taxe?s?|slaves?)\b|9/11|islam|muslim|genossen|stasi")
ASK_KO = rx(sa.EXPLICIT_ASK + r"|(나요|까요|가요|인가요|건가요|을까요|는지요|되나요|맞나요|있나요|없나요|할까요|하나요|될까요|인지요|가능할까요|나을까요|좋을까요|되죠|하죠|어떤가요|뭔가요|무엇인가요|얼마인가요)\s*[?？]|"
            r"(어떻게|어디|언제|얼마|몇|무슨|어느).{0,30}(요|까|니까)\s*[?？]|해 ?주세요|해주시면|주실 ?수|부탁|궁금(합니다|해요|하네요|한데요|한 ?점)|^\s*혹시|(나요|까요|가요|인가요|건가요|셨나요|맞죠|되죠|하죠|인지요)\s*[?？]*\s*[ㅋㅎ]*\s*$")
ASK_EN = rx(r"(^|[.!]\s+|\n)\s*(what|how|why|when|which|where|who|should|could|can|is|are|do|does|did|will|would|any|anyone)\b[^?]{2,200}\?|"
            r"\b(please|pls|plz|kindly)\b.{0,40}\b(do|make|cover|explain|analy[sz]e|discuss|continue|talk|share|teach|tell|batao|bataye|banayen|banaye)|"
            r"(can|could|would) you (make|do|cover|explain|talk|compare|analy[sz]e|share)|video on|request|batao|bataye|kaise|kab |kya .{0,40}\?|sir .{0,60}\?|kitna|konsi|cheppandi|gurinch|sikha|sakha|bolo|bola kro|^\s*(what|how|why|which|where) .{8,}|\b(kya|kahan|kaise|kab|kaun|batau|batao|bataye|pannalama|karen)\b")
RHET = rx(sa.RHETORICAL + r"|말이 ?돼|되냐|하냐|있냐|없냐|거냐|건가\?|ㅋㅋ.*\?|\?.*ㅋㅋ")
CRIT = rx(r"사기꾼|사기 ?꾼|낚시|어그로|광고|말 ?바꾸|말 ?돌리|헛소리|개소리|뇌피셜|언제적|실력도 ?없|무슨 ?박사|어디 ?박사|박사여|이 ?양반|저 ?양반|이 ?사람|저 ?사람|"
          r"전문가.{0,15}(믿|없|틀|반대|말 ?듣|척)|유튜버|계좌 ?(까|공개)|틀렸|틀린|맞지도 ?않|고장난 ?시계|간과|매국 ?방송|희망 ?없는 ?소리|멍청|한심|"
          r"\b(clickbait\w*|scam\w*|terrible|fear ?monger\w*|superficial|annoying|distracting|bla bla|pumped|propaganda|grifter|hubris|wrong|bad investor|title)\b|"
          r"you put an ad|what'?s the plan|in title|hohl|schlimm|propaganda|got paid|paid (heavily|for this)|sponsored|왜 ?찍|뭔 ?소린|말라 ?해서|라더니|하더니|하더만|멤버쉽에서만|ハードル")
EXP = rx(r"(?<![가-힣])(저는|제가|저도|나도|내가|저희|전 |난 )|물렸|물려|물린 ?(지|채)|손실 ?(중|남|이|봤)|손해 ?봤|익절|손절 ?했|샀|팔았|매수했|매도했|매수 ?들어|들어갔|담았|담음|버티기 ?했|"
         r"평단|계좌 ?(다|가|에)|원금 ?생각|파이어 ?했|모으고 ?있|모아 ?가는|투자 ?중|보유 ?중|-\d+ ?%|\d+ ?(억|만원|천만원).{0,10}(잃|날|손실|벌)|퇴직금.{0,10}(넣|절반)|"
         r"(고 ?있어요|고 ?있습니다|중입니다|중이에요|했어요|했네요|했는데|했습니다만|됐네요|녹아|날렸|잃었|내 ?종목)|profit hua|loss hua|\bpersonally\b|"
         r"\bI('m| am| have| bought| sold| own| lost| started| just| was| made)\b|\bmy (portfolio|account|shares|position|trade)\b|\bmaine\b|\bmera\b|\bmeri\b|私|僕")
INFO = rx(r"^\s*\d{1,2}:\d{2}.{3,}|타임라인|요약|정리:|출처|기사|발표했|according to|reuters|confirmed|\bsource\b|show starts|분배락|배당락|세금 ?제하면|무료입니다")
PRAISE = rx(r"감사|고맙|고마워|응원|화이팅|파이팅|유익|좋은 ?(영상|정보|분석|내용|강의|방송|말씀)|잘 ?(봤|보고|들었|정리|분석|설명)|최고|귀에 ?쏙|이해가 ?(잘|쏙)|쉽게 ?설명|정답이지|든든|"
            r"\b(thank\w*|thanks|thx|great (video|content|info\w*|job|explanation|reporting|podcast|work)|love (you|this|it)|amazing|awesome|informative|helpful|useful|god bless|nice|well done|brilliant|wonderful|excellent)\b|"
            r"guru ?ji|bhaiya|bhai|sir ji|❤|すごく|腑に落ち|癒し|ありがと|DANKE|موفقة|ممتاز")
OPIN = rx(r"주식|투자|매수|매도|시장|증시|코스피|코스닥|국장|미장|나스닥|S&P|에스앤피|삼전|닉스|하이닉스|삼성|반도체|ETF|레버리지|배당|금리|환율|바닥|폭락|급락|하락|상승|오르|떨어|빠지|"
          r"존버|장투|장기|단타|분할|적립|현금|비중|사라|팔아|사면|팔면|답이다|답입니다|해야|된다|안 ?된다|버블|거품|개미|외인|외국인|기관|실적|주가|"
          r"투기|빚투|떡상|떡락|파는|파느냐|사느냐|대비|공포|탐욕|부동산|매출|수요|미수|반대매매|IMF|"
          r"\b(stock\w*|market\w*|buy\w*|sell\w*|crash\w*|bull\w*|bear\w*|invest\w*|etf\w*|rates?|fed|inflation|recession|cash|gold|crypto|leverag\w*|bonds?|"
          r"nasdaq|s&p|dip|trade|trading|shares?|valuation|overvalued|hedge|profit|loss|dividend\w*|yield|greed|crisis|savings|wealth|financial|money|forex|crypto)\b|"
          r"株|投資|積立|相場|Börse|Aktie|faiz|borsa|trade|strategy|market")
LAUGH = rx(r"^[\sㅋㅎㅠㅜ😂🤣😅😆😁🙂😊❤️♥💯👍🎉🔥😢😭🙏!?.~^]*$|^(ㅋ|ㅎ|lol|lmao|haha)+")
PRAISE_STRONG = rx(r"유익(했|하고|한)|잘 ?시청|이해가 ?(정말 ?)?(잘|쏙)|공감(되|이 ?가)|도움이 ?(많이 ?)?(됐|되었|됩니다|돼요)|배울 ?수 ?있|"
                    r"감사(합니다|드립니다|해요)\s*[.!~^😊❤]*\s*$|\b(thank you|thanks|great (video|content|explanation|reporting|podcast)|very (useful|informative)|appreciate)\b|"
                    r"धन्यवाद|बेहतरीन|शानदार")
LAUGHY = rx(r"ㅋㅋ|ㅎㅎ|😂|🤣|ㄷㄷ|\blol\b|\blmao\b|haha")
EN_Q = rx(r"^(?!.*[가-힣]).{3,120}\?\s*$")
def classify(text):
    """댓글 → 유형 코드 하나 (TYPES 또는 OTHER='X'). 규칙 v1 — 위에서부터 먼저 맞는 것 (순서 = 표본 분류의 애매할 때 순서와 같은 뜻)."""
    t = str(text or "")
    core = re.sub(r"@\S+", "", t)
    core_s = re.sub(r"[\s\W_]+", "", core)
    if SPAM.search(t): return "S"
    if POL.search(core): return "G"
    if (ASK_KO.search(core) and not RHET.search(core)) or ASK_EN.search(core): return "Q"
    if CRIT.search(core): return "C"
    if PRAISE_STRONG.search(core): return "P"
    if EXP.search(core): return "E"
    if INFO.search(core): return "I"
    if LAUGH.search(core.strip()) or len(core_s) <= 3: return "R"
    if PRAISE.search(core) and len(core_s) <= 60: return "P"
    if EN_Q.search(core): return "Q"
    if OPIN.search(core): return "O"
    if LAUGHY.search(core) and len(core_s) <= 30: return "R"
    if len(core_s) <= 6: return "R"
    if PRAISE.search(core): return "P"
    if len(core_s) <= 20: return "R"
    return OTHER


# ---------------------------------------------------------------- 평가
def cmd_evaluate(topic):
    out = ROOT / topic / "result" / "outliers"
    s, lab = load_sample(out)
    res = {}
    for half in ("조정", "시험"):
        ids = [k for k, r in s.items() if r["half"] == half and k in lab]
        conf = Counter((lab[k], classify(s[k]["text"])) for k in ids)
        acc = sum(v for (a, b), v in conf.items() if a == b) / len(ids) if ids else None
        per = {}
        for c in TYPES:
            tp = conf[(c, c)]
            pred = sum(v for (a, b), v in conf.items() if b == c)
            true = sum(v for (a, b), v in conf.items() if a == c)
            per[c] = {"precision": tp / pred if pred else None, "recall": tp / true if true else None, "true": true, "pred": pred}
        other = sum(v for (a, b), v in conf.items() if b == OTHER) / len(ids) if ids else None
        res[half] = {"n": len(ids), "accuracy": acc, "other_share": other, "per_type": per,
                     "confusion": {f"{a}>{b}": v for (a, b), v in sorted(conf.items())}}
        log("EVAL", topic=topic, half=half, n=len(ids), accuracy=round(acc, 3) if acc is not None else "-",
            other_share=round(other, 3) if other is not None else "-")
    return res


# ---------------------------------------------------------------- 보고서
MIN_ROW = 5                 # 보정표 한 줄(규칙이 이 유형이라 한 표본)이 이보다 적으면 언어를 합친 줄을 씀
WEEKS = 4


def wilson(k, n, z=1.96):
    """비율 k/n 의 95% 범위 (Wilson)."""
    if not n:
        return None, None
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return max(0.0, c - h), min(1.0, c + h)


def calib_rows(s, lab):
    """보정표: 규칙이 k 라고 한 '시험' 절반 표본 중 사람이 t 라고 한 몫 — 언어 묶음별 + 합친 것. 규칙은 '조정' 절반에 맞춰졌으므로 '시험' 절반만 씀."""
    rows = defaultdict(lambda: defaultdict(Counter))
    for k, r in s.items():
        if r["half"] != "시험" or k not in lab:
            continue
        rk = classify(r["text"])
        rows[r["lang_group"]][rk][lab[k]] += 1
        rows["전체"][rk][lab[k]] += 1
    return rows


def calibrate(rule_counts, lg, rows, fallback):
    """규칙 유형 수 → 보정한 실제 유형 몫 (Σ 규칙 몫 × P(사람 유형 | 규칙 유형)). 줄이 MIN_ROW 미만이면 언어를 합친 줄, 그것도 없으면 fallback(그 언어 표본 분포)."""
    n = sum(rule_counts.values())
    est = Counter()
    if not n:
        return {}
    for rk, cnt in rule_counts.items():
        row = rows.get(lg, {}).get(rk)
        if not row or sum(row.values()) < MIN_ROW:
            row = rows["전체"].get(rk)
        if not row or sum(row.values()) < MIN_ROW:
            row = fallback
        tot = sum(row.values())
        for t, v in row.items():
            est[t] += cnt / n * v / tot
    return {t: est.get(t, 0.0) for t in TYPES}


def comment_frame(topic, now):
    """댓글 전부 → (언어 묶음, 나라, 묶음, 주, 답글, 좋아요, 규칙 유형). 나라·묶음은 title_comment_link·analysis.json 과 같은 규칙."""
    import title_comment_link as tcl
    out = ROOT / topic / "result" / "outliers"
    an = json.loads((out / "analysis.json").read_text("utf-8")) if (out / "analysis.json").is_file() else {}
    success_ids = {c["id"] for c in an.get("success_cases") or []}
    vpd_ids = {c["id"] for c in (an.get("vpd_top") or {}).get("cases") or []}
    chp = tcl.channels_path(out)
    ch = json.loads(chp.read_text("utf-8")) if chp.is_file() else {}
    rows = []
    for d, meta, info, cms in iter_videos(out):
        lg = lang_group(meta, info)
        cc = tcl.country_of({"lang": info.get("lang") or meta.get("video_lang"), "audio_lang": info.get("audio_lang"), "channel_id": meta.get("channel_id")}, ch) or "그 밖 나라"
        vid = meta.get("id")
        grp = "성공 사례" if vid in success_ids else ("하루 조회수 상위" if vid in vpd_ids else "그 밖의 승인 영상")
        try:
            age = (now - datetime.fromisoformat(str(meta.get("published_at") or meta.get("published"))[:10]).replace(tzinfo=timezone.utc)).days
        except ValueError:
            age = None
        wk = (age // 7 + 1) if age is not None and 0 <= age < WEEKS * 7 else None
        for m in cms:
            if m["creator"] or not m["text"].strip():
                continue
            rows.append({"lg": lg, "country": cc, "group": grp, "week": wk, "reply": m["reply"], "likes": m["likes"], "rule": classify(m["text"]), "vid": vid})
    return rows


def cmd_report(topic):
    out = ROOT / topic / "result" / "outliers"
    now = datetime.now(timezone.utc)
    s, lab = load_sample(out)
    ev = cmd_evaluate(topic)
    rows_c = calib_rows(s, lab)
    # A. 표본(사람) 분포 — 언어 묶음별 + 전체(모집단 크기로 가중)
    frame = comment_frame(topic, now)
    pop = Counter(r["lg"] for r in frame)
    samp = {}
    for lg in list(SAMPLE_SIZES) + ["전체"]:
        ids = [k for k, r in s.items() if k in lab and (lg == "전체" or r["lang_group"] == lg)]
        if lg == "전체":
            w = {g: pop[g] / sum(pop.values()) for g in SAMPLE_SIZES}
            share = {t: sum(w[g] * samp[g]["share"][t] for g in SAMPLE_SIZES) for t in TYPES}
            samp[lg] = {"n": len(ids), "share": share, "ci": {}, "weights": w}
            continue
        c = Counter(lab[k] for k in ids)
        samp[lg] = {"n": len(ids), "share": {t: c[t] / len(ids) for t in TYPES}, "ci": {t: wilson(c[t], len(ids)) for t in TYPES}}
    fallback = {lg: Counter({t: samp[lg]["share"][t] * 1000 for t in TYPES}) for lg in SAMPLE_SIZES}

    def est(sel, lg_hint=None, weight=None):
        """고른 댓글 → (수, 규칙 몫, 보정 몫). 언어가 섞이면 언어별로 보정해 수로 가중."""
        by_lg = defaultdict(Counter)
        for r in sel:
            by_lg[r["lg"]][r["rule"]] += (r["likes"] if weight == "likes" else 1)
        tot = sum(sum(c.values()) for c in by_lg.values())
        rule_share = Counter()
        cal = Counter()
        for lg, c in by_lg.items():
            n_lg = sum(c.values())
            for k, v in c.items():
                rule_share[k] += v / tot if tot else 0
            for t, v in calibrate(c, lg, rows_c, fallback[lg]).items():
                cal[t] += v * n_lg / tot if tot else 0
        return {"n": len(sel), "weight_total": tot, "rule": {k: rule_share.get(k, 0.0) for k in TYPE_ORDER}, "calibrated": {t: cal.get(t, 0.0) for t in TYPES}}

    data = {"tool": f"comment_types.py {VERSION}", "rules": RULES_VERSION, "topic": topic, "generated": now.isoformat(timespec="minutes"),
            "seed": SEED, "population": dict(pop), "population_total": len(frame), "types": {k: {"name": v[0], "def": v[1]} for k, v in TYPES.items()},
            "evaluate": ev, "sample": samp, "by_lang": {}, "by_group": {}, "by_week": {}, "by_reply": {}, "likes_weighted": {}}
    for lg in SAMPLE_SIZES:
        data["by_lang"][lg] = est([r for r in frame if r["lg"] == lg])
    data["by_lang"]["전체"] = est(frame)
    for cc in ("한국", "미국"):
        for g in ("성공 사례", "하루 조회수 상위", "그 밖의 승인 영상"):
            data["by_group"][f"{cc}|{g}"] = est([r for r in frame if r["country"] == cc and r["group"] == g])
        for wk in list(range(1, WEEKS + 1)) + [0]:
            data["by_week"][f"{cc}|{wk}"] = est([r for r in frame if r["country"] == cc and (r["week"] == wk if wk else r["week"] is None)])
        for rp in (False, True):
            data["by_reply"][f"{cc}|{'답글' if rp else '원댓글'}"] = est([r for r in frame if r["country"] == cc and r["reply"] == rp])
        data["likes_weighted"][cc] = est([r for r in frame if r["country"] == cc], weight="likes")
    (out / "comment_types.json").write_text(json.dumps(data, ensure_ascii=False, indent=1, default=str), "utf-8")
    write_md(out, data)
    log("REPORT", topic=topic, file=str(out / "comment_types.md"), comments=len(frame), sample=sum(1 for _ in lab),
        test_accuracy=round(ev["시험"]["accuracy"], 3), other_share_all=round(data["by_lang"]["전체"]["rule"][OTHER], 3))
    return data


def pct(x):
    return "-" if x is None else f"{x * 100:.0f}%"


def write_md(out, data):
    ev = data["evaluate"]
    L = ["# 댓글 유형 — 모든 댓글에 유형 하나 (표본 + 규칙)", "",
         f"자동 생성 — `tools/comment_types.py` {VERSION} · 규칙 {data['rules']} ({data['generated']} UTC). **숫자만** — 해석·지시사항은 읽는 AI 가. ※ 연구·교육용 — 투자 권유가 아님.", "",
         "## 0. 방법과 한계 (먼저 읽기)", "",
         f"- **모집단** = 승인한 영상의 시청자 댓글 전부 {data['population_total']:,}개 (채널 주인·빈 댓글 뺌, 답글 포함): "
         + " · ".join(f"{k} {v:,}" for k, v in data["population"].items()) + ". 언어 묶음 = 영상 언어(한국어·영어·그 밖).",
         f"- **A. 표본(사람)** — 언어 묶음별 무작위 {', '.join(f'{k} {v}' for k, v in SAMPLE_SIZES.items())}개 (씨앗 {data['seed']} — 다시 뽑아도 같음, "
         "`comment_type_sample.tsv`). 한 사람(Claude)이 댓글마다 **유형 하나**를 붙임 (`comment_type_labels.tsv`, 정의는 1번). 한 사람 판단이라 애매한 댓글(반어·맥락)은 사람마다 다를 수 있다.",
         f"- **B. 규칙** — 표본 절반('조정')만 보고 만든 낱말 규칙 {data['rules']} 을 댓글 전부에 적용. 정확도: 조정 절반 {pct(ev['조정']['accuracy'])} · "
         f"**처음 보는 시험 절반 {pct(ev['시험']['accuracy'])}** (규칙에 안 걸림 {pct(ev['시험']['other_share'])}). → 댓글 하나하나의 규칙 유형은 절반쯤 틀린다.",
         "- **보정** — 규칙 유형 몫에 '시험 절반에서 규칙이 k 라고 한 댓글이 사람 기준 무엇이었나'를 곱해 실제 몫을 추정 (언어별, 표본이 "
         f"{MIN_ROW}개 미만인 줄은 언어를 합침). 묶음·나라·주가 달라도 규칙이 틀리는 꼴은 같다고 가정한다 — 그래서 묶음별 숫자는 어림값이다.",
         "- **가장 믿을 숫자는 2번(표본)** — 묶음·주별 비교(5~8번)는 보정 어림값으로 '차이의 방향'만 본다. 칸 = **보정 (괄호 안 = 규칙 그대로)**. 규칙이 절반쯤 틀리므로 "
         "보정은 묶음 사이 차이를 줄이는 쪽으로 기운다 — 두 숫자가 같은 방향으로 다를 때만 차이로 본다. 나라: 한국 = 한국어 영상, 미국 = 채널 나라 US 인 영어 영상.",
         "- 기존 `analysis.md` 8번(성공 사례만·낱말 갈래)과 `weekly.md` 니즈 줄은 이 유형과 다른 규칙이다 — 그 표의 '어느 갈래에도 안 듦' 줄을 같이 볼 것.", "",
         "## 1. 유형 (댓글 하나 = 유형 하나, 애매하면 광고 > 정치 > 질문 > 비판 > 경험 > 의견 > 정보 > 칭찬 > 반응 순서로 앞의 것)", "",
         "| 코드 | 유형 | 정의 |", "|---|---|---|"]
    for k, v in TYPES.items():
        L.append(f"| {k} | {v[0]} | {v[1]} |")
    L += ["", "## 2. 실제 분포 — 표본(사람이 분류) · 95% 범위", "",
          "| 유형 | " + " | ".join(f"{lg} (n={data['sample'][lg]['n']})" for lg in SAMPLE_SIZES) + " | 전체 (모집단 크기로 가중) |",
          "|---|" + "---|" * (len(SAMPLE_SIZES) + 1)]
    for t in TYPES:
        cells = []
        for lg in SAMPLE_SIZES:
            sm = data["sample"][lg]
            lo, hi = sm["ci"][t]
            cells.append(f"{pct(sm['share'][t])} ({pct(lo)}~{pct(hi)})")
        L.append(f"| {type_name(t)} | " + " | ".join(cells) + f" | **{pct(data['sample']['전체']['share'][t])}** |")
    L += ["", "## 3. 규칙 정확도 — 처음 보는 '시험' 절반 (사람 기준)", "",
          "| 유형 | 사람 기준 수 | 규칙이 그 유형이라 한 수 | 맞힌 몫(정밀도) | 찾아낸 몫(재현율) |", "|---|---|---|---|---|"]
    for t in TYPES:
        p = ev["시험"]["per_type"][t]
        L.append(f"| {type_name(t)} | {p['true']} | {p['pred']} | {pct(p['precision'])} | {pct(p['recall'])} |")
    L += [f"| 그 밖 (규칙에 안 걸림) | - | {sum(v for k2, v in ev['시험']['confusion'].items() if k2.endswith('>' + OTHER))} | - | - |", "",
          "## 4. 댓글 전부 — 규칙 몫 vs 보정 어림값 (언어 묶음별)", "",
          "| 유형 | " + " | ".join(f"{lg} 규칙 · 보정" for lg in list(SAMPLE_SIZES) + ["전체"]) + " |", "|---|" + "---|" * (len(SAMPLE_SIZES) + 1)]
    for t in TYPE_ORDER:
        cells = []
        for lg in list(SAMPLE_SIZES) + ["전체"]:
            b = data["by_lang"][lg]
            cells.append(f"{pct(b['rule'].get(t))} · {pct(b['calibrated'].get(t)) if t in TYPES else '-'}")
        L.append(f"| {type_name(t)} | " + " | ".join(cells) + " |")
    L.append("| 댓글 수 | " + " | ".join(f"{data['by_lang'][lg]['n']:,}" for lg in list(SAMPLE_SIZES) + ["전체"]) + " |")

    def table(title, keys, label):
        L.extend(["", title, "", "| 유형 | " + " | ".join(label(k) for k in keys) + " |", "|---|" + "---|" * len(keys)])
        for t in TYPES:
            L.append(f"| {type_name(t)} | " + " | ".join(f"{pct(data_for(k)['calibrated'].get(t))} ({pct(data_for(k)['rule'].get(t))})" for k in keys) + " |")
        L.append("| 그 밖 (규칙에 안 걸림) | " + " | ".join(f"- ({pct(data_for(k)['rule'].get(OTHER))})" for k in keys) + " |")
        L.append("| 댓글 수 | " + " | ".join(f"{data_for(k)['n']:,}" for k in keys) + " |")

    groups = [f"{cc}|{g}" for cc in ("한국", "미국") for g in ("성공 사례", "하루 조회수 상위", "그 밖의 승인 영상")]
    data_for = lambda k: data["by_group"][k]          # noqa: E731
    table("## 5. 묶음별 (보정 어림값) — 성공 사례 · 하루 조회수 상위(analysis.md 1-3) · 그 밖", groups, lambda k: k.replace("|", " · "))
    weeks = [f"{cc}|{wk}" for cc in ("한국", "미국") for wk in list(range(1, WEEKS + 1)) + [0]]
    data_for = lambda k: data["by_week"][k]           # noqa: E731
    table("## 6. 올린 주별 (보정 어림값) — 1주 전 = 올린 지 0~6일, '그 전' = 4주보다 전", weeks,
          lambda k: k.split("|")[0] + " · " + (f"{k.split('|')[1]}주 전" if k.split("|")[1] != "0" else "그 전"))
    reps = [f"{cc}|{x}" for cc in ("한국", "미국") for x in ("원댓글", "답글")]
    data_for = lambda k: data["by_reply"][k]          # noqa: E731
    table("## 7. 원댓글 vs 답글 (보정 어림값)", reps, lambda k: k.replace("|", " · "))
    data_for = lambda k: data["likes_weighted"][k]    # noqa: E731
    table("## 8. 좋아요로 가중 — 관심 많은 댓글 몫 (보정 어림값, 좋아요 합 기준)", ["한국", "미국"], lambda k: k)
    (Path(out) / "comment_types.md").write_text("\n".join(L) + "\n", "utf-8")


def main(argv=None):
    ap = argparse.ArgumentParser(description="모든 댓글에 유형 하나 — 표본(사람) + 규칙(전부), 할당량 0")
    ap.add_argument("topic")
    ap.add_argument("cmd", choices=["sample", "evaluate", "report"])
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args(argv)
    logging.basicConfig(level=getattr(logging, a.log_level), format="%(message)s", stream=sys.stderr)
    log("START", topic=a.topic, cmd=a.cmd, tool=f"comment_types.py {VERSION}")
    if a.cmd == "sample":
        res = cmd_sample(a.topic)
    elif a.cmd == "evaluate":
        res = cmd_evaluate(a.topic)
    else:
        res = cmd_report(a.topic)
    log("DONE", cmd=a.cmd)
    return res


if __name__ == "__main__":
    main()
