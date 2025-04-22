from todo.models import Task


def add_task(tasks: list[Task], desc: str) -> list[Task]:
    if any(task.description == desc for task in tasks):
        return tasks  # Задача с таким описанием уже есть
    new_id = max([task.id for task in tasks], default=0) + 1
    tasks.append(Task(id=new_id, description=desc))
    return tasks

def delete_task(tasks: list[Task], task_id: int) -> bool:
    original_len = len(tasks)
    tasks[:] = [task for task in tasks if task.id != task_id]
    if len(tasks) < original_len:
        # Переиндексация: заново пронумеровать задачи с 1
        for idx, task in enumerate(tasks, start=1):
            task.id = idx
        return True
    return False

def edit_task(tasks: list[Task], task_id: int, new_description: str) -> bool:
    for task in tasks:
        if task.id == task_id:
            task.description = new_description
            return True
    return False

def mark_done(tasks: list[Task], task_id: int) -> bool:
    for task in tasks:
        if task.id == task_id:
            task.done = True
            return True
    return False

def toggle_task_status(tasks: list[Task], task_id: int) -> bool:
    for task in tasks:
        if task.id == task_id:
            task.done = not task.done
            return True
    return False

def format_tasks(tasks: list[Task]) -> list[str]:
    return [
        f"{task.id}. {task.description} [{'✅' if task.done else '❌'}]"
        for task in tasks
    ]






