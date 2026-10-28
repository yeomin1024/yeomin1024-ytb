# 재테크 주제 탐색 — 20개씩 · 평가를 배움 · 명확한 결론만 (+ 요약본 안 평가)

버전: v1.0 — 2026-10-28 — 새로 (사용자 지시 2026-10-28 "주식 주제 관련 세션에서 했던것처럼 똑같은 방식으로 진행해서 유튜브 분석부터 요약본까지 만들어봐" — 주식 `stock/topics/README.md` v1.1 과 같은 꼴).
※ 정보 제공용 — 세무·법률·투자 상담이 아님.

## 순서 (분석 → 요약본)
1. 분석: `python3 tools/cloud_run.py economic …` (세 묶음 — `economic/analysis_rules.toml` v1.8) → `economic/result/outliers/analysis.md`.
2. 확인 엑셀: `python3 tools/target_check.py economic` · 콘텐츠 분석 엑셀 `python3 tools/content_analysis.py economic` (성공 사례 썸네일은 Claude 가 그림을 보고 `thumb_codes.tsv`) · 대본 받을 목록 `python3 tools/pc_transcribe.py list economic`.
3. 시청자 페르소나: `economic/result/outliers/personas.md` (분석이 끝날 때 저절로 — 설정 `economic/personas.toml`).
4. 댓글 니즈: `python3 tools/comment_title_ideas.py economic candidates` → Claude 가 `comment_title_picks.tsv` 에 고름 → `… match` → `comment_titles.md`.
5. 주제 탐색 (이 폴더): `python3 tools/topic_ideas.py economic material` → 후보 `pool/<날짜>.json` → `… add` → `주제탐색.md` · 평가판.
6. 요약본: 고른 주제마다 `economic/source/<영상ID>/요약본_안.json` → `python3 tools/summary_ideas.py economic status` → `요약본.txt` · 요약본 평가판.
7. 사용자가 좋음을 고르면 → 대본 (`economic/guides/quick_script.md` 3번부터).

## 파일

| 파일 | 누가 | 내용 |
|---|---|---|
| `주제탐색.md` | 도구 (손으로 고치지 않음) | 이번 20개 (점수 순 표 · 주제별 질문·결론·판정 규칙·자료·근거·겹침 확인·점수 내역) · 배운 것 · 대기·뺀 후보 |
| `평가판.html` → https://claude.ai/artifact/KftXe7GXWXgA8MJ7RJDXZJ | 도구가 만들고 Claude 가 올림 | 휴대폰에서 좋음·나쁨 누르기 (+ 까닭). 누른 것은 페이지 저장소 'marks' 에 |
| `평가.txt` | 사용자 · Claude | 평가 한 줄씩 `T003 좋음 까닭` · `T007 나쁨` (`T003 지움` = 취소). 같은 주제는 마지막 줄 |
| `pool/<날짜>.json` | Claude | 후보 모음 (주제 글) — 재료를 읽고 씀 |
| `material.md` | 도구 | 후보를 쓰기 전 재료 한 장: 페르소나 · 댓글 니즈 · 주제 묶음 성공 비율 · 성공 사례 제목 · 이미 쓴 주제 · 배운 것 |
| `topics.json` | 도구 | 모든 주제·상태(이번 묶음·대기·작성중·작성함)·점수 |
| `settings.toml` | Claude | 묶음 크기·점수 무게·겹침 기준·애매한 말·평가판 주소 · `[summary]` 요약본 편 목록·쓰지 않는 말 |
| `요약본_평가.txt` · `요약본_평가판.html` · `요약본_material.md` | 도구·사용자 | 요약본 안 평가 (아래 절) |

## 사용자가 하는 것
- 평가판에서 좋음·나쁨을 누름 (또는 Claude 에게 'T003 좋아, T007 별로' · 또는 GitHub 에서 `평가.txt` 에 줄을 더함). 까닭을 적으면 다음 후보를 쓸 때 참고.
- 주제를 골라 Claude 에게 "T003 으로 요약본 만들어" → 그 주제는 작성중.

## Claude 가 하는 것 (순서)
1. **평가 가져오기**: `ArtifactData list` (url = 평가판 주소, collection `marks`) → 결과를 스크래치 파일에 그대로 저장 → `python3 tools/topic_ideas.py economic import <파일>` → `평가.txt` 에 바뀐 것만 더함 → 점수·문서 다시. 채팅 평가는 `python3 tools/topic_ideas.py economic mark T003 좋음 "까닭"`.
2. **쓰기 시작**: 요약본에 `주제 ID: T003` 한 줄 (저절로 작성중) 또는 `… use T003 <영상ID>` · 다 쓰면 `… done T003`.
3. **갱신**: `… status` 가 '갱신 필요'(이번 20개가 모두 작성중·작성함·나쁨)면 → `… material` → `material.md` 를 읽고 **새 후보 25개 안팎**을 `pool/<날짜>.json` 에 → `… add pool/<날짜>.json` → 새 20개 → 평가판을 같은 주소로 다시 올림 (Artifact publish `url`).

## 후보 한 개 (pool JSON — 칸은 `material.md` 머리 표)
- **결론 = 예상 결론 한 문장, 숫자·판정으로** ('부부가 나눠 받으면 3년에 ○○만 원 덜 낸다', '연 2,000만 원을 넘으면 피부양자에서 빠진다'). 애매한 말(상황에 따라·~일 수도·신중·장단점…)이 있으면 도구가 뺀다.
- **판정 규칙** = 계산이 어느 쪽으로 나와도 결론이 하나로 정해지는 기준 ('A 의 3년 합계가 B 보다 적으면 A, 아니면 B'). 기준(보다·이상·까지·%…)이 없으면 뺀다.
- **자료** = 오늘 시행 중인 법령 원문(조문) + 2026년 기준 금액·요율 + 계산 가정 (연도 필수). 경제 뉴스·금리·환율 해설·개별 종목은 뺀다.
- 이미 쓴·쓰는 주제와 같으면 뺀다: 낱말 닮음 ≥ 0.40 또는 글자 겹침 ≥ 0.50 (`economic/source/used_content.md` 이미 만든 대본 · `economic/source/*/요약본.txt` 방향·항목·제목 · 앞서 낸 주제).

## 점수와 배우기 (주식과 같은 식)
- 처음 점수 = 댓글 니즈 👍 · 주제 묶음 성공 비율 · 페르소나 몫 · 공급 틈 · 성공 사례 제목 닮음 (무게는 `settings.toml [score]`).
- 배운 점수 = 갈래(페르소나·형식·주제 묶음·시장·자료·니즈)마다 log((좋음+1)/(나쁨+1)) 평균 + 가장 닮은 좋음 주제 − 가장 닮은 나쁨 주제.
- 평가가 5개를 넘으면 새 20개 중 3자리는 아직 평가 없는 갈래에서.

## 요약본 안 평가
- 편마다 `economic/source/<영상ID>/요약본.txt` = 핵심 방향 + 안 5개 (칸 LT 롱폼 제목 · LM 롱폼 썸네일 주요(하단 2줄, '/' 로 줄 나눔) · LS 롱폼 썸네일 보조(그림 속 꼬리표 낱말 — 2개 이하·각 5자 안) · LF 롱폼 대본 진행 · ST·SM·SS·SF 쇼츠 같음). 글은 `요약본_안.json`, 편 글자는 `settings.toml [summary] EPISODES`.
- 검사(도구): 쓰지 않는 말(어르신·노인·무조건) · 제목·썸네일 문구에서 피할 말(방법·하는 법·이유·때문·이것·이때) · 쇼츠 제목에서 빼는 말(노후·은퇴·퇴직·N가지·얼마·비교·차이·vs) · 제목 2줄(`title_fit`) · 60자.
- 평가: 요약본 줄 끝 `=> 좋음` · 요약본 평가판(주소는 아래 기록) · 채팅 → `요약본_평가.txt`.
- Claude: 평가판 `ArtifactData list marks` → 파일 → `python3 tools/summary_ideas.py economic import <파일>` · 채팅 `… economic mark A2-LT 좋음 "까닭"` · 다음 회차 = `요약본_material.md` 를 읽고 새 안 5개 JSON → `… economic add <영상ID> <round.json>` → 평가판 같은 주소로 다시 올림.

## 한계
- 주제 글은 Claude 가 쓴다 — 도구는 거르고·점수 매기고·뽑고·배운다. 결론은 계산 전 예상이며 (요약본의 ○○ = 계산 전), 판정 규칙으로 계산 뒤 하나로 정해진다.
- 법령·기준 금액은 대본 단계에서 오늘 시행 중인 원문으로 다시 확인한다 (`tools/law_text.py`) — 요약본의 기준 숫자는 이미 만든 편의 확인표에서 가져온 것만 쓰고 출처를 주석에.
- 겹침은 글자·낱말 닮음 — 같은 주제를 아주 다른 말로 쓰면 못 잡을 수 있어 '가장 닮은 쓴 주제'를 문서에 함께 보인다.
