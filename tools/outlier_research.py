#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v2.2 — 2026-10-15 — 할당량을 덜 씀 (사용자 지시: "유튜브 분석 코드를 최대한 api 사용량 덜쓰는 방법(단어 줄이는 방법 말고) 찾아서
#          수정해보고" · "분석기 여러개 열어서 각자 다른 주제로 탐색해도 되지?"). 검색어는 그대로, 같은 정보를 덜 자주·덜 겹치게 받음:
#          ① 적응형 검색 캐시 (search_ttl — 검색 1번 = 100단위, 할당량의 거의 전부): 새로 고칠 때 지난 결과·다른 검색어 결과에 없던
#             '새로 보인 쓸 만한 영상'(롱폼·라이브 아님·한국어·기간 안)을 적어 두고, 그것이 2개 이하면 다음 새로 고침을 늦춤
#             (7일 → 14일 → 21일, 탐색 기간의 1/4 이하 — 8주면 14일까지), 많으면 7일로. 처음·예전 캐시는 7일 그대로
#          ② 채널 업로드 목록을 새 영상만 (channel_uploads — 아는 영상이 나오면 멈춤: 영상 500개 채널 새로 고침 10단위 → 1단위)
#          ③ 영상 정보 캐시 시간을 올린 지 오래된 영상은 길게 (30일 안 24시간 · 180일 안 3일 · 그보다 오래 7일 — 조회수가 거의 안 바뀜)
#          ④ 댓글 전부를 받을 때 한 쪽(100개 이하)으로 끝나는 영상은 인기 댓글 쪽(같은 댓글)을 건너뜀 (영상마다 1단위)
#          ⑤ Api(ledger=) — 요청마다 키 장부(tools/pc_analysis.py KeyLedger)에 먼저 적고 실패하면 돌려줌: 같은 키를 쓰는 다른 창·주제와
#             함께 셈 → 창 여러 개가 동시에 탐색해도 하루 한도를 넘지 않음. Google 의 하루 한도 답은 장부에 '오늘 끝'으로
# (v2.1 — 2026-10-14 — 수요·공급과 채널 성장을 셀 자료도 모음 (사용자 지시: "수요 대비 영상 공급이 별로 없는지도 파악해야해
#          이외에도 내가 말한 목표를 달성하기 위한 모든 분석 방법을 찾아서 반영해" — 목표: 조회수가 높고 구독자가 많이 모이는 영상):
#          ① 검색 캐시에 YouTube 가 알려 준 결과 수(pageInfo.totalResults — 그 기간에 올라온 영상 수 추정 = 공급)도 저장 (할당량 같음)
#          ② 채널 구독자 수를 받을 때 개설일·영상 수·총 조회수도 (channels.list part=snippet,statistics — 같은 1단위) +
#             받을 때마다 구독자 수 기록(history — 채널 성장 속도) — 예전 캐시는 한 번 다시 받음 (50채널 1단위)
#          ③ fetch_autocomplete: YouTube 검색어 자동완성(할당량 0, 7일 캐시 .cache/autocomplete.json) = 사람들이 찾는 말(수요)
#          ④ search_supply: 자동완성 말 하나의 최근 90일 공급 확인 (검색 1번 100단위 + 영상 정보) — 웹 화면 [공급 확인]이 부름)
# (v2.0.2 — 2026-10-14 — 안내 글만: 사례 폴더는 저장소가 공개여도 GitHub 에 올라감 (사용자 지시 "그냥 공개에서 다 올리도록 해" — 분석기 v2.9.3
#          UPLOAD_CASES_TO_PUBLIC_REPO). 받기·고르기·숫자는 그대로)
# (v2.0.1 — 2026-10-14 — --offline 다시 만들기가 결과를 지우던 것 고침 (사용자 질문 "분석 결과 다 올라온거야?" — GitHub 에
#          '후보 0개' 요약이 올라가 있었음): 음성인식이 하나 끝날 때마다 부르는 --offline 이 검색 캐시를 못 찾으면(결과 폴더를 지웠거나
#          7일 지남) 후보 0개로 summary.md·downloads.md·status.json·csv 를 덮어쓰고 사례 폴더(01_·P01_)까지 _old/ 로 옮길 수 있었음 →
#          ① --offline 은 오래된 검색 캐시도 씀 ② 그래도 후보가 0이면 아무것도 쓰지·옮기지 않고 있던 결과를 그대로 둠)
# (v2.0 — 2026-10-14 — 라이브 방송·외국 영상은 탐색 대상에서 뺌 (사용자 지시: "라이브 방송, 외국 영상은 탐색 대상에서 제외"):
#          exclusion_reason() — 라이브 = 지금 라이브·예정(liveBroadcastContent) 또는 라이브였던 영상(liveStreamingDetails, videos.list
#          같은 1단위로 같이 받음) 또는 제목에 라이브·생방송·스트리밍·LIVE. 외국 = 영상 언어(defaultAudioLanguage·defaultLanguage)가
#          한국어가 아님, 언어 표시가 없으면 제목에 한글이 없음. build_rows 가 뺌 (keep 으로 넘긴 영상 — 웹 화면에서 주소로 직접
#          넣은 것 — 은 남기고 표시만). 예전 캐시(라이브 여부 없음)는 다시 받음)
# (v1.9 — 2026-10-14 — 자막이 계속 막히던 것 고침 (사용자 지시: "왜 자꾸 자막 다운로드 막히는지 에러 찾아서 수정해"):
#          원인(PC 로그): YouTube 자막 서버가 PC 의 IP 에 HTTP 429(Too Many Requests)로 답함 → youtube-transcript-api 'IpBlocked'
#          35개 중 26개, 분석기 yt-dlp 자막도 8/8 이 429. 그런데 소리 받기는 됨(음성인식 17/17 성공). 예전 코드는 IpBlocked 를
#          '네트워크 실패 — 다음 회차에 다시'로 보고 음성인식에서 빼서, 매 회차 같은 자막을 또 요청 → 차단이 이어지고 대본은 영영 없음.
#          ① 자막 서버 차단(IpBlocked·RequestBlocked·429)은 음성인식 대기열로 (is_caption_block) — 연결 자체 실패만 다음 회차에 다시
#          ② 차단 쉬기: 연속 2번 막히면 6시간 동안 모든 도구(분석기·웹 화면 포함)가 자막 요청을 쉼 (.yt_work/caption_block.json)
#          ③ 자막 요청 사이 1.5~3초 쉼 (짧은 시간에 몰아서 요청하지 않게)
#          ④ 웹 화면(tools/web_ui.py)용: fetch_video_infos·fetch_channel_subs(영상·구독자 정보 따로), channel_uploads(채널의 모든 영상))
# (v1.8 — 2026-10-13 — 검색어는 그룹 없이 한 줄에 하나씩 (사용자 지시: "걍 검색어 내가 수정해도 돌아가게 하면 안돼? 꼭 그룹을
#          지정해야하나 검색어만 넣어도 되잖아"): <주제>/keywords.txt 가 있으면 그것이 검색어 목록 (read_keyword_list — 분석기 v2.8.0 과
#          같은 규칙), 없으면 keywords.toml 의 KEYWORD_GROUPS. EXTRA_KEYWORDS 도 검색. 잘된 영상 태그 검색어(--tag-keywords)는 기본 0 —
#          내가 적은 검색어만 검색 (지운 검색어가 태그로 되살아나지 않게))
# (v1.7 — 2026-10-13 — 검색어 전부·업로드 날짜 (사용자 지시: "그냥 검색어를 재테크 관련 태그로 찾아서 다 그걸로 탐색해봐
#          그리고 탐색 목록에 업로드 날짜도 같이 표시해"):
#          ① --per-group 0(기본) = 검색어 그룹의 검색어 전부 (keywords.toml 은 tools/tag_keywords.py 가 실제 영상 태그로 채움).
#             그룹이 달라도 같은 검색어(띄어쓰기·대소문자만 다름)는 한 번만 검색
#          ② downloads.md·downloads.csv·summary.md 표에 업로드 날짜(YYYY-MM-DD, 며칠 전) 칸
#          ③ 잘된 영상 태그 검색어(tag_keywords.json)는 검색어 목록에 이미 있는 것을 빼고 씀 (같은 검색 두 번 안 함))
# (v1.6 — 2026-10-13 — 태그 검색어·받은 자료 표·오프라인 다시 만들기 (사용자 지시: "태그도 검색어에 포함하도록 해서 탐색하고 …
#          탐색 목록에서 어떤 영상을 자료로 받았는지, 자막, 댓글 등 다운 성공한게 뭔지 표로 정리해서 깃허브에서 바로 확인 가능한 확장자로"):
#          ① 태그 검색어 (--tag-keywords 5): 잘된 영상(배수 ≥ --min-ratio 또는 조회수 상위 50, 주제 관련)의 태그 중 검색어에 없고
#             채널 2곳 이상이 쓴 것을 골라 검색 (tag_keywords.json 에 고정 — 매번 바뀌지 않게, 검색 1번 100단위)
#          ② downloads.md (GitHub 에서 바로 보이는 표) + downloads.csv: 탐색한 검색어(키워드·태그)별 결과, 자료로 받은 영상마다
#             자막(자막/음성인식/대기/막힘)·댓글(받은 수/영상 표시 수)·썸네일·설명·태그, 분석기 성공사례도 함께
#          ③ --offline: API·자막·썸네일 요청 없이 캐시·받은 파일로 요약·표·상태만 다시 (음성인식이 하나 끝날 때마다 분석기가 부름))
# (v1.5 — 2026-10-13 — 댓글 2단계 (사용자 지시: "너무 오래 걸리는데 댓글 전체 받아서 그런거야? … 좋은 해결 방법 생각해봐"):
#          ① 1단계: 모든 사례의 인기 댓글 100개(관련성 순 1쪽 = 영상마다 1단위)를 먼저 → 할당량이 모자라도 분석은 바로 시작 (status.json ready)
#          ② 2단계: 그다음 사례마다 댓글 전부(시간순 + 답글) — 남은 할당량으로, 못 받은 것은 다음 실행이 이어서 (같은 댓글은 id 로 하나로)
#          ※ 댓글은 100개에 1단위라 싸다 — 하루 할당량의 대부분은 검색(1번 100단위). 오래 걸린 까닭은 고정 배분(tools/pc_analysis.py v1.3 에서 고침))
# (v1.4 — 2026-10-13 — 주제별 키 (사용자 지시: "동시에 병렬로 다른 주제 분석도 가능하도록 … 키설정 파일도 여러개"):
#          키를 <주제폴더>/.env → 환경 변수 YOUTUBE_API_KEY_<폴더> → 환경 변수 YOUTUBE_API_KEY → 맨 위 .env 순으로 찾음.
#          주제 여러 개를 한 번에 돌리면 키마다 할당량을 따로 셈 (같은 키를 쓰는 주제끼리만 --quota 를 나눠 씀))
# (v1.3 — 2026-10-13 — 댓글 전부·조회수 상위 영상 (사용자 지시: "비공개로 돌릴테니까 전부 다 업로드되게 하고 댓글은 전부 받도록 수정해
#          그리고 구독자 수 상관없이 조회수 많이 나온 영상 댓글은 전부 받아야해"):
#          ① 댓글 전부: 최상위 댓글(commentThreads, 시간순, 100개씩) + 답글(5개 넘는 것은 comments.list) — 기본 --comments 0(전부)
#             쪽마다 comments.jsonl 에 덧붙이고 comments_state.json 에 다음 쪽을 저장 → 할당량이 끝나면 다음 실행이 그 쪽부터
#          ② 조회수 상위 영상(구독자 수 상관없음, --popular 20): 주제 관련(keywords.toml RELEVANCE_*, 분석기 topic_relevance 규칙)·
#             4분 이상·최근 --fallback-days 일 → 조회수 순, 채널당 2개 → 설명·자막·썸네일·댓글 전부 (폴더 P01_<영상ID>/, popular.csv)
#          ③ 댓글 기록에 답글 여부(parent)·채널 주인 댓글(creator) — 작성자 이름은 저장하지 않음)
# (v1.2 — 2026-10-13 — PC 실행·이어서 돌리기 (사용자 지시: "분석기 코드 pc에서 돌릴 수 있도록", "api 할당량이 초기화된 시간이 되면
#          다시 자동으로 분석결과를 확인 못한 부분부터 새로 추가로"):
#          ① 검색어는 <주제>/keywords.toml 에서 (분석기 v2.4.0과 같은 파일, 없으면 analyzer_config.toml)
#          ② 검색 결과 캐시(.cache/search_*.json, 기본 7일) — 다시 돌리면 받은 검색은 할당량 0, 못 한 검색만 새로
#          ③ 할당량이 끝나도 멈추지 않고 캐시로 계속 → status.json 에 못 한 검색·영상 정보·댓글을 적음 (tools/pc_analysis.py 가 읽음)
#          ④ 사례 폴더에 이미 받은 자막(transcript.json)·썸네일·댓글이 있으면 다시 받지 않음
#          ⑤ summary.md 에 자막 첫 1분 발췌·구간별 흐름(90초마다 첫 문장 앞부분), Python 3.10(tomli) 지원
#          ⑥ 주제 이름을 설정의 [topic] TOPIC 에서 제대로 읽음, EXCLUDE_KEYWORDS 를 [keywords] 섹션에서도 읽음
#          ⑦ 영상 정보 캐시는 24시간·구독자 수는 7일 지나면 다시 받음 (조회수가 바뀌므로). 할당량이 없으면 예전 숫자로 계속
#          ⑧ 검색은 이번 실행 한도에서 150단위를 남기고 멈춤 → 남은 단위로 영상 정보·구독자·댓글은 계속 받음)
# (v1.1 — 2026-10-12 — 기본 검색에 20분 넘는 영상도, 키워드는 그룹마다 1개(할당량 같게)
#  v1.0 — 2026-10-12 — 신규: 최근·작은 채널·조회수가 구독자의 몇 배인 롱폼 영상(작은 채널 성공 사례)의 내용(자막·설명·챕터)과 댓글)
r"""
사용법 (저장소 최상위, 또는 PC 실행 폴더):
  python tools/outlier_research.py economic                     # 주제 하나
  python tools/outlier_research.py economic --per-group 2 --top 20
  옵션: --per-group 0   검색어 그룹마다 검색할 검색어 수 (0 = 전부, 기본. <주제>/keywords.toml 의 KEYWORD_GROUPS 앞에서부터)
        --days 180      최근 며칠 안에 올라온 영상 (모자라면 --fallback-days 365 까지 넓힘)
        --max-subs 50000 --min-ratio 3 --min-views 10000 --min-sec 240   성공 사례 기준
        --top 15        자막·댓글을 모을 성공 사례 수 (채널당 최대 --per-channel 2)
        --comments 0    사례마다 최상위 댓글을 몇 개까지 (0 = 전부, 기본). 답글도 전부 (--no-replies 면 최상위만)
        --popular 20    구독자 수와 상관없이 조회수 상위 영상 수 (주제 관련·4분 이상·최근 --fallback-days 일) — 댓글 전부. 0 이면 안 함
        --no-long       20분 넘는 영상은 검색하지 않음 (기본은 4~20분과 20분 넘음 둘 다)
        --quota 9000    이번 실행 API 단위 한도 (하루 10,000 — 분석기와 같은 키면 나눠 쓴다)
        --search-ttl-hours 168   검색 결과 캐시 유효 시간 (이 안에 다시 돌리면 받은 검색은 할당량 0)
        --from-existing 분석기 결과에서 고르기 (API 키 없이)
        --refresh       캐시 무시 (검색·영상 정보·자막·썸네일·댓글 모두 새로)

수집 방법:
  YouTube Data API v3 — 키: <주제폴더>/.env → 환경 변수 YOUTUBE_API_KEY_<폴더> → YOUTUBE_API_KEY → 맨 위 .env (분석기와 같은 파일):
    검색 search.list (최근 --fallback-days 일·조회수 순·4~20분·20분 넘음, KR·ko) — 100단위/번 · 영상 videos.list · 채널 channels.list
    · 댓글 commentThreads.list(최상위 100개) · comments.list(답글 100개) — 1단위/번. 검색 횟수 = 검색어 수(--per-group 0 이면 전부) × 2(길이 둘).
    댓글 전부의 할당량: 영상마다 약 (최상위 댓글 수 ÷ 100) + (답글이 5개 넘는 댓글 수) 단위. 하루에 다 못 받으면 다음 실행이 이어서.
  할당량이 끝나면(이번 실행 한도 또는 하루 10,000): 새 요청을 멈추고 캐시에 있는 것만으로 결과를 만든다.
    못 한 검색·영상 정보·댓글은 status.json 의 pending 에 남는다 → 할당량이 초기화된 뒤 같은 명령을 다시 돌리면 그 부분만 새로 받는다.
    (태평양 자정 = 한국 시간 오후 4시(서머타임) / 5시. tools/pc_analysis.py 가 자동으로 기다렸다가 다시 돌린다)
  자막: youtube-transcript-api (한국어). 집 PC 에서는 받힌다. 클라우드는 네트워크 정책·YouTube 차단으로 못 받을 수 있다
        (2026-10-12: RequestBlocked / 2026-10-12 다른 환경: ProxyError 403). 못 받으면 status.json 에 적고 설명·챕터·댓글로 분석한다.
  yt-dlp 로 YouTube 페이지를 직접 읽는 방법은 쓰지 않는다 (봇 확인을 피해 가지 않는다).

결과 (<주제>/result/outliers/):
  candidates.csv  검색에서 걸린 롱폼 후보 전부 (구독자·조회수·배수·올린 날)                 ← git
  outliers.csv    기준을 통과한 성공 사례 (배수 순)                                        ← git
  downloads.md    받은 자료 표: 검색어(키워드·태그)별 탐색 결과, 영상마다 자막·댓글·썸네일 성공 여부  ← git (GitHub 에서 바로 보임)
  downloads.csv   같은 표 (영상마다 한 줄)                                                  ← git
  tag_keywords.json 태그에서 고른 검색어 (한 번 고르면 고정)                                 ← git
  popular.csv     조회수 상위 (구독자 수 상관없음, 주제 관련·롱폼)                         ← git
  summary.md      사례 표 + 사례마다 설명 앞부분·챕터·도입부·첫 1분·구간별 흐름·말 속도·인기 댓글 (짧게 인용) ← git
  status.json     이번 실행 상태: 검색 완료/남은 검색(pending)·할당량 멈춤·자막·썸네일·댓글 받은 수 (이어서 돌리기용)  ← git
  <순위>_<영상ID>/ 성공 사례 · P<순위>_<영상ID>/ 조회수 상위 — metadata.json · description.txt · transcript.txt·transcript.json ·
                  comments.csv(전부, 좋아요 순)·comments.jsonl(받은 순서)·comments_state.json(이어 받기) · thumbnail.jpg
                  ← 다른 사람의 글·이미지. 공개 저장소에도 GitHub 에 올라간다 (2026-10-14 사용자 지시 — 분석기 v2.9.3 UPLOAD_CASES_TO_PUBLIC_REPO)
  _old/           이번 상위에서 빠진 사례 폴더 (다시 들어오면 재사용, git 에 올리지 않음)
  .cache/         영상 정보·검색 결과 캐시 (git 에 올리지 않음)
로그: [STAGE] [시각] key=value (START·SEARCH·VIDEO·FILTER·DEEP·STATUS·DONE)
※ 연구·교육용. 다른 채널 영상을 내려받지 않는다(메타데이터·자막 글·댓글만).
"""
import argparse
import collections
import csv
import hashlib
import json
import logging
import os
import re
import shutil
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

try:
    import tomllib                      # Python 3.11+
except ModuleNotFoundError:             # Python 3.10 → tomli (분석기가 자동 설치)
    import tomli as tomllib

ROOT = Path(__file__).resolve().parent.parent
VERSION = "v2.2"
LOG = logging.getLogger("outlier")
HANGUL = re.compile(r"[가-힣]")
SEARCH_TTL_HOURS = 168
SEARCH_TTL_MAX_H = 504        # v2.2 적응형 검색 캐시: 결과가 거의 안 바뀌는 검색은 7일 → 14일 → 21일까지 늦춤
SEARCH_TTL_WINDOW_FRAC = 0.25 # 그래도 탐색 기간의 1/4 보다 오래 묵히지 않음 (8주 → 14일 · 12주 → 21일) — 최근 영상을 너무 놓치지 않게
SEARCH_NOVEL_LOW = 2          # 지난 새로 고침에서 '새로 보인 쓸 만한 영상'(다른 검색에도 없던 롱폼·한국어·라이브 아님·기간 안)이 이 이하면 늦춤
SEARCH_MAX_LEVEL = 2          # 늦추는 단계 (0 = 7일, 1 = 14일, 2 = 21일)
MIN_LONGFORM_SEC = 240        # '쓸 만한 영상' 판단용 롱폼 기준 (--min-sec 기본과 같음)
VIDEO_TTL_HOURS = 24          # 영상 조회수: 하루 지나면 다시 (videos.list 50개 = 1단위)
VIDEO_TTL_BY_AGE = ((30, 24), (180, 72), (None, 168))   # v2.2: 올린 지 30일 안 = 24시간 · 180일 안 = 3일 · 그보다 오래 = 7일
CHANNEL_TTL_HOURS = 168       # 구독자 수: 7일
SEARCH_RESERVE = 150          # 검색이 한도를 다 쓰지 않게 남기는 단위 (영상 정보·구독자·댓글용)
OUTLINE_EVERY_SEC = 90
NETWORK_ERRORS = ("ProxyError", "ConnectionError", "Timeout", "URLError")       # 연결 자체가 안 됨 → 다음 회차에 다시 (v1.9)
CAPTION_BLOCK_ERRORS = ("RequestBlocked", "IpBlocked", "TooManyRequests", "429")   # YouTube 자막 서버가 거부 → 음성인식으로 (v1.9)
CAPTION_BLOCK_AFTER = 2       # 자막 요청이 연속 이만큼 막히면
CAPTION_COOLDOWN_H = 6        # 이 시간 동안 모든 도구가 자막 요청을 쉼 (.yt_work/caption_block.json — 분석기·웹 화면도 봄)
CAPTION_PACE_SEC = (1.5, 3.0)  # 자막 요청 사이 쉬는 시간 (초, 무작위)


def log(stage, level=logging.INFO, **kv):
    LOG.log(level, "[%s] [%s] %s", stage, datetime.now().isoformat(timespec="seconds"),
            " ".join(f"{k}={json.dumps(v, ensure_ascii=False) if isinstance(v, str) and ' ' in v else v}" for k, v in kv.items()))


def _flat(data):
    """TOML 섹션을 한 단계로 펼침 (KEYWORD_GROUPS 처럼 값이 표인 설정은 그대로) — 분석기 flatten_config 와 같은 규칙."""
    out = {}
    for k, v in data.items():
        if k == "KEYWORD_GROUPS" or not isinstance(v, dict):
            out[k] = v
        else:
            out.update(v)
    return out


KEYWORD_LIST_FILE = "keywords.txt"      # 검색어만 한 줄에 하나씩 (v1.8) — 있으면 KEYWORD_GROUPS 대신


def read_keyword_list(path):
    """keywords.txt → 검색어 목록 (분석기 v2.8.0 read_keyword_list 와 같은 규칙). 한 줄에 하나, '#' 으로 시작하는 줄·빈 줄은 무시,
    띄어쓰기·대소문자만 다른 검색어는 처음 것만, "검색어", 처럼 써도 됨. UTF-8(BOM) — 안 되면 cp949. 파일이 없으면 None."""
    path = Path(path)
    if not path.is_file():
        return None
    raw = path.read_bytes()
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError:
        text = raw.decode("cp949", errors="replace")
    out, seen = [], set()
    for line in text.splitlines():
        k = line.strip().rstrip(",").strip().strip('"').strip("'").strip()
        if not k or k.startswith("#"):
            continue
        key = "".join(k.split()).lower()
        if key not in seen:
            seen.add(key)
            out.append(k)
    return out


def load_keywords(topic, per_group):
    """→ ([(그룹, 검색어)], 제외 낱말, 주제 이름, 검색어 파일 경로, 관련어 {strong, weak, exclude}). 검색어는 keywords.toml(분석기 v2.4.0), 없으면 analyzer_config.toml."""
    cfg_p = ROOT / topic / "analyzer_config.toml"
    if not cfg_p.is_file():
        raise SystemExit(f"[START] ❌ {cfg_p} 없음 — 주제 폴더 확인")
    cfg = _flat(tomllib.loads(cfg_p.read_text("utf-8")))
    kw_name = str(cfg.get("KEYWORDS_FILE") or "keywords.toml")
    kw_p = Path(kw_name) if Path(kw_name).is_absolute() else cfg_p.parent / kw_name
    src = _flat(tomllib.loads(kw_p.read_text("utf-8"))) if kw_p.is_file() else cfg
    groups = src.get("KEYWORD_GROUPS") or cfg.get("KEYWORD_GROUPS") or {}
    txt_p = cfg_p.parent / KEYWORD_LIST_FILE
    flat = read_keyword_list(txt_p)
    if flat:                                                       # v1.8: keywords.txt 가 있으면 그것만 (그룹·--per-group 무시)
        groups, per_group, kw_p = {"검색어": flat}, 0, txt_p
    extra = [str(k) for k in (src.get("EXTRA_KEYWORDS") or cfg.get("EXTRA_KEYWORDS") or []) if str(k).strip()]
    if extra:
        groups = {**groups, "기타": list(groups.get("기타", [])) + extra}
    kws, seen = [], set()
    for g, ks in groups.items():
        for k in (ks if per_group <= 0 else ks[:per_group]):          # 0 이하 = 그룹의 검색어 전부 (v1.7)
            k = str(k).strip()
            if k and re.sub(r"\s+", "", k).lower() not in seen:          # 그룹이 달라도 같은 검색어는 한 번만
                seen.add(re.sub(r"\s+", "", k).lower())
                kws.append((g, k))
    exclude = [w for w in (src.get("EXCLUDE_KEYWORDS") or cfg.get("EXCLUDE_KEYWORDS") or []) if w]
    rel = {"strong": [t for t in (src.get("RELEVANCE_TERMS") or cfg.get("RELEVANCE_TERMS") or []) if str(t).strip()],
           "weak": [t for t in (src.get("RELEVANCE_WEAK_TERMS") or cfg.get("RELEVANCE_WEAK_TERMS") or []) if str(t).strip()],
           "exclude": [t for t in (src.get("RELEVANCE_EXCLUDE") or cfg.get("RELEVANCE_EXCLUDE") or []) if str(t)]}
    return kws, exclude, cfg.get("TOPIC", topic), (kw_p if kw_p.is_file() else cfg_p), rel


API = "https://www.googleapis.com/youtube/v3/"
COST = {"search": 100, "videos": 1, "channels": 1, "commentThreads": 1, "comments": 1, "playlistItems": 1}


class QuotaStop(Exception):
    """kind: run_budget(이번 실행 한도 --quota) / daily(하루 할당량 소진)."""

    def __init__(self, msg, kind):
        super().__init__(msg)
        self.kind = kind


class Api:
    """YouTube Data API v3 (키는 환경 변수 YOUTUBE_API_KEY — 값은 로그에 쓰지 않음). 사용 단위를 세고 한도 전에 멈춘다.
    검색(100단위)은 한도에서 SEARCH_RESERVE 를 남기고 멈춘다 → 남은 단위로 영상 정보·구독자·댓글(1단위)은 계속 받는다.
    하루 할당량이 끝나면(daily) 같은 실행에서는 새 요청을 하지 않는다. stopped = 처음 멈춘 까닭."""

    def __init__(self, key, quota, ledger=None, what="", topic=""):
        self.key, self.quota, self.used, self.stopped = key, quota, 0, None
        self.last_total = None        # 마지막 검색의 pageInfo.totalResults (v2.1 — 공급 추정)
        self.channel_meta = {}        # 채널ID → 개설일·영상 수·총 조회수·이름 (v2.1 — 채널 성장)
        self.ledger, self.what, self.topic = ledger, what, topic   # v2.2: 키 장부(pc_analysis.KeyLedger) — 요청마다 먼저 잡고 실패하면 돌려줌
        self.calls = collections.Counter()                         # v2.2: 종류별 요청 수 (로그·시험용)

    def get(self, kind, **params):
        if self.stopped in ("daily", "offline"):
            raise QuotaStop("새 요청 안 함 (" + ("하루 할당량 소진" if self.stopped == "daily" else "--offline") + ")", self.stopped)
        limit = self.quota - (SEARCH_RESERVE if kind == "search" else 0)
        if self.used + COST[kind] > limit:
            self.stopped = self.stopped or "run_budget"
            raise QuotaStop(f"이번 실행 한도 {self.quota}단위 — 사용 {self.used}" + (f" (검색은 {SEARCH_RESERVE}단위 남김)" if kind == "search" else ""),
                            "run_budget")
        if self.ledger is not None and not self.ledger.reserve(COST[kind], self.what or kind, self.topic,
                                                               keep=SEARCH_RESERVE if kind == "search" else 0):
            self.stopped = self.stopped or "shared"     # 다른 창·주제가 같은 키로 써서 오늘 남은 양이 없음 (1단위 요청은 남았으면 계속)
            raise QuotaStop(f"같은 키의 오늘 남은 할당량이 모자람 (다른 창·주제 포함, {kind} {COST[kind]}단위"
                            + (f" + 검색은 {SEARCH_RESERVE}단위 남김" if kind == "search" else "") + ")", "shared")
        url = API + kind + "?" + urllib.parse.urlencode({**params, "key": self.key})
        ok = False
        try:
            for attempt in range(3):
                try:
                    with urllib.request.urlopen(urllib.request.Request(url), timeout=30) as r:
                        data = json.loads(r.read().decode("utf-8"))
                        self.used += COST[kind]
                        self.calls[kind] += 1
                        ok = True
                        return data
                except urllib.error.HTTPError as e:
                    body = e.read().decode("utf-8", "replace")[:300]
                    if e.code == 403 and ("quota" in body.lower()):
                        self.stopped = "daily"
                        if self.ledger is not None:
                            self.ledger.mark_exhausted(f"{kind} 403 quota")
                        raise QuotaStop("하루 할당량(10,000단위) 소진 — 태평양 자정(한국 오후 4~5시) 뒤 다시 (캐시는 남음)", "daily")
                    if e.code in (403, 404) and kind in ("commentThreads", "comments"):   # 댓글 막힌 영상·지워진 댓글
                        self.used += COST[kind]          # Google 은 오류 답도 센다 (v2.2: 장부와 맞춤)
                        self.calls[kind] += 1
                        ok = True
                        return {"items": [], "_error": e.code, "_reason": body[:120]}
                    if attempt == 2 or e.code < 500:
                        raise RuntimeError(f"HTTP {e.code} {kind}: {body}")
                except urllib.error.URLError as e:
                    if attempt == 2:
                        raise RuntimeError(f"{kind}: {e}")
                time.sleep(2 ** attempt)
        finally:
            if not ok and self.ledger is not None:   # 받지 못한 요청은 장부에서 돌려줌
                self.ledger.refund(COST[kind], self.what or kind, self.topic)

    def search(self, q, published_after, duration=None):
        p = dict(part="snippet", q=q, type="video", order="viewCount", publishedAfter=published_after, regionCode="KR",
                 relevanceLanguage="ko", maxResults=50)
        if duration:                                     # None = 길이 상관없이 (search_supply)
            p["videoDuration"] = duration
        d = self.get("search", **p)
        self.last_total = (d.get("pageInfo") or {}).get("totalResults")
        return [it["id"]["videoId"] for it in d.get("items", []) if it.get("id", {}).get("videoId")]

    def videos(self, ids):
        return self.get("videos", part="snippet,contentDetails,statistics,liveStreamingDetails", id=",".join(ids)).get("items", [])   # 같은 1단위

    def channels(self, ids):
        out = {}
        for it in self.get("channels", part="snippet,statistics", id=",".join(ids)).get("items", []):   # 같은 1단위 (v2.1: 개설일·영상 수도)
            st, sn = it.get("statistics", {}), it.get("snippet", {})
            out[it["id"]] = None if st.get("hiddenSubscriberCount") else int(st.get("subscriberCount", 0))
            self.channel_meta[it["id"]] = {"title": sn.get("title"), "created": sn.get("publishedAt"),
                                           "videos": int(st.get("videoCount", 0) or 0), "views": int(st.get("viewCount", 0) or 0)}
        return out


def iso_seconds(iso):
    m = re.fullmatch(r"P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", iso or "")
    if not m:
        return 0
    d, h, mi, se = (int(x or 0) for x in m.groups())
    return d * 86400 + h * 3600 + mi * 60 + se


_CAPTION = {"last": 0.0}


def caption_block_path():
    return ROOT / ".yt_work" / "caption_block.json"


def caption_blocked(now=None):
    """자막 요청을 쉬는 중이면 끝나는 시각(UTC), 아니면 None (v1.9 — 분석기 v2.9.0·웹 화면과 같은 파일)."""
    try:
        until = datetime.fromisoformat(json.loads(caption_block_path().read_text("utf-8")).get("until") or "")
    except (OSError, ValueError, TypeError):
        return None
    return until if until > (now or datetime.now(timezone.utc)) else None


def note_caption_result(blocked, why="", now=None):
    """자막 요청 결과 기록: 막힘이 CAPTION_BLOCK_AFTER 번 이어지면 CAPTION_COOLDOWN_H 시간 쉼. 막히지 않으면 이어진 횟수를 0 으로."""
    p = caption_block_path()
    try:
        d = json.loads(p.read_text("utf-8"))
    except (OSError, ValueError):
        d = {}
    now = now or datetime.now(timezone.utc)
    if blocked:
        d["streak"] = int(d.get("streak") or 0) + 1
        d["last_error"] = str(why)[:160]
        d["last_at"] = now.isoformat(timespec="seconds")
        if d["streak"] >= CAPTION_BLOCK_AFTER and not caption_blocked(now):
            d["until"] = (now + timedelta(hours=CAPTION_COOLDOWN_H)).isoformat(timespec="seconds")
            d["blocks"] = int(d.get("blocks") or 0) + 1
            log("TRANSCRIPT", logging.WARNING, note=f"YouTube 자막 서버가 연속 {d['streak']}번 막음(429) → {CAPTION_COOLDOWN_H}시간 동안 자막 요청을 쉼 "
                "(대본은 음성인식으로)", until=d["until"], error=str(why)[:100])
    elif d.get("streak"):
        d["streak"] = 0
    else:
        return
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(d, ensure_ascii=False, indent=1), "utf-8")


def is_caption_block(status):
    """YouTube 자막 서버가 거부했나 (IpBlocked·RequestBlocked·429). 소리는 받히므로 음성인식 대기열로 보냄 (v1.9)."""
    return any(w in str(status) for w in CAPTION_BLOCK_ERRORS)


def transcript(vid):
    """→ (조각 목록 [{text,start,duration}], 언어, 상태). 한국어 자막 → 자동 생성 한국어.
    v1.9: 자막 요청을 쉬는 중이면 요청하지 않음, 요청 사이 1.5~3초 쉼, 막힘·성공을 기록 (연속 2번 막히면 6시간 쉼)."""
    until = caption_blocked()
    if until:
        return [], "-", f"IpBlocked: 자막 서버 차단으로 {until.astimezone().strftime('%m-%d %H:%M')}까지 자막 요청을 쉼 → 음성인식"
    import random
    wait = _CAPTION["last"] + random.uniform(*CAPTION_PACE_SEC) - time.time()
    if wait > 0:
        time.sleep(wait)
    try:
        return _transcript_fetch(vid)
    finally:
        _CAPTION["last"] = time.time()


def _transcript_fetch(vid):
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
        api = YouTubeTranscriptApi()
        tl = api.list(vid)
        tr = None
        for finder in (tl.find_manually_created_transcript, tl.find_generated_transcript):
            try:
                tr = finder(["ko"])
                break
            except Exception:
                continue
        if tr is None:
            note_caption_result(False)
            return [], "-", "한국어 자막 없음"
        snips = [{"text": s.text, "start": s.start, "duration": s.duration} for s in tr.fetch()]
        note_caption_result(False)
        return snips, tr.language_code + ("(자동)" if tr.is_generated else ""), "ok"
    except Exception as e:
        st = f"{type(e).__name__}: {str(e)[:120]}"
        if is_caption_block(st):
            note_caption_result(True, st)
        elif not is_network_failure(st):
            note_caption_result(False)          # 자막 꺼짐·없음 등 = 서버는 답함
        return [], "-", st


def is_network_failure(status):
    """자막 실패가 연결 실패 때문인가 (다른 곳·다른 날 다시 하면 받을 수 있음) — '한국어 자막 없음'은 아님.
    v1.9: YouTube 자막 서버 차단(IpBlocked 등)은 여기 아님 → is_caption_block (음성인식으로)."""
    return any(w in str(status) for w in NETWORK_ERRORS)


def speech_stats(snips):
    """자막으로 말 속도(한글 음절/초 — 말하는 구간 기준), 도입부(첫 20초), 첫 1분 발췌, 구간별 흐름(90초마다 첫 문장 앞부분)."""
    if not snips:
        return {}
    syl = sum(len(HANGUL.findall(s["text"])) for s in snips)
    span = max(1e-6, snips[-1]["start"] + snips[-1]["duration"] - snips[0]["start"])
    hook = " ".join(s["text"] for s in snips if s["start"] < 20).replace("\n", " ")
    first60 = " ".join(s["text"] for s in snips if s["start"] < 60).replace("\n", " ")
    outline, next_t = [], 0.0
    for s in snips:
        if s["start"] >= next_t:
            outline.append({"t": int(s["start"]), "text": short(s["text"], 45)})
            next_t = (int(s["start"]) // OUTLINE_EVERY_SEC + 1) * OUTLINE_EVERY_SEC
    return {"syl": syl, "syl_per_sec": round(syl / span, 2), "hook20": hook[:300], "first60": first60[:400],
            "first60_syl": len(HANGUL.findall(first60)), "outline": outline[:20]}


def relevant(info, rel):
    """주제 관련 영상인가 — 분석기 topic_relevance 와 같은 규칙 (RELEVANCE_EXCLUDE 를 지운 뒤 ① 제목·태그에 강한 관련어
    ② 설명(앞 1500자)에 강한 관련어 2번 이상 ③ 제목에 약한 관련어 + (설명에 강한 관련어 또는 제목에 약한 관련어 2개)). 관련어가 없으면 True."""
    strong, weak, excl = rel.get("strong") or [], rel.get("weak") or [], rel.get("exclude") or []
    if not strong:
        return True

    def clean(x):
        x = str(x or "")
        for e in excl:
            x = x.replace(e, " ")
        return x.lower()
    tg = info.get("tags") or []
    title, tags = clean(info.get("title")), clean(tg if isinstance(tg, str) else " ".join(map(str, tg)))
    desc = clean((info.get("description") or "")[:1500])
    sl, wl = [t.lower() for t in strong], [t.lower() for t in weak]
    if any(t in title or t in tags for t in sl):
        return True
    d_strong = sum(desc.count(t) for t in sl)
    t_weak = sum(title.count(t) for t in wl)
    return d_strong >= 2 or (t_weak >= 1 and (d_strong >= 1 or t_weak >= 2))


def _now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _comment_rec(sn, cid, parent, channel_id, replies=0):
    """댓글 한 개 → 기록 (작성자 이름은 저장하지 않음. creator = 그 영상 채널 주인이 쓴 댓글)."""
    return {"id": cid, "parent": parent, "likes": int(sn.get("likeCount", 0) or 0),
            "text": (sn.get("textDisplay") or sn.get("textOriginal") or "").replace("\r", " "),
            "published": (sn.get("publishedAt") or "")[:19], "replies": int(replies or 0),
            "creator": bool(channel_id) and (sn.get("authorChannelId") or {}).get("value") == channel_id}


def _append_jsonl(path, recs):
    if recs:
        with open(path, "a", encoding="utf-8") as f:
            for r in recs:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")


def read_comments_jsonl(path):
    """comments.jsonl → 댓글 목록 (같은 댓글이 두 번 들어 있으면 하나로 — 쪽을 저장하다 멈췄을 때)."""
    out = {}
    if path.is_file():
        with open(path, encoding="utf-8") as f:
            for ln in f:
                ln = ln.strip()
                if ln:
                    try:
                        r = json.loads(ln)
                    except ValueError:
                        continue
                    out[r["id"]] = r
    return list(out.values())


def fetch_all_comments(api, d, vid, channel_id, cap, with_replies, refresh, full=True):
    """1단계(v1.5): 인기 댓글 100개(관련성 순 1쪽, 1단위) — full=False 면 여기까지.
    v2.2: full=True 면 시간순 첫 쪽을 먼저 — 그 한 쪽으로 다 받으면 인기 댓글 쪽(같은 댓글)은 건너뜀 (1단위 아낌, top_skipped).
    2단계 = 댓글 전부: 최상위 댓글(commentThreads, 시간순, 100개씩) + 답글(답글이 5개 넘는 댓글은 comments.list, 100개씩) — 쪽마다 1단위.
    쪽마다 comments.jsonl 에 덧붙이고 comments_state.json 에 다음 쪽을 저장 → 할당량이 끝나면 멈추고, 다음 실행이 그 쪽부터 이어 받는다.
    cap > 0 이면 최상위 댓글 cap 개쯤에서 멈춤 (나중에 cap 을 늘리거나 0 으로 하면 이어서). → (댓글 목록, 상태)."""
    jl, sp = d / "comments.jsonl", d / "comments_state.json"
    st = None
    if sp.is_file() and not refresh:
        try:
            st = json.loads(sp.read_text("utf-8"))
        except ValueError:
            st = None
    if not st or st.get("v") != 1:
        st = {"v": 1, "video": vid, "order": "time", "threads_next": None, "threads_done": False, "threads_end": None,
              "threads": 0, "reply_queue": [], "reply_next": {}, "replies": 0, "units": 0, "disabled": False,
              "restarts": 0, "complete": False, "started": _now(), "finished": None, "quota_stop": None, "error": None}
        jl.write_text("", "utf-8")
    if st["threads_done"] and st.get("threads_end") == "cap" and (cap == 0 or st["threads"] < cap):
        st["threads_done"] = False          # 예전에 개수 제한으로 멈춤 → 이번엔 더 받음
    st["quota_stop"], st["error"] = None, None

    def save():
        sp.write_text(json.dumps(st, ensure_ascii=False), "utf-8")
    def time_page():
        """시간순 최상위 댓글 한 쪽 (100개, 1단위). 댓글이 막혔으면 False."""
        params = dict(part="snippet,replies", videoId=vid, order="time", maxResults=100, textFormat="plainText")
        if st["threads_next"]:
            params["pageToken"] = st["threads_next"]
        data = api.get("commentThreads", **params)
        st["units"] += 1
        if data.get("_error"):
            st.update(threads_done=True, threads_end=f"http_{data['_error']}", disabled=data["_error"] == 403)
            save()
            return False
        recs = []
        for it in data.get("items", []):
            sn, top = it["snippet"], it["snippet"]["topLevelComment"]
            total = int(sn.get("totalReplyCount", 0) or 0)
            recs.append(_comment_rec(top["snippet"], top["id"], None, channel_id, total))
            inc = (it.get("replies") or {}).get("comments", [])
            if total > len(inc):
                st["reply_queue"].append(top["id"])       # 답글이 5개 넘음 → 나중에 comments.list 로 전부
            else:
                recs += [_comment_rec(r["snippet"], r["id"], top["id"], channel_id) for r in inc]
                st["replies"] += len(inc)
        _append_jsonl(jl, recs)
        st["threads"] += len(data.get("items", []))
        st["threads_next"] = data.get("nextPageToken")
        if not st["threads_next"]:
            st.update(threads_done=True, threads_end="end")
        elif cap and st["threads"] >= cap:
            st.update(threads_done=True, threads_end="cap")
        save()
        return True
    try:
        # v2.2: 댓글 전부를 받을 때(full)는 시간순 첫 쪽부터 — 그 한 쪽으로 끝나면(최상위 댓글 100개 이하 — 작은 채널 영상 대부분)
        # 인기 댓글 쪽은 같은 댓글을 다시 받는 것이라 건너뜀 (영상마다 1단위 아낌). 더 있으면 예전처럼 인기 댓글 쪽을 먼저 받아 둠
        # (할당량이 중간에 끝나도 분석에 쓸 인기 댓글이 있게).
        if full and not st.get("top_done") and not st["threads"] and not st["threads_done"] and not st["threads_next"]:
            time_page()
            if st["threads_done"]:
                st.update(top_done=True, top_skipped=True)
                save()
        if not st.get("top_done"):          # 1단계: 인기 댓글 100개 — 분석에 먼저 쓰는 것
            data = api.get("commentThreads", part="snippet,replies", videoId=vid, order="relevance",
                           maxResults=min(100, cap) if cap else 100, textFormat="plainText")
            st["units"] += 1
            if data.get("_error"):
                st.update(threads_done=True, threads_end=f"http_{data['_error']}", disabled=data["_error"] == 403)
            else:
                recs = []
                for it in data.get("items", []):
                    sn, top = it["snippet"], it["snippet"]["topLevelComment"]
                    recs.append(_comment_rec(top["snippet"], top["id"], None, channel_id, sn.get("totalReplyCount", 0)))
                    recs += [_comment_rec(r["snippet"], r["id"], top["id"], channel_id) for r in (it.get("replies") or {}).get("comments", [])]
                _append_jsonl(jl, recs)
            st["top_done"] = True
            save()
        while full and not st["threads_done"]:
            if not time_page():
                break
        while full and with_replies and st["reply_queue"]:
            tid = st["reply_queue"][0]
            params = dict(part="snippet", parentId=tid, maxResults=100, textFormat="plainText")
            if st["reply_next"].get(tid):
                params["pageToken"] = st["reply_next"][tid]
            data = api.get("comments", **params)
            st["units"] += 1
            recs = [_comment_rec(r["snippet"], r["id"], tid, channel_id) for r in data.get("items", [])]
            _append_jsonl(jl, recs)
            st["replies"] += len(recs)
            nxt = None if data.get("_error") else data.get("nextPageToken")
            if nxt:
                st["reply_next"][tid] = nxt
            else:
                st["reply_next"].pop(tid, None)
                st["reply_queue"].pop(0)
            save()
    except QuotaStop as e:
        st["quota_stop"] = e.kind
    except RuntimeError as e:          # HTTP 오류 (쪽 표시가 낡았을 수 있음 → 한 번은 처음부터, 같은 댓글은 하나로 합쳐짐)
        st["error"] = str(e)[:200]
        if "HTTP 400" in str(e) and st["restarts"] < 1:
            st.update(threads_next=None, threads_done=False, restarts=st["restarts"] + 1)
    st["complete"] = bool(st.get("top_done") and st["threads_done"] and (not with_replies or not st["reply_queue"]) and not st["error"])
    if st["complete"] and not st["finished"]:
        st["finished"] = _now()
    save()
    return read_comments_jsonl(jl), st


def write_comments_csv(path, cms):
    """comments.csv: 받은 댓글 전부 (최상위·답글), 좋아요 순."""
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=["id", "parent", "is_reply", "likes", "replies", "creator", "published", "text"])
        w.writeheader()
        for c in sorted(cms, key=lambda c: -int(c.get("likes") or 0)):
            w.writerow({"id": c.get("id"), "parent": c.get("parent") or "", "is_reply": bool(c.get("parent")),
                        "likes": c.get("likes"), "replies": c.get("replies"), "creator": c.get("creator"),
                        "published": c.get("published"), "text": c.get("text")})


def search_cache_file(cache_dir, q, dur, fallback_days):
    """검색 캐시 파일 경로 (검색어·길이·기간이 같으면 같은 파일)."""
    key = hashlib.sha1(f"{q}|{dur}|{fallback_days}|viewCount|KR|ko".encode("utf-8")).hexdigest()[:16]
    return cache_dir / f"search_{key}.json"


def _useful_novel(cache_dir, d, window_days, now=None):
    """캐시 d 가 지난번 새로 고침에서 새로 데려온 영상(d['novel']) 중 쓸 만한 것의 수 (v2.2) — 롱폼·라이브 아님·한국어·지금 기간 안.
    영상 정보 캐시가 없으면 쓸 만한 것으로 셈 (모르면 늦추지 않는 쪽)."""
    now = now or datetime.now(timezone.utc)
    n = 0
    for v in d.get("novel") or []:
        f = Path(cache_dir) / f"{v}.json"
        try:
            i = json.loads(f.read_text("utf-8"))
        except (OSError, ValueError):
            n += 1
            continue
        try:
            age = (now - datetime.fromisoformat(str(i.get("published")).replace("Z", "+00:00"))).days
        except ValueError:
            age = 0
        if (i.get("duration") or 0) >= MIN_LONGFORM_SEC and not exclusion_reason(i) and age <= window_days:
            n += 1
    return n


def search_ttl(cache_dir, d, base_h, window_days, now=None):
    """적응형 검색 캐시 시간 (v2.2 — 사용자 지시 "유튜브 분석 코드를 최대한 api 사용량 덜쓰는 방법(단어 줄이는 방법 말고) 찾아서 수정해보고"):
    검색 1번 = 100단위라 할당량의 거의 전부. 새로 고쳐도 새 영상이 거의 안 나오는 검색(결과가 안정 · 다른 검색어와 겹침)은 덜 자주.
    지난 새로 고침에서 '새로 보인 쓸 만한 영상'이 SEARCH_NOVEL_LOW 이하 → 한 단계 늦춤 (7일 → 14일 → 21일), 많으면 7일로 돌아감.
    상한 = max(기본, min(21일, 탐색 기간 × 1/4)). 새로 고친 기록이 없는 캐시(처음·예전 형식)는 기본.
    → (시간, 단계, 쓸 만한 새 영상 수|None)"""
    if "novel" not in d:
        return base_h, 0, None
    useful = _useful_novel(cache_dir, d, window_days, now)
    level = min(int(d.get("ttl_level") or 0) + 1, SEARCH_MAX_LEVEL) if useful <= SEARCH_NOVEL_LOW else 0
    cap = max(base_h, min(SEARCH_TTL_MAX_H, window_days * 24 * SEARCH_TTL_WINDOW_FRAC))
    return min(base_h * (1 + level), cap), level, useful


def _search_age_h(d, now=None):
    return ((now or datetime.now(timezone.utc)) - datetime.fromisoformat(d["fetched"])).total_seconds() / 3600


def search_is_cached(cache_dir, q, dur, fallback_days, ttl_h=SEARCH_TTL_HOURS):
    """이 검색을 지금 하면 캐시(할당량 0)인가 — 웹 화면의 예상 할당량 계산용 (v1.9, v2.2: 적응형 캐시 시간)."""
    f = search_cache_file(cache_dir, q, dur, fallback_days)
    try:
        d = json.loads(f.read_text("utf-8"))
        return _search_age_h(d) <= search_ttl(cache_dir, d, ttl_h, fallback_days)[0]
    except (OSError, ValueError, KeyError):
        return False


def _search_pool(cache_dir, skip):
    """다른 검색 캐시들이 이미 찾은 영상 ID (v2.2 — '새로 보인 영상'에서 뺌: 다른 검색어로 이미 찾은 영상은 이 검색이 새로 데려온 것이 아님)."""
    pool = set()
    for f in Path(cache_dir).glob("search_*.json"):
        if f.name == skip:
            continue
        try:
            pool.update(json.loads(f.read_text("utf-8")).get("ids") or [])
        except (OSError, ValueError):
            pass
    return pool


def cached_search(api, cache_dir, q, since, dur, fallback_days, ttl_h, refresh, info=None):
    """검색 캐시: (검색어, 길이, 기간) 이 같고 적응형 캐시 시간(search_ttl) 안이면 할당량 0. → (영상 ID 목록, 캐시 여부).
    할당량이 없으면 QuotaStop. info(dict) 를 주면 ttl_h·level·useful·age_h 를 채움 (로그용).
    새로 고칠 때 지난 결과와 비교해 '새로 보인 영상'(novel)·늦춤 단계(ttl_level)를 같이 저장 (v2.2)."""
    f = search_cache_file(cache_dir, q, dur, fallback_days)
    old = None
    if f.is_file():
        try:
            old = json.loads(f.read_text("utf-8"))
            old["fetched"], old["ids"]                                   # 형식 확인
        except (OSError, ValueError, KeyError, TypeError):
            old = None
    level = 0
    if old:
        eff, level, useful = search_ttl(cache_dir, old, ttl_h, fallback_days)
        age_h = _search_age_h(old)
        if info is not None:
            info.update(ttl_h=round(eff), level=level, useful=useful, age_h=round(age_h, 1))
        if age_h <= eff and not refresh:
            return old["ids"], True
    ids = api.search(q, since, dur)
    rec = {"q": q, "dur": dur, "fallback_days": fallback_days, "fetched": datetime.now(timezone.utc).isoformat(),
           "since": since, "total": getattr(api, "last_total", None), "ids": ids}
    if old:                                     # v2.2: 이번 새로 고침이 새로 데려온 영상 (지난 결과에도, 다른 검색에도 없던 것)
        prev, pool = set(old["ids"]), _search_pool(cache_dir, f.name)
        rec.update(novel=[v for v in ids if v not in prev and v not in pool], ttl_level=level, prev_fetched=old["fetched"],
                   refreshes=int(old.get("refreshes") or 0) + 1)
        if info is not None:
            info.update(novel=len(rec["novel"]))
    f.write_text(json.dumps(rec, ensure_ascii=False), "utf-8")
    return ids, False


def _fresh(path, ttl_h, refresh=False):
    """캐시 파일이 ttl_h 시간 안에 받은 것인가 (조회수·구독자 수는 바뀌므로 오래된 것은 다시 — 50개에 1단위)."""
    if refresh or not path.is_file():
        return False
    try:
        t = datetime.fromisoformat(json.loads(path.read_text("utf-8")).get("fetched", "2000-01-01T00:00:00+00:00"))
    except (ValueError, AttributeError):
        return False
    return (datetime.now(timezone.utc) - t).total_seconds() / 3600 <= ttl_h


def _info_from_item(it):
    sn, cd, st = it["snippet"], it["contentDetails"], it.get("statistics", {})
    return {"id": it["id"], "title": sn.get("title"), "channel": sn.get("channelTitle"), "channel_id": sn.get("channelId"),
            "published": sn.get("publishedAt"), "description": sn.get("description"), "tags": sn.get("tags"),
            "duration": iso_seconds(cd.get("duration")), "live": sn.get("liveBroadcastContent") != "none",
            "view_count": int(st.get("viewCount", 0)), "like_count": int(st.get("likeCount", 0) or 0),
            "comment_count": int(st.get("commentCount", 0) or 0), "fetched": datetime.now(timezone.utc).isoformat(),
            "was_live": bool(it.get("liveStreamingDetails")),                                   # v2.0: 라이브였던 영상
            "audio_lang": sn.get("defaultAudioLanguage") or "", "lang": sn.get("defaultLanguage") or ""}


def video_ttl_h(published, now=None):
    """영상 정보 캐시 시간 (v2.2): 조회수가 빨리 바뀌는 새 영상은 24시간, 오래된 영상은 길게 (VIDEO_TTL_BY_AGE). 날짜를 모르면 24시간."""
    now = now or datetime.now(timezone.utc)
    try:
        age = (now - datetime.fromisoformat(str(published).replace("Z", "+00:00"))).days
    except ValueError:
        return VIDEO_TTL_HOURS
    for max_age, ttl in VIDEO_TTL_BY_AGE:
        if max_age is None or age <= max_age:
            return ttl
    return VIDEO_TTL_HOURS


def fetch_video_infos(api, cache_dir, ids, state, refresh=False):
    """영상 정보 (캐시 .cache/<id>.json, 24시간). 할당량이 끝나면 있던 캐시로 계속하고 state 에 남김. → [info] (ids 순서, 받은 것만).
    v1.9: collect_api 에서 떼어 냄 — 웹 화면(tools/web_ui.py)이 채널·주소로 더한 영상에도 씀."""
    ids = list(dict.fromkeys(ids))
    now = datetime.now(timezone.utc)
    kept_old = [0]

    def ok(v):          # 캐시가 새것이고 v2.0 정보(라이브였는지·언어)가 있으면 다시 받지 않음
        f = cache_dir / f"{v}.json"
        if refresh or not f.is_file():
            return False
        try:
            i = json.loads(f.read_text("utf-8"))
            fetched = datetime.fromisoformat(i.get("fetched", "2000-01-01T00:00:00+00:00"))
        except (OSError, ValueError, TypeError):
            return False
        if "was_live" not in i:
            return False
        ttl = video_ttl_h(i.get("published"), now)
        fresh = (now - fetched).total_seconds() / 3600 <= ttl
        kept_old[0] += fresh and ttl > VIDEO_TTL_HOURS and (now - fetched).total_seconds() / 3600 > VIDEO_TTL_HOURS
        return fresh
    need = [v for v in ids if not ok(v)]
    missing = sum(1 for v in need if not (cache_dir / f"{v}.json").is_file())
    log("VIDEO", found=len(ids), refresh=len(need), new=missing, ttl_h="24/72/168 (올린 지 30일·180일 기준)",
        kept_old=kept_old[0], units=-(-len(need) // 50))
    for i in range(0, len(need), 50):
        chunk = need[i:i + 50]
        try:
            items = api.videos(chunk)
        except QuotaStop as e:
            state["quota_stop"] = state["quota_stop"] or e.kind
            left = need[i:]
            state["pending_videos"] += sum(1 for v in left if not (cache_dir / f"{v}.json").is_file())   # 없는 것만 '못 함'
            state["stale_videos"] += sum(1 for v in left if (cache_dir / f"{v}.json").is_file())        # 예전 숫자로 계속
            log("VIDEO", logging.WARNING, note="할당량이 끝나 영상 정보 못 받음 — 다음 실행에 이어서 (있던 캐시는 예전 숫자로 씀)",
                pending=state["pending_videos"], stale=state["stale_videos"])
            break
        for it in items:
            (cache_dir / f"{it['id']}.json").write_text(json.dumps(_info_from_item(it), ensure_ascii=False), "utf-8")
    return [json.loads((cache_dir / f"{v}.json").read_text("utf-8")) for v in ids if (cache_dir / f"{v}.json").is_file()]


def fetch_channel_subs(api, cache_dir, channel_ids, state, refresh=False):
    """채널 구독자 수 (캐시 .cache/channels.json, 7일). → {채널ID: {"subs": n|None, "fetched": 시각}} (v1.9: collect_api 에서 떼어 냄)."""
    subs_cache_p = cache_dir / "channels.json"     # {채널ID: {"subs": n|null, "fetched": 시각}}
    subs_cache = json.loads(subs_cache_p.read_text("utf-8")) if subs_cache_p.is_file() and not refresh else {}
    subs_cache = {k: v for k, v in subs_cache.items() if isinstance(v, dict)}       # v1.1 이전 형식(숫자만)은 다시 받음
    now = datetime.now(timezone.utc)

    def ch_fresh(cid):                          # v2.1: 개설일(created)이 없는 예전 캐시는 한 번 다시 받음
        v = subs_cache.get(cid)
        try:
            return bool(v) and "created" in v and (now - datetime.fromisoformat(v["fetched"])).total_seconds() / 3600 <= CHANNEL_TTL_HOURS
        except (ValueError, KeyError, TypeError):
            return False
    ch_need = sorted(c for c in channel_ids if c and not ch_fresh(c))
    for i in range(0, len(ch_need), 50):
        try:
            got = api.channels(ch_need[i:i + 50])
        except QuotaStop as e:
            state["quota_stop"] = state["quota_stop"] or e.kind
            state["pending_channels"] += sum(1 for c in ch_need[i:] if c not in subs_cache)
            log("VIDEO", logging.WARNING, note="할당량이 끝나 채널 구독자 수 못 받음 — 다음 실행에 이어서",
                pending=state["pending_channels"])
            break
        stamp = datetime.now(timezone.utc).isoformat()
        for cid, n in got.items():                 # v2.1: 개설일·영상 수 + 받을 때마다 구독자 수 기록 (날짜별, 최근 60번)
            hist = dict((subs_cache.get(cid) or {}).get("history") or {})
            if n is not None:
                hist[stamp[:10]] = n
            subs_cache[cid] = {"subs": n, "fetched": stamp, **(getattr(api, "channel_meta", {}).get(cid) or {}),
                               "history": dict(sorted(hist.items())[-60:])}
    subs_cache_p.write_text(json.dumps(subs_cache, ensure_ascii=False), "utf-8")
    return subs_cache


VIDEO_ID_RX = re.compile(r"(?:v=|youtu\.be/|/shorts/|/live/|/embed/)([0-9A-Za-z_-]{11})")
CHANNEL_ID_RX = re.compile(r"(UC[0-9A-Za-z_-]{22})")


def parse_target(text):
    """사용자가 넣은 주소·이름 → ("video", 영상ID) / ("channel", "UC…") / ("handle", "@이름") / (None, 까닭).
    영상: watch?v=… · youtu.be/… · shorts/… · 영상 ID 11자. 채널: /channel/UC… · UC… · /@이름 · @이름 (v1.9 — 웹 화면)."""
    t = str(text or "").strip()
    if not t:
        return None, "빈 칸"
    m = VIDEO_ID_RX.search(t)
    if m:
        return "video", m.group(1)
    m = CHANNEL_ID_RX.search(t)
    if m:
        return "channel", m.group(1)
    m = re.search(r"(?:youtube\.com/)?(@[^/?#\s]+)", t)
    if m:
        return "handle", urllib.parse.unquote(m.group(1))
    if re.fullmatch(r"[0-9A-Za-z_-]{11}", t):
        return "video", t
    return None, "영상 주소(watch?v=…, youtu.be/…)나 채널 주소(/channel/UC…, /@이름)가 아님"


AUTOCOMPLETE_URL = "https://suggestqueries.google.com/complete/search"
AUTOCOMPLETE_TTL_HOURS = 168
SUPPLY_TTL_HOURS = 168


def parse_autocomplete(text):
    """자동완성 응답 (client=firefox 순수 JSON, client=youtube JSONP) → [제안] (분석기 parse_autocomplete 와 같음)."""
    try:
        data = json.loads(text)
    except ValueError:
        m = re.search(r"\((\[.*\])\)\s*;?\s*$", text, re.S)
        if not m:
            return []
        data = json.loads(m.group(1))
    if not isinstance(data, list) or len(data) < 2 or not isinstance(data[1], list):
        return []
    out = [(x[0] if isinstance(x, list) and x else x) for x in data[1]]
    return [x.strip() for x in out if isinstance(x, str) and x.strip()]


def fetch_autocomplete(q, cache_dir, refresh=False, fetch=None):
    """YouTube 검색어 자동완성 (할당량 0) — 사람들이 이 말로 무엇을 찾는지 (수요). 캐시 .cache/autocomplete.json 7일.
    → (제안 목록 — 앞일수록 많이 찾음, 캐시 여부). fetch(url)→text 는 시험용."""
    p = Path(cache_dir) / "autocomplete.json"
    try:
        d = json.loads(p.read_text("utf-8")) if p.is_file() else {}
    except (OSError, ValueError):
        d = {}
    hit = d.get(q)
    if hit and not refresh:
        try:
            if (datetime.now(timezone.utc) - datetime.fromisoformat(hit["fetched"])).total_seconds() / 3600 <= AUTOCOMPLETE_TTL_HOURS:
                return hit["s"], True
        except (KeyError, ValueError):
            pass
    url = AUTOCOMPLETE_URL + "?" + urllib.parse.urlencode({"client": "firefox", "ds": "yt", "hl": "ko", "gl": "kr", "q": q})
    if fetch:
        text = fetch(url)
    else:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=10) as r:
            raw = r.read()
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            text = raw.decode("cp949", errors="replace")
    sugg = parse_autocomplete(text)
    d[q] = {"s": sugg, "fetched": datetime.now(timezone.utc).isoformat()}
    tmp = p.with_name(p.name + f".{os.getpid()}.tmp")
    tmp.write_text(json.dumps(d, ensure_ascii=False), "utf-8")
    os.replace(tmp, p)
    return sugg, False


def supply_cache_file(cache_dir, phrase, days):
    return Path(cache_dir) / f"supply_{hashlib.sha1(f'{phrase}|{days}'.encode('utf-8')).hexdigest()[:16]}.json"


def search_supply(api, cache_dir, phrase, days, state, refresh=False):
    """말 하나의 공급 확인 (v2.1): 최근 days 일·길이 상관없이 조회수 순 검색 1번(100단위) → 결과 수(totalResults 추정)·상위 50개 영상
    정보·채널 구독자. 캐시 .cache/supply_<해시>.json 7일. → {"phrase","days","total","ids","fetched","cached"}"""
    f = supply_cache_file(cache_dir, phrase, days)
    if f.is_file() and not refresh:
        try:
            d = json.loads(f.read_text("utf-8"))
            if (datetime.now(timezone.utc) - datetime.fromisoformat(d["fetched"])).total_seconds() / 3600 <= SUPPLY_TTL_HOURS:
                return {**d, "cached": True}
        except (ValueError, KeyError):
            pass
    since = (datetime.now(timezone.utc) - timedelta(days=days)).strftime("%Y-%m-%dT00:00:00Z")
    ids = api.search(phrase, since, None)
    d = {"phrase": phrase, "days": days, "since": since, "total": api.last_total, "ids": ids,
         "fetched": datetime.now(timezone.utc).isoformat()}
    f.write_text(json.dumps(d, ensure_ascii=False), "utf-8")
    infos = fetch_video_infos(api, Path(cache_dir), ids, state)
    fetch_channel_subs(api, Path(cache_dir), {i["channel_id"] for i in infos}, state)
    return {**d, "cached": False}


def resolve_channel(api, kind, value):
    """채널 ID 또는 @이름 → {"id","title","handle","uploads","subs","videos"} (channels.list 1단위). 없으면 None."""
    params = {"part": "snippet,contentDetails,statistics"}
    if kind == "handle":
        params["forHandle"] = value
    else:
        params["id"] = value
    items = api.get("channels", **params).get("items", [])
    if not items:
        return None
    it = items[0]
    st = it.get("statistics", {})
    return {"id": it["id"], "title": it["snippet"].get("title"), "handle": it["snippet"].get("customUrl") or (value if kind == "handle" else ""),
            "uploads": (it.get("contentDetails", {}).get("relatedPlaylists") or {}).get("uploads") or ("UU" + it["id"][2:]),
            "subs": None if st.get("hiddenSubscriberCount") else int(st.get("subscriberCount", 0)), "videos": int(st.get("videoCount", 0) or 0)}


def channel_uploads(api, cache_dir, ch, ttl_h=24, refresh=False, max_videos=0):
    """채널에 올라온 영상 전부 (업로드 목록 playlistItems.list — 50개에 1단위, 최근 것부터). 캐시 .cache/uploads_<채널ID>.json (ttl_h).
    max_videos > 0 이면 최근 그만큼만. → [영상ID] (v1.9 — 웹 화면: 채널을 더하면 그 채널 영상을 모두 탐색)"""
    p = cache_dir / f"uploads_{ch['id']}.json"
    if _fresh(p, ttl_h, refresh):
        ids = json.loads(p.read_text("utf-8"))["ids"]
        return ids[:max_videos] if max_videos else ids
    old = []                                  # v2.2: 예전 목록이 있으면 새 영상만 — 아는 영상이 나오면 멈춤 (채널 영상 500개면 10단위 → 1단위)
    if p.is_file() and not refresh:
        try:
            prev = json.loads(p.read_text("utf-8"))
            old = list(prev.get("ids") or []) if prev.get("complete") else []    # 예전 형식(complete 없음)은 잘린 목록일 수 있어 한 번 끝까지
        except (OSError, ValueError):
            old = []
    known = set(old)
    ids, token, pages, hit_known = [], None, 0, False
    while True:
        params = {"part": "contentDetails", "playlistId": ch["uploads"], "maxResults": 50}
        if token:
            params["pageToken"] = token
        d = api.get("playlistItems", **params)
        pages += 1
        page = [it["contentDetails"]["videoId"] for it in d.get("items", []) if it.get("contentDetails", {}).get("videoId")]
        new = [v for v in page if v not in known]
        ids += new
        token = d.get("nextPageToken")
        if len(new) < len(page):               # 아는 영상까지 왔음 → 나머지는 예전 목록 그대로
            hit_known = True
            break
        if not token or (max_videos and len(ids) >= max_videos):
            break
    merged = list(dict.fromkeys(ids + (old if hit_known else [])))
    complete = hit_known or not token          # 끝까지(또는 아는 영상까지) 받았나 — max_videos 로 멈춘 목록은 다음에 이어 붙이지 않음
    p.write_text(json.dumps({"channel": ch["id"], "fetched": datetime.now(timezone.utc).isoformat(), "ids": merged, "complete": complete},
                            ensure_ascii=False), "utf-8")
    log("CHANNEL", channel=ch.get("title"), id=ch["id"], videos=len(merged), new=len(ids), pages=pages, incremental=hit_known,
        quota_used=api.used)
    return merged[:max_videos] if max_videos else merged


def collect_api(topic, a, api, kws, exclude, out, state):
    """검색(최근·조회수 순) → 영상·채널 정보 → 후보 행 목록. 캐시: out/.cache/. 할당량이 끝나면 캐시만으로 계속하고 state 에 남김."""
    cache_dir = out / ".cache"
    since = (datetime.now(timezone.utc) - timedelta(days=a.fallback_days)).strftime("%Y-%m-%dT00:00:00Z")
    found = {}
    for g, q in kws:
        for dur in (("medium", "long") if a.long else ("medium",)):
            ttl = {}
            try:
                ids, hit = cached_search(api, cache_dir, q, since, dur, a.fallback_days, a.search_ttl_hours, a.refresh, info=ttl)
            except QuotaStop as e:
                state["quota_stop"] = state["quota_stop"] or e.kind
                state["pending_searches"].append(f"{q} ({dur})")
                state["search_log"].append({"q": q, "source": g, "dur": dur, "results": None, "status": "남음"})
                continue
            state["searched" if not hit else "search_cached"] += 1
            state["search_log"].append({"q": q, "source": g, "dur": dur, "results": len(ids), "status": "캐시" if hit else "새로"})
            for vid in ids:
                found.setdefault(vid, []).append(f"태그:{q}" if g == "태그" else q)
            log("SEARCH", query=q, group=g, dur=dur, results=len(ids), cached=hit, quota_used=api.used,
                **{k: v for k, v in ttl.items() if v is not None})          # v2.2: 적응형 캐시 시간·단계·새로 보인 영상
    if state["pending_searches"]:
        log("SEARCH", logging.WARNING, topic=topic, note="할당량이 끝나 못 한 검색 — status.json pending, 다음 실행에 이어서",
            pending=len(state["pending_searches"]), stop=state["quota_stop"])
    infos = fetch_video_infos(api, cache_dir, list(found), state, a.refresh)
    subs_cache = fetch_channel_subs(api, cache_dir, {i["channel_id"] for i in infos}, state, a.refresh)
    rows = []
    for i in infos:
        if any(w in (i["title"] or "") for w in exclude):
            continue
        i["subs"] = (subs_cache.get(i["channel_id"]) or {}).get("subs")
        rows.append(i)
    return rows, found


def collect_existing(topic):
    """분석기 결과(videos.csv)를 같은 모양으로. 설명은 없고, 댓글은 audience_comments.csv 에 있는 영상만."""
    import pandas as pd
    v = pd.read_csv(ROOT / topic / "result" / "data" / "videos.csv")
    rows = []
    for _, r in v.iterrows():
        rows.append({"id": r["video_id"], "title": r["title"], "channel": r["channel_title"], "channel_id": r["channel_id"],
                     "published": str(r["published_at"]), "description": "", "tags": r.get("tags"),
                     "duration": int(r["duration_sec"] or 0) if r["duration_sec"] == r["duration_sec"] else 0, "live": False,
                     "view_count": int(r["views"]), "like_count": int(r["likes"]) if r["likes"] == r["likes"] else 0,
                     "comment_count": int(r["comments"]) if r["comments"] == r["comments"] else 0,
                     "subs": int(r["subscribers"]) if r["subscribers"] == r["subscribers"] else None})
    c = pd.read_csv(ROOT / topic / "result" / "data" / "audience_comments.csv")
    cm = {vid: [{"likes": int(x.likes or 0), "text": str(x.comment), "replies": int(x.replies or 0), "published": str(x.published_at)[:10]}
                for x in g.itertuples()] for vid, g in c.groupby("video_id")}
    return rows, cm


def deep_case(d, r, info, a, api, source, existing_comments, state):
    """사례 하나: 설명·자막·썸네일·댓글 전부. 이미 받은 것은 다시 받지 않음(--refresh 면 다시). → (meta, comments)."""
    d.mkdir(parents=True, exist_ok=True)
    (d / "description.txt").write_text(info.get("description") or "", "utf-8")
    # 자막 (할당량 0 — 댓글보다 먼저)
    tj = d / "transcript.json"
    if tj.is_file() and not a.refresh:
        saved = json.loads(tj.read_text("utf-8"))
        snips, lang, st = saved["snippets"], saved["lang"], "ok"
        state["transcripts_reused"] += 1
    elif a.no_transcript:
        snips, lang, st = [], "-", "건너뜀(--no-transcript)"
    elif a.offline:                                   # 다시 만들기만: 예전 상태 그대로 (자막 요청 안 함)
        try:
            prev = json.loads((d / "metadata.json").read_text("utf-8")).get("transcript_status")
        except (OSError, ValueError):
            prev = None
        snips, lang, st = [], "-", prev or "확인 안 함(--offline)"
    else:
        snips, lang, st = transcript(r["id"])
        if snips:
            tj.write_text(json.dumps({"lang": lang, "snippets": snips}, ensure_ascii=False), "utf-8")
            (d / "transcript.txt").write_text("\n".join(f"[{x['start']:7.1f}] {x['text']}" for x in snips), "utf-8")
    if not snips:
        state["transcript_missing"].append({"id": r["id"], "status": st, "retry_elsewhere": is_network_failure(st)})
    # 썸네일
    th = d / "thumbnail.jpg"
    if a.offline and not (th.is_file() and th.stat().st_size > 0):
        state["thumbnail_missing"].append(r["id"])
    elif not (th.is_file() and th.stat().st_size > 0) or a.refresh:
        try:
            req = urllib.request.Request(f"https://i.ytimg.com/vi/{r['id']}/hqdefault.jpg", headers={"User-Agent": "Mozilla/5.0"})
            th.write_bytes(urllib.request.urlopen(req, timeout=20).read())
        except Exception as e:
            state["thumbnail_missing"].append(r["id"])
            log("DEEP", logging.WARNING, id=r["id"], step="thumbnail", error=str(e)[:100])
    # 댓글 1단계: 인기 댓글 100개 (전부는 run_topic 이 모든 사례의 1단계가 끝난 뒤 2단계로)
    cms, cst = comments_step(d, r, a, api, source, existing_comments, state, full=False)
    stats = speech_stats(snips)
    n_rep = sum(1 for c in cms if c.get("parent"))
    meta = {**r, "source": source, "tags": info.get("tags"), "chapters": chapters_from(info.get("description") or ""),
            "transcript_lang": lang, "transcript_status": st, **stats,
            "comments_fetched": len(cms), "comments_top_level": len(cms) - n_rep, "comments_replies": n_rep,
            "comments_by_creator": sum(1 for c in cms if c.get("creator")), "comments_complete": cst["complete"],
            "comments_disabled": cst.get("disabled", False), "comments_reported": r.get("comments"),
            "tool": f"outlier_research.py {VERSION}", "collected": datetime.now().isoformat(timespec="seconds")}
    (d / "metadata.json").write_text(json.dumps(meta, ensure_ascii=False, indent=1), "utf-8")
    return meta, cms


def comments_step(d, r, a, api, source, existing_comments, state, full):
    """댓글 받기 한 단계 (full=False: 인기 댓글 100개 / True: 전부) → comments.csv 다시 쓰고 (댓글, 상태). 할당량이 끝나면 다음 실행이 이어서."""
    if source == "existing":
        cms = existing_comments.get(r["id"], [])
        cst = {"complete": True, "top_done": True, "threads": len(cms), "replies": 0, "units": 0, "disabled": False}
    else:
        used0 = api.used
        cms, cst = fetch_all_comments(api, d, r["id"], r.get("channel_id"), a.comments, a.replies, a.refresh and not full, full=full)
        state["comment_units"] += api.used - used0
        if cst.get("quota_stop"):
            state["quota_stop"] = state["quota_stop"] or cst["quota_stop"]
        if cst.get("error"):
            log("DEEP", logging.WARNING, id=r["id"], step="comments", error=cst["error"][:150], next_step="다음 실행에 다시")
        if not full and not cst.get("top_done"):
            state["top_missing"].append(r["id"])
        if full and not cst["complete"]:
            state["pending_comments"].append(r["id"])
        elif full and api.used == used0:
            state["comments_reused"] += 1
    write_comments_csv(d / "comments.csv", cms)
    return cms, cst


def new_state():
    return {"quota_stop": None, "searched": 0, "search_cached": 0, "pending_searches": [], "pending_videos": 0,
            "pending_channels": 0, "pending_comments": [], "stale_videos": 0, "transcript_missing": [], "thumbnail_missing": [],
            "transcripts_reused": 0, "comments_reused": 0, "comments_total": 0, "comment_units": 0, "top_missing": [],
            "search_log": [], "tag_keywords": []}


def write_status(out, topic, a, api, state, rows, q, deep, pop_deep, kw_file):
    """이어서 돌리기용 상태 (tools/pc_analysis.py 가 읽음). complete = 할당량 때문에 못 한 일이 없음."""
    pending = bool(state["pending_searches"] or state["pending_videos"] or state["pending_channels"] or state["pending_comments"])
    n_cases = len(deep) + len(pop_deep)
    st = {"tool": f"outlier_research.py {VERSION}", "updated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
          "topic": topic, "keywords_file": str(kw_file.relative_to(ROOT)) if kw_file.is_relative_to(ROOT) else kw_file.name,
          "per_group": a.per_group, "top": a.top, "popular_top": a.popular, "comments_cap": a.comments, "replies": a.replies,
          "quota_used": api.used if api else 0, "quota_stop": state["quota_stop"],
          "searches_new": state["searched"], "searches_cached": state["search_cached"],
          "pending": {"searches": state["pending_searches"], "videos": state["pending_videos"], "channels": state["pending_channels"],
                      "comments": state["pending_comments"]}, "stale_videos": state["stale_videos"],
          "candidates": len(rows), "qualified": len(q), "deep": len(deep), "popular": len(pop_deep),
          "comments_total": state["comments_total"], "comment_units": state["comment_units"],
          "comments_complete": n_cases - len(state["pending_comments"]), "cases": n_cases,
          "transcripts_ok": n_cases - len(state["transcript_missing"]), "transcript_missing": state["transcript_missing"],
          "thumbnails_ok": n_cases - len(state["thumbnail_missing"]), "thumbnail_missing": state["thumbnail_missing"],
          "ready": not (state["pending_searches"] or state["pending_videos"] or state["pending_channels"] or state["top_missing"]),
          "top_comments_missing": state["top_missing"],
          "complete": not pending,
          "next": ("완료" if not pending else "할당량이 초기화된 뒤(태평양 자정 = 한국 오후 4시·겨울 5시) 같은 명령을 다시 — 받은 것은 캐시, 남은 것만 새로")}
    (out / "status.json").write_text(json.dumps(st, ensure_ascii=False, indent=1), "utf-8")
    log("STATUS", topic=topic, ready=st["ready"], complete=st["complete"], quota_stop=state["quota_stop"] or "-", pending_searches=len(state["pending_searches"]),
        pending_videos=state["pending_videos"], pending_comments=len(state["pending_comments"]),
        comments=f"{state['comments_total']}개·사례 {st['comments_complete']}/{n_cases} 끝", comment_units=state["comment_units"],
        transcripts=f"{st['transcripts_ok']}/{n_cases}", thumbnails=f"{st['thumbnails_ok']}/{n_cases}")
    return st


CASE_DIR = re.compile(r"^P?\d\d_(.+)$")


def case_folder(out, old_dir, name, vid):
    """사례 폴더 out/<name>. 같은 영상의 예전 폴더(다른 순위·다른 묶음·_old/)가 있으면 이름만 바꿔 받은 자막·댓글을 재사용."""
    d = out / name
    if d.exists():
        return d
    for base in (out, old_dir):
        if not base.is_dir():
            continue
        for p in base.iterdir():
            m = CASE_DIR.match(p.name)
            if p.is_dir() and m and m.group(1) == vid:
                p.rename(d)
                return d
    return d


def _write_rows(path, rows, fields, extra):
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=fields + list(extra))
        w.writeheader()
        for k, r in enumerate(rows, 1):
            w.writerow({**r, **{key: fn(k, r) for key, fn in extra.items()}})


LIVE_TITLE_RX = re.compile(r"라이브|생방송|스트리밍|실시간\s*방송|\blive\b", re.I)


def exclusion_reason(info):
    """탐색에서 뺄 영상인가 → '라이브 방송' / '외국 영상' / None (v2.0 — 사용자 지시 "라이브 방송, 외국 영상은 탐색 대상에서 제외")."""
    if info.get("live") or info.get("was_live") or LIVE_TITLE_RX.search(str(info.get("title") or "")):
        return "라이브 방송"
    lang = str(info.get("audio_lang") or info.get("lang") or "").lower()
    if lang and not lang.startswith("ko") and lang not in ("zxx", "und", "mul"):
        return "외국 영상"
    if not lang and not HANGUL.search(str(info.get("title") or "")):
        return "외국 영상"
    return None


def build_rows(infos, found, now, keep=()):
    """영상 정보 → 후보 행 (길이 없음·라이브 방송·외국 영상 제외 — keep 에 든 영상은 라이브·외국이어도 남기고 'flag' 로 표시).
    배수 = 조회수 ÷ 구독자(100 미만은 100)."""
    rows = []
    for i in infos:
        if not i.get("duration"):
            continue
        why = exclusion_reason(i)
        if why and i["id"] not in keep:
            continue
        try:
            pub = datetime.fromisoformat(str(i["published"]).replace("Z", "+00:00"))
            pub = pub if pub.tzinfo else pub.replace(tzinfo=timezone.utc)
            age = (now - pub).days
        except Exception:
            age = None
        subs, views = i.get("subs"), i.get("view_count") or 0
        ratio = round(views / max(subs, 100), 2) if subs else None
        rows.append({"id": i["id"], "title": i["title"], "channel": i["channel"], "channel_id": i["channel_id"], "subs": subs,
                     "views": views, "ratio": ratio, "age_days": age, "views_per_day": round(views / max(age or 1, 1), 1),
                     "minutes": round(i["duration"] / 60, 1), "likes": i.get("like_count"), "comments": i.get("comment_count"),
                     "published": str(i["published"])[:10], "queries": " | ".join(dict.fromkeys(found.get(i["id"], []))),
                     "url": f"https://www.youtube.com/watch?v={i['id']}", "flag": why or ""})
    return rows


def _norm(t):
    return re.sub(r"\s+", "", str(t)).lower()


def pick_tag_keywords(rows, info_by_id, kws, rel, n, out, min_ratio):
    """태그 검색어 n개: 잘된 영상(배수 ≥ min_ratio 또는 조회수 상위 50, 주제 관련)의 태그 중 검색어에 없고 채널 2곳 이상이 쓴 것,
    관련어가 들었거나 5번 이상 나온 것. 한 번 고르면 tag_keywords.json 에 고정 (모자라면 다음 실행에 채움)."""
    p = out / "tag_keywords.json"
    try:
        saved = json.loads(p.read_text("utf-8"))
    except (OSError, ValueError):
        saved = {}
    kw_norm = {_norm(k) for _, k in kws}
    chosen = [t for t in (saved.get("chosen") or []) if _norm(t) not in kw_norm]     # 검색어 목록에 들어간 태그는 빼고 (v1.7)
    if len(chosen) >= n:
        return chosen[:n]
    have = kw_norm | {_norm(t) for t in chosen}
    rel_rows = [r for r in rows if relevant(info_by_id[r["id"]], rel)]
    good = {r["id"] for r in rel_rows if (r["ratio"] or 0) >= min_ratio}
    good |= {r["id"] for r in sorted(rel_rows, key=lambda r: -r["views"])[:50]}
    cnt, chans = {}, {}
    for vid in good:
        for t in {str(x).strip().lstrip("#") for x in (info_by_id[vid].get("tags") or [])}:
            if 2 <= len(t) <= 20:
                cnt[t] = cnt.get(t, 0) + 1
                chans.setdefault(t, set()).add(info_by_id[vid].get("channel_id"))
    terms = [x.lower() for x in (rel.get("strong") or []) + (rel.get("weak") or [])]
    cands = [t for t, c in sorted(cnt.items(), key=lambda x: (-x[1], x[0]))
             if _norm(t) not in have and len(chans[t]) >= 2 and (any(x in t.lower() for x in terms) or c >= 5)]
    chosen += cands[: n - len(chosen)]
    if chosen:
        p.write_text(json.dumps({"chosen": chosen, "counts": {t: cnt.get(t) for t in chosen}, "from_videos": len(good),
                                 "updated": _now(), "rule": "잘된 영상의 태그 · 검색어에 없음 · 채널 2곳 이상 · 관련어 포함 또는 5번 이상"},
                                ensure_ascii=False, indent=1), "utf-8")
    return chosen


def run_topic(topic, a, api):
    t0 = time.time()
    out = ROOT / topic / "result" / "outliers"
    (out / ".cache").mkdir(parents=True, exist_ok=True)
    kws, exclude, topic_name, kw_file, rel = load_keywords(topic, a.per_group)
    source = "existing" if a.from_existing else "api"
    if source == "api" and not kws:                  # v1.8: 검색어가 없으면 '다 끝남'으로 착각하지 않게 멈춤
        log("START", logging.ERROR, topic=topic, note="검색어가 없음 — 검색할 것이 없어 멈춤",
            next_step=f"{topic}/{KEYWORD_LIST_FILE} 에 검색어를 한 줄에 하나씩 적으세요 (GitHub 에서 고치면 PC 가 다음 회차에 받음)")
        raise SystemExit(1)
    state = new_state()
    log("START", topic=topic, name=topic_name, source=source, keywords=len(kws), keywords_file=kw_file.name, per_group=a.per_group,
        days=a.days, max_subs=a.max_subs, min_ratio=a.min_ratio, min_views=a.min_views, min_sec=a.min_sec, quota=a.quota,
        top=a.top, popular=a.popular, comments="전부" if not a.comments else a.comments, replies=a.replies,
        relevance_terms=len(rel["strong"]), tool=f"outlier_research.py {VERSION}")
    now = datetime.now(timezone.utc)
    existing_comments = {}
    if a.from_existing:
        infos, existing_comments = collect_existing(topic)
        found = {}
    else:
        infos, found = collect_api(topic, a, api, kws, exclude, out, state)
    if source == "api" and a.tag_keywords > 0:                   # 태그 검색어 (v1.6): 잘된 영상들이 쓴 태그로 한 번 더 탐색
        tags = pick_tag_keywords(build_rows(infos, found, now), {i["id"]: i for i in infos}, kws, rel, a.tag_keywords, out, a.min_ratio)
        state["tag_keywords"] = tags
        if tags:
            log("SEARCH", topic=topic, note="태그 검색어로 더 탐색", tags=",".join(tags))
            tinfos, tfound = collect_api(topic, a, api, [("태그", t) for t in tags], exclude, out, state)
            seen = {i["id"] for i in infos}
            infos += [i for i in tinfos if i["id"] not in seen]
            for vid, qs in tfound.items():
                found.setdefault(vid, []).extend(qs)
    info_by_id = {i["id"]: i for i in infos}
    rows = build_rows(infos, found, now)
    if a.offline and not rows:                      # v2.0.1: 다시 만들 자료가 없으면 있던 결과를 지우지 않음
        log("DONE", logging.WARNING, topic=topic, note="--offline: 검색 캐시가 없어 다시 만들 후보가 0 — 요약·표·사례 폴더를 그대로 둠",
            hint="결과를 새로 만들려면 할당량이 있을 때 --offline 없이 (또는 웹 화면에서 탐색)")
        try:
            return json.loads((out / "status.json").read_text("utf-8"))
        except (OSError, ValueError):
            return {"complete": True, "skipped": "offline-no-data"}
    fields = list(rows[0].keys()) if rows else ["id"]
    _write_rows(out / "candidates.csv", sorted(rows, key=lambda r: -(r["ratio"] or 0)), fields, {})

    def qualify(days):
        qq = [r for r in rows if r["subs"] and r["subs"] <= a.max_subs and r["ratio"] and r["ratio"] >= a.min_ratio
              and r["views"] >= a.min_views and r["age_days"] is not None and r["age_days"] <= days and r["minutes"] * 60 >= a.min_sec]
        return sorted(qq, key=lambda r: -r["ratio"])
    used_days, q = a.days, qualify(a.days)
    for wider in (a.fallback_days, 730):
        if len(q) >= a.top or used_days >= wider:
            continue
        used_days, q = wider, qualify(wider)
        log("FILTER", logging.WARNING, topic=topic, note=f"최근 사례가 {a.top}개보다 적어 {wider}일로 넓힘", qualified=len(q))

    def cap_channels(cands, n):
        per_ch, top = {}, []
        for r in cands:
            if per_ch.get(r["channel_id"], 0) >= a.per_channel:
                continue
            per_ch[r["channel_id"]] = per_ch.get(r["channel_id"], 0) + 1
            top.append(r)
        return top[:n]
    top = cap_channels(q, a.top)
    log("FILTER", topic=topic, candidates=len(rows), qualified=len(q), days=used_days, chosen=len(top),
        ratios=",".join(str(r["ratio"]) for r in top))
    _write_rows(out / "outliers.csv", q, fields, {"rank": lambda k, r: k})
    # 조회수 상위 (구독자 수 상관없음): 주제 관련·롱폼·최근 fallback_days 일 → 조회수 순
    pool = [r for r in rows if r["minutes"] * 60 >= a.min_sec and r["age_days"] is not None and r["age_days"] <= a.fallback_days
            and relevant(info_by_id[r["id"]], rel)]
    pool.sort(key=lambda r: -r["views"])
    pop = cap_channels(pool, a.popular) if a.popular > 0 else []
    top_ids = {r["id"]: k for k, r in enumerate(top, 1)}
    _write_rows(out / "popular.csv", pool, fields, {"rank": lambda k, r: k, "success_rank": lambda k, r: top_ids.get(r["id"], "")})
    log("FILTER", topic=topic, popular_pool=len(pool), off_topic=sum(1 for r in rows if not relevant(info_by_id[r["id"]], rel)),
        popular=len(pop), overlap=sum(1 for r in pop if r["id"] in top_ids), views=",".join(str(r["views"]) for r in pop[:10]))
    old_dir = out / "_old"       # 이번에 빠진 사례 폴더 (다시 들어오면 받은 자막·댓글 재사용)
    deep, pop_deep, keep = [], [], set()
    jobs = [("", k, r) for k, r in enumerate(top, 1)] + [("P", k, r) for k, r in enumerate(pop, 1) if r["id"] not in top_ids]
    for prefix, k, r in jobs:
        name = f"{prefix}{k:02d}_{r['id']}"
        keep.add(name)
        d = case_folder(out, old_dir, name, r["id"])
        meta, cms = deep_case(d, {**r, "rank": f"{prefix}{k}" if prefix else k, "set": "popular" if prefix else "success", "folder": name},
                              info_by_id[r["id"]], a, api, source, existing_comments, state)
        (pop_deep if prefix else deep).append((meta, info_by_id[r["id"]], cms))
        log("DEEP", topic=topic, set="popular" if prefix else "success", rank=meta["rank"], id=r["id"], subs=r["subs"], views=r["views"],
            ratio=r["ratio"], age=r["age_days"], minutes=r["minutes"],
            transcript=meta["transcript_status"] if meta["transcript_status"] != "ok" else meta["transcript_lang"],
            top_comments=len(cms), quota_used=api.used if api else 0)
    # 댓글 2단계: 모든 사례의 인기 댓글을 받은 뒤 사례마다 전부 (성공 사례 먼저) — 남은 할당량으로, 못 받은 것은 다음 실행이 이어서
    for lst in (deep, pop_deep):
        for i, (meta, info, _) in enumerate(lst):
            d = out / meta["folder"]
            cms, cst = comments_step(d, meta, a, api, source, existing_comments, state, full=True)
            n_rep = sum(1 for c in cms if c.get("parent"))
            meta.update(comments_fetched=len(cms), comments_top_level=len(cms) - n_rep, comments_replies=n_rep,
                        comments_by_creator=sum(1 for c in cms if c.get("creator")), comments_complete=cst["complete"],
                        comments_disabled=cst.get("disabled", False))
            (d / "metadata.json").write_text(json.dumps(meta, ensure_ascii=False, indent=1), "utf-8")
            state["comments_total"] += len(cms)
            lst[i] = (meta, info, cms)
    log("DEEP", topic=topic, note="댓글 2단계(전부) 끝", comments=state["comments_total"], pending=len(state["pending_comments"]),
        comment_units=state["comment_units"], quota_used=api.used if api else 0)
    for meta, info, cms in deep:      # 성공 사례이면서 조회수 상위인 영상 → 조회수 상위 목록에도 표시
        meta["popular_rank"] = next((f"P{k}" for k, r in enumerate(pop, 1) if r["id"] == meta["id"]), None)
    moved = 0
    for p in out.iterdir():
        if p.is_dir() and CASE_DIR.match(p.name) and p.name not in keep:
            old_dir.mkdir(exist_ok=True)
            dst = old_dir / p.name
            if dst.exists():
                shutil.rmtree(dst)
            p.rename(dst)
            moved += 1
    if moved:
        log("DEEP", topic=topic, note="이번 목록에서 빠진 사례 폴더를 _old/ 로 옮김", moved=moved)
    write_summary(out, topic, topic_name, a, used_days, rows, q, deep, pop, pop_deep, source)
    st = write_status(out, topic, a, api, state, rows, q, deep, pop_deep, kw_file)
    write_downloads(out, topic, topic_name, a, rows, q, deep, pop_deep, state)
    log("DONE", topic=topic, source=source, candidates=len(rows), qualified=len(q), deep=len(deep), popular=len(pop_deep),
        comments=state["comments_total"], complete=st["complete"], quota_used=api.used if api else 0,
        minutes=round((time.time() - t0) / 60, 1), out=str(out.relative_to(ROOT)))
    return st


def _folder_tag(folder):
    return re.sub(r"[^0-9A-Za-z가-힣]+", "_", str(folder)).strip("_") or "topic"


def analyzer_out_dir(topic):
    """분석기 결과 폴더 (설정의 OUTPUT_DIR/PROJECT_FOLDER/RESULT_FOLDER, 기본 output/<주제>/result)."""
    try:
        cfg = _flat(tomllib.loads((ROOT / topic / "analyzer_config.toml").read_text("utf-8")))
    except Exception:
        cfg = {}
    base = Path(str(cfg.get("OUTPUT_DIR") or "output")).expanduser()
    base = base if base.is_absolute() else ROOT / base
    return base / str(cfg.get("PROJECT_FOLDER") or topic) / str(cfg.get("RESULT_FOLDER") or "result")


def _transcript_cell(meta, whisper):
    st, lang = str(meta.get("transcript_status") or ""), str(meta.get("transcript_lang") or "")
    if st == "ok":
        return "✅ 음성인식" if "음성인식" in lang else f"✅ 자막({lang})"
    if st.startswith("건너뜀"):
        return "– 건너뜀"
    if st.startswith("확인 안 함"):
        return "… 아직 확인 안 함 (다음 실행)"
    if is_network_failure(st):
        return "🔁 연결 안 됨 — 다음 회차에 다시"
    w = whisper.get(meta.get("id")) or {}
    if is_caption_block(st) and not (w.get("attempts", 0) >= 3 and not w.get("done")):
        return "⏳ 음성인식 대기" + (f" (시도 {w['attempts']}번)" if w.get("attempts") else "") + " — 자막 서버가 막음(429)"
    if w.get("attempts", 0) >= 3 and not w.get("done"):
        return f"❌ 음성인식 실패 ({short(w.get('error'), 40)})"
    return "⏳ 음성인식 대기" + (f" (시도 {w['attempts']}번)" if w.get("attempts") else "") + f" — {short(st, 20) or '자막 없음'}"


def _upload_cell(published, now=None):
    """업로드 날짜 칸: 'YYYY-MM-DD (N일 전)' (v1.7 — 사용자 지시 "탐색 목록에 업로드 날짜도 같이 표시해"). 모르면 '–'."""
    p = str(published or "")[:10]
    try:
        d = datetime.strptime(p, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    except ValueError:
        return "–"
    return f"{p} ({max(((now or datetime.now(timezone.utc)) - d).days, 0)}일 전)"


def _comment_cell(meta):
    got, rep_ = meta.get("comments_fetched") or 0, meta.get("comments_reported")
    total = f"{got:,}/{rep_:,}" if isinstance(rep_, int) else f"{got:,}"
    if meta.get("comments_disabled"):
        return "🚫 댓글 막힌 영상"
    return f"✅ {total}" if meta.get("comments_complete") else f"⏳ {total} 받는 중"


def write_downloads(out, topic, name, a, rows, q, deep, pop_deep, state):
    """downloads.md (GitHub 에서 바로 보이는 표) + downloads.csv — 탐색한 검색어와, 자료로 받은 영상마다 무엇을 받았는지."""
    try:
        whisper = json.loads((ROOT / ".yt_work" / f"whisper_{_folder_tag(topic)}.json").read_text("utf-8"))
    except (OSError, ValueError):
        whisper = {}
    cases = []
    for set_name, lst in (("성공 사례", deep), ("조회수 상위", pop_deep)):
        for meta, info, cms in lst:
            d = out / str(meta.get("folder") or "")
            cases.append({"set": set_name, "rank": meta.get("rank"), "id": meta.get("id"), "title": meta.get("title"),
                          "channel": meta.get("channel"), "subs": meta.get("subs"), "views": meta.get("views"), "ratio": meta.get("ratio"),
                          "published": str(meta.get("published") or "")[:10], "upload": _upload_cell(meta.get("published")),
                          "transcript": _transcript_cell(meta, whisper), "comments": _comment_cell(meta),
                          "thumbnail": "✅" if (d / "thumbnail.jpg").is_file() else "❌",
                          "description": "✅" if (info.get("description") or "").strip() else "–",
                          "tags": len(info.get("tags") or []), "chapters": len(meta.get("chapters") or []),
                          "folder": meta.get("folder"), "url": meta.get("url")})
    an = []
    sc = analyzer_out_dir(topic) / "success_cases"
    if sc.is_dir():
        for d in sorted(sc.iterdir()):
            try:
                m = json.loads((d / "metadata.json").read_text("utf-8"))
            except (OSError, ValueError):
                continue
            ds = m.get("download_status") or {}
            t = str(ds.get("transcript") or "-")
            an.append({"title": m.get("title"), "url": m.get("video_url"), "views": m.get("views"), "subs": m.get("subscribers"),
                       "upload": _upload_cell(m.get("published_at")),
                       "transcript": {"whisper_pending": "⏳ 음성인식 대기", "failed": "❌ 실패", "whisper": "✅ 음성인식"}.get(
                           t, f"✅ 자막({t})" if t != "-" else "–"),
                       "comments": f"✅ {ds['comments']} (분석기 표본)" if ds.get("comments") else "–",
                       "thumbnail": "✅" if ds.get("thumbnail") == "ok" else "❌",
                       "video": "– 받지 않음" if str(ds.get("video", "")).startswith("skipped") else str(ds.get("video") or "–"),
                       "folder": d.name})
    num = lambda v: f"{v:,}" if isinstance(v, (int, float)) and v == v else "–"
    ok_tr = sum(1 for c in cases if c["transcript"].startswith("✅"))
    wait_tr = sum(1 for c in cases if c["transcript"].startswith("⏳"))
    ok_cm = sum(1 for c in cases if c["comments"].startswith("✅"))
    sl = state["search_log"]
    L = [f"# {name} — 받은 자료 표", "",
         f"자동 생성 — `tools/outlier_research.py` {VERSION} ({datetime.now().strftime('%Y-%m-%d %H:%M')}). "
         "사례 폴더(설명·자막·댓글 전부·썸네일)도 GitHub 에 함께 올라갑니다 (공개 저장소에도 — 2026-10-14 사용자 지시). 진행 상태: `status.json`.", "",
         "## 한눈에", "",
         "| 항목 | 수 |", "|---|---|",
         f"| 탐색한 검색어 | {len({x['q'] for x in sl})}개 (검색어 목록 `keywords.toml` {len({x['q'] for x in sl if x['source'] != '태그'})} · 잘된 영상 태그 {len({x['q'] for x in sl if x['source'] == '태그'})}) — 검색 {len(sl)}번 (새로 {sum(1 for x in sl if x['status'] == '새로')} · 캐시 {sum(1 for x in sl if x['status'] == '캐시')} · 남음 {sum(1 for x in sl if x['status'] == '남음')}) |",
         f"| 찾은 후보 영상 (롱폼) | {len(rows):,} |",
         f"| 성공 사례 기준 통과 | {len(q):,} |",
         f"| 자료로 받은 영상 | {len(cases)} (성공 사례 {len(deep)} · 조회수 상위 {len(pop_deep)}) + 분석기 성공사례 {len(an)} |",
         f"| 자막 | ✅ {ok_tr} · ⏳ 음성인식 대기 {wait_tr} · 그 밖 {len(cases) - ok_tr - wait_tr} |",
         f"| 댓글 다 받음 | {ok_cm} / {len(cases)} (전부 {state['comments_total']:,}개) |",
         f"| 썸네일 | {sum(1 for c in cases if c['thumbnail'] == '✅')} / {len(cases)} |", "",
         "표시: ✅ 받음 · ⏳ 진행 중(다음 실행·음성인식 대기열이 이어서 — 자막 서버가 막은 영상도 음성인식으로) · 🔁 연결 안 됨(다음 회차에 다시) · ❌ 실패 · – 해당 없음", "",
         "## 자료로 받은 영상", "",
         "| 묶음 | # | 제목 | 채널 | 구독자 | 조회수 | 업로드 | 자막 | 댓글 (받음/영상 표시) | 썸네일 | 설명 | 태그 | 챕터 | 폴더 |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for c in cases:
        L.append(f"| {c['set']} | {c['rank']} | [{short(c['title'], 50)}]({c['url']}) | {short(c['channel'], 16)} | {num(c['subs'])} | "
                 f"{num(c['views'])} | {c['upload']} | {c['transcript']} | {c['comments']} | {c['thumbnail']} | {c['description']} | {c['tags']} | "
                 f"{c['chapters']} | `{c['folder']}` |")
    if an:
        L += ["", "## 분석기 성공사례 (`output/…/success_cases` — 영상 파일은 받지 않음)", "",
              "| 제목 | 구독자 | 조회수 | 업로드 | 자막 | 댓글 | 썸네일 | 영상 | 폴더 |", "|---|---|---|---|---|---|---|---|---|"]
        for c in an:
            L.append(f"| [{short(c['title'], 50)}]({c['url']}) | {num(c['subs'])} | {num(c['views'])} | {c['upload']} | {c['transcript']} | {c['comments']} | "
                     f"{c['thumbnail']} | {c['video']} | `{c['folder']}` |")
    L += ["", "## 탐색한 검색어", "", "검색어 목록은 실제 영상 태그에서 고른 것 (`tools/tag_keywords.py` → `keywords.toml`, 고른 표: `tag_candidates.md`). "
          "출처 = keywords.toml 의 묶음 이름", "", "| 검색어 | 출처 | 길이 | 결과 | 상태 |", "|---|---|---|---|---|"]
    for x in sl:
        L.append(f"| {x['q']} | {'잘된 영상 태그 (tag_keywords.json)' if x['source'] == '태그' else x['source']} | {'4~20분' if x['dur'] == 'medium' else '20분 넘음'} | "
                 f"{x['results'] if x['results'] is not None else '–'} | {x['status']} |")
    if state.get("tag_keywords"):
        L += ["", f"태그 검색어 고른 규칙·횟수: `tag_keywords.json` — {', '.join(state['tag_keywords'])}"]
    (out / "downloads.md").write_text("\n".join(L) + "\n", "utf-8")
    with open(out / "downloads.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=["set", "rank", "id", "title", "channel", "subs", "views", "ratio", "published", "transcript",
                                          "comments", "thumbnail", "description", "tags", "chapters", "folder", "url"], extrasaction="ignore")
        w.writeheader()
        w.writerows(cases)
    log("STATUS", topic=topic, note="받은 자료 표", file="downloads.md", cases=len(cases), analyzer_cases=len(an),
        transcripts_ok=ok_tr, whisper_wait=wait_tr, comments_done=ok_cm)


def chapters_from(desc):
    """설명란의 '0:00 제목' 줄 → 챕터 목록 (YouTube 챕터 규칙과 같은 모양)."""
    out = []
    for ln in desc.splitlines():
        m = re.match(r"\s*\(?((?:\d+:)?\d{1,2}:\d{2})\)?\s*[-–—|:]?\s*(.+)", ln)
        if m:
            parts = [int(x) for x in m.group(1).split(":")]
            sec = parts[-1] + 60 * parts[-2] + (3600 * parts[0] if len(parts) == 3 else 0)
            out.append({"start": sec, "title": m.group(2).strip()})
    return out if len(out) >= 3 and out[0]["start"] == 0 else []


def short(s, n):
    s = re.sub(r"\s+", " ", str(s or "")).strip()
    return s if len(s) <= n else s[: n - 1] + "…"


def _case_lines(meta, info, cms):
    L = [f"## {meta['rank']}. {short(meta['title'], 90)}", "",
         f"- {meta['url']} · {meta['channel']} · 구독자 {meta['subs']:,} · 조회수 {meta['views']:,} (×{meta['ratio']}) · "
         f"{meta['published']} ({meta['age_days']}일 전) · {meta['minutes']}분" + (f" · 검색어: {meta['queries']}" if meta['queries'] else "")
         if meta.get("subs") is not None else
         f"- {meta['url']} · {meta['channel']} · 구독자 비공개 · 조회수 {meta['views']:,} · {meta['published']} ({meta['age_days']}일 전) · "
         f"{meta['minutes']}분" + (f" · 검색어: {meta['queries']}" if meta['queries'] else ""),
         f"- 설명 앞부분: {short(info.get('description'), 300) or '(이 자료에는 설명 없음)'}"]
    if meta.get("chapters"):
        L.append("- 챕터: " + " / ".join(f"{int(c['start'] // 60)}:{int(c['start'] % 60):02d} {short(c['title'], 30)}"
                                       for c in meta["chapters"][:15]))
    if meta.get("hook20"):
        L.append(f"- 도입부(첫 20초, 자막 {meta['transcript_lang']}): {short(meta['hook20'], 220)}")
        L.append(f"- 첫 1분 발췌: {short(meta.get('first60'), 300)}")
        L.append(f"- 말 속도 {meta['syl_per_sec']}음절/초 · 첫 1분 {meta['first60_syl']}음절 · 전체 {meta.get('syl', 0):,}음절")
        if meta.get("outline"):
            L.append(f"- 구간별 흐름({OUTLINE_EVERY_SEC}초마다 첫 문장 앞부분): "
                     + " / ".join(f"{o['t'] // 60}:{o['t'] % 60:02d} {o['text']}" for o in meta["outline"]))
    else:
        L.append(f"- 자막: {meta['transcript_status']}")
    done = "다 받음" if meta.get("comments_complete") else "받는 중 — 다음 실행이 이어서"
    if meta.get("comments_disabled"):
        done = "댓글 막힌 영상"
    L.append(f"- 댓글 {meta.get('comments_fetched', 0):,}개 받음 (최상위 {meta.get('comments_top_level', 0):,} · 답글 {meta.get('comments_replies', 0):,} · "
             f"채널 주인 {meta.get('comments_by_creator', 0):,}) / 영상 표시 {meta.get('comments_reported') or 0:,}개 — {done}. 전부: 사례 폴더 `comments.csv`")
    top = sorted((c for c in cms if not c.get("parent")), key=lambda c: -int(c.get("likes") or 0))[:10]
    if top:
        L.append("- 인기 댓글 상위 10 (좋아요):")
        L += [f"  - ({c.get('likes')}) {short(c.get('text'), 140)}" for c in top]
    L.append("")
    return L


def write_summary(out, topic, name, a, used_days, rows, q, deep, pop, pop_deep, source):
    L = [f"# {name} — 작은 채널 성공 사례 + 조회수 상위 영상 (최근·롱폼)", "",
         f"자동 생성 — `tools/outlier_research.py` {VERSION} ({datetime.now().strftime('%Y-%m-%d %H:%M')}). "
         "사례마다 자막·댓글 전부(`comments.csv`)·썸네일은 사례 폴더에 있다 (GitHub 에도 올라감). "
         "진행 상태(못 한 검색·댓글·자막·썸네일)는 `status.json`.", "",
         f"- 성공 사례 기준: 최근 {used_days}일 안 · 구독자 {a.max_subs:,}명 이하 · 조회수 ≥ 구독자 × {a.min_ratio} · 조회수 {a.min_views:,} 이상 · "
         f"{a.min_sec // 60}분 이상 (쇼츠 제외) · 채널당 {a.per_channel}개까지",
         f"- 조회수 상위 기준: **구독자 수 상관없음** · 주제 관련(keywords.toml 관련어) · {a.min_sec // 60}분 이상 · 최근 {a.fallback_days}일 · "
         f"조회수 순 {a.popular}개 · 채널당 {a.per_channel}개까지",
         (f"- 후보 {len(rows)}개 — 자료: YouTube Data API 검색(검색어 {'전부' if a.per_group <= 0 else f'그룹마다 {a.per_group}개'}, 최근 {a.fallback_days}일·조회수 순·4~20분"
          + (", 20분 넘음" if a.long else "") + ")" if source == "api" else
          f"- 후보 {len(rows)}개 — 자료: 분석기 결과 `result/data/videos.csv` (⚠️ 분석기 검색은 최근 영상만 찾지 않았다)")
         + f" → 성공 사례 기준 통과 {len(q)}개 → 자세히 {len(deep)}개 · 조회수 상위 {len(pop)}개",
         f"- 댓글: " + ("전부 (최상위 + 답글)" if not a.comments and a.replies else
                       f"최상위 {a.comments or '전부'}개까지" + ("" if a.replies else " · 답글 안 받음")), "",
         "## 성공 사례 (작은 채널)", "",
         "| # | 제목 | 채널 | 구독자 | 조회수 | 배수 | 업로드 | 길이(분) | 말 속도(음절/초) | 댓글 받음 |", "|---|---|---|---|---|---|---|---|---|---|"]
    for meta, info, cms in deep:
        L.append(f"| {meta['rank']} | [{short(meta['title'], 60)}]({meta['url']}) | {short(meta['channel'], 20)} | {meta['subs']:,} | {meta['views']:,} | "
                 f"{meta['ratio']} | {_upload_cell(meta.get('published'))} | {meta['minutes']} | {meta.get('syl_per_sec', '-')} | "
                 f"{meta.get('comments_fetched', 0):,}{'' if meta.get('comments_complete') else ' (받는 중)'} |")
    by_id = {m["id"]: m for m, _, _ in deep + pop_deep}
    L += ["", "## 조회수 상위 (구독자 수 상관없음)", "",
          "| # | 제목 | 채널 | 구독자 | 조회수 | 업로드 | 길이(분) | 댓글 받음 | 성공 사례 |", "|---|---|---|---|---|---|---|---|---|"]
    for k, r in enumerate(pop, 1):
        m = by_id.get(r["id"], {})
        L.append(f"| P{k} | [{short(r['title'], 60)}]({r['url']}) | {short(r['channel'], 20)} | "
                 f"{'{:,}'.format(r['subs']) if r['subs'] is not None else '비공개'} | {r['views']:,} | {_upload_cell(r.get('published'))} | {r['minutes']} | "
                 f"{m.get('comments_fetched', 0):,}{'' if m.get('comments_complete') else ' (받는 중)'} | "
                 f"{m['rank'] if m.get('set') == 'success' else '-'} |")
    L.append("")
    for meta, info, cms in deep:
        L += _case_lines(meta, info, cms)
    for meta, info, cms in pop_deep:
        L += _case_lines(meta, info, cms)
    (out / "summary.md").write_text("\n".join(L), "utf-8")


def _env_file_key(path, name="YOUTUBE_API_KEY"):
    if not path.is_file():
        return ""
    m = re.search(rf"^[ \t]*{name}[ \t]*=[ \t]*['\"]?([^'\"\s]+)", path.read_text("utf-8-sig"), re.M)
    return m.group(1) if m else ""


def load_api_key(topic=None):
    """→ (키, 어디서). 주제별 키가 먼저 (v1.4): <주제폴더>/.env → 환경 변수 YOUTUBE_API_KEY_<폴더> → YOUTUBE_API_KEY → 맨 위 .env.
    값은 출력하지 않는다. ⚠️ 할당량을 늘리려고 같은 도구에 Google Cloud 프로젝트를 여러 개 쓰는 것은 YouTube API 정책 위반('sharding')."""
    if topic:
        k = _env_file_key(ROOT / topic / ".env")
        if k:
            return k, f"{topic}/.env"
        tag = re.sub(r"[^0-9A-Za-z가-힣]+", "_", str(topic)).strip("_").upper()
        k = os.environ.get(f"YOUTUBE_API_KEY_{tag}", "").strip()
        if k:
            return k, f"env:YOUTUBE_API_KEY_{tag}"
    k = os.environ.get("YOUTUBE_API_KEY", "").strip()
    if k:
        return k, "env:YOUTUBE_API_KEY"
    k = _env_file_key(ROOT / ".env")
    return (k, ".env") if k else ("", "-")


def main(argv=None):
    ap = argparse.ArgumentParser(description="작은 채널 성공 사례(최근·롱폼·조회수/구독자 배수) + 조회수 상위 영상 수집 — 자막·댓글 전부, 이어서 돌리기 지원")
    ap.add_argument("topics", nargs="+")
    ap.add_argument("--per-group", type=int, default=0, help="검색어 그룹마다 검색할 수 (0 = 전부, 기본)")
    ap.add_argument("--days", type=int, default=180)
    ap.add_argument("--fallback-days", type=int, default=365)
    ap.add_argument("--max-subs", type=int, default=50000)
    ap.add_argument("--min-ratio", type=float, default=3.0)
    ap.add_argument("--min-views", type=int, default=10000)
    ap.add_argument("--min-sec", type=int, default=240)
    ap.add_argument("--top", type=int, default=15)
    ap.add_argument("--per-channel", type=int, default=2)
    ap.add_argument("--comments", type=int, default=0, help="사례마다 최상위 댓글을 몇 개까지 (0 = 전부)")
    ap.add_argument("--no-replies", dest="replies", action="store_false", help="답글은 받지 않음 (기본: 답글도 전부)")
    ap.add_argument("--popular", type=int, default=20, help="구독자 수 상관없이 조회수 상위 영상 수 (0 = 안 함)")
    ap.add_argument("--no-long", dest="long", action="store_false", help="20분 넘는 영상은 검색하지 않음")
    ap.add_argument("--quota", type=int, default=9000, help="이번 실행 API 단위 한도 (주제 여러 개를 함께 셈. 하루 10,000)")
    ap.add_argument("--search-ttl-hours", type=float, default=SEARCH_TTL_HOURS, help="검색 캐시 유효 시간 (기본 168 = 7일)")
    ap.add_argument("--tag-keywords", type=int, default=0, help="잘된 영상의 태그에서 더 고를 검색어 수 (기본 0 = 내가 적은 검색어만)")
    ap.add_argument("--offline", action="store_true", help="API·자막·썸네일 요청 없이 캐시·받은 파일로 요약·표·상태만 다시 만듦")
    ap.add_argument("--from-existing", action="store_true", help="분석기 결과에서 고르기 (API 키 없이)")
    ap.add_argument("--no-transcript", action="store_true", help="자막 받기 건너뜀")
    ap.add_argument("--refresh", action="store_true", help="캐시·이미 받은 자막·썸네일·댓글을 무시하고 새로")
    ap.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING"])
    a = ap.parse_args(argv)
    logging.basicConfig(level=getattr(logging, a.log_level), format="%(message)s", stream=sys.stdout)
    apis, topic_api = {}, {}            # 키마다 Api 하나 (같은 키를 쓰는 주제끼리만 --quota 를 나눠 씀)
    if a.offline:                       # 요청 없이 다시 만들기만 (키 필요 없음)
        a.search_ttl_hours = float("inf")   # v2.0.1: 오래된 검색 캐시도 씀 (새로 요청할 수 없으므로)
        off = Api("", 0)
        off.stopped = "offline"
        topic_api = {t: off for t in a.topics}
    elif not a.from_existing:
        for t in a.topics:
            key, src = load_api_key(t)
            if not key:
                raise SystemExit(f"[START] ❌ {t}: YOUTUBE_API_KEY 가 없음 → {t}/.env 또는 맨 위 .env 에 YOUTUBE_API_KEY=... (PC), "
                                 "클라우드는 환경 변수 (키 없이 기존 자료로만: --from-existing)")
            fp = hashlib.sha256(key.encode()).hexdigest()[:8]
            apis.setdefault(fp, Api(key, a.quota))
            topic_api[t] = apis[fp]
            log("START", topic=t, key_source=src, key_id=fp,
                shared_with=",".join(x for x in topic_api if x != t and topic_api[x] is apis[fp]) or "-")
    statuses = {}
    for t in a.topics:
        try:
            statuses[t] = run_topic(t, a, topic_api.get(t))
        except SystemExit:
            raise
        except Exception as e:   # 한 주제가 실패해도 다음 주제
            log("DONE", logging.ERROR, topic=t, error=f"{type(e).__name__}: {str(e)[:200]}", hint="잠시 뒤 다시 (캐시는 남음)")
            statuses[t] = {"complete": False, "error": f"{type(e).__name__}: {str(e)[:200]}"}
    return 0 if all(s.get("complete") for s in statuses.values()) else 3   # 3 = 못 한 일이 남음 (할당량·오류) → 다시 돌리면 이어서


if __name__ == "__main__":
    sys.exit(main())
