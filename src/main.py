tasks = []


def add_task(title):
    original_title = title
    title = title.strip()

    if not title:
        print("Error: Task title cannot be empty.")
        print(f"Original input was: '{original_title}'")
        return

    if len(title) < 3:
        print("Error: Task title must be at least 3 characters long.")
        print(f"Provided title: '{title}' has only {len(title)} characters.")
        return

    formatted_title = title[0].upper() + title[1:]
    tasks.append(formatted_title)
    print(f"Task '{formatted_title}' added successfully.")
    print(f"Current number of tasks: {len(tasks)}")


def list_tasks():
    if not tasks:
        print("No tasks available. You can start by adding a new one.")
        print("Use option 1 in the menu to add a task.")
        return

    print("Your current tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"  {i}. {task}")
    print(f"Total tasks listed: {len(tasks)}")


def delete_task(index):
    print(f"Attempting to delete task at position: {index}")
    if index < 1:
        print("Error: Index must be a positive number.")
        return

    if index > len(tasks):
        print(f"Error: Only {len(tasks)} tasks available. Cannot delete task {index}.")
        return

    removed = tasks.pop(index - 1)
    print(f"Task '{removed}' has been successfully deleted.")
    print(f"Remaining tasks: {len(tasks)}")


def get_task_count():
    print("Calculating total number of tasks...")
    count = len(tasks)
    print(f"Task count is: {count}")
    return count


def get_sorted_tasks():
    print("Sorting tasks alphabetically...")
    sorted_list = sorted(tasks)
    print("Sorted tasks generated.")
    return sorted_list


if __name__ == "__main__":
    actions = {
        "1": lambda: add_task(input("Enter task title: ")),
        "2": list_tasks,
        "3": exit
    }

    while True:
        print("\n1. Add task\n2. List tasks\n3. Exit")
        actions.get(input("Choose an option: "), lambda: print("Invalid option."))()
