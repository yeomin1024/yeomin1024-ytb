# eonje-maesu-2026-10-shorts 업로드 시트 (주식 쇼츠)

버전: v1.1 — 2026-10-18 — **기본 언어 en** — 제목·설명란(부호 + 아주 쉬운 영어)·태그를 영어로, 한국어 제목은 언어별 ko, 언어별 설명은 모두 같은 쉬운 영어 · 오디오 언어 ko (사용자 지시 2026-10-18 "설명은 부호, 정말 간단한 영어로 간략하게 표현하도록 해봐 그리고 태그 같은 것도 영어로 하고 한국어로 쓰여진 곳은 정말 간단한 영어로 수정할 수 있어? 모든 영상").
(v1.0 — 2026-10-18 — 새로 만듦: `shorts.md` v2.1 의 제목 R1 · 설명란(4번) · 언어별 제목·설명(1-1)을 업로드 도구가 읽는 꼴로 옮김 · 자막 언어별 (사용자 지시 2026-10-18 "채권 표현 수정하고 영상 업로드 할 준비해").)

기준 파일: 쇼츠 대본 `eonje-maesu-2026-10-shorts.txt` (12문장) · SRT 문장 12 / 자막 14 (`align-audio` 로 오디오에 맞춤) · 오디오 `narration.mp3` 57.8초 · 올릴 영상 = `stock/out/eonje-maesu-2026-10-shorts/final_1080p.mp4` (이 클라우드 컨테이너에만 — git 에 넣지 않음, 장면 파일·오디오로 다시 만듦)

> 업로드: `python3 tools/youtube_upload.py stock eonje-maesu-2026-10-shorts --dry-run` → `--publish-at <시각>` (비공개로 올리고 그 시각에 공개). 롱폼 `eonje-maesu-2026-10` 과 **같은 시각에 공개** (`guides/upload_guide.md` 12번). 자막은 한국어 + 9개 언어 = 10개(4,000단위) — 할당량이 모자라면 남은 언어는 `--captions-only` 로 다음 날.
> ※ 연구·교육용 — 투자 권유가 아님.

## 1. 제목 (기본 언어 en — 아주 쉬운 영어 · 한국어 제목 「매수 신호 10가지, 무작위 매수보다 성공률 높을까?」은 3번 ko 로)

```
10 buy signals vs random buys: higher win rate?
```

## 2. 설명란 (부호 + 아주 쉬운 영어 — 쇼츠는 결과까지)

```
Do buy signals raise your win rate?
Test: AI-made Python code × real past prices (backtest)
SPY (S&P 500 ETF) · from 2016 · 10 buy signals (20-day average, RSI, VIX…)
✓ +5% first · ✗ −2% first
vs 🎲 2,000 accounts with random buy days · same rule
Best: buy when the price crosses above the 20-day average → 52.1% wins
All 10: no different from random buying
▶ Each signal's record + other periods → full video (link below): When to buy? 10 buy signals vs random buys — +5% before −2%?

Closes · sell the next day · fee 0.25% · AI code · AI voice
Past ≠ future · Not investment advice
#SPY #RSI
```

## 3. 언어별 제목·설명 (ko + 8개 언어 제목, 설명은 모두 2번과 같은 쉬운 영어)

```
{
 "ko": {
  "title": "매수 신호 10가지, 무작위 매수보다 성공률 높을까?",
  "description": "Do buy signals raise your win rate?\nTest: AI-made Python code × real past prices (backtest)\nSPY (S&P 500 ETF) · from 2016 · 10 buy signals (20-day average, RSI, VIX…)\n✓ +5% first · ✗ −2% first\nvs 🎲 2,000 accounts with random buy days · same rule\nBest: buy when the price crosses above the 20-day average → 52.1% wins\nAll 10: no different from random buying\n▶ Each signal's record + other periods → full video (link below): When to buy? 10 buy signals vs random buys — +5% before −2%?\n\nCloses · sell the next day · fee 0.25% · AI code · AI voice\nPast ≠ future · Not investment advice\n#SPY #RSI"
 },
 "hi": {
  "title": "10 खरीद संकेत: क्या रैंडम खरीद से ज़्यादा सफलता दर देते हैं?",
  "description": "Do buy signals raise your win rate?\nTest: AI-made Python code × real past prices (backtest)\nSPY (S&P 500 ETF) · from 2016 · 10 buy signals (20-day average, RSI, VIX…)\n✓ +5% first · ✗ −2% first\nvs 🎲 2,000 accounts with random buy days · same rule\nBest: buy when the price crosses above the 20-day average → 52.1% wins\nAll 10: no different from random buying\n▶ Each signal's record + other periods → full video (link below): When to buy? 10 buy signals vs random buys — +5% before −2%?\n\nCloses · sell the next day · fee 0.25% · AI code · AI voice\nPast ≠ future · Not investment advice\n#SPY #RSI"
 },
 "id": {
  "title": "10 sinyal beli: tingkat berhasilnya lebih tinggi dari beli acak?",
  "description": "Do buy signals raise your win rate?\nTest: AI-made Python code × real past prices (backtest)\nSPY (S&P 500 ETF) · from 2016 · 10 buy signals (20-day average, RSI, VIX…)\n✓ +5% first · ✗ −2% first\nvs 🎲 2,000 accounts with random buy days · same rule\nBest: buy when the price crosses above the 20-day average → 52.1% wins\nAll 10: no different from random buying\n▶ Each signal's record + other periods → full video (link below): When to buy? 10 buy signals vs random buys — +5% before −2%?\n\nCloses · sell the next day · fee 0.25% · AI code · AI voice\nPast ≠ future · Not investment advice\n#SPY #RSI"
 },
 "pt": {
  "title": "10 sinais de compra: acertam mais que comprar ao acaso?",
  "description": "Do buy signals raise your win rate?\nTest: AI-made Python code × real past prices (backtest)\nSPY (S&P 500 ETF) · from 2016 · 10 buy signals (20-day average, RSI, VIX…)\n✓ +5% first · ✗ −2% first\nvs 🎲 2,000 accounts with random buy days · same rule\nBest: buy when the price crosses above the 20-day average → 52.1% wins\nAll 10: no different from random buying\n▶ Each signal's record + other periods → full video (link below): When to buy? 10 buy signals vs random buys — +5% before −2%?\n\nCloses · sell the next day · fee 0.25% · AI code · AI voice\nPast ≠ future · Not investment advice\n#SPY #RSI"
 },
 "es-419": {
  "title": "10 señales de compra: ¿aciertan más que comprar al azar?",
  "description": "Do buy signals raise your win rate?\nTest: AI-made Python code × real past prices (backtest)\nSPY (S&P 500 ETF) · from 2016 · 10 buy signals (20-day average, RSI, VIX…)\n✓ +5% first · ✗ −2% first\nvs 🎲 2,000 accounts with random buy days · same rule\nBest: buy when the price crosses above the 20-day average → 52.1% wins\nAll 10: no different from random buying\n▶ Each signal's record + other periods → full video (link below): When to buy? 10 buy signals vs random buys — +5% before −2%?\n\nCloses · sell the next day · fee 0.25% · AI code · AI voice\nPast ≠ future · Not investment advice\n#SPY #RSI"
 },
 "ja": {
  "title": "買いシグナル10個、ランダムに買うより成功率は高い？",
  "description": "Do buy signals raise your win rate?\nTest: AI-made Python code × real past prices (backtest)\nSPY (S&P 500 ETF) · from 2016 · 10 buy signals (20-day average, RSI, VIX…)\n✓ +5% first · ✗ −2% first\nvs 🎲 2,000 accounts with random buy days · same rule\nBest: buy when the price crosses above the 20-day average → 52.1% wins\nAll 10: no different from random buying\n▶ Each signal's record + other periods → full video (link below): When to buy? 10 buy signals vs random buys — +5% before −2%?\n\nCloses · sell the next day · fee 0.25% · AI code · AI voice\nPast ≠ future · Not investment advice\n#SPY #RSI"
 },
 "de": {
  "title": "10 Kaufsignale: höhere Erfolgsquote als zufällige Käufe?",
  "description": "Do buy signals raise your win rate?\nTest: AI-made Python code × real past prices (backtest)\nSPY (S&P 500 ETF) · from 2016 · 10 buy signals (20-day average, RSI, VIX…)\n✓ +5% first · ✗ −2% first\nvs 🎲 2,000 accounts with random buy days · same rule\nBest: buy when the price crosses above the 20-day average → 52.1% wins\nAll 10: no different from random buying\n▶ Each signal's record + other periods → full video (link below): When to buy? 10 buy signals vs random buys — +5% before −2%?\n\nCloses · sell the next day · fee 0.25% · AI code · AI voice\nPast ≠ future · Not investment advice\n#SPY #RSI"
 },
 "vi": {
  "title": "10 tín hiệu mua: tỷ lệ thành công có cao hơn mua ngẫu nhiên?",
  "description": "Do buy signals raise your win rate?\nTest: AI-made Python code × real past prices (backtest)\nSPY (S&P 500 ETF) · from 2016 · 10 buy signals (20-day average, RSI, VIX…)\n✓ +5% first · ✗ −2% first\nvs 🎲 2,000 accounts with random buy days · same rule\nBest: buy when the price crosses above the 20-day average → 52.1% wins\nAll 10: no different from random buying\n▶ Each signal's record + other periods → full video (link below): When to buy? 10 buy signals vs random buys — +5% before −2%?\n\nCloses · sell the next day · fee 0.25% · AI code · AI voice\nPast ≠ future · Not investment advice\n#SPY #RSI"
 },
 "tr": {
  "title": "10 alım sinyali, rastgele alımdan daha yüksek başarı oranı verir mi?",
  "description": "Do buy signals raise your win rate?\nTest: AI-made Python code × real past prices (backtest)\nSPY (S&P 500 ETF) · from 2016 · 10 buy signals (20-day average, RSI, VIX…)\n✓ +5% first · ✗ −2% first\nvs 🎲 2,000 accounts with random buy days · same rule\nBest: buy when the price crosses above the 20-day average → 52.1% wins\nAll 10: no different from random buying\n▶ Each signal's record + other periods → full video (link below): When to buy? 10 buy signals vs random buys — +5% before −2%?\n\nCloses · sell the next day · fee 0.25% · AI code · AI voice\nPast ≠ future · Not investment advice\n#SPY #RSI"
 }
}
```

## 4. 태그 (영어)

```
SPY, S&P 500, when to buy, buy signal, RSI, VIX, moving average, backtest, investing, Shorts
```

## 6. 업로드 설정

| 항목 | 값 |
|---|---|
| 공개 범위 | 비공개로 올리고 예약 시각에 공개 (`--publish-at`) — 롱폼과 같은 시각 |
| 기본 언어 | en (제목·설명·태그 = 부호 + 아주 쉬운 영어 — 한국어 제목은 언어별 ko) |
| 오디오 언어 | ko (내레이션 — 업로드 도구 v1.13) |
| 자막 올리기 | **언어별** (한국어 `eonje-maesu-2026-10-shorts.srt` + `subs/eonje-maesu-2026-10-shorts.<언어>.srt` 9개 — 화면에는 굽지 않음, `stock/guides/README.md` v1.24 4번) |
| 변경되거나 합성된 콘텐츠 | **예** (내레이션이 AI 음성 — CLAUDE.md) |
| 카테고리 | 교육 |
| 썸네일 | `thumbnails/thumbnail_1.png` (세로 9:16 — 그림이 화면 끝까지) → 도구가 세로 720×1280 JPG 로 올림 · 0초 장면도 같은 그림 · 공개 뒤 `i.ytimg.com/vi/<ID>/oardefault.jpg` 로 확인 |
| 관련 동영상 | 롱폼 `eonje-maesu-2026-10` 「매수 타이밍, 저점·RSI·신고가 신호는 2% 떨어지기 전 5% 오를 확률이 무작위 매수보다 높을까?」 (`../youtube.json`) — 스튜디오 → 콘텐츠 → Shorts → 연필 → '관련 동영상' (API 로 못 검 — 사용자가 직접) |
| 자동 더빙 | 스튜디오에서 지원 언어가 보이면 켠다 |

## 7. 결과 (업로드 후)
- (올린 뒤 `youtube.json` 의 영상 ID·예약 시각·자막 언어를 적는다)
