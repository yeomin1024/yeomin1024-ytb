# 개미 재기 일지 — 종이인형극 배경 5장 (ChatGPT 에 넘기는 파일)

이 파일 판: v1.0 — 2026-10-23 — 배경 5장 (사용자 지시 2026-10-23 "일단 1화만 영상 필요 소스 생성해봐" — 1화 장면 표가 쓰는 배경). 무대 규칙 `stock/story/series.md` 4번 · 그림체는 인형 파일 `stock/story/protagonist_chatgpt.md` v3.0 의 STYLE 문단과 같다.

## ChatGPT에게 — 이 파일을 읽으면 할 일
0. **이 주소를 지금 새로 열어 그 내용만 쓴다.** 답의 첫 줄에 위 '이 파일 판' 줄을 그대로 적는다.
1. 아래 5장을 **1번부터 차례로 모두** 만든다. 질문하지 말고 바로 만든다. 이미지 한도로 멈추면 사용자가 `계속`이라고 보낸다 → 아직 안 만든 번호부터 이어서.
2. 프롬프트(``` 안)를 **한 글자도 바꾸지 않고 그대로** 쓰고, 맨 앞에 아래 **STYLE**·**BACKDROP** 두 문단을 그대로 붙인다.
3. **사람·인형·동물을 그리지 않는다** (빈 무대만 — 인형은 따로 있는 투명 그림을 코드가 올린다). 글자·숫자·로고도 없다 — 전광판·모니터·화이트보드는 빈 면.
4. **가로 3:2 (1536×1024)**. 바닥 줄은 높이 약 80% — 아래 1/5 은 아무것도 없는 바닥. 오른쪽 절반과 왼쪽 아래 바닥은 단순하게 (인형이 왼쪽에 서고, 숫자 화면이 오른쪽에 뜬다).
5. 그림 바로 위에 번호와 저장 경로를 한 줄 적는다 (예: `1. stock/story/puppet/P-HOME-NIGHT.jpg`). 그림 안에는 쓰지 않는다.
6. **다 만들면 저장소에 넣는다 — 저장 경로 그대로.**
   - 저장소 `yeomin1024/yeomin1024-ytb` main 브랜치, `stock/story/puppet/` 폴더, 파일 이름은 표 그대로 (대소문자·하이픈까지).
   - **JPEG(.jpg) 700KB 이하**로 저장해 올린다 (GitHub 앱은 약 768KB 를 넘는 파일을 잘라 올려 그림이 깨진다). 올린 뒤 GitHub 의 파일 크기(바이트)가 내 파일과 같은지 확인하고, 다르면 다시 올린다. 아래 코드 그대로:
   ```python
   from PIL import Image
   import os
   def save_jpg(src, dst, limit=700_000):
       im = Image.open(src).convert("RGB")
       w, h = im.size
       s, q = min(1.0, 1600 / max(w, h)), 90
       while True:
           cur = im.resize((round(w * s), round(h * s)), Image.LANCZOS) if s < 1 else im
           cur.save(dst, "JPEG", quality=q, optimize=True, progressive=True)
           if os.path.getsize(dst) <= limit or q <= 60:
               break
           q -= 6
       print(dst, os.path.getsize(dst), cur.size)
   ```
   - **GitHub 앱으로 커밋한다.** 커밋 메시지: `[주인공] puppet <파일 이름> 배경` (예: `[주인공] puppet P-HOME-NIGHT.jpg 배경`). 올린 뒤 파일 경로와 커밋 링크를 목록으로 적는다.
   - **올리기가 실패하면** (권한·연결 오류) 묻지 말고: 그림을 한 번 더 보여 주고, 이 문장을 그대로 쓴다 — **"이 그림을 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 저장 경로에 올립니다."** 직접 올리는 길: 그림을 표의 파일 이름으로 내려받아 https://github.com/yeomin1024/yeomin1024-ytb/upload/main/stock/story/puppet 에 끌어다 놓고 Commit changes.

## 공통 문단 (프롬프트 맨 앞에 그대로 붙임 — 5장 모두)

```
STYLE: paper-cut puppet theater (layered papercraft), like a hand-made paper puppet show. Everything is made of flat layered colored paper with a visible fine paper-fiber texture and clean, slightly irregular hand-cut edges; small soft shadows only between stacked paper layers; no outlines, no airbrush gradients, no photorealism. Limited calm palette: deep indigo #1E2A4A, warm cream #F2E6CF, charcoal #2B2B2B, gold ochre #D9A441, muted crimson #B3202A, soft teal #3E8E87, plus the character colors below. Flat stage view, like a stage seen from the audience. People are paper puppets WITH clearly readable facial expressions: every face is built from small cut-paper pieces — almond-shaped dark eyes with a tiny white highlight, thin dark-brown paper eyebrows, a simple mouth cut from darker paper, and soft pink paper cheek circles. The expression must read at a glance even when the picture is small. Fictional people, not recognizable as any real person. Modern everyday Korean life today. No text, letters, numbers, logos or watermarks anywhere.
```

```
BACKDROP: a single flat paper-theater stage backdrop seen straight from the audience, wide landscape. NO people, NO animals, NO puppets — an empty stage set only. The stage floor line is at about 80% of the image height: the bottom fifth is one plain, calm floor surface (wooden stage boards or ground) with nothing standing on it. Keep the lower-left and center floor area and the right half of the picture simple and uncluttered (a paper puppet will stand on the left, and number screens will be placed over the right half later). Main scenery stays in the upper three quarters. Soft even light, no strong spotlight, no frame or curtain edges. No text, letters, numbers, signs with writing, logos or watermarks anywhere — every screen, board and sign is completely blank.
```

## 5장

| 번호 | 저장 경로 | 무엇 |
|---|---|---|
| 1 | `stock/story/puppet/P-HOME-NIGHT.jpg` | 거실, 밤 — 1~4화 (기본 무대) |
| 2 | `stock/story/puppet/P-OFFICE.jpg` | 생산관리 사무실, 낮 — 회사 장면 |
| 3 | `stock/story/puppet/P-STREET-DAWN.jpg` | 아파트 단지 버스 정류장, 새벽 — 다짐·마무리 |
| 4 | `stock/story/puppet/P-BOARD.jpg` | 증권가 거리의 큰 전광판, 밤 — 시장 이야기 |
| 5 | `stock/story/puppet/P-PAPER.jpg` | 빈 종이 무대 — 숫자·차트·정리 카드 바탕 |

## 1. P-HOME-NIGHT — 거실, 밤 — 1~4화 (기본 무대)

저장 경로: `stock/story/puppet/P-HOME-NIGHT.jpg` (JPEG 700KB 이하)

```
SCENE: A small Korean apartment living room at night: a low fabric sofa, a small low wooden table, a standing lamp giving a warm glow, and a wide window showing distant apartment-building lights in deep indigo. Calm, slightly lonely mood. Palette mostly deep indigo #1E2A4A with warm cream lamp light.
```

## 2. P-OFFICE — 생산관리 사무실, 낮 — 회사 장면

저장 경로: `stock/story/puppet/P-OFFICE.jpg` (JPEG 700KB 이하)

```
SCENE: A small production-control office in an auto-parts factory by day: two simple desks with blank dark monitors, a filing shelf, a whiteboard that is completely blank, and a window showing grey factory roofs and a chimney. Neutral daylight, muted teal and cream tones.
```

## 3. P-STREET-DAWN — 아파트 단지 버스 정류장, 새벽 — 다짐·마무리

저장 경로: `stock/story/puppet/P-STREET-DAWN.jpg` (JPEG 700KB 이하)

```
SCENE: An apartment-complex bus stop at dawn: a simple bus shelter with an empty bench, one streetlight still on, apartment buildings in the background, and a soft sky turning from blue to gold near the horizon. Quiet, hopeful mood.
```

## 4. P-BOARD — 증권가 거리의 큰 전광판, 밤 — 시장 이야기

저장 경로: `stock/story/puppet/P-BOARD.jpg` (JPEG 700KB 이하)

```
SCENE: A financial-district street at night with one huge electronic billboard on a building wall. The billboard face is a completely blank, plain dark navy panel with a thin gold border — no charts, no numbers, no letters. A few dark office buildings and street lamps around it. Cool navy tones with small warm window lights.
```

## 5. P-PAPER — 빈 종이 무대 — 숫자·차트·정리 카드 바탕

저장 경로: `stock/story/puppet/P-PAPER.jpg` (JPEG 700KB 이하)

```
SCENE: A plain warm cream paper backdrop #F2E6CF filling the whole picture, with a fine visible paper-fiber texture, a few very subtle torn-paper layers at the edges, and a soft darker vignette in the corners. Nothing else — no objects, no shapes in the middle.
```

## 변경 이력

| 판 | 날짜 | 바꾼 것 |
|---|---|---|
| v1.0 | 2026-10-23 | 처음 만듦 — 배경 5장 (series.md 4번 표) |
