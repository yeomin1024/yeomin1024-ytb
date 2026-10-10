// 문장 번호 → 프레임. 장면 시간은 SRT 번호가 아니라 대본 문장 번호(TXT 줄 순서)로 계산한다 (guides/video_guide.md 2번)
// - 자막은 늘 한 줄. 긴 문장은 앞줄·뒷줄 자막 2개(parts)로 나뉜다 → 뒷줄 내용 그림은 b(n)에 맞춘다
// - SRT = 영상 시간: 자막을 코드에서 밀지 않는다. 고지 카드는 SRT 안의 공백(cards.start~end)에 들어간다
export type PartSrc = {start: number; end: number; text: string};
export type SentSrc = {n: number; start: number; end: number; parts: readonly PartSrc[]};
export type CardSrc = {afterSentence: number; title: string; lines: readonly string[]; start: number; end: number};
export type Src = {
  sentences: readonly SentSrc[];
  cards: readonly CardSrc[];
  audio: {file: string; seconds: number} | null;
  totalSeconds: number;
};

/** 화면 자막 한 개 (한 줄). n = 문장 번호, part = 0 앞줄 / 1 뒷줄 (나뉘지 않은 문장은 0) */
export type Sub = {n: number; part: number; from: number; to: number; text: string};
export type Card = {afterSentence: number; title: string; lines: readonly string[]; from: number; to: number};
export type Timeline = {
  subs: Sub[];
  cards: Card[];
  total: number;
  /** 문장 n 시작 프레임 */
  s: (n: number) => number;
  /** 문장 n 끝 프레임 */
  e: (n: number) => number;
  /** 문장 n 뒷줄 자막 시작 프레임 (나뉘지 않은 문장은 s(n)) */
  b: (n: number) => number;
  /** 문장 n이 앞줄·뒷줄로 나뉘었는지 */
  split: (n: number) => boolean;
};

export const makeTimeline = (src: Src, fps: number): Timeline => {
  const f = (sec: number) => Math.round(sec * fps);
  const subs: Sub[] = [];
  const byN = new Map<number, SentSrc>();
  for (const s of src.sentences) {
    byN.set(s.n, s);
    s.parts.forEach((p, i) => subs.push({n: s.n, part: i, from: f(p.start), to: f(p.end), text: p.text}));
  }
  const get = (n: number) => {
    const s = byN.get(n);
    if (!s) throw new Error(`문장 ${n} 없음`);
    return s;
  };
  const cards: Card[] = src.cards.map((c) => ({afterSentence: c.afterSentence, title: c.title, lines: c.lines, from: f(c.start), to: f(c.end)}));
  return {
    subs,
    cards,
    total: f(src.totalSeconds),
    s: (n) => f(get(n).start),
    e: (n) => f(get(n).end),
    b: (n) => {
      const s = get(n);
      return f(s.parts[s.parts.length - 1].start);
    },
    split: (n) => get(n).parts.length > 1,
  };
};

/** 장면 안 시간 (장면 시작 = 0)
 *  a(n)      = 문장 n 시작, a(n, 0.5) = 문장 n의 중간
 *  b(n)      = 문장 n 뒷줄 자막 시작, b(n, 0.5) = 뒷줄 자막의 중간 (나뉘지 않은 문장은 a와 같음)
 *  뒷줄에 나오는 말을 그리는 요소는 반드시 b()로 시간을 잡는다 (뒷줄 내용 동기화) */
export type ST = {a: (n: number, frac?: number) => number; b: (n: number, frac?: number) => number; dur: number};
export const sceneTime = (tl: Timeline, from: number, to: number): ST => ({
  dur: to - from,
  a: (n, frac = 0) => Math.round(tl.s(n) + (tl.e(n) - tl.s(n)) * frac) - from,
  b: (n, frac = 0) => Math.round(tl.b(n) + (tl.e(n) - tl.b(n)) * frac) - from,
});
