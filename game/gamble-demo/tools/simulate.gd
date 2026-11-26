# VERSION: v0.2.0 — 2026-11-26 — AI 대 AI 밸런스 (실시간 규칙): 승률 · 엿보기 성공률 · 시도당 들킴 · 고발 정확도
# 이전 VERSION: v0.1.1 — 2026-11-26 — 인자 읽는 줄의 타입 추론 오류 고침
#
# 실행 (저장소 맨 위에서):
#   godot --headless --path game/gamble-demo --script res://tools/simulate.gd -- --matches=1000 --seed=42
# 자리 0 = 사람 대신 정책(ai_brain.gd p0_*), 자리 1 = AI. 출력: [SIM] key=value … (조합마다 한 줄)
extends SceneTree

const AiBrain = preload("res://core/ai_brain.gd")
const GambleMatch = preload("res://core/match.gd")
const GameLog = preload("res://core/game_log.gd")

const SCENARIOS := [
	["honest", "honest"],
	["cheater", "honest"],
	["cheater", "watcher"],
	["honest", "cheater"],
	["watcher", "cheater"],
	["watcher", "gambler"],
	["cheater", "cheater"],
]


func _initialize() -> void:
	var args := _parse_args(OS.get_cmdline_user_args())
	var n := int(args.get("matches", "1000"))
	var base_seed := int(args.get("seed", "42"))
	GameLog.level = GameLog.Level.ERROR   # 매치마다 줄을 찍지 않음 (속도)
	print("[SIM] matches=%d base_seed=%d dt=%.2f rounds=%d" % [n, base_seed, GambleMatch.SIM_DT, GambleMatch.ROUNDS])
	for sc in SCENARIOS:
		_run(str(sc[0]), str(sc[1]), n, base_seed)
	quit(0)


func _run(k0: String, k1: String, n: int, base_seed: int) -> void:
	var t0 := Time.get_ticks_usec()
	var wins := [0, 0, 0]
	var out2 := [0, 0]
	var keys := ["peek_tries", "peek_done", "caught", "accusations", "hits", "timeouts"]
	var sums := {}
	for k in keys:
		sums[k] = [0, 0]
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
		if str(m.end_reason) == "CAUGHT_TWICE":
			out2[1 - int(m.winner)] += 1
		for k in keys:
			for s in 2:
				sums[k][s] += int(m.stats[k][s])
		for s in 2:
			score_sum[s] += int(m.scores[s])
	var ms := (Time.get_ticks_usec() - t0) / 1000.0
	var parts := PackedStringArray()
	parts.append("[SIM] seat0=%s seat1=%s n=%d" % [k0, k1, n])
	parts.append("win0_pct=%.1f win1_pct=%.1f draw_pct=%.1f" % [_pct(wins[0], n), _pct(wins[1], n), _pct(wins[2], n)])
	for s in 2:
		parts.append("tries%d_avg=%.2f peek_ok%d=%.3f caught_per_try%d=%.3f out2_%d_pct=%.1f acc%d_avg=%.2f acc_hit%d=%.3f score%d_avg=%.2f" % [
			s, float(sums["peek_tries"][s]) / n, s, _ratio(sums["peek_done"][s], sums["peek_tries"][s]),
			s, _ratio(sums["caught"][s], sums["peek_tries"][s]), s, _pct(out2[s], n),
			s, float(sums["accusations"][s]) / n, s, _ratio(sums["hits"][s], sums["accusations"][s]), s, float(score_sum[s]) / n])
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
