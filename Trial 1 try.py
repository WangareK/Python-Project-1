task_list = []

while True:
    print("\nTask Manager")
    print("1. Add Task\n2. View Tasks\n3. Remove Task\n4. Mark Task as Done\n5. Exit")

    x = input("Enter your option (1-5): ")

    if not x.isdigit() or int(x) < 1 or int(x) > 5:
        print("Please enter a number between 1 and 5")
        continue

    option = int(x)

    if option == 1:
        task = input("Enter your Task: ")
        task_list.append(task)
        print("Task added successfully")

    elif option == 2:
        if not task_list:
            print("No tasks available")
        else:
            print("\nTasks:")
            for i, task in enumerate(task_list):
                print(f"{i + 1}. {task}")

    elif option == 3:
        if not task_list:
            print("No tasks available")
        else:
            print("\nTasks:")
            for i, task in enumerate(task_list):
                print(f"{i + 1}. {task}")

            task_num = input("Enter the task number to remove: ")
            if task_num.isdigit() and 0 < int(task_num) <= len(task_list):
                removed = task_list.pop(int(task_num) - 1)
                print(f"Task '{removed}' removed successfully")
            else:
                print("Invalid task number")

    elif option == 4:
        if not task_list:
            print("No tasks to mark as done")
        else:
            print("\nTasks:")
            for i, task in enumerate(task_list):
                print(f"{i + 1}. {task}")

            task_num = input("Enter the task number to mark as done: ")
            if task_num.isdigit() and 0 < int(task_num) <= len(task_list):
                index = int(task_num) - 1
                task_list[index] = f"{task_list[index]} (Done)"
                print("Task marked as done")
            else:
                print("Invalid task number")

    elif option == 5:
        print("Exiting Task Manager")
        break