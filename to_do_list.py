#Creating an Advanced TO-DO List app in a command-line-based interface in Python.
import json
from datetime import datetime

tasks = []


#Load tasks from a file
def loadTask(clear_previous=True):
    global tasks
    if clear_previous:
        # Clear tasks list and reset file
        tasks = []
        with open("tasks.json", "w") as file:
            json.dump(tasks, file, indent=4)
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []


#Save tasks to a file
def saveTask():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)


#Add a new task
def addTask():
    title = input("\nEnter a task: ")
    category = input("Enter the category (eg. Work, Personal, Urgent): ")
    due_date = input("Enter the due date (YYYY-MM-DD) or leave blank: ")
    priority = input("Enter the priority (High, Medium, Low): ")

    task = {
        "title": title,
        "category": category,
        "due_date": due_date,
        "priority": priority.capitalize(),
        "completed": False,
    }
    tasks.append(task)
    saveTask()
    print(f"Task '{task}' is added to the list.")


#List all the tasks
def listTask():
    if not tasks:
        print("\nNo tasks available in the list!")
        return
    
    print("\nCurrent Tasks: ")
    print("-" * 50)
    for index, task in enumerate(tasks, start=1):
        status = "✔️ Completed" if task["completed"] else "❌ Not Completed"
        print(f"Task {index}. {task['title']} [{task['category']}] (Due: {task['due_date']}) - {status} (Priority: {task['priority']})")


#Delete a task
def deleteTask():
    if not tasks:
        print("\nNo tasks to delete.")
        return
    
    listTask()
    try:
        task_num = int(input("\nEnter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            deleted_task = tasks.pop(task_num - 1)
            saveTask()
            print(f"Task '{deleted_task['title']}' deleted.")
        else:
            print("Invalid task number!")
    
    except ValueError:
        print("Invalid input! Please enter correct task number.")


#Mark a task as completed
def markTaskCompleted():
    if not tasks:
        print("\nNo tasks to mark as completed in the list.")
        return
    
    listTask()
    try:
        task_num = int(input("\nEnter the task number to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            task = tasks[task_num - 1]
            if not task["completed"]:
                task["completed"]= True
                saveTask()
                print(f"Task '{task['title']} has been marked as completed!")
            else:
              print(f"Task '{tasks['title']} is already completed!")
        else:
            print("Invalid task number.")
   
    except ValueError:
        print("Invalid input! Please enter a valid task number.")
    listTask()


#Search a task in the list
def searchTask():
    query = input("\nEnter search query (title or category): ").lower()
    results = [task for task in tasks if query in task["title"].lower() or query in task["category"].lower()]
    if results:
        print("\nSearch Results:")
        for idx, task in enumerate(results, start=1):
            status = "✔️ Completed" if task["completed"] else "❌ Not Completed"
            print(f"{idx}. {task['title']} [{task['category']}] - {status}")
    else:
        print("No matching tasks found.") 


#Main menu
if __name__ == "__main__":
    #Load tasks from a file
    loadTask()      
    #Create a loop to run the app
    print("\n")
    print("Welcome to the Advanced TO-DO List app! :)")
    while True:
        print("\n")
        print("Please select the following choice from the following")
        print("-----------------------------------------------------")
        print("1. Add a new task.")
        print("2. List task.")
        print("3. Delete a task.")
        print("4. Mark task as completed.")
        print("5. Search tasks.")
        print("6. Exit.")

        choice = input("Enter your choice: ")

        if(choice == '1'):
            addTask()
        elif(choice == '2'):
            listTask()
        elif(choice == '3'):
            deleteTask()
        elif(choice == '4'):
            markTaskCompleted()
        elif(choice == '5'):
            searchTask()
        elif(choice == '6'):
            saveTask()
            break
        else:
            print("\nInvalid choice! Please select the correct choice.")

    print("\nThankYou! :)")