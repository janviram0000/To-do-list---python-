tasks = []

def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        if not tasks:
            print("Your list is empty!")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == '2':
        new_task = input("Enter the task: ")
        tasks.append(new_task)
        print("Task added!")

    elif choice == '3':
        if not tasks:
            print("Nothing to remove.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            num = int(input("Enter task number to remove: "))
            if 0 < num <= len(tasks):
                tasks.pop(num - 1)
                print("Task removed!")
            else:
                print("Invalid number.")

    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
      
