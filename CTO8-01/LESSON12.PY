import os

def encrypt(letter, key):
    num=ord(letter)
    num = num + key
    if num >=127:
        num = num%95
    elif num <= 32:
        num =  num + 95
    letter=chr(num)
    return letter

def charencrypt(string, key):
    encrypted = ""
    for letter in string:
        encrypted += encrypt(letter, key)
    return encrypted

def listencrypt(string, key):
    encrypted = []
    for letter in string:
        encrypted.append(charencrypt(letter, key))
    return encrypted

def fileencrypt(filename, key):
    with open(filename, "r") as file:
        text = file.readlines()
        encrypted = []
        encrypted.append(listencrypt(text, key))
        return encrypted

filename="example.txt"
filepath=os.getcwd()
fullpath=os.path.join(filepath,filename)

def bruteforce(filename):
    start=32
    end=126
    num=end-start+1
    with open(filename, "r") as file:
        text = file.readlines()
        for line in text:
            key=79
            decrypted = []
            decrypted.append(fileencrypt(filename, -key))
            if decrypted == line:
                print("Key is: ", key)
                return decrypted
        # for key in range(1, 95):
        #     decrypted = []
        #     decrypted.append(fileencrypt(filename, -key))
        #     return decrypted
# bruteforce("text.txt")
print(fileencrypt("text.txt", -79))




def menu():
    print("Ceasar Cipher Menu:")
    print("1. Encrypt Single Sentence")
    print("2. decrypt Single Sentence")
    print("3. encrypt list of sentences")
    print("4. decrypt list of sentences")
    print("5. encrypt file")
    print("6. decrypt file")
    print("7. bruteforce")
    print("8. Exit programme")


while True:
    menu()
    choice=input("Enter your choice:")
    if choice=="1":
        string=input("Enter your string:")
        key=int(input("Enter your key:"))
        print(charencrypt(string, key))
    elif choice=="2":
        string=input("Enter your string:")
        key=int(input("Enter your key:"))
        print(charencrypt(string, -key))
    elif choice=="3":
        string=input("Enter your string:")
        key=int(input("Enter your key:"))
        print(listencrypt(string, key))
    elif choice=="4":
        string=input("Enter your string:")
        key=int(input("Enter your key:"))
        print(listencrypt(string, -key))
    elif choice=="5":
        filename=input("Enter your filename:")
        key=int(input("Enter your key:"))
        print(fileencrypt(filename, key))
    elif choice=="6":
        filename=input("Enter your filename:")
        key=int(input("Enter your key:"))
        print(fileencrypt(filename, -key))
    elif choice=="7":
        filename=input("Enter your filename:")
        print(bruteforce(filename))
    elif choice=="8":
        print("Exiting the program.")
        break
    else:
        print("There is no such action!")
