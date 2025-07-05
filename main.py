FILENAME = "tasks.txt"

# Load existing tasks from file
tasks = []
try:
    with open(FILENAME, "r") as file:
        tasks = [line.strip() for line in file.readlines()]
except FileNotFoundError:
    tasks = []

def main():
    while True:
        print("\n1. Log a Task")
        print("2. View log")
        print("3. Remove a completed task")
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Add a new task: ").strip()

            if task:
                tasks.append(task)

                # Save after adding
                with open(FILENAME, "w") as file:
                    for t in tasks:
                        file.write(t + "\n")
            else:
                print("Task cannot be empty.")

        elif choice == "2":
            if tasks:
                print("\nYour tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
            else:
                print("No tasks logged yet.")

        elif choice == "3":
            if tasks:
                print("\nWhich task is complete?")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")

                try:
                    remove_index = int(input("Task number: ")) - 1
                    if 0 <= remove_index < len(tasks):
                        removed = tasks.pop(remove_index)
                        print(f"Removed: {removed}")

                        # Save after removing
                        with open(FILENAME, "w") as file:
                            for t in tasks:
                                file.write(t + "\n")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("No tasks to remove.")

        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

