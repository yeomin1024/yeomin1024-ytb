# reobeoriji-2026-10 업로드 시트

버전: v1.2 — 2026-10-17 — 대본 v1.2 (사용자가 붙인 ChatGPT 페르소나 검토 2026-10-17 '네 영상에 반복되는 문제 5개' — 경주 해설은 대표 장면만, 조건을 앞에서 분명히, 숫자와 뜻을 한 문장에, 말하는 금액은 어림(만 단위 하나), 한계에 결정 조건): 챕터 다시 계산 (문장 번호 바뀜).
(v1.1 — 2026-10-17 — 대본 v1.1 (도입 + 규칙 약 24초 — 사용자 지시 2026-10-17 "야 너 내가 테스트 들어가지 전 도입 및 규칙 설명 30초 넘기지 말라고 했잖아 근데 왜 안지켜 다시 수정해"): 챕터 다시 계산 — 규칙 챕터는 첫 챕터에 합침(10초 미만이 될 수 있어서), 설명 챕터는 결과 뒤. (v1.0 — 2026-10-16 — 최초 (주식 4번 레버리지 1·2·3배 — `backtest/run.py` v1.0). 사용자 지시 2026-10-16 "같은 방식으로 필요한 소스 생성해서 3개 영상 미리보기 영상 만들어봐". `stock/guides/README.md` 2·4번: 결말 없음, 언어별 제목·설명, 자막 올리지 않음.))
기준 파일: 대본 v1.2 (99문장) · SRT 문장 99 (추정 시각 — 오디오가 생기면 다시) · 결과 `backtest/results.json` · 올릴 영상 = 렌더 원본 `stock/out/reobeoriji-2026-10/final_1080p.mp4` (오디오가 생긴 뒤 — 지금 있는 `preview_estimated_silent.mp4` 는 소리 없는 미리보기라 올리지 않음)

> 업로드: 이 클라우드 환경의 키(= STOCK LAB 채널, `stock/youtube_channel.json`)로 `python tools/youtube_upload.py stock reobeoriji-2026-10 --publish-at +1h` — 비공개 업로드 + **1시간 뒤 예약 공개**. PC 업로더(`run_uploader.ps1 -Topic stock`)도 같은 시트를 쓴다.
> 연구·교육용 콘텐츠 — 투자 권유가 아님.

## 1. 제목 (`titles.md` R1, 한국어 — 기본 언어)

```
레버리지 ETF, 닷컴 폭락부터 27년 매달 모으면 QLD·TQQQ가 1배 QQQ보다 더 남을까?
```

## 2. 설명란 (한국어 — 그대로 복사)

```
나스닥100을 2배, 3배로 따라가는 QLD와 TQQQ. 오래 모으면 지수보다 훨씬 많이 남을 것 같지만, 폭락이 오면 얼마나 버틸까요?
닷컴 폭락이 있던 1999년 4월부터 2026년 10월까지, 세 계좌에 매달 첫 거래일 같은 500달러씩 매수했습니다. 1배는 QQQ, 2배·3배는 QLD·TQQQ와 같은 방식(매일 배수를 맞춤, 보수 0.95%, 빌린 돈 이자 = 13주 국채 금리 + 실제 QLD에 맞춘 웃돈)으로 계산했고, 같은 값으로 실제 TQQQ와도 맞춰 봤습니다. 매수 수수료 0.25%.
날짜가 흐르며 세 계좌의 값과 넣은 돈이 실시간으로 바뀝니다 (세로 눈금 한 칸 = 10배).

■ 챕터
0:00 레버리지, 오래 모으면?
0:29 1999년부터 날짜를 흘려 보면
1:24 2008년 금융위기와 그 뒤
2:21 2022년 긴 하락
3:01 27년 결과
3:53 매일 배수를 맞춘다는 것
4:45 처음에 한 번만 넣었다면
5:32 시작한 달을 바꾸면
6:27 2·3배 계산과 실제 QLD·TQQQ
7:41 정리
8:18 이 실험의 한계

■ 실험 방법
자료: QQQ·QLD·TQQQ 일별 종가·분배금(분할 반영), 13주 국채 금리, 1999-03-10 ~ 2026-10-15.
확인: 처음에 1만 달러 한 번, 시작 달을 바꾼 10년 적립 211개·25년 적립 31개, 2010년 3월부터 실제 QQQ·QLD·TQQQ 적립, +10%·−10% 예와 2018년.
계산 코드는 AI가 짰고, 미래 가격을 쓰지 않는지 시험한 뒤 돌렸습니다. 세금·환율은 넣지 않았습니다. 이 영상의 내레이션은 AI 음성입니다.

■ 자료
일별 종가·분배금·금리: Yahoo Finance 차트 API

■ 알려 드립니다
과거 자료로 계산한 결과이며 앞으로도 같다는 보장은 없습니다. 2배·3배의 1999~2010년 값은 계산한 값입니다. 특정 상품을 매수·매도하라는 이야기가 아니며 투자 권유가 아닙니다.

#레버리지 #TQQQ #백테스트
```

## 3. 챕터 다시 계산하기 (문장 번호 기준)

```
python tools/srt_tool.py upload stock/source/reobeoriji-2026-10/reobeoriji-2026-10.txt stock/source/reobeoriji-2026-10/reobeoriji-2026-10.srt --chapters "1=레버리지, 오래 모으면?;6=1999년부터 날짜를 흘려 보면;17=2008년 금융위기와 그 뒤;26=2022년 긴 하락;33=27년 결과;42=매일 배수를 맞춘다는 것;52=처음에 한 번만 넣었다면;61=시작한 달을 바꾸면;71=2·3배 계산과 실제 QLD·TQQQ;85=정리;92=이 실험의 한계"
```
- 2026-10-17 추정 시각(오디오 전, 대본 v1.2)으로 "✅ YouTube 챕터 규칙 통과". 업로드 도구가 오디오에 맞춘 SRT로 다시 계산한다. 챕터 이름에 결과를 쓰지 않는다.

## 4. 태그

```
레버리지 ETF, TQQQ, QLD, QQQ, 나스닥100, 레버리지 장기투자, 적립식, 닷컴 버블, 변동성 끌림, 백테스트, leveraged ETF, TQQQ backtest, Nasdaq 100
```

## 5. 언어별 제목·설명 (localizations)

JSON — 업로드 도구가 그대로 읽는다. 챕터는 넣지 않았다 (시각이 오디오 뒤에 바뀜).

```
{
 "en": {
  "title": "Leveraged ETFs from the dot-com crash: buying QLD and TQQQ monthly for 27 years, more than 1x QQQ?",
  "description": "QLD and TQQQ follow the Nasdaq-100 at 2x and 3x. Saved for a long time, they seem sure to beat the index. But how do they survive a crash?\nThree accounts bought the same $500 on the first trading day of every month from April 1999 (including the dot-com crash) to October 2026: 1x = QQQ, 2x and 3x calculated the way QLD and TQQQ work (daily reset, 0.95% fee, borrowing cost at the 13-week T-bill rate plus a spread fitted once to the real QLD, then checked against the real TQQQ). 0.25% fee per purchase. As the dates roll forward, the three accounts and the money put in move in real time on a log scale.\nChecks: one lump sum of $10,000, 211 ten-year accounts started in different months, 25-year accounts, and the real QQQ, QLD and TQQQ from March 2010.\nThe code was written by AI and tested for look-ahead bias. Taxes and currency are not included. The narration is an AI voice.\nData: Yahoo Finance (QQQ, QLD, TQQQ, Nasdaq-100, 13-week T-bill rate).\nPast results do not guarantee future returns. This video is for education only and is not investment advice."
 },
 "hi": {
  "title": "डॉट-कॉम गिरावट से लीवरेज ETF: 27 साल हर महीने QLD·TQQQ खरीदें तो क्या 1x QQQ से ज़्यादा बचेगा?",
  "description": "QLD और TQQQ नैस्डैक-100 को 2 गुना और 3 गुना फॉलो करते हैं। लंबे समय तक जमा करें तो लगता है इंडेक्स से आगे निकलेंगे। लेकिन गिरावट में क्या होता है?\nअप्रैल 1999 (डॉट-कॉम गिरावट सहित) से अक्टूबर 2026 तक तीन खातों ने हर महीने के पहले कारोबारी दिन $500 खरीदे: 1x = QQQ, 2x और 3x को QLD·TQQQ की तरह गणना की (रोज़ रीसेट, 0.95% शुल्क, उधार लागत)। हर खरीद पर 0.25% शुल्क।\nजाँच: एक साथ $10,000, अलग महीनों से शुरू हुए 211 दस-वर्षीय खाते, और मार्च 2010 से असली QQQ·QLD·TQQQ। कोड AI ने लिखा। वॉइस-ओवर AI आवाज़ है।\nडेटा: Yahoo Finance।\nपिछले नतीजे भविष्य की गारंटी नहीं हैं। यह वीडियो केवल शिक्षा के लिए है, निवेश सलाह नहीं।"
 },
 "id": {
  "title": "ETF leverage sejak krisis dot-com: beli QLD·TQQQ tiap bulan 27 tahun, sisa lebih dari 1x QQQ?",
  "description": "QLD dan TQQQ mengikuti Nasdaq-100 dua dan tiga kali lipat. Jika ditabung lama, tampaknya pasti mengalahkan indeks. Tapi bagaimana saat pasar jatuh?\nTiga akun membeli $500 yang sama pada hari bursa pertama setiap bulan dari April 1999 (termasuk krisis dot-com) sampai Oktober 2026: 1x = QQQ, 2x dan 3x dihitung seperti cara kerja QLD dan TQQQ (reset harian, biaya 0,95%, biaya pinjaman). Biaya 0,25% per pembelian.\nPengecekan: sekali $10.000, 211 akun sepuluh tahun dengan bulan mulai berbeda, dan QQQ, QLD, TQQQ asli sejak Maret 2010. Kode ditulis oleh AI. Narasi memakai suara AI.\nData: Yahoo Finance.\nHasil masa lalu tidak menjamin hasil masa depan. Video ini hanya untuk edukasi, bukan saran investasi."
 },
 "pt": {
  "title": "ETFs alavancados desde a bolha pontocom: comprar QLD e TQQQ todo mês por 27 anos rende mais que QQQ?",
  "description": "QLD e TQQQ seguem o Nasdaq-100 em 2x e 3x. Acumulando por muito tempo, parece certo que vençam o índice. Mas como sobrevivem a um crash?\nTrês contas compraram os mesmos US$ 500 no primeiro dia útil de cada mês, de abril de 1999 (com a bolha pontocom) a outubro de 2026: 1x = QQQ, 2x e 3x calculados como QLD e TQQQ funcionam (reajuste diário, taxa de 0,95%, custo de empréstimo). Taxa de 0,25% por compra.\nVerificações: um aporte único de US$ 10.000, 211 contas de dez anos iniciadas em meses diferentes e os QQQ, QLD e TQQQ reais desde março de 2010. O código foi escrito por IA. A narração é uma voz de IA.\nDados: Yahoo Finance.\nResultados passados não garantem resultados futuros. Este vídeo é educativo e não é recomendação de investimento."
 },
 "es-419": {
  "title": "ETF apalancados desde la burbuja puntocom: ¿comprar QLD y TQQQ cada mes 27 años deja más que QQQ?",
  "description": "QLD y TQQQ siguen al Nasdaq-100 a 2x y 3x. Acumulando mucho tiempo, parece seguro que ganen al índice. Pero ¿cómo sobreviven a un desplome?\nTres cuentas compraron los mismos US$500 el primer día hábil de cada mes, de abril de 1999 (con la burbuja puntocom) a octubre de 2026: 1x = QQQ, 2x y 3x calculados como funcionan QLD y TQQQ (reajuste diario, comisión de 0.95%, costo de préstamo). Comisión de 0.25% por compra.\nComprobaciones: una sola inversión de US$10,000, 211 cuentas de diez años iniciadas en meses distintos y los QQQ, QLD y TQQQ reales desde marzo de 2010. El código lo escribió una IA. La narración es una voz de IA.\nDatos: Yahoo Finance.\nLos resultados pasados no garantizan resultados futuros. Este video es educativo y no es asesoría de inversión."
 },
 "ja": {
  "title": "レバレッジETF、ITバブル崩壊から27年毎月積み立てると、QLD・TQQQは1倍のQQQより多く残る？",
  "description": "ナスダック100を2倍・3倍で追うQLDとTQQQ。長く積み立てれば指数より大きく増えそうですが、暴落が来たらどこまで耐えられるのでしょうか？\n1999年4月（ITバブル崩壊を含む）から2026年10月まで、3つの口座が毎月最初の取引日に同じ500ドルを買いました。1倍＝QQQ、2倍・3倍はQLD・TQQQと同じ仕組み（毎日倍率を合わせる、信託報酬0.95%、借入コスト）で計算。購入ごとに手数料0.25%。\n確認：1万ドルの一括投資、開始月を変えた10年口座211個、2010年3月からの実際のQQQ・QLD・TQQQ。コードはAIが書きました。ナレーションはAI音声です。\nデータ：Yahoo Finance。\n過去の結果は将来を保証しません。この動画は教育目的であり、投資助言ではありません。"
 },
 "de": {
  "title": "Hebel-ETFs ab dem Dotcom-Crash: QLD und TQQQ 27 Jahre monatlich kaufen – mehr als 1x QQQ?",
  "description": "QLD und TQQQ bilden den Nasdaq-100 zwei- und dreifach ab. Lange gespart, scheinen sie den Index sicher zu schlagen. Aber wie überstehen sie einen Crash?\nDrei Konten kauften von April 1999 (inklusive Dotcom-Crash) bis Oktober 2026 am ersten Handelstag jedes Monats dieselben 500 $: 1x = QQQ, 2x und 3x so berechnet, wie QLD und TQQQ funktionieren (tägliche Anpassung, 0,95 % Gebühr, Finanzierungskosten). 0,25 % Gebühr pro Kauf.\nPrüfungen: einmalig 10.000 $, 211 Zehnjahreskonten mit verschiedenen Startmonaten und die echten QQQ, QLD und TQQQ ab März 2010. Den Code hat eine KI geschrieben. Die Sprecherstimme ist eine KI-Stimme.\nDaten: Yahoo Finance.\nVergangene Ergebnisse garantieren keine zukünftigen Renditen. Dieses Video dient nur der Bildung und ist keine Anlageberatung."
 },
 "vi": {
  "title": "ETF đòn bẩy từ bong bóng dot-com: mua QLD, TQQQ mỗi tháng suốt 27 năm có hơn QQQ 1x không?",
  "description": "QLD và TQQQ bám theo Nasdaq-100 gấp 2 và 3 lần. Tích lũy lâu dài thì có vẻ chắc chắn vượt chỉ số. Nhưng khi thị trường sập thì sao?\nBa tài khoản mua cùng 500 USD vào ngày giao dịch đầu tiên mỗi tháng từ tháng 4/1999 (gồm cả bong bóng dot-com) đến tháng 10/2026: 1x = QQQ, 2x và 3x tính theo cách QLD và TQQQ vận hành (cân bằng hằng ngày, phí 0,95%, chi phí vay). Phí 0,25% mỗi lần mua.\nKiểm tra: đầu tư một lần 10.000 USD, 211 tài khoản mười năm bắt đầu ở các tháng khác nhau, và QQQ, QLD, TQQQ thật từ tháng 3/2010. Mã do AI viết. Giọng đọc là giọng AI.\nDữ liệu: Yahoo Finance.\nKết quả quá khứ không đảm bảo tương lai. Video chỉ nhằm mục đích giáo dục, không phải lời khuyên đầu tư."
 },
 "tr": {
  "title": "Dotcom çöküşünden kaldıraçlı ETF: 27 yıl her ay QLD ve TQQQ almak 1x QQQ'dan fazla bırakır mı?",
  "description": "QLD ve TQQQ, Nasdaq-100'ü 2 ve 3 kat izler. Uzun süre biriktirilince endeksi kesin geçecek gibi görünür. Peki bir çöküşte ne olur?\nÜç hesap, Nisan 1999'dan (dotcom çöküşü dahil) Ekim 2026'ya kadar her ayın ilk işlem gününde aynı 500 doları aldı: 1x = QQQ, 2x ve 3x QLD ile TQQQ'nun çalıştığı gibi hesaplandı (günlük sıfırlama, %0,95 ücret, borçlanma maliyeti). Alım başına %0,25 komisyon.\nKontroller: tek seferde 10.000 dolar, farklı aylarda başlayan 211 on yıllık hesap ve Mart 2010'dan itibaren gerçek QQQ, QLD ve TQQQ. Kodu yapay zekâ yazdı. Seslendirme yapay zekâ sesidir.\nVeri: Yahoo Finance.\nGeçmiş sonuçlar gelecekteki getirileri garanti etmez. Bu video yalnızca eğitim amaçlıdır, yatırım tavsiyesi değildir."
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
| 자막 올리기 | **아니요** (전 세계 대상) |
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
