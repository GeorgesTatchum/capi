import json
import os

from app.models import Backlog


def load_backlog():
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, "static", "backlog.json")
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return Backlog(**data)
    except FileNotFoundError:
        return Backlog(project="", sprint="", backlog=[])


def save_backlog(backlog: Backlog):
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, "static", "backlog.json")
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(backlog.dict(), file, indent=4)
    except FileNotFoundError:
        return []
