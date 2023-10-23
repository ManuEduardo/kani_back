import json
from pathlib import Path

def get_config():
    BASE_DIR = Path(__file__).resolve(strict=True).parent
    json_file = open(f"{BASE_DIR}/config.json")
    config = json.load(json_file)
    json_file.close()
    return config