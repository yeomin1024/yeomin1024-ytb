# 우주 — 대본 전용 규칙

버전: v1.2 — 2026-10-12 — 사용자 지시: 사연은 20~30초로 짧지만 강렬하게 (v1.1 — 2026-10-11 — 첫 영상 3개(누리호·보이저·소행성) 대본 완성: 9번 근거 자료 은행에 사용한 영상 표시·새로 확인한 근거 추가·미확인 후보 정리 (v1.0: 최초 작성, 분석 실행 20261011_120612 결과와 첫 기획 3개에 맞춰))

공통 규칙 `guides/script_guide.md`와 함께 쓴다. **이 파일이 공통 규칙과 다르면 이 파일을 따른다.**
제목은 `guides/title_guide.md` + `space/guides/title_rules.md`, 썸네일은 `guides/thumbnail_guide.md` + `space/guides/thumbnail_rules.md`를 따른다.

---

## 1. 시청자와 사연

- 시청자: 우주 뉴스·영상을 즐겨 보지만 전문 지식은 없는 성인. 쇼츠·자극적인 제목으로 우주 소식을 처음 접하는 사람이 많다 (`data_insights.md` 4·7번: 누리호 쇼츠, '벽을 발견했다' 같은 제목, "썸네일 낚시 영상 보지 마" 댓글).
- **사연은 재구성 사연이다.** 실제 발표·보도(날짜·확률·거리·횟수)를 바탕으로, 그 사건과 삶이 이어진 **평범한 사람**을 만들어 쓴다.
  - **실존 인물을 1인칭으로 흉내 내지 않는다.** 우주비행사, 연구원·엔지니어, 기관장·공무원, 실제 피해자(예: 우주 쓰레기가 떨어진 집의 가족)의 목소리로 쓰지 않는다. 실존 인물은 진행자 파트에서 3인칭 사실로만 말한다.
  - 영상 화면 문구: "실제 발표와 보도를 바탕으로 재구성한 사연" (`guides/video_guide.md` 1-11)
  - 영상 README에 사연 숫자의 **검산 표**(날짜·발표 숫자·사연 숫자·계산)를 남긴다.
- **사연의 각도: 우주 소식을 잘못 받아들여 한 행동을 억울해하고 후회하는 1인칭 고백.**
  - 예: 무서운 확률 숫자를 믿고 돈을 쓴 사람, 첫 실패 뉴스 하나로 가족의 꿈을 꺾은 사람, 자극적인 영상을 사실로 알고 남에게 전한 사람
  - 사연자는 여성이다 (내레이션 사연자 목소리 Sohee). 나이와 생활을 비트 ②에 한 마디로 넣는다 (공통 0-1의 14번). 예: "마흔하나, 아홉 살 아들을 키우는 직장인"
- **사연 숫자 = 실제 발표 숫자.** 확률·거리·날짜·횟수는 실제 발표값을 그대로 쓰고, 사연자의 돈·인원 같은 생활 숫자만 예시로 정한다.
  - 사연 속 돈은 **1천만 원 이하**로 쓴다. 이 주제의 핵심은 돈이 아니라 판단이다. 가격은 실제로 그 정도 하는 물건·서비스로 쓴다.

## 2. 파트 구성과 라벨 (우주 주제의 공통 구조 적용)

공통 구조(사연 → 진행자 → `[장면]` 고지 카드 → 문제 분석 → 올바른 방법 → 마무리)를 그대로 쓴다. 라벨도 공통과 같다.

| 라벨 (그대로) | 우주 주제에서 하는 일 |
|---|---|
| `-사연 파트` | 재구성 사연 7비트 (공통 2-1) |
| `-진행자 파트` | 사람들이 그 소식을 보고 할 만한 생각 3개, 남 일이 아닌 이유 |
| `[장면]` 카드 | 아래 3번 |
| `-문제 분석 파트` | **오해·위험 분석**: 그 소식에서 사람들이 잘못 받아들이는 점을 실제 발표·자료로 하나씩 바로잡는다 |
| `-올바른 방법 파트` | **제대로 아는 법·대처법**: 다음에 비슷한 소식을 볼 때 확인할 것, 언제 걱정·행동해도 되는지 기준 |
| `-마무리` | 7번 |

- **'사연'이라는 낱말은 `-사연 파트` 라벨에만 넣는다.** 내레이션 도구가 라벨에 '사연'이 든 파트를 사연자 목소리로 읽는다. 다른 라벨(예: "-사연 정리")에 넣지 않는다.

## 3. `[장면]` 고지 카드 — 과학 정보 제공용 재구성 사연입니다

화면 고지에 아래 4가지를 모두 넣고 5~6초 노출한다 (공통 0-1의 6번). SRT에는 카드 자리에 3.5초 이상 공백 (공통 5-2).
1. 과학 정보 제공 목적이며, 사연은 실제 발표·보도를 바탕으로 재구성한 이야기
2. 사연 속 인물·금액은 예시이며 실존 인물과 관계없음
3. 확률·거리 같은 수치는 발표 시점 기준이라 새 관측으로 바뀔 수 있음
4. 자료 출처는 설명란에 있음

```
[장면] 과학 정보 제공용 재구성 사연입니다
이 영상은 과학 정보 제공을 위한 것이며, 사연은 실제 발표와 보도를 바탕으로 재구성한 이야기입니다.
사연 속 인물과 금액은 이해를 돕기 위한 예시이며, 실존 인물과 관계없습니다.
확률과 거리 같은 수치는 발표 시점 기준이며, 새로운 관측으로 바뀔 수 있습니다.
영상 속 자료의 출처는 설명란에 있습니다.
```

## 4. 사례·숫자·출처 규칙

1. **사례·연구는 되도록 최신으로 쓴다 (사용자 지시 2026-10-10).** 2020년대를 먼저, 없으면 2010년대까지. **1900년대 사건과 1900년대 자료로 한 연구는 쓰지 않는다.**
   - 쓰지 않는 소재 예: 챌린저호(1986), 아폴로 13호(1970), 아폴로 11호 달 착륙(1969). 분석에서도 '사고·실화' 카테고리가 가장 낮았다 (기회 34점, 성공 21.2%, `data_insights.md` 4번).
   - 컬럼비아호(2003)처럼 2000년대 사건도 2020년대 사례가 있으면 쓰지 않는다.
   - 오래 쓰인 탐사선(예: 보이저, 1977년 발사)은 **2020년대에 일어난 일**(고장·복구, 장비 끄기, 거리 기록)이 중심이어야 한다. 발사 연도는 "50년 가까이" 정도로 한 번만 짚는다.
2. **숫자는 공식 기관·동료 심사 논문·주요 언론 보도에서만 가져온다.**
   - 공식 기관: 미국 항공우주국(나사)·제트추진연구소(JPL)·근지구천체연구센터(CNEOS), 유럽우주국(ESA), 우주항공청, 한국항공우주연구원, 한국천문연구원
   - 블로그·유튜브·쇼츠는 출처로 쓰지 않는다 (그 영상이 사연 속 '잘못 믿은 영상'이어도 숫자는 원문으로 확인).
3. **바뀌는 숫자에는 발표 날짜를 붙인다.** 확률·거리·남은 장비 수는 "2025년 2월 18일 발표 기준"처럼 말한다. 기록 표현("역대 최고", "가장 먼")에는 "당시" 또는 "지금까지"를 붙인다 (공통 0-1의 9번).
4. 보도마다 숫자가 다르면(예: 나사 3.1% / 유럽우주국 2.8%) 한 기관 숫자로 통일하고 어느 기관인지 말한다. README에 둘 다 적는다.
5. **내레이션용으로 읽기 쉽게 쓴다.** 대본 TXT가 곧 내레이션 원고다.
   - 영문 약어는 처음에 한국어로 풀어 말한다: 나사 → "미국 항공우주국 나사", 제임스 웹 우주망원경, 유럽우주국. 괄호·기호를 쓰지 않는다.
   - 큰 수와 확률은 귀로 알아듣게: "259억 킬로미터", "3.1퍼센트, 그러니까 32분의 1".
6. 확인하지 못한 수치는 쓰지 않는다. 기획서(brief)의 숫자도 다시 확인한다. "미확인"으로 표시된 후보는 확인되면 쓰고, 안 되면 뺀다.
7. 새로 쓴 사실은 영상 README 출처 표에 링크·원문 인용·자료 연도를 남긴다.

## 5. 쓰지 않는 것

- 공포 과장: "인류 멸망", "지구 종말", "당장 대피" 같은 말. 실제 발표가 그 정도가 아니면 쓰지 않는다 (분석: 공포/경고 단어 제목 0.59배).
- 음모론을 사실처럼 말하는 것 ("나사가 숨겼다", "달 착륙 조작"). 사연 속 '잘못 믿은 말'로만 나오고, 진행자 파트에서 반드시 바로잡는다.
- 특정 기업의 주식·관련주 이야기, 우주 관련 상품·강의·업체 추천
- 군사·외교 논쟁 (예: 누리호 미사일 논쟁), 다른 나라 비하·국뽕 표현
- 실존 인물 1인칭 (1번)

## 6. 보강 시 경력 시청자(우주 덕후)의 예상 반론과 답 (공통 0-1의 8번)

| 예상 반론 | 대본에서 미리 답하는 방식 |
|---|---|
| 3.1%면 낮은 확률 아냐? 왜 겁먹어? | 맞다고 인정하고, 그래도 '역대 최고'라는 보도가 겹치면 겁먹는 게 자연스럽다는 점, 등급(토리노 척도)으로 보면 행동할 단계가 아니었다는 점을 함께 준다 |
| 결국 나사도 틀린 거네 | 틀린 게 아니라 관측이 늘며 정밀해진 것 (나사 2026-03-05: "궤도가 바뀐 게 아니라 정밀도가 높아진 것") |
| 누리호 성공률 80%면 아직 낮은 거 아냐? | 맞다. 세계 시장 신뢰는 90% 이상이 필요하다는 연구자 말을 인용하고, 횟수가 쌓이는 중이라고 답한다 |
| 보이저는 어차피 곧 꺼지잖아 | 맞다. 전력이 해마다 약 4와트 줄어 장비를 차례로 끄는 중이다. 그래도 '끝났다'와 '아껴 쓰는 중'은 다르다 |
| 다 아는 얘기 아냐? | 2026년 최신 발표(날짜·숫자)로 대조한다. 옛 영상과 다른 점이 바로 최신 숫자다 |

## 7. 분석 결과 반영 (근거: `space/guides/data_insights.md`)

1. **목표 분량은 12~14분이다** (약 3,700~4,400음절, 공통 기본 8~12분보다 길게).
   - 근거: 롱폼 12~20분 성공 35.3%(n=17, 작은 채널 10개 중 5개 성공) vs 8~12분 12.5%(n=8). 보이저 해설 영상이 12~20분에서 작은 채널로 반복 성공.
   - 표본이 작으니 억지로 늘리지 않는다. 모자라면 문제 분석·올바른 방법 항목을 더한다 (문제 분석 4~5개, 올바른 방법 5~6개, 항목마다 5~7문장).
2. **도입:** 사연 첫 문장에 날짜·사건·숫자를 넣는다 (예: "2025년 2월 18일, 소행성이 지구에 부딪힐 확률이 3.1퍼센트라는 영상을 봤어요."). 제목이 약속한 반전은 **첫 문장**에 나온다. 사연 파트는 20~30초(5~7문장·읽는 음절 85~125) — 공통 0-1의 13번 (사용자 지시 2026-10-12). — 도입부 근거는 주식 결과 임시 사용 (`data_insights.md` 5번)
3. **소재 우선순위:** 뉴스·위험(누리호·소행성·우주 쓰레기) → 탐사(보이저·우주망원경·우주정거장) → 우주의 크기. 사고·실화(옛 사건)는 쓰지 않는다. 수면용 다큐는 형식이 달라 소재로 쓰지 않는다.
4. 호기심 단어(진짜·이유·결국)는 제목뿐 아니라 진행자 파트의 넘어가는 문장에 써도 된다 (예: "그렇다면 숫자가 이렇게 뒤집힌 진짜 이유는 뭘까요?").

## 8. 마무리 인사

"우주 소식일수록 숫자와 날짜부터 차분히 확인하셨으면 좋겠습니다." / "감사합니다." (고정 문구, 다시 써도 됨)

## 9. 근거 자료 은행 (2026-10-11 웹 검색으로 검증)

- "사용한 영상"에 이름이 있는 근거는 새 대본에서 다시 쓰지 않는다 (공통 0-1의 11번).
- **"배정"** = 기획 단계에서 그 영상에 나눠 준 근거다. 다른 영상은 쓰지 않는다. 대본을 다 쓰면 "사용한 영상"으로 바꾼다. (v1.1: 첫 영상 3개의 배정 줄은 모두 "사용한 영상"이 됐다. 줄 안에서 쓰지 않은 숫자는 괄호로 적었다.)
- 검증은 웹 검색 결과(기사 요약)로 했다. 2단계(대본 작성, 2026-10-11)에서도 이 환경은 원문 페이지를 열지 못해 **검색 결과의 원문 인용·요약으로 다시 확인**했다. 업로드 전에 원문 링크를 한 번 열어 보면 좋다.
- 첫 영상 3개가 새로 확인해 쓴 근거는 각 영상 아래에 이어 붙였다 (출처: 영상 README "근거 자료 은행 추가분").

| 주제 | 내용 | 출처 | 사용한 영상 |
|---|---|---|---|
| 누리호 1차 발사(2021) | 2021-10-21 1차 발사, 3단 7톤급 엔진이 목표 521초 대신 475초 만에 꺼짐(46초 조기 종료), 목표 고도에는 도달했지만 위성모사체 궤도 진입 실패 | [머니투데이 2022-02-25](https://www.mt.co.kr/tech/2022/02/25/2022022513354446679), [SBS Biz "아깝다 46초"](https://biz.sbs.co.kr/amp/article/20000035405), [경향신문 2026-10-04](https://khan.co.kr/article/202610040800001) | `nuriho-2026-10` |
| 누리호 1차 실패 원인·개선 | 발사조사위원회(2021-12): 3단 산화제탱크 안 헬륨탱크 고정지지부가 풀림. 비행 중 최대 4.3G에서 부력 증가를 설계에 반영하지 않음 → 헬륨 누설·산화제탱크 균열 → 산화제 공급 부족. 개선: 마찰 고정 → 걸쇠 같은 기계식, 4.3G의 1.5배까지 견디게 보강 | [파이낸셜뉴스 2021-12-29](https://www.fnnews.com/news/202112291416336373), [노컷뉴스](https://www.nocutnews.co.kr/news/5757648), [머니투데이 2022-02-25](https://www.mt.co.kr/tech/2022/02/25/2022022513354446679) | `nuriho-2026-10` (1.5배는 노컷뉴스 한 건으로만 확인) |
| 누리호 2~5차·성공률 | 2차 2022년 6월, 3차 2023년 5월, 4차 2025-11-27 새벽(목표 궤도 600km), 5차 2026-10-07 낮 12시 25분 — 2~5차 연속 성공. 성공률 75% → 80%(5회 중 4회). 한 연구자: 세계 시장에서 신뢰받으려면 90% 이상 필요. 6차는 2027년 하반기 목표 | [아이뉴스24 2026-10-07](https://inews24.com/view/2012682), [머니투데이 2026-10-07](https://www.mt.co.kr/article/2026100712582640831), [머니투데이 2025-11-26](https://www.mt.co.kr/tech/2025/11/26/2025112622393154473) | `nuriho-2026-10` |
| 누리호 5차 탑재·사출 | 고도 500km 넘어 주탑재 초소형군집위성 5기 모두 사출, 큐브위성 10기 중 1기('퍼샛-02') 사출관이 열리지 않음 → 15기 중 14기 목표 궤도. 군집위성 6호 남극 세종기지와 첫 교신, 3·4호도 교신 | [MTN 2026-10-07](https://news.mtn.co.kr/news-detail/2026100716330458112), [MTN 사출](https://news.mtn.co.kr/news-detail/2026100712511432601), [SBS Biz](https://biz.sbs.co.kr/amp/article/20000338743) | `nuriho-2026-10` (퍼샛은 이름 없이 "큐브위성 1기", 세종기지 교신은 쓰지 않음) |
| 누리호 민간 운영 | 5차는 한화에어로스페이스가 '주운영자'로 발사·교신 | [MTN 2026-10-08](https://news.mtn.co.kr/news-detail/2026100812444652520) | `nuriho-2026-10` (기업 이름은 쓰지 않고 "민간 기업") |
| 누리호 1차 원인 조사 데이터 | 발사조사위원회(과기정통부·항우연)가 비행 중 받은 텔레메트리 데이터 2,600여 개로 원인 분석 → 2021-12-29 발표 | [파이낸셜뉴스 2021-12-29](https://www.fnnews.com/news/202112291416336373), [노컷뉴스](https://nocutnews.co.kr/news/5714122) | `nuriho-2026-10` |
| 궤도 속도·1차 도달 단계 | 위성을 궤도에 올리려면 초속 7.5km. 1차는 1단 분리·페어링 분리·700km 도달·모사체(1.5t) 분리까지 성공, '절반의 성공' 평가 | [뉴시스 2022-06-21](https://www.newsis.com/view/NISX20220621_0001914924), [데일리안](https://www.dailian.co.kr/news/view/1123305/) | `nuriho-2026-10` |
| 누리호 2차 의미 | 2022-06-21 오후 4시, 성능검증위성 700km 궤도. 1t 이상 실용위성을 자체 발사한 세계 7번째 | [스마트투데이](https://www.smarttoday.co.kr/ko-kr/articles/23579), [경북매일](https://kbmaeil.com/article/202206210337721) | `nuriho-2026-10` |
| 누리호 3차·도요샛 3호 | 2023-05-25 오후 6시 24분, 첫 실용위성 8기(차세대소형위성 2호 등). 도요샛 3호는 사출관 문이 열리지 않아 미사출(2023-06 분석, 사출 명령은 정상), 발사는 성공 평가 | [머니투데이 2023-05-25](https://www.mt.co.kr/tech/2023/05/25/2023052515135396944), [YTN 2023-06-04](https://www.ytn.co.kr/_ln/0105_202306040538374850), [뉴스서울](https://newsseoul.co.kr/news/view/1065593407251485) | `nuriho-2026-10` |
| 누리호 4차 | 2025-11-27 새벽 1시 13분(압력 센서 신호 이상으로 18분 늦춤), 첫 야간 발사, 차세대중형위성 3호 분리 고도 601.3km(기준 600±35km) | [뉴스토마토](https://newstomato.com/ReadNews.aspx?no=1283066), [쿠키뉴스](https://www.kukinews.com/article/view/kuk202511270014), [전북일보](https://www.jjan.kr/article/20251127500004) | `nuriho-2026-10` (첫 야간 발사만) |
| 누리호 5차 성공 기준·향후 | 성패 기준: 네온샛 5기를 570km ±15km에 투입, 큐브위성은 부차 임무. 퍼샛은 사출 신호 정상·미분리, 정부 "사출관, 위성업체 소관". 6차 2027년 하반기, 2032년까지 매년 1회 이상 | [YTN 2026-10-07](https://www.ytn.co.kr/_ln/0105_202610071557514831), [더팩트](https://news.tf.co.kr/read/ogmeta/2373979.htm), [조선 미래](https://futurechosun.com/?p=162251), [아이뉴스24](https://inews24.com/view/2012682) | `nuriho-2026-10` |
| 성공률 90% 기준 | 세계 시장 신뢰 90% 이상, 추가 실패 없이 10번째 발사까지 가야 달성 (5차 전 기사, 5차 뒤에도 조건 같음) | [경향신문 2026-10-04](https://khan.co.kr/article/202610040800001) | `nuriho-2026-10` |
| 일본 H3 첫 발사 실패(2023)·성공(2024) | 30년 만의 신형 주력 로켓. 2023-03-07(한국 시간) 1호기 2단 엔진 미점화 → 파괴 명령, 관측위성 다이치 3호 손실. 2024-02-17 2호기 성공("실패 1년 만에") | [UPI 2023-03-06](https://www.upi.com/Science_News/2023/03/06/Japan-H3-rocket-launch-fails/7611678152873/), [Seradata](https://www.seradata.com/h3-rocket-fails-on-maiden-flight-losing-alos-3-into-sea-after-second-stage-fails-to-ignite/), [뉴시스 2024-02-17](https://www.newsis.com/view/NISX20240217_0002630060), [다음(2024-02-17)](https://v.daum.net/v/20240217104504439) | `nuriho-2026-10` |
| 보이저 1호 고장·복구(2023~2024) | 2023-11-14부터 알아볼 수 없는 데이터 → 2024-03 원인: 비행 데이터 컴퓨터(FDS) 메모리 칩 하나 고장 → 코드를 나눠 다른 곳에 옮김, 2024-04-18 명령, 04-20 상태 정보 복구 → 2024-06-13 과학 장비 4개 데이터 복구 | [CNN(KTVZ) 2024-06-18](https://ktvz.com/cnn-other/2024/06/18/voyager-1-sends-back-science-data-from-more-than-15-billion-miles-away-after-nasa-fix/), [The Register 2024-04-23](https://www.theregister.com/2024/04/23/voyager_1_engineering_updates/), [Nextgov 2024-04](https://www.nextgov.com/digital-government/2024/04/nasa-restores-data-transmissions-voyager-1-spacecraft/396044/) | `voyager-2026-10` |
| 보이저 전력·장비 끄기(2025~2026) | 두 탐사선 모두 해마다 전력 약 4와트 감소(원자력 전지). 2025-02-25 보이저 1호 우주 방사선 측정 장비 끔, 2025-03-24 보이저 2호 저에너지 입자 장비 끔. 2026-02 말 보이저 1호 전력 급락으로 자동 보호 직전 → 2026-04-17 보이저 1호 저에너지 입자 장비 끔(회전 모터 0.5와트는 켜 둠), 남은 과학 장비 2개(플라스마파·자기장), 약 1년 여유 | [JPL 2025-03](https://jpl.nasa.gov/news/nasa-turns-off-two-voyager-science-instruments-to-extend-mission), [나사 보이저 블로그 2026-04-17](https://science.nasa.gov/blogs/voyager/2026/04/17/nasa-shuts-off-instrument-on-voyager-1-to-keep-spacecraft-operating/), [Universe Today](https://www.universetoday.com/articles/another-instrument-shut-down-on-voyager-1-to-extend-its-interstellar-mission) | `voyager-2026-10` (보이저 2호 2025-03 장비 끄기는 쓰지 않음, 회전 모터 0.5와트는 확인 못 해 미사용) |
| 보이저 1호 1광일(2026) | 2026-11-18 지구에서 빛으로 하루 거리 도달: 25,902,068,356km(약 259억 km, 173.14AU). 시각은 미국 태평양 표준시 새벽 2시 16분 = 한국 시간 18일 저녁 7시 16분(계산). 국내 보도는 11월 13~15일로 쓴 곳도 있음 → 나사 발표 기준 18일 | [EarthSky](https://earthsky.org/space/voyager-1-1-light-day-from-earth-november-17-18-2026/), [IFLScience](https://iflscience.com/its-official-voyager-1-will-cross-the-1-light-day-threshold-on-november-18-2026-82733), [ScienceAlert](https://www.sciencealert.com/voyager-1-has-been-flying-across-space-since-1977-and-still-hasnt-traveled-1-light-day), [뉴스스페이스 2026-09-03](https://newsspace.kr/news/article.html?no=10906) | `voyager-2026-10` |
| 보이저 통신 | 송신기 출력 약 22~23와트, 나사 심우주통신망 70m 안테나(미국·스페인·호주). 2026-07-23 거리 약 255억 km, 신호 왕복 약 47시간 | [ScienceBlog](https://scienceblog.com/t-voyager1-22-watt-radio-signal-16-billion-miles/), [KeepTrack(JPL Horizons)](https://keeptrack.space/top-10/10-deep-space-probes-still-phoning-home), [ingenieur.de 2026-04-20](https://www.ingenieur.de/technik/fachbereiche/raumfahrt/strom-wird-knapp-wie-lange-sendet-voyager-1-noch-daten/) | `voyager-2026-10` (송신기·안테나만 — 아래 '심우주통신망·송신기' 줄의 제트추진연구소 자료로. 7월 255억 km·왕복 47시간은 공식 기관 자료로 확인 못 해 미사용) |
| 보이저 1호 고장·복구(2023~2024) — 세부 | 2023-12 나사: 명령은 받아 실행 중(비행 데이터 컴퓨터와 송신 장치 사이 문제) / 2024-03-01 메모리 읽기 명령 → 03-03 새 신호 / 2024-04-04 메모리 약 3% 손상·칩 하나(원인: 고에너지 입자 또는 낡음, 확실하지 않음) / 코드를 나눠 여러 자리에 저장 / 편도 약 22.5시간 / "다섯 달 만에" | [나사 블로그 2024-03-15](https://science.nasa.gov/blogs/voyager/2024/03/15/nasa-engineers-make-progress-toward-understanding-voyager-1-issue), [나사 블로그 2024-04-04](https://science.nasa.gov/blogs/voyager/2024/04/04/engineers-pinpoint-cause-of-voyager-1-issue-are-working-on-solution/), [나사 2024-04](https://blogs.nasa.gov/voyager/2024/04), [Space.com 2024-06](https://www.space.com/voyager-1-fully-operational) | `voyager-2026-10` |
| 보이저 1호 송신기 전환(2024) | 2024-10 히터 명령 뒤 보호 기능으로 X밴드 송신기 꺼짐 → 1981년 이후 안 쓰던 S밴드로 신호 → 10-22 확인·10-24 재연결 → 11월 중순 X밴드·과학 자료 재개 | [CNN 2024-11-01](https://edition.cnn.com/2024/11/01/science/voyager-1-transmitter-issue/index.html), [Smithsonian](https://www.smithsonianmag.com/smart-news/voyager-1-breaks-its-silence-with-nasa-via-a-radio-transmitter-not-used-since-1981-180985399/) | `voyager-2026-10` |
| 보이저 1호 주 추진기 복구(2025) | 2004년 히터 전원 문제로 멈춘 주 방향(롤) 추진기를 2025-03-20 되살림(2025-05-14 발표). 예비 추진기 연료관 막힘 우려, 캔버라 70m 안테나 정비(2025-05~2026-02) 전 | [CNN 2025-05-14](https://edition.cnn.com/2025/05/14/science/voyager-1-thruster-fix), [IFLScience](https://iflscience.com/after-21-years-voyager-1-fires-its-thrusters-again-thanks-to-long-distance-servicing-79235) | `voyager-2026-10` |
| 보이저 2호 'Big Bang' 전력 절약(2026) | 2026-08-04 나사: 히터 2개·열용 기록 장치를 끄고 저전력 장치를 켬 → 남은 과학 장비 3개 적어도 1년 더(안 하면 2026년 안에 하나 꺼야 했음). 보이저 1호에도 계획 | [나사 블로그 2026-08-04](https://science.nasa.gov/blogs/voyager/2026/08/04/nasa-engineers-help-prolong-voyager-2s-science-mission/), [Space.com](https://space.com/space-exploration/voyager/nasa-figured-out-how-to-keep-its-48-year-old-voyager-2-probe-running-for-yet-another-year) | `voyager-2026-10` |
| 보이저 인용(2025) | 수잔 도드(프로젝트 책임자): 지금 장비를 안 끄면 몇 달 뒤 임무 종료 선언 / 린다 스필커(프로젝트 과학자): "매일이 마지막일 수 있다" | [제트추진연구소 2025-03-05](https://www.jpl.nasa.gov/news/nasa-turns-off-two-voyager-science-instruments-to-extend-mission/), [The Debrief](https://thedebrief.org/every-day-could-be-our-last-voyager-instruments-shut-down-as-iconic-spacecraft-continue-farthest-ever-journey-from-earth/) | `voyager-2026-10` (대본에는 이름 없이 역할만) |
| 심우주통신망·송신기 | 송신기 약 23와트(냉장고 전구, 보도마다 20~23와트) / 골드스톤·마드리드·캔버라 120도 간격, 70m 안테나 | [제트추진연구소 보이저 글](https://voyager.jpl.nasa.gov/news/details.php?article_id=50), [제트추진연구소 심우주통신망](https://jpl.nasa.gov/deep-space-network-now) | `voyager-2026-10` |
| 헬리오포즈·'불의 벽'(2012~2013, 2025 보도) | 2012-08-25 통과(2013-09 나사 발표, Gurnett 외 Science), 2013-04~05 전자 밀도 약 0.08개/cm³. 2025년 '불의 벽' 보도: 벽이 아니라 경계, 아주 뜨겁지만 희박해 탐사선을 데우지 못함 (온도 3만~5만 K는 원 논문 미확인) | [제트추진연구소 2013](https://www.jpl.nasa.gov/news/nasa-spacecraft-embarks-on-historic-journey-into-interstellar-space/), [Science News](https://www.sciencenews.org/article/last-voyager-1-slips-interstellar-space), [IFLScience](https://iflscience.com/nasas-voyager-spacecraft-found-a-30000-50000-kelvin-wall-at-the-edge-of-our-solar-system-81411) | `voyager-2026-10` (2010년대 자료 — 2020년대 대체 자료 없음, 영상 README 메모) |
| 보이저 1호 1광일 — 정정 | 나사 위치 페이지: 2026-11-18 2:16:07 a.m. PST(10:16 UTC = 한국 19:16), 160억 9,400만 마일. EarthSky의 "12:16 a.m. CST"는 시간대 표기 오류로 보임. 이전 예상 11월 13일(Gigazine 2025-11)·15일(PopSci). 1광일 왕복 약 48시간(도드) | [나사 위치 페이지](https://science.nasa.gov/mission/voyager/where-are-voyager-1-and-voyager-2-now/), [EarthSky](https://earthsky.org/space/voyager-1-1-light-day-from-earth-november-17-18-2026/), [PopSci](https://popsci.com/science/voyager-one-light-day-earth) | `voyager-2026-10` |
| 소행성 2024 YR4 발견·크기 | 2024-12-27 칠레 ATLAS 망원경이 발견. 지상 관측 지름 40~90m → 제임스 웹 우주망원경(2025-03 관측, 4월 발표) 53~67m(약 60m). 나사 설명 "10층 건물 정도". 2025년 4월 이후 지상 망원경으로는 너무 어두워짐 | [나사 2024 YR4 페이지](https://science.nasa.gov/solar-system/asteroids/2024-yr4/), [CNEOS news210](https://cneos.jpl.nasa.gov/news/news210.html), [YTN(연합뉴스) 2025-02-20](https://www.ytn.co.kr/_ln/0134_202502201704227690) | `asteroid-2026-10` |
| 2024 YR4 지구 충돌 확률 | 2025-02-18 나사 3.1%(32분의 1, 이 크기 이상 소행성 중 당시 나사 기록 최고. 유럽우주국은 2.8%, "30m 넘는 소행성 중 최고 확률 기록"). 2004년 아포피스 2.7%를 넘음 → 02-19(미국 시간) 1.5% → 02-20 0.28%(360분의 1, 1% 아래로 내려가 토리노 1) → 02-23 관측 반영 토리노 0 → 02-24 0.004%(2만 5천분의 1, 다음 100년 의미 있는 충돌 가능성 없음). 유럽우주국 최종 0.001% | [Live Science](https://livescience.com/space/asteroids/asteroid-yr4-impact-odds-plummet-as-nasa-changes-threat-level-of-city-killer), [WTTW 2025-02-19](https://news.wttw.com/2025/02/19/will-asteroid-hit-earth-2032-space-rock-has-highest-impact-probability-ever-recorded-s), [YTN 2025-02-20](https://www.ytn.co.kr/_ln/0134_202502201704227690), [Weather Network](https://www.theweathernetwork.com/en/news/science/space/impact-odds-of-city-killer-asteroid-2024-yr4-suddenly-drop), [Space.com](https://space.com/the-universe/asteroids/earth-safe-from-city-killer-asteroid-2024-yr4-thats-impact-probability-zero-folks), [나사 2025-02-24](https://science.nasa.gov/blogs/planetary-defense/2025/02/24/latest-calculations-conclude-asteroid-2024-yr4-now-poses-no-significant-threat-to-earth-in-2032-and-beyond), [Boston.com 2025-02-25](https://www.boston.com/news/world-news/2025/02/25/nasa-gives-all-clear-asteroid-threaten-earth/), [ESA](https://www.esa.int/Space_Safety/Planetary_Defence/Asteroid_2024_YR4_no_longer_poses_significant_impact_risk), [파이낸셜뉴스 2025-02-20](https://www.fnnews.com/news/202502200941001866) | `asteroid-2026-10` (나사 숫자로 통일 — 유럽우주국 숫자는 README에만. 아포피스 2.7%는 2000년대 자료라 미사용) |
| 확률이 올랐다 떨어지는 이유 | 관측이 쌓이면 궤도 불확실 범위가 줄어든다. 지구가 그 범위 안에 남아 있으면 확률이 오르고, 범위가 지구를 벗어나면 빠르게 0으로 떨어진다 (유럽우주국 설명 — 원문 인용 확인, 2026년 논문도 같은 설명) | [CTV](https://www.ctvnews.ca/sci-tech/article/an-asteroids-chances-of-hitting-earth-keep-shifting-heres-why-that-is-happening/), [ESA](https://www.esa.int/Space_Safety/Planetary_Defence/Asteroid_2024_YR4_no_longer_poses_significant_impact_risk), [ESA 블로그](https://blogs.esa.int/rocketscience/?p=5746), [Springer 2026](https://link.springer.com/article/10.1007/s40295-026-00576-0) | `asteroid-2026-10` |
| 2024 YR4 달 충돌 확률 | 2025-02 말 1.7% → 2025-04 3.8% → 2025-06-03 4.3% → 제임스 웹 관측(2026-02-18·26)으로 2026-03-05 나사 "2032-12-22 달 충돌 가능성 없음", 달 표면에서 약 21,200km 지나감. "궤도가 바뀐 게 아니라 위치를 더 정밀하게 알게 된 것" | [나사 행성방위 블로그 2026-03-05](https://science.nasa.gov/blogs/planetary-defense/2026/03/05/new-nasa-asteroid-observations-eliminate-chance-of-2032-lunar-impact/), [KSL](https://www.ksl.com/article/51459942/new-data-shows-asteroid-2024-yr4-will-narrowly-miss-the-moon), [Discover](https://www.discovermagazine.com/chances-of-city-killer-asteroid-impacting-the-moon-raised-from-3-8-to-4-3-47700), [Sky at Night](https://www.skyatnightmagazine.com/news/asteroid-2024-yr-wont-hit-our-moon) | `asteroid-2026-10` |
| 토리노 척도 | 0~10등급. 1 = 일상적 발견, 대중이 걱정할 이유 없음, 새 관측으로 보통 0이 됨. 3 = 천문학자의 주의 필요(충돌 확률 1% 이상, 국지적 피해 규모, 원문 "Most likely, new telescopic observations will lead to re-assignment to Level 0"), 대중·공무원의 주의는 접근이 10년 안일 때. 2~4등급 = "meriting attention by astronomers". 2005년 개정 때 "사람들을 겁준다"는 비판으로 문구를 바꿈. 2024 YR4: 3 → 1 → 0. ⚠️ 2024 YR4(2032년)는 접근이 10년 안이었다 — '대중은 신경 쓸 필요 없다'고 쓰지 않는다 | [CNEOS 토리노 척도](https://cneos.jpl.nasa.gov/sentry/torino_scale.html), [행성협회 토리노 척도](https://www.planetary.org/articles/the-torino-scale), [행성협회 2005 개정](https://www.planetary.org/articles/astronomers-revise-torino), [MIT 2005](https://news.mit.edu/2005/torino), [CNEOS](https://cneos.jpl.nasa.gov/news/news210.html), [Space.com](https://space.com/the-universe/asteroids/earth-safe-from-city-killer-asteroid-2024-yr4-thats-impact-probability-zero-folks) | `asteroid-2026-10` (2005년 개정 이야기는 2000년대 자료라 대본에 쓰지 않음) |
| 다트(DART) 실험(2022) | 2022-09-26 탐사선 충돌로 소행성 디모르포스의 공전 주기 11시간 55분 → 11시간 23분(32분 단축, ±2분). 나사 최소 목표 73초의 25배 넘게. 후속 논문(Naidu 외)은 33분 15초 → "30분 넘게"로 쓰면 둘 다 맞음 | [APL 2022-10-11](https://www.jhuapl.edu/news/news-releases/221011-dart-mission-impact-changed-asteroids-motion-in-space), [APS Physics](https://physics.aps.org/articles/v15/156), [Science News](https://www.sciencenews.org/article/dart-mission-deflected-asteroid-for-planetary-defense) | `asteroid-2026-10` |
| 루빈 천문대(2025) | 2025-06-23 첫 영상 공개, 약 10시간 관측으로 새 소행성 2,104개(근지구 소행성 7개, 위험 없음). 다른 모든 관측소가 1년에 찾는 수는 약 2만 개 | [CNN 2025-06-23](https://cnn.com/2025/06/23/science/vera-rubin-observatory-first-images), [Fox 13](https://www.fox13news.com/news/vera-rubin-observatory-discovers-2000-unknown-asteroids-within-10-hours) | `asteroid-2026-10` |
| 근지구 소행성 발견 현황 | 나사 집계(2025-12-03): 근지구 소행성 39,123개 발견. 140m 이상 11,343개 발견·약 14,000개 남음(자체 계산 약 45% 발견), 1km 이상 873개 발견·약 50개 남음 (2단계에서 검색으로 숫자 확인) | [나사 근지구 소행성](https://science.nasa.gov/science-research/planetary-science/planetary-defense/near-Earth-asteroids/) (v1.0 링크 `science.nasa.gov/solar-system/asteroids-comets-meteors/near-earth-asteroids`에서 바꿈) | `asteroid-2026-10` |
| 니오 서베이어(NEO Surveyor) | 2027년 9월 이후 발사 예정(팰컨 9, JPL "no earlier than September 2027", 행성협회: 늦으면 2028년 6월). 5년 탐사로 아직 못 찾은 140m 이상 근지구 천체의 3분의 2 이상을 찾는 목표 | [JPL](https://www.jpl.nasa.gov/missions/near-earth-object-surveyor), [행성협회](https://planetary.org/space-missions/neosm), [위키백과](https://en.wikipedia.org/wiki/NEO_Surveyor) | `asteroid-2026-10` |
| 첼랴빈스크 운석(2013) | 부상 약 1,500명(대부분 깨진 유리창), 건물 약 7,200채 피해는 검색으로 확인. 지름 "약 20m"는 확인 못 함 | [위키백과](https://en.wikipedia.org/wiki/Chelyabinsk_meteor) | 미사용 (2010년대 사건이고 공포를 키울 수 있어 `asteroid-2026-10`에서 뺌) |
| 인공위성 추락 경보(2023) | 2023-01-09 과기정통부 경계경보, 전 국민 안전 안내 문자(낮 12시 20분~1시 20분 한반도 인근 추락 가능성, 외출 유의), 전국 공항 이륙 금지 12시 10분~1시 19분·71편 지연. 실제로는 베링해 상공에서 대부분 연소, 피해 없음 | [뉴시스 2023-01-09](https://www.newsis.com/view/NISX20230109_0002152327), [phys.org 2023-01](https://phys.org/news/2023-01-nasa-satellite-falling-sky-weekend.html) | 미사용 (우주 쓰레기 영상 후보) |
| 우주 쓰레기가 집을 뚫음(2024) | 2024-03-08 미국 플로리다 네이플스 주택 지붕과 2층을 뚫은 물체 → 나사(03-17) 국제우주정거장 배터리 운반대(2021년 버림)의 부품 확인, 약 0.7kg. 보상 결과는 확인 못 함 | [WQCS 2024-04-17](https://www.wqcs.org/wqcs-news/2024-04-17/nasa-confirms-object-that-crashed-through-roof-of-naples-home-came-from-the-space-station?_amp=true), [Fox Weather](https://www.foxweather.com/earth-space/nasa-investigates-iss-space-junk-falling-florida-home) | 미사용 (실제 가족을 1인칭으로 쓰지 않는다) |
| 미확인 후보 (v1.1 정리) | 확인되어 쓴 것: 일본 H3 1호기 실패·2호기 성공 → 위 'H3' 줄(`nuriho-2026-10`) / 보이저 1호 태양권 경계 통과(2012) → 위 '헬리오포즈' 줄(`voyager-2026-10`) / 첼랴빈스크 → 위 줄(미사용). **아직 확인 안 함 (쓰려면 먼저 확인):** 스타십 첫 통합 비행 폭발(2023-04) / 유럽 베가C 실패(2022-12 — 첫 발사가 아니라 두 번째 비행이라 '첫 발사 실패' 사례로는 맞지 않음) / 한국 성인의 유튜브 뉴스 이용률(세 영상 모두 쓰지 않음) / 누리호 5차 "역대 첫 정시 발사"(2차도 정각 발사 보도라 기준 불분명) | 웹 검색 할당량·차단으로 확인하지 못함 | — |

### 9-1. 확인하지 못해 뺀 숫자 (첫 영상 3개, 2026-10-11 — 확인 전에는 다음 대본에도 쓰지 않는다)

| 영상 | 뺀 숫자·표현 | 이유 |
|---|---|---|
| `nuriho-2026-10` | 1차 실제 도달 속도 초속 6.7km / 1차 "발사 36초 무렵 고정장치 풀림"(검색 요약에만 있음) / 5차 "역대 첫 정시 발사"(기준 불분명 — 그래서 1차 1시간·4차 18분 지연 문장도 함께 뺌) / 우주산업 일자리·연봉·학과 진학 통계 / 누리호 개발비 | 확인 못 함, 46초와 헷갈림, 개발비는 정치 논쟁(세금)을 피하려고 뺌 |
| `voyager-2026-10` | 저에너지 입자 장비를 끌 때 회전 모터 0.5와트 / 2026-07 거리 255억 km·왕복 47시간(KeepTrack) / 보이저 1호 'Big Bang' 결과 / 2030년대 중반까지 임무 전망 / '불의 벽' 온도 3만~5만 K / 수신 전력 / "사람이 만든 물체로 처음 1광일" | 공식 기관 자료로 확인 못 함, 보도마다 숫자가 다름 |
| `asteroid-2026-10` | 첼랴빈스크 지름 약 20m / 비상식량 국내 가격(기획서 230만 원 → 확인된 가격으로 150만 원) / "반품 기한이 지난 발전기" / 다트 "정확히 32분"(33분 15초 논문과 달라 "30분 넘게") | 확인 못 함, 날짜상 단정할 근거 없음 |

## 변경 이력

| 버전 | 날짜 | 변경 내용 |
|---|---|---|
| v1.2 | 2026-10-12 | 사용자 지시: 사연은 20~30초로 짧지만 강렬하게 — 결과 숫자는 첫 문장(30초 안), 공통 0-1의 13번 |
| v1.1 | 2026-10-11 | 9번 근거 자료 은행: 배정 줄(누리호 5·보이저 4·소행성 9)을 사용한 영상으로 바꾸고 쓰지 않은 숫자는 괄호로 표시, 영상 README '근거 자료 은행 추가분'의 새 줄 추가(누리호 8·보이저 8·첼랴빈스크 1 — 소행성 추가분은 기존 줄에 합침), 미확인 후보 정리, 9-1 확인하지 못해 뺀 숫자 표 |
| v1.0 | 2026-10-11 | 최초 작성: 시청자·재구성 사연(실존 인물 흉내 금지, 억울·후회 고백 각도), 파트 구성(문제 분석 = 오해·위험 분석, 올바른 방법 = 제대로 아는 법·대처법, 라벨은 공통 그대로), 고지 카드 4요소, 출처·숫자 규칙(최신, 1900년대 사건 금지, 발표 날짜 붙이기, 내레이션용 표기), 쓰지 않는 것, 예상 반론, 목표 분량 12~14분, 마무리 인사, 근거 자료 은행 20줄 |
