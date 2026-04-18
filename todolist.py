
def todotask(task, deadline, Status):
    data = ("Task: "+ task + " "+ "Deadline: "+ deadline+ " "+ "Status: " + Status + "\n")
    with open("info.txt", "a") as file:
        file.write(data)
def read_data():
    with open("info.txt", "r") as file:
        print("\n--- Task Update ---")
        print(file.read())
print("\n*********Welcome to TODOAPP*********")
num = 0
while num < 7:
    print("\nSelect: \n1.Add Task. \n2.View all tasks\n3.View Task By Name\n4.View Task By Status\n5. Update Task\n6. Delete Task\n7.exit" )
    num = int(input("Enter your choice: "))
    match num:
        case 1:
            task = input("Enter Task name: ").lower()
            ddate = input("Enter Deadline(eg. 30th June 2025): ").lower()
            status = input("Enter status: ").lower()
            todotask(task, ddate, status)
            print("task added  succesfully")
        case 2:
            read_data()
        case 3:
            taskn = input("Enter Task name to search: ").lower()
            found = False
            with open("info.txt", "r") as file:
                for line in file:
                    if f"Task: {taskn}" in line:
                        print("\nTask Found:\n", line.strip())
                        found = True
                        break
            if not found:
                print("Task not found.")
        case 4:
            with open("info.txt", "r") as file:
              for line in file:
                if "Status: completed" in line:
                    print("Task status:", line.strip())
                    found = True
            if not found:
                print("Work is pending..")
        case 5:
            taskl = input("Enter task name to update: ").lower()
            dl = input("Enter new deadline: ").lower()
            st = input("Enter new status: ").lower()
            updated = False
            lines = []
            with open("info.txt", "r") as file:
                for line in file:
                    if f"Task: {taskl}" in line:
                        parts = line.strip().split(" ")
                        task_name = parts[1]  #og task ho isme store kardiya
                        newline = f"Task: {task_name} Deadline: {dl} Status: {st}\n"
                        lines.append(newline)
                        updated = True
                    else:
                        lines.append(line)
            with open("info.txt", "w") as file:
                file.writelines(lines)
            if updated:
                print("Only deadline and status updated successfully.")
            else:
                print("Task not found.")
        case 6:
            delete=False
            lines=[]
            taskn = input('Enter task name for deletion: ').lower()
            with open('info.txt','r') as file:
                for line in file:
                    if f'Task: {taskn}' in line:
                        delete = True
                        continue
                    lines.append(line)
            with open("info.txt", "w") as file:
                file.writelines(lines)   
            if delete:
                print("Task deleted successfully.")
            else:
                print("Task not found.")
        case 7:print("********** Exit **********")      
        case _:print('Invalid Input')