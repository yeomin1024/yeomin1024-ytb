// 데이터 시트 — guides/video_guide.md 4번. 화면 숫자는 여기 값만 쓴다.
// 구분: 대본 = SRT에 나온 값 / 계산 = 대본 숫자로 계산한 값(식 포함) / 예시 = 대본의 예시 규칙
// 검산·출처: stock/source/multagi-2026-10/README.md
// ※ 투자 교육용. 특정 종목의 매수·매도 권유가 아님.

export type Kind = "대본" | "계산" | "예시";
export type Fact = {v: number | string; sub: number[]; kind: Kind; note?: string};

export const F = {
  // ── 사연 (재구성) ──
  storyMonth: {v: "2025년 4월", sub: [1], kind: "대본"},
  company: {v: "유나이티드헬스", sub: [1, 32], kind: "대본"},
  drop1: {v: 22, sub: [1, 32], kind: "대본", note: "%, '22% 넘게' (실제 -22.38%, 4/17)"},
  biggest: {v: "미국 최대 건강보험사", sub: [2], kind: "대본"},
  saved: {v: 8000, sub: [4], kind: "대본", note: "만 원, 모아 둔 8천만 원"},
  first: {v: 5000, sub: [4, 27, 87], kind: "대본", note: "만 원, 처음 산 금액"},
  pnlStart: {v: 0, sub: [4], kind: "계산", note: "산 직후 평가손익 0원"},
  week: {v: "일주일 만에", sub: [5], kind: "대본"},
  pnlWeek: {v: -200, sub: [5], kind: "대본", note: "만 원"},
  add1: {v: 1500, sub: [6], kind: "대본", note: "만 원, 물타기 ①"},
  add2: {v: 1500, sub: [7], kind: "계산", note: "남은 돈 = 8,000 - 5,000 - 1,500 = 1,500 (자막 7 '남은 1,500만 원')"},
  crashDay: {v: "5월 14일 아침", sub: [10], kind: "대본"},
  pnlCrash: {v: -2000, sub: [10, 79], kind: "대본", note: "만 원"},
  drop2: {v: 18, sub: [12, 33], kind: "대본", note: "%, '18% 가까이' (실제 -17.79%, 5/13)"},
  added: {v: 3000, sub: [13, 25], kind: "대본", note: "만 원 = 1,500 + 1,500"},

  // ── 진행자 ──
  netBuy: {v: 4800, sub: [20], kind: "대본", note: "억 원, '4,800억 원 넘게', 2025년 5월 서학개미 순매수"},
  netBuyMonth: {v: "2025년 5월", sub: [20], kind: "대본"},
  rank: {v: 1, sub: [21], kind: "대본", note: "그달 가장 많이 사들인 종목"},

  // ── 문제 01 ──
  avgFrom: {v: 428, sub: [26, 75], kind: "대본", note: "달러, 처음 평단"},
  avgTo: {v: 415, sub: [26, 39], kind: "대본", note: "달러, 물타기 후 평단"},
  avgDrop: {v: 3, sub: [26], kind: "대본", note: "%, '3% 정도'"},
  investedTo: {v: 8000, sub: [27], kind: "대본", note: "만 원"},
  investedUp: {v: 60, sub: [27], kind: "대본", note: "%, (8,000-5,000)/5,000 = 60%"},
  extraLoss: {v: 600, sub: [28], kind: "대본", note: "만 원, '600만 원 넘게'"},
  noAvgLoss: {v: -1400, sub: [28], kind: "계산", note: "막대 길이만 사용(숫자 표시 안 함): -2,000 + 600 = -1,400 (대본 '넘게'라 실제는 -1,362)"},

  // ── 문제 02 ──
  d1: {v: "4월 17일", sub: [32], kind: "대본"},
  d2: {v: "5월 13일", sub: [33, 63], kind: "대본"},
  d3: {v: "5월 15일", sub: [34], kind: "계산", note: "5월 13일 + 이틀"},
  drop3: {v: 11, sub: [34], kind: "대본", note: "%, '11% 가까이' (실제 -10.93%)"},
  p585: {v: 585, sub: [37], kind: "대본", note: "달러"},
  p274: {v: 274, sub: [37], kind: "대본", note: "달러, 한 달 만에 절반 아래"},
  p376: {v: 376, sub: [38], kind: "대본", note: "달러, 2026년 10월"},
  now: {v: "2026년 10월", sub: [38], kind: "대본"},

  // ── 문제 03 (오딘 1998) ──
  odean: {v: "테런스 오딘", sub: [41], kind: "대본"},
  odeanOrg: {v: "미국 캘리포니아대", sub: [41], kind: "대본"},
  accounts: {v: "1만 개", sub: [41], kind: "대본"},
  odeanFrom: {v: 1987, sub: [42], kind: "대본"},
  odeanYears: {v: 7, sub: [42], kind: "대본"},
  sellRatio: {v: 1.5, sub: [43], kind: "대본", note: "배"},
  gap: {v: 3.4, sub: [45], kind: "대본", note: "%포인트, 그 뒤 1년"},

  // ── 문제 04 (베어링스) ──
  baringsYear: {v: 1995, sub: [49], kind: "대본"},
  baringsAge: {v: 233, sub: [50], kind: "대본", note: "년"},
  baringsFounded: {v: 1762, sub: [50], kind: "계산", note: "1995 - 233 = 1762 (설립 연도, README 출처와 일치)"},
  leesonAge: {v: 27, sub: [51], kind: "대본"},
  baringsLoss: {v: 82700, sub: [54], kind: "대본", note: "만 파운드 = 8억 2,700만 파운드 (fmt.eokMan으로 표시)"},
  soldFor: {v: "1파운드", sub: [54], kind: "대본"},

  // ── 방법 ──
  firstBuyDay: {v: "4월 23일", sub: [66], kind: "대본"},
  sixDays: {v: "엿새 뒤", sub: [66], kind: "대본"},
  lastAddDay: {v: "5월 9일", sub: [69, 76, 78], kind: "대본"},
  p381: {v: 381, sub: [69, 71], kind: "대본", note: "달러"},
  avg424: {v: 424, sub: [70], kind: "대본", note: "달러, 마지막 물타기 직전 평단"},
  stopPct: {v: 10, sub: [74], kind: "예시", note: "%"},
  stopPrice: {v: 385, sub: [75], kind: "대본", note: "달러 = 428 × 0.9 = 385.2"},
  stopLoss: {v: -500, sub: [77, 79], kind: "대본", note: "만 원 = 5,000 × -10%"},
  spxWhen: {v: "2025년 4월 초", sub: [83], kind: "대본"},
  spxDrop: {v: 19, sub: [84], kind: "대본", note: "%, '19% 가까이', 2월 고점 대비"},
  spxBack: {v: "6월 말", sub: [85], kind: "대본", note: "사상 최고치"},
  limitFirst: {v: 5000, sub: [87], kind: "예시", note: "만 원"},
  limitAdd: {v: 1500, sub: [87], kind: "예시", note: "만 원, 한 번까지"},
} as const satisfies Record<string, Fact>;

/** 화면에 쓰는 고정 문구 */
export const RECON = "실제 주가 흐름을 바탕으로 재구성한 사연";
