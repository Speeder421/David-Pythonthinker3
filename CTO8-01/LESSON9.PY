import os

filename="sherlockholmes.txt"
filepath=os.getcwd()
fullpath=os.path.join(filepath,filename)


# with open(fullpath,"r") as file:
#     content=file.read()
#     print(content)
with open(fullpath,"r") as file:
        content=file.read()
        

def countchar(content):
     return len(content)
    
    
def countvowel(fullpath):
    
    vowels="aeiou"
    num=0
    for char in content.lower():
        if char in vowels:
            num+=1
    return num


def countfrequency(content):
    vowels={"a":0,"e":0,"i":0,"o":0,"u":0}
    for char in content.lower():
        if char in vowels:
            vowels[char]+=1
    return vowels

             
def count_percent(total,vowel):
     count=(vowel/total)*100
     return round(count,2)

         
def createfile(fullpath):
    with open("results.txt","w") as file:
        file.write("Text Analysis(Sherlock Holmes)\n")
        file.write(f"Total Characters: {countchar(content)}\n")
        file.write(f"Total Vowels: {countvowel(content)}\n")
        file.write("Vowel Frequency:\n")
        for key,value in countfrequency(content).items():
           file.write(f"{key} = {value}\n")
        file.write(f"Percentage of vowels in text: {count_percent(countchar(content),countvowel(content))}%")
         
    


createfile(fullpath)
with open("results.txt","r") as file:
    value=file.read()
    print(value)