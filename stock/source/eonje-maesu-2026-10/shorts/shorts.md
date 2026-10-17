# 쇼츠 — `eonje-maesu-2026-10` 롱폼으로 보내는 쇼츠 (프롤로그형 · 언어 없는 화면)

버전: v1.0.1 — 2026-10-17 — 쇼츠 썸네일 글자 `64.7%` · `BUY` · `?` (간단한 영어·숫자·기호 — 사용자 지시 2026-10-17 "문구 없으니까 너무 허전하네 buy, sell 같은 정말 간단해서 모두 알만한 영어 문구는 써도 돼" · "숫자나 기호 같은 문구도 써도 돼").
(v1.0 — 2026-10-17 — 새로 만듦 (사용자 지시 2026-10-17 "저번에 쇼츠 만들었었으니까 같은 방식으로 영상 당 쇼츠 1개씩 만들어봐" · "다른점은 전세계 시청자들 대상이니까 언어 문구, 자막 달지 말고 영상으로만 잘 이해가 가도록 해야해 계속 진행해"). 재테크 쇼츠(`economic/source/eunte-kkeonaeseugi-2026-10/shorts/`)와 같은 꼴 — 첫 문장 하나에 핵심 → 상황 → 질문 → '아래 영상에서 확인하세요' — 에 주식 규칙(자막 없음 · 화면 글자 언어 없음 · 결말 가림 · 10개 언어)을 더함.)

- 보내는 곳(롱폼): **매수 타이밍, 저점·RSI·신고가 신호는 2% 떨어지기 전 5% 오를 확률이 무작위 매수보다 높을까?** (`../upload.md` 1번 제목) — 쇼츠의 '관련 동영상'으로 연결 (롱폼 공개 뒤)
- **넣지 않는 것 (롱폼의 결말):** 10가지 신호의 **끝 성공률**과 무작위 90% 범위(회색 띠) 안인지 밖인지, 가장 높은·낮은 방법, 실패 기준 1%·1.5%와 1994~2015년 결과. 화면에도 종합 표·회색 띠를 그리지 않는다.
- **보여 주는 것:** 20일 평균선 돌파의 2021년 12월 성공률 64.7%(무작위 51.8%), 그 앞 ✓×5와 그 뒤 ✗×6 — 모두 롱폼 '-이동평균선' 장의 중간 숫자.
- 근거: [`stock/guides/shorts_insights.md`](../../../guides/shorts_insights.md) v1.0 (주식 쇼츠 분석 — 경주 그래프 쇼츠 같은 채널 ×32~×203 · 45~59초 19% · 금액 +20%p ⚑ · 해시태그 3~5개 6.6%) · 공통 규칙 `guides/shorts_guide.md` 4번
- 길이: **9문장 · 284음절 · 예상 약 48.6초** (`render.mjs sync --estimate` — 진행자 H04 실측으로 맞춘 추정) · 45~59초 · 50자 넘는 문장 없음 · 첫 문장 약 6.1초
- 목소리: 진행자 H04 하나 (CLAUDE.md) — 한국어 내레이션, **화면은 소리 없이도 이해되게** (해외 시청자는 자동 더빙·자동 번역)
- 숫자: 쇼츠 대본의 숫자는 모두 롱폼 대본에 있다 — `python3 tools/backtest/shorts_numcheck.py stock eonje-maesu-2026-10` → [`checklist.md`](checklist.md) (없음 0). 화면 숫자는 `stock/source/eonje-maesu-2026-10/backtest/barrier/anim.js` (롱폼과 같은 결과 파일 — 그날까지 판정 난 거래만 셈)에서만.
- ※ 연구·교육용 — 투자 권유가 아님

## 1. 제목

| | 제목 (한국어 — 기본 언어) | 글자 | 까닭 |
|---|---|---|---|
| **R1 (추천)** | **매수 타이밍 20일선, 한때 성공률 64.7%… 무작위 매수보다 높을까?** | 40 | 금액 대신 % (이 영상엔 금액 없음) · '한때'로 경주 중간 숫자임을 밝힘 · 맨 앞 니즈 낱말 '매수 타이밍'(롱폼 제목과 같음) · 질문으로 끝 |
| R2 | 매수 신호 10가지, 무작위로 매수한 계좌 2천 개보다 성공률 높을까? | 39 | 롱폼 질문 그대로 (신호 10가지 vs 무작위 2천 개) — 숫자 비교 형식은 쇼츠 비교 집단에서 7.5%로 낮아 2안 |

쓰지 않은 것: **'이유'**(쇼츠가 이유를 말하지 않음 — `guides/shorts_guide.md` 4번 5항) · '재테크'(0%)·'투자'(3.8%)·'주식투자'(4.7%)·'AI'(6.2%) 낱말 (shorts_insights 3번) · 결말(롱폼의 끝 결과). 길이는 40자 안팎 — 쇼츠 비교 집단에서 20자 미만 16%·30~39자 14%·40자 이상 15%로 차이가 작다 (shorts_insights 3번).

### 1-1. 언어별 제목·설명 (localizations — 롱폼 `upload.md` 5번과 같은 9개 언어)

JSON — 롱폼 업로드 시트와 같은 꼴 (업로드 도구 v1.6 이 읽는 형식). '▶' 줄의 롱폼 제목은 그 언어의 롱폼 제목. 해시태그는 언어와 상관없는 티커.

```
{
 "en": {
  "title": "Buy timing with the 20-day line: a 64.7% win rate at one point… better than random buys?",
  "description": "SPY bought each time it closed above its 20-day average: in December 2021 the win rate was 64.7%. Over the same period, 2,000 accounts that bought on random dates averaged 51.8%. Then, through July 2022, it failed six times in a row.\n▶ The 10-year results of 10 buy signals, including RSI and VIX, are in the related video below — When to buy: do dip, RSI and breakout signals hit +5% before −2% more often than random buys?\n\nWin = the price rises 5% above the buy price before it falls 2%; loss = it falls 2% first (closing prices). Data and full conditions are in the main video's description. The code was written by AI and the narration is an AI voice.\nPast data only — not investment advice.\n#SPY #RSI"
 },
 "hi": {
  "title": "20-दिन लाइन से खरीद का समय: एक समय 64.7% सफलता… क्या रैंडम खरीद से बेहतर?",
  "description": "हर बार जब SPY अपने 20-दिन औसत से ऊपर बंद हुआ, तब खरीदा: दिसंबर 2021 में सफलता दर 64.7% थी। उसी समय रैंडम तारीखों पर खरीदने वाले 2,000 खातों का औसत 51.8% था। फिर जुलाई 2022 तक लगातार छह बार विफल रहा।\n▶ RSI और VIX सहित 10 खरीद संकेतों के 10 साल के नतीजे नीचे जुड़े वीडियो में — कब खरीदें: क्या डिप, RSI और ब्रेकआउट संकेत रैंडम खरीद से ज़्यादा बार −2% से पहले +5% छूते हैं?\n\nसफलता = खरीद भाव से 2% गिरने से पहले 5% ऊपर; विफलता = पहले 2% नीचे (क्लोज़िंग भाव)। डेटा और पूरी शर्तें मुख्य वीडियो के विवरण में हैं। कोड AI ने लिखा और आवाज़ AI की है।\nसिर्फ़ पिछला डेटा — निवेश सलाह नहीं।\n#SPY #RSI"
 },
 "id": {
  "title": "Waktu beli dengan garis 20 hari: sempat berhasil 64,7%… lebih baik dari beli acak?",
  "description": "SPY dibeli setiap kali ditutup di atas rata-rata 20 harinya: pada Desember 2021 tingkat keberhasilannya 64,7%. Pada periode yang sama, 2.000 akun yang membeli di tanggal acak rata-rata 51,8%. Lalu sampai Juli 2022, gagal enam kali berturut-turut.\n▶ Hasil 10 tahun dari 10 sinyal beli, termasuk RSI dan VIX, ada di video tertaut di bawah — Kapan beli: sinyal dip, RSI, breakout lebih sering naik 5% sebelum turun 2% dibanding beli acak?\n\nBerhasil = harga naik 5% dari harga beli sebelum turun 2%; gagal = turun 2% lebih dulu (harga penutupan). Data dan syarat lengkap ada di deskripsi video utama. Kode ditulis AI dan narasinya suara AI.\nHanya data masa lalu — bukan saran investasi.\n#SPY #RSI"
 },
 "pt": {
  "title": "Hora de comprar pela média de 20 dias: chegou a 64,7% de acerto… melhor que comprar ao acaso?",
  "description": "SPY comprado toda vez que fechou acima da média de 20 dias: em dezembro de 2021 a taxa de acerto era 64,7%. No mesmo período, 2.000 contas que compraram em datas aleatórias tinham média de 51,8%. Depois, até julho de 2022, falhou seis vezes seguidas.\n▶ Os resultados de 10 anos de 10 sinais de compra, incluindo RSI e VIX, estão no vídeo vinculado abaixo — Quando comprar: queda, RSI e rompimento sobem 5% antes de cair 2% mais que compras aleatórias?\n\nAcerto = o preço sobe 5% acima do preço de compra antes de cair 2%; erro = cai 2% primeiro (preços de fechamento). Dados e condições completas na descrição do vídeo principal. O código foi escrito por IA e a narração é voz de IA.\nApenas dados passados — não é recomendação de investimento.\n#SPY #RSI"
 },
 "es-419": {
  "title": "Comprar con la media de 20 días: llegó a 64.7% de acierto… ¿mejor que comprar al azar?",
  "description": "SPY comprado cada vez que cerró por encima de su media de 20 días: en diciembre de 2021 la tasa de acierto era 64.7%. En el mismo período, 2,000 cuentas que compraron en fechas al azar promediaban 51.8%. Después, hasta julio de 2022, falló seis veces seguidas.\n▶ Los resultados de 10 años de 10 señales de compra, incluidas RSI y VIX, están en el video vinculado abajo — ¿Cuándo comprar? ¿Caída, RSI y ruptura suben 5% antes de caer 2% más seguido que comprar al azar?\n\nAcierto = el precio sube 5% sobre el precio de compra antes de caer 2%; fallo = cae 2% primero (precios de cierre). Datos y condiciones completas en la descripción del video principal. El código lo escribió una IA y la narración es una voz de IA.\nSolo datos pasados — no es asesoría de inversión.\n#SPY #RSI"
 },
 "ja": {
  "title": "20日線で買うタイミング、一時は成功率64.7%… ランダムに買うより高い？",
  "description": "SPYが20日平均線を上抜けるたびに買った結果、2021年12月の成功率は64.7%。同じ期間、日付だけランダムに選んで買った2,000口座の平均は51.8%でした。その後2022年7月までは6回連続で失敗。\n▶ RSI・VIXなど買いシグナル10種類の10年の結果は、下のリンクの動画で — 買うタイミング：押し目・RSI・高値更新のシグナルは、ランダムに買うより−2%の前に+5%に届く確率が高い？\n\n成功＝2%下がる前に買値より5%上昇、失敗＝先に2%下落（終値）。データと計算条件は本編の説明欄にあります。計算コードはAIが書き、ナレーションはAI音声です。\n過去データによる計算で、投資の勧誘ではありません。\n#SPY #RSI"
 },
 "de": {
  "title": "Kaufzeitpunkt per 20-Tage-Linie: zeitweise 64,7 % Trefferquote … besser als Zufallskäufe?",
  "description": "SPY jedes Mal gekauft, wenn der Schlusskurs über den 20-Tage-Durchschnitt stieg: Im Dezember 2021 lag die Trefferquote bei 64,7 %. Im selben Zeitraum kamen 2.000 Konten mit zufälligen Kaufdaten im Schnitt auf 51,8 %. Danach scheiterte es bis Juli 2022 sechsmal in Folge.\n▶ Die 10-Jahres-Ergebnisse von 10 Kaufsignalen, darunter RSI und VIX, im verlinkten Video unten — Wann kaufen: Erreichen Dip-, RSI- und Ausbruchssignale öfter +5 % vor −2 % als zufällige Käufe?\n\nTreffer = der Kurs steigt 5 % über den Kaufpreis, bevor er 2 % fällt; Fehlschlag = zuerst 2 % Minus (Schlusskurse). Daten und alle Bedingungen in der Beschreibung des Hauptvideos. Der Code wurde von einer KI geschrieben, die Stimme ist eine KI-Stimme.\nNur historische Daten – keine Anlageberatung.\n#SPY #RSI"
 },
 "vi": {
  "title": "Mua theo đường 20 ngày: có lúc thành công 64,7%… hơn mua ngẫu nhiên không?",
  "description": "Mua SPY mỗi khi giá đóng cửa vượt lên trên đường trung bình 20 ngày: tháng 12/2021 tỉ lệ thành công là 64,7%. Cùng thời gian, 2.000 tài khoản mua vào ngày ngẫu nhiên có trung bình 51,8%. Sau đó, đến tháng 7/2022, thất bại sáu lần liên tiếp.\n▶ Kết quả 10 năm của 10 tín hiệu mua, gồm RSI và VIX, ở video liên kết bên dưới — Khi nào mua: tín hiệu giảm sâu, RSI, phá đỉnh có lên 5% trước khi xuống 2% nhiều hơn mua ngẫu nhiên?\n\nThành công = giá tăng 5% so với giá mua trước khi giảm 2%; thất bại = giảm 2% trước (giá đóng cửa). Dữ liệu và điều kiện đầy đủ trong phần mô tả video chính. Mã do AI viết, lời thuyết minh là giọng AI.\nChỉ là dữ liệu quá khứ — không phải lời khuyên đầu tư.\n#SPY #RSI"
 },
 "tr": {
  "title": "20 günlük çizgiyle alım zamanı: bir ara %64,7 başarı… rastgele alımdan iyi mi?",
  "description": "SPY, kapanışı 20 günlük ortalamanın üstüne çıktığı her seferinde alındı: Aralık 2021'de başarı oranı %64,7'ydi. Aynı dönemde rastgele tarihlerde alım yapan 2.000 hesabın ortalaması %51,8'di. Sonra Temmuz 2022'ye kadar art arda altı kez başarısız oldu.\n▶ RSI ve VIX dahil 10 alım sinyalinin 10 yıllık sonuçları aşağıdaki bağlantılı videoda — Ne zaman almalı: düşüş, RSI ve kırılım sinyali, rastgele alımdan sık mı %2 düşmeden %5 çıkar?\n\nBaşarı = fiyat %2 düşmeden önce alış fiyatının %5 üstüne çıkar; başarısızlık = önce %2 düşer (kapanış fiyatları). Veriler ve tüm koşullar ana videonun açıklamasında. Kodu yapay zekâ yazdı, seslendirme yapay zekâ sesi.\nYalnızca geçmiş veriler — yatırım tavsiyesi değildir.\n#SPY #RSI"
 }
}
```

## 2. 대본 (시각은 예상 — 내레이션 뒤 실제 시각으로 맞춤)

| # | 시각 | 대본 | 역할 | 화면 (언어 없음 — 숫자·$·%·연도·티커·BUY·기호·아이콘) |
|---|---|---|---|---|
| 1 | 0:00 | 20일 평균선을 넘을 때 매수하면, 2021년 12월 성공률이 64.7%였습니다. | 핵심 한 문장 | **쇼츠 썸네일 그림** (글자 `64.7%` · `BUY` · `?` — `thumbnails/thumbnail_1.md`: 노란 평균선을 뚫는 초록 화살표 + 같은 높이의 주사위 더미) |
| 2 | 0:06 | S&P 500을 따라가는 ETF인 SPY로, 2016년부터 시험한 결과예요. | 대상·기간 | `SPY = S&P 500` · 2016년 SPY 종가(흰 선)와 20일 평균(노란 선)이 날짜를 따라 그려지고, 흰 선이 노란 선을 넘는 날마다 BUY ▲ · 아래 범례 `— SPY  — 20  ↗ BUY` |
| 3 | 0:12 | 5% 먼저 오르면 성공, 2% 먼저 떨어지면 실패로 셌어요. | 규칙 | 실제 거래 두 개 나란히: 왼쪽 2016.07 매수 → +5% 초록 점선에 먼저 닿아 ✓ · 오른쪽 2021.12 매수 → −2% 빨간 점선에 먼저 닿아 ✗ |
| 4 | 0:17 | 같은 때, 날짜만 무작위로 매수한 계좌 2천 개의 평균은 51.8%였고요. | 비교 상대 | 📅 `2021.12` · 왼쪽 카드 `↗20 BUY 64.7%` · 오른쪽 카드 주사위 `× 2,000` `51.8%` |
| 5 | 0:23 | 2016년 7월부터 2018년 1월까지는 다섯 번 연속 성공하기도 했어요. | 잘된 때 | 2016.06~2018.01 차트 — 판정마다 ✓ · 아래 칸 ✓✓✓✓✓ 가 하나씩 켜짐 · 위에 그날까지 성공률(초록)·무작위 평균(회색)이 날짜를 따라 바뀜 |
| 6 | 0:28 | 그런데 2021년 12월 뒤로는, 2022년 7월까지 여섯 번 연속 실패했습니다. | 꺾인 때 | 2021.11~2022.07 차트 — ✗✗✗✗✗✗ · 성공률 64.7% → 55.0% (그날까지 판정 난 것만) |
| 7 | 0:34 | RSI, 공포지수 VIX처럼 많이 쓰는 매수 신호 10가지도 함께 시험했어요. | 넓힘 | `10 × BUY` + 신호 10칸 (아이콘 + `RSI < 40` · `VIX ≥ 20` · `20D` · `−1%` …) — 4번(20일 평균)은 노란 테두리, RSI·VIX 를 말할 때 그 칸이 커짐 |
| 8 | 0:40 | 10년이 끝났을 때, 무작위보다 확실히 나은 신호가 있었을까요? | 질문 | `2016 → 2026` · 칸마다 노란 ? · 아래 `10 × BUY ＞ 🎲 ?` |
| 9 | 0:44 | 10가지 신호의 결과는 아래 영상에서 확인하세요. | 롱폼 안내 | 끝 화면: 신호 아이콘 10개 · `BUY ＞ 🎲 ?` · `2016 → 2026` · 노란 ⬇ (관련 동영상 링크 자리를 가리킴) |

- 흐름: ① 핵심 한 문장(경주 중간의 숫자) → ② 대상·티커 설명 → ③ 규칙 → ④ 경주 중간의 사실 → ⑤ 질문(결말) → ⑥ '아래 영상에서 확인하세요'.
- 롱폼과 같은 색 = 같은 계좌 (주식 쇼츠 0-1 5번) — 쇼츠에서 롱폼으로 넘어와도 같은 그림.
- 끝인사("시청해주셔서 감사합니다.")는 넣지 않는다 (`guides/shorts_guide.md` 4번).
- 대본 TXT (내레이션용): [`eonje-maesu-2026-10-shorts.txt`](eonje-maesu-2026-10-shorts.txt)

## 3. 영상 만드는 법 (오디오가 생긴 뒤 — CLAUDE.md '오디오 먼저')

**첫 문장 = 쇼츠 썸네일 그림:** 0초부터 첫 문장이 끝날 때까지 `thumbnails/thumbnail_1.png`(ChatGPT 가 [`thumbnails/thumbnail_1.md`](thumbnails/thumbnail_1.md) 로 만들고 Claude 가 검수해 올림 — 그림 + 첫 문장의 숫자·티커 `64.7%` · `BUY` · `?`)를 화면 가득 (kit.js `K.cover`). 0초 장면 = 앱에서 썸네일로 고를 장면. 그림이 없으면 미리보기는 그림 아이콘 자리(kit.js v1.5 — 언어 없음), 최종 렌더는 멈춘다.

**모양:** 세로 1080×1920 · 롱폼과 같은 짙은 남색 바탕·색 · **자막 없음**(굽지도 올리지도 않음) · 화면 글자는 언어 없이 (`K.init` `noWords` — `render.mjs check` 가 낱말을 잡음) · 음악 없음 · 음량 -14 LUFS.

**화면 자리 (유튜브가 쇼츠 위에 얹는 것을 피함 — `<meta name="video-safe" content="250 150 1500 60">`):**

| 자리 | 세로 위치 | 무엇 |
|---|---|---|
| 위 | 0~250px | 비움 (유튜브 위쪽 아이콘) |
| 가운데 | 250~1500px | 장면 — x 60~930 (오른쪽 150px 은 좋아요·댓글 버튼), 장면 가운데 x 495. 자막 띠가 없어 재테크 쇼츠(1270)보다 아래까지 씀 |
| 아래 | 1500~1920px | 비움 (제목·채널·관련 동영상 링크) — 끝 화면 ⬇ 이 이 링크를 가리킨다 |

**장면 9개:** ① 썸네일 그림(첫 문장) ② SPY·20일 평균·BUY ③ 규칙 ✓/✗ (실제 거래 2개) ④ 64.7% vs 51.8% ⑤ ✓×5 ⑥ ✗×6 ⑦ 신호 10칸 ⑧ 10가지 ＞ 무작위 ? ⑨ 끝 화면 ⬇ — 장면 파일 [`video/episodes/eonje-maesu-2026-10-shorts/index.html`](../../../../video/episodes/eonje-maesu-2026-10-shorts/index.html) v1.0. 장면 시각 = 문장·낱말 시각(손으로 적은 초 없음). 경주는 결말 전에서 멈추고, 오른쪽 '?' 띠가 그 뒤(→ 2026)를 가린다.

**도구:**
1. 내레이션 — `tools/tts_narration.py` 가 롱폼 대본과 함께 `shorts/eonje-maesu-2026-10-shorts.txt` 도 읽어 `shorts/narration.mp3`·`shorts/tts_narration.json` 을 만든다 (영상ID `eonje-maesu-2026-10-shorts`, Kaggle 셀 범위 `stock` 또는 전체 · 진행자 H04 · `voices/ref/host.wav`).
2. 오디오가 오면:
   ```
   cd video && npm run align-audio -- stock eonje-maesu-2026-10-shorts --no-export && cd ..
   node video/render/render.mjs sync  stock eonje-maesu-2026-10-shorts
   node video/render/render.mjs check stock eonje-maesu-2026-10-shorts
   node video/render/render.mjs video stock eonje-maesu-2026-10-shorts
   ```
   → `stock/out/eonje-maesu-2026-10-shorts/final_1080p.mp4` (git 에 넣지 않음). 지금은 추정 시각의 소리 없는 미리보기 `stock/out/eonje-maesu-2026-10-shorts/preview_estimated_silent.mp4` 만 (이 컨테이너에만 — 최종본 아님).
3. 올리기 — 롱폼 공개 뒤. 업로드 도구(`tools/youtube_upload.py`)는 아직 쇼츠 시트를 읽지 않는다 (재테크 쇼츠와 같은 상태 — shorts_insights 7번). 3분 이하 세로 영상은 유튜브가 쇼츠로 본다.

## 4. 설명란 (한국어 — 그대로 복사)

```
20일 평균선을 넘을 때 매수한 SPY, 2021년 12월 성공률은 64.7%였습니다. 같은 때 날짜만 무작위로 매수한 계좌 2천 개의 평균은 51.8%. 그 뒤 2022년 7월까지는 여섯 번 연속 실패했습니다.
▶ RSI·VIX 등 매수 신호 10가지의 10년 결과는 아래 '관련 동영상'에서 — 매수 타이밍, 저점·RSI·신고가 신호는 2% 떨어지기 전 5% 오를 확률이 무작위 매수보다 높을까?

성공 = 매수한 값보다 5% 먼저 오름 · 실패 = 2% 먼저 떨어짐 (종가). 자료·계산 조건은 본편 설명란에 있습니다. 계산 코드는 AI가 짰고, 내레이션은 AI 음성입니다.
과거 자료로 계산한 결과이며 투자 권유가 아닙니다.
#SPY #RSI
```
- 해시태그 2개 `#SPY #RSI` — SPY는 영상 주인공, RSI는 7번 문장의 신호 이름. 3~5개 쇼츠의 성공 비율이 6.6%로 가장 낮다 (shorts_insights 4번) · 태그 자체의 효과는 근거 없음.
- 결말(끝 값·10년 결과)은 쓰지 않는다 (`stock/guides/README.md` 2번). 계산 조건 전체는 롱폼 설명란 '실험 방법·재현 조건'에 있다.

## 5. 올리기 설정

| 항목 | 값 |
|---|---|
| 관련 동영상 | **이 롱폼** (`../youtube.json` 의 영상). API 로는 못 건다 → 사용자가 직접: 컴퓨터 스튜디오 → 콘텐츠 → Shorts → 이 쇼츠의 연필(세부정보) → 오른쪽 '관련 동영상' → 이 롱폼 → 저장 (같은 채널·공개된 영상만). 끝 화면 ⬇ 이 그 링크 자리를 가리킴 |
| 썸네일 | 올린 뒤 **유튜브 앱**에서 쇼츠 수정 → 썸네일 → **0초 장면**(첫 문장 그림) · 파트너 프로그램 가입 뒤: 스튜디오에서 `thumbnails/thumbnail_1.png` |
| 올리는 때 | 롱폼 공개 뒤, **월·목 15~17시** 하나씩 (네 편을 한꺼번에 올리지 않음 — 약한 기울기, shorts_insights 6번) |
| 기본 언어 | ko |
| 자막 올리기 | **아니요** (전 세계 대상 — 사용자 지시 2026-10-15) |
| 자동 더빙 | 스튜디오에서 지원 언어가 보이면 켠다 |
| 변경되거나 합성된 콘텐츠 | **예** (내레이션이 AI 음성 — CLAUDE.md) |
| 카테고리 | 교육 |
| 공개 범위 | 롱폼과 같은 방식 (비공개 업로드 → 예약 공개) |
| 고정 댓글 | 쓰려면 질문 하나: "매수 신호 하나만 고른다면 어떤 걸 쓰시나요? 10가지 결과는 본편에서 확인하세요." — 근거 없음, 시험 |

## 6. 숫자 근거 (쇼츠 대본의 숫자 → 롱폼 대본 문장)

롱폼 숫자는 `backtest/check_numbers.py` 가 결과 파일로 맞춰 봤다. 같은 숫자가 여러 문장에 있으면 첫 문장만 적음 (전부는 `checklist.md`).

| 쇼츠 문장 | 숫자 | 롱폼 문장 | 롱폼 대본 |
|---:|---|---|---|
| 1 | `20일` | s20 | 두 번째, 20일 신고가 돌파 매수입니다. |
| 1 | `2021년` | s12 | 2021년 말에는 성공률 56.1%로, 무작위 평균 51.7%보다 높았습니다. |
| 1 | `12월` | s38 | 2021년 12월에는 성공률 64.7%로, 무작위 평균 51.8%보다 크게 앞섰습니다. |
| 1 | `64.7%` | s38 | 2021년 12월에는 성공률 64.7%로, 무작위 평균 51.8%보다 크게 앞섰습니다. |
| 2 | `500` | s3 | 2016년부터, S&P 500을 따라가는 ETF인 SPY로 백테스트해 보겠습니다. |
| 2 | `2016년` | s3 | 2016년부터, S&P 500을 따라가는 ETF인 SPY로 백테스트해 보겠습니다. |
| 3 | `5%` | s4 | 성공은 매수한 값보다 5% 오르는 것, 그 전에 2% 떨어지면 실패예요. |
| 3 | `2%` | s4 | 성공은 매수한 값보다 5% 오르는 것, 그 전에 2% 떨어지면 실패예요. |
| 4 | `2천` | s6 | 비교 상대는 날짜만 무작위로 매수한 계좌 2천 개예요. |
| 4 | `51.8%` | s38 | 2021년 12월에는 성공률 64.7%로, 무작위 평균 51.8%보다 크게 앞섰습니다. |
| 5 | `2016년` | s3 | 2016년부터, S&P 500을 따라가는 ETF인 SPY로 백테스트해 보겠습니다. |
| 5 | `7월` | s37 | 2016년 7월부터 2018년 1월까지 다섯 번 연속 성공했어요. |
| 5 | `2018년` | s37 | 2016년 7월부터 2018년 1월까지 다섯 번 연속 성공했어요. |
| 5 | `1월` | s37 | 2016년 7월부터 2018년 1월까지 다섯 번 연속 성공했어요. |
| 6 | `2021년` | s12 | 2021년 말에는 성공률 56.1%로, 무작위 평균 51.7%보다 높았습니다. |
| 6 | `12월` | s38 | 2021년 12월에는 성공률 64.7%로, 무작위 평균 51.8%보다 크게 앞섰습니다. |
| 6 | `2022년` | s13 | 그런데 2022년에는 판정 12번 중 11번이 실패였어요. |
| 6 | `7월` | s37 | 2016년 7월부터 2018년 1월까지 다섯 번 연속 성공했어요. |
| 7 | `10가지` | s2 | 많이 쓰는 매수 신호 10가지가 정말 성공 확률을 높일까요? |
| 8 | `10년` | s110 | 이번 10년이 특별했을 수도 있어서, 기간을 1994년부터 2015년으로 바꿔 봤어요. |
| 9 | `10가지` | s2 | 많이 쓰는 매수 신호 10가지가 정말 성공 확률을 높일까요? |

## 7. 주의 — 근거와 다른 점 (사용자 지시로 고름)

- 주식 쇼츠 근거의 경주 쇼츠(디히치 ×32~×203)는 **끝 결과까지 보여 준다.** 이 쇼츠는 채널 규칙(결말을 말하지 않음 — `stock/guides/README.md` 2·3번)과 프롤로그형(`guides/shorts_guide.md` 4번)에 따라 **결과를 롱폼에 둔다.** 결말을 가린 효과는 근거 없음 — 올린 뒤 '본편 공개' 불만 댓글 수·관련 동영상 클릭 수로 본다 (shorts_insights 8번).
- 대본(자막·음성인식)이 있는 성공 쇼츠가 0개라 첫 3초·말 속도·끝 문장은 근거 없음 — 롱폼 말투를 그대로 썼다.
- 언어 없는 화면이 해외에서 통하는지는 올린 뒤 시청자 지리로 본다.

## 8. 다음에 할 일

1. 사용자가 소리 없는 미리보기를 보고 장면을 확인 → 썸네일 그림(ChatGPT — `stock/thumbnails_chatgpt.md`) → Claude 검수·업로드.
2. Kaggle 셀(범위 `stock`)로 내레이션 → 3번 '도구' 2 (맞춤·sync·check·video) → 롱폼 공개 뒤 올리기 → 5번 관련 동영상을 사용자가 건다.

## 변경 이력

| 버전 | 날짜 | 내용 |
|---|---|---|
| v1.0.1 | 2026-10-17 | 쇼츠 썸네일 글자 `64.7%` · `BUY` · `?` (사용자 지시 — 영어·숫자·기호 써도 됨) |
| v1.0 | 2026-10-17 | 새로 만듦 — 대본 9문장 284음절 예상 약 48.6초 · 제목 R1 「매수 타이밍 20일선, 한때 성공률 64.7%… 무작위 매수보다 높을까?」 · 9개 언어 제목·설명 · 언어 없는 세로 장면 v1.0 · 숫자 근거 21개 (없음 0) |
