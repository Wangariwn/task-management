from datetime import datetime

from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

tasks = []

def add_task(title, description, due_date):

    if not validate_task_title(title):
        return

    if not validate_task_description(description):
        return

    if not validate_due_date(due_date):
        return

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)

    print("Task added successfully!")

def mark_task_as_complete(index, tasks=tasks):

    if index < 0 or index >= len(tasks):
        print("Invalid task number.")
        return

    tasks[index]["completed"] = True

    print("Task marked as complete!")

def view_pending_tasks(tasks=tasks):

    found = False

    for i, task in enumerate(tasks):

        if not task["completed"]:
            found = True

            print(
                f"{i + 1}. {task['title']} - "
                f"{task['description']} "
                f"(Due: {task['due_date']})"
            )

    if not found:
        print("No pending tasks.")

def calculate_progress(tasks=tasks):

    if len(tasks) == 0:
        progress = 0
    else:
        completed = 0

        for task in tasks:
            if task["completed"]:
                completed += 1

        progress = (completed / len(tasks)) * 100

    return progress