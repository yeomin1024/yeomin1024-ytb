# ppalli-test-2026-11 업로드 시트

버전: v1.16 — 2026-11-06 — 1-1번 B 말풍선 꼬리 · C '주식으로' 노랑 (사용자 지시 "설마 나도 말풍선 삐뚤어져수 수정하고 주식으로는 노란색 칠해").
이전 v1.15 — 2026-11-06 — 1-1번 B·C 썸네일 문구·말풍선 (사용자 지시 "이런 5가지 선택~ 무조건 주식 손해~ 이렇게 수정하고 보조문구는 설마 나도? 설정하고 주식으로 돈 버는 ~ 상위10% 이렇게 수정하고 보조 문구는 주식 손해만 보네...  수정해").
이전 v1.14 — 2026-11-05 — 1-1번 A/B 테스트 제목·썸네일 짝 (사용자 지시 "1. 주식 투자 중 이런 선택을 한다면 당신은 무조건 손해볼겁니다 2. 주식으로 돈버는 상위 %는 절대 이렇게 선택하지 않습니다 이 두가지 제목에 맞춰 썸네일 문구들 새로 만들어봐 상위%는 몇프로인지 평균 수치로 채우고" → "1편 ab 테스트에 쓸거야") · 썸네일 2·3 문구 새로.
이전 v1.13 — 2026-11-05 — 외국어 설정 (사용자 지시 "외국어 자막, 제목, 썸네일 등 외국어 설정에 필요한 것들 생성하고 지시사항에 반영해 이건 영상이 렌더까지 완료되면 하는거야"): 6번 언어별 제목·설명 9개 언어(en·hi·id·pt·es-419·ja·de·vi·tr — 1·2번 그대로 옮김, 챕터 시각 같음) · 자막 = 한국어 + 언어별 SRT 9개 (`subs/`, `tools/subs_tool.py` build — 완성 영상의 문장 시각) · 언어별 썸네일 `thumbnails/<언어>/thumbnail_1.jpg` (`thumb.mjs` v1.2 lang) · 업로드 설정에 기본 언어 ko · 자막 올리기 언어별 · 섹션 번호 6→7·7→8·8→9.
이전 v1.12 — 2026-11-05 — 설명란 줄임·태그 늘림 (사용자 지시 "김씨는 실제 숫자로 만든 가상의 인물입니다. 내레이션은 AI 음성이고, 그림은 AI로 만든 연출입니다. 다섯 가지 선택, 계산기준빼고 태그도 더 추가 하는걸로 설명 만들자 지시사항에도 반영해" — `stock/guides/quick_board.md` 규칙 45): '다섯 가지 선택'·'계산 기준'·'○씨는 가상의 인물'·'AI 음성/그림' 줄 뺌 · 태그 24개(편 낱말 + 실제 영상 태그 `stock/tag_candidates.md`).
이전 v1.11 — 2026-11-05 — 설명란 끝을 면세 편 꼴로: '그림은 AI로 만든 연출' + 해시태그 2개 (사용자 "영상 설명 좀 면세 영상 올릴 때 처럼 자세하게") · 실험 썸네일 2·3 을 실사 TH-PHOTO2 로 다시 그림(옛 TH-ART 얼굴 그림이 남아 있었음).
이전 v1.10 — 2026-11-05 — 완성 영상을 저장소에 둠 `stock/videos/ppalli-test-2026-11.mp4` (사용자 지시 "그냥 깃허브에 올려 1편 영상들") → 새 세션은 다시 렌더 없이 `python3 tools/youtube_upload.py stock ppalli-test-2026-11 --video stock/videos/ppalli-test-2026-11.mp4 --publish-at 2026-11-12T08:00:00Z`.
이전 v1.9 — 2026-11-04 — 챕터 시각 채움 (대본 v17 음성) · 예약 공개 2026-11-12T08:00:00Z (한국 11월 12일 17시 — 사용자 지시 "1편은 각각 일주일 후로 자동 예약 걸어서 업로드 해", 짝 쇼츠와 같은 시각) · 썸네일 줄 = 실사 TH-PHOTO2.
이전 v1.8 — 2026-11-04 — 대본: 선택마다 질문 뒤 '선택해 보세요.' · '3, 2, 1.' (사용자 지시 "매수 하시겠습니까? 선택 항목 다음에 선택해보세요. 멘트 추가하고 3, 2, 1 카운트 후에 정답 얘기하도록수정해 다른 대본도 그렇게 하고") — 문장 10개 늘어 챕터 번호 다시.
이전 v1.7 — 2026-11-04 — 새 음성(7:11.9, tts v1.17)으로 챕터 시각 채움 · 챕터 제목 2개를 정답이 안 보이게 ('현금 남기기' → '얼마를 넣을까' · '손절' → '실적이 무너진 날' — 규칙 '챕터 제목에 정답을 쓰지 않는다').
이전 v1.6 — 2026-11-04 — 대본 v16 (판 피드백 2건: 2번 하락을 그날 바로 뒤 S&P 500 10%로 · 5번 업종 통계 지움) · 계산 기준 2번 · 챕터 번호.
이전 v1.5 — 2026-11-04 — 대본 평가판 1편 피드백 11건을 1~4편 모두에 (인물 결과 문장 지움 → '○씨의 결과' 챕터 없앰) — 챕터 번호 다시.
이전 v1.4 — 2026-11-04 — 대본 질문형(선택마다 바로 정답·해설, quick_board 규칙 25) — 챕터 문장 번호 다시 · \'정답과 해설\' 챕터 없앰.
이전 v1.3 — 2026-11-02 — 대본 v11 (대본 평가판 3차 4건 — 보기 'A,'·'B,' · 2번 현금 수치·3번 비율 수치는 보기에서 빼고 해설에 '예를 들어' · 정리 공통점 두 줄 삭제) · 챕터 번호 다시
이전 v1.2 — 2026-11-02 — 대본 v10 (피드백판 2차 5건 — S&P 500 · 1번 '사지 않음' · 3번 5%마다 3분의 1 · 4번 바로 매도, 김씨 −74%) · 숫자 longform_items.py v2.3 (`sp_1편_v2.3`)
이전 v1.1 — 2026-11-02 — 대본 v9 (피드백판 1편 롱폼 10건 반영 — 업스타트·현금 3천만·2025 관세 하락장 기준·C3.ai·아이온큐 비중, 김씨 −73%) · 숫자 longform_items.py v2.2
이전 v1.0 — 2026-11-01 — 1편 「주식 투자 실패하는 사람들은 절대 통과 못하는 테스트」 (사용자 지시 2026-11-01 "1편만 영상 관련 소스 만들어봐") · 대본 v8 (104문장)
기준 파일: 대본 `ppalli-test-2026-11.txt` v10 · 숫자 `stock/topics/precheck/longform_items.py` v2.4 (`longform_items_2026-11-04.json` · `sp_1편_v2.3`) · 그래프 `calc/series.py` v1.0 · 오디오·SRT는 아직 없음 (Kaggle TTS 뒤 `align-audio`)

> 업로드 채널 = 주식 채널(STOCK LAB) — 도구는 키의 채널이 다르면 멈춤. 영상: `node video/render/render.mjs video stock ppalli-test-2026-11` 뒤 `stock/out/ppalli-test-2026-11/final_1080p.mp4`.
> 연구·교육용 콘텐츠 — 투자 상담이나 권유가 아님.

## 1. 제목 (사용자 제목 — 주제 판 피드백 2026-11-03)

```
주식 투자 실패하는 사람들은 절대 통과 못하는 테스트
```

## 1-1. A/B 테스트 (스튜디오 '테스트 및 비교' — 제목·썸네일 짝, 2026-11-05 사용자 지시 "1. 주식 투자 중 이런 선택을 한다면 당신은 무조건 손해볼겁니다 2. 주식으로 돈버는 상위 %는 절대 이렇게 선택하지 않습니다 이 두가지 제목에 맞춰 썸네일 문구들 새로 만들어봐 상위%는 몇프로인지 평균 수치로 채우고" → "1편 ab 테스트에 쓸거야")

| 안 | 제목 | 썸네일 | 문구 (아래 2줄 · 말풍선) |
|---|---|---|---|
| A (본안) | 주식 투자 실패하는 사람들은 절대 통과 못하는 테스트 | `thumbnails/thumbnail_1.jpg` | 주식 투자 실패하는 사람들은 / 절대 통과 못하는 테스트 · 「-50%, -70% 손실」「설마 나도?」 |
| B | 주식 투자 중 이런 선택을 한다면 당신은 무조건 손해볼겁니다 | `thumbnails/thumbnail_2.jpg` | **이런 5가지 선택**을 한다면 / 무조건 **주식 손해** 봅니다 · 「설마 나도?」 |
| C | 주식으로 돈버는 상위 10%는 절대 이렇게 선택하지 않습니다 | `thumbnails/thumbnail_3.jpg` | **주식으로** 돈 버는 **상위 10%**는 / **절대 이렇게** 선택 안 합니다 · 「주식 손해만 보네...」 |

- 2026-11-06 B 말풍선 꼬리를 평평한 아래쪽으로(삐뚤어 보임) · C '주식으로' 노랑 (사용자 지시 "설마 나도 말풍선 삐뚤어져수 수정하고 주식으로는 노란색 칠해").
- 2026-11-06 문구·말풍선 고침 (사용자 지시 "이런 5가지 선택~ 무조건 주식 손해~ 이렇게 수정하고 보조문구는 설마 나도? 설정하고 주식으로 돈 버는 ~ 상위10% 이렇게 수정하고 보조 문구는 주식 손해만 보네...  수정해").
- 'A/B 테스트' 는 API 로 못 함 — 사용자가 스튜디오에서 (영상 → 제목 옆 '테스트 및 비교' → 제목·썸네일 3안). 그림은 셋 다 본안과 같은 실사(`images/TH-PHOTO2.jpg`), 문구만 다름.
- **'상위 10%'** = 사용자 지시 '평균 수치로' → 흔히 인용되는 '개인 투자자 10%만 번다(90%는 잃는다)' 값. ⚠ 이 값을 직접 밝힌 2020년대 1차 연구는 찾지 못함 (2026-11-05 검색 — 자본시장연구원 2021: 2020년 3~10월 개인 약 20만 명 가운데 약 46% 손실 · 1편 영상 안에는 이 숫자를 증명하는 장면 없음, CLAUDE.md '숫자는 대본이 증명'과 어긋남 — 사용자 확인 필요).
- 제목 길이 (`title_fit.py`): B 33자 — PC 다음 동영상(좁은 화면)만 3줄 ❌ · C 33자 ✅. '무조건'·'절대'는 반론 페르소나 K8 과장 낱말(`board_check.py`) — 사용자 제목이라 그대로.

## 2. 설명란 (그대로 복사)

```
지난 3년여 동안 S&P 500 지수는 70% 넘게 올랐는데, 김씨는 1억 원 가운데 74%를 잃었습니다.
김씨가 마주했던 다섯 번의 갈림길에서, 당신이라면 어떤 선택을 했을지 테스트해 보세요. 틀린 개수만 세면 됩니다.

■ 챕터
0:00 김씨에게 무슨 일이
0:31 선택 1 남들이 좋다는 종목
1:41 선택 2 얼마를 넣을까
2:43 선택 3 하락장의 기준
4:14 선택 4 실적이 무너진 날
5:44 선택 5 한 종목의 비중
6:55 당신의 결과
7:16 정리

■ 출처
- 손실 종목 버티기: Terrance Odean (1998), "Are Investors Reluctant to Realize Their Losses?", Journal of Finance

■ 알려 드립니다
이 테스트는 공식 시험이 아니라, 실제 과거 데이터로 직접 만든 것입니다. 모두 과거 자료이고, 앞으로도 꼭 같다는 보장은 없습니다.
이 영상은 투자 권유가 아니며, 특정 종목을 사거나 팔라는 뜻이 아닙니다.

#주식테스트 #미국주식
```

## 3. 챕터 다시 계산하기 (문장 번호 기준 — 오디오·SRT 가 생긴 뒤)

```
python tools/srt_tool.py upload stock/source/ppalli-test-2026-11/ppalli-test-2026-11.txt stock/source/ppalli-test-2026-11/ppalli-test-2026-11.srt --chapters "1=김씨에게 무슨 일이;8=선택 1 남들이 좋다는 종목;25=선택 2 얼마를 넣을까;40=선택 3 하락장의 기준;59=선택 4 실적이 무너진 날;78=선택 5 한 종목의 비중;93=당신의 결과;97=정리"
```
- 챕터 제목에 정답을 쓰지 않는다 (해설 전 단서 금지 — 사용자 지시 2026-11-01 "도입부 부터 날짜 같은 정답을 알 수 있는 요소 말하지마").

## 4. 태그

```
주식 테스트, 주식 투자 습관, 투자 실패, 손절, 분할매수, 분산투자, 비중 조절, 비상금, 하락장, 나스닥, 주식, 주식투자, 미국주식, 주식초보, 주린이, 주식공부, 주식기초, 투자공부, 투자마인드, 개미투자자, 초보투자자, 장기투자, S&P500, 주식하는법
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
  "title": "The Test People Who Fail at Stock Investing Can Never Pass",
  "description": "Over the past 3-plus years, the S&P 500 rose more than 70%, yet Mr. Kim lost 74% of his 100 million won.\nAt the five crossroads Mr. Kim faced, test which choice you would make. Just count how many you get wrong.\n\n■ Chapters\n0:00 What happened to Mr. Kim\n0:31 Choice 1 The stock everyone loves\n1:41 Choice 2 How much to put in\n2:43 Choice 3 A rule for falling markets\n4:14 Choice 4 The day earnings collapsed\n5:44 Choice 5 How much in one stock\n6:55 Your result\n7:16 Summary\n\n■ Source\n- Holding on to losing stocks: Terrance Odean (1998), \"Are Investors Reluctant to Realize Their Losses?\", Journal of Finance\n\n■ Please note\nThis test is not an official exam; we made it ourselves from real historical data. All of it is past data, and there is no guarantee the future will be the same.\nThis video is not investment advice and does not recommend buying or selling any particular stock.\n\n#StockTest #USStocks"
 },
 "hi": {
  "title": "शेयर निवेश में नाकाम लोग यह टेस्ट कभी पास नहीं कर पाते",
  "description": "पिछले 3 साल से कुछ ज़्यादा समय में S&P 500 इंडेक्स 70% से ज़्यादा चढ़ा, लेकिन मिस्टर किम ने 10 करोड़ वॉन में से 74% गँवा दिए।\nमिस्टर किम के सामने आए पाँच मोड़ों पर आप क्या चुनते, यह टेस्ट करके देखिए। बस ग़लत जवाब गिनने हैं।\n\n■ चैप्टर\n0:00 मिस्टर किम के साथ क्या हुआ\n0:31 चुनाव 1 वह शेयर जिसे सब अच्छा कहते हैं\n1:41 चुनाव 2 कितना लगाएँ\n2:43 चुनाव 3 गिरते बाज़ार का नियम\n4:14 चुनाव 4 जिस दिन कमाई ढह गई\n5:44 चुनाव 5 एक शेयर का हिस्सा\n6:55 आपका नतीजा\n7:16 सारांश\n\n■ स्रोत\n- घाटे वाले शेयर पकड़े रहना: Terrance Odean (1998), \"Are Investors Reluctant to Realize Their Losses?\", Journal of Finance\n\n■ ध्यान दें\nयह टेस्ट कोई आधिकारिक परीक्षा नहीं है, हमने इसे असली पुराने आँकड़ों से ख़ुद बनाया है। सब पुराने आँकड़े हैं, और आगे भी ऐसा ही होगा, इसकी कोई गारंटी नहीं।\nयह वीडियो निवेश की सलाह नहीं है, और किसी ख़ास शेयर को ख़रीदने या बेचने के लिए नहीं कहता।\n\n#शेयरटेस्ट #अमेरिकीशेयर"
 },
 "id": {
  "title": "Tes yang Tidak Akan Pernah Bisa Dilewati Orang yang Gagal Investasi Saham",
  "description": "Dalam 3 tahun lebih terakhir, indeks S&P 500 naik lebih dari 70%, tapi Pak Kim kehilangan 74% dari 100 juta won miliknya.\nDi lima persimpangan yang dihadapi Pak Kim, uji pilihan apa yang akan Anda ambil. Cukup hitung jawaban yang salah.\n\n■ Bab\n0:00 Apa yang terjadi pada Pak Kim\n0:31 Pilihan 1 Saham yang dipuji semua orang\n1:41 Pilihan 2 Berapa yang dimasukkan\n2:43 Pilihan 3 Aturan saat pasar turun\n4:14 Pilihan 4 Hari kinerja runtuh\n5:44 Pilihan 5 Porsi satu saham\n6:55 Hasil Anda\n7:16 Rangkuman\n\n■ Sumber\n- Menahan saham rugi: Terrance Odean (1998), \"Are Investors Reluctant to Realize Their Losses?\", Journal of Finance\n\n■ Perlu diketahui\nTes ini bukan ujian resmi, melainkan kami buat sendiri dari data nyata masa lalu. Semuanya data masa lalu, dan tidak ada jaminan masa depan akan sama.\nVideo ini bukan ajakan investasi dan bukan saran untuk membeli atau menjual saham tertentu.\n\n#TesSaham #SahamAS"
 },
 "pt": {
  "title": "O teste em que quem fracassa com ações nunca passa",
  "description": "Em pouco mais de 3 anos, o índice S&P 500 subiu mais de 70%, mas o Sr. Kim perdeu 74% dos seus 100 milhões de wons.\nNas cinco encruzilhadas que o Sr. Kim enfrentou, teste qual seria a sua escolha. É só contar quantas você errou.\n\n■ Capítulos\n0:00 O que aconteceu com o Sr. Kim\n0:31 Escolha 1 A ação que todo mundo elogia\n1:41 Escolha 2 Quanto investir\n2:43 Escolha 3 Uma regra para a queda\n4:14 Escolha 4 O dia em que os resultados desabaram\n5:44 Escolha 5 O peso de uma ação\n6:55 Seu resultado\n7:16 Resumo\n\n■ Fonte\n- Segurar ações no prejuízo: Terrance Odean (1998), \"Are Investors Reluctant to Realize Their Losses?\", Journal of Finance\n\n■ Aviso\nEste teste não é uma prova oficial; nós o criamos com dados reais do passado. Todos são dados passados, e não há garantia de que o futuro será igual.\nEste vídeo não é recomendação de investimento nem sugestão para comprar ou vender qualquer ação específica.\n\n#TesteDeAções #AçõesAmericanas"
 },
 "es-419": {
  "title": "La prueba que quienes fracasan en la bolsa nunca logran pasar",
  "description": "En poco más de 3 años, el índice S&P 500 subió más de 70%, pero el señor Kim perdió el 74% de sus 100 millones de wones.\nEn las cinco encrucijadas que enfrentó el señor Kim, pon a prueba qué elegirías tú. Solo cuenta cuántas fallas.\n\n■ Capítulos\n0:00 Qué le pasó al señor Kim\n0:31 Decisión 1 La acción que todos recomiendan\n1:41 Decisión 2 Cuánto invertir\n2:43 Decisión 3 Una regla para las caídas\n4:14 Decisión 4 El día que se derrumbaron los resultados\n5:44 Decisión 5 El peso de una sola acción\n6:55 Tu resultado\n7:16 Resumen\n\n■ Fuente\n- Aferrarse a acciones con pérdida: Terrance Odean (1998), \"Are Investors Reluctant to Realize Their Losses?\", Journal of Finance\n\n■ Aviso\nEsta prueba no es un examen oficial; la creamos nosotros con datos reales del pasado. Todo son datos pasados y no hay garantía de que el futuro sea igual.\nEste video no es asesoría de inversión ni una recomendación para comprar o vender ninguna acción en particular.\n\n#PruebaDeAcciones #AccionesDeEEUU"
 },
 "ja": {
  "title": "株式投資で失敗する人は絶対に合格できないテスト",
  "description": "この3年あまりでS&P 500指数は70%以上上がりましたが、キムさんは1億ウォンのうち74%を失いました。\nキムさんが直面した五つの分かれ道で、あなたならどんな選択をするかテストしてみてください。間違えた数を数えるだけです。\n\n■ チャプター\n0:00 キムさんに何が\n0:31 選択1 みんながいいと言う銘柄\n1:41 選択2 いくら入れるか\n2:43 選択3 下落相場のルール\n4:14 選択4 業績が崩れた日\n5:44 選択5 一つの銘柄の比率\n6:55 あなたの結果\n7:16 まとめ\n\n■ 出典\n- 含み損の銘柄を持ち続けること：Terrance Odean (1998), \"Are Investors Reluctant to Realize Their Losses?\", Journal of Finance\n\n■ お知らせ\nこのテストは公式の試験ではなく、実際の過去データをもとに独自に作ったものです。すべて過去のデータで、今後も同じになる保証はありません。\nこの動画は投資の勧誘ではなく、特定の銘柄の売買をすすめるものではありません。\n\n#株式テスト #米国株"
 },
 "de": {
  "title": "Der Test, den Leute, die an der Börse scheitern, nie bestehen",
  "description": "In gut 3 Jahren ist der S&P 500 um mehr als 70% gestiegen, doch Herr Kim hat 74% seiner 100 Millionen Won verloren.\nTeste an den fünf Weggabelungen, vor denen Herr Kim stand, wie du dich entscheiden würdest. Zähl einfach deine Fehler.\n\n■ Kapitel\n0:00 Was ist mit Herrn Kim passiert\n0:31 Wahl 1 Die Aktie, die alle lieben\n1:41 Wahl 2 Wie viel investieren\n2:43 Wahl 3 Eine Regel für fallende Märkte\n4:14 Wahl 4 Der Tag, an dem die Gewinne einbrachen\n5:44 Wahl 5 Der Anteil einer Aktie\n6:55 Dein Ergebnis\n7:16 Fazit\n\n■ Quelle\n- Am Verlierer festhalten: Terrance Odean (1998), \"Are Investors Reluctant to Realize Their Losses?\", Journal of Finance\n\n■ Hinweis\nDieser Test ist keine offizielle Prüfung, sondern selbst erstellt aus echten historischen Daten. Alles sind Vergangenheitsdaten, und es gibt keine Garantie, dass es künftig genauso kommt.\nDieses Video ist keine Anlageberatung und keine Empfehlung, eine bestimmte Aktie zu kaufen oder zu verkaufen.\n\n#AktienTest #USAktien"
 },
 "vi": {
  "title": "Bài kiểm tra mà người đầu tư cổ phiếu thất bại không bao giờ vượt qua được",
  "description": "Trong hơn 3 năm qua, chỉ số S&P 500 tăng hơn 70%, nhưng anh Kim lại mất 74% trong số 100 triệu won.\nỞ năm ngã rẽ mà anh Kim từng gặp, hãy thử xem bạn sẽ chọn gì. Chỉ cần đếm số câu sai.\n\n■ Chương\n0:00 Chuyện gì đã xảy ra với anh Kim\n0:31 Lựa chọn 1 Mã ai cũng khen\n1:41 Lựa chọn 2 Nên bỏ vào bao nhiêu\n2:43 Lựa chọn 3 Nguyên tắc khi thị trường giảm\n4:14 Lựa chọn 4 Ngày kết quả kinh doanh sụp đổ\n5:44 Lựa chọn 5 Tỷ trọng của một mã\n6:55 Kết quả của bạn\n7:16 Tổng kết\n\n■ Nguồn\n- Giữ mã đang lỗ: Terrance Odean (1998), \"Are Investors Reluctant to Realize Their Losses?\", Journal of Finance\n\n■ Lưu ý\nBài kiểm tra này không phải kỳ thi chính thức mà do chúng tôi tự làm từ dữ liệu thực tế trong quá khứ. Tất cả đều là dữ liệu quá khứ và không có gì đảm bảo tương lai sẽ giống vậy.\nVideo này không phải lời khuyên đầu tư, cũng không khuyến nghị mua hay bán bất kỳ cổ phiếu cụ thể nào.\n\n#TestCổPhiếu #CổPhiếuMỹ"
 },
 "tr": {
  "title": "Borsada başarısız olanların asla geçemediği test",
  "description": "Son 3 yılı aşkın sürede S&P 500 endeksi %70'ten fazla yükseldi, ama Kim Bey 100 milyon wonunun %74'ünü kaybetti.\nKim Bey'in karşılaştığı beş yol ayrımında sizin ne seçeceğinizi test edin. Sadece yanlışlarınızı saymanız yeterli.\n\n■ Bölümler\n0:00 Kim Bey'e ne oldu\n0:31 Seçim 1 Herkesin övdüğü hisse\n1:41 Seçim 2 Ne kadar yatırmalı\n2:43 Seçim 3 Düşen piyasa için kural\n4:14 Seçim 4 Kârların çöktüğü gün\n5:44 Seçim 5 Tek hissenin payı\n6:55 Sonucunuz\n7:16 Özet\n\n■ Kaynak\n- Zarardaki hisseyi tutmak: Terrance Odean (1998), \"Are Investors Reluctant to Realize Their Losses?\", Journal of Finance\n\n■ Bilgilendirme\nBu test resmî bir sınav değildir; gerçek geçmiş verilerle kendimiz hazırladık. Hepsi geçmiş veridir ve geleceğin aynı olacağının garantisi yoktur.\nBu video yatırım tavsiyesi değildir; belirli bir hisseyi almanızı ya da satmanızı önermez.\n\n#BorsaTesti #ABDHisseleri"
 }
}
```

- 한국어 1·2번을 그대로 옮김 (챕터 시각 = 2번 — 한국어 챕터를 다시 계산하면 여기도 같이 고친다) · 해시태그는 언어마다 2개 · 김씨 = Mr. Kim·Pak Kim·Sr. Kim·señor Kim·キムさん·Herr Kim·anh Kim·Kim Bey·मिस्टर किम.
- 언어별 자막 `subs/ppalli-test-2026-11.<언어>.srt` (대본 `subs/ppalli-test-2026-11.<언어>.txt` — 한국어와 문장 1:1) · 언어별 썸네일 `thumbnails/<언어>/thumbnail_1.jpg` (업로드 도구는 한국어 `thumbnails/thumbnail_1.jpg` 만 올림 — 언어별 썸네일은 스튜디오에서 언어별로 넣을 수 있을 때 씀).

## 7. 업로드 설정

| 항목 | 값 |
|---|---|
| 공개 상태 | 비공개로 올린 뒤 예약 공개 |
| 썸네일 | `thumbnails/thumbnail_1.jpg` (본안 — `node video/render/thumb.mjs stock/source/ppalli-test-2026-11/thumbnails/thumbnail_1.json`, 그림 `images/TH-PHOTO2.jpg` 실사) · 2·3 = A/B 테스트 실험안 (1-1번 짝 제목과 함께, 스튜디오 '테스트 및 비교') |
| 자막 | `ppalli-test-2026-11.srt` (오디오 뒤 `align-audio` 로 맞춘 것) |
| 자막 올리기 | 언어별 (한국어 `ppalli-test-2026-11.srt` + `subs/ppalli-test-2026-11.<언어>.srt` 9개 — 외국어는 CC · 한국어 자막은 화면에 구워져 있어 CC 를 켜면 아래 자막 띠와 겹칠 수 있음, 올리기 전 사용자 확인 — `stock/guides/quick_board.md` 규칙 46) |
| 기본 언어 | ko |
| 언어별 썸네일 | `thumbnails/<언어>/thumbnail_1.jpg` 9개 (`node video/render/thumb.mjs stock/source/ppalli-test-2026-11/thumbnails/<언어>/thumbnail_1.json`) |
| 카테고리 | 교육 |
| 동영상 언어 | 한국어 |
| 시청자층 | 아동용 아님 |
| 유료 프로모션 | 없음 |
| 변경되거나 합성된 콘텐츠 | **예** (내레이션이 AI 음성, 그림이 AI 연출) |

## 8. 점검

- 설명란 숫자는 대본·`longform_items.py` v2.3 출력에 있는 것만 썼다 (74%·1억 원·3년여·70% 넘게 — S&P 500 배당 포함 +76.1%, 가격 +68.7%, 3.2년).
- 대본에서 지운 문장(과거 자료라 보장은 없음·공식 시험 아님·가상 인물·투자 권유 아님 — 사용자 지시 "네줄모두 맘에 안드니까 삭제")은 2번 '알려 드립니다'에 넣었다.

## 9. 결과 (업로드 후)

- (아직 없음)
