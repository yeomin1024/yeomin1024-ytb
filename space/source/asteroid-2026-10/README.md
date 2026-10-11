# 소행성 2024 YR4 영상 대본 소스 (asteroid-2026-10)

버전: v1.0 — 2026-10-11 — 최초 작성 (사용자 지시: 주식 밖 주제 오디오 전까지 주제마다 3개)

> 과학 정보 제공용 원고입니다. 사연은 실제 발표와 보도를 바탕으로 재구성한 이야기이며, 사연 속 인물과 금액은 예시입니다. 확률·거리는 발표 시점 기준입니다.

## 파일

| 파일 | 내용 |
|---|---|
| `asteroid-2026-10.txt` | 대본 v1.0 — **문장 131**. 파트 라벨(`-사연 파트` 1–19 / `-진행자 파트` 20–31 / `-문제 분석 파트` 32–82 / `-올바른 방법 파트` 83–125 / `-마무리` 126–131), `[장면] 과학 정보 제공용 재구성 사연입니다` (문장 31 뒤) |
| `asteroid-2026-10.srt` | **문장 131 / 자막 158** (1432px 넘는 27문장은 앞줄·뒷줄), 문장 31 뒤 고지 공백 8.0초, **끝 12:28** (추정치, 읽는 음절 3,561) |
| `titles.md` | 제목 3개 (T1 채택) |
| `thumbnails/thumbnail_1.md` ~ `_3.md` | 썸네일 이미지 AI 프롬프트 3개 (숫자 반전 / 인물·감정 / 쇼츠 대 실제 대비) |
| `upload.md` | 업로드 시트 (설명란·챕터 13개·태그 15개·고정 댓글) |
| `tts_lexicon.tsv` | 읽는 소리 사전: `2024 YR4` → "이천이십사 와이알포" (TTS에만 쓰고 대본·자막은 그대로, `guides/tts_guide.md`) |
| `summary.md` | 요약 문서 (자동 생성, `tools/make_summary.py`) |

검사: `python3 tools/srt_tool.py check space/source/asteroid-2026-10/asteroid-2026-10.txt space/source/asteroid-2026-10/asteroid-2026-10.srt --expect 131/158`
→ `문장 131 / 자막 158 (나뉜 문장 27개) / SRT–TXT 일치 ✅ / 고지 공백 문장 31 뒤 8.0초 ✅ / 끝 00:12:28,058` · `✅ 이상 없음`
녹음 후: `video/`에서 `npm run align-audio -- space asteroid-2026-10` (오디오는 고치지 않음, 문장 31 뒤 3.5초 이상 쉼)

- 50자 넘는 문장 없음. 제목이 약속한 장면(0.004%)은 문장 11, **0:52** (1분 안).
- 목표 분량 12~14분(`space/guides/script_rules.md` 7-1) 안이다. 문장을 늘이지 않고 문제 분석 5개·올바른 방법 5개로 채웠다.

## 주제를 고른 이유 (분석 숫자, `space/guides/data_insights.md`)
- 카테고리 '5. 뉴스·위험' 기회점수 **71 (1위)**. ⚠️ 단, 이 점수는 누리호 키워드 2개로만 계산됐고 소행성 키워드는 수집되지 않았다. `소행성 충돌 확률`·`소행성 충돌 2032`는 2026-10-09 YouTube 자동완성에서 수요를 확인한 검색어다 (`space/analyzer_config.toml`). 세 영상 중 데이터 근거가 가장 약하다 → 제작 순서 3번째.
- 호기심 단어(진짜·이유·결국) 제목이 롱폼에서 **3.32배**(성공 72.0% vs 48.8%, n=25) → T3·진행자 넘어가는 문장("엿새 만에 뒤집힌 진짜 이유")에 사용.
- 공포/경고 단어 제목 **0.59배** → 공포를 파는 대신 바로잡는 영상. 숫자 포함 제목 0.51배 → 제목 숫자는 반전 한 쌍(3.1% → 0.004%)만.
- 롱폼 12~20분 성공 **35.3%**(n=17, 작은 채널 10개 중 5개) → 12분 28초.
- 이야기가 2024년 12월 발견 → 2025년 2월 3.1% → 엿새 뒤 0.004% → 달 4.3% → 2026년 3월 '가능성 없음'으로 끝나, 모든 숫자를 공식 발표·보도로 검산할 수 있다 (최신 자료 규칙).

## 사연 검산 (재구성 — 실제 발표 숫자에 맞춤)

| 항목 | 사연 값 | 실제 값·계산 | 대본 |
|---|---|---|---|
| 처음 본 날 | 2025년 2월 19일 아침 (한국) | 나사 3.1% 발표 = 미국 시간 2025-02-18(화). 한국은 미국 동부보다 14시간 빠르므로 국내에는 19일에 퍼졌다. YTN(연합뉴스) 2025-02-20: "18일에는 충돌 확률이 3.1%" | 문장 1, 35 |
| 결제 시점 | 그날(19일) 밤 | 다음 발표 1.5%는 미국 시간 2월 19일 = 한국 20일. 그래서 "하루만 기다렸어도 절반" | 문장 5, 97·98 |
| 3.1% | 32분의 1 | 1 ÷ 32 = 3.125% → 나사 표기 3.1% | 문장 1, 35 |
| 0.004% | 2만 5천분의 1 | 1 ÷ 25,000 = 0.004%. 나사 2025-02-24 발표 | 문장 11, 38 |
| 엿새 | 엿새 뒤 | 미국 시간 18일 → 24일 = 6일 (한국 시간으로도 19일 → 25일 = 6일) | 문장 11, 38, 99 |
| 발견 53일 만 | 두 달도 안 됨 | 2024-12-27 → 2025-02-18: 12월 4일 + 1월 31일 + 2월 18일 = 53일 | 문장 15, 36, 84 |
| 하루 뒤 절반 | 3.1% → 1.5% | 1.5 ÷ 3.1 = 48% | 문장 98 |
| 사연자·딸 나이 | 2025년 마흔하나, 딸 아홉 살 → 2032년 열여섯 | 9 + (2032 − 2025) = 16 (설정) | 문장 3·4 |
| 150만 원 | 생존 배낭 두 개 + 한 달 치 비상식량 + 캠핑용 대용량 배터리 | 배낭 풀세트 1개 약 15만 7천~17만 2천 원 × 2 = 약 31만~34만 원 (국내 쇼핑몰 검색 결과) / 1000Wh급 캠핑용 대용량 배터리 약 92만 원대 (국내 쇼핑몰 검색 결과) / 한 달 치 380인분 비상식량 189.99달러 (2024년 미국 보도) × 1,400~1,450원으로 가정 ≈ 27만 원 → 합계 약 150만~153만 원. 주제 상한 1천만 원 이하 | 문장 5·6, 18, 97 |
| 45% | 140m 이상 발견 비율 | 11,343 ÷ (11,343 + 약 14,000) = 44.8% (나사 2025-12-03 집계로 계산) | 문장 122 |
| 큰 소행성 대부분 | 1km 이상 | 873 ÷ (873 + 약 50) = 94.6% (계산) | 문장 107·108·109 |
| 30분 넘게 / 25배 | 다트 | 11시간 55분 → 11시간 23분 = 32분(±2분). 73초 × 25 = 30.4분 < 32분 | 문장 119·120 |

- **기획서의 230만 원은 확인하지 못해 150만 원으로 바꿨다.** 비상식량 국내 가격을 검색으로 확인하지 못했고, 확인된 가격(배낭·배터리)과 미국 보도 가격으로 맞춘 합계가 약 150만 원이다. 금액은 제목에 없다.
- 기획서의 "반품 기한이 지난 발전기"는 쓰지 않았다. 2월 19일 결제 → 25일 0.004%는 엿새 차이라 '기한이 지났다'고 단정할 근거가 없다. 대신 "상자는 이미 다 뜯어서 딸과 함께 배낭까지 싸 둔 뒤였죠"(문장 12)로 썼다.
- 사연 속 쇼츠는 가상이다 (실제 채널·영상 제목 없음). 사연자는 실존 인물·천문학자를 흉내 내지 않는다.

## 숫자와 출처

확인 방법: 이 환경은 원문 페이지(science.nasa.gov, blogs.nasa.gov 등)를 직접 열 수 없어(DNS 차단), **2026-10-11 웹 검색 결과(원문 인용·요약)로 확인**했다. 링크는 검색 결과에 나온 주소다.

| 문장 | 대본 표현 | 값 | 출처 (원문 인용) | 자료 연도 |
|---|---|---|---|---|
| 33·34 | 2024년 12월 27일, 칠레의 소행성 감시 망원경이 발견 | ATLAS(나사 지원), 칠레 리오우르타도 | 나사 제트추진연구소 근지구천체연구센터(CNEOS) news210: "2024 YR4 was discovered on December 27, 2024, by the NASA-funded Asteroid Terrestrial-impact Last Alert System (ATLAS) telescope in Rio Hurtado, Chile." | 2024~2025 |
| 1, 25·26, 35 | 3.1%, 당시 기록, 지름 수십 미터가 넘는 소행성 가운데 최고 | 나사 3.1%(32분의 1), 2025-02-18 | Yahoo News(WTTW 2025-02-19): NASA's website listed "a 3.1% chance (about 1 in 32)" … Boston.com 2025-02-25: 3.1%는 "higher than any NASA had previously recorded for an object of this size or larger". YTN 2025-02-20: "역대 이 정도 이상 크기의 소행성 가운데 가장 높은 충돌 확률". 유럽우주국: "For asteroids larger than 30 metres in size, 2024 YR4 now holds the record for the highest impact probability" | 2025 |
| 37 | 하루 뒤 1.5% | 나사, 미국 시간 2025-02-19 | YTN(연합뉴스) 2025-02-20: "미 항공우주국(NASA)은 19일(현지시간) … 2032년 지구 충돌 확률이 1.5%로 낮아졌다고 밝혔다" | 2025 |
| 37, 59 | 이틀 뒤 0.28%, 1% 아래로 내려가자 1등급 | 360분의 1, 2025-02-20 | The Weather Network (나사 행성방위 블로그 인용): "refine YR4's odds of impact to 1 in 360, or 0.28%" · "Once the odds fell below 1%, the asteroid moved to Level 1 on the Torino scale" | 2025 |
| 11, 38, 39 | 엿새 뒤 2월 24일 0.004%, 앞으로 100년 동안 의미 있는 충돌 위험 없음 | 나사 2025-02-24 | 나사 행성방위 블로그 2025-02-24 "Latest Calculations Conclude Asteroid 2024 YR4 Now Poses No Significant Threat to Earth in 2032 and Beyond" (검색 요약: Earth impact 0.004%, "no significant potential for impact over the next century"), Boston.com 2025-02-25 "NASA analysis drops asteroid 2024 YR4's impact probability to 0.004%" | 2025 |
| 61 | 곧 0등급 | 토리노 0 | Space.com: "reassigned to Torino Scale Level Zero, the level for 'No Hazard'" (2025-02-23 관측 반영) | 2025 |
| 43~48 | 범위가 좁아지면 확률이 오르고, 지구를 벗어나면 빠르게 0 | 유럽우주국 설명 | 유럽우주국(ESA): "as we narrow down where exactly 2024 YR4 will be located on 22 December 2032, Earth fills up a larger fraction of our shrinking uncertainty region" · "this rising impact probability is an expected result" · "If we reach a point at which Earth is no longer inside this region, the impact probability will quickly drop to 0" | 2025 |
| 52~57, 60, 91·92, 106 | 토리노 척도 0~10, 3등급 설명, 1등급 설명, 2~4등급 = 천문학자 주의 | 나사 CNEOS 토리노 척도 표 | 3등급: "A close encounter, meriting attention by astronomers. Current calculations give a 1% or greater chance of collision capable of localized destruction. Most likely, new telescopic observations will lead to re-assignment to Level 0. Attention by public and by public officials is merited if the encounter is less than a decade away." · 1등급: "the chance of collision is extremely unlikely with no cause for public attention or public concern" · MIT 뉴스(2005 개정): 2~4등급을 "meriting attention by astronomers"로 설명 | 척도 현행 문구(2005년 개정판) — 2025년 적용 |
| 53, 90 | 3.1%일 때 3등급 | CNEOS news210 "Asteroid 2024 YR4 reaches level 3 on the Torino Scale" | 같은 페이지 | 2025 |
| 17, 63, 65 | 달 충돌 1.7% → 2025년 4월 3.8% → 6월 4.3% | 나사 2025-02-24 / 2025-04-02 / 2025-06-03 | 나사 2024 YR4 페이지(검색 요약): "raised the chance of a lunar impact on Dec. 22, 2032, from 1.7% as of late February to 3.8%" · The Weather Network: 4.3% "as of June 3, 2025" | 2025 |
| 17, 66~72 | 2026년 2월 제임스 웹 관측, 3월 5일 달 충돌 가능성 없음, 달 표면에서 약 2만 1,200km, 궤도가 바뀐 게 아니라 정밀해진 것 | 나사 2026-03-05 | 나사 행성방위 블로그 2026-03-05 "New NASA Asteroid Observations Eliminate Chance of 2032 Lunar Impact" (검색 요약): Webb 관측 2026-02-18·26, "pass the lunar surface at a distance of 13,200 miles (21,200 km)", "improved precision in our understanding of where the asteroid is expected to be in 2032 rather than a shift in its orbital path" · KSL·Sky at Night 같은 내용 | 2026 |
| 67 | 지상 망원경으로는 너무 어두워 보이지 않게 된 뒤 | 2025년 4월 이후 | 같은 검색 결과: "by April 2025, asteroid 2024 YR4 had moved so far from Earth that it became too faint for ground-based telescopes to see" | 2025 |
| 75~78, 105 | 밝기만으로 40~90m → 제임스 웹 2025년 3월 관측, 53~67m(약 60m), 10층 건물 정도 | 나사 2025-04-02 | CNEOS: "most likely in the range of 40 to 90 meters (130 to 300 feet)", 밝기 기반 · 나사(검색 요약): Webb 적외선 자료로 "174-220 feet (53-67 meters), about the size of a 10-story building" · 위키백과 60±7m | 2025 |
| 79 | 해외 언론 별명 '도시 파괴급' | city killer | Live Science·The Weather Network 기사 제목 "'city-killer' asteroid 2024 YR4" | 2025 |
| 107·108 | 1km 이상 873개 발견, 약 50개 남음 (2025년 12월 기준) | 나사 행성방위조정국 그래픽 2025-12-03 | 검색 요약: "39,123 discovered near-Earth asteroids … 873 discovered above 1 kilometer, with an estimated 50 still to be found, and 11,343 discovered above 140 meters, with an estimated 14,000 remaining" | 2025 |
| 122 | 140m 이상 45% 정도 | 위 집계로 계산 (44.8%) | 같은 자료 / 행성협회: "we've found just 43% of our goal" (시점 다름 — 대본은 나사 2025-12 숫자로 계산) | 2025 |
| 114~116 | 2025년 6월 베라 루빈 천문대 첫 영상, 약 10시간 관측으로 새 소행성 2,104개, 근지구 7개 위험 없음 | 2025-06-23 | CNN 2025-06-23, Fox 13: "2,104 previously unknown asteroids, with seven classed as near-Earth objects", 약 10시간 관측, "none of the new near-Earth asteroids pose a risk to Earth" | 2025 |
| 117~120 | 2022년 다트 실험, 공전 주기 30분 넘게 짧아짐, 최소 목표 73초의 25배 넘게 | 2022-09-26 충돌, 2022-10-11 발표 | 존스홉킨스 응용물리연구소(APL) 2022-10-11: 11시간 55분 → 11시간 23분, "32 minutes … plus or minus 2 minutes" · "minimum benchmark … 73 seconds … by more than 25 times". 이후 논문(Naidu 외)은 33분 15초 → 대본은 "30분 넘게" | 2022 |
| 123·124 | 니오 서베이어 2027년 9월 이후 발사, 5년 동안 140m 이상의 3분의 2 이상 | 나사 JPL | JPL: launch "no earlier than September 2027" · "find at least two-thirds of the near-Earth objects larger than 140 meters" (5년 기본 탐사). 행성협회: 늦으면 2028년 6월 | 2025~2026 |

### 출처 링크
- 나사 소행성 2024 YR4: https://science.nasa.gov/solar-system/asteroids/2024-yr4/
- 나사 CNEOS 2024 YR4 토리노 3등급: https://cneos.jpl.nasa.gov/news/news210.html
- 나사 CNEOS 토리노 척도: https://cneos.jpl.nasa.gov/sentry/torino_scale.html
- 3.1% (WTTW 2025-02-19): https://news.wttw.com/2025/02/19/will-asteroid-hit-earth-2032-space-rock-has-highest-impact-probability-ever-recorded-s
- 1.5% (YTN 2025-02-20): https://www.ytn.co.kr/_ln/0134_202502201704227690 · 파이낸셜뉴스 2025-02-20: https://www.fnnews.com/news/202502200941001866
- 0.28%·1등급 (The Weather Network): https://www.theweathernetwork.com/en/news/science/space/impact-odds-of-city-killer-asteroid-2024-yr4-suddenly-drop
- 0.004%·달 1.7% (나사 2025-02-24): https://science.nasa.gov/blogs/planetary-defense/2025/02/24/latest-calculations-conclude-asteroid-2024-yr4-now-poses-no-significant-threat-to-earth-in-2032-and-beyond · Boston.com 2025-02-25: https://www.boston.com/news/world-news/2025/02/25/nasa-gives-all-clear-asteroid-threaten-earth/
- 0등급 (Space.com): https://space.com/the-universe/asteroids/earth-safe-from-city-killer-asteroid-2024-yr4-thats-impact-probability-zero-folks
- 유럽우주국 설명: https://blogs.esa.int/rocketscience/?p=5746 · https://www.esa.int/Space_Safety/Planetary_Defence/Asteroid_2024_YR4_no_longer_poses_significant_impact_risk
- 달 3.8%·4.3% (The Weather Network): https://www.theweathernetwork.com/en/news/science/space/puck-shaped-asteroid-2024-yr4-chances-of-hitting-the-moon-increase
- 달 충돌 가능성 없음 (나사 2026-03-05): https://science.nasa.gov/blogs/planetary-defense/2026/03/05/new-nasa-asteroid-observations-eliminate-chance-of-2032-lunar-impact/ · KSL: https://www.ksl.com/article/51459942/new-data-shows-asteroid-2024-yr4-will-narrowly-miss-the-moon · Sky at Night: https://www.skyatnightmagazine.com/news/asteroid-2024-yr-wont-hit-our-moon
- 토리노 척도 2005 개정 (MIT 뉴스): https://news.mit.edu/2005/torino
- 근지구 소행성 발견 현황 (나사): https://science.nasa.gov/science-research/planetary-science/planetary-defense/near-Earth-asteroids/
- 루빈 천문대 (CNN 2025-06-23): https://cnn.com/2025/06/23/science/vera-rubin-observatory-first-images · Fox 13: https://www.fox13news.com/news/vera-rubin-observatory-discovers-2000-unknown-asteroids-within-10-hours
- 다트 (APL 2022-10-11): https://www.jhuapl.edu/news/news-releases/221011-dart-mission-impact-changed-asteroids-motion-in-space
- 니오 서베이어 (JPL): https://www.jpl.nasa.gov/missions/near-earth-object-surveyor · 행성협회: https://www.planetary.org/space-missions/neosm
- 사연 금액 검산용 가격 (검색 결과, 상품 추천 아님): 국내 쇼핑몰 생존 배낭 풀세트·1000Wh 캠핑용 배터리 상품 페이지(쿠팡), 미국 코스트코 비상식량 보도(ABC 2024-07): https://abc7.com/post/costco-offering-apocalypse-ready-emergency-food-kits-150/15063150/

### 기관마다 다른 숫자 (대본은 나사 숫자로 통일, `script_rules.md` 4-4)
| 항목 | 나사 | 유럽우주국 |
|---|---|---|
| 최고 지구 충돌 확률 (2025-02-18) | 3.1% | 2.8% |
| 다음 날 | 1.5% | 1.4% |
| 2월 말 | 0.004% (2025-02-24), 이후 0.0017% | 0.001% |

### 쓰지 않은 것 (확인 못 했거나 규칙에 걸림)
- **첼랴빈스크 운석(2013):** 부상자 약 1,500명(유리창 파편)은 검색으로 확인했지만 크기 "약 20m"는 확인하지 못했다. 2010년대 사건이고 공포를 키울 수 있어 뺐다.
- **아포피스 2.7%(2004)**와 **토리노 척도 2005년 개정 이야기:** 2000년대 자료라 대본에 쓰지 않았다 (최신 자료 규칙: 2020년대 → 없으면 2010년대까지). 2~4등급 설명 문구의 근거로만 README에 남긴다.
- 기획서 230만 원, "반품 기한이 지난 발전기" (위 검산 참고)
- "아들" → **딸**로 바꿨다: 같은 주제 누리호 영상(`nuriho-2026-10`)의 사연이 '아들의 꿈'이라 사연 소재가 겹치지 않게.
- 다트 33분 15초(후속 논문)·"정확히 32분": 숫자가 둘이라 "30분 넘게"로만 썼다.

## 경력 시청자(우주 덕후) 예상 반론과 대본의 답 (`script_rules.md` 6번)
| 반론 | 대본 위치 |
|---|---|
| 3.1%면 낮은 확률 아냐? 왜 겁먹어? | 문장 28~30: 맞다고 인정 → '역대 최고'라는 말이 붙으면 그 말이 먼저 들어온다 → 세 번째 문제(문장 51~61)에서 등급으로 보면 '관심' 단계였음 |
| 결국 나사도 틀린 거네 | 문장 70~72: 나사 "길이 바뀐 게 아니라 위치를 더 정밀하게 알게 된 것" |
| 토리노 3등급이면 대중도 주의하라는 거 아냐? | 문장 57·58: 접근이 10년 안이면 '관심'을 가질 만하다는 문구까지 그대로 전하고, 관심과 짐을 싸는 행동을 나눔 |

## 다른 두 영상과 겹치지 않게 한 점
- 근거: 누리호·보이저 줄, 인공위성 추락 경보(2023)·우주 쓰레기(2024)는 쓰지 않았다. 이 영상의 근거는 `script_rules.md` 9번 "배정: asteroid-2026-10" 줄만 썼다.
- 방법: "공식 원문 찾기·영상 날짜 확인"(보이저), "몇 번 중 몇 번"(누리호)은 쓰지 않고 **발견 며칠째·등급·다음 발표까지 기다리기·지름·지켜보는 사람들**에 집중했다.
- 사연: 아들 → 딸 (누리호 사연과 구분).

## used_content 추가분

### 3. 소행성 2024 YR4 — `asteroid-2026-10` (v1.0)
원본: `space/source/asteroid-2026-10/asteroid-2026-10.txt`, `.srt` (문장 131 / 자막 158, 추정 12:28)
제목: 충돌 확률 3.1%에 생존 배낭부터 샀는데 엿새 뒤 0.004%였습니다. 소행성 뉴스에 놀란 사람들의 공통점

| 구분 | 쓴 내용 |
|---|---|
| 사연 소재·사건 | 소행성 2024 YR4 '2032년 충돌 확률 3.1%, 역대 최고' 쇼츠(가상)를 2025-02-19 아침 출근길에 보고 그날 밤 생존 용품 결제 → 엿새 뒤 0.004% → 달 충돌 4.3%도 2026-03 '가능성 없음' |
| 사연자 | 2025년 마흔하나 여성 직장인, 아홉 살 딸(2032년 열여섯), 남편은 과하다고 반대 |
| 사연 금액·물건 | 생존 배낭 두 개 + 한 달 치 비상식량 + 캠핑용 대용량 배터리 = 150만 원 |
| 사연 문장 | "택배 상자가 현관에 쌓이자 오히려 마음이 놓였어요" / "3%면 백 명 중 세 명이라며 밀어붙였죠" / "엄마가 다 준비해 뒀으니 걱정하지 말라고" / "하지만 그 숫자는 일주일도 버티지 못했어요" / "상자는 이미 다 뜯어서 딸과 함께 배낭까지 싸 둔 뒤였죠" / "잠들기 전마다 2032년에 우리 어떻게 되냐고" / 한탄: "3.1%라는 숫자 하나에 150만 원과 딸의 밤잠을 맞바꾼 셈이에요", "숫자가 왜 바뀌는지 한 번만 찾아봤어도 아이 앞에서 그렇게 겁먹지 않았을 거예요" |
| 진행자 연결 | "역대 최고 충돌 확률이라는 뉴스를 보면 많은 분들이 이런 생각을 하죠" / "실제로 3.1%는 당시 기록이었습니다" / "사연자처럼 겁이 난 것도 무리는 아니었던 거죠" / "그렇다면 이 숫자가 엿새 만에 뒤집힌 진짜 이유는 뭘까요?" |
| 혼잣말 | 3%면 백 번 중 세 번이나 되잖아 / 나사가 발표했으면 진짜 위험한 거겠지 / 확률이 계속 오르면 결국 부딪히는 거 아냐? |
| 사례·발표 | 2024 YR4 발견(2024-12-27, 칠레 ATLAS) / 나사 3.1%(2025-02-18) → 1.5% → 0.28% → 0.004%(02-24), 100년 동안 의미 있는 충돌 위험 없음 / 토리노 3 → 1 → 0 / 달 1.7% → 3.8%(2025-04) → 4.3%(2025-06) → 제임스 웹 관측(2026-02) → 나사 2026-03-05 '가능성 없음', 달 표면 약 21,200km / 크기 40~90m → 제임스 웹 53~67m(약 60m, 10층 건물) / 별명 '도시 파괴급' |
| 연구·통계 | 유럽우주국: 불확실 범위가 좁아지면 확률이 오르고 지구가 빠지면 빠르게 0 / 토리노 척도 3등급·1등급 공식 문구, 2~4등급 = 천문학자 주의 / 나사 2025-12: 1km 이상 873개 발견·약 50개 남음, 140m 이상 11,343개·약 14,000개 남음(약 45%) / 루빈 천문대 2025-06 약 10시간에 새 소행성 2,104개(근지구 7개, 위험 없음) / 다트 2022: 공전 주기 30분 넘게 단축, 최소 목표 73초의 25배 넘게 / 니오 서베이어 2027-09 이후, 5년에 140m 이상 3분의 2 이상 |
| 비유 | 태풍 예상 진로가 날마다 좁아지며 우리 동네가 들어갔다가 빠지는 것 |
| 계산·개념 | 처음 확률 = '아직 모른다'의 다른 말 / 3.1%는 범위가 좁아지는 도중의 숫자, 중간 계산 / "관심을 가질 단계였지, 짐을 쌀 단계라는 뜻은 아니었습니다" / "지구에서 있었던 일이 달에서 한 번 더 반복된 겁니다" |
| 올바른 방법 | 확률 옆에 발견 며칠째를 붙여 읽기(53일 만의 3.1%) / 퍼센트를 등급으로(0·1등급 = 대중이 걱정할 이유 없음, 2~4 = 천문학자 주의, 행동은 정부·공식 기관의 구체적 안내가 나올 때) / 큰돈은 다음 발표 한 번 뒤에(하루 뒤 1.5%로 절반, 엿새 뒤 0.004%, 결제 대신 달력에 일주일 뒤 날짜) — 평소 비상용품 준비는 별개 / 지름 확인(약 60m = 한 지역 규모, 1km 이상은 대부분 찾음) / 아이에게는 지켜보는 사람들(루빈·다트·니오 서베이어)과 지금 등급을 말해 주기 |
| 마무리 당부 | "처음 나온 확률은 아직 모른다는 뜻이라는 것만 기억하셔도 충분합니다" / "발견된 날짜와 등급, 크기부터 확인해 보세요" |

비슷한 유형이라 다음에 피할 것 (추가): 확률이 '올랐다 떨어지는' 위험 뉴스 사연(같은 구조 반복 금지), 생존 용품 구매 사연, 토리노 척도 설명, 태풍 진로 비유

## 근거 자료 은행 추가분

`space/guides/script_rules.md` 9번 표: 아래 "배정: asteroid-2026-10" 줄을 **"사용한 영상: `asteroid-2026-10`"** 으로 바꾸고, 새로 확인한 내용을 덧붙인다.

| 주제 | 내용 | 출처 | 사용한 영상 |
|---|---|---|---|
| 소행성 2024 YR4 발견·크기 | (기존 줄 그대로) + 나사 설명 "10층 건물 정도", 2025년 4월 이후 지상 망원경으로는 너무 어두워짐 | [CNEOS news210](https://cneos.jpl.nasa.gov/news/news210.html), [나사 2024 YR4](https://science.nasa.gov/solar-system/asteroids/2024-yr4/) | `asteroid-2026-10` |
| 2024 YR4 지구 충돌 확률 | (기존 줄) + 1.5%는 미국 시간 02-19 발표(국내 YTN 2025-02-20), 0.28% 때 토리노 1, 02-23 관측 반영 토리노 0, 나사 3.1%는 "이 크기 이상 중 나사 기록 최고", 유럽우주국은 "30m 넘는 소행성 중 최고 확률 기록" | [YTN 2025-02-20](https://www.ytn.co.kr/_ln/0134_202502201704227690), [Weather Network](https://www.theweathernetwork.com/en/news/science/space/impact-odds-of-city-killer-asteroid-2024-yr4-suddenly-drop), [Space.com](https://space.com/the-universe/asteroids/earth-safe-from-city-killer-asteroid-2024-yr4-thats-impact-probability-zero-folks), [나사 2025-02-24](https://science.nasa.gov/blogs/planetary-defense/2025/02/24/latest-calculations-conclude-asteroid-2024-yr4-now-poses-no-significant-threat-to-earth-in-2032-and-beyond) | `asteroid-2026-10` |
| 확률이 올랐다 떨어지는 이유 | (기존 줄 그대로) — 유럽우주국 원문 인용 확인 | [ESA 블로그](https://blogs.esa.int/rocketscience/?p=5746) | `asteroid-2026-10` |
| 2024 YR4 달 충돌 확률 | (기존 줄 그대로) — 2026-03-05 발표, Webb 관측 02-18·26, 21,200km, "궤도 변화가 아니라 정밀도 향상" 검색으로 다시 확인 | [나사 2026-03-05](https://science.nasa.gov/blogs/planetary-defense/2026/03/05/new-nasa-asteroid-observations-eliminate-chance-of-2032-lunar-impact/), [KSL](https://www.ksl.com/article/51459942/new-data-shows-asteroid-2024-yr4-will-narrowly-miss-the-moon) | `asteroid-2026-10` |
| 토리노 척도 | (기존 줄) + 3등급 원문에 "Most likely, new telescopic observations will lead to re-assignment to Level 0", 2~4등급 = "meriting attention by astronomers". ⚠️ 3등급 원문에 "접근이 10년 안이면 대중·공무원의 주의"가 있고 2024 YR4(2032년)는 10년 안이었다 — '대중은 신경 쓸 필요 없다'고 쓰지 않는다 | [CNEOS 토리노 척도](https://cneos.jpl.nasa.gov/sentry/torino_scale.html), [MIT 2005](https://news.mit.edu/2005/torino) | `asteroid-2026-10` |
| 다트(DART) 실험(2022) | (기존 줄) + 후속 논문(Naidu 외)은 33분 15초 → "30분 넘게"로 쓰면 둘 다 맞음 | [APL 2022-10-11](https://www.jhuapl.edu/news/news-releases/221011-dart-mission-impact-changed-asteroids-motion-in-space) | `asteroid-2026-10` |
| 루빈 천문대(2025) | (기존 줄 그대로) | [CNN 2025-06-23](https://cnn.com/2025/06/23/science/vera-rubin-observatory-first-images) | `asteroid-2026-10` |
| 근지구 소행성 발견 현황 | (기존 줄 그대로) — 2025-12-03 숫자 검색으로 확인. 링크는 아래 주소로 | [나사 근지구 소행성](https://science.nasa.gov/science-research/planetary-science/planetary-defense/near-Earth-asteroids/) | `asteroid-2026-10` |
| 니오 서베이어(NEO Surveyor) | (기존 줄) + JPL "no earlier than September 2027", 행성협회 "늦으면 2028년 6월" | [JPL](https://www.jpl.nasa.gov/missions/near-earth-object-surveyor), [행성협회](https://planetary.org/space-missions/neosm) | `asteroid-2026-10` |
| 첼랴빈스크 운석(2013) — 미확인 후보 정리 | 부상 약 1,500명(대부분 깨진 유리창), 건물 약 7,200채 피해는 검색으로 확인. 지름 "약 20m"는 확인 못 함 → 미사용 | [위키백과](https://en.wikipedia.org/wiki/Chelyabinsk_meteor) | 미사용 |
