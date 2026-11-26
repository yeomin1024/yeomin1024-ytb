# VERSION: v0.1.1 — 2026-11-26 — 인자 읽는 줄의 타입 추론 오류 고침
# 이전 VERSION: v0.1.0 — 2026-11-26 — AI 대 AI 밸런스 시뮬레이션 (성격 조합별 승률·적발률·고발 정확도)
#
# 실행 (저장소 맨 위에서):
#   godot --headless --path game/gamble-demo --script res://tools/simulate.gd -- --matches=2000 --seed=42
# 출력: [SIM] key=value … (조합마다 한 줄). 숫자를 바꾸면 core/cheat_rules.gd · core/ai_brain.gd 만 고치면 됨.
extends SceneTree

const AiBrain = preload("res://core/ai_brain.gd")
const GambleMatch = preload("res://core/match.gd")
const GameLog = preload("res://core/game_log.gd")

const SCENARIOS := [
	["honest", "honest"],
	["cheater", "honest"],
	["honest", "cheater"],
	["cheater", "watcher"],
	["watcher", "cheater"],
	["cheater", "cheater"],
	["bluffer", "watcher"],
]


func _initialize() -> void:
	var args := _parse_args(OS.get_cmdline_user_args())
	var n := int(args.get("matches", "1000"))
	var base_seed := int(args.get("seed", "42"))
	GameLog.level = GameLog.Level.WARNING   # 매치마다 줄을 찍지 않음 (속도)
	print("[SIM] matches=%d base_seed=%d rounds=%d note=seat0_commits_first_seat1_ai_late" % [n, base_seed, GambleMatch.ROUNDS])
	for sc in SCENARIOS:
		_run(str(sc[0]), str(sc[1]), n, base_seed)
	quit(0)


func _run(k0: String, k1: String, n: int, base_seed: int) -> void:
	var t0 := Time.get_ticks_usec()
	var wins := [0, 0, 0]
	var caught_out := [0, 0]
	var cheats := [0, 0]
	var fakes := [0, 0]
	var strikes := [0, 0]
	var acc := [0, 0]
	var hits := [0, 0]
	var score_sum := [0, 0]
	for i in n:
		var b0 = AiBrain.new()
		b0.configure(k0)
		var b1 = AiBrain.new()
		b1.configure(k1)
		var m = GambleMatch.new()
		m.setup(base_seed + i, b0, b1)
		m.run_auto()
		wins[int(m.winner)] += 1
		if m.end_reason == "CAUGHT_TWICE":
			caught_out[1 - int(m.winner)] += 1
		for s in 2:
			cheats[s] += int(m.stats["cheats"][s])
			fakes[s] += int(m.stats["fakes"][s])
			strikes[s] += int(m.strikes[s])
			acc[s] += int(m.stats["accusations"][s])
			hits[s] += int(m.stats["hits"][s])
			score_sum[s] += int(m.scores[s])
	var ms := (Time.get_ticks_usec() - t0) / 1000.0
	var parts := PackedStringArray()
	parts.append("[SIM] seat0=%s seat1=%s n=%d" % [k0, k1, n])
	parts.append("win0_pct=%.1f win1_pct=%.1f draw_pct=%.1f" % [_pct(wins[0], n), _pct(wins[1], n), _pct(wins[2], n)])
	for s in 2:
		parts.append("caught_out%d_pct=%.1f cheats%d_avg=%.2f fakes%d_avg=%.2f caught_per_cheat%d=%.3f accuse%d_avg=%.2f accuse_acc%d=%.3f score%d_avg=%.2f" % [
			s, _pct(caught_out[s], n), s, float(cheats[s]) / n, s, float(fakes[s]) / n,
			s, _ratio(strikes[s], cheats[s]), s, float(acc[s]) / n, s, _ratio(hits[s], acc[s]), s, float(score_sum[s]) / n])
	parts.append("ms=%.0f" % ms)
	print(" ".join(parts))


func _pct(a: int, n: int) -> float:
	return 100.0 * a / maxi(n, 1)


func _ratio(a: int, b: int) -> float:
	return float(a) / b if b > 0 else 0.0


func _parse_args(raw: PackedStringArray) -> Dictionary:
	var out := {}
	for a in raw:
		var arg: String = a
		if arg.begins_with("--") and arg.contains("="):
			var kv: PackedStringArray = arg.substr(2).split("=", true, 1)
			out[kv[0]] = kv[1]
	return out
