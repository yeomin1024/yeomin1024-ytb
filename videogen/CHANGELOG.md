# CHANGELOG — videogen

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
