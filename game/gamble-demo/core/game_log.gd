# VERSION: v0.1.0 — 2026-11-26 — 첫 데모: 단계별 구조화 로그
#
# 형식: [STAGE] [t=000123ms] key=value key=value ...
# 단계: MATCH(설정·끝) · DEAL(패 배분) · TURN(턴·시선) · AI_CARD/AI_LATE(AI 카드 결정)
#       · CHEAT(속임수·단서) · NOTICE(알아챔) · SUSPECT(의심 갱신) · ACCUSE(고발 판정)
#       · REVEAL(공개) · ROUND(판 결과) · REFUSE(규칙상 거절된 행동 — WARNING)
# 수준은 GameLog.level 로 바꿈 (시뮬레이션은 WARNING — 줄마다 출력하지 않아 빠름)
extends RefCounted

enum Level { DEBUG, INFO, WARNING, ERROR }

static var level: int = Level.INFO
## true 면 출력하지 않고 lines 에 모음 (시험용)
static var capture: bool = false
static var lines: PackedStringArray = PackedStringArray()


static func enabled(lv: int) -> bool:
	return lv >= level


static func write(lv: int, stage: String, fields: Dictionary = {}) -> void:
	if lv < level:
		return
	var parts := PackedStringArray()
	parts.append("[%s]" % stage)
	parts.append("[t=%06dms]" % Time.get_ticks_msec())
	for k in fields:
		parts.append("%s=%s" % [k, _fmt(fields[k])])
	var line := " ".join(parts)
	if capture:
		lines.append(line)
	elif lv >= Level.WARNING:
		printerr(line)
	else:
		print(line)


static func debug(stage: String, fields: Dictionary = {}) -> void:
	write(Level.DEBUG, stage, fields)


static func info(stage: String, fields: Dictionary = {}) -> void:
	write(Level.INFO, stage, fields)


static func warn(stage: String, fields: Dictionary = {}) -> void:
	write(Level.WARNING, stage, fields)


static func _fmt(v) -> String:
	if typeof(v) == TYPE_FLOAT:
		return "%.3f" % v
	return str(v)
