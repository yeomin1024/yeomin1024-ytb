# reobeoriji-2026-10-shorts 업로드 시트 (주식 쇼츠)

버전: v1.0 — 2026-10-18 — 새로 만듦: `shorts.md` v2.1 의 제목 R1 · 설명란(4번) · 언어별 제목·설명(1-1)을 업로드 도구가 읽는 꼴로 옮김 · 자막 언어별 (사용자 지시 2026-10-18 "채권 표현 수정하고 영상 업로드 할 준비해").

기준 파일: 쇼츠 대본 `reobeoriji-2026-10-shorts.txt` (12문장) · SRT 문장 12 / 자막 15 (`align-audio` 로 오디오에 맞춤) · 오디오 `narration.mp3` 60.6초 · 올릴 영상 = `stock/out/reobeoriji-2026-10-shorts/final_1080p.mp4` (이 클라우드 컨테이너에만 — git 에 넣지 않음, 장면 파일·오디오로 다시 만듦)

> 업로드: `python3 tools/youtube_upload.py stock reobeoriji-2026-10-shorts --dry-run` → `--publish-at <시각>` (비공개로 올리고 그 시각에 공개). 롱폼 `reobeoriji-2026-10` 과 **같은 시각에 공개** (`guides/upload_guide.md` 12번). 자막은 한국어 + 9개 언어 = 10개(4,000단위) — 할당량이 모자라면 남은 언어는 `--captions-only` 로 다음 날.
> ※ 연구·교육용 — 투자 권유가 아님.

## 1. 제목 (`shorts.md` R1, `title_fit.py --shorts` 2줄 안)

```
TQQQ 3배 매달 500달러, QQQ보다 훨씬 남을까?
```

## 2. 설명란 (`shorts.md` 4번 그대로)

```
나스닥100을 3배로 따라가는 TQQQ를 오래 모으면 훨씬 많이 남는다고들 하죠. 정말 그런지 AI가 짠 파이썬 코드로 과거 실제 가격을 넣어 백테스트했습니다. 나스닥100을 1배로 따라가는 QQQ, 2배 QLD, 3배 TQQQ를 비교했고, QLD·TQQQ는 1999년엔 없어서 매일 지수의 2배·3배에서 비용을 빼 계산했어요. 1999년부터 세 계좌에 매달 500달러씩, 폭락이 와도 계속 매수했습니다. 2026년까지 넣은 돈은 약 17만 달러. 3배 계좌는 약 1,700만 달러로 1배 약 200만 달러의 8.55배였지만, 2001년에는 넣은 돈의 92.3%를, 2008년에도 89.5%를 잃었어요.
▶ 그 이유와, 처음에 한 번에 넣었다면 어땠을지는 아래 '관련 동영상'에서 — 레버리지 ETF, 닷컴 폭락부터 27년 매달 모으면 QLD·TQQQ가 1배 QQQ보다 더 남을까?

자료·계산 조건(2배·3배 계산 방법, 금리, 수수료 0.25%)은 본편 설명란에 있습니다. 계산 코드는 AI가 짰고, 내레이션은 AI 음성입니다.
과거 자료로 계산한 결과이며 투자 권유가 아닙니다.
#TQQQ #QQQ
```

## 3. 언어별 제목·설명 (`shorts.md` 1-1 그대로 — 9개 언어, 업로드 도구 v1.6 localizations)

```
{
 "en": {
  "title": "$500 a month in 3x TQQQ: far more left than QQQ?",
  "description": "People say saving for years in TQQQ, which tracks the Nasdaq-100 at 3x, leaves far more. To check, we ran a backtest with AI-written Python code on real past prices. We compared QQQ, tracking the Nasdaq-100 at 1x, with 2x QLD and 3x TQQQ; since QLD and TQQQ didn't exist in 1999, we used 2x or 3x the index each day, minus costs. From 1999, each of the three accounts got $500 every month and kept buying even in crashes. By 2026 each had put in about $170,000. The 3x account had about $17,000,000, 8.55 times 1x's about $2,000,000, but in 2001 it lost 92.3% of the money put in, and in 2008, 89.5%.\n▶ Why — and what a single lump sum at the start would have done — in the related video below: Leveraged ETFs from the dot-com crash: buying QLD and TQQQ monthly for 27 years, more than 1x QQQ?\n\nData and full conditions (how 2x and 3x are calculated, interest rates, 0.25% fee) are in the main video's description. The code was written by AI and the narration is an AI voice.\nPast data only — not investment advice.\n#TQQQ #QQQ"
 },
 "hi": {
  "title": "3x TQQQ में हर महीने $500: क्या QQQ से कहीं ज़्यादा बचेगा?",
  "description": "कहते हैं कि नैस्डैक-100 को 3x पर फॉलो करने वाला TQQQ लंबे समय तक जमा करें, तो बहुत ज़्यादा बचता है। यह जाँचने के लिए हमने AI के लिखे Python कोड से पिछली असली कीमतों पर बैकटेस्ट किया। नैस्डैक-100 को 1x पर फॉलो करने वाले QQQ, 2x QLD और 3x TQQQ की तुलना की; QLD·TQQQ 1999 में नहीं थे, इसलिए रोज़ इंडेक्स के 2x·3x में से लागत घटाकर गणना की। 1999 से तीनों खातों में हर महीने $500 डाले और गिरावट में भी खरीदते रहे। 2026 तक हर खाते में लगभग $170,000 डाले गए। 3x खाता लगभग $17,000,000 था, 1x के लगभग $2,000,000 का 8.55 गुना, लेकिन 2001 में उसने लगाए गए पैसे का 92.3% और 2008 में 89.5% गँवाया।\n▶ इसकी वजह, और शुरुआत में एक साथ पूरा पैसा डालते तो क्या होता — नीचे जुड़े वीडियो में: डॉट-कॉम गिरावट से लीवरेज ETF: 27 साल हर महीने QLD·TQQQ खरीदें तो क्या 1x QQQ से ज़्यादा बचेगा?\n\nडेटा और पूरी शर्तें (2x·3x की गणना का तरीका, ब्याज दर, 0.25% शुल्क) मुख्य वीडियो के विवरण में हैं। कोड AI ने लिखा और आवाज़ AI की है।\nसिर्फ़ पिछला डेटा — निवेश सलाह नहीं।\n#TQQQ #QQQ"
 },
 "id": {
  "title": "TQQQ 3x $500 tiap bulan: sisa jauh lebih banyak dari QQQ?",
  "description": "Katanya menabung TQQQ, yang mengikuti Nasdaq-100 dengan 3x, lama-lama menyisakan jauh lebih banyak. Untuk mengeceknya, kami melakukan backtest dengan kode Python buatan AI pada harga riil masa lalu. Kami bandingkan QQQ yang mengikuti Nasdaq-100 dengan 1x, QLD 2x, dan TQQQ 3x; karena QLD dan TQQQ belum ada di 1999, keduanya dihitung dari 2x dan 3x indeks tiap hari, dikurangi biaya. Sejak 1999, ketiga akun diisi $500 tiap bulan dan terus membeli walau pasar anjlok. Sampai 2026 uang yang masuk sekitar $170.000. Akun 3x sekitar $17.000.000, 8,55 kali akun 1x yang sekitar $2.000.000, tapi pada 2001 kehilangan 92,3% dari uang yang masuk, dan pada 2008 juga 89,5%.\n▶ Alasannya, dan bagaimana jika semua uang masuk sekaligus di awal — di video tertaut di bawah: ETF leverage sejak krisis dot-com: beli QLD·TQQQ tiap bulan 27 tahun, sisa lebih dari 1x QQQ?\n\nData dan syarat lengkap (cara menghitung 2x dan 3x, suku bunga, biaya 0,25%) ada di deskripsi video utama. Kode ditulis AI dan narasinya suara AI.\nHanya data masa lalu — bukan saran investasi.\n#TQQQ #QQQ"
 },
 "pt": {
  "title": "US$ 500 por mês no TQQQ 3x: sobra muito mais que no QQQ?",
  "description": "Dizem que acumular TQQQ, que segue o Nasdaq-100 em 3x, por anos deixa muito mais. Para conferir, fizemos um backtest com código Python escrito por IA sobre preços reais do passado. Comparamos o QQQ, que segue o Nasdaq-100 em 1x, com o QLD 2x e o TQQQ 3x; como QLD e TQQQ não existiam em 1999, usamos 2x ou 3x o índice a cada dia, menos os custos. Desde 1999, as três contas receberam US$ 500 por mês e seguiram comprando mesmo nos crashes. Até 2026, cada uma aplicou cerca de US$ 170.000. A conta 3x teve cerca de US$ 17.000.000, 8,55 vezes os cerca de US$ 2.000.000 da 1x, mas em 2001 perdeu 92,3% do valor aplicado e, em 2008, 89,5%.\n▶ O porquê, e como seria aplicar tudo de uma vez no início — no vídeo vinculado abaixo: ETFs alavancados desde a bolha pontocom: comprar QLD e TQQQ todo mês por 27 anos rende mais que QQQ?\n\nDados e condições completas (como 2x e 3x são calculados, juros, taxa de 0,25%) na descrição do vídeo principal. O código foi escrito por IA e a narração é voz de IA.\nApenas dados passados — não é recomendação de investimento.\n#TQQQ #QQQ"
 },
 "es-419": {
  "title": "US$500 al mes en TQQQ 3x: ¿queda mucho más que en QQQ?",
  "description": "Dicen que acumular TQQQ, que sigue al Nasdaq-100 a 3x, por años deja mucho más. Para comprobarlo, hicimos un backtest con código Python escrito por IA sobre precios reales del pasado. Comparamos QQQ, que sigue al Nasdaq-100 a 1x, con QLD 2x y TQQQ 3x; como QLD y TQQQ no existían en 1999, usamos 2x o 3x el índice cada día, menos costos. Desde 1999, las tres cuentas recibieron US$500 al mes y siguieron comprando aun en los desplomes. Hasta 2026, cada una invirtió unos US$170,000. La cuenta 3x tuvo unos US$17,000,000: 8.55 veces la 1x, con unos US$2,000,000; pero en 2001 perdió el 92.3% de lo invertido y en 2008, el 89.5%.\n▶ El porqué, y qué habría pasado invirtiendo todo de una vez al inicio — en el video vinculado abajo: ETF apalancados desde la burbuja puntocom: ¿comprar QLD y TQQQ cada mes 27 años deja más que QQQ?\n\nDatos y condiciones completas (cómo se calculan 2x y 3x, tasas de interés, comisión de 0.25%) en la descripción del video principal. El código lo escribió una IA y la narración es una voz de IA.\nSolo datos pasados — no es asesoría de inversión.\n#TQQQ #QQQ"
 },
 "ja": {
  "title": "TQQQ 3倍に毎月500ドル、QQQよりずっと多く残る？",
  "description": "ナスダック100を3倍で追うTQQQを長く積み立てれば、ずっと多く残ると言われます。本当かどうか、AIが書いたPythonコードで過去の実際の価格を使ってバックテストしました。ナスダック100を1倍で追うQQQ、2倍のQLD、3倍のTQQQを比べ、QLD・TQQQは1999年にはなかったので、毎日指数の2倍・3倍からコストを引いて計算しました。1999年から三つの口座に毎月500ドルずつ、暴落が来ても買い続けました。2026年までに入れた額は約17万ドル。3倍の口座は約1,700万ドルで1倍の約200万ドルの8.55倍でしたが、2001年には入れたお金の92.3%を、2008年にも89.5%を失いました。\n▶ その理由と、最初に一度に入れていたらどうだったかは下のリンクの動画で — レバレッジETF、ITバブル崩壊から27年毎月積み立てると、QLD・TQQQは1倍のQQQより多く残る？\n\nデータと計算条件（2倍・3倍の計算方法・金利・手数料0.25%）は本編の説明欄にあります。計算コードはAIが書き、ナレーションはAI音声です。\n過去データによる計算で、投資の勧誘ではありません。\n#TQQQ #QQQ"
 },
 "de": {
  "title": "Monatlich 500 $ in TQQQ 3x: Bleibt viel mehr als bei QQQ?",
  "description": "Es heißt, TQQQ, der den Nasdaq-100 mit 3x abbildet, bringt lange bespart viel mehr. Zur Prüfung haben wir mit von KI geschriebenem Python-Code einen Backtest auf echten historischen Kursen gemacht. Verglichen wurden QQQ, der den Nasdaq-100 mit 1x abbildet, QLD mit 2x und TQQQ mit 3x; da es QLD und TQQQ 1999 noch nicht gab, wurde täglich mit 2x bzw. 3x des Index minus Kosten gerechnet. Ab 1999 bekam jedes der drei Konten monatlich 500 $ und kaufte auch in Crashs weiter. Bis 2026 wurden je rund 170.000 $ eingezahlt. Das 3x-Konto hatte rund 17.000.000 $, das 8,55-Fache von 1x mit rund 2.000.000 $, verlor aber 92,3 % des eingezahlten Geldes im Jahr 2001 und 89,5 % im Jahr 2008.\n▶ Warum – und was eine Einmalanlage am Anfang gebracht hätte – im verlinkten Video unten: Hebel-ETFs ab dem Dotcom-Crash: QLD und TQQQ 27 Jahre monatlich kaufen – mehr als 1x QQQ?\n\nDaten und alle Bedingungen (Berechnung von 2x und 3x, Zinsen, 0,25 % Gebühr) in der Beschreibung des Hauptvideos. Der Code wurde von einer KI geschrieben, die Stimme ist eine KI-Stimme.\nNur historische Daten – keine Anlageberatung.\n#TQQQ #QQQ"
 },
 "vi": {
  "title": "Mỗi tháng 500 USD vào TQQQ 3x: còn nhiều hơn hẳn QQQ không?",
  "description": "Người ta nói tích lũy lâu TQQQ, quỹ gấp 3 lần Nasdaq-100, sẽ còn nhiều hơn hẳn. Để kiểm tra, chúng tôi chạy backtest bằng mã Python do AI viết trên giá thực tế trong quá khứ. Chúng tôi so sánh QQQ bám theo Nasdaq-100 ở mức 1x, QLD 2x và TQQQ 3x; năm 1999 chưa có QLD, TQQQ nên tính mỗi ngày gấp 2, 3 lần chỉ số rồi trừ chi phí. Từ năm 1999, ba tài khoản đều bỏ vào 500 USD mỗi tháng và vẫn mua tiếp dù thị trường sập. Đến năm 2026, mỗi tài khoản đã bỏ vào khoảng 170.000 USD. Tài khoản 3x khoảng 17.000.000 USD, gấp 8,55 lần 1x khoảng 2.000.000 USD, nhưng năm 2001 đã mất 92,3% số tiền bỏ vào, năm 2008 cũng mất 89,5%.\n▶ Lý do, và nếu bỏ hết tiền một lần từ đầu thì sẽ ra sao — xem ở video liên kết bên dưới: ETF đòn bẩy từ bong bóng dot-com: mua QLD, TQQQ mỗi tháng suốt 27 năm có hơn QQQ 1x không?\n\nDữ liệu và điều kiện đầy đủ (cách tính 2x và 3x, lãi suất, phí 0,25%) trong phần mô tả video chính. Mã do AI viết, lời thuyết minh là giọng AI.\nChỉ là dữ liệu quá khứ — không phải lời khuyên đầu tư.\n#TQQQ #QQQ"
 },
 "tr": {
  "title": "TQQQ 3x'e her ay 500 $: QQQ'dan çok daha fazla kalır mı?",
  "description": "Nasdaq-100'ü 3x izleyen TQQQ uzun süre biriktirilirse çok daha fazla kaldığı söylenir. Bunu kontrol etmek için yapay zekânın yazdığı Python koduyla geçmişteki gerçek fiyatlar üzerinde backtest yaptık. Nasdaq-100'ü 1x izleyen QQQ'yu, 2x QLD ve 3x TQQQ ile karşılaştırdık; QLD ve TQQQ 1999'da olmadığı için her gün endeksin 2x ve 3x'inden maliyet düşerek hesapladık. 1999'dan itibaren üç hesaba her ay 500 $ koyduk ve çöküşlerde bile almaya devam ettik. 2026'ya kadar her hesaba yaklaşık 170.000 $ kondu. 3x hesapta yaklaşık 17.000.000 $ vardı; 1x'teki yaklaşık 2.000.000 $'ın 8,55 katı. Ama 2001'de yatırılan paranın %92,3'ünü, 2008'de de %89,5'ini kaybetti.\n▶ Nedeni ve başta paranın hepsini bir kerede koysaydık ne olacağı aşağıdaki bağlantılı videoda: Dotcom çöküşünden kaldıraçlı ETF: 27 yıl her ay QLD ve TQQQ almak 1x QQQ'dan fazla bırakır mı?\n\nVeriler ve tüm koşullar (2x ve 3x hesaplama yöntemi, faiz, %0,25 komisyon) ana videonun açıklamasında. Kodu yapay zekâ yazdı, seslendirme yapay zekâ sesi.\nYalnızca geçmiş veriler — yatırım tavsiyesi değildir.\n#TQQQ #QQQ"
 }
}
```

## 4. 태그

```
TQQQ, QQQ, QLD, 레버리지 ETF, 3배 레버리지, 나스닥100, 적립식, 백테스트, leveraged ETF, backtest
```

## 6. 업로드 설정

| 항목 | 값 |
|---|---|
| 공개 범위 | 비공개로 올리고 예약 시각에 공개 (`--publish-at`) — 롱폼과 같은 시각 |
| 기본 언어 | ko |
| 자막 올리기 | **언어별** (한국어 `reobeoriji-2026-10-shorts.srt` + `subs/reobeoriji-2026-10-shorts.<언어>.srt` 9개 — 화면에는 굽지 않음, `stock/guides/README.md` v1.24 4번) |
| 변경되거나 합성된 콘텐츠 | **예** (내레이션이 AI 음성 — CLAUDE.md) |
| 카테고리 | 교육 |
| 썸네일 | `thumbnails/thumbnail_1.png` (세로 9:16 — 그림이 화면 끝까지) → 도구가 세로 720×1280 JPG 로 올림 · 0초 장면도 같은 그림 · 공개 뒤 `i.ytimg.com/vi/<ID>/oardefault.jpg` 로 확인 |
| 관련 동영상 | 롱폼 `reobeoriji-2026-10` 「레버리지 ETF, 닷컴 폭락부터 27년 매달 모으면 QLD·TQQQ가 1배 QQQ보다 더 남을까?」 (`../youtube.json`) — 스튜디오 → 콘텐츠 → Shorts → 연필 → '관련 동영상' (API 로 못 검 — 사용자가 직접) |
| 자동 더빙 | 스튜디오에서 지원 언어가 보이면 켠다 |

## 7. 결과 (업로드 후)
- (올린 뒤 `youtube.json` 의 영상 ID·예약 시각·자막 언어를 적는다)
