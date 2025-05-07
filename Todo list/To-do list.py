from datetime import datetime
#Stores all the tasks
tasks = []
#Stores all the due dates
duedate = []

def addtask(tasks, duedate):
    while True:
        try:
            n_task = int(input("How many tasks do you wish to add: "))
            break
        except ValueError:
           
            print("Error: Please enter a valid number.")
    for i in range(n_task):
        task = input("Enter a task: ")
        tasks.append(task)
        while True:
            duedate_str = input("Enter a date in DD/MM/YYYY format with the slashes: ")
            try:
                date_obj = datetime.strptime(duedate_str, "%d/%m/%Y")  
                duedate.append(date_obj)
                break
            except ValueError:
                
                print("Error: Invalid date format. Please use DD/MM/YYYY.")

        print("Task", task, "added to the list Due-", duedate_str)

def showtasks(tasks, duedate):
    if not tasks:
        print("No tasks are in the list.")
    else:
        print("These are the tasks in your To-do list:")
        #lists out the tasks and their due date based on when they were added
        for i, (task, date) in enumerate(zip(tasks, duedate), 1):
            print(f"{i}. Task: {task} | Due Date: {date.strftime('%d/%m/%Y')}")
            
def edittask(tasks, duedate):
    if not tasks:
        print("No tasks available to edit.")
        return

    showtasks(tasks, duedate) 

    while True:
        try:
            task_index = int(input("Enter the task number you want to edit: ")) - 1

            if 0 <= task_index < len(tasks):
                # Get new task description 
                new_task = input("Enter the new task description (press Enter to keep unchanged): ")
                if new_task.strip():  # Only update if user enters something
                    tasks[task_index] = new_task

                # Get new due date 
                new_due_date = input("Enter the new due date in DD/MM/YYYY (press Enter to keep unchanged): ")
                if new_due_date.strip():
                    try:
                        new_due_date_obj = datetime.strptime(new_due_date, "%d/%m/%Y")
                        duedate[task_index] = new_due_date_obj  # Update due date
                    except ValueError:
                        print("Invalid date format. Keeping the old due date.")

                print("Task updated successfully!")
                break
            else:
                print("Invalid task number. Please enter a valid task number from the list.")

        except ValueError:
            print("Invalid input. Please enter a numeric value.")
def savetask(task, duedate_str):
    if not tasks:
        print("No tasks are in the list.")
    else:
        with open(r"C:\Users\garen\Documents\Project Work\Todo list\data.txt", "a") as data:
            data.write(f"Task :{task},Due:{duedate_str}\n")
def donetask(tasks, duedate):
    if not tasks:
        print("No tasks have been added.")
        return
    
    while True:
        try:
            task_index = int(input("Which one of these tasks have you done? (Enter task number): ")) - 1
            
            if 0 <= task_index < len(tasks):
                tasks.pop(task_index)
                duedate.pop(task_index)
                print("Task completed and has been removed from the list.")
                break
            else:
                print("Invalid task number. Please enter a valid task number from the list.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
def TODOLIST():
    tasks = []
    duedate = []
    while True:
        print("===========To-Do List===========")
        print("Please choose one of the following: ")
        print("1.Add a new task to the list")
        print("2.Show all tasks")
        print("3.Mark tasks as done")
        print("4.Edit task")
        print("5.Savetasks")
        print("6.Exit")

        try:
            choice = int(input("What do you want to do: "))  
        except ValueError:
            print("Error: Please enter a valid number between 1 and 5.")
            continue  

        if choice == 1:
            addtask(tasks, duedate)
        elif choice == 2:
            showtasks(tasks, duedate)
        elif choice == 3:
            donetask(tasks, duedate)
        elif choice == 4:
            edittask(tasks, duedate)
        elif choice == 5:
            savetask(tasks, duedate)
        elif choice == 6:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number from 1-5.")

TODOLIST()
