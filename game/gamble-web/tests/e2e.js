// VERSION: v0.8.0-web.1 — 2026-11-27 — 브라우저(Playwright Chromium)에서 실제로 한 매치를 눌러 보며 확인 + 화면 찍기
// 실행: node game/gamble-web/tests/e2e.js [화면 저장 폴더]
// 확인: 페이지 오류 0 · 준비 → 왕(내 테이블) → 상대 테이블(불빛) → 판단 → 결과 → … → 매치 끝까지 · 엿보기 게이지·'!' · 협력자 부르기(누르고 있기)
"use strict";
const { chromium } = require("playwright");
const path = require("path");
const fs = require("fs");

(async () => {
  const outDir = process.argv[2] || path.join(__dirname, "shots");
  fs.mkdirSync(outDir, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1312, height: 824 }, deviceScaleFactor: 1 });
  const errors = [], seen = {};
  page.on("pageerror", (e) => errors.push("pageerror: " + e.message));
  page.on("console", (m) => { if (m.type() === "error") errors.push("console: " + m.text()); });
  await page.goto("file://" + path.resolve(__dirname, "..", "index.html"));
  await page.waitForFunction(() => window.__gm && window.__gm.game);
  await page.waitForTimeout(1200); // 글꼴
  const shot = async (name) => { await page.screenshot({ path: path.join(outDir, name + ".png") }); console.log(`[E2E] shot=${name}`); };
  const st = () => page.evaluate(() => {
    const g = window.__gm.game;
    return { phase: g.phase, king: g.king, slave: g.slave, actor: g.actor(), committed: g.committed.slice(), hand: g.hands[0].slice(),
      objects0: g.objects[0].slice(), objects1: g.objects[1].slice(), marks: g.marks.slice(), over: g.is_over(), result: !document.getElementById("result").hidden,
      view: window.__gm.view.mode, scores: g.scores.slice(), strikes: g.strikes.slice(), round: g.round_index, calling: g.calling[0],
      connected: g.acc_connected[0], suspect0: g.acc_suspect[0], info: g.info_done, gaze1: g.gaze[1] };
  });
  const toPage = async (x, y) => {
    const r = await page.evaluate(() => { const b = document.getElementById("stage").getBoundingClientRect(); return [b.left, b.top, b.width / 1280]; });
    return [r[0] + x * r[2], r[1] + y * r[2]];
  };
  const clickStage = async (x, y) => { const [px, py] = await toPage(x, y); await page.mouse.move(px, py); await page.mouse.click(px, py); };
  const moveStage = async (x, y) => { const [px, py] = await toPage(x, y); await page.mouse.move(px, py, { steps: 4 }); };
  const cardX = (i, n) => 640 + (i - (n - 1) / 2) * 106;
  const M_OBJ = [[430, 440], [640, 420], [850, 440]], T_OBJ = [[850, 600], [960, 610], [1070, 600]];
  const P = { IDLE: 0, KT: 1, ST: 2, JUDGE: 3, REVEALED: 4, OVER: 5 };

  await shot("01_setup");
  await page.click("#btn-start");
  await page.waitForTimeout(400);
  let s = await st();
  console.log(`[E2E] start phase=${s.phase} king=${s.king} view=${s.view} objects0=${s.objects0}`);
  // 1판: 내가 왕 — 내 테이블에서 카드 고르기
  await moveStage(640, 200); await page.waitForTimeout(300);
  await moveStage(cardX(0, s.hand.length), 728); await page.waitForTimeout(300);
  await shot("02_king_choose_mine");
  await clickStage(cardX(0, s.hand.length), 728);
  await page.waitForTimeout(1500);
  s = await st();
  console.log(`[E2E] after_commit phase=${s.phase} view=${s.view} gaze1=${s.gaze1}`);
  await moveStage(640, 190); // 상대 얼굴 보기 (주시)
  await page.waitForTimeout(1200);
  await shot("03_watch_ai_theirs");
  // '!' 가 뜨면 그 물건을 확인, 아니면 판단 시간에 Enter
  let inspected = false;
  for (let i = 0; i < 160; i++) {
    s = await st();
    if (s.result || s.over || s.phase === P.KT) break;
    const mi = s.marks.findIndex(Boolean);
    if (!inspected && mi >= 0 && (s.phase === P.ST || s.phase === P.JUDGE)) {
      await moveStage(T_OBJ[mi][0], T_OBJ[mi][1] - 10); await page.waitForTimeout(250);
      await shot("04_mark_hover_inspect");
      await clickStage(T_OBJ[mi][0], T_OBJ[mi][1] - 10); inspected = true; await page.waitForTimeout(400);
      await shot("05_after_inspect");
    }
    if (s.phase === P.JUDGE) { await page.keyboard.press("Enter"); }
    await page.waitForTimeout(150);
  }
  s = await st();
  if (s.result) { await shot("06_result"); }
  // 나머지는 4배속으로 끝까지
  await page.evaluate(() => window.__gm.setSpeed(4));
  let peekShot = false, callShot = false, mineSlaveShot = false, steps = 0;
  const t0 = Date.now();
  while (Date.now() - t0 < 240000) {
    s = await st();
    if (s.over) break;
    steps++;
    if (s.result) { await page.click("#btn-result"); await page.waitForTimeout(150); continue; }
    const myTurn = (s.phase === P.KT || s.phase === P.ST) && s.actor === 0 && s.committed[0] === -1;
    if (s.phase === P.KT && s.slave === 0 && !callShot && !s.connected) {
      // 상대(왕)가 고르는 중 — 협력자 부르기 버튼을 누르고 있기
      const box = await page.locator("#act-call").boundingBox();
      if (box && !(await page.locator("#act-call").isDisabled())) {
        await page.mouse.move(box.x + box.width / 2, box.y + box.height / 2);
        await page.mouse.down(); await page.waitForTimeout(350);
        await shot("08_calling_hold"); await page.waitForTimeout(500); await page.mouse.up();
        callShot = true; await page.waitForTimeout(200);
        s = await st(); console.log(`[E2E] call connected=${s.connected} suspect=${s.suspect0.toFixed(2)}`);
        continue;
      }
    }
    if (myTurn && s.phase === P.ST && !peekShot) {
      const mi = s.objects0.findIndex((k) => k === "lighter" || k === "cigcase");
      if (mi >= 0) {
        if (!mineSlaveShot) { await moveStage(640, 600); await page.waitForTimeout(100); await shot("07_slave_mine"); mineSlaveShot = true; }
        await moveStage(M_OBJ[mi][0], M_OBJ[mi][1] - 10); await page.waitForTimeout(200);
        await shot("09_peek_gauge"); await page.waitForTimeout(500);
        await shot("10_peek_done"); peekShot = true;
        s = await st(); console.log(`[E2E] peek info=${s.info}`);
      }
    }
    if (myTurn) {
      s = await st();
      if ((s.phase === P.KT || s.phase === P.ST) && s.actor === 0 && s.committed[0] === -1) { await clickStage(cardX(0, s.hand.length), 728); }
      await page.waitForTimeout(150); continue;
    }
    if (s.phase === P.JUDGE && s.king === 0) { await page.keyboard.press("Enter"); }
    await page.waitForTimeout(120);
  }
  s = await st();
  await page.waitForTimeout(300);
  await shot("11_match_over");
  const evc = await page.evaluate(() => { const c = {}; for (const e of window.__gm.game.events) c[e.type] = (c[e.type] || 0) + 1; return c; });
  console.log(`[E2E] over=${s.over} rounds=${s.round + 1} scores=${s.scores} strikes=${s.strikes} steps=${steps} secs=${((Date.now() - t0) / 1000).toFixed(1)}`);
  console.log(`[E2E] events=${JSON.stringify(evc)}`);
  console.log(`[E2E] errors=${errors.length}`); for (const e of errors) console.log("  " + e);
  // 폰 너비에서 가로 스크롤 없는지
  await page.setViewportSize({ width: 400, height: 800 });
  await page.waitForTimeout(300);
  const overflow = await page.evaluate(() => document.documentElement.scrollWidth > window.innerWidth);
  await shot("12_phone_width");
  console.log(`[E2E] phone_horizontal_overflow=${overflow}`);
  await browser.close();
  process.exit(errors.length === 0 && s.over && !overflow ? 0 : 1);
})();
