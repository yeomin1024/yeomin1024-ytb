# keobeodeu-kol-2026-10 업로드 시트

버전: v1.1 — 2026-10-17 — 대본 v1.1 (도입 + 규칙 약 23초 — 사용자 지시 2026-10-17 "야 너 내가 테스트 들어가지 전 도입 및 규칙 설명 30초 넘기지 말라고 했잖아 근데 왜 안지켜 다시 수정해"): 챕터 다시 계산 — 규칙 챕터는 첫 챕터에 합침(10초 미만이 될 수 있어서), 설명 챕터는 결과 뒤. (v1.0 — 2026-10-16 — 최초 (주식 2번 커버드콜 원금 — `backtest/run.py` v1.0). 사용자 지시 2026-10-16 "같은 방식으로 필요한 소스 생성해서 3개 영상 미리보기 영상 만들어봐". `stock/guides/README.md` 2·4번: 결말 없음, 언어별 제목·설명, 자막 올리지 않음.)
기준 파일: 대본 (125문장) · SRT 문장 125 (추정 시각 — 오디오가 생기면 다시) · 결과 `backtest/results.json` · 올릴 영상 = 렌더 원본 `stock/out/keobeodeu-kol-2026-10/final_1080p.mp4` (오디오가 생긴 뒤 — 지금 있는 `preview_estimated_silent.mp4` 는 소리 없는 미리보기라 올리지 않음)

> 업로드: 이 클라우드 환경의 키(= STOCK LAB 채널, `stock/youtube_channel.json` — 업로드 도구 v1.7 이 채널이 다르면 올리지 않음)로 `python tools/youtube_upload.py stock keobeodeu-kol-2026-10 --publish-at +1h` — 비공개 업로드 + **1시간 뒤 예약 공개**. PC 업로더(`run_uploader.ps1 -Topic stock`)도 같은 시트를 쓴다.
> 연구·교육용 콘텐츠 — 투자 권유가 아님.

## 1. 제목 (`titles.md` R1, 한국어 — 기본 언어)

```
커버드콜 분배금, 매달 꺼내 쓰면 같은 금액을 매도한 QQQ보다 13년 뒤 원금이 더 남을까?
```

## 2. 설명란 (한국어 — 그대로 복사)

```
매달 분배금이 나오는데 원금은 잘 안 깎인다는 커버드콜 ETF. 분배금을 매달 꺼내 써도 원금이 정말 지켜질까요?
같은 돈 10만 달러를 나스닥100 커버드콜 ETF(QYLD)와 같은 나스닥100을 따라가는 QQQ에 넣고, QYLD 분배금이 나올 때마다 전부 꺼내 쓰고, QQQ는 같은 날 같은 금액만큼 매도해서 꺼내 썼습니다. 두 계좌가 꺼낸 돈은 날짜도 금액도 같습니다. 2013년 12월 ~ 2026년 10월, 수수료 0.25%, 세전.
날짜가 흐르며 두 계좌의 값, 꺼낸 돈, 원금(10만 달러 = 상자 하나)이 실시간으로 바뀝니다.

■ 챕터
0:00 커버드콜 분배금, 원금은?
0:26 2013년부터 날짜를 흘려 보면
2:58 2022년 긴 하락
4:15 2024년부터 끝까지
4:50 13년 결과
5:38 커버드콜은 어떻게 분배금을 만드나
6:50 시작한 달을 바꾸면
7:59 XYLD·JEPI도 같을까
9:08 세금·다시 매수하면
9:56 정리
10:31 이 실험의 한계

■ 실험 방법
자료: QYLD·QQQ·XYLD·SPY·JEPI 일별 종가·분배금 (분할 반영), QYLD 첫 거래일 2013-12-12 ~ 2026-10-15.
분배금은 배당락일 종가 기준으로 꺼낸 것으로 셈. QQQ 자기 배당은 다시 매수. 사고팔 때마다 수수료 0.25%.
확인: 시작 달을 바꾼 5년 계좌 94개·3년 계좌 118개, S&P 500 커버드콜 XYLD vs SPY, JEPI vs SPY, 원천징수 15%, 분배금을 다시 매수하는 경우.
계산 코드는 AI가 짰고, 미래 가격을 쓰지 않는지 시험한 뒤 돌렸습니다. 물가·환율·나라별 세금은 넣지 않았습니다. 이 영상의 내레이션은 AI 음성입니다.

■ 자료
일별 종가·분배금: Yahoo Finance 차트 API

■ 알려 드립니다
과거 자료로 계산한 결과이며 앞으로도 같다는 보장은 없습니다. 특정 상품을 매수·매도하라는 이야기가 아니며 투자 권유가 아닙니다.

#커버드콜 #백테스트 #QYLD
```

## 3. 챕터 다시 계산하기 (문장 번호 기준)

```
python tools/srt_tool.py upload stock/source/keobeodeu-kol-2026-10/keobeodeu-kol-2026-10.txt stock/source/keobeodeu-kol-2026-10/keobeodeu-kol-2026-10.srt --chapters "1=커버드콜 분배금, 원금은?;7=2013년부터 날짜를 흘려 보면;35=2022년 긴 하락;51=2024년부터 끝까지;58=13년 결과;67=커버드콜은 어떻게 분배금을 만드나;80=시작한 달을 바꾸면;93=XYLD·JEPI도 같을까;105=세금·다시 매수하면;113=정리;119=이 실험의 한계"
```
- 2026-10-17 추정 시각(오디오 전, 대본 v1.1)으로 "✅ YouTube 챕터 규칙 통과". 업로드 도구가 올릴 때 오디오에 맞춘 SRT로 다시 계산해 2번 설명란에 넣는다.
- 챕터 이름에 결과를 쓰지 않는다.

## 4. 태그

```
커버드콜, 커버드콜 ETF, 분배금, 원금, QYLD, QQQ, XYLD, JEPI, 나스닥100, 월배당, 은퇴 생활비, 백테스트, covered call, backtest, dividend income
```

## 5. 언어별 제목·설명 (localizations)

JSON — 업로드 도구가 그대로 읽는다. 챕터는 넣지 않았다 (시각이 오디오 뒤에 바뀜).

```
{
 "en": {
  "title": "Covered call payouts spent monthly: is more principal left after 13 years than selling QQQ?",
  "description": "Covered call ETFs pay every month and are said to keep your principal. If you spend the payouts every month, is the principal really kept?\nWe put the same $100,000 into a Nasdaq-100 covered call ETF (QYLD) and into QQQ, which follows the same Nasdaq-100. Every time QYLD paid out, we spent all of it; from QQQ we sold the same amount on the same day. Both accounts took out exactly the same cash. December 2013 to October 2026, 0.25% fee per trade, before tax. As the dates roll forward, the two account values, the cash taken out and the principal (one box = $100,000) change in real time.\nChecks: 94 five-year and 118 three-year accounts started in different months, XYLD vs SPY, JEPI vs SPY, 15% withholding tax, and reinvesting the payouts. The code was written by AI and tested for look-ahead bias. Inflation, currency and country taxes are not included. The narration is an AI voice.\nData: Yahoo Finance (daily closes and distributions).\nPast results do not guarantee future returns. This video is for education only and is not investment advice."
 },
 "hi": {
  "title": "कवर्ड कॉल भुगतान हर महीने खर्च करें तो क्या 13 साल बाद QQQ बेचने से ज़्यादा मूलधन बचेगा?",
  "description": "कवर्ड कॉल ETF हर महीने भुगतान देते हैं और कहा जाता है कि मूलधन बचा रहता है। अगर हर महीने भुगतान खर्च करें तो क्या मूलधन सच में बचता है?\nहमने वही $100,000 नैस्डैक-100 कवर्ड कॉल ETF (QYLD) और उसी नैस्डैक-100 को फॉलो करने वाले QQQ में लगाए। QYLD के हर भुगतान को पूरा खर्च किया और QQQ से उसी दिन उतनी ही रकम बेची — दोनों खातों से बिल्कुल बराबर पैसा निकला। दिसंबर 2013 से अक्टूबर 2026, हर सौदे पर 0.25% शुल्क, टैक्स से पहले।\nजाँच: अलग-अलग महीनों में शुरू हुए 5 साल के 94 और 3 साल के 118 खाते, XYLD बनाम SPY, JEPI बनाम SPY, 15% टैक्स, और भुगतान दोबारा निवेश। कोड AI ने लिखा। वॉइस-ओवर AI आवाज़ है।\nडेटा: Yahoo Finance।\nपिछले नतीजे भविष्य की गारंटी नहीं हैं। यह वीडियो केवल शिक्षा के लिए है, निवेश सलाह नहीं।"
 },
 "id": {
  "title": "Dividen covered call dipakai tiap bulan: apakah modal tersisa lebih banyak dari jual QQQ, 13 tahun?",
  "description": "ETF covered call membayar tiap bulan dan katanya modal tetap terjaga. Jika pembayarannya dipakai setiap bulan, apakah modal benar-benar terjaga?\nKami menaruh $100.000 yang sama di ETF covered call Nasdaq-100 (QYLD) dan di QQQ yang mengikuti Nasdaq-100 yang sama. Setiap QYLD membayar, semuanya kami pakai; dari QQQ kami jual jumlah yang sama di hari yang sama. Kedua akun menarik uang yang persis sama. Desember 2013 sampai Oktober 2026, biaya 0,25% per transaksi, sebelum pajak.\nPengecekan: 94 akun 5 tahun dan 118 akun 3 tahun dengan bulan mulai berbeda, XYLD vs SPY, JEPI vs SPY, pajak 15%, dan menginvestasikan kembali pembayaran. Kode ditulis oleh AI. Narasi memakai suara AI.\nData: Yahoo Finance.\nHasil masa lalu tidak menjamin hasil masa depan. Video ini hanya untuk edukasi, bukan saran investasi."
 },
 "pt": {
  "title": "Renda de covered call gasta todo mês: sobra mais capital em 13 anos do que vendendo QQQ?",
  "description": "ETFs de covered call pagam todo mês e dizem que preservam o capital. Se você gastar os pagamentos todo mês, o capital é mesmo preservado?\nColocamos os mesmos US$ 100.000 num ETF de covered call do Nasdaq-100 (QYLD) e no QQQ, que segue o mesmo Nasdaq-100. A cada pagamento do QYLD gastamos tudo; do QQQ vendemos o mesmo valor no mesmo dia. As duas contas retiraram exatamente o mesmo dinheiro. Dezembro de 2013 a outubro de 2026, taxa de 0,25% por operação, antes de impostos.\nVerificações: 94 contas de 5 anos e 118 de 3 anos iniciadas em meses diferentes, XYLD vs SPY, JEPI vs SPY, imposto de 15% e reinvestimento dos pagamentos. O código foi escrito por IA. A narração é uma voz de IA.\nDados: Yahoo Finance.\nResultados passados não garantem resultados futuros. Este vídeo é educativo e não é recomendação de investimento."
 },
 "es-419": {
  "title": "Ingreso de covered call gastado cada mes: ¿queda más capital en 13 años que vendiendo QQQ?",
  "description": "Los ETF de covered call pagan cada mes y dicen que conservan el capital. Si gastas los pagos cada mes, ¿de verdad se conserva el capital?\nPusimos los mismos US$100,000 en un ETF de covered call del Nasdaq-100 (QYLD) y en QQQ, que sigue el mismo Nasdaq-100. Cada vez que QYLD pagó, gastamos todo; de QQQ vendimos el mismo monto el mismo día. Las dos cuentas retiraron exactamente el mismo dinero. Diciembre de 2013 a octubre de 2026, comisión de 0.25% por operación, antes de impuestos.\nComprobaciones: 94 cuentas de 5 años y 118 de 3 años iniciadas en meses distintos, XYLD vs SPY, JEPI vs SPY, impuesto de 15% y reinvertir los pagos. El código lo escribió una IA. La narración es una voz de IA.\nDatos: Yahoo Finance.\nLos resultados pasados no garantizan resultados futuros. Este video es educativo y no es asesoría de inversión."
 },
 "ja": {
  "title": "カバードコールの分配金を毎月使うと、同じ額を売るQQQより13年後に元本は多く残る？",
  "description": "毎月分配金が出て、元本はあまり減らないと言われるカバードコールETF。分配金を毎月使っても、元本は本当に守られるのでしょうか？\n同じ10万ドルを、ナスダック100のカバードコールETF（QYLD）と、同じナスダック100に連動するQQQに入れました。QYLDの分配金は出るたびに全部使い、QQQは同じ日に同じ金額だけ売って使います。2つの口座が引き出したお金は日付も金額も同じです。2013年12月〜2026年10月、売買ごとに手数料0.25%、税引き前。\n確認：開始月を変えた5年口座94個・3年口座118個、XYLD対SPY、JEPI対SPY、源泉徴収15%、分配金を再投資した場合。コードはAIが書きました。ナレーションはAI音声です。\nデータ：Yahoo Finance。\n過去の結果は将来を保証しません。この動画は教育目的であり、投資助言ではありません。"
 },
 "de": {
  "title": "Covered-Call-Ausschüttung monatlich ausgeben: Bleibt nach 13 Jahren mehr als beim QQQ-Verkauf?",
  "description": "Covered-Call-ETFs zahlen jeden Monat aus und sollen das Kapital erhalten. Bleibt das Kapital wirklich erhalten, wenn man die Ausschüttungen jeden Monat ausgibt?\nWir haben dieselben 100.000 $ in einen Nasdaq-100-Covered-Call-ETF (QYLD) und in QQQ angelegt, der denselben Nasdaq-100 abbildet. Jede QYLD-Ausschüttung wurde komplett ausgegeben; bei QQQ wurde am selben Tag derselbe Betrag verkauft. Beide Konten entnahmen genau dasselbe Geld. Dezember 2013 bis Oktober 2026, 0,25 % Gebühr pro Trade, vor Steuern.\nPrüfungen: 94 Fünfjahres- und 118 Dreijahreskonten mit verschiedenen Startmonaten, XYLD vs. SPY, JEPI vs. SPY, 15 % Quellensteuer und Wiederanlage der Ausschüttungen. Den Code hat eine KI geschrieben. Die Sprecherstimme ist eine KI-Stimme.\nDaten: Yahoo Finance.\nVergangene Ergebnisse garantieren keine zukünftigen Renditen. Dieses Video dient nur der Bildung und ist keine Anlageberatung."
 },
 "vi": {
  "title": "Tiêu cổ tức covered call mỗi tháng: sau 13 năm vốn còn nhiều hơn bán QQQ cùng số tiền không?",
  "description": "ETF covered call trả tiền mỗi tháng và được cho là giữ được vốn gốc. Nếu tiêu khoản chi trả mỗi tháng, vốn gốc có thật sự được giữ?\nChúng tôi đặt cùng 100.000 USD vào ETF covered call Nasdaq-100 (QYLD) và vào QQQ, quỹ theo cùng chỉ số Nasdaq-100. Mỗi lần QYLD chi trả, chúng tôi tiêu hết; với QQQ, bán cùng số tiền vào cùng ngày. Hai tài khoản rút ra số tiền giống hệt nhau. Từ tháng 12/2013 đến tháng 10/2026, phí 0,25% mỗi giao dịch, trước thuế.\nKiểm tra: 94 tài khoản 5 năm và 118 tài khoản 3 năm bắt đầu ở các tháng khác nhau, XYLD so với SPY, JEPI so với SPY, thuế 15% và tái đầu tư khoản chi trả. Mã do AI viết. Giọng đọc là giọng AI.\nDữ liệu: Yahoo Finance.\nKết quả quá khứ không đảm bảo tương lai. Video chỉ nhằm mục đích giáo dục, không phải lời khuyên đầu tư."
 },
 "tr": {
  "title": "Covered call dağıtımını her ay harcarsanız 13 yıl sonra QQQ satmaktan fazla anapara kalır mı?",
  "description": "Covered call ETF'leri her ay ödeme yapar ve anaparayı koruduğu söylenir. Ödemeleri her ay harcarsanız anapara gerçekten korunur mu?\nAynı 100.000 doları Nasdaq-100 covered call ETF'si QYLD'ye ve aynı Nasdaq-100'ü izleyen QQQ'ya yatırdık. QYLD her ödeme yaptığında hepsini harcadık; QQQ'dan aynı gün aynı tutarı sattık. İki hesap da tam olarak aynı parayı çekti. Aralık 2013 - Ekim 2026, işlem başına %0,25 komisyon, vergi öncesi.\nKontroller: farklı aylarda başlayan 94 beş yıllık ve 118 üç yıllık hesap, XYLD - SPY, JEPI - SPY, %15 stopaj ve ödemelerin yeniden yatırılması. Kodu yapay zekâ yazdı. Seslendirme yapay zekâ sesidir.\nVeri: Yahoo Finance.\nGeçmiş sonuçlar gelecekteki getirileri garanti etmez. Bu video yalnızca eğitim amaçlıdır, yatırım tavsiyesi değildir."
 }
}
```

## 6. 고정 댓글

```
분배금을 매달 꺼내 쓰는 커버드콜 계좌와, 같은 돈을 꺼낸 지수 계좌 — 13년 뒤 어느 쪽 원금이 더 남을 거라고 생각하셨나요? 지금 쓰고 계신 커버드콜 ETF가 있다면 알려 주세요.
다음에 백테스트로 검증해 볼 가설도 댓글로 남겨 주세요.
(정보 제공용이며 투자 권유가 아닙니다)
```

## 7. 업로드 설정

| 항목 | 값 |
|---|---|
| 공개 상태 | 비공개로 올리고 **1시간 뒤 예약 공개** (`--publish-at +1h`) |
| 썸네일 | `thumbnails/thumbnail_1.*` (본안 — 글자 없음). 공개 뒤 '테스트 및 비교'에 thumbnail_1~3 |
| 기본 언어 | ko |
| 자막 올리기 | **아니요** (전 세계 대상 — 자막을 굽지도 올리지도 않음, 사용자 지시 2026-10-15) |
| 카테고리 | 교육 |
| 동영상 언어 | 한국어 (내레이션) |
| 자동 더빙 | 스튜디오에서 지원 언어가 보이면 켠다 |
| 시청자층 | 아동용 아님 |
| 유료 프로모션 | 없음 |
| 변경되거나 합성된 콘텐츠 | **예** (내레이션이 AI 음성 — 사용자 지시 2026-10-11) |

## 8. 점검

- **결말 없음**: 제목·설명란·챕터·고정 댓글·언어별 제목·설명 어디에도 결과(남은 원금·어느 쪽이 많았는지·배수)를 쓰지 않았다. 결과는 영상 '13년 결과'(s58~)와 각 확인 장 끝에서만.
- 설명란·언어별 설명의 숫자(10만 달러·2013-12·2026-10·0.25%·94·118·5년·3년·15%)는 대본·`backtest/results.json`·`run.py` 설정에 있는 것만 썼다.
- 언어별 제목 100자 이하 · `< >` 없음 — `python tools/youtube_upload.py stock keobeodeu-kol-2026-10 --dry-run` 으로 확인.
- 사다 → 매수, 팔다 → 매도 (설명란의 '매도해서').

## 9. 결과 (업로드 후)
- 영상 ID·예약 공개 시각·올린 언어: `youtube.json` (업로드 도구가 씀)
- 48시간 뒤·7일 뒤: 노출 클릭률, 평균 시청 지속 시간, 시청 지속 그래프에서 크게 떨어지는 장, **나라·언어별 조회수**
