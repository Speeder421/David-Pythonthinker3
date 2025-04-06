import os

filename="tasks.txt"
filepath=os.getcwd()
fullpath=os.path.join(filepath,filename)

def createfile(fullpath):
    if os.path.exists(fullpath):
        print("file allready exists.")
        option=input("Do you want to overwrite the current file?y/n:")
        if option =="y":
            print("creating file now...")
            with open("tasks.txt", 'w') as file:
                file.write("My Task List:")
        else:
            pass
    else:
        print("creating file now...")
        with open("tasks.txt", 'w') as file:
            file.write("My Task List:")

def addfile(fullpath):
    add=input("Enter a new task:")
    with open(fullpath,"a") as file:
        file.write(f"\n{add}")



def readfile(fullpath):
    with open(fullpath,"r") as file:
        content=file.readlines()
    if len(content)<2:
        print("no tasks found")
        return[]
    for i in range(len(content)):
        if i ==0:
            print(content[i].strip())
        else:
            print(f"{i}. {content[i]}".strip())
    return content

def markfile(fullpath):
    tasks=readfile(fullpath)
    if len(tasks)<=1:
        print("No tasks available to mark!")
        return
    else:
        choice=input("choose the number corresponding to the task that is done:")
        # if int(choice)<=1 or int(choice) >len(tasks)-1:
        #     print("Invalid number...")
        if "[DONE]" in tasks[int(choice)]:
            print("Task already finished")
        else:
            tasks[int(choice)]=tasks[int(choice)].strip()+"[DONE]\n"
    with open(fullpath,"w") as file:        
        file.writelines(tasks)


def delfile(fullpath):
    tasks=readfile(fullpath)
    if len(tasks)<=1:
        print("No tasks available to delete!")
        return
    else:
        choice=input("choose the number corresponding to the task that you want to delete:")
        choice2=int(choice)
        # if int(choice)<=1 or int(choice) >len(tasks)-1:
        #     print("Invalid number...")
        if tasks[choice2] not in tasks:
            print("Task not found")
        else:
            deltaks=tasks.pop(choice2)
    with open(fullpath,"w") as file:        
        file.writelines(tasks)
        print (tasks)



def menu():
    print("Tasklist control:")
    print("1. Create new task file")
    print("2. View all tasks")
    print("3. Add new task")
    print("4. Mark task as done")
    print("5. Delete task")
    print("6. Exit programme")


while True:
    menu()
    choice=input("Enter your choice:")
    if choice=="1":
        createfile(fullpath)
    elif choice=="2":
        readfile(fullpath)
    elif choice=="3":
        addfile(fullpath)
    elif choice=="4":
        markfile(fullpath)
    elif choice=="5":
        delfile(fullpath)
    elif choice=="6":
        print("Exiting programme...")
        break
    else:
        print("There is no such action!")
    






