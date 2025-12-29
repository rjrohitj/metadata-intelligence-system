# validator.py

from src.schemas import METADATA_SCHEMA


def validate_item(item: dict) -> list[str]:
    errors = []

    for field, rules in METADATA_SCHEMA.items():
        # Required field check
        if rules.get("required") and field not in item:
            errors.append(f"missing_field:{field}")
            continue

        if field in item:
            value = item[field]

            # Type check
            if not isinstance(value, rules["type"]):
                errors.append(f"invalid_type:{field}")
                continue

            # Allowed values check
            if "allowed" in rules and value not in rules["allowed"]:
                errors.append(f"invalid_value:{field}")

    return errors

from src.llm_schema import LLM_ENRICHMENT_SCHEMA


def validate_llm_output(output: dict) -> list[str]:
    errors = []

    if not isinstance(output, dict):
        return ["llm_output_not_dict"]

    for field, rules in LLM_ENRICHMENT_SCHEMA.items():
        if rules.get("required") and field not in output:
            errors.append(f"missing_field:{field}")
            continue

        if field in output:
            value = output[field]

            if not isinstance(value, rules["type"]):
                errors.append(f"invalid_type:{field}")
                continue

            if rules["type"] == list:
                item_type = rules.get("item_type")
                for item in value:
                    if not isinstance(item, item_type):
                        errors.append(f"invalid_list_item:{field}")
                        break

            if "allowed" in rules and value not in rules["allowed"]:
                errors.append(f"invalid_value:{field}")

    return errors
