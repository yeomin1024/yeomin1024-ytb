# 쇼츠 — `reobeoriji-2026-10` 롱폼으로 보내는 쇼츠 (프롤로그형 · 언어 없는 화면)

버전: v1.0.6 — 2026-10-17 — 쇼츠 썸네일 글자 `TQQQ 3× > QQQ 1× ?` · `−92.3%` — 티커 + 배수 같이 (사용자 지시 2026-10-17 "아오 진짜 배수랑 티커 같이 넣으라고").
(v1.0.5 — 2026-10-17 — 쇼츠 썸네일 글자 `TQQQ > QQQ ?` · `−92.3%` — 시청자 니즈·티커 (사용자 지시 2026-10-17 "티커 문구는 왠만하면 있어야 하는거 아니야? 그리고 내가 댓글 시청자의 니즈를 반영하라고 했잖아 매수 조건 10가지 테스트 한다고 그거 그대로 썸네일에 박는게 아니라고 니즈는 언제 사야할까 잖아 그럼 그냥 그걸로 썸네일로 만들면 되는거야").)
(v1.0.4 — 2026-10-17 — 쇼츠 썸네일 글자 = 큰 부등호 머리글 `3× > 1× ?` · `−92.3%` (사용자 지시 2026-10-17 "그냥 SCHD > SPY ? 이렇게만 해도 단번에 의미 전달 가능한데 부등호 좀 잘 사용해봐 문구는 눈에 잘 들어오도록 크게 강조해야해").)
(v1.0.3 — 2026-10-17 — 쇼츠 썸네일 글자 = 쉬운 것만 `3× > 1× ?` · `−92.3%` (사용자 지시 2026-10-17 "아니 굳이 표현이 어려운 건 문구로 달지말고 표현이 쉬운걸로 딱 봤을 때 이해되는 걸 표현해").)
(v1.0.2 — 2026-10-17 — 쇼츠 썸네일 글자에 비교·수식 기호 `3× = −92.3%` · `+$500` · `?` (사용자 지시 2026-10-17 "<, >, =, vs, +, - 등등 비교나 간단한 수식 관련된 기호 문구도 사용하는 게 좋을 것 같아 다시 수정해봐").)
(v1.0.1 — 2026-10-17 — 쇼츠 썸네일 글자 `−92.3%` · `3×` · `$500` (간단한 영어·숫자·기호 — 사용자 지시 2026-10-17 "문구 없으니까 너무 허전하네 buy, sell 같은 정말 간단해서 모두 알만한 영어 문구는 써도 돼" · "숫자나 기호 같은 문구도 써도 돼").)
(v1.0 — 2026-10-17 — 새로 만듦 (사용자 지시 2026-10-17 "저번에 쇼츠 만들었었으니까 같은 방식으로 영상 당 쇼츠 1개씩 만들어봐" · "다른점은 전세계 시청자들 대상이니까 언어 문구, 자막 달지 말고 영상으로만 잘 이해가 가도록 해야해 계속 진행해"). 재테크 쇼츠(`economic/source/eunte-kkeonaeseugi-2026-10/shorts/`)와 같은 꼴 — 첫 문장 하나에 핵심 → 상황 → 질문 → '아래 영상에서 확인하세요' — 에 주식 규칙(자막 없음 · 화면 글자 언어 없음 · 결말 가림 · 10개 언어)을 더함.)

- 보내는 곳(롱폼): **레버리지 ETF, 닷컴 폭락부터 27년 매달 모으면 QLD·TQQQ가 1배 QQQ보다 더 남을까?** (`../upload.md` 1번 제목) — 쇼츠의 '관련 동영상'으로 연결 (롱폼 공개 뒤)
- **넣지 않는 것 (롱폼의 결말):** 2009년 뒤 경주, 2026년 세 계좌의 **끝 값**, 3배가 1배를 앞선 때, 한 번에 넣은 경우, 시작 시점 211개, 실제 ETF(2010~) 비교, 매일 맞추기 설명. 화면에도 2009 → 2026 은 '?' 띠로 가린다.
- **보여 주는 것:** 1·2·3배 경주 1999~2008.11: 닷컴 바닥 −92.3%·−80.7%·−49.9% · 금융위기 3배 −89.5% · 같은 날 1배 −36.4% — 롱폼 경주 앞부분의 숫자 (모두 넣은 돈 대비).
- 근거: [`stock/guides/shorts_insights.md`](../../../guides/shorts_insights.md) v1.0 (주식 쇼츠 분석 — 경주 그래프 쇼츠 같은 채널 ×32~×203 · 45~59초 19% · 금액 +20%p ⚑ · 해시태그 3~5개 6.6%) · 공통 규칙 `guides/shorts_guide.md` 4번
- 길이: **9문장 · 262음절 · 예상 약 45.3초** (`render.mjs sync --estimate` — 진행자 H04 실측으로 맞춘 추정) · 45~59초 · 50자 넘는 문장 없음 · 첫 문장 약 6.2초
- 목소리: 진행자 H04 하나 (CLAUDE.md) — 한국어 내레이션, **화면은 소리 없이도 이해되게** (해외 시청자는 자동 더빙·자동 번역)
- 숫자: 쇼츠 대본의 숫자는 모두 롱폼 대본에 있다 — `python3 tools/backtest/shorts_numcheck.py stock reobeoriji-2026-10` → [`checklist.md`](checklist.md) (없음 0). 화면 숫자는 `stock/source/reobeoriji-2026-10/backtest/anim.js` (`x1`·`x2`·`x3`·`paid`·`facts.dot`·`facts.gfc` — 2009.03 뒤 값은 그리지 않음)에서만.
- ※ 연구·교육용 — 투자 권유가 아님

## 1. 제목

| | 제목 (한국어 — 기본 언어) | 글자 | 까닭 |
|---|---|---|---|
| **R1 (추천)** | **3배 레버리지 매달 500달러, 넣은 돈 92.3% 사라졌다… 1배보다 더 남을까?** | 46 | 금액 '500달러' +20%p ⚑ · 맨 앞 니즈 낱말 '3배 레버리지' · 경주 중간 숫자 92.3% · 말줄임 · 질문으로 끝 (결말 없음) |
| R2 | TQQQ vs QQQ, 닷컴·금융위기에도 매달 500달러씩 모으면 어느 쪽이 더 남을까? | 49 | 두 티커 vs 비교 · 닷컴·금융위기 — 근거가 R1보다 약해 2안 |

쓰지 않은 것: **'이유'**(쇼츠가 이유를 말하지 않음 — `guides/shorts_guide.md` 4번 5항) · '재테크'(0%)·'투자'(3.8%)·'주식투자'(4.7%)·'AI'(6.2%) 낱말 (shorts_insights 3번) · 결말(롱폼의 끝 결과). 길이는 40자 안팎 — 쇼츠 비교 집단에서 20자 미만 16%·30~39자 14%·40자 이상 15%로 차이가 작다 (shorts_insights 3번).

### 1-1. 언어별 제목·설명 (localizations — 롱폼 `upload.md` 5번과 같은 9개 언어)

JSON — 롱폼 업로드 시트와 같은 꼴 (업로드 도구 v1.6 이 읽는 형식). '▶' 줄의 롱폼 제목은 그 언어의 롱폼 제목. 해시태그는 언어와 상관없는 티커.

```
{
 "en": {
  "title": "3x leverage, $500 every month: 92.3% of the money put in was gone… will it beat 1x?",
  "description": "From 1999 we put $500 a month into three accounts calculated like QQQ (1x the Nasdaq-100), QLD (2x) and TQQQ (3x). In the dot-com crash, in 2001, the 3x account lost 92.3% of the money put in, and in the 2008 financial crisis it lost 89.5% again. On that same day, 1x QQQ was down 36.4%.\n▶ The result of saving in all three until 2026 is in the related video below — Leveraged ETFs from the dot-com crash: buying QLD and TQQQ monthly for 27 years, more than 1x QQQ?\n\n2x and 3x are calculated as 2 and 3 times the Nasdaq-100 daily return (method in the main video's description). The code was written by AI and the narration is an AI voice.\nPast data only — not investment advice.\n#TQQQ #QQQ"
 },
 "hi": {
  "title": "3x लीवरेज, हर महीने $500: डाले गए पैसे का 92.3% गायब… क्या 1x से ज़्यादा बचेगा?",
  "description": "1999 से हर महीने $500 तीन खातों में डाले, जिनकी गणना QQQ (नैस्डैक-100 का 1x), QLD (2x) और TQQQ (3x) की तरह की गई। डॉट-कॉम क्रैश में, 2001 में, 3x खाते ने डाले गए पैसे का 92.3% गंवाया और 2008 के वित्तीय संकट में फिर 89.5%। उसी दिन 1x QQQ 36.4% नीचे था।\n▶ 2026 तक तीनों में जमा करने का नतीजा नीचे जुड़े वीडियो में — डॉट-कॉम गिरावट से लीवरेज ETF: 27 साल हर महीने QLD·TQQQ खरीदें तो क्या 1x QQQ से ज़्यादा बचेगा?\n\n2x और 3x की गणना नैस्डैक-100 के दैनिक रिटर्न के 2 और 3 गुना से की गई (तरीका मुख्य वीडियो के विवरण में)। कोड AI ने लिखा और आवाज़ AI की है।\nसिर्फ़ पिछला डेटा — निवेश सलाह नहीं।\n#TQQQ #QQQ"
 },
 "id": {
  "title": "Leverage 3x, $500 tiap bulan: 92,3% uang yang disetor lenyap… akankah lebih dari 1x?",
  "description": "Sejak 1999 kami menaruh $500 per bulan di tiga akun yang dihitung seperti QQQ (1x Nasdaq-100), QLD (2x) dan TQQQ (3x). Saat crash dot-com, pada 2001, akun 3x kehilangan 92,3% uang yang disetor, dan pada krisis keuangan 2008 kehilangan 89,5% lagi. Pada hari yang sama, QQQ 1x turun 36,4%.\n▶ Hasil menabung di ketiganya sampai 2026 ada di video tertaut di bawah — ETF leverage sejak krisis dot-com: beli QLD·TQQQ tiap bulan 27 tahun, sisa lebih dari 1x QQQ?\n\n2x dan 3x dihitung sebagai 2 dan 3 kali return harian Nasdaq-100 (metode di deskripsi video utama). Kode ditulis AI dan narasinya suara AI.\nHanya data masa lalu — bukan saran investasi.\n#TQQQ #QQQ"
 },
 "pt": {
  "title": "Alavancagem 3x, US$ 500 por mês: 92,3% do dinheiro aportado sumiu… vai superar o 1x?",
  "description": "Desde 1999 colocamos US$ 500 por mês em três contas calculadas como QQQ (1x o Nasdaq-100), QLD (2x) e TQQQ (3x). No crash das pontocom, em 2001, a conta 3x perdeu 92,3% do dinheiro aportado, e na crise financeira de 2008 perdeu 89,5% de novo. No mesmo dia, o QQQ 1x estava 36,4% abaixo.\n▶ O resultado de aportar nas três até 2026 está no vídeo vinculado abaixo — ETFs alavancados desde a bolha pontocom: comprar QLD e TQQQ todo mês por 27 anos rende mais que QQQ?\n\n2x e 3x são calculados como 2 e 3 vezes o retorno diário do Nasdaq-100 (método na descrição do vídeo principal). O código foi escrito por IA e a narração é voz de IA.\nApenas dados passados — não é recomendação de investimento.\n#TQQQ #QQQ"
 },
 "es-419": {
  "title": "Apalancamiento 3x, US$500 cada mes: se esfumó 92.3% del dinero aportado… ¿superará al 1x?",
  "description": "Desde 1999 pusimos US$500 al mes en tres cuentas calculadas como QQQ (1x el Nasdaq-100), QLD (2x) y TQQQ (3x). En la caída de las puntocom, en 2001, la cuenta 3x perdió 92.3% del dinero aportado, y en la crisis financiera de 2008 volvió a perder 89.5%. Ese mismo día, QQQ 1x estaba 36.4% abajo.\n▶ El resultado de aportar en las tres hasta 2026 está en el video vinculado abajo — ETF apalancados desde la burbuja puntocom: ¿comprar QLD y TQQQ cada mes 27 años deja más que QQQ?\n\n2x y 3x se calculan como 2 y 3 veces el rendimiento diario del Nasdaq-100 (método en la descripción del video principal). El código lo escribió una IA y la narración es una voz de IA.\nSolo datos pasados — no es asesoría de inversión.\n#TQQQ #QQQ"
 },
 "ja": {
  "title": "3倍レバレッジに毎月500ドル、入れたお金の92.3%が消えた… 1倍より多く残る？",
  "description": "1999年から毎月500ドルずつ、QQQ（ナスダック100の1倍）・QLD（2倍）・TQQQ（3倍）のように計算した3つの口座に入れました。3倍口座はITバブル崩壊の2001年に入れたお金の92.3%を、2008年の金融危機でもまた89.5%を失いました。同じ日、1倍のQQQは36.4%減でした。\n▶ 2026年まで積み立て続けた3つの口座の結果は、下のリンクの動画で — レバレッジETF、ITバブル崩壊から27年毎月積み立てると、QLD・TQQQは1倍のQQQより多く残る？\n\n2倍・3倍はナスダック100の日次リターンを2倍・3倍にして計算した値です（方法は本編の説明欄）。計算コードはAIが書き、ナレーションはAI音声です。\n過去データによる計算で、投資の勧誘ではありません。\n#TQQQ #QQQ"
 },
 "de": {
  "title": "3-fach-Hebel, jeden Monat 500 $: 92,3 % des eingezahlten Geldes weg … mehr als 1-fach am Ende?",
  "description": "Ab 1999 flossen jeden Monat 500 $ in drei Konten, berechnet wie QQQ (1-fach Nasdaq-100), QLD (2-fach) und TQQQ (3-fach). Im Dotcom-Crash, 2001, verlor das 3-fach-Konto 92,3 % des eingezahlten Geldes und in der Finanzkrise 2008 erneut 89,5 %. Am selben Tag lag 1-fach QQQ 36,4 % im Minus.\n▶ Das Ergebnis, wenn man in alle drei bis 2026 weiterspart, im verlinkten Video unten — Hebel-ETFs ab dem Dotcom-Crash: QLD und TQQQ 27 Jahre monatlich kaufen – mehr als 1x QQQ?\n\n2-fach und 3-fach sind als 2- und 3-fache Tagesrendite des Nasdaq-100 berechnet (Methode in der Beschreibung des Hauptvideos). Der Code wurde von einer KI geschrieben, die Stimme ist eine KI-Stimme.\nNur historische Daten – keine Anlageberatung.\n#TQQQ #QQQ"
 },
 "vi": {
  "title": "Đòn bẩy 3x, mỗi tháng 500 USD: mất 92,3% số tiền đã bỏ vào… có hơn 1x không?",
  "description": "Từ năm 1999, mỗi tháng chúng tôi bỏ 500 USD vào ba tài khoản tính như QQQ (1x Nasdaq-100), QLD (2x) và TQQQ (3x). Khi bong bóng dot-com vỡ, năm 2001, tài khoản 3x mất 92,3% số tiền đã bỏ vào, và trong khủng hoảng tài chính 2008 lại mất 89,5%. Cùng ngày đó, QQQ 1x đang giảm 36,4%.\n▶ Kết quả khi tiếp tục tích lũy cả ba đến năm 2026 ở video liên kết bên dưới — ETF đòn bẩy từ bong bóng dot-com: mua QLD, TQQQ mỗi tháng suốt 27 năm có hơn QQQ 1x không?\n\n2x và 3x được tính bằng 2 và 3 lần lợi nhuận ngày của Nasdaq-100 (cách tính trong phần mô tả video chính). Mã do AI viết, lời thuyết minh là giọng AI.\nChỉ là dữ liệu quá khứ — không phải lời khuyên đầu tư.\n#TQQQ #QQQ"
 },
 "tr": {
  "title": "3x kaldıraç, her ay 500 $: yatırılan paranın %92,3'ü gitti… 1x'ten fazla kalır mı?",
  "description": "1999'dan itibaren her ay 500 $'ı QQQ (Nasdaq-100'ün 1x'i), QLD (2x) ve TQQQ (3x) gibi hesaplanan üç hesaba yatırdık. Dot-com çöküşünde, 2001'de, 3x hesap yatırılan paranın %92,3'ünü, 2008 finans krizinde yine %89,5'ini kaybetti. Aynı gün 1x QQQ %36,4 eksideydi.\n▶ Üçüne de 2026'ya kadar yatırmaya devam etmenin sonucu aşağıdaki bağlantılı videoda — Dotcom çöküşünden kaldıraçlı ETF: 27 yıl her ay QLD ve TQQQ almak 1x QQQ'dan fazla bırakır mı?\n\n2x ve 3x, Nasdaq-100 günlük getirisinin 2 ve 3 katı olarak hesaplandı (yöntem ana videonun açıklamasında). Kodu yapay zekâ yazdı, seslendirme yapay zekâ sesi.\nYalnızca geçmiş veriler — yatırım tavsiyesi değildir.\n#TQQQ #QQQ"
 }
}
```

## 2. 대본 (시각은 예상 — 내레이션 뒤 실제 시각으로 맞춤)

| # | 시각 | 대본 | 역할 | 화면 (언어 없음 — 숫자·$·%·연도·티커·BUY·기호·아이콘) |
|---|---|---|---|---|
| 1 | 0:00 | 3배 레버리지에 매달 500달러씩 넣었더니, 2001년 넣은 돈의 92.3%가 사라졌어요. | 핵심 한 문장 | **쇼츠 썸네일 그림** (글자 `TQQQ 3× > QQQ 1× ?` · `−92.3%` — 번개 맞은 주황 3점 로켓, 동전을 떨어뜨리는 손, 뒤의 보라·파랑 로켓, 위는 구름) |
| 2 | 0:06 | 나스닥100을 1배 따라가는 QQQ, 2배 QLD, 3배 TQQQ처럼 계산한 계좌예요. | 세 계좌 | `↗ NASDAQ 100` · `1×` 막대 1칸 `= QQQ` · `2×` 2칸 `≈ QLD` · `3×` 3칸 `≈ TQQQ` (≈ = 그 ETF처럼 계산) |
| 3 | 0:12 | 1999년부터 세 계좌에 똑같이, 매달 500달러씩 넣었어요. | 규칙 | 경주 시작 1999.04 (로그 눈금 — 한 칸 10배) · 위 `📅 BUY $500` · 넣은 돈 노란 점선 · 아래 칸 4줄(넣은 돈·1×·2×·3×) |
| 4 | 0:17 | 닷컴 폭락 때 2배는 넣은 돈의 80.7%, 1배는 49.9%를 잃었고요. | 닷컴 | 2001.03.29 에서 잠깐 멈춤 · 칩 3× `−92.3%` → 2001.04.04 칩 2× `−80.7%` · 1× `−49.9%` (말할 때 그 줄이 빛남) |
| 5 | 0:23 | 그래도 세 계좌 모두 매달 계속 매수했어요. | 계속 매수 | BUY 표가 깜빡이며 2001 → 2008 빨리 감기 · 넣은 돈 점선이 계속 오름 |
| 6 | 0:26 | 그리고 2008년 금융위기에, 3배 계좌는 또 89.5%를 잃었습니다. | 금융위기 | 2008.11.20 · 칩 3× `−89.5%` |
| 7 | 0:31 | 같은 날 1배 QQQ는 넣은 돈의 36.4%를 잃은 상태였어요. | 같은 날 1배 | 칩 1× `−36.4%` · 아래 칸 1× 줄이 빛남 |
| 8 | 0:36 | 2026년까지 계속 모았다면, 3배 계좌는 1배보다 많이 남았을까요? | 질문 | 경주 위에 `2026` · `3× ＞ 1× ?` · 오른쪽 '?' 띠가 깜빡임 |
| 9 | 0:41 | 세 계좌의 결과는 아래 영상에서 확인하세요. | 롱폼 안내 | 끝 화면: `1× QQQ` `2× QLD` `3× TQQQ` · `1999 → 2026` · 큰 `?` · 노란 ⬇ |

- 흐름: ① 핵심 한 문장(경주 중간의 숫자) → ② 대상·티커 설명 → ③ 규칙 → ④ 경주 중간의 사실 → ⑤ 질문(결말) → ⑥ '아래 영상에서 확인하세요'.
- 롱폼과 같은 색 = 같은 계좌 (주식 쇼츠 0-1 5번) — 쇼츠에서 롱폼으로 넘어와도 같은 그림.
- 끝인사("시청해주셔서 감사합니다.")는 넣지 않는다 (`guides/shorts_guide.md` 4번).
- 대본 TXT (내레이션용): [`reobeoriji-2026-10-shorts.txt`](reobeoriji-2026-10-shorts.txt)

## 3. 영상 만드는 법 (오디오가 생긴 뒤 — CLAUDE.md '오디오 먼저')

**첫 문장 = 쇼츠 썸네일 그림:** 0초부터 첫 문장이 끝날 때까지 `thumbnails/thumbnail_1.png`(ChatGPT 가 [`thumbnails/thumbnail_1.md`](thumbnails/thumbnail_1.md) 로 만들고 Claude 가 검수해 올림 — 그림 + 첫 문장의 숫자·티커 `TQQQ 3× > QQQ 1× ?` · `−92.3%`)를 화면 가득 (kit.js `K.cover`). 0초 장면 = 앱에서 썸네일로 고를 장면. 그림이 없으면 미리보기는 그림 아이콘 자리(kit.js v1.5 — 언어 없음), 최종 렌더는 멈춘다.

**모양:** 세로 1080×1920 · 롱폼과 같은 짙은 남색 바탕·색 · **자막 없음**(굽지도 올리지도 않음) · 화면 글자는 언어 없이 (`K.init` `noWords` — `render.mjs check` 가 낱말을 잡음) · 음악 없음 · 음량 -14 LUFS.

**화면 자리 (유튜브가 쇼츠 위에 얹는 것을 피함 — `<meta name="video-safe" content="250 150 1500 60">`):**

| 자리 | 세로 위치 | 무엇 |
|---|---|---|
| 위 | 0~250px | 비움 (유튜브 위쪽 아이콘) |
| 가운데 | 250~1500px | 장면 — x 60~930 (오른쪽 150px 은 좋아요·댓글 버튼), 장면 가운데 x 495. 자막 띠가 없어 재테크 쇼츠(1270)보다 아래까지 씀 |
| 아래 | 1500~1920px | 비움 (제목·채널·관련 동영상 링크) — 끝 화면 ⬇ 이 이 링크를 가리킨다 |

**장면 9개:** ① 썸네일 그림 ② 1·2·3배 = QQQ·≈QLD·≈TQQQ ③ 경주 시작 BUY $500 ④ 닷컴 바닥 ⑤ 계속 매수 ⑥ 금융위기 3× −89.5% ⑦ 1× −36.4% ⑧ 3× ＞ 1× ? ⑨ 끝 화면 ⬇ — 장면 파일 [`video/episodes/reobeoriji-2026-10-shorts/index.html`](../../../../video/episodes/reobeoriji-2026-10-shorts/index.html) v1.0. 장면 시각 = 문장·낱말 시각(손으로 적은 초 없음). 경주는 결말 전에서 멈추고, 오른쪽 '?' 띠가 그 뒤(→ 2026)를 가린다.

**도구:**
1. 내레이션 — `tools/tts_narration.py` 가 롱폼 대본과 함께 `shorts/reobeoriji-2026-10-shorts.txt` 도 읽어 `shorts/narration.mp3`·`shorts/tts_narration.json` 을 만든다 (영상ID `reobeoriji-2026-10-shorts`, Kaggle 셀 범위 `stock` 또는 전체 · 진행자 H04 · `voices/ref/host.wav`).
2. 오디오가 오면:
   ```
   cd video && npm run align-audio -- stock reobeoriji-2026-10-shorts --no-export && cd ..
   node video/render/render.mjs sync  stock reobeoriji-2026-10-shorts
   node video/render/render.mjs check stock reobeoriji-2026-10-shorts
   node video/render/render.mjs video stock reobeoriji-2026-10-shorts
   ```
   → `stock/out/reobeoriji-2026-10-shorts/final_1080p.mp4` (git 에 넣지 않음). 지금은 추정 시각의 소리 없는 미리보기 `stock/out/reobeoriji-2026-10-shorts/preview_estimated_silent.mp4` 만 (이 컨테이너에만 — 최종본 아님).
3. 올리기 — 롱폼 공개 뒤. 업로드 도구(`tools/youtube_upload.py`)는 아직 쇼츠 시트를 읽지 않는다 (재테크 쇼츠와 같은 상태 — shorts_insights 7번). 3분 이하 세로 영상은 유튜브가 쇼츠로 본다.

## 4. 설명란 (한국어 — 그대로 복사)

```
나스닥100을 1배 따라가는 QQQ, 2배 QLD, 3배 TQQQ처럼 계산한 세 계좌에 1999년부터 매달 500달러씩 넣었습니다. 3배 계좌는 닷컴 폭락 때인 2001년 넣은 돈의 92.3%를, 2008년 금융위기엔 또 89.5%를 잃었습니다. 같은 날 1배 QQQ는 36.4%를 잃은 상태였고요.
▶ 2026년까지 계속 모은 세 계좌의 결과는 아래 '관련 동영상'에서 — 레버리지 ETF, 닷컴 폭락부터 27년 매달 모으면 QLD·TQQQ가 1배 QQQ보다 더 남을까?

2·3배는 나스닥100 하루 수익률을 2·3배로 계산한 값입니다 (계산 방법은 본편 설명란). 계산 코드는 AI가 짰고, 내레이션은 AI 음성입니다.
과거 자료로 계산한 결과이며 투자 권유가 아닙니다.
#TQQQ #QQQ
```
- 해시태그 2개 `#TQQQ #QQQ` — 3배와 1배의 티커. 3~5개 쇼츠의 성공 비율이 6.6%로 가장 낮다 (shorts_insights 4번) · 태그 자체의 효과는 근거 없음.
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
| 고정 댓글 | 쓰려면 질문 하나: "3배 레버리지를 폭락 때도 매달 계속 살 수 있을까요? 세 계좌의 결과는 본편에서 확인하세요." — 근거 없음, 시험 |

## 6. 숫자 근거 (쇼츠 대본의 숫자 → 롱폼 대본 문장)

롱폼 숫자는 `backtest/check_numbers.py` 가 결과 파일로 맞춰 봤다. 같은 숫자가 여러 문장에 있으면 첫 문장만 적음 (전부는 `checklist.md`).

| 쇼츠 문장 | 숫자 | 롱폼 문장 | 롱폼 대본 |
|---:|---|---|---|
| 1 | `3배` | s1 | 나스닥100을 2배, 3배로 따라가는 QLD와 TQQQ. |
| 1 | `500달러` | s5 | 매달 첫 거래일에 500달러씩 매수하고, 수수료는 0.25%입니다. |
| 1 | `2001년` | s13 | 2001년 3월 29일, 3배 계좌는 넣은 돈 1만 2천 달러의 92.3%를 잃었어요. |
| 1 | `92.3%` | s13 | 2001년 3월 29일, 3배 계좌는 넣은 돈 1만 2천 달러의 92.3%를 잃었어요. |
| 2 | `100` | s1 | 나스닥100을 2배, 3배로 따라가는 QLD와 TQQQ. |
| 2 | `1배` | s3 | 1999년부터, 1배·2배·3배를 백테스트로 비교해 보겠습니다. |
| 2 | `2배` | s1 | 나스닥100을 2배, 3배로 따라가는 QLD와 TQQQ. |
| 2 | `3배` | s1 | 나스닥100을 2배, 3배로 따라가는 QLD와 TQQQ. |
| 3 | `1999년` | s3 | 1999년부터, 1배·2배·3배를 백테스트로 비교해 보겠습니다. |
| 3 | `500달러` | s5 | 매달 첫 거래일에 500달러씩 매수하고, 수수료는 0.25%입니다. |
| 4 | `2배` | s1 | 나스닥100을 2배, 3배로 따라가는 QLD와 TQQQ. |
| 4 | `80.7%` | s14 | 4월 4일에는 2배가 80.7%, 1배가 49.9% 줄어, 셋 다 넣은 돈보다 적었어요. |
| 4 | `1배` | s3 | 1999년부터, 1배·2배·3배를 백테스트로 비교해 보겠습니다. |
| 4 | `49.9%` | s14 | 4월 4일에는 2배가 80.7%, 1배가 49.9% 줄어, 셋 다 넣은 돈보다 적었어요. |
| 6 | `2008년` | s18 | 그리고 2008년 금융위기가 왔어요. |
| 6 | `3배` | s1 | 나스닥100을 2배, 3배로 따라가는 QLD와 TQQQ. |
| 6 | `89.5%` | s19 | 11월 20일, 3배 계좌는 넣은 돈 5만 8천 달러의 89.5%를 잃었어요. |
| 7 | `1배` | s3 | 1999년부터, 1배·2배·3배를 백테스트로 비교해 보겠습니다. |
| 7 | `36.4%` | s20 | 같은 날 2배는 72.8%, 1배는 36.4%를 잃은 상태였고요. |
| 8 | `2026년` | s34 | 2026년 10월 15일, 결과입니다. |
| 8 | `3배` | s1 | 나스닥100을 2배, 3배로 따라가는 QLD와 TQQQ. |
| 8 | `1배` | s3 | 1999년부터, 1배·2배·3배를 백테스트로 비교해 보겠습니다. |

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
| v1.0.6 | 2026-10-17 | 쇼츠 썸네일 글자 `TQQQ 3× > QQQ 1× ?` · `−92.3%` — 티커 + 배수 (사용자 지시) |
| v1.0.5 | 2026-10-17 | 쇼츠 썸네일 글자 `TQQQ > QQQ ?` · `−92.3%` — 시청자 니즈·티커 (사용자 지시) |
| v1.0.4 | 2026-10-17 | 쇼츠 썸네일 글자 `3× > 1× ?` · `−92.3%` — 큰 부등호 머리글 (사용자 지시) |
| v1.0.3 | 2026-10-17 | 쇼츠 썸네일 글자 `−92.3%` · `3×` · `+$500` — 딱 봤을 때 이해되는 것만 (사용자 지시) |
| v1.0.2 | 2026-10-17 | 쇼츠 썸네일 글자 `3× = −92.3%` · `+$500` · `?` — 비교·수식 기호 (사용자 지시) |
| v1.0.1 | 2026-10-17 | 쇼츠 썸네일 글자 `−92.3%` · `3×` · `$500` (사용자 지시 — 영어·숫자·기호 써도 됨) |
| v1.0 | 2026-10-17 | 새로 만듦 — 대본 9문장 262음절 예상 약 45.3초 · 제목 R1 「3배 레버리지 매달 500달러, 넣은 돈 92.3% 사라졌다… 1배보다 더 남을까?」 · 9개 언어 제목·설명 · 언어 없는 세로 장면 v1.0 · 숫자 근거 22개 (없음 0) |
