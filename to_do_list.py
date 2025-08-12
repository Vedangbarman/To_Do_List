task = []
task_counter = 1

def Create_Task():
    global task_counter 

    task_input = input("Enter Task :")
    task.append({"ID" :task_counter , "Task" : task_input, "Status" : "Pending"}) #Storing Values as dictionary nesting it in list

    task_counter += 1 #Increment the flag
    print("Task Added!")

def Print_Task():
    print(''' 
1. Print All
2. Print Incomplete Task
3. Print Complete Task
4. Exit''')
    ch = int(input("Enter Choice :"))
    if ch == 1:
        if len(task) == 0:
            print("No Task !")
        else:
            for t in task:
                for key, value in t.items():
                    print(key, ":", value)
                print()  # blank line between tasks
    elif ch == 2:
        for pending in task:
            if pending["Status"] == "Pending":
                for key, value in pending.items():
                    print(key, ":", value)
                print()
    elif ch == 3:
        for done in task:
            if done["Status"] == "Done":
                for key, value in done.items():
                    print(key, ":", value)
                print()
    elif ch == 4:
        return


def mark_as_done():
    if len(task) == 0:
        print("No Task!")
        return  

    mark = int(input("Enter Id: "))
    for t in task:
        if t["ID"] == mark:
            if t["Status"] == "Done":
                print("Task Already Completed")
            else:
                t["Status"] = "Done"
                print("Task Marked as Completed!")
            return  # stop here so "Id Not Found" doesn't run

    print("Id Not Found")




def deleted_task():
    if len(task) == 0:
        print("No Task to Delete")
        return  

    mark = int(input("Enter Id: "))
    for t in task:
        if t['ID'] == mark:
            task.remove(t)
            print("Task Deleted!")
            return  

    else :
        print("Id not found")

    

while True:
    print(''' 
1. Print Task
2. Add Task
3. Mark Task as Complete
4. Delete Task
5. Exit''')
    
    choice = int(input("Enter Choice :"))
    if choice == 1:
        Print_Task()
    elif choice == 2:
        Create_Task()

    elif choice == 3:
        mark_as_done()
    
    elif choice == 4:
        deleted_task()
    
    elif choice == 5:
        break

    else:
        print('Invaild Choice!')

    

