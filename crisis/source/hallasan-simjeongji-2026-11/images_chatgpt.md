# hallasan-simjeongji-2026-11 — 다큐 재연 사진 24장 (ChatGPT용 · 1번부터 차례로 모두)

작성: v1.0 — 2026-11-25 — 사용자 지시 "대본 이걸로 하고 영상은 심리 영상처럼 이미지들을 사용하여 실감나는 영상을 만들돼 뉴스, 다큐에서 설명하듯 느낌으로 하고 사람 이미지는 실루엣으로 해 생성 명령 알려줘". 기준 대본 = `crisis/source/hallasan-simjeongji-2026-11/대본_초안.txt` v2.2 · 영상 「"먼저 내려가겠다"는 사소한 결정 — 한라산 둘레길 심정지」.

**어떻게 쓰는가 — 뉴스·다큐 재연 꼴**
- 사진처럼 실감 나는 **재연 장면 사진**(1~11 · 16~24번)과 **의학 설명 그림**(12~15번)을 Claude 가 코드로 이어 붙인다: 천천히 다가가거나 옆으로 흐르는 카메라 움직임, 장 제목, 시각(13:48 등), 한국 지도·숫자 카드·연구 카드·몸 위 신호 점·4분 시계·점검 목록, 화면 구석의 '재연' 표시, 자막은 모두 코드가 얹는다 → **사진에는 글자가 하나도 없어야 한다.**
- **사람은 모두 실루엣** — 역광·그늘·먼 뒷모습으로 얼굴과 생김새가 전혀 보이지 않게. 실제 사건의 A씨(54세, 제주 도민)·일행·구급대원을 닮게 그리지 않는다(재연). 숨진 분의 몸·얼굴은 그리지 않는다 — 쓰러진 장면은 덤불에 가려 보이지 않게, 들것 위는 담요로 덮인 형체만.
- 썸네일 그림은 제목이 정해진 뒤 따로 요청한다 (이 파일에 없음).
- ※ 안전 교육 영상(연구·교육용) — 의학적 진단이 아니다. 피·상처·시신·공포 연출 없음. 차분하고 존중하는 분위기.

| 번호 | 저장 경로 (모두 `crisis/source/hallasan-simjeongji-2026-11/` 아래) | 무엇 | 대본 |
|---|---|---|---|
| 1 | `images/DOC-01-INTRO.jpg` | 오르막 숲길에서 숨이 차 무릎에 손을 짚은 등산객 실루엣 (뒷모습) | 도입 |
| 2 | `images/DOC-02-ENTRANCE.jpg` | 이른 봄 한라산 둘레길 입구 · 일행 4명이 숲길로 들어감 (뒷모습) | 1장 |
| 3 | `images/DOC-03-FOREST.jpg` | 해발 600~800m 중산간 숲길 넓은 풍경 (사람 없음) | 1장 · 5장① |
| 4 | `images/DOC-04-STOP.jpg` | 숲길에서 A씨 실루엣이 걸음을 멈춤 · 앞서가던 일행이 뒤를 돌아봄 | 2장 · 5장② |
| 5 | `images/DOC-05-TURN.jpg` | A씨 혼자 왔던 길로 돌아섬 · 일행은 반대쪽으로 멀어짐 | 2장 · 5장③ |
| 6 | `images/DOC-06-EMPTY.jpg` | 사람이 아무도 없는 오후의 텅 빈 숲길 | 3장 · 4장 |
| 7 | `images/DOC-07-CALL.jpg` | 둘레길 입구 쪽 일행이 주위를 둘러보고, 한 명이 휴대폰으로 신고 | 3장 |
| 8 | `images/DOC-08-SEARCH.jpg` | 119 구급대원 실루엣들이 숲으로 흩어져 수색 | 3장 |
| 9 | `images/DOC-09-FOUND.jpg` | 한 대원이 낮은 덤불 쪽을 가리키며 동료를 부름 (쓰러진 사람은 보이지 않음) | 3장 |
| 10 | `images/DOC-10-STRETCHER.jpg` | 대원들이 들것을 들고 숲길을 급히 내려감 (들것 위는 담요로 덮인 형체) | 4장 |
| 11 | `images/DOC-11-AMBULANCE.jpg` | 숲 입구 도로의 구급차와 경광등 (글자 없음) | 4장 |
| 12 | `images/MED-12-HEART.jpg` | 의학 그림: 사람 심장과 심장을 감싼 혈관 | 5장① |
| 13 | `images/MED-13-ARTERY.jpg` | 의학 그림: 안쪽이 좁아진 혈관 단면 | 5장① |
| 14 | `images/MED-14-BODY.jpg` | 의학 그림: 반투명 상반신 실루엣 · 가슴의 심장만 은은히 빛남 | 5장② · 8장 |
| 15 | `images/MED-15-BRAIN.jpg` | 의학 그림: 옆모습 머리 실루엣 속 뇌 · 혈류가 끊겨 어두워지는 모습 | 5장④ |
| 16 | `images/DOC-16-SEONGPANAK.jpg` | 초봄 바람 부는 한라산 성판악 쪽 돌길 탐방로 (사람 없음) | 6장 |
| 17 | `images/DOC-17-SUMMER.jpg` | 한여름 폭염, 아침 햇빛 아래 바위 산길 (사람 없음) | 6장 |
| 18 | `images/DOC-18-AUTUMN.jpg` | 가을 단풍이 든 바위 능선 등산로 (사람 없음) | 6장 |
| 19 | `images/DOC-19-HALLA-AUTUMN.jpg` | 늦가을 한라산 숲 하산길 · 멀리 내려가는 등산객 실루엣 하나 | 6장 |
| 20 | `images/DOC-20-RIDGE.jpg` | 새벽 운해 위로 겹겹이 이어진 큰 산 능선 (통계 배경) | 7장 |
| 21 | `images/DOC-21-CITY.jpg` | 밤 도시를 내려다본 풍경 · 길 위로 구급차 불빛이 흐름 (통계 배경) | 7장 |
| 22 | `images/DOC-22-NIGHT-PREP.jpg` | 등산 전날 밤 거실 탁자 · 배낭·물병·겉옷·약 봉투·빈 결과지 · 등 뒤 조명의 실루엣 사람 | 8장 |
| 23 | `images/DOC-23-SIT.jpg` | 숲길에서 한 사람이 바위에 앉고, 일행이 옆에 쪼그려 앉아 휴대폰으로 통화 | 8장 |
| 24 | `images/DOC-24-END.jpg` | 오후 햇살이 드는 둘레길을 일행 몇 명이 나란히 천천히 걸어감 (뒷모습) | 마무리 |

## ChatGPT에게 — 이 파일을 읽으면 할 일
0. **이 주소를 지금 새로 열어 그 내용만 쓴다** — 이 대화에서 예전에 읽은 파일·프롬프트(다른 편의 웹툰·만화·종이 인형극·실사 사진 포함)가 있어도 쓰지 않는다. 답의 첫 줄에 이 파일 맨 위 '작성' 줄을 그대로 적는다.
1. 아래 1~24번 **24장을 번호 순서대로 모두** 만든다. 질문하지 말고, 한 장을 만든 뒤 멈추지 말고 다음 장으로 넘어간다. 이미지 한도 때문에 멈추면 사용자가 `계속`이라고 보낸다 → 아직 안 만든 번호부터.
2. 프롬프트(``` 안)를 **한 글자도 바꾸지 않고 그대로** 쓰고, 앞에 아래 블록을 이 순서로 붙인다.
   - **재연 사진(1~11, 16~24번)**: 다큐 재연 화풍 → 실루엣 인물 → 프롬프트. (사람이 없는 장면 3, 6, 16, 17, 18, 20, 21번도 같은 순서로 붙인다.)
   - **의학 그림(12~15번)**: 의학 그림 화풍 → 프롬프트.
3. **모든 장이 한 편의 다큐처럼 이어져야 한다** — 같은 색감(차분하고 살짝 어두운 자연광, 낮은 채도), 같은 카메라 느낌(눈높이 또는 조금 낮은 앵글, 얕은 심도, 옅은 필름 그레인). 2~11번과 23~24번의 같은 장소(둘레길 숲길)는 같은 숲으로 보이게.
4. **사람은 실루엣만** — 얼굴·눈·코·입·피부 결이 보이면 다시 만든다. 역광이나 그늘로 몸의 윤곽만, 또는 멀리 뒷모습. 같은 사람(A씨, 일행, 구급대원)은 장마다 윤곽(모자·배낭·체격)이 같게.
5. **글자·숫자·로고·워터마크를 하나도 넣지 않는다** — 안내판·이정표·구급차·구조복·휴대폰 화면·종이·약 봉투에도 없음 (빈 판이나 단순한 무늬만). 실제 기관·회사·차량의 이름·로고·표시를 닮게 그리지 않는다. 만든 뒤 확대해 글자처럼 보이는 것이 있으면 다시 만든다.
   **피·상처·시신·공포 연출 없음** — 쓰러진 사람은 그리지 않거나(덤불에 가려 안 보임), 들것 위는 담요로 덮인 형체만. 아무도 무섭게 그리지 않는다.
6. 그림 바로 위에 번호와 저장 경로를 한 줄 적는다 (`1. crisis/source/hallasan-simjeongji-2026-11/images/DOC-01-INTRO.jpg`). 그림 안에는 쓰지 않는다.
7. **다 만들면 저장소에 넣는다 — 저장 경로 그대로.**
   - 저장소 `yeomin1024/yeomin1024-ytb` main 브랜치, 경로는 표의 파일 이름 그대로 (대소문자·하이픈까지 같게 — 모두 `crisis/source/hallasan-simjeongji-2026-11/images/`).
   - **JPEG `.jpg` · RGB · 1536×864 · 700KB 이하** — 품질 90부터 5씩 낮춰 700KB 아래가 될 때까지 저장한다 (GitHub 앱은 약 768KB 를 넘는 파일을 잘라 올려 그림이 깨진다). 올린 뒤 GitHub 의 파일 크기(바이트)가 내 파일과 같은지 확인하고, 다르면 다시 올린다.
     ```python
     from PIL import Image
     import os
     def save_jpg(src, dst, limit=700_000):
         im = Image.open(src).convert("RGB")
         if im.size != (1536, 864):
             w, h = im.size; s = max(1536 / w, 864 / h)
             im = im.resize((round(w * s), round(h * s)), Image.LANCZOS)
             l, t = (im.width - 1536) // 2, (im.height - 864) // 2
             im = im.crop((l, t, l + 1536, t + 864))
         q = 90
         while True:
             im.save(dst, "JPEG", quality=q, optimize=True, progressive=True)
             if os.path.getsize(dst) <= limit or q <= 50: break
             q -= 5
         print(dst, os.path.getsize(dst), im.size, "q", q)
     ```
   - **GitHub 앱으로 장마다 커밋한다.** 커밋 메시지: `[crisis] hallasan-simjeongji-2026-11 <파일 이름> 이미지` (예: `[crisis] hallasan-simjeongji-2026-11 DOC-01-INTRO.jpg 이미지`). 다 올리면 올린 파일 경로와 커밋 링크를 목록으로 적는다.
   - **올리기가 실패한 장만** (권한·연결 오류) 그림을 번호 순서대로 한 번 더 보여 준 뒤 이 문장을 그대로 쓴다: **"올리지 못한 그림을 이 순서대로 Claude 대화창에 붙여 넣어 주세요. Claude가 검수한 뒤 각 저장 경로에 올립니다."**

## 다큐 재연 화풍 (재연 사진 1~11, 16~24번 — 맨 앞에 그대로 붙임)

```
STYLE: a photorealistic documentary reenactment still, like a frame from a serious Korean TV news report or investigative documentary. Full-bleed landscape 1536x864, cinematic 16:9 composition, eye-level or slightly low camera, shallow depth of field, natural light only, calm and slightly dark muted colors with low saturation, soft contrast, a subtle film grain. Setting: Korea — Jeju island's mid-mountain forests and Korean mountain trails — but no identifiable real landmark. The mood is quiet, serious and respectful, never horror or action-movie drama. Absolutely no text, letters, numbers, logos, emblems or watermarks anywhere: trail signs, direction posts, vehicles, uniforms, phone screens, papers and medicine packets are blank or show only plain shapes. No blood, no injuries, no dead body, nothing gruesome.
```

## 실루엣 인물 (재연 사진 — 다큐 재연 화풍 다음에 그대로 붙임)

```
PEOPLE AS SILHOUETTES: every person in the picture appears only as a dark silhouette — backlit against brighter light, standing in shadow, or seen from behind at a distance — so that no face, eyes, nose, mouth, skin texture or identifying detail is visible. Keep the body outline natural and realistic (posture, clothing shape, backpack), not cartoon. Recurring people keep the same outline in every picture:
A — a Korean man in his 50s, medium build, a plain dark baseball cap, a dark gray outdoor jacket, dark trousers, a small black daypack, no hiking poles.
COMPANIONS — three other hikers in their 50s (two men and one woman), plain outdoor jackets in muted colors, small daypacks; one of them wears a brimmed hiking hat.
RESCUERS — Korean emergency rescue workers seen as silhouettes: rescue helmets, dark uniforms with thin reflective stripes that catch the light (no letters or emblems), rescue backpacks.
OTHER HIKERS — anonymous hikers, silhouettes only.
If a picture describes no people, there are no people or animals at all.
```

## 의학 그림 화풍 (의학 그림 12~15번 — 맨 앞에 그대로 붙임)

```
STYLE-MED: a clean, realistic 3D medical visualization for a TV health documentary. Full-bleed landscape 1536x864, deep navy-to-black background, soft rim light and gentle glow, semi-transparent anatomy where described, realistic tissue rendered tastefully (not bloody, not gory), red tones for blood and the heart, cool blue-gray for the body outline. Keep the subject large and centered with empty dark space around it for on-screen graphics added later. Absolutely no text, labels, arrows, numbers, logos or watermarks.
```

## 1. DOC-01-INTRO — 오르막 숲길에서 숨이 찬 등산객 (도입)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/DOC-01-INTRO.jpg`** — JPEG 700KB 이하 · 1536×864

```
A steep forest trail with stone steps climbing upward through a Korean mountain forest in early spring. In the middle distance, one OTHER HIKER seen from behind as a silhouette has stopped on the steps, bent forward with both hands on the knees, catching breath. Soft hazy light comes down the slope from above, behind the hiker, so the figure is backlit. A few bare branches and new pale-green leaves. The upper part of the slope fades into bright haze.
```

## 2. DOC-02-ENTRANCE — 이른 봄 한라산 둘레길 입구 (1장)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/DOC-02-ENTRANCE.jpg`** — JPEG 700KB 이하 · 1536×864

```
Early spring midday on Jeju island, the entrance of a gentle, mostly flat forest trail at about 700 meters above sea level. A wide packed-earth path with scattered black volcanic stones leads into a quiet forest of tall Japanese cedars and leafless broadleaf trees, moss on the rocks, low ferns. A plain wooden post with a blank board stands at the trail edge. Four people walk into the forest away from the camera, seen from behind as silhouettes against the brighter path ahead: A (cap, small black daypack) walking second, and the three COMPANIONS. Overcast soft daylight filtering through the trees.
```

## 3. DOC-03-FOREST — 해발 600~800m 중산간 숲길 넓은 풍경 (1장 · 5장①)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/DOC-03-FOREST.jpg`** — JPEG 700KB 이하 · 1536×864

```
A wide establishing shot of the same Jeju mid-mountain forest trail: a flat earth path winding gently between tall Japanese cedars and broadleaf trees, black volcanic stones covered in green moss, ferns and low bamboo grass on both sides, light mist between the trunks in the distance. Overcast early-spring daylight, cool and calm. No people.
```

## 4. DOC-04-STOP — A씨가 걸음을 멈추고 일행이 돌아봄 (2장 · 5장②)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/DOC-04-STOP.jpg`** — JPEG 700KB 이하 · 1536×864

```
On the same flat forest path, seen from slightly behind and to the side: A has stopped walking in the foreground-left, standing still with shoulders slightly lowered and one hand resting on the trunk of a cedar tree beside him, a dark silhouette against the brighter path. Several steps ahead on the path, the three COMPANIONS have paused and are turning back to look at him, also silhouettes. Quiet overcast light between the trees. The mood is uneasy but calm.
```

## 5. DOC-05-TURN — A씨 혼자 돌아서고 일행은 멀어짐 (2장 · 5장③)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/DOC-05-TURN.jpg`** — JPEG 700KB 이하 · 1536×864

```
The same forest path seen from a low angle in the middle of the trail. On the left half, A walks alone back the way he came, toward the camera-left edge, head slightly down, a silhouette. On the right half, far ahead along the path, the three COMPANIONS continue walking away into the forest, small silhouettes. The empty stretch of path between them is the center of the picture, emphasizing the growing distance. Soft, slightly darker afternoon light.
```

## 6. DOC-06-EMPTY — 텅 빈 오후의 숲길 (3장 · 4장)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/DOC-06-EMPTY.jpg`** — JPEG 700KB 이하 · 1536×864

```
The same flat forest path in the early afternoon, completely empty. A light wind moves the leaves and ferns; a few dry leaves lie on the path. Tall cedar trunks on both sides, moss-covered black volcanic stones, cool gray-green light, a quiet and lonely atmosphere. No people, no animals, no objects left on the path.
```

## 7. DOC-07-CALL — 일행이 주위를 둘러보고 한 명이 신고 (3장)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/DOC-07-CALL.jpg`** — JPEG 700KB 이하 · 1536×864

```
Near the trail entrance at the edge of the forest, where the path meets a small gravel clearing. The three COMPANIONS are seen as silhouettes against the bright clearing: one looks back toward the dark forest path with a hand shading the eyes, one looks around to the side, and the one with the brimmed hiking hat holds a phone to the ear, the phone's blank screen giving a faint glow on the hand. A's figure is nowhere in the picture. Overcast early-afternoon light, a worried, searching mood.
```

## 8. DOC-08-SEARCH — 119 구급대원들이 숲을 수색 (3장)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/DOC-08-SEARCH.jpg`** — JPEG 700KB 이하 · 1536×864

```
Inside the same mid-mountain forest beside the path, four RESCUERS spread out between the cedar trunks, searching through ferns and low bamboo grass, seen as silhouettes against the hazy light deeper in the forest. Their helmets and the thin reflective stripes on their dark uniforms catch the light. One rescuer in the foreground is turned away from the camera, scanning to the right. Afternoon light, urgent but controlled atmosphere.
```

## 9. DOC-09-FOUND — 대원이 덤불 쪽을 가리키며 동료를 부름 (3장)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/DOC-09-FOUND.jpg`** — JPEG 700KB 이하 · 1536×864

```
In the forest a little off the path, one RESCUER in the middle ground, a silhouette, points down toward a patch of dense ferns and low shrubs in the lower-right of the picture while turning his head to call the others; two other RESCUERS hurry toward him from the left between the tree trunks. Nothing and no one is visible inside the ferns — the person who was found is completely hidden by the plants and is not shown at all. Afternoon light through the trees.
```

## 10. DOC-10-STRETCHER — 들것을 들고 급히 숲길을 내려감 (4장)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/DOC-10-STRETCHER.jpg`** — JPEG 700KB 이하 · 1536×864

```
On the forest path, four RESCUERS carry a rescue stretcher quickly down the trail toward the camera, seen as dark silhouettes against bright light behind them. The person on the stretcher is fully covered by a plain dark gray blanket and is shown only as a low, indistinct shape — no head, face, hands or feet visible. Motion in their steps, dry leaves lifting at their feet. Serious, respectful mood.
```

## 11. DOC-11-AMBULANCE — 숲 입구 도로의 구급차 (4장)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/DOC-11-AMBULANCE.jpg`** — JPEG 700KB 이하 · 1536×864

```
A narrow mountain road at the edge of the Jeju forest in late afternoon. A white ambulance van with plain red side stripes and glowing red-and-blue emergency lights on its roof waits with its rear doors open; the van has no letters, numbers, emblems or logos anywhere. Two RESCUERS as silhouettes stand near the rear doors. Tall cedars behind, the emergency light casting a soft red and blue glow on the road and tree trunks. Slight motion blur on the flashing lights.
```

## 12. MED-12-HEART — 사람 심장과 심장을 감싼 혈관 (5장①)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/MED-12-HEART.jpg`** — JPEG 700KB 이하 · 1536×864

```
A realistic human heart, three-quarter front view, slightly to the left of center, with the coronary arteries clearly visible running over its surface like branching red vessels. A soft glow around the heart against the dark background. Calm, clean documentary medical visualization.
```

## 13. MED-13-ARTERY — 안쪽이 좁아진 혈관 단면 (5장①)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/MED-13-ARTERY.jpg`** — JPEG 700KB 이하 · 1536×864

```
A long, horizontal cutaway view of one artery running from left to right across the picture, sliced open lengthwise. On the left the inside is wide and smooth with red blood cells flowing freely; toward the center a pale yellowish fatty plaque builds up on the inner wall and narrows the channel to a small gap; on the right the blood cells squeeze through the narrow opening. Realistic but clean and not gory, dark background.
```

## 14. MED-14-BODY — 반투명 상반신 실루엣과 빛나는 심장 (5장② · 8장)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/MED-14-BODY.jpg`** — JPEG 700KB 이하 · 1536×864

```
A semi-transparent, glass-like silhouette of an adult human upper body facing the viewer, from the top of the head to the waist, arms relaxed at the sides, centered in the picture. No face details — the head is a smooth outline. Inside the chest, only the heart is visible, glowing softly red; the rest of the body is a cool blue-gray translucent outline. Leave the chest, upper stomach, both arms, the jaw and the shoulders clearly visible and uncluttered.
```

## 15. MED-15-BRAIN — 옆모습 머리 속 뇌, 혈류가 끊겨 어두워짐 (5장④)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/MED-15-BRAIN.jpg`** — JPEG 700KB 이하 · 1536×864

```
A semi-transparent side-view silhouette of an adult human head and neck facing right, centered, with no face details (smooth outline). Inside the head, a realistic brain; a thin red blood vessel rises from the neck into the brain. The front of the brain still has a soft warm glow while the rest is fading into cool dim gray, suggesting the blood flow has stopped. Calm, serious mood.
```

## 16. DOC-16-SEONGPANAK — 초봄 바람 부는 한라산 돌길 탐방로 (6장)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/DOC-16-SEONGPANAK.jpg`** — JPEG 700KB 이하 · 1536×864

```
Early morning in late winter to early spring on a long, gently rising mountain trail on Hallasan in Jeju at about 1,100 meters: a path of rough black volcanic stones and short stretches of plain wooden decking, dense low bamboo grass on both sides, leafless trees bending in a strong wind, patches of old snow in the shade, gray clouds moving fast. No people.
```

## 17. DOC-17-SUMMER — 한여름 폭염 아래 바위 산길 (6장)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/DOC-17-SUMMER.jpg`** — JPEG 700KB 이하 · 1536×864

```
A hot midsummer morning on a rocky Korean mountain trail: a narrow path between large pale rocks and dark-green summer forest, harsh bright sunlight already high, heat haze shimmering over the rocks, cicada-season stillness, the sky pale and washed out. A generic mountain, not any identifiable landmark. No people.
```

## 18. DOC-18-AUTUMN — 가을 단풍이 든 바위 능선 등산로 (6장)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/DOC-18-AUTUMN.jpg`** — JPEG 700KB 이하 · 1536×864

```
A mid-October morning on a Korean mountain: a trail running along a rocky ridge between maple and oak trees in deep red, orange and yellow, granite rocks, the next ridges fading blue in the distance, clear cool autumn light. A generic mountain, not any identifiable landmark. No people.
```

## 19. DOC-19-HALLA-AUTUMN — 늦가을 한라산 숲 하산길 (6장)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/DOC-19-HALLA-AUTUMN.jpg`** — JPEG 700KB 이하 · 1536×864

```
Late October on a Hallasan forest trail in Jeju, seen looking downhill: a path of black volcanic stones descending between trees with brown and golden late-autumn leaves, low bamboo grass, gray overcast sky with drizzle in the air. Far down the path, one OTHER HIKER, a small silhouette from behind, is walking down. Damp, cold, quiet atmosphere.
```

## 20. DOC-20-RIDGE — 새벽 운해 위 겹겹의 산 능선 (7장)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/DOC-20-RIDGE.jpg`** — JPEG 700KB 이하 · 1536×864

```
A vast dawn view over layers of large Korean mountain ridges rising above a sea of clouds, the ridgelines fading from dark blue-gray in front to pale in the distance, a faint pink-orange glow at the horizon. Wide, calm and solemn, with a lot of quiet space in the upper half of the picture. Generic mountains, no identifiable landmark. No people.
```

## 21. DOC-21-CITY — 밤 도시와 구급차 불빛 (7장)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/DOC-21-CITY.jpg`** — JPEG 700KB 이하 · 1536×864

```
A high view over a Korean city at night: apartment blocks and streets with countless small lights, and along one main road a long-exposure trail of red-and-blue emergency lights from a moving ambulance, blurred into streaks. Dark blue night sky with a faint glow. No readable signs, no letters or numbers anywhere. No visible people.
```

## 22. DOC-22-NIGHT-PREP — 등산 전날 밤 거실 탁자 (8장)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/DOC-22-NIGHT-PREP.jpg`** — JPEG 700KB 이하 · 1536×864

```
Evening inside a quiet Korean apartment living room, lit only by a warm floor lamp behind the scene. On a low wooden table in the foreground, neatly laid out: a small hiking daypack, a water bottle, a folded windbreaker, a plain white medicine packet with no printing, and a few sheets of a blank health check-up report with only plain lines (no letters or numbers). Behind the table, one OTHER HIKER sits on a sofa as a dark silhouette against the lamp light, holding one sheet of the report and looking down at it. Calm, thoughtful mood.
```

## 23. DOC-23-SIT — 바위에 앉은 사람과 옆에서 통화하는 일행 (8장)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/DOC-23-SIT.jpg`** — JPEG 700KB 이하 · 1536×864

```
On the same kind of flat Jeju forest path, two OTHER HIKERS as silhouettes against the brighter path behind them: one sits on a flat black volcanic rock at the side of the path, leaning forward slightly and resting; the other crouches right beside them, one hand on their shoulder, the other holding a phone to the ear, the phone's blank screen glowing faintly. Calm, caring, not panicked. Soft daylight through the trees.
```

## 24. DOC-24-END — 오후 햇살 둘레길을 나란히 걷는 일행 (마무리)

**저장 경로: `crisis/source/hallasan-simjeongji-2026-11/images/DOC-24-END.jpg`** — JPEG 700KB 이하 · 1536×864

```
Late afternoon on the same Jeju mid-mountain forest path, warm golden sunlight streaming low through the cedar trunks in long rays. A small group of four OTHER HIKERS walks slowly side by side away from the camera, close together, seen from behind as silhouettes against the warm light. Peaceful, hopeful, quiet ending mood.
```
