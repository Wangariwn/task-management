from datetime import datetime

# Import validation functions
from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    # Validate each input using the imported functions
    valid_title = validate_task_title(title)
    valid_desc = validate_task_description(description)
    valid_date = validate_due_date(due_date)
    
    # If any validation returns None, stop and do not add the task
    if valid_title is None or valid_desc is None or valid_date is None:
        print("Failed to add task due to validation errors.")
        return False
        
    # Create the task dictionary layout required by the assignment
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
        # Check if the index falls within the valid range of the list
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            print("Task marked as complete!")
            return True
        else:
            print("Error: Invalid task index number.")
            return False
    except (TypeError, ValueError):
        print("Error: Please provide a valid index number.")
        return False

# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    # Filter out completed items to isolate pending ones
    pending_items = [t for t in tasks if not t["completed"]]
    
    if len(pending_items) == 0:
        print("No pending tasks found.")
        return
        
    print("\n--- Pending Tasks ---")
    # Display the items along with their original index numbers
    for idx, task in enumerate(tasks):
        if not task["completed"]:
            print(f"[{idx}] Title: {task['title']}")
            print(f"    Description: {task['description']}")
            print(f"    Due Date: {task['due_date']}\n")

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    total_tasks = len(tasks)
    if total_tasks == 0:
        print("Progress: No tasks available. (0.0% Complete)")
        return 0.0
        
    completed_count = sum(1 for task in tasks if task["completed"])
    progress = (completed_count / total_tasks) * 100
    
    print(f"Progress: {completed_count}/{total_tasks} tasks completed ({progress:.1f}%)")
    return progress