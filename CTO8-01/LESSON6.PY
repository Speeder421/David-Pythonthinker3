answerkey=["A","B","B","D"]
studentanswers={
    "john":["A","C","B","D"],
    "jane":["A","B","B","D"],
    "alice":["A","C","C","D"],
    "bob":["A","B","B","D"]
}

def gradestudents(answerkey,studentanswers):
    scores={}
    for name,answer in studentanswers.items():
        for i in answer:
            if answer[0]==answerkey[0]:
                scores[name].append(1)
    return scores
            


print(gradestudents(answerkey,studentanswers))





