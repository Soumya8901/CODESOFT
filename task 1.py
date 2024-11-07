# To-Do List Application

# Initialize the to-do list
todo_list = []

def display_tasks():
    """Display all tasks in the to-do list."""
    if not todo_list:
        print("\nYour to-do list is empty!")
        return
    print("\nTo-Do List:")
    for idx, task in enumerate(todo_list, 1):
        status = "✔️ Completed" if task["completed"] else "❌ Incomplete"
        print(f"{idx}. {task['task']} - {status}")
    print()

def add_task():
    """Add a new task to the to-do list."""
    task = input("Enter the task: ")
    todo_list.append({"task": task, "completed": False})
    print(f"Task '{task}' added to the list.\n")

def mark_task_completed():
    """Mark a specific task as completed."""
    display_tasks()
    try:
        task_num = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_num <= len(todo_list):
            todo_list[task_num - 1]["completed"] = True
            print(f"Task {task_num} marked as completed.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid task number.\n")

def remove_task():
    """Remove a task from the to-do list."""
    display_tasks()
    try:
        task_num = int(input("Enter the task number to remove: "))
        if 1 <= task_num <= len(todo_list):
            removed_task = todo_list.pop(task_num - 1)
            print(f"Task '{removed_task['task']}' removed from the list.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid task number.\n")

def main():
    """Main function to interact with the to-do list."""
    while True:
        print("To-Do List Application")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task Completed")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            display_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_task_completed()
        elif choice == "4":
            remove_task()
        elif choice == "5":
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose between 1-5.\n")

if __name__ == "__main__":
    main()
