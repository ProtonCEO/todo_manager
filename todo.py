import os

TODO_FILE = "todo.txt"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        tasks = [line.strip() for line in f.readlines()]
    return tasks

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("📋 No tasks yet.")
    else:
        print("\n📋 Your tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print()

tasks = load_tasks()

while True:
    print("📝 To-Do List Manager")
    print("[1] View tasks")
    print("[2] Add task")
    print("[3] Mark task as done")
    print("[4] Quit")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        show_tasks(tasks)
    elif choice == "2":
        new_task = input("Enter new task: ").strip()
        if new_task:
            tasks.append(new_task)
            save_tasks(tasks)
            print("✅ Task added.\n")
    elif choice == "3":
        show_tasks(tasks)
        try:
            done = int(input("Enter task number to mark as done: "))
            if 1 <= done <= len(tasks):
                removed = tasks.pop(done - 1)
                save_tasks(tasks)
                print(f"✅ Task '{removed}' marked as done.\n")
            else:
                print("❌ Invalid task number.\n")
        except ValueError:
            print("❌ Please enter a valid number.\n")
    elif choice == "4":
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid choice. Please pick 1–4.\n")
