# schemas.py
# This file defines what valid metadata looks like

METADATA_SCHEMA = {
    "id": {
        "type": str,
        "required": True
    },
    "title": {
        "type": str,
        "required": True
    },
    "description": {
        "type": str,
        "required": False
    },
    "duration_sec": {
        "type": int,
        "required": True,
        "min": 1
    },
    "platform": {
        "type": str,
        "required": True,
        "allowed": ["youtube", "instagram"]
    }
}
