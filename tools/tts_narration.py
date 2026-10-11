#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.2.1 — 2026-10-11 — Kaggle 사본에서 실행 권한(파일 모드)만 바뀐 파일 때문에 git pull 이 멈추던 문제: git 실행에 core.fileMode=false,
#          올리기 전에 사본의 다른 변경 파일을 알림(커밋하지 않음). Kaggle 셀은 git pull 대신 main 과 똑같이 맞춤(fetch + reset --hard)
# (v1.2: 2026-10-11 — 사용자 지시: 오디오는 고르지 않고 하나로(말투 시험 sample·preset·--story-style 삭제, 역할만 이은 트랙 삭제 →
#          영상마다 narration.mp3 하나), 결과 파일을 GitHub에 올리기(--push: 영상이 끝날 때마다 대본 폴더 <주제>/source/<영상ID>/ 에
#          narration.mp3·tts_narration.json·tts_report.md 를 main에 커밋·푸시, 토큰은 Kaggle Secrets GITHUB_TOKEN 에서만 읽음)
#          (v1.1: 사연자·진행자 역할별 목소리 설정 voices/*.json, all·pack·check / v1.0: 최초 작성 — Qwen3-TTS 로 대본 TXT → narration.mp3)
r"""
대본 TXT로 내레이션 오디오를 만듭니다. Kaggle 노트북(GPU T4)에서 돌리는 것을 기준으로 썼습니다. 사용법: guides/tts_guide.md

  python tools/tts_narration.py all --push                             # 저장소의 대본을 모두 읽어 오디오가 없는 영상 전부 → 영상마다 GitHub에 올림
  python tools/tts_narration.py all --dry-run                          # 무엇을 만들지 목록만 (모델 안 불러옴)
  python tools/tts_narration.py all --push --gpu 0 --split 0/2         # GPU 2개: 영상을 나눠 0/2 와 1/2 를 동시에 (올리기는 차례로)
  python tools/tts_narration.py build stock panicsell-2026-10 --push   # 영상 하나
  python tools/tts_narration.py build stock panicsell-2026-10 --redo 12,15 --push   # 12·15번 문장만 새 시드로 다시
  python tools/tts_narration.py push                                   # 만들어 두고 못 올린 결과를 GitHub에 올리기
  python tools/tts_narration.py check stock panicsell-2026-10          # 저장소의 narration 이 지금 대본으로 만든 것인지
  python tools/tts_narration.py pack                                   # (올리기가 안 될 때만) 결과를 저장소 경로 그대로 zip 하나로
  (어느 명령이든 --fake: 모델 없이 가짜 소리로 전 과정 확인 — 가짜 소리는 github.com 에 올리지 않는다)

모델: Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice — 한국어 화자 Sohee, 말투를 글로 지시(instruct). 라이선스 Apache-2.0(상업 이용 가능).
  ※ 0.6B 모델은 말투 지시를 무시한다(qwen-tts 패키지가 instruct=None 으로 바꿈). 말투를 쓰려면 1.7B.

역할 (사용자 지시 2026-10-10) — 말투는 설정 파일 하나로 정해져 있고 고르지 않는다 (사용자 지시 2026-10-11)
  - 사연자(storyteller): 파트 라벨에 '사연'이 든 문장 — 1인칭 고백. 설정 voices/storyteller.json
  - 진행자(host): 나머지 모든 파트(진행자·문제 분석·올바른 방법·마무리). 설정 voices/host.json
  - 설정은 voices/<역할>.json → <주제>/voices/<역할>.json → <주제>/source/<영상ID>/voices/<역할>.json 순서로 덮어쓴다.

결과 (영상마다 오디오 하나)
  저장소 <주제>/source/<영상ID>/narration.mp3      ← 영상에 쓰는 오디오 (--push 가 대본 폴더에 각각 올린다)
  저장소 <주제>/source/<영상ID>/tts_narration.json ← 문장별 역할·시작·끝, 대본 해시(check 용), 목소리 설정
  저장소 <주제>/source/<영상ID>/tts_report.md      ← 문장별 길이·속도·귀로 확인할 문장
  작업 폴더 OUT(= /kaggle/working/tts_out, Kaggle 밖에서는 output/tts): OUT/upload/… (위 세 파일, 올리기 전 원본),
           OUT/<영상ID>/storyteller/S###.wav · OUT/<영상ID>/host/S###.wav (역할별 문장 파일), OUT/<영상ID>/cache/

GitHub 올리기 (--push)
  - 토큰: 환경 변수 GITHUB_TOKEN, 없으면 Kaggle Secrets 의 GITHUB_TOKEN. 값은 로그·파일·명령줄·원격 주소에 남기지 않는다(GIT_ASKPASS).
  - 시작할 때 토큰으로 push 권한을 먼저 확인한다(git push --dry-run, 실제로 올리지 않음). 안 되면 만들기 전에 멈춘다.
  - 영상 하나가 끝날 때마다 그 영상의 세 파일만 git add → 커밋 → pull --rebase → push (최대 4번 다시). 다른 파일은 올리지 않는다.
  - GPU 2개(--split)로 동시에 돌려도 git 작업은 잠금 파일로 하나씩 한다.

규칙 (guides/tts_guide.md 5번, guides/video_guide.md 2번 "내레이션")
  - 문장 = tools/srt_tool.py parse_txt 와 같은 순서(파트 라벨·[장면]·카드 문구 제외). 오디오 문장 = 대본 문장.
  - 문장 사이 쉼 = 역할 설정의 gap(기본 0.45초, 디지털 무음), 파트가 바뀌면 1.0초. align-audio(무음 −35dB·0.12초 이상)가 이 쉼으로 문장 경계를 찾는다.
  - 고지 카드 자리([장면] 바로 앞 문장 뒤): srt_tool.parse_cards 의 길이(문구 글자 수 ÷ 7 + 1초, 4~8초). 최소 3.5초 규칙보다 길다.
  - 문장마다 검사: 말 속도 2.5~8음절/초, 문장 안 무음 1.8초 이하, NaN·빈 소리 없음. 벗어나면 시드를 바꿔 다시(최대 3번).
  - 볼륨: 영상 전체에 이득 하나만 곱한다(말소리 RMS −18dBFS, 최고점 −1dBFS 이하). 문장·역할마다 따로 바꾸지 않는다.
  - 문장 파일은 OUT/<영상ID>/cache/ 에 남는다(<키>.wav + <키>.json). 글·말투·화자·설정이 같으면 다시 만들지 않는다.
※ 연구·교육용 도구다. 영상 내용은 투자 권유가 아니다(주식 영상 고지 규칙은 stock/guides 를 따른다).
"""
import argparse
import hashlib
import importlib.util
import json
import logging
import math
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import wave
import zipfile
from datetime import datetime
from pathlib import Path

import numpy as np

TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent
sys.path.insert(0, str(TOOLS))
import srt_tool  # noqa: E402  (문장·카드 판정을 자막 도구와 똑같이 쓰기 위해)

VERSION = "v1.2.1"
CACHE_VERSION = 1            # 생성 방식이 바뀌면 올린다 → 문장 파일을 모두 다시 만든다 (v1.1은 v1.0 캐시와 같은 키)
DEFAULT_MODEL = "Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice"
FRAME_HZ = 12.5              # Qwen3-TTS-Tokenizer-12Hz: 24000Hz ÷ 1920 = 초당 12.5 프레임 (max_new_tokens 계산)
CARD_GAP_MIN = srt_tool.CARD_GAP_MIN   # 3.5초 — align-audio.mjs 와 같은 값
MIN_RATE, MAX_RATE = 2.5, 8.0  # 문장 말 속도(읽는 음절/초) 허용 범위. 성공 영상 4.2~5.5 (stock/guides/data_insights.md 2번)
SHORT_SYL = 6                # 이보다 짧은 문장("감사합니다.")은 속도 대신 길이 4초 이하만 본다
MAX_INNER_SIL = 1.8          # 문장 안 무음이 이보다 길면 이상(말을 멈추고 딴소리·잡음일 수 있음)
SIL_DB = -45.0               # 10ms 구간 RMS가 이 값 이하면 무음 (앞뒤 자르기·문장 안 무음)
TRIM_PAD = 0.06              # 앞뒤를 자를 때 남기는 여유(초) — 숨소리·첫소리가 잘리지 않게
TARGET_RMS_DB = -18.0        # 말소리 구간 RMS 목표
PEAK_DB = -1.0               # 최고점 한도
RATE_REF = 4.8               # 검사를 모두 통과한 시도가 없을 때 이 속도에 가까운 것을 고른다
MIN_GAP = 0.2                # 역할 설정 gap 하한 — align-audio 가 문장 경계로 보는 무음(0.12초)보다 넉넉하게

VOICES_DIR = ROOT / "voices"           # 역할별 목소리 설정 (파일 이름 = 역할 = 결과 폴더 이름)
VOICE_KEYS = {"role", "name", "parts", "speaker", "instruct", "part_instruct", "seed", "gap", "generation"}
GEN_KEYS = {"temperature", "top_p", "top_k", "repetition_penalty"}
STORY_ROLE = "storyteller"             # 사연자 역할 (영상 코드 plan.ts 의 STORY_LAST 와 비교)
AUDIO_EXTS = ("mp3", "wav", "m4a")     # align-audio.mjs·publish.sh 가 찾는 narration 확장자
META_NAME = "tts_narration.json"       # narration 옆에 두는 메타 (check 가 읽음). 'narration.*' 와 겹치지 않는 이름
ZIP_NAME = "narration_upload.zip"     # pack: 올리기가 안 될 때만 쓰는 zip
REPORT_NAME = "tts_report.md"          # narration 옆에 두는 보고 (문장별 길이·속도·귀로 확인할 문장)
REPO_FILES = ("narration.mp3", META_NAME, REPORT_NAME)   # --push 가 대본 폴더에 올리는 파일 (이것만)
TOKEN_ENV = "GITHUB_TOKEN"             # 환경 변수·Kaggle Secrets 이름. 값은 어디에도 출력하지 않는다
GIT_NAME, GIT_EMAIL = "tts_narration (Kaggle)", "tts-narration@users.noreply.github.com"
PUSH_TRIES = 4

LOG = logging.getLogger("tts")


# ----------------------------------------------------------------------------- 로그
def _fmt(v):
    if isinstance(v, float):
        return f"{v:.3f}".rstrip("0").rstrip(".") if math.isfinite(v) else str(v)
    s = str(v)
    return f'"{s}"' if (" " in s or not s) else s


def log(stage, level=logging.INFO, **kv):
    """[STAGE] [TIMESTAMP] key=value ... (가이드의 공통 로그 형식)"""
    LOG.log(level, "[%s] [%s] %s", stage, datetime.now().isoformat(timespec="seconds"),
            " ".join(f"{k}={_fmt(v)}" for k, v in kv.items()))


def die(stage, error, hint, **kv):
    log(stage, logging.ERROR, error=error, hint=hint, **kv)
    raise SystemExit(1)


def rel(p):
    try:
        return str(Path(p).resolve().relative_to(ROOT))
    except ValueError:
        return str(p)


def ranges(nums):
    """[1,2,3,7,8] → '1-3,7-8' (로그·보고서에서 역할별 문장 범위)"""
    out, start, prev = [], None, None
    for n in nums:
        if start is None:
            start = prev = n
        elif n == prev + 1:
            prev = n
        else:
            out.append(f"{start}-{prev}" if prev > start else str(start))
            start = prev = n
    if start is not None:
        out.append(f"{start}-{prev}" if prev > start else str(start))
    return ",".join(out)


def sha(obj):
    return hashlib.sha1(json.dumps(obj, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()[:16]


# ----------------------------------------------------------------------------- 대본
def read_script(txt_path):
    """(문장, 파트 라벨) 목록과 카드 목록. 판정은 srt_tool.parse_txt / parse_cards 와 같다(같은 is_label)."""
    rows, part, in_card = [], "", False
    for raw in Path(txt_path).read_text("utf-8-sig").splitlines():
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
            rows.append((line, part))
    if [r[0] for r in rows] != srt_tool.parse_txt(txt_path):   # 같은 규칙인지 스스로 확인
        die("INPUT", "문장 판정이 srt_tool.parse_txt 와 다름", "srt_tool.py 가 바뀌었는지 확인", txt=txt_path)
    return rows, srt_tool.parse_cards(txt_path)


def script_sha(rows, cards):
    """대본 해시 — 문장·파트·고지 카드 쉼만 본다(빈 줄·띄어쓰기 바꿈은 무시). check·all 이 오디오가 지금 대본으로 만든 것인지 볼 때 쓴다."""
    return sha({"rows": [list(r) for r in rows], "cards": [[c["after"], c["seconds"]] for c in cards]})


def load_lexicon(paths):
    """읽는 소리 사전 TSV: '원문<TAB>읽는 소리' (# 주석). TTS에 넣는 글에만 쓰고 대본·자막은 그대로 둔다."""
    pairs = []
    for p in paths:
        if not p or not Path(p).is_file():
            continue
        n0 = len(pairs)
        for ln in Path(p).read_text("utf-8-sig").splitlines():
            if ln.strip() and not ln.lstrip().startswith("#") and "\t" in ln:
                src, dst = ln.split("\t", 1)
                pairs.append((src.strip(), dst.strip()))
        log("INPUT", lexicon=rel(p), entries=len(pairs) - n0)
    return sorted(pairs, key=lambda x: -len(x[0]))   # 긴 것부터 바꿔 겹침 방지


def tts_text(text, lexicon):
    """TTS에 넣는 글. 부호 붙은 금액은 뜻이 바뀌지 않게 소리로 바꾼다(srt_tool.spoken 과 같은 규칙): -800만 → 마이너스 800만."""
    s = text
    for src, dst in lexicon:
        s = s.replace(src, dst)
    s = re.sub(r"(?<![\w.])-(?=\d)", "마이너스 ", s)
    s = re.sub(r"(?<![\w.])\+(?=\d)", "플러스 ", s)
    return s


# ----------------------------------------------------------------------------- 목소리 설정 (역할)
def load_voices(topic=None, vid=None, args=None):
    """역할별 목소리 설정 → {역할: 설정}. voices/<역할>.json 을 주제·영상 폴더의 같은 이름 파일이 차례로 덮어쓴다.
    part_instruct·generation 은 항목 단위로 합친다. '_' 로 시작하는 항목(설명)은 무시한다."""
    base = sorted(VOICES_DIR.glob("*.json"))
    if not base:
        die("VOICE", "목소리 설정 파일 없음", "저장소를 git pull 했는지 (voices/storyteller.json·host.json)", dir=rel(VOICES_DIR))
    voices = {}
    for p in base:
        role = p.stem
        cfg, files = {}, []
        layers = [p]
        if topic:
            layers.append(ROOT / topic / "voices" / p.name)
            if vid:
                layers.append(ROOT / topic / "source" / vid / "voices" / p.name)
        for q in layers:
            if not q.is_file():
                continue
            try:
                d = json.loads(q.read_text("utf-8-sig"))
            except json.JSONDecodeError as e:
                die("VOICE", f"설정 파일 JSON 오류: {e}", "쉼표·따옴표·괄호 확인 (마지막 항목 뒤에는 쉼표 없음)", file=rel(q))
            unknown = sorted(k for k in d if k not in VOICE_KEYS and not k.startswith("_"))
            if unknown:
                log("VOICE", logging.WARNING, file=rel(q), unknown=",".join(unknown), note="모르는 항목은 무시")
            for k, v in d.items():
                if k.startswith("_") or k not in VOICE_KEYS:
                    continue
                cfg[k] = {**cfg.get(k, {}), **v} if k in ("part_instruct", "generation") and isinstance(v, dict) else v
            files.append(rel(q))
        cfg = {"name": role, "parts": ["*"], "speaker": "Sohee", "instruct": "", "part_instruct": {},
               "seed": 1234, "gap": 0.45, "generation": {}, **cfg, "role": role, "files": files}
        voices[role] = cfg
    # 명령줄 덮어쓰기 (설정 파일을 고치지 않고 시험할 때) — 바꾼 것은 로그에 남긴다
    if args is not None:
        for role, v in voices.items():
            for key, val in (("speaker", getattr(args, "speaker", None)), ("seed", getattr(args, "seed", None)),
                             ("gap", getattr(args, "gap", None))):
                if val is not None and v[key] != val:
                    log("VOICE", role=role, key=key, file_value=v[key], cli_value=val, note="명령줄 값이 설정 파일보다 우선")
                    v[key] = val
    for role, v in voices.items():
        v["style_name"] = v["name"]
        if not str(v["instruct"]).strip():
            die("VOICE", "말투 지시(instruct)가 비어 있음", "voices/<역할>.json 의 instruct 채우기", role=role)
        if not isinstance(v["parts"], list) or not v["parts"]:
            die("VOICE", "parts 는 파트 라벨 낱말 목록이어야 함 (예: [\"사연\"] 또는 [\"*\"])", "voices/<역할>.json 확인", role=role)
        bad = sorted(set(v["generation"]) - GEN_KEYS)
        if bad:
            die("VOICE", f"generation 에 모르는 항목: {','.join(bad)}", f"쓸 수 있는 항목: {','.join(sorted(GEN_KEYS))}", role=role)
        if not isinstance(v["gap"], (int, float)) or v["gap"] < MIN_GAP:
            die("VOICE", f"gap {v['gap']} < {MIN_GAP}초", "문장 사이 쉼이 짧으면 align-audio 가 문장 경계를 못 찾음", role=role)
        if not isinstance(v["seed"], int):
            die("VOICE", f"seed 는 정수여야 함: {v['seed']}", "예: 1234", role=role)
    # 낱말로 정한 역할(사연자)을 먼저, 나머지("*") 역할(진행자)을 뒤에 — 로그·보고서 순서
    voices = dict(sorted(voices.items(), key=lambda kv: ("*" in kv[1]["parts"], kv[0])))
    wild = [r for r, v in voices.items() if "*" in v["parts"]]
    if len(wild) != 1:
        die("VOICE", f"나머지 파트(\"*\")를 맡는 역할이 {len(wild)}개", "한 역할만 parts 에 \"*\" (기본: host)", roles=",".join(wild) or "-")
    return voices


def role_of(part, voices):
    """파트 라벨 → 역할. 낱말이 맞는 역할이 먼저, 없으면 "*" 역할(진행자)."""
    for role, v in voices.items():
        if any(k != "*" and k in part for k in v["parts"]):
            return role
    return next(r for r, v in voices.items() if "*" in v["parts"])


def instruct_for(voice, part):
    """역할 안에서 파트별 말투(part_instruct)가 있으면 그것, 없으면 역할 기본 말투. → (지시, 말투 이름)"""
    for k, ins in voice["part_instruct"].items():
        if k in part:
            return ins, f"{voice['name']} · {k}"
    return voice["instruct"], voice["style_name"]


def spec_of(voice, instruct):
    """문장 하나를 만들 때 쓰는 목소리 값. 캐시 키·메타에 그대로 들어간다."""
    return {"speaker": voice["speaker"], "instruct": instruct, "gen": dict(voice["generation"]),
            "seed": voice["seed"], "gap": float(voice["gap"])}


def plan_items(vid, rows, voices, lex):
    """문장마다 역할·말투를 정하고 역할별 범위를 로그로 남긴다."""
    items = []
    for n, (text, part) in enumerate(rows, 1):
        role = role_of(part, voices)
        instruct, style = instruct_for(voices[role], part)
        items.append({"n": n, "text": text, "part": part, "role": role, "style": style,
                      "spec": spec_of(voices[role], instruct), "tts": tts_text(text, lex), "syl": srt_tool.syllables(text)})
    for role, v in voices.items():
        mine = [it for it in items if it["role"] == role]
        log("ROLE", video=vid, role=role, name=v["name"], sentences=len(mine), range=ranges([it["n"] for it in mine]) or "-",
            syllables=sum(it["syl"] for it in mine), speaker=v["speaker"], seed=v["seed"], gap_s=v["gap"],
            parts=" / ".join(dict.fromkeys(it["part"] for it in mine)) or "-", files=",".join(v["files"]))
    for style, ins in dict.fromkeys((it["style"], it["spec"]["instruct"]) for it in items):
        log("STYLE", video=vid, style=style, instruct=ins)
    story = [it["n"] for it in items if it["role"] == STORY_ROLE]
    plan = ROOT / "video" / "src" / "episodes" / vid / "plan.ts"
    mm = re.search(r"STORY_LAST\s*=\s*(\d+)", plan.read_text("utf-8")) if plan.is_file() else None
    if mm and story:   # 영상 코드의 사연 끝 번호와 대본의 사연자 끝 번호가 같은지 (다르면 자막·장면이 어긋남)
        ok = int(mm.group(1)) == story[-1]
        log("ROLE", level=logging.INFO if ok else logging.WARNING, video=vid, plan_story_last=int(mm.group(1)),
            script_story_last=story[-1], ok=ok, note="-" if ok else "영상 코드 plan.ts 의 STORY_LAST 와 다름 — 대본·영상 코드 확인")
    return items


# ----------------------------------------------------------------------------- 소리 계산 (numpy만)
def silence(sec, sr):
    return np.zeros(int(round(sec * sr)), dtype=np.float32)


def frame_db(x, sr, win=0.01):
    n = max(1, int(sr * win))
    m = len(x) // n
    if m == 0:
        return np.array([-120.0])
    fr = x[: m * n].reshape(m, n).astype(np.float64)
    return 10 * np.log10(np.mean(fr * fr, axis=1) + 1e-12)


def trim(x, sr):
    """앞뒤 무음만 자른다(TRIM_PAD 여유). 문장 사이 쉼을 이 도구가 정한 길이로 맞추기 위해서다."""
    voiced = np.where(frame_db(x, sr) > SIL_DB)[0]
    if voiced.size == 0:
        return x[:0]
    n, pad = int(sr * 0.01), int(sr * TRIM_PAD)
    return x[max(0, voiced[0] * n - pad): min(len(x), (voiced[-1] + 1) * n + pad)]


def longest_silence(x, sr):
    """가장 긴 무음 구간(초). 10ms 구간의 무음 여부가 바뀌는 곳으로 구간 길이를 잰다(반복문 없음)."""
    q = np.concatenate([[0], (frame_db(x, sr) <= SIL_DB).astype(np.int8), [0]])
    d = np.diff(q)
    starts, ends = np.where(d == 1)[0], np.where(d == -1)[0]
    return float((ends - starts).max()) * 0.01 if starts.size else 0.0


def voiced_rms_db(x, sr):
    db = frame_db(x, sr)
    v = db[db > SIL_DB]
    return float(10 * np.log10(np.mean(10 ** (v / 10)))) if v.size else -120.0


def check(x, sr, syl, nonfinite):
    """문장 하나 검사 → (통과 여부, 문제 목록, 경고 목록, 수치)."""
    issues, warns = [], []
    if nonfinite:
        issues.append("NaN/inf")
    dur = len(x) / sr if sr else 0.0
    if dur <= 0.05:
        return False, issues + ["빈 소리"], warns, {"dur": dur, "rate": 0.0, "inner_sil": 0.0, "rms_db": -120.0, "peak": 0.0}
    rate = syl / dur
    if syl >= SHORT_SYL:
        if not MIN_RATE <= rate <= MAX_RATE:
            issues.append(f"말 속도 {rate:.1f}음절/초(허용 {MIN_RATE}~{MAX_RATE})")
    elif dur > 4.0:
        issues.append(f"짧은 문장인데 {dur:.1f}초")
    sil = longest_silence(x, sr)
    if sil > MAX_INNER_SIL:
        issues.append(f"문장 안 무음 {sil:.1f}초")
    peak = float(np.max(np.abs(x)))
    if np.mean(np.abs(x) >= 0.999) > 0.001:
        warns.append("소리 깨짐(클리핑) 의심")
    return not issues, issues, warns, {"dur": dur, "rate": rate, "inner_sil": sil, "rms_db": voiced_rms_db(x, sr), "peak": peak}


def write_wav(path, x, sr):
    y = np.clip(x, -1.0, 1.0)
    pcm = (y * 32767.0).round().astype("<i2")
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes(pcm.tobytes())


def read_wav(path):
    with wave.open(str(path), "rb") as w:
        sr, data = w.getframerate(), w.readframes(w.getnframes())
    return np.frombuffer(data, dtype="<i2").astype(np.float32) / 32767.0, sr


# ----------------------------------------------------------------------------- 엔진
class QwenEngine:
    """Qwen3-TTS CustomVoice. 모델 하나를 영상·역할이 함께 쓰고, 문장마다 화자·말투 지시를 넘긴다."""

    def __init__(self, args, speakers):
        try:
            import torch
            from qwen_tts import Qwen3TTSModel
        except ImportError as e:
            die("MODEL", f"패키지 없음: {e}", "Kaggle 셀에서 먼저: !pip install -q -U qwen-tts")
        self.torch = torch
        self.language, self.model_id = args.language, args.model
        device = args.device or (f"cuda:{args.gpu}" if torch.cuda.is_available() else "cpu")
        if device.startswith("cuda") and not torch.cuda.is_available():
            die("MODEL", "GPU가 없음", "Kaggle 오른쪽 설정 → Accelerator → 'GPU T4 x2', Internet 켜기")
        cap = torch.cuda.get_device_capability(device) if device.startswith("cuda") else (0, 0)
        gpu = torch.cuda.get_device_name(device) if device.startswith("cuda") else "CPU"
        if device == "cpu":
            log("MODEL", logging.WARNING, device="cpu", note="CPU는 문장 하나에 몇 분 걸림 — GPU 권장")
        elif cap < (7, 0):
            log("MODEL", logging.WARNING, gpu=gpu, capability=f"{cap[0]}.{cap[1]}",
                note="P100 등 옛 GPU는 최신 PyTorch가 지원하지 않을 수 있음 → 'GPU T4 x2' 권장")
        # T4(7.5)는 bfloat16 연산 장치가 없고 float16은 값이 넘쳐 NaN이 날 수 있다 → 기본 float32 (1.7B ≈ 7GB, T4 16GB에 들어감)
        dtype_name = ("bfloat16" if cap >= (8, 0) else "float32") if args.dtype == "auto" else args.dtype
        dtype = getattr(torch, dtype_name)
        attn = args.attn
        if attn == "auto":
            attn = ("flash_attention_2" if cap >= (8, 0) and dtype_name != "float32" and importlib.util.find_spec("flash_attn")
                    else "sdpa")
        log("MODEL", model=self.model_id, device=device, gpu=gpu, dtype=dtype_name, attn=attn)
        t0 = time.time()
        try:
            self.model = Qwen3TTSModel.from_pretrained(self.model_id, device_map=device, dtype=dtype, attn_implementation=attn)
        except Exception as e:  # 다운로드·메모리·버전 문제를 한 곳에서 안내
            die("MODEL", f"모델을 불러오지 못함: {type(e).__name__}: {e}",
                "Kaggle 설정에서 Internet 켜기(휴대폰 인증 필요) / GPU 메모리 부족이면 런타임 재시작 / --attn sdpa 로 다시")
        self.dtype_name, self.device = dtype_name, device
        mem = torch.cuda.memory_allocated(device) / 1e9 if device.startswith("cuda") else 0.0
        log("MODEL", loaded_s=time.time() - t0, gpu_mem_gb=mem, gen_defaults=json.dumps(self.model.generate_defaults, ensure_ascii=False))
        spk = self.model.get_supported_speakers() or []
        langs = self.model.get_supported_languages() or []
        log("MODEL", speakers=",".join(spk), languages=",".join(langs))
        for s in sorted(speakers):
            if spk and s.lower() not in [x.lower() for x in spk]:
                die("MODEL", f"없는 화자: {s}", f"voices/<역할>.json 의 speaker 를 이 중에서: {', '.join(spk)}")
        if langs and self.language.lower() not in [x.lower() for x in langs]:
            die("MODEL", f"없는 언어: {self.language}", f"--language 를 이 중에서: {', '.join(langs)}")
        if "0.6B" in self.model_id:
            log("MODEL", logging.WARNING, note="0.6B 모델은 말투 지시(instruct)를 무시함 — 감정 표현은 1.7B")
        self.gen = {k: v for k, v in {"temperature": args.temperature, "top_p": args.top_p, "top_k": args.top_k,
                                      "repetition_penalty": args.repetition_penalty}.items() if v is not None}

    def synth(self, text, spec, seed, max_new_tokens):
        """→ (소리 float32, 표본율) 또는 생성 오류면 None."""
        torch = self.torch
        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)
        try:
            wavs, sr = self.model.generate_custom_voice(
                text=text, speaker=spec["speaker"], language=self.language, instruct=spec["instruct"] or None,
                max_new_tokens=max_new_tokens, **{**self.gen, **spec["gen"]})
        except torch.cuda.OutOfMemoryError as e:
            torch.cuda.empty_cache()
            log("TTS", logging.ERROR, error=f"GPU 메모리 부족: {e}", hint="런타임 재시작 후 다시 (만든 문장은 cache에 남아 있음)")
            raise
        except RuntimeError as e:   # 예: float16 넘침 → 'probability tensor contains either inf, nan'
            log("TTS", logging.WARNING, error=f"{type(e).__name__}: {str(e)[:200]}",
                hint="--dtype float16 을 썼다면 float32 로" if "nan" in str(e).lower() or "inf" in str(e).lower() else "")
            return None
        return np.asarray(wavs[0], dtype=np.float32).reshape(-1), int(sr)

    def describe(self, spec):
        # v1.0 과 같은 모양 → 화자 Sohee·생성 설정 기본이면 v1.0 에서 만든 문장 캐시를 그대로 쓴다
        return {"engine": "qwen3-tts", "model": self.model_id, "speaker": spec["speaker"], "language": self.language,
                "dtype": self.dtype_name, "gen": {**self.gen, **spec["gen"]}}


class FakeEngine:
    """테스트용: 모델 없이 문장 길이에 맞는 가짜 소리(읽는 음절 ÷ 4.8초, 쉼표마다 0.25초 쉼, 앞뒤 무음).
    역할을 귀로 구분할 수 있게 말투 지시마다 음 높이를 다르게 한다."""

    def __init__(self, args, speakers=()):
        self.sr = 24000
        log("MODEL", engine="fake", note="가짜 소리 — 역할 나누기·잇기·쉼·내보내기·align-audio 확인용")

    def synth(self, text, spec, seed, max_new_tokens):
        rng = np.random.default_rng(seed)
        hz = 150 + int(hashlib.sha1(spec["instruct"].encode("utf-8")).hexdigest()[:4], 16) % 120
        out = [silence(0.15, self.sr)]
        chunks = [c for c in re.split(r"[,，]", text) if c.strip()]
        for i, ch in enumerate(chunks):
            d = max(0.3, srt_tool.syllables(ch) / 4.8 * rng.uniform(0.9, 1.1))
            t = np.arange(int(d * self.sr)) / self.sr
            out.append((0.2 * np.sin(2 * np.pi * hz * t) * (0.6 + 0.4 * np.sin(2 * np.pi * 4.8 * t))).astype(np.float32))
            if i < len(chunks) - 1:
                out.append(silence(0.25, self.sr))
        out.append(silence(0.3, self.sr))
        return np.concatenate(out), self.sr

    def describe(self, spec):
        return {"engine": "fake", "model": "fake", "speaker": spec["speaker"], "language": "-", "dtype": "-", "gen": {}}


def make_engine(args, speakers):
    return FakeEngine(args, speakers) if args.fake else QwenEngine(args, speakers)


# ----------------------------------------------------------------------------- 문장 하나 만들기 (캐시·검사·다시)
def cache_key(engine, text, spec):
    d = dict(engine.describe(spec), text=text, instruct=spec["instruct"], seed=spec["seed"], cache=CACHE_VERSION)
    return hashlib.sha1(json.dumps(d, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()[:16]


def make_sentence(engine, cache_dir, label, text, spec, syl, args, redo=False, role="-"):
    """캐시에 있으면 그대로, 없으면(또는 redo) 만들고 검사한다. → 메타 dict (wav 경로 포함)."""
    key = cache_key(engine, text, spec)
    wav_p, meta_p = cache_dir / f"{key}.wav", cache_dir / f"{key}.json"
    old = json.loads(meta_p.read_text("utf-8")) if meta_p.is_file() else None
    if old and wav_p.is_file() and not redo:
        log("CACHE", level=logging.DEBUG, item=label, role=role, key=key, dur=old["dur"], ok=old["ok"])
        return dict(old, wav=str(wav_p), cached=True)
    # 시드: 역할 기본 시드 + 글 내용 해시(문장 위치가 바뀌어도 같은 글은 같은 시드) + 시도 번호. redo 는 전에 쓴 시도 다음부터.
    seed0 = spec["seed"] + int(key[:6], 16) % 1_000_000 * 10
    start = (max(old.get("tried", [0])) + 1) if (old and redo) else 1
    max_new = int(FRAME_HZ * max(syl, 4) / 2.0) + 50     # 2음절/초보다 느리면 끊는다(그보다 느리면 어차피 검사 탈락)
    best, tried = None, list(old.get("tried", [])) if (old and redo) else []
    for attempt in range(start, start + args.max_tries):
        seed = seed0 + attempt
        tried.append(attempt)
        t0 = time.time()
        res = engine.synth(text, spec, seed, max_new)
        gen_s = time.time() - t0
        if res is None:
            log("TTS", logging.WARNING, item=label, role=role, attempt=attempt, seed=seed, ok=False, issues="생성 오류")
            continue
        x, sr = res
        nonfinite = not np.isfinite(x).all()
        x = trim(np.nan_to_num(x, nan=0.0, posinf=0.0, neginf=0.0), sr)
        ok, issues, warns, m = check(x, sr, syl, nonfinite)
        log("TTS", level=logging.INFO if ok else logging.WARNING, item=label, role=role, attempt=attempt, seed=seed, syl=syl,
            dur=m["dur"], rate=m["rate"], inner_sil=m["inner_sil"], gen_s=gen_s, rtf=gen_s / max(m["dur"], 1e-6),
            ok=ok, issues=";".join(issues) or "-", warns=";".join(warns) or "-")
        score = (0 if ok else 1, abs(math.log(max(m["rate"], 1e-3) / RATE_REF)) + max(0.0, m["inner_sil"] - MAX_INNER_SIL))
        if best is None or score < best[0]:
            best = (score, x, sr, attempt, seed, ok, issues, warns, m, gen_s)
        if ok:
            break
    if best is None:
        die("TTS", f"{label}: {args.max_tries}번 모두 생성 오류", "로그의 오류를 보고 --dtype float32 / 런타임 재시작 후 다시", text=text)
    _, x, sr, attempt, seed, ok, issues, warns, m, gen_s = best
    write_wav(wav_p, x, sr)
    meta = {"key": key, "text": text, "instruct": spec["instruct"], "syl": syl, "sr": sr, "attempt": attempt, "seed": seed,
            "base_seed": spec["seed"], "role": role,
            "tried": tried, "ok": ok, "issues": issues, "warns": warns, "gen_s": round(gen_s, 2),
            **{k: round(float(v), 3) for k, v in m.items()}, **engine.describe(spec), "tool": VERSION}
    meta_p.write_text(json.dumps(meta, ensure_ascii=False, indent=1), "utf-8")
    if not ok:
        log("QA", logging.WARNING, item=label, role=role, chosen_attempt=attempt, issues=";".join(issues),
            note="모든 시도가 검사 탈락 — 가장 나은 것을 씀, 귀로 확인")
    return dict(meta, wav=str(wav_p), cached=False)


def load_cache_index(cache, args):
    """--assemble-only: 모델을 불러오지 않고 cache 메타로 문장 파일을 찾는다. 같은 글·말투·화자·기본 시드·모델 중 가장 최근 것."""
    model = "fake" if args.fake else args.model
    idx, files = {}, sorted(cache.glob("*.json"), key=lambda q: q.stat().st_mtime)
    for p in files:
        m = json.loads(p.read_text("utf-8"))
        wav = p.with_suffix(".wav")
        if m.get("model") == model and wav.is_file():
            idx[(m["text"], m["instruct"], m.get("speaker"), m.get("base_seed"))] = dict(m, wav=str(wav), cached=True)
    log("CACHE", files=len(files), usable=len(idx), model=model)
    return idx


# ----------------------------------------------------------------------------- 잇기·볼륨·내보내기
def gain_for(clips, sr):
    """전체 말소리 RMS를 TARGET_RMS_DB로, 최고점은 PEAK_DB 이하로 — 이득 하나(dB)."""
    allv = np.concatenate([c for c in clips if c.size]) if clips else np.zeros(1, np.float32)
    rms_db, peak = voiced_rms_db(allv, sr), float(np.max(np.abs(allv)) or 1e-9)
    peak_db = 20 * math.log10(peak)
    g = min(TARGET_RMS_DB - rms_db, PEAK_DB - peak_db)
    log("ASSEMBLE", rms_db_before=rms_db, peak_db_before=peak_db, gain_db=g, rms_db_after=rms_db + g, peak_db_after=peak_db + g)
    if rms_db + g < TARGET_RMS_DB - 3:
        log("ASSEMBLE", logging.WARNING, note="최고점 한도 때문에 목표보다 3dB 넘게 작음 — 튀는 소리가 있는 문장 확인")
    return g


def find_ffmpeg():
    ff = shutil.which("ffmpeg")
    if ff:
        return ff
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        return None


def export(y, sr, out_mp3, keep_wav=False):
    out_mp3 = Path(out_mp3)
    out_mp3.parent.mkdir(parents=True, exist_ok=True)
    wav_p = out_mp3.with_suffix(".wav")
    write_wav(wav_p, y, sr)
    ff = find_ffmpeg()
    if not ff:
        log("EXPORT", logging.WARNING, wav=wav_p, note="ffmpeg 없음 → WAV만 저장 (pip install imageio-ffmpeg 후 --assemble-only)")
        return wav_p
    r = subprocess.run([ff, "-y", "-hide_banner", "-loglevel", "error", "-i", str(wav_p), "-c:a", "libmp3lame", "-b:a", "160k", str(out_mp3)],
                       capture_output=True, text=True)
    if r.returncode != 0:
        log("EXPORT", logging.ERROR, error=r.stderr.strip()[:300], wav=wav_p, hint="WAV는 남아 있음 — 그대로 올려도 됨(25MB 이하일 때)")
        return wav_p
    probe = subprocess.run([ff, "-hide_banner", "-i", str(out_mp3)], capture_output=True, text=True).stderr
    mm = re.search(r"Duration:\s*(\d+):(\d+):([\d.]+)", probe)
    mp3_s = int(mm.group(1)) * 3600 + int(mm.group(2)) * 60 + float(mm.group(3)) if mm else float("nan")
    if not keep_wav:
        wav_p.unlink()
    log("EXPORT", mp3=out_mp3, seconds=len(y) / sr, mp3_seconds=mp3_s, mb=out_mp3.stat().st_size / 1e6)
    return out_mp3


def mmss(t):
    return f"{int(t // 60)}:{t % 60:04.1f}"


# ----------------------------------------------------------------------------- 결과 경로
def out_root(args):
    if args.out_dir:
        return Path(args.out_dir)
    kaggle = Path("/kaggle/working")
    return (kaggle / "tts_out") if kaggle.is_dir() else (ROOT / "output" / "tts")


def episode_paths(root, topic, vid):
    """정해진 결과 경로. upload/ 아래는 저장소와 같은 경로라 그대로 올리면 된다."""
    up = root / "upload" / topic / "source" / vid
    work = root / vid
    return {"upload": up, "narration": up / "narration.mp3", "meta": up / META_NAME,
            "work": work, "cache": work / "cache", "report": up / REPORT_NAME}


def repo_audio(topic, vid):
    src = ROOT / topic / "source" / vid
    return next((src / f"narration.{e}" for e in AUDIO_EXTS if (src / f"narration.{e}").is_file()), None)


# ----------------------------------------------------------------------------- 영상 하나 (build·all 이 함께 씀)
def build_episode(engine, topic, vid, args, root, txt=None):
    """대본 → 역할별 문장 → narration.mp3 하나 + tts_narration.json + tts_report.md (+ 작업 폴더에 역할별 문장 파일). → 결과 dict."""
    src = ROOT / topic / "source" / vid
    txt = Path(txt) if txt else src / f"{vid}.txt"
    if not txt.is_file():
        die("INPUT", "대본 TXT 없음", "주제 폴더·영상ID 확인 (Kaggle: 저장소를 git clone·pull 했는지)", path=txt)
    rows, cards = read_script(txt)
    card_after = {c["after"]: c for c in cards}
    lex = load_lexicon([getattr(args, "lexicon", None), ROOT / topic / "tts_lexicon.tsv", src / "tts_lexicon.tsv"])
    voices = load_voices(topic, vid, args)
    P = episode_paths(root, topic, vid)
    P["cache"].mkdir(parents=True, exist_ok=True)
    total_syl = sum(srt_tool.syllables(t) for t, _ in rows)
    log("INPUT", video=vid, txt=rel(txt), sentences=len(rows), cards=len(cards), syllables=total_syl,
        est_minutes=total_syl / 4.8 / 60, parts=" / ".join(dict.fromkeys(p for _, p in rows)), work=P["work"])
    for c in cards:
        if c["seconds"] < CARD_GAP_MIN:
            die("INPUT", f"고지 카드 쉼 {c['seconds']}초 < {CARD_GAP_MIN}초", "srt_tool.parse_cards 규칙 확인", after=c["after"])
        log("INPUT", video=vid, card_after_sentence=c["after"], card_title=c["title"], gap_s=c["seconds"])
    items = plan_items(vid, rows, voices, lex)
    changed = [it["n"] for it in items if it["tts"] != it["text"]]
    log("INPUT", video=vid, tts_text_changed=",".join(map(str, changed)) or "-", note="부호 금액·사전 바꿈 (대본·자막은 그대로)")

    k, K = (int(v) for v in getattr(args, "shard", "0/1").split("/"))   # all 은 문장을 나누지 않는다(영상 단위 --split)
    redo = parse_nums(getattr(args, "redo", ""))
    targets = [it for it in items if (it["n"] - 1) % K == k]
    metas = {}
    if engine is not None:
        t_start, done_syl, todo_syl = time.time(), 0, sum(it["syl"] for it in targets)
        for it in targets:
            m = make_sentence(engine, P["cache"], f"S{it['n']:03d}", it["tts"], it["spec"], it["syl"], args,
                              redo=it["n"] in redo, role=it["role"])
            metas[it["n"]] = m
            done_syl += it["syl"]
            if not m["cached"]:
                el = time.time() - t_start
                log("PROGRESS", video=vid, n=it["n"], of=len(items), role=it["role"], elapsed_min=el / 60,
                    eta_min=el / max(done_syl, 1) * (todo_syl - done_syl) / 60)
        if K > 1:
            log("SHARD", video=vid, shard=args.shard, made=len(targets), note="다른 조각도 끝나면 --assemble-only 로 잇기")
            return {"video": vid, "topic": topic, "status": "shard", "sentences": len(items)}
    else:   # --assemble-only
        index = load_cache_index(P["cache"], args)
        missing = []
        for it in items:
            hit = index.get((it["tts"], it["spec"]["instruct"], it["spec"]["speaker"], it["spec"]["seed"]))
            if hit:
                metas[it["n"]] = hit
            else:
                missing.append(it["n"])
        if missing:
            die("ASSEMBLE", f"문장 파일 없음: {ranges(missing)}", "--assemble-only 없이 다시 실행(없는 문장만 만든다)", video=vid)

    # 잇기: 볼륨은 영상 전체에 이득 하나 → narration (역할 사이 볼륨 차이도 모델이 낸 그대로)
    sr, clips = None, []
    for it in items:
        x, s = read_wav(metas[it["n"]]["wav"])
        if sr is None:
            sr = s
        elif s != sr:
            die("ASSEMBLE", f"표본율이 다름 S{it['n']:03d} {s} ≠ {sr}", "같은 모델로 다시 만들기", video=vid)
        clips.append(x)
    g = 10 ** (gain_for(clips, sr) / 20)
    clips = [x * g for x in clips]
    pieces, t, timing, gaps = [silence(args.lead_in, sr)], args.lead_in, {}, {}
    gap_kinds = {"sentence": 0, "part": 0, "card": 0}
    for i, it in enumerate(items):
        x = clips[i]
        timing[it["n"]] = (t, t + len(x) / sr)
        pieces.append(x)
        t += len(x) / sr
        if i == len(items) - 1:
            gap, kind = args.tail, "tail"
        elif it["n"] in card_after:
            gap, kind = card_after[it["n"]]["seconds"], "card"
        elif items[i + 1]["part"] != it["part"]:
            gap, kind = args.part_gap, "part"
        else:
            gap, kind = it["spec"]["gap"], "sentence"
        if kind == "card":
            log("ASSEMBLE", video=vid, card_after_sentence=it["n"], gap_s=gap, at=mmss(t), rule=f">= {CARD_GAP_MIN}s")
        gaps[it["n"]] = gap
        gap_kinds[kind] = gap_kinds.get(kind, 0) + 1
        pieces.append(silence(gap, sr))
        t += gap
    y = np.concatenate(pieces)
    total = len(y) / sr
    log("ASSEMBLE", video=vid, sentences=len(items), seconds=total, minutes=total / 60, sr=sr,
        gaps=" ".join(f"{k2}={v}" for k2, v in gap_kinds.items()), part_gap_s=args.part_gap)
    out = export(y, sr, P["narration"], keep_wav=args.keep_wav)

    # 역할별 정해진 경로(작업 폴더): OUT/<영상ID>/<역할>/S###.wav — 볼륨 맞춘 문장 파일. 결과 오디오는 narration.mp3 하나뿐이다
    role_out = {}
    for role in voices:
        mine = [i for i, it in enumerate(items) if it["role"] == role]
        rdir = P["work"] / role
        if rdir.is_dir():   # 대본이 바뀌어 번호가 달라졌을 때 옛 문장 파일이 섞이지 않게
            for old in rdir.glob("S*.wav"):
                old.unlink()
        if not mine:
            continue
        rdir.mkdir(parents=True, exist_ok=True)
        for i in mine:
            write_wav(rdir / f"S{items[i]['n']:03d}.wav", clips[i], sr)
        role_out[role] = {"dir": str(rdir), "sentences": len(mine), "range": ranges([items[i]["n"] for i in mine])}
        log("ROLE", video=vid, role=role, name=voices[role]["name"], files=f"{rdir}/S###.wav", count=len(mine),
            range=role_out[role]["range"])

    meta = {"tool": f"tts_narration.py {VERSION}", "created": datetime.now().isoformat(timespec="seconds"),
            "topic": topic, "id": vid, "script": rel(txt), "script_sha1": script_sha(rows, cards),
            "sentences": len(items), "seconds": round(total, 2), "engine": engine.describe(items[0]["spec"]) if engine else
            {k: metas[items[0]["n"]].get(k) for k in ("engine", "model", "language", "dtype")},
            "voices": {r: {k: v[k] for k in ("name", "parts", "speaker", "instruct", "part_instruct", "seed", "gap",
                                                "generation", "files")} for r, v in voices.items()},
            "gaps": {"lead_in": args.lead_in, "part": args.part_gap, "tail": args.tail,
                     "cards": [{"after": c["after"], "seconds": c["seconds"]} for c in cards]},
            "items": [{"n": it["n"], "role": it["role"], "part": it["part"], "text": it["text"],
                       "start": round(timing[it["n"]][0], 3), "end": round(timing[it["n"]][1], 3)} for it in items]}
    meta["voice_sha1"] = sha(meta["voices"])
    P["meta"].write_text(json.dumps(meta, ensure_ascii=False, indent=1), "utf-8")
    write_report(P["report"], topic, vid, args, items, metas, timing, cards, total, voices, role_out, out)
    flagged = [it["n"] for it in items if not metas[it["n"]]["ok"] or metas[it["n"]]["warns"]]
    log("SUMMARY", video=vid, out=out, meta=P["meta"], minutes=total / 60, flagged=ranges(flagged) or "-", report=P["report"])
    if Path(out).suffix != ".mp3":
        die("EXPORT", "mp3 를 만들지 못함 (WAV만 있음)", "ffmpeg 확인: pip install imageio-ffmpeg 후 --assemble-only", video=vid)
    return {"video": vid, "topic": topic, "status": "made", "sentences": len(items), "minutes": total / 60,
            "flagged": flagged, "out": str(out)}


def write_report(path, topic, vid, args, items, metas, timing, cards, total_s, voices, role_out, out):
    m0 = metas[items[0]["n"]]
    lines = [f"# 내레이션 보고 — {vid}", "",
             f"- 도구: tools/tts_narration.py {VERSION} · 만든 시각 {datetime.now().isoformat(timespec='seconds')}",
             f"- 모델: {m0.get('model')} · {m0.get('dtype')}",
             f"- 길이 {mmss(total_s)} · 문장 {len(items)}개 · 파트 쉼 {args.part_gap}초 · 고지 카드 "
             + (", ".join(f"문장 {c['after']} 뒤 {c['seconds']}초" for c in cards) or "없음"),
             f"- 결과 오디오(하나): 저장소 `{topic}/source/{vid}/narration.mp3` (옆에 `{META_NAME}`, 이 보고 `{REPORT_NAME}`)", "",
             "## 역할 (목소리 설정)", "", "| 역할 | 문장 | 화자 | 문장 쉼 | 시드 | 설정 파일 | 문장 파일 (Kaggle 작업 폴더) |", "|---|---|---|---|---|---|---|"]
    for role, v in voices.items():
        ro = role_out.get(role, {})
        lines.append(f"| {v['name']} (`{role}`) | {ro.get('range', '-')} ({ro.get('sentences', 0)}개) | {v['speaker']} | {v['gap']}초 | "
                     f"{v['seed']} | {', '.join(f'`{f}`' for f in v['files'])} | `{ro.get('dir', '-')}/S###.wav` |")
    lines += ["", "## 말투 지시", ""]
    for style, ins in dict.fromkeys((it["style"], it["spec"]["instruct"]) for it in items):
        lines.append(f"- **{style}**: {ins}")
    lines += ["", "## 문장", "", "| 번호 | 역할 | 파트 | 시작 | 길이(초) | 음절/초 | 시도 | 확인 |", "|---|---|---|---|---|---|---|---|"]
    for it in items:
        m = metas[it["n"]]
        flag = "; ".join(m["issues"] + m["warns"]) or "✅"
        lines.append(f"| {it['n']} | {voices[it['role']]['name']} | {it['part']} | {mmss(timing[it['n']][0])} | {m['dur']:.2f} | "
                     f"{m['rate']:.1f} | {m['attempt']} | {flag} |")
    bad = [it for it in items if not metas[it["n"]]["ok"] or metas[it["n"]]["warns"]]
    lines += ["", "## 귀로 확인할 문장", ""]
    lines += [f"- {it['n']}번 ({mmss(timing[it['n']][0])}, {voices[it['role']]['name']}): {it['text']} — "
              f"{'; '.join(metas[it['n']]['issues'] + metas[it['n']]['warns'])}" for it in bad] or ["- 없음 (그래도 사연 파트는 한 번 들어 보기)"]
    lines += ["", "다시 만들기: `python tools/tts_narration.py build <주제> <영상ID> --redo 12,15 --push` (새 시드로 그 문장만, 같은 Kaggle 세션 안에서)", ""]
    Path(path).write_text("\n".join(lines), "utf-8")


# ----------------------------------------------------------------------------- 명령: build (영상 하나)
def cmd_build(args):
    root = out_root(args)
    token = push_preflight(args)
    voices = load_voices(args.topic, args.id, args)
    engine = None if args.assemble_only else make_engine(args, {v["speaker"] for v in voices.values()})
    res = build_episode(engine, args.topic, args.id, args, root, txt=args.txt)
    if res["status"] != "made":
        return
    if args.push:
        if not push_results(root, [(args.topic, args.id)], token, args):
            raise SystemExit(1)
    else:
        log("NEXT", note=f"올리려면 같은 명령에 --push (또는 python tools/tts_narration.py push) → 저장소 {args.topic}/source/{args.id}/")


# ----------------------------------------------------------------------------- 명령: all (저장소의 대본 전부)
def topic_on_hold(topic):
    """주제 README 앞부분에 '⏸ … 보류' 표시가 있으면 보류 (사용자 지시 2026-10-10: 분석 결과 없는 주제는 진행하지 않음)."""
    p = ROOT / topic / "README.md"
    if not p.is_file():
        return False
    head = "\n".join(p.read_text("utf-8").splitlines()[:30])
    return any("⏸" in ln and "보류" in ln for ln in head.splitlines())


def repo_status(topic, vid, rows, cards):
    """저장소 상태 → (상태, 메모). made 여부는 따로 본다."""
    src = ROOT / topic / "source" / vid
    if (src / "youtube.json").is_file():
        return "uploaded", "이미 업로드(youtube.json)"
    audio = repo_audio(topic, vid)
    if not audio:
        return "todo", "오디오 없음"
    meta_p = src / META_NAME
    if not meta_p.is_file():
        return "has_audio", f"{audio.name} 있음 (직접 녹음 또는 v1.0 — 대본과 같은지 알 수 없음)"
    meta = json.loads(meta_p.read_text("utf-8"))
    if meta.get("script_sha1") != script_sha(rows, cards):
        return "stale", f"{audio.name} 이 옛 대본으로 만든 것 (바뀐 문장: check 명령)"
    return "has_audio", f"{audio.name} 있음 (지금 대본과 같음)"


def discover(args, root):
    """저장소의 대본 TXT(<주제>/source/<영상ID>/<영상ID>.txt)를 모두 읽어 할 일을 정한다."""
    want_topics = {t.strip() for t in (args.topics or "").split(",") if t.strip()}
    want_ids = {t.strip() for t in (args.ids or "").split(",") if t.strip()}
    plan = []
    for txt in sorted(ROOT.glob("*/source/*/*.txt")):
        vid, topic = txt.parent.name, txt.parent.parent.parent.name
        if txt.stem != vid or (want_topics and topic not in want_topics) or (want_ids and vid not in want_ids):
            continue
        rows, cards = read_script(txt)
        st, note = repo_status(topic, vid, rows, cards)
        hold = topic_on_hold(topic)
        P = episode_paths(root, topic, vid)
        made = P["meta"].is_file() and P["narration"].is_file() and \
            json.loads(P["meta"].read_text("utf-8")).get("script_sha1") == script_sha(rows, cards)
        if hold and not args.include_hold:
            action, why = "skip", "주제 보류(⏸ README) — --include-hold 로 포함"
        elif st == "uploaded":
            action, why = "skip", note
        elif st == "has_audio" and not args.force:
            action, why = "skip", note + " — 다시 만들려면 --force"
        elif st == "stale" and args.keep_stale:
            action, why = "skip", note + " — --keep-stale 이라 그대로 둠"
        elif made and not args.force:
            action, why = "done", f"이번 결과 폴더에 이미 만듦 ({rel(P['narration']) if str(P['narration']).startswith(str(ROOT)) else P['narration']})"
        else:
            action, why = "make", note + (" → 지금 대본으로 다시 만듦" if st == "stale" else "")
        syl = sum(srt_tool.syllables(t) for t, _ in rows)
        plan.append({"topic": topic, "video": vid, "action": action, "status": st, "why": why, "sentences": len(rows),
                     "est_min": syl / 4.8 / 60, "hold": hold})
        lvl = logging.WARNING if st == "stale" else logging.INFO
        log("PLAN", level=lvl, video=vid, topic=topic, action=action, status=st, sentences=len(rows),
            est_audio_min=syl / 4.8 / 60, why=why)
    return plan


def cmd_all(args):
    root = out_root(args)
    k, K = (int(v) for v in args.split.split("/"))
    plan = discover(args, root)
    todo = [p for p in plan if p["action"] == "make"]
    mine = [p for i, p in enumerate(todo) if i % K == k][: args.max or None]
    log("PLAN", scripts=len(plan), make=len(todo), this_process=len(mine), split=args.split, max=args.max or "-",
        out=root, list=",".join(p["video"] for p in mine) or "-",
        est_audio_min=sum(p["est_min"] for p in mine))
    done = [p for i, p in enumerate([p for p in plan if p["action"] == "done"]) if i % K == k]
    if args.dry_run:
        return
    token = push_preflight(args)
    pushed_ok = True
    if args.push and done:   # 이번 결과 폴더에 만들어 두고 아직 저장소에 없는 영상 → 다시 만들지 않고 올리기만
        log("PUSH", note="만들어 두고 못 올린 영상부터 올림", list=",".join(p["video"] for p in done))
        pushed_ok = push_results(root, [(p["topic"], p["video"]) for p in done], token, args)
    if not mine:
        log("PLAN", note="만들 영상 없음 (오디오가 없고 보류·업로드가 아닌 대본이 없음)")
        if not pushed_ok:
            raise SystemExit(1)
        return
    speakers = set()
    for p in mine:
        speakers |= {v["speaker"] for v in load_voices(p["topic"], p["video"], args).values()}
    engine = make_engine(args, speakers)
    results, t0 = [], time.time()
    for i, p in enumerate(mine, 1):
        log("BATCH", n=i, of=len(mine), video=p["video"], topic=p["topic"], elapsed_min=(time.time() - t0) / 60)
        try:
            res = build_episode(engine, p["topic"], p["video"], args, root)
            if args.push:   # 영상 하나가 끝날 때마다 바로 올린다 (세션이 끊겨도 끝난 영상은 저장소에 남게)
                try:
                    res["pushed"] = push_results(root, [(p["topic"], p["video"])], token, args)
                except Exception as e:   # 올리기 오류는 오디오 실패가 아니다 — 결과는 OUT/upload 에 남아 push 로 다시 올린다
                    res["pushed"] = False
                    log("PUSH", logging.ERROR, video=p["video"], error=_redact(f"{type(e).__name__}: {str(e)[:200]}", token),
                        hint="python tools/tts_narration.py push")
            results.append(res)
        except SystemExit:
            results.append({"video": p["video"], "topic": p["topic"], "status": "failed"})
            log("BATCH", logging.ERROR, video=p["video"], note="이 영상만 멈춤 — 위 [ERROR] 로그 확인, 다음 영상 계속")
        except Exception as e:   # GPU 메모리 부족 등: 이 영상만 실패로 남기고 다음 영상
            results.append({"video": p["video"], "topic": p["topic"], "status": "failed"})
            log("BATCH", logging.ERROR, video=p["video"], error=f"{type(e).__name__}: {str(e)[:200]}",
                hint="런타임 재시작 후 같은 명령 (만든 문장은 cache 에 남아 이어서 만든다)")
    for r in results:
        log("BATCH", video=r["video"], status=r["status"], minutes=r.get("minutes", 0.0),
            flagged=ranges(r.get("flagged", [])) or "-", pushed=r.get("pushed", "-"), out=r.get("out", "-"))
    failed = [r["video"] for r in results if r["status"] != "made"]
    not_pushed = [r["video"] for r in results if r["status"] == "made" and args.push and not r.get("pushed")]
    log("BATCH", done=len(results) - len(failed), failed=",".join(failed) or "-", not_pushed=",".join(not_pushed) or "-",
        total_min=(time.time() - t0) / 60)
    if args.push:
        if not not_pushed and not failed and pushed_ok:
            log("NEXT", note="영상마다 대본 폴더에 올라감 → Claude에게 '오디오 올렸어'")
        elif not not_pushed and pushed_ok:
            log("NEXT", logging.WARNING, note="만든 영상은 올라감. 실패한 영상은 위 [ERROR] 확인 뒤 같은 명령을 다시")
        else:
            log("NEXT", logging.WARNING, note="못 올린 영상: 토큰을 확인하고 python tools/tts_narration.py push (안 되면 pack 으로 zip)")
    elif K == 1 and not args.no_pack:
        pack(root)
    else:
        log("NEXT", note="다른 조각(--split)도 끝나면 python tools/tts_narration.py push (또는 pack)")
    if failed or not_pushed or not pushed_ok:
        raise SystemExit(1)


def pack(root):
    """OUT/upload/ 를 저장소 경로 그대로 zip 하나로. 압축을 풀어 저장소 최상위에 올리면 각 영상 폴더에 들어간다."""
    up = root / "upload"
    files = sorted(p for p in up.rglob("*") if p.is_file()) if up.is_dir() else []
    if not files:
        log("PACK", logging.WARNING, note="올릴 파일 없음", dir=up)
        return None
    zp = root / ZIP_NAME
    with zipfile.ZipFile(zp, "w") as z:
        for p in files:   # mp3 는 이미 압축돼 있어 그대로 넣는다(빠름), json 만 압축
            z.write(p, p.relative_to(up).as_posix(), compress_type=zipfile.ZIP_STORED if p.suffix == ".mp3" else zipfile.ZIP_DEFLATED)
    for p in files:
        log("PACK", file=p.relative_to(up).as_posix(), mb=p.stat().st_size / 1e6)
    log("PACK", zip=zp, files=len(files), mb=zp.stat().st_size / 1e6)
    log("NEXT", note=f"(--push 가 안 될 때만) {ZIP_NAME} 내려받기 → 압축 풀기 → GitHub 저장소 Add file → Upload files 에 "
                     "안의 폴더(stock 등)를 그대로 끌어 놓기 → Commit → Claude에게 '오디오 올렸어'")
    return zp


def cmd_pack(args):
    pack(out_root(args))



# ----------------------------------------------------------------------------- GitHub 올리기 (--push, push)
def get_token():
    """GitHub 토큰: 환경 변수 GITHUB_TOKEN → 없으면 Kaggle Secrets 의 GITHUB_TOKEN. 값은 어디에도 출력하지 않는다."""
    tok, src = os.environ.get(TOKEN_ENV, "").strip(), "env"
    if not tok:
        try:
            from kaggle_secrets import UserSecretsClient   # Kaggle 노트북 안에서만 있음
            tok, src = (UserSecretsClient().get_secret(TOKEN_ENV) or "").strip(), "kaggle_secrets"
        except Exception as e:   # 패키지 없음·비밀값 없음·노트북에 연결 안 됨 — 메시지에 값은 없다
            log("PUSH", logging.DEBUG, kaggle_secrets=type(e).__name__)
            tok = ""
    return tok, src


def _redact(text, token):
    return text.replace(token, "***") if token else text


class Git:
    """저장소(ROOT)에서 git 실행. 토큰은 GIT_ASKPASS 스크립트가 환경 변수에서 읽어 넘긴다 — 명령줄·원격 주소·설정 파일에 남지 않는다."""

    def __init__(self, token):
        self.token = token
        self.tmp = Path(tempfile.mkdtemp(prefix="tts_git_"))
        self.env = {**os.environ, "GIT_TERMINAL_PROMPT": "0"}
        if token:
            ask = self.tmp / "askpass.sh"
            ask.write_text('#!/bin/sh\ncase "$1" in\n  Username*) echo x-access-token ;;\n  *) printf "%s\\n" "$TTS_GIT_TOKEN" ;;\nesac\n')
            ask.chmod(0o700)
            self.env.update(GIT_ASKPASS=str(ask), TTS_GIT_TOKEN=token)

    def run(self, *argv, timeout=900):
        # core.fileMode=false: Kaggle 등에서 실행 권한(파일 모드)만 달라진 파일을 변경으로 보지 않게 (pull --rebase 가 멈추지 않게)
        cmd = ["git", "-C", str(ROOT), "-c", "credential.helper=", "-c", "core.fileMode=false",
               "-c", f"user.name={GIT_NAME}", "-c", f"user.email={GIT_EMAIL}", *argv]
        try:
            r = subprocess.run(cmd, capture_output=True, text=True, env=self.env, timeout=timeout)
        except subprocess.TimeoutExpired:
            return 124, f"시간 초과 {timeout}초"
        return r.returncode, _redact((r.stdout + r.stderr).strip(), self.token)

    def close(self):
        shutil.rmtree(self.tmp, ignore_errors=True)


def remote_url(g):
    rc, url = g.run("remote", "get-url", "origin")
    return url if rc == 0 else ""


def push_preflight(args):
    """--push 면 만들기 전에: 토큰이 있는지, 그 토큰으로 push 할 수 있는지 확인한다. 안 되면 GPU 시간을 쓰기 전에 멈춘다."""
    if not getattr(args, "push", False):
        return ""
    if not (ROOT / ".git").exists():
        die("PUSH", "저장소가 git clone 이 아님", "Kaggle 셀 1에서 git clone 한 폴더에서 실행", root=ROOT)
    token, src = get_token()
    g = Git(token)
    try:
        url = remote_url(g)
        if "@" in url.split("://")[-1].split("/")[0]:
            die("PUSH", "원격 주소에 계정 정보가 들어 있음", "git remote set-url origin https://github.com/yeomin1024/yeomin1024-ytb.git")
        github = "github.com" in url
        if getattr(args, "fake", False) and github:
            die("PUSH", "가짜 소리(--fake)는 GitHub에 올리지 않음", "--push 를 빼거나 시험용 저장소에서")
        if github and not token:
            die("PUSH", f"GitHub 토큰 없음 ({TOKEN_ENV})",
                "Kaggle 오른쪽 Add-ons → Secrets → GITHUB_TOKEN 추가 후 이 노트북에 연결(체크) — guides/tts_guide.md 2번. "
                "토큰을 셀·채팅에 붙여 넣지 않는다")
        # 권한만 본다: 없는 브랜치 이름으로 dry-run (main 이 앞서 있어도 fast-forward 문제로 실패하지 않게). 실제로 만들지는 않는다
        rc, out = g.run("push", "--dry-run", "origin", "HEAD:refs/heads/tts-push-check", timeout=120)
        if rc != 0:
            die("PUSH", f"push 권한 확인 실패: {' '.join(out.split())[:300]}",
                "토큰 만료·저장소 선택·Contents 읽기/쓰기 권한 확인 (guides/tts_guide.md 2번)", remote=url)
        log("PUSH", remote=url, token="있음(값은 표시하지 않음)" if token else "없음(로컬 원격)", token_source=src if token else "-",
            check="push --dry-run 통과")
        rc, dirty = g.run("status", "--porcelain", "--untracked-files=no")
        if rc == 0 and dirty.strip():   # 이 사본에서 바뀐 다른 파일 — 올리지 않는다 (결과 3개만 커밋)
            log("PUSH", logging.WARNING, local_changes=" ".join(ln[3:] for ln in dirty.splitlines())[:300],
                note="이 사본의 다른 변경은 커밋하지 않음. 사본을 main 과 맞추려면: git fetch origin main && git reset --hard origin/main")
    finally:
        g.close()
    return token


def _lock():
    """GPU 2개(--split)로 두 프로세스가 동시에 올려도 git 작업이 겹치지 않게 잠근다 (Linux·macOS)."""
    try:
        import fcntl
    except ImportError:
        return None
    f = open(ROOT / ".git" / "tts_push.lock", "w")
    fcntl.flock(f, fcntl.LOCK_EX)
    return f


def push_results(root, entries, token, args):
    """영상마다 결과 세 파일을 대본 폴더 <주제>/source/<영상ID>/ 에 복사 → 그 파일만 커밋 → pull --rebase → push. → 성공 여부."""
    lock = _lock()
    g = Git(token)
    try:
        paths, vids = [], []
        for topic, vid in entries:
            P = episode_paths(root, topic, vid)
            dst = ROOT / topic / "source" / vid
            if not (dst / f"{vid}.txt").is_file():
                log("PUSH", logging.WARNING, video=vid, note="저장소에 이 영상의 대본 폴더가 없음 — 건너뜀", dst=rel(dst))
                continue
            if not P["narration"].is_file() or not P["meta"].is_file():
                log("PUSH", logging.WARNING, video=vid, note="narration.mp3·메타 없음 — 건너뜀", src=P["upload"])
                continue
            new = json.loads(P["meta"].read_text("utf-8"))
            rows, cards = read_script(dst / f"{vid}.txt")
            if new.get("script_sha1") != script_sha(rows, cards):   # 지금 대본과 다른 옛 결과는 올리지 않는다
                log("PUSH", logging.WARNING, video=vid, note="이 결과는 옛 대본으로 만든 것 — 올리지 않음 (all 로 다시 만들기)")
                continue
            old_p = dst / META_NAME
            old = json.loads(old_p.read_text("utf-8")) if old_p.is_file() else {}
            if old.get("script_sha1") == new.get("script_sha1") and old.get("created", "") > new.get("created", ""):
                log("PUSH", logging.WARNING, video=vid, note="저장소에 더 나중에 만든 결과가 있음 — 덮어쓰지 않음",
                    repo_created=old.get("created"), this_created=new.get("created"))
                continue
            for name in REPO_FILES:
                if (P["upload"] / name).is_file():
                    shutil.copy2(P["upload"] / name, dst / name)
                    paths.append(rel(dst / name))
            for e in AUDIO_EXTS:   # 다른 확장자의 옛 내레이션이 있으면 지운다 (align-audio 가 mp3 를 먼저 쓰지만 헷갈리지 않게)
                old = dst / f"narration.{e}"
                if e != "mp3" and old.is_file():
                    rc, _ = g.run("rm", "-q", "--cached", "--ignore-unmatch", "--", rel(old))
                    old.unlink()
                    log("PUSH", video=vid, removed=rel(old), note="옛 내레이션 (다른 확장자)")
                    paths.append(rel(old))
            vids.append(vid)
            log("PUSH", video=vid, files=",".join(n for n in REPO_FILES if (P["upload"] / n).is_file()), dst=rel(dst),
                mb=P["narration"].stat().st_size / 1e6)
        if not vids:
            return False
        rc, out = g.run("add", "-A", "--", *paths)
        if rc != 0:
            log("PUSH", logging.ERROR, step="add", error=" ".join(out.split())[:300])
            return False
        rc, _ = g.run("diff", "--cached", "--quiet", "--", *paths)
        if rc == 0:   # 새로 커밋할 것은 없다 — 전에 커밋만 하고 못 올린 것이 있을 수 있으니 아래 push 는 그대로 한다
            log("PUSH", videos=",".join(vids), note="새로 커밋할 변경 없음 — 못 올린 커밋이 있으면 올림")
        else:
            msg = (f"내레이션: {', '.join(vids)} (tts_narration {VERSION}, Kaggle)\n\n"
                   f"자동 생성 — 대본 폴더마다 narration.mp3 · {META_NAME} · {REPORT_NAME}. 연구·교육용, 투자 권유 아님.")
            rc, out = g.run("commit", "-q", "-m", msg, "--", *paths)
            if rc != 0:
                log("PUSH", logging.ERROR, step="commit", error=" ".join(out.split())[:300])
                return False
        _, head = g.run("rev-parse", "--short", "HEAD")
        for attempt in range(1, PUSH_TRIES + 1):
            rc, out = g.run("pull", "-q", "--rebase", "--autostash", "origin", "main")
            if rc != 0:
                g.run("rebase", "--abort")
                log("PUSH", logging.WARNING, step="pull", attempt=attempt, error=" ".join(out.split())[:300])
            else:
                rc, out = g.run("push", "-q", "origin", "HEAD:main")
                if rc == 0:
                    _, head = g.run("rev-parse", "--short", "HEAD")
                    log("PUSH", videos=",".join(vids), commit=head, branch="main", ok=True,
                        note="대본 폴더마다 올라감: " + ", ".join(f"{t}/source/{v}/" for t, v in entries if v in vids))
                    return True
                log("PUSH", logging.WARNING, step="push", attempt=attempt, error=" ".join(out.split())[:300])
            time.sleep(2 ** attempt)
        log("PUSH", logging.ERROR, videos=",".join(vids), ok=False, commit=head,
            hint="커밋은 이 Kaggle 저장소에 남아 있음 → 잠시 뒤 python tools/tts_narration.py push, 안 되면 pack 으로 zip")
        return False
    finally:
        g.close()
        if lock:
            lock.close()


def cmd_push(args):
    """OUT/upload/ 에 만들어 둔 결과를 대본 폴더마다 올린다 (all·build 의 --push 가 실패했을 때, --split 뒤)."""
    root = out_root(args)
    args.push = True
    token = push_preflight(args)
    entries = sorted({(p.parents[1].name, p.name) for p in (root / "upload").glob("*/source/*") if (p / "narration.mp3").is_file()})
    if not entries:
        log("PUSH", logging.WARNING, note="올릴 결과 없음", dir=root / "upload")
        return
    if not push_results(root, entries, token, args):
        raise SystemExit(1)


# ----------------------------------------------------------------------------- 명령: check (저장소 오디오 ↔ 지금 대본)
def cmd_check(args):
    src = ROOT / args.topic / "source" / args.id
    txt = src / f"{args.id}.txt"
    if not txt.is_file():
        die("CHECK", "대본 TXT 없음", "주제 폴더·영상ID 확인", path=rel(txt))
    rows, cards = read_script(txt)
    audio, meta_p = repo_audio(args.topic, args.id), src / META_NAME
    if not audio:
        log("CHECK", video=args.id, ok=False, note="narration 오디오 없음")
        raise SystemExit(2)
    if not meta_p.is_file():
        log("CHECK", logging.WARNING, video=args.id, audio=rel(audio), ok="unknown",
            note=f"{META_NAME} 없음 (직접 녹음 또는 v1.0) — 문장 수는 align-audio 가 확인")
        return
    meta = json.loads(meta_p.read_text("utf-8"))
    now = script_sha(rows, cards)
    if meta.get("script_sha1") == now:
        log("CHECK", video=args.id, audio=rel(audio), ok=True, sentences=len(rows), made=meta.get("created"), tool=meta.get("tool"))
        return
    old = [(i["text"], i["part"]) for i in meta.get("items", [])]
    diff = [n for n in range(1, max(len(old), len(rows)) + 1)
            if n > len(old) or n > len(rows) or old[n - 1] != rows[n - 1]]
    log("CHECK", logging.WARNING, video=args.id, audio=rel(audio), ok=False, audio_sentences=len(old), script_sentences=len(rows),
        changed=ranges(diff) or "고지 카드만", hint="대본이 바뀜 → Kaggle 에서 all 을 다시 돌리면 이 영상을 지금 대본으로 다시 만든다")
    raise SystemExit(1)


# ----------------------------------------------------------------------------- 공통
def parse_nums(s):
    out = []
    for part in (s or "").replace(" ", "").split(","):
        if not part:
            continue
        a, _, b = part.partition("-")
        out += list(range(int(a), int(b or a) + 1))
    return out


def check_split(s, name):
    if not re.fullmatch(r"\d+/\d+", s) or not 0 <= int(s.split("/")[0]) < int(s.split("/")[1]):
        die("START", f"{name} 형식 오류: {s}", "예: 0/2, 1/2")


def main():
    ap = argparse.ArgumentParser(description="대본 TXT → 내레이션 하나 (Qwen3-TTS, Kaggle GPU, 사연자·진행자 목소리) → 대본 폴더에 GitHub 올리기")
    sub = ap.add_subparsers(dest="cmd", required=True)
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--model", default=DEFAULT_MODEL)
    common.add_argument("--speaker", default=None, help="모든 역할의 화자를 이것으로 (기본: voices/*.json 의 speaker, 한국어 Sohee)")
    common.add_argument("--language", default="Korean")
    common.add_argument("--gpu", type=int, default=0, help="GPU 번호 (Kaggle T4 x2: 0 또는 1)")
    common.add_argument("--device", default=None, help="직접 지정 (예: cuda:1, cpu)")
    common.add_argument("--dtype", default="auto", choices=["auto", "float32", "float16", "bfloat16"],
                        help="auto: T4는 float32, A100 등은 bfloat16")
    common.add_argument("--attn", default="auto", choices=["auto", "sdpa", "eager", "flash_attention_2"])
    common.add_argument("--seed", type=int, default=None, help="모든 역할의 기본 시드를 이것으로 (기본: voices/*.json 의 seed)")
    common.add_argument("--max-tries", type=int, default=3)
    common.add_argument("--temperature", type=float, default=None, help="비우면 모델 기본값 (역할별은 voices/*.json 의 generation)")
    common.add_argument("--top-p", type=float, default=None)
    common.add_argument("--top-k", type=int, default=None)
    common.add_argument("--repetition-penalty", type=float, default=None)
    common.add_argument("--gap", type=float, default=None, help="모든 역할의 문장 사이 쉼(초)을 이것으로 (기본: voices/*.json 의 gap)")
    common.add_argument("--lead-in", type=float, default=0.3, help="첫 문장 앞 쉼(초, 2초 이하)")
    common.add_argument("--out-dir", default=None, help="결과 최상위 폴더 (기본: Kaggle /kaggle/working/tts_out, 그 밖 output/tts)")
    common.add_argument("--keep-wav", action="store_true", help="narration.mp3 옆에 WAV도 남기기")
    common.add_argument("--fake", action="store_true", help="테스트: 모델 없이 가짜 소리")
    common.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])

    bopt = argparse.ArgumentParser(add_help=False)   # build·all 공통
    bopt.add_argument("--lexicon", default=None, help="읽는 소리 사전 TSV 추가 (기본: <주제>/tts_lexicon.tsv, source/<영상ID>/tts_lexicon.tsv)")
    bopt.add_argument("--part-gap", type=float, default=1.0, help="파트가 바뀔 때 쉼(초)")
    bopt.add_argument("--tail", type=float, default=0.8, help="마지막 문장 뒤 쉼(초)")
    bopt.add_argument("--push", action="store_true",
                      help="영상이 끝날 때마다 결과(narration.mp3·tts_narration.json·tts_report.md)를 대본 폴더에 GitHub main 으로 올리기 (토큰: GITHUB_TOKEN)")

    b = sub.add_parser("build", parents=[common, bopt], help="영상 하나 → narration.mp3 (--push 로 대본 폴더에 올림)")
    b.add_argument("topic")
    b.add_argument("id")
    b.add_argument("--txt", default=None, help="대본 TXT 직접 지정")
    b.add_argument("--redo", default="", help="새 시드로 다시 만들 문장 번호 (예: 12,15 또는 3-5)")
    b.add_argument("--shard", default="0/1", help="GPU 2개로 한 영상을 나눠 만들기: 0/2 와 1/2 를 동시에, 끝나면 --assemble-only")
    b.add_argument("--assemble-only", action="store_true", help="만들어 둔 문장 파일로 잇기·내보내기만")

    a = sub.add_parser("all", parents=[common, bopt], help="저장소의 대본을 모두 읽어 오디오가 없는 영상 전부")
    a.add_argument("--topics", default=None, help="이 주제만 (예: stock 또는 stock,health)")
    a.add_argument("--ids", default=None, help="이 영상만 (예: bittu-2026-10,panicsell-2026-10)")
    a.add_argument("--include-hold", action="store_true", help="보류(⏸) 주제도 포함")
    a.add_argument("--force", action="store_true", help="저장소에 지금 대본과 같은 오디오가 있어도 다시 만들기")
    a.add_argument("--keep-stale", action="store_true", help="옛 대본으로 만든 오디오를 다시 만들지 않기 (기본: 다시 만듦)")
    a.add_argument("--max", type=int, default=0, help="이번에 만들 최대 영상 수 (0 = 전부)")
    a.add_argument("--split", default="0/1", help="GPU 2개로 영상을 나눠: --gpu 0 --split 0/2 와 --gpu 1 --split 1/2 를 동시에 (--push 는 차례로 올림)")
    a.add_argument("--dry-run", action="store_true", help="무엇을 만들지 목록만 (모델 안 불러옴)")
    a.add_argument("--no-pack", action="store_true", help="--push 없이 돌릴 때 끝나고 zip 만들지 않기")

    sub.add_parser("push", parents=[common], help="만들어 둔 결과를 대본 폴더마다 GitHub main 에 올리기")
    sub.add_parser("pack", parents=[common], help=f"(올리기가 안 될 때만) OUT/upload/ → {ZIP_NAME}")

    c = sub.add_parser("check", parents=[common], help="저장소의 narration 이 지금 대본으로 만든 것인지 (tts_narration.json)")
    c.add_argument("topic")
    c.add_argument("id")

    args = ap.parse_args()
    logging.basicConfig(level=getattr(logging, args.log_level), format="%(message)s", stream=sys.stdout)
    log("START", tool=f"tts_narration.py {VERSION}", cmd=args.cmd, out=out_root(args), note="연구·교육용 — 투자 권유 아님")
    if args.lead_in > 2.0:
        die("START", "--lead-in 은 2초 이하", "srt_tool 규칙: 첫 자막 앞 여백 2초 이내")
    if args.cmd == "build":
        check_split(args.shard, "--shard")
        cmd_build(args)
    elif args.cmd == "all":
        check_split(args.split, "--split")
        cmd_all(args)
    elif args.cmd == "push":
        cmd_push(args)
    elif args.cmd == "pack":
        cmd_pack(args)
    else:
        cmd_check(args)


if __name__ == "__main__":
    main()
