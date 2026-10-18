# keobeodeu-kol-2026-10-shorts 업로드 시트 (주식 쇼츠)

버전: v1.1 — 2026-10-18 — **기본 언어 en** — 제목·설명란(부호 + 아주 쉬운 영어)·태그를 영어로, 한국어 제목은 언어별 ko, 언어별 설명은 모두 같은 쉬운 영어 · 오디오 언어 ko (사용자 지시 2026-10-18 "설명은 부호, 정말 간단한 영어로 간략하게 표현하도록 해봐 그리고 태그 같은 것도 영어로 하고 한국어로 쓰여진 곳은 정말 간단한 영어로 수정할 수 있어? 모든 영상").
(v1.0 — 2026-10-18 — 새로 만듦: `shorts.md` v2.1.1 의 제목 R1 · 설명란(4번) · 언어별 제목·설명(1-1)을 업로드 도구가 읽는 꼴로 옮김 · 자막 언어별 (사용자 지시 2026-10-18 "채권 표현 수정하고 영상 업로드 할 준비해").)

기준 파일: 쇼츠 대본 `keobeodeu-kol-2026-10-shorts.txt` (12문장) · SRT 문장 12 / 자막 15 (`align-audio` 로 오디오에 맞춤) · 오디오 `narration.mp3` 62.3초 · 올릴 영상 = `stock/out/keobeodeu-kol-2026-10-shorts/final_1080p.mp4` (이 클라우드 컨테이너에만 — git 에 넣지 않음, 장면 파일·오디오로 다시 만듦)

> 업로드: `python3 tools/youtube_upload.py stock keobeodeu-kol-2026-10-shorts --dry-run` → `--publish-at <시각>` (비공개로 올리고 그 시각에 공개). 롱폼 `keobeodeu-kol-2026-10` 과 **같은 시각에 공개** (`guides/upload_guide.md` 12번). 자막은 한국어 + 9개 언어 = 10개(4,000단위) — 할당량이 모자라면 남은 언어는 `--captions-only` 로 다음 날.
> ※ 연구·교육용 — 투자 권유가 아님.

## 1. 제목 (기본 언어 en — 아주 쉬운 영어 · 한국어 제목 「커버드콜 10만 달러, 분배금 매달 써도 원금 지켜질까?」은 3번 ko 로)

```
Covered call, $100K: spend the payout monthly — is it safe?
```

## 2. 설명란 (부호 + 아주 쉬운 영어 — 쇼츠는 결과까지)

```
Covered call ETF: spend the payout every month → is the $100K safe?
Test: AI-made Python code × real past prices (backtest)
QYLD (Nasdaq-100 covered call) vs QQQ (Nasdaq-100, no covered call)
$100,000 each · Dec 2013 → 2026
QYLD: spend every payout · QQQ: sell the same $ on the same day (fair ⚖️)
Paid out: ≈ $110,000 each
QYLD: ≈ $75,000 left (−25.3% vs $100K)
QQQ: ≈ $510,000 left (×6.83)
▶ Why? + other start months → full video (link below): Covered call: spend the payout every month — is your $100K safe? QYLD vs QQQ, 13 years

Before tax · fee 0.25% · AI code · AI voice
Past ≠ future · Not investment advice
#QYLD #QQQ
```

## 3. 언어별 제목·설명 (ko + 8개 언어 제목, 설명은 모두 2번과 같은 쉬운 영어)

```
{
 "ko": {
  "title": "커버드콜 10만 달러, 분배금 매달 써도 원금 지켜질까?",
  "description": "Covered call ETF: spend the payout every month → is the $100K safe?\nTest: AI-made Python code × real past prices (backtest)\nQYLD (Nasdaq-100 covered call) vs QQQ (Nasdaq-100, no covered call)\n$100,000 each · Dec 2013 → 2026\nQYLD: spend every payout · QQQ: sell the same $ on the same day (fair ⚖️)\nPaid out: ≈ $110,000 each\nQYLD: ≈ $75,000 left (−25.3% vs $100K)\nQQQ: ≈ $510,000 left (×6.83)\n▶ Why? + other start months → full video (link below): Covered call: spend the payout every month — is your $100K safe? QYLD vs QQQ, 13 years\n\nBefore tax · fee 0.25% · AI code · AI voice\nPast ≠ future · Not investment advice\n#QYLD #QQQ"
 },
 "hi": {
  "title": "कवर्ड कॉल में $100K: हर महीने भुगतान खर्च करें, क्या मूलधन बचेगा?",
  "description": "Covered call ETF: spend the payout every month → is the $100K safe?\nTest: AI-made Python code × real past prices (backtest)\nQYLD (Nasdaq-100 covered call) vs QQQ (Nasdaq-100, no covered call)\n$100,000 each · Dec 2013 → 2026\nQYLD: spend every payout · QQQ: sell the same $ on the same day (fair ⚖️)\nPaid out: ≈ $110,000 each\nQYLD: ≈ $75,000 left (−25.3% vs $100K)\nQQQ: ≈ $510,000 left (×6.83)\n▶ Why? + other start months → full video (link below): Covered call: spend the payout every month — is your $100K safe? QYLD vs QQQ, 13 years\n\nBefore tax · fee 0.25% · AI code · AI voice\nPast ≠ future · Not investment advice\n#QYLD #QQQ"
 },
 "id": {
  "title": "$100 ribu di covered call: dividen dipakai tiap bulan, modal aman?",
  "description": "Covered call ETF: spend the payout every month → is the $100K safe?\nTest: AI-made Python code × real past prices (backtest)\nQYLD (Nasdaq-100 covered call) vs QQQ (Nasdaq-100, no covered call)\n$100,000 each · Dec 2013 → 2026\nQYLD: spend every payout · QQQ: sell the same $ on the same day (fair ⚖️)\nPaid out: ≈ $110,000 each\nQYLD: ≈ $75,000 left (−25.3% vs $100K)\nQQQ: ≈ $510,000 left (×6.83)\n▶ Why? + other start months → full video (link below): Covered call: spend the payout every month — is your $100K safe? QYLD vs QQQ, 13 years\n\nBefore tax · fee 0.25% · AI code · AI voice\nPast ≠ future · Not investment advice\n#QYLD #QQQ"
 },
 "pt": {
  "title": "US$ 100 mil em covered call: gastando a renda todo mês, o capital se mantém?",
  "description": "Covered call ETF: spend the payout every month → is the $100K safe?\nTest: AI-made Python code × real past prices (backtest)\nQYLD (Nasdaq-100 covered call) vs QQQ (Nasdaq-100, no covered call)\n$100,000 each · Dec 2013 → 2026\nQYLD: spend every payout · QQQ: sell the same $ on the same day (fair ⚖️)\nPaid out: ≈ $110,000 each\nQYLD: ≈ $75,000 left (−25.3% vs $100K)\nQQQ: ≈ $510,000 left (×6.83)\n▶ Why? + other start months → full video (link below): Covered call: spend the payout every month — is your $100K safe? QYLD vs QQQ, 13 years\n\nBefore tax · fee 0.25% · AI code · AI voice\nPast ≠ future · Not investment advice\n#QYLD #QQQ"
 },
 "es-419": {
  "title": "US$100,000 en covered call: gastando cada pago, ¿se conserva el capital?",
  "description": "Covered call ETF: spend the payout every month → is the $100K safe?\nTest: AI-made Python code × real past prices (backtest)\nQYLD (Nasdaq-100 covered call) vs QQQ (Nasdaq-100, no covered call)\n$100,000 each · Dec 2013 → 2026\nQYLD: spend every payout · QQQ: sell the same $ on the same day (fair ⚖️)\nPaid out: ≈ $110,000 each\nQYLD: ≈ $75,000 left (−25.3% vs $100K)\nQQQ: ≈ $510,000 left (×6.83)\n▶ Why? + other start months → full video (link below): Covered call: spend the payout every month — is your $100K safe? QYLD vs QQQ, 13 years\n\nBefore tax · fee 0.25% · AI code · AI voice\nPast ≠ future · Not investment advice\n#QYLD #QQQ"
 },
 "ja": {
  "title": "カバードコールに10万ドル、分配金を毎月使っても元本は守られる？",
  "description": "Covered call ETF: spend the payout every month → is the $100K safe?\nTest: AI-made Python code × real past prices (backtest)\nQYLD (Nasdaq-100 covered call) vs QQQ (Nasdaq-100, no covered call)\n$100,000 each · Dec 2013 → 2026\nQYLD: spend every payout · QQQ: sell the same $ on the same day (fair ⚖️)\nPaid out: ≈ $110,000 each\nQYLD: ≈ $75,000 left (−25.3% vs $100K)\nQQQ: ≈ $510,000 left (×6.83)\n▶ Why? + other start months → full video (link below): Covered call: spend the payout every month — is your $100K safe? QYLD vs QQQ, 13 years\n\nBefore tax · fee 0.25% · AI code · AI voice\nPast ≠ future · Not investment advice\n#QYLD #QQQ"
 },
 "de": {
  "title": "100.000 $ im Covered Call: Ausschüttung monatlich ausgeben – bleibt das Kapital?",
  "description": "Covered call ETF: spend the payout every month → is the $100K safe?\nTest: AI-made Python code × real past prices (backtest)\nQYLD (Nasdaq-100 covered call) vs QQQ (Nasdaq-100, no covered call)\n$100,000 each · Dec 2013 → 2026\nQYLD: spend every payout · QQQ: sell the same $ on the same day (fair ⚖️)\nPaid out: ≈ $110,000 each\nQYLD: ≈ $75,000 left (−25.3% vs $100K)\nQQQ: ≈ $510,000 left (×6.83)\n▶ Why? + other start months → full video (link below): Covered call: spend the payout every month — is your $100K safe? QYLD vs QQQ, 13 years\n\nBefore tax · fee 0.25% · AI code · AI voice\nPast ≠ future · Not investment advice\n#QYLD #QQQ"
 },
 "vi": {
  "title": "100.000 USD vào covered call: tiêu cổ tức mỗi tháng, vốn gốc có giữ được?",
  "description": "Covered call ETF: spend the payout every month → is the $100K safe?\nTest: AI-made Python code × real past prices (backtest)\nQYLD (Nasdaq-100 covered call) vs QQQ (Nasdaq-100, no covered call)\n$100,000 each · Dec 2013 → 2026\nQYLD: spend every payout · QQQ: sell the same $ on the same day (fair ⚖️)\nPaid out: ≈ $110,000 each\nQYLD: ≈ $75,000 left (−25.3% vs $100K)\nQQQ: ≈ $510,000 left (×6.83)\n▶ Why? + other start months → full video (link below): Covered call: spend the payout every month — is your $100K safe? QYLD vs QQQ, 13 years\n\nBefore tax · fee 0.25% · AI code · AI voice\nPast ≠ future · Not investment advice\n#QYLD #QQQ"
 },
 "tr": {
  "title": "Covered call'a 100.000 $: dağıtımı her ay harcarsanız anapara korunur mu?",
  "description": "Covered call ETF: spend the payout every month → is the $100K safe?\nTest: AI-made Python code × real past prices (backtest)\nQYLD (Nasdaq-100 covered call) vs QQQ (Nasdaq-100, no covered call)\n$100,000 each · Dec 2013 → 2026\nQYLD: spend every payout · QQQ: sell the same $ on the same day (fair ⚖️)\nPaid out: ≈ $110,000 each\nQYLD: ≈ $75,000 left (−25.3% vs $100K)\nQQQ: ≈ $510,000 left (×6.83)\n▶ Why? + other start months → full video (link below): Covered call: spend the payout every month — is your $100K safe? QYLD vs QQQ, 13 years\n\nBefore tax · fee 0.25% · AI code · AI voice\nPast ≠ future · Not investment advice\n#QYLD #QQQ"
 }
}
```

## 4. 태그 (영어)

```
QYLD, QQQ, covered call, covered call ETF, monthly dividend, Nasdaq 100, backtest, investing, Shorts
```

## 6. 업로드 설정

| 항목 | 값 |
|---|---|
| 공개 범위 | 비공개로 올리고 예약 시각에 공개 (`--publish-at`) — 롱폼과 같은 시각 |
| 기본 언어 | en (제목·설명·태그 = 부호 + 아주 쉬운 영어 — 한국어 제목은 언어별 ko) |
| 오디오 언어 | ko (내레이션 — 업로드 도구 v1.13) |
| 자막 올리기 | **언어별** (한국어 `keobeodeu-kol-2026-10-shorts.srt` + `subs/keobeodeu-kol-2026-10-shorts.<언어>.srt` 9개 — 화면에는 굽지 않음, `stock/guides/README.md` v1.24 4번) |
| 변경되거나 합성된 콘텐츠 | **예** (내레이션이 AI 음성 — CLAUDE.md) |
| 카테고리 | 교육 |
| 썸네일 | `thumbnails/thumbnail_1.png` (세로 9:16 — 그림이 화면 끝까지) → 도구가 세로 720×1280 JPG 로 올림 · 0초 장면도 같은 그림 · 공개 뒤 `i.ytimg.com/vi/<ID>/oardefault.jpg` 로 확인 |
| 관련 동영상 | 롱폼 `keobeodeu-kol-2026-10` 「커버드콜 분배금, 매달 꺼내 쓰면 같은 금액을 매도한 QQQ보다 13년 뒤 원금이 더 남을까?」 (`../youtube.json`) — 스튜디오 → 콘텐츠 → Shorts → 연필 → '관련 동영상' (API 로 못 검 — 사용자가 직접) |
| 자동 더빙 | 스튜디오에서 지원 언어가 보이면 켠다 |

## 7. 결과 (업로드 후)
- (올린 뒤 `youtube.json` 의 영상 ID·예약 시각·자막 언어를 적는다)
