# CHANGELOG — videogen

## v1.3.1 — 2026-10-19
### 왜 (사용자 보고)
- "RuntimeError: 업스케일 결과 크기 None != 1080x1920" — 기초연금 AI 쇼츠 테스트(`wan2.2-5b-fast` · 장면 11장 · 704x1280 → 1080x1920 Lanczos) 실행 끝에서.

### 원인 (재현함)
- `_video_info()` 가 ffmpeg 정보 출력을 `text=True`(로캘 인코딩)로 읽었다. Kaggle 커널 로캘이 UTF-8 이 아니면(ASCII) WanGP 가 결과 mp4 메타데이터(comment)에 넣은 설정 — Wan 기본 부정 프롬프트는 중국어 — 에서 `UnicodeDecodeError` → 예외를 삼키고 `{}` → 크기 `None` → `업스케일 결과 크기 None`.
- 같은 원인의 **조용한 피해**: `_ffmpeg_concat()` 이 첫 클립 fps 를 못 읽으면 몰래 `16` 을 썼다. 5B 클립은 24fps → 이어 붙인 영상이 16fps(프레임 1/3 버림, 길이는 같음). 재현: 24fps 39프레임 → 16fps 27프레임.
- 재현 환경: 하위 프로세스 `LC_ALL=C LANG=C PYTHONCOERCECLOCALE=0 python -X utf8=0` (표준 출력만 UTF-8 = Jupyter 처럼). v1.3.0 은 이 환경에서 `RuntimeError: 업스케일 결과 크기 None != 540x960` 로 똑같이 멈춤.

### 한 것
| 대상 | 내용 |
|---|---|
| 모든 `subprocess.run/Popen` | `text=True` → `encoding="utf-8", errors="replace"` (로캘과 상관없이) |
| `_child_env()` | `PYTHONUTF8=1` · `PYTHONIOENCODING=utf-8` — WanGP 가 한·중 글자를 찍거나 쓸 때 로캘 때문에 죽지 않게 |
| `_ffprobe_exe()` (새) · `_video_info()` | ffprobe JSON(가로·세로·길이·fps) 먼저, 없거나 실패하면 ffmpeg 정보 출력. 크기를 못 읽으면 경고 `could not parse video size` + ffmpeg 끝 줄 |
| `_check_size()` (새) | 업스케일 결과 크기: 다르면 멈춤 · 못 읽으면 경고 `output size not verified` 만 (ffmpeg scale 이 크기를 정하므로 '못 읽음' ≠ 실패) |
| `_ffmpeg_upscale()` · `_ffmpeg_concat()` | `-map_metadata -1` — 결과 파일에 WanGP 메타데이터를 옮기지 않음 |
| `_ffmpeg_concat()` | fps: 첫 클립 → 못 읽으면 모델 fps(`MODELS[...]["fps"]`, 경고) → 둘 다 없으면 멈춤. 로그 `[CONCAT] encode ... fps= source=` |
| `upscale_file()` (새, 공개) | 생성 없이 다시 키우기: 파일 또는 결과 폴더. 폴더면 `…<N>clips.mp4`(없으면 `media/` 최근 영상). 이어 붙인 파일 fps 가 `media/` 클립 N개와 다르면 클립으로 다시 이어 붙인 뒤 Lanczos (`rejoin=True`) |
| `tests/test_videogen.py` v1.3.1 | `test_ascii_locale`(위 재현 환경에서: v1.3.0 방식 실패 확인 → ffprobe·ffmpeg 두 길 · `_check_size` · `upscale_file` · `_stream` · 시작 이미지 3장 → Lanczos cover 흐름) · `test_upscale_file_rejoin`(16fps 이어 붙인 폴더 → 24fps · fps 못 읽을 때) · 가짜 WanGP 가 결과 mp4 에 중국어 메타데이터 · 시험 파일 읽기·쓰기 UTF-8 고정 |
| `README.md` | 2-3번(다시 생성하지 않고 마무리하는 셀) · 문제 해결 두 줄 · 검증 범위 |

### 측정
- 시험 전체 28초 (클라우드 CPU, 10묶음 통과). 실행 속도에 영향 없음 — ffprobe 한 번이 ffmpeg 정보 출력 한 번을 대신(파일마다 수십 ms).

### 위험 관련 변경
- 없음 (생성 설정·업스케일 배율 그대로). 동작 변경 둘: 크기를 **못 읽을** 때 멈추지 않고 경고 · 이어 붙이기 fps 를 몰래 16 으로 하지 않음.

## v1.3.0 — 2026-10-18
### 왜 (사용자 지시)
- "3개 영상 나왔는데 2시간 걸렸어 너무 오래걸리는데 빠르게 생성하는 방법 없어? 시작 이미지를 전달하면 더 빨리 할 수 있어? 시작 이미지 여러개 만들어서 짧게 짧게 각각 만드는거지"
- v1.2.1 hq 는 Kaggle 에서 끝까지 돌았다 (영상 3개 = 첫 5초 조각 · 합친 15초 720p · 1080p 최종).

### 짚은 점
- 시작 이미지가 있다고 프레임당 계산이 줄지는 않는다 (같은 크기 모델이면 같음). 빨라지는 까닭은 ① 장면을 이미지가 정해 5B 3-step 같은 가벼운 모델로도 일관됨 ② T2V 단계가 없어 모델 하나만 받고 불러옴 ③ 클립들을 WanGP 한 번 실행에 작업 목록으로 넘겨 모델을 한 번만 불러옴.
- 계산량 추정(모델 크기·토큰 수·step 수): hq 15초 ≈ 14B 720p 21번(한 번 ≈ 6.8e15 FLOP) → T4 약 1.5시간 — 사용자 실측(설치 포함 약 2시간)과 대략 맞음. 5B FastWan 이미지 3장 × 5초 ≈ 5B 1280x704 9번(한 번 ≈ 5.5e14) → hq 의 약 3~4%. **실측 아님**.

### 한 것
| 대상 | 내용 |
|---|---|
| `Config` | 새 설정 `start_images`(경로·URL 또는 `{"image", "prompt"}`) · `clip_sec` · `concat` |
| `MODELS` | 새 모델 `wan2.2-5b-fast`(TI2V 5B + FastWan 3-step, WanGP `ti2v_2_2_fastwan`, 24fps, 32 배수) · `wan2.2-14b-i2v`(I2V 14B + Lightning i2v 2-phase 4-step, 시작 이미지 필요). Wan 모델에 `block`(해상도 배수) |
| `prepare_start_images()` (새) | URL 은 받고(비공개 저장소면 Kaggle Secret `GITHUB_TOKEN`), 생성 해상도 비율로 가운데를 잘라 정확히 그 크기 PNG 로 (WanGP 는 시작 이미지 비율을 결과 비율로 따름). 잘린 비율 로그, 20% 넘으면 경고 |
| `clip_frames_for()` · `wangp_image_tasks()` (새) | 클립 길이 = `clip_sec` > `duration_sec` ÷ 이미지 수 > 모델 기본 5초. 이미지마다 작업 하나(`image_prompt_type S`, seed 42·43·44…) → **목록 하나로 WanGP 한 번 실행** |
| `_ffmpeg_concat()` (새) | 클립들을 순서대로 이어 한 영상 (컷 전환), 크기·fps 를 맞춰 다시 인코딩 |
| `upscale_plan()` (← `upscale_factor`) | 정확한 배율이 아니어도 비율 차이 3% 이하면 목표를 덮는 가장 작은 배율로 키운 뒤 가운데 자르기(cover) — 5B 1280x704 → ×2 → 1920x1080 (가로 약 2.3% 잘림). 그보다 다르면 멈춤 |
| `_upscale_video()` | FlashVSR 결과가 목표를 덮으면 cover 로 맞춤, Lanczos 대체도 cover |
| `_wangp_generate()` | `resolve_params(spatial_multiple=block)` — WanGP 가 몰래 내리기 전에 블록 배수로 맞추고 전·후 로그 (이전의 16 배수 경고 대신). `[IMAGES]` · `clip plan` · `[CONCAT]` 단계 |
| `_wangp_process()` | 작업 하나 또는 목록, 결과는 저장 순서(mtime)대로 |
| `tests/test_videogen.py` | `test_start_images`(3장: 가로·정사각·`file://` URL → 작업 목록 1회 → 이어 붙이기 → cover 업스케일) · `upscale_plan` 시험 · 가짜 WanGP 가 작업 목록·시작 이미지(크기 = 해상도 확인) 처리 · hq 시험 해상도를 16 배수(256x144)로 |
| `README.md` | 2-2번(이유·시간 추정 표·ChatGPT 이미지 프롬프트 3장·이미지 올리는 법·`SETTINGS`) · 설정 키 · 모델 · 문제 해결 |

### 위험 관련 변경
- 없음. 기존 모델은 해상도가 이미 블록 배수면 그대로 (hq 1280x720, lightning 832x480).

## v1.2.1 — 2026-10-18
### 왜 (사용자 보고)
- "해결해 에러 났어" + Kaggle `wangp_process.log`:
  `[ERROR] You have requested to Generate Sliding Windows with a Text to Video model. Unless you use the Video to Video feature this is useless as a t2v model doesn't see past frames and it will generate the same video in each new window.`

### 원인
- v1.2.0 의 `wan2.2-14b-hq` 는 T2V 모델(`t2v_2_2`)에 창 이어붙이기(81프레임 창)로 15초(241프레임)를 만들게 했다. WanGP(`wgp.py:1549`)는 T2V 모델에서 창 이어붙이기를 막는다 — T2V 는 앞 창을 보지 못해 창마다 같은 영상이 나오기 때문. 내 판단 잘못(모델 정의의 `sliding_window` 표시만 보고 T2V 도 이어진다고 봄).
- 생성 전 검증(`--dry-run`)에서 멈춰 몇 시간 생성은 낭비되지 않았다. 설치·`15s` → 241프레임 변환은 정상이었다.

### 한 것
| 대상 | 내용 |
|---|---|
| `MODELS["wan2.2-14b-hq"]` | 두 단계로: ① T2V 14B + Lightning 8-step 3-phase 로 첫 `first_frames=81` ② 길면 `continue_with` = **SVI 2 Pro**(`i2v_2_2_svi2pro` — Wan2.2 I2V 14B + Stable Video Infinity LoRA, WanGP 설명 "potentially unlimited Videos to Continue") + Lightning i2v 2-phase 4-step(SVI LoRA 의 2-phase 형식과 맞춤). 창 이어붙이기 설정(`extra`) 제거. FP8 가중치 판(Enhanced Lightning)은 T4 에서 불확실해 쓰지 않음 |
| `wangp_plan()` (새) | 길이 계획 — 15초 × 16fps → 241, 첫 81 + 이어 만들기 160 |
| `wangp_continue_settings()` (새) | `image_prompt_type: "V"` + `video_source` = ①의 영상, `video_length` = 새 프레임 수 (WanGP: 결과는 원본 + 새 프레임을 합친 한 파일) |
| `_wangp_process()` (새) | 설정 저장 → `--dry-run` → `--process` → 결과 수집을 단계마다 같은 방식으로. 실패하면 **WanGP 의 마지막 오류 줄을 예외 문장에 바로** 붙임 |
| `_wangp_generate()` | `[SETUP] length plan` 로그 · `[CONTINUE]` 단계 · ①의 영상은 `segments` 로 남김 · 디스크 추정치 경고(80GB) · 16 배수 아닌 해상도 경고 |
| `_video_info()` (새) | 가로·세로·길이·fps (ffmpeg) — 결과 파일마다 로그 |
| `tests/test_videogen.py` | 가짜 WanGP 가 **실제 T2V 거부 규칙을 흉내** → v1.2.0 설정이 같은 오류로 거부되는지(회귀) · 두 단계 설정 · 합친 영상 241프레임(16fps 15.06초) · 업스케일 확인 |
| `README.md` | 2-1번 설명(두 단계·시간·디스크) · 빠르게 하는 방법 고침(옛 안내 '4-step 모델 + 창 이어붙이기'도 같은 오류) · 문제 해결 표 |

### 위험 관련 변경
- 없음. 다른 모델·프리셋 동작은 그대로.

## v1.2.0 — 2026-10-18
### 왜 (사용자 지시)
- "좀 고품질의 1920, 1080 해상도로 할아버지가 소파에 앉아서 호통치는 영상으로 15초 정도로 생성하는 설정, 프롬프트로 변경해줘"

### 짚은 점 (바꾸기 전에)
- Kaggle T4 에서 1920x1080·15초를 한 번에 만들 수는 없다: Wan 계열은 약 5초(81~121프레임) 길이로 학습됐고, 1080p·15초를 한 번에 만들면 계산량이 수십 배가 된다 (diffusers 5B 로는 361프레임 = 학습 길이의 3배).
- 그래서 **1280x720 으로 15초(81프레임 창 이어붙이기) → ×1.5 업스케일 = 1920x1080**.

### 한 것
| 대상 | 내용 |
|---|---|
| `MODELS["wan2.2-14b-hq"]` (새) | Wan2.2 T2V 14B + Lightning **8-step 3-phase**(v2025-12-17 — WanGP 설명: 가속 LoRA 앞에 CFG 단계를 넣어 슬로모션 줄임) + `sliding_window_size=81`·`overlap=5` |
| `PRESETS["fhd_15s"]` (새) | 1280x720 · `duration_sec=15` · `upscale_to="1920x1080"` |
| `Config` | 새 설정 `duration_sec`(길이 — WanGP 에는 `"15s"` 로 넘겨 모델 fps 로 프레임 수를 고르게) · `upscale_to` · `upscaler`(flashvsr \| lanczos) |
| `resolve_params()` | 길이 우선순위(직접 duration > 직접 num_frames > 프리셋), diffusers 는 fps 로 프레임 수 계산, 업스케일 배율 확인 |
| `upscale_factor()` (새) | 가로세로 같은 배율이고 1.5·2·…·4 중 하나여야 함. 아니면 그 목표에 맞는 생성 해상도를 알려 주고 멈춤 (늘이거나 자르지 않음) |
| `_upscale_video()` (새) | WanGP 후처리 작업(`mode: edit_postprocessing`, `spatial_upsampling: flashvsr*1.5`) → 결과 크기를 ffmpeg 로 확인 → 실패하거나 크기가 다르면 경고 로그 후 **ffmpeg Lanczos** 로 대신. 생성 원본은 `base_videos` 로 남김 |
| `_diffusers_generate()` | 121프레임(5초)을 넘으면 생성 전에 멈추고 `wan2.2-14b-hq` 를 안내 · `upscale_to` 면 Lanczos |
| `wangp_settings()` | 길이 `"15s"` · 모델 고정값(`extra`) 합치기 · 프로필의 UI 안내 키 `help` 는 뺌 |
| `run()` SUMMARY | 최종 파일마다 해상도·크기, 업스케일 전 원본 경로 |
| `tests/test_videogen.py` | `test_fhd_params` · `test_wangp_fhd`(가짜 WanGP 가 작은 진짜 mp4 생성 → FlashVSR 성공 / 실패→Lanczos, 최종 96x54·원본 64x36 확인) · `test_diffusers_frame_limit` |
| `README.md` | 2-1번 예시(할아버지 호통 프롬프트) · 설정 키 · 모델 · 문제 해결 |

### 위험 관련 변경
- 없음. 기존 모델·프리셋의 동작은 그대로 (창 이어붙이기 설정은 새 모델에만).

## v1.1.1 — 2026-10-18
### 왜 (사용자 보고)
- Kaggle 실행 중 `RuntimeError: Failed to import diffusers.models.autoencoders.autoencoder_kl_wan ... cannot import name 'FqnToConfig' from 'torchao.quantization' (/usr/local/lib/python3.13/dist-packages/torchao/...) 해결해`

### 원인
- diffusers 0.41.0 의 `quantizers/torchao/torchao_quantizer.py` 는 torchao 가 **깔려 있기만 하면** `from torchao.quantization import FqnToConfig` 를 실행한다 (diffusers 가 요구하는 torchao 는 0.15.0 이상). Kaggle 이미지(Python 3.13)에 미리 깔린 torchao 는 그보다 오래돼 `FqnToConfig` 가 없다 → 모든 diffusers 모델 import 실패. videogen 은 torchao(양자화)를 쓰지 않는다.
- 재현: torchao 0.13.0 + diffusers 0.41.0 에서 같은 오류 (이 저장소 클라우드 환경).

### 한 것
| 대상 | 내용 |
|---|---|
| `_disable_old_torchao()` (새 함수) | torchao 가 0.15 미만이면 경고 로그(버전·요구 버전) → Kaggle 에서는 `pip uninstall -y torchao`(이번 세션만, 다음 세션은 Kaggle 이 다시 깖) → diffusers 가 import 때 기억해 둔 'torchao 있음' 표시(`_torchao_available`)를 끄고 꺼졌는지 확인. 앞 실행이 실패한 같은 커널에서 셀을 다시 실행해도 **커널 재시작 없이** 된다 |
| `run()` | diffusers 길에서 패키지 확인 뒤 `_disable_old_torchao()` 호출. Kaggle 밖(내 PC 등)에서는 패키지를 지우지 않고 표시만 끈다 |
| `tests/test_videogen.py` | `test_old_torchao` — 같은 커널에서 '첫 import 실패 → 수정 → 다시 import' 순서를 그대로 재현. 결과: 오래된 torchao(표시만 끔) · Kaggle 길(지움, `VIDEOGEN_TEST_UNINSTALL=1`) · torchao 없음 세 경우 모두 통과 |

### 위험 관련 변경
- 없음 (생성 파라미터 그대로).

## v1.1.0 — 2026-10-18
### 왜 (사용자 지시)
- "핵심 코드를 하나로 만들어서 저장소에 올리고 kaggle에서는 코드 받아서 실행하는 방식으로 하고 prompt 같은 설정만 고치고 실행만 하는 코드를 따로 알려줘"

### 한 것
| 대상 | 내용 |
|---|---|
| `videogen/videogen.py` (새 파일) | v1.0.0 노트북 2개(diffusers 헤드리스 · WanGP 웹 UI)의 핵심을 파일 하나로. `run(SETTINGS)` 한 번으로 실행, `model` 키로 실행 방식 자동 선택 (`MODELS`) |
| `make_config()` | 모르는 설정 키·모델·프리셋이면 바로 멈춤 (오타 방지) |
| `_diffusers_generate()` | v1.0.0 노트북 A 그대로 (단계별로 올리고 내림, 2-GPU 배치, fp16/bf16 자동, NaN·검은 화면 검사). 전역 변수 대신 함수 안에서 끝나 다시 실행해도 GPU 메모리가 남지 않음 |
| `_wangp_generate()` · `wangp_settings()` | **WanGP 를 웹 UI 대신 `wgp.py --process`(헤드리스)로** — 설정 JSON 에 가속 프로필(Lightning 4-step)을 합치고, 사용자가 직접 적은 steps/guidance 만 덮어씀. 생성 전에 `--dry-run` 으로 검증해 실제 step·프레임 수를 로그에 남김 |
| `_wangp_install()` | v1.0.0 노트북 B 의 설치(커밋 고정 · 드라이버별 torch · venv · Sage 자가 테스트 후 SDPA 대체) + 같은 세션 두 번째 실행부터 설치를 건너뛰는 표식 파일 |
| `_ensure_packages()` | 빠졌거나 버전이 다른 pip 패키지만 설치 (다시 실행할 때 시간 절약) |
| `run()` | 실행마다 `<output_dir>/<실행시각>/` 에 영상 · 메타데이터 JSON(코드 sha256 포함) · run.log |
| 제거 | WanGP 공개 링크(Gradio share)·비밀번호 — 헤드리스라 필요 없음 |
| `videogen/tests/test_videogen.py` | 설정 검사 · diffusers 길 전체(작은 랜덤 Wan 모델, CPU) · WanGP 길 흐름(가짜 wgp.py) |
| `videogen/README.md` | Kaggle 셀(설정만 고침) · 설정 키 · 모델 · 검증 범위 · 문제 해결 |

### 위험 관련 변경
- 없음 (생성 파라미터 기본값은 v1.0.0 프리셋 그대로).

## v1.0.0 — 2026-10-18
- 저장소 밖에서 만든 Kaggle 노트북 2개 (`wan22_ti2v5b_kaggle.ipynb`, `wangp_kaggle_launcher.ipynb`). 이 폴더에는 v1.1.0 으로 합쳐서 올림.
