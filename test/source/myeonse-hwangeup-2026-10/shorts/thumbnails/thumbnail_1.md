# 쇼츠 첫 장면 그림 (= 쇼츠 썸네일, 0초 장면)

v3.0 — 2026-10-25 — 문구 바꿈 (사용자 지시 "쇼츠 문구: 11월 일본 면세 변경 후 벌어질 골치 아픈 일 (알면 2분 삭제, 캐릭터 말풍선: 면세 줄 안서는 방법 있나?)")
· 그림은 ChatGPT(글자 없음), 문구는 코드 (`guides/thumbnail_guide.md` 13번)

COVER_LAYOUT: band

| 항목 | 값 |
|---|---|
| 배치 | `COVER_LAYOUT: band` — 세 칸: 위 검정 + 문구 2줄 · 가운데 그림(35~71%) · 아래 검정(첫 문장 자막 자리) |
| 만드는 법 | `node video/render/thumb.mjs test/source/myeonse-hwangeup-2026-10/shorts/thumbnails/<설정>.json` → `thumbnail_1.jpg` (1080×1920) → `python3 tools/cover_check.py --layout band` |
| **지금(임시)** | 설정 `thumbnail_1.json` — 옛 `images/SHORTS-OPEN.jpg` 의 그림 칸에서 그림 속 꼬리표('알면 2분', y 630~786) **아래만** 잘라 씀(y 800~1421) → 남은 글자 없음. 문구·말풍선은 모두 코드 |
| **본안(그림 오면)** | 설정 `thumbnail_1.art.json` — 글자 없는 `images/SHORTS-ART.jpg`(가로 3:2, images_chatgpt.md v6.3 27번) |
| 위 1줄 | 11월 일본 면세 변경 후 ('11월' 노랑) |
| 위 2줄 | 벌어질 골치 아픈 일 ('골치 아픈 일' 빨강) |
| 말풍선 | 면세 줄 안 서는 방법 있나? (검정 글자 · 흰 말풍선, 휴대전화를 보는 앞쪽 여행객의 말) — 사용자 문구 '안서는' 을 띄어 씀('안 서는') |
| 뺀 것 | 꼬리표 '알면 2분' (사용자 지시) |
| 검사 | `tools/cover_check.py --layout band` ✅ (2026-10-25 — 사진칸 35~71% · 글자 19.0~30.6% · 너비 5~96%) |

(v2.0 — 2026-10-25 — '일본 면세 바뀌면 / 공항에서 2시간' + 그림 속 '알면 2분' · v1.0 — 2026-10-24 — ChatGPT 가 문구까지 그린 SHORTS-OPEN)
