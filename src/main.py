tasks = []

def add_task(title):
    title = title.strip()
    if not title:
        print("Error: Task title cannot be empty.")
        return
    if len(title) < 3:
        print("Error: Task title must be at least 3 characters long.")
        return
    tasks.append(title)
    print(f"Task '{title}' added.")

def list_tasks():
    if not tasks:
        print("No tasks available.")
        return
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def delete_task(index):
    try:
        removed = tasks.pop(index - 1)
        print(f"Task '{removed}' deleted.")
    except IndexError:
        print("Error: Invalid task number.")

def get_task_count():
    return len(tasks)

def get_sorted_tasks():
    """Return a sorted list of tasks alphabetically."""
    return sorted(tasks)

if __name__ == "__main__":
    while True:
        print("\n1. Add task\n2. List tasks\n3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            add_task(title)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            break
        else:
            print("Invalid option.")