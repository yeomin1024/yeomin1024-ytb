# 쇼츠 — `keobeodeu-kol-2026-10` 롱폼으로 보내는 쇼츠 (프롤로그형 · 언어 없는 화면)

버전: v1.0.4 — 2026-10-17 — 쇼츠 썸네일 글자 = 큰 부등호 머리글 `QYLD > QQQ ?` · `−17.5%` (사용자 지시 2026-10-17 "그냥 SCHD > SPY ? 이렇게만 해도 단번에 의미 전달 가능한데 부등호 좀 잘 사용해봐 문구는 눈에 잘 들어오도록 크게 강조해야해").
(v1.0.3 — 2026-10-17 — 쇼츠 썸네일 글자 = 쉬운 것만 `QYLD > QQQ ?` · `−17.5%` (사용자 지시 2026-10-17 "아니 굳이 표현이 어려운 건 문구로 달지말고 표현이 쉬운걸로 딱 봤을 때 이해되는 걸 표현해").)
(v1.0.2 — 2026-10-17 — 쇼츠 썸네일 글자에 비교·수식 기호 `QYLD < $100,000` · `−17.5%` · `QQQ = ?` (사용자 지시 2026-10-17 "<, >, =, vs, +, - 등등 비교나 간단한 수식 관련된 기호 문구도 사용하는 게 좋을 것 같아 다시 수정해봐").)
(v1.0.1 — 2026-10-17 — 쇼츠 썸네일 글자 `−17.5%` · `QYLD` · `$100,000` · `?` (간단한 영어·숫자·기호 — 사용자 지시 2026-10-17 "문구 없으니까 너무 허전하네 buy, sell 같은 정말 간단해서 모두 알만한 영어 문구는 써도 돼" · "숫자나 기호 같은 문구도 써도 돼").)
(v1.0 — 2026-10-17 — 새로 만듦 (사용자 지시 2026-10-17 "저번에 쇼츠 만들었었으니까 같은 방식으로 영상 당 쇼츠 1개씩 만들어봐" · "다른점은 전세계 시청자들 대상이니까 언어 문구, 자막 달지 말고 영상으로만 잘 이해가 가도록 해야해 계속 진행해"). 재테크 쇼츠(`economic/source/eunte-kkeonaeseugi-2026-10/shorts/`)와 같은 꼴 — 첫 문장 하나에 핵심 → 상황 → 질문 → '아래 영상에서 확인하세요' — 에 주식 규칙(자막 없음 · 화면 글자 언어 없음 · 결말 가림 · 10개 언어)을 더함.)

- 보내는 곳(롱폼): **커버드콜 분배금, 매달 꺼내 쓰면 같은 금액을 매도한 QQQ보다 13년 뒤 원금이 더 남을까?** (`../upload.md` 1번 제목) — 쇼츠의 '관련 동영상'으로 연결 (롱폼 공개 뒤)
- **넣지 않는 것 (롱폼의 결말):** 2026년 두 계좌의 **끝 값**(QYLD·QQQ), QQQ 계좌의 선 전체, 커버드콜이 분배금을 만드는 방법(콜옵션), 시작 달을 바꾼 결과, XYLD·JEPI·세금·다시 매수. 화면에도 QQQ 선은 그리지 않고 '?' 칸만 둔다.
- **보여 주는 것:** QYLD 계좌의 2014년 3월 +3.4% · 2016년 −17.5% · 2019년 11월 꺼낸 돈 5만 달러 · 2020년 3월 −28.3% — 롱폼 경주 앞부분의 숫자.
- 근거: [`stock/guides/shorts_insights.md`](../../../guides/shorts_insights.md) v1.0 (주식 쇼츠 분석 — 경주 그래프 쇼츠 같은 채널 ×32~×203 · 45~59초 19% · 금액 +20%p ⚑ · 해시태그 3~5개 6.6%) · 공통 규칙 `guides/shorts_guide.md` 4번
- 길이: **9문장 · 257음절 · 예상 약 44.5초** (`render.mjs sync --estimate` — 진행자 H04 실측으로 맞춘 추정) · 45~59초 · 50자 넘는 문장 없음 · 첫 문장 약 5.9초
- 목소리: 진행자 H04 하나 (CLAUDE.md) — 한국어 내레이션, **화면은 소리 없이도 이해되게** (해외 시청자는 자동 더빙·자동 번역)
- 숫자: 쇼츠 대본의 숫자는 모두 롱폼 대본에 있다 — `python3 tools/backtest/shorts_numcheck.py stock keobeodeu-kol-2026-10` → [`checklist.md`](checklist.md) (없음 0). 화면 숫자는 `stock/source/keobeodeu-kol-2026-10/backtest/anim.js` (`a` QYLD 계좌 · `out` 꺼낸 돈 · `ev` 분배금 날 — `b` QQQ 는 쓰지 않음)에서만.
- ※ 연구·교육용 — 투자 권유가 아님

## 1. 제목

| | 제목 (한국어 — 기본 언어) | 글자 | 까닭 |
|---|---|---|---|
| **R1 (추천)** | **커버드콜 분배금 매달 꺼내 쓴 10만 달러, QQQ였다면 더 남았을까?** | 39 | 금액 '10만 달러' +20%p ⚑ (shorts_insights 3번) · 맨 앞 니즈 낱말 '커버드콜 분배금' · 비교 상대 QQQ 를 질문으로 — 끝 값은 말하지 않음 |
| R2 | 커버드콜 원금, 분배금 매달 꺼내 쓰니 코로나 땐 28.3% 아래… 2026년엔 얼마 남았을까? | 53 | 경주 중간 숫자 28.3% · 말줄임 — 길이 49자로 길어 2안 |

쓰지 않은 것: **'이유'**(쇼츠가 이유를 말하지 않음 — `guides/shorts_guide.md` 4번 5항) · '재테크'(0%)·'투자'(3.8%)·'주식투자'(4.7%)·'AI'(6.2%) 낱말 (shorts_insights 3번) · 결말(롱폼의 끝 결과). 길이는 40자 안팎 — 쇼츠 비교 집단에서 20자 미만 16%·30~39자 14%·40자 이상 15%로 차이가 작다 (shorts_insights 3번).

### 1-1. 언어별 제목·설명 (localizations — 롱폼 `upload.md` 5번과 같은 9개 언어)

JSON — 롱폼 업로드 시트와 같은 꼴 (업로드 도구 v1.6 이 읽는 형식). '▶' 줄의 롱폼 제목은 그 언어의 롱폼 제목. 해시태그는 언어와 상관없는 티커.

```
{
 "en": {
  "title": "$100,000 in a covered call ETF, payouts spent every month: would QQQ have left more?",
  "description": "We put $100,000 into QYLD, a Nasdaq-100 covered call ETF, in December 2013 and spent every payout as it came. In March 2014 it was 3.4% above the principal, but in March 2020, when the COVID crash hit, it was 28.3% below. There is also a QQQ account, which follows the Nasdaq-100, that took out the same cash on the same days.\n▶ How much each account had left by 2026 is in the related video below — Covered call payouts spent monthly: is more principal left after 13 years than selling QQQ?\n\nData and full conditions (payout handling, fees) are in the main video's description. The code was written by AI and the narration is an AI voice.\nPast data only — not investment advice.\n#QYLD #QQQ"
 },
 "hi": {
  "title": "कवर्ड कॉल ETF में $100,000, हर महीने भुगतान खर्च: क्या QQQ में ज़्यादा बचता?",
  "description": "दिसंबर 2013 में नैस्डैक-100 कवर्ड कॉल ETF QYLD में $100,000 लगाए और हर भुगतान आते ही पूरा खर्च किया। मार्च 2014 में यह मूलधन से 3.4% ज़्यादा था, लेकिन मार्च 2020 के कोरोना क्रैश में मूलधन से 28.3% कम था। नैस्डैक-100 को फॉलो करने वाले QQQ से भी उन्हीं दिनों उतनी ही रकम निकालने वाला खाता है।\n▶ 2026 तक दोनों खातों में कितना बचा, नीचे जुड़े वीडियो में — कवर्ड कॉल भुगतान हर महीने खर्च करें तो क्या 13 साल बाद QQQ बेचने से ज़्यादा मूलधन बचेगा?\n\nडेटा और पूरी शर्तें (भुगतान, शुल्क) मुख्य वीडियो के विवरण में हैं। कोड AI ने लिखा और आवाज़ AI की है।\nसिर्फ़ पिछला डेटा — निवेश सलाह नहीं।\n#QYLD #QQQ"
 },
 "id": {
  "title": "$100.000 di ETF covered call, dividen dipakai tiap bulan: apakah QQQ akan tersisa lebih banyak?",
  "description": "Kami menaruh $100.000 di QYLD, ETF covered call Nasdaq-100, pada Desember 2013 dan memakai setiap pembayaran begitu cair. Pada Maret 2014 nilainya 3,4% di atas modal, tetapi pada Maret 2020 saat crash COVID, 28,3% di bawah modal. Ada juga akun QQQ, yang mengikuti Nasdaq-100, yang menarik uang yang sama di hari yang sama.\n▶ Berapa sisa kedua akun pada 2026 ada di video tertaut di bawah — Dividen covered call dipakai tiap bulan: apakah modal tersisa lebih banyak dari jual QQQ, 13 tahun?\n\nData dan syarat lengkap (pembayaran, biaya) ada di deskripsi video utama. Kode ditulis AI dan narasinya suara AI.\nHanya data masa lalu — bukan saran investasi.\n#QYLD #QQQ"
 },
 "pt": {
  "title": "US$ 100 mil num ETF de covered call, renda gasta todo mês: com QQQ sobraria mais?",
  "description": "Colocamos US$ 100.000 no QYLD, um ETF de covered call do Nasdaq-100, em dezembro de 2013 e gastamos cada pagamento assim que saiu. Em março de 2014 ele estava 3,4% acima do capital, mas em março de 2020, no crash da COVID, estava 28,3% abaixo. Há também uma conta de QQQ, que segue o Nasdaq-100, que retirou o mesmo dinheiro nos mesmos dias.\n▶ Quanto sobrou em cada conta até 2026 está no vídeo vinculado abaixo — Renda de covered call gasta todo mês: sobra mais capital em 13 anos do que vendendo QQQ?\n\nDados e condições completas (pagamentos, taxas) na descrição do vídeo principal. O código foi escrito por IA e a narração é voz de IA.\nApenas dados passados — não é recomendação de investimento.\n#QYLD #QQQ"
 },
 "es-419": {
  "title": "US$100,000 en un ETF de covered call, gastando cada pago mensual: ¿con QQQ quedaría más?",
  "description": "Pusimos US$100,000 en QYLD, un ETF de covered call del Nasdaq-100, en diciembre de 2013 y gastamos cada pago apenas llegó. En marzo de 2014 estaba 3.4% por encima del capital, pero en marzo de 2020, con la caída del COVID, estaba 28.3% por debajo. También hay una cuenta de QQQ, que sigue el Nasdaq-100, que retiró el mismo dinero los mismos días.\n▶ Cuánto le quedó a cada cuenta en 2026 está en el video vinculado abajo — Ingreso de covered call gastado cada mes: ¿queda más capital en 13 años que vendiendo QQQ?\n\nDatos y condiciones completas (pagos, comisiones) en la descripción del video principal. El código lo escribió una IA y la narración es una voz de IA.\nSolo datos pasados — no es asesoría de inversión.\n#QYLD #QQQ"
 },
 "ja": {
  "title": "カバードコールETFに10万ドル、分配金を毎月使ったら… QQQなら多く残った？",
  "description": "2013年12月、ナスダック100のカバードコールETF・QYLDに10万ドルを入れ、分配金は出るたびに全部使いました。2014年3月には元本より3.4%多かったものの、コロナ暴落の2020年3月には元本より28.3%少なくなりました。ナスダック100に連動するQQQからも、同じ日に同じ額を引き出した口座があります。\n▶ 2026年までに2つの口座にいくら残ったかは、下のリンクの動画で — カバードコールの分配金を毎月使うと、同じ額を売るQQQより13年後に元本は多く残る？\n\nデータと計算条件（分配金の扱い・手数料）は本編の説明欄にあります。計算コードはAIが書き、ナレーションはAI音声です。\n過去データによる計算で、投資の勧誘ではありません。\n#QYLD #QQQ"
 },
 "de": {
  "title": "100.000 $ im Covered-Call-ETF, Ausschüttung jeden Monat ausgegeben: Wäre mit QQQ mehr übrig?",
  "description": "Wir haben im Dezember 2013 100.000 $ in QYLD angelegt, einen Nasdaq-100-Covered-Call-ETF, und jede Ausschüttung sofort ausgegeben. Im März 2014 lag das Konto 3,4 % über dem Kapital, im März 2020, beim Corona-Crash, aber 28,3 % darunter. Es gibt auch ein QQQ-Konto, das den Nasdaq-100 abbildet und an denselben Tagen dasselbe Geld entnahm.\n▶ Wie viel beiden Konten bis 2026 blieb, im verlinkten Video unten — Covered-Call-Ausschüttung monatlich ausgeben: Bleibt nach 13 Jahren mehr als beim QQQ-Verkauf?\n\nDaten und alle Bedingungen (Ausschüttungen, Gebühren) in der Beschreibung des Hauptvideos. Der Code wurde von einer KI geschrieben, die Stimme ist eine KI-Stimme.\nNur historische Daten – keine Anlageberatung.\n#QYLD #QQQ"
 },
 "vi": {
  "title": "100.000 USD vào ETF covered call, tiêu cổ tức mỗi tháng: nếu là QQQ có còn nhiều hơn?",
  "description": "Tháng 12/2013 chúng tôi đặt 100.000 USD vào QYLD, ETF covered call Nasdaq-100, và tiêu hết mỗi khoản chi trả ngay khi nhận. Tháng 3/2014 tài khoản cao hơn vốn gốc 3,4%, nhưng tháng 3/2020, khi COVID sập, thấp hơn vốn gốc 28,3%. Còn có một tài khoản QQQ, quỹ theo Nasdaq-100, rút cùng số tiền vào cùng ngày.\n▶ Đến năm 2026 mỗi tài khoản còn bao nhiêu, xem ở video liên kết bên dưới — Tiêu cổ tức covered call mỗi tháng: sau 13 năm vốn còn nhiều hơn bán QQQ cùng số tiền không?\n\nDữ liệu và điều kiện đầy đủ (chi trả, phí) trong phần mô tả video chính. Mã do AI viết, lời thuyết minh là giọng AI.\nChỉ là dữ liệu quá khứ — không phải lời khuyên đầu tư.\n#QYLD #QQQ"
 },
 "tr": {
  "title": "Covered call ETF'sine 100.000 $, dağıtım her ay harcandı: QQQ olsaydı daha fazla kalır mıydı?",
  "description": "Aralık 2013'te Nasdaq-100 covered call ETF'si QYLD'ye 100.000 $ yatırdık ve her ödemeyi gelir gelmez harcadık. Mart 2014'te anaparanın %3,4 üstündeydi, ama COVID çöküşünün geldiği Mart 2020'de anaparanın %28,3 altındaydı. Nasdaq-100'ü izleyen QQQ'dan da aynı günlerde aynı parayı çeken bir hesap var.\n▶ 2026'ya kadar iki hesapta ne kadar kaldığı aşağıdaki bağlantılı videoda — Covered call dağıtımını her ay harcarsanız 13 yıl sonra QQQ satmaktan fazla anapara kalır mı?\n\nVeriler ve tüm koşullar (ödemeler, komisyon) ana videonun açıklamasında. Kodu yapay zekâ yazdı, seslendirme yapay zekâ sesi.\nYalnızca geçmiş veriler — yatırım tavsiyesi değildir.\n#QYLD #QQQ"
 }
}
```

## 2. 대본 (시각은 예상 — 내레이션 뒤 실제 시각으로 맞춤)

| # | 시각 | 대본 | 역할 | 화면 (언어 없음 — 숫자·$·%·연도·티커·BUY·기호·아이콘) |
|---|---|---|---|---|
| 1 | 0:00 | 분배금을 매달 꺼내 쓴 커버드콜 계좌가, 2016년 원금보다 17.5% 적어졌습니다. | 핵심 한 문장 | **쇼츠 썸네일 그림** (글자 `QYLD > QQQ ?` · `−17.5%` — 주황 금고에서 동전을 꺼내는 손, 노란 점선 아래로 가라앉는 금고, 천에 덮인 두 번째 계좌) |
| 2 | 0:06 | 나스닥100 커버드콜 ETF인 QYLD에, 2013년 12월 10만 달러를 넣은 계좌예요. | 대상·시작 | `NASDAQ 100` · `QYLD` + 위가 노란 천장에 잘린 선 그림(커버드콜) · 📅 `2013.12` · 노란 점선 상자 `$100,000` |
| 3 | 0:13 | 분배금은 나올 때마다 전부 꺼내 썼어요. | 규칙 | 경주 시작 — 분배금이 나올 때마다 동전이 계좌 선 끝에서 아래 '꺼낸 돈' 칸으로 날아감 · 위 `🪙 → 👛` |
| 4 | 0:15 | 2014년 3월엔 원금보다 3.4% 많아, 원금이 지켜지는 듯했죠. | 잘된 때 | 2014.03.18 에서 잠깐 멈춤 · 칩 `+3.4%`(초록) · 아래 칸 QYLD `$103,375` `+3.4%` |
| 5 | 0:20 | 2019년 11월, 꺼낸 돈이 5만 달러를 넘었고요. | 꺼낸 돈 | 2016.02 바닥 칩 `−17.5%` · 2019.11 꺼낸 돈 칸이 노랗게 깜빡 `$50,353` |
| 6 | 0:24 | 그런데 코로나 폭락이 온 2020년 3월, 원금보다 28.3% 적었어요. | 폭락 | 2020.03.16 · 칩 `−28.3%`(빨강) · QYLD `$71,665` |
| 7 | 0:30 | 나스닥100을 따라가는 ETF인 QQQ에서도, 같은 날 같은 돈을 꺼낸 계좌가 있어요. | 비교 상대 | 아래 칸에 `QQQ 🪙 = →` (같은 날 같은 돈) · 값 자리는 노란 `?` — QQQ 선은 그리지 않음 |
| 8 | 0:36 | 2026년까지 똑같이 꺼냈다면, 두 계좌에는 얼마씩 남았을까요? | 질문 | 경주 위에 `2026` · `QYLD ?` `QQQ ?` 두 상자 · 오른쪽 '?' 띠가 깜빡임 |
| 9 | 0:41 | 두 계좌의 결과는 아래 영상에서 확인하세요. | 롱폼 안내 | 끝 화면: `QYLD ?` `QQQ ?` · `🪙 → 👛 =` · `2013 → 2026` · 노란 ⬇ |

- 흐름: ① 핵심 한 문장(경주 중간의 숫자) → ② 대상·티커 설명 → ③ 규칙 → ④ 경주 중간의 사실 → ⑤ 질문(결말) → ⑥ '아래 영상에서 확인하세요'.
- 롱폼과 같은 색 = 같은 계좌 (주식 쇼츠 0-1 5번) — 쇼츠에서 롱폼으로 넘어와도 같은 그림.
- 끝인사("시청해주셔서 감사합니다.")는 넣지 않는다 (`guides/shorts_guide.md` 4번).
- 대본 TXT (내레이션용): [`keobeodeu-kol-2026-10-shorts.txt`](keobeodeu-kol-2026-10-shorts.txt)

## 3. 영상 만드는 법 (오디오가 생긴 뒤 — CLAUDE.md '오디오 먼저')

**첫 문장 = 쇼츠 썸네일 그림:** 0초부터 첫 문장이 끝날 때까지 `thumbnails/thumbnail_1.png`(ChatGPT 가 [`thumbnails/thumbnail_1.md`](thumbnails/thumbnail_1.md) 로 만들고 Claude 가 검수해 올림 — 그림 + 첫 문장의 숫자·티커 `QYLD > QQQ ?` · `−17.5%`)를 화면 가득 (kit.js `K.cover`). 0초 장면 = 앱에서 썸네일로 고를 장면. 그림이 없으면 미리보기는 그림 아이콘 자리(kit.js v1.5 — 언어 없음), 최종 렌더는 멈춘다.

**모양:** 세로 1080×1920 · 롱폼과 같은 짙은 남색 바탕·색 · **자막 없음**(굽지도 올리지도 않음) · 화면 글자는 언어 없이 (`K.init` `noWords` — `render.mjs check` 가 낱말을 잡음) · 음악 없음 · 음량 -14 LUFS.

**화면 자리 (유튜브가 쇼츠 위에 얹는 것을 피함 — `<meta name="video-safe" content="250 150 1500 60">`):**

| 자리 | 세로 위치 | 무엇 |
|---|---|---|
| 위 | 0~250px | 비움 (유튜브 위쪽 아이콘) |
| 가운데 | 250~1500px | 장면 — x 60~930 (오른쪽 150px 은 좋아요·댓글 버튼), 장면 가운데 x 495. 자막 띠가 없어 재테크 쇼츠(1270)보다 아래까지 씀 |
| 아래 | 1500~1920px | 비움 (제목·채널·관련 동영상 링크) — 끝 화면 ⬇ 이 이 링크를 가리킨다 |

**장면 9개:** ① 썸네일 그림 ② QYLD·커버드콜·2013.12·$100,000 ③ 경주 시작(동전이 나감) ④ +3.4% ⑤ −17.5%·꺼낸 돈 $50,000 넘음 ⑥ −28.3% ⑦ QQQ = 같은 돈 · ? ⑧ 2026 QYLD ? QQQ ? ⑨ 끝 화면 ⬇ — 장면 파일 [`video/episodes/keobeodeu-kol-2026-10-shorts/index.html`](../../../../video/episodes/keobeodeu-kol-2026-10-shorts/index.html) v1.0. 장면 시각 = 문장·낱말 시각(손으로 적은 초 없음). 경주는 결말 전에서 멈추고, 오른쪽 '?' 띠가 그 뒤(→ 2026)를 가린다.

**도구:**
1. 내레이션 — `tools/tts_narration.py` 가 롱폼 대본과 함께 `shorts/keobeodeu-kol-2026-10-shorts.txt` 도 읽어 `shorts/narration.mp3`·`shorts/tts_narration.json` 을 만든다 (영상ID `keobeodeu-kol-2026-10-shorts`, Kaggle 셀 범위 `stock` 또는 전체 · 진행자 H04 · `voices/ref/host.wav`).
2. 오디오가 오면:
   ```
   cd video && npm run align-audio -- stock keobeodeu-kol-2026-10-shorts --no-export && cd ..
   node video/render/render.mjs sync  stock keobeodeu-kol-2026-10-shorts
   node video/render/render.mjs check stock keobeodeu-kol-2026-10-shorts
   node video/render/render.mjs video stock keobeodeu-kol-2026-10-shorts
   ```
   → `stock/out/keobeodeu-kol-2026-10-shorts/final_1080p.mp4` (git 에 넣지 않음). 지금은 추정 시각의 소리 없는 미리보기 `stock/out/keobeodeu-kol-2026-10-shorts/preview_estimated_silent.mp4` 만 (이 컨테이너에만 — 최종본 아님).
3. 올리기 — 롱폼 공개 뒤. 업로드 도구(`tools/youtube_upload.py`)는 아직 쇼츠 시트를 읽지 않는다 (재테크 쇼츠와 같은 상태 — shorts_insights 7번). 3분 이하 세로 영상은 유튜브가 쇼츠로 본다.

## 4. 설명란 (한국어 — 그대로 복사)

```
나스닥100 커버드콜 ETF QYLD에 2013년 12월 10만 달러를 넣고, 분배금은 나올 때마다 전부 꺼내 썼습니다. 2014년 3월엔 원금보다 3.4% 많았지만, 코로나 폭락이 온 2020년 3월엔 원금보다 28.3% 적었습니다. 나스닥100을 따라가는 QQQ에서도 같은 날 같은 돈을 꺼낸 계좌가 있습니다.
▶ 2026년까지 두 계좌에 얼마씩 남았는지는 아래 '관련 동영상'에서 — 커버드콜 분배금, 매달 꺼내 쓰면 같은 금액을 매도한 QQQ보다 13년 뒤 원금이 더 남을까?

자료·계산 조건(분배금 처리·수수료)은 본편 설명란에 있습니다. 계산 코드는 AI가 짰고, 내레이션은 AI 음성입니다.
과거 자료로 계산한 결과이며 투자 권유가 아닙니다.
#QYLD #QQQ
```
- 해시태그 2개 `#QYLD #QQQ` — 두 계좌의 티커. 3~5개 쇼츠의 성공 비율이 6.6%로 가장 낮다 (shorts_insights 4번) · 태그 자체의 효과는 근거 없음.
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
| 고정 댓글 | 쓰려면 질문 하나: "분배금을 매달 꺼내 쓰면 원금이 어떻게 될 거라고 생각하셨나요? 두 계좌의 결과는 본편에서 확인하세요." — 근거 없음, 시험 |

## 6. 숫자 근거 (쇼츠 대본의 숫자 → 롱폼 대본 문장)

롱폼 숫자는 `backtest/check_numbers.py` 가 결과 파일로 맞춰 봤다. 같은 숫자가 여러 문장에 있으면 첫 문장만 적음 (전부는 `checklist.md`).

| 쇼츠 문장 | 숫자 | 롱폼 문장 | 롱폼 대본 |
|---:|---|---|---|
| 1 | `2016년` | s14 | 하지만 2016년 2월에는 원금보다 17.5% 적어졌습니다. |
| 1 | `17.5%` | s14 | 하지만 2016년 2월에는 원금보다 17.5% 적어졌습니다. |
| 2 | `100` | s1 | 원금은 잘 안 깎인다는 나스닥100 커버드콜 ETF, QYLD. |
| 2 | `2013년` | s4 | 2013년 12월, 10만 달러씩 매수해요. |
| 2 | `12월` | s4 | 2013년 12월, 10만 달러씩 매수해요. |
| 2 | `10만` | s4 | 2013년 12월, 10만 달러씩 매수해요. |
| 4 | `2014년` | s12 | 첫 분배금은 2014년 1월, 1,024달러였어요. |
| 4 | `3월` | s13 | 2014년 3월엔 QYLD 계좌가 원금보다 3.4% 많아, 원금이 지켜지는 듯했어요. |
| 4 | `3.4%` | s13 | 2014년 3월엔 QYLD 계좌가 원금보다 3.4% 많아, 원금이 지켜지는 듯했어요. |
| 5 | `2019년` | s18 | 2019년 11월, 두 계좌가 꺼낸 돈이 5만 달러를 넘었어요. |
| 5 | `11월` | s18 | 2019년 11월, 두 계좌가 꺼낸 돈이 5만 달러를 넘었어요. |
| 5 | `5만` | s18 | 2019년 11월, 두 계좌가 꺼낸 돈이 5만 달러를 넘었어요. |
| 6 | `2020년` | s19 | 코로나 폭락이 온 2020년 3월 16일, QYLD 계좌는 원금보다 28.3% 적었어요. |
| 6 | `3월` | s13 | 2014년 3월엔 QYLD 계좌가 원금보다 3.4% 많아, 원금이 지켜지는 듯했어요. |
| 6 | `28.3%` | s19 | 코로나 폭락이 온 2020년 3월 16일, QYLD 계좌는 원금보다 28.3% 적었어요. |
| 7 | `100` | s1 | 원금은 잘 안 깎인다는 나스닥100 커버드콜 ETF, QYLD. |
| 8 | `2026년` | s33 | 2026년 10월 15일, 결과입니다. |

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
| v1.0.4 | 2026-10-17 | 쇼츠 썸네일 글자 `QYLD > QQQ ?` · `−17.5%` — 큰 부등호 머리글 (사용자 지시) |
| v1.0.3 | 2026-10-17 | 쇼츠 썸네일 글자 `−17.5%` · `QYLD` · `?` — 딱 봤을 때 이해되는 것만 (사용자 지시) |
| v1.0.2 | 2026-10-17 | 쇼츠 썸네일 글자 `QYLD < $100,000` · `−17.5%` · `QQQ = ?` — 비교·수식 기호 (사용자 지시) |
| v1.0.1 | 2026-10-17 | 쇼츠 썸네일 글자 `−17.5%` · `QYLD` · `$100,000` · `?` (사용자 지시 — 영어·숫자·기호 써도 됨) |
| v1.0 | 2026-10-17 | 새로 만듦 — 대본 9문장 257음절 예상 약 44.5초 · 제목 R1 「커버드콜 분배금 매달 꺼내 쓴 10만 달러, QQQ였다면 더 남았을까?」 · 9개 언어 제목·설명 · 언어 없는 세로 장면 v1.0 · 숫자 근거 17개 (없음 0) |
