# tasks = []

# def load_tasks():
#     try:
#         with open("tasks.txt", "r") as file:
#             for line in file:
#                 line = line.strip()
#                 if line.startswith("[x] "):
#                     tasks.append({"text": line[4:], "done": True})
#                 elif line.startswith("[ ] "):
#                     tasks.append({"text": line[4:], "done": False})
#     except FileNotFoundError:
#         pass

# def save_tasks():
#     with open("tasks.txt", "w") as file:
#         for task in tasks:
#             marker = "[x] " if task["done"] else "[ ] "
#             file.write(marker + task["text"] + "\n")

# def show_tasks():
#     if not tasks:
#         print("No tasks yet.")
#     else:
#         for index, task in enumerate(tasks, start=1):
#             status = "✓" if task["done"] else " "
#             print(f"{index}. [{status}] {task['text']}")

# def add_task():
#     new_task = input("Enter a new task: ")
#     tasks.append({"text": new_task, "done": False})
#     save_tasks()
    print(f"Added: {new_task}")

# def remove_task():
#     show_tasks()
#     if tasks:
#         choice = input("Enter the number of the task to remove: ")
#         index = int(choice) - 1
#         if 0 <= index < len(tasks):
#             removed = tasks.pop(index)
#             save_tasks()
#             print(f"Removed: {removed['text']}")
#         else:
#             print("Invalid task number.")

# def complete_task():
#     show_tasks()
#     if tasks:
#         choice = input("Enter the number of the task to mark complete: ")
#         index = int(choice) - 1
#         if 0 <= index < len(tasks):
#             tasks[index]["done"] = True
#             save_tasks()
#             print(f"Marked complete: {tasks[index]['text']}")
#         else:
#             print("Invalid task number.")

# load_tasks()

# while True:
#     print("\n1. Add task")
#     print("2. Show tasks")
#     print("3. Remove task")
#     print("4. Mark task complete")
#     print("5. Quit")
#     choice = input("Choose an option: ")

#     if choice == "1":
#         add_task()
#     elif choice == "2":
#         show_tasks()
#     elif choice == "3":
#         remove_task()
#     elif choice == "4":
#         complete_task()
#     elif choice == "5":
#         print("Goodbye!")
#         break
#     else:
#         print("Invalid choice, try again.")



tasks = []

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line.startswith("[x] "):
                    tasks.append({"text": line[4:], "done": True})
                elif line.startswith("[ ] "):
                    tasks.append({"text": line[4:], "done": False})
    except FileNotFoundError:
        pass

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            marker = "[x] " if task["done"] else "[ ] "
            file.write(marker + task["text"] + "\n")

def show_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        for index, task in enumerate(tasks, start=1):
            status = "✓" if task["done"] else " "
            print(f"{index}. [{status}] {task['text']}")

def add_task():
    new_task = input("Enter a new task: ")
    tasks.append({"text": new_task, "done": False})
    save_tasks()
    print(f"Added: {new_task}")

def remove_task():
    show_tasks()
    if tasks:
        choice = input("Enter the number of the task to remove: ")
        index = int(choice) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks()
            print(f"Removed: {removed['text']}")
        else:
            print("Invalid task number.")

def complete_task():
    show_tasks()
    if tasks:
        choice = input("Enter the number of the task to mark complete: ")
        index = int(choice) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            save_tasks()
            print(f"Marked complete: {tasks[index]['text']}")
        else:
            print("Invalid task number.")

load_tasks()

while True:
    print("\n1. Add task")
    print("2. Show tasks")
    print("3. Remove task")
    print("4. Mark task complete")
    print("5. Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        complete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")