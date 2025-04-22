from todo.models import Task
from todo.storage import load_tasks, save_tasks
from todo.logic import add_task, mark_done, format_tasks


def main():
    tasks = load_tasks()
    while True:
        print("\n===== TODO =====")
        for line in format_tasks(tasks):
            print(line)

        print("\nДоступные команды:")
        print("1 - Добавить задачу")
        print("2 - Отметить как выполненную")
        print("3 - Выйти")

        cmd = input("Выберите команду: ")
        if cmd == "1":
            desc = input("Введите описание задачи: ")
            tasks = add_task(tasks, desc)
            save_tasks(tasks)
        elif cmd == "2":
            try:
                task_id = int(input("Введите ID задачи для отметки: "))
                if mark_done(tasks, task_id):
                    save_tasks(tasks)
                else:
                    print("Задача не найдена.")
                save_tasks(tasks)
            except ValueError:
                print("Некорректный ввод.")
        elif cmd == "3":
            break
        else:
            print("Неизвестная команда.")

if __name__ == "__main__":
    main()