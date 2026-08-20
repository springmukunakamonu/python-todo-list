todo_list = []

def add_todo_item():
    task = input("Enter the task: ")
    time = input("Enter the time for the task (e.g., 10:00 AM): ")
    todo_list.append((task, time))


def view_todo_list():
    print("\nTodo List:")

    for index, (task, time) in enumerate(todo_list, start=1):
        print(f"{index}.\n {task} at {time}")


def remove_todo_item():
    if not todo_list:
        print("\nNo tasks found yet, please input tasks and try again.")
        return

def view_todo_list():
    if not todo_list:
        print("\nNo tasks found yet, please input tasks and try again.")
        return

    print("\nTodo List:")
    for index, (task, time) in enumerate(todo_list, start=1):
        print(f"{index}. {task} at {time}")


def remove_todo_item():
    if not todo_list:
        print("\nNo tasks found yet, please input tasks and try again.")
        return

    view_todo_list()
    task_index = int(input("Enter the index or the name of the task to remove: ")) - 1

    if 0 <= task_index < len(todo_list):
        removed_task = todo_list.pop(task_index)
        print(f"\nTask '{removed_task[0]}' removed successfully!")
    else:
        print("\nInvalid task index.")

def main_menu():
    while True:
        print("--------------------------------")
        print("\nTodo List Menu:")
        print("--------------------------------")

        print("1.Add Todo Item")
        print("2. view Todo List")
        print("3. Remove Todo Item")
        print("4. Exit")

        choice = input("Enter your choice (1-4) and we will be at your service: ")

        if choice == "1":
            add_todo_item()
        elif choice == "2":
            view_todo_list()
        elif choice == "3":
            remove_todo_item()
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
