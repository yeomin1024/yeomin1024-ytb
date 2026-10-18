# gicho-yeongeum-ai-2026-10-shorts — AI 실사 영상 쇼츠: 기초연금을 안 된다고 믿다 놓친 할아버지

버전: v1.1 — 2026-10-18 — **테스트로 음성·자막 없이 영상만** (사용자 지시 "이건 그냥 테스트 용이라서 음성도 안붙여도 되니까 썸네일 만들었으니 다음 단계 진행해") — 3-1번 셀.
이전 v1.0 — 2026-10-18 — 사용자 지시 "기초연금 신청 못해서 좌절한 할아버지 영상 1분 만들건데 대본 만들고 영상을 만들기 위한 이미지를 chatgpt보고 생성하라고 할건데 뭐라고 하면 돼?"

| 항목 | 값 |
|---|---|
| 형식 | **AI 실사 영상 쇼츠 (새 시도)** — 장면 그림 11장(ChatGPT) → 그림마다 짧은 클립(`videogen/` `start_images`) → 내레이션·자막을 얹음. 기존 쇼츠의 HTML 인포그래픽 대신 |
| 보내는 곳 | 롱폼 `gicho-yeongeum-2026-10` (기초연금 — 집 한 채에 국민연금까지 있어도) |
| ⚠️ 규칙과 다른 점 | `shorts_guide.md` 4번 '롱폼 하나에 쇼츠 하나' — 이 롱폼에는 이미 쇼츠(`gicho-yeongeum-2026-10-shorts`, 박씨 부부)가 올라가 있다. 이 영상은 **둘째 쇼츠**가 된다 → 올릴지·기존 쇼츠를 바꿀지는 사용자가 정한다. 그래서 폴더를 따로 두었다 (내레이션 도구는 롱폼 폴더마다 쇼츠 대본 하나만 찾음) |
| 넣지 않는 것 | 롱폼의 '왜'(소득인정액·재산을 소득으로 바꾸는 법·선정기준액)와 '고치는 법'(신청 방법·지난 달 몫·이의신청) — 대본·그림 모두. 마지막 장면도 외출·서류 같은 '할 일'을 보여 주지 않음 |
| 각색 | 인물 '최씨 할아버지 부부'·아들·추석에 아들이 계산해 본 장면은 지어낸 것. **숫자·결과는 롱폼 그대로** (67세 부부 · 서울 공시가격 5억 원 아파트 · 국민연금 둘이 합쳐 170만 원 · 기초연금 부부 최소 월 41만 9,640원 · 1년 약 500만 원). 기존 쇼츠(박씨 부부, 이웃과 저녁)와 다른 이름·경위 |
| 길이 | 11문장 · 287음절 (`srt_tool.py` — 쇼츠 기준 285~315) · 도구 추정 60.4초 × 기존 쇼츠 실측 비율 0.84 → **약 51초** (기존 기초연금 쇼츠 277음절 = 실제 48.9초) |
| 자막 | `srt_tool.py build`·`check` ✅ — 문장 11 = 자막 11, 모두 두 줄 안, 나뉜 문장 0 |
| 목소리 | 진행자 H04 하나 (`voices/host.json`) — Kaggle 내레이션 셀이 이 대본을 찾음 (`tts_narration.py` 쇼츠 `gicho-yeongeum-ai-2026-10-shorts`) |

## 1. 제목 — 나중에 (B 단계, `economic/guides/quick_package.md` 4번 — 2안을 보여 주고 사용자가 고름)

## 2. 대본 · 장면

| # | 대본 | 역할 | 장면 그림 | 영상 움직임 (videogen 클립 프롬프트) |
|---|---|---|---|---|
| 1 | 67세 최씨 할아버지 부부는 기초연금을 매달 41만 원 넘게 놓치고 있었습니다. | 핵심 한 문장 · 첫 화면 | `scenes/scene_01.png` — 거실 소파의 부부 — 할아버지는 놓친 돈을 알고 좌절(고개 떨굼·이마에 손), 아내가 등을 쓸어 줌 | The grandfather slowly lowers his head further and rubs his forehead in regret while his wife gently strokes his back; subtle natural motion, static camera, normal speed. |
| 2 | 서울 아파트 공시가격은 5억 원, 국민연금은 둘이 합쳐 한 달 170만 원이에요. | 배경 — 집·연금 | `scenes/scene_02.png` — 서울 아파트 단지 바깥 — 사람 없이, 오후 햇살 (간판·글자 없음) | Slow gentle camera push-in toward the apartment buildings, leaves moving slightly in the breeze, calm atmosphere. |
| 3 | 할아버지는 집도 있고 연금도 받으니, 기초연금은 당연히 안 된다고 믿었습니다. | 믿은 것 — 안 된다고 생각 | `scenes/scene_03.png` — 식탁에서 신문을 내려놓고 손사래 치며 웃는 할아버지 — '우린 안 돼'라는 확신(아직 모름) | The grandfather chuckles and waves his hand dismissively, then sips his tea; the wife shrugs; static camera, natural speed. |
| 4 | 그런데 추석에 아들이 공시가격과 연금을 묻더니 계산해 봤어요. | 알게 된 경위 — 추석, 아들이 계산 | `scenes/scene_04.png` — 추석 — 거실 낮은 상에 송편·과일, 아들이 수첩에 적으며 부모에게 묻는 중 (수첩 글씨 안 보이게) | The son writes in his notebook and looks up asking a question, the grandfather answers with a small shrug, the wife pours tea; static camera, natural speed. |
| 5 | 결과는 두 분 모두 기초연금을 받을 수 있다는 것이었습니다. | 결과 — 두 분 모두 대상 | `scenes/scene_05.png` — 아들이 놀란 얼굴로 부모를 바라보며 설명 — 할아버지는 몸을 앞으로 기울여 듣고 놀람 | The son explains with an open hand gesture, the grandfather leans closer with growing surprise, the wife slowly covers her mouth; static camera, natural speed. |
| 6 | 둘이 합쳐 한 달에 최소 41만 9,640원이었어요. | 금액 — 한 달 최소 41만 9,640원 | `scenes/scene_06.png` — 할아버지 얼굴 클로즈업 — 눈이 커지며 굳는 순간 | Very slow push-in on the grandfather's face as his eyes widen and he stops breathing for a moment; static, subtle motion, normal speed. |
| 7 | 할아버지는 한참 동안 아무 말도 하지 못했습니다. | 반응 — 한참 아무 말 못 함 | `scenes/scene_07.png` — 소파에 혼자 앉아 멍하니 바닥을 보는 할아버지, 뒤에서 걱정스레 보는 아내 — 정적 | Almost still: the grandfather stares at the floor and blinks slowly, the wife in the background shifts her weight and watches him; curtains move slightly; static camera. |
| 8 | 안 된다고만 생각하고, 신청은커녕 알아본 적도 없었거든요. | 까닭 — 알아본 적도 없음 | `scenes/scene_08.png` — 고개를 떨구고 두 손으로 얼굴을 감싼 할아버지 — 후회 (좌절 얼굴: 미간·처진 어깨) | The grandfather slowly shakes his bowed head in regret behind his hands, shoulders sinking; static camera, natural speed. |
| 9 | 신청하지 않고 1년이 지나면, 놓치는 돈은 약 500만 원입니다. | 걸린 것 — 1년에 약 500만 원 | `scenes/scene_09.png` — 밤, 스탠드 불빛 아래 창가에 홀로 서서 밖을 내다보는 할아버지의 뒷모습과 옆얼굴 — 시간이 흐른 느낌 | The grandfather lets out a long sigh, his shoulders drop, city lights twinkle softly outside; static camera, natural speed. |
| 10 | 최씨 부부, 지금이라도 기초연금을 받을 수 있을까요? | 질문 — 지금이라도 받을 수 있을까 | `scenes/scene_10.png` — 다음 날 아침, 식탁에 마주 앉은 부부 — 아내가 할아버지 손을 잡고, 서로 바라보며 희미한 희망 | The wife squeezes his hand, the grandfather looks up at her and gives a small hopeful nod; static camera, natural speed. |
| 11 | 우리 집도 되는지, 지금 할 일까지 아래 영상에서 확인하세요. | 끝 — 아래 영상에서 확인 | `scenes/scene_11.png` — 할아버지 정면 상반신 — 결심한 듯 카메라를 바라봄 (외출·서류 같은 '할 일'은 보이지 않게) | The grandfather takes a breath, straightens his back and gives a small determined nod toward the camera; static camera, natural speed. |

- 그림 프롬프트(영어 원문)는 `scenes/chatgpt.md` — ChatGPT 에 넘기는 파일. 그림은 `scenes/scene_01.png` ~ `scene_11.png`.
- 모든 장면이 **같은 인물·옷·거실**: 할아버지(67세, 은회색 짧은 머리, 짙은 초록 니트 가디건 + 연회색 셔츠) · 아내(66세, 짙은 갈색 파마머리, 버건디 니트) · 아들(약 40세, 검은 뿔테 안경, 차콜 니트) · 밝은 아파트 거실(밝은 오크 마루·베이지 소파·낮은 나무 탁자·왼쪽 큰 창). 기존 썸네일들(남색 카디건·하늘색 체크 셔츠 등)과 옷이 겹치지 않게.
- 그림 안에 글자·숫자·돈·서류 없음 (정보는 자막이 전함). 세로 9:16, 얼굴은 높이 20~60%·너비 가운데 80%, 아래 30%는 자막 자리.
- 색 = 뜻 규칙(빨강 손해 등)은 자막·그래픽을 얹을 때 적용 — 그림은 실사.

## 3. 영상 만드는 법 (그림·오디오가 생긴 뒤)
1. **그림 11장** — ChatGPT 가 만든 그림을 사용자가 Claude 대화에 번호 순서대로 붙임 → Claude 검수(같은 인물·옷·방, 글자 없음, 세로, 얼굴 자리·좌절 표정) → `scenes/scene_NN.png` 로 main.
2. **오디오 먼저** — Kaggle 내레이션 셀(`guides/tts_guide.md` 3번)을 돌리면 이 대본의 `shorts/narration.mp3` 가 생김. 문장별 시작·끝 시각은 `tts_narration.json`.
3. **클립 11개** — `videogen` Kaggle 셀에 `model="wan2.2-5b-fast"`(빠름) 또는 `"wan2.2-14b-i2v"`(품질), 세로 `width=704, height=1280, upscale_to="1080x1920"`, `start_images` = 장면 그림 + `scenes/clips.json` 의 움직임 프롬프트. 클립 길이는 문장 길이에 맞춤 (오디오가 생긴 뒤 문장별 길이를 넣음 — Claude 가 셀을 만들어 줌).
4. **합치기** — 클립을 문장 시각에 맞춰 잇고, 내레이션·구운 자막(한 문장 = 자막 하나)·음량(-14 LUFS)을 얹어 `economic/out/gicho-yeongeum-ai-2026-10-shorts/final_1080p.mp4`. 렌더 뒤 완성 장면을 Claude 가 직접 본다.

## 3-1. 테스트 실행 — 음성·자막 없이 영상만 (v1.1)
1. 그림 11장을 `scenes/scene_01.png` ~ `scene_11.png` 로 main 에 (Claude 대화에 번호 순서대로 붙이면 Claude 가 검수·커밋, 또는 https://github.com/yeomin1024/yeomin1024-ytb/upload/main/economic/source/gicho-yeongeum-ai-2026-10/shorts/scenes 에 그 이름으로 끌어다 놓기).
2. Kaggle 의 videogen 셀(`videogen/README.md` 2번 — *GPU T4 x2*, *Internet On*)에서 `SETTINGS` 만 아래로 바꿔 실행. 같은 세션에서 처음이면 설치·모델 다운로드가 먼저.
3. 결과: `/kaggle/working/outputs/<실행시각>/` — 클립 11개(`media/`) · 이어 붙인 704x1280 · 최종 1080x1920 `…_lanczos.mp4` · `run.log`(`[SUMMARY] stage timings` = 실제 시간).
- 검증 (`videogen` v1.3.0 `make_config`·`resolve_params`·`clip_frames_for`): 그림 11장 · 704x1280 · 클립 121프레임(5.04초) · 합계 약 55.5초 · 1080x1920 은 ×2 뒤 가운데 맞춤(가로 2.2% 잘림). ChatGPT 세로 2:3(1024x1536) 그림은 704x1280 에 맞추며 양옆 약 17.5% 잘림 (20% 넘으면 로그 경고).
- 클립 길이는 모두 5초 — 음성이 없어 문장 길이에 맞추지 않음. 컷 사이에 장면이 바뀜.

```python
BASE = "https://raw.githubusercontent.com/yeomin1024/yeomin1024-ytb/main/economic/source/gicho-yeongeum-ai-2026-10/shorts/scenes/"
SETTINGS = dict(
    model="wan2.2-5b-fast",          # 빠름 (TI2V 5B + FastWan 3-step). 품질 비교는 "wan2.2-14b-i2v"
    width=704, height=1280,          # 세로 (5B 는 32 배수) → 키운 뒤 가운데 맞춰 1080x1920
    upscale_to="1080x1920", upscaler="lanczos",
    clip_sec=5,                      # 장면 11개 × 5초 ≈ 55초 (음성 없음 — 테스트)
    prompt="Photorealistic Korean family drama, natural lifelike motion at normal speed, static camera.",
    start_images=[
        {"image": BASE + "scene_01.png",
         "prompt": "The grandfather slowly lowers his head further and rubs his forehead in regret while his wife gently strokes his back; subtle natural motion, static camera, normal speed."},
        {"image": BASE + "scene_02.png",
         "prompt": "Slow gentle camera push-in toward the apartment buildings, leaves moving slightly in the breeze, calm atmosphere."},
        {"image": BASE + "scene_03.png",
         "prompt": "The grandfather chuckles and waves his hand dismissively, then sips his tea; the wife shrugs; static camera, natural speed."},
        {"image": BASE + "scene_04.png",
         "prompt": "The son writes in his notebook and looks up asking a question, the grandfather answers with a small shrug, the wife pours tea; static camera, natural speed."},
        {"image": BASE + "scene_05.png",
         "prompt": "The son explains with an open hand gesture, the grandfather leans closer with growing surprise, the wife slowly covers her mouth; static camera, natural speed."},
        {"image": BASE + "scene_06.png",
         "prompt": "Very slow push-in on the grandfather's face as his eyes widen and he stops breathing for a moment; static, subtle motion, normal speed."},
        {"image": BASE + "scene_07.png",
         "prompt": "Almost still: the grandfather stares at the floor and blinks slowly, the wife in the background shifts her weight and watches him; curtains move slightly; static camera."},
        {"image": BASE + "scene_08.png",
         "prompt": "The grandfather slowly shakes his bowed head in regret behind his hands, shoulders sinking; static camera, natural speed."},
        {"image": BASE + "scene_09.png",
         "prompt": "The grandfather lets out a long sigh, his shoulders drop, city lights twinkle softly outside; static camera, natural speed."},
        {"image": BASE + "scene_10.png",
         "prompt": "The wife squeezes his hand, the grandfather looks up at her and gives a small hopeful nod; static camera, natural speed."},
        {"image": BASE + "scene_11.png",
         "prompt": "The grandfather takes a breath, straightens his back and gives a small determined nod toward the camera; static camera, natural speed."},
    ],
    seed=42,
)
```

## 6. 숫자·사실 근거 (롱폼 `gicho-yeongeum-2026-10` README 4번 표 · 대본에 있는 것만)
| 문장 | 숫자·사실 | 근거 |
|---|---|---|
| 1 | 매달 41만 원 넘게 | 부부 최소 월 41만 9,640원 (27만 9,760 + 13만 9,880) — 내려 잡음 |
| 2 | 67세 · 서울 아파트 공시가격 5억 원 · 국민연금 둘이 합쳐 한 달 170만 원 | 롱폼 예시 부부 (README 3번, 대본 '예시 부부의 형편') |
| 5 | 두 분 모두 받을 수 있음 | 소득인정액 약 309만 원 < 부부 선정기준액 395만 2천 원 |
| 6 | 둘이 합쳐 한 달 최소 41만 9,640원 | README 4번 |
| 9 | 신청 안 하고 1년이 지나면 약 500만 원 | 41만 9,640 × 12 = 503만 5,680원 → 내려 잡음 (기존 쇼츠·썸네일과 같은 문장) |
- 2026년 숫자 (선정기준액·기준연금액은 해마다 바뀜 — 설명란에 '숫자는 2026년 10월 기준').

## 8. 다음에 할 일
- [x] 사용자: ChatGPT 로 그림 11장 만듦 (2026-10-18)
- [ ] 사용자: 그림 11장을 Claude 대화에 번호 순서대로 붙이기(또는 scenes/ 에 직접 올리기) → Claude 검수·커밋 → 3-1번 셀 실행
- [ ] Claude: 그림 검수·커밋 → 오디오가 생기면 문장 길이에 맞춘 videogen 셀 · 합치기
- [ ] 사용자: 둘째 쇼츠로 올릴지(규칙과 다름) 정하기 → B 단계(제목 2안·썸네일·설명란·`upload.md`)
