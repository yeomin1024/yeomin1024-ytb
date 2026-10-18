# reobeoriji-2026-10 업로드 시트

버전: v1.6 — 2026-10-18 — 제목을 2줄 안으로 줄임 · 설명란 = 첫 설명(간단히) + 챕터(괄호 영어) + 자료 + 알려 드립니다, 각 아래 영어 (실험 방법·재현 조건 단락은 지움) · 태그에 영어 더함 · 그 밖(기본 언어 ko·언어별·고정 댓글)은 원래대로 (사용자 지시 2026-10-18 "설명에 맨처음 설명(최대한 간단하게) 챕터, 자료, 알려 드립니다 만 남기고 나머지는 지워 그리고 각 밑 부분에 영어로 번역해서 쓰고 챕터는 각각 챕터 옆에 괄호 안에 영어로 번역해서 넣어 그렇게 수정하고 태그에 영어도 포함해 그리고 나머지는 원래대로 돌리자" · "한국어 제목 잘리잖아 안질리도록 영상 제목 다시 수정해봐").
(v1.5 — 2026-10-18 — 기본 언어 en 판은 되돌림)
(v1.4.1 — 2026-10-17 — 업로드 설정 '자막 올리기' = **언어별** (한국어 + 9개 언어 CC — 화면에는 굽지 않음, 사용자 지시 2026-10-17 "외국어 자막 대본도 필요하지? 쇼츠, 롱폼 각각 언어별로 작성해봐") · 자막 대본 `subs/<영상ID>.<언어>.txt` 9개.)
(v1.4 — 2026-10-17 — 대본 v1.4 (티커 설명 (사용자 지시 2026-10-17 "일단 티커에 대한 설명도 추가해 예를 들어 'S&P500을 추종하는 ETF인 SPY' 이런식으로 다 수정해보고")) — 챕터·문장 수 다시.)
(v1.3 — 2026-10-17 — 대본 v1.3 (사용자가 붙인 ChatGPT 페르소나 검토 2차 '네 영상에 공통으로 반복되는 문제 5개'): 2번 설명란과 5번 언어별 설명 9개에 **재현 조건** 한 단락 (가격 자료·배당 처리·매수 날·보정 기간·ETF 보수) · 챕터 다시 계산.)
(v1.2 — 2026-10-17 — 대본 v1.2 (사용자가 붙인 ChatGPT 페르소나 검토 2026-10-17 '네 영상에 반복되는 문제 5개' — 경주 해설은 대표 장면만, 조건을 앞에서 분명히, 숫자와 뜻을 한 문장에, 말하는 금액은 어림(만 단위 하나), 한계에 결정 조건): 챕터 다시 계산 (문장 번호 바뀜).)
(v1.1 — 2026-10-17 — 대본 v1.1 (도입 + 규칙 약 24초 — 사용자 지시 2026-10-17 "야 너 내가 테스트 들어가지 전 도입 및 규칙 설명 30초 넘기지 말라고 했잖아 근데 왜 안지켜 다시 수정해"): 챕터 다시 계산 — 규칙 챕터는 첫 챕터에 합침(10초 미만이 될 수 있어서), 설명 챕터는 결과 뒤. (v1.0 — 2026-10-16 — 최초 (주식 4번 레버리지 1·2·3배 — `backtest/run.py` v1.0). 사용자 지시 2026-10-16 "같은 방식으로 필요한 소스 생성해서 3개 영상 미리보기 영상 만들어봐". `stock/guides/README.md` 2·4번: 결말 없음, 언어별 제목·설명, 자막 올리지 않음.))
기준 파일: 대본 v1.4 (102문장) · SRT 문장 102 (추정 시각 — 오디오가 생기면 다시) · 결과 `backtest/results.json` · 올릴 영상 = 렌더 원본 `stock/out/reobeoriji-2026-10/final_1080p.mp4` (오디오가 생긴 뒤 — 지금 있는 `preview_estimated_silent.mp4` 는 소리 없는 미리보기라 올리지 않음)

> 업로드: 이 클라우드 환경의 키(= STOCK LAB 채널, `stock/youtube_channel.json`)로 `python tools/youtube_upload.py stock reobeoriji-2026-10 --publish-at +1h` — 비공개 업로드 + **1시간 뒤 예약 공개**. PC 업로더(`run_uploader.ps1 -Topic stock`)도 같은 시트를 쓴다.
> 연구·교육용 콘텐츠 — 투자 권유가 아님.

## 1. 제목 (한국어 — 기본 언어 · 모바일·PC 목록 2줄 안 `title_fit.py` ✅ · 예전 「레버리지 ETF, 닷컴 폭락부터 27년 매달 모으면 QLD·TQQQ가 1배 QQQ보다 더 남을까?」은 잘려서 줄임)

```
레버리지 TQQQ, 27년 매달 모으면 QQQ보다 더 남을까?
```

## 2. 설명란 (첫 설명 · 챕터 · 자료 · 알려 드립니다 — 각 아래 영어, 챕터는 괄호 영어 · 시각은 업로드 도구가 SRT 로 다시 계산)

```
나스닥100을 2배·3배로 따라가는 QLD·TQQQ, 오래 모으면 훨씬 많이 남을까요? 1999년부터 1배·2배·3배 계좌에 매달 500달러씩 넣고 27년을 AI가 짠 파이썬 코드로 백테스트했습니다.
QLD and TQQQ follow the Nasdaq-100 at 2× and 3×. Buy them for years — far more money? From 1999 we put $500 a month into 1×, 2× and 3× accounts and backtested 27 years with AI-written Python code.

■ 챕터 (Chapters)
0:00 레버리지, 오래 모으면? (Leverage for years?)
0:27 1999년부터 날짜를 흘려 보면 (From 1999, day by day)
1:19 2008년 금융위기와 그 뒤 (The 2008 crisis and after)
2:09 2022년 긴 하락 (2022: a long fall)
2:43 27년 결과 (27-year result)
3:28 매일 배수를 맞춘다는 것 (Daily reset, explained)
4:11 처음에 한 번만 넣었다면 (One lump sum?)
4:52 시작한 달을 바꾸면 (Other start months)
5:44 2·3배 계산과 실제 QLD·TQQQ (2×/3× math vs real QLD/TQQQ)
6:54 정리 (Summary)
7:24 이 실험의 한계 (Limits)

■ 자료 (Data)
일별 종가·분배금·금리: Yahoo Finance 차트 API
Daily close, payouts & interest rates: Yahoo Finance chart API

■ 알려 드립니다 (Notice)
과거 자료로 계산한 결과이며 앞으로도 같다는 보장은 없습니다. 2배·3배의 1999~2010년 값은 계산한 값입니다. 특정 상품을 매수·매도하라는 이야기가 아니며 투자 권유가 아닙니다. 계산 코드는 AI가 짰고, 내레이션은 AI 음성입니다.
These results come from past data — the future may be different. The 2× and 3× values for 1999–2010 are calculated. This is not a tip to buy or sell any product and not investment advice. The code was written by AI and the narration is an AI voice.

#레버리지 #TQQQ #백테스트
```

## 3. 챕터 다시 계산하기 (문장 번호 기준)

```
python tools/srt_tool.py upload stock/source/reobeoriji-2026-10/reobeoriji-2026-10.txt stock/source/reobeoriji-2026-10/reobeoriji-2026-10.srt --chapters "1=레버리지, 오래 모으면?;6=1999년부터 날짜를 흘려 보면;18=2008년 금융위기와 그 뒤;27=2022년 긴 하락;34=27년 결과;43=매일 배수를 맞춘다는 것;53=처음에 한 번만 넣었다면;62=시작한 달을 바꾸면;73=2·3배 계산과 실제 QLD·TQQQ;88=정리;95=이 실험의 한계"
```
- 2026-10-17 추정 시각(오디오 전, 대본 v1.4)으로 "✅ YouTube 챕터 규칙 통과". 업로드 도구가 오디오에 맞춘 SRT로 다시 계산한다. 챕터 이름에 결과를 쓰지 않는다.

## 4. 태그 (한국어 + 영어)

```
레버리지 ETF, TQQQ, QLD, QQQ, 나스닥100, 레버리지 장기투자, 적립식, 닷컴 버블, 변동성 끌림, 백테스트, leveraged ETF, TQQQ backtest, Nasdaq 100, 3x leverage, 2x leverage, dot com crash, volatility decay, dollar cost averaging, backtest, Python backtest, investing
```

## 5. 언어별 제목·설명 (localizations)

JSON — 업로드 도구가 그대로 읽는다. 챕터는 넣지 않았다 (시각이 오디오 뒤에 바뀜).

```
{
 "en": {
  "title": "Leveraged ETFs from the dot-com crash: buying QLD and TQQQ monthly for 27 years, more than 1x QQQ?",
  "description": "QLD and TQQQ follow the Nasdaq-100 at 2x and 3x. Saved for a long time, they seem sure to beat the index. But how do they survive a crash?\nThree accounts bought the same $500 on the first trading day of every month from April 1999 (including the dot-com crash) to October 2026: 1x = QQQ, 2x and 3x calculated the way QLD and TQQQ work (daily reset, 0.95% fee, borrowing cost at the 13-week T-bill rate plus a spread fitted once to the real QLD, then checked against the real TQQQ). 0.25% fee per purchase. As the dates roll forward, the three accounts and the money put in move in real time on a log scale.\nChecks: one lump sum of $10,000, 211 ten-year accounts started in different months, 25-year accounts, and the real QQQ, QLD and TQQQ from March 2010.\nThe code was written by AI and tested for look-ahead bias. Taxes and currency are not included. The narration is an AI voice.\nReproduction details: 1x = QQQ total return with dividends reinvested. 2x/3x = daily return of the Nasdaq-100 total return (QQQ total return + QQQ's 0.20% fee) × 2 or 3, minus a 0.95% fee and minus the borrowed part (1x for 2x, 2x for 3x) × (previous day's 13-week T-bill rate + 1.02%), costs charged per calendar day. The 1.02% was set once so the end value matches the real QLD from its first day (2006-06-21) to 2026-10-15; with the same value, TQQQ comes out 0.57% a year below the real one. $500 at the close of the first trading day of each month, 0.25% fee.\nData: Yahoo Finance (QQQ, QLD, TQQQ, Nasdaq-100, 13-week T-bill rate).\nPast results do not guarantee future returns. This video is for education only and is not investment advice."
 },
 "hi": {
  "title": "डॉट-कॉम गिरावट से लीवरेज ETF: 27 साल हर महीने QLD·TQQQ खरीदें तो क्या 1x QQQ से ज़्यादा बचेगा?",
  "description": "QLD और TQQQ नैस्डैक-100 को 2 गुना और 3 गुना फॉलो करते हैं। लंबे समय तक जमा करें तो लगता है इंडेक्स से आगे निकलेंगे। लेकिन गिरावट में क्या होता है?\nअप्रैल 1999 (डॉट-कॉम गिरावट सहित) से अक्टूबर 2026 तक तीन खातों ने हर महीने के पहले कारोबारी दिन $500 खरीदे: 1x = QQQ, 2x और 3x को QLD·TQQQ की तरह गणना की (रोज़ रीसेट, 0.95% शुल्क, उधार लागत)। हर खरीद पर 0.25% शुल्क।\nजाँच: एक साथ $10,000, अलग महीनों से शुरू हुए 211 दस-वर्षीय खाते, और मार्च 2010 से असली QQQ·QLD·TQQQ। कोड AI ने लिखा। वॉइस-ओवर AI आवाज़ है।\nदोबारा जाँचने के लिए: 1x = QQQ का कुल रिटर्न (डिविडेंड दोबारा लगाकर)। 2x/3x = नैस्डैक-100 कुल रिटर्न (QQQ कुल रिटर्न + QQQ शुल्क 0.20%) का रोज़ का रिटर्न × 2 या 3, घटाकर 0.95% शुल्क और उधार वाला हिस्सा (2x में 1x, 3x में 2x) × (पिछले दिन की 13-हफ़्ते की ट्रेज़री बिल दर + 1.02%), खर्च कैलेंडर दिनों के हिसाब से। 1.02% एक बार इस तरह तय किया गया कि QLD के पहले दिन (2006-06-21) से 2026-10-15 तक अंतिम मूल्य असली QLD जितना हो; उसी मान से TQQQ असली से सालाना 0.57% कम निकलता है। हर महीने के पहले कारोबारी दिन बंद भाव पर $500, 0.25% शुल्क।\nडेटा: Yahoo Finance।\nपिछले नतीजे भविष्य की गारंटी नहीं हैं। यह वीडियो केवल शिक्षा के लिए है, निवेश सलाह नहीं।"
 },
 "id": {
  "title": "ETF leverage sejak krisis dot-com: beli QLD·TQQQ tiap bulan 27 tahun, sisa lebih dari 1x QQQ?",
  "description": "QLD dan TQQQ mengikuti Nasdaq-100 dua dan tiga kali lipat. Jika ditabung lama, tampaknya pasti mengalahkan indeks. Tapi bagaimana saat pasar jatuh?\nTiga akun membeli $500 yang sama pada hari bursa pertama setiap bulan dari April 1999 (termasuk krisis dot-com) sampai Oktober 2026: 1x = QQQ, 2x dan 3x dihitung seperti cara kerja QLD dan TQQQ (reset harian, biaya 0,95%, biaya pinjaman). Biaya 0,25% per pembelian.\nPengecekan: sekali $10.000, 211 akun sepuluh tahun dengan bulan mulai berbeda, dan QQQ, QLD, TQQQ asli sejak Maret 2010. Kode ditulis oleh AI. Narasi memakai suara AI.\nDetail untuk mengulang: 1x = total return QQQ dengan dividen diinvestasikan kembali. 2x/3x = imbal hasil harian total return Nasdaq-100 (total return QQQ + biaya QQQ 0,20%) × 2 atau 3, dikurangi biaya 0,95% dan bagian pinjaman (1x untuk 2x, 2x untuk 3x) × (suku bunga T-bill 13 minggu hari sebelumnya + 1,02%), biaya dihitung per hari kalender. Angka 1,02% ditetapkan sekali agar nilai akhir sama dengan QLD asli sejak hari pertamanya (2006-06-21) sampai 2026-10-15; dengan angka yang sama, TQQQ hasilnya 0,57% per tahun di bawah yang asli. $500 di harga penutupan hari bursa pertama tiap bulan, biaya 0,25%.\nData: Yahoo Finance.\nHasil masa lalu tidak menjamin hasil masa depan. Video ini hanya untuk edukasi, bukan saran investasi."
 },
 "pt": {
  "title": "ETFs alavancados desde a bolha pontocom: comprar QLD e TQQQ todo mês por 27 anos rende mais que QQQ?",
  "description": "QLD e TQQQ seguem o Nasdaq-100 em 2x e 3x. Acumulando por muito tempo, parece certo que vençam o índice. Mas como sobrevivem a um crash?\nTrês contas compraram os mesmos US$ 500 no primeiro dia útil de cada mês, de abril de 1999 (com a bolha pontocom) a outubro de 2026: 1x = QQQ, 2x e 3x calculados como QLD e TQQQ funcionam (reajuste diário, taxa de 0,95%, custo de empréstimo). Taxa de 0,25% por compra.\nVerificações: um aporte único de US$ 10.000, 211 contas de dez anos iniciadas em meses diferentes e os QQQ, QLD e TQQQ reais desde março de 2010. O código foi escrito por IA. A narração é uma voz de IA.\nDetalhes para reproduzir: 1x = retorno total do QQQ com dividendos reinvestidos. 2x/3x = retorno diário do retorno total do Nasdaq-100 (retorno total do QQQ + taxa do QQQ de 0,20%) × 2 ou 3, menos taxa de 0,95% e menos a parte emprestada (1x no 2x, 2x no 3x) × (taxa do T-bill de 13 semanas do dia anterior + 1,02%), custos cobrados por dia corrido. O 1,02% foi definido uma vez para o valor final igualar o QLD real desde seu primeiro pregão (2006-06-21) até 2026-10-15; com o mesmo valor, o TQQQ sai 0,57% ao ano abaixo do real. US$ 500 no fechamento do primeiro pregão de cada mês, taxa de 0,25%.\nDados: Yahoo Finance.\nResultados passados não garantem resultados futuros. Este vídeo é educativo e não é recomendação de investimento."
 },
 "es-419": {
  "title": "ETF apalancados desde la burbuja puntocom: ¿comprar QLD y TQQQ cada mes 27 años deja más que QQQ?",
  "description": "QLD y TQQQ siguen al Nasdaq-100 a 2x y 3x. Acumulando mucho tiempo, parece seguro que ganen al índice. Pero ¿cómo sobreviven a un desplome?\nTres cuentas compraron los mismos US$500 el primer día hábil de cada mes, de abril de 1999 (con la burbuja puntocom) a octubre de 2026: 1x = QQQ, 2x y 3x calculados como funcionan QLD y TQQQ (reajuste diario, comisión de 0.95%, costo de préstamo). Comisión de 0.25% por compra.\nComprobaciones: una sola inversión de US$10,000, 211 cuentas de diez años iniciadas en meses distintos y los QQQ, QLD y TQQQ reales desde marzo de 2010. El código lo escribió una IA. La narración es una voz de IA.\nDetalles para reproducir: 1x = retorno total de QQQ con dividendos reinvertidos. 2x/3x = rendimiento diario del retorno total del Nasdaq-100 (retorno total de QQQ + comisión de QQQ de 0.20%) × 2 o 3, menos comisión de 0.95% y menos la parte prestada (1x en el 2x, 2x en el 3x) × (tasa del T-bill a 13 semanas del día anterior + 1.02%), costos cobrados por día calendario. El 1.02% se fijó una vez para que el valor final iguale al QLD real desde su primer día (2006-06-21) hasta 2026-10-15; con ese mismo valor, TQQQ sale 0.57% al año por debajo del real. US$500 al cierre del primer día hábil de cada mes, comisión de 0.25%.\nDatos: Yahoo Finance.\nLos resultados pasados no garantizan resultados futuros. Este video es educativo y no es asesoría de inversión."
 },
 "ja": {
  "title": "レバレッジETF、ITバブル崩壊から27年毎月積み立てると、QLD・TQQQは1倍のQQQより多く残る？",
  "description": "ナスダック100を2倍・3倍で追うQLDとTQQQ。長く積み立てれば指数より大きく増えそうですが、暴落が来たらどこまで耐えられるのでしょうか？\n1999年4月（ITバブル崩壊を含む）から2026年10月まで、3つの口座が毎月最初の取引日に同じ500ドルを買いました。1倍＝QQQ、2倍・3倍はQLD・TQQQと同じ仕組み（毎日倍率を合わせる、信託報酬0.95%、借入コスト）で計算。購入ごとに手数料0.25%。\n確認：1万ドルの一括投資、開始月を変えた10年口座211個、2010年3月からの実際のQQQ・QLD・TQQQ。コードはAIが書きました。ナレーションはAI音声です。\n再現条件：1倍＝配当を再投資したQQQのトータルリターン。2倍・3倍＝ナスダック100のトータルリターン（QQQのトータルリターン＋QQQの経費率0.20%）の日次リターン×2・3から、信託報酬0.95%と、借入部分（2倍は1倍分、3倍は2倍分）×（前日の13週米国債金利＋1.02%）を引いたもの。コストは暦日数で日割り。1.02%は、QLDの初取引日（2006-06-21）から2026-10-15までの最終値が実際のQLDと同じになるよう一度だけ決めた値で、同じ値で計算したTQQQは実際より年0.57%低くなります。毎月最初の取引日の終値で500ドル、手数料0.25%。\nデータ：Yahoo Finance。\n過去の結果は将来を保証しません。この動画は教育目的であり、投資助言ではありません。"
 },
 "de": {
  "title": "Hebel-ETFs ab dem Dotcom-Crash: QLD und TQQQ 27 Jahre monatlich kaufen – mehr als 1x QQQ?",
  "description": "QLD und TQQQ bilden den Nasdaq-100 zwei- und dreifach ab. Lange gespart, scheinen sie den Index sicher zu schlagen. Aber wie überstehen sie einen Crash?\nDrei Konten kauften von April 1999 (inklusive Dotcom-Crash) bis Oktober 2026 am ersten Handelstag jedes Monats dieselben 500 $: 1x = QQQ, 2x und 3x so berechnet, wie QLD und TQQQ funktionieren (tägliche Anpassung, 0,95 % Gebühr, Finanzierungskosten). 0,25 % Gebühr pro Kauf.\nPrüfungen: einmalig 10.000 $, 211 Zehnjahreskonten mit verschiedenen Startmonaten und die echten QQQ, QLD und TQQQ ab März 2010. Den Code hat eine KI geschrieben. Die Sprecherstimme ist eine KI-Stimme.\nDetails zum Nachrechnen: 1x = Gesamtrendite von QQQ mit wiederangelegten Dividenden. 2x/3x = Tagesrendite der Nasdaq-100-Gesamtrendite (QQQ-Gesamtrendite + QQQ-Gebühr 0,20 %) × 2 oder 3, abzüglich 0,95 % Gebühr und abzüglich des geliehenen Teils (1x bei 2x, 2x bei 3x) × (Vortageszins der 13-Wochen-T-Bills + 1,02 %), Kosten je Kalendertag. Die 1,02 % wurden einmal so gesetzt, dass der Endwert dem echten QLD vom ersten Handelstag (2006-06-21) bis 2026-10-15 entspricht; mit demselben Wert liegt TQQQ 0,57 % pro Jahr unter dem echten. 500 $ zum Schlusskurs am ersten Handelstag jedes Monats, 0,25 % Gebühr.\nDaten: Yahoo Finance.\nVergangene Ergebnisse garantieren keine zukünftigen Renditen. Dieses Video dient nur der Bildung und ist keine Anlageberatung."
 },
 "vi": {
  "title": "ETF đòn bẩy từ bong bóng dot-com: mua QLD, TQQQ mỗi tháng suốt 27 năm có hơn QQQ 1x không?",
  "description": "QLD và TQQQ bám theo Nasdaq-100 gấp 2 và 3 lần. Tích lũy lâu dài thì có vẻ chắc chắn vượt chỉ số. Nhưng khi thị trường sập thì sao?\nBa tài khoản mua cùng 500 USD vào ngày giao dịch đầu tiên mỗi tháng từ tháng 4/1999 (gồm cả bong bóng dot-com) đến tháng 10/2026: 1x = QQQ, 2x và 3x tính theo cách QLD và TQQQ vận hành (cân bằng hằng ngày, phí 0,95%, chi phí vay). Phí 0,25% mỗi lần mua.\nKiểm tra: đầu tư một lần 10.000 USD, 211 tài khoản mười năm bắt đầu ở các tháng khác nhau, và QQQ, QLD, TQQQ thật từ tháng 3/2010. Mã do AI viết. Giọng đọc là giọng AI.\nChi tiết để tính lại: 1x = tổng lợi nhuận QQQ có tái đầu tư cổ tức. 2x/3x = lợi nhuận hằng ngày của tổng lợi nhuận Nasdaq-100 (tổng lợi nhuận QQQ + phí QQQ 0,20%) × 2 hoặc 3, trừ phí 0,95% và trừ phần đi vay (1x với 2x, 2x với 3x) × (lãi suất tín phiếu kho bạc 13 tuần của ngày hôm trước + 1,02%), chi phí tính theo ngày lịch. Con số 1,02% được đặt một lần để giá trị cuối khớp với QLD thật từ ngày đầu tiên (2006-06-21) đến 2026-10-15; với cùng con số đó, TQQQ thấp hơn thực tế 0,57% mỗi năm. 500 USD ở giá đóng cửa ngày giao dịch đầu mỗi tháng, phí 0,25%.\nDữ liệu: Yahoo Finance.\nKết quả quá khứ không đảm bảo tương lai. Video chỉ nhằm mục đích giáo dục, không phải lời khuyên đầu tư."
 },
 "tr": {
  "title": "Dotcom çöküşünden kaldıraçlı ETF: 27 yıl her ay QLD ve TQQQ almak 1x QQQ'dan fazla bırakır mı?",
  "description": "QLD ve TQQQ, Nasdaq-100'ü 2 ve 3 kat izler. Uzun süre biriktirilince endeksi kesin geçecek gibi görünür. Peki bir çöküşte ne olur?\nÜç hesap, Nisan 1999'dan (dotcom çöküşü dahil) Ekim 2026'ya kadar her ayın ilk işlem gününde aynı 500 doları aldı: 1x = QQQ, 2x ve 3x QLD ile TQQQ'nun çalıştığı gibi hesaplandı (günlük sıfırlama, %0,95 ücret, borçlanma maliyeti). Alım başına %0,25 komisyon.\nKontroller: tek seferde 10.000 dolar, farklı aylarda başlayan 211 on yıllık hesap ve Mart 2010'dan itibaren gerçek QQQ, QLD ve TQQQ. Kodu yapay zekâ yazdı. Seslendirme yapay zekâ sesidir.\nYeniden hesaplama ayrıntıları: 1x = temettüler yeniden yatırılmış QQQ toplam getirisi. 2x/3x = Nasdaq-100 toplam getirisinin (QQQ toplam getirisi + QQQ'nun %0,20 ücreti) günlük getirisi × 2 veya 3, eksi %0,95 ücret ve eksi borçlanılan kısım (2x'te 1x, 3x'te 2x) × (bir önceki günün 13 haftalık hazine bonosu faizi + %1,02); maliyetler takvim günü başına. %1,02 bir kez, QLD'nin ilk işlem gününden (2006-06-21) 2026-10-15'e kadar bitiş değeri gerçek QLD'ye eşit olacak şekilde belirlendi; aynı değerle TQQQ gerçeğinden yılda %0,57 düşük çıkar. Her ayın ilk işlem günü kapanışından 500 dolar, %0,25 komisyon.\nVeri: Yahoo Finance.\nGeçmiş sonuçlar gelecekteki getirileri garanti etmez. Bu video yalnızca eğitim amaçlıdır, yatırım tavsiyesi değildir."
 }
}
```

## 6. 고정 댓글

```
1배·2배·3배를 27년 동안 매달 같은 돈으로 모았다면, 어느 계좌가 가장 많이 남을 거라고 생각하셨나요? 폭락을 지날 때 계속 매수할 수 있었을지도 궁금합니다.
다음에 백테스트로 검증해 볼 가설도 댓글로 남겨 주세요.
(정보 제공용이며 투자 권유가 아닙니다)
```

## 7. 업로드 설정

| 항목 | 값 |
|---|---|
| 공개 상태 | 비공개로 올리고 **1시간 뒤 예약 공개** (`--publish-at +1h`) |
| 썸네일 | `thumbnails/thumbnail_1.*` (본안 — 글자 없음). 공개 뒤 '테스트 및 비교'에 thumbnail_1~3 |
| 기본 언어 | ko |
| 자막 올리기 | **언어별** (한국어 + en·hi·id·pt·es-419·ja·de·vi·tr — 화면에는 굽지 않고 CC 로, `subs/` 대본 → 오디오 뒤 `python3 tools/subs_tool.py build stock reobeoriji-2026-10` · 업로드 도구 v1.12 가 자막 하나 400단위 — 할당량이 모자라면 `--captions-only` 로 다음 날, 사용자 지시 2026-10-17 "외국어 자막 대본도 필요하지? 쇼츠, 롱폼 각각 언어별로 작성해봐") |
| 카테고리 | 교육 |
| 동영상 언어 | 한국어 (내레이션) |
| 자동 더빙 | 스튜디오에서 지원 언어가 보이면 켠다 |
| 시청자층 | 아동용 아님 |
| 유료 프로모션 | 없음 |
| 변경되거나 합성된 콘텐츠 | **예** (내레이션이 AI 음성) |

## 8. 점검

- **결말 없음**: 제목·설명란·챕터·고정 댓글·언어별 제목·설명 어디에도 결과(어느 계좌가 많았는지·배수·금액)를 쓰지 않았다.
- 설명란 숫자(1999-04·2026-10·500달러·0.95%·13주·0.25%·1만 달러·211·31·10년·25년·2010-03·10%·2018·1999-03-10)는 대본·`backtest/results.json`·`run.py` 설정에 있는 것만.
- 언어별 제목 100자 이하 · `< >` 없음 — `python tools/youtube_upload.py stock reobeoriji-2026-10 --dry-run` 으로 확인.
- 사다 → 매수, 팔다 → 매도.

## 9. 결과 (업로드 후)
- 영상 ID·예약 공개 시각·올린 언어: `youtube.json` (업로드 도구가 씀)
- 48시간 뒤·7일 뒤: 노출 클릭률, 평균 시청 지속 시간, 시청 지속 그래프에서 크게 떨어지는 장, **나라·언어별 조회수**
