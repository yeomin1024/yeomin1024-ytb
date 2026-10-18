# 재테크 영상 B 단계 — 제목·썸네일·업로드·쇼츠 (요약 지시사항)

버전: v1.0.1 — 2026-10-18 — 쇼츠 고정 댓글 절 (사용자 질문 "댓글에도 링크를 첨부해야 될 것 같은데 어떻게 써야하는지 멘트, 링크 알려줘").
(v1.0 — 2026-10-18 — 새로 만듦. 새 세션이 긴 지시사항과 다른 영상 폴더를 읽지 않고 B 단계를 끝내게 한 요약.

이 파일은 아래 원본 지시사항의 요약이다. 원본이 바뀌면 이 파일도 고친다 (원본이 우선).
원본: `guides/title_guide.md` v3.4 · `thumbnail_guide.md` v3.14 · `upload_guide.md` v1.11 · `shorts_guide.md` v1.15 4번 · `economic/guides/shorts_insights.md` v1.0.1 · `data_insights.md` v1.1 2·5번 · `pipeline.md` v1.27 3단계 · `CLAUDE.md` 제목·썸네일·쇼츠·재테크 업로드 줄 · 본보기 `gungmin-sigi-2026-10`·`geumyung-soduk-2026-10` v1.0.1
**읽는 것:** A 결과 폴더의 `README.md`(1·4번)·`<ID>.txt`·`cd economic/source/<ID>/calc && python3 calc.py` 출력만 (앞 단계 `quick_script.md`).

## 0. 공통
- 숫자·사실은 대본·README·calc 출력에 있는 것만. 제목·썸네일·설명란 첫 줄이 같은 약속, 영상에 없는 약속 없음.
- 대본 피드백 19~21 을 여기에도: 애매한 말 금지(짧은 곳은 '그냥 두면' → '모르면') · 금액 뒤 뜻 낱말('월 30만 원 손해') · 왜·어떻게를 빼지 않음.
- **동사로 끝 + 조사**('1년 500만 원 날림' ✗ → '1년에 500만 원 날린다'). **조사로 뜻을 분명히** — 금액 앞 낱말이 목적어로 읽히지 않게: '세금 200만 원 날린다' ✗ → '세금으로 200만 원 날린다', 헷갈리지 않으면 더하지 않음('세금 96만 원 더 낸다' ✓). 줄마다 '무엇을 날리나? 무엇으로?'.
- 사람 이름(박씨 등)·'어르신·노인'·이모지·과장('무조건')·개별 종목 없음.

## 1. 제목 3개 `titles.md`
- **호기심 구절 + 해소 구절**(쉼표·'ㅣ'), 결론을 담는다. 숫자는 대본이 증명·설명하는 것만(안전한 쪽 반올림). 사용자 예시도 데이터로 고쳐 쓴다.
- 맨 앞 12자 = 핵심·검색 낱말('연금'·'노후'·'은퇴' — 나이만 맨 앞은 약함). 시청자층 낱말(노후·은퇴·50·60대)은 주제 낱말과 붙여('50·60대 노후 연금').
- 쓸 것: '모르면'·손해 낱말·'월 N만 원'·'은퇴·부부·50~70대'·'순서·단계'·드러낸 호기심. 피할 것: '방법·하는 법'·금지형·'이유·때문'·'투자'·'세금' 단독(→ '건보료'·'손해')·'절세·퇴직금·생활비'·가린 말('이것·이 OO·이때'). 물음표는 없어도 됨. 목돈만 쓰지 않고 **월 금액 + 목돈**. 요청과 데이터가 다르면 둘 다 보여 주고 이유.
- 60자 이하, 실제 한도는 **화면 폭 — 모든 화면 ✅ 여야 채택**: `python3 tools/title_fit.py "제목1" "제목2" "제목3"` (쇼츠 `--shorts`, 전체 `python3 tools/title_fit.py economic`). 남기는 순서 ① 핵심 낱말 맨 앞 ② 시청자층 ③ 숫자의 조건·뜻 낱말 ④ 숫자의 주인('부부'). 빼는 것: 꾸밈말('집 한 채'·'61세 직장인')·되풀이·'ㅣ' 뒤 구절·월 금액/목돈 중 하나(썸네일 문구와 같은 쪽을 남김). **폭이 먼저** — 빠진 시청자층은 썸네일 1줄 맨 앞에. 나중에 줄인 안은 R4(채택)로 + 뺀 것·이유.
- R1 추천 · R2 데이터가 가장 단단한(짧은) 안 · R3 다른 갈래(비추천이면 이유) — 맨 앞 말·금액 표현이 서로 다르게. 근거 숫자는 `python3 tools/content_research.py titles economic` 또는 `data_insights.md` 2번만 (비교 / 좁힌 주제 / 같은 채널, 15개 미만 '표본 적음', 한 쪽만 좋으면 '약함').
```
# <ID> 제목 3개 (title_guide v3.4, 분석 결과 <generated>)
- 대본 · 결론 · 제목 숫자와 대본에서의 뜻 (calc, 문장 번호)
| # | 제목 | 글자 | 호기심 구절 / 해소 구절 | 근거 (비교 / 좁힌 주제 / 같은 채널) |
- 화면 폭(가장 좁은 칸 줄 나눔·잘려서 안 쓴 안) · 피할 낱말 · 한계 · 짝 썸네일(세 장 모두 R1 짝)
## 채택 표시 (`make_summary.py`·`youtube_upload.py` 가 읽음 — 사용자가 고르기 전에는 R1)
- [x] **T1 = R1 (추천 — 업로드 시트 1번)** <제목> `NN자` — 짝 썸네일: thumbnail_1
- [ ] **T2 = R2** <제목> `NN자`
- [ ] **T3 = R3** <제목> `NN자`
## 결과 (업로드 후)
```

## 2. 롱폼 썸네일 프롬프트 3장 `thumbnails/`
Claude 는 프롬프트 파일까지 (그림은 ChatGPT). 옛 틀(시안 3축·검은 배경 thumbnail_3·펀치 문구·채널 색표) 금지, 근거는 재테크 결과로만.
- **근거(README 3번):** 3-1 `data_insights.md` 5번 · 3-2 같은 주제 승인 영상 썸네일(`economic/result/outliers/W_<ID>/thumbnail.jpg`)을 눈으로 표시한 `thumbnails/analysis/codes.csv`(인물·걱정 표정·글자 위치·줄 수·금액·빨강·경고 낱말·물건·로고) + 같은 채널 짝 `analysis_thumbs_pairs_*.jpg` · 3-3 니즈 낱말. 30개 미만·차이 10%p 안팎은 방향만('한계').
- **문구 = 하단 2줄, 세 장 같게**(그림만 시험): 채택 제목에서 덧붙인 숫자·그림이 보여 주는 말을 빼고 나머지는 제목 글자 그대로. **시청자층 낱말은 빼지 않고**(없으면 더함) 흰색 맨 앞, 그 뒤 중요한 것 노랑. 두 줄을 따로 읽어도 뜻이 같게.
- **색:** 노랑 #FFD400 = 중요한 것 · 빨강 #FF2A2A = 나쁜 상황 · 나머지 흰색. 외곽선 흰·노랑 = 두꺼운 검정, 빨강 = 두꺼운 흰. 손해 줄을 조금 크게.
- **자리:** 아래 약 35% 어두운 띠 위 왼쪽 정렬, 한 줄 약 14자 너비(띄어쓰기 포함 20자 이내), 2줄째는 가로 80% 앞에서 끝(오른쪽 18%·아래 15% = 영상 길이 표시). 사람·글자는 가운데 16:9 안·위아래 8% 비움, 320px 에서도 읽힘.
- **그림 = 문구의 장면.** 손해 문구면 **손해를 알고 좌절한 얼굴**(미간·고개를 떨굼·처진 어깨·입을 가림, 240px 에서도, 얼굴을 손에 다 가리지 않게) — 원인 행동(포기·손사래)·놀람·고민 얼굴만으로 그리지 않음. 인물 = AI 가상 인물·시청자 대표·되도록 젊게. **니즈 낱말**(예: 건보료·조기수령)은 물건이 아니라 **낱말 그대로** 꼬리표·판 앞면 **평면 글자**(입체 금지), 2개 이하·각 4자 안팎, 가리지 않게, 손해와 붙여 크게. 영상의 방법은 물건으로 그리지 않음. 금지: 실제 로고·서식·화폐 도안(그리면 'plain generic banknotes with no portraits, no numbers')·이모지·글자 있는 종이.
- **본안 1** = 성공과 차이가 큰 특징을 모두(좌절 실사 인물 + 빨강 손해 낱말 + 니즈 낱말 꼬리표) · **실험안 2** = 성공 자료에 적거나 없는 것, 본안과 **한 가지만** 다르게(한 사람↔부부·사람 없음·은유 장면). 쇼츠 썸네일과 곳·옷·몸짓을 다르게.
- `thumbnail_N.md` (도구가 `| 시험하는 가설 |`·`## 문구`·`## [A]`·`## [B]` 를 읽음 — [A]·[B] 는 언어 표시 없는 코드 블록): `# <ID> 썸네일 N — <본안(클릭률 최대)|실험안 ①·②>: <그림>` → 버전 → `| 항목 | 값 |`(역할·시험하는 가설·짝 제목·문구·근거·숫자 근거·인물 나이·저장 경로 `economic/source/<ID>/thumbnails/thumbnail_N.png`) → `## 화면 구성` → `## 문구 (그대로 사용)` `| 자리 | 문구 | 색 |` → `## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)` → `## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집 프로그램으로)` → `## 검수` → `## 이미지 검수 (Claude — 지시사항 10번)` → `## 결과 (업로드 후)` `| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |`.
- [A] 에 그대로 넣는 문장 (장면·하단 2줄은 위 규칙대로 영어로, 표정은 'crushed … frustration, regret and despair … readable at small size, realistic, not cartoonish' · [B] 는 같은 장면 + 'Absolutely no text, letters, numbers, logos or watermarks.'):
```
YouTube thumbnail, 16:9 landscape (1280x720), photorealistic, high contrast, bold and readable at small size.
Fictional person, not resembling any real or famous person.
… printed in huge flat heavy bold white letters on its flat front face (flat print, not carved or 3D letter shapes).
The second line MUST end at or before 80% of the image width (x ≤ 1024 px of 1280): the right 18% of the width in the bottom 15% of the height must contain no text (video length badge). If the lines do not fit, make both lines a little smaller.
If 16:9 is not available, use the widest landscape canvas; in any case keep all text and faces inside the central 16:9 area, at least 8% away from the top and bottom edges.
Render ONLY the Korean text given in quotes, exactly as written with the same letters, numbers and spacing, in a heavy bold sans-serif Korean font. No other text, letters, numbers, watermarks or logos anywhere.
```
- `thumbnails/README.md` 절: 1 이번 시안 3개 · 2 문구를 어떻게 줄였나(조사 점검·Noto Sans KR 900 으로 잰 px) · 3 근거 — 분석 결과 (재테크 결과로만) · 4 색 · 5 인물 · 6 ChatGPT로 이미지 만들기 · 7 한계 · 8 파일.

## 3. 업로드 시트 `upload.md`
- 절 번호·낱말 그대로 (도구가 '제목'·'설명란'·'챕터'·'태그' 절의 첫 코드 블록과 설정 표를 읽음): 머리(버전 · 기준 파일·올릴 영상 `economic/out/<ID>/final_1080p.mp4` · `> 업로드:` dry-run → `--publish-at`, 짝 쇼츠와 같은 시각, 먼저 부자백서 업로드 목록을 읽어 두 번 올리지 않음) → `## 1. 제목` → `## 2. 설명란 (그대로 복사)` → `## 3. 챕터 다시 계산하기 (문장 번호 기준)` → `## 4. 태그` → `## 5. 고정 댓글` → `## 6. 업로드 설정` → `## 7. 점검` → `## 8. 결과 (업로드 후)`.
- 설명란 (5,000자 이하, 순서 고정): 첫 2줄(약 100자 — 숫자 비교 + 영상이 알려 주는 것, 제목 반복 없이 핵심 검색어) → `■ 이 영상에서 다루는 것`(원칙 1~3 · 할 일 A → B → C · 이미 ~한 분이 할 일) → `■ 챕터` → `■ 예시에 대해`("영상 속 <부부>(…)는 계산용 가상 사례입니다." + 넣지 않은 것 + "숫자는 <연>년 <월>월 기준이며, …" + "이 영상의 내레이션은 AI 음성으로 만들었습니다.") → `■ 근거`("<날짜> 시행 중인 법령 원문으로 확인: <법령(조문)>") → `■ 알려 드립니다`("이 영상은 정보 제공을 위한 것이며 <…> 상담·권유가 아닙니다." + 기준은 바뀔 수 있으니 <기관(전화번호)>에서 확인) → 해시태그 3개(핵심 행동·주제·해결).
- 챕터는 손으로 계산하지 않음 (숫자 = 챕터 첫 **대본 문장 번호**, 첫 항목 `1=`): `python tools/srt_tool.py upload economic/source/<ID>/<ID>.txt economic/source/<ID>/<ID>.srt --chapters "1=<라벨>;13=…"` → "✅ YouTube 챕터 규칙 통과"(0:00·3개 이상·각 10초 이상·시간 순). 제목 = 파트 라벨('원칙 하나, X' → '원칙 1 X').
- 태그 10~15개·합계 500자 이하(핵심 검색어 → 넓은 주제어 → 사례), 낚시 태그 없음. 고정 댓글 3~6줄·링크 없음: 소개 → 핵심 행동 1~2(1. 2.) → 경험 질문 하나 → "정보 제공용이며 <…> 상담이 아닙니다."
- 설정 표 `| 항목 | 값 |`: 공개 상태 = 비공개 + 예약 공개(짝 쇼츠와 같은 시각) · 썸네일 `thumbnails/thumbnail_1.*`(**그림이 오기 전에는 올리지 않음**, 2·3은 공개 뒤 '테스트 및 비교') · 자막 `<ID>.srt` 그대로 · 카테고리 교육 · 동영상 언어 한국어 · 아동용 아님 · 유료 프로모션 없음 · **변경되거나 합성된 콘텐츠 예**(AI 음성) · 최종 화면(선택).
- 점검: 숫자 출처 · 제목 100자 이하 · `< >` 없음 · 해시태그 3 · 챕터 ✅ · checklist C표 · `python3 tools/youtube_upload.py economic <ID> --dry-run` (렌더 전이면 '영상 파일 없음'만 문제).

## 4. 쇼츠 `shorts/` (영상ID `<ID>-shorts`)
- **프롤로그형** — 롱폼 하나에 하나, 롱폼의 가상 사례(돈 문제 하나)로. 롱폼의 핵심 정보(이유·방법·기준 금액·할 일)는 대본·화면에 없음 — 숨기는 것은 '왜'와 '고치는 법'뿐, 이야기는 쇼츠 안에서 끝남. ① **핵심 한 문장**(첫 문장 하나가 누가·언제·무엇 때문에·얼마 — "김씨 부부는 은퇴 첫해에만 세금과 건보료로 200만 원 넘게 손해 본 걸 알게 됐습니다.") ② 배경 1~2문장 ③ 알게 된 경위 — 짧게, **각색 가능**(이름·장면, 숫자·결과는 롱폼 그대로, 실제 사이트·사람·기관 없음) ④ 걸린 것(이대로 가면 얼마) ⑤ 질문 — 무엇을 하는지 넣어 "지금이라도 건보료를 줄일 수 있을까요?" ⑥ 끝 문장만 롱폼 안내 "…, 지금 할 일까지 아래 영상에서 확인하세요."
- 진행자 하나·3인칭 · 대본 피드백(조사·기준 이름+금액·숫자 근거·19~21) · 문장 50자 이하 · 끝인사 없음 · 정부·외국인·제도 탓 없음 · **50~55초 ≈ 285~315음절**(보통 11문장) · 숫자는 롱폼 README 4번 표에 있는 것만(조건까지, 내려 잡아서).
- TXT 첫 줄은 파트 라벨(`-같은 X, 다른 Y`). **첫 문장은 42px 2줄 자막 하나**여야(안 되면 줄임):
  ```
  python3 tools/srt_tool.py build economic/source/<ID>/shorts/<ID>-shorts.txt economic/source/<ID>/shorts/<ID>-shorts.srt
  python3 tools/srt_tool.py check economic/source/<ID>/shorts/<ID>-shorts.txt economic/source/<ID>/shorts/<ID>-shorts.srt
  ```
- **제목 2안(R1 추천·R2) — 사용자가 고른다.** 꼴 [핵심 낱말][한 일·믿은 것][누구][기간]에 [금액][손해 동사] (「기초연금 안 된다고 포기한 부부 1년에 500만 원 날린다」). 이름 없음 · 핵심 낱말 맨 앞 · '이유' 안 씀 · 'N가지'·'노후·은퇴·퇴직금·50~70대'·'얼마·비교·차이·vs' 없음 · 과장 동사 금지(먼저 받는 돈이 있으면 '덜 받는다') · `title_fit.py --shorts` ✅(넘치면 쉼표·꾸밈말부터). 고른 안은 채택 줄로(옛 채택은 남김) `upload.md` 1번에. **제목이 바뀌면 썸네일 문구·그림도 다시.**
- 해시태그 2개 — 롱폼 주제 낱말로(#재테크·#노후준비·#연금저축·답을 내비치는 태그 빼고). 근거 숫자는 `shorts_insights.md` 2~4번만.
- `shorts.md` 절: 머리(보내는 곳 = 롱폼 제목 · **넣지 않는 것** · **각색** · 길이·첫 문장 자막 ✅ · 목소리 H04) → `## 1. 제목 (2안 — 사용자가 고름)` → `## 2. 대본` `| # | 시각 | 대본 | 역할 | 화면 (색 = 뜻: 빨강 손해 · 청록 아낌 · 노랑 중요) |`(1번 화면 = 썸네일 그림, 롱폼과 같은 사람·색) → `## 3. 영상 만드는 법 (오디오가 생긴 뒤)`(첫 문장 동안 그림을 확대 없이 `K.cover(…, { zoom: 1 })`, 자막은 아래 검정 칸 · 세로 1080×1920 · 장면 목록 — 핵심 정보는 그리지 않음, 장면 파일은 4단계) → `## 4. 설명란 (그대로 복사)` → `## 5. 올리기 설정` → `## 6. 숫자·사실 근거 (롱폼 대본·README 에 있는 것만) · 각색한 것` → `## 7. 주의 — 근거와 반대 방향`(올린 뒤 관련 동영상 클릭·본 비율·'본편 공개' 불만 댓글 → shorts_insights 8번) → `## 8. 다음에 할 일`.
- 쇼츠 설명란 (결론 없음): 상황·결과 1~2문장 / `▶ <무엇이 달랐는지>는 아래 '관련 동영상'에서 — <롱폼 제목>` / 빈 줄 / "<인물> 이야기는 계산용 가상 사례를 각색한 것이며, 숫자는 <연>년 <월>월 기준입니다. 이 영상의 내레이션은 AI 음성으로 만들었습니다." / "정보 제공을 위한 것이며 <…> 상담이나 권유가 아닙니다." / 해시태그 2.
- `shorts/upload.md` 에 `## 5. 고정 댓글`(v1.0.1): 쇼츠 댓글·설명란 링크는 눌리지 않으므로(2023-08-31~) 주소 대신 '화면 아래 ▶ <본편 제목 앞부분> 링크를 누르면 본편으로' + 못 찾을 때 '부자백서 채널 → 동영상에서 「본편 제목」' + 가상 사례 각색 고지, 결말 없음 — 공개 뒤 사용자가 달고 고정.
- `shorts/upload.md` — 절 번호 1·2·4·5·6 그대로(챕터 없음): 머리(올릴 영상 `economic/out/<ID>-shorts/final_1080p.mp4` · `python tools/youtube_upload.py economic <ID>-shorts --dry-run` → `--publish-at`, 짝 롱폼과 같은 시각) → `## 1. 제목` → `## 2. 설명란` → `## 4. 태그`(2~3개) → `## 6. 업로드 설정`(공개 범위 · 기본 언어 ko · 자막 올리기 예 · 변경되거나 합성된 콘텐츠 **예** · 썸네일 · 관련 동영상 = 롱폼: API 로 못 검, 롱폼 공개 뒤 사용자가 스튜디오 → 콘텐츠 → Shorts → 연필 → '관련 동영상'). 공개 뒤 `https://i.ytimg.com/vi/<영상ID>/oardefault.jpg` 로 썸네일 확인, 아니면 사용자가 앱 → 쇼츠 수정 → 썸네일 → 0초 장면.
- **세로 썸네일 1장** `shorts/thumbnails/thumbnail_1.md` (롱폼과 같은 절, 표에 ``| 배치 | `COVER_LAYOUT: band` … |`` (`cover_check.py`·`make_summary.py` 가 이 낱말로 세 칸 규칙을 씀)·`| 시험하는 가설 | 없음 — 쇼츠는 1장 |`·저장 경로): **세 칸** — 위 0~36% 순검정 + 문구 2줄 · 가운데 36~72% 사진(가로 끝까지) · 아래 72~100% 순검정 빈 칸(첫 문장 자막 자리). 글자·얼굴·꼬리표는 **높이 15~85%** 안, 오른쪽 16%(높이 45% 아래 버튼)에 얼굴·꼬리표 없음. 문구 = 쇼츠 제목을 줄인 2줄, **줄마다 가운데·같은 크기·최대 크기**(굵은 글꼴로 재어 px), 그림에서 가장 큰 것, 2줄째 손해 빨강. 그림 = 첫 문장 상황(각색)·좌절 얼굴·결말 없음·롱폼 썸네일과 곳·옷·몸짓·색을 다르게. [A] 에 그대로 넣는 문장 (+ 롱폼의 'Fictional person …'·'Render ONLY …' 줄):
```
Vertical YouTube Shorts thumbnail, 9:16 portrait (1080x1920), high contrast. This is a vertical image: ignore any general instruction about a 16:9 landscape canvas.
LAYOUT — three full-width zones: 0–36% of the height flat solid pure black (#000000) with only the headline; 36–72% one photorealistic photograph edge to edge with straight top and bottom edges; 72–100% flat solid pure black, empty. No gradient, fade or border.
SAFE AREA: some feeds crop to about 4:5 — all text, faces and word tags stay between 15% and 85% of the height.
Headline: exactly TWO lines of very large heavy bold Korean text, same size, EACH LINE CENTERED on the same axis, the longer line from about 4% to 96% of the width, the block between about 19% and 32% of the height and at least 3% above the photo; flat letters, no glow, no 3D.
If 9:16 is not available, use a 2:3 portrait canvas (1024x1536) with the same zones and keep the headline between 12% and 88% of the width.
```

## 5. 모으기·올리기·ChatGPT 안내
```
python3 tools/make_summary.py economic <ID>                  # summary.md (자동 생성 — 직접 고치지 않음)
python3 tools/make_summary.py --chatgpt economic <ID>        # thumbnails/chatgpt.md (쇼츠: <ID>-shorts)
python3 tools/make_summary.py --chatgpt-all economic         # economic/thumbnails_chatgpt.md — 남은 썸네일 전부
git pull --rebase --autostash origin main
git add economic/source/<ID>/ economic/thumbnails_chatgpt.md && git commit -m "재테크 <N>편 제목·썸네일·업로드·쇼츠 (<ID>)" && git push origin main
git rev-parse HEAD                                           # 고정 주소에 넣을 커밋
```
- `thumbnails_chatgpt.md` 를 끝까지 읽어 이 영상 4장이 다 있고 옛 말('dark navy'·'비운다')이 없는지 본다.
- 사용자에게 알릴 메시지 — **새 ChatGPT 대화**에서, **커밋을 고정한 주소**로(main 주소는 몇 분 늦게 바뀜):
```
이 파일을 열어 끝까지 읽고, 파일에 적힌 썸네일을 1번부터 차례로 모두 만들어서 장마다 적힌 저장 경로에 올려 줘.
https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/<커밋>/economic/thumbnails_chatgpt.md
```
  멈추면 `계속`. 이 계정 ChatGPT 는 저장소에 못 쓴다 → 'Claude 대화창에 붙여 넣어 주세요'로 끝나면 사용자가 **번호 순서대로** Claude 대화에 붙인다 (직접 올리는 길 `https://github.com/yeomin1024/yeomin1024-ytb/upload/main/economic/source/<ID>/thumbnails` · 저장소가 비공개면 파일을 대화창에 끌어다 놓게).
- **그림이 오면 (Claude 검수):** 원본 크기로 문구·그림 낱말을 잘라 확대해 한 글자씩 → '이미지 검수' 표(크기 16:9≈1.77·쇼츠 9:16 · 한글 · 색 · 자리 · 인물(가상·좌절·로고·화폐 없음) · 320px). 쇼츠는 `python3 tools/cover_check.py economic/source/<ID>/shorts/thumbnails/thumbnail_1.png` ✅, 문구가 15% 선 위면 다시 그리지 않고 `python3 tools/cover_shift.py <원본> <새 그림>`(원본은 `thumbnails/original/`). 통과한 것만 `thumbnail_N.<확장자>` 로 main(통과 전에는 영상·업로드에 안 씀). 실패 → 옛 그림 `rejected/`, 원인을 프롬프트에 넣어 버전을 올리고 chatgpt 파일을 다시 → 새 커밋 주소로 같은 메시지. 한글만 틀리면 같은 대화에 `thumbnail_N의 글자를 파일의 문구표와 똑같이 고쳐 줘. 그림은 그대로.` — 두세 번 틀리면 [B] + 캔바.
- 공개 뒤 '테스트 및 비교'(3장) 결과는 `thumbnail_N.md`·`titles.md` 결과 칸에, 48시간·7일 뒤 클릭률·평균 시청 지속·크게 떨어지는 구간은 `upload.md` 8번에. 영상 3개 이상 쌓이면 이긴 시안 특징을 `data_insights.md` '썸네일'에.

## 6. 끝내기 전 점검
- [ ] 제목 3개 `title_fit` ✅ · 결론·시청자층(또는 썸네일 1줄)·뜻 낱말 · 피할 낱말 없음 · 채택 표시 줄
- [ ] 썸네일 3장: 같은 문구(제목 줄임·조사) · 노랑/빨강 · 2줄째 80% 앞 · 좌절 얼굴 · 니즈 낱말 평면 글자 · 실험안은 한 가지만 · [A] 문장
- [ ] upload.md 절 번호·낱말 · 챕터 ✅ · 태그 10~15 · 해시태그 3 · 합성 콘텐츠 예 · dry-run
- [ ] 쇼츠: 첫 문장 하나에 핵심 · 핵심 정보 없음 · 각색 표 · 285~315음절 · check ✅ · 제목 2안 `--shorts` ✅ · 해시태그 2 · band 표·세 칸 수치
- [ ] `make_summary`·`--chatgpt-all economic` → main 푸시 → 커밋 고정 주소 메시지를 사용자에게
