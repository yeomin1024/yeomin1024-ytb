# 쇼츠 첫 장면 그림 (= 쇼츠 썸네일, 0초 장면)

v1.0 — 2026-10-25 — **그림은 ChatGPT(글자 없음), 문구·말풍선은 코드** (시험 채널 규칙 — `guides/thumbnail_guide.md` 13번, 면세 쇼츠와 같은 꼴)

COVER_LAYOUT: band

| 항목 | 값 |
|---|---|
| 배치 | `COVER_LAYOUT: band` — 세 칸: 위 검정 + 문구 2줄 · 가운데 그림(35~71%) · 아래 검정(첫 문장 자막 자리) |
| 만드는 법 | 그림이 오면 `node video/render/thumb.mjs test/source/kaerieo-tugi-2026-10/shorts/thumbnails/thumbnail_1.art.json` → `thumbnail_1.jpg` → `python3 tools/cover_check.py --layout band` → 쇼츠 `render.mjs sync`·`video` |
| 그림 | `images/SHORTS-ART.jpg` (가로 3:2, images_chatgpt.md v2.0 22번) — 밤 골목 집적소 옆 버려진 캐리어 + 들여다보는 행인 |
| 위 1줄 | 깨끗한 일본 길거리에 ('깨끗한' 노랑) |
| 위 2줄 | 버려진 캐리어, 왜? ('왜?' 빨강) — 제작안 v1.1 그대로 |
| 말풍선 | 이거 누가 두고 간 거야? (흰 말풍선, 행인의 말) — **Claude 가 지은 말** (면세 쇼츠처럼 인물 말풍선을 넣음 — 바꿀 말이 있으면 설정 파일의 text 만 고침) |
| 뺀 것 | 꼬리표 '도시마구 1년 290개' (제작안 v1.1) |
| 지금 | 그림이 아직 없어 `thumbnail_1.jpg` 없음 → 쇼츠 첫 장면도 그림이 온 뒤 렌더 |
