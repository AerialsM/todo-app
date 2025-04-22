from flask import render_template, request, redirect, url_for, flash
from todo.storage import load_tasks, save_tasks
from todo.logic import add_task, mark_done, edit_task, toggle_task_status, delete_task


def configure_routes(app):
    @app.route("/")
    def index():
        tasks = load_tasks()
        return render_template("index.html", tasks=tasks)

    @app.route("/add", methods=["POST"])
    def add():
        desc = request.form.get("description", "").strip()
        if desc:
            tasks = load_tasks()
            old_len = len(tasks)
            tasks = add_task(tasks, desc)
            if len(tasks) == old_len:
                flash("Такая задача уже есть", "warning")
            else:
                save_tasks(tasks)
        return redirect(url_for("index"))

    @app.route("/delete/<int:task_id>")
    def delete(task_id):
        tasks = load_tasks()
        if delete_task(tasks, task_id):
            save_tasks(tasks)
        return redirect(url_for("index"))

    @app.route("/done/<int:task_id>")
    def done(task_id):
        tasks = load_tasks()
        if mark_done(tasks, task_id):
            save_tasks(tasks)
        return redirect(url_for("index"))

    @app.route("/toggle/<int:task_id>")
    def toggle(task_id):
        tasks = load_tasks()
        if toggle_task_status(tasks, task_id):
            save_tasks(tasks)
        return redirect(url_for("index"))

    @app.route("/edit/<int:task_id>", methods=["GET", "POST"])
    def edit(task_id):
        tasks = load_tasks()
        task = next((t for t in tasks if t.id == task_id), None)

        if not task:
            flash("Задача не найдена", "error")
            return redirect(url_for("index"))

        if request.method == "POST":
            new_desc = request.form.get("description", "").strip()
            if not new_desc:
                flash("Описание не может быть пустым", "warning")
            elif any(t.description == new_desc and t.id != task_id for t in tasks):
                flash("Задача с таким описанием уже существует", "warning")
            else:
                edit_task(tasks, task_id, new_desc)
                save_tasks(tasks)
            return redirect(url_for("index"))

        return render_template("edit.html", task=task)

