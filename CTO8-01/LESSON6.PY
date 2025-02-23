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
            if answer[]==answerkey[0]:
                scores[name].append(1)
    return scores
            


print(gradestudents(answerkey,studentanswers))





