# 내레이션 만들기 — 오픈소스 음성 AI(Qwen3-TTS)를 Kaggle에서 (모든 주제 공통)

버전: v1.10 — 2026-10-15 — 사용자 지시 "맨 마지막 대사 … 시청해주셔서 감사합니다. 로 변경 … 음성 … 에 모두 반영": **바뀐 문장만 다시 만들기** (tts_narration v1.8) — 대본 글이 조금 바뀌면 셀이 그 문장만 새로 만들어 저장소 오디오에 끼운다 (3번 1·5번 '일괄 대상') (v1.9 — 2026-10-15 — 사용자 지시 "오디오 코드도 진행자 목소리로만 대본 읽도록 하고 오디오를 생성할 경로를 전체 경로 또는 economic 같은 단일 주제 경로를 버튼으로 선택할수 있게해 디폴트는 전체야": **진행자(H04) 목소리 하나로 모든 문장**(사연자 역할 끔 — `voices/storyteller.json` enabled=false, tts_narration v1.7), 노트북 셀에 **범위 버튼**(전체 · 주제 폴더, 기본 전체 — `tools/kaggle_tts_panel.py`) (v1.8 — 2026-10-13 — 저장소를 비공개로 돌려도 되게: 노트북 셀이 Kaggle Secrets 의 토큰으로 저장소를 받음 (사용자 지시 "비공개로 돌릴테니까") (v1.7 — 2026-10-12 — 사용자 지시: **사연자 S07(말 속도 조금 더 빠르게)·진행자 H04로 고정** — `pace.speed`(모든 문장을 이 배수로) 추가 (v1.6 — 2026-10-12 — 사용자 지시: 사연자 남성 후보(억울·자책 연기 톤) S07·S08, 말 속도 맞추기(pace), 터미널에서 바로 듣기(listen) (v1.5 — 2026-10-12 — 사용자 지시: **사연자·진행자 목소리 샘플을 각각 여러 개 만들고, 사용자가 고르면 그 목소리로 일관되게** (4-0). 고르기 전에는 셀이 오디오 대신 샘플만 만든다 (v1.4 — 2026-10-11 — 사용자 지시: 진행자 목소리는 중저음 남성(귀에 쏙쏙 들어오고 신뢰감 있게), 대본마다 달라지면 안 됨 → 기준 목소리 하나를 저장소에 고정하고 모든 대본이 복제 (1번, 4-1번) (v1.3.1: 셀이 `git pull` 대신 Kaggle 사본을 main과 똑같이 맞춤 (`Your local changes ... would be overwritten by merge` 오류 해결) (v1.3: 사용자 지시: 오디오는 고르지 않고 하나로(말투 시험·선택 단계 삭제, 영상마다 `narration.mp3` 하나), 결과 파일은 GitHub의 대본 폴더마다 자동으로 올린다(`--push`), Kaggle 셀 하나 (v1.2: 사연자·진행자 목소리 설정 파일, 대본 전부 한 번에 `all`; v1.1: 셀에 도구 파일을 붙여 넣지 말 것; v1.0: 사용자 지시: edge-tts는 어색하다 → 오픈소스 음성 AI로, Kaggle에서, 사연은 억울하고 후회하는 톤))))))))

도구: `tools/tts_narration.py` v1.8 · 범위 버튼 `tools/kaggle_tts_panel.py` v1.0 · 목소리: **진행자 하나** `voices/host.json`(**H04 — 고정**, 기준 목소리 `voices/ref/host.wav`) — 사연자 `voices/storyteller.json`(S07)은 **꺼 둠**(enabled=false, 사용자 지시 2026-10-15) · 목소리 후보: `voices/samples/samples.json`
결과: 영상마다 오디오 **하나** — `<주제폴더>/source/<영상ID>/narration.mp3`가 **대본 폴더마다 각각** GitHub main에 자동으로 올라가고, 4단계(`guides/pipeline.md`)가 이어진다.
※ 연구·교육용 도구다. 주식 영상 내용은 투자 권유가 아니다.

## 1. 모델

| 항목 | 내용 |
|---|---|
| 모델 | Qwen3-TTS 1.7B 세 가지 (Alibaba Qwen, 2026-01 공개, 같은 `qwen-tts` 패키지) — 아래 표 |
| 라이선스 | Apache-2.0 — 상업 이용 가능 (수익 창출 채널에 써도 됨) |
| 한국어 | 지원 10개 언어 중 하나. 기본 화자 중 한국어가 모국어인 화자는 **Sohee**(여성) 하나뿐 — 그래서 남성 진행자는 목소리를 글로 묘사해 만든다 |
| 주의 | **0.6B 모델은 말투 지시를 무시한다** (패키지 코드가 지시를 지움). 감정을 넣으려면 1.7B |

| 역할 | 모델 | 하는 일 |
|---|---|---|
| 사연자 (**꺼 둠** — 2026-10-15부터 진행자가 모든 문장) | `Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice` | 화자 Sohee + 말투 지시(억울·후회 고백) |
| 진행자 | `Qwen/Qwen3-TTS-12Hz-1.7B-Base` | 저장소의 **기준 목소리** `voices/ref/host.wav`를 복제해 읽는다 → 모든 대본·모든 세션에서 같은 남성 목소리 |
| (처음 한 번) | `Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign` | 기준 목소리가 없을 때만: `voices/host.json`의 묘사(30대 후반 남성, 따뜻한 중저음 바리톤, 뉴스 앵커·다큐 내레이터처럼 신뢰감, 또렷한 발음, 숫자에 힘을 주는 보통 속도)로 만든다 |

- GPU가 둘(T4 x2)이면 사연자 모델은 GPU 0, 진행자 모델은 GPU 1에 올린다. 하나면 번갈아 올린다(느려짐).
- 처음 실행은 모델 세 개를 받느라 시간이 더 걸린다 (그 뒤 세션도 Kaggle이 새로 받는다).

edge-tts와 다른 점: 문장 뜻을 읽고 억양·쉼을 스스로 정한다. 같은 문장도 시드마다 조금씩 다르게 읽으므로 이상한 문장만 다시 만들 수 있다 (3번 `--redo`). 말투는 설정 파일 하나로 정해져 있고, 시험해 보고 고르는 단계는 없다.

## 2. 처음 한 번 준비

### 2-1. Kaggle 노트북
1. kaggle.com → Create → **New Notebook**
2. 오른쪽 **Settings**
   - **Accelerator: GPU T4 x2** (P100은 최신 PyTorch가 지원하지 않을 수 있다)
   - **Internet: On** — 계정 휴대폰 인증이 있어야 켜진다
3. GPU 사용 시간은 주당 한도가 있다(계정 화면에 남은 시간이 나온다).

### 2-2. GitHub 토큰 (결과를 저장소에 올리는 열쇠)
**토큰은 채팅창·노트북 셀·파일에 붙여 넣지 않는다.** Kaggle Secrets에만 넣는다.
1. GitHub → 오른쪽 위 사진 → **Settings** → 맨 아래 **Developer settings** → **Personal access tokens** → **Fine-grained tokens** → **Generate new token**
   - Token name: `kaggle-tts` · Expiration: 90일 (만료되면 같은 방법으로 새로 만든다)
   - Repository access: **Only select repositories** → `yeomin1024/yeomin1024-ytb` 하나만
   - Permissions → Repository permissions → **Contents: Read and write** (Metadata: Read-only는 자동) — 다른 권한은 주지 않는다
   - **Generate token** → 보이는 값(`github_pat_…`)을 복사한다 (이때 한 번만 보인다)
2. Kaggle 노트북 위 메뉴 **Add-ons → Secrets** → **Add Secret**
   - Label: `GITHUB_TOKEN` · Value: 복사한 토큰 → Save
   - 목록에서 `GITHUB_TOKEN` 옆 체크(이 노트북에 연결)를 켠다
3. 노트북을 공개(Public)로 바꾸지 않는다. Secrets 값은 노트북을 복사·공유해도 따라가지 않는다.
- 도구는 토큰을 로그·파일·명령줄·원격 주소에 남기지 않는다 (git 이 물을 때만 `GIT_ASKPASS`로 넘김). 시작할 때 push 권한부터 확인하고, 안 되면 오디오를 만들기 전에 멈춘다.

## 3. 노트북 셀 (이것 하나만 복사해서 실행)

> ⚠️ `tools/tts_narration.py`의 **내용을 셀에 붙여 넣지 않는다** (잘리면 `_IncompleteInputError`, 저장소의 다른 파일도 필요). 아래 셀만 넣는다.

```
from kaggle_secrets import UserSecretsClient
import os, sys, base64, importlib
os.environ["GITHUB_TOKEN"] = UserSecretsClient().get_secret("GITHUB_TOKEN")
os.environ.update(GIT_CONFIG_COUNT="1", GIT_CONFIG_KEY_0="http.https://github.com/.extraheader",
                  GIT_CONFIG_VALUE_0="AUTHORIZATION: basic " + base64.b64encode(("x-access-token:" + os.environ["GITHUB_TOKEN"]).encode()).decode())
!pip install -q -U qwen-tts
!test -d /kaggle/working/yeomin1024-ytb || git clone -q --depth 1 https://github.com/yeomin1024/yeomin1024-ytb.git /kaggle/working/yeomin1024-ytb
!cd /kaggle/working/yeomin1024-ytb && git config core.fileMode false && git fetch -q origin main && git reset -q --hard origin/main
sys.path.insert(0, "/kaggle/working/yeomin1024-ytb/tools")
import kaggle_tts_panel; importlib.reload(kaggle_tts_panel).panel()
```
- 셀을 실행하면 맨 아래에 **범위 버튼**이 나온다 (사용자 지시 2026-10-15):
  - `전체 (대본 N개)` — **기본** (모든 주제 폴더) · `economic (대본 N개)` 처럼 주제 폴더 하나
  - **[오디오 만들기]**: 고른 범위로 `tools/tts_narration.py all --push` (주제 하나면 `--topics 주제`). 그대로 누르면 전체
  - **[목록만 보기]**: 같은 범위로 `all --dry-run` — 모델을 불러오지 않고 무엇을 만들지만
  - 로그는 버튼 아래 칸과 `/kaggle/working/tts_panel.log`에 남는다. 실행 중에는 버튼이 잠긴다.
  - 버튼이 안 보이면(위젯이 없는 환경) 기본 범위(전체)로 바로 실행한다. 터미널: `python tools/kaggle_tts_panel.py --topic economic`
- 넷째·다섯째 줄(`GIT_CONFIG_…`)은 **저장소가 비공개여도** `git clone`·`git fetch`가 되게 Secrets 의 토큰을 git 에 머리글로 넘긴다 (2026-10-13). 값은 셀·출력·파일에 나오지 않는다. 공개 저장소에서도 그대로 쓴다.
- `git fetch … reset --hard origin/main` 줄은 Kaggle의 저장소 사본을 main과 **똑같이** 맞춘다 (`git pull` 대신). 이 사본은 도구를 돌리는 용도라 고쳐 쓰지 않는다. 사본에서 실행 권한만 바뀐 파일이 있으면 `git pull`이 `Your local changes to the following files would be overwritten by merge`로 멈췄다.
- 올리기가 실패해 사본에만 남은 커밋은 이 줄로 지워져도 괜찮다 — 결과는 `/kaggle/working/tts_out/upload/`에 있어 다음 실행이 다시 올린다.

하는 일:
0. **목소리를 아직 고르지 않았으면 (처음 한 번)** 오디오 대신 **목소리 후보 샘플**만 만들어 `voices/samples/`에 올리고 끝난다 (4-0). 로그 `[PLAN] unpicked=storyteller,host` → `[SAMPLES] …` → `[NEXT] … 듣고 Claude에게 '사연자 S0?, 진행자 H0?'`. 고른 뒤 **같은 셀을 다시** 실행하면 아래 1~4를 한다.
1. 저장소를 받고(이미 있으면 main과 똑같이 맞추고), 대본(`<주제폴더>/source/<영상ID>/<영상ID>.txt`)을 **모두 읽어** 오디오가 없는 영상을 고른다. 로그 `[PLAN] video=… action=make|skip`
   - 건너뜀: 보류 주제(README에 ⏸), 이미 업로드한 영상(`youtube.json`), 지금 대본으로 만든 오디오가 이미 저장소에 있는 영상
   - 다시 만듦: 저장소의 오디오가 옛 대본으로 만든 것일 때 (Claude가 대본을 고친 뒤)
   - **바뀐 문장만 (v1.8)**: 문장 수·챕터·카드·쉼·목소리가 같고 **글만 바뀐 문장이 20% 이하**면 그 문장만 새로 만들어 저장소 `narration.mp3`의 그 자리에 끼운다. 다른 문장은 소리·길이 그대로(뒤 문장 시각만 길이 차이만큼 밀림), 새 문장 크기는 다른 문장들 말소리 크기에 맞춘다. 로그 `[PLAN] mode="patch 99"` → `[PATCH] mode="바뀐 문장만"`, `tts_report.md` 끝에 '부분 다시 만들기' 표(귀로 확인할 문장). 그 밖(문장 수가 바뀜 등)은 전부 다시 — `[PATCH] mode="전부 만들기" why=…`. 일부러 전부 다시: `all --full --push`
2. 영상마다 **진행자 목소리(H04) 하나로** 모든 문장을 만들어 **오디오 하나**(`narration.mp3`)로 잇는다 (사연 파트도 진행자가 읽는다 — 사용자 지시 2026-10-15).
3. **영상 하나가 끝날 때마다** 그 영상의 결과 3개를 그 영상의 대본 폴더에 넣어 main에 커밋·푸시한다. 로그 `[PUSH] … ok=True note="대본 폴더마다 올라감: stock/source/<영상ID>/"`
   - `narration.mp3` — 영상에 쓰는 오디오
   - `tts_narration.json` — 문장별 역할·시작·끝 시각, 대본 해시 (오디오가 지금 대본으로 만든 것인지 확인용)
   - `tts_report.md` — 문장별 길이·속도와 **귀로 확인할 문장**
4. 끝나면 Claude에게 **"오디오 올렸어"** → 영상 코드가 없으면 만들고, 렌더·비공개 업로드까지 승인 없이 진행한다 (`pipeline.md` 4단계).

- 걸리는 시간은 로그 `[PROGRESS] … eta_min=`에 나온다. 브라우저 탭을 열어 둔다. 중간에 끊기면 같은 셀을 다시 실행한다 — 이미 올라간 영상은 건너뛰고, 같은 세션이면 만든 문장은 cache에서 그대로 쓴다.
- 일부만: 주제 하나는 **범위 버튼**. 영상 몇 개만이면 셀 대신 `!cd /kaggle/working/yeomin1024-ytb && python tools/tts_narration.py all --push --ids eunte-kkeonaeseugi-2026-10` · `--max 2`
- 무엇을 만들지 목록만 보기: **[목록만 보기]** 버튼 (= `all --dry-run`)

**문제가 생겼을 때 (같은 노트북에서 셀 하나 더)**

| 상황 | 셀 |
|---|---|
| `error: Your local changes to the following files would be overwritten by merge` (옛 셀의 `git pull`) | 위 셀을 그대로 다시 실행 (넷째 줄이 사본을 main과 맞춘다). 셀을 못 바꾸면: `!cd /kaggle/working/yeomin1024-ytb && git config core.fileMode false && git fetch -q origin main && git reset -q --hard origin/main` |
| 올리기만 실패 (`[PUSH] … ok=False`) | `!cd /kaggle/working/yeomin1024-ytb && python tools/tts_narration.py push` |
| 토큰 오류로 멈춤 (`GitHub 토큰 없음`, `push 권한 확인 실패`) | 2-2를 다시 확인(만료·저장소 선택·Contents 쓰기, 노트북 연결 체크) → 셀 다시 실행 |
| 이상한 문장만 다시 (새 시드, 같은 세션 안에서) | `!cd /kaggle/working/yeomin1024-ytb && python tools/tts_narration.py build stock panicsell-2026-10 --redo 12,15 --push` |
| GitHub에 도저히 못 올릴 때 | `!cd /kaggle/working/yeomin1024-ytb && python tools/tts_narration.py pack` → `/kaggle/working/tts_out/narration_upload.zip` 내려받아 GitHub 웹 Add file → Upload files에 안의 `stock` 폴더를 끌어 놓기 |
| GPU 2개로 빠르게 (선택) | `!cd /kaggle/working/yeomin1024-ytb && (python tools/tts_narration.py all --push --gpu 0 --split 0/2 > /kaggle/working/log0.txt 2>&1 & python tools/tts_narration.py all --push --gpu 1 --split 1/2 > /kaggle/working/log1.txt 2>&1 & wait); grep -hE "PUSH\|BATCH\|ERROR" /kaggle/working/log0.txt /kaggle/working/log1.txt` (올리기는 잠금 파일로 차례로) |

## 4. 사연자·진행자와 결과 경로

> **2026-10-15부터 진행자(H04) 하나로 모든 문장을 읽는다** (사용자 지시 "진행자 목소리로만"). 사연자는 `voices/storyteller.json`의 `"enabled": false`로 꺼 두었다 — 고른 기록(S07)·기준 소리는 남겨 두어, `enabled`를 지우면 다시 켜진다. 꺼진 역할은 고르기·샘플·모델에서 빠진다. 아래 4-0은 목소리를 처음 고를 때의 기록이다.

### 4-0. 목소리 고르기 — 샘플을 듣고 하나씩 (사용자 지시 2026-10-12)
1. **샘플 만들기 (Kaggle, 3번 셀 그대로):** 두 역할 중 하나라도 고르지 않았으면 셀이 후보마다 같은 문장을 읽힌 샘플을 만든다. 후보는 `voices/samples/samples.json`:

   | 역할 | 후보 | 만드는 법 |
   |---|---|---|
   | 사연자 | **S01** 지금 목소리(Sohee 억울·후회) · S02 Sohee 담담 · S03 Sohee 감정 많이 · S04 30대 초반 여성 · S05 40대 중반 여성 · S06 40대 초반 남성 · **S07 40대 초반 남성 — 손실에 억울해하다 자책으로 가라앉는 연기 톤 · S08 30대 후반 남성 — 친구에게 털어놓듯 억울함과 자책** (S07·S08: 사용자 지시 2026-10-12 "사연자 목소리를 남자로, 억울하고 자책하듯, 자연스러운 속도") | current / 화자+말투(CustomVoice) / 묘사(VoiceDesign) → 기준 소리 → 복제(Base) |
   | 진행자 | **H01** 지금 기준 목소리 · H02 같은 묘사 다른 시드 · H03 40대 깊은 저음 앵커 · H04 30대 밝은 경제 유튜버 · H05 50대 다큐 내레이터 · H06 심야 라디오 | current / 묘사 → 기준 소리 → 복제 |

   - 묘사 후보는 시드 3개로 기준 소리를 만들어 목소리 높이 범위(여성 약 140~300Hz, 남성 약 80~170Hz)·속도·무음 검사로 하나를 고른 뒤, **그 소리를 복제해** 미리 듣기 문장을 읽힌다 — 실제 내레이션과 같은 방식이라 들은 그대로 나온다.
   - 결과: `voices/samples/<역할>/<ID>.mp3`(약 18초), `<ID>.json`(높이·속도·확인할 점), 묘사 후보는 `<ID>_ref.wav`(기준 소리), 표 `voices/samples/README.md`. main에 올라간다. 걸리는 시간: T4 x2 기준 약 20~30분(추정).
2. **듣고 고르기 (사용자):** `voices/samples/README.md`의 mp3를 듣고 Claude에게 **"사연자 S04, 진행자 H01"**처럼 말한다.
3. **고정 (Claude, GPU 필요 없음):** `python tools/tts_narration.py pick S04 H01` → 커밋·푸시.
   - current(S01·H01): 설정 그대로 — 그 역할은 아무것도 바뀌지 않는다.
   - 화자+말투(S02·S03): `voices/storyteller.json`에 화자·말투·시드를 고정 (`lock`).
   - 묘사(S04~S06, H02~H06): 기준 소리를 `voices/ref/<역할>.wav`·`.json`으로 복사하고 `engine: clone`, `lock`. 모든 대본이 이 소리를 복제한다.
   - 고른 기록: `voices/<역할>.json`의 `"picked": {"id", "label", "date", "sample"}`. 두 역할 모두 `picked`가 있어야 셀이 오디오를 만든다 (`build`는 멈춘다).
   - `lock`이라 주제 폴더의 `voices/storyteller.json`(주제별 말투)은 무시된다 — 모든 대본 같은 목소리 (사용자 지시). current(S01)를 고르면 지금처럼 주제별 말투를 쓴다.
4. **다시 셀 실행:** 고른 목소리로 오디오가 없는 영상을 모두 만든다. 그 역할 목소리가 바뀐 영상(오디오가 있고 아직 안 올린 것)은 다시 만든다. **이미 유튜브에 올린 영상(`youtube.json`)은 그대로 둔다.**
- 후보를 바꾸거나 더하려면 `samples.json`을 고친 뒤 셀을 다시 실행 → 바뀐 후보만 새로 만든다. 일부만 다시: `python tools/tts_narration.py samples --only S04,H02 --force --push`
- **바로 듣기 (터미널):** `python tools/tts_narration.py listen S07 S08` (ffplay·afplay·mpv로 재생) · 만들면서 듣기: `samples --only S07,S08 --play`. 소리 장치가 없는 곳(Kaggle·클라우드)에서는 경로를 알려 주고, Kaggle 셀에서는 `from IPython.display import Audio; Audio("voices/samples/storyteller/S07.mp3")`로 듣는다.
- **말 속도 맞추기 (`pace`):** 후보·역할 설정 `{"min": 4.2, "max": 5.2, "max_stretch": 0.15}`(음절/초) — 고른 문장의 속도가 범위 밖이면 음 높이는 그대로 두고(ffmpeg atempo) ±15% 안에서 늘이거나 줄인다. 로그 `[PACE] rate_before= rate_after= factor=`, 보고서 '속도 맞춤 ×0.93'. S07·S08에 들어 있고 pick 하면 사연자 설정으로 옮겨진다. 문장 사이 쉼도 S07·S08은 0.55초(고백하듯 조금 길게).
  - **`speed` (v1.6):** `{"speed": 1.1, ...}` → 모든 문장을 먼저 1.1배 빠르게 한 뒤 [min, max] 안으로 (짧은 문장도 speed 만큼). 지금 사연자 설정: `{"speed": 1.1, "min": 4.6, "max": 5.8, "max_stretch": 0.15}` (사용자 지시 "말하는 속도 조금 더 빠르게"). speed 를 바꾸면 사연자 문장을 다시 만든다.
- 고른 뒤 다른 후보로 바꿀 때도 `pick`. current ID(S01·H01)는 샘플을 만든 때의 설정으로만 돌아갈 수 있다 — 설정이 바뀐 뒤에는 `pick`이 거절하고, git으로 되돌린다.

- **고른 결과 (2026-10-12, 사용자):** 사연자 **S07**(40대 초반 남성, 억울함→자책 연기 톤, 말 속도 조금 더 빠르게 — `pace.speed` 1.1), 진행자 **H04**(30대 초반, 또렷하고 밝은 중저음, 경제 유튜버). `pick S07 H04` → `voices/ref/storyteller.wav`(새로)·`voices/ref/host.wav`(H01 → H04로 바뀜). 이미 올린 주식 영상 4개(`stock_backup/`)는 옛 목소리 그대로.

### 4-1. 진행자 목소리는 모든 대본에서 같다 (사용자 지시 2026-10-11)
- 4-0에서 묘사 후보를 고르면 그 후보의 기준 소리가 `voices/ref/host.wav`가 된다. 아래 1~2는 기준 소리가 아예 없을 때만 한다.
1. **기준 목소리 한 번 만들기:** 저장소에 `voices/ref/host.wav`가 없으면 셀이 처음 실행될 때 VoiceDesign으로 만든다. 시드를 바꿔 6번 만들고 검사해서 하나를 고른다. 사람이 고르지 않는다.
   - 목소리 높이(기본 주파수)가 **남성 중저음 85~150Hz** 안 — 여러 개면 **110Hz**에 가장 가까운 것
   - 말 속도 3.8~6.0음절/초(귀에 잘 들어오게), 문장 안 무음 1초 이하
   - 6번 모두 높이가 범위 밖이면 만들지 않고 멈춘다 (엉뚱한 목소리로 고정되지 않게)
2. **저장소에 고정:** 고른 소리와 정보를 `voices/ref/host.wav`·`voices/ref/host.json`(만든 문장·묘사·시드·높이·해시)으로 main에 올린다. 올리지 못하면 오디오를 만들지 않는다 — 다음 세션이 다른 목소리를 만들지 않게.
3. **모든 대본이 복제:** 진행자 문장은 전부 이 파일을 복제해 읽는다. 문장마다 목소리 높이를 재서 기준에서 **±30%** 넘게 벗어나면 시드를 바꿔 다시 만든다. 보고서 `tts_report.md`에 문장마다 높이(Hz)가 나온다.
4. **덮어쓰기 없음:** `voices/host.json`의 `"lock": true` — 주제·영상 폴더의 설정 파일이나 명령줄 값이 진행자를 바꾸지 못한다.
5. **목소리가 바뀌면 다시:** 오디오마다 `tts_narration.json`에 목소리 정체(설정·기준 목소리 해시)를 남긴다. 기준 목소리나 목소리 설정이 바뀌면 이미 올린 오디오는 "다른 목소리"로 보고 다음 실행이 다시 만든다 (`publish.sh`도 그 오디오로 영상을 만들지 않는다). 그래서 모든 영상의 진행자가 같은 목소리로 맞춰진다.
- 기준 목소리를 일부러 바꿀 때만 (Claude가): `python tools/tts_narration.py voice --force --push` → 그 뒤 셀을 실행하면 모든 영상이 새 목소리로 다시 만들어진다.

### 4-2. 결과 경로

| 역할 | 읽는 문장 | 설정 파일 | 문장 파일 (Kaggle 작업 폴더, 올리지 않음) |
|---|---|---|---|
| 사연자 `storyteller` | 파트 라벨에 '사연'이 든 문장 (1인칭 고백) | `voices/storyteller.json` | `/kaggle/working/tts_out/<영상ID>/storyteller/S001.wav` … |
| 진행자 `host` (중저음 남성, 기준 목소리 복제) | 나머지 모든 파트 (진행자·문제 분석·올바른 방법·마무리) | `voices/host.json` + `voices/ref/host.wav` | `/kaggle/working/tts_out/<영상ID>/host/S017.wav` … |

- **결과는 영상마다 오디오 하나:** 두 역할을 대본 순서대로 이은 `narration.mp3`. 저장소의 **그 영상 대본 폴더** `<주제폴더>/source/<영상ID>/`에 올라간다 (예: `stock/source/bittu-2026-10/narration.mp3`).
- 문장 파일 번호 = 대본 문장 번호 (자막 도구 `srt_tool.py`와 같은 번호). 볼륨은 영상 전체에 맞춘 뒤의 소리다.
- 올리기 안전장치: 지금 대본과 다른 옛 결과, 저장소에 이미 있는 더 나중 결과는 올리지 않는다. 그 영상의 결과 3개 말고 다른 파일은 커밋하지 않는다. 가짜 소리(`--fake`)는 github.com에 올리지 않는다.
- `python tools/tts_narration.py check <주제폴더> <영상ID>`: 저장소 오디오가 지금 대본·지금 목소리로 만든 것인지 (`publish.sh`도 확인한다).
- 영상 코드의 사연 끝 번호(`plan.ts`의 `STORY_LAST`)와 사연자 마지막 문장 번호가 다르면 로그에 `[ROLE] … ok=False`가 나온다.

## 5. 도구가 지키는 규칙

| 규칙 | 값 | 근거 |
|---|---|---|
| 문장 = 대본 문장 | 파트 라벨·`[장면]`·카드 문구는 읽지 않음. 판정은 `srt_tool.parse_txt`와 같음 | `pipeline.md` 4단계 |
| 역할 | 파트 라벨에 `parts` 낱말('사연')이 있으면 사연자, 없으면 `"*"` 역할(진행자) | 사용자 지시 2026-10-10 |
| 말투 | 역할마다 설정 파일의 말투 하나. 시험해 보고 고르는 단계 없음 | 사용자 지시 2026-10-11 |
| 결과 | 영상마다 `narration.mp3` 하나 → 대본 폴더마다 GitHub main에 자동 커밋·푸시 | 사용자 지시 2026-10-11 |
| 문장 사이 쉼 | 역할 설정의 `gap`(기본 0.45초, 0.2초 이상), 파트가 바뀌면 1.0초, 완전 무음 | `align-audio`가 무음(−35dB, 0.12초 이상)으로 문장 경계를 찾음 |
| 고지 카드 자리 | `[장면]` 바로 앞 문장 뒤 4~8초 (카드 문구 글자 수 ÷ 7 + 1초) | 최소 3.5초 규칙 (`video_guide.md` 2번) |
| 첫 문장 앞 | 0.3초 | 첫 자막 앞 2초 이내 |
| 문장 검사 | 말 속도 2.5~8음절/초, 문장 안 무음 1.8초 이하, NaN·빈 소리 없음. 벗어나면 시드를 바꿔 최대 3번 | 성공 영상 4.2~5.5음절/초 (`stock/guides/data_insights.md` 2번) |
| 볼륨 | 영상 전체에 같은 이득 하나 (말소리 RMS −18dBFS, 최고점 −1dBFS 이하). 역할마다 따로 바꾸지 않음 | 문장마다 바꾸면 감정의 강약이 사라짐 |
| 부호 금액 | `-800만 원` → TTS에는 "마이너스 800만 원"으로 (대본·자막은 그대로) | 부호가 빠지면 뜻이 바뀜 |
| 읽는 소리 사전 | `<주제폴더>/tts_lexicon.tsv`, `source/<영상ID>/tts_lexicon.tsv` (`원문<TAB>읽는 소리`)가 있으면 씀 | 잘못 읽는 낱말 고치기 |
| 재현 | 시드 = 역할 설정의 `seed`(1234) + 문장 글로 정한 값 + 시도 번호. 로그·`cache/*.json`에 남음 | 같은 GPU·같은 설정이면 같은 소리 |
| 일괄 대상 | 보류 주제·업로드한 영상·지금 대본 오디오가 있는 영상은 건너뜀, 옛 대본 오디오는 다시 만듦 — 글만 조금 바뀌었으면 그 문장만 (v1.8, `--full` 이면 전부) | 사용자 지시 2026-10-10 · 2026-10-15 (끝인사만 바꿈 → 영상마다 문장 하나, GPU 몇 초) |

- 오디오가 만들어진 뒤에는 고치지 않는다(자르기·늘이기 금지). 이상하면 그 문장만 `--redo`로 다시 만들고 다시 잇는다.
- 저장소에서 `--fake`로 모델 없이 전 과정을 시험할 수 있다 (가짜 소리 → mp3 → `npm run align-audio`, 올리기는 시험용 로컬 저장소로만).

## 6. 목소리 설정 파일 (바꿀 때만 — 평소에는 손대지 않는다)

말투는 고르지 않는다. 바꿔야 하면 Claude에게 "사연자 목소리를 더 담담하게"처럼 말하면 설정 파일을 고쳐 main에 올린다. 진행자 목소리를 바꾸면 모든 영상의 오디오가 다시 만들어진다 (4-1의 5). `voices/<역할>.json` 항목:

| 항목 | 뜻 | 기본값 |
|---|---|---|
| `parts` | 이 역할이 읽는 파트 라벨 낱말. `"*"`는 다른 역할이 맡지 않은 모든 파트 (한 역할만) | 사연자 `["사연"]`, 진행자 `["*"]` |
| `engine` | `custom_voice`(화자 + 말투 지시) 또는 `clone`(기준 목소리 복제) | 사연자 `custom_voice`, 진행자 `clone` |
| `lock` | `true`면 주제·영상 덮어쓰기와 명령줄 값을 받지 않음 | 진행자 `true` (pick 하면 두 역할 모두 `true`, current 는 그대로) |
| `picked` | 사용자가 고른 샘플 `{id, label, date, sample}` — `pick` 이 쓴다. 두 역할 모두 있어야 오디오를 만든다 | 없음 (고르기 전) |
| `speaker` | (custom_voice) 화자. 한국어가 모국어인 화자는 **Sohee** 하나 | 사연자 `Sohee` |
| `ref_audio`·`ref_meta` | (clone) 기준 목소리 파일 — 손으로 바꾸지 않는다 (해시 검사에서 멈춤) | `voices/ref/host.wav`·`.json` |
| `design` | (clone) 기준 목소리를 만들 때만: `instruct`(목소리 묘사), `text`(읽을 문장), `seed`, `tries`(6), `f0_range`([85, 150]Hz), `f0_target`(110Hz) | 중저음 남성 뉴스 앵커·다큐 내레이터 |
| `f0_tolerance` | (clone) 문장 목소리 높이가 기준에서 벗어나도 되는 비율 | 0.3 |
| `instruct` | (custom_voice) 말투 지시. 음색보다 **감정·속도·쉼·억양**을 쓴다. 끝에 "Keep every word clear" | 사연자: 억울·후회 고백 |
| `part_instruct` | (custom_voice) 역할 안에서 파트별 말투 `{파트 낱말: 지시}`. clone은 말투 지시를 받지 않아 무시 | 비어 있음 |
| `seed` | 기본 시드. 바꾸면 그 역할의 문장을 모두 새로 만든다 | 1234 |
| `gap` | 그 역할의 문장 사이 쉼(초), 0.2 이상 | 0.45 |
| `generation` | 생성 설정 `{temperature, top_p, top_k, repetition_penalty}` | 모델 기본값 |

- 주제·영상마다 다르게 (사연자만 — 진행자는 lock): 바꿀 항목만 담은 같은 이름의 파일을 `<주제폴더>/voices/` 또는 `<주제폴더>/source/<영상ID>/voices/`에 둔다 (영상 > 주제 > 기본 순서로 덮어씀, 로그 `[ROLE] … files=`).
- 설정을 바꾸면 파일 안 `_버전`에 남긴다. 0.6B 모델은 말투 지시를 무시한다 (기본 1.7B).

## 변경 이력

| 버전 | 날짜 | 변경 내용 |
|---|---|---|
| v1.10 | 2026-10-15 | 사용자 지시(끝인사 "시청해주셔서 감사합니다."를 음성에도): tts_narration v1.8 바뀐 문장만 다시 만들기 — 3번 1(바뀐 문장만)·5번 일괄 대상, `--full` |
| v1.9 | 2026-10-15 | 사용자 지시: 진행자 목소리 하나로 모든 문장(사연자 역할 끔, tts_narration v1.7 `enabled`), 노트북 셀에 범위 버튼(전체 기본 · 주제 폴더 — `tools/kaggle_tts_panel.py`) |
| v1.8 | 2026-10-13 | 사용자 지시 "비공개로 돌릴테니까 전부 다 업로드되게": 3번 셀이 Kaggle Secrets 토큰으로 저장소를 받음(`GIT_CONFIG_*` 환경 변수 — 비공개 저장소의 `git clone`·`fetch`), 공개 저장소에서도 같은 셀 |
| v1.7 | 2026-10-12 | 사용자 지시: 사연자 S07(말 속도 조금 더 빠르게)·진행자 H04 고정 (`pick S07 H04`), `pace.speed` 1.1 (`tts_narration.py` v1.6) |
| v1.6 | 2026-10-12 | 사용자 지시: 사연자를 남자로(손실로 억울해하며 자책하는 연기 톤), 자연스러운 속도, 터미널에서 바로 듣기 — 후보 S07·S08, `pace`(속도 맞추기), `listen`·`samples --play` (4-0) |
| v1.5 | 2026-10-12 | 사용자 지시: 사연자·진행자 목소리 샘플을 각각 여러 개 만들고 사용자가 고르면 그 목소리로 일관되게 — 4-0(후보 12개 `voices/samples/samples.json`, 샘플 `voices/samples/`, `pick`, 고르기 전에는 셀이 샘플만), 3번 '하는 일' 0단계, 6번 `picked`, 업로드한 영상은 다시 만들지 않음 |
| v1.4 | 2026-10-11 | 사용자 지시: 진행자는 중저음 남성(귀에 쏙쏙 들어오고 신뢰감 있게), 대본마다 달라지면 안 됨 — 기준 목소리를 처음 한 번 VoiceDesign으로 만들어(남성 중저음 85~150Hz·속도·무음 검사, 사람이 고르지 않음) `voices/ref/host.wav`로 고정하고 모든 대본이 Base 모델로 복제. 문장마다 높이 ±30% 검사, lock, 목소리가 바뀐 오디오는 다시 만듦. 1번 모델 표, 4-1 |
| v1.3.1 | 2026-10-11 | 셀 넷째 줄: `git pull` → `git config core.fileMode false && git fetch origin main && git reset --hard origin/main` (사본에서 실행 권한만 바뀐 `tools/publish.sh` 때문에 pull이 멈춘 오류), 문제 표에 이 오류 추가 |
| v1.3 | 2026-10-11 | 사용자 지시: 오디오는 고르지 않고 하나로 — 말투 시험(sample A~D)·`preset`·역할만 이은 트랙 삭제, 영상마다 `narration.mp3` 하나. 결과를 GitHub에 올리기 — `all --push`가 영상마다 대본 폴더에 `narration.mp3`·`tts_narration.json`·`tts_report.md`를 main에 커밋·푸시(2-2 토큰은 Kaggle Secrets만). 노트북 셀 하나(3번), 문제가 생겼을 때 표, 올리기 안전장치(4번) |
| v1.2 | 2026-10-10 | 사용자 지시: 사연자·진행자 역할과 목소리 설정 파일(`voices/storyteller.json`·`host.json`, 주제·영상별 덮어쓰기), 역할별 문장 파일·트랙의 정해진 경로(4번), 대본이 있는 영상을 모두 읽어 한 번에(`all`, 보류·업로드·옛 대본 처리), `pack`(zip)·`check`, Kaggle 셀 4개와 GitHub 웹 올리기 순서(3번), 목소리 바꾸기(6번) |
| v1.1 | 2026-10-10 | 3번: 도구 파일 내용을 셀에 붙여 넣지 말 것(`_IncompleteInputError`), 한 셀로 시험하기 |
| v1.0 | 2026-10-10 | 최초 작성: Qwen3-TTS 1.7B CustomVoice(Sohee), Kaggle 셀 4개, 억울·후회 말투 A~D, 도구 규칙(쉼·고지 카드·검사·볼륨) |
