# main.py

import json
from src.validator import validate_item, validate_llm_output
from src.llm_client import call_llm
from src.evaluator import evaluate


def load_data():
    with open("data/sample_input.json", "r") as f:
        return json.load(f)


def main():
    items = load_data()
    outputs = {}   # <-- MOVE outputs here

    for item in items:
        errors = validate_item(item)
        item_id = item.get("id", "UNKNOWN")

        if errors:
            print(f"INVALID: {item_id} -> {errors}")
            continue

        title = item.get("title", "")
        description = item.get("description", "")

        llm_output = call_llm(title, description)
        llm_errors = validate_llm_output(llm_output)

        if llm_errors:
            enriched = {
                "topics": [],
                "content_type": "other",
                "safety_flags": ["llm_failed"]
            }
        else:
            enriched = llm_output

        outputs[item_id] = enriched

        print(f"VALID: {item_id}")
        print("ENRICHED:", enriched)

    # ---- Evaluation MUST be here ----
    with open("data/gold.json", "r") as f:
        gold = json.load(f)

    report = evaluate(outputs, gold)
    print("EVAL REPORT:", report)


if __name__ == "__main__":
    main()
