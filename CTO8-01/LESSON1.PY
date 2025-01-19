# def is_ascending(item):
#     for i in range(len(item)-1):
#         if item[i]>=item[i+1]:
#             return False
#     return True
# list=[1,2,3,4,5]
# is_ascending(list)
# print(is_ascending(list))
list=[9,6,3,25,21,8,23,1,17,14]
n=len(list)
def bubble_sort(numbers):
    for i in range(n):
        for j in range(0,n-o,-1):
            if numbers[i]>numbers[i+1]:
                item=numbers[i+1]
                numbers[i+1]=numbers[i]
                numbers[i]=item
        return numbers
ordered=bubble_sort(list) # you never assign to a variable
print(ordered)