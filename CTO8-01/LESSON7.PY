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
# with open("example.txt","r") as file:
#     content=file.read()
#     print(content)
# file.read()
# with open("example.txt","a") as file:
#     file.write("\nthis will add a new line to the file")
lines=["line1\n","line2\n","line3\n"]
with open("example.txt","w") as file:
    file.writelines(lines)
    file.write("end")

