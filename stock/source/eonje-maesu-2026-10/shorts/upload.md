# eonje-maesu-2026-10-shorts 업로드 시트 (주식 쇼츠)

버전: v1.2 — 2026-10-18 — 설명란 = 첫 설명(간단히) + 롱폼 안내 + 자료 + 알려 드립니다, 각 아래 영어 · 롱폼 제목을 새 2줄 제목으로 · 태그에 영어 더함 · 그 밖은 원래대로 (사용자 지시 2026-10-18 "설명에 맨처음 설명(최대한 간단하게) 챕터, 자료, 알려 드립니다 만 남기고 나머지는 지워 그리고 각 밑 부분에 영어로 번역해서 쓰고 챕터는 각각 챕터 옆에 괄호 안에 영어로 번역해서 넣어 그렇게 수정하고 태그에 영어도 포함해 그리고 나머지는 원래대로 돌리자" · "한국어 제목 잘리잖아 안질리도록 영상 제목 다시 수정해봐").
(v1.1 — 2026-10-18 — 기본 언어 en 판은 되돌림)
(v1.0 — 2026-10-18 — 새로 만듦: `shorts.md` v2.1 의 제목 R1 · 설명란(4번) · 언어별 제목·설명(1-1)을 업로드 도구가 읽는 꼴로 옮김 · 자막 언어별 (사용자 지시 2026-10-18 "채권 표현 수정하고 영상 업로드 할 준비해").)

기준 파일: 쇼츠 대본 `eonje-maesu-2026-10-shorts.txt` (12문장) · SRT 문장 12 / 자막 14 (`align-audio` 로 오디오에 맞춤) · 오디오 `narration.mp3` 57.8초 · 올릴 영상 = `stock/out/eonje-maesu-2026-10-shorts/final_1080p.mp4` (이 클라우드 컨테이너에만 — git 에 넣지 않음, 장면 파일·오디오로 다시 만듦)

> 업로드: `python3 tools/youtube_upload.py stock eonje-maesu-2026-10-shorts --dry-run` → `--publish-at <시각>` (비공개로 올리고 그 시각에 공개). 롱폼 `eonje-maesu-2026-10` 과 **같은 시각에 공개** (`guides/upload_guide.md` 12번). 자막은 한국어 + 9개 언어 = 10개(4,000단위) — 할당량이 모자라면 남은 언어는 `--captions-only` 로 다음 날.
> ※ 연구·교육용 — 투자 권유가 아님.

## 1. 제목 (`shorts.md` R1, `title_fit.py --shorts` 2줄 안)

```
매수 신호 10가지, 무작위 매수보다 성공률 높을까?
```

## 2. 설명란 (첫 설명 · 롱폼 안내 · 자료 · 알려 드립니다 — 각 아래 영어)

```
매수 신호 10가지를 무작위 매수 2천 개와 비교해, AI가 짠 파이썬 코드로 백테스트했습니다(SPY, 2016년부터). 가장 높은 건 20일 평균선을 넘을 때 매수(성공률 52.1%)였지만, 10가지 모두 무작위 매수와 차이가 없는 범위였어요.
We backtested 10 buy signals against 2,000 random buys with AI-written Python code (SPY, from 2016). The best was buying when the price crosses above the 20-day average (52.1% success), but all 10 were in a range no different from random buying.
▶ 10가지 신호의 기록과, 기간을 바꿔도 같은지는 아래 '관련 동영상'에서 — 매수 타이밍, 신호 10가지는 무작위보다 5% 먼저 오를까?
▶ Each signal's record, and other periods: see the related video below — When to buy: do dip, RSI and breakout signals hit +5% before −2% more often than random buys?

■ 자료 (Data)
SPY·VIX 일별: Yahoo Finance 차트 API
SPY & VIX daily data: Yahoo Finance chart API

■ 알려 드립니다 (Notice)
과거 자료로 계산한 결과이며 투자 권유가 아닙니다. 계산 코드는 AI가 짰고, 내레이션은 AI 음성입니다.
Results from past data. Not investment advice. The code was written by AI and the narration is an AI voice.
#SPY #RSI
```

## 3. 언어별 제목·설명 (`shorts.md` 1-1 그대로 — 9개 언어, 업로드 도구 v1.6 localizations)

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

## 4. 태그 (한국어 + 영어)

```
SPY, 매수 타이밍, 매수 신호, 언제 사야 할까, 이동평균선, RSI, 백테스트, S&P 500, when to buy, backtest, buy signal, VIX, moving average, investing, Shorts
```

## 6. 업로드 설정

| 항목 | 값 |
|---|---|
| 공개 범위 | 비공개로 올리고 예약 시각에 공개 (`--publish-at`) — 롱폼과 같은 시각 |
| 기본 언어 | ko |
| 자막 올리기 | **언어별** (한국어 `eonje-maesu-2026-10-shorts.srt` + `subs/eonje-maesu-2026-10-shorts.<언어>.srt` 9개 — 화면에는 굽지 않음, `stock/guides/README.md` v1.24 4번) |
| 변경되거나 합성된 콘텐츠 | **예** (내레이션이 AI 음성 — CLAUDE.md) |
| 카테고리 | 교육 |
| 썸네일 | `thumbnails/thumbnail_1.png` (세로 9:16 — 그림이 화면 끝까지) → 도구가 세로 720×1280 JPG 로 올림 · 0초 장면도 같은 그림 · 공개 뒤 `i.ytimg.com/vi/<ID>/oardefault.jpg` 로 확인 |
| 관련 동영상 | 롱폼 `eonje-maesu-2026-10` 「매수 타이밍, 저점·RSI·신고가 신호는 2% 떨어지기 전 5% 오를 확률이 무작위 매수보다 높을까?」 (`../youtube.json`) — 스튜디오 → 콘텐츠 → Shorts → 연필 → '관련 동영상' (API 로 못 검 — 사용자가 직접) |
| 자동 더빙 | 스튜디오에서 지원 언어가 보이면 켠다 |

## 7. 결과 (업로드 후)
- (올린 뒤 `youtube.json` 의 영상 ID·예약 시각·자막 언어를 적는다)
