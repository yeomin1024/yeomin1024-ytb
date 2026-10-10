#!/usr/bin/env bash
# VERSION: v1.0 — 2026-10-10 — 클라우드(Claude Code)에서 분석기 실행 → 결과를 <주제폴더>/result/ 로 복사 (커밋·푸시는 Claude가 main에)
# ------------------------------------------------------------------------------------------------
#  사용법 (저장소 최상위에서):
#    bash tools/run_analysis.sh stock                  # stock/analyzer_config.toml 로 분석
#    bash tools/run_analysis.sh health -- --cases 3    # '--' 뒤는 분석기 옵션
#
#  필요: 환경변수 YOUTUBE_API_KEY (클라우드 환경 설정의 Network secrets 또는 환경 변수). .env 파일은 쓰지 않음.
#  하는 일:
#    ① .venv(처음 한 번)에서 분석기를 --no-push --no-video --no-open 으로 실행
#       - --no-push : 분석기가 직접 GitHub에 올리지 않음 (Claude가 main에 커밋)
#       - --no-video: 성공사례 영상 파일을 받지 않음 (공개 저장소에 남의 영상 금지, 클라우드 IP 다운로드 차단 회피)
#    ② output/<주제폴더>/result/ → <주제폴더>/result/ 로 교체 복사 (영상·음성 파일은 복사하지 않음)
#  분석 결과로 지시사항을 고치는 절차: guides/pipeline.md 1·2단계
# ------------------------------------------------------------------------------------------------
set -euo pipefail
cd "$(dirname "$0")/.."
ROOT="$(pwd)"

TOPIC_DIR="${1:-}"
if [ -z "$TOPIC_DIR" ] || [ ! -f "$TOPIC_DIR/analyzer_config.toml" ]; then
  echo "[ANALYSIS] ❌ 주제 폴더를 주세요 (예: bash tools/run_analysis.sh stock). 설정 파일: <주제폴더>/analyzer_config.toml"
  exit 1
fi
shift
[ "${1:-}" = "--" ] && shift
if [ -z "${YOUTUBE_API_KEY:-}" ]; then
  echo "[ANALYSIS] ❌ 환경변수 YOUTUBE_API_KEY 가 없습니다 → 클라우드 환경 설정(Network secrets/환경 변수)에 넣고 새 세션에서 다시 실행"
  exit 1
fi

log() { echo "[ANALYSIS] [$(date -u +%Y-%m-%dT%H:%M:%SZ)] $*"; }

if [ ! -x .venv/bin/python ]; then
  log "stage=venv 가상환경 만들기 (.venv)"
  python3 -m venv .venv
fi
PY=.venv/bin/python

log "stage=run topic_dir=$TOPIC_DIR options=--no-push --no-video --no-open $*"
"$PY" youtube_topic_analyzer.py --config "$TOPIC_DIR/analyzer_config.toml" --no-push --no-video --no-open "$@"

SRC="output/$TOPIC_DIR/result"
if [ ! -d "$SRC" ]; then
  log "❌ 결과 폴더가 없습니다: $SRC (설정 파일의 PROJECT_FOLDER가 폴더 이름과 같은지 확인)"
  exit 1
fi
log "stage=copy from=$SRC to=$TOPIC_DIR/result (영상·음성 제외)"
rm -rf "$TOPIC_DIR/result"
mkdir -p "$TOPIC_DIR/result"
(cd "$SRC" && find . -type f ! \( -iname '*.mp4' -o -iname '*.mkv' -o -iname '*.webm' -o -iname '*.mov' -o -iname '*.m4a' -o -iname '*.mp3' -o -iname '*.opus' \) \
  -exec cp --parents {} "$ROOT/$TOPIC_DIR/result/" \;)
log "stage=done files=$(find "$TOPIC_DIR/result" -type f | wc -l) → 다음: guides/pipeline.md 2단계 (data_insights.md·지시사항 갱신)"
