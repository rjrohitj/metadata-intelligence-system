# llm_schema.py

LLM_ENRICHMENT_SCHEMA = {
    "topics": {
        "type": list,
        "required": True,
        "item_type": str
    },
    "content_type": {
        "type": str,
        "required": True,
        "allowed": ["news", "sports", "entertainment", "education", "other"]
    },
    "safety_flags": {
        "type": list,
        "required": True,
        "item_type": str
    }
}
