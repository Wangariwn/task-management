from datetime import datetime


def validate_task_title(title):
    if len(title) == 0:
        print("Error: Task title cannot be empty.")
        return None
    return title.strip()


def validate_task_description(description):
    if len(description) == 0:
        print("Error: Task description cannot be empty.")
        return None
    return description.strip()


def validate_due_date(due_date):
    if len(due_date) == 0:
        print("Error: Due date cannot be empty.")
        return None

    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return due_date.strip()

    except ValueError:
        print("Error: Invalid date format. Please use YYYY-MM-DD.")
        return None