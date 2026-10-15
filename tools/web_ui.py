#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v2.1 — 2026-10-15 — 주제마다 다른 키 · 외국 영상 켜고 끄기 (사용자 지시: "키도 나눠서 쓸수 있게해 주제별로 다른키 넣을거니까 그리고
#          주식은 외국 영상도 다 분석할 건데 확인해봐 on/off 기능(default off) 있는지 확인하고 없으면 추가해"):
#          ① 4번 칸 [외국 영상도] — 이 주제의 analyzer_config.toml [search] INCLUDE_FOREIGN 을 고침 (POST /api/foreign — PC 파일 + GitHub 토큰이
#             있으면 GitHub 에도, 작업 중엔 못 바꿈). 기본 꺼짐 = 예전처럼 외국 영상을 뺌. 켜면 탐색이 외국 영상을 빼지 않고 '외국 영상' 표시만,
#             검색은 언어 지정 없이 (outlier_research v2.4 — 검색 캐시가 따로라 켠 뒤 첫 탐색은 새로 검색), 분석(success·shorts)도 넣음
#          ② 0번 칸 할당량에 '이 탭 키'(지문 끝 4자리)·같은 키를 쓰는 다른 주제 — 주제마다 다른 키면 할당량도 따로 보임 (키 장부가 키마다 하나)
# (v2.0 — 2026-10-15 — 한 화면에 주제 탭 (사용자 지시: "헷갈리니까 하나의 사이트에서 그냥 탭 만들어서 다른 주제 볼 수 있게 하자 서로
#          캐시는 공유하지 않도록 하고" · "설정도 다 따로써야해"):
#          ① 창(포트)을 주제마다 띄우던 것 → 한 화면(http://127.0.0.1:8765/) 위쪽 탭으로 주제를 고름. 요청마다 X-Topic 머리글로 주제를 보냄
#          ② 작업(JOB)도 주제마다 따로 — 재테크 탭에서 승인하는 동안 주식 탭에서 탐색 가능 (할당량은 같은 키 장부로 함께 셈)
#          ③ 이 화면이 모든 주제를 잠금 (다른 화면·예전 창이 쓰는 주제는 그 탭을 보기만, 동작은 막음)
#          ④ 설정 따로: 키는 그 주제 .env 에만 저장(처음엔 맨 위 .env 복사 — pc_analysis v1.14), 화면의 롱폼/쇼츠·최근 N주도 탭마다 기억
#          ⑤ 캐시 따로: 탐색 캐시·목록은 주제 폴더, 분석기 API 캐시는 .yt_work/cache_<주제>(분석기 v2.12.0) — 예전 공동 캐시는 켤 때 .yt_work/old/ 로
#          ⑥ 음성인식은 PC 에서 한 번에 하나 — 다른 탭에서 누르면 줄을 세워 앞 주제가 끝나면 이어서
#          ⑦ 할당량 초기화 뒤 이어서 — 탭(주제)마다 남은 것을 차례로
# (v1.6.2 — 2026-10-15 — 주제 캐시 (사용자 지시: "왜 예전 재테크 캐시가 남아 있어 이거 어떻게해"):
#          ① 0번 칸에서 주제를 바꾸면 앞 주제의 끝난 작업 줄·쇼츠 분석 칸이 화면에 남던 것 — 작업 줄을 비우고 쇼츠 분석도 다시 읽음
#          ② 켤 때·주제를 바꿀 때 pc_analysis.fresh_start — 설정에 FRESH_START 가 있는 새 주제(stock)면 예전 PC 자료를 한 번 옮김
#          ③ 4번 칸 [캐시 비우기] → /api/cache/reset (pc_analysis.reset_topic_cache — 탐색 캐시·탐색 목록만, 지우지 않고 .yt_work/old/ 로))
# (v1.6.1 — 2026-10-15 — 분석 칸의 'analysis.md 전문' 경로를 이 창의 주제로 (예전엔 economic 고정 — stock 창에서 틀린 경로))
# (v1.6 — 2026-10-15 — 쇼츠 탐색·승인·분석 (사용자 지시: "깃허브 저장소에 유튜브 분석기 있지? 거기에 쇼츠 분석 기능도 추가해 목적은
#          사람들의 니즈를 충족해주는 쇼츠를 만들어서 최대한 조회수를 높이기 위한 쇼츠를 만들기 위해 분석하는거야 전력을 다해서 해봐"):
#          ① 4·5번 칸에 [롱폼 | 쇼츠] 전환 — 쇼츠 탐색 = 검색어마다 쇼츠 검색 1번(videoDuration=short, 100단위, 적응형 7일 캐시) + 추가한 채널의
#             쇼츠 목록(UUSH — 50개에 1단위) + 주소로 넣은 쇼츠 → 3분 이하·세로만 (outlier_research v2.3 is_short — 화면비는 영상 정보와 같은 1단위)
#             → 배수 높은 순 목록, 추천(성공 쇼츠: 구독자 5만 이하·조회수 5만 이상·×3 / 조회수 상위 20 / 추가한 것)은 체크만
#          ② 쇼츠 [승인] → 설명·자막(시도)·표지(세로 먼저)·댓글 전부 → <주제>/result/outliers/shorts/S_<영상ID>/ → 채널 평소 쇼츠(채널 쇼츠 목록
#             최근 50개 — 채널 하나 약 2단위) → 쇼츠 분석(tools/shorts_analysis.py → shorts/analysis.md) → 바로 GitHub → 음성인식은 뒤에서
#             (분석기 v2.11.0 — 쇼츠 먼저, 쇼츠는 짧아 하나에 1~2분)
#          ③ 6번 칸에 쇼츠 분석 요약 · [쇼츠 성공 후보 체크], 켤 때·다시 분석·초기화 뒤 이어서에 쇼츠도 (못 받은 댓글·채널 평소 쇼츠·남은 쇼츠 탐색)
#          ④ 시험 고침: 초기화 뒤 이어서의 상태('started')를 작업 시작 전에 적음 (시험이 작업 시작과 상태 쓰기 사이를 읽어 실패하던 것))
# (v1.5 — 2026-10-15 — 할당량 표시·주제별 창·초기화 뒤 자동으로 이어서 (사용자 지시: "유튜브 분석 코드를 최대한 api 사용량 덜쓰는
#          방법(단어 줄이는 방법 말고) 찾아서 수정해보고 웹 ui에 사용량 얼마나 남았는지 표시하고 그리고 분석기 여러개 열어서 각자 다른 주제로
#          탐색해도 되지? 그리고 economic 같은 주제 경로를 선택할 수 있게해서 각각 주제별로 탐색할 수 있게 수정해 그리고 사용량 초기화되면
#          자동으로 다시 분석 마저 하는거지? 그렇게 되야해"):
#          ① 남은 할당량: 화면 위에 '남은 N / 9,800 · 초기화 한국 시간 MM-DD HH:MM (n시간 뒤)' — 같은 키를 쓰는 모든 창·주제·자동 실행을
#             합친 키 장부(tools/pc_analysis.py KeyLedger, 요청마다 적음). 자세히: 주제별·작업별 사용량, 열린 다른 창
#          ② 주제 고르기: 화면 위 주제 목록 = 설정 파일이 있는 모든 주제 폴더(경로 표시) + [새 주제] (폴더·이름·검색어 → 설정 파일 3개)
#          ③ 창 여러 개: 창(프로세스)마다 주제 하나를 잠금(.yt_work/web_<주제>.lock — OS 잠금) — 같은 주제를 두 창이 동시에 쓰지 않게,
#             다른 주제는 동시에. 같은 주제 창이 이미 있으면 그 창 주소를 열고 끝. `web_ui.py economic health` 처럼 주제를 여러 개 주면
#             주제마다 창을 하나씩 띄움 (포트 자동). 음성인식은 PC 에서 한 번에 하나 (분석기 v2.10.1 — 다른 주제는 기다렸다가)
#          ④ 초기화 뒤 자동으로 이어서: 태평양 자정(+10분)이 되면 할당량 때문에 남은 것(탐색 검색·영상 정보, 못 받은 댓글, 채널 기준선)을
#             저절로 이어서 하고 다시 분석·올림 (job_resume). 켤 때도 남은 탐색이 있으면 이어서. 다시 탐색해도 내가 체크한 것은 그대로
#          ⑤ 할당량 아끼기 (outlier_research v2.2): 적응형 검색 캐시(안 바뀌는 검색은 7→14→21일), 채널 목록은 새 영상만, 오래된 영상 정보는
#             길게, 한 쪽짜리 댓글은 인기 댓글 쪽 건너뜀 — 탐색 로그에 검색마다 캐시 시간·단계·새로 보인 영상)
# (v1.4 — 2026-10-14 — 분석 결과로 '무엇이 먹혔나'를 가릴 수 있게 (사용자 지시: "결과 올라갔는데 문제가 부분 수정하고
#          분석결과로 내가 말한 거 할수 있는지 판단해 개선 필요하면 더 개선하고"):
#          ① 같은 채널 기준선 (job_baseline): 켤 때·승인 때 사례 채널(구독자 5만 이하) 최근 영상 50개(업로드 목록 + 영상 정보 —
#             채널 하나 약 2단위, 7일 캐시)를 받음 → 분석이 '채널 평소 대비 ×'·같은 채널 잘된 영상 vs 평소 영상을 셈
#             (⚠️ 할당량: 처음 한 번 채널 141곳이면 약 280단위)
#          ② 음성인식 2단계 표시 (분석기 v2.10.0 — 1차 앞 5분 → 2차 전체): 차수 이름·차수마다 n/전체, 남은 수에 2차 남은 영상도
#          ③ 분석 요약 칸에 같은 채널 기준선 (성공 사례 몇 개에 '채널 평소 대비'가 있나)
# (v1.3 — 2026-10-14 — 성공 사례 분석(analysis.md)이 맞게 나오게 (사용자 지시: "성공 사례 영상의 정보와 시청자들의 니즈 …
#          어떤 주제, 어떤 제목, 어떤 썸네일, 내용을 어떻게 구성해야하는지 … 올바른 분석 결과까지만 내도록 수정해"):
#          ① 켤 때 코드도 GitHub 최신으로 받은 뒤 도구를 불러옴 (새 도구 tools/success_analysis.py 가 PC 에 오게 — 실행기 목록에 없던 파일)
#          ② 못 받은 댓글 이어 받기 (job_comments — 승인 영상 W_ 중 comments_complete=False: 2026-10-14 88개 중 55개가 할당량이 끝나 0개였고
#             예전엔 다시 받을 길이 없었음) — 켤 때 저절로, [못 받은 댓글 이어 받기] 단추
#          ③ 분석 결과 칸 위에 성공 사례 분석 요약 (성공 사례 수·글 출처·한계·자료 없는 성공 후보 → [성공 후보 체크] 단추)
#          ④ 수요와 공급 (사용자 지시: "수요 대비 영상 공급이 별로 없는지도 파악해야해 …"): [탐색] 때 검색어마다 YouTube 자동완성(사람들이 찾는 말)도
#             받음 (할당량 0, 7일 캐시) · [공급 확인] = 수요는 있는데 영상이 적어 보이는 말 N개를 직접 검색(말 하나 100단위) → 다시 분석·올림)
# (v1.2.1 — 2026-10-14 — 공개 저장소에도 자료(사례 폴더)를 다 올림 (사용자 지시 "그냥 공개에서 다 올리도록 해" — 분석기 v2.9.3): 승인 결과 안내를
#          분석기 로그의 full=True/False 로 읽음 (예전: private=True/False — 공개면 늘 'PC 에만'으로 보였을 것))
# (v1.2 — 2026-10-14 — 결과 먼저 올리고 음성인식은 뒤에서 (사용자 지시: "아니 음성인식이랑 별개로 분석결과 낼 수 있잖아 자막도
#          다운 시도했는데 안되면영상 설명으로 대체해서 그냥 분석결과랑 자료 다 올려 그 다음 음성인식하라고 수정해"):
#          ① [승인] = 자료 받기(설명·자막 시도·썸네일·댓글 전부) → 주별 분석(자막을 못 받은 영상은 영상 설명으로 대신 —
#             weekly_analysis v1.2, 승인 영상 표 approved.md) → **바로 GitHub 에 올림** → 작업 끝. (예전 v1.1: 음성인식 대기열이
#             다 끝나야 — 289개면 2~3일 — 올렸음)
#          ② 음성인식은 그 뒤에 '뒤에서' 따로 (화면 위 '음성인식' 표시: n/전체·지금 영상, [음성인식 시작]·[멈춤]) — 하나 끝날 때마다
#             대본을 넣어 주별 분석을 다시 만들고 바로 올림 (분석기 --whisper-queue). 도는 동안에도 탐색·승인을 할 수 있음.
#             승인을 더 하면 지금 대기열이 끝난 뒤 새 영상도 이어서
#          ③ 화면을 켜면: 승인한 영상이 있으면 주별 분석을 다시 만들어 올리고(새 코드의 설명 대체·표), 자막 없는 영상이 남았으면
#             음성인식을 뒤에서 시작 (--no-whisper 로 끔)
#          ④ [다시 분석]도 다시 만든 뒤 올림
#          ※ 사례 폴더(W_ — 다른 사람의 설명·자막·댓글·썸네일 원문)는 저장소가 비공개일 때만 올라감 (CLAUDE.md) — 공개면 화면에 안내)
# (v1.1.1 — 2026-10-14 — 분석 결과 안내 글만: 오래된 영상은 '창 밖' → 마지막 '전체' 창에 (weekly_analysis v1.1))
# (v1.1 — 2026-10-14 — 목록 고침 (사용자 지시: "영상이나 채널 여러 개 넣을 수 있게 하고 체크된거랑 안된거 따로 목록 분리해서
#          보여주고 이미 분석에 사용한 영상이면 목록에서 제외해 그리고 라이브 방송, 외국 영상은 탐색 대상에서 제외 그리고 목록을 배수가
#          가장 높은순으로 정렬해"): ① 직접 추가 칸에 여러 개 (한 줄에 하나 — 띄어쓰기·쉼표로 나눠도 됨) ② 목록을 '체크한 영상'과
#          '체크 안 한 영상' 두 표로 (체크하면 위 표로 옮겨 감) ③ 이미 분석에 쓴 영상(승인한 W_·성공 사례 01_·조회수 상위 P01_·_old·
#          분석기 성공사례)은 목록에서 뺌 ④ 라이브 방송·외국 영상은 탐색에서 뺌 (tools/outlier_research.py v2.0 exclusion_reason —
#          주소로 직접 넣은 영상만 남기고 표시) ⑤ 목록은 배수(조회수÷구독자) 높은 순 (구독자 비공개는 맨 뒤)
# (v1.0 — 2026-10-14 — 신규: 분석기 웹 화면 (사용자 지시: "이거 분석기 웹 ui 형식으로 만들어 실행하면 바로 웹 ui가 나와서 env, 검색어
#          수정할 수 있게하고 탐색 버튼 누르면 탐색 대상 영상 목록이 나오지만 체크 표시만 해놓고 내가 승인 버튼을 눌러야 관련 자료를 받아서
#          분석하는걸로 해 그리고 내가 영상 url이나 채널을 추가하면 탐색 대상에 추가하도록 하고(채널을 추가하면 그 채널에 올려진 영상 다
#          탐색하는거야) 목록은 최근에 업로드 된 순으로 하고 1주 전, 2주 전, 3주 전 1주씩 늘리면서 분석 결과 내보도록 해"):
#          ① 실행하면 브라우저에 화면이 뜸 (이 PC 안에서만 — 127.0.0.1, 요청마다 무작위 열쇠 확인)
#          ② 키(.env 의 YOUTUBE_API_KEY·GITHUB_TOKEN — 끝 4자리만 보임)·검색어(<주제>/keywords.txt, GitHub 에도 저장 가능) 고치기
#          ③ 직접 추가: 영상 주소 → 그 영상, 채널 주소·@이름 → 그 채널에 올라온 영상 전부 (<주제>/targets.json)
#          ④ [탐색] → 검색어(최근 N주·조회수 순·4~20분·20분 넘음) + 추가한 채널·영상 → 목록 (최근 업로드 순). 추천(성공 사례·조회수 상위·
#             추가한 것)은 체크만 해 둠 — 자료는 아직 안 받음
#          ⑤ [승인] → 체크한 영상만 설명·자막·썸네일·댓글 전부를 받고(<주제>/result/outliers/W_<영상ID>/) 주별 분석
#             (tools/weekly_analysis.py — 최근 1주·2주·3주 … 한 주씩 넓힘) → 자막을 못 받은 영상은 음성인식 대기열 → 다시 분석 → GitHub))
r"""
사용법 (PC 실행 폴더 — run_analyzer.ps1 이 기본으로 띄움):
  python tools/web_ui.py                    # economic (설정 파일이 있는 주제 폴더가 여럿이면 화면에서 고름)
  python tools/web_ui.py economic --port 8765 --no-browser
  python tools/web_ui.py economic health    # 주제마다 창 하나씩 (같은 키의 할당량은 함께 셈 — 화면 위 '남은 할당량')
  옵션: --port 8765 (쓰는 중이면 다음 번호) · --no-browser (주소만 보여 줌) · --no-sync (GitHub 에서 설정·검색어를 받지 않음)
        --no-whisper (켤 때 음성인식을 뒤에서 시작하지 않음 — 화면의 [음성인식 시작]으로)
순서: [승인] → 자료 받기 → 같은 채널 기준선(채널 평소 영상) → 주별·성공 사례 분석(자막 없으면 설명으로) → GitHub 에 올림
      → (뒤에서) 음성인식 — 성공 사례부터 1차(앞 5분) → 2차(전체), 하나 끝날 때마다 다시 분석, 15분마다·차수 끝에 올림
쇼츠 (v1.6, 화면 4·5번 칸 [쇼츠]): [탐색] → 쇼츠 목록(3분 이하·세로) → 체크 → [승인] → shorts/S_<영상ID>/ → 채널 평소 쇼츠 → 쇼츠 분석
      (shorts/analysis.md) → GitHub → 음성인식(쇼츠 먼저). 검색어는 <주제>/shorts_keywords.txt 가 있으면 그것, 없으면 keywords.txt
할당량: 탐색 = 검색어 1개마다 검색 2번(200단위, 7일 캐시) + 채널 영상 목록 50개에 1단위 + 영상 정보 50개에 1단위.
        쇼츠 탐색 = 검색어 1개마다 검색 1번(100단위, 7일 캐시) + 영상 정보 50개에 1단위. 쇼츠 승인 = 댓글 100개에 1단위 + 채널 평소 쇼츠 채널 하나 약 2단위.
        승인 = 영상마다 댓글 100개에 1단위 (+ 답글). 같은 채널 기준선(켤 때·승인 때) = 채널 하나 약 2단위 (7일 캐시).
        오늘 쓴 양: 키 장부 .yt_work/quota_key_<키 지문>.json (같은 키의 모든 창·주제·자동 실행) + 주제 장부 .yt_work/quota_<주제>.json.
        할당량이 끝나 남은 것은 태평양 자정(한국 오후 4~5시) +10분에 저절로 이어서 (창을 켜 둔 동안 · 켤 때도).
로그: [STAGE] [시각] key=value — 화면의 '진행' 칸과 .yt_work/web_ui.log
비밀값(키·토큰)은 화면·로그에 끝 4자리만. ※ 연구·교육용 분석 도구. 투자 권유가 아니다.
"""
import argparse
import base64
import collections
import hashlib
import json
import logging
import os
import re
import secrets
import subprocess
import sys
import threading
import time
import types
import urllib.error
import urllib.parse
import urllib.request
import webbrowser
from datetime import datetime, timedelta, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import pc_analysis as pc                 # noqa: E402  할당량 장부·키 찾기·GitHub 동기화·패키지 준비

ROOT = pc.ROOT
VERSION = "v2.1"
LOG = logging.getLogger("web")
KST = timezone(timedelta(hours=9))
TOKEN = secrets.token_urlsafe(18)        # 화면이 요청마다 보내는 열쇠 (다른 사이트가 이 PC 의 화면을 조작하지 못하게)
MIN_SEC = 240                            # 롱폼 기준 (4분) — 그보다 짧으면 '짧은 영상'
POPULAR_N = 20                           # 검색 결과 중 조회수 상위 몇 개를 추천(체크)할지
orr = None                               # tools/outlier_research.py (패키지 준비 뒤 불러옴)
wa = None                                # tools/weekly_analysis.py
sh = None                                # tools/shorts_analysis.py (v1.6 — 쇼츠 분석, 없으면 쇼츠 기능만 꺼짐)
SHORTS_POPULAR_N = 20                    # v1.6: 쇼츠 검색 결과 중 조회수 상위 몇 개를 추천(체크)할지
SHORTS_BASELINE_VIDEOS = 50              # v1.6: 채널 평소 쇼츠 — 채널 쇼츠 목록(UUSH) 최근 몇 개 (목록 1단위 + 영상 정보 1단위)
SHORTS_BASELINE_TTL_H = 168
SHORTS_CASE_RX = re.compile(r"^S_([0-9A-Za-z_-]{11})$")
STATE = {"topic": None, "topics": [], "port": None}     # v2.0: topic = 처음 열 탭, topics = 화면의 탭(주제 폴더)
LOCKS = {}                                # v2.0: 이 화면이 잠근 주제 {주제: 잠금 파일} (OS 잠금 — 화면이 꺼지면 풀림)
RESUME_T = {}                             # v2.0: 주제마다 지난 이어서 {"last", "last_result", "note"}
RESUME = {"next": None, "last": None, "last_result": None, "status": "idle", "note": ""}   # v1.5: 초기화 뒤 자동으로 이어서
RESUME_MARGIN_MIN = 10                   # 태평양 자정 + 이 분 뒤에 이어서 (Google 쪽 초기화가 조금 늦을 때)
RESUME_JOB_WAIT_H = 6                    # 그때 다른 작업이 도는 중이면 끝나길 기다리는 최대 시간
TOPIC_RX = re.compile(r"^[a-z][a-z0-9_-]{1,30}$")
def new_job():
    return {"name": None, "status": "idle", "step": "", "done": 0, "total": 0, "started": None, "finished": None, "error": None,
            "result": None, "cancel": False, "log": collections.deque(maxlen=500), "proc": None}


JOBS = {}                                 # v2.0: 주제마다 작업 하나 {주제: 작업} — 다른 주제 작업은 동시에
_TL = threading.local()                   # 작업 스레드가 자기 작업(진행 칸)을 앎 — step()·run_subprocess·로그 줄
_SCRATCH = new_job()                      # 작업 밖에서 부른 step() 이 쓰는 빈 자리 (화면에 안 보임)


def job_of(t):
    return JOBS.setdefault(t, new_job())


def cur_job():
    """지금 스레드의 작업 (작업 밖이면 도는 작업이 하나뿐일 때 그것 — 작업이 띄운 일꾼 스레드의 로그도 진행 칸에)."""
    j = getattr(_TL, "job", None)
    if j is not None:
        return j
    running = [x for x in JOBS.values() if x["status"] == "running"]
    return running[0] if len(running) == 1 else _SCRATCH


JOB_LOCK = threading.Lock()
# 음성인식 (v1.2) — 작업(JOB)과 따로 뒤에서: 탐색·승인을 하는 동안에도 돎. 분석기 --whisper-queue 를 돌리고 출력 줄로 진행을 읽음
WHISPER = {"queued": [], "status": "idle", "topic": None, "proc": None, "started": None, "finished": None, "current": "", "done": 0, "failed": 0,
           "total": 0, "pass": "", "rerun": False, "stop": False, "last_exit": None, "note": "", "log": collections.deque(maxlen=300)}
WHISPER_LOCK = threading.Lock()
WHISPER_LINE_RX = re.compile(r"\[(?:INFO|WARNING)\] (\d+)/(\d+) (시작|끝|실패|올림|올리기 실패)(.*)$")
WHISPER_ITEMS_RX = re.compile(r"음성인식 대기열 items=(\d+)(?:.*?pass_=(\"[^\"]*\"|\S+))?")   # 분석기 v2.10.0 — 차수(1차 앞 5분·2차 전체)마다 한 줄
WHISPER_MAX_ATTEMPTS = 3                 # 분석기 WHISPER_QUEUE_MAX_ATTEMPTS 와 같게 (그만큼 실패한 영상은 '남은 것'에서 뺌)
SKIP_TRANSCRIPT = ("건너뜀", "확인 안 함")
NETWORK_FAIL_WORDS = ("ProxyError", "ConnectionError", "Timeout", "URLError")     # 분석기 대기열과 같은 기준 (연결 자체 실패는 뺌)
_PENDING_CACHE = {"t": None, "at": 0.0, "n": 0}


def log(stage, level=logging.INFO, **kv):
    LOG.log(level, "[%s] [%s] %s", stage, datetime.now().isoformat(timespec="seconds"),
            " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) and ' ' in v else v}" for k, v in kv.items()))


class _JobLogHandler(logging.Handler):
    """도구들의 로그 줄을 화면의 '진행' 칸으로."""

    def emit(self, record):
        try:
            j = cur_job()
            if j is not _SCRATCH:
                j["log"].append(self.format(record))
        except Exception:
            pass


class UserError(Exception):
    """사용자에게 그대로 보여 줄 오류 (키 없음 등)."""


class Cancelled(Exception):
    pass


# ---------------------------------------------------------------- 경로·파일
def topic_dir(t):
    return ROOT / t


def out_dir(t):
    return ROOT / t / "result" / "outliers"


def web_dir(t):
    d = ROOT / t / "result" / "web"           # 탐색 목록 등 PC 에만 (GitHub 에 올리지 않음)
    d.mkdir(parents=True, exist_ok=True)
    return d


def _read_json(p, default):
    try:
        return json.loads(Path(p).read_text("utf-8"))
    except (OSError, ValueError):
        return default


def _write_json(p, data):
    p = Path(p)
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_name(p.name + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=1), "utf-8")
    os.replace(tmp, p)


def find_topics():
    return sorted(p.parent.name for p in ROOT.glob("*/analyzer_config.toml") if not p.parent.name.startswith("."))


def topic_name(t):
    try:
        flat = {}
        for k, v in pc._toml().loads((ROOT / t / "analyzer_config.toml").read_text("utf-8")).items():
            flat.update(v if isinstance(v, dict) and k != "KEYWORD_GROUPS" else {k: v})
        return str(flat.get("TOPIC") or t)
    except Exception:
        return t


# ---------------------------------------------------------------- 키 (.env)
ENV_NAMES = ("YOUTUBE_API_KEY", "GITHUB_TOKEN")


def mask(v):
    return f"…{v[-4:]} ({len(v)}자)" if v else ""


def env_view(t):
    out = {}
    for n in ENV_NAMES:
        v, src = pc.find_secret(n, t)
        out[n] = {"set": bool(v), "tail": mask(v), "source": src if v else "-"}
    return out


def set_env_value(path, name, value):
    """.env 의 name= 줄을 바꾸거나 더함 (다른 줄·메모는 그대로). 값은 로그에 쓰지 않음."""
    path = Path(path)
    lines = path.read_text("utf-8-sig").splitlines() if path.is_file() else []
    rx = re.compile(rf"^[ \t]*{name}[ \t]*=")
    for i, line in enumerate(lines):
        if rx.match(line):
            lines[i] = f"{name}={value}"
            break
    else:
        lines.append(f"{name}={value}")
    path.write_text("\n".join(lines) + "\n", "utf-8")


# ---------------------------------------------------------------- 검색어·직접 추가
def keywords_path(t):
    return ROOT / t / pc.KEYWORD_LIST_FILE


def targets_path(t):
    return ROOT / t / "targets.json"


def load_targets(t):
    d = _read_json(targets_path(t), {})
    return {"channels": list(d.get("channels") or []), "videos": list(d.get("videos") or [])}


def github_put(t, rel, data, message):
    """GitHub 에 파일 하나 저장 (contents API — 토큰 필요). → (ok, 설명)."""
    token = pc.find_secret("GITHUB_TOKEN", t)[0]
    if not token:
        return False, "GITHUB_TOKEN 없음 — PC 에만 저장"
    repo, branch = pc.repo_of(t)
    url = f"https://api.github.com/repos/{repo}/contents/{urllib.parse.quote(rel)}"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
    sha = None
    try:
        with urllib.request.urlopen(urllib.request.Request(f"{url}?ref={urllib.parse.quote(branch)}", headers=headers), timeout=30) as r:
            sha = json.loads(r.read().decode("utf-8")).get("sha")
    except urllib.error.HTTPError as e:
        if e.code != 404:
            return False, f"GitHub 읽기 실패 HTTP {e.code}"
    except Exception as e:
        return False, f"GitHub 연결 실패 ({type(e).__name__})"
    body = {"message": message, "content": base64.b64encode(data).decode("ascii"), "branch": branch}
    if sha:
        body["sha"] = sha
    req = urllib.request.Request(url, data=json.dumps(body).encode("utf-8"), headers={**headers, "Content-Type": "application/json"}, method="PUT")
    try:
        with urllib.request.urlopen(req, timeout=30):
            pass
    except urllib.error.HTTPError as e:
        return False, f"GitHub 저장 실패 HTTP {e.code}" + (" — 토큰의 Contents 권한이 Read and write 인지 확인" if e.code in (403, 404) else "")
    except Exception as e:
        return False, f"GitHub 연결 실패 ({type(e).__name__})"
    sync_p = ROOT / ".yt_work" / "config_sync.json"            # 자동 실행의 동기화가 'GitHub 과 같음'으로 보게
    st = _read_json(sync_p, {})
    st[rel] = hashlib.sha256(data).hexdigest()
    _write_json(sync_p, st)
    return True, f"GitHub 에도 저장 ({repo}/{rel})"


def key_ledger(t):
    """이 주제가 쓰는 YouTube 키의 장부 (같은 키 = 모든 창·주제가 함께, v1.5). 키가 없으면 None."""
    key = orr.load_api_key(t)[0]
    return pc.KeyLedger(key) if key else None


def make_api(t, what="web"):
    """v1.5: 남은 양 = 키 장부(같은 키의 다른 창·주제·자동 실행 포함). 요청마다 키 장부에 먼저 적고(orr.Api ledger=) 실패하면 돌려줌."""
    key, src = orr.load_api_key(t)
    if not key:
        raise UserError("YouTube API 키가 없습니다 — 화면 위 '1. 키 설정'에서 넣고 저장하세요")
    kl = pc.KeyLedger(key)
    left = kl.left()
    if left < 1:
        q = kl.snapshot()
        raise UserError(f"오늘 할당량을 다 썼습니다 (이 키로 {q['used']:,}단위" + (" · Google 이 하루 한도라고 답함" if q["exhausted"] else "")
                        + f") — 한국 시간 {q['reset_kst']} 초기화 +{RESUME_MARGIN_MIN}분 뒤 남은 것은 저절로 이어서 합니다 (이 창을 켜 두면)")
    return orr.Api(key, left, ledger=kl, what=what, topic=t), pc.Ledger(t), src


def record_use(t, api, ledger, what):
    """작업이 끝날 때 (v1.5): 주제 장부(자동 실행이 주제 몫을 셀 때 봄)에 적음 — 키 장부는 요청마다 이미 적었으므로 기록 한 줄만."""
    ledger.add(api.used, what, forward=False)
    if api.used and getattr(api, "ledger", None) is not None:
        api.ledger.note_run(what, t, api.used)
    if api.used:
        log("QUOTA", topic=t, what=what, units=api.used, calls=",".join(f"{k}:{v}" for k, v in sorted(api.calls.items())) or "-",
            left=api.ledger.left() if getattr(api, "ledger", None) is not None else "-")


def quota_view(t):
    """화면 위 할당량 (v1.5): 같은 키의 오늘 사용·남은 양·다음 초기화(한국 시간)·주제별·작업별."""
    kl = key_ledger(t)
    budget = pc.DAILY_LIMIT - pc.DAILY_MARGIN
    if not kl:
        reset, _ = pc.next_quota_reset(datetime.now(timezone.utc), margin_min=0)
        return {"key": None, "used": 0, "left": None, "budget": budget, "exhausted": False, "by_topic": {}, "by_what": {},
                "reset_kst": reset.astimezone(KST).strftime("%m-%d %H:%M"), "topic_used": pc.Ledger(t).used(),
                "day": pc.pacific_day(datetime.now(timezone.utc))}
    q = kl.snapshot()
    q.update(budget=budget, topic_used=int((q.get("by_topic") or {}).get(t, 0)),
             same_key=[x for x in STATE.get("topics") or [] if x != t and key_fp(x) == kl.fp])   # v2.1: 같은 키를 쓰는 다른 주제
    return q


def key_fp(t):
    """이 주제가 쓰는 YouTube 키의 지문 (v2.1 — 주제마다 다른 키인지 보기). 키가 없으면 None. 키 값은 내보내지 않음."""
    key = orr.load_api_key(t)[0]
    return pc.key_fingerprint(key) if key else None


def foreign_ok(t):
    """이 주제는 외국 영상도 탐색·분석하나 (v2.1 — <주제>/analyzer_config.toml [search] INCLUDE_FOREIGN, 기본 꺼짐)."""
    return orr.include_foreign(t, ROOT)


FOREIGN_LINE_RX = re.compile(r"(?m)^[ \t]*INCLUDE_FOREIGN[ \t]*=[^\n]*$")     # 주석 줄(# …)은 건드리지 않음
FOREIGN_NOTE = "# 외국 영상도 탐색·분석 (true) — 기본 false = 한국어 영상만. 웹 화면 4번 칸 [외국 영상도]로 켜고 끔"


def set_include_foreign(t, on):
    """<주제>/analyzer_config.toml 의 INCLUDE_FOREIGN 을 고침 (v2.1). 줄이 있으면 그 줄만, 없으면 [search] 밑에 (없으면 끝에 [search] 와 함께).
    → 고친 파일 내용(bytes). 다른 줄·주석은 그대로."""
    p = ROOT / t / "analyzer_config.toml"
    text = p.read_text("utf-8")
    line = f"INCLUDE_FOREIGN = {'true' if on else 'false'}".ljust(37) + FOREIGN_NOTE
    if FOREIGN_LINE_RX.search(text):
        text = FOREIGN_LINE_RX.sub(lambda m: line, text, count=1)
    elif re.search(r"(?m)^\[search\][ \t]*$", text):
        text = re.sub(r"(?m)^\[search\][ \t]*$", lambda m: m.group(0) + "\n" + line, text, count=1)
    else:
        text = text.rstrip("\n") + "\n\n[search]\n" + line + "\n"
    data = text.encode("utf-8")
    tmp = p.with_name(p.name + ".tmp")
    tmp.write_bytes(data)
    os.replace(tmp, p)
    return data


# ---------------------------------------------------------------- 주제 잠금 (v2.0: 한 화면이 주제 탭 전부를 잠금)
def _window_tag(t):
    return re.sub(r"[^0-9A-Za-z_-]+", "_", str(t)) or "topic"


def _window_paths(t):
    base = ROOT / ".yt_work" / f"web_{_window_tag(t)}"
    return base.with_suffix(".lock"), base.with_suffix(".json")


def topic_window(t):
    """다른 화면(예전 창 포함)이 이 주제를 쓰는 중이면 그 화면 정보 {url, pid, since}, 아니면 None (잠금을 잠깐 잡아 보고 바로 놓음)."""
    if t in LOCKS:
        return None
    lock_p, info_p = _window_paths(t)
    if not lock_p.is_file():
        return None
    f = pc.os_lock(lock_p, 0)
    if f is not None:                 # 아무도 안 잡고 있음 (예전 화면이 꺼짐)
        pc.os_unlock(f)
        return None
    return _read_json(info_p, {}) or {"url": "", "pid": None}


def claim_topic(t):
    """이 화면이 주제 t 를 씀 (v2.0: 여러 주제를 함께 잠금) — 다른 화면이 쓰는 중이면 UserError (그 화면 주소와 함께)."""
    if t in LOCKS:
        return
    lock_p, info_p = _window_paths(t)
    lock_p.parent.mkdir(parents=True, exist_ok=True)
    f = pc.os_lock(lock_p, 0)
    if f is None:
        other = _read_json(info_p, {})
        raise UserError(f"'{t}' 주제는 다른 분석기 화면이 쓰는 중입니다 — {other.get('url') or '그 창'} 을 닫으면 이 탭에서 쓸 수 있어요 "
                        "(예전 판은 주제마다 창이 따로 떴음 — 그 창을 닫으세요)")
    LOCKS[t] = f
    _write_json(info_p, {"topic": t, "url": f"http://127.0.0.1:{STATE['port']}/" if STATE.get("port") else "", "pid": os.getpid(),
                         "since": datetime.now(KST).isoformat(timespec="seconds")})
    log("WINDOW", topic=t, port=STATE.get("port"), note="이 화면의 탭으로 씀 (다른 화면은 이 주제를 못 씀)")


def release_topic(t=None):
    for x in ([t] if t else list(LOCKS)):
        f = LOCKS.pop(x, None)
        if f is not None:
            pc.os_unlock(f)
            try:
                _window_paths(x)[1].unlink()
            except OSError:
                pass


def open_windows():
    """주제마다 누가 쓰나 → [{topic, url, me}] (me = 이 화면의 탭)."""
    out = []
    for t in find_topics():
        if t in LOCKS:
            out.append({"topic": t, "url": f"http://127.0.0.1:{STATE['port']}/", "me": True})
            continue
        w = topic_window(t)
        if w is not None:
            out.append({"topic": t, "url": w.get("url") or "", "me": False})
    return out


def create_topic(folder, name, keywords_text, push=False):
    """새 주제 폴더 (v1.5): <폴더>/analyzer_config.toml(economic 틀에서 주제 이름·폴더만 바꿈)·keywords.txt·keywords.toml(관련어 비움)
    ·analysis_rules.toml(economic 것 복사). 관련어가 비어 있으면 모든 검색 결과를 주제 관련으로 봄 → Claude 에게 '<주제> 검색어 만들어줘'로 다듬기."""
    folder = str(folder or "").strip()
    name = str(name or "").strip() or folder
    if not TOPIC_RX.match(folder):
        raise UserError("폴더 이름은 영어 소문자로 시작하고 영어 소문자·숫자·-·_ 만 (2~31자) — 예: health, side-job")
    d = ROOT / folder
    if (d / "analyzer_config.toml").is_file():
        raise UserError(f"'{folder}' 주제 폴더가 이미 있습니다 — 위 주제 목록에서 고르세요")
    if any(c in name for c in '"\\\n') or len(name) > 40:
        raise UserError("주제 이름은 40자 이하, 따옴표·역슬래시 없이")
    tpl_p = ROOT / "economic" / "analyzer_config.toml"
    if tpl_p.is_file():
        cfg = tpl_p.read_text("utf-8")
        cfg = re.sub(r'(?m)^TOPIC\s*=\s*"[^"]*"', f'TOPIC = "{name}"', cfg)
        cfg = re.sub(r'(?m)^PROJECT_FOLDER\s*=\s*"[^"]*"', f'PROJECT_FOLDER = "{folder}"', cfg)
    else:
        cfg = (f'[topic]\nTOPIC = "{name}"\nPROJECT_FOLDER = "{folder}"\nRESULT_FOLDER = "result"\n\n[github]\nGITHUB_REPO = "yeomin1024/yeomin1024-ytb"\n'
               f'GITHUB_BRANCH = "main"\n\n[search]\nREGION_CODE = "KR"\nLANGUAGE = "ko"\nINCLUDE_FOREIGN = false             # 외국 영상도 탐색·분석 (true) — 기본 false\n\n[keywords]\nKEYWORD_MODE = "curated"\nKEYWORDS_FILE = "keywords.toml"\n')
    cfg = f"# {name} — 웹 화면에서 새로 만든 주제 ({datetime.now(KST).strftime('%Y-%m-%d')}, web_ui {VERSION}, 틀: economic)\n" + cfg
    kws = [k.strip() for k in str(keywords_text or "").splitlines() if k.strip() and not k.strip().startswith("#")]
    files = {
        "analyzer_config.toml": cfg,
        "keywords.txt": f"# {name} 검색어 — 한 줄에 하나 (# 은 메모)\n" + "".join(k + "\n" for k in kws),
        "keywords.toml": (f"# {name} — 관련어(주제와 관련된 영상 가리기)·제외어. 비어 있으면 모든 검색 결과를 주제 관련으로 봄\n"
                          "EXTRA_KEYWORDS = []\nEXCLUDE_KEYWORDS = []\n\n[KEYWORD_GROUPS]\n\n[relevance]\n"
                          "RELEVANCE_TERMS = []\nRELEVANCE_WEAK_TERMS = []\nRELEVANCE_EXCLUDE = []\n"),
    }
    rules = ROOT / "economic" / "analysis_rules.toml"
    if rules.is_file():
        files["analysis_rules.toml"] = rules.read_text("utf-8")
    d.mkdir(parents=True, exist_ok=True)
    for fn, text in files.items():
        (d / fn).write_text(text, "utf-8")
    notes = [f"PC 에 만듦 ({folder}/ — {', '.join(files)})"]
    if push:
        for fn, text in files.items():
            ok, note = github_put(folder, f"{folder}/{fn}", text.encode("utf-8"), f"[{name}] 새 주제 (웹 화면) — {fn}")
            if not ok:
                notes.append(note)
                break
        else:
            notes.append("GitHub 에도 저장")
    log("TOPIC", folder=folder, name=name, keywords=len(kws), note=" · ".join(notes))
    return {"folder": folder, "name": name, "keywords": len(kws), "message": " · ".join(notes)}


def add_target(t, text):
    kind, val = orr.parse_target(text)
    if not kind:
        raise UserError(val)
    tg = load_targets(t)
    now = datetime.now(KST).isoformat(timespec="minutes")
    if kind == "video":
        if any(v["id"] == val for v in tg["videos"]):
            return {"kind": "video", "id": val, "note": "이미 있음"}
        entry = {"id": val, "title": "", "added": now}
        try:
            api, ledger, _ = make_api(t, "web_add")
        except UserError as e:                       # 키가 없거나 할당량이 없어도 추가는 됨 — 제목은 탐색 때
            api, entry["note"] = None, f"제목은 탐색 때 ({e})"
        if api:
            try:
                items = api.videos([val])
            except Exception as e:
                items, entry["note"] = None, f"제목은 탐색 때 ({type(e).__name__})"
            finally:
                record_use(t, api, ledger, "web_add")
            if items == []:
                raise UserError(f"영상을 찾지 못했습니다 (지워졌거나 비공개): {val}")
            if items:
                entry["title"] = items[0]["snippet"].get("title", "")
                entry["channel"] = items[0]["snippet"].get("channelTitle", "")
        tg["videos"].append(entry)
        _write_json(targets_path(t), tg)
        log("TARGET", kind="video", id=val, title=entry.get("title", ""))
        return {"kind": "video", **entry}
    api, ledger, _ = make_api(t, "web_add")
    try:
        ch = orr.resolve_channel(api, kind, val)
    finally:
        record_use(t, api, ledger, "web_add")
    if not ch:
        raise UserError(f"채널을 찾지 못했습니다: {val}")
    if any(c["id"] == ch["id"] for c in tg["channels"]):
        return {"kind": "channel", **ch, "note": "이미 있음"}
    ch["added"] = now
    tg["channels"].append(ch)
    _write_json(targets_path(t), tg)
    log("TARGET", kind="channel", id=ch["id"], title=ch["title"], videos=ch["videos"])
    return {"kind": "channel", **ch}


def add_targets(t, text):
    """여러 개를 한 번에 (한 줄에 하나 — 띄어쓰기·쉼표로 나눠도 됨). → [{input, ok, kind, id, title, note|error}] (v1.1)."""
    items = [x for x in re.split(r"[\s,]+", str(text or "")) if x.strip()]
    if not items:
        raise UserError("빈 칸 — 영상 주소나 채널 주소를 넣으세요")
    out = []
    for x in items[:200]:
        try:
            out.append({"input": x, "ok": True, **add_target(t, x)})
        except UserError as e:
            out.append({"input": x, "ok": False, "error": str(e)})
        except Exception as e:
            out.append({"input": x, "ok": False, "error": f"{type(e).__name__}: {e}"[:160]})
    return out


CASE_RX = re.compile(r"^(?:W_|P?\d\d_)([0-9A-Za-z_-]{11})$")


def used_ids(t):
    """이미 분석에 쓴 영상 (v1.1 — 목록에서 뺌): 웹 화면에서 승인한 W_·성공 사례 01_·조회수 상위 P01_ (빠진 것 _old/ 도) +
    분석기 성공사례(output/…/success_cases). → {영상ID}"""
    ids = set()
    od = out_dir(t)
    for base in (od, od / "_old"):
        if base.is_dir():
            for d in base.iterdir():
                m = CASE_RX.match(d.name)
                if m and d.is_dir() and (d / "metadata.json").is_file():
                    ids.add(m.group(1))
    try:
        sc = pc.read_paths(t)[1] / "success_cases"
        for d in (sc.iterdir() if sc.is_dir() else []):
            vid = _read_json(d / "metadata.json", {}).get("video_id")
            if vid:
                ids.add(vid)
    except Exception:
        pass
    return ids


def remove_target(t, kind, tid):
    tg = load_targets(t)
    key = "channels" if kind == "channel" else "videos"
    tg[key] = [x for x in tg[key] if x["id"] != tid]
    _write_json(targets_path(t), tg)
    return tg


# ---------------------------------------------------------------- 작업 (한 번에 하나, 뒤에서)
def job_view(t):
    return {k: (list(v)[-200:] if k == "log" else v) for k, v in job_of(t).items() if k not in ("proc", "cancel")}


def start_job(name, fn, t, *args):
    """v2.0: 주제 t 의 작업 (주제마다 하나 — 다른 주제 작업은 동시에). fn(t, *args)."""
    job = job_of(t)
    with JOB_LOCK:
        if job["status"] == "running":
            return False, f"'{job['name']}' 작업이 아직 도는 중입니다 — 끝난 뒤 다시"
        job.update(name=name, status="running", step="시작", done=0, total=0, started=datetime.now(KST).isoformat(timespec="seconds"),
                   finished=None, error=None, result=None, cancel=False, proc=None)
        job["log"].clear()

    def runner():
        _TL.job = job
        try:
            job["result"] = fn(t, *args)
            job["status"] = "done"
        except Cancelled:
            job["status"] = "cancelled"
            log("JOB", logging.WARNING, topic=t, name=name, note="사용자가 멈춤 — 받은 것은 캐시·폴더에 남음")
        except UserError as e:
            job.update(status="error", error=str(e))
            log("JOB", logging.WARNING, topic=t, name=name, error=str(e))
        except Exception as e:
            job.update(status="error", error=f"{type(e).__name__}: {e}"[:300])
            LOG.exception("[JOB] %s %s 실패", t, name)
        finally:
            job["finished"] = datetime.now(KST).isoformat(timespec="seconds")
            job["proc"] = None
            _TL.job = None
    threading.Thread(target=runner, daemon=True, name=f"job-{t}-{name}").start()
    return True, "시작"


def step(text, done=None, total=None):
    job = cur_job()
    if job["cancel"]:
        raise Cancelled()
    job["step"] = text
    if done is not None:
        job["done"] = done
    if total is not None:
        job["total"] = total


def run_subprocess(cmd, label, capture=None):
    """도구를 따로 돌리고 출력 줄을 '진행' 칸으로 (멈춤을 누르면 끝냄). capture(목록)가 있으면 출력 줄을 거기에도. → 종료 코드."""
    env = {**os.environ, "PYTHONIOENCODING": "utf-8", "PYTHONUTF8": "1"}
    log("JOB", step=label, cmd=" ".join(str(c) for c in cmd[1:]))
    job = cur_job()
    p = subprocess.Popen(cmd, cwd=ROOT, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    job["proc"] = p
    for raw in p.stdout:
        line = raw.decode("utf-8", errors="replace").rstrip()
        job["log"].append(line)
        if capture is not None:
            capture.append(line)
        if job["cancel"]:
            p.terminate()
    code = p.wait()
    job["proc"] = None
    if job["cancel"]:
        raise Cancelled()
    return code


# ---------------------------------------------------------------- 탐색
def estimate(t, weeks, use_keywords):
    """탐색하면 쓸 검색 할당량 (캐시는 0). → {searches, cached, units, channels}."""
    cache = out_dir(t) / ".cache"
    kws = orr.load_keywords(t, 0)[0] if use_keywords else []
    lang = orr.search_lang(foreign_ok(t))                  # v2.1: 외국 영상을 넣는 주제는 언어 지정 없는 검색 캐시
    total = cached = 0
    for _, q in kws:
        for dur in ("medium", "long"):
            total += 1
            cached += orr.search_is_cached(cache, q, dur, weeks * 7, lang=lang)
    tg = load_targets(t)
    ch_units = sum(max(1, -(-int(c.get("videos") or 50) // 50)) * 2 for c in tg["channels"])   # 목록 + 영상 정보
    q = quota_view(t)
    return {"keywords": len(kws), "searches": total, "cached": cached, "units": (total - cached) * 100 + ch_units + 20,
            "channels": len(tg["channels"]), "videos": len(tg["videos"]), "left": q.get("left"), "reset_kst": q.get("reset_kst")}


def ratio_key(r):
    """배수 높은 순 (구독자 비공개 = 배수 없음은 맨 뒤), 같으면 조회수 많은 순."""
    return (r.get("ratio") is None, -(r.get("ratio") or 0), -(r.get("views") or 0))


def _is_success(r):
    return r["subs"] is not None and r["subs"] <= 50000 and r["views"] >= 10000 and (r["ratio"] or 0) >= 3


def preselect(rows):
    """추천 = 체크만 해 둠: 직접 추가한 영상 · 추가한 채널의 최근 N주 롱폼 · 검색 결과 중 성공 사례(작은 채널)·조회수 상위(주제 관련, 최근 N주 롱폼)."""
    reasons = {}
    searched = [r for r in rows if r["in_window"] and not r["short"] and r["relevant"] and any(s.startswith("검색:") for s in r["sources"])]
    searched_ids = {r["id"] for r in searched}
    for r in sorted(searched, key=lambda r: -r["views"])[:POPULAR_N]:
        reasons[r["id"]] = "조회수 상위"
    for r in rows:
        if "주소" in r["sources"]:
            reasons[r["id"]] = "추가한 영상"
        elif any(s.startswith("채널:") for s in r["sources"]) and r["in_window"] and not r["short"]:
            reasons[r["id"]] = "추가한 채널"
        elif r["id"] in searched_ids and _is_success(r):
            reasons[r["id"]] = "성공 사례"
    return reasons


def job_explore(t, weeks, use_keywords):
    api, ledger, src = make_api(t, "web_explore")
    out = out_dir(t)
    cache = out / ".cache"
    cache.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc)
    days = weeks * 7
    since = (now - timedelta(days=days)).strftime("%Y-%m-%dT00:00:00Z")
    kws, exclude, _, _, rel = orr.load_keywords(t, 0)
    kws = kws if use_keywords else []
    fo = foreign_ok(t)                                           # v2.1: 외국 영상도 (주제 설정 INCLUDE_FOREIGN — 기본 꺼짐)
    lang = orr.search_lang(fo)
    tg = load_targets(t)
    if not kws and not tg["channels"] and not tg["videos"]:
        raise UserError("탐색할 것이 없습니다 — 검색어를 넣거나 영상·채널을 추가하세요")
    found, pending = {}, []
    searched_new = 0
    state = orr.new_state()
    infos = []
    total = len(kws) * 2 + len(tg["channels"]) + 2
    n = 0
    log("EXPLORE", topic=t, weeks=weeks, keywords=len(kws), channels=len(tg["channels"]), videos=len(tg["videos"]), key_source=src,
        quota_left=api.quota, include_foreign=fo, search_lang=lang or orr.ANY_LANG)
    try:
        for g, q in kws:
            for dur in ("medium", "long"):
                n += 1
                step(f"검색 {q} ({'4~20분' if dur == 'medium' else '20분 넘음'})", n, total)
                ttl = {}
                try:
                    ids, hit = orr.cached_search(api, cache, q, since, dur, days, orr.SEARCH_TTL_HOURS, False, info=ttl, lang=lang)
                except orr.QuotaStop:
                    pending.append(f"{q} ({dur})")
                    continue
                for vid in ids:
                    found.setdefault(vid, []).append(f"검색:{q}")
                searched_new += not hit
                log("SEARCH", query=q, dur=dur, results=len(ids), cached=hit, quota_used=api.used,
                    **{k: v for k, v in ttl.items() if v is not None})       # v1.5: 적응형 캐시 시간(ttl_h)·단계·새로 보인 영상
        for ch in tg["channels"]:
            n += 1
            step(f"채널 {ch.get('title') or ch['id']} 영상 목록", n, total)
            try:
                ids = orr.channel_uploads(api, cache, ch)
            except orr.QuotaStop:
                pending.append(f"채널 {ch.get('title')}")
                continue
            for vid in ids:
                found.setdefault(vid, []).append(f"채널:{ch.get('title') or ch['id']}")
        for v in tg["videos"]:
            found.setdefault(v["id"], []).append("주소")
        if kws:                                   # v1.3: 수요 — 사람들이 찾는 말 (YouTube 자동완성, 할당량 0, 7일 캐시)
            ac_fail = ac_new = 0
            for k, (g, q) in enumerate(kws, 1):
                step(f"자동완성(사람들이 찾는 말) {k}/{len(kws)} — {q} (할당량 0)", n, total)
                try:
                    _, hit = orr.fetch_autocomplete(q, cache)
                    if not hit:
                        ac_new += 1
                        time.sleep(0.2)
                except Exception as e:
                    ac_fail += 1
                    if ac_fail == 3:
                        log("AUTOCOMPLETE", logging.WARNING, note="자동완성 연결 실패가 이어짐 — 이번엔 그만 (분석은 자동완성 없이)", error=f"{type(e).__name__}"[:60])
                        break
            log("AUTOCOMPLETE", keywords=len(kws), new=ac_new, failed=ac_fail, note="수요 자료 (할당량 0)")
        step(f"영상 {len(found):,}개 정보·구독자 수", n + 1, total)
        infos = orr.fetch_video_infos(api, cache, list(found), state)
        subs = orr.fetch_channel_subs(api, cache, {i["channel_id"] for i in infos}, state)
    finally:
        record_use(t, api, ledger, "web_explore")
    for i in infos:
        i["subs"] = (subs.get(i["channel_id"]) or {}).get("subs")
    info_by_id = {i["id"]: i for i in infos}
    url_ids = {v["id"] for v in tg["videos"]}                     # 주소로 직접 넣은 영상은 라이브·외국이어도 남김 (표시만)
    excluded = collections.Counter(orr.exclusion_reason(i, fo) for i in infos if i["id"] not in url_ids)
    excluded.pop(None, None)
    rows = []
    for r in orr.build_rows(infos, found, now, keep=url_ids, foreign_ok=fo):
        srcs = list(dict.fromkeys(found.get(r["id"], [])))
        if "주소" not in srcs and any(w in (r["title"] or "") for w in exclude):
            continue
        r.update(sources=srcs, published_at=str(info_by_id[r["id"]].get("published") or ""),
                 relevant=orr.relevant(info_by_id[r["id"]], rel), short=r["minutes"] * 60 < MIN_SEC,
                 in_window=r["age_days"] is not None and r["age_days"] <= days,
                 downloaded=(out / f"W_{r['id']}" / "metadata.json").is_file())
        r["success"] = _is_success(r)
        rows.append(r)
    reasons = preselect(rows)
    for r in rows:
        r["reason"] = reasons.get(r["id"], "")
    rows.sort(key=ratio_key)                                         # 배수 높은 순 (v1.1)
    prev = _read_json(web_dir(t) / "explore.json", {})               # v1.5: 다시 탐색해도(자동 이어서 포함) 전에 있던 영상은 내가 체크한 그대로
    prev_rows, prev_checked = {r["id"] for r in prev.get("rows") or []}, set(prev.get("checked") or [])
    checked = [r["id"] for r in rows if (r["id"] in prev_checked if r["id"] in prev_rows else bool(r["reason"]))]
    data = {"topic": t, "generated": datetime.now(KST).isoformat(timespec="seconds"), "weeks": weeks, "use_keywords": use_keywords,
            "rows": rows, "checked": checked, "pending": pending, "quota_used": api.used,
            "pending_videos": state["pending_videos"], "pending_channels": state["pending_channels"],
            "searched_new": searched_new, "excluded": dict(excluded)}
    _write_json(web_dir(t) / "explore.json", data)
    log("EXPLORE", topic=t, videos=len(rows), checked=len(data["checked"]), kept_checks=len(prev_rows & {r["id"] for r in rows}),
        pending=len(pending), pending_videos=state["pending_videos"], searched_new=searched_new, quota_used=api.used,
        excluded=",".join(f"{k}:{v}" for k, v in excluded.items()) or "-", note="체크만 해 둠 — [승인]을 눌러야 자료를 받음")
    step("끝", total, total)
    return {"videos": len(rows), "checked": len(data["checked"]), "pending": pending, "pending_videos": state["pending_videos"],
            "quota_used": api.used}


# ---------------------------------------------------------------- 승인 → 자료 받기 → 주별 분석 → 음성인식 → 다시 분석 → GitHub
def job_approve(t, ids, auto_whisper=True):
    ex = _read_json(web_dir(t) / "explore.json", {})
    by_id = {r["id"]: r for r in ex.get("rows") or []}
    ids = [i for i in dict.fromkeys(ids) if i in by_id]
    if not ids:
        raise UserError("승인할 영상이 없습니다 — 목록에서 체크하세요 (탐색을 먼저)")
    api, ledger, _ = make_api(t, "web_approve")
    out = out_dir(t)
    cache = out / ".cache"
    a = types.SimpleNamespace(refresh=False, no_transcript=False, offline=False, comments=0, replies=True)
    state = orr.new_state()
    got = []
    log("APPROVE", topic=t, videos=len(ids), note="설명·자막·썸네일·댓글 전부 받음")
    try:
        for n, vid in enumerate(ids, 1):
            step(f"자료 받기 {n}/{len(ids)} — {by_id[vid]['title'][:40]}", n - 1, len(ids))
            info = _read_json(cache / f"{vid}.json", None)
            if not info:
                log("APPROVE", logging.WARNING, id=vid, note="영상 정보 캐시 없음 — 탐색을 다시")
                continue
            d = out / f"W_{vid}"
            row = {k: v for k, v in by_id[vid].items() if k not in ("sources", "reason", "downloaded", "in_window", "relevant", "short", "success")}
            row.update(rank=f"W{n}", set="web", folder=d.name, sources=by_id[vid]["sources"], url=f"https://www.youtube.com/watch?v={vid}")
            meta, cms = orr.deep_case(d, row, info, a, api, "web", {}, state)
            cms, cst = orr.comments_step(d, meta, a, api, "web", {}, state, full=True)
            n_rep = sum(1 for c in cms if c.get("parent"))
            meta.update(comments_fetched=len(cms), comments_top_level=len(cms) - n_rep, comments_replies=n_rep,
                        comments_by_creator=sum(1 for c in cms if c.get("creator")), comments_complete=cst["complete"],
                        comments_disabled=cst.get("disabled", False), approved=datetime.now(KST).isoformat(timespec="minutes"))
            (d / "metadata.json").write_text(json.dumps(meta, ensure_ascii=False, indent=1), "utf-8")
            got.append(meta)
            log("APPROVE", n=f"{n}/{len(ids)}", id=vid, transcript=meta["transcript_status"] if meta["transcript_status"] != "ok" else meta["transcript_lang"],
                comments=len(cms), comments_complete=cst["complete"], quota_used=api.used)
    finally:
        record_use(t, api, ledger, "web_approve")
    appr = _read_json(web_dir(t) / "approved.json", {"approved": []})
    appr["approved"] = list(dict.fromkeys(appr["approved"] + [m["id"] for m in got]))
    _write_json(web_dir(t) / "approved.json", appr)
    missing = [m["id"] for m in got if m["transcript_status"] != "ok"]
    base = job_baseline(t, quiet=True)          # v1.4: 같은 채널 기준선 — 새로 승인한 영상의 채널 최근 영상 (채널 하나 약 2단위)
    # v1.2: 음성인식을 기다리지 않음 — 자막을 못 받은 영상은 설명으로 대신 분석하고 바로 올림, 음성인식은 그 뒤에 뒤에서
    step(f"주별 분석 (자막 못 받은 {len(missing)}개는 영상 설명으로 대신)", len(ids), len(ids))
    rep = wa.run(t)
    got_ids = {m["id"] for m in got}
    src = collections.Counter(c["src"] for c in wa.load_cases(out) if c["meta"].get("id") in got_ids)
    res = {"videos": len(got), "transcripts_ok": len(got) - len(missing), "description_fallback": src.get("설명", 0),
           "no_text": src.get("없음", 0), "whisper_needed": len(missing), "quota_used": api.used,
           "pending_comments": len(state["pending_comments"]), "windows": len(rep["windows"]), **base}
    res.update(push_results(t, f"웹 화면 승인 {len(got)}개 — 자료·주별 분석 (자막 못 받은 {len(missing)}개는 설명으로, 음성인식은 뒤에서)"))
    if missing and auto_whisper:
        res["whisper"] = start_whisper(t, f"승인한 영상 중 자막을 못 받은 {len(missing)}개")[1]
    elif missing:
        res["whisper"] = "자동 음성인식 끔 — 화면의 [음성인식 시작]으로"
    log("APPROVE", topic=t, **{k: v for k, v in res.items()})
    step("끝 — " + ("결과를 GitHub 에 올렸습니다" if res.get("pushed") else res.get("push_note") or "PC 에 저장")
         + (" · 음성인식은 뒤에서 (화면 위 '음성인식')" if missing and auto_whisper else ""))
    return res


def push_results(t, message):
    """분석 결과와 자료(사례 폴더 — 공개 저장소에도, 분석기 v2.9.3)를 바로 GitHub 에 (분석기 --push-only, 다른 올리기와 차례로 — 분석기 v2.9.2 잠금).
    → {pushed, push_exit, push_note, materials}"""
    if not pc.find_secret("GITHUB_TOKEN", t)[0]:
        note = "GITHUB_TOKEN 없음 — 결과는 PC 에만 (화면 위 '1. 키 설정'에서 넣으면 다음부터 올라감)"
        log("PUSH", logging.WARNING, topic=t, note=note)
        return {"pushed": False, "push_note": note}
    step("GitHub 에 올리기 (분석 결과·자료)")
    lines = []                          # 진행 칸(최근 500줄)과 따로 — 승인이 많아 진행 칸이 차 있어도 올리기 출력을 읽게
    code = run_subprocess([sys.executable, "youtube_topic_analyzer.py", "--config", f"{t}/analyzer_config.toml", "--push-only",
                           "--push-message", message], "GitHub", capture=lines)
    out = "\n".join(lines)
    if re.search(r"\bfull=True\b", out):
        materials = "올림 — 사례 폴더(설명·자막·댓글 전부·썸네일)까지" + (" (공개 저장소)" if re.search(r"\bprivate=False\b", out) else "")
    elif re.search(r"\bfull=False\b", out) or "요약 파일만" in out:
        materials = "PC 에만 — 분석기 설정 UPLOAD_CASES_TO_PUBLIC_REPO 가 꺼져 있고 저장소가 공개라 사례 폴더는 올리지 않음"
    else:
        materials = "확인 못 함 (진행 칸의 GitHub 줄 참고)"
    no_change = "변경 사항 없음" in out
    note = ("바뀐 것 없음 (이미 올라가 있음)" if code == 0 and no_change else "GitHub 에 올림" if code == 0
            else f"올리기 실패 (종료 코드 {code}) — 진행 칸의 GitHub 줄 확인, [다시 분석]을 누르면 다시 올림")
    log("PUSH", logging.INFO if code == 0 else logging.WARNING, topic=t, exit=code, note=note, materials=materials)
    return {"pushed": code == 0, "push_exit": code, "push_note": note, "materials": materials}


def job_analyze(t):
    if any(out_dir(t).glob("W_*/metadata.json")):           # v1.6: 롱폼 승인 영상이 없으면(쇼츠만) 롱폼 분석 파일을 빈 것으로 덮지 않음
        step("주별 분석·성공 사례 분석 (자막 없으면 설명으로)")
        rep = wa.run(t)
    else:
        rep = {"windows": [], "cases": 0}
    res = {"windows": len(rep["windows"]), "cases": rep["cases"], "text_sources": rep.get("text_sources")}
    res.update(run_shorts_analysis(t))                      # v1.6: 쇼츠 분석도 (쇼츠 자료가 있을 때만)
    if rep["cases"] or res.get("shorts_cases"):
        res.update(push_results(t, f"웹 화면 분석 다시 (승인 롱폼 {rep['cases']}개 · 쇼츠 {res.get('shorts_cases') or 0}개)"))
    step("끝 — " + (res.get("push_note") or "승인한 영상 없음"))
    return res


def job_comments(t, quiet=False):
    """못 받은 댓글 이어 받기 (v1.3): 승인 영상(W_) 중 댓글을 다 받지 못한 것 — 받은 쪽 다음부터 (comments_state.json),
    할당량이 끝나면 멈추고 다음에 이어서. quiet=True(켤 때)면 키·할당량이 없을 때 오류 대신 건너뜀."""
    todo = []
    for d in sorted(out_dir(t).glob("W_*")) + sorted(shorts_out(t).glob("S_*")):     # v1.6: 쇼츠(S_)도
        m = _read_json(d / "metadata.json", None)
        if m and m.get("id") and not m.get("comments_complete") and not m.get("comments_disabled"):
            todo.append((d, m))
    if not todo:
        return {"comments_todo": 0}
    try:
        api, ledger, _ = make_api(t, "web_comments")
    except UserError as e:
        if not quiet:
            raise
        log("COMMENTS", logging.WARNING, topic=t, todo=len(todo), note=f"못 받은 댓글 이어 받기 건너뜀 — {e}")
        return {"comments_todo": len(todo), "comments_skipped": str(e)}
    a = types.SimpleNamespace(refresh=False, no_transcript=False, offline=False, comments=0, replies=True)
    state = orr.new_state()
    done = got = 0
    log("COMMENTS", topic=t, todo=len(todo), quota_left=api.quota, note="못 받은 댓글 이어 받기")
    try:
        for n, (d, m) in enumerate(todo, 1):
            step(f"못 받은 댓글 이어 받기 {n}/{len(todo)} — {str(m.get('title') or '')[:40]}", n - 1, len(todo))
            cms, cst = orr.comments_step(d, m, a, api, "web", {}, state, full=True)
            n_rep = sum(1 for c in cms if c.get("parent"))
            m.update(comments_fetched=len(cms), comments_top_level=len(cms) - n_rep, comments_replies=n_rep,
                     comments_by_creator=sum(1 for c in cms if c.get("creator")), comments_complete=cst["complete"],
                     comments_disabled=cst.get("disabled", False))
            _write_json(d / "metadata.json", m)
            done += bool(cst["complete"])
            got += len(cms)
            if state["quota_stop"]:
                log("COMMENTS", logging.WARNING, topic=t, note="할당량이 끝나 멈춤 — 다음에 이어서", done=done, left=len(todo) - n)
                break
    finally:
        record_use(t, api, ledger, "web_comments")
    log("COMMENTS", topic=t, todo=len(todo), completed=done, comments=got, quota_used=api.used)
    return {"comments_todo": len(todo), "comments_completed": done, "comments_quota_used": api.used,
            "comments_quota_stop": state["quota_stop"]}


def job_supply(t, n=None):
    """[공급 확인] (v1.3): 분석의 '수요는 있는데 영상이 적어 보이는 말'(analysis.json gap_candidates) n개를 직접 검색 —
    최근 90일·길이 상관없이 조회수 순 (말 하나 = 검색 1번 100단위 + 영상 정보) → 다시 분석·올림."""
    a = _read_json(out_dir(t) / "analysis.json", {})
    words = list(a.get("gap_candidates") or [])
    days = int(((a.get("rules") or {}).get("demand") or {}).get("RECENT_DAYS") or 90)
    if n:
        words = words[:n]
    if not words:
        raise UserError("확인할 말이 없습니다 — 먼저 '검색어로도 찾기'로 탐색해 자동완성(수요)을 받고 다시 분석하세요")
    api, ledger, _ = make_api(t, "web_supply")
    cache = out_dir(t) / ".cache"
    state = orr.new_state()
    done = []
    log("SUPPLY", topic=t, words=len(words), days=days, quota_left=api.quota, note="말 하나 = 검색 1번 100단위")
    try:
        for k, w in enumerate(words, 1):
            step(f"공급 확인 {k}/{len(words)} — '{w}' 최근 {days}일 검색", k - 1, len(words))
            try:
                r = orr.search_supply(api, cache, w, days, state)
            except orr.QuotaStop as e:
                log("SUPPLY", logging.WARNING, note=f"할당량이 끝나 멈춤 — {e}", done=len(done))
                break
            done.append(w)
            log("SUPPLY", word=w, total=r.get("total"), found=len(r.get("ids") or []), cached=r.get("cached"))
    finally:
        record_use(t, api, ledger, "web_supply")
    res = {"supply_checked": len(done), "supply_quota_used": api.used}
    res.update(job_analyze(t))
    return res


BASELINE_VIDEOS = 50                     # 채널마다 최근 영상 몇 개로 '평소'를 셈 (업로드 목록 1단위 + 영상 정보 1단위)
BASELINE_TTL_H = 168                     # 채널 업로드 목록 캐시 7일 (영상 정보는 outlier_research 캐시 24시간)


def job_baseline(t, quiet=False):
    """같은 채널 기준선 (v1.4): 사례(W_·01_·P01_) 채널 중 구독자 ≤ 비교 기준(analysis_rules [compare] MAX_SUBS)인 곳의 최근 영상
    BASELINE_VIDEOS 개 (업로드 목록 + 영상 정보 — 채널 하나 약 2단위, 7일 캐시) → .cache/uploads_<채널ID>.json · .cache/<영상ID>.json
    → 분석(success_analysis 1-2번)이 '채널 평소 대비 ×'와 같은 채널 잘된 영상 vs 평소 영상을 셈. 성공 사례 채널부터, 할당량이 끝나면 멈춤."""
    plan = baseline_plan(t)
    cache, todo, fresh, need, meta_need = plan["cache"], plan["todo"], plan["fresh"], plan["need"], plan["meta_need"]
    res = {"baseline_channels": len(todo), "baseline_cached": len(fresh), "channel_meta_missing": len(meta_need)}
    if not need and not meta_need:
        log("BASELINE", topic=t, channels=len(todo), cached=len(fresh), note="채널 평소 영상·채널 정보 — 모두 캐시")
        return res
    return _baseline_fetch(t, quiet, cache, todo, fresh, need, meta_need, res)


def baseline_plan(t):
    """같은 채널 기준선에서 받을 것 (v1.5: job_baseline 에서 떼어 냄 — 자동 이어서(resume_plan)도 셈). 할당량 0."""
    od = out_dir(t)
    cache = od / ".cache"
    succ = {c.get("id"): c.get("no") or 999 for c in (_read_json(od / "analysis.json", {}).get("success_cases") or [])}
    max_subs = 50000
    try:
        rp = topic_dir(t) / "analysis_rules.toml"
        if rp.is_file():
            max_subs = int(orr.tomllib.loads(rp.read_text("utf-8")).get("compare", {}).get("MAX_SUBS", max_subs))
    except Exception as e:                  # 규칙 파일이 깨져도 기본값으로
        log("BASELINE", logging.WARNING, note=f"analysis_rules.toml 못 읽음 — 구독자 {max_subs} 이하로 — {type(e).__name__}")
    chans = {}
    for d in (od.iterdir() if od.is_dir() else []):
        if not (CASE_RX.match(d.name) and d.is_dir()):
            continue
        m = _read_json(d / "metadata.json", None)
        cid = (m or {}).get("channel_id") or ""
        if not (cid.startswith("UC") and len(cid) == 24):
            continue
        subs = m.get("subs")
        if subs is not None and subs > max_subs:
            continue
        rank = min(succ.get(m.get("id"), 999), chans.get(cid, {}).get("rank", 999))
        chans[cid] = {"id": cid, "uploads": "UU" + cid[2:], "title": m.get("channel") or cid, "rank": rank}
    todo = sorted(chans.values(), key=lambda c: (c["rank"], c["title"]))
    fresh = [c for c in todo if orr._fresh(cache / f"uploads_{c['id']}.json", BASELINE_TTL_H, False)]
    need = [c for c in todo if c not in fresh]
    # 채널 개설일·영상 수 (analysis.md 7번 '빨리 크는 작은 채널') — 탐색에서 본 영상의 채널 중 개설일이 없거나 7일 지난 것 (50채널에 1단위)
    pool = _pool_channels(t)
    try:
        known = _read_json(cache / "channels.json", {})
    except Exception:
        known = {}
    meta_need = sorted(c for c in pool if not (isinstance(known.get(c), dict) and "created" in known[c]))
    return {"cache": cache, "todo": todo, "fresh": fresh, "need": need, "meta_need": meta_need}


def _baseline_fetch(t, quiet, cache, todo, fresh, need, meta_need, res):
    try:
        api, ledger, _ = make_api(t, "web_baseline")
    except UserError as e:
        if not quiet:
            raise
        log("BASELINE", logging.WARNING, topic=t, todo=len(need), note=f"채널 평소 영상 받기 건너뜀 — {e}")
        return {**res, "baseline_skipped": str(e)}
    state = orr.new_state()
    got = 0
    log("BASELINE", topic=t, channels=len(todo), cached=len(fresh), todo=len(need), channel_meta=len(meta_need), quota_left=api.quota,
        note=f"채널 평소 영상 (최근 {BASELINE_VIDEOS}개) — 채널 하나 약 2단위, 성공 사례 채널부터 · 채널 개설일은 50채널에 1단위")
    try:
        if meta_need:
            step(f"채널 정보(개설일·영상 수) {len(meta_need)}곳 — 50곳에 1단위", 0, max(len(need), 1))
            orr.fetch_channel_subs(api, cache, set(meta_need), state)
            res["channel_meta_fetched"] = len(meta_need) - state["pending_channels"]
        for n, c in enumerate(need, 1):
            step(f"채널 평소 영상 {n}/{len(need)} — {c['title'][:30]}", n - 1, len(need))
            try:
                ids = orr.channel_uploads(api, cache, c, ttl_h=BASELINE_TTL_H, max_videos=BASELINE_VIDEOS)
                orr.fetch_video_infos(api, cache, ids[:BASELINE_VIDEOS], state)
            except orr.QuotaStop as e:
                log("BASELINE", logging.WARNING, topic=t, note=f"할당량이 끝나 멈춤 — 다음에 이어서 ({e})", done=got, left=len(need) - n + 1)
                state["quota_stop"] = state["quota_stop"] or getattr(e, "kind", "quota")
                break
            except (RuntimeError, urllib.error.URLError, OSError, ValueError, KeyError) as e:   # 채널이 지워졌거나 비공개 등 — 그 채널만
                log("BASELINE", logging.WARNING, channel=c["title"], id=c["id"], error=f"{type(e).__name__}: {e}"[:160],
                    note="이 채널만 건너뜀")
                continue
            got += 1
            if state["quota_stop"]:
                log("BASELINE", logging.WARNING, topic=t, note="할당량이 끝나 멈춤 — 다음에 이어서", done=got, left=len(need) - n)
                break
    finally:
        record_use(t, api, ledger, "web_baseline")
    log("BASELINE", topic=t, fetched=got, todo=len(need), quota_used=api.used)
    return {**res, "baseline_fetched": got, "baseline_quota_used": api.used, "baseline_quota_stop": state["quota_stop"]}


def _pool_channels(t):
    """탐색에서 본 영상(.cache/<영상ID>.json)의 채널 ID 전부 (v1.4 — 채널 개설일을 받을 대상)."""
    cache = out_dir(t) / ".cache"
    ids = set()
    for f in (cache.glob("*.json") if cache.is_dir() else []):
        if f.name.startswith(("search_", "supply_", "uploads_")) or f.name in ("channels.json", "autocomplete.json"):
            continue
        cid = (_read_json(f, {}) or {}).get("channel_id")
        if isinstance(cid, str) and cid.startswith("UC"):
            ids.add(cid)
    return ids


def job_demand(t, quiet=True):
    """수요 자료 (v1.4): 검색어(keywords.txt)마다 YouTube 자동완성 — 할당량 0, 7일 캐시. 켤 때 저절로 (예전엔 '검색어로도 찾기' 탐색 때만 받아
    탐색을 안 하면 analysis.md 3-3 이 비었음). 연결 실패가 3번 이어지면 그만."""
    qs = pc.read_keyword_list(keywords_path(t)) or []
    cache = out_dir(t) / ".cache"
    cache.mkdir(parents=True, exist_ok=True)
    new = fail = 0
    for k, q in enumerate(qs, 1):
        step(f"자동완성(사람들이 찾는 말) {k}/{len(qs)} — {q} (할당량 0)", k - 1, len(qs))
        try:
            _, hit = orr.fetch_autocomplete(q, cache)
            if not hit:
                new += 1
                time.sleep(0.2)
        except Exception as e:
            fail += 1
            if fail >= 3:
                log("AUTOCOMPLETE", logging.WARNING, note="자동완성 연결 실패가 이어짐 — 이번엔 그만 (분석은 자동완성 없이)", error=type(e).__name__)
                break
    log("AUTOCOMPLETE", topic=t, keywords=len(qs), new=new, failed=fail, note="수요 자료 (할당량 0, 켤 때)")
    return {"autocomplete_keywords": len(qs), "autocomplete_new": new, "autocomplete_failed": fail}


def job_comments_then_analyze(t):
    res = job_comments(t)
    res.update(job_analyze(t))
    return res


def job_startup(t, whisper=True):
    """화면을 켤 때 (v1.2·v1.3·v1.4): 못 받은 댓글 이어 받기 → 채널 평소 영상(같은 채널 기준선)·채널 개설일 → 자동완성(수요, 할당량 0)
    → 승인한 영상이 있으면 분석(주별·성공 사례)을 다시 만들어 올림
    → 자막 없는 영상이 남았으면 음성인식을 뒤에서."""
    res = job_comments(t, quiet=True)
    res.update(job_baseline(t, quiet=True))
    if sh is not None:
        res.update(job_shorts_baseline(t, quiet=True))   # v1.6: 받은 쇼츠의 채널 평소 쇼츠
    res.update(job_demand(t))
    res.update(_resume_explore(t, "켤 때"))         # v1.5: 할당량 때문에 남은 탐색(검색·영상 정보)이 있으면 이어서
    if sh is not None:
        res.update(_resume_shorts_explore(t, "켤 때"))
    if any(out_dir(t).glob("W_*/metadata.json")) or any(shorts_out(t).glob("S_*/metadata.json")):
        res.update(job_analyze(t))
    n = whisper_pending(t, fresh=True)
    res["whisper_pending"] = n
    if n and whisper:
        res["whisper"] = start_whisper(t, f"켤 때 남은 {n}개")[1]
    step("끝 — " + (res.get("push_note") or "올릴 결과 없음") + (f" · 음성인식 {n}개 남음" if n else ""))
    return res


# ---------------------------------------------------------------- 할당량 초기화 뒤 자동으로 이어서 (v1.5)
def resume_plan(t):
    """할당량 때문에 남은 것 (할당량 0으로 셈): 탐색의 못 한 검색·채널·영상 정보 · 못 받은 댓글 · 같은 채널 기준선."""
    ex = _read_json(web_dir(t) / "explore.json", {})
    pend = list(ex.get("pending") or [])
    pv = int(ex.get("pending_videos") or 0) + int(ex.get("pending_channels") or 0)
    comments = 0
    for d in sorted(out_dir(t).glob("W_*")) + sorted(shorts_out(t).glob("S_*")):
        m = _read_json(d / "metadata.json", None)
        if m and m.get("id") and not m.get("comments_complete") and not m.get("comments_disabled"):
            comments += 1
    sx = _read_json(web_dir(t) / "shorts_explore.json", {})                      # v1.6: 쇼츠 탐색·채널 평소 쇼츠
    s_pend = len(sx.get("pending") or []) + int(sx.get("pending_videos") or 0) + int(sx.get("pending_channels") or 0)
    try:
        s_base = len(shorts_baseline_plan(t)["need"]) if sh is not None else 0
    except Exception as e:
        log("RESUME", logging.WARNING, topic=t, note=f"채널 평소 쇼츠 계획 실패 — {type(e).__name__}")
        s_base = 0
    try:
        bp = baseline_plan(t)
        base = len(bp["need"]) + (1 if bp["meta_need"] else 0)
    except Exception as e:                  # 계획을 못 세워도 다른 것은 이어서
        log("RESUME", logging.WARNING, topic=t, note=f"채널 기준선 계획 실패 — {type(e).__name__}")
        base = 0
    plan = {"explore_searches": len(pend), "explore_videos": pv, "explore_weeks": ex.get("weeks"),
            "explore_keywords": ex.get("use_keywords", True), "comments": comments, "baseline": base,
            "shorts_explore": s_pend, "shorts_baseline": s_base}
    plan["any"] = bool(pend or pv or comments or base or s_pend or s_base)
    return plan


def _resume_explore(t, why):
    ex = _read_json(web_dir(t) / "explore.json", {})
    if not (ex.get("pending") or ex.get("pending_videos") or ex.get("pending_channels")):
        return {}
    kl = key_ledger(t)
    need = 100 + orr.SEARCH_RESERVE if ex.get("pending") else 1
    if not kl or kl.left() < need:
        log("RESUME", topic=t, why=why, note="남은 탐색이 있지만 할당량이 모자람 — 다음 초기화 뒤에", left=kl.left() if kl else "-")
        return {"explore_resume": "할당량 모자람 — 다음 초기화 뒤"}
    log("RESUME", topic=t, why=why, pending=len(ex.get("pending") or []), pending_videos=ex.get("pending_videos") or 0,
        note="할당량 때문에 남은 탐색을 이어서 (캐시된 검색은 0단위, 체크는 그대로)")
    r = job_explore(t, int(ex.get("weeks") or 8), bool(ex.get("use_keywords", True)))
    return {"explore_resumed": True, "explore_pending_after": len(r.get("pending") or []), "explore_quota_used": r.get("quota_used")}


def job_resume(t, why="할당량 초기화"):
    """남은 것 이어서 (v1.5 — 사용자 지시 "사용량 초기화되면 자동으로 다시 분석 마저 하는거지? 그렇게 되야해"):
    못 받은 댓글 → 같은 채널 기준선 → 남은 탐색 → 분석 다시·GitHub. 각 단계는 할당량이 끝나면 멈추고 다음 초기화 때 또 이어서."""
    plan = resume_plan(t)
    log("RESUME", topic=t, why=why, **{k: v for k, v in plan.items() if k != "any"})
    res = {"plan": plan}
    res.update(job_comments(t, quiet=True))
    res.update(job_baseline(t, quiet=True))
    res.update(_resume_explore(t, why))
    if sh is not None:                       # v1.6: 쇼츠 — 채널 평소 쇼츠·남은 쇼츠 탐색
        res.update(job_shorts_baseline(t, quiet=True))
        res.update(_resume_shorts_explore(t, why))
    has_cases = any(out_dir(t).glob("W_*/metadata.json")) or any(shorts_out(t).glob("S_*/metadata.json"))
    if has_cases and (plan["comments"] or plan["baseline"] or plan["shorts_baseline"]):
        res.update(job_analyze(t))           # 댓글·기준선이 바뀌었으면 분석을 다시 만들어 올림
    after = resume_plan(t)
    res["left_after"] = {k: v for k, v in after.items() if k != "any"}
    RESUME.update(last=datetime.now(KST).isoformat(timespec="minutes"), last_result=res["left_after"])
    RESUME_T.setdefault(t, {}).update(last=RESUME["last"], last_result=res["left_after"])
    step("끝 — " + ("남은 것 없음" if not after["any"] else "아직 남은 것은 다음 초기화 뒤에 또 이어서"))
    return res


def resume_view(t):
    """v2.0: 화면의 '자동 이어서' — 다음 시각·상태는 모두 같고, 지난번 결과는 탭(주제)마다."""
    return {**RESUME, **RESUME_T.get(t, {})}


def _resume_loop():
    """태평양 자정 + RESUME_MARGIN_MIN 분마다 남은 것을 저절로 이어서 (이 화면이 켜져 있는 동안). PC 가 잠들었다 깨도 벽시계로 다시 셈.
    v2.0: 화면의 탭(주제)마다 차례로 — 그 주제 작업이 도는 중이면 끝나길 기다림."""
    while True:
        try:
            nxt, how = pc.next_quota_reset(datetime.now(timezone.utc), margin_min=RESUME_MARGIN_MIN)
            RESUME.update(next=nxt.astimezone(KST).isoformat(timespec="minutes"), status="waiting")
            while True:
                left_s = (nxt - datetime.now(timezone.utc)).total_seconds()
                if left_s <= 0:
                    break
                time.sleep(min(60.0, left_s))
            for t in [x for x in (STATE["topics"] or [STATE["topic"]]) if x and (x in LOCKS or not LOCKS)]:
                plan = resume_plan(t)
                if not plan["any"]:
                    RESUME_T.setdefault(t, {}).update(last=datetime.now(KST).isoformat(timespec="minutes"), last_result={},
                                                      note="초기화 — 남은 것 없음")
                    log("RESUME", topic=t, note="할당량 초기화 — 이어서 할 것 없음")
                    continue
                RESUME.update(status="waiting_job")
                waited = 0
                while job_of(t)["status"] == "running" and waited < RESUME_JOB_WAIT_H * 3600:
                    time.sleep(30)
                    waited += 30
                RESUME.update(status="started", note="시작")      # v1.6: 작업을 띄우기 전에 적음 (작업이 바로 끝나도 상태가 맞게)
                ok, msg = start_job("할당량 초기화 — 남은 것 이어서", job_resume, t, "할당량 초기화")
                RESUME.update(status="started" if ok else "skipped", note=msg)
                RESUME_T.setdefault(t, {}).update(note=msg)
                log("RESUME", topic=t, started=ok, note=msg, waited_min=waited // 60)
            time.sleep(90)                   # 같은 초기화로 두 번 돌지 않게
        except Exception as e:               # 이어서 하기가 죽지 않게 — 기록하고 다음 초기화에
            LOG.exception("[RESUME] 실패")
            RESUME.update(status="error", note=f"{type(e).__name__}: {e}"[:200])
            time.sleep(300)


# ---------------------------------------------------------------- 음성인식 (뒤에서, v1.2)
def whisper_pending(t, fresh=False):
    """음성인식이 남은 영상 수 — 분석기 대기열과 같은 기준 (W_·01_·P01_ 중 대본 없음·자막 서버 차단·자막 없음 + 앞부분만 한 대본(2차);
    건너뜀·연결 실패·시도 한도를 넘은 것은 뺌). 화면이 자주 물어서 15초 동안은 지난 값."""
    now = time.monotonic()
    if not fresh and _PENDING_CACHE["t"] == t and now - _PENDING_CACHE["at"] < 15:
        return _PENDING_CACHE["n"]
    tag = re.sub(r"[^0-9A-Za-z가-힣]+", "_", str(t)).strip("_") or "topic"
    tried = _read_json(ROOT / ".yt_work" / f"whisper_{tag}.json", {})
    n = 0
    od, sd = out_dir(t), shorts_out(t)
    dirs = list(od.iterdir() if od.is_dir() else []) + list(sd.iterdir() if sd.is_dir() else [])    # v1.6: 쇼츠(S_)도
    for d in dirs:
        m = CASE_RX.match(d.name) or SHORTS_CASE_RX.match(d.name)
        if not (m and d.is_dir() and (d / "metadata.json").is_file()):
            continue
        if (d / "transcript.json").is_file():     # v1.4: 앞부분만 한 대본(partial_sec — 분석기 v2.10.0 1차)은 2차(전체)가 남음 (쇼츠는 '말 없음'도 끝)
            if _read_json(d / "transcript.json", {}).get("partial_sec"):
                rec = tried.get(m.group(1) + "#full") or {}
                n += not (rec.get("done") or rec.get("attempts", 0) >= WHISPER_MAX_ATTEMPTS)
            continue
        st = str(_read_json(d / "metadata.json", {}).get("transcript_status") or "")
        if st == "ok" or st.startswith(SKIP_TRANSCRIPT) or any(w in st for w in NETWORK_FAIL_WORDS):
            continue
        rec = tried.get(m.group(1)) or {}
        if rec.get("done") or rec.get("attempts", 0) >= WHISPER_MAX_ATTEMPTS:
            continue
        n += 1
    _PENDING_CACHE.update(t=t, at=now, n=n)
    return n


def whisper_view(t=None):
    """v2.0: 음성인식은 PC 에서 하나 — topic = 지금 도는 주제, pending = 이 탭(t) 주제의 남은 수, queued = 기다리는 주제."""
    w = {k: (list(v)[-120:] if k == "log" else v) for k, v in WHISPER.items() if k not in ("proc", "stop")}
    t = t or WHISPER["topic"] or STATE["topic"]
    try:
        w["pending"] = whisper_pending(t) if t else 0
    except Exception:
        w["pending"] = None
    w["queued"] = list(WHISPER.get("queued") or [])
    return w


def start_whisper(t, why=""):
    """음성인식을 뒤에서 시작. 이미 도는 중이면 '끝나면 다시'만 표시 (새로 승인한 영상도 이어서). → (시작했나, 설명)."""
    with WHISPER_LOCK:
        if WHISPER["status"] in ("running", "stopping"):
            if WHISPER["topic"] == t:
                WHISPER["rerun"] = True
                return False, "음성인식이 이미 도는 중 — 지금 대기열이 끝나면 새 영상도 이어서"
            if t not in WHISPER["queued"]:                       # v2.0: 다른 주제는 줄을 세움 (PC 에서 한 번에 하나)
                WHISPER["queued"].append(t)
            return False, f"음성인식은 PC 에서 한 번에 하나 — '{WHISPER['topic']}' 이 끝나면 '{t}' 를 이어서 합니다"
        WHISPER.update(status="running", topic=t, started=datetime.now(KST).isoformat(timespec="seconds"), finished=None, current="",
                       done=0, failed=0, total=0, rerun=False, stop=False, last_exit=None, note=why, proc=None, **{"pass": ""})
        WHISPER["log"].clear()
    log("WHISPER", topic=t, note=f"뒤에서 시작 — {why}" if why else "뒤에서 시작")
    threading.Thread(target=_whisper_loop, args=(t,), daemon=True, name="whisper").start()
    return True, "음성인식을 뒤에서 시작 — 성공 사례부터 1차(앞 5분) → 2차(전체), 하나 끝날 때마다 분석을 다시 만들고 15분마다·차수 끝에 올림"


def stop_whisper():
    with WHISPER_LOCK:
        if WHISPER["status"] != "running":
            return False
        WHISPER.update(stop=True, status="stopping", rerun=False, queued=[])      # v2.0: 줄 선 다른 주제도 멈춤
        p = WHISPER.get("proc")
    if p:
        p.terminate()
    log("WHISPER", logging.WARNING, note="사용자가 멈춤 — 끝난 영상의 대본은 남음, 하던 영상은 다음에 처음부터")
    return True


def _whisper_loop(t):
    try:
        while True:
            has_token = bool(pc.find_secret("GITHUB_TOKEN", t)[0])
            cmd = [sys.executable, "youtube_topic_analyzer.py", "--config", f"{t}/analyzer_config.toml", "--whisper-queue"] + \
                  ([] if has_token else ["--no-push"])
            WHISPER.update(done=0, failed=0, total=0, current="", **{"pass": ""})
            code = _whisper_run(cmd)
            WHISPER["last_exit"] = code
            _PENDING_CACHE["at"] = 0.0
            with WHISPER_LOCK:
                again = WHISPER["rerun"] and not WHISPER["stop"]
                WHISPER["rerun"] = False
            if not again:
                break
            log("WHISPER", topic=t, note="새로 승인한 영상도 이어서")
    except Exception as e:
        WHISPER["note"] = f"오류: {type(e).__name__}: {e}"[:200]
        LOG.exception("[WHISPER] 실패")
    finally:
        with WHISPER_LOCK:
            stopped = WHISPER["stop"]
            WHISPER.update(status="stopped" if stopped else "idle", finished=datetime.now(KST).isoformat(timespec="seconds"), proc=None,
                           current="")
        log("WHISPER", topic=t, done=WHISPER["done"], failed=WHISPER["failed"], exit=WHISPER["last_exit"],
            note="멈춤" if stopped else "대기열 끝")
        nxt = None
        with WHISPER_LOCK:                   # v2.0: 줄 선 다른 주제가 있으면 이어서
            if not stopped and WHISPER["queued"]:
                nxt = WHISPER["queued"].pop(0)
        if nxt:
            start_whisper(nxt, f"'{t}' 다음 차례")


def _whisper_run(cmd):
    env = {**os.environ, "PYTHONIOENCODING": "utf-8", "PYTHONUTF8": "1"}
    log("WHISPER", cmd=" ".join(str(c) for c in cmd[1:]))
    p = subprocess.Popen(cmd, cwd=ROOT, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    WHISPER["proc"] = p
    for raw in p.stdout:
        line = raw.decode("utf-8", errors="replace").rstrip()
        WHISPER["log"].append(line)
        m = WHISPER_ITEMS_RX.search(line)
        if m:                           # 차수가 바뀌면 n/전체를 새로 셈 (v1.4 — 분석기 v2.10.0: 1차 앞 5분 → 2차 전체)
            WHISPER.update(total=int(m.group(1)), done=0, failed=0, current="")
            WHISPER["pass"] = (m.group(2) or "").strip('"')
        m = WHISPER_LINE_RX.search(line)
        if m:
            n, total, what, rest = int(m.group(1)), int(m.group(2)), m.group(3), m.group(4)
            WHISPER["total"] = total
            if what == "시작":
                title = re.search(r'title=("([^"]*)"|\S+)', rest)
                WHISPER["current"] = f"{n}/{total} " + ((title.group(2) if title.group(2) is not None else title.group(1)) if title else "")
            elif what == "끝":
                WHISPER["done"] += 1
                _PENDING_CACHE["at"] = 0.0
            elif what == "실패":
                WHISPER["failed"] += 1
        if "이미 도는 중" in line:
            WHISPER["note"] = "다른 창(자동 실행)에서 음성인식이 이미 도는 중 — 그쪽이 하나씩 올림"
        if WHISPER["stop"]:
            p.terminate()
    code = p.wait()
    WHISPER["proc"] = None
    return code


# ---------------------------------------------------------------- 쇼츠 (v1.6)
def shorts_out(t):
    return out_dir(t) / "shorts"


def shorts_cache(t):
    d = out_dir(t) / ".cache" / "shorts"         # .cache 아래 — GitHub 에 올리지 않음 (분석기 OUTLIERS_SKIP_DIRS·.gitignore)
    d.mkdir(parents=True, exist_ok=True)
    return d


def need_sh():
    if sh is None:
        raise UserError("쇼츠 분석 도구(tools/shorts_analysis.py)가 PC 에 없습니다 — 이 창을 닫고 같은 명령으로 다시 켜면 GitHub 최신 코드를 받습니다")
    return sh


def shorts_rules(t):
    """[shorts]·[shorts_compare] 규칙 (analysis_rules.toml — 없으면 shorts_analysis 기본값)."""
    m = need_sh()
    d = {}
    try:
        rp = topic_dir(t) / "analysis_rules.toml"
        d = orr.tomllib.loads(rp.read_text("utf-8")) if rp.is_file() else {}
    except Exception as e:
        log("SHORTS", logging.WARNING, note=f"analysis_rules.toml 못 읽음 — 쇼츠 기본값으로 — {type(e).__name__}")
    out = {}
    for sec, dflt in m.DEFAULT_RULES.items():
        out[sec] = {**dflt, **{k: v for k, v in (d.get(sec) or {}).items() if k in dflt}}
    return out


def shorts_keywords(t, kws):
    """쇼츠 검색어: <주제>/shorts_keywords.txt 가 있으면 그것 (한 줄에 하나), 없으면 롱폼 검색어(keywords.txt) 그대로."""
    p = topic_dir(t) / "shorts_keywords.txt"
    own = pc.read_keyword_list(p) if p.is_file() else None
    return ([("쇼츠", q) for q in own], p.name) if own else (kws, pc.KEYWORD_LIST_FILE)


def shorts_known(t):
    """채널 쇼츠 목록(UUSH)에 있는 영상 ID 전부 — 쇼츠 '확실' 판별용 (할당량 0)."""
    ids = set()
    for f in shorts_cache(t).glob("uploads_*.json"):
        ids.update(_read_json(f, {}).get("ids") or [])
    return ids


def used_shorts_ids(t):
    sd = shorts_out(t)
    return {m.group(1) for d in (sd.iterdir() if sd.is_dir() else []) for m in [SHORTS_CASE_RX.match(d.name)]
            if m and d.is_dir() and (d / "metadata.json").is_file()}


def estimate_shorts(t, weeks, use_keywords):
    kws = shorts_keywords(t, orr.load_keywords(t, 0)[0])[0] if use_keywords else []
    cache = shorts_cache(t)
    lang = orr.search_lang(foreign_ok(t))
    cached = sum(orr.search_is_cached(cache, q, "short", weeks * 7, lang=lang) for _, q in kws)
    tg = load_targets(t)
    ch_units = len(tg["channels"]) * 2
    q = quota_view(t)
    return {"keywords": len(kws), "searches": len(kws), "cached": cached, "units": (len(kws) - cached) * 100 + ch_units + 20,
            "channels": len(tg["channels"]), "videos": len(tg["videos"]), "left": q.get("left"), "reset_kst": q.get("reset_kst")}


def _is_success_short(r, S):
    return (r["subs"] is not None and r["subs"] <= S["MAX_SUBS"] and r["views"] >= S["MIN_VIEWS"] and (r["ratio"] or 0) >= S["MIN_RATIO"]
            and r["age_days"] is not None and S["MIN_AGE_DAYS"] <= r["age_days"] <= S["MAX_AGE_DAYS"])


def preselect_shorts(rows, S):
    """쇼츠 추천 = 체크만: 주소로 넣은 쇼츠 · 추가한 채널의 최근 N주 쇼츠 · 쇼츠 검색 결과 중 성공 쇼츠·조회수 상위(주제 관련, 최근 N주)."""
    reasons = {}
    searched = [r for r in rows if r["in_window"] and r["relevant"] and r.get("flag") != "부풀림 의심" and any(s.startswith("검색:") for s in r["sources"])]
    searched_ids = {r["id"] for r in searched}
    for r in sorted(searched, key=lambda r: -r["views"])[:SHORTS_POPULAR_N]:
        reasons[r["id"]] = "조회수 상위"
    for r in rows:
        if "주소" in r["sources"]:
            reasons[r["id"]] = "추가한 영상"
        elif any(s.startswith("채널:") for s in r["sources"]) and r["in_window"] and r.get("flag") != "부풀림 의심":
            reasons[r["id"]] = "추가한 채널"
        elif r["id"] in searched_ids and r["success"]:
            reasons[r["id"]] = "성공 쇼츠"
    return reasons


def job_shorts_explore(t, weeks, use_keywords):
    """쇼츠 탐색 (v1.6): 검색어마다 쇼츠 검색 1번(4분 미만·조회수 순·최근 N주 — 100단위, 적응형 캐시) + 추가한 채널의 쇼츠 목록(UUSH) + 주소로 넣은
    영상 → 영상 정보(화면비 포함, 50개에 1단위)·구독자 → 3분 이하·세로만 (주소로 넣은 것은 남기고 표시) → web/shorts_explore.json. 자료는 안 받음."""
    S = shorts_rules(t)["shorts"]
    api, ledger, src = make_api(t, "web_shorts_explore")
    cache, main_cache = shorts_cache(t), out_dir(t) / ".cache"
    main_cache.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc)
    days = weeks * 7
    since = (now - timedelta(days=days)).strftime("%Y-%m-%dT00:00:00Z")
    kws, exclude, _, _, rel = orr.load_keywords(t, 0)
    kws, kw_file = shorts_keywords(t, kws)
    kws = kws if use_keywords else []
    fo = foreign_ok(t)                                           # v2.1: 외국 영상도 (주제 설정 INCLUDE_FOREIGN — 기본 꺼짐)
    lang = orr.search_lang(fo)
    tg = load_targets(t)
    if not kws and not tg["channels"] and not tg["videos"]:
        raise UserError("탐색할 것이 없습니다 — 검색어를 넣거나 영상·채널을 추가하세요")
    found, pending, searched_new = {}, [], 0
    state = orr.new_state()
    infos = []
    total, n = len(kws) + len(tg["channels"]) + 2, 0
    log("SHORTS", step="explore", topic=t, weeks=weeks, keywords=len(kws), keywords_file=kw_file, channels=len(tg["channels"]),
        videos=len(tg["videos"]), key_source=src, quota_left=api.quota, include_foreign=fo, search_lang=lang or orr.ANY_LANG)
    try:
        for g, q in kws:
            n += 1
            step(f"쇼츠 검색 {q} (4분 미만 → 3분 이하·세로만)", n, total)
            ttl = {}
            try:
                ids, hit = orr.cached_search(api, cache, q, since, "short", days, orr.SEARCH_TTL_HOURS, False, info=ttl, lang=lang)
            except orr.QuotaStop:
                pending.append(f"{q} (short)")
                continue
            for vid in ids:
                found.setdefault(vid, []).append(f"검색:{q}")
            searched_new += not hit
            log("SEARCH", query=q, dur="short", results=len(ids), cached=hit, quota_used=api.used, **{k: v for k, v in ttl.items() if v is not None})
        for ch in tg["channels"]:
            n += 1
            step(f"채널 {ch.get('title') or ch['id']} 쇼츠 목록", n, total)
            try:
                ids = orr.channel_shorts(api, cache, ch["id"], ttl_h=24, title=ch.get("title") or "")
            except orr.QuotaStop:
                pending.append(f"채널 {ch.get('title')}")
                continue
            for vid in ids:
                found.setdefault(vid, []).append(f"채널:{ch.get('title') or ch['id']}")
        for v in tg["videos"]:
            found.setdefault(v["id"], []).append("주소")
        for k, (g, q) in enumerate(kws, 1):                 # 수요 — 롱폼과 같은 자동완성 캐시 (할당량 0, 이미 받았으면 그대로)
            step(f"자동완성(사람들이 찾는 말) {k}/{len(kws)} — {q} (할당량 0)", n, total)
            try:
                orr.fetch_autocomplete(q, main_cache)
            except Exception:
                break
        step(f"영상 {len(found):,}개 정보(화면비 포함)·구독자 수", n + 1, total)
        infos = orr.fetch_video_infos(api, cache, list(found), state, player=True)
        subs = orr.fetch_channel_subs(api, main_cache, {i["channel_id"] for i in infos}, state)
    finally:
        record_use(t, api, ledger, "web_shorts_explore")
    known = shorts_known(t)
    url_ids = {v["id"] for v in tg["videos"]}
    excluded, rows, excluded_note = collections.Counter(), [], collections.Counter()
    for i in infos:
        i["subs"] = (subs.get(i["channel_id"]) or {}).get("subs")
        why = orr.exclusion_reason(i, fo)
        ok, basis = orr.is_short(i, known)
        if i["id"] not in url_ids:
            if why:
                excluded[why] += 1
                continue
            if not ok:
                excluded["쇼츠 아님 (" + basis + ")"] += 1
                continue
        srcs = list(dict.fromkeys(found.get(i["id"], [])))
        if "주소" not in srcs and any(w in (i.get("title") or "") for w in exclude):
            continue
        try:
            pub = datetime.fromisoformat(str(i["published"]).replace("Z", "+00:00"))
            age = (now - pub).days
        except (ValueError, TypeError):
            age = None
        sec, views, sb = int(i.get("duration") or 0), int(i.get("view_count") or 0), i["subs"]
        r = {"id": i["id"], "title": i.get("title") or "", "channel": i.get("channel") or "", "channel_id": i.get("channel_id") or "",
             "subs": sb, "views": views, "ratio": round(views / max(sb, 100), 2) if sb else None, "age_days": age,
             "views_per_day": round(views / max(age or 1, 1), 1), "minutes": round(sec / 60, 1), "seconds": sec,
             "likes": i.get("like_count"), "comments": i.get("comment_count"), "published": str(i.get("published") or "")[:10],
             "published_at": str(i.get("published") or ""), "queries": " | ".join(srcs), "url": f"https://www.youtube.com/shorts/{i['id']}",
             "flag": why or ("" if ok else "쇼츠 아님?"), "sources": srcs, "relevant": orr.relevant(i, rel), "short": False,
             "short_basis": basis, "in_window": age is not None and age <= days,
             "downloaded": (shorts_out(t) / f"S_{i['id']}" / "metadata.json").is_file(), "hashtags": len(orr.hashtags(i.get("title"), i.get("description")))}
        ad = sh.ad_suspect(r, S)              # 조회수 부풀림 의심 — 광고 또는 반복 재생 (2026-10-15 실측: 6초·좋아요 0.04%) — 표시만, 추천 안 함
        if ad and not r["flag"]:
            r["flag"] = "부풀림 의심"
            excluded_note["조회수 부풀림 의심 — 광고·반복 재생 (표시만, 추천 안 함)"] += 1
        if fo and not r["flag"] and orr.is_foreign(i):     # v2.1: 외국 영상을 넣는 주제 — 표시만 (추천·성공 판정은 그대로)
            r["flag"] = orr.FOREIGN
        r["success"] = ok and not ad and _is_success_short(r, S)
        rows.append(r)
    reasons = preselect_shorts(rows, S)
    for r in rows:
        r["reason"] = reasons.get(r["id"], "")
    rows.sort(key=ratio_key)
    p = web_dir(t) / "shorts_explore.json"
    prev = _read_json(p, {})
    prev_rows, prev_checked = {r["id"] for r in prev.get("rows") or []}, set(prev.get("checked") or [])
    checked = [r["id"] for r in rows if (r["id"] in prev_checked if r["id"] in prev_rows else bool(r["reason"]))]
    data = {"topic": t, "mode": "shorts", "generated": datetime.now(KST).isoformat(timespec="seconds"), "weeks": weeks, "use_keywords": use_keywords,
            "keywords_file": kw_file, "rows": rows, "checked": checked, "pending": pending, "quota_used": api.used,
            "pending_videos": state["pending_videos"], "pending_channels": state["pending_channels"], "searched_new": searched_new,
            "excluded": {**dict(excluded), **dict(excluded_note)}}
    _write_json(p, data)
    log("SHORTS", step="explore", topic=t, shorts=len(rows), checked=len(checked), success=sum(1 for r in rows if r["success"]),
        pending=len(pending), pending_videos=state["pending_videos"], searched_new=searched_new, quota_used=api.used,
        excluded=",".join(f"{k}:{v}" for k, v in (excluded + excluded_note).items()) or "-", note="체크만 해 둠 — [승인]을 눌러야 자료를 받음")
    step("끝", total, total)
    return {"videos": len(rows), "checked": len(checked), "pending": pending, "pending_videos": state["pending_videos"], "quota_used": api.used}


def job_shorts_approve(t, ids, auto_whisper=True):
    """쇼츠 승인 (v1.6): 체크한 쇼츠만 설명·자막(시도)·표지(세로 먼저)·댓글 전부 → shorts/S_<영상ID>/ → 채널 평소 쇼츠 → 쇼츠 분석 → GitHub
    → 자막을 못 받은 쇼츠는 음성인식(뒤에서, 쇼츠 먼저)."""
    need_sh()
    ex = _read_json(web_dir(t) / "shorts_explore.json", {})
    by_id = {r["id"]: r for r in ex.get("rows") or []}
    ids = [i for i in dict.fromkeys(ids) if i in by_id]
    if not ids:
        raise UserError("승인할 쇼츠가 없습니다 — [쇼츠] 목록에서 체크하세요 (쇼츠 탐색을 먼저)")
    api, ledger, _ = make_api(t, "web_shorts_approve")
    sdir, cache = shorts_out(t), shorts_cache(t)
    a = types.SimpleNamespace(refresh=False, no_transcript=False, offline=False, comments=0, replies=True)
    state = orr.new_state()
    known = shorts_known(t)
    got = []
    log("SHORTS", step="approve", topic=t, shorts=len(ids), note="설명·자막·표지·댓글 전부 받음")
    try:
        for n, vid in enumerate(ids, 1):
            step(f"쇼츠 자료 받기 {n}/{len(ids)} — {by_id[vid]['title'][:40]}", n - 1, len(ids))
            info = _read_json(cache / f"{vid}.json", None)
            if not info:
                log("SHORTS", logging.WARNING, id=vid, note="영상 정보 캐시 없음 — 쇼츠 탐색을 다시")
                continue
            d = sdir / f"S_{vid}"
            d.mkdir(parents=True, exist_ok=True)
            th = d / "thumbnail.jpg"
            cover = None
            if not (th.is_file() and th.stat().st_size > 0):
                cover = orr.shorts_cover(vid, th)                  # 세로 표지 먼저 (deep_case 는 있으면 다시 받지 않음)
            row = {k: v for k, v in by_id[vid].items() if k not in ("sources", "reason", "downloaded", "in_window", "relevant", "short", "success")}
            row.update(rank=f"S{n}", set="web_shorts", folder=d.name, sources=by_id[vid]["sources"], url=f"https://www.youtube.com/shorts/{vid}")
            meta, cms = orr.deep_case(d, row, info, a, api, "web_shorts", {}, state)
            cms, cst = orr.comments_step(d, meta, a, api, "web_shorts", {}, state, full=True)
            n_rep = sum(1 for c in cms if c.get("parent"))
            ok, basis = orr.is_short(info, known)
            old = _read_json(d / "metadata.json", {})
            meta.update(comments_fetched=len(cms), comments_top_level=len(cms) - n_rep, comments_replies=n_rep,
                        comments_by_creator=sum(1 for c in cms if c.get("creator")), comments_complete=cst["complete"],
                        comments_disabled=cst.get("disabled", False), approved=datetime.now(KST).isoformat(timespec="minutes"), kind="shorts",
                        seconds=int(info.get("duration") or 0), published_at=str(info.get("published") or ""), short_basis=basis,
                        embed_w=info.get("embed_w"), embed_h=info.get("embed_h"), hashtags=orr.hashtags(info.get("title"), info.get("description")),
                        cover=cover or old.get("cover") or ("hqdefault.jpg" if th.is_file() and th.stat().st_size > 0 else ""))
            _write_json(d / "metadata.json", meta)
            got.append(meta)
            log("SHORTS", step="approve", n=f"{n}/{len(ids)}", id=vid, seconds=meta["seconds"], cover=meta["cover"] or "-",
                transcript=meta["transcript_status"] if meta["transcript_status"] != "ok" else meta["transcript_lang"],
                comments=len(cms), comments_complete=cst["complete"], quota_used=api.used)
    finally:
        record_use(t, api, ledger, "web_shorts_approve")
    appr = _read_json(web_dir(t) / "shorts_approved.json", {"approved": []})
    appr["approved"] = list(dict.fromkeys(appr["approved"] + [m["id"] for m in got]))
    _write_json(web_dir(t) / "shorts_approved.json", appr)
    missing = [m["id"] for m in got if m["transcript_status"] != "ok"]
    base = job_shorts_baseline(t, quiet=True)
    step(f"쇼츠 분석 (자막 못 받은 {len(missing)}개는 음성인식 뒤에 다시 셈)", len(ids), len(ids))
    res = {"videos": len(got), "transcripts_ok": len(got) - len(missing), "whisper_needed": len(missing), "quota_used": api.used,
           "pending_comments": len(state["pending_comments"]), **base, **run_shorts_analysis(t)}
    res.update(push_results(t, f"웹 화면 쇼츠 승인 {len(got)}개 — 자료·쇼츠 분석 (자막 못 받은 {len(missing)}개는 음성인식 뒤에서)"))
    if missing and auto_whisper:
        res["whisper"] = start_whisper(t, f"승인한 쇼츠 중 자막을 못 받은 {len(missing)}개")[1]
    elif missing:
        res["whisper"] = "자동 음성인식 끔 — 화면의 [음성인식 시작]으로"
    log("SHORTS", step="approve", topic=t, **{k: v for k, v in res.items()})
    step("끝 — " + ("결과를 GitHub 에 올렸습니다" if res.get("pushed") else res.get("push_note") or "PC 에 저장")
         + (" · 음성인식은 뒤에서 (화면 위 '음성인식')" if missing and auto_whisper else ""))
    return res


def shorts_baseline_plan(t):
    """채널 평소 쇼츠 (v1.6)에서 받을 것 — 받은 쇼츠(S_)의 채널 중 구독자 ≤ [shorts_compare] MAX_SUBS (할당량 0으로 셈)."""
    try:
        max_subs = int(shorts_rules(t)["shorts_compare"]["MAX_SUBS"])
    except UserError:
        return {"todo": [], "need": []}
    cache = shorts_cache(t)
    chans = {}
    sd = shorts_out(t)
    for d in (sd.iterdir() if sd.is_dir() else []):
        if not (SHORTS_CASE_RX.match(d.name) and d.is_dir()):
            continue
        m = _read_json(d / "metadata.json", None) or {}
        cid = m.get("channel_id") or ""
        if not (cid.startswith("UC") and len(cid) == 24) or (m.get("subs") is not None and m["subs"] > max_subs):
            continue
        chans[cid] = {"id": cid, "title": m.get("channel") or cid, "views": max(int(m.get("views") or 0), chans.get(cid, {}).get("views", 0))}
    todo = sorted(chans.values(), key=lambda c: -c["views"])
    need = [c for c in todo if not orr._fresh(cache / f"uploads_{c['id']}.json", SHORTS_BASELINE_TTL_H, False)]
    return {"todo": todo, "need": need}


def job_shorts_baseline(t, quiet=False):
    """채널 평소 쇼츠 (v1.6): 받은 쇼츠의 채널마다 쇼츠 목록(UUSH) 최근 SHORTS_BASELINE_VIDEOS 개 + 영상 정보 — 채널 하나 약 2단위, 7일 캐시
    → 쇼츠 분석 1-2번 '채널 평소 쇼츠 대비 ×'·잘된 쇼츠 vs 평소 쇼츠. 조회수 큰 쇼츠의 채널부터, 할당량이 끝나면 멈춤."""
    plan = shorts_baseline_plan(t)
    todo, need = plan["todo"], plan["need"]
    res = {"shorts_baseline_channels": len(todo), "shorts_baseline_cached": len(todo) - len(need)}
    if not need:
        return res
    try:
        api, ledger, _ = make_api(t, "web_shorts_baseline")
    except UserError as e:
        if not quiet:
            raise
        log("SHORTS", logging.WARNING, step="baseline", topic=t, todo=len(need), note=f"채널 평소 쇼츠 받기 건너뜀 — {e}")
        return {**res, "shorts_baseline_skipped": str(e)}
    cache = shorts_cache(t)
    state = orr.new_state()
    got = 0
    log("SHORTS", step="baseline", topic=t, channels=len(todo), todo=len(need), quota_left=api.quota,
        note=f"채널 평소 쇼츠 (쇼츠 목록 최근 {SHORTS_BASELINE_VIDEOS}개) — 채널 하나 약 2단위")
    try:
        for n, c in enumerate(need, 1):
            step(f"채널 평소 쇼츠 {n}/{len(need)} — {c['title'][:30]}", n - 1, len(need))
            try:
                ids = orr.channel_shorts(api, cache, c["id"], ttl_h=SHORTS_BASELINE_TTL_H, max_videos=SHORTS_BASELINE_VIDEOS, title=c["title"])
                orr.fetch_video_infos(api, cache, ids[:SHORTS_BASELINE_VIDEOS], state, player=True)
            except orr.QuotaStop as e:
                log("SHORTS", logging.WARNING, step="baseline", topic=t, note=f"할당량이 끝나 멈춤 — 다음에 이어서 ({e})", done=got, left=len(need) - n + 1)
                break
            except (RuntimeError, urllib.error.URLError, OSError, ValueError, KeyError) as e:
                log("SHORTS", logging.WARNING, step="baseline", channel=c["title"], id=c["id"], error=f"{type(e).__name__}: {e}"[:160], note="이 채널만 건너뜀")
                continue
            got += 1
            if state["quota_stop"]:
                break
    finally:
        record_use(t, api, ledger, "web_shorts_baseline")
    log("SHORTS", step="baseline", topic=t, fetched=got, todo=len(need), quota_used=api.used)
    return {**res, "shorts_baseline_fetched": got, "shorts_baseline_quota_used": api.used}


def has_shorts(t):
    return bool(used_shorts_ids(t)) or any(shorts_cache(t).glob("search_*.json"))


def run_shorts_analysis(t):
    """쇼츠 분석 (tools/shorts_analysis.py — 할당량 0) → 요약 숫자. 쇼츠 자료가 없거나 도구가 없으면 건너뜀 (롱폼 작업을 멈추지 않음)."""
    if sh is None or not has_shorts(t):
        return {}
    step("쇼츠 분석 (shorts/analysis.md)")
    try:
        d = sh.run(t)
    except Exception as e:
        LOG.exception("[SHORTS] 쇼츠 분석 실패")
        return {"shorts_analysis_error": f"{type(e).__name__}: {e}"[:200]}
    if not d:
        return {}
    return {"shorts_success": len(d.get("success_cases") or []), "shorts_cases": d["sources"]["case_folders"],
            "shorts_compare": d["sources"]["compare_group"]}


def _resume_shorts_explore(t, why):
    ex = _read_json(web_dir(t) / "shorts_explore.json", {})
    if not (ex.get("pending") or ex.get("pending_videos") or ex.get("pending_channels")):
        return {}
    kl = key_ledger(t)
    need = 100 + orr.SEARCH_RESERVE if ex.get("pending") else 1
    if not kl or kl.left() < need:
        log("RESUME", topic=t, why=why, note="남은 쇼츠 탐색이 있지만 할당량이 모자람 — 다음 초기화 뒤에", left=kl.left() if kl else "-")
        return {"shorts_explore_resume": "할당량 모자람 — 다음 초기화 뒤"}
    log("RESUME", topic=t, why=why, pending=len(ex.get("pending") or []), note="할당량 때문에 남은 쇼츠 탐색을 이어서 (체크는 그대로)")
    r = job_shorts_explore(t, int(ex.get("weeks") or 8), bool(ex.get("use_keywords", True)))
    return {"shorts_explore_resumed": True, "shorts_explore_pending_after": len(r.get("pending") or [])}


def shorts_view(t):
    """6번 칸 쇼츠 분석 요약 (shorts/analysis.json)."""
    a = _read_json(shorts_out(t) / "analysis.json", {})
    if not a:
        return {"generated": None}
    sp, src = a.get("speech") or {}, a.get("sources") or {}
    eng = a.get("engagement") or {}
    return {"generated": a.get("generated"), "success": len(a.get("success_cases") or []), "cases": src.get("case_folders"),
            "text_sources": src.get("text_sources"), "compare_group": src.get("compare_group"), "compare_rate": src.get("compare_rate"),
            "pool_shorts": src.get("pool_shorts"), "limits": a.get("limits"), "missing_ids": [x["id"] for x in a.get("missing_success") or []],
            "missing_total": a.get("missing_success_total"),
            "seconds": {"success": (eng.get("success_cases") or {}).get("seconds_median"), "others": (eng.get("others") or {}).get("seconds_median")},
            "hooks": {k: [((sp.get("success") or {}).get("hook_types") or {}).get(k), ((sp.get("others") or {}).get("hook_types") or {}).get(k)]
                      for k in ((sp.get("success") or {}).get("hook_types") or {})},
            "first_speech": [(sp.get("success") or {}).get("first_speech_sec"), (sp.get("others") or {}).get("first_speech_sec")],
            "formats": [(r["format"].split(" (")[0], r.get("success_share"), r.get("rate"), r.get("n")) for r in a.get("formats") or []],
            "needs": [(c["name"], c["count"]) for c in (a.get("needs") or {}).get("categories") or []],
            "requests": (a.get("needs") or {}).get("requests_total"),
            "gaps": [(r["phrase"], r["shorts_recent"]) for r in ((a.get("market") or {}).get("autocomplete") or [])[:8]],
            "market_themes": [(r["theme"], r["index"], r["videos"]) for r in (a.get("market") or {}).get("themes") or [] if not r.get("small_sample")][:6],
            "baseline": {k: (a.get("baseline") or {}).get(k) for k in ("success_covered", "channels", "hits", "normal")},
            "channel_types": [(r["type"].split(" (")[0], r.get("rate"), r.get("n")) for r in a.get("channel_types") or []]}


# ---------------------------------------------------------------- 화면 상태
def state_view(t):
    ex = _read_json(web_dir(t) / "explore.json", {})
    kp = keywords_path(t)
    text = kp.read_text("utf-8-sig") if kp.is_file() else ""
    until = orr.caption_blocked()
    STATE["topics"] = sorted(set(find_topics()) | {t}, key=lambda x: (x != "economic", x))     # v1.5: 새로 만든 주제 폴더도
    wins = open_windows()
    other = next((w for w in wins if w["topic"] == t and not w["me"]), None)
    return {"version": VERSION, "topic": t, "name": topic_name(t), "topics": STATE["topics"], "env": env_view(t),
            "topic_names": {x: topic_name(x) for x in STATE["topics"]}, "windows": wins, "port": STATE.get("port"),
            "locked_elsewhere": (other or {}).get("url") or (bool(other) or None),                  # v2.0: 다른 화면이 쓰는 주제 — 보기만
            "env_file": f"{t}/.env",
            "include_foreign": foreign_ok(t),                                                       # v2.1: 이 주제 설정 (기본 꺼짐)
            "resume": {**resume_view(t), "plan": resume_plan(t)},
            "keywords_text": text, "keywords_count": len(pc.read_keyword_list(kp) or []), "targets": load_targets(t),
            "explore": {"generated": ex.get("generated"), "weeks": ex.get("weeks"), "videos": len(ex.get("rows") or []),
                        "checked": len(ex.get("checked") or []), "pending": ex.get("pending") or []},
            "shorts": {"available": sh is not None, "approved": len(used_shorts_ids(t)),
                       "keywords_file": shorts_keywords(t, [])[1] if sh is not None else None},
            "quota": quota_view(t),
            "caption_block": until.astimezone(KST).strftime("%m-%d %H:%M") if until else None,
            "approved": len(_read_json(web_dir(t) / "approved.json", {"approved": []})["approved"]),
            "job": job_view(t), "tabs": tabs_view()}


def tabs_view():
    """v2.0: 탭마다 작업 상태 (탭 이름 옆 점) — {주제: running|done|error|idle}."""
    return {x: job_of(x)["status"] for x in STATE["topics"]}


PAGE = None      # 아래 HTML (파일 끝)


class Handler(BaseHTTPRequestHandler):
    server_version = "AnalyzerUI/" + VERSION

    def log_message(self, fmt, *args):          # 접속 기록은 남기지 않음 (화면이 1초마다 묻기 때문)
        pass

    def _send(self, code, body, ctype="application/json; charset=utf-8"):
        data = body if isinstance(body, bytes) else json.dumps(body, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(data)

    def _host_ok(self):
        host = (self.headers.get("Host") or "").split(":")[0]
        return host in ("127.0.0.1", "localhost")

    def _authorized(self):
        return self._host_ok() and secrets.compare_digest(self.headers.get("X-Token") or "", TOKEN)

    def _topic(self):
        """v2.0: 요청의 탭(주제) — X-Topic 머리글 (없거나 틀리면 처음 탭)."""
        hdr = getattr(self, "headers", None)
        want = ((hdr.get("X-Topic") if hdr is not None else "") or "").strip()
        if want and TOPIC_RX.match(want) and (ROOT / want / "analyzer_config.toml").is_file():
            return want
        return STATE["topic"]

    def do_GET(self):
        if not self._host_ok():
            return self._send(403, {"error": "이 PC 에서만 열 수 있습니다"})
        u = urllib.parse.urlparse(self.path)
        if u.path in ("/", "/index.html"):
            return self._send(200, PAGE.replace("{{TOKEN}}", TOKEN).encode("utf-8"), "text/html; charset=utf-8")
        if u.path == "/favicon.ico":                         # 브라우저가 저절로 묻는 아이콘 — 없음 (403 오류로 보이지 않게)
            self.send_response(204)
            self.end_headers()
            return
        if not self._authorized():
            return self._send(403, {"error": "열쇠가 맞지 않음 — 화면을 새로 고침"})
        t = self._topic()
        q = urllib.parse.parse_qs(u.query)
        try:
            if u.path == "/api/state":
                return self._send(200, state_view(t))
            if u.path == "/api/job":                                   # v1.5: 남은 할당량·자동 이어서도 (화면이 1~3초마다 물음)
                return self._send(200, {**job_view(t), "whisper": whisper_view(t), "quota": quota_view(t),
                                        "resume": resume_view(t), "tabs": tabs_view(), "topic": t})
            if u.path == "/api/explore":
                shorts = (q.get("mode") or [""])[0] == "shorts"        # v1.6: 쇼츠 목록
                ex = _read_json(web_dir(t) / ("shorts_explore.json" if shorts else "explore.json"), {})
                used = used_shorts_ids(t) if shorts else used_ids(t)   # 이미 분석에 쓴 영상은 뺌 (승인하면 바로 빠짐)
                rows = sorted((r for r in ex.get("rows") or [] if r["id"] not in used), key=ratio_key)
                return self._send(200, {"rows": rows, "checked": [i for i in ex.get("checked") or [] if i not in used],
                                        "generated": ex.get("generated"), "weeks": ex.get("weeks"), "excluded": ex.get("excluded") or {},
                                        "used_hidden": sum(1 for r in ex.get("rows") or [] if r["id"] in used), "mode": "shorts" if shorts else "long",
                                        "keywords_file": ex.get("keywords_file")})
            if u.path == "/api/estimate":
                weeks = max(1, min(52, int((q.get("weeks") or ["8"])[0])))
                if (q.get("mode") or [""])[0] == "shorts":
                    need_sh()
                    return self._send(200, estimate_shorts(t, weeks, (q.get("kw") or ["1"])[0] == "1"))
                return self._send(200, estimate(t, weeks, (q.get("kw") or ["1"])[0] == "1"))
            if u.path == "/api/shorts_analysis":               # v1.6: 쇼츠 분석 요약 (전문은 shorts/analysis.md)
                return self._send(200, shorts_view(t))
            if u.path == "/api/report":
                return self._send(200, _read_json(out_dir(t) / "weekly.json", {}))
            if u.path == "/api/analysis":                      # v1.3: 성공 사례 분석 요약 (전문은 analysis.md)
                a = _read_json(out_dir(t) / "analysis.json", {})
                return self._send(200, {k: a.get(k) for k in ("generated", "sources", "limits", "missing_success_total", "tool", "gap_candidates")}
                                  | {"success": len(a.get("success_cases") or []),
                                     "missing_ids": [x["id"] for x in a.get("missing_success") or []],
                                     "needs": [(c["name"], c["count"]) for c in (a.get("needs") or {}).get("categories") or []],
                                     "market_themes": [(r["theme"], r["index"], r["videos"]) for r in (a.get("market") or {}).get("themes") or []
                                                       if not r.get("small_sample")][:6],
                                     "gaps": [(r["phrase"], r["pool_recent"], (r.get("verified") or {}).get("total"))
                                              for r in ((a.get("market") or {}).get("autocomplete") or [])[:8]],
                                     "fast_channels": len((a.get("growth") or {}).get("fast") or []),
                                     "baseline": {k: (a.get("baseline") or {}).get(k) for k in ("success_covered", "channels", "hits", "normal")},
                                     "formats": [(r["format"].split(" (")[0], r.get("success_share"), r.get("market_index")) for r in a.get("formats") or []],
                                     "requests": (a.get("needs") or {}).get("requests_total")})
        except UserError as e:
            return self._send(400, {"error": str(e)})
        except Exception as e:
            LOG.exception("GET %s", u.path)
            return self._send(500, {"error": f"{type(e).__name__}: {e}"[:300]})
        return self._send(404, {"error": "없는 주소"})

    def do_POST(self):
        if not self._authorized():
            return self._send(403, {"error": "열쇠가 맞지 않음 — 화면을 새로 고침"})
        n = int(self.headers.get("Content-Length") or 0)
        if n > 2_000_000:
            return self._send(413, {"error": "너무 큼"})
        try:
            body = json.loads(self.rfile.read(n).decode("utf-8") or "{}")
        except ValueError:
            return self._send(400, {"error": "JSON 이 아님"})
        t = self._topic()
        path = urllib.parse.urlparse(self.path).path
        try:
            if path != "/api/topic/new" and t not in LOCKS:           # v2.0: 이 화면이 아직 안 잡은 탭(새로 만든 주제 등)은 지금 잡음
                claim_topic(t)                                         # 다른 화면이 쓰는 중이면 UserError — 그 탭은 보기만
            if path == "/api/topic/new":                               # v1.5: 새 주제 폴더
                r = create_topic(body.get("folder"), body.get("name"), body.get("keywords"), bool(body.get("push")))
                try:                                                   # v2.0: 새 주제도 탭으로 — 키 파일 따로·잠금
                    pc.ensure_topic_env(r["folder"])
                    claim_topic(r["folder"])
                except Exception as e:
                    log("TOPIC", logging.WARNING, topic=r.get("folder"), note="새 주제 탭 준비 실패", error=f"{type(e).__name__}: {e}"[:160])
                return self._send(200, r)
            if path == "/api/foreign":                                 # v2.1: [외국 영상도] — 이 주제 설정 INCLUDE_FOREIGN
                if job_of(t)["status"] == "running":
                    raise UserError(f"'{job_of(t)['name']}' 작업이 도는 중 — 끝난 뒤(또는 [멈춤] 뒤)에 바꾸세요")
                on = body.get("on") is True
                if foreign_ok(t) == on:
                    return self._send(200, {"ok": True, "include_foreign": on, "message": "이미 " + ("켜져" if on else "꺼져") + " 있습니다"})
                data = set_include_foreign(t, on)
                ok, note = github_put(t, f"{t}/analyzer_config.toml", data,
                                      f"[{topic_name(t)}] 외국 영상 {'켬' if on else '끔'} — INCLUDE_FOREIGN = {'true' if on else 'false'} (웹 화면)")
                log("SETTINGS", topic=t, include_foreign=on, file=f"{t}/analyzer_config.toml", github=note)
                msg = (("켬 — 다음 탐색부터 외국 영상도 목록·분석에 넣습니다 (검색은 언어 지정 없이 새로 — 첫 탐색은 캐시 없음)" if on
                        else "끔 — 다음 탐색부터 외국 영상을 뺍니다 (주소로 직접 넣은 영상만 남김)") + f" · PC 설정 저장 · {note}")
                return self._send(200, {"ok": True, "include_foreign": foreign_ok(t), "github": ok, "message": msg})
            if path == "/api/cache/reset":                             # v1.6.2: [캐시 비우기] — 이 주제의 탐색 캐시·탐색 목록만
                if job_of(t)["status"] == "running":
                    raise UserError(f"'{job_of(t)['name']}' 작업이 도는 중 — 끝난 뒤(또는 [멈춤] 뒤)에 비우세요")
                r = pc.reset_topic_cache(t, why="웹 화면 [캐시 비우기]")
                return self._send(200, {"ok": True, **r, "message": (f"캐시 {len(r['moved'])}곳을 {r['to']} 로 옮겼습니다 — 다음 탐색은 처음부터 새로 검색합니다"
                                                                      if r["moved"] else "치울 캐시가 없습니다")})
            if path == "/api/resume":                                  # v1.5: [지금 이어서] — 초기화를 기다리지 않고 남은 것을 이어서
                ok, msg = start_job("남은 것 이어서", job_resume, t, "화면에서")
                return self._send(200 if ok else 409, {"ok": ok, "message": msg})
            if path == "/api/env":
                changed = []
                for name in ENV_NAMES:
                    v = str(body.get(name) or "").strip().strip('"').strip("'")
                    if not v:
                        continue
                    if re.search(r"\s", v):
                        raise UserError(f"{name}: 값에 띄어쓰기·줄바꿈이 있으면 안 됩니다")
                    pc.ensure_topic_env(t)                         # v2.0: 키는 주제마다 따로 — 이 주제 .env 에만 저장 (다른 주제 키는 그대로)
                    set_env_value(ROOT / t / ".env", name, v)
                    os.environ.pop(name, None)                   # 예전 환경 변수보다 .env 를 쓰게
                    changed.append(name)
                log("ENV", topic=t, file=f"{t}/.env", changed=",".join(changed) or "-", note="값은 로그에 쓰지 않음")
                return self._send(200, {"changed": changed, "env": env_view(t)})
            if path == "/api/keywords":
                text = str(body.get("text") or "")
                data = (text.replace("\r\n", "\n").rstrip("\n") + "\n").encode("utf-8")
                kp = keywords_path(t)
                kp.write_bytes(data)
                kws = pc.read_keyword_list(kp) or []
                msg = f"PC 에 저장 ({len(kws)}개)"
                if body.get("push"):
                    ok, note = github_put(t, f"{t}/{pc.KEYWORD_LIST_FILE}", data, f"[{topic_name(t)}] 검색어 고침 (웹 화면, {len(kws)}개)")
                    msg += " · " + note
                log("KEYWORDS", topic=t, keywords=len(kws), note=msg)
                return self._send(200, {"count": len(kws), "message": msg})
            if path == "/api/targets/add":
                return self._send(200, {"results": add_targets(t, body.get("text")), "targets": load_targets(t)})
            if path == "/api/targets/remove":
                return self._send(200, {"targets": remove_target(t, body.get("kind"), body.get("id"))})
            if path == "/api/checked":
                fn = "shorts_explore.json" if body.get("mode") == "shorts" else "explore.json"      # v1.6: 쇼츠 목록의 체크는 따로
                ex = _read_json(web_dir(t) / fn, {})
                if ex:
                    ok_ids = {r["id"] for r in ex.get("rows") or []}
                    ex["checked"] = [i for i in body.get("ids") or [] if i in ok_ids]
                    _write_json(web_dir(t) / fn, ex)
                return self._send(200, {"checked": len(ex.get("checked") or [])})
            if path == "/api/explore":
                weeks = max(1, min(52, int(body.get("weeks") or 8)))
                if body.get("mode") == "shorts":
                    need_sh()
                    ok, msg = start_job("쇼츠 탐색", job_shorts_explore, t, weeks, bool(body.get("keywords", True)))
                else:
                    ok, msg = start_job("탐색", job_explore, t, weeks, bool(body.get("keywords", True)))
                return self._send(200 if ok else 409, {"ok": ok, "message": msg})
            if path == "/api/approve":
                if body.get("mode") == "shorts":
                    need_sh()
                    ok, msg = start_job("쇼츠 승인 — 자료 받고 분석", job_shorts_approve, t, list(body.get("ids") or []), bool(body.get("whisper", True)))
                else:
                    ok, msg = start_job("승인 — 자료 받고 분석", job_approve, t, list(body.get("ids") or []), bool(body.get("whisper", True)))
                return self._send(200 if ok else 409, {"ok": ok, "message": msg})
            if path == "/api/analyze":
                ok, msg = start_job("주별 분석", job_analyze, t)
                return self._send(200 if ok else 409, {"ok": ok, "message": msg})
            if path == "/api/supply":
                n = max(1, min(30, int(body.get("n") or 10)))
                ok, msg = start_job("공급 확인 — 수요는 있는데 영상이 적어 보이는 말", job_supply, t, n)
                return self._send(200 if ok else 409, {"ok": ok, "message": msg})
            if path == "/api/comments":
                ok, msg = start_job("못 받은 댓글 이어 받기", job_comments_then_analyze, t)
                return self._send(200 if ok else 409, {"ok": ok, "message": msg})
            if path == "/api/whisper":
                ok, msg = start_whisper(t, "화면에서 [음성인식 시작]")
                return self._send(200, {"ok": ok, "message": msg})
            if path == "/api/whisper/stop":
                return self._send(200, {"ok": stop_whisper()})
            if path == "/api/cancel":
                job = job_of(t)
                job["cancel"] = True
                p = job.get("proc")
                if p:
                    p.terminate()
                return self._send(200, {"ok": True})
        except UserError as e:
            return self._send(400, {"error": str(e)})
        except Exception as e:
            LOG.exception("POST %s", path)
            return self._send(500, {"error": f"{type(e).__name__}: {e}"[:300]})
        return self._send(404, {"error": "없는 주소"})


def serve(port, host="127.0.0.1"):
    for p in range(port, port + 20):
        try:
            return ThreadingHTTPServer((host, p), Handler), p
        except OSError:
            continue
    raise SystemExit(f"[START] ❌ {port}~{port + 19} 번 포트를 모두 쓰는 중 — --port 로 다른 번호")


def main(argv=None):
    global orr, wa, sh
    ap = argparse.ArgumentParser(description="분석기 웹 화면 — 키·검색어 고치기, 탐색 → 체크 → 승인 → 자료 받기·주별 분석")
    ap.add_argument("topics", nargs="*", help="먼저 열 주제 폴더 (v2.0: 설정 파일이 있는 폴더는 모두 탭으로 — economic 먼저)")
    ap.add_argument("--port", type=int, default=8765)
    ap.add_argument("--no-browser", action="store_true")
    ap.add_argument("--no-sync", action="store_true", help="GitHub 에서 설정·검색어를 받지 않음")
    ap.add_argument("--skip-install", action="store_true")
    ap.add_argument("--no-whisper", action="store_true", help="켤 때 음성인식을 뒤에서 시작하지 않음 (화면의 [음성인식 시작]으로)")
    ap.add_argument("--no-startup", action="store_true", help="켤 때 주별 분석 다시 만들기·올리기를 하지 않음")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    ap.add_argument("--log-file", default="", help=argparse.SUPPRESS)          # 기록 파일 (기본 .yt_work/web_ui.log)
    ap.add_argument("--no-resume", action="store_true", help="할당량 초기화 뒤 남은 것을 저절로 이어서 하지 않음")
    a = ap.parse_args(argv)
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass
    fmt = logging.Formatter("%(message)s")
    root_log = logging.getLogger()
    root_log.setLevel(getattr(logging, a.log_level))
    for h in (logging.StreamHandler(sys.stdout), _JobLogHandler()):
        h.setFormatter(fmt)
        root_log.addHandler(h)
    (ROOT / ".yt_work").mkdir(exist_ok=True)
    fh = logging.FileHandler(Path(a.log_file) if a.log_file else ROOT / ".yt_work" / "web_ui.log", encoding="utf-8")
    fh.setFormatter(fmt)
    root_log.addHandler(fh)
    local = find_topics()
    remote = [] if a.no_sync else pc.remote_topics((a.topics or local or ["economic"])[0])   # v2.0: 저장소 topics.txt — PC 에 없는 주제도 받아 탭으로
    topics = list(dict.fromkeys([x for x in (a.topics or []) if x] + local + remote))    # v2.0: -Folder 로 준 주제 먼저 + PC 주제 + 저장소 주제 = 탭
    if not topics:
        raise SystemExit("[START] ❌ 주제 폴더(<폴더>/analyzer_config.toml)가 없음 — run_analyzer.ps1 로 받거나 폴더 이름 확인")
    if not a.topics and "economic" in topics:
        topics = ["economic"] + [x for x in topics if x != "economic"]
    STATE.update(topic=topics[0], topics=topics)
    # 한 화면에 탭 전부 — 같은 주제를 다른 화면(예전 창 포함)이 쓰는 중이면 그 탭은 보기만. 전부 다른 화면이 쓰면 그 화면을 엶
    if all(topic_window(t) is not None for t in topics if (ROOT / t / "analyzer_config.toml").is_file()) and any(
            (ROOT / t / "analyzer_config.toml").is_file() for t in topics):
        other = topic_window(topics[0]) or {}
        url = other.get("url") or ""
        log("START", topics=",".join(topics), note="모든 주제를 이미 다른 분석기 화면이 쓰는 중 — 그 화면을 씀", url=url or "-")
        print(f"\n  ▶ 분석기 화면이 이미 열려 있습니다: {url or '(다른 창)'}\n", flush=True)
        if url and not a.no_browser:
            webbrowser.open(url)
        return 0
    if not a.skip_install and not pc.ensure_packages(False):
        raise SystemExit("[START] ❌ 패키지 설치 실패 — 위 오류 확인")
    if not a.no_sync:                         # v1.3: 코드도 — 실행기 목록에 없는 새 도구(tools/success_analysis.py)가 PC 에 오게 (불러오기 전에)
        for k, t in enumerate(topics):
            try:
                res = pc.sync_from_github(t, code=(k == 0))
                got = [r for r, v in res.items() if v in ("새로 받음", "GitHub 새 판으로 바꿈")]
                log("SYNC", topic=t, updated=",".join(got) or "-", note="GitHub 최신 설정·코드 (이 화면 자신은 다음 실행부터)")
            except Exception as e:
                log("SYNC", logging.WARNING, topic=t, note="GitHub 에서 설정·코드를 받지 못함 — PC 파일로", error=f"{type(e).__name__}"[:80])
    topics = [t for t in topics if (ROOT / t / "analyzer_config.toml").is_file()]       # 받지 못한 주제는 탭에서 뺌
    if not topics:
        raise SystemExit("[START] ❌ 주제 설정(<폴더>/analyzer_config.toml)을 하나도 받지 못함 — 인터넷 연결 확인 뒤 다시")
    STATE.update(topic=topics[0], topics=topics)
    import outlier_research as _orr
    import weekly_analysis as _wa
    orr, wa = _orr, _wa
    try:                                      # v1.6: 쇼츠 분석 (없으면 쇼츠 기능만 꺼짐 — 롱폼은 그대로)
        import shorts_analysis as _sh
        sh = _sh
    except Exception as e:
        log("START", logging.WARNING, note="쇼츠 분석 도구를 못 불러옴 — 쇼츠 기능 꺼짐 (창을 닫고 다시 켜면 GitHub 최신 코드를 받음)",
            error=f"{type(e).__name__}: {e}"[:160])
    srv, port = serve(a.port)
    STATE["port"] = port
    try:                                      # v2.0: 캐시·설정을 주제마다 — 예전 공동 캐시는 옮김
        pc.retire_shared_cache()
    except Exception as e:
        log("RESET", logging.WARNING, note="예전 공동 캐시 옮기기 실패 — 그대로 계속 (아무도 안 읽음)", error=f"{type(e).__name__}: {e}"[:160])
    mine = []
    for t in topics:                          # v2.0: 이 화면이 탭 전부를 잠금 — 켜는 사이 다른 화면이 잡은 주제는 보기만
        try:
            claim_topic(t)
            mine.append(t)
        except UserError as e:
            log("START", logging.WARNING, topic=t, note=str(e))
            continue
        for fn, what in ((pc.ensure_topic_env, "주제 전용 키 파일"), (pc.fresh_start, "새 주제의 옛 자료 옮기기")):
            try:
                fn(t)
            except Exception as e:
                log("START", logging.WARNING, topic=t, note=f"{what} 실패 — 그대로 계속", error=f"{type(e).__name__}: {e}"[:160])
    if not mine:
        srv.server_close()
        print("\n  ▶ 고른 주제가 모두 다른 화면에 열려 있습니다 — 그 화면을 쓰세요\n", flush=True)
        return 0
    STATE["topic"] = mine[0]
    url = f"http://127.0.0.1:{port}/"
    log("START", url=url, tabs=",".join(topics), mine=",".join(mine), tool=f"web_ui.py {VERSION}",
        note="이 창을 닫으면 화면도 꺼집니다 (Ctrl+C 로 끝냄) — 주제는 화면 위쪽 탭으로")
    print(f"\n  ▶ 분석기 화면: {url}  (주제 탭: {', '.join(topics)})\n    (브라우저가 안 열리면 위 주소를 복사해 여세요. 끝내려면 이 창에서 Ctrl+C)\n", flush=True)
    if not a.no_browser:
        threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    if not a.no_startup:                      # v1.2: 승인한 영상 결과를 새로 만들어 올리고, 남은 음성인식은 뒤에서 (v2.0: 탭마다)
        for t in mine:
            start_job("켤 때 — 분석 결과 올리기", job_startup, t, not a.no_whisper)
    if not a.no_resume:                       # v1.5: 할당량 초기화(태평양 자정 +10분) 뒤 남은 것을 저절로 이어서
        threading.Thread(target=_resume_loop, daemon=True, name="resume").start()
        log("RESUME", topics=",".join(mine), next_kst=pc.next_quota_reset(datetime.now(timezone.utc), RESUME_MARGIN_MIN)[0].astimezone(KST)
            .strftime("%m-%d %H:%M"), note="할당량이 끝나 남은 것은 초기화 뒤 저절로 이어서 (이 화면을 켜 둔 동안, 탭마다)")
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        log("DONE", note="화면을 끔")
    finally:
        srv.server_close()
        release_topic()
        for holder in [WHISPER] + list(JOBS.values()):    # 음성인식·올리기도 같이 끝냄 (하던 영상은 다음에 처음부터)
            p = holder.get("proc")
            if p and p.poll() is None:
                p.terminate()
    return 0


PAGE = r"""<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="t" content="{{TOKEN}}"><title>분석기</title>
<style>
:root{--bg:#f7f7f5;--card:#fff;--fg:#1d1d1f;--mut:#6b6b70;--line:#e3e3e0;--acc:#2563eb;--acc2:#1d4ed8;--ok:#15803d;--warn:#b45309;--bad:#b91c1c;--chip:#eef2ff;--row:#fafaf9}
@media (prefers-color-scheme:dark){:root{--bg:#111113;--card:#1a1a1d;--fg:#ececee;--mut:#a0a0a8;--line:#2c2c31;--acc:#5b8cff;--acc2:#7aa2ff;--ok:#4ade80;--warn:#fbbf24;--bad:#f87171;--chip:#1e2540;--row:#161618}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:14px/1.5 -apple-system,"Segoe UI","Malgun Gothic","Apple SD Gothic Neo",sans-serif}
header{position:sticky;top:0;z-index:5;background:var(--card);border-bottom:1px solid var(--line);padding:10px 16px;display:flex;gap:14px;align-items:center;flex-wrap:wrap}
header h1{font-size:17px;margin:0}header .pill{font-size:12px;color:var(--mut);background:var(--bg);border:1px solid var(--line);border-radius:99px;padding:2px 10px}
main{max-width:1280px;margin:0 auto;padding:16px;display:grid;gap:14px}main>*,.two>*{min-width:0}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px 16px}
.card h2{font-size:15px;margin:0 0 10px}.card h2 small{font-weight:400;color:var(--mut);margin-left:6px}
.row{display:flex;gap:8px;align-items:center;flex-wrap:wrap}.grow{flex:1;min-width:200px}
input[type=text],input[type=password],input[type=number],textarea,select{font:inherit;color:var(--fg);background:var(--bg);border:1px solid var(--line);border-radius:8px;padding:7px 10px}
textarea{width:100%;min-height:180px;font-family:ui-monospace,Consolas,monospace;font-size:13px}
button{font:inherit;border:1px solid var(--line);background:var(--bg);color:var(--fg);border-radius:8px;padding:7px 14px;cursor:pointer}
button.pri{background:var(--acc);border-color:var(--acc);color:#fff;font-weight:600}button.pri:hover{background:var(--acc2)}
button:disabled{opacity:.5;cursor:not-allowed}.mut{color:var(--mut)}.ok{color:var(--ok)}.warn{color:var(--warn)}.bad{color:var(--bad)}
.two{display:grid;grid-template-columns:1fr 1fr;gap:14px}@media (max-width:860px){.two{grid-template-columns:1fr}}
.chip{display:inline-flex;gap:6px;align-items:center;background:var(--chip);border-radius:99px;padding:3px 6px 3px 10px;margin:3px 4px 0 0;font-size:13px}
.chip button{padding:0 7px;border:0;background:transparent;color:var(--mut)}
.tablewrap{overflow:auto;max-height:620px;border:1px solid var(--line);border-radius:8px}
table{border-collapse:collapse;width:100%;font-size:13px}th,td{padding:6px 8px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top;white-space:nowrap}
th{position:sticky;top:0;background:var(--card);z-index:1;font-weight:600}td.t{white-space:normal;min-width:260px}tr.on{background:var(--row)}
td.n,th.n{text-align:right;font-variant-numeric:tabular-nums}a{color:var(--acc)}
.tag{font-size:11px;border-radius:6px;padding:1px 6px;background:var(--bg);border:1px solid var(--line);margin-right:3px}
.tag.s{border-color:var(--ok);color:var(--ok)}.tag.d{border-color:var(--acc);color:var(--acc)}
.bar{height:6px;background:var(--line);border-radius:9px;overflow:hidden}.bar i{display:block;height:100%;background:var(--acc);width:0}
pre{background:var(--bg);border:1px solid var(--line);border-radius:8px;padding:10px;max-height:260px;overflow:auto;font-size:12px;white-space:pre-wrap;margin:8px 0 0}
details{border:1px solid var(--line);border-radius:8px;padding:8px 12px;margin-top:8px}summary{cursor:pointer;font-weight:600}
.msg{min-height:20px;font-size:13px}h3.sub{font-size:14px;margin:14px 0 6px}.tag.x{border-color:var(--warn);color:var(--warn)}.k{display:grid;grid-template-columns:150px 1fr;gap:8px;align-items:center;margin-bottom:8px}
@media (max-width:600px){.k{grid-template-columns:1fr}}
.seg{display:inline-flex;border:1px solid var(--line);border-radius:9px;overflow:hidden;margin-left:8px;vertical-align:middle}.seg button{border:0;border-radius:0;padding:4px 14px;font-size:13px}
.seg button.on{background:var(--acc);color:#fff;font-weight:600}.seg button:disabled{opacity:.4}
nav.tabs{display:flex;gap:4px;flex-wrap:wrap}nav.tabs button{border-radius:8px 8px 0 0;border-bottom:3px solid transparent;padding:6px 14px;font-weight:600;background:var(--bg)}
nav.tabs button.on{border-bottom-color:var(--acc);color:var(--acc);background:var(--card)}nav.tabs .dot{display:inline-block;width:8px;height:8px;border-radius:9px;margin-left:6px;background:transparent;vertical-align:middle}
nav.tabs .dot.running{background:var(--ok)}nav.tabs .dot.error{background:var(--bad)}nav.tabs .dot.other{background:var(--warn)}
.banner{background:var(--chip);border:1px solid var(--line);border-radius:10px;padding:8px 12px}
</style></head><body>
<header><h1 id="title">분석기</h1><nav class="tabs" id="tabs" title="주제 탭 — 탭마다 검색어·키·캐시·작업·분석 결과가 따로 (할당량만 같은 키에서 함께)"></nav>
<span class="pill" id="quota">할당량 …</span><span class="pill" id="caption">자막 서버 …</span><span class="pill" id="wPill">음성인식 …</span><span class="pill" id="ver"></span></header>
<main>
<div class="banner warn" id="otherBanner" style="display:none"></div>
<section class="card"><h2>0. 주제 · 할당량 <small>위쪽 탭으로 주제를 고름 — 탭마다 검색어·키(.env)·캐시·작업·결과가 따로, 다른 탭 작업도 동시에 돎 · 할당량만 같은 키를 쓰는 모든 탭이 함께</small></h2>
 <div class="row"><b id="qBig">할당량 …</b><span class="mut" id="qReset"></span></div>
 <div class="bar" style="margin-top:6px"><i id="qBar"></i></div>
 <div class="mut" id="qBy" style="margin-top:6px"></div>
 <div class="row" style="margin-top:6px"><span class="grow mut" id="resumeInfo"></span><button id="resumeNow" title="초기화를 기다리지 않고 남은 탐색·댓글·채널 기준선을 지금 이어서 (남은 할당량만큼)">지금 이어서</button></div>
 <div class="mut" id="winInfo" style="margin-top:4px"></div>
 <details><summary>새 주제 만들기 (새 탭)</summary>
  <h3 class="sub">새 주제 만들기 <small class="mut">— economic 설정을 틀로 <code>&lt;폴더&gt;/analyzer_config.toml · keywords.txt · keywords.toml</code></small></h3>
  <div class="k"><label for="ntFolder">폴더 이름 (영어 소문자)</label><input type="text" id="ntFolder" placeholder="예: health"></div>
  <div class="k"><label for="ntName">주제 이름</label><input type="text" id="ntName" placeholder="예: 건강"></div>
  <div class="k"><label for="ntKw">검색어 (한 줄에 하나)</label><textarea id="ntKw" style="min-height:90px"></textarea></div>
  <div class="row"><button class="pri" id="ntMake">주제 폴더 만들기</button><label><input type="checkbox" id="ntPush" checked> GitHub 에도 저장</label><span class="msg" id="ntMsg"></span></div>
  <div class="mut">관련어(주제와 관련된 영상 가리기)는 비어 있게 만들어집니다 — 비어 있으면 모든 검색 결과를 주제 관련으로 봅니다. 다듬으려면 Claude 에게 '&lt;주제&gt; 검색어 만들어줘'.</div>
 </details>
</section>
<div class="two">
 <section class="card"><h2>1. 키 설정 <small id="envFile">이 주제 전용 .env — 끝 4자리만 보입니다</small></h2>
  <div class="k"><label for="ytkey">YouTube API 키</label><div><input type="password" id="ytkey" class="grow" style="width:100%" placeholder="바꿀 때만 붙여넣기" autocomplete="off"><div class="mut" id="ytkey_now"></div></div></div>
  <div class="k"><label for="ghtok">GitHub 토큰</label><div><input type="password" id="ghtok" style="width:100%" placeholder="바꿀 때만 붙여넣기" autocomplete="off"><div class="mut" id="ghtok_now"></div></div></div>
  <div class="row"><button class="pri" id="saveEnv">키 저장</button><span class="msg" id="envMsg"></span></div>
 </section>
 <section class="card"><h2>2. 검색어 <small>한 줄에 하나 · # 은 메모</small></h2>
  <textarea id="kw" spellcheck="false"></textarea>
  <div class="row" style="margin-top:8px"><button class="pri" id="saveKw">검색어 저장</button>
   <label><input type="checkbox" id="kwPush" checked> GitHub 에도 저장</label><span class="mut" id="kwCount"></span><span class="msg" id="kwMsg"></span></div>
 </section>
</div>
<section class="card"><h2>3. 직접 추가 <small>영상 주소 → 그 영상 · 채널 주소나 @이름 → 그 채널에 올라온 영상 전부 · 여러 개는 한 줄에 하나</small></h2>
 <div class="row" style="align-items:flex-start"><textarea id="tgIn" class="grow" style="min-height:70px" placeholder="https://www.youtube.com/watch?v=…&#10;https://www.youtube.com/@채널이름&#10;(여러 개를 한 번에 붙여넣어도 됩니다)"></textarea><button class="pri" id="tgAdd">추가</button></div>
 <div class="msg" id="tgMsg"></div>
 <div id="tgList" style="margin-top:6px"></div>
</section>
<section class="card"><h2>4. 탐색 <span class="seg" id="modeSeg" title="롱폼(4분 넘음)과 쇼츠(3분 이하 세로)는 목록·자료·분석이 따로입니다"><button data-m="long">롱폼</button><button data-m="shorts">쇼츠</button></span> <small id="exploreSub">목록만 만듭니다 — 자료는 승인한 영상만 받습니다</small></h2>
 <div class="row">최근 <input type="number" id="weeks" min="1" max="52" value="8" style="width:70px"> 주
  <label><input type="checkbox" id="useKw" checked> 검색어로도 찾기</label>
  <label title="이 주제 설정(analyzer_config.toml INCLUDE_FOREIGN) — 켜면 외국 영상도 목록·분석에 넣고 검색은 언어 지정 없이. 기본 꺼짐"><input type="checkbox" id="foreign"> 외국 영상도 <small class="mut">(이 주제 설정)</small></label>
  <span class="mut" id="est"></span><button id="cacheReset" title="이 주제의 탐색 캐시·탐색 목록(체크 포함)을 .yt_work/old/ 로 옮김 — 승인한 자료·분석 결과는 그대로">캐시 비우기</button><button class="pri" id="explore">탐색</button></div>
 <div class="msg" id="foreignMsg"></div>
</section>
<section class="card" id="listCard"><h2>5. <span id="listTitle">탐색 목록</span> <small id="listInfo">배수 높은 순 · 추천은 체크해 둠</small></h2>
 <div class="row" style="margin-bottom:8px"><input type="text" id="flt" class="grow" placeholder="제목·채널 거르기">
  <label id="fShortLbl"><input type="checkbox" id="fShort"> 짧은 영상(4분 미만)도</label><label><input type="checkbox" id="fRel" checked> 주제 관련만</label>
  <button id="chkAll">보이는 것 모두 체크</button><button id="chkNone">모두 해제</button><button id="chkRec">추천만</button></div>
 <h3 class="sub">✅ 체크한 영상 <span id="onCount"></span> <small class="mut">— 승인하면 이 영상들의 자료를 받습니다</small></h3>
 <div class="tablewrap"><table><thead><tr><th></th><th>업로드</th><th>제목</th><th>채널</th><th class="n">구독자</th><th class="n">조회수</th><th class="n">배수 ▼</th><th class="n">하루 조회수</th><th class="n">길이</th><th>추천 · 출처</th></tr></thead><tbody id="rowsOn"><tr><td colspan="10" class="mut">탐색을 누르면 여기에 나옵니다</td></tr></tbody></table></div>
 <h3 class="sub">☐ 체크 안 한 영상 <span id="offCount"></span></h3>
 <div class="tablewrap"><table><thead><tr><th></th><th>업로드</th><th>제목</th><th>채널</th><th class="n">구독자</th><th class="n">조회수</th><th class="n">배수 ▼</th><th class="n">하루 조회수</th><th class="n">길이</th><th>추천 · 출처</th></tr></thead><tbody id="rowsOff"><tr><td colspan="10" class="mut">—</td></tr></tbody></table></div>
 <div class="row" style="margin-top:10px"><button class="pri" id="approve">승인 — 자료 받고 분석해서 바로 올리기</button><label><input type="checkbox" id="autoW" checked> 그다음 자막 못 받은 영상 음성인식 (뒤에서)</label><span class="mut" id="chkInfo"></span></div>
 <div class="mut" style="margin-top:6px" id="approveNote">순서: 자료(설명·자막·썸네일·댓글) 받기 → 채널 평소 영상(같은 채널 기준선, 채널 하나 약 2단위) → 분석 (자막을 못 받은 영상은 영상 설명으로 대신) → GitHub 에 바로 올림 → 음성인식은 뒤에서 (성공 사례부터 앞 5분 → 전체)</div>
</section>
<section class="card"><h2>진행 <small id="jobName"></small></h2>
 <div class="row"><span id="jobStep" class="grow">쉬는 중</span><button id="cancel" disabled>멈춤</button><button id="reanalyze" title="주별 분석·성공 사례 분석을 다시 만들어 GitHub 에 올림">다시 분석·올리기</button><button id="comments" title="할당량이 끝나 다 받지 못한 댓글을 이어 받고 다시 분석">못 받은 댓글 이어 받기</button></div>
 <div class="msg" id="jobRes"></div>
 <div class="bar" style="margin-top:8px"><i id="jobBar"></i></div><pre id="jobLog"></pre>
</section>
<section class="card"><h2>음성인식 <small>뒤에서 하나씩 · 성공 사례부터 1차(앞 5분) → 2차(전체) · 끝날 때마다 분석을 다시 만들고 15분마다·차수 끝에 올림 · 도는 동안에도 탐색·승인 가능</small></h2>
 <div class="row"><span id="wStep" class="grow">쉬는 중</span><button id="wStart">음성인식 시작</button><button id="wStop" disabled>멈춤</button></div>
 <div class="bar" style="margin-top:8px"><i id="wBar"></i></div>
 <details><summary>음성인식 기록</summary><pre id="wLog"></pre></details>
</section>
<section class="card"><h2>6. 분석 결과 <small>성공 사례 분석 analysis.md (지시사항 재료) · 쇼츠 분석 shorts/analysis.md · 주별 추세 weekly.md</small></h2>
 <div id="analysis" class="mut" style="margin-bottom:12px"></div>
 <h3 class="sub">쇼츠 분석 <small class="mut">— 받은 쇼츠(shorts/S_) · 성공 쇼츠 · 첫 3초 · 길이 · 니즈</small></h3>
 <div id="shortsAnalysis" class="mut" style="margin-bottom:12px">쇼츠를 승인하면 여기에 나옵니다 (4번 칸에서 [쇼츠]로 바꿔 탐색)</div>
 <h3 class="sub">주별 추세 <small class="mut">— 승인한 영상 전부 (최근 1주부터 한 주씩 넓힘, 누적)</small></h3>
 <div id="report" class="mut">승인한 영상이 생기면 여기에 나옵니다</div></section>
</main>
<script>
const T=document.querySelector('meta[name=t]').content;let ROWS=[],CHECK=new Set(),REC=new Set(),busy=false,lastJob=null,waitDone=false,lastWDone=null,TOPICS={names:{},windows:[],list:[]},PLAN=null,TABS={};
// v2.0: 주제 탭 — 요청마다 X-Topic. 탭마다 롱폼/쇼츠·최근 N주를 따로 기억 (사용자 지시 "설정도 다 따로써야해")
let TOPIC='';try{TOPIC=decodeURIComponent(location.hash.slice(1))||localStorage.getItem('ytTopic')||''}catch(e){}
function lsGet(k,d){try{const v=localStorage.getItem(k+':'+TOPIC);return v==null?d:v}catch(e){return d}}
function lsSet(k,v){try{localStorage.setItem(k+':'+TOPIC,v)}catch(e){}}
let MODE='long',SHORTS_OK=true;
const $=id=>document.getElementById(id);const esc=s=>String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const num=x=>x==null?'–':(typeof x==='number'?x.toLocaleString('ko-KR',{maximumFractionDigits:1}):x);
async function api(p,b){const h={'X-Token':T,'Content-Type':'application/json'};if(TOPIC)h['X-Topic']=TOPIC;
 const r=await fetch(p,{method:b?'POST':'GET',headers:h,body:b?JSON.stringify(b):undefined});
 const j=await r.json().catch(()=>({error:'응답 오류'}));if(!r.ok)throw new Error(j.error||j.message||r.status);return j}
function say(id,t,cls){const e=$(id);e.textContent=t;e.className='msg '+(cls||'')}
async function loadState(){const s=await api('/api/state');if(TOPIC!==s.topic){TOPIC=s.topic;applyTabPrefs()}
 $('title').textContent='분석기';$('ver').textContent='web_ui '+s.version;document.title=s.name+' — 분석기';
 renderTopics(s);$('envFile').textContent=`이 주제 전용 ${s.env_file||'.env'} — 다른 탭 키는 안 바뀜 · 끝 4자리만 보입니다`;
 const ob=$('otherBanner');if(s.locked_elsewhere){ob.style.display='';ob.innerHTML=`⚠️ 이 주제(${esc(s.topic)})는 다른 분석기 화면이 쓰는 중이라 이 탭은 보기만 됩니다 — ${typeof s.locked_elsewhere==='string'?`<a href="${esc(s.locked_elsewhere)}" target=_blank rel=noopener>${esc(s.locked_elsewhere)}</a>`:'그 창'} 을 닫고 이 창을 다시 켜세요 (예전 판은 주제마다 창이 따로 떴음)`}else ob.style.display='none';PLAN=s.resume&&s.resume.plan;renderQuota(s.quota);renderResume(s.resume);
 $('caption').textContent=s.caption_block?`자막 서버 차단 — ${s.caption_block}까지 쉬는 중 (음성인식으로)`:'자막 서버 정상';$('caption').className='pill '+(s.caption_block?'warn':'');
 const e=s.env;$('ytkey_now').innerHTML=e.YOUTUBE_API_KEY.set?`<span class=ok>설정됨</span> ${esc(e.YOUTUBE_API_KEY.tail)} · ${esc(e.YOUTUBE_API_KEY.source)}`:'<span class=bad>없음</span> — 넣어야 탐색할 수 있습니다';
 $('ghtok_now').innerHTML=e.GITHUB_TOKEN.set?`<span class=ok>설정됨</span> ${esc(e.GITHUB_TOKEN.tail)} · ${esc(e.GITHUB_TOKEN.source)}`:'없음 — 결과는 PC 에만 저장';
 if(document.activeElement!==$('kw'))$('kw').value=s.keywords_text;$('kwCount').textContent=`검색어 ${s.keywords_count}개`;
 $('foreign').checked=!!s.include_foreign;renderTargets(s.targets);showJob(s.job);SHORTS_OK=!!(s.shorts&&s.shorts.available);if(!SHORTS_OK&&MODE==='shorts')MODE='long';renderMode();estimate();return s}
function renderMode(){document.querySelectorAll('#modeSeg button').forEach(b=>{b.classList.toggle('on',b.dataset.m===MODE);if(b.dataset.m==='shorts'){b.disabled=!SHORTS_OK;b.title=SHORTS_OK?'':'쇼츠 분석 도구가 없음 — 창을 닫고 다시 켜면 받음'}});
 const sh=MODE==='shorts';$('listTitle').textContent=sh?'쇼츠 목록':'탐색 목록';$('fShortLbl').style.display=sh?'none':'';
 $('exploreSub').textContent=sh?'쇼츠(3분 이하·세로)만 — 검색어마다 쇼츠 검색 1번(100단위) + 추가한 채널의 쇼츠 목록. 자료는 승인한 쇼츠만':'목록만 만듭니다 — 자료는 승인한 영상만 받습니다';
 $('approve').textContent=sh?'쇼츠 승인 — 자료 받고 분석해서 바로 올리기':'승인 — 자료 받고 분석해서 바로 올리기';
 $('approveNote').textContent=sh?'순서: 쇼츠 자료(설명·자막·세로 표지·댓글 전부) 받기 → 채널 평소 쇼츠(채널 쇼츠 목록, 채널 하나 약 2단위) → 쇼츠 분석(shorts/analysis.md) → GitHub 에 바로 올림 → 음성인식은 뒤에서 (쇼츠 먼저 — 하나에 1~2분)'
  :'순서: 자료(설명·자막·썸네일·댓글) 받기 → 채널 평소 영상(같은 채널 기준선, 채널 하나 약 2단위) → 분석 (자막을 못 받은 영상은 영상 설명으로 대신) → GitHub 에 바로 올림 → 음성인식은 뒤에서 (성공 사례부터 앞 5분 → 전체)'}
function applyTabPrefs(){MODE=lsGet('ytMode','long')==='shorts'?'shorts':'long';$('weeks').value=lsGet('ytWeeks','8');$('useKw').checked=lsGet('ytUseKw','1')==='1';
 try{localStorage.setItem('ytTopic',TOPIC)}catch(e){}if(TOPIC&&location.hash.slice(1)!==TOPIC)history.replaceState(null,'','#'+TOPIC)}
function setMode(m){if(m===MODE||(m==='shorts'&&!SHORTS_OK))return;MODE=m;lsSet('ytMode',m);renderMode();ROWS=[];CHECK=new Set();renderRows();estimate();loadRows().then(()=>{loadAnalysis();loadShortsAnalysis()})}
function hm(m){return m>=60?`${Math.floor(m/60)}시간 ${m%60}분`:`${m}분`}
function renderQuota(q){if(!q)return;
 if(q.key===null){$('quota').textContent='할당량 — 키 없음';$('quota').className='pill warn';$('qBig').textContent='YouTube API 키를 넣으면 남은 할당량이 보입니다';$('qBy').textContent='';return}
 const pct=Math.min(100,Math.round(100*q.used/Math.max(1,q.budget)));
 $('quota').textContent=`남은 할당량 ${num(q.left)} / ${num(q.budget)} · 초기화 ${q.reset_kst} (${hm(q.reset_in_min)} 뒤)`;
 $('quota').className='pill '+(q.left<=0?'bad':q.left<1000?'warn':'ok');
 $('qBig').textContent=q.exhausted?`오늘 할당량 끝 — Google 이 하루 한도라고 답함 (장부상 쓴 양 ${num(q.used)})`:`남은 ${num(q.left)}단위 · 오늘 쓴 ${num(q.used)} / ${num(q.budget)}`;
 $('qReset').textContent=` · 하루 ${num(q.limit)} − 여유 ${num(q.margin)} · 초기화 한국 시간 ${q.reset_kst} (${hm(q.reset_in_min)} 뒤)`;
 $('qBar').style.width=pct+'%';$('qBar').style.background=q.left<=0?'var(--bad)':q.left<1000?'var(--warn)':'var(--acc)';
 const bt=Object.entries(q.by_topic||{}).filter(x=>x[1]).map(([k,v])=>`${esc(k)} ${num(v)}`).join(' · ');
 const bw=Object.entries(q.by_what||{}).filter(x=>x[1]).sort((a,b)=>b[1]-a[1]).slice(0,6).map(([k,v])=>`${esc(k)} ${num(v)}`).join(' · ');
 const sk=(q.same_key||[]).length?`같은 키를 쓰는 다른 탭: ${q.same_key.map(esc).join(' · ')} (할당량을 함께 씀)`:'이 탭만 쓰는 키 (할당량 따로)';
 $('qBy').innerHTML=`<b>이 탭 키</b> 지문 …${esc(String(q.key).slice(-4))} — ${sk}<br>주제별 ${bt||'—'} · 작업별 ${bw||'—'} <span class=mut>(같은 키를 쓰는 이 PC 의 모든 창·자동 실행 합계 — 다른 PC·클라우드에서 쓴 양은 모름, 그때는 Google 의 한도 답으로 멈춤)</span>`}
function renderResume(r){if(!r)return;const p=PLAN||{};
 const parts=[p.explore_searches?`검색 ${p.explore_searches}개`:'',p.explore_videos?`영상 정보 ${p.explore_videos}개`:'',p.comments?`댓글 못 받은 영상 ${p.comments}개`:'',p.baseline?`채널 기준선 ${p.baseline}곳`:''].filter(Boolean);
 const nx=r.next?`다음 자동 이어서: 한국 시간 ${r.next.slice(5,16).replace('T',' ')}`:'자동 이어서 꺼짐 (--no-resume)';
 $('resumeInfo').textContent=(parts.length?`할당량 때문에 남은 것: ${parts.join(' · ')} → ${nx}`:`남은 것 없음 · ${nx}`)+(r.status==='waiting_job'?' · 지금 작업이 끝나길 기다리는 중':'')+(r.last?` · 지난번 ${r.last.slice(5,16).replace('T',' ')}`:'')}
function renderTopics(s){TOPICS={names:s.topic_names||{},windows:s.windows||[],list:s.topics||[]};if(s.tabs)TABS=s.tabs;renderTabs();
 const other=TOPICS.windows.filter(w=>!w.me);
 $('winInfo').innerHTML=other.length?'다른 화면이 쓰는 주제: '+other.map(w=>`${esc(w.topic)}${w.url?` (<a href="${esc(w.url)}" target=_blank rel=noopener>${esc(w.url)}</a>)`:''}`).join(' · ')+' — 그 창을 닫으면 이 화면의 탭에서 씁니다':''}
function renderTabs(){const other=new Set(TOPICS.windows.filter(w=>!w.me).map(w=>w.topic));
 $('tabs').innerHTML=TOPICS.list.map(t=>{const st=other.has(t)?'other':(TABS[t]||'');return `<button data-t="${esc(t)}" class="${t===TOPIC?'on':''}" title="${esc(t)}/ 폴더${other.has(t)?' — 다른 화면이 쓰는 중 (보기만)':st==='running'?' — 작업 도는 중':''}">${esc(TOPICS.names[t]||t)}<span class="dot ${st}"></span></button>`}).join('');
 $('tabs').querySelectorAll('button').forEach(b=>b.onclick=()=>switchTab(b.dataset.t))}
async function switchTab(t){if(!t||t===TOPIC)return;TOPIC=t;applyTabPrefs();ROWS=[];CHECK=new Set();REC=new Set();lastJob=null;waitDone=false;lastWDone=null;busy=false;
 MISSING=[];SMISSING=[];renderRows();renderTabs();$('jobLog').textContent='';$('jobRes').innerHTML='';
 try{await loadState();await loadRows();loadAnalysis();loadShortsAnalysis();loadReport();showJob(await api('/api/job'))}catch(e){alert(e.message)}}
function renderTargets(tg){const c=tg.channels.map(x=>`<span class=chip>📺 ${esc(x.title||x.id)} <span class=mut>영상 ${num(x.videos)}개</span><button data-k=channel data-id="${esc(x.id)}" title="빼기">✕</button></span>`);
 const v=tg.videos.map(x=>`<span class=chip>▶ ${esc((x.title||x.id).slice(0,40))}<button data-k=video data-id="${esc(x.id)}" title="빼기">✕</button></span>`);
 $('tgList').innerHTML=(c.concat(v).join(''))||'<span class=mut>추가한 영상·채널 없음</span>';
 $('tgList').querySelectorAll('button').forEach(b=>b.onclick=async()=>{const r=await api('/api/targets/remove',{kind:b.dataset.k,id:b.dataset.id});renderTargets(r.targets);estimate()})}
let estT;function estimate(){clearTimeout(estT);estT=setTimeout(async()=>{try{const e=await api(`/api/estimate?weeks=${$('weeks').value}&kw=${$('useKw').checked?1:0}&mode=${MODE}`);
 $('est').textContent=`${MODE==='shorts'?'쇼츠 검색':'검색'} ${e.searches}번 (캐시 ${e.cached}) + 채널 ${e.channels}·영상 ${e.videos} → 약 ${num(e.units)}단위`+(e.left!=null?` · 오늘 남은 ${num(e.left)}`+(e.units>e.left?' (모자라는 만큼은 초기화 뒤 저절로 이어서)':''):'')}catch(x){$('est').textContent=x.message}},250)}
async function loadRows(){const m=MODE,d=await api(`/api/explore?mode=${m}`);if(m!==MODE)return;ROWS=d.rows;CHECK=new Set(d.checked);REC=new Set(ROWS.filter(r=>r.reason).map(r=>r.id));
 const ex=Object.entries(d.excluded||{}).map(([k,v])=>`${k} ${v}개`);if(d.used_hidden)ex.unshift(`이미 분석에 쓴 ${m==='shorts'?'쇼츠':'영상'} ${d.used_hidden}개`);
 const what=m==='shorts'?'쇼츠':'영상';
 $('listInfo').textContent=(d.generated?`배수 높은 순 · ${d.generated.slice(0,16).replace('T',' ')} ${m==='shorts'?'쇼츠 ':''}탐색 (최근 ${d.weeks}주${d.keywords_file?' · 검색어 '+d.keywords_file:''}) · ${what} ${ROWS.length.toLocaleString()}개 · 추천은 체크해 둠`:(m==='shorts'?'쇼츠 탐색을 누르면 여기에 나옵니다 · 배수 높은 순':'배수 높은 순 · 추천은 체크해 둠'))+(ex.length?` · 뺀 것: ${ex.join(', ')}`:'');renderRows()}
function byRatio(a){return a.sort((x,y)=>((y.ratio??-1)-(x.ratio??-1))||(y.views-x.views))}
function visible(){const f=$('flt').value.trim().toLowerCase();return ROWS.filter(r=>(r.sources.includes('주소')||(($('fShort').checked||MODE==='shorts'||!r.short)&&(!$('fRel').checked||r.relevant)))
 &&(!f||(r.title+' '+r.channel).toLowerCase().includes(f)))}
function rowHtml(r){const src=r.sources.map(s=>s.startsWith('검색:')?'🔎'+s.slice(3):s.startsWith('채널:')?'📺'+s.slice(3):'▶ 추가').slice(0,3).join(' ');
  return `<tr class="${CHECK.has(r.id)?'on':''}"><td><input type=checkbox data-id="${r.id}" ${CHECK.has(r.id)?'checked':''}></td><td>${esc(r.published)}<div class=mut>${r.age_days}일 전</div></td>
  <td class=t><a href="${r.url}" target=_blank rel=noopener>${esc(r.title)}</a></td><td>${esc(r.channel)}</td><td class=n>${r.subs==null?'비공개':num(r.subs)}</td><td class=n>${num(r.views)}</td>
  <td class=n>${r.ratio==null?'–':num(r.ratio)}</td><td class=n>${num(r.views_per_day)}</td><td class=n>${r.seconds!=null&&MODE==='shorts'?num(r.seconds)+'초':num(r.minutes)+'분'}</td>
  <td>${r.reason?`<span class="tag ${r.reason==='성공 사례'||r.reason==='성공 쇼츠'?'s':''}">${esc(r.reason)}</span>`:''}${r.flag?`<span class="tag x">${esc(r.flag)}</span>`:''}<span class=mut>${esc(src)}</span></td></tr>`}
function fill(id,list,empty){$(id).innerHTML=list.length?list.slice(0,3000).map(rowHtml).join('')+(list.length>3000?`<tr><td colspan=10 class=mut>앞 3,000개만 보입니다 — 거르기를 쓰세요 (전체 ${list.length.toLocaleString()}개)</td></tr>`:''):`<tr><td colspan=10 class=mut>${empty}</td></tr>`}
function renderRows(){if(!ROWS.length){$('rowsOn').innerHTML=`<tr><td colspan=10 class=mut>${MODE==='shorts'?'쇼츠':''} 탐색을 누르면 여기에 나옵니다</td></tr>`;$('rowsOff').innerHTML='<tr><td colspan=10 class=mut>—</td></tr>';$('onCount').textContent='';$('offCount').textContent='';updChk();return}
 const vs=visible(),on=byRatio(vs.filter(r=>CHECK.has(r.id))),off=byRatio(vs.filter(r=>!CHECK.has(r.id)));
 fill('rowsOn',on,'체크한 영상 없음 — 아래 표에서 체크하세요');fill('rowsOff',off,'체크 안 한 영상 없음');
 $('onCount').textContent=`${on.length.toLocaleString()}개`;$('offCount').textContent=`${off.length.toLocaleString()}개`;
 document.querySelectorAll('#rowsOn input[type=checkbox],#rowsOff input[type=checkbox]').forEach(c=>c.onchange=()=>{c.checked?CHECK.add(c.dataset.id):CHECK.delete(c.dataset.id);renderRows();saveChk()});updChk()}
function updChk(){$('chkInfo').textContent=`체크 ${CHECK.size.toLocaleString()}개 / 목록 ${ROWS.length.toLocaleString()}개`;$('approve').disabled=busy||!CHECK.size}
let chkT;function saveChk(){clearTimeout(chkT);const m=MODE,ids=[...CHECK];chkT=setTimeout(()=>api('/api/checked',{ids,mode:m}).catch(()=>{}),700)}
function showJob(j){if(j.topic&&j.topic!==TOPIC)return;if(j.tabs){TABS=j.tabs;renderTabs()}if(j.quota)renderQuota(j.quota);if(j.resume)renderResume(j.resume);busy=j.status==='running';$('jobName').textContent=j.name?`${j.name} — ${({running:'도는 중',done:'끝',error:'오류',cancelled:'멈춤',idle:''})[j.status]||j.status}`:'';
 $('jobStep').innerHTML=j.status==='error'?`<span class=bad>${esc(j.error)}</span>`:esc(j.step||'쉬는 중');
 $('jobBar').style.width=j.total?Math.round(100*j.done/j.total)+'%':(busy?'15%':'0');$('cancel').disabled=!busy;
 ['explore','reanalyze','comments','resumeNow','cacheReset'].forEach(id=>$(id).disabled=busy);updChk();
 const r=j.result||{};$('jobRes').innerHTML=j.status==='done'&&(r.push_note||r.materials||r.whisper)?[r.push_note?`GitHub: ${esc(r.push_note)}`:'',
  r.description_fallback!=null?`자막 ${r.transcripts_ok}개 · 설명으로 대신 ${r.description_fallback}개${r.no_text?` · 글 없음 ${r.no_text}개`:''}`:'',
  r.materials?`<span class="${String(r.materials).startsWith('PC')?'warn':'ok'}">자료(사례 폴더): ${esc(r.materials)}</span>`:'',r.whisper?`음성인식: ${esc(r.whisper)}`:''].filter(Boolean).join('<br>'):'';
 const L=$('jobLog'),atEnd=L.scrollTop+L.clientHeight>=L.scrollHeight-20;L.textContent=(j.log||[]).join('\n');if(atEnd)L.scrollTop=L.scrollHeight;
 if(j.whisper)showWhisper(j.whisper);
 if((lastJob==='running'||waitDone)&&j.status!=='running'){waitDone=false;loadState();loadRows().then(()=>{loadAnalysis();loadShortsAnalysis()});loadReport()}lastJob=j.status}
function showWhisper(w){const run=w.status==='running'||w.status==='stopping';const left=w.pending==null?'':` · 이 탭 남은 ${num(w.pending)}개`;
 const elsewhere=run&&w.topic&&w.topic!==TOPIC,queued=(w.queued||[]).includes(TOPIC);
 if(elsewhere){$('wPill').textContent=`음성인식 — ${TOPICS.names[w.topic]||w.topic} 탭에서 도는 중`;$('wPill').className='pill';
  $('wStep').innerHTML=`<span class=mut>음성인식은 PC 에서 한 번에 하나 — 지금 ${esc(TOPICS.names[w.topic]||w.topic)} 탭(${w.done}/${w.total||'…'})${queued?' · 끝나면 이 탭 차례':' · [음성인식 시작]을 누르면 그다음 차례로 줄을 섬'}${left}</span>`;
  $('wBar').style.width='0';$('wStart').disabled=queued;$('wStop').disabled=true;lastWDone=null;return}
 $('wPill').textContent=run?`음성인식${w.pass?' '+w.pass:''} ${w.done}/${w.total||'…'}${w.failed?` (실패 ${w.failed})`:''}`:`음성인식 쉬는 중${left}`;$('wPill').className='pill '+(run?'ok':'');
 $('wStep').innerHTML=run?`${w.status==='stopping'?'멈추는 중… ':''}${esc(w.current||'준비 중 (소리 받기·모델 불러오기)')} <span class=mut>${w.pass?esc(w.pass)+' — ':''}끝 ${w.done} · 실패 ${w.failed} / 이번 대기열 ${w.total||'…'}${left}${w.rerun?' · 끝나면 새로 승인한 영상도':''}</span>`
  :`${w.status==='stopped'?'멈춤':'쉬는 중'}${left}${w.finished?` <span class=mut>(마지막 ${esc(w.finished.slice(5,16).replace('T',' '))} — 끝 ${w.done} · 실패 ${w.failed})</span>`:''}${w.note?` <span class=mut>${esc(w.note)}</span>`:''}`;
 $('wBar').style.width=w.total?Math.round(100*(w.done+w.failed)/w.total)+'%':(run?'5%':'0');$('wStart').disabled=run;$('wStop').disabled=!run||w.status==='stopping';
 const L=$('wLog'),atEnd=L.scrollTop+L.clientHeight>=L.scrollHeight-20;L.textContent=(w.log||[]).join('\n');if(atEnd)L.scrollTop=L.scrollHeight;
 if(lastWDone!==null&&w.done!==lastWDone){loadReport();loadAnalysis();loadShortsAnalysis()}lastWDone=w.done}
async function poll(){try{showJob(await api('/api/job'))}catch(e){}setTimeout(poll,busy?1000:3000)}
function pct(x){return x==null?'–':Math.round(x*100)+'%'}
let MISSING=[];
async function loadAnalysis(){let a;try{a=await api('/api/analysis')}catch(e){return}
 if(!a.generated){$('analysis').innerHTML='<span class=mut>성공 사례 분석은 승인한 영상이 생기면 만들어집니다 (analysis.md)</span>';return}
 const s=a.sources||{},ts=Object.entries(s.success_text_sources||{}).map(([k,v])=>`${k} ${v}`).join(' · ')||'-';MISSING=a.missing_ids||[];
 const inList=MISSING.filter(id=>ROWS.some(r=>r.id===id)).length;
 $('analysis').innerHTML=`<div><b>성공 사례 ${a.success}개</b> <span class=mut>(${esc(a.generated.slice(0,16).replace('T',' '))} UTC · 기준 통과 ${s.success_passed} − 뺀 것 ${(s.success_excluded||[]).length} − 채널당 제한 ${(s.success_channel_cut||[]).length})</span>
  · 글 출처 ${esc(ts)} · 댓글 ${num(s.success_comments_fetched)}/${num(s.success_comments_reported)} · 비교 집단 ${num(s.compare_group)}개 (성공 ${pct(s.compare_rate)})</div>
  <div>시청자 니즈: ${(a.needs||[]).map(([n,c])=>esc(n.split(' (')[0])+' '+num(c)).join(' · ')}${a.requests!=null?` <span class=mut>(그중 '다뤄 주세요·알려 주세요' 요청 ${num(a.requests)}개 — analysis.md 8-1)</span>`:''}</div>
  <div>형식(성공 사례 몫·시장 지수): ${(a.formats||[]).map(([f,sh,ix])=>esc(f)+' '+pct(sh)+(ix!=null?' · '+num(ix):'')).join(' / ')||'<span class=mut>자료 없음</span>'}</div>
  <div>수요/공급 지수 (1보다 크면 영상이 모자라 보임): ${(a.market_themes||[]).map(([t,i,v])=>esc(t)+' <b>'+num(i)+'</b>').join(' · ')||'<span class=mut>자료 없음</span>'}</div>
  <div>찾는데 영상이 적어 보이는 말: ${(a.gaps||[]).map(([p,n,tot])=>esc(p)+` <span class=mut>(본 영상 ${n}${tot!=null?` · 결과 ${num(tot)}`:''})</span>`).join(', ')||'<span class=mut>자동완성 자료 없음 — 검색어로 탐색하면 받음</span>'}
   ${(a.gap_candidates||[]).length?`<button id="supply">공급 확인 ${(a.gap_candidates||[]).length}개 (≈${(a.gap_candidates||[]).length*100+20}단위)</button>`:''}</div>
  <div>같은 채널 기준선: 성공 사례 ${num((a.baseline||{}).success_covered)}/${num(a.success)}개에 '채널 평소 대비' · 잘된 영상 ${num((a.baseline||{}).hits)} vs 평소 영상 ${num((a.baseline||{}).normal)} <span class=mut>(채널 평소 영상은 켤 때·승인 때 받음, analysis.md 1-2번)</span></div>
  <div>빨리 크는 작은 채널: ${num(a.fast_channels)}곳 <span class=mut>(analysis.md 7번)</span></div>
  ${a.missing_success_total?`<div class=warn style="margin-top:4px">자료를 받지 않은 성공 후보 ${a.missing_success_total}개 — 승인하면 분석에 들어갑니다 <button id="chkMissing" ${inList?'':'disabled'}>성공 후보 체크 (지금 목록에 ${inList}개)</button></div>`:''}
  <details><summary>한계 ${(a.limits||[]).length}개</summary><ul>${(a.limits||[]).map(x=>`<li>${esc(x)}</li>`).join('')}</ul></details>
  <div class=mut>전문(주제·제목·썸네일·구성·니즈·사례별): GitHub 의 ${esc(TOPIC||'<주제>')}/result/outliers/analysis.md</div>`;
 const sb=$('supply');if(sb)sb.onclick=()=>{const n=(a.gap_candidates||[]).length;if(!confirm(`수요는 있는데 영상이 적어 보이는 말 ${n}개를 직접 검색합니다 (최근 90일).\n말 하나 = 검색 1번 100단위 → 약 ${n*100+20}단위`))return;startJob('/api/supply',{n})};
 const b=$('chkMissing');if(b){b.disabled=MODE!=='long'||!inList;b.onclick=()=>{MISSING.forEach(id=>{if(ROWS.some(r=>r.id===id))CHECK.add(id)});renderRows();saveChk();$('listCard').scrollIntoView({behavior:'smooth'})}}}
let SMISSING=[];
async function loadShortsAnalysis(){let a;try{a=await api('/api/shorts_analysis')}catch(e){return}
 if(!a.generated){$('shortsAnalysis').innerHTML='<span class=mut>쇼츠를 승인하면 여기에 나옵니다 (4번 칸에서 [쇼츠]로 바꿔 탐색 → 체크 → 쇼츠 승인)</span>';return}
 SMISSING=a.missing_ids||[];const inList=MODE==='shorts'?SMISSING.filter(id=>ROWS.some(r=>r.id===id)).length:0;
 const ts=Object.entries(a.text_sources||{}).map(([k,v])=>`${k} ${v}`).join(' · ')||'-';
 const hk=Object.entries(a.hooks||{}).filter(([k,[x,y]])=>x!=null||y!=null).map(([k,[x,y]])=>`${esc(k)} ${pct(x)} vs ${pct(y)}`).join(' · ');
 $('shortsAnalysis').innerHTML=`<div><b>성공 쇼츠 ${a.success}개</b> <span class=mut>(${esc(a.generated.slice(0,16).replace('T',' '))} UTC · 받은 쇼츠 ${num(a.cases)} · 탐색에서 본 쇼츠 ${num(a.pool_shorts)})</span> · 글 출처 ${esc(ts)} · 비교 집단 ${num(a.compare_group)}개 (성공 ${pct(a.compare_rate)})</div>
  <div>길이 중앙값: 성공 쇼츠 ${a.seconds.success==null?'–':num(a.seconds.success)+'초'} · 비교 집단 나머지 ${a.seconds.others==null?'–':num(a.seconds.others)+'초'} · 첫 말까지: 성공 ${a.first_speech[0]==null?'–':a.first_speech[0]+'초'} vs 나머지 ${a.first_speech[1]==null?'–':a.first_speech[1]+'초'}</div>
  <div>첫 줄 유형 (성공 vs 나머지 받은 쇼츠): ${hk||'<span class=mut>대본이 생기면 (음성인식 — 쇼츠 먼저)</span>'}</div>
  <div>형식 (성공 쇼츠 몫 · 비교 집단 성공 비율): ${(a.formats||[]).map(([f,sh,r,n])=>esc(f)+' '+pct(sh)+' · '+pct(r)+` <span class=mut>(${n})</span>`).join(' / ')||'<span class=mut>자료 없음</span>'}</div>
  <div>시청자 니즈: ${(a.needs||[]).map(([n,c])=>esc(n.split(' (')[0])+' '+num(c)).join(' · ')}${a.requests!=null?` <span class=mut>(요청 ${num(a.requests)}개 — shorts/analysis.md 11-1)</span>`:''}</div>
  <div>수요/공급 지수: ${(a.market_themes||[]).map(([t,i])=>esc(t)+' <b>'+num(i)+'</b>').join(' · ')||'<span class=mut>자료 없음</span>'} · 찾는데 쇼츠가 적은 말: ${(a.gaps||[]).map(([p,n])=>esc(p)+` <span class=mut>(${n})</span>`).join(', ')||'<span class=mut>–</span>'}</div>
  <div>같은 채널 기준선: 성공 쇼츠 ${num((a.baseline||{}).success_covered)}/${num(a.success)}개에 '채널 평소 쇼츠 대비' · 잘된 쇼츠 ${num((a.baseline||{}).hits)} vs 평소 ${num((a.baseline||{}).normal)} · 채널 유형: ${(a.channel_types||[]).map(([t,r,n])=>esc(t)+' '+pct(r)+` (${n})`).join(' · ')}</div>
  ${a.missing_total?`<div class=warn style="margin-top:4px">자료를 받지 않은 성공 쇼츠 후보 ${a.missing_total}개 <button id="chkSMissing" ${inList?'':'disabled'} title="4번 칸이 [쇼츠]일 때">쇼츠 성공 후보 체크 (지금 목록에 ${inList}개)</button></div>`:''}
  <details><summary>한계 ${(a.limits||[]).length}개</summary><ul>${(a.limits||[]).map(x=>`<li>${esc(x)}</li>`).join('')}</ul></details>
  <div class=mut>전문(성공 쇼츠·같은 채널·주제·길이·첫 3초·끝 문장·해시태그·올린 시각·니즈·사례별): GitHub 의 &lt;주제&gt;/result/outliers/shorts/analysis.md</div>`;
 const b=$('chkSMissing');if(b)b.onclick=()=>{SMISSING.forEach(id=>{if(ROWS.some(r=>r.id===id))CHECK.add(id)});renderRows();saveChk();$('listCard').scrollIntoView({behavior:'smooth'})}}
function srcTxt(w){const s=w.text_sources;return s?`${s['자막']||0}·${s['음성인식']||0}·${s['설명']||0}`:num(w.transcripts)}
async function loadReport(){const r=await api('/api/report');if(!r.windows){$('report').innerHTML='<span class=mut>승인한 영상이 생기면 여기에 나옵니다</span>';return}
 const ts=r.text_sources||{};let h=`<div class=mut>${esc(r.generated.slice(0,16).replace('T',' '))} UTC · 승인 영상 ${r.cases}개 (글 출처: 자막 ${ts['자막']||0} · 음성인식 ${ts['음성인식']||0} · 설명으로 대신 ${ts['설명']||0} · 없음 ${ts['없음']||0}) · 승인 영상 표는 approved.md · ${esc(r.criteria)}${r.older_than_windows?` · ${r.max_weeks}주보다 오래된 영상 ${r.older_than_windows}개는 마지막 '전체' 창에`:''}</div>
 <div class=tablewrap style="margin-top:8px"><table><thead><tr><th>창</th><th class=n>영상</th><th class=n>채널</th><th class=n>이번 주 새로</th><th class=n>조회수 중앙값</th><th class=n>하루 조회수</th><th class=n>배수</th><th class=n>성공 사례</th><th class=n>길이(분)</th><th class=n>제목 글자</th><th class=n title="분석에 쓴 글: 자막 · 음성인식 · 설명(자막을 못 받아 대신)">글 출처 자막·음성·설명</th><th class=n>댓글</th></tr></thead><tbody>`;
 h+=r.windows.map(w=>`<tr><td>${esc(w.label)}</td><td class=n>${w.videos}</td><td class=n>${w.channels}</td><td class=n>${w.new_this_week.length}</td><td class=n>${num(w.views_median)}</td><td class=n>${num(w.views_per_day_median)}</td><td class=n>${num(w.ratio_median)}</td><td class=n>${w.success}</td><td class=n>${num(w.minutes_median)}</td><td class=n>${num(w.title_len_avg)}</td><td class=n>${srcTxt(w)}</td><td class=n>${num(w.comments)}</td></tr>`).join('')+'</tbody></table></div>';
 h+=r.windows.filter(w=>w.videos).map(w=>`<details><summary>${esc(w.label)} — 영상 ${w.videos}개 (이번 주 새로 ${w.new_this_week.length})</summary>
  ${w.title_features.length?`<p><b>제목 특징</b> ${w.title_features.slice(0,6).map(f=>esc(f.name)+' '+pct(f.share)).join(' · ')}</p>`:''}
  ${w.title_words.length?`<p><b>자주 쓴 낱말</b> ${w.title_words.map(x=>esc(x.word)+'('+x.count+')').join(', ')}</p>`:''}
  ${w.content_words&&w.content_words.length?`<p><b>내용에 자주 나온 낱말</b> <span class=mut>(자막·음성인식, 없으면 설명)</span> ${w.content_words.map(x=>esc(x.word)+'('+x.count+')').join(', ')}</p>`:''}
  ${w.hooks.length?`<p><b>도입부</b> <span class=mut>(자막·음성인식은 첫 20초${w.transcripts?` · 말 속도 ${num(w.syl_per_sec_median)} 음절/초`:''}, 없으면 설명 앞부분)</span></p><ul>${w.hooks.map(x=>`<li><span class="tag ${x.src==='설명'?'x':'d'}">${esc(x.src||'자막')}</span>${esc(x.title.slice(0,30))}: “${esc(x.hook)}”</li>`).join('')}</ul>`:''}
  ${w.comment_needs.length?`<p><b>댓글 ${num(w.comments)}개 니즈</b> ${w.comment_needs.map(n=>esc(n.name)+' '+pct(n.share)).join(' · ')}</p><ul>${w.top_comments.map(c=>`<li>👍${num(c.likes)} “${esc(c.text)}”</li>`).join('')}</ul>`:''}
  <p><b>상위 영상</b> (하루 조회수 순)</p><ol>${w.top_videos.map(v=>`<li><a href="${v.url}" target=_blank rel=noopener>${esc(v.title)}</a> <span class=mut>${esc(v.channel)} · ${num(v.views)}회 · 하루 ${num(v.views_per_day)} · ${v.published}</span></li>`).join('')}</ol></details>`).join('');
 $('report').innerHTML=h}
$('cacheReset').onclick=async()=>{if(!confirm('이 주제의 탐색 캐시(검색 결과·영상 정보)와 탐색 목록(체크 포함)을 치웁니다.\n지우지 않고 .yt_work/old/ 로 옮기며, 승인한 자료·분석 결과는 그대로입니다.\n다음 탐색은 처음부터 새로 검색합니다 (검색 1번 = 100단위).'))return;
 try{const r=await api('/api/cache/reset',{});alert(r.message);ROWS=[];CHECK=new Set();renderRows();await loadRows();estimate()}catch(e){alert(e.message)}};
$('ntMake').onclick=async()=>{try{const r=await api('/api/topic/new',{folder:$('ntFolder').value.trim(),name:$('ntName').value.trim(),keywords:$('ntKw').value,push:$('ntPush').checked});
 say('ntMsg',r.message+' — 위쪽에 새 탭이 생겼습니다','ok');$('ntFolder').value='';$('ntName').value='';$('ntKw').value='';await loadState();switchTab(r.folder)}catch(e){say('ntMsg',e.message,'bad')}};
$('resumeNow').onclick=()=>startJob('/api/resume',{});
$('saveEnv').onclick=async()=>{try{const r=await api('/api/env',{YOUTUBE_API_KEY:$('ytkey').value,GITHUB_TOKEN:$('ghtok').value});$('ytkey').value='';$('ghtok').value='';
 say('envMsg',r.changed.length?`저장함: ${r.changed.join(', ')}`:'바뀐 것 없음 (넣은 칸만 저장)','ok');loadState()}catch(e){say('envMsg',e.message,'bad')}};
$('saveKw').onclick=async()=>{try{const r=await api('/api/keywords',{text:$('kw').value,push:$('kwPush').checked});say('kwMsg',r.message,'ok');$('kwCount').textContent=`검색어 ${r.count}개`;estimate()}catch(e){say('kwMsg',e.message,'bad')}};
$('tgAdd').onclick=async()=>{const v=$('tgIn').value.trim();if(!v)return;say('tgMsg','확인 중…');try{const r=await api('/api/targets/add',{text:v});
 const ok=r.results.filter(x=>x.ok),bad=r.results.filter(x=>!x.ok);
 $('tgMsg').innerHTML=ok.map(x=>`<span class=ok>✓ ${x.kind==='channel'?`채널 ${esc(x.title)} (영상 ${num(x.videos)}개)`:`영상 ${esc(x.title||x.id)}`}${x.note?' — '+esc(x.note):''}</span>`).concat(
  bad.map(x=>`<span class=bad>✕ ${esc(x.input.slice(0,60))} — ${esc(x.error)}</span>`)).join('<br>');$('tgMsg').className='msg';
 $('tgIn').value=bad.map(x=>x.input).join('\n');renderTargets(r.targets);estimate()}catch(e){say('tgMsg',e.message,'bad')}};
$('tgIn').onkeydown=e=>{if(e.key==='Enter'&&(e.ctrlKey||e.metaKey))$('tgAdd').click()};
$('weeks').oninput=()=>{lsSet('ytWeeks',$('weeks').value);estimate()};
$('foreign').onchange=async()=>{const on=$('foreign').checked;try{const r=await api('/api/foreign',{on});$('foreign').checked=!!r.include_foreign;say('foreignMsg','외국 영상 '+r.message,'ok');estimate()}catch(e){$('foreign').checked=!on;say('foreignMsg',e.message,'bad')}};$('useKw').onchange=()=>{lsSet('ytUseKw',$('useKw').checked?'1':'0');estimate()};
async function startJob(p,b){try{waitDone=true;await api(p,b);busy=true;showJob(await api('/api/job'))}catch(e){waitDone=false;alert(e.message)}}
$('explore').onclick=()=>startJob('/api/explore',{weeks:+$('weeks').value,keywords:$('useKw').checked,mode:MODE});
$('approve').onclick=async()=>{const ids=ROWS.filter(r=>CHECK.has(r.id)).map(r=>r.id);if(!ids.length)return;
 const msg=MODE==='shorts'?`체크한 쇼츠 ${ids.length}개의 설명·자막·세로 표지·댓글 전부를 받고 → 채널 평소 쇼츠 → 쇼츠 분석 → GitHub 에 바로 올립니다.\n자막을 못 받은 쇼츠는 음성인식을 뒤에서 합니다 (쇼츠 먼저).\n(댓글 100개에 할당량 1단위 · 채널 하나 약 2단위)`
  :`체크한 영상 ${ids.length}개의 설명·자막·썸네일·댓글 전부를 받고 → 주별 분석 → GitHub 에 바로 올립니다.\n자막을 못 받은 영상은 영상 설명으로 대신 분석하고, 음성인식은 그다음 뒤에서 합니다.\n(댓글 100개에 할당량 1단위)`;
 if(!confirm(msg))return;
 startJob('/api/approve',{ids,whisper:$('autoW').checked,mode:MODE})};
document.querySelectorAll('#modeSeg button').forEach(b=>b.onclick=()=>setMode(b.dataset.m));
$('cancel').onclick=()=>api('/api/cancel',{});$('reanalyze').onclick=()=>startJob('/api/analyze',{});$('comments').onclick=()=>startJob('/api/comments',{});
$('wStart').onclick=async()=>{try{const r=await api('/api/whisper',{});if(!r.ok)alert(r.message);showJob(await api('/api/job'))}catch(e){alert(e.message)}};
$('wStop').onclick=async()=>{if(!confirm('음성인식을 멈출까요? (끝난 영상의 대본은 남고, 하던 영상은 다음에 처음부터)'))return;await api('/api/whisper/stop',{});showJob(await api('/api/job'))};
['flt','fShort','fRel'].forEach(id=>$(id).addEventListener('input',renderRows));
$('chkAll').onclick=()=>{visible().forEach(r=>CHECK.add(r.id));renderRows();saveChk()};$('chkNone').onclick=()=>{CHECK.clear();renderRows();saveChk()};
$('chkRec').onclick=()=>{CHECK=new Set(REC);renderRows();saveChk()};
applyTabPrefs();loadState().then(()=>{loadRows().then(()=>{loadAnalysis();loadShortsAnalysis()});loadReport()}).catch(e=>document.body.insertAdjacentHTML('afterbegin',`<p class=bad style="padding:16px">${esc(e.message)}</p>`));poll();
</script></body></html>
"""


if __name__ == "__main__":
    sys.exit(main())
