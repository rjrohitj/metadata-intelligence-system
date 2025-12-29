# llm_client.py

import subprocess
import json


def call_llm(title: str, description: str) -> dict:
    prompt = f"""
You are a metadata classification system.

Return ONLY valid JSON.
Do NOT add explanations.
Do NOT use markdown.

Schema:
{{
  "topics": [string],
  "content_type": one of ["news","sports","entertainment","education","other"],
  "safety_flags": [string]
}}

Input:
Title: "{title}"
Description: "{description}"
"""

    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=prompt,
        text=True,
        encoding="utf-8",
        errors="ignore",
        capture_output=True
    )

    raw_output = result.stdout.strip()

    try:
        return json.loads(raw_output)
    except json.JSONDecodeError:
        return {"_error": "invalid_json"}
