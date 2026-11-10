# 1편 쇼츠 썸네일 — 배치 (2026-11-04)

COVER_LAYOUT: band

| 칸 | 내용 |
|---|---|
| 배치 | `COVER_LAYOUT: band` — 세 칸: 위 검정 + 문구 2줄 · 가운데 그림(35~71%) · 아래 검정(첫 문장 자막 자리) — 사용자 지시 2026-11-04 "쇼츠 처음 썸네일 면세처럼 문구랑 이미지 위치 나눠야지" |
| 그림 | `../../images/TH-PHOTO2.jpg` (롱폼 썸네일과 같은 실사 · 얼굴 안 보임) — 코드로 옮기기만 (`thumbnail_1.json` → `node video/render/thumb.mjs`) |
| 문구 | 쇼츠 판 사용자 문구 그대로: '이 생각'으로 주식 투자를 하면 / 당신은 99% 손해 봅니다 · 말풍선 '빨리 벌고 싶었을 뿐인데..' |
| 검사 | `python3 tools/cover_check.py stock/source/ppalli-test-2026-11/shorts/thumbnails/thumbnail_1.jpg` (band) |
