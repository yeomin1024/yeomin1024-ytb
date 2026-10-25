# 롱폼 썸네일 (본안)

v4.0 — 2026-10-25 — 글자 없는 그림(THUMB-L-ART)이 와서 **본안 완성** · 그림은 ChatGPT, 문구·말풍선은 코드 (`guides/thumbnail_guide.md` 13번)
(v3.0 — 문구를 사용자 지시대로: "첫줄 문구: 11월 일본 면세 변경되면 골치 아프다, 캐릭터 말풍선: 이걸 언제 기다려... (알면 면세 줄 X, 모르면 면세에만 2시간 넘게 삭제)")

| 항목 | 값 |
|---|---|
| 만드는 법 | `node video/render/thumb.mjs test/source/myeonse-hwangeup-2026-10/thumbnails/thumbnail_1.json` → `thumbnail_1.jpg` (1280×720, 265KB) |
| 그림 | `images/THUMB-L-ART.jpg` (images_chatgpt.md v6.3 26번) — 긴 공항 줄 앞에서 이마를 짚고 고개 떨군 여행객 (손해를 알고 좌절한 얼굴) · 그림 속 글자 없음 (2026-10-25 Claude 확대 확인) |
| 말풍선 | 이걸 언제 기다려... (흰 말풍선, 오른쪽 위 — 꼬리가 여행객 머리 쪽 `tailPos 0.1`) |
| 아래 1줄 | 11월 일본 면세 변경되면 골치 아프다 ('11월' 노랑 · '골치 아프다' 빨강 · 검정 외곽선) |
| 아래 2줄 | 가장 빠르게 면세 받는 방법 ('가장 빠르게' 노랑 · 1줄보다 크게 · 오른쪽 끝 x ≤ 1020) |
| 옛 그림 | `images/THUMB-L.jpg` (문구까지 ChatGPT 가 그린 것) — 쓰지 않음 |
