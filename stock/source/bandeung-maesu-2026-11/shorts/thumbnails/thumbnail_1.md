# 반등 매수법 쇼츠 썸네일 — 배치 (2026-11-07)

COVER_LAYOUT: band

| 칸 | 내용 |
|---|---|
| 배치 | `COVER_LAYOUT: band` — 세 칸: 위 검정 + 문구 2줄 · 가운데 그림(35~71%) · 아래 검정(첫 문장 자막 자리) — 사용자 지시 2026-11-04 "쇼츠 처음 썸네일 면세처럼 문구랑 이미지 위치 나눠야지" |
| 그림 | `TH-PHOTO.jpg` (ChatGPT 실사 — 밤 편의점 앞 야외 탁자 · 어깨 너머 · 얼굴 안 보임 · 화면 = 파랑으로 빠졌다 빨강으로 튀는 선) — 코드로 옮기기만 (`thumbnail_1.json` → `node video/render/thumb.mjs`) |
| 문구 | 폭락 뒤 반등, 지금 살까? / 이렇게 사면 덜 잃습니다 · 말풍선 '진짜 반등일까..?' |
| 검사 | `python3 tools/cover_check.py stock/source/bandeung-maesu-2026-11/shorts/thumbnails/thumbnail_1.jpg` (band) |
