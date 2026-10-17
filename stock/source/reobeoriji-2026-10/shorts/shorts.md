# 쇼츠 — `reobeoriji-2026-10` 결과를 바로 보여 주는 쇼츠 (왜 → 어떻게 → 비교 상대 → 조건 → 결과 → 왜? → 롱폼 · 언어 없는 화면)

버전: v2.1 — 2026-10-17 — **결과형 + 왜·어떻게** (2번 커버드콜 쇼츠 v2.1 과 같은 꼴 — 사용자 지시 2026-10-17 "R1으로 하고 나머지 3개도 수정하고 외국어 자막 대본도 필요하지? 쇼츠, 롱폼 각각 언어별로 작성해봐" · 그 앞 "그래 왜 그런 테스트 했는지 언급을 해줘야 할 거 아니야 … 파이썬 코드로 테스트를 해봤습니다 이렇게 무슨 방법으로 테스트했는지도 말해야지 … 니가 아무것도 모르는 시청자 입장이 되보라고"): 대본 12문장 — 왜(시험할 말) → 어떻게(AI가 짠 파이썬 코드 · 과거 실제 가격 · 백테스트 — 화면에 코드 카드) → 비교 상대와 까닭 → 조건 → 결과 → 왜? → 롱폼에만 있는 것. 제목 R1·R2 = 시험할 말(2줄). 9개 언어 제목·설명 다시 · 언어별 자막 대본 `subs/` (화면에 굽지 않고 CC 로 올림).
(v1.0.6 까지 — 프롤로그형(첫 문장 2001년 넣은 돈의 92.3% → 닷컴 → 2008 −89.5% → '세 계좌의 결과는 아래 영상') — 결말 가림, 커밋 9b8be2b5.)

- 보내는 곳(롱폼): **레버리지 ETF, 닷컴 폭락부터 27년 매달 모으면 QLD·TQQQ가 1배 QQQ보다 더 남을까?** (`../upload.md` 1번 제목) — 쇼츠의 '관련 동영상'으로 연결 (롱폼 공개 뒤)
- **쇼츠에서 말하는 것:** (왜) 나스닥100을 3배로 따라가는 TQQQ를 오래 모으면 훨씬 많이 남는다는 말을 확인하려고 · (어떻게) AI가 짠 파이썬 코드에 과거 실제 가격을 넣은 백테스트, 1배 QQQ · 2배 QLD · 3배 TQQQ, QLD·TQQQ 는 1999년엔 없어서 매일 지수의 2배·3배에서 비용을 빼 계산, 1999년부터 매달 500달러씩 똑같이, 폭락이 와도 계속 매수 · (결과) 넣은 돈 약 17만 달러 · 3배 약 1,700만 달러 = 1배 약 200만 달러의 8.55배 · 하지만 2001년 넣은 돈의 92.3%, 2008년 89.5% 를 잃음.
- **롱폼에만 남기는 것 (더 보고 싶은 사람에게):** 날짜별 과정(2003·2009·2023 반등 · 2013년 7월 3배가 1배를 앞섬 · 코로나 · 2022년 −80.9%) · 이유(매일 배수를 맞추면 오르내릴수록 깎임 — 10% 오르고 10% 떨어진 예) · 처음에 한 번에 넣었다면(3배가 1배의 11.4%) · 시작 달을 바꾼 10년 계좌 211개 · 실제 ETF 확인 · 한계. 쇼츠 끝 문장이 '그 이유와, 처음에 한 번에 넣었다면 어땠을지는'을 부르고 끝 화면이 그림 둘(매일 오르내림 ? · 한 번에 넣기 ?)로 보여 준다.
- 근거: [`stock/guides/shorts_insights.md`](../../../guides/shorts_insights.md) v1.1 (주식 성공 경주 쇼츠는 끝 결과까지 보여 줌 — 결과형과 같은 방향) · 꼴 `stock/guides/README.md` v1.24 7번
- 길이: **12문장 · 예상 약 59.2초** (`render.mjs sync --estimate` — 진행자 H04 실측으로 맞춘 추정) · 결과 첫 숫자 약 32초 · 50자 넘는 문장 없음 · 45~59초 = 비교 집단에서 가장 높은 구간 (shorts_insights 2번)
- 목소리: 진행자 H04 하나 (CLAUDE.md) — 한국어 내레이션, **화면은 소리 없이도 이해되게** · 외국어는 언어별 자막(CC — `subs/<영상ID>-shorts.<언어>.txt` → 오디오 뒤 `tools/subs_tool.py build` 로 SRT) + 자동 더빙
- 숫자: 쇼츠 대본의 숫자는 모두 롱폼 대본에 있다 — `python3 tools/backtest/shorts_numcheck.py stock reobeoriji-2026-10` → [`checklist.md`](checklist.md) (숫자 24개 · 없음 0). 화면 숫자는 그 롱폼의 `backtest/` anim 자료에서만 — 장면 파일이 대본 숫자와 맞춰 보고 다르면 멈춘다.
- ※ 연구·교육용 — 투자 권유가 아님

## 1. 제목

| | 제목 (한국어 — 기본 언어) | 2줄 (`title_fit.py --shorts`) | 까닭 |
|---|---|---|---|
| **R1 (추천)** | **TQQQ 3배 매달 500달러, QQQ보다 훨씬 남을까?** | ✅ 홈 Shorts 칸·재생 화면·PC 다음 동영상 | 쇼츠가 시험하는 말 그대로 · 맨 앞 핵심 낱말 · 질문 (결과는 영상 안에서) |
| R2 | TQQQ 3배, 오래 모으면 QQQ보다 훨씬 남을까? | ✅ | 같은 질문을 다르게 |

- 제목은 결과를 말하지 않는다 (테스트로 호기심 — 사용자 지시). 결과는 영상 32초부터.

### 1-1. 언어별 제목·설명 (localizations — 롱폼 `upload.md` 5번과 같은 9개 언어)

JSON — 업로드 도구가 읽는 꼴. 설명 = 한국어 설명란(4번)과 같은 뜻 (왜 → 어떻게 → 결과, '▶' 줄 = 롱폼에만 있는 것 + 그 언어의 롱폼 제목). 해시태그는 티커. 숫자 표기는 그 언어 관습.

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

## 2. 대본 (시각은 예상 — 내레이션 뒤 실제 시각으로 맞춤)

| # | 시각 | 대본 | 역할 | 화면 (언어 없음 — 숫자·$·%·×·연도·티커·기호·아이콘) |
|---|---|---|---|---|
| 1 | 0:00 | 나스닥100을 3배로 따라가는 TQQQ를 오래 모으면, 훨씬 많이 남는다고들 하죠. | **왜** — 시험할 말 | **쇼츠 썸네일 그림** (`TQQQ 3× > QQQ 1× ?` — 멀쩡한 로켓 셋이 폭풍 구름 쪽으로, 주황 연료 구멍에 동전) |
| 2 | 0:05 | 정말 그런지, AI가 짠 파이썬 코드로 과거 실제 가격을 넣어 백테스트해 봤습니다. | **어떻게** | 흰 가격 선 + **코드 카드** `leverage.py` (`tools/backtest/leverage.py` `daily_returns()` 를 줄인 줄 — `out = L * r` · `out -= (L - 1) * rf * days / 365` · `out -= er * days / 365`) |
| 3 | 0:11 | 나스닥100을 1배로 따라가는 QQQ, 2배 QLD, 3배 TQQQ를 비교했어요. | 비교한 것 | `NASDAQ 100` · 카드 셋 `QQQ 1×` (파랑) · `QLD 2×` (보라) · `TQQQ 3×` (주황) |
| 4 | 0:17 | QLD·TQQQ는 1999년엔 없어서, 매일 지수의 2배·3배에서 비용을 빼 계산했어요. | 계산한 까닭·방법 | 📅 `1999` · QLD·TQQQ 카드 테두리가 노란 점선(그때는 없음) · `% × 2 − $` · `% × 3 − $` |
| 5 | 0:24 | 1999년부터 세 계좌에 매달 500달러씩 똑같이 넣었어요. | 조건 ① | 경주 화면 1999.04.01 · 세로축 10배 눈금 · 넣은 돈 노란 점선 · 칩 `$500` → 날짜가 흐름 |
| 6 | 0:28 | 폭락이 와도, 세 계좌 모두 매달 계속 매수했고요. | 조건 ② (폭락에도 계속) | 위 오른쪽 `$500 → BUY ×3` · 아래 칸 QQQ 1× · QLD 2× · TQQQ 3× 값 |
| 7 | 0:31 | 2026년까지 세 계좌 모두 약 17만 달러를 넣었어요. | **결과 ①** | 경주가 2026.10.15 에 닿음 · 칩 `$165,500` |
| 8 | 0:35 | 3배 계좌는 약 1,700만 달러로, 1배 약 200만 달러의 8.55배였어요. | **결과 ②** | `TQQQ 3×` `×8.55` (위 왼쪽 큰 글자) · 1배 끝 → 3배 끝 노란 점선 · 아래 칸 `$17,306,585` · `$2,023,890` 깜빡 |
| 9 | 0:41 | 하지만 2001년에는 3배 계좌가 넣은 돈의 92.3%를 잃었어요. | **결과 ③** (손해) | 2001.03.29 빨간 점선 + 3배 선에 칩 `−92.3%` |
| 10 | 0:46 | 2008년에도 89.5%를 잃었고요. | **결과 ④** (손해) | 2008.11.20 빨간 점선 + 칩 `−89.5%` |
| 11 | 0:49 | 같은 지수인데, 3배는 왜 폭락 때 이렇게 많이 잃었을까요? | 호기심 (왜?) | 두 폭락 사이에 큰 `?` |
| 12 | 0:53 | 그 이유와, 처음에 한 번에 넣었다면 어땠을지는 아래 영상에서 확인하세요. | 롱폼 안내 | 끝 화면: `QQQ 1×` `QLD 2×` `TQQQ 3×` · 그림 둘(매일 오르내림 `?` · 한 번에 넣기 `?`) · 노란 ⬇ |

- **아무것도 모르는 시청자가 '뭐야? 왜 이렇게 했고 어떻게 했다는 거야?'라고 묻지 않게** — 왜·어떻게·비교 상대와 까닭·공정한 조건은 빼지 않는다 (`stock/guides/README.md` 7번 · `guides/script_guide.md` 피드백 21).
- 롱폼과 같은 색 = 같은 계좌. 끝인사("시청해주셔서 감사합니다.")는 넣지 않는다 (`guides/shorts_guide.md` 4번).
- 대본 TXT (내레이션용): [`reobeoriji-2026-10-shorts.txt`](reobeoriji-2026-10-shorts.txt) · 언어별 자막 대본: [`subs/`](subs/) (`python3 tools/subs_tool.py check stock reobeoriji-2026-10-shorts`)

## 3. 영상 만드는 법 (오디오가 생긴 뒤 — CLAUDE.md '오디오 먼저')

**첫 문장 = 쇼츠 썸네일 그림:** 0초부터 첫 문장(시험할 말)이 끝날 때까지 `thumbnails/thumbnail_1.png` (ChatGPT 가 [`thumbnails/thumbnail_1.md`](thumbnails/thumbnail_1.md) 로 만들고 Claude 가 검수 — 글자 `TQQQ 3× > QQQ 1× ?`)를 화면 가득 (kit.js `K.cover`). 빈 띠가 있으면 `tools/cover_check.py` 로 재고 `K.cover(…, { box })`.

**모양:** 세로 1080×1920 · 롱폼과 같은 짙은 남색 바탕·색 · **화면에 자막을 굽지 않음** (언어별 자막은 CC 로 올림) · 화면 글자는 언어 없이 (`K.init` `noWords`) · 음악 없음 · 음량 -14 LUFS.

**화면 자리 — 가운데·크게** (`guides/video_guide.md` v4.13 6번, `<meta name="video-safe" content="150 60 1320 60">`): 장면 파일 v2.1 은 화면 좌표를 바로 씀 (가운데 x 540), 글자·그림 y 160~1316, 아래 1320~1920 은 비움 (제목·관련 동영상 링크 — 끝 화면 ⬇ 이 가리킴).

**장면:** 2번 표 — 장면 파일 [`video/episodes/reobeoriji-2026-10-shorts/index.html`](../../../../video/episodes/reobeoriji-2026-10-shorts/index.html) v2.1 (check 문제 0 · 완성 mp4 장면을 직접 봄). 장면 시각 = 문장·낱말 시각(손으로 적은 초 없음).

**도구:**
1. 내레이션 — Kaggle 셀 범위 `stock` (영상ID `reobeoriji-2026-10-shorts` — `shorts/narration.mp3`·`shorts/tts_narration.json`).
2. 오디오가 오면:
   ```
   cd video && npm run align-audio -- stock reobeoriji-2026-10-shorts --no-export && cd ..
   node video/render/render.mjs sync  stock reobeoriji-2026-10-shorts
   node video/render/render.mjs check stock reobeoriji-2026-10-shorts
   node video/render/render.mjs video stock reobeoriji-2026-10-shorts
   python3 tools/subs_tool.py build stock reobeoriji-2026-10-shorts        # 언어별 SRT (오디오 시각) → shorts/subs/
   ```
   → `stock/out/reobeoriji-2026-10-shorts/final_1080p.mp4` (git 밖) → **완성 mp4 장면을 Claude 가 직접 본다**. 지금은 추정 시각의 소리 없는 미리보기 `stock/out/reobeoriji-2026-10-shorts/preview_estimated_silent.mp4` 만.
3. 올리기 — `tools/youtube_upload.py` v1.12 가 쇼츠 시트 `shorts/upload.md`(아직 없음 — 다음 할 일)를 읽고 한국어 + 언어별 자막(CC)을 올림. 자막 하나 400단위 — 할당량이 모자라면 `--captions-only` 로 다음 날. 롱폼과 같은 시각에 공개 (`guides/upload_guide.md` 12번).

## 4. 설명란 (한국어 — 그대로 복사)

```
나스닥100을 3배로 따라가는 TQQQ를 오래 모으면 훨씬 많이 남는다고들 하죠. 정말 그런지 AI가 짠 파이썬 코드로 과거 실제 가격을 넣어 백테스트했습니다. 나스닥100을 1배로 따라가는 QQQ, 2배 QLD, 3배 TQQQ를 비교했고, QLD·TQQQ는 1999년엔 없어서 매일 지수의 2배·3배에서 비용을 빼 계산했어요. 1999년부터 세 계좌에 매달 500달러씩, 폭락이 와도 계속 매수했습니다. 2026년까지 넣은 돈은 약 17만 달러. 3배 계좌는 약 1,700만 달러로 1배 약 200만 달러의 8.55배였지만, 2001년에는 넣은 돈의 92.3%를, 2008년에도 89.5%를 잃었어요.
▶ 그 이유와, 처음에 한 번에 넣었다면 어땠을지는 아래 '관련 동영상'에서 — 레버리지 ETF, 닷컴 폭락부터 27년 매달 모으면 QLD·TQQQ가 1배 QQQ보다 더 남을까?

자료·계산 조건(2배·3배 계산 방법, 금리, 수수료 0.25%)은 본편 설명란에 있습니다. 계산 코드는 AI가 짰고, 내레이션은 AI 음성입니다.
과거 자료로 계산한 결과이며 투자 권유가 아닙니다.
#TQQQ #QQQ
```
- 해시태그 2개 `#TQQQ #QQQ` (shorts_insights 4번 — 3~5개가 가장 낮음).
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
| 1 | `100` · `3배` | s1 | 나스닥100을 2배, 3배로 따라가는 QLD와 TQQQ. |
| 3 | `100` · `2배` · `3배` | s1 | 나스닥100을 2배, 3배로 따라가는 QLD와 TQQQ. |
| 3 | `1배` | s3 | 1999년부터, 1배·2배·3배를 백테스트로 비교해 보겠습니다. |
| 4 | `2배` · `3배` | s1 | 나스닥100을 2배, 3배로 따라가는 QLD와 TQQQ. |
| 4 | `1999년` | s3 | 1999년부터, 1배·2배·3배를 백테스트로 비교해 보겠습니다. |
| 5 | `1999년` | s3 | 1999년부터, 1배·2배·3배를 백테스트로 비교해 보겠습니다. |
| 5 | `500달러` | s5 | 매달 첫 거래일에 500달러씩 매수하고, 수수료는 0.25%입니다. |
| 7 | `2026년` | s34 | 2026년 10월 15일, 결과입니다. |
| 7 | `17만` | s35 | 세 계좌 모두 331번, 약 17만 달러를 넣었어요. |
| 8 | `3배` | s1 | 나스닥100을 2배, 3배로 따라가는 QLD와 TQQQ. |
| 8 | `1배` | s3 | 1999년부터, 1배·2배·3배를 백테스트로 비교해 보겠습니다. |
| 8 | `200만` | s36 | 1배 계좌는 약 200만 달러, 2배는 약 790만 달러예요. |
| 8 | `1,700만` | s37 | 3배 계좌는 약 1,700만 달러였습니다. |
| 8 | `8.55배` | s39 | 3배가 1배의 8.55배, 2배는 3.91배였어요. |
| 9 | `3배` | s1 | 나스닥100을 2배, 3배로 따라가는 QLD와 TQQQ. |
| 9 | `2001년` · `92.3%` | s13 | 2001년 3월 29일, 3배 계좌는 넣은 돈 1만 2천 달러의 92.3%를 잃었어요. |
| 10 | `2008년` | s18 | 그리고 2008년 금융위기가 왔어요. |
| 10 | `89.5%` | s19 | 11월 20일, 3배 계좌는 넣은 돈 5만 8천 달러의 89.5%를 잃었어요. |
| 11 | `3배` | s1 | 나스닥100을 2배, 3배로 따라가는 QLD와 TQQQ. |

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
| v2.1 | 2026-10-17 | 결과형 + 왜·어떻게 — 대본 12문장 예상 약 59.2초 · 제목 R1 「TQQQ 3배 매달 500달러, QQQ보다 훨씬 남을까?」 · 9개 언어 제목·설명 · 언어별 자막 대본 · 장면 v2.1 (가운데·크게, 코드 카드, 경주 끝까지) · 썸네일 글자 `TQQQ 3× > QQQ 1× ?`만 · 숫자 24개 없음 0 (사용자 지시) |
|---|---|---|
| v1.0.6 | 2026-10-17 | 쇼츠 썸네일 글자 `TQQQ 3× > QQQ 1× ?` · `−92.3%` — 티커 + 배수 (사용자 지시) |
| v1.0.5 | 2026-10-17 | 쇼츠 썸네일 글자 `TQQQ > QQQ ?` · `−92.3%` — 시청자 니즈·티커 (사용자 지시) |
| v1.0.4 | 2026-10-17 | 쇼츠 썸네일 글자 `3× > 1× ?` · `−92.3%` — 큰 부등호 머리글 (사용자 지시) |
| v1.0.3 | 2026-10-17 | 쇼츠 썸네일 글자 `−92.3%` · `3×` · `+$500` — 딱 봤을 때 이해되는 것만 (사용자 지시) |
| v1.0.2 | 2026-10-17 | 쇼츠 썸네일 글자 `3× = −92.3%` · `+$500` · `?` — 비교·수식 기호 (사용자 지시) |
| v1.0.1 | 2026-10-17 | 쇼츠 썸네일 글자 `−92.3%` · `3×` · `$500` (사용자 지시 — 영어·숫자·기호 써도 됨) |
| v1.0 | 2026-10-17 | 새로 만듦 — 대본 9문장 262음절 예상 약 45.3초 · 제목 R1 「3배 레버리지 매달 500달러, 넣은 돈 92.3% 사라졌다… 1배보다 더 남을까?」 · 9개 언어 제목·설명 · 언어 없는 세로 장면 v1.0 · 숫자 근거 22개 (없음 0) |
