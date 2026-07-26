tasks = []
while True:
    print("=======TO-DO-LIST=========")
    print("1. Add Task")
    print("2. view Task")
    print("3. Exit")
    choice = input("enter your choice:")
    if choice == "1":
       task = input("enter a new tasks: ")
       tasks.append(task)
       
       print("task added successfully!")
    elif choice == "2":
        if len(tasks) == 0:
            print("no task available.")
        else:
            print("\nyour tasks:")
            for i, task in enumerate(tasks, start=1):
              print(f"{i}. {task}")
    elif choice == "3":
        print("thank you")
        break
    else:
        print("Invalid choice. please try again.")               

    