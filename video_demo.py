"""
Video Demo — clean terminal output for screen recording.
Run this during Scene 5 of the video pitch.
"""

import time
import json
from pathlib import Path

def slow_print(text, delay=0.02):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def section(title):
    print()
    slow_print(f"  {'=' * 60}")
    slow_print(f"   {title}")
    slow_print(f"  {'=' * 60}")
    time.sleep(0.5)

def subsection(title):
    print()
    slow_print(f"   {title}")
    slow_print(f"   {'─' * len(title)}")
    time.sleep(0.3)


if __name__ == "__main__":

    # ── Title ──
    print("\n" * 2)
    slow_print("  ╔════════════════════════════════════════════════════════════╗", 0.008)
    slow_print("  ║                                                          ║", 0.008)
    slow_print("  ║   BIOMEDICAL CONTEXT LAYER — ONTOLOGY ENGINE             ║", 0.008)
    slow_print("  ║   Palantir Foundry Hydration Pattern                     ║", 0.008)
    slow_print("  ║                                                          ║", 0.008)
    slow_print("  ║   DATA + MODELS  →  ONTOLOGY  →  ANALYTICS              ║", 0.008)
    slow_print("  ║                                                          ║", 0.008)
    slow_print("  ╚════════════════════════════════════════════════════════════╝", 0.008)
    time.sleep(1)

    # ── Step 1: Hydration ──
    section("STEP 1: HYDRATE THE ONTOLOGY (WRITES)")

    from ontology_engine import OntologyEngine, HydrationPipeline, OntologyReader, DB_PATH

    if DB_PATH.exists():
        DB_PATH.unlink()
    engine = OntologyEngine()

    slow_print("\n   Engine initialized. SQLite backend ready.")
    time.sleep(0.5)

    slow_print("\n   Ingesting 4 evaluation result sets...")
    time.sleep(0.3)

    pipeline = HydrationPipeline(engine)
    result_files = sorted(Path(__file__).parent.glob("eval_*_results.json"))
    total_obj, total_lnk = 0, 0

    for rf in result_files:
        with open(rf) as f:
            data = json.load(f)
        results = data.get("results", [])
        if not results:
            continue
        h = pipeline.hydrate_from_results(str(rf))
        total_obj += h["objects"]
        total_lnk += h["links"]
        pipeline.hydrated = {"objects": 0, "links": 0}
        time.sleep(0.3)

    time.sleep(0.5)
    slow_print(f"\n   TOTAL: {total_obj} objects, {total_lnk} links hydrated")

    # ── Step 2: Ontology Stats ──
    section("STEP 2: ONTOLOGY OBJECTS")

    stats = engine.stats()
    objects = stats["objects"]
    for obj_type, count in objects.items():
        if count > 0:
            bar = "█" * min(count, 40)
            slow_print(f"   {obj_type:<20} {bar} {count}", 0.01)
            time.sleep(0.15)

    time.sleep(0.3)
    slow_print(f"\n   Total Objects : {stats['total_objects']}")
    slow_print(f"   Total Links   : {stats['total_links']}")
    slow_print(f"   Link Types    : JUDGES, PRODUCES, EVALUATED_IN, TESTS, EXHIBITS, BELONGS_TO")

    # ── Step 3: Judge Leaderboard ──
    section("STEP 3: JUDGE LEADERBOARD (READS)")

    reader = OntologyReader(engine)
    board = reader.judge_leaderboard()

    slow_print(f"   {'Judge':<22} {'Accuracy':>10} {'FP Rate':>10} {'Cost':>10}  {'Biases':>8}", 0.01)
    slow_print(f"   {'─' * 22} {'─' * 10} {'─' * 10} {'─' * 10}  {'─' * 8}", 0.01)
    time.sleep(0.2)

    for j in board:
        acc = f"{j['accuracy']:.1%}"
        fp = f"{j['false_pass_rate']:.1%}"
        cost = f"${j['total_cost']:.4f}"
        bias_count = sum(j['bias_profile'].values()) if j['bias_profile'] else 0
        marker = " ◄ WINNER" if j['accuracy'] == 1.0 and j['method'] == 'wr' else ""
        marker = " ◄ WORST" if j['accuracy'] < 0.6 and j['method'] in ('nr', 'bias_test') else marker
        slow_print(f"   {j['label']:<22} {acc:>10} {fp:>10} {cost:>10}  {bias_count:>8}{marker}", 0.01)
        time.sleep(0.2)

    # ── Step 4: Bias Report ──
    section("STEP 4: BIAS DETECTION (AUTOMATIONS)")

    bias = reader.bias_report()
    for bias_type, info in bias.items():
        icon = "⚠" if info["count"] > 0 else "✓"
        slow_print(f"   {icon}  {bias_type:<20} : {info['count']} instances detected", 0.015)
        time.sleep(0.2)

    slow_print(f"\n   Automations fired on every BiasPattern creation — zero manual triage needed.")

    # ── Step 5: Hardest Tests ──
    section("STEP 5: HARDEST TEST CASES (FUNCTIONS)")

    hardest = reader.hardest_tests(8)
    for t in hardest:
        diff_bar = "▓" * int(t["difficulty"] * 20)
        slow_print(f"   {t['test_id']:<28} [{t['category']:<18}] {diff_bar} {t['difficulty']:.0%}", 0.01)
        time.sleep(0.15)

    # ── Step 6: Cost ──
    section("STEP 6: COST ANALYSIS")

    cost = reader.cost_analysis()
    slow_print(f"   Total eval cost    : ${cost['total_cost_usd']:.4f}")
    slow_print(f"   Total verdicts     : {cost['total_verdicts']}")
    slow_print(f"   Cost per verdict   : ${cost['cost_per_verdict']:.6f}")
    time.sleep(0.3)
    slow_print(f"\n   Deterministic cost : $0.0000  (<1ms latency)")
    slow_print(f"   LLM Judge cost     : $0.0022  (3,467ms latency)")
    slow_print(f"   Monthly @ 1K/day   : $0.00 vs $131.64")

    # ── Step 7: Actions ──
    section("STEP 7: ACTIONS (MUTATIONS THROUGH ONTOLOGY)")

    slow_print("   > Promoting best judge: judge-wr (Wide-Retrieval LLM)...")
    result = engine.execute_action("promote_judge", "judge-wr")
    time.sleep(0.3)
    slow_print(f"     Status: {result['status']}")

    slow_print("   > Queuing rerun for failed test cases...")
    result = engine.execute_action("rerun_failed", list(engine.get_objects_by_type("EvalRun"))[0].object_id)
    time.sleep(0.3)
    slow_print(f"     Status: {result['status']} — {result.get('failed_count', '?')} cases to rerun")

    # ── Close ──
    print("\n" * 1)
    slow_print("  ╔════════════════════════════════════════════════════════════╗", 0.008)
    slow_print("  ║                                                          ║", 0.008)
    slow_print("  ║   YOUR CONTEXT IS YOUR EDGE                              ║", 0.008)
    slow_print("  ║                                                          ║", 0.008)
    slow_print("  ║   Context is what you BUILD (ontology + rules + graph)   ║", 0.008)
    slow_print("  ║   Not what you BUY (LLM judge API calls)                ║", 0.008)
    slow_print("  ║                                                          ║", 0.008)
    slow_print("  ╚════════════════════════════════════════════════════════════╝", 0.008)
    print()
