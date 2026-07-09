import json
import os

FILE = "data.json"

def load_data() -> dict:
    if not os.path.exists(FILE):
        return {}
    
    try:
        with open(FILE, "r", encoding = "utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

def save_data(data: dict):
    with open(FILE, "w", encoding = "utf-8") as f:
        json.dump(data, f, ensure_ascii = False, indent = 4)
        