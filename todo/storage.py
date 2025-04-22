import json
from typing import List
from todo.models import Task


def load_tasks(filename: str = "tasks.json") -> List[Task]:
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Task(**item) for item in data]
    except FileNotFoundError:
        return []

def save_tasks(tasks: List[Task], filename: str = "tasks.json") -> None:
    with open(filename, "w", encoding="utf-8") as f:
        json.dump([task.__dict__ for task in tasks], f, ensure_ascii=False, indent=2)