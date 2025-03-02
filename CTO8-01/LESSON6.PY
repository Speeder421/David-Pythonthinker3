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
    for student,score in scores.items():
        print("student:")
        


scores=gradestudents(answerkey,studentanswers)
print(average(gradestudents(answerkey,studentanswers)))
print(highestscorer(scores))



