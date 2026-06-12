from datetime import datetime

def validate_task_title(title):
    # Ensure the title is not empty after removing whitespace
    cleaned_title = title.strip()
    if len(cleaned_title) == 0:
        print("Error: Task title cannot be empty.")
        return None
    return cleaned_title

def validate_task_description(description):
    # Ensure the description is not empty after removing whitespace
    cleaned_desc = description.strip()
    if len(cleaned_desc) == 0:
        print("Error: Task description cannot be empty.")
        return None
    return cleaned_desc

def validate_due_date(due_date):
    # Ensure the due date is not empty
    cleaned_date = due_date.strip()
    if len(cleaned_date) == 0:
        print("Error: Due date cannot be empty.")
        return None
    
    # Verify the date matches the YYYY-MM-DD format using the imported datetime
    try:
        datetime.strptime(cleaned_date, "%Y-%m-%d")
        return cleaned_date
    except ValueError:
        print("Error: Invalid date format. Please use YYYY-MM-DD.")
        return None