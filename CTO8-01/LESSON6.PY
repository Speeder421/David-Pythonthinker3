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
    for score in scores.value():
        score+=total
    total/len



print(gradestudents(answerkey,studentanswers))





