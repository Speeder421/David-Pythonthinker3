import random,string

def generatepass(length=12):
    count=0
    password=""
    upletters=string.ascii_uppercase
    loletters=string.ascii_lowercase
    symbols=string.punctuation
    for i in range(int(length)):
        num=random.randint(1,4)
        if num == 1:
            word=random.randint(65,90)
        elif num==2:
            word=random.randint(97,122)
        elif num ==3:
            word=random.randint(48,57)
        else:
            word=random.randint(33,47)
        password+=chr(word)
    if len(password)>=12:
        count+=1
        pass
    for i in upletters: #ABC...
        if i in password: # A in password?, B in password?
            count+=1
            break
    for j in loletters:
        if j in password:
            count+=1
            break
    for u in symbols:
        if u in password:
            count+=1
            break
    if count==4:
        print("Password generated!")
        return password
    else:
        print("Password invalid!")
        return None

passwords={}
def create_new_user(passwords):
    name=input("Please input a name:").lower()
    
    if name in passwords:
        print("user already generated pass.")
        return None

    else:
        length=input("How long will your password be?")
        passw=generatepass(length)
        print(f"{name} : {passw}")
        passwords[name]=passw
        print(passwords)
        return passwords
    
def updatepass(passwords):
    name=input("enter your username:").lower()
    if name in passwords:
        passw=input("Enter your password:")
        if passw==passwords[name]:
            num=input("How long will your password be?")
            newpass=generatepass(num)
            passwords[name]=newpass
            print(newpass)
            print(passwords)
            return passwords
        else:
            print("Access denied!")
            return None
    else:
        print("Access denied!")
        return None

def login(passwords):
    name=input("enter your username:").lower()
    if name in passwords:
        passw=input("Enter your password:")
        if passw==passwords[name]:
            return True
        else:
            print("Access denied!")
            return False
    else:
        print("Access denied!")
        return False

def view_data(passwords):
    for key,value in passwords.items():
        print(f"{key}:{"*"* len(value)}")


def menu():
    print("Password database control:")
    print("1. Create new user")
    print("2. update password")
    print("3. login")
    print("4. view all usernames and passwords")
    print("5. Exit programme")


while True:
    menu()
    choice=input("Enter your choice:")
    if choice=="1":
        create_new_user(passwords)
    elif choice=="2":
        updatepass(passwords)
    elif choice=="3":
        login(passwords)
    elif choice=="4":
        view_data(passwords)
    elif choice=="5":
        print("Exiting programme...")
        break
    else:
        print("There is no such action!")
