#!/usr/bin/env bash
# VERSION: v1.1 — 2026-10-10 — 렌더 완료 1시간 뒤 예약 공개 (사용자 지시), --publish-delay·--no-schedule
# (v1.0: 4단계 자동 진행 — 오디오가 생긴 영상 → SRT 맞춤 → 스토리보드·렌더 → 유튜브 비공개 업로드 → 요약 문서)
# ------------------------------------------------------------------------------------------------
#  사용법 (저장소 최상위에서):
#    bash tools/publish.sh                       # 오디오가 있고 아직 안 올린 영상을 찾아 최대 3개 진행
#    bash tools/publish.sh stock bittu-2026-10   # 영상 하나만
#    옵션: --max N (기본 3) · --dry-run (찾기·점검만) · --no-upload (렌더까지만)
#          --publish-delay 1h (기본: 렌더가 끝난 시각 + 1시간에 예약 공개) · --no-schedule (예약 없이 비공개로만)
#
#  대상 조건 (영상마다):
#    ① <주제폴더>/source/<영상ID>/narration.mp3 · .wav · .m4a 가 있다      ← 사용자가 올리는 오디오
#    ② source/<영상ID>/youtube.json 이 없다 (아직 안 올림)
#    ③ 영상 코드 video/src/episodes/<영상ID>/ 가 있고 video/src/Root.tsx 에 등록돼 있다 (3단계 스토리보드까지 끝남)
#  진행 (영상마다, 실패하면 그 영상만 멈추고 다음 영상으로):
#    1. npm run align-audio   — 오디오는 고치지 않고 SRT·subtitles.ts 를 오디오에 맞춤 (고지 카드 자리 3.5초 쉼 필요)
#    2. 타입 검사 → 스토리보드 다시 렌더 (시간이 바뀌었으므로)
#    3. 완성 영상 렌더 → <주제폴더>/out/<영상ID>/final_1080p.mp4 (ffprobe로 길이·오디오 확인)
#    4. tools/youtube_upload.py — 비공개 업로드 + 예약 공개(렌더 완료 + 1시간), 제목·설명란(챕터 재계산)·태그·자막·채택 썸네일 1개 → youtube.json
#       (키가 없으면 업로드만 건너뜀)
#    5. tools/make_summary.py — 요약 문서 갱신
#  끝나면 Claude가 바뀐 파일(SRT, subtitles.ts, youtube.json, summary.md, 스토리보드)을 main에 커밋·푸시한다. mp4는 올리지 않음.
# ------------------------------------------------------------------------------------------------
set -uo pipefail
cd "$(dirname "$0")/.."
ROOT="$(pwd)"
MAX=3; DRY=0; NO_UPLOAD=0; ONLY_TOPIC=""; ONLY_ID=""; DELAY="1h"
while [ $# -gt 0 ]; do
  case "$1" in
    --max) MAX="$2"; shift 2 ;;
    --dry-run) DRY=1; shift ;;
    --no-upload) NO_UPLOAD=1; shift ;;
    --publish-delay) DELAY="$2"; shift 2 ;;
    --no-schedule) DELAY=""; shift ;;
    *) if [ -z "$ONLY_TOPIC" ]; then ONLY_TOPIC="$1"; else ONLY_ID="$1"; fi; shift ;;
  esac
done
log() { echo "[PUBLISH] [$(date -u +%Y-%m-%dT%H:%M:%SZ)] $*"; }

# ── 1. 대상 찾기 ──
CANDIDATES=()
for src in "$ROOT"/*/source/*/; do
  src="${src%/}"; vid="$(basename "$src")"; topic="$(basename "$(dirname "$(dirname "$src")")")"
  [ -n "$ONLY_TOPIC" ] && [ "$topic" != "$ONLY_TOPIC" ] && continue
  [ -n "$ONLY_ID" ] && [ "$vid" != "$ONLY_ID" ] && continue
  audio=""; for e in mp3 wav m4a; do [ -f "$src/narration.$e" ] && audio="$src/narration.$e" && break; done
  [ -z "$audio" ] && continue
  if [ -f "$src/youtube.json" ]; then log "skip video=$vid reason=이미_업로드(youtube.json)"; continue; fi
  if [ ! -d "video/src/episodes/$vid" ] || ! grep -q "id=\"$vid\"" video/src/Root.tsx; then
    log "skip video=$vid reason=영상_코드_없음 → 3단계(영상 코드·스토리보드)를 먼저 만들어야 함"; continue
  fi
  CANDIDATES+=("$topic/$vid")
done
log "stage=scan candidates=${#CANDIDATES[@]} max=$MAX dry_run=$DRY no_upload=$NO_UPLOAD publish_delay=${DELAY:-없음(비공개만)} list=${CANDIDATES[*]:-없음}"
[ ${#CANDIDATES[@]} -eq 0 ] && { log "할 일 없음 (오디오가 있고 아직 안 올린 영상이 없음)"; exit 0; }
[ "$DRY" = 1 ] && exit 0

if [ "$NO_UPLOAD" = 0 ] && { [ -z "${YOUTUBE_CLIENT_ID:-}" ] || [ -z "${YOUTUBE_CLIENT_SECRET:-}" ] || [ -z "${YOUTUBE_REFRESH_TOKEN:-}" ]; }; then
  log "⚠️ 유튜브 키(YOUTUBE_CLIENT_ID·SECRET·REFRESH_TOKEN)가 없어 업로드는 건너뜀 → 렌더까지만"
  NO_UPLOAD=1
fi
BROWSER_ARG=(); [ -n "${REMOTION_BROWSER:-}" ] && BROWSER_ARG=(--browser-executable "$REMOTION_BROWSER")

DONE=0; FAILED=()
for item in "${CANDIDATES[@]}"; do
  [ "$DONE" -ge "$MAX" ] && { log "최대 ${MAX}개에 도달 → 나머지는 다음 실행에서"; break; }
  topic="${item%%/*}"; vid="${item##*/}"; out="$topic/out/$vid"
  t0=$(date +%s)
  log "stage=start video=$vid topic=$topic"
  fail() { log "❌ video=$vid stage=$1 → 이 영상은 멈춤 (다음 영상 계속). $2"; FAILED+=("$vid:$1"); }

  (cd video && node scripts/align-audio.mjs "$topic" "$vid") || { fail align-audio "고지 카드 자리 3.5초 쉼·문장 수를 확인 (오디오는 고치지 않음)"; continue; }
  (cd video && npx tsc --noEmit) || { fail typecheck "영상 코드 오류"; continue; }
  (cd video && node scripts/storyboard.mjs "$vid" "../$out") || { fail storyboard "스토리보드 렌더 실패"; continue; }
  mkdir -p "$out"
  (cd video && npx remotion render "$vid" "../$out/final_1080p.mp4" --codec=h264 --crf=18 "${BROWSER_ARG[@]}") \
    || { fail render "렌더 실패"; continue; }
  dur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$out/final_1080p.mp4" 2>/dev/null || echo "?")
  has_audio=$(ffprobe -v error -select_streams a -show_entries stream=codec_name -of csv=p=0 "$out/final_1080p.mp4" 2>/dev/null | head -1)
  log "stage=render video=$vid duration_s=$dur audio=${has_audio:-없음} size_mb=$(du -m "$out/final_1080p.mp4" | cut -f1)"
  [ -z "$has_audio" ] && { fail render-check "완성 영상에 오디오가 없음 (align-audio 내보내기 확인)"; continue; }

  if [ "$NO_UPLOAD" = 0 ]; then
    SCHED=(); [ -n "$DELAY" ] && SCHED=(--publish-at "+$DELAY")     # 렌더가 끝난 지금 기준 (기본 +1h)
    log "stage=schedule video=$vid publish=${DELAY:+렌더 완료 + $DELAY}${DELAY:-예약 없음(비공개)}"
    python3 tools/youtube_upload.py "$topic" "$vid" "${SCHED[@]}" || { fail upload "업로드 실패 (영상은 렌더됨)"; python3 tools/make_summary.py "$topic" "$vid"; continue; }
  else
    log "stage=upload video=$vid status=건너뜀"
  fi
  python3 tools/make_summary.py "$topic" "$vid"
  DONE=$((DONE + 1))
  log "stage=done video=$vid seconds=$(( $(date +%s) - t0 ))"
done
log "stage=end done=$DONE failed=${#FAILED[@]} ${FAILED[*]:-}"
log "다음: 바뀐 파일을 main에 커밋·푸시 (mp4 제외 — .gitignore)"
[ ${#FAILED[@]} -eq 0 ]
