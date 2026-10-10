#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.0 — 2026-10-10 — 최초 작성: 오픈소스 Qwen3-TTS(Apache-2.0)로 대본 TXT → narration.mp3, 파트별 말투 지시, Kaggle GPU(T4) 기준
r"""
대본 TXT로 내레이션 오디오를 만듭니다. Kaggle 노트북(GPU T4)에서 돌리는 것을 기준으로 썼습니다. 사용법: guides/tts_guide.md

  python tools/tts_narration.py sample                                        # 억울·후회 톤 시험: 말투 A·B·C·D × 시험 문장 5개
  python tools/tts_narration.py sample --episode stock/panicsell-2026-10 --lines 11-16   # 대본 문장 11~16으로 시험
  python tools/tts_narration.py build stock panicsell-2026-10                 # 영상 전체 → narration.mp3
  python tools/tts_narration.py build stock panicsell-2026-10 --story-style B # 사연 파트를 sample 의 B(울먹임) 말투로
  python tools/tts_narration.py build stock panicsell-2026-10 --redo 12,15    # 12·15번 문장만 새 시드로 다시
  python tools/tts_narration.py build stock panicsell-2026-10 --assemble-only # 만들어 둔 문장 파일로 잇기만
  python tools/tts_narration.py build stock panicsell-2026-10 --fake          # 테스트: 모델 없이 가짜 소리로 전 과정 확인

모델: Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice — 한국어 화자 Sohee, 말투를 글로 지시(instruct). 라이선스 Apache-2.0(상업 이용 가능).
  ※ 0.6B 모델은 말투 지시를 무시한다(qwen-tts 패키지가 instruct=None 으로 바꿈). 말투를 쓰려면 1.7B.

규칙 (guides/pipeline.md 4단계, guides/video_guide.md 2번 "내레이션")
  - 문장 = tools/srt_tool.py parse_txt 와 같은 순서(파트 라벨·[장면]·카드 문구 제외). 오디오 문장 = 대본 문장.
  - 문장 사이 쉼 0.45초(디지털 무음), 파트가 바뀌면 1.0초. align-audio(무음 −35dB·0.12초 이상)가 이 쉼으로 문장 경계를 찾는다.
  - 고지 카드 자리([장면] 바로 앞 문장 뒤): srt_tool.parse_cards 의 길이(문구 글자 수 ÷ 7 + 1초, 4~8초). 최소 3.5초 규칙보다 길다.
  - 문장마다 검사: 말 속도 2.5~8음절/초, 문장 안 무음 1.8초 이하, NaN·빈 소리 없음. 벗어나면 시드를 바꿔 다시(최대 3번).
  - 볼륨: 전체에 이득 하나만 곱한다(말소리 RMS −18dBFS, 최고점 −1dBFS 이하). 문장마다 따로 바꾸지 않는다.
  - 문장 파일은 work 폴더 cache/ 에 남는다(<키>.wav + <키>.json). 글·말투·화자·설정이 같으면 다시 만들지 않는다.
※ 연구·교육용 도구다. 영상 내용은 투자 권유가 아니다(주식 영상 고지 규칙은 stock/guides 를 따른다).
"""
import argparse
import hashlib
import importlib.util
import json
import logging
import math
import re
import shutil
import subprocess
import sys
import time
import wave
from datetime import datetime
from pathlib import Path

import numpy as np

TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent
sys.path.insert(0, str(TOOLS))
import srt_tool  # noqa: E402  (문장·카드 판정을 자막 도구와 똑같이 쓰기 위해)

VERSION = "v1.0"
CACHE_VERSION = 1            # 생성 방식이 바뀌면 올린다 → 문장 파일을 모두 다시 만든다
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

# 파트별 말투 지시(instruct). 영어로 쓴 이유: Qwen3-TTS 말투 지시는 중국어·영어 지시로 평가됐다(README InstructTTSEval-ZH/EN).
# 한국어 지시는 sample 의 D 로 비교해 볼 수 있다. CustomVoice 의 지시는 음색이 아니라 감정·속도·억양을 바꾼다.
STYLES = {
    "story": ("사연 — 억울하고 후회하는 1인칭 고백",
              "Speak like someone confessing a painful stock-market loss: regretful and aggrieved, "
              "a low voice that trembles slightly, slow pace, a soft sigh before key phrases, "
              "bitter self-blame as if holding back tears. Keep every word clear."),
    "host": ("진행자 — 차분하고 공감하는 진행",
             "A calm, trustworthy narrator of an investment-education channel. "
             "Warm and empathetic, steady medium pace, clear articulation, no exaggeration."),
    "explain": ("분석·방법 — 또렷한 설명",
                "A clear, composed documentary narrator explaining data. "
                "Confident and steady, medium pace, numbers pronounced distinctly, light emphasis on key figures."),
    "closing": ("마무리 — 따뜻한 인사",
                "A warm, gentle narrator closing the episode. Kind and encouraging, slightly slower, a soft smile in the voice."),
}
PART_STYLE = [("사연", "story"), ("진행", "host"), ("분석", "explain"), ("방법", "explain"), ("마무리", "closing")]

# sample: 같은 문장을 말투 4가지로 만들어 귀로 고른다. 고른 말투를 STYLES["story"] 에 넣는다.
SAMPLE_STYLES = {
    "A": ("담담한 후회",
          "Quietly regretful and subdued, as if replaying a costly mistake over and over. "
          "Low voice, slow pace, soft sighs, resigned self-blame. Keep every word clear."),
    "B": ("울먹임",
          "On the verge of tears after losing money in stocks: voice choked up and trembling, "
          "short pauses as if swallowing sobs, deep regret. Keep every word clear."),
    "C": ("억울함",
          "Aggrieved and frustrated at the unfairness of a stock loss: a bitter, tense voice that rises on the unfair parts "
          "and sinks into regret at the end of each sentence. Keep every word clear."),
    "D": ("한국어 지시",
          "주식으로 큰돈을 잃고 억울하고 후회하는 목소리로 말해 주세요. 낮고 살짝 떨리는 목소리, 느린 속도, "
          "중요한 말 앞에서 작은 한숨. 울음을 참는 듯하지만 단어는 또렷하게."),
}
SAMPLE_LINES = [
    "그날 아침까지만 해도 저는 괜찮을 줄 알았어요.",
    "4천만 원을 넣은 계좌가 하루 만에 -800만 원이 됐어요.",
    "남들은 다 번다는데 왜 저만 이렇게 됐는지, 억울해서 잠이 안 오더라고요.",
    "조금만 더 버텼으면 됐는데, 결국 제일 쌀 때 다 팔아 버렸어요.",
    "그 돈이 어떤 돈인데요… 다 제 탓이죠.",
]

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


def style_of(part):
    for word, key in PART_STYLE:
        if word in part:
            return key
    log("STYLE", logging.WARNING, part=part, fallback="host", note="파트 이름으로 말투를 정하지 못해 진행자 말투를 씀")
    return "host"


def load_lexicon(paths):
    """읽는 소리 사전 TSV: '원문<TAB>읽는 소리' (# 주석). TTS에 넣는 글에만 쓰고 대본·자막은 그대로 둔다."""
    pairs = []
    for p in paths:
        if not p or not Path(p).is_file():
            continue
        for ln in Path(p).read_text("utf-8-sig").splitlines():
            if ln.strip() and not ln.lstrip().startswith("#") and "\t" in ln:
                src, dst = ln.split("\t", 1)
                pairs.append((src.strip(), dst.strip()))
        log("INPUT", lexicon=p, entries=len(pairs))
    return sorted(pairs, key=lambda x: -len(x[0]))   # 긴 것부터 바꿔 겹침 방지


def tts_text(text, lexicon):
    """TTS에 넣는 글. 부호 붙은 금액은 뜻이 바뀌지 않게 소리로 바꾼다(srt_tool.spoken 과 같은 규칙): -800만 → 마이너스 800만."""
    s = text
    for src, dst in lexicon:
        s = s.replace(src, dst)
    s = re.sub(r"(?<![\w.])-(?=\d)", "마이너스 ", s)
    s = re.sub(r"(?<![\w.])\+(?=\d)", "플러스 ", s)
    return s


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
    """Qwen3-TTS CustomVoice. 화자 하나 + 문장마다 말투 지시."""

    def __init__(self, args):
        try:
            import torch
            from qwen_tts import Qwen3TTSModel
        except ImportError as e:
            die("MODEL", f"패키지 없음: {e}", "Kaggle 셀에서 먼저: !pip install -q -U qwen-tts")
        self.torch = torch
        self.speaker, self.language, self.model_id = args.speaker, args.language, args.model
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
        if args.dtype == "auto":
            dtype_name = "bfloat16" if cap >= (8, 0) else "float32"
        else:
            dtype_name = args.dtype
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
        if spk and self.speaker.lower() not in [s.lower() for s in spk]:
            die("MODEL", f"없는 화자: {self.speaker}", f"--speaker 를 이 중에서: {', '.join(spk)}")
        if langs and self.language.lower() not in [s.lower() for s in langs]:
            die("MODEL", f"없는 언어: {self.language}", f"--language 를 이 중에서: {', '.join(langs)}")
        if "0.6B" in self.model_id:
            log("MODEL", logging.WARNING, note="0.6B 모델은 말투 지시(instruct)를 무시함 — 감정 표현은 1.7B")
        self.gen = {k: v for k, v in {"temperature": args.temperature, "top_p": args.top_p, "top_k": args.top_k,
                                      "repetition_penalty": args.repetition_penalty}.items() if v is not None}

    def synth(self, text, instruct, seed, max_new_tokens):
        """→ (소리 float32, 표본율) 또는 생성 오류면 None."""
        torch = self.torch
        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)
        try:
            wavs, sr = self.model.generate_custom_voice(
                text=text, speaker=self.speaker, language=self.language, instruct=instruct or None,
                max_new_tokens=max_new_tokens, **self.gen)
        except torch.cuda.OutOfMemoryError as e:
            torch.cuda.empty_cache()
            log("TTS", logging.ERROR, error=f"GPU 메모리 부족: {e}", hint="런타임 재시작 후 다시 (만든 문장은 cache에 남아 있음)")
            raise
        except RuntimeError as e:   # 예: float16 넘침 → 'probability tensor contains either inf, nan'
            log("TTS", logging.WARNING, error=f"{type(e).__name__}: {str(e)[:200]}",
                hint="--dtype float16 을 썼다면 float32 로" if "nan" in str(e).lower() or "inf" in str(e).lower() else "")
            return None
        return np.asarray(wavs[0], dtype=np.float32).reshape(-1), int(sr)

    def describe(self):
        return {"engine": "qwen3-tts", "model": self.model_id, "speaker": self.speaker, "language": self.language,
                "dtype": self.dtype_name, "gen": self.gen}


class FakeEngine:
    """테스트용: 모델 없이 문장 길이에 맞는 가짜 소리(읽는 음절 ÷ 4.8초, 쉼표마다 0.25초 쉼, 앞뒤 무음)."""

    def __init__(self, args):
        self.sr, self.gen = 24000, {}
        log("MODEL", engine="fake", note="가짜 소리 — 잇기·쉼·내보내기·align-audio 확인용")

    def synth(self, text, instruct, seed, max_new_tokens):
        rng = np.random.default_rng(seed)
        out = [silence(0.15, self.sr)]
        chunks = [c for c in re.split(r"[,，]", text) if c.strip()]
        for i, ch in enumerate(chunks):
            d = max(0.3, srt_tool.syllables(ch) / 4.8 * rng.uniform(0.9, 1.1))
            t = np.arange(int(d * self.sr)) / self.sr
            out.append((0.2 * np.sin(2 * np.pi * 180 * t) * (0.6 + 0.4 * np.sin(2 * np.pi * 4.8 * t))).astype(np.float32))
            if i < len(chunks) - 1:
                out.append(silence(0.25, self.sr))
        out.append(silence(0.3, self.sr))
        return np.concatenate(out), self.sr

    def describe(self):
        return {"engine": "fake", "model": "fake", "speaker": "-", "language": "-", "dtype": "-", "gen": {}}


# ----------------------------------------------------------------------------- 문장 하나 만들기 (캐시·검사·다시)
def cache_key(engine, text, instruct, base_seed):
    d = dict(engine.describe(), text=text, instruct=instruct, seed=base_seed, cache=CACHE_VERSION)
    return hashlib.sha1(json.dumps(d, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()[:16]


def make_sentence(engine, cache_dir, label, text, instruct, syl, args, redo=False):
    """캐시에 있으면 그대로, 없으면(또는 redo) 만들고 검사한다. → 메타 dict (wav 경로 포함)."""
    key = cache_key(engine, text, instruct, args.seed)
    wav_p, meta_p = cache_dir / f"{key}.wav", cache_dir / f"{key}.json"
    old = json.loads(meta_p.read_text("utf-8")) if meta_p.is_file() else None
    if old and wav_p.is_file() and not redo:
        log("CACHE", item=label, key=key, dur=old["dur"], ok=old["ok"], level=logging.DEBUG)
        return dict(old, wav=str(wav_p), cached=True)
    # 시드: 기본 시드 + 글 내용 해시(문장 위치가 바뀌어도 같은 글은 같은 시드) + 시도 번호. redo 는 전에 쓴 시도 다음부터.
    seed0 = args.seed + int(key[:6], 16) % 1_000_000 * 10
    start = (max(old.get("tried", [0])) + 1) if (old and redo) else 1
    max_new = int(FRAME_HZ * max(syl, 4) / 2.0) + 50     # 2음절/초보다 느리면 끊는다(그보다 느리면 어차피 검사 탈락)
    best, tried = None, list(old.get("tried", [])) if (old and redo) else []
    for attempt in range(start, start + args.max_tries):
        seed = seed0 + attempt
        tried.append(attempt)
        t0 = time.time()
        res = engine.synth(text, instruct, seed, max_new)
        gen_s = time.time() - t0
        if res is None:
            log("TTS", logging.WARNING, item=label, attempt=attempt, seed=seed, ok=False, issues="생성 오류")
            continue
        x, sr = res
        nonfinite = not np.isfinite(x).all()
        x = trim(np.nan_to_num(x, nan=0.0, posinf=0.0, neginf=0.0), sr)
        ok, issues, warns, m = check(x, sr, syl, nonfinite)
        log("TTS", level=logging.INFO if ok else logging.WARNING, item=label, attempt=attempt, seed=seed, syl=syl,
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
    meta = {"key": key, "text": text, "instruct": instruct, "syl": syl, "sr": sr, "attempt": attempt, "seed": seed,
            "base_seed": args.seed,
            "tried": tried, "ok": ok, "issues": issues, "warns": warns, "gen_s": round(gen_s, 2),
            **{k: round(float(v), 3) for k, v in m.items()}, **engine.describe(), "tool": VERSION}
    meta_p.write_text(json.dumps(meta, ensure_ascii=False, indent=1), "utf-8")
    if not ok:
        log("QA", logging.WARNING, item=label, chosen_attempt=attempt, issues=";".join(issues), note="모든 시도가 검사 탈락 — 가장 나은 것을 씀, 귀로 확인")
    return dict(meta, wav=str(wav_p), cached=False)


def load_cache_index(cache, args):
    """--assemble-only: 모델을 불러오지 않고 cache 메타로 문장 파일을 찾는다. 같은 글·말투·모델·화자·기본 시드 중 가장 최근 것."""
    model, speaker = ("fake", "-") if args.fake else (args.model, args.speaker)
    idx, files = {}, sorted(cache.glob("*.json"), key=lambda q: q.stat().st_mtime)
    for p in files:
        m = json.loads(p.read_text("utf-8"))
        wav = p.with_suffix(".wav")
        if m.get("model") == model and m.get("speaker") == speaker and m.get("base_seed") == args.seed and wav.is_file():
            idx[(m["text"], m["instruct"])] = dict(m, wav=str(wav), cached=True)
    log("CACHE", files=len(files), usable=len(idx), model=model, speaker=speaker, base_seed=args.seed)
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


# ----------------------------------------------------------------------------- 명령: build
def cmd_build(args):
    src = ROOT / args.topic / "source" / args.id
    txt = Path(args.txt) if args.txt else src / f"{args.id}.txt"
    if not txt.is_file():
        die("INPUT", "대본 TXT 없음", "주제 폴더·영상ID 확인 (Kaggle: 저장소를 git clone 했는지)", path=txt)
    rows, cards = read_script(txt)
    card_after = {c["after"]: c for c in cards}
    lex = load_lexicon([args.lexicon, src / "tts_lexicon.tsv"])
    work = Path(args.out_dir or default_out(args.id))
    cache = work / "cache"
    cache.mkdir(parents=True, exist_ok=True)
    total_syl = sum(srt_tool.syllables(t) for t, _ in rows)
    log("INPUT", txt=txt, sentences=len(rows), cards=len(cards), syllables=total_syl,
        est_minutes=total_syl / 4.8 / 60, parts=" / ".join(dict.fromkeys(p for _, p in rows)), work=work)
    for c in cards:
        if c["seconds"] < CARD_GAP_MIN:
            die("INPUT", f"고지 카드 쉼 {c['seconds']}초 < {CARD_GAP_MIN}초", "srt_tool.parse_cards 규칙 확인", after=c["after"])
        log("INPUT", card_after_sentence=c["after"], card_title=c["title"], gap_s=c["seconds"])
    if args.story_style or args.story_instruct:   # sample 에서 고른 말투로 사연 파트를 바꾼다 (코드 수정 없이)
        if args.story_instruct:
            STYLES["story"] = ("사연 — 직접 지시", args.story_instruct)
        else:
            v = parse_variants(args.story_style)[0]
            STYLES["story"] = (f"사연 — {SAMPLE_STYLES[v][0]} (sample {v})", SAMPLE_STYLES[v][1])
    styles_used = {}
    items = []
    for n, (text, part) in enumerate(rows, 1):
        sk = style_of(part)
        name, instruct = STYLES[sk]
        styles_used[sk] = (name, instruct)
        items.append({"n": n, "text": text, "part": part, "style": sk, "instruct": instruct,
                      "tts": tts_text(text, lex), "syl": srt_tool.syllables(text)})
    for sk, (name, ins) in styles_used.items():
        log("STYLE", style=sk, name=name, instruct=ins)
    changed = [it["n"] for it in items if it["tts"] != it["text"]]
    log("INPUT", tts_text_changed=",".join(map(str, changed)) or "-", note="부호 금액·사전 바꿈 (대본·자막은 그대로)")

    k, K = (int(v) for v in args.shard.split("/"))
    redo = parse_nums(args.redo)
    targets = [it for it in items if (it["n"] - 1) % K == k]
    engine = None if args.assemble_only else (FakeEngine(args) if args.fake else QwenEngine(args))
    metas = {}
    if engine:
        t_start, done_syl, todo_syl = time.time(), 0, sum(it["syl"] for it in targets)
        for it in targets:
            m = make_sentence(engine, cache, f"S{it['n']:03d}", it["tts"], it["instruct"], it["syl"], args, redo=it["n"] in redo)
            metas[it["n"]] = m
            done_syl += it["syl"]
            if not m["cached"]:
                el = time.time() - t_start
                log("PROGRESS", n=it["n"], of=len(items), part=it["part"], elapsed_min=el / 60,
                    eta_min=el / max(done_syl, 1) * (todo_syl - done_syl) / 60)
        if K > 1:
            log("SHARD", shard=args.shard, made=len(targets), note="다른 조각도 끝나면 --assemble-only 로 잇기")
            return
    if args.assemble_only:
        index = load_cache_index(cache, args)
        missing = []
        for it in items:
            if (it["tts"], it["instruct"]) in index:
                metas[it["n"]] = index[(it["tts"], it["instruct"])]
            else:
                missing.append(it["n"])
        if missing:
            die("ASSEMBLE", f"문장 파일 없음: {','.join(map(str, missing))}", "--assemble-only 없이 다시 실행(없는 문장만 만든다)")
    sr = None
    clips = []
    for it in items:
        x, s = read_wav(metas[it["n"]]["wav"])
        if sr is None:
            sr = s
        elif s != sr:
            die("ASSEMBLE", f"표본율이 다름 S{it['n']:03d} {s} ≠ {sr}", "같은 모델로 다시 만들기")
        clips.append(x)
    g = 10 ** (gain_for(clips, sr) / 20)
    pieces, t, timing = [silence(args.lead_in, sr)], args.lead_in, []
    gap_kinds = {"sentence": 0, "part": 0, "card": 0}
    for i, it in enumerate(items):
        x = clips[i] * g
        timing.append((it["n"], t, t + len(x) / sr))
        pieces.append(x)
        t += len(x) / sr
        if i == len(items) - 1:
            gap, kind = args.tail, "tail"
        elif it["n"] in card_after:
            gap, kind = card_after[it["n"]]["seconds"], "card"
        elif items[i + 1]["part"] != it["part"]:
            gap, kind = args.part_gap, "part"
        else:
            gap, kind = args.gap, "sentence"
        if kind == "card":
            log("ASSEMBLE", card_after_sentence=it["n"], gap_s=gap, at=mmss(t), rule=f">= {CARD_GAP_MIN}s")
        gap_kinds[kind] = gap_kinds.get(kind, 0) + 1
        pieces.append(silence(gap, sr))
        t += gap
    y = np.concatenate(pieces)
    log("ASSEMBLE", sentences=len(items), seconds=len(y) / sr, minutes=len(y) / sr / 60, sr=sr,
        gaps=" ".join(f"{k2}={v}" for k2, v in gap_kinds.items()), gap_s=args.gap, part_gap_s=args.part_gap)
    out = export(y, sr, work / "narration.mp3", keep_wav=args.keep_wav)
    write_report(work / "report.md", args, items, metas, timing, cards, len(y) / sr)
    flagged = [it["n"] for it in items if not metas[it["n"]]["ok"] or metas[it["n"]]["warns"]]
    log("SUMMARY", out=out, minutes=len(y) / sr / 60, flagged=",".join(map(str, flagged)) or "-", report=work / "report.md")
    log("NEXT", note=f"{out.name} 를 저장소 {args.topic}/source/{args.id}/narration{out.suffix} 로 올린 뒤 Claude에게 '오디오 올렸어'")


def write_report(path, args, items, metas, timing, cards, total_s):
    m0 = metas[items[0]["n"]]
    lines = [f"# 내레이션 보고 — {args.id}", "",
             f"- 도구: tools/tts_narration.py {VERSION} · 만든 시각 {datetime.now().isoformat(timespec='seconds')}",
             f"- 모델: {m0.get('model')} · 화자 {m0.get('speaker')} · {m0.get('dtype')} · 기본 시드 {args.seed}",
             f"- 길이 {mmss(total_s)} · 문장 {len(items)}개 · 쉼 {args.gap}초 / 파트 {args.part_gap}초 / 고지 카드 "
             + ", ".join(f"문장 {c['after']} 뒤 {c['seconds']}초" for c in cards), "",
             "## 말투 지시", ""]
    for sk in dict.fromkeys(it["style"] for it in items):
        lines.append(f"- **{STYLES[sk][0]}**: {STYLES[sk][1]}")
    lines += ["", "## 문장", "", "| 번호 | 파트 | 시작 | 길이(초) | 음절/초 | 시도 | 확인 |", "|---|---|---|---|---|---|---|"]
    start = {n: a for n, a, _ in timing}
    for it in items:
        m = metas[it["n"]]
        flag = "; ".join(m["issues"] + m["warns"]) or "✅"
        lines.append(f"| {it['n']} | {it['part']} | {mmss(start[it['n']])} | {m['dur']:.2f} | {m['rate']:.1f} | {m['attempt']} | {flag} |")
    bad = [it for it in items if not metas[it["n"]]["ok"] or metas[it["n"]]["warns"]]
    lines += ["", "## 귀로 확인할 문장", ""]
    lines += [f"- {it['n']}번 ({mmss(start[it['n']])}): {it['text']} — {'; '.join(metas[it['n']]['issues'] + metas[it['n']]['warns'])}"
              for it in bad] or ["- 없음 (그래도 사연 파트는 한 번 들어 보기)"]
    lines += ["", "다시 만들기: `python tools/tts_narration.py build <주제> <영상ID> --redo 12,15` (새 시드로 그 문장만)", ""]
    Path(path).write_text("\n".join(lines), "utf-8")


# ----------------------------------------------------------------------------- 명령: sample
def cmd_sample(args):
    if args.episode:
        topic, vid = args.episode.strip("/").split("/", 1)
        txt = ROOT / topic / "source" / vid / f"{vid}.txt"
        if not txt.is_file():
            die("INPUT", "대본 TXT 없음", "--episode 주제폴더/영상ID 확인", path=txt)
        rows, _ = read_script(txt)
        if args.lines:
            nums = parse_nums(args.lines)
        else:   # 사연 파트의 마지막 6문장 (후회가 가장 짙은 곳)
            nums = [n for n, (_, p) in enumerate(rows, 1) if style_of(p) == "story"][-6:]
        lines = [rows[n - 1][0] for n in nums if 1 <= n <= len(rows)]
        log("INPUT", episode=args.episode, lines=",".join(map(str, nums)))
    else:
        lines = list(SAMPLE_LINES)
        log("INPUT", source="내장 시험 문장", lines=len(lines))
    variants = {v: SAMPLE_STYLES[v] for v in parse_variants(args.styles)}
    if args.instruct:
        variants["X"] = ("직접 지시", args.instruct)
    work = Path(args.out_dir or default_out("sample"))
    cache = work / "cache"
    cache.mkdir(parents=True, exist_ok=True)
    engine = FakeEngine(args) if args.fake else QwenEngine(args)
    outs = []
    for v, (name, instruct) in variants.items():
        log("STYLE", variant=v, name=name, instruct=instruct)
        clips, sr, rates = [], None, []
        for i, text in enumerate(lines, 1):
            m = make_sentence(engine, cache, f"{v}{i:02d}", tts_text(text, []), instruct, srt_tool.syllables(text), args)
            x, sr = read_wav(m["wav"])
            clips.append(x)
            rates.append(m["rate"])
        g = 10 ** (gain_for(clips, sr) / 20)
        pieces = [silence(args.lead_in, sr)]
        for x in clips:
            pieces += [x * g, silence(args.gap, sr)]
        out = export(np.concatenate(pieces), sr, work / f"sample_{v}.mp3", keep_wav=args.keep_wav)
        log("SAMPLE", variant=v, name=name, out=out, mean_rate=float(np.mean(rates)))
        outs.append(out)
    log("NEXT", note="노트북 셀에서 듣기: from IPython.display import Audio, display; "
                     + "; ".join(f"display(Audio('{o}'))" for o in outs))
    log("NEXT", note="마음에 드는 말투로 전체 만들기: build <주제> <영상ID> --story-style B (또는 --story-instruct \"...\")")


# ----------------------------------------------------------------------------- 공통
def default_out(name):
    kaggle = Path("/kaggle/working")
    return (kaggle / "tts_out" / name) if kaggle.is_dir() else (ROOT / "output" / "tts" / name)


def parse_nums(s):
    out = []
    for part in (s or "").replace(" ", "").split(","):
        if not part:
            continue
        a, _, b = part.partition("-")
        out += list(range(int(a), int(b or a) + 1))
    return out


def parse_variants(s):
    vs = [v.strip().upper() for v in s.split(",") if v.strip()]
    bad = [v for v in vs if v not in SAMPLE_STYLES]
    if bad:
        die("STYLE", f"없는 말투: {','.join(bad)}", f"--styles 를 {','.join(SAMPLE_STYLES)} 중에서")
    return vs


def main():
    ap = argparse.ArgumentParser(description="대본 TXT → 내레이션 (Qwen3-TTS, Kaggle GPU)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--model", default=DEFAULT_MODEL)
    common.add_argument("--speaker", default="Sohee", help="CustomVoice 화자 (한국어: Sohee)")
    common.add_argument("--language", default="Korean")
    common.add_argument("--gpu", type=int, default=0, help="GPU 번호 (Kaggle T4 x2: 0 또는 1)")
    common.add_argument("--device", default=None, help="직접 지정 (예: cuda:1, cpu)")
    common.add_argument("--dtype", default="auto", choices=["auto", "float32", "float16", "bfloat16"],
                        help="auto: T4는 float32, A100 등은 bfloat16")
    common.add_argument("--attn", default="auto", choices=["auto", "sdpa", "eager", "flash_attention_2"])
    common.add_argument("--seed", type=int, default=1234, help="기본 시드 (문장마다 글 내용으로 정해진 만큼 더한다)")
    common.add_argument("--max-tries", type=int, default=3)
    common.add_argument("--temperature", type=float, default=None, help="비우면 모델 기본값")
    common.add_argument("--top-p", type=float, default=None)
    common.add_argument("--top-k", type=int, default=None)
    common.add_argument("--repetition-penalty", type=float, default=None)
    common.add_argument("--gap", type=float, default=0.45, help="문장 사이 쉼(초)")
    common.add_argument("--lead-in", type=float, default=0.3, help="첫 문장 앞 쉼(초, 2초 이하)")
    common.add_argument("--out-dir", default=None, help="기본: /kaggle/working/tts_out/<영상ID> (Kaggle), output/tts/<영상ID>")
    common.add_argument("--keep-wav", action="store_true", help="mp3 옆에 WAV도 남기기")
    common.add_argument("--fake", action="store_true", help="테스트: 모델 없이 가짜 소리")
    common.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])

    b = sub.add_parser("build", parents=[common], help="영상 전체 내레이션 → narration.mp3")
    b.add_argument("topic")
    b.add_argument("id")
    b.add_argument("--txt", default=None, help="대본 TXT 직접 지정")
    b.add_argument("--lexicon", default=None, help="읽는 소리 사전 TSV (기본: source/<영상ID>/tts_lexicon.tsv 가 있으면 씀)")
    b.add_argument("--part-gap", type=float, default=1.0, help="파트가 바뀔 때 쉼(초)")
    b.add_argument("--tail", type=float, default=0.8, help="마지막 문장 뒤 쉼(초)")
    b.add_argument("--redo", default="", help="새 시드로 다시 만들 문장 번호 (예: 12,15 또는 3-5)")
    b.add_argument("--shard", default="0/1", help="GPU 2개로 나눠 만들기: 0/2 와 1/2 를 동시에, 끝나면 --assemble-only")
    b.add_argument("--assemble-only", action="store_true", help="만들어 둔 문장 파일로 잇기·내보내기만")
    b.add_argument("--story-style", default=None, help="사연 파트 말투를 sample 의 A·B·C·D 중 하나로")
    b.add_argument("--story-instruct", default=None, help="사연 파트 말투 지시를 직접 쓰기")

    s = sub.add_parser("sample", parents=[common], help="말투 시험 (억울·후회 톤 A·B·C·D)")
    s.add_argument("--episode", default=None, help="주제폴더/영상ID — 그 대본 문장으로 시험")
    s.add_argument("--lines", default=None, help="대본 문장 번호 (예: 11-16)")
    s.add_argument("--styles", default="A,B,C,D", help="시험할 말투")
    s.add_argument("--instruct", default=None, help="직접 쓴 말투 지시를 X로 추가")
    args = ap.parse_args()
    logging.basicConfig(level=getattr(logging, args.log_level), format="%(message)s", stream=sys.stdout)
    log("START", tool=f"tts_narration.py {VERSION}", cmd=args.cmd, note="연구·교육용 — 투자 권유 아님")
    if args.lead_in > 2.0:
        die("START", "--lead-in 은 2초 이하", "srt_tool 규칙: 첫 자막 앞 여백 2초 이내")
    if args.cmd == "build":
        if not re.fullmatch(r"\d+/\d+", args.shard) or not 0 <= int(args.shard.split("/")[0]) < int(args.shard.split("/")[1]):
            die("START", f"--shard 형식 오류: {args.shard}", "예: 0/2, 1/2")
        cmd_build(args)
    else:
        cmd_sample(args)


if __name__ == "__main__":
    main()
