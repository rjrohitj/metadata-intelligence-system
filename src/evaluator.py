# evaluator.py

def evaluate(outputs: dict, gold: list[dict]) -> dict:
    report = {"pass": 0, "fail": 0, "details": []}

    gold_by_id = {g["id"]: g["expected"] for g in gold}

    for item_id, enriched in outputs.items():
        expected = gold_by_id.get(item_id)
        if not expected:
            continue

        ok = True
        for key, val in expected.items():
            if enriched.get(key) != val:
                ok = False

        if ok:
            report["pass"] += 1
        else:
            report["fail"] += 1
            report["details"].append({
                "id": item_id,
                "expected": expected,
                "actual": enriched
            })

    return report