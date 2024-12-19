import json
import os


def load_backlog():
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, "static", "backlog.json")
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_backlog(backlog):
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, "static", "backlog.json")
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(backlog, file, indent=4)
    except FileNotFoundError:
        return []
