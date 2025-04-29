task_list = []
while True:
    print("\nTask Manager", "1. Add Task", "2. View Tasks", "3. Remove Task", "4. Mark Task as Done", "5. Exit")
    x = input("Enter your option (1-5): ")

    if not x.isdigit() or int(x) < 1 or int(x) > 5:
        print("Please enter a number between 1 and 5")
        continue
    option = int(x)

    if option == 1:
        task = input("Enter your Task : ")
        task_list.append(task)
        print("Task added successfully")
    elif option == 2:
        if not task_list:
            print("No tasks available")
        for x in task_list:
            print("Tasks:", x)
    elif option == 3:
        if not task_list:
            print("No tasks available")
        else:
            for x in task_list:
                print("Tasks:", x)
            task = input("Enter the task you want to remove: ")
            task_list.remove(task)
            print("Task removed successfully")
    elif option == 4:
        for i in range(len(task_list)):
            if task_list[i] == task:
                task_list[i] = "Done"
        if not task_list:
            print("No tasks to mark as done")
    elif option == 5:
        print("Exiting Task Manager")
        break

