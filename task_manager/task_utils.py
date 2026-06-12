from validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

tasks = []


def add_task(title, description, due_date):
    title = validate_task_title(title)
    description = validate_task_description(description)
    due_date = validate_due_date(due_date)

    if title is None or description is None or due_date is None:
        return False

    tasks.append({
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    })

    print("Task added successfully!")
    return True


def mark_task_as_complete(index):
    try:
        index = int(index) - 1

        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            print("Task marked as complete!")
            return True

        return False

    except ValueError:
        return False


def view_pending_tasks():
    for i, task in enumerate(tasks):
        if not task["completed"]:
            print(f"[{i}] {task['title']} - {task['description']} - {task['due_date']}")


def calculate_progress():
    if len(tasks) == 0:
        return 0.0

    completed = sum(1 for t in tasks if t["completed"])
    return float((completed / len(tasks)) * 100)