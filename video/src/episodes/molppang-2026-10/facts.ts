// 데이터 시트 — guides/video_guide.md 4번. 화면 숫자는 여기 값만 쓴다.
// 구분: 대본 = SRT에 나온 값 / 계산 = 대본 숫자로 계산한 값(식 포함) / 예시 = 대본의 예시 규칙
//       출처 = 대본 문장의 근거 자료(README·stock/guides/script_rules.md 7번 몰빵 줄)에만 있는 값 — 막대 길이·칸 비율에만 쓰고 화면에 숫자로 표시하지 않는다
// 검산·출처: stock/source/molppang-2026-10/README.md (문장 40–47·51), stock/guides/script_rules.md 7번 (몽고디비·대형주 급락·애널리스트·비스트라·15%·버핏)
// 번호는 대본 문장 번호 (v2.1, 문장 91)
// ※ 투자 교육용. 특정 종목의 매수·매도 권유가 아님.

export type Kind = "대본" | "계산" | "예시" | "출처";
export type Fact = {v: number | string; sub: number[]; kind: Kind; note?: string};

export const F = {
  // ── 사연 (재구성, 문장 1–11) ──
  aiStock: {v: "AI 관련 주식", sub: [1], kind: "대본"},
  company: {v: "몽고디비", sub: [1, 3, 8], kind: "대본", note: "티커 MDB (화면에는 이름만)"},
  outlook: {v: "투자 전망", sub: [2], kind: "대본"},
  earnings: {v: "실적", sub: [2], kind: "대본"},
  trend: {v: "주가 상승세", sub: [2], kind: "대본"},
  all: {v: 7000, sub: [3, 36, 59, 60], kind: "대본", note: "만 원, '전 재산 7천만 원' (script_rules 7번: 약 $414에 매수)"},
  allIn: {v: "몰빵", sub: [3], kind: "대본"},
  gain: {v: 1000, sub: [4], kind: "대본", note: "만 원 '정도' (script_rules 7번 검산: 고점 $473.10 → +1천만 원)"},
  prevHigh: {v: "전고점", sub: [5], kind: "대본"},
  loss: {v: -2000, sub: [7, 61], kind: "대본", note: "만 원 (script_rules 7번 검산: 장중 저점 약 -1,930만 원)"},
  lossPct: {v: -28.6, sub: [7], kind: "계산", note: "%, -2,000 ÷ 7,000. 화면 표시 안 함 (문장 61 '약 200만 원' 검산용)"},
  ceo: {v: "CEO, 다른 회사로 이적", sub: [8], kind: "대본", note: "2026-09-28 발표 (날짜·옮겨 간 회사는 대본에 없어 화면에 쓰지 않음)"},
  maxDrop: {v: -26, sub: [9], kind: "대본", note: "%, '최대 -26%' (직전 종가 $410.44 → 장중 저점 약 $300)"},
  cash0: {v: 0, sub: [10, 30, 31, 78], kind: "계산", note: "현금 0원 = 7,000 - 7,000 (전 재산을 한 종목에)"},

  // ── 진행자 (문장 12–18) ──
  // 문장 13–15 생각 말풍선은 대본 문장의 핵심 구절 (숫자 없음)

  // ── 문제 01 (문장 19–33) ──
  meta: {v: "메타", sub: [23, 24, 29], kind: "대본"},
  google: {v: "구글", sub: [23, 25], kind: "대본"},
  nvidia: {v: "엔비디아", sub: [23, 26, 66], kind: "대본"},
  metaYear: {v: "2022년", sub: [24], kind: "대본"},
  metaWhy: {v: "실적 실망", sub: [24], kind: "대본"},
  metaDrop: {v: -26, sub: [24], kind: "대본", note: "%, 하루 (2022-02-03 -26.4%)"},
  googleYear: {v: "2023년", sub: [25], kind: "대본"},
  googleWhy: {v: "AI 챗봇 광고 속 오답", sub: [25], kind: "대본"},
  googleDrop: {v: -9, sub: [25], kind: "대본", note: "%, 장중 (2023-02-08, 종가 -8%)"},
  nvidiaYear: {v: "2025년", sub: [26], kind: "대본"},
  nvidiaWhy: {v: "딥시크 등장", sub: [26, 66], kind: "대본", note: "중국 AI 기업"},
  nvidiaDrop: {v: -17, sub: [26, 66], kind: "대본", note: "%, 하루 (2025-01-27)"},
  record: {v: "미국 증시 역사상 하루 최대 시가총액 손실", sub: [27], kind: "대본", note: "약 5,890억 달러 (대본에 금액이 없어 화면에 쓰지 않음)"},
  analysts: {v: 2, sub: [29], kind: "대본", note: "명, 메타 폭락 직전 매도 의견 (블룸버그 2022-02-11)"},

  // ── 문제 02 (문장 34–38) ──
  after: {v: 5000, sub: [36], kind: "대본", note: "만 원, '7천만 원이 5천만 원이 되면'"},
  need40: {v: 40, sub: [36], kind: "대본", note: "%, 7,000 ÷ 5,000 - 1 = 40%"},
  drop29: {v: -29, sub: [36], kind: "계산", note: "%, 5,000 ÷ 7,000 - 1 = -28.6% (막대 길이만, 화면에는 금액으로)"},
  half: {v: -50, sub: [37], kind: "계산", note: "%, '반토막'"},
  need100: {v: 100, sub: [37], kind: "계산", note: "%, 1 ÷ 0.5 - 1 = 100% = '두 배'"},
  drop70: {v: -70, sub: [37], kind: "대본", note: "%, '70% 빠지면'"},
  need233: {v: 233, sub: [37], kind: "계산", note: "%, 1 ÷ 0.3 - 1 = 233% (= 3.3배, '세 배 넘게'). script_rules 7번 손실 회복 수학"},

  // ── 문제 03 (문장 39–48) ──
  kcmi: {v: "자본시장연구원", sub: [40], kind: "대본", note: "이상호·강소현·김민기, 이슈보고서 24-31 (2024-12-19) p.12"},
  kcmiPeriod: {v: "2023년 말까지 10년", sub: [40], kind: "대본"},
  kcmiScope: {v: "국내 상장사", sub: [40], kind: "대본", note: "국내 비금융 상장사, 주주 총수익률(배당 포함)"},
  under52: {v: 52, sub: [41], kind: "대본", note: "%, 10년 누적 주식수익률 < 무위험수익률(통안채 364일물)"},
  bond: {v: "1년짜리 안전한 채권", sub: [41], kind: "대본", note: "통안채 364일물"},
  large: {v: "시가총액 상위 30% 대형주", sub: [42], kind: "대본"},
  under58: {v: 58, sub: [42], kind: "대본", note: "%"},
  kospiYear: {v: "2026년", sub: [43], kind: "대본"},
  kospiTo: {v: "6월까지", sub: [43], kind: "대본", note: "2025-12-30 4,214.17 → 2026-06-22 고점 9,114.55"},
  kospiTwice: {v: "두 배 넘게", sub: [43], kind: "대본", note: "+116.28%"},
  beat4: {v: 4, sub: [43, 44], kind: "대본", note: "%, '4%도 안 됐죠' (한국경제 2026-07-28: 2,626개 중 94개 = 3.58%)"},
  beatShare: {v: 3.58, sub: [43], kind: "출처", note: "%, 94 ÷ 2,626. 와플 칸 채움 비율에만 사용(숫자 표시 안 함) — 4번째 칸을 0.58만 채워 '4% 미만'을 그림"},
  nc: {v: "엔씨소프트", sub: [45], kind: "대본"},
  lgh: {v: "LG생활건강", sub: [45], kind: "대본"},
  highYear: {v: "2021년", sub: [45, 47], kind: "대본", note: "고점: 엔씨소프트 2021-02-08 · LG생활건강 2021-07-01 · 코스피 2021-07-06"},
  down70: {v: 70, sub: [45], kind: "대본", note: "%, '70% 넘게 빠져' (엔씨 -78.5%, LG생활건강 -85.0%)"},
  ncRatio: {v: 0.215, sub: [45], kind: "출처", note: "223,000 ÷ 1,038,000 (2026-10-08). 막대 길이에만 사용"},
  lghRatio: {v: 0.15, sub: [45], kind: "출처", note: "266,000 ÷ 1,770,000 (2026-10-08). 막대 길이에만 사용"},
  years5: {v: "5년 넘게", sub: [46], kind: "대본", note: "2021-02·07 → 2026-10"},
  kospiDouble: {v: "두 배 수준", sub: [47], kind: "대본", note: "3,305.21 → 6,625.93"},
  kospiRatio: {v: 2.005, sub: [47], kind: "출처", note: "6,625.93 ÷ 3,305.21. 막대 길이에만 사용"},

  // ── 문제 04 (문장 49–55) ──
  lossX2: {v: "두 배 정도", sub: [51], kind: "대본", note: "손실 회피 계수 평균 1.955 (Brown·Imai·Vieider·Camerer 2024 메타분석). 대본에 연구자 이름이 없어 출처 캡션 없음"},
  manyTimes: {v: "수십 번", sub: [53], kind: "대본"},
  usMarket: {v: "미국 장", sub: [53], kind: "대본"},

  // ── 방법 (문장 56–85) ──
  five: {v: 5, sub: [57], kind: "대본", note: "다섯 가지"},
  cap: {v: 15, sub: [59, 84], kind: "예시", note: "%, '예를 들어 상한이 15%면' (CNN Money 2001 '15% 이상 넣지 말라')"},
  capAmt: {v: 1050, sub: [59], kind: "대본", note: "만 원 = 7,000 × 15%"},
  n10: {v: 10, sub: [60], kind: "대본", note: "10개 종목"},
  each: {v: 700, sub: [60, 76, 82], kind: "대본", note: "만 원 = 7,000 ÷ 10"},
  splitLoss: {v: -200, sub: [61], kind: "대본", note: "만 원 '약' = 700 × (2,000 ÷ 7,000)"},
  splitPct: {v: 3, sub: [61], kind: "대본", note: "% '정도' = 200 ÷ 7,000 = 2.9%"},
  aiChip: {v: "AI 반도체", sub: [65, 66], kind: "대본"},
  aiSoft: {v: "AI 소프트웨어", sub: [65], kind: "대본"},
  aiPower: {v: "AI 전력주", sub: [65, 67], kind: "대본"},
  broadcom: {v: "브로드컴", sub: [66], kind: "대본"},
  vistra: {v: "비스트라", sub: [67], kind: "대본"},
  vistraDrop: {v: -28, sub: [67], kind: "대본", note: "%, '28%나' (로이터: -28.3%)"},
  sectors: {v: "반도체 · 헬스케어 · 소비재 · 금융", sub: [68], kind: "대본"},
  sp500: {v: "S&P 500", sub: [71, 73], kind: "대본"},
  n500: {v: 500, sub: [71], kind: "대본", note: "미국 대표 기업 500곳"},
  buffett: {v: "워런 버핏", sub: [73], kind: "대본", note: "버크셔 해서웨이 2013 주주 서한 (연도는 대본에 없어 화면에 쓰지 않음)"},
  buffett90: {v: 90, sub: [73], kind: "대본", note: "%, 아내에게 남길 돈의 90% → S&P 500 지수 펀드 (나머지 10% 단기 국채는 대본에 없어 이름을 쓰지 않음)"},
  halfEtf: {v: "절반", sub: [74], kind: "예시"},
  thirds: {v: 3, sub: [76], kind: "예시", note: "세 번에 나눠 삼"},
  doubleUp: {v: "두 배", sub: [82], kind: "대본"},
  w10: {v: 10, sub: [82], kind: "대본", note: "% = 700 ÷ 7,000"},
  w18: {v: 18, sub: [82], kind: "대본", note: "% '정도' = 1,400 ÷ (7,000 - 700 + 1,400) = 18.2%"},
} as const satisfies Record<string, Fact>;

/** 실제 가격 비율 (script_rules 7번 몽고디비) — 선의 꺾임에만 쓰고 화면에 숫자로 표시하지 않는다 */
export const PRICE = {
  mdbHigh: 473.1, // 52주 고점 ($)
  mdbPrevClose: 410.44, // CEO 이적 발표 직전 종가
  mdbLow: 303.7, // 장중 저점 = 410.44 × (1 - 0.26)
} as const;

/** 화면에 쓰는 고정 문구 */
export const RECON = "실제 주가 흐름을 바탕으로 재구성한 사연";
