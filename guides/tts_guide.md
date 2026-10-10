# 내레이션 만들기 — 오픈소스 음성 AI(Qwen3-TTS)를 Kaggle에서 (모든 주제 공통)

버전: v1.2 — 2026-10-10 — 사용자 지시: 대본을 사연자·진행자 파트로 나눠 역할마다 목소리 설정 파일(`voices/`), 역할별 오디오를 정해진 경로에, 대본이 있는 영상을 모두 읽어 한 번에(`all`), Kaggle 실행 셀 (v1.1: 셀에 도구 파일 내용을 붙여 넣지 말 것, 한 셀로 시험하기; v1.0: 사용자 지시: edge-tts는 어색하다 → 오픈소스 음성 AI로 자연스럽게, Kaggle에서 돌아가게, 사연은 주식 손실로 억울하고 후회하는 톤)

도구: `tools/tts_narration.py` v1.1 · 목소리 설정: `voices/storyteller.json`(사연자), `voices/host.json`(진행자)
결과: `narration_upload.zip` 하나 → 압축을 풀어 GitHub에 올리면 영상마다 `<주제폴더>/source/<영상ID>/narration.mp3`가 생기고 4단계(`guides/pipeline.md`)가 이어진다.
※ 연구·교육용 도구다. 주식 영상 내용은 투자 권유가 아니다.

## 1. 모델

| 항목 | 내용 |
|---|---|
| 모델 | `Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice` (Alibaba Qwen, 2026-01 공개) |
| 라이선스 | Apache-2.0 — 상업 이용 가능 (수익 창출 채널에 써도 됨) |
| 한국어 | 지원 10개 언어 중 하나. 한국어가 모국어인 화자 **Sohee**(따뜻한 여성, 감정 표현이 풍부함) |
| 말투 | `instruct`에 글로 지시 (예: "후회하고 억울한 목소리로, 낮게 떨리며 천천히"). 음색은 그대로, 감정·속도·억양이 바뀐다 |
| 주의 | **0.6B 모델은 말투 지시를 무시한다** (패키지 코드가 지시를 지움). 감정을 넣으려면 1.7B |

edge-tts와 다른 점: 문장 뜻을 읽고 억양·쉼을 스스로 정한다. 같은 문장도 시드마다 조금씩 다르게 읽으므로 이상한 문장만 다시 만들 수 있다 (3번 `--redo`).

## 2. Kaggle 준비 (처음 한 번)

1. kaggle.com → Create → **New Notebook**
2. 오른쪽 **Settings**
   - **Accelerator: GPU T4 x2** (P100은 최신 PyTorch가 지원하지 않을 수 있다)
   - **Internet: On** — 계정 휴대폰 인증이 있어야 켜진다
3. GPU 사용 시간은 주당 한도가 있다(계정 화면에 남은 시간이 나온다). 세션이 끝나면 `/kaggle/working`이 지워지므로 **만든 mp3는 바로 내려받는다.**

## 3. 노트북 셀 (이것만 복사해서 쓴다)

> ⚠️ `tools/tts_narration.py`의 **내용을 셀에 붙여 넣지 않는다.** 길어서 붙여 넣다 잘리면 `_IncompleteInputError: incomplete input`이 나고,
> 잘리지 않아도 저장소의 다른 파일(`tools/srt_tool.py`, `voices/`)이 있어야 돌아간다. 셀에는 아래 명령만 넣는다.

**셀 1 — 설치·저장소 받기** (세션마다 한 번, 몇 분)
```
!pip install -q -U qwen-tts
!test -d /kaggle/working/yeomin1024-ytb || git clone -q --depth 1 https://github.com/yeomin1024/yeomin1024-ytb.git /kaggle/working/yeomin1024-ytb
!cd /kaggle/working/yeomin1024-ytb && git pull -q
%cd /kaggle/working/yeomin1024-ytb
```
- 설치 중 의존성 경고(`pip's dependency resolver ...`)가 나올 수 있다. 다음 셀에서 오류가 나면 그 메시지(`[MODEL] ... error=... hint=...`)를 Claude에게 보여 준다.

**셀 2 — 목소리 시험 (처음 한 번, 선택)** — 처음엔 모델 받기 몇 분 + 생성
```
!python tools/tts_narration.py sample --roles --episode stock/bittu-2026-10
from IPython.display import Audio, display
for r in ("storyteller", "host"):
    print(r); display(Audio(f"/kaggle/working/tts_out/sample/sample_{r}.mp3"))
```
- 지금 설정 파일 그대로 사연자 4문장(사연 끝), 진행자 4문장(파트마다 첫 문장)을 만든다.
- 사연자 말투를 4가지로 비교하려면: `!python tools/tts_narration.py sample` → `sample_A.mp3`~`sample_D.mp3`

| 말투 | 이름 | 지시 요약 |
|---|---|---|
| A | 담담한 후회 | 낮고 느리게, 작은 한숨, 체념한 자책 |
| B | 울먹임 | 목이 메고 떨림, 울음을 삼키는 짧은 쉼 |
| C | 억울함 | 억울한 대목에서 올라가고 문장 끝은 후회로 가라앉음 |
| D | 한국어 지시 | A~C와 비슷한 내용을 한국어로 지시 (영어 지시와 비교용) |

  마음에 드는 글자를 Claude에게 "사연자 말투 B로"라고 하면 `voices/storyteller.json`의 `preset`을 바꿔 main에 올린다. 다음 셀 1의 `git pull`부터 반영된다.

**셀 3 — 대본 전부 → 오디오 (메인)**
```
!python tools/tts_narration.py all --dry-run
!python tools/tts_narration.py all
```
- 첫 줄은 목록만 본다: `[PLAN] video=… action=make|skip|done why=…`
- 둘째 줄이 저장소의 대본(`<주제폴더>/source/<영상ID>/<영상ID>.txt`)을 **모두 읽어** 오디오가 없는 영상을 차례로 만들고, 끝나면 `narration_upload.zip`으로 묶는다.
  - 건너뜀: 보류 주제(README에 ⏸), 이미 업로드한 영상(`youtube.json`), 지금 대본으로 만든 오디오가 이미 저장소에 있는 영상 (다시 만들려면 `--force`)
  - 다시 만듦: 저장소의 오디오가 옛 대본으로 만든 것일 때 (Claude가 대본을 고친 뒤). 그대로 두려면 `--keep-stale`
  - 일부만: `--ids bittu-2026-10,panicsell-2026-10` · `--topics stock` · `--max 2`
- 걸리는 시간은 로그 `[PROGRESS] … eta_min=`에 나온다. 브라우저 탭을 열어 둔다. 중간에 멈추면 같은 셀을 다시 돌린다 — 같은 세션이면 만든 문장은 cache에서 그대로 쓴다.
- **GPU 2개로 빠르게** (셀 2를 먼저 돌려 모델을 받아 둔 뒤): 영상을 반씩 나눠 동시에 만들고 마지막에 묶는다.
  ```
  !python tools/tts_narration.py all --gpu 0 --split 0/2 > /kaggle/working/log0.txt 2>&1 & python tools/tts_narration.py all --gpu 1 --split 1/2 > /kaggle/working/log1.txt 2>&1 & wait
  !grep -h "BATCH\|ERROR" /kaggle/working/log0.txt /kaggle/working/log1.txt
  !python tools/tts_narration.py pack
  ```

**셀 4 — 듣고 내려받기**
```
import glob
from IPython.display import Audio, display, FileLink
for f in sorted(glob.glob("/kaggle/working/tts_out/upload/*/source/*/narration.mp3")):
    print(f); display(Audio(f))
%cd /kaggle/working
FileLink("tts_out/narration_upload.zip")
```
- 링크를 눌러 `narration_upload.zip`을 받는다. 세션이 끝나면 `/kaggle/working`이 지워지므로 **바로 받는다.**
- 영상마다 `/kaggle/working/tts_out/<영상ID>/report.md`: 문장별 역할·시작 시각·길이·속도와 **귀로 확인할 문장** 목록
- 사연자만·진행자만 들어 보기: `/kaggle/working/tts_out/<영상ID>/storyteller.mp3`, `host.mp3`
- 이상한 문장만 다시 (새 시드, 같은 세션 안에서만): `%cd /kaggle/working/yeomin1024-ytb` 다음 `!python tools/tts_narration.py build stock panicsell-2026-10 --redo 12,15` → `!python tools/tts_narration.py pack` → 셀 4 다시

**올리기 (GitHub 웹)**
1. 받은 zip의 압축을 푼다. 안에 `stock/source/<영상ID>/narration.mp3`, `tts_narration.json`이 있다.
2. GitHub 저장소 첫 화면 → **Add file → Upload files** → 압축을 푼 **`stock` 폴더를 통째로 끌어 놓는다** (폴더 구조가 그대로 들어간다).
3. 아래 **Commit directly to the main branch** → Commit changes
4. Claude에게 "오디오 올렸어" → 영상 코드가 없으면 만들고, 렌더·비공개 업로드까지 승인 없이 진행한다 (`pipeline.md` 4단계).
- 파일당 25MB까지 (8~9분 mp3는 약 11MB). `tts_narration.json`은 같이 올린다 — 오디오가 지금 대본으로 만든 것인지 확인할 때 쓴다.

## 4. 사연자·진행자 역할과 결과 경로

| 역할 | 읽는 문장 | 설정 파일 | 문장 파일 (Kaggle) | 역할만 이은 트랙 |
|---|---|---|---|---|
| 사연자 `storyteller` | 파트 라벨에 '사연'이 든 문장 (1인칭 고백) | `voices/storyteller.json` | `tts_out/<영상ID>/storyteller/S001.wav` … | `tts_out/<영상ID>/storyteller.mp3` |
| 진행자 `host` | 나머지 모든 파트 (진행자·문제 분석·올바른 방법·마무리) | `voices/host.json` | `tts_out/<영상ID>/host/S017.wav` … | `tts_out/<영상ID>/host.mp3` |

- 문장 파일 번호 = 대본 문장 번호 (자막 도구 `srt_tool.py`와 같은 번호). 볼륨은 영상 전체에 맞춘 뒤의 소리다.
- **영상에 쓰는 오디오:** `tts_out/upload/<주제폴더>/source/<영상ID>/narration.mp3` — 두 역할을 대본 순서대로 이은 것. 저장소에서도 같은 경로다.
- `tts_narration.json` (narration 옆): 문장마다 역할·파트·시작·끝 시각, 대본 해시, 쓴 목소리 설정. `python tools/tts_narration.py check <주제폴더> <영상ID>`가 이 파일로 "지금 대본으로 만든 오디오인지" 본다 (`publish.sh`도 확인).
- 영상 코드의 사연 끝 번호(`plan.ts`의 `STORY_LAST`)와 사연자 마지막 문장 번호가 다르면 로그에 `[ROLE] … ok=False`가 나온다.

## 5. 도구가 지키는 규칙

| 규칙 | 값 | 근거 |
|---|---|---|
| 문장 = 대본 문장 | 파트 라벨·`[장면]`·카드 문구는 읽지 않음. 판정은 `srt_tool.parse_txt`와 같음 | `pipeline.md` 4단계 |
| 역할 | 파트 라벨에 `parts` 낱말('사연')이 있으면 사연자, 없으면 `"*"` 역할(진행자) | 사용자 지시 2026-10-10 |
| 문장 사이 쉼 | 역할 설정의 `gap`(기본 0.45초, 0.2초 이상), 파트가 바뀌면 1.0초, 완전 무음 | `align-audio`가 무음(−35dB, 0.12초 이상)으로 문장 경계를 찾음 |
| 고지 카드 자리 | `[장면]` 바로 앞 문장 뒤 4~8초 (카드 문구 글자 수 ÷ 7 + 1초) | 최소 3.5초 규칙 (`video_guide.md` 2번) |
| 첫 문장 앞 | 0.3초 | 첫 자막 앞 2초 이내 |
| 문장 검사 | 말 속도 2.5~8음절/초, 문장 안 무음 1.8초 이하, NaN·빈 소리 없음. 벗어나면 시드를 바꿔 최대 3번 | 성공 영상 4.2~5.5음절/초 (`stock/guides/data_insights.md` 2번) |
| 볼륨 | 영상 전체에 같은 이득 하나 (말소리 RMS −18dBFS, 최고점 −1dBFS 이하). 역할마다 따로 바꾸지 않음 | 문장마다 바꾸면 감정의 강약이 사라짐 |
| 부호 금액 | `-800만 원` → TTS에는 "마이너스 800만 원"으로 (대본·자막은 그대로) | 부호가 빠지면 뜻이 바뀜 |
| 읽는 소리 사전 | `<주제폴더>/tts_lexicon.tsv`, `source/<영상ID>/tts_lexicon.tsv` (`원문<TAB>읽는 소리`)가 있으면 씀 | 잘못 읽는 낱말 고치기 |
| 재현 | 시드 = 역할 설정의 `seed`(1234) + 문장 글로 정한 값 + 시도 번호. 로그·`cache/*.json`에 남음 | 같은 GPU·같은 설정이면 같은 소리 |
| 일괄 대상 | 보류 주제·업로드한 영상·지금 대본 오디오가 있는 영상은 건너뜀, 옛 대본 오디오는 다시 만듦 | 사용자 지시 2026-10-10 (대본이 생긴 파일을 모두 읽어 오디오 생성) |

- 오디오가 만들어진 뒤에는 고치지 않는다(자르기·늘이기 금지). 이상하면 그 문장만 `--redo`로 다시 만들고 다시 잇는다.
- 저장소에서 `--fake`로 모델 없이 전 과정을 시험할 수 있다 (가짜 소리 → mp3 → `npm run align-audio` 확인용). 역할마다 음 높이가 달라 귀로 구분된다.

## 6. 목소리 바꾸기 (설정 파일)

`voices/<역할>.json` 항목 (파일 안 `_항목`에도 설명이 있다):

| 항목 | 뜻 | 기본값 |
|---|---|---|
| `parts` | 이 역할이 읽는 파트 라벨 낱말. `"*"`는 다른 역할이 맡지 않은 모든 파트 (한 역할만) | 사연자 `["사연"]`, 진행자 `["*"]` |
| `speaker` | 화자. 한국어가 모국어인 화자는 **Sohee** 하나 (다른 화자는 외국인 억양이 섞일 수 있음, 목록은 로그 `[MODEL] speakers=`) | `Sohee` |
| `preset` | 사연 말투 시험 글자 `A`~`D`. 넣으면 `instruct` 대신 그 말투 | `""` |
| `instruct` | 말투 지시. 음색보다 **감정·속도·쉼·억양**을 쓴다. 끝에 "Keep every word clear"(단어는 또렷하게) | 사연자: 억울·후회 고백 / 진행자: 차분한 진행 |
| `part_instruct` | 역할 안에서 파트별 말투 `{파트 낱말: 지시}`. 비우면 모두 `instruct` | 진행자: 분석·방법 = 또렷한 설명, 마무리 = 따뜻한 인사 |
| `seed` | 기본 시드. 바꾸면 그 역할의 문장을 모두 새로 만든다 | 1234 |
| `gap` | 그 역할의 문장 사이 쉼(초), 0.2 이상 | 0.45 |
| `generation` | 생성 설정 `{temperature, top_p, top_k, repetition_penalty}` | 모델 기본값 |

- **주제·영상마다 다르게:** 바꿀 항목만 담은 같은 이름의 파일을 `<주제폴더>/voices/storyteller.json` 또는 `<주제폴더>/source/<영상ID>/voices/storyteller.json`에 둔다. 순서대로 덮어쓴다 (영상 > 주제 > 기본). 로그 `[ROLE] … files=`에 쓴 파일이 나온다.
- **시험만 할 때 (파일은 그대로):** `--story-style B` 또는 `--story-instruct "..."`(사연자), `--speaker`·`--seed`·`--gap`(모든 역할). 바뀐 값은 로그 `[VOICE] … note="명령줄 값이 설정 파일보다 우선"`에 남는다.
- 설정 파일을 바꾸면 버전·변경 이력을 남긴다 (파일 안 `_버전`). 바뀐 역할의 문장만 다시 만들고, 나머지는 같은 세션의 cache를 쓴다.
- 0.6B 모델은 말투 지시를 무시한다. 감정 표현은 1.7B (기본).

## 변경 이력

| 버전 | 날짜 | 변경 내용 |
|---|---|---|
| v1.2 | 2026-10-10 | 사용자 지시: 사연자·진행자 역할과 목소리 설정 파일(`voices/storyteller.json`·`host.json`, 주제·영상별 덮어쓰기), 역할별 문장 파일·트랙의 정해진 경로(4번), 대본이 있는 영상을 모두 읽어 한 번에(`all`, 보류·업로드·옛 대본 처리), `pack`(zip)·`check`, Kaggle 셀 4개와 GitHub 웹 올리기 순서(3번), 목소리 바꾸기(6번) |
| v1.1 | 2026-10-10 | 3번: 도구 파일 내용을 셀에 붙여 넣지 말 것(`_IncompleteInputError`), 한 셀로 시험하기 |
| v1.0 | 2026-10-10 | 최초 작성: Qwen3-TTS 1.7B CustomVoice(Sohee), Kaggle 셀 4개, 억울·후회 말투 A~D, 도구 규칙(쉼·고지 카드·검사·볼륨) |
