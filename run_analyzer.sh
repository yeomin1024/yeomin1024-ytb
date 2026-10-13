#!/usr/bin/env bash
# ================================================================================================
#  YouTube 분석 PC 실행기 (macOS / Linux)
#  VERSION: v2.0 — 2026-10-13 — 기본 주제 economic(경제·재테크). 분석기 + 작은 채널 성공 사례(자막·썸네일·댓글)를
#           tools/pc_analysis.py 로 함께 돌리고, 할당량이 끝나 못 한 부분은 할당량 초기화(한국 오후 4~5시) 뒤 자동으로 이어서.
#           검색어 목록 <폴더>/keywords.toml 도 받음. --once · --analyzer-only(예전 방식) · --print-cron 추가
#  (v1.0 — 2026-10-09 — 분석 코드·설정 파일을 GitHub에서 wget으로 받아 분석기만 실행)
# ================================================================================================
#  처음 한 번 (새 폴더에서, 자세히: guides/pc_analysis.md):
#    wget -O run_analyzer.sh https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/main/run_analyzer.sh
#    bash run_analyzer.sh
#    → 처음 실행하면 .env 파일이 생깁니다. YOUTUBE_API_KEY(필수)·GITHUB_TOKEN(권장)을 넣고 다시 실행
#
#  자주 쓰는 실행:
#    bash run_analyzer.sh                       # 경제·재테크 — 끝날 때까지 (남으면 다음 날 자동으로 이어서, 터미널을 열어 두기)
#    bash run_analyzer.sh --once                # 한 회차만 (남은 부분은 다음에 실행할 때)
#    bash run_analyzer.sh --print-cron          # 매일 17:15 에 --once 로 돌리는 crontab 줄을 보여 줌 (crontab -e 에 붙여넣기)
#    bash run_analyzer.sh --update-config       # 설정·검색어 파일도 GitHub 최신으로 (기존 파일은 .bak)
#    bash run_analyzer.sh --analyzer-only       # 예전처럼 분석기만 한 번
#    bash run_analyzer.sh -- --dry-run          # '--' 뒤는 tools/pc_analysis.py 옵션 (--analyzer-only 면 분석기 옵션)
#
#  동작: ① 코드(youtube_topic_analyzer.py · tools/pc_analysis.py · tools/outlier_research.py · tools/outlier_stats.py)는 매번 최신으로
#        ② <폴더>/analyzer_config.toml · <폴더>/keywords.toml 은 없을 때만 받음 (내가 고친 설정·검색어를 덮어쓰지 않음)
#        ③ .venv 가상환경을 만들고(처음 한 번) 그 안의 Python으로 실행 — 필요한 패키지는 자동 설치
set -uo pipefail
REPO="yeomin1024/yeomin1024-ytb"; BRANCH="main"; FOLDER="economic"; UPDATE_CONFIG=0; NO_VENV=0; ONCE=0; ANALYZER_ONLY=0; PRINT_CRON=0
EXTRA=()
while [ $# -gt 0 ]; do
  case "$1" in
    --folder) FOLDER="$2"; shift 2 ;;
    --repo) REPO="$2"; shift 2 ;;
    --branch) BRANCH="$2"; shift 2 ;;
    --update-config) UPDATE_CONFIG=1; shift ;;
    --no-venv) NO_VENV=1; shift ;;
    --once) ONCE=1; shift ;;
    --analyzer-only) ANALYZER_ONLY=1; shift ;;
    --print-cron) PRINT_CRON=1; shift ;;
    -h|--help) sed -n '2,25p' "$0"; exit 0 ;;
    --) shift; EXTRA+=("$@"); break ;;
    *) EXTRA+=("$1"); shift ;;
  esac
done
cd "$(dirname "$0")" || exit 1
BASE="${RAW_BASE:-https://raw.githubusercontent.com/$REPO/$BRANCH}"
CODE_FILES=(youtube_topic_analyzer.py tools/pc_analysis.py tools/outlier_research.py tools/outlier_stats.py)
CONFIG_FILES=("$FOLDER/analyzer_config.toml" "$FOLDER/keywords.toml")
step() { echo "[RUNNER] [$(date '+%Y-%m-%dT%H:%M:%S')] $*"; }

if [ "$PRINT_CRON" = 1 ]; then
  step "아래 줄을 'crontab -e' 에 붙여넣으면 매일 17:15(이 PC 시간대가 한국일 때)에 한 회차씩 돕니다 (할당량 초기화 = 한국 오후 4시, 11~3월엔 5시):"
  echo "15 17 * * * cd \"$(pwd)\" && mkdir -p .yt_work && bash run_analyzer.sh --folder $FOLDER --branch $BRANCH --once >> .yt_work/cron_$FOLDER.log 2>&1"
  exit 0
fi

fetch() {   # fetch <저장소 안 경로> <저장할 파일>
  local url="$BASE/$1" out="$2"
  mkdir -p "$(dirname "$out")"
  if command -v wget >/dev/null 2>&1; then wget -q -O "$out.download" "$url"; else curl -fsSL -o "$out.download" "$url"; fi
  if [ $? -eq 0 ] && [ -s "$out.download" ]; then mv -f "$out.download" "$out"; step "받음: $1"; return 0; fi
  rm -f "$out.download"; step "받기 실패: $url"; return 1
}

# ① 코드 (항상 최신, 못 받으면 있던 파일)
for f in "${CODE_FILES[@]}"; do
  if ! fetch "$f" "$f"; then
    if [ -f "$f" ]; then step "⚠️ 최신 $f 를 못 받아서 있던 파일로 실행합니다"
    else step "❌ $f 를 받지 못했습니다 → 인터넷 연결과 --repo/--branch 값을 확인하세요 (현재: $REPO / $BRANCH)"; exit 1; fi
  fi
done

# ② 설정·검색어 파일 (없을 때만, --update-config 면 백업 후 최신으로)
for c in "${CONFIG_FILES[@]}"; do
  if [ "$UPDATE_CONFIG" = 1 ] && [ -f "$c" ]; then cp -f "$c" "$c.bak"; step "기존 파일 백업: $c.bak"; fi
  if [ "$UPDATE_CONFIG" = 1 ] || [ ! -f "$c" ]; then
    if ! fetch "$c" "$c"; then
      if [ -f "$c" ]; then step "있던 파일을 그대로 씁니다: $c"
      else step "⚠️ GitHub에 $c 가 없습니다 → --folder 이름을 확인하세요 (현재: $FOLDER)"; fi
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
    "$PY" -m venv .venv || { step "❌ 가상환경을 만들지 못했습니다 (Ubuntu면: sudo apt install python3-venv) → --no-venv 로도 실행 가능"; exit 1; }
  fi
  PY=".venv/bin/python"
fi

# ④ 실행
if [ "$ANALYZER_ONLY" = 1 ]; then ARGS=(youtube_topic_analyzer.py --config "$FOLDER/analyzer_config.toml")
else ARGS=(tools/pc_analysis.py "$FOLDER"); if [ "$ONCE" = 1 ]; then ARGS+=(--once); fi; fi
step "실행: python ${ARGS[*]} ${EXTRA[*]+${EXTRA[*]}}"
"$PY" "${ARGS[@]}" ${EXTRA[@]+"${EXTRA[@]}"}
code=$?
if [ $code -eq 3 ]; then step "할당량 때문에 남은 부분이 있습니다 → 다음 실행(또는 cron)이 이어서 받습니다"; fi
if [ $code -ne 0 ] && [ $code -ne 3 ] && [ -f .env ] && ! grep -Eq '^YOUTUBE_API_KEY=.+' .env; then
  step "👉 .env 파일에 YOUTUBE_API_KEY 를 넣고 저장한 뒤 다시 실행하세요"
fi
exit $code
