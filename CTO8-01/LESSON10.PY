import os
filename="nullcypher.txt"
filepath=os.getcwd()
fullpath=os.path.join(filepath,filename)



with open(fullpath,"r") as file:
    content=file.read()
    print(content)




