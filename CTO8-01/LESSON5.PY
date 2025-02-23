

def takeattendence(students):
    print("We will be taking attendence now!")
    for student in students.keys():
        while True:
            a=input(f"Is {student} present? y/n:")
            if a=="y":
                students[student].append(True)
                break
            elif a=="n":
                students[student].append(False)
                break
            else:
                print("This is not an accepted response!")
            print("Attendence has been taken!")
    return students
      

def percentage(students,student):
    attend=0
    count=0
    for attendence in students[student]:
        if attendence:
            attend+=1
            count+=1
        else:
            count+=1
    percent=(attend/count)*100
    return percent

def notify(students,min):
    low=[]
    for name,attend in students.items():
        attendence=(percentage(students,name))
        if attendence<min:
            low.append(name)
            print(f"Warning! {name} has a low attendence of {attendence}!")
    return low


students={
    "john":[True,False,True],
    "sam":[False,True,False],
    "tom":[True,True,True],
    "bob":[False,False,False]
}
def menu():
    print("School attendence system")
    print("1. Take attendence")
    print("2. Calculate attendence percentage for a student")
    print("3. Notify low attendence")
    print("4. Exit programme")
    



min=50.0
while True:
    menu()
    choice=input("Enter your choice:")
    if choice=="1":
        updatedstudents=takeattendence(students)
        p
    elif choice=="2":
        student=input("Whose attendence would you like to check?")
        print(percentage(students,student))
    elif choice=="3":
        warning=notify(students,min)
        print(f"Students with a low attendence;{warning}")
    elif choice=="4":
        print("Exiting...")
        break
    else:
        print("There is no such action!")
    




