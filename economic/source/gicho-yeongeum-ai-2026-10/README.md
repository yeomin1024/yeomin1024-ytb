# gicho-yeongeum-ai-2026-10 — 기초연금 AI 실사 영상 쇼츠 (쇼츠만)

버전: v1.0 — 2026-10-18 — 사용자 지시 "기초연금 신청 못해서 좌절한 할아버지 영상 1분 만들건데 대본 만들고 영상을 만들기 위한 이미지를 chatgpt보고 생성하라고 할건데 뭐라고 하면 돼?"

- 롱폼 없음 — 보내는 곳은 기존 롱폼 `economic/source/gicho-yeongeum-2026-10/`. 숫자·사실은 그 롱폼의 계산(`calc/calc.py`)·README 4번 표에서만.
- 쇼츠 하나만 두는 폴더: 같은 롱폼에 이미 쇼츠가 있어서(내레이션 도구는 롱폼 폴더마다 쇼츠 하나) 따로 둠. '롱폼 하나에 쇼츠 하나' 규칙과 다름 — `shorts/shorts.md` 머리 표.

| 파일 | 내용 |
|---|---|
| `shorts/gicho-yeongeum-ai-2026-10-shorts.txt` | 대본 11문장 (내레이션·자막의 원본) |
| `shorts/gicho-yeongeum-ai-2026-10-shorts.srt` | 자막 (`srt_tool.py build` — 추정 시각, 오디오가 생기면 다시) |
| `shorts/shorts.md` | 대본·장면 표 · 근거 · 영상 만드는 법 · 다음 할 일 |
| `shorts/scenes/chatgpt.md` | ChatGPT 에 넘기는 장면 그림 11장 프롬프트 |
| `shorts/scenes/clips.json` | 장면마다 영상 움직임 프롬프트 (videogen `start_images` 용) |
