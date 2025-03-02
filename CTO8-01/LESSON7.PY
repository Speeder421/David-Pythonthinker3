import os
# filepath=os.getcwd()
# fullpath=os.path.join(filepath,"example.txt")
# if os.path.exists(fullpath):
#     print("exists")
# else:
#     print("it does not exist")
# print(filepath)
# file=open("example.txt","w")
# file.write("hi i am a boy")
# file.close()  
# file=open("example.txt","r")
# content=file.read()
# print(content)
# file.close()    
with open("example.txt","r") as file:
    content=file.read()
    
