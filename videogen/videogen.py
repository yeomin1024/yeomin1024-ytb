#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.1.0 — 2026-10-18 — 사용자 지시 "핵심 코드를 하나로 만들어서 저장소에 올리고 kaggle에서는 코드 받아서 실행하는
#          방식으로 하고 prompt 같은 설정만 고치고 실행만 하는 코드를 따로 알려줘": v1.0.0 노트북 2개(diffusers 헤드리스 ·
#          WanGP 웹 UI)의 핵심을 이 파일 하나로 합침. WanGP 는 웹 UI 대신 `wgp.py --process`(헤드리스)로 돌려서 두 길 모두
#          설정(dict)만 바꾸고 run() 한 번으로 실행. CHANGELOG: videogen/CHANGELOG.md
r"""
오픈소스 영상 생성 AI 를 Kaggle(GPU T4 x2)에서 설정만 바꿔 돌리는 핵심 코드 — 파일 하나.

Kaggle 셀 (videogen/README.md 의 셀을 그대로):
    SETTINGS = dict(model="wan2.2-5b", prompt="...", preset="t4_fast", seed=42)
    ... videogen.py 를 raw.githubusercontent.com 에서 받아 ...
    result = videogen.run(SETTINGS)

터미널:
    python videogen/videogen.py --model wan2.2-5b --prompt "A cat surfing" --preset t4_fast
    python videogen/videogen.py --settings my_settings.json

모델 (MODELS):
    wan2.2-5b             diffusers 로 Wan2.2-TI2V-5B (Apache-2.0)  — 기본값, 오프라인 스모크 테스트 통과
    wan2.2-14b-lightning  WanGP 로 Wan2.2 T2V 14B + Lightning 4-step LoRA (Apache-2.0)
    ltx2.5-distilled      WanGP 로 LTX-2.5 Distilled 22B, 영상+오디오 (LTX-2 Community License — 연매출 1천만 달러 이상 유료)

결과: <output_dir>/<run_id>/ 에 영상 + videogen_<run_id>.json(설정·버전·시간·코드 sha256) + run.log
로그 형식: [STAGE] [TIMESTAMP] [LEVEL] message key=value ...
※ 연구·교육용 도구다. 모델별 라이선스·Kaggle 약관·생성물 권리 확인은 사용자 책임이다.
"""
from __future__ import annotations

import argparse
import gc
import hashlib
import json
import logging
import os
import platform
import random
import re
import shutil
import subprocess
import sys
import time
from dataclasses import asdict, dataclass, field, fields

__version__ = "1.1.0"

# --------------------------------------------------------------------------------------------------
# 모델 · 프리셋
# --------------------------------------------------------------------------------------------------
MODELS = {
    "wan2.2-5b": dict(backend="diffusers", repo="Wan-AI/Wan2.2-TI2V-5B-Diffusers", license="Apache-2.0"),
    "wan2.2-14b-lightning": dict(backend="wangp", model_type="t2v_2_2", license="Apache-2.0",
                                 profile="wan_2_2/Lightning t2v v2025-09-28 2 Phases - 4 Steps.json"),
    "ltx2.5-distilled": dict(backend="wangp", model_type="ltx2_25_22B_distilled", profile=None,
                             license="LTX-2 Community License (revenue >= USD 10M needs a paid license)"),
}

# steps/guidance_scale 는 diffusers 에만 쓴다. WanGP 는 모델 기본값(Lightning 이면 4 step)을 쓰고,
# 사용자가 steps/guidance_scale 을 직접 적었을 때만 넘긴다.
PRESETS = {
    "t4_fast":       dict(height=480, width=832,  num_frames=81,  steps=30, guidance_scale=5.0),
    "t4_balanced":   dict(height=704, width=1280, num_frames=49,  steps=40, guidance_scale=5.0),
    "official_720p": dict(height=704, width=1280, num_frames=121, steps=50, guidance_scale=5.0),
}

# Wan 공식 부정 프롬프트 (Wan2.x 예제에 실린 중국어 원문)
WAN_NEGATIVE_PROMPT = (
    "色调艳丽，过曝，静态，细节模糊不清，字幕，风格，作品，画作，画面，静止，整体发灰，最差质量，低质量，JPEG压缩残留，"
    "丑陋的，残缺的，多余的手指，画得不好的手部，画得不好的脸部，畸形的，毁容的，形态畸形的肢体，手指融合，"
    "静止不动的画面，杂乱的背景，三条腿，背景人很多，倒着走"
)

# diffusers 길에서 Kaggle 커널에 맞춰 둘 패키지 (오프라인 스모크 테스트에 쓴 버전). torch 는 Kaggle 것을 그대로 쓴다.
DIFFUSERS_PACKAGES = {"diffusers": "==0.41.0", "transformers": "==5.20.1", "accelerate": ">=1.10",
                      "ftfy": "", "sentencepiece": "", "imageio": ">=2.34", "imageio-ffmpeg": ""}

WANGP_REPO = "https://github.com/deepbeepmeep/Wan2GP.git"
# WanGP 가 문서화한 torch 빌드 (setup_config.json @ wangp_ref). CUDA 13 휠은 드라이버 580 이상이 필요하다.
TORCH_BUILDS = {
    "cu130": dict(pkgs=["torch==2.10.0", "torchvision==0.25.0", "torchaudio==2.10.0"],
                  index="https://download.pytorch.org/whl/cu130", min_driver=580),
    "cu128": dict(pkgs=["torch==2.7.1", "torchvision==0.22.1", "torchaudio==2.7.1"],
                  index="https://download.pytorch.org/whl/cu128", min_driver=525),
}
MEDIA_EXT = {".mp4", ".webm", ".mkv", ".gif", ".png", ".jpg", ".jpeg", ".webp", ".wav", ".mp3", ".flac"}


@dataclass
class Config:
    # ---- 자주 바꾸는 것 ----
    model: str = "wan2.2-5b"
    prompt: str = ("A golden retriever runs through a sunlit meadow toward the camera, wildflowers swaying, "
                   "slow motion, cinematic lighting, shallow depth of field, 35mm film look.")
    negative_prompt: str = WAN_NEGATIVE_PROMPT
    preset: str = "t4_fast"
    seed: int = 42
    # ---- 프리셋 값 덮어쓰기 (None = 프리셋/모델 기본값) ----
    height: int | None = None
    width: int | None = None
    num_frames: int | None = None
    steps: int | None = None
    guidance_scale: float | None = None
    fps: int | None = None                       # None: diffusers 24fps, WanGP 는 모델 기본값
    # ---- 경로 ----
    output_dir: str = "/kaggle/working/outputs"  # 결과 (Kaggle Output 탭으로 저장됨, 20GB 한도)
    work_dir: str = "/kaggle/tmp/videogen"       # 가중치·venv·WanGP 소스 (저장 안 되는 임시 디스크)
    log_level: str = "INFO"                      # DEBUG | INFO | WARNING
    preview: bool = True                         # 노트북이면 끝나고 영상 미리보기
    # ---- diffusers 길 ----
    max_sequence_length: int = 512
    model_revision: str = "main"                 # 재현하려면 HF 커밋 해시
    model_path: str | None = None                # 로컬 diffusers 폴더 (스모크 테스트용) — repo 대신 사용
    device_plan: str = "auto"                    # auto(T4 x2 = 2장 나눠 씀) | single | cpu(테스트용)
    vae_tiling: bool = True
    step_log_every: int = 5
    install_deps: bool = True                    # Kaggle 에서 필요한 pip 패키지 자동 설치
    # ---- WanGP 길 ----
    wangp_ref: str = "fde3c7e10c47c854913d5877d955901a35e44714"  # 2026-10-17 HEAD (v18.17). "main" = 최신
    wangp_profile: str = "4"                     # 메모리 프로필 (4 = 가중치를 나눠 GPU 로, 기본). RAM 부족하면 "5"
    wangp_attention: str = "sage"                # sage(SageAttention 1.0.6, T4) | sdpa
    wangp_gpu: str = "cuda:0"
    wangp_torch_build: str = "auto"              # auto | cu130 | cu128
    wangp_dry_run_first: bool = True             # 생성 전에 설정 검증(--dry-run)으로 실제 step·프레임 수를 로그에
    wangp_extra: dict = field(default_factory=dict)  # WanGP 설정 키를 직접 (고급, 마지막에 덮어씀)
    wangp_app_dir: str | None = None             # 이미 있는 WanGP 폴더 (테스트·재사용)
    wangp_python: str | None = None              # 이미 있는 파이썬 (테스트·재사용) — 주면 설치를 건너뜀


def make_config(settings: dict | Config | None = None, **overrides) -> Config:
    """dict/Config + 키워드 → Config. 모르는 키는 오타일 수 있어 바로 멈춘다."""
    base = asdict(settings) if isinstance(settings, Config) else dict(settings or {})
    base.update(overrides)
    valid = {f.name for f in fields(Config)}
    unknown = sorted(set(base) - valid)
    if unknown:
        raise ValueError(f"알 수 없는 설정 {unknown}. 쓸 수 있는 키: {sorted(valid)}")
    cfg = Config(**base)
    if cfg.model not in MODELS:
        raise ValueError(f"model={cfg.model!r} 없음. 고를 수 있는 것: {list(MODELS)}")
    if cfg.preset not in PRESETS:
        raise ValueError(f"preset={cfg.preset!r} 없음. 고를 수 있는 것: {list(PRESETS)}")
    if not cfg.prompt.strip():
        raise ValueError("prompt 가 비어 있다")
    return cfg


# --------------------------------------------------------------------------------------------------
# 로깅: [STAGE] [TIMESTAMP] [LEVEL] message key=value ...
# --------------------------------------------------------------------------------------------------
LOGGER = logging.getLogger("videogen")


class _StageFormatter(logging.Formatter):
    def format(self, record):
        ts = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(record.created))
        return f"[{getattr(record, 'stage', 'GENERAL')}] [{ts}] [{record.levelname}] {record.getMessage()}"


def _setup_logging(level: str, log_file: str):
    LOGGER.handlers.clear()
    LOGGER.setLevel(getattr(logging, level.upper(), logging.INFO))
    LOGGER.propagate = False
    for h in (logging.StreamHandler(sys.stdout), logging.FileHandler(log_file, encoding="utf-8")):
        h.setFormatter(_StageFormatter())
        LOGGER.addHandler(h)


def _fmt(v):
    if isinstance(v, float):
        return f"{v:.4g}"
    s = str(v)
    return f'"{s}"' if " " in s else s


def log(stage: str, msg: str = "", level: int = logging.INFO, **kv):
    LOGGER.log(level, " ".join([msg] + [f"{k}={_fmt(v)}" for k, v in kv.items()]).strip(), extra={"stage": stage})


class _Stage:
    """단계별 시간 기록 + 실패하면 어떤 단계에서 왜 멈췄는지와 다음 할 일을 남긴다."""

    def __init__(self, name: str, timings: dict, hint: str):
        self.name, self.timings, self.hint = name, timings, hint

    def __enter__(self):
        self.t0 = time.perf_counter()
        log(self.name, "start")
        return self

    def __exit__(self, exc_type, exc, tb):
        self.timings[self.name] = round(time.perf_counter() - self.t0, 2)
        if exc is not None:
            log(self.name, "FAILED", logging.ERROR, error=repr(exc)[:500], next_step=self.hint)
        else:
            log(self.name, "done", sec=self.timings[self.name])
        return False


# --------------------------------------------------------------------------------------------------
# 공통 도우미
# --------------------------------------------------------------------------------------------------
def _sha256(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _read_json(*parts: str) -> dict:
    with open(os.path.join(*parts), encoding="utf-8") as f:
        return json.load(f)


def _free_disk_gb(path: str) -> float:
    p = path
    while not os.path.exists(p):
        p = os.path.dirname(p) or "/"
    return round(shutil.disk_usage(p).free / 1e9, 1)


def _ram_gb() -> tuple[float, float]:
    try:
        with open("/proc/meminfo") as f:
            info = {k: int(v.split()[0]) / 1e6 for k, v in (line.split(":", 1) for line in f)}
        return round(info["MemTotal"], 1), round(info["MemAvailable"], 1)
    except (OSError, KeyError, ValueError):
        return float("nan"), float("nan")


def _nvidia_smi() -> list[dict]:
    """GPU 목록 (torch 없이). nvidia-smi 가 없으면 빈 목록."""
    try:
        out = subprocess.run(["nvidia-smi", "--query-gpu=index,name,driver_version,memory.total,compute_cap",
                              "--format=csv,noheader"], capture_output=True, text=True, timeout=30).stdout
    except (OSError, subprocess.TimeoutExpired):
        return []
    keys = ["idx", "name", "driver", "vram", "cc"]
    return [dict(zip(keys, [c.strip() for c in row.split(",")])) for row in out.strip().splitlines() if row.strip()]


def resolve_params(cfg: Config, spatial_multiple: int | None = None, temporal_factor: int | None = None) -> dict:
    """프리셋 + 직접 적은 값 → 실제 생성 값. 모양 규칙(배수·4k+1)을 맞출 때는 전·후 값을 경고로 남긴다."""
    p = dict(PRESETS[cfg.preset])
    explicit = {k for k in p if getattr(cfg, k) is not None}
    for k in explicit:
        p[k] = getattr(cfg, k)
    p["explicit"] = sorted(explicit)
    if spatial_multiple:
        for k in ("height", "width"):
            fixed = max(spatial_multiple, p[k] // spatial_multiple * spatial_multiple)
            if fixed != p[k]:
                log("DATA", f"{k} is not a multiple of {spatial_multiple}; adjusted", logging.WARNING,
                    before=p[k], after=fixed)
                p[k] = fixed
    if temporal_factor and p["num_frames"] % temporal_factor != 1:
        fixed = max(1, p["num_frames"] // temporal_factor * temporal_factor + 1)
        log("DATA", f"num_frames must be {temporal_factor}k+1; adjusted", logging.WARNING,
            before=p["num_frames"], after=fixed)
        p["num_frames"] = fixed
    return p


def _ensure_packages(specs: dict[str, str]):
    """빠졌거나 버전이 다른 패키지만 pip 로 설치 (다시 실행할 때 시간 낭비 없게)."""
    from importlib import metadata
    try:
        from packaging.specifiers import SpecifierSet
    except ImportError:
        SpecifierSet = None
    need = []
    for name, spec in specs.items():
        try:
            have = metadata.version(name)
            if spec and (SpecifierSet is None or have not in SpecifierSet(spec)):
                need.append(name + spec)
        except metadata.PackageNotFoundError:
            need.append(name + spec)
    if not need:
        log("SETUP", "packages already satisfied", packages=len(specs))
        return
    if any(m in sys.modules for m in ("diffusers", "transformers")):
        log("SETUP", "diffusers/transformers already imported in this kernel; restart the kernel if the "
                     "upgrade below does not take effect", logging.WARNING)
    log("SETUP", "pip install", packages=" ".join(need))
    r = subprocess.run([sys.executable, "-m", "pip", "install", "-q", *need], capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"pip install failed: {r.stderr[-1500:]}\n→ Kaggle 설정에서 Internet 을 켰는지 확인")


# --------------------------------------------------------------------------------------------------
# diffusers 길: 텍스트 인코딩 → 디노이즈 → VAE 디코딩을 단계별로 올리고 내린다
# --------------------------------------------------------------------------------------------------
def _diffusers_generate(cfg: Config, run_dir: str, run_id: str, timings: dict) -> dict:
    import numpy as np
    import torch

    if tuple(int(x) for x in torch.__version__.split("+")[0].split(".")[:2]) < (2, 6):
        raise RuntimeError(f"torch {torch.__version__} 는 너무 오래됨 (transformers 5.x 는 2.6 이상). "
                           "Kaggle Settings → Environment 에서 최신 환경을 고르세요.")
    import diffusers
    import transformers
    from diffusers import AutoencoderKLWan, WanPipeline, WanTransformer3DModel
    from diffusers.pipelines.wan.pipeline_wan import prompt_clean
    from diffusers.utils import export_to_video

    def vram(dev):
        if not dev.startswith("cuda"):
            return "n/a"
        return f"{torch.cuda.memory_allocated(dev) / 1e9:.2f}GB(peak {torch.cuda.max_memory_allocated(dev) / 1e9:.2f}GB)"

    def free(dev):
        gc.collect()
        if dev.startswith("cuda"):
            torch.cuda.empty_cache()

    def stats(t):
        t = t.float()
        return dict(shape=tuple(t.shape), mean=t.mean().item(), std=t.std().item(),
                    finite=bool(torch.isfinite(t).all()))

    # ---- SETUP: 장치·dtype·시드 ----
    with _Stage("SETUP", timings, "Accelerator 를 GPU T4 x2 로 두고 세션을 다시 시작"):
        log("SETUP", "libraries", torch=torch.__version__, cuda=torch.version.cuda,
            diffusers=diffusers.__version__, transformers=transformers.__version__)
        gpus = [dict(idx=i, name=torch.cuda.get_device_properties(i).name,
                     cc=f"{torch.cuda.get_device_properties(i).major}.{torch.cuda.get_device_properties(i).minor}")
                for i in range(torch.cuda.device_count())]
        if cfg.device_plan == "cpu":
            te_dev = dit_dev = vae_dev = "cpu"
            dtype = torch.float32
        else:
            if not gpus:
                raise RuntimeError("CUDA GPU 가 없다. Kaggle 설정에서 Accelerator = GPU T4 x2")
            # Turing(T4, cc 7.5)은 bf16 텐서 코어가 없어 fp16, Ampere 이상은 체크포인트 기본인 bf16
            dtype = torch.bfloat16 if min(int(g["cc"].split(".")[0]) for g in gpus) >= 8 else torch.float16
            two = cfg.device_plan == "auto" and len(gpus) >= 2
            te_dev, dit_dev, vae_dev = ("cuda:1", "cuda:0", "cuda:1") if two else ("cuda:0",) * 3
        vae_dtype = torch.float32  # 모델 카드 권장
        log("SETUP", "device plan", text_encoder=te_dev, dit=dit_dev, vae=vae_dev,
            dtype=str(dtype).replace("torch.", ""), vae_dtype="float32")
        random.seed(cfg.seed)
        np.random.seed(cfg.seed)
        torch.manual_seed(cfg.seed)
        torch.cuda.manual_seed_all(cfg.seed)
        log("SETUP", "seed fixed", seed=cfg.seed)

    # ---- DATA: 가중치 받기·확인 + 생성 값 확정 ----
    with _Stage("DATA", timings, "다시 실행. 계속 실패하면 Internet=On 확인 또는 model_revision 고정"):
        if cfg.model_path:
            model_dir = cfg.model_path
            log("DATA", "using local weights", path=model_dir)
        else:
            from huggingface_hub import snapshot_download
            token = _kaggle_secret("HF_TOKEN")
            cache = os.path.join(cfg.work_dir, "hf_cache")
            if _free_disk_gb(cache) < 30:
                log("DATA", "low disk for weights (~25GB needed)", logging.WARNING, free_gb=_free_disk_gb(cache))
            repo = MODELS[cfg.model]["repo"]
            log("DATA", "downloading", repo=repo, revision=cfg.model_revision, cache=cache,
                hf_token="set" if token else "none")
            t0, err, model_dir = time.perf_counter(), None, None
            for attempt in range(1, 4):
                try:
                    model_dir = snapshot_download(repo, revision=cfg.model_revision, cache_dir=cache, token=token,
                                                  allow_patterns=["model_index.json", "scheduler/*", "tokenizer/*",
                                                                  "text_encoder/*", "transformer/*", "vae/*"])
                    break
                except Exception as e:  # 네트워크·허브 오류: 재시도, 조용히 넘어가지 않음
                    err = e
                    log("DATA", "download attempt failed", logging.WARNING, attempt=attempt, error=repr(e)[:300])
                    time.sleep(10 * attempt)
            if model_dir is None:
                raise RuntimeError(f"가중치 다운로드 3회 실패 ({err!r}). Internet=On · HF 상태 · HF_TOKEN 시크릿 확인")
            log("DATA", "weights ready", path=model_dir, sec=round(time.perf_counter() - t0, 1))
        index = _read_json(model_dir, "model_index.json")
        tr_cfg = _read_json(model_dir, "transformer", "config.json")
        vae_cfg = _read_json(model_dir, "vae", "config.json")
        log("DATA", "model config", pipeline=index.get("_class_name"), expand_timesteps=index.get("expand_timesteps"),
            dit_layers=tr_cfg.get("num_layers"), dit_in_ch=tr_cfg.get("in_channels"), vae_z=vae_cfg.get("z_dim"),
            vae_spatial=vae_cfg.get("scale_factor_spatial"), vae_temporal=vae_cfg.get("scale_factor_temporal"))
        if index.get("_class_name") != "WanPipeline":
            raise ValueError(f"WanPipeline 저장소가 아님: {index.get('_class_name')}")
        if tr_cfg["in_channels"] != vae_cfg["z_dim"]:
            raise ValueError(f"DiT in_channels={tr_cfg['in_channels']} != VAE z_dim={vae_cfg['z_dim']}")
        params = resolve_params(cfg, vae_cfg.get("scale_factor_spatial", 8) * tr_cfg["patch_size"][1],
                                vae_cfg.get("scale_factor_temporal", 4))
        fps = cfg.fps or 24
        log("DATA", "generation params", preset=cfg.preset, height=params["height"], width=params["width"],
            num_frames=params["num_frames"], steps=params["steps"], guidance_scale=params["guidance_scale"],
            fps=fps, duration_sec=round(params["num_frames"] / fps, 2))

    # ---- ENCODE: 텍스트 인코더 장치에서 임베딩 → 바로 해제 ----
    with _Stage("ENCODE", timings, "GPU 1장에서 메모리 부족이면 GPU T4 x2 로 다시 시작"):
        # VAE 는 DECODE 전까지 CPU 에 둔다 (파이프라인이 VAE 에서 잠재 공간 배율을 읽기 때문에 지금 넘김)
        vae = AutoencoderKLWan.from_pretrained(model_dir, subfolder="vae", dtype=vae_dtype)
        pipe = WanPipeline.from_pretrained(model_dir, vae=vae, transformer=None, text_encoder=None)
        te_cls = getattr(transformers, index["text_encoder"][1])
        te = te_cls.from_pretrained(model_dir, subfolder="text_encoder", dtype=dtype).to(te_dev).eval()
        pipe.register_modules(text_encoder=te)
        n_tok = len(pipe.tokenizer(prompt_clean(cfg.prompt)).input_ids)
        log("ENCODE", "text encoder loaded", cls=te_cls.__name__, device=te_dev, vram=vram(te_dev),
            prompt_tokens=n_tok, max_tokens=cfg.max_sequence_length)
        if n_tok > cfg.max_sequence_length:
            log("ENCODE", "prompt will be truncated", logging.WARNING, tokens=n_tok, limit=cfg.max_sequence_length)
        use_cfg = params["guidance_scale"] > 1.0

        def encode():
            with torch.inference_mode():
                return pipe.encode_prompt(prompt=cfg.prompt, negative_prompt=cfg.negative_prompt,
                                          do_classifier_free_guidance=use_cfg, num_videos_per_prompt=1,
                                          max_sequence_length=cfg.max_sequence_length, device=dit_dev, dtype=dtype)

        emb, neg = encode()
        if not (torch.isfinite(emb).all() and (neg is None or torch.isfinite(neg).all())):
            log("ENCODE", "non-finite fp16 embeddings; re-encoding on CPU in bf16", logging.WARNING)
            pipe.register_modules(text_encoder=te.to("cpu", torch.bfloat16))
            free(te_dev)
            emb, neg = encode()
            if not torch.isfinite(emb).all():
                raise FloatingPointError("CPU bf16 로 다시 해도 프롬프트 임베딩에 NaN/Inf")
        log("ENCODE", "prompt embeddings", **stats(emb))
        if neg is not None:
            log("ENCODE", "negative embeddings", **stats(neg))
        pipe.register_modules(text_encoder=None)
        del te
        free(te_dev)
        log("ENCODE", "text encoder released", vram=vram(te_dev))

    # ---- DENOISE: DiT (잠재값만 — 디코딩은 DiT 를 내린 뒤) ----
    st = {"t": None, "i": -1, "nan": None, "sps": None}

    def on_step_end(p, i, t, kw):
        total = params["steps"]
        if i == 0 or (i + 1) % cfg.step_log_every == 0 or i == total - 1:
            s = stats(kw["latents"])  # .item() 이 GPU 를 동기화하므로 아래 시간은 실제 계산 시간
            now = time.perf_counter()
            if st["t"] is not None:
                st["sps"] = (now - st["t"]) / (i - st["i"])
            st["t"], st["i"] = now, i
            log("DENOISE", "step", step=f"{i + 1}/{total}", timestep=float(t), latent_mean=s["mean"],
                latent_std=s["std"], finite=s["finite"], sec_per_step=st["sps"] or "warmup",
                eta_min=round(st["sps"] * (total - i - 1) / 60, 1) if st["sps"] else "n/a", vram=vram(dit_dev))
            if not s["finite"]:
                st["nan"] = i
                p._interrupt = True  # 남은 step 은 파이프라인이 건너뜀
        return {}

    with _Stage("DENOISE", timings, "메모리 부족 → preset 't4_fast' 나 num_frames 줄이기 · NaN → 로그의 dtype/GPU 확인"):
        dit = WanTransformer3DModel.from_pretrained(model_dir, subfolder="transformer", dtype=dtype).to(dit_dev).eval()
        pipe.register_modules(transformer=dit)
        # 잠재값·스케줄러는 pipe._execution_device 에 만들어진다 → DiT 장치여야 함 (VAE 는 아직 CPU)
        if pipe._execution_device != torch.device(dit_dev):
            raise RuntimeError(f"execution device {pipe._execution_device} != DiT device {dit_dev}")
        log("DENOISE", "DiT loaded", device=dit_dev, dtype=str(dit.dtype).replace("torch.", ""),
            params_b=round(sum(x.numel() for x in dit.parameters()) / 1e9, 2), vram=vram(dit_dev),
            scheduler=type(pipe.scheduler).__name__, flow_shift=pipe.scheduler.config.get("flow_shift"))
        out = pipe(prompt_embeds=emb, negative_prompt_embeds=neg if use_cfg else None,
                   height=params["height"], width=params["width"], num_frames=params["num_frames"],
                   num_inference_steps=params["steps"], guidance_scale=params["guidance_scale"],
                   generator=torch.Generator(device=dit_dev).manual_seed(cfg.seed), output_type="latent",
                   callback_on_step_end=on_step_end, callback_on_step_end_tensor_inputs=["latents"])
        latents = out.frames
        if st["nan"] is not None:
            raise FloatingPointError(f"{st['nan'] + 1} step 에서 잠재값이 NaN/Inf (dtype={dtype}). "
                                     "다른 seed 나 bf16 지원 GPU 로 시도")
        log("DENOISE", "final latents", **stats(latents))
        pipe.register_modules(transformer=None)
        del dit, out
        free(dit_dev)
        log("DENOISE", "DiT released", vram=vram(dit_dev))

    # ---- DECODE: VAE(fp32) → 프레임 + 결과 검사 ----
    with _Stage("DECODE", timings, "메모리 부족 → vae_tiling=True 유지 또는 해상도 낮추기"):
        vae.to(vae_dev)
        if cfg.vae_tiling:
            vae.enable_tiling()
        lat = latents.to(vae_dev, dtype=vae.dtype)
        # WanPipeline.__call__ (diffusers 0.41.0) 과 같은 역정규화
        mean = torch.tensor(vae.config.latents_mean).view(1, vae.config.z_dim, 1, 1, 1).to(lat.device, lat.dtype)
        inv_std = 1.0 / torch.tensor(vae.config.latents_std).view(1, vae.config.z_dim, 1, 1, 1).to(lat.device, lat.dtype)
        with torch.inference_mode():
            video = vae.decode(lat / inv_std + mean, return_dict=False)[0]
        frames = pipe.video_processor.postprocess_video(video, output_type="np")[0]  # (F, H, W, 3), 0~1
        fstats = dict(frames=frames.shape[0], height=frames.shape[1], width=frames.shape[2],
                      mean=float(frames.mean()), std=float(frames.std()), finite=bool(np.isfinite(frames).all()),
                      temporal_diff=float(np.abs(np.diff(frames, axis=0)).mean()) if frames.shape[0] > 1 else 0.0)
        log("DECODE", "frames", vram=vram(vae_dev), **fstats)
        if not fstats["finite"]:
            raise FloatingPointError("디코딩한 프레임에 NaN/Inf")
        if fstats["std"] < 0.02:
            log("DECODE", "near-constant frames (black/flat video?)", logging.WARNING, std=fstats["std"])
        if fstats["temporal_diff"] < 1e-3:
            log("DECODE", "almost no motion between frames", logging.WARNING, temporal_diff=fstats["temporal_diff"])
        del video, lat
        vae.to("cpu")
        free(vae_dev)

    with _Stage("EXPORT", timings, "/kaggle/working 남은 공간 확인 (20GB 한도)"):
        path = os.path.join(run_dir, f"{cfg.model}_{run_id}_seed{cfg.seed}.mp4")
        export_to_video(list(frames), path, fps=fps)
        log("EXPORT", "saved", video=path, size_mb=round(os.path.getsize(path) / 1e6, 2), fps=fps,
            duration_sec=round(fstats["frames"] / fps, 2))

    return dict(videos=[path], params=params, frame_stats=fstats, fps=fps, gpus=gpus,
                devices=dict(te=te_dev, dit=dit_dev, vae=vae_dev), dtype=str(dtype),
                versions=dict(torch=torch.__version__, diffusers=diffusers.__version__,
                              transformers=transformers.__version__))


def _kaggle_secret(name: str) -> str | None:
    """Kaggle Secrets → 환경 변수 순서로 찾는다. 값은 로그에 남기지 않는다."""
    try:
        from kaggle_secrets import UserSecretsClient
        return UserSecretsClient().get_secret(name)
    except Exception:
        return os.environ.get(name)


# --------------------------------------------------------------------------------------------------
# WanGP 길: 격리 venv 에 설치 → 설정 JSON → `wgp.py --process` (웹 UI 없음)
# --------------------------------------------------------------------------------------------------
def pick_torch_build(driver_version: str, forced: str = "auto") -> str:
    if forced != "auto":
        if forced not in TORCH_BUILDS:
            raise ValueError(f"wangp_torch_build={forced!r} 없음: {list(TORCH_BUILDS)}")
        return forced
    major = int(driver_version.strip().split(".")[0])
    for name in ("cu130", "cu128"):
        if major >= TORCH_BUILDS[name]["min_driver"]:
            return name
    raise RuntimeError(f"NVIDIA 드라이버 {driver_version} 는 지원하는 torch 빌드보다 오래됨")


def _child_env(**extra) -> dict:
    """venv 하위 프로세스 환경: 커널의 PYTHONPATH 와 인라인 matplotlib 백엔드를 뺀다
    (venv 에 matplotlib_inline 이 없어 `import matplotlib.pyplot` 이 깨짐)."""
    env = {k: v for k, v in os.environ.items() if k not in ("PYTHONPATH", "PYTHONHOME", "VIRTUAL_ENV")}
    env.update(MPLBACKEND="Agg", PYTHONUNBUFFERED="1", **extra)
    return env


def _run(stage: str, cmd: list, hint: str, log_file: str, cwd=None, check=True, timeout=3600):
    """명령 실행: 전체 출력은 log_file 에, 결과는 한 줄로."""
    t0 = time.perf_counter()
    log(stage, "exec", cmd=" ".join(map(str, cmd))[:240])
    r = subprocess.run(list(map(str, cmd)), cwd=cwd, env=_child_env(), capture_output=True, text=True, timeout=timeout)
    sec = round(time.perf_counter() - t0, 1)
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"\n$ {' '.join(map(str, cmd))}\n(rc={r.returncode}, {sec}s)\n{r.stdout}\n{r.stderr}\n")
    if r.returncode != 0:
        log(stage, "command failed", logging.ERROR, rc=r.returncode, sec=sec, next_step=hint, full_log=log_file)
        for line in (r.stderr or r.stdout).strip().splitlines()[-6:]:
            log(stage, "  | " + line[:300], logging.ERROR)
        if check:
            raise RuntimeError(f"[{stage}] 실패: {' '.join(map(str, cmd))[:120]} (전체 출력: {log_file})")
    else:
        log(stage, "ok", sec=sec)
    return r


def _wangp_install(cfg: Config, timings: dict, install_log: str) -> tuple[str, str, str]:
    """WanGP 소스(커밋 고정) + Python 3.11 venv. 같은 세션에서 두 번째부터는 표식 파일로 건너뜀.
    → (app_dir, python, attention)"""
    app_dir = cfg.wangp_app_dir or os.path.join(cfg.work_dir, "Wan2GP")
    if cfg.wangp_python:
        log("INSTALL", "using given interpreter (install skipped)", python=cfg.wangp_python, app_dir=app_dir)
        return app_dir, cfg.wangp_python, cfg.wangp_attention
    venv = os.path.join(cfg.work_dir, "wgp-venv")
    py = os.path.join(venv, "bin", "python")
    marker = os.path.join(venv, ".videogen_install.json")
    want = dict(wangp_ref=cfg.wangp_ref, attention_requested=cfg.wangp_attention,
                torch_build=cfg.wangp_torch_build, videogen=__version__)
    if os.path.exists(marker):
        done = _read_json(marker)
        if {k: done.get(k) for k in want} == want:
            log("INSTALL", "already installed in this session", **done)
            return app_dir, py, done["attention"]

    with _Stage("INSTALL", timings, "wangp_logs 의 install 로그에서 실패한 패키지 확인 · Internet=On 확인"):
        gpus = _nvidia_smi()
        if not gpus:
            raise RuntimeError("nvidia-smi 에 GPU 가 없다. Accelerator = GPU T4 x2")
        build_name = pick_torch_build(gpus[0]["driver"], cfg.wangp_torch_build)
        build = TORCH_BUILDS[build_name]
        log("INSTALL", "torch build selected", build=build_name, driver=gpus[0]["driver"], packages=" ".join(build["pkgs"]))
        if _free_disk_gb(cfg.work_dir) < 60:
            log("INSTALL", "scratch disk < 60GB: 14B/22B models may not fit", logging.WARNING,
                free_gb=_free_disk_gb(cfg.work_dir))
        # 1) 커밋 고정 소스 (그 커밋만 얕게)
        if not os.path.isdir(os.path.join(app_dir, ".git")):
            os.makedirs(app_dir, exist_ok=True)
            _run("INSTALL", ["git", "init", "-q", app_dir], "디스크 공간 확인", install_log)
            _run("INSTALL", ["git", "-C", app_dir, "remote", "add", "origin", WANGP_REPO], "", install_log)
            _run("INSTALL", ["git", "-C", app_dir, "fetch", "--depth", "1", "origin", cfg.wangp_ref],
                 "Internet=On 확인, 또는 wangp_ref='main'", install_log)
            _run("INSTALL", ["git", "-C", app_dir, "checkout", "-q", "FETCH_HEAD"], "", install_log)
        head = _run("INSTALL", ["git", "-C", app_dir, "log", "-1", "--format=%H %cI"], "", install_log).stdout.strip()
        log("INSTALL", "WanGP source", commit=head)
        # 2) uv + Python 3.11 venv (이미지에 3.11 이 없으면 uv 가 받아 옴)
        _run("INSTALL", [sys.executable, "-m", "pip", "install", "-q", "uv"], "Internet=On 확인", install_log)
        uv = [sys.executable, "-m", "uv"]
        if not os.path.exists(py):
            _run("INSTALL", uv + ["venv", "--seed", "--python", "3.11", venv], "Internet/디스크 확인", install_log)
        # 3) 드라이버에 맞는 torch → requirements 가 다른 CUDA 빌드로 바꾸지 못하게 고정
        _run("INSTALL", uv + ["pip", "install", "--python", py, *build["pkgs"], "--index-url", build["index"]],
             "드라이버가 cu130 에 비해 오래됐으면 wangp_torch_build='cu128'", install_log)
        constraints = os.path.join(cfg.work_dir, "torch-constraints.txt")
        with open(constraints, "w") as f:
            f.write("\n".join(build["pkgs"]) + "\n")
        # 4) WanGP requirements (uv 가 빠름, 충돌 시 pip — pip 는 약한 충돌을 넘어감)
        r = _run("INSTALL", uv + ["pip", "install", "--python", py, "-r", "requirements.txt", "-c", constraints,
                                  "--index-strategy", "unsafe-best-match"], "pip 로 다시", install_log,
                 cwd=app_dir, check=False)
        if r.returncode != 0:
            _run("INSTALL", [py, "-m", "pip", "install", "-q", "-r", "requirements.txt", "-c", constraints],
                 "install 로그에서 충돌 패키지 확인", install_log, cwd=app_dir)
        # 5) T4(Turing) 용 SageAttention 1.0.6 + Triton 3.2 (WanGP 의 RTX 20XX 조합) → GPU 자가 테스트, 실패면 SDPA
        attention = cfg.wangp_attention
        if attention == "sage":
            r = _run("INSTALL", [py, "-m", "pip", "install", "-q", "triton>=3.2,<3.3", "sageattention==1.0.6"],
                     "SDPA 로 대신", install_log, check=False)
            test = ("import torch; from sageattention import sageattn; "
                    "q = torch.randn(1, 8, 256, 64, device='cuda', dtype=torch.float16); "
                    "o = sageattn(q, q, q); assert torch.isfinite(o).all(); print('sage-ok')")
            t = _run("INSTALL", [py, "-c", test], "SDPA 로 대신", install_log, check=False) if r.returncode == 0 else r
            if t.returncode != 0 or "sage-ok" not in t.stdout:
                log("INSTALL", "SageAttention self-test failed -> attention switched", logging.WARNING,
                    before="sage", after="sdpa")
                attention = "sdpa"
        # 6) venv 의 torch 가 GPU 를 보는지
        probe = ("import json, torch; print(json.dumps(dict(torch=torch.__version__, cuda=torch.version.cuda, "
                 "gpu=torch.cuda.is_available())))")
        info = json.loads(_run("INSTALL", [py, "-c", probe], "wangp_torch_build='cu128' 로 다시", install_log)
                          .stdout.strip().splitlines()[-1])
        if not info["gpu"]:
            raise RuntimeError(f"venv 의 torch 가 GPU 를 못 봄 ({info}) → wangp_torch_build='cu128' 로 다시")
        with open(marker, "w") as f:
            json.dump(dict(want, attention=attention, commit=head, **info), f)
        log("INSTALL", "ready", attention=attention, **info)
    return app_dir, py, attention


def wangp_settings(cfg: Config, params: dict, app_dir: str) -> dict:
    """WanGP 설정 JSON. 빠진 키는 WanGP 가 모델 기본값으로 채운다(clean_settings).
    순서: 기본 → 가속 프로필(Lightning 등) → 사용자가 직접 적은 steps/guidance → wangp_extra."""
    spec = MODELS[cfg.model]
    s = dict(model_type=spec["model_type"], prompt=cfg.prompt, negative_prompt=cfg.negative_prompt,
             resolution=f"{params['width']}x{params['height']}", video_length=params["num_frames"], seed=cfg.seed)
    if spec.get("profile"):
        prof_path = os.path.join(app_dir, "profiles", spec["profile"])
        if not os.path.exists(prof_path):
            raise FileNotFoundError(f"WanGP 가속 프로필이 없음: {prof_path} (wangp_ref 를 바꿨다면 프로필 이름 확인)")
        with open(prof_path, encoding="utf-8") as f:
            s.update(json.load(f))
    if "steps" in params["explicit"]:
        s["num_inference_steps"] = params["steps"]
    if "guidance_scale" in params["explicit"]:
        s["guidance_scale"] = params["guidance_scale"]
    if cfg.fps:
        s["force_fps"] = str(cfg.fps)
    s.update(cfg.wangp_extra)
    return s


_PROGRESS_RE = re.compile(r"\d+%\||it/s|s/it|steps/s|s/step")
_IMPORTANT_RE = re.compile(r"error|exception|traceback|warning|saved|task|loaded|download|valid|frames|steps",
                           re.IGNORECASE)


def _stream(cmd: list, cwd: str, log_file: str, stage: str, every: float = 30.0) -> int:
    """하위 프로세스 출력을 전부 log_file 에, 화면에는 중요한 줄 + 진행 줄은 every 초마다 하나."""
    last = 0.0
    with open(log_file, "a", encoding="utf-8") as lf:
        lf.write(f"\n$ {' '.join(map(str, cmd))}\n")
        proc = subprocess.Popen(list(map(str, cmd)), cwd=cwd, env=_child_env(), stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT, text=True, bufsize=1)
        for line in proc.stdout:
            lf.write(line)
            line = line.strip()
            if not line:
                continue
            if _PROGRESS_RE.search(line):
                if time.perf_counter() - last >= every:
                    log(stage, "progress", line=line[-160:])
                    last = time.perf_counter()
            elif _IMPORTANT_RE.search(line):
                log(stage, "wgp", line=line[:240])
        return proc.wait()


def _wangp_generate(cfg: Config, run_dir: str, run_id: str, timings: dict) -> dict:
    install_log = os.path.join(run_dir, "wangp_install.log")
    wgp_log = os.path.join(run_dir, "wangp_process.log")
    with _Stage("SETUP", timings, "Accelerator = GPU T4 x2"):
        gpus = _nvidia_smi()
        for g in gpus:
            log("SETUP", "gpu", **g)
        params = resolve_params(cfg)  # 모양 맞추기는 WanGP 가 모델 블록 크기에 맞춰 한다
        log("SETUP", "generation params", preset=cfg.preset, resolution=f"{params['width']}x{params['height']}",
            num_frames=params["num_frames"], explicit=",".join(params["explicit"]) or "none",
            note="steps/guidance from the WanGP model or accelerator profile unless explicit")
    app_dir, py, attention = _wangp_install(cfg, timings, install_log)

    with _Stage("GENERATE", timings, "wangp_process.log 끝부분 확인 · RAM 부족이면 wangp_profile='5'"):
        settings = wangp_settings(cfg, params, app_dir)
        settings_path = os.path.join(run_dir, "wangp_settings.json")
        with open(settings_path, "w", encoding="utf-8") as f:
            json.dump(settings, f, ensure_ascii=False, indent=2)
        shown = {k: (v if not isinstance(v, str) or len(v) < 80 else v[:77] + "...") for k, v in settings.items()}
        log("GENERATE", "settings", **{k: json.dumps(v, ensure_ascii=False) if isinstance(v, (list, dict)) else v
                                      for k, v in shown.items() if k not in ("prompt", "negative_prompt")})
        media_dir = os.path.join(run_dir, "media")
        os.makedirs(media_dir, exist_ok=True)
        base = [py, "wgp.py", "--process", settings_path, "--output-dir", media_dir,
                "--profile", cfg.wangp_profile, "--attention", attention, "--gpu", cfg.wangp_gpu]
        if cfg.wangp_dry_run_first:
            rc = _stream(base + ["--dry-run"], app_dir, wgp_log, "GENERATE")
            if rc != 0:
                raise RuntimeError(f"WanGP 설정 검증 실패 (rc={rc}) — {wgp_log}")
            log("GENERATE", "dry-run ok (settings valid)")
        before = set(os.listdir(media_dir))
        t0 = time.perf_counter()
        rc = _stream(base, app_dir, wgp_log, "GENERATE")
        if rc != 0:
            tail = open(wgp_log, encoding="utf-8", errors="replace").read().strip().splitlines()[-8:]
            for line in tail:
                log("GENERATE", "  | " + line[:300], logging.ERROR)
            raise RuntimeError(f"WanGP 생성 실패 (rc={rc}) — 전체 로그: {wgp_log}")
        new = sorted(os.path.join(media_dir, n) for n in set(os.listdir(media_dir)) - before
                     if os.path.splitext(n)[1].lower() in MEDIA_EXT)
        if not new:
            raise RuntimeError(f"WanGP 가 0 으로 끝났지만 새 결과 파일이 없음 — {wgp_log}")
        for p in new:
            log("GENERATE", "saved", file=p, size_mb=round(os.path.getsize(p) / 1e6, 2))
        log("GENERATE", "wall time", sec=round(time.perf_counter() - t0, 1))
    return dict(videos=new, params=params, settings_file=settings_path, wangp_log=wgp_log, gpus=gpus,
                attention=attention, wangp_ref=cfg.wangp_ref)


# --------------------------------------------------------------------------------------------------
# 진입점
# --------------------------------------------------------------------------------------------------
def run(settings: dict | Config | None = None, **overrides) -> dict:
    """설정 dict 하나로 영상 생성. 반환: {'videos': [...], 'metadata': ..., 'log': ..., 'timings': {...}}"""
    cfg = make_config(settings, **overrides)
    spec = MODELS[cfg.model]
    run_id = time.strftime("%Y%m%d-%H%M%S")
    run_dir = os.path.join(cfg.output_dir, run_id)
    os.makedirs(run_dir, exist_ok=True)
    os.makedirs(cfg.work_dir, exist_ok=True)
    os.environ.setdefault("PYTORCH_CUDA_ALLOC_CONF", "expandable_segments:True")
    log_file = os.path.join(run_dir, "run.log")
    _setup_logging(cfg.log_level, log_file)
    timings: dict[str, float] = {}
    code_sha = _sha256(os.path.abspath(__file__))
    ram_total, ram_avail = _ram_gb()
    log("CONFIG", "videogen", version=__version__, code_sha256=code_sha[:12], model=cfg.model,
        backend=spec["backend"], license=spec["license"], run_dir=run_dir)
    log("CONFIG", "prompt", text=cfg.prompt[:200] + ("..." if len(cfg.prompt) > 200 else ""))
    log("CONFIG", "machine", python=platform.python_version(), ram_total_gb=ram_total, ram_avail_gb=ram_avail,
        disk_free_work_gb=_free_disk_gb(cfg.work_dir), disk_free_output_gb=_free_disk_gb(cfg.output_dir),
        run_type=os.environ.get("KAGGLE_KERNEL_RUN_TYPE", "local"))

    if spec["backend"] == "diffusers":
        if cfg.install_deps and "KAGGLE_KERNEL_RUN_TYPE" in os.environ:
            _ensure_packages(DIFFUSERS_PACKAGES)
        result = _diffusers_generate(cfg, run_dir, run_id, timings)
    else:
        result = _wangp_generate(cfg, run_dir, run_id, timings)

    meta_path = os.path.join(run_dir, f"videogen_{run_id}.json")
    meta = dict(videogen_version=__version__, code_sha256=code_sha, run_id=run_id, config=asdict(cfg),
                backend=spec["backend"], timings_sec=timings, python=platform.python_version(), **result)
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2, default=str)
    log("SUMMARY", "stage timings (sec)", **timings, total=round(sum(timings.values()), 1))
    log("SUMMARY", "outputs", videos=len(result["videos"]), metadata=meta_path, log=log_file)
    if cfg.preview:
        _preview(result["videos"])
    return dict(videos=result["videos"], metadata=meta_path, log=log_file, timings=timings, run_dir=run_dir)


def _preview(paths: list[str], max_mb: float = 40.0):
    try:
        from IPython import get_ipython
        from IPython.display import Video, display
        if get_ipython() is None:
            return
        for p in paths:
            if p.lower().endswith((".mp4", ".webm")) and os.path.getsize(p) < max_mb * 1e6:
                display(Video(p, embed=True, width=640))
    except Exception as e:  # 미리보기는 부가 기능 — 실패해도 결과에는 영향 없음
        log("SUMMARY", "preview skipped", logging.DEBUG, reason=repr(e)[:200])


def _cli(argv=None):
    ap = argparse.ArgumentParser(description="오픈소스 영상 생성 (Kaggle T4 x2) — videogen " + __version__)
    ap.add_argument("--settings", help="설정 JSON 파일 (Config 키)")
    ap.add_argument("--model", choices=list(MODELS))
    ap.add_argument("--prompt")
    ap.add_argument("--preset", choices=list(PRESETS))
    ap.add_argument("--seed", type=int)
    ap.add_argument("--output-dir", dest="output_dir")
    a = ap.parse_args(argv)
    settings = json.load(open(a.settings, encoding="utf-8")) if a.settings else {}
    settings.update({k: v for k, v in vars(a).items() if k != "settings" and v is not None})
    settings.setdefault("preview", False)
    result = run(settings)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    _cli()
