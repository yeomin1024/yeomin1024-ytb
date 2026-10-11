# CHANGELOG — youtube_topic_analyzer

## 2026-10-11 — 음량 -14 LUFS (loudnorm v1.0, publish v1.3.0) · 썸네일 하단 제목 2줄·검은 배경 제목형 (thumbnail_guide v1.3) · 몰빵 업로드 자료

### 왜 바꿨나 (사용자 지시: "음량 맞추고 몰빵 업로드 자료 만들고 썸네일에 보니까 짧막한 문구만 중간중간 있고 하단에 두줄의 제목 관련 문구가 없잖아 지시사항에 반영해 그리고 썸네일 중 하나는 그냥 검은 배경에 제목 문구를 잘보이도록 그대로 넣는걸로 해봐 빨간색, 노란색 강조할 부분은 강조하고")
- 음량: 렌더한 4개가 -19.7~-20.5 LUFS. 유튜브는 큰 소리만 줄이고 작은 소리는 키워 주지 않아 다른 영상보다 작게 들림
- 썸네일: 사용자가 만든 주식 썸네일 9개(beb8e1e)에 "담보 부족", "-2,500만 원" 같은 짧은 문구만 있고 무슨 일인지 알려 주는 제목 문구가 없음

| 영역 | 함수/파일 | 변경 내용 |
|---|---|---|
| 도구 | `tools/loudnorm.py` v1.0 (신규) `measure`·`normalize`·`build_filter` | 측정(ffmpeg loudnorm) → 이득 = -14 - I → 이득 더한 피크가 -1.5 dBTP를 넘으면 리미터(alimiter, 한도 -2.0 dBFS, 5ms, 지연 보정) → 결과 다시 측정(목표 ±0.3 LU, TP ≤ -1.5)·필요하면 보정해 최대 3번 → 길이 같을 때만 원본 교체. 영상 스트림 복사. 이미 기준 안이면 건너뜀. 로그 `[LOUDNESS] stage=measure/plan/pass/done` |
| 도구 | `tools/publish.sh` v1.3.0 | 렌더·오디오 확인 바로 뒤 `loudnorm.py` (실패하면 그 영상만 멈춤, 원본 렌더는 그대로) |
| 지시사항 | `CLAUDE.md`, `guides/video_guide.md` v3.6, `guides/pipeline.md` v1.6, `guides/README.md` v1.6, `README.md` | 음량 규칙(-14 LUFS·트루 피크 -1.5 dBTP 이하, 내레이션 파일은 그대로) |
| 지시사항 | `guides/thumbnail_guide.md` v1.3 (1·2·3·4·4-1·4-2·6·7번), `guides/title_guide.md` v2.1 (11번 5항), 주제별 `thumbnail_rules.md` (stock·story v1.2, health v1.2, space·selfdev·lifetips v1.1), `CLAUDE.md` | 모든 썸네일 아래쪽에 제목 문구 2줄(짝 제목 앞 문장을 줄인 것, 한 줄 14자·합 26자 이내), 위쪽 펀치 문구는 1개·10자 이내. thumbnail_3 = 검은 배경 제목형(채택 제목 앞 문장 글자 그대로 3~4줄, 흰 글자 + 노랑·빨강 강조 3곳 이하) — 대비 축은 기본에서 뺌. 빨강 뜻은 주제 규칙: 주식·사연은 손실 숫자를 빨강으로 쓰지 않음(→ 노랑) |

### 측정 (전 → 후, `python3 tools/loudnorm.py --all`, 4코어 238초)
| 영상 | 통합 음량 LUFS | 트루 피크 dBTP | LRA | 이득 | 리미터 | 길이 |
|---|---|---|---|---|---|---|
| bittu-2026-10 | -19.68 → **-14.08** | -4.49 → -1.84 | 6.4 → 6.3 | +5.68 dB | 씀 | 458.333초 그대로 |
| multagi-2026-10 | -20.48 → **-14.07** | -4.43 → -1.88 | 6.0 → 5.9 | +6.48 dB | 씀 | 472.833초 그대로 |
| panicsell-2026-10 | -19.67 → **-14.07** | -4.43 → -1.86 | 5.8 → 5.8 | +5.67 dB | 씀 | 464.933초 그대로 |
| molppang-2026-10 | -20.35 → **-14.06** | -4.46 → -1.86 | 6.1 → 6.1 | +6.35 dB | 씀 | 477.033초 그대로 |
- 영상 스트림 md5가 4개 모두 전과 같음 (화면은 그대로). 30초 시험 구간에서 원본과 처리본의 오디오 지연 0ms (교차 상관) → 자막 싱크 그대로. 같은 파일에 다시 돌리면 `stage=skip reason=이미_기준_안`

### 썸네일 프롬프트 다시 쓰기 (19개 영상, 57개 파일)
| 영역 | 파일 | 변경 내용 |
|---|---|---|
| 산출물 | 18개 영상 `thumbnails/thumbnail_1·2.md` (v1.x → 다음 버전) | 그림은 위쪽 60%로, 펀치 문구 1개(10자 이내)만 남김, 하단 제목 2줄 추가([A]에 "Bottom title" 지시, [B]는 아래쪽 빈 어두운 띠) |
| 산출물 | 18개 영상 `thumbnails/thumbnail_3.md` (v2.0) | 대비 → 검은 배경 제목형: 채택 제목 앞 문장을 글자 그대로 3~4줄, 강조 노랑·빨강 3곳 이하(주제 색 뜻대로), [B]는 편집 프로그램으로 직접(1280×720 #000000, Noto Sans KR Black 약 100px) |
| 산출물 | 18개 영상 `titles.md` (T3 줄 괄호만), `README.md`(썸네일 줄) | 짝 썸네일 3 설명을 "(검은 배경 제목형 — 채택 제목 문구)"로 |
| 이미지 | `stock/source/{bittu,multagi,panicsell}-2026-10/thumbnails/thumbnail_1~3.png` → `thumbnails/old/` | 옛 규칙으로 만든 이미지(하단 제목 없음, 3번은 대비형)를 지우지 않고 옮김 → 업로드 도구가 옛 이미지를 쓰지 않고, 요약·`thumbnail_todo.md`에 다시 만들 것으로 나옴 |
| 지시사항 | `health`·`lifetips`·`selfdev`·`space` `thumbnail_rules.md` 문구 절 | 옛 "2줄 이하, 20자 이내" → 펀치 1개·10자, 하단 2줄 한 줄 14자·합 26자 |
| 산출물 | `*/summary.md` 19개, `*/thumbnail_todo.md` 6개 주제 (5개 새로) | `make_summary.py --all`, `--thumb-todo` 다시 생성 |
- 검사(임시 스크립트): 19개 영상 × 3개 모두 통과 — 1·2번은 [A]에 하단 2줄(줄마다 14자 이내·합 26자 이내), 3번은 #000000·3~4줄·이은 글자 = 채택 제목 앞 문장(마침표만 뺌)

### 몰빵 업로드 자료 (`stock/source/molppang-2026-10/`)
- `titles.md`: T1(채택) "한 종목에만 몰빵해서 얻은 천만원 수익이 -2천만원이 됐습니다. 한 종목 올인한 사람들의 최악의 결말" (기준 제목, `stock/guides/title_rules.md` 5번), T2 속마음·공통점, T3 짧은 변형(CEO 이적 소식)
- `thumbnails/thumbnail_1~3.md` (v1.3 규칙: 계좌 카드 +1,000만 원 → -2,000만 원 / 가상 인물 / 검은 배경 제목형)
- `upload.md`: 설명란·챕터 12개(오디오에 맞춘 SRT 시각)·태그 15개·고정 댓글·투자 유의 사항·출처. `youtube_upload.py --dry-run` 결과 "문제 없음". 블룸버그 2022-02-11 링크는 검색 결과로 기사 제목·주소 확인("두 명만 매도 의견")
- `stock/README.md`·`README.md` 몰빵 줄 갱신

## 2026-10-11 — Kaggle 내레이션으로 영상 4개 렌더 + 요약 상태표 오류 수정 (make_summary v1.3.2)

### 왜 바꿨나 (사용자 지시: "오디오 만들어졌는지 확인하고 잘됐으면 영상 만들어")
- 4개 영상(bittu·multagi·panicsell·molppang)의 `narration.mp3` 확인: `tts_narration.py check` 모두 ok, 보고서상 다시 할 문장 0, 진행자 목소리 높이 135~138Hz로 영상마다 같음
- 자막은 align-audio v1.2(`tts_narration.json`의 문장 시각)로 맞춘 뒤 렌더. 몰빵은 영상 코드가 없어서 새로 만듦 (`video/CHANGELOG.md`)

| 영역 | 함수/파일 | 변경 내용 |
|---|---|---|
| 도구 | `tools/make_summary.py` v1.3.2 `build` 상태표 | 썸네일 줄이 프롬프트 파일이 없어도 "프롬프트 3개 ✅"로 나오던 오류 → `thumbnails/thumbnail_N.md` 개수를 세서 3개가 아니면 "❌ 프롬프트 n/3". 다른 영상 3개는 결과 같음(생성 시각 줄만 다름) |
| 산출물 | `stock/source/molppang-2026-10/summary.md` (신규) | 몰빵 요약: 제목·썸네일 프롬프트·업로드 시트가 아직 없다고 표시 (업로드 전에 필요) |
| 렌더(커밋 안 함) | `stock/out/<영상ID>/final_1080p.mp4` | bittu 7:38, multagi 7:53, panicsell 7:45, molppang 7:57. 통합 음량 약 -20 LUFS. 유튜브 키가 없어 업로드는 건너뜀 |
## 2026-10-11 — 주식 밖 5개 주제: 분석 → 주제 규칙 → 영상 3개씩 패키지(오디오 전까지)

### 왜 (사용자 지시)
- "주식을 제외한 나머지 건강, 우주 등 주제도 분석기 돌려서 오디오 전까지 3개까지 만들어봐" → 주제마다 최대 3개 (사용자 선택)

### 1단계 분석 (클라우드, `bash tools/run_analysis.sh <주제> -- --keywords 13 --skip-install`)
| 주제 | 쿼터 | 수집 | 비고 |
|---|---|---|---|
| health · space · selfdev · story · lifetips | 1,958 · 1,782 · 1,920 · 1,990 · 2,006 (합 9,656 / 하루 10,000) | 주제마다 키워드 13개(설정 48개 중, 카테고리 순환) | 남은 키워드는 다음 실행에서 (검색 7일 캐시) |
- 클라우드 네트워크 정책으로 `suggestqueries.google.com`(자동완성 수요), `www.youtube.com`(자막·쇼츠 확인), 썸네일 이미지가 막힘 → 수요 점수 0, 성공사례 대본·썸네일 없음. 각 주제 `guides/data_insights.md`에 한계로 적고 말하기 속도·도입부·썸네일은 주식 결과를 임시로 씀

### 2단계 주제 규칙 (각 `<주제>/guides/`, `README.md`, `source/used_content.md`, `voices/storyteller.json`)
- health v1.1~1.2(분석 반영, 1900년대 자료 DPP는 사용 불가), space·selfdev·lifetips v1.0~1.1(새로 만듦), story v1.0~1.2(대본 규칙 새로 만듦)
- 건강·사연 README의 ⏸ 보류 해제 (보류 조건이 "분석 결과 전까지"였음) → 내레이션 도구가 이 주제들도 읽음
- 주제마다 사연자 말투만 덮어쓰는 `voices/storyteller.json` (공통 instruct가 "주식 손실 고백"이라). 화자 Sohee·진행자 기준 목소리는 그대로

### 3단계 영상 패키지 15개 (각 `<주제>/source/<영상ID>/`: 대본 TXT·SRT·README(검산·출처)·제목 3개·썸네일 프롬프트 3개·업로드 시트·요약)
| 주제 | 영상ID (추정 길이) |
|---|---|
| 건강 | prediabetes-2026-10 v1.1 (9:03, DPP → 영국 NDPP·독일 PLIS 2023) · supplement-liver-2026-10 (11:48) · sarcopenia-2026-10 (10:18) |
| 우주 | nuriho-2026-10 (11:52) · voyager-2026-10 (12:14) · asteroid-2026-10 (12:28) |
| 자기계발 | miraclemorning-2026-10 (11:01) · habit21-2026-10 (10:37) · dopaminedetox-2026-10 (11:57) |
| 사연 | myeoneuri-2026-10 (12:14) · jeungyeo-2026-10 (12:20) · chayongjeung-2026-10 (11:13) |
| 생활꿀팁 | washer-2026-10 (8:39) · heater-2026-10 (8:43) · bleach-2026-10 (8:29) |
- 15개 모두 `srt_tool.py check` 4항목 ✅, `tts_narration.py all --dry-run`에 15개 모두 "오디오 없음 → make"로 잡힘
- 읽는 소리 사전 `tts_lexicon.tsv`: health(kg·범위 물결표), selfdev(범위 물결표), 영상별(H3·2024 YR4·119·AST/ALT 등) — TTS에만 쓰고 대본·자막은 그대로
- 확인하지 못한 숫자는 쓰지 않음: 예) 근감소증 '50~64세 의자 일어서기 10초'(출처마다 10/12초) → 확인된 12초 기준으로, 소행성 생존 용품 230만 → 150만 원(가격 확인분만)
- 이 환경은 WebFetch·curl로 원문을 열 수 없어 모든 근거를 웹 검색 결과의 인용으로 확인 — 각 README 출처 표에 확인 방법을 적음

### 다음
- 사용자: Kaggle 셀 하나(`python tools/tts_narration.py all --push`, `guides/tts_guide.md` 3번) → 15개 오디오가 대본 폴더마다 main에 올라감 → "오디오 올렸어" → 4단계(영상 코드·렌더·비공개 업로드, 한 번에 최대 3개)
- 썸네일 이미지는 사용자가 각 `thumbnails/thumbnail_N.md`의 [A] 프롬프트로 이미지 AI에서


## 2026-10-11 — 진행자는 중저음 남성, 모든 대본에서 같은 목소리 (tts_narration v1.3)

### 왜 바꿨나 (사용자 지시)
- 진행자 목소리는 중저음의 남성이지만 적당히 귀에 쏙쏙 들어오고 신뢰도 높은 목소리로, 그리고 대본마다 달라지면 안 된다
- 문제: 지금 모델(CustomVoice)의 한국어 원어민 화자는 여성 Sohee 하나뿐 (남성 화자는 외국인 억양). 패키지 소스(`qwen-tts` 0.1.1)로 확인한 방법: VoiceDesign `generate_voice_design(text, instruct, language)` → Base `create_voice_clone_prompt(ref_audio=(wav, sr), ref_text)` + `generate_voice_clone(..., voice_clone_prompt)`

| 영역 | 함수/파일 | 변경 내용 |
|---|---|---|
| 도구 | `tools/tts_narration.py` v1.3 `QwenPool` (QwenEngine 대체) | 모델 세 가지를 필요할 때 불러옴: 사연자 CustomVoice(GPU 0), 진행자 Base 복제(GPU 1), 기준 목소리 만들기 VoiceDesign(한 번만, 끝나면 내림). GPU 하나면 번갈아 올림. 복제 프롬프트는 기준 목소리마다 한 번 |
| 도구 | 같은 파일 `ensure_reference`, `voice` 명령 | `voices/ref/host.wav`가 없으면 `voices/host.json`의 design 묘사로 시드 6개 만들어 검사(목소리 높이 85~150Hz, 110Hz에 가깝게, 속도 3.8~6.0음절/초, 무음 1초 이하) → 고른 것을 `voices/ref/host.wav`·`host.json`(해시 포함)로 저장하고 main에 올림. 범위 밖뿐이면 멈춤, 못 올리면 오디오를 만들지 않음 |
| 도구 | 같은 파일 `f0_median`(신규), `make_sentence` | 목소리 높이(기본 주파수) 측정: 40ms 구간 FFT 자기상관, 큰 소리·주기가 뚜렷한 구간 중간값. 진행자 문장이 기준 ±30% 밖이면 다시(최대 3번), 보고서에 문장마다 높이 |
| 도구 | 같은 파일 `load_voices`(lock·engine·clone 검사), `attach_reference`(해시 검사), `voice_ids`, `voice_mismatch`, `repo_status`, `cmd_check` | 진행자 `lock`: 주제·영상 덮어쓰기·명령줄 값 무시. 오디오마다 목소리 정체(모델·기준 목소리 해시·설정)를 남기고, 바뀌면 "다른 목소리"로 다시 만듦 (v1.2 이하 오디오도 다시). `--split`은 복제 모델이 있으면 막음(한 프로세스가 GPU 2개) |
| 설정 | `voices/host.json` v2.0, `voices/storyteller.json` v1.2 | 진행자: engine clone, lock, design(30대 후반 남성, 따뜻한 중저음 바리톤, 뉴스 앵커·다큐 내레이터처럼 신뢰감, 또렷한 발음, 숫자에 힘, 보통 속도 / 기준 문장 49음절 약 10초). 사연자: engine custom_voice(그대로 Sohee) |
| 도구 | `tools/publish.sh` v1.2.2 | 건너뜀 표시: 옛 대본·목소리로 만든 오디오 |
| 지시사항 | `guides/tts_guide.md` v1.4(1번 모델 표, 4-1), `guides/pipeline.md` v1.5, `guides/README.md` v1.5, `CLAUDE.md`, `README.md` | 진행자 목소리 규칙과 바꾸는 법 |

### 검증 (가짜 소리, 로컬 시험용 원격 저장소)
- 높이 측정: 110Hz 톱니파 → 110.1Hz, 120Hz+잡음 → 120.0, 220Hz → 220.2, 무음 → 0. 9초 소리 한 번 약 26ms
- 첫 실행: 기준 목소리 시도 6번(198·123·175·99·152·76Hz) → 범위 안 3개 중 110Hz에 가까운 99Hz 선택 → `voices/ref/host.wav` 커밋·푸시 → 빚투·패닉셀 진행자 문장 모두 같은 기준(해시 같음), 문장 높이 97~105Hz
- 다시 실행: 둘 다 "지금 대본·목소리와 같음"으로 건너뜀 / 주제 폴더에 진행자 덮어쓰기 파일 → lock으로 무시, check ok
- 기준 목소리를 바꿈(design 시드 변경 + `voice --force --push`) → 두 영상 `check` ok=False "목소리:host", `publish.sh`가 건너뜀 → `all --push`가 둘 다 새 목소리로 다시 만들어 올림(두 영상 기준 해시 같음)
- `--split` 막음, `--assemble-only` 캐시로 잇기 정상
- 실제 남성 목소리는 Kaggle 첫 실행에서 만들어짐 (이 환경은 모델을 받을 수 없음)

## 2026-10-11 — Kaggle 셀 `git pull` 오류 해결 (tts_narration v1.2.1, tts_guide v1.3.1)

- 증상: `error: Your local changes to the following files would be overwritten by merge: tools/publish.sh`
- 원인: Kaggle의 저장소 사본에서 `tools/publish.sh`의 실행 권한(파일 모드 100755)만 바뀐 상태 → main의 같은 파일이 바뀌자(v1.2.1 주석) `git pull`이 합치지 못하고 멈춤. 같은 상황을 재현해 확인(실행 권한을 뺀 사본 + 한 커밋 뒤 → pull 이 같은 오류)
- 셀: `git pull` → `git config core.fileMode false && git fetch -q origin main && git reset -q --hard origin/main` (사본을 main과 똑같이). 재현한 사본에서 깨끗하게 최신(43c7e9c)으로 맞춰짐
- `tools/tts_narration.py` v1.2.1 `Git.run`: 모든 git 실행에 `core.fileMode=false`. `push_preflight`: 사본의 다른 변경 파일을 경고로 알림(커밋하지 않음)
- 올리기가 실패해 사본에만 남은 커밋이 reset으로 지워져도 결과는 `tts_out/upload/`에 남아 다음 `all --push`가 다시 올림 (시험으로 확인)

## 2026-10-11 — 오디오는 하나로(고르지 않음), 결과는 Kaggle에서 대본 폴더마다 GitHub에 자동으로 (tts_narration v1.2)

### 왜 바꿨나 (사용자 지시)
1. 오디오를 고르지 말고 그냥 하나로
2. 결과 파일을 GitHub에 올리도록 — 오디오는 대본별 폴더에 각각

| 영역 | 함수/파일 | 변경 내용 |
|---|---|---|
| 도구 | `tools/tts_narration.py` v1.2 — `cmd_sample`, `SAMPLE_STYLES`, `preset`, `--story-style/--story-instruct` 삭제 | 말투 시험·선택 단계 없음. 역할마다 설정 파일의 말투 하나 |
| 도구 | 같은 파일 `build_episode` | 역할만 이은 트랙(`storyteller.mp3`·`host.mp3`) 삭제 → 결과 오디오는 영상마다 `narration.mp3` 하나. 보고서는 `tts_report.md`로 결과 옆에. mp3를 못 만들면 멈춤 |
| 도구 | 같은 파일 `get_token`, `Git`, `push_preflight`, `push_results`, `cmd_push` (신규), `all/build --push`, `push` 명령 | 영상 하나가 끝날 때마다 결과 3개(`narration.mp3`·`tts_narration.json`·`tts_report.md`)를 **그 영상의 대본 폴더** `<주제>/source/<영상ID>/`에 복사 → 그 파일만 커밋 → `pull --rebase --autostash` → `push origin HEAD:main` (최대 4번, 2·4·8·16초 간격). 토큰은 환경 변수 또는 Kaggle Secrets `GITHUB_TOKEN`, `GIT_ASKPASS`로만 넘김(로그·명령줄·원격 주소·설정에 없음, 출력은 가림). 시작 전 `push --dry-run`(없는 브랜치 이름)으로 권한 확인 → 안 되면 GPU 쓰기 전에 멈춤. 두 프로세스(`--split`)는 잠금 파일로 차례로. 안전장치: 옛 대본 결과·저장소의 더 나중 결과는 안 올림, 가짜 소리는 github.com에 안 올림, 다른 확장자 옛 내레이션은 지움 |
| 설정 | `voices/storyteller.json`·`host.json` v1.1 | `preset` 삭제 |
| 지시사항 | `guides/tts_guide.md` v1.3, `guides/pipeline.md` v1.4, `guides/README.md` v1.4, `CLAUDE.md`, `README.md`, `tools/make_summary.py` v1.3.1(문구), `tools/publish.sh` v1.2.1(주석) | Kaggle 셀 하나, GitHub 토큰 만들기(이 저장소만·Contents 읽기/쓰기·Kaggle Secrets), 문제가 생겼을 때 표, zip·웹 업로드는 마지막 수단 |

### 검증 (가짜 소리, 로컬 시험용 원격 저장소 — 실제 GitHub에는 올리지 않음)
- 전후 비교 (빚투, `--fake`): v1.1 mp3 내보내기 3개(narration + 역할 트랙 2) 18.2초 → v1.2 1개 8.2초. 문장 시각·역할(사연자 1–16 / 진행자 17–88)·쉼 구성은 v1.1과 같음
- `all --push`: 빚투·패닉셀 영상마다 커밋 1개, 각 커밋에 그 대본 폴더의 3파일만 → 원격이 앞서 있어도 rebase 후 push 성공. 다시 실행하면 둘 다 has_audio로 건너뜀, `check` ok=True, `publish.sh --dry-run` 후보 2개
- 거부(pre-receive) → 4번 다시 시도 후 ok=False·종료 1 → 원격이 받아 주자 `push`가 남아 있던 커밋을 올림
- `--split 0/2·1/2` 동시 실행 → 두 영상 모두 올라감(잠금)
- 얕은 clone(`--depth 1`, Kaggle 셀과 같음)이 원격보다 뒤처져 있어도 올라감
- 가드: 가짜 소리 + github.com 원격 → 멈춤 / 토큰 없음 → 모델을 불러오기 전에 멈춤 / 옛 대본 결과 → 안 올림 / 저장소에 더 나중 결과 → 안 덮어씀 / 로그에 토큰 문자열 0회
- 실제 모델 음성·실제 GitHub 올리기는 Kaggle에서 처음 실행

## 2026-10-10 — 사연자·진행자 두 목소리, 대본 전부 한 번에 오디오, 스토리보드 삭제, 사례는 최신으로 (tts_narration v1.1)

### 왜 바꿨나 (사용자 지시)
1. 요약에 스토리보드까지 하라고 했는데 그건 하지 말고, 오디오가 만들어지면 그냥 영상을 만든다 (승인 단계 없음)
2. 대본에서 사연자와 진행자 파트를 나누고, 역할마다 목소리 톤 설정 파일을 만들고, 역할마다 정해진 경로에 오디오가 생기게
3. 대본이 생성된 파일들을 모두 읽고 오디오가 생기게
4. 대본 4개의 사례는 되도록 최신 사례로 — 1900년대는 너무 옛날
5. 오디오 생성 코드를 실행하는 코드(Kaggle 셀)를 알려 주고, 말한 내용을 모두 지시사항에 반영

| 영역 | 함수/파일 | 변경 내용 |
|---|---|---|
| 도구 | `tools/tts_narration.py` v1.1 `load_voices`, `role_of`, `instruct_for`, `plan_items` | 역할 = 목소리 설정 파일 `voices/<역할>.json`. 파트 라벨에 `parts` 낱말('사연')이 있으면 사연자, 없으면 `"*"` 역할(진행자). 주제·영상 폴더의 같은 이름 파일이 덮어씀. 역할별 문장 범위·말투를 `[ROLE]`·`[STYLE]` 로그로, `plan.ts`의 `STORY_LAST`와 사연자 끝 번호 비교 |
| 도구 | 같은 파일 `build_episode` | 정해진 경로: `OUT/upload/<주제>/source/<영상ID>/narration.mp3`+`tts_narration.json`(저장소와 같은 경로), 역할별 `OUT/<영상ID>/<역할>/S###.wav`·`<역할>.mp3`. 문장 사이 쉼은 역할 설정 `gap` |
| 도구 | 같은 파일 `cmd_all`, `discover`, `pack`, `cmd_check` (신규) | `all`: 저장소의 대본(`*/source/<id>/<id>.txt`)을 모두 읽어 할 일 표 → 모델 한 번 불러 차례로 만들고 zip. 건너뜀: 보류 주제(⏸)·업로드한 영상·지금 대본 오디오가 있는 영상. 옛 대본 오디오는 다시 만듦(`--keep-stale`로 끔). GPU 2개 `--split 0/2·1/2` → `pack`. `check`: 저장소 오디오가 지금 대본으로 만든 것인지(대본 해시·바뀐 문장 번호) |
| 도구 | 같은 파일 `QwenEngine`, `cache_key` | 화자·생성 설정을 문장마다(역할 설정) 넘김. 캐시 키는 v1.0과 같은 모양(기본 설정이면 v1.0 캐시 그대로). `--out-dir`은 결과 최상위 폴더로 |
| 설정 | `voices/storyteller.json`, `voices/host.json` (신규) | v1.0의 말투 그대로 옮김: 사연자 = 억울·후회 고백, 진행자 = 차분한 진행 + `part_instruct`(분석·방법 = 또렷한 설명, 마무리 = 따뜻한 인사). Sohee, 시드 1234, 쉼 0.45초 |
| 도구 | `tools/make_summary.py` v1.3 | 스토리보드 절·상태 줄 삭제 → "내레이션 역할"(사연자 1–16 · 진행자 17–88)·"영상 코드" 상태, 대본 파트마다 🎙 역할, 오디오가 옛 대본이면 ⚠️. `--all`은 보류 주제 건너뜀 |
| 도구 | `tools/publish.sh` v1.2 | 스토리보드 단계 삭제. `tts_narration.json`이 있으면 `check`로 옛 대본 오디오를 건너뜀. 영상 코드가 없으면 "Claude가 만든 뒤 다시(승인 대기 없음)" |
| 대본 | 몰빵 v2.1 (문장 40~43, 45~47) | 베셈바인더(1926~2016년 미국 주식) → 자본시장연구원 2024(2023년 말까지 10년 국내 상장사 52%가 1년짜리 안전한 채권보다 못 벎, 대형주 58%)·한국경제 2026(코스피가 두 배 넘게 오른 6월까지 지수를 이긴 종목 4% 미만). JP모건(1980년 이후) → 엔씨소프트·LG생활건강 2021년 고점 대비 -70% 넘게·5년 넘게 회복 못 함·그사이 코스피 2배. 카카오는 물타기에 써서 뺌. 문장 51 손실 회피 출처를 2024 메타분석(JEL)으로. 자막 117 → 116 |
| 대본 | 패닉셀 v1.1 (문장 80~85) | 탈러 등 1997년 실험 → 자본시장연구원 2021(2020년 개인투자자 20만 명: 신규 투자자 거래 두 배 가까이, 비용 뺀 수익률 기존 15% vs 신규 -1.2%, 자주 사고팔수록 시장보다 덜 벎). 자막 109 → 111, 정리 챕터 8:01 → 8:09 |
| 대본 | 물타기 v1.4 (문장 41~45, 49~55) | 오딘 1998(1987~1993년 계좌) → 자본시장연구원 2022(2020년 개인 약 20만 명: 산 다음 날 수익 종목 41% vs 손실 종목 22% 매도, 처분효과 최강 그룹 -9.8% vs 손실부터 정리한 그룹 +4.9%). 베어링스 은행 1995 → 카카오 2021~2026(빅테크 규제 주간 개인 1조 원 넘게, 2022년 2조 원 넘게 순매수, 소액주주 206만 명, 2026-10 3만 2천 원대 = 고점의 5분의 1 미만). 자막 110 → 107, 챕터 4:23부터 다시 계산 |
| 지시사항 | `guides/pipeline.md` v1.3, `guides/README.md` v1.3, `guides/video_guide.md` v3.5, `guides/tts_guide.md` v1.2, `guides/script_guide.md` v2.3, `stock/guides/script_rules.md` v1.3, `CLAUDE.md`, `README.md` | 3단계에서 영상 코드·스토리보드·승인 삭제 → 4단계 0번(오디오가 생기면 Claude가 영상 코드, still 자체 점검, 바로 렌더). 3-6 내레이션(역할·설정 파일·`all`·zip·GitHub 웹 올리기). 사례는 되도록 최신(2020년대 먼저, 1900년대 사건·자료 쓰지 않음). Kaggle 셀 4개 |

### 검증
- `--fake`(가짜 소리) 빚투: 사연자 16문장(1–16)·진행자 72문장(17–88), `plan.ts` STORY_LAST=16 일치. 쉼 구성은 v1.0과 같음(문장 83·파트 3·카드 1·끝 1), 555.45초. `npm run align-audio --dry-run`이 고지 카드 쉼 7.98초를 찾고 자막 105개를 맞춤
- `all --split 0/2`·`1/2` 동시 실행 → 4개 영상(빚투·몰빵·물타기·패닉셀) 각각 made, 보류 주제(건강) 건너뜀 → `pack` zip 8개 파일 45.6MB → 다시 `all --dry-run`은 4개 모두 done
- `check`: 같은 대본 ok=True(종료 0) / 대본 해시·문장 52 바꾼 메타 → ok=False changed=52(종료 1), `all`은 stale로 표시. `publish.sh --dry-run`이 옛 대본 오디오를 건너뜀
- `--assemble-only`(88/88 캐시), `--redo 12,15`(사연자 2문장만 시도 2), `--shard 0/2·1/2` → `--assemble-only` 92문장, `sample --roles`(대본·내장 문장), `sample --story-style B`
- 실제 모델 음성은 이 환경에서 만들 수 없음(Hugging Face 차단) → Kaggle에서 사용자가 실행

## 2026-10-10 — 내레이션 만들기: 오픈소스 음성 AI(Qwen3-TTS)를 Kaggle에서 (tts_narration v1.0)

### 왜 바꿨나 (사용자 지시)
1. edge-tts는 너무 어색하다 → 오픈소스 음성 AI로 자연스럽게
2. Kaggle에서 돌아가는 코드로
3. 사연은 주식 손실로 억울하고 후회하는 톤으로

| 영역 | 함수/파일 | 변경 내용 |
|---|---|---|
| 도구 | `tools/tts_narration.py` v1.0 (신규) | Qwen3-TTS 1.7B CustomVoice(Apache-2.0, 한국어 화자 Sohee) + 파트별 말투 지시(`STYLES`: 사연=억울·후회, 진행자·분석·마무리=차분한 설명). `sample`(말투 A~D 비교) / `build`(대본 → `narration.mp3` + `report.md`) |
| 도구 | 같은 파일 `read_script` | 문장·카드 판정은 `srt_tool.parse_txt`·`parse_cards`를 그대로 씀(결과가 다르면 멈춤) |
| 도구 | 같은 파일 `make_sentence`, `check` | 문장마다 검사(말 속도 2.5~8음절/초, 문장 안 무음 1.8초 이하, NaN·빈 소리) → 시드를 바꿔 최대 3번, 통과 못 하면 가장 나은 것 + "귀로 확인" 표시. 문장 파일 캐시(글·말투·화자·설정이 같으면 재사용), `--redo`는 새 시드 |
| 도구 | 같은 파일 `cmd_build` 잇기 | 문장 사이 0.45초·파트 1.0초 무음, 고지 카드 자리 4~8초(`parse_cards` 길이, 최소 3.5초 규칙), 첫 문장 앞 0.3초. 볼륨은 전체 이득 하나(RMS −18dBFS, 최고점 −1dBFS) |
| 도구 | 같은 파일 `tts_text` | TTS 입력만 `-800만` → "마이너스 800만", `+55만` → "플러스 55만" (대본·자막은 그대로), 선택 사전 `tts_lexicon.tsv` |
| 도구 | 같은 파일 `QwenEngine` | T4(연산 능력 7.5)는 float32 기본(bfloat16 장치 없음, float16은 NaN 위험), A100 등은 bfloat16. GPU 2개 나눠 만들기 `--shard 0/2·1/2` + `--assemble-only` |
| 지시사항 | `guides/tts_guide.md` v1.1 (신규, v1.1: 셀에 도구 파일을 붙여 넣지 말 것·한 셀 시험),  `guides/pipeline.md` v1.2, `guides/README.md` v1.2, 저장소 `README.md` | Kaggle 셀 4개(설치 → 말투 시험 → 전체 → 듣기·내려받기), 도구 규칙, 말투 바꾸는 법 |

### 검증
- 모델 API: `qwen-tts` 0.1.1 패키지 소스로 확인 — `Qwen3TTSModel.from_pretrained`, `generate_custom_voice(text, speaker, language, instruct, **generate kwargs)`, 출력 24kHz(24000 ÷ 1920 = 초당 12.5 프레임), 0.6B는 instruct 무시
- 이 작업 환경에서는 Hugging Face 접속이 막혀(403) **실제 모델 음성은 만들지 못함** → Kaggle에서 사용자가 `sample` 실행 필요
- `--fake`(가짜 소리)로 패닉셀 대본 전체: 문장 92개, 9분 23초 mp3 11.3MB. `npm run align-audio`(임시 SRT로)가 고지 카드 쉼 7.97초를 찾고 자막 109개를 맞춤, `srt_tool check` ✅. 문장 92개 시작 시각이 도구 기록과 최대 0.11초 차이
- 캐시: 두 번째 실행은 생성 0개 / `--redo 12,15`는 그 2문장만 새 시드(시도 2) / `--shard 0/2·1/2` 46개씩 → `--assemble-only` 92개 / `--story-style B`는 사연 문장만 다시
- 검사·재시도: 1회차 너무 김+무음 2.9초 → 2회차 NaN → 3회차 통과 / 3번 모두 너무 빠름 → 3회차를 쓰고 `report.md` "귀로 확인할 문장"에 표시 / 생성 오류 1번 → 2회차 통과

## 2026-10-10 — 전체 진행 순서(pipeline)와 자동화 도구 · 분석기 v2.3.1

### 왜 바꿨나 (사용자 지시)
1. 분석 결과가 없으면 분석기를 돌리고 → 결과로 지시사항·주제 탐색 → 제목 3개·썸네일 프롬프트 3개·업로드 정보·대본 → 영상별 요약 문서 → 오디오가 생기면 렌더·유튜브 비공개 업로드(최대 3개, 제목·썸네일 등록)
2. 썸네일은 프롬프트 파일만 만든다 (이미지는 다른 이미지 AI가 만든다)
3. 앞으로 main에 바로 올린다 (`CLAUDE.md`)

| 영역 | 함수/파일 | 변경 내용 |
|---|---|---|
| 분석기 | `youtube_topic_analyzer.py` v2.3.1 `load_keys` | `.env`가 없어도 환경변수 `YOUTUBE_API_KEY`가 있으면 실행 (클라우드). 없으면 예전처럼 템플릿 생성·종료 |
| 도구 | `tools/run_analysis.sh` v1.0 (신규) | 클라우드 분석: `--no-push --no-video --no-open` → `output/<주제>/result` → `<주제>/result` 복사 (영상·음성 제외) |
| 도구 | `tools/youtube_auth.py` v1.0 (신규) | 사용자 PC에서 한 번: OAuth(PKCE·루프백)로 업로드용 리프레시 토큰 발급 |
| 도구 | `tools/youtube_upload.py` v1.1 (신규) | upload.md 기준 비공개 업로드(이어 올리기), 챕터를 지금 SRT로 재계산, 한국어 자막, 채택 제목의 짝 썸네일 1개(1280×720·2MB 이하 JPG로 자동 변환), `youtube.json` 기록, `--dry-run`·`--check-auth` |
| 도구 | `tools/make_summary.py` v1.0 (신규) | 영상별 `summary.md`(상태·제목 3개·썸네일 프롬프트·설명란·태그·고정 댓글·스토리보드·대본), `--thumb-todo`로 이미지 없는 썸네일 프롬프트 모음 |
| 도구 | `tools/publish.sh` v1.0 (신규) | 4단계: 오디오(`narration.*`)가 있고 아직 안 올린 영상 → align-audio → 타입 검사 → 스토리보드 → 렌더(길이·오디오 확인) → 업로드 → 요약 문서, 최대 3개 |
| 지시사항 | `guides/pipeline.md` v1.0 (신규), `guides/README.md` v1.1, `upload_guide.md` v1.2(9번 API 업로드), `thumbnail_guide.md` v1.2(프롬프트만), `video_guide.md` v3.4(8·9번), `script_guide.md` v2.2(5-4), 저장소 `README.md`, `CLAUDE.md` | 전체 순서·키 설정·Claude에게 하는 말 예시, 비공개 잠금·테스트 및 비교 제약 |

### 검증
- `load_keys`: .env 없음 + 환경변수 키 → 계속 진행(.env 안 만듦) / .env 없음 + 키 없음 → 템플릿 생성·종료
- `run_analysis.sh`: 가짜 분석 결과로 복사 확인 (mp4 제외)
- `youtube_upload.py`: 실제 시트 3개 `--dry-run` 통과(챕터 12개 재계산, 태그 93~113자). 로컬 가짜 API로 전 과정: 20MB 이어 올리기, 자막 110개, 1536×1024 PNG → 1280×720 JPG 변환·등록, `youtube.json`, 재실행 시 건너뜀
- `publish.sh --dry-run`: 오디오 없음 → 대상 0 / 가짜 오디오 → 물타기 대상, 빚투는 "영상 코드 없음"으로 제외. 렌더 명령은 30프레임으로 확인
- 실제 유튜브 업로드는 키가 아직 없어 하지 못함

## 2026-10-09 — 새 주제 설정 파일 5개 (분석기 코드는 v2.3.0 그대로)

| 폴더 | 주제 | 내용 |
|---|---|---|
| `selfdev/analyzer_config.toml` | 자기계발 | 검색어 48개(무기력·번아웃 / 미루기·습관 / 도파민 중독 / 루틴·갓생 / 나이대·직장인 / 자존감·성공 습관) |
| `health/analyzer_config.toml` | 건강 | 검색어 48개(혈당·당뇨 / 간·혈압·콜레스테롤 / 검진·나이대 / 영양제·약 / 노화·통증 / 습관·몸의 신호) |
| `space/analyzer_config.toml` | 우주 | 검색어 48개(사고·실화 / 미스터리 / 크기·끝·탄생 / 탐사 / 뉴스·위험 / 다큐 포맷), 동음이의어 제외(우주소녀·로켓배송·화성시 등) |
| `story/analyzer_config.toml` | 사연을 통한 교훈 | 검색어 48개(가족 갈등 / 돈·배신·결혼 후회 / 인생 후회 / 인간관계 / 사연 포맷 / 사이다·감동) |
| `lifetips/analyzer_config.toml` | 생활꿀팁 | 검색어 48개(난방·전기 절약 / 곰팡이·냄새 / 청소 / 정리·살림 / 자취·이사 / 겨울 안전·상식), '청소년'·'대표이사' 제외 |

- 근거: 2026-10-09 YouTube 자동완성(쿼터 0) — 씨앗 검색어 250개를 조회해 실제로 이어지는 표현만 골랐다. 단독 주제어("우주", "사연", "자기계발")는 채널·노래·게임 이름이 섞여 넣지 않았다.
- 모두 `KEYWORD_MODE = "curated"`. "both"로 바꿀 때 쓰도록 자동완성 제외어(`EXCLUDE_KEYWORDS`)도 넣어 둠.
- 검증: 분석기 `apply_config_file`로 5개 모두 로드(모르는 설정 0개), 검색어 240개 중복 0개, `topic_relevance`로 검색어 240개 모두 관련 판정, 미끼 제목 22개(예: "우주소녀 다영 직캠", "청소년 상담 사례", "양파 채썰기") 모두 무관 판정.

## 2026-10-09 — 영상 제작 도구 (분석기는 v2.3.0 그대로)

### 왜 바꿨나 (사용자 지시: "일단 그냥 영상 만들어봐", "업로드 템플릿을 지시사항에 추가해서 만들어")

| 영역 | 함수/파일 | 변경 내용 |
|---|---|---|
| 도구 | `tools/srt_tool.py` v1.1 `export_remotion`, `parse_cards` | 대본의 `[장면]` 고지 카드 위치·길이(글자 수 ÷ 7 + 1초, 4~8초)와 자막을 영상용 `subtitles.ts`로 내보내기 |
| 도구 | `tools/srt_tool.py` v1.2 `video_times`, `export_upload` (신규) | 업로드용 SRT(고지 카드만큼 뒤 자막을 밂) + `--chapters "자막번호=제목"` → 영상 시간 챕터, YouTube 챕터 규칙(0:00 시작·3개 이상·10초 이상·순서) 검사 |
| 영상 | `video/` (신규, Remotion 4.0.534) | 공통 디자인·컴포넌트, 스토리보드 스크립트, 첫 영상 `multagi-2026-10` (31장면 + 고지 카드, 8분 29초) — `video/CHANGELOG.md` |
| 지시사항 | `guides/upload_guide.md`, `stock/guides/upload_rules.md` (신규), `guides/video_guide.md` v3.2 | 업로드 시트 규칙, 첫 영상 제작에서 정한 방식(로컬 폰트·plan.ts·storyboard.mjs) 반영 |

### 검증
- `srt_tool.py check` 통과(자막 91개), `upload` → 업로드용 SRT 자막 24부터 +8.0초, 챕터 12개 "✅ YouTube 챕터 규칙 통과"
- `video/`: `tsc --noEmit` 통과, 스토리보드 still 44장 검수(9개 장면 수정 후 다시 렌더)
- 전체 렌더: `final_1080p.mp4` 1920×1080 · 30fps · 15,285프레임 · 8분 29.5초 · 71.9MB · H.264, 오디오 없음(내레이션 전). 렌더 857초(4코어, concurrency 4). mp4에서 뽑은 프레임 8장이 스토리보드와 일치

## v2.3.0 — 2026-10-09 — 주제별 설정 파일 분리 · wget 실행기 · 저장소 구조 정리

### 왜 바꿨나 (사용자 지시)
1. 주식 말고 다른 주제로도 영상을 만들 수 있게, **공통으로 쓰는 코드·지시사항은 최상위**로, 주제별 내용은 주제 폴더로 나눈다.
2. 분석 코드의 키워드처럼 **바뀔 수 있는 값은 따로 설정 파일**에서 고칠 수 있게 한다.
3. 분석 코드를 **wget으로 받아서 실행**하는 스크립트를 만든다.

| 영역 | 함수/파일 | 변경 내용 |
|---|---|---|
| 설정 | `stock/analyzer_config.toml` (신규) | 주식 검색어 9개 카테고리·90개, 관련어(강한/약한/제외), 광고 의심 기준, GitHub 저장소를 코드에서 옮김. `[advanced]`에 바꿀 수 있는 주요 설정과 기본값(주석) |
| 설정 | `[설정 2]` 기본값 | 코드에는 주제와 무관한 기본값만 남김: `KEYWORD_MODE="autocomplete"`, `KEYWORD_GROUPS={}`, 관련어 `[]`(= TOPIC 한 단어). ⚠️ **설정 파일 없이 실행하면 주식도 자동완성 모드로 동작** (설정 파일이 없으면 틀을 만들고 경고) |
| 설정 | `apply_config_file`, `flatten_config`, `config_template`, `resolve_config_path` (신규) | TOML 읽기(3.11+ `tomllib`, 3.10은 `tomli` 자동 설치). `[섹션]`을 펼쳐 같은 이름의 설정을 덮어씀. 형식 오류(줄·칸 번호)·형식 불일치는 실행 전에 멈춤, 모르는 이름은 비슷한 이름 제안(오타), 정수↔실수 자동 변환, 설정 파일로 못 바꾸는 키(`AUTO_INSTALL_PACKAGES`, `UPDATE_YTDLP_DAILY`) 안내 |
| 실행부 | `load_config`, `init_config_only`, `--config`, `--init-config` | 우선순위 코드 기본값 < 설정 파일 < 명령줄. 기본 경로 `<스크립트 폴더>/<--folder 또는 PROJECT_FOLDER>/analyzer_config.toml`. `--init-config`는 새 주제 설정 파일 틀만 만들고 종료(덮어쓰지 않음). `--push-only`도 설정 파일의 폴더를 따름 |
| 리포트 | `write_report`, `write_run_info` | 사용한 설정 파일(스크립트 폴더 기준 상대경로 — PC 사용자 이름 노출 방지)·생성 여부 표시 |
| Stage 1 | `stage1_keyword_discovery` | 🐛 자동완성 모드에서 수요 점수 열이 object 형식이 되어 pandas 3에서 `nlargest` 오류 → 숫자 형식으로 고정 (설정 파일 없는 새 주제가 이 경로를 타므로 수정) |
| 자가진단 | `run_self_test`, `SELFTEST_TOPIC_CFG` | 🐛 가짜 데이터가 '주식' 제목이라 다른 주제 설정이면 자가진단이 실패하던 문제 → 주제 관련 값을 고정. 설정 파일 읽기·검증 테스트 추가 → **23개** |
| 실행기 | `run_analyzer.ps1`, `run_analyzer.sh` (신규) | 분석 코드는 매번 최신으로, 설정 파일은 없을 때만 GitHub raw에서 받음(wget / Invoke-WebRequest, 없으면 curl). `.venv` 자동 생성, `-Folder/-Topic/-Branch/-UpdateConfig` 옵션, 키가 없으면 안내 |
| 도구 | `tools/srt_tool.py` (신규) | 대본 TXT → SRT 생성(`build --reuse`: 바뀐 문장만 새로 계산)·검사(`check`). 지시사항 5-2 규칙(1자막=1문장, 22자 줄바꿈, 50자 제한, 빈 시간 없음, 초당 5.2음절) |
| 저장소 | `guides/`, `stock/guides/`, `stock/source/`, `stock/titles/` | 영상 제작 지시사항을 공통(`guides/`)과 주식 전용(`stock/guides/`)으로 나눔 — 각 파일의 변경 이력 참고 |

### 검증
- 자가진단 23/23. 기본값·주식 설정·다른 주제 설정(부동산) 모두 통과
- CLI: `--init-config` 생성·덮어쓰기 방지, 형식 오류(따옴표 없음 → 줄·칸 번호), 형식 불일치(숫자 자리에 글자), `--config` 경로 없음 → 모두 분석 전에 멈춤(종료 코드 1)
- 모의 전체 실행 4회 통과:
  - 주식 설정 파일 (Python 3.11): 90개 키워드 curated 모드, 푸시까지
  - 설정 파일 없음 (Python 3.11 / 3.13·pandas 3): 틀 생성 → 자동완성 150개 → 리포트·푸시
- 실행기: `run_analyzer.sh`(bash)와 `run_analyzer.ps1`(PowerShell 7.4)을 로컬 서버에서 받아 실행 → 코드·설정 다운로드, `.env` 생성 안내, `-UpdateConfig` 백업, 새 주제 설정 틀 생성, 실제 YouTube API 호출(가짜 키 → `API_KEY_INVALID`로 정상 종료)
- ⚠️ Windows PowerShell 5.1(윈도우 기본)에서는 실행해 보지 못함. UTF-8 BOM 저장, `-UseBasicParsing`, TLS 1.2 설정으로 대비

## v2.2.0 — 2026-10-09 — 실제 실행 결과(20261009_204204) 검토 후 수정: 검색 일일 한도 · 광고 의심 영상 · 제목 예시 · 재인코딩

### 왜 바꿨나 (v2.1.0 실제 실행 로그·데이터에서 확인된 문제)
1. **검색 74회 중 34회 실패** — `429 RATE_LIMIT_EXCEEDED: ... limit 'Search Queries per day'` (유닛 쿼터와 별개인 *일일 검색 횟수 한도*). 코드는 이를 일반 오류로 보고 남은 키워드를 계속 요청(34번 모두 실패), 실패한 키워드는 이월 목록에도 없었고 리포트는 "이월 16개"만 표시
2. **광고 집행(유료 홍보) 영상이 성공사례 1위** — 구독자 681명 채널의 쇼츠가 조회수 274만·좋아요 0.16%·댓글 3개(아웃라이어 8,690배). 성공 영상 95개 중 8개가 이런 형태(좋아요 <0.25% & 댓글 <0.05/1,000회, 전체 중앙값은 좋아요 0.97%·댓글 1.19/1,000회)
3. **제목 예시가 소재와 안 맞음** — '주식 폭락 전재산 손실' 같은 실패 사연 키워드에 「수수료 0.1% 차이가 만드는 결과」「현실적으로 수익 내는 방법」 같은 일반 투자 템플릿이 붙음
4. **불필요한 재인코딩 약 11분** — 공개 저장소라 영상은 어차피 GitHub에 안 올라가는데 49MB 맞추려고 240p로 재인코딩(성공사례 단계 775초 중 약 696초). 최저 비트레이트에서 같은 재인코딩을 두 번 반복(4분)
5. 자가진단의 **모의 다운로드 경고**("봇 확인 차단 → 다운로드 중단")가 실제 로그에 섞여 혼동

| 영역 | 함수/설정 | 변경 내용 |
|---|---|---|
| API | `is_daily_limit` (신규), `YouTubeClient._request`, `QuotaExceededError.kind` | 429/403 + 'per day' 메시지 → 일일 한도로 판정, 재시도 없이 즉시 중단. 거부된 요청은 예산 추적에서 차감 안 함(실제로 실행 안 됨). 분당 제한(`RATE_LIMIT_EXCEEDED`, per minute)은 재시도 대상에 추가 |
| Stage 2 | `collect_search` | 한도 도달 후 새 검색 중단(1회만 실패), **캐시에 있는 검색은 계속 사용**, 못 한 키워드는 사유와 함께 이월(`deferred_reason`: 예산 초과/일일 검색 횟수/일일 쿼터) |
| Stage 3 | `flag_ad_suspects` (신규), `AD_SUSPECT_FILTER`/`AD_SUSPECT_MIN_VIEWS=50,000`/`AD_SUSPECT_MAX_LIKE_RATE=0.25%`/`AD_SUSPECT_MAX_COMMENT_RATE=0.05/1,000` | 고조회수인데 좋아요율·댓글률이 **둘 다** 극히 낮은 영상 → 성과 분석(`perf`)·성공 판정·성공사례·키워드별 참고 영상에서 제외 (좋아요/댓글 숨김이면 판단 보류). ⚠️ 성공 판정 기준 변경 → 성공 비율·키워드 점수가 v2.1.0과 달라짐 |
| Stage 4 | `analyze_keywords`, `recent_hot` | 키워드별 성과·참고 영상·최근 급상승에서 광고 의심 영상 제외 (검색 경쟁도 계산에는 그대로 포함 — 실제 검색 화면 경쟁자이므로) |
| Stage 6 | `process_success_case`, `ensure_max_size`, `videos_go_to_github` (신규) | 영상이 GitHub에 안 올라가는 게 확실하면(공개 저장소·푸시 안 함) **재인코딩 생략 → 원본 화질 유지**. 비공개 저장소면 기존대로 49MB 이하로. 최저 비트레이트(60kbps)에서 같은 재인코딩 반복 방지 |
| Stage 7 | `keyword_intent`, `make_titles`, `TITLE_TEMPLATES_BY_INTENT` (신규) | 키워드 성격(실패·손실 사연 / 사기·피해 / 일반)별 제목 템플릿. 데이터에서 효과가 확인된 제목 요소 순서는 그대로 |
| Stage 7 | 리포트 | 이월 사유별 개수, 광고 의심 제외 목록, 기준선 부족 시 "채널 평균 비교 불가" 표시(기존 "-배"), `videos.csv` 에 `on_topic`·`topic_reason`·`ad_suspect`·`category`·`found_by` 열 추가 |
| 자가진단 | `_quiet_logs` 외 4개 검사 | 모의 다운로드 로그 숨김 + 일일 한도 판정 / 한도 도달 시 이월·캐시 계속 / 광고 의심 판정 / 성격별 제목 → **22개** |

### 검증
- 자가진단 22/22
- 모의 전체 실행(실제 v2.1.0 429 응답 형식 재현, 30회 후 한도): 429는 **1번만** 발생 → 새 검색 중단, 이월 60개(예산 16 + 한도 44), 쿼터 추적 3,223(거부된 요청 미차감), 광고 영상 3개 제외(성공 3개 제거), 공개 저장소 → 재인코딩 생략, 제목 예시 성격별 생성
- 비공개 저장소 모의 실행: 재인코딩(57→25MB)·푸시 정상
- 최저 비트레이트 가드: 0.05MB 목표로 강제 → 1회 후 "재인코딩 중단" 경고
- Python 3.11/pandas 2.2 · 3.13/pandas 3.0 실행 통과

## v2.1.0 — 2026-10-09 — 카테고리별 검색어 · 주제 관련성 필터 · GitHub 쓰기권한 확인/--push-only

### 왜 바꿨나
1. 검색어를 사연·노후·가족 갈등·사기 피해 등 **카테고리별로 다양하게** 지정하고 싶음
2. `git push` 가 `Permission to ... denied to yeomin1024` 로 실패 — 토큰은 인증되지만 **쓰기 권한이 없음**. 기존 사전 확인은 저장소 API의 '계정' 권한(관리자)을 봐서 토큰 권한 부족을 못 잡았음
3. 성공사례에 `홈쇼핑_방송_사고` 같은 **주제와 무관한 영상**이 들어감 — YouTube 검색은 무관한 인기 영상도 섞어 보여주는데 조회수·배수만으로 골랐기 때문

| 영역 | 함수/설정 | 변경 내용 |
|---|---|---|
| 설정 | `KEYWORD_MODE`, `KEYWORD_GROUPS`(9개 카테고리·90개), `AUTOCOMPLETE_TOP_N` | 카테고리별 직접 지정 검색어 (기본 = 요청하신 8개 카테고리 80개 + '사연·썰·다큐 포맷' 10개). 기존 자동완성 방식은 `"autocomplete"`/`"both"` 로 선택 |
| 설정 | `SEARCH_ORDERS` | **`["relevance","viewCount"]` → `["relevance"]`** (키워드 수 증가에 따른 쿼터 절약, 키워드당 100유닛) |
| 설정 | `SEARCH_CACHE_TTL_HOURS=168`, `BASELINE_CACHE_TTL_HOURS=72` | 검색 7일·채널 업로드 목록 3일 캐시 → 하루 예산 초과 키워드를 다음 실행에서 이어서 수집 |
| Stage 1 | `keyword_demand`, `score_keyword_demand`, `round_robin_priority` | 키워드별 검색 수요 = 자동완성이 표현을 어디까지 알아보는지(깊이×폭, 쿼터 0). 카테고리를 번갈아 배치해 예산이 모자라도 모든 카테고리가 골고루 수집 |
| Stage 2 | `plan_quota` | 캐시된 검색은 0유닛으로 항상 포함, 나머지는 우선순위대로 예산까지 → 초과분 이월(로그·리포트 표시) |
| Stage 3 | `topic_relevance` (신규), `RELEVANCE_TERMS`/`RELEVANCE_WEAK_TERMS`/`RELEVANCE_EXCLUDE` | 제목·태그의 강한 관련어(또는 설명란 2회 이상, 약한 관련어+맥락)로 주제 관련 판정, '주식회사' 등 오탐 표현 제거. 무관 영상은 성과 분석·성공 판정·성공사례에서 제외하고 `data/excluded_offtopic.csv` 로 기록 |
| Stage 4 | `analyze_keywords`, `analyze_categories` (신규) | 수요·경쟁을 **주제 관련 영상만**으로 계산, `relevant_share`·`content_gap`(검색 상위 중 무관 영상 비율) 추가, 카테고리별 요약 |
| Stage 4 | `KEYWORD_SCORE_WEIGHTS` | ⚠️ **가중치 변경**: median_outlier 0.15→0.10, fresh_share 0.10→0.05, content_gap 0.10 신규 (합계 1.0) — 무관 영상이 많은 검색어 = 볼 영상이 부족한 공백 |
| Stage 6 | `select_success_cases`, `MAX_CASES_PER_CATEGORY=2` | 주제 관련 영상만, 카테고리당 최대 2개(부족하면 완화) → 여러 소재를 골고루 |
| Stage 8 | `check_push_access` (신규), `reload_github_token`, `push_only`, `--push-only` | 토큰의 실제 쓰기 권한을 git 푸시 엔드포인트로 **분석 전에** 확인, 토큰 종류(fine-grained/classic)별 해결 방법 안내, 푸시 직전 `.env` 재확인, 분석 없이 결과만 올리는 `--push-only` |
| 리포트 | 카테고리별 기회 표·차트(`12_category_opportunity.png`), 이월 키워드, 무관 영상 목록, 성공사례의 카테고리·검색어 | |

### 검증
- 자가진단 18/18 (관련성 필터: 홈쇼핑·'주식회사'·곤충 '개미' 제외 / 수요 점수: 실제 자동완성 응답 기반 / 카테고리 순환 / 캐시 인식 쿼터 / 토큰 403·scope 부족 판정)
- 모의 데이터 전체 실행: 90개 키워드 중 74개 수집·16개 이월 → **같은 폴더 2회차 실행에서 74개 캐시 재사용(0유닛) + 16개 추가 = 90개 완료**, 무관 영상('홈쇼핑 방송 사고') 제외·성공사례 6개가 6개 카테고리에 분산
- 쓰기 권한 없는 토큰 시나리오: 시작 시 경고 → 분석 완료 → 푸시만 안내와 함께 건너뜀 / `--push-only` 로 기존 결과 푸시 성공
- 실제 YouTube 자동완성으로 90개 키워드 수요 점수 계산 확인 (259개 질의)
- Python 3.10~3.13 컴파일, Python 3.11/pandas 2.2 · 3.13/pandas 3.0 실행 통과
- ⚠️ 실제 GitHub 403 응답은 이 환경에서 재현 불가 (GitHub 표준 동작 기준 구현 + 푸시 오류 메시지 해석으로 이중 대비)

## v2.0.0 — 2026-10-09 — 내 PC에서 실행하는 단일 스크립트로 전환

Kaggle 노트북(`youtube_topic_analyzer.ipynb`, v1.2.0) → **`youtube_topic_analyzer.py`** 하나로 교체 (노트북은 git 기록 `977bc4f` 에 보존).
분석 로직·점수 가중치·성공 기준·위험 관련 기본값은 **변경 없음**.

| 영역 | 함수/위치 | 변경 내용 · 이유 |
|---|---|---|
| 키 | `.env` (`load_env_file`, `load_keys`) | Kaggle Secrets → 스크립트 폴더의 `.env`. 처음 실행 시 템플릿 자동 생성, `.gitignore` 등록. 값은 앞뒤 4자만 표시 |
| 설정 | 스크립트 상단 [설정 2] + 명령줄 | `--topic --folder --result-folder --keywords --cases --no-video --no-push --no-open --log-level --skip-install` (변경값은 로그에 기록). 주제만 바꾸고 폴더가 `stock` 이면 덮어쓰기 경고 |
| 설치 | `bootstrap` | 필요한 패키지 자동 설치(pip), yt-dlp 하루 1회 업데이트, faster-whisper 설치 실패 시 24시간 재시도 안 함, Python 3.10 미만 차단, 콘솔 UTF-8 |
| 경로 | `init_run` | 결과 = `<스크립트 폴더>/output/<PROJECT_FOLDER>/<RESULT_FOLDER>`, 캐시·임시 = `.yt_work/` (재실행 시 캐시 재사용 → 쿼터 절약) |
| Windows | `rmtree_force`, `close_log_files`, `run_git`, `ensure_max_size`, subprocess 전반 | git 읽기전용 파일 삭제, 열린 로그 파일 잠금 해제, `core.longpaths`·`credential.helper=`(로그인 팝업 방지), `os.replace`, 하위 프로세스 출력 UTF-8 디코딩 |
| 차트 | `setup_chart_style` | 맑은 고딕(Windows)·AppleGothic(macOS)·나눔고딕(Linux) 순 탐색, 없으면 나눔고딕 자동 다운로드. 항상 PNG 저장(Agg) |
| 다운로드 | `run_ytdlp`, `prepare_cookies`, `ytdlp_base_opts` | 일시 오류(간헐 403·응답 추출 실패·5xx·타임아웃) 자동 재시도(3초·8초), 스크립트 폴더 `cookies*.txt` 자동 인식, `COOKIES_FROM_BROWSER` 지원. PC용 다운로드 스크립트 생성 기능 제거(이미 PC) |
| GitHub | `stage8_push_github` | Git 미설치 시 안내 후 건너뜀, 푸시 실패는 PC 결과에 영향 없이 경고만 |
| 마무리 | `stage8_finish` (신규, Kaggle 출력 대체) | 결과 요약, 선택 zip, 결과 폴더 열기(탐색기/Finder) |

### 검증
- 문법: Python 3.10 / 3.11 / 3.12 / 3.13 컴파일 통과 (SyntaxWarning 없음), pyflakes 미정의 이름 없음
- 자가진단 13/13 (일시 오류 재시도 테스트 추가)
- **새 가상환경 첫 실행 재현**: `.env` 자동 생성 → 패키지 자동 설치 → 키 없으면 안내 후 종료 → (가짜 키) 자가진단·실제 자동완성 수집까지 진행 후 실제 YouTube API가 키 오류를 반환하자 안내 메시지와 함께 종료
- 모의 YouTube 데이터 + 로컬 git 원격으로 전체 실행 통과 (Python 3.11/pandas 2.2, 3.13/pandas 3.0), 봇 확인 시나리오·`cookies.txt` 자동 인식 확인
- 실제 YouTube: 시스템 ffmpeg 없이(번들 ffmpeg) 영상+음성 병합 다운로드, 길이 측정, 재인코딩, 자막 수집 성공
- ⚠️ 실제 Windows/macOS 기기와 실제 API 키로는 실행하지 않음 (Windows 대응은 코드 검토 기준)

## v1.2.0 — 2026-10-09 — YouTube 봇 확인('Sign in to confirm you're not a bot') 대응

원인: Kaggle(구글 클라우드 데이터센터 IP)에서 yt-dlp 요청 시 YouTube가 로그인(봇 확인)을 요구. 분석 로직·점수는 **변경 없음**.

| 영역 | 셀/함수 | 변경 내용 · 이유 |
|---|---|---|
| 키 | 블록 1 | 선택 Secret `YTDLP_PROXY`(주거용 프록시) 추가 |
| 설정 | 블록 2 | `YTDLP_CLIENT_FALLBACK`, `YTDLP_MAX_BOT_BLOCKS=2`, `WRITE_LOCAL_DOWNLOAD_SCRIPT` 추가. `YTDLP_COOKIES_FILE` 비우면 데이터셋 자동 탐색 |
| 공통 | `find_cookie_files`, `inspect_cookies`, `prepare_cookies` | `/kaggle/input/**/*cookie*.txt` 자동 인식, 쿠키 점검(로그인 쿠키 유무·만료 — **이름만 기록, 값은 기록 안 함**). 쿠키 처리를 `init_run` 에서 분리 |
| Stage 6 | `refresh_download_auth` (신규) | Stage 6 셀 실행 때마다 쿠키/프록시 Secret을 다시 읽고 봇 확인 상태 초기화 → **쿠키 추가 후 Stage 6만 재실행** 가능 |
| Stage 6 | `run_ytdlp` (신규), `ytdlp_download`, `transcript_via_ytdlp` | 봇 확인 시 다른 YouTube 클라이언트(tv_simply → tv → web_embedded → mweb)로 재시도, 성공 클라이언트 재사용. **연속 2개 영상**이 모두 막히면 이번 실행의 yt-dlp 시도 중단(시간 낭비·IP 평판 악화 방지). 같은 영상의 영상/자막/음성 시도는 1회로 집계 |
| Stage 6 | `transcript_via_api`, `ytdlp_base_opts` | 프록시 지원(yt-dlp, youtube-transcript-api) |
| Stage 6 | `write_local_download_script` (신규) | 막힌 사례만 담은 `success_cases/download_on_pc.py` 생성 — 가정용 IP(내 PC)에서 영상·대본을 같은 폴더 구조로 받기 |
| Stage 6/7 | 상태·리포트 | 영상 상태 `blocked(bot_check)`, 리포트·요약에 해결 방법 안내 |

### 검증
- 자가진단 12/12 (쿠키 점검, 클라이언트 재시도 → tv 기억, 연속 차단 시 중단 테스트 추가)
- 봇 확인을 항상 반환하는 가짜 yt-dlp로 Stage 0~8 전체 실행: 2번째 영상에서 중단, 이후 사례는 즉시 건너뜀, `download_on_pc.py` 생성·리포트 안내 확인
- 실제 YouTube: 쿠키 파일을 붙인 상태에서 래퍼 경유 영상·자막 다운로드 성공, 생성된 `download_on_pc.py` 를 실제로 실행해 영상+대본 저장 성공
- Python 3.11/pandas 2.2 및 Python 3.13/pandas 3.0 모두 통과
- ⚠️ 실제 Kaggle IP에서의 봇 확인 해소 여부는 이 환경에서 재현할 수 없어 미검증 (쿠키 품질·계정 상태에 따라 다름)

## v1.1.0 — 2026-10-09 — Kaggle 노트북 실행 + Kaggle Secrets로 키 읽기

실행 환경을 Colab → **Kaggle Notebooks** 로 전환. 분석 로직(Stage 1~4)·점수 가중치·성공 기준은 **변경 없음**.

| 영역 | 셀/함수 | 변경 내용 · 이유 |
|---|---|---|
| 키 입력 | 블록 1 (`read_secret`) | 셀 입력칸·Colab Secrets·getpass 제거 → `kaggle_secrets.UserSecretsClient().get_secret()` 로만 읽음 (로컬 테스트용 환경변수 폴백). Secret 이름은 `SECRET_LABELS` 로 변경 가능. 선택 Secret `YTDLP_COOKIES` 추가 |
| 설정 | 블록 2 | Colab `#@param` 폼, `VIDEO_FALLBACK_TO_DRIVE`·`SAVE_TO_GOOGLE_DRIVE`·`DRIVE_FOLDER` 제거 → `MAKE_RESULT_ZIP` 추가 |
| 설치 | 블록 3 | Internet Off 감지 시 안내와 함께 중단, 한글 폰트 apt 실패 시 Google Fonts에서 다운로드, `imageio-ffmpeg` 추가(시스템 ffmpeg 없을 때) |
| 공통 | `init_run`, `find_ffmpeg`, `prepare_cookies` | 결과 = `/kaggle/working/<PROJECT_FOLDER>/<RESULT_FOLDER>` (Kaggle Output), 캐시·임시파일 = `/tmp` (Output 미포함). 키가 없으면 초기화에서 즉시 중단. 쿠키 Secret(base64/원문) → 권한 600 파일, `/kaggle/input` 쿠키는 복사 후 사용(읽기전용 대비) |
| Stage 5 | `setup_chart_style`, `_save` | 인라인 표시 조건을 노트북 여부로 변경, 다운로드 폰트 경로 추가 |
| Stage 6 | `ytdlp_base_opts`, `media_duration`, `ensure_max_size`, `transcript_via_whisper` | yt-dlp에 `ffmpeg_location` 지정, ffprobe 없으면 `ffmpeg -i` 로 길이 파싱, Whisper GPU는 `compute_type="auto"`(P100 등 대비) + GPU 오류 시 CPU 재시도, 안내 문구 Kaggle 기준 |
| Stage 8 | `stage8_kaggle_output` (신규), `stage8_save_drive` (삭제) | Google Drive 저장 → Kaggle 출력 정리 + `<PROJECT_FOLDER>_<RESULT_FOLDER>.zip`. 공개 저장소에서 GitHub에 못 올린 영상은 Kaggle 출력에 보관됨을 로그·리포트에 표시 |

### 위험 관련 기본값 — 변경 없음
`QUOTA_BUDGET=9000`, `SUCCESS_CASE_COUNT=8`, `VIDEO_MAX_MB=49`, `ALLOW_VIDEO_UPLOAD_TO_PUBLIC_REPO=False`

### 검증
- Kaggle 모사 환경(Python 3.11.17 · pandas 2.2.3 · 가짜 `kaggle_secrets` · `/kaggle/working`)에서 전체 Stage 실행 통과 (공개/비공개 저장소 모두)
- 키를 Secrets에서만 읽음 확인, Secret 미등록 시 안내 후 중단 확인, 출력·git 기록에 키/토큰 문자열 없음 확인
- 시스템 ffmpeg 없이(imageio-ffmpeg) 길이 측정·재인코딩·yt-dlp 병합 경로 동작 확인
- node 없이 deno만으로 실제 yt-dlp 자막·영상 다운로드 성공
- 자가진단 10/10 통과

## v1.0.0 — 2026-10-09 — 최초 작성

구독자 0명 채널이 '주제(기본: 주식)'에서 조회수를 가장 잘 받을 영상을 찾는 Colab 노트북.

| 영역 | 셀/함수 | 내용 |
|---|---|---|
| 키 입력 | 블록 1 (`_resolve_secret`) | YouTube API 키·GitHub 토큰을 별도 블록에서 입력. 셀 입력 → Colab Secrets → 환경변수 → getpass 순서 |
| 설정 | 블록 2 | `TOPIC`(주제 변경 가능), `PROJECT_FOLDER`(결과 상위 폴더, 없으면 생성), `RESULT_FOLDER`, 수집/성공 기준/다운로드 옵션 |
| 설치 | 블록 3 | yt-dlp[default] + deno(JS 런타임), youtube-transcript-api, kiwipiepy, faster-whisper, 한글 폰트 |
| 공통 | `setup_logging`, `log`, `stage_timer`, `JsonCache`, `init_run` | `[STAGE] [시각] [레벨] key=value` 구조화 로그, 토큰 마스킹, 단계별 소요시간, API 응답 캐시, 시드 고정, 위험 설정 변경 경고 |
| API | `YouTubeClient` | 쿼터 예산 추적(요청 전 예약), 재시도/백오프, 치명 오류(키 오류·API 미사용) 안내, 50개 묶음 병렬 요청 |
| Stage 1 | `stage1_keyword_discovery` | YouTube 자동완성 확장(ㄱ~ㅎ, 가~하, a~z, 수식어, 2단계) → 검색 수요 점수, 유사 키워드 중복 제거 |
| Stage 2 | `stage2_collect`, `plan_quota` | 검색(관련도=실제 검색화면, 조회수순=기간 내 히트) → 영상/채널 상세 → 채널 최근 업로드 기준선. 쿼터 부족 시 키워드 수 자동 축소(전/후 로그) |
| Stage 3 | `validate_videos`, `compute_outlier_scores` | 중복·결측·범위·미래날짜 검증, 일평균 조회수, 구독자 대비 조회수, **채널 기준선 대비 아웃라이어 배수**(leave-one-out, 포맷별, 14일 미만 영상 제외로 누적 편향 방지), 쇼츠 판별 |
| Stage 4 | `analyze_keywords` 외 | 키워드 기회점수(가중치 명시), 채널명 검색 제외, 제목 요소 효과(Mann-Whitney + BH-FDR 보정), 형태소 단어 분석, 길이/포맷/요일·시간/채널 규모, 제목 클러스터(KMeans, 시드 고정), 태그, 댓글 질문 |
| Stage 5 | `stage5_charts` | 차트 11종 PNG (색각이상 검증 팔레트, 이중축 없음) |
| Stage 6 | `stage6_success_cases` | 성공사례 선정(소규모 채널·롱폼 쿼터, 채널당 1개) → 썸네일, 영상(용량 초과 시 ffmpeg 재인코딩), 대본(자막 API → yt-dlp 단일 트랙 → Whisper), 메타데이터, 댓글 |
| Stage 7 | `stage7_report` | `README.md` 리포트(추천 아이디어·업로드 플랜·체크리스트·방법론), `analysis.xlsx`, `data/*.csv`, `run_info.json`, `run_log.txt` |
| Stage 8 | `stage8_push_github`, `stage8_save_drive` | `<PROJECT_FOLDER>/<RESULT_FOLDER>`로 커밋·푸시(폴더 자동 생성, 토큰은 헤더로만 전달), 100MB 초과 파일 제외, **공개 저장소면 영상 파일은 GitHub 대신 Drive** |

### 위험 관련 기본값 (변경 시 로그·리포트에 경고)
- `QUOTA_BUDGET=9000` (일일 한도 10,000)
- `SUCCESS_CASE_COUNT=8`, `VIDEO_MAX_MB=49`, `VIDEO_MAX_HEIGHT=480`
- `ALLOW_VIDEO_UPLOAD_TO_PUBLIC_REPO=False` — 공개 저장소에 타인 영상을 올리지 않도록 기본 차단 (저작권)

### 검증
- 오프라인 자가진단 10/10 통과 (심어둔 3배 효과를 lift 3.02배로 탐지 등)
- 모의 YouTube 데이터 + 로컬 git 원격으로 Stage 0~8 전체 실행: 공개/비공개 저장소, 기존 결과 교체, 다른 폴더 보존, 쿼터 부족 시나리오
- 실제 네트워크: 쇼츠 판별, 자막 API, yt-dlp 자막·영상 다운로드, ffmpeg 재인코딩, faster-whisper 동작 확인
- pandas 2.2.3 / 3.0.6 모두 경고 없이 동작
