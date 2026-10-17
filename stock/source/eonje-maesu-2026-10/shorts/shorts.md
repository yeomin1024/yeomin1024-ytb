# 쇼츠 — `eonje-maesu-2026-10` 결과를 바로 보여 주는 쇼츠 (왜 → 어떻게 → 비교 상대 → 조건 → 결과 → 왜? → 롱폼 · 언어 없는 화면)

버전: v2.1 — 2026-10-17 — **결과형 + 왜·어떻게** (2번 커버드콜 쇼츠 v2.1 과 같은 꼴 — 사용자 지시 2026-10-17 "R1으로 하고 나머지 3개도 수정하고 외국어 자막 대본도 필요하지? 쇼츠, 롱폼 각각 언어별로 작성해봐" · 그 앞 "그래 왜 그런 테스트 했는지 언급을 해줘야 할 거 아니야 … 파이썬 코드로 테스트를 해봤습니다 이렇게 무슨 방법으로 테스트했는지도 말해야지 … 니가 아무것도 모르는 시청자 입장이 되보라고"): 대본 12문장 — 왜(시험할 말) → 어떻게(AI가 짠 파이썬 코드 · 과거 실제 가격 · 백테스트 — 화면에 코드 카드) → 비교 상대와 까닭 → 조건 → 결과 → 왜? → 롱폼에만 있는 것. 제목 R1·R2 = 시험할 말(2줄). 9개 언어 제목·설명 다시 · 언어별 자막 대본 `subs/` (화면에 굽지 않고 CC 로 올림).
(v1.0.5 까지 — 프롤로그형(첫 문장 2021년 12월 64.7% → ✓×5 → ✗×6 → 10가지 ＞ 무작위 ? → '결과는 아래 영상') — 결말 가림, 커밋 9b8be2b5.)

- 보내는 곳(롱폼): **매수 타이밍, 저점·RSI·신고가 신호는 2% 떨어지기 전 5% 오를 확률이 무작위 매수보다 높을까?** (`../upload.md` 1번 제목) — 쇼츠의 '관련 동영상'으로 연결 (롱폼 공개 뒤)
- **쇼츠에서 말하는 것:** (왜) 매수 신호를 따르면 성공 확률이 높아진다는 말을 확인하려고 · (어떻게) AI가 짠 파이썬 코드에 과거 실제 가격을 넣은 백테스트, S&P 500을 따라가는 SPY로 2016년부터, 매수 신호 10가지, 5% 먼저 오르면 성공·2% 먼저 떨어지면 실패, 비교 상대 = 날짜만 무작위로 매수한 계좌 2천 개(신호가 쓸모 있다면 무작위보다 성공률이 높아야 하니까), 무작위도 같은 기준 · (결과) 가장 높은 20일 평균선 매수 성공률 52.1% · 10가지 모두 무작위 매수와 차이가 없는 범위.
- **롱폼에만 남기는 것 (더 보고 싶은 사람에게):** 신호마다의 기록(2021년 12월 64.7% · 다섯 번 연속 성공 · 여섯 번 연속 실패 · 2022년 실패) · 무작위 90% 범위 숫자 · 실패 기준 1%·1.5% · 기간 1994~2015 · 한계. 쇼츠 끝 문장이 '10가지 신호의 기록과, 기간을 바꿔도 같은지는'을 부르고 끝 화면이 그림 둘(신호 아이콘 10 · 달력 ↔)로 보여 준다.
- 근거: [`stock/guides/shorts_insights.md`](../../../guides/shorts_insights.md) v1.1 (주식 성공 경주 쇼츠는 끝 결과까지 보여 줌 — 결과형과 같은 방향) · 꼴 `stock/guides/README.md` v1.24 7번
- 길이: **12문장 · 예상 약 58.4초** (`render.mjs sync --estimate` — 진행자 H04 실측으로 맞춘 추정) · 결과 첫 숫자 약 40초 · 50자 넘는 문장 없음 · 45~59초 = 비교 집단에서 가장 높은 구간 (shorts_insights 2번)
- 목소리: 진행자 H04 하나 (CLAUDE.md) — 한국어 내레이션, **화면은 소리 없이도 이해되게** · 외국어는 언어별 자막(CC — `subs/<영상ID>-shorts.<언어>.txt` → 오디오 뒤 `tools/subs_tool.py build` 로 SRT) + 자동 더빙
- 숫자: 쇼츠 대본의 숫자는 모두 롱폼 대본에 있다 — `python3 tools/backtest/shorts_numcheck.py stock eonje-maesu-2026-10` → [`checklist.md`](checklist.md) (숫자 11개 · 없음 0). 화면 숫자는 그 롱폼의 `backtest/` anim 자료에서만 — 장면 파일이 대본 숫자와 맞춰 보고 다르면 멈춘다.
- ※ 연구·교육용 — 투자 권유가 아님

## 1. 제목

| | 제목 (한국어 — 기본 언어) | 2줄 (`title_fit.py --shorts`) | 까닭 |
|---|---|---|---|
| **R1 (추천)** | **매수 신호 10가지, 무작위 매수보다 성공률 높을까?** | ✅ 홈 Shorts 칸·재생 화면·PC 다음 동영상 | 쇼츠가 시험하는 말 그대로 · 맨 앞 핵심 낱말 · 질문 (결과는 영상 안에서) |
| R2 | 매수 타이밍, 신호 따르면 무작위보다 잘 맞을까? | ✅ | 같은 질문을 다르게 |

- 제목은 결과를 말하지 않는다 (테스트로 호기심 — 사용자 지시). 결과는 영상 40초부터.

### 1-1. 언어별 제목·설명 (localizations — 롱폼 `upload.md` 5번과 같은 9개 언어)

JSON — 업로드 도구가 읽는 꼴. 설명 = 한국어 설명란(4번)과 같은 뜻 (왜 → 어떻게 → 결과, '▶' 줄 = 롱폼에만 있는 것 + 그 언어의 롱폼 제목). 해시태그는 티커. 숫자 표기는 그 언어 관습.

```
{
 "en": {
  "title": "10 buy signals: do they beat random buying on success rate?",
  "description": "People say following buy signals raises your odds of success. To check, we ran a backtest with AI-written Python code on real past prices. Using SPY, an ETF that tracks the S&P 500, from 2016, we tested 10 buy signals such as the 20-day average, RSI and the fear index VIX. Rising 5% above the buy price first counted as success and falling 2% first as failure; 2,000 accounts that bought only on random dates were judged by the same rule. The best was buying when the price crosses above the 20-day average, with a 52.1% success rate, but all 10 were in a range no different from random buying.\n▶ The 10 signals' records — and whether a different period gives the same result — in the related video below: When to buy: do dip, RSI and breakout signals hit +5% before −2% more often than random buys?\n\nData and full conditions (judged on closing prices, sold the day after each verdict, 0.25% fee) are in the main video's description. The code was written by AI and the narration is an AI voice.\nPast data only — not investment advice.\n#SPY #RSI"
 },
 "hi": {
  "title": "10 खरीद संकेत: क्या रैंडम खरीद से ज़्यादा सफलता दर देते हैं?",
  "description": "कहा जाता है कि खरीद संकेत मानने से सफलता की संभावना बढ़ती है। यह जाँचने के लिए हमने AI के लिखे Python कोड से पिछली असली कीमतों पर बैकटेस्ट किया। S&P 500 को फॉलो करने वाले ETF, SPY पर 2016 से 20 दिन की औसत रेखा, RSI और डर सूचकांक VIX जैसे 10 खरीद संकेत परखे। खरीद भाव से पहले 5% बढ़ना सफलता और पहले 2% गिरना असफलता गिना गया; सिर्फ़ रैंडम तारीखों पर खरीदने वाले 2,000 खातों को भी उसी नियम से परखा। सबसे ऊपर रहा 20 दिन की औसत रेखा पार होने पर खरीद, सफलता दर 52.1%, लेकिन सभी 10 संकेत रैंडम खरीद से अलग न होने वाले दायरे में रहे।\n▶ 10 संकेतों का रिकॉर्ड, और अवधि बदलने पर भी नतीजा वही रहता है या नहीं — नीचे जुड़े वीडियो में: कब खरीदें: क्या डिप, RSI और ब्रेकआउट संकेत रैंडम खरीद से ज़्यादा बार −2% से पहले +5% छूते हैं?\n\nडेटा और पूरी शर्तें (बंद भाव पर फ़ैसला, फ़ैसले के अगले दिन बिक्री, 0.25% शुल्क) मुख्य वीडियो के विवरण में हैं। कोड AI ने लिखा और आवाज़ AI की है।\nसिर्फ़ पिछला डेटा — निवेश सलाह नहीं।\n#SPY #RSI"
 },
 "id": {
  "title": "10 sinyal beli: tingkat berhasilnya lebih tinggi dari beli acak?",
  "description": "Katanya mengikuti sinyal beli menaikkan peluang berhasil. Untuk mengeceknya, kami melakukan backtest dengan kode Python buatan AI pada harga riil masa lalu. Dengan SPY, ETF yang mengikuti S&P 500, sejak 2016 kami menguji 10 sinyal beli seperti rata-rata 20 hari, RSI, dan indeks ketakutan VIX. Naik 5% di atas harga beli lebih dulu dihitung berhasil, turun 2% lebih dulu dihitung gagal; 2.000 akun yang hanya tanggal belinya acak juga dinilai dengan aturan yang sama. Tertinggi adalah beli saat harga menembus rata-rata 20 hari, dengan tingkat berhasil 52,1%, tapi ke-10 sinyal masih dalam rentang yang tak beda dari beli acak.\n▶ Catatan 10 sinyal itu, dan apakah hasilnya sama di periode lain — di video tertaut di bawah: Kapan beli: sinyal dip, RSI, breakout lebih sering naik 5% sebelum turun 2% dibanding beli acak?\n\nData dan syarat lengkap (dinilai dari harga penutupan, dijual sehari setelah penilaian, biaya 0,25%) ada di deskripsi video utama. Kode ditulis AI dan narasinya suara AI.\nHanya data masa lalu — bukan saran investasi.\n#SPY #RSI"
 },
 "pt": {
  "title": "10 sinais de compra: acertam mais que comprar ao acaso?",
  "description": "Dizem que seguir sinais de compra aumenta a chance de acerto. Para conferir, fizemos um backtest com código Python escrito por IA sobre preços reais do passado. Com o SPY, ETF que segue o S&P 500, a partir de 2016, testamos 10 sinais de compra, como a média de 20 dias, o RSI e o índice do medo VIX. Subir 5% acima do preço de compra primeiro contou como acerto e cair 2% primeiro, como erro; 2.000 contas que compraram só em datas aleatórias foram julgadas pelo mesmo critério. O melhor foi comprar ao cruzar a média de 20 dias para cima, com 52,1% de acerto, mas os 10 ficaram numa faixa sem diferença das compras aleatórias.\n▶ O histórico dos 10 sinais, e se o resultado é o mesmo em outro período — no vídeo vinculado abaixo: Quando comprar: queda, RSI e rompimento sobem 5% antes de cair 2% mais que compras aleatórias?\n\nDados e condições completas (julgamento pelo fechamento, venda no dia seguinte ao resultado, taxa de 0,25%) na descrição do vídeo principal. O código foi escrito por IA e a narração é voz de IA.\nApenas dados passados — não é recomendação de investimento.\n#SPY #RSI"
 },
 "es-419": {
  "title": "10 señales de compra: ¿aciertan más que comprar al azar?",
  "description": "Dicen que seguir señales de compra sube la probabilidad de acertar. Para comprobarlo, hicimos un backtest con código Python escrito por IA sobre precios reales del pasado. Con SPY, un ETF que sigue el S&P 500, desde 2016 probamos 10 señales de compra, como la media de 20 días, el RSI y el índice del miedo VIX. Subir 5% sobre el precio de compra primero contó como acierto y caer 2% primero, como fallo; 2,000 cuentas que compraron solo en fechas al azar se juzgaron con el mismo criterio. La mejor fue comprar al cruzar hacia arriba la media de 20 días, con 52.1% de aciertos, pero las 10 quedaron en un rango sin diferencia con comprar al azar.\n▶ El historial de las 10 señales, y si el resultado es el mismo en otro periodo — en el video vinculado abajo: ¿Cuándo comprar? ¿Caída, RSI y ruptura suben 5% antes de caer 2% más seguido que comprar al azar?\n\nDatos y condiciones completas (juicio con el precio de cierre, venta al día siguiente del resultado, comisión de 0.25%) en la descripción del video principal. El código lo escribió una IA y la narración es una voz de IA.\nSolo datos pasados — no es asesoría de inversión.\n#SPY #RSI"
 },
 "ja": {
  "title": "買いシグナル10個、ランダムに買うより成功率は高い？",
  "description": "買いシグナルに従えば成功の確率が上がると言われます。本当かどうか、AIが書いたPythonコードで過去の実際の価格を使ってバックテストしました。S&P 500に連動するETF・SPYで2016年から、20日平均線・RSI・恐怖指数VIXなど買いシグナル10個を試しました。買値より先に5%上がれば成功、先に2%下がれば失敗と数え、日付だけランダムに買った口座2,000個も同じ基準で判定しました。最も高かったのは20日平均線を超えたときの買いで成功率52.1%でしたが、10個とも、ランダムな買いと差がない範囲でした。\n▶ 10個のシグナルの記録と、期間を変えても同じかどうかは下のリンクの動画で — 買うタイミング：押し目・RSI・高値更新のシグナルは、ランダムに買うより−2%の前に+5%に届く確率が高い？\n\nデータと計算条件（終値で判定・判定の翌日に売却・手数料0.25%）は本編の説明欄にあります。計算コードはAIが書き、ナレーションはAI音声です。\n過去データによる計算で、投資の勧誘ではありません。\n#SPY #RSI"
 },
 "de": {
  "title": "10 Kaufsignale: höhere Erfolgsquote als zufällige Käufe?",
  "description": "Es heißt, wer Kaufsignalen folgt, erhöht seine Erfolgschance. Zur Prüfung haben wir mit von KI geschriebenem Python-Code einen Backtest auf echten historischen Kursen gemacht. Mit SPY, einem ETF auf den S&P 500, haben wir 10 Kaufsignale ab 2016 getestet, etwa den 20-Tage-Schnitt, RSI und den Angstindex VIX. Zuerst 5 % über dem Kaufkurs zählte als Erfolg, zuerst 2 % darunter als Misserfolg; 2.000 Konten, die nur an zufälligen Tagen kauften, wurden nach derselben Regel bewertet. Am besten war Kaufen beim Überschreiten des 20-Tage-Schnitts mit 52,1 % Erfolgsquote, doch alle 10 lagen in einem Bereich ohne Unterschied zum Zufallskauf.\n▶ Die Bilanz der 10 Signale – und ob ein anderer Zeitraum zum gleichen Ergebnis führt – im verlinkten Video unten: Wann kaufen: Erreichen Dip-, RSI- und Ausbruchssignale öfter +5 % vor −2 % als zufällige Käufe?\n\nDaten und alle Bedingungen (Bewertung zum Schlusskurs, Verkauf am Tag nach dem Ergebnis, 0,25 % Gebühr) in der Beschreibung des Hauptvideos. Der Code wurde von einer KI geschrieben, die Stimme ist eine KI-Stimme.\nNur historische Daten – keine Anlageberatung.\n#SPY #RSI"
 },
 "vi": {
  "title": "10 tín hiệu mua: tỷ lệ thành công có cao hơn mua ngẫu nhiên?",
  "description": "Người ta nói theo tín hiệu mua sẽ tăng xác suất thành công. Để kiểm tra, chúng tôi chạy backtest bằng mã Python do AI viết trên giá thực tế trong quá khứ. Với SPY, ETF bám theo S&P 500, từ năm 2016, chúng tôi thử 10 tín hiệu mua như đường trung bình 20 ngày, RSI và chỉ số sợ hãi VIX. Tăng 5% so với giá mua trước thì là thành công, giảm 2% trước là thất bại; 2.000 tài khoản chỉ mua vào ngày ngẫu nhiên cũng được chấm theo cùng tiêu chí. Cao nhất là mua khi giá vượt đường trung bình 20 ngày, tỷ lệ thành công 52,1%, nhưng cả 10 đều nằm trong vùng không khác gì mua ngẫu nhiên.\n▶ Kết quả của 10 tín hiệu, và đổi giai đoạn thì có giống không — xem ở video liên kết bên dưới: Khi nào mua: tín hiệu giảm sâu, RSI, phá đỉnh có lên 5% trước khi xuống 2% nhiều hơn mua ngẫu nhiên?\n\nDữ liệu và điều kiện đầy đủ (chấm theo giá đóng cửa, bán vào ngày sau khi có kết quả, phí 0,25%) trong phần mô tả video chính. Mã do AI viết, lời thuyết minh là giọng AI.\nChỉ là dữ liệu quá khứ — không phải lời khuyên đầu tư.\n#SPY #RSI"
 },
 "tr": {
  "title": "10 alım sinyali, rastgele alımdan daha yüksek başarı oranı verir mi?",
  "description": "Alım sinyallerine uymanın başarı şansını artırdığı söylenir. Bunu kontrol etmek için yapay zekânın yazdığı Python koduyla geçmişteki gerçek fiyatlar üzerinde backtest yaptık. S&P 500'ü izleyen ETF SPY ile 2016'dan itibaren 20 günlük ortalama, RSI ve korku endeksi VIX gibi 10 alım sinyalini test ettik. Alış fiyatından önce %5 çıkmak başarı, önce %2 düşmek başarısızlık sayıldı; yalnızca rastgele tarihlerde alan 2.000 hesap da aynı kuralla değerlendirildi. En yükseği 20 günlük ortalamayı aşınca alımdı, başarı oranı %52,1; ama 10 sinyalin hepsi rastgele alımdan farksız bir aralıktaydı.\n▶ 10 sinyalin kaydı ve dönem değişince sonucun aynı olup olmadığı aşağıdaki bağlantılı videoda: Ne zaman almalı: düşüş, RSI ve kırılım sinyali, rastgele alımdan sık mı %2 düşmeden %5 çıkar?\n\nVeriler ve tüm koşullar (kapanış fiyatıyla değerlendirme, sonucun ertesi günü satış, %0,25 komisyon) ana videonun açıklamasında. Kodu yapay zekâ yazdı, seslendirme yapay zekâ sesi.\nYalnızca geçmiş veriler — yatırım tavsiyesi değildir.\n#SPY #RSI"
 }
}
```

## 2. 대본 (시각은 예상 — 내레이션 뒤 실제 시각으로 맞춤)

| # | 시각 | 대본 | 역할 | 화면 (언어 없음 — 숫자·$·%·×·연도·티커·기호·아이콘) |
|---|---|---|---|---|
| 1 | 0:00 | 언제 매수할지 고민될 때, 매수 신호를 따르면 성공 확률이 높아진다고들 하죠. | **왜** — 시험할 말 | **쇼츠 썸네일 그림** (`WHEN TO BUY ?` · `SPY` — 초록 선이 노란 평균선을 막 뚫고 위는 안개, 버튼 위 손가락) |
| 2 | 0:05 | 정말 그런지, AI가 짠 파이썬 코드로 과거 실제 가격을 넣어 백테스트해 봤습니다. | **어떻게** | 흰 가격 선 + **코드 카드** `entry.py` (`tools/backtest/entry.py` `barrier_table()` 을 줄인 줄 — `up = p[b] * (1 + n)` · `dn = p[b] * (1 - m)` · `res[b] = 1 if ju < jd else 0`) |
| 3 | 0:11 | 시험한 건 S&P 500을 따라가는 ETF인 SPY, 2016년부터예요. | 시험한 것 | `SPY = S&P 500` · 2016 → 2026 SPY 종가(흰 선) · 📅 `2016 →` |
| 4 | 0:17 | 20일 평균선, RSI, 공포지수 VIX 같은 매수 신호 10가지를 넣었어요. | 신호 10가지 | `10 × BUY` · 신호 10칸 (아이콘 + `20` · `RSI < 40` · `VIX ≥ 20` …) — 말하는 신호(20일 평균선·RSI·VIX)를 노랗게 |
| 5 | 0:23 | 매수한 값보다 5% 먼저 오르면 성공, 2% 먼저 떨어지면 실패로 셌어요. | 판정 기준 | 실제 거래 둘: 2016.07 매수 → `+5%` 먼저 ✓ · 2021.12 매수 → `−2%` 먼저 ✗ |
| 6 | 0:29 | 비교 상대는 날짜만 무작위로 매수한 계좌 2천 개예요. | 비교 상대 | 🎲 `× 2,000` · 2016 → 2026 줄 위에 무작위 매수 날 ▲ |
| 7 | 0:32 | 신호가 쓸모 있다면, 무작위보다 성공률이 높아야 하니까요. | 비교 상대를 고른 까닭 | 카드 둘: 신호(20 BUY) `%` ＞ 🎲 `%` · 노란 `?` |
| 8 | 0:36 | 무작위 계좌도 똑같은 기준으로 판정했어요. | 공정한 조건 | 두 카드 아래 `+5%` `−2%` 칩 · 가운데 `=` |
| 9 | 0:40 | 가장 높은 건 20일 평균선을 넘을 때 매수로, 성공률 52.1%였어요. | **결과 ①** | 10가지 성공률(점) · 무작위 90% 범위(회색 띠) · 성공률 순 · 20일 평균선 점이 노랗게 + 칩 `52.1%` |
| 10 | 0:45 | 하지만 10가지 모두, 무작위 매수와 차이가 없는 범위였어요. | **결과 ②** | 띠가 모두 깜빡 · `BUY = 🎲` |
| 11 | 0:49 | 그럼 신호마다 언제 맞고, 언제 틀렸을까요? | 호기심 | 20 BUY · ✓×5 → ✗×6 · 큰 `?` (롱폼에 있는 기록 — 그림만) |
| 12 | 0:52 | 10가지 신호의 기록과, 기간을 바꿔도 같은지는 아래 영상에서 확인하세요. | 롱폼 안내 | 끝 화면: 신호 아이콘 10 · 달력 ↔ 달력 `?` · 노란 ⬇ |

- **아무것도 모르는 시청자가 '뭐야? 왜 이렇게 했고 어떻게 했다는 거야?'라고 묻지 않게** — 왜·어떻게·비교 상대와 까닭·공정한 조건은 빼지 않는다 (`stock/guides/README.md` 7번 · `guides/script_guide.md` 피드백 21).
- 롱폼과 같은 색 = 같은 계좌. 끝인사("시청해주셔서 감사합니다.")는 넣지 않는다 (`guides/shorts_guide.md` 4번).
- 대본 TXT (내레이션용): [`eonje-maesu-2026-10-shorts.txt`](eonje-maesu-2026-10-shorts.txt) · 언어별 자막 대본: [`subs/`](subs/) (`python3 tools/subs_tool.py check stock eonje-maesu-2026-10-shorts`)

## 3. 영상 만드는 법 (오디오가 생긴 뒤 — CLAUDE.md '오디오 먼저')

**첫 문장 = 쇼츠 썸네일 그림:** 0초부터 첫 문장(시험할 말)이 끝날 때까지 `thumbnails/thumbnail_1.png` (ChatGPT 가 [`thumbnails/thumbnail_1.md`](thumbnails/thumbnail_1.md) 로 만들고 Claude 가 검수 — 글자 `WHEN TO BUY ?` · `SPY`)를 화면 가득 (kit.js `K.cover`). 빈 띠가 있으면 `tools/cover_check.py` 로 재고 `K.cover(…, { box })`.

**모양:** 세로 1080×1920 · 롱폼과 같은 짙은 남색 바탕·색 · **화면에 자막을 굽지 않음** (언어별 자막은 CC 로 올림) · 화면 글자는 언어 없이 (`K.init` `noWords`) · 음악 없음 · 음량 -14 LUFS.

**화면 자리 — 가운데·크게** (`guides/video_guide.md` v4.13 6번, `<meta name="video-safe" content="150 60 1320 60">`): 장면 파일 v2.1 은 화면 좌표를 바로 씀 (가운데 x 540), 글자·그림 y 160~1316, 아래 1320~1920 은 비움 (제목·관련 동영상 링크 — 끝 화면 ⬇ 이 가리킴).

**장면:** 2번 표 — 장면 파일 [`video/episodes/eonje-maesu-2026-10-shorts/index.html`](../../../../video/episodes/eonje-maesu-2026-10-shorts/index.html) v2.1 (check 문제 0 · 완성 mp4 장면을 직접 봄). 장면 시각 = 문장·낱말 시각(손으로 적은 초 없음).

**도구:**
1. 내레이션 — Kaggle 셀 범위 `stock` (영상ID `eonje-maesu-2026-10-shorts` — `shorts/narration.mp3`·`shorts/tts_narration.json`).
2. 오디오가 오면:
   ```
   cd video && npm run align-audio -- stock eonje-maesu-2026-10-shorts --no-export && cd ..
   node video/render/render.mjs sync  stock eonje-maesu-2026-10-shorts
   node video/render/render.mjs check stock eonje-maesu-2026-10-shorts
   node video/render/render.mjs video stock eonje-maesu-2026-10-shorts
   python3 tools/subs_tool.py build stock eonje-maesu-2026-10-shorts        # 언어별 SRT (오디오 시각) → shorts/subs/
   ```
   → `stock/out/eonje-maesu-2026-10-shorts/final_1080p.mp4` (git 밖) → **완성 mp4 장면을 Claude 가 직접 본다**. 지금은 추정 시각의 소리 없는 미리보기 `stock/out/eonje-maesu-2026-10-shorts/preview_estimated_silent.mp4` 만.
3. 올리기 — `tools/youtube_upload.py` v1.12 가 쇼츠 시트 `shorts/upload.md`(아직 없음 — 다음 할 일)를 읽고 한국어 + 언어별 자막(CC)을 올림. 자막 하나 400단위 — 할당량이 모자라면 `--captions-only` 로 다음 날. 롱폼과 같은 시각에 공개 (`guides/upload_guide.md` 12번).

## 4. 설명란 (한국어 — 그대로 복사)

```
매수 신호를 따르면 성공 확률이 높아진다고들 하죠. 정말 그런지 AI가 짠 파이썬 코드로 과거 실제 가격을 넣어 백테스트했습니다. S&P 500을 따라가는 ETF인 SPY로 2016년부터, 20일 평균선·RSI·공포지수 VIX 같은 매수 신호 10가지를 시험했어요. 매수한 값보다 5% 먼저 오르면 성공, 2% 먼저 떨어지면 실패로 셌고, 날짜만 무작위로 매수한 계좌 2천 개도 똑같은 기준으로 판정했습니다. 가장 높은 건 20일 평균선을 넘을 때 매수로 성공률 52.1%였지만, 10가지 모두 무작위 매수와 차이가 없는 범위였어요.
▶ 10가지 신호의 기록과, 기간을 바꿔도 같은지는 아래 '관련 동영상'에서 — 매수 타이밍, 저점·RSI·신고가 신호는 2% 떨어지기 전 5% 오를 확률이 무작위 매수보다 높을까?

자료·계산 조건(종가로 판정, 판정 다음 날 매도, 수수료 0.25%)은 본편 설명란에 있습니다. 계산 코드는 AI가 짰고, 내레이션은 AI 음성입니다.
과거 자료로 계산한 결과이며 투자 권유가 아닙니다.
#SPY #RSI
```
- 해시태그 2개 `#SPY #RSI` (shorts_insights 4번 — 3~5개가 가장 낮음).
- 왜·어떻게·결과는 쓰고(영상과 같음), **롱폼에만 있는 것은 쓰지 않는다** — 롱폼으로 가는 까닭.

## 5. 올리기 설정

| 항목 | 값 |
|---|---|
| 관련 동영상 | **이 롱폼** (`../youtube.json`). API 로는 못 건다 → 사용자가 스튜디오 → 콘텐츠 → Shorts → 이 쇼츠 세부정보 → '관련 동영상' |
| 썸네일 | `youtube_upload.py` 가 세로 720×1280 으로 올림 (빈 띠 그림이면 완성 영상 0초 장면) |
| 올리는 때 | 롱폼과 **같은 시각에 공개** (`guides/upload_guide.md` 12번) |
| 기본 언어 | ko |
| 자막 올리기 | **언어별** (한국어 + en·hi·id·pt·es-419·ja·de·vi·tr — 화면에 굽지 않고 CC, 사용자 지시 2026-10-17) |
| 자동 더빙 | 스튜디오에서 지원 언어가 보이면 켠다 |
| 변경되거나 합성된 콘텐츠 | **예** (내레이션이 AI 음성 — CLAUDE.md) |
| 카테고리 | 교육 |
| 공개 범위 | 롱폼과 같은 방식 (비공개 업로드 → 예약 공개) |

## 6. 숫자 근거 (쇼츠 대본의 숫자 → 롱폼 대본 문장)

롱폼 숫자는 `backtest/check_numbers.py` 가 결과 파일로 맞춰 봤다 (전부는 `checklist.md`).

| 쇼츠 문장 | 숫자 | 롱폼 문장 | 롱폼 대본 |
|---:|---|---|---|
| 3 | `500` · `2016년` | s3 | 2016년부터, S&P 500을 따라가는 ETF인 SPY로 백테스트해 보겠습니다. |
| 4 | `10가지` | s2 | 많이 쓰는 매수 신호 10가지가 정말 성공 확률을 높일까요? |
| 4 | `20일` | s20 | 두 번째, 20일 신고가 돌파 매수입니다. |
| 5 | `5%` · `2%` | s4 | 성공은 매수한 값보다 5% 오르는 것, 그 전에 2% 떨어지면 실패예요. |
| 6 | `2천` | s6 | 비교 상대는 날짜만 무작위로 매수한 계좌 2천 개예요. |
| 9 | `20일` | s20 | 두 번째, 20일 신고가 돌파 매수입니다. |
| 9 | `52.1%` | s41 | 결과는 판정 71번 중 37번 성공, 52.1%로, 지금까지 본 네 가지 중 가장 높아요. |
| 10 | `10가지` | s2 | 많이 쓰는 매수 신호 10가지가 정말 성공 확률을 높일까요? |
| 12 | `10가지` | s2 | 많이 쓰는 매수 신호 10가지가 정말 성공 확률을 높일까요? |

## 7. 주의 — 근거와 다른 점·한계

- **결과를 쇼츠에서 말한다** (사용자 지시) — 롱폼으로 넘어오는지는 근거 없음 → 올린 뒤 '관련 동영상' 클릭 수·롱폼 트래픽 소스 'Shorts 피드' (shorts_insights 8번).
- 쇼츠의 결과는 한 가지 시작 날·한 가지 조건의 결과다 — 다른 조건·시작 시점은 롱폼에 (설명란 '▶' 줄).
- 대본이 있는 성공 쇼츠가 0개라 첫 3초·말 속도는 근거 없음. 언어 없는 화면 + 언어별 자막이 해외에서 통하는지는 올린 뒤 시청자 지리·자막 언어로 본다.

## 8. 다음에 할 일

1. 사용자가 소리 없는 미리보기를 확인 → 썸네일 그림(ChatGPT — `stock/thumbnails_chatgpt.md`) → Claude 검수·업로드.
2. 쇼츠 업로드 시트 `shorts/upload.md` (업로드 도구 v1.12 꼴 — 자막 올리기 '언어별').
3. Kaggle 내레이션(범위 `stock`) → 3번 '도구' 2 → 롱폼과 같은 시각에 올리기 → 관련 동영상을 사용자가 건다.

## 변경 이력

| 버전 | 날짜 | 내용 |
|---|---|---|
| v2.1 | 2026-10-17 | 결과형 + 왜·어떻게 — 대본 12문장 예상 약 58.4초 · 제목 R1 「매수 신호 10가지, 무작위 매수보다 성공률 높을까?」 · 9개 언어 제목·설명 · 언어별 자막 대본 · 장면 v2.1 (가운데·크게, 코드 카드, 경주 끝까지) · 썸네일 글자 `WHEN TO BUY ?` · `SPY`만 · 숫자 11개 없음 0 (사용자 지시) |
|---|---|---|
| v1.0.5 | 2026-10-17 | 쇼츠 썸네일 글자 `WHEN TO BUY ?` · `SPY` — 시청자 니즈·티커 (사용자 지시) |
| v1.0.4 | 2026-10-17 | 쇼츠 썸네일 글자 (그림)화살표 `>` (그림)주사위 `?` — 큰 부등호 머리글 (사용자 지시) |
| v1.0.3 | 2026-10-17 | 쇼츠 썸네일 글자 `vs` · `BUY` — 딱 봤을 때 이해되는 것만 (사용자 지시) |
| v1.0.2 | 2026-10-17 | 쇼츠 썸네일 글자 `64.7% > 51.8% ?` · `BUY` — 비교·수식 기호 (사용자 지시) |
| v1.0.1 | 2026-10-17 | 쇼츠 썸네일 글자 `64.7%` · `BUY` · `?` (사용자 지시 — 영어·숫자·기호 써도 됨) |
| v1.0 | 2026-10-17 | 새로 만듦 — 대본 9문장 284음절 예상 약 48.6초 · 제목 R1 「매수 타이밍 20일선, 한때 성공률 64.7%… 무작위 매수보다 높을까?」 · 9개 언어 제목·설명 · 언어 없는 세로 장면 v1.0 · 숫자 근거 21개 (없음 0) |
