import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def show_menu():
    print("\nTo-Do Manager")
    print("1. View tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Exit")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added.")

def delete_task(tasks):
    view_tasks(tasks)
    index = int(input("Enter task number to delete: "))
    if 1 <= index <= len(tasks):
        removed = tasks.pop(index - 1)
        print(f"Removed task: {removed}")
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
