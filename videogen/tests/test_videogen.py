# -*- coding: utf-8 -*-
# VERSION: v1.1.0 — 2026-10-18 — videogen.py 오프라인 시험 (GPU·네트워크 없이)
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
    assert "adjusted" in open(os.path.join(tmp, "cfg.log")).read()
    env = videogen._child_env()
    assert "PYTHONPATH" not in env and env["MPLBACKEND"] == "Agg"
    print("ok  config / helpers")


def build_tiny_wan(path):
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
    meta = json.load(open(res["metadata"]))
    fs = meta["frame_stats"]
    assert (fs["frames"], fs["height"], fs["width"]) == (9, 64, 128) and fs["finite"], fs
    assert os.path.getsize(res["videos"][0]) > 0 and meta["config"]["seed"] == 42
    assert len(meta["code_sha256"]) == 64 and meta["videogen_version"] == videogen.__version__
    text = open(res["log"]).read()
    for tag in ("[CONFIG]", "[SETUP]", "[DATA]", "[ENCODE]", "[DENOISE]", "[DECODE]", "[EXPORT]", "[SUMMARY]"):
        assert tag in text, tag
    print("ok  diffusers path (tiny model, CPU):", res["videos"][0])


FAKE_WGP = textwrap.dedent('''
    import argparse, json, os, sys
    ap = argparse.ArgumentParser()
    ap.add_argument("--process"); ap.add_argument("--output-dir"); ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--profile"); ap.add_argument("--attention"); ap.add_argument("--gpu")
    a = ap.parse_args()
    s = json.load(open(a.process))
    assert s["model_type"] and s["prompt"], s
    if a.dry_run:
        print(f"  Task 1: model={s['model_type']}, steps={s.get('num_inference_steps')}, frames={s['video_length']}")
        print("[DRY-RUN] Validation complete. 1/1 task(s) valid."); sys.exit(0)
    for i in range(1, 5):
        print(f" {i * 25}%|##| {i}/4 [00:0{i}<00:00, 1.00s/it]", flush=True)
    path = os.path.join(a.output_dir, "2026-10-18-12h00m00s_seed42_fake.mp4")
    open(path, "wb").write(b"\\x00" * 2048)
    print("New video saved to Path: " + path)
''')


def test_wangp(tmp):
    app = os.path.join(tmp, "Wan2GP")
    os.makedirs(os.path.join(app, "profiles", os.path.dirname(PROFILE)))
    open(os.path.join(app, "wgp.py"), "w").write(FAKE_WGP)
    json.dump({"num_inference_steps": 4, "guidance_scale": 1, "activated_loras": ["high.safetensors"]},
              open(os.path.join(app, "profiles", PROFILE), "w"))
    res = videogen.run(dict(model="wan2.2-14b-lightning", prompt="a cat surfing", wangp_app_dir=app,
                            wangp_python=sys.executable, output_dir=os.path.join(tmp, "out_w"),
                            work_dir=os.path.join(tmp, "work"), preview=False))
    assert len(res["videos"]) == 1 and res["videos"][0].endswith("_fake.mp4")
    s = json.load(open(os.path.join(res["run_dir"], "wangp_settings.json")))
    # 프리셋 steps(30)가 아니라 Lightning 프로필의 4 step 이 남아야 한다 (사용자가 steps 를 적지 않았으므로)
    assert s["num_inference_steps"] == 4 and s["guidance_scale"] == 1, s
    assert s["resolution"] == "832x480" and s["video_length"] == 81 and s["model_type"] == "t2v_2_2", s
    log_text = open(res["log"]).read()
    assert "dry-run ok" in log_text and "[GENERATE]" in log_text and "saved" in log_text
    # 사용자가 steps 를 직접 적으면 그 값이 프로필보다 우선
    s2 = videogen.wangp_settings(videogen.make_config(model="wan2.2-14b-lightning", steps=8),
                                 videogen.resolve_params(videogen.make_config(steps=8)), app)
    assert s2["num_inference_steps"] == 8
    print("ok  wangp path (fake wgp.py):", res["videos"][0])


def main():
    tmp = tempfile.mkdtemp(prefix="videogen_test_")
    test_config(tmp)
    test_diffusers(tmp)
    test_wangp(tmp)
    print("ALL TESTS PASSED", tmp)


if __name__ == "__main__":
    main()
