# To_Do_List

**Task Manager CLI Application**  
A simple command-line To-Do List manager written in Python.  
Allows you to add tasks, view all or filtered tasks (pending/completed), mark tasks as done, and delete tasks by ID.

## Features
- Add new tasks with automatic incremental IDs
- View all tasks or filter by status (*Pending* / *Done*)
- Mark tasks as completed
- Delete tasks by task ID
- User-friendly menu interface

## Requirements
- Python 3.x

## How to Run
1. Clone or download the repository.  
2. Run the Python script:
   python task_manager.py
3. Follow on-screen prompts to manage your tasks.


## Usage
Choose options from the menu by entering the corresponding number.

When adding tasks, enter the task description.

To mark or delete a task, enter the ID displayed when viewing tasks.


## Sample Interaction

1. Print Task
2. Add Task
3. Mark Task as Complete
4. Delete Task
5. Exit
Enter Choice : 2
Enter Task : Do Homework
Task Added!

Enter Choice : 1

ID : 1
Task : Do Homework
Status : Pending

Enter Choice : 3
Enter Id: 1
Task Marked as Completed!

Enter Choice : 1

ID : 1
Task : Do Homework
Status : Done


## Notes
Task IDs are auto-incremented and unique.

Tasks are stored only during the session (no persistence).
