from todo.models import Task
from todo.logic import add_task, mark_done, format_tasks


def test_add_task():
    tasks = []
    tasks = add_task(tasks, "Сходить в магазин")
    assert len(tasks) == 1
    assert tasks[0].description == "Сходить в магазин"
    assert tasks[0].id == 1
    assert not tasks[0].done

def test_mark_done_success():
    tasks = [Task(id=1, description="Почистить зубы")]
    result = mark_done(tasks, 1)
    assert result is True
    assert tasks[0].done is True

def test_mark_done_failure():
    tasks = [Task(id=1, description="Прочитать книгу")]
    result = mark_done(tasks, 2)
    assert result is False
    assert tasks[0].done is False

def test_format_tasks():
    tasks = [
        Task(id=1, description="Сделать дз", done=False),
        Task(id=2, description="Погулять", done=True),
    ]
    lines = format_tasks(tasks)
    assert lines == [
        "1. Сделать дз [❌]",
        "2. Погулять [✅]"
    ]
