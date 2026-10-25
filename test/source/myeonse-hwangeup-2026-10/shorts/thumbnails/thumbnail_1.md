# 쇼츠 첫 장면 그림 (= 쇼츠 썸네일, 0초 장면)

v4.0 — 2026-10-25 — 글자 없는 그림(SHORTS-ART)이 와서 **본안 완성** · 그림은 ChatGPT, 문구·말풍선은 코드 (`guides/thumbnail_guide.md` 13번)
(v3.0 — 문구를 사용자 지시대로: "쇼츠 문구: 11월 일본 면세 변경 후 벌어질 골치 아픈 일 (알면 2분 삭제, 캐릭터 말풍선: 면세 줄 안서는 방법 있나?)")

COVER_LAYOUT: band

| 항목 | 값 |
|---|---|
| 배치 | `COVER_LAYOUT: band` — 세 칸: 위 검정 + 문구 2줄 · 가운데 그림(35~71%) · 아래 검정(첫 문장 자막 자리) |
| 만드는 법 | `node video/render/thumb.mjs test/source/myeonse-hwangeup-2026-10/shorts/thumbnails/thumbnail_1.json` → `thumbnail_1.jpg` → `python3 tools/cover_check.py --layout band` ✅ (사진칸 35~71% · 글자 19.0~30.6%) |
| 그림 | `images/SHORTS-ART.jpg` (가로 3:2, images_chatgpt.md v6.3 27번) — 초록 화면 휴대전화를 보는 여행객(뒷모습) + 긴 줄 · 그림 속 글자 없음 |
| 위 1줄 | 11월 일본 면세 변경 후 ('11월' 노랑) |
| 위 2줄 | 벌어질 골치 아픈 일 ('골치 아픈 일' 빨강) |
| 말풍선 | 면세 줄 안 서는 방법 있나? (흰 말풍선, 여행객 머리 위 — 사용자 문구 '안서는' 을 띄어 씀) |
| 옛 그림 | `images/SHORTS-OPEN.jpg` · `original/` (문구까지 ChatGPT 가 그린 것) — 쓰지 않음 |
