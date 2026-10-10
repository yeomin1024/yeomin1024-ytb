# 내레이션 만들기 — 오픈소스 음성 AI(Qwen3-TTS)를 Kaggle에서 (모든 주제 공통)

버전: v1.1 — 2026-10-10 — 셀에 도구 파일 내용을 붙여 넣으면 안 된다는 주의, 한 셀로 시험하기 (v1.0: 사용자 지시: edge-tts는 어색하다 → 오픈소스 음성 AI로 자연스럽게, Kaggle에서 돌아가게, 사연은 주식 손실로 억울하고 후회하는 톤)

도구: `tools/tts_narration.py` · 결과: `narration.mp3` → `<주제폴더>/source/<영상ID>/narration.mp3` 로 올리면 4단계(`guides/pipeline.md`)가 이어진다.

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

## 3. 노트북 셀

> ⚠️ `tools/tts_narration.py`의 **내용을 셀에 붙여 넣지 않는다.** 길어서 붙여 넣다 잘리면 `_IncompleteInputError: incomplete input`이 나고,
> 잘리지 않아도 저장소의 다른 파일(`tools/srt_tool.py`)이 있어야 돌아간다. 셀에는 아래 명령만 넣는다 (`!python tools/tts_narration.py ...`).

**한 셀로 바로 시험** (아래 셀 1·2를 합친 것):
```
!pip install -q -U qwen-tts
!test -d /kaggle/working/yeomin1024-ytb || git clone -q --depth 1 https://github.com/yeomin1024/yeomin1024-ytb.git /kaggle/working/yeomin1024-ytb
!cd /kaggle/working/yeomin1024-ytb && git pull -q && python tools/tts_narration.py sample
from IPython.display import Audio, display
for v in "ABCD":
    print(v); display(Audio(f"/kaggle/working/tts_out/sample/sample_{v}.mp3"))
```

셀 1 — 설치·저장소 받기 (세션마다 한 번, 몇 분)
```
!pip install -q -U qwen-tts
!test -d /kaggle/working/yeomin1024-ytb || git clone -q --depth 1 https://github.com/yeomin1024/yeomin1024-ytb.git /kaggle/working/yeomin1024-ytb
!cd /kaggle/working/yeomin1024-ytb && git pull -q
%cd /kaggle/working/yeomin1024-ytb
```
- 설치 중 의존성 경고(`pip's dependency resolver ...`)가 나올 수 있다. 셀 2에서 오류가 나면 그 메시지(`[MODEL] ... error=... hint=...`)를 Claude에게 보여 준다.

셀 2 — 말투 시험: 억울·후회 톤 4가지 (처음엔 모델 받기 몇 분 + 생성)
```
!python tools/tts_narration.py sample
from IPython.display import Audio, display
for v in "ABCD":
    print(v); display(Audio(f"/kaggle/working/tts_out/sample/sample_{v}.mp3"))
```
| 말투 | 이름 | 지시 요약 |
|---|---|---|
| A | 담담한 후회 | 낮고 느리게, 작은 한숨, 체념한 자책 |
| B | 울먹임 | 목이 메고 떨림, 울음을 삼키는 짧은 쉼 |
| C | 억울함 | 억울한 대목에서 올라가고 문장 끝은 후회로 가라앉음 |
| D | 한국어 지시 | A~C와 비슷한 내용을 한국어로 지시 (영어 지시와 비교용) |

- 실제 대본 문장으로 시험: `!python tools/tts_narration.py sample --episode stock/panicsell-2026-10 --lines 11-16`
- 직접 쓴 지시 시험: `--instruct "..."` (X로 추가된다)

셀 3 — 영상 전체 (고른 말투를 사연 파트에)
```
!python tools/tts_narration.py build stock panicsell-2026-10 --story-style B
```
- 진행자·분석·방법·마무리 파트는 차분한 설명 말투다 (`STYLES` in `tools/tts_narration.py`).
- 걸리는 시간은 로그 `[PROGRESS] ... eta_min=`에 나온다.
- GPU 2개로 나눠 빠르게 (셀 2를 먼저 돌려 모델을 받아 둔 뒤):
  ```
  !python tools/tts_narration.py build stock panicsell-2026-10 --story-style B --gpu 0 --shard 0/2 > /kaggle/working/log0.txt 2>&1 & python tools/tts_narration.py build stock panicsell-2026-10 --story-style B --gpu 1 --shard 1/2 > /kaggle/working/log1.txt 2>&1 & wait
  !python tools/tts_narration.py build stock panicsell-2026-10 --story-style B --assemble-only
  ```

셀 4 — 듣고 내려받기
```
from IPython.display import Audio, display, FileLink
display(Audio("/kaggle/working/tts_out/panicsell-2026-10/narration.mp3"))
%cd /kaggle/working
FileLink("tts_out/panicsell-2026-10/narration.mp3")
```
- `tts_out/<영상ID>/report.md`: 문장별 시작 시각·길이·속도와 **귀로 확인할 문장** 목록
- 이상한 문장만 다시 (새 시드): `!python tools/tts_narration.py build stock panicsell-2026-10 --story-style B --redo 12,15`
  - 같은 세션 안에서만 된다 (만든 문장 파일이 `/kaggle/working/tts_out/<영상ID>/cache/`에 있음)

그 뒤: `narration.mp3`를 GitHub 웹에서 `stock/source/<영상ID>/`에 올리고 Claude에게 "오디오 올렸어" → 4단계.

## 4. 도구가 지키는 규칙

| 규칙 | 값 | 근거 |
|---|---|---|
| 문장 = 대본 문장 | 파트 라벨·`[장면]`·카드 문구는 읽지 않음. 판정은 `srt_tool.parse_txt`와 같음 | `pipeline.md` 4단계 |
| 문장 사이 쉼 | 0.45초 (파트가 바뀌면 1.0초), 완전 무음 | `align-audio`가 무음(−35dB, 0.12초 이상)으로 문장 경계를 찾음 |
| 고지 카드 자리 | `[장면]` 바로 앞 문장 뒤 4~8초 (카드 문구 글자 수 ÷ 7 + 1초) | 최소 3.5초 규칙 (`video_guide.md` 2번) |
| 첫 문장 앞 | 0.3초 | 첫 자막 앞 2초 이내 |
| 문장 검사 | 말 속도 2.5~8음절/초, 문장 안 무음 1.8초 이하, NaN·빈 소리 없음. 벗어나면 시드를 바꿔 최대 3번 | 성공 영상 4.2~5.5음절/초 (`stock/guides/data_insights.md` 2번) |
| 볼륨 | 전체에 같은 이득 하나 (말소리 RMS −18dBFS, 최고점 −1dBFS 이하) | 문장마다 바꾸면 감정의 강약이 사라짐 |
| 부호 금액 | `-800만 원` → TTS에는 "마이너스 800만 원"으로 (대본·자막은 그대로) | 부호가 빠지면 뜻이 바뀜 |
| 읽는 소리 사전 | `source/<영상ID>/tts_lexicon.tsv` (`원문<TAB>읽는 소리`)가 있으면 씀 | 잘못 읽는 낱말 고치기 |
| 재현 | 시드 = 기본 시드(1234) + 문장 글로 정한 값 + 시도 번호. 로그·`cache/*.json`에 남음 | 같은 GPU·같은 설정이면 같은 소리 |

- 오디오가 만들어진 뒤에는 고치지 않는다(자르기·늘이기 금지). 이상하면 그 문장만 `--redo`로 다시 만들고 다시 잇는다.
- 저장소에서 `--fake`로 모델 없이 전 과정을 시험할 수 있다 (가짜 소리 → mp3 → `npm run align-audio` 확인용).

## 5. 말투 바꾸기

- 사연 파트: `--story-style A|B|C|D` 또는 `--story-instruct "..."` — 바뀐 사연 문장만 다시 만든다 (나머지는 cache 재사용).
- 다른 파트·기본값: `tools/tts_narration.py`의 `STYLES`를 고친다 (버전·변경 이력 남기기).
- 지시 쓰는 법: 음색(나이·성별)보다 **감정·속도·쉼·억양**을 쓴다. 끝에 "Keep every word clear"(단어는 또렷하게)를 붙이면 감정이 강해도 발음이 덜 뭉개진다.
- 화자를 바꾸려면 `--speaker` (목록은 로그 `[MODEL] speakers=`). 한국어는 Sohee가 가장 자연스럽다 (다른 화자는 외국인 억양이 섞일 수 있음).

## 변경 이력

| 버전 | 날짜 | 변경 내용 |
|---|---|---|
| v1.1 | 2026-10-10 | 3번: 도구 파일 내용을 셀에 붙여 넣지 말 것(`_IncompleteInputError`), 한 셀로 시험하기 |
| v1.0 | 2026-10-10 | 최초 작성: Qwen3-TTS 1.7B CustomVoice(Sohee), Kaggle 셀 4개, 억울·후회 말투 A~D, 도구 규칙(쉼·고지 카드·검사·볼륨) |
