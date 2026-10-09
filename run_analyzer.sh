#!/usr/bin/env bash
# ================================================================================================
#  YouTube 주제 분석기 실행기 (macOS / Linux)
#  VERSION: v1.0 — 2026-10-09 — 분석 코드·설정 파일을 GitHub에서 wget으로 받아 실행 (wget 없으면 curl)
# ================================================================================================
#  처음 한 번 (새 폴더에서):
#    wget -O run_analyzer.sh https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/main/run_analyzer.sh
#    bash run_analyzer.sh
#    → 처음 실행하면 .env 파일이 생깁니다. YOUTUBE_API_KEY(필수)·GITHUB_TOKEN(권장)을 넣고 다시 실행
#
#  자주 쓰는 실행:
#    bash run_analyzer.sh                                     # 주식 (stock/analyzer_config.toml)
#    bash run_analyzer.sh --folder realestate --topic 부동산   # 다른 주제
#    bash run_analyzer.sh --update-config                     # 설정 파일도 GitHub 최신으로 (기존 파일은 .bak)
#    bash run_analyzer.sh --branch claude/dreamy-brown-r105x4  # main에 합치기 전 브랜치에서 받기
#    bash run_analyzer.sh -- --no-push --cases 3              # '--' 뒤는 분석기 옵션
#
#  동작: ① youtube_topic_analyzer.py 를 매번 최신으로 받음 (실패하면 있던 파일 사용)
#        ② <폴더>/analyzer_config.toml 은 없을 때만 받음 (내가 고친 설정을 덮어쓰지 않음)
#        ③ .venv 가상환경을 만들고(처음 한 번) 그 안의 Python으로 실행 — 필요한 패키지는 분석기가 자동 설치
set -uo pipefail
REPO="yeomin1024/yeomin1024-ytb"; BRANCH="main"; FOLDER="stock"; TOPIC=""; UPDATE_CONFIG=0; NO_VENV=0; EXTRA=()
while [ $# -gt 0 ]; do
  case "$1" in
    --folder) FOLDER="$2"; shift 2 ;;
    --topic) TOPIC="$2"; shift 2 ;;
    --repo) REPO="$2"; shift 2 ;;
    --branch) BRANCH="$2"; shift 2 ;;
    --update-config) UPDATE_CONFIG=1; shift ;;
    --no-venv) NO_VENV=1; shift ;;
    -h|--help) sed -n '2,22p' "$0"; exit 0 ;;
    --) shift; EXTRA+=("$@"); break ;;
    *) EXTRA+=("$1"); shift ;;
  esac
done
cd "$(dirname "$0")" || exit 1
BASE="${RAW_BASE:-https://raw.githubusercontent.com/$REPO/$BRANCH}"
SCRIPT="youtube_topic_analyzer.py"
CFG="$FOLDER/analyzer_config.toml"
step() { echo "[RUNNER] $*"; }

fetch() {   # fetch <저장소 안 경로> <저장할 파일>
  local url="$BASE/$1" out="$2"
  mkdir -p "$(dirname "$out")"
  if command -v wget >/dev/null 2>&1; then wget -q -O "$out.download" "$url"; else curl -fsSL -o "$out.download" "$url"; fi
  if [ $? -eq 0 ] && [ -s "$out.download" ]; then mv -f "$out.download" "$out"; step "받음: $1"; return 0; fi
  rm -f "$out.download"; step "받기 실패: $url"; return 1
}

# ① 분석 코드 (항상 최신)
if ! fetch "$SCRIPT" "$SCRIPT"; then
  if [ -f "$SCRIPT" ]; then step "⚠️ 최신 코드를 못 받아서 있던 $SCRIPT 로 실행합니다"
  else step "❌ $SCRIPT 를 받지 못했습니다 → 인터넷 연결과 --repo/--branch 값을 확인하세요 (현재: $REPO / $BRANCH)"; exit 1; fi
fi

# ② 설정 파일 (없을 때만, --update-config 면 백업 후 최신으로)
if [ "$UPDATE_CONFIG" = 1 ] && [ -f "$CFG" ]; then cp -f "$CFG" "$CFG.bak"; step "기존 설정 파일 백업: $CFG.bak"; fi
if [ "$UPDATE_CONFIG" = 1 ] || [ ! -f "$CFG" ]; then
  if ! fetch "$CFG" "$CFG"; then
    if [ -f "$CFG" ]; then step "설정 파일은 있던 것을 그대로 씁니다: $CFG"
    else step "GitHub에 $CFG 가 없습니다 → 분석기가 새 설정 파일 틀을 만들고 주제어 자동완성 모드로 실행합니다"; fi
  fi
fi

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
ARGS=("$SCRIPT")
if [ -f "$CFG" ]; then ARGS+=(--config "$CFG"); else ARGS+=(--folder "$FOLDER"); fi
if [ -n "$TOPIC" ]; then ARGS+=(--topic "$TOPIC"); fi
step "실행: python ${ARGS[*]} ${EXTRA[*]+${EXTRA[*]}}"
"$PY" "${ARGS[@]}" ${EXTRA[@]+"${EXTRA[@]}"}
code=$?
if [ $code -ne 0 ] && [ -f .env ] && ! grep -Eq '^YOUTUBE_API_KEY=.+' .env; then
  step "👉 .env 파일에 YOUTUBE_API_KEY 를 넣고 저장한 뒤 다시 실행하세요"
fi
exit $code
