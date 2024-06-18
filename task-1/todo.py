import os
import json

TODO_FILE = 'todo_list.json'

def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return []

def save_todos(todos):
    with open(TODO_FILE, 'w') as file:
        json.dump(todos, file, indent=4)

def display_todos(todos):
    if not todos:
        print("No tasks in the to-do list.")
        return
    for index, todo in enumerate(todos, start=1):
        status = "Done" if todo['done'] else "Not Done"
        print(f"{index}. [{status}] {todo['task']}")

def add_todo():
    task = input("Enter the task: ")
    todos = load_todos()
    todos.append({"task": task, "done": False})
    save_todos(todos)
    print("Task added!")

def update_todo():
    todos = load_todos()
    display_todos(todos)
    task_num = int(input("Enter the task number to update: ")) - 1
    if 0 <= task_num < len(todos):
        new_task = input("Enter the new task: ")
        todos[task_num]['task'] = new_task
        save_todos(todos)
        print("Task updated!")
    else:
        print("Invalid task number.")

def mark_done():
    todos = load_todos()
    display_todos(todos)
    task_num = int(input("Enter the task number to mark as done: ")) - 1
    if 0 <= task_num < len(todos):
        todos[task_num]['done'] = True
        save_todos(todos)
        print("Task marked as done!")
    else:
        print("Invalid task number.")

def delete_todo():
    todos = load_todos()
    display_todos(todos)
    task_num = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_num < len(todos):
        todos.pop(task_num)
        save_todos(todos)
        print("Task deleted!")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nTo-Do List")
        print("1. View tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Mark task as done")
        print("5. Delete task")
        print("6. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            todos = load_todos()
            display_todos(todos)
        elif choice == '2':
            add_todo()
        elif choice == '3':
            update_todo()
        elif choice == '4':
            mark_done()
        elif choice == '5':
            delete_todo()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
