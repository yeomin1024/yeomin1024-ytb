// 자막 번호 → 프레임. 초를 하드코딩하지 않고 SRT 자막 번호로 장면 시간을 계산한다 (guides/video_guide.md 2번)
export type SubSrc = {n: number; start: number; end: number; lines: readonly string[]};
export type CardSrc = {afterSub: number; title: string; lines: readonly string[]; seconds: number};
export type Src = {subtitles: readonly SubSrc[]; cards: readonly CardSrc[]; totalSeconds: number};

export type Sub = {n: number; from: number; to: number; lines: readonly string[]};
export type Card = CardSrc & {from: number; to: number};
export type Timeline = {subs: Sub[]; cards: Card[]; total: number; s: (n: number) => number; e: (n: number) => number};

export const makeTimeline = (src: Src, fps: number): Timeline => {
  const f = (sec: number) => Math.round(sec * fps);
  const subs: Sub[] = [];
  const cards: Card[] = [];
  let shift = 0;
  for (const s of src.subtitles) {
    subs.push({n: s.n, from: f(s.start) + shift, to: f(s.end) + shift, lines: s.lines});
    for (const c of src.cards.filter((c) => c.afterSub === s.n)) {
      const from = f(s.end) + shift;
      const len = f(c.seconds);
      cards.push({...c, from, to: from + len});
      shift += len;
    }
  }
  const total = f(src.totalSeconds);
  const byN = new Map(subs.map((s) => [s.n, s]));
  const get = (n: number) => {
    const s = byN.get(n);
    if (!s) throw new Error(`자막 ${n} 없음`);
    return s;
  };
  return {subs, cards, total, s: (n) => get(n).from, e: (n) => get(n).to};
};

/** 장면 안 시간: a(n) = 자막 n 시작 프레임(장면 기준), a(n, 0.5) = 자막 n의 중간 */
export type ST = {a: (n: number, frac?: number) => number; dur: number};
export const sceneTime = (tl: Timeline, from: number, to: number): ST => ({
  dur: to - from,
  a: (n, frac = 0) => Math.round(tl.s(n) + (tl.e(n) - tl.s(n)) * frac) - from,
});
