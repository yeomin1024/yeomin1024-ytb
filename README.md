# 업로드 대기 영상 (tools/upload_pack.py 가 늘 다시 짜는 커밋 하나짜리 브랜치)

- 아직 유튜브에 안 올린 완성 영상만 90MB 조각으로 둔다 — PC 의 tools/upload_web.py 가 받아 이어 붙이고 sha256 을 확인한다.
- 올린 영상(main 에 youtube.json)은 다음 pack 때 빠지고, 이 브랜치는 부모 없는 새 커밋으로 바뀐다 (강제 푸시).
- main 에는 영상이 들어가지 않는다. 확인값은 main 의 <주제>/source/<영상ID>/video.json.
