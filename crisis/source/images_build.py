# VERSION: v1.0 — 2026-11-14 — 위기 상황 네 편 그림 요청 파일(ChatGPT용) — 만스피 편과 같은 꼴(만화 배경판 + 3장 동작 원화 + 소품 + 썸네일 그림)
# CHANGELOG
# | 버전 | 날짜 | 바뀐 것 | 함수 |
# |---|---|---|---|
# | v1.0 | 2026-11-14 | 최초 — 네 편 67장 · 공통 블록은 심리 images_build.py v1.0 을 옮기고 위기 상황에 맞게 STYLE(바깥 하늘 띠 허용 · 위험은 차분히) · WATER(물속 3장) 더함 | 전체 |
"""위기 상황 네 편의 ChatGPT 그림 요청 파일 `crisis/source/<영상ID>/images_chatgpt.md` 를 만든다.

사용자 지시 2026-11-14 "만스피 영상처럼 영상 만들거니까 챗지피티한테 만들 이미지 생성 명령 알려줘 그리고 썸네일 이미지도".
꼴은 심리 네 편(`psychology/source/images_build.py` v1.0 — 주식 만스피·반등 편 요청 파일과 같은 말)을 그대로 따름:
  - 배경판(사람 없음 · 앞 가운데 빈 바닥) · 인물 기준 그림 · 동작 원화 3장(키 → 중간 → 키) · 소품 판 · 썸네일 그림
  - 숫자·카드·자막·문자 말풍선·썸네일 문구는 코드가 얹음 → 그림에는 글자 0
  - 그림체는 만스피 편과 같게, 인물은 편마다 새로 · 편마다 무대가 다름 (유튜브 반복 콘텐츠 정책)
위기 상황만의 규칙 (crisis/guides/channel.md 3번):
  - 실제 사고의 숨진 분·다친 분·피해자는 그리지 않는다 (사고는 빈 무대·소품·숫자로) · 위험은 차분히(연기·어두운 틈·깨진 얼음·창밖 불빛)
  - 실제 항공사·은행·앱의 이름·로고·색 조합을 닮게 그리지 않는다 · 사기범은 그리지 않는다 (아무도 악당으로 그리지 않음)
  - 위험에 빠진 아이(중학생 얼음 사고)는 그리지 않는다

쓰는 법:  python3 crisis/source/images_build.py            # 네 편 모두 다시 씀
          python3 crisis/source/images_build.py --check    # 쓰지 않고 장 수·경로만 출력
          python3 crisis/source/images_build.py --only <영상ID>
로그: [images_build] key=value · 연구·교육용 영상 소스 — 안전 수칙은 공식 지침(대본 폴더 checklist.md)으로 확인.
"""
import argparse
import logging
import pathlib
import sys

VERSION = "v1.0"
DATE = "2026-11-14"
ROOT = pathlib.Path(__file__).resolve().parents[2]
REPO = "yeomin1024/yeomin1024-ytb"
# 만스피 편 그림체 기준 (main 커밋 고정 주소 — 2026-11-14 확인: 6개 파일이 그 커밋에 있음)
REF_COMMIT = "a2bac49315919a0aca335688d499adb3a9a82176"
REF_BASE = f"https://raw.githubusercontent.com/{REPO}/{REF_COMMIT}/stock/source/manspi-jeonmang-2026-11"

log = logging.getLogger("images_build")

# ── 공통 블록 (심리 v1.0 = 반등 편 v1.0 과 같은 말 — 검증된 문장, 위기 상황에 맞게 STYLE 끝만 바꿈) ──
STYLE = (
    "STYLE: Match exactly the art style of the reference pictures (style only — do NOT draw the people in them): "
    "a polished flat 2D cartoon illustration with bold clean dark outlines, flat colors with one simple cel-shading tone "
    "and small highlights, warm cozy lighting mixed with cool blue screen or night glow, expressive faces (big eyes, clear "
    "eyebrows, open mouths) and easy-to-read body language for a small phone screen. Slightly chunky "
    "proportions (head about one quarter of the body height). Calm, clear and caring mood — this is a safety-education "
    "video: danger is shown clearly but calmly (gray smoke, a dark gap, broken ice and dark cold water, an orange glow of "
    "fire seen far away or through a window), never blood, injuries, dead or falling people, flames on anyone, or "
    "children in danger. Nobody is a monster or a villain. It is a 2D drawing — not a 3D render, not clay or plastic, not "
    "a photo. Absolutely no text, letters, numbers, logos or watermarks anywhere — signs, buttons, screens, phones, "
    "papers, cards, uniforms and vehicles are blank or show only simple lines and shapes. No sun, no birds, no falling "
    "rain or snow lines; an outdoor background may show only a plain pale (or dark night) sky band."
)
PLATE = (
    "BACKGROUND PLATE for a 2D animation: full-bleed landscape 1536x864, eye-level camera, NO people and no animals "
    "anywhere. Leave a clear, flat, empty floor area in the front-center of the picture where cartoon characters will be "
    "placed later: a standing adult there would be about 75% of the picture height, feet near 92% of the height. Keep the "
    "middle of the picture calm and uncluttered. Same drawing style, outline weight and color richness as the reference "
    "background pictures."
)
CUTOUT = (
    "CUTOUT: only the described subjects, as isolated cutouts on a fully transparent background (PNG with alpha channel) "
    "— no ground, no floor line, no cast shadow, no scenery, no frame, no other objects or people. Clean hard edges with "
    "the dark outline. Every subject must be fully visible with empty margin: nothing may touch or cross the canvas edges "
    "— keep at least 5% empty transparent space on every side. If a transparent background is impossible, make the whole "
    "background one flat pure magenta #FF00FF with no shading, and use no magenta, purple or hot pink at all on the subjects."
)
MOTION = (
    "MOTION STRIP: landscape 1536x1024, divided into three equal invisible columns. The three figures are three "
    "consecutive animation drawings of ONE continuous movement by the SAME person, like an animator's key pose, "
    "in-between and key pose: frame 1 in the left column, frame 2 in the center column, frame 3 in the right column. "
    "Between the frames keep everything identical except the moving parts: same scale, same camera angle, same facing "
    "direction, same clothes, colors and line weight, and the soles of the feet (or the legs of the stool, when sitting) "
    "on exactly the same invisible baseline at about 92% of the canvas height, at the same horizontal spot in each column "
    "— the body stays in place and only the arms, hands, head, face, torso lean and held objects move. A standing adult "
    "is about 70% of the canvas height (top of the head near 22%) — a sitting adult or a child is smaller in the same "
    "scale. Any object held in the hands keeps the same design and size in all three frames and stays inside the same "
    "column. Each figure is centered in its column, full body from head to shoes, and never crosses a column border; "
    "leave clear empty space between the columns. No motion lines, no effects, no flying objects unless the prompt asks "
    "for them."
)
WATER = (
    "IN-WATER STRIP: landscape 1536x1024, divided into three equal invisible columns, three consecutive animation "
    "drawings of ONE continuous movement by the SAME person who is in cold water. Draw only what is above the water: "
    "everything below a perfectly straight, invisible horizontal line at about 80% of the canvas height (the water "
    "surface) is not drawn at all — no water, no ice, no splash, no ripples. That cut line is at exactly the same height "
    "in all three frames. Same scale (the head about the same size as a standing adult's head that is 70% of the canvas "
    "tall), same clothes (wet winter clothes), colors and line weight; only the arms, hands, head, face and torso lean "
    "change unless the prompt says the body comes up onto the line. Each figure is centered in its column and never "
    "crosses a column border; leave clear empty space between the columns. No motion lines, no effects."
)
TURN = (
    "CHARACTER REFERENCE SHEET: landscape 1536x1024, three equal invisible columns, the SAME person three times standing "
    "relaxed with a calm, kind face: column 1 front view, column 2 three-quarter view facing left, column 3 pure side view "
    "facing left. Same scale, feet on the same invisible baseline at about 92% of the canvas height, standing adult about "
    "70% of the canvas height. This sheet defines this person for every later picture."
)
THUMB = (
    "THUMBNAIL PICTURE for a video cover: full-bleed landscape 1536x864, a complete scene with background (NOT a cutout). "
    "The people and their faces sit in the upper 62% of the picture; the bottom 35% is a calm, simple, darker surface "
    "(table, floor or ground) where large title text will be added later by code — nothing important there. Leave one "
    "empty space beside the main person's head (not over any face, hand or body) where a speech bubble will be added "
    "later. Strong, readable emotion for a small phone screen. Absolutely no text, no letters, no numbers, no symbols, "
    "no speech bubbles drawn."
)

CHECK_CODE = '''   ```python
   from PIL import Image
   import numpy as np
   def filled_mask(a):
       if a[2, 2, 3] > 0:                        # 투명이 아니면 순자홍 바탕을 빈 곳으로 봄
           r, g, b = (a[:, :, i].astype(int) for i in range(3))
           return ~((r > 200) & (b > 200) & (g < 90))
       return a[:, :, 3] > 40
   def check(path, cols, rows=1, margin=0.04, gap=0.012, feet=None):
       a = np.array(Image.open(path).convert("RGBA"))
       h, w = a.shape[:2]
       m = filled_mask(a)
       ys, xs = np.where(m)
       box = (xs.min() / w, ys.min() / h, xs.max() / w, ys.max() / h)
       bad = []
       if not (box[0] >= margin and box[1] >= margin and box[2] <= 1 - margin and box[3] <= 1 - margin):
           bad.append("잘림")
       for c in range(1, cols):                  # 칸 경계 둘레는 비어 있어야 함
           x = int(w * c / cols); d = int(w * gap)
           if m[:, x - d:x + d].any(): bad.append(f"칸 넘음 세로 {c}")
       for r in range(1, rows):
           y = int(h * r / rows); d = int(h * gap)
           if m[y - d:y + d, :].any(): bad.append(f"칸 넘음 가로 {r}")
       if feet:                                  # 동작·물속 그림: 세 사람의 아래 끝(발바닥·물 높이)이 같아야 함
           bottoms = []
           for c in range(cols):
               ys_c = np.where(m[:, w * c // cols:w * (c + 1) // cols].any(axis=1))[0]
               bottoms.append(ys_c.max() / h)
           if max(bottoms) - min(bottoms) > 0.02: bad.append(f"아래 끝 높이 다름 {[round(v, 3) for v in bottoms]}")
       print(path, "OK" if not bad else f"다시 — {bad}", [round(float(v), 3) for v in box])
       return not bad
   # 기준 그림·동작 그림·물속 그림: check(경로, cols=3, feet=True) · 소품 판: check(경로, cols=4, margin=0.02)
   ```'''

SAVE_CODE = '''       ```python
       from PIL import Image
       import os
       Q = getattr(Image, "Quantize", Image).FASTOCTREE
       def save_png(src, dst, limit=700_000):
           im = Image.open(src).convert("RGBA")
           w, h = im.size
           s = min(1.0, 1536 / max(w, h))
           while True:
               cur = im.resize((round(w * s), round(h * s)), Image.LANCZOS) if s < 1 else im
               cur.save(dst, optimize=True)
               if os.path.getsize(dst) > limit:
                   cur.quantize(colors=256, method=Q).save(dst, optimize=True)   # 256색 (투명 유지)
               if os.path.getsize(dst) <= limit or max(cur.size) <= 900:
                   break
               s *= 0.9
           print(dst, os.path.getsize(dst), cur.size)
       ```'''


def explainer(who: str, pron: str, poss: str) -> str:
    """설명 장면용 3장 (심리 편 G07·R08 과 같은 꼴 — 가리킴 → 말함 → 입 다묾, 입 맞추기용)."""
    return (f"{who}, three-quarter view, {poss} body facing slightly to the left of the picture, calm and focused. Frame 1: "
            f"{poss} left arm raised, pointing with the index finger up and to the LEFT (toward a screen out of frame), "
            f"looking where {pron} points, mouth closed. Frame 2: {pron} turns {poss} head to look at the viewer, the left "
            f"hand now held open at chest height palm up, explaining, mouth open as if talking. Frame 3: exactly like frame "
            f"2 but with {poss} mouth closed (for lip-sync).")


# ── 편마다 ───────────────────────────────────────────────────────────────────
# kind: ref(기준 그림 3면) · bg(배경판) · motion(동작 3장) · water(물속 3장) · props(소품 4) · thumb(썸네일 그림)
# 대본 줄 = tools/persona_gate.py 번호 (빈 줄·# 줄을 뺀 번호 · '-' 장 이름 줄 포함)
EPISODES = {
    "ellibeiteo-gathim-2026-11": {
        "title": "엘리베이터 떨어질 때 점프하면 살까? 갇혔을 때 진짜 할 일",
        "script": "대본 v1.11 (101줄)",
        "thumb_text": "「떨어질 때 점프하면 / 살 수 있을까?」 + 보조 「승강기안전공단의 답」",
        "stages": "멈춘 엘리베이터 안 · 층 사이 문틈 · 건물 1층 승강장 · 승강로 단면 그림",
        "people": (
            "E — the main person ('you' in this video): an ordinary Korean office worker in his early 30s on his way home, "
            "short neat black hair, a light-blue button shirt with rolled sleeves, a loosened navy tie, gray slacks, white "
            "sneakers, a dark-gray crossbody bag. A friendly, honest face that shows feelings clearly (surprise, worry, "
            "calm relief).\n"
            "M — a building manager: a kind Korean man in his early 60s, short gray hair, a plain dark-green work jacket "
            "(no logo, no name tag), beige work pants, black shoes, a small key ring clipped to his belt. Warm and "
            "responsible.\n"
            "R — a 119 rescue worker: a Korean man in his 30s in a plain orange rescue uniform with silver reflective "
            "stripes, a white helmet and work gloves (no letters, no badges, no logos), carrying a small dark tool bag. "
            "Calm and reassuring."
        ),
        "items": [
            ("ref", "E-REF", "E 기준 그림 (앞 · 4분의 3 · 옆)", "전체", ""),
            ("ref", "M-REF", "M(관리인) 기준 그림", "76~82 · 97", "This is M, the building manager."),
            ("bg", "BG-CAR", "멈춘 엘리베이터 안 · 닫힌 문 · 오른쪽 버튼판", "1~8 · 14~25 · 45~56 · 65~74 · 91~100",
             "Inside a stopped passenger elevator car of an ordinary Korean office building at night, seen from the back of "
             "the car looking toward the doors. In the center of the back wall: closed brushed-steel double doors. On the "
             "right side wall: a tall button panel with rows of plain round buttons that have no numbers or symbols, below "
             "them one larger round yellow emergency call button and a small round speaker grille; next to the panel a "
             "small blank metal plate (no writing). A thin metal handrail along the side walls. Soft, slightly dim ceiling "
             "lights. Cool gray-blue tones with a warm dim ceiling glow. The front-center floor of the car is open and "
             "empty where a character will stand or sit."),
            ("bg", "BG-GAP", "층 사이 · 조금 열린 문 아래로 깊은 틈", "3 · 9 · 31 · 41~42 · 59 · 84~88",
             "Seen from inside a stopped elevator car, looking straight at its doors, which are open only a hand's width "
             "in the center (about 15% of the picture width). The car stopped between floors: through the narrow opening "
             "the outer landing door's bottom edge and the building's hallway floor are far BELOW the car floor level, and "
             "under the car floor edge a deep, dark vertical gap of the elevator shaft drops away into shadow, with plain "
             "concrete walls and one steel rail. The danger is clear but calm — no people, nothing falling. Dim light. The "
             "car floor in the front of the picture is empty."),
            ("bg", "BG-LOBBY", "건물 1층 승강장 · 닫힌 엘리베이터 문 · 벽의 빨간 소화전함", "17~18 · 28~30 · 37~39 · 62~63 · 72~73 · 76~82 · 97",
             "The ground-floor elevator landing of an ordinary Korean apartment building in the evening. In the back "
             "center: closed brushed-steel elevator landing doors, a plain call-button panel beside them (blank buttons, no "
             "numbers) and a dark blank floor indicator above. On the left wall: a red metal fire hydrant cabinet (plain, no "
             "letters). On the right: a light-gray wall with a small plain bench. Clean tiled floor, warm ceiling lights. "
             "The front-center floor is open and empty."),
            ("bg", "BG-SHAFT", "승강로 단면 그림 · 레일 · 레일을 붙잡는 장치 · 바닥 완충기", "46~50 · 56",
             "This background is an exception: no character will stand in it, so the shaft may fill the picture. A clean "
             "side cut-away view, like a friendly educational cartoon diagram in the same painted style, of an elevator "
             "shaft in a building: a tall vertical shaft through the center with plain concrete walls; an elevator car (a "
             "simple box with a door) hangs in the middle from several steel ropes coming from above; two vertical steel "
             "guide rails run along the left and right sides of the car; on the car's lower sides two small sturdy clamp "
             "devices grip the rails (the safety brakes); at the very bottom on the pit floor stand two short spring "
             "buffers. Building floor slabs show as horizontal bands at the sides. No people, no labels, no arrows, no "
             "text — labels will be added by code. Calm daylight colors."),
            ("motion", "E01", "E: 덜컹 흔들려 비틀 → 벽을 짚고 버팀 → 둘레를 보며 불안", "2~3",
             "E, three-quarter view facing left, standing inside an elevator (no background). Frame 1: thrown slightly off "
             "balance by a sudden jolt, knees bent, both arms out to the sides, startled face. Frame 2: steadying himself, "
             "his right palm pressed flat against an invisible wall to his right at shoulder height, eyes wide. Frame 3: "
             "hand still on the invisible wall, looking around and up with a worried face, mouth slightly open."),
            ("motion", "E02", "E: 무릎 굽혀 뛰려는 자세 → 멈칫 바로 섬 → 바닥에 앉아 숨 고름", "7 · 10 · 46~52 · 94",
             "E, front view. Frame 1: knees deeply bent, arms pulled back, ready to jump up, a tense scared face. Frame 2: "
             "standing up straight again, hands loosely at his sides, eyebrows raised in realization ('wait, no need'). "
             "Frame 3: sitting directly on the floor with his legs crossed (his seat and legs rest on the same baseline as "
             "the feet in frames 1 and 2), back straight, hands on his knees, eyes half closed, breathing out slowly, calm."),
            ("motion", "E03", "E: 노란 비상통화 버튼을 누름 → 스피커 쪽으로 몸을 기울여 말함 → 끄덕이며 기다림", "6 · 65~66 · 96",
             "E, three-quarter view facing right, standing. Frame 1: his right index finger pressing forward at shoulder "
             "height (on a button out of frame on the right), focused face. Frame 2: leaning his head slightly to the right "
             "as if talking into a small speaker, mouth open, the hand still near the same spot. Frame 3: standing upright, "
             "hands lowered, nodding with a reassured small smile, waiting calmly."),
            ("motion", "E04", "E: 휴대전화로 전화 → 오른쪽 번호판을 가리키며 읽음 → 문자를 침", "67~70",
             "E, three-quarter view facing right, standing, holding the same smartphone (blank glowing screen) in all "
             "frames. Frame 1: the phone at his left ear, talking, focused face. Frame 2: the phone still at his ear, his "
             "right index finger pointing to the right at eye level (at a small plate out of frame), reading it aloud, "
             "mouth open. Frame 3: holding the phone in both hands at chest height, typing a text with his thumbs, "
             "concentrated."),
            ("motion", "E05", "E: 문을 손바닥으로 가볍게 두드림 → 손을 입가에 대고 소리쳐 알림 → 문에서 몸을 뒤로 물림", "71 · 86~88",
             "E, pure side view facing right, standing. Frame 1: his right palm raised flat at shoulder height, lightly "
             "tapping forward (on a door out of frame on the right). Frame 2: his right hand cupped beside his mouth, "
             "calling out toward the right, mouth wide open (not angry). Frame 3: leaning his upper body back away from "
             "the right, weight on his back foot, both palms raised a little in front of his chest, a careful calm face."),
            ("motion", "E06", "E: 문틈에 손을 넣어 벌리려 함 → 멈칫 손을 뺌 → 고개를 저음", "5 · 58~60 · 95",
             "E, three-quarter view facing right, standing. Frame 1: both hands reaching forward at chest height, fingers "
             "curled as if about to pry open a door, a hasty anxious face. Frame 2: he freezes and pulls both hands back "
             "toward his chest, eyes wide, realizing. Frame 3: hands lowered, shaking his head 'no' with a calm, firm face."),
            ("motion", "E07", "E: 왼쪽 화면을 가리킴 → 카메라를 보며 말함 → 같은 자세 입 다묾 (설명 장면)",
             "14~16 · 41~43 · 47~50 · 62~63 · 91~100", explainer("E", "he", "his")),
            ("motion", "M01", "M: 열쇠를 꺼내려다 → 멈추고 손을 듦 → 휴대전화로 119에 신고", "76~78 · 97",
             "M, three-quarter view facing left, standing in front of an elevator (no background). Frame 1: his right hand "
             "reaching to the key ring on his belt, a hurried, worried face. Frame 2: he stops, the key ring left on his "
             "belt, both hands raised a little with palms out, thinking 'no, I shouldn't open it'. Frame 3: holding a "
             "smartphone (blank screen) to his ear with his right hand, talking calmly, his left hand gesturing to the "
             "left (toward the elevator)."),
            ("motion", "M02", "M: 문 쪽으로 몸을 기울여 말을 걺 → 손바닥을 문에 대고 안심시킴 → 끄덕이며 기다림", "79~82",
             "M, pure side view facing left, standing close to a closed door out of frame on the left. Frame 1: leaning "
             "toward the left, one hand cupped beside his mouth, talking gently, kind face. Frame 2: his left palm resting "
             "flat at shoulder height to the left (on the closed door), a reassuring smile, mouth open ('help is "
             "coming'). Frame 3: standing upright, nodding, a patient calm face, hands relaxed."),
            ("motion", "R01", "R(119 구조대원): 공구 가방을 들고 도착 → 손을 들어 자기소개 → '이제 나오세요' 손짓", "23 · 62 · 72~73 · 87",
             "R, three-quarter view facing left, standing, the same small dark tool bag in his left hand in all frames. "
             "Frame 1: arriving with quick but calm steps, looking ahead. Frame 2: his right hand raised open at shoulder "
             "height in a friendly greeting, mouth open as if introducing himself. Frame 3: his right hand beckoning gently "
             "toward himself ('you can come out now, step here'), a reassuring smile."),
            ("props", "PROPS-E", "소품 4: 휴대전화 · 빈 승강기번호 판 · 빨간 소화전 상자 · 짐 상자", "20~22 · 32 · 39 · 68~69",
             "Prop sheet, landscape 1536x1024, four equal invisible columns, one prop centered in each column, all at a "
             "similar visual size, each fully inside its column: (1) a smartphone, front view, glowing blank screen; (2) a "
             "small rectangular brushed-metal plate with four screws, completely blank (a number will be added later); (3) "
             "a red metal fire hydrant cabinet box, front view, closed, plain with no letters; (4) a closed brown "
             "cardboard box with tape."),
            ("thumb", "TH-CHAR", "썸네일 그림: 멈춘 엘리베이터 안에서 뛰려고 무릎을 굽힌 E · 벽 너머 레일을 붙잡은 장치", "썸네일 · 0초",
             "Inside the stopped elevator car from picture 3, seen slightly from the side. On the LEFT half, E bends his "
             "knees deeply with his arms pulled back, about to jump, with a scared, unsure face (big eyes, clenched teeth). "
             "On the RIGHT third, the side wall of the car opens as a clean cut-away window into the shaft: a steel guide "
             "rail with a sturdy clamp device gripping it, softly lit. Empty space above E's head at the upper left for a "
             "speech bubble. The bottom 35% is the plain dark elevator floor."),
        ],
    },
    "ginae-yeongi-2026-11": {
        "title": "비행기 비상 탈출 때 짐 챙기면 위험, 승무원이 연 문으로",
        "script": "대본 v1.7 (118줄)",
        "thumb_text": "「기내에 연기가 찼다 / 가방, 두고 갈 수 있나?」 + 보조 「379명 전원 탈출」",
        "stages": "여객기 객실 통로 · 연기 찬 통로 · 비상구 문 앞 · 밤 활주로의 미끄럼대",
        "people": (
            "A — the main person ('you' in this video): an ordinary Korean woman in her early 30s traveling, long dark hair "
            "in a low ponytail, a soft oatmeal knit sweater, light-blue jeans, white sneakers, a small dark crossbody pouch "
            "worn across her body. A sensible, kind face that shows feelings clearly (shock, hesitation, determination).\n"
            "C — a flight attendant: a Korean woman in her 30s, neat low bun, a plain charcoal-navy uniform jacket and "
            "skirt, a simple mustard-yellow neck scarf, black low-heeled shoes, no wings, no badges, no logos, no name tag "
            "(not the uniform of any real airline). Brave, calm and commanding.\n"
            "P — another passenger: a Korean man in his late 50s, short graying hair, a navy windbreaker, khaki pants. "
            "Flustered and in a hurry, an ordinary person — not a bad person."
        ),
        "items": [
            ("ref", "A-REF", "A 기준 그림 (앞 · 4분의 3 · 옆)", "전체", ""),
            ("ref", "C-REF", "C(승무원) 기준 그림", "3~4 · 24~30 · 73~83", "This is C, the flight attendant."),
            ("bg", "BG-CABIN", "여객기 객실 통로 · 양쪽 좌석 · 바닥 불빛 줄", "2 · 5 · 11 · 57 · 68~71 · 96~101",
             "The economy cabin of a generic passenger jet, seen from the middle of the aisle looking toward the front. "
             "Rows of seats on the left and right with plain gray-blue fabric (no patterns, no logos), blank seatbacks, "
             "closed overhead bins above both sides, small round windows on the side walls showing only dark night. A thin "
             "line of small floor lights runs along both edges of the aisle carpet toward the front. Normal warm cabin "
             "lighting. Far ahead, a closed exit door area with a blank sign shape (no letters). The front-center aisle "
             "floor is open and empty where a character will stand."),
            ("bg", "BG-SMOKE", "같은 통로 · 위쪽 절반에 연기 · 바닥 불빛만 또렷", "2 · 65 · 85~90 · 93 · 115",
             "The same aircraft cabin aisle as before, but in an emergency: the main lights are off, dim emergency lighting, "
             "soft gray smoke fills the upper half of the cabin and hides the overhead bins and the tops of the seats, while "
             "near the floor the air is clearer and the two lines of small floor lights along the aisle glow brightly, "
             "leading forward. No fire inside the cabin, no people. Serious but calm mood. The front-center aisle floor is "
             "open and empty."),
            ("bg", "BG-EXIT", "비상구 문 앞 · 한 문의 창밖에 주황 불빛 · 다른 문은 어두움", "8 · 12 · 23~25 · 28 · 73~83",
             "The galley and exit area of a passenger jet, front view: in the back center, a large closed emergency exit "
             "door with a small round window and a big lever handle (blank, no letters, no arrows). Through that door's "
             "small window, a strong orange glow shows outside (fire outside — only the glow, no flames inside). Further "
             "to the left, a second exit door whose small window is dark and calm. Dim emergency lights, a little gray "
             "smoke near the ceiling. The front-center floor is open and empty."),
            ("bg", "BG-SLIDE", "밤 활주로 · 여객기 문에서 펼쳐진 노란 미끄럼대", "18~33 · 42 · 91 · 105",
             "Night at an airport, ground level on the tarmac. On the right, the side of a large generic white passenger "
             "jet (plain white body, no logos, no stripes or colors of any real airline, no letters or numbers) with an "
             "open door high up; from that door a big yellow inflatable evacuation slide comes down at an angle to the "
             "ground in the center-right. Small runway lights dot the dark ground; far behind the plane on the left, a "
             "soft orange glow and some dark smoke (a fire far away — no flames close up). Plain dark-blue night sky band, "
             "no stars. The front-left ground is open and empty where characters will stand."),
            ("motion", "A01", "A: 선반으로 손을 뻗어 가방을 잡으려 함 → 멈칫 뒤를 돌아봄 → 빈손으로 출구 쪽으로 몸을 돌림", "5 · 7 · 11 · 57 · 68~71 · 104",
             "A, three-quarter view facing right, standing in an aisle (no background). Frame 1: both arms reaching up and "
             "forward to an overhead bin out of frame above, fingers about to grab a bag handle, an anxious hurried face. "
             "Frame 2: she freezes, arms coming down, looking back over her left shoulder (thinking of the people behind "
             "her). Frame 3: arms down with empty hands, her body turned slightly to the left toward the exit, a "
             "determined face."),
            ("motion", "A02", "A: 허리를 숙여 걸음 → 좌석 등받이를 짚으며 줄을 셈 → 낮게 계속 앞으로", "9 · 14 · 85~90 · 115",
             "A, pure side view facing right, walking bent forward at the waist (NOT crawling), knees slightly bent, head "
             "low, her left forearm pressing a sleeve over her nose and mouth in all frames. Frame 1: her right hand "
             "reaching forward low. Frame 2: her right hand touching the top corner of an invisible seatback at waist "
             "height, counting, focused eyes. Frame 3: her right hand forward again, continuing low and steady."),
            ("motion", "A03", "A: 발부터 앉아 팔을 가슴에 모음 → 뒤로 기대어 미끄러짐 → 내려와 일어나 앞으로 감", "91~92 · 105",
             "A, pure side view facing right (the slide itself is NOT drawn — code moves her along it). Frame 1: sitting "
             "with both legs straight out in front, feet first, arms crossed over her chest, a brave face. Frame 2: the same "
             "pose leaning back a little, ponytail flying back, eyes squinting (sliding down). Frame 3: standing up and "
             "stepping forward to the right, arms down, moving away quickly, relieved face. Her lowest point touches the "
             "same baseline in all frames."),
            ("motion", "A04", "A: 뒤쪽 비상구까지 줄을 손가락으로 셈 → 여권을 바지 주머니에 넣음 → 보조배터리를 앞 좌석 주머니에 꽂음", "96~101 · 117",
             "A, three-quarter view facing right, standing calmly in an aisle before sitting down. Frame 1: looking back "
             "over her shoulder, her left index finger pointing back, counting rows with a light smile. Frame 2: putting a "
             "small dark-blue passport (plain cover, no emblem, no letters) into the front pocket of her jeans with her "
             "right hand. Frame 3: bending slightly forward, sliding a small white power bank into an invisible seatback "
             "pocket in front of her at waist height."),
            ("motion", "A05", "A: 왼쪽 화면을 가리킴 → 카메라를 보며 말함 → 같은 자세 입 다묾 (설명 장면)",
             "13~16 · 49~55 · 58~65 · 109~117", explainer("A", "she", "her")),
            ("motion", "C01", "C: 확성기를 들고 외침 → 팔을 뻗어 출구를 가리킴 → '이쪽으로' 손짓", "3~4 · 26~27 · 30 · 77",
             "C, three-quarter view facing left, standing firm, holding the same small white handheld megaphone (no "
             "letters) in her left hand in all frames. Frame 1: the megaphone raised to her mouth, shouting clearly, "
             "eyebrows set, a brave face. Frame 2: the megaphone lowered, her right arm stretched straight out pointing to "
             "the left (toward an exit), mouth open. Frame 3: her right hand beckoning strongly toward the left ('this way, "
             "come!'), calm but urgent face."),
            ("motion", "C02", "C: 문 창밖을 확인 → 고개를 저으며 팔로 길을 막음 → 다른 문을 가리킴", "12 · 24~25 · 28 · 75~76",
             "C, pure side view facing right, standing next to a door out of frame on the right. Frame 1: leaning close to "
             "the right, looking carefully through a small window at eye level, serious face. Frame 2: her head turned back "
             "to the left, shaking her head 'no', her right arm stretched out flat to block the way, palm out. Frame 3: her "
             "left arm pointing far to the left toward another exit, mouth open, calling out the direction."),
            ("motion", "P01", "P: 선반에서 여행 가방을 끌어내리려 애씀 → 가방이 걸려 쩔쩔맴 → 가방을 두고 몸만 나감", "40 · 43 · 48 · 106~107",
             "P, three-quarter view facing right, standing in an aisle. Frame 1: both arms up, pulling a gray hard-shell "
             "rolling suitcase down from an overhead bin out of frame, straining, a worried sweaty face. Frame 2: holding "
             "the suitcase at chest height, stuck, looking back with a flustered, embarrassed face. Frame 3: the suitcase "
             "is gone (he left it behind), both hands empty, turning to the right to go, a relieved, determined face."),
            ("props", "PROPS-A", "소품 4: 기내용 여행 가방 · 여권 · 보조배터리 · 노트북 가방", "5 · 41~44 · 66 · 98~100",
             "Prop sheet, landscape 1536x1024, four equal invisible columns, one prop centered in each column, all at a "
             "similar visual size, each fully inside its column: (1) a gray hard-shell carry-on rolling suitcase, standing "
             "upright; (2) a closed dark-blue passport with a plain cover (no emblem, no letters); (3) a small white power "
             "bank with a short cable; (4) a black laptop bag with a shoulder strap."),
            ("thumb", "TH-CHAR", "썸네일 그림: 연기 찬 통로 · 선반의 가방과 출구 사이에서 망설이는 A · 출구를 가리키는 승무원 C", "썸네일 · 0초",
             "In the smoky aircraft cabin aisle from picture 4. In the CENTER-LEFT, A stands in the aisle with one hand "
             "reaching up toward an open overhead bin with her bag inside, but her head is turned toward the exit with a "
             "torn, frightened face (wide eyes, biting her lip). On the RIGHT, C the flight attendant points strongly to the "
             "front exit with a brave, commanding face. Gray smoke along the ceiling, the floor lights glowing. Empty space "
             "above A's head at the upper left for a speech bubble. The bottom 35% is the plain dark aisle carpet and seat "
             "bases."),
        ],
    },
    "eoreum-kkaejim-2026-11": {
        "title": "얼음이 깨져 물에 빠졌을 때, 가까운 기슭 말고 왔던 쪽으로",
        "script": "대본 v1.6 (123줄)",
        "thumb_text": "「얼음이 깨졌다 / 첫 1분, 당신이라면?」 + 보조 「① 가까운 기슭 ② 왔던 쪽」",
        "stages": "얼어붙은 저수지 · 깨진 얼음 구멍과 걸어온 발자국 · 저수지 기슭 · 따뜻한 방",
        "people": (
            "I — the main person ('you' in this video): an ordinary Korean man in his 40s, a dark-green padded winter "
            "jacket, a gray knit beanie, a mustard scarf, dark jeans, brown winter boots. An honest everyday face that "
            "shows feelings clearly (shock, effort, calm focus, relief).\n"
            "W — a passer-by who helps: an ordinary Korean woman in her 30s, a long cream padded coat, a red knit scarf, "
            "black pants, black winter boots, a small crossbody bag. Quick-thinking and calm, never reckless."
        ),
        "items": [
            ("ref", "I-REF", "I 기준 그림 (앞 · 4분의 3 · 옆)", "전체", ""),
            ("ref", "W-REF", "W(돕는 사람) 기준 그림", "19 · 91~109 · 120", "This is W, the passer-by who helps."),
            ("bg", "BG-LAKE", "얼어붙은 저수지 · 멀리 기슭과 마른 나무", "2 · 15~17 · 22~23 · 31~34 · 112~115 · 122",
             "A wide frozen reservoir in the Korean countryside on a gray winter afternoon. The flat gray-white ice surface "
             "fills the lower two thirds of the picture, with a few darker, thinner-looking patches farther out. A far shore "
             "with bare brown trees, dry reeds and low hills. A plain pale overcast sky band at the top (no sun, no birds). "
             "Quiet, cold, slightly lonely mood. The front-center ice surface is open and empty where a character will "
             "stand."),
            ("bg", "BG-HOLE", "깨진 얼음 구멍 · 뒤로 이어진 걸어온 발자국 · 반대쪽 가까워 보이는 기슭", "3 · 9~11 · 44~49 · 57~66 · 74~82 · 85~89 · 117~119",
             "A close view of a frozen reservoir. In the front-center, a jagged broken hole in the ice filled with dark, cold "
             "blue-black water; the hole spans about 25% to 75% of the picture width and about 62% to 82% of the height, "
             "and the water in it is EMPTY (a person will be placed in it later). Behind the hole, a clear line of boot "
             "footprints in thin snow on the ice leads straight back from the hole to the distant shore at the upper left "
             "(the way the person came). To the right, a different shore looks closer, but the ice between is darker and "
             "thinner. A plain pale overcast sky band at the top. Cold, serious but calm mood."),
            ("bg", "BG-SHORE", "저수지 기슭 · 마른 갈대 · 빈 구명환 걸이", "19 · 91~106",
             "The snowy bank of a frozen reservoir, seen from the land side looking out over the ice. In the front, flat "
             "snowy ground on the bank, open and empty in the center where a character will stand or lie down. On the left, "
             "a wooden post with an empty hook for a ring buoy (no buoy, no sign, no letters). Dry brown reeds along the "
             "edge, then the flat frozen ice reaching to the far shore with bare trees. A plain pale sky band at the top."),
            ("bg", "BG-WARM", "따뜻한 방 · 난로 · 접은 담요", "21 · 70~71 · 107~109",
             "A small warm room in winter (like the rest room of a reservoir fishing site): a glowing orange electric heater "
             "on the left, a low sofa with thick folded blankets on the right, a window showing only snowy gray light, "
             "warm lamp light. The front-center floor is open and empty."),
            ("water", "I01", "I(물속): 찬물에 숨을 헉 → 얼음 가장자리를 붙잡고 숨을 고름 → 왔던 쪽으로 몸을 돌림", "3 · 44~49 · 57 · 87~88 · 117",
             "I, in the water. Frame 1: front view, gasping in shock from the cold, mouth wide open, eyes squeezed, both "
             "hands slapping down onto the cut line. Frame 2: front view, both forearms resting on the cut line in front of "
             "him (holding the ice edge — draw no ice), mouth closed, breathing out slowly, a calmer face, eyes open. Frame "
             "3: his body turned to a three-quarter view facing left, looking back to the left (the way he came), a "
             "determined face, forearms still on the line."),
            ("water", "I02", "I(물속): 두 팔을 얼음 위로 길게 뻗음 → 다리를 차며 몸을 눕힘 → 배를 얼음 위로 밀어 올림", "60~65 · 118",
             "I, pure side view facing left, climbing out over the edge of the ice. Frame 1: his chest at the cut line, "
             "both arms stretched far forward to the left lying flat ON the line (on top of the ice — draw no ice), head "
             "up. Frame 2: his body tilted more horizontal, more of his back above the line, effort on his face (his legs "
             "under the line are not drawn). Frame 3: his belly is up on the line and his whole body lies almost flat along "
             "it, his legs now visible stretched out behind him on the line, arms forward, a relieved, strained face. In "
             "every frame anything below the line is not drawn."),
            ("motion", "I03", "I(얼음 위): 엎드려 숨 고름 → 옆으로 굴러감 → 팔꿈치로 기어 멀어짐", "67~69 · 118",
             "I, on the ice (no ice drawn), pure side view facing left, his clothes wet. Frame 1: lying flat on his belly, "
             "arms forward, catching his breath. Frame 2: rolling sideways, half on his back, arms tucked in. Frame 3: back "
             "on his belly, crawling forward on his elbows to the left, body low and flat. The lowest point of his body "
             "touches the same baseline in all frames."),
            ("water", "I04", "I(물속): 팔꿈치까지 얼음에 걸치고 버팀 → 손을 입가에 대고 크게 외침 → 다시 차분히 기다림", "74~82 · 89 · 119",
             "I, in the water, front view. Frame 1: both forearms and elbows resting flat on the cut line, his chin above "
             "it, a calm, patient face, eyes open (waiting). Frame 2: his right hand cupped beside his mouth, shouting "
             "loudly for help, mouth wide open, his left forearm staying on the line. Frame 3: both forearms back on the "
             "line, resting his chin near his arms, a tired but steady face."),
            ("motion", "I05", "I(마른 옷 · 기슭): 왼쪽 화면을 가리킴 → 카메라를 보며 말함 → 같은 자세 입 다묾 (설명 장면)",
             "26~28 · 31~41 · 50~55 · 111~122", explainer("I (dry clothes, standing)", "he", "his")),
            ("motion", "W01", "W: 사람이 빠진 걸 보고 놀람 → 휴대전화로 119에 신고하며 가리킴 → 던질 것을 찾아 둘러봄", "19 · 91~94 · 120",
             "W, three-quarter view facing left, standing on a bank (no background). Frame 1: frozen in shock, both hands "
             "at her mouth, eyes wide, looking to the left. Frame 2: holding a smartphone (blank screen) at her ear with her "
             "right hand, talking fast but clearly, her left arm pointing to the left. Frame 3: the phone held in front of "
             "her chest on speaker, her head turned to the right, quickly searching around for something to throw, a "
             "focused face."),
            ("motion", "W02", "W: 구명환을 뒤로 젖혀 던질 준비 → 앞으로 던짐 → 던진 쪽을 지켜봄", "96 · 102~103",
             "W, pure side view facing left, standing firmly, legs apart. Frame 1: holding an orange-and-white ring buoy "
             "(no letters) in her right hand pulled back behind her, a coil of white rope in her left hand. Frame 2: her "
             "right arm swinging forward, the ring buoy just leaving her fingers in front of her, body leaning forward. "
             "Frame 3: her empty right hand forward, the rope end still held in her left hand, watching carefully to the "
             "left."),
            ("motion", "W03", "W: 기슭에 엎드려 긴 나뭇가지를 내밂 → 팔꿈치로 버팀 → 천천히 당김", "103~104",
             "W, pure side view facing left, lying flat on her belly (the ground is not drawn), holding the same long brown "
             "wooden branch in both hands in all frames, reaching it far to the left. Frame 1: pushing the branch forward, "
             "arms stretched, concentrating. Frame 2: holding it steady, elbows dug in, calling out encouragement, mouth "
             "open. Frame 3: pulling the branch back slowly toward herself, still lying flat, a determined face. The lowest "
             "point of her body touches the same baseline in all frames."),
            ("motion", "W04", "W: 접은 담요를 들어 올림 → 넓게 펼쳐 감싸 주는 손짓 → 휴대전화로 119 안내를 들으며 끄덕", "107~109",
             "W, three-quarter view facing left, standing indoors. Frame 1: holding a thick folded gray wool blanket in both "
             "hands at chest height. Frame 2: spreading the blanket wide open with both arms, as if wrapping it around "
             "someone in front of her (no other person drawn). Frame 3: the blanket gone, holding a smartphone on speaker in "
             "front of her, listening carefully and nodding."),
            ("props", "PROPS-I", "소품 4: 주황 구명환 · 긴 나뭇가지 · 접은 담요 · 목에 거는 얼음 송곳", "62 · 96~104 · 107 · 115",
             "Prop sheet, landscape 1536x1024, four equal invisible columns, one prop centered in each column, all at a "
             "similar visual size, each fully inside its column: (1) an orange-and-white ring buoy with a coiled white rope "
             "(no letters); (2) a long, straight dry brown tree branch, lying diagonally; (3) a thick folded gray wool "
             "blanket; (4) a pair of ice picks — two short plastic handles with small metal spikes, joined by a cord to hang "
             "around the neck."),
            ("thumb", "TH-CHAR", "썸네일 그림: 깨진 얼음 구멍 속 I · 뒤로 걸어온 발자국 · 반대쪽 가까워 보이는 기슭", "썸네일 · 0초",
             "The broken ice hole from picture 4. In the CENTER, I is in the dark water up to his chest, both forearms on "
             "the broken ice edge, his face turned to look back over his shoulder with a frightened, hesitant face (wide "
             "eyes, mouth open). Behind him the clear line of his own footprints leads back to the far shore; on the other "
             "side a nearer-looking shore lies beyond darker, thinner ice. Empty space above his head at the upper right "
             "for a speech bubble. The bottom 35% is a plain, slightly shadowed gray ice surface in the foreground."),
        ],
    },
    "pon-kkaejyeosseo-2026-11": {
        "title": "'엄마 나 폰 깨졌어' 문자에 3억 원 잃은 엄마와 막은 엄마",
        "script": "대본 v1.11 (119줄)",
        "thumb_text": "「엄마 나 폰 깨졌어 / 당신이라면 답장?」 + 보조 「앱 하나로 명의 대출까지」",
        "stages": "저녁 집 식탁 · 아들의 사무실 · 은행 창구",
        "people": (
            "O — the main person ('you' in this video): an ordinary Korean mother around 60, short soft-permed dark hair "
            "with some gray strands, thin gold-rimmed glasses, a mustard-yellow cardigan over a cream blouse, gray slacks, "
            "house slippers. A warm, caring face that shows feelings clearly (worry, doubt, relief).\n"
            "S — her son: a Korean man around 30, short neat hair, a white shirt and dark-gray suit pants, a lanyard with a "
            "blank card. Cheerful and kind."
        ),
        "items": [
            ("ref", "O-REF", "O 기준 그림 (앞 · 4분의 3 · 옆)", "전체", ""),
            ("ref", "S-REF", "S(아들) 기준 그림", "31~37", "This is S, her son."),
            ("bg", "BG-HOME", "저녁 집 식탁 · 앞쪽에 가로로 긴 빈 식탁", "2~12 · 19~28 · 41~55 · 84~86 · 95~99 · 109~118",
             "A cozy Korean apartment dining room in the evening, front view from across a table. In the FRONT, a wooden "
             "dining table runs across the whole width of the picture: its top surface is visible as a wide flat band from "
             "about 70% to 82% of the picture height, completely EMPTY (a phone will be added later), its front edge fills "
             "the bottom. A character will sit BEHIND this table in the middle, visible from the chest up. Behind: a warm "
             "cream wall with a framed picture of only soft color shapes, a wall clock with no numbers, a window with "
             "evening blue light, a warm pendant lamp. Calm and homely."),
            ("bg", "BG-OFFICE", "아들의 사무실 · 책상과 빈 모니터", "31~37",
             "A bright modern Korean office in the daytime: rows of desks with monitors whose screens show only simple "
             "colored shapes (no text), a few green plants, big windows with only soft light. The front-center floor is "
             "open and empty where a character will stand."),
            ("bg", "BG-BANK", "은행 창구 · 이름·로고 없는 은행", "73 · 87~89 · 98 · 100~105",
             "A generic bank branch (no logo, no bank name, no colors of any real bank): a long light-wood service counter "
             "at the back with a few blank screens and a small plant, a waiting-number display that is completely blank, a "
             "row of simple waiting chairs on the left, soft daylight. The front-center floor is open and empty where a "
             "character will stand."),
            ("motion", "O01", "O(앉아서): 진동에 휴대전화를 집어 듦 → 화면을 읽으며 걱정 → 답장하려 엄지가 머뭇", "2~5 · 7",
             "O, sitting on a plain low wooden stool (the same stool in all frames, part of the cutout), front view, as if "
             "at a table, holding the same smartphone (blank glowing screen) in all frames. Frame 1: picking up the phone "
             "with a surprised face as it buzzes. Frame 2: holding it closer with both hands, reading through her glasses, "
             "eyebrows knitted with worry ('is my child in trouble?'). Frame 3: her right thumb hovering over the screen, "
             "about to type a reply, a hesitant, anxious face."),
            ("motion", "O02", "O(앉아서): 턱에 손 · 고개를 갸웃 → 손바닥으로 휴대전화를 엎어 누름 → 결심한 얼굴로 끄덕", "8 · 11 · 41~46 · 57 · 113",
             "O, sitting on the same plain low wooden stool, front view. Frame 1: her hand on her chin, head tilted, a "
             "doubtful frown, looking down at the invisible table in front of her. Frame 2: her right hand pressing down "
             "flat at table height, as if turning a phone face down (draw no phone). Frame 3: hands folded on her lap, a "
             "firm, decided face, a small nod."),
            ("motion", "O03", "O(앉아서): 저장된 번호를 누름 → 귀에 대고 초조 → 아들 목소리에 안도의 웃음", "9 · 34~35 · 41 · 51~52 · 112",
             "O, sitting on the same plain low wooden stool, three-quarter view facing right, holding the same smartphone in "
             "all frames. Frame 1: tapping a saved contact on the phone with her index finger, focused. Frame 2: the phone "
             "at her right ear, waiting, a nervous face, her left hand on her chest. Frame 3: the phone still at her ear, a "
             "big relieved smile, eyes crinkled, her left hand waving lightly ('oh, you're fine!')."),
            ("motion", "O04", "O(서서): 휴대전화 전원 버튼을 길게 누름 → 꺼진 휴대전화를 멀리 둠 → 무선 집 전화로 112에 신고", "95~98 · 114",
             "O, standing, three-quarter view facing right. Frame 1: holding a smartphone in both hands, pressing its side "
             "power button firmly with a serious face. Frame 2: holding the dark, turned-off phone away from her at arm's "
             "length to the right, about to put it down. Frame 3: the smartphone gone; she holds a plain white cordless home "
             "phone handset to her ear, talking clearly and urgently."),
            ("motion", "O05", "O: 손을 입가에 대고 속삭이듯 암호 정하기 → 검지를 입에 '쉿' → 기쁘게 끄덕", "36 · 84~86 · 116~117",
             "O, standing, three-quarter view facing right. Frame 1: leaning slightly to the right, her hand cupped beside "
             "her mouth, whispering a secret with a playful smile. Frame 2: her index finger on her lips ('shh, just between "
             "us'), eyes smiling. Frame 3: a firm, happy nod, hands together in front of her."),
            ("motion", "O06", "O: 창구에서 신분증을 건넴 → 서류에 서명 → 안심한 얼굴", "87~89 · 102~103",
             "O, standing, three-quarter view facing right, as if at a counter. Frame 1: holding out a small plain ID card "
             "(only a simple gray head-silhouette shape and gray lines, no letters) toward the right. Frame 2: leaning "
             "slightly forward, signing on an invisible counter with a pen in her right hand, concentrating. Frame 3: "
             "standing upright, the pen gone, both hands on her bag strap, a relieved, satisfied smile."),
            ("motion", "O07", "O: 왼쪽 화면을 가리킴 → 카메라를 보며 말함 → 같은 자세 입 다묾 (설명 장면)",
             "16~27 · 47~50 · 59~81 · 109~111", explainer("O", "she", "her")),
            ("motion", "S01", "S(사무실): 울리는 휴대전화를 받음 → 귀에 대고 어리둥절 → 웃으며 '나 괜찮아'", "34~35",
             "S, three-quarter view facing left, standing at work, holding the same smartphone in all frames. Frame 1: "
             "lifting the phone and looking at its screen, a little surprised. Frame 2: the phone at his left ear, a puzzled "
             "face ('mom? what happened?'). Frame 3: the phone at his ear, laughing reassuringly, his right hand raised open "
             "('I'm totally fine!')."),
            ("props", "PROPS-P1", "소품 4: 큰 휴대전화(빈 화면) · 액정 깨진 휴대전화 · 신분증 · 카드", "2~5 · 11 · 57~61 · 101",
             "Prop sheet, landscape 1536x1024, four equal invisible columns, one prop centered in each column, all at a "
             "similar visual size, each fully inside its column: (1) a smartphone, front view, with a completely blank white "
             "glowing screen (message bubbles will be added later by code); (2) a smartphone with a cracked screen (simple "
             "crack lines on a dark screen); (3) a plain ID card with only a simple gray head-silhouette shape and gray lines "
             "(no letters, no numbers, no real ID design); (4) a plain blue bank card with only a chip and a few gray lines "
             "(no letters, no numbers, no brand)."),
            ("props", "PROPS-P2", "소품 4: 무선 집 전화 · 자물쇠 · 서류와 펜 · 지폐 봉투", "73~81 · 87~91 · 97~98",
             "Prop sheet, landscape 1536x1024, four equal invisible columns, one prop centered in each column, all at a "
             "similar visual size, each fully inside its column: (1) a white cordless home phone handset standing on its "
             "small base; (2) a closed silver padlock; (3) a sheet of paper with only gray lines and an empty signature "
             "line, with a black pen lying on it; (4) a plain white envelope with a few green-gray banknote shapes peeking "
             "out (no numbers, no faces, no real currency design)."),
            ("thumb", "TH-CHAR", "썸네일 그림: 저녁 식탁에서 문자를 보며 답장할지 망설이는 엄마 O", "썸네일 · 0초",
             "At the evening dining table from picture 3. In the CENTER, O sits behind the table holding her smartphone close "
             "with both hands, its blank screen glowing white on her face, her thumb hovering over it, with a deeply "
             "worried, torn face (eyebrows up, lips pressed), her glasses reflecting the screen light. Warm lamp light "
             "behind her, cool screen light on her face. Empty space above her head at the upper right for a speech bubble. "
             "The bottom 35% is the plain dark wooden table surface."),
        ],
    },
}

KIND_INFO = {
    "ref": ("PNG 700KB 이하 · 투명 · 가로 1536×1024 · 기준 3면"),
    "bg": ("JPEG 700KB 이하 · 가로 1536×864"),
    "motion": ("PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장"),
    "water": ("PNG 700KB 이하 · 투명 · 가로 1536×1024 · 물속 3장 (물·얼음은 그리지 않음)"),
    "props": ("PNG 700KB 이하 · 투명 · 가로 1536×1024 · 소품 4"),
    "thumb": ("JPEG 700KB 이하 · 가로 1536×864 · 글자 없음"),
}


def rel_path(ep: str, kind: str, name: str) -> str:
    """저장 경로 — 만스피·심리 편과 같은 폴더 꼴 (배경 puppet/ · 원화·소품 puppet/motion/ · 썸네일 그림 images/)."""
    if kind == "bg":
        return f"crisis/source/{ep}/puppet/{name}.jpg"
    if kind == "thumb":
        return f"crisis/source/{ep}/images/{name}.jpg"
    return f"crisis/source/{ep}/puppet/motion/{name}.png"


def build(ep: str, spec: dict) -> str:
    items = spec["items"]
    n = len(items)
    num = {it[1]: i + 1 for i, it in enumerate(items)}
    refs = [it for it in items if it[0] == "ref"]
    ref_nums = " · ".join(f"{num[r[1]]}번 {r[1]}" for r in refs)
    first_bg = min(i + 1 for i, it in enumerate(items) if it[0] == "bg")
    last_bg = max(i + 1 for i, it in enumerate(items) if it[0] == "bg")
    has_water = any(it[0] == "water" for it in items)
    L = []
    L.append(f"# {ep} 롱폼 — 만화 무대·움직임 그림 {n}장 (ChatGPT용 · 1번부터 차례로 모두)")
    L.append("")
    L.append(f"작성: {VERSION} — {DATE} — 사용자 지시 \"만스피 영상처럼 영상 만들거니까 챗지피티한테 만들 이미지 생성 명령 알려줘 그리고 썸네일 이미지도\". "
             f"기준 대본 = `crisis/source/{ep}/{ep}.txt` {spec['script']} · 영상 「{spec['title']}」.")
    L.append("")
    L.append("**어떻게 쓰는가 — 주식 만스피 편과 같은 코드 애니메이션**")
    L.append("- Claude 가 코드로 만든다: 배경 그림 위에 인물·소품 조각을 올리고, **동작마다 이어지는 원화 3장**(키 → 중간 → 키)을 초당 8~12장으로 바꿔 끼워 팔·몸·얼굴이 실제로 움직이게 한다. "
             "숫자·카드·자막·문자 말풍선은 그림 속 빈 판·빈 화면 위에 코드가 얹는다 → **그림에는 글자가 하나도 없어야 한다.**")
    L.append(f"- 인물은 **이 편에서 새로** — 만스피 편 사람(곱슬머리 V · 정장 E)은 그리지 않고 그림체만 같게. 첫 그림({ref_nums})이 이 편 인물의 기준.")
    L.append(f"- 무대는 다른 편과 겹치지 않게 ({spec['stages']}) — 유튜브 '반복 콘텐츠' 정책.")
    L.append(f"- 썸네일 그림(마지막 장)은 만스피처럼 **그림만** — 문구 {spec['thumb_text']} 는 Claude 가 코드로 얹는다 (문구는 페르소나 관문 제목 단계 통과).")
    L.append("- ※ 안전 교육 영상(연구·교육용) — 실제 사고의 숨진 분·다친 분은 그리지 않고, 사고는 빈 무대·소품·숫자로 보여 준다. 위험은 차분히, 아무도 악당으로 그리지 않는다.")
    L.append("")
    L.append(f"| 번호 | 저장 경로 (모두 `crisis/source/{ep}/` 아래) | 무엇 | 대본 줄 |")
    L.append("|---|---|---|---|")
    for i, (kind, name, what, lines, _p) in enumerate(items, 1):
        short = rel_path(ep, kind, name).split(f"{ep}/", 1)[1]
        L.append(f"| {i} | `{short}` | {what} | {lines} |")
    L.append("")
    L.append("## ChatGPT에게 — 이 파일을 읽으면 할 일")
    L.append("0. **이 주소를 지금 새로 열어 그 내용만 쓴다** — 이 대화에서 예전에 읽은 파일·프롬프트(주식·심리 편·실사 사진·종이 인형극 포함)가 있어도 쓰지 않는다. 답의 첫 줄에 이 파일 맨 위 '작성' 줄을 그대로 적는다.")
    L.append("   **★ 먼저 그림체 기준 그림을 열어 본다 — 새 그림은 모두 이 그림들과 같은 사람이 그린 것처럼 (그림체·선 굵기·색·얼굴 꼴·비율). 단, 그 안의 사람(곱슬머리 남자 · 정장 남자)·장소·글자는 따라 그리지 않는다.**")
    L.append(f"   - 인물 그림체 (만스피 편): {REF_BASE}/puppet/V-CALM.png · 동작 시트 {REF_BASE}/puppet/motion/V04.png · {REF_BASE}/puppet/motion/V16.png")
    L.append(f"   - 배경 그림체: {REF_BASE}/puppet/BG-NIGHT.jpg · {REF_BASE}/puppet/BG-STUDIO.jpg")
    L.append(f"   - 썸네일 그림체: {REF_BASE}/images/TH-CHAR.jpg (왼쪽 '-50%' 글자는 따라 그리지 않음)")
    L.append("   그림을 열 수 없으면 아래 '공통 화풍'과 '인물' 설명대로 그린다.")
    L.append(f"   **★ 이 편의 인물은 {ref_nums} 이 기준이다 — 그 뒤 모든 그림의 같은 사람은 기준 그림과 얼굴·머리·옷·색·비율이 똑같아야 한다.** 다르게 나오면 다시 만든다.")
    L.append(f"1. 아래 1~{n}번 **{n}장을 번호 순서대로 모두** 만든다. 질문하지 말고, 한 장을 만든 뒤 멈추지 말고 다음 장으로 넘어간다. 이미지 한도 때문에 멈추면 사용자가 `계속`이라고 보낸다 → 아직 안 만든 번호부터.")
    L.append("2. 프롬프트(``` 안)를 **한 글자도 바꾸지 않고 그대로** 쓰고, 맨 앞에 **공통 화풍** 문단을 붙인다.")
    L.append("   - **기준 그림(ref)**: 공통 화풍 → **인물** → **CUTOUT** → **기준 시트** → 프롬프트.")
    L.append(f"   - **배경({first_bg}~{last_bg}번)**: 공통 화풍 → **배경판** → 프롬프트.")
    L.append("   - **동작 그림**: 공통 화풍 → **인물** → **CUTOUT** → **MOTION STRIP** → 프롬프트.")
    if has_water:
        L.append("   - **물속 그림**: 공통 화풍 → **인물** → **CUTOUT** → **IN-WATER STRIP** → 프롬프트. (물·얼음은 그리지 않는다 — 코드가 얼음 구멍 배경 위에 얹는다.)")
    L.append("   - **소품**: 공통 화풍 → **CUTOUT** → 프롬프트.")
    L.append(f"   - **썸네일 그림({n}번)**: 공통 화풍 → **인물** → **썸네일** → 프롬프트.")
    L.append("3. **동작 그림은 한 장에 같은 사람을 3번** 그린다 — 왼쪽 → 가운데 → 오른쪽이 **한 동작을 이어 그린 3장**(애니메이션 원화)이다. 세 사람이 **같은 크기·같은 자리·같은 방향·같은 옷**이고, **발바닥(앉은 자세는 의자 다리, 누운 자세는 몸 아래 끝 · 물속 그림은 물 높이 선)이 같은 높이**에 있고, **움직이는 부분(팔·손·머리·얼굴·상체 기울기·손에 든 물건)만** 바뀐다. 손에 든 물건은 세 장 모두 같은 모양·같은 크기. 서로 겹치거나 칸(가로 3등분)을 넘지 않는다. 다른 사람·배경·바닥 그림자는 없다.")
    L.append("4. **검사 (기준 그림·동작 그림·물속 그림·소품 필수, 올리기 전에):** 파이썬으로 아래 코드를 돌려 `OK` 가 나와야 올린다. `잘림`·`칸 넘음`·`아래 끝 높이 다름`이면 고쳐서 다시 만든다 (더 작게 · 여백을 넓게 · 발이나 물 높이 선을 같은 선에). **투명이 아니면 배경을 순자홍 #FF00FF 한 색 평면으로 다시 만든다.**")
    L.append(CHECK_CODE)
    L.append("5. **글자·숫자·로고·워터마크를 하나도 넣지 않는다** — 버튼·간판·화면·휴대전화·서류·카드·여권·제복·비행기 몸체에도 없음 (빈 판이나 단순한 줄·도형만). 실제 항공사·은행·통신사·앱의 이름·로고·색 조합을 닮게 그리지 않는다. 해·새·내리는 비나 눈 줄은 그리지 않는다. 만든 뒤 확대해 글자가 보이면 다시 만든다.")
    L.append("   **위험은 차분히, 사람은 나쁘게 그리지 않는다** — 연기·어두운 틈·깨진 얼음·찬물·멀리 보이는 불빛은 되지만 피·다친 몸·떨어지거나 쓰러진 사람·몸에 붙은 불·위험에 빠진 아이는 그리지 않는다. 놀라거나 걱정하는 얼굴은 되지만 무섭게 소리치거나 때리는 괴물처럼은 그리지 않는다. 사기범은 그리지 않는다.")
    L.append(f"6. 그림 바로 위에 번호와 저장 경로를 한 줄 적는다 (`1. {rel_path(ep, items[0][0], items[0][1])}`). 그림 안에는 쓰지 않는다.")
    L.append("7. **다 만들면 저장소에 넣는다 — 저장 경로 그대로.**")
    L.append(f"   - 저장소 `{REPO}` main 브랜치, 경로는 표의 파일 이름 그대로 (대소문자·하이픈까지 같게 — 배경은 `crisis/source/{ep}/puppet/`, 기준·동작·물속·소품은 `crisis/source/{ep}/puppet/motion/`, 썸네일 그림은 `crisis/source/{ep}/images/`).")
    L.append("   - **올리기 전에 700KB 이하로 만든다** — GitHub 앱은 약 768KB 를 넘는 파일을 잘라 올려 그림이 깨진다. 올린 뒤 GitHub 의 파일 크기(바이트)가 내 파일과 같은지 확인하고, 다르면 다시 올린다.")
    L.append("     - 배경·썸네일(JPEG): RGB · 크기 1536×864 그대로 · 품질 90부터 5씩 낮춰 700KB 아래가 될 때까지 저장.")
    L.append("     - 기준·동작·물속·소품(PNG, 투명 유지): 아래 코드 그대로.")
    L.append(SAVE_CODE)
    L.append(f"   - **GitHub 앱으로 장마다 커밋한다.** 커밋 메시지: `[crisis] {ep} <파일 이름> 이미지` (예: `[crisis] {ep} {items[0][1]}.png 이미지`). 다 올리면 올린 파일 경로와 커밋 링크를 목록으로 적는다.")
    L.append("   - **올리기가 실패한 장만** (권한·연결 오류) 그림을 번호 순서대로 한 번 더 보여 준 뒤 이 문장을 그대로 쓴다: **\"올리지 못한 그림을 이 순서대로 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 각 저장 경로에 올립니다.\"**")
    L.append("")
    L.append(f"## 공통 화풍 (1~{n}번 모든 프롬프트 맨 앞에 그대로 붙임 — 기준 그림과 같은 그림체)")
    L += ["", "```", STYLE, "```", ""]
    L.append("## 배경판 (배경 — 공통 화풍 다음에 그대로 붙임)")
    L += ["", "```", PLATE, "```", ""]
    L.append("## 인물 (기준 그림·동작 그림·물속 그림·썸네일 — 공통 화풍 다음에 그대로 붙임)")
    L += ["", "```", "CHARACTERS — draw each person exactly like their reference sheet (pictures " + ", ".join(str(num[r[1]]) for r in refs) +
          "); a person without a reference sheet must look exactly like the first picture of them made in this chat. "
          "The same face, hair, clothes, colors and proportions in every picture:", spec["people"], "```", ""]
    L.append("## CUTOUT (기준 그림·동작 그림·물속 그림·소품 — 그다음에 그대로 붙임 · 배경·썸네일에는 붙이지 않음)")
    L += ["", "```", CUTOUT, "```", ""]
    L.append("## 기준 시트 (기준 그림 — CUTOUT 다음에 그대로 붙임)")
    L += ["", "```", TURN, "```", ""]
    L.append("## MOTION STRIP (동작 그림 — CUTOUT 다음에 그대로 붙임)")
    L += ["", "```", MOTION, "```", ""]
    if has_water:
        L.append("## IN-WATER STRIP (물속 그림 — CUTOUT 다음에 그대로 붙임)")
        L += ["", "```", WATER, "```", ""]
    L.append("## 썸네일 (썸네일 그림 — 인물 다음에 그대로 붙임)")
    L += ["", "```", THUMB, "```", ""]
    for i, (kind, name, what, lines, prompt) in enumerate(items, 1):
        path = rel_path(ep, kind, name)
        L.append(f"## {i}. {name} — {what}")
        L.append("")
        L.append(f"**저장 경로: `{path}`** — {KIND_INFO[kind]}")
        L.append("")
        if kind == "ref":
            who = name.split("-")[0]
            body = f"Draw {who} only. " + (prompt or f"This is {who}, the main person of this video.")
        else:
            body = prompt
        L += ["```", body, "```", ""]
    L.append("## 받은 뒤 (Claude)")
    L.append(f"- main 의 `crisis/source/{ep}/puppet/`·`images/` 를 가져와 {n}장을 확대해 검수: 기준 그림과 같은 사람인지 · 그림 속 글자·로고 없음 · 세 장의 발(물 높이) 선·크기·옷이 같은지 · 손에 든 물건이 세 장에서 같은지 · 배경판의 빈 자리(앞 가운데 바닥 · 빈 식탁 · 빈 얼음 구멍)가 글대로인지 · 피해자·다친 사람·아이를 위험하게 그리지 않았는지.")
    L.append("- 만스피 편 `puppet/slice.py`(v1.2) · 심리 `psychology/source/puppet_slice.py` 를 바탕으로 동작 시트를 같은 인물 키 기준으로 잘라 `cut/` 에 · 소품 4 · 배경 앞 물건 FG(식탁 앞판 · 얼음 구멍 앞 가장자리 — 배경 그림의 있는 픽셀만).")
    L.append(f"- 장면 파일 `video/episodes/{ep}/index.html` (만스피 v3.1 엔진 — 원화 바꿔 끼우기 · 세계 층 카메라 · 영역 표 `window.ZONES`) → 오디오(`narration.mp3`)가 생기면 `render.mjs check` · `layout-check` · `zone-check --every 0.25` 문제 0 → 렌더 → 완성 mp4 를 직접 봄.")
    L.append("- 썸네일 = `images/TH-CHAR.jpg` + 문구는 코드(`video/render/thumb.mjs` · `thumbnails/thumbnail_N.json` — 1 본안 · 2 보조 문구 없음 · 3 강조 색 바꿈), 보조 문구는 사람을 가리지 않는 머리 옆 빈 자리에.")
    L.append("")
    return "\n".join(L)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true", help="쓰지 않고 장 수·경로만")
    ap.add_argument("--only", help="한 편만 (영상ID)")
    a = ap.parse_args()
    logging.basicConfig(level=logging.INFO, format="[%(name)s] %(message)s")
    log.info("version=%s ref_commit=%s episodes=%d", VERSION, REF_COMMIT[:8], len(EPISODES))
    for f in ("puppet/V-CALM.png", "puppet/motion/V04.png", "puppet/motion/V16.png", "puppet/BG-NIGHT.jpg",
              "puppet/BG-STUDIO.jpg", "images/TH-CHAR.jpg"):
        p = ROOT / "stock" / "source" / "manspi-jeonmang-2026-11" / f
        if not p.exists():
            log.warning("그림체 기준 그림이 이 작업 사본에 없음 path=%s — REF_COMMIT 주소가 맞는지 확인", p.relative_to(ROOT))
    total = 0
    for ep, spec in EPISODES.items():
        if a.only and ep != a.only:
            continue
        script = ROOT / "crisis" / "source" / ep / f"{ep}.txt"
        if not script.exists():
            log.error("대본 없음 ep=%s path=%s — 영상ID 를 확인하세요", ep, script)
            return 1
        names = [it[1] for it in spec["items"]]
        if len(set(names)) != len(names):
            log.error("파일 이름 겹침 ep=%s", ep)
            return 1
        for kind, name, _w, _l, prompt in spec["items"]:
            if kind not in KIND_INFO:
                log.error("모르는 종류 ep=%s name=%s kind=%s", ep, name, kind)
                return 1
            if kind != "ref" and not prompt.strip():
                log.error("프롬프트 비어 있음 ep=%s name=%s", ep, name)
                return 1
        kinds = {k: sum(1 for it in spec["items"] if it[0] == k) for k in KIND_INFO}
        total += len(names)
        log.info("ep=%s images=%d %s", ep, len(names), kinds)
        if a.check:
            continue
        out = ROOT / "crisis" / "source" / ep / "images_chatgpt.md"
        out.write_text(build(ep, spec), encoding="utf-8")
        log.info("wrote %s bytes=%d", out.relative_to(ROOT), out.stat().st_size)
    log.info("total_images=%d", total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
