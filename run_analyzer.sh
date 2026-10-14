#!/usr/bin/env bash
# ================================================================================================
#  YouTube 분석 PC 실행기 (macOS / Linux)
#  VERSION: v3.0 — 2026-10-14 — 실행하면 웹 화면이 뜸 (사용자 지시: "이거 분석기 웹 ui 형식으로 만들어 실행하면 바로 웹 ui가 나와서"):
#           기본 = tools/web_ui.py (http://127.0.0.1:8765/). 예전 자동 실행은 --auto (--once·cron 도 자동 실행).
#           코드 목록에 tools/web_ui.py·tools/weekly_analysis.py 추가
#  (v2.5 — 2026-10-13 — 검색어 목록 <주제>/keywords.txt (한 줄에 하나, 그룹 없음)도 받음 (사용자 지시: "걍 검색어 내가 수정해도
#           돌아가게 하면 안돼?"). GitHub 에서 고친 설정·검색어는 tools/pc_analysis.py v1.7 이 회차마다 받아 씀 (VERSION 안 올려도 됨))
#  (v2.4 — 2026-10-13 — pip 이 없는 가상환경 고침 (사용자 PC 오류: ".venv\Scripts\python.exe: No module named pip"):
#           ① .venv 에 pip 이 없으면 ensurepip 로 설치 (안 되면 분석 코드가 공식 get-pip.py 로 한 번 더)
#           ② .venv 만들기가 실패하면 반쯤 만든 .venv 를 지우고 pip 없이 다시 만들어 분석 코드가 pip 을 설치하게 함)
#  (v2.3 — 2026-10-13 — 검색어를 태그로 바꾼 새 판을 PC 가 자동으로 받게 (사용자 지시: "그냥 검색어를 재테크 관련 태그로 찾아서
#           다 그걸로 탐색해봐"): 설정·검색어 파일(<주제>/analyzer_config.toml·keywords.toml·tag_rules.toml)은 PC 에 있어도
#           GitHub 쪽 파일 머리의 VERSION 이 더 높으면 예전 것을 .bak 으로 두고 새 판으로 바꿈 (같거나 낮으면, VERSION 이 없으면 그대로).
#           코드 목록에 tools/tag_keywords.py (태그에서 검색어 고르기) 추가)
#  (v2.2 — 2026-10-13 — 여러 주제를 동시에: --folder economic --folder health (또는 --folder economic,health)
#           (사용자 지시: "동시에 병렬로 다른 주제 분석도 가능하도록"). 주제마다 설정·검색어 파일을 받고, 주제별 키는 <주제>/.env)
#  (v2.1 — 2026-10-13 — 비공개 저장소에서도 받기: .env(또는 환경 변수)의 GITHUB_TOKEN 이 있으면 GitHub API 로 코드·설정을 받음
#           (사용자 지시: "비공개로 돌릴테니까 전부 다 업로드되게"). 토큰은 curl 설정(표준 입력)으로만 넘겨 명령줄·화면에 남기지 않음.
#           .env 가 없으면 먼저 틀을 만듦)
#  (v2.0 — 2026-10-13 — 기본 주제 economic(경제·재테크). 분석기 + 작은 채널 성공 사례(자막·썸네일·댓글)를
#           tools/pc_analysis.py 로 함께 돌리고, 할당량이 끝나 못 한 부분은 할당량 초기화(한국 오후 4~5시) 뒤 자동으로 이어서.
#           검색어 목록 <폴더>/keywords.toml 도 받음. --once · --analyzer-only(예전 방식) · --print-cron 추가)
#  (v1.0 — 2026-10-09 — 분석 코드·설정 파일을 GitHub에서 wget으로 받아 분석기만 실행)
# ================================================================================================
#  처음 한 번 (새 폴더에서, 자세히: guides/pc_analysis.md — 저장소가 비공개면 그 문서의 토큰으로 받는 방법):
#    wget -O run_analyzer.sh https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/main/run_analyzer.sh
#    bash run_analyzer.sh
#    → 처음 실행하면 .env 파일이 생깁니다. YOUTUBE_API_KEY(필수)·GITHUB_TOKEN(권장)을 넣고 다시 실행
#
#  자주 쓰는 실행:
#    bash run_analyzer.sh                       # ★ 웹 화면 (키·검색어 고치기 → 탐색 → 체크 → 승인 → 주별 분석)
#    bash run_analyzer.sh --auto                # 예전 자동 실행 — 끝날 때까지 (남으면 다음 날 이어서, 터미널을 열어 두기)
#    bash run_analyzer.sh --auto --folder economic,health   # 자동 실행 여러 주제 동시에
#    bash run_analyzer.sh --once                # 자동 실행 한 회차만 (남은 부분은 다음에 실행할 때)
#    bash run_analyzer.sh --print-cron          # 매일 17:15 에 --once 로 돌리는 crontab 줄을 보여 줌 (crontab -e 에 붙여넣기)
#    bash run_analyzer.sh --update-config       # 설정·검색어 파일도 GitHub 최신으로 (기존 파일은 .bak)
#    bash run_analyzer.sh --analyzer-only       # 예전처럼 분석기만 한 번
#    bash run_analyzer.sh -- --port 8800        # '--' 뒤는 웹 화면 옵션 (--auto 면 tools/pc_analysis.py, --analyzer-only 면 분석기 옵션)
#
#  동작: ① 코드(youtube_topic_analyzer.py · tools/pc_analysis.py · tools/outlier_research.py · tools/outlier_stats.py · tools/tag_keywords.py)는 매번 최신으로
#        ② <폴더>/analyzer_config.toml · keywords.toml · keywords.txt(검색어) · tag_rules.toml 은 없을 때(또는 VERSION 이 더 높을 때) 받고,
#           실행 중에는 tools/pc_analysis.py 가 회차마다 GitHub 에서 고친 것을 받음
#           (예전 것은 .bak — 같은 판이면 내가 고친 설정·검색어를 덮어쓰지 않음)
#        ③ .venv 가상환경을 만들고(처음 한 번) 그 안의 Python으로 실행 — 필요한 패키지는 자동 설치
set -uo pipefail
REPO="yeomin1024/yeomin1024-ytb"; BRANCH="main"; FOLDERS=(); UPDATE_CONFIG=0; NO_VENV=0; ONCE=0; ANALYZER_ONLY=0; PRINT_CRON=0; AUTO=0
EXTRA=()
while [ $# -gt 0 ]; do
  case "$1" in
    --folder) IFS=',' read -r -a _f <<< "$2"; FOLDERS+=("${_f[@]}"); shift 2 ;;
    --repo) REPO="$2"; shift 2 ;;
    --branch) BRANCH="$2"; shift 2 ;;
    --update-config) UPDATE_CONFIG=1; shift ;;
    --no-venv) NO_VENV=1; shift ;;
    --once) ONCE=1; shift ;;
    --auto) AUTO=1; shift ;;
    --analyzer-only) ANALYZER_ONLY=1; shift ;;
    --print-cron) PRINT_CRON=1; shift ;;
    -h|--help) sed -n '2,25p' "$0"; exit 0 ;;
    --) shift; EXTRA+=("$@"); break ;;
    *) EXTRA+=("$1"); shift ;;
  esac
done
cd "$(dirname "$0")" || exit 1
BASE="${RAW_BASE:-https://raw.githubusercontent.com/$REPO/$BRANCH}"
CODE_FILES=(youtube_topic_analyzer.py tools/pc_analysis.py tools/outlier_research.py tools/outlier_stats.py tools/tag_keywords.py
            tools/web_ui.py tools/weekly_analysis.py)
[ ${#FOLDERS[@]} -eq 0 ] && FOLDERS=(economic)
CONFIG_FILES=()
for f in "${FOLDERS[@]}"; do CONFIG_FILES+=("$f/analyzer_config.toml" "$f/keywords.toml" "$f/keywords.txt" "$f/tag_rules.toml"); done
FOLDER_CSV="$(IFS=,; echo "${FOLDERS[*]}")"
step() { echo "[RUNNER] [$(date '+%Y-%m-%dT%H:%M:%S')] $*"; }

if [ "$PRINT_CRON" = 1 ]; then
  step "아래 줄을 'crontab -e' 에 붙여넣으면 매일 17:15(이 PC 시간대가 한국일 때)에 한 회차씩 돕니다 (할당량 초기화 = 한국 오후 4시, 11~3월엔 5시):"
  echo "15 17 * * * cd \"$(pwd)\" && mkdir -p .yt_work && bash run_analyzer.sh --folder $FOLDER_CSV --branch $BRANCH --once >> .yt_work/cron_${FOLDER_CSV//,/_}.log 2>&1"
  exit 0
fi

# .env 틀 (없을 때만) — 비공개 저장소는 GITHUB_TOKEN 이 있어야 코드를 받으므로 먼저 만든다
if [ ! -f .env ]; then
  cat > .env <<'ENVEOF'
# YouTube 분석 비밀 키 파일 — 절대 GitHub 에 올리거나 공유하지 마세요
# '=' 뒤에 값을 붙여넣고 저장 (따옴표 필요 없음). 자세히: guides/pc_analysis.md

# [필수] YouTube Data API v3 키 (Google Cloud 콘솔 → API 및 서비스 → 사용자 인증 정보 → API 키)
YOUTUBE_API_KEY=

# [비공개 저장소면 필수] GitHub 토큰 (Fine-grained, 저장소 yeomin1024-ytb, Contents: Read and write) — 코드 받기·결과 올리기
GITHUB_TOKEN=
ENVEOF
  step "📝 .env 파일을 만들었습니다 → YOUTUBE_API_KEY·GITHUB_TOKEN 을 넣고 저장하세요"
fi
env_get() {   # 환경 변수 → 없으면 .env (값은 출력하지 않음)
  local v="${!1:-}"
  if [ -z "$v" ] && [ -f .env ]; then v="$(sed -n -E "s/^[[:space:]]*$1[[:space:]]*=[[:space:]]*['\"]?([^'\" ]+).*/\1/p" .env | head -1)"; fi
  printf '%s' "$v"
}
TOKEN="$(env_get GITHUB_TOKEN)"
USE_API=0
if [ -n "$TOKEN" ] && [ -z "${RAW_BASE:-}" ] && command -v curl >/dev/null 2>&1; then USE_API=1; fi
step "코드 받는 방법: $([ $USE_API = 1 ] && echo 'GitHub API + 토큰 (비공개 저장소도 됨)' || echo '공개 주소 (토큰 없음 — 저장소가 비공개면 실패)')"

fetch() {   # fetch <저장소 안 경로> <저장할 파일>
  local url="$BASE/$1" out="$2" rc
  mkdir -p "$(dirname "$out")"
  if [ "$USE_API" = 1 ]; then   # 비공개 저장소: GitHub API (Contents, 원본 그대로). 토큰은 표준 입력의 curl 설정으로만
    url="https://api.github.com/repos/$REPO/contents/$1?ref=$BRANCH"
    printf 'header = "Authorization: Bearer %s"\n' "$TOKEN" | curl -fsSL -K - -H "Accept: application/vnd.github.raw" \
      -H "X-GitHub-Api-Version: 2022-11-28" -o "$out.download" "$url"; rc=$?
  elif command -v wget >/dev/null 2>&1; then wget -q -O "$out.download" "$url"; rc=$?
  else curl -fsSL -o "$out.download" "$url"; rc=$?; fi
  if [ $rc -eq 0 ] && [ -s "$out.download" ]; then mv -f "$out.download" "$out"; step "받음: $1"; return 0; fi
  rm -f "$out.download"; step "받기 실패: $url"
  if [ "$USE_API" = 1 ]; then step "👉 토큰이 이 저장소를 읽을 수 있는지 확인: Repository access 에 yeomin1024-ytb · Contents 권한"
  else step "👉 저장소가 비공개면 .env 에 GITHUB_TOKEN 을 넣고 다시 실행하세요"; fi
  return 1
}

# ① 코드 (항상 최신, 못 받으면 있던 파일)
for f in "${CODE_FILES[@]}"; do
  if ! fetch "$f" "$f"; then
    if [ -f "$f" ]; then step "⚠️ 최신 $f 를 못 받아서 있던 파일로 실행합니다"
    else step "❌ $f 를 받지 못했습니다 → 인터넷 연결과 --repo/--branch 값을 확인하세요 (현재: $REPO / $BRANCH)"; exit 1; fi
  fi
done

file_version() {   # 파일 머리(처음 15줄)의 'VERSION: v2.0' → 2.0 (없으면 빈 값) — 설정 파일 새 판 알아보기 (v2.3)
  [ -f "$1" ] || return 0
  head -n 15 "$1" | grep -oE 'VERSION: *v[0-9]+(\.[0-9]+)*' | head -n 1 | sed -E 's/.*v//'
}
version_gt() {     # $1 > $2 ? (숫자 마디별로 비교, sort -V 없이)
  awk -v a="$1" -v b="$2" 'BEGIN { n = split(a, x, "."); m = split(b, y, "."); k = (n > m ? n : m)
    for (i = 1; i <= k; i++) { if ((x[i] + 0) > (y[i] + 0)) exit 0; if ((x[i] + 0) < (y[i] + 0)) exit 1 } exit 1 }'
}

# ② 설정·검색어 파일 (없을 때만, --update-config 면 백업 후 최신으로, GitHub 쪽 VERSION 이 더 높으면 백업 후 새 판으로 — v2.3)
for c in "${CONFIG_FILES[@]}"; do
  if [ "$UPDATE_CONFIG" != 1 ] && [ -f "$c" ]; then
    if fetch "$c" "$c.remote"; then
      lv="$(file_version "$c")"; rv="$(file_version "$c.remote")"
      if [ -n "$lv" ] && [ -n "$rv" ] && version_gt "$rv" "$lv"; then
        cp -f "$c" "$c.bak"; mv -f "$c.remote" "$c"
        step "🔄 새 판으로 바꿈: $c (v$lv → v$rv). 예전 파일은 $c.bak — 내가 고친 내용이 있었다면 거기서 옮기세요"
      else
        rm -f "$c.remote"; step "있던 파일 그대로: $c (PC v${lv:-?} · GitHub v${rv:-?})"
      fi
    else
      step "있던 파일을 그대로 씁니다: $c"
    fi
    continue
  fi
  if [ "$UPDATE_CONFIG" = 1 ] && [ -f "$c" ]; then cp -f "$c" "$c.bak"; step "기존 파일 백업: $c.bak"; fi
  if [ "$UPDATE_CONFIG" = 1 ] || [ ! -f "$c" ]; then
    if ! fetch "$c" "$c"; then
      if [ -f "$c" ]; then step "있던 파일을 그대로 씁니다: $c"
      else step "⚠️ GitHub에 $c 가 없습니다 → --folder 이름을 확인하세요 (현재: $FOLDER_CSV). 새 주제는 Claude 에게 '<주제> 검색어 만들어줘'"; fi
    fi
  fi
done

# ③ Python + 가상환경
PY=""
for c in python3 python; do
  if command -v "$c" >/dev/null 2>&1 && "$c" -c 'import sys; sys.exit(0 if sys.version_info >= (3, 10) else 1)' 2>/dev/null; then PY="$c"; break; fi
done
if [ -z "$PY" ]; then step "❌ Python 3.10 이상을 찾지 못했습니다 → https://www.python.org/downloads/ 에서 설치 후 다시 실행"; exit 1; fi
if [ "$NO_VENV" = 0 ]; then
  if [ ! -x ".venv/bin/python" ]; then
    step "가상환경(.venv) 만드는 중 (처음 한 번)"
    if ! "$PY" -m venv .venv; then   # 반쯤 만든 .venv 를 남기지 않음 (v2.4) → pip 없이 다시 만들고 pip 은 아래에서
      step "⚠️ 가상환경 만들기 실패 → 지우고 pip 없이 다시 만듦 (pip 은 다음 단계에서 설치)"
      rm -rf .venv
      "$PY" -m venv --without-pip .venv || { rm -rf .venv; step "❌ 가상환경을 만들지 못했습니다 (Ubuntu면: sudo apt install python3-venv) → --no-venv 로도 실행 가능"; exit 1; }
    fi
  fi
  # pip 확인 (v2.4): 만들다 끊긴 .venv 는 python 만 있고 pip 이 없음 ('No module named pip') → ensurepip
  if ! .venv/bin/python -m pip --version >/dev/null 2>&1; then
    step "⚠️ 가상환경(.venv)에 pip 이 없습니다 → ensurepip 로 설치"
    .venv/bin/python -m ensurepip --upgrade --default-pip
    if .venv/bin/python -m pip --version >/dev/null 2>&1; then step "pip 준비됨"
    else step "⚠️ ensurepip 실패 → 분석 코드가 공식 get-pip.py 로 한 번 더 시도합니다 (그래도 안 되면 .venv 폴더를 지우고 다시 실행)"; fi
  fi
  PY=".venv/bin/python"
fi

# ④ 실행
if [ "$ANALYZER_ONLY" = 1 ]; then   # 예전 방식: 분석기만, 주제마다 차례로
  code=0
  for f in "${FOLDERS[@]}"; do
    step "실행: python youtube_topic_analyzer.py --config $f/analyzer_config.toml ${EXTRA[*]+${EXTRA[*]}}"
    "$PY" youtube_topic_analyzer.py --config "$f/analyzer_config.toml" ${EXTRA[@]+"${EXTRA[@]}"} || code=$?
  done
elif [ "$AUTO" = 1 ] || [ "$ONCE" = 1 ]; then   # 예전 자동 실행 (할당량이 끝나면 다음 날 이어서)
  ARGS=(tools/pc_analysis.py "${FOLDERS[@]}"); if [ "$ONCE" = 1 ]; then ARGS+=(--once); fi   # 주제가 여러 개면 동시에
  step "실행: python ${ARGS[*]} ${EXTRA[*]+${EXTRA[*]}}"
  "$PY" "${ARGS[@]}" ${EXTRA[@]+"${EXTRA[@]}"}
  code=$?
else                                       # 기본: 웹 화면 (v3.0) — 브라우저가 저절로 열림, Ctrl+C 로 끝냄
  step "웹 화면 실행: python tools/web_ui.py ${FOLDERS[*]} — 브라우저가 저절로 열림 (주소는 아래 ▶ 줄, 끝내려면 Ctrl+C)"
  "$PY" tools/web_ui.py "${FOLDERS[@]}" ${EXTRA[@]+"${EXTRA[@]}"}
  code=$?
fi
if [ $code -eq 3 ]; then step "할당량 때문에 남은 부분이 있습니다 → 다음 실행(또는 cron)이 이어서 받습니다"; fi
if [ $code -ne 0 ] && [ $code -ne 3 ] && [ -f .env ] && ! grep -Eq '^YOUTUBE_API_KEY=.+' .env; then
  step "👉 .env 파일에 YOUTUBE_API_KEY 를 넣고 저장한 뒤 다시 실행하세요"
fi
exit $code
