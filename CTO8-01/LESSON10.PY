import os
import string
filename="nullcypher.txt"
filepath=os.getcwd()
fullpath=os.path.join(filepath,filename)



with open(fullpath,"r") as file:
    content=file.read()
punctuations=string.punctuation
content=content.lower()
for i in punctuations:
    if i in content:
        content=content.replace(i,"")
# print(content)
words=content.split()
msg=""
for i in words:
    if len(words)>0:
        msg+=words[0]
    
print(msg)






