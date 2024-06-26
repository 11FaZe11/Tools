tasks = []

while True:
    print("\nSimple Todo List")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")

    option = int(input("Choose an option: "))

    if option == 1:
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added.")
    elif option == 2:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    elif option == 3:
        task_num = int(input("Enter the task number to delete: "))
        if task_num > 0 and task_num <= len(tasks):
            del tasks[task_num - 1]
            print("Task deleted.")
        else:
            print("Invalid task number.")
    elif option == 4:
        break
    else:
        print("Invalid option. Please try again.")
