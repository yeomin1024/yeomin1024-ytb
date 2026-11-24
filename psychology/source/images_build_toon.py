#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VERSION: v1.1 — 2026-11-24 — 추가 요청 파일(images_chatgpt_add.md): 이미 받은 1번 A-REF 를 그림체 기준으로 몇 장만 더 — 사용자 지시
#          "나는 왜 이렇게 게으를까 부분에 배경이 없는데 내용에 맞는 이미지를 넣고 … 이미지 추가 생성 필요하면 명령 알려주고" (ADD · build_add)
# (v1.0) — 2026-11-23 — 신규: 일상툰 꼴 영상의 ChatGPT 그림 요청 파일 만들기 (사용자 지시 2026-11-23 "그럼 모든 이미지 생성
#          명령 알려줘 지시사항은 저장소에서 읽으라하고 업로드하라고해" · "썸네일 이미지도 만들어 A, B 사람 반반 나눠서 대비되도록")
"""일상툰 꼴 ChatGPT 그림 요청 파일 `psychology/source/<영상ID>/images_chatgpt.md` 를 만든다.

틀은 심리 만스피 꼴 `psychology/source/images_build.py` v1.0 (ChatGPT 에서 검증된 '할 일'·잘림 검사 코드·700KB 저장 코드·
CUTOUT·MOTION STRIP·썸네일 블록)을 그대로 가져오고, 바뀌는 것만 여기 둔다:
  - 그림체 = 일상툰 (둥근 선·파스텔·약 3등신 어른) — 바깥 기준 그림 없이 **1번 A 기준 그림이 그림체 기준**
  - 조연은 '자세 그림'(POSES — 한 장에 대본에 필요한 자세 3개, 이어지는 동작이 아님)으로 장 수를 줄임
  - 반반 화면에 쓰는 배경판은 가운데 절반만 잘라도 되게
  - 썸네일 = 두 사람 반반 대비 (문구는 코드)
그림에는 글자 0 (말풍선·자막·숫자·그래프는 코드).

쓰는 법:  python3 psychology/source/images_build_toon.py            # 요청 파일 다시 씀
          python3 psychology/source/images_build_toon.py --check    # 쓰지 않고 장 수·경로만
※ 연구·교육용 영상 소스 — 심리 진단·치료가 아니다.
"""
import argparse
import logging
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from images_build import CHECK_CODE, CUTOUT, MOTION, SAVE_CODE, THUMB  # noqa: E402 — ChatGPT 에서 검증된 문장 그대로

VERSION = "v1.1"
DATE = "2026-11-24"
ROOT = pathlib.Path(__file__).resolve().parents[2]
REPO = "yeomin1024/yeomin1024-ytb"
log = logging.getLogger("images_build_toon")

# ── 일상툰 공통 블록 ─────────────────────────────────────────────────────────────
STYLE = (
    "STYLE: a simple, warm Korean daily-life webtoon (일상툰) look for a YouTube animation. Rounded simple shapes, thin "
    "clean dark-brown outlines, soft flat pastel colors with at most one light shading tone, very little detail. People "
    "are about 3 heads tall — a little cute but clearly adults (children smaller). Simple faces: small oval eyes, short "
    "eyebrows that carry the emotion, a small mouth; light pink cheeks only when embarrassed or crying. Simple comic "
    "marks are allowed only as shapes (one sweat drop, small sparkle lines, a little gloomy cloud scribble). Expressions "
    "must read instantly on a small phone screen. From picture 2 on, match EXACTLY the drawing style, line weight, colors "
    "and proportions of picture 1. Warm, gentle, emotionally honest mood — no horror, no violence, nobody is a villain. "
    "2D drawing only — not 3D, not a photo, not glossy anime. Absolutely no text, letters, numbers, logos or watermarks "
    "anywhere — screens, phones, papers, books, boards, signs, clocks and packages are blank or show only simple shapes. "
    "Do not imitate any specific existing webtoon or artist."
)
PLATE = (
    "BACKGROUND PLATE for a 2D daily-life webtoon animation: full-bleed landscape 1536x864, eye-level camera, NO people "
    "and no animals anywhere. Simple, clean webtoon background in the same style as the characters: few objects, soft "
    "pastel colors, light outlines. Leave a clear empty area in the front-center where characters will be placed later "
    "(a standing adult there would be about 75% of the picture height, feet near 92% of the height; a sitting person sits "
    "on the furniture described). Keep the middle calm and uncluttered."
)
SPLIT = (
    "SPLIT-SCREEN SAFE: this plate will often be cropped to its central half (from 25% to 75% of the width) for a "
    "side-by-side split screen, so put the furniture the person uses inside that central half."
)
POSES = (
    "POSE SHEET: landscape 1536x1024, three equal invisible columns, the SAME person three times, one pose per column as "
    "described (three separate poses for different scenes — not one continuous movement). Same scale, same clothes and "
    "colors, feet (or the chair legs, when sitting) on the same invisible baseline at about 92% of the canvas height, a "
    "standing adult about 70% of the canvas height. Each figure centered in its column, full body, never crossing a "
    "column border; clear empty space between the columns. This sheet also defines how this person looks in every "
    "later picture."
)
TURN = (
    "CHARACTER REFERENCE SHEET: landscape 1536x1024, three equal invisible columns, the SAME person three times standing "
    "relaxed with a calm, kind face: column 1 front view, column 2 three-quarter view facing left, column 3 pure side view "
    "facing left. Same scale, feet on the same invisible baseline at about 92% of the canvas height, standing adult about "
    "70% of the canvas height. This sheet defines this person for every later picture."
)

KIND_INFO = {   # kind → (폴더, 형식 설명)
    "ref": ("motion", "PNG 700KB 이하 · 투명 · 가로 1536×1024 · 기준 3면"),
    "poses": ("motion", "PNG 700KB 이하 · 투명 · 가로 1536×1024 · 자세 3개"),
    "bg": ("", "JPEG 700KB 이하 · 가로 1536×864"),
    "bgs": ("", "JPEG 700KB 이하 · 가로 1536×864 · 가운데 절반으로 잘라 반반 화면에도 씀"),
    "motion": ("motion", "PNG 700KB 이하 · 투명 · 가로 1536×1024 · 동작 3장"),
    "props": ("motion", "PNG 700KB 이하 · 투명 · 가로 1536×1024 · 소품 4"),
    "thumb": ("", "JPEG 700KB 이하 · 가로 1536×864 · 글자 없음"),
}
ORDER = {"ref": "공통 화풍 → 인물 → CUTOUT → 기준 시트 → 프롬프트",
         "poses": "공통 화풍 → 인물 → CUTOUT → 자세 시트 → 프롬프트",
         "bg": "공통 화풍 → 배경판 → 프롬프트",
         "bgs": "공통 화풍 → 배경판 → 반반 화면 → 프롬프트",
         "motion": "공통 화풍 → 인물 → CUTOUT → MOTION STRIP → 프롬프트",
         "props": "공통 화풍 → CUTOUT → 프롬프트",
         "thumb": "공통 화풍 → 인물 → 썸네일 → 프롬프트"}

EPISODES = {
    "adhd-ab-2026-11": {
        "script": "`psychology/source/adhd-ab-2026-11/대본_초안.txt` v1.0",
        "title": "ADHD 알고 치료한 A씨 vs 모르고 산 B씨",
        "thumb_text": "(제목이 정해지면 Claude 가 코드로 얹음 — 아래 35% 어두운 띠)",
        "people": (
            "A — the main person: a 32-year-old Korean woman, office worker. Shoulder-length dark brown hair in a loose low "
            "ponytail with soft side bangs and a few loose strands. Light blue shirt with sleeves rolled up once, navy "
            "cardigan, dark gray slacks, white sneakers, a plain blank ID badge on a lanyard. Kind, a bit scattered, "
            "relatable; slightly tired eyes when neutral.\n"
            "B — the other main person: a 51-year-old Korean man, office worker and father. Short black hair neatly combed, "
            "gray at the temples, slightly receding hairline, slightly round face with smile lines, a small belly. White "
            "shirt, plain navy tie (loosened or removed at home), gray slacks, black shoes; at home a gray knit cardigan "
            "over the white shirt. Warm but tired, a little stubborn, clearly early 50s.\n"
            "W — B's wife: a 50-year-old Korean woman, short wavy dark hair with a few gray strands, a soft pink blouse, "
            "beige trousers. Tired and hurt, never angry like a monster.\n"
            "S — B's son: a 14-year-old Korean boy, messy short black hair, a plain navy school hoodie, gray pants, "
            "sneakers. Shy and fidgety.\n"
            "T — A's team leader: a 45-year-old Korean woman, short bob haircut, glasses, a gray blazer over a white top, "
            "black trousers. Strict-looking but fair, never mean.\n"
            "D — A's psychiatrist: a 40-year-old Korean woman doctor, hair tied back, a white doctor's coat over a light "
            "green top, calm and kind.\n"
            "K — the son's child psychiatrist: a 55-year-old Korean man doctor, short gray hair, round glasses, a white "
            "doctor's coat over a light blue shirt, warm grandfatherly smile.\n"
            "F — B's friend: a 52-year-old Korean man, a little chubby, short hair, a casual dark green jacket over a "
            "T-shirt. Cheerful and loud."
        ),
        "items": [
            # (kind, 이름, 무엇, 대본 장면, 프롬프트)
            ("ref", "A-REF", "A 기준 그림 (앞 · 4분의 3 · 옆) — 이 편 그림체 기준", "전체",
             "Draw A only. This is A, the main person of this video. Picture 1 also defines the drawing style of every "
             "later picture."),
            ("ref", "B-REF", "B 기준 그림 (앞 · 4분의 3 · 옆)", "전체",
             "Draw B only, in exactly the same style as picture 1. This is B, the other main person of this video."),
            ("poses", "W-POSES", "아내 자세 3: 따짐 · 빈손을 가리킴 · 베란다 통화", "4장",
             "Draw W only. Column 1: standing, three-quarter view facing left, arms crossed, asking with a tired, "
             "disappointed face. Column 2: standing, facing left, one open palm gesturing toward someone's empty hands, "
             "frustrated but not angry-looking. Column 3: standing, facing right, talking on a phone held to her ear, "
             "sad eyes looking down."),
            ("poses", "T-POSES", "팀장 자세 3: 회의 중 '듣고 있어요?' · 서류 읽기 · 엄지 척", "3장",
             "Draw T only. Column 1: sitting on an office chair, facing left, leaning forward with a puzzled face and one "
             "hand slightly raised as if asking a question. Column 2: standing, facing left, reading a blank document. "
             "Column 3: standing, facing left, giving a small approving thumbs-up with a warm smile."),
            ("poses", "D-POSES", "A씨 주치의 자세 3: 질문 · 기록부 보기 · 끄덕임 (앉은 자세)", "2장",
             "Draw D only, sitting on a doctor's office chair, facing left. Column 1: asking a gentle question, one open "
             "palm. Column 2: looking down at a blank open booklet in her hands. Column 3: a kind nod with a small smile."),
            ("poses", "S-POSES", "아들 자세 3 (앉은 자세): 손 꼼지락 · 아빠 쳐다봄 · 수줍은 웃음", "마무리",
             "Draw S only, sitting on a clinic chair, facing right. Column 1: fidgeting with his fingers, looking down. "
             "Column 2: glancing up and to the left at his father. Column 3: a small shy smile."),
            ("poses", "K-POSES", "소아청소년과 의사 자세 3 (앉은 자세): 설명 · 아버지에게 질문 · 따뜻한 미소", "마무리",
             "Draw K only, sitting on a doctor's office chair, facing left. Column 1: explaining with one hand open. "
             "Column 2: turning slightly to look up at an adult on the left with a curious, gentle questioning face. "
             "Column 3: a warm reassuring smile."),
            ("poses", "F-POSES", "친구 자세 3 (술집, 앉은 자세): 휴대폰 보여 주기 · 크게 웃기 · 잔 들기", "6장",
             "Draw F only, sitting on a pub stool, facing left. Column 1: holding up a phone toward the left with its "
             "blank screen visible, grinning. Column 2: laughing loudly, head back. Column 3: raising a beer glass."),
            ("bgs", "BG-OFFICE", "A씨 사무실 자리 (낮) — 1장 · 3장", "1장 · 3장",
             "A small open-plan office in the afternoon: a clean desk in the center with a monitor (blank light-blue "
             "screen), a keyboard, a mug and a small potted plant; an office chair in front of the desk; soft daylight "
             "from a window on the left; other desks blurred in the back."),
            ("bgs", "BG-B-LIVING", "B씨 집 거실 (저녁) — 1장 · 2장(밤은 코드로 어둡게) · 4장", "1장 · 2장 · 4장",
             "A cozy Korean apartment living room in the evening: a brown fabric sofa in the center with a low wooden "
             "table in front of it, a standing lamp, a TV cabinet on the right (TV off, blank), warm yellow light, wooden "
             "floor."),
            ("bgs", "BG-A-BED", "A씨 원룸 침실 (새벽 3시)", "1장 · 2장",
             "A small studio-apartment bedroom at 3 a.m.: a single bed with a light-gray blanket and pillows in the center, "
             "a bedside table with a small lamp turned off, dark blue night colors, soft cool glow, curtains closed."),
            ("bg", "BG-CLINIC", "A씨가 간 정신건강의학과 진료실", "2장",
             "A calm, bright psychiatry consultation room: a wooden desk on the right with a blank monitor, a doctor's "
             "chair behind it facing left, a comfortable patient chair on the left facing right, a potted plant, soft "
             "beige walls, a window with light curtains."),
            ("bg", "BG-RESTROOM", "회사 화장실 세면대", "3장",
             "A clean company restroom: a row of white sinks with a long mirror above (the mirror shows only soft light "
             "reflections, no people), pale mint tiles, warm ceiling light. The front-center floor in front of the middle "
             "sink is empty for a standing person."),
            ("bg", "BG-MEETING", "회사 회의실", "3장",
             "A small company meeting room: a long light-wood table seen from the side across the front, office chairs "
             "around it, a blank wall screen at the back, glass wall on the right, daylight."),
            ("bg", "BG-B-ROOM", "B씨 침실 (밤) — 다툰 뒤 혼자", "4장",
             "A Korean apartment bedroom at night: the edge of a double bed in the center (gray-blue bedding), a closed "
             "wooden door on the left, a small bedside lamp giving dim warm light, the rest in dark blue."),
            ("bg", "BG-VERANDA", "아파트 베란다 (저녁)", "4장",
             "An apartment veranda in the early evening: potted plants along the floor, a drying rack folded against the "
             "wall, big windows looking out on other apartment buildings with a few lit windows (no signs), soft orange "
             "and blue evening light."),
            ("bg", "BG-B-OFFICE", "B씨 회사 — 왼쪽 책상 · 오른쪽 빈 게시판", "4장",
             "A quiet company office floor: on the left a desk with a blank monitor and an office chair; on the right wall "
             "a large cork notice board with several blank white papers pinned on it (no writing). Neutral gray-blue "
             "colors, fluorescent light. The front area in front of the board is empty for a standing person."),
            ("bg", "BG-PUB", "동네 술집 테이블 (밤)", "6장",
             "A cozy Korean neighborhood pub at night: a round metal table in the center with small dishes of snacks and "
             "two empty beer glasses, low stools on both sides, warm hanging lights, wooden walls with blank paper menus "
             "(no writing)."),
            ("bg", "BG-PEDS", "소아청소년 정신건강의학과 진료실", "마무리",
             "A bright, friendly child and adolescent psychiatry consultation room: a desk on the right with a doctor's "
             "chair facing left, two chairs on the left facing right (one for a parent, one for a teenager), soft pastel "
             "colors, a few toys and plain picture frames with only color shapes."),
            ("bg", "BG-RECEPTION", "병원 접수대", "마무리",
             "A clean hospital reception area: a light-wood reception counter on the right (no people behind it), a "
             "waiting area with a few chairs on the left, a blank number display on the wall, soft daylight."),
            ("motion", "A01", "A: 모니터 보며 한숨 → 휴대폰을 들고 멍함 → 시계를 보고 화들짝 (땀방울)", "1장",
             "A, sitting on an office chair, three-quarter view facing RIGHT. Frame 1: looking at an invisible monitor on "
             "the right with a heavy sigh, shoulders down. Frame 2: holding a phone up in both hands, zoned out with empty "
             "eyes, the phone screen glowing blank. Frame 3: startled, looking up to the upper right at an invisible clock, "
             "wide eyes, one sweat drop, the phone still in her hand."),
            ("motion", "A02", "A: (침대에 앉아) 드라마에 빠져 키득 → 화면에 몰입 → 하품하면서도 다음 편 누름", "1장",
             "A, sitting cross-legged on an invisible bed, hugging a pillow, facing the viewer, holding a phone. Frame 1: "
             "giggling at the phone screen. Frame 2: completely absorbed, face lit by the screen's glow, eyes wide. "
             "Frame 3: a big yawn with watery eyes, but her thumb taps the screen to keep watching."),
            ("motion", "A03", "A: (밤, 침대) 영상을 진지하게 봄 → 입을 가리며 '내 얘기네' → 결심한 얼굴로 화면을 누름", "2장",
             "A, sitting on an invisible bed, facing the viewer, holding a phone. Frame 1: watching the phone seriously, "
             "eyebrows slightly raised. Frame 2: one hand over her mouth, realizing 'this is me', eyes wide. Frame 3: "
             "determined face, tapping the phone screen firmly with one finger."),
            ("motion", "A04", "A: (진료실 의자) 긴장해 듣기 → 빈 기록부를 펼쳐 보여 줌 → 안도하며 가슴에 손", "2장",
             "A, sitting on a patient chair, three-quarter view facing RIGHT. Frame 1: listening nervously, hands on her "
             "knees. Frame 2: holding up an open booklet with blank pages toward the right. Frame 3: a relieved small nod, "
             "one hand on her chest."),
            ("motion", "A05", "A: (사무실) 집중해 타자 → 마우스 클릭 → 놀라 멍하니 굳음", "3장",
             "A, sitting on an office chair, three-quarter view facing RIGHT. Frame 1: typing on an invisible keyboard, "
             "very focused, calm face. Frame 2: clicking an invisible mouse with a small decisive nod. Frame 3: frozen, "
             "stunned, eyes wide and mouth slightly open, slowly realizing something."),
            ("motion", "A06", "A: (세면대 앞에 서서) 눈물을 참음 → 눈물을 손등으로 닦음 → 슬프게 옅은 미소", "3장",
             "A, standing, three-quarter view facing LEFT, as if in front of an invisible sink. Frame 1: both hands "
             "gripping the edge of an invisible sink, lips pressed, holding back tears. Frame 2: tears falling, wiping her "
             "eyes with the back of her hand. Frame 3: a small, sad smile after wiping, shoulders relaxed."),
            ("motion", "A07", "A: (회의 중) 멍하니 허공 → 불리자 화들짝 → 이마를 짚으며 '아침 약…'", "3장",
             "A, sitting on an office chair, three-quarter view facing LEFT. Frame 1: zoned out, staring into space, mouth "
             "slightly open. Frame 2: startled, sitting up straight, one sweat drop. Frame 3: one hand on her forehead, "
             "embarrassed, eyes closed, realizing she forgot something."),
            ("motion", "A08", "A: (1년 뒤) 휴대폰을 서랍에 넣음 → 차분히 일함 → 기대앉아 만족한 미소", "3장",
             "A, sitting on an office chair, three-quarter view facing RIGHT. Frame 1: putting her phone into an open desk "
             "drawer at her side with a calm face. Frame 2: typing on an invisible keyboard, focused and relaxed. Frame 3: "
             "leaning back in the chair with a satisfied small smile."),
            ("motion", "B01", "B: (거실 소파) 고지서를 보며 인상 → 고지서를 놓고 휴대폰에 멍함 → 시계를 보고 화들짝", "1장",
             "B, sitting on an invisible sofa, three-quarter view facing LEFT, wearing the gray cardigan. Frame 1: frowning "
             "at a blank paper bill in his hand. Frame 2: the bill dropped on his lap, holding a phone, zoned out with "
             "empty eyes. Frame 3: startled, looking up to the upper left at an invisible clock, one sweat drop."),
            ("motion", "B02", "B: (밤, 소파) 낚시 영상에 신나 주먹 → 화면에 몰입 → 하품하면서도 계속 봄", "1장",
             "B, sitting on an invisible sofa, facing the viewer, gray cardigan, holding a phone. Frame 1: excited, a small "
             "fist pump, watching the phone. Frame 2: completely absorbed, face lit by the screen's glow. Frame 3: a big "
             "yawn, but still holding the phone up and watching."),
            ("motion", "B03", "B: (밤, 소파) 영상을 진지하게 봄 → 불편하게 인상 → 손을 내저으며 화면을 끔", "2장",
             "B, sitting on an invisible sofa, facing the viewer, gray cardigan, holding a phone. Frame 1: watching "
             "seriously with a slight nod. Frame 2: an uneasy frown, lips pressed. Frame 3: waving his free hand "
             "dismissively while pressing the phone's side button to turn it off."),
            ("motion", "B04", "B: (거실에 서서) 손바닥을 들어 방어 → 답답해 소리침 → 등을 돌려 방으로 감", "4장",
             "B, standing, three-quarter view facing LEFT, gray cardigan. Frame 1: both palms raised defensively, an "
             "awkward face. Frame 2: shouting in frustration — eyebrows angled, mouth wide — but arms down and no fists "
             "(frustrated, not violent). Frame 3: turning away toward the right, starting to walk off, head down."),
            ("motion", "B05", "B: (침대 끝에 앉아) 두 손으로 머리를 감쌈 → 한숨 쉬며 바닥을 봄 → 얼굴을 쓸어내림", "4장",
             "B, sitting on the edge of an invisible bed, facing the viewer, gray cardigan. Frame 1: head in both hands. "
             "Frame 2: a long sigh, elbows on knees, looking at the floor with guilty eyes. Frame 3: rubbing his face with "
             "one hand, tired and regretful."),
            ("motion", "B06", "B: (회사 책상) 화면을 읽음 → 충격에 굳음 → 눈을 감고 이마를 짚음", "4장",
             "B, sitting on an office chair, three-quarter view facing RIGHT, white shirt and navy tie. Frame 1: reading an "
             "invisible monitor calmly. Frame 2: frozen in shock, eyes wide, one sweat drop. Frame 3: eyes closed, one hand "
             "on his forehead."),
            ("motion", "B07", "B: (게시판 앞에 서서) 기대하며 훑어봄 → 실망 → 어깨가 처지고 고개 숙임", "4장",
             "B, standing, three-quarter back view facing RIGHT toward an invisible notice board, white shirt and navy "
             "tie. Frame 1: scanning the board with a hopeful look. Frame 2: disappointed, mouth tight. Frame 3: shoulders "
             "dropped, looking down at the floor."),
            ("motion", "B08", "B: (술집에 앉아) 내민 휴대폰을 봄 → 따라 웃음 → 어색하게 잔을 듦", "6장",
             "B, sitting on a pub stool, three-quarter view facing RIGHT, gray cardigan. Frame 1: leaning to look at a phone "
             "held out from the right. Frame 2: laughing along. Frame 3: raising a beer glass with a slightly forced smile."),
            ("motion", "B09", "B: (진료실 의자) 진지하게 듣기 → 자기를 가리키며 '저요?' → 턱을 괴고 생각", "마무리",
             "B, sitting on a chair, three-quarter view facing RIGHT, white shirt without a tie. Frame 1: listening "
             "seriously, hands on his knees. Frame 2: pointing at himself, surprised and confused — a 'who, me?' face. "
             "Frame 3: thoughtful, hand on his chin, looking down."),
            ("motion", "B10", "B: (접수대 앞에 서서) 머뭇거리며 뒷목을 만짐 → 손을 살짝 들고 물음 → 어색하지만 희망찬 미소", "마무리",
             "B, standing, three-quarter view facing RIGHT toward an invisible counter, white shirt without a tie. Frame 1: "
             "hesitating, rubbing the back of his neck. Frame 2: asking something with one hand slightly raised. Frame 3: "
             "an awkward but hopeful smile."),
            ("props", "PROPS-A", "소품 4: 휴대폰 · 고지서 · 요일 약통과 물컵 · 바늘 없는 벽시계", "1장 · 3장",
             "Prop sheet, landscape 1536x1024, four equal invisible columns, one prop centered in each column, similar "
             "visual size, each fully inside its column: (1) a smartphone, front view, the screen glowing plain light "
             "blue; (2) an opened envelope with a paper bill sticking out, only blank gray lines on it; (3) a weekly pill "
             "organizer box with seven small lids and a glass of water beside it; (4) a round wall clock face with tick "
             "marks only — NO numbers and NO clock hands (the hands will be added by code)."),
            ("props", "PROPS-B", "소품 4: 세탁소 비닐 속 양복 · 생활기록부 · 재생 버튼 화면 · 빈 달력", "2장 · 4장",
             "Prop sheet, landscape 1536x1024, four equal invisible columns, one prop centered in each column, similar "
             "visual size: (1) a dark suit on a hanger inside a clear dry-cleaning plastic bag; (2) a closed school record "
             "booklet with a plain light-green cover (no writing); (3) a smartphone showing a video player — a big white "
             "play-button triangle and a thin progress bar, nothing else; (4) a wall calendar page that is just a grid of "
             "empty squares with one square circled in red (no numbers, no letters)."),
            ("thumb", "TH-CHAR", "썸네일 그림: 왼쪽 A(환한 낮 · 일을 끝내고 안도) | 오른쪽 B(어두운 밤 · 머리를 감쌈) 반반 대비", "썸네일",
             "SPLIT CONTRAST in one picture, divided exactly in half by a clean vertical line in the middle. LEFT HALF: "
             "A at her office desk in bright warm daylight, leaning back with a relieved small smile, her phone put away "
             "in an open drawer, the monitor glowing calm, a tidy desk — her face clearly visible. RIGHT HALF: B at night "
             "on the edge of his bed in dark blue light, head in his hands, a crumpled blank paper bill and a phone on the "
             "floor, a small gloomy cloud scribble above his head — his face visible and tired. The two halves feel like "
             "opposites (light vs dark, warm vs cold). Leave empty space beside each person's head (not over any face) for "
             "speech bubbles. The bottom 35% of the whole picture is a calm, darker surface (desk front on the left, floor "
             "on the right) where large title text will be added later — nothing important there."),
        ],
    },
}


# v1.1 추가 요청 — 이미 받은 그림(1번 A-REF)을 그림체 기준으로, 몇 장만 더 (images_chatgpt_add.md)
ADD = {
    "adhd-ab-2026-11": {
        "why": "도입부 「할 일을 미루고 휴대폰만 보다가 하루가 지나감 → 밤에 '나는 왜 이렇게 게으를까' 자책」 장면 — 지금은 배경 없는 화면 "
               "(사용자 지시 2026-11-24 \"나는 왜 이렇게 게으를까 부분에 배경이 없는데 내용에 맞는 이미지를 넣고\")",
        "style_ref": "psychology/source/adhd-ab-2026-11/puppet/motion/A-REF.png",
        "people": (
            "V — the 'viewer' of the opening: a 29-year-old Korean man living alone, short messy black hair, an oversized "
            "light gray sweatshirt, navy sweatpants, white socks. Ordinary and relatable, a little tired. He must look clearly "
            "different from A (32-year-old woman), B (51-year-old man) and S (14-year-old boy in a navy hoodie)."
        ),
        "items": [
            ("bg", "BG-INTRO-ROOM", "도입 무대: 혼자 사는 원룸 (늦은 오후 — 밤은 코드로 어둡게)", "도입 1~2",
             "A small one-room studio apartment of a young office worker who lives alone, seen straight from the front. "
             "LEFT third: a desk against the wall with a closed laptop, a messy stack of blank papers, a few blank yellow "
             "sticky notes on the wall above the desk (no writing at all), a desk lamp. CENTER and RIGHT: a single bed with a "
             "rumpled light-blue blanket and two pillows, its long side facing us, the mattress top at about 55% of the "
             "picture height; a small side table with a phone charger cable. A window on the back wall above the bed shows a "
             "warm late-afternoon sky (orange and pink) over city buildings. A plain wall area at the upper right (about "
             "15% wide) is empty — a wall clock will be added there by code. Leave the floor in front of the bed and the bed "
             "itself empty of people. No text anywhere."),
            ("motion", "V01", "V: (침대 끝에 앉아) 휴대폰 보며 웃음 → 화면에 빠져 멍함 → 휴대폰을 내려놓고 이마를 짚으며 자책", "도입 1~2",
             "V, sitting on the edge of an invisible bed, facing the viewer, feet on the floor, both shoes off (socks). "
             "Frame 1: holding a phone with both hands, smiling at the screen, relaxed. Frame 2: completely absorbed in the "
             "phone, empty eyes, face lit by the screen's glow, slouching. Frame 3: the phone dropped face-down on his lap, "
             "one hand on his forehead, eyes closed, a guilty sigh — blaming himself."),
        ],
    },
}


def rel_path(ep: str, kind: str, name: str) -> str:
    """저장 경로 — 만스피 꼴과 같은 폴더 (배경 puppet/ · 기준·자세·원화·소품 puppet/motion/ · 썸네일 그림 images/)."""
    if kind in ("bg", "bgs"):
        return f"psychology/source/{ep}/puppet/{name}.jpg"
    if kind == "thumb":
        return f"psychology/source/{ep}/images/{name}.jpg"
    return f"psychology/source/{ep}/puppet/motion/{name}.png"


def build(ep: str, spec: dict) -> str:
    items = spec["items"]
    n = len(items)
    num = {it[1]: i + 1 for i, it in enumerate(items)}
    refs = [it for it in items if it[0] in ("ref", "poses")]
    ref_nums = " · ".join(f"{num[r[1]]}번 {r[1]}" for r in refs)
    L = []
    w = L.append
    w(f"# {ep} — 일상툰 그림 {n}장 (ChatGPT용 · 1번부터 차례로 모두)")
    w("")
    w(f"작성: {VERSION} — {DATE} — 사용자 지시 \"그럼 모든 이미지 생성 명령 알려줘 지시사항은 저장소에서 읽으라하고 업로드하라고해\" · "
      f"\"썸네일 이미지도 만들어 A, B 사람 반반 나눠서 대비되도록\". 기준 대본 = {spec['script']} · 영상 「{spec['title']}」.")
    w("")
    w("**어떻게 쓰는가 — 일상툰 꼴 코드 애니메이션**")
    w("- Claude 가 코드로 만든다: 배경 그림 위에 인물·소품 조각을 올리고, 동작마다 이어지는 원화 3장(키 → 중간 → 키)을 바꿔 끼워 움직이게 한다. "
      "화면 반반(왼쪽 A · 오른쪽 B)·말풍선·자막·시계 바늘·그래프는 코드가 얹는다 → **그림에는 글자가 하나도 없어야 한다.**")
    w(f"- **그림체 기준 = 1번 A-REF** — 이 편은 바깥 기준 그림이 없다. 1번이 정한 그림체를 2번부터 모두 똑같이 따른다. 사람 기준 = {ref_nums}.")
    w(f"- 썸네일 그림(마지막 장)은 **A·B 반반 대비** 그림만 — 문구 {spec['thumb_text']}.")
    w("- A·B 는 가상 인물. ※ 연구·교육용 영상 — 의학적 진단·처방이 아니다. 누구도 나쁜 사람으로 그리지 않는다.")
    w("")
    w(f"| 번호 | 저장 경로 (모두 `psychology/source/{ep}/` 아래) | 무엇 | 대본 |")
    w("|---|---|---|---|")
    for i, (kind, name, what, where, _p) in enumerate(items, 1):
        w(f"| {i} | `{rel_path(ep, kind, name).split(f'{ep}/', 1)[1]}` | {what} | {where} |")
    w("")
    w("## ChatGPT에게 — 이 파일을 읽으면 할 일")
    w("0. **이 주소를 지금 새로 열어 그 내용만 쓴다** — 이 대화에서 예전에 읽은 파일·프롬프트가 있어도 쓰지 않는다. 답의 첫 줄에 이 파일 맨 위 '작성' 줄을 그대로 적는다.")
    w(f"   **★ 1번 A-REF 가 이 편 그림체의 기준이다 — 2번부터 모든 그림은 1번과 같은 사람이 그린 것처럼 (선 굵기·색·얼굴 꼴·약 3등신 비율).** 사람은 {ref_nums} 이 기준 — 그 뒤 같은 사람은 얼굴·머리·옷·색·비율이 똑같아야 한다. 다르게 나오면 다시 만든다.")
    w(f"1. 아래 1~{n}번 **{n}장을 번호 순서대로 모두** 만든다. 질문하지 말고, 한 장을 만든 뒤 멈추지 말고 다음 장으로 넘어간다. 이미지 한도 때문에 멈추면 사용자가 `계속`이라고 보낸다 → 아직 안 만든 번호부터.")
    w("2. 프롬프트(``` 안)를 **한 글자도 바꾸지 않고 그대로** 쓰고, 앞에 아래 블록을 이 순서로 붙인다.")
    for k, label in (("ref", "기준 그림"), ("poses", "조연 자세 그림"), ("bg", "배경"), ("bgs", "반반 화면 배경"),
                     ("motion", "동작 그림"), ("props", "소품"), ("thumb", "썸네일 그림")):
        nums = [str(i) for i, it in enumerate(items, 1) if it[0] == k]
        if nums:
            w(f"   - **{label}({', '.join(nums)}번)**: {ORDER[k]}.")
    w("3. **동작 그림은 한 장에 같은 사람을 3번** 그린다 — 왼쪽 → 가운데 → 오른쪽이 **한 동작을 이어 그린 3장**(애니메이션 원화)이다. 같은 크기·같은 자리·같은 방향·같은 옷, **발바닥(앉은 자세는 의자·소파 자리)이 같은 높이**, **움직이는 부분(팔·손·머리·얼굴·상체)만** 바뀐다. "
      "**자세 그림(POSES)** 은 이어지는 동작이 아니라 서로 다른 자세 3개 — 그래도 크기·발 높이·옷은 같다. 서로 겹치거나 칸(가로 3등분)을 넘지 않는다. 다른 사람·배경·바닥 그림자는 없다.")
    w("4. **검사 (기준·자세·동작·소품 필수, 올리기 전에):** 파이썬으로 아래 코드를 돌려 `OK` 가 나와야 올린다. `잘림`·`칸 넘음`·`발 높이 다름`이면 고쳐서 다시 만든다. **투명이 아니면 배경을 순자홍 #FF00FF 한 색 평면으로 다시 만든다.**")
    w(CHECK_CODE.replace("# 기준 그림·동작 그림: check(경로, cols=3, feet=True)",
                         "# 기준·자세·동작 그림: check(경로, cols=3, feet=True)"))
    w("5. **글자·숫자·로고·워터마크를 하나도 넣지 않는다** — 화면·휴대폰·서류·책·게시판·시계·달력·간판에도 없음 (빈 판이나 단순한 줄·도형만). 실제 회사·앱·병원의 이름·로고를 닮게 그리지 않는다. 만든 뒤 확대해 글자가 보이면 다시 만든다.")
    w("   **사람을 나쁘게 그리지 않는다** — B 가 소리치는 장면도 답답함이지 폭력이 아니다(주먹·물건 던지기 없음). 아내·팀장·의사는 지치거나 놀란 얼굴은 되지만 무서운 사람처럼 그리지 않는다. 약을 먹는 장면·주사·피는 그리지 않는다.")
    w(f"6. 그림 바로 위에 번호와 저장 경로를 한 줄 적는다 (`1. {rel_path(ep, items[0][0], items[0][1])}`). 그림 안에는 쓰지 않는다.")
    w("7. **다 만들면 저장소에 넣는다 — 저장 경로 그대로.**")
    w(f"   - 저장소 `{REPO}` main 브랜치, 경로는 표의 파일 이름 그대로 (대소문자·하이픈까지 같게 — 배경은 `psychology/source/{ep}/puppet/`, 기준·자세·동작·소품은 `psychology/source/{ep}/puppet/motion/`, 썸네일 그림은 `psychology/source/{ep}/images/`).")
    w("   - **올리기 전에 700KB 이하로 만든다** — GitHub 앱은 약 768KB 를 넘는 파일을 잘라 올려 그림이 깨진다. 올린 뒤 GitHub 의 파일 크기(바이트)가 내 파일과 같은지 확인하고, 다르면 다시 올린다.")
    w("     - 배경·썸네일(JPEG): RGB · 크기 1536×864 그대로 · 품질 90부터 5씩 낮춰 700KB 아래가 될 때까지 저장.")
    w("     - 기준·자세·동작·소품(PNG, 투명 유지): 아래 코드 그대로.")
    w(SAVE_CODE)
    w(f"   - **GitHub 앱으로 장마다 커밋한다.** 커밋 메시지: `[psychology] {ep} <파일 이름> 이미지` (예: `[psychology] {ep} {items[0][1]}.png 이미지`). 다 올리면 올린 파일 경로와 커밋 링크를 목록으로 적는다.")
    w("   - **올리기가 실패한 장만** (권한·연결 오류) 그림을 번호 순서대로 한 번 더 보여 준 뒤 이 문장을 그대로 쓴다: **\"올리지 못한 그림을 이 순서대로 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 각 저장 경로에 올립니다.\"**")
    w("")
    blocks = [("공통 화풍 (모든 프롬프트 맨 앞에 그대로 붙임)", STYLE),
              ("배경판 (배경 — 공통 화풍 다음에 그대로 붙임)", PLATE),
              ("반반 화면 (반반 화면 배경 — 배경판 다음에 그대로 붙임)", SPLIT),
              ("인물 (기준·자세·동작·썸네일 — 공통 화풍 다음에 그대로 붙임)",
               "CHARACTERS — draw each person exactly like their reference or pose sheet (pictures "
               + ", ".join(str(num[r[1]]) for r in refs) + "). The same face, hair, clothes, colors and proportions in every "
               "picture:\n" + spec["people"]),
              ("CUTOUT (기준·자세·동작·소품 — 그다음에 그대로 붙임 · 배경·썸네일에는 붙이지 않음)", CUTOUT),
              ("기준 시트 (기준 그림 — CUTOUT 다음에 그대로 붙임)", TURN),
              ("자세 시트 (조연 자세 그림 — CUTOUT 다음에 그대로 붙임)", POSES),
              ("MOTION STRIP (동작 그림 — CUTOUT 다음에 그대로 붙임)", MOTION),
              ("썸네일 (썸네일 그림 — 인물 다음에 그대로 붙임)", THUMB)]
    for title, text in blocks:
        L += [f"## {title}", "", "```", text, "```", ""]
    for i, (kind, name, what, where, prompt) in enumerate(items, 1):
        L += [f"## {i}. {name} — {what}", "", f"**저장 경로: `{rel_path(ep, kind, name)}`** — {KIND_INFO[kind][1]}", "",
              "```", prompt, "```", ""]
    w("## 받은 뒤 (Claude)")
    w(f"- main 의 `psychology/source/{ep}/puppet/`·`images/` 를 가져와 {n}장을 확대해 검수: 1번 그림체와 같은지 · 같은 사람인지 · 그림 속 글자 없음 · 세 장의 발 높이·크기·옷 · 반반 화면 배경의 가운데 절반 · 사람을 나쁘게 그리지 않았는지.")
    w(f"- `psychology/source/puppet_slice.py {ep}` 로 자르기 → `puppet/cut/` + `manifest.js` · 장면 `video/episodes/{ep}/index.html` (공통 엔진 `video/render/psy_anim.js` — 반반 화면·말풍선·시계 바늘은 코드).")
    w("- 오디오(`narration.mp3`, 내레이션만 — 말풍선은 소리 없음)가 생기면 align → sync → check·layout-check 문제 0 → 렌더 → 완성 mp4 를 직접 봄.")
    w("- 썸네일 = `images/TH-CHAR.jpg` + 문구는 코드(`video/render/thumb.mjs`) — 제목·문구는 `guides/persona_loop.md` 검증 뒤.")
    w("")
    return "\n".join(L)


def build_add(ep: str, spec: dict, ref_url: str) -> str:
    """v1.1 추가 요청 파일 — 이미 받은 A-REF 를 그림체 기준으로 몇 장만 (할 일·검사·저장 규칙은 본 요청 파일과 같음)."""
    items = spec["items"]
    n = len(items)
    L = []
    w = L.append
    w(f"# {ep} — 일상툰 추가 그림 {n}장 (ChatGPT용 · 1번부터 차례로 모두)")
    w("")
    w(f"작성: {VERSION} — {DATE} — 추가 요청. 까닭: {spec['why']}.")
    w("")
    w(f"- **그림체 기준 = 이미 저장소에 올린 A-REF 그림** — {ref_url}")
    w("  이 그림(약 3등신 어른 · 둥근 선 · 부드러운 파스텔 · 갈색 선)과 **같은 사람이 그린 것처럼** 그린다. 이 대화에서 앞서 이 편 그림을 만들었다면 그 그림체 그대로. "
      "주소를 열 수 없으면 사용자에게 A-REF 그림을 붙여 달라고 한 번만 말한다.")
    w("- 그림에는 글자·숫자·로고가 하나도 없다 (말풍선·자막·시계 바늘은 코드). 누구도 나쁜 사람으로 그리지 않는다. 가상 인물. ※ 연구·교육용 영상 — 의학적 진단·처방이 아니다.")
    w("")
    w(f"| 번호 | 저장 경로 (모두 `psychology/source/{ep}/` 아래) | 무엇 | 대본 |")
    w("|---|---|---|---|")
    for i, (kind, name, what, where, _p) in enumerate(items, 1):
        w(f"| {i} | `{rel_path(ep, kind, name).split(f'{ep}/', 1)[1]}` | {what} | {where} |")
    w("")
    w("## ChatGPT에게 — 이 파일을 읽으면 할 일")
    w("0. 이 주소를 지금 새로 열어 그 내용만 쓴다. 답의 첫 줄에 이 파일 맨 위 '작성' 줄을 그대로 적는다.")
    w(f"1. 아래 1~{n}번 **{n}장을 번호 순서대로 모두** 만든다. 질문하지 말고 멈추지 않는다.")
    w("2. 프롬프트(``` 안)를 **한 글자도 바꾸지 않고 그대로** 쓰고, 앞에 아래 블록을 이 순서로 붙인다.")
    for k, label in (("bg", "배경"), ("motion", "동작 그림")):
        nums = [str(i) for i, it in enumerate(items, 1) if it[0] == k]
        if nums:
            w(f"   - **{label}({', '.join(nums)}번)**: {ORDER[k]}.")
    w("3. **동작 그림은 한 장에 같은 사람을 3번** — 왼쪽 → 가운데 → 오른쪽이 한 동작을 이어 그린 3장. 같은 크기·같은 자리·같은 방향·같은 옷, 앉은 자리(엉덩이·발바닥)가 같은 높이, 움직이는 부분만 바뀐다. 서로 겹치거나 칸(가로 3등분)을 넘지 않는다. 다른 사람·배경·바닥 그림자 없음.")
    w("4. **검사 (동작 그림, 올리기 전에):** 아래 코드로 `check(경로, cols=3, feet=True)` 가 `OK` 여야 올린다. 투명이 아니면 배경을 순자홍 #FF00FF 한 색 평면으로 다시 만든다.")
    w(CHECK_CODE)
    w("5. 화면·휴대폰·종이·포스트잇·시계에도 글자·숫자가 없다. 만든 뒤 확대해 글자가 보이면 다시 만든다.")
    w(f"6. 그림 바로 위에 번호와 저장 경로를 한 줄 적는다 (`1. {rel_path(ep, items[0][0], items[0][1])}`).")
    w(f"7. **저장소 `{REPO}` main 에 저장 경로 그대로 올린다** — 700KB 이하 (배경 JPEG: 1536×864 · 품질 90부터 5씩 낮춤 · 동작 PNG: 아래 코드).")
    w(SAVE_CODE)
    w(f"   - GitHub 앱으로 장마다 커밋: `[psychology] {ep} <파일 이름> 이미지`. 다 올리면 파일 경로와 커밋 링크를 목록으로 적는다.")
    w("   - 올리기가 실패한 장만: \"올리지 못한 그림을 이 순서대로 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 각 저장 경로에 올립니다.\"")
    w("")
    blocks = [("공통 화풍 (모든 프롬프트 맨 앞에 그대로 붙임)", STYLE),
              ("배경판 (배경 — 공통 화풍 다음에 그대로 붙임)", PLATE),
              ("인물 (동작 그림 — 공통 화풍 다음에 그대로 붙임)", "CHARACTERS — the same face, hair, clothes, colors and proportions in every frame:\n" + spec["people"]),
              ("CUTOUT (동작 그림 — 그다음에 그대로 붙임 · 배경에는 붙이지 않음)", CUTOUT),
              ("MOTION STRIP (동작 그림 — CUTOUT 다음에 그대로 붙임)", MOTION)]
    for title, text in blocks:
        L += [f"## {title}", "", "```", text, "```", ""]
    for i, (kind, name, what, where, prompt) in enumerate(items, 1):
        L += [f"## {i}. {name} — {what}", "", f"**저장 경로: `{rel_path(ep, kind, name)}`** — {KIND_INFO[kind][1]}", "",
              "```", prompt, "```", ""]
    w("## 받은 뒤 (Claude)")
    w(f"- 확대 검수(그림체·글자 없음·발 높이) → `psychology/source/puppet_slice.py {ep}` → 장면 파일 도입 장면에 넣고 다시 렌더.")
    w("")
    return "\n".join(L)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true", help="쓰지 않고 장 수·경로만")
    a = ap.parse_args()
    logging.basicConfig(level=logging.INFO, format="[%(name)s] %(message)s")
    for ep, spec in EPISODES.items():
        script = ROOT / "psychology" / "source" / ep / "대본_초안.txt"
        if not script.exists():
            log.error("대본 없음 ep=%s path=%s — 영상ID 를 확인하세요", ep, script)
            return 1
        names = [it[1] for it in spec["items"]]
        if len(names) != len(set(names)):
            log.error("이름 겹침 ep=%s", ep)
            return 1
        counts = {k: sum(1 for it in spec["items"] if it[0] == k) for k in KIND_INFO}
        text = build(ep, spec)
        if "ADHD" in "".join(it[4] for it in spec["items"]):
            log.warning("프롬프트에 'ADHD' 글자 — 그림 속 글자로 들어갈 수 있음, 확인할 것")
        out = ROOT / "psychology" / "source" / ep / "images_chatgpt.md"
        log.info("version=%s ep=%s items=%d kinds=%s chars=%d out=%s", VERSION, ep, len(spec["items"]), counts, len(text),
                 out.relative_to(ROOT))
        if not a.check:
            out.write_text(text, encoding="utf-8")
    for ep, spec in ADD.items():                       # v1.1 추가 요청 파일
        ref = ROOT / spec["style_ref"]
        if not ref.exists():
            log.error("그림체 기준 그림 없음 ep=%s path=%s — 본 요청 그림이 main 에 왔는지 확인", ep, spec["style_ref"])
            return 1
        ref_url = f"https://raw.githubusercontent.com/{REPO}/main/{spec['style_ref']}"
        text = build_add(ep, spec, ref_url)
        out = ROOT / "psychology" / "source" / ep / "images_chatgpt_add.md"
        log.info("version=%s ep=%s add_items=%d chars=%d out=%s", VERSION, ep, len(spec["items"]), len(text), out.relative_to(ROOT))
        if not a.check:
            out.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
