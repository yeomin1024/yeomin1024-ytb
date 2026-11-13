# VERSION: v1.0 — 2026-11-13 — 심리 네 편 그림 요청 파일(ChatGPT용) 만들기 — 만스피 편과 같은 꼴(만화 배경판 + 3장 동작 원화 + 소품 + 썸네일 그림)
"""심리 네 편의 ChatGPT 그림 요청 파일 `psychology/source/<영상ID>/images_chatgpt.md` 를 만든다.

사용자 지시 2026-11-13 "만스피 영상처럼 영상 만들거니까 챗지피티한테 만들 이미지 생성 명령 알려줘".
꼴은 주식 만스피·반등 편 요청 파일(`stock/source/bandeung-maesu-2026-11/images_chatgpt_long.md` v1.0, 커밋 fd6301a1c)을 그대로 따름:
  - 배경판(사람 없음 · 앞 가운데 빈 바닥) · 인물 동작 원화 3장(키 → 중간 → 키) · 소품 판 · 썸네일 그림
  - 숫자·카드·자막은 코드가 얹음 → 그림에는 글자 0
  - 그림체는 만스피 편과 같게, 인물은 새로 (만스피 V·E 는 그리지 않음) · 편마다 무대·인물이 다름 (유튜브 반복 콘텐츠 정책)

쓰는 법:  python3 psychology/source/images_build.py            # 네 편 모두 다시 씀
          python3 psychology/source/images_build.py --check    # 쓰지 않고 장 수·경로만 출력
※ 연구·교육용 영상 소스 — 심리 진단·치료가 아니다.
"""
import argparse
import logging
import pathlib
import sys

VERSION = "v1.0"
DATE = "2026-11-13"
ROOT = pathlib.Path(__file__).resolve().parents[2]
REPO = "yeomin1024/yeomin1024-ytb"
# 만스피 편 그림체 기준 (main 커밋 고정 주소 — 2026-11-13 확인: 파일이 그 커밋에 있음)
REF_COMMIT = "92f5b034c8adc7c10d5d66ddd7cbba4cc0057eeb"
REF_BASE = f"https://raw.githubusercontent.com/{REPO}/{REF_COMMIT}/stock/source/manspi-jeonmang-2026-11"

log = logging.getLogger("images_build")

# ── 공통 블록 (반등 편 v1.0 과 같은 말 — 검증된 문장) ─────────────────────────────
STYLE = (
    "STYLE: Match exactly the art style of the reference pictures (style only — do NOT draw the people in them): "
    "a polished flat 2D cartoon illustration with bold clean dark outlines, flat colors with one simple cel-shading tone "
    "and small highlights, warm cozy lighting mixed with cool blue screen or night glow, expressive faces (big eyes, clear "
    "eyebrows, open mouths, tears when sad) and easy-to-read body language for a small phone screen. Slightly chunky "
    "proportions (head about one quarter of the body height). Warm, gentle and emotionally honest mood — no horror, no "
    "violence, nobody is a monster or a villain. It is a 2D drawing — not a 3D render, not clay or plastic, not a photo. "
    "Absolutely no text, letters, numbers, logos or watermarks anywhere — signs, menus, boards, screens, papers, books, "
    "phones, clocks and packages are blank or show only simple lines and shapes. No sky, no sun, no clouds, no falling "
    "rain lines."
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
TURN = (
    "CHARACTER REFERENCE SHEET: landscape 1536x1024, three equal invisible columns, the SAME person three times standing "
    "relaxed with a calm, kind face: column 1 front view, column 2 three-quarter view facing left, column 3 pure side view "
    "facing left. Same scale, feet on the same invisible baseline at about 92% of the canvas height, standing adult about "
    "70% of the canvas height (a child smaller in the same scale). This sheet defines this person for every later picture."
)
THUMB = (
    "THUMBNAIL PICTURE for a video cover: full-bleed landscape 1536x864, a complete scene with background (NOT a cutout). "
    "The people and their faces sit in the upper 62% of the picture; the bottom 35% is a calm, simple, darker surface "
    "(table, floor or wall) where large title text will be added later by code — nothing important there. Leave one "
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
       if feet:                                  # 동작 그림: 세 사람의 발바닥 높이가 같아야 함
           bottoms = []
           for c in range(cols):
               ys_c = np.where(m[:, w * c // cols:w * (c + 1) // cols].any(axis=1))[0]
               bottoms.append(ys_c.max() / h)
           if max(bottoms) - min(bottoms) > 0.02: bad.append(f"발 높이 다름 {[round(v, 3) for v in bottoms]}")
       print(path, "OK" if not bad else f"다시 — {bad}", [round(float(v), 3) for v in box])
       return not bad
   # 기준 그림·동작 그림: check(경로, cols=3, feet=True) · 소품 판: check(경로, cols=4, margin=0.02)
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

# ── 편마다 ───────────────────────────────────────────────────────────────────
# kind: ref(기준 그림 3면) · bg(배경판) · motion(동작 3장) · props(소품 4) · thumb(썸네일 그림)
EPISODES = {
    "geureut-moa-2026-11": {
        "title": "식당에서 그릇 모아 두는 사람, 심리학적 특징 3가지",
        "script": "대본 v1.9 (110줄)",
        "thumb_text": "「식당 그릇 모아 두는 사람 / 의외의 속마음」 + 보조 「\"안 치우면 거슬려서요\"」",
        "stages": "동네 한식당 · 강연 끝난 작은 강의실 · 서재(빈 코르크판) · 집 부엌",
        "people": (
            "G — the main person: an ordinary, tidy Korean woman around 50, short neat dark-brown bob with a few gray strands, "
            "small gold stud earrings, a soft lavender knit cardigan over a white round-collar blouse, navy slacks, gray "
            "flat shoes. A warm, thoughtful face that shows small feelings clearly (unease, relief, care).\n"
            "H — her husband: a Korean man around 55, short graying hair, round black-rimmed glasses, a relaxed gray "
            "sweatshirt and dark-blue track pants, house slippers. Easygoing, a little sheepish, never lazy-looking or mean.\n"
            "S — a restaurant server: a friendly Korean woman in her twenties, hair tied back, a plain black apron (no logo) "
            "over a white T-shirt, black trousers, sneakers."
        ),
        "items": [
            ("ref", "G-REF", "G 기준 그림 (앞 · 4분의 3 · 옆)", "전체", ""),
            ("bg", "BG-RESTAURANT", "동네 한식당 · 앞쪽에 가로로 긴 나무 식탁", "2~16 · 22~24 · 31~46 · 103~109",
             "A small, homely Korean neighborhood restaurant at lunchtime, front view from across a table. In the FRONT, a "
             "wooden dining table runs across the whole width of the picture: its top surface is visible as a wide flat "
             "band from about 70% to 82% of the picture height, completely EMPTY (dishes will be added later), its front "
             "edge and front panel fill the bottom of the picture. A character will sit BEHIND this table in the middle, "
             "visible from the chest up. Behind: a warm cream wall with a few blank wooden menu boards (no writing), two "
             "warm pendant lamps, a kitchen pass-through window at the back right with soft steam, a few other empty tables "
             "softly out of focus at the left. Warm daylight, homely and calm."),
            ("bg", "BG-HALL", "강연이 끝난 작은 강의실 · 의자들", "27~28 · 37~38 · 50~55",
             "A small community lecture room just after a talk ended, seen from the side-back. Rows of simple wooden "
             "folding chairs: in the left rows the chairs are pushed in neatly in straight lines, in the right rows a few "
             "chairs are left pulled out at angles. A small empty podium at the far back, a blank light wall screen above "
             "it (empty). Soft afternoon light from tall windows on the left (only the window frames and light, no sky). "
             "The front-center floor (wooden floor) is open and empty where a character will stand."),
            ("bg", "BG-STUDY", "서재 · 가운데 큰 빈 코르크판", "19~21 · 56~64",
             "A cozy home study, front view. In the CENTER of the back wall, one very large EMPTY cork board in a simple "
             "light-wood frame, its top near 10% and its bottom near 55% of the picture height, from about 22% to 78% of "
             "the width — completely empty (no pins, no papers, no lines). A low bookshelf on the left with plain colored "
             "book spines (no labels), a green potted plant and a warm floor lamp on the right. Warm afternoon light, calm "
             "and thoughtful mood. The front-center wooden floor is open and empty."),
            ("bg", "BG-KITCHEN", "집 부엌 · 개수대와 작은 식탁", "72~100",
             "A bright, lived-in Korean apartment kitchen in the evening, front view. Along the back wall: a white "
             "counter with a stainless sink on the left part, a drying rack with a few plates, warm under-cabinet lights, "
             "the wall above the counter plain and empty. On the right: a small round dining table with two chairs and a "
             "little vase. The front-center "
             "tiled floor is open and empty where characters will stand. Warm cozy evening light."),
            ("motion", "G01", "G: (앉아서) 왼쪽 그릇을 끌어옴 → 두 손을 가운데로 모음 → 손을 내려놓고 흐뭇", "2~3 · 9 · 18~24 · 104",
             "G, sitting on a plain low wooden stool (the same stool in all frames, part of the cutout), seen from the "
             "front, both forearms forward at the height of an invisible table top in front of her. Frame 1: leaning "
             "slightly, both hands reaching to her left as if sliding a bowl toward her, focused face. Frame 2: both hands "
             "together in front of her chest-low, as if stacking bowls neatly, small concentrated pout. Frame 3: hands "
             "resting flat and relaxed, shoulders down, a small satisfied smile."),
            ("motion", "G02", "G: (앉아서) 일어나려다 → 뒤돌아 식탁을 보며 찜찜 → 다시 앉아 손을 뻗음", "11 · 49 · 65~66 · 106",
             "G, sitting on the same plain low wooden stool, three-quarter view facing right. Frame 1: she starts to stand "
             "up, hands on her knees, her handbag strap on one shoulder. Frame 2: half-risen, she glances back down at the "
             "table area in front of her with an uneasy, twitchy frown, one eyebrow raised. Frame 3: seated again, "
             "reaching one hand forward to tidy something, a slightly sheepish but relieved face."),
            ("motion", "G03", "G: (앉아서) 직원 쪽을 보며 배려 → 모은 그릇을 식탁 끝으로 밂 → 끄덕이며 미소", "10 · 31~35 · 46 · 105",
             "G, sitting on the same plain low wooden stool, three-quarter view facing right. Frame 1: she looks to the "
             "right with a gentle, caring face, as if noticing a busy server. Frame 2: both hands push forward and to the "
             "right at table height, as if sliding a neat stack of dishes to the table edge. Frame 3: hands back on her lap, "
             "a warm small smile and a little nod."),
            ("motion", "G04", "G: 걷다가 풀린 신발 끈을 봄 → 쪼그려 앉아 묶음 → 일어나 홀가분", "67~68",
             "G, pure side view facing right, outdoors walking clothes are the same as always. Frame 1: standing mid-step, "
             "looking down at her right shoe whose lace is untied and trailing, a bothered frown. Frame 2: crouching down "
             "low in place, tying the shoelace with both hands, concentrating. Frame 3: standing tall again, both laces "
             "tied, a light relieved smile, shoulders relaxed."),
            ("motion", "G05", "G: 컵을 씻으려다 → 내려놓고 손이 머뭇 → 숨 고르며 편안", "79~83",
             "G, front three-quarter view, standing. Frame 1: holding a clear drinking glass in her right hand, about to "
             "wash it, reaching toward something on her left. Frame 2: she has put the glass down (no glass now), both "
             "hands hovering in front of her, fingers twitching, uneasy face looking at where the glass was. Frame 3: "
             "hands lowered and relaxed, eyes softly closed, taking a calm breath, a small peaceful smile."),
            ("motion", "G06", "G: 허리에 손 · 한숨 → 팔짱 끼고 서운 → 손바닥 펴고 차분히 의논", "86~99",
             "G, three-quarter view facing right, standing, at home. Frame 1: hands on her hips, a tired sigh, mouth "
             "puffed, eyebrows tilted ('why only me'). Frame 2: arms crossed, looking down to the side, hurt and sulky. "
             "Frame 3: arms open, one palm up at chest height, calm friendly face, mouth open as if proposing a plan."),
            ("motion", "G07", "G: 왼쪽 판을 검지로 가리킴 → 카메라를 보며 손바닥 펴고 말함 → 같은 자세 입 다묾", "19~21 · 56~64 · 102~109",
             "G, three-quarter view, her body facing slightly to the left of the picture, calm and focused. Frame 1: her "
             "left arm raised, pointing with the index finger up and to the LEFT (toward a board out of frame), looking "
             "where she points, mouth closed. Frame 2: she turns her head to look at the viewer, the left hand now held "
             "open at chest height palm up, explaining, mouth open as if talking. Frame 3: exactly like frame 2 but with "
             "her mouth closed (for lip-sync)."),
            ("motion", "S01", "S: 그릇 쟁반을 들고 바쁨 → 행주로 식탁을 닦음 → 손바닥 펴고 공손히 웃으며 말함", "32~33 · 40~43",
             "S, three-quarter view facing left, standing. Frame 1: carrying a wide round tray with a few stacked empty "
             "bowls at chest height with both hands, walking-busy face, a drop of sweat. Frame 2: the tray is gone; she "
             "bends slightly forward wiping with a folded white cloth in her right hand at table height. Frame 3: standing "
             "up straight, the cloth in her left hand, her right palm open toward the left in a polite 'it's okay' "
             "gesture, a kind smile, mouth open as if talking."),
            ("motion", "H01", "H: 편히 휴대전화를 봄 → 눈치채고 뒷머리 긁음 → 손바닥 펴고 진지하게 말함", "87 · 90~95",
             "H, three-quarter view facing left, standing relaxed at home. Frame 1: looking at a smartphone in his right "
             "hand (blank screen), relaxed, slightly smiling. Frame 2: he looks up to the left, noticing someone, awkward "
             "face, scratching the back of his head with his left hand, the phone lowered. Frame 3: the phone in his pocket "
             "(not visible), both palms open at chest height, earnest face, mouth open as if saying 'I'll do it later, I "
             "promise'."),
            ("props", "PROPS-A1", "소품 4: 밥공기 · 반찬 접시 · 숟가락·젓가락 · 구긴 휴지", "2~3 · 18~24 · 41",
             "Prop sheet, landscape 1536x1024, four equal invisible columns, one prop centered in each column, all at a "
             "similar visual size, each fully inside its column, seen from slightly above: (1) an empty white ceramic rice "
             "bowl with a few rice grains left inside; (2) a small round white side-dish plate with a little leftover red "
             "kimchi; (3) a stainless steel Korean spoon and a pair of flat stainless chopsticks lying side by side; (4) a "
             "crumpled white paper napkin."),
            ("props", "PROPS-A2", "소품 4: 모아 쌓은 그릇 · 유리컵 · 빈 벽시계 · 나무 접이의자", "24 · 42 · 79~83 · 37 · 50~51",
             "Prop sheet, landscape 1536x1024, four equal invisible columns, one prop centered in each column, all at a "
             "similar visual size, each fully inside its column: (1) a neat stack of three empty white bowls with a spoon "
             "and chopsticks laid straight on top, seen from slightly above; (2) an empty clear drinking glass; (3) a round "
             "white wall clock with only short tick marks — no numbers and NO hands; (4) a simple wooden folding chair, "
             "side view facing right (the same chairs as in the lecture room picture)."),
            ("thumb", "TH-CHAR", "썸네일 그림: 식당에서 그릇을 모으며 멋쩍게 웃는 G · 뒤에서 놀라 보는 직원 S", "썸네일 · 0초",
             "Inside the same homely Korean restaurant as picture 2. G (left of center, facing slightly right) sits "
             "behind the wooden table, both hands neatly stacking white bowls with spoons laid straight on top; her face "
             "is a funny mix of an awkward, sheepish smile and a twitchy eyebrow, eyes glancing sideways at one single "
             "spoon still lying crooked on the table. Behind her on the right, S stands holding an empty tray, looking at "
             "the neat stack with a surprised, touched face. Empty space at the upper right beside G's head for a speech "
             "bubble. The table front fills the bottom 35% of the picture in a darker warm brown, plain."),
        ],
    },
    "eomma-gibun-2026-11": {
        "title": "엄마 눈치 보며 자란 아이, 커서도 남을 수 있는 5가지",
        "script": "대본 v1.7 (120줄)",
        "thumb_text": "「엄마 눈치 보며 자란 아이 / 커서도 남을 수 있는 5가지」 + 보조 「\"내가 참으면 되지...\"」",
        "stages": "아파트 복도(현관문 앞) · 어린 시절 거실 · 회사 회의실 · 어른이 된 지금의 원룸 · 상담실(빈 화이트보드)",
        "people": (
            "A — the main person, grown up: an ordinary Korean woman around 35, long dark hair in a low ponytail, a small "
            "dark mole under her LEFT eye, a mustard-yellow knit sweater, dark-blue jeans, white sneakers. Gentle, "
            "considerate face that shows worry and relief clearly.\n"
            "C — the SAME person as a 9-year-old girl (clearly A as a child: the same face shape, the same mole under her "
            "LEFT eye, the same dark hair in two short pigtails with red hair ties), a mustard-yellow T-shirt, a denim "
            "skirt, white socks and small sneakers. Sensitive, watchful eyes.\n"
            "M — her mother in those days: a Korean woman around 38, wavy shoulder-length dark hair, a faded pink house "
            "cardigan over a gray T-shirt, beige trousers. A tired, sad but loving face — never angry, never scary."
        ),
        "items": [
            ("ref", "A-REF", "A 기준 그림 (앞 · 4분의 3 · 옆)", "전체", ""),
            ("ref", "C-REF", "C 기준 그림 — A 의 아홉 살 때 (앞 · 4분의 3 · 옆)", "2~5 · 24 · 35 · 47 · 56~57",
             "This is A as a 9-year-old girl: draw C exactly like the description, the same face shape and the same mole "
             "under the LEFT eye as A in picture 1, so anyone can tell they are the same person."),
            ("bg", "BG-CORRIDOR", "저녁 · 아파트 복도 · 닫힌 현관문", "2~5",
             "An evening corridor of an older Korean apartment building, side view along the corridor. On the RIGHT third, "
             "a closed beige metal front door with a plain handle and a small warm light leaking from under the door "
             "(no number plate, no text). The corridor wall has a long window band on the left showing only warm dusk "
             "light glow (no sky drawn — only light), a few potted plants and a folded child's umbrella by the wall. "
             "The front-center corridor floor (light gray tiles) is open and empty where a child will stand. Calm, slightly "
             "lonely evening mood."),
            ("bg", "BG-OLDHOME", "어린 시절 거실 (따뜻한 옛집)", "3~4 · 21~26 · 35~36 · 47~48 · 56~57 · 75",
             "A warm, slightly old-fashioned Korean family living room in the evening, front view. On the LEFT third, a "
             "soft brown fabric sofa with two cushions (empty); in front of it a low wooden table with a cup of tea. A "
             "wooden cabinet with a small boxy TV (screen off, dark) on the right, a floor cushion, a framed picture on the "
             "wall that shows only soft color shapes. Warm yellow lamp light. The front-center floor (warm wooden floor "
             "with a simple rug) is open and empty."),
            ("bg", "BG-MEETING", "회사 회의실", "33 · 43~51",
             "A modern office meeting room, front view: a long light-wood meeting table seen from its end, running from "
             "the middle toward the back, with a few empty chairs on both sides and two closed laptops (blank lids, no "
             "logos), a blank whiteboard on the back wall, glass walls on the right with soft blurred office lights "
             "behind. The front-center floor (gray carpet) in front of the table end is open and empty where a character "
             "will stand. Neutral, slightly tense daytime light."),
            ("bg", "BG-MYROOM", "어른이 된 지금 · 작은 원룸 (주말 아침)", "54~78 · 90~110",
             "A small, tidy one-room apartment of a woman in her thirties, on a quiet weekend morning, front view. On the "
             "LEFT, a single bed with a light-gray blanket; on the RIGHT, a small desk with a desk lamp, a mug and a "
             "closed notebook, a coat rack with a mustard scarf. A window with sheer curtains glowing with soft morning "
             "light (no sky drawn). The front-center wooden floor is open and empty. Soft, quiet, a little lonely but warm."),
            ("bg", "BG-COUNSEL", "상담실 · 가운데 큰 빈 화이트보드", "6~19 · 27~30 · 59 · 112~119",
             "A warm, calm counseling room, front view. In the CENTER of the back wall, one very large EMPTY whiteboard in "
             "a thin light-wood frame, its top near 10% and its bottom near 55% of the picture height, from about 22% to "
             "78% of the width — completely empty. Two soft armchairs angled at the left and right edges, a small side "
             "table with a tissue box (blank) and a green plant, warm wall lamps. The front-center floor (soft beige "
             "carpet) is open and empty."),
            ("motion", "C01", "C: 현관 손잡이를 잡고 귀를 댐 → 밝은 목소리에 안도 → 가라앉은 목소리에 걱정", "2~3",
             "C, pure side view facing RIGHT, standing close to an invisible door on the right, her school backpack on. "
             "Frame 1: her right hand on an invisible door handle at her shoulder height, her ear leaning toward the right, "
             "listening carefully, eyes wide and holding her breath. Frame 2: same pose, her face relaxes into a relieved "
             "small smile, shoulders down. Frame 3: same pose, her face falls into worry, eyebrows up and together, "
             "shoulders raised, lips pressed."),
            ("motion", "C02", "C: 엄마 곁에서 귀 기울임 → 손을 뻗어 토닥 → '내가 뭘 잘못했지' 손가락을 꼼지락", "3~4 · 24 · 47",
             "C, three-quarter view facing LEFT, standing. Frame 1: leaning forward a little with both hands on her knees, "
             "listening attentively and seriously to someone on the left. Frame 2: reaching her right hand forward to the "
             "left at shoulder height as if gently patting someone's arm, a caring, grown-up look. Frame 3: hands together "
             "in front of her, fingers fidgeting, eyes looking down, worried face as if thinking 'did I do something wrong?'."),
            ("motion", "C03", "C: 말하려고 입을 엶 → 입을 꾹 다묾 → 억지로 웃으며 주먹을 쥠", "56~57",
             "C, front view, standing. Frame 1: she opens her mouth to say something, one hand slightly raised, hopeful "
             "eyes. Frame 2: she presses her lips tightly together, eyes looking down, the raised hand lowered. Frame 3: a "
             "forced bright smile while both small hands are clenched into fists at her sides, eyes a little teary."),
            ("motion", "M01", "M: (앉은 자세) 고개 숙여 한숨 → 이마를 짚음 → 지친 얼굴로 옅은 미소", "3~4 · 35 · 48",
             "M, sitting on an invisible sofa seat (no sofa drawn), feet on the floor, front three-quarter view facing "
             "right. Frame 1: head down, a long sigh, shoulders slumped, hands on her lap. Frame 2: her left hand on her "
             "forehead, eyes closed, tired face. Frame 3: she looks up to the right with a tired but warm small smile, as "
             "if a child just came to her side."),
            ("motion", "A01", "A: 회의실에 들어오며 둘러봄 → '나 때문인가' 곁눈질 → 굳은 웃음", "33 · 37~40",
             "A, three-quarter view facing left, standing, holding a closed laptop against her chest. Frame 1: stepping in, "
             "eyes scanning the room carefully. Frame 2: eyes glancing sideways to the left, a worried face as if thinking "
             "'is it because of me?'. Frame 3: a stiff, polite smile, shoulders a little raised."),
            ("motion", "A02", "A: 손바닥 펴며 '괜찮아요' 억지 웃음 → 서류철을 껴안음 → 높이 쌓인 서류에 지쳐 처짐", "43~50",
             "A, three-quarter view facing left, standing. Frame 1: one palm raised toward the left with a forced 'it's "
             "fine' smile, eyebrows tense. Frame 2: hugging a stack of five document folders (blank covers) against her "
             "chest, smiling weakly. Frame 3: holding a very tall stack of folders up to her chin, knees slightly bent, "
             "exhausted droopy face, a drop of sweat."),
            ("motion", "A03", "A: '너는 괜찮아?'에 놀라 자기를 가리킴 → 가슴에 손 · 멍함 → 혼자 눈물이 맺힘", "54~62 · 64~66",
             "A, front view, standing. Frame 1: surprised blinking, pointing at herself with her right index finger, as "
             "if asked 'are YOU okay?'. Frame 2: her right hand on her chest, a blank, searching look, mouth slightly "
             "open. Frame 3: alone, tears welling up in her eyes, a trembling small smile, hands loosely together."),
            ("motion", "A04", "A: 머그를 들고 쉬지 못해 두리번 → 먼지떨이로 청소 → 지쳐 이마를 닦음", "70~78",
             "A, three-quarter view facing right, standing, at home in the same clothes. Frame 1: holding a warm mug in "
             "both hands, but her eyes dart around uneasily, she cannot relax. Frame 2: the mug is gone; she dusts busily "
             "with a feather duster in her right hand. Frame 3: the duster lowered, shoulders slumped, wiping her "
             "forehead with the back of her left hand, exhausted."),
            ("motion", "A05", "A: 왼쪽 누군가에게 휴지를 건넴 → 휴대전화로 일정을 챙김 → 두 손을 자기 가슴에 · 옅은 미소", "80~87",
             "A, three-quarter view facing left, standing. Frame 1: kindly offering a folded tissue with her right hand to "
             "someone out of frame on the left, a caring face. Frame 2: a smartphone at her ear (blank screen) and a small "
             "planner in her other hand, busy organizing for someone else. Frame 3: both hands crossed gently on her own "
             "chest, eyes closed, a soft smile — caring for herself."),
            ("motion", "A06", "A: 작은 수첩에 한 낱말을 적음 → 손바닥 내밀며 정중히 거절 → 가슴에 손 · 안도", "90~96 · 119",
             "A, three-quarter view facing left, standing. Frame 1: writing one short word in a small notebook held in "
             "her left hand, a calm thoughtful face (the page shows only a short line, no letters). Frame 2: the "
             "notebook lowered; her right palm held out politely toward the left, a calm firm face, mouth open as if "
             "saying 'this time it's hard for me'. Frame 3: her hand on her chest, a relieved exhale, a light smile."),
            ("motion", "A07", "A: 왼쪽 판을 검지로 가리킴 → 카메라를 보며 손바닥 펴고 말함 → 같은 자세 입 다묾", "6~19 · 27~30 · 112~119",
             "A, three-quarter view, her body facing slightly to the left of the picture, calm and focused. Frame 1: her "
             "left arm raised, pointing with the index finger up and to the LEFT (toward a board out of frame), looking "
             "where she points, mouth closed. Frame 2: she turns her head to look at the viewer, the left hand now held "
             "open at chest height palm up, explaining, mouth open as if talking. Frame 3: exactly like frame 2 but with "
             "her mouth closed (for lip-sync)."),
            ("props", "PROPS-B", "소품 4: 휴대전화(빈 말풍선) · 서류철 더미 · 작은 수첩과 펜 · 먼지떨이", "34 · 44~50 · 76 · 90~92",
             "Prop sheet, landscape 1536x1024, four equal invisible columns, one prop centered in each column, all at a "
             "similar visual size, each fully inside its column: (1) a smartphone, front view, its screen showing a chat "
             "with three blank rounded message bubbles (no letters, no dots); (2) a tall stack of colorful document "
             "folders with blank covers; (3) a small open pocket notebook with a pen lying across it, the pages blank; (4) "
             "a feather duster with a wooden handle."),
            ("thumb", "TH-CHAR", "썸네일 그림: 문 앞에서 귀 기울이는 어린 C · 오른쪽에 같은 눈치를 보는 어른 A", "썸네일 · 0초",
             "A split-feeling scene in one picture with a soft warm background that blends from an evening apartment "
             "corridor on the left into a modern office on the right. On the LEFT, little C presses her ear to a closed "
             "beige front door, holding her breath, worried eyes. On the RIGHT, grown-up A (the same person) stands "
             "holding a tall stack of folders with a forced polite smile, her eyes glancing sideways with the same "
             "worried look as the child. Both faces clearly visible. Empty space above A's head at the upper right for a "
             "speech bubble. The bottom 35% is a plain darker floor."),
        ],
    },
    "eomma-hasoyeon-2026-11": {
        "title": "엄마 하소연을 혼자 다 받아 주면 안 되는 이유 3가지",
        "script": "대본 v1.9 (118줄)",
        "thumb_text": "「엄마 하소연 다 받아 주면 / 딸 혼자 지칩니다」 + 보조 「\"나 아니면 들어 줄 사람이 없잖아...\"」",
        "stages": "퇴근길 버스 정류장 · 엄마 집 거실 · 딸의 침실(밤) · 가족 식탁 · 도서관 한쪽(빈 판)",
        "people": (
            "D — the main person, the daughter: an ordinary Korean woman around 38, an office worker, straight "
            "shoulder-length dark hair tucked behind one ear, a beige trench coat over a navy top, black trousers, low "
            "black heels, a beige tote bag on her shoulder. A kind, tired face that shows exhaustion, guilt and relief "
            "clearly.\n"
            "MO — her mother: a Korean woman around 65, short permed gray-black hair, a floral blouse under a purple knit "
            "cardigan, gray trousers, reading glasses on a thin chain. Expressive and lonely, loving — never a villain.\n"
            "F — her father: a Korean man around 68, short gray hair, a brown knit vest over a checked shirt, dark "
            "trousers. Quiet and a little awkward, kind."
        ),
        "items": [
            ("ref", "D-REF", "D 기준 그림 (앞 · 4분의 3 · 옆)", "전체", ""),
            ("bg", "BG-BUSSTOP", "퇴근길 · 밤 버스 정류장", "2~5 · 70",
             "A city bus stop on the way home from work at night, side-front view. On the LEFT, a bus shelter with a "
             "plain glass wall, a metal bench and a blank lit advertising panel (completely empty white glow, no text). "
             "Behind, softly blurred shop lights and an office building wall filling the top of the picture (no sky). The "
             "sidewalk floor (gray paving with a yellow curb line) in the front-center is open and empty. Cool night blue "
             "with warm street-lamp light."),
            ("bg", "BG-MOMHOME", "엄마 집 거실", "3 · 14 · 26 · 50 · 98~101",
             "A Korean parents' living room in the evening, front view. On the RIGHT third, a beige leather sofa with a "
             "crocheted cushion (empty); a low table with a bowl of tangerines; a TV cabinet on the left with the TV off "
             "(dark screen), a row of plain photo frames on the cabinet showing only soft color shapes, a big green "
             "potted plant. Warm but quiet lamp light. The front-center floor (wooden floor) is open and empty."),
            ("bg", "BG-DROOM", "딸의 침실 · 밤", "27~29 · 71~78",
             "A small bedroom of a working woman at night, front view. On the LEFT third, a bed with a dark-blue blanket "
             "and a pillow, the edge of the bed facing the viewer; a nightstand with a small warm lamp and a phone "
             "charger cable; a window with closed curtains. The room is dim with warm lamp light and a cool blue tone. "
             "The front-center floor is open and empty."),
            ("bg", "BG-DINING", "가족 식탁", "53~54 · 66",
             "A Korean family dining room at dinner time, front view. A rectangular wooden dining table runs from the "
             "middle toward the back with four chairs, set with a few covered side dishes and a rice cooker on the "
             "counter behind. A warm pendant lamp over the table. The front-center floor in front of the table is open "
             "and empty where two characters will stand on the left and right."),
            ("bg", "BG-LIBRARY", "도서관 한쪽 · 가운데 큰 빈 판", "18~23 · 30~31 · 39~40 · 61~66 · 109~116",
             "A quiet corner of a public library, front view. In the CENTER, one very large EMPTY display board on a "
             "sturdy wooden stand (light cream surface), its top near 10% and its bottom near 55% of the picture height, "
             "from about 22% to 78% of the width — completely empty. Tall bookshelves with plain colored spines (no "
             "labels) on the left and right, a reading lamp glow. The front-center floor (soft green carpet) is open and "
             "empty. Calm, studious warm light."),
            ("motion", "D01", "D: 울리는 휴대전화를 보고 굳음 → 눈 감고 숨 고름 → 전화를 귀에 대고 억지로 밝게", "2 · 70",
             "D, three-quarter view facing left, standing, her tote bag on her shoulder. Frame 1: looking down at a "
             "smartphone in her right hand (blank glowing screen), she freezes, eyes wide, a small gulp. Frame 2: eyes "
             "closed, shoulders lifted, taking a deep breath, the phone held at her chest. Frame 3: the phone at her ear, "
             "a forced bright smile, eyebrows still tense."),
            ("motion", "D02", "D: 전화를 귀에 대고 끄덕임 → 지쳐 목을 주무름 → 끊고 녹초가 되어 처짐", "3~4 · 73",
             "D, three-quarter view facing left, standing, tote bag on her shoulder. Frame 1: phone at her right ear, "
             "nodding patiently, listening. Frame 2: still on the phone, tired eyes, her left hand rubbing the back of her "
             "neck. Frame 3: the call is over; the phone hangs loosely in her lowered hand, shoulders slumped, head "
             "drooping, completely drained face."),
            ("motion", "MO01", "MO: 전화하며 손을 저으며 하소연 → 볼에 손 · 한숨 → 밝아진 얼굴로 웃음", "3~5 · 26 · 50",
             "MO, three-quarter view facing right, standing, a smartphone at her left ear. Frame 1: talking upset, her "
             "right hand waving in the air, eyebrows knit, mouth open complaining. Frame 2: her right hand on her cheek, a "
             "long sigh, sad eyes. Frame 3: her face brightened, a relieved, cheerful smile, still on the phone."),
            ("motion", "D03", "D: 무거운 자루를 가방에 넣음 → 무거운 가방에 몸이 기욺 → 가방을 멘 채 지쳐 서 있음", "33~34",
             "D, three-quarter view facing right, standing. Frame 1: she lifts a heavy tied burlap sack with both hands "
             "and puts it into her open beige tote bag, straining. Frame 2: the tote bag on her shoulder is now bulging and "
             "heavy, her body leans to that side, a strained face. Frame 3: standing still with the heavy bag still on "
             "her shoulder, too tired to put it down, eyes half closed."),
            ("motion", "D04", "D: (침대 끝에 앉은 자세) 꺼진 휴대전화를 바라봄 → 머리를 감쌈 → 무릎을 안고 잠 못 듦", "28~29 · 72",
             "D in loose gray pajamas (same hair and face), sitting on an invisible bed edge (no bed drawn), feet on the "
             "floor, front view. Frame 1: staring at a dark phone in both hands, a worried face, as if her mother's words "
             "keep replaying. Frame 2: the phone on her lap, both hands holding her head. Frame 3: hugging her knees to "
             "her chest, eyes open in the dark, sleepless."),
            ("motion", "D05", "D: 왼쪽을 보며 난처 → 오른쪽을 보며 난처 → 양쪽에서 끼인 듯 어깨를 움츠림", "51~54 · 63~67",
             "D, front view, standing. Frame 1: looking to the LEFT with a troubled face, her left hand slightly raised "
             "toward that side. Frame 2: looking to the RIGHT with a troubled face, her right hand slightly raised toward "
             "that side. Frame 3: both arms pressed tight against her body, shoulders squeezed up, eyes shut, as if "
             "squeezed from both sides."),
            ("motion", "D06", "D: 아빠를 피해 팔짱 · 고개 돌림 → 차가운 곁눈질 → 후회하며 팔을 쓸어내림", "53",
             "D, three-quarter view facing right, standing, without her coat (navy top). Frame 1: arms crossed, head "
             "turned away to the left, a cool expressionless face. Frame 2: a cold sidelong glance to the right, lips "
             "tight. Frame 3: looking down, regretful face, her right hand stroking her left upper arm."),
            ("motion", "F01", "F: 접은 신문(빈 종이)을 읽음 → 고개 들어 반갑게 웃음 → 서운한 듯 어리둥절", "53 · 66",
             "F, three-quarter view facing left, standing. Frame 1: reading a folded newspaper (only blank gray lines, no "
             "letters) held in both hands, calm. Frame 2: lowering the paper, looking up to the left with a warm, happy "
             "greeting smile. Frame 3: the smile gone, a puzzled and slightly hurt face, eyebrows up."),
            ("motion", "D07", "D: 울리는 전화를 뒤집어 놓음 → 나중에 문자 → 가슴에 손 · 죄책감", "71~72",
             "D, three-quarter view facing right, standing. Frame 1: turning a ringing smartphone face down in her right "
             "hand, looking away, tense. Frame 2: typing a short text with both thumbs, a guilty, hesitant face. Frame 3: "
             "the phone lowered, her left hand on her chest, sad eyebrows, guilt."),
            ("motion", "D08", "D: 통화하며 검지를 세움(끝나는 때) → 가슴에 손 · 공감 끄덕 → 손바닥 펴고 차분하고 단단히", "81~97 · 117",
             "D, three-quarter view facing left, standing, a smartphone at her right ear. Frame 1: raising her left index "
             "finger as if saying 'only until dinner', a calm kind face. Frame 2: her left hand on her chest, nodding "
             "with empathy, warm eyes. Frame 3: her left palm open at chest height, a calm, gentle but firm smile."),
            ("motion", "MO02", "MO: 놀라 서운 → 팔짱 끼고 돌아섬 → 누그러져 옅은 미소", "98~101",
             "MO, three-quarter view facing right, standing, no phone. Frame 1: surprised and hurt, hand on her chest, "
             "mouth open ('my daughter feels like a stranger'). Frame 2: arms crossed, body turned a little away to the "
             "left, sulking, pouting. Frame 3: arms lowered, softening, a small shy smile."),
            ("motion", "D09", "D: 왼쪽 판을 검지로 가리킴 → 카메라를 보며 손바닥 펴고 말함 → 같은 자세 입 다묾", "18~23 · 30~31 · 61~66 · 109~116",
             "D, three-quarter view, her body facing slightly to the left of the picture, calm and focused, no coat (navy "
             "top). Frame 1: her left arm raised, pointing with the index finger up and to the LEFT (toward a board out "
             "of frame), looking where she points, mouth closed. Frame 2: she turns her head to look at the viewer, the "
             "left hand now held open at chest height palm up, explaining, mouth open as if talking. Frame 3: exactly "
             "like frame 2 but with her mouth closed (for lip-sync)."),
            ("props", "PROPS-C", "소품 4: 울리는 휴대전화 · 묶은 무거운 자루 · 열린 토트백 · 놋쇠 저울", "2 · 33 · 44 · 70",
             "Prop sheet, landscape 1536x1024, four equal invisible columns, one prop centered in each column, all at a "
             "similar visual size, each fully inside its column: (1) a smartphone, front view, its screen glowing plain "
             "green-white with one round blank call button (no letters, no numbers); (2) a heavy, lumpy burlap sack tied "
             "at the top with rope; (3) an open beige canvas tote bag, empty; (4) a simple brass balance scale with two "
             "empty pans, perfectly level."),
            ("thumb", "TH-CHAR", "썸네일 그림: 전화를 귀에 댄 채 무거운 자루를 멘 지친 딸 D", "썸네일 · 0초",
             "At the night bus stop from picture 2. D stands slightly left of center, a smartphone pressed to her ear, a "
             "huge heavy burlap sack on her shoulder pulling her down; her head droops, eyes half closed, eyebrows "
             "drawn together in exhaustion, shoulders sagging, her free hand covering her mouth to hide a sigh. Her face "
             "is clearly visible. Empty space at the upper right beside her head for a speech bubble. The bottom 35% is a "
             "plain dark sidewalk."),
        ],
    },
    "sangcheo-gonggyeok-2026-11": {
        "title": "상처받은 사람이 오히려 공격적이 되는 이유 3가지",
        "script": "대본 v1.7 (112줄)",
        "thumb_text": "「상처받은 사람이 / 오히려 공격적이 되는 이유」 + 보조 「\"왜, 안 어울려?\"」",
        "stages": "회사 탕비실 · 지하철 안 · 사무실 자리 · 밤의 자취방 · 작은 세미나실(빈 화면)",
        "people": (
            "R — the main person: an ordinary Korean man around 32, an office worker, short black hair with a side part, "
            "a NEW teal-blue knit sweater over a white collar shirt, gray slacks, brown shoes. A face that flips quickly "
            "between hurt and sharp — sharp but never violent, and also capable of calm and warmth.\n"
            "K — his coworker and friend: a Korean woman around 30, a chin-length bob with bangs, a coral cardigan over a "
            "cream blouse, beige trousers, a plain blank ID card on a lanyard. Friendly and easygoing.\n"
            "B — their team leader: a Korean man around 48, neat short hair with gray at the sides, a navy blazer over a "
            "light-blue shirt, no tie. Calm and polite, not scary."
        ),
        "items": [
            ("ref", "R-REF", "R 기준 그림 (앞 · 4분의 3 · 옆)", "전체", ""),
            ("bg", "BG-PANTRY", "회사 탕비실", "2~3 · 55~56 · 79 · 93~102",
             "An office pantry / break room, front view. Along the back wall: a counter with a coffee machine (plain, no "
             "logo), a water dispenser, paper cups, a small fridge on the right, a few plain mugs on a shelf, a window "
             "band with soft daylight (no sky drawn). The front-center floor (light gray tiles) is open and empty where "
             "two characters will stand facing each other. Bright, casual daytime light."),
            ("bg", "BG-SUBWAY", "지하철 객차 안", "42~45",
             "Inside a subway train car, side view looking across the car: a long row of empty blue seats along the far "
             "wall under dark windows with soft blurred tunnel lights, metal poles, a row of hanging hand straps from the "
             "ceiling bar across the top, plain blank panels above the windows (no maps, no text). The front-center "
             "floor (gray) is open and empty where a standing passenger will be placed. Cool fluorescent light."),
            ("bg", "BG-OFFICE", "사무실 자리", "31 · 57~59 · 69~71 · 88",
             "An open-plan office, front view: in the middle, a desk with a monitor (screen showing only blurred gray "
             "blocks), a keyboard, a small cactus and a stack of papers; low partitions and other empty desks behind, "
             "softly out of focus; ceiling lights. The front-center floor (gray carpet) in front of the desk is open and "
             "empty where two characters will stand. Neutral daytime light."),
            ("bg", "BG-RROOM", "밤의 자취방", "30 · 33~34 · 78~91",
             "A young man's small studio room at night, front view: on the LEFT, a single bed with a navy blanket; on the "
             "RIGHT, a desk with a laptop (closed), a desk lamp glowing warm, a glass of water; a window with blinds "
             "showing a cool blue night glow (no sky drawn). The front-center floor is open and empty. Quiet, a little "
             "lonely late-night mood."),
            ("bg", "BG-SEMINAR", "작은 세미나실 · 가운데 큰 빈 화면", "19~26 · 35~36 · 49~54 · 62~66 · 72~73 · 105~111",
             "A small seminar room, front view. In the CENTER of the back wall, one very large EMPTY projection screen "
             "(plain light gray, glowing softly), its top near 10% and its bottom near 55% of the picture height, from "
             "about 22% to 78% of the width — completely empty. A few rows of simple chairs seen from behind at the left "
             "and right bottom corners (empty), a small lectern at the side. Calm, cool light. The front-center floor is "
             "open and empty."),
            ("motion", "K01", "K: 웃으며 R 의 옷을 가리킴 → 쏘아붙임에 놀라 눈 깜빡 → 입을 가리고 무안", "3 · 94",
             "K, three-quarter view facing RIGHT, standing. Frame 1: a friendly casual smile, pointing lightly with her "
             "right hand toward someone's sweater on the right, mouth open as if asking 'is that new?'. Frame 2: startled, "
             "blinking, both hands pulled back to her chest. Frame 3: her right hand over her mouth, an awkward, hurt "
             "face, eyes looking down."),
            ("motion", "R01", "R: 덤덤함 → 몸을 내밀며 날카롭게 받아침 → 팔짱 끼고 돌아섬", "3 · 32 · 59 · 68 · 71",
             "R, three-quarter view facing LEFT, standing. Frame 1: a neutral face, hands loosely at his sides. Frame 2: "
             "leaning forward a little, eyebrows sharply down, mouth open in a sharp retort, his right hand open at chest "
             "height (not pointing at anyone, not a fist). Frame 3: arms crossed, body turned a little away, a defensive "
             "sulky frown, looking aside."),
            ("motion", "R02", "R: 휴대전화를 봄 → 답장이 없어 불안 → 화난 얼굴로 빠르게 입력", "30 · 33~34",
             "R, front three-quarter view facing right, standing, at night in the same clothes. Frame 1: looking at a "
             "smartphone in his right hand (blank screen), expecting a reply. Frame 2: anxious, eyebrows up and together, "
             "lips pressed. Frame 3: typing fast with both thumbs, an irritated, angry face."),
            ("motion", "R03", "R: 손잡이를 잡고 섬 → 어깨가 부딪혀 휘청 → 옆을 노려봄", "42~45",
             "R, pure side view facing right, standing, his left hand raised holding an invisible overhead strap (the "
             "hand closed around nothing at the top). Frame 1: standing calmly, a little tired. Frame 2: his body jolted "
             "and leaning, his right shoulder pushed back as if bumped, surprised face. Frame 3: steady again, glaring "
             "angrily over his right shoulder, jaw tight."),
            ("motion", "R04", "R: 왼쪽 상사의 말을 들음 → 움츠러들며 얼굴이 어두워짐 → 방어적으로 받아침", "57~59 · 69~71",
             "R, three-quarter view facing LEFT, standing. Frame 1: listening to someone on the left, holding a document, "
             "neutral. Frame 2: shrinking a little, shoulders up, eyes down, his face darkening with hurt as if he heard "
             "'you are incompetent'. Frame 3: snapping back, eyebrows sharply down, mouth open in a defensive reply, the "
             "document held tight against his chest."),
            ("motion", "B01", "B: 서류의 한 곳을 차분히 가리킴 → 손바닥 펴고 친절히 설명 → 날 선 반응에 놀람", "57",
             "B, three-quarter view facing RIGHT, standing. Frame 1: holding a document in his left hand and pointing "
             "calmly at one spot on it with his right index finger, a neutral helpful face. Frame 2: his right palm open "
             "toward the right, explaining kindly, a gentle smile. Frame 3: eyebrows raised in surprise, leaning back "
             "slightly, both hands lowered, as if caught off guard by a sharp reaction."),
            ("motion", "R05", "R: 얼굴이 달아오르고 주먹에 힘 → 종이컵 물을 마심 → 눈 감고 숨 고르며 차분", "81~84",
             "R, front three-quarter view facing left, standing. Frame 1: face flushed red, eyebrows down, both hands "
             "tense (fists loosely at his sides, not raised), breathing fast. Frame 2: drinking water from a white paper "
             "cup held in his right hand, eyes closed. Frame 3: the cup lowered, eyes closed, a slow deep breath, calm "
             "face, shoulders down."),
            ("motion", "R06", "R: 가슴에 손 · 조용히 속마음을 말함 → 손바닥 펴고 차분 → 미안한 듯 옅은 미소", "85~88",
             "R, three-quarter view facing LEFT, standing. Frame 1: his right hand on his chest, eyes a little down, "
             "speaking softly and honestly, mouth open ('I'm a bit hurt right now'). Frame 2: his right palm open at "
             "chest height, a calm face, mouth open talking. Frame 3: a small, slightly apologetic smile, hands relaxed."),
            ("motion", "R07", "R: 자기 몸을 감싸 쥐고 불안 → 말 한마디에 움찔 → 방어하듯 팔을 들어 막음", "64~71",
             "R, front view, standing. Frame 1: hugging his own arms, shoulders hunched, eyes wavering, insecure. Frame 2: "
             "flinching sharply, eyes squeezed shut, as if a single word hit him. Frame 3: both forearms raised in front "
             "of his chest like a shield (defensive, not attacking), a tense, braced face."),
            ("motion", "K02", "K: 턱에 손 · '내 말이 서운했나' 돌아봄 → 손바닥 펴고 분명히 다시 말함 → 손을 들어 부드럽게 선 긋기", "97~102",
             "K, three-quarter view facing RIGHT, standing. Frame 1: her hand on her chin, thinking back honestly ('did "
             "my words sound hurtful?'). Frame 2: her right palm open toward the right, explaining clearly and kindly, "
             "mouth open. Frame 3: her right hand raised with the palm facing out at shoulder height, a calm, gentle but "
             "firm face — setting a boundary."),
            ("motion", "R08", "R: 왼쪽 화면을 검지로 가리킴 → 카메라를 보며 손바닥 펴고 말함 → 같은 자세 입 다묾", "19~26 · 35~36 · 49~54 · 72~73 · 105~111",
             "R, three-quarter view, his body facing slightly to the left of the picture, calm and focused. Frame 1: his "
             "left arm raised, pointing with the index finger up and to the LEFT (toward a screen out of frame), looking "
             "where he points, mouth closed. Frame 2: he turns his head to look at the viewer, the left hand now held "
             "open at chest height palm up, explaining, mouth open as if talking. Frame 3: exactly like frame 2 but with "
             "his mouth closed (for lip-sync)."),
            ("props", "PROPS-D", "소품 4: 물 담긴 종이컵 · 빨간 동그라미 하나 친 보고서 · 휴대전화 · 뿌연 손거울", "57 · 70 · 81~83 · 30 · 63~68",
             "Prop sheet, landscape 1536x1024, four equal invisible columns, one prop centered in each column, all at a "
             "similar visual size, each fully inside its column: (1) a white paper cup filled with water; (2) a sheet of "
             "report paper with only gray lines (no letters) and ONE small red circle marked around a tiny spot; (3) a "
             "smartphone, front view, blank glowing screen; (4) a small round hand mirror whose glass is foggy and blurred."),
            ("thumb", "TH-CHAR", "썸네일 그림: 탕비실 · 새 스웨터를 묻는 K 와 날카롭게 받아치는 R", "썸네일 · 0초",
             "In the office pantry from picture 2. On the RIGHT, R in his new teal-blue sweater leans forward with a "
             "sharp, angry retort face, eyebrows down, mouth open, but his eyes show hurt; his hand open at chest height "
             "(no fist, no pointing at her). On the LEFT, K holds a paper cup, startled and blinking, leaning back with "
             "a surprised, awkward smile frozen on her face. Both faces clearly visible. Empty space above R's head at "
             "the upper right for a speech bubble. The bottom 35% is a plain darker counter surface."),
        ],
    },
}

KIND_INFO = {
    "ref": ("motion", "PNG 700KB 이하 · 투명 · 가로 1536×1024 · 기준 3면"),
    "bg": ("", "JPEG 700KB 이하 · 가로 1536×864"),
    "motion": ("motion", "PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장"),
    "props": ("motion", "PNG 700KB 이하 · 투명 · 가로 1536×1024 · 소품 4"),
    "thumb": ("", "JPEG 700KB 이하 · 가로 1536×864 · 글자 없음"),
}


def rel_path(ep: str, kind: str, name: str) -> str:
    """저장 경로 — 만스피 편과 같은 폴더 꼴 (배경 puppet/ · 원화·소품 puppet/motion/ · 썸네일 그림 images/)."""
    if kind == "bg":
        return f"psychology/source/{ep}/puppet/{name}.jpg"
    if kind == "thumb":
        return f"psychology/source/{ep}/images/{name}.jpg"
    return f"psychology/source/{ep}/puppet/motion/{name}.png"


def build(ep: str, spec: dict) -> str:
    items = spec["items"]
    n = len(items)
    counts = {k: sum(1 for it in items if it[0] == k) for k in KIND_INFO}
    num = {it[1]: i + 1 for i, it in enumerate(items)}
    refs = [it for it in items if it[0] == "ref"]
    ref_nums = " · ".join(f"{num[r[1]]}번 {r[1]}" for r in refs)
    first_bg = next(i + 1 for i, it in enumerate(items) if it[0] == "bg")
    last_bg = max(i + 1 for i, it in enumerate(items) if it[0] == "bg")
    L = []
    L.append(f"# {ep} 롱폼 — 만화 무대·움직임 그림 {n}장 (ChatGPT용 · 1번부터 차례로 모두)")
    L.append("")
    L.append(f"작성: {VERSION} — {DATE} — 사용자 지시 \"만스피 영상처럼 영상 만들거니까 챗지피티한테 만들 이미지 생성 명령 알려줘\". "
             f"기준 대본 = `psychology/source/{ep}/{ep}.txt` {spec['script']} · 영상 「{spec['title']}」.")
    L.append("")
    L.append("**어떻게 쓰는가 — 주식 만스피 편과 같은 코드 애니메이션**")
    L.append("- Claude 가 코드로 만든다: 배경 그림 위에 인물·소품 조각을 올리고, **동작마다 이어지는 원화 3장**(키 → 중간 → 키)을 초당 8~12장으로 바꿔 끼워 팔·몸·얼굴이 실제로 움직이게 한다. "
             "숫자·연구 카드·자막·말풍선은 그림 속 빈 판·빈 칸 위에 코드가 얹는다 → **그림에는 글자가 하나도 없어야 한다.**")
    L.append(f"- 인물은 **이 편에서 새로** — 만스피 편 사람(곱슬머리 V · 정장 E)은 그리지 않고 그림체만 같게. 첫 그림({ref_nums})이 이 편 인물의 기준.")
    L.append(f"- 무대는 다른 편과 겹치지 않게 ({spec['stages']}) — 유튜브 '반복 콘텐츠' 정책.")
    L.append(f"- 썸네일 그림(마지막 장)은 만스피처럼 **그림만** — 문구 {spec['thumb_text']} 는 Claude 가 코드로 얹는다.")
    L.append("- ※ 연구·교육용 영상 — 심리 진단·치료가 아니다. 엄마·가족·상대를 나쁜 사람으로 그리지 않는다.")
    L.append("")
    L.append(f"| 번호 | 저장 경로 (모두 `psychology/source/{ep}/` 아래) | 무엇 | 대본 줄 |")
    L.append("|---|---|---|---|")
    for i, (kind, name, what, lines, _p) in enumerate(items, 1):
        short = rel_path(ep, kind, name).split(f"{ep}/", 1)[1]
        L.append(f"| {i} | `{short}` | {what} | {lines} |")
    L.append("")
    L.append("## ChatGPT에게 — 이 파일을 읽으면 할 일")
    L.append("0. **이 주소를 지금 새로 열어 그 내용만 쓴다** — 이 대화에서 예전에 읽은 파일·프롬프트(주식 편·실사 사진·종이 인형극 포함)가 있어도 쓰지 않는다. 답의 첫 줄에 이 파일 맨 위 '작성' 줄을 그대로 적는다.")
    L.append("   **★ 먼저 그림체 기준 그림을 열어 본다 — 새 그림은 모두 이 그림들과 같은 사람이 그린 것처럼 (그림체·선 굵기·색·얼굴 꼴·비율). 단, 그 안의 사람(곱슬머리 남자 · 정장 남자)·장소·글자는 따라 그리지 않는다.**")
    L.append(f"   - 인물 그림체 (만스피 편): {REF_BASE}/puppet/V-CALM.png · 동작 시트 {REF_BASE}/puppet/motion/V04.png · {REF_BASE}/puppet/motion/V16.png")
    L.append(f"   - 배경 그림체: {REF_BASE}/puppet/BG-NIGHT.jpg · {REF_BASE}/puppet/BG-STUDIO.jpg")
    L.append(f"   - 썸네일 그림체: {REF_BASE}/images/TH-CHAR.jpg (왼쪽 '-50%' 글자는 따라 그리지 않음)")
    L.append("   그림을 열 수 없으면 아래 '공통 화풍'과 '인물' 설명대로 그린다.")
    L.append(f"   **★ 이 편의 인물은 {ref_nums} 이 기준이다 — 그 뒤 모든 그림의 같은 사람은 기준 그림과 얼굴·머리·옷·색·비율이 똑같아야 한다.** 다르게 나오면 다시 만든다.")
    L.append(f"1. 아래 1~{n}번 **{n}장을 번호 순서대로 모두** 만든다. 질문하지 말고, 한 장을 만든 뒤 멈추지 말고 다음 장으로 넘어간다. 이미지 한도 때문에 멈추면 사용자가 `계속`이라고 보낸다 → 아직 안 만든 번호부터.")
    L.append("2. 프롬프트(``` 안)를 **한 글자도 바꾸지 않고 그대로** 쓰고, 맨 앞에 **공통 화풍** 문단을 붙인다.")
    L.append("   - **기준 그림(ref)**: 공통 화풍 → **인물** → **CUTOUT** → **기준 시트** → 프롬프트(있으면).")
    L.append(f"   - **배경({first_bg}~{last_bg}번)**: 공통 화풍 → **배경판** → 프롬프트.")
    L.append("   - **동작 그림**: 공통 화풍 → **인물** → **CUTOUT** → **MOTION STRIP** → 프롬프트.")
    L.append("   - **소품**: 공통 화풍 → **CUTOUT** → 프롬프트.")
    L.append(f"   - **썸네일 그림({n}번)**: 공통 화풍 → **인물** → **썸네일** → 프롬프트.")
    L.append("3. **동작 그림은 한 장에 같은 사람을 3번** 그린다 — 왼쪽 → 가운데 → 오른쪽이 **한 동작을 이어 그린 3장**(애니메이션 원화)이다. 세 사람이 **같은 크기·같은 자리·같은 방향·같은 옷**이고, **발바닥(앉은 자세는 의자 다리·발)이 같은 높이**에 있고, **움직이는 부분(팔·손·머리·얼굴·상체 기울기·손에 든 물건)만** 바뀐다. 손에 든 물건은 세 장 모두 같은 모양·같은 크기. 서로 겹치거나 칸(가로 3등분)을 넘지 않는다. 다른 사람·배경·바닥 그림자는 없다.")
    L.append("4. **검사 (기준 그림·동작 그림·소품 필수, 올리기 전에):** 파이썬으로 아래 코드를 돌려 `OK` 가 나와야 올린다. `잘림`·`칸 넘음`·`발 높이 다름`이면 고쳐서 다시 만든다 (더 작게 · 여백을 넓게 · 발을 같은 선에). **투명이 아니면 배경을 순자홍 #FF00FF 한 색 평면으로 다시 만든다.**")
    L.append(CHECK_CODE)
    L.append("5. **글자·숫자·로고·워터마크를 하나도 넣지 않는다** — 간판·메뉴판·게시판·화면·휴대전화·서류·책·시계·상자에도 없음 (빈 판이나 단순한 줄·도형만). 실제 가게·회사·앱의 이름·로고·색 조합을 닮게 그리지 않는다. 하늘·해·구름·비 내리는 줄은 그리지 않는다. 만든 뒤 확대해 글자가 보이면 다시 만든다.")
    L.append("   **사람을 나쁘게 그리지 않는다** — 엄마·아빠·배우자·상사·동료는 지치거나 서운하거나 놀란 얼굴은 되지만 무섭거나 때리거나 소리치는 괴물처럼은 그리지 않는다. 폭력·피·약·병원 장면은 그리지 않는다. 아이는 늘 옷을 다 입은 평범한 모습.")
    L.append(f"6. 그림 바로 위에 번호와 저장 경로를 한 줄 적는다 (`1. {rel_path(ep, items[0][0], items[0][1])}`). 그림 안에는 쓰지 않는다.")
    L.append("7. **다 만들면 저장소에 넣는다 — 저장 경로 그대로.**")
    L.append(f"   - 저장소 `{REPO}` main 브랜치, 경로는 표의 파일 이름 그대로 (대소문자·하이픈까지 같게 — 배경은 `psychology/source/{ep}/puppet/`, 기준·동작·소품은 `psychology/source/{ep}/puppet/motion/`, 썸네일 그림은 `psychology/source/{ep}/images/`).")
    L.append("   - **올리기 전에 700KB 이하로 만든다** — GitHub 앱은 약 768KB 를 넘는 파일을 잘라 올려 그림이 깨진다. 올린 뒤 GitHub 의 파일 크기(바이트)가 내 파일과 같은지 확인하고, 다르면 다시 올린다.")
    L.append("     - 배경·썸네일(JPEG): RGB · 크기 1536×864 그대로 · 품질 90부터 5씩 낮춰 700KB 아래가 될 때까지 저장.")
    L.append("     - 기준·동작·소품(PNG, 투명 유지): 아래 코드 그대로.")
    L.append(SAVE_CODE)
    L.append(f"   - **GitHub 앱으로 장마다 커밋한다.** 커밋 메시지: `[psychology] {ep} <파일 이름> 이미지` (예: `[psychology] {ep} {items[0][1]}.png 이미지`). 다 올리면 올린 파일 경로와 커밋 링크를 목록으로 적는다.")
    L.append("   - **올리기가 실패한 장만** (권한·연결 오류) 그림을 번호 순서대로 한 번 더 보여 준 뒤 이 문장을 그대로 쓴다: **\"올리지 못한 그림을 이 순서대로 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 각 저장 경로에 올립니다.\"**")
    L.append("")
    L.append(f"## 공통 화풍 (1~{n}번 모든 프롬프트 맨 앞에 그대로 붙임 — 기준 그림과 같은 그림체)")
    L += ["", "```", STYLE, "```", ""]
    L.append("## 배경판 (배경 — 공통 화풍 다음에 그대로 붙임)")
    L += ["", "```", PLATE, "```", ""]
    L.append("## 인물 (기준 그림·동작 그림·썸네일 — 공통 화풍 다음에 그대로 붙임)")
    L += ["", "```", "CHARACTERS — draw each person exactly like their reference sheet (pictures " + ", ".join(str(num[r[1]]) for r in refs) +
          "); a person without a reference sheet must look exactly like the first picture of them made in this chat. "
          "The same face, hair, clothes, colors and proportions in every picture:", spec["people"], "```", ""]
    L.append("## CUTOUT (기준 그림·동작 그림·소품 — 그다음에 그대로 붙임 · 배경·썸네일에는 붙이지 않음)")
    L += ["", "```", CUTOUT, "```", ""]
    L.append("## 기준 시트 (기준 그림 — CUTOUT 다음에 그대로 붙임)")
    L += ["", "```", TURN, "```", ""]
    L.append("## MOTION STRIP (동작 그림 — CUTOUT 다음에 그대로 붙임)")
    L += ["", "```", MOTION, "```", ""]
    L.append("## 썸네일 (썸네일 그림 — 인물 다음에 그대로 붙임)")
    L += ["", "```", THUMB, "```", ""]
    for i, (kind, name, what, lines, prompt) in enumerate(items, 1):
        path = rel_path(ep, kind, name)
        L.append(f"## {i}. {name} — {what}")
        L.append("")
        L.append(f"**저장 경로: `{path}`** — {KIND_INFO[kind][1]}")
        L.append("")
        if kind == "ref":
            who = name.split("-")[0]
            body = f"Draw {who} only. " + (prompt or f"This is {who}, the main person of this video.")
        else:
            body = prompt
        L += ["```", body, "```", ""]
    L.append("## 받은 뒤 (Claude)")
    L.append(f"- main 의 `psychology/source/{ep}/puppet/`·`images/` 를 가져와 {n}장을 확대해 검수: 기준 그림과 같은 사람인지 · 그림 속 글자 없음 · 세 장의 발 높이·크기·옷이 같은지 · 손에 든 물건이 세 장에서 같은지 · 배경판의 빈 자리(앞 가운데 바닥 · 가운데 빈 판)가 글대로인지 · 사람을 나쁘게 그리지 않았는지.")
    L.append(f"- 만스피 편 `puppet/slice.py`(v1.2)를 바탕으로 동작 시트를 같은 인물 키 기준으로 잘라 `cut/` 에 · 소품 4 · 배경 앞 물건 FG(식탁 앞판 등 — 배경 그림의 있는 픽셀만).")
    L.append(f"- 장면 파일 `video/episodes/{ep}/index.html` (만스피 v3.1 엔진 — 원화 바꿔 끼우기 · 세계 층 카메라 · 영역 표 `window.ZONES`) → 오디오(`narration.mp3`)가 생기면 `render.mjs check` · `layout-check` · `zone-check --every 0.25` 문제 0 → 렌더 → 완성 mp4 를 직접 봄.")
    L.append("- 썸네일 = `images/TH-CHAR.jpg` + 문구는 코드(`video/render/thumb.mjs` · `thumbnails/thumbnail_N.json`), 보조 문구는 사람을 가리지 않는 빈 자리에.")
    L.append("")
    return "\n".join(L)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true", help="쓰지 않고 장 수·경로만")
    ap.add_argument("--only", help="한 편만 (영상ID)")
    a = ap.parse_args()
    logging.basicConfig(level=logging.INFO, format="[%(name)s] %(message)s")
    log.info("version=%s ref_commit=%s episodes=%d", VERSION, REF_COMMIT[:8], len(EPISODES))
    total = 0
    for ep, spec in EPISODES.items():
        if a.only and ep != a.only:
            continue
        script = ROOT / "psychology" / "source" / ep / f"{ep}.txt"
        if not script.exists():
            log.error("대본 없음 ep=%s path=%s — 영상ID 를 확인하세요", ep, script)
            return 1
        nlines = len(script.read_text(encoding="utf-8").splitlines())
        names = [it[1] for it in spec["items"]]
        if len(set(names)) != len(names):
            log.error("파일 이름 겹침 ep=%s", ep)
            return 1
        for kind, name, _w, _l, prompt in spec["items"]:
            if kind != "ref" and not prompt.strip():
                log.error("프롬프트 비어 있음 ep=%s name=%s", ep, name)
                return 1
        kinds = {k: sum(1 for it in spec["items"] if it[0] == k) for k in KIND_INFO}
        total += len(names)
        log.info("ep=%s images=%d %s script_lines=%d", ep, len(names), kinds, nlines)
        if a.check:
            continue
        out = ROOT / "psychology" / "source" / ep / "images_chatgpt.md"
        out.write_text(build(ep, spec), encoding="utf-8")
        log.info("wrote %s bytes=%d", out.relative_to(ROOT), out.stat().st_size)
    log.info("total_images=%d", total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
