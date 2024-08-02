
# it add tasks to tasks list
def addtask(tasks):
    n=int(input("Enter how many tasks you  want to add : "))

    for i in range(n):
        task =input("enter task: ")
        tasks.append( {"task":task,"done":False})
        print("!task added")
    print("\n")

#i removes tasks from task list
def deletetask(tasks):
    if not tasks :
        print("No tasks to delete")
        print("\n")
    else :   
        showtask()
        task_no = int(input("Enter which task you wants to delete:" ))
        if (0 <= task_no and task_no <=len(tasks)):
            tasks.pop((task_no-1))
            print("succesfully deleted task")
    
        else:

            print("No such task")
            s=input("if you want to delete another task( yes or no) ")
            if s== "yes":
                deletetask(tasks)
        print("\n")

# it displays tasks
def showtask():
    if not  tasks: 
        print("No tasks in the list ")
    else:
        for index ,i in enumerate(tasks):
            status = "Done" if i["done"] else "Not done"
            print(f"{index+1}.{i['task']}-{status}")
        print("\n")
        return tasks
            
#Mark tasks as done 
def  marktask(tasks):
    if not tasks :
        print("No tasks to mark")
        print("\n")
    else :
        showtask()#it's shows list of tasks
        task_index = int(input("Enter which task you want to mark done: "))
        if (0 <= task_index and task_index <=len(tasks)):
            task_i =task_index-1
            tasks[task_i]["done"] = True

            print("succesfully marked task")
        else:
            print("No such task")
            s=input("if you want to mark another task( yes or no) ")
            if s== "yes":
                marktask(tasks)
        print("\n")

#it's start exceution from this part
print("         ******WELCOME TO DO LIST*******")
tasks= []
while True:# for running multiple times
    print("1.Add Task")
    print("2.Delete Task")
    print("3.show tasks")
    print("4.To mark-done")
    print("5.quit")
    choice = input("Enter your choice : ")
    if choice == '1':
        addtask(tasks)
    elif choice == '2':
        deletetask(tasks)
    elif choice == '3':
        showtask()
    elif choice == '4' :
        marktask(tasks)
    elif choice =='5' :
        print("     ****THANK YOU****")
        break
    else:
        print("Enter valid option")
