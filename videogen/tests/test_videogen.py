# -*- coding: utf-8 -*-
# VERSION: v1.4.0 — 2026-10-19 — 장면 클립 시험 (test_scene_clips: 항목 sec·name·image_base 검사 · clips/ + 목록 ·
#          가짜 GitHub Release(메모리, 네트워크 없음 — GITHUB_TOKEN 류 환경 변수를 지우고 가짜 저장소 이름)로 새로 만들기 ·
#          같은 이름 바꿔 올리기 · 목록 합치기 · 502 다시 시도 · 올리기 실패는 경고만 · 토큰 없음 · 토큰이 로그에 없음)
# 이전 v1.3.1 — 2026-10-19 — ASCII 로캘 회귀 시험 (test_ascii_locale: Kaggle '업스케일 결과 크기 None' 재현 →
#          ffprobe·ffmpeg 크기 읽기 · _check_size · upscale_file · _stream · 시작 이미지 Lanczos 흐름) · 가짜 WanGP 가
#          진짜처럼 결과 mp4 에 중국어 메타데이터 · 시험 파일 읽기·쓰기를 UTF-8 로 고정 · test_upscale_file_rejoin(16fps 로
#          이어 붙인 결과 폴더 → 클립으로 다시 24fps · 클립 fps 를 못 읽으면 모델 fps/멈춤)
# 이전 v1.3.0 — 2026-10-18 — 시작 이미지 여러 장 시험 (test_start_images: 이미지 받기·자르기 · 작업 목록 한 번 실행 ·
#          이어 붙이기 · cover 업스케일) · upscale_plan 시험 · 가짜 WanGP 가 작업 목록·시작 이미지를 처리
# 이전 v1.2.1 — 2026-10-18 — hq 두 단계(T2V 81프레임 → SVI 2 Pro 이어 만들기) 시험, 가짜 WanGP 가 Kaggle 에서 난
#          'Sliding Windows with a Text to Video model' 거부 규칙을 흉내 내 v1.2.0 설정이 거부되는지(회귀) 확인
# 이전 v1.2.0 — 2026-10-18 — 1080p·15초 시험 추가 (test_fhd: 길이→프레임, 업스케일 배율 검사, 창 이어붙이기 설정,
#          가짜 WanGP 로 FlashVSR 성공·실패→Lanczos 대체, diffusers 121프레임 한도)
# 이전 v1.1.1 — 2026-10-18 — 오래된 torchao(FqnToConfig 없음) 재현·수정 시험 추가 (test_old_torchao)
# 이전 v1.1.0 — 2026-10-18 — videogen.py 오프라인 시험 (GPU·네트워크 없이)
r"""
1) 설정 검사: 모르는 키·모델·프리셋은 바로 멈추고, 모양 규칙(32 배수·4k+1) 보정은 경고로 남는다.
2) diffusers 길 전체: 실제 Wan 클래스로 만든 아주 작은 랜덤 Wan2.2-TI2V 구조 모델로 CPU 에서
   인코딩 → 디노이즈 → 디코딩 → mp4·JSON·로그까지 (torch·diffusers 가 없으면 건너뜀). 화질이 아니라 코드 경로를 본다.
3) WanGP 길: 가짜 wgp.py 로 설정 JSON(가속 프로필 합치기) → --dry-run → --process → 결과 수집·메타데이터.
   진짜 WanGP 설치·생성은 Kaggle GPU 가 필요해 여기서는 시험하지 않는다.

실행:  python videogen/tests/test_videogen.py
"""
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import textwrap

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import videogen  # noqa: E402

PROFILE = videogen.MODELS["wan2.2-14b-lightning"]["profile"]


def expect_error(fn, exc, text):
    try:
        fn()
    except exc as e:
        assert text in str(e), str(e)
        return
    raise AssertionError(f"{exc.__name__} expected")


def test_config(tmp):
    expect_error(lambda: videogen.make_config({"promt": "x"}), ValueError, "promt")
    expect_error(lambda: videogen.make_config(model="sora"), ValueError, "sora")
    expect_error(lambda: videogen.make_config(preset="4k"), ValueError, "4k")
    expect_error(lambda: videogen.make_config(prompt="  "), ValueError, "prompt")
    assert videogen.pick_torch_build("580.82.07") == "cu130"
    assert videogen.pick_torch_build("560.35.03") == "cu128"
    expect_error(lambda: videogen.pick_torch_build("470.1"), RuntimeError, "470.1")
    videogen._setup_logging("INFO", os.path.join(tmp, "cfg.log"))
    p = videogen.resolve_params(videogen.make_config(height=70, width=130, num_frames=10), 32, 4)
    assert (p["height"], p["width"], p["num_frames"]) == (64, 128, 9) and p["explicit"] == ["height", "num_frames", "width"]
    assert "adjusted" in open(os.path.join(tmp, "cfg.log"), encoding="utf-8").read()
    env = videogen._child_env()
    assert "PYTHONPATH" not in env and env["MPLBACKEND"] == "Agg"
    expect_error(lambda: videogen.make_config(upscaler="esrgan"), ValueError, "esrgan")
    expect_error(lambda: videogen.make_config(upscale_to="1080p"), ValueError, "1080p")
    expect_error(lambda: videogen.make_config(duration_sec=0), ValueError, "duration_sec")
    print("ok  config / helpers")


def test_fhd_params(tmp):
    """fhd_15s: 1280x720 생성 → ×1.5 = 1920x1080, 길이는 WanGP 에 '15s' 로, diffusers 는 fps 로 프레임 수."""
    videogen._setup_logging("INFO", os.path.join(tmp, "fhd.log"))
    cfg = videogen.make_config(model="wan2.2-14b-hq", preset="fhd_15s")
    p = videogen.resolve_params(cfg)
    assert (p["width"], p["height"], p["duration_sec"], p["num_frames"]) == (1280, 720, 15, None), p
    assert p["upscale_to"] == "1920x1080" and p["upscale_factor"] == 1.5, p
    # diffusers 처럼 fps 를 주면 프레임 수로: 15초 × 24 = 360 → 4k+1 = 361
    assert videogen.resolve_params(cfg, None, 4, fps=24)["num_frames"] == 361
    # 직접 적은 num_frames 는 프리셋 길이보다 우선, 직접 적은 duration_sec 은 그보다 우선
    assert videogen.resolve_params(videogen.make_config(preset="fhd_15s", num_frames=81))["duration_sec"] is None
    assert videogen.resolve_params(videogen.make_config(preset="fhd_15s", num_frames=81, duration_sec=10))["duration_sec"] == 10
    # 배율이 맞지 않으면 멈추고 맞는 생성 해상도를 알려 준다
    assert videogen.upscale_plan(1280, 720, "1920x1080") == {"factor": 1.5, "fit": "exact", "crop_pct": 0.0}
    assert videogen.upscale_plan(960, 540, "1920x1080")["factor"] == 2.0
    # 5B 는 32 배수라 1280x704: 비율 차이 2.3% → ×2 로 키운 뒤 가운데 자르기
    up = videogen.upscale_plan(1280, 704, "1920x1080")
    assert up["fit"] == "cover" and up["factor"] == 2.0 and 2 < up["crop_pct"] < 3, up
    # 비율이 3% 넘게 다르면 멈추고 맞는 생성 해상도를 알려 줌 (832x480 은 16:9 와 2.5% 차이라 cover 허용)
    assert videogen.upscale_plan(832, 480, "1920x1080")["fit"] == "cover"
    expect_error(lambda: videogen.upscale_plan(1024, 1024, "1920x1080"), ValueError, "1280x720(×1.5)")
    expect_error(lambda: videogen.upscale_plan(256, 144, "1920x1080"), ValueError, "지원 배율")
    print("ok  fhd_15s params / upscale factor checks")


def build_tiny_wan(path):
    # 이 시험은 run() 보다 먼저 diffusers 를 import 하므로, run() 과 같은 torchao 처리를 먼저 한다
    videogen._setup_logging("INFO", os.path.join(os.path.dirname(path), "build.log"))
    videogen._disable_old_torchao(allow_uninstall=False)
    import torch
    from diffusers import AutoencoderKLWan, UniPCMultistepScheduler, WanPipeline, WanTransformer3DModel
    from tokenizers import Tokenizer, models, pre_tokenizers
    from transformers import PreTrainedTokenizerFast, UMT5Config, UMT5EncoderModel

    torch.manual_seed(0)
    z = 8  # 실제 모델은 48
    words = ["<pad>", "</s>", "<unk>"] + "a golden retriever runs through sunlit meadow toward the camera".split()
    tok = Tokenizer(models.WordLevel({w: i for i, w in enumerate(words)}, unk_token="<unk>"))
    tok.pre_tokenizer = pre_tokenizers.Whitespace()
    WanPipeline(
        tokenizer=PreTrainedTokenizerFast(tokenizer_object=tok, pad_token="<pad>", eos_token="</s>", unk_token="<unk>"),
        text_encoder=UMT5EncoderModel(UMT5Config(vocab_size=len(words), d_model=32, d_kv=8, d_ff=64, num_layers=1,
                                                 num_heads=4, relative_attention_num_buckets=8)),
        vae=AutoencoderKLWan(base_dim=16, decoder_base_dim=16, z_dim=z, dim_mult=[1, 2, 2, 2], num_res_blocks=1,
                             temperal_downsample=[False, True, True], is_residual=True, in_channels=12,
                             out_channels=12, patch_size=2, scale_factor_temporal=4, scale_factor_spatial=16,
                             latents_mean=[0.0] * z, latents_std=[1.0] * z),
        scheduler=UniPCMultistepScheduler(prediction_type="flow_prediction", use_flow_sigmas=True,
                                          num_train_timesteps=1000, flow_shift=5.0),
        transformer=WanTransformer3DModel(patch_size=(1, 2, 2), num_attention_heads=2, attention_head_dim=8,
                                          in_channels=z, out_channels=z, text_dim=32, freq_dim=16, ffn_dim=32,
                                          num_layers=2, cross_attn_norm=True, qk_norm="rms_norm_across_heads",
                                          rope_max_seq_len=32),
        expand_timesteps=True,
    ).save_pretrained(path)


def test_diffusers(tmp):
    if not all(importlib.util.find_spec(m) for m in ("torch", "diffusers", "transformers")):
        print("skip diffusers smoke test (torch/diffusers not installed)")
        return
    model_dir = os.path.join(tmp, "tiny-wan22-ti2v")
    build_tiny_wan(model_dir)
    res = videogen.run(dict(model="wan2.2-5b", model_path=model_dir, device_plan="cpu", prompt="a golden retriever",
                            negative_prompt="blurry static", height=70, width=130, num_frames=10, steps=4, fps=8,
                            step_log_every=2, max_sequence_length=16, output_dir=os.path.join(tmp, "out_d"),
                            work_dir=os.path.join(tmp, "work"), preview=False, install_deps=False))
    meta = json.load(open(res["metadata"], encoding="utf-8"))
    fs = meta["frame_stats"]
    assert (fs["frames"], fs["height"], fs["width"]) == (9, 64, 128) and fs["finite"], fs
    assert os.path.getsize(res["videos"][0]) > 0 and meta["config"]["seed"] == 42
    assert len(meta["code_sha256"]) == 64 and meta["videogen_version"] == videogen.__version__
    text = open(res["log"], encoding="utf-8").read()
    for tag in ("[CONFIG]", "[SETUP]", "[DATA]", "[ENCODE]", "[DENOISE]", "[DECODE]", "[EXPORT]", "[SUMMARY]"):
        assert tag in text, tag
    print("ok  diffusers path (tiny model, CPU):", res["videos"][0])


STALE_KERNEL = textwrap.dedent('''
    # 사용자가 Kaggle 에서 겪은 순서: 첫 실행이 FqnToConfig 오류로 실패 → 같은 커널에서 셀을 다시 실행
    import sys; sys.path.insert(0, sys.argv[1])
    try:
        from diffusers import AutoencoderKLWan
        print("before: import ok")
    except RuntimeError as e:
        print("before: FqnToConfig error" if "FqnToConfig" in str(e) else "before: other error " + str(e)[:200])
    import videogen
    videogen._setup_logging("INFO", sys.argv[2])
    videogen._disable_old_torchao(allow_uninstall=sys.argv[3] == "1")
    from diffusers import AutoencoderKLWan  # noqa: F811
    print("after: import ok")
''')


def test_old_torchao(tmp):
    """오래된 torchao 가 있는 환경에서만 의미가 있다 (Kaggle 2026-10 이미지 재현: torchao 0.13.0)."""
    from importlib import metadata
    try:
        have = metadata.version("torchao")
    except metadata.PackageNotFoundError:
        have = None
    if have is None or videogen._version_tuple(have) >= videogen.TORCHAO_MIN:
        print(f"skip old-torchao test (torchao={have}; install torchao==0.13.0 to reproduce the Kaggle error)")
        return
    script = os.path.join(tmp, "stale_kernel.py")
    open(script, "w", encoding="utf-8").write(STALE_KERNEL)
    # 1 = 지우는 길(Kaggle) — VIDEOGEN_TEST_UNINSTALL=1 일 때만 (시험 환경의 torchao 를 실제로 지움)
    mode = "1" if os.environ.get("VIDEOGEN_TEST_UNINSTALL") == "1" else "0"
    log_path = os.path.join(tmp, "torchao.log")
    r = subprocess.run([sys.executable, script, os.path.dirname(HERE), log_path, mode], capture_output=True, text=True)
    assert "before: FqnToConfig error" in r.stdout and "after: import ok" in r.stdout, r.stdout + r.stderr[-1500:]
    assert "too old" in open(log_path, encoding="utf-8").read()
    print(f"ok  old torchao {have}: FqnToConfig error reproduced, fixed without kernel restart (uninstall={mode})")


FAKE_WGP = textwrap.dedent('''
    # 가짜 WanGP: 생성은 작은 진짜 mp4(프레임 수 = video_length), 이어 만들기(image_prompt_type V)는 원본 + 새 프레임을 합친
    # 파일, edit_postprocessing 은 배율만큼 큰 mp4. WanGP @ fde3c7e 의 검증 규칙 하나를 그대로 흉내 낸다:
    # T2V 모델(t2v_2_2)에서 video_length > sliding_window_size(기본 129) 면 같은 [ERROR] 로 멈춤 (2026-10-18 Kaggle 오류).
    import argparse, json, os, re, sys
    import imageio.v2 as iio, numpy as np
    ap = argparse.ArgumentParser()
    ap.add_argument("--process"); ap.add_argument("--output-dir"); ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--profile"); ap.add_argument("--attention"); ap.add_argument("--gpu")
    a = ap.parse_args()
    s = json.load(open(a.process))
    # 진짜 WanGP 처럼 결과 mp4 메타데이터(comment)에 설정을 넣는다 — Wan 기본 부정 프롬프트는 중국어 (v1.3.1 회귀)
    META = ["-metadata", "comment=" + json.dumps({"negative_prompt": "色调艳丽，过曝，静态，细节模糊不清，字幕"},
                                                 ensure_ascii=False)]
    def write(path, w, h, n, start=0, fps=16):
        frames = [np.full((h, w, 3), (20 * (start + i)) % 256, dtype=np.uint8) for i in range(n)]
        iio.mimwrite(path, frames, fps=fps, codec="libx264", macro_block_size=1, output_params=META)
    if isinstance(s, dict) and s.get("mode") == "edit_postprocessing":
        if os.environ.get("FAKE_FLASHVSR_FAIL") == "1":
            print("RuntimeError: FlashVSR Auto backend could not load any sparse attention backend"); sys.exit(3)
        w, h = iio.get_reader(s["video_source"]).get_meta_data()["size"]
        f = float(re.match(r"flashvsr\\*([\\d.]+)", s["spatial_upsampling"]).group(1))
        out = os.path.join(a.output_dir, "upscaled_fake.mp4")
        write(out, round(w * f), round(h * f), 8)
        print("New video saved to Path: " + out); sys.exit(0)
    tasks = s if isinstance(s, list) else [s]  # WanGP 는 작업 목록을 한 프로세스에서 차례로
    for t in tasks:
        assert t["model_type"] and t["prompt"], t
        vl = t["video_length"]
        n = int(vl) if not isinstance(vl, str) else int(float(vl.rstrip("s")) * 16) // 4 * 4 + 1
        if t["model_type"] == "t2v_2_2" and n > t.get("sliding_window_size", 129):
            print("[ERROR] You have requested to Generate Sliding Windows with a Text to Video model. Unless you use "
                  "the Video to Video feature this is useless as a t2v model doesn't see past frames and it will "
                  "generate the same video in each new window."); sys.exit(1)
        if "V" in t.get("image_prompt_type", "") and not os.path.exists(t.get("video_source") or ""):
            print("[ERROR] You must provide a Source Video file to continue"); sys.exit(1)
        if "S" in t.get("image_prompt_type", ""):
            if not os.path.exists(t.get("image_start") or ""):
                print("[ERROR] You must provide a Start Image"); sys.exit(1)
            if t["model_type"] == "t2v_2_2":
                print("[ERROR] t2v_2_2 does not accept a start image"); sys.exit(1)
    if a.dry_run:
        for i, t in enumerate(tasks, 1):
            print(f"  Task {i}: model={t['model_type']}, steps={t.get('num_inference_steps')}, frames={t['video_length']}")
        print(f"[DRY-RUN] Validation complete. {len(tasks)}/{len(tasks)} task(s) valid."); sys.exit(0)
    for t in tasks:
        vl = t["video_length"]
        n = int(vl) if not isinstance(vl, str) else int(float(vl.rstrip("s")) * 16) // 4 * 4 + 1
        fps = 24 if t["model_type"].startswith("ti2v") else 16
        for i in range(1, 5):
            print(f" {i * 25}%|##| {i}/4 [00:0{i}<00:00, 1.00s/it]", flush=True)
        w, h = map(int, t["resolution"].split("x"))
        if "S" in t.get("image_prompt_type", ""):  # WanGP 는 시작 이미지 비율을 결과 비율로 따른다 → 크기가 같아야 함
            iw, ih = iio.imread(t["image_start"]).shape[1::-1]
            assert (iw, ih) == (w, h), f"start image {iw}x{ih} != resolution {w}x{h}"
        path = os.path.join(a.output_dir, f"{t['model_type']}_seed{t['seed']}_fake.mp4")
        if "V" in t.get("image_prompt_type", ""):
            src = [f for f in iio.mimread(t["video_source"], memtest=False)]
            merged = src + [np.full((h, w, 3), 7, dtype=np.uint8)] * n
            iio.mimwrite(path, merged, fps=fps, codec="libx264", macro_block_size=1, output_params=META)
        else:
            write(path, w, h, n, start=t["seed"], fps=fps)
        print("New video saved to Path: " + path, flush=True)
        import time; time.sleep(0.02)  # 저장 순서 = 작업 순서 (mtime)
''')


def test_wangp(tmp):
    app = os.path.join(tmp, "Wan2GP")
    os.makedirs(os.path.join(app, "profiles", os.path.dirname(PROFILE)))
    open(os.path.join(app, "wgp.py"), "w", encoding="utf-8").write(FAKE_WGP)
    json.dump({"num_inference_steps": 4, "guidance_scale": 1, "activated_loras": ["high.safetensors"]},
              open(os.path.join(app, "profiles", PROFILE), "w", encoding="utf-8"))
    res = videogen.run(dict(model="wan2.2-14b-lightning", prompt="a cat surfing", wangp_app_dir=app,
                            wangp_python=sys.executable, output_dir=os.path.join(tmp, "out_w"),
                            work_dir=os.path.join(tmp, "work"), preview=False))
    assert len(res["videos"]) == 1 and res["videos"][0].endswith("_fake.mp4")
    s = json.load(open(os.path.join(res["run_dir"], "wangp_settings.json"), encoding="utf-8"))
    # 프리셋 steps(30)가 아니라 Lightning 프로필의 4 step 이 남아야 한다 (사용자가 steps 를 적지 않았으므로)
    assert s["num_inference_steps"] == 4 and s["guidance_scale"] == 1, s
    assert s["resolution"] == "832x480" and s["video_length"] == 81 and s["model_type"] == "t2v_2_2", s
    log_text = open(res["log"], encoding="utf-8").read()
    assert "dry-run ok" in log_text and "[GENERATE]" in log_text and "saved" in log_text
    # 사용자가 steps 를 직접 적으면 그 값이 프로필보다 우선
    s2 = videogen.wangp_settings(videogen.make_config(model="wan2.2-14b-lightning", steps=8),
                                 videogen.resolve_params(videogen.make_config(steps=8)), app)
    assert s2["num_inference_steps"] == 8
    print("ok  wangp path (fake wgp.py):", res["videos"][0])
    return app


HQ = videogen.MODELS["wan2.2-14b-hq"]


def test_wangp_fhd(tmp, app):
    """hq 모델 + fhd_15s 두 단계 흐름 (작게: 256x144 → ×1.5 = 384x216, 14B 는 16 배수).
    1단계 T2V 81프레임 → 2단계 SVI 2 Pro 가 160프레임 이어 만들기(합친 241프레임 = 16fps 15.06초) → 업스케일.
    FlashVSR 성공 · 실패→Lanczos 대체 두 경우."""
    for rel, prof in ((HQ["profile"], {"num_inference_steps": 8, "guidance_scale": 3.5, "guidance_phases": 3, "help": "x"}),
                      (HQ["continue_with"]["profile"], {"num_inference_steps": 4, "guidance_scale": 1})):
        os.makedirs(os.path.join(app, "profiles", os.path.dirname(rel)), exist_ok=True)
        json.dump(prof, open(os.path.join(app, "profiles", rel), "w", encoding="utf-8"))
    # 회귀: v1.2.0 이 보낸 설정(T2V + "15s" + 창 81)은 가짜 WanGP 도 Kaggle 과 같은 오류로 거부해야 한다
    old = os.path.join(tmp, "old_v120.json")
    json.dump(dict(model_type="t2v_2_2", prompt="x", resolution="256x144", video_length="15s", seed=1,
                   sliding_window_size=81, sliding_window_overlap=5), open(old, "w", encoding="utf-8"))
    r = subprocess.run([sys.executable, "wgp.py", "--process", old, "--output-dir", tmp, "--dry-run"], cwd=app,
                       capture_output=True, encoding="utf-8", errors="replace")
    assert r.returncode == 1 and "Sliding Windows with a Text to Video model" in r.stdout, r.stdout
    for fail in ("0", "1"):
        os.environ["FAKE_FLASHVSR_FAIL"] = fail
        res = videogen.run(dict(model="wan2.2-14b-hq", preset="fhd_15s", prompt="an old man shouting on a sofa",
                                width=256, height=144, upscale_to="384x216", wangp_app_dir=app, wangp_python=sys.executable,
                                output_dir=os.path.join(tmp, f"out_fhd{fail}"), work_dir=os.path.join(tmp, "work"),
                                preview=False))
        s1 = json.load(open(os.path.join(res["run_dir"], "wangp_settings.json"), encoding="utf-8"))
        s2 = json.load(open(os.path.join(res["run_dir"], "wangp_continue.json"), encoding="utf-8"))
        assert s1["model_type"] == "t2v_2_2" and s1["video_length"] == 81 and s1["num_inference_steps"] == 8 and s1["resolution"] == "256x144", s1
        assert "sliding_window_size" not in s1 and "help" not in s1, s1
        meta = json.load(open(res["metadata"], encoding="utf-8"))
        assert meta["plan"] == {"total": 241, "first": 81, "cont": 160}, meta["plan"]
        assert s2["model_type"] == "i2v_2_2_svi2pro" and s2["image_prompt_type"] == "V" and s2["video_length"] == 160, s2
        assert s2["video_source"] == meta["segments"][0] and s2["num_inference_steps"] == 4, s2
        merged = videogen._video_info(meta["base_videos"][0])
        assert (merged["width"], merged["height"]) == (256, 144) and abs(merged["duration_sec"] - 241 / 16) < 0.1, merged
        want = "flashvsr" if fail == "0" else "lanczos"
        assert meta["upscale_methods"] == [want], meta["upscale_methods"]
        assert videogen._video_size(res["videos"][0]) == (384, 216) and res["videos"][0].endswith(f"_384x216_{want}.mp4")
        log_text = open(res["log"], encoding="utf-8").read()
        assert "[CONTINUE]" in log_text and "length plan" in log_text
        if fail == "1":
            assert "FlashVSR failed -> falling back to Lanczos" in log_text
        print(f"ok  wangp fhd two-stage flow (FlashVSR {'fails -> Lanczos' if fail == '1' else 'ok'}): "
              f"merged {merged['duration_sec']}s ->", res["videos"][0])
    os.environ.pop("FAKE_FLASHVSR_FAIL")
    # 짧으면(81프레임 이하) 이어 만들기 없이 한 단계
    short = videogen.wangp_plan(videogen.make_config(model="wan2.2-14b-hq", num_frames=81),
                                videogen.resolve_params(videogen.make_config(num_frames=81)))
    assert short == {"total": 81, "first": 81, "cont": None}, short


def test_start_images(tmp, app):
    """시작 이미지 3장 → 클립 3개(WanGP 한 번 실행에 작업 목록) → 이어 붙이기 → 업스케일(cover). 작게 돌린다:
    448x256(5B 는 32 배수) · 클립 0.5초(13프레임 @24fps) · 목표 480x270(비율 1.6% 차이 → ×1.5 뒤 가운데 자르기)."""
    from PIL import Image
    # 설정 검사
    expect_error(lambda: videogen.make_config(model="wan2.2-14b-i2v"), ValueError, "시작 이미지가 필요")
    expect_error(lambda: videogen.make_config(model="wan2.2-5b", start_images=["a.png"]), ValueError, "WanGP 모델에서만")
    expect_error(lambda: videogen.make_config(model="wan2.2-5b-fast", start_images=[{"prompt": "x"}]), ValueError,
                 "start_images[0]")
    videogen._setup_logging("INFO", os.path.join(tmp, "img_cfg.log"))
    # 15초 ÷ 3장 = 클립 5초: 5B(24fps) 121프레임 · 14B I2V(16fps) 81프레임. 5B 는 1280x720 → 32 배수 1280x704
    cfg = videogen.make_config(model="wan2.2-5b-fast", preset="fhd_15s", start_images=["a", "b", "c"])
    p = videogen.resolve_params(cfg, spatial_multiple=32)
    assert (p["width"], p["height"], p["upscale_fit"], p["upscale_factor"]) == (1280, 704, "cover", 2.0), p
    assert videogen.clip_frames_for(cfg, p, 3) == 121
    cfg14 = videogen.make_config(model="wan2.2-14b-i2v", preset="fhd_15s", start_images=["a", "b", "c"])
    assert videogen.clip_frames_for(cfg14, videogen.resolve_params(cfg14, spatial_multiple=16), 3) == 81

    img_dir = os.path.join(tmp, "imgs")
    os.makedirs(img_dir)
    sizes = {"wide.png": (1536, 1024), "square.png": (1024, 1024), "fhd.png": (1920, 1080)}
    for name, (w, h) in sizes.items():
        Image.new("RGB", (w, h), (200, 120, 60)).save(os.path.join(img_dir, name))
    res = videogen.run(dict(
        model="wan2.2-5b-fast", preset="fhd_15s", prompt="an old man shouting on a sofa", width=448, height=256,
        upscale_to="480x270", clip_sec=0.5, wangp_app_dir=app, wangp_python=sys.executable,
        start_images=[os.path.join(img_dir, "wide.png"),
                      {"image": os.path.join(img_dir, "square.png"), "prompt": "close-up of his angry face"},
                      "file://" + os.path.join(img_dir, "fhd.png")],
        output_dir=os.path.join(tmp, "out_img"), work_dir=os.path.join(tmp, "work"), preview=False))
    meta = json.load(open(res["metadata"], encoding="utf-8"))
    tasks = json.load(open(os.path.join(res["run_dir"], "wangp_settings.json"), encoding="utf-8"))
    assert isinstance(tasks, list) and len(tasks) == 3, tasks
    assert [t["seed"] for t in tasks] == [42, 43, 44] and {t["video_length"] for t in tasks} == {13}, tasks
    assert {t["model_type"] for t in tasks} == {"ti2v_2_2_fastwan"} and all(t["image_prompt_type"] == "S" for t in tasks)
    assert tasks[0]["prompt"] == "an old man shouting on a sofa" and tasks[1]["prompt"] == "close-up of his angry face"
    for t in tasks:
        with Image.open(t["image_start"]) as im:
            assert im.size == (448, 256), im.size
    assert meta["plan"]["clips"] == 3 and meta["plan"]["clip_frames"] == 13, meta["plan"]
    assert len(meta["segments"]) == 3
    joined = videogen._video_info(meta["base_videos"][0])
    assert (joined["width"], joined["height"]) == (448, 256) and abs(joined["duration_sec"] - 39 / 24) < 0.15, joined
    assert meta["upscale_methods"] == ["flashvsr"] and videogen._video_size(res["videos"][0]) == (480, 270)
    log_text = open(res["log"], encoding="utf-8").read()
    for needle in ("[IMAGES]", "clip plan", "[CONCAT]", "fitted to target", "more than 20% of the image was cropped"):
        assert needle in log_text, needle
    print("ok  start images: 3 clips in one WanGP run -> joined", joined["duration_sec"], "s ->", res["videos"][0])


class FakeGitHub:
    """GitHub Release API 흉내 (메모리). 네트워크 없음 — videogen._http 를 이것으로 바꿔 끼운다.
    fail_names: 그 이름 자산 올리기는 400 · flaky: 처음 한 번 502 (다시 시도 확인)."""

    def __init__(self, fail_names=(), flaky=False):
        self.releases, self.assets, self.next_id = {}, {}, 100
        self.calls, self.tokens, self.fail_names, self.flaky = [], set(), set(fail_names), flaky

    def _id(self):
        self.next_id += 1
        return self.next_id

    def _asset_json(self, a):
        return dict(id=a["id"], name=a["name"], url=f"https://api.github.com/repos/{a['repo']}/releases/assets/{a['id']}",
                    browser_download_url=f"https://github.com/{a['repo']}/releases/download/{a['tag']}/{a['name']}")

    def __call__(self, method, url, token, data=None, content_type=None, accept="application/vnd.github+json",
                 timeout=300):
        import re
        import urllib.parse
        self.calls.append((method, url))
        self.tokens.add(token)
        if self.flaky:
            self.flaky = False
            raise videogen._HTTPError(502, "bad gateway")
        u = urllib.parse.urlparse(url)
        q = urllib.parse.parse_qs(u.query)
        if u.netloc == "uploads.github.com" and method == "POST":
            rel_id = int(re.search(r"/releases/(\d+)/assets$", u.path).group(1))
            name = q["name"][0]
            if name in self.fail_names:
                raise videogen._HTTPError(400, "fake upload refused")
            if any(a["rel"] == rel_id and a["name"] == name for a in self.assets.values()):
                raise videogen._HTTPError(422, '{"errors":[{"code":"already_exists"}]}')
            rel = next(r for r in self.releases.values() if r["id"] == rel_id)
            a = dict(id=self._id(), name=name, rel=rel_id, repo=rel["repo"], tag=rel["tag_name"], data=data,
                     ctype=content_type)
            self.assets[a["id"]] = a
            return 201, json.dumps(self._asset_json(a)).encode()
        assert u.netloc == "api.github.com", url
        m = re.fullmatch(r"/repos/([^/]+/[^/]+)/releases/tags/(.+)", u.path)
        if m and method == "GET":
            if m.group(2) not in self.releases:
                raise videogen._HTTPError(404, '{"message":"Not Found"}')
            return 200, json.dumps(self.releases[m.group(2)]).encode()
        m = re.fullmatch(r"/repos/([^/]+/[^/]+)/releases", u.path)
        if m and method == "POST":
            p = json.loads(data)
            rel = dict(id=self._id(), tag_name=p["tag_name"], prerelease=p["prerelease"], repo=m.group(1),
                       html_url=f"https://github.com/{m.group(1)}/releases/tag/{p['tag_name']}")
            self.releases[p["tag_name"]] = rel
            return 201, json.dumps(rel).encode()
        m = re.fullmatch(r"/repos/[^/]+/[^/]+/releases/(\d+)/assets", u.path)
        if m and method == "GET":
            page, per = int(q["page"][0]), int(q["per_page"][0])
            mine = [self._asset_json(a) for a in self.assets.values() if a["rel"] == int(m.group(1))]
            return 200, json.dumps(mine[(page - 1) * per: page * per]).encode()
        m = re.fullmatch(r"/repos/[^/]+/[^/]+/releases/assets/(\d+)", u.path)
        if m and method == "DELETE":
            del self.assets[int(m.group(1))]
            return 204, b""
        if m and method == "GET":
            assert accept == "application/octet-stream", accept
            return 200, self.assets[int(m.group(1))]["data"]
        raise AssertionError(f"unexpected {method} {url}")

    def names(self, tag):
        rel = self.releases[tag]["id"]
        return sorted(a["name"] for a in self.assets.values() if a["rel"] == rel)

    def manifest(self, tag):
        rel = self.releases[tag]["id"]
        return json.loads(next(a["data"] for a in self.assets.values()
                               if a["rel"] == rel and a["name"] == videogen.MANIFEST_NAME))


def test_scene_clips(tmp, app):
    """v1.4.0 장면 클립: 항목마다 sec·name · image_base(상대 경로) · concat=False → clips/<이름>.mp4 + 목록 →
    가짜 GitHub Release 에 올림 (새로 만들기 · 같은 이름 바꿔 올리기 · 목록 합치기 · 실패는 경고만 · 토큰 없음).
    CLAUDE.md: 올릴 수 있는 도구 시험은 GITHUB_TOKEN 류 환경 변수를 지우고 가짜 저장소 이름으로 — _http 도 가짜."""
    from PIL import Image
    saved_env = {k: os.environ.pop(k) for k in list(os.environ) if "GITHUB" in k and "TOKEN" in k}
    real_http, real_sleep = videogen._http, videogen.time.sleep
    try:
        # 설정 검사
        mk = lambda items, **kw: videogen.make_config(model="wan2.2-5b-fast", start_images=items, **kw)  # noqa: E731
        expect_error(lambda: mk([{"image": "a", "secs": 2}]), ValueError, "알 수 없는 키 ['secs']")
        expect_error(lambda: mk([{"image": "a", "sec": 0}]), ValueError, "sec=0")
        expect_error(lambda: mk([{"image": "a", "sec": "3"}]), ValueError, "sec='3'")
        expect_error(lambda: mk([{"image": "a", "name": "L 01"}]), ValueError, "name='L 01'")
        expect_error(lambda: mk([{"image": "a", "name": "L01"}, {"image": "b", "name": "L01"}]), ValueError, "겹친다")
        expect_error(lambda: videogen.make_config(release_tag="clips-x"), ValueError, "start_images 가 비어")
        expect_error(lambda: mk(["a"], release_tag="clips x"), ValueError, "release_tag=")
        expect_error(lambda: mk(["a"], release_repo="no-slash"), ValueError, "release_repo=")
        cfg = mk([{"image": "a", "sec": 0.5}, {"image": "b", "sec": 0.25}, "c"], clip_sec=1.0)
        assert videogen.clip_frames_each(cfg, videogen.resolve_params(cfg, 32)) == [13, 5, 25]  # 24fps 4k+1
        cfg_url = mk(["scenes/L01.png", "https://x/y.png", "/abs/z.png"], image_base="https://raw.example/repo/abc123/")
        assert [videogen._image_source(cfg_url, s) for s in cfg_url.start_images] == \
            ["https://raw.example/repo/abc123/scenes/L01.png", "https://x/y.png", "/abs/z.png"]

        img_dir = os.path.join(tmp, "scene_imgs", "scenes")
        os.makedirs(img_dir)
        for i, (w, h) in enumerate([(1536, 1024), (1536, 1024), (1024, 1024)], 1):
            Image.new("RGB", (w, h), (60 * i, 120, 200)).save(os.path.join(img_dir, f"L0{i}.png"))
        gh = FakeGitHub(flaky=True)
        videogen._http = gh
        videogen.time.sleep = lambda s: None
        settings = dict(
            model="wan2.2-5b-fast", prompt="warm 2D animation, gentle natural motion", width=448, height=256,
            image_base=os.path.join(tmp, "scene_imgs"), concat=False, clip_sec=0.5, preview=False,
            wangp_app_dir=app, wangp_python=sys.executable, output_dir=os.path.join(tmp, "out_scene"),
            work_dir=os.path.join(tmp, "work"), release_tag="clips-fake-episode", release_repo="fake-owner/fake-repo",
            start_images=[{"image": "scenes/L01.png", "name": "L01", "sec": 0.5, "prompt": "he sighs"},
                          {"image": "scenes/L02.png", "name": "L02", "sec": 0.25},
                          {"image": "scenes/L03.png", "name": "L03"}])
        res = videogen.run(dict(settings))   # 토큰 없음 → 클립은 만들고 Release 는 경고만
        assert res["release"]["ok"] is False and res["release"]["error"] == "no GITHUB_TOKEN" and not gh.releases
        clip_dir = os.path.join(res["run_dir"], "clips")
        assert sorted(os.listdir(clip_dir)) == ["L01.mp4", "L02.mp4", "L03.mp4", "clips_manifest.json"]
        man = json.load(open(res["clips_manifest"], encoding="utf-8"))
        assert [c["name"] for c in man["clips"]] == ["L01", "L02", "L03"]
        assert [c["frames"] for c in man["clips"]] == [13, 5, 13] and [c["seed"] for c in man["clips"]] == [42, 43, 44]
        assert man["clips"][0]["prompt"] == "he sighs" and man["clips"][1]["prompt"] == settings["prompt"]
        for c, n in zip(man["clips"], (13, 5, 13)):
            assert (c["width"], c["height"]) == (448, 256) and abs(c["duration_sec"] - n / 24) < 0.1, c
        tasks = json.load(open(os.path.join(res["run_dir"], "wangp_settings.json"), encoding="utf-8"))
        assert [t["video_length"] for t in tasks] == [13, 5, 13], tasks

        os.environ["GITHUB_TOKEN"] = "fake-token-for-test"  # 가짜 값 (진짜 토큰은 위에서 지움)
        r1 = videogen.publish_release(res["clips_manifest"], "clips-fake-episode", "fake-owner/fake-repo")
        assert r1["ok"] and r1["uploaded"] == ["L01", "L02", "L03"], r1
        assert gh.releases["clips-fake-episode"]["prerelease"] is True and gh.tokens == {"fake-token-for-test"}
        assert gh.names("clips-fake-episode") == ["L01.mp4", "L02.mp4", "L03.mp4", "clips_manifest.json"]
        m1 = gh.manifest("clips-fake-episode")
        assert [c["name"] for c in m1["clips"]] == ["L01", "L02", "L03"] and m1["clips"][0]["release_url"].endswith(
            "/releases/download/clips-fake-episode/L01.mp4"), m1
        # 한 장면만 다시 만들어 올림 (L02) → 같은 이름 자산을 바꾸고, 목록은 셋 그대로 (L02 만 새 run_id)
        res2 = videogen.run(dict(settings, start_images=[{"image": "scenes/L02.png", "name": "L02", "sec": 0.5}],
                                 seed=7))
        assert res2["release"]["ok"], res2["release"]
        assert gh.names("clips-fake-episode") == ["L01.mp4", "L02.mp4", "L03.mp4", "clips_manifest.json"]
        m2 = {c["name"]: c for c in gh.manifest("clips-fake-episode")["clips"]}
        assert sorted(m2) == ["L01", "L02", "L03"] and m2["L02"]["seed"] == 7 and m2["L02"]["frames"] == 13, m2
        assert m2["L01"]["run_id"] == m1["clips"][0]["run_id"]
        assert any(m == "DELETE" for m, _ in gh.calls)
        # 올리기 실패(L03) → 경고만, 목록에서 L03 이 빠지고 나머지는 올라감
        gh.fail_names = {"L03.mp4"}
        r3 = videogen.publish_release(res["clips_manifest"], "clips-fake-episode", "fake-owner/fake-repo")
        assert r3["ok"] is False and r3["failed"] == ["L03"] and r3["uploaded"] == ["L01", "L02"], r3
        assert sorted(c["name"] for c in gh.manifest("clips-fake-episode")["clips"]) == ["L01", "L02"]
        log_text = open(res2["log"], encoding="utf-8").read() + open(res["log"], encoding="utf-8").read()
        for needle in ("[CLIPS]", "[RELEASE]", "replaced old asset", "GITHUB_TOKEN not found", "request failed, retrying"):
            assert needle in log_text, needle
        assert "fake-token-for-test" not in log_text  # 토큰 값은 로그에 남지 않음
        meta = json.load(open(res2["metadata"], encoding="utf-8"))
        assert "fake-token-for-test" not in json.dumps(meta) and meta["release"]["ok"] is True
        print("ok  scene clips: per-clip sec/name -> clips/ + manifest -> fake Release (create, replace, merge, fail)")
    finally:
        videogen._http, videogen.time.sleep = real_http, real_sleep
        os.environ.pop("GITHUB_TOKEN", None)
        os.environ.update(saved_env)


def test_diffusers_frame_limit(tmp):
    """diffusers 5B 로 15초(361프레임)를 한 번에 만들려 하면 생성 전에 멈추고 hq 모델을 알려 준다."""
    if not all(importlib.util.find_spec(m) for m in ("torch", "diffusers", "transformers")):
        print("skip diffusers frame-limit test")
        return
    model_dir = os.path.join(tmp, "tiny-wan22-ti2v")  # test_diffusers 가 만든 것
    expect_error(lambda: videogen.run(dict(model="wan2.2-5b", model_path=model_dir, device_plan="cpu", duration_sec=15,
                                           height=64, width=64, output_dir=os.path.join(tmp, "out_lim"),
                                           work_dir=os.path.join(tmp, "work"), preview=False, install_deps=False)),
                 ValueError, "wan2.2-14b-hq")
    print("ok  diffusers 121-frame limit")


def test_upscale_file_rejoin(tmp):
    """v1.3.0 이 로캘 문제로 24fps 클립들을 16fps 로 이어 붙인 결과 폴더를 흉내 → upscale_file 이 media/ 클립으로 다시
    이어 붙여(24fps) 키운다. 또 _ffmpeg_concat 이 클립 fps 를 못 읽으면 모델 fps(경고) · 그것도 없으면 멈춘다."""
    ff = videogen._ffmpeg_exe()
    run_dir = os.path.join(tmp, "rejoin", "20261019-0300")
    os.makedirs(os.path.join(run_dir, "media"))
    clips = []
    for i, color in enumerate(("red", "green", "blue")):
        c = os.path.join(run_dir, "media", f"ti2v_2_2_fastwan_seed{42 + i}_fake.mp4")
        subprocess.run([ff, "-y", "-loglevel", "error", "-f", "lavfi", "-i", f"color=c={color}:s=176x320:d=1:r=24",
                        "-c:v", "libx264", "-pix_fmt", "yuv420p", c], check=True)
        clips.append(c)
        os.utime(c, (1e9 + i, 1e9 + i))  # 만든 순서 = mtime 순서
    joined = os.path.join(run_dir, "wan2.2-5b-fast_20261019-0300_3clips.mp4")
    chains = "".join(f"[{i}:v]fps=16[v{i}];" for i in range(3))
    subprocess.run([ff, "-y", "-loglevel", "error", "-i", clips[0], "-i", clips[1], "-i", clips[2], "-filter_complex",
                    chains + "[v0][v1][v2]concat=n=3:v=1:a=0[v]", "-map", "[v]", "-c:v", "libx264", "-pix_fmt", "yuv420p",
                    joined], check=True)
    assert videogen._video_info(joined)["fps"] == 16.0
    videogen._setup_logging("INFO", os.path.join(tmp, "rejoin.log"))
    out = videogen.upscale_file(run_dir, "270x480")
    info = videogen._video_info(out)
    assert (info["width"], info["height"], info["fps"]) == (270, 480, 24.0) and abs(info["duration_sec"] - 3) < 0.1, info
    assert videogen._video_info(joined)["fps"] == 24.0
    log_text = open(os.path.join(tmp, "rejoin.log"), encoding="utf-8").read()
    assert "re-joining clips" in log_text and "joined_fps=16 clip_fps=24" in log_text, log_text[-800:]
    # 클립 fps 를 못 읽을 때
    dst = os.path.join(tmp, "rejoin", "model_fps.mp4")
    info_fn, videogen._video_info = videogen._video_info, lambda path: {}
    try:
        videogen._ffmpeg_concat(clips, dst, 176, 320, fps=24)
        expect_error(lambda: videogen._ffmpeg_concat(clips, dst, 176, 320), RuntimeError, "fps 를 읽지 못함")
    finally:
        videogen._video_info = info_fn
    assert videogen._video_info(dst)["fps"] == 24.0
    assert "clip fps not readable -> using model fps" in open(os.path.join(tmp, "rejoin.log"), encoding="utf-8").read()
    print("ok  upscale_file: 16fps joined file re-joined from clips at", info["fps"], "fps ->", out)


ZH_NEG = "色调艳丽，过曝，静态，细节模糊不清，字幕"  # Wan 기본 부정 프롬프트 앞부분 — WanGP 가 결과 mp4 comment 에 넣는다


def _ascii_locale_body(tmp):
    """test_ascii_locale 이 ASCII 로캘 하위 프로세스에서 부르는 본문 (Kaggle 커널 로캘이 UTF-8 이 아닐 때를 흉내)."""
    import locale
    import shutil
    from PIL import Image
    enc = locale.getpreferredencoding(False)
    assert enc.lower().replace("-", "") in ("ansi_x3.41968", "ascii", "usascii"), f"locale is not ASCII: {enc}"
    videogen._setup_logging("INFO", os.path.join(tmp, "ascii.log"))
    zh = os.path.join(tmp, "zh.mp4")  # test_ascii_locale 이 UTF-8 쪽에서 만들어 둔 것 (WanGP 도 UTF-8 하위 프로세스에서 씀)
    # 재현: v1.3.0 이 쓰던 방식(text=True → 로캘 인코딩)은 여기서 UnicodeDecodeError — 이 환경이 버그를 재현하는지 확인
    try:
        subprocess.run([videogen._ffmpeg_exe(), "-hide_banner", "-i", zh], capture_output=True, text=True)
        raise AssertionError("v1.3.0-style ffmpeg read did not fail — ASCII locale not reproduced")
    except UnicodeDecodeError:
        pass
    # 수정: ffprobe 길 · ffmpeg 길 둘 다 크기를 읽는다
    assert videogen._video_size(zh) == (176, 320), videogen._video_info(zh)
    probe, videogen._ffprobe_exe = videogen._ffprobe_exe, lambda: None
    try:
        info = videogen._video_info(zh)
        assert (info.get("width"), info.get("height")) == (176, 320) and info.get("fps") == 24.0, info
    finally:
        videogen._ffprobe_exe = probe
    # _check_size: 같으면 통과 · 다르면 멈춤 · 못 읽으면 경고만
    videogen._check_size(zh, 176, 320)
    expect_error(lambda: videogen._check_size(zh, 100, 100), RuntimeError, "176x320 != 100x100")
    size, videogen._video_size = videogen._video_size, lambda path: None
    try:
        videogen._check_size(zh, 176, 320)
    finally:
        videogen._video_size = size
    assert "output size not verified" in open(os.path.join(tmp, "ascii.log"), encoding="utf-8").read()
    # upscale_file: 결과 폴더를 주면 '…clips.mp4' 를 골라 생성 없이 키운다 (사용자 복구 길). 176x320 → 270x480 = cover
    run_dir = os.path.join(tmp, "20261019-0300")
    os.makedirs(os.path.join(run_dir, "media"))
    shutil.copy(zh, os.path.join(run_dir, "media", "clip1.mp4"))
    shutil.copy(zh, os.path.join(run_dir, "t2v_seed42_3clips.mp4"))
    out = videogen.upscale_file(run_dir, "270x480")
    assert out == os.path.join(run_dir, "t2v_seed42_3clips_270x480_lanczos.mp4") and videogen._video_size(out) == (270, 480), out
    tags = subprocess.run([videogen._ffprobe_exe(), "-v", "error", "-show_entries", "format_tags", "-of", "json", out],
                          capture_output=True, encoding="utf-8").stdout
    assert "色调" not in tags, tags  # -map_metadata -1: 결과에는 중국어 메타데이터를 남기지 않는다
    # _stream: 하위 프로세스가 한·중 글자를 찍어도 죽지 않고 로그에 남는다
    lf = os.path.join(tmp, "stream.log")
    rc = videogen._stream([sys.executable, "-c", "print('\\u8272\\u8c03 \\ud560\\uc544\\ubc84\\uc9c0 saved')"], tmp, lf, "TEST")
    assert rc == 0 and "色调 할아버지 saved" in open(lf, encoding="utf-8").read()
    # 사용자 흐름 그대로: 시작 이미지 3장 → 클립(중국어 메타데이터) → 이어 붙이기 → Lanczos cover 업스케일
    app = test_wangp(tmp)
    img = os.path.join(tmp, "s.png")
    Image.new("RGB", (1024, 1536), (90, 60, 40)).save(img)  # ChatGPT 세로 그림 크기
    # 352x640 → 540x960 = 사용자 설정 704x1280 → 1080x1920 의 절반 (비율 2.3% 차이 → cover)
    res = videogen.run(dict(model="wan2.2-5b-fast", prompt="an old man on a sofa", width=352, height=640,
                            upscale_to="540x960", upscaler="lanczos", clip_sec=0.5, start_images=[img, img, img],
                            wangp_app_dir=app, wangp_python=sys.executable, output_dir=os.path.join(tmp, "out_ascii"),
                            work_dir=os.path.join(tmp, "work"), preview=False))
    assert videogen._video_size(res["videos"][0]) == (540, 960) and res["videos"][0].endswith("_540x960_lanczos.mp4"), res
    print("ok  ASCII locale: ffprobe/ffmpeg size read · check_size · upscale_file · stream · start-images run ->",
          res["videos"][0])


def test_ascii_locale(tmp):
    """회귀 (2026-10-19 Kaggle 'RuntimeError: 업스케일 결과 크기 None != 1080x1920'): 로캘이 ASCII 인 커널에서
    WanGP 결과 mp4 의 중국어 메타데이터 때문에 크기를 못 읽던 문제. 하위 프로세스를 LC_ALL=C · UTF-8 모드 끔으로
    띄워(표준 출력만 UTF-8 = Jupyter 처럼) 위 본문을 돌린다."""
    sub = os.path.join(tmp, "ascii")
    os.makedirs(sub)
    # 176x320 = 704x1280 의 1/4 (사용자 클립과 같은 비율), comment 에 중국어 — ASCII 쪽에서는 인자로 못 넘겨 여기서 만든다
    subprocess.run([videogen._ffmpeg_exe(), "-y", "-loglevel", "error", "-f", "lavfi", "-i", "color=c=gray:s=176x320:d=1:r=24",
                    "-metadata", "comment=" + ZH_NEG, "-c:v", "libx264", "-pix_fmt", "yuv420p", os.path.join(sub, "zh.mp4")],
                   check=True)
    env = {k: v for k, v in os.environ.items() if k not in ("PYTHONUTF8", "LC_CTYPE", "LANGUAGE")}
    env.update(LC_ALL="C", LANG="C", PYTHONCOERCECLOCALE="0", PYTHONIOENCODING="utf-8")
    r = subprocess.run([sys.executable, "-X", "utf8=0", os.path.abspath(__file__), "--ascii-body", sub], env=env,
                       capture_output=True, encoding="utf-8", errors="replace")
    sys.stdout.write("".join(f"    | {ln}\n" for ln in r.stdout.splitlines() if ln.startswith("ok ")))
    assert r.returncode == 0, (r.stdout[-3000:], r.stderr[-3000:])
    print("ok  ASCII-locale regression (subprocess)")


def main():
    tmp = tempfile.mkdtemp(prefix="videogen_test_")
    test_config(tmp)
    test_fhd_params(tmp)
    test_old_torchao(tmp)
    test_diffusers(tmp)
    test_diffusers_frame_limit(tmp)
    app = test_wangp(tmp)
    test_wangp_fhd(tmp, app)
    test_start_images(tmp, app)
    test_scene_clips(tmp, app)
    test_upscale_file_rejoin(tmp)
    test_ascii_locale(tmp)
    print("ALL TESTS PASSED", tmp)


if __name__ == "__main__":
    if sys.argv[1:2] == ["--ascii-body"]:
        _ascii_locale_body(sys.argv[2])
    else:
        main()
