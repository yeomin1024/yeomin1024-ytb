# gongpo-test-2026-11 업로드 시트

버전: v1.8 — 2026-11-05 — 외국어 설정 (사용자 지시 "외국어 자막, 제목, 썸네일 등 외국어 설정에 필요한 것들 생성하고 지시사항에 반영해 이건 영상이 렌더까지 완료되면 하는거야" — `stock/guides/quick_board.md` 규칙 46): 6번 언어별 제목·설명 9개 언어(en·hi·id·pt·es-419·ja·de·vi·tr — 1·2번 그대로 옮김, 챕터 시각 같음) · 자막 = 한국어 + 언어별 SRT 9개 (`subs/`, `tools/subs_tool.py` build — 완성 영상의 문장 시각) · 언어별 썸네일 `thumbnails/<언어>/thumbnail_1.jpg` (`thumb.mjs` v1.2 lang) · 업로드 설정에 기본 언어 ko · 자막 올리기 언어별 · 섹션 번호 6→7·7→8·8→9.
이전 v1.7 — 2026-11-05 — 설명란 줄임·태그 늘림 (사용자 지시 "김씨는 실제 숫자로 만든 가상의 인물입니다. 내레이션은 AI 음성이고, 그림은 AI로 만든 연출입니다. 다섯 가지 선택, 계산기준빼고 태그도 더 추가 하는걸로 설명 만들자 지시사항에도 반영해" — `stock/guides/quick_board.md` 규칙 45): '다섯 가지 선택'·'계산 기준'·'○씨는 가상의 인물'·'AI 음성/그림' 줄 뺌 · 태그 23개(편 낱말 + 실제 영상 태그 `stock/tag_candidates.md`).
이전 v1.6 — 2026-11-04 — 챕터 시각 = 새 음성(바뀐 문장 하나 — Kaggle 2026-11-04) 기준.
이전 v1.5 — 2026-11-04 — 대본: 선택마다 질문 뒤 '선택해 보세요.' · '3, 2, 1.' (사용자 지시 "매수 하시겠습니까? 선택 항목 다음에 선택해보세요. 멘트 추가하고 3, 2, 1 카운트 후에 정답 얘기하도록수정해 다른 대본도 그렇게 하고") — 문장 10개 늘어 챕터 번호 다시.
이전 v1.4 — 2026-11-04 — 대본 v15 (판 피드백 5건 — 질문 구체 행동 · '하락했다' · 금리차 '역전' · 결론 안 겹침) · 제목 바꿈 (사용자 지시 "1편이랑 안겹치개 제목도 변경해봐") — 문장 수 그대로라 챕터 번호 그대로.
이전 v1.3 — 2026-11-04 — 대본 평가판 1편 피드백 11건을 1~4편 모두에 (인물 결과 문장 지움 → '○씨의 결과' 챕터 없앰) — 챕터 번호 다시.
이전 v1.2 — 2026-11-04 — 대본 질문형(선택마다 바로 정답·해설, quick_board 규칙 25) — 챕터 문장 번호 다시 · \'정답과 해설\' 챕터 없앰.
이전 v1.1 — 2026-11-02 — 대본 v10 (대본 평가판 피드백 — 도입·해설 넘어가는 말·결과 문장을 다른 편과 겹치지 않게) · 챕터 번호 다시.
이전 v1.0 — 2026-11-02 — 4편 「주식 폭락 공포에 매수 못하는 사람들은 통과 못하는 테스트」 대본 v9 (대본 평가판 피드백 "이건 폭락 중 공포에 매몰되지 않고 안전한 계획을 가지면서 매수할 수 있는지 테스트하는거야 항목 다시 쓰고 멘트좀 겹치지 않게 해봐 주제에 맞게" — 다섯 선택을 모두 새로) · 114문장 · 숫자 `stock/topics/precheck/longform_ep4.py` v1.0
기준 파일: 대본 `gongpo-test-2026-11.txt` v9 · 숫자 `stock/topics/precheck/longform_ep4_2026-11-02.json` (`4편_v9`) · 오디오·SRT는 아직 없음 (Kaggle TTS 뒤 `align-audio`)

> 업로드 채널 = 주식 채널(STOCK LAB) — 도구는 키의 채널이 다르면 멈춤.
> 연구·교육용 콘텐츠 — 투자 상담이나 권유가 아님.

## 1. 제목 (2026-11-04 새 제목 — 사용자 지시 "1편이랑 안겹치개 제목도 변경해봐" · 옛 제목 「주식 폭락 공포에 매수 못하는 사람들은 통과 못하는 테스트」)

```
공포 지수 36 폭락장, 당신은 계획대로 매수할 수 있나요?
```

## 2. 설명란 (그대로 복사)

```
폭락이 시작된 날부터 4년 동안 S&P 500 지수는 40% 넘게 올랐는데, 정씨는 1억 원 가운데 64%를 잃었습니다.
정씨가 폭락 속에서 마주했던 다섯 번의 갈림길에서, 당신이라면 어떤 선택을 했을지 테스트해 보세요. 공포에 진 결정이 몇 개인지 세면 됩니다.

■ 챕터
0:00 정씨에게 무슨 일이
0:37 선택 1 공포가 가장 클 때
2:30 선택 2 공포가 가라앉은 날
3:51 선택 3 가장 많이 하락한 종목
5:14 선택 4 크게 반등한 날
6:34 선택 5 바닥이 다시 깨졌을 때
7:53 당신의 결과
8:15 정리

■ 출처
- 주가·지수: Yahoo Finance (S&P 500 ^GSPC·배당 포함 지수 ^SP500TR·공포 지수 ^VIX·13주 국채 ^IRX·MRNA·NFLX 수정 종가)
- S&P 500 구성 종목 목록: github.com/datasets/s-and-p-500-companies

■ 알려 드립니다
이 테스트는 공식 시험이 아니라, 실제 과거 데이터로 직접 만든 것입니다. 모두 과거 자료이고, 앞으로도 꼭 같다는 보장은 없습니다.
이 영상은 투자 권유가 아니며, 특정 종목을 사거나 팔라는 뜻이 아닙니다.

#주식테스트 #미국주식
```

## 3. 챕터 다시 계산하기 (문장 번호 기준 — 오디오·SRT 가 생긴 뒤)

```
python tools/srt_tool.py upload stock/source/gongpo-test-2026-11/gongpo-test-2026-11.txt stock/source/gongpo-test-2026-11/gongpo-test-2026-11.srt --chapters "1=정씨에게 무슨 일이;9=선택 1 공포가 가장 클 때;33=선택 2 공포가 가라앉은 날;51=선택 3 가장 많이 하락한 종목;68=선택 4 크게 반등한 날;85=선택 5 바닥이 다시 깨졌을 때;102=당신의 결과;106=정리"
```
- 챕터 제목에 정답을 쓰지 않는다 (해설 전 단서 금지 — 사용자 지시 2026-11-01 "도입부 부터 날짜 같은 정답을 알 수 있는 요소 말하지마").

## 4. 태그

```
주식 테스트, 폭락장, 하락장 매수, 공포 지수, 분할매수, 신용 투자, 반대매매, 투자 실패, 하락장, 주식, 주식투자, 미국주식, 주식초보, 주린이, 주식공부, 주식기초, 투자공부, 투자마인드, 개미투자자, 초보투자자, 장기투자, S&P500, 주식하는법
```

## 5. 고정 댓글

```
당신은 몇 개를 틀리셨나요? 댓글로 남겨 주세요.
1~5번 가운데 가장 헷갈렸던 선택은 몇 번이었나요?
과거 자료로 만든 연구·교육용 테스트이며, 투자 권유가 아닙니다.
```

## 6. 언어별 제목·설명 (9개 언어 en·hi·id·pt·es-419·ja·de·vi·tr — 업로드 도구 localizations · 기본 언어 ko 는 1·2번)

```json
{
 "en": {
  "title": "Fear index at 36 in a crash: can you still buy as planned?",
  "description": "In the 4 years from the day the crash began, the S&P 500 rose more than 40%, yet Mr. Jeong lost 64% of his 100 million won.\nAt the five crossroads Mr. Jeong faced during the crash, test which choice you would have made. Just count how many of your decisions gave in to fear.\n\n■ Chapters\n0:00 What happened to Mr. Jeong\n0:37 Choice 1 When fear is at its peak\n2:30 Choice 2 The day fear faded\n3:51 Choice 3 The stock that had fallen the most\n5:14 Choice 4 The day of a big rally\n6:34 Choice 5 When the low breaks again\n7:53 Your result\n8:15 Summary\n\n■ Sources\n- Prices and indexes: Yahoo Finance (S&P 500 ^GSPC, total return index incl. dividends ^SP500TR, fear index ^VIX, 13-week US Treasury bill ^IRX, MRNA and NFLX adjusted close)\n- S&P 500 constituents list: github.com/datasets/s-and-p-500-companies\n\n■ Please note\nThis test is not an official exam; we made it ourselves from real historical data. All of it is past data, and there is no guarantee the future will be the same.\nThis video is not investment advice and does not recommend buying or selling any particular stock.\n\n#StockTest #USStocks"
 },
 "hi": {
  "title": "फियर इंडेक्स 36 पर भारी गिरावट: क्या आप योजना के मुताबिक़ ख़रीद पाएँगे?",
  "description": "भारी गिरावट शुरू होने के दिन से 4 साल में S&P 500 इंडेक्स 40% से ज़्यादा चढ़ा, फिर भी मिस्टर जियोंग ने अपने 10 करोड़ वॉन में से 64% गँवा दिए।\nगिरावट के दौरान मिस्टर जियोंग के सामने आए पाँच मोड़ों पर आप क्या चुनते, टेस्ट करके देखिए। बस गिनिए कि आपके कितने फ़ैसले डर से हारे।\n\n■ चैप्टर\n0:00 मिस्टर जियोंग के साथ क्या हुआ\n0:37 चुनाव 1 जब डर सबसे बड़ा हो\n2:30 चुनाव 2 जिस दिन डर थमा\n3:51 चुनाव 3 सबसे ज़्यादा गिरा शेयर\n5:14 चुनाव 4 बड़े उछाल का दिन\n6:34 चुनाव 5 जब निचला स्तर फिर टूटा\n7:53 आपका नतीजा\n8:15 सारांश\n\n■ स्रोत\n- शेयर भाव और इंडेक्स: Yahoo Finance (S&P 500 ^GSPC, डिविडेंड सहित इंडेक्स ^SP500TR, फियर इंडेक्स ^VIX, 13 हफ़्ते का अमेरिकी ट्रेज़री बिल ^IRX, MRNA और NFLX का एडजस्टेड क्लोज़)\n- S&P 500 कंपनियों की सूची: github.com/datasets/s-and-p-500-companies\n\n■ ध्यान दें\nयह टेस्ट कोई आधिकारिक परीक्षा नहीं है, हमने इसे असली पुराने आँकड़ों से ख़ुद बनाया है। सब पुराने आँकड़े हैं, और आगे भी ऐसा ही होगा, इसकी कोई गारंटी नहीं।\nयह वीडियो निवेश की सलाह नहीं है, और किसी ख़ास शेयर को ख़रीदने या बेचने के लिए नहीं कहता।\n\n#शेयरटेस्ट #अमेरिकीशेयर"
 },
 "id": {
  "title": "Indeks ketakutan 36 saat pasar anjlok, bisakah Anda tetap beli sesuai rencana?",
  "description": "Dalam 4 tahun sejak hari pasar mulai anjlok, indeks S&P 500 naik lebih dari 40%, tetapi Pak Jeong kehilangan 64% dari 100 juta won miliknya.\nUji pilihan Anda di lima persimpangan yang dihadapi Pak Jeong saat pasar anjlok. Cukup hitung berapa keputusan Anda yang kalah oleh rasa takut.\n\n■ Bab\n0:00 Apa yang terjadi pada Pak Jeong\n0:37 Pilihan 1 Saat rasa takut memuncak\n2:30 Pilihan 2 Hari rasa takut mereda\n3:51 Pilihan 3 Saham yang paling anjlok\n5:14 Pilihan 4 Hari pantulan besar\n6:34 Pilihan 5 Saat titik terendah tertembus lagi\n7:53 Hasil Anda\n8:15 Rangkuman\n\n■ Sumber\n- Harga saham dan indeks: Yahoo Finance (S&P 500 ^GSPC, indeks termasuk dividen ^SP500TR, indeks ketakutan ^VIX, surat utang AS 13 minggu ^IRX, harga penutupan disesuaikan MRNA dan NFLX)\n- Daftar perusahaan S&P 500: github.com/datasets/s-and-p-500-companies\n\n■ Perlu diketahui\nTes ini bukan ujian resmi, melainkan kami buat sendiri dari data nyata masa lalu. Semuanya data masa lalu, dan tidak ada jaminan masa depan akan sama.\nVideo ini bukan ajakan investasi dan bukan saran untuk membeli atau menjual saham tertentu.\n\n#TesSaham #SahamAS"
 },
 "pt": {
  "title": "Índice do medo em 36 numa queda forte: você conseguiria comprar como planejou?",
  "description": "Nos 4 anos desde o dia em que a queda começou, o índice S&P 500 subiu mais de 40%, mas o Sr. Jeong perdeu 64% dos seus 100 milhões de wons.\nTeste o que você teria escolhido nas cinco encruzilhadas que o Sr. Jeong enfrentou durante a queda. Basta contar quantas das suas decisões cederam ao medo.\n\n■ Capítulos\n0:00 O que aconteceu com o Sr. Jeong\n0:37 Escolha 1 Quando o medo está no auge\n2:30 Escolha 2 O dia em que o medo passou\n3:51 Escolha 3 A ação que mais tinha caído\n5:14 Escolha 4 O dia do grande repique\n6:34 Escolha 5 Quando o fundo é rompido de novo\n7:53 Seu resultado\n8:15 Resumo\n\n■ Fontes\n- Preços e índices: Yahoo Finance (S&P 500 ^GSPC, índice com dividendos ^SP500TR, índice do medo ^VIX, título do Tesouro americano de 13 semanas ^IRX, fechamento ajustado de MRNA e NFLX)\n- Lista de empresas do S&P 500: github.com/datasets/s-and-p-500-companies\n\n■ Aviso\nEste teste não é uma prova oficial; nós o criamos com dados reais do passado. Todos são dados passados, e não há garantia de que o futuro será igual.\nEste vídeo não é recomendação de investimento nem sugestão para comprar ou vender qualquer ação específica.\n\n#TesteDeAções #AçõesAmericanas"
 },
 "es-419": {
  "title": "Índice del miedo en 36 en pleno desplome: ¿podrías comprar según tu plan?",
  "description": "En los 4 años desde el día en que empezó el desplome, el índice S&P 500 subió más del 40%, pero el señor Jeong perdió el 64% de sus 100 millones de wones.\nPon a prueba qué habrías elegido en las cinco encrucijadas que enfrentó el señor Jeong durante el desplome. Solo cuenta cuántas de tus decisiones cedieron al miedo.\n\n■ Capítulos\n0:00 Qué le pasó al señor Jeong\n0:37 Decisión 1 Cuando el miedo está en su punto máximo\n2:30 Decisión 2 El día en que el miedo se calmó\n3:51 Decisión 3 La acción que más había caído\n5:14 Decisión 4 El día del gran rebote\n6:34 Decisión 5 Cuando se rompe otra vez el mínimo\n7:53 Tu resultado\n8:15 Resumen\n\n■ Fuentes\n- Precios e índices: Yahoo Finance (S&P 500 ^GSPC, índice con dividendos ^SP500TR, índice del miedo ^VIX, letra del Tesoro de EE. UU. a 13 semanas ^IRX, cierre ajustado de MRNA y NFLX)\n- Lista de empresas del S&P 500: github.com/datasets/s-and-p-500-companies\n\n■ Aviso\nEsta prueba no es un examen oficial; la creamos nosotros con datos reales del pasado. Todo son datos pasados y no hay garantía de que el futuro sea igual.\nEste video no es asesoría de inversión ni una recomendación para comprar o vender ninguna acción en particular.\n\n#PruebaDeAcciones #AccionesDeEEUU"
 },
 "ja": {
  "title": "恐怖指数36の暴落相場、あなたは計画どおり買えますか？",
  "description": "暴落が始まった日から4年間でS&P 500指数は40%以上上がったのに、チョンさんは1億ウォンのうち64%を失いました。\nチョンさんが暴落の中で直面した五つの分かれ道で、あなたならどれを選んだか、テストしてみてください。恐怖に負けた決断がいくつか数えるだけです。\n\n■ チャプター\n0:00 チョンさんに何が\n0:37 選択1 恐怖が最も大きいとき\n2:30 選択2 恐怖が収まった日\n3:51 選択3 最も下落していた銘柄\n5:14 選択4 大きく反発した日\n6:34 選択5 底が再び割れたとき\n7:53 あなたの結果\n8:15 まとめ\n\n■ 出典\n- 株価・指数：Yahoo Finance（S&P 500 ^GSPC・配当込み指数 ^SP500TR・恐怖指数 ^VIX・13週米国債 ^IRX・MRNA・NFLXの調整後終値）\n- S&P 500構成銘柄リスト：github.com/datasets/s-and-p-500-companies\n\n■ お知らせ\nこのテストは公式の試験ではなく、実際の過去データをもとに独自に作ったものです。すべて過去のデータで、今後も同じになる保証はありません。\nこの動画は投資の勧誘ではなく、特定の銘柄の売買をすすめるものではありません。\n\n#株式テスト #米国株"
 },
 "de": {
  "title": "Angstindex 36 im Crash: Kannst du noch nach Plan kaufen?",
  "description": "In den 4 Jahren ab dem Tag, an dem der Crash begann, stieg der S&P 500 um mehr als 40 % – doch Herr Jeong verlor 64 % seiner 100 Millionen Won.\nTeste, wie du an den fünf Weggabelungen entschieden hättest, vor denen Herr Jeong im Crash stand. Zähl einfach, wie oft du der Angst nachgegeben hast.\n\n■ Kapitel\n0:00 Was ist mit Herrn Jeong passiert\n0:37 Wahl 1 Wenn die Angst am größten ist\n2:30 Wahl 2 Der Tag, an dem die Angst nachließ\n3:51 Wahl 3 Die Aktie, die am stärksten gefallen war\n5:14 Wahl 4 Der Tag der großen Erholung\n6:34 Wahl 5 Wenn das Tief erneut bricht\n7:53 Dein Ergebnis\n8:15 Fazit\n\n■ Quellen\n- Kurse und Indizes: Yahoo Finance (S&P 500 ^GSPC, Index inkl. Dividenden ^SP500TR, Angstindex ^VIX, 13-Wochen-US-Schatzwechsel ^IRX, bereinigte Schlusskurse von MRNA und NFLX)\n- Liste der S&P-500-Unternehmen: github.com/datasets/s-and-p-500-companies\n\n■ Hinweis\nDieser Test ist keine offizielle Prüfung, sondern selbst erstellt aus echten historischen Daten. Alles sind Vergangenheitsdaten, und es gibt keine Garantie, dass es künftig genauso kommt.\nDieses Video ist keine Anlageberatung und keine Empfehlung, eine bestimmte Aktie zu kaufen oder zu verkaufen.\n\n#AktienTest #USAktien"
 },
 "vi": {
  "title": "Chỉ số sợ hãi 36 giữa cơn sập, bạn có mua đúng kế hoạch được không?",
  "description": "Trong 4 năm kể từ ngày cơn sập bắt đầu, chỉ số S&P 500 tăng hơn 40%, nhưng anh Jeong đã mất 64% trong số 100 triệu won của mình.\nHãy thử xem bạn sẽ chọn gì ở năm ngã rẽ mà anh Jeong gặp giữa cơn sập. Chỉ cần đếm xem có bao nhiêu quyết định thua nỗi sợ.\n\n■ Chương\n0:00 Chuyện gì đã xảy ra với anh Jeong\n0:37 Lựa chọn 1 Khi nỗi sợ lên đỉnh\n2:30 Lựa chọn 2 Ngày nỗi sợ lắng xuống\n3:51 Lựa chọn 3 Mã giảm mạnh nhất\n5:14 Lựa chọn 4 Ngày hồi phục mạnh\n6:34 Lựa chọn 5 Khi đáy lại bị thủng\n7:53 Kết quả của bạn\n8:15 Tổng kết\n\n■ Nguồn\n- Giá cổ phiếu và chỉ số: Yahoo Finance (S&P 500 ^GSPC, chỉ số gồm cổ tức ^SP500TR, chỉ số sợ hãi ^VIX, tín phiếu kho bạc Mỹ 13 tuần ^IRX, giá đóng cửa điều chỉnh của MRNA và NFLX)\n- Danh sách công ty S&P 500: github.com/datasets/s-and-p-500-companies\n\n■ Lưu ý\nBài kiểm tra này không phải kỳ thi chính thức mà do chúng tôi tự làm từ dữ liệu thực tế trong quá khứ. Tất cả đều là dữ liệu quá khứ và không có gì đảm bảo tương lai sẽ giống vậy.\nVideo này không phải lời khuyên đầu tư, cũng không khuyến nghị mua hay bán bất kỳ cổ phiếu cụ thể nào.\n\n#TestCổPhiếu #CổPhiếuMỹ"
 },
 "tr": {
  "title": "Korku endeksi 36'da çöküş: Planladığınız gibi alım yapabilir misiniz?",
  "description": "Çöküşün başladığı günden itibaren 4 yılda S&P 500 endeksi %40'tan fazla yükseldi, ama Jeong Bey 100 milyon wonunun %64'ünü kaybetti.\nJeong Bey'in çöküş sırasında karşılaştığı beş yol ayrımında siz olsanız ne seçerdiniz, test edin. Korkuya yenilen kararlarınızı saymanız yeterli.\n\n■ Bölümler\n0:00 Jeong Bey'e ne oldu\n0:37 Seçim 1 Korkunun zirvede olduğu an\n2:30 Seçim 2 Korkunun dindiği gün\n3:51 Seçim 3 En çok düşmüş hisse\n5:14 Seçim 4 Güçlü toparlanma günü\n6:34 Seçim 5 Dip yeniden kırıldığında\n7:53 Sonucunuz\n8:15 Özet\n\n■ Kaynaklar\n- Hisse fiyatları ve endeksler: Yahoo Finance (S&P 500 ^GSPC, temettü dahil endeks ^SP500TR, korku endeksi ^VIX, 13 haftalık ABD hazine bonosu ^IRX, MRNA ve NFLX düzeltilmiş kapanış fiyatları)\n- S&P 500 şirket listesi: github.com/datasets/s-and-p-500-companies\n\n■ Bilgilendirme\nBu test resmî bir sınav değildir; gerçek geçmiş verilerle kendimiz hazırladık. Hepsi geçmiş veridir ve geleceğin aynı olacağının garantisi yoktur.\nBu video yatırım tavsiyesi değildir; belirli bir hisseyi almanızı ya da satmanızı önermez.\n\n#BorsaTesti #ABDHisseleri"
 }
}
```
- 한국어 1·2번을 그대로 옮김 (챕터 시각 = 2번 — 한국어 챕터를 다시 계산하면 여기도 같이 고친다) · '알려 드립니다'·해시태그는 1편(`ppalli-test-2026-11`)과 같은 번역 · 정씨 = Mr. Jeong·मिस्टर जियोंग·Pak Jeong·Sr. Jeong·señor Jeong·チョンさん·Herr Jeong·anh Jeong·Jeong Bey · 공포 지수 = fear index (VIX)·फियर इंडेक्स·indeks ketakutan·índice do medo·índice del miedo·恐怖指数·Angstindex·chỉ số sợ hãi·korku endeksi.
- 언어별 자막 `subs/gongpo-test-2026-11.<언어>.srt` (대본 `subs/gongpo-test-2026-11.<언어>.txt` — 한국어와 문장 1:1) · 언어별 썸네일 `thumbnails/<언어>/thumbnail_1.jpg` (업로드 도구는 한국어 `thumbnails/thumbnail_1.jpg` 만 올림 — 언어별 썸네일은 스튜디오에서 언어별로 넣을 수 있을 때 씀).

## 7. 업로드 설정

| 항목 | 값 |
|---|---|
| 공개 상태 | 비공개로 올린 뒤 예약 공개 |
| 썸네일 | (아직 없음 — 4편 썸네일 문구·그림은 대본 통과 뒤) |
| 자막 | `gongpo-test-2026-11.srt` (오디오 뒤 `align-audio` 로 맞춘 것) |
| 자막 올리기 | 언어별 (한국어 `gongpo-test-2026-11.srt` + `subs/gongpo-test-2026-11.<언어>.srt` 9개 — 화면에는 굽지 않음) |
| 기본 언어 | ko |
| 언어별 썸네일 | `thumbnails/<언어>/thumbnail_1.jpg` 9개 (`node video/render/thumb.mjs stock/source/gongpo-test-2026-11/thumbnails/<언어>/thumbnail_1.json`) |
| 카테고리 | 교육 |
| 동영상 언어 | 한국어 |
| 시청자층 | 아동용 아님 |
| 유료 프로모션 | 없음 |
| 변경되거나 합성된 콘텐츠 | **예** (내레이션이 AI 음성) |

## 8. 점검

- 설명란 숫자는 대본·`longform_ep4.py` v1.0 출력에 있는 것만 썼다 (64%·1억 원·4년·40% 넘게 — S&P 500 가격 +42.7%, 배당 포함 +51.4%).
- 과거 자료라 보장은 없음·공식 시험 아님·가상 인물·투자 권유 아님은 2번 '알려 드립니다'에.

## 9. 결과 (업로드 후)

- (아직 없음)
