# 영상 생성 AI — Kaggle 에서 설정만 바꿔 실행 (`videogen/`)

버전: v1.2.1 — 2026-10-18 — WanGP 가 T2V 모델의 창 이어붙이기를 거부한 오류 고침 (사용자 보고 wangp_process.log): `wan2.2-14b-hq` 를 두 단계로 — T2V 14B 첫 5초 → SVI 2 Pro 가 이어 만들기 (2-1번).
이전 v1.2.0 — 2026-10-18 — **1920x1080 · 15초 고품질** (사용자 지시 "좀 고품질의 1920, 1080 해상도로 할아버지가 소파에 앉아서 호통치는 영상으로 15초 정도로 생성하는 설정, 프롬프트로 변경해줘"): 새 모델 `wan2.2-14b-hq` · 새 프리셋 `fhd_15s` · 새 설정 `duration_sec` `upscale_to` `upscaler` — 2-1번 예시.
이전 v1.1.1 — 2026-10-18 — Kaggle 의 오래된 torchao 때문에 나던 `cannot import name 'FqnToConfig'` 오류 고침 (6번 표 첫 줄). 셀은 그대로 다시 실행하면 된다.
이전 v1.1.0 — 2026-10-18 — 사용자 지시 "핵심 코드를 하나로 만들어서 저장소에 올리고 kaggle에서는 코드 받아서 실행하는 방식으로 하고 prompt 같은 설정만 고치고 실행만 하는 코드를 따로 알려줘"

- 핵심 코드: **`videogen/videogen.py` 파일 하나**. Kaggle 셀은 이 파일만 받아서(저장소 전체 clone 안 함) `videogen.run(SETTINGS)` 를 부른다.
- 시험: `python videogen/tests/test_videogen.py` (GPU·네트워크 없이 — 아래 '검증 범위')
- 변경 이력: `videogen/CHANGELOG.md`
- ※ 연구·교육용. 모델별 라이선스·Kaggle 약관·생성물 권리 확인은 사용자 책임.

## 1. Kaggle 준비 (처음 한 번)
1. kaggle.com → Create → **New Notebook**
2. 오른쪽 Settings: **Accelerator = GPU T4 x2**, **Internet = On** (전화번호 인증 필요)
3. (저장소를 비공개로 돌렸을 때만) Add-ons → Secrets 에 `GITHUB_TOKEN` 을 붙인다 — 내레이션 셀(`guides/tts_guide.md` 2-1)과 같은 토큰. 공개 저장소면 필요 없다.

## 2. 노트북 셀 (이것 하나만 — 위 `SETTINGS` 만 고친다)

```python
# ===== 설정: 여기만 고치세요 =====
SETTINGS = dict(
    model="wan2.2-5b",   # "wan2.2-5b"(기본·가장 안정) | "wan2.2-14b-lightning"(고품질) | "ltx2.5-distilled"(영상+소리, 미검증)
    prompt="A golden retriever runs through a sunlit meadow toward the camera, slow motion, cinematic lighting.",
    preset="t4_fast",    # "t4_fast" 832x480·81프레임 | "t4_balanced" 1280x704·49프레임 | "official_720p" 1280x704·121프레임
    seed=42,
)
CODE_REF = "main"        # 결과를 똑같이 재현하려면 커밋 해시로 고정

# ===== 실행: 고치지 않음 =====
import os, sys, importlib, urllib.request
url = f"https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/{CODE_REF}/videogen/videogen.py"
src = "/kaggle/tmp/videogen_src/videogen.py"
os.makedirs(os.path.dirname(src), exist_ok=True)
headers = [{}]
try:
    from kaggle_secrets import UserSecretsClient
    headers.insert(0, {"Authorization": "token " + UserSecretsClient().get_secret("GITHUB_TOKEN")})
except Exception:
    pass  # 공개 저장소면 토큰 없이 받는다
for h in headers:
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=60) as r:
            open(src, "wb").write(r.read())
        break
    except Exception as e:
        err = e
else:
    raise RuntimeError(f"코드 받기 실패: {err} — Internet=On 인지, CODE_REF 가 맞는지 확인")
sys.path.insert(0, os.path.dirname(src))
import videogen; importlib.reload(videogen)
result = videogen.run(SETTINGS)
```

- **대화형으로 실행**하면 로그가 셀 아래에 나오고 끝나면 영상 미리보기가 뜬다.
- **Save Version → Save & Run All (Commit)** 으로 실행하면 브라우저를 닫아도 끝까지 돈다. 결과는 그 버전의 Output 탭.
- 결과: `/kaggle/working/outputs/<실행시각>/` — 영상 · `videogen_<실행시각>.json`(설정·실제 사용 값·버전·단계별 시간·코드 sha256) · `run.log`.
- `CODE_REF="main"` 은 GitHub raw 캐시 때문에 올린 직후 몇 분은 옛 파일이 올 수 있다. 확실히 하려면 커밋 해시를 넣는다 (로그 첫 줄 `code_sha256` 으로 어떤 코드였는지 확인).

### 2-1. 예시: 1920x1080 · 15초 고품질 (할아버지가 소파에서 호통) — 위 셀의 `SETTINGS` 만 이것으로

```python
SETTINGS = dict(
    model="wan2.2-14b-hq",   # 첫 5초: T2V 14B + Lightning 8-step 3-phase → 나머지 10초: SVI 2 Pro(I2V 14B)가 이어 만들기
    preset="fhd_15s",        # 1280x720 으로 15초(16fps 241프레임) 생성 → ×1.5 업스케일 = 1920x1080
    prompt=(
        "Cinematic, photorealistic medium shot. An elderly Korean grandfather in his late seventies with short "
        "silver-gray hair, deep wrinkles and thick gray eyebrows, wearing a beige knit cardigan over a white collared "
        "shirt, sits on a worn brown leather sofa in a warm, cozy Korean apartment living room. He is furious and "
        "scolding loudly: eyebrows knitted together, eyes wide and glaring, mouth opening wide as he shouts, tendons "
        "in his neck taut. He leans forward on the sofa, jabbing his index finger toward the camera again and again, "
        "slaps the sofa armrest with his palm and keeps shouting. Framed family photos on the wall behind him, a low "
        "wooden table with a cup of tea in front. Soft warm afternoon light from a window on the left, gentle shadows, "
        "shallow depth of field. Static camera at eye level, natural lifelike motion at normal speed, highly detailed "
        "skin texture, sharp focus, subtle film grain."
    ),
    seed=42,
)
```
- 왜 바로 1920x1080 으로 만들지 않나: Wan 계열은 약 5초(81~121프레임) 길이로 학습됐고, T4 에서 1080p·15초를 한 번에 만들면 계산량이 수십 배가 된다. 그래서 학습 해상도·길이 안에서 만들고 이어 만든 뒤 키운다.
- 왜 두 단계인가 (v1.2.1): T2V 모델은 앞 구간을 보지 못해 WanGP 가 창 이어붙이기를 거부한다 (`You have requested to Generate Sliding Windows with a Text to Video model` — 2026-10-18 Kaggle). 그래서 **① T2V 14B 로 첫 81프레임(5초)** → **② SVI 2 Pro(Wan2.2 I2V 14B + Stable Video Infinity LoRA, Lightning i2v 4-step)가 ①의 영상을 이어 160프레임(10초)** 을 만들어 한 파일(241프레임)로 합친다. 로그 `[SETUP] length plan total=241 first_stage=t2v_2_2:81 continue_stage=i2v_2_2_svi2pro:160` · `[CONTINUE]`. ①의 영상도 `media/` 에 남는다.
- 업스케일: FlashVSR(학습형 복원, WanGP 후처리)를 먼저 하고, 실패하면(T4 = sm75 는 FlashVSR 전용 커널 목록에 없어 Triton 대체 경로) **ffmpeg Lanczos 로 대신** — 로그 `FlashVSR failed -> falling back to Lanczos`. 생성 원본 1280x720 도 `media/` 에 남는다.
- 시간·디스크: **T4 실측 없음.** 처음 실행은 설치 10~20분 + T2V·I2V 14B 두 벌 다운로드(임시 디스크 약 80GB 추정 — 모자라면 `[SETUP]` 경고). 2025-12 공개 Kaggle 기록(Wan2.2 14B 4-step 한 편, 해상도·길이 미상)이 약 9~10분이었고, 이번은 720p · ① 8 step + ② 창 약 3개라 **몇 시간** 걸릴 수 있다 → *Save & Run All (Commit)* 으로 (Kaggle 세션 한도 12시간). 진행은 `[GENERATE]`·`[CONTINUE] progress` 줄.
- 더 빠르게: `duration_sec=10` 처럼 줄이면 이어 만들 구간이 짧아진다. (`wan2.2-14b-lightning` 에 창 이어붙이기를 더하는 방법은 같은 T2V 거부에 걸려 쓸 수 없다.)
- 해상도는 16의 배수로 (WanGP 가 Wan 블록 크기 16에 맞춰 내림) — 1280x720 은 그대로.
- 세로 쇼츠면 `width=720, height=1280, upscale_to="1080x1920"`.
- 소리는 없다 (Wan2.2 는 영상만). 호통 목소리는 내레이션 셀(`guides/tts_guide.md`)로 따로.

## 3. 설정 키 (`SETTINGS` 에 넣을 수 있는 것)
모르는 키를 넣으면 오타로 보고 바로 멈춘다 (쓸 수 있는 키 목록을 보여 줌).

| 키 | 기본값 | 뜻 |
|---|---|---|
| `model` | `wan2.2-5b` | 아래 모델 표 |
| `prompt` | (예시 문장) | 영어 권장 (Wan 은 영어·중국어 위주로 학습) |
| `negative_prompt` | Wan 공식 중국어 문구 | 피하고 싶은 것 |
| `preset` | `t4_fast` | 해상도·프레임·step 묶음 |
| `seed` | 42 | 같은 seed·설정·코드면 같은 결과 |
| `height` `width` `num_frames` `steps` `guidance_scale` `fps` | None | 프리셋 값을 하나씩 덮어씀. 규칙(32 배수·4k+1)에 안 맞으면 고친 전·후 값을 경고로 남김 |
| `duration_sec` | None | 길이(초). `num_frames` 대신 — WanGP 는 모델 fps 로 가장 가까운 프레임 수를 고름. 우선순위: 직접 적은 `duration_sec` > 직접 적은 `num_frames` > 프리셋 |
| `upscale_to` | None | 최종 해상도 `"1920x1080"`. 생성 해상도의 1.5·2·2.5·3·3.5·4배(가로세로 같은 배율)만 — 안 맞으면 맞는 생성 해상도를 알려 주고 멈춤 |
| `upscaler` | `flashvsr` | `flashvsr`(WanGP 모델에서만, 실패하면 Lanczos) · `lanczos`(ffmpeg) |
| `output_dir` | `/kaggle/working/outputs` | 결과 (20GB 한도) |
| `work_dir` | `/kaggle/tmp/videogen` | 가중치·설치물 (저장 안 됨) |
| `wangp_profile` | `"4"` | WanGP 메모리 프로필. RAM 부족으로 죽으면 `"5"` |
| `wangp_extra` | `{}` | WanGP 설정 키를 직접 (고급) |

## 4. 모델
| `model` | 실행 방식 | 라이선스 | 상태 |
|---|---|---|---|
| `wan2.2-5b` | diffusers, Wan2.2-TI2V-5B. T4 x2 에서 텍스트 인코더·VAE 는 `cuda:1`, DiT 는 `cuda:0` | Apache-2.0 | 작은 랜덤 모델로 CPU 전체 경로 시험 통과. 실제 T4 속도는 첫 실행 `[DENOISE] eta_min` 로그로 확인 |
| `wan2.2-14b-lightning` | WanGP(`wgp.py --process`, 웹 UI 없음) — Wan2.2 T2V 14B + Lightning 4-step LoRA | Apache-2.0 | 가짜 WanGP 로 흐름만 시험. 처음 실행은 설치 10~20분 + 모델 수십 GB 다운로드 |
| `wan2.2-14b-hq` | WanGP 두 단계 — ① Wan2.2 T2V 14B + Lightning 8-step 3-phase(v2025-12-17)로 첫 81프레임 ② 길면 SVI 2 Pro(`i2v_2_2_svi2pro`, I2V 14B) + Lightning i2v 4-step 이 이어 만들기 | Apache-2.0 | 가짜 WanGP(실제 T2V 거부 규칙 흉내)로 두 단계·업스케일만 시험. 긴 영상·고품질용 |
| `ltx2.5-distilled` | WanGP — LTX-2.5 Distilled 22B, 영상과 소리를 함께 | LTX-2 Community License (연매출 1천만 달러 이상 유료) | 미검증. Kaggle RAM(약 30GB)으로 부족할 수 있음 → `wangp_profile="5"` |

- HunyuanVideo 1.5 · MiniMax H3 는 넣지 않았다: 라이선스 적용 지역에서 **대한민국이 빠져 있다**(HunyuanVideo 는 Tencent Hunyuan Community License, H3 는 보도 기준).
- Wan 2.7 · 3.0 은 API 전용(가중치 비공개)이라 쓸 수 없다.

## 5. 검증 범위
- 통과 (2026-10-18, 이 저장소 클라우드 환경, diffusers 0.41.0 · transformers 5.20.1 · CPU): 설정 검사 · 1080p·15초 설정(길이→프레임 · 배율 검사 · 두 단계 T2V→SVI 2 Pro 이어 만들기 · WanGP 의 T2V 창 거부 규칙 회귀 · FlashVSR 성공/실패→Lanczos, 작은 진짜 mp4 로 크기·길이 확인) · 오래된 torchao(0.13.0 — Kaggle 오류 재현) 처리 · diffusers 길 전체(실제 Wan 클래스로 만든 작은 랜덤 모델 — 인코딩 → 디노이즈 → 디코딩 → mp4·JSON·로그) · WanGP 길 흐름(가짜 `wgp.py` — 설정 JSON 에 Lightning 프로필 합치기, `--dry-run` → `--process`, 결과 수집).
- 못 한 것: 실제 Kaggle T4 실행·속도·메모리·화질, 진짜 WanGP 설치. 클라우드 환경에서 Hugging Face·PyTorch 다운로드 서버가 막혀 있었다.

## 6. 문제 해결
| 증상 | 할 일 |
|---|---|
| `num_frames=361 은 Wan2.2-5B 한 번 생성 한도 121 ...` | 5초 넘는 영상은 `model="wan2.2-14b-hq"` |
| `... → 1920x1080 는 배율 ...` | 오류 문장의 '맞는 생성 해상도' 중 하나로 `width`·`height` |
| `FlashVSR failed -> falling back to Lanczos` | 정상 동작(대체). Lanczos 결과 파일 이름 끝이 `_lanczos.mp4` |
| `You have requested to Generate Sliding Windows with a Text to Video model` | v1.2.0 의 `wan2.2-14b-hq` 설정 — v1.2.1 에서 두 단계로 고침. 셀을 그대로 다시 실행 (`CODE_REF` 가 옛 파일을 받으면 커밋 해시로). 다른 T2V 모델에 창 이어붙이기(`wangp_extra` 의 `sliding_window_size`)를 넣어도 같은 오류 |
| `WanGP 설정 검증 실패 ...` · `WanGP 생성 실패 ...` | 오류 문장 뒤에 WanGP 의 마지막 오류 줄이 붙어 나온다. 전체는 결과 폴더 `wangp_process.log` |
| `cannot import name 'FqnToConfig' from 'torchao.quantization'` | v1.1.1 에서 고침 — 셀을 **그대로 다시 실행** (커널 재시작 필요 없음). 로그에 `torchao uninstalled for this Kaggle session` · `diffusers torchao flag switched off` 가 나오면 처리된 것. `CODE_REF="main"` 이 옛 파일을 받으면(올린 직후 raw 캐시) 커밋 해시로 |
| `[DATA] download attempt failed` 반복 | Internet=On 확인. Hugging Face 가 느리면 Secrets 에 `HF_TOKEN` 추가 |
| `[DENOISE] FAILED ... out of memory` | `preset="t4_fast"` 또는 `num_frames` 줄이기 |
| `latents became non-finite` | 다른 `seed`. T4(fp16) 한계일 수 있음 |
| WanGP 설치 실패 | 로그의 `full_log=` 파일(결과 폴더 `wangp_install.log`) 끝부분 확인. 드라이버 문제면 `wangp_torch_build="cu128"` |
| WanGP 생성 중 프로세스가 죽음 (RAM) | `wangp_profile="5"` |
| `알 수 없는 설정 [...]` | 키 이름 오타 — 위 3번 표 |
