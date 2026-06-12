from datetime import datetime

# Import validation functions
from validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

# Define tasks list exactly as provided in the template
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    valid_title = validate_task_title(title)
    valid_desc = validate_task_description(description)
    valid_date = validate_due_date(due_date)
    
    if valid_title is None or valid_desc is None or valid_date is None:
        return False
        
    new_task = {
        "title": valid_title,
        "description": valid_desc,
        "due_date": valid_date,
        "completed": False
    }
    
    tasks.append(new_task)
    print("Task added successfully!")
    return True

# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    try:
        idx = int(index)
        if 0 <= idx < len(tasks):
            tasks[idx]["completed"] = True
            print("Task marked as complete!")
            return True
        else:
            return False
    except (TypeError, ValueError):
        return False

# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    for idx, task in enumerate(tasks):
        if not task["completed"]:
            print(f"[{idx}] Title: {task['title']}")
            print(f"    Description: {task['description']}")
            print(f"    Due Date: {task['due_date']}")

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    total_tasks = len(tasks)
    if total_tasks == 0:
        progress = 0.0
        print(progress)
        return progress
        
    completed_count = sum(1 for task in tasks if task["completed"])
    progress = float((completed_count / total_tasks) * 100)
    print(progress)
    return progress