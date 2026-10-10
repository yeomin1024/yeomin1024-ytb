// 데이터 시트 — guides/video_guide.md 4번. 화면 숫자는 여기 값만 쓴다.
// 구분: 대본 = SRT에 나온 값 / 계산 = 대본 숫자 또는 README 검산표로 계산한 값(식 포함) / 예시 = 대본의 예시 규칙
//       출처 = 대본 문장의 근거 자료(README 출처 표)에만 있는 값 — 막대 길이 비율에만 쓰고 화면에 숫자로 표시하지 않는다
// 검산·출처: stock/source/panicsell-2026-10/README.md (번호는 대본 문장 번호)
// ※ 투자 교육용. 특정 종목의 매수·매도 권유가 아님.

export type Kind = "대본" | "계산" | "예시" | "출처";
export type Fact = {v: number | string; sub: number[]; kind: Kind; note?: string};

export const F = {
  // ── 사연 (재구성, 문장 1–16) ──
  crashDay: {v: "3월 4일", sub: [1, 22, 28, 45, 70, 88], kind: "대본", note: "2026년 3월 4일"},
  crashYear: {v: "2026년", sub: [1], kind: "대본"},
  kospiDrop: {v: 12, sub: [1], kind: "대본", note: "%, '12% 넘게' (실제 -12.06%, 코스피 5,093.54)"},
  fiveDays: {v: "닷새 전", sub: [2], kind: "대본", note: "README 매수일 2026-02-27(금) 종가"},
  invest: {v: 4000, sub: [2, 62], kind: "대본", note: "만 원, 4천만 원으로 매수"},
  company: {v: "삼성전자", sub: [2, 12], kind: "대본"},
  reason: {v: "반도체가 잘 팔린다", sub: [3], kind: "대본"},
  holdLong: {v: "오래 들고 갈 생각", sub: [3], kind: "대본"},
  dayAfterBuy: {v: "산 다음 날", sub: [4], kind: "대본", note: "README: 2026-02-28 공격(휴장일)"},
  attack: {v: "미국·이스라엘, 이란 공격", sub: [4], kind: "대본"},
  firstTradeDay: {v: "3월 3일", sub: [5], kind: "대본", note: "연휴 뒤 첫 거래일 (3/1 일요일·3/2 대체공휴일 휴장)"},
  holiday: {v: "연휴 뒤 첫 거래일", sub: [5], kind: "대본"},
  pnl0303: {v: -400, sub: [5], kind: "대본", note: "만 원 (README 검산 -395)"},
  nextDay: {v: "다음 날", sub: [7], kind: "대본", note: "3월 3일 다음 날 = 3월 4일"},
  cbTime: {v: "오전 11시쯤", sub: [8], kind: "대본", note: "코스닥 11:16, 코스피 11:19 발동"},
  cbMinutes: {v: 20, sub: [8], kind: "대본", note: "분, 시장 전체 거래 중단"},
  pnl0304: {v: -800, sub: [9, 15, 67, 71, 77], kind: "대본", note: "만 원, '-800만 원이 넘어' (README 검산 -818)"},
  pnl0304Exact: {v: -818, sub: [9], kind: "계산", note: "4,000 × (172,200 ÷ 216,500 - 1) = -818. 막대 길이 비율에만 사용(숫자 표시 안 함)"},
  news: {v: "전쟁 확대 · 유가 ↑ · 환율 ↑", sub: [10], kind: "대본"},
  sellWhen: {v: "장 마감 직전", sub: [11], kind: "대본"},
  sellAll: {v: "전부 매도", sub: [11], kind: "대본", note: "'모두 팔았어요'"},
  nextDayRise: {v: 11, sub: [12, 38], kind: "대본", note: "%, '11% 넘게' (172,200 → 191,600원 +11.27%)"},
  weeks7: {v: "7주 뒤", sub: [13], kind: "대본", note: "3/4 → 4/23"},
  rise30: {v: 30, sub: [13], kind: "대본", note: "%, 판 가격보다 '30% 넘게' (4/23 224,500원 +30.4%)"},
  aboveBuy: {v: "처음 산 가격", sub: [14], kind: "대본", note: "216,500원, 4/16 처음 넘음"},
  thrown: {v: 800, sub: [15], kind: "대본", note: "만 원, '내던진 800만 원'"},

  // ── 진행자 (문장 17–26) ──
  vkospi: {v: 80, sub: [22], kind: "대본", note: "'80을 넘어 사상 최고' (실제 80.37)"},
  tradeValue: {v: 58, sub: [24], kind: "대본", note: "조 원, '58조 원을 넘어 사상 최대' (실제 58조 6,880억 원)"},

  // ── 문제 01 (문장 27–36) ──
  kospiNext: {v: 10, sub: [29], kind: "대본", note: "%, '10% 가까이' (3/5 +9.63%)"},
  covidYear: {v: "2020년", sub: [30], kind: "대본"},
  covidDay: {v: "3월 19일", sub: [31], kind: "대본"},
  covidDrop: {v: 8, sub: [31], kind: "대본", note: "%, '8% 넘게' (-8.39%)"},
  covidRise: {v: 7, sub: [31], kind: "대본", note: "%, 다음 날 '7% 넘게' (+7.44%)"},
  jpm: {v: "JP모건", sub: [32], kind: "대본", note: "미국 자산운용사"},
  jpmFrom: {v: 2006, sub: [32], kind: "대본"},
  jpmYears: {v: 20, sub: [32], kind: "대본"},
  jpmTo: {v: 2025, sub: [32], kind: "계산", note: "2006 + 20 - 1 = 2025 (README: 2006-01-02 ~ 2025-12-31)"},
  index: {v: "S&P 500", sub: [32], kind: "대본"},
  jpmStart: {v: 1000, sub: [33], kind: "대본", note: "만 원 (원화는 비율만 옮긴 것)"},
  jpmAll: {v: 8000, sub: [33], kind: "대본", note: "만 원, '8천만 원이 넘었습니다' ($10,000 → $80,619)"},
  jpmMiss: {v: 3600, sub: [34], kind: "대본", note: "만 원, 최고의 10일 제외 ($35,866)"},
  bestDays: {v: 10, sub: [34, 35], kind: "대본", note: "가장 많이 오른 10일"},
  nearWorst: {v: 6, sub: [35], kind: "대본", note: "10일 중 6일, 가장 크게 떨어진 10일과 2주 안"},
  twoWeeks: {v: "2주 안", sub: [35], kind: "대본"},

  // ── 문제 02 (문장 37–43) ──
  mit: {v: "MIT 연구진", sub: [40], kind: "대본", note: "미국. Elkind, Kaminski, Lo, Siah, Wong (2022)"},
  mitFrom: {v: 2003, sub: [40], kind: "대본"},
  mitYears: {v: 13, sub: [40], kind: "대본", note: "2003-01 ~ 2015-12"},
  accounts: {v: "65만여 개", sub: [40], kind: "대본", note: "계좌 653,455개"},
  panicMonth: {v: "한 달 사이", sub: [41], kind: "대본"},
  panicPct: {v: 90, sub: [41], kind: "대본", note: "%, 주식을 '90% 넘게' 정리"},
  neverBack: {v: 31, sub: [42], kind: "대본", note: "%, 다시 주식으로 돌아오지 않음"},

  // ── 문제 03 (문장 44–49) ──
  kospiLowDay: {v: "3월 31일", sub: [46], kind: "대본"},
  kospiLow: {v: 5052, sub: [46], kind: "대본", note: "5,052.46 (3월 최저 종가, 3/4 5,093.54보다 낮음)"},
  rebound30: {v: 30, sub: [47], kind: "대본", note: "%, '한 달도 안 돼 30% 넘게' (4/27 6,615.03, +30.9%)"},

  // ── 문제 04 (문장 50–57) ──
  morningstar: {v: "모닝스타", sub: [51], kind: "대본", note: "미국 펀드 평가사, Mind the Gap 2025"},
  msTo: {v: 2024, sub: [51], kind: "대본"},
  msYears: {v: 10, sub: [51], kind: "대본"},
  fundRet: {v: 8.2, sub: [52], kind: "대본", note: "%/년, 펀드 자체"},
  investorRet: {v: 7.0, sub: [52], kind: "대본", note: "%/년, 투자자가 실제로 번 돈"},
  gapPt: {v: 1.2, sub: [53], kind: "대본", note: "%포인트 = 8.2 - 7.0"},
  gapShare: {v: 15, sub: [53], kind: "대본", note: "%, 전체 수익의 15% 정도"},
  gfcYear: {v: "2008년", sub: [55, 60], kind: "대본", note: "금융위기"},
  gfcDrop: {v: "절반 넘게", sub: [55], kind: "대본", note: "1년 만에 (2007-10-31 2,064.85 → 2008-10-24 938.75, -54.5%)"},
  gfcRecover: {v: "3년 넘게", sub: [56], kind: "대본", note: "이전 고점 회복 2011-01-03 2,070.08 (3년 2개월)"},

  // ── 방법 (문장 59–88) ──
  spendYears: {v: "1~2년", sub: [59], kind: "대본"},
  spend: {v: 1000, sub: [62], kind: "예시", note: "만 원, 1년 안에 쓸 돈"},
  stockOnly: {v: 3000, sub: [63], kind: "예시", note: "만 원 = 4,000 - 1,000"},
  delayDay: {v: "3월 5일", sub: [66], kind: "대본"},
  delayLoss: {v: -460, sub: [66], kind: "대본", note: "만 원 = 4,000 × (191,600 ÷ 216,500 - 1)"},
  halfish: {v: "절반 가까이", sub: [67], kind: "대본", note: "-460은 -818보다 44% 작음"},
  sellThird: {v: "1/3", sub: [69, 70], kind: "예시", note: "'3분의 1'"},
  checkDay: {v: "4월 23일", sub: [70, 76], kind: "대본"},
  partialPnl: {v: -170, sub: [70], kind: "대본", note: "만 원 '정도' (README 검산 -174: 판 1/3 1,061 + 남은 2/3 2,765 = 3,826)"},
  partialBetter: {v: 650, sub: [71], kind: "대본", note: "만 원 '가까이' (818 - 174 = 644)"},
  rebuyWeeks: {v: 4, sub: [74], kind: "예시", note: "4주 동안 매주 금요일 4분의 1씩"},
  rebuyDays: {v: "3월 6일 · 13일 · 20일 · 27일", sub: [74], kind: "계산", note: "3/4 뒤 4주 동안의 금요일 (README: 188,200 · 183,500 · 199,400 · 180,100원)"},
  rebuyFrac: {v: "1/4", sub: [74], kind: "예시", note: "'4분의 1씩'"},
  rebuyAvg: {v: "18만 8천 원", sub: [75], kind: "대본", note: "'정도' (평균 187,524원)"},
  rebuyPnl: {v: -190, sub: [76], kind: "대본", note: "만 원 '정도' (README 검산 -191)"},
  rebuyBetter: {v: 600, sub: [77], kind: "대본", note: "만 원 '넘게' (818 - 191 = 627)"},
  // 자본시장연구원 (김민기·김준석, 이슈보고서 21-11 「코로나19 국면의 개인투자자: 투자행태와 투자성과」, 2021-06-14)
  kcmi: {v: "자본시장연구원", sub: [80], kind: "대본"},
  kcmiYear: {v: "2021년", sub: [80], kind: "대본", note: "발표 2021-06-14"},
  kcmiPeriod: {v: "2020년 3월 코로나 폭락 → 10월", sub: [81], kind: "대본", note: "2020년 3~10월 거래내역 (8개월)"},
  kcmiInvestors: {v: "20만 명", sub: [81], kind: "대본", note: "4개 대형 증권사 개인투자자 204,004명 (신규 60,446명, 약 30%)"},
  tradeTwice: {v: "두 배 가까이", sub: [82], kind: "대본", note: "신규 투자자의 거래회전율이 기존 투자자의 '두 배 가까이' (보고서 p.12)"},
  turnoverOld: {v: 6.5, sub: [82], kind: "출처", note: "%, 기존 투자자 일간 거래회전율 (세미나 수치, 서울신문 2021-04-13). 막대 길이 비율에만 사용(숫자 표시 안 함)"},
  turnoverNew: {v: 12.2, sub: [82], kind: "출처", note: "%, 신규 투자자 일간 거래회전율 (12.2 ÷ 6.5 = 1.88배). 막대 길이 비율에만 사용(숫자 표시 안 함)"},
  retOld: {v: 15, sub: [83], kind: "대본", note: "%, 기존 투자자 거래세·수수료 뺀 수익률 15.0% (차감 전 18.8%, 2020년 3~10월)"},
  retNew: {v: -1.2, sub: [83], kind: "대본", note: "%, 신규 투자자 거래세·수수료 뺀 수익률 (차감 전 5.9%)"},
  // 문장 84 '자주 사고판 투자자일수록 시장보다 덜 벎' = 기존·신규 각 집단 안에서 회전율이 높을수록 초과수익률이 낮음 (p.16). -1.2%의 원인을 잦은 매매 하나로 그리지 않는다
  // 문장 85는 진행자 해석 (숫자 없음)
  lastFri: {v: "매달 마지막 금요일", sub: [86], kind: "예시"},
  check1Day: {v: "3월 27일", sub: [87], kind: "대본", note: "3월 마지막 금요일"},
  check1: {v: -670, sub: [87], kind: "대본", note: "만 원 (4,000 × (180,100 ÷ 216,500 - 1) = -672)"},
  check2Day: {v: "4월 24일", sub: [87], kind: "대본", note: "4월 마지막 금요일"},
  check2: {v: 55, sub: [87], kind: "대본", note: "만 원 (219,500원 → +55)"},
} as const satisfies Record<string, Fact>;

/** 실제 종가 (README 검산표) — 선 차트의 꺾임·막대 비율에만 쓰고, 화면에 숫자로 표시하지 않는다 */
export const PRICE = {
  // 삼성전자 (원)
  buy: 216500, // 2026-02-27 산 날
  d0303: 195100,
  sold: 172200, // 2026-03-04 판 날
  d0305: 191600,
  d0423: 224500,
  rebuy: [188200, 183500, 199400, 180100], // 3/6 · 3/13 · 3/20 · 3/27 (금)
  // 코스피 (지수)
  k0304: 5093.54,
  k0305: 5583.9,
  k0331: 5052.46,
  k0427: 6615.03,
  // 코스피 2008 금융위기
  k2007peak: 2064.85, // 2007-10-31
  k2008low: 938.75, // 2008-10-24
  k2011back: 2070.08, // 2011-01-03
  // 하루 등락률 (%) — 막대 길이
  kDrop0304: -12.06,
  kRise0305: 9.63,
  kDrop2020: -8.39,
  kRise2020: 7.44,
  // JP모건 ($10,000 기준)
  jpmAll: 80619,
  jpmMiss: 35866,
} as const;

/** 화면에 쓰는 고정 문구 */
export const RECON = "실제 주가 흐름을 바탕으로 재구성한 사연";
