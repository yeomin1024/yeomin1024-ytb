# eonje-maesu-2026-10 업로드 시트

버전: v2.1 — 2026-10-16 — 대본 v2.1(도입 + 같은 조건을 6문장 약 20초로 · 사다/팔다 → 매수/매도 — 사용자 지시 2026-10-16 "메인인 실시간 비교 전 도입부가 너무 길어 20초 안으로 다 설명하게 해" · "내가 말한 도입은 도입 + 규칙 설명이야 무리면 적어도 30초안에는 끝내도록 해")에 맞춰 챕터 다시 (예전 '같은 조건' 챕터 없앰). 제목·설명·언어별은 그대로.
(v2.0 — 2026-10-16 — 다시 만듦 (매수 신호 10가지 × 같은 매도 규칙 '산 뒤 최고 종가 −10% → 다음 날 매도' · SPY 총수익 2016-01-04~2026-10-15 · 수수료 0.25% — `backtest/run.py` v3.0). `guides/upload_guide.md` 8번 형식 + `stock/guides/README.md` 2·4번: 결말 없음, 언어별 제목·설명, 자막 올리지 않음.
(v1.0 — 매수 규칙 10가지 vs 관망 32년 — `stock/source/_old/eonje-maesu-2026-10-v1/upload.md`)
기준 파일: 대본 v2.1 (108문장) · SRT 문장 108 (추정 시각 — 오디오가 생기면 align-audio 로 다시) · 결과 `backtest/results.json` (`run.py` v3.0) · 올릴 영상 = 렌더 원본 `stock/out/eonje-maesu-2026-10/final_1080p.mp4` (오디오가 생긴 뒤 — 지금 있는 `preview_estimated_silent.mp4` 는 소리 없는 미리보기라 올리지 않음)

> 업로드: 이 클라우드 환경의 키(= STOCK LAB 채널, `stock/youtube_channel.json` — 업로드 도구 v1.7 이 채널이 다르면 올리지 않음)로 `python tools/youtube_upload.py stock eonje-maesu-2026-10 --publish-at +1h` — 비공개 업로드 + **1시간 뒤 예약 공개**. PC 업로더(`run_uploader.ps1 -Topic stock`)도 같은 시트를 쓴다.
> 연구·교육용 콘텐츠 — 투자 권유가 아님.

## 1. 제목 (`titles.md` R1, 한국어 — 기본 언어)

```
매수 타이밍, 저점·RSI·200일선 등 매수 신호 10가지 중 1만 달러로 10년 뒤 가장 많이 번 건?
```

## 2. 설명란 (한국어 — 그대로 복사)

```
"주식은 언제 매수해야 할까?" 쌀 때, 공포가 클 때, 신고가를 뚫을 때… 답이 사람마다 다릅니다.
많이 쓰는 매수 신호 10가지를 같은 조건으로 붙여 봤습니다. 같은 1만 달러, 같은 매도 규칙(산 뒤 가장 높았던 종가보다 10% 떨어지면 다음 날 매도), 2016년 1월부터 2026년 10월까지 SPY.
날짜가 흐르며 각 신호가 언제 매수(BUY)하고 언제 매도(SELL)했는지, 첫날 사서 그대로 둔 계좌(BUY & HOLD)와 함께 3D 차트로 확인합니다.

■ 챕터
0:00 언제 매수할까
0:25 1 매달 첫 거래일
1:11 2 52주 신고가 돌파
1:50 3 12개월 모멘텀
2:28 4 200일 이동평균선
3:05 5 골든 크로스
3:39 6 하루 −2% 급락 다음 날
4:11 7 RSI 30 아래
4:45 8 공포지수 VIX 30 이상
5:20 9 고점 −20%
6:00 10 고점 −10%
6:43 10가지 결과
7:46 매도 기준을 바꾸면
8:02 정리
8:31 이 실험의 한계

■ 시험한 매수 신호 10가지
1 매달 첫 거래일 / 2 52주 신고가 돌파 / 3 12개월 모멘텀(1년 전 종가보다 높으면) / 4 200일 이동평균선 위로 돌파 / 5 골든 크로스 50·200일 / 6 하루 −2% 급락 다음 날 / 7 RSI(14) 30 아래 / 8 공포지수 VIX 30 이상 / 9 고점보다 20% 아래 / 10 고점보다 10% 아래
신호의 숫자는 교과서 기본값이며, 결과를 보고 바꾸지 않았습니다.

■ 실험 방법
자료: SPY(S&P 500 ETF) 일별 종가와 배당(배당은 다시 투자), 2016-01-04 ~ 2026-10-15. 시작 돈 1만 달러 — 10가지 모두 같고, 더 넣거나 빼지 않습니다.
신호는 그날 종가까지만 보고, 매수는 다음 거래일 종가. 매도는 10가지 모두 같습니다: 산 뒤 가장 높았던 종가보다 10% 떨어진 날의 종가를 보고, 다음 거래일 종가에 전부 매도. 판 뒤 신호가 다시 나오면 다시 매수.
사고팔 때마다 수수료 0.25% (국내 증권사 미국 주식 온라인 기본 수수료 수준). 현금 이자는 0.
확인용으로 매도 기준 5·15·20%, 수수료 0.07%·0, 현금에 단기 국채 이자, 배당을 뺀 가격만으로도 다시 계산했습니다.
계산 코드는 AI가 짰고, 미래 가격을 쓰지 않는지와 따로 쓴 계산과 같은 답이 나오는지 시험한 뒤 돌렸습니다.
세금·환전 비용은 넣지 않았습니다. 이 영상의 내레이션은 AI 음성입니다.

■ 자료
SPY·VIX·13주 국채 금리(^IRX) 일별: Yahoo Finance 차트 API · 확인: FRED SP500(S&P 500 지수), github.com/datasets/finance-vix(VIX)

■ 알려 드립니다
과거 자료로 계산한 결과이며 앞으로도 같다는 보장은 없습니다. 특정 상품을 매수하라는 이야기가 아니며 투자 권유가 아닙니다.

#매수타이밍 #백테스트 #SPY
```

## 3. 챕터 다시 계산하기 (문장 번호 기준)

```
python tools/srt_tool.py upload stock/source/eonje-maesu-2026-10/eonje-maesu-2026-10.txt stock/source/eonje-maesu-2026-10/eonje-maesu-2026-10.srt --chapters "1=언제 매수할까;7=1 매달 첫 거래일;16=2 52주 신고가 돌파;24=3 12개월 모멘텀;32=4 200일 이동평균선;39=5 골든 크로스;47=6 하루 −2% 급락 다음 날;54=7 RSI 30 아래;61=8 공포지수 VIX 30 이상;67=9 고점 −20%;74=10 고점 −10%;82=10가지 결과;94=매도 기준을 바꾸면;98=정리;103=이 실험의 한계"
```
- 2026-10-16 추정 시각(오디오 전)으로 "✅ YouTube 챕터 규칙 통과". 업로드 도구가 올릴 때 오디오에 맞춘 SRT로 다시 계산해 2번 설명란에 넣는다.
- 챕터 이름에 결과를 쓰지 않는다 (진행 막대에 미리 보이므로). 번호는 영상에 나오는 순서 (장 카드의 노란 번호와 같음).

## 4. 태그

```
매수 타이밍, 매수 신호, 저점 매수, RSI, 200일 이동평균선, 골든크로스, 52주 신고가, 모멘텀, 공포지수, VIX, 매달 매수, 트레일링 스탑, 백테스트, SPY, S&P500, buy signal, backtest
```

## 5. 언어별 제목·설명 (localizations)

`stock/guides/README.md` 2번의 9개 언어 (기본 언어 ko 는 1·2번). JSON — 업로드 도구가 그대로 읽는다 (고칠 때 따옴표·쉼표 주의). 챕터는 넣지 않았다 (시각이 오디오 뒤에 바뀜). 만든 스크립트가 제목 100자 이하·`< >` 없음을 확인했다.

```
{
 "en": {
  "title": "When to buy: dip, RSI, 200-day line... which of 10 buy signals grew $10,000 the most in 10 years?",
  "description": "\"When should I buy stocks?\" When it's cheap, when fear is high, when it breaks a new high... everyone has a different answer.\nWe put 10 popular buy signals through the same test: the same $10,000, the same sell rule (sell the next day once the close falls 10% below the highest close since buying), SPY from January 2016 to October 2026 with dividends reinvested. A 3D chart shows when each signal bought (BUY) and sold (SELL), next to an account that bought on day one and held (BUY & HOLD).\n\nSignals: first trading day of each month, 52-week high breakout, 12-month momentum, 200-day moving average breakout, 50/200 golden cross, the day after a 2% drop, RSI(14) below 30, VIX at 30 or above, 20% below the high, 10% below the high. Textbook settings, not tuned to the results.\nSignals use closes up to that day; buys happen at the next day's close; 0.25% fee per trade; no interest on cash (also checked with 5/15/20% sell levels, 0.07% and zero fees, T-bill interest, and price only). The backtest code was written by AI and tested for look-ahead bias and against an independent calculation. Taxes and currency costs are not included. The narration is an AI voice.\nData: Yahoo Finance (SPY, ^VIX, ^IRX daily), checked against FRED SP500 and datasets/finance-vix.\nPast results do not guarantee future returns. This video is for education only and is not investment advice."
 },
 "hi": {
  "title": "कब खरीदें: डिप, RSI, 200-दिन औसत... 10 खरीद संकेतों में से किसने $10,000 को सबसे ज़्यादा बढ़ाया?",
  "description": "\"शेयर कब खरीदें?\" सस्ता होने पर, डर ज़्यादा होने पर, नया हाई टूटने पर... हर किसी का जवाब अलग है।\nहमने 10 लोकप्रिय खरीद संकेतों को एक ही तरह परखा: वही $10,000, वही बिक्री नियम (खरीद के बाद के सबसे ऊँचे बंद भाव से 10% गिरते ही अगले दिन बेचना), जनवरी 2016 से अक्टूबर 2026 तक SPY, डिविडेंड दोबारा निवेश के साथ। हर सौदे पर 0.25% शुल्क, नकद पर ब्याज नहीं। कोड AI ने लिखा और भविष्य के डेटा व अलग गणना से जाँचा। टैक्स और मुद्रा खर्च शामिल नहीं। वॉइस-ओवर AI आवाज़ है।\nडेटा: Yahoo Finance (SPY, ^VIX, ^IRX), जाँच: FRED SP500, datasets/finance-vix।\nपिछले नतीजे भविष्य की गारंटी नहीं हैं। यह वीडियो केवल शिक्षा के लिए है, निवेश सलाह नहीं।"
 },
 "id": {
  "title": "Kapan beli: dip, RSI, MA200... dari 10 sinyal beli, mana yang paling menumbuhkan $10.000?",
  "description": "\"Kapan sebaiknya beli saham?\" Saat murah, saat pasar takut, saat menembus rekor... jawabannya berbeda-beda.\nKami menguji 10 sinyal beli populer dengan syarat yang sama: $10.000 yang sama, aturan jual yang sama (jual esok hari begitu harga penutupan turun 10% dari penutupan tertinggi sejak beli), SPY Januari 2016 sampai Oktober 2026 dengan dividen diinvestasikan kembali. Biaya 0,25% per transaksi, tanpa bunga kas. Kode ditulis oleh AI dan diuji terhadap look-ahead bias serta perhitungan terpisah. Pajak dan biaya kurs tidak dihitung. Narasi memakai suara AI.\nData: Yahoo Finance (SPY, ^VIX, ^IRX), dicek dengan FRED SP500 dan datasets/finance-vix.\nHasil masa lalu tidak menjamin hasil masa depan. Video ini hanya untuk edukasi, bukan saran investasi."
 },
 "pt": {
  "title": "Quando comprar: queda, RSI, MM200... qual de 10 sinais de compra rendeu mais com US$ 10 mil?",
  "description": "\"Quando devo comprar ações?\" Quando está barato, quando o medo é grande, quando rompe a máxima... cada um tem uma resposta.\nTestamos 10 sinais de compra populares nas mesmas condições: os mesmos US$ 10.000, a mesma regra de venda (vender no dia seguinte quando o fechamento cai 10% abaixo do maior fechamento desde a compra), SPY de janeiro de 2016 a outubro de 2026 com dividendos reinvestidos. Taxa de 0,25% por operação, sem juros no caixa. O código foi escrito por IA e testado contra viés de antecipação e um cálculo independente. Impostos e câmbio não foram incluídos. A narração é uma voz de IA.\nDados: Yahoo Finance (SPY, ^VIX, ^IRX), conferidos com FRED SP500 e datasets/finance-vix.\nResultados passados não garantem resultados futuros. Este vídeo é educativo e não é recomendação de investimento."
 },
 "es-419": {
  "title": "¿Cuándo comprar? Caída, RSI, MM200... ¿cuál de 10 señales de compra rindió más con US$10.000?",
  "description": "\"¿Cuándo debo comprar acciones?\" Cuando está barato, cuando hay mucho miedo, cuando rompe un máximo... cada quien tiene su respuesta.\nProbamos 10 señales de compra populares con las mismas condiciones: los mismos US$10,000, la misma regla de venta (vender al día siguiente cuando el cierre cae 10% por debajo del cierre más alto desde la compra), SPY de enero de 2016 a octubre de 2026 con dividendos reinvertidos. Comisión de 0.25% por operación, sin intereses en efectivo. El código lo escribió una IA y se probó contra el sesgo de anticipación y un cálculo independiente. No incluye impuestos ni costos de cambio. La narración es una voz de IA.\nDatos: Yahoo Finance (SPY, ^VIX, ^IRX), revisados con FRED SP500 y datasets/finance-vix.\nLos resultados pasados no garantizan resultados futuros. Este video es educativo y no es asesoría de inversión."
 },
 "ja": {
  "title": "買うタイミング：押し目・RSI・200日線など買いシグナル10個、1万ドルで10年後に一番増えたのは？",
  "description": "「株はいつ買えばいい？」安いとき、恐怖が大きいとき、高値を抜けたとき…答えは人それぞれです。\nよく使われる買いシグナル10個を同じ条件で試しました。同じ1万ドル、同じ売りルール（買った後の最高終値から10%下がったら翌日に売る）、2016年1月から2026年10月までのSPY（配当再投資）。売買ごとに手数料0.25%、現金の利息は0。コードはAIが書き、未来の情報を使っていないか・別の計算と一致するかを確認しました。税金・為替コストは含みません。ナレーションはAI音声です。\nデータ：Yahoo Finance（SPY、^VIX、^IRX）、確認：FRED SP500、datasets/finance-vix。\n過去の結果は将来を保証しません。この動画は教育目的であり、投資助言ではありません。"
 },
 "de": {
  "title": "Wann kaufen: Dip, RSI, 200-Tage-Linie… welches von 10 Kaufsignalen machte am meisten aus 10.000 $?",
  "description": "„Wann soll ich Aktien kaufen?“ Wenn es billig ist, wenn die Angst groß ist, wenn ein neues Hoch fällt … jeder antwortet anders.\nWir haben 10 beliebte Kaufsignale unter denselben Bedingungen getestet: dieselben 10.000 US-Dollar, dieselbe Verkaufsregel (am nächsten Tag verkaufen, sobald der Schlusskurs 10 % unter den höchsten Schlusskurs seit dem Kauf fällt), SPY von Januar 2016 bis Oktober 2026 mit reinvestierten Dividenden. 0,25 % Gebühr pro Trade, keine Zinsen auf Bargeld. Den Code hat eine KI geschrieben; er wurde auf Look-ahead-Bias und gegen eine unabhängige Rechnung geprüft. Steuern und Wechselkosten sind nicht enthalten. Die Sprecherstimme ist eine KI-Stimme.\nDaten: Yahoo Finance (SPY, ^VIX, ^IRX), geprüft mit FRED SP500 und datasets/finance-vix.\nVergangene Ergebnisse garantieren keine zukünftigen Renditen. Dieses Video dient nur der Bildung und ist keine Anlageberatung."
 },
 "vi": {
  "title": "Khi nào nên mua: giảm sâu, RSI, MA200... tín hiệu nào trong 10 tín hiệu mua lãi nhất với 10.000 USD?",
  "description": "\"Khi nào nên mua cổ phiếu?\" Khi rẻ, khi thị trường sợ hãi, khi vượt đỉnh mới... mỗi người một câu trả lời.\nChúng tôi thử 10 tín hiệu mua phổ biến với cùng điều kiện: cùng 10.000 USD, cùng quy tắc bán (bán vào ngày hôm sau khi giá đóng cửa giảm 10% so với giá đóng cửa cao nhất kể từ khi mua), SPY từ tháng 1/2016 đến tháng 10/2026 có tái đầu tư cổ tức. Phí 0,25% mỗi giao dịch, tiền mặt không có lãi. Mã do AI viết và đã được kiểm tra lỗi dùng dữ liệu tương lai cũng như so với một phép tính độc lập. Chưa tính thuế và chi phí đổi tiền. Giọng đọc là giọng AI.\nDữ liệu: Yahoo Finance (SPY, ^VIX, ^IRX), đối chiếu với FRED SP500 và datasets/finance-vix.\nKết quả quá khứ không đảm bảo tương lai. Video chỉ nhằm mục đích giáo dục, không phải lời khuyên đầu tư."
 },
 "tr": {
  "title": "Ne zaman almalı: düşüş, RSI, MA200... 10 alım sinyalinden hangisi 10.000 $'ı en çok büyüttü?",
  "description": "\"Hisse ne zaman alınmalı?\" Ucuzken, korku büyükken, yeni zirve kırılınca... herkesin cevabı farklı.\n10 popüler alım sinyalini aynı koşullarla test ettik: aynı 10.000 dolar, aynı satış kuralı (kapanış, alımdan sonraki en yüksek kapanışın %10 altına düşünce ertesi gün sat), Ocak 2016'dan Ekim 2026'ya kadar temettüleri yeniden yatırılan SPY. İşlem başına %0,25 komisyon, nakitte faiz yok. Kodu yapay zekâ yazdı; geleceğe bakma hatasına ve bağımsız bir hesaba karşı test edildi. Vergi ve kur maliyetleri dahil değildir. Seslendirme yapay zekâ sesidir.\nVeri: Yahoo Finance (SPY, ^VIX, ^IRX), FRED SP500 ve datasets/finance-vix ile kontrol edildi.\nGeçmiş sonuçlar gelecekteki getirileri garanti etmez. Bu video yalnızca eğitim amaçlıdır, yatırım tavsiyesi değildir."
 }
}
```

## 6. 고정 댓글

```
10가지 매수 신호 가운데, 영상을 보기 전에는 어느 것이 1위일 거라고 생각하셨나요? 지금 쓰고 계신 신호가 있다면 몇 번인지도 알려 주세요.
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
| 자동 더빙 | 스튜디오에서 지원 언어가 보이면 켠다 (전 세계 대상) |
| 시청자층 | 아동용 아님 |
| 유료 프로모션 | 없음 |
| 변경되거나 합성된 콘텐츠 | **예** (내레이션이 AI 음성 — 사용자 지시 2026-10-11) |

## 8. 점검

- **결말 없음**: 제목·설명란·챕터·고정 댓글·언어별 제목·설명 어디에도 결과(1위가 무엇인지·끝 값·BUY & HOLD 를 넘은 수)를 쓰지 않았다. 결과는 영상 각 장의 끝과 '10가지 결과'(s82~)에서만.
- 설명란·언어별 설명의 숫자(1만 달러·2016-01-04·2026-10-15·10%·0.25%·5·15·20%·0.07%·52주·12개월·200일·50·−2%·14·30·20%)는 대본·`backtest/results.json`·`run.py` 설정에 있는 것만 썼다.
- 제목 59자 · 언어별 제목 51~100자 (모두 100자 이하) · `< >` 없음 — `python tools/youtube_upload.py stock eonje-maesu-2026-10 --dry-run` 으로 확인.
- 사다 → 매수, 팔다 → 매도.

## 9. 결과 (업로드 후)
- 영상 ID·예약 공개 시각·올린 언어: `youtube.json` (업로드 도구가 씀)
- 48시간 뒤·7일 뒤: 노출 클릭률, 평균 시청 지속 시간, 시청 지속 그래프에서 크게 떨어지는 장(1~10), **나라·언어별 조회수**
