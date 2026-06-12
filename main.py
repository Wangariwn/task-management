# Import functions from local task_utils module
from task_utils import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    calculate_progress,
)

# Define the main function
def main():
    # Initialize the task list data structure required by the system
    task_list = []
    
    try:
        while True:
            print("\nTask Management System")
            print("1. Add Task")
            print("2. Mark Task as Complete")
            print("3. View Pending Tasks")
            print("4. View Progress")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                title = input("Enter task title: ")
                description = input("Enter task description: ")
                due_date = input("Enter due date (YYYY-MM-DD): ")
                add_task(task_list, title, description, due_date)

            elif choice == "2":
                # Display pending tasks first so the user can see their index numbers
                view_pending_tasks(task_list)
                try:
                    # Users see 1-based indices; convert to 0-based internally
                    task_index = int(input("Enter the task number to mark as complete: "))
                    if task_index <= 0:
                        print("Invalid input. Please enter a positive number.")
                    else:
                        mark_task_as_complete(task_list, task_index - 1)
                except ValueError:
                    print("Invalid input. Please enter a number.")

            elif choice == "3":
                view_pending_tasks(task_list)

            elif choice == "4":
                calculate_progress(task_list)

            elif choice == "5":
                print("Exiting the program...")
                break
            else:
                print("Invalid choice. Please try again.")
    except (EOFError, KeyboardInterrupt):
        # Graceful exit on EOF (no more input) or user interrupt
        return

if __name__ == "__main__":
    main()