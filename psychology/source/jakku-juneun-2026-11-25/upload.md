# jakku-juneun-2026-11-25 업로드 시트 (롱폼 · 심리)

버전: v1.4 — 2026-11-25 — 최초 (사용자 지시 "아래는 이제부터 적용할 영상 제작 공통 규칙이야 … 자꾸 주는 사람 영상 전반적으로 규칙 만족하도록 수정해서 아티팩트에 올려") · 생성 `psychology/source/upload_sheets.py` v1.4.
기준 파일: 대본 `jakku-juneun-2026-11-25.txt` (98문장) · 오디오 `narration.mp3` · 자막 `jakku-juneun-2026-11-25.srt`(align-audio — 실제 오디오) · 영상 `psychology/out/jakku-juneun-2026-11-25/final_1080p.mp4`(만스피 꼴 · `video/episodes/jakku-juneun-2026-11-25/`) · 썸네일 `thumbnails/thumbnail_1~3.jpg`.

> 업로드 채널 = 심리 채널. 연구·교육용 콘텐츠 — 심리 진단·치료가 아님.
> ⚠ `psychology/youtube_channel.json` 이 아직 없음 → 올리는 도구가 키의 채널을 확인하지 못함. PC 업로드 화면 psychology 탭에는 **심리 채널 키**만 넣는다 (처음 올린 뒤 화면의 '기억'으로 채널 ID 를 남김).

## 1. 제목 (본안)

```
필요 없다는데 자꾸 선물 주는 사람의 심리 3가지
```
- 짝 썸네일 `thumbnail_1.jpg` (「필요 없다는데 자꾸 주는 사람 / 거절해도 또 주는 이유」 + 말풍선 「너 주려고 챙겼지~ · 마음은 고마운데…」 — 그림 `images/TH-CHAR2.jpg` ChatGPT + 문구 코드 `thumb.mjs`).
- 제목·썸네일 문구는 package.json 그대로 — 페르소나 관문 title 단계 통과 (`persona_loop.json`). `title_fit`: 모바일·PC 모든 화면 2줄 안 ✅

## 1-1. 실험안 — 스튜디오 '테스트 및 비교'용 (API 로 올리지 않음 · 공개 뒤 사용자가 넣음)

| 안 | 제목 | 썸네일 |
|---|---|---|
| 실험 1 | (본안과 같음) | `thumbnail_2.jpg` — 보조 문구(말풍선) 없음 |
| 실험 2 | (본안과 같음) | `thumbnail_3.jpg` — 같은 낱말 · 강조 색 바꿈 + 노란 말풍선 |
- 글이 다른 실험 제목은 만들지 않음 (새 문구는 persona_loop title 단계부터).

## 2. 설명란 (그대로 복사)

```
필요 없다는데 자꾸 선물을 주는 사람, 거절해도 또 챙겨 주는 사람의 심리를 심리학 연구로 짚었습니다.
자꾸 주는 사람의 심리 세 가지와 받는 쪽이 불편한 이유, 소비기한, 그리고 인간관계를 지키며 서운하지 않게 거절하는 말까지 정리했습니다.

■ 챕터
0:00 필요 없다는데 자꾸 선물 주는 사람
0:00 이유 1. 버리기 아까워서
0:00 이유 2. 받은 뒤의 일은 안 보여서
0:00 이유 3. 주고 나면 기분이 좋아서
0:00 받는 쪽이 불편한 이유 (소비기한)
0:00 서운하지 않게 거절하는 말
0:00 내가 주는 쪽이라면 확인할 3가지

■ 출처
- van Herpen, de Hooge (2019). When product attitudes go to waste: Wasting products with remaining utility decreases consumers' product attitudes. Journal of Cleaner Production, 210, 410–418.
- Galak, Givi, Williams (2016). Why certain gifts are great to give but not to get: A framework for understanding errors in gift giving. Current Directions in Psychological Science, 25(6), 380–385.
- Gino, Flynn (2011). Give them what they want: The benefits of explicitness in gift exchange. Journal of Experimental Social Psychology, 47(5), 915–922.
- Aknin, Dunn, Proulx, Lok, Norton (2020). Does spending money on others promote happiness?: A registered replication report. Journal of Personality and Social Psychology, 119(2), e15–e26.
- 식품의약품안전처 소비기한 표시제 (2023년 도입 · 2024년 본격 시행 · 우유는 2031년부터).

■ 알려 드립니다
교육용 영상이며 심리 진단이나 상담을 대신하지 않습니다.
소개한 연구는 이 행동을 직접 잰 것이 아니라 비슷한 마음을 다룬 연구입니다. 사람마다 까닭은 다를 수 있습니다.

■ 도움받을 곳
24시간 정신건강 상담 전화 1577-0199

#인간관계 #심리학
```

## 3. 챕터 다시 계산하기 (문장 번호 기준 — 실제 내레이션 SRT)

```
python tools/srt_tool.py upload psychology/source/jakku-juneun-2026-11-25/jakku-juneun-2026-11-25.txt psychology/source/jakku-juneun-2026-11-25/jakku-juneun-2026-11-25.srt --chapters "1=필요 없다는데 자꾸 선물 주는 사람;7=이유 1. 버리기 아까워서;27=이유 2. 받은 뒤의 일은 안 보여서;40=이유 3. 주고 나면 기분이 좋아서;49=받는 쪽이 불편한 이유 (소비기한);59=서운하지 않게 거절하는 말;83=내가 주는 쪽이라면 확인할 3가지"
```

## 4. 태그

```
자꾸 주는 사람, 선물 주는 사람 심리, 인간관계, 심리학, 심리, 선물 심리, 필요 없는 선물, 거절하는 법, 거절, 서운하지 않게 거절, 부담스러운 선물, 이웃, 나눔, 정, 배려, 소비기한, 말투, 인간관계 심리, 관계 심리, 자존감, 마음, 마음공부, 감정조절, 정신건강, 심리상담
```

## 5. 고정 댓글

```
받는 쪽이었나요, 주는 쪽이었나요? 서운하지 않게 거절했던 말이 있다면 남겨 주세요.
교육용 영상이며 심리 진단·상담이 아닙니다.
```

## 7. 업로드 설정

| 항목 | 값 |
|---|---|
| 공개 상태 | 비공개로 올린 뒤 예약 공개 |
| 추천 공개 순서 | 6번째 — ADHD 다음 — 공개 시각은 PC 업로드 화면 기본(7일 뒤 17:00) 또는 사용자가 정함 · 비슷한 영상이 많아(overlap_giver_2026-11-26.md) 날수를 1~2일로 줄이는 것을 권함 |
| 썸네일 | `thumbnails/thumbnail_1.jpg` (본안 · 1280×720) |
| 자막 | `jakku-juneun-2026-11-25.srt` (실제 오디오에 맞춤) |
| 자막 올리기 | 예 |
| 카테고리 | 교육 |
| 동영상 언어 · 기본 언어 | 한국어 · ko |
| 오디오 언어 | ko |
| 시청자층 | 아동용 아님 |
| 유료 프로모션 | 없음 |
| 변경되거나 합성된 콘텐츠 | **예** (내레이션이 AI 음성 · 그림이 AI 생성) |

## 8. 점검 (설명란에 넣지 않음)

- 페르소나 관문 (`persona_loop.json`): title ✅ 6회차 · script_exit ❌ 18회차 · script_rebuttal ✅ 18회차 — 이탈·반론 단계는 상한(5회차, 일부 7회차)까지 돌린 뒤 사용자가 영상·썸네일·업로드로 진행 (2026-11-13). 통과로 적지 않음.
- 숫자·연구는 `근거.md` 1번 표 · 지금 대본에서 뺀 연구는 출처에 넣지 않음. · 페르소나 관문: 제목·썸네일 6회차 ✅ (2026-11-26 새 제목) · 대본 v3.4 — 반론 18회차 ✅ · 이탈 17회차 약한 줄 22·46 은 사용자 결정 A 그대로("A로 해 음성 다시 만들게") · 18회차(도입 6번째 문장만 바뀐 글) 약한 줄 15·22 — 결과는 persona_loop.json
- 잡음 검사 `audio_check.md`: 보고 수준 후보만 (고칠 것 없음).
- 영상: render check 0 · layout-check 0 · 완성 mp4 장면을 Claude 가 봄 · 음량 -14 LUFS 안팎 · 트루 피크 -1.5 dBTP 이하.
- 다른 사람의 영상 파일은 받지도 넣지도 않음 · 댓글은 뜻만 (작성자 정보 없음).

## 9. 결과 (업로드 후)

- (아직 없음)
