from datetime import datetime

def validate_task_title(title):
    if title.strip() == "":
        print("Title cannot be empty.")
        return False
    return True

def validate_task_description(description):
    if description.strip() == "":
        print("Description cannot be empty.")
        return False
    return True

def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        print("Due date must be in YYYY-MM-DD format.")
        return False