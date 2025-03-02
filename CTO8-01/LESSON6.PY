answerkey=["A","B","B","D"]
studentanswers={
    "john":["A","C","B","D"],
    "jane":["A","B","B","D"],
    "alice":["A","C","C","D"],
    "bob":["A","B","B","D"]
}

def gradestudents(answerkey,studentanswers):
    scores={}
    for student,answer in studentanswers.items():
        score=0
        for i in range(len(answerkey)):
            if answer[i]==answerkey[i]:
                score+=1
        scores[student]=score
    return scores

def average(scores):
    total=0
    count=0
    for score in scores.values():
        count+=1
        total+=score
    average=total/count
    return average

def highestscorer(scores):
    topppl=[]
    highestscore=max(scores.values())
    for name,score in scores.items():
        if score==highestscore:
            topppl.append(name)
    return topppl

def displayscore(scores):
    print("Class results: ")
    for student,score in scores.items():
        print(f"{student}:{score}")
        

def menu():
    print("Quiz Grading System Menu")
    print("1. Grade all students")
    print("2. Calculate class avarage")
    print("3. Find highest scorer(s)")
    print("4. Display all results")
    print("5. Exit programme")
    




while True:
    menu()
    choice=input("Enter your choice:")
    if choice=="1":
        scores=gradestudents(answerkey,studentanswers)
        print("Quiz graded")
    elif choice=="2":
        print(average(gradestudents(answerkey,studentanswers)))
    elif choice=="3":
        warning=notify(students,min)
        print(f"Students with a low attendence;{warning}")
    elif choice=="4":
        print("Exiting...")
        break
    else:
        print("There is no such action!")
    

print(highestscorer(scores))
displayscore(scores)


