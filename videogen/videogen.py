#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.4.0 — 2026-10-19 — 사용자 지시 "롱폼,숏폼 둘다 아까 짧게 짧게 시작이미지로 영상 만들었던 코드로 만들거니까
#          그 코드 수정필요하면 수정하고 영상을 이어 붙이는건 그 코드에서 하는게 아니라 너가 하는거야": 영상 한 편의 장면
#          클립 수십 개를 한 번에 만들고 Claude 가 받아 이어 붙이게 — start_images 항목마다 길이(sec)·이름(name),
#          상대 경로 이미지는 image_base 앞에 붙여 받음, 결과 clips/<이름>.mp4 + clips_manifest.json,
#          release_tag 를 주면 GitHub Release 에 올림(Kaggle Secret GITHUB_TOKEN · 같은 이름은 바꿔 올림 · 목록은 합침 ·
#          실패는 경고만 — Output 탭에는 그대로)
# 이전 v1.3.1 — 2026-10-19 — 사용자 보고 "RuntimeError: 업스케일 결과 크기 None != 1080x1920": Kaggle 커널 로캘이 UTF-8 이
#          아니면 ffmpeg 출력 속 영상 메타데이터(WanGP 가 넣은 중국어 부정 프롬프트)를 읽다 UnicodeDecodeError → 크기 None.
#          하위 프로세스 출력을 UTF-8(대체)로 읽고 WanGP 도 UTF-8 로 찍게(PYTHONUTF8) · ffprobe(JSON) 먼저 · 결과 파일 메타데이터
#          제거 · 크기를 못 읽으면 경고만(다르면 멈춤) · 생성 없이 다시 키우는 upscale_file() · 같은 원인으로 이어 붙이기가
#          클립 fps 를 못 읽어 몰래 16fps(5B 클립은 24fps → 프레임 1/3 버림)로 하던 것을 모델 fps·경고로, upscale_file 은
#          fps 가 틀린 이어 붙인 파일을 media/ 클립들로 다시 이어 붙임
# 이전 v1.3.0 — 2026-10-18 — 사용자 지시 "3개 영상 나왔는데 2시간 걸렸어 너무 오래걸리는데 빠르게 생성하는 방법 없어?
#          시작 이미지를 전달하면 더 빨리 할 수 있어? 시작 이미지 여러개 만들어서 짧게 짧게 각각 만드는거지": 시작 이미지
#          여러 장 → 장마다 짧은 클립을 WanGP 한 번 실행에 연달아(모델 한 번만 불러옴) → 이어 붙임 → 업스케일
#          (start_images · clip_sec · concat). 새 모델 wan2.2-5b-fast(TI2V 5B FastWan 3-step) · wan2.2-14b-i2v(I2V 14B
#          Lightning 4-step). 업스케일은 비율 차이 3% 이하면 키운 뒤 가운데 자르기(cover) 허용 (5B 1280x704 → 1920x1080)
# 이전 v1.2.1 — 2026-10-18 — 사용자 보고(wangp_process.log) "해결해 에러 났어": WanGP 가 T2V 모델의 창 이어붙이기를
#          거부 ("You have requested to Generate Sliding Windows with a Text to Video model ... a t2v model doesn't see past
#          frames"). wan2.2-14b-hq 를 두 단계로: T2V 14B 로 첫 81프레임(5초) → SVI 2 Pro(I2V 14B, 영상 이어 만들기 'V')로
#          나머지 160프레임 (wangp_plan · wangp_continue_settings). 오류 메시지에 WanGP 의 [ERROR] 줄을 바로 보여 줌
# 이전 v1.2.0 — 2026-10-18 — 사용자 지시 "좀 고품질의 1920, 1080 해상도로 할아버지가 소파에 앉아서 호통치는 영상으로
#          15초 정도로 생성하는 설정, 프롬프트로 변경해줘": T4 에서 1080p·15초를 한 번에 만들 수 없어(학습 길이 약 5초 ·
#          계산량) 새 모델 wan2.2-14b-hq(Lightning 8-step 3-phase + 81프레임 sliding window)로 1280x720 15초를 만든 뒤
#          ×1.5 업스케일(FlashVSR, 실패하면 ffmpeg Lanczos)로 1920x1080 — 새 프리셋 fhd_15s, 새 설정 duration_sec·upscale_to·upscaler
# 이전 v1.1.1 — 2026-10-18 — 사용자 보고 "RuntimeError: Failed to import diffusers.models.autoencoders.autoencoder_kl_wan
#          ... cannot import name 'FqnToConfig' from 'torchao.quantization' 해결해": Kaggle 에 미리 깔린 오래된 torchao(<0.15)
#          때문에 diffusers 0.41.0 모델 import 가 깨지던 것 고침 — _disable_old_torchao() (videogen 은 torchao 를 쓰지 않음)
# 이전 v1.1.0 — 2026-10-18 — 사용자 지시 "핵심 코드를 하나로 만들어서 저장소에 올리고 kaggle에서는 코드 받아서 실행하는
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
    wan2.2-14b-hq         WanGP 로 두 단계: T2V 14B + Lightning 8-step 3-phase(첫 5초) → SVI 2 Pro I2V 14B 로 나머지를 이어 만들기
    wan2.2-5b-fast        WanGP 로 TI2V 5B + FastWan 3-step — 빠름. 시작 이미지(start_images)·텍스트만 둘 다
    wan2.2-14b-i2v        WanGP 로 I2V 14B + Lightning i2v 4-step — 시작 이미지 필요, 클립 품질 우선
    ltx2.5-distilled      WanGP 로 LTX-2.5 Distilled 22B, 영상+오디오 (LTX-2 Community License — 연매출 1천만 달러 이상 유료)

결과: <output_dir>/<run_id>/ 에 영상 + videogen_<run_id>.json(설정·버전·시간·코드 sha256) + run.log
      시작 이미지 길: clips/<이름>.mp4 + clips/clips_manifest.json (release_tag 면 GitHub Release 에도 — v1.4.0)
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

__version__ = "1.4.0"

# --------------------------------------------------------------------------------------------------
# 모델 · 프리셋
# --------------------------------------------------------------------------------------------------
MODELS = {
    "wan2.2-5b": dict(backend="diffusers", repo="Wan-AI/Wan2.2-TI2V-5B-Diffusers", license="Apache-2.0"),
    "wan2.2-14b-lightning": dict(backend="wangp", model_type="t2v_2_2", license="Apache-2.0", block=16,
                                 profile="wan_2_2/Lightning t2v v2025-09-28 2 Phases - 4 Steps.json"),
    # 8-step 3-phase 프로필 설명(WanGP): "insert a CFG phase before the 2 accelerated phases ... reduce the slow motion
    # effect of these Loras Accelerators". T2V 는 앞 창을 보지 못해 WanGP 가 창 이어붙이기를 막으므로 (v1.2.0 Kaggle 오류)
    # 처음 81프레임(16fps 5초)만 T2V 로 만들고, 나머지는 SVI 2 Pro(Wan2.2 I2V 14B + Stable Video Infinity LoRA —
    # "potentially unlimited Videos to Continue")가 그 영상을 이어 만든다. Lightning i2v 는 SVI LoRA 와 같은 2-phase 4-step.
    "wan2.2-14b-hq": dict(backend="wangp", model_type="t2v_2_2", license="Apache-2.0", fps=16, block=16, first_frames=81,
                          profile="wan_2_2/Lightning t2v v2025-12-17 3 Phases - 8 Steps.json",
                          continue_with=dict(model_type="i2v_2_2_svi2pro",
                                             profile="wan_2_2/Lightning i2v v2025-10-14 2 Phases - 4 Steps.json"),
                          disk_gb=80),  # 추정: T2V·I2V 14B int8 두 벌 + 텍스트 인코더·VAE·LoRA + venv
    # 빠름: Wan2.2 TI2V 5B + FastWan(3-step 증류 LoRA, CFG 없음 — WanGP 프리셋 ti2v_2_2_fastwan). 시작 이미지·텍스트만 둘 다 됨.
    # 5B 는 T2V 로 분류되지 않아(WanGP test_class_t2v) 텍스트만으로 긴 영상도 창 이어붙이기(창 121)가 허용된다. 해상도 32 배수.
    "wan2.2-5b-fast": dict(backend="wangp", model_type="ti2v_2_2_fastwan", fps=24, block=32, clip_frames=121,
                           license="Apache-2.0 (Wan2.2) — FastWan LoRA 는 원문 라이선스 확인", disk_gb=30),
    # 품질: Wan2.2 I2V 14B + Lightning i2v 2-phase 4-step. 시작 이미지가 꼭 있어야 한다 (start_images).
    "wan2.2-14b-i2v": dict(backend="wangp", model_type="i2v_2_2", fps=16, block=16, clip_frames=81, needs_image=True,
                           profile="wan_2_2/Lightning i2v v2025-10-14 2 Phases - 4 Steps.json",
                           license="Apache-2.0", disk_gb=50),
    "ltx2.5-distilled": dict(backend="wangp", model_type="ltx2_25_22B_distilled", profile=None,
                             license="LTX-2 Community License (revenue >= USD 10M needs a paid license)"),
}

# steps/guidance_scale 는 diffusers 에만 쓴다. WanGP 는 모델 기본값(Lightning 이면 4 step)을 쓰고,
# 사용자가 steps/guidance_scale 을 직접 적었을 때만 넘긴다.
# duration_sec 이 있으면 num_frames 대신 길이로 (WanGP 는 모델 fps 로 프레임 수를 고름), upscale_to 는 생성 뒤 최종 해상도.
PRESETS = {
    "t4_fast":       dict(height=480, width=832,  num_frames=81,  steps=30, guidance_scale=5.0),
    "t4_balanced":   dict(height=704, width=1280, num_frames=49,  steps=40, guidance_scale=5.0),
    "official_720p": dict(height=704, width=1280, num_frames=121, steps=50, guidance_scale=5.0),
    # 1280x720 으로 15초 생성 → ×1.5 = 1920x1080. WanGP 모델(wan2.2-14b-hq 권장)용 — diffusers 5B 는 121프레임까지만
    "fhd_15s":       dict(height=720, width=1280, num_frames=None, duration_sec=15, upscale_to="1920x1080",
                          steps=50, guidance_scale=5.0),
}
UPSCALE_FACTORS = (1.5, 2.0, 2.5, 3.0, 3.5, 4.0)  # FlashVSR·Lanczos 가 둘 다 지원하는 배율 (WanGP @ wangp_ref)
UPSCALE_ASPECT_TOL = 0.03                          # 생성·목표 비율 차이가 이 이하면 키운 뒤 가운데를 잘라 맞춤(cover)
DIFFUSERS_MAX_FRAMES = 121                        # Wan2.2-TI2V-5B 모델 카드 기본값 (24fps 5초) — 넘으면 학습 밖

# Wan 공식 부정 프롬프트 (Wan2.x 예제에 실린 중국어 원문)
WAN_NEGATIVE_PROMPT = (
    "色调艳丽，过曝，静态，细节模糊不清，字幕，风格，作品，画作，画面，静止，整体发灰，最差质量，低质量，JPEG压缩残留，"
    "丑陋的，残缺的，多余的手指，画得不好的手部，画得不好的脸部，畸形的，毁容的，形态畸形的肢体，手指融合，"
    "静止不动的画面，杂乱的背景，三条腿，背景人很多，倒着走"
)

# diffusers 길에서 Kaggle 커널에 맞춰 둘 패키지 (오프라인 스모크 테스트에 쓴 버전). torch 는 Kaggle 것을 그대로 쓴다.
DIFFUSERS_PACKAGES = {"diffusers": "==0.41.0", "transformers": "==5.20.1", "accelerate": ">=1.10",
                      "ftfy": "", "sentencepiece": "", "imageio": ">=2.34", "imageio-ffmpeg": ""}
# diffusers 0.41.0 은 torchao 가 깔려 있기만 하면 `torchao.quantization.FqnToConfig` 를 import 한다 (extra 요구 torchao>=0.15.0)
TORCHAO_MIN = (0, 15)

WANGP_REPO = "https://github.com/deepbeepmeep/Wan2GP.git"
# WanGP 가 문서화한 torch 빌드 (setup_config.json @ wangp_ref). CUDA 13 휠은 드라이버 580 이상이 필요하다.
TORCH_BUILDS = {
    "cu130": dict(pkgs=["torch==2.10.0", "torchvision==0.25.0", "torchaudio==2.10.0"],
                  index="https://download.pytorch.org/whl/cu130", min_driver=580),
    "cu128": dict(pkgs=["torch==2.7.1", "torchvision==0.22.1", "torchaudio==2.7.1"],
                  index="https://download.pytorch.org/whl/cu128", min_driver=525),
}
MEDIA_EXT = {".mp4", ".webm", ".mkv", ".gif", ".png", ".jpg", ".jpeg", ".webp", ".wav", ".mp3", ".flac"}
# v1.4.0 장면 클립: 시작 이미지 항목 키 · 이름(파일 이름이 됨) · GitHub Release
START_IMAGE_KEYS = {"image", "prompt", "sec", "name"}
CLIP_NAME_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,63}")
RELEASE_TAG_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,99}")
REPO_RE = re.compile(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+")
MANIFEST_NAME = "clips_manifest.json"
GITHUB_API = "https://api.github.com"
GITHUB_UPLOADS = "https://uploads.github.com"


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
    duration_sec: float | None = None            # 길이(초) — 주면 num_frames 대신 (WanGP: 모델 fps 로 가장 가까운 프레임 수)
    upscale_to: str | None = None                # 최종 해상도 "1920x1080" — 생성 해상도의 1.5·2·…배(가로세로 같은 배율)
    upscaler: str = "flashvsr"                   # flashvsr(학습형 복원, WanGP) | lanczos(단순 확대, ffmpeg). flashvsr 실패 → lanczos
    # ---- 시작 이미지 (WanGP 모델) — 장마다 짧은 클립 하나, WanGP 한 번 실행에 연달아 (모델을 한 번만 불러옴) ----
    # 경로·URL, 또는 {"image": 경로·URL, "prompt": 이 클립만의 프롬프트, "sec": 이 클립 길이(초), "name": 결과 이름}
    start_images: list = field(default_factory=list)
    image_base: str | None = None                # 상대 경로 image 앞에 붙일 주소·폴더 (v1.4.0 — 예: raw.githubusercontent.com/<저장소>/<커밋>/)
    clip_sec: float | None = None                # 클립 하나 길이(초). 우선순위: 항목 sec > clip_sec > duration_sec ÷ 이미지 수 > 모델 기본(약 5초)
    concat: bool = True                          # 클립들을 순서대로 이어 한 영상으로 (컷 전환). 장면 클립을 따로 받을 땐 False
    # ---- 클립 보내기 (v1.4.0) — Claude 가 받아 영상에 이어 붙임. 실패해도 Output 탭에는 그대로 남음 ----
    release_tag: str | None = None               # 예: "clips-<영상ID>" — 이 태그의 GitHub Release 에 clips/ 를 올림. None: 안 올림
    release_repo: str = "yeomin1024/yeomin1024-ytb"  # 토큰 = Kaggle Secret GITHUB_TOKEN (contents 쓰기 권한)
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
    if cfg.upscaler not in ("flashvsr", "lanczos"):
        raise ValueError(f"upscaler={cfg.upscaler!r} 없음: 'flashvsr' | 'lanczos'")
    if cfg.duration_sec is not None and cfg.duration_sec <= 0:
        raise ValueError(f"duration_sec={cfg.duration_sec} 은 0보다 커야 한다")
    if cfg.upscale_to is not None:
        _parse_size(cfg.upscale_to)
    spec = MODELS[cfg.model]
    if spec.get("needs_image") and not cfg.start_images:
        raise ValueError(f"model={cfg.model!r} 는 시작 이미지가 필요하다 — start_images=[...] 를 넣거나 'wan2.2-5b-fast'")
    if cfg.start_images and spec["backend"] != "wangp":
        raise ValueError(f"start_images 는 WanGP 모델에서만: {[m for m, v in MODELS.items() if v['backend'] == 'wangp']}")
    names = []
    for i, item in enumerate(cfg.start_images):
        if not (isinstance(item, str) and item.strip()) and not (isinstance(item, dict) and item.get("image")):
            raise ValueError(f"start_images[{i}] 는 경로·URL 문자열이나 {{'image': ..., 'prompt': ...}} 이어야 한다: {item!r}")
        if not isinstance(item, dict):
            continue
        extra = sorted(set(item) - START_IMAGE_KEYS)
        if extra:
            raise ValueError(f"start_images[{i}] 의 알 수 없는 키 {extra}. 쓸 수 있는 키: {sorted(START_IMAGE_KEYS)}")
        sec = item.get("sec")
        if sec is not None and (isinstance(sec, bool) or not isinstance(sec, (int, float)) or sec <= 0):
            raise ValueError(f"start_images[{i}].sec={sec!r} 은 0보다 큰 숫자(초)여야 한다")
        if item.get("name") is not None:
            if not CLIP_NAME_RE.fullmatch(str(item["name"])):
                raise ValueError(f"start_images[{i}].name={item['name']!r} — 영문·숫자·_-. 로 64자까지 (파일 이름이 됨)")
            names.append(str(item["name"]))
    dup = sorted({n for n in names if names.count(n) > 1})
    if dup:
        raise ValueError(f"start_images 의 name 이 겹친다: {dup} (같은 이름이면 결과 파일이 덮어써짐)")
    if cfg.clip_sec is not None and cfg.clip_sec <= 0:
        raise ValueError(f"clip_sec={cfg.clip_sec} 은 0보다 커야 한다")
    if cfg.release_tag is not None:
        if not cfg.start_images:
            raise ValueError("release_tag 는 시작 이미지 길(start_images)의 clips/ 를 올린다 — start_images 가 비어 있음")
        if not RELEASE_TAG_RE.fullmatch(cfg.release_tag):
            raise ValueError(f"release_tag={cfg.release_tag!r} — 영문·숫자·_-. 로 100자까지 (예: 'clips-<영상ID>')")
    if not REPO_RE.fullmatch(cfg.release_repo):
        raise ValueError(f"release_repo={cfg.release_repo!r} 는 '소유자/저장소' 꼴이어야 한다")
    return cfg


def _parse_size(text: str) -> tuple[int, int]:
    """'1920x1080' → (1920, 1080)"""
    m = re.fullmatch(r"\s*(\d{2,5})\s*[xX×]\s*(\d{2,5})\s*", str(text))
    if not m:
        raise ValueError(f"해상도 {text!r} 는 '1920x1080' 꼴이어야 한다")
    return int(m.group(1)), int(m.group(2))


def upscale_plan(width: int, height: int, target: str) -> dict:
    """생성 해상도 → 최종 해상도 계획 {'factor', 'fit', 'crop_pct'}.
    exact: 가로세로 같은 지원 배율 (1280x720 → ×1.5 = 1920x1080).
    cover: 비율 차이가 3% 이하면 목표를 덮는 가장 작은 지원 배율로 키운 뒤 가운데를 잘라 맞춘다
           (5B 는 32 배수라 1280x704 → ×2 → 줄여서 1964x1080 → 가운데 1920x1080, 가로 약 2% 잘림).
    비율이 그보다 다르면 많이 잘리므로 멈추고 맞는 생성 해상도를 알려 준다."""
    tw, th = _parse_size(target)
    fw, fh = tw / width, th / height
    if abs(fw - fh) < 1e-6 and round(fw, 6) in UPSCALE_FACTORS:
        return dict(factor=round(fw, 6), fit="exact", crop_pct=0.0)
    aspect_diff = abs((width / height) / (tw / th) - 1)
    factor = next((f for f in UPSCALE_FACTORS if f >= max(fw, fh) - 1e-9), None)
    if aspect_diff <= UPSCALE_ASPECT_TOL and factor is not None:
        return dict(factor=factor, fit="cover", crop_pct=round(aspect_diff * 100, 2))
    hint = ", ".join(f"{round(tw / f)}x{round(th / f)}(×{f:g})" for f in UPSCALE_FACTORS
                     if abs(tw / f - round(tw / f)) < 1e-6 and abs(th / f - round(th / f)) < 1e-6)
    raise ValueError(f"{width}x{height} → {target}: 비율 차이 {aspect_diff * 100:.1f}% (허용 {UPSCALE_ASPECT_TOL * 100:g}%) "
                     f"또는 배율 {max(fw, fh):.3g} 이 지원 배율 {UPSCALE_FACTORS} 밖. 이 목표에 맞는 생성 해상도: {hint or '없음'}")


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
                              "--format=csv,noheader"], capture_output=True, encoding="utf-8", errors="replace", timeout=30).stdout
    except (OSError, subprocess.TimeoutExpired):
        return []
    keys = ["idx", "name", "driver", "vram", "cc"]
    return [dict(zip(keys, [c.strip() for c in row.split(",")])) for row in out.strip().splitlines() if row.strip()]


_PARAM_KEYS = ("height", "width", "num_frames", "steps", "guidance_scale", "duration_sec", "upscale_to")


def resolve_params(cfg: Config, spatial_multiple: int | None = None, temporal_factor: int | None = None,
                   fps: int | None = None) -> dict:
    """프리셋 + 직접 적은 값 → 실제 생성 값. 모양 규칙(배수·4k+1)을 맞출 때는 전·후 값을 경고로 남긴다.
    길이 우선순위: 직접 적은 duration_sec > 직접 적은 num_frames > 프리셋 duration_sec > 프리셋 num_frames.
    fps 를 주면(diffusers) 길이를 프레임 수로 바꾸고, 안 주면(WanGP) duration_sec 을 그대로 둬 WanGP 가 모델 fps 로 바꾼다."""
    preset = PRESETS[cfg.preset]
    p = {k: preset.get(k) for k in _PARAM_KEYS}
    explicit = {k for k in _PARAM_KEYS if getattr(cfg, k) is not None}
    for k in explicit:
        p[k] = getattr(cfg, k)
    if "num_frames" in explicit and "duration_sec" not in explicit:
        p["duration_sec"] = None  # 직접 적은 프레임 수가 프리셋 길이보다 우선
    p["explicit"] = sorted(explicit)
    if spatial_multiple:
        for k in ("height", "width"):
            fixed = max(spatial_multiple, p[k] // spatial_multiple * spatial_multiple)
            if fixed != p[k]:
                log("DATA", f"{k} is not a multiple of {spatial_multiple}; adjusted", logging.WARNING,
                    before=p[k], after=fixed)
                p[k] = fixed
    if p["duration_sec"] is not None and fps:
        p["num_frames"] = max(1, round(p["duration_sec"] * fps))
        log("DATA", "num_frames from duration", duration_sec=p["duration_sec"], fps=fps, num_frames=p["num_frames"])
    if p["num_frames"] is None and p["duration_sec"] is None:
        raise ValueError("num_frames 나 duration_sec 중 하나는 있어야 한다")
    if temporal_factor and p["num_frames"] is not None and p["num_frames"] % temporal_factor != 1:
        fixed = max(1, p["num_frames"] // temporal_factor * temporal_factor + 1)
        log("DATA", f"num_frames must be {temporal_factor}k+1; adjusted", logging.WARNING,
            before=p["num_frames"], after=fixed)
        p["num_frames"] = fixed
    up = upscale_plan(p["width"], p["height"], p["upscale_to"]) if p["upscale_to"] else {}
    p["upscale_factor"], p["upscale_fit"], p["upscale_crop_pct"] = up.get("factor"), up.get("fit"), up.get("crop_pct")
    if up.get("fit") == "cover":
        log("DATA", "upscale will scale up then center-crop to the target aspect", logging.WARNING,
            generation=f"{p['width']}x{p['height']}", target=p["upscale_to"], factor=up["factor"],
            crop_pct=up["crop_pct"])
    return p


# --------------------------------------------------------------------------------------------------
# 업스케일: FlashVSR(WanGP 후처리 작업) → 실패하면 ffmpeg Lanczos. 생성 원본은 지우지 않는다.
# --------------------------------------------------------------------------------------------------
def _ffmpeg_exe() -> str:
    exe = shutil.which("ffmpeg")
    if exe:
        return exe
    try:
        import imageio_ffmpeg
    except ImportError:
        _ensure_packages({"imageio-ffmpeg": ""})
        import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()


def _ffprobe_exe() -> str | None:
    exe = shutil.which("ffprobe")
    if exe:
        return exe
    sib = os.path.join(os.path.dirname(_ffmpeg_exe()), "ffprobe")
    return sib if os.path.exists(sib) else None


def _video_info(path: str) -> dict:
    """영상 가로·세로·길이·fps. ffprobe(JSON)가 있으면 그것으로, 없으면 ffmpeg 정보 출력에서. 읽지 못한 값은 빠진다.
    출력은 로캘과 상관없이 UTF-8 로 읽는다 — v1.3.0 은 Kaggle 커널 로캘(ASCII)에서 영상 메타데이터의 중국어
    (WanGP 가 넣은 부정 프롬프트)를 읽다가 UnicodeDecodeError → 크기 None → '업스케일 결과 크기 None' 으로 멈췄다."""
    probe = _ffprobe_exe()
    if probe:
        try:
            r = subprocess.run([probe, "-v", "error", "-select_streams", "v:0", "-show_entries",
                                "stream=width,height,avg_frame_rate:format=duration", "-of", "json", path],
                               capture_output=True, encoding="utf-8", errors="replace", timeout=120)
            d = json.loads(r.stdout or "{}")
            st = (d.get("streams") or [{}])[0]
            info = {}
            if st.get("width") and st.get("height"):
                info.update(width=int(st["width"]), height=int(st["height"]))
            if (d.get("format") or {}).get("duration"):
                info["duration_sec"] = round(float(d["format"]["duration"]), 2)
            num, _, den = str(st.get("avg_frame_rate", "")).partition("/")
            if num.isdigit() and den.isdigit() and int(den):
                info["fps"] = round(int(num) / int(den), 3)
            if "width" in info:
                return info
        except Exception as e:  # ffprobe 가 이상하면 ffmpeg 정보 출력으로
            log("UPSCALE", "ffprobe failed, trying ffmpeg", logging.DEBUG, file=path, error=repr(e)[:200])
    try:
        r = subprocess.run([_ffmpeg_exe(), "-hide_banner", "-i", path], capture_output=True, encoding="utf-8",
                           errors="replace", timeout=120)
    except Exception as e:  # ffmpeg 를 못 찾거나 멈춤 — 정보 확인만 못 한 것
        log("UPSCALE", "could not read video info", logging.WARNING, file=path, error=repr(e)[:200])
        return {}
    info = {}
    m = re.search(r"Video:.*?\b(\d{2,5})x(\d{2,5})\b", r.stderr)
    if m:
        info.update(width=int(m.group(1)), height=int(m.group(2)))
    m = re.search(r"Duration:\s*(\d+):(\d+):(\d+(?:\.\d+)?)", r.stderr)
    if m:
        info["duration_sec"] = round(int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3)), 2)
    m = re.search(r"Video:.*?([\d.]+)\s*fps", r.stderr)
    if m:
        info["fps"] = float(m.group(1))
    if "width" not in info:
        log("UPSCALE", "could not parse video size", logging.WARNING, file=path,
            ffmpeg_tail=" | ".join(r.stderr.strip().splitlines()[-4:])[:300])
    return info


def _video_size(path: str) -> tuple[int, int] | None:
    info = _video_info(path)
    return (info["width"], info["height"]) if "width" in info else None


def _ffmpeg_upscale(src: str, dst: str, width: int, height: int, fit: str = "exact"):
    """Lanczos 로 width x height 로. fit='cover' 면 비율을 지켜 덮도록 키운 뒤 가운데를 잘라 맞춘다."""
    vf = f"scale={width}:{height}:flags=lanczos" if fit == "exact" else \
        f"scale={width}:{height}:force_original_aspect_ratio=increase:flags=lanczos,crop={width}:{height}"
    cmd = [_ffmpeg_exe(), "-y", "-hide_banner", "-loglevel", "error", "-i", src, "-map_metadata", "-1",
           "-vf", vf, "-map", "0:v:0", "-map", "0:a?",
           "-c:v", "libx264", "-preset", "slow", "-crf", "16", "-pix_fmt", "yuv420p", "-c:a", "copy", dst]
    r = subprocess.run(cmd, capture_output=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        raise RuntimeError(f"ffmpeg 업스케일 실패: {r.stderr[-800:]}")


def _check_size(path: str, tw: int, th: int):
    """결과 크기 확인: 다르면 멈추고, 읽지 못하면(None) 경고만 — ffmpeg scale 이 크기를 정하므로 '못 읽음'은 실패가 아니다."""
    got = _video_size(path)
    if got is None:
        log("UPSCALE", "output size not verified (could not read it) — ffmpeg scale sets it", logging.WARNING,
            file=path, expected=f"{tw}x{th}")
    elif got != (tw, th):
        raise RuntimeError(f"업스케일 결과 크기 {got[0]}x{got[1]} != {tw}x{th} — {path}")


def upscale_file(path: str, target: str = "1080x1920", upscaler: str = "lanczos", rejoin: bool = True) -> str:
    """이미 만든 영상만 다시 키운다 (생성 없이). path = 영상 파일, 또는 결과 폴더(<output_dir>/<실행시각>) — 폴더면
    이어 붙인 '…<N>clips.mp4', 없으면 media/ 의 가장 최근 영상. FlashVSR 는 WanGP 설치가 필요해 여기서는 Lanczos 만.
    rejoin: 이어 붙인 파일의 fps 가 media/ 클립 N개와 다르면(v1.3.0 이 로캘 문제로 16fps 로 이어 붙인 경우) 클립들로
    다시 이어 붙인 뒤 키운다. Kaggle 예: videogen.upscale_file("/kaggle/working/outputs/20261019-0300", "1080x1920")"""
    if upscaler != "lanczos":
        raise ValueError("upscale_file 은 lanczos 만 (FlashVSR 는 run() 안에서 WanGP 로)")
    src = path
    if os.path.isdir(path):
        if not LOGGER.handlers:
            _setup_logging("INFO", os.path.join(path, "upscale_file.log"))
        joined = sorted((os.path.join(path, n) for n in os.listdir(path) if re.search(r"_\d+clips\.mp4$", n)),
                        key=os.path.getmtime)
        media = os.path.join(path, "media")
        clips = sorted((os.path.join(media, n) for n in os.listdir(media) if n.endswith(".mp4")),
                       key=os.path.getmtime) if os.path.isdir(media) else []
        if not (joined or clips):
            raise FileNotFoundError(f"{path} 에 '…clips.mp4' 도 media/*.mp4 도 없음")
        src = (joined or clips)[-1]
        if joined:
            n = int(re.search(r"_(\d+)clips\.mp4$", src).group(1))
            old_fps, clip_fps = _video_info(src).get("fps"), (_video_info(clips[0]).get("fps") if clips else None)
            log("UPSCALE", "joined file check", file=src, joined_fps=old_fps, clips_in_media=len(clips), expected_clips=n,
                clip_fps=clip_fps)
            if rejoin and len(clips) == n and clip_fps and (not old_fps or abs(old_fps - clip_fps) > 0.01):
                cw, ch = _video_size(clips[0])
                log("CONCAT", "re-joining clips (joined fps differs from clip fps)", logging.WARNING, joined_fps=old_fps,
                    clip_fps=clip_fps, clips=n)
                _ffmpeg_concat(clips, src, cw, ch, fps=clip_fps)
                log("CONCAT", "joined", file=src, clips=n, **_video_info(src))
            elif rejoin and len(clips) != n:
                log("UPSCALE", "media clip count differs; using the joined file as is", logging.WARNING,
                    clips_in_media=len(clips), expected_clips=n)
    if not LOGGER.handlers:
        _setup_logging("INFO", os.path.join(os.path.dirname(os.path.abspath(src)), "upscale_file.log"))
    tw, th = _parse_size(target)
    w, h = _video_size(src) or (None, None)
    if w is None:
        raise RuntimeError(f"원본 크기를 읽지 못함: {src}")
    plan = upscale_plan(w, h, target)
    dst = os.path.join(os.path.dirname(os.path.abspath(src)),
                       f"{os.path.splitext(os.path.basename(src))[0]}_{tw}x{th}_lanczos.mp4")
    log("UPSCALE", "upscale_file", src=src, src_size=f"{w}x{h}", target=target, fit=plan["fit"], crop_pct=plan["crop_pct"])
    _ffmpeg_upscale(src, dst, tw, th, fit=plan["fit"])
    _check_size(dst, tw, th)
    log("UPSCALE", "done", method="lanczos", file=dst, size_mb=round(os.path.getsize(dst) / 1e6, 2), **_video_info(dst))
    return dst


def _upscale_video(cfg: Config, params: dict, src: str, run_dir: str, wangp: tuple | None = None) -> tuple[str, str]:
    """src → upscale_to 해상도 파일. → (경로, 실제 쓴 방법)"""
    tw, th = _parse_size(params["upscale_to"])
    factor, fit = params["upscale_factor"], params.get("upscale_fit") or "exact"
    stem = os.path.splitext(os.path.basename(src))[0]
    log("UPSCALE", "start", src=src, src_size="x".join(map(str, _video_size(src) or ("?", "?"))),
        target=f"{tw}x{th}", factor=factor, fit=fit, upscaler=cfg.upscaler)
    if cfg.upscaler == "flashvsr" and wangp is not None:
        app_dir, py, attention, wgp_log = wangp
        up_dir = os.path.join(run_dir, "upscale_tmp")
        os.makedirs(up_dir, exist_ok=True)
        spath = os.path.join(run_dir, "wangp_upscale.json")
        with open(spath, "w", encoding="utf-8") as f:
            json.dump(dict(mode="edit_postprocessing", video_source=os.path.abspath(src),
                           spatial_upsampling=f"flashvsr*{factor:g}"), f, ensure_ascii=False, indent=2)
        before = set(os.listdir(up_dir))
        rc = _stream([py, "wgp.py", "--process", spath, "--output-dir", up_dir, "--profile", cfg.wangp_profile,
                      "--attention", attention, "--gpu", cfg.wangp_gpu], app_dir, wgp_log, "UPSCALE")
        new = sorted(os.path.join(up_dir, n) for n in set(os.listdir(up_dir)) - before
                     if n.lower().endswith((".mp4", ".webm", ".mkv")))
        got = _video_size(new[0]) if new else None
        if rc == 0 and got and got[0] >= tw and got[1] >= th:  # 목표를 덮으면 성공 (cover 면 아래에서 맞춰 자름)
            dst = os.path.join(run_dir, f"{stem}_{tw}x{th}_flashvsr.mp4")
            if got == (tw, th):
                shutil.move(new[0], dst)
            else:
                _ffmpeg_upscale(new[0], dst, tw, th, fit="cover")
                log("UPSCALE", "FlashVSR output fitted to target (scale + center crop)", flashvsr_size=f"{got[0]}x{got[1]}")
            _check_size(dst, tw, th)
            log("UPSCALE", "done", method="flashvsr", file=dst, size_mb=round(os.path.getsize(dst) / 1e6, 2))
            return dst, "flashvsr"
        log("UPSCALE", "FlashVSR failed -> falling back to Lanczos", logging.WARNING, rc=rc, outputs=len(new),
            got_size=got, expected=f"{tw}x{th}", log=wgp_log)
    elif cfg.upscaler == "flashvsr":
        log("UPSCALE", "FlashVSR runs only through WanGP models; using Lanczos", logging.WARNING)
    dst = os.path.join(run_dir, f"{stem}_{tw}x{th}_lanczos.mp4")
    _ffmpeg_upscale(src, dst, tw, th, fit=fit)
    _check_size(dst, tw, th)
    log("UPSCALE", "done", method="lanczos", file=dst, size_mb=round(os.path.getsize(dst) / 1e6, 2))
    return dst, "lanczos"


def _ffmpeg_concat(clips: list[str], dst: str, width: int, height: int, fps: float | None = None):
    """클립들을 순서대로 한 영상으로 (컷 전환). 크기·fps 를 첫 클립에 맞춰 다시 인코딩한다. 첫 클립 fps 를 못 읽으면
    fps(모델 fps)로, 그것도 없으면 멈춘다 — v1.3.0 은 몰래 16 으로 해서 24fps 클립이 16fps(프레임 1/3 버림)가 됐다."""
    got = _video_info(clips[0]).get("fps")
    if got:
        if fps and abs(got - fps) > 0.01:
            log("CONCAT", "clip fps differs from model fps (using clip fps)", logging.WARNING, clip_fps=got, model_fps=fps)
        fps = got
    elif fps:
        log("CONCAT", "clip fps not readable -> using model fps", logging.WARNING, fps=fps, file=clips[0])
    else:
        raise RuntimeError(f"첫 클립 fps 를 읽지 못함 (모델 fps 도 없음): {clips[0]}")
    log("CONCAT", "encode", clips=len(clips), size=f"{width}x{height}", fps=fps, source="clip" if got else "model")
    chains = "".join(f"[{i}:v]scale={width}:{height}:flags=lanczos,setsar=1,fps={fps:g}[v{i}];" for i in range(len(clips)))
    joins = "".join(f"[v{i}]" for i in range(len(clips)))
    cmd = [_ffmpeg_exe(), "-y", "-hide_banner", "-loglevel", "error"]
    for c in clips:
        cmd += ["-i", c]
    cmd += ["-filter_complex", f"{chains}{joins}concat=n={len(clips)}:v=1:a=0[v]", "-map", "[v]", "-map_metadata", "-1",
            "-c:v", "libx264", "-preset", "slow", "-crf", "16", "-pix_fmt", "yuv420p", dst]
    r = subprocess.run(cmd, capture_output=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        raise RuntimeError(f"ffmpeg 이어 붙이기 실패: {r.stderr[-800:]}")


# --------------------------------------------------------------------------------------------------
# 시작 이미지: URL 이면 받고, 생성 해상도 비율로 가운데를 잘라 그 크기로 (WanGP 는 시작 이미지 비율을 결과 비율로 따름)
# --------------------------------------------------------------------------------------------------
def _fetch(url: str, dst: str):
    import urllib.request
    headers = [{}]
    token = _kaggle_secret("GITHUB_TOKEN") if "githubusercontent.com" in url else None
    if token:
        headers.append({"Authorization": "token " + token})  # 비공개 저장소일 때만 필요 (값은 로그에 남기지 않음)
    err = None
    for attempt, h in enumerate(headers * 2, 1):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=60) as r, open(dst, "wb") as f:
                f.write(r.read())
            return
        except Exception as e:  # 네트워크·권한 오류: 다음 방법으로, 모두 실패하면 멈춤
            err = e
            log("IMAGES", "download attempt failed", logging.WARNING, attempt=attempt, url=url[:120], error=repr(e)[:200])
            time.sleep(2)
    raise RuntimeError(f"시작 이미지 받기 실패: {url} ({err!r}) — 주소·Internet=On 확인")


def _image_source(cfg: Config, src: str) -> str:
    """상대 경로 이미지 → image_base 를 앞에 (URL·절대 경로는 그대로). v1.4.0"""
    if not cfg.image_base or re.match(r"^(https?|file)://", src) or os.path.isabs(src):
        return src
    base = cfg.image_base
    if re.match(r"^(https?|file)://", base):
        return base.rstrip("/") + "/" + src.lstrip("/")
    return os.path.join(base, src)


def prepare_start_images(cfg: Config, params: dict, run_dir: str) -> list[dict]:
    """start_images → [{'path', 'prompt', 'src', 'orig', 'sec', 'name'}]. 가운데를 잘라 생성 해상도(params width x height)에
    정확히 맞춘다. name 이 없으면 clip01, clip02, … (v1.4.0)"""
    from PIL import Image

    out_dir = os.path.join(run_dir, "start_images")
    os.makedirs(out_dir, exist_ok=True)
    tw, th = params["width"], params["height"]
    images = []
    for i, item in enumerate(cfg.start_images, 1):
        item = {"image": item} if isinstance(item, str) else item
        src, prompt = _image_source(cfg, item["image"]), item.get("prompt")
        name, sec = str(item.get("name") or f"clip{i:02d}"), item.get("sec")
        if re.match(r"^(https?|file)://", src):
            local = os.path.join(out_dir, f"{i:02d}_source{os.path.splitext(src.split('?')[0])[1] or '.img'}")
            _fetch(src, local)
        else:
            local = src
            if not os.path.exists(local):
                raise FileNotFoundError(f"start_images[{i - 1}] 파일이 없음: {local} (Kaggle 데이터는 /kaggle/input/... 경로)")
        with Image.open(local) as im:
            im = im.convert("RGB")
            ow, oh = im.size
            scale = max(tw / ow, th / oh)
            nw, nh = max(tw, round(ow * scale)), max(th, round(oh * scale))
            im = im.resize((nw, nh), Image.LANCZOS)
            left, top = (nw - tw) // 2, (nh - th) // 2
            im = im.crop((left, top, left + tw, top + th))
            path = os.path.join(out_dir, f"{i:02d}.png")
            im.save(path)
        cut = round((1 - (tw * th) / (nw * nh)) * 100, 1)
        log("IMAGES", "start image", idx=i, name=name, src=src[-120:], orig=f"{ow}x{oh}", final=f"{tw}x{th}",
            cropped_pct=cut, prompt="own" if prompt else "global", sec=sec if sec is not None else "default")
        if cut > 20:
            log("IMAGES", "more than 20% of the image was cropped to fit the video aspect — the subject may be cut",
                logging.WARNING, idx=i, name=name, cropped_pct=cut)
        images.append(dict(path=path, prompt=prompt or cfg.prompt, src=src, orig=f"{ow}x{oh}", sec=sec, name=name))
    return images


def clip_frames_for(cfg: Config, params: dict, n_images: int) -> int:
    """클립 하나의 프레임 수: clip_sec > duration_sec ÷ 이미지 수 > 모델 기본(약 5초)."""
    spec = MODELS[cfg.model]
    if cfg.clip_sec is not None:
        sec = cfg.clip_sec
    elif params.get("duration_sec") is not None:
        sec = params["duration_sec"] / n_images
    else:
        return spec.get("clip_frames", 81)
    return _wan_frames(sec, spec["fps"])


def clip_frames_each(cfg: Config, params: dict) -> list[int]:
    """시작 이미지마다 프레임 수 (v1.4.0): 항목 sec 이 있으면 그것으로, 없으면 clip_frames_for 와 같음."""
    fps = MODELS[cfg.model]["fps"]
    default = clip_frames_for(cfg, params, len(cfg.start_images))
    return [_wan_frames(item["sec"], fps) if isinstance(item, dict) and item.get("sec") is not None else default
            for item in cfg.start_images]


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
    r = subprocess.run([sys.executable, "-m", "pip", "install", "-q", *need], capture_output=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        raise RuntimeError(f"pip install failed: {r.stderr[-1500:]}\n→ Kaggle 설정에서 Internet 을 켰는지 확인")


def _version_tuple(v: str) -> tuple[int, ...]:
    return tuple(int(x) for x in re.findall(r"\d+", v.split("+")[0])[:3])


def _disable_old_torchao(allow_uninstall: bool):
    """오래된 torchao(<0.15)가 있으면 diffusers 모델 import 가 FqnToConfig ImportError 로 깨진다. videogen 은 torchao 를
    쓰지 않으므로 (1) Kaggle 에서는 이번 세션에서만 지우고 (2) diffusers 가 기억해 둔 'torchao 있음' 표시를 끈다 —
    앞 실행이 실패해 diffusers·torchao 가 이미 커널에 올라와 있어도 커널 재시작 없이 된다."""
    from importlib import metadata
    try:
        have = metadata.version("torchao")
    except metadata.PackageNotFoundError:
        have = None
    if have is not None and _version_tuple(have) >= TORCHAO_MIN:
        log("SETUP", "torchao compatible", version=have)
        return
    if have is not None:
        log("SETUP", "preinstalled torchao is too old for diffusers (no FqnToConfig); videogen does not use torchao",
            logging.WARNING, torchao=have, required=">=" + ".".join(map(str, TORCHAO_MIN)))
        if allow_uninstall:
            r = subprocess.run([sys.executable, "-m", "pip", "uninstall", "-y", "-q", "torchao"],
                               capture_output=True, encoding="utf-8", errors="replace")
            if r.returncode != 0:
                raise RuntimeError(f"pip uninstall torchao 실패: {r.stderr[-800:]}")
            import importlib
            importlib.invalidate_caches()
            log("SETUP", "torchao uninstalled for this Kaggle session", logging.WARNING, before=have, after="none")
    import diffusers.utils.import_utils as iu
    if iu.is_torchao_available():  # 지우지 않았거나, 지우기 전에 이미 import 된 커널
        iu._torchao_available = False
        log("SETUP", "diffusers torchao flag switched off", logging.WARNING, before=True, after=iu.is_torchao_available())
    if iu.is_torchao_available():
        raise RuntimeError("diffusers 가 아직 torchao 를 씀 — 커널을 재시작(Run → Restart)한 뒤 셀을 다시 실행")


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
    with _Stage("DATA", timings, "설정 오류면 오류 문장대로 고치기 · 다운로드 오류면 Internet=On 확인 또는 model_revision 고정"):
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
        fps = cfg.fps or 24
        params = resolve_params(cfg, vae_cfg.get("scale_factor_spatial", 8) * tr_cfg["patch_size"][1],
                                vae_cfg.get("scale_factor_temporal", 4), fps=fps)
        if params["num_frames"] > DIFFUSERS_MAX_FRAMES:
            raise ValueError(f"num_frames={params['num_frames']} 은 Wan2.2-5B 한 번 생성 한도 {DIFFUSERS_MAX_FRAMES}"
                             f"({DIFFUSERS_MAX_FRAMES / fps:.1f}초)를 넘음 — 긴 영상은 model='wan2.2-14b-hq'(창 이어붙이기)")
        log("DATA", "generation params", preset=cfg.preset, height=params["height"], width=params["width"],
            num_frames=params["num_frames"], steps=params["steps"], guidance_scale=params["guidance_scale"],
            fps=fps, duration_sec=round(params["num_frames"] / fps, 2), upscale_to=params["upscale_to"])

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

    videos, base, methods = [path], [], []
    if params["upscale_to"]:
        with _Stage("UPSCALE", timings, "ffmpeg 확인 · 원본은 base_videos 에 그대로 있음"):
            dst, method = _upscale_video(cfg, params, path, run_dir)
            videos, base, methods = [dst], [path], [method]

    return dict(videos=videos, base_videos=base, upscale_methods=methods, params=params, frame_stats=fstats, fps=fps, gpus=gpus,
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
    # PYTHONUTF8·PYTHONIOENCODING: 커널 로캘이 UTF-8 이 아니어도 WanGP 가 한·중 글자(프롬프트)를 찍다가 죽지 않게
    env.update(MPLBACKEND="Agg", PYTHONUNBUFFERED="1", PYTHONUTF8="1", PYTHONIOENCODING="utf-8", **extra)
    return env


def _run(stage: str, cmd: list, hint: str, log_file: str, cwd=None, check=True, timeout=3600):
    """명령 실행: 전체 출력은 log_file 에, 결과는 한 줄로."""
    t0 = time.perf_counter()
    log(stage, "exec", cmd=" ".join(map(str, cmd))[:240])
    r = subprocess.run(list(map(str, cmd)), cwd=cwd, env=_child_env(), capture_output=True, encoding="utf-8", errors="replace", timeout=timeout)
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


def _wan_frames(duration_sec: float, fps: int) -> int:
    """길이(초) → Wan 프레임 수(4k+1). WanGP 의 '15s' 변환과 같은 값 (15초 × 16fps → 241)."""
    return max(1, round(duration_sec * fps)) // 4 * 4 + 1


def wangp_plan(cfg: Config, params: dict) -> dict:
    """WanGP 길이 계획 → {'total', 'first', 'cont'}.
    continue_with 가 있는 모델(wan2.2-14b-hq)은 처음 first_frames 를 T2V 로, 나머지(cont)를 I2V 이어 만들기로.
    T2V 는 앞 창을 보지 못해 WanGP 가 창 이어붙이기를 막는다 ("a t2v model doesn't see past frames")."""
    spec = MODELS[cfg.model]
    if params.get("duration_sec") is not None:
        total = _wan_frames(params["duration_sec"], spec["fps"]) if spec.get("fps") else f"{params['duration_sec']:g}s"
    else:
        total = params["num_frames"]
    first = spec.get("first_frames")
    if spec.get("continue_with") and isinstance(total, int) and first and total > first:
        return dict(total=total, first=first, cont=total - first)
    return dict(total=total, first=total, cont=None)


def _load_profile(app_dir: str, rel: str) -> dict:
    path = os.path.join(app_dir, "profiles", rel)
    if not os.path.exists(path):
        raise FileNotFoundError(f"WanGP 가속 프로필이 없음: {path} (wangp_ref 를 바꿨다면 프로필 이름 확인)")
    with open(path, encoding="utf-8") as f:
        prof = json.load(f)
    prof.pop("help", None)  # UI 안내 문구 — 생성 설정이 아님 (WanGP 도 생성 인자만 걸러 씀)
    return prof


def wangp_settings(cfg: Config, params: dict, app_dir: str, video_length: int | str | None = None) -> dict:
    """첫 단계 WanGP 설정 JSON. 빠진 키는 WanGP 가 모델 기본값으로 채운다(clean_settings).
    순서: 기본 → 가속 프로필(Lightning 등) → 모델 고정값 → 사용자가 직접 적은 steps/guidance → wangp_extra.
    길이는 video_length(계획) → 없으면 duration_sec 을 "15s" 꼴로 (WanGP 가 모델 fps 로 유효 프레임 수를 고름)."""
    spec = MODELS[cfg.model]
    if video_length is None:
        video_length = f"{params['duration_sec']:g}s" if params.get("duration_sec") is not None else params["num_frames"]
    s = dict(model_type=spec["model_type"], prompt=cfg.prompt, negative_prompt=cfg.negative_prompt,
             resolution=f"{params['width']}x{params['height']}", video_length=video_length, seed=cfg.seed)
    if spec.get("profile"):
        s.update(_load_profile(app_dir, spec["profile"]))
    s.update(spec.get("extra", {}))
    if "steps" in params["explicit"]:
        s["num_inference_steps"] = params["steps"]
    if "guidance_scale" in params["explicit"]:
        s["guidance_scale"] = params["guidance_scale"]
    if cfg.fps:
        s["force_fps"] = str(cfg.fps)
    s.update(cfg.wangp_extra)
    return s


def wangp_continue_settings(cfg: Config, params: dict, app_dir: str, source: str, new_frames: int) -> dict:
    """둘째 단계: source 영상을 이어 만든다 (image_prompt_type 'V' — 결과는 source + 새 프레임을 합친 한 파일,
    video_length = 새로 만들 프레임 수). 창 크기·겹침은 모델 기본값 (SVI 2 Pro = 81·4)."""
    cont = MODELS[cfg.model]["continue_with"]
    s = dict(model_type=cont["model_type"], prompt=cfg.prompt, negative_prompt=cfg.negative_prompt,
             resolution=f"{params['width']}x{params['height']}", video_length=new_frames, seed=cfg.seed,
             image_prompt_type="V", video_source=os.path.abspath(source))
    if cont.get("profile"):
        s.update(_load_profile(app_dir, cont["profile"]))
    if cfg.fps:
        s["force_fps"] = str(cfg.fps)
    return s


def wangp_image_tasks(cfg: Config, params: dict, app_dir: str, images: list[dict],
                      clip_frames: int | list[int]) -> list[dict]:
    """시작 이미지마다 작업 하나 (image_prompt_type 'S' + image_start). WanGP 는 목록을 한 프로세스에서 차례로 돌려
    모델을 한 번만 불러온다. seed 는 클립마다 seed, seed+1, … (같은 설정·이미지면 같은 결과).
    clip_frames: 모든 클립 같은 수, 또는 클립마다 (v1.4.0 — 항목 sec)."""
    frames = clip_frames if isinstance(clip_frames, list) else [clip_frames] * len(images)
    if len(frames) != len(images):
        raise ValueError(f"clip_frames {len(frames)}개 != 이미지 {len(images)}장")
    base = wangp_settings(cfg, params, app_dir, video_length=frames[0] if frames else None)
    tasks = []
    for i, (img, n) in enumerate(zip(images, frames)):
        t = dict(base, prompt=img["prompt"], seed=cfg.seed + i, image_prompt_type="S", video_length=n,
                 image_start=os.path.abspath(img["path"]))
        tasks.append(t)
    return tasks


_PROGRESS_RE = re.compile(r"\d+%\||it/s|s/it|steps/s|s/step")
_IMPORTANT_RE = re.compile(r"error|exception|traceback|warning|saved|task|loaded|download|valid|frames|steps",
                           re.IGNORECASE)


def _stream(cmd: list, cwd: str, log_file: str, stage: str, every: float = 30.0) -> int:
    """하위 프로세스 출력을 전부 log_file 에, 화면에는 중요한 줄 + 진행 줄은 every 초마다 하나."""
    last = 0.0
    with open(log_file, "a", encoding="utf-8") as lf:
        lf.write(f"\n$ {' '.join(map(str, cmd))}\n")
        proc = subprocess.Popen(list(map(str, cmd)), cwd=cwd, env=_child_env(), stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT, encoding="utf-8", errors="replace", bufsize=1)
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


def _last_error_line(log_file: str) -> str:
    try:
        lines = open(log_file, encoding="utf-8", errors="replace").read().splitlines()
    except OSError:
        return ""
    errs = [ln.strip() for ln in lines if "[ERROR]" in ln or "Error" in ln or "error" in ln]
    return errs[-1][:400] if errs else ""


def _wangp_process(cfg: Config, settings: dict | list, name: str, run_dir: str, media_dir: str, app_dir: str, py: str,
                   attention: str, wgp_log: str, stage: str) -> list[str]:
    """설정 JSON(작업 하나 또는 목록) 저장 → (--dry-run 검증) → --process → 새 결과 파일 목록 (만든 순서)."""
    settings_path = os.path.join(run_dir, name)
    with open(settings_path, "w", encoding="utf-8") as f:
        json.dump(settings, f, ensure_ascii=False, indent=2)
    tasks = settings if isinstance(settings, list) else [settings]
    for n, task in enumerate(tasks, 1):
        shown = {k: (v if not isinstance(v, str) or len(v) < 80 else "..." + v[-60:]) for k, v in task.items()}
        log(stage, "settings", file=name, task=f"{n}/{len(tasks)}",
            **{k: json.dumps(v, ensure_ascii=False) if isinstance(v, (list, dict)) else v
               for k, v in shown.items() if k not in ("prompt", "negative_prompt")})
        if len(tasks) > 1:
            log(stage, "task prompt", task=f"{n}/{len(tasks)}", prompt=task["prompt"][:160])
    base = [py, "wgp.py", "--process", settings_path, "--output-dir", media_dir,
            "--profile", cfg.wangp_profile, "--attention", attention, "--gpu", cfg.wangp_gpu]
    if cfg.wangp_dry_run_first:
        rc = _stream(base + ["--dry-run"], app_dir, wgp_log, stage)
        if rc != 0:
            raise RuntimeError(f"WanGP 설정 검증 실패 (rc={rc}): {_last_error_line(wgp_log)} — 전체 로그: {wgp_log}")
        log(stage, "dry-run ok (settings valid)")
    before = set(os.listdir(media_dir))
    t0 = time.perf_counter()
    rc = _stream(base, app_dir, wgp_log, stage)
    if rc != 0:
        for line in open(wgp_log, encoding="utf-8", errors="replace").read().strip().splitlines()[-8:]:
            log(stage, "  | " + line[:300], logging.ERROR)
        raise RuntimeError(f"WanGP 생성 실패 (rc={rc}): {_last_error_line(wgp_log)} — 전체 로그: {wgp_log}")
    new = sorted((os.path.join(media_dir, n) for n in set(os.listdir(media_dir)) - before
                  if os.path.splitext(n)[1].lower() in MEDIA_EXT), key=os.path.getmtime)  # WanGP 는 작업을 차례로 저장
    if not new:
        raise RuntimeError(f"WanGP 가 0 으로 끝났지만 새 결과 파일이 없음 — {wgp_log}")
    for p in new:
        info = _video_info(p) if p.lower().endswith((".mp4", ".webm", ".mkv")) else {}
        log(stage, "saved", file=p, size_mb=round(os.path.getsize(p) / 1e6, 2), **info)
    log(stage, "wall time", sec=round(time.perf_counter() - t0, 1))
    return new


def _clips(paths: list[str]) -> list[str]:
    return [p for p in paths if p.lower().endswith((".mp4", ".webm", ".mkv"))]


def _wangp_generate(cfg: Config, run_dir: str, run_id: str, timings: dict) -> dict:
    install_log = os.path.join(run_dir, "wangp_install.log")
    wgp_log = os.path.join(run_dir, "wangp_process.log")
    spec = MODELS[cfg.model]
    with _Stage("SETUP", timings, "Accelerator = GPU T4 x2"):
        gpus = _nvidia_smi()
        for g in gpus:
            log("SETUP", "gpu", **g)
        # Wan 해상도는 모델 블록 크기(14B 16 · 5B 32)의 배수로 — WanGP 가 몰래 내리기 전에 여기서 맞추고 전·후를 남긴다
        params = resolve_params(cfg, spatial_multiple=spec.get("block"))
        log("SETUP", "generation params", preset=cfg.preset, resolution=f"{params['width']}x{params['height']}",
            num_frames=params["num_frames"], duration_sec=params["duration_sec"], upscale_to=params["upscale_to"],
            upscale_factor=params["upscale_factor"], upscale_fit=params["upscale_fit"],
            explicit=",".join(params["explicit"]) or "none",
            note="steps/guidance from the WanGP model or accelerator profile unless explicit")
        if cfg.start_images:
            frames = clip_frames_each(cfg, params)
            same = len(set(frames)) == 1
            plan = dict(total=sum(frames), first=frames[0], cont=None, clips=len(frames),
                        clip_frames=frames[0] if same else frames)
            log("SETUP", "clip plan", clips=plan["clips"],
                frames_per_clip=frames[0] if same else f"{min(frames)}..{max(frames)} (per clip)",
                sec_per_clip=round(frames[0] / spec["fps"], 2) if same else "per clip",
                total_sec=round(plan["total"] / spec["fps"], 2), model=spec["model_type"], concat=cfg.concat,
                release_tag=cfg.release_tag or "none")
            if not same:
                log("SETUP", "per-clip frames", logging.DEBUG, frames=",".join(map(str, frames)))
            limit = spec.get("clip_frames", 81)
            for item, n in zip(cfg.start_images, frames):
                if n > limit:
                    log("SETUP", "clip longer than the model's ~5s training length: WanGP will window it (slower)",
                        logging.WARNING, name=item.get("name", "") if isinstance(item, dict) else "",
                        frames=n, model_clip_frames=limit)
            if cfg.release_tag and cfg.concat:
                log("SETUP", "release_tag with concat=True: clips/ holds the clips before joining/upscaling — "
                    "set concat=False to get each clip upscaled", logging.WARNING)
        else:
            plan = wangp_plan(cfg, params)
            log("SETUP", "length plan", total=plan["total"], first_stage=f"{spec['model_type']}:{plan['first']}",
                continue_stage=f"{spec['continue_with']['model_type']}:{plan['cont']}" if plan["cont"] else "none",
                model_fps=spec.get("fps", "model default"))
        if spec.get("disk_gb") and _free_disk_gb(cfg.work_dir) < spec["disk_gb"]:
            log("SETUP", "scratch disk may be too small for this model's downloads (estimate)", logging.WARNING,
                free_gb=_free_disk_gb(cfg.work_dir), estimate_gb=spec["disk_gb"])
    images = []
    if cfg.start_images:  # 설치 전에 받아 두어 주소가 틀렸으면 바로 멈춘다
        with _Stage("IMAGES", timings, "이미지 주소·경로 확인 (Kaggle 데이터는 /kaggle/input/...)"):
            images = prepare_start_images(cfg, params, run_dir)
    app_dir, py, attention = _wangp_install(cfg, timings, install_log)
    media_dir = os.path.join(run_dir, "media")
    os.makedirs(media_dir, exist_ok=True)
    run_args = (run_dir, media_dir, app_dir, py, attention, wgp_log)

    segments, raw_clips = [], []
    with _Stage("GENERATE", timings, "wangp_process.log 끝부분 확인 · RAM 부족이면 wangp_profile='5'"):
        if images:
            new = _wangp_process(cfg, wangp_image_tasks(cfg, params, app_dir, images, plan["clip_frames"]),
                                 "wangp_settings.json", *run_args, "GENERATE")
            if len(_clips(new)) != len(images):
                raise RuntimeError(f"클립 {len(images)}개를 기대했는데 {len(_clips(new))}개 — {wgp_log}")
            raw_clips = _clips(new)   # 이어 붙이기 전, 이미지 순서대로 (v1.4.0 clips/ 용)
        else:
            new = _wangp_process(cfg, wangp_settings(cfg, params, app_dir, video_length=plan["first"]),
                                 "wangp_settings.json", *run_args, "GENERATE")
    if plan["cont"]:
        with _Stage("CONTINUE", timings, "첫 단계 영상은 media 폴더에 있음 · wangp_process.log 끝부분 확인"):
            first = _clips(new)
            if len(first) != 1:
                raise RuntimeError(f"첫 단계 영상이 1개가 아님: {first}")
            segments = first
            new = _wangp_process(cfg, wangp_continue_settings(cfg, params, app_dir, first[0], plan["cont"]),
                                 "wangp_continue.json", *run_args, "CONTINUE")
    if images and cfg.concat and len(_clips(new)) > 1:
        with _Stage("CONCAT", timings, "클립들은 media 폴더에 그대로 있음 · concat=False 로 따로 받기"):
            segments = _clips(new)
            joined = os.path.join(run_dir, f"{cfg.model}_{run_id}_{len(segments)}clips.mp4")
            _ffmpeg_concat(segments, joined, params["width"], params["height"], fps=spec.get("fps"))
            log("CONCAT", "joined", file=joined, clips=len(segments), **_video_info(joined))
            new = [joined]

    videos, base, methods = new, [], []
    clips = _clips(new)
    if params["upscale_to"] and clips:
        with _Stage("UPSCALE", timings, "생성 원본은 base_videos(media 폴더)에 그대로 있음 · upscaler='lanczos' 로 다시"):
            ups = [_upscale_video(cfg, params, c, run_dir, wangp=(app_dir, py, attention, wgp_log)) for c in clips]
            videos, base, methods = [u[0] for u in ups], clips, [u[1] for u in ups]
    named, manifest = [], None
    if images:
        with _Stage("CLIPS", timings, "생성 결과는 media/ 에 그대로 있음"):
            # concat=False 면 클립마다 최종(업스케일)본, 이어 붙였으면 이어 붙이기 전 원본
            per_clip = videos if not segments and len(videos) == len(images) else raw_clips
            frames = plan["clip_frames"] if isinstance(plan["clip_frames"], list) else [plan["clip_frames"]] * len(images)
            named, manifest = collect_clips(cfg, run_dir, run_id, images, per_clip, frames,
                                            upscaled=per_clip is videos and bool(base))
    return dict(videos=videos, base_videos=base, segments=segments, upscale_methods=methods, params=params, plan=plan,
                start_images=images, clips=named, clips_manifest=manifest, wangp_log=wgp_log, gpus=gpus,
                attention=attention, wangp_ref=cfg.wangp_ref)


def collect_clips(cfg: Config, run_dir: str, run_id: str, images: list[dict], per_clip: list[str], frames: list[int],
                  upscaled: bool) -> tuple[list[str], str]:
    """클립마다 clips/<이름>.mp4 로 복사 + clips_manifest.json (이름·이미지·프롬프트·seed·프레임·실제 길이·크기·sha256).
    Claude 가 이 목록으로 영상 시각표에 클립을 놓는다 (v1.4.0)."""
    if len(per_clip) != len(images):
        raise RuntimeError(f"클립 {len(per_clip)}개 != 이미지 {len(images)}장 — media/ 확인")
    out_dir = os.path.join(run_dir, "clips")
    os.makedirs(out_dir, exist_ok=True)
    fps = MODELS[cfg.model]["fps"]
    entries, paths = [], []
    for i, (img, src, n) in enumerate(zip(images, per_clip, frames)):
        dst = os.path.join(out_dir, img["name"] + os.path.splitext(src)[1].lower())
        shutil.copyfile(src, dst)
        info = _video_info(dst)
        entry = dict(name=img["name"], file=os.path.basename(dst), image=img["src"], prompt=img["prompt"],
                     seed=cfg.seed + i, target_sec=img.get("sec"), frames=n, model_fps=fps,
                     duration_sec=info.get("duration_sec"), width=info.get("width"), height=info.get("height"),
                     fps=info.get("fps"), upscaled=upscaled, source=os.path.basename(src), sha256=_sha256(dst),
                     run_id=run_id)
        entries.append(entry)
        paths.append(dst)
        short = img.get("sec") is not None and info.get("duration_sec") and info["duration_sec"] + 0.05 < img["sec"]
        log("CLIPS", "clip", name=img["name"], file=dst, frames=n, target_sec=img.get("sec") or "default",
            duration_sec=info.get("duration_sec"), size=f"{info.get('width')}x{info.get('height')}",
            size_mb=round(os.path.getsize(dst) / 1e6, 2))
        if short:
            log("CLIPS", "clip shorter than asked (Wan frame rule 4k+1 or model cap)", logging.WARNING,
                name=img["name"], target_sec=img["sec"], duration_sec=info["duration_sec"])
    manifest = os.path.join(out_dir, MANIFEST_NAME)
    with open(manifest, "w", encoding="utf-8") as f:
        json.dump(dict(videogen_version=__version__, run_id=run_id, model=cfg.model, created=_now_iso(),
                       clips=entries), f, ensure_ascii=False, indent=2)
    log("CLIPS", "manifest", file=manifest, clips=len(entries),
        total_sec=round(sum(e["duration_sec"] or 0 for e in entries), 2))
    return paths, manifest


def _now_iso() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


# --------------------------------------------------------------------------------------------------
# v1.4.0 GitHub Release 로 클립 보내기 — Kaggle 결과를 Claude(클라우드 환경)가 받아 이어 붙임.
# 토큰은 Kaggle Secret GITHUB_TOKEN (내레이션 셀과 같은 토큰). 값은 로그·메타데이터에 남기지 않는다.
# 실패는 경고만: 생성한 클립은 Output 탭(clips/)에 그대로 있고, 아래 publish_release() 를 같은 세션에서 다시 부르면 된다.
# --------------------------------------------------------------------------------------------------
class _HTTPError(Exception):
    def __init__(self, status: int, body: str):
        super().__init__(f"HTTP {status}: {body[:300]}")
        self.status, self.body = status, body


def _http(method: str, url: str, token: str, data: bytes | None = None, content_type: str | None = None,
          accept: str = "application/vnd.github+json", timeout: int = 300) -> tuple[int, bytes]:
    """GitHub API 한 번. 토큰은 리디렉트(자산 내려받기 → 다른 호스트)로 따라가지 않게 unredirected 헤더로."""
    import urllib.error
    import urllib.request
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Accept", accept)
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    req.add_header("User-Agent", "videogen/" + __version__)
    if content_type:
        req.add_header("Content-Type", content_type)
    req.add_unredirected_header("Authorization", "Bearer " + token)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        raise _HTTPError(e.code, e.read().decode("utf-8", "replace")) from None


def _gh(method: str, url: str, token: str, tries: int = 4, **kw) -> tuple[int, bytes]:
    """네트워크 오류·5xx·429 는 2·4·8초 쉬고 다시 (4xx 는 바로 올림)."""
    for attempt in range(1, tries + 1):
        try:
            return _http(method, url, token, **kw)
        except _HTTPError as e:
            if e.status < 500 and e.status != 429 or attempt == tries:
                raise
            err = e
        except OSError as e:  # URLError·연결 끊김·시간 초과
            if attempt == tries:
                raise
            err = e
        log("RELEASE", "request failed, retrying", logging.WARNING, method=method, url=url.split("?")[0][-100:],
            attempt=attempt, error=repr(err)[:200])
        time.sleep(2 ** attempt)
    raise RuntimeError("unreachable")


def _release(repo: str, tag: str, token: str) -> dict:
    """태그의 Release — 없으면 만든다 (prerelease: 공개 저장소면 로그인 없이 받을 수 있게, 초안은 안 됨)."""
    try:
        _, body = _gh("GET", f"{GITHUB_API}/repos/{repo}/releases/tags/{tag}", token)
        rel = json.loads(body)
        log("RELEASE", "found", tag=tag, id=rel["id"], url=rel.get("html_url"))
        return rel
    except _HTTPError as e:
        if e.status != 404:
            raise
    payload = dict(tag_name=tag, name=tag, prerelease=True,
                   body="videogen 장면 클립 (Kaggle) — 영상 합치기용 중간 결과. clips_manifest.json 에 클립 목록.")
    _, body = _gh("POST", f"{GITHUB_API}/repos/{repo}/releases", token, data=json.dumps(payload).encode(),
                  content_type="application/json")
    rel = json.loads(body)
    log("RELEASE", "created", tag=tag, id=rel["id"], url=rel.get("html_url"), prerelease=True)
    return rel


def _release_assets(repo: str, rel_id: int, token: str) -> dict[str, dict]:
    assets, page = {}, 1
    while True:
        _, body = _gh("GET", f"{GITHUB_API}/repos/{repo}/releases/{rel_id}/assets?per_page=100&page={page}", token)
        batch = json.loads(body)
        assets.update({a["name"]: a for a in batch})
        if len(batch) < 100:
            return assets
        page += 1


def _upload_asset(repo: str, rel: dict, path: str, name: str, token: str, assets: dict[str, dict]) -> dict:
    """같은 이름 자산이 있으면 지우고 올린다 (클립을 다시 만든 경우)."""
    import urllib.parse
    if name in assets:
        _gh("DELETE", f"{GITHUB_API}/repos/{repo}/releases/assets/{assets[name]['id']}", token)
        log("RELEASE", "replaced old asset", name=name)
    ctype = "application/json" if name.endswith(".json") else "video/mp4"
    with open(path, "rb") as f:
        data = f.read()
    url = f"{GITHUB_UPLOADS}/repos/{repo}/releases/{rel['id']}/assets?name={urllib.parse.quote(name)}"
    _, body = _gh("POST", url, token, data=data, content_type=ctype, timeout=900)
    asset = json.loads(body)
    assets[name] = asset
    return asset


def publish_release(manifest_path: str, tag: str, repo: str = "yeomin1024/yeomin1024-ytb",
                    token: str | None = None) -> dict:
    """clips_manifest.json 과 그 클립들을 Release(tag)에 올린다. 이미 있는 목록과 이름으로 합친다(다시 만든 클립만 바뀜).
    실패해도 멈추지 않고 {'ok': False, 'error': ...} — Kaggle 같은 세션에서 다시:
        videogen.publish_release("/kaggle/working/outputs/<실행시각>/clips/clips_manifest.json", "clips-<영상ID>")"""
    t0 = time.perf_counter()
    token = token or _kaggle_secret("GITHUB_TOKEN")
    if not token:
        log("RELEASE", "GITHUB_TOKEN not found — clips stay in the Output tab only. Kaggle: Add-ons → Secrets → "
            "GITHUB_TOKEN (attach to this notebook), then call videogen.publish_release(...)", logging.WARNING,
            manifest=manifest_path)
        return dict(ok=False, error="no GITHUB_TOKEN", uploaded=[], failed=[])
    try:
        man = json.load(open(manifest_path, encoding="utf-8"))
        clip_dir = os.path.dirname(manifest_path)
        rel = _release(repo, tag, token)
        assets = _release_assets(repo, rel["id"], token)
        merged = {}
        if MANIFEST_NAME in assets:  # 이전 실행에서 올린 목록 — 자산 API 로 받음 (리디렉트엔 토큰을 안 붙임)
            _, body = _gh("GET", assets[MANIFEST_NAME]["url"], token, accept="application/octet-stream")
            merged = {c["name"]: c for c in json.loads(body).get("clips", [])}
            log("RELEASE", "existing manifest", clips=len(merged))
        uploaded, failed, total = [], [], 0
        for c in man["clips"]:
            path = os.path.join(clip_dir, c["file"])
            try:
                a = _upload_asset(repo, rel, path, c["file"], token, assets)
            except Exception as e:  # 한 클립 실패 — 나머지는 계속, 목록에서는 뺀다(옛 자산도 지웠을 수 있음)
                failed.append(c["name"])
                merged.pop(c["name"], None)
                log("RELEASE", "upload failed", logging.WARNING, name=c["name"], error=repr(e)[:300])
                continue
            total += os.path.getsize(path)
            merged[c["name"]] = dict(c, release_url=a.get("browser_download_url"), asset_id=a.get("id"))
            uploaded.append(c["name"])
            log("RELEASE", "uploaded", name=c["name"], size_mb=round(os.path.getsize(path) / 1e6, 2),
                done=f"{len(uploaded)}/{len(man['clips'])}")
        out = dict({k: v for k, v in man.items() if k != "clips"}, updated=_now_iso(), release_tag=tag, repo=repo,
                   clips=sorted(merged.values(), key=lambda c: c["name"]))
        rel_manifest = os.path.join(clip_dir, "clips_manifest_release.json")
        with open(rel_manifest, "w", encoding="utf-8") as f:
            json.dump(out, f, ensure_ascii=False, indent=2)
        _upload_asset(repo, rel, rel_manifest, MANIFEST_NAME, token, assets)
        log("RELEASE", "done", tag=tag, url=rel.get("html_url"), uploaded=len(uploaded), failed=len(failed),
            clips_in_release=len(merged), mb=round(total / 1e6, 1), sec=round(time.perf_counter() - t0, 1))
        if failed:
            log("RELEASE", "some clips failed — call publish_release(...) again in this session", logging.WARNING,
                failed=",".join(failed))
        return dict(ok=not failed, url=rel.get("html_url"), uploaded=uploaded, failed=failed, manifest=rel_manifest)
    except Exception as e:  # Release 를 못 만들거나 목록을 못 올림 — 클립은 Output 탭에 그대로
        hint = "토큰 권한(contents: write)·저장소 이름 확인" if isinstance(e, _HTTPError) and e.status in (401, 403, 404) \
            else "Internet=On 확인 후 publish_release(...) 다시"
        log("RELEASE", "FAILED — clips stay in the Output tab (clips/)", logging.WARNING, tag=tag, repo=repo,
            error=repr(e)[:300], next_step=hint)
        return dict(ok=False, error=repr(e)[:300], uploaded=[], failed=[])


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
        manage_env = cfg.install_deps and "KAGGLE_KERNEL_RUN_TYPE" in os.environ  # 남의 PC 환경은 고치지 않음
        if manage_env:
            _ensure_packages(DIFFUSERS_PACKAGES)
        _disable_old_torchao(allow_uninstall=manage_env)
        result = _diffusers_generate(cfg, run_dir, run_id, timings)
    else:
        result = _wangp_generate(cfg, run_dir, run_id, timings)
    if cfg.release_tag and result.get("clips_manifest"):
        t0 = time.perf_counter()
        result["release"] = publish_release(result["clips_manifest"], cfg.release_tag, cfg.release_repo)
        timings["RELEASE"] = round(time.perf_counter() - t0, 1)

    meta_path = os.path.join(run_dir, f"videogen_{run_id}.json")
    meta = dict(videogen_version=__version__, code_sha256=code_sha, run_id=run_id, config=asdict(cfg),
                backend=spec["backend"], timings_sec=timings, python=platform.python_version(), **result)
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2, default=str)
    log("SUMMARY", "stage timings (sec)", **timings, total=round(sum(timings.values()), 1))
    log("SUMMARY", "outputs", videos=len(result["videos"]), metadata=meta_path, log=log_file)
    for v in result["videos"]:
        size = _video_size(v) if v.lower().endswith((".mp4", ".webm", ".mkv")) else None
        log("SUMMARY", "final", file=v, size="x".join(map(str, size)) if size else "n/a",
            size_mb=round(os.path.getsize(v) / 1e6, 2))
    for v in result.get("base_videos", []):
        log("SUMMARY", "base (before upscale, kept)", file=v)
    for v in result.get("segments", []):
        log("SUMMARY", "segment (kept)", file=v)
    if result.get("clips_manifest"):
        log("SUMMARY", "named clips", clips=len(result["clips"]), manifest=result["clips_manifest"])
    if result.get("release"):
        rel = result["release"]
        log("SUMMARY", "release", ok=rel["ok"], url=rel.get("url", "n/a"), uploaded=len(rel["uploaded"]),
            failed=len(rel["failed"]), error=rel.get("error", "none"))
    if cfg.preview:
        _preview(result["videos"][:3] if result.get("clips") else result["videos"])  # 장면 클립 수십 개면 앞 3개만
    return dict(videos=result["videos"], metadata=meta_path, log=log_file, timings=timings, run_dir=run_dir,
                clips_manifest=result.get("clips_manifest"), release=result.get("release"))


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
