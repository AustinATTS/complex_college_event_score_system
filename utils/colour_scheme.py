import json
import os

COLOR_SCHEME_FILE = "color_scheme.json"

def save_color_scheme(scheme):
    with open(COLOR_SCHEME_FILE, 'w') as f:
        json.dump(scheme, f)

def load_color_scheme():
    if os.path.exists(COLOR_SCHEME_FILE):
        with open(COLOR_SCHEME_FILE, 'r') as f:
            return json.load(f)
    return {"bg": "#FFFFFF", "fg": "#000000"}
