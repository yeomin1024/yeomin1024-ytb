# 종이인형 (투명 PNG) — 모두 표정이 있음

ChatGPT 가 `stock/story/protagonist_chatgpt.md` (v3.0) 대로 만들어 이 폴더에 올린다 (PNG 투명, 700KB 이하).
- 주인공 8장: `P-BONSEOK.png` · `-WALK` · `-PHONE` · `-DESPAIR` · `-RESOLVE` · `-STUDY` · `-BACK` · `-SMILE`
- 4화 개미 무리 1장: `P-CROWD.png`

장면 파일에서는 일본 축제 영상처럼 `Puppet.stage({ dir: "../../../stock/story/puppet/", files: { BONSEOK: { f: "P-BONSEOK.png" }, … } })` 로 쓴다 (`video/render/puppet.js`).

올라오면 Claude 가 검수한다:
- 8장이 같은 인형인지 (얼굴 모양·안경·작업 점퍼·뻗친 머리)
- **표정이 프롬프트대로인지** (좌절 = 놀란 얼굴이 아니라 무너진 얼굴)
- 글자 없음 · 투명(또는 순초록) · 잘림 검사 · 파일이 끝까지 읽히는지
