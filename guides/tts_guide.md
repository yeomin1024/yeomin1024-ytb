# 내레이션 만들기 — 오픈소스 음성 AI(Qwen3-TTS)를 Kaggle에서 (모든 주제 공통)

버전: v1.3.1 — 2026-10-11 — 셀이 `git pull` 대신 Kaggle 사본을 main과 똑같이 맞춤 (`Your local changes ... would be overwritten by merge` 오류 해결) (v1.3: 사용자 지시: 오디오는 고르지 않고 하나로(말투 시험·선택 단계 삭제, 영상마다 `narration.mp3` 하나), 결과 파일은 GitHub의 대본 폴더마다 자동으로 올린다(`--push`), Kaggle 셀 하나 (v1.2: 사연자·진행자 목소리 설정 파일, 대본 전부 한 번에 `all`; v1.1: 셀에 도구 파일을 붙여 넣지 말 것; v1.0: 사용자 지시: edge-tts는 어색하다 → 오픈소스 음성 AI로, Kaggle에서, 사연은 억울하고 후회하는 톤)

도구: `tools/tts_narration.py` v1.2 · 목소리 설정: `voices/storyteller.json`(사연자), `voices/host.json`(진행자)
결과: 영상마다 오디오 **하나** — `<주제폴더>/source/<영상ID>/narration.mp3`가 **대본 폴더마다 각각** GitHub main에 자동으로 올라가고, 4단계(`guides/pipeline.md`)가 이어진다.
※ 연구·교육용 도구다. 주식 영상 내용은 투자 권유가 아니다.

## 1. 모델

| 항목 | 내용 |
|---|---|
| 모델 | `Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice` (Alibaba Qwen, 2026-01 공개) |
| 라이선스 | Apache-2.0 — 상업 이용 가능 (수익 창출 채널에 써도 됨) |
| 한국어 | 지원 10개 언어 중 하나. 한국어가 모국어인 화자 **Sohee**(따뜻한 여성, 감정 표현이 풍부함) |
| 말투 | `instruct`에 글로 지시 (예: "후회하고 억울한 목소리로, 낮게 떨리며 천천히"). 음색은 그대로, 감정·속도·억양이 바뀐다 |
| 주의 | **0.6B 모델은 말투 지시를 무시한다** (패키지 코드가 지시를 지움). 감정을 넣으려면 1.7B |

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
import os
os.environ["GITHUB_TOKEN"] = UserSecretsClient().get_secret("GITHUB_TOKEN")
!pip install -q -U qwen-tts
!test -d /kaggle/working/yeomin1024-ytb || git clone -q --depth 1 https://github.com/yeomin1024/yeomin1024-ytb.git /kaggle/working/yeomin1024-ytb
!cd /kaggle/working/yeomin1024-ytb && git config core.fileMode false && git fetch -q origin main && git reset -q --hard origin/main && python tools/tts_narration.py all --push
```
- 넷째 줄 뒤쪽은 Kaggle의 저장소 사본을 main과 **똑같이** 맞춘다 (`git pull` 대신). 이 사본은 도구를 돌리는 용도라 고쳐 쓰지 않는다. 사본에서 실행 권한만 바뀐 파일이 있으면 `git pull`이 `Your local changes to the following files would be overwritten by merge`로 멈췄다.
- 올리기가 실패해 사본에만 남은 커밋은 이 줄로 지워져도 괜찮다 — 결과는 `/kaggle/working/tts_out/upload/`에 있어 다음 실행이 다시 올린다.

하는 일:
1. 저장소를 받고(이미 있으면 main과 똑같이 맞추고), 대본(`<주제폴더>/source/<영상ID>/<영상ID>.txt`)을 **모두 읽어** 오디오가 없는 영상을 고른다. 로그 `[PLAN] video=… action=make|skip`
   - 건너뜀: 보류 주제(README에 ⏸), 이미 업로드한 영상(`youtube.json`), 지금 대본으로 만든 오디오가 이미 저장소에 있는 영상
   - 다시 만듦: 저장소의 오디오가 옛 대본으로 만든 것일 때 (Claude가 대본을 고친 뒤)
2. 영상마다 사연자·진행자 목소리로 문장을 만들어 **오디오 하나**(`narration.mp3`)로 잇는다.
3. **영상 하나가 끝날 때마다** 그 영상의 결과 3개를 그 영상의 대본 폴더에 넣어 main에 커밋·푸시한다. 로그 `[PUSH] … ok=True note="대본 폴더마다 올라감: stock/source/<영상ID>/"`
   - `narration.mp3` — 영상에 쓰는 오디오
   - `tts_narration.json` — 문장별 역할·시작·끝 시각, 대본 해시 (오디오가 지금 대본으로 만든 것인지 확인용)
   - `tts_report.md` — 문장별 길이·속도와 **귀로 확인할 문장**
4. 끝나면 Claude에게 **"오디오 올렸어"** → 영상 코드가 없으면 만들고, 렌더·비공개 업로드까지 승인 없이 진행한다 (`pipeline.md` 4단계).

- 걸리는 시간은 로그 `[PROGRESS] … eta_min=`에 나온다. 브라우저 탭을 열어 둔다. 중간에 끊기면 같은 셀을 다시 실행한다 — 이미 올라간 영상은 건너뛰고, 같은 세션이면 만든 문장은 cache에서 그대로 쓴다.
- 일부만: 마지막 줄 끝에 `--ids bittu-2026-10,panicsell-2026-10` · `--topics stock` · `--max 2`
- 무엇을 만들지 목록만 보기: `all --dry-run`

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

| 역할 | 읽는 문장 | 설정 파일 | 문장 파일 (Kaggle 작업 폴더, 올리지 않음) |
|---|---|---|---|
| 사연자 `storyteller` | 파트 라벨에 '사연'이 든 문장 (1인칭 고백) | `voices/storyteller.json` | `/kaggle/working/tts_out/<영상ID>/storyteller/S001.wav` … |
| 진행자 `host` | 나머지 모든 파트 (진행자·문제 분석·올바른 방법·마무리) | `voices/host.json` | `/kaggle/working/tts_out/<영상ID>/host/S017.wav` … |

- **결과는 영상마다 오디오 하나:** 두 역할을 대본 순서대로 이은 `narration.mp3`. 저장소의 **그 영상 대본 폴더** `<주제폴더>/source/<영상ID>/`에 올라간다 (예: `stock/source/bittu-2026-10/narration.mp3`).
- 문장 파일 번호 = 대본 문장 번호 (자막 도구 `srt_tool.py`와 같은 번호). 볼륨은 영상 전체에 맞춘 뒤의 소리다.
- 올리기 안전장치: 지금 대본과 다른 옛 결과, 저장소에 이미 있는 더 나중 결과는 올리지 않는다. 그 영상의 결과 3개 말고 다른 파일은 커밋하지 않는다. 가짜 소리(`--fake`)는 github.com에 올리지 않는다.
- `python tools/tts_narration.py check <주제폴더> <영상ID>`: 저장소 오디오가 지금 대본으로 만든 것인지 (`publish.sh`도 확인한다).
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
| 일괄 대상 | 보류 주제·업로드한 영상·지금 대본 오디오가 있는 영상은 건너뜀, 옛 대본 오디오는 다시 만듦 | 사용자 지시 2026-10-10 |

- 오디오가 만들어진 뒤에는 고치지 않는다(자르기·늘이기 금지). 이상하면 그 문장만 `--redo`로 다시 만들고 다시 잇는다.
- 저장소에서 `--fake`로 모델 없이 전 과정을 시험할 수 있다 (가짜 소리 → mp3 → `npm run align-audio`, 올리기는 시험용 로컬 저장소로만).

## 6. 목소리 설정 파일 (바꿀 때만 — 평소에는 손대지 않는다)

말투는 고르지 않는다. 바꿔야 하면 Claude에게 "사연자 목소리를 더 담담하게"처럼 말하면 설정 파일을 고쳐 main에 올린다. `voices/<역할>.json` 항목:

| 항목 | 뜻 | 기본값 |
|---|---|---|
| `parts` | 이 역할이 읽는 파트 라벨 낱말. `"*"`는 다른 역할이 맡지 않은 모든 파트 (한 역할만) | 사연자 `["사연"]`, 진행자 `["*"]` |
| `speaker` | 화자. 한국어가 모국어인 화자는 **Sohee** 하나 (다른 화자는 외국인 억양이 섞일 수 있음) | `Sohee` |
| `instruct` | 말투 지시. 음색보다 **감정·속도·쉼·억양**을 쓴다. 끝에 "Keep every word clear"(단어는 또렷하게) | 사연자: 억울·후회 고백 / 진행자: 차분한 진행 |
| `part_instruct` | 역할 안에서 파트별 말투 `{파트 낱말: 지시}`. 비우면 모두 `instruct` | 진행자: 분석·방법 = 또렷한 설명, 마무리 = 따뜻한 인사 |
| `seed` | 기본 시드. 바꾸면 그 역할의 문장을 모두 새로 만든다 | 1234 |
| `gap` | 그 역할의 문장 사이 쉼(초), 0.2 이상 | 0.45 |
| `generation` | 생성 설정 `{temperature, top_p, top_k, repetition_penalty}` | 모델 기본값 |

- 주제·영상마다 다르게: 바꿀 항목만 담은 같은 이름의 파일을 `<주제폴더>/voices/` 또는 `<주제폴더>/source/<영상ID>/voices/`에 둔다 (영상 > 주제 > 기본 순서로 덮어씀, 로그 `[ROLE] … files=`).
- 설정을 바꾸면 파일 안 `_버전`에 남긴다. 0.6B 모델은 말투 지시를 무시한다 (기본 1.7B).

## 변경 이력

| 버전 | 날짜 | 변경 내용 |
|---|---|---|
| v1.3.1 | 2026-10-11 | 셀 넷째 줄: `git pull` → `git config core.fileMode false && git fetch origin main && git reset --hard origin/main` (사본에서 실행 권한만 바뀐 `tools/publish.sh` 때문에 pull이 멈춘 오류), 문제 표에 이 오류 추가 |
| v1.3 | 2026-10-11 | 사용자 지시: 오디오는 고르지 않고 하나로 — 말투 시험(sample A~D)·`preset`·역할만 이은 트랙 삭제, 영상마다 `narration.mp3` 하나. 결과를 GitHub에 올리기 — `all --push`가 영상마다 대본 폴더에 `narration.mp3`·`tts_narration.json`·`tts_report.md`를 main에 커밋·푸시(2-2 토큰은 Kaggle Secrets만). 노트북 셀 하나(3번), 문제가 생겼을 때 표, 올리기 안전장치(4번) |
| v1.2 | 2026-10-10 | 사용자 지시: 사연자·진행자 역할과 목소리 설정 파일(`voices/storyteller.json`·`host.json`, 주제·영상별 덮어쓰기), 역할별 문장 파일·트랙의 정해진 경로(4번), 대본이 있는 영상을 모두 읽어 한 번에(`all`, 보류·업로드·옛 대본 처리), `pack`(zip)·`check`, Kaggle 셀 4개와 GitHub 웹 올리기 순서(3번), 목소리 바꾸기(6번) |
| v1.1 | 2026-10-10 | 3번: 도구 파일 내용을 셀에 붙여 넣지 말 것(`_IncompleteInputError`), 한 셀로 시험하기 |
| v1.0 | 2026-10-10 | 최초 작성: Qwen3-TTS 1.7B CustomVoice(Sohee), Kaggle 셀 4개, 억울·후회 말투 A~D, 도구 규칙(쉼·고지 카드·검사·볼륨) |
