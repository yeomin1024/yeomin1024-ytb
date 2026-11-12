# 재테크 — 평가판 세 장으로 주제 → 대본 → 쇼츠 → 영상 (새 세션은 이 파일 하나로)

VERSION: v1.3 — 2026-11-12 — 0번 맨 위 **페르소나 반복 검증 — 빠뜨리지 않음** + 표 2·6번 (`guides/persona_loop.md`) — 사용자 지시 "제목,썸네일, 대본 만들때 자꾸 페르소나 반복 검증 빼먹는데 빼먹지 말도록 주제별 지시사항 수정해봐".
(이전) VERSION: v1.2 — 2026-11-02 — **제목 = 따옴표 속 시청자 말 + 사실** (사용자 지시 "제목좀 더 자극적으로 해봐 댓글보면 나라가 일을 안한다 도둑놈이다…") — 2번 title 줄 · 3번 '놈' · `tools/anger_words.py`.
(v1.1 — 2026-11-02 — **쇼츠 판 = 쇼츠 제목·썸네일 문구·보조 칸 + 쇼츠 대본** (주식 v1.5 와 같이 — 전달 내용 칸 뺌, 주식 사용자 지시 "쇼츠 평가판에 전달내용 빼고 대본써서 하는걸로 하자") · `board_check.py` v1.5 · `script_feedback_board.py` v2.3.)
(v1.0 — 2026-11-02 — 최초, 사용자 지시 2026-11-02 "지시사항 수정됐으니 stock/guides/quick_board.md 대로 평가판 구성해" — 주식 `stock/guides/quick_board.md` v1.4 의 판 세 장·점검·db 읽기를 그대로 쓰고, 재테크에서 다른 것만 여기에 적음.)
※ 정보 제공용 — 세무·법률 상담이 아님.

**이 파일 + 맡은 편 폴더만 읽는다.** 공통 꼴(판에서 읽고 답하기·피드백 반영 반복·삭제)은 `stock/guides/quick_board.md` 1번이 기준. 대본 문장 규칙은 `economic/guides/quick_script.md`(v1.4 — 컨셉 말투) · 제목·썸네일·쇼츠는 `quick_package.md`(v1.2).

## 0. 한눈에

> **★ 페르소나 반복 검증 — 빠뜨리지 않음** (2026-11-12 사용자 지시 "제목,썸네일, 대본 만들때 자꾸 페르소나 반복 검증 빼먹는데 빼먹지 말도록 주제별 지시사항 수정해봐"): 제목·썸네일 문구·보조 문구·대본(롱폼·쇼츠)을 쓰거나 바꿀 때마다 `guides/persona_loop.md` 세 단계(`title` 피드 시험 · `script_exit` 이탈 · `script_rebuttal` 반론)를 **회차마다 새 하위 에이전트로 2회차 이상, 마지막 회차 = 지금 글**까지 — 기록은 `tools/persona_gate.py`, `tools/board_check.py` v1.11 이 기록을 읽어 없거나 오래되면 ❌ (판·시트·사용자에게 내놓지 않음). 규칙 점검(board_check)만으로는 페르소나 검증이 아니다.

| 단계 | 하는 것 | 명령·판 |
|---|---|---|
| 0 | 후보 = 주제 탐색 20개 (`economic/topics/주제탐색.md` — 꼬집을 제도가 있는 것만, `tools/topic_ideas.py economic`) | 기획안을 쓸 때 고름 (`topic_id`) |
| 1 | 주제 기획안 10개 (꼬집는 제도 + 롱폼 5칸 + 쇼츠 4칸 + 확인 방법·근거) | `economic/topics/board/topics_<날짜>.json` (꼴 = 2번) |
| 2 | 판에 올리기 전 점검 — 일반·반론 페르소나 (규칙 · 토큰 0) + **페르소나 반복 검증 `title`** (기획안마다 2회차 이상 — `guides/persona_loop.md`, 기록 `<topics>.persona.json`) | `python3 tools/board_check.py package economic <파일> --write` (+ `--stage shorts --write`) → ❌ 0 까지 고침 (v1.11 — 피드 시험 기록 없으면 ❌) |
| 3 | **1단계 주제 평가판** (롱폼 칸만) | `python3 tools/topic_board.py economic` → Artifact 다시 올림(같은 파일 `economic/topics/주제평가판.html`) — **https://claude.ai/artifact/EtFeGPhdVV9GXyTSzU8o1G** |
| 4 | 판정·피드백 읽기 | `ArtifactData list verdicts` · `query feedback where status == new` (주식 판과 db 가 따로) |
| 5 | 통과(pass)만 **롱폼 대본** — 법 원문 → 계산 → 대본 | `tools/law_text.py --source auto` · `economic/source/<영상ID>/calc/calc.py` · 대본 꼴 = 3번 |
| 6 | 롱폼 대본 점검 + **페르소나 반복 검증 `script_exit`·`script_rebuttal`** (대본을 고칠 때마다 — 기록 `<편 폴더>/persona_loop.json`) | `python3 tools/board_check.py script economic <대본.txt> --calc <json> --upload <upload.md>` → ❌ 0 (+ `tools/persona_review.py economic` · v1.11 — 검증 기록 없으면 ❌) |
| 7 | **2단계 대본 평가판** | `economic/topics/board/script_board.json` 'extra' 에 한 줄 `{key:'E01-long', ep:'E01', label:'E01 연금저축 1,500만 원 문턱', kind:'long', title, ver:'대본 v1', file}` → `python3 tools/script_feedback_board.py economic` → Artifact 다시 올림 — **https://claude.ai/artifact/6SbgVekYkvvh2vWXrDrFtk** |
| 8 | 롱폼 피드백 반영 반복 | 주식 판과 같음 (반영 → 계산 다시 → 6번 → 판 다시 → status=done·reply) |
| 9 | 대본 판 `verdicts/<key>.verdict == pass`('통과 (쇼츠로)') 인 편만 **쇼츠 대본** (프롤로그형 — 기획안 s_message 를 대본으로 늘림) | 쇼츠 대본 파일(한 줄 한 문장) · **쇼츠 판엔 전달 내용 칸이 없고 대본으로 평가** · 쇼츠 칸(제목·썸네일 문구·보조) 점검 `board_check.py package economic <파일> --stage shorts --write` · 대본 점검 `board_check.py script economic <쇼츠.txt> --kind short` (끝 멘트 「…아래 영상에서 확인하세요.」 를 마지막 두 줄에서 확인 — 없으면 ❌) → ❌ 0 |
| 10 | **3단계 쇼츠 평가판** | `economic/topics/board/shorts_board.json` 'items' 에 `{key:'E01-short', ep:'E01', label, from:'file', file, fields_from:'economic/topics/board/topics_2026-11-02.json#E01', long_key:'E01-long', ver:'v1'}` → `script_feedback_board.py economic` → 다시 올림 — **https://claude.ai/artifact/UJA5kHCvhHTx9VosVviSAN** |
| 11 | 쇼츠 피드백 반영 반복 → 쇼츠 판 통과 | 영상 = `quick_package.md` 4번·`guides/video_guide.md` (오디오 먼저 → 영상 → 썸네일) |

판 주소는 `economic/topics/board/urls.json` 에도 (대본·쇼츠 판의 '1단계 → 2단계 → 3단계' 연결 글이 여기서 채워짐). 판 셋 다 `capabilities {db, user}`, 같은 파일 경로로 다시 올림 (주소·피드백 그대로).

## 1. 옛 판과의 관계
- 주제 탐색 평가판(https://claude.ai/artifact/KftXe7GXWXgA8MJ7RJDXZJ — 20개 좋음·나쁨)과 요약본 평가판(https://claude.ai/artifact/7d9qx5BXr5JxywuWcwPUgM)은 **기획안 재료**로만 남김 — 결정은 이 파일의 주제 평가판에서. 거기 평가가 들어오면 `topic_ideas.py economic import` 로 배워 다음 기획안 고를 때 씀.
- 요약본 세 편(I·G·S)은 기획안 E03·E02·E01 로 옮김 (계산 `calc/calc.py` v0.1 그대로).

## 2. 기획안 꼴 (`topics_<날짜>.json` 의 `packages` 한 줄) — 주식 2번에서 다른 칸만
| 칸 | 쓰는 법 (재테크) |
|---|---|
| id · topic_id · persona · theme | `E01`… · 주제 탐색 `T0NN` · `P1`(은퇴 6070)·`P2`(3040 직장인)·`P3`(은퇴 앞둔 50대) — `economic/result/outliers/personas.json` |
| **complaint (꼬집는 제도)** | **필수** — 상대는 제도·조항·숫자·기한 ('1원만 넘어도'·'성실하게 낸 사람이 깎이는'·'아무도 안 알려 주는'). 사람·정당·세대·외국인 탓 ✗ (`economic/board_rules.toml` NO_TARGET) |
| message (전달 내용) | 시청자가 가져갈 결론 + **그래도 지금 할 일** 한 문장 |
| approach (전달 방식) | 사연형·비교형 · 인물(성씨)·나이·소득·재산 조건 · 조항 원문 꼬집기 → 계산 → 할 일 → 바뀌어야 할 점 |
| title · thumb_main · thumb_sub | **제목 = `"시청자 말" + 사실`** (v1.2 — 예 `"나라가 도둑이네" 연금저축 1원만 넘어도 16.5%`): 따옴표 속 = 그 제도에 댓글이 하는 말 (갈래·배수 `economic/result/outliers/anger_words.md` 1번 — D 성실히 낸 게 죄 ×3.27 · A 나라가 일을 안 한다 ×2.54 · B 떼어 간다·도둑 ×1.7~1.9 · E 폭탄 ×1.70) · 따옴표 밖 = 조건·숫자(대본이 증명) · 화면 2줄 (`title_fit`) · '하는 법·이유·때문·이것·이때'·'아무도 안 알려 준다'·'정부가'·'놈' ✗ · 갈래를 편마다 섞음 · 썸네일 주요 2줄도 같은 말투 · 보조 = 니즈 낱말·조건 꼬리표 · basis 에 쓴 갈래·배수, verify 에 '따옴표 밖 사실을 대본이 보여 주나(K8)' |
| s_title · s_thumb_main · s_thumb_sub | 1인칭 경험 + 당부 (「…손해봤어요. 꼭 보세요」) · '노후·은퇴·퇴직·N가지·얼마·비교·차이·vs' ✗ |
| s_message (쇼츠 대본 꼴 — 판엔 안 보임) | 쇼츠는 판에 **대본**으로 올림. 대본 꼴 = 프롤로그형: 첫 문장 핵심(누가·무엇 때문에·얼마) → 경위(각색) → 걸린 것 → '지금이라도 …?' → 끝 멘트 **「…, 아래 영상에서 확인하세요.」** (끝 멘트는 대본 점검 `--kind short` 이 확인) |
| verify | 사실 확인 길 — 법 조문·시행일·올해 기준 금액 + 다른 가정(나이·소득·가구)이면 뒤집히나 — 없으면 ❌ |
| basis · calc | 재테크 분석 근거(댓글 니즈 K···, 성공 사례, 반론 K··) · 숫자를 계산했으면 calc 경로 (법에 적힌 숫자는 ⚠ 로 남고 대본 단계에서 원문 확인) |

## 3. 점검 규칙 (`tools/board_check.py` v1.5 + `economic/board_rules.toml`)
- 일반 페르소나 `economic/result/outliers/personas.json` · 반론 페르소나 `economic/result/outliers/rebuttal_persona.md` (K5 숫자·법 오류 27% · K1 조건마다 25% · K4 빠진 비용 16% · K3 가정 골랐다 14% · K8 낚시·과장 10% — 좋아요 몫, 2026-11-02 댓글 26개).
- 재테크에서 더한 ❌: 꼬집는 제도 빈칸 · 컨셉 밖(금리·환율·증시 전망·종목·코인·부동산 투자) · 사람·정당 탓 · 비속어('놈' 포함 — board_rules v1.1) · 제목·쇼츠 제목에서 피할 말.
- ⚠ 는 Claude 가 그 줄만 읽고 판단 — 어려운 말(IRP·피부양자·종합과세…)은 대본에서 '쉽게 말해' 한 문장, 법 숫자(30%·500만 원·16.5%)는 대본 단계 원문 확인.

## 4. 롱폼 대본 꼴 (재테크 — `quick_script.md` 5-1 사연형 + 컨셉)
```
-도입        (사례 인물·조건) → 제도 때문에 본 손해 금액 → '이게 말이 됩니까?'(조항 한 문장) → 반전 예고
-챕터 N      조항 원문(조문·시행일) → 계산 한 걸음 → 끝 문장 = 다음 궁금증
-할 일       그래도 지금 할 일 (신청·기한·서류를 구체적으로 — 반론 K6)
-정리        세 가지 한 문장씩 → 바뀌어야 할 점 한 문장(조항을 향해) → 시청해주셔서 감사합니다.
```
- 숫자는 calc 출력만 · 조건(나이·소득·재산·가구)을 도입에서 못 박음(K1) · 건보료·세금·피부양자·기초연금 중 결론을 바꿀 것을 말함(K4) · 진행자 H17 하나·3인칭.

## 5. 끝낼 때
- `guides/status.md` 맨 위 버전 줄·'재테크 분석' 줄 · `CHANGELOG.md` · 편 폴더 README → 커밋·푸시 (main).
