# 역사 주제 탐색 — 20개씩 · 평가를 배움 · 명확한 결론만 (+ 요약본 안 평가)

버전: v1.0 — 2026-10-28 — 새로 (사용자 지시 2026-10-28 "주식 주제 관련 세션에서 했던것처럼 똑같은 방식으로 진행해서 유튜브 분석부터 요약본까지 만들어봐" — 주식 `stock/topics/README.md`·재테크 `economic/topics/README.md` 와 같은 꼴).
※ 연구·교육용. 역사 사실은 사료·연구 원문으로 확인한 뒤 대본에 쓴다 — 여기 결론은 확인 전 예상.

## 순서 (분석 → 요약본)
1. 분석: `python3 tools/cloud_run.py history …` (세 묶음 — `history/analysis_rules.toml` v1.7) → `history/result/outliers/analysis.md`.
2. 확인 엑셀: `python3 tools/target_check.py history` · 콘텐츠 분석 엑셀 `python3 tools/content_analysis.py history` (성공 사례 썸네일은 Claude 가 그림을 보고 `thumb_codes.tsv` — 2026-10-28 무게 순 위 144장) · 대본 받을 목록 `python3 tools/pc_transcribe.py list history`.
3. 시청자 페르소나: `history/result/outliers/personas.md` (분석이 끝날 때 저절로 — 설정 `history/personas.toml`).
4. 댓글 니즈: `python3 tools/comment_title_ideas.py history candidates` → Claude 가 `comment_title_picks.tsv` 에 고름 → `… match` → `comment_titles.md`.
5. 채널 설명: `history/guides/channel.md` (⚠️ 임시 — 사용자가 채널 설명을 주기 전).
6. 주제 탐색 (이 폴더): `python3 tools/topic_ideas.py history material` → 후보 `pool/<날짜>.json` → `… add` → `주제탐색.md` · 평가판.
7. 요약본: 고른 주제마다 `history/source/<영상ID>/요약본_안.json` → `python3 tools/summary_ideas.py history status` → `요약본.txt` · 요약본 평가판.
8. 사용자가 좋음을 고르면 → 사실 확인(사료 원문) → 대본. 역사 제작 지시사항은 아직 없음 (`history/README.md` — 분석만 하던 주제).

## 파일

| 파일 | 누가 | 내용 |
|---|---|---|
| `주제탐색.md` | 도구 (손으로 고치지 않음) | 이번 20개 (점수 순 표 · 주제별 질문·결론·판정 규칙·자료·근거·겹침 확인·점수 내역) · 배운 것 · 대기·뺀 후보 |
| `평가판.html` → 주소는 `settings.toml [page] URL` | 도구가 만들고 Claude 가 올림 | 휴대폰에서 좋음·나쁨 누르기 (+ 까닭). 누른 것은 페이지 저장소 'marks' 에 |
| `평가.txt` | 사용자 · Claude | 평가 한 줄씩 `T003 좋음 까닭` · `T007 나쁨` (`T003 지움` = 취소). 같은 주제는 마지막 줄 (첫 평가 때 생김) |
| `pool/<날짜>.json` | Claude | 후보 모음 (주제 글) — 재료를 읽고 씀 |
| `material.md` | 도구 | 후보를 쓰기 전 재료 한 장: 채널 설명 · 페르소나 · 댓글 니즈 · 주제 묶음 성공 비율 · 성공 사례 제목 · 이미 쓴 주제 · 배운 것 |
| `topics.json` | 도구 | 모든 주제·상태(이번 묶음·대기·작성중·작성함)·점수 |
| `settings.toml` | Claude | 묶음 크기·점수 무게·겹침 기준·애매한 말·연도 꼴(`[clarity] YEAR` — 세기·기원전도 연도로 봄)·평가판 주소 · `[summary]` 요약본 편 목록·쓰지 않는 말 |
| `요약본_평가.txt` · `요약본_평가판.html` · `요약본_material.md` | 도구·사용자 | 요약본 안 평가 (아래 절) |

## 사용자가 하는 것
- 평가판에서 좋음·나쁨을 누름 (또는 Claude 에게 'T003 좋아, T007 별로' · 또는 GitHub 에서 `평가.txt` 에 줄을 더함). 까닭을 적으면 다음 후보를 쓸 때 참고.
- 주제를 골라 Claude 에게 "T003 으로 요약본 만들어" → 그 주제는 작성중.

## Claude 가 하는 것 (순서)
1. **평가 가져오기**: `ArtifactData list` (url = 평가판 주소, collection `marks`) → 결과를 스크래치 파일에 그대로 저장 → `python3 tools/topic_ideas.py history import <파일>` → `평가.txt` 에 바뀐 것만 더함 → 점수·문서 다시. 채팅 평가는 `python3 tools/topic_ideas.py history mark T003 좋음 "까닭"`.
2. **쓰기 시작**: 요약본에 `주제 ID: T003` 한 줄 (저절로 작성중) 또는 `… use T003 <영상ID>` · 다 쓰면 `… done T003`.
3. **갱신**: `… status` 가 '갱신 필요'(이번 20개가 모두 작성중·작성함·나쁨)면 → `… material` → `material.md` 를 읽고 **새 후보 25개 안팎**을 `pool/<날짜>.json` 에 → `… add pool/<날짜>.json` → 새 20개 → 평가판을 같은 주소로 다시 올림 (Artifact publish `url`).

## 후보 한 개 (pool JSON — 칸은 `material.md` 머리 표)
- **결론 = 예상 결론 한 문장, 숫자·판정으로** ('조선 사람 한 끼 밥은 오늘 한 공기의 약 3배였다', '사극의 주막 방은 기록과 다르다'). 애매한 말(설이 있다·알려지지 않았다·논란이 있다·상황에 따라·~일 수도…)이 있으면 도구가 뺀다.
- **판정 규칙** = 기록이 어느 쪽으로 나와도 결론이 하나로 정해지는 기준 ('기록 3개가 모두 2배 이상이면 사실, 1개라도 2배 미만이면 절반만 사실'). 기준(보다·이상·까지·%·번·개·명…)이 없으면 뺀다.
- **자료** = 기록 원문(실록·일기·여행기·법전) 이름 + 시기(연도·세기·기원전 — 없으면 뺌) + 계산 가정. 지금 정치·전쟁과 엮기·반일·국뽕 선동·재야사학·영토 주장·지어낸 야담·타임슬립은 뺀다 (`history/guides/channel.md` 1번).
- 이미 쓴·쓰는 주제와 같으면 뺀다: 낱말 닮음 ≥ 0.40 또는 글자 겹침 ≥ 0.50 (`history/source/*/요약본.txt` 방향·항목·제목 · 앞서 낸 주제).

## 점수와 배우기 (주식과 같은 식)
- 처음 점수 = 댓글 니즈 👍 · 주제 묶음 성공 비율 · 페르소나 몫 · 공급 틈 · 성공 사례 제목 닮음 (무게는 `settings.toml [score]`).
- 배운 점수 = 갈래(페르소나·형식·주제 묶음·시장(한국사·세계사)·자료·니즈)마다 log((좋음+1)/(나쁨+1)) 평균 + 가장 닮은 좋음 주제 − 가장 닮은 나쁨 주제.
- 평가가 5개를 넘으면 새 20개 중 3자리는 아직 평가 없는 갈래에서.

## 요약본 안 평가
- 편마다 `history/source/<영상ID>/요약본.txt` = 핵심 방향 + 안 5개 (칸 LT 롱폼 제목 · LM 롱폼 썸네일 주요(하단 2줄, '/' 로 줄 나눔) · LS 롱폼 썸네일 보조(그림 속 꼬리표 낱말 — 2개 이하·각 6자 안) · LF 롱폼 대본 진행 · ST·SM·SS·SF 쇼츠 같음). 글은 `요약본_안.json`, 편 글자는 `settings.toml [summary] EPISODES`.
- 검사(도구): 쓰지 않는 말(`[summary] BANNED` — 국뽕·매국·타임슬립 등) · 제목·썸네일 문구에서 피할 말(`TITLE_BANNED` — 세계사·진실·숨겨진) · 제목 2줄(`title_fit`) · 60자.
- 평가: 요약본 줄 끝 `=> 좋음` · 요약본 평가판(주소는 `history/README.md` 기록) · 채팅 → `요약본_평가.txt`.
- Claude: 평가판 `ArtifactData list marks` → 파일 → `python3 tools/summary_ideas.py history import <파일>` · 채팅 `… history mark A2-LT 좋음 "까닭"` · 다음 회차 = `요약본_material.md` 를 읽고 새 안 5개 JSON → `… history add <영상ID> <round.json>` → 평가판 같은 주소로 다시 올림.

## 한계
- 주제 글은 Claude 가 쓴다 — 도구는 거르고·점수 매기고·뽑고·배운다. 결론은 기록 확인 전 예상이며 (요약본의 ○○ = 확인 전), 판정 규칙으로 확인 뒤 하나로 정해진다.
- 조선 사료 사이트(실록·국사편찬위원회·민족문화대백과)가 이 클라우드 환경에서 막혀 있어 사실 확인은 사용자가 Network access 를 열거나 PC 에서 — 요약본 단계에서는 사료 이름과 확인할 것만 적는다.
- 역사는 대본이 0개 (자막 막힘·음성인식 보류) → 성공 사례의 대본 진행 근거가 없음. 요약본의 대본 진행은 채널 설명의 꼴(생활사 해설형·확인형·지도형)로만.
- 겹침은 글자·낱말 닮음 — 같은 주제를 아주 다른 말로 쓰면 못 잡을 수 있어 '가장 닮은 쓴 주제'를 문서에 함께 보인다.
