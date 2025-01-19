# students={
#     "john":56,
#     "sam":99,
#     "sara":65
# }
# print(students["john"])
# students["samantha"]=100
# print(students)
# students["john"]=50
# print(students)
# del students["john"]
# print(students)
# if "bob" in students:
#     print("True")
# for i in students:
#     print(i)
#     break
# for name in students:
#     grade=students[name]
#     print(name,grade)\
#Three methods in dictionaries
# students.keys()
# students.value()
# students.items()
# for name,grade in students.items():
#     print(name,grade)
item={
    "cheesburger":5.50,
    "double bacon burger":7.90,
    "french fries":2.80,
    "cheese fries":3.00,
    "chocolate sundae":3.20,
    "apple pie":2.00,
    "coke":1.50
}
def show_menu(item):
    print("******Welcome to HanBAoBAo restaraunt!******")
    print("***This is our menu***")
    for food,price in item.items():
        print(f"{food} :$ {price:.2f}")
    print("***This is the end of the menu***")
    




show_menu(item)