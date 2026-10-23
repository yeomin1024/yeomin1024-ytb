#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.2.0 — 2026-10-23 — ① 대본의 [장면] 카드와 그 줄은 문장으로 세지 않음 (srt_tool.parse_txt 와 같음 — 개미 재기 일지 정리 카드 · 103줄 vs 97문장)
#          ② 한국어 '조'·'천억' 단위 · '2억 5천'(만 없이) = 2억 5천만 ③ 번역 단위 낱말(trillion·Milliarden·triliun·nghìn tỷ·करोड़ …)과 일본어 붙은 단위
#          (38兆6千億) — 1화 언어별 자막 번역에서 찾음 (사용자 지시 2026-10-23 "외국인 대상으로도 할거니까 그것도 고려해 …").
# (v1.1.0) — 2026-10-18 — build 자막 나누기 고침: 덩어리가 문장의 25% 보다 짧게 나뉘지 않음 (일본어 '本当かどうか、' 0.8초짜리) · 일본어 줄바꿈은
#          조사·구두점 뒤에서, 영문·숫자 낱말(Python·ETF·1,700) 안에서는 끊지 않음 (예전엔 20자마다 '実|際' 처럼 끊음). 첫 실제 오디오 SRT 점검 때 찾음
#          (사용자 지시 2026-10-18 "채권 표현 수정하고 영상 업로드 할 준비해").
# v1.0.2 — 2026-10-17 — 한국어 '1'(1년에·1주에)은 번역에 숫자가 없어도 됨 — 'per year' 처럼 자연스럽게.
# v1.0.1 — 2026-10-17 — 숫자 읽기 두 곳 고침: 'K·M' 줄임은 뒤에 글자가 없을 때만 (베트남어 '100 mà' 가 1억으로 읽힘) · 일본어 '7万5千' 은 75,000 하나로 (7万·5千 따로 세지 않음).
# v1.0 — 2026-10-17 — 최초. 언어별 자막 대본(번역) 검사 + SRT 만들기 (사용자 지시 2026-10-17 "외국어 자막 대본도 필요하지? 쇼츠, 롱폼 각각
#          언어별로 작성해봐"). 화면에는 자막을 굽지 않고(주식 — 언어 없는 화면), 언어별 자막 파일(CC)을 올린다.
#          자막 대본 = 한국어 대본(<영상ID>.txt)과 문장 1:1 — 파트 줄('-…')은 한국어 그대로, 문장 줄만 번역.
#            롱폼  <주제>/source/<영상ID>/subs/<영상ID>.<언어>.txt
#            쇼츠  <주제>/source/<영상ID>/shorts/subs/<영상ID>-shorts.<언어>.txt
#          check: 문장 수·파트 줄이 한국어와 같은가 · 번역 줄에 한글이 없는가 · 한국어 문장의 숫자가 번역에 모두 있는가(월은 달 이름도 됨,
#                 '7만 5천' = 75,000, 언어마다 소수점·천 단위 표기) · 읽는 속도(한국어 예상 길이 대비 글자/초 — 경고만).
#          build: 장면 파일 EP 자료(video/episodes/<영상ID>/index.html — render.mjs sync 가 넣은 문장 시각)로 언어마다 SRT.
#                 오디오 시각이면 자막 폴더에 <영상ID>.<언어>.srt (올릴 것), 추정 시각(--estimated)이면 <주제>/out/<영상ID>/subs/ (점검만).
"""
python3 tools/subs_tool.py check stock [영상ID ...]          # 영상ID 를 빼면 그 주제 자막 대본 전부 · 문제가 있으면 끝 코드 1
python3 tools/subs_tool.py build stock <영상ID> [--estimated] # 언어별 SRT (오디오 시각이 아니면 --estimated 로만)
python3 tools/subs_tool.py status stock                        # 영상마다 어떤 언어 대본·SRT 가 있는지
"""
import argparse
import json
import logging
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import srt_tool  # noqa: E402

LANGS = ["en", "hi", "id", "pt", "es-419", "ja", "de", "vi", "tr"]          # 롱폼 upload.md 5번 localizations 와 같은 9개 (+ 기본 ko)
LANG_NAME = {"ko": "한국어", "en": "English", "hi": "हिन्दी", "id": "Bahasa Indonesia", "pt": "Português", "es-419": "Español (Latinoamérica)",
             "ja": "日本語", "de": "Deutsch", "vi": "Tiếng Việt", "tr": "Türkçe"}
DEC_COMMA = {"id", "pt", "de", "vi", "tr"}                                    # 소수점 쉼표 · 천 단위 점 (upload.md 설명란과 같은 표기)
CJK = {"ja"}
# v1.2.0 번역의 단위 낱말 (긴 말 먼저) — '38.6 trillion' 처럼 써도 한국어 '38조 6천억' 과 같은 값으로 셈
SCALE = {
    "en": [("thousand", 1e3), ("million", 1e6), ("billion", 1e9), ("trillion", 1e12)],
    "es-419": [("mil millones", 1e9), ("billón", 1e12), ("billones", 1e12), ("millón", 1e6), ("millones", 1e6), ("mil", 1e3)],
    "pt": [("trilhão", 1e12), ("trilhões", 1e12), ("bilhão", 1e9), ("bilhões", 1e9), ("milhão", 1e6), ("milhões", 1e6), ("mil", 1e3)],
    "de": [("billionen", 1e12), ("billion", 1e12), ("milliarden", 1e9), ("milliarde", 1e9), ("millionen", 1e6), ("million", 1e6), ("tausend", 1e3), ("bio.", 1e12), ("mrd.", 1e9), ("mio.", 1e6)],
    "id": [("triliun", 1e12), ("miliar", 1e9), ("juta", 1e6), ("ribu", 1e3)],
    "vi": [("nghìn tỷ", 1e12), ("ngàn tỷ", 1e12), ("tỷ", 1e9), ("triệu", 1e6), ("nghìn", 1e3), ("ngàn", 1e3)],
    "tr": [("trilyon", 1e12), ("milyar", 1e9), ("milyon", 1e6), ("bin", 1e3)],
    "hi": [("ट्रिलियन", 1e12), ("खरब", 1e11), ("अरब", 1e9), ("बिलियन", 1e9), ("करोड़", 1e7), ("मिलियन", 1e6), ("लाख", 1e5), ("हज़ार", 1e3), ("हजार", 1e3)],
}
LINE_CHARS = {"ja": 20}                                                        # 자막 한 줄 글자 수 (그 밖 42 — 방송 자막 관행)
MAX_CPS = {"ja": 13}                                                           # 읽는 속도 경고 (그 밖 21 글자/초)
EST = {"perSyl": 0.151, "comma": 0.25, "base": -0.08, "min": 0.8}              # render.mjs 추정 모델과 같은 값 (진행자 H04 실측)
MONTHS = {
    "en": "january february march april may june july august september october november december",
    "pt": "janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro",
    "es-419": "enero febrero marzo abril mayo junio julio agosto septiembre octubre noviembre diciembre",
    "de": "januar februar märz april mai juni juli august september oktober november dezember",
    "id": "januari februari maret april mei juni juli agustus september oktober november desember",
    "tr": "ocak şubat mart nisan mayıs haziran temmuz ağustos eylül ekim kasım aralık",
    "hi": "जनवरी फ़रवरी मार्च अप्रैल मई जून जुलाई अगस्त सितंबर अक्टूबर नवंबर दिसंबर",
}
MONTH_ALT = {"hi": {"फरवरी": 2, "सितम्बर": 9, "अक्तूबर": 10, "नवम्बर": 11, "दिसम्बर": 12}, "tr": {"subat": 2, "mayis": 5, "eylul": 9, "kasim": 11, "aralik": 12}}
HANGUL = re.compile(r"[가-힣ㄱ-ㅎㅏ-ㅣ]")
log = logging.getLogger("subs_tool")


def lg(stage, level=logging.INFO, **kv):
    log.log(level, "[%s] [%s] %s", stage, datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) and ' ' in v else v}" for k, v in kv.items()))


# ----------------------------------------------------------------------------- 파일
def ko_script(topic, vid):
    """영상ID → 한국어 대본 경로 (쇼츠는 '<롱폼>-shorts')."""
    if vid.endswith("-shorts"):
        base = vid[: -len("-shorts")]
        return ROOT / topic / "source" / base / "shorts" / f"{vid}.txt"
    return ROOT / topic / "source" / vid / f"{vid}.txt"


def subs_dir(topic, vid):
    return ko_script(topic, vid).parent / "subs"


def all_videos(topic):
    out = []
    for d in sorted((ROOT / topic / "source").iterdir()):
        if not d.is_dir() or d.name.startswith("_"):
            continue
        if (d / f"{d.name}.txt").exists() and (d / "upload.md").exists():
            out.append(d.name)
            if (d / "shorts" / f"{d.name}-shorts.txt").exists():
                out.append(f"{d.name}-shorts")
    return out


def structure(path):
    """대본 → [('label', '-도입') | ('s', 문장)] — 빈 줄·'#' 주석 줄 뺌. 한국어·번역 모두 같은 규칙 (srt_tool.is_label)."""
    out, in_card = [], False
    for raw in Path(path).read_text("utf-8-sig").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if srt_tool.is_label(line):
            in_card = False
            out.append(("label", line))
            continue
        if line.startswith("[장면]"):                                           # v1.2.0 말 없는 카드와 그 줄은 문장이 아님 (srt_tool.parse_txt 와 같음)
            in_card = True
            continue
        if not in_card:
            out.append(("s", line))
    return out


# ----------------------------------------------------------------------------- 숫자
KO_NUM = re.compile(r"(?<![\d.,])(\d[\d,]*(?:\.\d+)?)\s*(조|천억|억|천만|만|천)?")
KO_MUL = {"조": 1e12, "천억": 1e11, "억": 1e8, "천만": 1e7, "만": 1e4, "천": 1e3}


def ko_values(text):
    """한국어 문장 → [(값, 종류)] — 종류: 'month'(…월) · 'num'. '7만 5천' = 75000 · '1,024' = 1024 · '3억' = 3e8."""
    vals, i = [], 0
    toks = list(KO_NUM.finditer(text))
    while i < len(toks):
        m = toks[i]
        v = float(m.group(1).replace(",", ""))
        unit = m.group(2)
        mul = KO_MUL.get(unit, 1)
        v *= mul
        # '7만 5천' · '1억 2천만' — 큰 단위 뒤에 바로 더 작은 단위가 오면 더함
        while unit and i + 1 < len(toks):
            n = toks[i + 1]
            gap = text[m.end():n.start()]
            if gap.strip() or n.group(2) is None:
                break
            nmul = KO_MUL[n.group(2)]
            if n.group(2) == "천" and mul == 1e8 and not text[n.end():n.end() + 1] == "만":
                nmul = 1e7                                                      # v1.2.0 '2억 5천' (만 없이) = 2억 5천만 — 돈 말할 때 흔한 줄임
            if nmul >= mul:
                break
            v += float(n.group(1).replace(",", "")) * nmul
            mul, m, i = nmul, n, i + 1
        after = text[m.end():m.end() + 1]
        kind = "month" if (m.group(2) is None and after == "월") else "num"
        vals.append((round(v, 6), kind))
        i += 1
    return vals


def tr_values(text, lang):
    """번역 문장 → {값} (언어마다 소수점·천 단위 · 일본어 万·千 · K/M 줄임). 달 이름은 'month:<n>' 으로 따로."""
    out = set()
    t = text.replace(" ", " ").replace(" ", " ")
    if lang in CJK:
        JA = {"兆": 1e12, "千億": 1e11, "億": 1e8, "千万": 1e7, "万": 1e4, "千": 1e3}
        unit = r"(兆|千億|億|千万|万|千)"
        for m in re.finditer(rf"(?:\d[\d,]*(?:\.\d+)?\s*{unit}\s*)+", t):        # v1.2.0 38兆6千億 · 2億5千万 · 7万5千 — 붙은 단위는 한 덩어리로 더함
            v = sum(float(a.replace(",", "")) * JA[u] for a, u in re.findall(rf"(\d[\d,]*(?:\.\d+)?)\s*{unit}", m.group(0)))
            out.add(round(v, 6))
        t = re.sub(rf"(?:\d[\d,]*(?:\.\d+)?\s*{unit}\s*)+", " ", t)
        for m in re.finditer(r"(\d[\d,]*(?:\.\d+)?)", t):
            out.add(round(float(m.group(1).replace(",", "")), 6))
        for m in re.finditer(r"(\d+)\s*月", t):
            out.add(f"month:{int(m.group(1))}")
        return out
    num = r"\d{1,3}(?:\.\d{3})+(?:,\d+)?|\d+(?:,\d+)?" if lang in DEC_COMMA else r"\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?"
    low_t = t.lower()
    for m in re.finditer(rf"(?<![\d.,])({num})\s*([KkMm](?![^\W\d_]))?", t):
        s = m.group(1)
        s = s.replace(".", "").replace(",", ".") if lang in DEC_COMMA else s.replace(",", "")
        rest = low_t[m.end():m.end() + 16].lstrip()                            # v1.2.0 단위 낱말 (38.6 trillion · 2,5 Milliarden · 250 juta …) — 곱한 값만 셈
        scaled = next((mul for word, mul in SCALE.get(lang, ()) if rest.startswith(word)), None)
        if scaled and not m.group(2):
            out.add(round(float(s) * scaled, 6))
            continue
        v = float(s) * {"k": 1e3, "m": 1e6, None: 1}[(m.group(2) or "").lower() or None]
        out.add(round(v, 6))
        if m.group(2):                                                         # 'K' 가 낱말 일부일 수도 — 줄이지 않은 값도 둠
            out.add(round(float(s), 6))
    low = t.lower()
    names = MONTHS.get(lang)
    if names:
        for n, name in enumerate(names.split(), 1):
            if re.search(rf"(?<!\w){re.escape(name)}(?!\w)", low):
                out.add(f"month:{n}")
    for name, n in MONTH_ALT.get(lang, {}).items():
        if name in low:
            out.add(f"month:{n}")
    if lang == "vi":
        for m in re.finditer(r"tháng\s*(\d+)", low):
            out.add(f"month:{int(m.group(1))}")
        for m in re.finditer(r"(\d+)/(\d{4})", low):                            # 12/2013
            out.add(f"month:{int(m.group(1))}")
    if lang in ("en", "hi", "es-419", "pt", "de", "id", "tr", "vi"):
        for m in re.finditer(r"(?<!\d)(\d{1,2})[./](\d{4})(?!\d)", t):          # 12.2013 · 12/2013
            out.add(f"month:{int(m.group(1))}")
    return out


def num_problems(ko, tr, lang):
    """한국어 숫자 중 번역에 없는 것 → [설명]. 번역에만 있는 숫자 → [경고]."""
    have = tr_values(tr, lang)
    missing, used = [], set()
    for v, kind in ko_values(ko):
        if v == 1 and kind == "num":                                           # '1년에'·'1주에' → 'per year'·'a share' 처럼 낱말로 옮겨도 됨 (v1.0.2)
            continue
        if v in have:
            used.add(v)
            continue
        if kind == "month" and f"month:{int(v)}" in have:
            used.add(f"month:{int(v)}")
            continue
        missing.append(f"{v:g}" + ("월" if kind == "month" else ""))
    ko_set = {v for v, _ in ko_values(ko)}
    extra = sorted(f"{x:g}" for x in have if isinstance(x, float) and x not in ko_set and x not in used)
    return missing, extra


# ----------------------------------------------------------------------------- 길이
def ko_seconds(text):
    """한국어 문장 예상 길이 (render.mjs 추정 모델과 같은 꼴 — 진행자 H04)."""
    syl = srt_tool.syllables(text) if hasattr(srt_tool, "syllables") else len(HANGUL.findall(text))
    commas = text.count(",")
    return max(EST["min"], syl * EST["perSyl"] + commas * EST["comma"] + EST["base"])


def visible_len(text):
    return len(re.sub(r"\s+", " ", text.strip()))


# ----------------------------------------------------------------------------- check
def check_video(topic, vid, langs=None):
    ko_path = ko_script(topic, vid)
    ko = structure(ko_path)
    rows, errors, warns = [], 0, 0
    for lang in langs or LANGS:
        p = subs_dir(topic, vid) / f"{vid}.{lang}.txt"
        if not p.exists():
            rows.append((lang, "—", "❌ 파일 없음", ""))
            errors += 1
            continue
        tr = structure(p)
        prob = []
        if [k for k, _ in tr] != [k for k, _ in ko]:
            prob.append(f"줄 구조 다름 (한국어 문장 {sum(1 for k, _ in ko if k == 's')} · 번역 {sum(1 for k, _ in tr if k == 's')})")
        else:
            for (k1, a), (k2, b) in zip(ko, tr):
                if k1 == "label" and a != b:
                    prob.append(f"파트 줄 다름: {a} ≠ {b}")
        n = 0
        for (k1, a), (k2, b) in zip(ko, tr):
            if k1 != "s" or k2 != "s":
                continue
            n += 1
            if HANGUL.search(b):
                prob.append(f"s{n} 한글 남음: {b[:40]}")
            miss, extra = num_problems(a, b, lang)
            if miss:
                prob.append(f"s{n} 숫자 없음 {miss}: {b[:60]}")
            if extra:
                rows.append((lang, f"s{n}", f"⚠️ 번역에만 있는 숫자 {extra}", b[:60]))
                warns += 1
            cps = visible_len(b) / ko_seconds(a)
            if cps > MAX_CPS.get(lang, 21):
                rows.append((lang, f"s{n}", f"⚠️ 빠름 {cps:.0f}자/초 (한국어 약 {ko_seconds(a):.1f}초)", b[:60]))
                warns += 1
        for x in prob:
            rows.append((lang, "", f"❌ {x}", ""))
        errors += len(prob)
        if not prob:
            rows.append((lang, f"{n}문장", "✅", ""))
    lg("SUBS", video=vid, langs=len(langs or LANGS), errors=errors, warnings=warns)
    return rows, errors, warns


def cmd_check(topic, vids, langs):
    vids = vids or all_videos(topic)
    total = 0
    for vid in vids:
        rows, err, warn = check_video(topic, vid, langs)
        total += err
        d = subs_dir(topic, vid)
        if d.exists():
            md = [f"# {vid} 자막 대본 검사 (`tools/subs_tool.py` v1.0)", "",
                  f"- {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M')} UTC · 한국어 대본 `{ko_script(topic, vid).name}` · 언어 {len(langs or LANGS)}개 · 문제 {err} · 경고 {warn}",
                  "- 번역 줄 = 한국어 문장과 1:1 · 한국어 문장의 숫자가 번역에 모두 있어야 통과 (월은 달 이름도) · 속도는 한국어 예상 길이로 잰 경고만.", "",
                  "| 언어 | 문장 | 결과 | 번역 앞부분 |", "|---|---|---|---|"]
            md += [f"| {a} | {b} | {c} | {e.replace('|', '¦')} |" for a, b, c, e in rows]
            (d / "checklist.md").write_text("\n".join(md) + "\n", "utf-8")
        for a, b, c, e in rows:
            if not c.startswith("✅"):
                print(f"  {vid} {a} {b} {c} {e}")
        print(f"[SUBS] {vid} errors={err} warnings={warn}")
    return 1 if total else 0


# ----------------------------------------------------------------------------- build
def ep_data(vid):
    html = (ROOT / "video" / "episodes" / vid / "index.html").read_text("utf-8")
    m = re.search(r"/\*EP-DATA:BEGIN\*/window\.EP=(.*?);/\*EP-DATA:END\*/", html, re.S)
    if not m:
        raise SystemExit(f"[SUBS] ❌ 장면 파일에 EP 자료 없음 → node video/render/render.mjs sync <주제> {vid}")
    return json.loads(m.group(1))


JA_PUNCT = set("、。！？」』）・… ")                                             # v1.1.0 일본어: 이 글자 뒤가 가장 좋은 줄 끝
JA_PARTICLE = set("をはがでにとのもやへか")                                      # v1.1.0 조사 뒤 (다음 글자가 히라가나가 아닐 때)
MIN_PART = 0.25                                                                 # v1.1.0 자막 덩어리 하나가 문장 글자의 이 비율보다 짧으면 그 자리에서 안 나눔


def _cls(c):
    o = ord(c)
    if c in JA_PUNCT:
        return "p"
    if 0x3040 <= o <= 0x309F:
        return "h"                                                              # 히라가나
    if 0x30A0 <= o <= 0x30FF:
        return "k"                                                              # 가타카나 (ー 포함)
    if 0x4E00 <= o <= 0x9FFF or c == "々":
        return "K"                                                              # 한자
    if c.isascii() and (c.isalnum() or c in ",.%$×"):
        return "a"                                                              # 영문·숫자 낱말 (Python·ETF·1,700·25.3%)
    return "o"


def ja_score(prev, nxt):
    """일본어 prev|nxt 사이에서 줄을 끊기 좋은 정도 (클수록 좋음). 낱말 안(영문·숫자·가타카나·한자 이어짐)은 0."""
    cp, cn = _cls(prev), _cls(nxt)
    if cp == "p":
        return 3
    if cp == cn and cp in "akK" or {cp, cn} == {"a", "k"}:
        return 0
    if prev in JA_PARTICLE and cn != "h":
        return 2.5
    if cp == "K" and cn == "h":
        return 0.5                                                              # 한자 + 오쿠리가나 (書|いた)
    if cp == "h" and cn in "Kka":
        return 2
    return 1


def ja_best(text, lo, hi, target):
    """첫 줄 길이 j (lo ≤ j ≤ hi) 중 끊기 좋은 곳 — 점수가 높고, 같으면 target 에 가까운 곳. 없으면 None."""
    js = [j for j in range(max(lo, 1), min(hi, len(text) - 1) + 1)]
    if not js:
        return None
    return max(js, key=lambda j: (ja_score(text[j - 1], text[j]), -abs(j - target)))


def wrap(text, lang):
    """→ 줄 목록 (한 줄 LINE_CHARS). v1.1.0: 2줄에 들어가면 두 줄 길이를 고르게 — 영어 등은 낱말 사이,
    일본어는 구두점·조사 뒤 (영문·숫자·가타카나·한자 낱말 안은 피함). 2줄을 넘으면 앞에서부터 채움."""
    lim = LINE_CHARS.get(lang, 42)
    if len(text) <= lim:
        return [text]
    if lang in CJK:
        if len(text) <= 2 * lim:
            k = ja_best(text, len(text) - lim, lim, len(text) / 2)
            if k:
                return [text[:k], text[k:]]
        lines, rest = [], text
        while len(rest) > lim:
            k = ja_best(rest, lim - 8, lim, lim) or lim
            lines.append(rest[:k])
            rest = rest[k:]
        return lines + ([rest] if rest else [])
    words = text.split()
    if len(text) <= 2 * lim + 1:
        best = None
        for i in range(1, len(words)):
            x, y = " ".join(words[:i]), " ".join(words[i:])
            if len(x) <= lim and len(y) <= lim and (best is None or max(len(x), len(y)) < best[0]):
                best = (max(len(x), len(y)), x, y)
        if best:
            return [best[1], best[2]]
    lines, cur = [], ""
    for w in words:
        if cur and len(cur) + 1 + len(w) > lim:
            lines.append(cur)
            cur = w
        else:
            cur = f"{cur} {w}" if cur else w
    return lines + ([cur] if cur else [])


def cue_parts(text, lang):
    """문장 → 자막 덩어리 (덩어리마다 2줄까지). 넘으면 쉼표·쌍점·줄표·'、' 에서 나눔 (가운데에 가까운 곳 —
    v1.1.0 덩어리가 문장의 25% 보다 짧아지는 곳은 빼고, 없으면 가운데 낱말 사이·일본어는 가운데 조사 뒤)."""
    if len(wrap(text, lang)) <= 2:
        return [text]
    n = len(text)
    cut = [m.end() for m in re.finditer(r"[,;:、，]\s|\s[—–-]\s|、", text)]
    cut = [c for c in cut if min(c, n - c) >= MIN_PART * n]
    if not cut:
        if lang in CJK:
            k = ja_best(text, int(n * MIN_PART), n - int(n * MIN_PART), n / 2) or n // 2
        else:
            sp = [m.start() for m in re.finditer(r"\s", text)]
            k = min(sp, key=lambda c: abs(c - n / 2)) if sp else n // 2
        a, b = text[:k].strip(), text[k:].strip()
        if not a or not b:
            return [text]
        return cue_parts(a, lang) + cue_parts(b, lang)
    k = min(cut, key=lambda c: abs(c - n / 2))
    return cue_parts(text[:k].strip(), lang) + cue_parts(text[k:].strip(), lang)


def ts(t):
    t = max(0.0, t)
    h, r = divmod(int(round(t * 1000)), 3600000)
    m, r = divmod(r, 60000)
    s, ms = divmod(r, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def build(topic, vid, estimated=False, langs=None):
    ep = ep_data(vid)
    if ep.get("estimated") and not estimated:
        raise SystemExit(f"[SUBS] ❌ {vid} 장면 시각이 추정(오디오 전) → 오디오가 오면 render.mjs sync 뒤 다시 · 점검만이면 --estimated")
    sents = ep["sent"]
    out_dir = (ROOT / topic / "out" / vid / "subs") if ep.get("estimated") else subs_dir(topic, vid)
    out_dir.mkdir(parents=True, exist_ok=True)
    made = []
    for lang in langs or LANGS:
        p = subs_dir(topic, vid) / f"{vid}.{lang}.txt"
        if not p.exists():
            lg("SUBS", logging.WARNING, video=vid, lang=lang, status="skip", reason="자막 대본 없음")
            continue
        tr = [b for k, b in structure(p) if k == "s"]
        if len(tr) != len(sents):
            raise SystemExit(f"[SUBS] ❌ {vid}.{lang}: 번역 {len(tr)}문장 ≠ 장면 문장 {len(sents)} → check 먼저")
        cues = []
        for s, text in zip(sents, tr):
            parts = cue_parts(text, lang)
            total = sum(len(x) for x in parts) or 1
            t = s["start"]
            for x in parts:
                d = (s["end"] - s["start"]) * len(x) / total
                cues.append((t, t + d, "\n".join(wrap(x, lang))))
                t += d
        srt = "\n".join(f"{i}\n{ts(a)} --> {ts(b)}\n{x}\n" for i, (a, b, x) in enumerate(cues, 1))
        f = out_dir / f"{vid}.{lang}.srt"
        f.write_text(srt, "utf-8")
        made.append(f)
        lg("SUBS", video=vid, lang=lang, cues=len(cues), sentences=len(sents), estimated=bool(ep.get("estimated")), file=str(f.relative_to(ROOT)))
    return made


def cmd_status(topic):
    for vid in all_videos(topic):
        d = subs_dir(topic, vid)
        txt = [l for l in LANGS if (d / f"{vid}.{l}.txt").exists()]
        srt = [l for l in LANGS if (d / f"{vid}.{l}.srt").exists()]
        print(f"{vid}: 대본 {len(txt)}/{len(LANGS)} {','.join(txt) or '-'} · SRT {len(srt)}")


def main():
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["check", "build", "status"])
    ap.add_argument("topic")
    ap.add_argument("videos", nargs="*")
    ap.add_argument("--lang", action="append", help="언어 하나만 (여러 번 가능)")
    ap.add_argument("--estimated", action="store_true", help="build: 추정 시각으로 (점검용 — <주제>/out 에)")
    a = ap.parse_args()
    if a.cmd == "check":
        sys.exit(cmd_check(a.topic, a.videos, a.lang))
    if a.cmd == "status":
        cmd_status(a.topic)
        return
    for vid in a.videos or all_videos(a.topic):
        build(a.topic, vid, a.estimated, a.lang)


if __name__ == "__main__":
    main()
