import os

TODO_FILE = 'todo_list.txt'

def load_tasks():
    if not os.path.isfile(TODO_FILE):
        return []
    with open(TODO_FILE, 'r') as file:
        tasks = file.readlines()
    return [task.strip() for task in tasks]

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def display_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print()

def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f'Task "{task}" added.')

def delete_task(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f'Task "{removed_task}" deleted.')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("Options:")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Delete a task")
        print("4. Exit")
        
        choice = input("Choose an option: ").strip()
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
