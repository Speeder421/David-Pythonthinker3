my_list= [96, 94, 99, 78, 14, 63, 73, 70, 38, 3, 53, 20, 27, 32, 89]
n = len(my_list)

for i in range(n):
    for j in range(n-1):
        if my_list[j] < my_list[j+1]:
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

print(my_list)


