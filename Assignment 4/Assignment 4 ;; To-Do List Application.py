"""Develop a simple to-do list application using Python and object-oriented programming (OOP) concepts. 
The application should allow users to add tasks, edit tasks, mark tasks as completed, and view the list of tasks.
 - Add Task: Users should be able to add tasks to the to-do list by providing a task description 
        and priority level. 

- Edit Tasks: Users should be able to edit description and priority of tasks in this section 

- Mark Task as Completed: Users should be able to mark tasks as completed. Once completed,
     tasks should be visually distinguished from incomplete tasks by displaying its status 
     
- View Tasks: Users should be able to view the list of tasks, including their descriptions, priorities, 
    and completion status. 
    
You are expected to implement the application using at least one class for managing your To-Do List Application.
 Make sure to incorporate proper error handling to handle invalid user inputs gracefully.
"""


class ToDoList:
    def __init__(self):
        self.tasks = []  

    def add_task(self):
        name = input("Task Name: ")
        desc = input("Task Description: ")
        priority = input("Priority (High/Medium/Low): ").capitalize()

        if priority not in ["High", "Medium", "Low"]:
            print("Invalid , Only Use High or Medium or Low.")
            return

        self.tasks.append([name, desc, priority, "pending"])
        print("Task added ")

    def edit_task(self):
        name = input("Enter task name to edit : ")
        for task in self.tasks:
            if task[0].lower() == name.lower():
                task[0] = input("New Task Name: ")
                task[1] = input("New Task Description: ")
                priority = input("New Priority (High/Medium/Low): ").capitalize()
                if priority not in ["High", "Medium", "Low"]:
                    print("Invalid priority! Edit cancelled.")
                    return
                task[2] = priority
                print("Task updated!")
                return
        print("Task not found!")

    def status(self):
        name = input("Enter the completed task name : ")
        for task in self.tasks:
            if task[0].lower() == name.lower():
                task[3] = "completed"
                print("Task marked as completed!")
                return
        print("Task not found!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks to show.")
            return
        count = 1
        for task in self.tasks:
            print(f"{count}. Name: {task[0]} | Description: {task[1]} | Priority: {task[2]} | Status: {task[3]}")
            count += 1

todo = ToDoList()

while True:
    print("\n1. Add Task")
    print("2. Edit Task")
    print("3. Mark Task as Completed")
    print("4. View Tasks")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        todo.add_task()
    elif choice == "2":
        todo.edit_task()
    elif choice == "3":
        todo.status()
    elif choice == "4":
        todo.view_tasks()
    elif choice == "5":
        print("Good Bye !!!")
        break
    else:
        print("Invalid choice.")




















