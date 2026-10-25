# 쇼츠 첫 장면 그림 (= 쇼츠 썸네일, 0초 장면)

v2.0 — 2026-10-25 — **그림은 ChatGPT(글자 없음), 문구는 코드** (사용자 지시 "그 썸네일은 이제 이미지만 만들고 문구는 너가 만들어서 넣는식으로 하자" — `guides/thumbnail_guide.md` 13번)

COVER_LAYOUT: band

| 항목 | 값 |
|---|---|
| 배치 | `COVER_LAYOUT: band` — 세 칸: 위 검정 + 문구 2줄(높이 15.6~33%) · 가운데 그림(35~75%) · 아래 검정(첫 문장 자막 자리) |
| 만드는 법 | `node video/render/thumb.mjs test/source/myeonse-hwangeup-2026-10/shorts/thumbnails/<설정>.json` → `thumbnail_1.jpg` (1080×1920) → `python3 tools/cover_check.py --layout band` |
| **지금(임시)** | 설정 `thumbnail_1.json` — 옛 `images/SHORTS-OPEN.jpg` 의 그림 칸(y 577~1337, 꼬리표 '알면 2분' 포함 — 그림 속 글자)만 잘라 씀 + 위 문구는 코드 |
| **본안(그림 오면)** | 설정 `thumbnail_1.art.json` — 글자 없는 `images/SHORTS-ART.jpg`(가로 3:2, images_chatgpt.md v6.2 27번) + 위 문구·'알면 2분' 꼬리표 모두 코드 |
| 위 1줄 | 일본 면세 바뀌면 ('바뀌면' 노랑 #FFD400) |
| 위 2줄 | 공항에서 2시간 ('2시간' 빨강 #FF2A2A) — 쇼츠 6번 '면세에만 2시간 넘게' · 쇼츠 제목 |
| 그림 꼬리표 | 알면 2분 (검정 글자 · 노랑 상자) — 쇼츠 7번 '2분 정도' |
| 검사 | `tools/cover_check.py --layout band` ✅ (2026-10-25 — 사진칸 35~75% · 글자 16.9~32.9% · 너비 5~95%) |

(v1.0 — 2026-10-24 — ChatGPT 가 문구까지 그린 SHORTS-OPEN 을 cover_shift 로 옮긴 것, 2줄 '공항 줄 1시간 반')
