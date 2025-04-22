import os
import tempfile
import json
from todo.models import Task
from todo.storage import load_tasks, save_tasks


def test_save_and_load_tasks():
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        temp_path = tmp.name

    try:
        # Подготовим тестовые данные
        tasks = [
            Task(id=1, description="Сходить в магазин", done=False),
            Task(id=2, description="Позвонить маме", done=True)
        ]

        # Сохраняем и загружаем
        save_tasks(tasks, filename=temp_path)
        loaded = load_tasks(filename=temp_path)

        # Проверки
        assert len(loaded) == 2
        assert loaded[0].id == 1
        assert loaded[0].description == "Сходить в магазин"
        assert not loaded[0].done
        assert loaded[1].done is True
    finally:
        os.remove(temp_path)

def test_load_tasks_returns_empty_if_file_not_found():
    tasks = load_tasks(filename="non_existent.json")
    assert tasks == []

def test_save_tasks_creates_file():
    tasks = [Task(id=1, description="Тест", done=False)]
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        temp_path = tmp.name
    try:
        os.remove(temp_path)
        save_tasks(tasks, filename=temp_path)
        assert os.path.exists(temp_path)
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

def test_task_serialization_manual():
    task = Task(id=1, description="Тест", done=False)
    # сериализация
    serialized = json.dumps(task.__dict__, ensure_ascii=False)
    assert '"description": "Тест"' in serialized
    # десериализация
    obj = json.loads(serialized)
    restored = Task(**obj)
    assert restored.id == 1
    assert restored.description == "Тест"
    assert restored.done is False