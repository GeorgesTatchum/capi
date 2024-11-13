import json


def load_backlog():
    try:
        with open("backlog.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_backlog(backlog):
    with open("backlog.json", "w") as file:
        json.dump(backlog, file, indent=4)
