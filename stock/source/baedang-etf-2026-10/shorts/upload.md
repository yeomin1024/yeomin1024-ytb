# baedang-etf-2026-10-shorts 업로드 시트 (주식 쇼츠)

버전: v1.1 — 2026-10-18 — **기본 언어 en** — 제목·설명란(부호 + 아주 쉬운 영어)·태그를 영어로, 한국어 제목은 언어별 ko, 언어별 설명은 모두 같은 쉬운 영어 · 오디오 언어 ko (사용자 지시 2026-10-18 "설명은 부호, 정말 간단한 영어로 간략하게 표현하도록 해봐 그리고 태그 같은 것도 영어로 하고 한국어로 쓰여진 곳은 정말 간단한 영어로 수정할 수 있어? 모든 영상").
(v1.0 — 2026-10-18 — 새로 만듦: `shorts.md` v2.1 의 제목 R1 · 설명란(4번) · 언어별 제목·설명(1-1)을 업로드 도구가 읽는 꼴로 옮김 · 자막 언어별 (사용자 지시 2026-10-18 "채권 표현 수정하고 영상 업로드 할 준비해").)

기준 파일: 쇼츠 대본 `baedang-etf-2026-10-shorts.txt` (12문장) · SRT 문장 12 / 자막 14 (`align-audio` 로 오디오에 맞춤) · 오디오 `narration.mp3` 59.9초 · 올릴 영상 = `stock/out/baedang-etf-2026-10-shorts/final_1080p.mp4` (이 클라우드 컨테이너에만 — git 에 넣지 않음, 장면 파일·오디오로 다시 만듦)

> 업로드: `python3 tools/youtube_upload.py stock baedang-etf-2026-10-shorts --dry-run` → `--publish-at <시각>` (비공개로 올리고 그 시각에 공개). 롱폼 `baedang-etf-2026-10` 과 **같은 시각에 공개** (`guides/upload_guide.md` 12번). 자막은 한국어 + 9개 언어 = 10개(4,000단위) — 할당량이 모자라면 남은 언어는 `--captions-only` 로 다음 날.
> ※ 연구·교육용 — 투자 권유가 아님.

## 1. 제목 (기본 언어 en — 아주 쉬운 영어 · 한국어 제목 「배당 ETF 매달 1,000달러, S&P 500보다 더 남을까?」은 3번 ko 로)

```
Dividend ETF, $1,000 a month: more than the S&P 500?
```

## 2. 설명란 (부호 + 아주 쉬운 영어 — 쇼츠는 결과까지)

```
Dividend ETF for years → more money than an index ETF?
Test: AI-made Python code × real past prices (backtest)
SCHD (US dividend ETF) vs SPY (S&P 500 ETF)
$1,000 / month each · 2011 → 2026 · total in: $180,000
Every dividend: −15% tax → buy again (both)
SCHD ≈ $480,000 · SPY ≈ $590,000
Dividends: SCHD ×2.1 · money left: SPY ×1.22
▶ Why? + other start months → full video (link below): Dividend ETF vs S&P 500: $1,000 a month, 15% tax — which leaves more? SCHD vs SPY

Fractional shares · fee 0.25% · AI code · AI voice
Past ≠ future · Not investment advice
#SCHD #SPY
```

## 3. 언어별 제목·설명 (ko + 8개 언어 제목, 설명은 모두 2번과 같은 쉬운 영어)

```
{
 "ko": {
  "title": "배당 ETF 매달 1,000달러, S&P 500보다 더 남을까?",
  "description": "Dividend ETF for years → more money than an index ETF?\nTest: AI-made Python code × real past prices (backtest)\nSCHD (US dividend ETF) vs SPY (S&P 500 ETF)\n$1,000 / month each · 2011 → 2026 · total in: $180,000\nEvery dividend: −15% tax → buy again (both)\nSCHD ≈ $480,000 · SPY ≈ $590,000\nDividends: SCHD ×2.1 · money left: SPY ×1.22\n▶ Why? + other start months → full video (link below): Dividend ETF vs S&P 500: $1,000 a month, 15% tax — which leaves more? SCHD vs SPY\n\nFractional shares · fee 0.25% · AI code · AI voice\nPast ≠ future · Not investment advice\n#SCHD #SPY"
 },
 "hi": {
  "title": "डिविडेंड ETF में हर महीने $1,000: क्या S&P 500 से ज़्यादा बचेगा?",
  "description": "Dividend ETF for years → more money than an index ETF?\nTest: AI-made Python code × real past prices (backtest)\nSCHD (US dividend ETF) vs SPY (S&P 500 ETF)\n$1,000 / month each · 2011 → 2026 · total in: $180,000\nEvery dividend: −15% tax → buy again (both)\nSCHD ≈ $480,000 · SPY ≈ $590,000\nDividends: SCHD ×2.1 · money left: SPY ×1.22\n▶ Why? + other start months → full video (link below): Dividend ETF vs S&P 500: $1,000 a month, 15% tax — which leaves more? SCHD vs SPY\n\nFractional shares · fee 0.25% · AI code · AI voice\nPast ≠ future · Not investment advice\n#SCHD #SPY"
 },
 "id": {
  "title": "ETF dividen $1.000 tiap bulan: sisa lebih banyak dari S&P 500?",
  "description": "Dividend ETF for years → more money than an index ETF?\nTest: AI-made Python code × real past prices (backtest)\nSCHD (US dividend ETF) vs SPY (S&P 500 ETF)\n$1,000 / month each · 2011 → 2026 · total in: $180,000\nEvery dividend: −15% tax → buy again (both)\nSCHD ≈ $480,000 · SPY ≈ $590,000\nDividends: SCHD ×2.1 · money left: SPY ×1.22\n▶ Why? + other start months → full video (link below): Dividend ETF vs S&P 500: $1,000 a month, 15% tax — which leaves more? SCHD vs SPY\n\nFractional shares · fee 0.25% · AI code · AI voice\nPast ≠ future · Not investment advice\n#SCHD #SPY"
 },
 "pt": {
  "title": "US$ 1.000 por mês em ETF de dividendos: sobra mais que no S&P 500?",
  "description": "Dividend ETF for years → more money than an index ETF?\nTest: AI-made Python code × real past prices (backtest)\nSCHD (US dividend ETF) vs SPY (S&P 500 ETF)\n$1,000 / month each · 2011 → 2026 · total in: $180,000\nEvery dividend: −15% tax → buy again (both)\nSCHD ≈ $480,000 · SPY ≈ $590,000\nDividends: SCHD ×2.1 · money left: SPY ×1.22\n▶ Why? + other start months → full video (link below): Dividend ETF vs S&P 500: $1,000 a month, 15% tax — which leaves more? SCHD vs SPY\n\nFractional shares · fee 0.25% · AI code · AI voice\nPast ≠ future · Not investment advice\n#SCHD #SPY"
 },
 "es-419": {
  "title": "US$1,000 al mes en un ETF de dividendos: ¿queda más que en el S&P 500?",
  "description": "Dividend ETF for years → more money than an index ETF?\nTest: AI-made Python code × real past prices (backtest)\nSCHD (US dividend ETF) vs SPY (S&P 500 ETF)\n$1,000 / month each · 2011 → 2026 · total in: $180,000\nEvery dividend: −15% tax → buy again (both)\nSCHD ≈ $480,000 · SPY ≈ $590,000\nDividends: SCHD ×2.1 · money left: SPY ×1.22\n▶ Why? + other start months → full video (link below): Dividend ETF vs S&P 500: $1,000 a month, 15% tax — which leaves more? SCHD vs SPY\n\nFractional shares · fee 0.25% · AI code · AI voice\nPast ≠ future · Not investment advice\n#SCHD #SPY"
 },
 "ja": {
  "title": "配当ETFに毎月1,000ドル、S&P 500より多く残る？",
  "description": "Dividend ETF for years → more money than an index ETF?\nTest: AI-made Python code × real past prices (backtest)\nSCHD (US dividend ETF) vs SPY (S&P 500 ETF)\n$1,000 / month each · 2011 → 2026 · total in: $180,000\nEvery dividend: −15% tax → buy again (both)\nSCHD ≈ $480,000 · SPY ≈ $590,000\nDividends: SCHD ×2.1 · money left: SPY ×1.22\n▶ Why? + other start months → full video (link below): Dividend ETF vs S&P 500: $1,000 a month, 15% tax — which leaves more? SCHD vs SPY\n\nFractional shares · fee 0.25% · AI code · AI voice\nPast ≠ future · Not investment advice\n#SCHD #SPY"
 },
 "de": {
  "title": "Monatlich 1.000 $ in einen Dividenden-ETF: Bleibt mehr als im S&P 500?",
  "description": "Dividend ETF for years → more money than an index ETF?\nTest: AI-made Python code × real past prices (backtest)\nSCHD (US dividend ETF) vs SPY (S&P 500 ETF)\n$1,000 / month each · 2011 → 2026 · total in: $180,000\nEvery dividend: −15% tax → buy again (both)\nSCHD ≈ $480,000 · SPY ≈ $590,000\nDividends: SCHD ×2.1 · money left: SPY ×1.22\n▶ Why? + other start months → full video (link below): Dividend ETF vs S&P 500: $1,000 a month, 15% tax — which leaves more? SCHD vs SPY\n\nFractional shares · fee 0.25% · AI code · AI voice\nPast ≠ future · Not investment advice\n#SCHD #SPY"
 },
 "vi": {
  "title": "Mỗi tháng 1.000 USD vào ETF cổ tức: còn nhiều hơn S&P 500 không?",
  "description": "Dividend ETF for years → more money than an index ETF?\nTest: AI-made Python code × real past prices (backtest)\nSCHD (US dividend ETF) vs SPY (S&P 500 ETF)\n$1,000 / month each · 2011 → 2026 · total in: $180,000\nEvery dividend: −15% tax → buy again (both)\nSCHD ≈ $480,000 · SPY ≈ $590,000\nDividends: SCHD ×2.1 · money left: SPY ×1.22\n▶ Why? + other start months → full video (link below): Dividend ETF vs S&P 500: $1,000 a month, 15% tax — which leaves more? SCHD vs SPY\n\nFractional shares · fee 0.25% · AI code · AI voice\nPast ≠ future · Not investment advice\n#SCHD #SPY"
 },
 "tr": {
  "title": "Temettü ETF'sine her ay 1.000 $: S&P 500'den fazla kalır mı?",
  "description": "Dividend ETF for years → more money than an index ETF?\nTest: AI-made Python code × real past prices (backtest)\nSCHD (US dividend ETF) vs SPY (S&P 500 ETF)\n$1,000 / month each · 2011 → 2026 · total in: $180,000\nEvery dividend: −15% tax → buy again (both)\nSCHD ≈ $480,000 · SPY ≈ $590,000\nDividends: SCHD ×2.1 · money left: SPY ×1.22\n▶ Why? + other start months → full video (link below): Dividend ETF vs S&P 500: $1,000 a month, 15% tax — which leaves more? SCHD vs SPY\n\nFractional shares · fee 0.25% · AI code · AI voice\nPast ≠ future · Not investment advice\n#SCHD #SPY"
 }
}
```

## 4. 태그 (영어)

```
SCHD, SPY, dividend ETF, dividend investing, dividend tax, S&P 500, backtest, investing, Shorts
```

## 6. 업로드 설정

| 항목 | 값 |
|---|---|
| 공개 범위 | 비공개로 올리고 예약 시각에 공개 (`--publish-at`) — 롱폼과 같은 시각 |
| 기본 언어 | en (제목·설명·태그 = 부호 + 아주 쉬운 영어 — 한국어 제목은 언어별 ko) |
| 오디오 언어 | ko (내레이션 — 업로드 도구 v1.13) |
| 자막 올리기 | **언어별** (한국어 `baedang-etf-2026-10-shorts.srt` + `subs/baedang-etf-2026-10-shorts.<언어>.srt` 9개 — 화면에는 굽지 않음, `stock/guides/README.md` v1.24 4번) |
| 변경되거나 합성된 콘텐츠 | **예** (내레이션이 AI 음성 — CLAUDE.md) |
| 카테고리 | 교육 |
| 썸네일 | `thumbnails/thumbnail_1.png` (세로 9:16 — 그림이 화면 끝까지) → 도구가 세로 720×1280 JPG 로 올림 · 0초 장면도 같은 그림 · 공개 뒤 `i.ytimg.com/vi/<ID>/oardefault.jpg` 로 확인 |
| 관련 동영상 | 롱폼 `baedang-etf-2026-10` 「배당 ETF, 매달 모으면 배당세 15%를 떼고도 같은 돈을 모은 S&P 500보다 더 남을까?」 (`../youtube.json`) — 스튜디오 → 콘텐츠 → Shorts → 연필 → '관련 동영상' (API 로 못 검 — 사용자가 직접) |
| 자동 더빙 | 스튜디오에서 지원 언어가 보이면 켠다 |

## 7. 결과 (업로드 후)
- (올린 뒤 `youtube.json` 의 영상 ID·예약 시각·자막 언어를 적는다)
