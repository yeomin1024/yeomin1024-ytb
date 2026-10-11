# jeungyeo-2026-10 썸네일 3 — 대비 (그때 들은 말 ↔ 3년 뒤 월세방)

버전: v1.0 — 2026-10-11 — 최초 작성 (`guides/thumbnail_guide.md` v1.2, `story/guides/thumbnail_rules.md` v1.1), 대본 v1.0 기준

| 항목 | 값 |
|---|---|
| 시험하는 가설 | "그때 들은 말"과 "3년 뒤 결과"를 한 화면에 나란히 두면, 문제 분석 두 번째 메시지(말은 법이 지켜 주지 않는다)가 한눈에 전해져 클릭을 부른다 |
| 짝 제목 | `titles.md` T3 (짧은 변형) "집을 넘기고 3년, 아들의 전화가 끊겼습니다. …" — T1·T2와도 어울림 |
| 숫자 근거 | 문장 3 "집을 자기 앞으로 해 주면 들어와서 모시겠다고 했어요" (0:11) · 문장 11 "제게 남은 건 월세방 하나" (0:56) · 문장 13 "집을 넘긴 지 3년 만에" (1:05) |

## 화면 구성
- 화면을 세로로 반씩 나눈다.
- 왼쪽 (따뜻한 크림 톤, 낮): 거실 탁자 위에서 나이 든 여성의 손이 젊은 남성의 손에 집 열쇠를 건네는 장면 (손만, 얼굴 없음). 위에 흰 말풍선 + 검정 글자 **"들어와서 모실게요"**
- 가운데: 세로 경계선
- 오른쪽 (어두운 네이비 톤, 밤): 좁은 원룸에 70대 여성이 혼자 등을 보이고 앉아 있는 뒷모습. 위에 노랑 상자 + 검정 글자 **"3년 뒤"**, 그 아래 파랑 상자 + 흰 글자 **"월세방"** (가장 큰 글자)
- 오른쪽 아래 구석 비움

## 문구 (그대로 사용)
| 줄 | 문구 | 색 | 강조 |
|---|---|---|---|
| 왼쪽 말풍선 | 들어와서 모실게요 | 검정 #1E1E1E (흰 말풍선) | — |
| 오른쪽 1 | 3년 뒤 | 검정 #1E1E1E | 노랑 상자 #FFD400 (유일한 강조) |
| 오른쪽 2 | 월세방 | 흰색 (파랑 #2D6CDF 상자) | 가장 큰 글자 |

- 말풍선은 대본 문장 3의 아들 말("들어와서 모시겠다고 했어요")을 직접 말투로 옮긴 것이다 (새 말을 지어내지 않음). 전체 15자.
- "3년 뒤"는 증여(2022년 3월)에서 송금·전화가 끊긴 때(2025년 6월)까지 — 월세방으로 옮긴 때는 2024년 2월이고 2025년 6월에도 월세방에 산다 (README 검산 표). 

## [A] 완성형 프롬프트 (이미지 AI에 그대로 붙여 넣기)
```
YouTube thumbnail, 16:9 (1280x720), bold high-contrast composition readable at small size.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF, gain red #E63B2E.
Bottom-right corner kept empty (video length badge).
Realistic photo style, split screen with a clean vertical divider in the middle.
LEFT HALF (warm cream tones, daytime): close-up of hands only over a wooden living-room table — an elderly woman's hand
placing a single house key into a younger man's open hand; no faces visible. Above the hands, a white speech bubble with
black bold text "들어와서 모실게요".
RIGHT HALF (cool dark navy tones, night): inside a small bare one-room studio, a fictional Korean woman in her early 70s
seen from behind, sitting alone on a thin floor mattress facing a small dark window; only her back and gray-streaked
hair are visible. Above her, a solid bright yellow (#FFD400) box with black bold text "3년 뒤", and below it a wide
solid blue (#2D6CDF) rounded box with thin white border containing huge white bold text "월세방", the largest text.
Fictional people, not resembling any real or famous person. No documents, no logos, no money.
Render ONLY the Korean text given in quotes, exactly as written, in a heavy bold sans-serif Korean font, large and highly legible at small sizes. No other text, letters, numbers, watermarks or logos anywhere.
```

## [B] 글자 없는 프롬프트 (한글이 틀릴 때 — 글자는 편집에서 "문구" 표대로 얹기)
```
YouTube thumbnail background, 16:9 (1280x720), bold high-contrast composition.
Palette: cream #F2EBDD, dark navy #14213D, ink black #1E1E1E, highlight yellow #FFD400, loss blue #2D6CDF.
Realistic photo style, split screen with a clean vertical divider. Left half (warm cream, daytime): hands only over a
wooden table, an elderly woman's hand placing a house key into a younger man's open hand, no faces; an empty white
speech bubble above. Right half (dark navy, night): a small bare one-room studio, a fictional Korean woman in her early
70s seen from behind sitting alone on a thin floor mattress facing a small dark window; an empty bright yellow box and
an empty solid blue (#2D6CDF) rounded box with thin white border above her. Fictional people, not resembling any real
or famous person. Bottom-right corner empty.
Absolutely no text, letters, numbers, logos or watermarks. Leave clean empty space where the headline will be added later.
```

## 검수
- [ ] "들어와서 모실게요" · "3년 뒤" · "월세방"이 한 글자도 틀리지 않음
- [ ] 아들은 손만, 사연자는 뒷모습만 (얼굴로 특정인을 비난하는 연출 없음)
- [ ] 실제 등기 서류·계약서 서식·도장·법원 상징 없음
- [ ] 노랑 강조 1곳("3년 뒤") · 320px 축소본에서 좌우 대비와 "월세방"이 읽힘
- [ ] 오른쪽 아래 비어 있음 · 1280×720, 2MB 이하

## 결과 (업로드 후)
| 날짜 | 테스트 및 비교 결과 (시청 시간 비율) | 메모 |
|---|---|---|
