# VERSION: v0.8.0 — 2026-11-26 — 통계 칸: 정보(반사경·이어폰·가짜) · '!' 표시·미끼 · 협력자 부르기·연결 · 물건 확인·몸 수색 적중률 · 무효 턴
# 이전 VERSION: v0.5.0 — 2026-11-26 — 새 통계 칸: 정보(엿보기·협력자·가짜) · 들킴 · 가능성 불·미끼 · 밝혀내기 적중률 · 가리기·무작위·바꿔치기 · 시선 끌기·제스처
# 이전 VERSION: v0.4.0 — 2026-11-26 — 출력에 협력자·덮개·블러핑·준비 동작 칸 추가
# 이전 VERSION: v0.2.0 — 2026-11-26 — AI 대 AI 밸런스 (실시간 규칙): 승률 · 엿보기 성공률 · 시도당 들킴 · 고발 정확도
# 이전 VERSION: v0.1.1 — 2026-11-26 — 인자 읽는 줄의 타입 추론 오류 고침
#
# 실행 (저장소 맨 위에서):
#   godot --headless --path game/gamble-demo --script res://tools/simulate.gd -- --matches=1000 --seed=42
# 자리 0 = 사람 대신 AI, 자리 1 = AI. 출력: [SIM] key=value … (조합마다 한 줄, 자리마다 매치당 평균)
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
	["gambler", "watcher"],
	["cheater", "cheater"],
]
const KEYS := ["info_peek", "info_acc", "info_fake", "caught", "marks", "baits", "inspect", "inspect_hit", "search", "search_hit",
	"voids", "covers", "randoms", "fakes", "attentions", "acc_calls", "acc_connects", "objects_placed", "timeouts"]


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
	var sums := {}
	for k in KEYS:
		sums[k] = [0, 0]
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
		for k in KEYS:
			for s in 2:
				sums[k][s] += int(m.stats[k][s])
	var ms := (Time.get_ticks_usec() - t0) / 1000.0
	var parts := PackedStringArray()
	parts.append("[SIM] seat0=%s seat1=%s n=%d" % [k0, k1, n])
	parts.append("win0_pct=%.1f win1_pct=%.1f draw_pct=%.1f" % [_pct(wins[0], n), _pct(wins[1], n), _pct(wins[2], n)])
	for s in 2:
		var info := _avg(sums, "info_peek", s, n) + _avg(sums, "info_acc", s, n)
		parts.append("s%d: info=%.2f acc=%.2f fake=%.2f caught=%.2f out2_pct=%.1f marks=%.2f baits=%.2f calls=%.2f connects=%.2f inspect=%.2f inspect_hit=%.2f search=%.2f search_hit=%.2f voids=%.2f cov=%.2f rnd=%.2f fakes=%.2f att=%.2f placed=%.2f to=%.2f" % [
			s, info, _avg(sums, "info_acc", s, n), _avg(sums, "info_fake", s, n), _avg(sums, "caught", s, n), _pct(out2[s], n),
			_avg(sums, "marks", s, n), _avg(sums, "baits", s, n), _avg(sums, "acc_calls", s, n), _avg(sums, "acc_connects", s, n),
			_avg(sums, "inspect", s, n), _ratio(int(sums["inspect_hit"][s]), int(sums["inspect"][s])),
			_avg(sums, "search", s, n), _ratio(int(sums["search_hit"][s]), int(sums["search"][s])), _avg(sums, "voids", s, n),
			_avg(sums, "covers", s, n), _avg(sums, "randoms", s, n), _avg(sums, "fakes", s, n),
			_avg(sums, "attentions", s, n), _avg(sums, "objects_placed", s, n), _avg(sums, "timeouts", s, n)])
	parts.append("ms=%.0f" % ms)
	print(" ".join(parts))


func _avg(sums: Dictionary, key: String, s: int, n: int) -> float:
	return float(sums[key][s]) / maxi(n, 1)


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
