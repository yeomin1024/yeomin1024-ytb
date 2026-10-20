#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.14 — 2026-10-20 — 영상 하나(또는 몇 개)만 다른 목소리: 영상 폴더 voices/<역할>.json 에 "own_voice": true 가 있으면 공통 설정의
#          lock 을 넘어 그 영상만 그 목소리 (다른 영상·공통 voices/<역할>.json 은 그대로). 만드는 법 `pick H09 --only-for test/<영상ID>,test/<영상ID>-shorts`
#          — 기준 소리는 첫 영상 폴더 voices/ref/ 에, 나머지는 그 파일을 가리킴. 사용자 지시 2026-10-20 "오디오는 H09 음성으로 가고" (일본 축제 시험 영상).
# (v1.13) — 2026-10-20 — 목소리 후보마다 읽을 문장을 따로 줄 수 있음: samples.json 후보에 "text": {"ref", "preview"} 가 있으면 그 문장
#          (없으면 예전처럼 역할 공통 text.<역할>). 사용자 지시 2026-10-20 "오디오 목소리 안 약간 높고 약간 빠른 지루하지 않은 목소리로 대본 몇줄
#          읽어보는 여러 테스트 안을 만들어봐" — 새 후보(H07~)는 test/ 일본 축제 대본 문장을 읽고, 옛 후보(H01~H06)의 샘플·정체는 그대로.
# (v1.12) — 2026-10-19 — 영상 하나를 오디오에서 빼는 표시 파일 NO_TTS.md (대본 폴더 — 롱폼 <영상ID>/ · 쇼츠 <영상ID>/shorts/):
#          있으면 업로드한 영상과 똑같이 all(--force 여도)·build·build_episode·push 모두 만들지도 올리지도 않음, 첫 줄이 까닭(로그·계획에 나옴).
#          사용자 지시 2026-10-19 "테스트용은 오디오 만들지마" — 기초연금 AI 쇼츠 시험 편(gicho-yeongeum-ai-2026-10)에 둠. 다른 동작은 그대로.
# (v1.11 — 2026-10-19 — 업로드한 영상(대본 폴더에 youtube.json)은 어느 길로도 오디오를 만들지 않는다 — all 은 예전부터 건너뛰었고(repo_status
#          'uploaded', --force 보다 먼저), 이번에 build(영상 하나 — 모델을 불러오기 전에 멈춤)·build_episode(안전장치)·push(이미 만든 결과를 올리지
#          않음)에도 같은 막음. 사용자 지시 2026-10-19 "새로 만든 영상 2개에 대해 오디오 코드로 생성하는지 확인해 그리고 업로드 완료한건 오디오
#          생성하지 말도록 하고". 대상 고르기·만드는 방법은 그대로.)
# (v1.10 — 2026-10-17 — 부분 다시 만들기: 파트 라벨 **글자만** 바뀐 것은 막지 않는다 (라벨은 소리로 읽지 않음) — 파트 경계(어느 문장에서
#          챕터가 바뀌는지)와 문장마다 읽는 목소리(역할)가 같으면 바뀐 문장만 다시. 경계나 역할이 바뀌면 예전처럼 전부 다시.
#          사용자 피드백 2026-10-17 "아니 너무 또 길게 풀어서 쓰면 읽기 힘들잖아 최대한 짧지만 이해가 다 되도록 다시 고쳐봐" — 재테크 대본을
#          낱말 몇 개만 고쳤는데 챕터 이름 한 글자 때문에 오디오를 전부 다시 만들지 않게.)
# (v1.9 — 2026-10-16 — 쇼츠 대본도 읽는다: <주제>/source/<영상ID>/shorts/<영상ID>-shorts.txt → 같은 쇼츠 폴더에 narration.mp3 ·
#          tts_narration.json · tts_report.md (영상ID 는 '<영상ID>-shorts'). all·check·push·pick 이 롱폼과 같은 방식으로 다룬다 (src_dir).
#          사용자 지시 2026-10-16 "좋아 나머지도 세 편도 대본은 같은 방식으로 만들고 일단 이 쇼츠만 영상 만들어봐" — 쇼츠 영상도 오디오 먼저 (CLAUDE.md).)
# (v1.8 — 2026-10-15 — 사용자 지시 "맨 마지막 대사 … 시청해주셔서 감사합니다. 로 변경 … 음성 … 에 모두 반영": 부분 다시 만들기 —
#          대본의 글만 조금 바뀌면(문장 수·파트·카드·쉼·목소리가 같고 바뀐 문장 ≤ 20%) all·build 가 그 문장만 새로 만들어 저장소
#          narration.mp3 의 그 자리에 끼운다. 다른 문장의 소리·시각은 그대로(뒤 문장만 길이 차이만큼 밀림), 새 문장 크기는 다른 문장
#          말소리 크기 중간값에 맞춤, 메타 patches 에 기록, 보고에 '부분 다시 만들기' 절. --full 이면 예전처럼 전부 다시.)
# (v1.7 — 2026-10-15 — 사용자 지시 "오디오 코드도 진행자 목소리로만 대본 읽도록": 역할 설정 enabled(false 면 그 역할을 끔) —
#          voices/storyteller.json enabled=false → 모든 문장(사연 파트 포함)을 진행자(H04 기준 목소리)가 읽는다. 꺼진 역할은 고르기·샘플·모델에서 빠진다.
#          범위 버튼(전체 / 주제 하나)은 tools/kaggle_tts_panel.py 가 all --topics 로 넘긴다)
# (v1.6 — 2026-10-12 — 사용자 지시: 사연자 S07(말 속도 조금 더 빠르게)·진행자 H04 로 고정 → pace 에 speed(모든 문장을 이 배수로
#          빠르게 한 뒤 [min, max] 안으로, 음 높이 그대로 ±max_stretch 까지; 짧은 문장도 speed 만큼). speed 없으면 v1.5 와 같음.
#          고른 뒤 current 후보(S01·H01) 샘플은 '고르기 전 목소리' 기록으로 두고 다시 만들지 않음 (frozen_current).
#          두 역할 모두 clone 이면 화자 확인용 CustomVoice 모델을 불러오지 않음 (check_speakers))
# (v1.5.1 — 2026-10-12 — check: 올린 영상(youtube.json)은 대본이 달라도 '다시 만든다'고 하지 않음 — 스튜디오에서 사연을
#          잘라 낸 영상(studio_trim.md)은 대본이 잘라 낸 영상 기준이고 오디오는 원본 렌더 기록 (all 은 원래 올린 영상을 건드리지 않음))
# (v1.5 — 2026-10-12 — 사용자 지시: 사연자를 남자 목소리로(손실을 보고 억울해하며 자책하는 연기 톤), 말 속도를 자연스럽게 맞추고,
#          터미널에서 바로 들을 수 있게 → 후보 S07·S08(남성 억울·자책 묘사), 역할·후보 설정 pace(문장 말 속도가 범위를 벗어나면
#          ffmpeg atempo 로 음 높이는 그대로 두고 ±15% 안에서 늘이거나 줄임), listen 명령·samples --play (ffplay/afplay/mpv, Jupyter 는 오디오 위젯))
# (v1.4 — 2026-10-12 — 사용자 지시: 사연자·진행자 목소리 샘플을 각각 여러 개 만들고(samples), 사용자가 고르면(pick) 그 목소리로
#          모든 대본을 일관되게. 두 역할을 다 고르기 전에는 all 이 오디오 대신 샘플만 만들어 voices/samples/ 에 올린다.
#          후보 설정 voices/samples/samples.json (current = 지금 목소리 그대로 / custom_voice = 화자+말투 / design = 묘사 → 기준 소리 → 복제))
# (v1.3 — 2026-10-11 — 사용자 지시: 진행자 목소리는 중저음 남성(귀에 잘 들어오고 신뢰감 있게), 대본마다 달라지지 않게 →
#          진행자는 저장소에 고정한 기준 목소리(voices/ref/host.wav)를 Base 모델로 복제. 기준 목소리는 없을 때 한 번만 VoiceDesign 으로
#          만들어(목소리 높이 85~150Hz·속도·무음 검사) main 에 올린다. 문장마다 목소리 높이가 기준 ±30% 밖이면 다시 만든다.
#          host.json lock(주제·영상 덮어쓰기 무시), 목소리 정체(voice_ids)가 바뀐 오디오는 옛 것으로 보고 다시 만든다. voice 명령
#          (v1.2.1: Kaggle 사본 git 파일 모드 / v1.2: 오디오 하나·GitHub 대본 폴더에 올리기 / v1.1: 역할별 목소리 설정 / v1.0: 최초 작성))
r"""
대본 TXT로 내레이션 오디오를 만듭니다. Kaggle 노트북(GPU T4)에서 돌리는 것을 기준으로 썼습니다. 사용법: guides/tts_guide.md

  python tools/tts_narration.py all --push                             # 저장소의 대본을 모두 읽어 오디오가 없는 영상 전부 → 영상마다 GitHub에 올림
                                                                       #   (목소리를 아직 안 골랐으면 오디오 대신 목소리 샘플만 → voices/samples/)
  python tools/tts_narration.py samples --push                         # 목소리 후보 샘플 (voices/samples/samples.json) → voices/samples/<역할>/<ID>.mp3
  python tools/tts_narration.py pick S04 H01                           # 고른 목소리로 고정 (GPU 필요 없음 — Claude 가 실행하고 커밋)
  python tools/tts_narration.py samples --only S07,S08 --play          # 그 후보만 만들고 바로 듣기 (터미널: ffplay·afplay·mpv / Kaggle·Jupyter: 오디오 위젯)
  python tools/tts_narration.py listen S07 S08                         # 만들어 둔 샘플 바로 듣기 (파일 경로도 됨)
  python tools/tts_narration.py all --dry-run                          # 무엇을 만들지 목록만 (모델 안 불러옴)
  python tools/tts_narration.py build stock panicsell-2026-10 --push   # 영상 하나
  python tools/tts_narration.py build stock panicsell-2026-10 --redo 12,15 --push   # 12·15번 문장만 새 시드로 다시
  (v1.8) 대본 글이 조금 바뀌면 all·build 가 바뀐 문장만 새로 만들어 저장소 오디오에 끼운다 — 전부 다시는 --full
  python tools/tts_narration.py push                                   # 만들어 두고 못 올린 결과를 GitHub에 올리기
  python tools/tts_narration.py check stock panicsell-2026-10          # 저장소의 narration 이 지금 대본·목소리로 만든 것인지
  python tools/tts_narration.py voice                                  # 진행자 기준 목소리 정보 (없으면 만들기, --push 로 올림)
  python tools/tts_narration.py pack                                   # (올리기가 안 될 때만) 결과를 저장소 경로 그대로 zip 하나로
  (어느 명령이든 --fake: 모델 없이 가짜 소리로 전 과정 확인 — 가짜 소리는 github.com 에 올리지 않는다)

모델 (모두 Qwen3-TTS 1.7B, Apache-2.0 — 상업 이용 가능)
  - 사연자: CustomVoice — 한국어 화자 Sohee + 말투 지시(instruct). ※ 0.6B 는 말투 지시를 무시한다
  - 진행자: Base — 저장소의 기준 목소리 voices/ref/host.wav 를 복제 (모든 대본·세션에서 같은 목소리)
  - 기준 목소리가 없을 때 한 번만: VoiceDesign — voices/host.json 의 design(중저음 남성 묘사)으로 만들어 main 에 올림
  - GPU 둘(T4 x2)이면 사연자 모델은 GPU 0, 진행자 모델은 GPU 1. 하나면 한 번에 한 모델만 올린다

목소리 고르기 (사용자 지시 2026-10-12) — 역할마다 후보 샘플을 듣고 하나를 고르면, 그 목소리가 모든 대본에 고정된다
  - samples: 후보마다 같은 문장(voices/samples/samples.json 의 text)을 읽힌 샘플 mp3 + 정보(json), design 후보는 기준 소리(_ref.wav)도
  - pick <ID>...: current → 설정 그대로(이미 만든 오디오도 그대로) / custom_voice → 화자·말투 고정 / design → 기준 소리를 voices/ref/<역할>.wav 로
    복사하고 복제(clone)로 고정. 둘 다 lock(주제·영상 덮어쓰기 무시). 목소리가 바뀐 역할의 오디오는 다음 all 이 다시 만든다
  - 두 역할 모두 voices/<역할>.json 에 picked 가 생기기 전에는 all 이 오디오를 만들지 않고 샘플만 만든다 (build 는 멈춘다)

역할 (사용자 지시 2026-10-10) — 말투는 설정 파일 하나로 정해져 있고 고르지 않는다 (사용자 지시 2026-10-11)
  - ★ 2026-10-15 사용자 지시 "진행자 목소리로만": voices/storyteller.json 의 enabled=false → 사연자 역할을 끄고 모든 문장을 진행자가 읽는다.
    다시 켜려면 enabled 를 지우거나 true (그러면 사연 파트는 다시 사연자 S07).
  - 사연자(storyteller): 파트 라벨에 '사연'이 든 문장 — 1인칭 고백. 설정 voices/storyteller.json
  - 진행자(host): 나머지 모든 파트(진행자·문제 분석·올바른 방법·마무리). 설정 voices/host.json — 중저음 남성, lock(덮어쓰기 없음)
  - 설정은 voices/<역할>.json → <주제>/voices/<역할>.json → <주제>/source/<영상ID>/voices/<역할>.json 순서로 덮어쓴다.

결과 (영상마다 오디오 하나)
  저장소 <주제>/source/<영상ID>/narration.mp3      ← 영상에 쓰는 오디오 (--push 가 대본 폴더에 각각 올린다)
  (v1.9) 쇼츠: <주제>/source/<영상ID>/shorts/<영상ID>-shorts.txt → 같은 shorts/ 폴더에 narration.mp3 · tts_narration.json (영상ID = <영상ID>-shorts)
  저장소 <주제>/source/<영상ID>/tts_narration.json ← 문장별 역할·시작·끝, 대본 해시(check 용), 목소리 설정
  저장소 <주제>/source/<영상ID>/tts_report.md      ← 문장별 길이·속도·귀로 확인할 문장
  작업 폴더 OUT(= /kaggle/working/tts_out, Kaggle 밖에서는 output/tts): OUT/upload/… (위 세 파일, 올리기 전 원본),
           OUT/<영상ID>/storyteller/S###.wav · OUT/<영상ID>/host/S###.wav (역할별 문장 파일), OUT/<영상ID>/cache/

GitHub 올리기 (--push)
  - 토큰: 환경 변수 GITHUB_TOKEN, 없으면 Kaggle Secrets 의 GITHUB_TOKEN. 값은 로그·파일·명령줄·원격 주소에 남기지 않는다(GIT_ASKPASS).
  - 시작할 때 토큰으로 push 권한을 먼저 확인한다(git push --dry-run, 실제로 올리지 않음). 안 되면 만들기 전에 멈춘다.
  - 영상 하나가 끝날 때마다 그 영상의 세 파일만 git add → 커밋 → pull --rebase → push (최대 4번 다시). 다른 파일은 올리지 않는다.
  - GPU 2개(--split)로 동시에 돌려도 git 작업은 잠금 파일로 하나씩 한다.

규칙 (guides/tts_guide.md 5번, guides/video_guide.md 2번 "내레이션")
  - 문장 = tools/srt_tool.py parse_txt 와 같은 순서(파트 라벨·[장면]·카드 문구 제외). 오디오 문장 = 대본 문장.
  - 문장 사이 쉼 = 역할 설정의 gap(기본 0.45초, 디지털 무음), 파트가 바뀌면 1.0초. align-audio(무음 −35dB·0.12초 이상)가 이 쉼으로 문장 경계를 찾는다.
  - 고지 카드 자리([장면] 바로 앞 문장 뒤): srt_tool.parse_cards 의 길이(문구 글자 수 ÷ 7 + 1초, 4~8초). 최소 3.5초 규칙보다 길다.
  - 문장마다 검사: 말 속도 2.5~8음절/초, 문장 안 무음 1.8초 이하, NaN·빈 소리 없음. 벗어나면 시드를 바꿔 다시(최대 3번).
  - 말 속도 맞추기(pace, 역할·후보 설정): {"min": 음절/초, "max": 음절/초, "max_stretch": 0.15} — 고른 문장의 속도가 범위 밖이면
    가장 가까운 끝으로 ffmpeg atempo(음 높이 그대로)로 늘이거나 줄인다. 한 번에 ±15%까지만(그 이상은 소리가 어색해짐). 보고서에 배율
  - 볼륨: 영상 전체에 이득 하나만 곱한다(말소리 RMS −18dBFS, 최고점 −1dBFS 이하). 문장·역할마다 따로 바꾸지 않는다.
  - 문장 파일은 OUT/<영상ID>/cache/ 에 남는다(<키>.wav + <키>.json). 글·말투·화자·설정이 같으면 다시 만들지 않는다.
※ 연구·교육용 도구다. 영상 내용은 투자 권유가 아니다(주식 영상 고지 규칙은 stock/guides 를 따른다).
"""
import argparse
import hashlib
import importlib.util
import json
import logging
import math
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import wave
import zipfile
from datetime import datetime
from pathlib import Path

import numpy as np

TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent
sys.path.insert(0, str(TOOLS))
import srt_tool  # noqa: E402  (문장·카드 판정을 자막 도구와 똑같이 쓰기 위해)

VERSION = "v1.14"
CACHE_VERSION = 1            # 생성 방식이 바뀌면 올린다 → 문장 파일을 모두 다시 만든다 (v1.1은 v1.0 캐시와 같은 키)
DEFAULT_MODEL = "Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice"     # 사연자 (화자 + 말투 지시)
DEFAULT_CLONE_MODEL = "Qwen/Qwen3-TTS-12Hz-1.7B-Base"       # 진행자 (기준 목소리 복제)
DEFAULT_DESIGN_MODEL = "Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign"   # 진행자 기준 목소리를 처음 한 번 만들 때
F0_TOL = 0.30                # 진행자 문장의 목소리 높이가 기준 목소리에서 ±30% 넘게 벗어나면 다시 (대본마다 같은 목소리)
DESIGN_RATE = (3.8, 6.0)     # 기준 목소리: 귀에 잘 들어오는 말 속도(음절/초)
DESIGN_MAX_SIL = 1.0         # 기준 목소리: 문장 안 무음 한도(초)
FRAME_HZ = 12.5              # Qwen3-TTS-Tokenizer-12Hz: 24000Hz ÷ 1920 = 초당 12.5 프레임 (max_new_tokens 계산)
CARD_GAP_MIN = srt_tool.CARD_GAP_MIN   # 3.5초 — align-audio.mjs 와 같은 값
MIN_RATE, MAX_RATE = 2.5, 8.0  # 문장 말 속도(읽는 음절/초) 허용 범위. 성공 영상 4.2~5.5 (stock/guides/data_insights.md 2번)
SHORT_SYL = 6                # 이보다 짧은 문장("감사합니다.")은 속도 대신 길이 4초 이하만 본다
MAX_INNER_SIL = 1.8          # 문장 안 무음이 이보다 길면 이상(말을 멈추고 딴소리·잡음일 수 있음)
SIL_DB = -45.0               # 10ms 구간 RMS가 이 값 이하면 무음 (앞뒤 자르기·문장 안 무음)
TRIM_PAD = 0.06              # 앞뒤를 자를 때 남기는 여유(초) — 숨소리·첫소리가 잘리지 않게
TARGET_RMS_DB = -18.0        # 말소리 구간 RMS 목표
PEAK_DB = -1.0               # 최고점 한도
RATE_REF = 4.8               # 검사를 모두 통과한 시도가 없을 때 이 속도에 가까운 것을 고른다
PATCH_MAX_FRAC = 0.2         # v1.8: 글이 바뀐 문장이 이 비율 이하면 그 문장만 다시 만들어 저장소 오디오에 끼운다 (넘으면 전부 다시)
MIN_GAP = 0.2                # 역할 설정 gap 하한 — align-audio 가 문장 경계로 보는 무음(0.12초)보다 넉넉하게

VOICES_DIR = ROOT / "voices"           # 역할별 목소리 설정 (파일 이름 = 역할 = 결과 폴더 이름)
VOICE_KEYS = {"role", "name", "parts", "engine", "lock", "speaker", "instruct", "part_instruct", "seed", "gap", "generation",
              "ref_audio", "ref_meta", "design", "f0_tolerance", "picked", "pace", "enabled", "own_voice"}
SAMPLES_DIR = VOICES_DIR / "samples"   # 목소리 후보 샘플 (하위 폴더라 역할 설정과 섞이지 않음)
SAMPLES_CFG = SAMPLES_DIR / "samples.json"
SAMPLE_HOW = ("current", "custom_voice", "design")
SAMPLE_GAP = 0.45                      # 샘플 문장 사이 쉼(초)
ENGINES = ("custom_voice", "clone")
GEN_KEYS = {"temperature", "top_p", "top_k", "repetition_penalty"}
STORY_ROLE = "storyteller"             # 사연자 역할 (영상 코드 plan.ts 의 STORY_LAST 와 비교)
AUDIO_EXTS = ("mp3", "wav", "m4a")     # align-audio.mjs·publish.sh 가 찾는 narration 확장자
META_NAME = "tts_narration.json"       # narration 옆에 두는 메타 (check 가 읽음). 'narration.*' 와 겹치지 않는 이름
ZIP_NAME = "narration_upload.zip"     # pack: 올리기가 안 될 때만 쓰는 zip
REPORT_NAME = "tts_report.md"          # narration 옆에 두는 보고 (문장별 길이·속도·귀로 확인할 문장)
REPO_FILES = ("narration.mp3", META_NAME, REPORT_NAME)   # --push 가 대본 폴더에 올리는 파일 (이것만)
TOKEN_ENV = "GITHUB_TOKEN"             # 환경 변수·Kaggle Secrets 이름. 값은 어디에도 출력하지 않는다
GIT_NAME, GIT_EMAIL = "tts_narration (Kaggle)", "tts-narration@users.noreply.github.com"
PUSH_TRIES = 4

LOG = logging.getLogger("tts")


# ----------------------------------------------------------------------------- 로그
def _fmt(v):
    if isinstance(v, float):
        return f"{v:.3f}".rstrip("0").rstrip(".") if math.isfinite(v) else str(v)
    s = str(v)
    return f'"{s}"' if (" " in s or not s) else s


def log(stage, level=logging.INFO, **kv):
    """[STAGE] [TIMESTAMP] key=value ... (가이드의 공통 로그 형식)"""
    LOG.log(level, "[%s] [%s] %s", stage, datetime.now().isoformat(timespec="seconds"),
            " ".join(f"{k}={_fmt(v)}" for k, v in kv.items()))


def die(stage, error, hint, **kv):
    log(stage, logging.ERROR, error=error, hint=hint, **kv)
    raise SystemExit(1)


def rel(p):
    try:
        return str(Path(p).resolve().relative_to(ROOT))
    except ValueError:
        return str(p)


def ranges(nums):
    """[1,2,3,7,8] → '1-3,7-8' (로그·보고서에서 역할별 문장 범위)"""
    out, start, prev = [], None, None
    for n in nums:
        if start is None:
            start = prev = n
        elif n == prev + 1:
            prev = n
        else:
            out.append(f"{start}-{prev}" if prev > start else str(start))
            start = prev = n
    if start is not None:
        out.append(f"{start}-{prev}" if prev > start else str(start))
    return ",".join(out)


def sha(obj):
    return hashlib.sha1(json.dumps(obj, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()[:16]


# ----------------------------------------------------------------------------- 대본
def read_script(txt_path):
    """(문장, 파트 라벨) 목록과 카드 목록. 판정은 srt_tool.parse_txt / parse_cards 와 같다(같은 is_label)."""
    rows, part, in_card = [], "", False
    for raw in Path(txt_path).read_text("utf-8-sig").splitlines():
        line = raw.strip()
        if not line:
            continue
        if srt_tool.is_label(line):
            part, in_card = line.lstrip("-").strip(), False
            continue
        if line.startswith("[장면]"):
            in_card = True
            continue
        if not in_card:
            rows.append((line, part))
    if [r[0] for r in rows] != srt_tool.parse_txt(txt_path):   # 같은 규칙인지 스스로 확인
        die("INPUT", "문장 판정이 srt_tool.parse_txt 와 다름", "srt_tool.py 가 바뀌었는지 확인", txt=txt_path)
    return rows, srt_tool.parse_cards(txt_path)


def script_sha(rows, cards):
    """대본 해시 — 문장·파트·고지 카드 쉼만 본다(빈 줄·띄어쓰기 바꿈은 무시). check·all 이 오디오가 지금 대본으로 만든 것인지 볼 때 쓴다."""
    return sha({"rows": [list(r) for r in rows], "cards": [[c["after"], c["seconds"]] for c in cards]})


def load_lexicon(paths):
    """읽는 소리 사전 TSV: '원문<TAB>읽는 소리' (# 주석). TTS에 넣는 글에만 쓰고 대본·자막은 그대로 둔다."""
    pairs = []
    for p in paths:
        if not p or not Path(p).is_file():
            continue
        n0 = len(pairs)
        for ln in Path(p).read_text("utf-8-sig").splitlines():
            if ln.strip() and not ln.lstrip().startswith("#") and "\t" in ln:
                src, dst = ln.split("\t", 1)
                pairs.append((src.strip(), dst.strip()))
        log("INPUT", lexicon=rel(p), entries=len(pairs) - n0)
    return sorted(pairs, key=lambda x: -len(x[0]))   # 긴 것부터 바꿔 겹침 방지


def tts_text(text, lexicon):
    """TTS에 넣는 글. 부호 붙은 금액은 뜻이 바뀌지 않게 소리로 바꾼다(srt_tool.spoken 과 같은 규칙): -800만 → 마이너스 800만."""
    s = text
    for src, dst in lexicon:
        s = s.replace(src, dst)
    s = re.sub(r"(?<![\w.])-(?=\d)", "마이너스 ", s)
    s = re.sub(r"(?<![\w.])\+(?=\d)", "플러스 ", s)
    return s


# ----------------------------------------------------------------------------- 목소리 설정 (역할)
def load_voices(topic=None, vid=None, args=None, quiet=False):
    """역할별 목소리 설정 → {역할: 설정}. voices/<역할>.json 을 주제·영상 폴더의 같은 이름 파일이 차례로 덮어쓴다.
    part_instruct·generation 은 항목 단위로 합친다. '_' 로 시작하는 항목(설명)은 무시한다."""
    base = sorted(VOICES_DIR.glob("*.json"))   # 역할 설정만 (기준 목소리는 voices/ref/ 하위 폴더라 섞이지 않음)
    if not base:
        die("VOICE", "목소리 설정 파일 없음", "저장소를 git pull 했는지 (voices/storyteller.json·host.json)", dir=rel(VOICES_DIR))
    voices = {}
    for p in base:
        role = p.stem
        cfg, files = {}, []
        layers = [p]
        locked = bool(json.loads(p.read_text("utf-8-sig")).get("lock")) if p.is_file() else False
        if topic and not locked:   # lock: 주제·영상 폴더의 덮어쓰기를 받지 않는다 (진행자 목소리는 모든 대본에서 같게)
            layers.append(ROOT / topic / "voices" / p.name)
            if vid:
                layers.append(src_dir(topic, vid) / "voices" / p.name)
        elif topic:                # v1.14 own_voice: 주제·영상 폴더 설정에 "own_voice": true 면 lock 을 넘어 그 영상만 다른 목소리
            for q in [ROOT / topic / "voices" / p.name] + ([src_dir(topic, vid) / "voices" / p.name] if vid else []):
                if not q.is_file():
                    continue
                try:
                    own = json.loads(q.read_text("utf-8-sig")).get("own_voice") is True
                except json.JSONDecodeError as e:
                    die("VOICE", f"설정 파일 JSON 오류: {e}", "쉼표·따옴표·괄호 확인 (마지막 항목 뒤에는 쉼표 없음)", file=rel(q))
                if own:
                    layers.append(q)
                    if not quiet:
                        log("VOICE", role=role, own_voice=rel(q), note="이 영상만 다른 목소리 (공통 lock 을 넘음)")
        for q in layers:
            if not q.is_file():
                continue
            try:
                d = json.loads(q.read_text("utf-8-sig"))
            except json.JSONDecodeError as e:
                die("VOICE", f"설정 파일 JSON 오류: {e}", "쉼표·따옴표·괄호 확인 (마지막 항목 뒤에는 쉼표 없음)", file=rel(q))
            unknown = sorted(k for k in d if k not in VOICE_KEYS and not k.startswith("_"))
            if unknown and not quiet:
                log("VOICE", logging.WARNING, file=rel(q), unknown=",".join(unknown), note="모르는 항목은 무시")
            for k, v in d.items():
                if k.startswith("_") or k not in VOICE_KEYS:
                    continue
                cfg[k] = {**cfg.get(k, {}), **v} if k in ("part_instruct", "generation") and isinstance(v, dict) else v
            files.append(rel(q))
        if locked and topic:
            ignored = [rel(q) for q in (ROOT / topic / "voices" / p.name, src_dir(topic, vid or "-") / "voices" / p.name)
                       if q.is_file() and q not in layers]
            if ignored and not quiet:
                log("VOICE", logging.WARNING, role=role, ignored=",".join(ignored), note="lock: 이 역할은 모든 대본에서 같은 목소리 — 덮어쓰기 무시")
        cfg = {"name": role, "parts": ["*"], "engine": "custom_voice", "lock": False, "speaker": "Sohee", "instruct": "",
               "part_instruct": {}, "seed": 1234, "gap": 0.45, "generation": {}, "f0_tolerance": F0_TOL, "picked": None, "pace": None,
               "enabled": True, **cfg, "role": role, "files": files}
        if cfg["enabled"] is False:   # 꺼진 역할 (사용자 지시 2026-10-15: 진행자 목소리로만) — 그 파트는 "*" 역할(진행자)이 읽는다
            if not quiet:
                log("VOICE", role=role, enabled=False, files=",".join(files), note="꺼진 역할 — 이 역할 문장은 진행자가 읽음 (고르기·샘플·모델에서 빠짐)")
            continue
        voices[role] = cfg
    # 명령줄 덮어쓰기 (설정 파일을 고치지 않고 시험할 때) — 바꾼 것은 로그에 남긴다
    if args is not None:
        for role, v in voices.items():
            for key, val in (("speaker", getattr(args, "speaker", None)), ("seed", getattr(args, "seed", None)),
                             ("gap", getattr(args, "gap", None))):
                if val is not None and v[key] != val:
                    if v["lock"]:
                        log("VOICE", logging.WARNING, role=role, key=key, cli_value=val, note="lock 역할이라 명령줄 값 무시")
                        continue
                    log("VOICE", role=role, key=key, file_value=v[key], cli_value=val, note="명령줄 값이 설정 파일보다 우선")
                    v[key] = val
    for role, v in voices.items():
        v["style_name"] = v["name"]
        if v["engine"] not in ENGINES:
            die("VOICE", f"없는 engine: {v['engine']}", f"{' 또는 '.join(ENGINES)}", role=role)
        if v["engine"] == "clone":
            if not v.get("ref_audio") or not v.get("ref_meta"):
                die("VOICE", "clone 은 ref_audio·ref_meta 가 필요", "예: voices/ref/host.wav, voices/ref/host.json", role=role)
            d = v.get("design") or {}
            if not (ROOT / v["ref_audio"]).is_file() and not (d.get("instruct") and d.get("text")):
                die("VOICE", "기준 목소리 파일도, 만들 설명(design.instruct·text)도 없음", "voices/<역할>.json 의 design 채우기", role=role)
            if v["part_instruct"]:
                log("VOICE", logging.WARNING, role=role, note="clone 은 말투 지시를 받지 않음 — part_instruct 무시 (기준 목소리의 말투 그대로)")
                v["part_instruct"] = {}
            v["style_name"] = f"{v['name']} — 기준 목소리 복제"
            if args is not None and getattr(args, "fake", False) and origin_is_github():
                # 가짜 소리로 만든 기준 목소리는 진짜 저장소의 voices/ref/ 에 절대 두지 않는다 → 작업 폴더에
                fake_dir = out_root(args) / "fake_ref"
                v["ref_audio"], v["ref_meta"] = str(fake_dir / f"{role}.wav"), str(fake_dir / f"{role}.json")
                if not quiet:
                    log("VOICE", logging.WARNING, role=role, reference=v["ref_audio"], note="--fake: 기준 목소리를 작업 폴더에 (저장소에 넣지 않음)")
            attach_reference(v)
        elif not str(v["instruct"]).strip():
            die("VOICE", "말투 지시(instruct)가 비어 있음", "voices/<역할>.json 의 instruct 채우기", role=role)
        if not isinstance(v["parts"], list) or not v["parts"]:
            die("VOICE", "parts 는 파트 라벨 낱말 목록이어야 함 (예: [\"사연\"] 또는 [\"*\"])", "voices/<역할>.json 확인", role=role)
        bad = sorted(set(v["generation"]) - GEN_KEYS)
        if bad:
            die("VOICE", f"generation 에 모르는 항목: {','.join(bad)}", f"쓸 수 있는 항목: {','.join(sorted(GEN_KEYS))}", role=role)
        if not isinstance(v["gap"], (int, float)) or v["gap"] < MIN_GAP:
            die("VOICE", f"gap {v['gap']} < {MIN_GAP}초", "문장 사이 쉼이 짧으면 align-audio 가 문장 경계를 못 찾음", role=role)
        if not isinstance(v["seed"], int):
            die("VOICE", f"seed 는 정수여야 함: {v['seed']}", "예: 1234", role=role)
        if v.get("pace") is not None and not pace_ok(v["pace"]):
            die("VOICE", f"pace 형식 오류: {v['pace']}", '예: {"min": 4.2, "max": 5.2, "max_stretch": 0.15} (음절/초, 늘이기·줄이기 한도 0.25 이하)', role=role)
    # 낱말로 정한 역할(사연자)을 먼저, 나머지("*") 역할(진행자)을 뒤에 — 로그·보고서 순서
    voices = dict(sorted(voices.items(), key=lambda kv: ("*" in kv[1]["parts"], kv[0])))
    wild = [r for r, v in voices.items() if "*" in v["parts"]]
    if len(wild) != 1:
        die("VOICE", f"나머지 파트(\"*\")를 맡는 역할이 {len(wild)}개", "한 역할만 parts 에 \"*\" (기본: host)", roles=",".join(wild) or "-")
    return voices


def attach_reference(v):
    """clone 역할: 저장소의 기준 목소리(wav)와 메타(json)를 읽어 붙인다. 파일이 바뀌었으면(해시 다름) 멈춘다."""
    ref, meta = ROOT / v["ref_audio"], ROOT / v["ref_meta"]
    v["ref_sha"] = v["ref_f0"] = v["ref_text"] = None
    if not (ref.is_file() and meta.is_file()):
        return
    m = json.loads(meta.read_text("utf-8"))
    actual = hashlib.sha1(ref.read_bytes()).hexdigest()[:16]
    if m.get("sha1") != actual:
        die("VOICE", f"기준 목소리 파일의 해시가 메타와 다름 ({actual} ≠ {m.get('sha1')})",
            "기준 목소리를 손으로 바꾸지 않는다. 다시 만들려면: python tools/tts_narration.py voice --force --push", file=rel(ref))
    v["ref_sha"], v["ref_f0"], v["ref_text"] = actual, float(m["f0_hz"]), m["text"]


_ORIGIN_GITHUB = None


def origin_is_github():
    """저장소 원격이 github.com 인가 (한 번만 확인). --fake 결과가 진짜 저장소에 섞이지 않게 쓴다."""
    global _ORIGIN_GITHUB
    if _ORIGIN_GITHUB is None:
        r = subprocess.run(["git", "-C", str(ROOT), "remote", "get-url", "origin"], capture_output=True, text=True)
        _ORIGIN_GITHUB = r.returncode == 0 and "github.com" in r.stdout
    return _ORIGIN_GITHUB


def voice_ids(voices, engine):
    """역할마다 '목소리 정체' 해시 — 이것이 바뀌면 이미 만든 오디오는 다른 목소리다 (대본마다 같은 목소리를 지키려고 다시 만든다)."""
    out = {}
    for role, v in voices.items():
        if v["engine"] == "clone":
            ident = {"engine": "clone", "model": engine_ids(engine)["clone"], "ref": v.get("ref_sha"), "seed": v["seed"],
                     "generation": v["generation"]}
        else:
            ident = {"engine": "custom_voice", "model": engine_ids(engine)["custom_voice"], "speaker": v["speaker"],
                     "instruct": v["instruct"], "part_instruct": v["part_instruct"], "seed": v["seed"], "generation": v["generation"]}
        if v.get("pace"):   # 말 속도 맞추기를 쓰면 정체에 넣는다 (안 쓰는 역할의 정체는 v1.4 와 같게 — 이미 만든 오디오를 옛 것으로 보지 않게)
            ident["pace"] = v["pace"]
        out[role] = sha(ident)
    return out


def engine_ids(engine):
    """모델 이름 (엔진이 없으면 명령줄 기본값 — check·all --dry-run 은 모델을 불러오지 않는다)."""
    if engine is not None:
        return engine.ids
    a = getattr(engine_ids, "args", None)
    if a is not None and a.fake:
        return {k: "fake" for k in MODEL_KINDS}
    return {"custom_voice": getattr(a, "model", DEFAULT_MODEL), "clone": getattr(a, "clone_model", DEFAULT_CLONE_MODEL),
            "design": getattr(a, "design_model", DEFAULT_DESIGN_MODEL)}


def role_of(part, voices):
    """파트 라벨 → 역할. 낱말이 맞는 역할이 먼저, 없으면 "*" 역할(진행자)."""
    for role, v in voices.items():
        if any(k != "*" and k in part for k in v["parts"]):
            return role
    return next(r for r, v in voices.items() if "*" in v["parts"])


def instruct_for(voice, part):
    """역할 안에서 파트별 말투(part_instruct)가 있으면 그것, 없으면 역할 기본 말투. → (지시, 말투 이름). clone 은 지시 없음."""
    if voice["engine"] == "clone":
        return "", voice["style_name"]
    for k, ins in voice["part_instruct"].items():
        if k in part:
            return ins, f"{voice['name']} · {k}"
    return voice["instruct"], voice["style_name"]


def spec_of(voice, instruct):
    """문장 하나를 만들 때 쓰는 목소리 값. 캐시 키·메타에 그대로 들어간다."""
    spec = {"engine": voice["engine"], "speaker": voice["speaker"] if voice["engine"] != "clone" else "-", "instruct": instruct,
            "gen": dict(voice["generation"]), "seed": voice["seed"], "gap": float(voice["gap"])}
    if voice["engine"] == "clone":
        spec.update(ref_audio=voice["ref_audio"], ref_sha=voice["ref_sha"], ref_f0=voice["ref_f0"], ref_text=voice["ref_text"],
                    f0_tol=float(voice["f0_tolerance"]))
    if voice.get("pace"):
        spec["pace"] = voice["pace"]
    return spec


def pace_ok(pc):
    try:
        lo, hi, st = float(pc.get("min", 0)), float(pc.get("max", 99)), float(pc.get("max_stretch", 0.15))
        sp = float(pc.get("speed", 1.0))
        return isinstance(pc, dict) and 0 < lo < hi and 0 < st <= 0.25 and 0.8 <= sp <= 1.25
    except Exception:
        return False


def atempo(x, sr, factor):
    """음 높이는 그대로 두고 빠르기만 factor 배 (ffmpeg atempo). 실패하면 None."""
    ff = find_ffmpeg()
    if not ff:
        return None
    with tempfile.TemporaryDirectory() as td:
        a, b = Path(td) / "in.wav", Path(td) / "out.wav"
        write_wav(a, x, sr)
        r = subprocess.run([ff, "-y", "-hide_banner", "-loglevel", "error", "-i", str(a), "-filter:a", f"atempo={factor:.4f}",
                            "-ac", "1", "-ar", str(sr), "-c:a", "pcm_s16le", str(b)], capture_output=True, text=True)
        if r.returncode != 0 or not b.is_file():
            log("PACE", logging.WARNING, error=r.stderr.strip()[:200], note="속도 맞추기 실패 — 원래 소리 그대로")
            return None
        y, _ = read_wav(b)
        return y


def plan_items(vid, rows, voices, lex):
    """문장마다 역할·말투를 정하고 역할별 범위를 로그로 남긴다."""
    items = []
    for n, (text, part) in enumerate(rows, 1):
        role = role_of(part, voices)
        instruct, style = instruct_for(voices[role], part)
        items.append({"n": n, "text": text, "part": part, "role": role, "style": style,
                      "spec": spec_of(voices[role], instruct), "tts": tts_text(text, lex), "syl": srt_tool.syllables(text)})
    for role, v in voices.items():
        mine = [it for it in items if it["role"] == role]
        log("ROLE", video=vid, role=role, name=v["name"], sentences=len(mine), range=ranges([it["n"] for it in mine]) or "-",
            syllables=sum(it["syl"] for it in mine), engine=v["engine"], speaker=v["speaker"] if v["engine"] != "clone" else "-",
            ref=f"{v['ref_audio']} f0={v['ref_f0']}Hz sha={v['ref_sha']}" if v["engine"] == "clone" else "-", lock=v["lock"], seed=v["seed"], gap_s=v["gap"],
            parts=" / ".join(dict.fromkeys(it["part"] for it in mine)) or "-", files=",".join(v["files"]))
    for style, ins in dict.fromkeys((it["style"], it["spec"]["instruct"]) for it in items):
        log("STYLE", video=vid, style=style, instruct=ins)
    story = [it["n"] for it in items if it["role"] == STORY_ROLE]
    plan = ROOT / "video" / "src" / "episodes" / vid / "plan.ts"
    mm = re.search(r"STORY_LAST\s*=\s*(\d+)", plan.read_text("utf-8")) if plan.is_file() else None
    if mm and story:   # 영상 코드의 사연 끝 번호와 대본의 사연자 끝 번호가 같은지 (다르면 자막·장면이 어긋남)
        ok = int(mm.group(1)) == story[-1]
        log("ROLE", level=logging.INFO if ok else logging.WARNING, video=vid, plan_story_last=int(mm.group(1)),
            script_story_last=story[-1], ok=ok, note="-" if ok else "영상 코드 plan.ts 의 STORY_LAST 와 다름 — 대본·영상 코드 확인")
    return items


# ----------------------------------------------------------------------------- 소리 계산 (numpy만)
def silence(sec, sr):
    return np.zeros(int(round(sec * sr)), dtype=np.float32)


def frame_db(x, sr, win=0.01):
    n = max(1, int(sr * win))
    m = len(x) // n
    if m == 0:
        return np.array([-120.0])
    fr = x[: m * n].reshape(m, n).astype(np.float64)
    return 10 * np.log10(np.mean(fr * fr, axis=1) + 1e-12)


def trim(x, sr):
    """앞뒤 무음만 자른다(TRIM_PAD 여유). 문장 사이 쉼을 이 도구가 정한 길이로 맞추기 위해서다."""
    voiced = np.where(frame_db(x, sr) > SIL_DB)[0]
    if voiced.size == 0:
        return x[:0]
    n, pad = int(sr * 0.01), int(sr * TRIM_PAD)
    return x[max(0, voiced[0] * n - pad): min(len(x), (voiced[-1] + 1) * n + pad)]


def longest_silence(x, sr):
    """가장 긴 무음 구간(초). 10ms 구간의 무음 여부가 바뀌는 곳으로 구간 길이를 잰다(반복문 없음)."""
    q = np.concatenate([[0], (frame_db(x, sr) <= SIL_DB).astype(np.int8), [0]])
    d = np.diff(q)
    starts, ends = np.where(d == 1)[0], np.where(d == -1)[0]
    return float((ends - starts).max()) * 0.01 if starts.size else 0.0


def voiced_rms_db(x, sr):
    db = frame_db(x, sr)
    v = db[db > SIL_DB]
    return float(10 * np.log10(np.mean(10 ** (v / 10)))) if v.size else -120.0


def check(x, sr, syl, nonfinite):
    """문장 하나 검사 → (통과 여부, 문제 목록, 경고 목록, 수치)."""
    issues, warns = [], []
    if nonfinite:
        issues.append("NaN/inf")
    dur = len(x) / sr if sr else 0.0
    if dur <= 0.05:
        return False, issues + ["빈 소리"], warns, {"dur": dur, "rate": 0.0, "inner_sil": 0.0, "rms_db": -120.0, "peak": 0.0}
    rate = syl / dur
    if syl >= SHORT_SYL:
        if not MIN_RATE <= rate <= MAX_RATE:
            issues.append(f"말 속도 {rate:.1f}음절/초(허용 {MIN_RATE}~{MAX_RATE})")
    elif dur > 4.0:
        issues.append(f"짧은 문장인데 {dur:.1f}초")
    sil = longest_silence(x, sr)
    if sil > MAX_INNER_SIL:
        issues.append(f"문장 안 무음 {sil:.1f}초")
    peak = float(np.max(np.abs(x)))
    if np.mean(np.abs(x) >= 0.999) > 0.001:
        warns.append("소리 깨짐(클리핑) 의심")
    return not issues, issues, warns, {"dur": dur, "rate": rate, "inner_sil": sil, "rms_db": voiced_rms_db(x, sr), "peak": peak}


def write_wav(path, x, sr):
    y = np.clip(x, -1.0, 1.0)
    pcm = (y * 32767.0).round().astype("<i2")
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes(pcm.tobytes())


def read_wav(path):
    with wave.open(str(path), "rb") as w:
        sr, data = w.getframerate(), w.readframes(w.getnframes())
    return np.frombuffer(data, dtype="<i2").astype(np.float32) / 32767.0, sr


# ----------------------------------------------------------------------------- 엔진 (모델 세 가지를 필요할 때 불러온다)
MODEL_KINDS = ("custom_voice", "clone", "design")


class QwenPool:
    """Qwen3-TTS 모델 묶음.
      custom_voice — CustomVoice (사연자: 화자 Sohee + 말투 지시)
      clone        — Base (진행자: 저장소의 기준 목소리 voices/ref/host.wav 를 복제해 모든 대본에서 같은 목소리)
      design       — VoiceDesign (기준 목소리가 없을 때 한 번만: 글로 묘사한 목소리 → voices/ref/host.wav)
    GPU 가 둘이면 custom_voice 는 --gpu, clone·design 은 다른 GPU. 하나면 한 번에 한 모델만 올린다(바꿀 때 내림)."""

    def __init__(self, args):
        try:
            import torch
            import qwen_tts  # noqa: F401  (설치 확인)
        except ImportError as e:
            die("MODEL", f"패키지 없음: {e}", "Kaggle 셀에서 먼저: !pip install -q -U qwen-tts")
        self.torch, self.args, self.language = torch, args, args.language
        self.ids = {"custom_voice": args.model, "clone": args.clone_model, "design": args.design_model}
        n = torch.cuda.device_count() if torch.cuda.is_available() else 0
        if args.device:
            dev = {k: args.device for k in MODEL_KINDS}
        elif n == 0:
            log("MODEL", logging.WARNING, device="cpu", note="GPU가 없음 — CPU는 문장 하나에 몇 분 걸림. Kaggle: Accelerator 'GPU T4 x2'")
            dev = {k: "cpu" for k in MODEL_KINDS}
        else:
            g0 = args.gpu % n
            g1 = (g0 + 1) % n if n >= 2 else g0
            dev = {"custom_voice": f"cuda:{g0}", "clone": f"cuda:{g1}", "design": f"cuda:{g1}"}
        self.devices, self.single = dev, len(set(dev.values())) == 1 and dev["custom_voice"] != "cpu"
        self.dtypes = {k: self._dtype_name(d) for k, d in dev.items()}
        self.models, self.prompts = {}, {}
        self.gen = {k: v for k, v in {"temperature": args.temperature, "top_p": args.top_p, "top_k": args.top_k,
                                      "repetition_penalty": args.repetition_penalty}.items() if v is not None}
        log("MODEL", gpus=n, devices=" ".join(f"{k}={v}" for k, v in dev.items()), dtypes=" ".join(f"{k}={v}" for k, v in self.dtypes.items()),
            note="GPU 하나: 모델을 바꿔 가며 올림" if self.single else "역할별 모델을 서로 다른 GPU에")

    def _dtype_name(self, device):
        torch = self.torch
        cap = torch.cuda.get_device_capability(device) if device.startswith("cuda") else (0, 0)
        # T4(7.5)는 bfloat16 연산 장치가 없고 float16은 값이 넘쳐 NaN이 날 수 있다 → 기본 float32 (1.7B ≈ 7GB, T4 16GB에 하나씩)
        return ("bfloat16" if cap >= (8, 0) else "float32") if self.args.dtype == "auto" else self.args.dtype

    def unload(self, kind):
        if kind in self.models:
            del self.models[kind]
            self.prompts = {k: v for k, v in self.prompts.items() if k[0] != kind}
            import gc
            gc.collect()
            if self.torch.cuda.is_available():
                self.torch.cuda.empty_cache()
            log("MODEL", unloaded=kind)

    def get(self, kind):
        if kind in self.models:
            return self.models[kind]
        if self.single:   # GPU 하나: 메모리를 넘지 않게 다른 모델을 내린다
            for other in list(self.models):
                self.unload(other)
        torch, args = self.torch, self.args
        from qwen_tts import Qwen3TTSModel
        device, dtype_name, model_id = self.devices[kind], self.dtypes[kind], self.ids[kind]
        cap = torch.cuda.get_device_capability(device) if device.startswith("cuda") else (0, 0)
        if device.startswith("cuda") and cap < (7, 0):
            log("MODEL", logging.WARNING, capability=f"{cap[0]}.{cap[1]}", note="P100 등 옛 GPU는 최신 PyTorch가 지원하지 않을 수 있음 → 'GPU T4 x2'")
        attn = args.attn
        if attn == "auto":
            attn = ("flash_attention_2" if cap >= (8, 0) and dtype_name != "float32" and importlib.util.find_spec("flash_attn")
                    else "sdpa")
        gpu = torch.cuda.get_device_name(device) if device.startswith("cuda") else "CPU"
        log("MODEL", kind=kind, model=model_id, device=device, gpu=gpu, dtype=dtype_name, attn=attn)
        t0 = time.time()
        try:
            m = Qwen3TTSModel.from_pretrained(model_id, device_map=device, dtype=getattr(torch, dtype_name), attn_implementation=attn)
        except Exception as e:  # 다운로드·메모리·버전 문제를 한 곳에서 안내
            die("MODEL", f"모델을 불러오지 못함 ({kind}): {type(e).__name__}: {e}",
                "Kaggle 설정에서 Internet 켜기(휴대폰 인증 필요) / GPU 메모리 부족이면 런타임 재시작 / --attn sdpa 로 다시")
        mem = torch.cuda.memory_allocated(device) / 1e9 if device.startswith("cuda") else 0.0
        langs = m.get_supported_languages() or []
        log("MODEL", kind=kind, loaded_s=time.time() - t0, gpu_mem_gb=mem, languages=",".join(langs))
        if langs and self.language.lower() not in [x.lower() for x in langs]:
            die("MODEL", f"없는 언어: {self.language}", f"--language 를 이 중에서: {', '.join(langs)}")
        if kind == "custom_voice":
            log("MODEL", speakers=",".join(m.get_supported_speakers() or []))
            if "0.6B" in model_id:
                log("MODEL", logging.WARNING, note="0.6B 모델은 말투 지시(instruct)를 무시함 — 감정 표현은 1.7B")
        self.models[kind] = m
        return m

    def check_speakers(self, speakers):
        if not speakers:        # custom_voice 역할이 없으면 화자 확인용으로 CustomVoice 모델(3.8GB)을 불러오지 않는다 (v1.6)
            return
        spk = self.get("custom_voice").get_supported_speakers() or []
        for s in sorted(speakers):
            if spk and s.lower() not in [x.lower() for x in spk]:
                die("MODEL", f"없는 화자: {s}", f"voices/<역할>.json 의 speaker 를 이 중에서: {', '.join(spk)}")

    def _seed(self, seed):
        self.torch.manual_seed(seed)
        if self.torch.cuda.is_available():
            self.torch.cuda.manual_seed_all(seed)

    def _call(self, fn):
        torch = self.torch
        try:
            wavs, sr = fn()
        except torch.cuda.OutOfMemoryError as e:
            torch.cuda.empty_cache()
            log("TTS", logging.ERROR, error=f"GPU 메모리 부족: {e}", hint="런타임 재시작 후 다시 (만든 문장은 cache에 남아 있음)")
            raise
        except RuntimeError as e:   # 예: float16 넘침 → 'probability tensor contains either inf, nan'
            log("TTS", logging.WARNING, error=f"{type(e).__name__}: {str(e)[:200]}",
                hint="--dtype float16 을 썼다면 float32 로" if "nan" in str(e).lower() or "inf" in str(e).lower() else "")
            return None
        return np.asarray(wavs[0], dtype=np.float32).reshape(-1), int(sr)

    def synth(self, text, spec, seed, max_new_tokens):
        """→ (소리 float32, 표본율) 또는 생성 오류면 None."""
        gen = {**self.gen, **spec["gen"]}
        if spec["engine"] == "clone":
            m = self.get("clone")
            pk = ("clone", spec["ref_sha"])
            if pk not in self.prompts:   # 기준 목소리 → 복제 프롬프트 (ICL: 기준 소리 + 기준 문장). 한 번만 만든다
                x, sr = read_wav(ROOT / spec["ref_audio"])
                self.prompts[pk] = m.create_voice_clone_prompt(ref_audio=(x, sr), ref_text=spec["ref_text"], x_vector_only_mode=False)
                log("MODEL", clone_prompt="만듦", ref=spec["ref_audio"], ref_sha=spec["ref_sha"])
            self._seed(seed)
            return self._call(lambda: m.generate_voice_clone(text=text, language=self.language, voice_clone_prompt=self.prompts[pk],
                                                             max_new_tokens=max_new_tokens, **gen))
        m = self.get("custom_voice")
        self._seed(seed)
        return self._call(lambda: m.generate_custom_voice(text=text, speaker=spec["speaker"], language=self.language,
                                                          instruct=spec["instruct"] or None, max_new_tokens=max_new_tokens, **gen))

    def design(self, text, instruct, seed, max_new_tokens):
        m = self.get("design")
        self._seed(seed)
        return self._call(lambda: m.generate_voice_design(text=text, instruct=instruct, language=self.language,
                                                          max_new_tokens=max_new_tokens, **self.gen))

    def describe(self, spec):
        if spec["engine"] == "clone":
            return {"engine": "qwen3-tts-clone", "model": self.ids["clone"], "ref": spec["ref_sha"], "mode": "icl",
                    "language": self.language, "dtype": self.dtypes["clone"], "gen": {**self.gen, **spec["gen"]}}
        # v1.0 과 같은 모양 → 화자 Sohee·생성 설정 기본이면 v1.0 에서 만든 문장 캐시를 그대로 쓴다
        return {"engine": "qwen3-tts", "model": self.ids["custom_voice"], "speaker": spec["speaker"], "language": self.language,
                "dtype": self.dtypes["custom_voice"], "gen": {**self.gen, **spec["gen"]}}


class FakeEngine:
    """테스트용: 모델 없이 문장 길이에 맞는 가짜 소리(읽는 음절 ÷ 4.8초, 쉼표마다 0.25초 쉼, 앞뒤 무음).
    사연자는 말투 지시마다 음 높이가 다르고, 진행자(복제)는 기준 목소리 높이, 목소리 만들기(design)는 시드마다 높이가 다르다."""

    def __init__(self, args):
        self.sr, self.ids = 24000, {k: "fake" for k in MODEL_KINDS}
        log("MODEL", engine="fake", note="가짜 소리 — 역할 나누기·잇기·쉼·내보내기·목소리 높이 검사·align-audio 확인용")

    def check_speakers(self, speakers):
        return None

    def unload(self, kind):
        return None

    def _tone(self, text, hz, seed):
        rng = np.random.default_rng(seed)
        out = [silence(0.15, self.sr)]
        chunks = [c for c in re.split(r"[,，]", text) if c.strip()]
        for i, ch in enumerate(chunks):
            d = max(0.3, srt_tool.syllables(ch) / 4.8 * rng.uniform(0.9, 1.1))
            t = np.arange(int(d * self.sr)) / self.sr
            out.append((0.2 * np.sin(2 * np.pi * hz * t) * (0.6 + 0.4 * np.sin(2 * np.pi * 4.8 * t))).astype(np.float32))
            if i < len(chunks) - 1:
                out.append(silence(0.25, self.sr))
        out.append(silence(0.3, self.sr))
        return np.concatenate(out), self.sr

    def synth(self, text, spec, seed, max_new_tokens):
        if spec["engine"] == "clone":
            return self._tone(text, spec["ref_f0"] * (1 + 0.04 * np.sin(seed)), seed)
        return self._tone(text, 150 + int(hashlib.sha1(spec["instruct"].encode("utf-8")).hexdigest()[:4], 16) % 120, seed)

    def design(self, text, instruct, seed, max_new_tokens):
        return self._tone(text, 70 + (seed * 53) % 130, seed)   # 70~199Hz — 범위 밖 시드로 다시 시도하는 길도 시험

    def describe(self, spec):
        if spec["engine"] == "clone":
            return {"engine": "fake-clone", "model": "fake", "ref": spec["ref_sha"], "language": "-", "dtype": "-", "gen": {}}
        return {"engine": "fake", "model": "fake", "speaker": spec["speaker"], "language": "-", "dtype": "-", "gen": {}}


def make_engine(args):
    return FakeEngine(args) if args.fake else QwenPool(args)


# ----------------------------------------------------------------------------- 목소리 높이 (진행자 남성 중저음 확인)
def f0_median(x, sr, fmin=60.0, fmax=400.0):
    """말소리의 기본 주파수(목소리 높이) 중간값(Hz). 40ms 구간 자기상관(FFT), 소리가 큰 구간·주기가 뚜렷한 구간만. 못 재면 0."""
    frame, hop = int(0.04 * sr), int(0.02 * sr)
    n = (len(x) - frame) // hop
    if n <= 0:
        return 0.0
    starts = hop * np.arange(n)
    if n > 800:   # 긴 소리는 고르게 800구간만 (속도)
        starts = starts[np.linspace(0, n - 1, 800).astype(int)]
    fr = x[starts[:, None] + np.arange(frame)[None, :]].astype(np.float64) * np.hanning(frame)
    energy = np.mean(fr * fr, axis=1)
    loud = energy > max(10 ** (SIL_DB / 10), np.percentile(energy, 40))
    fr = fr[loud]
    if not len(fr):
        return 0.0
    nfft = 1 << (2 * frame - 1).bit_length()
    spec = np.fft.rfft(fr, nfft, axis=1)
    ac = np.fft.irfft(spec * np.conj(spec), nfft, axis=1)[:, :frame]
    lo, hi = int(sr / fmax), min(int(sr / fmin), frame - 1)
    seg = ac[:, lo:hi]
    lag = lo + np.argmax(seg, axis=1)
    clear = seg.max(axis=1) / (ac[:, 0] + 1e-12) > 0.3
    return float(np.median(sr / lag[clear])) if clear.any() else 0.0


# ----------------------------------------------------------------------------- 문장 하나 만들기 (캐시·검사·다시)
def cache_key(engine, text, spec):
    d = dict(engine.describe(spec), text=text, instruct=spec["instruct"], seed=spec["seed"], cache=CACHE_VERSION)
    if spec.get("pace"):
        d["pace"] = spec["pace"]
    return hashlib.sha1(json.dumps(d, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()[:16]


def make_sentence(engine, cache_dir, label, text, spec, syl, args, redo=False, role="-"):
    """캐시에 있으면 그대로, 없으면(또는 redo) 만들고 검사한다. → 메타 dict (wav 경로 포함)."""
    key = cache_key(engine, text, spec)
    wav_p, meta_p = cache_dir / f"{key}.wav", cache_dir / f"{key}.json"
    old = json.loads(meta_p.read_text("utf-8")) if meta_p.is_file() else None
    if old and wav_p.is_file() and not redo:
        log("CACHE", level=logging.DEBUG, item=label, role=role, key=key, dur=old["dur"], ok=old["ok"])
        return dict(old, wav=str(wav_p), cached=True)
    # 시드: 역할 기본 시드 + 글 내용 해시(문장 위치가 바뀌어도 같은 글은 같은 시드) + 시도 번호. redo 는 전에 쓴 시도 다음부터.
    seed0 = spec["seed"] + int(key[:6], 16) % 1_000_000 * 10
    start = (max(old.get("tried", [0])) + 1) if (old and redo) else 1
    max_new = int(FRAME_HZ * max(syl, 4) / 2.0) + 50     # 2음절/초보다 느리면 끊는다(그보다 느리면 어차피 검사 탈락)
    best, tried = None, list(old.get("tried", [])) if (old and redo) else []
    for attempt in range(start, start + args.max_tries):
        seed = seed0 + attempt
        tried.append(attempt)
        t0 = time.time()
        res = engine.synth(text, spec, seed, max_new)
        gen_s = time.time() - t0
        if res is None:
            log("TTS", logging.WARNING, item=label, role=role, attempt=attempt, seed=seed, ok=False, issues="생성 오류")
            continue
        x, sr = res
        nonfinite = not np.isfinite(x).all()
        x = trim(np.nan_to_num(x, nan=0.0, posinf=0.0, neginf=0.0), sr)
        ok, issues, warns, m = check(x, sr, syl, nonfinite)
        m["f0"] = f0_median(x, sr) if x.size else 0.0
        f0_dev = 0.0
        if spec["engine"] == "clone" and syl >= SHORT_SYL and spec.get("ref_f0"):   # 진행자: 기준 목소리 높이와 같은가
            f0_dev = abs(m["f0"] / spec["ref_f0"] - 1) if m["f0"] else 1.0
            if f0_dev > spec["f0_tol"]:
                issues.append(f"목소리 높이 {m['f0']:.0f}Hz (기준 {spec['ref_f0']:.0f}Hz ±{spec['f0_tol']:.0%})")
                ok = False
        log("TTS", level=logging.INFO if ok else logging.WARNING, item=label, role=role, attempt=attempt, seed=seed, syl=syl,
            dur=m["dur"], rate=m["rate"], inner_sil=m["inner_sil"], f0=m["f0"], gen_s=gen_s, rtf=gen_s / max(m["dur"], 1e-6),
            ok=ok, issues=";".join(issues) or "-", warns=";".join(warns) or "-")
        score = (0 if ok else 1, abs(math.log(max(m["rate"], 1e-3) / RATE_REF)) + max(0.0, m["inner_sil"] - MAX_INNER_SIL) + f0_dev)
        if best is None or score < best[0]:
            best = (score, x, sr, attempt, seed, ok, issues, warns, m, gen_s)
        if ok:
            break
    if best is None:
        die("TTS", f"{label}: {args.max_tries}번 모두 생성 오류", "로그의 오류를 보고 --dtype float32 / 런타임 재시작 후 다시", text=text)
    _, x, sr, attempt, seed, ok, issues, warns, m, gen_s = best
    pace_factor = 1.0
    pc = spec.get("pace")
    if pc and m["rate"] > 0:   # 말 속도 맞추기 (음 높이 그대로, ±max_stretch 까지)
        lo, hi, lim = float(pc.get("min", 0)), float(pc.get("max", 99)), float(pc.get("max_stretch", 0.15))
        sp = float(pc.get("speed", 1.0))   # 모든 문장을 이 배수로 (v1.6) → 그다음 [min, max] 안으로
        if syl >= SHORT_SYL:
            target = min(max(m["rate"] * sp, lo), hi)
            f = target / m["rate"]
        else:                              # 짧은 문장은 속도 재기가 부정확 → speed 만 고르게
            f, target = sp, m["rate"] * sp
        f = min(max(f, 1 - lim), 1 + lim)
        if abs(f - 1) > 1e-3:
            y = atempo(x, sr, f)
            if y is not None:
                before = m["rate"]
                x, pace_factor = trim(y, sr), f
                _, issues2, warns2, m2 = check(x, sr, syl, False)
                m2["f0"] = m["f0"]
                issues = issues2 + [i for i in issues if i.startswith("목소리 높이")]
                ok, m = not issues, m2
                log("PACE", item=label, role=role, rate_before=before, rate_after=m["rate"], factor=round(f, 3), speed=sp,
                    target=f"{lo}-{hi}")
    write_wav(wav_p, x, sr)
    meta = {"key": key, "text": text, "instruct": spec["instruct"], "syl": syl, "sr": sr, "attempt": attempt, "seed": seed,
            "base_seed": spec["seed"], "role": role,
            "tried": tried, "ok": ok, "issues": issues, "warns": warns, "gen_s": round(gen_s, 2), "pace_factor": round(pace_factor, 3),
            **{k: round(float(v), 3) for k, v in m.items()}, **engine.describe(spec), "tool": VERSION}
    meta_p.write_text(json.dumps(meta, ensure_ascii=False, indent=1), "utf-8")
    if not ok:
        log("QA", logging.WARNING, item=label, role=role, chosen_attempt=attempt, issues=";".join(issues),
            note="모든 시도가 검사 탈락 — 가장 나은 것을 씀, 귀로 확인")
    return dict(meta, wav=str(wav_p), cached=False)


def cached_sentence(engine, cache_dir, text, spec):
    """--assemble-only: 모델을 쓰지 않고 캐시 키로 문장 파일을 찾는다 (없으면 None)."""
    key = cache_key(engine, text, spec)
    wav_p, meta_p = cache_dir / f"{key}.wav", cache_dir / f"{key}.json"
    if wav_p.is_file() and meta_p.is_file():
        return dict(json.loads(meta_p.read_text("utf-8")), wav=str(wav_p), cached=True)
    return None


# ----------------------------------------------------------------------------- 잇기·볼륨·내보내기
def gain_for(clips, sr):
    """전체 말소리 RMS를 TARGET_RMS_DB로, 최고점은 PEAK_DB 이하로 — 이득 하나(dB)."""
    allv = np.concatenate([c for c in clips if c.size]) if clips else np.zeros(1, np.float32)
    rms_db, peak = voiced_rms_db(allv, sr), float(np.max(np.abs(allv)) or 1e-9)
    peak_db = 20 * math.log10(peak)
    g = min(TARGET_RMS_DB - rms_db, PEAK_DB - peak_db)
    log("ASSEMBLE", rms_db_before=rms_db, peak_db_before=peak_db, gain_db=g, rms_db_after=rms_db + g, peak_db_after=peak_db + g)
    if rms_db + g < TARGET_RMS_DB - 3:
        log("ASSEMBLE", logging.WARNING, note="최고점 한도 때문에 목표보다 3dB 넘게 작음 — 튀는 소리가 있는 문장 확인")
    return g


def find_ffmpeg():
    ff = shutil.which("ffmpeg")
    if ff:
        return ff
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        return None


def export(y, sr, out_mp3, keep_wav=False):
    out_mp3 = Path(out_mp3)
    out_mp3.parent.mkdir(parents=True, exist_ok=True)
    wav_p = out_mp3.with_suffix(".wav")
    write_wav(wav_p, y, sr)
    ff = find_ffmpeg()
    if not ff:
        log("EXPORT", logging.WARNING, wav=wav_p, note="ffmpeg 없음 → WAV만 저장 (pip install imageio-ffmpeg 후 --assemble-only)")
        return wav_p
    r = subprocess.run([ff, "-y", "-hide_banner", "-loglevel", "error", "-i", str(wav_p), "-c:a", "libmp3lame", "-b:a", "160k", str(out_mp3)],
                       capture_output=True, text=True)
    if r.returncode != 0:
        log("EXPORT", logging.ERROR, error=r.stderr.strip()[:300], wav=wav_p, hint="WAV는 남아 있음 — 그대로 올려도 됨(25MB 이하일 때)")
        return wav_p
    probe = subprocess.run([ff, "-hide_banner", "-i", str(out_mp3)], capture_output=True, text=True).stderr
    mm = re.search(r"Duration:\s*(\d+):(\d+):([\d.]+)", probe)
    mp3_s = int(mm.group(1)) * 3600 + int(mm.group(2)) * 60 + float(mm.group(3)) if mm else float("nan")
    if not keep_wav:
        wav_p.unlink()
    log("EXPORT", mp3=out_mp3, seconds=len(y) / sr, mp3_seconds=mp3_s, mb=out_mp3.stat().st_size / 1e6)
    return out_mp3


def mmss(t):
    return f"{int(t // 60)}:{t % 60:04.1f}"


# ----------------------------------------------------------------------------- 결과 경로
def out_root(args):
    if args.out_dir:
        return Path(args.out_dir)
    kaggle = Path("/kaggle/working")
    return (kaggle / "tts_out") if kaggle.is_dir() else (ROOT / "output" / "tts")


SHORTS_SUFFIX = "-shorts"   # v1.9: 영상ID 가 이렇게 끝나면 쇼츠 — 대본 폴더는 source/<롱폼 영상ID>/shorts/


def src_dir(topic, vid):
    """대본 폴더: 롱폼 <주제>/source/<영상ID> · 쇼츠(<영상ID>-shorts) <주제>/source/<영상ID>/shorts (v1.9)."""
    if vid and vid.endswith(SHORTS_SUFFIX):
        return ROOT / topic / "source" / vid[: -len(SHORTS_SUFFIX)] / "shorts"
    return ROOT / topic / "source" / vid


def script_entries():
    """저장소의 모든 대본 TXT → [(주제, 영상ID, TXT)] — 롱폼 <영상ID>/<영상ID>.txt 와 쇼츠 <영상ID>/shorts/<영상ID>-shorts.txt (v1.9)."""
    out = []
    for txt in sorted(ROOT.glob("*/source/*/*.txt")):
        if txt.stem == txt.parent.name:
            out.append((txt.parents[2].name, txt.stem, txt))
    for txt in sorted(ROOT.glob("*/source/*/shorts/*.txt")):
        if txt.stem == txt.parents[1].name + SHORTS_SUFFIX:
            out.append((txt.parents[3].name, txt.stem, txt))
    return out


def episode_paths(root, topic, vid):
    """정해진 결과 경로. upload/ 아래는 저장소와 같은 경로라 그대로 올리면 된다."""
    up = root / "upload" / src_dir(topic, vid).relative_to(ROOT)
    work = root / vid
    return {"upload": up, "narration": up / "narration.mp3", "meta": up / META_NAME,
            "work": work, "cache": work / "cache", "report": up / REPORT_NAME}


def repo_audio(topic, vid):
    src = src_dir(topic, vid)
    return next((src / f"narration.{e}" for e in AUDIO_EXTS if (src / f"narration.{e}").is_file()), None)


# ----------------------------------------------------------------------------- 부분 다시 만들기 (v1.8)
def voices_meta(voices):
    """메타에 적는 역할 설정 (build·patch 가 같은 모양으로)."""
    return {r: {k: v.get(k) for k in ("name", "parts", "engine", "lock", "speaker", "instruct", "part_instruct", "seed",
                                       "gap", "generation", "ref_audio", "ref_sha", "ref_f0", "files")} for r, v in voices.items()}


def patch_candidate(topic, vid, rows, cards, args):
    """저장소 오디오는 그대로 두고 글이 바뀐 문장만 다시 만들 수 있는지 (모델 없이 판단).
    → (바뀐 문장 번호 목록, None) 또는 (None, 전부 다시 만드는 이유). 문장 수·파트·카드·쉼·목소리가 모두 같고 글만 바뀐 경우만."""
    src = src_dir(topic, vid)
    mp3, meta_p = src / "narration.mp3", src / META_NAME
    if getattr(args, "full", False) or getattr(args, "force", False):
        return None, "--full/--force"
    if not mp3.is_file() or not meta_p.is_file():
        return None, "저장소에 narration.mp3·메타 없음"
    meta = json.loads(meta_p.read_text("utf-8"))
    if meta.get("script_sha1") == script_sha(rows, cards):
        return None, "바뀐 문장 없음"
    bad = voice_mismatch(meta, topic, vid)
    if bad:
        return None, f"목소리가 바뀜({','.join(bad)})"
    old = meta.get("items") or []
    if len(old) != len(rows):
        return None, f"문장 수가 다름 ({len(old)} → {len(rows)})"
    olds, news = [o.get("part") for o in old], [p for _, p in rows]
    if any((olds[i] != olds[i - 1]) != (news[i] != news[i - 1]) for i in range(1, len(rows))):
        return None, "파트(챕터) 나눔이 다름"            # v1.10: 경계가 바뀌면 쉼(파트 사이 쉼)이 달라짐 → 전부 다시
    voices = load_voices(topic, vid, args, quiet=True)
    if any(o.get("role") != role_of(p, voices) for o, p in zip(old, news)):
        return None, "파트 이름이 바뀌어 읽는 목소리(역할)가 달라짐"
    renamed = list(dict.fromkeys((a, b) for a, b in zip(olds, news) if a != b))
    if renamed:                                          # v1.10: 라벨 글자만 바뀜 — 소리로 읽지 않으므로 막지 않음
        log("PATCH", video=vid, note="파트 이름만 바뀜 (경계·목소리 같음) — 부분 다시 만들기 가능",
            renamed=" · ".join(f"{a} → {b}" for a, b in renamed))
    if any(not isinstance(o.get("start"), (int, float)) or not isinstance(o.get("end"), (int, float)) for o in old):
        return None, "메타에 문장 시각 없음"
    g = meta.get("gaps") or {}
    if g.get("cards", []) != [{"after": c["after"], "seconds": c["seconds"]} for c in cards]:
        return None, "고지 카드가 바뀜"
    if (g.get("lead_in"), g.get("part"), g.get("tail")) != (args.lead_in, args.part_gap, args.tail):
        return None, "쉼 설정(--lead-in·--part-gap·--tail)이 다름"
    if any((meta.get("voices") or {}).get(r, {}).get("gap") != v["gap"] for r, v in voices.items()):
        return None, "문장 쉼(gap) 설정이 다름"
    changed = [i + 1 for i, (o, (t, _)) in enumerate(zip(old, rows)) if o.get("text") != t]
    if not changed:
        return None, "글은 같음 (해시만 다름)"
    limit = max(1, int(len(rows) * PATCH_MAX_FRAC))
    if len(changed) > limit:
        return None, f"바뀐 문장 {len(changed)}개 > {limit}개 ({PATCH_MAX_FRAC:.0%})"
    return changed, None


def decode_audio(path, sr):
    """오디오 파일 → float32 단일 채널 (sr 로). ffmpeg 가 없거나 실패하면 None."""
    ff = find_ffmpeg()
    if not ff:
        return None
    r = subprocess.run([ff, "-hide_banner", "-loglevel", "error", "-i", str(path), "-f", "s16le", "-acodec", "pcm_s16le",
                        "-ac", "1", "-ar", str(sr), "-"], capture_output=True)
    if r.returncode != 0 or not r.stdout:
        log("PATCH", logging.WARNING, error=r.stderr.decode("utf-8", "replace").strip()[:200], path=path)
        return None
    return np.frombuffer(r.stdout, dtype="<i2").astype(np.float32) / 32767.0


def patch_report(old_text, vid, items, timing, total, new, base, voices):
    """옛 보고(tts_report.md)의 시작 시각을 새 시각으로, 다시 만든 문장 줄을 새 수치로 바꾸고 '부분 다시 만들기' 절을 붙인다."""
    now = datetime.now().isoformat(timespec="seconds")
    out = []
    for ln in old_text.splitlines():
        cells = [c.strip() for c in ln.split("|")[1:-1]] if ln.startswith("| ") else []
        if len(cells) == 9 and cells[0].isdigit() and int(cells[0]) in timing:
            n = int(cells[0])
            cells[3] = mmss(timing[n][0])
            if n in new:
                m = new[n]["meta"]
                flag = "; ".join(m["issues"] + m["warns"]) or "✅"
                if abs(m.get("pace_factor", 1.0) - 1) > 1e-3:
                    flag += f" · 속도 맞춤 ×{m['pace_factor']:.2f}"
                cells[1:3] = [voices[items[n - 1]["role"]]["name"], items[n - 1]["part"]]
                cells[4:9] = [f"{m['dur']:.2f}", f"{m['rate']:.1f}", f"{m.get('f0', 0):.0f}", str(m["attempt"]), flag + f" · 부분 다시 만듦 ({VERSION})"]
            ln = "| " + " | ".join(cells) + " |"
        elif ln.startswith("- 도구: "):
            ln = (f"- 도구: tools/tts_narration.py {VERSION} · 고친 시각 {now} — 바뀐 문장만 다시 만듦 "
                  f"(나머지는 {base.get('created', '-')} 에 {base.get('tool', '-')} 로 만든 오디오 그대로)")
        elif ln.startswith("- 길이 "):
            ln = re.sub(r"^- 길이 [0-9:.]+", f"- 길이 {mmss(total)}", ln)
        out.append(ln)
    sec = ["", f"## 부분 다시 만들기 ({VERSION} — {now[:10]})", "",
           "글이 바뀐 문장만 새로 만들어 저장소 오디오의 그 자리에 넣었다. 다른 문장은 소리·길이·쉼이 예전 그대로이고, "
           "뒤 문장의 시작 시각만 길이 차이만큼 밀린다. 새 문장 크기는 다른 문장들의 말소리 크기 중간값에 맞췄다.", "",
           "| 번호 | 예전 글 | 새 글 | 길이(초) 예전 → 새 | 맞춘 이득(dB) | 확인 |", "|---|---|---|---|---|---|"]
    for n, d in sorted(new.items()):
        m = d["meta"]
        sec.append(f"| {n} | {d['old_text']} | {items[n - 1]['text']} | {d['old_dur']:.2f} → {m['dur']:.2f} | {d['gain_db']:+.1f} | "
                   f"{'; '.join(m['issues'] + m['warns']) or '✅'} |")
    sec += ["", "귀로 확인: " + ", ".join(f"{n}번({mmss(timing[n][0])})" for n in sorted(new)) + " — 앞뒤 문장과 목소리·크기가 이어지는지.",
            "전부 다시 만들려면 `python tools/tts_narration.py all --full --push` (또는 build … --full).", ""]
    tail_at = next((i for i, ln in enumerate(out) if ln.startswith("다시 만들기: ")), len(out))
    return "\n".join(out[:tail_at] + sec + out[tail_at:]) + "\n"


def patch_episode(engine, topic, vid, args, P, rows, cards, items, voices, changed, txt):
    """저장소 narration.mp3 에서 바뀐 문장(changed)만 새로 만든 문장으로 바꿔 넣는다 → build_episode 와 같은 결과 dict.
    못 하면(디코드 실패·길이 불일치) None — 부르는 쪽이 전부 다시 만든다."""
    src = src_dir(topic, vid)
    base = json.loads((src / META_NAME).read_text("utf-8"))
    old_items = base["items"]
    t0 = time.time()
    log("PATCH", video=vid, mode="바뀐 문장만", changed=ranges(changed), of=len(items), base_created=base.get("created"),
        base_tool=base.get("tool"), note="나머지 문장은 저장소 오디오 그대로 (--full 이면 전부 다시)")
    new = {}
    for n in changed:
        it = items[n - 1]
        log("PATCH", video=vid, n=n, old_text=old_items[n - 1]["text"], new_text=it["text"])
        m = make_sentence(engine, P["cache"], f"S{n:03d}", it["tts"], it["spec"], it["syl"], args, role=it["role"])
        x, sr = read_wav(m["wav"])
        new[n] = {"meta": m, "x": x, "sr": sr, "old_text": old_items[n - 1]["text"],
                  "old_dur": old_items[n - 1]["end"] - old_items[n - 1]["start"]}
    srs = {d["sr"] for d in new.values()}
    if len(srs) != 1:
        log("PATCH", logging.WARNING, video=vid, note=f"새 문장 표본율이 여러 개 {sorted(srs)} → 전부 다시")
        return None
    sr = srs.pop()
    old = decode_audio(src / "narration.mp3", sr)
    if old is None:
        log("PATCH", logging.WARNING, video=vid, note="저장소 narration.mp3 를 읽지 못함 (ffmpeg) → 전부 다시")
        return None
    old_s = len(old) / sr
    if abs(old_s - float(base.get("seconds", 0))) > 0.15:
        log("PATCH", logging.WARNING, video=vid, mp3_seconds=old_s, meta_seconds=base.get("seconds"),
            note="저장소 오디오 길이가 메타와 다름 (메타와 다른 파일) → 전부 다시")
        return None
    se = [(int(round(o["start"] * sr)), int(round(o["end"] * sr))) for o in old_items]
    # 새 문장 크기: 바뀌지 않은 문장들의 말소리 크기(같은 역할) 중간값에 맞춘다 — 전부 만들 때의 '이득 하나'와 같은 크기가 되게
    for n, d in new.items():
        role = items[n - 1]["role"]
        ref_db = [voiced_rms_db(old[a:b], sr) for (a, b), it in zip(se, items) if it["n"] not in new and it["role"] == role]
        ref_db = [v for v in ref_db if v > -100] or [TARGET_RMS_DB]
        target, now_db = float(np.median(ref_db)), voiced_rms_db(d["x"], sr)
        peak = float(np.max(np.abs(d["x"])) or 1e-9)
        g_db = min(target - now_db, PEAK_DB - 20 * math.log10(peak))
        d["x"], d["gain_db"] = d["x"] * 10 ** (g_db / 20), g_db
        log("PATCH", video=vid, n=n, role=role, level_target_db=target, level_before_db=now_db, gain_db=g_db,
            level_after_db=voiced_rms_db(d["x"], sr), ref_sentences=len(ref_db))
    pieces, t, timing = [old[: se[0][0]]], se[0][0], {}
    for i, it in enumerate(items):
        n = it["n"]
        clip = new[n]["x"] if n in new else old[se[i][0]: se[i][1]]
        timing[n] = (t / sr, (t + len(clip)) / sr)
        pieces.append(clip)
        t += len(clip)
        last = i == len(items) - 1
        if last:                                     # 끝 쉼 = 메타의 tail (디지털 무음, 처음 만들 때와 같음)
            gap = silence(float(base["gaps"]["tail"]), sr)
        elif n in new or items[i + 1]["n"] in new:   # 바뀐 문장 옆 쉼은 같은 길이의 깨끗한 무음 (옛 문장의 mp3 잔향이 남지 않게)
            gap = np.zeros(se[i + 1][0] - se[i][1], np.float32)
        else:
            gap = old[se[i][1]: se[i + 1][0]]
        pieces.append(gap)
        t += len(gap)
    y = np.concatenate(pieces).astype(np.float32)
    total = len(y) / sr
    shift = {n: timing[n][0] - old_items[n - 1]["start"] for n in timing}
    moved = [n for n in timing if abs(shift[n]) > 1e-3]
    log("PATCH", video=vid, seconds_before=old_s, seconds_after=total, delta_s=total - old_s,
        unchanged_timing=len(items) - len(moved), moved_from=min(moved) if moved else "-",
        max_shift_s=max((abs(v) for v in shift.values()), default=0.0), gen_min=(time.time() - t0) / 60)
    out = export(y, sr, P["narration"], keep_wav=args.keep_wav)
    if Path(out).suffix != ".mp3":
        die("EXPORT", "mp3 를 만들지 못함 (WAV만 있음)", "ffmpeg 확인: pip install imageio-ffmpeg", video=vid)
    meta = dict(base)
    meta.update({"tool": f"tts_narration.py {VERSION}", "created": datetime.now().isoformat(timespec="seconds"),
                 "script": rel(txt), "script_sha1": script_sha(rows, cards), "sentences": len(items), "seconds": round(total, 2),
                 "voices": voices_meta(voices), "voice_ids": voice_ids(voices, engine),
                 "items": [{"n": it["n"], "role": it["role"], "part": it["part"], "text": it["text"],
                            "start": round(timing[it["n"]][0], 3), "end": round(timing[it["n"]][1], 3)} for it in items]})
    meta["voice_sha1"] = sha(meta["voices"])
    meta["patches"] = list(base.get("patches", [])) + [{
        "at": meta["created"], "tool": VERSION, "sentences": changed, "base_created": base.get("created"), "base_tool": base.get("tool"),
        "texts": {str(n): {"old": d["old_text"], "new": items[n - 1]["text"]} for n, d in new.items()},
        "gain_db": {str(n): round(d["gain_db"], 2) for n, d in new.items()}}]
    P["meta"].write_text(json.dumps(meta, ensure_ascii=False, indent=1), "utf-8")
    rep_old = src / REPORT_NAME
    rep_txt = rep_old.read_text("utf-8") if rep_old.is_file() else f"# 내레이션 보고 — {vid}\n\n- 도구: -\n"
    P["report"].write_text(patch_report(rep_txt, vid, items, timing, total, new, base, voices), "utf-8")
    flagged = [n for n, d in new.items() if not d["meta"]["ok"] or d["meta"]["warns"]]
    log("SUMMARY", video=vid, mode="patch", out=out, meta=P["meta"], minutes=total / 60, patched=ranges(changed),
        flagged=ranges(flagged) or "-", report=P["report"], next="Claude: align-audio → 영상 sync·다시 렌더")
    return {"video": vid, "topic": topic, "status": "made", "sentences": len(items), "minutes": total / 60,
            "flagged": flagged, "out": str(out), "patched": changed}


# ----------------------------------------------------------------------------- 영상 하나 (build·all 이 함께 씀)
def build_episode(engine, topic, vid, args, root, txt=None):
    """대본 → 역할별 문장 → narration.mp3 하나 + tts_narration.json + tts_report.md (+ 작업 폴더에 역할별 문장 파일). → 결과 dict."""
    src = src_dir(topic, vid)
    why = no_tts_reason(topic, vid)
    if why:   # v1.11·v1.12 안전장치 — all·build 가 먼저 거르지만 다른 길로 불려도 만들지 않음
        die("INPUT", f"{vid} — {why} — 오디오를 만들지 않음", "업로드한 영상·NO_TTS.md 가 있는 영상은 오디오를 만들지 않는다", folder=rel(src))
    txt = Path(txt) if txt else src / f"{vid}.txt"
    if not txt.is_file():
        die("INPUT", "대본 TXT 없음", "주제 폴더·영상ID 확인 (Kaggle: 저장소를 git clone·pull 했는지)", path=txt)
    rows, cards = read_script(txt)
    card_after = {c["after"]: c for c in cards}
    lex = load_lexicon([getattr(args, "lexicon", None), ROOT / topic / "tts_lexicon.tsv"]
                       + ([src.parent / "tts_lexicon.tsv"] if vid.endswith(SHORTS_SUFFIX) else []) + [src / "tts_lexicon.tsv"])   # v1.9 쇼츠는 롱폼 것도
    voices = load_voices(topic, vid, args)
    P = episode_paths(root, topic, vid)
    P["cache"].mkdir(parents=True, exist_ok=True)
    total_syl = sum(srt_tool.syllables(t) for t, _ in rows)
    log("INPUT", video=vid, txt=rel(txt), sentences=len(rows), cards=len(cards), syllables=total_syl,
        est_minutes=total_syl / 4.8 / 60, parts=" / ".join(dict.fromkeys(p for _, p in rows)), work=P["work"])
    for c in cards:
        if c["seconds"] < CARD_GAP_MIN:
            die("INPUT", f"고지 카드 쉼 {c['seconds']}초 < {CARD_GAP_MIN}초", "srt_tool.parse_cards 규칙 확인", after=c["after"])
        log("INPUT", video=vid, card_after_sentence=c["after"], card_title=c["title"], gap_s=c["seconds"])
    for role, v in voices.items():
        if v["engine"] == "clone" and not v.get("ref_sha"):
            die("VOICE", f"{role} 기준 목소리 없음 ({v['ref_audio']})", "all·build 가 먼저 만든다 — 또는 python tools/tts_narration.py voice --push",
                video=vid)
    items = plan_items(vid, rows, voices, lex)
    changed = [it["n"] for it in items if it["tts"] != it["text"]]
    log("INPUT", video=vid, tts_text_changed=",".join(map(str, changed)) or "-", note="부호 금액·사전 바꿈 (대본·자막은 그대로)")

    k, K = (int(v) for v in getattr(args, "shard", "0/1").split("/"))   # all 은 문장을 나누지 않는다(영상 단위 --split)
    redo = parse_nums(getattr(args, "redo", ""))
    if K == 1 and not redo and not getattr(args, "assemble_only", False):
        # v1.8: 글만 조금 바뀐 대본 → 바뀐 문장만 만들어 저장소 오디오에 끼운다 (다른 문장 소리·시각은 그대로, GPU 시간 절약)
        changed, why = patch_candidate(topic, vid, rows, cards, args)
        if changed:
            res = patch_episode(engine, topic, vid, args, P, rows, cards, items, voices, changed, txt)
            if res:
                return res
            why = "부분 다시 만들기 실패 (위 [PATCH] 경고)"
        log("PATCH", video=vid, mode="전부 만들기", why=why)
    targets = [it for it in items if (it["n"] - 1) % K == k]
    metas = {}
    if not getattr(args, "assemble_only", False):
        # 엔진별로 모아서 만든다 (GPU 하나면 모델을 한 번만 바꿔 올리게: 사연자 → 진행자)
        targets = sorted(targets, key=lambda it: (it["spec"]["engine"] != "custom_voice", it["n"]))
        t_start, done_syl, todo_syl = time.time(), 0, sum(it["syl"] for it in targets)
        for it in targets:
            m = make_sentence(engine, P["cache"], f"S{it['n']:03d}", it["tts"], it["spec"], it["syl"], args,
                              redo=it["n"] in redo, role=it["role"])
            metas[it["n"]] = m
            done_syl += it["syl"]
            if not m["cached"]:
                el = time.time() - t_start
                log("PROGRESS", video=vid, n=it["n"], of=len(items), role=it["role"], elapsed_min=el / 60,
                    eta_min=el / max(done_syl, 1) * (todo_syl - done_syl) / 60)
        if K > 1:
            log("SHARD", video=vid, shard=args.shard, made=len(targets), note="다른 조각도 끝나면 --assemble-only 로 잇기")
            return {"video": vid, "topic": topic, "status": "shard", "sentences": len(items)}
    else:   # --assemble-only
        missing = []
        for it in items:
            hit = cached_sentence(engine, P["cache"], it["tts"], it["spec"])
            if hit:
                metas[it["n"]] = hit
            else:
                missing.append(it["n"])
        if missing:
            die("ASSEMBLE", f"문장 파일 없음: {ranges(missing)}", "--assemble-only 없이 다시 실행(없는 문장만 만든다)", video=vid)

    # 잇기: 볼륨은 영상 전체에 이득 하나 → narration (역할 사이 볼륨 차이도 모델이 낸 그대로)
    sr, clips = None, []
    for it in items:
        x, s = read_wav(metas[it["n"]]["wav"])
        if sr is None:
            sr = s
        elif s != sr:
            die("ASSEMBLE", f"표본율이 다름 S{it['n']:03d} {s} ≠ {sr}", "같은 모델로 다시 만들기", video=vid)
        clips.append(x)
    g = 10 ** (gain_for(clips, sr) / 20)
    clips = [x * g for x in clips]
    pieces, t, timing, gaps = [silence(args.lead_in, sr)], args.lead_in, {}, {}
    gap_kinds = {"sentence": 0, "part": 0, "card": 0}
    for i, it in enumerate(items):
        x = clips[i]
        timing[it["n"]] = (t, t + len(x) / sr)
        pieces.append(x)
        t += len(x) / sr
        if i == len(items) - 1:
            gap, kind = args.tail, "tail"
        elif it["n"] in card_after:
            gap, kind = card_after[it["n"]]["seconds"], "card"
        elif items[i + 1]["part"] != it["part"]:
            gap, kind = args.part_gap, "part"
        else:
            gap, kind = it["spec"]["gap"], "sentence"
        if kind == "card":
            log("ASSEMBLE", video=vid, card_after_sentence=it["n"], gap_s=gap, at=mmss(t), rule=f">= {CARD_GAP_MIN}s")
        gaps[it["n"]] = gap
        gap_kinds[kind] = gap_kinds.get(kind, 0) + 1
        pieces.append(silence(gap, sr))
        t += gap
    y = np.concatenate(pieces)
    total = len(y) / sr
    log("ASSEMBLE", video=vid, sentences=len(items), seconds=total, minutes=total / 60, sr=sr,
        gaps=" ".join(f"{k2}={v}" for k2, v in gap_kinds.items()), part_gap_s=args.part_gap)
    out = export(y, sr, P["narration"], keep_wav=args.keep_wav)

    # 역할별 정해진 경로(작업 폴더): OUT/<영상ID>/<역할>/S###.wav — 볼륨 맞춘 문장 파일. 결과 오디오는 narration.mp3 하나뿐이다
    role_out = {}
    for role in voices:
        mine = [i for i, it in enumerate(items) if it["role"] == role]
        rdir = P["work"] / role
        if rdir.is_dir():   # 대본이 바뀌어 번호가 달라졌을 때 옛 문장 파일이 섞이지 않게
            for old in rdir.glob("S*.wav"):
                old.unlink()
        if not mine:
            continue
        rdir.mkdir(parents=True, exist_ok=True)
        for i in mine:
            write_wav(rdir / f"S{items[i]['n']:03d}.wav", clips[i], sr)
        role_out[role] = {"dir": str(rdir), "sentences": len(mine), "range": ranges([items[i]["n"] for i in mine])}
        log("ROLE", video=vid, role=role, name=voices[role]["name"], files=f"{rdir}/S###.wav", count=len(mine),
            range=role_out[role]["range"])

    meta = {"tool": f"tts_narration.py {VERSION}", "created": datetime.now().isoformat(timespec="seconds"),
            "topic": topic, "id": vid, "script": rel(txt), "script_sha1": script_sha(rows, cards),
            "sentences": len(items), "seconds": round(total, 2), "engine": engine.describe(items[0]["spec"]) if engine else
            {k: metas[items[0]["n"]].get(k) for k in ("engine", "model", "language", "dtype")},
            "voices": voices_meta(voices),
            "voice_ids": voice_ids(voices, engine),
            "gaps": {"lead_in": args.lead_in, "part": args.part_gap, "tail": args.tail,
                     "cards": [{"after": c["after"], "seconds": c["seconds"]} for c in cards]},
            "items": [{"n": it["n"], "role": it["role"], "part": it["part"], "text": it["text"],
                       "start": round(timing[it["n"]][0], 3), "end": round(timing[it["n"]][1], 3)} for it in items]}
    meta["voice_sha1"] = sha(meta["voices"])
    P["meta"].write_text(json.dumps(meta, ensure_ascii=False, indent=1), "utf-8")
    write_report(P["report"], topic, vid, args, items, metas, timing, cards, total, voices, role_out, out)
    flagged = [it["n"] for it in items if not metas[it["n"]]["ok"] or metas[it["n"]]["warns"]]
    log("SUMMARY", video=vid, out=out, meta=P["meta"], minutes=total / 60, flagged=ranges(flagged) or "-", report=P["report"])
    if Path(out).suffix != ".mp3":
        die("EXPORT", "mp3 를 만들지 못함 (WAV만 있음)", "ffmpeg 확인: pip install imageio-ffmpeg 후 --assemble-only", video=vid)
    return {"video": vid, "topic": topic, "status": "made", "sentences": len(items), "minutes": total / 60,
            "flagged": flagged, "out": str(out)}


def write_report(path, topic, vid, args, items, metas, timing, cards, total_s, voices, role_out, out):
    m0 = metas[items[0]["n"]]
    lines = [f"# 내레이션 보고 — {vid}", "",
             f"- 도구: tools/tts_narration.py {VERSION} · 만든 시각 {datetime.now().isoformat(timespec='seconds')}",
             f"- 모델: {m0.get('model')} · {m0.get('dtype')}",
             f"- 길이 {mmss(total_s)} · 문장 {len(items)}개 · 파트 쉼 {args.part_gap}초 · 고지 카드 "
             + (", ".join(f"문장 {c['after']} 뒤 {c['seconds']}초" for c in cards) or "없음"),
             f"- 결과 오디오(하나): 저장소 `{topic}/source/{vid}/narration.mp3` (옆에 `{META_NAME}`, 이 보고 `{REPORT_NAME}`)", "",
             "## 역할 (목소리 설정)", "", "| 역할 | 문장 | 화자 | 문장 쉼 | 시드 | 설정 파일 | 문장 파일 (Kaggle 작업 폴더) |", "|---|---|---|---|---|---|---|"]
    for role, v in voices.items():
        ro = role_out.get(role, {})
        lines.append(f"| {v['name']} (`{role}`) | {ro.get('range', '-')} ({ro.get('sentences', 0)}개) | {v['speaker']} | {v['gap']}초 | "
                     f"{v['seed']} | {', '.join(f'`{f}`' for f in v['files'])} | `{ro.get('dir', '-')}/S###.wav` |")
    lines += ["", "## 말투 지시", ""]
    for style, ins in dict.fromkeys((it["style"], it["spec"]["instruct"]) for it in items):
        lines.append(f"- **{style}**: {ins}")
    for role, v in voices.items():
        if v["engine"] == "clone":
            lines.append(f"- **{v['name']} 기준 목소리**: `{v['ref_audio']}` (높이 {v['ref_f0']:.0f}Hz, 해시 {v['ref_sha']}) — "
                         f"모든 대본에서 같은 파일을 복제. 문장 높이가 ±{v['f0_tolerance']:.0%} 넘게 벗어나면 다시 만듦")
    lines += ["", "## 문장", "", "| 번호 | 역할 | 파트 | 시작 | 길이(초) | 음절/초 | 높이(Hz) | 시도 | 확인 |", "|---|---|---|---|---|---|---|---|---|"]
    for it in items:
        m = metas[it["n"]]
        flag = "; ".join(m["issues"] + m["warns"]) or "✅"
        if abs(m.get("pace_factor", 1.0) - 1) > 1e-3:
            flag += f" · 속도 맞춤 ×{m['pace_factor']:.2f}"
        lines.append(f"| {it['n']} | {voices[it['role']]['name']} | {it['part']} | {mmss(timing[it['n']][0])} | {m['dur']:.2f} | "
                     f"{m['rate']:.1f} | {m.get('f0', 0):.0f} | {m['attempt']} | {flag} |")
    bad = [it for it in items if not metas[it["n"]]["ok"] or metas[it["n"]]["warns"]]
    lines += ["", "## 귀로 확인할 문장", ""]
    lines += [f"- {it['n']}번 ({mmss(timing[it['n']][0])}, {voices[it['role']]['name']}): {it['text']} — "
              f"{'; '.join(metas[it['n']]['issues'] + metas[it['n']]['warns'])}" for it in bad] or ["- 없음 (그래도 사연 파트는 한 번 들어 보기)"]
    lines += ["", "다시 만들기: `python tools/tts_narration.py build <주제> <영상ID> --redo 12,15 --push` (새 시드로 그 문장만, 같은 Kaggle 세션 안에서)", ""]
    Path(path).write_text("\n".join(lines), "utf-8")


# ----------------------------------------------------------------------------- 명령: build (영상 하나)
def cmd_build(args):
    root = out_root(args)
    why = no_tts_reason(args.topic, args.id)
    if why:   # v1.11 업로드 · v1.12 NO_TTS.md — 오디오를 만들지 않음 (all 과 같음)
        die("PLAN", f"{args.id} — {why} — 오디오를 만들지 않음",
            "업로드한 영상·NO_TTS.md 가 있는 영상은 오디오를 만들지 않는다 (사용자 지시 2026-10-19). 새 영상이면 새 영상ID 폴더로",
            folder=rel(src_dir(args.topic, args.id)))
    unpicked = unpicked_roles(load_voices(quiet=True))
    if unpicked:
        die("VOICE", f"목소리를 아직 고르지 않음: {','.join(unpicked)}",
            "먼저 샘플을 듣고 고르기: Kaggle all --push(또는 samples --push) → voices/samples/README.md → Claude 가 pick")
    token = push_preflight(args)
    voices = load_voices(args.topic, args.id, args)
    engine = make_engine(args)
    if not args.assemble_only:
        ensure_reference(engine, voices, args, token)
        engine.check_speakers({v["speaker"] for v in voices.values() if v["engine"] == "custom_voice"})
    res = build_episode(engine, args.topic, args.id, args, root, txt=args.txt)
    if res["status"] != "made":
        return
    if args.push:
        if not push_results(root, [(args.topic, args.id)], token, args):
            raise SystemExit(1)
    else:
        log("NEXT", note=f"올리려면 같은 명령에 --push (또는 python tools/tts_narration.py push) → 저장소 {args.topic}/source/{args.id}/")


# ----------------------------------------------------------------------------- 명령: all (저장소의 대본 전부)
def topic_on_hold(topic):
    """주제 README 앞부분에 '⏸ … 보류' 표시가 있으면 보류 (사용자 지시 2026-10-10: 분석 결과 없는 주제는 진행하지 않음)."""
    p = ROOT / topic / "README.md"
    if not p.is_file():
        return False
    head = "\n".join(p.read_text("utf-8").splitlines()[:30])
    return any("⏸" in ln and "보류" in ln for ln in head.splitlines())


NO_TTS_NAME = "NO_TTS.md"   # v1.12: 대본 폴더에 이 파일이 있으면 그 영상은 오디오를 만들지 않음 (첫 줄 = 까닭)


def uploaded_record(topic, vid):
    """v1.11: 업로드한 영상이면 그 기록(youtube.json) 경로, 아니면 None — 업로드한 영상은 오디오를 만들지도 올리지도 않는다."""
    p = src_dir(topic, vid) / "youtube.json"
    return p if p.is_file() else None


def no_tts_reason(topic, vid):
    """v1.12: 오디오를 만들지 않는 영상이면 까닭 문자열, 아니면 None — 업로드(youtube.json) 또는 표시 파일 NO_TTS.md."""
    if uploaded_record(topic, vid):
        return "이미 업로드(youtube.json)"
    m = src_dir(topic, vid) / NO_TTS_NAME
    if m.is_file():
        first = next((ln.strip("# ").strip() for ln in m.read_text("utf-8").splitlines() if ln.strip()), "")
        return f"오디오 만들지 않음({NO_TTS_NAME}: {first[:80] or '까닭 없음'})"
    return None


def repo_status(topic, vid, rows, cards):
    """저장소 상태 → (상태, 메모). made 여부는 따로 본다."""
    src = src_dir(topic, vid)
    if uploaded_record(topic, vid):
        return "uploaded", "이미 업로드(youtube.json)"
    why = no_tts_reason(topic, vid)
    if why:                                   # v1.12: NO_TTS.md
        return "no_tts", why
    audio = repo_audio(topic, vid)
    if not audio:
        return "todo", "오디오 없음"
    meta_p = src / META_NAME
    if not meta_p.is_file():
        return "has_audio", f"{audio.name} 있음 (직접 녹음 또는 v1.0 — 대본과 같은지 알 수 없음)"
    meta = json.loads(meta_p.read_text("utf-8"))
    if meta.get("script_sha1") != script_sha(rows, cards):
        return "stale", f"{audio.name} 이 옛 대본으로 만든 것 (바뀐 문장: check 명령)"
    bad = voice_mismatch(meta, topic, vid)
    if bad:
        return "stale", f"{audio.name} 이 다른 목소리로 만든 것 ({','.join(bad)}) — 모든 대본을 같은 목소리로"
    return "has_audio", f"{audio.name} 있음 (지금 대본·목소리와 같음)"


def voice_mismatch(meta, topic, vid):
    """메타의 목소리 정체와 지금 설정이 다른 역할 목록 (v1.2 이하 메타는 목소리 정체가 없어 모두 다름)."""
    now = voice_ids(load_voices(topic, vid, quiet=True), None)
    old = meta.get("voice_ids") or {}
    return [r for r in now if old.get(r) != now[r]]


def discover(args, root):
    """저장소의 대본 TXT(<주제>/source/<영상ID>/<영상ID>.txt)를 모두 읽어 할 일을 정한다."""
    want_topics = {t.strip() for t in (args.topics or "").split(",") if t.strip()}
    want_ids = {t.strip() for t in (args.ids or "").split(",") if t.strip()}
    plan = []
    for topic, vid, txt in script_entries():                  # v1.9 롱폼 + 쇼츠
        if (want_topics and topic not in want_topics) or (want_ids and vid not in want_ids):
            continue
        rows, cards = read_script(txt)
        st, note = repo_status(topic, vid, rows, cards)
        hold = topic_on_hold(topic)
        P = episode_paths(root, topic, vid)
        made = False
        if P["meta"].is_file() and P["narration"].is_file():
            om = json.loads(P["meta"].read_text("utf-8"))
            made = om.get("script_sha1") == script_sha(rows, cards) and not voice_mismatch(om, topic, vid)
        if hold and not args.include_hold:
            action, why = "skip", "주제 보류(⏸ README) — --include-hold 로 포함"
        elif st in ("uploaded", "no_tts"):     # v1.12: --force 여도 만들지 않음
            action, why = "skip", note
        elif st == "has_audio" and not args.force:
            action, why = "skip", note + " — 다시 만들려면 --force"
        elif st == "stale" and args.keep_stale:
            action, why = "skip", note + " — --keep-stale 이라 그대로 둠"
        elif made and not args.force:
            action, why = "done", f"이번 결과 폴더에 이미 만듦 ({rel(P['narration']) if str(P['narration']).startswith(str(ROOT)) else P['narration']})"
        else:
            action, why = "make", note + (" → 지금 대본으로 다시 만듦" if st == "stale" else "")
        syl = sum(srt_tool.syllables(t) for t, _ in rows)
        patch = None
        if action == "make" and st == "stale":   # v1.8: 글만 조금 바뀌었으면 그 문장만
            patch, pwhy = patch_candidate(topic, vid, rows, cards, args)
            why += (f" — 바뀐 문장 {ranges(patch)}만 다시 (나머지는 저장소 오디오 그대로)" if patch else f" — 전부 다시 ({pwhy})")
            if patch:
                syl = sum(srt_tool.syllables(rows[n - 1][0]) for n in patch)
        plan.append({"topic": topic, "video": vid, "action": action, "status": st, "why": why, "sentences": len(rows),
                     "est_min": syl / 4.8 / 60, "hold": hold, "patch": patch})
        lvl = logging.WARNING if st == "stale" else logging.INFO
        log("PLAN", level=lvl, video=vid, topic=topic, action=action, status=st, sentences=len(rows),
            mode=("patch " + ranges(patch)) if patch else ("full" if action == "make" else "-"), est_audio_min=syl / 4.8 / 60, why=why)
    return plan


def cmd_all(args):
    root = out_root(args)
    k, K = (int(v) for v in args.split.split("/"))
    if K > 1 and any(v["engine"] == "clone" for v in load_voices(quiet=True).values()):
        die("START", "--split 은 쓰지 않음 (진행자 복제 모델이 있으면 한 프로세스가 GPU 2개를 나눠 씀: 사연자 GPU 0, 진행자 GPU 1)",
            "--split 없이 실행")
    plan = discover(args, root)
    todo = [p for p in plan if p["action"] == "make"]
    mine = [p for i, p in enumerate(todo) if i % K == k][: args.max or None]
    log("PLAN", scripts=len(plan), make=len(todo), this_process=len(mine), split=args.split, max=args.max or "-",
        out=root, list=",".join(p["video"] for p in mine) or "-",
        est_audio_min=sum(p["est_min"] for p in mine))
    done = [p for i, p in enumerate([p for p in plan if p["action"] == "done"]) if i % K == k]
    base_voices = load_voices(quiet=True)
    for role, v in base_voices.items():
        if v["engine"] == "clone":
            log("PLAN", role=role, reference=v["ref_audio"] if v["ref_sha"] else "없음",
                note=f"모든 대본이 이 기준 목소리 (높이 {v['ref_f0']}Hz)" if v["ref_sha"] else "처음 실행 때 한 번 만들어(VoiceDesign) voices/ref/ 에 올린 뒤 모든 대본이 복제")
    unpicked = unpicked_roles(base_voices)
    if unpicked:   # 사용자 지시 2026-10-12: 목소리 샘플을 듣고 고르기 전에는 오디오를 만들지 않는다
        log("PLAN", logging.WARNING, unpicked=",".join(unpicked),
            note="목소리를 아직 고르지 않음 → 이번에는 오디오 대신 목소리 후보 샘플만 만든다 (voices/samples/). 고른 뒤 같은 셀을 다시")
        token = "" if args.dry_run else push_preflight(args)
        if not run_samples(args, token, base_voices):
            raise SystemExit(1)
        return
    if args.dry_run:
        return
    token = push_preflight(args)
    pushed_ok = True
    if args.push and done:   # 이번 결과 폴더에 만들어 두고 아직 저장소에 없는 영상 → 다시 만들지 않고 올리기만
        log("PUSH", note="만들어 두고 못 올린 영상부터 올림", list=",".join(p["video"] for p in done))
        pushed_ok = push_results(root, [(p["topic"], p["video"]) for p in done], token, args)
    if not mine:
        log("PLAN", note="만들 영상 없음 (오디오가 없고 보류·업로드가 아닌 대본이 없음)")
        if not pushed_ok:
            raise SystemExit(1)
        return
    speakers, any_voices = set(), None
    for p in mine:
        vv = load_voices(p["topic"], p["video"], args, quiet=True)
        any_voices = any_voices or vv
        speakers |= {v["speaker"] for v in vv.values() if v["engine"] == "custom_voice"}
    engine = make_engine(args)
    ensure_reference(engine, any_voices, args, token)   # 진행자 기준 목소리 (없으면 한 번 만들어 저장소에 올림)
    engine.check_speakers(speakers)
    results, t0 = [], time.time()
    for i, p in enumerate(mine, 1):
        log("BATCH", n=i, of=len(mine), video=p["video"], topic=p["topic"], elapsed_min=(time.time() - t0) / 60)
        try:
            res = build_episode(engine, p["topic"], p["video"], args, root)
            if args.push:   # 영상 하나가 끝날 때마다 바로 올린다 (세션이 끊겨도 끝난 영상은 저장소에 남게)
                try:
                    res["pushed"] = push_results(root, [(p["topic"], p["video"])], token, args)
                except Exception as e:   # 올리기 오류는 오디오 실패가 아니다 — 결과는 OUT/upload 에 남아 push 로 다시 올린다
                    res["pushed"] = False
                    log("PUSH", logging.ERROR, video=p["video"], error=_redact(f"{type(e).__name__}: {str(e)[:200]}", token),
                        hint="python tools/tts_narration.py push")
            results.append(res)
        except SystemExit:
            results.append({"video": p["video"], "topic": p["topic"], "status": "failed"})
            log("BATCH", logging.ERROR, video=p["video"], note="이 영상만 멈춤 — 위 [ERROR] 로그 확인, 다음 영상 계속")
        except Exception as e:   # GPU 메모리 부족 등: 이 영상만 실패로 남기고 다음 영상
            results.append({"video": p["video"], "topic": p["topic"], "status": "failed"})
            log("BATCH", logging.ERROR, video=p["video"], error=f"{type(e).__name__}: {str(e)[:200]}",
                hint="런타임 재시작 후 같은 명령 (만든 문장은 cache 에 남아 이어서 만든다)")
    for r in results:
        log("BATCH", video=r["video"], status=r["status"], minutes=r.get("minutes", 0.0),
            flagged=ranges(r.get("flagged", [])) or "-", pushed=r.get("pushed", "-"), out=r.get("out", "-"))
    failed = [r["video"] for r in results if r["status"] != "made"]
    not_pushed = [r["video"] for r in results if r["status"] == "made" and args.push and not r.get("pushed")]
    log("BATCH", done=len(results) - len(failed), failed=",".join(failed) or "-", not_pushed=",".join(not_pushed) or "-",
        total_min=(time.time() - t0) / 60)
    if args.push:
        if not not_pushed and not failed and pushed_ok:
            log("NEXT", note="영상마다 대본 폴더에 올라감 → Claude에게 '오디오 올렸어'")
        elif not not_pushed and pushed_ok:
            log("NEXT", logging.WARNING, note="만든 영상은 올라감. 실패한 영상은 위 [ERROR] 확인 뒤 같은 명령을 다시")
        else:
            log("NEXT", logging.WARNING, note="못 올린 영상: 토큰을 확인하고 python tools/tts_narration.py push (안 되면 pack 으로 zip)")
    elif K == 1 and not args.no_pack:
        pack(root)
    else:
        log("NEXT", note="다른 조각(--split)도 끝나면 python tools/tts_narration.py push (또는 pack)")
    if failed or not_pushed or not pushed_ok:
        raise SystemExit(1)


def pack(root):
    """OUT/upload/ 를 저장소 경로 그대로 zip 하나로. 압축을 풀어 저장소 최상위에 올리면 각 영상 폴더에 들어간다."""
    up = root / "upload"
    files = sorted(p for p in up.rglob("*") if p.is_file()) if up.is_dir() else []
    if not files:
        log("PACK", logging.WARNING, note="올릴 파일 없음", dir=up)
        return None
    zp = root / ZIP_NAME
    with zipfile.ZipFile(zp, "w") as z:
        for p in files:   # mp3 는 이미 압축돼 있어 그대로 넣는다(빠름), json 만 압축
            z.write(p, p.relative_to(up).as_posix(), compress_type=zipfile.ZIP_STORED if p.suffix == ".mp3" else zipfile.ZIP_DEFLATED)
    for p in files:
        log("PACK", file=p.relative_to(up).as_posix(), mb=p.stat().st_size / 1e6)
    log("PACK", zip=zp, files=len(files), mb=zp.stat().st_size / 1e6)
    log("NEXT", note=f"(--push 가 안 될 때만) {ZIP_NAME} 내려받기 → 압축 풀기 → GitHub 저장소 Add file → Upload files 에 "
                     "안의 폴더(stock 등)를 그대로 끌어 놓기 → Commit → Claude에게 '오디오 올렸어'")
    return zp


def cmd_pack(args):
    pack(out_root(args))



# ----------------------------------------------------------------------------- GitHub 올리기 (--push, push)
def get_token():
    """GitHub 토큰: 환경 변수 GITHUB_TOKEN → 없으면 Kaggle Secrets 의 GITHUB_TOKEN. 값은 어디에도 출력하지 않는다."""
    tok, src = os.environ.get(TOKEN_ENV, "").strip(), "env"
    if not tok:
        try:
            from kaggle_secrets import UserSecretsClient   # Kaggle 노트북 안에서만 있음
            tok, src = (UserSecretsClient().get_secret(TOKEN_ENV) or "").strip(), "kaggle_secrets"
        except Exception as e:   # 패키지 없음·비밀값 없음·노트북에 연결 안 됨 — 메시지에 값은 없다
            log("PUSH", logging.DEBUG, kaggle_secrets=type(e).__name__)
            tok = ""
    return tok, src


def _redact(text, token):
    return text.replace(token, "***") if token else text


class Git:
    """저장소(ROOT)에서 git 실행. 토큰은 GIT_ASKPASS 스크립트가 환경 변수에서 읽어 넘긴다 — 명령줄·원격 주소·설정 파일에 남지 않는다."""

    def __init__(self, token):
        self.token = token
        self.tmp = Path(tempfile.mkdtemp(prefix="tts_git_"))
        self.env = {**os.environ, "GIT_TERMINAL_PROMPT": "0"}
        if token:
            ask = self.tmp / "askpass.sh"
            ask.write_text('#!/bin/sh\ncase "$1" in\n  Username*) echo x-access-token ;;\n  *) printf "%s\\n" "$TTS_GIT_TOKEN" ;;\nesac\n')
            ask.chmod(0o700)
            self.env.update(GIT_ASKPASS=str(ask), TTS_GIT_TOKEN=token)

    def run(self, *argv, timeout=900):
        # core.fileMode=false: Kaggle 등에서 실행 권한(파일 모드)만 달라진 파일을 변경으로 보지 않게 (pull --rebase 가 멈추지 않게)
        cmd = ["git", "-C", str(ROOT), "-c", "credential.helper=", "-c", "core.fileMode=false",
               "-c", f"user.name={GIT_NAME}", "-c", f"user.email={GIT_EMAIL}", *argv]
        try:
            r = subprocess.run(cmd, capture_output=True, text=True, env=self.env, timeout=timeout)
        except subprocess.TimeoutExpired:
            return 124, f"시간 초과 {timeout}초"
        return r.returncode, _redact((r.stdout + r.stderr).strip(), self.token)

    def close(self):
        shutil.rmtree(self.tmp, ignore_errors=True)


def remote_url(g):
    rc, url = g.run("remote", "get-url", "origin")
    return url if rc == 0 else ""


def push_preflight(args):
    """--push 면 만들기 전에: 토큰이 있는지, 그 토큰으로 push 할 수 있는지 확인한다. 안 되면 GPU 시간을 쓰기 전에 멈춘다."""
    if not getattr(args, "push", False):
        return ""
    if not (ROOT / ".git").exists():
        die("PUSH", "저장소가 git clone 이 아님", "Kaggle 셀 1에서 git clone 한 폴더에서 실행", root=ROOT)
    token, src = get_token()
    g = Git(token)
    try:
        url = remote_url(g)
        if "@" in url.split("://")[-1].split("/")[0]:
            die("PUSH", "원격 주소에 계정 정보가 들어 있음", "git remote set-url origin https://github.com/yeomin1024/yeomin1024-ytb.git")
        github = "github.com" in url
        if getattr(args, "fake", False) and github:
            die("PUSH", "가짜 소리(--fake)는 GitHub에 올리지 않음", "--push 를 빼거나 시험용 저장소에서")
        if github and not token:
            die("PUSH", f"GitHub 토큰 없음 ({TOKEN_ENV})",
                "Kaggle 오른쪽 Add-ons → Secrets → GITHUB_TOKEN 추가 후 이 노트북에 연결(체크) — guides/tts_guide.md 2번. "
                "토큰을 셀·채팅에 붙여 넣지 않는다")
        # 권한만 본다: 없는 브랜치 이름으로 dry-run (main 이 앞서 있어도 fast-forward 문제로 실패하지 않게). 실제로 만들지는 않는다
        rc, out = g.run("push", "--dry-run", "origin", "HEAD:refs/heads/tts-push-check", timeout=120)
        if rc != 0:
            die("PUSH", f"push 권한 확인 실패: {' '.join(out.split())[:300]}",
                "토큰 만료·저장소 선택·Contents 읽기/쓰기 권한 확인 (guides/tts_guide.md 2번)", remote=url)
        log("PUSH", remote=url, token="있음(값은 표시하지 않음)" if token else "없음(로컬 원격)", token_source=src if token else "-",
            check="push --dry-run 통과")
        rc, dirty = g.run("status", "--porcelain", "--untracked-files=no")
        if rc == 0 and dirty.strip():   # 이 사본에서 바뀐 다른 파일 — 올리지 않는다 (결과 3개만 커밋)
            log("PUSH", logging.WARNING, local_changes=" ".join(ln[3:] for ln in dirty.splitlines())[:300],
                note="이 사본의 다른 변경은 커밋하지 않음. 사본을 main 과 맞추려면: git fetch origin main && git reset --hard origin/main")
    finally:
        g.close()
    return token


def _lock():
    """GPU 2개(--split)로 두 프로세스가 동시에 올려도 git 작업이 겹치지 않게 잠근다 (Linux·macOS)."""
    try:
        import fcntl
    except ImportError:
        return None
    f = open(ROOT / ".git" / "tts_push.lock", "w")
    fcntl.flock(f, fcntl.LOCK_EX)
    return f


def push_results(root, entries, token, args):
    """영상마다 결과 세 파일을 대본 폴더 <주제>/source/<영상ID>/ 에 복사 → 그 파일만 커밋 → pull --rebase → push. → 성공 여부."""
    lock = _lock()
    g = Git(token)
    try:
        paths, vids = [], []
        for topic, vid in entries:
            P = episode_paths(root, topic, vid)
            dst = src_dir(topic, vid)
            if not (dst / f"{vid}.txt").is_file():
                log("PUSH", logging.WARNING, video=vid, note="저장소에 이 영상의 대본 폴더가 없음 — 건너뜀", dst=rel(dst))
                continue
            if not P["narration"].is_file() or not P["meta"].is_file():
                log("PUSH", logging.WARNING, video=vid, note="narration.mp3·메타 없음 — 건너뜀", src=P["upload"])
                continue
            nwhy = no_tts_reason(topic, vid)
            if nwhy:   # v1.11 업로드 · v1.12 NO_TTS.md — 오디오를 올리지 않음
                log("PUSH", logging.WARNING, video=vid, note=f"{nwhy} — 오디오를 올리지 않음", dst=rel(dst))
                continue
            new = json.loads(P["meta"].read_text("utf-8"))
            rows, cards = read_script(dst / f"{vid}.txt")
            if new.get("script_sha1") != script_sha(rows, cards):   # 지금 대본과 다른 옛 결과는 올리지 않는다
                log("PUSH", logging.WARNING, video=vid, note="이 결과는 옛 대본으로 만든 것 — 올리지 않음 (all 로 다시 만들기)")
                continue
            old_p = dst / META_NAME
            old = json.loads(old_p.read_text("utf-8")) if old_p.is_file() else {}
            if old.get("script_sha1") == new.get("script_sha1") and old.get("created", "") > new.get("created", ""):
                log("PUSH", logging.WARNING, video=vid, note="저장소에 더 나중에 만든 결과가 있음 — 덮어쓰지 않음",
                    repo_created=old.get("created"), this_created=new.get("created"))
                continue
            for name in REPO_FILES:
                if (P["upload"] / name).is_file():
                    shutil.copy2(P["upload"] / name, dst / name)
                    paths.append(rel(dst / name))
            for e in AUDIO_EXTS:   # 다른 확장자의 옛 내레이션이 있으면 지운다 (align-audio 가 mp3 를 먼저 쓰지만 헷갈리지 않게)
                old = dst / f"narration.{e}"
                if e != "mp3" and old.is_file():
                    rc, _ = g.run("rm", "-q", "--cached", "--ignore-unmatch", "--", rel(old))
                    old.unlink()
                    log("PUSH", video=vid, removed=rel(old), note="옛 내레이션 (다른 확장자)")
                    paths.append(rel(old))
            vids.append(vid)
            log("PUSH", video=vid, files=",".join(n for n in REPO_FILES if (P["upload"] / n).is_file()), dst=rel(dst),
                mb=P["narration"].stat().st_size / 1e6)
        if not vids:
            return False
        msg = (f"내레이션: {', '.join(vids)} (tts_narration {VERSION}, Kaggle)\n\n"
               f"자동 생성 — 대본 폴더마다 narration.mp3 · {META_NAME} · {REPORT_NAME}. 연구·교육용, 투자 권유 아님.")
        return commit_and_push(g, paths, msg, ",".join(vids),
                               "대본 폴더마다 올라감: " + ", ".join(f"{src_dir(t, v).relative_to(ROOT)}/" for t, v in entries if v in vids))
    finally:
        g.close()
        if lock:
            lock.close()


def commit_and_push(g, paths, msg, label, ok_note):
    """paths 만 커밋 → pull --rebase → push origin HEAD:main (최대 PUSH_TRIES 번). → 성공 여부."""
    rc, out = g.run("add", "-A", "--", *paths)
    if rc != 0:
        log("PUSH", logging.ERROR, step="add", error=" ".join(out.split())[:300])
        return False
    rc, _ = g.run("diff", "--cached", "--quiet", "--", *paths)
    if rc == 0:   # 새로 커밋할 것은 없다 — 전에 커밋만 하고 못 올린 것이 있을 수 있으니 아래 push 는 그대로 한다
        log("PUSH", items=label, note="새로 커밋할 변경 없음 — 못 올린 커밋이 있으면 올림")
    else:
        rc, out = g.run("commit", "-q", "-m", msg, "--", *paths)
        if rc != 0:
            log("PUSH", logging.ERROR, step="commit", error=" ".join(out.split())[:300])
            return False
    _, head = g.run("rev-parse", "--short", "HEAD")
    for attempt in range(1, PUSH_TRIES + 1):
        rc, out = g.run("pull", "-q", "--rebase", "--autostash", "origin", "main")
        if rc != 0:
            g.run("rebase", "--abort")
            log("PUSH", logging.WARNING, step="pull", attempt=attempt, error=" ".join(out.split())[:300])
        else:
            rc, out = g.run("push", "-q", "origin", "HEAD:main")
            if rc == 0:
                _, head = g.run("rev-parse", "--short", "HEAD")
                log("PUSH", items=label, commit=head, branch="main", ok=True, note=ok_note)
                return True
            log("PUSH", logging.WARNING, step="push", attempt=attempt, error=" ".join(out.split())[:300])
        time.sleep(2 ** attempt)
    log("PUSH", logging.ERROR, items=label, ok=False, commit=head,
        hint="커밋은 이 Kaggle 저장소에 남아 있음 → 잠시 뒤 python tools/tts_narration.py push, 안 되면 pack 으로 zip")
    return False


# ----------------------------------------------------------------------------- 기준 소리 고르기 (VoiceDesign·샘플 공통)
def design_best(engine, text, instruct, seed0, tries, f0_range, f0_target, label, gen=None):
    """시드를 바꿔 tries 번 만들고 검사(목소리 높이 범위·말 속도·문장 안 무음) → (가장 알맞은 것, 모든 시도).
    가장 알맞은 것 = 높이가 범위 안인 것 중 검사 통과 → 목표 높이·기준 속도에 가까운 순. 범위 안이 없으면 전체에서 고른다(in_range=False).
    gen(seed, max_new) 를 주면 VoiceDesign 대신 그 함수로 만든다(예: CustomVoice). 시도 = dict(x, sr, f0, m, seed, issues, in_range)."""
    lo, hi = f0_range
    center = float(f0_target if f0_target else (lo + hi) / 2)
    syl = srt_tool.syllables(text)
    max_new = int(FRAME_HZ * max(syl, 4) / 2.0) + 50
    cands = []
    for i in range(tries):
        seed = seed0 + i
        res = gen(seed, max_new) if gen else engine.design(text, instruct, seed, max_new)
        if res is None:
            continue
        x, sr = res
        x = trim(np.nan_to_num(x, nan=0.0, posinf=0.0, neginf=0.0), sr)
        _, issues, _, m = check(x, sr, syl, False)
        f0 = f0_median(x, sr) if x.size else 0.0
        in_range = lo <= f0 <= hi
        if not in_range:
            issues.append(f"높이 {f0:.0f}Hz (범위 {lo}~{hi}Hz 아님)")
        if not DESIGN_RATE[0] <= m["rate"] <= DESIGN_RATE[1]:
            issues.append(f"속도 {m['rate']:.1f}음절/초 ({DESIGN_RATE[0]}~{DESIGN_RATE[1]})")
        if m["inner_sil"] > DESIGN_MAX_SIL:
            issues.append(f"문장 안 무음 {m['inner_sil']:.1f}초")
        log("VOICE", item=label, attempt=i + 1, seed=seed, f0_hz=f0, rate=m["rate"], dur=m["dur"], inner_sil=m["inner_sil"],
            ok=not issues, issues=";".join(issues) or "-")
        score = (0 if not issues else 1, abs(f0 - center) / center + abs(math.log(max(m["rate"], 1e-3) / RATE_REF)))
        cands.append({"score": score, "in_range": in_range, "seed": seed, "x": x, "sr": sr, "f0": f0, "m": m, "issues": issues})
    pool = [c for c in cands if c["in_range"]] or cands
    best = min(pool, key=lambda c: c["score"]) if pool else None
    if best is not None and best["issues"]:
        log("VOICE", logging.WARNING, item=label, chosen_seed=best["seed"], issues=";".join(best["issues"]),
            note="모든 검사를 통과한 시도가 없어 가장 나은 것 — 귀로 확인")
    return best, cands


# ----------------------------------------------------------------------------- 진행자 기준 목소리 (처음 한 번)
def ensure_reference(engine, voices, args, token, force=False):
    """clone 역할의 기준 목소리가 저장소에 없으면(또는 force) VoiceDesign 으로 한 번 만들어 voices/ 에 저장하고 main 에 올린다.
    시드를 바꿔 몇 번 만들고, 목소리 높이(남성 중저음 범위)·말 속도·무음 검사를 통과한 것 중 가장 알맞은 것을 고른다.
    이 파일이 저장소에 있으면 어느 대본·어느 세션이든 같은 파일을 복제하므로 진행자 목소리가 달라지지 않는다."""
    for role, v in (voices or {}).items():
        if v["engine"] != "clone":
            continue
        ref, meta_p = ROOT / v["ref_audio"], ROOT / v["ref_meta"]
        if ref.is_file() and meta_p.is_file() and not force:
            log("VOICE", role=role, reference=v["ref_audio"], f0_hz=v["ref_f0"], sha=v["ref_sha"], note="저장소의 기준 목소리를 씀 (모든 대본 같은 목소리)")
            continue
        d = v.get("design") or {}
        lo, hi = d.get("f0_range", [85, 150])
        text, instruct, seed0, tries = d["text"], d["instruct"], int(d.get("seed", 2026)), int(d.get("tries", 6))
        log("VOICE", role=role, step="기준 목소리 만들기", model=engine.ids["design"], tries=tries, f0_range=f"{lo}-{hi}Hz",
            instruct=instruct, text=text)
        best, cands = design_best(engine, text, instruct, seed0, tries, (lo, hi), d.get("f0_target"), role)
        if best is None or not best["in_range"]:   # 범위 안 높이가 하나도 없으면 만들지 않는다 (엉뚱한 목소리로 고정되지 않게)
            die("VOICE", f"{tries}번 모두 목소리 높이가 {lo}~{hi}Hz 밖", "voices/host.json 의 design.seed 를 바꾸거나 tries 를 늘려 다시",
                f0s=",".join(f"{c['f0']:.0f}" for c in cands) or "-")
        seed, x, sr, f0, m = best["seed"], best["x"], best["sr"], best["f0"], best["m"]
        ref.parent.mkdir(parents=True, exist_ok=True)
        write_wav(ref, x, sr)
        meta = {"role": role, "text": text, "instruct": instruct, "language": args.language, "model": engine.ids["design"],
                "seed": seed, "f0_hz": round(f0, 1), "dur": round(m["dur"], 2), "rate": round(m["rate"], 2), "sr": sr,
                "sha1": hashlib.sha1(ref.read_bytes()).hexdigest()[:16], "created": datetime.now().isoformat(timespec="seconds"),
                "tool": f"tts_narration.py {VERSION}",
                "_설명": "진행자 기준 목소리 — 모든 대본의 진행자 문장이 이 소리를 복제한다. 손으로 바꾸지 않는다 (바꾸면 해시 검사에서 멈춤)."}
        meta_p.write_text(json.dumps(meta, ensure_ascii=False, indent=1) + "\n", "utf-8")
        engine.unload("design")
        attach_reference(v)
        log("VOICE", role=role, reference=rel(ref), f0_hz=f0, seed=seed, sha=v["ref_sha"], note="기준 목소리 만듦")
        if getattr(args, "push", False):
            g = Git(token)
            lock = _lock()
            try:
                ok = commit_and_push(g, [rel(ref), rel(meta_p)],
                                     f"진행자 기준 목소리 만듦: 남성 중저음 {f0:.0f}Hz (tts_narration {VERSION}, Kaggle VoiceDesign)\n\n"
                                     "모든 대본의 진행자 문장이 이 파일을 복제한다 (대본마다 같은 목소리).", rel(ref), "voices/ 에 올라감")
            finally:
                g.close()
                if lock:
                    lock.close()
            if not ok:   # 저장소에 없으면 다음 세션이 다른 목소리를 만들게 되므로, 올라가기 전에는 오디오를 만들지 않는다
                die("VOICE", "기준 목소리를 저장소에 올리지 못함", "토큰·네트워크 확인 후 같은 셀을 다시 (기준 목소리는 이 사본에 있음)")
        else:
            log("VOICE", logging.WARNING, note="--push 가 없어 기준 목소리가 이 사본에만 있음 — 저장소에 올려야 다음에도 같은 목소리")


def cmd_voice(args):
    """진행자 기준 목소리: 있으면 정보만, 없거나 --force 면 만들고(--push 면 올림)."""
    token = push_preflight(args)
    voices = load_voices(args=args)
    clones = {r: v for r, v in voices.items() if v["engine"] == "clone"}
    if not clones:
        log("VOICE", note="clone 역할 없음 — 기준 목소리가 필요 없음")
        return
    have = all((ROOT / v["ref_audio"]).is_file() for v in clones.values())
    if have and not args.force:
        for r, v in clones.items():
            log("VOICE", role=r, reference=v["ref_audio"], f0_hz=v["ref_f0"], sha=v["ref_sha"], note="이미 있음 — 모든 대본이 이 목소리")
        return
    ensure_reference(make_engine(args), voices, args, token, force=args.force)


def cmd_push(args):
    """OUT/upload/ 에 만들어 둔 결과를 대본 폴더마다 올린다 (all·build 의 --push 가 실패했을 때, --split 뒤)."""
    root = out_root(args)
    args.push = True
    token = push_preflight(args)
    entries = sorted({(p.parents[1].name, p.name) for p in (root / "upload").glob("*/source/*") if (p / "narration.mp3").is_file()}
                     | {(p.parents[2].name, p.parent.name + SHORTS_SUFFIX) for p in (root / "upload").glob("*/source/*/shorts")
                        if (p / "narration.mp3").is_file()})   # v1.9 쇼츠
    if not entries:
        log("PUSH", logging.WARNING, note="올릴 결과 없음", dir=root / "upload")
        return
    if not push_results(root, entries, token, args):
        raise SystemExit(1)


# ----------------------------------------------------------------------------- 목소리 고르기: samples · pick (사용자 지시 2026-10-12)
def load_samples_cfg(voices):
    """voices/samples/samples.json 읽기·검사 → dict. 역할마다 후보 목록과 같은 문장(text.<역할>.ref·preview)."""
    if not SAMPLES_CFG.is_file():
        die("SAMPLES", "후보 설정 없음", "저장소를 git pull 했는지 (voices/samples/samples.json)", file=rel(SAMPLES_CFG))
    try:
        cfg = json.loads(SAMPLES_CFG.read_text("utf-8-sig"))
    except json.JSONDecodeError as e:
        die("SAMPLES", f"JSON 오류: {e}", "쉼표·따옴표·괄호 확인", file=rel(SAMPLES_CFG))
    seen = set()
    for role in voices:
        t = (cfg.get("text") or {}).get(role) or {}
        if not t.get("ref") or not t.get("preview"):
            die("SAMPLES", f"{role}: text.{role}.ref·preview 가 없음", "samples.json 의 text 채우기")
        if not cfg.get(role):
            die("SAMPLES", f"{role}: 후보가 없음", f"samples.json 에 \"{role}\": [ … ]")
        for c in cfg[role]:
            if c.get("id") in seen or not c.get("id"):
                die("SAMPLES", f"후보 id 가 비었거나 겹침: {c.get('id')}", "S01·H01 처럼 하나씩 다르게")
            seen.add(c["id"])
            if c.get("how") not in SAMPLE_HOW:
                die("SAMPLES", f"{c['id']}: how 는 {'/'.join(SAMPLE_HOW)}", "samples.json 확인")
            if c["how"] == "custom_voice" and not (c.get("speaker") and c.get("instruct")):
                die("SAMPLES", f"{c['id']}: custom_voice 는 speaker·instruct 필요", "samples.json 확인")
            if c["how"] == "design" and not (c.get("instruct") and c.get("f0_range")):
                die("SAMPLES", f"{c['id']}: design 은 instruct·f0_range 필요", "samples.json 확인")
            if c.get("text") is not None and not (c["text"].get("ref") and c["text"].get("preview")):   # v1.13
                die("SAMPLES", f"{c['id']}: 후보 text 에는 ref·preview 가 모두 필요", "samples.json 확인")
    return cfg


def stext(cfg, role, c):
    """v1.13 후보가 읽는 문장 {ref, preview} — 후보에 text 가 있으면 그것, 없으면 역할 공통 text.<역할>."""
    return c.get("text") or cfg["text"][role]


def find_sample(cfg, voices, sid):
    for role in voices:
        for c in cfg.get(role, []):
            if c["id"].lower() == str(sid).lower():
                return role, c
    die("PICK", f"없는 후보: {sid}", "voices/samples/README.md 의 ID (예: S04, H01)")


def sample_paths(role, sid, base=None):
    d = (base or SAMPLES_DIR) / role
    return {"dir": d, "mp3": d / f"{sid}.mp3", "ref": d / f"{sid}_ref.wav", "meta": d / f"{sid}.json"}


def sample_ident(role, c, cfg, voices):
    """후보 하나의 정체 — 후보 설정·문장·모델·(current 면 지금 목소리 정체)가 바뀌면 샘플을 다시 만든다."""
    ident = {"role": role, "c": {k: v for k, v in c.items() if k != "label"}, "text": stext(cfg, role, c),
             "models": engine_ids(None), "cache": CACHE_VERSION}
    if c["how"] == "current":
        ident["current"] = voice_ids({role: voices[role]}, None)[role]
    return sha(ident)


def frozen_current(role, c, voices, meta):
    """current 후보 샘플은 '고르기 전 목소리'의 기록이다. 역할을 고른 뒤에는 설정이 바뀌어 정체가 달라져도
    그 샘플을 그대로 둔다 (다시 만들면 고른 목소리를 한 번 더 녹음할 뿐 — v1.6)."""
    return c["how"] == "current" and bool(voices[role].get("picked")) and bool(meta)


def samples_status(cfg, voices):
    """→ [(역할, 후보, 정체, 저장소에 이 정체의 샘플이 있는지)]"""
    out = []
    for role in voices:
        for c in cfg[role]:
            P = sample_paths(role, c["id"])
            ident = sample_ident(role, c, cfg, voices)
            meta = json.loads(P["meta"].read_text("utf-8")) if P["meta"].is_file() else {}
            have = P["mp3"].is_file() and (meta.get("ident") == ident or frozen_current(role, c, voices, meta))
            out.append((role, c, ident, have))
    return out


def unpicked_roles(voices):
    return [r for r, v in voices.items() if not v.get("picked")]


def sample_spec(role, c, voices, ref):
    """후보로 미리 듣기 문장을 읽을 목소리 값 (spec_of 와 같은 모양). current 는 지금 설정 그대로."""
    if c["how"] == "current":
        v = voices[role]
        if v["engine"] == "clone" and not v.get("ref_sha"):
            return None
        return spec_of(v, v["instruct"] if v["engine"] == "custom_voice" else "")
    if c["how"] == "custom_voice":
        sp = {"engine": "custom_voice", "speaker": c["speaker"], "instruct": c["instruct"], "gen": {},
              "seed": int(c.get("seed", 1234)), "gap": float(c.get("gap", SAMPLE_GAP))}
        return dict(sp, pace=c["pace"]) if c.get("pace") else sp
    if not ref:
        return None
    sp = {"engine": "clone", "speaker": "-", "instruct": "", "gen": {}, "seed": int(c.get("seed", 1234)), "gap": float(c.get("gap", SAMPLE_GAP)),
          "ref_audio": str(ref["path"]), "ref_sha": ref["sha"], "ref_f0": ref["f0"], "ref_text": ref["text"], "f0_tol": F0_TOL}
    return dict(sp, pace=c["pace"]) if c.get("pace") else sp


def make_samples(engine, args, cfg, voices, todo):
    """후보마다: (design) 기준 소리 → 미리 듣기 문장 → mp3 하나 + 정보 json. 작업 폴더 OUT/samples/ 에 만들고,
    저장소(voices/samples/<역할>/)에 복사한다(--fake 이고 원격이 github.com 이면 복사하지 않음). → 저장소에 쓴 파일 목록"""
    work = out_root(args) / "samples"
    cache = work / "cache"
    cache.mkdir(parents=True, exist_ok=True)
    to_repo = not (args.fake and origin_is_github())
    refs, written, failed = {}, [], []
    # 1) design 후보의 기준 소리 먼저 (VoiceDesign 모델을 한 번 올려 모두 만든 뒤 내린다 — GPU 메모리)
    for role, c, ident, _ in todo:
        if c["how"] != "design":
            continue
        text = stext(cfg, role, c)["ref"]
        log("SAMPLES", role=role, id=c["id"], step="기준 소리", label=c["label"], f0_range=c["f0_range"], tries=int(c.get("tries", 3)))
        best, _ = design_best(engine, text, c["instruct"], int(c.get("seed", 2026)), int(c.get("tries", 3)), c["f0_range"],
                              c.get("f0_target"), c["id"])
        if best is None:
            failed.append(c["id"])
            log("SAMPLES", logging.ERROR, id=c["id"], error="기준 소리를 만들지 못함", hint="로그의 오류 확인 후 samples --only " + c["id"])
            continue
        wp = work / role / f"{c['id']}_ref.wav"
        wp.parent.mkdir(parents=True, exist_ok=True)
        write_wav(wp, best["x"], best["sr"])
        refs[c["id"]] = {"path": wp, "sha": hashlib.sha1(wp.read_bytes()).hexdigest()[:16], "f0": round(best["f0"], 1),
                         "text": text, "seed": best["seed"], "m": best["m"], "issues": best["issues"], "in_range": best["in_range"]}
    engine.unload("design")
    # 2) 미리 듣기: 같은 모델끼리 모아서 (CustomVoice → Base 복제)
    order = sorted(todo, key=lambda t: (t[1]["how"] == "design" or voices[t[0]]["engine"] == "clone" and t[1]["how"] == "current",
                                        t[1]["id"]))
    for role, c, ident, _ in order:
        if c["id"] in failed:
            continue
        spec = sample_spec(role, c, voices, refs.get(c["id"]))
        if spec is None:
            failed.append(c["id"])
            log("SAMPLES", logging.ERROR, id=c["id"], error="읽을 목소리가 없음 (current 인데 기준 소리 파일이 없음)",
                hint="python tools/tts_narration.py voice --push 로 기준 소리를 먼저")
            continue
        clips, metas, sr = [], [], None
        for j, text in enumerate(stext(cfg, role, c)["preview"], 1):
            m = make_sentence(engine, cache, f"{c['id']}/p{j}", tts_text(text, []), spec, srt_tool.syllables(text), args, role=role)
            x, s_ = read_wav(m["wav"])
            sr = sr or s_
            clips.append(x)
            metas.append(m)
        g = 10 ** (gain_for(clips, sr) / 20)
        pieces = [silence(0.3, sr)]
        for x in clips:
            pieces += [x * g, silence(spec["gap"], sr)]
        y = np.concatenate(pieces + [silence(0.4, sr)])
        mp3 = export(y, sr, work / role / f"{c['id']}.mp3")
        f0s = [m.get("f0", 0.0) for m in metas if m.get("f0")]
        ref = refs.get(c["id"])
        meta = {"id": c["id"], "role": role, "label": c["label"], "how": c["how"], "ident": ident,
                "speaker": spec.get("speaker"), "instruct": c.get("instruct") or spec.get("instruct", ""),
                "seed": spec["seed"], "preview": stext(cfg, role, c)["preview"], "seconds": round(len(y) / sr, 2),
                "f0_hz": round(float(np.median(f0s)), 1) if f0s else 0.0,
                "rate": round(float(np.mean([m["rate"] for m in metas])), 2), "pace": c.get("pace") or spec.get("pace"),
                "pace_factors": [m.get("pace_factor", 1.0) for m in metas],
                "issues": sorted({i for m in metas for i in m["issues"]} | set((ref or {}).get("issues", []))),
                "models": {k: v for k, v in engine.ids.items()}, "created": datetime.now().isoformat(timespec="seconds"),
                "tool": f"tts_narration.py {VERSION}"}
        if ref:
            meta["ref"] = {"audio": rel(sample_paths(role, c["id"])["ref"]), "text": ref["text"], "sha1": ref["sha"],
                           "f0_hz": ref["f0"], "seed": ref["seed"], "dur": round(ref["m"]["dur"], 2), "rate": round(ref["m"]["rate"], 2),
                           "in_range": ref["in_range"], "f0_range": c["f0_range"], "design_model": engine.ids["design"]}
        elif c["how"] == "current" and spec["engine"] == "clone":
            meta["ref"] = {"audio": spec["ref_audio"], "sha1": spec["ref_sha"], "f0_hz": spec["ref_f0"], "text": spec["ref_text"]}
        (work / role / f"{c['id']}.json").write_text(json.dumps(meta, ensure_ascii=False, indent=1) + "\n", "utf-8")
        log("SAMPLES", role=role, id=c["id"], how=c["how"], mp3=mp3, seconds=meta["seconds"], f0_hz=meta["f0_hz"], rate=meta["rate"],
            issues=";".join(meta["issues"]) or "-")
        if to_repo:
            P = sample_paths(role, c["id"])
            P["dir"].mkdir(parents=True, exist_ok=True)
            shutil.copy2(mp3, P["mp3"])
            (P["meta"]).write_text(json.dumps(meta, ensure_ascii=False, indent=1) + "\n", "utf-8")
            written += [P["mp3"], P["meta"]]
            if ref:
                shutil.copy2(ref["path"], P["ref"])
                written.append(P["ref"])
    if not to_repo:
        log("SAMPLES", logging.WARNING, out=work, note="--fake: 샘플을 저장소에 넣지 않음 (작업 폴더에만)")
    return written, failed


def write_samples_readme(cfg, voices):
    """voices/samples/README.md — 후보 표(듣기 링크·높이·속도·확인할 점). 사용자가 듣고 고르는 문서."""
    lines = ["# 목소리 후보 샘플 — 듣고 하나씩 고르기", "",
             f"자동 생성 — `tools/tts_narration.py samples` ({VERSION}). 후보 설정: `samples.json`. 고친 뒤에는 Kaggle 셀을 다시 돌리면 바뀐 후보만 다시 만든다.", "",
             "**고르는 법:** 아래 mp3를 듣고 Claude에게 \"사연자 S0?, 진행자 H0?\"라고 말한다 → Claude 가 "
             "`python tools/tts_narration.py pick S0? H0?` 로 고정하고 main 에 올린다 → Kaggle 셀을 다시 돌리면 그 목소리로 모든 대본의 오디오를 만든다.",
             "- **current(지금 목소리)** 를 고르면 그 역할은 아무것도 바뀌지 않는다. 다른 후보를 고른 뒤에는 '고르기 전 목소리' 기록으로 남는다 (다시 고를 수는 없음 — git 으로 되돌림).",
             "- 다른 후보를 고르면, 아직 올리지 않은 영상 중 그 역할 오디오가 이미 있는 것은 다음 Kaggle 실행 때 새 목소리로 다시 만든다 (모든 대본 같은 목소리). "
             "이미 유튜브에 올린 영상(youtube.json 있음 — 주식 4개)은 그대로 둔다.", ""]
    for role in voices:
        t = cfg["text"][role]
        own = {}                                                  # v1.13 후보별 문장 → 그 문장을 읽는 후보 ID 들
        for c in cfg[role]:
            if c.get("text"):
                own.setdefault(json.dumps(c["text"]["preview"], ensure_ascii=False), []).append(c["id"])
        lines += [f"## {voices[role]['name']} (`{role}`)", "", "읽는 문장 (따로 적지 않은 후보): " + " / ".join(f"\"{x}\"" for x in t["preview"]), ""]
        for k, ids in own.items():
            lines += [f"읽는 문장 ({'·'.join(ids)}): " + " / ".join(f"\"{x}\"" for x in json.loads(k)), ""]
        lines += [
                  "| ID | 목소리 | 방식 | 듣기 | 높이(Hz) | 속도(음절/초) | 확인할 점 |", "|---|---|---|---|---|---|---|"]
        for c in cfg[role]:
            P = sample_paths(role, c["id"])
            m = json.loads(P["meta"].read_text("utf-8")) if P["meta"].is_file() else None
            frozen = m is not None and m.get("ident") != sample_ident(role, c, cfg, voices) and frozen_current(role, c, voices, m)
            ok = m is not None and (m.get("ident") == sample_ident(role, c, cfg, voices) or frozen)
            listen = f"[{c['id']}.mp3]({role}/{c['id']}.mp3)" if (P["mp3"].is_file() and ok) else "⏳ 아직 없음"
            how = {"current": "고르기 전 목소리" if frozen else "지금 그대로", "custom_voice": f"화자 {c.get('speaker')}",
                   "design": "묘사 → 복제"}[c["how"]]
            picked = " ✅ 고름" if (voices[role].get("picked") or {}).get("id") == c["id"] else ""
            lines.append(f"| **{c['id']}**{picked} | {c['label']} | {how} | {listen} | {m['f0_hz'] if ok else '-'} | "
                         f"{m['rate'] if ok else '-'} | {'; '.join(m['issues']) if ok and m['issues'] else ('-' if ok else '')} |")
        lines.append("")
    lines += ["※ 높이·속도는 자동 측정값이다. 최종 판단은 귀로 한다. 연구·교육용 도구 — 영상 내용은 투자 권유가 아니다.", ""]
    out = SAMPLES_DIR / "README.md"
    out.write_text("\n".join(lines), "utf-8")
    return out


def run_samples(args, token, voices, only=None, force=False):
    """할 일 정하기 → 만들기 → README → (--push) 올리기. → 성공 여부."""
    cfg = load_samples_cfg(voices)
    st = samples_status(cfg, voices)
    only = {x.strip().lower() for x in (only or []) if x.strip()}
    todo = [t for t in st if (force or not t[3]) and (not only or t[1]["id"].lower() in only)]
    for role, c, ident, have in st:
        log("SAMPLES", role=role, id=c["id"], how=c["how"], label=c["label"],
            action="make" if any(t[1]["id"] == c["id"] for t in todo) else "skip", have=have)
    log("SAMPLES", candidates=len(st), make=len(todo), dir=rel(SAMPLES_DIR))
    if getattr(args, "dry_run", False):
        return True
    written, failed = [], []
    if todo:
        engine = make_engine(args)
        spk = {c["speaker"] for _, c, _, _ in todo if c["how"] == "custom_voice"}
        spk |= {voices[r]["speaker"] for r, c, _, _ in todo if c["how"] == "current" and voices[r]["engine"] == "custom_voice"}
        if spk:
            engine.check_speakers(spk)
        written, failed = make_samples(engine, args, cfg, voices, todo)
    if args.fake and origin_is_github():
        return not failed
    readme = write_samples_readme(cfg, voices)
    if getattr(args, "push", False) and (written or todo == []):
        g, lock = Git(token), _lock()
        try:
            ok = commit_and_push(g, [rel(p) for p in written] + [rel(readme)],
                                 f"목소리 후보 샘플 {len(written) // 2}개 (tts_narration {VERSION}, Kaggle)\n\n"
                                 "voices/samples/README.md 의 mp3 를 듣고 사연자·진행자를 하나씩 고른다 (pick).", "voices/samples",
                                 "voices/samples/ 에 올라감")
        finally:
            g.close()
            if lock:
                lock.close()
        if not ok:
            return False
    log("NEXT", note="voices/samples/README.md 의 샘플을 듣고 Claude에게 '사연자 S0?, 진행자 H0?' — 고르기 전에는 오디오를 만들지 않음",
        failed=",".join(failed) or "-")
    return not failed


def cmd_samples(args):
    token = push_preflight(args)
    voices = load_voices(args=args, quiet=True)
    ok = run_samples(args, token, voices, only=(args.only or "").split(","), force=args.force)
    if args.play and not args.dry_run:
        ids = [x for x in (args.only or "").split(",") if x.strip()] or [c["id"] for r in voices for c in load_samples_cfg(voices)[r]]
        listen(ids, args)
    if not ok:
        raise SystemExit(1)


def play(path, seconds=None):
    """터미널에서 바로 재생 → 쓴 방법. ffplay·afplay·mpv (wav 면 paplay·aplay도). 소리 장치가 없으면 시간 안에 끝내고 None."""
    for cmd in (["ffplay", "-nodisp", "-autoexit", "-loglevel", "error"], ["afplay"], ["mpv", "--no-video", "--really-quiet"],
                ["paplay"], ["aplay", "-q"]):
        if not shutil.which(cmd[0]) or (cmd[0] in ("paplay", "aplay") and not str(path).endswith(".wav")):
            continue
        t0 = time.time()
        try:
            r = subprocess.run(cmd + [str(path)], timeout=(seconds or 60) + 15, capture_output=True, text=True)
        except subprocess.TimeoutExpired:
            return None
        took, err = time.time() - t0, (r.stderr or "").lower()
        # ffplay 는 소리 장치가 없어도 종료 코드 0 으로 바로 끝난다 → 오류 문구·걸린 시간으로 실제 재생 여부를 판단
        dead = any(s in err for s in ("audio device", "audio open failed", "failed to open", "cannot find card", "connection refused"))
        if r.returncode == 0 and not dead and (not seconds or took >= seconds * 0.5):
            return cmd[0]
        log("LISTEN", logging.DEBUG, player=cmd[0], rc=r.returncode, took_s=round(took, 2), expect_s=seconds or "-",
            err=(r.stderr or "").strip().splitlines()[-1:] or "-")
    return None


def listen(items, args):
    """샘플 ID(S07)·역할 기준 소리(storyteller·host)·파일 경로를 찾아 바로 재생. 못 틀면 경로와 노트북용 한 줄을 알려 준다."""
    voices = load_voices(quiet=True)
    work = out_root(args) / "samples"
    for it in items:
        it = it.strip()
        path = Path(it) if Path(it).is_file() else None
        if path is None and it in voices and voices[it].get("ref_audio") and (ROOT / voices[it]["ref_audio"]).is_file():
            path = ROOT / voices[it]["ref_audio"]
        if path is None:
            for role in voices:
                for base in (SAMPLES_DIR, work):
                    q = base / role / f"{it.upper()}.mp3"
                    if q.is_file():
                        path = q
                        break
                if path:
                    break
        if path is None:
            log("LISTEN", logging.WARNING, item=it, note="파일 없음 — 먼저 samples --only " + it.upper())
            continue
        meta_p = path.with_suffix(".json")
        info = json.loads(meta_p.read_text("utf-8")) if meta_p.is_file() else {}
        x, sr = (read_wav(path) if path.suffix == ".wav" else (None, None))
        secs = info.get("seconds") or (len(x) / sr if x is not None else None)
        log("LISTEN", item=it, file=rel(path), label=info.get("label", "-"), seconds=secs or "-", f0_hz=info.get("f0_hz", "-"),
            rate=info.get("rate", "-"), pace_factors=info.get("pace_factors", "-"))
        how = play(path, secs)
        if how:
            log("LISTEN", item=it, played=how)
        else:
            log("LISTEN", logging.WARNING, item=it, file=str(path),
                note="이 환경에는 소리 장치가 없음 — Kaggle·Jupyter 셀: from IPython.display import Audio; Audio(\"" + str(path) + "\")")


def cmd_listen(args):
    listen(args.items, args)


def ref_meta_of(role, c, meta, today, note):
    """고른 묘사 후보의 기준 소리 메타 (voices/ref/<역할>.json 또는 영상 폴더 voices/ref/<역할>.json)."""
    return {"role": role, "text": meta["ref"]["text"], "instruct": c["instruct"], "language": "Korean",
            "model": meta["ref"].get("design_model"), "seed": meta["ref"]["seed"], "f0_hz": meta["ref"]["f0_hz"],
            "dur": meta["ref"]["dur"], "rate": meta["ref"]["rate"], "sha1": meta["ref"]["sha1"], "sample": c["id"],
            "label": c["label"], "picked": today, "created": meta["created"], "tool": f"tts_narration.py {VERSION}", "_설명": note}


def pick_own(args, chosen, cfg, voices, today):
    """v1.14 고른 후보를 --only-for 영상들에만 (공통 voices/<역할>.json·voices/ref/ 는 그대로).
    영상 폴더 voices/<역할>.json = {"own_voice": true, engine·기준 소리·시드·속도·쉼·picked} — load_voices 가 lock 을 넘어 그 영상만 이 목소리.
    기준 소리(wav·json)는 첫 영상 폴더 voices/ref/ 에 한 번, 나머지 영상 설정은 그 파일을 가리킨다."""
    targets = []
    for t in (x.strip().strip("/") for x in args.only_for.split(",")):
        if not t:
            continue
        if "/" not in t:
            die("PICK", f"--only-for 는 <주제>/<영상ID>: {t}", "예: test/ilbon-chukje-2026-10,test/ilbon-chukje-2026-10-shorts")
        topic, vid = t.split("/", 1)
        d = src_dir(topic, vid)
        if not d.is_dir():
            die("PICK", f"대본 폴더 없음 {rel(d)}", "주제·영상ID 확인 (쇼츠는 <영상ID>-shorts)")
        if (d / "youtube.json").is_file():
            die("PICK", f"{vid} 는 이미 업로드한 영상 — 목소리를 바꾸지 않음", "--only-for 에서 빼기")
        targets.append((topic, vid, d))
    if not targets:
        die("PICK", "--only-for 에 영상이 없음", "예: test/ilbon-chukje-2026-10")
    for role, c in chosen.items():
        if c["how"] == "current":
            die("PICK", f"{c['id']} 는 지금 공통 목소리 — --only-for 로 고를 필요 없음", "영상 폴더의 voices/<역할>.json 을 지우면 공통 목소리로 돌아감")
        P = sample_paths(role, c["id"])
        meta = json.loads(P["meta"].read_text("utf-8")) if P["meta"].is_file() else None
        if meta is None or meta.get("ident") != sample_ident(role, c, cfg, voices):
            die("PICK", f"{c['id']} 샘플이 저장소에 없거나 후보 설정과 다름", "Kaggle 에서 samples --only " + c["id"] + " --push 를 먼저 — 들어 보지 않은 목소리는 고정하지 않음")
        own = {"_설명": f"{voices[role]['name']} — 이 영상만 다른 목소리 (공통 voices/{role}.json 의 lock 을 넘음, tts_narration v1.14 own_voice). "
                        f"사용자가 샘플 {c['id']}({c['label']})를 고름 {today}. 이 파일을 지우면 공통 목소리로 돌아감 (다음 all 이 오디오를 다시 만듦)",
               "own_voice": True, "picked": {"id": c["id"], "label": c["label"], "date": today, "sample": rel(P["mp3"]) if P["mp3"].is_file() else "-"},
               "part_instruct": {}}
        ref = None
        if c["how"] == "design":
            if not P["ref"].is_file() or hashlib.sha1(P["ref"].read_bytes()).hexdigest()[:16] != meta["ref"]["sha1"]:
                die("PICK", f"{c['id']} 기준 소리 파일이 없거나 해시가 다름", "Kaggle 에서 samples --only " + c["id"] + " --force --push")
            d0 = targets[0][2] / "voices" / "ref"
            ref_wav, ref_json = d0 / f"{role}.wav", d0 / f"{role}.json"
            own.update(engine="clone", ref_audio=rel(ref_wav), ref_meta=rel(ref_json), seed=int(c.get("seed", 1234)),
                       design={"instruct": c["instruct"], "text": meta["ref"]["text"], "seed": meta["ref"]["seed"], "tries": int(c.get("tries", 3)),
                               "f0_range": c["f0_range"], "f0_target": c.get("f0_target")})
            # 복제한 문장의 높이가 기준 소리와 많이 다르면(샘플 미리 듣기 평균 vs 기준 소리) 허용 폭을 그만큼 넓힌다 — 같은 목소리를 괜히 다시 만들지 않게
            dev = abs(float(meta.get("f0_hz") or 0) / float(meta["ref"]["f0_hz"]) - 1) if meta.get("f0_hz") else 0.0
            if dev + 0.15 > F0_TOL:
                own["f0_tolerance"] = round(dev + 0.15, 2)
                log("PICK", role=role, id=c["id"], ref_f0=meta["ref"]["f0_hz"], preview_f0=meta.get("f0_hz"), dev=f"{dev:.0%}",
                    f0_tolerance=f"{F0_TOL:.0%}→{own['f0_tolerance']:.0%}", note="샘플을 복제한 소리가 기준 소리보다 낮거나 높음 — 허용 폭을 넓힘")
            ref = (P["ref"], ref_wav, ref_meta_of(role, c, meta, today, f"{voices[role]['name']} 기준 목소리 — 이 영상들만 ({', '.join(v for _, v, _ in targets)}): "
                                                   f"사용자가 고른 샘플 {c['id']}. 손으로 바꾸지 않는다 (바꾸면 해시 검사에서 멈춤)."))
        else:
            own.update(engine="custom_voice", speaker=c["speaker"], instruct=c["instruct"], seed=int(c.get("seed", 1234)))
        for k in ("pace", "gap"):
            if c.get(k) is not None:
                own[k] = c[k]
        files = [rel(d / "voices" / f"{role}.json") for _, _, d in targets] + ([rel(ref[1]), rel(ref[1].with_suffix(".json"))] if ref else [])
        log("PICK", role=role, id=c["id"], label=c["label"], how=c["how"], only_for=",".join(v for _, v, _ in targets), files=",".join(files),
            common=f"voices/{role}.json 그대로")
        if args.dry_run:
            continue
        if ref:
            ref[1].parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ref[0], ref[1])
            ref[1].with_suffix(".json").write_text(json.dumps(ref[2], ensure_ascii=False, indent=1) + "\n", "utf-8")
        for _, _, d in targets:
            (d / "voices").mkdir(parents=True, exist_ok=True)
            (d / "voices" / f"{role}.json").write_text(json.dumps(own, ensure_ascii=False, indent=2) + "\n", "utf-8")
    if args.dry_run:
        log("PICK", note="--dry-run: 파일을 바꾸지 않음")
        return
    for topic, vid, d in targets:                              # 다시 읽어 검사 — 그 영상은 고른 목소리, 기준 소리 해시 확인
        vv = load_voices(topic, vid, quiet=True)
        for role, c in chosen.items():
            got = (vv[role].get("picked") or {}).get("id")
            if got != c["id"]:
                die("PICK", f"{vid} {role} 가 {got} 로 읽힘 (고른 것 {c['id']})", "영상 폴더 voices/ 설정 확인")
            mp = d / META_NAME
            stale = mp.is_file() and bool(voice_mismatch(json.loads(mp.read_text("utf-8")), topic, vid))
            log("PICK", video=vid, role=role, id=got, engine=vv[role]["engine"], ref=vv[role].get("ref_audio") or "-", ref_sha=vv[role].get("ref_sha") or "-",
                audio="다음 all 이 다시 만듦 (목소리 바뀜)" if stale else ("없음 — 다음 all 이 만듦" if not repo_audio(topic, vid) else "그대로"))
    log("NEXT", note="커밋·푸시 후 Kaggle: all --push --ids " + ",".join(v for _, v, _ in targets))


def cmd_pick(args):
    """고른 후보로 역할 목소리를 고정 (GPU 필요 없음). current → 설정 그대로 / custom_voice → 화자·말투 / design → 기준 소리 복사 + clone.
    고친 파일: voices/<역할>.json (+ design 이면 voices/ref/<역할>.wav·json). 커밋은 하지 않는다 (Claude 가 확인 후 main 에)."""
    voices = load_voices(quiet=True)
    cfg = load_samples_cfg(voices)
    chosen = {}
    for sid in args.ids:
        role, c = find_sample(cfg, voices, sid)
        if role in chosen:
            die("PICK", f"{role} 를 두 번 고름: {chosen[role]['id']}, {c['id']}", "역할마다 하나씩")
        chosen[role] = c
    today = datetime.now().strftime("%Y-%m-%d")
    if args.only_for:                                          # v1.14 이 영상들만
        return pick_own(args, chosen, cfg, voices, today)
    plans = []
    for role, c in chosen.items():
        P = sample_paths(role, c["id"])
        meta = json.loads(P["meta"].read_text("utf-8")) if P["meta"].is_file() else None
        if c["how"] != "current" and (meta is None or meta.get("ident") != sample_ident(role, c, cfg, voices)):
            die("PICK", f"{c['id']} 샘플이 저장소에 없거나 후보 설정과 다름", "Kaggle 에서 samples (또는 all) --push 를 먼저 — 들어 보지 않은 목소리는 고정하지 않음")
        if c["how"] == "current" and meta is not None and meta.get("ident") != sample_ident(role, c, cfg, voices):
            # current = '샘플을 만들 때의 설정'. 그 뒤 다른 후보를 골라 설정이 바뀌었으면 이 ID 는 더는 그 목소리가 아니다
            die("PICK", f"{c['id']}(지금 목소리)의 샘플을 만든 뒤 {role} 설정이 바뀜 — 이 ID 로는 예전 목소리로 돌아갈 수 없음",
                f"예전 목소리로 되돌리려면 git 으로 voices/{role}.json(과 voices/ref/{role}.*)을 되돌린 뒤 다시 pick")
        cfg_p = VOICES_DIR / f"{role}.json"
        d = json.loads(cfg_p.read_text("utf-8-sig"))
        new = dict(d)
        new["picked"] = {"id": c["id"], "label": c["label"], "date": today,
                         "sample": rel(P["mp3"]) if P["mp3"].is_file() else "-"}
        files = [cfg_p]
        if c["how"] == "custom_voice":
            for k in ("ref_audio", "ref_meta", "design"):
                new.pop(k, None)
            new.update(engine="custom_voice", speaker=c["speaker"], instruct=c["instruct"], seed=int(c.get("seed", 1234)), lock=True,
                       part_instruct={})
            for k in ("pace", "gap"):
                if c.get(k) is not None:
                    new[k] = c[k]
        elif c["how"] == "design":
            if not P["ref"].is_file() or hashlib.sha1(P["ref"].read_bytes()).hexdigest()[:16] != meta["ref"]["sha1"]:
                die("PICK", f"{c['id']} 기준 소리 파일이 없거나 해시가 다름", "Kaggle 에서 samples --only " + c["id"] + " --force --push")
            ref_wav, ref_json = VOICES_DIR / "ref" / f"{role}.wav", VOICES_DIR / "ref" / f"{role}.json"
            new.update(engine="clone", lock=True, ref_audio=rel(ref_wav), ref_meta=rel(ref_json), seed=int(c.get("seed", 1234)),
                       part_instruct={},
                       design={"instruct": c["instruct"], "text": meta["ref"]["text"], "seed": meta["ref"]["seed"], "tries": int(c.get("tries", 3)),
                               "f0_range": c["f0_range"], "f0_target": c.get("f0_target")})
            for k in ("pace", "gap"):
                if c.get(k) is not None:
                    new[k] = c[k]
            ref_meta = ref_meta_of(role, c, meta, today, f"{voices[role]['name']} 기준 목소리 — 사용자가 고른 샘플 {c['id']}. 모든 대본의 이 역할 문장이 "
                                   "이 소리를 복제한다. 손으로 바꾸지 않는다 (바꾸면 해시 검사에서 멈춤). 바꾸려면 다른 샘플을 pick")
            files += [ref_wav, ref_json]
            plans.append((role, c, new, files, (P["ref"], ref_wav, ref_meta)))
            continue
        plans.append((role, c, new, files, None))
    # 영향: 지금 저장소에 오디오가 있는 영상 중 이 역할 목소리가 바뀌는 것 (다음 all 이 다시 만든다)
    for role, c, new, files, ref in plans:
        changed_voice = c["how"] != "current"
        log("PICK", role=role, id=c["id"], label=c["label"], how=c["how"], files=",".join(rel(f) for f in files),
            voice_changes=changed_voice)
    if args.dry_run:
        log("PICK", note="--dry-run: 파일을 바꾸지 않음")
        return
    for role, c, new, files, ref in plans:
        if ref:
            src, dst, rmeta = ref
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
            (dst.with_suffix(".json")).write_text(json.dumps(rmeta, ensure_ascii=False, indent=1) + "\n", "utf-8")
        new["_버전"] = (f"picked {c['id']} — {today} — 사용자가 샘플 {c['id']}({c['label']})를 고름 → 모든 대본 이 목소리"
                       + (f" ({d0})" if (d0 := new.get("_버전")) and not str(d0).startswith("picked") else ""))
        (VOICES_DIR / f"{role}.json").write_text(json.dumps(new, ensure_ascii=False, indent=2) + "\n", "utf-8")
    after = load_voices(quiet=True)   # 다시 읽어 검사 (clone 이면 해시·기준 소리 확인)
    stale, kept = [], []
    for topic, vid, txt in script_entries():                  # v1.9 롱폼 + 쇼츠
        mp = txt.parent / META_NAME
        if mp.is_file() and repo_audio(topic, vid):
            bad = voice_mismatch(json.loads(mp.read_text("utf-8")), topic, vid)
            if bad and (txt.parent / "youtube.json").is_file():
                kept.append(vid)            # 이미 올린 영상은 all 이 건드리지 않는다 (repo_status=uploaded)
            elif bad:
                stale.append(f"{vid}({','.join(bad)})")
    log("PICK", picked=" ".join(f"{r}={v['picked']['id']}" for r, v in after.items() if v.get("picked")),
        unpicked=",".join(unpicked_roles(after)) or "-", remake=",".join(stale) or "없음",
        uploaded_kept=",".join(kept) or "-",
        note=("remake 영상은 다음 Kaggle all 이 새 목소리로 다시 만들고, 렌더한 영상은 다시 렌더" if stale else "다시 만들 오디오 없음")
        + (" · 이미 업로드한 영상은 옛 목소리 그대로 둔다" if kept else ""))
    if SAMPLES_DIR.is_dir():
        write_samples_readme(cfg, after)
    log("NEXT", note="바뀐 voices/ 파일을 main 에 커밋 → Kaggle 셀(all --push)을 다시 돌리면 고른 목소리로 오디오를 만든다")


# ----------------------------------------------------------------------------- 명령: check (저장소 오디오 ↔ 지금 대본)
def cmd_check(args):
    src = src_dir(args.topic, args.id)
    txt = src / f"{args.id}.txt"
    if not txt.is_file():
        die("CHECK", "대본 TXT 없음", "주제 폴더·영상ID 확인", path=rel(txt))
    rows, cards = read_script(txt)
    audio, meta_p = repo_audio(args.topic, args.id), src / META_NAME
    if not audio:
        log("CHECK", video=args.id, ok=False, note="narration 오디오 없음")
        raise SystemExit(2)
    if not meta_p.is_file():
        log("CHECK", logging.WARNING, video=args.id, audio=rel(audio), ok="unknown",
            note=f"{META_NAME} 없음 (직접 녹음 또는 v1.0) — 문장 수는 align-audio 가 확인")
        return
    meta = json.loads(meta_p.read_text("utf-8"))
    now = script_sha(rows, cards)
    if meta.get("script_sha1") == now:
        bad = voice_mismatch(meta, args.topic, args.id)
        if bad:
            log("CHECK", logging.WARNING, video=args.id, audio=rel(audio), ok=False, changed="목소리:" + ",".join(bad),
                hint="목소리 설정·기준 목소리가 바뀜 → Kaggle 셀을 다시 실행하면 지금 목소리로 다시 만든다 (모든 대본 같은 목소리)")
            raise SystemExit(1)
        log("CHECK", video=args.id, audio=rel(audio), ok=True, sentences=len(rows), made=meta.get("created"), tool=meta.get("tool"))
        return
    old = [(i["text"], i["part"]) for i in meta.get("items", [])]
    diff = [n for n in range(1, max(len(old), len(rows)) + 1)
            if n > len(old) or n > len(rows) or old[n - 1] != rows[n - 1]]
    yt_p = audio.parent / "youtube.json"
    if yt_p.is_file():      # 올린 영상: all 은 건드리지 않는다(repo_status=uploaded) → 다시 만들라고 하지 않는다
        trim = json.loads(yt_p.read_text("utf-8")).get("studioTrim")
        log("CHECK", logging.WARNING, video=args.id, audio=rel(audio), ok=False, audio_sentences=len(old),
            script_sentences=len(rows), changed=ranges(diff) or "고지 카드만",
            hint=("올린 영상을 스튜디오에서 잘라 냄 → 대본은 잘라 낸 영상 기준, 오디오는 원본 렌더 기록 (studio_trim.md, 다시 만들지 않음)"
                  if trim else "올린 영상의 대본이 바뀜 — all 은 올린 영상의 오디오를 다시 만들지 않는다 (새로 올리려면 사용자 확인)"))
        raise SystemExit(1)
    log("CHECK", logging.WARNING, video=args.id, audio=rel(audio), ok=False, audio_sentences=len(old), script_sentences=len(rows),
        changed=ranges(diff) or "고지 카드만", hint="대본이 바뀜 → Kaggle 에서 all 을 다시 돌리면 이 영상을 지금 대본으로 다시 만든다")
    raise SystemExit(1)


# ----------------------------------------------------------------------------- 공통
def parse_nums(s):
    out = []
    for part in (s or "").replace(" ", "").split(","):
        if not part:
            continue
        a, _, b = part.partition("-")
        out += list(range(int(a), int(b or a) + 1))
    return out


def check_split(s, name):
    if not re.fullmatch(r"\d+/\d+", s) or not 0 <= int(s.split("/")[0]) < int(s.split("/")[1]):
        die("START", f"{name} 형식 오류: {s}", "예: 0/2, 1/2")


def main():
    ap = argparse.ArgumentParser(description="대본 TXT → 내레이션 하나 (Qwen3-TTS, Kaggle GPU, 사연자·진행자 목소리) → 대본 폴더에 GitHub 올리기")
    sub = ap.add_subparsers(dest="cmd", required=True)
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--model", default=DEFAULT_MODEL, help="사연자 모델 (CustomVoice)")
    common.add_argument("--clone-model", default=DEFAULT_CLONE_MODEL, help="진행자 모델 (Base, 기준 목소리 복제)")
    common.add_argument("--design-model", default=DEFAULT_DESIGN_MODEL, help="진행자 기준 목소리를 처음 만들 때 (VoiceDesign)")
    common.add_argument("--speaker", default=None, help="모든 역할의 화자를 이것으로 (기본: voices/*.json 의 speaker, 한국어 Sohee)")
    common.add_argument("--language", default="Korean")
    common.add_argument("--gpu", type=int, default=0, help="GPU 번호 (Kaggle T4 x2: 0 또는 1)")
    common.add_argument("--device", default=None, help="직접 지정 (예: cuda:1, cpu)")
    common.add_argument("--dtype", default="auto", choices=["auto", "float32", "float16", "bfloat16"],
                        help="auto: T4는 float32, A100 등은 bfloat16")
    common.add_argument("--attn", default="auto", choices=["auto", "sdpa", "eager", "flash_attention_2"])
    common.add_argument("--seed", type=int, default=None, help="모든 역할의 기본 시드를 이것으로 (기본: voices/*.json 의 seed)")
    common.add_argument("--max-tries", type=int, default=3)
    common.add_argument("--temperature", type=float, default=None, help="비우면 모델 기본값 (역할별은 voices/*.json 의 generation)")
    common.add_argument("--top-p", type=float, default=None)
    common.add_argument("--top-k", type=int, default=None)
    common.add_argument("--repetition-penalty", type=float, default=None)
    common.add_argument("--gap", type=float, default=None, help="모든 역할의 문장 사이 쉼(초)을 이것으로 (기본: voices/*.json 의 gap)")
    common.add_argument("--lead-in", type=float, default=0.3, help="첫 문장 앞 쉼(초, 2초 이하)")
    common.add_argument("--out-dir", default=None, help="결과 최상위 폴더 (기본: Kaggle /kaggle/working/tts_out, 그 밖 output/tts)")
    common.add_argument("--keep-wav", action="store_true", help="narration.mp3 옆에 WAV도 남기기")
    common.add_argument("--fake", action="store_true", help="테스트: 모델 없이 가짜 소리")
    common.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])

    bopt = argparse.ArgumentParser(add_help=False)   # build·all 공통
    bopt.add_argument("--lexicon", default=None, help="읽는 소리 사전 TSV 추가 (기본: <주제>/tts_lexicon.tsv, source/<영상ID>/tts_lexicon.tsv)")
    bopt.add_argument("--part-gap", type=float, default=1.0, help="파트가 바뀔 때 쉼(초)")
    bopt.add_argument("--tail", type=float, default=0.8, help="마지막 문장 뒤 쉼(초)")
    bopt.add_argument("--full", action="store_true",
                      help="v1.8: 글이 바뀐 문장만 다시 만들지 않고 영상 전체를 다시 만들기 (기본: 바뀐 문장이 20%% 이하면 그 문장만)")
    bopt.add_argument("--push", action="store_true",
                      help="영상이 끝날 때마다 결과(narration.mp3·tts_narration.json·tts_report.md)를 대본 폴더에 GitHub main 으로 올리기 (토큰: GITHUB_TOKEN)")

    b = sub.add_parser("build", parents=[common, bopt], help="영상 하나 → narration.mp3 (--push 로 대본 폴더에 올림)")
    b.add_argument("topic")
    b.add_argument("id")
    b.add_argument("--txt", default=None, help="대본 TXT 직접 지정")
    b.add_argument("--redo", default="", help="새 시드로 다시 만들 문장 번호 (예: 12,15 또는 3-5)")
    b.add_argument("--shard", default="0/1", help="GPU 2개로 한 영상을 나눠 만들기: 0/2 와 1/2 를 동시에, 끝나면 --assemble-only")
    b.add_argument("--assemble-only", action="store_true", help="만들어 둔 문장 파일로 잇기·내보내기만")

    a = sub.add_parser("all", parents=[common, bopt], help="저장소의 대본을 모두 읽어 오디오가 없는 영상 전부")
    a.add_argument("--topics", default=None, help="이 주제만 (예: stock 또는 stock,health)")
    a.add_argument("--ids", default=None, help="이 영상만 (예: bittu-2026-10,panicsell-2026-10)")
    a.add_argument("--include-hold", action="store_true", help="보류(⏸) 주제도 포함")
    a.add_argument("--force", action="store_true", help="저장소에 지금 대본과 같은 오디오가 있어도 다시 만들기")
    a.add_argument("--keep-stale", action="store_true", help="옛 대본으로 만든 오디오를 다시 만들지 않기 (기본: 다시 만듦)")
    a.add_argument("--max", type=int, default=0, help="이번에 만들 최대 영상 수 (0 = 전부)")
    a.add_argument("--split", default="0/1", help="GPU 2개로 영상을 나눠: --gpu 0 --split 0/2 와 --gpu 1 --split 1/2 를 동시에 (--push 는 차례로 올림)")
    a.add_argument("--dry-run", action="store_true", help="무엇을 만들지 목록만 (모델 안 불러옴)")
    a.add_argument("--no-pack", action="store_true", help="--push 없이 돌릴 때 끝나고 zip 만들지 않기")

    sub.add_parser("push", parents=[common], help="만들어 둔 결과를 대본 폴더마다 GitHub main 에 올리기")
    vo = sub.add_parser("voice", parents=[common], help="진행자 기준 목소리 확인·만들기 (없을 때만. --force 는 다시 만들기 — 모든 영상 목소리가 바뀜)")
    vo.add_argument("--force", action="store_true", help="이미 있어도 다시 만들기 (그 뒤 all 이 모든 영상을 새 목소리로 다시 만든다)")
    vo.add_argument("--push", action="store_true", help="만든 기준 목소리를 voices/ 에 올리기")
    sub.add_parser("pack", parents=[common], help=f"(올리기가 안 될 때만) OUT/upload/ → {ZIP_NAME}")

    sp = sub.add_parser("samples", parents=[common], help="목소리 후보 샘플 (voices/samples/samples.json) → voices/samples/<역할>/<ID>.mp3")
    sp.add_argument("--only", default=None, help="이 후보만 (예: S04,H02)")
    sp.add_argument("--force", action="store_true", help="이미 있어도 다시 만들기")
    sp.add_argument("--push", action="store_true", help="만든 샘플을 voices/samples/ 에 올리기")
    sp.add_argument("--dry-run", action="store_true", help="무엇을 만들지 목록만")
    sp.add_argument("--play", action="store_true", help="만든 뒤 바로 듣기 (터미널 ffplay·afplay·mpv)")
    li = sub.add_parser("listen", parents=[common], help="샘플·기준 소리 바로 듣기 (예: listen S07 S08, listen storyteller, 파일 경로)")
    li.add_argument("items", nargs="+", help="후보 ID · 역할 이름(기준 소리) · 파일 경로")
    pk = sub.add_parser("pick", parents=[common], help="고른 샘플로 역할 목소리 고정 (예: pick S04 H01) — GPU 필요 없음")
    pk.add_argument("ids", nargs="+", help="고른 후보 ID (역할마다 하나)")
    pk.add_argument("--dry-run", action="store_true", help="바꿀 내용만 보기")
    pk.add_argument("--only-for", default=None, help="v1.14 이 영상들만 (예: test/ilbon-chukje-2026-10,test/ilbon-chukje-2026-10-shorts) — 공통 목소리는 그대로")
    c = sub.add_parser("check", parents=[common], help="저장소의 narration 이 지금 대본으로 만든 것인지 (tts_narration.json)")
    c.add_argument("topic")
    c.add_argument("id")

    args = ap.parse_args()
    logging.basicConfig(level=getattr(logging, args.log_level), format="%(message)s", stream=sys.stdout)
    engine_ids.args = args   # 모델을 불러오지 않는 명령(check·dry-run)도 목소리 정체를 같은 모델 이름으로 계산
    log("START", tool=f"tts_narration.py {VERSION}", cmd=args.cmd, out=out_root(args), note="연구·교육용 — 투자 권유 아님")
    if args.lead_in > 2.0:
        die("START", "--lead-in 은 2초 이하", "srt_tool 규칙: 첫 자막 앞 여백 2초 이내")
    if args.cmd == "build":
        check_split(args.shard, "--shard")
        cmd_build(args)
    elif args.cmd == "all":
        check_split(args.split, "--split")
        cmd_all(args)
    elif args.cmd == "push":
        cmd_push(args)
    elif args.cmd == "voice":
        cmd_voice(args)
    elif args.cmd == "pack":
        cmd_pack(args)
    elif args.cmd == "samples":
        cmd_samples(args)
    elif args.cmd == "pick":
        cmd_pick(args)
    elif args.cmd == "listen":
        cmd_listen(args)
    else:
        cmd_check(args)


if __name__ == "__main__":
    main()
